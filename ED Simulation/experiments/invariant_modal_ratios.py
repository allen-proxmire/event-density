"""
invariant_modal_ratios.py
=========================
Experiment / Analysis: Invariant Modal Ratio Structure

Scans all completed regime_D*_A*_Nm* runs, computes the inter-modal
amplitude ratios R_k(t) = |a_{k+1}(t)| / |a_k(t)|, and produces:

  (A) Modal Ratio Evolution — R_k(t) for k = 1..10 (representative run).
  (B) Modal Ratio Attractor Profile — R_k^* vs k (all runs overlaid).
  (C) Convergence Heatmap — boolean convergence flags across (D, A, Nm).

Also prints a summary table.

All figures saved to output/figures/invariants/modal_ratios/ as PNG (300 dpi).

Usage:
    python experiments/invariant_modal_ratios.py

Requires: numpy, matplotlib.
"""

import os
import sys
import glob
import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SIM_DIR = os.path.dirname(SCRIPT_DIR)  # ED Simulation/
RUNS_DIR = os.path.join(SIM_DIR, "output", "runs")
FIG_DIR = os.path.join(SIM_DIR, "output", "figures", "invariants", "modal_ratios")

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
# Number of ratio indices to analyse (R_1 through R_K_MAX)
K_MAX = 10

# Fraction of time series used for late-time average
LATE_FRAC = 0.10

# Fraction used for convergence-rate fit
FIT_FRAC = 0.20

# Minimum amplitude below which a mode is treated as dead
AMP_FLOOR = 1e-28

# R^2 threshold for declaring convergence
R2_THRESH = 0.95


# ---------------------------------------------------------------------------
# Discovery
# ---------------------------------------------------------------------------
def discover_regime_runs() -> list[dict]:
    """Scan RUNS_DIR for regime_D*_A*_Nm* folders with valid data.

    Returns a list of dicts with keys:
        dir, name, D, A, Nm, metadata, t, modal
    sorted by (D, A, Nm).
    """
    pattern = os.path.join(RUNS_DIR, "regime_D*_A*_Nm*")
    dirs = sorted(glob.glob(pattern))

    runs = []
    for d in dirs:
        ts_path = os.path.join(d, "time_series.npz")
        meta_path = os.path.join(d, "metadata.json")
        if not os.path.isfile(ts_path):
            continue

        # Load metadata
        meta = {}
        if os.path.isfile(meta_path):
            with open(meta_path, "r") as f:
                meta = json.load(f)

        # Skip inadmissible runs
        regime = meta.get("regime", "")
        if regime == "inadmissible":
            continue

        # Extract parameters
        D = meta.get("D")
        A = meta.get("A") or meta.get("A_per_mode")
        Nm = meta.get("Nm") or meta.get("n_seeded") or meta.get("N_modes_seeded")

        # Fallback: parse from directory name
        name = os.path.basename(d)
        if D is None or A is None or Nm is None:
            D, A, Nm = _parse_dirname(name, D, A, Nm)

        if D is None or A is None or Nm is None:
            continue

        # Load time series
        ts = np.load(ts_path, allow_pickle=True)
        modal = ts.get("modal_amplitudes")
        t = ts.get("t")

        if modal is None or t is None:
            continue
        if modal.ndim != 2:
            continue

        n = min(len(t), modal.shape[0])
        n_modes = modal.shape[1]

        # Need at least K_MAX + 1 modes
        if n_modes < 2:
            continue

        runs.append({
            "dir": d,
            "name": name,
            "D": float(D),
            "A": float(A),
            "Nm": int(Nm),
            "metadata": meta,
            "t": t[:n],
            "modal": modal[:n],
        })

    # Sort by (D, A, Nm)
    runs.sort(key=lambda r: (r["D"], r["A"], r["Nm"]))
    return runs


