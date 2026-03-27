"""
invariant_dissipation_geometry.py
==================================
Experiment / Analysis: Invariant Dissipation Geometry

Scans all completed regime_D*_A*_Nm* runs and analyses the joint
energy-dissipation trajectory

    (X(t), Y(t)) = (E(t), D_total(t))

in the energy-dissipation plane.  The attractor point (X*, Y*) encodes
the equilibrium energy and the equilibrium dissipation rate -- two
structural invariants of the ED architecture whose existence is guaranteed
by the Lyapunov theory (Appendix C.5) and whose uniqueness follows from
Principle 3 (strict penalty monotonicity).

Produces:
  (A) Energy-Dissipation Trajectory -- parametric curve for a representative run.
  (B) Attractor Geometry Scatter -- (X*, Y*) for all runs with covariance ellipse.
  (C) Convergence Heatmap -- converged/not across (D, A, Nm).

All figures saved to output/figures/invariants/dissipation_geometry/
as PNG (300 dpi).

Usage:
    python experiments/invariant_dissipation_geometry.py

Requires: numpy, matplotlib.
"""

import os
import sys
import glob
import json
import re
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.patches import Ellipse

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SIM_DIR = os.path.dirname(SCRIPT_DIR)  # ED Simulation/
RUNS_DIR = os.path.join(SIM_DIR, "output", "runs")
FIG_DIR = os.path.join(SIM_DIR, "output", "figures", "invariants",
                        "dissipation_geometry")

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
LATE_FRAC = 0.10        # Fraction for late-time average
FIT_FRAC = 0.20         # Fraction for convergence fit
R2_THRESH = 0.95        # R² threshold for convergence
D_TOTAL_FLOOR = 1e-30   # Floor for D_total reconstruction


# ---------------------------------------------------------------------------
# Discovery (shared pattern)
# ---------------------------------------------------------------------------
def discover_regime_runs() -> list[dict]:
    """Scan RUNS_DIR for regime_D*_A*_Nm* folders with energy and dissipation."""
    pattern = os.path.join(RUNS_DIR, "regime_D*_A*_Nm*")
    dirs = sorted(glob.glob(pattern))

    runs = []
    for d in dirs:
        ts_path = os.path.join(d, "time_series.npz")
        meta_path = os.path.join(d, "metadata.json")
        if not os.path.isfile(ts_path):
            continue

        meta = {}
        if os.path.isfile(meta_path):
            with open(meta_path, "r") as f:
                meta = json.load(f)

        if meta.get("inadmissible", False):
            continue

        D_val = meta.get("D")
        A_val = meta.get("A") or meta.get("A_per_mode")
        Nm_val = (meta.get("Nm") or meta.get("n_seeded")
                  or meta.get("N_modes_seeded"))

        name = os.path.basename(d)
        D_val, A_val, Nm_val = _fill_from_dirname(name, D_val, A_val, Nm_val)

        if D_val is None or A_val is None or Nm_val is None:
            continue

        ts = np.load(ts_path, allow_pickle=True)
        t = ts.get("t")
        E = ts.get("E_total")
        if t is None or E is None:
            continue

        # Load dissipation channels
        D_grad = ts.get("D_gradient")
        D_pen = ts.get("D_penalty")
        D_part = ts.get("D_participation")
        D_total = ts.get("D_total")

        if D_grad is None or D_pen is None or D_part is None:
            continue
        if D_total is None:
            D_total = D_grad + D_pen + D_part

        # Trim to consistent length
        n = min(len(t), len(E), len(D_grad), len(D_pen),
                len(D_part), len(D_total))
        if n < 50:
            continue

        runs.append({
            "dir": d,
            "name": name,
            "D": float(D_val),
            "A": float(A_val),
            "Nm": int(Nm_val),
            "metadata": meta,
            "t": t[:n],
            "E": E[:n],
            "D_total": D_total[:n],
        })

    runs.sort(key=lambda r: (r["D"], r["A"], r["Nm"]))
    return runs


