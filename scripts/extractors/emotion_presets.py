"""Extract emotion event presets with appraisal semantics and predicted impulses."""

from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from decimal import ROUND_HALF_UP, Decimal
from typing import Any

import scripts.config as config

_TARGET_RELATIVE_PATH = "data/emotions/event_presets.json"

_APPRAISAL_DIMENSIONS = [
    {
        "id": "goal_congruence",
        "abbrev": "g",
        "range": "-1 to +1",
        "description": "Does this event help (+) or hinder (-) the entity's goals?",
        "primary_emotions": ["joy", "sadness"],
    },
    {
        "id": "novelty",
        "abbrev": "n",
        "range": "0 to 1",
        "description": "How unexpected/new is this event?",
        "primary_emotions": ["surprise"],
    },
    {
        "id": "controllability",
        "abbrev": "c",
        "range": "0 to 1",
        "description": "Can the entity control/influence the situation?",
        "primary_emotions": ["fear", "anger"],
    },
    {
        "id": "agency",
        "abbrev": "a",
        "range": "-1 to +1",
        "description": "Who caused this? Self (+1) vs external (-1).",
        "primary_emotions": ["anger", "guilt"],
    },
    {
        "id": "norm_violation",
        "abbrev": "m",
        "range": "0 to 1",
        "description": "Does this violate social/moral norms?",
        "primary_emotions": ["disgust"],
    },
    {
        "id": "pathogen",
        "abbrev": "p",
        "range": "0 to 1",
        "description": "Is there contamination/disease threat?",
        "primary_emotions": ["disgust"],
    },
    {
        "id": "social_bond",
        "abbrev": "b",
        "range": "-1 to +1",
        "description": "Does this strengthen (+) or weaken (-) social bonds?",
        "primary_emotions": ["trust", "distrust"],
    },
    {
        "id": "future_relevance",
        "abbrev": "fr",
        "range": "0 to 1",
        "description": "How important is this for future wellbeing?",
        "primary_emotions": ["anticipation"],
    },
]

_IMPULSE_FORMULAS = {
    "joy": "I * max(g, 0)",
    "sadness": "I * max(-g, 0) * (1 - c)",
    "fear": "I * max(-g, 0) * (1 - c) * fr",
    "surprise": "I * n",
    "anger": "I * max(-g, 0) * max(-a, 0) * (1 - c)",
    "disgust": "I * max(m + p, 0)",
    "trust": "I * max(b, 0)",
    "anticipation": "I * fr * max(g, 0)",
}


def _round_two(value: float) -> float:
    return float(Decimal(str(value)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))


def _normalize_rel_path(path: str) -> str:
    return path.replace("\\", "/").strip("/")


def _find_presets_relative_path(manifest: dict, warnings: list[str]) -> str | None:
    entries = manifest.get("data_files", [])
    if not isinstance(entries, list):
        warnings.append("manifest.data_files is not a list; no emotion presets processed")
        return None

    matches: list[str] = []
    for entry in entries:
        if not isinstance(entry, dict):
            warnings.append("skipping non-dict data_files entry while locating emotion presets")
            continue

        rel_path = entry.get("file")
        if not isinstance(rel_path, str) or not rel_path:
            continue

        if _normalize_rel_path(rel_path) == _TARGET_RELATIVE_PATH:
            matches.append(rel_path)

    if not matches:
        warnings.append(f"emotion presets file not listed in manifest.data_files: {_TARGET_RELATIVE_PATH}")
        return None

    if len(matches) > 1:
        warnings.append(f"multiple emotion presets entries in manifest; using first: {matches[0]}")

    return matches[0]


def _coerce_float(value: Any, field_name: str, event_id: str, warnings: list[str]) -> float:
    if isinstance(value, bool):
        warnings.append(f"{event_id}: {field_name} was boolean; using 0.0")
        return 0.0

    if isinstance(value, (int, float)):
        return float(value)

    warnings.append(f"{event_id}: missing/invalid {field_name}; using 0.0")
    return 0.0


def _coerce_intensity(value: Any, event_id: str, warnings: list[str]) -> float:
    return _coerce_float(value, "intensity", event_id, warnings)


def _compute_predicted_emotions(appraisal: dict[str, float], intensity: float) -> dict[str, float]:
    g = appraisal["g"]
    n = appraisal["n"]
    c = appraisal["c"]
    a = appraisal["a"]
    m = appraisal["m"]
    p = appraisal["p"]
    b = appraisal["b"]
    fr = appraisal["fr"]

    impulse_scale = intensity / 100.0
    raw = {
        "joy": impulse_scale * max(g, 0.0),
        "sadness": impulse_scale * max(-g, 0.0) * (1.0 - c),
        "fear": impulse_scale * max(-g, 0.0) * (1.0 - c) * fr,
        "surprise": impulse_scale * n,
        "anger": impulse_scale * max(-g, 0.0) * max(-a, 0.0) * (1.0 - c),
        "disgust": impulse_scale * max(m + p, 0.0),
        "trust": impulse_scale * max(b, 0.0),
        "anticipation": impulse_scale * fr * max(g, 0.0),
    }

    predicted: dict[str, float] = {}
    for emotion, score in raw.items():
        rounded = _round_two(score)
        if rounded > 0.01:
            predicted[emotion] = rounded

    return predicted


