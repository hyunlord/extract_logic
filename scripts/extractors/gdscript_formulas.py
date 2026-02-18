"""Phase 2 extractor: detect formula-like math logic in GDScript modules."""

from __future__ import annotations

import json
import os
import re
from datetime import datetime, timezone

import scripts.config as config

_FUNC_RE = re.compile(r"^(\s*)func\s+([A-Za-z_]\w*)\s*\(")
_MODEL_KEYWORDS = (
    "siler",
    "ornstein-uhlenbeck",
    "ou process",
    "plutchik",
    "gaussian",
    "box-muller",
    "hazard",
    "mortality",
    "decay",
    "appraisal",
)
_DOC_MODEL_KEYWORDS = (
    "siler",
    "ornstein",
    "ou process",
    "plutchik",
    "gaussian",
    "box-muller",
)
_MATH_CALL_RE = re.compile(
    r"\b(exp|log|pow|sqrt|sin|cos|abs|clamp|clampf|lerp|lerpf)\s*\("
)
_CALLABLE_RE = re.compile(r"\b([A-Za-z_]\w*)\s*\(")
_TOKEN_RE = re.compile(r"\b([A-Za-z_]\w*)\b")
_SIMPLE_ASSIGN_RE = re.compile(
    r'^\s*(?:var\s+)?[A-Za-z_]\w*\s*=\s*(?:-?\d+(?:\.\d+)?|true|false|null|"[^"]*"|\'[^\']*\')\s*$'
)
_INC_ASSIGN_RE = re.compile(r"^\s*[A-Za-z_][\w\.\[\]]*\s*[\+\-]=\s*-?\d+(?:\.\d+)?\s*$")
_BANNED_VARIABLES = {
    "and",
    "as",
    "break",
    "class_name",
    "const",
    "continue",
    "elif",
    "else",
    "extends",
    "false",
    "for",
    "func",
    "if",
    "in",
    "not",
    "null",
    "or",
    "pass",
    "return",
    "signal",
    "true",
    "var",
    "while",
}
_COMMON_CALLS = {
    "abs",
    "clamp",
    "clampf",
    "cos",
    "emit_event",
    "exp",
    "float",
    "int",
    "lerp",
    "lerpf",
    "log",
    "maxf",
    "minf",
    "pow",
    "posmod",
    "print",
    "push_warning",
    "randf",
    "randfn",
    "range",
    "sin",
    "sqrt",
    "str",
}


def _indent_size(line: str) -> int:
    size = 0
    for ch in line:
        if ch == " ":
            size += 1
        elif ch == "\t":
            size += 4
        else:
            break
    return size


def _math_operator_count(line: str) -> int:
    return len(re.findall(r"(?<![<>=!+\-*/])[\+\-\*/](?![=])", line))


def _is_simple_assignment(stripped: str) -> bool:
    return bool(_SIMPLE_ASSIGN_RE.match(stripped))


def _line_has_formula_signal(line: str, func_name: str) -> bool:
    stripped = line.strip()
    if not stripped or stripped.startswith("#"):
        return False
    if stripped.startswith(("if ", "elif ", "for ", "while ", "match ")):
        return False
    if _INC_ASSIGN_RE.match(stripped):
        return False
    if any(op in stripped for op in ("==", "!=", "<=", ">=")) and not _MATH_CALL_RE.search(stripped):
        return False
    if _MATH_CALL_RE.search(stripped):
        return True
    op_count = _math_operator_count(stripped)
    if op_count >= 3 and not _is_simple_assignment(stripped):
        return True

    lower = stripped.lower()
    if any(
        token in lower
        for token in (
            "* exp(-",
            "half_life",
            "decay_rate",
            "growth_rate",
            "normal_distribution",
            "standard deviation",
            " variance",
            " sigma",
            "randfn(",
            "randf()",
        )
    ):
        return True
    if re.search(r"(apprais|evaluat|calculat|comput)", func_name, re.IGNORECASE):
        if op_count >= 2 and not _is_simple_assignment(stripped):
            return True
        if "randf(" in lower or "randfn(" in lower:
            return True
    return False


