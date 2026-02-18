"""Generate interpreted Markdown pages for extracted JSON data files."""

from __future__ import annotations

import json
import os
import re
from collections import defaultdict
from typing import Any

import scripts.config as config


MANUAL_BLOCK_RE = re.compile(r"<!-- MANUAL:START -->.*?<!-- MANUAL:END -->", re.DOTALL)
MAX_GENERIC_ROWS = 220

SEMANTIC_GROUP_ORDER = [
    "Timing & Decay",
    "Thresholds & Bounds",
    "Weights & Multipliers",
    "Probabilities",
    "Stress & Emotion",
    "Identifiers & Labels",
    "Other Parameters",
]


def _group_display(group: str) -> str:
    mapping = {
        "Timing & Decay": "Timing & Decay (시간/감쇠)",
        "Thresholds & Bounds": "Thresholds & Bounds (임계/경계)",
        "Weights & Multipliers": "Weights & Multipliers (가중/배수)",
        "Probabilities": "Probabilities (확률)",
        "Stress & Emotion": "Stress & Emotion (스트레스/감정)",
        "Identifiers & Labels": "Identifiers & Labels (식별자/라벨)",
        "Other Parameters": "Other Parameters (기타)",
    }
    return mapping.get(group, group)


def _json_type(value: Any) -> str:
    if isinstance(value, bool):
        return "boolean"
    if isinstance(value, dict):
        return "object"
    if isinstance(value, list):
        return "array"
    if isinstance(value, str):
        return "string"
    if isinstance(value, int):
        return "int"
    if isinstance(value, float):
        return "float"
    if value is None:
        return "null"
    return type(value).__name__


def _escape_pipes(text: str) -> str:
    return text.replace("|", r"\|")


def _sanitize_inline(value: str) -> str:
    return value.replace("\n", " ").strip()


def _to_posix(path: str) -> str:
    return path.replace(os.sep, "/")


def _slug_from_path(file_path: str) -> str:
    return os.path.splitext(os.path.basename(file_path))[0]


def _quote_yaml(text: str) -> str:
    return text.replace("\\", "\\\\").replace('"', r'\"')


