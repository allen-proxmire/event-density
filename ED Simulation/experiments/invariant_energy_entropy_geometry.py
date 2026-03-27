"""
invariant_energy_entropy_geometry.py
=====================================
Experiment / Analysis: Invariant Energy–Entropy Geometry

Scans all completed regime_D*_A*_Nm* runs, computes the joint trajectory

    (E(t), H(t))

in the energy–entropy plane, where H(t) = −Σ_k p_k log p_k is the
Shannon spectral entropy, and analyses convergence toward the attractor
point (E*, H*).

The energy–entropy plane combines two complementary invariants: E
measures the total perturbation amplitude, H measures how evenly that
amplitude is distributed across modes.  Together they define a
two-dimensional geometric fingerprint of the ED equilibrium — a
structural invariant whose existence follows from the Lyapunov theory
(Appendix C.5) and whose uniqueness follows from Principle 3.

Produces:
  (A) Energy–Entropy Trajectory — parametric curve for a representative run.
  (B) Attractor Geometry Scatter — (E*, H*) for all runs with ellipse.
  (C) Convergence Heatmap — converged/not across (D, A, Nm).

All figures saved to output/figures/invariants/energy_entropy_geometry/
as PNG (300 dpi).

Usage:
    python experiments/invariant_energy_entropy_geometry.py

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
from matplotlib.collections import LineCollection

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SIM_DIR = os.path.dirname(SCRIPT_DIR)
RUNS_DIR = os.path.join(SIM_DIR, "output", "runs")
FIG_DIR = os.path.join(SIM_DIR, "output", "figures", "invariants",
                        "energy_entropy_geometry")

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
LATE_FRAC = 0.10
FIT_FRAC = 0.20
R2_THRESH = 0.95
LOG_FLOOR = 1e-30
N_ARROWS = 12          # Number of directional arrows in Figure A


# ---------------------------------------------------------------------------
# Discovery
# ---------------------------------------------------------------------------
def discover_regime_runs() -> list[dict]:
    """Scan RUNS_DIR for regime_D*_A*_Nm* folders with energy and modal data."""
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

        if meta.get("regime") == "inadmissible":
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
        modal = ts.get("modal_amplitudes")

        if t is None or E is None or modal is None or modal.ndim != 2:
            continue

        n = min(len(t), len(E), modal.shape[0])
        if modal.shape[1] < 3 or n < 50:
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
            "modal": modal[:n],
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
# Shannon entropy computation
# ---------------------------------------------------------------------------
def compute_shannon_entropy(modal: np.ndarray) -> np.ndarray:
    """Compute H(t) = −Σ_k p_k log p_k from modal amplitudes (k ≥ 1)."""
    E_k = modal[:, 1:] ** 2
    E_total = np.sum(E_k, axis=1, keepdims=True)
    E_total = np.maximum(E_total, LOG_FLOOR)
    p = E_k / E_total
    log_p = np.log(p + LOG_FLOOR)
    H = -np.sum(p * log_p, axis=1)
    return H


# ---------------------------------------------------------------------------
# Per-run analysis
# ---------------------------------------------------------------------------
def analyse_run(run: dict) -> dict:
    """Compute energy–entropy attractor and convergence."""
    t = run["t"]
    E = run["E"]
    H = compute_shannon_entropy(run["modal"])

    n = min(len(t), len(E), len(H))
    t = t[:n]
    E = E[:n]
    H = H[:n]

    # Late-time averages
    start = max(0, int((1.0 - LATE_FRAC) * n))
    E_star = float(np.mean(E[start:]))
    H_star = float(np.mean(H[start:]))

    # Convergence fits
    fit_E = _fit_exponential(t, E, E_star)
    fit_H = _fit_exponential(t, H, H_star)

    both = fit_E["converged"] and fit_H["converged"]

    return {
        "E_star": E_star,
        "H_star": H_star,
        "sigma_E": fit_E["sigma"],
        "sigma_H": fit_H["sigma"],
        "R2_E": fit_E["R2"],
        "R2_H": fit_H["R2"],
        "conv_E": fit_E["converged"],
        "conv_H": fit_H["converged"],
        "converged": both,
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
    """2-sigma covariance ellipse from a 2-D point cloud."""
    mean = np.mean(points, axis=0)
    cov = np.cov(points, rowvar=False)
    eigvals, eigvecs = np.linalg.eigh(cov)
    order = eigvals.argsort()[::-1]
    eigvals = eigvals[order]
    eigvecs = eigvecs[:, order]
    angle = np.degrees(np.arctan2(eigvecs[1, 0], eigvecs[0, 0]))
    width = 2 * n_std * np.sqrt(max(eigvals[0], 0))
    height = 2 * n_std * np.sqrt(max(eigvals[1], 0))
    return Ellipse(
        xy=mean, width=width, height=height, angle=angle,
        facecolor="none", edgecolor="0.3", linewidth=1.5,
        linestyle="--", alpha=0.7,
    )


# ---------------------------------------------------------------------------
# Figure A: Energy–Entropy Trajectory (representative run)
# ---------------------------------------------------------------------------
def figure_trajectory(runs: list[dict], analyses: list[dict]):
    """Parametric (E(t), H(t)) colored by time with arrows."""
    best_idx = max(range(len(runs)), key=lambda i: runs[i]["Nm"])
    run = runs[best_idx]
    ana = analyses[best_idx]

    E = run["E"]
    H = compute_shannon_entropy(run["modal"])
    t = run["t"]
    n = min(len(t), len(E), len(H))
    E = E[:n]
    H = H[:n]

    fig, ax = plt.subplots(figsize=(9, 8))

    # Time-colored trajectory
    time_frac = np.linspace(0, 1, n)
    points = np.array([E, H]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)

    norm = plt.Normalize(0, 1)
    lc = LineCollection(segments, cmap="coolwarm", norm=norm,
                        linewidths=1.4, alpha=0.8)
    lc.set_array(time_frac[:-1])
    ax.add_collection(lc)

    # Directional arrows
    arrow_indices = np.linspace(0, n - 2, N_ARROWS, dtype=int)
    for idx in arrow_indices:
        dx = E[min(idx + 1, n - 1)] - E[idx]
        dy = H[min(idx + 1, n - 1)] - H[idx]
        if np.sqrt(dx ** 2 + dy ** 2) < 1e-30:
            continue
        color = plt.cm.coolwarm(idx / max(n - 1, 1))
        ax.annotate(
            "", xy=(E[min(idx + 1, n - 1)], H[min(idx + 1, n - 1)]),
            xytext=(E[idx], H[idx]),
            arrowprops=dict(arrowstyle="-|>", color=color,
                            lw=1.0, alpha=0.5, mutation_scale=12),
        )

    # Markers
    ax.plot(E[0], H[0], "o", color="#2166ac", markersize=10, zorder=10,
            label="Start")
    ax.plot(E[-1], H[-1], "s", color="#b2182b", markersize=9, zorder=10,
            label="End")
    ax.plot(ana["E_star"], ana["H_star"], "*", color="#1b7837",
            markersize=16, zorder=10,
            markeredgecolor="black", markeredgewidth=0.5,
            label=rf"$(E^*, H^*) = ({ana['E_star']:.3e},\;{ana['H_star']:.4f})$")

    # Colorbar
    cbar = fig.colorbar(lc, ax=ax, label="Time (early → late)", pad=0.02)
    cbar.ax.tick_params(labelsize=9)

    # Scale
    pad_x = 0.05 * max(abs(E.max() - E.min()), 1e-10)
    pad_y = 0.05 * max(abs(H.max() - H.min()), 1e-10)
    ax.set_xlim(E.min() - pad_x, E.max() + pad_x)
    ax.set_ylim(H.min() - pad_y, H.max() + pad_y)

    setup_axes(
        ax,
        xlabel=r"Energy $\mathcal{E}(t)$",
        ylabel=r"Shannon entropy $H(t)$",
        title=(f"Energy–Entropy Trajectory — D={run['D']}, "
               f"A={run['A']}, Nm={run['Nm']}"),
    )
    ax.legend(fontsize=9, loc="upper right", framealpha=0.9)
    fig.tight_layout()

    fname = "trajectory.png"
    fig.savefig(os.path.join(FIG_DIR, fname), dpi=300)
    plt.close(fig)
    print(f"  Saved: {fname}")

    del H


# ---------------------------------------------------------------------------
# Figure B: Attractor Geometry Scatter (all runs)
# ---------------------------------------------------------------------------
def figure_attractor_scatter(runs: list[dict], analyses: list[dict]):
    """Scatter (E*, H*) with covariance ellipse."""
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

    all_points = []

    for run, ana in zip(runs, analyses):
        es = ana["E_star"]
        hs = ana["H_star"]
        if np.isnan(es) or np.isnan(hs):
            continue

        color = D_cmap(D_norm(run["D"]))
        marker = Nm_markers.get(run["Nm"], "o")

        ax.scatter(
            es, hs,
            color=color, marker=marker, s=60, alpha=0.7,
            edgecolors="0.3", linewidths=0.4, zorder=5,
        )
        all_points.append([es, hs])

    all_points = np.array(all_points)

    # Global mean
    if len(all_points) > 1:
        mean_pt = np.mean(all_points, axis=0)
        ax.plot(
            mean_pt[0], mean_pt[1], "+", color="black",
            markersize=16, markeredgewidth=2.5, zorder=10,
            label=rf"Mean $= ({mean_pt[0]:.3e},\;{mean_pt[1]:.4f})$",
        )

        # Covariance ellipse
        if len(all_points) >= 3:
            try:
                ellipse = covariance_ellipse(all_points, n_std=2.0)
                ellipse.set_label(r"$2\sigma$ ellipse")
                ax.add_patch(ellipse)
            except np.linalg.LinAlgError:
                pass

    # Colorbar
    sm = plt.cm.ScalarMappable(cmap=D_cmap, norm=D_norm)
    sm.set_array([])
    cbar = fig.colorbar(sm, ax=ax, label=r"Diffusion $D$", pad=0.02)
    cbar.ax.tick_params(labelsize=9)

    # Legend
    legend_handles = [
        plt.Line2D([0], [0], marker=m, color="0.5", markersize=7,
                   linestyle="None", label=rf"$N_m = {Nm}$")
        for Nm, m in Nm_markers.items()
    ]
    for h in ax.get_legend_handles_labels()[0]:
        legend_handles.append(h)
    ax.legend(
        handles=legend_handles, fontsize=8, loc="upper right",
        framealpha=0.9, title="Legend",
    )

    setup_axes(
        ax,
        xlabel=r"Attractor energy $E^*$",
        ylabel=r"Attractor entropy $H^*$",
        title="Energy–Entropy Geometry — Attractor Scatter",
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
    """One panel per Nm; cell = 1 if both E and H converged."""
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

        ax.imshow(
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

        for di_idx in range(len(D_vals)):
            for ai_idx in range(len(A_vals)):
                val = grid[di_idx, ai_idx]
                if np.isnan(val):
                    ax.text(ai_idx, di_idx, "—", ha="center", va="center",
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
        "Energy–Entropy Convergence — Heatmap by $(D, A, N_m)$",
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
    print("  Invariant Energy–Entropy Geometry — Summary Table")
    print(f"{'='*120}")

    print(f"  {'D':<7} {'A':<7} {'Nm':<5} "
          f"{'E*':<14} {'H*':<12} "
          f"{'σ_E':<12} {'σ_H':<12} "
          f"{'R²_E':<8} {'R²_H':<8} "
          f"{'CE':<4} {'CH':<4} {'Both':<5}")
    print("  " + "-" * 105)

    all_E = []
    all_H = []

    for run, ana in zip(runs, analyses):
        ce = "Y" if ana["conv_E"] else "N"
        ch = "Y" if ana["conv_H"] else "N"
        both = "Y" if ana["converged"] else "N"

        print(f"  {run['D']:<7.3f} {run['A']:<7.4f} {run['Nm']:<5d} "
              f"{ana['E_star']:<14.6e} {ana['H_star']:<12.6f} "
              f"{ana['sigma_E']:<12.4e} {ana['sigma_H']:<12.4e} "
              f"{ana['R2_E']:<8.4f} {ana['R2_H']:<8.4f} "
              f"{ce:<4} {ch:<4} {both:<5}")

        if not np.isnan(ana["E_star"]):
            all_E.append(ana["E_star"])
        if not np.isnan(ana["H_star"]):
            all_H.append(ana["H_star"])

    # Global statistics
    print(f"\n  {'Coord':<10} {'Mean':<14} {'Std':<14} "
          f"{'Min':<14} {'Max':<14} {'CV':<10} {'Verdict'}")
    print("  " + "-" * 82)

    for label, arr_list in [("E*", all_E), ("H*", all_H)]:
        arr = np.array(arr_list)
        if len(arr) == 0:
            print(f"  {label:<10} (no data)")
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

        print(f"  {label:<10} "
              f"{mean_v:<14.6e} {std_v:<14.6e} "
              f"{np.min(arr):<14.6e} {np.max(arr):<14.6e} "
              f"{cv:<10.4f} {verdict}")

    # Overall convergence
    total = len(runs)
    conv_both = sum(1 for ana in analyses if ana["converged"])
    conv_E = sum(1 for ana in analyses if ana["conv_E"])
    conv_H = sum(1 for ana in analyses if ana["conv_H"])
    print(f"\n  Convergence: E={conv_E}/{total}, H={conv_H}/{total}, "
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
    print(f"  D range:  {min(r['D'] for r in runs):.3f} – "
          f"{max(r['D'] for r in runs):.3f}")
    print(f"  A range:  {min(r['A'] for r in runs):.4f} – "
          f"{max(r['A'] for r in runs):.4f}")
    print(f"  Nm range: {min(r['Nm'] for r in runs)} – "
          f"{max(r['Nm'] for r in runs)}")

    # --- Analyse all runs ---
    print("\nComputing energy–entropy geometry...")
    analyses = []
    for i, run in enumerate(runs):
        ana = analyse_run(run)
        analyses.append(ana)
        if (i + 1) % 10 == 0 or i == len(runs) - 1:
            c_str = "Y" if ana["converged"] else "N"
            print(f"  [{i+1}/{len(runs)}] {run['name']}: "
                  f"E*={ana['E_star']:.3e} H*={ana['H_star']:.4f} "
                  f"(conv={c_str})")

    # --- Figures ---
    print("\n--- (A) Energy–Entropy Trajectory ---")
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
