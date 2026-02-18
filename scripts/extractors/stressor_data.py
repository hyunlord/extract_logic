"""Extract stressor event data for stress documentation generation."""

from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from typing import Any

import scripts.config as config


TARGET_FILE = "data/stressor_events.json"
MODEL_REFERENCES = {
    "holmes_rahe": "Holmes & Rahe (1967) Social Readjustment Rating Scale",
    "lazarus": "Lazarus & Folkman (1984) Transactional Model of Stress",
    "cor": "Hobfoll (1989) Conservation of Resources — loss aversion 2.5x multiplier",
    "hexaco": "Ashton & Lee (2007) HEXACO Personality Model",
}


def _normalize_rel_path(path: str) -> str:
    return path.replace("\\", "/")


def _find_stressor_path(manifest: dict, warnings: list[str]) -> str | None:
    entries = manifest.get("data_files", [])
    if not isinstance(entries, list):
        warnings.append("manifest.data_files is not a list; stressor extractor skipped")
        return None

    for entry in entries:
        if not isinstance(entry, dict):
            warnings.append("skipping non-dict data_files entry")
            continue

        rel_path = entry.get("file")
        if not isinstance(rel_path, str) or not rel_path:
            warnings.append("skipping data_files entry with missing file path")
            continue

        normalized = _normalize_rel_path(rel_path)
        if normalized == TARGET_FILE or os.path.basename(normalized) == "stressor_events.json":
            return normalized

    warnings.append("stressor_events.json not found in manifest.data_files")
    return None


def _to_float(value: Any, field: str, event_id: str, warnings: list[str]) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        warnings.append(f"{event_id}: invalid {field} '{value}', defaulting to 0.0")
        return 0.0


def _to_bool(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, (int, float)):
        return value != 0
    if isinstance(value, str):
        normalized = value.strip().lower()
        return normalized in {"true", "1", "yes", "y"}
    return False


def _to_numeric_effect(value: Any, field: str, event_id: str, warnings: list[str]) -> int | float:
    number = _to_float(value, field, event_id, warnings)
    if number.is_integer():
        return int(number)
    return number


def _parse_emotion_inject(
    emotion_inject: Any,
    event_id: str,
    warnings: list[str],
) -> tuple[dict[str, int | float], dict[str, int | float]]:
    fast_layer_effects: dict[str, int | float] = {}
    slow_layer_effects: dict[str, int | float] = {}

    if emotion_inject is None:
        return fast_layer_effects, slow_layer_effects
    if not isinstance(emotion_inject, dict):
        warnings.append(f"{event_id}: emotion_inject is not an object")
        return fast_layer_effects, slow_layer_effects

    for key, value in emotion_inject.items():
        if not isinstance(key, str):
            continue
        if key.endswith("_fast"):
            fast_layer_effects[key[: -len("_fast")]] = _to_numeric_effect(
                value, f"emotion_inject.{key}", event_id, warnings
            )
        elif key.endswith("_slow"):
            slow_layer_effects[key[: -len("_slow")]] = _to_numeric_effect(
                value, f"emotion_inject.{key}", event_id, warnings
            )

    return (
        {key: fast_layer_effects[key] for key in sorted(fast_layer_effects)},
        {key: slow_layer_effects[key] for key in sorted(slow_layer_effects)},
    )


def _parse_personality_modifiers(
    personality_modifiers: Any,
    event_id: str,
    warnings: list[str],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]]]:
    axis_modifiers: list[dict[str, Any]] = []
    facet_modifiers: list[dict[str, Any]] = []
    trait_modifiers: list[dict[str, Any]] = []

    if personality_modifiers is None:
        return axis_modifiers, facet_modifiers, trait_modifiers
    if not isinstance(personality_modifiers, dict):
        warnings.append(f"{event_id}: personality_modifiers is not an object")
        return axis_modifiers, facet_modifiers, trait_modifiers

    traits = personality_modifiers.get("traits")
    if traits is None:
        pass
    elif isinstance(traits, dict):
        for trait, multiplier in sorted(traits.items()):
            if not isinstance(trait, str):
                continue
            trait_modifiers.append(
                {
                    "trait": trait,
                    "multiplier": _to_float(
                        multiplier,
                        f"personality_modifiers.traits.{trait}",
                        event_id,
                        warnings,
                    ),
                }
            )
    else:
        warnings.append(f"{event_id}: personality_modifiers.traits is not an object")

    for key, value in sorted(personality_modifiers.items()):
        if key == "traits":
            continue
        if not isinstance(value, dict):
            warnings.append(f"{event_id}: personality_modifiers.{key} is not an object")
            continue

        modifier = {
            "weight": _to_float(
                value.get("weight"),
                f"personality_modifiers.{key}.weight",
                event_id,
                warnings,
            ),
            "direction": value.get("direction")
            if isinstance(value.get("direction"), str)
            else "",
        }

        if key.endswith("_axis"):
            axis_modifiers.append({"axis": key.split("_", 1)[0], **modifier})
        else:
            facet_modifiers.append({"facet": key, **modifier})

    return axis_modifiers, facet_modifiers, trait_modifiers


