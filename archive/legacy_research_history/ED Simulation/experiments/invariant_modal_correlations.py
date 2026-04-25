"""
invariant_modal_correlations.py
================================
Experiment / Analysis: Invariant Modal Correlation Structure

Scans all completed regime_D*_A*_Nm* runs, computes the modal energy
correlation matrix

    C_ij = corr( E_i(t), E_j(t) )

over the attractor window (last 20% of timesteps), where E_k = |a_k|²,
and extracts structural invariants of C: mean off-diagonal correlation,
extremal correlations, spectral radius, and condition number.

The correlation matrix encodes the coupling geometry among modes in the
asymptotic regime -- which modes co-fluctuate, which are independent,
and how the triad coupling (Principle 7) organises the inter-modal
relationships at equilibrium.  Its summary statistics are structural
invariants of the ED architecture (Appendix C.4, Theorem C.34).

Produces:
  (A) Correlation Matrix -- heatmap for a representative run.
  (B) Attractor Correlation Profiles -- mean row correlations for all runs.
  (C) Correlation Invariant Scatter -- summary invariants vs D.

All figures saved to output/figures/invariants/modal_correlations/
as PNG (300 dpi).

Usage:
    python experiments/invariant_modal_correlations.py

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
SIM_DIR = os.path.dirname(SCRIPT_DIR)
RUNS_DIR = os.path.join(SIM_DIR, "output", "runs")
FIG_DIR = os.path.join(SIM_DIR, "output", "figures", "invariants",
                        "modal_correlations")

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
K_MAX = 20               # Maximum number of modes for correlation matrix
ATTRACTOR_FRAC = 0.20    # Last 20% for correlation computation
MIN_VARIANCE = 1e-30     # Floor for std to avoid NaN correlations


# ---------------------------------------------------------------------------
# Discovery
# ---------------------------------------------------------------------------
def discover_regime_runs() -> list[dict]:
    """Scan RUNS_DIR for regime_D*_A*_Nm* folders with modal data."""
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
# Correlation matrix computation
# ---------------------------------------------------------------------------
def compute_correlation_matrix(modal: np.ndarray, n_total: int) -> np.ndarray:
    """Compute the K×K correlation matrix of modal energies in the
    attractor window (last ATTRACTOR_FRAC of timesteps).

    Parameters
    ----------
    modal : ndarray, shape (n_steps, n_modes)
    n_total : int, total number of timesteps

    Returns
    -------
    C : ndarray, shape (K, K), the Pearson correlation matrix.
    K : int, number of modes used.
    """
    n_modes = modal.shape[1]
    K = min(K_MAX, n_modes - 1)  # modes 1..K

    # Attractor window
    start = max(0, int((1.0 - ATTRACTOR_FRAC) * n_total))
    E_window = modal[start:, 1:K+1] ** 2   # (n_window, K)

    n_window = E_window.shape[0]
    if n_window < 10:
        return np.eye(K), K

    # Standardise columns (subtract mean, divide by std)
    means = np.mean(E_window, axis=0)          # (K,)
    stds = np.std(E_window, axis=0)            # (K,)
    stds = np.maximum(stds, MIN_VARIANCE)

    Z = (E_window - means) / stds              # (n_window, K)

    # Correlation = Z^T Z / (n_window - 1)
    C = (Z.T @ Z) / max(n_window - 1, 1)      # (K, K)

    # Clip to [-1, 1] (numerical safety)
    np.clip(C, -1.0, 1.0, out=C)

    return C, K


# ---------------------------------------------------------------------------
# Per-run analysis
# ---------------------------------------------------------------------------
def analyse_run(run: dict) -> dict:
    """Compute correlation matrix and summary invariants."""
    modal = run["modal"]
    n_total = len(run["t"])

    C, K = compute_correlation_matrix(modal, n_total)

    # Summary invariants
    # Off-diagonal mask
    mask_off = ~np.eye(K, dtype=bool)
    off_diag = C[mask_off]

    mean_corr = float(np.mean(off_diag)) if len(off_diag) > 0 else 0.0
    max_corr = float(np.max(off_diag)) if len(off_diag) > 0 else 0.0
    min_corr = float(np.min(off_diag)) if len(off_diag) > 0 else 0.0

    # Spectral radius = max |eigenvalue|
    try:
        eigvals = np.linalg.eigvalsh(C)
        spectral_radius = float(np.max(np.abs(eigvals)))
        # Condition number = max_eigval / min_eigval (both positive for corr matrix)
        eigvals_pos = eigvals[eigvals > 1e-15]
        if len(eigvals_pos) >= 2:
            cond_number = float(np.max(eigvals_pos) / np.min(eigvals_pos))
        else:
            cond_number = float("inf")
    except np.linalg.LinAlgError:
        spectral_radius = float("nan")
        cond_number = float("nan")

    # Mean row correlation (for profile plot)
    mean_row = np.mean(C, axis=1)  # (K,) -- includes diagonal (=1)
    # Exclude self-correlation: mean of off-diagonal per row
    mean_row_off = (np.sum(C, axis=1) - 1.0) / max(K - 1, 1)

    return {
        "C": C,
        "K": K,
        "mean_corr": mean_corr,
        "max_corr": max_corr,
        "min_corr": min_corr,
        "spectral_radius": spectral_radius,
        "cond_number": cond_number,
        "mean_row_off": mean_row_off.tolist(),
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
# Figure A: Correlation Matrix Heatmap (representative run)
# ---------------------------------------------------------------------------
def figure_correlation_matrix(runs: list[dict], analyses: list[dict]):
    """Heatmap of C_ij for the run with largest Nm."""
    best_idx = max(range(len(runs)), key=lambda i: runs[i]["Nm"])
    run = runs[best_idx]
    ana = analyses[best_idx]

    C = ana["C"]
    K = ana["K"]

    fig, ax = plt.subplots(figsize=(9, 8))

    # Diverging colormap centred at 0
    vmax = max(abs(C[~np.eye(K, dtype=bool)].max()),
               abs(C[~np.eye(K, dtype=bool)].min()),
               0.1)

    im = ax.imshow(
        C, cmap="RdBu_r", vmin=-vmax, vmax=vmax,
        interpolation="nearest", origin="lower",
    )

    # Tick labels: mode indices 1..K
    ticks = np.arange(K)
    tick_labels = [str(k + 1) for k in range(K)]
    ax.set_xticks(ticks)
    ax.set_xticklabels(tick_labels, fontsize=7, rotation=45)
    ax.set_yticks(ticks)
    ax.set_yticklabels(tick_labels, fontsize=7)

    # Annotate diagonal and strong off-diagonal
    for i in range(K):
        for j in range(K):
            val = C[i, j]
            if i == j:
                ax.text(j, i, "1", ha="center", va="center",
                        fontsize=6, color="white", fontweight="bold")
            elif abs(val) > 0.5:
                ax.text(j, i, f"{val:.2f}", ha="center", va="center",
                        fontsize=5, color="white" if abs(val) > 0.7 else "black")

    cbar = fig.colorbar(im, ax=ax, label="Pearson correlation", pad=0.02,
                        shrink=0.85)
    cbar.ax.tick_params(labelsize=9)

    # Summary annotation
    ax.annotate(
        (f"mean off-diag = {ana['mean_corr']:.4f}\n"
         f"spectral radius = {ana['spectral_radius']:.4f}\n"
         f"cond number = {ana['cond_number']:.1f}"),
        xy=(0.02, 0.98), xycoords="axes fraction",
        fontsize=8, va="top",
        bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8),
    )

    setup_axes(
        ax,
        xlabel="Mode index $k$",
        ylabel="Mode index $k$",
        title=(f"Modal Energy Correlation -- D={run['D']}, A={run['A']}, "
               f"Nm={run['Nm']} ($K={K}$)"),
    )
    fig.tight_layout()

    fname = "correlation_matrix.png"
    fig.savefig(os.path.join(FIG_DIR, fname), dpi=300)
    plt.close(fig)
    print(f"  Saved: {fname}")


# ---------------------------------------------------------------------------
# Figure B: Attractor Correlation Profiles
# ---------------------------------------------------------------------------
def figure_correlation_profiles(runs: list[dict], analyses: list[dict]):
    """Mean row correlation (off-diagonal) for all runs."""
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

    max_K = max(ana["K"] for ana in analyses)

    fig, ax = plt.subplots(figsize=(12, 6))

    all_profiles = []

    for run, ana in zip(runs, analyses):
        K = ana["K"]
        profile = np.array(ana["mean_row_off"])
        k_axis = np.arange(1, K + 1)

        color = D_cmap(D_norm(run["D"]))
        marker = Nm_markers.get(run["Nm"], "o")

        ax.plot(
            k_axis, profile,
            color=color, marker=marker, markersize=3,
            linewidth=0.6, alpha=0.35,
        )

        padded = np.full(max_K, np.nan)
        padded[:K] = profile
        all_profiles.append(padded)

    # Mean profile
    if all_profiles:
        stacked = np.array(all_profiles)
        with np.errstate(all="ignore"):
            mean_profile = np.nanmean(stacked, axis=0)
        k_full = np.arange(1, max_K + 1)
        valid = ~np.isnan(mean_profile)

        ax.plot(
            k_full[valid], mean_profile[valid],
            color="black", marker="o", markersize=5,
            linewidth=2.5, alpha=0.9, zorder=10,
            label="Mean profile",
        )

    # Zero line
    ax.axhline(0.0, color="0.5", linestyle=":", linewidth=0.7, alpha=0.5)

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
    legend_handles.append(
        plt.Line2D([0], [0], color="black", marker="o", markersize=5,
                   linewidth=2.5, label="Mean profile")
    )
    ax.legend(handles=legend_handles, fontsize=8, loc="upper right",
              framealpha=0.9, title="Legend")

    setup_axes(
        ax,
        xlabel="Mode index $k$",
        ylabel="Mean off-diagonal correlation",
        title="Modal Correlation Profile -- All Admissible Runs",
    )
    fig.tight_layout()

    fname = "correlation_profiles.png"
    fig.savefig(os.path.join(FIG_DIR, fname), dpi=300)
    plt.close(fig)
    print(f"  Saved: {fname}")


# ---------------------------------------------------------------------------
# Figure C: Correlation Invariant Scatter
# ---------------------------------------------------------------------------
def figure_invariant_scatter(runs: list[dict], analyses: list[dict]):
    """Three panels: mean_corr, spectral_radius, cond_number vs D."""
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

    invariants = [
        ("mean_corr", "Mean off-diag corr", False),
        ("spectral_radius", "Spectral radius", False),
        ("cond_number", "Condition number", True),   # log scale
    ]

    fig, axes = plt.subplots(1, 3, figsize=(16, 5))

    for panel_idx, (key, title, use_log) in enumerate(invariants):
        ax = axes[panel_idx]

        all_vals = []

        for run, ana in zip(runs, analyses):
            val = ana[key]
            if np.isnan(val) or np.isinf(val):
                continue

            color = A_cmap(A_norm(run["A"]))
            marker = Nm_markers.get(run["Nm"], "o")

            ax.scatter(
                run["D"], val,
                color=color, marker=marker, s=50, alpha=0.7,
                edgecolors="0.3", linewidths=0.3,
            )
            all_vals.append(val)

        if all_vals:
            mean_v = np.mean(all_vals)
            ax.axhline(mean_v, color="0.4", linestyle="--",
                       linewidth=1.0, alpha=0.6)
            ax.annotate(
                rf"mean = {mean_v:.4f}",
                xy=(0.02, 0.95), xycoords="axes fraction",
                fontsize=9, color="0.3", va="top",
            )

        if use_log:
            ax.set_yscale("log")

        setup_axes(ax, r"Diffusion $D$", title,
                   title if panel_idx == 1 else "")

    # Global title
    fig.suptitle("Correlation Invariants vs Diffusion -- All Runs",
                 fontsize=14, fontweight="bold", y=1.02)

    # Colorbar
    sm = plt.cm.ScalarMappable(cmap=A_cmap, norm=A_norm)
    sm.set_array([])
    fig.colorbar(sm, ax=axes.tolist(), label=r"Amplitude $A$",
                 shrink=0.8, pad=0.03)

    # Marker legend on last panel
    legend_handles = [
        plt.Line2D([0], [0], marker=m, color="0.5", markersize=7,
                   linestyle="None", label=rf"$N_m = {Nm}$")
        for Nm, m in Nm_markers.items()
    ]
    axes[2].legend(handles=legend_handles, fontsize=7, loc="upper right",
                   framealpha=0.9, title="Seed count")

    fig.tight_layout()

    fname = "invariant_scatter.png"
    fig.savefig(os.path.join(FIG_DIR, fname), dpi=300, bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved: {fname}")


# ---------------------------------------------------------------------------
# Summary table and invariance verdict
# ---------------------------------------------------------------------------
def print_summary(runs: list[dict], analyses: list[dict]):
    print(f"\n{'='*110}")
    print("  Invariant Modal Correlations -- Summary Table")
    print(f"{'='*110}")

    print(f"  {'D':<7} {'A':<7} {'Nm':<5} {'K':<4} "
          f"{'mean_corr':<12} {'max_corr':<12} {'min_corr':<12} "
          f"{'spec_rad':<12} {'cond_num':<12}")
    print("  " + "-" * 90)

    inv_names = ["mean_corr", "max_corr", "min_corr",
                 "spectral_radius", "cond_number"]
    all_inv = {name: [] for name in inv_names}

    for run, ana in zip(runs, analyses):
        cond_str = (f"{ana['cond_number']:<12.2f}"
                    if not np.isinf(ana["cond_number"])
                    else f"{'inf':<12}")

        print(f"  {run['D']:<7.3f} {run['A']:<7.4f} {run['Nm']:<5d} "
              f"{ana['K']:<4d} "
              f"{ana['mean_corr']:<12.6f} "
              f"{ana['max_corr']:<12.6f} "
              f"{ana['min_corr']:<12.6f} "
              f"{ana['spectral_radius']:<12.6f} "
              f"{cond_str}")

        for name in inv_names:
            val = ana[name]
            if not np.isnan(val) and not np.isinf(val):
                all_inv[name].append(val)

    # Global statistics
    print(f"\n  {'Invariant':<16} {'Mean':<14} {'Std':<14} "
          f"{'Min':<14} {'Max':<14} {'CV':<10} {'Verdict'}")
    print("  " + "-" * 88)

    for name in inv_names:
        arr = np.array(all_inv[name])
        if len(arr) == 0:
            print(f"  {name:<16} (no data)")
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

        print(f"  {name:<16} "
              f"{mean_v:<14.6f} {std_v:<14.6f} "
              f"{np.min(arr):<14.6f} {np.max(arr):<14.6f} "
              f"{cv:<10.4f} {verdict}")


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

    # Analyse all runs
    print(f"\nComputing modal correlation matrices (K <= {K_MAX})...")
    analyses = []
    for i, run in enumerate(runs):
        ana = analyse_run(run)
        analyses.append(ana)
        if (i + 1) % 10 == 0 or i == len(runs) - 1:
            print(f"  [{i+1}/{len(runs)}] {run['name']}: "
                  f"K={ana['K']}, mean_corr={ana['mean_corr']:.4f}, "
                  f"spec_rad={ana['spectral_radius']:.4f}")

    # Figures
    print("\n--- (A) Correlation Matrix ---")
    figure_correlation_matrix(runs, analyses)

    print("\n--- (B) Correlation Profiles ---")
    figure_correlation_profiles(runs, analyses)

    print("\n--- (C) Invariant Scatter ---")
    figure_invariant_scatter(runs, analyses)

    # Summary
    print_summary(runs, analyses)

    print(f"\nAll figures saved to: {FIG_DIR}")
    print("Done.")


if __name__ == "__main__":
    main()