def _is_doc_formula_line(line: str) -> bool:
    stripped = line.strip()
    if not stripped.startswith("#"):
        return False
    text = stripped.lstrip("#").strip().lower()
    if not text:
        return False
    if any(keyword in text for keyword in _DOC_MODEL_KEYWORDS):
        return True
    if "process" in text and any(keyword in text for keyword in ("decay", "hazard", "appraisal")):
        return True
    if "=" in text and any(op in text for op in ("+", "-", "*", "/", "^")):
        return True
    return bool(re.search(r"[μσθ]\s*\(", text))


def _collect_modules(manifest: dict) -> list[dict]:
    modules: list[dict] = []
    seen: set[str] = set()
    for key in ("systems", "ai_modules", "core_modules"):
        for entry in manifest.get(key, []):
            file_path = entry.get("file")
            if file_path and file_path not in seen:
                modules.append(entry)
                seen.add(file_path)
    return modules


def _resolve_source_file(manifest: dict, relative_path: str) -> str:
    candidate = config.source_path(*relative_path.replace("\\", "/").split("/"))
    if os.path.exists(candidate):
        return candidate
    source_repo = manifest.get("source_repo", "")
    if source_repo:
        alt = os.path.join(source_repo, relative_path)
        if os.path.exists(alt):
            return alt
    return candidate


def _extract_assigned_name(lines: list[str]) -> str | None:
    for line in lines:
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        match = re.match(r"^(?:var\s+)?([A-Za-z_]\w*)\s*=", stripped)
        if match:
            return match.group(1)
    return None


def _description_from_context(comment_text: str, func_name: str, snippet: str) -> str:
    if comment_text:
        return comment_text
    lowered = snippet.lower()
    for keyword in _MODEL_KEYWORDS:
        if keyword in lowered:
            return f"{keyword.title()} formula logic extracted from {func_name}"
    return f"Formula logic extracted from {func_name}"


def _category_from_context(module: dict, func_name: str, snippet: str) -> str:
    raw_name = module.get("system_name", "")
    if not raw_name:
        base = os.path.splitext(os.path.basename(module.get("file", "")))[0]
        raw_name = base.replace("_system", "")

    text = " ".join([raw_name, func_name, snippet]).lower()
    if any(key in text for key in ("mortality", "siler", "hazard")):
        return "mortality"
    if any(key in text for key in ("emotion", "plutchik", "valence", "arousal", "appraisal")):
        return "emotion"
    if any(key in text for key in ("decay", "half_life", "exp(-", "memory_trace")):
        return "decay"
    if any(key in text for key in ("personality", "trait", "ornstein", "ou process", "maturation")):
        return "personality"
    if any(key in text for key in ("needs", "hunger", "energy", "metabolic")):
        return "needs"
    if any(key in text for key in ("movement", "path", "speed")):
        return "movement"

    normalized = raw_name.strip().lower()
    if normalized == "emotions":
        return "emotion"
    return normalized or "general"


def _name_from_context(func_name: str, snippet_lines: list[str], description: str, line_start: int) -> str:
    lowered = "\n".join(snippet_lines).lower()
    if "siler" in lowered and "hazard" in lowered:
        return "siler_hazard_rate"
    if "ornstein" in lowered or "ou process" in lowered:
        return "ornstein_uhlenbeck_update"
    if "box-muller" in lowered:
        return "box_muller_normal"
    if "appraisal" in lowered:
        return f"{func_name}_appraisal"

    assigned = _extract_assigned_name(snippet_lines)
    if assigned:
        return f"{func_name}_{assigned}"
    return f"{func_name}_line_{line_start}"


def _guess_variable_meaning(name: str) -> str:
    lower = name.lower()
    if lower in {"a1", "a2", "a3"}:
        return "coefficient term"
    if lower in {"b1", "b2", "b3"}:
        return "rate coefficient"
    if lower.startswith("mu"):
        return "hazard or mean term"
    if lower.startswith("q_") or "prob" in lower:
        return "probability term"
    if "decay" in lower:
        return "decay factor"
    if "growth" in lower:
        return "growth factor"
    if "rate" in lower:
        return "rate parameter"
    if "half_life" in lower:
        return "half-life value"
    if "sigma" in lower:
        return "standard deviation/noise scale"
    if "theta" in lower:
        return "mean reversion coefficient"
    if "age" in lower:
        return "age-related input"
    if "hunger" in lower or "nutrition" in lower:
        return "nutrition state input"
    return name.replace("_", " ")


