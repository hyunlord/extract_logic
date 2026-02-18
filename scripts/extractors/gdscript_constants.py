"""Extract constants, enums, dictionaries, and function signatures from game_config.gd."""

import json
import os
import re
from datetime import datetime, timezone

import scripts.config as config

_CONST_OR_VAR_RE = re.compile(
    r"^(const|var)\s+([A-Za-z_]\w*)(?:\s*:\s*([^=:#]+?))?\s*(?::=|=)\s*(.*)$"
)
_ENUM_RE = re.compile(r"^enum\s+([A-Za-z_]\w*)\s*\{(.*)$")
_FUNC_RE = re.compile(
    r"^(static\s+)?func\s+([A-Za-z_]\w*)\s*\((.*)\)\s*(?:->\s*([^:]+))?\s*:\s*$"
)
_MATH_TOKEN_RE = re.compile(
    r"\s*(\d+(?:_\d+)*(?:\.\d+(?:_\d+)*)?|[()+\-*/%])"
)

_MATH_PRECEDENCE = {
    "u+": 3,
    "u-": 3,
    "*": 2,
    "/": 2,
    "%": 2,
    "+": 1,
    "-": 1,
}
_MATH_ASSOC = {
    "u+": "right",
    "u-": "right",
    "*": "left",
    "/": "left",
    "%": "left",
    "+": "left",
    "-": "left",
}


def _is_top_level(line: str) -> bool:
    return line[:1] not in (" ", "\t")


def _strip_inline_comment(text: str) -> str:
    in_string = False
    string_char = ""
    escaped = False

    for idx, char in enumerate(text):
        if in_string:
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == string_char:
                in_string = False
            continue

        if char in ('"', "'"):
            in_string = True
            string_char = char
            continue

        if char == "#":
            return text[:idx]

    return text


def _expression_depth_delta(text: str) -> int:
    in_string = False
    string_char = ""
    escaped = False
    delta = 0

    stripped = _strip_inline_comment(text)
    for char in stripped:
        if in_string:
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == string_char:
                in_string = False
            continue

        if char in ('"', "'"):
            in_string = True
            string_char = char
            continue

        if char in "{[(":
            delta += 1
        elif char in "}])":
            delta -= 1

    return delta


def _collect_multiline_expression(lines: list[str], start_idx: int, initial_expr: str) -> tuple[str, int]:
    parts = [initial_expr.rstrip("\n")]
    depth = _expression_depth_delta(initial_expr)
    idx = start_idx

    while depth > 0 and idx + 1 < len(lines):
        idx += 1
        next_line = lines[idx].rstrip("\n")
        parts.append(next_line)
        depth += _expression_depth_delta(next_line)

    return "\n".join(parts).strip(), idx


def _split_top_level(text: str, delimiter: str) -> list[str]:
    parts: list[str] = []
    current: list[str] = []
    depth_brace = 0
    depth_bracket = 0
    depth_paren = 0
    in_string = False
    string_char = ""
    escaped = False

    for char in text:
        if in_string:
            current.append(char)
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == string_char:
                in_string = False
            continue

        if char in ('"', "'"):
            in_string = True
            string_char = char
            current.append(char)
            continue

        if char == "{":
            depth_brace += 1
        elif char == "}":
            depth_brace -= 1
        elif char == "[":
            depth_bracket += 1
        elif char == "]":
            depth_bracket -= 1
        elif char == "(":
            depth_paren += 1
        elif char == ")":
            depth_paren -= 1

        if (
            char == delimiter
            and depth_brace == 0
            and depth_bracket == 0
            and depth_paren == 0
        ):
            part = "".join(current).strip()
            if part:
                parts.append(part)
            current = []
            continue

        current.append(char)

    tail = "".join(current).strip()
    if tail:
        parts.append(tail)

    return parts


def _tokenize_math(expr: str) -> list[str] | None:
    tokens: list[str] = []
    idx = 0
    while idx < len(expr):
        match = _MATH_TOKEN_RE.match(expr, idx)
        if not match:
            return None
        token = match.group(1)
        tokens.append(token)
        idx = match.end()
    return tokens


def _math_to_rpn(tokens: list[str]) -> list[object] | None:
    output: list[object] = []
    ops: list[str] = []
    prev_type = "start"

    for token in tokens:
        if token[0].isdigit():
            number = token.replace("_", "")
            value: int | float
            value = float(number) if "." in number else int(number)
            output.append(value)
            prev_type = "number"
            continue

        if token == "(":
            ops.append(token)
            prev_type = "("
            continue

        if token == ")":
            while ops and ops[-1] != "(":
                output.append(ops.pop())
            if not ops or ops[-1] != "(":
                return None
            ops.pop()
            prev_type = ")"
            continue

        if token in "+-" and prev_type in ("start", "op", "("):
            op = "u+" if token == "+" else "u-"
        else:
            op = token
            if op in ("*", "/", "%") and prev_type in ("start", "op", "("):
                return None

        while ops and ops[-1] != "(":
            top = ops[-1]
            if (
                (_MATH_ASSOC[op] == "left" and _MATH_PRECEDENCE[op] <= _MATH_PRECEDENCE[top])
                or (
                    _MATH_ASSOC[op] == "right"
                    and _MATH_PRECEDENCE[op] < _MATH_PRECEDENCE[top]
                )
            ):
                output.append(ops.pop())
                continue
            break

        ops.append(op)
        prev_type = "op"

    while ops:
        op = ops.pop()
        if op == "(":
            return None
        output.append(op)

    return output


