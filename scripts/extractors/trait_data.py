"""Extract trait definitions with HEXACO grouping and effect summaries."""

from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from typing import Any

import scripts.config as config


TRAIT_SOURCE_PATH = "data/species/human/personality/trait_definitions.json"
HEXACO_SOURCE_PATH = "data/personality/hexaco_definition.json"


def _is_number(value: Any) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def _as_str_list(value: Any) -> list[str]:
    if not isinstance(value, list):
        return []
    return [item for item in value if isinstance(item, str)]


def _find_manifest_file(
    entries: list[dict[str, Any]],
    preferred_path: str,
    contains: str,
) -> str | None:
    normalized_preferred = preferred_path.replace("\\", "/")
    candidates: list[str] = []

    for entry in entries:
        rel_path = entry.get("file")
        if not isinstance(rel_path, str) or not rel_path:
            continue
        normalized = rel_path.replace("\\", "/")
        if normalized == normalized_preferred:
            return normalized
        if contains in normalized:
            candidates.append(normalized)

    return candidates[0] if candidates else None


def _find_trait_file(entries: list[dict[str, Any]]) -> str | None:
    path = _find_manifest_file(
        entries=entries,
        preferred_path=TRAIT_SOURCE_PATH,
        contains="trait_definitions",
    )
    if path is None:
        return None
    if path.endswith("trait_definitions.json"):
        return path

    for entry in entries:
        rel_path = entry.get("file")
        if not isinstance(rel_path, str):
            continue
        normalized = rel_path.replace("\\", "/")
        if "trait_definitions" in normalized and normalized.endswith(".json"):
            return normalized
    return path


def _load_json(relative_path: str, warnings: list[str]) -> Any | None:
    source_file = config.source_path(*relative_path.split("/"))
    if not os.path.exists(source_file):
        warnings.append(f"missing file: {relative_path}")
        return None

    try:
        with open(source_file, "r", encoding="utf-8") as handle:
            return json.load(handle)
    except json.JSONDecodeError as exc:
        warnings.append(f"invalid JSON in {relative_path}: {exc}")
        return None
    except OSError as exc:
        warnings.append(f"failed to read {relative_path}: {exc}")
        return None


def _extract_axis_from_condition_entry(condition: dict[str, Any]) -> str | None:
    facet = condition.get("facet")
    if isinstance(facet, str) and facet:
        axis = facet.split("_", 1)[0].strip().upper()
        if axis:
            return axis

    axis_value = condition.get("axis")
    if isinstance(axis_value, str) and axis_value:
        return axis_value.strip().upper()

    return None


def _extract_trait_axis(condition: Any) -> str | None:
    if not isinstance(condition, dict):
        return None

    composite = condition.get("all")
    if isinstance(composite, list) and composite:
        first = composite[0]
        if isinstance(first, dict):
            axis = _extract_axis_from_condition_entry(first)
            if axis:
                return axis
        return None

    return _extract_axis_from_condition_entry(condition)


