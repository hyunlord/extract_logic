"""Verify internal Markdown links in generated content pages."""

from __future__ import annotations

import glob
import os
import re
from urllib.parse import unquote

import scripts.config as config


LINK_PATTERN = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
HEADING_PATTERN = re.compile(r"^\s{0,3}#{1,6}\s+(.+?)\s*$")


def _to_repo_relative(path: str, repo_root: str) -> str:
    return os.path.relpath(path, repo_root).replace(os.sep, "/")


def _extract_link_target(raw_target: str) -> str:
    target = raw_target.strip()
    if target.startswith("<") and ">" in target:
        return target[1:target.find(">")].strip()
    return target.split()[0] if target else ""


def _normalize_slug(value: str) -> str:
    normalized = value.strip().lower()
    normalized = re.sub(r"`([^`]*)`", r"\1", normalized)
    normalized = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", normalized)
    normalized = re.sub(r"<[^>]+>", "", normalized)
    normalized = re.sub(r"\s+#+\s*$", "", normalized)
    normalized = re.sub(r"[^\w\s-]", "", normalized)
    normalized = re.sub(r"[\s_-]+", "-", normalized).strip("-")
    return normalized


def _collect_heading_slugs(path: str) -> set[str]:
    slugs: set[str] = set()
    with open(path, "r", encoding="utf-8") as handle:
        for line in handle:
            heading_match = HEADING_PATTERN.match(line)
            if not heading_match:
                continue
            slug = _normalize_slug(heading_match.group(1))
            if slug:
                slugs.add(slug)
    return slugs


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
            - links: link verification summary
    """
    _ = manifest
    warnings: list[str] = []
    errors: list[str] = []

    repo_root = os.path.dirname(config.CONTENT_DIR)
    md_files = sorted(glob.glob(os.path.join(config.CONTENT_DIR, "**", "*.md"), recursive=True))

    total_links = 0
    valid_links = 0
    external_skipped = 0
    broken: list[dict[str, object]] = []
    heading_cache: dict[str, set[str]] = {}

    if not os.path.isdir(config.CONTENT_DIR):
        warnings.append(f"Content directory not found: {config.CONTENT_DIR}")

    for page_path in md_files:
        try:
            with open(page_path, "r", encoding="utf-8") as handle:
                lines = handle.readlines()
        except OSError as exc:
            warnings.append(f"Failed to read markdown file {page_path}: {exc}")
            continue

        page_dir = os.path.dirname(page_path)
        for line_no, line in enumerate(lines, start=1):
            for match in LINK_PATTERN.finditer(line):
                link_target = _extract_link_target(match.group(1))
                if not link_target:
                    continue

                total_links += 1
                lower_target = link_target.lower()
                if lower_target.startswith("http://") or lower_target.startswith("https://"):
                    external_skipped += 1
                    continue

                anchor = ""
                link_path = link_target
                if "#" in link_target:
                    link_path, anchor = link_target.split("#", 1)

                if link_path.startswith("/"):
                    resolved = os.path.normpath(os.path.join(config.CONTENT_DIR, link_path.lstrip("/")))
                elif link_path:
                    resolved = os.path.normpath(os.path.join(page_dir, link_path))
                else:
                    resolved = page_path

                if not os.path.exists(resolved):
                    broken.append(
                        {
                            "file": _to_repo_relative(page_path, repo_root),
                            "line": line_no,
                            "link": link_target,
                            "resolved": _to_repo_relative(resolved, repo_root),
                        }
                    )
                    continue

                valid_links += 1
                if not anchor:
                    continue

                target_anchor = _normalize_slug(unquote(anchor))
                if not target_anchor:
                    continue

                if resolved not in heading_cache:
                    try:
                        heading_cache[resolved] = _collect_heading_slugs(resolved)
                    except OSError as exc:
                        warnings.append(f"Failed to read headings from {resolved}: {exc}")
                        heading_cache[resolved] = set()

                if target_anchor not in heading_cache[resolved]:
                    warnings.append(
                        "Missing anchor target: "
                        f"{_to_repo_relative(page_path, repo_root)}:{line_no} -> {link_target}"
                    )

    if broken:
        errors.append(f"Found {len(broken)} broken internal links")

    return {
        "files_written": [],
        "items_processed": total_links,
        "warnings": warnings,
        "errors": errors,
        "links": {
            "total_links": total_links,
            "valid": valid_links,
            "broken": broken,
            "external_skipped": external_skipped,
        },
    }
