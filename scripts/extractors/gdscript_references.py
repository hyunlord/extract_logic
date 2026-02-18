"""Phase 2 extractor: build GDScript cross-references from source files.

Reads module file paths from manifest and scans .gd content for imports, signals,
config references, entity field access, and cross-system calls.
Outputs: extracted/references.json
"""

from __future__ import annotations

import json
import os
import re
from collections import defaultdict
from datetime import datetime, timezone

import scripts.config as config


IMPORT_CALL_RE = re.compile(r"\b(preload|load)\(\s*\"(res://[^\"]+)\"\s*\)")
ALIAS_IMPORT_RE = re.compile(
    r"\b(?:const|var)\s+(\w+)\s*=\s*(?:preload|load)\(\s*\"(res://[^\"]+)\"\s*\)"
)
GAMECONFIG_RE = re.compile(r"\bGameConfig\.(\w+)")
SPECIES_RE = re.compile(r"\bSpeciesManager\.(\w+)")
DATA_PATH_RE = re.compile(r"\"((?:res://)?(?:data|localization)/[^\"]+)\"")
FUNC_DECL_RE = re.compile(r"^\s*func\s+(\w+)\s*\(")
ENTITY_FIELD_RE = re.compile(r"\bentity\.(\w+)")
CROSS_CALL_RE = re.compile(r"\b(\w+)\.(\w+)\s*\(")

EMIT_SIGNAL_RE = re.compile(r"\.emit_signal\(\s*\"(\w+)\"")
SIMBUS_EMIT_RE = re.compile(r"\bSimulationBus\.(\w+)\.emit\s*\(")
GENERIC_EMIT_RE = re.compile(r"\b(\w+)\.emit\s*\(")
CONNECT_STRING_RE = re.compile(r"\.connect\(\s*\"(\w+)\"")
GENERIC_CONNECT_RE = re.compile(r"\b(\w+)\.connect\s*\(")


def _normalize_resource_path(path: str) -> str:
    """Normalize resource path to source-repo relative path style."""
    normalized = path.replace("\\", "/")
    if normalized.startswith("res://"):
        return normalized[6:]
    return normalized


def _manifest_gd_files(manifest: dict) -> list[str]:
    """Collect unique .gd file paths from manifest module sections."""
    files: set[str] = set()
    for key in ("systems", "core_modules", "ai_modules"):
        for entry in manifest.get(key, []):
            path = entry.get("file")
            if isinstance(path, str) and path.endswith(".gd"):
                files.add(path)
    return sorted(files)


def _is_system_process_scope(file_path: str) -> bool:
    """Return whether this file is considered a system module for entity access scan."""
    return file_path.startswith("scripts/systems/") or file_path.startswith("scripts/ai/")


