"""Phase 2 extractor for GDScript systems into extracted/systems.json."""

from __future__ import annotations

import json
import os
import re
from datetime import datetime, timezone
from typing import Any

import scripts.config as config

_FUNC_RE = re.compile(
    r"^(?:static\s+)?func\s+([A-Za-z_]\w*)\s*\(([^)]*)\)\s*(?:->\s*([^:]+))?:"
)
_VAR_RE = re.compile(
    r"^(?:static\s+)?var\s+([A-Za-z_]\w+)(?::\s*([^=]+))?(?:\s*=\s*(.+))?$"
)
_CONST_RE = re.compile(r"^const\s+([A-Za-z_]\w+)(?::\s*([^=]+))?\s*=\s*(.+)$")
_CALL_RE = re.compile(r"\b([A-Za-z_]\w*(?:\.[A-Za-z_]\w+)+)\b")
_TOP_LEVEL_DECL_RE = re.compile(r"^(?:(?:static\s+)?func|var|const|signal)\b")


def _is_top_level(line: str) -> bool:
    return len(line) == len(line.lstrip(" \t"))


def _strip_inline_comment(value: str | None) -> str | None:
    if value is None:
        return None
    return value.split("#", 1)[0].strip()


def _get_doc_comment(lines: list[str], index: int) -> str:
    doc_lines: list[str] = []
    cursor = index - 1
    while cursor >= 0:
        stripped = lines[cursor].strip()
        if not stripped:
            break
        if not stripped.startswith("##"):
            break
        doc_lines.append(stripped[2:].strip())
        cursor -= 1
    doc_lines.reverse()
    return " ".join(doc_lines).strip()


def _extract_file_doc_comment(lines: list[str]) -> str:
    doc_lines: list[str] = []
    started = False
    for line in lines:
        stripped = line.strip()
        if not stripped:
            if started:
                continue
            continue
        if stripped.startswith("##"):
            started = True
            doc_lines.append(stripped[2:].strip())
            continue
        if stripped.startswith("extends") or stripped.startswith("class_name"):
            if started:
                continue
            continue
        break
    return " ".join(doc_lines).strip()


def _extract_local_vars(body_lines: list[str]) -> list[str]:
    local_vars: list[str] = []
    seen: set[str] = set()
    for line in body_lines:
        stripped = line.lstrip()
        if not stripped.startswith("var "):
            continue
        match = _VAR_RE.match(stripped)
        if not match:
            continue
        name = match.group(1)
        if name not in seen:
            seen.add(name)
            local_vars.append(name)
    return local_vars


def _extract_calls(body_lines: list[str]) -> list[str]:
    calls: set[str] = set()
    for line in body_lines:
        code = line.split("#", 1)[0]
        for call in _CALL_RE.findall(code):
            calls.add(call)
    return sorted(calls)


def _parse_system_file(source_file: str) -> dict[str, Any]:
    with open(source_file, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    class_variables: list[dict[str, Any]] = []
    constants: list[dict[str, Any]] = []
    functions_seed: list[dict[str, Any]] = []

    for index, line in enumerate(lines):
        if not _is_top_level(line):
            continue
        stripped = line.strip()
        if not stripped:
            continue

        var_match = _VAR_RE.match(stripped)
        if var_match:
            class_variables.append(
                {
                    "name": var_match.group(1),
                    "type": (var_match.group(2) or "").strip(),
                    "default": _strip_inline_comment(var_match.group(3)),
                    "line": index + 1,
                }
            )
            continue

        const_match = _CONST_RE.match(stripped)
        if const_match:
            constants.append(
                {
                    "name": const_match.group(1),
                    "value": _strip_inline_comment(const_match.group(3)) or "",
                    "line": index + 1,
                }
            )
            continue

        func_match = _FUNC_RE.match(stripped)
        if func_match:
            functions_seed.append(
                {
                    "_start_index": index,
                    "name": func_match.group(1),
                    "params": func_match.group(2).strip(),
                    "returns": (func_match.group(3) or "Variant").strip(),
                    "line": index + 1,
                    "doc_comment": _get_doc_comment(lines, index),
                }
            )

    functions: list[dict[str, Any]] = []
    for idx, function in enumerate(functions_seed):
        start_index = function["_start_index"]
        end_index = len(lines)
        for cursor in range(start_index + 1, len(lines)):
            stripped = lines[cursor].strip()
            if not stripped:
                continue
            if _is_top_level(lines[cursor]) and _TOP_LEVEL_DECL_RE.match(stripped):
                end_index = cursor
                break

        body_lines = lines[start_index + 1 : end_index]
        functions.append(
            {
                "name": function["name"],
                "params": function["params"],
                "returns": function["returns"],
                "line": function["line"],
                "line_count": max(1, end_index - start_index),
                "doc_comment": function["doc_comment"],
                "calls_to": _extract_calls(body_lines),
                "local_vars": _extract_local_vars(body_lines),
            }
        )

    return {
        "doc_comment": _extract_file_doc_comment(lines),
        "class_variables": class_variables,
        "constants": constants,
        "functions": functions,
        "stats": {
            "total_lines": len(lines),
            "total_functions": len(functions),
            "total_variables": len(class_variables),
            "total_constants": len(constants),
        },
    }


def run(manifest: dict) -> dict:
    """Extract system-level GDScript metadata to extracted/systems.json."""
    warnings: list[str] = []
    errors: list[str] = []
    entries = list(manifest.get("systems", [])) + list(manifest.get("ai_modules", []))
    systems_out: list[dict[str, Any]] = []

    for entry in entries:
        rel_path = entry.get("file", "")
        if not rel_path:
            warnings.append("Skipped entry with missing 'file' in manifest.")
            continue

        source_file = config.source_path(rel_path)
        if not os.path.exists(source_file):
            warnings.append(f"Missing source file, skipped: {rel_path}")
            continue

        try:
            parsed = _parse_system_file(source_file)
            merged = dict(entry)
            if parsed["doc_comment"] and "doc_comment" not in merged:
                merged["doc_comment"] = parsed["doc_comment"]
            merged["class_variables"] = parsed["class_variables"]
            merged["constants"] = parsed["constants"]
            merged["functions"] = parsed["functions"]
            merged["stats"] = parsed["stats"]
            systems_out.append(merged)
        except OSError as exc:
            warnings.append(f"Failed to read {rel_path}: {exc}")
        except Exception as exc:
            errors.append(f"Failed to parse {rel_path}: {exc}")

    total_functions = sum(s["stats"]["total_functions"] for s in systems_out)
    total_lines = sum(s["stats"]["total_lines"] for s in systems_out)
    output = {
        "extracted_at": datetime.now(timezone.utc).isoformat(),
        "systems": systems_out,
        "stats": {
            "total_systems": len(systems_out),
            "total_functions": total_functions,
            "total_lines": total_lines,
        },
    }

    config.ensure_dir(config.EXTRACTED_DIR)
    output_path = os.path.join(config.EXTRACTED_DIR, "systems.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    return {
        "files_written": [output_path],
        "items_processed": len(systems_out),
        "warnings": warnings,
        "errors": errors,
    }
