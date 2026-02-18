"""Generate the docs index page at content/index.md."""

from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from typing import Any

import scripts.config as config

_MANUAL_START = "<!-- MANUAL:START -->"
_MANUAL_END = "<!-- MANUAL:END -->"


def _as_int(value: Any, default: int = 0) -> int:
    """Convert values to int safely; return default when conversion fails."""
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def _format_number(value: int) -> str:
    """Render integer with comma separators."""
    return f"{value:,}"


def _load_json(path: str, warnings: list[str]) -> dict[str, Any]:
    """Load JSON file if present; warn and return empty dict on failure."""
    if not os.path.exists(path):
        warnings.append(f"Missing extracted file, skipped: {path}")
        return {}

    try:
        with open(path, "r", encoding="utf-8") as handle:
            data = json.load(handle)
    except (OSError, json.JSONDecodeError) as exc:
        warnings.append(f"Failed to read extracted file {path}: {exc}")
        return {}

    if not isinstance(data, dict):
        warnings.append(f"Extracted file is not a JSON object: {path}")
        return {}

    return data


def _preserve_manual_block(new_text: str, existing_text: str) -> str:
    """Keep existing MANUAL block content when overwriting a markdown file."""
    old_start = existing_text.find(_MANUAL_START)
    old_end = existing_text.find(_MANUAL_END)
    if old_start == -1 or old_end == -1 or old_start > old_end:
        return new_text

    old_content = existing_text[old_start + len(_MANUAL_START):old_end]
    new_start = new_text.find(_MANUAL_START)
    new_end = new_text.find(_MANUAL_END)

    if new_start == -1 or new_end == -1 or new_start > new_end:
        return f"{new_text.rstrip()}\n\n{_MANUAL_START}{old_content}{_MANUAL_END}\n"

    before = new_text[: new_start + len(_MANUAL_START)]
    after = new_text[new_end:]
    return f"{before}{old_content}{after}"


