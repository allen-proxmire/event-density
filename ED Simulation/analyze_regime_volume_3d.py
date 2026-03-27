"""
analyze_regime_volume_3d.py
============================
Post-processing script for the 3D Regime Volume experiment (Atlas §8.5,
Suite §4.1).

Loads all regime_D*_A*_Nm* runs and produces:

  (A) 3D regime scatter — axes (D, A, N_m), color by regime, size by peak
      active modes.
  (B) Regime slices — fix one axis, show the 2D regime map of the other two.
  (C) Decay-rate tensor — sigma(D, A, N_m) as heatmaps per N_m.
  (D) Cascade-breadth tensor — peak_active(D, A, N_m) as heatmaps per N_m.

All figures saved to output/figures/regime_volume_3d/ as PNG (300 dpi).

Usage:
    python analyze_regime_volume_3d.py

Requires: numpy, matplotlib.
"""

import os
import re
import sys
import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from mpl_toolkits.mplot3d import Axes3D

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
RUNS_DIR = os.path.join(SCRIPT_DIR, "output", "runs")
FIG_DIR = os.path.join(SCRIPT_DIR, "output", "figures", "regime_volume_3d")

RE_RUN = re.compile(r"^regime_D.+_A.+_Nm\d+$")

ACTIVATION_FRAC = 1e-4

# Regime visual encoding (shared with 2D analysis)
REGIME_COLORS = {
    "underdamped":           "#2166ac",
    "underdamped_weak":      "#92c5de",
    "oscillatory":           "#4393c3",
    "critical":              "#f4a582",
    "overdamped":            "#b2182b",
    "transient_oscillatory": "#762a83",
    "inadmissible":          "#333333",
    "unknown":               "#cccccc",
}
REGIME_MARKERS = {
    "underdamped":           "o",
    "underdamped_weak":      "o",
    "oscillatory":           "o",
    "critical":              "D",
    "overdamped":            "s",
    "transient_oscillatory": "^",
    "inadmissible":          "X",
    "unknown":               ".",
}
REGIME_ORDER = [
    "underdamped", "underdamped_weak", "oscillatory",
    "critical", "overdamped", "transient_oscillatory",
    "inadmissible",
]
REGIME_ABBREV = {
    "underdamped": "UD", "underdamped_weak": "UDw",
    "oscillatory": "OSC", "critical": "CR",
    "overdamped": "OD", "transient_oscillatory": "tOSC",
    "inadmissible": "INAD", "unknown": "?",
}


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------
def load_run(run_dir: str) -> dict | None:
    ts_path = os.path.join(run_dir, "time_series.npz")
    meta_path = os.path.join(run_dir, "metadata.json")
    if not os.path.isfile(ts_path):
        # May be a pre-skipped point with only metadata
        if os.path.isfile(meta_path):
            with open(meta_path, "r") as f:
                meta = json.load(f)
            return {"metadata": meta}
        return None
    ts = dict(np.load(ts_path, allow_pickle=True))
    meta = {}
    if os.path.isfile(meta_path):
        with open(meta_path, "r") as f:
            meta = json.load(f)
    ts["metadata"] = meta
    return ts


def discover_runs() -> dict:
    """Discover all regime_D*_A*_Nm* runs. Key = (D, A, Nm)."""
    runs = {}
    if not os.path.isdir(RUNS_DIR):
        print(f"ERROR: runs directory not found: {RUNS_DIR}")
        sys.exit(1)
    for name in sorted(os.listdir(RUNS_DIR)):
        if not RE_RUN.match(name):
            continue
        run_dir = os.path.join(RUNS_DIR, name)
        if not os.path.isdir(run_dir):
            continue
        data = load_run(run_dir)
        if data is None:
            continue
        meta = data["metadata"]
        D = meta.get("D")
        A = meta.get("A_per_mode")
        Nm = meta.get("Nm")
        if D is not None and A is not None and Nm is not None:
            runs[(D, A, int(Nm))] = {"dir": run_dir, "name": name, "data": data}
    return runs


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def setup_axes(ax, xlabel: str, ylabel: str, title: str):
    ax.set_xlabel(xlabel, fontsize=11)
    ax.set_ylabel(ylabel, fontsize=11)
    ax.set_title(title, fontsize=13, fontweight="bold")
    ax.tick_params(labelsize=10)
    ax.grid(True, alpha=0.3, linewidth=0.5)


