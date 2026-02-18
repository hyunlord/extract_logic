"""Phase 3 generator: produce narrative system documentation pages."""

from __future__ import annotations

import json
import os
import re
from collections import defaultdict
from typing import Any

import scripts.config as config
from scripts.generators.strings import t

_MANUAL_BLOCK_RE = re.compile(
    r"<!-- MANUAL:START -->.*?<!-- MANUAL:END -->",
    re.DOTALL,
)
_EXP_CALL_RE = re.compile(r"exp\(([^()]+)\)")
_VALID_SLUG_RE = re.compile(r"[^a-z0-9_]+")
_MATH_OPERATOR_RE = re.compile(r"[A-Za-z0-9_)\]]\s*[\+\*/]\s*[A-Za-z0-9_(\[]")
_MATH_MINUS_RE = re.compile(r"[A-Za-z0-9_)\]]\s+-\s+[A-Za-z0-9_(\[]")


def _load_json(path: str, label: str, warnings: list[str]) -> dict[str, Any]:
    if not os.path.exists(path):
        warnings.append(f"Missing input file, skipped: {label} ({path})")
        return {}
    try:
        with open(path, "r", encoding="utf-8") as handle:
            payload = json.load(handle)
    except OSError as exc:
        warnings.append(f"Failed to read {label} ({path}): {exc}")
        return {}
    except json.JSONDecodeError as exc:
        warnings.append(f"Invalid JSON in {label} ({path}): {exc}")
        return {}

    if not isinstance(payload, dict):
        warnings.append(f"Invalid payload for {label}: expected object root.")
        return {}
    return payload


def _load_payload(
    extracted: dict[str, Any] | None,
    key: str,
    path: str,
    label: str,
    warnings: list[str],
) -> dict[str, Any]:
    if isinstance(extracted, dict):
        if key in extracted:
            payload = extracted.get(key)
        else:
            payload = extracted.get(f"{key}.json")
        if payload is not None:
            if isinstance(payload, dict):
                return payload
            warnings.append(f"Invalid in-memory payload for {label}: expected object root.")
            return {}
    return _load_json(path, label, warnings)


def _list_of_dicts(value: Any) -> list[dict[str, Any]]:
    if not isinstance(value, list):
        return []
    output: list[dict[str, Any]] = []
    for item in value:
        if isinstance(item, dict):
            output.append(item)
    return output


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


def _normalize_text(value: Any) -> str:
    if not isinstance(value, str):
        return ""
    return " ".join(value.split()).strip()


def _first_sentence(text: str) -> str:
    normalized = _normalize_text(text)
    if not normalized:
        return "Generated system documentation page."
    parts = re.split(r"(?<=[.!?])\s+", normalized, maxsplit=1)
    return parts[0] if parts else normalized


def _yaml_quote(value: str) -> str:
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def _md_cell(value: Any) -> str:
    text = str(value)
    return text.replace("|", r"\|").replace("\n", " ")


def _display_name(entry: dict[str, Any], slug: str) -> str:
    system_name = entry.get("system_name")
    if isinstance(system_name, str) and system_name.strip():
        token = system_name.strip()
    else:
        token = slug
    return token.replace("_", " ").strip().title()


def _slug_from_entry(entry: dict[str, Any]) -> str:
    system_name = entry.get("system_name")
    if isinstance(system_name, str) and system_name.strip():
        raw = system_name.strip().lower()
    else:
        rel_file = entry.get("file")
        base = os.path.splitext(os.path.basename(rel_file))[0] if isinstance(rel_file, str) else "system"
        raw = base.lower()
        if raw.endswith("_system"):
            raw = raw[: -len("_system")]

    slug = _VALID_SLUG_RE.sub("_", raw).strip("_")
    return slug or "system"


def _resolve_slug_collisions(entries: list[dict[str, Any]]) -> dict[str, str]:
    slug_by_file: dict[str, str] = {}
    used: set[str] = set()
    for entry in entries:
        rel_file = entry.get("file")
        if not isinstance(rel_file, str) or not rel_file:
            continue
        base_slug = _slug_from_entry(entry)
        slug = base_slug
        suffix = 2
        while slug in used:
            slug = f"{base_slug}_{suffix}"
            suffix += 1
        used.add(slug)
        slug_by_file[rel_file] = slug
    return slug_by_file


def _parse_numeric(value: Any) -> float | None:
    if isinstance(value, (int, float)):
        return float(value)
    if isinstance(value, str):
        match = re.search(r"-?\d+(?:\.\d+)?", value.strip())
        if match:
            try:
                return float(match.group(0))
            except ValueError:
                return None
    return None


def _tick_interval_text(entry: dict[str, Any]) -> str:
    interval = entry.get("tick_interval")
    if isinstance(interval, (int, float)):
        if isinstance(interval, float) and interval.is_integer():
            return str(int(interval))
        return str(interval)

    raw = entry.get("tick_interval_raw")
    if isinstance(raw, str) and raw.strip():
        return f"config ({raw.strip()})"
    return "n/a"


def _manual_block(text: str) -> str:
    match = _MANUAL_BLOCK_RE.search(text)
    return match.group(0) if match else ""


def _merge_manual_blocks(generated: str, existing: str) -> str:
    existing_block = _manual_block(existing)
    if not existing_block:
        return generated

    if _MANUAL_BLOCK_RE.search(generated):
        return _MANUAL_BLOCK_RE.sub(existing_block, generated, count=1)

    output = generated.rstrip() + "\n\n" + existing_block + "\n"
    return output


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
    except OSError as exc:
        errors.append(f"Failed to write markdown ({path}): {exc}")
        return False
    return True


def _render_markdown_table(headers: list[str], rows: list[list[str]]) -> str:
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join([":--"] * len(headers)) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(_md_cell(cell) for cell in row) + " |")
    return "\n".join(lines)


