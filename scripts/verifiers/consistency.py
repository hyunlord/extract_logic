"""Verify documented constant values against extracted/constants.json."""

import json
import os
import re

import scripts.config as config

_CODE_SPAN_RE = re.compile(r"`([^`]+)`")
_TABLE_SPLIT_RE = re.compile(r"(?<!\\)\|")
_WS_RE = re.compile(r"\s+")


def _normalize_ws(value: str) -> str:
    """Normalize whitespace for comparison — collapse tabs/newlines/<br> to single space."""
    v = value.replace("<br>", " ").replace("\\n", " ").replace("\\t", " ")
    return _WS_RE.sub(" ", v).strip()


def _to_relpath(path: str) -> str:
    return os.path.relpath(path, start=os.getcwd()).replace(os.sep, "/")


def _normalize_reference_name(code_span: str, known_constants: set[str]) -> str | None:
    if code_span in known_constants:
        return code_span
    if "." in code_span:
        suffix = code_span.rsplit(".", 1)[-1]
        if suffix in known_constants:
            return suffix
    return None


def _extract_value_after_constant(line: str, marker_end: int) -> str | None:
    tail = line[marker_end:]

    code_match = re.match(r"\s*(?::|=|->|is)?\s*`([^`]+)`", tail)
    if code_match:
        return code_match.group(1).strip()

    plain_match = re.match(r"\s*(?::|=|->|is)\s*([^\s|,;]+)", tail)
    if plain_match:
        return plain_match.group(1).strip().strip("`")

    return None


def _split_markdown_row(line: str) -> list[str]:
    parts = _TABLE_SPLIT_RE.split(line.strip())
    if not parts:
        return []
    if parts[0] == "":
        parts = parts[1:]
    if parts and parts[-1] == "":
        parts = parts[:-1]
    return [part.strip() for part in parts]


def _is_separator_row(cells: list[str]) -> bool:
    if not cells:
        return False
    for cell in cells:
        token = cell.replace(" ", "")
        if not re.fullmatch(r":?-{3,}:?", token):
            return False
    return True


def _extract_value_from_cell(cell: str) -> str | None:
    code_match = _CODE_SPAN_RE.search(cell)
    if code_match:
        return code_match.group(1).strip()

    plain = cell.replace("\\|", "|").strip()
    if not plain:
        return None
    return plain


def _extract_pairs_from_table_row(
    line: str, known_constants: set[str], line_no: int
) -> list[tuple[str, str, int]]:
    cells = _split_markdown_row(line)
    if len(cells) < 2 or _is_separator_row(cells):
        return []

    pairs: list[tuple[str, str, int]] = []

    for idx, cell in enumerate(cells):
        for code_match in _CODE_SPAN_RE.finditer(cell):
            const_name = _normalize_reference_name(code_match.group(1).strip(), known_constants)
            if not const_name:
                continue

            value = _extract_value_after_constant(cell, code_match.end())
            if value is None and idx + 1 < len(cells):
                value = _extract_value_from_cell(cells[idx + 1])
            if value is None and idx > 0:
                value = _extract_value_from_cell(cells[idx - 1])

            if value is not None:
                pairs.append((const_name, value, line_no))

    return pairs


def _extract_pairs_from_inline_line(
    line: str, known_constants: set[str], line_no: int
) -> list[tuple[str, str, int]]:
    pairs: list[tuple[str, str, int]] = []
    for code_match in _CODE_SPAN_RE.finditer(line):
        const_name = _normalize_reference_name(code_match.group(1).strip(), known_constants)
        if not const_name:
            continue

        value = _extract_value_after_constant(line, code_match.end())
        if value is not None:
            pairs.append((const_name, value, line_no))

    return pairs


def _extract_constant_pairs(text: str, known_constants: set[str]) -> list[tuple[str, str, int]]:
    pairs: list[tuple[str, str, int]] = []
    in_code_fence = False

    for line_no, line in enumerate(text.splitlines(), start=1):
        stripped = line.strip()
        if stripped.startswith("```"):
            in_code_fence = not in_code_fence
            continue
        if in_code_fence:
            continue

        if "|" in line:
            pairs.extend(_extract_pairs_from_table_row(line, known_constants, line_no))
        else:
            pairs.extend(_extract_pairs_from_inline_line(line, known_constants, line_no))

    return pairs


