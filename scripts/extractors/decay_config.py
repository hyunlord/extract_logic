"""Extract emotion decay and coupling parameters from decay_parameters.json."""

from __future__ import annotations

import json
import math
import os
from datetime import datetime, timezone
from typing import Any

import scripts.config as config


SOURCE_HINT = "decay_parameters"
MODEL_REFERENCES = {
    "verduyn_brans_2012": (
        "Verduyn & Brans (2012) — emotion duration research (fast half-lives)"
    ),
    "plutchik_1980": (
        "Plutchik (1980, 2001) — 8 basic emotions, opposite pairs, intensity levels"
    ),
    "russell_1980": "Russell (1980) — Circumplex Model of Affect (Valence-Arousal)",
    "fan_2016": "Fan et al. (2016) — emotional contagion rates (anger > fear > joy)",
    "ashton_lee_2007": "Ashton & Lee (2007) — HEXACO personality model",
}


def _as_number(value: Any) -> float | None:
    if isinstance(value, bool):
        return None
    if isinstance(value, (int, float)):
        return float(value)
    return None


def _extract_decay_rates(
    section: Any,
    section_name: str,
    warnings: list[str],
) -> dict[str, dict[str, float | None]]:
    if not isinstance(section, dict):
        warnings.append(f"{section_name} is missing or not an object")
        return {}

    emotions: dict[str, dict[str, float | None]] = {}
    for emotion, half_life in section.items():
        if emotion == "comment":
            continue
        numeric_half_life = _as_number(half_life)
        if numeric_half_life is None:
            warnings.append(f"{section_name}.{emotion} is not numeric; skipped")
            continue
        decay_rate = None
        if numeric_half_life > 0:
            decay_rate = round(math.log(2) / numeric_half_life, 6)
        else:
            warnings.append(f"{section_name}.{emotion} must be > 0 to compute decay rate")
        emotions[emotion] = {
            "half_life_hours": numeric_half_life,
            "decay_rate": decay_rate,
        }
    return emotions


def _extract_unique_pairs(section: Any, warnings: list[str]) -> tuple[list[list[str]], dict[str, str]]:
    if not isinstance(section, dict):
        warnings.append("opposite_pairs is missing or not an object")
        return [], {}

    pairs: list[list[str]] = []
    bidirectional: dict[str, str] = {}
    seen: set[frozenset[str]] = set()

    for emotion, opposite in section.items():
        if not isinstance(emotion, str) or not emotion:
            warnings.append("opposite_pairs contains a non-string emotion key; skipped")
            continue
        if not isinstance(opposite, str) or not opposite:
            warnings.append(f"opposite_pairs.{emotion} is not a non-empty string; skipped")
            continue

        key = frozenset((emotion, opposite))
        if key not in seen:
            seen.add(key)
            pairs.append([emotion, opposite])

        bidirectional[emotion] = opposite
        if opposite not in bidirectional:
            bidirectional[opposite] = emotion

    return pairs, bidirectional


def _extract_kappa(contagion: Any, warnings: list[str]) -> tuple[dict[str, float], str]:
    if not isinstance(contagion, dict):
        warnings.append("contagion is missing or not an object")
        return {}, ""

    kappa_obj = contagion.get("kappa")
    if not isinstance(kappa_obj, dict):
        warnings.append("contagion.kappa is missing or not an object")
        return {}, ""

    kappa_comment = ""
    if isinstance(kappa_obj.get("comment"), str):
        kappa_comment = kappa_obj["comment"]

    kappa_values: dict[str, float] = {}
    for emotion, value in kappa_obj.items():
        if emotion == "comment":
            continue
        numeric_value = _as_number(value)
        if numeric_value is None:
            warnings.append(f"contagion.kappa.{emotion} is not numeric; skipped")
            continue
        kappa_values[emotion] = numeric_value

    return kappa_values, kappa_comment


def _normalize_couplings(value: Any, warnings: list[str], section_key: str) -> list[dict[str, Any]]:
    if isinstance(value, dict):
        entries = [value]
    elif isinstance(value, list):
        entries = value
    else:
        warnings.append(f"{section_key} must be an object or array; skipped")
        return []

    couplings: list[dict[str, Any]] = []
    for index, entry in enumerate(entries):
        if not isinstance(entry, dict):
            warnings.append(f"{section_key}[{index}] is not an object; skipped")
            continue
        axis = entry.get("axis")
        coeff = _as_number(entry.get("coeff"))
        if not isinstance(axis, str) or not axis:
            warnings.append(f"{section_key}[{index}].axis is invalid; skipped")
            continue
        if coeff is None:
            warnings.append(f"{section_key}[{index}].coeff is invalid; skipped")
            continue
        couplings.append({"axis": axis, "coeff": coeff})
    return couplings


