"""Phase 3 generator: build cross-system interaction pages from extracted references."""

from __future__ import annotations

import json
import os
import re
from collections import defaultdict
from itertools import combinations
from typing import Any

import scripts.config as config


MANUAL_BLOCK_RE = re.compile(
    r"(<!-- MANUAL:START -->)(.*?)(<!-- MANUAL:END -->)",
    re.DOTALL,
)


def _read_json(path: str, warnings: list[str]) -> dict[str, Any] | None:
    """Read JSON file with graceful error handling."""
    if not os.path.exists(path):
        warnings.append(f"Missing required input file: {path}")
        return None
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, dict):
            return data
        warnings.append(f"Expected JSON object in {path}, got {type(data).__name__}.")
        return None
    except (OSError, json.JSONDecodeError) as exc:
        warnings.append(f"Failed to read {path}: {exc}")
        return None


def _slugify(name: str) -> str:
    """Convert system name to deterministic filename-safe slug."""
    slug = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
    return slug or "system"


def _display_name(meta: dict[str, Any]) -> str:
    """Pick a stable display name for a system."""
    for key in ("system_name", "class_name", "name"):
        value = meta.get(key)
        if isinstance(value, str) and value.strip():
            return value.strip()
    file_path = str(meta.get("file", ""))
    base = os.path.splitext(os.path.basename(file_path))[0]
    return base or "unknown_system"


def _collect_systems(manifest: dict, systems_doc: dict[str, Any]) -> list[dict[str, str]]:
    """Build system records from manifest and systems.json metadata."""
    by_file: dict[str, dict[str, Any]] = {}
    for section in ("systems", "ai_modules"):
        for entry in manifest.get(section, []):
            path = entry.get("file")
            if isinstance(path, str) and path.endswith(".gd"):
                by_file[path] = dict(entry)

    for entry in systems_doc.get("systems", []):
        path = entry.get("file")
        if isinstance(path, str) and path.endswith(".gd"):
            merged = dict(by_file.get(path, {}))
            merged.update(entry)
            by_file[path] = merged

    systems: list[dict[str, str]] = []
    for path, meta in by_file.items():
        name = _display_name(meta)
        systems.append(
            {
                "file": path,
                "name": name,
                "slug": _slugify(name),
                "module": os.path.splitext(os.path.basename(path))[0],
            }
        )

    return sorted(systems, key=lambda item: (item["name"], item["file"]))


def _format_access(accesses: set[str]) -> str:
    """Render entity field access set to compact label."""
    if "read" in accesses and "write" in accesses:
        return "read/write"
    if "write" in accesses:
        return "write"
    if "read" in accesses:
        return "read"
    return "-"


def _escape_cell(text: str) -> str:
    """Escape markdown table-special pipes."""
    return text.replace("|", "\\|")


def _preserve_manual(existing_text: str, new_text: str) -> str:
    """Preserve MANUAL block content from existing markdown when overwriting."""
    existing_match = MANUAL_BLOCK_RE.search(existing_text)
    new_match = MANUAL_BLOCK_RE.search(new_text)
    if not existing_match or not new_match:
        return new_text
    manual_content = existing_match.group(2)
    return MANUAL_BLOCK_RE.sub(
        lambda match: f"{match.group(1)}{manual_content}{match.group(3)}",
        new_text,
        count=1,
    )


def _write_markdown(path: str, content: str, warnings: list[str]) -> bool:
    """Write markdown with MANUAL block preservation."""
    final_content = content
    if os.path.exists(path):
        try:
            with open(path, "r", encoding="utf-8") as f:
                existing = f.read()
            final_content = _preserve_manual(existing, content)
        except OSError as exc:
            warnings.append(f"Failed to read existing markdown {path}: {exc}")

    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(final_content)
        return True
    except OSError as exc:
        warnings.append(f"Failed to write markdown {path}: {exc}")
        return False


