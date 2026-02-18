"""Phase 3 generator: build calculation-pipeline interaction documentation pages."""

from __future__ import annotations

import json
import os
import re
from collections import defaultdict
from typing import Any

import scripts.config as config
from scripts.generators.strings import t

MANUAL_BLOCK_RE = re.compile(
    r"(<!-- MANUAL:START -->)(.*?)(<!-- MANUAL:END -->)",
    re.DOTALL,
)

def _read_json(path: str, warnings: list[str]) -> dict[str, Any] | None:
    """Read JSON file with graceful error handling."""
    if not os.path.exists(path):
        warnings.append(f"Missing required input file: {path}")
        return None

    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (OSError, json.JSONDecodeError) as exc:
        warnings.append(f"Failed to read {path}: {exc}")
        return None

    if isinstance(data, dict):
        return data

    warnings.append(f"Expected JSON object in {path}, got {type(data).__name__}.")
    return None


def _load_payload(
    extracted: dict[str, Any] | None,
    key: str,
    filename: str,
    warnings: list[str],
) -> dict[str, Any]:
    """Load payload from extracted cache first, then extracted/*.json fallback."""
    if isinstance(extracted, dict):
        for lookup_key in (key, os.path.splitext(filename)[0], filename):
            payload = extracted.get(lookup_key)
            if isinstance(payload, dict):
                return payload

    path = os.path.join(config.EXTRACTED_DIR, filename)
    loaded = _read_json(path, warnings)
    return loaded or {}


def _slugify(name: str) -> str:
    """Convert a value to a deterministic filename-safe slug."""
    slug = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
    return slug or "item"


def _display_name(meta: dict[str, Any]) -> str:
    """Pick a stable display name for a system entry."""
    for key in ("system_name", "class_name", "name"):
        value = meta.get(key)
        if isinstance(value, str) and value.strip():
            return value.strip()

    file_path = str(meta.get("file", ""))
    base = os.path.splitext(os.path.basename(file_path))[0]
    return base or "unknown_system"


def _collect_systems(manifest: dict[str, Any], systems_doc: dict[str, Any]) -> list[dict[str, str]]:
    """Merge manifest + systems metadata into a deterministic system list."""
    by_file: dict[str, dict[str, Any]] = {}

    for section in ("systems", "ai_modules"):
        for entry in manifest.get(section, []):
            if not isinstance(entry, dict):
                continue
            path = entry.get("file")
            if isinstance(path, str) and path.endswith(".gd"):
                by_file[path] = dict(entry)

    for entry in systems_doc.get("systems", []):
        if not isinstance(entry, dict):
            continue
        path = entry.get("file")
        if isinstance(path, str) and path.endswith(".gd"):
            merged = dict(by_file.get(path, {}))
            merged.update(entry)
            by_file[path] = merged

    systems: list[dict[str, str]] = []
    for path, meta in by_file.items():
        name = _display_name(meta)
        systems.append(
            {
                "file": path,
                "name": name,
                "slug": _slugify(name),
                "module": os.path.splitext(os.path.basename(path))[0],
            }
        )

    return sorted(systems, key=lambda item: (item["name"], item["file"]))


def _collect_role_systems(systems: list[dict[str, str]]) -> dict[str, list[dict[str, str]]]:
    """Classify systems into documentation roles."""
    roles: dict[str, list[dict[str, str]]] = defaultdict(list)

    for system in systems:
        text = " ".join((system["file"], system["name"], system["module"])).lower()
        if "personality" in text:
            roles["personality"].append(system)
        if "emotion" in text or "emotions" in text:
            roles["emotion"].append(system)
        if "stress" in text:
            roles["stress"].append(system)
        if "mortality" in text:
            roles["mortality"].append(system)
        if "event" in text:
            roles["events"].append(system)
        if "mental_break" in text:
            roles["mental_break"].append(system)

    for systems_in_role in roles.values():
        systems_in_role.sort(key=lambda item: (item["name"], item["file"]))
    return roles


def _escape_cell(text: str) -> str:
    """Escape markdown table-special pipes."""
    return text.replace("|", "\\|")


def _preserve_manual(existing_text: str, new_text: str) -> str:
    """Preserve MANUAL block content from existing markdown when overwriting."""
    existing_match = MANUAL_BLOCK_RE.search(existing_text)
    new_match = MANUAL_BLOCK_RE.search(new_text)
    if not existing_match or not new_match:
        return new_text

    manual_content = existing_match.group(2)
    return MANUAL_BLOCK_RE.sub(
        lambda match: f"{match.group(1)}{manual_content}{match.group(3)}",
        new_text,
        count=1,
    )


def _write_markdown(path: str, content: str, warnings: list[str]) -> bool:
    """Write markdown with MANUAL block preservation."""
    final_content = content

    if os.path.exists(path):
        try:
            with open(path, "r", encoding="utf-8") as f:
                existing = f.read()
            final_content = _preserve_manual(existing, content)
        except OSError as exc:
            warnings.append(f"Failed to read existing markdown {path}: {exc}")

    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(final_content)
        return True
    except OSError as exc:
        warnings.append(f"Failed to write markdown {path}: {exc}")
        return False


def _normalize_couplings(raw: Any) -> list[tuple[str, float]]:
    """Normalize coupling payload to (axis, coeff) pairs."""
    couplings: list[tuple[str, float]] = []

    def add_from_dict(entry: dict[str, Any]) -> None:
        axis = entry.get("axis")
        coeff = entry.get("coeff")
        if isinstance(axis, str) and isinstance(coeff, (int, float)):
            couplings.append((axis, float(coeff)))

    if isinstance(raw, dict):
        if isinstance(raw.get("couplings"), list):
            for item in raw["couplings"]:
                if isinstance(item, dict):
                    add_from_dict(item)
        else:
            add_from_dict(raw)
    elif isinstance(raw, list):
        for item in raw:
            if isinstance(item, dict):
                add_from_dict(item)

    return couplings


def _find_data_file_content(data_files_payload: dict[str, Any], file_name: str) -> dict[str, Any]:
    """Fetch full_content for one extracted data file entry."""
    for row in data_files_payload.get("files", []):
        if not isinstance(row, dict):
            continue
        if row.get("file") != file_name:
            continue
        full_content = row.get("full_content")
        if isinstance(full_content, dict):
            return full_content
    return {}


