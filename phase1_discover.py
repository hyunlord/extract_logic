"""Phase 1: DISCOVER — Scan the game repository and build manifest.json.

Discovers all .gd files, .json data files, and localization files.
Extracts basic metadata from each file without deep parsing.
Outputs: extracted/manifest.json
"""

import glob
import json
import os
import re
import subprocess
from datetime import datetime, timezone

import scripts.config as config


def _glob_source(pattern: str) -> list[str]:
    """Glob a pattern relative to SOURCE_REPO, return relative paths."""
    full_pattern = os.path.join(config.SOURCE_REPO, pattern)
    results = glob.glob(full_pattern, recursive=True)
    return sorted(
        os.path.relpath(r, config.SOURCE_REPO)
        for r in results
        if os.path.relpath(r, config.SOURCE_REPO) not in config.IGNORE_FILES
    )


def _get_git_commit() -> str:
    """Get current git commit hash of the source repo."""
    try:
        result = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=config.SOURCE_REPO,
            capture_output=True,
            text=True,
            timeout=5,
        )
        return result.stdout.strip()[:12] if result.returncode == 0 else "unknown"
    except Exception:
        return "unknown"


def _quick_gd_metadata(filepath: str) -> dict:
    """Extract quick metadata from a .gd file without full parsing."""
    meta = {"file": filepath, "lines": 0}
    full_path = config.source_path(filepath)
    if not os.path.exists(full_path):
        return meta

    with open(full_path, "r", encoding="utf-8") as f:
        content = f.read()

    meta["lines"] = content.count("\n") + 1

    # extends
    m = re.search(r'extends\s+"([^"]+)"', content)
    if m:
        meta["extends"] = m.group(1)
    else:
        m = re.search(r"extends\s+(\w+)", content)
        if m:
            meta["extends"] = m.group(1)

    # class_name
    m = re.search(r"class_name\s+(\w+)", content)
    if m:
        meta["class_name"] = m.group(1)

    # system_name (for simulation systems)
    m = re.search(r'system_name\s*=\s*"(\w+)"', content)
    if m:
        meta["system_name"] = m.group(1)

    # priority
    m = re.search(r"priority\s*=\s*(\d+)", content)
    if m:
        meta["priority"] = int(m.group(1))

    # tick_interval
    m = re.search(r"tick_interval\s*=\s*(.+?)(?:\s*#|$)", content, re.MULTILINE)
    if m:
        val = m.group(1).strip()
        try:
            meta["tick_interval"] = int(val)
        except ValueError:
            meta["tick_interval_raw"] = val

    # Doc comments (## at file top)
    doc_lines = []
    for line in content.split("\n"):
        stripped = line.strip()
        if stripped.startswith("##"):
            doc_lines.append(stripped[2:].strip())
        elif stripped.startswith("extends") or stripped.startswith("const") or stripped == "":
            continue
        else:
            break
    if doc_lines:
        meta["doc_comment"] = " ".join(doc_lines)

    # Imports / preloads
    imports = re.findall(r'(?:preload|load)\(\s*"([^"]+)"\s*\)', content)
    if imports:
        meta["imports"] = imports

    # GameConfig references
    config_refs = sorted(set(re.findall(r"GameConfig\.(\w+)", content)))
    if config_refs:
        meta["config_refs"] = config_refs

    # SpeciesManager references
    species_refs = sorted(set(re.findall(r"SpeciesManager\.(\w+)", content)))
    if species_refs:
        meta["species_refs"] = species_refs

    # SimulationBus signal emissions
    signal_emits = sorted(set(re.findall(r"SimulationBus\.(\w+)\.emit", content)))
    event_emits = re.findall(r'SimulationBus\.emit_event\(\s*"(\w+)"', content)
    if signal_emits or event_emits:
        meta["signals_emitted"] = sorted(set(signal_emits + event_emits))

    # SimulationBus signal connections
    signal_connects = sorted(set(re.findall(r"SimulationBus\.(\w+)\.connect", content)))
    if signal_connects:
        meta["signals_connected"] = signal_connects

    # Entity field access patterns
    entity_fields = sorted(set(re.findall(r"entity\.(\w+)", content)))
    if entity_fields:
        meta["entity_fields"] = entity_fields

    return meta


