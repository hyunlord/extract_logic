"""Phase 2 locale extractor.

Builds a unified Korean/English glossary from source localization files and
writes extracted/locale.json.
"""

import json
import os
from datetime import datetime, timezone

import scripts.config as config


def _normalize_locale_value(value) -> str:
    """Convert locale JSON values to stable string representation."""
    if isinstance(value, str):
        return value
    if isinstance(value, (dict, list)):
        return json.dumps(value, ensure_ascii=False, sort_keys=True)
    if value is None:
        return ""
    return str(value)


def _load_locale_file(relative_path: str, warnings: list[str]) -> dict[str, str]:
    """Load locale JSON file from SOURCE_REPO; warn and return empty dict on failure."""
    full_path = config.source_path(relative_path)
    if not os.path.exists(full_path):
        warnings.append(f"Locale file not found: {relative_path}")
        return {}

    try:
        with open(full_path, "r", encoding="utf-8") as handle:
            data = json.load(handle)
    except (OSError, json.JSONDecodeError) as exc:
        warnings.append(f"Failed to read locale file {relative_path}: {exc}")
        return {}

    if not isinstance(data, dict):
        warnings.append(f"Locale file is not an object and was skipped: {relative_path}")
        return {}

    return {
        str(key): _normalize_locale_value(value)
        for key, value in data.items()
    }


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

    locale_entries = manifest.get("locale_files", [])
    if not isinstance(locale_entries, list):
        warnings.append("manifest.locale_files is not a list; using empty list")
        locale_entries = []

    manifest_categories = manifest.get("locale_categories", [])
    if not isinstance(manifest_categories, list):
        warnings.append("manifest.locale_categories is not a list; using discovered categories only")
        manifest_categories = []

    grouped: dict[str, dict[str, str]] = {}
    for entry in locale_entries:
        if not isinstance(entry, dict):
            warnings.append("Skipping malformed locale manifest entry (not an object)")
            continue

        category = entry.get("category")
        lang = entry.get("lang")
        file_path = entry.get("file")

        if not isinstance(category, str) or not category:
            warnings.append("Skipping locale entry missing category")
            continue
        if lang not in {"en", "ko"}:
            warnings.append(f"Skipping locale entry with unsupported language '{lang}' in category '{category}'")
            continue
        if not isinstance(file_path, str) or not file_path:
            warnings.append(f"Skipping locale entry missing file path for category '{category}'/{lang}")
            continue

        grouped.setdefault(category, {})
        if lang in grouped[category]:
            warnings.append(f"Duplicate locale file for category '{category}'/{lang}; keeping first")
            continue
        grouped[category][lang] = file_path

    category_order: list[str] = []
    seen_categories: set[str] = set()
    for category in manifest_categories:
        if isinstance(category, str) and category and category not in seen_categories:
            category_order.append(category)
            seen_categories.add(category)
    for category in sorted(grouped.keys()):
        if category not in seen_categories:
            category_order.append(category)
            seen_categories.add(category)

    categories_output: dict = {}
    keys_only_en: list[str] = []
    keys_only_ko: list[str] = []
    total_keys = 0
    total_missing_en = 0
    total_missing_ko = 0

    for category in category_order:
        lang_files = grouped.get(category, {})

        en_data = {}
        ko_data = {}

        if "en" in lang_files:
            en_data = _load_locale_file(lang_files["en"], warnings)
        else:
            warnings.append(f"Missing en locale file for category '{category}'")

        if "ko" in lang_files:
            ko_data = _load_locale_file(lang_files["ko"], warnings)
        else:
            warnings.append(f"Missing ko locale file for category '{category}'")

        all_keys = sorted(set(en_data.keys()) | set(ko_data.keys()))
        merged_keys = {}

        missing_en = 0
        missing_ko = 0

        for key in all_keys:
            in_en = key in en_data
            in_ko = key in ko_data

            if not in_en:
                missing_en += 1
                total_missing_en += 1
                keys_only_ko.append(f"{category}:{key}")
            if not in_ko:
                missing_ko += 1
                total_missing_ko += 1
                keys_only_en.append(f"{category}:{key}")

            merged_keys[key] = {
                "en": en_data.get(key, ""),
                "ko": ko_data.get(key, ""),
            }

        categories_output[category] = {
            "keys": merged_keys,
            "stats": {
                "total_keys": len(all_keys),
                "missing_en": missing_en,
                "missing_ko": missing_ko,
            },
        }
        total_keys += len(all_keys)

    locale_output = {
        "extracted_at": datetime.now(timezone.utc).isoformat(),
        "languages": ["en", "ko"],
        "categories": categories_output,
        "stats": {
            "total_keys": total_keys,
            "total_categories": len(categories_output),
            "languages": 2,
            "missing_translations": {
                "en": total_missing_en,
                "ko": total_missing_ko,
            },
            "keys_only_en": sorted(keys_only_en),
            "keys_only_ko": sorted(keys_only_ko),
        },
    }

    config.ensure_dir(config.EXTRACTED_DIR)
    output_path = os.path.join(config.EXTRACTED_DIR, "locale.json")
    try:
        with open(output_path, "w", encoding="utf-8") as handle:
            handle.write(json.dumps(locale_output, indent=2, ensure_ascii=False))
            handle.write("\n")
    except OSError as exc:
        errors.append(f"Failed to write locale output: {exc}")
        return {
            "files_written": [],
            "items_processed": total_keys,
            "warnings": warnings,
            "errors": errors,
        }

    return {
        "files_written": [output_path],
        "items_processed": total_keys,
        "warnings": warnings,
        "errors": errors,
    }