def _eval_simple_math(expr: str) -> int | float | None:
    tokens = _tokenize_math(expr)
    if not tokens:
        return None

    rpn = _math_to_rpn(tokens)
    if rpn is None:
        return None

    stack: list[int | float] = []
    for token in rpn:
        if isinstance(token, (int, float)):
            stack.append(token)
            continue

        if token in ("u+", "u-"):
            if not stack:
                return None
            value = stack.pop()
            stack.append(+value if token == "u+" else -value)
            continue

        if len(stack) < 2:
            return None
        right = stack.pop()
        left = stack.pop()
        try:
            if token == "+":
                stack.append(left + right)
            elif token == "-":
                stack.append(left - right)
            elif token == "*":
                stack.append(left * right)
            elif token == "/":
                stack.append(left / right)
            elif token == "%":
                stack.append(left % right)
            else:
                return None
        except ZeroDivisionError:
            return None

    if len(stack) != 1:
        return None
    return stack[0]


def _parse_simple_math(value_raw: str) -> str | None:
    expr = value_raw.strip()
    if not expr:
        return None

    if not re.fullmatch(r"[0-9_\s+\-*/().%]+", expr):
        return None
    value = _eval_simple_math(expr)
    if value is None:
        return None
    return str(value)


def _parse_int_literal(value_raw: str) -> int | None:
    expr = value_raw.strip().replace("_", "")
    if not expr:
        return None

    if re.fullmatch(r"[-+]?\d+", expr):
        return int(expr)

    computed = _parse_simple_math(expr)
    if computed is None:
        return None

    if re.fullmatch(r"[-+]?\d+", computed):
        return int(computed)

    return None


def _extract_doc_comment(comment_lines: list[str]) -> str | None:
    if not comment_lines:
        return None
    return " ".join(line.strip() for line in comment_lines if line.strip())


def _extract_dict_keys(dict_literal: str) -> list[str]:
    literal = dict_literal.strip()
    start = literal.find("{")
    end = literal.rfind("}")
    if start < 0 or end <= start:
        return []

    inner = literal[start + 1 : end]
    entries = _split_top_level(inner, ",")

    keys: list[str] = []
    for entry in entries:
        key_chars: list[str] = []
        depth_brace = 0
        depth_bracket = 0
        depth_paren = 0
        in_string = False
        string_char = ""
        escaped = False
        key_done = False

        for char in entry:
            if in_string:
                key_chars.append(char)
                if escaped:
                    escaped = False
                elif char == "\\":
                    escaped = True
                elif char == string_char:
                    in_string = False
                continue

            if char in ('"', "'"):
                in_string = True
                string_char = char
                key_chars.append(char)
                continue

            if char == "{":
                depth_brace += 1
            elif char == "}":
                depth_brace -= 1
            elif char == "[":
                depth_bracket += 1
            elif char == "]":
                depth_bracket -= 1
            elif char == "(":
                depth_paren += 1
            elif char == ")":
                depth_paren -= 1

            if (
                char == ":"
                and depth_brace == 0
                and depth_bracket == 0
                and depth_paren == 0
            ):
                key_done = True
                break

            key_chars.append(char)

        if not key_done:
            continue

        key_text = "".join(key_chars).strip()
        if len(key_text) >= 2 and key_text[0] == key_text[-1] and key_text[0] in ('"', "'"):
            key_text = key_text[1:-1]

        if key_text:
            keys.append(key_text)

    return keys


def _preview_literal(value_raw: str) -> str:
    compact = re.sub(r"\s+", " ", value_raw.strip())
    return compact[:200]


def _parse_enum_values(enum_literal: str) -> dict:
    literal = enum_literal.strip()
    start = literal.find("{")
    end = literal.rfind("}")
    if start < 0 or end <= start:
        return {}

    inner = literal[start + 1 : end]
    entries = _split_top_level(inner, ",")

    values: dict[str, int | str] = {}
    next_value = 0

    for entry in entries:
        if not entry:
            continue

        if "=" in entry:
            left, right = entry.split("=", 1)
            key = left.strip()
            raw_val = right.strip()
            parsed_val = _parse_int_literal(raw_val)
            if parsed_val is None:
                values[key] = raw_val
            else:
                values[key] = parsed_val
                next_value = parsed_val + 1
            continue

        key = entry.strip()
        values[key] = next_value
        next_value += 1

    return values