def _load_json(path: str) -> Any:
    with open(path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def _entry_content(entry: dict[str, Any]) -> Any:
    """Return the best-effort content payload for a discovered data file entry."""
    for key in ("full_content", "content", "parsed", "data"):
        if key in entry:
            return entry.get(key)
    return None


def _is_meta_key(key: str) -> bool:
    return key.startswith("_comment") or key.startswith("_")


def _is_comment_separator_entry(value: Any) -> bool:
    return isinstance(value, dict) and "_comment" in value and "id" not in value


def _filter_meta_content(value: Any) -> Any:
    if isinstance(value, dict):
        filtered: dict[str, Any] = {}
        for key, item in value.items():
            if _is_meta_key(key):
                continue
            filtered[key] = _filter_meta_content(item)
        return filtered

    if isinstance(value, list):
        filtered_items: list[Any] = []
        for item in value:
            if _is_comment_separator_entry(item):
                continue
            filtered_items.append(_filter_meta_content(item))
        return filtered_items

    return value


def _format_number(value: float) -> str:
    if value.is_integer():
        return str(int(value))
    return f"{value:.4f}".rstrip("0").rstrip(".")


def _infer_unit(parameter: str, value: Any) -> str:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return ""

    key = parameter.lower()
    if "hour" in key or key.endswith("_h"):
        return "hours"
    if "day" in key or key.endswith("_d"):
        return "days"
    if "prob" in key or "chance" in key:
        return "probability"
    if "half_life" in key:
        return "hours"
    if "rate" in key:
        return "rate"
    if "threshold" in key or key.endswith("_min") or key.endswith("_max"):
        return "threshold"
    if "weight" in key or "mult" in key or "coeff" in key or "factor" in key or "ratio" in key:
        return "multiplier"
    return ""


def _format_value(value: Any, parameter: str = "") -> str:
    if isinstance(value, str):
        return value
    if isinstance(value, bool):
        return "true" if value else "false"
    if value is None:
        return "null"
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        number_text = _format_number(float(value))
        unit = _infer_unit(parameter, value)
        if unit:
            return f"{number_text} {unit}"
        return number_text
    if isinstance(value, list):
        return f"{len(value)} items"
    if isinstance(value, dict):
        return f"{len(value)} keys"
    return str(value)


def _semantic_group(parameter: str) -> str:
    key = parameter.lower()

    if any(token in key for token in ("half_life", "decay", "duration", "time", "tick", "tau", "season")):
        return "Timing & Decay"
    if any(token in key for token in ("threshold", "min", "max", "limit", "bound", "clamp")):
        return "Thresholds & Bounds"
    if any(token in key for token in ("weight", "mult", "coeff", "factor", "ratio", "scale", "kappa", "gamma", "beta")):
        return "Weights & Multipliers"
    if any(token in key for token in ("chance", "prob", "likelihood")):
        return "Probabilities"
    if any(token in key for token in ("stress", "emotion", "fear", "joy", "anger", "sadness", "trust", "disgust")):
        return "Stress & Emotion"
    if any(token in key for token in ("id", "name", "label", "title", "type", "category")):
        return "Identifiers & Labels"
    return "Other Parameters"


def _infer_control_description(parameter: str) -> str:
    key = parameter.lower()

    # Mental break domain keys
    if "duration_base" in key:
        return "기본 지속 시간 (틱) — mental break 지속 틱 수 기준값. Base duration in ticks for this mental break type."
    if "duration_variance" in key:
        return "지속 시간 분산 (틱) — 기준값에 더해지는 무작위 분산 범위. Random variance range added to base duration."
    if "break_scale" in key:
        return "발동 확률 분모 — p = (stress - threshold) / break_scale. Higher = rarer breaks. 확률 계산 분모."
    if "break_cap" in key or "cap_per_tick" in key:
        return "틱당 최대 발동 확률 상한. Maximum mental break probability per simulation tick."
    if "shaken_work_penalty" in key:
        return "흔들린 상태 작업 효율 패널티. Work efficiency penalty applied during the shaken aftermath state."
    if "shaken_duration" in key:
        return "흔들린 상태 지속 시간 (틱). Duration of shaken aftermath state in simulation ticks."
    if "catharsis" in key:
        return "카타르시스 회복 비율 — mental break 종료 후 스트레스 회복 계수. Stress recovery factor on break resolution."
    if "weight" in key and (
        "break" in key
        or any(
            bt in key
            for bt in (
                "panic",
                "rage",
                "grief",
                "fugue",
                "outrage",
                "paranoia",
                "purge",
                "ritual",
                "bonding",
                "shutdown",
            )
        )
    ):
        return "이 유형의 mental break 선택 가중치. Selection weight for this break type during break selection."
    if "contagion" in key:
        return "감정 전파 계수 (κ) — 주변 엔티티로의 감정 전파 강도. Emotional contagion coefficient to nearby entities."
    if "duration" in key and "ticks" in key:
        return "지속 시간 (틱). Duration in simulation ticks."

    if "siler" in key:
        return "Siler mortality hazard component. (Siler 사망 위험도 구성요소)"
    if "care_protection" in key:
        return "Infant protection modifier applied when caregivers can respond. (영아 보호 보정값)"
    if "tech_modifiers" in key:
        return "Technology-driven reduction of mortality pressure. (기술 수준에 따른 사망률 감소)"
    if "season_modifiers" in key:
        return "Seasonal environmental multiplier applied to mortality risk. (계절 환경 배수)"
    if any(token in key for token in ("half_life", "decay", "tau")):
        return "How quickly this state fades over simulation time. (시간 경과 감소 속도)"
    if any(token in key for token in ("threshold", "min", "max", "limit", "bound")):
        return "Activation boundary used by game logic. (작동 임계값)"
    if any(token in key for token in ("weight", "mult", "coeff", "factor", "ratio", "scale", "kappa", "gamma", "beta")):
        return "Strength multiplier used in gameplay calculations. (계산 강도 배수)"
    if any(token in key for token in ("chance", "prob", "likelihood")):
        return "Probability that this branch triggers during evaluation. (발생 확률)"
    if any(token in key for token in ("stress", "emotion", "fear", "joy", "anger", "sadness", "trust", "disgust")):
        return "Stress/emotion contribution in simulation updates. (스트레스/감정 기여도)"
    if any(token in key for token in ("id", "name", "label", "title", "type", "category")):
        return "Identifier/label used for lookup or UI presentation. (식별자/라벨)"
    return "General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값)"


def _flatten_parameters(value: Any, prefix: str = "", rows: list[tuple[str, Any]] | None = None) -> list[tuple[str, Any]]:
    if rows is None:
        rows = []

    if len(rows) >= MAX_GENERIC_ROWS:
        return rows

    if isinstance(value, dict):
        for key in sorted(value.keys()):
            child = value[key]
            path = f"{prefix}.{key}" if prefix else str(key)
            if isinstance(child, dict):
                _flatten_parameters(child, path, rows)
                if len(rows) >= MAX_GENERIC_ROWS:
                    break
                continue
            if isinstance(child, list):
                rows.append((path, child))
                if child and isinstance(child[0], dict):
                    _flatten_parameters(child[0], f"{path}.item", rows)
                elif child:
                    rows.append((f"{path}.sample", child[0]))
                if len(rows) >= MAX_GENERIC_ROWS:
                    break
                continue
            rows.append((path, child))
            if len(rows) >= MAX_GENERIC_ROWS:
                break
        return rows

    if isinstance(value, list):
        rows.append((prefix or "items", value))
        if value:
            first = value[0]
            if isinstance(first, dict):
                _flatten_parameters(first, f"{prefix}.item" if prefix else "item", rows)
            else:
                rows.append((f"{prefix}.sample" if prefix else "sample", first))
        return rows

    if prefix:
        rows.append((prefix, value))
    return rows


def _render_parameter_table(rows: list[tuple[str, str, str, str]]) -> str:
    lines = [
        "| Parameter (매개변수) | Value (값) | Type (유형) | What it controls (게임 영향) |",
        "|----------------------|-----------|------------|-----------------------------|",
    ]

    for parameter, value, type_name, controls in rows:
        safe_parameter = _escape_pipes(_sanitize_inline(parameter))
        safe_value = _escape_pipes(_sanitize_inline(value))
        safe_type = _escape_pipes(_sanitize_inline(type_name))
        safe_controls = _escape_pipes(_sanitize_inline(controls))
        lines.append(
            f"| `{safe_parameter}` | {safe_value} | {safe_type} | {safe_controls} |"
        )

    return "\n".join(lines)


def _render_metric_table(rows: list[tuple[str, str]]) -> str:
    lines = [
        "| Metric (지표) | Value (값) |",
        "|---------------|-----------|",
    ]

    for metric, value in rows:
        safe_metric = _escape_pipes(_sanitize_inline(metric))
        safe_value = _escape_pipes(_sanitize_inline(value))
        lines.append(f"| {safe_metric} | {safe_value} |")

    return "\n".join(lines)


def _module_slug(section: str, module_file: str, module_entry: dict[str, Any]) -> str:
    if section in {"systems", "ai_modules"}:
        system_name = module_entry.get("system_name")
        if isinstance(system_name, str) and system_name:
            return system_name
        stem = _slug_from_path(module_file)
        return stem[:-7] if stem.endswith("_system") else stem
    return _slug_from_path(module_file)


def _build_module_meta(manifest: dict) -> dict[str, dict[str, str]]:
    meta: dict[str, dict[str, str]] = {}
    sections = (
        ("systems", config.CONTENT_SYSTEMS),
        ("ai_modules", config.CONTENT_SYSTEMS),
        ("core_modules", config.CONTENT_CORE),
    )

    for section, content_dir in sections:
        entries = manifest.get(section, [])
        if not isinstance(entries, list):
            continue

        for module_entry in entries:
            if not isinstance(module_entry, dict):
                continue

            file_path = module_entry.get("file")
            if not isinstance(file_path, str) or not file_path.endswith(".gd"):
                continue

            slug = _module_slug(section, file_path, module_entry)
            title = (
                module_entry.get("system_name")
                if section in {"systems", "ai_modules"}
                else _slug_from_path(file_path)
            )
            if not isinstance(title, str) or not title:
                title = _slug_from_path(file_path)

            meta[file_path] = {
                "title": title,
                "doc_path": os.path.join(content_dir, f"{slug}.md"),
            }

    return meta


def _dependency_matches_file(dependency: str, data_file: str) -> bool:
    dep = dependency.replace("\\", "/").rstrip("/")
    target = data_file.replace("\\", "/")

    if dep == target:
        return True

    return target.startswith(dep + "/")


def _build_referenced_by_map(
    data_entries: list[dict[str, Any]],
    manifest: dict,
    warnings: list[str],
) -> dict[str, list[dict[str, str]]]:
    references_path = os.path.join(config.EXTRACTED_DIR, "references.json")
    if not os.path.exists(references_path):
        warnings.append("references.json not found; Referenced By sections omitted")
        return {}

    try:
        references = _load_json(references_path)
    except (OSError, json.JSONDecodeError) as exc:
        warnings.append(f"failed to load references.json: {exc}")
        return {}

    dependency_graph = references.get("dependency_graph")
    if not isinstance(dependency_graph, dict):
        warnings.append("references.json missing dependency_graph; Referenced By sections omitted")
        return {}

    module_meta = _build_module_meta(manifest)
    referenced_by: dict[str, list[dict[str, str]]] = defaultdict(list)

    data_files: list[str] = []
    for entry in data_entries:
        file_path = entry.get("file")
        if isinstance(file_path, str) and file_path:
            data_files.append(file_path)

    for module_file, module_data in sorted(dependency_graph.items()):
        if not isinstance(module_data, dict):
            continue

        depends_on = module_data.get("depends_on")
        if not isinstance(depends_on, list):
            continue

        module_info = module_meta.get(module_file)
        if not module_info:
            continue

        for dep in depends_on:
            if not isinstance(dep, str) or not dep.startswith("data/"):
                continue

            for data_file in data_files:
                if not _dependency_matches_file(dep, data_file):
                    continue

                reason = f"references `{dep}`" if data_file == dep else f"references data under `{dep.rstrip('/')}/`"
                referenced_by[data_file].append(
                    {
                        "module_title": module_info["title"],
                        "module_doc_path": module_info["doc_path"],
                        "reason": reason,
                    }
                )

    for file_path, refs in referenced_by.items():
        deduped: dict[tuple[str, str], dict[str, str]] = {}
        for ref in refs:
            key = (ref["module_title"], ref["module_doc_path"])
            deduped[key] = ref
        referenced_by[file_path] = [deduped[key] for key in sorted(deduped.keys())]

    return referenced_by


def _preserve_manual_blocks(path: str, new_text: str) -> str:
    if not os.path.exists(path):
        return new_text

    try:
        with open(path, "r", encoding="utf-8") as handle:
            previous_text = handle.read()
    except OSError:
        return new_text

    old_blocks = MANUAL_BLOCK_RE.findall(previous_text)
    if not old_blocks:
        return new_text

    if not MANUAL_BLOCK_RE.search(new_text):
        return new_text

    index = 0

    def _replace_block(match: re.Match[str]) -> str:
        nonlocal index
        if index >= len(old_blocks):
            return match.group(0)
        block = old_blocks[index]
        index += 1
        return block

    return MANUAL_BLOCK_RE.sub(_replace_block, new_text)


def _write_markdown(path: str, content: str, files_written: list[str], errors: list[str]) -> None:
    try:
        with open(path, "w", encoding="utf-8") as handle:
            handle.write(content)
        files_written.append(path)
    except OSError as exc:
        errors.append(f"failed to write {path}: {exc}")


def _derive_domain_from_file(file_path: str) -> str:
    normalized = file_path.replace("\\", "/")
    if normalized.startswith("data/species/"):
        return "species"
    if "/emotions/" in normalized or normalized.startswith("data/emotions/"):
        return "emotions"
    if "/personality/" in normalized or normalized.startswith("data/personality/"):
        return "personality"
    if normalized.endswith("stressor_events.json"):
        return "stress"

    parts = normalized.split("/")
    if len(parts) >= 2 and parts[0] == "data":
        return parts[1]
    return "unknown"


def _domain_group(entry: dict[str, Any]) -> str:
    file_path = entry.get("file", "")
    if not isinstance(file_path, str):
        return "unknown"

    domain = entry.get("domain")
    if not isinstance(domain, str) or not domain:
        domain = _derive_domain_from_file(file_path)

    normalized = domain.lower()
    if normalized in {"species", "emotions", "personality", "stress"}:
        return normalized
    if normalized == "mortality":
        return "species"
    return normalized


def _domain_display(group: str) -> str:
    mapping = {
        "species": "Species (종족)",
        "emotions": "Emotions (감정)",
        "personality": "Personality (성격)",
        "stress": "Stress (스트레스)",
        "unknown": "Unknown (미상)",
    }
    return mapping.get(group, group.replace("_", " ").title())


def _load_optional_payload(extracted: dict[str, Any], key: str, warnings: list[str]) -> dict[str, Any] | None:
    value = extracted.get(key)
    if isinstance(value, dict):
        return value

    fallback_file = {
        "trait_data": "trait_data.json",
        "emotion_presets": "emotion_presets.json",
        "decay_config": "decay_config.json",
        "stressor_data": "stressor_data.json",
    }.get(key)
    if not fallback_file:
        return None

    path = os.path.join(config.EXTRACTED_DIR, fallback_file)
    if not os.path.exists(path):
        return None

    try:
        loaded = _load_json(path)
    except (OSError, json.JSONDecodeError) as exc:
        warnings.append(f"failed to load {fallback_file}: {exc}")
        return None

    if not isinstance(loaded, dict):
        warnings.append(f"{fallback_file} is not an object; ignoring")
        return None
    return loaded


def _resolve_data_entries(
    extracted: dict[str, Any],
    warnings: list[str],
    errors: list[str],
) -> list[dict[str, Any]]:
    in_memory = extracted.get("data_files")
    if isinstance(in_memory, dict):
        files = in_memory.get("files")
        if isinstance(files, list):
            return [item for item in files if isinstance(item, dict)]
    elif isinstance(in_memory, list):
        return [item for item in in_memory if isinstance(item, dict)]

    extracted_path = os.path.join(config.EXTRACTED_DIR, "data_files.json")
    if not os.path.exists(extracted_path):
        warnings.append("extracted/data_files.json not found")
        return []

    try:
        loaded = _load_json(extracted_path)
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"failed to load extracted/data_files.json: {exc}")
        return []

    files = loaded.get("files") if isinstance(loaded, dict) else None
    if not isinstance(files, list):
        warnings.append("extracted/data_files.json has non-list 'files' field")
        return []

    return [item for item in files if isinstance(item, dict)]


