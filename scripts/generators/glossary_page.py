"""Phase 3 glossary page generator.

Reads extracted/locale.json and generates bilingual Korean/English glossary
pages by category under content/glossary/.
"""

import json
import os

import scripts.config as config


MANUAL_START = "<!-- MANUAL:START -->"
MANUAL_END = "<!-- MANUAL:END -->"


def _escape_table_cell(value: str) -> str:
    """Escape markdown table delimiters and normalize line breaks."""
    return value.replace("|", "\\|").replace("\n", "<br>")


def _escape_yaml_string(value: str) -> str:
    """Escape string for inclusion in double-quoted YAML scalar."""
    return value.replace("\\", "\\\\").replace('"', '\\"')


def _manual_block(text: str) -> str:
    """Extract MANUAL marker block (inclusive) from markdown text."""
    start = text.find(MANUAL_START)
    if start == -1:
        return ""
    end = text.find(MANUAL_END, start)
    if end == -1:
        return ""
    end += len(MANUAL_END)
    return text[start:end]


def _preserve_manual_block(new_text: str, existing_text: str) -> str:
    """Preserve existing MANUAL block content when regenerating files."""
    existing_block = _manual_block(existing_text)
    if not existing_block:
        return new_text

    new_start = new_text.find(MANUAL_START)
    if new_start == -1:
        if not new_text.endswith("\n"):
            new_text += "\n"
        return f"{new_text}\n{existing_block}\n"

    new_end = new_text.find(MANUAL_END, new_start)
    if new_end == -1:
        if not new_text.endswith("\n"):
            new_text += "\n"
        return f"{new_text}\n{existing_block}\n"

    new_end += len(MANUAL_END)
    return f"{new_text[:new_start]}{existing_block}{new_text[new_end:]}"


def _write_markdown(path: str, content: str, warnings: list[str], errors: list[str]) -> bool:
    """Write markdown file with MANUAL block preservation if file exists."""
    existing_text = ""
    if os.path.exists(path):
        try:
            with open(path, "r", encoding="utf-8") as handle:
                existing_text = handle.read()
        except OSError as exc:
            warnings.append(f"Failed to read existing file for MANUAL preservation {path}: {exc}")

    if existing_text:
        content = _preserve_manual_block(content, existing_text)

    try:
        with open(path, "w", encoding="utf-8") as handle:
            handle.write(content)
            if not content.endswith("\n"):
                handle.write("\n")
    except OSError as exc:
        errors.append(f"Failed to write glossary page {path}: {exc}")
        return False
    return True


def _collect_source_files_for_category(manifest: dict, category: str, warnings: list[str]) -> list[str]:
    """Collect source locale files from manifest for a specific category."""
    locale_entries = manifest.get("locale_files", [])
    if not isinstance(locale_entries, list):
        warnings.append("manifest.locale_files is not a list; source_files will be empty")
        return []

    files: set[str] = set()
    for entry in locale_entries:
        if not isinstance(entry, dict):
            continue
        if entry.get("category") != category:
            continue
        file_path = entry.get("file")
        if isinstance(file_path, str) and file_path:
            files.add(file_path)
    return sorted(files)


def _collect_all_source_files(manifest: dict, warnings: list[str]) -> list[str]:
    """Collect all locale source files from manifest for index frontmatter."""
    locale_entries = manifest.get("locale_files", [])
    if not isinstance(locale_entries, list):
        warnings.append("manifest.locale_files is not a list; index source_files will be empty")
        return []

    files: set[str] = set()
    for entry in locale_entries:
        if not isinstance(entry, dict):
            continue
        file_path = entry.get("file")
        if isinstance(file_path, str) and file_path:
            files.add(file_path)
    return sorted(files)


def _frontmatter(
    title: str,
    description: str,
    nav_order: int,
    source_files: list[str],
) -> str:
    """Build YAML frontmatter string."""
    lines = [
        "---",
        f'title: "{_escape_yaml_string(title)}"',
        f'description: "{_escape_yaml_string(description)}"',
        "generated: true",
    ]

    if source_files:
        lines.append("source_files:")
        for source_file in source_files:
            lines.append(f'  - "{_escape_yaml_string(source_file)}"')
    else:
        lines.append("source_files: []")

    lines.extend(
        [
            f"nav_order: {nav_order}",
            "---",
            "",
        ]
    )
    return "\n".join(lines)