def _fill_from_dirname(name: str, D, A, Nm):
    m_D = re.search(r"D([\d.eE+-]+)", name)
    m_A = re.search(r"A([\d.eE+-]+)", name)
    m_Nm = re.search(r"Nm(\d+)", name)
    if D is None and m_D:
        try:
            D = float(m_D.group(1))
        except ValueError:
            pass
    if A is None and m_A:
        try:
            A = float(m_A.group(1))
        except ValueError:
            pass
    if Nm is None and m_Nm:
        try:
            Nm = int(m_Nm.group(1))
        except ValueError:
            pass
    return D, A, Nm


# ---------------------------------------------------------------------------
# Per-run analysis (streaming -- no extra arrays retained)
# ---------------------------------------------------------------------------
def analyse_run(run: dict) -> dict:
    """Compute attractor coordinates and convergence for one run."""
    t = run["t"]
    X = run["E"]           # energy trajectory
    Y = run["D_total"]     # dissipation trajectory

    # Late-time averages
    start = max(0, int((1.0 - LATE_FRAC) * len(t)))
    X_star = float(np.mean(X[start:]))
    Y_star = float(np.mean(Y[start:]))

    # Convergence fits
    fit_X = _fit_exponential(t, X, X_star)
    fit_Y = _fit_exponential(t, Y, Y_star)

    both_converged = fit_X["converged"] and fit_Y["converged"]

    return {
        "X_star": X_star,
        "Y_star": Y_star,
        "sigma_X": fit_X["sigma"],
        "sigma_Y": fit_Y["sigma"],
        "R2_X": fit_X["R2"],
        "R2_Y": fit_Y["R2"],
        "conv_X": fit_X["converged"],
        "conv_Y": fit_Y["converged"],
        "converged": both_converged,
    }


def _fit_exponential(t: np.ndarray, arr: np.ndarray,
                     target: float) -> dict:
    """Fit |arr(t) - target| ~ C exp(-sigma t) over the last FIT_FRAC."""
    result = {"sigma": 0.0, "R2": 0.0, "converged": False}

    n = len(t)
    start = max(0, int((1.0 - FIT_FRAC) * n))
    t_fit = t[start:]
    residual = np.abs(arr[start:] - target)

    valid = residual > 1e-30
    if np.sum(valid) < 10:
        return result

    log_r = np.log(residual[valid])
    t_v = t_fit[valid]

    try:
        coeffs = np.polyfit(t_v, log_r, 1)
        sigma = -coeffs[0]

        predicted = coeffs[0] * t_v + coeffs[1]
        ss_res = np.sum((log_r - predicted) ** 2)
        ss_tot = np.sum((log_r - np.mean(log_r)) ** 2)
        R2 = 1.0 - ss_res / max(ss_tot, 1e-30)

        result["sigma"] = float(sigma)
        result["R2"] = float(R2)
        result["converged"] = R2 > R2_THRESH and sigma > 0
    except (np.linalg.LinAlgError, ValueError):
        pass

    return result


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def setup_axes(ax, xlabel: str, ylabel: str, title: str):
    ax.set_xlabel(xlabel, fontsize=11)
    ax.set_ylabel(ylabel, fontsize=11)
    ax.set_title(title, fontsize=13, fontweight="bold")
    ax.tick_params(labelsize=10)
    ax.grid(True, alpha=0.3, linewidth=0.5)


def covariance_ellipse(points: np.ndarray, n_std: float = 2.0) -> Ellipse:
    """Compute a matplotlib Ellipse patch from a 2-D point cloud.

    Parameters
    ----------
    points : ndarray, shape (N, 2)
    n_std : number of standard deviations for the ellipse radius

    Returns
    -------
    Ellipse patch (not yet added to an axes).
    """
    mean = np.mean(points, axis=0)
    cov = np.cov(points, rowvar=False)

    # Eigenvalues and eigenvectors
    eigvals, eigvecs = np.linalg.eigh(cov)
    order = eigvals.argsort()[::-1]
    eigvals = eigvals[order]
    eigvecs = eigvecs[:, order]

    # Angle of the major axis
    angle = np.degrees(np.arctan2(eigvecs[1, 0], eigvecs[0, 0]))

    # Width and height (2 * n_std * sqrt(eigenvalue))
    width = 2 * n_std * np.sqrt(max(eigvals[0], 0))
    height = 2 * n_std * np.sqrt(max(eigvals[1], 0))

    return Ellipse(
        xy=mean, width=width, height=height, angle=angle,
        facecolor="none", edgecolor="0.3", linewidth=1.5,
        linestyle="--", alpha=0.7,
    )