def _known_system_docs(file_stem: str) -> list[tuple[str, str]]:
    mapping: dict[str, list[tuple[str, str]]] = {
        "siler_parameters": [("mortality", os.path.join(config.CONTENT_SYSTEMS, "mortality.md"))],
        "trait_definitions": [("trait", os.path.join(config.CONTENT_SYSTEMS, "trait.md"))],
        "decay_parameters": [("emotions", os.path.join(config.CONTENT_SYSTEMS, "emotions.md"))],
        "event_presets": [("emotions", os.path.join(config.CONTENT_SYSTEMS, "emotions.md"))],
        "stressor_events": [("stress", os.path.join(config.CONTENT_SYSTEMS, "stress.md"))],
    }
    return mapping.get(file_stem, [])


def _overview_summary(file_stem: str, category: str) -> str:
    mapping = {
        "siler_parameters": "종족 사망률 위험도와 생존 보정값. Species mortality hazards and survival modifiers.",
        "trait_definitions": "성격 특성의 발동 규칙과 효과 메타데이터. Trait activation rules and effect metadata.",
        "decay_parameters": "감정 감쇠/전염/기준치/정신 붕괴 튜닝. Emotion decay, contagion, baselines, mental-break tuning.",
        "event_presets": "세계 이벤트를 감정 자극으로 변환하는 평가 프리셋. Event appraisal presets for emotion impulses.",
        "stressor_events": "스트레스 이벤트 템플릿과 심각도/맥락 보정. Stress event templates and severity/context modifiers.",
    }
    if file_stem in mapping:
        return mapping[file_stem]
    return f"`{category}` 데이터 도메인 설정 값. Configuration values for the `{category}` data domain."


