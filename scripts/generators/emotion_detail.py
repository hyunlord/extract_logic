"""Generate detailed emotion-system documentation from extracted artifacts."""

from __future__ import annotations

import math
import os
import re
from typing import Any

import scripts.config as config


_MANUAL_BLOCK_RE = re.compile(r"<!-- MANUAL:START -->.*?<!-- MANUAL:END -->", re.DOTALL)

_BASE_MODEL_REFERENCES = [
    "**Plutchik (1980, 2001)**: 8 basic emotions, opposite pairs, intensity levels",
    "**Lazarus (1991)**: Appraisal theory — events evaluated on 8 dimensions",
    "**Scherer (2009)**: Component Process Model — appraisal to impulse mapping",
    "**Verduyn & Brans (2012)**: Emotion duration research (half-life values)",
    "**Uhlenbeck & Ornstein (1930)**: Stochastic mean-reversion process (slow layer)",
]


def _as_dict(value: Any) -> dict[str, Any]:
    return value if isinstance(value, dict) else {}


def _as_list(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def _as_float(value: Any) -> float | None:
    if isinstance(value, bool):
        return None
    if isinstance(value, (int, float)):
        return float(value)
    return None


def _yaml_quote(value: str) -> str:
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def _md_cell(value: Any) -> str:
    text = str(value)
    return text.replace("|", r"\|").replace("\n", " ")


def _title_case(token: str) -> str:
    return token.replace("_", " ").strip().title()


def _fmt_number(value: Any, decimals: int = 3) -> str:
    numeric = _as_float(value)
    if numeric is None:
        return "n/a"
    if float(int(numeric)) == numeric:
        return str(int(numeric))
    rendered = f"{numeric:.{decimals}f}"
    rendered = rendered.rstrip("0").rstrip(".")
    return rendered if rendered else "0"


def _first_sentence(text: Any) -> str:
    if not isinstance(text, str):
        return ""
    cleaned = " ".join(text.split()).strip()
    if not cleaned:
        return ""
    parts = re.split(r"(?<=[.!?])\s+", cleaned, maxsplit=1)
    return parts[0].strip()


def _merge_manual_blocks(generated: str, existing: str) -> str:
    existing_match = _MANUAL_BLOCK_RE.search(existing)
    if not existing_match:
        return generated
    if _MANUAL_BLOCK_RE.search(generated):
        return _MANUAL_BLOCK_RE.sub(existing_match.group(0), generated, count=1)
    return generated.rstrip() + "\n\n" + existing_match.group(0) + "\n"


def _format_source(path: str, line: int | None = None) -> str:
    if not path:
        return ""
    if isinstance(line, int) and line > 0:
        return f"`{path}:L{line}`"
    return f"`{path}`"


def _find_emotion_system(manifest: dict[str, Any], extracted_systems: dict[str, Any]) -> dict[str, Any]:
    candidates: list[dict[str, Any]] = []
    for entry in _as_list(extracted_systems.get("systems")):
        if isinstance(entry, dict):
            candidates.append(entry)
    for entry in _as_list(manifest.get("systems")):
        if isinstance(entry, dict):
            candidates.append(entry)

    for entry in candidates:
        rel_file = str(entry.get("file", ""))
        system_name = str(entry.get("system_name", "")).strip().lower()
        if "emotion_system" in rel_file or system_name in {"emotion", "emotions", "emotion_system"}:
            return entry
    return {}


def _find_function_line(system_entry: dict[str, Any], function_name: str) -> int | None:
    for fn in _as_list(system_entry.get("functions")):
        if not isinstance(fn, dict):
            continue
        if str(fn.get("name", "")) == function_name:
            line = fn.get("line")
            if isinstance(line, int) and line > 0:
                return line
    return None


def _emotion_order(decay_config: dict[str, Any], emotion_presets: dict[str, Any]) -> list[str]:
    ordered: list[str] = []
    seen: set[str] = set()

    def add(name: Any) -> None:
        if not isinstance(name, str):
            return
        if not name:
            return
        if name in seen:
            return
        seen.add(name)
        ordered.append(name)

    for container in (
        _as_dict(_as_dict(decay_config.get("fast_decay")).get("emotions")),
        _as_dict(_as_dict(decay_config.get("slow_decay")).get("emotions")),
        _as_dict(_as_dict(decay_config.get("contagion")).get("kappa")),
        _as_dict(_as_dict(decay_config.get("opposite_pairs")).get("bidirectional_map")),
        _as_dict(emotion_presets.get("impulse_formulas")),
    ):
        for key in container.keys():
            add(key)

    for pair in _as_list(_as_dict(decay_config.get("opposite_pairs")).get("pairs")):
        if isinstance(pair, list) and len(pair) == 2:
            add(pair[0])
            add(pair[1])

    return ordered


def _formula_interpretation(formula: str) -> str:
    parts: list[str] = []
    if "max(g, 0)" in formula:
        parts.append("positive goal congruence")
    if "max(-g, 0)" in formula:
        parts.append("negative goal congruence")
    if "(1 - c)" in formula:
        parts.append("low controllability")
    if "max(-a, 0)" in formula:
        parts.append("external agency/blame")
    if "max(m + p, 0)" in formula:
        parts.append("norm/pathogen threat")
    if "max(b, 0)" in formula:
        parts.append("positive social bond")
    if re.search(r"\bfr\b", formula):
        parts.append("future relevance")
    if re.search(r"\bn\b", formula):
        parts.append("novelty")
    if not parts:
        return "Intensity-scaled appraisal response."
    return "Intensity-scaled " + ", ".join(parts) + "."


def _model_references(
    decay_config: dict[str, Any],
    emotion_presets: dict[str, Any],
    formulas: dict[str, Any],
) -> list[str]:
    refs: list[str] = []
    seen: set[str] = set()

    for base in _BASE_MODEL_REFERENCES:
        if base not in seen:
            seen.add(base)
            refs.append(base)

    for mapping in (
        _as_dict(decay_config.get("model_references")),
        _as_dict(emotion_presets.get("model_references")),
    ):
        for value in mapping.values():
            if isinstance(value, str):
                cleaned = " ".join(value.split()).strip()
                if cleaned and cleaned not in seen:
                    seen.add(cleaned)
                    refs.append(cleaned)

    for formula in _as_list(formulas.get("formulas")):
        if not isinstance(formula, dict):
            continue
        model_ref = _as_dict(formula.get("model_ref"))
        name = str(model_ref.get("name", "")).strip()
        reference = str(model_ref.get("reference", "")).strip()
        rendered = " — ".join(part for part in (name, reference) if part)
        if rendered and rendered not in seen:
            seen.add(rendered)
            refs.append(rendered)

    return refs


def _render_markdown(manifest: dict[str, Any], extracted: dict[str, Any], warnings: list[str]) -> str:
    emotion_presets = _as_dict(extracted.get("emotion_presets"))
    decay_config = _as_dict(extracted.get("decay_config"))
    formulas = _as_dict(extracted.get("formulas"))
    systems_payload = _as_dict(extracted.get("systems"))

    if not emotion_presets:
        warnings.append("missing extracted.emotion_presets; sections will be partially empty")
    if not decay_config:
        warnings.append("missing extracted.decay_config; sections will be partially empty")
    if not systems_payload:
        warnings.append("missing extracted.systems; source metadata may be incomplete")

    system_entry = _find_emotion_system(manifest, systems_payload)
    system_source = str(system_entry.get("file", "")).strip()
    if not system_source:
        system_source = "scripts/systems/emotion_system.gd"
        warnings.append("emotion system metadata not found; using default source path")

    source_files: list[str] = []
    for source in (
        system_source,
        str(decay_config.get("source_file", "")).strip(),
        str(emotion_presets.get("source_file", "")).strip(),
        str(formulas.get("source_file", "")).strip(),
    ):
        if source and source not in source_files:
            source_files.append(source)

    if not source_files:
        source_files = ["scripts/systems/emotion_system.gd"]

    nav_order = 33
    priority = system_entry.get("priority")
    if isinstance(priority, int):
        nav_order = priority + 1

    fast_decay = _as_dict(_as_dict(decay_config.get("fast_decay")).get("emotions"))
    slow_decay = _as_dict(_as_dict(decay_config.get("slow_decay")).get("emotions"))
    opposite_pairs = _as_dict(decay_config.get("opposite_pairs"))
    opposite_map = _as_dict(opposite_pairs.get("bidirectional_map"))
    pair_list = _as_list(opposite_pairs.get("pairs"))
    contagion = _as_dict(decay_config.get("contagion"))
    contagion_kappa = _as_dict(contagion.get("kappa"))
    baselines = _as_dict(_as_dict(decay_config.get("baselines")).get("emotions"))
    personality_coupling = _as_dict(_as_dict(decay_config.get("personality_coupling")).get("emotions"))
    memory_traces = _as_dict(decay_config.get("memory_traces"))
    mental_break = _as_dict(decay_config.get("mental_break"))
    appraisal_dimensions = _as_list(emotion_presets.get("appraisal_dimensions"))
    impulse_formulas = _as_dict(emotion_presets.get("impulse_formulas"))
    presets = _as_list(emotion_presets.get("presets"))

    emotions = _emotion_order(decay_config, emotion_presets)
    model_refs = _model_references(decay_config, emotion_presets, formulas)

    execute_tick_line = _find_function_line(system_entry, "execute_tick")
    impulse_line = _find_function_line(system_entry, "_calculate_event_impulse")
    contagion_line = _find_function_line(system_entry, "_apply_contagion_settlement")
    mental_break_line = _find_function_line(system_entry, "_check_mental_break")
    memory_trace_line = _find_function_line(system_entry, "_create_memory_trace")

    lines: list[str] = [
        "---",
            'title: "Emotion System — Detailed Documentation"',
            'description: "Detailed 3-layer emotion dynamics, appraisal pipeline, contagion, and mental break mechanics"',
        "generated: true",
        "source_files:",
    ]
    for source_file in source_files:
        lines.append(f"  - {_yaml_quote(source_file)}")
    lines.extend(
        [
            f"nav_order: {nav_order}",
            "---",
            "",
            "# Emotion System — Detailed Documentation",
            "",
            "Localization: 한국어 / English",
            "",
            "## Architecture",
            "",
            "The emotion system implements **Plutchik's 8 basic emotions** with a **3-layer temporal model**:",
            "",
            "| Layer | Role | Dynamics | Time Scale |",
            "|-------|------|----------|------------|",
            "| **Fast** | Episodic reactions | Exponential decay | Minutes to hours |",
            "| **Slow** | Mood / baseline | Ornstein-Uhlenbeck mean reversion | Days to weeks |",
            "| **Memory Traces** | Emotional memories | Very slow decay, trauma-persistent | Weeks to years |",
            "",
            "The combined emotion value: `emotion = clamp(fast + slow + memory_traces, 0, 100)`",
            "",
            f"📄 source: {_format_source(system_source, execute_tick_line)}",
            "",
            "### Academic Models",
        ]
    )
    if model_refs:
        for model_ref in model_refs:
            lines.append(f"- {model_ref}")
    else:
        lines.append("- Model references not available in extracted data.")
    lines.append("")

    lines.extend(
        [
            "## The 8 Basic Emotions",
            "",
            "| Emotion | Opposite | Fast Half-life | Slow Half-life | Contagion κ |",
            "|---------|----------|---------------:|---------------:|------------:|",
        ]
    )
    if emotions:
        for emotion in emotions:
            fast_hl = _as_float(_as_dict(fast_decay.get(emotion)).get("half_life_hours"))
            slow_hl = _as_float(_as_dict(slow_decay.get(emotion)).get("half_life_hours"))
            kappa = _as_float(contagion_kappa.get(emotion))
            opposite = str(opposite_map.get(emotion, "-"))
            lines.append(
                "| "
                + " | ".join(
                    [
                        _md_cell(_title_case(emotion)),
                        _md_cell(_title_case(opposite) if opposite != "-" else "-"),
                        _fmt_number(fast_hl, 3),
                        _fmt_number(slow_hl, 3),
                        _fmt_number(kappa, 3),
                    ]
                )
                + " |"
            )
    else:
        lines.append("| - | - | - | - | - |")
    lines.append("")

    lines.extend(
        [
            "## Fast Layer — Episodic Emotion",
            "",
            "The fast layer responds immediately to events and decays exponentially:",
            "",
            "$$",
            r"\text{fast}(t+1) = \text{fast}(t) \cdot e^{-\lambda \cdot \Delta t} + \text{impulse}",
            "$$",
            "",
            r"where $\lambda = \ln(2) / \text{half\_life\_hours}$",
            "",
            "### Decay Rates by Emotion",
            "",
            "| Emotion | Half-life (hours) | Decay rate λ |",
            "|---------|------------------:|-------------:|",
        ]
    )
    if emotions:
        for emotion in emotions:
            fast_entry = _as_dict(fast_decay.get(emotion))
            half_life = _as_float(fast_entry.get("half_life_hours"))
            decay_rate = _as_float(fast_entry.get("decay_rate"))
            if decay_rate is None and isinstance(half_life, float) and half_life > 0:
                decay_rate = math.log(2.0) / half_life
            lines.append(
                "| "
                + " | ".join(
                    [
                        _md_cell(_title_case(emotion)),
                        _fmt_number(half_life, 3),
                        _fmt_number(decay_rate, 3),
                    ]
                )
                + " |"
            )
    else:
        lines.append("| - | - | - |")
    lines.append("")
    lines.append(f"📄 source: {_format_source(system_source, execute_tick_line)}")
    lines.append("")

    lines.extend(
        [
            "## Slow Layer — Mood Baseline (Ornstein-Uhlenbeck)",
            "",
            "The slow layer models mood as a mean-reverting stochastic process:",
            "",
            "$$",
            r"d\text{slow} = \theta \cdot (\mu - \text{slow}) \cdot dt + \sigma \cdot dW",
            "$$",
            "",
            "Where:",
            r"- $\theta$: mean-reversion speed (derived from slow half-life)",
            r"- $\mu$: personality-derived baseline",
            r"- $\sigma$: noise amplitude",
            r"- $dW$: Wiener process increment",
            "",
            "### Personality Baselines",
            "",
            "Each emotion's slow baseline is derived from HEXACO personality:",
            "",
            "$$",
            r"\text{baseline} = \text{clamp}(\text{base} + \text{scale} \cdot z_{\text{axis}}, \text{min}, \text{max})",
            "$$",
            "",
            "| Emotion | Base | Scale | Axis | Min | Max |",
            "|---------|-----:|------:|------|----:|----:|",
        ]
    )
    if emotions:
        for emotion in emotions:
            baseline = _as_dict(baselines.get(emotion))
            lines.append(
                "| "
                + " | ".join(
                    [
                        _md_cell(_title_case(emotion)),
                        _fmt_number(baseline.get("base"), 3),
                        _fmt_number(baseline.get("scale"), 3),
                        _md_cell(baseline.get("axis", "-")),
                        _fmt_number(baseline.get("min"), 3),
                        _fmt_number(baseline.get("max"), 3),
                    ]
                )
                + " |"
            )
    else:
        lines.append("| - | - | - | - | - | - |")
    lines.append("")
    lines.append(f"📄 source: {_format_source(system_source, execute_tick_line)}")
    lines.append("")

    memory_threshold = _as_float(memory_traces.get("threshold"))
    trace_ratio = _as_float(memory_traces.get("trace_ratio"))
    normal_days = _as_float(memory_traces.get("default_half_life_days"))
    trauma_days = _as_float(memory_traces.get("trauma_half_life_days"))
    lines.extend(
        [
            "## Memory Traces — Long-term Emotional Memory",
            "",
            f"When a fast emotion exceeds the **memory trace threshold** ({_fmt_number(memory_threshold, 2)}),",
            f"a fraction ({_fmt_number(trace_ratio, 2)}) is stored as a memory trace with very slow decay.",
            "",
            f"- **Normal memories**: half-life = {_fmt_number(normal_days, 2)} days",
            f"- **Trauma memories**: half-life = {_fmt_number(trauma_days, 2)} days (for events with `is_trauma: true`)",
            "",
            f"📄 source: {_format_source(system_source, memory_trace_line)}",
            "",
            "## Event → Emotion Pipeline",
            "",
            "```mermaid",
            "flowchart TD",
            "    A[Event] --> B[8D Appraisal Vector]",
            "    B --> C[Impulse Formulas]",
            "    C --> D[Personality Sensitivity Scaling]",
            "    D --> E[Fast Layer Update]",
            "    E --> F[Slow Layer Mean Reversion]",
            "    E --> G[Memory Trace Creation]",
            "    E --> H[Opposite Emotion Inhibition]",
            "    E --> I[Settlement Contagion]",
            "    F --> J[Final Emotion Clamp 0-100]",
            "    G --> J",
            "```",
            "",
            "### Step 1: Event Appraisal",
            "",
            "Each event has an 8-dimensional appraisal vector:",
            "",
            "| Dimension | Symbol | Range | Meaning |",
            "|-----------|--------|-------|---------|",
        ]
    )
    if appraisal_dimensions:
        for dimension in appraisal_dimensions:
            if not isinstance(dimension, dict):
                continue
            lines.append(
                "| "
                + " | ".join(
                    [
                        _md_cell(_title_case(str(dimension.get("id", "-")))),
                        _md_cell(dimension.get("abbrev", "-")),
                        _md_cell(dimension.get("range", "-")),
                        _md_cell(dimension.get("description", "-")),
                    ]
                )
                + " |"
            )
    else:
        lines.append("| - | - | - | - |")
    lines.append("")

    lines.extend(
        [
            "### Step 2: Impulse Calculation",
            "",
            "Appraisal dimensions map to Plutchik emotions via these formulas:",
            "",
            "| Emotion | Formula | Interpretation |",
            "|---------|---------|----------------|",
        ]
    )
    if impulse_formulas:
        remaining = [name for name in impulse_formulas.keys() if isinstance(name, str) and name not in emotions]
        formula_order = emotions + sorted(remaining)
        for emotion in formula_order:
            if emotion not in impulse_formulas:
                continue
            formula = str(impulse_formulas.get(emotion, "")).strip()
            lines.append(
                "| "
                + " | ".join(
                    [
                        _md_cell(_title_case(emotion)),
                        f"`{_md_cell(formula)}`",
                        _md_cell(_formula_interpretation(formula)),
                    ]
                )
                + " |"
            )
    else:
        lines.append("| - | - | - |")
    lines.extend(
        [
            "",
            "where `I = intensity / 100`",
            "",
            "### Step 3: Personality Sensitivity",
            "",
            "Each emotion's impulse is scaled by HEXACO personality:",
            "",
            "$$",
            r"\text{sensitivity} = e^{\text{coeff} \cdot z_{\text{axis}}}",
            "$$",
            "",
            "| Emotion | Couplings |",
            "|---------|-----------|",
        ]
    )
    if emotions:
        for emotion in emotions:
            coupling_cfg = _as_dict(personality_coupling.get(emotion))
            coupling_rows = []
            for coupling in _as_list(coupling_cfg.get("couplings")):
                if not isinstance(coupling, dict):
                    continue
                axis = str(coupling.get("axis", "")).strip()
                coeff = _fmt_number(coupling.get("coeff"), 3)
                if axis:
                    coupling_rows.append(f"{axis}: {coeff}")
            lines.append(
                f"| {_md_cell(_title_case(emotion))} | {_md_cell(', '.join(coupling_rows) if coupling_rows else '-')} |"
            )
    else:
        lines.append("| - | - |")
    lines.append("")
    lines.append(f"📄 source: {_format_source(system_source, impulse_line)}")
    lines.append("")

    gamma = _as_float(_as_dict(decay_config.get("inhibition")).get("gamma"))
    if gamma is None:
        gamma = _as_float(opposite_pairs.get("inhibition_gamma"))
    lines.extend(
        [
            "## Opposite Emotion Inhibition",
            "",
            f"When one emotion rises by delta, its opposite is suppressed by γ·delta where γ = {_fmt_number(gamma, 3)}.",
            "",
            "| Emotion | Opposite | Inhibition |",
            "|---------|----------|------------|",
        ]
    )
    added_pair = False
    for pair in pair_list:
        if not isinstance(pair, list) or len(pair) != 2:
            continue
        left = str(pair[0]).strip()
        right = str(pair[1]).strip()
        if not left or not right:
            continue
        added_pair = True
        lines.append(
            f"| {_md_cell(_title_case(left))} ↑ | {_md_cell(_title_case(right))} ↓ | -{_fmt_number(gamma, 3)} * delta |"
        )
    if not added_pair:
        lines.append("| - | - | - |")
    lines.append("")
    lines.append(f"📄 source: {_format_source(system_source, execute_tick_line)}")
    lines.append("")

    distance_scale = _as_float(contagion.get("distance_scale"))
    min_source = _as_float(contagion.get("min_source"))
    highest_contagion_name = ""
    highest_contagion_value = None
    anger_kappa = _as_float(contagion_kappa.get("anger"))
    for emotion_name, value in contagion_kappa.items():
        numeric = _as_float(value)
        if numeric is None:
            continue
        if highest_contagion_value is None or numeric > highest_contagion_value:
            highest_contagion_name = str(emotion_name)
            highest_contagion_value = numeric

    lines.extend(
        [
            "## Emotional Contagion",
            "",
            "Emotions spread between nearby entities in a settlement:",
            "",
            "$$",
            r"\text{contagion} = \kappa_e \cdot \text{source\_intensity} \cdot e^{-d / d_{\text{scale}}}",
            "$$",
            "",
            r"- $\kappa_e$: per-emotion contagion coefficient",
            r"- $d$: distance between entities",
            f"- $d_{{scale}}$: spatial decay parameter ({_fmt_number(distance_scale, 2)})",
            f"- Minimum source intensity: {_fmt_number(min_source, 2)}",
            "",
        ]
    )
    if anger_kappa is not None and highest_contagion_name == "anger":
        lines.append(
            f"**Anger is the most contagious** (κ={_fmt_number(anger_kappa, 3)}), "
            "consistent with Fan et al. (2016)."
        )
    elif highest_contagion_name and highest_contagion_value is not None:
        lines.append(
            f"**{_title_case(highest_contagion_name)} is the most contagious** "
            f"(κ={_fmt_number(highest_contagion_value, 3)})."
        )
        if anger_kappa is not None:
            warnings.append(
                "contagion data indicates anger is not the highest kappa; "
                "check consistency with Fan et al. (2016) note"
            )
    else:
        lines.append("Most contagious emotion could not be derived from extracted data.")
    lines.append("")
    lines.append(f"📄 source: {_format_source(system_source, contagion_line)}")
    lines.append("")

    tick_prob = _as_float(mental_break.get("tick_prob"))
    beta = _as_float(mental_break.get("beta"))
    threshold = _as_float(mental_break.get("threshold"))
    if threshold is None:
        warnings.append("mental_break.threshold missing in extracted data")

    lines.extend(
        [
            "## Mental Break",
            "",
            "When stress exceeds a threshold, entities may experience a mental break:",
            "",
            "$$",
            r"P(\text{break}) = \frac{\text{tick\_prob}}{1 + e^{-(\text{stress} - \text{threshold}) / \beta}}",
            "$$",
            "",
            f"- tick_prob: {_fmt_number(tick_prob, 4)}",
            f"- beta: {_fmt_number(beta, 3)} (sigmoid steepness)",
            f"- threshold: {_fmt_number(threshold, 3)}",
            "",
            "### Break Types",
            "",
            "| Type | Duration | Energy Drain | Description |",
            "|------|---------:|-------------:|-------------|",
        ]
    )
    behaviors = _as_dict(mental_break.get("behaviors"))
    if behaviors:
        for behavior_name in sorted(behaviors.keys()):
            behavior = _as_dict(behaviors.get(behavior_name))
            lines.append(
                "| "
                + " | ".join(
                    [
                        _md_cell(_title_case(behavior_name)),
                        _fmt_number(behavior.get("duration_hours"), 2) + "h",
                        _fmt_number(behavior.get("energy_drain"), 2),
                        _md_cell(_first_sentence(behavior.get("description")) or "-"),
                    ]
                )
                + " |"
            )
    else:
        lines.append("| - | - | - | - |")
    lines.append("")
    lines.append(f"📄 source: {_format_source(system_source, mental_break_line)}")
    lines.append("")

    lines.extend(
        [
            "## Event Presets",
            "",
            "| Event | Category | Intensity | Primary Emotions | Trauma |",
            "|-------|----------|----------:|------------------|--------|",
        ]
    )
    if presets:
        sorted_presets = sorted(
            (preset for preset in presets if isinstance(preset, dict)),
            key=lambda preset: str(preset.get("id", "")),
        )
        for preset in sorted_presets:
            predicted = _as_dict(preset.get("predicted_emotions"))
            sorted_predicted = sorted(
                (
                    (str(emotion), _as_float(score))
                    for emotion, score in predicted.items()
                    if isinstance(emotion, str)
                ),
                key=lambda item: item[1] if isinstance(item[1], float) else -1.0,
                reverse=True,
            )
            primary = ", ".join(
                f"{_title_case(emotion)} ({_fmt_number(score, 2)})"
                for emotion, score in sorted_predicted
                if isinstance(score, float)
            )
            lines.append(
                "| "
                + " | ".join(
                    [
                        _md_cell(preset.get("id", "-")),
                        _md_cell(preset.get("category", "-")),
                        _fmt_number(preset.get("intensity"), 2),
                        _md_cell(primary or "-"),
                        "Yes" if bool(preset.get("is_trauma")) else "No",
                    ]
                )
                + " |"
            )
    else:
        warnings.append("emotion_presets.presets is empty; generated table with placeholder row")
        lines.append("| - | - | - | - | - |")
    lines.append("")

    preset_source = str(emotion_presets.get("source_file", "")).strip()
    if preset_source:
        lines.append(f"📄 source: {_format_source(preset_source)}")
        lines.append("")

    lines.extend(
        [
            "<!-- MANUAL:START -->",
            "",
            "<!-- MANUAL:END -->",
            "",
        ]
    )

    return "\n".join(lines)


def run(manifest: dict, extracted: dict) -> dict:
    """Generate emotion system detail documentation.

    Args:
        manifest: The manifest.json data from Phase 1.
        extracted: Extracted payloads keyed by extractor name.

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
        warnings.append("manifest is not an object; using empty manifest")
        manifest = {}
    if not isinstance(extracted, dict):
        warnings.append("extracted is not an object; using empty extracted payload")
        extracted = {}

    output_path = os.path.join(config.CONTENT_DIR, "systems", "emotion-detail.md")
    config.ensure_dir(config.CONTENT_SYSTEMS)

    try:
        markdown = _render_markdown(manifest, extracted, warnings)
    except Exception as exc:
        errors.append(f"failed to render emotion detail markdown: {exc}")
        return {
            "files_written": files_written,
            "pages_generated": 0,
            "warnings": warnings,
            "errors": errors,
        }

    existing = ""
    if os.path.exists(output_path):
        try:
            with open(output_path, "r", encoding="utf-8") as handle:
                existing = handle.read()
        except OSError as exc:
            warnings.append(f"failed to read existing markdown for MANUAL merge ({output_path}): {exc}")

    final_text = _merge_manual_blocks(markdown, existing)

    try:
        with open(output_path, "w", encoding="utf-8") as handle:
            handle.write(final_text)
        files_written.append(output_path)
    except OSError as exc:
        errors.append(f"failed to write {output_path}: {exc}")

    return {
        "files_written": files_written,
        "pages_generated": len(files_written),
        "warnings": warnings,
        "errors": errors,
    }