def _reference_lines_for_files(
    references: dict[str, Any],
    files: set[str],
    limit: int = 20,
) -> list[str]:
    """Collect file:line references from references.json for selected files."""
    refs: set[tuple[str, int]] = set()

    for row in references.get("imports", []):
        if not isinstance(row, dict):
            continue
        source = row.get("from_file")
        line = row.get("line")
        if source in files and isinstance(line, int):
            refs.add((source, line))

    for row in references.get("config_refs", []):
        if not isinstance(row, dict):
            continue
        source = row.get("file")
        line = row.get("line")
        if source in files and isinstance(line, int):
            refs.add((source, line))

    for row in references.get("entity_field_access", []):
        if not isinstance(row, dict):
            continue
        source = row.get("file")
        line = row.get("line")
        if source in files and isinstance(line, int):
            refs.add((source, line))

    for row in references.get("cross_system_calls", []):
        if not isinstance(row, dict):
            continue
        source = row.get("from_file")
        line = row.get("line")
        if source in files and isinstance(line, int):
            refs.add((source, line))

    for row in references.get("signals", []):
        if not isinstance(row, dict):
            continue

        emitter = row.get("emitter")
        emitter_line = row.get("emitter_line")
        if emitter in files and isinstance(emitter_line, int):
            refs.add((emitter, emitter_line))

        subscribers = row.get("subscribers", [])
        if not isinstance(subscribers, list):
            continue
        for subscriber in subscribers:
            if not isinstance(subscriber, dict):
                continue
            sub_file = subscriber.get("file")
            sub_line = subscriber.get("line")
            if sub_file in files and isinstance(sub_line, int):
                refs.add((sub_file, sub_line))

    return [
        f"{path}:L{line}"
        for path, line in sorted(refs, key=lambda item: (item[0], item[1]))[:limit]
    ]


def _formula_refs(
    formulas_payload: dict[str, Any],
    file_keywords: tuple[str, ...],
    text_keywords: tuple[str, ...],
    limit: int = 10,
) -> list[str]:
    """Collect formula source references relevant to one interaction pair."""
    refs: set[tuple[str, int]] = set()

    for row in formulas_payload.get("formulas", []):
        if not isinstance(row, dict):
            continue

        file_path = row.get("file")
        line = row.get("line_start")
        if not isinstance(file_path, str) or not isinstance(line, int):
            continue

        blob = " ".join(
            str(row.get(key, ""))
            for key in ("description", "code_snippet", "category", "name", "system", "purpose")
        ).lower()
        path_lower = file_path.lower()

        path_hit = any(keyword.lower() in path_lower for keyword in file_keywords)
        text_hit = any(keyword.lower() in blob for keyword in text_keywords)
        if path_hit or text_hit:
            refs.add((file_path, line))

    return [
        f"{path}:L{line}"
        for path, line in sorted(refs, key=lambda item: (item[0], item[1]))[:limit]
    ]


def _title_case_role(role: str) -> str:
    """Convert role key to display label."""
    labels = {
        "personality": "Personality",
        "emotion": "Emotion",
        "stress": "Stress",
        "mortality": "Mortality",
        "events": "Events",
    }
    return labels.get(role, role.replace("_", " ").title())


def _role_files(role_systems: dict[str, list[dict[str, str]]], *roles: str) -> list[str]:
    """Collect unique system files for one or more roles."""
    files: set[str] = set()
    for role in roles:
        for system in role_systems.get(role, []):
            files.add(system["file"])
    return sorted(files)


def _stress_events(stressor_data: dict[str, Any]) -> list[dict[str, Any]]:
    """Return normalized stress event records."""
    events = stressor_data.get("events", [])
    if isinstance(events, list):
        rows = [row for row in events if isinstance(row, dict)]
        return sorted(rows, key=lambda row: float(row.get("severity_score", 0.0)), reverse=True)
    return []


def _build_data_flow_table(rows: list[dict[str, str]]) -> list[str]:
    """Render a markdown data-flow table."""
    if not rows:
        return [
            "| Data Field | Source | Destination | Formula | Purpose |",
            "|---|---|---|---|---|",
            "| `(none)` | `(none)` | `(none)` | `(none)` | No extracted data flow available |",
        ]

    lines = [
        "| Data Field | Source | Destination | Formula | Purpose |",
        "|---|---|---|---|---|",
    ]
    for row in rows:
        lines.append(
            "| "
            f"`{_escape_cell(row['field'])}` | "
            f"`{_escape_cell(row['source'])}` | "
            f"`{_escape_cell(row['destination'])}` | "
            f"`{_escape_cell(row['formula'])}` | "
            f"{_escape_cell(row['purpose'])} |"
        )
    return lines


def _collect_trait_emotion_examples(trait_data: dict[str, Any]) -> list[dict[str, Any]]:
    """Extract trait-based emotion sensitivity modifiers."""
    examples: list[dict[str, Any]] = []

    for row in trait_data.get("traits", []):
        if not isinstance(row, dict):
            continue

        trait_id = row.get("id")
        effects = row.get("effects")
        if not isinstance(trait_id, str) or not isinstance(effects, dict):
            continue

        emotion_mods = effects.get("emotion_modifiers")
        if not isinstance(emotion_mods, dict):
            continue

        for key, value in emotion_mods.items():
            if not isinstance(key, str) or not isinstance(value, (int, float)):
                continue
            if not key.endswith(("_sensitivity", "_decay_mult")):
                continue

            delta = float(value) - 1.0
            examples.append(
                {
                    "trait": trait_id,
                    "effect": key,
                    "value": float(value),
                    "delta_pct": round(delta * 100.0, 1),
                }
            )

    examples.sort(key=lambda item: (-abs(item["delta_pct"]), item["trait"], item["effect"]))
    return examples


def _source_refs_block(source_refs: list[str]) -> list[str]:
    """Render source reference section lines."""
    if source_refs:
        return [f"- 📄 source: `{ref}`" for ref in source_refs]
    return ["- 📄 source: `(none)`"]


def _merge_source_refs(*ref_lists: list[str], limit: int = 16) -> list[str]:
    """Merge multiple source-ref lists into a deterministic unique list."""
    merged: list[str] = []
    seen: set[str] = set()
    for refs in ref_lists:
        for ref in refs:
            if ref not in seen:
                seen.add(ref)
                merged.append(ref)
            if len(merged) >= limit:
                return merged
    return merged


def _linear_formula(base: float, scale: float, axis: str, minimum: float, maximum: float) -> str:
    """Format baseline linear clamp formula with readable sign."""
    sign = "+" if scale >= 0 else "-"
    scale_mag = abs(scale)
    return f"clamp({base:.3g}{sign}{scale_mag:.3g}*z_{axis}, {minimum:.3g}, {maximum:.3g})"