def _parse_dirname(name: str, D, A, Nm):
    """Fallback parser for directory names like regime_D0.1_A0.02_Nm20."""
    import re
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
# Ratio computation
# ---------------------------------------------------------------------------
def compute_ratios(modal: np.ndarray, k_max: int) -> np.ndarray:
    """Compute R_k(t) = |a_{k+1}(t)| / |a_k(t)| for k = 1..k_max.

    Parameters
    ----------
    modal : ndarray, shape (n_steps, n_modes)
    k_max : int

    Returns
    -------
    ratios : ndarray, shape (n_steps, k_max)
        ratios[:, j] = R_{j+1}(t), i.e. column j corresponds to k = j+1.
        NaN where the denominator is below AMP_FLOOR.
    """
    n_steps, n_modes = modal.shape
    k_eff = min(k_max, n_modes - 2)  # need a_{k+1} → mode index k+1
    ratios = np.full((n_steps, k_eff), np.nan)

    for j in range(k_eff):
        k = j + 1  # mode index for denominator
        num = np.abs(modal[:, k + 1])
        den = np.abs(modal[:, k])

        valid = den > AMP_FLOOR
        ratios[valid, j] = num[valid] / den[valid]

    return ratios


def late_time_average(ratios: np.ndarray, frac: float) -> np.ndarray:
    """Compute the late-time mean of each ratio column.

    Returns ndarray of shape (k_eff,). NaN if insufficient valid data.
    """
    n_steps, k_eff = ratios.shape
    start = max(0, int((1.0 - frac) * n_steps))
    late = ratios[start:]

    averages = np.full(k_eff, np.nan)
    for j in range(k_eff):
        col = late[:, j]
        valid = ~np.isnan(col)
        if np.sum(valid) > 5:
            averages[j] = np.nanmean(col)
    return averages


def fit_convergence(t: np.ndarray, ratios: np.ndarray,
                    R_star: np.ndarray, frac: float) -> list[dict]:
    """Fit exponential convergence |R_k(t) - R_k^*| ~ C exp(-sigma t).

    Returns a list of dicts (one per ratio index) with keys:
        sigma, C, R2, converged
    """
    n_steps, k_eff = ratios.shape
    start = max(0, int((1.0 - frac) * n_steps))
    results = []

    for j in range(k_eff):
        entry = {"sigma": 0.0, "C": 0.0, "R2": 0.0, "converged": False}

        if np.isnan(R_star[j]):
            results.append(entry)
            continue

        residual = np.abs(ratios[start:, j] - R_star[j])
        t_fit = t[start:]

        valid = (~np.isnan(residual)) & (residual > 1e-30)
        if np.sum(valid) < 10:
            results.append(entry)
            continue

        log_r = np.log(residual[valid])
        t_v = t_fit[valid]

        try:
            coeffs = np.polyfit(t_v, log_r, 1)
            sigma = -coeffs[0]
            C = np.exp(coeffs[1])

            predicted = coeffs[0] * t_v + coeffs[1]
            ss_res = np.sum((log_r - predicted) ** 2)
            ss_tot = np.sum((log_r - np.mean(log_r)) ** 2)
            R2 = 1.0 - ss_res / max(ss_tot, 1e-30)

            entry["sigma"] = sigma
            entry["C"] = C
            entry["R2"] = R2
            entry["converged"] = R2 > R2_THRESH and sigma > 0
        except (np.linalg.LinAlgError, ValueError):
            pass

        results.append(entry)

    return results


# ---------------------------------------------------------------------------
# Analysis pipeline (per run)
# ---------------------------------------------------------------------------
def analyse_run(run: dict) -> dict:
    """Compute ratios, late-time averages, and convergence fits for one run.

    Returns dict with keys: ratios, R_star, fits, k_eff.
    """
    modal = run["modal"]
    t = run["t"]
    n_modes = modal.shape[1]
    k_eff = min(K_MAX, n_modes - 2)

    ratios = compute_ratios(modal, k_eff)
    R_star = late_time_average(ratios, LATE_FRAC)
    fits = fit_convergence(t, ratios, R_star, FIT_FRAC)

    return {
        "ratios": ratios,
        "R_star": R_star,
        "fits": fits,
        "k_eff": k_eff,
    }


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def setup_axes(ax, xlabel: str, ylabel: str, title: str):
    ax.set_xlabel(xlabel, fontsize=11)
    ax.set_ylabel(ylabel, fontsize=11)
    ax.set_title(title, fontsize=13, fontweight="bold")
    ax.tick_params(labelsize=10)
    ax.grid(True, alpha=0.3, linewidth=0.5)


