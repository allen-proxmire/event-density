"""
Diagnostic Scenario
====================
Runs only consistency checks -- no new simulations, no new invariants.

Checks:
  - Environment
  - Data integrity
  - Output validation

Useful for debugging when runs already exist.

Expected runtime: < 30 seconds.

Usage:
    python reproducibility/scenarios/diagnostic/run.py
"""

import os
import sys
import subprocess

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SIM_DIR = os.path.dirname(os.path.dirname(os.path.dirname(SCRIPT_DIR)))

CHECKS = [
    ("Environment Check",
     os.path.join(SIM_DIR, "reproducibility", "checks",
                  "check_environment.py")),
    ("Data Integrity",
     os.path.join(SIM_DIR, "reproducibility", "checks",
                  "check_data_integrity.py")),
    ("Output Validation",
     os.path.join(SIM_DIR, "reproducibility", "validation",
                  "validate_outputs.py")),
]


def run_script(label: str, path: str) -> bool:
    print(f"\n  [{label}]")
    if not os.path.isfile(path):
        print(f"    SKIP: {path} not found.")
        return False
    result = subprocess.run(
        [sys.executable, path], cwd=SIM_DIR,
        capture_output=True, text=True, timeout=120,
    )
    if result.returncode == 0:
        print(f"    PASS")
        return True
    else:
        lines = result.stderr.strip().split("\n")
        print(f"    FAIL: {lines[-1] if lines else '(no output)'}")
        # Print stdout too for diagnostics
        if result.stdout.strip():
            for line in result.stdout.strip().split("\n")[-10:]:
                print(f"      {line}")
        return False


def main():
    print("  ED-SIM v1 -- Diagnostic Scenario")
    print("  " + "=" * 50)

    n_pass = 0
    for label, path in CHECKS:
        if run_script(label, path):
            n_pass += 1

    print(f"\n  Result: {n_pass}/{len(CHECKS)} passed.")
    if n_pass == len(CHECKS):
        print("  Diagnostic: ALL CLEAR")
    else:
        print("  Diagnostic: ISSUES FOUND -- see details above.")


if __name__ == "__main__":
    main()