def _relative_link(output_dir: str, target_path: str) -> str:
    return _to_posix(os.path.relpath(target_path, output_dir))


def _render_overview_section(
    *,
    entry: dict[str, Any],
    referenced_by: list[dict[str, str]],
    output_dir: str,
) -> list[str]:
    source_file = entry["file"]
    category = entry["category"]
    file_stem = _slug_from_path(source_file)

    lines = [
        "## 개요 (Overview)",
        "",
        f"- Configures (설정 내용): {_overview_summary(file_stem, category)}",
    ]

    if referenced_by:
        reader_names = ", ".join(sorted({ref["module_title"] for ref in referenced_by}))
        lines.append(f"- Read by systems/modules (읽는 시스템/모듈): {reader_names}")
    else:
        lines.append("- Read by systems/modules (읽는 시스템/모듈): `references.json`에서 추론되지 않음.")

    doc_links: list[str] = []
    for title, doc_path in _known_system_docs(file_stem):
        doc_links.append(f"[`{title}`]({_relative_link(output_dir, doc_path)})")

    if not doc_links and referenced_by:
        for ref in referenced_by[:3]:
            doc_links.append(
                f"[`{ref['module_title']}`]({_relative_link(output_dir, ref['module_doc_path'])})"
            )

    if doc_links:
        lines.append(f"- Related documentation (관련 문서): {', '.join(doc_links)}")
    else:
        lines.append("- Related documentation (관련 문서): 없음.")

    return lines + [""]


def _academic_references(file_stem: str) -> list[str]:
    mapping = {
        "siler_parameters": ["Siler (1979) Competing-Risk Model"],
        "decay_parameters": ["Verduyn & Brans (2012)", "Plutchik (1980)"],
        "event_presets": ["Plutchik (1980)", "Lazarus (1991)", "Scherer (2009)"],
        "stressor_events": ["Holmes & Rahe (1967)", "Hobfoll (1989) COR"],
    }
    return mapping.get(file_stem, [])