# ---------------------------------------------------------------------------
# Figure A: Modal Ratio Evolution (representative run)
# ---------------------------------------------------------------------------
def figure_ratio_evolution(runs: list[dict], analyses: list[dict]):
    """Plot R_k(t) for k = 1..10 from the run with the largest Nm."""
    # Select run with largest Nm
    best_idx = max(range(len(runs)), key=lambda i: runs[i]["Nm"])
    run = runs[best_idx]
    ana = analyses[best_idx]

    t = run["t"]
    ratios = ana["ratios"]
    R_star = ana["R_star"]
    k_eff = ana["k_eff"]

    n_plot = min(k_eff, 10)
    colors = plt.cm.tab10(np.linspace(0, 1, n_plot))

    fig, ax = plt.subplots(figsize=(10, 6))

    for j in range(n_plot):
        k = j + 1
        R_k = ratios[:, j]
        valid = ~np.isnan(R_k)
        if np.sum(valid) < 5:
            continue

        ax.plot(
            t[valid], R_k[valid],
            color=colors[j], linewidth=1.3,
            label=rf"$R_{{{k}}}$",
        )

        # Horizontal dashed line at R_k^*
        if not np.isnan(R_star[j]):
            ax.axhline(
                R_star[j], color=colors[j], linestyle="--",
                linewidth=0.7, alpha=0.5,
            )

    setup_axes(
        ax,
        xlabel=r"Time $t$",
        ylabel=r"Modal ratio $R_k(t) = |a_{k+1}| / |a_k|$",
        title=(f"Modal Ratio Evolution — D={run['D']}, A={run['A']}, "
               f"Nm={run['Nm']}"),
    )
    ax.legend(fontsize=8, loc="upper right", framealpha=0.9, ncol=2)
    fig.tight_layout()

    fname = "ratio_evolution.png"
    fig.savefig(os.path.join(FIG_DIR, fname), dpi=300)
    plt.close(fig)
    print(f"  Saved: {fname}")


# ---------------------------------------------------------------------------
# Figure B: Modal Ratio Attractor Profile (all runs overlaid)
# ---------------------------------------------------------------------------
def figure_attractor_profile(runs: list[dict], analyses: list[dict]):
    """Plot R_k^* vs k for all runs, colored by D, shaped by Nm."""
    # Unique D and Nm values for color/marker mapping
    D_vals = sorted(set(r["D"] for r in runs))
    Nm_vals = sorted(set(r["Nm"] for r in runs))

    D_cmap = plt.cm.plasma
    D_norm = mcolors.Normalize(
        vmin=min(D_vals) * 0.9 if D_vals else 0,
        vmax=max(D_vals) * 1.1 if D_vals else 1,
    )

    Nm_markers = {Nm_vals[i]: m for i, m in
                  zip(range(len(Nm_vals)), ["o", "s", "^", "D", "v", "P", "*"])}

    fig, ax = plt.subplots(figsize=(10, 6))

    for run, ana in zip(runs, analyses):
        R_star = ana["R_star"]
        k_eff = ana["k_eff"]

        ks = np.arange(1, k_eff + 1)
        valid = ~np.isnan(R_star)
        if np.sum(valid) < 1:
            continue

        color = D_cmap(D_norm(run["D"]))
        marker = Nm_markers.get(run["Nm"], "o")

        ax.plot(
            ks[valid], R_star[valid],
            color=color, marker=marker, markersize=5,
            linewidth=0.8, alpha=0.6,
        )

    # Colorbar for D
    sm = plt.cm.ScalarMappable(cmap=D_cmap, norm=D_norm)
    sm.set_array([])
    cbar = fig.colorbar(sm, ax=ax, label=r"Diffusion $D$", pad=0.02)
    cbar.ax.tick_params(labelsize=9)

    # Marker legend for Nm
    legend_handles = []
    for Nm, marker in Nm_markers.items():
        h = plt.Line2D(
            [0], [0], marker=marker, color="0.5", markersize=7,
            linestyle="None", label=f"$N_m = {Nm}$",
        )
        legend_handles.append(h)
    ax.legend(
        handles=legend_handles, fontsize=9, loc="upper right",
        framealpha=0.9, title="Seed count",
    )

    setup_axes(
        ax,
        xlabel=r"Mode index $k$",
        ylabel=r"Attractor ratio $R_k^*$",
        title="Modal Ratio Attractor Profile — All Admissible Runs",
    )
    ax.set_xticks(range(1, K_MAX + 1))
    fig.tight_layout()

    fname = "attractor_profile.png"
    fig.savefig(os.path.join(FIG_DIR, fname), dpi=300)
    plt.close(fig)
    print(f"  Saved: {fname}")


