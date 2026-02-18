"""Generate HEXACO trait documentation pages from extracted trait data."""

from __future__ import annotations

import json
import os
import re
from typing import Any

import scripts.config as config


_MANUAL_BLOCK_RE = re.compile(r"<!-- MANUAL:START -->.*?<!-- MANUAL:END -->", re.DOTALL)
_AXIS_ORDER = {code: index for index, code in enumerate("HEXACO", start=1)}
_VALENCE_EMOJI = {
    "positive": "✅",
    "negative": "❌",
    "neutral": "➖",
}
_TYPE_DESCRIPTIONS = {
    "personality": "Standard facet-threshold traits",
    "dark": "Dark triad/tetrad traits (composite conditions)",
    "composite": "Multi-condition traits",
}


def _yaml_quote(value: str) -> str:
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def _md_cell(value: Any) -> str:
    text = str(value)
    return text.replace("|", r"\|").replace("\n", " ")


def _normalize_text(value: Any) -> str:
    if not isinstance(value, str):
        return ""
    return " ".join(value.split()).strip()


def _format_number(value: Any) -> str:
    if isinstance(value, bool):
        return str(value)
    if isinstance(value, int):
        return str(value)
    if isinstance(value, float):
        if value.is_integer():
            return str(int(value))
        return f"{value:.4f}".rstrip("0").rstrip(".")
    return str(value)


def _is_number(value: Any) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def _unique_strings(values: list[Any]) -> list[str]:
    seen: set[str] = set()
    output: list[str] = []
    for value in values:
        if not isinstance(value, str):
            continue
        if value in seen:
            continue
        seen.add(value)
        output.append(value)
    return output


def _manual_block(text: str) -> str:
    match = _MANUAL_BLOCK_RE.search(text)
    return match.group(0) if match else ""


def _merge_manual_blocks(generated: str, existing: str) -> str:
    existing_block = _manual_block(existing)
    if not existing_block:
        return generated

    if _MANUAL_BLOCK_RE.search(generated):
        return _MANUAL_BLOCK_RE.sub(existing_block, generated, count=1)

    return generated.rstrip() + "\n\n" + existing_block + "\n"


def _write_markdown(path: str, content: str, warnings: list[str], errors: list[str]) -> bool:
    existing = ""
    if os.path.exists(path):
        try:
            with open(path, "r", encoding="utf-8") as handle:
                existing = handle.read()
        except OSError as exc:
            warnings.append(f"Failed to read existing markdown for MANUAL merge ({path}): {exc}")

    final_content = _merge_manual_blocks(content, existing)
    try:
        with open(path, "w", encoding="utf-8") as handle:
            handle.write(final_content)
            if not final_content.endswith("\n"):
                handle.write("\n")
    except OSError as exc:
        errors.append(f"Failed to write markdown ({path}): {exc}")
        return False
    return True


def _frontmatter(
    title: str,
    description: str,
    nav_order: int,
    source_files: list[str],
) -> str:
    lines = [
        "---",
        f"title: {_yaml_quote(title)}",
        f"description: {_yaml_quote(description)}",
        "generated: true",
        "source_files:",
    ]

    if source_files:
        for source_file in source_files:
            lines.append(f"  - {_yaml_quote(source_file)}")
    else:
        lines.append("  - \"extracted/trait_data.json\"")

    lines.extend(
        [
            f"nav_order: {nav_order}",
            "---",
            "",
        ]
    )
    return "\n".join(lines)


def _render_markdown_table(headers: list[str], rows: list[list[Any]]) -> str:
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(["---"] * len(headers)) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(_md_cell(cell) for cell in row) + " |")
    return "\n".join(lines)


def _axis_codes(hexaco_axes: dict[str, Any], by_axis: dict[str, Any]) -> list[str]:
    del hexaco_axes
    del by_axis
    return list(_AXIS_ORDER.keys())


def _axis_description(axis_info: dict[str, Any], axis_code: str, axis_name: str) -> str:
    description = _normalize_text(axis_info.get("description"))
    if description:
        return description
    description = _normalize_text(axis_info.get("description_en"))
    if description:
        return description
    return f"personality tendencies represented by the `{axis_code}` axis in the HEXACO model"


