"""Phase 2: EXTRACT — Run all extractors to parse source code into structured JSON.

Calls each extractor module in order. Each writes its output to extracted/.
All extractors follow the run(manifest) -> result dict interface.
"""

import scripts.config as config


def run(manifest: dict) -> dict:
    """Run all Phase 2 extraction modules sequentially.

    Args:
        manifest: The manifest.json data from Phase 1.

    Returns:
        Aggregated result dict with files_written, items_processed, warnings, errors.
    """
    config.ensure_all_dirs()

    extractors = [
        ("gdscript_constants", "scripts.extractors.gdscript_constants"),
        ("gdscript_systems", "scripts.extractors.gdscript_systems"),
        ("gdscript_formulas", "scripts.extractors.gdscript_formulas"),
        ("gdscript_references", "scripts.extractors.gdscript_references"),
        ("json_data", "scripts.extractors.json_data"),
        ("locale", "scripts.extractors.locale"),
        # v2 semantic extractors
        ("trait_data", "scripts.extractors.trait_data"),
        ("stressor_data", "scripts.extractors.stressor_data"),
        ("emotion_presets", "scripts.extractors.emotion_presets"),
        ("decay_config", "scripts.extractors.decay_config"),
    ]

    all_files = []
    all_items = 0
    all_warnings = []
    all_errors = []

    for name, module_path in extractors:
        print(f"  [phase2] Running {name}...")
        try:
            mod = __import__(module_path, fromlist=["run"])
            result = mod.run(manifest)
            all_files.extend(result.get("files_written", []))
            all_items += result.get("items_processed", 0)
            all_warnings.extend(result.get("warnings", []))
            all_errors.extend(result.get("errors", []))
            print(f"  [phase2] {name}: {result.get('items_processed', 0)} items, "
                  f"{len(result.get('warnings', []))} warnings")
        except Exception as e:
            msg = f"{name} failed: {e}"
            print(f"  [phase2] ERROR: {msg}")
            all_errors.append(msg)

    return {
        "files_written": all_files,
        "items_processed": all_items,
        "warnings": all_warnings,
        "errors": all_errors,
    }