# ---------------------------------------------------------------------------
# Figure C: Convergence Heatmap
# ---------------------------------------------------------------------------
def figure_convergence_heatmap(runs: list[dict], analyses: list[dict]):
    """Heatmap of convergence flags across (D, A, Nm).

    Since we have three parameter axes, we produce one heatmap per Nm
    (rows = D, cols = A, cell color = fraction of ratio indices converged).
    """
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

        # Build the grid
        grid = np.full((len(D_vals), len(A_vals)), np.nan)

        for run, ana in zip(runs, analyses):
            if run["Nm"] != Nm:
                continue
            di = D_vals.index(run["D"]) if run["D"] in D_vals else None
            ai = A_vals.index(run["A"]) if run["A"] in A_vals else None
            if di is None or ai is None:
                continue

            fits = ana["fits"]
            n_conv = sum(1 for f in fits if f["converged"])
            n_total = len(fits)
            frac = n_conv / max(n_total, 1)
            grid[di, ai] = frac

        # Plot
        cmap = plt.cm.RdYlGn
        im = ax.imshow(
            grid, aspect="auto", origin="lower",
            cmap=cmap, vmin=0.0, vmax=1.0,
            interpolation="nearest",
        )

        # Tick labels
        ax.set_xticks(range(len(A_vals)))
        ax.set_xticklabels([f"{a:.3f}" for a in A_vals], fontsize=8, rotation=45)
        ax.set_yticks(range(len(D_vals)))
        ax.set_yticklabels([f"{d:.3f}" for d in D_vals], fontsize=8)

        ax.set_xlabel(r"Amplitude $A$", fontsize=10)
        if panel_idx == 0:
            ax.set_ylabel(r"Diffusion $D$", fontsize=10)
        ax.set_title(rf"$N_m = {Nm}$", fontsize=12, fontweight="bold")

        # Cell annotations
        for di_idx in range(len(D_vals)):
            for ai_idx in range(len(A_vals)):
                val = grid[di_idx, ai_idx]
                if np.isnan(val):
                    ax.text(ai_idx, di_idx, "—", ha="center", va="center",
                            fontsize=8, color="0.5")
                else:
                    txt_color = "white" if val < 0.4 else "black"
                    ax.text(ai_idx, di_idx, f"{val:.0%}", ha="center",
                            va="center", fontsize=8, color=txt_color,
                            fontweight="bold")

    # Shared colorbar
    fig.colorbar(
        plt.cm.ScalarMappable(cmap=plt.cm.RdYlGn,
                              norm=mcolors.Normalize(0, 1)),
        ax=axes.tolist(), label="Fraction of ratios converged",
        shrink=0.8, pad=0.04,
    )

    fig.suptitle("Modal Ratio Convergence — Heatmap by $(D, A, N_m)$",
                 fontsize=14, fontweight="bold", y=1.03)
    fig.tight_layout()

    fname = "convergence_heatmap.png"
    fig.savefig(os.path.join(FIG_DIR, fname), dpi=300, bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved: {fname}")


# ---------------------------------------------------------------------------
# Summary table
# ---------------------------------------------------------------------------
def print_summary(runs: list[dict], analyses: list[dict]):
    # Header
    ratio_cols = "  ".join(f"R{k}*" for k in range(1, K_MAX + 1))
    conv_cols = "  ".join(f"C{k}" for k in range(1, K_MAX + 1))

    print(f"\n{'='*140}")
    print("  Invariant Modal Ratios — Summary Table")
    print(f"{'='*140}")

    # Compact table: D, A, Nm, R_k^* for k=1..K_MAX
    header = (f"  {'D':<7} {'A':<7} {'Nm':<5} "
              + "  ".join(f"{'R'+str(k)+'^*':>8}" for k in range(1, K_MAX + 1))
              + "  " + "  ".join(f"{'C'+str(k):>4}" for k in range(1, K_MAX + 1)))
    print(header)
    print("  " + "-" * (len(header) - 2))

    for run, ana in zip(runs, analyses):
        R_star = ana["R_star"]
        fits = ana["fits"]
        k_eff = ana["k_eff"]

        ratio_strs = []
        conv_strs = []
        for j in range(K_MAX):
            if j < k_eff and not np.isnan(R_star[j]):
                ratio_strs.append(f"{R_star[j]:8.4f}")
            else:
                ratio_strs.append(f"{'—':>8}")

            if j < len(fits):
                conv_strs.append(f"{'Y' if fits[j]['converged'] else 'N':>4}")
            else:
                conv_strs.append(f"{'—':>4}")

        line = (f"  {run['D']:<7.3f} {run['A']:<7.4f} {run['Nm']:<5d} "
                + "  ".join(ratio_strs) + "  " + "  ".join(conv_strs))
        print(line)

    # Statistics
    all_R1 = [a["R_star"][0] for a in analyses
              if a["k_eff"] >= 1 and not np.isnan(a["R_star"][0])]
    if all_R1:
        print(f"\n  R_1^* statistics (across {len(all_R1)} admissible runs):")
        print(f"    Mean:   {np.mean(all_R1):.6f}")
        print(f"    Std:    {np.std(all_R1):.6f}")
        print(f"    Min:    {np.min(all_R1):.6f}")
        print(f"    Max:    {np.max(all_R1):.6f}")
        cv = np.std(all_R1) / max(abs(np.mean(all_R1)), 1e-30)
        print(f"    CV:     {cv:.4f}")
        if cv < 0.05:
            print(f"    Verdict: INVARIANT (CV < 5%)")
        elif cv < 0.15:
            print(f"    Verdict: WEAKLY INVARIANT (CV < 15%)")
        else:
            print(f"    Verdict: NOT INVARIANT (CV >= 15%)")

    # Convergence summary
    n_total_fits = sum(len(a["fits"]) for a in analyses)
    n_converged = sum(sum(1 for f in a["fits"] if f["converged"])
                      for a in analyses)
    print(f"\n  Convergence: {n_converged}/{n_total_fits} ratio indices converged "
          f"({100*n_converged/max(n_total_fits,1):.1f}%)")


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
    print("\nComputing modal ratios and convergence fits...")
    analyses = []
    for i, run in enumerate(runs):
        ana = analyse_run(run)
        analyses.append(ana)
        if (i + 1) % 10 == 0 or i == len(runs) - 1:
            print(f"  Processed {i+1}/{len(runs)} runs.")

    # --- Figures ---
    print("\n--- (A) Modal Ratio Evolution ---")
    figure_ratio_evolution(runs, analyses)

    print("\n--- (B) Attractor Profile ---")
    figure_attractor_profile(runs, analyses)

    print("\n--- (C) Convergence Heatmap ---")
    figure_convergence_heatmap(runs, analyses)

    # --- Summary ---
    print_summary(runs, analyses)

    print(f"\nAll figures saved to: {FIG_DIR}")
    print("Done.")


if __name__ == "__main__":
    main()
