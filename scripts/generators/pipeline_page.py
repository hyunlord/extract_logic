"""Generate a master documentation page for the personality→emotion→stress→mortality pipeline."""

from __future__ import annotations

import math
import os
from typing import Any

import scripts.config as config

_MANUAL_START = "<!-- MANUAL:START -->"
_MANUAL_END = "<!-- MANUAL:END -->"


def _as_dict(value: Any) -> dict[str, Any]:
    return value if isinstance(value, dict) else {}


def _as_list(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def _as_float(value: Any, default: float = 0.0) -> float:
    if isinstance(value, (int, float)):
        return float(value)
    if isinstance(value, str):
        try:
            return float(value.strip())
        except ValueError:
            return default
    return default


def _as_int(value: Any, default: int = 0) -> int:
    if isinstance(value, bool):
        return default
    if isinstance(value, int):
        return value
    if isinstance(value, float) and value.is_integer():
        return int(value)
    if isinstance(value, str):
        try:
            return int(value.strip())
        except ValueError:
            return default
    return default


def _fmt_num(value: float, digits: int = 2) -> str:
    if abs(value - round(value)) < 1e-9:
        return str(int(round(value)))
    return f"{value:.{digits}f}".rstrip("0").rstrip(".")


def _yaml_quote(value: str) -> str:
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def _preserve_manual_block(new_text: str, existing_text: str) -> str:
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


def _extract_sections(extracted: dict[str, Any], warnings: list[str]) -> dict[str, dict[str, Any]]:
    required = [
        "systems",
        "formulas",
        "references",
        "trait_data",
        "stressor_data",
        "emotion_presets",
        "decay_config",
    ]

    out: dict[str, dict[str, Any]] = {}
    for key in required:
        payload = extracted.get(key)
        if not isinstance(payload, dict):
            warnings.append(f"Missing or invalid extracted section: {key}")
            payload = {}
        out[key] = payload

    data_files = extracted.get("data_files")
    if isinstance(data_files, dict):
        out["data_files"] = data_files
    else:
        out["data_files"] = {}

    return out


def _find_system_by_file(systems: list[dict[str, Any]], file_name: str) -> dict[str, Any]:
    for entry in systems:
        if entry.get("file") == file_name:
            return entry
    return {}


def _function_line(system: dict[str, Any], name: str) -> int | None:
    for fn in _as_list(system.get("functions")):
        if not isinstance(fn, dict):
            continue
        if fn.get("name") == name and isinstance(fn.get("line"), int):
            return fn["line"]
    return None


def _tick_interval_text(system: dict[str, Any]) -> str:
    if isinstance(system.get("tick_interval"), (int, float)):
        value = float(system["tick_interval"])
        return _fmt_num(value)
    raw = system.get("tick_interval_raw")
    if isinstance(raw, str) and raw.strip():
        return f"config ({raw.strip()})"
    return "n/a"


def _collect_formula_strings(sections: dict[str, dict[str, Any]]) -> list[str]:
    formulas: set[str] = set()

    for item in _as_list(sections["formulas"].get("formulas")):
        if not isinstance(item, dict):
            continue
        for key in ("expression", "latex", "formula", "code"):
            value = item.get(key)
            if isinstance(value, str) and value.strip():
                formulas.add(value.strip())
                break

    impulse_formulas = _as_dict(sections["emotion_presets"].get("impulse_formulas"))
    for value in impulse_formulas.values():
        if isinstance(value, str) and value.strip():
            formulas.add(value.strip())

    decay = sections["decay_config"]
    for section_key, formula_key in (
        ("personality_coupling", "formula"),
        ("inhibition", "formula"),
        ("mental_break", "probability_formula"),
    ):
        value = _as_dict(decay.get(section_key)).get(formula_key)
        if isinstance(value, str) and value.strip():
            formulas.add(value.strip())

    formulas.add("mu(x) = a1 * exp(-b1 * x) + a2 + a3 * exp(b3 * x)")
    formulas.add("P(death) = 1 - exp(-mu_final(x) / TICKS_PER_YEAR)")
    return sorted(formulas)


def _collect_models(sections: dict[str, dict[str, Any]]) -> list[str]:
    models: set[str] = set()

    for key in ("emotion_presets", "stressor_data", "decay_config"):
        refs = _as_dict(sections[key].get("model_references"))
        for value in refs.values():
            if isinstance(value, str) and value.strip():
                models.add(value.strip())

    models.update(
        {
            "Ashton & Lee (2007) HEXACO Personality Model",
            "Selye (1956) General Adaptation Syndrome",
            "McEwen (1998) Allostatic Load",
            "Yerkes & Dodson (1908) arousal-performance law",
            "Siler (1979) hazard model",
        }
    )

    return sorted(models)


def _extract_mortality_baseline(sections: dict[str, dict[str, Any]]) -> dict[str, float]:
    data_files = sections.get("data_files", {})
    for item in _as_list(data_files.get("files")):
        if not isinstance(item, dict):
            continue
        if item.get("file") != "data/species/human/mortality/siler_parameters.json":
            continue
        full_content = _as_dict(item.get("full_content"))
        baseline = _as_dict(full_content.get("baseline"))
        if baseline:
            return {
                "a1": _as_float(baseline.get("a1"), 0.6),
                "b1": _as_float(baseline.get("b1"), 1.3),
                "a2": _as_float(baseline.get("a2"), 0.01),
                "a3": _as_float(baseline.get("a3"), 0.00006),
                "b3": _as_float(baseline.get("b3"), 0.09),
            }

    return {"a1": 0.6, "b1": 1.3, "a2": 0.01, "a3": 0.00006, "b3": 0.09}


def _siler_mu(age_years: float, params: dict[str, float]) -> float:
    return (
        params["a1"] * math.exp(-params["b1"] * age_years)
        + params["a2"]
        + params["a3"] * math.exp(params["b3"] * age_years)
    )


def _ten_year_survival(age_years: float, params: dict[str, float], hazard_mult: float) -> float:
    mu = _siler_mu(age_years, params) * hazard_mult
    return math.exp(-mu * 10.0)


def _eval_formula(formula: str, values: dict[str, float]) -> float | None:
    safe_globals = {"__builtins__": {}}
    safe_locals = {
        "max": max,
        "min": min,
        "abs": abs,
    }
    safe_locals.update(values)

    try:
        result = eval(formula, safe_globals, safe_locals)  # noqa: S307 - controlled formulas only
    except Exception:
        return None

    if isinstance(result, (int, float)):
        return float(result)
    return None


def _source_ref(path: str, line: int | None = None) -> str:
    if line is None:
        return f"📄 source: `{path}`"
    return f"📄 source: `{path}:L{line}`"


def _build_markdown(manifest: dict[str, Any], sections: dict[str, dict[str, Any]], warnings: list[str]) -> str:
    _ = manifest

    systems_list = [s for s in _as_list(sections["systems"].get("systems")) if isinstance(s, dict)]
    formulas_all = _collect_formula_strings(sections)
    models_all = _collect_models(sections)

    personality_gen = _find_system_by_file(systems_list, "scripts/systems/personality_generator.gd")
    personality_maturation = _find_system_by_file(systems_list, "scripts/systems/personality_maturation.gd")
    trait_system = _find_system_by_file(systems_list, "scripts/systems/trait_system.gd")
    emotion_system = _find_system_by_file(systems_list, "scripts/systems/emotion_system.gd")
    stress_system = _find_system_by_file(systems_list, "scripts/systems/stress_system.gd")
    mortality_system = _find_system_by_file(systems_list, "scripts/systems/mortality_system.gd")

    emotion_tick_interval = _tick_interval_text(emotion_system)
    stress_tick_interval = _tick_interval_text(stress_system)
    mortality_tick_interval = _tick_interval_text(mortality_system)

    trait_data = sections["trait_data"]
    stressor_data = sections["stressor_data"]
    emotion_presets = sections["emotion_presets"]
    decay_config = sections["decay_config"]
    references = sections["references"]

    trait_count = _as_int(_as_dict(trait_data.get("stats")).get("total_traits"), len(_as_list(trait_data.get("traits"))))
    axis_data = _as_dict(trait_data.get("hexaco_axes"))
    axis_count = len(axis_data)

    impulse_formulas = _as_dict(emotion_presets.get("impulse_formulas"))
    formula_order = ["joy", "trust", "fear", "surprise", "sadness", "disgust", "anger", "anticipation"]

    appraisal_values = {
        "I": 95.0,
        "g": -0.9,
        "n": 0.3,
        "c": 0.1,
        "a": -0.8,
        "m": 0.0,
        "p": 0.0,
        "b": -0.7,
        "fr": 0.4,
    }

    computed_impulses: dict[str, float] = {}
    for emotion in formula_order:
        formula = impulse_formulas.get(emotion)
        if isinstance(formula, str) and formula.strip():
            value = _eval_formula(formula, appraisal_values)
            if value is not None:
                computed_impulses[emotion] = value

    partner_event = {}
    for event in _as_list(stressor_data.get("events")):
        if not isinstance(event, dict):
            continue
        if event.get("id") == "partner_death":
            partner_event = event
            break

    base_instant = _as_float(partner_event.get("base_instant"), 450.0)
    base_per_tick = _as_float(partner_event.get("base_per_tick"), 10.0)
    base_decay = _as_float(partner_event.get("base_decay_rate"), 0.01)
    is_loss = bool(partner_event.get("is_loss", True))

    severity_raw = base_instant
    if base_decay > 0:
        severity_raw += (base_per_tick / base_decay) * 10.0

    loss_multiplier = 2.5 if is_loss else 1.0
    severity_loss = severity_raw * loss_multiplier

    e_weight = 0.4
    for mod in _as_list(partner_event.get("axis_modifiers")):
        if not isinstance(mod, dict):
            continue
        if mod.get("axis") == "E":
            e_weight = _as_float(mod.get("weight"), 0.4)
            break
    personality_mult = 1.0 + e_weight
    severity_personality = severity_loss * personality_mult

    stress_weights = _as_dict(_as_dict(decay_config.get("stress")).get("weights"))
    fast_effects = _as_dict(partner_event.get("fast_layer_effects"))
    weighted_emotion_stress = 0.0
    for emotion, weight in stress_weights.items():
        weighted_emotion_stress += _as_float(weight, 0.0) * _as_float(fast_effects.get(emotion), 0.0)

    allostatic_proxy = severity_personality / 10_000.0

    siler_params = _extract_mortality_baseline(sections)
    survival_base = _ten_year_survival(35.0, siler_params, 1.0)
    survival_stress = _ten_year_survival(35.0, siler_params, 1.6)

    reference_stats = _as_dict(references.get("stats"))
    cross_flows = _as_int(reference_stats.get("total_cross_system_calls"), 0) + _as_int(
        reference_stats.get("total_signal_connections"),
        0,
    )
    if cross_flows <= 0:
        cross_flows = 5
        warnings.append("references.stats flow counts missing; using fallback cross-system flow count")

    relevant_system_fields: set[str] = set()
    for system in (trait_system, emotion_system, stress_system, mortality_system):
        for field in _as_list(system.get("entity_fields")):
            if isinstance(field, str) and field.strip():
                relevant_system_fields.add(field)

    stage1_models = "Ashton & Lee (2007) HEXACO"
    stage2_models = "Plutchik (1980), Lazarus (1991), Scherer (2009)"
    stage3_models = "Lazarus (1984), Selye (1956), McEwen (1998), Hobfoll (1989)"
    stage4_models = "Siler (1979)"

    source_files: list[str] = []

    for path in (
        "scripts/systems/personality_generator.gd",
        "scripts/systems/personality_maturation.gd",
        "scripts/systems/trait_system.gd",
        "scripts/systems/emotion_system.gd",
        "scripts/systems/stress_system.gd",
        "scripts/systems/mortality_system.gd",
    ):
        if _find_system_by_file(systems_list, path):
            source_files.append(path)

    for key in ("source_file",):
        for section_key in ("trait_data", "stressor_data", "emotion_presets", "decay_config"):
            src = sections[section_key].get(key)
            if isinstance(src, str) and src not in source_files:
                source_files.append(src)

    data_files = sections.get("data_files", {})
    for file_entry in _as_list(data_files.get("files")):
        if not isinstance(file_entry, dict):
            continue
        if file_entry.get("file") == "data/species/human/mortality/siler_parameters.json":
            source_files.append("data/species/human/mortality/siler_parameters.json")
            break

    deduped_sources: list[str] = []
    seen_sources: set[str] = set()
    for source in source_files:
        if source in seen_sources:
            continue
        seen_sources.add(source)
        deduped_sources.append(source)

    axis_effects = {
        "H": "Social behavior, corruption resistance",
        "E": "Emotion sensitivity, fear/sadness amplification",
        "X": "Joy/social baselines, stress recovery",
        "A": "Trust, conflict avoidance",
        "C": "Work quality, stress from disorder",
        "O": "Novelty response, adaptability",
    }

    lines: list[str] = [
        "---",
        f"title: {_yaml_quote('System Pipeline')}",
        f"description: {_yaml_quote('Master personality-emotion-stress-mortality pipeline reference')}",
        "generated: true",
        "source_files:",
    ]
    for source in deduped_sources:
        lines.append(f"  - {_yaml_quote(source)}")
    lines.extend(
        [
            "nav_order: 1",
            "---",
            "",
            "# The WorldSim Pipeline: Personality → Emotion → Stress → Mortality",
            "",
            "## 개요 / Overview",
            "",
            "WorldSim simulates a complete psychophysiological pipeline for each entity:",
            "",
            "1. **Personality** (static): HEXACO axes + discrete traits define individual differences",
            "2. **Emotion** (fast): Events trigger emotions via Lazarus appraisal, modulated by personality",
            "3. **Stress** (medium): Emotions, needs, and stressors accumulate stress, modulated by personality",
            "4. **Mortality** (slow): Chronic stress (allostatic load) increases death risk via Siler hazard model",
            "",
            "```mermaid",
            "graph TD",
            "    subgraph \"Layer 1: Personality (Static)\"",
            "        HEX[HEXACO 6 Axes<br/>24 Facets] --> TRAITS[Discrete Traits<br/>~85 traits]",
            "    end",
            "",
            "    subgraph \"Layer 2: Emotion (Fast)\"",
            "        EVT[Game Events] --> APR[Appraisal<br/>8 dimensions]",
            "        APR --> IMP[Impulse Calculation<br/>8 Plutchik emotions]",
            "        IMP --> FAST[Fast Layer<br/>exponential decay]",
            "        FAST --> SLOW[Slow Layer<br/>O-U mean reversion]",
            "        SLOW --> MEM[Memory Traces<br/>long-term storage]",
            "    end",
            "",
            "    subgraph \"Layer 3: Stress (Medium)\"",
            "        CONT[Continuous Stressors<br/>hunger, energy, social] --> STR[Stress Accumulation]",
            "        EMSTR[Emotion Contribution<br/>VA-weighted] --> STR",
            "        STR --> REC[Recovery<br/>sleep, safety, support]",
            "        REC --> ALLO[Allostatic Load<br/>chronic wear]",
            "        ALLO --> GAS[GAS Stage<br/>alarm→resist→exhaust]",
            "    end",
            "",
            "    subgraph \"Layer 4: Mortality (Slow)\"",
            "        SILER[Siler Hazard<br/>μ(x) bathtub curve] --> DEATH[Death Probability<br/>per tick]",
            "    end",
            "",
            "    HEX -->|sensitivity| IMP",
            "    HEX -->|baselines| SLOW",
            "    TRAITS -->|emotion modifiers| IMP",
            "    TRAITS -->|stress modifiers| STR",
            "    FAST -->|emotion values| EMSTR",
            "    ALLO -->|load factor| SILER",
            "    DEATH -->|death event| EVT",
            "```",
            "",
            "## Stage 1: Personality (Static Foundation) / 성격 (정적 기반)",
            "",
            f"**Model**: {stage1_models}",
            "**Computation**: Once at entity creation + yearly maturation",
            "**Output**: 6 axis z-scores, 24 facet scores, set of active traits",
            "",
            "The HEXACO model provides 6 orthogonal personality axes:",
            "",
            "| Axis | Name | Key Effect |",
            "|------|------|-----------|",
        ]
    )

    for axis in ("H", "E", "X", "A", "C", "O"):
        axis_name = _as_dict(axis_data.get(axis)).get("name")
        if not isinstance(axis_name, str) or not axis_name.strip():
            axis_name = axis
        lines.append(f"| {axis} | {axis_name} | {axis_effects.get(axis, '-')} |")

    lines.extend(
        [
            "",
            "Traits activate when facet scores exceed thresholds "
            "(e.g., `H_sincerity > 0.92` → \"Sincere\" trait).",
            "",
            _source_ref("scripts/systems/personality_generator.gd", _function_line(personality_gen, "init")),
            _source_ref("scripts/systems/personality_maturation.gd", _function_line(personality_maturation, "apply_maturation")),
            _source_ref("scripts/systems/trait_system.gd", _function_line(trait_system, "check_traits")),
            _source_ref(str(trait_data.get("source_file", "data/species/human/personality/trait_definitions.json"))),
            "",
            "---",
            "",
            "## Stage 2: Emotion (Fast Response) / 감정 (빠른 반응)",
            "",
            f"**Models**: {stage2_models}",
            f"**Tick interval**: {emotion_tick_interval} ticks",
            "",
            "### Input / 입력",
            "- Game events with appraisal vectors (8 dimensions)",
            "- Personality sensitivity multipliers",
            "- Trait emotion modifiers",
            "",
            "### Computation / 계산",
            "1. **Appraisal**: emotion impulses from appraisal dimensions",
            "",
            "| Emotion | Formula |",
            "|---------|---------|",
        ]
    )

    for emotion in formula_order:
        formula = impulse_formulas.get(emotion)
        if isinstance(formula, str) and formula.strip():
            lines.append(f"| {emotion} | `{formula}` |")

    lines.extend(
        [
            "",
            "2. **Personality scaling**: `impulse *= exp(coeff * z_axis)`",
            "3. **Fast decay**: `fast *= exp(-λ * dt)` then add impulse",
            "4. **Slow update**: O-U process: `dslow = θ(μ - slow)dt + σdW`",
            "5. **Inhibition**: opposite pair suppression at γ = "
            f"{_fmt_num(_as_float(_as_dict(decay_config.get('inhibition')).get('gamma'), 0.3), 2)}",
            "6. **Contagion**: spatial spread with κ coefficients",
            "",
            "### Output / 출력",
            "- 8 emotion values (0-100 each)",
            "- Valence-arousal coordinates",
            "- Mental break trigger probability update",
            "",
            _source_ref("scripts/systems/emotion_system.gd", _function_line(emotion_system, "execute_tick")),
            _source_ref(str(emotion_presets.get("source_file", "data/emotions/event_presets.json"))),
            _source_ref(str(decay_config.get("source_file", "data/species/human/emotions/decay_parameters.json"))),
            "",
            "---",
            "",
            "## Stage 3: Stress (Medium Accumulation) / 스트레스 (중간 축적)",
            "",
            f"**Models**: {stage3_models}",
            f"**Tick interval**: {stress_tick_interval} ticks",
            "",
            "### Input / 입력",
            "- Emotion values (from Stage 2)",
            "- Continuous need states (hunger, energy, social)",
            "- Stressor events",
            "- Personality modifiers",
            "",
            "### Computation / 계산",
            "1. **Emotion contribution**: `stress += γ_VA * Σ(w_e * emotion_e)`",
            "2. **Continuous stressors**: hunger/energy/social deficit → stress",
            "3. **Event stressors**: `severity = base_instant + per_tick/decay * 10; if loss: × 2.5`",
            "4. **Recovery**: `recovery = base * (1 + sleep + safe + support) * resilience`",
            "5. **Allostatic load**: chronic accumulation when stress exceeds reserve",
            "6. **GAS stages**: alarm → resistance → exhaustion",
            "",
            "### Output / 출력",
            "- Current stress level (0-100)",
            "- Allostatic load (0-100)",
            "- GAS stage (alarm/resistance/exhaustion)",
            "- Yerkes-Dodson efficiency multiplier",
            "",
            _source_ref("scripts/systems/stress_system.gd", _function_line(stress_system, "_update_entity_stress")),
            _source_ref("scripts/systems/stress_system.gd", _function_line(stress_system, "_calc_emotion_contribution")),
            _source_ref(str(stressor_data.get("source_file", "data/stressor_events.json"))),
            "",
            "---",
            "",
            "## Stage 4: Mortality (Slow Selection) / 사망 (느린 선택)",
            "",
            f"**Model**: {stage4_models}",
            f"**Tick interval**: {mortality_tick_interval} ticks",
            "",
            "### Input / 입력",
            "- Entity age",
            "- Allostatic load (from Stage 3)",
            "- Tech level, nutrition, care status, season",
            "",
            "### Computation / 계산",
            "$$",
            r"\mu(x) = a_1 e^{-b_1 x} + a_2 + a_3 e^{b_3 x}",
            "$$",
            "Modified by: tech × care × season × stress × nutrition",
            "",
            "$$",
            r"P(\text{death}) = 1 - e^{-\mu_{\text{final}}(x) / \text{TICKS\_PER\_YEAR}}",
            "$$",
            "",
            "### Output / 출력",
            "- Death probability per tick",
            "- Death event (triggers bereavement stressors on survivors)",
            "",
            _source_ref("scripts/systems/mortality_system.gd", _function_line(mortality_system, "_do_mortality_check")),
            _source_ref("scripts/systems/mortality_system.gd", _function_line(mortality_system, "_inject_bereavement_stress")),
            _source_ref("data/species/human/mortality/siler_parameters.json"),
            "",
            "## Feedback Loops / 피드백 루프",
            "",
            "### Bereavement Cascade / 애도 연쇄",
            "```mermaid",
            "graph LR",
            "    DEATH[Entity Death] -->|bereavement stressor| STRESS[Survivor Stress]",
            "    STRESS -->|allostatic load| MORT[Survivor Mortality ↑]",
            "    MORT -->|more deaths| DEATH",
            "```",
            "",
            "### Mental Break Loop / 정신 붕괴 루프",
            "```mermaid",
            "graph LR",
            "    STRESS[High Stress] -->|threshold exceeded| BREAK[Mental Break]",
            "    BREAK -->|emotion injection| EMOT[Negative Emotions ↑]",
            "    EMOT -->|emotion contribution| STRESS",
            "```",
            "",
            "## Example: Entity Loses Partner / 예시: 동반자 상실",
            "",
            "**Event**: `partner_death` (intensity=95, is_trauma=true, is_loss=true)",
            "",
            "### Stage 2: Emotion",
            "- Appraisal: g=-0.9, n=0.3, c=0.1, a=-0.8, b=-0.7, fr=0.4",
            "- Impulses (computed): "
            f"sadness={_fmt_num(computed_impulses.get('sadness', 0.0))}, "
            f"fear={_fmt_num(computed_impulses.get('fear', 0.0))}, "
            f"anger={_fmt_num(computed_impulses.get('anger', 0.0))}, trust impulse={_fmt_num(computed_impulses.get('trust', 0.0))}",
            "- Fast layer: sadness_fast += "
            f"{_fmt_num(_as_float(fast_effects.get('sadness'), 80.0))}, "
            f"fear_fast += {_fmt_num(_as_float(fast_effects.get('fear'), 30.0))}, "
            f"anger_fast += {_fmt_num(_as_float(fast_effects.get('anger'), 20.0))}",
            "- Slow layer: trust_slow -= "
            f"{_fmt_num(abs(_as_float(_as_dict(partner_event.get('slow_layer_effects')).get('trust'), -25.0)))}, "
            f"joy_slow -= {_fmt_num(abs(_as_float(_as_dict(partner_event.get('slow_layer_effects')).get('joy'), -40.0)))}",
            "- Memory trace created (trauma half-life: "
            f"{_fmt_num(_as_float(_as_dict(decay_config.get('memory_traces')).get('trauma_half_life_days'), 365.0))} days)",
            "",
            "### Stage 3: Stress",
            f"- Base instant: {_fmt_num(base_instant)}",
            f"- Event severity: {_fmt_num(base_instant)} + ({_fmt_num(base_per_tick)} / {_fmt_num(base_decay)}) * 10 = {_fmt_num(severity_raw)}",
            f"- COR loss aversion: × { _fmt_num(loss_multiplier, 1) } → severity {_fmt_num(severity_loss)}",
            f"- Personality modifier (high E_axis): × {_fmt_num(personality_mult, 2)} → {_fmt_num(severity_personality)}",
            f"- Emotion contribution proxy: Σ(w_e * fast_e) = {_fmt_num(weighted_emotion_stress)}",
            "- Recovery slowed: grief state degrades sleep/support recovery factors",
            "",
            "### Stage 4: Mortality",
            f"- Allostatic load proxy increases by ~{_fmt_num(allostatic_proxy)} per stress tick (severity-normalized)",
            "- At allostatic_load=60: mortality hazard ×1.6",
            f"- 10-year survival (age 35, baseline Siler params): {_fmt_num(survival_base * 100.0, 1)}% → {_fmt_num(survival_stress * 100.0, 1)}%",
            "",
            "## Pipeline Statistics / 파이프라인 통계",
            "",
            "| Metric | Value |",
            "|--------|-------|",
            "| Total systems in pipeline | 4 |",
            f"| Total formulas | {len(formulas_all)} |",
            f"| Academic models referenced | {len(models_all)} |",
            f"| Entity data fields | {len(relevant_system_fields)} |",
            f"| Cross-system data flows | {cross_flows} |",
            "| Feedback loops | 2 |",
            "",
            f"- Personality coverage: {axis_count} HEXACO axes, {trait_count} discovered traits",
            "",
            _MANUAL_START,
            "",
            _MANUAL_END,
            "",
        ]
    )

    return "\n".join(lines)


def run(manifest: dict, extracted: dict) -> dict:
    """Generate master pipeline documentation page.

    Args:
        manifest: The manifest.json data from Phase 1.
        extracted: Aggregated extracted data payload containing systems/formulas/references
            and specialized extraction outputs.

    Returns:
        dict with keys:
            - files_written: list[str]
            - pages_generated: int
            - warnings: list[str]
            - errors: list[str]
    """
    warnings: list[str] = []
    errors: list[str] = []

    if not isinstance(manifest, dict):
        warnings.append("Manifest is not a dict; continuing with empty manifest")
        manifest = {}

    if not isinstance(extracted, dict):
        errors.append("Extracted payload is not a dict")
        return {
            "files_written": [],
            "pages_generated": 0,
            "items_processed": 0,
            "warnings": warnings,
            "errors": errors,
        }

    sections = _extract_sections(extracted, warnings)

    try:
        markdown = _build_markdown(manifest, sections, warnings)
    except Exception as exc:  # pragma: no cover - defensive safety for pipeline
        errors.append(f"Failed to build pipeline page markdown: {exc}")
        return {
            "files_written": [],
            "pages_generated": 0,
            "items_processed": 0,
            "warnings": warnings,
            "errors": errors,
        }

    output_path = os.path.join(config.CONTENT_KO, "pipeline.md")
    config.ensure_dir(config.CONTENT_KO)

    try:
        if os.path.exists(output_path):
            with open(output_path, "r", encoding="utf-8") as f:
                existing = f.read()
            markdown = _preserve_manual_block(markdown, existing)

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(markdown)
    except OSError as exc:
        errors.append(f"Failed to write pipeline page: {exc}")
        return {
            "files_written": [],
            "pages_generated": 0,
            "items_processed": 0,
            "warnings": warnings,
            "errors": errors,
        }

    return {
        "files_written": [output_path],
        "pages_generated": 1,
        "items_processed": 1,
        "warnings": warnings,
        "errors": errors,
    }