def _facet_list_text(axis_info: dict[str, Any]) -> str:
    facets = axis_info.get("facets")
    if not isinstance(facets, dict) or not facets:
        return "n/a"

    tokens: list[str] = []
    for facet_id in sorted(facets.keys()):
        facet_meta = facets.get(facet_id)
        if not isinstance(facet_id, str):
            continue

        if isinstance(facet_meta, dict):
            name_en = _normalize_text(facet_meta.get("name"))
            name_kr = _normalize_text(facet_meta.get("name_kr"))
        else:
            name_en = ""
            name_kr = ""

        if name_en and name_kr:
            tokens.append(f"`{facet_id}` ({name_kr} / {name_en})")
        elif name_en:
            tokens.append(f"`{facet_id}` ({name_en})")
        elif name_kr:
            tokens.append(f"`{facet_id}` ({name_kr})")
        else:
            tokens.append(f"`{facet_id}`")

    return ", ".join(tokens) if tokens else "n/a"


def _condition_text(condition: dict[str, Any]) -> str:
    if not isinstance(condition, dict):
        return "Unknown condition metadata"

    facet = condition.get("facet")
    direction = condition.get("direction")
    threshold = condition.get("threshold")

    if isinstance(facet, str) and facet:
        parts = [f"Facet `{facet}`"]
        if isinstance(direction, str) and direction:
            parts.append(f"direction `{direction}`")
        if threshold is not None:
            parts.append(f"threshold `{_format_number(threshold)}`")
        return " ".join(parts)

    serialized = json.dumps(condition, ensure_ascii=False)
    return serialized if len(serialized) <= 120 else serialized[:117] + "..."


def _activation_lines(condition: Any) -> list[str]:
    if isinstance(condition, dict):
        all_conditions = condition.get("all")
        if isinstance(all_conditions, list) and all_conditions:
            lines: list[str] = []
            for item in all_conditions:
                if isinstance(item, dict):
                    lines.append(f"- {_condition_text(item)}")
                else:
                    lines.append(f"- {_md_cell(item)}")
            return lines
        return [f"- {_condition_text(condition)}"]

    return ["- Unknown condition metadata"]


def _format_pct_delta(value: float) -> str:
    return f"{abs((value - 1.0) * 100):.0f}%"


def _effect_meaning(category: str, effect: str, value: Any) -> str:
    if category == "Stress" and effect.startswith("violation:"):
        action = effect.split(":", 1)[1].strip()
        return f"+{_format_number(value)} stress when {action}"

    if not _is_number(value):
        return "n/a"

    effect_label = effect.replace("_", " ")
    if category == "Behavior":
        effect_label = f"{effect_label} weight"
    if value > 1.0:
        return f"+{_format_pct_delta(value)} {effect_label}"
    if value < 1.0:
        return f"-{_format_pct_delta(value)} {effect_label}"
    return "no change"


def _effect_rows(effects: Any) -> list[list[str]]:
    if not isinstance(effects, dict):
        return []

    rows: list[list[str]] = []
    category_map = {
        "behavior_weights": "Behavior",
        "emotion_modifiers": "Emotion",
        "relationship_modifiers": "Relationship",
        "work_modifiers": "Work",
        "combat_modifiers": "Combat",
    }

    for effect_key, category_name in category_map.items():
        payload = effects.get(effect_key)
        if not isinstance(payload, dict):
            continue
        for name in sorted(payload.keys()):
            value = payload.get(name)
            rows.append(
                [
                    category_name,
                    name,
                    _format_number(value),
                    _effect_meaning(category_name, name, value),
                ]
            )

    stress_payload = effects.get("stress_modifiers")
    if isinstance(stress_payload, dict):
        for name in sorted(stress_payload.keys()):
            if name == "violation_stress":
                continue
            value = stress_payload.get(name)
            rows.append(
                [
                    "Stress",
                    name,
                    _format_number(value),
                    _effect_meaning("Stress", name, value),
                ]
            )

        violation = stress_payload.get("violation_stress")
        if isinstance(violation, dict):
            for action in sorted(violation.keys()):
                value = violation.get(action)
                rows.append(
                    [
                        "Stress",
                        f"violation: {action}",
                        _format_number(value),
                        _effect_meaning("Stress", f"violation: {action}", value),
                    ]
                )

    return rows


def _behavior_summaries(effects: Any) -> tuple[list[str], list[str]]:
    amplified: list[str] = []
    suppressed: list[str] = []

    if not isinstance(effects, dict):
        return amplified, suppressed

    behavior = effects.get("behavior_weights")
    if not isinstance(behavior, dict):
        return amplified, suppressed

    for action in sorted(behavior.keys()):
        value = behavior.get(action)
        if not _is_number(value):
            continue
        if value > 1.0:
            amplified.append(action)
        elif value < 1.0:
            suppressed.append(action)

    return amplified, suppressed