def _build_personality_emotion_doc(context: dict[str, Any]) -> dict[str, Any]:
    """Build Personality -> Emotion interaction content."""
    decay_config = context["decay_config"]
    trait_data = context["trait_data"]
    role_systems = context["role_systems"]

    personality_cfg = decay_config.get("personality_coupling", {})
    baselines_cfg = decay_config.get("baselines", {})
    half_life_cfg = decay_config.get("half_life_adjustments", {})

    sensitivity_formula = str(
        personality_cfg.get("formula", "sensitivity = exp(coeff * z_axis)")
    )
    baseline_formula = str(
        baselines_cfg.get("formula", "baseline = clamp(base + scale * z_axis, min, max)")
    )
    half_life_formula = str(
        half_life_cfg.get(
            "formula",
            "adjusted_half_life = base_half_life * exp(coeff * z_axis)",
        )
    )

    sensitivity_map = personality_cfg.get("emotions", {})
    baseline_map = baselines_cfg.get("emotions", {})
    half_life_map = half_life_cfg.get("emotions", {})

    if not isinstance(sensitivity_map, dict):
        sensitivity_map = {}
    if not isinstance(baseline_map, dict):
        baseline_map = {}
    if not isinstance(half_life_map, dict):
        half_life_map = {}

    trait_examples = _collect_trait_emotion_examples(trait_data)
    trait_line = "No trait-level emotion modifiers extracted."
    trait_row: dict[str, str] | None = None
    if trait_examples:
        top_trait = trait_examples[0]
        sign = "+" if top_trait["delta_pct"] >= 0 else ""
        trait_line = (
            f"Example: `{top_trait['trait']}` applies `{top_trait['effect']}` "
            f"({sign}{top_trait['delta_pct']}%)."
        )
        trait_row = {
            "field": top_trait["effect"],
            "source": f"trait_data.traits[{top_trait['trait']}].effects.emotion_modifiers",
            "destination": "emotion_system.trait_sensitivity",
            "formula": f"value * {top_trait['value']:.3g}",
            "purpose": "Apply discrete personality trait multiplier",
        }

    flow_rows: list[dict[str, str]] = []

    for emotion in sorted(sensitivity_map.keys())[:4]:
        couplings = _normalize_couplings(sensitivity_map.get(emotion))
        if not couplings:
            continue
        terms = [f"{coeff:.3g}*z_{axis}" for axis, coeff in couplings]
        axes = ", ".join(axis for axis, _ in couplings)
        flow_rows.append(
            {
                "field": f"{emotion}_sensitivity",
                "source": f"entity.personality[{axes}]",
                "destination": f"emotion_system.sensitivity[{emotion}]",
                "formula": f"exp({' + '.join(terms)})",
                "purpose": f"Scale {emotion} impulse amplitude",
            }
        )

    for emotion in sorted(baseline_map.keys())[:3]:
        cfg = baseline_map.get(emotion)
        if not isinstance(cfg, dict):
            continue
        axis = cfg.get("axis")
        base = cfg.get("base")
        scale = cfg.get("scale")
        minimum = cfg.get("min")
        maximum = cfg.get("max")
        if not isinstance(axis, str) or not isinstance(base, (int, float)):
            continue
        if not isinstance(scale, (int, float)):
            continue
        if not isinstance(minimum, (int, float)) or not isinstance(maximum, (int, float)):
            continue
        flow_rows.append(
            {
                "field": f"{emotion}_baseline",
                "source": f"entity.personality.{axis}",
                "destination": f"emotion_system.slow_baseline[{emotion}]",
                "formula": _linear_formula(float(base), float(scale), axis, float(minimum), float(maximum)),
                "purpose": "Set slow-layer emotional baseline",
            }
        )

    for emotion in sorted(half_life_map.keys())[:3]:
        cfg = half_life_map.get(emotion)
        if not isinstance(cfg, dict):
            continue
        couplings = _normalize_couplings(cfg)
        if not couplings:
            continue
        axis, coeff = couplings[0]
        flow_rows.append(
            {
                "field": f"{emotion}_half_life_adj",
                "source": f"entity.personality.{axis}",
                "destination": f"emotion_system.half_life[{emotion}]",
                "formula": f"base_half_life * exp({coeff:.3g}*z_{axis})",
                "purpose": "Adjust emotion persistence duration",
            }
        )

    if trait_row:
        flow_rows.append(trait_row)

    system_files = _role_files(role_systems, "personality", "emotion")
    source_files = sorted(
        {
            *system_files,
            str(decay_config.get("source_file", "")),
            str(trait_data.get("source_file", "")),
        }
        - {""}
    )

    source_refs = _merge_source_refs(
        _reference_lines_for_files(context["references"], set(system_files)),
        _formula_refs(
            context["formulas"],
            file_keywords=("emotion_system", "personality"),
            text_keywords=("sensitivity", "baseline", "half_life", "hexaco"),
        ),
    )

    return {
        "filename": "personality-emotion.md",
        "title": "Personality -> Emotion Calculation Pipeline",
        "description": "How HEXACO personality parameters drive emotion dynamics",
        "header": "Personality -> Emotion",
        "summary": (
            "Personality parameters flow directly into emotion sensitivity, baseline targets, "
            "and half-life controls before impulses are integrated."
        ),
        "interaction_heading": "Personality -> Emotion System",
        "how_heading": "How Personality Affects Emotions",
        "how_lines": [
            f"1. **Sensitivity Coupling**: each emotion is scaled by HEXACO axes via `{sensitivity_formula}`.",
            "   - Example: high Emotionality (`E`) increases fear/sadness response gain.",
            f"2. **Baseline Setting**: slow-layer targets come from `{baseline_formula}`.",
            "   - Example: higher Extraversion (`X`) raises joy baseline.",
            f"3. **Half-life Adjustment**: emotion duration is modulated by `{half_life_formula}`.",
            "   - Example: higher Emotionality (`E`) prolongs fear and sadness traces.",
            f"4. **Trait Effects**: discrete traits apply emotion modifiers. {trait_line}",
        ],
        "flow_title": "Data Flow: Personality -> Emotion",
        "flow_rows": flow_rows,
        "diagram_lines": [
            "```mermaid",
            "graph LR",
            "    subgraph Personality",
            "        P[HEXACO Axes] --> S[Sensitivity]",
            "        P --> B[Baselines]",
            "        P --> HL[Half-life Adj]",
            "        T[Discrete Traits] --> EM[Emotion Modifiers]",
            "    end",
            "    subgraph Emotion",
            "        S --> FI[Fast Impulse]",
            "        B --> SL[Slow Layer]",
            "        HL --> D[Decay Rate]",
            "        EM --> FI",
            "    end",
            "```",
        ],
        "feedback_lines": [
            "- Personality alters emotion dynamics immediately; stronger negative emotion patterns later increase stress feedback risk.",
        ],
        "source_files": source_files,
        "source_refs": source_refs,
    }


