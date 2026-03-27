"""
check_data_integrity.py
=======================
Verifies that run directories contain valid data for the ED-SIM v1 pipeline.

Checks:
  - Run directories exist under output/runs/
  - Each run has time_series.npz and metadata.json
  - NPZ files are loadable and contain required fields
  - Metadata JSON is parseable and contains required keys
  - Reports missing, corrupted, or incomplete runs

Writes a JSON summary to output/atlas/data_integrity_check.json.

Usage:
    python reproducibility/checks/check_data_integrity.py
"""

import os
import sys
import glob
import json
import datetime
import numpy as np

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SIM_DIR = os.path.dirname(os.path.dirname(SCRIPT_DIR))
RUNS_DIR = os.path.join(SIM_DIR, "output", "runs")
ATLAS_DIR = os.path.join(SIM_DIR, "output", "atlas")

# Required fields in time_series.npz
REQUIRED_TS_FIELDS = ["t", "E_total", "v"]

# Required fields in metadata.json
REQUIRED_META_KEYS = ["D", "method", "N"]

# Run patterns to check
RUN_PATTERNS = [
    "regime_D*_A*_Nm*",
    "three_stage_*",
    "modal_*",
    "triad_cascade_*",
    "overlap_cascade_*",
    "broadband_*",
    "attractor_*",
    "param_D*",
]


def check_run(run_dir: str) -> dict:
    """Check a single run directory for completeness and validity."""
    name = os.path.basename(run_dir)
    result = {
        "name": name,
        "path": run_dir,
        "has_ts": False,
        "has_meta": False,
        "ts_valid": False,
        "meta_valid": False,
        "ts_fields": [],
        "meta_keys": [],
        "n_timesteps": 0,
        "issues": [],
        "status": "UNKNOWN",
    }

    # Check time_series.npz
    ts_path = os.path.join(run_dir, "time_series.npz")
    if os.path.isfile(ts_path):
        result["has_ts"] = True
        try:
            ts = np.load(ts_path, allow_pickle=True)
            fields = list(ts.keys())
            result["ts_fields"] = fields

            missing = [f for f in REQUIRED_TS_FIELDS if f not in fields]
            if missing:
                result["issues"].append(
                    f"Missing NPZ fields: {', '.join(missing)}")
            else:
                result["ts_valid"] = True
                t = ts["t"]
                result["n_timesteps"] = len(t)

                # Check for NaN/Inf
                for field in ["t", "E_total"]:
                    if field in ts:
                        arr = ts[field]
                        if np.any(np.isnan(arr)):
                            result["issues"].append(f"NaN in {field}")
                        if np.any(np.isinf(arr)):
                            result["issues"].append(f"Inf in {field}")

        except Exception as e:
            result["issues"].append(f"NPZ load error: {e}")
    else:
        result["issues"].append("time_series.npz missing")

    # Check metadata.json
    meta_path = os.path.join(run_dir, "metadata.json")
    if os.path.isfile(meta_path):
        result["has_meta"] = True
        try:
            with open(meta_path, "r") as f:
                meta = json.load(f)
            result["meta_keys"] = list(meta.keys())

            missing = [k for k in REQUIRED_META_KEYS if k not in meta]
            if missing:
                result["issues"].append(
                    f"Missing metadata keys: {', '.join(missing)}")
            else:
                result["meta_valid"] = True

        except Exception as e:
            result["issues"].append(f"JSON parse error: {e}")
    else:
        result["issues"].append("metadata.json missing")

    # Overall status
    if result["ts_valid"] and result["meta_valid"] and not result["issues"]:
        result["status"] = "VALID"
    elif result["has_ts"] and result["has_meta"]:
        result["status"] = "PARTIAL"
    else:
        result["status"] = "INVALID"

    return result


def main():
    os.makedirs(ATLAS_DIR, exist_ok=True)

    print("  ED-SIM v1 Data Integrity Check")
    print("  " + "=" * 50)
    print()

    if not os.path.isdir(RUNS_DIR):
        print(f"  WARNING: Runs directory not found: {RUNS_DIR}")
        print("  No data to check.")
        report = {
            "timestamp": datetime.datetime.now().isoformat(),
            "runs_dir": RUNS_DIR,
            "n_runs": 0,
            "verdict": "NO_DATA",
        }
        out_path = os.path.join(ATLAS_DIR, "data_integrity_check.json")
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2)
        sys.exit(0)

    # Discover all run directories
    all_dirs = set()
    for pattern in RUN_PATTERNS:
        matches = glob.glob(os.path.join(RUNS_DIR, pattern))
        for m in matches:
            if os.path.isdir(m):
                all_dirs.add(m)

    all_dirs = sorted(all_dirs)
    print(f"  Found {len(all_dirs)} run directories.")
    print()

    # Check each
    results = []
    n_valid = 0
    n_partial = 0
    n_invalid = 0

    for d in all_dirs:
        r = check_run(d)
        results.append(r)

        if r["status"] == "VALID":
            n_valid += 1
        elif r["status"] == "PARTIAL":
            n_partial += 1
        else:
            n_invalid += 1

    # Print summary table
    print(f"  {'Run':<40} {'Status':<10} {'Steps':>7} {'Issues'}")
    print("  " + "-" * 75)

    for r in results:
        issues_str = "; ".join(r["issues"][:2]) if r["issues"] else "—"
        if len(issues_str) > 30:
            issues_str = issues_str[:28] + "..."
        print(f"  {r['name']:<40} {r['status']:<10} "
              f"{r['n_timesteps']:>7} {issues_str}")

    # Totals
    print()
    print(f"  Valid:   {n_valid}")
    print(f"  Partial: {n_partial}")
    print(f"  Invalid: {n_invalid}")

    # Regime volume coverage
    regime_runs = [r for r in results
                   if r["name"].startswith("regime_D")
                   and r["status"] == "VALID"]
    print(f"\n  Regime volume (valid): {len(regime_runs)} / 64 expected")

    # Verdict
    if n_valid >= 64:
        verdict = "COMPLETE"
    elif n_valid >= 32:
        verdict = "SUFFICIENT"
    elif n_valid > 0:
        verdict = "PARTIAL"
    else:
        verdict = "NO_DATA"

    print(f"\n  Verdict: {verdict}")

    # Save
    report = {
        "timestamp": datetime.datetime.now().isoformat(),
        "runs_dir": RUNS_DIR,
        "n_runs": len(all_dirs),
        "n_valid": n_valid,
        "n_partial": n_partial,
        "n_invalid": n_invalid,
        "n_regime_valid": len(regime_runs),
        "verdict": verdict,
        "runs": results,
    }

    out_path = os.path.join(ATLAS_DIR, "data_integrity_check.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, default=str)
    print(f"  Report: {out_path}")

    sys.exit(0)


if __name__ == "__main__":
    main()