def _emotion_summaries(effects: Any) -> list[str]:
    if not isinstance(effects, dict):
        return []
    emotion = effects.get("emotion_modifiers")
    if not isinstance(emotion, dict):
        return []

    output: list[str] = []
    for name in sorted(emotion.keys()):
        value = emotion.get(name)
        if _is_number(value) and value != 1.0:
            output.append(f"{name} ({_format_number(value)})")
    return output


def _violation_summaries(effects: Any) -> list[str]:
    if not isinstance(effects, dict):
        return []
    stress = effects.get("stress_modifiers")
    if not isinstance(stress, dict):
        return []
    violation = stress.get("violation_stress")
    if not isinstance(violation, dict):
        return []

    output: list[str] = []
    for action in sorted(violation.keys()):
        value = violation.get(action)
        output.append(f"{action} (+{_format_number(value)})")
    return output


def _trait_link(
    target_id: str,
    current_axis: str,
    trait_axis_by_id: dict[str, str],
) -> str:
    target_axis = trait_axis_by_id.get(target_id, "")
    if not target_axis:
        return f"`{target_id}`"
    if target_axis == current_axis:
        return f"[`{target_id}`](#{target_id})"
    return f"[`{target_id}`]({target_axis}.md#{target_id})"


def _axis_table_rows(
    axis_codes: list[str],
    hexaco_axes: dict[str, Any],
    by_axis: dict[str, list[str]],
    trait_by_id: dict[str, dict[str, Any]],
) -> list[list[Any]]:
    rows: list[list[Any]] = []
    for axis_code in axis_codes:
        axis_meta = hexaco_axes.get(axis_code, {}) if isinstance(hexaco_axes, dict) else {}
        axis_name = _normalize_text(axis_meta.get("name")) or axis_code
        axis_name_kr = _normalize_text(axis_meta.get("name_kr")) or "-"
        trait_ids = by_axis.get(axis_code, []) if isinstance(by_axis, dict) else []

        positive = 0
        negative = 0
        for trait_id in trait_ids:
            trait = trait_by_id.get(trait_id, {})
            valence = str(trait.get("valence", "")).lower()
            if valence == "positive":
                positive += 1
            elif valence == "negative":
                negative += 1

        rows.append([axis_code, axis_name, axis_name_kr, len(trait_ids), positive, negative])

    return rows


def _type_table_rows(by_type: dict[str, Any]) -> list[list[Any]]:
    rows: list[list[Any]] = []
    seen: set[str] = set()

    ordered_types = ["personality", "dark", "composite"]
    for trait_type in ordered_types:
        ids = by_type.get(trait_type, []) if isinstance(by_type, dict) else []
        count = len(ids) if isinstance(ids, list) else 0
        label = trait_type.title()
        rows.append([label, count, _TYPE_DESCRIPTIONS.get(trait_type, "Trait category")])
        seen.add(trait_type)

    if isinstance(by_type, dict):
        for trait_type in sorted(by_type.keys()):
            if not isinstance(trait_type, str) or trait_type in seen:
                continue
            ids = by_type.get(trait_type, [])
            count = len(ids) if isinstance(ids, list) else 0
            rows.append([trait_type.title(), count, "Trait category"])

    return rows


def _top_synergy_traits(synergy_graph: dict[str, Any], limit: int = 20) -> list[str]:
    ranked: list[tuple[int, str]] = []
    for trait_id, links in synergy_graph.items():
        if not isinstance(trait_id, str):
            continue
        if not isinstance(links, dict):
            continue
        synergy = links.get("synergies") if isinstance(links.get("synergies"), list) else []
        anti = links.get("anti_synergies") if isinstance(links.get("anti_synergies"), list) else []
        connection_count = len(_unique_strings(synergy + anti))
        ranked.append((connection_count, trait_id))

    ranked.sort(key=lambda item: (-item[0], item[1]))
    return [trait_id for _, trait_id in ranked[:limit]]


