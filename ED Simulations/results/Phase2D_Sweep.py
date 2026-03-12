"""
Phase2D_Sweep.py
================
4 x 4 parameter sweep over mobility_exp and noise_amp for Scenario D.

Grid:
    mobility_exp  in [0.5, 1.0, 2.0, 4.0]
    noise_amp     in [0.01, 0.02, 0.05, 0.10]

For each of the 16 combinations the script:
  1. Runs Run_Simulation.py --scenario D with the given parameters.
  2. Parses console output for key observables.
  3. Copies output/*.png  to  results/phase2D/n_{exp}/noise_{amp}/.
  4. Writes a metrics.txt summary alongside the PNGs.

Usage
-----
    python Phase2D_Sweep.py
    python Phase2D_Sweep.py --outdir my_output --results my_results
"""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path


# ---------------------------------------------------------------------------
# Parameter grid
# ---------------------------------------------------------------------------

EXPONENTS    = [0.5, 1.0, 2.0, 4.0]
NOISE_LEVELS = [0.01, 0.02, 0.05, 0.10]


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _label(value: float) -> str:
    """Return a filesystem-safe label for a float (e.g. 0.5 -> '0.5')."""
    return str(value)


def _parse_metrics(output: str) -> dict:
    """Extract observables from Run_Simulation.py console output."""
    metrics: dict = {
        "phase_exit_step": None,
        "final_p_hat":     None,
        "final_G":         None,
        "final_L":         None,
        "structures":      None,
    }

    # First verbose line showing phase=3-structure_formation
    for line in output.splitlines():
        if metrics["phase_exit_step"] is None:
            m = re.search(
                r"step=\s*(\d+).*phase=3-structure_formation", line
            )
            if m:
                metrics["phase_exit_step"] = int(m.group(1))

    # Last step=500 verbose line  -> final_p_hat, final_G, final_L
    for line in output.splitlines():
        m = re.search(
            r"step=\s*500\s+t=.*?"
            r"p_hat=([\d.]+).*?"
            r"G=([\d.]+).*?"
            r"L=([\d.]+)",
            line,
        )
        if m:
            metrics["final_p_hat"] = float(m.group(1))
            metrics["final_G"]     = float(m.group(2))
            metrics["final_L"]     = float(m.group(3))

    # Structures detected
    for line in output.splitlines():
        m = re.search(r"Structures detected:\s*(\d+)", line)
        if m:
            metrics["structures"] = int(m.group(1))

    return metrics


def _metrics_txt(n: float, noise: float, m: dict) -> str:
    return (
        f"mobility_exp: {n}\n"
        f"noise_amp: {noise}\n"
        f"phase_exit_step: {m['phase_exit_step']}\n"
        f"final_p_hat: {m['final_p_hat']}\n"
        f"final_G: {m['final_G']}\n"
        f"final_L: {m['final_L']}\n"
        f"structures: {m['structures']}\n"
    )


# ---------------------------------------------------------------------------
# Sweep
# ---------------------------------------------------------------------------

def run_sweep(
    outdir:      str = "output",
    results_dir: str = "results/phase2D",
) -> None:
    script    = Path(__file__).parent / "Run_Simulation.py"
    out_path  = Path(__file__).parent / outdir
    res_base  = Path(__file__).parent / results_dir

    total = len(EXPONENTS) * len(NOISE_LEVELS)
    done  = 0

    print(f"\n{'='*60}")
    print(f"  Phase-2D Sweep: {len(EXPONENTS)} exponents x "
          f"{len(NOISE_LEVELS)} noise levels = {total} runs")
    print(f"  Results -> {res_base}")
    print(f"{'='*60}\n")

    summary_rows: list[dict] = []

    for n in EXPONENTS:
        for noise in NOISE_LEVELS:
            done += 1
            tag = f"n={n}  noise={noise}"
            print(f"[{done:2d}/{total}]  Running {tag} ...", flush=True)

            # ---- run ----
            proc = subprocess.run(
                [
                    sys.executable, str(script),
                    "--scenario", "D",
                    "--mobility-exp", str(n),
                    "--noise-amp",    str(noise),
                    "--no-show",
                ],
                capture_output=True,
                text=True,
            )

            if proc.returncode != 0:
                print(f"  ERROR (returncode={proc.returncode}):")
                print(proc.stderr[-800:])
                continue

            # ---- parse ----
            metrics = _parse_metrics(proc.stdout)

            # ---- copy PNGs ----
            dest = res_base / f"n_{_label(n)}" / f"noise_{_label(noise)}"
            dest.mkdir(parents=True, exist_ok=True)

            for png in sorted(out_path.glob("*.png")):
                shutil.copy(png, dest / png.name)

            # ---- write metrics.txt ----
            (dest / "metrics.txt").write_text(
                _metrics_txt(n, noise, metrics), encoding="utf-8"
            )

            # ---- report ----
            print(
                f"         phase_exit={metrics['phase_exit_step']}  "
                f"G={metrics['final_G']}  "
                f"L={metrics['final_L']}  "
                f"structs={metrics['structures']}"
            )
            print(f"         -> {dest}")

            summary_rows.append({"n": n, "noise": noise, **metrics})

    # ---- summary table ----
    print(f"\n{'='*78}")
    print(f"  {'n':>5}  {'noise':>6}  {'exit':>5}  {'G_f':>8}  "
          f"{'L_f':>7}  {'structs':>8}  p_hat_f")
    print(f"  {'-'*5}  {'-'*6}  {'-'*5}  {'-'*8}  {'-'*7}  {'-'*8}  {'-'*7}")
    for r in summary_rows:
        exit_s = str(r["phase_exit_step"]) if r["phase_exit_step"] else "---"
        print(
            f"  {r['n']:>5}  {r['noise']:>6}  {exit_s:>5}  "
            f"{r['final_G'] or 0:>8.5f}  "
            f"{r['final_L'] or 0:>7.1f}  "
            f"{r['structures'] or 0:>8d}  "
            f"{r['final_p_hat'] or 0:.4f}"
        )
    print(f"{'='*78}\n")

    # ---- write combined summary CSV ----
    csv_path = res_base / "summary.csv"
    with csv_path.open("w", encoding="utf-8") as f:
        f.write("mobility_exp,noise_amp,phase_exit_step,final_p_hat,"
                "final_G,final_L,structures\n")
        for r in summary_rows:
            f.write(
                f"{r['n']},{r['noise']},"
                f"{r['phase_exit_step']},"
                f"{r['final_p_hat']},"
                f"{r['final_G']},"
                f"{r['final_L']},"
                f"{r['structures']}\n"
            )
    print(f"Summary CSV -> {csv_path}\n")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def _parse_args(argv=None) -> argparse.Namespace:
    p = argparse.ArgumentParser(
        prog="Phase2D_Sweep.py",
        description="4x4 mobility_exp x noise_amp sweep for Scenario D.",
    )
    p.add_argument(
        "--outdir", default="output",
        help="Subdirectory (relative to script) where Run_Simulation writes PNGs.  "
             "Default: output",
    )
    p.add_argument(
        "--results", default="results/phase2D", dest="results_dir",
        help="Root for per-run result directories.  Default: results/phase2D",
    )
    return p.parse_args(argv)


if __name__ == "__main__":
    args = _parse_args()
    run_sweep(outdir=args.outdir, results_dir=args.results_dir)