def _filename_for_pair(left: dict[str, str], right: dict[str, str], taken: set[str]) -> str:
    """Build alphabetical pair filename from system names with collision handling."""
    base = f"{left['slug']}-{right['slug']}.md"
    if base not in taken:
        taken.add(base)
        return base
    suffix = 2
    while True:
        candidate = f"{left['slug']}-{right['slug']}-{suffix}.md"
        if candidate not in taken:
            taken.add(candidate)
            return candidate
        suffix += 1


def _build_interactions(
    systems: list[dict[str, str]],
    references: dict[str, Any],
    warnings: list[str],
) -> list[dict[str, Any]]:
    """Construct interaction records for every system pair with >=1 interaction type."""
    system_files = {system["file"] for system in systems}
    system_by_file = {system["file"]: system for system in systems}

    imports_by_file: dict[str, set[str]] = defaultdict(set)
    import_lines: dict[tuple[str, str], list[int]] = defaultdict(list)
    for row in references.get("imports", []):
        source = row.get("from_file")
        target = row.get("to_file")
        line = row.get("line")
        if source in system_files and isinstance(target, str):
            imports_by_file[source].add(target)
            if isinstance(line, int):
                import_lines[(source, target)].append(line)

    config_by_file: dict[str, set[str]] = defaultdict(set)
    config_lines: dict[tuple[str, str], list[int]] = defaultdict(list)
    for row in references.get("config_refs", []):
        source = row.get("file")
        constant = row.get("constant")
        line = row.get("line")
        if source in system_files and isinstance(constant, str):
            config_by_file[source].add(constant)
            if isinstance(line, int):
                config_lines[(source, constant)].append(line)

    field_access: dict[str, dict[str, set[str]]] = defaultdict(
        lambda: defaultdict(set)
    )
    field_lines: dict[tuple[str, str], list[int]] = defaultdict(list)
    for row in references.get("entity_field_access", []):
        source = row.get("file")
        field = row.get("field")
        access_type = row.get("access_type")
        line = row.get("line")
        if source in system_files and isinstance(field, str) and isinstance(access_type, str):
            field_access[source][field].add(access_type)
            if isinstance(line, int):
                field_lines[(source, field)].append(line)

    signal_rows: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    for row in references.get("signals", []):
        signal_name = row.get("signal_name")
        emitter = row.get("emitter")
        emitter_line = row.get("emitter_line")
        if signal_name is None or emitter not in system_files:
            continue
        subscribers = row.get("subscribers", [])
        if not isinstance(subscribers, list):
            continue
        for subscriber in subscribers:
            if not isinstance(subscriber, dict):
                continue
            consumer = subscriber.get("file")
            consumer_line = subscriber.get("line")
            if consumer in system_files and consumer != emitter:
                key = tuple(sorted((emitter, consumer)))
                signal_rows[key].append(
                    {
                        "signal_name": str(signal_name),
                        "from_file": emitter,
                        "to_file": consumer,
                        "emitter_line": emitter_line,
                        "subscriber_line": consumer_line,
                    }
                )

    module_to_files: dict[str, list[str]] = defaultdict(list)
    for system in systems:
        module_to_files[system["module"]].append(system["file"])

    call_rows: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    for row in references.get("cross_system_calls", []):
        source = row.get("from_file")
        to_module = row.get("to_module")
        function_name = row.get("function")
        line = row.get("line")

        if source not in system_files or not isinstance(to_module, str):
            continue

        candidates = sorted(set(module_to_files.get(to_module, [])))
        if len(candidates) > 1:
            warnings.append(
                f"Ambiguous cross-system call target '{to_module}' from {source}; skipped."
            )
            continue
        if not candidates:
            continue

        target = candidates[0]
        if target == source:
            continue

        key = tuple(sorted((source, target)))
        call_rows[key].append(
            {
                "from_file": source,
                "to_file": target,
                "function": str(function_name or ""),
                "line": line,
            }
        )

    interactions: list[dict[str, Any]] = []
    taken_filenames: set[str] = set()
    for left, right in combinations(systems, 2):
        left_file = left["file"]
        right_file = right["file"]
        pair_key = tuple(sorted((left_file, right_file)))

        shared_imports = sorted(imports_by_file[left_file] & imports_by_file[right_file])
        shared_configs = sorted(config_by_file[left_file] & config_by_file[right_file])
        shared_fields = sorted(
            set(field_access[left_file].keys()) & set(field_access[right_file].keys())
        )
        signals = sorted(
            signal_rows.get(pair_key, []),
            key=lambda row: (row["signal_name"], row["from_file"], row["to_file"]),
        )
        direct_calls = sorted(
            call_rows.get(pair_key, []),
            key=lambda row: (row["from_file"], row["to_file"], row["function"], row["line"]),
        )

        interaction_types: list[str] = []
        if shared_imports:
            interaction_types.append("shared_dependencies")
        if signals:
            interaction_types.append("signal_flow")
        if shared_fields:
            interaction_types.append("shared_entity_fields")
        if direct_calls:
            interaction_types.append("direct_calls")

        if not interaction_types:
            continue

        interaction = {
            "left": left,
            "right": right,
            "shared_imports": shared_imports,
            "shared_configs": shared_configs,
            "shared_fields": shared_fields,
            "signals": signals,
            "direct_calls": direct_calls,
            "interaction_types": interaction_types,
            "strength": len(interaction_types),
            "filename": _filename_for_pair(left, right, taken_filenames),
            "import_lines": import_lines,
            "config_lines": config_lines,
            "field_lines": field_lines,
            "field_access": field_access,
            "system_by_file": system_by_file,
        }
        interactions.append(interaction)

    interactions.sort(
        key=lambda row: (
            -row["strength"],
            row["left"]["name"],
            row["right"]["name"],
        )
    )
    return interactions