def _render_category_page(
    category: str,
    keys_data: dict,
    nav_order: int,
    source_files: list[str],
) -> tuple[str, int]:
    """Render markdown for a single glossary category page."""
    key_names = sorted(str(key) for key in keys_data.keys())
    total_entries = len(key_names)

    lines = [
        _frontmatter(
            title=f"용어 사전 — {category}",
            description=f"{category} 한영 대조 용어",
            nav_order=nav_order,
            source_files=source_files,
        ),
        f"# {category} 용어 / Glossary",
        "",
        f"총 {total_entries}개 항목 | Total {total_entries} entries",
        "",
        "## 용어 목록",
        "",
        "| Key | 한국어 | English |",
        "|-----|--------|---------|",
    ]

    for key_name in key_names:
        item = keys_data.get(key_name, {})
        ko_raw = ""
        en_raw = ""
        if isinstance(item, dict):
            ko_raw = str(item.get("ko", "") or "")
            en_raw = str(item.get("en", "") or "")

        ko_text = ko_raw if ko_raw else "⚠️ 미번역"
        en_text = en_raw if en_raw else "⚠️ untranslated"

        lines.append(
            "| `{key}` | {ko} | {en} |".format(
                key=_escape_table_cell(key_name),
                ko=_escape_table_cell(ko_text),
                en=_escape_table_cell(en_text),
            )
        )

    lines.extend(
        [
            "",
            "## 수동 메모 / Manual Notes",
            "",
            MANUAL_START,
            MANUAL_END,
            "",
        ]
    )

    return "\n".join(lines), total_entries


def _render_index_page(
    category_counts: list[tuple[str, int]],
    total_entries: int,
    source_files: list[str],
) -> str:
    """Render glossary overview page."""
    total_categories = len(category_counts)
    lines = [
        _frontmatter(
            title="용어 사전",
            description="카테고리별 한영 대조 용어",
            nav_order=0,
            source_files=source_files,
        ),
        "# 용어 사전 / Glossary Index",
        "",
        f"총 {total_categories}개 카테고리 | Total {total_categories} categories",
        "",
        f"총 {total_entries}개 항목 | Total {total_entries} entries",
        "",
        "## 카테고리별 통계 / Category Stats",
        "",
        "| Category | 항목 수 | Entries |",
        "|----------|-------:|--------:|",
    ]

    for category, count in category_counts:
        safe_category = _escape_table_cell(category)
        lines.append(f"| [{safe_category}]({safe_category}.md) | {count} | {count} |")

    lines.extend(
        [
            "",
            "## 수동 메모 / Manual Notes",
            "",
            MANUAL_START,
            MANUAL_END,
            "",
        ]
    )
    return "\n".join(lines)


def run(manifest: dict) -> dict:
    """Generate glossary markdown pages from extracted locale data.

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
    items_processed = 0

    locale_path = os.path.join(config.EXTRACTED_DIR, "locale.json")
    if not os.path.exists(locale_path):
        warnings.append(f"Locale extract not found, skipping glossary generation: {locale_path}")
        return {
            "files_written": files_written,
            "items_processed": items_processed,
            "warnings": warnings,
            "errors": errors,
        }

    try:
        with open(locale_path, "r", encoding="utf-8") as handle:
            locale_data = json.load(handle)
    except (OSError, json.JSONDecodeError) as exc:
        warnings.append(f"Failed to load locale extract, skipping glossary generation: {exc}")
        return {
            "files_written": files_written,
            "items_processed": items_processed,
            "warnings": warnings,
            "errors": errors,
        }

    if not isinstance(locale_data, dict):
        warnings.append("locale.json is not an object; skipping glossary generation")
        return {
            "files_written": files_written,
            "items_processed": items_processed,
            "warnings": warnings,
            "errors": errors,
        }

    categories_data = locale_data.get("categories", {})
    if not isinstance(categories_data, dict):
        warnings.append("locale.json.categories is not an object; skipping glossary generation")
        return {
            "files_written": files_written,
            "items_processed": items_processed,
            "warnings": warnings,
            "errors": errors,
        }

    config.ensure_dir(config.CONTENT_GLOSSARY)

    sorted_categories = sorted(str(category) for category in categories_data.keys())
    category_counts: list[tuple[str, int]] = []

    for nav_order, category in enumerate(sorted_categories, start=1):
        category_payload = categories_data.get(category, {})
        keys_data = {}
        if isinstance(category_payload, dict):
            maybe_keys_data = category_payload.get("keys", {})
            if isinstance(maybe_keys_data, dict):
                keys_data = maybe_keys_data
            else:
                warnings.append(f"Category '{category}' has invalid keys payload; generating empty table")
        else:
            warnings.append(f"Category '{category}' payload is invalid; generating empty table")

        source_files = _collect_source_files_for_category(manifest, category, warnings)
        page_content, entry_count = _render_category_page(
            category=category,
            keys_data=keys_data,
            nav_order=nav_order,
            source_files=source_files,
        )
        output_path = os.path.join(config.CONTENT_GLOSSARY, f"{category}.md")
        if _write_markdown(output_path, page_content, warnings, errors):
            files_written.append(output_path)
            category_counts.append((category, entry_count))
            items_processed += entry_count

    index_content = _render_index_page(
        category_counts=category_counts,
        total_entries=items_processed,
        source_files=_collect_all_source_files(manifest, warnings),
    )
    index_path = os.path.join(config.CONTENT_GLOSSARY, "_index.md")
    if _write_markdown(index_path, index_content, warnings, errors):
        files_written.append(index_path)

    return {
        "files_written": files_written,
        "items_processed": items_processed,
        "warnings": warnings,
        "errors": errors,
    }
