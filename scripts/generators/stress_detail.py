"""Generate detailed stress-system documentation from extracted pipeline data."""

from __future__ import annotations

import os
import re
from typing import Any

import scripts.config as config


_MANUAL_START = "<!-- MANUAL:START -->"
_MANUAL_END = "<!-- MANUAL:END -->"
_STRESS_SYSTEM_FILE = "scripts/systems/stress_system.gd"


def _as_dict(value: Any) -> dict[str, Any]:
    return value if isinstance(value, dict) else {}


def _as_list(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def _escape_md_cell(value: Any) -> str:
    return str(value).replace("|", r"\|").replace("\n", " ").strip()


def _yaml_quote(value: str) -> str:
    escaped = value.replace("\\", "\\\\").replace('"', r'\"')
    return f'"{escaped}"'


def _to_float(value: Any) -> float | None:
    if isinstance(value, bool):
        return None
    if isinstance(value, (int, float)):
        return float(value)
    if isinstance(value, str):
        text = value.strip()
        if not text:
            return None
        if text.startswith("{"):
            return None
        try:
            return float(text)
        except ValueError:
            return None
    return None


def _format_number(value: Any, digits: int = 3) -> str:
    number = _to_float(value)
    if number is None:
        return "n/a"
    if abs(number - round(number)) < 1e-9:
        return f"{int(round(number))}"
    formatted = f"{number:.{digits}f}".rstrip("0").rstrip(".")
    return formatted


def _title_from_category(category: str) -> str:
    token = category.replace("_", " ").strip()
    return token.title() if token else "Unknown"


def _extract_manual_block(text: str) -> str | None:
    start = text.find(_MANUAL_START)
    if start < 0:
        return None
    end = text.find(_MANUAL_END, start)
    if end < 0:
        return None
    end += len(_MANUAL_END)
    return text[start:end]


def _merge_manual_block(new_text: str, existing_text: str) -> str:
    existing_block = _extract_manual_block(existing_text)
    if not existing_block:
        return new_text

    pattern = re.compile(
        re.escape(_MANUAL_START) + r".*?" + re.escape(_MANUAL_END),
        flags=re.DOTALL,
    )
    if pattern.search(new_text):
        return pattern.sub(existing_block, new_text, count=1)

    return new_text.rstrip() + "\n\n" + existing_block + "\n"


def _find_stress_system_entry(systems_data: dict[str, Any]) -> dict[str, Any]:
    systems = _as_list(_as_dict(systems_data).get("systems"))
    for entry in systems:
        item = _as_dict(entry)
        file_path = item.get("file")
        if isinstance(file_path, str) and file_path.endswith("stress_system.gd"):
            return item
        if item.get("system_name") == "stress":
            return item
    return {}


def _index_named_entries(entries: list[Any]) -> dict[str, dict[str, Any]]:
    indexed: dict[str, dict[str, Any]] = {}
    for entry in entries:
        item = _as_dict(entry)
        name = item.get("name")
        if isinstance(name, str) and name:
            indexed[name] = item
    return indexed


def _function_line(system_entry: dict[str, Any], function_name: str) -> int | None:
    for raw in _as_list(system_entry.get("functions")):
        item = _as_dict(raw)
        if item.get("name") != function_name:
            continue
        line = item.get("line")
        if isinstance(line, int) and line > 0:
            return line
    return None


def _source_ref(path: str, line: int | None = None) -> str:
    if isinstance(line, int) and line > 0:
        return f"`{path}:L{line}`"
    return f"`{path}`"


def _constant_number(constants: dict[str, dict[str, Any]], name: str) -> float | None:
    entry = constants.get(name, {})
    return _to_float(entry.get("value"))


def _parse_gd_dict_const(gd_text: str, const_name: str) -> dict[str, float]:
    pattern = re.compile(
        rf"const\s+{re.escape(const_name)}\s*:\s*Dictionary\s*=\s*\{{(.*?)\}}",
        flags=re.DOTALL,
    )
    match = pattern.search(gd_text)
    if not match:
        return {}

    parsed: dict[str, float] = {}
    body = match.group(1)
    for pair in re.finditer(r'"([A-Za-z_]\w*)"\s*:\s*(-?(?:\d+(?:\.\d+)?|\.\d+))', body):
        parsed[pair.group(1)] = float(pair.group(2))
    return parsed


def _collect_stress_model_refs(
    stressor_data: dict[str, Any],
    formulas_data: dict[str, Any],
) -> dict[str, str]:
    refs: dict[str, str] = {
        "lazarus": "Lazarus & Folkman (1984): Transactional Model of Stress — demand/resource appraisal",
        "selye": "Selye (1956): General Adaptation Syndrome (GAS) — alarm/resistance/exhaustion stages",
        "mcewen": "McEwen (1998): Allostatic Load — chronic stress wear on the body",
        "yerkes": "Yerkes & Dodson (1908): Inverted-U performance curve — optimal stress for efficiency",
        "cor": "Hobfoll (1989): Conservation of Resources (COR) — loss events hit 2.5× harder",
    }

    for key, value in _as_dict(stressor_data.get("model_references")).items():
        if not isinstance(key, str) or not isinstance(value, str):
            continue
        lowered = key.lower()
        if "lazarus" in lowered:
            refs["lazarus"] = value
        elif "cor" in lowered or "hobfoll" in lowered:
            refs["cor"] = value

    for formula in _as_list(formulas_data.get("formulas")):
        model_ref = _as_dict(_as_dict(formula).get("model_ref"))
        name = model_ref.get("name")
        if not isinstance(name, str):
            continue
        lowered = name.lower()
        if "yerkes" in lowered:
            refs["yerkes"] = name
        elif "allostatic" in lowered or "mcewen" in lowered:
            refs["mcewen"] = name
        elif "general adaptation" in lowered or "selye" in lowered:
            refs["selye"] = name
        elif "lazarus" in lowered:
            refs["lazarus"] = name
        elif "hobfoll" in lowered or "cor" in lowered:
            refs["cor"] = name

    return refs


def _collect_emotion_weights(stress_path: str, warnings: list[str]) -> dict[str, float]:
    source_file = stress_path if os.path.isabs(stress_path) else config.source_path(stress_path)
    if not os.path.exists(source_file):
        warnings.append(f"missing stress source file for emotion weights: {source_file}")
        return {}

    try:
        with open(source_file, "r", encoding="utf-8") as handle:
            gd_text = handle.read()
    except OSError as exc:
        warnings.append(f"failed to read stress source file for emotion weights ({source_file}): {exc}")
        return {}

    weights = _parse_gd_dict_const(gd_text, "EMOTION_WEIGHTS")
    if not weights:
        warnings.append(f"EMOTION_WEIGHTS not found in {source_file}")
    return weights


def _collect_events_by_category(
    stressor_data: dict[str, Any],
) -> tuple[list[str], dict[str, list[dict[str, Any]]], dict[str, dict[str, Any]]]:
    events = [_as_dict(item) for item in _as_list(stressor_data.get("events")) if isinstance(item, dict)]
    event_by_id: dict[str, dict[str, Any]] = {}
    category_map: dict[str, list[dict[str, Any]]] = {}

    for event in events:
        event_id = event.get("id")
        if not isinstance(event_id, str) or not event_id:
            continue
        event_by_id[event_id] = event
        category = event.get("category")
        if not isinstance(category, str) or not category:
            category = "unknown"
        category_map.setdefault(category, []).append(event)

    by_category_ids = _as_dict(stressor_data.get("by_category"))
    for category, entries in by_category_ids.items():
        if not isinstance(category, str):
            continue
        event_ids = [item for item in _as_list(entries) if isinstance(item, str)]
        ordered = [event_by_id[event_id] for event_id in event_ids if event_id in event_by_id]
        if ordered:
            category_map[category] = ordered

    for category in list(category_map.keys()):
        category_map[category].sort(
            key=lambda event: _to_float(event.get("severity_score")) or 0.0,
            reverse=True,
        )

    ordered_categories = sorted(
        category_map.keys(),
        key=lambda category: (
            max((_to_float(ev.get("severity_score")) or 0.0 for ev in category_map.get(category, [])), default=0.0),
            category,
        ),
        reverse=True,
    )

    return ordered_categories, category_map, event_by_id


def _collect_personality_rows(
    ordered_events: list[dict[str, Any]],
) -> tuple[list[tuple[str, str, float, str]], list[tuple[str, str, float, str]]]:
    axis_rows: list[tuple[str, str, float, str]] = []
    trait_rows: list[tuple[str, str, float, str]] = []

    for event in ordered_events:
        event_id = event.get("id") if isinstance(event.get("id"), str) else "unknown"

        for axis_item in _as_list(event.get("axis_modifiers")):
            modifier = _as_dict(axis_item)
            axis = modifier.get("axis")
            weight = _to_float(modifier.get("weight"))
            direction = modifier.get("direction")
            if not isinstance(axis, str) or weight is None:
                continue
            axis_rows.append(
                (
                    event_id,
                    axis,
                    weight,
                    direction if isinstance(direction, str) and direction else "n/a",
                )
            )

        for trait_item in _as_list(event.get("trait_modifiers")):
            modifier = _as_dict(trait_item)
            trait = modifier.get("trait")
            multiplier = _to_float(modifier.get("multiplier"))
            if not isinstance(trait, str) or multiplier is None:
                continue
            diff = (multiplier - 1.0) * 100.0
            if diff > 0:
                effect = f"+{_format_number(diff, digits=1)}% stress"
            elif diff < 0:
                effect = f"{_format_number(diff, digits=1)}% stress"
            else:
                effect = "0%"
            trait_rows.append((event_id, trait, multiplier, effect))

    return axis_rows, trait_rows


def _render_markdown(
    manifest: dict[str, Any],
    extracted: dict[str, Any],
    warnings: list[str],
) -> str:
    del manifest  # Reserved for future ticket extensions.

    stressor_data = _as_dict(extracted.get("stressor_data"))
    decay_config = _as_dict(extracted.get("decay_config"))
    formulas_data = _as_dict(extracted.get("formulas"))
    systems_data = _as_dict(extracted.get("systems"))
    constants_data = _as_dict(extracted.get("constants"))

    stress_system = _find_stress_system_entry(systems_data)
    if not stress_system:
        warnings.append("systems.stress entry not found; source line references may be incomplete")

    stress_constants = _index_named_entries(_as_list(stress_system.get("constants")))
    game_constants = _index_named_entries(_as_list(constants_data.get("constants")))

    if not stressor_data:
        warnings.append("missing extracted.stressor_data")
    if not decay_config:
        warnings.append("missing extracted.decay_config")
    if not formulas_data:
        warnings.append("missing extracted.formulas")
    if not systems_data:
        warnings.append("missing extracted.systems")
    if not constants_data:
        warnings.append("missing extracted.constants")

    stress_path = stress_system.get("file") if isinstance(stress_system.get("file"), str) else _STRESS_SYSTEM_FILE
    stressor_source = stressor_data.get("source_file") if isinstance(stressor_data.get("source_file"), str) else "data/stressor_events.json"
    decay_source = decay_config.get("source_file") if isinstance(decay_config.get("source_file"), str) else "data/species/human/emotions/decay_parameters.json"

    model_refs = _collect_stress_model_refs(stressor_data, formulas_data)

    va_gamma = _constant_number(stress_constants, "VA_GAMMA")
    eustress_optimal = _constant_number(stress_constants, "EUSTRESS_OPTIMAL")
    base_decay = _constant_number(stress_constants, "BASE_DECAY_PER_TICK")
    sleep_bonus = _constant_number(stress_constants, "SLEEP_DECAY_BONUS")
    safe_bonus = _constant_number(stress_constants, "SAFE_DECAY_BONUS")
    support_mult = _constant_number(stress_constants, "SUPPORT_DECAY_MULT")

    allo_rate = _constant_number(stress_constants, "ALLO_RATE")
    allo_stress_threshold = _constant_number(stress_constants, "ALLO_STRESS_THRESHOLD")
    allo_recovery_threshold = _constant_number(stress_constants, "ALLO_RECOVERY_THRESHOLD")
    allo_recovery_rate = _constant_number(stress_constants, "ALLO_RECOVERY_RATE")

    reserve_max = _constant_number(stress_constants, "RESERVE_MAX")
    threshold_tense = _constant_number(stress_constants, "THRESHOLD_TENSE")
    threshold_crisis = _constant_number(stress_constants, "THRESHOLD_CRISIS")
    threshold_break = _constant_number(stress_constants, "THRESHOLD_BREAK_RISK")

    hunger_eat_threshold = _constant_number(game_constants, "HUNGER_EAT_THRESHOLD")

    emotion_weights = _collect_emotion_weights(stress_path, warnings)

    ordered_categories, events_by_category, _ = _collect_events_by_category(stressor_data)
    ordered_events: list[dict[str, Any]] = []
    for category in ordered_categories:
        ordered_events.extend(events_by_category.get(category, []))

    axis_rows, trait_rows = _collect_personality_rows(ordered_events)

    stress_nav_order = stress_system.get("priority")
    nav_order = 35
    if isinstance(stress_nav_order, int):
        nav_order = stress_nav_order + 1

    source_files: list[str] = []
    for file_path in [
        stress_path,
        stressor_source,
        decay_source,
        "extracted/stressor_data.json",
        "extracted/decay_config.json",
        "extracted/formulas.json",
        "extracted/systems.json",
        "extracted/constants.json",
    ]:
        if isinstance(file_path, str) and file_path and file_path not in source_files:
            source_files.append(file_path)

    lines: list[str] = [
        "---",
        f"title: {_yaml_quote('Stress System — Detailed Documentation')}",
        f"description: {_yaml_quote('Lazarus appraisal, stress accumulation/recovery, allostatic load, GAS stages, and eustress curve')}",
        "generated: true",
        "source_files:",
    ]
    for file_path in source_files:
        lines.append(f"  - {_yaml_quote(file_path)}")
    lines.extend(
        [
            f"nav_order: {nav_order}",
            "---",
            "",
            "# Stress System — Detailed Documentation",
            "",
            "## Overview",
            "",
            "The stress system implements a **multi-source stress accumulation and recovery model** based on:",
            f"- **{model_refs['lazarus']}**",
            f"- **{model_refs['selye']}**",
            f"- **{model_refs['mcewen']}**",
            f"- **{model_refs['yerkes']}**",
            f"- **{model_refs['cor']}**",
            "",
            "Localization: 한국어 / English labels are shown where source data provides both.",
            "",
            "## Stress Pipeline (per tick)",
            "",
            "```mermaid",
            "graph TD",
            "    A[Lazarus Appraisal] --> B[Continuous Stressors]",
            "    B --> C[Emotion → Stress Conversion]",
            "    C --> D[Personality Modifiers]",
            "    D --> E[Total Stress Δ]",
            "    E --> F[Recovery Calculation]",
            "    F --> G[Net Stress Change]",
            "    G --> H[Allostatic Load Update]",
            "    H --> I[GAS Stage Update]",
            "    I --> J[Yerkes-Dodson Efficiency]",
            "```",
            "",
            f"📄 source: {_source_ref(stress_path, _function_line(stress_system, 'execute_tick'))}",
            "",
            "## Lazarus Appraisal Scale",
            "",
            "The demand/resource ratio determines stress:",
            "",
            "$$",
            r"\text{appraisal} = \frac{D}{R}",
            "$$",
            "",
            "Where:",
            "- $D$ = demand composite (weighted by HEXACO personality modulation)",
            "- $R$ = resource composite",
            "",
            "| Ratio | Interpretation | Effect |",
            "|:------|:---------------|:-------|",
            "| < 0.5 | Low demand relative to resources | Eustress zone |",
            "| 0.5 - 1.0 | Balanced | Normal stress |",
            "| 1.0 - 2.0 | Demand exceeds resources | Distress |",
            "| > 2.0 | Overwhelmed | Severe stress, GAS alarm |",
            "",
            f"📄 source: {_source_ref(stress_path, _function_line(stress_system, '_calc_appraisal_scale'))}",
            "",
            "## Continuous Stressors",
            "",
            "These stressors accumulate every tick based on entity state:",
            "",
            "| Stressor | Condition | Formula | Source |",
            "|:---------|:----------|:--------|:-------|",
            "| Hunger | food_satiety < threshold"
            + (f" (`HUNGER_EAT_THRESHOLD={_format_number(hunger_eat_threshold, 2)}`)" if hunger_eat_threshold is not None else "")
            + " | `stress += (threshold - satiety) * hunger_mult` | Needs system |",
            "| Energy | energy < threshold | `stress += (threshold - energy) * energy_mult` | Needs system |",
            "| Social isolation | social_need < threshold | `stress += (threshold - social) * social_mult` | Social system |",
            "| Overcrowding | density > threshold | `stress += (density - threshold) * crowd_mult` | Settlement |",
            "",
            f"📄 source: {_source_ref(stress_path, _function_line(stress_system, '_calc_continuous_stressors'))}",
            "",
            "## Emotion → Stress Contribution",
            "",
            "Negative emotions contribute to stress via weighted sum:",
            "",
            "$$",
            r"\text{emotion\_stress} = \gamma_{VA} \sum_e w_e \cdot \text{emotion}_e",
            "$$",
            "",
            "Where:",
            (
                f"- $\\gamma_{{VA}}$ = `{_format_number(va_gamma, 3)}` (from `VA_GAMMA`)"
                if va_gamma is not None
                else "- $\\gamma_{VA}$ = valence-arousal gamma coefficient"
            ),
            "- $w_e$ = per-emotion weight",
            "",
            "| Emotion | Weight | Rationale |",
            "|:--------|------:|:----------|",
        ]
    )

    rationale_by_emotion = {
        "fear": "최고 스트레스 기여 — 고각성 부정 감정 (highest stress contribution, high arousal negative)",
        "anger": "고각성 부정 감정 (high arousal, negative valence)",
        "sadness": "저각성 부정 감정 (low arousal, negative valence)",
        "disgust": "중간 기여 부정 감정 (moderate negative contribution)",
        "surprise": "낮은 기여 (low contribution, valence-neutral)",
        "joy": "스트레스 감소 경로 (stress reduction pathway, negative weight)",
        "trust": "스트레스 감소 경로 (stress reduction pathway, negative weight)",
        "anticipation": "미약한 스트레스 감소 (mild stress reduction, anticipatory)",
    }

    preferred_emotions = ["fear", "anger", "sadness", "disgust", "surprise", "joy", "trust", "anticipation"]
    emitted: set[str] = set()
    for emotion in preferred_emotions:
        emitted.add(emotion)
        if emotion in emotion_weights:
            weight_text = f"{emotion_weights[emotion]:.3f}"
        else:
            weight_text = "n/a"
        lines.append(
            "| "
            + " | ".join(
                [
                    _escape_md_cell(_title_from_category(emotion)),
                    _escape_md_cell(weight_text),
                    _escape_md_cell(rationale_by_emotion.get(emotion, "Extracted emotion weight")),
                ]
            )
            + " |"
        )

    for emotion in sorted(emotion_weights.keys()):
        if emotion in emitted:
            continue
        lines.append(
            "| "
            + " | ".join(
                [
                    _escape_md_cell(_title_from_category(emotion)),
                    _escape_md_cell(f"{emotion_weights[emotion]:.3f}"),
                    "Extracted emotion weight",
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            f"📄 source: {_source_ref(stress_path, _function_line(stress_system, '_calc_emotion_contribution'))}",
            f"📄 source: {_source_ref(decay_source)}",
            "",
            "## Stress Recovery",
            "",
            "Recovery occurs when conditions are met:",
            "",
            "$$",
            r"\text{recovery} = \text{base\_recovery} \cdot (1 + \text{sleep\_bonus} + \text{safety\_bonus} + \text{support\_bonus}) \cdot \text{resilience}",
            "$$",
            "",
            "| Bonus | Condition | Value | Source |",
            "|:------|:----------|------:|:-------|",
            "| Sleep | entity sleeping | +"
            + _format_number(sleep_bonus, 3)
            + " | Needs system |",
            "| Safety | entity in safe location | +"
            + _format_number(safe_bonus, 3)
            + " | Settlement |",
            "| Social support | positive social bonds nearby | +support_score * "
            + _format_number(support_mult, 3)
            + " | Social system |",
            "| Resilience | personality-derived factor | ×dynamic | CD-RISC based |",
            "",
            "Base recovery term:",
            f"- `BASE_DECAY_PER_TICK` = {_format_number(base_decay, 3)}",
            "",
            f"📄 source: {_source_ref(stress_path, _function_line(stress_system, '_calc_recovery'))}",
            "",
            "## Allostatic Load (Chronic Stress)",
            "",
            "Allostatic load represents cumulative physiological wear from chronic stress:",
            "",
            "$$",
            r"\text{allostatic}_{t+1} = \begin{cases}",
            r"\text{allostatic}_t + \alpha \cdot (\text{stress} - \text{threshold}) & \text{if stress > threshold} \\",
            r"\text{allostatic}_t \cdot (1 - \beta) & \text{if stress < threshold and safe}",
            r"\end{cases}",
            "$$",
            "",
            f"- Range: 0-{_format_number(reserve_max, 1)}",
            f"- Accumulates when stress exceeds `{_format_number(allo_stress_threshold, 3)}`",
            f"- Recovery starts under `{_format_number(allo_recovery_threshold, 3)}` in safe conditions",
            f"- Parameters: `alpha={_format_number(allo_rate, 4)}`, `beta={_format_number(allo_recovery_rate, 4)}`",
            "- High allostatic load increases mortality risk (feeds into Siler model)",
            "",
            f"📄 source: {_source_ref(stress_path, _function_line(stress_system, '_update_allostatic'))}",
            "",
            "## General Adaptation Syndrome (Selye 1956)",
            "",
            "| Stage | Condition | Reserve Effect | Duration |",
            "|:------|:----------|:---------------|:---------|",
            "| Alarm | Acute stress event (stress >= " + _format_number(threshold_tense, 1) + ") | Reserve depletes rapidly | Short |",
            "| Resistance | Sustained stress (stress >= " + _format_number(threshold_crisis, 1) + ") | Reserve depletes slowly | Variable |",
            "| Exhaustion | Reserve depleted or break-risk stress >= " + _format_number(threshold_break, 1) + " | Collapse, mental break risk | Until recovery |",
            "",
            "$$",
            r"\text{reserve}_{t+1} = \text{reserve}_t - \text{drain}(\text{stress}, \text{stage})",
            "$$",
            "",
            f"- Reserve range: 0-{_format_number(reserve_max, 1)}",
            "- Stage transitions are driven by reserve and prolonged stress exposure",
            "",
            f"📄 source: {_source_ref(stress_path, _function_line(stress_system, '_update_reserve'))}",
            "",
            "## Yerkes-Dodson Efficiency Curve",
            "",
            "Moderate stress improves performance (eustress):",
            "",
            "$$",
            r"\text{efficiency} = 1.0 + \text{eustress\_bonus} \cdot e^{-\left(\frac{\text{stress} - \text{optimal}}{\sigma}\right)^2}",
            "$$",
            "",
            f"- Extracted optimal stress (`EUSTRESS_OPTIMAL`): `{_format_number(eustress_optimal, 3)}`",
            "- Too little stress → low motivation",
            "- Optimal stress → peak performance",
            "- Too much stress → impaired performance",
            "",
            f"📄 source: {_source_ref(stress_path, _function_line(stress_system, 'get_work_efficiency'))}",
            "",
            "## Stressor Events",
            "",
            "### By Category",
            "",
            f"📄 source: {_source_ref(stressor_source)}",
            "",
        ]
    )

    if not ordered_categories:
        lines.append("No stressor events were found in extracted data.")
        lines.append("")

    for category in ordered_categories:
        title = _title_from_category(category)
        suffix = " (highest severity)" if category == "death" else ""
        lines.extend(
            [
                f"#### {title} Events{suffix}",
                "",
                "| Event | Name (EN) | Name (KR) | Severity | Instant | Per-tick | Is Loss |",
                "|:------|:----------|:----------|---------:|--------:|---------:|:-------:|",
            ]
        )
        events = events_by_category.get(category, [])
        if not events:
            lines.append("| - | - | - | - | - | - | - |")
            lines.append("")
            continue

        for event in events:
            lines.append(
                "| "
                + " | ".join(
                    [
                        _escape_md_cell(event.get("id", "")),
                        _escape_md_cell(event.get("name_en", "")),
                        _escape_md_cell(event.get("name_kr", "")),
                        _escape_md_cell(_format_number(event.get("severity_score"), 3)),
                        _escape_md_cell(_format_number(event.get("base_instant"), 3)),
                        _escape_md_cell(_format_number(event.get("base_per_tick"), 3)),
                        "Yes" if bool(event.get("is_loss")) else "No",
                    ]
                )
                + " |"
            )
        lines.append("")

    lines.extend(
        [
            "## Personality Modifiers",
            "",
            "Each stressor's impact is modulated by HEXACO personality:",
            "",
            "### Axis Modifiers",
            "",
            "| Stressor | Axis | Weight | Direction |",
            "|:---------|:----:|------:|:----------|",
        ]
    )

    if not axis_rows:
        lines.append("| - | - | - | - |")
    else:
        for stressor, axis, weight, direction in axis_rows:
            lines.append(
                "| "
                + " | ".join(
                    [
                        _escape_md_cell(stressor),
                        _escape_md_cell(axis),
                        _escape_md_cell(_format_number(weight, 3)),
                        _escape_md_cell(direction),
                    ]
                )
                + " |"
            )

    lines.extend(
        [
            "",
            "### Trait Modifiers",
            "",
            "| Stressor | Trait | Multiplier | Effect |",
            "|:---------|:------|-----------:|:-------|",
        ]
    )

    if not trait_rows:
        lines.append("| - | - | - | - |")
    else:
        for stressor, trait, multiplier, effect in trait_rows:
            lines.append(
                "| "
                + " | ".join(
                    [
                        _escape_md_cell(stressor),
                        _escape_md_cell(trait),
                        _escape_md_cell(_format_number(multiplier, 3)),
                        _escape_md_cell(effect),
                    ]
                )
                + " |"
            )

    lines.extend(
        [
            "",
            f"📄 source: {_source_ref(stress_path, _function_line(stress_system, '_calc_personality_scale'))}",
            "",
            _MANUAL_START,
            "",
            _MANUAL_END,
            "",
        ]
    )

    return "\n".join(lines)


def run(manifest: dict, extracted: dict) -> dict:
    """Generate stress system detail documentation.

    Args:
        manifest: The manifest.json data from Phase 1.
        extracted: Aggregated extracted data payloads.

    Returns:
        dict with keys:
            - files_written: list of output file paths
            - pages_generated: int count
            - warnings: list of warning strings
            - errors: list of error strings
    """
    warnings: list[str] = []
    errors: list[str] = []
    files_written: list[str] = []

    if not isinstance(manifest, dict):
        warnings.append("manifest is not an object; continuing with empty manifest")
        manifest = {}

    if not isinstance(extracted, dict):
        warnings.append("extracted is not an object; continuing with empty extracted data")
        extracted = {}

    markdown = _render_markdown(manifest, extracted, warnings)

    output_path = os.path.join(config.CONTENT_SYSTEMS, "stress-detail.md")
    config.ensure_dir(os.path.dirname(output_path))

    existing_content = ""
    if os.path.exists(output_path):
        try:
            with open(output_path, "r", encoding="utf-8") as handle:
                existing_content = handle.read()
        except OSError as exc:
            warnings.append(f"failed to read existing markdown for MANUAL merge ({output_path}): {exc}")

    final_content = _merge_manual_block(markdown, existing_content)

    try:
        with open(output_path, "w", encoding="utf-8") as handle:
            handle.write(final_content)
        files_written.append(output_path)
    except OSError as exc:
        errors.append(f"failed to write {output_path}: {exc}")

    return {
        "files_written": files_written,
        "pages_generated": 1 if files_written else 0,
        "items_processed": 1 if files_written else 0,
        "warnings": warnings,
        "errors": errors,
    }
