"""Extract structured metadata for JSON data files listed in manifest."""

from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from typing import Any

import scripts.config as config


LARGE_FILE_BYTES = 1_000_000
LARGE_ARRAY_SAMPLE_SIZE = 100
SCHEMA_RECURSION_LIMIT = 2


def _json_type(value: Any) -> str:
    if isinstance(value, dict):
        return "object"
    if isinstance(value, list):
        return "array"
    if isinstance(value, str):
        return "string"
    if isinstance(value, bool):
        return "boolean"
    if isinstance(value, (int, float)):
        return "number"
    if value is None:
        return "null"
    return type(value).__name__


def _count_depth(value: Any) -> int:
    if isinstance(value, dict):
        if not value:
            return 1
        return 1 + max(_count_depth(item) for item in value.values())
    if isinstance(value, list):
        if not value:
            return 1
        return 1 + max(_count_depth(item) for item in value)
    return 1


def _count_total_keys(value: Any) -> int:
    if isinstance(value, dict):
        return len(value) + sum(_count_total_keys(item) for item in value.values())
    if isinstance(value, list):
        return sum(_count_total_keys(item) for item in value)
    return 0


def _count_numeric_values(value: Any) -> int:
    if isinstance(value, bool):
        return 0
    if isinstance(value, dict):
        return sum(_count_numeric_values(item) for item in value.values())
    if isinstance(value, list):
        return sum(_count_numeric_values(item) for item in value)
    if isinstance(value, (int, float)):
        return 1
    return 0


def _has_arrays(value: Any) -> bool:
    if isinstance(value, list):
        return True
    if isinstance(value, dict):
        return any(_has_arrays(item) for item in value.values())
    return False


def _is_meta_key(key: str) -> bool:
    return key == "" or key == "comment" or key.startswith("_comment")


def _collect_comment_text(value: Any, comments: list[str]) -> None:
    if isinstance(value, str):
        if value:
            comments.append(value)
        return
    if isinstance(value, list):
        for item in value:
            _collect_comment_text(item, comments)
        return
    if isinstance(value, dict):
        for item in value.values():
            _collect_comment_text(item, comments)
        return
    if value is not None:
        comments.append(str(value))


def _filter_meta_keys(value: Any, comments: list[str]) -> Any:
    if isinstance(value, dict):
        filtered: dict[str, Any] = {}
        for key, item in value.items():
            if _is_meta_key(key):
                _collect_comment_text(item, comments)
                continue
            filtered[key] = _filter_meta_keys(item, comments)
        return filtered
    if isinstance(value, list):
        return [_filter_meta_keys(item, comments) for item in value]
    return value


def _sample_object(value: dict[str, Any], limit: int = 2) -> dict[str, Any]:
    sample: dict[str, Any] = {}
    for key, item in value.items():
        if len(sample) >= limit:
            break
        if isinstance(item, (dict, list)):
            continue
        sample[key] = item
    return sample


def _build_value_schema(value: Any, level: int = 1) -> dict[str, Any]:
    value_type = _json_type(value)

    if value_type == "object":
        schema: dict[str, Any] = {
            "type": "object",
            "keys": list(value.keys()),
            "sample": _sample_object(value),
        }
        if level < SCHEMA_RECURSION_LIMIT:
            schema["schema"] = {
                key: _build_value_schema(item, level + 1)
                for key, item in value.items()
            }
        return schema

    if value_type == "array":
        schema = {
            "type": "array",
            "items": len(value),
        }
        if value:
            first_item = value[0]
            schema["item_type"] = _json_type(first_item)
            if isinstance(first_item, dict):
                schema["sample_item_keys"] = list(first_item.keys())
            if level < SCHEMA_RECURSION_LIMIT:
                schema["sample_item_schema"] = _build_value_schema(first_item, level + 1)
        else:
            schema["item_type"] = "unknown"
        return schema

    primitive_schema: dict[str, Any] = {"type": value_type}
    if value_type in {"string", "number", "boolean", "null"}:
        primitive_schema["value"] = value
    return primitive_schema


