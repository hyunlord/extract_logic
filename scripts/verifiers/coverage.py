"""Phase 5 coverage verifier for generated documentation pages.

Checks whether manifest-discovered source items have corresponding markdown
pages in content/, then merges results into extracted/verification_report.json.
"""

from __future__ import annotations

import json
import os
import re
from typing import Any

import scripts.config as config


_SLUG_INVALID_RE = re.compile(r"[^a-z0-9_]+")
_MISSING_ERROR_THRESHOLD = 5


def _slugify(value: str) -> str:
    """Convert names to stable filename slugs used by generators."""
    normalized = value.strip().lower().replace("-", "_").replace(" ", "_")
    normalized = _SLUG_INVALID_RE.sub("_", normalized)
    return normalized.strip("_")


def _file_stem(path: str) -> str:
    """Extract a file stem from a relative source path."""
    return os.path.splitext(os.path.basename(path.replace("\\", "/")))[0]


def _system_page_name(entry: dict[str, Any]) -> str:
    """Resolve expected systems-page filename from manifest entry."""
    system_name = entry.get("system_name")
    if isinstance(system_name, str):
        slug = _slugify(system_name)
        if slug:
            return f"{slug}.md"

    file_path = entry.get("file", "")
    stem = _file_stem(file_path) if isinstance(file_path, str) else ""
    if stem.endswith("_system"):
        stem = stem[: -len("_system")]
    slug = _slugify(stem)
    return f"{slug or 'unknown'}.md"


def _core_page_name(entry: dict[str, Any]) -> str:
    """Resolve expected core-page filename from manifest entry."""
    file_path = entry.get("file", "")
    stem = _file_stem(file_path) if isinstance(file_path, str) else ""
    slug = _slugify(stem)
    return f"{slug or 'unknown'}.md"


def _data_page_path(entry: dict[str, Any]) -> str:
    """Resolve expected data-page absolute path from manifest entry."""
    file_path = entry.get("file", "")
    normalized_file = file_path.replace("\\", "/") if isinstance(file_path, str) else ""
    path_parts = [p for p in normalized_file.split("/") if p]

    category = entry.get("category")
    if not isinstance(category, str) or not category.strip():
        if len(path_parts) > 2:
            category = "/".join(path_parts[1:-1])
        else:
            category = ""

    category_parts = [_slugify(part) for part in category.split("/") if _slugify(part)]

    stem = _file_stem(normalized_file)
    slug = _slugify(stem)
    filename = f"{slug or 'unknown'}.md"
    return os.path.join(config.CONTENT_DATA, *category_parts, filename)


def _build_expectations(
    manifest: dict[str, Any], warnings: list[str]
) -> tuple[list[dict[str, str]], list[dict[str, str]], list[dict[str, str]], list[dict[str, str]], list[dict[str, str]]]:
    """Build expected documentation paths from manifest data."""
    systems_expected: list[dict[str, str]] = []
    core_expected: list[dict[str, str]] = []
    data_expected: list[dict[str, str]] = []
    glossary_expected: list[dict[str, str]] = []
    required_expected: list[dict[str, str]] = [
        {"group": "required", "source": "content/config-reference.md", "path": os.path.join(config.CONTENT_DIR, "config-reference.md")},
        {"group": "required", "source": "content/index.md", "path": os.path.join(config.CONTENT_DIR, "index.md")},
    ]

    def _append_from_manifest(
        key: str,
        output: list[dict[str, str]],
        group: str,
        path_builder: Any,
    ) -> None:
        items = manifest.get(key, [])
        if not isinstance(items, list):
            warnings.append(f"manifest.{key} is not a list; skipping")
            return
        for item in items:
            if not isinstance(item, dict):
                warnings.append(f"manifest.{key} contains non-object entry; skipping")
                continue
            source = item.get("file", "")
            if not isinstance(source, str) or not source:
                warnings.append(f"manifest.{key} entry missing file path; skipping")
                continue
            path_value = path_builder(item)
            output.append({"group": group, "source": source, "path": path_value})

    _append_from_manifest(
        key="systems",
        output=systems_expected,
        group="systems",
        path_builder=lambda item: os.path.join(config.CONTENT_SYSTEMS, _system_page_name(item)),
    )
    _append_from_manifest(
        key="ai_modules",
        output=systems_expected,
        group="ai_modules",
        path_builder=lambda item: os.path.join(config.CONTENT_SYSTEMS, _system_page_name(item)),
    )
    _append_from_manifest(
        key="core_modules",
        output=core_expected,
        group="core",
        path_builder=lambda item: os.path.join(config.CONTENT_CORE, _core_page_name(item)),
    )
    _append_from_manifest(
        key="data_files",
        output=data_expected,
        group="data",
        path_builder=_data_page_path,
    )

    categories = manifest.get("locale_categories", [])
    if not isinstance(categories, list):
        warnings.append("manifest.locale_categories is not a list; skipping glossary coverage")
    else:
        for category in categories:
            if category is None:
                warnings.append("manifest.locale_categories contains null entry; skipping")
                continue
            category_name = str(category).strip()
            if not category_name:
                warnings.append("manifest.locale_categories contains empty entry; skipping")
                continue
            glossary_expected.append(
                {
                    "group": "glossary",
                    "source": category_name,
                    "path": os.path.join(config.CONTENT_GLOSSARY, f"{category_name}.md"),
                }
            )

    return systems_expected, core_expected, data_expected, glossary_expected, required_expected