def _extract_variables(snippet: str) -> dict[str, str]:
    cleaned_lines: list[str] = []
    for line in snippet.splitlines():
        code = line.split("#", 1)[0]
        code = re.sub(r'"[^"]*"|\'[^\']*\'', "", code)
        if code.strip():
            cleaned_lines.append(code)
    cleaned = "\n".join(cleaned_lines)

    callables = set(_CALLABLE_RE.findall(cleaned))
    variables: dict[str, str] = {}
    for token in _TOKEN_RE.findall(cleaned):
        if token in _BANNED_VARIABLES or token in _COMMON_CALLS:
            continue
        if token in callables:
            continue
        if token.isupper():
            continue
        if re.fullmatch(r"[A-Z][A-Za-z0-9_]*", token):
            continue
        if token not in variables:
            variables[token] = _guess_variable_meaning(token)
        if len(variables) >= 16:
            break
    return variables


def _collect_comment_context(lines: list[str], start_idx: int) -> str:
    comments: list[str] = []
    idx = start_idx - 1
    while idx >= 0:
        stripped = lines[idx].strip()
        if stripped.startswith("#"):
            comments.append(stripped.lstrip("#").strip())
            idx -= 1
            continue
        if not stripped:
            idx -= 1
            continue
        break
    comments.reverse()
    return " ".join(c for c in comments if c)


def _extract_file_references(file_text: str, data_files: list[dict]) -> list[str]:
    mentions = set(re.findall(r"SpeciesManager\.(\w+)", file_text))
    mentions.update(re.findall(r"([A-Za-z0-9_]+)\.json", file_text))

    references: set[str] = set()
    for data in data_files:
        rel = data.get("file", "")
        if not rel:
            continue
        base = os.path.basename(rel)
        stem = os.path.splitext(base)[0]
        for mention in mentions:
            mention_lower = mention.lower()
            stem_lower = stem.lower()
            if (
                mention_lower == stem_lower
                or mention_lower.endswith("_" + stem_lower)
                or stem_lower in mention_lower
            ):
                references.add(base)
                break
    return sorted(references)


def _extract_doc_formulas(
    module: dict,
    lines: list[str],
    references: list[str],
) -> list[dict]:
    formulas: list[dict] = []
    idx = 0
    while idx < len(lines):
        if not _is_doc_formula_line(lines[idx]):
            idx += 1
            continue
        start = idx
        block = [lines[idx].strip().lstrip("#").strip()]
        idx += 1
        while idx < len(lines) and lines[idx].strip().startswith("#"):
            block.append(lines[idx].strip().lstrip("#").strip())
            idx += 1
            if len(block) >= 20:
                break
        snippet = "\n".join(line for line in block if line).strip()
        if not snippet:
            continue
        description = snippet.split("\n", 1)[0]
        name = _name_from_context("doc", [snippet], description, start + 1)
        formulas.append(
            {
                "system": module.get("system_name")
                or os.path.splitext(os.path.basename(module.get("file", "")))[0].replace("_system", ""),
                "file": module.get("file", ""),
                "name": name,
                "description": description,
                "line_start": start + 1,
                "line_end": min(start + len(block), len(lines)),
                "code_snippet": snippet,
                "variables": _extract_variables(snippet),
                "references": references,
                "category": _category_from_context(module, "doc", snippet),
            }
        )
    return formulas