def _count_numeric_parameters(value: Any) -> int:
    if isinstance(value, dict):
        total = 0
        for key, item in value.items():
            if key == "comment":
                continue
            total += _count_numeric_parameters(item)
        return total
    if isinstance(value, list):
        return sum(_count_numeric_parameters(item) for item in value)
    return int(_as_number(value) is not None)


def _compute_total_parameters(
    *,
    fast_decay: dict[str, Any],
    slow_decay: dict[str, Any],
    opposite_pairs: list[list[str]],
    inhibition_gamma: float | None,
    memory_traces: dict[str, Any],
    habituation_eta: float | None,
    stress_tau_hours: float | None,
    stress_weights: dict[str, float],
    contagion_kappa: dict[str, float],
    contagion_distance_scale: float | None,
    contagion_min_source: float | None,
    mental_break_beta: float | None,
    mental_break_tick_prob: float | None,
    mental_break_threshold: float | None,
    mental_break_behaviors: dict[str, Any],
    personality_emotions: dict[str, dict[str, Any]],
    baseline_emotions: dict[str, dict[str, Any]],
    half_life_adj_emotions: dict[str, dict[str, Any]],
) -> int:
    total = 0

    total += len(fast_decay)
    total += len(slow_decay)
    total += len(opposite_pairs)

    total += int(inhibition_gamma is not None)

    for key in (
        "memory_trace_threshold",
        "memory_trace_ratio",
        "memory_trace_default_half_life_days",
        "memory_trace_trauma_half_life_days",
    ):
        total += int(_as_number(memory_traces.get(key)) is not None)

    total += int(habituation_eta is not None)

    total += int(stress_tau_hours is not None)
    total += len(stress_weights)

    total += len(contagion_kappa)
    total += int(contagion_distance_scale is not None)
    total += int(contagion_min_source is not None)

    total += int(mental_break_beta is not None)
    total += int(mental_break_tick_prob is not None)
    total += int(mental_break_threshold is not None)
    total += len(mental_break_behaviors)

    total += sum(
        len(details.get("couplings", [])) for details in personality_emotions.values()
    )

    # Baselines contain clamp bounds (min/max) and axis metadata; for an at-a-glance
    # parameter count we treat only base/scale as tunable baselines.
    for baseline in baseline_emotions.values():
        total += int(_as_number(baseline.get("base")) is not None)
        total += int(_as_number(baseline.get("scale")) is not None)

    total += sum(
        len(details.get("couplings", [])) for details in half_life_adj_emotions.values()
    )

    return total


def _select_source_file(manifest: dict, warnings: list[str]) -> str | None:
    entries = manifest.get("data_files", [])
    if not isinstance(entries, list):
        warnings.append("manifest.data_files is not a list; cannot locate decay parameters")
        return None

    candidates: list[str] = []
    for entry in entries:
        if not isinstance(entry, dict):
            continue
        rel_path = entry.get("file")
        if not isinstance(rel_path, str):
            continue
        if SOURCE_HINT in rel_path.replace("\\", "/"):
            candidates.append(rel_path)

    if not candidates:
        warnings.append("No decay_parameters JSON file found in manifest.data_files")
        return None
    if len(candidates) > 1:
        warnings.append(f"Multiple decay parameter files found; using first: {candidates[0]}")
    return candidates[0]


