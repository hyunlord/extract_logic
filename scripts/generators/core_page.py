"""Generate Markdown docs for core modules from extracted metadata."""

from __future__ import annotations

import json
import os
import re
from typing import Any

import scripts.config as config


_MANUAL_BLOCK_RE = re.compile(
    r"<!-- MANUAL:START -->.*?<!-- MANUAL:END -->",
    re.DOTALL,
)


def _read_json(path: str, warnings: list[str], label: str) -> dict[str, Any]:
    """Read JSON file and return dict, or empty dict on failure."""
    if not os.path.exists(path):
        warnings.append(f"{label} missing, skipped: {path}")
        return {}

    try:
        with open(path, "r", encoding="utf-8") as handle:
            data = json.load(handle)
        if not isinstance(data, dict):
            warnings.append(f"{label} must be a JSON object, got {type(data).__name__}.")
            return {}
        return data
    except (OSError, json.JSONDecodeError) as exc:
        warnings.append(f"Failed to read {label}: {exc}")
        return {}


def _slugify_filename(path: str) -> str:
    """Convert source filename to deterministic markdown slug."""
    stem = os.path.splitext(os.path.basename(path))[0].lower()
    slug = re.sub(r"[^a-z0-9_]+", "_", stem)
    slug = re.sub(r"_+", "_", slug).strip("_")
    return slug or "module"


def _title_from_entry(entry: dict[str, Any]) -> str:
    """Choose a readable module title."""
    class_name = entry.get("class_name")
    if isinstance(class_name, str) and class_name.strip():
        return class_name.strip()
    stem = os.path.splitext(os.path.basename(str(entry.get("file", ""))))[0]
    words = [part for part in stem.replace("-", "_").split("_") if part]
    if not words:
        return "Core Module"
    return " ".join(word.capitalize() for word in words)


def _first_sentence(text: str) -> str:
    """Return first sentence-like chunk for descriptions."""
    cleaned = " ".join((text or "").strip().split())
    if not cleaned:
        return ""
    parts = re.split(r"(?<=[.!?])\s+", cleaned, maxsplit=1)
    return parts[0].strip()


def _yaml_quote(text: str) -> str:
    return '"' + text.replace("\\", "\\\\").replace('"', '\\"') + '"'


def _md_escape(text: Any) -> str:
    return str(text).replace("|", "\\|").replace("\n", " ").strip()


def _normalize_ref_path(path: str) -> str:
    normalized = str(path).replace("\\", "/")
    if normalized.startswith("res://"):
        return normalized[6:]
    return normalized


def _build_system_slug_map(manifest: dict) -> dict[str, str]:
    """Build source file path → page slug map, matching system_page.py logic."""
    entries = list(manifest.get("systems", [])) + list(manifest.get("ai_modules", []))
    slug_map: dict[str, str] = {}
    used: set[str] = set()
    for entry in entries:
        file_path = entry.get("file")
        if not isinstance(file_path, str) or not file_path:
            continue
        system_name = entry.get("system_name")
        if isinstance(system_name, str) and system_name.strip():
            raw = system_name.strip().lower()
        else:
            base = os.path.splitext(os.path.basename(file_path))[0].lower()
            raw = base
            if raw.endswith("_system"):
                raw = raw[: -len("_system")]
        slug = re.sub(r"[^a-z0-9_]+", "_", raw).strip("_") or "system"
        base_slug = slug
        suffix = 2
        while slug in used:
            slug = f"{base_slug}_{suffix}"
            suffix += 1
        used.add(slug)
        slug_map[file_path] = slug
    return slug_map


def _link_for_source_path(path: str, system_slug_map: dict[str, str] | None = None) -> str:
    normalized = _normalize_ref_path(path)
    basename = os.path.basename(normalized)
    if normalized.startswith("scripts/core/"):
        return f"[`{basename}`]({_slugify_filename(normalized)}.md)"
    if normalized.startswith("scripts/systems/") or normalized.startswith("scripts/ai/"):
        slug = (system_slug_map or {}).get(normalized, _slugify_filename(normalized))
        return f"[`{basename}`](../systems/{slug}.md)"
    return f"`{normalized}`"