# ---------------------------------------------------------------------------
# Figure A: Energy-Dissipation Trajectory (representative run)
# ---------------------------------------------------------------------------
def figure_trajectory(runs: list[dict], analyses: list[dict]):
    """Parametric curve (E(t), D_total(t)) for the run with largest Nm."""
    best_idx = max(range(len(runs)), key=lambda i: runs[i]["Nm"])
    run = runs[best_idx]
    ana = analyses[best_idx]

    X = run["E"]
    Y = run["D_total"]
    t = run["t"]
    n = len(t)

    fig, ax = plt.subplots(figsize=(9, 7))

    # Color by time
    time_frac = np.linspace(0, 1, n)

    # Plot as colored line segments
    from matplotlib.collections import LineCollection
    points = np.array([X, Y]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)

    norm = plt.Normalize(0, 1)
    lc = LineCollection(segments, cmap="coolwarm", norm=norm,
                        linewidths=1.4, alpha=0.8)
    lc.set_array(time_frac[:-1])
    ax.add_collection(lc)

    # Start marker
    ax.plot(X[0], Y[0], "o", color="#2166ac", markersize=10, zorder=10,
            label="Start")

    # End marker
    ax.plot(X[-1], Y[-1], "s", color="#b2182b", markersize=9, zorder=10,
            label="End")

    # Attractor point
    ax.plot(ana["X_star"], ana["Y_star"], "*", color="#1b7837",
            markersize=16, zorder=10, markeredgecolor="black",
            markeredgewidth=0.5,
            label=rf"$(X^*, Y^*) = ({ana['X_star']:.4e}, {ana['Y_star']:.4e})$")

    # Time arrows (every 10% of the trajectory)
    arrow_indices = np.linspace(0, n - 2, 8, dtype=int)
    for idx in arrow_indices:
        dx = X[idx + 1] - X[idx]
        dy = Y[idx + 1] - Y[idx]
        length = np.sqrt(dx ** 2 + dy ** 2)
        if length > 1e-30:
            ax.annotate(
                "", xy=(X[idx + 1], Y[idx + 1]),
                xytext=(X[idx], Y[idx]),
                arrowprops=dict(arrowstyle="->", color="0.4",
                                lw=1.0, alpha=0.5),
            )

    # Colorbar
    cbar = fig.colorbar(lc, ax=ax, label="Time (early → late)", pad=0.02)
    cbar.ax.tick_params(labelsize=9)

    # Auto-scale with padding
    pad_x = 0.05 * max(abs(X.max() - X.min()), 1e-10)
    pad_y = 0.05 * max(abs(Y.max() - Y.min()), 1e-10)
    ax.set_xlim(X.min() - pad_x, X.max() + pad_x)
    ax.set_ylim(Y.min() - pad_y, Y.max() + pad_y)

    setup_axes(
        ax,
        xlabel=r"Energy $\mathcal{E}(t)$",
        ylabel=r"Total dissipation $\mathcal{D}(t)$",
        title=(f"Energy-Dissipation Trajectory -- D={run['D']}, "
               f"A={run['A']}, Nm={run['Nm']}"),
    )
    ax.legend(fontsize=9, loc="upper right", framealpha=0.9)
    fig.tight_layout()

    fname = "trajectory.png"
    fig.savefig(os.path.join(FIG_DIR, fname), dpi=300)
    plt.close(fig)
    print(f"  Saved: {fname}")


