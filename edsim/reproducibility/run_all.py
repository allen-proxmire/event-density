"""
edsim.reproducibility.run_all — CLI entry point for the reproducibility pipeline.

Usage:
    python -m edsim.reproducibility.run_all
"""

from __future__ import annotations

import sys
import time

from .pipeline import run_pipeline


def main() -> int:
    """Run the full reproducibility pipeline and print a summary.

    Returns
    -------
    int
        Exit code: 0 if all phases passed, 1 if any failed.
    """
    print("=" * 65)
    print("  ED-SIM-02 Reproducibility Pipeline")
    print("=" * 65)
    print()

    t_start = time.time()
    cert = run_pipeline()
    t_elapsed = time.time() - t_start

    # Header
    summary = cert.summary()
    print(f"Version:    {summary['version']}")
    print(f"Timestamp:  {summary['timestamp']}")
    print(f"Elapsed:    {t_elapsed:.1f}s")
    print(f"Phases:     {summary['n_phases']} total, "
          f"{summary['n_passed']} passed, {summary['n_failed']} failed")
    print()

    # Phase details
    print("-" * 65)
    for i, phase in enumerate(cert.phases, 1):
        status = "[OK]  " if phase.passed else "[FAIL]"
        print(f"  {i}. {status} {phase.name}")
        print(f"     {phase.description}")

        # Print 2-3 key details
        d = phase.details
        detail_items = []
        for key, val in d.items():
            if isinstance(val, bool):
                continue  # skip redundant booleans
            if isinstance(val, float):
                detail_items.append(f"{key}={val:.4g}")
            elif isinstance(val, (int, str)):
                detail_items.append(f"{key}={val}")
            elif isinstance(val, dict):
                # Morphology fractions — show compact
                compact = ", ".join(f"{k}={v:.2f}" for k, v in val.items() if isinstance(v, (int, float)))
                if compact:
                    detail_items.append(compact)
            elif isinstance(val, list) and len(val) <= 5:
                detail_items.append(f"{key}={val}")
        if detail_items:
            # Show first 4 details
            line = "     " + "  |  ".join(detail_items[:4])
            print(line)
        print()

    # Summary line
    print("-" * 65)
    if cert.all_passed:
        print("  RESULT: ALL PHASES PASSED")
    else:
        print(f"  RESULT: {summary['n_failed']} PHASE(S) FAILED")
        print(f"  Failed: {', '.join(summary['failed_names'])}")
    print("=" * 65)

    return 0 if cert.all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