def fit_energy_decay_rate(t: np.ndarray, E: np.ndarray) -> tuple:
    """Fit E ~ C * exp(-sigma * t) in the last half. Returns (sigma, R2)."""
    n = len(t)
    half = n // 2
    t_fit = t[half:]
    E_fit = np.abs(E[half:])
    mask = E_fit > 1e-30
    if np.sum(mask) < 10:
        return 0.0, 0.0
    t_m = t_fit[mask]
    log_E = np.log(E_fit[mask])
    try:
        coeffs = np.polyfit(t_m, log_E, 1)
        sigma = -coeffs[0]
        predicted = coeffs[0] * t_m + coeffs[1]
        ss_res = np.sum((log_E - predicted) ** 2)
        ss_tot = np.sum((log_E - np.mean(log_E)) ** 2)
        R2 = 1.0 - ss_res / max(ss_tot, 1e-30)
        return sigma, R2
    except (np.linalg.LinAlgError, ValueError):
        return 0.0, 0.0


def peak_active_modes(ts: dict) -> int:
    modal = ts.get("modal_amplitudes")
    if modal is None or not hasattr(modal, "ndim") or modal.ndim != 2:
        return 0
    A_pm = ts["metadata"].get("A_per_mode", 0.02)
    thresh = ACTIVATION_FRAC * A_pm ** 2
    count = np.sum(np.abs(modal) > thresh, axis=1)
    return int(np.max(count)) if len(count) > 0 else 0


# ---------------------------------------------------------------------------
# Pre-compute sweep data
# ---------------------------------------------------------------------------
def compute_sweep_data(runs: dict) -> dict:
    data = {}
    for (D, A, Nm), run in sorted(runs.items()):
        ts = run["data"]
        meta = ts["metadata"]

        # Some runs may be pre-skipped (no time_series)
        has_ts = "t" in ts and "E_total" in ts

        sigma, R2 = 0.0, 0.0
        peak = 0
        E0, ET = 0.0, 0.0

        if has_ts:
            t = ts["t"]
            E = ts["E_total"]
            n_e = min(len(t), len(E))
            sigma, R2 = fit_energy_decay_rate(t[:n_e], E[:n_e])
            peak = peak_active_modes(ts)
            E0 = E[0] if len(E) > 0 else 0
            ET = E[-1] if len(E) > 0 else 0

        data[(D, A, Nm)] = {
            "D": D, "A": A, "Nm": Nm,
            "Delta": meta.get("discriminant_Delta", 0),
            "linear_regime": meta.get("linear_regime", "unknown"),
            "effective_regime": meta.get("effective_regime", "unknown"),
            "inadmissible": meta.get("inadmissible", False),
            "sigma": sigma, "R2": R2,
            "peak_active": peak,
            "E0": E0, "ET": ET,
            "n_sign_changes": meta.get("n_sign_changes", 0),
            "has_ts": has_ts,
        }
    return data