def _render_synergy_mermaid(synergy_graph: dict[str, Any]) -> str:
    selected = _top_synergy_traits(synergy_graph, limit=20)
    lines = ["```mermaid", "graph LR"]

    if not selected:
        lines.append("  %% No synergy data extracted")
        lines.append("```")
        return "\n".join(lines)

    node_ids = {trait_id: f"t{index}" for index, trait_id in enumerate(selected)}
    for trait_id in selected:
        lines.append(f"  {node_ids[trait_id]}[\"{trait_id}\"]")

    has_edges = False
    for trait_id in selected:
        links = synergy_graph.get(trait_id, {})
        if not isinstance(links, dict):
            continue

        synergy_targets = links.get("synergies") if isinstance(links.get("synergies"), list) else []
        anti_targets = links.get("anti_synergies") if isinstance(links.get("anti_synergies"), list) else []

        for target in _unique_strings(synergy_targets):
            if target not in node_ids or target == trait_id:
                continue
            lines.append(f"  {node_ids[trait_id]} -->|synergy| {node_ids[target]}")
            has_edges = True

        for target in _unique_strings(anti_targets):
            if target not in node_ids or target == trait_id:
                continue
            lines.append(f"  {node_ids[trait_id]} -.->|conflict| {node_ids[target]}")
            has_edges = True

    if not has_edges:
        lines.append("  %% Top traits have no intra-group links")

    lines.append("```")
    return "\n".join(lines)


def _render_index_page(
    trait_data: dict[str, Any],
    trait_by_id: dict[str, dict[str, Any]],
    axis_codes: list[str],
    source_files: list[str],
) -> str:
    hexaco_axes = trait_data.get("hexaco_axes") if isinstance(trait_data.get("hexaco_axes"), dict) else {}
    by_axis = trait_data.get("by_axis") if isinstance(trait_data.get("by_axis"), dict) else {}
    by_type = trait_data.get("by_type") if isinstance(trait_data.get("by_type"), dict) else {}
    synergy_graph = (
        trait_data.get("synergy_graph") if isinstance(trait_data.get("synergy_graph"), dict) else {}
    )

    stats = trait_data.get("stats") if isinstance(trait_data.get("stats"), dict) else {}
    total_traits = stats.get("total_traits")
    if not isinstance(total_traits, int):
        total_traits = len(trait_by_id)

    lines: list[str] = [
        _frontmatter(
            title="Personality Traits",
            description="HEXACO trait overview with axis grouping and synergy network.",
            nav_order=10,
            source_files=source_files,
        ),
        "# Personality Traits",
        "",
        f"The WorldSim personality system uses **{total_traits} discrete traits** activated by HEXACO personality axes.",
        "Traits modify emotion sensitivity, behavior weights, stress responses, and social interactions.",
        "",
        "**Model basis**: Ashton & Lee (2007) HEXACO Personality Model, with extensions for dark triad traits and composite conditions.",
        "",
        "## Overview",
        "",
        _render_markdown_table(
            ["HEXACO Axis", "Name (EN)", "Name (KR)", "Traits", "Positive", "Negative"],
            _axis_table_rows(axis_codes, hexaco_axes, by_axis, trait_by_id),
        ),
        "",
        "## Trait Types",
        "",
        _render_markdown_table(
            ["Type", "Count", "Description"],
            _type_table_rows(by_type),
        ),
        "",
        "## How Traits Work",
        "",
        "1. **Activation**: Each entity's HEXACO personality scores are checked against trait conditions.",
        "2. **Threshold**: A trait activates when a facet score is above (`high`) or below (`low`) the threshold.",
        "3. **Effects**: Active traits modify behavior weights, emotion sensitivity, stress responses, and social interactions.",
        "4. **Synergies**: Some traits amplify each other's effects; anti-synergies create internal conflict.",
        "",
        "## Axis Pages",
        "",
    ]

    for axis_code in axis_codes:
        axis_meta = hexaco_axes.get(axis_code, {}) if isinstance(hexaco_axes, dict) else {}
        axis_name = _normalize_text(axis_meta.get("name")) or axis_code
        axis_name_kr = _normalize_text(axis_meta.get("name_kr"))
        if axis_name_kr:
            lines.append(f"- [{axis_name} ({axis_code}) - {axis_name_kr}]({axis_code}.md)")
        else:
            lines.append(f"- [{axis_name} ({axis_code})]({axis_code}.md)")

    lines.extend(
        [
            "",
            "## Synergy Network (Top 20 Connected Traits)",
            "",
            _render_synergy_mermaid(synergy_graph),
            "",
            "📄 source: `extracted/trait_data.json`",
            "",
            "## Manual Notes",
            "",
            "<!-- MANUAL:START -->",
            "<!-- MANUAL:END -->",
            "",
        ]
    )

    return "\n".join(lines)