def run(manifest: dict) -> dict:
    """Main entry point for index page generation.

    Args:
        manifest: The manifest.json data from Phase 1.

    Returns:
        dict with keys:
            - "files_written": list of output file paths
            - "items_processed": int count
            - "warnings": list of warning strings
            - "errors": list of error strings
    """
    warnings: list[str] = []
    errors: list[str] = []

    if not isinstance(manifest, dict):
        warnings.append("Manifest is not a dict; using empty manifest")
        manifest = {}

    manifest_stats = manifest.get("stats")
    if not isinstance(manifest_stats, dict):
        warnings.append("manifest.stats missing or invalid; using fallbacks")
        manifest_stats = {}

    systems_json = _load_json(os.path.join(config.EXTRACTED_DIR, "systems.json"), warnings)
    constants_json = _load_json(os.path.join(config.EXTRACTED_DIR, "constants.json"), warnings)
    locale_json = _load_json(os.path.join(config.EXTRACTED_DIR, "locale.json"), warnings)

    systems_count = _as_int(
        manifest_stats.get("total_system_files"),
        len(manifest.get("systems", [])) + len(manifest.get("ai_modules", [])),
    )
    core_count = _as_int(manifest_stats.get("total_core_files"), len(manifest.get("core_modules", [])))
    ai_count = _as_int(manifest_stats.get("total_ai_files"), len(manifest.get("ai_modules", [])))
    data_count = _as_int(manifest_stats.get("total_json_data_files"), len(manifest.get("data_files", [])))
    locale_files_count = _as_int(
        manifest_stats.get("total_locale_files"),
        len(manifest.get("locale_files", [])),
    )
    locale_key_count = _as_int(
        locale_json.get("stats", {}).get("total_keys"),
        _as_int(manifest_stats.get("total_locale_keys")),
    )
    gdscript_lines = _as_int(
        manifest_stats.get("total_lines_gd"),
        _as_int(systems_json.get("stats", {}).get("total_lines")),
    )

    source_commit = manifest.get("source_commit")
    if not isinstance(source_commit, str) or not source_commit:
        source_commit = "unknown"

    generated_date = None
    generated_at = manifest.get("generated_at")
    if isinstance(generated_at, str) and generated_at:
        try:
            normalized = generated_at.replace("Z", "+00:00")
            generated_date = datetime.fromisoformat(normalized).date().isoformat()
        except ValueError:
            warnings.append("manifest.generated_at has invalid timestamp; using current date")

    if not generated_date:
        generated_date = datetime.now(timezone.utc).date().isoformat()

    index_md = (
        "---\n"
        "title: \"WorldSim Documentation\"\n"
        "description: \"Complete system reference for the WorldSim civilization simulation\"\n"
        "generated: true\n"
        "source_files:\n"
        "  - extracted/manifest.json\n"
        "  - extracted/systems.json\n"
        "  - extracted/constants.json\n"
        "  - extracted/locale.json\n"
        "nav_order: 0\n"
        "---\n\n"
        "# WorldSim Documentation\n\n"
        "자동 생성된 WorldSim 게임 시뮬레이션 시스템 문서입니다.\n\n"
        "## 프로젝트 통계\n\n"
        "| 항목 | 수량 |\n"
        "|------|------|\n"
        f"| 시스템 (Systems) | {_format_number(systems_count)} |\n"
        f"| 코어 모듈 (Core) | {_format_number(core_count)} |\n"
        f"| AI 모듈 | {_format_number(ai_count)} |\n"
        f"| 데이터 파일 (Data) | {_format_number(data_count)} |\n"
        f"| 로케일 파일 (Locale) | {_format_number(locale_files_count)} |\n"
        f"| 로케일 키 (Keys) | {_format_number(locale_key_count)} |\n"
        f"| GDScript 라인 | {_format_number(gdscript_lines)} |\n\n"
        f"> 📅 Generated: {generated_date} | Source commit: `{source_commit}`\n\n"
        "## 주요 섹션\n\n"
        "- **[시스템](systems/)** — 시뮬레이션 시스템 문서 (우선순위 순)\n"
        "- **[설정 레퍼런스](config-reference.md)** — GameConfig 전체 상수\n"
        "- **[데이터](data/)** — JSON 데이터 파일 분석\n"
        "- **[시스템 상호작용](interactions/)** — 시스템 간 의존성 및 상호작용\n"
        "- **[용어 사전](glossary/)** — 한영 대조 게임 용어\n"
        "- **[코어](core/)** — 코어 모듈 레퍼런스\n\n"
        "## 시뮬레이션 아키텍처\n\n"
        "```mermaid\n"
        "graph TD\n"
        "  subgraph \"Core\"\n"
        "    EM[EntityManager] --> ED[EntityData]\n"
        "    SE[SimulationEngine] --> EM\n"
        "  end\n"
        "  subgraph \"Systems\"\n"
        "    NS[NeedsSystem] --> EM\n"
        "    ES[EmotionSystem] --> EM\n"
        "    MS[MortalitySystem] --> EM\n"
        "  end\n"
        "```\n"
    )

    output_path = os.path.join(config.CONTENT_DIR, "index.md")
    config.ensure_dir(config.CONTENT_DIR)

    try:
        if os.path.exists(output_path):
            with open(output_path, "r", encoding="utf-8") as handle:
                existing = handle.read()
            index_md = _preserve_manual_block(index_md, existing)

        with open(output_path, "w", encoding="utf-8") as handle:
            handle.write(index_md)
    except OSError as exc:
        errors.append(f"Failed to write index page: {exc}")
        return {
            "files_written": [],
            "items_processed": 0,
            "warnings": warnings,
            "errors": errors,
        }

    items_processed = systems_count + core_count + ai_count + data_count + locale_files_count
    if constants_json:
        items_processed += 1

    return {
        "files_written": [output_path],
        "items_processed": items_processed,
        "warnings": warnings,
        "errors": errors,
    }