def _render_siler_parameters(content: dict[str, Any]) -> list[str]:
    baseline = content.get("baseline") if isinstance(content.get("baseline"), dict) else {}
    tech_modifiers = content.get("tech_modifiers") if isinstance(content.get("tech_modifiers"), dict) else {}
    care_protection = content.get("care_protection") if isinstance(content.get("care_protection"), dict) else {}
    season_modifiers = content.get("season_modifiers") if isinstance(content.get("season_modifiers"), dict) else {}

    baseline_help = {
        "a1": "Infant mortality amplitude in the Siler hazard term. (영아 사망 위험도 진폭)",
        "b1": "Rate at which infant mortality hazard declines with age. (연령에 따른 영아 위험도 감소율)",
        "a2": "Age-independent background mortality floor. (연령 무관 기본 사망률)",
        "a3": "Late-life mortality growth amplitude. (노년기 위험도 진폭)",
        "b3": "Exponential growth rate of senescent mortality. (노년기 위험도 증가율)",
    }

    tech_help = {
        "k1": "Tech-driven reduction for infant hazard; lower hazard ⇒ higher survival. (기술로 영아 위험도 감소 → 생존율 증가)",
        "k2": "Tech-driven reduction for background hazard; lower hazard ⇒ higher survival. (기술로 기본 위험도 감소 → 생존율 증가)",
        "k3": "Tech-driven reduction for senescent hazard; lower hazard ⇒ higher survival. (기술로 노년 위험도 감소 → 생존율 증가)",
    }

    care_help = {
        "hunger_min": "Minimum hunger condition where infant care protection remains active. (보호 유지 최소 배고픔)",
        "protection_factor": "Fraction of infant mortality risk reduced by effective care. (보호로 줄어드는 위험 비율)",
    }

    lines = [
        "## 사망 모델 해석 (Mortality Model Interpretation)",
        "",
        "This file defines parameters for the Siler competing-risk hazard model used by the mortality system. (사망 시스템이 사용하는 Siler 경쟁위험도 모델 파라미터)",
        "",
        "Siler hazard (Siler 사망 위험도):",
        "",
        "$$\\mu(x) = a_1 e^{-b_1 x} + a_2 + a_3 e^{b_3 x}$$",
        "",
        "- `a1,b1`: infant/early-life hazard that decays with age. (영아/초기 위험도, 연령 증가로 감소)",
        "- `a2`: background hazard floor. (연령 무관 기본 위험도)",
        "- `a3,b3`: senescent hazard that grows with age. (노년기 위험도, 연령 증가로 증가)",
        "",
        "### 기본 파라미터 (Baseline Parameters)",
        "",
    ]

    baseline_rows: list[tuple[str, str, str, str]] = []
    for key in sorted(baseline.keys()):
        value = baseline[key]
        baseline_rows.append(
            (
                key,
                _format_value(value, key),
                _json_type(value),
                baseline_help.get(key, _infer_control_description(key)),
            )
        )

    if baseline_rows:
        lines.extend([_render_parameter_table(baseline_rows), ""])
    else:
        lines.extend(["- No baseline parameters found. (기본 파라미터 없음)", ""])

    lines.extend(["### 기술 보정 (Technology Modifiers)", ""])
    tech_rows: list[tuple[str, str, str, str]] = []
    for key in sorted(tech_modifiers.keys()):
        value = tech_modifiers[key]
        tech_rows.append((f"tech_modifiers.{key}", _format_value(value, key), _json_type(value), tech_help.get(key, _infer_control_description(f"tech_modifiers.{key}"))))

    if tech_rows:
        lines.extend([
            "Higher technology typically reduces mortality via these coefficients; lower hazard ⇒ higher survival. (기술 수준이 높을수록 위험도↓ → 생존율↑)",
            "",
            _render_parameter_table(tech_rows),
            "",
        ])
    else:
        lines.extend(["- No technology modifiers found. (기술 보정 없음)", ""])

    lines.extend(["### 영아 보호 (Infant Care Protection)", ""])
    care_rows: list[tuple[str, str, str, str]] = []
    for key in sorted(care_protection.keys()):
        value = care_protection[key]
        care_rows.append((f"care_protection.{key}", _format_value(value, key), _json_type(value), care_help.get(key, _infer_control_description(f"care_protection.{key}"))))

    if care_rows:
        lines.extend([
            "These parameters model caregiver buffering for infant survival during vulnerable periods. (보호자 돌봄에 따른 생존 완충)",
            "",
            _render_parameter_table(care_rows),
            "",
        ])
    else:
        lines.extend(["- No care_protection section found. (care_protection 없음)", ""])

    lines.extend(["### 계절 환경 영향 (Seasonal Environment Effects)", ""])
    season_rows: list[tuple[str, str, str, str]] = []
    for season, payload in sorted(season_modifiers.items()):
        if not isinstance(payload, dict):
            season_rows.append((f"season_modifiers.{season}", _format_value(payload, season), _json_type(payload), _infer_control_description(f"season_modifiers.{season}")))
            continue
        for channel, value in sorted(payload.items()):
            parameter = f"season_modifiers.{season}.{channel}"
            if channel == "infant":
                control = f"Seasonal multiplier for infant mortality during {season}. ({season} 영아 사망률 계절 배수)"
            elif channel == "background":
                control = f"Seasonal multiplier for background mortality during {season}. ({season} 기본 사망률 계절 배수)"
            else:
                control = _infer_control_description(parameter)
            season_rows.append((parameter, _format_value(value, parameter), _json_type(value), control))

    if season_rows:
        lines.extend([_render_parameter_table(season_rows), ""])
    else:
        lines.extend(["- No season_modifiers found. (계절 보정 없음)", ""])

    return lines


def _count_trait_entries(content: Any) -> int:
    if isinstance(content, list):
        return sum(1 for item in content if isinstance(item, dict) and item.get("id"))
    if isinstance(content, dict):
        traits = content.get("traits")
        if isinstance(traits, list):
            return sum(1 for item in traits if isinstance(item, dict) and item.get("id"))
    return 0


