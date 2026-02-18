"""Phase 3 generator: produce system documentation pages and systems index."""

from __future__ import annotations

import json
import os
import re
from collections import defaultdict
from typing import Any

import scripts.config as config

_MANUAL_BLOCK_RE = re.compile(
    r"<!-- MANUAL:START -->.*?<!-- MANUAL:END -->",
    re.DOTALL,
)
_EXP_CALL_RE = re.compile(r"exp\(([^()]+)\)")
_VALID_SLUG_RE = re.compile(r"[^a-z0-9_]+")
_MATH_OPERATOR_RE = re.compile(r"[A-Za-z0-9_)\]]\s*[\+\*/]\s*[A-Za-z0-9_(\[]")
_MATH_MINUS_RE = re.compile(r"[A-Za-z0-9_)\]]\s+-\s+[A-Za-z0-9_(\[]")


def _load_json(path: str, label: str, warnings: list[str]) -> dict[str, Any]:
    if not os.path.exists(path):
        warnings.append(f"Missing input file, skipped: {label} ({path})")
        return {}
    try:
        with open(path, "r", encoding="utf-8") as f:
            payload = json.load(f)
    except OSError as exc:
        warnings.append(f"Failed to read {label} ({path}): {exc}")
        return {}
    except json.JSONDecodeError as exc:
        warnings.append(f"Invalid JSON in {label} ({path}): {exc}")
        return {}

    if not isinstance(payload, dict):
        warnings.append(f"Invalid payload for {label}: expected object root.")
        return {}
    return payload


def _unique_strings(values: list[Any]) -> list[str]:
    seen: set[str] = set()
    output: list[str] = []
    for value in values:
        if not isinstance(value, str):
            continue
        if value in seen:
            continue
        seen.add(value)
        output.append(value)
    return output


def _normalize_text(value: Any) -> str:
    if not isinstance(value, str):
        return ""
    return " ".join(value.split()).strip()


def _first_sentence(text: str) -> str:
    normalized = _normalize_text(text)
    if not normalized:
        return "Generated system documentation page."
    parts = re.split(r"(?<=[.!?])\s+", normalized, maxsplit=1)
    return parts[0] if parts else normalized


def _yaml_quote(value: str) -> str:
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def _md_cell(value: Any) -> str:
    text = str(value)
    return text.replace("|", r"\|").replace("\n", " ")


def _display_name(entry: dict[str, Any], slug: str) -> str:
    system_name = entry.get("system_name")
    if isinstance(system_name, str) and system_name.strip():
        token = system_name.strip()
    else:
        token = slug
    return token.replace("_", " ").strip().title()


def _slug_from_entry(entry: dict[str, Any]) -> str:
    system_name = entry.get("system_name")
    if isinstance(system_name, str) and system_name.strip():
        raw = system_name.strip().lower()
    else:
        rel_file = entry.get("file")
        base = os.path.splitext(os.path.basename(rel_file))[0] if isinstance(rel_file, str) else "system"
        raw = base.lower()
        if raw.endswith("_system"):
            raw = raw[: -len("_system")]

    slug = _VALID_SLUG_RE.sub("_", raw).strip("_")
    return slug or "system"


def _resolve_slug_collisions(entries: list[dict[str, Any]]) -> dict[str, str]:
    slug_by_file: dict[str, str] = {}
    used: set[str] = set()
    for entry in entries:
        rel_file = entry.get("file")
        if not isinstance(rel_file, str) or not rel_file:
            continue
        base_slug = _slug_from_entry(entry)
        slug = base_slug
        suffix = 2
        while slug in used:
            slug = f"{base_slug}_{suffix}"
            suffix += 1
        used.add(slug)
        slug_by_file[rel_file] = slug
    return slug_by_file


def _tick_interval_text(entry: dict[str, Any]) -> str:
    interval = entry.get("tick_interval")
    if isinstance(interval, (int, float)):
        if isinstance(interval, float) and interval.is_integer():
            return str(int(interval))
        return str(interval)

    raw = entry.get("tick_interval_raw")
    if isinstance(raw, str) and raw.strip():
        return f"config ({raw.strip()})"
    return "n/a"


def _manual_block(text: str) -> str:
    match = _MANUAL_BLOCK_RE.search(text)
    return match.group(0) if match else ""


