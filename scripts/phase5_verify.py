"""Phase 5: VERIFY — Run all verification checks on generated documentation.

Calls each verifier module. Aggregates results into a verification report.
All verifiers follow the run(manifest) -> result dict interface.
"""

import json
import os

import scripts.config as config


def run(manifest: dict) -> dict:
    """Run all Phase 5 verification modules sequentially.

    Args:
        manifest: The manifest.json data from Phase 1.

    Returns:
        Aggregated result dict with files_written, items_processed, warnings, errors.
    """
    verifiers = [
        ("coverage", "scripts.verifiers.coverage"),
        ("consistency", "scripts.verifiers.consistency"),
        ("completeness", "scripts.verifiers.completeness"),
        ("links", "scripts.verifiers.links"),
    ]

    all_files = []
    all_items = 0
    all_warnings = []
    all_errors = []
    report = {}

    for name, module_path in verifiers:
        print(f"  [phase5] Running {name}...")
        try:
            mod = __import__(module_path, fromlist=["run"])
            result = mod.run(manifest)
            all_files.extend(result.get("files_written", []))
            all_items += result.get("items_processed", 0)
            all_warnings.extend(result.get("warnings", []))
            all_errors.extend(result.get("errors", []))
            # Collect verifier-specific data for report
            for key in result:
                if key not in ("files_written", "items_processed", "warnings", "errors"):
                    report[key] = result[key]
            status = "PASS" if not result.get("errors") else "FAIL"
            print(f"  [phase5] {name}: {status} — "
                  f"{len(result.get('warnings', []))} warnings, "
                  f"{len(result.get('errors', []))} errors")
        except Exception as e:
            msg = f"{name} failed: {e}"
            print(f"  [phase5] ERROR: {msg}")
            all_errors.append(msg)

    # Write verification report
    report_path = os.path.join(config.EXTRACTED_DIR, "verification_report.json")
    report["summary"] = {
        "total_warnings": len(all_warnings),
        "total_errors": len(all_errors),
        "status": "PASS" if not all_errors else "FAIL",
    }
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    all_files.append(report_path)

    if all_errors:
        print(f"\n  [phase5] VERIFICATION FAILED: {len(all_errors)} errors")
        for err in all_errors[:10]:
            print(f"    ❌ {err}")
    else:
        print(f"\n  [phase5] VERIFICATION PASSED: {len(all_warnings)} warnings")

    return {
        "files_written": all_files,
        "items_processed": all_items,
        "warnings": all_warnings,
        "errors": all_errors,
    }