# ---------------------------------------------------------------------------
# Figure A: 3D regime scatter
# ---------------------------------------------------------------------------
def figure_3d_scatter(sweep_data: dict):
    fig = plt.figure(figsize=(11, 9))
    ax = fig.add_subplot(111, projection="3d")

    plotted_regimes = set()

    for (D, A, Nm), d in sorted(sweep_data.items()):
        regime = d["effective_regime"]
        color = REGIME_COLORS.get(regime, "#cccccc")
        marker = REGIME_MARKERS.get(regime, "o")
        # Size proportional to peak active modes (min 30, max 300)
        size = max(30, min(300, 5 * d["peak_active"])) if d["peak_active"] > 0 else 30

        ax.scatter(
            D, A, Nm,
            c=color, marker=marker, s=size,
            edgecolors="white", linewidths=0.6, alpha=0.85,
            zorder=5,
        )
        plotted_regimes.add(regime)

    # Legend (flat scatter for legend only)
    legend_handles = []
    for regime in REGIME_ORDER:
        if regime in plotted_regimes:
            legend_handles.append(
                plt.Line2D([0], [0], marker=REGIME_MARKERS[regime],
                           color="w", markerfacecolor=REGIME_COLORS[regime],
                           markersize=8, label=regime.replace("_", " "),
                           markeredgecolor="white", markeredgewidth=0.5)
            )

    ax.legend(handles=legend_handles, fontsize=8, loc="upper left",
              title="Effective Regime", title_fontsize=9, framealpha=0.9)

    ax.set_xlabel(r"$D$", fontsize=11, labelpad=8)
    ax.set_ylabel(r"$A$", fontsize=11, labelpad=8)
    ax.set_zlabel(r"$N_m$", fontsize=11, labelpad=8)
    ax.set_title("3D Regime Volume — $(D, A, N_m)$",
                 fontsize=14, fontweight="bold", pad=15)
    ax.tick_params(labelsize=8)

    # Viewing angle
    ax.view_init(elev=25, azim=135)

    fig.tight_layout()
    fig.savefig(os.path.join(FIG_DIR, "regime_scatter_3d.png"), dpi=300)
    plt.close(fig)
    print("  Saved: regime_scatter_3d.png")


# ---------------------------------------------------------------------------
# Figure B: Regime slices
# ---------------------------------------------------------------------------
def _plot_2d_regime_slice(ax, x_vals, y_vals, data_grid, xlabel, ylabel, title):
    """Plot a 2D regime scatter from a dict keyed by (x, y) -> regime."""
    plotted = set()
    for (x, y), regime in data_grid.items():
        color = REGIME_COLORS.get(regime, "#cccccc")
        marker = REGIME_MARKERS.get(regime, "o")
        ax.scatter(x, y, c=color, marker=marker, s=140,
                   edgecolors="white", linewidths=0.8, zorder=5)
        plotted.add(regime)
    setup_axes(ax, xlabel, ylabel, title)
    return plotted