def _ticks_per_year(constants_map: dict[str, dict[str, Any]]) -> float | None:
    constant = constants_map.get("TICKS_PER_YEAR")
    if not constant:
        return None
    value = _parse_numeric(constant.get("value"))
    if value and value > 0:
        return value
    value_raw = _parse_numeric(constant.get("value_raw"))
    if value_raw and value_raw > 0:
        return value_raw
    return None


def _humanize_field_name(field_name: str) -> str:
    return field_name.replace("_", " ").strip()


def _academic_models(entry: dict[str, Any], formulas: list[dict[str, Any]]) -> list[str]:
    output: list[str] = []
    seen: set[str] = set()

    for formula in formulas:
        model_ref = formula.get("model_ref")
        if isinstance(model_ref, dict):
            name = _normalize_text(model_ref.get("name"))
            if name and name not in seen:
                seen.add(name)
                output.append(name)

    doc_text = _normalize_text(entry.get("doc_comment")).lower()
    keyword_models = [
        ("plutchik", "Plutchik emotion model"),
        ("lazarus", "Lazarus appraisal model"),
        ("scherer", "Scherer appraisal process"),
        ("russell", "Russell circumplex model"),
        ("ornstein", "Ornstein-Uhlenbeck mean reversion"),
        ("siler", "Siler mortality hazard model"),
        ("allostatic", "Allostatic load model"),
        ("yerkes", "Yerkes-Dodson arousal-performance law"),
        ("gas", "General Adaptation Syndrome"),
        ("hexaco", "HEXACO personality framework"),
    ]
    for keyword, label in keyword_models:
        if keyword in doc_text and label not in seen:
            seen.add(label)
            output.append(label)

    if not output:
        output.append("a domain-specific simulation model")
    return output


def _domain_description(entry: dict[str, Any], display_name: str) -> str:
    doc_comment = _normalize_text(entry.get("doc_comment"))
    if doc_comment:
        sentence = _first_sentence(doc_comment).rstrip(".")
        return sentence[0].lower() + sentence[1:] if sentence else doc_comment.lower()
    return f"{display_name.lower()} dynamics for entities and world state"


def _tick_interval_overview(entry: dict[str, Any], ticks_per_year: float | None) -> str:
    interval = _parse_numeric(entry.get("tick_interval"))
    raw_text = _normalize_text(entry.get("tick_interval_raw"))
    if interval and interval > 0:
        if ticks_per_year and ticks_per_year > 0:
            years = interval / ticks_per_year
            return f"every **{interval:g} ticks** ({years:.1f} game-years)"
        return f"every **{interval:g} ticks**"
    if raw_text:
        return f"on a **config-driven cadence** (`{raw_text}`)"
    return "**at an unspecified cadence**"


def _core_entity_data_text(entry: dict[str, Any], access_map: dict[str, set[str]] | None) -> str:
    fields = _unique_strings(entry.get("entity_fields", []))
    if not fields:
        return "No entity fields were extracted."
    readable: list[str] = []
    for field in fields:
        access = ""
        if access_map is not None:
            access = _field_access_text(access_map.get(field, set()))
        if access:
            readable.append(f"`{field}` ({access})")
        else:
            readable.append(f"`{field}`")
    return ", ".join(readable)


def _field_access_text(access_set: set[str]) -> str:
    if access_set == {"read", "write"}:
        return "read/write"
    if access_set == {"write"}:
        return "write"
    if access_set == {"read"}:
        return "read"
    return "read/write (inferred)"


def _looks_like_math_expression(expression: str) -> bool:
    stripped = expression.strip()
    if (
        (stripped.startswith('"') and stripped.endswith('"'))
        or (stripped.startswith("'") and stripped.endswith("'"))
    ):
        return False

    lowered = expression.lower()
    if any(fn in lowered for fn in ("exp(", "pow(", "log(", "sqrt(", "sin(", "cos(")):
        return True
    if _MATH_OPERATOR_RE.search(expression):
        return True
    if _MATH_MINUS_RE.search(expression):
        return True
    return False


def _extract_formula_expression(code_snippet: str) -> str:
    for raw_line in code_snippet.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        line = line.rstrip(",")
        if ":" in line and "=" not in line:
            line = line.split(":", 1)[1].strip()
        if "=" in line:
            line = line.split("=", 1)[1].strip()
        line = re.sub(r"\bvar\s+", "", line)
        if line:
            return line
    return ""


def _code_to_latex(code_snippet: str) -> str:
    expression = _extract_formula_expression(code_snippet)
    if not expression:
        return ""
    if not _looks_like_math_expression(expression):
        return ""

    latex = _EXP_CALL_RE.sub(r"e^{\1}", expression)
    latex = latex.replace("*", r" \cdot ")
    latex = latex.replace(">=", r"\ge ")
    latex = latex.replace("<=", r"\le ")
    return latex


def _formula_title(name: str) -> str:
    return name.replace("_", " ").strip().title()


def _function_line_range(function: dict[str, Any]) -> tuple[int | None, int | None]:
    start = function.get("line")
    line_count = function.get("line_count")
    if isinstance(start, int) and isinstance(line_count, int) and line_count > 0:
        return start, start + line_count - 1
    if isinstance(start, int):
        return start, start
    return None, None


def _is_pipeline_function(name: str) -> bool:
    lowered = name.lower()
    if lowered in {"_init", "init", "_ready", "_process", "_physics_process", "_debug_log"}:
        return False
    if lowered.startswith("_load_") or lowered.startswith("load_"):
        return False
    if lowered.startswith("_rand") or lowered.startswith("rand"):
        return False
    if "tick" in lowered:
        return True
    return lowered.startswith(
        (
            "_calc_",
            "calc_",
            "_calculate_",
            "calculate_",
            "_update_",
            "update_",
            "_apply_",
            "apply_",
            "_process_",
            "process_",
            "_check_",
            "check_",
            "_record_",
            "record_",
            "_determine_",
            "determine_",
            "_inject_",
            "inject_",
            "_get_",
            "get_",
        )
    )