# ---------------------------------------------------------------------------
# Figure B: Attractor Geometry Scatter (all runs)
# ---------------------------------------------------------------------------
def figure_attractor_scatter(runs: list[dict], analyses: list[dict]):
    """Scatter (X*, Y*) for all runs with covariance ellipse."""
    D_vals = sorted(set(r["D"] for r in runs))
    Nm_vals = sorted(set(r["Nm"] for r in runs))

    D_cmap = plt.cm.plasma
    D_norm = mcolors.Normalize(
        vmin=min(D_vals) * 0.9 if D_vals else 0,
        vmax=max(D_vals) * 1.1 if D_vals else 1,
    )
    Nm_markers = {Nm_vals[i]: m for i, m in
                  zip(range(len(Nm_vals)),
                      ["o", "s", "^", "D", "v", "P", "*"])}

    fig, ax = plt.subplots(figsize=(10, 8))

    # Collect points for covariance ellipse
    all_points = []

    for run, ana in zip(runs, analyses):
        X_s = ana["X_star"]
        Y_s = ana["Y_star"]
        if np.isnan(X_s) or np.isnan(Y_s):
            continue

        color = D_cmap(D_norm(run["D"]))
        marker = Nm_markers.get(run["Nm"], "o")

        ax.scatter(
            X_s, Y_s,
            color=color, marker=marker, s=60, alpha=0.7,
            edgecolors="0.3", linewidths=0.4, zorder=5,
        )

        all_points.append([X_s, Y_s])

    all_points = np.array(all_points)

    # Global mean
    if len(all_points) > 1:
        mean_pt = np.mean(all_points, axis=0)
        ax.plot(
            mean_pt[0], mean_pt[1], "+", color="black",
            markersize=16, markeredgewidth=2.5, zorder=10,
            label=rf"Mean $= ({mean_pt[0]:.4e},\;{mean_pt[1]:.4e})$",
        )

        # Covariance ellipse (2-sigma)
        if len(all_points) >= 3:
            try:
                ellipse = covariance_ellipse(all_points, n_std=2.0)
                ellipse.set_label(r"$2\sigma$ ellipse")
                ax.add_patch(ellipse)
            except np.linalg.LinAlgError:
                pass  # degenerate covariance

    # Colorbar for D
    sm = plt.cm.ScalarMappable(cmap=D_cmap, norm=D_norm)
    sm.set_array([])
    cbar = fig.colorbar(sm, ax=ax, label=r"Diffusion $D$", pad=0.02)
    cbar.ax.tick_params(labelsize=9)

    # Marker legend for Nm
    legend_handles = [
        plt.Line2D([0], [0], marker=m, color="0.5", markersize=7,
                   linestyle="None", label=rf"$N_m = {Nm}$")
        for Nm, m in Nm_markers.items()
    ]
    # Add mean and ellipse to legend
    for h in ax.get_legend_handles_labels()[0]:
        legend_handles.append(h)
    ax.legend(
        handles=legend_handles, fontsize=8, loc="upper right",
        framealpha=0.9, title="Legend",
    )

    setup_axes(
        ax,
        xlabel=r"Attractor energy $X^* = \mathcal{E}^*$",
        ylabel=r"Attractor dissipation $Y^* = \mathcal{D}^*$",
        title="Dissipation Geometry -- Attractor Scatter",
    )
    fig.tight_layout()

    fname = "attractor_scatter.png"
    fig.savefig(os.path.join(FIG_DIR, fname), dpi=300)
    plt.close(fig)
    print(f"  Saved: {fname}")


