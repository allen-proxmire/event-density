"""
invariant_geometric_norms.py
=============================
Experiment / Analysis: Invariant Geometric Norm Structure

Scans all completed regime_D*_A*_Nm* runs, computes the weighted spectral
norms (geometric norms)

    G_alpha(t) = Σ_k  k^alpha  |a_k(t)|²

for a fixed set of exponents alpha in {−2, −1, 0, 1, 2, 3, 4}, and analyses
their convergence toward late-time attractor values G_alpha^*.

These norms probe the shape of the spectral distribution at different
scales: negative alpha weights low modes (large-scale structure), positive alpha
weights high modes (small-scale / gradient structure).  Their attractor
values and convergence rates are structural invariants of the ED
architecture (Appendix C.4-C.5, Appendix D).

Produces:
  (A) Geometric Norm Evolution -- G_alpha(t) for a representative run.
  (B) Attractor Geometry Profile -- G_alpha^* vs D for all runs.
  (C) Convergence Heatmap -- fraction converged across (D, A, Nm) per alpha.

All figures saved to output/figures/invariants/geometric_norms/
as PNG (300 dpi).

Usage:
    python experiments/invariant_geometric_norms.py

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

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SIM_DIR = os.path.dirname(SCRIPT_DIR)  # ED Simulation/
RUNS_DIR = os.path.join(SIM_DIR, "output", "runs")
FIG_DIR = os.path.join(SIM_DIR, "output", "figures", "invariants",
                        "geometric_norms")

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
ALPHAS = [-2, -1, 0, 1, 2, 3, 4]   # Exponent set
LATE_FRAC = 0.10                     # Fraction for late-time average
FIT_FRAC = 0.20                      # Fraction for convergence fit
R2_THRESH = 0.95                     # R² threshold for convergence

# Labels and colors for each alpha
ALPHA_COLORS = {
    -2: "#1b9e77", -1: "#d95f02", 0: "#7570b3",
    1: "#e7298a", 2: "#66a61e", 3: "#e6ab02", 4: "#a6761d",
}
ALPHA_LABELS = {a: rf"$G_{{{a}}}$" for a in ALPHAS}


# ---------------------------------------------------------------------------
# Discovery (shared pattern)
# ---------------------------------------------------------------------------
def discover_regime_runs() -> list[dict]:
    """Scan RUNS_DIR for regime_D*_A*_Nm* folders with valid modal data."""
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
        modal = ts.get("modal_amplitudes")
        t = ts.get("t")

        if modal is None or t is None or modal.ndim != 2:
            continue

        n = min(len(t), modal.shape[0])
        if modal.shape[1] < 2:
            continue

        runs.append({
            "dir": d,
            "name": name,
            "D": float(D_val),
            "A": float(A_val),
            "Nm": int(Nm_val),
            "metadata": meta,
            "t": t[:n],
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
# Streaming per-run analysis
# ---------------------------------------------------------------------------
def analyse_run(run: dict) -> dict:
    """Compute geometric norms and their attractor summaries.

    Streams through exponents one at a time.  For each alpha, the norm
    G_alpha(t) = Σ_k k^alpha |a_k(t)|² is computed as a dot product (no new
    2-D allocation), then the summary is extracted and the 1-D norm
    array is discarded.

    Returns dict with:
        norms: {alpha: {"G_star": float, "sigma": float, "R2": float,
                     "converged": bool}}
        n_converged, frac_converged
    """
    modal = run["modal"]        # shape (n_steps, n_modes)
    t = run["t"]
    n_steps, n_modes = modal.shape

    # Pre-compute |a_k|² -- shape (n_steps, n_modes).
    # This is the only 2-D array we hold; it replaces repeated squaring.
    a_sq = modal ** 2           # element-wise; same size as modal

    # Mode indices starting from 1 (skip k=0 for negative alpha to avoid 0^alpha)
    # For alpha < 0, k=0 would give 0^alpha = inf, so we start from k=1.
    # For alpha >= 0, k=0 gives 0^alpha = 0 (alpha>0) or 1 (alpha=0), but the
    # homogeneous mode a_0 is part of the mass, not the gradient
    # structure.  We include k >= 1 uniformly for consistency.
    k_indices = np.arange(1, n_modes)   # [1, 2, ..., n_modes-1]
    a_sq_active = a_sq[:, 1:]           # shape (n_steps, n_modes-1)

    norms = {}
    n_converged = 0

    for alpha in ALPHAS:
        # Weight vector: k^alpha for k = 1, ..., n_modes-1
        weights = k_indices.astype(np.float64) ** alpha   # (n_modes-1,)

        # G_alpha(t) = Σ_{k>=1} k^alpha |a_k(t)|²  -- via matrix-vector product
        G = a_sq_active @ weights                         # (n_steps,)

        # Late-time average
        start = max(0, int((1.0 - LATE_FRAC) * len(G)))
        G_star = float(np.mean(G[start:]))

        # Convergence fit
        fit = _fit_exponential(t, G, G_star)

        norms[alpha] = {
            "G_star": G_star,
            "sigma": fit["sigma"],
            "R2": fit["R2"],
            "converged": fit["converged"],
        }
        if fit["converged"]:
            n_converged += 1

        del G  # discard norm array

    del a_sq, a_sq_active  # free the squared-amplitude matrix

    frac = n_converged / max(len(ALPHAS), 1)

    return {
        "norms": norms,
        "n_converged": n_converged,
        "frac_converged": frac,
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


# ---------------------------------------------------------------------------
# Figure A: Geometric Norm Evolution (representative run)
# ---------------------------------------------------------------------------
def figure_norm_evolution(runs: list[dict], analyses: list[dict]):
    """Plot G_alpha(t) for all alpha on semilog-y for the run with largest Nm.

    Recomputes norm time series on-the-fly for the single representative
    run.
    """
    best_idx = max(range(len(runs)), key=lambda i: runs[i]["Nm"])
    run = runs[best_idx]
    ana = analyses[best_idx]

    t = run["t"]
    modal = run["modal"]
    n_steps, n_modes = modal.shape

    k_indices = np.arange(1, n_modes)
    a_sq_active = modal[:, 1:] ** 2

    fig, ax = plt.subplots(figsize=(10, 6))

    for alpha in ALPHAS:
        weights = k_indices.astype(np.float64) ** alpha
        G = a_sq_active @ weights
        G_star = ana["norms"][alpha]["G_star"]

        color = ALPHA_COLORS[alpha]
        ax.semilogy(
            t[:len(G)], np.maximum(G, 1e-30),
            color=color, linewidth=1.4,
            label=ALPHA_LABELS[alpha],
        )

        # Attractor line
        if G_star > 1e-30:
            ax.axhline(
                G_star, color=color, linestyle="--",
                linewidth=0.8, alpha=0.5,
            )

        del G

    del a_sq_active

    setup_axes(
        ax,
        xlabel=r"Time $t$",
        ylabel=r"Geometric norm $G_\alpha(t)$",
        title=(f"Geometric Norms -- D={run['D']}, A={run['A']}, "
               f"Nm={run['Nm']}"),
    )
    ax.legend(fontsize=9, loc="upper right", framealpha=0.9, ncol=2)
    fig.tight_layout()

    fname = "norm_evolution.png"
    fig.savefig(os.path.join(FIG_DIR, fname), dpi=300)
    plt.close(fig)
    print(f"  Saved: {fname}")


# ---------------------------------------------------------------------------
# Figure B: Attractor Geometry Profile (G_alpha^* vs D, all runs)
# ---------------------------------------------------------------------------
def figure_attractor_profile(runs: list[dict], analyses: list[dict]):
    """One panel per alpha: G_alpha^* vs D, colored by A, marker by Nm."""
    A_vals = sorted(set(r["A"] for r in runs))
    Nm_vals = sorted(set(r["Nm"] for r in runs))

    A_cmap = plt.cm.viridis
    A_norm = mcolors.Normalize(
        vmin=min(A_vals) * 0.8 if A_vals else 0,
        vmax=max(A_vals) * 1.2 if A_vals else 1,
    )
    Nm_markers = {Nm_vals[i]: m for i, m in
                  zip(range(len(Nm_vals)),
                      ["o", "s", "^", "D", "v", "P", "*"])}

    n_alpha = len(ALPHAS)
    n_cols = min(4, n_alpha)
    n_rows = (n_alpha + n_cols - 1) // n_cols

    fig, axes = plt.subplots(
        n_rows, n_cols,
        figsize=(4.5 * n_cols, 4 * n_rows),
        squeeze=False,
    )

    for panel_idx, alpha in enumerate(ALPHAS):
        row, col = divmod(panel_idx, n_cols)
        ax = axes[row][col]

        # Collect all G_alpha^* for global mean
        all_G = [ana["norms"][alpha]["G_star"]
                 for ana in analyses
                 if not np.isnan(ana["norms"][alpha]["G_star"])
                 and ana["norms"][alpha]["G_star"] > 1e-30]
        global_mean = np.mean(all_G) if all_G else np.nan

        for run, ana in zip(runs, analyses):
            G_star = ana["norms"][alpha]["G_star"]
            if np.isnan(G_star) or G_star <= 1e-30:
                continue

            color = A_cmap(A_norm(run["A"]))
            marker = Nm_markers.get(run["Nm"], "o")

            ax.scatter(
                run["D"], G_star,
                color=color, marker=marker, s=40, alpha=0.7,
                edgecolors="0.3", linewidths=0.3,
            )

        if not np.isnan(global_mean) and global_mean > 1e-30:
            ax.axhline(global_mean, color="0.4", linestyle="--",
                       linewidth=0.9, alpha=0.5)

        ax.set_yscale("log")
        setup_axes(
            ax,
            xlabel=r"$D$" if row == n_rows - 1 else "",
            ylabel=ALPHA_LABELS[alpha] + r"$^*$" if col == 0 else "",
            title=rf"$\alpha = {alpha}$",
        )

    # Hide unused panels
    for panel_idx in range(n_alpha, n_rows * n_cols):
        row, col = divmod(panel_idx, n_cols)
        axes[row][col].set_visible(False)

    # Shared colorbar
    sm = plt.cm.ScalarMappable(cmap=A_cmap, norm=A_norm)
    sm.set_array([])
    cbar = fig.colorbar(sm, ax=axes.tolist(), label=r"Amplitude $A$",
                        shrink=0.7, pad=0.03)
    cbar.ax.tick_params(labelsize=9)

    # Marker legend
    legend_handles = []
    for Nm, marker in Nm_markers.items():
        h = plt.Line2D(
            [0], [0], marker=marker, color="0.5", markersize=7,
            linestyle="None", label=rf"$N_m = {Nm}$",
        )
        legend_handles.append(h)
    axes[0][-1].legend(
        handles=legend_handles, fontsize=7, loc="upper right",
        framealpha=0.9, title="Seed count",
    )

    fig.suptitle(
        "Geometric Norm Attractor Profile -- All Admissible Runs",
        fontsize=14, fontweight="bold", y=1.01,
    )
    fig.tight_layout()

    fname = "attractor_profile.png"
    fig.savefig(os.path.join(FIG_DIR, fname), dpi=300, bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved: {fname}")


# ---------------------------------------------------------------------------
# Figure C: Convergence Heatmap (one panel per alpha)
# ---------------------------------------------------------------------------
def figure_convergence_heatmap(runs: list[dict], analyses: list[dict]):
    """One panel per alpha; cell color = converged (1) or not (0)."""
    D_vals = sorted(set(r["D"] for r in runs))
    A_vals = sorted(set(r["A"] for r in runs))
    Nm_vals = sorted(set(r["Nm"] for r in runs))

    # For each alpha, aggregate convergence across Nm values:
    # cell value = fraction of Nm values for which that (D, A) converged.
    n_alpha = len(ALPHAS)
    n_cols = min(4, n_alpha)
    n_rows = (n_alpha + n_cols - 1) // n_cols

    fig, axes = plt.subplots(
        n_rows, n_cols,
        figsize=(4.2 * n_cols + 1.5, max(3, 0.55 * len(D_vals) + 1.5) * n_rows),
        squeeze=False,
    )

    for panel_idx, alpha in enumerate(ALPHAS):
        row, col = divmod(panel_idx, n_cols)
        ax = axes[row][col]

        # Grid: count converged across Nm for each (D, A)
        conv_count = np.zeros((len(D_vals), len(A_vals)))
        total_count = np.zeros((len(D_vals), len(A_vals)))

        for run, ana in zip(runs, analyses):
            di = D_vals.index(run["D"]) if run["D"] in D_vals else None
            ai = A_vals.index(run["A"]) if run["A"] in A_vals else None
            if di is None or ai is None:
                continue
            total_count[di, ai] += 1
            if ana["norms"][alpha]["converged"]:
                conv_count[di, ai] += 1

        # Fraction converged (NaN where no runs)
        with np.errstate(invalid="ignore"):
            grid = np.where(total_count > 0,
                            conv_count / total_count, np.nan)

        im = ax.imshow(
            grid, aspect="auto", origin="lower",
            cmap=plt.cm.RdYlGn, vmin=0.0, vmax=1.0,
            interpolation="nearest",
        )

        ax.set_xticks(range(len(A_vals)))
        ax.set_xticklabels([f"{a:.3f}" for a in A_vals],
                           fontsize=7, rotation=45)
        ax.set_yticks(range(len(D_vals)))
        ax.set_yticklabels([f"{d:.3f}" for d in D_vals], fontsize=7)

        if row == n_rows - 1:
            ax.set_xlabel(r"$A$", fontsize=9)
        if col == 0:
            ax.set_ylabel(r"$D$", fontsize=9)
        ax.set_title(rf"$\alpha = {alpha}$", fontsize=11, fontweight="bold")

        # Annotations
        for di_idx in range(len(D_vals)):
            for ai_idx in range(len(A_vals)):
                tot = int(total_count[di_idx, ai_idx])
                if tot == 0:
                    ax.text(ai_idx, di_idx, "--", ha="center", va="center",
                            fontsize=7, color="0.5")
                else:
                    cv = int(conv_count[di_idx, ai_idx])
                    val = grid[di_idx, ai_idx]
                    txt_color = "white" if val < 0.4 else "black"
                    ax.text(ai_idx, di_idx, f"{cv}/{tot}", ha="center",
                            va="center", fontsize=7, color=txt_color,
                            fontweight="bold")

    # Hide unused panels
    for panel_idx in range(n_alpha, n_rows * n_cols):
        r, c = divmod(panel_idx, n_cols)
        axes[r][c].set_visible(False)

    fig.colorbar(
        plt.cm.ScalarMappable(cmap=plt.cm.RdYlGn,
                              norm=mcolors.Normalize(0, 1)),
        ax=axes.tolist(),
        label="Fraction converged (across $N_m$)",
        shrink=0.7, pad=0.04,
    )

    fig.suptitle(
        r"Geometric Norm Convergence -- Heatmap by $(D, A)$, per $\alpha$",
        fontsize=14, fontweight="bold", y=1.02,
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
    # --- Per-run table ---
    alpha_hdr = "  ".join(f"G_{a}*" for a in ALPHAS)
    print(f"\n{'='*130}")
    print("  Invariant Geometric Norms -- Summary Table")
    print(f"{'='*130}")

    print(f"  {'D':<7} {'A':<7} {'Nm':<5} "
          f"{'Conv':<8} {'Frac':<8} ", end="")
    for a in ALPHAS:
        print(f"{'G_'+str(a)+'*':<12}", end="")
    print()
    print("  " + "-" * 120)

    # Collect per-alpha values
    all_G = {a: [] for a in ALPHAS}

    for run, ana in zip(runs, analyses):
        norms = ana["norms"]

        # Convergence string
        conv_str = ""
        for a in ALPHAS:
            conv_str += "+" if norms[a]["converged"] else "."

        print(f"  {run['D']:<7.3f} {run['A']:<7.4f} {run['Nm']:<5d} "
              f"{conv_str:<8} {ana['frac_converged']:<8.1%} ", end="")
        for a in ALPHAS:
            G_s = norms[a]["G_star"]
            print(f"{G_s:<12.4e}", end="")
            if not np.isnan(G_s) and G_s > 1e-30:
                all_G[a].append(G_s)
        print()

    # --- Global statistics ---
    print(f"\n  {'Alpha':<8} {'Mean':<14} {'Std':<14} "
          f"{'Min':<14} {'Max':<14} {'CV':<10} {'Verdict'}")
    print("  " + "-" * 90)

    for a in ALPHAS:
        arr = np.array(all_G[a])
        if len(arr) == 0:
            print(f"  alpha={a:<5} (no data)")
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

        print(f"  alpha={a:<5} "
              f"{mean_v:<14.6e} {std_v:<14.6e} "
              f"{np.min(arr):<14.6e} {np.max(arr):<14.6e} "
              f"{cv:<10.4f} {verdict}")

    # Overall convergence
    total = len(runs) * len(ALPHAS)
    total_conv = sum(ana["n_converged"] for ana in analyses)
    print(f"\n  Overall convergence: {total_conv}/{total} "
          f"({100*total_conv/max(total,1):.1f}%)")


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

    # --- Analyse all runs (streaming) ---
    print(f"\nComputing geometric norms (alpha in {ALPHAS})...")
    analyses = []
    for i, run in enumerate(runs):
        ana = analyse_run(run)
        analyses.append(ana)
        if (i + 1) % 10 == 0 or i == len(runs) - 1:
            n_c = ana["n_converged"]
            print(f"  [{i+1}/{len(runs)}] {run['name']}: "
                  f"{n_c}/{len(ALPHAS)} converged")

    # --- Figures ---
    print("\n--- (A) Geometric Norm Evolution ---")
    figure_norm_evolution(runs, analyses)

    print("\n--- (B) Attractor Geometry Profile ---")
    figure_attractor_profile(runs, analyses)

    print("\n--- (C) Convergence Heatmap ---")
    figure_convergence_heatmap(runs, analyses)

    # --- Summary ---
    print_summary(runs, analyses)

    print(f"\nAll figures saved to: {FIG_DIR}")
    print("Done.")


if __name__ == "__main__":
    main()