def _parse_game_config(lines: list[str]) -> dict:
    constants: list[dict] = []
    enums: list[dict] = []
    dictionaries: list[dict] = []
    functions: list[dict] = []

    doc_buffer: list[str] = []
    idx = 0

    while idx < len(lines):
        line = lines[idx].rstrip("\n")
        stripped = line.strip()

        if _is_top_level(line) and stripped.startswith("##"):
            doc_buffer.append(stripped[2:].strip())
            idx += 1
            continue

        if stripped == "":
            doc_buffer = []
            idx += 1
            continue

        if not _is_top_level(line):
            idx += 1
            continue

        doc_comment = _extract_doc_comment(doc_buffer)
        doc_buffer = []

        enum_match = _ENUM_RE.match(stripped)
        if enum_match:
            enum_name = enum_match.group(1)
            enum_literal, end_idx = _collect_multiline_expression(lines, idx, stripped[stripped.find("{") :])
            enum_entry = {
                "name": enum_name,
                "values": _parse_enum_values(enum_literal),
                "line": idx + 1,
            }
            if doc_comment:
                enum_entry["comment"] = doc_comment
            enums.append(enum_entry)
            idx = end_idx + 1
            continue

        decl_match = _CONST_OR_VAR_RE.match(stripped)
        if decl_match:
            decl_type, name, annotation, value_raw = decl_match.groups()
            value_expr = _strip_inline_comment(value_raw).strip()
            end_idx = idx

            if _expression_depth_delta(value_expr) > 0:
                value_expr, end_idx = _collect_multiline_expression(lines, idx, value_expr)

            computed = _parse_simple_math(value_expr)
            constant_entry = {
                "name": name,
                "type": decl_type,
                "value": computed if computed is not None else value_expr,
                "value_raw": value_expr,
                "line": idx + 1,
            }
            if annotation:
                constant_entry["type_annotation"] = annotation.strip()
            if doc_comment:
                constant_entry["comment"] = doc_comment
            constants.append(constant_entry)

            if value_expr.lstrip().startswith("{"):
                dict_entry = {
                    "name": name,
                    "keys": _extract_dict_keys(value_expr),
                    "line": idx + 1,
                    "value_preview": _preview_literal(value_expr),
                }
                if doc_comment:
                    dict_entry["comment"] = doc_comment
                dictionaries.append(dict_entry)

            idx = end_idx + 1
            continue

        func_match = _FUNC_RE.match(stripped)
        if func_match:
            is_static, name, params, returns = func_match.groups()
            function_entry = {
                "name": name,
                "params": params.strip(),
                "returns": returns.strip() if returns else "unknown",
                "line": idx + 1,
            }
            if is_static:
                function_entry["static"] = True
            if doc_comment:
                function_entry["doc_comment"] = doc_comment
            functions.append(function_entry)

            idx += 1
            continue

        idx += 1

    return {
        "constants": constants,
        "enums": enums,
        "dictionaries": dictionaries,
        "functions": functions,
    }


def run(manifest: dict) -> dict:
    """Extract constants from game_config.gd.

    Returns:
        dict with keys: files_written, items_processed, warnings, errors
    """
    warnings: list[str] = []
    errors: list[str] = []
    files_written: list[str] = []

    source_rel_path = os.path.join("scripts", "core", "game_config.gd")
    source_file = config.source_path("scripts", "core", "game_config.gd")

    manifest_source_repo = manifest.get("source_repo") if isinstance(manifest, dict) else None
    if manifest_source_repo:
        source_file = os.path.join(manifest_source_repo, source_rel_path)

    if not os.path.exists(source_file):
        warnings.append(f"Missing source file, skipping: {source_file}")
        return {
            "files_written": files_written,
            "items_processed": 0,
            "warnings": warnings,
            "errors": errors,
        }

    try:
        with open(source_file, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except OSError as exc:
        errors.append(f"Failed to read source file: {exc}")
        return {
            "files_written": files_written,
            "items_processed": 0,
            "warnings": warnings,
            "errors": errors,
        }

    extracted = _parse_game_config(lines)

    output = {
        "source_file": source_rel_path.replace(os.sep, "/"),
        "extracted_at": datetime.now(timezone.utc).isoformat(),
        "constants": extracted["constants"],
        "enums": extracted["enums"],
        "dictionaries": extracted["dictionaries"],
        "functions": extracted["functions"],
        "stats": {
            "total_constants": len(extracted["constants"]),
            "total_enums": len(extracted["enums"]),
            "total_dicts": len(extracted["dictionaries"]),
            "total_functions": len(extracted["functions"]),
        },
    }

    config.ensure_dir(config.EXTRACTED_DIR)
    output_path = os.path.join(config.EXTRACTED_DIR, "constants.json")

    try:
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(output, f, indent=2, ensure_ascii=False)
    except OSError as exc:
        errors.append(f"Failed to write constants.json: {exc}")
        return {
            "files_written": files_written,
            "items_processed": 0,
            "warnings": warnings,
            "errors": errors,
        }

    files_written.append(output_path)
    items_processed = (
        output["stats"]["total_constants"]
        + output["stats"]["total_enums"]
        + output["stats"]["total_dicts"]
        + output["stats"]["total_functions"]
    )

    return {
        "files_written": files_written,
        "items_processed": items_processed,
        "warnings": warnings,
        "errors": errors,
    }