# ---------------------------------------------------------------------------
# Figure C: Convergence Heatmap
# ---------------------------------------------------------------------------
def figure_convergence_heatmap(runs: list[dict], analyses: list[dict]):
    """One panel per Nm; cell = 1 if both X and Y converged."""
    Nm_vals = sorted(set(r["Nm"] for r in runs))
    D_vals = sorted(set(r["D"] for r in runs))
    A_vals = sorted(set(r["A"] for r in runs))

    n_Nm = len(Nm_vals)
    if n_Nm == 0:
        print("  SKIP convergence heatmap: no data.")
        return

    fig, axes = plt.subplots(
        1, n_Nm,
        figsize=(4.5 * n_Nm + 1, max(3, 0.6 * len(D_vals) + 1.5)),
        squeeze=False,
    )
    axes = axes.flatten()

    for panel_idx, Nm in enumerate(Nm_vals):
        ax = axes[panel_idx]
        grid = np.full((len(D_vals), len(A_vals)), np.nan)

        for run, ana in zip(runs, analyses):
            if run["Nm"] != Nm:
                continue
            di = D_vals.index(run["D"]) if run["D"] in D_vals else None
            ai = A_vals.index(run["A"]) if run["A"] in A_vals else None
            if di is None or ai is None:
                continue
            grid[di, ai] = 1.0 if ana["converged"] else 0.0

        im = ax.imshow(
            grid, aspect="auto", origin="lower",
            cmap=plt.cm.RdYlGn, vmin=0.0, vmax=1.0,
            interpolation="nearest",
        )

        ax.set_xticks(range(len(A_vals)))
        ax.set_xticklabels([f"{a:.3f}" for a in A_vals],
                           fontsize=8, rotation=45)
        ax.set_yticks(range(len(D_vals)))
        ax.set_yticklabels([f"{d:.3f}" for d in D_vals], fontsize=8)

        ax.set_xlabel(r"Amplitude $A$", fontsize=10)
        if panel_idx == 0:
            ax.set_ylabel(r"Diffusion $D$", fontsize=10)
        ax.set_title(rf"$N_m = {Nm}$", fontsize=12, fontweight="bold")

        # Annotations
        for di_idx in range(len(D_vals)):
            for ai_idx in range(len(A_vals)):
                val = grid[di_idx, ai_idx]
                if np.isnan(val):
                    ax.text(ai_idx, di_idx, "--", ha="center", va="center",
                            fontsize=9, color="0.5")
                else:
                    label = "Y" if val > 0.5 else "N"
                    txt_color = "black" if val > 0.5 else "white"
                    ax.text(ai_idx, di_idx, label, ha="center",
                            va="center", fontsize=9, color=txt_color,
                            fontweight="bold")

    fig.colorbar(
        plt.cm.ScalarMappable(cmap=plt.cm.RdYlGn,
                              norm=mcolors.Normalize(0, 1)),
        ax=axes.tolist(), label="Both converged",
        shrink=0.8, pad=0.04,
    )

    fig.suptitle(
        "Dissipation Geometry Convergence -- Heatmap by $(D, A, N_m)$",
        fontsize=14, fontweight="bold", y=1.03,
    )
    fig.tight_layout()

    fname = "convergence_heatmap.png"
    fig.savefig(os.path.join(FIG_DIR, fname), dpi=300, bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved: {fname}")


# ---------------------------------------------------------------------------
# Summary table and invariance verdict
# ---------------------------------------------------------------------------
def print_summary(runs: list[dict], analyses: list[dict]):
    print(f"\n{'='*120}")
    print("  Invariant Dissipation Geometry -- Summary Table")
    print(f"{'='*120}")

    print(f"  {'D':<7} {'A':<7} {'Nm':<5} "
          f"{'X*':<14} {'Y*':<14} "
          f"{'σ_X':<12} {'σ_Y':<12} "
          f"{'R²_X':<8} {'R²_Y':<8} "
          f"{'CX':<4} {'CY':<4} {'Both':<5}")
    print("  " + "-" * 105)

    all_X = []
    all_Y = []

    for run, ana in zip(runs, analyses):
        cx = "Y" if ana["conv_X"] else "N"
        cy = "Y" if ana["conv_Y"] else "N"
        both = "Y" if ana["converged"] else "N"

        print(f"  {run['D']:<7.3f} {run['A']:<7.4f} {run['Nm']:<5d} "
              f"{ana['X_star']:<14.6e} {ana['Y_star']:<14.6e} "
              f"{ana['sigma_X']:<12.4e} {ana['sigma_Y']:<12.4e} "
              f"{ana['R2_X']:<8.4f} {ana['R2_Y']:<8.4f} "
              f"{cx:<4} {cy:<4} {both:<5}")

        if not np.isnan(ana["X_star"]):
            all_X.append(ana["X_star"])
        if not np.isnan(ana["Y_star"]):
            all_Y.append(ana["Y_star"])

    # --- Global statistics ---
    print(f"\n  {'Coord':<8} {'Mean':<14} {'Std':<14} "
          f"{'Min':<14} {'Max':<14} {'CV':<10} {'Verdict'}")
    print("  " + "-" * 80)

    for label, arr_list in [("X* (E)", all_X), ("Y* (D)", all_Y)]:
        arr = np.array(arr_list)
        if len(arr) == 0:
            print(f"  {label:<8} (no data)")
            continue

        mean_v = np.mean(arr)
        std_v = np.std(arr)
        cv = std_v / max(abs(mean_v), 1e-30)

        if cv < 0.05:
            verdict = "INVARIANT"
        elif cv < 0.15:
            verdict = "WEAKLY INVARIANT"
        else:
            verdict = "NOT INVARIANT"

        print(f"  {label:<8} "
              f"{mean_v:<14.6e} {std_v:<14.6e} "
              f"{np.min(arr):<14.6e} {np.max(arr):<14.6e} "
              f"{cv:<10.4f} {verdict}")

    # Overall convergence
    total = len(runs)
    conv_both = sum(1 for ana in analyses if ana["converged"])
    conv_X = sum(1 for ana in analyses if ana["conv_X"])
    conv_Y = sum(1 for ana in analyses if ana["conv_Y"])
    print(f"\n  Convergence: X={conv_X}/{total}, Y={conv_Y}/{total}, "
          f"Both={conv_both}/{total} "
          f"({100*conv_both/max(total,1):.1f}%)")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    os.makedirs(FIG_DIR, exist_ok=True)

    print("Discovering regime volume runs...")
    runs = discover_regime_runs()

    if not runs:
        print(f"\nERROR: No admissible regime_D*_A*_Nm* runs found in:")
        print(f"  {RUNS_DIR}")
        print("\nRun the regime volume experiment first:")
        print("  python experiments/regime_volume_3d.py")
        sys.exit(1)

    print(f"  Found {len(runs)} admissible runs.")
    print(f"  D range:  {min(r['D'] for r in runs):.3f} - "
          f"{max(r['D'] for r in runs):.3f}")
    print(f"  A range:  {min(r['A'] for r in runs):.4f} - "
          f"{max(r['A'] for r in runs):.4f}")
    print(f"  Nm range: {min(r['Nm'] for r in runs)} - "
          f"{max(r['Nm'] for r in runs)}")

    # --- Analyse all runs ---
    print("\nComputing dissipation geometry...")
    analyses = []
    for i, run in enumerate(runs):
        ana = analyse_run(run)
        analyses.append(ana)
        if (i + 1) % 10 == 0 or i == len(runs) - 1:
            c_str = "Y" if ana["converged"] else "N"
            print(f"  [{i+1}/{len(runs)}] {run['name']}: "
                  f"X*={ana['X_star']:.4e} Y*={ana['Y_star']:.4e} "
                  f"(conv={c_str})")

    # --- Figures ---
    print("\n--- (A) Energy-Dissipation Trajectory ---")
    figure_trajectory(runs, analyses)

    print("\n--- (B) Attractor Geometry Scatter ---")
    figure_attractor_scatter(runs, analyses)

    print("\n--- (C) Convergence Heatmap ---")
    figure_convergence_heatmap(runs, analyses)

    # --- Summary ---
    print_summary(runs, analyses)

    print(f"\nAll figures saved to: {FIG_DIR}")
    print("Done.")


if __name__ == "__main__":
    main()