def _render_personality_defer(
    *,
    content: Any,
    trait_data: dict[str, Any] | None,
    output_dir: str,
) -> list[str]:
    lines = [
        "## 전용 문서 (Specialized Documentation)",
        "",
        "Detailed trait interpretation is generated by `scripts/generators/trait_page.py`. (세부 특성 해석은 별도 생성)",
        "",
    ]

    trait_index_path = os.path.join(config.CONTENT_DIR, "traits", "_index.md")
    lines.append(
        f"- See [`Trait Pages`]({_relative_link(output_dir, trait_index_path)}) for HEXACO conditions and effect breakdowns. (HEXACO 조건/효과 정리)"
    )
    lines.append("")

    total_traits = _count_trait_entries(content)
    axis_count = "-"
    type_breakdown = "-"

    if trait_data:
        stats = trait_data.get("stats") if isinstance(trait_data.get("stats"), dict) else {}
        total_from_extractor = stats.get("total_traits")
        if isinstance(total_from_extractor, int):
            total_traits = total_from_extractor

        by_axis = stats.get("by_axis_count")
        if isinstance(by_axis, dict):
            axis_count = str(len(by_axis))

        by_type_count = stats.get("by_type_count")
        if isinstance(by_type_count, dict) and by_type_count:
            parts = []
            for key in sorted(by_type_count.keys()):
                value = by_type_count[key]
                if isinstance(value, int):
                    parts.append(f"{key}:{value}")
            if parts:
                type_breakdown = ", ".join(parts)

    summary_rows = [
        ("Trait entries (특성 수)", str(total_traits)),
        ("HEXACO axis groups (축 그룹)", axis_count),
        ("Type breakdown (유형 분포)", type_breakdown),
    ]

    lines.extend([
        "### 요약 (Summary)",
        "",
        _render_metric_table(summary_rows),
        "",
    ])

    return lines


def _render_emotion_defer(
    *,
    file_stem: str,
    content: Any,
    output_dir: str,
    emotion_presets: dict[str, Any] | None,
    decay_config: dict[str, Any] | None,
) -> list[str]:
    lines = [
        "## 전용 문서 (Specialized Documentation)",
        "",
        "Detailed emotion-system explanation is generated by `scripts/generators/emotion_detail.py`. (감정 시스템 상세 문서)",
        "",
    ]

    detail_path = os.path.join(config.CONTENT_SYSTEMS, "emotion-detail.md")
    lines.append(
        f"- See [`Emotion Detail`]({_relative_link(output_dir, detail_path)}) for model-level formulas and dynamics. (모델 수식/동역학)"
    )
    lines.append("")

    summary_rows: list[tuple[str, str]] = []

    if file_stem == "decay_parameters":
        stats = decay_config.get("stats") if isinstance(decay_config, dict) and isinstance(decay_config.get("stats"), dict) else {}
        total_parameters = stats.get("total_parameters") if isinstance(stats.get("total_parameters"), int) else "-"
        emotion_count = stats.get("emotion_count") if isinstance(stats.get("emotion_count"), int) else "-"
        mental_break_types = stats.get("mental_break_types") if isinstance(stats.get("mental_break_types"), int) else "-"

        if isinstance(content, dict) and total_parameters == "-":
            total_parameters = len(_flatten_parameters(content))

        summary_rows = [
            ("Total parameters (총 파라미터)", str(total_parameters)),
            ("Emotion channels (감정 채널)", str(emotion_count)),
            ("Mental break behavior types (붕괴 유형)", str(mental_break_types)),
        ]

    if file_stem == "event_presets":
        stats = emotion_presets.get("stats") if isinstance(emotion_presets, dict) and isinstance(emotion_presets.get("stats"), dict) else {}
        total_presets = stats.get("total_presets") if isinstance(stats.get("total_presets"), int) else 0
        by_category_count = stats.get("by_category_count") if isinstance(stats.get("by_category_count"), dict) else {}
        trauma_events = stats.get("trauma_events") if isinstance(stats.get("trauma_events"), int) else "-"

        if isinstance(content, dict):
            events = content.get("events")
            if isinstance(events, dict):
                total_presets = max(total_presets, len(events))
                if not by_category_count:
                    generated: dict[str, int] = {}
                    for payload in events.values():
                        if not isinstance(payload, dict):
                            continue
                        category = payload.get("category")
                        if not isinstance(category, str) or not category:
                            category = "unknown"
                        generated[category] = generated.get(category, 0) + 1
                    by_category_count = generated

        top_categories = ", ".join(
            f"{key}:{value}"
            for key, value in sorted(by_category_count.items())[:6]
            if isinstance(value, int)
        )
        if not top_categories:
            top_categories = "-"

        summary_rows = [
            ("Total event presets (프리셋 수)", str(total_presets)),
            ("Trauma-marked events (트라우마)", str(trauma_events)),
            ("Category counts (카테고리)", top_categories),
        ]

    lines.extend([
        "### 요약 (Summary)",
        "",
        _render_metric_table(summary_rows),
        "",
    ])

    return lines


def _render_stress_defer(
    *,
    output_dir: str,
    stressor_data: dict[str, Any] | None,
    content: Any,
) -> list[str]:
    lines = [
        "## 전용 문서 (Specialized Documentation)",
        "",
        "Detailed stress mechanics are generated by `scripts/generators/stress_detail.py`. (스트레스 상세 문서)",
        "",
    ]

    detail_path = os.path.join(config.CONTENT_SYSTEMS, "stress-detail.md")
    lines.append(
        f"- See [`Stress Detail`]({_relative_link(output_dir, detail_path)}) for pipeline formulas and stage interpretation. (수식/단계 해석)"
    )
    lines.append("")

    stats = stressor_data.get("stats") if isinstance(stressor_data, dict) and isinstance(stressor_data.get("stats"), dict) else {}

    total_events = stats.get("total_events") if isinstance(stats.get("total_events"), int) else 0
    loss_events = stats.get("loss_events") if isinstance(stats.get("loss_events"), int) else "-"
    by_category = stats.get("by_category_count") if isinstance(stats.get("by_category_count"), dict) else {}

    if isinstance(content, dict) and total_events == 0:
        total_events = sum(1 for value in content.values() if isinstance(value, dict))

    category_summary = ", ".join(
        f"{key}:{value}" for key, value in sorted(by_category.items()) if isinstance(value, int)
    )
    if not category_summary:
        category_summary = "-"

    summary_rows = [
        ("Total stressor events (이벤트 수)", str(total_events)),
        ("Loss-coded events (상실 분류)", str(loss_events)),
        ("By category (카테고리)", category_summary),
    ]

    lines.extend([
        "### 요약 (Summary)",
        "",
        _render_metric_table(summary_rows),
        "",
    ])

    return lines


