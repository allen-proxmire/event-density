"""
Generate the Barenblatt front-propagation validation figure for the
mobility-law paper.

Runs the Barenblatt experiment at beta = 1.69 (hard-sphere colloid case)
using the existing edsim analogue code, then plots:
  (A) Front radius R(t) vs t on log-log axes
  (B) Peak density delta_max(t) vs t on log-log axes

Output: outputs/figures/barenblatt_validation.png
"""

import os
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Ensure repo root is on the path
script_dir = os.path.dirname(os.path.abspath(__file__))
repo_root = os.path.join(script_dir, "..")
sys.path.insert(0, repo_root)

from edsim.phys.analogues.barenblatt import (
    run_barenblatt_experiment,
    predict_barenblatt,
)


def main():
    beta = 1.69  # hard-sphere colloid exponent
    print(f"Running Barenblatt experiment for beta = {beta} ...")
    print("  (This may take a few minutes at N=64, T=500)")

    # Run the experiment with enough time for asymptotic convergence
    res = run_barenblatt_experiment(
        beta=beta,
        N=64,
        L=8.0,
        A_ic=0.4,
        R0_ic=0.5,
        T=500.0,
        n_snaps=40,
        dt=0.005,
    )

    pred = res.prediction
    times = res.times
    front_radii = res.front_radii
    central_delta = res.central_delta

    print(f"  Done. {len(times)} snapshots.")
    print(f"  Predicted  alpha_R   = {pred.alpha_R:.6f}")
    print(f"  Simulated  alpha_R   = {res.alpha_R_fitted:.6f}")
    print(f"  Error      alpha_R   = {res.alpha_R_error_pct:.2f}%")
    print(f"  Predicted  alpha_rho = {pred.alpha_rho:.6f}")
    print(f"  Simulated  alpha_rho = {res.alpha_rho_fitted:.6f}")
    print(f"  Error      alpha_rho = {res.alpha_rho_error_pct:.2f}%")
    print(f"  Compact support      = {res.compact_support}")

    # ── Fit window: use t > 20% of T for asymptotic regime ──────────
    t_fit_min = 0.2 * times[-1]
    mask = times > t_fit_min

    # ── Reference power-law lines (anchored at geometric mean of fit window)
    t_fit = times[mask]
    t_anchor = np.sqrt(t_fit[0] * t_fit[-1])

    # R(t) reference
    R_fit = front_radii[mask]
    R_anchor = np.exp(np.interp(np.log(t_anchor), np.log(t_fit), np.log(R_fit)))
    R_pred_line = R_anchor * (t_fit / t_anchor) ** pred.alpha_R

    # delta_max(t) reference
    cd_fit = central_delta[mask]
    cd_anchor = np.exp(np.interp(np.log(t_anchor), np.log(t_fit),
                                  np.log(np.maximum(cd_fit, 1e-30))))
    cd_pred_line = cd_anchor * (t_fit / t_anchor) ** pred.alpha_rho

    # ── Figure ──────────────────────────────────────────────────────
    fig, (ax_a, ax_b) = plt.subplots(1, 2, figsize=(12, 5))

    # ── Panel A: Front radius R(t) ─────────────────────────────────
    valid_r = (times > 0) & (front_radii > 0)
    ax_a.loglog(times[valid_r], front_radii[valid_r], "o",
                color="#2563EB", markersize=5, markeredgecolor="white",
                markeredgewidth=0.4, label="ED simulation", zorder=3)
    ax_a.loglog(t_fit, R_pred_line, "--", color="#DC2626", linewidth=2.0,
                label=f"Predicted slope: $\\alpha_R$ = {pred.alpha_R:.4f}",
                zorder=2)

    ax_a.set_xlabel("Time  $t$", fontsize=12)
    ax_a.set_ylabel("Front radius  $R(t)$", fontsize=12)
    ax_a.set_title("(A)  Front-radius scaling", fontsize=13, fontweight="bold")

    ax_a.text(0.04, 0.96,
              f"$\\beta$ = {beta}\n"
              f"Predicted $\\alpha_R$ = {pred.alpha_R:.4f}\n"
              f"Simulated $\\alpha_R$ = {res.alpha_R_fitted:.4f}\n"
              f"Error: {res.alpha_R_error_pct:.1f}%",
              transform=ax_a.transAxes, fontsize=9.5,
              verticalalignment="top", fontfamily="monospace",
              bbox=dict(boxstyle="round,pad=0.4", facecolor="white",
                        edgecolor="#D1D5DB", alpha=0.95))

    ax_a.legend(fontsize=9, loc="lower right", framealpha=0.9)
    ax_a.spines["top"].set_visible(False)
    ax_a.spines["right"].set_visible(False)

    # ── Panel B: Peak density delta_max(t) ─────────────────────────
    valid_d = (times > 0) & (central_delta > 1e-15)
    ax_b.loglog(times[valid_d], central_delta[valid_d], "o",
                color="#2563EB", markersize=5, markeredgecolor="white",
                markeredgewidth=0.4, label="ED simulation", zorder=3)
    ax_b.loglog(t_fit, cd_pred_line, "--", color="#DC2626", linewidth=2.0,
                label=f"Predicted slope: $\\alpha_\\rho$ = {pred.alpha_rho:.4f}",
                zorder=2)

    ax_b.set_xlabel("Time  $t$", fontsize=12)
    ax_b.set_ylabel("Peak density  $\\delta_{\\mathrm{max}}(t)$", fontsize=12)
    ax_b.set_title("(B)  Peak-density decay", fontsize=13, fontweight="bold")

    ax_b.text(0.04, 0.04,
              f"$\\beta$ = {beta}\n"
              f"Predicted $\\alpha_\\rho$ = {pred.alpha_rho:.4f}\n"
              f"Simulated $\\alpha_\\rho$ = {res.alpha_rho_fitted:.4f}\n"
              f"Error: {res.alpha_rho_error_pct:.1f}%",
              transform=ax_b.transAxes, fontsize=9.5,
              verticalalignment="bottom", fontfamily="monospace",
              bbox=dict(boxstyle="round,pad=0.4", facecolor="white",
                        edgecolor="#D1D5DB", alpha=0.95))

    ax_b.legend(fontsize=9, loc="upper right", framealpha=0.9)
    ax_b.spines["top"].set_visible(False)
    ax_b.spines["right"].set_visible(False)

    # ── Suptitle ───────────────────────────────────────────────────
    fig.suptitle(
        f"Barenblatt front-propagation validation  "
        f"($\\beta = {beta}$,  $m = {pred.m:.2f}$,  $d = 2$)",
        fontsize=14, fontweight="bold", y=1.01,
    )

    plt.tight_layout()

    # ── Save ───────────────────────────────────────────────────────
    outdir = os.path.join(repo_root, "outputs", "figures")
    os.makedirs(outdir, exist_ok=True)
    outpath = os.path.join(outdir, "barenblatt_validation.png")
    fig.savefig(outpath, dpi=150, bbox_inches="tight", facecolor="white")
    plt.close()

    print(f"\nSaved: {outpath}")
    print(f"Size:  {os.path.getsize(outpath) / 1024:.0f} KB")


if __name__ == "__main__":
    main()