def _extract_for_file(file_path: str) -> dict:
    """Scan one .gd source file and return extracted reference records."""
    full_path = config.source_path(file_path)
    result = {
        "missing": False,
        "imports": [],
        "config_refs": [],
        "entity_field_access": [],
        "cross_system_calls": [],
        "signal_emissions": [],
        "signal_connections": [],
        "dependency_targets": set(),
    }

    if not os.path.exists(full_path):
        result["missing"] = True
        return result

    with open(full_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    alias_imports: dict[str, dict[str, str]] = {}
    in_process_func = False
    track_entity_fields = _is_system_process_scope(file_path)

    for line_no, line in enumerate(lines, start=1):
        func_match = FUNC_DECL_RE.match(line)
        if func_match:
            func_name = func_match.group(1).lower()
            in_process_func = "process" in func_name

        for match in IMPORT_CALL_RE.finditer(line):
            import_type = match.group(1)
            target_file = _normalize_resource_path(match.group(2))
            result["imports"].append(
                {
                    "from_file": file_path,
                    "to_file": target_file,
                    "type": import_type,
                    "line": line_no,
                }
            )
            result["dependency_targets"].add(target_file)

        for match in ALIAS_IMPORT_RE.finditer(line):
            alias = match.group(1)
            target_file = _normalize_resource_path(match.group(2))
            alias_imports[alias] = {
                "path": target_file,
                "module": os.path.splitext(os.path.basename(target_file))[0],
            }

        for match in GAMECONFIG_RE.finditer(line):
            constant = match.group(1)
            result["config_refs"].append(
                {"file": file_path, "constant": constant, "line": line_no}
            )
            result["dependency_targets"].add("GameConfig")

        for _ in SPECIES_RE.finditer(line):
            result["dependency_targets"].add("SpeciesManager")

        for match in DATA_PATH_RE.finditer(line):
            data_path = _normalize_resource_path(match.group(1))
            result["dependency_targets"].add(data_path)

        emitted_on_line: set[str] = set()
        for match in EMIT_SIGNAL_RE.finditer(line):
            emitted_on_line.add(match.group(1))
        for match in SIMBUS_EMIT_RE.finditer(line):
            emitted_on_line.add(match.group(1))
        for match in GENERIC_EMIT_RE.finditer(line):
            emitted_on_line.add(match.group(1))

        for signal_name in sorted(emitted_on_line):
            result["signal_emissions"].append(
                {"signal_name": signal_name, "emitter": file_path, "emitter_line": line_no}
            )

        connected_on_line: set[str] = set()
        for match in CONNECT_STRING_RE.finditer(line):
            connected_on_line.add(match.group(1))
        for match in GENERIC_CONNECT_RE.finditer(line):
            connected_on_line.add(match.group(1))

        for signal_name in sorted(connected_on_line):
            result["signal_connections"].append(
                {"signal_name": signal_name, "file": file_path, "line": line_no}
            )

        if track_entity_fields and in_process_func:
            for match in ENTITY_FIELD_RE.finditer(line):
                field = match.group(1)
                remainder = line[match.end() :]
                access_type = (
                    "write" if re.match(r"\s*(?:[+\-*/%]?=)", remainder) else "read"
                )
                result["entity_field_access"].append(
                    {
                        "file": file_path,
                        "field": field,
                        "access_type": access_type,
                        "line": line_no,
                    }
                )

        if track_entity_fields:
            for match in CROSS_CALL_RE.finditer(line):
                alias = match.group(1)
                function_name = match.group(2)
                import_meta = alias_imports.get(alias)
                if not import_meta:
                    continue
                target_path = import_meta["path"]
                if not (
                    target_path.startswith("scripts/systems/")
                    or target_path.startswith("scripts/ai/")
                ):
                    continue

                result["cross_system_calls"].append(
                    {
                        "from_file": file_path,
                        "to_module": import_meta["module"],
                        "function": function_name,
                        "line": line_no,
                    }
                )
                result["dependency_targets"].add(target_path)

    return result


def _dedupe_sort(items: list[dict], keys: tuple[str, ...]) -> list[dict]:
    """Deduplicate list[dict] by key tuple and return sorted deterministic order."""
    seen: set[tuple] = set()
    output = []
    for item in items:
        marker = tuple(item.get(k) for k in keys)
        if marker in seen:
            continue
        seen.add(marker)
        output.append(item)
    return sorted(output, key=lambda item: tuple(item.get(k) for k in keys))


def _build_dependency_graph(
    gd_files: list[str],
    dependency_edges: set[tuple[str, str]],
) -> dict:
    """Build depends_on / depended_by adjacency summary."""
    file_set = set(gd_files)
    depends_on_map: dict[str, set[str]] = defaultdict(set)
    depended_by_map: dict[str, set[str]] = defaultdict(set)

    for from_file, target in dependency_edges:
        depends_on_map[from_file].add(target)
        if target in file_set:
            depended_by_map[target].add(from_file)

    graph = {}
    for file_path in sorted(gd_files):
        graph[file_path] = {
            "depends_on": sorted(depends_on_map.get(file_path, set())),
            "depended_by": sorted(depended_by_map.get(file_path, set())),
        }
    return graph


def run(manifest: dict) -> dict:
    """Main entry point.

    Args:
        manifest: The manifest.json data from Phase 1.

    Returns:
        dict with keys:
            - files_written
            - items_processed
            - warnings
            - errors
    """
    files_written: list[str] = []
    warnings: list[str] = []
    errors: list[str] = []

    gd_files = _manifest_gd_files(manifest)

    imports: list[dict] = []
    config_refs: list[dict] = []
    entity_field_access: list[dict] = []
    cross_system_calls: list[dict] = []
    signal_emissions: list[dict] = []
    signal_connections: list[dict] = []
    dependency_edges: set[tuple[str, str]] = set()

    processed_files = 0
    for file_path in gd_files:
        try:
            extracted = _extract_for_file(file_path)
        except OSError as exc:
            warnings.append(f"Failed to read source file {file_path}: {exc}")
            continue

        if extracted["missing"]:
            warnings.append(f"Missing source file: {file_path}")
            continue

        processed_files += 1
        imports.extend(extracted["imports"])
        config_refs.extend(extracted["config_refs"])
        entity_field_access.extend(extracted["entity_field_access"])
        cross_system_calls.extend(extracted["cross_system_calls"])
        signal_emissions.extend(extracted["signal_emissions"])
        signal_connections.extend(extracted["signal_connections"])

        for target in extracted["dependency_targets"]:
            dependency_edges.add((file_path, target))

    imports = _dedupe_sort(imports, ("from_file", "to_file", "type", "line"))
    config_refs = _dedupe_sort(config_refs, ("file", "constant", "line"))
    entity_field_access = _dedupe_sort(
        entity_field_access, ("file", "field", "access_type", "line")
    )
    cross_system_calls = _dedupe_sort(
        cross_system_calls, ("from_file", "to_module", "function", "line")
    )
    signal_emissions = _dedupe_sort(
        signal_emissions, ("signal_name", "emitter", "emitter_line")
    )
    signal_connections = _dedupe_sort(signal_connections, ("signal_name", "file", "line"))

    subscribers_by_signal: dict[str, list[dict]] = defaultdict(list)
    for connection in signal_connections:
        subscribers_by_signal[connection["signal_name"]].append(
            {"file": connection["file"], "line": connection["line"]}
        )

    signals: list[dict] = []
    signal_emitter_map: dict[str, set[str]] = defaultdict(set)
    for emission in signal_emissions:
        signal_name = emission["signal_name"]
        emitter = emission["emitter"]
        signal_emitter_map[signal_name].add(emitter)
        signals.append(
            {
                "signal_name": signal_name,
                "emitter": emitter,
                "emitter_line": emission["emitter_line"],
                "subscribers": sorted(
                    subscribers_by_signal.get(signal_name, []),
                    key=lambda item: (item["file"], item["line"]),
                ),
            }
        )

    signals = _dedupe_sort(signals, ("signal_name", "emitter", "emitter_line"))

    for signal_name, subscribers in subscribers_by_signal.items():
        emitters = signal_emitter_map.get(signal_name, set())
        if not emitters:
            continue
        for subscriber in subscribers:
            for emitter in emitters:
                dependency_edges.add((subscriber["file"], emitter))

    dependency_graph = _build_dependency_graph(gd_files, dependency_edges)

    references = {
        "extracted_at": datetime.now(timezone.utc).isoformat(),
        "imports": imports,
        "signals": signals,
        "config_refs": config_refs,
        "entity_field_access": entity_field_access,
        "cross_system_calls": cross_system_calls,
        "dependency_graph": dependency_graph,
        "stats": {
            "total_imports": len(imports),
            "total_signal_connections": len(signal_connections),
            "total_config_refs": len(config_refs),
            "total_cross_system_calls": len(cross_system_calls),
        },
    }

    try:
        config.ensure_dir(config.EXTRACTED_DIR)
        out_path = os.path.join(config.EXTRACTED_DIR, "references.json")
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(references, f, indent=2, ensure_ascii=False)
        files_written.append(out_path)
    except OSError as exc:
        errors.append(f"Failed to write references.json: {exc}")

    return {
        "files_written": files_written,
        "items_processed": processed_files,
        "warnings": warnings,
        "errors": errors,
    }


if __name__ == "__main__":
    manifest_path = os.path.join(config.EXTRACTED_DIR, "manifest.json")
    with open(manifest_path, "r", encoding="utf-8") as f:
        manifest_data = json.load(f)
    print(run(manifest_data))
