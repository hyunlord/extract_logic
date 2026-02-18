"""Phase 3: GENERATE — Run all generators to produce Markdown documentation.

Calls each generator module in order. Each reads from extracted/ and writes to content/.
Nav builder runs last to scan all generated .md files and build mkdocs.yml.

Generators can use either interface:
  - run(manifest) -> result dict           (v1 generators)
  - run(manifest, extracted) -> result dict (v2 generators with enriched data)
"""

import inspect
import json
import os

import scripts.config as config

# Extracted JSON files to load for v2 generators
_EXTRACTED_FILES = {
    "constants": "constants.json",
    "systems": "systems.json",
    "formulas": "formulas.json",
    "references": "references.json",
    "signals": "signals.json",
    "data_files": "data_files.json",
    "locale": "locale.json",
    # v2 semantic extractions
    "trait_data": "trait_data.json",
    "stressor_data": "stressor_data.json",
    "emotion_presets": "emotion_presets.json",
    "decay_config": "decay_config.json",
}


def _load_extracted() -> dict:
    """Load all extracted JSON files into a single dict."""
    extracted = {}
    for key, filename in _EXTRACTED_FILES.items():
        path = os.path.join(config.EXTRACTED_DIR, filename)
        if os.path.exists(path):
            try:
                with open(path, "r", encoding="utf-8") as f:
                    extracted[key] = json.load(f)
            except (json.JSONDecodeError, OSError):
                extracted[key] = None
        else:
            extracted[key] = None
    return extracted


def run(manifest: dict) -> dict:
    """Run all Phase 3 generation modules sequentially.

    Args:
        manifest: The manifest.json data from Phase 1.

    Returns:
        Aggregated result dict with files_written, items_processed, warnings, errors.
    """
    config.ensure_all_dirs()

    # Load all extracted data for v2 generators
    extracted = _load_extracted()

    generators = [
        # v1 generators (use run(manifest))
        ("system_page", "scripts.generators.system_page"),
        ("data_page", "scripts.generators.data_page"),
        ("glossary_page", "scripts.generators.glossary_page"),
        ("config_reference", "scripts.generators.config_reference"),
        ("interaction_page", "scripts.generators.interaction_page"),
        ("core_page", "scripts.generators.core_page"),
        # v2 generators (use run(manifest, extracted))
        ("trait_page", "scripts.generators.trait_page"),
        ("emotion_detail", "scripts.generators.emotion_detail"),
        ("stress_detail", "scripts.generators.stress_detail"),
        ("mortality_detail", "scripts.generators.mortality_detail"),
        ("pipeline_page", "scripts.generators.pipeline_page"),
        # Always last
        ("index_page", "scripts.generators.index_page"),
        ("nav_builder", "scripts.generators.nav_builder"),  # Must run last
    ]

    all_files = []
    all_items = 0
    all_warnings = []
    all_errors = []

    for name, module_path in generators:
        print(f"  [phase3] Running {name}...")
        try:
            mod = __import__(module_path, fromlist=["run"])
            run_fn = mod.run

            # Auto-detect signature: pass extracted if the generator accepts it
            sig = inspect.signature(run_fn)
            if len(sig.parameters) >= 2:
                result = run_fn(manifest, extracted)
            else:
                result = run_fn(manifest)

            all_files.extend(result.get("files_written", []))
            all_items += result.get("items_processed", 0)
            all_warnings.extend(result.get("warnings", []))
            all_errors.extend(result.get("errors", []))
            print(f"  [phase3] {name}: {result.get('items_processed', 0)} items, "
                  f"{len(result.get('warnings', []))} warnings")
        except Exception as e:
            msg = f"{name} failed: {e}"
            print(f"  [phase3] ERROR: {msg}")
            all_errors.append(msg)

    return {
        "files_written": all_files,
        "items_processed": all_items,
        "warnings": all_warnings,
        "errors": all_errors,
    }