def _merge_manual_blocks(generated: str, existing: str) -> str:
    existing_block = _manual_block(existing)
    if not existing_block:
        return generated

    if _MANUAL_BLOCK_RE.search(generated):
        return _MANUAL_BLOCK_RE.sub(existing_block, generated, count=1)

    output = generated.rstrip() + "\n\n" + existing_block + "\n"
    return output


def _write_markdown(path: str, content: str, warnings: list[str], errors: list[str]) -> bool:
    existing = ""
    if os.path.exists(path):
        try:
            with open(path, "r", encoding="utf-8") as f:
                existing = f.read()
        except OSError as exc:
            warnings.append(f"Failed to read existing markdown for MANUAL merge ({path}): {exc}")

    final_content = _merge_manual_blocks(content, existing)
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(final_content)
    except OSError as exc:
        errors.append(f"Failed to write markdown ({path}): {exc}")
        return False
    return True


def _field_description(field_name: str) -> str:
    token = field_name.lower()
    if "emotion" in token:
        return "Emotion-related state."
    if "hunger" in token:
        return "Hunger/food state."
    if "energy" in token:
        return "Energy or fatigue state."
    if "social" in token:
        return "Social interaction state."
    if "position" in token or "path" in token:
        return "World-space movement data."
    if "age" in token:
        return "Age or stage lifecycle state."
    if token == "id" or token.endswith("_id"):
        return "Entity identity reference."
    if "personality" in token or "trait" in token:
        return "Personality and trait state."
    if "action" in token:
        return "Current behavior/action state."
    return field_name.replace("_", " ")


def _formula_title(name: str) -> str:
    return name.replace("_", " ").strip().title()


def _extract_formula_expression(code_snippet: str) -> str:
    for raw_line in code_snippet.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        line = line.rstrip(",")
        if line.startswith("#"):
            continue
        if ":" in line and "=" not in line:
            line = line.split(":", 1)[1].strip()
        if "=" in line:
            line = line.split("=", 1)[1].strip()
        line = re.sub(r"\bvar\s+", "", line)
        if line:
            return line
    return ""


def _code_to_latex(code_snippet: str) -> str:
    expression = _extract_formula_expression(code_snippet)
    if not expression:
        return ""
    if not _looks_like_math_expression(expression):
        return ""

    latex = _EXP_CALL_RE.sub(r"e^{\1}", expression)
    latex = latex.replace("*", r" \cdot ")
    latex = latex.replace(">=", r"\ge ")
    latex = latex.replace("<=", r"\le ")
    return latex


def _looks_like_math_expression(expression: str) -> bool:
    stripped = expression.strip()
    if (
        (stripped.startswith('"') and stripped.endswith('"'))
        or (stripped.startswith("'") and stripped.endswith("'"))
    ):
        return False

    lowered = expression.lower()
    if any(fn in lowered for fn in ("exp(", "pow(", "log(", "sqrt(", "sin(", "cos(")):
        return True
    if _MATH_OPERATOR_RE.search(expression):
        return True
    if _MATH_MINUS_RE.search(expression):
        return True
    return False


def _render_system_frontmatter(
    display_name: str,
    description: str,
    source_file: str,
    nav_order: int,
) -> str:
    return (
        "---\n"
        f"title: {_yaml_quote(f'{display_name} System')}\n"
        f"description: {_yaml_quote(description)}\n"
        "generated: true\n"
        "source_files:\n"
        f"  - {_yaml_quote(source_file)}\n"
        f"nav_order: {nav_order}\n"
        "---\n"
    )


def _build_configuration_rows(
    entry: dict[str, Any],
    constants_map: dict[str, dict[str, Any]],
) -> list[tuple[str, str, str]]:
    rows: list[tuple[str, str, str]] = []
    config_refs = _unique_strings(entry.get("config_refs", []))
    for constant in config_refs:
        constant_info = constants_map.get(constant)
        if constant_info:
            value = str(constant_info.get("value", ""))
            comment = _normalize_text(constant_info.get("comment")) or "from GameConfig"
        elif re.fullmatch(r"[A-Z0-9_]+", constant):
            value = "(not found)"
            comment = "from GameConfig"
        else:
            value = "-"
            comment = "GameConfig function reference"
        rows.append((constant, value, comment))
    return rows