def _interaction_summary(interaction: dict[str, Any]) -> str:
    """Render brief summary sentence for interaction page."""
    left_name = interaction["left"]["name"]
    right_name = interaction["right"]["name"]
    labels = {
        "shared_dependencies": "shared dependencies",
        "signal_flow": "signal flow",
        "shared_entity_fields": "shared entity fields",
        "direct_calls": "direct calls",
    }
    type_text = ", ".join(labels[t] for t in interaction["interaction_types"])
    summary = (
        f"`{left_name}` and `{right_name}` interact through "
        f"{interaction['strength']} connection types: {type_text}."
    )
    if interaction["shared_configs"]:
        summary += (
            f" They also share {len(interaction['shared_configs'])} "
            "GameConfig constant reference(s)."
        )
    return summary


def _build_pair_markdown(interaction: dict[str, Any], nav_order: int) -> str:
    """Render one pair interaction page markdown."""
    left = interaction["left"]
    right = interaction["right"]
    left_name = left["name"]
    right_name = right["name"]
    left_file = left["file"]
    right_file = right["file"]

    field_access = interaction["field_access"]
    shared_field_rows = []
    for field in interaction["shared_fields"]:
        left_access = _format_access(field_access[left_file][field])
        right_access = _format_access(field_access[right_file][field])
        shared_field_rows.append(
            f"| `{_escape_cell(field)}` | {_escape_cell(left_access)} | {_escape_cell(right_access)} |"
        )
    if not shared_field_rows:
        shared_field_rows.append("| (none) | - | - |")

    signal_lines = []
    for row in interaction["signals"]:
        emitter_name = interaction["system_by_file"][row["from_file"]]["name"]
        consumer_name = interaction["system_by_file"][row["to_file"]]["name"]
        signal_lines.append(
            f"- `{row['signal_name']}` -> emitted by `{emitter_name}` -> consumed by `{consumer_name}`"
        )
    if not signal_lines:
        signal_lines.append("- None")

    shared_dependency_lines = []
    for dep in interaction["shared_imports"]:
        shared_dependency_lines.append(f"- Both import `{dep}`")
    for constant in interaction["shared_configs"]:
        shared_dependency_lines.append(f"- Both reference `GameConfig.{constant}`")
    if not shared_dependency_lines:
        shared_dependency_lines.append("- None")

    direct_call_lines = []
    for row in interaction["direct_calls"]:
        caller = interaction["system_by_file"][row["from_file"]]["name"]
        callee = interaction["system_by_file"][row["to_file"]]["name"]
        function_name = row["function"] or "(unknown)"
        direct_call_lines.append(
            f"- `{caller}` directly calls `{callee}.{function_name}()`"
        )
    if not direct_call_lines:
        direct_call_lines.append("- None")

    mermaid_lines = [
        "```mermaid",
        "graph LR",
        f"  A[{left_name}]",
        f"  B[{right_name}]",
        "  E[(Entity)]",
    ]
    for row in interaction["signals"]:
        if row["from_file"] == left_file:
            source_node = "A"
            target_node = "B"
        else:
            source_node = "B"
            target_node = "A"
        label = row["signal_name"].replace("|", "/")
        mermaid_lines.append(f"  {source_node} -->|{label}| {target_node}")
    for field in interaction["shared_fields"]:
        left_access = _format_access(field_access[left_file][field])
        right_access = _format_access(field_access[right_file][field])
        if left_access != "-":
            mermaid_lines.append(
                f"  A -->|{left_access} {field.replace('|', '/')}| E"
            )
        if right_access != "-":
            mermaid_lines.append(
                f"  B -->|{right_access} {field.replace('|', '/')}| E"
            )
    for row in interaction["direct_calls"]:
        label = f"calls {row['function']}()".replace("|", "/")
        if row["from_file"] == left_file:
            source_node = "A"
            target_node = "B"
        else:
            source_node = "B"
            target_node = "A"
        mermaid_lines.append(f"  {source_node} -->|{label}| {target_node}")
    if len(mermaid_lines) == 5:
        mermaid_lines.append("  A --- B")
    mermaid_lines.append("```")

    source_refs: set[tuple[str, int]] = set()
    for dep in interaction["shared_imports"]:
        for file_path in (left_file, right_file):
            for line in interaction["import_lines"].get((file_path, dep), []):
                if isinstance(line, int):
                    source_refs.add((file_path, line))
    for constant in interaction["shared_configs"]:
        for file_path in (left_file, right_file):
            for line in interaction["config_lines"].get((file_path, constant), []):
                if isinstance(line, int):
                    source_refs.add((file_path, line))
    for field in interaction["shared_fields"]:
        for file_path in (left_file, right_file):
            for line in interaction["field_lines"].get((file_path, field), []):
                if isinstance(line, int):
                    source_refs.add((file_path, line))
    for row in interaction["signals"]:
        if isinstance(row.get("emitter_line"), int):
            source_refs.add((row["from_file"], row["emitter_line"]))
        if isinstance(row.get("subscriber_line"), int):
            source_refs.add((row["to_file"], row["subscriber_line"]))
    for row in interaction["direct_calls"]:
        if isinstance(row.get("line"), int):
            source_refs.add((row["from_file"], row["line"]))

    source_lines = [
        f"- 📄 source: `{path}:L{line}`"
        for path, line in sorted(source_refs, key=lambda item: (item[0], item[1]))
    ]
    if not source_lines:
        source_lines = ["- 📄 source: `(none)`"]

    return "\n".join(
        [
            "---",
            f"title: \"{left_name} ↔ {right_name} Interaction\"",
            "description: \"Cross-system interaction analysis\"",
            "generated: true",
            "source_files:",
            f"  - \"{left_file}\"",
            f"  - \"{right_file}\"",
            f"nav_order: {nav_order}",
            "---",
            "",
            f"# {left_name} ↔ {right_name}",
            "",
            "## Interaction Summary",
            _interaction_summary(interaction),
            "",
            "## Shared Entity Fields",
            "| Field | "
            f"{_escape_cell(left_name)} Access | {_escape_cell(right_name)} Access |",
            "|-------|----------------|----------------|",
            *shared_field_rows,
            "",
            "## Signal Flow",
            *signal_lines,
            "",
            "## Shared Dependencies",
            *shared_dependency_lines,
            "",
            "## Direct Calls",
            *direct_call_lines,
            "",
            "## Data Flow Diagram",
            *mermaid_lines,
            "",
            "## Source References",
            *source_lines,
            "",
            "## Manual Notes",
            "<!-- MANUAL:START -->",
            "<!-- MANUAL:END -->",
            "",
        ]
    )