def _render_axis_page(
    axis_code: str,
    axis_info: dict[str, Any],
    trait_ids: list[str],
    trait_by_id: dict[str, dict[str, Any]],
    trait_axis_by_id: dict[str, str],
    source_files: list[str],
) -> str:
    axis_name = _normalize_text(axis_info.get("name")) or axis_code
    axis_name_kr = _normalize_text(axis_info.get("name_kr")) or "-"
    axis_description = _axis_description(axis_info, axis_code, axis_name)
    facets_text = _facet_list_text(axis_info)

    nav_order = 10 + _AXIS_ORDER.get(axis_code, 90)
    title = f"{axis_name} ({axis_code}) Traits"

    lines: list[str] = [
        _frontmatter(
            title=title,
            description=f"Trait breakdown for {axis_name} ({axis_code}).",
            nav_order=nav_order,
            source_files=source_files,
        ),
        f"# {axis_name} ({axis_code}) — {axis_name_kr}",
        "",
        "## Axis Overview",
        "",
        f"The **{axis_name}** axis measures {axis_description}.",
        f"**Facets**: {facets_text}",
        "",
        "## Traits",
        "",
    ]

    rendered_count = 0
    for trait_id in trait_ids:
        trait = trait_by_id.get(trait_id)
        if not isinstance(trait, dict):
            continue

        rendered_count += 1
        name_en = _normalize_text(trait.get("name_en")) or trait_id
        name_kr = _normalize_text(trait.get("name_kr")) or "-"
        trait_type = _normalize_text(trait.get("type")) or "unknown"
        valence = _normalize_text(trait.get("valence")).lower() or "neutral"
        valence_emoji = _VALENCE_EMOJI.get(valence, "➖")

        lines.append(f"<a id=\"{trait_id}\"></a>")
        lines.append(f"### {name_en} ({name_kr}) — `{trait_id}`")
        lines.append("")
        lines.append(f"**Type**: {trait_type} | **Valence**: {valence_emoji} {valence}")
        lines.append("")

        lines.append("**Activation Condition**:")
        lines.extend(_activation_lines(trait.get("condition")))
        lines.append("")

        lines.append("**Effects**:")
        lines.append("")
        effect_rows = _effect_rows(trait.get("effects"))
        if effect_rows:
            lines.append(
                _render_markdown_table(
                    ["Category", "Effect", "Value", "Meaning"],
                    effect_rows,
                )
            )
        else:
            lines.append("No effect modifiers extracted.")
        lines.append("")

        amplified, suppressed = _behavior_summaries(trait.get("effects"))
        emotion_sensitivities = _emotion_summaries(trait.get("effects"))
        violation_triggers = _violation_summaries(trait.get("effects"))

        lines.append(
            "**Amplified behaviors**: "
            + (", ".join(f"`{item}`" for item in amplified) if amplified else "none")
        )
        lines.append(
            "**Suppressed behaviors**: "
            + (", ".join(f"`{item}`" for item in suppressed) if suppressed else "none")
        )
        lines.append(
            "**Emotion sensitivities**: "
            + (", ".join(f"`{item}`" for item in emotion_sensitivities) if emotion_sensitivities else "none")
        )
        lines.append(
            "**Violation stress triggers**: "
            + (
                ", ".join(f"`{item}`" for item in violation_triggers)
                if violation_triggers
                else "none"
            )
        )
        lines.append("")

        synergies = _unique_strings(trait.get("synergies") if isinstance(trait.get("synergies"), list) else [])
        anti_synergies = _unique_strings(
            trait.get("anti_synergies") if isinstance(trait.get("anti_synergies"), list) else []
        )

        lines.append(
            "**Synergies**: "
            + (
                ", ".join(_trait_link(item, axis_code, trait_axis_by_id) for item in synergies)
                if synergies
                else "none"
            )
        )
        lines.append(
            "**Anti-synergies**: "
            + (
                ", ".join(_trait_link(item, axis_code, trait_axis_by_id) for item in anti_synergies)
                if anti_synergies
                else "none"
            )
        )
        lines.append("")
        lines.append("📄 source: `extracted/trait_data.json`")
        lines.append("")
        lines.append("---")
        lines.append("")

    if rendered_count == 0:
        lines.append("No traits extracted for this axis.")
        lines.append("")

    lines.extend(
        [
            "## Manual Notes",
            "",
            "<!-- MANUAL:START -->",
            "<!-- MANUAL:END -->",
            "",
        ]
    )

    return "\n".join(lines)