def _build_entity_field_rows(
    entry: dict[str, Any],
    file_path: str,
    field_access_map: dict[str, dict[str, set[str]]],
) -> list[tuple[str, str, str]]:
    rows: list[tuple[str, str, str]] = []
    ordered_fields = _unique_strings(entry.get("entity_fields", []))
    access_for_file = field_access_map.get(file_path, {})

    for field in sorted(access_for_file.keys()):
        if field not in ordered_fields:
            ordered_fields.append(field)

    for field in ordered_fields:
        access_set = access_for_file.get(field, set())
        if access_set == {"read", "write"}:
            access_text = "read/write"
        elif access_set == {"write"}:
            access_text = "write"
        elif access_set == {"read"}:
            access_text = "read"
        else:
            access_text = "read"
        rows.append((field, access_text, _field_description(field)))

    return rows


def _to_system_doc_link(target_file: str, slug_by_file: dict[str, str]) -> str:
    slug = slug_by_file.get(target_file)
    if slug:
        return f"{slug}.md"
    return ""


def _to_import_doc_link(target_file: str, slug_by_file: dict[str, str]) -> str:
    linked = _to_system_doc_link(target_file, slug_by_file)
    if linked:
        return linked
    if target_file.startswith("scripts/core/"):
        base = os.path.splitext(os.path.basename(target_file))[0]
        return f"../core/{base}.md"
    return ""


def _render_markdown_table(headers: list[str], rows: list[list[str]]) -> str:
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(["---"] * len(headers)) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(_md_cell(cell) for cell in row) + " |")
    return "\n".join(lines)