def _extract_function_formulas(
    module: dict,
    lines: list[str],
    references: list[str],
) -> list[dict]:
    formulas: list[dict] = []
    idx = 0
    while idx < len(lines):
        match = _FUNC_RE.match(lines[idx])
        if not match:
            idx += 1
            continue

        func_indent = _indent_size(match.group(1))
        func_name = match.group(2)
        body_start = idx + 1
        cursor = body_start
        while cursor < len(lines):
            stripped = lines[cursor].strip()
            if not stripped:
                cursor += 1
                continue
            if _indent_size(lines[cursor]) <= func_indent and not stripped.startswith("#"):
                break
            cursor += 1
        body_end = cursor
        body = [(line_no + 1, lines[line_no]) for line_no in range(body_start, body_end)]

        bidx = 0
        while bidx < len(body):
            line_no, line = body[bidx]
            if not _line_has_formula_signal(line, func_name):
                bidx += 1
                continue

            block_start = bidx

            block_end = bidx
            while block_end + 1 < len(body) and (block_end - block_start + 1) < 20:
                next_line = body[block_end + 1][1].strip()
                if not next_line:
                    break
                if next_line.startswith("#"):
                    break
                if _line_has_formula_signal(next_line, func_name):
                    block_end += 1
                    continue
                if _math_operator_count(next_line) >= 1 and not any(
                    op in next_line for op in ("==", "!=", "<=", ">=")
                ):
                    block_end += 1
                    continue
                break

            snippet_lines = [body[i][1].rstrip() for i in range(block_start, block_end + 1)]
            snippet = "\n".join(snippet_lines).strip()
            if snippet:
                comment_context = _collect_comment_context(lines, body[block_start][0] - 1)
                description = _description_from_context(comment_context, func_name, snippet)
                name = _name_from_context(func_name, snippet_lines, description, body[block_start][0])
                formulas.append(
                    {
                        "system": module.get("system_name")
                        or os.path.splitext(os.path.basename(module.get("file", "")))[0].replace("_system", ""),
                        "file": module.get("file", ""),
                        "name": name,
                        "description": description,
                        "line_start": body[block_start][0],
                        "line_end": body[block_end][0],
                        "code_snippet": snippet,
                        "variables": _extract_variables(snippet),
                        "references": references,
                        "category": _category_from_context(module, func_name, snippet),
                    }
                )

            bidx = block_end + 1

        idx = body_end if body_end > idx else idx + 1

    return formulas


def run(manifest: dict) -> dict:
    """Extract formula-like math logic from system/core/AI GDScript files."""
    files_written: list[str] = []
    warnings: list[str] = []
    errors: list[str] = []
    formulas: list[dict] = []

    modules = _collect_modules(manifest)
    if not modules:
        warnings.append("No modules found in manifest under systems/core_modules/ai_modules.")

    for module in modules:
        relative_file = module.get("file", "")
        if not relative_file:
            warnings.append(f"Manifest entry missing file path: {module}")
            continue

        source_file = _resolve_source_file(manifest, relative_file)
        if not os.path.exists(source_file):
            warnings.append(f"Missing source file, skipping: {relative_file}")
            continue

        try:
            with open(source_file, "r", encoding="utf-8") as f:
                content = f.read()
        except OSError as exc:
            warnings.append(f"Failed to read {relative_file}: {exc}")
            continue

        lines = content.splitlines()
        refs = _extract_file_references(content, manifest.get("data_files", []))
        formulas.extend(_extract_doc_formulas(module, lines, refs))
        formulas.extend(_extract_function_formulas(module, lines, refs))

    deduped: list[dict] = []
    seen: set[tuple[str, int, int, str]] = set()
    for formula in formulas:
        key = (
            formula.get("file", ""),
            formula.get("line_start", 0),
            formula.get("line_end", 0),
            formula.get("name", ""),
        )
        if key in seen:
            continue
        seen.add(key)
        deduped.append(formula)

    deduped.sort(key=lambda x: (x.get("file", ""), x.get("line_start", 0), x.get("name", "")))

    by_category: dict[str, int] = {}
    for formula in deduped:
        category = formula.get("category", "general")
        by_category[category] = by_category.get(category, 0) + 1

    payload = {
        "extracted_at": datetime.now(timezone.utc).isoformat(),
        "formulas": deduped,
        "categories": sorted(by_category.keys()),
        "stats": {
            "total_formulas": len(deduped),
            "by_category": dict(sorted(by_category.items())),
        },
    }

    try:
        config.ensure_dir(config.EXTRACTED_DIR)
        output_path = os.path.join(config.EXTRACTED_DIR, "formulas.json")
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(payload, f, indent=2, ensure_ascii=False)
        files_written.append(output_path)
    except OSError as exc:
        errors.append(f"Failed to write formulas.json: {exc}")

    return {
        "files_written": files_written,
        "items_processed": len(deduped),
        "warnings": warnings,
        "errors": errors,
    }
