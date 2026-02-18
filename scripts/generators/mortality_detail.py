"""Generate detailed mortality system documentation from extracted pipeline data."""

from __future__ import annotations

import math
import os
import re
from typing import Any

import scripts.config as config


MANUAL_START = "<!-- MANUAL:START -->"
MANUAL_END = "<!-- MANUAL:END -->"
MANUAL_BLOCK_RE = re.compile(r"<!-- MANUAL:START -->.*?<!-- MANUAL:END -->", re.DOTALL)
SAMPLE_AGES = (0, 1, 5, 20, 50, 70, 90)


def _to_float(value: Any) -> float | None:
    if isinstance(value, (int, float)):
        return float(value)
    if isinstance(value, str):
        token = value.strip().replace("_", "")
        if not token:
            return None
        try:
            return float(token)
        except ValueError:
            return None
    return None


def _as_dict(value: Any) -> dict[str, Any]:
    if isinstance(value, dict):
        return value
    return {}


def _collect_entries(payload: Any, list_keys: tuple[str, ...]) -> list[dict[str, Any]]:
    if isinstance(payload, list):
        return [item for item in payload if isinstance(item, dict)]
    if not isinstance(payload, dict):
        return []

    for key in list_keys:
        raw = payload.get(key)
        if isinstance(raw, list):
            return [item for item in raw if isinstance(item, dict)]
    return []


def _format_decimal(value: float | None, digits: int = 3) -> str:
    if value is None:
        return "n/a"
    return f"{value:.{digits}f}"


def _format_pct(prob: float) -> str:
    pct = prob * 100.0
    if pct >= 10:
        return f"{pct:.1f}%"
    if pct >= 1:
        return f"{pct:.2f}%"
    if pct >= 0.1:
        return f"{pct:.3f}%"
    return f"{pct:.4f}%"


def _escape_md(value: Any) -> str:
    return str(value).replace("|", r"\|").replace("\n", " ")


def _yaml_quote(text: str) -> str:
    escaped = text.replace("\\", "\\\\").replace('"', r'\"')
    return f'"{escaped}"'


def _find_siler_data_file(data_files_payload: Any) -> tuple[dict[str, Any], dict[str, Any]]:
    entries = _collect_entries(data_files_payload, ("files", "data_files"))
    for entry in entries:
        file_path = str(entry.get("file", "")).lower()
        if "siler_parameters" in file_path:
            content = (
                entry.get("full_content")
                or entry.get("content")
                or entry.get("parsed")
                or entry.get("data")
            )
            return entry, _as_dict(content)
    return {}, {}


def _find_mortality_system(systems_payload: Any) -> dict[str, Any]:
    entries = _collect_entries(systems_payload, ("systems",))
    for entry in entries:
        file_path = str(entry.get("file", "")).lower()
        system_name = str(entry.get("system_name", "")).lower()
        if "mortality_system.gd" in file_path or system_name == "mortality":
            return entry
    return {}


def _constant_lookup(constants_payload: Any) -> dict[str, tuple[Any, int | None]]:
    entries = _collect_entries(constants_payload, ("constants",))
    lookup: dict[str, tuple[Any, int | None]] = {}
    for entry in entries:
        name = entry.get("name")
        if not isinstance(name, str) or not name:
            continue
        line = entry.get("line")
        line_num = line if isinstance(line, int) else None
        lookup[name] = (entry.get("value"), line_num)
    return lookup


def _class_var_lookup(system_entry: dict[str, Any]) -> dict[str, tuple[str, int | None]]:
    lookup: dict[str, tuple[str, int | None]] = {}
    for entry in system_entry.get("class_variables", []):
        if not isinstance(entry, dict):
            continue
        name = entry.get("name")
        if not isinstance(name, str) or not name:
            continue
        default = entry.get("default")
        default_text = "" if default is None else str(default)
        line = entry.get("line")
        line_num = line if isinstance(line, int) else None
        lookup[name] = (default_text, line_num)
    return lookup


