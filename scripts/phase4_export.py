"""Phase 4: EXPORT — Merge generated markdown pages into LLM-context exports."""

import glob
import os
import re
from datetime import datetime, timezone

import scripts.config as config

TRUNCATION_MARKER = "[TRUNCATED — see full docs]"


def _section_map() -> dict[str, str]:
    """Return content section name -> absolute directory path."""
    return {
        os.path.basename(config.CONTENT_SYSTEMS): config.CONTENT_SYSTEMS,
        os.path.basename(config.CONTENT_DATA): config.CONTENT_DATA,
        os.path.basename(config.CONTENT_INTERACTIONS): config.CONTENT_INTERACTIONS,
        os.path.basename(config.CONTENT_GLOSSARY): config.CONTENT_GLOSSARY,
        os.path.basename(config.CONTENT_CORE): config.CONTENT_CORE,
    }


def _full_export_sections() -> list[tuple[str, str]]:
    """Resolve full export section order from config nav order."""
    section_map = _section_map()
    sections: list[tuple[str, str]] = []

    for _, nav_target in config.NAV_SECTION_ORDER:
        if nav_target in section_map:
            sections.append((nav_target, section_map[nav_target]))

    return sections


def _parse_frontmatter_nav_order(frontmatter: str) -> int:
    """Extract integer nav_order from frontmatter."""
    match = re.search(r"^nav_order\s*:\s*(\d+)\s*$", frontmatter, re.MULTILINE)
    if not match:
        return 1_000_000
    try:
        return int(match.group(1))
    except ValueError:
        return 1_000_000


def _strip_frontmatter(text: str) -> tuple[int, str]:
    """Strip YAML frontmatter and return (nav_order, body_text)."""
    lines = text.splitlines(keepends=True)
    if not lines or lines[0].strip() != "---":
        return 1_000_000, text.strip()

    for idx in range(1, len(lines)):
        if lines[idx].strip() == "---":
            frontmatter = "".join(lines[1:idx])
            body = "".join(lines[idx + 1 :]).strip()
            return _parse_frontmatter_nav_order(frontmatter), body

    # Unclosed frontmatter: keep original content to avoid data loss.
    return 1_000_000, text.strip()