def _render_system_page(
    entry: dict[str, Any],
    slug_by_file: dict[str, str],
    constants_map: dict[str, dict[str, Any]],
    formulas_by_file: dict[str, list[dict[str, Any]]],
    imports_by_file: dict[str, list[dict[str, Any]]],
    signals_by_emitter: dict[str, list[dict[str, Any]]],
    manifest_signals: dict[str, dict[str, Any]],
    dependency_graph: dict[str, dict[str, list[str]]],
    field_access_map: dict[str, dict[str, set[str]]],
) -> str:
    rel_file = entry.get("file", "")
    slug = slug_by_file.get(rel_file, "system")
    display_name = _display_name(entry, slug)
    doc_comment = _normalize_text(entry.get("doc_comment"))
    description = _first_sentence(doc_comment)

    priority = entry.get("priority")
    nav_order = priority if isinstance(priority, int) else 999
    priority_text = str(priority) if isinstance(priority, int) else "n/a"
    tick_interval = _tick_interval_text(entry)

    frontmatter = _render_system_frontmatter(
        display_name=display_name,
        description=description,
        source_file=rel_file,
        nav_order=nav_order,
    )

    lines: list[str] = [frontmatter]
    lines.append(f"# {display_name} System")
    lines.append("")
    lines.append(f"> {doc_comment or 'No module-level documentation comment was extracted.'}")
    lines.append("")
    lines.append(
        f"📄 source: `{rel_file}` | Priority: {priority_text} | Tick interval: {tick_interval}"
    )
    lines.append("")
    lines.append("## Overview")
    lines.append("")

    function_count = len(entry.get("functions", []))
    config_count = len(_unique_strings(entry.get("config_refs", [])))
    field_count = len(_unique_strings(entry.get("entity_fields", [])))
    lines.append(
        doc_comment
        or f"This page summarizes the extracted structure and runtime behavior for `{display_name}`."
    )
    lines.append("")
    lines.append(
        f"The extractor found {function_count} functions, {config_count} configuration references, "
        f"and {field_count} tracked entity fields."
    )
    lines.append("")

    lines.append("## Configuration")
    lines.append("")
    config_rows = _build_configuration_rows(entry, constants_map)
    if config_rows:
        lines.append(
            _render_markdown_table(
                ["Constant", "Value", "Description"],
                [[f"`{name}`", value, desc] for name, value, desc in config_rows],
            )
        )
    else:
        lines.append("No explicit `GameConfig` references extracted.")
    lines.append("")

    lines.append("## Entity Fields Accessed")
    lines.append("")
    field_rows = _build_entity_field_rows(entry, rel_file, field_access_map)
    if field_rows:
        lines.append(
            _render_markdown_table(
                ["Field", "Access", "Description"],
                [[f"`{name}`", access, desc] for name, access, desc in field_rows],
            )
        )
    else:
        lines.append("No entity field access metadata extracted.")
    lines.append("")

    lines.append("## Functions")
    lines.append("")
    functions = entry.get("functions", [])
    if isinstance(functions, list) and functions:
        for function in functions:
            func_name = str(function.get("name", "unknown"))
            params = str(function.get("params", "")).strip()
            signature = f"{func_name}({params})" if params else f"{func_name}()"
            lines.append(f"### `{signature}`")
            lines.append("")
            func_doc = _normalize_text(function.get("doc_comment"))
            if func_doc:
                lines.append(func_doc)
                lines.append("")

            param_text = params if params else "(none)"
            line_start = function.get("line")
            line_count = function.get("line_count")
            if isinstance(line_start, int) and isinstance(line_count, int):
                line_end = line_start + max(1, line_count) - 1
                line_text = f"{line_start}-{line_end} ({line_count} lines)"
            elif isinstance(line_start, int):
                line_text = str(line_start)
            else:
                line_text = "unknown"

            lines.append(f"**Parameters**: `{param_text}`")
            lines.append(f"**Lines**: {line_text}")
            lines.append("")
    else:
        lines.append("No function metadata extracted.")
        lines.append("")

    lines.append("## Formulas")
    lines.append("")
    formulas = formulas_by_file.get(rel_file, [])
    if formulas:
        formulas = sorted(formulas, key=lambda item: (item.get("line_start", 0), item.get("name", "")))
        for formula in formulas:
            formula_name = str(formula.get("name", "formula"))
            lines.append(f"### {_formula_title(formula_name)}")
            lines.append("")

            formula_desc = _normalize_text(formula.get("description"))
            if formula_desc:
                lines.append(formula_desc)
                lines.append("")

            code_snippet = str(formula.get("code_snippet", "")).strip()
            latex = _code_to_latex(code_snippet)
            if latex:
                lines.append(f"$${latex}$$")
                lines.append("")

            if code_snippet:
                lines.append("```gdscript")
                lines.append(code_snippet)
                lines.append("```")
                lines.append("")

            line_start = formula.get("line_start")
            if isinstance(line_start, int):
                lines.append(f"📄 source: `{rel_file}:L{line_start}`")
                lines.append("")
    else:
        lines.append("No formulas extracted for this module.")
        lines.append("")

    lines.append("## Dependencies")
    lines.append("")
    lines.append("### Imports")
    lines.append("")
    imports = imports_by_file.get(rel_file, [])
    if imports:
        imports = sorted(imports, key=lambda item: (item.get("line", 0), item.get("to_file", "")))
        for import_ref in imports:
            to_file = str(import_ref.get("to_file", ""))
            import_type = str(import_ref.get("type", "import"))
            line_no = import_ref.get("line")
            filename = os.path.basename(to_file)
            doc_link = _to_import_doc_link(to_file, slug_by_file)
            if doc_link:
                target_text = f"[`{filename}`]({doc_link})"
            else:
                target_text = f"`{to_file}`"
            suffix = f" (line {line_no})" if isinstance(line_no, int) else ""
            lines.append(f"- {target_text} - via `{import_type}`{suffix}")
    else:
        lines.append("- None")
    lines.append("")

    lines.append("### Signals Emitted")
    lines.append("")
    emitted_signals = signals_by_emitter.get(rel_file, [])
    if emitted_signals:
        emitted_signals = sorted(
            emitted_signals,
            key=lambda item: (item.get("signal_name", ""), item.get("emitter_line", 0)),
        )
        seen_signals: set[tuple[str, int | None]] = set()
        for signal in emitted_signals:
            signal_name = str(signal.get("signal_name", ""))
            emitter_line = signal.get("emitter_line") if isinstance(signal.get("emitter_line"), int) else None
            marker = (signal_name, emitter_line)
            if marker in seen_signals:
                continue
            seen_signals.add(marker)
            signal_meta = manifest_signals.get(signal_name, {})
            params = signal_meta.get("params", "")
            params_text = str(params).strip() or "unknown"
            line_suffix = f" (line {emitter_line})" if emitter_line is not None else ""
            lines.append(
                f"- `{signal_name}` - parameters: `{params_text}`{line_suffix}"
            )
    else:
        lines.append("- None")
    lines.append("")

    lines.append("### Referenced By")
    lines.append("")
    depended_by = dependency_graph.get(rel_file, {}).get("depended_by", [])
    if depended_by:
        for source_file in sorted(depended_by):
            link = _to_system_doc_link(source_file, slug_by_file)
            if link:
                source_slug = slug_by_file.get(source_file, source_file)
                lines.append(f"- [`{source_slug}`]({link}) - depends on this module")
            else:
                lines.append(f"- `{source_file}` - depends on this module")
    else:
        lines.append("- None")
    lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def _priority_bucket(priority: Any) -> str:
    if not isinstance(priority, int):
        return "Unspecified Priority"
    if priority <= 20:
        return "High Priority (0-20)"
    if priority <= 40:
        return "Medium Priority (21-40)"
    return "Low Priority (41+)"