def _build_effect_summary(effects: Any) -> dict[str, Any]:
    if not isinstance(effects, dict):
        effects = {}

    behavior_weights = effects.get("behavior_weights")
    if not isinstance(behavior_weights, dict):
        behavior_weights = {}

    emotion_modifiers = effects.get("emotion_modifiers")
    if not isinstance(emotion_modifiers, dict):
        emotion_modifiers = {}

    stress_modifiers = effects.get("stress_modifiers")
    if not isinstance(stress_modifiers, dict):
        stress_modifiers = {}

    violation_stress = stress_modifiers.get("violation_stress")
    if not isinstance(violation_stress, dict):
        violation_stress = {}

    amplified_behaviors = [
        key
        for key, value in behavior_weights.items()
        if isinstance(key, str) and _is_number(value) and value > 1.0
    ]
    suppressed_behaviors = [
        key
        for key, value in behavior_weights.items()
        if isinstance(key, str) and _is_number(value) and value < 1.0
    ]
    emotion_sensitivities = [
        key
        for key, value in emotion_modifiers.items()
        if isinstance(key, str) and _is_number(value) and value > 1.0
    ]
    violation_actions = [key for key in violation_stress if isinstance(key, str)]

    stress_gain_mult = stress_modifiers.get("stress_gain_mult")
    if _is_number(stress_gain_mult):
        if stress_gain_mult > 1.0:
            stress_impact = "increases"
        elif stress_gain_mult < 1.0:
            stress_impact = "decreases"
        else:
            stress_impact = "neutral"
    else:
        stress_impact = "unknown"

    return {
        "amplified_behaviors": amplified_behaviors,
        "suppressed_behaviors": suppressed_behaviors,
        "emotion_sensitivities": emotion_sensitivities,
        "violation_actions": violation_actions,
        "stress_impact": stress_impact,
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

    entries = manifest.get("data_files", [])
    if not isinstance(entries, list):
        warnings.append("manifest.data_files is not a list; no trait data processed")
        entries = []

    normalized_entries: list[dict[str, Any]] = []
    for entry in entries:
        if not isinstance(entry, dict):
            warnings.append("skipping non-dict data_files entry")
            continue
        normalized_entries.append(entry)

    trait_source = _find_trait_file(normalized_entries)
    if trait_source is None:
        warnings.append("trait_definitions file not found in manifest.data_files")
        trait_source = TRAIT_SOURCE_PATH

    hexaco_source = _find_manifest_file(
        entries=normalized_entries,
        preferred_path=HEXACO_SOURCE_PATH,
        contains="hexaco_definition",
    )
    if hexaco_source is None:
        warnings.append("hexaco_definition file not found in manifest.data_files")
        hexaco_source = HEXACO_SOURCE_PATH

    hexaco_axes: dict[str, Any] = {}
    hexaco_data = _load_json(hexaco_source, warnings)
    if isinstance(hexaco_data, dict):
        axes = hexaco_data.get("axes")
        if isinstance(axes, dict):
            hexaco_axes = axes
        else:
            warnings.append(f"hexaco_definition missing 'axes' object: {hexaco_source}")
    elif hexaco_data is not None:
        warnings.append(f"hexaco_definition is not an object: {hexaco_source}")

    raw_traits = _load_json(trait_source, warnings)
    if raw_traits is None:
        raw_traits = []
    if not isinstance(raw_traits, list):
        warnings.append(f"trait_definitions is not an array: {trait_source}")
        raw_traits = []

    traits: list[dict[str, Any]] = []
    by_axis: dict[str, list[str]] = {}
    by_type: dict[str, list[str]] = {
        "personality": [],
        "dark": [],
        "composite": [],
    }
    synergy_graph: dict[str, dict[str, list[str]]] = {}
    by_valence_count: dict[str, int] = {}

    for item in raw_traits:
        if not isinstance(item, dict):
            warnings.append("skipping non-object trait entry")
            continue
        if "_comment" in item or "id" not in item:
            continue

        trait_id = item.get("id")
        if not isinstance(trait_id, str) or not trait_id:
            warnings.append("skipping trait entry with invalid id")
            continue

        axis = _extract_trait_axis(item.get("condition")) or "unknown"
        axis_info = hexaco_axes.get(axis, {}) if isinstance(hexaco_axes, dict) else {}

        trait_type = item.get("type") if isinstance(item.get("type"), str) else "unknown"
        valence = item.get("valence") if isinstance(item.get("valence"), str) else "unknown"

        by_axis.setdefault(axis, []).append(trait_id)
        by_type.setdefault(trait_type, []).append(trait_id)
        by_valence_count[valence] = by_valence_count.get(valence, 0) + 1

        synergies = _as_str_list(item.get("synergies"))
        anti_synergies = _as_str_list(item.get("anti_synergies"))
        synergy_graph[trait_id] = {
            "synergies": synergies,
            "anti_synergies": anti_synergies,
        }

        trait_output = dict(item)
        trait_output["axis"] = axis
        trait_output["axis_name"] = (
            axis_info.get("name") if isinstance(axis_info, dict) else ""
        )
        trait_output["axis_name_kr"] = (
            axis_info.get("name_kr") if isinstance(axis_info, dict) else ""
        )
        trait_output["effect_summary"] = _build_effect_summary(item.get("effects"))
        traits.append(trait_output)

    output = {
        "extracted_at": datetime.now(timezone.utc).isoformat(),
        "source_file": trait_source,
        "hexaco_axes": hexaco_axes,
        "traits": traits,
        "by_axis": by_axis,
        "by_type": by_type,
        "synergy_graph": synergy_graph,
        "stats": {
            "total_traits": len(traits),
            "by_axis_count": {axis: len(ids) for axis, ids in by_axis.items()},
            "by_type_count": {kind: len(ids) for kind, ids in by_type.items()},
            "by_valence_count": by_valence_count,
        },
    }

    config.ensure_dir(config.EXTRACTED_DIR)
    output_path = os.path.join(config.EXTRACTED_DIR, "trait_data.json")
    try:
        with open(output_path, "w", encoding="utf-8") as handle:
            json.dump(output, handle, indent=2, ensure_ascii=False)
            handle.write("\n")
        files_written.append(output_path)
    except OSError as exc:
        errors.append(f"failed to write {output_path}: {exc}")

    return {
        "files_written": files_written,
        "items_processed": len(traits),
        "warnings": warnings,
        "errors": errors,
    }