def _build_personality_stress_doc(context: dict[str, Any]) -> dict[str, Any]:
    """Build Personality -> Stress interaction content."""
    stressor_data = context["stressor_data"]
    role_systems = context["role_systems"]

    events = _stress_events(stressor_data)

    axis_rows: list[dict[str, Any]] = []
    trait_rows: list[dict[str, Any]] = []
    sample_event_id = "(none)"

    for event in events:
        event_id = str(event.get("id", ""))
        if event_id and sample_event_id == "(none)":
            sample_event_id = event_id

        for axis_row in event.get("axis_modifiers", []):
            if not isinstance(axis_row, dict):
                continue
            axis = axis_row.get("axis")
            weight = axis_row.get("weight")
            direction = axis_row.get("direction")
            if isinstance(axis, str) and isinstance(weight, (int, float)) and isinstance(direction, str):
                axis_rows.append(
                    {
                        "event": event_id,
                        "axis": axis,
                        "weight": float(weight),
                        "direction": direction,
                    }
                )

        for trait_row in event.get("trait_modifiers", []):
            if not isinstance(trait_row, dict):
                continue
            trait = trait_row.get("trait")
            multiplier = trait_row.get("multiplier")
            if isinstance(trait, str) and isinstance(multiplier, (int, float)):
                trait_rows.append(
                    {
                        "event": event_id,
                        "trait": trait,
                        "multiplier": float(multiplier),
                    }
                )

    axis_rows.sort(key=lambda row: (-abs(row["weight"]), row["event"], row["axis"]))
    trait_rows.sort(key=lambda row: (-abs(row["multiplier"] - 1.0), row["event"], row["trait"]))

    flow_rows: list[dict[str, str]] = []
    for row in axis_rows[:4]:
        if row["direction"] == "low_amplifies":
            formula = f"1 + {row['weight']:.3g} * (1 - z_{row['axis']})"
        else:
            formula = f"1 + {row['weight']:.3g} * z_{row['axis']}"
        flow_rows.append(
            {
                "field": f"{row['event']}.{row['axis']}_modifier",
                "source": f"stressor_events.{row['event']}.personality_modifiers",
                "destination": "stress_system.event_scale",
                "formula": formula,
                "purpose": f"Apply {row['direction']} personality amplification",
            }
        )

    for row in trait_rows[:4]:
        flow_rows.append(
            {
                "field": f"{row['event']}.{row['trait']}",
                "source": f"stressor_events.{row['event']}.personality_modifiers.traits",
                "destination": "stress_system.event_scale",
                "formula": f"scale * {row['multiplier']:.3g}",
                "purpose": "Trait-specific multiplier on stress event impact",
            }
        )

    sample_event = events[0] if events else {}
    if isinstance(sample_event, dict):
        base_instant = sample_event.get("base_instant")
        base_per_tick = sample_event.get("base_per_tick")
        if isinstance(base_instant, (int, float)) and isinstance(base_per_tick, (int, float)):
            flow_rows.append(
                {
                    "field": f"{sample_event.get('id', 'event')}.base_load",
                    "source": f"stressor_events.{sample_event.get('id', 'event')}",
                    "destination": "stress_system.trace_builder",
                    "formula": f"instant={base_instant:.3g}, per_tick={base_per_tick:.3g}",
                    "purpose": "Seed stress trace magnitude from event template",
                }
            )

    system_files = _role_files(role_systems, "personality", "stress")
    source_files = sorted(
        {
            *system_files,
            str(stressor_data.get("source_file", "")),
        }
        - {""}
    )

    source_refs = _merge_source_refs(
        _reference_lines_for_files(context["references"], set(system_files)),
        _formula_refs(
            context["formulas"],
            file_keywords=("stress_system", "personality"),
            text_keywords=("appraisal", "stress", "loss", "reserve"),
        ),
    )

    return {
        "filename": "personality-stress.md",
        "title": "Personality -> Stress Calculation Pipeline",
        "description": "How personality weights and traits modulate stress calculations",
        "header": "Personality -> Stress",
        "summary": (
            "Stress templates are personality-conditioned through axis/facet weights and trait "
            "multipliers before event load is accumulated."
        ),
        "interaction_heading": "Personality -> Stress System",
        "how_heading": "How Personality Affects Stress",
        "how_lines": [
            "1. **Modifier Weights**: each stress event applies axis/facet weights using `high_amplifies` / `low_amplifies` directions.",
            "   - Formula pattern: `scale *= (1 + weight * z)` or `scale *= (1 + weight * (1 - z))`.",
            "2. **Trait Multipliers**: event templates apply per-trait multipliers to amplify/suppress stress gain.",
            "   - Example: resilient/callous traits reduce loss-event impact while caregiver/sentimental traits amplify it.",
            "3. **Event Load Seeding**: each event contributes base instant and per-tick stress components.",
            "4. **Loss Amplification**: loss-tagged events apply stronger weighting in stress integration.",
        ],
        "flow_title": "Data Flow: Personality -> Stress",
        "flow_rows": flow_rows,
        "diagram_lines": [
            "```mermaid",
            "graph LR",
            "    subgraph Personality",
            "        AX[HEXACO/Facet Axes] --> WM[Weight Modifiers]",
            "        TR[Traits] --> TM[Trait Multipliers]",
            "    end",
            "    subgraph Stress",
            "        EV[Stress Event Template] --> SC[Event Scale]",
            "        WM --> SC",
            "        TM --> SC",
            "        SC --> ST[Stress Load]",
            "    end",
            "```",
        ],
        "feedback_lines": [
            f"- Personality-conditioned stress scaling is event-specific; highest-severity extracted sample is `{sample_event_id}`.",
        ],
        "source_files": source_files,
        "source_refs": source_refs,
    }