def run(manifest: dict, extracted: dict) -> dict:
    """Generate trait documentation pages from extracted trait data.

    Args:
        manifest: The manifest.json payload (unused but part of generator contract).
        extracted: Aggregated extracted payloads containing key ``trait_data``.

    Returns:
        dict with keys:
            - files_written: list[str]
            - pages_generated: int
            - warnings: list[str]
            - errors: list[str]
    """
    del manifest

    warnings: list[str] = []
    errors: list[str] = []
    files_written: list[str] = []

    if not isinstance(extracted, dict):
        warnings.append("extracted payload is not a dict; trait pages not generated")
        return {
            "files_written": files_written,
            "pages_generated": 0,
            "items_processed": 0,
            "warnings": warnings,
            "errors": errors,
        }

    trait_data = extracted.get("trait_data")
    if not isinstance(trait_data, dict):
        warnings.append("trait_data not available in extracted payload; trait pages not generated")
        return {
            "files_written": files_written,
            "pages_generated": 0,
            "items_processed": 0,
            "warnings": warnings,
            "errors": errors,
        }

    traits_payload = trait_data.get("traits")
    traits = traits_payload if isinstance(traits_payload, list) else []
    if not isinstance(traits_payload, list):
        warnings.append("trait_data.traits missing or invalid; using empty list")

    trait_by_id: dict[str, dict[str, Any]] = {}
    trait_axis_by_id: dict[str, str] = {}

    for item in traits:
        if not isinstance(item, dict):
            continue
        trait_id = item.get("id")
        if not isinstance(trait_id, str) or not trait_id:
            continue
        trait_by_id[trait_id] = item

        axis_code = _normalize_text(item.get("axis")).upper()
        if axis_code:
            trait_axis_by_id[trait_id] = axis_code

    hexaco_axes = trait_data.get("hexaco_axes") if isinstance(trait_data.get("hexaco_axes"), dict) else {}
    by_axis_raw = trait_data.get("by_axis") if isinstance(trait_data.get("by_axis"), dict) else {}

    by_axis: dict[str, list[str]] = {}
    for axis_code, raw_ids in by_axis_raw.items():
        if not isinstance(axis_code, str):
            continue
        normalized_axis = axis_code.strip().upper()
        if not normalized_axis:
            continue
        if isinstance(raw_ids, list):
            ids = [trait_id for trait_id in raw_ids if isinstance(trait_id, str) and trait_id in trait_by_id]
        else:
            ids = []
        by_axis[normalized_axis] = _unique_strings(ids)

    for trait_id, trait in trait_by_id.items():
        axis_code = _normalize_text(trait.get("axis")).upper()
        if not axis_code:
            continue
        by_axis.setdefault(axis_code, [])
        if trait_id not in by_axis[axis_code]:
            by_axis[axis_code].append(trait_id)

    axis_codes = _axis_codes(hexaco_axes, by_axis)

    source_files = ["extracted/trait_data.json"]
    raw_source_file = _normalize_text(trait_data.get("source_file"))
    if raw_source_file:
        source_files.append(raw_source_file)

    traits_dir = os.path.join(config.CONTENT_DIR, "traits")
    config.ensure_dir(traits_dir)

    index_content = _render_index_page(
        trait_data=trait_data,
        trait_by_id=trait_by_id,
        axis_codes=axis_codes,
        source_files=source_files,
    )
    index_path = os.path.join(traits_dir, "_index.md")
    if _write_markdown(index_path, index_content, warnings, errors):
        files_written.append(index_path)

    for axis_code in axis_codes:
        axis_info = hexaco_axes.get(axis_code)
        if not isinstance(axis_info, dict):
            axis_info = {}

        trait_ids = by_axis.get(axis_code, [])
        axis_content = _render_axis_page(
            axis_code=axis_code,
            axis_info=axis_info,
            trait_ids=trait_ids,
            trait_by_id=trait_by_id,
            trait_axis_by_id=trait_axis_by_id,
            source_files=source_files,
        )
        axis_path = os.path.join(traits_dir, f"{axis_code}.md")
        if _write_markdown(axis_path, axis_content, warnings, errors):
            files_written.append(axis_path)

    return {
        "files_written": files_written,
        "pages_generated": len(files_written),
        "items_processed": len(files_written),
        "warnings": warnings,
        "errors": errors,
    }