def figure_regime_slices(sweep_data: dict):
    D_vals = sorted(set(d["D"] for d in sweep_data.values()))
    A_vals = sorted(set(d["A"] for d in sweep_data.values()))
    Nm_vals = sorted(set(d["Nm"] for d in sweep_data.values()))

    # --- B1: Fix Nm, plot (D, A) for each Nm ---
    n_Nm = len(Nm_vals)
    fig1, axes1 = plt.subplots(1, n_Nm, figsize=(4.5 * n_Nm, 4.5), squeeze=False)
    axes1 = axes1.flatten()

    all_regimes = set()
    for idx, Nm in enumerate(Nm_vals):
        grid = {}
        for (D, A, nm), d in sweep_data.items():
            if nm == Nm:
                grid[(D, A)] = d["effective_regime"]
        plotted = _plot_2d_regime_slice(
            axes1[idx], D_vals, A_vals, grid,
            r"$D$", r"$A$" if idx == 0 else "",
            f"$N_m = {Nm}$",
        )
        all_regimes |= plotted
        if idx > 0:
            axes1[idx].set_yticklabels([])

    # Shared legend
    handles = [plt.Line2D([0], [0], marker=REGIME_MARKERS[r], color="w",
               markerfacecolor=REGIME_COLORS[r], markersize=8,
               label=r.replace("_", " "), markeredgecolor="white")
               for r in REGIME_ORDER if r in all_regimes]
    fig1.legend(handles=handles, loc="upper center", ncol=min(len(handles), 6),
                fontsize=8, framealpha=0.9, bbox_to_anchor=(0.5, 1.05))
    fig1.suptitle("Regime Slices: Fix $N_m$, vary $(D, A)$",
                  fontsize=14, fontweight="bold", y=1.09)
    fig1.tight_layout()
    fig1.savefig(os.path.join(FIG_DIR, "slice_fix_Nm.png"),
                 dpi=300, bbox_inches="tight")
    plt.close(fig1)
    print("  Saved: slice_fix_Nm.png")

    # --- B2: Fix A, plot (D, Nm) for each A ---
    n_A = len(A_vals)
    fig2, axes2 = plt.subplots(1, n_A, figsize=(4.5 * n_A, 4.5), squeeze=False)
    axes2 = axes2.flatten()

    all_regimes = set()
    for idx, A_val in enumerate(A_vals):
        grid = {}
        for (D, A, Nm), d in sweep_data.items():
            if A == A_val:
                grid[(D, Nm)] = d["effective_regime"]
        plotted = _plot_2d_regime_slice(
            axes2[idx], D_vals, Nm_vals, grid,
            r"$D$", r"$N_m$" if idx == 0 else "",
            f"$A = {A_val}$",
        )
        all_regimes |= plotted
        if idx > 0:
            axes2[idx].set_yticklabels([])

    handles = [plt.Line2D([0], [0], marker=REGIME_MARKERS[r], color="w",
               markerfacecolor=REGIME_COLORS[r], markersize=8,
               label=r.replace("_", " "), markeredgecolor="white")
               for r in REGIME_ORDER if r in all_regimes]
    fig2.legend(handles=handles, loc="upper center", ncol=min(len(handles), 6),
                fontsize=8, framealpha=0.9, bbox_to_anchor=(0.5, 1.05))
    fig2.suptitle("Regime Slices: Fix $A$, vary $(D, N_m)$",
                  fontsize=14, fontweight="bold", y=1.09)
    fig2.tight_layout()
    fig2.savefig(os.path.join(FIG_DIR, "slice_fix_A.png"),
                 dpi=300, bbox_inches="tight")
    plt.close(fig2)
    print("  Saved: slice_fix_A.png")

    # --- B3: Fix D, plot (A, Nm) for each D ---
    n_D = len(D_vals)
    fig3, axes3 = plt.subplots(1, n_D, figsize=(4.5 * n_D, 4.5), squeeze=False)
    axes3 = axes3.flatten()

    all_regimes = set()
    for idx, D_val in enumerate(D_vals):
        grid = {}
        for (D, A, Nm), d in sweep_data.items():
            if D == D_val:
                grid[(A, Nm)] = d["effective_regime"]
        Delta = None
        for d in sweep_data.values():
            if d["D"] == D_val:
                Delta = d["Delta"]
                break
        plotted = _plot_2d_regime_slice(
            axes3[idx], A_vals, Nm_vals, grid,
            r"$A$", r"$N_m$" if idx == 0 else "",
            f"$D = {D_val}$" + (f"\n$\\Delta = {Delta:.2f}$" if Delta else ""),
        )
        all_regimes |= plotted
        if idx > 0:
            axes3[idx].set_yticklabels([])

    handles = [plt.Line2D([0], [0], marker=REGIME_MARKERS[r], color="w",
               markerfacecolor=REGIME_COLORS[r], markersize=8,
               label=r.replace("_", " "), markeredgecolor="white")
               for r in REGIME_ORDER if r in all_regimes]
    fig3.legend(handles=handles, loc="upper center", ncol=min(len(handles), 6),
                fontsize=8, framealpha=0.9, bbox_to_anchor=(0.5, 1.05))
    fig3.suptitle("Regime Slices: Fix $D$, vary $(A, N_m)$",
                  fontsize=14, fontweight="bold", y=1.09)
    fig3.tight_layout()
    fig3.savefig(os.path.join(FIG_DIR, "slice_fix_D.png"),
                 dpi=300, bbox_inches="tight")
    plt.close(fig3)
    print("  Saved: slice_fix_D.png")