def _read_page(path: str, warnings: list[str]) -> tuple[int, str] | None:
    """Read a markdown page and return (nav_order, body_without_frontmatter)."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
    except OSError as exc:
        warnings.append(f"Failed to read content page: {path} ({exc})")
        return None

    nav_order, body = _strip_frontmatter(text)
    if not body:
        warnings.append(f"Empty page content after frontmatter strip: {path}")
    return nav_order, body


def _collect_pages(
    section_dirs: list[tuple[str, str]],
    warnings: list[str],
) -> list[tuple[str, str]]:
    """Collect pages across sections, sorted by section order and nav_order."""
    collected: list[tuple[int, int, str, str]] = []

    for section_index, (section_name, section_dir) in enumerate(section_dirs):
        pattern = os.path.join(section_dir, "**", "*.md")
        paths = sorted(glob.glob(pattern, recursive=True))
        if not paths:
            continue

        for path in paths:
            page = _read_page(path, warnings)
            if page is None:
                continue

            nav_order, body = page
            relative = os.path.relpath(path, config.CONTENT_DIR).replace(os.sep, "/")
            collected.append((section_index, nav_order, relative, body))

    collected.sort(key=lambda item: (item[0], item[1], item[2]))
    return [(item[2], item[3]) for item in collected]


def _build_header(section_name: str, manifest: dict) -> str:
    """Build standard export header from manifest stats."""
    stats = manifest.get("stats", {}) if isinstance(manifest, dict) else {}
    locale_files = manifest.get("locale_files", []) if isinstance(manifest, dict) else []

    locale_keys = stats.get("total_locale_keys")
    if locale_keys is None:
        locale_keys = sum(
            entry.get("keys_count", 0)
            for entry in locale_files
            if isinstance(entry, dict)
        )

    return "\n".join(
        [
            f"# WorldSim Documentation — {section_name}",
            f"Generated: {datetime.now(timezone.utc).isoformat()} | Source: {manifest.get('source_commit', 'unknown')}",
            f"Systems: {stats.get('total_system_files', len(manifest.get('systems', [])))}"
            f" | Core: {stats.get('total_core_files', len(manifest.get('core_modules', [])))}"
            f" | Data: {stats.get('total_json_data_files', len(manifest.get('data_files', [])))}"
            f" | Locale keys: {locale_keys}",
        ]
    )


def _compose_export(section_name: str, pages: list[tuple[str, str]], manifest: dict) -> str:
    """Compose final export markdown with header and page separators."""
    header = _build_header(section_name, manifest)
    if not pages:
        return f"{header}\n\n---\n"

    page_chunks = [body for _, body in pages]
    merged_pages = "\n\n---\n\n".join(page_chunks)
    return f"{header}\n\n---\n\n{merged_pages}\n\n---\n"


def _truncate_to_max(text: str, max_bytes: int) -> str:
    """Truncate UTF-8 text to max_bytes and append truncation marker."""
    marker_block = f"\n\n{TRUNCATION_MARKER}\n"
    marker_bytes = marker_block.encode("utf-8")
    if max_bytes <= len(marker_bytes):
        return marker_block.encode("utf-8")[:max_bytes].decode("utf-8", errors="ignore")

    encoded = text.encode("utf-8")
    keep_bytes = max_bytes - len(marker_bytes)
    prefix = encoded[:keep_bytes].decode("utf-8", errors="ignore").rstrip()
    return f"{prefix}{marker_block}"


def _write_export(
    output_name: str,
    section_name: str,
    pages: list[tuple[str, str]],
    manifest: dict,
    warnings: list[str],
    errors: list[str],
) -> tuple[str | None, int]:
    """Render, size-check, and write one export file. Returns (path, bytes)."""
    content = _compose_export(section_name, pages, manifest)
    raw_size = len(content.encode("utf-8"))

    if raw_size > config.EXPORT_TARGET_BYTES:
        warnings.append(
            f"{output_name} is {raw_size} bytes, above target {config.EXPORT_TARGET_BYTES} bytes"
        )

    if raw_size > config.EXPORT_MAX_BYTES:
        warnings.append(
            f"{output_name} is {raw_size} bytes, above max {config.EXPORT_MAX_BYTES} bytes; truncating"
        )
        content = _truncate_to_max(content, config.EXPORT_MAX_BYTES)

    output_path = os.path.join(config.EXPORTS_DIR, output_name)
    try:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(content)
    except OSError as exc:
        errors.append(f"Failed to write export file: {output_path} ({exc})")
        return None, 0

    return output_path, len(content.encode("utf-8"))


def run(manifest: dict) -> dict:
    """Run Phase 4 export generation.

    Args:
        manifest: The manifest.json data from Phase 1.

    Returns:
        dict with keys:
            - files_written: list of output file paths
            - items_processed: int count of source pages merged
            - warnings: list of warning strings
            - errors: list of error strings
            - sizes_bytes: dict[path, size_bytes]
    """
    warnings: list[str] = []
    errors: list[str] = []
    files_written: list[str] = []
    sizes_bytes: dict[str, int] = {}

    config.ensure_dir(config.EXPORTS_DIR)

    section_map = _section_map()
    full_sections = _full_export_sections()

    all_sections = [
        (os.path.basename(config.CONTENT_SYSTEMS), config.CONTENT_SYSTEMS),
        (os.path.basename(config.CONTENT_DATA), config.CONTENT_DATA),
        (os.path.basename(config.CONTENT_INTERACTIONS), config.CONTENT_INTERACTIONS),
        (os.path.basename(config.CONTENT_GLOSSARY), config.CONTENT_GLOSSARY),
        (os.path.basename(config.CONTENT_CORE), config.CONTENT_CORE),
    ]
    source_pages = _collect_pages(all_sections, warnings)

    export_specs = [
        ("worldsim-full.md", "Full", full_sections),
        (
            "worldsim-systems.md",
            "Systems",
            [(os.path.basename(config.CONTENT_SYSTEMS), section_map[os.path.basename(config.CONTENT_SYSTEMS)])],
        ),
        (
            "worldsim-data.md",
            "Data",
            [(os.path.basename(config.CONTENT_DATA), section_map[os.path.basename(config.CONTENT_DATA)])],
        ),
        (
            "worldsim-interactions.md",
            "Interactions",
            [(
                os.path.basename(config.CONTENT_INTERACTIONS),
                section_map[os.path.basename(config.CONTENT_INTERACTIONS)],
            )],
        ),
    ]

    for output_name, section_name, section_dirs in export_specs:
        pages = _collect_pages(section_dirs, warnings)
        output_path, output_size = _write_export(
            output_name=output_name,
            section_name=section_name,
            pages=pages,
            manifest=manifest,
            warnings=warnings,
            errors=errors,
        )
        if output_path:
            files_written.append(output_path)
            sizes_bytes[output_path] = output_size

    return {
        "files_written": files_written,
        "items_processed": len(source_pages),
        "warnings": warnings,
        "errors": errors,
        "sizes_bytes": sizes_bytes,
    }