def _render_generic_interpreted(content: Any) -> list[str]:
    lines = [
        "## 해석된 파라미터 (Interpreted Parameters)",
        "",
    ]

    grouped_rows: dict[str, list[tuple[str, str, str, str]]] = defaultdict(list)

    flattened = _flatten_parameters(content)
    for parameter, value in flattened:
        group = _semantic_group(parameter)
        grouped_rows[group].append(
            (
                parameter,
                _format_value(value, parameter),
                _json_type(value),
                _infer_control_description(parameter),
            )
        )

    if not grouped_rows:
        lines.extend(["- No interpretable parameters found. (해석 가능한 파라미터 없음)", ""])
        return lines

    for group in SEMANTIC_GROUP_ORDER:
        rows = grouped_rows.get(group, [])
        if not rows:
            continue
        lines.extend([
            f"### {_group_display(group)}",
            "",
            _render_parameter_table(rows),
            "",
        ])

    for group in sorted(grouped_rows.keys()):
        if group in SEMANTIC_GROUP_ORDER:
            continue
        lines.extend([
            f"### {_group_display(group)}",
            "",
            _render_parameter_table(grouped_rows[group]),
            "",
        ])

    return lines


def _render_domain_content(
    *,
    entry: dict[str, Any],
    output_dir: str,
    trait_data: dict[str, Any] | None,
    emotion_presets: dict[str, Any] | None,
    decay_config: dict[str, Any] | None,
    stressor_data: dict[str, Any] | None,
) -> list[str]:
    source_file = entry["file"]
    file_stem = _slug_from_path(source_file)
    content = entry.get("full_content")

    if file_stem == "siler_parameters" and isinstance(content, dict):
        return _render_siler_parameters(content)

    if file_stem == "trait_definitions":
        return _render_personality_defer(content=content, trait_data=trait_data, output_dir=output_dir)

    if file_stem in {"decay_parameters", "event_presets"}:
        return _render_emotion_defer(
            file_stem=file_stem,
            content=content,
            output_dir=output_dir,
            emotion_presets=emotion_presets,
            decay_config=decay_config,
        )

    if file_stem == "stressor_events":
        return _render_stress_defer(output_dir=output_dir, stressor_data=stressor_data, content=content)

    return _render_generic_interpreted(content)


def _render_page(
    *,
    entry: dict[str, Any],
    referenced_by: list[dict[str, str]],
    output_dir: str,
    trait_data: dict[str, Any] | None,
    emotion_presets: dict[str, Any] | None,
    decay_config: dict[str, Any] | None,
    stressor_data: dict[str, Any] | None,
) -> str:
    source_file = entry["file"]
    category = entry["category"]
    file_stem = _slug_from_path(source_file)
    value_type = entry.get("type", "unknown")

    lines = [
        "---",
        f'title: "{_quote_yaml(file_stem)} Data"',
        f'description: "{_quote_yaml(category)} data file documentation"',
        "generated: true",
        "source_files:",
        f'  - "{_quote_yaml(source_file)}"',
        "nav_order: 10",
        "---",
        "",
        f"# {file_stem}",
        "",
        f"📄 source (출처): `{source_file}` | Category (분류): {category} | Type (유형): {value_type}",
        "",
    ]

    lines.extend(_render_overview_section(entry=entry, referenced_by=referenced_by, output_dir=output_dir))
    lines.extend(
        _render_domain_content(
            entry=entry,
            output_dir=output_dir,
            trait_data=trait_data,
            emotion_presets=emotion_presets,
            decay_config=decay_config,
            stressor_data=stressor_data,
        )
    )

    academic_refs = _academic_references(file_stem)
    if academic_refs:
        lines.extend(
            [
                "## 참고 문헌 (Academic References)",
                "",
            ]
        )
        for ref in academic_refs:
            lines.append(f"- {ref}")
        lines.append("")

    lines.append("## 참조하는 시스템 (Referenced By)")
    lines.append("")
    if referenced_by:
        for ref in referenced_by:
            relative_link = _relative_link(output_dir, ref["module_doc_path"])
            lines.append(f"- [`{ref['module_title']}`]({relative_link}) - {ref['reason']}")
    else:
        lines.append("- None found. (참조 없음)")

    lines.extend(
        [
            "",
            "## 수동 노트 (Manual Notes)",
            "",
            "<!-- MANUAL:START -->",
            "<!-- MANUAL:END -->",
            "",
        ]
    )

    return "\n".join(lines)


def _render_index_page(grouped: dict[str, list[dict[str, Any]]], source_files: list[str]) -> str:
    total_files = sum(len(entries) for entries in grouped.values())

    lines = [
        "---",
        'title: "데이터 (Data)"',
        'description: "WorldSim interpreted data file documentation (WorldSim 데이터 해석 문서)"',
        "generated: true",
        "source_files:",
    ]

    for source in source_files:
        lines.append(f'  - "{_quote_yaml(source)}"')

    lines.extend(
        [
            "nav_order: 1",
            "---",
            "",
            "# 데이터 (Data)",
            "",
            f"Total files (총 파일 수): **{total_files}**",
            "",
            "## 도메인 요약 (Domain Summary)",
            "",
            "| Domain (도메인) | Files (파일 수) |",
            "|-----------------|----------------|",
        ]
    )

    for group in sorted(grouped.keys()):
        lines.append(f"| {_domain_display(group)} | {len(grouped[group])} |")

    lines.append("")

    for group in sorted(grouped.keys()):
        entries = sorted(grouped[group], key=lambda item: item["file"])
        lines.extend(
            [
                f"## {_domain_display(group)}",
                "",
                "| File (파일) | Category (분류) | Type (유형) | Key Count (키 수) | Items (항목 수) |",
                "|-------------|----------------|------------|------------------|----------------|",
            ]
        )

        for entry in entries:
            rel_path = _to_posix(entry["index_rel_link"])
            key_count = entry.get("key_count", "-")
            items = entry.get("items_count", "-")
            file_stem = _slug_from_path(entry["file"])
            value_type = entry.get("type", "unknown")
            category = entry.get("category", "unknown")
            lines.append(
                f"| [{file_stem}]({rel_path}) | {category} | {value_type} | {key_count} | {items} |"
            )

        lines.append("")

    lines.extend(
        [
            "## 수동 노트 (Manual Notes)",
            "",
            "<!-- MANUAL:START -->",
            "<!-- MANUAL:END -->",
            "",
        ]
    )

    return "\n".join(lines)