# ---------------------------------------------------------------------------
# Figure C: Decay-rate tensor — heatmaps per Nm
# ---------------------------------------------------------------------------
def figure_decay_rate_tensor(sweep_data: dict):
    D_vals = sorted(set(d["D"] for d in sweep_data.values()))
    A_vals = sorted(set(d["A"] for d in sweep_data.values()))
    Nm_vals = sorted(set(d["Nm"] for d in sweep_data.values()))

    n_Nm = len(Nm_vals)
    fig, axes = plt.subplots(1, n_Nm, figsize=(4.8 * n_Nm, 4.5), squeeze=False)
    axes = axes.flatten()

    # Collect all valid sigmas for a shared color scale
    all_sigma = [d["sigma"] for d in sweep_data.values()
                 if d["sigma"] > 0 and not d["inadmissible"]]
    if not all_sigma:
        print("  SKIP: no valid decay rates.")
        plt.close(fig)
        return

    vmin = max(min(all_sigma), 1e-6)
    vmax = max(all_sigma)

    for idx, Nm in enumerate(Nm_vals):
        ax = axes[idx]
        grid = np.full((len(A_vals), len(D_vals)), np.nan)

        for (D, A, nm), d in sweep_data.items():
            if nm != Nm:
                continue
            if d["sigma"] > 0 and not d["inadmissible"]:
                i_D = D_vals.index(D)
                i_A = A_vals.index(A)
                grid[i_A, i_D] = d["sigma"]

        im = ax.pcolormesh(
            D_vals, A_vals,
            np.ma.masked_invalid(grid),
            cmap="YlOrRd",
            norm=mcolors.LogNorm(vmin=vmin, vmax=vmax),
            shading="nearest",
        )

        # Annotate values
        for (D, A, nm), d in sweep_data.items():
            if nm != Nm:
                continue
            if d["inadmissible"]:
                ax.plot(D, A, "X", color="black", markersize=8, zorder=5)
            elif d["sigma"] > 0:
                ax.text(D, A, f"{d['sigma']:.2f}",
                        ha="center", va="center", fontsize=6,
                        color="black" if d["sigma"] < 0.5 * vmax else "white",
                        fontweight="bold")

        ax.set_title(f"$N_m = {Nm}$", fontsize=11)
        ax.set_xlabel(r"$D$", fontsize=10)
        if idx == 0:
            ax.set_ylabel(r"$A$", fontsize=10)
        ax.tick_params(labelsize=8)

    # Shared colorbar
    cbar = fig.colorbar(im, ax=axes.tolist(), label=r"Decay rate $\sigma$",
                        pad=0.02, shrink=0.85)
    cbar.ax.tick_params(labelsize=8)

    fig.suptitle(r"Decay-Rate Tensor $\sigma(D, A, N_m)$",
                 fontsize=14, fontweight="bold", y=1.02)
    fig.tight_layout()
    fig.savefig(os.path.join(FIG_DIR, "decay_rate_tensor.png"),
                dpi=300, bbox_inches="tight")
    plt.close(fig)
    print("  Saved: decay_rate_tensor.png")