def _build_index_markdown(
    interactions: list[dict[str, Any]],
    significant_count: int,
) -> str:
    """Render master interaction index with full dependency graph."""
    all_names = sorted(
        {
            interaction["left"]["name"]
            for interaction in interactions
        }
        | {
            interaction["right"]["name"]
            for interaction in interactions
        }
    )
    node_ids = {name: f"S{idx}" for idx, name in enumerate(all_names, start=1)}

    mermaid_lines = ["```mermaid", "graph LR"]
    for name in all_names:
        mermaid_lines.append(f"  {node_ids[name]}[{name}]")

    for interaction in interactions:
        left_name = interaction["left"]["name"]
        right_name = interaction["right"]["name"]
        label = ", ".join(interaction["interaction_types"]).replace("|", "/")
        mermaid_lines.append(
            f"  {node_ids[left_name]} ---|{label}| {node_ids[right_name]}"
        )
    mermaid_lines.append("```")

    if interactions:
        table_lines = [
            "| Pair | Strength | Types |",
            "|------|----------|-------|",
        ]
        for interaction in interactions:
            left_name = interaction["left"]["name"]
            right_name = interaction["right"]["name"]
            table_lines.append(
                "| "
                f"`{left_name} ↔ {right_name}` | "
                f"{interaction['strength']} | "
                f"{', '.join(interaction['interaction_types'])} |"
            )
    else:
        table_lines = ["No cross-system interactions detected."]

    return "\n".join(
        [
            "---",
            "title: \"System Interaction Index\"",
            "description: \"Master dependency graph of cross-system interactions\"",
            "generated: true",
            "source_files:",
            "  - \"extracted/references.json\"",
            "  - \"extracted/systems.json\"",
            "nav_order: 1",
            "---",
            "",
            "# System Interaction Index",
            "",
            (
                f"Generated {len(interactions)} interaction link(s) total, "
                f"with {significant_count} significant pair page(s) (2+ types)."
            ),
            "",
            "## Master Dependency Graph",
            *mermaid_lines,
            "",
            "## Interaction Strength Table",
            *table_lines,
            "",
            "## Manual Notes",
            "<!-- MANUAL:START -->",
            "<!-- MANUAL:END -->",
            "",
        ]
    )


