"""
Full Reproducibility Scenario
==============================
Runs the complete ED-SIM v1 pipeline. Equivalent to:
    python reproducibility/run_all.py

Expected runtime: 30-120 minutes depending on hardware.

Usage:
    python reproducibility/scenarios/full/run.py
"""

import os
import sys
import subprocess

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SIM_DIR = os.path.dirname(os.path.dirname(os.path.dirname(SCRIPT_DIR)))


def main():
    print("  ED-SIM v1 -- Full Reproducibility Scenario")
    print("  Delegating to run_all.py...")
    print()

    run_all = os.path.join(SIM_DIR, "reproducibility", "run_all.py")
    result = subprocess.run(
        [sys.executable, run_all],
        cwd=SIM_DIR,
    )
    sys.exit(result.returncode)


if __name__ == "__main__":
    main()
