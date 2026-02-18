#!/usr/bin/env python3
"""WorldSim Docs — Single entry point for the entire extraction pipeline.

Usage:
    python scripts/extract_all.py              # Run full pipeline
    python scripts/extract_all.py --phase 1    # Run only Phase 1 (discover)
    python scripts/extract_all.py --phase 1-3  # Run Phases 1 through 3
    python scripts/extract_all.py --verify     # Run only Phase 5 (verify)
"""

import argparse
import json
import os
import sys
import time

# Add repo root to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import scripts.config as config


def load_manifest() -> dict:
    """Load manifest.json from extracted/ directory."""
    path = os.path.join(config.EXTRACTED_DIR, "manifest.json")
    if not os.path.exists(path):
        print("[pipeline] ERROR: manifest.json not found. Run Phase 1 first.")
        sys.exit(1)
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def run_phase(phase_num: int, manifest: dict = None) -> dict:
    """Run a single pipeline phase. Returns updated manifest if applicable."""
    phases = {
        1: ("DISCOVER", "scripts.phase1_discover"),
        2: ("EXTRACT", "scripts.phase2_extract"),
        3: ("GENERATE", "scripts.phase3_generate"),
        4: ("EXPORT", "scripts.phase4_export"),
        5: ("VERIFY", "scripts.phase5_verify"),
    }

    if phase_num not in phases:
        print(f"[pipeline] ERROR: Unknown phase {phase_num}")
        sys.exit(1)

    name, module_path = phases[phase_num]
    print(f"\n{'='*60}")
    print(f"  Phase {phase_num}: {name}")
    print(f"{'='*60}")

    start = time.time()

    try:
        module = __import__(module_path, fromlist=["run"])
        if phase_num == 1:
            result = module.run()
        else:
            if manifest is None:
                manifest = load_manifest()
            result = module.run(manifest)
    except ImportError as e:
        print(f"[pipeline] Phase {phase_num} module not yet implemented: {e}")
        return manifest or {}
    except Exception as e:
        print(f"[pipeline] Phase {phase_num} FAILED: {e}")
        import traceback
        traceback.print_exc()
        return manifest or {}

    elapsed = time.time() - start
    print(f"\n[Phase {phase_num}] Completed in {elapsed:.1f}s")

    if isinstance(result, dict):
        if "files_written" in result:
            print(f"  Files written: {len(result['files_written'])}")
        if "items_processed" in result:
            print(f"  Items processed: {result['items_processed']}")
        if "warnings" in result and result["warnings"]:
            print(f"  Warnings: {len(result['warnings'])}")
            for w in result["warnings"][:5]:
                print(f"    ⚠️  {w}")
            if len(result["warnings"]) > 5:
                print(f"    ... and {len(result['warnings']) - 5} more")
        if "errors" in result and result["errors"]:
            print(f"  ❌ Errors: {len(result['errors'])}")
            for e in result["errors"]:
                print(f"    ❌ {e}")

    # Phase 1 returns the manifest itself
    if phase_num == 1 and isinstance(result, dict) and "stats" in result:
        return result

    return manifest


def main():
    parser = argparse.ArgumentParser(description="WorldSim Docs extraction pipeline")
    parser.add_argument("--phase", type=str, default=None, help="Phase number or range (e.g., '1', '1-3')")
    parser.add_argument("--verify", action="store_true", help="Run only verification (Phase 5)")
    args = parser.parse_args()

    print("╔══════════════════════════════════════════════════════════╗")
    print("║        WorldSim Docs — Extraction Pipeline              ║")
    print("╚══════════════════════════════════════════════════════════╝")
    print(f"Source repo: {config.SOURCE_REPO}")
    print(f"Source exists: {os.path.isdir(config.SOURCE_REPO)}")

    if not os.path.isdir(config.SOURCE_REPO):
        print(f"\n[pipeline] ERROR: Source repo not found at {config.SOURCE_REPO}")
        print(f"[pipeline] Set WORLDSIM_SOURCE env var or place new-world/ as sibling directory.")
        sys.exit(1)

    config.ensure_all_dirs()

    total_start = time.time()

    if args.verify:
        manifest = load_manifest()
        run_phase(5, manifest)
    elif args.phase:
        if "-" in args.phase:
            start, end = map(int, args.phase.split("-"))
            phases = range(start, end + 1)
        else:
            phases = [int(args.phase)]

        manifest = None
        for p in phases:
            if p == 1:
                manifest = run_phase(1)
            else:
                manifest = run_phase(p, manifest)
    else:
        # Full pipeline
        manifest = run_phase(1)
        manifest = run_phase(2, manifest)
        run_phase(3, manifest)
        run_phase(4, manifest)
        run_phase(5, manifest)

    total_elapsed = time.time() - total_start
    print(f"\n{'='*60}")
    print(f"  Pipeline complete in {total_elapsed:.1f}s")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