def _find_numeric_from_formulas(formulas_payload: Any, keywords: tuple[str, ...], target_token: str) -> float | None:
    entries = _collect_entries(formulas_payload, ("formulas",))
    token_pattern = re.compile(
        rf"(?:(?P<a>[-+]?\d*\.?\d+)\s*\*\s*{re.escape(target_token)}|{re.escape(target_token)}\s*\*\s*(?P<b>[-+]?\d*\.?\d+))",
        re.IGNORECASE,
    )

    for entry in entries:
        if not isinstance(entry, dict):
            continue

        text = " ".join(
            str(entry.get(key, ""))
            for key in ("name", "description", "code_snippet", "purpose", "category")
        ).lower()

        if not all(word in text for word in keywords):
            continue

        snippet = str(entry.get("code_snippet", ""))
        match = token_pattern.search(snippet)
        if not match:
            match = token_pattern.search(text)
        if not match:
            continue

        raw = match.group("a") or match.group("b")
        if raw is None:
            continue
        value = _to_float(raw)
        if value is not None:
            return value

    return None


def _extract_manual_block(path: str, warnings: list[str]) -> str | None:
    if not os.path.exists(path):
        return None
    try:
        with open(path, "r", encoding="utf-8") as handle:
            existing = handle.read()
    except OSError as exc:
        warnings.append(f"Failed to read existing file for MANUAL merge ({path}): {exc}")
        return None

    match = MANUAL_BLOCK_RE.search(existing)
    if not match:
        return None
    return match.group(0)


def _merge_manual_block(new_text: str, existing_manual: str | None) -> str:
    if existing_manual is None:
        return new_text

    if MANUAL_BLOCK_RE.search(new_text):
        return MANUAL_BLOCK_RE.sub(existing_manual, new_text, count=1)

    return new_text.rstrip() + "\n\n" + existing_manual + "\n"


def _season_display(value: Any) -> tuple[str, str]:
    number = _to_float(value)
    if number is not None:
        if number > 1.0:
            return f"×{number:.2f}", "사망률 증가 / Increased mortality risk"
        if number < 1.0:
            return f"×{number:.2f}", "사망률 감소 / Reduced mortality risk"
        return f"×{number:.2f}", "중립 / Neutral"

    if isinstance(value, dict):
        fragments: list[str] = []
        numeric_values: list[float] = []
        for key in sorted(value.keys()):
            part = _to_float(value.get(key))
            if part is None:
                continue
            fragments.append(f"{key} ×{part:.2f}")
            numeric_values.append(part)

        if not fragments:
            return "n/a", "데이터 없음 / No data"

        if all(part > 1.0 for part in numeric_values):
            effect = "사망률 증가 / Increased mortality risk"
        elif all(part < 1.0 for part in numeric_values):
            effect = "사망률 감소 / Reduced mortality risk"
        else:
            effect = "혼합 영향 / Mixed effect"
        return ", ".join(fragments), effect

    return "n/a", "데이터 없음 / No data"


def _dominant_component(mu_infant: float, mu_background: float, mu_senescent: float) -> str:
    pairs = [
        (mu_infant, "Infant / 영아"),
        (mu_background, "Background / 배경"),
        (mu_senescent, "Senescent / 노화"),
    ]
    pairs.sort(key=lambda item: item[0], reverse=True)
    return pairs[0][1]