def _step_label_from_function(function: dict[str, Any]) -> str:
    name = str(function.get("name", "step")).lower()

    if "habituation" in name:
        return "Apply habituation to repeated events"
    if "appraisal" in name:
        return "Calculate appraisal scale from demand/resource context"
    if "continuous_stressor" in name:
        return "Process continuous stressors (hunger, energy, social)"
    if "emotion_contribution" in name:
        return "Convert emotions into stress contribution"
    if "personality" in name and ("scale" in name or "sensitivity" in name):
        return "Apply personality modifiers to sensitivity"
    if "half_life" in name or "decay" in name:
        return "Update fast layer with exponential-style decay"
    if "baseline" in name or "mean_revert" in name:
        return "Update slow layer with baseline mean reversion"
    if "contagion" in name:
        return "Process emotional contagion in settlement scope"
    if "mental_break" in name:
        return "Check mental break conditions"
    if "allostatic" in name:
        return "Update allostatic load (chronic stress accumulation)"
    if "reserve" in name or "gas" in name:
        return "Update GAS reserve and stress stage"
    if "recovery" in name:
        return "Calculate recovery from rest and support"
    if "work_efficiency" in name:
        return "Calculate Yerkes-Dodson-style work efficiency"
    if "stress_state" in name:
        return "Update stress-state classification"
    if "trace" in name:
        return "Process memory/stress trace accumulation"

    if name == "execute_tick":
        return "Run per-entity tick update loop"

    normalized = name.strip("_")
    tokens = [token for token in normalized.split("_") if token and token not in {"func"}]
    if not tokens:
        return "Execute system step"

    verb_map = {
        "calc": "Calculate",
        "calculate": "Calculate",
        "update": "Update",
        "apply": "Apply",
        "process": "Process",
        "check": "Check",
        "record": "Record",
        "determine": "Determine",
        "inject": "Inject",
        "get": "Resolve",
    }
    first = tokens[0]
    verb = verb_map.get(first, first.title())
    remainder = " ".join(tokens[1:]) if len(tokens) > 1 else "system state"
    return f"{verb} {remainder}".strip()


