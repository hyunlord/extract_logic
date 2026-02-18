"""Completeness verifier for generated markdown pages.

Scans generated content pages for incomplete markers such as TODO/FIXME.
"""

from __future__ import annotations

import os
import re

import scripts.config as config


# "Containing" means substring match, case-insensitive (no word-boundary guards).
_MARKER_PATTERN = re.compile(r"(?:TODO|PLACEHOLDER|FIXME|XXX|NOT IMPLEMENTED|TBD)", re.IGNORECASE)
_FRONTMATTER_PATTERN = re.compile(r"^---\r?\n(.*?)\r?\n---(?:\r?\n|$)", re.DOTALL)
_GENERATED_PATTERN = re.compile(r"^generated\s*:\s*(.+)$", re.MULTILINE)


def _is_generated_page(text: str) -> bool:
    """Return True when markdown frontmatter contains generated: true."""
    frontmatter_match = _FRONTMATTER_PATTERN.match(text)
    if not frontmatter_match:
        return False

    generated_match = _GENERATED_PATTERN.search(frontmatter_match.group(1))
    if not generated_match:
        return False

    generated_raw = generated_match.group(1).split("#", 1)[0].strip()
    generated_value = generated_raw.strip("'\"").lower()
    return generated_value == "true"


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
        plus:
            - completeness: detailed completeness verification results
    """
    del manifest  # Completeness check operates on generated markdown only.

    warnings: list[str] = []
    errors: list[str] = []
    violations: list[dict[str, object]] = []
    files_checked = 0

    if not os.path.isdir(config.CONTENT_DIR):
        warnings.append(f"content directory not found: {config.CONTENT_DIR}")
    else:
        repo_root = os.path.dirname(config.CONTENT_DIR)
        manual_dir = os.path.normpath(config.CONTENT_MANUAL)

        for root, dirs, files in os.walk(config.CONTENT_DIR):
            root_norm = os.path.normpath(root)
            if root_norm == manual_dir:
                dirs[:] = []
                continue

            dirs[:] = [d for d in dirs if d != "_manual"]

            for name in files:
                if not name.endswith(".md"):
                    continue

                file_path = os.path.join(root, name)
                try:
                    with open(file_path, "r", encoding="utf-8") as handle:
                        content = handle.read()
                except OSError as exc:
                    warnings.append(f"failed to read {file_path}: {exc}")
                    continue

                if not _is_generated_page(content):
                    continue

                files_checked += 1
                for line_num, line in enumerate(content.splitlines(), start=1):
                    if _MARKER_PATTERN.search(line):
                        violations.append(
                            {
                                "file": os.path.relpath(file_path, repo_root),
                                "line": line_num,
                                "text": line.rstrip(),
                            }
                        )

    clean = files_checked - len({entry["file"] for entry in violations})
    completeness = {
        "files_checked": files_checked,
        "clean": clean,
        "violations": violations,
    }

    if len(violations) > config.MAX_ALLOWED_TODOS:
        errors.append(
            "completeness failed: "
            f"{len(violations)} violations exceed MAX_ALLOWED_TODOS={config.MAX_ALLOWED_TODOS}"
        )

    return {
        "files_written": [],
        "items_processed": files_checked,
        "warnings": warnings,
        "errors": errors,
        "completeness": completeness,
    }