def _check_entries(entries: list[dict[str, str]]) -> tuple[int, list[str], list[dict[str, str]]]:
    """Check expected paths and return documented count + missing details."""
    documented = 0
    missing_paths: list[str] = []
    missing_records: list[dict[str, str]] = []
    for entry in entries:
        path = entry["path"]
        if os.path.exists(path):
            documented += 1
            continue
        rel = os.path.relpath(path, os.getcwd())
        missing_paths.append(rel)
        missing_records.append(
            {
                "group": entry["group"],
                "source": entry["source"],
                "path": rel,
            }
        )
    return documented, missing_paths, missing_records


def _load_existing_report(path: str, warnings: list[str]) -> dict[str, Any]:
    """Load existing verification report if present and valid."""
    if not os.path.exists(path):
        return {}
    try:
        with open(path, "r", encoding="utf-8") as handle:
            data = json.load(handle)
    except (OSError, json.JSONDecodeError) as exc:
        warnings.append(f"Failed to read existing verification report, replacing it: {exc}")
        return {}
    if not isinstance(data, dict):
        warnings.append("Existing verification report is not an object, replacing it")
        return {}
    return data


def run(manifest: dict) -> dict:
    """Check content coverage and merge results into verification_report.json."""
    warnings: list[str] = []
    errors: list[str] = []
    files_written: list[str] = []

    (
        systems_expected,
        core_expected,
        data_expected,
        glossary_expected,
        required_expected,
    ) = _build_expectations(manifest, warnings)

    systems_documented, systems_missing, systems_missing_records = _check_entries(systems_expected)
    core_documented, core_missing, core_missing_records = _check_entries(core_expected)
    data_documented, data_missing, data_missing_records = _check_entries(data_expected)
    glossary_documented, glossary_missing, glossary_missing_records = _check_entries(glossary_expected)
    required_documented, required_missing, required_missing_records = _check_entries(required_expected)

    total_expected = (
        len(systems_expected)
        + len(core_expected)
        + len(data_expected)
        + len(glossary_expected)
        + len(required_expected)
    )
    total_documented = (
        systems_documented
        + core_documented
        + data_documented
        + glossary_documented
        + required_documented
    )
    overall_percent = round((total_documented / total_expected * 100.0), 2) if total_expected else 100.0

    coverage = {
        "systems": {
            "total": len(systems_expected),
            "documented": systems_documented,
            "missing": systems_missing,
        },
        "core": {
            "total": len(core_expected),
            "documented": core_documented,
            "missing": core_missing,
        },
        "data": {
            "total": len(data_expected),
            "documented": data_documented,
            "missing": data_missing,
        },
        "glossary": {
            "total": len(glossary_expected),
            "documented": glossary_documented,
            "missing": glossary_missing,
        },
        "overall_percent": overall_percent,
    }

    missing_records = (
        systems_missing_records
        + core_missing_records
        + data_missing_records
        + glossary_missing_records
        + required_missing_records
    )
    if missing_records:
        target = errors if len(missing_records) >= _MISSING_ERROR_THRESHOLD else warnings
        for item in missing_records:
            target.append(
                f"Missing page [{item['group']}]: {item['path']} (source: {item['source']})"
            )

    if overall_percent < config.COVERAGE_MIN_PERCENT:
        errors.append(
            "Coverage below minimum threshold: "
            f"{overall_percent}% < {config.COVERAGE_MIN_PERCENT}%"
        )

    report_path = os.path.join(config.EXTRACTED_DIR, "verification_report.json")
    config.ensure_dir(config.EXTRACTED_DIR)
    report = _load_existing_report(report_path, warnings)
    report["coverage"] = coverage

    try:
        with open(report_path, "w", encoding="utf-8") as handle:
            json.dump(report, handle, indent=2, ensure_ascii=False)
        files_written.append(report_path)
    except OSError as exc:
        errors.append(f"Failed to write verification report: {exc}")

    items_processed = total_expected
    return {
        "files_written": files_written,
        "items_processed": items_processed,
        "warnings": warnings,
        "errors": errors,
        "coverage": coverage,
    }