# ---------------------------------------------------------------------------
# Figure D: Cascade-breadth tensor — heatmaps per Nm
# ---------------------------------------------------------------------------
def figure_cascade_breadth_tensor(sweep_data: dict):
    D_vals = sorted(set(d["D"] for d in sweep_data.values()))
    A_vals = sorted(set(d["A"] for d in sweep_data.values()))
    Nm_vals = sorted(set(d["Nm"] for d in sweep_data.values()))

    n_Nm = len(Nm_vals)
    fig, axes = plt.subplots(1, n_Nm, figsize=(4.8 * n_Nm, 4.5), squeeze=False)
    axes = axes.flatten()

    all_peaks = [d["peak_active"] for d in sweep_data.values()
                 if d["peak_active"] > 0 and not d["inadmissible"]]
    if not all_peaks:
        print("  SKIP: no valid peak-active data.")
        plt.close(fig)
        return

    vmax_global = max(all_peaks)

    for idx, Nm in enumerate(Nm_vals):
        ax = axes[idx]
        grid = np.full((len(A_vals), len(D_vals)), np.nan)

        for (D, A, nm), d in sweep_data.items():
            if nm != Nm:
                continue
            if not d["inadmissible"]:
                i_D = D_vals.index(D)
                i_A = A_vals.index(A)
                grid[i_A, i_D] = d["peak_active"]

        im = ax.pcolormesh(
            D_vals, A_vals,
            np.ma.masked_invalid(grid),
            cmap="viridis",
            vmin=0, vmax=vmax_global,
            shading="nearest",
        )

        # Annotate
        for (D, A, nm), d in sweep_data.items():
            if nm != Nm:
                continue
            if d["inadmissible"]:
                ax.plot(D, A, "X", color="red", markersize=8, zorder=5)
            elif d["peak_active"] > 0:
                ax.text(D, A, str(d["peak_active"]),
                        ha="center", va="center", fontsize=6,
                        color="white" if d["peak_active"] > 0.55 * vmax_global
                        else "black",
                        fontweight="bold")

        ax.set_title(f"$N_m = {Nm}$", fontsize=11)
        ax.set_xlabel(r"$D$", fontsize=10)
        if idx == 0:
            ax.set_ylabel(r"$A$", fontsize=10)
        ax.tick_params(labelsize=8)

    cbar = fig.colorbar(im, ax=axes.tolist(), label="Peak active modes",
                        pad=0.02, shrink=0.85)
    cbar.ax.tick_params(labelsize=8)

    fig.suptitle("Cascade-Breadth Tensor — Peak Active Modes",
                 fontsize=14, fontweight="bold", y=1.02)
    fig.tight_layout()
    fig.savefig(os.path.join(FIG_DIR, "cascade_breadth_tensor.png"),
                dpi=300, bbox_inches="tight")
    plt.close(fig)
    print("  Saved: cascade_breadth_tensor.png")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    os.makedirs(FIG_DIR, exist_ok=True)

    print("Discovering 3D regime-volume runs...")
    runs = discover_runs()

    if not runs:
        print(f"\nERROR: No regime_D*_A*_Nm* runs found in:")
        print(f"  {RUNS_DIR}")
        print("\nRun the experiment first:")
        print("  python experiments/regime_volume_3d.py")
        sys.exit(1)

    keys = sorted(runs.keys())
    D_vals = sorted(set(k[0] for k in keys))
    A_vals = sorted(set(k[1] for k in keys))
    Nm_vals = sorted(set(k[2] for k in keys))
    print(f"  Found {len(runs)} runs")
    print(f"  D  grid: {D_vals}")
    print(f"  A  grid: {A_vals}")
    print(f"  Nm grid: {Nm_vals}")

    # Pre-compute
    print("\nComputing sweep data...")
    sweep_data = compute_sweep_data(runs)

    # --- (A) 3D scatter ---
    print("\n--- (A) 3D Regime Scatter ---")
    figure_3d_scatter(sweep_data)

    # --- (B) Regime slices ---
    print("\n--- (B) Regime Slices ---")
    figure_regime_slices(sweep_data)

    # --- (C) Decay-rate tensor ---
    print("\n--- (C) Decay-Rate Tensor ---")
    figure_decay_rate_tensor(sweep_data)

    # --- (D) Cascade-breadth tensor ---
    print("\n--- (D) Cascade-Breadth Tensor ---")
    figure_cascade_breadth_tensor(sweep_data)

    # --- Summary table ---
    print(f"\n{'='*125}")
    print("  3D Regime Volume — Full Summary")
    print(f"{'='*125}")
    print(f"  {'D':<7} {'A':<7} {'Nm':<5} {'Delta':<9} "
          f"{'Regime':<18} {'sigma':<12} {'R^2':<8} "
          f"{'Peak':<7} {'E(0)':<14} {'E(T)':<14} {'Signs':<6}")
    print("  " + "-" * 120)

    for key in sorted(sweep_data.keys()):
        d = sweep_data[key]
        regime = d["effective_regime"][:16]
        print(f"  {d['D']:<7.3f} {d['A']:<7.4f} {d['Nm']:<5} "
              f"{d['Delta']:<9.4f} {regime:<18} "
              f"{d['sigma']:<12.6f} {d['R2']:<8.4f} "
              f"{d['peak_active']:<7} {d['E0']:<14.6e} "
              f"{d['ET']:<14.6e} {d['n_sign_changes']:<6}")

    # --- Compact grids per Nm ---
    for Nm in Nm_vals:
        print(f"\n  --- Compact Grid: Nm = {Nm} ---")
        header = f"  {'D \\ A':<10}"
        for A_val in A_vals:
            header += f" {A_val:<8}"
        print(header)
        print("  " + "-" * (10 + 9 * len(A_vals)))

        for D_val in D_vals:
            row = f"  {D_val:<10.3f}"
            for A_val in A_vals:
                d = sweep_data.get((D_val, A_val, Nm))
                if d is None:
                    row += f" {'--':<8}"
                else:
                    short = REGIME_ABBREV.get(d["effective_regime"], "?")
                    row += f" {short:<8}"
            print(row)

    # --- Global statistics ---
    regime_counts = {}
    n_inad = 0
    for d in sweep_data.values():
        r = d["effective_regime"]
        regime_counts[r] = regime_counts.get(r, 0) + 1
        if d["inadmissible"]:
            n_inad += 1

    print(f"\n  Global Statistics:")
    print(f"    Total points:    {len(sweep_data)}")
    print(f"    Admissible:      {len(sweep_data) - n_inad}")
    print(f"    Inadmissible:    {n_inad}")
    print(f"\n  Regime distribution:")
    for r in REGIME_ORDER:
        if r in regime_counts:
            print(f"    {r:<24}: {regime_counts[r]}")

    # Sigma statistics
    sigmas = [d["sigma"] for d in sweep_data.values()
              if d["sigma"] > 0 and not d["inadmissible"]]
    if sigmas:
        print(f"\n  Decay-rate statistics (admissible, sigma > 0):")
        print(f"    n:     {len(sigmas)}")
        print(f"    min:   {min(sigmas):.6f}")
        print(f"    max:   {max(sigmas):.6f}")
        print(f"    mean:  {np.mean(sigmas):.6f}")
        print(f"    stdev: {np.std(sigmas):.6f}")

    # Scaling: sigma vs D (averaged over A, Nm)
    print(f"\n  Scaling: mean sigma vs D (averaged over A, Nm):")
    for D_val in D_vals:
        s_at_D = [d["sigma"] for d in sweep_data.values()
                  if d["D"] == D_val and d["sigma"] > 0
                  and not d["inadmissible"]]
        if s_at_D:
            print(f"    D={D_val:<6.3f}  mean_sigma={np.mean(s_at_D):.6f}  "
                  f"n={len(s_at_D)}")

    # Scaling: peak_active vs Nm (averaged over D, A)
    print(f"\n  Scaling: mean peak_active vs Nm (averaged over D, A):")
    for Nm in Nm_vals:
        p_at_Nm = [d["peak_active"] for d in sweep_data.values()
                   if d["Nm"] == Nm and d["peak_active"] > 0
                   and not d["inadmissible"]]
        if p_at_Nm:
            print(f"    Nm={Nm:<4}  mean_peak={np.mean(p_at_Nm):.1f}  "
                  f"n={len(p_at_Nm)}")

    print(f"\nAll figures saved to: {FIG_DIR}")
    print("Done.")


if __name__ == "__main__":
    main()