def _extract_manual_blocks(existing_path: str) -> list[str]:
    """Extract MANUAL blocks from existing markdown file."""
    if not os.path.exists(existing_path):
        return []
    try:
        with open(existing_path, "r", encoding="utf-8") as handle:
            text = handle.read()
    except OSError:
        return []
    return _MANUAL_BLOCK_RE.findall(text)


def _write_markdown(path: str, content: str) -> None:
    """Write markdown while preserving existing MANUAL blocks."""
    manual_blocks = _extract_manual_blocks(path)
    out = content.rstrip() + "\n"
    if manual_blocks:
        out += "\n" + "\n\n".join(block.rstrip() for block in manual_blocks) + "\n"
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(out)


def _core_entries(
    manifest: dict[str, Any],
    systems_data: dict[str, Any],
    warnings: list[str],
) -> list[dict[str, Any]]:
    """Merge manifest core_modules with detailed systems core entries."""
    manifest_core = manifest.get("core_modules", [])
    if not isinstance(manifest_core, list):
        warnings.append("manifest.core_modules is not a list.")
        manifest_core = []

    manifest_by_file: dict[str, dict[str, Any]] = {}
    for item in manifest_core:
        if not isinstance(item, dict):
            continue
        file_path = item.get("file")
        if not isinstance(file_path, str) or not file_path:
            warnings.append("Skipped core module with missing file path in manifest.")
            continue
        manifest_by_file[file_path] = dict(item)

    detailed_by_file: dict[str, dict[str, Any]] = {}
    for item in systems_data.get("systems", []) if isinstance(systems_data.get("systems"), list) else []:
        if not isinstance(item, dict):
            continue
        file_path = item.get("file")
        if isinstance(file_path, str) and file_path.startswith("scripts/core/"):
            detailed_by_file[file_path] = dict(item)

    merged: list[dict[str, Any]] = []
    all_files = sorted(set(manifest_by_file) | set(detailed_by_file))
    for file_path in all_files:
        entry = dict(manifest_by_file.get(file_path, {"file": file_path}))
        entry.update(detailed_by_file.get(file_path, {}))
        merged.append(entry)
    return merged


def _functions_table(functions: list[dict[str, Any]]) -> str:
    rows = [
        "| Function | Parameters | Returns | Line |",
        "|----------|------------|---------|------|",
    ]
    if not functions:
        rows.append("| - | - | - | - |")
        return "\n".join(rows)

    for func in sorted(
        [f for f in functions if isinstance(f, dict)],
        key=lambda item: (str(item.get("name", "")), int(item.get("line", 0) or 0)),
    ):
        name = str(func.get("name", "")).strip() or "unknown"
        params = str(func.get("params", "")).strip() or "-"
        returns = str(func.get("returns", "")).strip() or "-"
        line = func.get("line")
        line_text = str(line) if isinstance(line, int) else "-"
        rows.append(
            f"| `{_md_escape(name)}()` | `{_md_escape(params)}` | "
            f"`{_md_escape(returns)}` | {line_text} |"
        )
    return "\n".join(rows)


def _signals_table(signal_entries: list[dict[str, str]]) -> str:
    rows = [
        "| Signal | Parameters |",
        "|--------|------------|",
    ]
    if not signal_entries:
        rows.append("| - | - |")
        return "\n".join(rows)

    for item in sorted(signal_entries, key=lambda sig: sig.get("name", "")):
        name = item.get("name", "").strip() or "unknown"
        params = item.get("params", "").strip() or "-"
        rows.append(f"| `{_md_escape(name)}` | `{_md_escape(params)}` |")
    return "\n".join(rows)