def _match_formulas_for_function(
    function: dict[str, Any],
    formulas: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    start, end = _function_line_range(function)
    name = str(function.get("name", ""))
    matched: list[dict[str, Any]] = []
    for formula in formulas:
        line_start = formula.get("line_start")
        if isinstance(start, int) and isinstance(end, int) and isinstance(line_start, int):
            if start <= line_start <= end:
                matched.append(formula)
                continue
        formula_name = str(formula.get("name", ""))
        if name and formula_name.startswith(name):
            matched.append(formula)
    return matched


def _math_hint_for_function(function: dict[str, Any]) -> str:
    text_parts = [str(function.get("name", ""))]
    for call in function.get("calls_to", []):
        if isinstance(call, str):
            text_parts.append(call)
    text = " ".join(text_parts).lower()

    if any(token in text for token in ("exp(", "half_life", "decay")):
        return "exponential decay dynamics"
    if any(token in text for token in ("ornstein", "mean", "baseline")):
        return "mean-reverting dynamics"
    if "appraisal" in text:
        return "appraisal scaling"
    if "allostatic" in text:
        return "allostatic accumulation model"
    if any(token in text for token in ("reserve", "gas_stage")):
        return "adaptive reserve update"
    if "efficiency" in text and "stress" in text:
        return "stress-performance curve"
    if "contagion" in text:
        return "contagion diffusion update"
    return ""


def _formula_context(formula: dict[str, Any]) -> str:
    model_ref = formula.get("model_ref")
    if isinstance(model_ref, dict):
        formula_text = model_ref.get("formula")
        if isinstance(formula_text, str) and formula_text.strip():
            return formula_text.strip()
    purpose = _normalize_text(formula.get("purpose"))
    if purpose:
        return purpose
    name = _normalize_text(formula.get("name"))
    if name:
        return _formula_title(name)
    return ""


def _match_formulas_by_keywords(
    formulas: list[dict[str, Any]],
    keywords: list[str],
) -> list[dict[str, Any]]:
    matched: list[dict[str, Any]] = []
    for formula in formulas:
        text = " ".join(
            [
                str(formula.get("name", "")),
                str(formula.get("purpose", "")),
                str(formula.get("code_snippet", "")),
            ]
        ).lower()
        if any(keyword in text for keyword in keywords):
            matched.append(formula)
    return matched


def _math_hint_for_label(label: str) -> str:
    text = label.lower()
    if "exponential" in text or "decay" in text:
        return "exponential decay dynamics"
    if "ornstein" in text or "mean reversion" in text:
        return "mean-reverting dynamics"
    if "lazarus" in text or "appraisal" in text:
        return "appraisal scaling"
    if "allostatic" in text:
        return "allostatic accumulation model"
    if "yerkes" in text:
        return "stress-performance curve"
    if "contagion" in text:
        return "contagion diffusion update"
    return ""


def _match_function_by_keywords(
    functions: list[dict[str, Any]],
    keywords: list[str],
) -> dict[str, Any] | None:
    for function in functions:
        name = str(function.get("name", "")).lower()
        if any(keyword in name for keyword in keywords):
            return function
        for call in function.get("calls_to", []):
            if isinstance(call, str) and any(keyword in call.lower() for keyword in keywords):
                return function
    return None


def _explicit_pipeline_steps(
    rel_file: str,
    functions: list[dict[str, Any]],
    formulas: list[dict[str, Any]],
    emitted_signals: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    filename = os.path.basename(rel_file)
    if filename == "emotion_system.gd":
        steps_spec = [
            ("Apply habituation to repeated events", ["habituation", "habituate"]),
            ("Calculate appraisal impulses from pending events", ["appraisal", "impulse", "pending"]),
            ("Apply personality sensitivity modifiers", ["personality", "sensitivity"]),
            ("Update fast layer (exponential decay + impulses)", ["fast", "decay", "half_life", "impulse"]),
            ("Update slow layer (Ornstein-Uhlenbeck mean reversion)", ["slow", "ornstein", "mean_revert", "baseline"]),
            ("Apply opposite emotion inhibition", ["opposite", "inhibit"]),
            ("Process emotional contagion (settlement-scoped)", ["contagion", "settlement"]),
            ("Check mental break conditions", ["mental_break", "break"]),
            ("Emit emotion change signals", ["emit", "signal", "emotion"]),
        ]
    elif filename == "stress_system.gd":
        steps_spec = [
            ("Calculate Lazarus appraisal scale (demand/resource ratio)", ["lazarus", "appraisal", "demand", "resource"]),
            ("Process continuous stressors (hunger, energy, social)", ["continuous", "stressor", "hunger", "energy", "social"]),
            ("Convert emotions to stress contribution", ["emotion", "stress", "contribution"]),
            ("Apply personality modifiers to stress sensitivity", ["personality", "sensitivity", "modifier"]),
            ("Calculate recovery from sleep/safety/support", ["recovery", "sleep", "safety", "support"]),
            ("Update allostatic load (chronic stress accumulation)", ["allostatic", "load", "chronic"]),
            ("Update GAS stage (alarm -> resistance -> exhaustion)", ["gas", "stage", "alarm", "resistance", "exhaustion"]),
            ("Calculate Yerkes-Dodson eustress efficiency", ["yerkes", "dodson", "efficiency", "eustress"]),
            ("Emit stress update signals", ["emit", "signal", "stress"]),
        ]
    else:
        return []

    steps: list[dict[str, Any]] = []
    for label, keywords in steps_spec:
        matched_function = _match_function_by_keywords(functions, keywords)
        line_start, line_end = _function_line_range(matched_function) if matched_function else (None, None)
        matched_formulas = _match_formulas_by_keywords(formulas, keywords)
        math_refs = _unique_strings([_formula_context(formula) for formula in matched_formulas if _formula_context(formula)])
        hint = _math_hint_for_label(label)
        if hint:
            math_refs.append(hint)
        steps.append(
            {
                "label": label,
                "line_start": line_start,
                "line_end": line_end,
                "math": _unique_strings(math_refs),
            }
        )

    signal_names: list[str] = []
    for signal in emitted_signals:
        signal_name = signal.get("signal_name")
        if isinstance(signal_name, str) and signal_name and signal_name not in signal_names:
            signal_names.append(signal_name)
    if signal_names:
        has_emit_step = any("emit" in str(step.get("label", "")).lower() for step in steps)
        if not has_emit_step:
            steps.append(
                {
                    "label": f"Emit system signals: {', '.join(f'`{name}`' for name in signal_names)}",
                    "line_start": None,
                    "line_end": None,
                    "math": [],
                }
            )

    return steps


def _build_tick_pipeline(
    rel_file: str,
    entry: dict[str, Any],
    formulas: list[dict[str, Any]],
    emitted_signals: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    raw_functions = _list_of_dicts(entry.get("functions"))
    functions = sorted(raw_functions, key=lambda item: item.get("line", 0))
    if not functions:
        return []

    explicit_steps = _explicit_pipeline_steps(rel_file, functions, formulas, emitted_signals)
    if explicit_steps:
        return explicit_steps

    tick_fn = None
    for function in functions:
        name = str(function.get("name", ""))
        if name == "execute_tick" or name.endswith("tick"):
            tick_fn = function
            break

    steps: list[dict[str, Any]] = []
    if tick_fn:
        start, end = _function_line_range(tick_fn)
        base_math = _math_hint_for_function(tick_fn)
        matched_formulas = _match_formulas_for_function(tick_fn, formulas)
        formulas_text = [_formula_context(formula) for formula in matched_formulas]
        if base_math:
            formulas_text.append(base_math)
        steps.append(
            {
                "label": "Run per-entity tick update loop",
                "line_start": start,
                "line_end": end,
                "math": _unique_strings([text for text in formulas_text if text]),
            }
        )

    for function in functions:
        name = str(function.get("name", ""))
        if tick_fn is function:
            continue
        if not _is_pipeline_function(name):
            continue

        label = _step_label_from_function(function)
        start, end = _function_line_range(function)
        matched_formulas = _match_formulas_for_function(function, formulas)
        formulas_text = [_formula_context(formula) for formula in matched_formulas]
        hint = _math_hint_for_function(function)
        if hint:
            formulas_text.append(hint)
        steps.append(
            {
                "label": label,
                "line_start": start,
                "line_end": end,
                "math": _unique_strings([text for text in formulas_text if text]),
            }
        )

    seen_labels: set[str] = set()
    deduped: list[dict[str, Any]] = []
    for step in steps:
        label = str(step.get("label", "")).strip()
        if not label or label in seen_labels:
            continue
        seen_labels.add(label)
        deduped.append(step)

    signal_names: list[str] = []
    for signal in emitted_signals:
        signal_name = signal.get("signal_name")
        if isinstance(signal_name, str) and signal_name and signal_name not in signal_names:
            signal_names.append(signal_name)
    if signal_names:
        has_emit_step = any("emit" in str(step.get("label", "")).lower() for step in deduped)
        if not has_emit_step:
            line_no = None
            for signal in emitted_signals:
                candidate = signal.get("emitter_line")
                if isinstance(candidate, int):
                    line_no = candidate
                    break
            deduped.append(
                {
                    "label": f"Emit system signals: {', '.join(f'`{name}`' for name in signal_names)}",
                    "line_start": line_no,
                    "line_end": line_no,
                    "math": [],
                }
            )

    return deduped


def _render_pipeline_mermaid(steps: list[dict[str, Any]]) -> str:
    if len(steps) <= 5:
        return ""
    lines = ["```mermaid", "flowchart TD"]
    for index, step in enumerate(steps, start=1):
        label = str(step.get("label", "step")).replace('"', "'")
        lines.append(f'  step{index}["{index}. {label}"]')
        if index > 1:
            lines.append(f"  step{index - 1} --> step{index}")
    lines.append("```")
    return "\n".join(lines)


def _constant_controls_text(constant_name: str, comment: str) -> str:
    normalized = constant_name.lower()
    if "tick" in normalized and "interval" in normalized:
        return "System update cadence."
    if "tick" in normalized:
        return "Simulation-time conversion or cadence."
    if "threshold" in normalized:
        return "Threshold gate for state transitions."
    if "decay" in normalized or "half_life" in normalized or "lambda" in normalized:
        return "Decay speed of accumulated state."
    if "rate" in normalized:
        return "Rate coefficient for change per tick."
    if "weight" in normalized or "mult" in normalized or "scale" in normalized:
        return "Contribution weight in composite scoring."
    if "min" in normalized or "max" in normalized or "cap" in normalized:
        return "Hard bound for safe state range."
    if comment:
        return _first_sentence(comment)
    return "Behavior tuning constant."


def _constant_effect_text(constant_name: str) -> str:
    normalized = constant_name.lower()
    if "interval" in normalized:
        return "Lower values increase update frequency and responsiveness."
    if "threshold" in normalized:
        return "Changing this moves trigger points for behavior changes."
    if "decay" in normalized or "half_life" in normalized:
        return "Higher values usually lengthen persistence of historical state."
    if "rate" in normalized:
        return "Directly scales accumulation/decay velocity each tick."
    if "weight" in normalized or "mult" in normalized or "scale" in normalized:
        return "Rebalances influence among competing factors."
    if "min" in normalized or "max" in normalized or "cap" in normalized:
        return "Constrains extremes to stabilize the simulation."
    return "Adjusts baseline system behavior under this module."


def _build_configuration_rows(
    entry: dict[str, Any],
    constants_map: dict[str, dict[str, Any]],
) -> list[tuple[str, str, str, str]]:
    rows: list[tuple[str, str, str, str]] = []
    config_refs = _unique_strings(entry.get("config_refs", []))
    for constant_name in config_refs:
        constant = constants_map.get(constant_name, {})
        if constant:
            value = constant.get("value")
            if value in {None, ""}:
                value = constant.get("value_raw")
            value_text = str(value) if value not in {None, ""} else "(not found)"
        else:
            value_text = "(not found)"
        comment = _normalize_text(constant.get("comment")) if constant else ""
        controls = _constant_controls_text(constant_name, comment)
        effect = _constant_effect_text(constant_name)
        rows.append((constant_name, value_text, controls, effect))
    return rows


def _infer_field_type(field: str) -> str:
    lowered = field.lower()
    if lowered in {"id", "age", "tick", "action_timer"} or lowered.endswith("_id"):
        return "int"
    if lowered in {"energy", "hunger", "social", "stress", "arousal", "valence"}:
        return "float"
    if lowered in {"is_alive", "is_child", "is_pregnant"} or lowered.startswith("has_"):
        return "bool"
    if lowered in {"position", "velocity", "target_position"}:
        return "Vector2 / Vector2i"
    if lowered.endswith("_stage") or lowered.endswith("_type") or lowered.endswith("_action"):
        return "String enum"
    if lowered in {"personality", "emotion_data", "emotions"}:
        return "Dictionary / custom data object"
    if lowered.endswith("_history") or lowered.endswith("_traces"):
        return "Array"
    return "Variant"


def _infer_field_representation(field: str) -> str:
    lowered = field.lower()
    if "emotion" in lowered:
        return "Affective state used for behavior modulation and social propagation."
    if "stress" in lowered:
        return "Physiological/psychological pressure state used in coping logic."
    if "hunger" in lowered:
        return "Nutritional deprivation level driving survival and action priorities."
    if "energy" in lowered:
        return "Fatigue/rest capacity controlling action readiness."
    if "social" in lowered:
        return "Social fulfillment/deficit level affecting mood and stress."
    if "position" in lowered:
        return "World-space location used for movement and proximity checks."
    if "age" in lowered:
        return "Lifecycle progression used for stage-specific behavior and events."
    if lowered == "id" or lowered.endswith("_id"):
        return "Stable entity identity used for referencing across systems."
    if "personality" in lowered or "trait" in lowered:
        return "Trait/axis profile used for sensitivity and decision weighting."
    if "action" in lowered or "goal" in lowered:
        return "Current behavior intent used by schedulers and downstream systems."
    return _humanize_field_name(field).capitalize() + "."


def _infer_field_typical_values(field: str) -> str:
    lowered = field.lower()
    if lowered in {"energy", "hunger", "social", "stress", "arousal", "valence"}:
        return "Normalized scalar (commonly 0.0-1.0 or 0-100 by system)."
    if lowered in {"age", "tick", "action_timer"}:
        return "Non-negative tick counts."
    if lowered.endswith("_stage") or lowered.endswith("_type"):
        return "Named categorical states."
    if lowered in {"position", "velocity"}:
        return "Grid/world vectors."
    if lowered == "id" or lowered.endswith("_id"):
        return "Positive integer identifiers."
    if lowered in {"emotion_data", "personality"}:
        return "Structured object with nested metrics/axes."
    return "System-defined value domain."


def _file_link(file_path: str, slug_by_file: dict[str, str]) -> str:
    slug = slug_by_file.get(file_path)
    if slug:
        return f"[`{slug}`]({slug}.md)"
    return f"`{file_path}`"


def _build_field_usage_map(entries: list[dict[str, Any]]) -> dict[str, set[str]]:
    usage: dict[str, set[str]] = defaultdict(set)
    for entry in entries:
        rel_file = entry.get("file")
        if not isinstance(rel_file, str) or not rel_file:
            continue
        for field in _unique_strings(entry.get("entity_fields", [])):
            usage[field].add(rel_file)
    return usage


def _render_system_frontmatter(
    display_name: str,
    description: str,
    source_file: str,
    nav_order: int,
    slug: str,
) -> str:
    return (
        "---\n"
        f"title: {_yaml_quote(display_name)}\n"
        f"description: {_yaml_quote(description)}\n"
        "generated: true\n"
        "source_files:\n"
        f"  - {_yaml_quote(source_file)}\n"
        f"nav_order: {nav_order}\n"
        f"system_name: {_yaml_quote(slug)}\n"
        "---\n"
    )


def _render_system_page(
    entry: dict[str, Any],
    slug_by_file: dict[str, str],
    constants_map: dict[str, dict[str, Any]],
    formulas_by_file: dict[str, list[dict[str, Any]]],
    imports_by_file: dict[str, list[dict[str, Any]]],
    signals_by_emitter: dict[str, list[dict[str, Any]]],
    manifest_signals: dict[str, dict[str, Any]],
    dependency_graph: dict[str, dict[str, list[str]]],
    field_access_map: dict[str, dict[str, set[str]]],
    field_usage_map: dict[str, set[str]],
    ticks_per_year: float | None,
    lang: str,
) -> str:
    rel_file = str(entry.get("file", ""))
    slug = slug_by_file.get(rel_file, "system")
    display_name = _display_name(entry, slug)
    doc_comment = _normalize_text(entry.get("doc_comment"))
    description = _first_sentence(doc_comment)

    priority = entry.get("priority")
    nav_order = priority if isinstance(priority, int) else 999
    priority_text = str(priority) if isinstance(priority, int) else "n/a"
    tick_interval_text = _tick_interval_text(entry)
    rel_field_access = field_access_map.get(rel_file, {})

    frontmatter = _render_system_frontmatter(
        display_name=display_name,
        description=description,
        source_file=rel_file,
        nav_order=nav_order,
        slug=slug,
    )

    formulas = formulas_by_file.get(rel_file, [])
    formulas = sorted(formulas, key=lambda item: (item.get("line_start", 0), item.get("name", "")))
    emitted_signals = signals_by_emitter.get(rel_file, [])
    pipeline_steps = _build_tick_pipeline(rel_file, entry, formulas, emitted_signals)
    pipeline_mermaid = _render_pipeline_mermaid(pipeline_steps)

    lines: list[str] = [frontmatter]
    lines.append(f"# {display_name}")
    lines.append("")
    lines.append(
        f"{t('label_source', lang)} `{rel_file}` | {t('label_priority', lang)}: {priority_text} | "
        f"{t('label_tick_interval', lang)}: {tick_interval_text}"
    )
    lines.append("")

    lines.append(f"## {t('section_overview', lang)}")
    lines.append("")
    model_text = ", ".join(_academic_models(entry, formulas))
    lines.append(
        f"The **{display_name}** system implements {model_text} to simulate "
        f"{_domain_description(entry, display_name)}."
    )
    lines.append(
        f"It runs {_tick_interval_overview(entry, ticks_per_year)} at priority **{priority_text}**."
    )
    lines.append("")
    lines.append(f"**{t('label_core_entity_data', lang)}**: {_core_entity_data_text(entry, rel_field_access)}")
    lines.append("")
    if doc_comment:
        lines.append(f"> {_first_sentence(doc_comment)}")
        lines.append("")

    lines.append(f"## {t('section_tick_pipeline', lang)}")
    lines.append("")
    if pipeline_steps:
        for index, step in enumerate(pipeline_steps, start=1):
            label = str(step.get("label", "Execute pipeline step"))
            lines.append(f"{index}. {label}")
            start = step.get("line_start")
            end = step.get("line_end")
            if isinstance(start, int) and isinstance(end, int):
                if start == end:
                    lines.append(f"   📄 source: `{rel_file}:L{start}`")
                else:
                    lines.append(f"   📄 source: `{rel_file}:L{start}`")
            math_refs = step.get("math", [])
            if isinstance(math_refs, list) and math_refs:
                lines.append(f"   Math context: {', '.join(_md_cell(item) for item in math_refs)}")
        lines.append("")
        if pipeline_mermaid:
            lines.append(f"### {t('section_pipeline_diagram', lang)}")
            lines.append("")
            lines.append(pipeline_mermaid)
            lines.append("")
    else:
        lines.append(t("phrase_no_tick_pipeline", lang))
        lines.append("")

    lines.append(f"## {t('section_formulas', lang)}")
    lines.append("")
    if formulas:
        for formula in formulas:
            purpose = _normalize_text(formula.get("purpose"))
            title = purpose or _formula_title(str(formula.get("name", "formula")))
            lines.append(f"### {title}")
            lines.append("")

            model_ref = formula.get("model_ref")
            if isinstance(model_ref, dict):
                model_name = _normalize_text(model_ref.get("name")) or "Unspecified model"
                reference = _normalize_text(model_ref.get("reference")) or "reference unavailable"
                lines.append(f"**Model**: {model_name} ({reference})")
                lines.append("")
                formula_text = model_ref.get("formula")
                if isinstance(formula_text, str) and formula_text.strip():
                    lines.append("$$")
                    lines.append(formula_text.strip())
                    lines.append("$$")
                    lines.append("")
            else:
                latex = _code_to_latex(str(formula.get("code_snippet", "")))
                if latex:
                    lines.append("$$")
                    lines.append(latex)
                    lines.append("$$")
                    lines.append("")

            if purpose:
                lines.append(f"**Interpretation**: {purpose}")
                lines.append("")

            code_snippet = str(formula.get("code_snippet", "")).rstrip()
            if code_snippet:
                lines.append("**GDScript**:")
                lines.append("```gdscript")
                lines.append(code_snippet)
                lines.append("```")
                lines.append("")

            variables = formula.get("variables")
            if isinstance(variables, dict) and variables:
                rows: list[list[str]] = []
                for variable, meaning in variables.items():
                    rows.append([f"`{variable}`", str(meaning)])
                lines.append(
                    _render_markdown_table(
                        ["Variable", "Meaning"],
                        rows,
                    )
                )
                lines.append("")

            line_start = formula.get("line_start")
            if isinstance(line_start, int):
                lines.append(f"📄 source: `{rel_file}:L{line_start}`")
                lines.append("")
    else:
        lines.append("No extracted formulas for this module.")
        lines.append("")

    lines.append(f"## {t('section_config_reference', lang)}")
    lines.append("")
    config_rows = _build_configuration_rows(entry, constants_map)
    if config_rows:
        lines.append(
            _render_markdown_table(
                ["Constant", "Default", "Controls", "Behavior Effect"],
                [[f"`{name}`", value, controls, effect] for name, value, controls, effect in config_rows],
            )
        )
        lines.append("")
    else:
        lines.append(t("phrase_no_config_refs", lang))
        lines.append("")

    lines.append(f"## {t('section_cross_system_effects', lang)}")
    lines.append("")
    lines.append(f"### {t('section_imported_modules', lang)}")
    lines.append("")
    imports = imports_by_file.get(rel_file, [])
    if imports:
        for import_ref in sorted(imports, key=lambda item: (item.get("line", 0), item.get("to_file", ""))):
            target = str(import_ref.get("to_file", ""))
            import_type = str(import_ref.get("type", "import"))
            line_no = import_ref.get("line")
            target_text = _file_link(target, slug_by_file)
            if isinstance(line_no, int):
                lines.append(f"- {target_text} via `{import_type}` at `{rel_file}:L{line_no}`")
            else:
                lines.append(f"- {target_text} via `{import_type}`")
    else:
        lines.append(t("phrase_no_imports", lang))
    lines.append("")

    lines.append(f"### {t('section_shared_entity_fields', lang)}")
    lines.append("")
    shared_rows: list[list[str]] = []
    for field in _unique_strings(entry.get("entity_fields", [])):
        peers = sorted(field_usage_map.get(field, set()) - {rel_file})
        if not peers:
            continue
        peer_links = ", ".join(_file_link(peer, slug_by_file) for peer in peers)
        access = _field_access_text(rel_field_access.get(field, set()))
        shared_rows.append([f"`{field}`", access, peer_links])
    if shared_rows:
        lines.append(_render_markdown_table(["Field", "Access", "Shared With"], shared_rows))
        read_shared = [
            f"`{field}`"
            for field in _unique_strings(entry.get("entity_fields", []))
            if field_usage_map.get(field, set()) - {rel_file}
            and "read" in rel_field_access.get(field, set())
        ]
        write_shared = [
            f"`{field}`"
            for field in _unique_strings(entry.get("entity_fields", []))
            if field_usage_map.get(field, set()) - {rel_file}
            and "write" in rel_field_access.get(field, set())
        ]
        if read_shared:
            lines.append("")
            lines.append(f"{t('phrase_reads_shared_fields', lang)}: {', '.join(read_shared)}")
        if write_shared:
            lines.append("")
            lines.append(f"{t('phrase_writes_shared_fields', lang)}: {', '.join(write_shared)}")
    else:
        lines.append(t("phrase_no_shared_fields", lang))
    lines.append("")

    lines.append(f"### {t('section_signals', lang)}")
    lines.append("")
    if emitted_signals:
        signal_rows: list[list[str]] = []
        seen_signals: set[tuple[str, int | None]] = set()
        for signal in sorted(
            emitted_signals,
            key=lambda item: (item.get("signal_name", ""), item.get("emitter_line", 0)),
        ):
            signal_name = str(signal.get("signal_name", "")).strip()
            if not signal_name:
                continue
            emitter_line = signal.get("emitter_line") if isinstance(signal.get("emitter_line"), int) else None
            marker = (signal_name, emitter_line)
            if marker in seen_signals:
                continue
            seen_signals.add(marker)

            signal_meta = manifest_signals.get(signal_name, {})
            params_text = _normalize_text(signal_meta.get("params")) or "unknown"

            subscribers: list[str] = []
            local_subscribers = signal.get("subscribers", [])
            if isinstance(local_subscribers, list):
                for subscriber in local_subscribers:
                    if isinstance(subscriber, dict):
                        file_path = subscriber.get("file")
                        if isinstance(file_path, str) and file_path:
                            subscribers.append(file_path)
            manifest_subscribers = signal_meta.get("subscribers", [])
            if isinstance(manifest_subscribers, list):
                for file_path in manifest_subscribers:
                    if isinstance(file_path, str) and file_path:
                        subscribers.append(file_path)

            deduped_subscribers = []
            seen_subscribers: set[str] = set()
            for file_path in subscribers:
                if file_path in seen_subscribers:
                    continue
                seen_subscribers.add(file_path)
                deduped_subscribers.append(file_path)

            subscriber_text = ", ".join(_file_link(file_path, slug_by_file) for file_path in deduped_subscribers)
            if not subscriber_text:
                subscriber_text = "No known subscribers"

            line_suffix = f"L{emitter_line}" if emitter_line is not None else "n/a"
            signal_rows.append([f"`{signal_name}`", params_text, subscriber_text, line_suffix])

        if signal_rows:
            lines.append(
                _render_markdown_table(
                    ["Signal", "Parameters", "Subscribers", "Source Line"],
                    signal_rows,
                )
            )
        else:
            lines.append(t("phrase_no_signals", lang))
    else:
        lines.append(t("phrase_no_signals", lang))
    lines.append("")

    lines.append(f"### {t('section_downstream_impact', lang)}")
    lines.append("")
    downstream = dependency_graph.get(rel_file, {}).get("depended_by", [])
    if isinstance(downstream, list) and downstream:
        for dep in sorted(_unique_strings(downstream)):
            lines.append(f"- {_file_link(dep, slug_by_file)} depends on this system's outputs.")
    else:
        lines.append(f"- {t('phrase_no_downstream', lang)}")
    lines.append("")

    lines.append(f"## {t('section_entity_data_model', lang)}")
    lines.append("")
    field_rows: list[list[str]] = []
    ordered_fields = _unique_strings(entry.get("entity_fields", []))
    for field in sorted(rel_field_access.keys()):
        if field not in ordered_fields:
            ordered_fields.append(field)
    for field in ordered_fields:
        access = _field_access_text(rel_field_access.get(field, set()))
        field_rows.append(
            [
                f"`{field}`",
                access,
                _infer_field_type(field),
                _infer_field_representation(field),
                _infer_field_typical_values(field),
            ]
        )
    if field_rows:
        lines.append(
            _render_markdown_table(
                ["Field", "Access", "Type", "Represents", "Typical Values"],
                field_rows,
            )
        )
        lines.append("")
    else:
        lines.append("No entity field metadata extracted for this module.")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def run(manifest: dict, extracted: dict | None = None, lang: str = "ko") -> dict:
    """Generate one narrative documentation page per system module."""
    warnings: list[str] = []
    errors: list[str] = []
    files_written: list[str] = []

    dirs = config.lang_dirs(lang)
    config.ensure_dir(dirs["systems"])

    systems_path = os.path.join(config.EXTRACTED_DIR, "systems.json")
    formulas_path = os.path.join(config.EXTRACTED_DIR, "formulas.json")
    references_path = os.path.join(config.EXTRACTED_DIR, "references.json")
    constants_path = os.path.join(config.EXTRACTED_DIR, "constants.json")

    systems_payload = _load_payload(extracted, "systems", systems_path, "systems.json", warnings)
    formulas_payload = _load_payload(extracted, "formulas", formulas_path, "formulas.json", warnings)
    references_payload = _load_payload(extracted, "references", references_path, "references.json", warnings)
    constants_payload = _load_payload(extracted, "constants", constants_path, "constants.json", warnings)

    entries = list(manifest.get("systems", [])) + list(manifest.get("ai_modules", []))
    if not entries:
        warnings.append("No systems or ai_modules in manifest; nothing generated.")
        return {
            "files_written": [],
            "items_processed": 0,
            "warnings": warnings,
            "errors": errors,
        }

    systems_by_file: dict[str, dict[str, Any]] = {}
    for system_entry in _list_of_dicts(systems_payload.get("systems", [])):
        file_path = system_entry.get("file")
        if isinstance(file_path, str) and file_path:
            systems_by_file[file_path] = system_entry

    merged_entries: list[dict[str, Any]] = []
    for entry in entries:
        rel_file = entry.get("file")
        if not isinstance(rel_file, str) or not rel_file:
            warnings.append("Skipped manifest entry with missing file path.")
            continue
        merged = dict(entry)
        merged.update(systems_by_file.get(rel_file, {}))
        merged_entries.append(merged)

    slug_by_file = _resolve_slug_collisions(merged_entries)

    constants_map: dict[str, dict[str, Any]] = {}
    for constant in _list_of_dicts(constants_payload.get("constants", [])):
        name = constant.get("name")
        if isinstance(name, str) and name:
            constants_map[name] = constant

    formulas_by_file: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for formula in _list_of_dicts(formulas_payload.get("formulas", [])):
        file_path = formula.get("file")
        if isinstance(file_path, str) and file_path:
            formulas_by_file[file_path].append(formula)

    imports_by_file: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for import_ref in _list_of_dicts(references_payload.get("imports", [])):
        from_file = import_ref.get("from_file")
        if isinstance(from_file, str) and from_file:
            imports_by_file[from_file].append(import_ref)

    signals_by_emitter: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for signal in _list_of_dicts(references_payload.get("signals", [])):
        emitter = signal.get("emitter")
        if isinstance(emitter, str) and emitter:
            signals_by_emitter[emitter].append(signal)

    field_access_map: dict[str, dict[str, set[str]]] = defaultdict(lambda: defaultdict(set))
    for access in _list_of_dicts(references_payload.get("entity_field_access", [])):
        file_path = access.get("file")
        field_name = access.get("field")
        access_type = access.get("access_type")
        if not (isinstance(file_path, str) and isinstance(field_name, str)):
            continue
        if access_type in {"read", "write"}:
            field_access_map[file_path][field_name].add(access_type)

    dependency_graph = references_payload.get("dependency_graph", {})
    if not isinstance(dependency_graph, dict):
        dependency_graph = {}

    manifest_signals = manifest.get("signals", {})
    if not isinstance(manifest_signals, dict):
        manifest_signals = {}

    ordered_entries = sorted(
        merged_entries,
        key=lambda item: (
            item.get("priority") if isinstance(item.get("priority"), int) else 10_000,
            _display_name(item, slug_by_file.get(item.get("file", ""), "system")),
        ),
    )

    ticks_per_year = _ticks_per_year(constants_map)
    field_usage_map = _build_field_usage_map(ordered_entries)

    for entry in ordered_entries:
        rel_file = entry.get("file")
        if not isinstance(rel_file, str) or not rel_file:
            continue

        slug = slug_by_file.get(rel_file, "system")
        page_content = _render_system_page(
            entry=entry,
            slug_by_file=slug_by_file,
            constants_map=constants_map,
            formulas_by_file=formulas_by_file,
            imports_by_file=imports_by_file,
            signals_by_emitter=signals_by_emitter,
            manifest_signals=manifest_signals,
            dependency_graph=dependency_graph,
            field_access_map=field_access_map,
            field_usage_map=field_usage_map,
            ticks_per_year=ticks_per_year,
            lang=lang,
        )

        output_path = os.path.join(dirs["systems"], f"{slug}.md")
        if _write_markdown(output_path, page_content, warnings, errors):
            files_written.append(output_path)

    return {
        "files_written": files_written,
        "items_processed": len(ordered_entries),
        "warnings": warnings,
        "errors": errors,
    }
