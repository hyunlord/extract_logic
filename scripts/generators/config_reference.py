"""Generate Config Reference markdown from extracted constants and references."""

from __future__ import annotations

import json
import os
from collections import defaultdict

import scripts.config as config
from scripts.generators.strings import t

_SOURCE_REL_PATH = "scripts/core/game_config.gd"
_MANUAL_START = "<!-- MANUAL:START -->"
_MANUAL_END = "<!-- MANUAL:END -->"


def _read_json(path: str) -> tuple[dict | None, str | None]:
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (OSError, json.JSONDecodeError) as exc:
        return None, str(exc)
    if not isinstance(data, dict):
        return None, "JSON root is not an object"
    return data, None


def _escape_table_cell(value: object) -> str:
    text = str(value)
    return text.replace("|", "\\|").replace("\n", "<br>")


def _module_label(file_path: str) -> str:
    stem = os.path.splitext(os.path.basename(file_path))[0]
    if stem.endswith("_system"):
        return stem[: -len("_system")]
    return stem


def _usage_map(references: dict) -> dict[str, list[str]]:
    usage: dict[str, set[str]] = defaultdict(set)
    for ref in references.get("config_refs", []):
        if not isinstance(ref, dict):
            continue
        name = ref.get("constant")
        file_path = ref.get("file")
        if not isinstance(name, str) or not isinstance(file_path, str):
            continue
        usage[name].add(_module_label(file_path))
    return {name: sorted(modules) for name, modules in usage.items()}


def _constant_group(used_by: list[str]) -> str:
    if not used_by:
        return "unreferenced"
    if len(used_by) == 1:
        return used_by[0]
    return "shared"


def _source_line_count(manifest: dict, constants_data: dict) -> int:
    for entry in manifest.get("core_modules", []):
        if not isinstance(entry, dict):
            continue
        if entry.get("file") == _SOURCE_REL_PATH and isinstance(entry.get("lines"), int):
            return entry["lines"]

    source_repo = manifest.get("source_repo")
    if isinstance(source_repo, str):
        source_path = os.path.join(source_repo, _SOURCE_REL_PATH)
    else:
        source_path = config.source_path("scripts", "core", "game_config.gd")

    if os.path.exists(source_path):
        try:
            with open(source_path, "r", encoding="utf-8") as f:
                return sum(1 for _ in f)
        except OSError:
            pass

    max_line = 0
    for key in ("constants", "enums", "dictionaries", "functions"):
        for item in constants_data.get(key, []):
            if isinstance(item, dict) and isinstance(item.get("line"), int):
                max_line = max(max_line, item["line"])
    return max_line


def _existing_manual_block(path: str) -> str | None:
    if not os.path.exists(path):
        return None
    try:
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
    except OSError:
        return None

    start = text.find(_MANUAL_START)
    if start < 0:
        return None
    end = text.find(_MANUAL_END, start + len(_MANUAL_START))
    if end < 0:
        return None
    end += len(_MANUAL_END)
    return text[start:end]