def _base_output() -> dict[str, Any]:
    return {
        "extracted_at": datetime.now(timezone.utc).isoformat(),
        "source_file": _TARGET_RELATIVE_PATH,
        "model_references": {
            "lazarus_1991": "Lazarus (1991) Emotion and Adaptation — Appraisal Theory",
            "scherer_2009": "Scherer (2009) Component Process Model",
            "plutchik_1980": "Plutchik (1980) 8 Basic Emotions",
        },
        "appraisal_dimensions": _APPRAISAL_DIMENSIONS,
        "impulse_formulas": _IMPULSE_FORMULAS,
        "presets": [],
        "by_category": {},
        "stats": {
            "total_presets": 0,
            "by_category_count": {},
            "trauma_events": 0,
            "highest_intensity": {"id": None, "intensity": 0},
        },
    }


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
    warnings: list[str] = []
    errors: list[str] = []
    files_written: list[str] = []

    output_data = _base_output()

    rel_path = _find_presets_relative_path(manifest, warnings)
    events: dict[str, Any] = {}

    if rel_path:
        source_path = config.source_path(rel_path)
        if not os.path.exists(source_path):
            warnings.append(f"missing file: {rel_path}")
        else:
            try:
                with open(source_path, "r", encoding="utf-8") as handle:
                    parsed = json.load(handle)
            except json.JSONDecodeError as exc:
                warnings.append(f"invalid JSON in {rel_path}: {exc}")
            except OSError as exc:
                warnings.append(f"failed to read {rel_path}: {exc}")
            else:
                if not isinstance(parsed, dict):
                    warnings.append(f"emotion presets root is not an object: {rel_path}")
                else:
                    raw_events = parsed.get("events")
                    if not isinstance(raw_events, dict):
                        warnings.append(f"missing/invalid events object in {rel_path}")
                    else:
                        events = raw_events

    presets: list[dict[str, Any]] = []
    by_category: dict[str, list[str]] = {}
    trauma_events = 0
    highest_intensity_id: str | None = None
    highest_intensity_value = float("-inf")

    for event_id, payload in events.items():
        if not isinstance(payload, dict):
            warnings.append(f"skipping event '{event_id}' because payload is not an object")
            continue

        event_key = str(event_id)
        description = payload.get("description")
        category = payload.get("category")
        is_trauma = bool(payload.get("is_trauma", False))

        if not isinstance(description, str):
            description = ""
        if not isinstance(category, str) or not category:
            category = "unknown"
            warnings.append(f"{event_key}: missing/invalid category; using 'unknown'")

        intensity = _coerce_intensity(payload.get("intensity"), event_key, warnings)

        appraisal = {
            "g": _coerce_float(payload.get("goal_congruence"), "goal_congruence", event_key, warnings),
            "n": _coerce_float(payload.get("novelty"), "novelty", event_key, warnings),
            "c": _coerce_float(payload.get("controllability"), "controllability", event_key, warnings),
            "a": _coerce_float(payload.get("agency"), "agency", event_key, warnings),
            "m": _coerce_float(payload.get("norm_violation"), "norm_violation", event_key, warnings),
            "p": _coerce_float(payload.get("pathogen"), "pathogen", event_key, warnings),
            "b": _coerce_float(payload.get("social_bond"), "social_bond", event_key, warnings),
            "fr": _coerce_float(payload.get("future_relevance"), "future_relevance", event_key, warnings),
        }

        predicted_emotions = _compute_predicted_emotions(appraisal, intensity)

        preset = {
            "id": event_key,
            "description": description,
            "category": category,
            "intensity": _round_two(intensity),
            "is_trauma": is_trauma,
            "appraisal": appraisal,
            "predicted_emotions": predicted_emotions,
        }
        presets.append(preset)

        by_category.setdefault(category, []).append(event_key)
        if is_trauma:
            trauma_events += 1

        if intensity > highest_intensity_value:
            highest_intensity_id = event_key
            highest_intensity_value = intensity

    presets.sort(key=lambda item: item["id"])
    for category_ids in by_category.values():
        category_ids.sort()

    by_category_count = {
        category: len(ids)
        for category, ids in sorted(by_category.items())
    }

    highest_intensity = {"id": highest_intensity_id, "intensity": 0}
    if highest_intensity_id is not None:
        highest_intensity = {
            "id": highest_intensity_id,
            "intensity": _round_two(highest_intensity_value),
        }

    output_data["presets"] = presets
    output_data["by_category"] = {
        category: ids
        for category, ids in sorted(by_category.items())
    }
    output_data["stats"] = {
        "total_presets": len(presets),
        "by_category_count": by_category_count,
        "trauma_events": trauma_events,
        "highest_intensity": highest_intensity,
    }

    config.ensure_dir(config.EXTRACTED_DIR)
    output_path = os.path.join(config.EXTRACTED_DIR, "emotion_presets.json")
    try:
        with open(output_path, "w", encoding="utf-8") as handle:
            json.dump(output_data, handle, ensure_ascii=False, indent=2)
            handle.write("\n")
        files_written.append(output_path)
    except OSError as exc:
        errors.append(f"failed to write {output_path}: {exc}")

    return {
        "files_written": files_written,
        "items_processed": len(presets),
        "warnings": warnings,
        "errors": errors,
    }