def _quick_json_metadata(filepath: str) -> dict:
    """Extract quick metadata from a JSON data file."""
    meta = {"file": filepath}
    full_path = config.source_path(filepath)
    if not os.path.exists(full_path):
        return meta

    try:
        with open(full_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        meta["lines"] = sum(1 for _ in open(full_path, encoding="utf-8"))

        if isinstance(data, dict):
            meta["type"] = "object"
            meta["top_level_keys"] = sorted(data.keys())
            meta["keys_count"] = len(data)
        elif isinstance(data, list):
            meta["type"] = "array"
            meta["items_count"] = len(data)
            if data and isinstance(data[0], dict):
                meta["item_keys"] = sorted(data[0].keys())
        else:
            meta["type"] = type(data).__name__

        # Derive category from directory structure
        parts = filepath.replace("\\", "/").split("/")
        if len(parts) > 2:
            meta["category"] = "/".join(parts[1:-1])
        else:
            meta["category"] = parts[0] if parts else ""

    except (json.JSONDecodeError, OSError) as e:
        meta["error"] = str(e)

    return meta


def _quick_locale_metadata(filepath: str) -> dict:
    """Extract metadata from a localization JSON file."""
    meta = {"file": filepath}
    full_path = config.source_path(filepath)

    parts = filepath.replace("\\", "/").split("/")
    # localization/ko/emotions.json → lang=ko, category=emotions
    if len(parts) >= 3:
        meta["lang"] = parts[1]
        meta["category"] = os.path.splitext(parts[2])[0]

    try:
        with open(full_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, dict):
            meta["keys_count"] = len(data)
            meta["sample_keys"] = sorted(data.keys())[:5]
    except (json.JSONDecodeError, OSError) as e:
        meta["error"] = str(e)

    return meta


def _discover_signals() -> dict:
    """Parse SimulationBus signal definitions."""
    bus_path = config.source_path("scripts", "core", "simulation_bus.gd")
    signals = {}
    if not os.path.exists(bus_path):
        return signals

    with open(bus_path, "r", encoding="utf-8") as f:
        for line in f:
            m = re.match(r"signal\s+(\w+)\(([^)]*)\)", line.strip())
            if m:
                name = m.group(1)
                params = m.group(2).strip()
                signals[name] = {"params": params, "emitters": [], "subscribers": []}

    return signals


def run() -> dict:
    """Execute Phase 1: Discover all source files and build manifest.

    Returns: The manifest dict (also written to extracted/manifest.json).
    """
    warnings = []

    # ── Discover files ──
    system_files = []
    for pattern in config.SYSTEM_GLOBS:
        system_files.extend(_glob_source(pattern))

    core_files = []
    for pattern in config.CORE_GLOBS:
        core_files.extend(_glob_source(pattern))

    ai_files = []
    for pattern in config.AI_GLOBS:
        ai_files.extend(_glob_source(pattern))

    data_files = []
    for pattern in config.DATA_GLOBS:
        data_files.extend(_glob_source(pattern))

    locale_files = []
    for pattern in config.LOCALE_GLOBS:
        locale_files.extend(_glob_source(pattern))

    # ── Extract metadata ──
    systems = [_quick_gd_metadata(f) for f in system_files]
    core_modules = [_quick_gd_metadata(f) for f in core_files]
    ai_modules = [_quick_gd_metadata(f) for f in ai_files]
    data_entries = [_quick_json_metadata(f) for f in data_files]
    locale_entries = [_quick_locale_metadata(f) for f in locale_files]

    # ── Discover signals and wire emitters/subscribers ──
    signals = _discover_signals()
    all_gd = systems + core_modules + ai_modules
    for gd_meta in all_gd:
        for sig in gd_meta.get("signals_emitted", []):
            if sig in signals:
                signals[sig]["emitters"].append(gd_meta["file"])
        for sig in gd_meta.get("signals_connected", []):
            if sig in signals:
                signals[sig]["subscribers"].append(gd_meta["file"])

    # ── Derive locale categories ──
    locale_categories = sorted(set(
        e.get("category", "") for e in locale_entries if "category" in e
    ))

    # ── Stats ──
    total_gd = len(system_files) + len(core_files) + len(ai_files)
    total_gd_lines = sum(m.get("lines", 0) for m in all_gd)
    total_locale_keys = sum(e.get("keys_count", 0) for e in locale_entries)

    # ── Build manifest ──
    manifest = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source_repo": config.SOURCE_REPO,
        "source_commit": _get_git_commit(),
        "systems": systems,
        "core_modules": core_modules,
        "ai_modules": ai_modules,
        "data_files": data_entries,
        "locale_files": locale_entries,
        "locale_categories": locale_categories,
        "signals": signals,
        "stats": {
            "total_gd_files": total_gd,
            "total_system_files": len(system_files),
            "total_core_files": len(core_files),
            "total_ai_files": len(ai_files),
            "total_json_data_files": len(data_files),
            "total_locale_files": len(locale_files),
            "total_locale_keys": total_locale_keys,
            "total_locale_categories": len(locale_categories),
            "total_lines_gd": total_gd_lines,
        },
    }

    # ── Write manifest ──
    config.ensure_dir(config.EXTRACTED_DIR)
    manifest_path = os.path.join(config.EXTRACTED_DIR, "manifest.json")
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)

    print(f"\n[discover] Manifest written to {manifest_path}")
    print(f"[discover] Systems: {len(systems)}")
    print(f"[discover] Core modules: {len(core_modules)}")
    print(f"[discover] AI modules: {len(ai_modules)}")
    print(f"[discover] Data files: {len(data_entries)}")
    print(f"[discover] Locale files: {len(locale_entries)} ({total_locale_keys} keys)")
    print(f"[discover] Locale categories: {locale_categories}")
    print(f"[discover] Signals: {len(signals)}")
    print(f"[discover] Total GDScript: {total_gd} files, {total_gd_lines} lines")

    return manifest


if __name__ == "__main__":
    run()