def run(manifest: dict) -> dict:
    """Generate interaction pair pages and a master interaction graph index."""
    files_written: list[str] = []
    warnings: list[str] = []
    errors: list[str] = []

    references_path = os.path.join(config.EXTRACTED_DIR, "references.json")
    systems_path = os.path.join(config.EXTRACTED_DIR, "systems.json")
    references = _read_json(references_path, warnings)
    systems_doc = _read_json(systems_path, warnings)
    if references is None or systems_doc is None:
        return {
            "files_written": files_written,
            "items_processed": 0,
            "warnings": warnings,
            "errors": errors,
        }

    systems = _collect_systems(manifest, systems_doc)
    if len(systems) < 2:
        warnings.append("Not enough systems discovered to build interaction pages.")

    interactions = _build_interactions(systems, references, warnings)
    significant_pairs = [row for row in interactions if row["strength"] >= 2]

    config.ensure_dir(config.CONTENT_INTERACTIONS)

    for index, interaction in enumerate(significant_pairs, start=10):
        output_path = os.path.join(config.CONTENT_INTERACTIONS, interaction["filename"])
        page_content = _build_pair_markdown(interaction, nav_order=index)
        if _write_markdown(output_path, page_content, warnings):
            files_written.append(output_path)

    index_path = os.path.join(config.CONTENT_INTERACTIONS, "_index.md")
    index_content = _build_index_markdown(
        interactions=interactions,
        significant_count=len(significant_pairs),
    )
    if _write_markdown(index_path, index_content, warnings):
        files_written.append(index_path)

    return {
        "files_written": files_written,
        "items_processed": len(significant_pairs),
        "warnings": warnings,
        "errors": errors,
    }