def _derive_category(path: str) -> str:
    parts = path.split("/")
    if len(parts) >= 3 and parts[0] == "data":
        return "/".join(parts[1:-1])
    return "unknown"


def _derive_domain(path: str) -> str:
    if path.startswith("data/species/human/personality/"):
        return "personality"
    if path.startswith("data/species/human/emotions/"):
        return "emotions"
    if path.startswith("data/species/human/mortality/"):
        return "mortality"
    if path.startswith("data/emotions/"):
        return "emotions"
    if path.startswith("data/personality/"):
        return "personality"
    if path == "data/stressor_events.json":
        return "stress"

    parts = path.split("/")
    if len(parts) >= 2 and parts[0] == "data" and parts[1]:
        return parts[1]
    return "unknown"


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

    entries = manifest.get("data_files", [])
    if not isinstance(entries, list):
        warnings.append("manifest.data_files is not a list; no data files processed")
        entries = []

    files: list[dict[str, Any]] = []
    categories: dict[str, list[str]] = {}
    by_type: dict[str, int] = {}

    for entry in entries:
        if not isinstance(entry, dict):
            warnings.append("skipping non-dict data_files entry")
            continue

        rel_path = entry.get("file")
        if not rel_path:
            warnings.append("skipping data_files entry with missing file path")
            continue

        source_file = config.source_path(rel_path)
        if not os.path.exists(source_file):
            warnings.append(f"missing file: {rel_path}")
            continue

        try:
            with open(source_file, "r", encoding="utf-8") as f:
                parsed = json.load(f)
        except json.JSONDecodeError as exc:
            warnings.append(f"invalid JSON in {rel_path}: {exc}")
            continue
        except OSError as exc:
            warnings.append(f"failed to read {rel_path}: {exc}")
            continue

        meta_comments: list[str] = []
        filtered_parsed = _filter_meta_keys(parsed, meta_comments)

        value_type = _json_type(filtered_parsed)
        if value_type == "object":
            top_level_keys = list(filtered_parsed.keys())
            schema: Any = {
                key: _build_value_schema(value)
                for key, value in filtered_parsed.items()
            }
        else:
            top_level_keys = []
            schema = _build_value_schema(filtered_parsed)

        file_size = os.path.getsize(source_file)
        full_content = filtered_parsed
        if (
            value_type == "array"
            and file_size > LARGE_FILE_BYTES
            and isinstance(filtered_parsed, list)
        ):
            full_content = filtered_parsed[:LARGE_ARRAY_SAMPLE_SIZE]

        category = entry.get("category") or _derive_category(rel_path)
        domain = _derive_domain(rel_path)
        categories.setdefault(category, []).append(rel_path)
        by_type[value_type] = by_type.get(value_type, 0) + 1

        files.append(
            {
                "file": rel_path,
                "category": category,
                "domain": domain,
                "type": value_type,
                "top_level_keys": top_level_keys,
                "schema": schema,
                "full_content": full_content,
                "_meta_comments": meta_comments,
                "stats": {
                    "total_keys": _count_total_keys(filtered_parsed),
                    "numeric_value_count": _count_numeric_values(filtered_parsed),
                    "nested_depth": _count_depth(filtered_parsed),
                    "has_arrays": _has_arrays(filtered_parsed),
                },
            }
        )

    output_data = {
        "extracted_at": datetime.now(timezone.utc).isoformat(),
        "files": files,
        "categories": categories,
        "stats": {
            "total_files": len(files),
            "total_categories": len(categories),
            "by_type": by_type,
        },
    }

    config.ensure_dir(config.EXTRACTED_DIR)
    output_path = os.path.join(config.EXTRACTED_DIR, "data_files.json")
    try:
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(output_data, f, ensure_ascii=False, indent=2)
            f.write("\n")
        files_written.append(output_path)
    except OSError as exc:
        errors.append(f"failed to write {output_path}: {exc}")

    return {
        "files_written": files_written,
        "items_processed": len(files),
        "warnings": warnings,
        "errors": errors,
    }