def _load_constants(warnings: list[str], errors: list[str]) -> dict[str, str]:
    constants_path = os.path.join(config.EXTRACTED_DIR, "constants.json")
    if not os.path.exists(constants_path):
        warnings.append(f"Missing constants.json, skipping consistency check: {_to_relpath(constants_path)}")
        return {}

    try:
        with open(constants_path, "r", encoding="utf-8") as handle:
            payload = json.load(handle)
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"Failed to load constants.json: {exc}")
        return {}

    entries = payload.get("constants", [])
    if not isinstance(entries, list):
        errors.append("Invalid constants.json: 'constants' must be a list")
        return {}

    constants: dict[str, str] = {}
    for item in entries:
        if not isinstance(item, dict):
            continue
        name = item.get("name")
        if not isinstance(name, str) or not name:
            continue
        constants[name] = str(item.get("value", ""))

    if not constants:
        warnings.append("No constants found in extracted/constants.json")

    return constants


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
            - consistency: summary of checks and mismatches
    """
    _ = manifest
    warnings: list[str] = []
    errors: list[str] = []

    constants = _load_constants(warnings, errors)
    known_constants = set(constants.keys())

    mismatches: list[dict] = []
    checked = 0
    matches = 0

    if known_constants:
        if not os.path.isdir(config.CONTENT_DIR):
            warnings.append(f"Content directory not found: {_to_relpath(config.CONTENT_DIR)}")
        else:
            config_ref_path = os.path.join(config.CONTENT_KO, "config-reference.md")
            markdown_files: list[str] = []
            for root, _, files in os.walk(config.CONTENT_DIR):
                for filename in sorted(files):
                    if filename.endswith(".md"):
                        markdown_files.append(os.path.join(root, filename))

            for path in sorted(markdown_files):
                if os.path.normpath(path) == os.path.normpath(config_ref_path):
                    continue

                try:
                    with open(path, "r", encoding="utf-8") as handle:
                        text = handle.read()
                except OSError as exc:
                    warnings.append(f"Failed to read {_to_relpath(path)}: {exc}")
                    continue

                for const_name, documented, _ in _extract_constant_pairs(text, known_constants):
                    checked += 1
                    actual = constants.get(const_name, "")
                    if _normalize_ws(documented) == _normalize_ws(actual):
                        matches += 1
                        continue
                    mismatches.append(
                        {
                            "constant": const_name,
                            "file": _to_relpath(path),
                            "documented": documented,
                            "actual": actual,
                        }
                    )

            if os.path.exists(config_ref_path):
                try:
                    with open(config_ref_path, "r", encoding="utf-8") as handle:
                        config_ref_text = handle.read()
                except OSError as exc:
                    warnings.append(f"Failed to read {_to_relpath(config_ref_path)}: {exc}")
                else:
                    ref_pairs = _extract_constant_pairs(config_ref_text, known_constants)
                    ref_map: dict[str, str] = {}
                    for const_name, documented, _ in ref_pairs:
                        ref_map[const_name] = documented

                    for const_name, actual in constants.items():
                        checked += 1
                        documented = ref_map.get(const_name)
                        if documented is None:
                            mismatches.append(
                                {
                                    "constant": const_name,
                                    "file": _to_relpath(config_ref_path),
                                    "documented": "<missing>",
                                    "actual": actual,
                                }
                            )
                            continue
                        if _normalize_ws(documented) == _normalize_ws(actual):
                            matches += 1
                        else:
                            mismatches.append(
                                {
                                    "constant": const_name,
                                    "file": _to_relpath(config_ref_path),
                                    "documented": documented,
                                    "actual": actual,
                                }
                            )
            else:
                warnings.append(f"Missing config reference file: {_to_relpath(config_ref_path)}")

    for mismatch in mismatches:
        errors.append(
            "Constant mismatch in {file}: {constant} documented '{documented}' != actual '{actual}'".format(
                **mismatch
            )
        )

    return {
        "files_written": [],
        "items_processed": checked,
        "warnings": warnings,
        "errors": errors,
        "consistency": {
            "checked": checked,
            "matches": matches,
            "mismatches": mismatches,
        },
    }