def _build_emotion_stress_doc(context: dict[str, Any]) -> dict[str, Any]:
    """Build Emotion -> Stress interaction content."""
    decay_config = context["decay_config"]
    role_systems = context["role_systems"]

    stress_cfg = decay_config.get("stress", {})
    if not isinstance(stress_cfg, dict):
        stress_cfg = {}
    weights = stress_cfg.get("weights", {})
    if not isinstance(weights, dict):
        weights = {}

    tau_hours = stress_cfg.get("tau_hours")
    tau_text = f"{float(tau_hours):.3g}" if isinstance(tau_hours, (int, float)) else "tau_hours"

    flow_rows: list[dict[str, str]] = []
    for emotion, weight in sorted(weights.items(), key=lambda item: (-abs(float(item[1])), item[0]))[:6]:
        if not isinstance(weight, (int, float)):
            continue
        flow_rows.append(
            {
                "field": emotion,
                "source": f"emotion_data.fast['{emotion}']",
                "destination": "stress_system._calc_emotion_contribution()",
                "formula": f"{float(weight):.3g} * {emotion}",
                "purpose": "Convert emotion magnitude into stress load",
            }
        )

    flow_rows.append(
        {
            "field": "valence_arousal_term",
            "source": "emotion_data.valence, emotion_data.arousal",
            "destination": "stress_system._calc_emotion_contribution()",
            "formula": "gamma_VA * arousal * max(-valence, 0)",
            "purpose": "Capture negative high-arousal stress amplification",
        }
    )

    flow_rows.append(
        {
            "field": "stress_decay_tau",
            "source": "decay_parameters.stress.tau_hours",
            "destination": "stress_system.integrator",
            "formula": f"stress(t+dt) = stress(t) * exp(-dt/{tau_text})",
            "purpose": "Exponential stress decay between updates",
        }
    )

    system_files = _role_files(role_systems, "emotion", "stress")
    source_files = sorted(
        {
            *system_files,
            str(decay_config.get("source_file", "")),
        }
        - {""}
    )

    source_refs = _merge_source_refs(
        _reference_lines_for_files(context["references"], set(system_files)),
        _formula_refs(
            context["formulas"],
            file_keywords=("stress_system", "emotion_system"),
            text_keywords=("emotion", "va", "valence", "arousal", "stress"),
        ),
    )

    return {
        "filename": "emotion-stress.md",
        "title": "Emotion -> Stress Calculation Pipeline",
        "description": "How emotion state contributes to stress accumulation",
        "header": "Emotion -> Stress",
        "summary": (
            "Stress integrates weighted emotion channels plus valence-arousal amplification, "
            "then applies exponential decay over time."
        ),
        "interaction_heading": "Emotion -> Stress System",
        "how_heading": "How Emotions Drive Stress",
        "how_lines": [
            "1. **Emotion Contribution**: stress receives weighted emotion channels from the fast layer.",
            "   - Formula: `gamma_VA * sum(w_e * emotion_e)` with valence-arousal coupling.",
            "2. **Negative Arousal Boost**: high arousal + negative valence increases stress increment.",
            "3. **Temporal Integration**: stress load decays exponentially using `tau_hours`.",
            "4. **Downstream State Impact**: integrated stress updates reserve/allostatic burden.",
        ],
        "flow_title": "Data Flow: Emotion -> Stress",
        "flow_rows": flow_rows,
        "diagram_lines": [
            "```mermaid",
            "graph LR",
            "    subgraph Emotion",
            "        EF[Fast Emotion Values] --> WS[Weighted Sum]",
            "        VA[Valence/Arousal] --> WS",
            "    end",
            "    subgraph Stress",
            "        WS --> INC[Stress Increment]",
            "        INC --> INT[Stress Integrator]",
            "        DEC[Exponential Decay] --> INT",
            "    end",
            "```",
        ],
        "feedback_lines": [
            "- Elevated stress feeds back into emotion dynamics through stress-induced baseline shifts and mental-break pathways.",
        ],
        "source_files": source_files,
        "source_refs": source_refs,
    }


def _build_stress_mortality_doc(context: dict[str, Any]) -> dict[str, Any]:
    """Build Stress -> Mortality interaction content."""
    role_systems = context["role_systems"]
    siler_params = context["siler_parameters"]

    baseline = siler_params.get("baseline", {}) if isinstance(siler_params, dict) else {}
    if not isinstance(baseline, dict):
        baseline = {}
    a1 = baseline.get("a1", "a1")
    b1 = baseline.get("b1", "b1")
    a2 = baseline.get("a2", "a2")
    a3 = baseline.get("a3", "a3")
    b3 = baseline.get("b3", "b3")

    flow_rows = [
        {
            "field": "allostatic_load",
            "source": "stress_system.entity_state.allostatic",
            "destination": "mortality_system.hazard_adjustment",
            "formula": "mu_adj = mu_base * (1 + alpha * allostatic/100)",
            "purpose": "Amplify baseline hazard by chronic stress burden",
        },
        {
            "field": "siler_baseline",
            "source": "mortality.siler_parameters.baseline",
            "destination": "mortality_system.mu_base(age)",
            "formula": f"{a1}*exp(-{b1}*x) + {a2} + {a3}*exp({b3}*x)",
            "purpose": "Compute age-dependent baseline mortality hazard",
        },
        {
            "field": "annual_death_probability",
            "source": "mortality_system.mu_adj",
            "destination": "mortality_system.death_roll",
            "formula": "q = 1 - exp(-mu_adj)",
            "purpose": "Convert adjusted hazard into death probability",
        },
    ]

    system_files = _role_files(role_systems, "stress", "mortality")
    source_files = sorted(
        {
            *system_files,
            "data/species/human/mortality/siler_parameters.json",
        }
    )

    source_refs = _merge_source_refs(
        _reference_lines_for_files(context["references"], set(system_files)),
        _formula_refs(
            context["formulas"],
            file_keywords=("stress_system", "mortality_system"),
            text_keywords=("allostatic", "hazard", "mortality", "siler"),
        ),
    )

    return {
        "filename": "stress-mortality.md",
        "title": "Stress -> Mortality Calculation Pipeline",
        "description": "How stress and allostatic load amplify mortality hazard",
        "header": "Stress -> Mortality",
        "summary": "Stress-derived allostatic load scales mortality hazard before death probability checks.",
        "interaction_heading": "Stress -> Mortality System",
        "how_heading": "How Stress Changes Mortality Risk",
        "how_lines": [
            "1. **Baseline Hazard**: mortality starts from the Siler hazard curve by age.",
            "2. **Allostatic Amplification**: chronic stress increases hazard via `mu * (1 + alpha * allostatic/100)`.",
            "3. **Probability Conversion**: adjusted hazard converts to death probability with `q = 1 - exp(-mu)`.",
            "4. **Event Emission**: death outcomes trigger cross-system aftermath processing.",
        ],
        "flow_title": "Data Flow: Stress -> Mortality",
        "flow_rows": flow_rows,
        "diagram_lines": [
            "```mermaid",
            "graph LR",
            "    S[Stress State] --> AL[Allostatic Load]",
            "    M0[Siler Baseline Hazard] --> HM[Adjusted Hazard]",
            "    AL --> HM",
            "    HM --> D[Death Probability]",
            "```",
        ],
        "feedback_lines": [
            "- Death events can create bereavement stressors in survivors, forming a mortality-stress feedback channel.",
        ],
        "source_files": source_files,
        "source_refs": source_refs,
    }


