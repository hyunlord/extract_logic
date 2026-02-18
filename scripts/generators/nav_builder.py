"""Build mkdocs.yml from static config and generated markdown frontmatter."""

from __future__ import annotations

import glob
import json
import os
from typing import Any

try:
    import yaml
except ModuleNotFoundError:
    yaml = None  # type: ignore[assignment]

import scripts.config as config


_DEFAULT_NAV_ORDER = 1_000_000


def _to_posix(path: str) -> str:
    return path.replace(os.sep, "/")


def _fallback_title(rel_path: str) -> str:
    stem = os.path.splitext(os.path.basename(rel_path))[0]
    if stem == "_index":
        section = os.path.basename(os.path.dirname(rel_path))
        stem = section or "index"
    return stem.replace("_", " ").replace("-", " ").strip().title()


def _parse_nav_order(value: Any) -> int:
    if isinstance(value, int):
        return value
    if isinstance(value, float) and value.is_integer():
        return int(value)
    if isinstance(value, str):
        try:
            return int(value.strip())
        except ValueError:
            return _DEFAULT_NAV_ORDER
    return _DEFAULT_NAV_ORDER


def _parse_simple_frontmatter(payload: str) -> dict[str, Any]:
    parsed: dict[str, Any] = {}
    for raw_line in payload.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or ":" not in line:
            continue

        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if not key:
            continue

        lowered = value.lower()
        if lowered == "true":
            parsed[key] = True
            continue
        if lowered == "false":
            parsed[key] = False
            continue

        try:
            parsed[key] = int(value)
            continue
        except ValueError:
            parsed[key] = value.strip("'\"")

    return parsed


def _yaml_scalar(value: Any) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    if value is None:
        return "null"
    if isinstance(value, (int, float)):
        return str(value)
    return json.dumps(str(value), ensure_ascii=False)


def _render_yaml_lines(value: Any, indent: int = 0) -> list[str]:
    spacer = " " * indent

    if isinstance(value, dict):
        if not value:
            return [f"{spacer}{{}}"]

        lines: list[str] = []
        for key, item in value.items():
            key_str = str(key)
            if isinstance(item, (dict, list)):
                lines.append(f"{spacer}{key_str}:")
                lines.extend(_render_yaml_lines(item, indent + 2))
            else:
                lines.append(f"{spacer}{key_str}: {_yaml_scalar(item)}")
        return lines

    if isinstance(value, list):
        if not value:
            return [f"{spacer}[]"]

        lines = []
        for item in value:
            if isinstance(item, dict):
                if not item:
                    lines.append(f"{spacer}- {{}}")
                    continue

                entries = list(item.items())
                first_key, first_value = entries[0]
                first_key_str = str(first_key)
                if isinstance(first_value, (dict, list)):
                    lines.append(f"{spacer}- {first_key_str}:")
                    lines.extend(_render_yaml_lines(first_value, indent + 4))
                else:
                    lines.append(
                        f"{spacer}- {first_key_str}: {_yaml_scalar(first_value)}"
                    )

                for next_key, next_value in entries[1:]:
                    next_key_str = str(next_key)
                    next_prefix = " " * (indent + 2)
                    if isinstance(next_value, (dict, list)):
                        lines.append(f"{next_prefix}{next_key_str}:")
                        lines.extend(_render_yaml_lines(next_value, indent + 4))
                    else:
                        lines.append(
                            f"{next_prefix}{next_key_str}: {_yaml_scalar(next_value)}"
                        )
                continue

            if isinstance(item, list):
                lines.append(f"{spacer}-")
                lines.extend(_render_yaml_lines(item, indent + 2))
                continue

            lines.append(f"{spacer}- {_yaml_scalar(item)}")

        return lines

    return [f"{spacer}{_yaml_scalar(value)}"]


