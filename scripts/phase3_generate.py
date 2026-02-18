"""Phase 3: GENERATE — Run all generators to produce Markdown documentation.

Calls each generator module in order. Each reads from extracted/ and writes to content/.
Nav builder runs last to scan all generated .md files and build mkdocs.yml.
All generators follow the run(manifest) -> result dict interface.
"""

import scripts.config as config


def run(manifest: dict) -> dict:
    """Run all Phase 3 generation modules sequentially.

    Args:
        manifest: The manifest.json data from Phase 1.

    Returns:
        Aggregated result dict with files_written, items_processed, warnings, errors.
    """
    config.ensure_all_dirs()

    generators = [
        ("system_page", "scripts.generators.system_page"),
        ("data_page", "scripts.generators.data_page"),
        ("glossary_page", "scripts.generators.glossary_page"),
        ("config_reference", "scripts.generators.config_reference"),
        ("interaction_page", "scripts.generators.interaction_page"),
        ("core_page", "scripts.generators.core_page"),
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
            result = mod.run(manifest)
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