def _build_personality_mortality_doc(context: dict[str, Any]) -> dict[str, Any]:
    """Build Personality -> Mortality interaction content."""
    role_systems = context["role_systems"]

    flow_rows = [
        {
            "field": "personality_modifiers",
            "source": "stressor_events.*.personality_modifiers",
            "destination": "stress_system.event_scale",
            "formula": "scale *= f(axis, facet, trait)",
            "purpose": "Convert personality profile into stress sensitivity",
        },
        {
            "field": "chronic_stress",
            "source": "stress_system.event_scale accumulation",
            "destination": "stress_system.allostatic",
            "formula": "allostatic(t+1)=clamp(allostatic+inc-recovery)",
            "purpose": "Accumulate long-term physiological wear",
        },
        {
            "field": "allostatic_to_hazard",
            "source": "stress_system.allostatic",
            "destination": "mortality_system.hazard",
            "formula": "mu_adj = mu_base * (1 + alpha * allostatic/100)",
            "purpose": "Indirectly map personality to mortality risk",
        },
    ]

    system_files = _role_files(role_systems, "personality", "stress", "mortality")
    source_files = sorted(
        {
            *system_files,
            "data/stressor_events.json",
            "data/species/human/mortality/siler_parameters.json",
        }
    )

    source_refs = _merge_source_refs(
        _reference_lines_for_files(context["references"], set(system_files)),
        _formula_refs(
            context["formulas"],
            file_keywords=("stress_system", "mortality_system", "personality"),
            text_keywords=("allostatic", "hazard", "personality", "stress"),
        ),
    )

    return {
        "filename": "personality-mortality.md",
        "title": "Personality -> Mortality Indirect Pipeline",
        "description": "Indirect mortality pathway via personality-conditioned stress",
        "header": "Personality -> Mortality",
        "summary": "Personality influences mortality indirectly through stress sensitivity and allostatic load buildup.",
        "interaction_heading": "Personality -> Mortality System (Indirect)",
        "how_heading": "How Personality Reaches Mortality",
        "how_lines": [
            "1. **Personality -> Stress**: personality axes/traits alter stress event scaling.",
            "2. **Stress Integration**: repeated stress raises allostatic load over time.",
            "3. **Mortality Amplification**: allostatic load scales hazard with the stress coupling term.",
            "4. **Chain Formula**: `personality -> stress -> allostatic -> mortality`.",
        ],
        "flow_title": "Data Flow: Personality -> Mortality (via Stress)",
        "flow_rows": flow_rows,
        "diagram_lines": [
            "```mermaid",
            "graph LR",
            "    P[Personality Profile] --> ST[Stress Sensitivity]",
            "    ST --> AL[Allostatic Load]",
            "    AL --> HM[Mortality Hazard]",
            "```",
        ],
        "feedback_lines": [
            "- This path is indirect: personality has no direct mortality equation, but continuously shifts upstream stress dynamics.",
        ],
        "source_files": source_files,
        "source_refs": source_refs,
    }


def _build_events_emotion_doc(context: dict[str, Any]) -> dict[str, Any]:
    """Build Events -> Emotion interaction content."""
    emotion_presets = context["emotion_presets"]
    role_systems = context["role_systems"]
    event_presets = context["event_presets"]

    impulse_formulas = emotion_presets.get("impulse_formulas", {})
    if not isinstance(impulse_formulas, dict):
        impulse_formulas = {}

    appraisal_dims = emotion_presets.get("appraisal_dimensions", [])
    if not isinstance(appraisal_dims, list):
        appraisal_dims = []

    sample_event_name = "(none)"
    sample_event = {}
    events_map = event_presets.get("events", {}) if isinstance(event_presets, dict) else {}
    if isinstance(events_map, dict) and events_map:
        sample_event_name = sorted(events_map.keys())[0]
        raw_sample = events_map.get(sample_event_name)
        if isinstance(raw_sample, dict):
            sample_event = raw_sample

    flow_rows: list[dict[str, str]] = []
    for emotion, formula in sorted(impulse_formulas.items())[:8]:
        if not isinstance(formula, str):
            continue
        flow_rows.append(
            {
                "field": emotion,
                "source": "event_appraisal_vector (g,n,c,a,m,p,b,fr,I)",
                "destination": f"emotion_system.impulse[{emotion}]",
                "formula": formula,
                "purpose": f"Compute {emotion} impulse from event appraisal",
            }
        )

    for row in appraisal_dims[:3]:
        if not isinstance(row, dict):
            continue
        abbrev = row.get("abbrev")
        dim_id = row.get("id")
        if isinstance(abbrev, str) and isinstance(dim_id, str):
            flow_rows.append(
                {
                    "field": dim_id,
                    "source": f"event_presets.{sample_event_name}.{dim_id}",
                    "destination": f"appraisal_vector.{abbrev}",
                    "formula": "direct assignment",
                    "purpose": "Populate appraisal vector used by impulse equations",
                }
            )

    if sample_event:
        intensity = sample_event.get("intensity")
        if isinstance(intensity, (int, float)):
            flow_rows.append(
                {
                    "field": f"{sample_event_name}.intensity",
                    "source": f"event_presets.{sample_event_name}.intensity",
                    "destination": "emotion_system.impulse_scale",
                    "formula": f"I = {float(intensity):.3g}",
                    "purpose": "Scale appraisal equations by event intensity",
                }
            )

    system_files = _role_files(role_systems, "events", "emotion")
    source_files = sorted(
        {
            *system_files,
            str(emotion_presets.get("source_file", "")),
            "data/emotions/event_presets.json",
        }
        - {""}
    )

    source_refs = _merge_source_refs(
        _reference_lines_for_files(context["references"], set(system_files)),
        _formula_refs(
            context["formulas"],
            file_keywords=("emotion_system", "event"),
            text_keywords=("appraisal", "impulse", "emotion", "lazarus"),
        ),
    )

    return {
        "filename": "events-emotion.md",
        "title": "Events -> Emotion Appraisal Pipeline",
        "description": "How event appraisal vectors generate emotion impulses",
        "header": "Events -> Emotion",
        "summary": "Event presets provide appraisal vectors that are transformed into per-emotion impulses.",
        "interaction_heading": "Events -> Emotion System",
        "how_heading": "How Events Inject Emotional Impulses",
        "how_lines": [
            "1. **Appraisal Vector Build**: each event defines appraisal dimensions (`g, n, c, a, m, p, b, fr`).",
            "2. **Impulse Equations**: emotion channels are computed with formulas like `I * max(g,0)` and `I * max(-g,0)*(1-c)`.",
            "3. **Intensity Scaling**: event intensity (`I`) scales all impulse terms.",
            "4. **Trauma Handling**: trauma-tagged events can create long-lived emotional memory traces.",
        ],
        "flow_title": "Data Flow: Events -> Emotion",
        "flow_rows": flow_rows,
        "diagram_lines": [
            "```mermaid",
            "graph LR",
            "    E[Game Events] --> AV[Appraisal Vector]",
            "    AV --> J[Joy Formula]",
            "    AV --> SD[Sadness/Fear Formula]",
            "    AV --> AN[Anger/Disgust Formula]",
            "    AV --> OT[Trust/Anticipation/Surprise]",
            "    J --> EM[Emotion Impulses]",
            "    SD --> EM",
            "    AN --> EM",
            "    OT --> EM",
            "```",
        ],
        "feedback_lines": [
            f"- Sample extracted event preset used for table generation: `{sample_event_name}`.",
        ],
        "source_files": source_files,
        "source_refs": source_refs,
    }