def _render_markdown(manifest: dict, constants_data: dict, references: dict, lang: str) -> str:
    constants = [c for c in constants_data.get("constants", []) if isinstance(c, dict)]
    enums = [e for e in constants_data.get("enums", []) if isinstance(e, dict)]
    dictionaries = [d for d in constants_data.get("dictionaries", []) if isinstance(d, dict)]
    functions = [f for f in constants_data.get("functions", []) if isinstance(f, dict)]
    usage = _usage_map(references)
    source_lines = _source_line_count(manifest, constants_data)

    lines: list[str] = [
        "---",
        'title: "설정 레퍼런스 (Config Reference)"',
        'description: "GameConfig 전체 상수, 열거형, 사전 레퍼런스"',
        "generated: true",
        "source_files:",
        '  - "scripts/core/game_config.gd"',
        "nav_order: 2",
        "---",
        "",
        "# GameConfig Reference",
        "",
        f"📄 source: `{_SOURCE_REL_PATH}` ({source_lines} lines)",
        "",
        f"## {t('section_constants', lang)}",
        "",
    ]

    grouped: dict[str, list[dict]] = defaultdict(list)
    for constant in sorted(constants, key=lambda c: (int(c.get("line", 0)), str(c.get("name", "")))):
        used_by = usage.get(str(constant.get("name", "")), [])
        grouped[_constant_group(used_by)].append(constant)

    for group_name in sorted(grouped):
        lines.extend(
            [
                f"### {group_name}",
                "",
                "| Name | Value | Raw Expression | Used By | Source | Notes |",
                "|------|------:|---------------|---------|--------|-------|",
            ]
        )
        for item in grouped[group_name]:
            name = str(item.get("name", ""))
            used_by = usage.get(name, [])
            used_by_text = ", ".join(used_by) if used_by else "-"
            value = _escape_table_cell(item.get("value", ""))
            raw = _escape_table_cell(item.get("value_raw", ""))
            source = f"`{_SOURCE_REL_PATH}:L{int(item.get('line', 0))}`"
            comment = _escape_table_cell(item.get("comment", "-"))
            lines.append(
                "| "
                + " | ".join(
                    [
                        f"`{_escape_table_cell(name)}`",
                        value,
                        f"`{raw}`",
                        _escape_table_cell(used_by_text),
                        source,
                        comment if comment else "-",
                    ]
                )
                + " |"
            )
        lines.append("")

    lines.extend([f"## {t('section_enums', lang)}", ""])
    for enum in sorted(enums, key=lambda e: (int(e.get("line", 0)), str(e.get("name", "")))):
        enum_name = str(enum.get("name", ""))
        lines.append(f"### {enum_name}")
        lines.append("")
        if isinstance(enum.get("comment"), str):
            lines.append(enum["comment"])
            lines.append("")
        used_by = usage.get(enum_name, [])
        lines.append(f"Used by: {', '.join(used_by) if used_by else '-'}")
        lines.append(f"📄 source: `{_SOURCE_REL_PATH}:L{int(enum.get('line', 0))}`")
        lines.append("")
        lines.append("| Key | Value |")
        lines.append("|-----|------:|")
        values = enum.get("values", {})
        if isinstance(values, dict):
            for key, value in values.items():
                lines.append(f"| `{_escape_table_cell(key)}` | {_escape_table_cell(value)} |")
        lines.append("")

    lines.extend([f"## {t('section_dictionaries', lang)}", ""])
    constants_by_name = {str(c.get("name", "")): c for c in constants}
    for dictionary in sorted(dictionaries, key=lambda d: (int(d.get("line", 0)), str(d.get("name", "")))):
        name = str(dictionary.get("name", ""))
        lines.append(f"### {name}")
        lines.append("")
        if isinstance(dictionary.get("comment"), str):
            lines.append(dictionary["comment"])
            lines.append("")
        used_by = usage.get(name, [])
        lines.append(f"Used by: {', '.join(used_by) if used_by else '-'}")
        lines.append(f"📄 source: `{_SOURCE_REL_PATH}:L{int(dictionary.get('line', 0))}`")
        keys = dictionary.get("keys", [])
        if isinstance(keys, list) and keys:
            lines.append("Keys: " + ", ".join(f"`{_escape_table_cell(k)}`" for k in keys))
        lines.append("")
        raw_value = ""
        if name in constants_by_name:
            raw_value = str(constants_by_name[name].get("value_raw", ""))
        lines.append("```gdscript")
        lines.append(f"var {name} = {raw_value}")
        lines.append("```")
        lines.append("")

    lines.extend([f"## {t('section_utility_functions', lang)}", ""])
    for function in sorted(functions, key=lambda f: (int(f.get("line", 0)), str(f.get("name", "")))):
        name = str(function.get("name", ""))
        params = str(function.get("params", ""))
        returns = str(function.get("returns", "unknown"))
        lines.append(f"### `{name}({params})`")
        lines.append("")
        if isinstance(function.get("doc_comment"), str):
            lines.append(function["doc_comment"])
            lines.append("")
        lines.append(f"Returns: `{returns}`")
        used_by = usage.get(name, [])
        lines.append(f"Used by: {', '.join(used_by) if used_by else '-'}")
        lines.append(f"📄 source: `{_SOURCE_REL_PATH}:L{int(function.get('line', 0))}`")
        lines.append("")

    lines.extend([_MANUAL_START, "", _MANUAL_END, ""])
    return "\n".join(lines)


def run(manifest: dict, extracted: dict | None = None, lang: str = "ko") -> dict:
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
    del extracted
    dirs = config.lang_dirs(lang)

    constants_path = os.path.join(config.EXTRACTED_DIR, "constants.json")
    references_path = os.path.join(config.EXTRACTED_DIR, "references.json")

    constants_data, constants_error = _read_json(constants_path)
    if constants_error:
        warnings.append(f"Missing or invalid constants.json, skipping: {constants_error}")
        return {
            "files_written": files_written,
            "items_processed": 0,
            "warnings": warnings,
            "errors": errors,
        }

    references_data, references_error = _read_json(references_path)
    if references_error:
        warnings.append(f"Missing or invalid references.json, using empty references: {references_error}")
        references_data = {}

    output_path = os.path.join(dirs["base"], "config-reference.md")
    manual_block = _existing_manual_block(output_path)

    try:
        markdown = _render_markdown(manifest, constants_data, references_data, lang)
    except Exception as exc:
        errors.append(f"Failed to render config reference: {exc}")
        return {
            "files_written": files_written,
            "items_processed": 0,
            "warnings": warnings,
            "errors": errors,
        }

    if manual_block is not None:
        generated_start = markdown.find(_MANUAL_START)
        generated_end = markdown.find(_MANUAL_END, generated_start + len(_MANUAL_START))
        if generated_start >= 0 and generated_end >= 0:
            generated_end += len(_MANUAL_END)
            markdown = (
                markdown[:generated_start]
                + manual_block
                + markdown[generated_end:]
            )

    try:
        config.ensure_dir(dirs["base"])
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(markdown)
    except OSError as exc:
        errors.append(f"Failed to write config-reference.md: {exc}")
        return {
            "files_written": files_written,
            "items_processed": 0,
            "warnings": warnings,
            "errors": errors,
        }

    files_written.append(output_path)
    stats = constants_data.get("stats", {})
    items_processed = (
        int(stats.get("total_constants", 0))
        + int(stats.get("total_enums", 0))
        + int(stats.get("total_dicts", 0))
        + int(stats.get("total_functions", 0))
    )

    return {
        "files_written": files_written,
        "items_processed": items_processed,
        "warnings": warnings,
        "errors": errors,
    }