def _safe_object(value: Any, field_name: str, event_id: str, warnings: list[str]) -> dict[str, Any]:
    if value is None:
        return {}
    if isinstance(value, dict):
        return value
    warnings.append(f"{event_id}: {field_name} is not an object")
    return {}


def _build_output(
    source_rel_path: str,
    raw_data: Any,
    warnings: list[str],
) -> tuple[dict[str, Any], int]:
    category_events: dict[str, list[dict[str, Any]]] = {}
    filtered_comments = 0
    loss_events = 0

    if not isinstance(raw_data, dict):
        warnings.append(f"{source_rel_path} is not a top-level object")
        raw_data = {}

    for event_id, event_value in raw_data.items():
        if isinstance(event_id, str) and event_id.startswith("_comment"):
            filtered_comments += 1
            continue
        if not isinstance(event_id, str):
            continue
        if not isinstance(event_value, dict):
            warnings.append(f"{event_id}: stressor event payload is not an object")
            continue

        base_instant = _to_float(event_value.get("base_instant"), "base_instant", event_id, warnings)
        base_per_tick = _to_float(event_value.get("base_per_tick"), "base_per_tick", event_id, warnings)
        base_decay_rate = _to_float(
            event_value.get("base_decay_rate"), "base_decay_rate", event_id, warnings
        )
        decay_for_formula = max(base_decay_rate, 0.001)

        is_loss = _to_bool(event_value.get("is_loss"))
        severity_score = base_instant + (base_per_tick / decay_for_formula) * 10
        if is_loss:
            severity_score *= 2.5
            loss_events += 1

        (
            axis_modifiers,
            facet_modifiers,
            trait_modifiers,
        ) = _parse_personality_modifiers(
            event_value.get("personality_modifiers"),
            event_id,
            warnings,
        )
        fast_layer_effects, slow_layer_effects = _parse_emotion_inject(
            event_value.get("emotion_inject"),
            event_id,
            warnings,
        )

        category = event_value.get("category")
        if not isinstance(category, str) or not category:
            category = "unknown"

        name_kr = event_value.get("name_kr")
        name_en = event_value.get("name_en")

        event_record = {
            "id": event_id,
            "name_kr": name_kr if isinstance(name_kr, str) else "",
            "name_en": name_en if isinstance(name_en, str) else "",
            "category": category,
            "is_loss": is_loss,
            "base_instant": base_instant,
            "base_per_tick": base_per_tick,
            "base_decay_rate": base_decay_rate,
            "severity_score": severity_score,
            "axis_modifiers": axis_modifiers,
            "facet_modifiers": facet_modifiers,
            "trait_modifiers": trait_modifiers,
            "relationship_scaling": _safe_object(
                event_value.get("relationship_scaling"),
                "relationship_scaling",
                event_id,
                warnings,
            ),
            "context_modifiers": _safe_object(
                event_value.get("context_modifiers"),
                "context_modifiers",
                event_id,
                warnings,
            ),
            "fast_layer_effects": fast_layer_effects,
            "slow_layer_effects": slow_layer_effects,
        }

        category_events.setdefault(category, []).append(event_record)

    sorted_categories = sorted(category_events)
    events: list[dict[str, Any]] = []
    by_category: dict[str, list[str]] = {}
    by_category_count: dict[str, int] = {}

    for category in sorted_categories:
        sorted_items = sorted(
            category_events[category],
            key=lambda item: item["severity_score"],
            reverse=True,
        )
        events.extend(sorted_items)
        by_category[category] = [item["id"] for item in sorted_items]
        by_category_count[category] = len(sorted_items)

    max_severity = max((item["severity_score"] for item in events), default=0.0)

    return (
        {
            "extracted_at": datetime.now(timezone.utc).isoformat(),
            "source_file": source_rel_path,
            "model_references": MODEL_REFERENCES,
            "events": events,
            "by_category": by_category,
            "stats": {
                "total_events": len(events),
                "by_category_count": by_category_count,
                "loss_events": loss_events,
                "max_severity": max_severity,
                "filtered_comments": filtered_comments,
            },
        },
        len(events),
    )


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

    source_rel_path = _find_stressor_path(manifest, warnings) or TARGET_FILE
    source_path = config.source_path(source_rel_path)

    raw_data: Any = {}
    if os.path.exists(source_path):
        try:
            with open(source_path, "r", encoding="utf-8") as handle:
                raw_data = json.load(handle)
        except json.JSONDecodeError as exc:
            warnings.append(f"invalid JSON in {source_rel_path}: {exc}")
        except OSError as exc:
            warnings.append(f"failed to read {source_rel_path}: {exc}")
    else:
        warnings.append(f"missing file: {source_rel_path}")

    output, items_processed = _build_output(source_rel_path, raw_data, warnings)

    config.ensure_dir(config.EXTRACTED_DIR)
    output_path = os.path.join(config.EXTRACTED_DIR, "stressor_data.json")
    try:
        with open(output_path, "w", encoding="utf-8") as handle:
            json.dump(output, handle, ensure_ascii=False, indent=2)
            handle.write("\n")
        files_written.append(output_path)
    except OSError as exc:
        errors.append(f"failed to write {output_path}: {exc}")

    return {
        "files_written": files_written,
        "items_processed": items_processed,
        "warnings": warnings,
        "errors": errors,
    }