def _build_stress_emotion_doc(context: dict[str, Any]) -> dict[str, Any]:
    """Build Stress -> Emotion interaction content."""
    decay_config = context["decay_config"]
    role_systems = context["role_systems"]

    mental_break_cfg = decay_config.get("mental_break", {})
    if not isinstance(mental_break_cfg, dict):
        mental_break_cfg = {}

    prob_formula = str(
        mental_break_cfg.get(
            "probability_formula",
            "p(break) = tick_prob / (1 + exp(-(stress - threshold) / beta))",
        )
    )

    behaviors = mental_break_cfg.get("behaviors", {})
    behavior_count = len(behaviors) if isinstance(behaviors, dict) else 0

    flow_rows = [
        {
            "field": "stress",
            "source": "stress_system.entity_state.stress",
            "destination": "mental_break_trigger",
            "formula": prob_formula,
            "purpose": "Compute per-tick mental break probability",
        },
        {
            "field": "break_type",
            "source": "mental_break_trigger.sample_behavior",
            "destination": "emotion_system.break_event",
            "formula": "emit stress-driven emotion event",
            "purpose": "Inject acute emotion impulse after break onset",
        },
        {
            "field": "allostatic_ratio",
            "source": "stress_system.entity_state.allostatic/100",
            "destination": "emotion_system.slow_layer_shift",
            "formula": "mu_shift = f(stress, allostatic)",
            "purpose": "Shift slow emotion baselines under chronic stress",
        },
        {
            "field": "post_break_emotions",
            "source": "emotion_system.fast/slow channels",
            "destination": "stress_system._calc_emotion_contribution()",
            "formula": "gamma_VA * sum(w_e * emotion_e)",
            "purpose": "Close stress-emotion feedback loop",
        },
    ]

    system_files = _role_files(role_systems, "stress", "emotion", "mental_break")
    source_files = sorted(
        {
            *system_files,
            str(decay_config.get("source_file", "")),
            "data/mental_breaks.json",
        }
        - {""}
    )

    source_refs = _merge_source_refs(
        _reference_lines_for_files(context["references"], set(system_files)),
        _formula_refs(
            context["formulas"],
            file_keywords=("stress_system", "emotion_system", "mental_break_system"),
            text_keywords=("mental break", "allostatic", "emotion", "stress"),
        ),
    )

    return {
        "filename": "stress-emotion.md",
        "title": "Stress -> Emotion Feedback Pipeline",
        "description": "How stress triggers mental-break and emotion injection feedback",
        "header": "Stress -> Emotion",
        "summary": "Stress can trigger mental-break behavior and inject new emotion impulses, creating recursive feedback.",
        "interaction_heading": "Stress -> Emotion System",
        "how_heading": "How Stress Feeds Back Into Emotion",
        "how_lines": [
            f"1. **Mental Break Trigger**: break probability follows `{prob_formula}`.",
            "2. **Behavior Routing**: sampled break behavior drives emotion/event injection pathways.",
            "3. **Baseline Shift**: sustained stress/allostatic load shifts slow emotional targets.",
            "4. **Loop Closure**: injected emotions feed back into stress contribution equations.",
        ],
        "flow_title": "Data Flow: Stress -> Emotion",
        "flow_rows": flow_rows,
        "diagram_lines": [
            "```mermaid",
            "graph LR",
            "    ST[Stress State] --> MB[Mental Break Probability]",
            "    MB --> BT[Break Type Selection]",
            "    BT --> EI[Emotion Injection]",
            "    ST --> MU[Slow Baseline Shift]",
            "    EI --> EM[Emotion State]",
            "    MU --> EM",
            "    EM --> ST",
            "```",
        ],
        "feedback_lines": [
            f"- Extracted mental-break behavior templates available: {behavior_count}.",
            "- Core loop: stress -> mental break -> emotion inject -> stress.",
        ],
        "source_files": source_files,
        "source_refs": source_refs,
    }


def _build_pair_markdown(page: dict[str, Any], nav_order: int, lang: str) -> str:
    """Render one pair interaction markdown page."""
    source_files = page.get("source_files", [])
    if not source_files:
        source_files = ["(none)"]

    flow_table = _build_data_flow_table(page.get("flow_rows", []))
    source_lines = _source_refs_block(page.get("source_refs", []))

    return "\n".join(
        [
            "---",
            f"title: \"{page['title']}\"",
            f"description: \"{page['description']}\"",
            "generated: true",
            "source_files:",
            *[f"  - \"{item}\"" for item in source_files],
            f"nav_order: {nav_order}",
            "---",
            "",
            f"# {page['header']}",
            "",
            "한국어 / English: 계산 파이프라인 중심 상호작용 문서 / Calculation-pipeline interaction documentation.",
            "",
            f"## {t('section_interaction_overview', lang)}",
            str(page.get("summary", "")),
            "",
            f"## {page['interaction_heading']}",
            f"### {page['how_heading']}",
            *page.get("how_lines", []),
            "",
            f"### {page['flow_title']}",
            *flow_table,
            "",
            f"## {t('section_calculation_flow_diagram', lang)}",
            *page.get("diagram_lines", []),
            "",
            f"## {t('section_feedback_loops', lang)}",
            *page.get("feedback_lines", ["- None"]),
            "",
            f"## {t('section_source_notes', lang)}",
            *source_lines,
            "",
            f"## {t('section_manual_notes', lang)}",
            "<!-- MANUAL:START -->",
            "<!-- MANUAL:END -->",
            "",
        ]
    )


