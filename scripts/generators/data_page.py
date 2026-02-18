"""Generate Markdown pages for extracted JSON data files."""

from __future__ import annotations

import json
import os
import re
from collections import defaultdict
from typing import Any

import scripts.config as config


MANUAL_BLOCK_RE = re.compile(r"<!-- MANUAL:START -->.*?<!-- MANUAL:END -->", re.DOTALL)
MAX_SCHEMA_DEPTH = 3
SMALL_OBJECT_KEYS = 50
LARGE_ARRAY_ITEMS = 50


def _json_type(value: Any) -> str:
    if isinstance(value, bool):
        return "boolean"
    if isinstance(value, dict):
        return "object"
    if isinstance(value, list):
        return "array"
    if isinstance(value, str):
        return "string"
    if isinstance(value, int):
        return "int"
    if isinstance(value, float):
        return "float"
    if value is None:
        return "null"
    return type(value).__name__


def _escape_pipes(text: str) -> str:
    return text.replace("|", r"\|")


def _sanitize_inline(value: str) -> str:
    return value.replace("\n", " ").strip()


def _to_posix(path: str) -> str:
    return path.replace(os.sep, "/")


def _slug_from_path(file_path: str) -> str:
    return os.path.splitext(os.path.basename(file_path))[0]


def _quote_yaml(text: str) -> str:
    return text.replace("\\", "\\\\").replace('"', r'\"')