def _build_markdown(
    manifest: dict,
    extracted: dict,
    warnings: list[str],
) -> tuple[str, dict[str, Any]]:
    del manifest  # intentionally unused for this generator

    data_file_entry, siler_payload = _find_siler_data_file(extracted.get("data_files"))
    if not siler_payload:
        warnings.append("Missing siler_parameters data in extracted['data_files']; using fallback defaults.")

    mortality_system = _find_mortality_system(extracted.get("systems"))
    constants = _constant_lookup(extracted.get("constants"))
    class_vars = _class_var_lookup(mortality_system)

    baseline = _as_dict(siler_payload.get("baseline"))
    tech_modifiers = _as_dict(siler_payload.get("tech_modifiers"))
    care_protection = _as_dict(siler_payload.get("care_protection"))
    season_modifiers = _as_dict(siler_payload.get("season_modifiers"))

    a1 = _to_float(baseline.get("a1"))
    b1 = _to_float(baseline.get("b1"))
    a2 = _to_float(baseline.get("a2"))
    a3 = _to_float(baseline.get("a3"))
    b3 = _to_float(baseline.get("b3"))

    # Fallback to known class defaults from mortality_system when data file is incomplete.
    if a1 is None:
        a1 = _to_float(class_vars.get("_a1", ("", None))[0]) or 0.60
    if b1 is None:
        b1 = _to_float(class_vars.get("_b1", ("", None))[0]) or 1.30
    if a2 is None:
        a2 = _to_float(class_vars.get("_a2", ("", None))[0]) or 0.010
    if a3 is None:
        a3 = _to_float(class_vars.get("_a3", ("", None))[0]) or 0.00006
    if b3 is None:
        b3 = _to_float(class_vars.get("_b3", ("", None))[0]) or 0.090

    k1 = _to_float(tech_modifiers.get("k1"))
    k2 = _to_float(tech_modifiers.get("k2"))
    k3 = _to_float(tech_modifiers.get("k3"))
    if k1 is None:
        k1 = _to_float(class_vars.get("_tech_k1", ("", None))[0]) or 0.30
    if k2 is None:
        k2 = _to_float(class_vars.get("_tech_k2", ("", None))[0]) or 0.20
    if k3 is None:
        k3 = _to_float(class_vars.get("_tech_k3", ("", None))[0]) or 0.05

    care_reduction = _to_float(care_protection.get("protection_factor"))
    if care_reduction is None:
        care_reduction = _to_float(class_vars.get("_care_protection_factor", ("", None))[0])

    ticks_per_year = _to_float(constants.get("TICKS_PER_YEAR", (None, None))[0]) or 4380.0
    age_child_end_ticks = _to_float(constants.get("AGE_CHILD_END", (None, None))[0])
    if age_child_end_ticks is not None and ticks_per_year > 0:
        care_max_age = age_child_end_ticks / ticks_per_year
    else:
        care_max_age = None

    orphan_penalty = _find_numeric_from_formulas(
        extracted.get("formulas"),
        keywords=("orphan",),
        target_token="orphan",
    )

    source_data_file = str(data_file_entry.get("file", "")).strip()
    if not source_data_file:
        warnings.append("Siler parameters source file missing in extracted data_files.")
        source_data_file = "unknown"

    source_system_file = str(mortality_system.get("file", "")).strip()
    if not source_system_file:
        warnings.append("Mortality system source file missing in extracted systems.")
        source_system_file = "unknown"

    mortality_rows: list[str] = []
    for age in SAMPLE_AGES:
        mu_infant = a1 * math.exp(-b1 * age)
        mu_background = a2
        mu_senescent = a3 * math.exp(b3 * age)
        mu = mu_infant + mu_background + mu_senescent
        annual_prob = 1.0 - math.exp(-mu)
        per_tick_prob = 1.0 - math.exp(-mu / ticks_per_year)

        mortality_rows.append(
            "| "
            + " | ".join(
                [
                    str(age),
                    f"{mu:.3f}",
                    _format_pct(annual_prob),
                    _format_pct(per_tick_prob),
                    _escape_md(_dominant_component(mu_infant, mu_background, mu_senescent)),
                ]
            )
            + " |"
        )

    season_rows: list[str] = []
    for season in ("spring", "summer", "autumn", "winter"):
        display, effect = _season_display(season_modifiers.get(season, 1.0))
        season_rows.append(
            "| "
            + " | ".join(
                [
                    season.capitalize(),
                    _escape_md(display),
                    _escape_md(effect),
                ]
            )
            + " |"
        )

    mortality_line = None
    for fn in mortality_system.get("functions", []):
        if isinstance(fn, dict) and fn.get("name") == "_do_mortality_check":
            if isinstance(fn.get("line"), int):
                mortality_line = fn["line"]
                break

    ticks_line = constants.get("TICKS_PER_YEAR", (None, None))[1]

    manual_block = "\n".join([MANUAL_START, "", MANUAL_END])

    lines: list[str] = [
        "---",
        f"title: {_yaml_quote('Mortality System — Detailed Documentation')}",
        f"description: {_yaml_quote('Siler mortality model, modifiers, and per-tick death probability details')}",
        "generated: true",
        "source_files:",
        f"  - {_yaml_quote(source_system_file)}",
        f"  - {_yaml_quote(source_data_file)}",
        "nav_order: 49",
        "---",
        "",
        "# Mortality System — Detailed Documentation",
        "",
        "한국어 / English: 사망 시스템의 수학적 구조와 계수 결합을 설명합니다. This page explains the mortality model mathematics and modifier coupling.",
        "",
        f"📄 source: `{source_system_file}`"
        + (f":L{mortality_line}" if mortality_line is not None else "")
        + f", `{source_data_file}`",
        "",
        "## The Siler Mortality Model",
        "",
        "The mortality system implements **Siler's (1979) competing-risk model**, which produces a bathtub-shaped hazard curve:",
        "",
        "$$",
        r"\mu(x) = a_1 \cdot e^{-b_1 \cdot x} + a_2 + a_3 \cdot e^{b_3 \cdot x}",
        "$$",
        "",
        "Where x = age in years, and:",
        "",
        "| Parameter | Value | Meaning |",
        "|:----------|------:|:--------|",
        f"| $a_1$ | {a1:.2f} | Infant mortality amplitude - high risk at birth, rapidly declining |",
        f"| $b_1$ | {b1:.2f} | Infant mortality decline rate - how fast infant risk drops |",
        f"| $a_2$ | {a2:.3f} | Age-independent background mortality - constant baseline risk |",
        f"| $a_3$ | {a3:.5f} | Senescent mortality amplitude - exponential aging onset |",
        f"| $b_3$ | {b3:.3f} | Senescent acceleration rate (Gompertz parameter) - how fast aging kills |",
        "",
        "### The Three Components",
        "",
        "| Component | Formula | Age Profile | Biological Meaning |",
        "|:----------|:--------|:------------|:-------------------|",
        "| Infant decline | $a_1 \\cdot e^{-b_1 x}$ | Highest at birth, drops rapidly | Birth defects, immune immaturity |",
        "| Background | $a_2$ | Constant across all ages | Accidents, infections, random events |",
        "| Senescent | $a_3 \\cdot e^{b_3 x}$ | Negligible in youth, exponential in old age | Aging, organ failure, cancer |",
        "",
        "## Technology Modifiers",
        "",
        "Settlement technology level reduces mortality:",
        "",
        "$$",
        r"\mu_{\text{tech}}(x) = a_1 \cdot (1 - k_1 \cdot T) \cdot e^{-b_1 x} + a_2 \cdot (1 - k_2 \cdot T) + a_3 \cdot (1 - k_3 \cdot T) \cdot e^{b_3 x}",
        "$$",
        "",
        "Where T = tech_level (0.0 to 1.0):",
        "",
        "| Modifier | Value | Effect | Interpretation |",
        "|:---------|------:|:-------|:---------------|",
        f"| $k_1$ | {k1:.2f} | -{k1 * 100:.0f}% infant mortality at max tech | Better obstetric care |",
        f"| $k_2$ | {k2:.2f} | -{k2 * 100:.0f}% background mortality at max tech | Sanitation, medicine |",
        f"| $k_3$ | {k3:.2f} | -{k3 * 100:.0f}% senescent mortality at max tech | Marginal anti-aging impact |",
        "",
        "**Design note**: Tech has the strongest effect on infant mortality (easiest wins) and weakest on aging (hard biological limit).",
        "",
        "## Infant & Child Care Protection",
        "",
        "Young entities receive mortality reduction when cared for:",
        "",
        "$$",
        r"\mu_{\text{care}}(x) = \mu(x) \cdot (1 - \text{care\_factor})",
        "$$",
        "",
        "| Parameter | Value | Meaning |",
        "|:----------|------:|:--------|",
        f"| care_max_age | {_format_decimal(care_max_age, 2)} | Maximum age for care protection |",
        f"| care_reduction | {_format_decimal(care_reduction, 2)} | Mortality reduction when cared for |",
        f"| orphan_penalty | {_format_decimal(orphan_penalty, 2)} | Additional mortality risk without caregiver |",
        "",
        "## Seasonal Mortality Modifiers",
        "",
        "| Season | Modifier | Effect |",
        "|:-------|:---------|:-------|",
        *season_rows,
        "",
        "Winter increases mortality (cold, food scarcity), while spring/summer reduce it.",
        "",
        "## Stress → Mortality Coupling",
        "",
        "High allostatic load from the stress system increases mortality:",
        "",
        "$$",
        r"\mu_{\text{stress}}(x) = \mu(x) \cdot (1 + \alpha \cdot \text{allostatic\_load} / 100)",
        "$$",
        "",
        "This creates a feedback loop:",
        "- Stressful events → high stress → allostatic load accumulates",
        "- High allostatic load → increased hazard rate → earlier death",
        "- Early death of partner/child → massive stressor → more allostatic load on survivors",
        "",
        "## Nutrition Modifier",
        "",
        "Malnutrition increases mortality:",
        "",
        "$$",
        r"\mu_{\text{nutrition}}(x) = \mu(x) \cdot (1 + \beta \cdot (1 - \text{food\_satiety}))",
        "$$",
        "",
        "Implementation note: In code this is typically derived from `entity.hunger` / `food_satiety` (0.0 to 1.0).",
        "",
        "## Per-Tick Death Probability",
        "",
        "The final death probability per tick:",
        "",
        "$$",
        r"P(\text{death}) = 1 - e^{-\mu_{\text{final}}(x) / \text{TICKS\_PER\_YEAR}}",
        "$$",
        "",
        "Where $\\mu_{\\text{final}}$ combines all modifiers:",
        "$$",
        r"\mu_{\text{final}}(x) = \mu_{\text{tech}}(x) \cdot \text{care} \cdot \text{season} \cdot \text{stress} \cdot \text{nutrition}",
        "$$",
        "",
        f"TICKS_PER_YEAR = **{int(ticks_per_year)}**"
        + (f" (📄 source: `scripts/core/game_config.gd:L{ticks_line}`)" if ticks_line is not None else ""),
        "",
        "## Example Mortality Rates (Baseline, No Modifiers)",
        "",
        "| Age | $\\mu(x)$ | Annual Death Prob | Per-tick Prob | Dominant Component |",
        "|----:|----------:|------------------:|--------------:|:-------------------|",
        *mortality_rows,
        "",
        "## Source Notes",
        "",
        f"- 📄 source: `{source_system_file}`",
        f"- 📄 source: `{source_data_file}`",
        "",
        manual_block,
        "",
    ]

    metadata = {
        "source_system_file": source_system_file,
        "source_data_file": source_data_file,
        "ticks_per_year": ticks_per_year,
    }
    return "\n".join(lines), metadata