def run(manifest: dict, extracted: dict) -> dict:
    """Main entry point.

    Args:
        manifest: The manifest.json data from Phase 1.
        extracted: In-memory extracted payloads.

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

    if not isinstance(manifest, dict):
        warnings.append("manifest is not an object; using empty manifest")
        manifest = {}

    extracted_payloads = extracted if isinstance(extracted, dict) else {}

    data_entries = _resolve_data_entries(extracted_payloads, warnings, errors)
    if errors:
        return {
            "files_written": files_written,
            "items_processed": 0,
            "warnings": warnings,
            "errors": errors,
        }

    manifest_data_entries = manifest.get("data_files", [])
    if not isinstance(manifest_data_entries, list):
        manifest_data_entries = []

    manifest_meta_by_file: dict[str, dict[str, Any]] = {}
    for entry in manifest_data_entries:
        if not isinstance(entry, dict):
            continue
        file_path = entry.get("file")
        if isinstance(file_path, str) and file_path:
            manifest_meta_by_file[file_path] = entry

    config.ensure_dir(config.CONTENT_DATA)

    referenced_by_map = _build_referenced_by_map(data_entries, manifest, warnings)

    trait_data = _load_optional_payload(extracted_payloads, "trait_data", warnings)
    emotion_presets = _load_optional_payload(extracted_payloads, "emotion_presets", warnings)
    decay_config = _load_optional_payload(extracted_payloads, "decay_config", warnings)
    stressor_data = _load_optional_payload(extracted_payloads, "stressor_data", warnings)

    grouped_for_index: dict[str, list[dict[str, Any]]] = defaultdict(list)
    processed_count = 0

    sorted_entries = sorted(
        (item for item in data_entries if isinstance(item, dict)),
        key=lambda item: (str(item.get("category", "")), str(item.get("file", ""))),
    )

    for entry in sorted_entries:
        source_file = entry.get("file")
        category = entry.get("category")

        if not isinstance(source_file, str) or not source_file:
            warnings.append("skipping data entry with missing file path")
            continue

        if not isinstance(category, str) or not category:
            warnings.append(f"skipping data entry with missing category: {source_file}")
            continue

        normalized_entry = dict(entry)
        raw_content = _entry_content(entry)
        normalized_entry["full_content"] = _filter_meta_content(raw_content)
        normalized_entry["type"] = _json_type(normalized_entry["full_content"])
        if not isinstance(normalized_entry.get("domain"), str) or not normalized_entry.get("domain"):
            normalized_entry["domain"] = _derive_domain_from_file(source_file)

        category_dir = os.path.join(config.CONTENT_DATA, *category.split("/"))
        config.ensure_dir(category_dir)

        output_file = os.path.join(category_dir, f"{_slug_from_path(source_file)}.md")
        page_content = _render_page(
            entry=normalized_entry,
            referenced_by=referenced_by_map.get(source_file, []),
            output_dir=category_dir,
            trait_data=trait_data,
            emotion_presets=emotion_presets,
            decay_config=decay_config,
            stressor_data=stressor_data,
        )
        page_content = _preserve_manual_blocks(output_file, page_content)
        _write_markdown(output_file, page_content, files_written, errors)

        manifest_meta = manifest_meta_by_file.get(source_file, {})
        stats = normalized_entry.get("stats") if isinstance(normalized_entry.get("stats"), dict) else {}

        key_count: int | str = "-"
        if isinstance(manifest_meta, dict):
            keys_count = manifest_meta.get("keys_count")
            if isinstance(keys_count, int):
                key_count = keys_count
            else:
                item_keys = manifest_meta.get("item_keys")
                if isinstance(item_keys, list):
                    key_count = len(item_keys)

        if key_count == "-":
            key_count = stats.get("total_keys", "-")

        items_count = manifest_meta.get("items_count") if isinstance(manifest_meta, dict) else "-"
        if not isinstance(items_count, int):
            items_count = "-"

        index_rel_link = os.path.relpath(output_file, config.CONTENT_DATA)
        grouped_for_index[_domain_group(normalized_entry)].append(
            {
                "file": source_file,
                "category": category,
                "type": normalized_entry.get("type", "unknown"),
                "key_count": key_count,
                "items_count": items_count,
                "index_rel_link": index_rel_link,
            }
        )

        processed_count += 1

    index_path = os.path.join(config.CONTENT_DATA, "_index.md")
    index_sources = ["extracted/data_files.json"]

    optional_sources = {
        "references.json": os.path.join(config.EXTRACTED_DIR, "references.json"),
        "trait_data.json": os.path.join(config.EXTRACTED_DIR, "trait_data.json"),
        "emotion_presets.json": os.path.join(config.EXTRACTED_DIR, "emotion_presets.json"),
        "decay_config.json": os.path.join(config.EXTRACTED_DIR, "decay_config.json"),
        "stressor_data.json": os.path.join(config.EXTRACTED_DIR, "stressor_data.json"),
    }
    for source_name, source_path in optional_sources.items():
        if os.path.exists(source_path):
            index_sources.append(f"extracted/{source_name}")

    index_content = _render_index_page(grouped_for_index, index_sources)
    index_content = _preserve_manual_blocks(index_path, index_content)
    _write_markdown(index_path, index_content, files_written, errors)

    return {
        "files_written": files_written,
        "items_processed": processed_count,
        "warnings": warnings,
        "errors": errors,
    }