def _render_module_page(
    entry: dict[str, Any],
    nav_order: int,
    import_links: list[str],
    used_by_links: list[str],
    signal_entries: list[dict[str, str]],
) -> str:
    file_path = str(entry.get("file", ""))
    title = _title_from_entry(entry)
    doc_comment = str(entry.get("doc_comment", "")).strip()
    overview = _first_sentence(doc_comment) or "No summary available."
    description = _first_sentence(doc_comment) or f"{title} core module."
    lines = entry.get("lines")
    if not isinstance(lines, int):
        lines = int(entry.get("stats", {}).get("total_lines", 0) or 0)
    extends = str(entry.get("extends", "-")).strip() or "-"
    functions = entry.get("functions")
    if not isinstance(functions, list):
        functions = []

    imports_text = ", ".join(import_links) if import_links else "-"
    used_by_text = ", ".join(used_by_links) if used_by_links else "-"
    quote = doc_comment or "No module documentation found."

    return (
        "---\n"
        f"title: {_yaml_quote(title)}\n"
        f"description: {_yaml_quote(description)}\n"
        "generated: true\n"
        "source_files:\n"
        f"  - {_yaml_quote(file_path)}\n"
        f"nav_order: {nav_order}\n"
        "---\n\n"
        f"# {title}\n\n"
        f"> {quote}\n\n"
        f"📄 source: `{file_path}` | {lines} lines | extends: {extends}\n\n"
        "## 개요 (Overview)\n"
        f"{overview}\n\n"
        "## 공개 API (Public API)\n\n"
        "### Functions\n"
        f"{_functions_table(functions)}\n\n"
        "### Signals\n"
        f"{_signals_table(signal_entries)}\n\n"
        "## 의존성 (Dependencies)\n"
        f"- Imports: {imports_text}\n"
        f"- Used by: {used_by_text}\n"
    )


def _render_index_page(entries: list[dict[str, Any]]) -> str:
    source_files = sorted(
        str(entry.get("file", ""))
        for entry in entries
        if isinstance(entry.get("file"), str) and entry.get("file")
    )

    lines = [
        "---",
        'title: "코어 모듈 (Core Modules)"',
        'description: "Core module overview and quick reference"',
        "generated: true",
        "source_files:",
    ]
    if source_files:
        for source_file in source_files:
            lines.append(f"  - {_yaml_quote(source_file)}")
    else:
        lines.append('  - "N/A"')
    lines.extend(
        [
            "nav_order: 1",
            "---",
            "",
            "# 코어 모듈 (Core Modules)",
            "",
            f"Total: {len(entries)} modules",
            "",
            "| Module | File | Lines | Description |",
            "|--------|------|-------|-------------|",
        ]
    )

    if not entries:
        lines.append("| - | - | - | - |")
        return "\n".join(lines) + "\n"

    for entry in entries:
        file_path = str(entry.get("file", ""))
        slug = _slugify_filename(file_path)
        title = _title_from_entry(entry)
        doc_comment = str(entry.get("doc_comment", "")).strip()
        description = _first_sentence(doc_comment) or "-"
        line_count = entry.get("lines")
        if not isinstance(line_count, int):
            line_count = int(entry.get("stats", {}).get("total_lines", 0) or 0)
        lines.append(
            f"| [{_md_escape(title)}]({slug}.md) | `{_md_escape(file_path)}` | "
            f"{line_count} | {_md_escape(description)} |"
        )

    return "\n".join(lines) + "\n"


