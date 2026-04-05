"""
Minimal Reproducibility Scenario
=================================
Runs the smallest possible ED-SIM pipeline:
  1 regime volume run (D=0.1, A=0.01, Nm=5)
  1 invariant (low-mode collapse)
  1 figure

Expected runtime: < 2 minutes.

Usage:
    python reproducibility/scenarios/minimal/run.py
"""

import os
import sys
import subprocess

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SIM_DIR = os.path.dirname(os.path.dirname(os.path.dirname(SCRIPT_DIR)))

sys.path.insert(0, SIM_DIR)


def run_script(label: str, path: str) -> bool:
    print(f"\n  [{label}]")
    if not os.path.isfile(path):
        print(f"    SKIP: {path} not found.")
        return False
    result = subprocess.run(
        [sys.executable, path], cwd=SIM_DIR,
        capture_output=True, text=True, timeout=600,
    )
    if result.returncode == 0:
        print(f"    PASS")
        return True
    else:
        print(f"    FAIL: {result.stderr.strip().split(chr(10))[-1]}")
        return False


def main():
    print("  ED-SIM v1 -- Minimal Reproducibility Scenario")
    print("  " + "=" * 50)

    exp = os.path.join(SIM_DIR, "experiments")

    steps = [
        ("Environment Check",
         os.path.join(SIM_DIR, "reproducibility", "checks",
                      "check_environment.py")),
        ("Regime Volume (single point)",
         os.path.join(exp, "regime_volume_3d.py")),
        ("Low-Mode Collapse Invariant",
         os.path.join(exp, "invariant_low_mode_collapse.py")),
        ("Validate Outputs",
         os.path.join(SIM_DIR, "reproducibility", "validation",
                      "validate_outputs.py")),
    ]

    n_pass = 0
    for label, path in steps:
        if run_script(label, path):
            n_pass += 1

    print(f"\n  Result: {n_pass}/{len(steps)} passed.")
    if n_pass == len(steps):
        print("  Minimal scenario: PASS")
    else:
        print("  Minimal scenario: PARTIAL")


if __name__ == "__main__":
    main()