def _build_index_markdown(pages: list[dict[str, Any]], lang: str) -> str:
    """Render master interaction index with required dependency graph."""
    table_lines = [
        "| Interaction Pair | Output Page |",
        "|---|---|",
    ]
    for page in pages:
        pair_label = page["header"].replace("->", "→")
        table_lines.append(
            f"| `{pair_label}` | [{page['filename']}]({page['filename']}) |"
        )

    return "\n".join(
        [
            "---",
            "title: \"System Interaction Index\"",
            "description: \"Master calculation-pipeline dependency graph\"",
            "generated: true",
            "source_files:",
            "  - \"extracted/references.json\"",
            "  - \"extracted/systems.json\"",
            "  - \"extracted/formulas.json\"",
            "  - \"extracted/stressor_data.json\"",
            "  - \"extracted/decay_config.json\"",
            "  - \"extracted/emotion_presets.json\"",
            "nav_order: 1",
            "---",
            "",
            "# System Interaction Index",
            "",
            "한국어 / English: 시스템 계산 의존 그래프 / System calculation dependency graph.",
            "",
            f"Generated {len(pages)} calculation-pipeline interaction pages.",
            "",
            f"## {t('section_system_dependency_graph', lang)}",
            "```mermaid",
            "graph TD",
            "    PERS[Personality System] -->|sensitivity, baselines| EMOT[Emotion System]",
            "    PERS -->|modifier weights| STRESS[Stress System]",
            "    EVENTS[Game Events] -->|appraisal vectors| EMOT",
            "    EMOT -->|emotion values| STRESS",
            "    STRESS -->|allostatic load| MORT[Mortality System]",
            "    STRESS -->|mental break| EMOT",
            "    MORT -->|death event| STRESS",
            "    MORT -->|death event| EMOT",
            "```",
            "",
            f"## {t('section_interaction_pages', lang)}",
            *table_lines,
            "",
            f"## {t('section_feedback_loops', lang)}",
            "- stress -> mental break -> emotion inject -> more stress",
            "- death event -> bereavement stressor -> stress -> allostatic load -> mortality",
            "",
            f"## {t('section_manual_notes', lang)}",
            "<!-- MANUAL:START -->",
            "<!-- MANUAL:END -->",
            "",
        ]
    )


def run(manifest: dict, extracted: dict | None = None, lang: str = "ko") -> dict:
    """Generate calculation-pipeline interaction pages and master dependency index.

    Args:
        manifest: The manifest.json data from Phase 1.
        extracted: Optional extracted payload cache from phase3 orchestrator.

    Returns:
        dict with standard generator result fields.
    """
    files_written: list[str] = []
    warnings: list[str] = []
    errors: list[str] = []

    references = _load_payload(extracted, "references", "references.json", warnings)
    systems_doc = _load_payload(extracted, "systems", "systems.json", warnings)
    formulas = _load_payload(extracted, "formulas", "formulas.json", warnings)
    stressor_data = _load_payload(extracted, "stressor_data", "stressor_data.json", warnings)
    decay_config = _load_payload(extracted, "decay_config", "decay_config.json", warnings)
    emotion_presets = _load_payload(extracted, "emotion_presets", "emotion_presets.json", warnings)
    trait_data = _load_payload(extracted, "trait_data", "trait_data.json", warnings)
    data_files = _load_payload(extracted, "data_files", "data_files.json", warnings)

    systems = _collect_systems(manifest, systems_doc)
    if not systems:
        warnings.append("No systems discovered from manifest/systems.json; using extracted data-only docs.")

    role_systems = _collect_role_systems(systems)

    siler_parameters = _find_data_file_content(
        data_files,
        "data/species/human/mortality/siler_parameters.json",
    )
    event_presets = _find_data_file_content(
        data_files,
        "data/emotions/event_presets.json",
    )

    context = {
        "references": references,
        "formulas": formulas,
        "stressor_data": stressor_data,
        "decay_config": decay_config,
        "emotion_presets": emotion_presets,
        "trait_data": trait_data,
        "data_files": data_files,
        "role_systems": role_systems,
        "siler_parameters": siler_parameters,
        "event_presets": event_presets,
    }

    pages = [
        _build_personality_emotion_doc(context),
        _build_personality_stress_doc(context),
        _build_emotion_stress_doc(context),
        _build_stress_mortality_doc(context),
        _build_personality_mortality_doc(context),
        _build_events_emotion_doc(context),
        _build_stress_emotion_doc(context),
    ]

    dirs = config.lang_dirs(lang)
    interactions_dir = dirs["interactions"]
    config.ensure_dir(interactions_dir)

    expected = {page["filename"] for page in pages}
    for filename in os.listdir(interactions_dir):
        if filename in expected:
            continue
        if not filename.endswith(".md") or filename == "_index.md":
            continue
        path = os.path.join(interactions_dir, filename)
        if os.path.isfile(path):
            is_generated = False
            try:
                with open(path, "r", encoding="utf-8") as f:
                    existing = f.read()
                frontmatter_match = re.match(r"^---\n(.*?)\n---", existing, re.DOTALL)
                if frontmatter_match:
                    frontmatter = frontmatter_match.group(1).lower()
                    is_generated = "generated: true" in frontmatter
            except OSError as exc:
                warnings.append(f"Failed to inspect stale interaction page {path}: {exc}")
                continue

            if is_generated:
                try:
                    os.remove(path)
                except OSError as exc:
                    warnings.append(f"Failed to remove stale interaction page {path}: {exc}")
            else:
                warnings.append(f"Skipping non-generated interaction page: {path}")

    items_processed = 0
    for nav_order, page in enumerate(pages, start=10):
        output_path = os.path.join(interactions_dir, page["filename"])
        content = _build_pair_markdown(page, nav_order, lang)
        if _write_markdown(output_path, content, warnings):
            files_written.append(output_path)
            items_processed += 1

    index_path = os.path.join(interactions_dir, "_index.md")
    index_content = _build_index_markdown(pages, lang)
    if _write_markdown(index_path, index_content, warnings):
        files_written.append(index_path)

    return {
        "files_written": files_written,
        "items_processed": items_processed,
        "warnings": warnings,
        "errors": errors,
    }