def _load_json(path: str) -> Any:
    with open(path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def _value_preview(value: Any) -> str:
    if isinstance(value, dict):
        return f"object with {len(value)} keys"
    if isinstance(value, list):
        item_type = _json_type(value[0]) if value else "unknown"
        return f"array ({len(value)} items, {item_type} entries)"

    text = json.dumps(value, ensure_ascii=False)
    if len(text) > 120:
        text = f"{text[:117]}..."
    return text


def _flatten_schema_rows(value: Any, prefix: str = "", depth: int = 1) -> list[tuple[str, str, str]]:
    rows: list[tuple[str, str, str]] = []

    if isinstance(value, dict):
        for key in sorted(value.keys()):
            child = value[key]
            path = f"{prefix}.{key}" if prefix else str(key)
            child_type = _json_type(child)
            rows.append((path, child_type, _value_preview(child)))

            if isinstance(child, dict) and depth < MAX_SCHEMA_DEPTH:
                rows.extend(_flatten_schema_rows(child, path, depth + 1))
            elif isinstance(child, list) and depth < MAX_SCHEMA_DEPTH and child:
                first_dict = next((item for item in child if isinstance(item, dict)), None)
                if first_dict is not None:
                    rows.extend(
                        _flatten_schema_rows(
                            first_dict,
                            f"{path}.item",
                            depth + 1,
                        )
                    )

    return rows


def _schema_rows_for_entry(entry: dict[str, Any], manifest_meta: dict[str, Any]) -> list[tuple[str, str, str]]:
    full_content = entry.get("full_content")
    value_type = entry.get("type")

    if value_type == "object" and isinstance(full_content, dict):
        return _flatten_schema_rows(full_content)

    if value_type == "array" and isinstance(full_content, list):
        item_count = manifest_meta.get("items_count")
        if not isinstance(item_count, int):
            item_count = len(full_content)

        rows: list[tuple[str, str, str]] = [
            ("items", "int", str(item_count)),
        ]

        if full_content:
            first_item = full_content[0]
            first_type = _json_type(first_item)
            rows.append(("item", first_type, _value_preview(first_item)))
            if isinstance(first_item, dict):
                rows.extend(_flatten_schema_rows(first_item, "item", 1))

        return rows

    if full_content is not None:
        return [("value", _json_type(full_content), _value_preview(full_content))]

    return []


def _render_schema_table(rows: list[tuple[str, str, str]]) -> str:
    lines = [
        "| Key | Type | Description |",
        "|-----|------|-------------|",
    ]

    for key, type_name, description in rows:
        safe_key = _escape_pipes(_sanitize_inline(key))
        safe_type = _escape_pipes(_sanitize_inline(type_name))
        safe_desc = _escape_pipes(_sanitize_inline(description))
        lines.append(f"| `{safe_key}` | {safe_type} | {safe_desc} |")

    return "\n".join(lines)


def _json_code_block(value: Any) -> str:
    return "```json\n" + json.dumps(value, ensure_ascii=False, indent=2) + "\n```"


def _render_full_content(entry: dict[str, Any], manifest_meta: dict[str, Any]) -> str:
    value_type = entry.get("type")
    full_content = entry.get("full_content")
    stats = entry.get("stats") if isinstance(entry.get("stats"), dict) else {}
    total_keys = stats.get("total_keys", 0)

    if value_type == "array" and isinstance(full_content, list):
        item_count = manifest_meta.get("items_count")
        if not isinstance(item_count, int):
            item_count = len(full_content)

        if item_count <= LARGE_ARRAY_ITEMS:
            return _json_code_block(full_content)

        sample_size = min(3, len(full_content))
        sample_items = full_content[:sample_size]

        lines = [
            f"Large array detected: **{item_count}** items.",
            "",
            f"Showing sampled content ({sample_size} item(s)):",
            "",
            "<details>",
            "<summary>Expand sampled content</summary>",
            "",
            _json_code_block(sample_items),
            "",
            "</details>",
        ]
        return "\n".join(lines)

    if value_type == "object" and isinstance(full_content, dict):
        if total_keys < SMALL_OBJECT_KEYS:
            return _json_code_block(full_content)

        preview_keys = sorted(full_content.keys())[:10]
        preview = {key: full_content[key] for key in preview_keys}
        lines = [
            f"Large object detected: **{total_keys}** total nested keys.",
            "",
            f"Top-level keys: **{len(full_content)}**",
            "",
            "<details>",
            "<summary>Expand top-level preview</summary>",
            "",
            _json_code_block(preview),
            "",
            "</details>",
        ]
        return "\n".join(lines)

    return _json_code_block(full_content)


def _module_slug(section: str, module_file: str, module_entry: dict[str, Any]) -> str:
    if section in {"systems", "ai_modules"}:
        system_name = module_entry.get("system_name")
        if isinstance(system_name, str) and system_name:
            return system_name
        stem = _slug_from_path(module_file)
        return stem[:-7] if stem.endswith("_system") else stem
    return _slug_from_path(module_file)


def _build_module_meta(manifest: dict) -> dict[str, dict[str, str]]:
    meta: dict[str, dict[str, str]] = {}
    sections = (
        ("systems", config.CONTENT_SYSTEMS),
        ("ai_modules", config.CONTENT_SYSTEMS),
        ("core_modules", config.CONTENT_CORE),
    )

    for section, content_dir in sections:
        entries = manifest.get(section, [])
        if not isinstance(entries, list):
            continue

        for module_entry in entries:
            if not isinstance(module_entry, dict):
                continue

            file_path = module_entry.get("file")
            if not isinstance(file_path, str) or not file_path.endswith(".gd"):
                continue

            slug = _module_slug(section, file_path, module_entry)
            title = module_entry.get("system_name") if section in {"systems", "ai_modules"} else _slug_from_path(file_path)
            if not isinstance(title, str) or not title:
                title = _slug_from_path(file_path)

            meta[file_path] = {
                "title": title,
                "doc_path": os.path.join(content_dir, f"{slug}.md"),
            }

    return meta


def _dependency_matches_file(dependency: str, data_file: str) -> bool:
    dep = dependency.replace("\\", "/").rstrip("/")
    target = data_file.replace("\\", "/")

    if dep == target:
        return True

    return target.startswith(dep + "/")


def _build_referenced_by_map(
    data_entries: list[dict[str, Any]],
    manifest: dict,
    warnings: list[str],
) -> dict[str, list[dict[str, str]]]:
    references_path = os.path.join(config.EXTRACTED_DIR, "references.json")
    if not os.path.exists(references_path):
        warnings.append("references.json not found; Referenced By sections omitted")
        return {}

    try:
        references = _load_json(references_path)
    except (OSError, json.JSONDecodeError) as exc:
        warnings.append(f"failed to load references.json: {exc}")
        return {}

    dependency_graph = references.get("dependency_graph")
    if not isinstance(dependency_graph, dict):
        warnings.append("references.json missing dependency_graph; Referenced By sections omitted")
        return {}

    module_meta = _build_module_meta(manifest)
    referenced_by: dict[str, list[dict[str, str]]] = defaultdict(list)

    data_files = []
    for entry in data_entries:
        file_path = entry.get("file")
        if isinstance(file_path, str) and file_path:
            data_files.append(file_path)

    for module_file, module_data in sorted(dependency_graph.items()):
        if not isinstance(module_data, dict):
            continue

        depends_on = module_data.get("depends_on")
        if not isinstance(depends_on, list):
            continue

        module_info = module_meta.get(module_file)
        if not module_info:
            continue

        for dep in depends_on:
            if not isinstance(dep, str) or not dep.startswith("data/"):
                continue

            for data_file in data_files:
                if not _dependency_matches_file(dep, data_file):
                    continue

                if data_file == dep:
                    reason = f"references `{dep}`"
                else:
                    reason = f"references data under `{dep.rstrip('/')}/`"

                referenced_by[data_file].append(
                    {
                        "module_title": module_info["title"],
                        "module_doc_path": module_info["doc_path"],
                        "reason": reason,
                    }
                )

    for file_path, refs in referenced_by.items():
        deduped: dict[tuple[str, str], dict[str, str]] = {}
        for ref in refs:
            key = (ref["module_title"], ref["module_doc_path"])
            deduped[key] = ref
        referenced_by[file_path] = [
            deduped[key]
            for key in sorted(deduped.keys())
        ]

    return referenced_by


def _preserve_manual_blocks(path: str, new_text: str) -> str:
    if not os.path.exists(path):
        return new_text

    try:
        with open(path, "r", encoding="utf-8") as handle:
            previous_text = handle.read()
    except OSError:
        return new_text

    old_blocks = MANUAL_BLOCK_RE.findall(previous_text)
    if not old_blocks:
        return new_text

    if not MANUAL_BLOCK_RE.search(new_text):
        return new_text

    index = 0

    def _replace_block(match: re.Match[str]) -> str:
        nonlocal index
        if index >= len(old_blocks):
            return match.group(0)
        block = old_blocks[index]
        index += 1
        return block

    return MANUAL_BLOCK_RE.sub(_replace_block, new_text)


def _write_markdown(path: str, content: str, files_written: list[str], errors: list[str]) -> None:
    try:
        with open(path, "w", encoding="utf-8") as handle:
            handle.write(content)
        files_written.append(path)
    except OSError as exc:
        errors.append(f"failed to write {path}: {exc}")


def _render_page(
    entry: dict[str, Any],
    manifest_meta: dict[str, Any],
    referenced_by: list[dict[str, str]],
    output_dir: str,
) -> str:
    source_file = entry["file"]
    category = entry["category"]
    file_stem = _slug_from_path(source_file)
    value_type = entry.get("type", "unknown")

    schema_rows = _schema_rows_for_entry(entry, manifest_meta)
    schema_table = _render_schema_table(schema_rows)
    full_content_section = _render_full_content(entry, manifest_meta)

    lines = [
        "---",
        f'title: "{_quote_yaml(file_stem)} Data"',
        f'description: "{_quote_yaml(category)} data file documentation"',
        "generated: true",
        "source_files:",
        f'  - "{_quote_yaml(source_file)}"',
        "nav_order: 10",
        "---",
        "",
        f"# {file_stem}",
        "",
        f"📄 source: `{source_file}` | Category: {category} | Type: {value_type}",
        "",
        "## Schema",
        "",
        schema_table,
        "",
        "## Full Content",
        "",
        full_content_section,
        "",
    ]

    full_content = entry.get("full_content")
    if value_type == "array" and isinstance(full_content, list) and full_content:
        lines.extend(
            [
                "### Example Entry",
                "",
                _json_code_block(full_content[0]),
                "",
            ]
        )

    lines.append("## Referenced By")
    lines.append("")
    if referenced_by:
        for ref in referenced_by:
            relative_link = os.path.relpath(ref["module_doc_path"], output_dir)
            relative_link = _to_posix(relative_link)
            lines.append(
                f"- [`{ref['module_title']}`]({relative_link}) - {ref['reason']}"
            )
    else:
        lines.append("- None found.")

    lines.extend(
        [
            "",
            "## Manual Notes",
            "",
            "<!-- MANUAL:START -->",
            "<!-- MANUAL:END -->",
            "",
        ]
    )

    return "\n".join(lines)


def _render_index_page(
    grouped: dict[str, list[dict[str, Any]]],
    source_files: list[str],
) -> str:
    total_files = sum(len(entries) for entries in grouped.values())

    lines = [
        "---",
        'title: "데이터 (Data)"',
        'description: "WorldSim data file documentation"',
        "generated: true",
        "source_files:",
    ]

    for source in source_files:
        lines.append(f'  - "{_quote_yaml(source)}"')

    lines.extend(
        [
            "nav_order: 1",
            "---",
            "",
            "# 데이터 (Data)",
            "",
            f"Total files: **{total_files}**",
            "",
        ]
    )

    for category in sorted(grouped.keys()):
        entries = sorted(grouped[category], key=lambda item: item["file"])
        lines.extend(
            [
                f"## {category}",
                "",
                "| File | Type | Key Count | Items |",
                "|------|------|-----------|-------|",
            ]
        )

        for entry in entries:
            rel_path = _to_posix(entry["index_rel_link"])
            key_count = entry.get("key_count", "-")
            items = entry.get("items_count", "-")
            file_stem = _slug_from_path(entry["file"])
            value_type = entry.get("type", "unknown")
            lines.append(
                f"| [{file_stem}]({rel_path}) | {value_type} | {key_count} | {items} |"
            )

        lines.append("")

    lines.extend(
        [
            "## Manual Notes",
            "",
            "<!-- MANUAL:START -->",
            "<!-- MANUAL:END -->",
            "",
        ]
    )

    return "\n".join(lines)


def run(manifest: dict) -> dict:
    """Main entry point.

    Args:
        manifest: The manifest.json data from Phase 1.

    Returns:
        dict with keys:
            - files_written: list of output file paths
            - items_processed: int count
            - warnings: list of warning strings
            - errors: list of error strings
    """
    warnings: list[str] = []
    errors: list[str] = []
    files_written: list[str] = []

    extracted_path = os.path.join(config.EXTRACTED_DIR, "data_files.json")
    if not os.path.exists(extracted_path):
        warnings.append("extracted/data_files.json not found")
        return {
            "files_written": files_written,
            "items_processed": 0,
            "warnings": warnings,
            "errors": errors,
        }

    try:
        extracted = _load_json(extracted_path)
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"failed to load extracted/data_files.json: {exc}")
        return {
            "files_written": files_written,
            "items_processed": 0,
            "warnings": warnings,
            "errors": errors,
        }

    data_entries = extracted.get("files", [])
    if not isinstance(data_entries, list):
        warnings.append("extracted/data_files.json has non-list 'files' field")
        data_entries = []

    manifest_data_entries = manifest.get("data_files", [])
    if not isinstance(manifest_data_entries, list):
        manifest_data_entries = []

    manifest_meta_by_file: dict[str, dict[str, Any]] = {}
    for entry in manifest_data_entries:
        if not isinstance(entry, dict):
            continue
        file_path = entry.get("file")
        if isinstance(file_path, str) and file_path:
            manifest_meta_by_file[file_path] = entry

    config.ensure_dir(config.CONTENT_DATA)

    referenced_by_map = _build_referenced_by_map(data_entries, manifest, warnings)

    grouped_for_index: dict[str, list[dict[str, Any]]] = defaultdict(list)
    processed_count = 0

    for entry in sorted(
        (item for item in data_entries if isinstance(item, dict)),
        key=lambda item: (str(item.get("category", "")), str(item.get("file", ""))),
    ):
        source_file = entry.get("file")
        category = entry.get("category")

        if not isinstance(source_file, str) or not source_file:
            warnings.append("skipping data entry with missing file path")
            continue

        if not isinstance(category, str) or not category:
            warnings.append(f"skipping data entry with missing category: {source_file}")
            continue

        category_dir = os.path.join(config.CONTENT_DATA, *category.split("/"))
        config.ensure_dir(category_dir)

        output_file = os.path.join(category_dir, f"{_slug_from_path(source_file)}.md")
        manifest_meta = manifest_meta_by_file.get(source_file, {})
        page_content = _render_page(
            entry=entry,
            manifest_meta=manifest_meta,
            referenced_by=referenced_by_map.get(source_file, []),
            output_dir=category_dir,
        )
        page_content = _preserve_manual_blocks(output_file, page_content)
        _write_markdown(output_file, page_content, files_written, errors)

        stats = entry.get("stats") if isinstance(entry.get("stats"), dict) else {}
        key_count: int | str = "-"
        if isinstance(manifest_meta, dict):
            keys_count = manifest_meta.get("keys_count")
            if isinstance(keys_count, int):
                key_count = keys_count
            else:
                item_keys = manifest_meta.get("item_keys")
                if isinstance(item_keys, list):
                    key_count = len(item_keys)

        if key_count == "-":
            key_count = stats.get("total_keys", "-")

        items_count = manifest_meta.get("items_count") if isinstance(manifest_meta, dict) else "-"
        if not isinstance(items_count, int):
            items_count = "-"

        index_rel_link = os.path.relpath(output_file, config.CONTENT_DATA)
        grouped_for_index[category].append(
            {
                "file": source_file,
                "type": entry.get("type", "unknown"),
                "key_count": key_count,
                "items_count": items_count,
                "index_rel_link": index_rel_link,
            }
        )

        processed_count += 1

    index_path = os.path.join(config.CONTENT_DATA, "_index.md")
    index_sources = ["extracted/data_files.json"]
    if os.path.exists(os.path.join(config.EXTRACTED_DIR, "references.json")):
        index_sources.append("extracted/references.json")

    index_content = _render_index_page(grouped_for_index, index_sources)
    index_content = _preserve_manual_blocks(index_path, index_content)
    _write_markdown(index_path, index_content, files_written, errors)

    return {
        "files_written": files_written,
        "items_processed": processed_count,
        "warnings": warnings,
        "errors": errors,
    }
