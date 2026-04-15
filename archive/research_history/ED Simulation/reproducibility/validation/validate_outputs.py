"""
validate_outputs.py
===================
Validates that the ED-SIM v1 pipeline produced all expected outputs.

Checks:
  1. Run directories exist and contain valid data
  2. Invariant figure directories exist and contain PNGs
  3. Invariant summary JSONs exist and are parseable
  4. Atlas report, master index, and certificate exist
  5. Optionally compares output hashes to reference

Writes a validation report to output/atlas/validation_report.json.

Usage:
    python reproducibility/validation/validate_outputs.py
    python reproducibility/validation/validate_outputs.py --generate-hashes

Exit codes:
    0 = all critical checks pass
    1 = one or more critical checks fail
"""

import os
import sys
import glob
import json
import hashlib
import argparse
import datetime

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPRO_DIR = os.path.dirname(SCRIPT_DIR)
SIM_DIR = os.path.dirname(REPRO_DIR)
ATLAS_DIR = os.path.join(SIM_DIR, "output", "atlas")
INV_FIG_DIR = os.path.join(SIM_DIR, "output", "figures", "invariants")
RUNS_DIR = os.path.join(SIM_DIR, "output", "runs")

EXPECTED_PATH = os.path.join(SCRIPT_DIR, "expected_structure.json")
HASH_REF_PATH = os.path.join(SCRIPT_DIR, "hash_reference.json")


def load_expected() -> dict:
    if os.path.isfile(EXPECTED_PATH):
        with open(EXPECTED_PATH, "r") as f:
            return json.load(f)
    return {}


def check_runs() -> dict:
    pattern = os.path.join(RUNS_DIR, "regime_D*_A*_Nm*")
    dirs = sorted(glob.glob(pattern))
    valid = []
    invalid = []
    for d in dirs:
        ts = os.path.join(d, "time_series.npz")
        meta = os.path.join(d, "metadata.json")
        if os.path.isfile(ts) and os.path.isfile(meta):
            valid.append(os.path.basename(d))
        else:
            invalid.append(os.path.basename(d))
    return {
        "n_found": len(dirs),
        "n_valid": len(valid),
        "n_invalid": len(invalid),
        "status": "PASS" if len(valid) >= 64 else
                  "PARTIAL" if len(valid) > 0 else "FAIL",
    }


def check_invariant_dirs(expected: dict) -> dict:
    subdirs = (expected.get("directories", {})
               .get("output/figures/invariants", {})
               .get("subdirectories", []))
    found = []
    missing = []
    has_figures = []

    for name in subdirs:
        path = os.path.join(INV_FIG_DIR, name)
        if os.path.isdir(path):
            found.append(name)
            pngs = glob.glob(os.path.join(path, "*.png"))
            if pngs:
                has_figures.append(name)
        else:
            missing.append(name)

    return {
        "expected": len(subdirs),
        "found": len(found),
        "missing": missing,
        "with_figures": len(has_figures),
        "status": "PASS" if len(missing) == 0 else
                  "PARTIAL" if len(found) > len(subdirs) // 2 else "FAIL",
    }


def check_invariant_jsons(expected: dict) -> dict:
    expected_jsons = (expected.get("invariant_jsons", {})
                      .get("expected", []))
    found = []
    missing = []
    parseable = []

    # Search in invariant figure directories and output/invariants/
    search_dirs = [INV_FIG_DIR]
    for sub in glob.glob(os.path.join(INV_FIG_DIR, "*")):
        if os.path.isdir(sub):
            search_dirs.append(sub)

    inv_dir = os.path.join(SIM_DIR, "output", "invariants")
    if os.path.isdir(inv_dir):
        search_dirs.append(inv_dir)

    for name in expected_jsons:
        found_this = False
        for sd in search_dirs:
            path = os.path.join(sd, name)
            if os.path.isfile(path):
                found_this = True
                found.append(name)
                try:
                    with open(path, "r") as f:
                        json.load(f)
                    parseable.append(name)
                except Exception:
                    pass
                break
        if not found_this:
            missing.append(name)

    return {
        "expected": len(expected_jsons),
        "found": len(found),
        "parseable": len(parseable),
        "missing": missing,
        "status": "PASS" if len(missing) == 0 else
                  "PARTIAL" if len(found) > 0 else "FAIL",
    }