def run(manifest: dict) -> dict:
    """Main entry point.

    Args:
        manifest: The manifest.json data from Phase 1.

    Returns:
        dict with keys:
            - "files_written": list of output file paths
            - "items_processed": int count
            - "warnings": list of warning strings
            - "errors": list of error strings
    """
    files_written: list[str] = []
    warnings: list[str] = []
    errors: list[str] = []

    systems_path = os.path.join(config.EXTRACTED_DIR, "systems.json")
    references_path = os.path.join(config.EXTRACTED_DIR, "references.json")
    systems_data = _read_json(systems_path, warnings, "systems.json")
    references_data = _read_json(references_path, warnings, "references.json")

    try:
        config.ensure_dir(config.CONTENT_CORE)
    except OSError as exc:
        return {
            "files_written": [],
            "items_processed": 0,
            "warnings": warnings,
            "errors": [f"Failed to ensure core content directory: {exc}"],
        }

    entries = _core_entries(manifest, systems_data, warnings)
    system_slug_map = _build_system_slug_map(manifest)

    dep_graph = references_data.get("dependency_graph", {})
    if not isinstance(dep_graph, dict):
        dep_graph = {}

    imports_records = references_data.get("imports", [])
    if not isinstance(imports_records, list):
        imports_records = []

    signals_records = references_data.get("signals", [])
    if not isinstance(signals_records, list):
        signals_records = []

    for nav_order, entry in enumerate(entries, start=1):
        file_path = str(entry.get("file", "")).strip()
        if not file_path:
            warnings.append("Skipped core entry with empty file path.")
            continue

        slug = _slugify_filename(file_path)
        page_path = os.path.join(config.CONTENT_CORE, f"{slug}.md")

        imports_set: set[str] = set()
        entry_imports = entry.get("imports", [])
        if isinstance(entry_imports, list):
            for import_path in entry_imports:
                if isinstance(import_path, str) and import_path.strip():
                    imports_set.add(_normalize_ref_path(import_path))
        for record in imports_records:
            if not isinstance(record, dict):
                continue
            if _normalize_ref_path(str(record.get("from_file", ""))) != file_path:
                continue
            target = str(record.get("to_file", "")).strip()
            if target:
                imports_set.add(_normalize_ref_path(target))
        import_links = [_link_for_source_path(path, system_slug_map) for path in sorted(imports_set)]

        used_by_set: set[str] = set()
        dep_entry = dep_graph.get(file_path)
        if isinstance(dep_entry, dict):
            depended_by = dep_entry.get("depended_by", [])
            if isinstance(depended_by, list):
                for source in depended_by:
                    if isinstance(source, str):
                        used_by_set.add(source)
        if not used_by_set:
            for record in imports_records:
                if not isinstance(record, dict):
                    continue
                if _normalize_ref_path(str(record.get("to_file", ""))) != file_path:
                    continue
                source = str(record.get("from_file", "")).strip()
                if source:
                    used_by_set.add(source)
        used_by_links = [_link_for_source_path(path, system_slug_map) for path in sorted(used_by_set)]

        signal_map: dict[str, str] = {}
        entry_signals = entry.get("signals", [])
        if isinstance(entry_signals, list):
            for signal in entry_signals:
                if isinstance(signal, str):
                    signal_map[signal] = ""
                elif isinstance(signal, dict):
                    name = str(signal.get("name", "")).strip()
                    if name:
                        signal_map[name] = str(signal.get("params", "")).strip()
        emitted = entry.get("signals_emitted", [])
        if isinstance(emitted, list):
            for signal_name in emitted:
                if isinstance(signal_name, str) and signal_name.strip():
                    signal_map[signal_name.strip()] = signal_map.get(signal_name.strip(), "")
        for record in signals_records:
            if not isinstance(record, dict):
                continue
            if _normalize_ref_path(str(record.get("emitter", ""))) != file_path:
                continue
            signal_name = str(record.get("signal_name", "")).strip()
            if signal_name:
                signal_map[signal_name] = signal_map.get(signal_name, "")
        signal_entries = [
            {"name": name, "params": params}
            for name, params in sorted(signal_map.items(), key=lambda item: item[0])
        ]

        try:
            markdown = _render_module_page(
                entry=entry,
                nav_order=nav_order,
                import_links=import_links,
                used_by_links=used_by_links,
                signal_entries=signal_entries,
            )
            _write_markdown(page_path, markdown)
            files_written.append(page_path)
        except OSError as exc:
            errors.append(f"Failed to write core page for {file_path}: {exc}")

    index_path = os.path.join(config.CONTENT_CORE, "_index.md")
    try:
        _write_markdown(index_path, _render_index_page(entries))
        files_written.append(index_path)
    except OSError as exc:
        errors.append(f"Failed to write core index page: {exc}")

    return {
        "files_written": files_written,
        "items_processed": len(entries),
        "warnings": warnings,
        "errors": errors,
    }


if __name__ == "__main__":
    manifest_path = os.path.join(config.EXTRACTED_DIR, "manifest.json")
    if not os.path.exists(manifest_path):
        print({"files_written": [], "items_processed": 0, "warnings": [], "errors": ["manifest.json not found"]})
    else:
        with open(manifest_path, "r", encoding="utf-8") as handle:
            manifest_data = json.load(handle)
        print(run(manifest_data))