def _render_index_page(
    ordered_entries: list[dict[str, Any]],
    slug_by_file: dict[str, str],
    dependency_graph: dict[str, dict[str, list[str]]],
) -> str:
    lines: list[str] = [
        "---",
        'title: "시스템 (Systems)"',
        'description: "WorldSim simulation systems in execution order"',
        "generated: true",
        "source_files:",
    ]
    for entry in ordered_entries:
        rel_file = entry.get("file", "")
        if isinstance(rel_file, str) and rel_file:
            lines.append(f"  - {_yaml_quote(rel_file)}")
    lines.extend(
        [
            "nav_order: 1",
            "---",
            "",
            "# 시스템 (Systems)",
            "",
            f"Total: {len(ordered_entries)} systems",
            "",
            "## Execution Order",
            "",
        ]
    )

    table_rows: list[list[str]] = []
    for entry in ordered_entries:
        rel_file = entry.get("file", "")
        slug = slug_by_file.get(rel_file, "system")
        name = _display_name(entry, slug)
        priority = entry.get("priority")
        priority_text = str(priority) if isinstance(priority, int) else "-"
        description = _first_sentence(str(entry.get("doc_comment", "")))
        table_rows.append(
            [
                priority_text,
                f"[{name}]({slug}.md)",
                _tick_interval_text(entry),
                description,
            ]
        )

    lines.append(
        _render_markdown_table(
            ["Priority", "System", "Tick Interval", "Description"],
            table_rows,
        )
    )
    lines.append("")
    lines.append("## Architecture Diagram")
    lines.append("")
    lines.append("```mermaid")
    lines.append("graph TD")

    bucket_names = [
        "High Priority (0-20)",
        "Medium Priority (21-40)",
        "Low Priority (41+)",
        "Unspecified Priority",
    ]
    bucket_nodes: dict[str, list[str]] = {name: [] for name in bucket_names}

    for entry in ordered_entries:
        rel_file = entry.get("file", "")
        slug = slug_by_file.get(rel_file, "")
        if not slug:
            continue
        bucket = _priority_bucket(entry.get("priority"))
        if bucket not in bucket_nodes:
            continue
        bucket_nodes[bucket].append(slug)

    for bucket in bucket_names:
        lines.append(f'  subgraph "{bucket}"')
        nodes = sorted(set(bucket_nodes[bucket]))
        if nodes:
            for node in nodes:
                lines.append(f"    {node}")
        else:
            lines.append("    placeholder")
        lines.append("  end")

    edge_set: set[tuple[str, str]] = set()
    for entry in ordered_entries:
        from_file = entry.get("file", "")
        from_slug = slug_by_file.get(from_file, "")
        if not from_slug:
            continue
        targets = dependency_graph.get(from_file, {}).get("depends_on", [])
        for target_file in targets:
            to_slug = slug_by_file.get(target_file, "")
            if not to_slug:
                continue
            if from_slug == to_slug:
                continue
            edge_set.add((from_slug, to_slug))

    if edge_set:
        for from_slug, to_slug in sorted(edge_set):
            lines.append(f"  {from_slug} --> {to_slug}")
    else:
        lines.append("  %% No intra-system dependency edges extracted")

    lines.append("```")
    lines.append("")
    return "\n".join(lines)