def run(manifest: dict) -> dict:
    """Extract emotion decay, personality sensitivity, contagion, and mental break parameters.

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

    if not isinstance(manifest, dict):
        warnings.append("manifest is not an object; using empty manifest")
        manifest = {}

    source_file = _select_source_file(manifest, warnings)
    source_data: dict[str, Any] = {}
    if source_file:
        source_path = config.source_path(source_file)
        if not os.path.exists(source_path):
            warnings.append(f"Missing source file: {source_file}")
        else:
            try:
                with open(source_path, "r", encoding="utf-8") as handle:
                    loaded = json.load(handle)
                if isinstance(loaded, dict):
                    source_data = loaded
                else:
                    warnings.append(f"{source_file} root is not an object; extraction skipped")
            except (OSError, json.JSONDecodeError) as exc:
                warnings.append(f"Failed to read {source_file}: {exc}")

    fast_section = source_data.get("fast_half_life_hours", {})
    slow_section = source_data.get("slow_half_life_hours", {})
    fast_decay = _extract_decay_rates(fast_section, "fast_half_life_hours", warnings)
    slow_decay = _extract_decay_rates(slow_section, "slow_half_life_hours", warnings)

    opposite_pairs_raw = source_data.get("opposite_pairs", {})
    opposite_pairs, bidirectional_pairs = _extract_unique_pairs(opposite_pairs_raw, warnings)

    inhibition_gamma = _as_number(source_data.get("inhibition_gamma"))
    if inhibition_gamma is None:
        warnings.append("inhibition_gamma is missing or non-numeric")

    memory_traces = {
        "memory_trace_threshold": _as_number(source_data.get("memory_trace_threshold")),
        "memory_trace_ratio": _as_number(source_data.get("memory_trace_ratio")),
        "memory_trace_default_half_life_days": _as_number(
            source_data.get("memory_trace_default_half_life_days")
        ),
        "memory_trace_trauma_half_life_days": _as_number(
            source_data.get("memory_trace_trauma_half_life_days")
        ),
        "description": "Memory traces persist intense fast-layer emotion events over long horizons",
    }

    habituation_eta = _as_number(source_data.get("habituation_eta"))
    if habituation_eta is None:
        warnings.append("habituation_eta is missing or non-numeric")

    stress_obj = source_data.get("stress", {})
    stress_tau_hours = None
    stress_weights: dict[str, float] = {}
    if isinstance(stress_obj, dict):
        stress_tau_hours = _as_number(stress_obj.get("tau_hours"))
        raw_weights = stress_obj.get("weights", {})
        if isinstance(raw_weights, dict):
            for emotion, value in raw_weights.items():
                numeric_value = _as_number(value)
                if numeric_value is None:
                    warnings.append(f"stress.weights.{emotion} is not numeric; skipped")
                    continue
                stress_weights[emotion] = numeric_value
        else:
            warnings.append("stress.weights is missing or not an object")
    elif source_data:
        warnings.append("stress is not an object")

    contagion_obj = source_data.get("contagion", {})
    kappa_values, kappa_comment = _extract_kappa(contagion_obj, warnings)
    contagion_distance_scale = None
    contagion_min_source = None
    if isinstance(contagion_obj, dict):
        contagion_distance_scale = _as_number(contagion_obj.get("distance_scale"))
        contagion_min_source = _as_number(contagion_obj.get("min_source"))

    mental_break_obj = source_data.get("mental_break", {})
    mental_break_beta = None
    mental_break_tick_prob = None
    mental_break_threshold = None
    mental_break_behaviors: dict[str, dict[str, Any]] = {}
    if isinstance(mental_break_obj, dict):
        mental_break_beta = _as_number(mental_break_obj.get("beta"))
        mental_break_tick_prob = _as_number(mental_break_obj.get("tick_prob"))
        mental_break_threshold = _as_number(mental_break_obj.get("threshold"))

        behaviors_obj = mental_break_obj.get("behaviors", {})
        if isinstance(behaviors_obj, dict):
            for behavior_name, behavior in behaviors_obj.items():
                if not isinstance(behavior, dict):
                    warnings.append(f"mental_break.behaviors.{behavior_name} is not an object; skipped")
                    continue
                mental_break_behaviors[behavior_name] = {
                    "duration_hours": _as_number(behavior.get("duration_hours")),
                    "energy_drain": _as_number(behavior.get("energy_drain")),
                    "description": behavior.get("description", ""),
                }
        else:
            warnings.append("mental_break.behaviors is missing or not an object")
    elif source_data:
        warnings.append("mental_break is not an object")

    personality_obj = source_data.get("personality_sensitivity", {})
    personality_comment = ""
    personality_emotions: dict[str, dict[str, Any]] = {}
    if isinstance(personality_obj, dict):
        if isinstance(personality_obj.get("comment"), str):
            personality_comment = personality_obj["comment"]
        for emotion, value in personality_obj.items():
            if emotion == "comment":
                continue
            couplings = _normalize_couplings(value, warnings, f"personality_sensitivity.{emotion}")
            personality_emotions[emotion] = {
                "couplings": couplings,
                "formula": "sensitivity = exp(coeff * z_axis)",
            }
    elif source_data:
        warnings.append("personality_sensitivity is not an object")

    baselines_obj = source_data.get("baselines", {})
    baselines_comment = ""
    baseline_emotions: dict[str, dict[str, Any]] = {}
    if isinstance(baselines_obj, dict):
        if isinstance(baselines_obj.get("comment"), str):
            baselines_comment = baselines_obj["comment"]
        for emotion, value in baselines_obj.items():
            if emotion == "comment":
                continue
            if not isinstance(value, dict):
                warnings.append(f"baselines.{emotion} is not an object; skipped")
                continue
            baseline_emotions[emotion] = dict(value)
    elif source_data:
        warnings.append("baselines is not an object")

    half_life_adj_obj = source_data.get("half_life_adjustments", {})
    half_life_adj_comment = ""
    half_life_adj_emotions: dict[str, dict[str, Any]] = {}
    if isinstance(half_life_adj_obj, dict):
        if isinstance(half_life_adj_obj.get("comment"), str):
            half_life_adj_comment = half_life_adj_obj["comment"]
        for emotion, value in half_life_adj_obj.items():
            if emotion == "comment":
                continue
            couplings = _normalize_couplings(value, warnings, f"half_life_adjustments.{emotion}")
            half_life_adj_emotions[emotion] = {
                "couplings": couplings,
                "formula": "adjusted_half_life = base_half_life * exp(coeff * z_axis)",
            }
    elif source_data:
        warnings.append("half_life_adjustments is not an object")

    output_data: dict[str, Any] = {
        "extracted_at": datetime.now(timezone.utc).isoformat(),
        "source_file": source_file or "",
        "model_references": MODEL_REFERENCES,
        "fast_decay": {
            "emotions": fast_decay,
            "description": (
                "Fast layer (episodic) — rapid exponential decay after emotional events"
            ),
        },
        "slow_decay": {
            "emotions": slow_decay,
            "description": (
                "Slow layer (mood/baseline) — long-timescale exponential decay"
            ),
        },
        "opposite_pairs": {
            "pairs": opposite_pairs,
            "bidirectional_map": bidirectional_pairs,
            "inhibition_gamma": inhibition_gamma,
            "description": (
                "When emotion rises by delta, opposite is suppressed by gamma * delta"
            ),
        },
        "inhibition": {
            "gamma": inhibition_gamma,
            "description": "When one emotion rises by delta, opposite is suppressed by gamma * delta",
            "formula": "opposite_delta = -gamma * delta",
        },
        "memory_traces": memory_traces,
        "habituation": {
            "eta": habituation_eta,
            "formula": "factor = exp(-eta * count)",
        },
        "stress": {
            "tau_hours": stress_tau_hours,
            "weights": stress_weights,
            "description": "Emotion-weighted stress accumulator with exponential decay",
        },
        "contagion": {
            "kappa": kappa_values,
            "distance_scale": contagion_distance_scale,
            "min_source": contagion_min_source,
            "threshold": contagion_min_source,
            "description": "Settlement-scoped emotional contagion with distance attenuation",
            "kappa_comment": kappa_comment,
        },
        "mental_break": {
            "beta": mental_break_beta,
            "tick_prob": mental_break_tick_prob,
            "threshold": mental_break_threshold,
            "probability_formula": (
                "p(break) = tick_prob / (1 + exp(-(stress - threshold) / beta))"
            ),
            "behaviors": mental_break_behaviors,
        },
        "personality_coupling": {
            "formula": "sensitivity = exp(coeff * z_axis)",
            "comment": personality_comment,
            "emotions": personality_emotions,
        },
        "baselines": {
            "formula": "clampf(base + scale * z_axis, min, max)",
            "comment": baselines_comment,
            "emotions": baseline_emotions,
        },
        "half_life_adjustments": {
            "formula": "base_half_life * exp(coeff * z_axis)",
            "comment": half_life_adj_comment,
            "emotions": half_life_adj_emotions,
        },
        "stats": {
            "total_parameters": _compute_total_parameters(
                fast_decay=fast_decay,
                slow_decay=slow_decay,
                opposite_pairs=opposite_pairs,
                inhibition_gamma=inhibition_gamma,
                memory_traces=memory_traces,
                habituation_eta=habituation_eta,
                stress_tau_hours=stress_tau_hours,
                stress_weights=stress_weights,
                contagion_kappa=kappa_values,
                contagion_distance_scale=contagion_distance_scale,
                contagion_min_source=contagion_min_source,
                mental_break_beta=mental_break_beta,
                mental_break_tick_prob=mental_break_tick_prob,
                mental_break_threshold=mental_break_threshold,
                mental_break_behaviors=mental_break_behaviors,
                personality_emotions=personality_emotions,
                baseline_emotions=baseline_emotions,
                half_life_adj_emotions=half_life_adj_emotions,
            ),
            "emotion_count": len(set(fast_decay.keys()) | set(slow_decay.keys())),
            "mental_break_types": len(mental_break_behaviors),
        },
    }

    config.ensure_dir(config.EXTRACTED_DIR)
    output_path = os.path.join(config.EXTRACTED_DIR, "decay_config.json")
    try:
        with open(output_path, "w", encoding="utf-8") as handle:
            json.dump(output_data, handle, indent=2, ensure_ascii=False)
            handle.write("\n")
        files_written.append(output_path)
    except OSError as exc:
        errors.append(f"failed to write {output_path}: {exc}")

    return {
        "files_written": files_written,
        "items_processed": int(bool(source_data)),
        "warnings": warnings,
        "errors": errors,
    }