def _dump_yaml(data: dict[str, Any], path: str) -> None:
    with open(path, "w", encoding="utf-8") as handle:
        if yaml is not None:
            yaml.dump(
                data,
                handle,
                default_flow_style=False,
                allow_unicode=True,
                sort_keys=False,
            )
            return

        rendered = "\n".join(_render_yaml_lines(data))
        handle.write(rendered)
        handle.write("\n")


def _read_frontmatter(path: str, rel_path: str, warnings: list[str]) -> dict[str, Any]:
    try:
        with open(path, "r", encoding="utf-8") as handle:
            lines = handle.read().splitlines()
    except OSError as exc:
        warnings.append(f"failed to read {rel_path}: {exc}")
        return {}

    if not lines or lines[0].strip() != "---":
        warnings.append(f"missing frontmatter: {rel_path}")
        return {}

    end_index = -1
    for index, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            end_index = index
            break

    if end_index == -1:
        warnings.append(f"unclosed frontmatter: {rel_path}")
        return {}

    payload = "\n".join(lines[1:end_index])
    if not payload.strip():
        return {}

    if yaml is not None:
        try:
            data = yaml.safe_load(payload) or {}
        except yaml.YAMLError as exc:
            warnings.append(f"invalid frontmatter in {rel_path}: {exc}")
            return {}
    else:
        data = _parse_simple_frontmatter(payload)

    if not isinstance(data, dict):
        warnings.append(f"frontmatter must be a mapping in {rel_path}")
        return {}

    return data


def _build_directory_nav(section_path: str, warnings: list[str]) -> list[dict[str, str]]:
    absolute_dir = os.path.join(config.CONTENT_DIR, section_path)
    if not os.path.isdir(absolute_dir):
        warnings.append(f"section directory missing: {section_path}")
        return []

    markdown_files = sorted(
        glob.glob(os.path.join(absolute_dir, "**", "*.md"), recursive=True)
    )
    pages: list[dict[str, Any]] = []

    for file_path in markdown_files:
        rel_path = _to_posix(os.path.relpath(file_path, config.CONTENT_DIR))
        frontmatter = _read_frontmatter(file_path, rel_path, warnings)

        title_value = frontmatter.get("title")
        title = str(title_value).strip() if isinstance(title_value, str) else ""
        if not title:
            title = _fallback_title(rel_path)

        nav_order = _parse_nav_order(frontmatter.get("nav_order"))
        is_index = os.path.basename(file_path) == "_index.md"
        if is_index:
            nav_order = 0

        pages.append(
            {
                "title": title,
                "path": rel_path,
                "nav_order": nav_order,
                "is_index": is_index,
            }
        )

    pages.sort(
        key=lambda page: (
            0 if page["is_index"] else 1,
            int(page["nav_order"]),
            str(page["path"]).lower(),
        )
    )

    return [{str(page["title"]): str(page["path"])} for page in pages]


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
    _ = manifest

    warnings: list[str] = []
    errors: list[str] = []
    files_written: list[str] = []

    nav: list[dict[str, Any]] = []
    items_processed = 0

    for section_title, section_target in config.NAV_SECTION_ORDER:
        if section_target.lower().endswith(".md"):
            file_path = os.path.join(config.CONTENT_DIR, section_target)
            if not os.path.exists(file_path):
                warnings.append(f"section file missing: {section_target}")
                continue

            relative_target = _to_posix(section_target)
            nav.append({section_title: relative_target})
            items_processed += 1
            continue

        children = _build_directory_nav(section_target, warnings)
        nav.append({section_title: children})
        items_processed += len(children)

    mkdocs_config = dict(config.MKDOCS_STATIC_CONFIG)
    mkdocs_config["docs_dir"] = "content"
    mkdocs_config["nav"] = nav

    try:
        _dump_yaml(mkdocs_config, config.MKDOCS_YML)
        files_written.append(config.MKDOCS_YML)
    except OSError as exc:
        errors.append(f"failed to write {config.MKDOCS_YML}: {exc}")

    return {
        "files_written": files_written,
        "items_processed": items_processed,
        "warnings": warnings,
        "errors": errors,
    }