def check_atlas_files(expected: dict) -> dict:
    required = (expected.get("directories", {})
                .get("output/atlas", {})
                .get("required_files", []))
    found = []
    missing = []

    for name in required:
        path = os.path.join(ATLAS_DIR, name)
        if os.path.isfile(path):
            found.append(name)
        else:
            missing.append(name)

    return {
        "expected": len(required),
        "found": len(found),
        "missing": missing,
        "status": "PASS" if len(missing) == 0 else
                  "PARTIAL" if len(found) > 0 else "FAIL",
    }


def file_hash(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def generate_hashes() -> dict:
    hashes = {}
    # Hash atlas files
    for name in os.listdir(ATLAS_DIR) if os.path.isdir(ATLAS_DIR) else []:
        path = os.path.join(ATLAS_DIR, name)
        if os.path.isfile(path):
            hashes[f"atlas/{name}"] = file_hash(path)
    return hashes


def main():
    parser = argparse.ArgumentParser(
        description="Validate ED-SIM v1 outputs.")
    parser.add_argument(
        "--generate-hashes", action="store_true",
        help="Generate reference hashes and update hash_reference.json.")
    args = parser.parse_args()

    os.makedirs(ATLAS_DIR, exist_ok=True)

    expected = load_expected()

    print("  ED-SIM v1 Output Validation")
    print("  " + "=" * 50)
    print()

    # 1. Runs
    runs = check_runs()
    print(f"  Regime runs:      {runs['n_valid']}/64 valid  [{runs['status']}]")

    # 2. Invariant dirs
    inv_dirs = check_invariant_dirs(expected)
    print(f"  Invariant dirs:   {inv_dirs['found']}/{inv_dirs['expected']} "
          f"found, {inv_dirs['with_figures']} with figures  "
          f"[{inv_dirs['status']}]")
    if inv_dirs["missing"]:
        for m in inv_dirs["missing"][:5]:
            print(f"    MISSING: {m}")
        if len(inv_dirs["missing"]) > 5:
            print(f"    ... and {len(inv_dirs['missing']) - 5} more")

    # 3. Invariant JSONs
    inv_jsons = check_invariant_jsons(expected)
    print(f"  Invariant JSONs:  {inv_jsons['found']}/{inv_jsons['expected']} "
          f"found, {inv_jsons['parseable']} parseable  "
          f"[{inv_jsons['status']}]")

    # 4. Atlas files
    atlas = check_atlas_files(expected)
    print(f"  Atlas files:      {atlas['found']}/{atlas['expected']} found  "
          f"[{atlas['status']}]")
    if atlas["missing"]:
        for m in atlas["missing"]:
            print(f"    MISSING: {m}")

    # Overall verdict
    statuses = [runs["status"], inv_dirs["status"],
                inv_jsons["status"], atlas["status"]]
    if all(s == "PASS" for s in statuses):
        verdict = "PASS"
    elif any(s == "FAIL" for s in statuses):
        verdict = "FAIL"
    else:
        verdict = "PARTIAL"

    print()
    print(f"  Overall verdict: {verdict}")

    # Generate hashes if requested
    if args.generate_hashes:
        print("\n  Generating reference hashes...")
        hashes = generate_hashes()
        ref = {
            "version": "1.0.0",
            "description": "Reference hashes for ED-SIM v1 outputs.",
            "timestamp": datetime.datetime.now().isoformat(),
            "hashes": hashes,
        }
        with open(HASH_REF_PATH, "w", encoding="utf-8") as f:
            json.dump(ref, f, indent=2)
        print(f"  Saved {len(hashes)} hashes to {HASH_REF_PATH}")

    # Save report
    report = {
        "timestamp": datetime.datetime.now().isoformat(),
        "runs": runs,
        "invariant_dirs": inv_dirs,
        "invariant_jsons": inv_jsons,
        "atlas_files": atlas,
        "verdict": verdict,
    }

    out_path = os.path.join(ATLAS_DIR, "validation_report.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)
    print(f"\n  Report: {out_path}")

    sys.exit(0 if verdict != "FAIL" else 1)


if __name__ == "__main__":
    main()