def run(manifest: dict) -> dict:
    """Generate one documentation page per system and a systems index page."""
    warnings: list[str] = []
    errors: list[str] = []
    files_written: list[str] = []

    config.ensure_dir(config.CONTENT_SYSTEMS)

    systems_path = os.path.join(config.EXTRACTED_DIR, "systems.json")
    formulas_path = os.path.join(config.EXTRACTED_DIR, "formulas.json")
    references_path = os.path.join(config.EXTRACTED_DIR, "references.json")
    constants_path = os.path.join(config.EXTRACTED_DIR, "constants.json")

    systems_payload = _load_json(systems_path, "systems.json", warnings)
    formulas_payload = _load_json(formulas_path, "formulas.json", warnings)
    references_payload = _load_json(references_path, "references.json", warnings)
    constants_payload = _load_json(constants_path, "constants.json", warnings)

    entries = list(manifest.get("systems", [])) + list(manifest.get("ai_modules", []))
    if not entries:
        warnings.append("No systems or ai_modules in manifest; nothing generated.")
        return {
            "files_written": [],
            "items_processed": 0,
            "warnings": warnings,
            "errors": errors,
        }

    systems_by_file: dict[str, dict[str, Any]] = {}
    for system_entry in systems_payload.get("systems", []):
        file_path = system_entry.get("file")
        if isinstance(file_path, str) and file_path:
            systems_by_file[file_path] = system_entry

    merged_entries: list[dict[str, Any]] = []
    for entry in entries:
        rel_file = entry.get("file")
        if not isinstance(rel_file, str) or not rel_file:
            warnings.append("Skipped manifest entry with missing file path.")
            continue
        merged = dict(entry)
        merged.update(systems_by_file.get(rel_file, {}))
        merged_entries.append(merged)

    slug_by_file = _resolve_slug_collisions(merged_entries)

    constants_map: dict[str, dict[str, Any]] = {}
    for constant in constants_payload.get("constants", []):
        name = constant.get("name")
        if isinstance(name, str) and name:
            constants_map[name] = constant

    formulas_by_file: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for formula in formulas_payload.get("formulas", []):
        file_path = formula.get("file")
        if isinstance(file_path, str) and file_path:
            formulas_by_file[file_path].append(formula)

    imports_by_file: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for import_ref in references_payload.get("imports", []):
        from_file = import_ref.get("from_file")
        if isinstance(from_file, str) and from_file:
            imports_by_file[from_file].append(import_ref)

    signals_by_emitter: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for signal in references_payload.get("signals", []):
        emitter = signal.get("emitter")
        if isinstance(emitter, str) and emitter:
            signals_by_emitter[emitter].append(signal)

    field_access_map: dict[str, dict[str, set[str]]] = defaultdict(lambda: defaultdict(set))
    for access in references_payload.get("entity_field_access", []):
        file_path = access.get("file")
        field_name = access.get("field")
        access_type = access.get("access_type")
        if not (isinstance(file_path, str) and isinstance(field_name, str)):
            continue
        if access_type in {"read", "write"}:
            field_access_map[file_path][field_name].add(access_type)

    dependency_graph = references_payload.get("dependency_graph", {})
    if not isinstance(dependency_graph, dict):
        dependency_graph = {}

    manifest_signals = manifest.get("signals", {})
    if not isinstance(manifest_signals, dict):
        manifest_signals = {}

    ordered_entries = sorted(
        merged_entries,
        key=lambda item: (
            item.get("priority") if isinstance(item.get("priority"), int) else 10_000,
            _display_name(item, slug_by_file.get(item.get("file", ""), "system")),
        ),
    )

    for entry in ordered_entries:
        rel_file = entry.get("file")
        if not isinstance(rel_file, str) or not rel_file:
            continue

        slug = slug_by_file.get(rel_file, "system")
        page_content = _render_system_page(
            entry=entry,
            slug_by_file=slug_by_file,
            constants_map=constants_map,
            formulas_by_file=formulas_by_file,
            imports_by_file=imports_by_file,
            signals_by_emitter=signals_by_emitter,
            manifest_signals=manifest_signals,
            dependency_graph=dependency_graph,
            field_access_map=field_access_map,
        )
        output_path = os.path.join(config.CONTENT_SYSTEMS, f"{slug}.md")
        if _write_markdown(output_path, page_content, warnings, errors):
            files_written.append(output_path)

    index_content = _render_index_page(
        ordered_entries=ordered_entries,
        slug_by_file=slug_by_file,
        dependency_graph=dependency_graph,
    )
    index_path = os.path.join(config.CONTENT_SYSTEMS, "_index.md")
    if _write_markdown(index_path, index_content, warnings, errors):
        files_written.append(index_path)

    return {
        "files_written": files_written,
        "items_processed": len(ordered_entries),
        "warnings": warnings,
        "errors": errors,
    }