def run(manifest: dict, extracted: dict) -> dict:
    """Generate mortality system detail documentation.

    Args:
        manifest: The manifest.json data from Phase 1.
        extracted: Aggregated extracted payload containing data_files, formulas, systems, constants.

    Returns:
        dict with keys:
            - "files_written": list[str]
            - "pages_generated": int
            - "warnings": list[str]
            - "errors": list[str]
    """
    files_written: list[str] = []
    warnings: list[str] = []
    errors: list[str] = []

    if not isinstance(manifest, dict):
        warnings.append("Manifest payload is not a dict; continuing with available extracted data.")
    if not isinstance(extracted, dict):
        warnings.append("Extracted payload is not a dict; cannot generate mortality detail page.")
        return {
            "files_written": files_written,
            "pages_generated": 0,
            "warnings": warnings,
            "errors": errors,
        }

    try:
        markdown, _meta = _build_markdown(manifest, extracted, warnings)
    except Exception as exc:  # pragma: no cover - defensive guard
        errors.append(f"Failed to render mortality detail page: {exc}")
        return {
            "files_written": files_written,
            "pages_generated": 0,
            "warnings": warnings,
            "errors": errors,
        }

    output_dir = config.CONTENT_SYSTEMS
    output_path = os.path.join(output_dir, "mortality-detail.md")

    existing_manual = _extract_manual_block(output_path, warnings)
    final_content = _merge_manual_block(markdown, existing_manual)

    try:
        config.ensure_dir(output_dir)
        with open(output_path, "w", encoding="utf-8") as handle:
            handle.write(final_content)
    except OSError as exc:
        errors.append(f"Failed to write mortality detail markdown ({output_path}): {exc}")
        return {
            "files_written": files_written,
            "pages_generated": 0,
            "warnings": warnings,
            "errors": errors,
        }

    files_written.append(output_path)
    return {
        "files_written": files_written,
        "pages_generated": 1,
        "warnings": warnings,
        "errors": errors,
    }
