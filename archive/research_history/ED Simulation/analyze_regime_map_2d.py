"""
analyze_regime_map_2d.py
=========================
Post-processing script for the 2D Regime Map experiment (Atlas §8.5,
Suite §4.1).

Loads all regime_D*_A* runs and produces:

  (A) 2D regime map -- scatter in (D, A) colored by effective regime.
  (B) Decay-rate surface -- sigma(D, A) as a filled contour / heatmap.
  (C) Peak-active-modes surface -- peak_active(D, A) as a heatmap.
  (D) Representative modal funnels -- |a_k(t)| for selected (D, A) pairs.

All figures saved to output/figures/regime_map_2d/ as PNG (300 dpi).

Usage:
    python analyze_regime_map_2d.py

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
from matplotlib.patches import Patch

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
RUNS_DIR = os.path.join(SCRIPT_DIR, "output", "runs")
FIG_DIR = os.path.join(SCRIPT_DIR, "output", "figures", "regime_map_2d")

RE_RUN = re.compile(r"^regime_D.+_A.+$")

# Activation threshold
ACTIVATION_FRAC = 1e-4

# Regime visual encoding
REGIME_COLORS = {
    "underdamped":           "#2166ac",   # blue
    "underdamped_weak":      "#92c5de",   # light blue
    "oscillatory":           "#4393c3",   # medium blue
    "critical":              "#f4a582",   # orange
    "overdamped":            "#b2182b",   # red
    "transient_oscillatory": "#762a83",   # purple
    "inadmissible":          "#333333",   # dark grey
    "unknown":               "#cccccc",   # light grey
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
    "critical",
    "overdamped", "transient_oscillatory",
    "inadmissible",
]


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------
def load_run(run_dir: str) -> dict | None:
    ts_path = os.path.join(run_dir, "time_series.npz")
    meta_path = os.path.join(run_dir, "metadata.json")
    if not os.path.isfile(ts_path):
        return None
    ts = dict(np.load(ts_path, allow_pickle=True))
    meta = {}
    if os.path.isfile(meta_path):
        with open(meta_path, "r") as f:
            meta = json.load(f)
    ts["metadata"] = meta
    return ts


def discover_runs() -> dict:
    """Discover all regime_D*_A* runs. Key = (D, A) tuple."""
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
        if D is not None and A is not None:
            runs[(D, A)] = {"dir": run_dir, "name": name, "data": data}
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
    if modal is None or modal.ndim != 2:
        return 0
    A_pm = ts["metadata"].get("A_per_mode", 0.02)
    thresh = ACTIVATION_FRAC * A_pm ** 2
    count = np.sum(np.abs(modal) > thresh, axis=1)
    return int(np.max(count)) if len(count) > 0 else 0


# ---------------------------------------------------------------------------
# Pre-compute sweep data
# ---------------------------------------------------------------------------
def compute_sweep_data(runs: dict) -> dict:
    """Extract summary quantities for every (D, A) point."""
    data = {}
    for (D, A), run in sorted(runs.items()):
        ts = run["data"]
        meta = ts["metadata"]
        t = ts["t"]
        E = ts["E_total"]
        n_e = min(len(t), len(E))

        sigma, R2 = fit_energy_decay_rate(t[:n_e], E[:n_e])
        peak = peak_active_modes(ts)

        data[(D, A)] = {
            "D": D,
            "A": A,
            "Delta": meta.get("discriminant_Delta", 0),
            "linear_regime": meta.get("linear_regime", "unknown"),
            "effective_regime": meta.get("effective_regime", "unknown"),
            "inadmissible": meta.get("inadmissible", False),
            "sigma": sigma,
            "R2": R2,
            "peak_active": peak,
            "E0": E[0] if len(E) > 0 else 0,
            "ET": E[-1] if len(E) > 0 else 0,
            "n_sign_changes": meta.get("n_sign_changes", 0),
        }
    return data


# ---------------------------------------------------------------------------
# Figure A: 2D regime map
# ---------------------------------------------------------------------------
def figure_regime_map(sweep_data: dict):
    fig, ax = plt.subplots(figsize=(9, 7))

    # Plot each point
    plotted_regimes = set()
    for (D, A), d in sorted(sweep_data.items()):
        regime = d["effective_regime"]
        color = REGIME_COLORS.get(regime, "#cccccc")
        marker = REGIME_MARKERS.get(regime, "o")

        ax.scatter(
            D, A,
            c=color, marker=marker, s=180,
            edgecolors="white", linewidths=1.0, zorder=5,
        )
        plotted_regimes.add(regime)

    # Legend
    legend_handles = []
    for regime in REGIME_ORDER:
        if regime in plotted_regimes:
            legend_handles.append(
                plt.scatter([], [],
                            c=REGIME_COLORS[regime],
                            marker=REGIME_MARKERS[regime],
                            s=80, edgecolors="white", linewidths=0.8,
                            label=regime.replace("_", " "))
            )

    ax.legend(
        handles=legend_handles,
        fontsize=9, loc="upper right", framealpha=0.9,
        title="Effective Regime", title_fontsize=10,
    )

    # Delta = 1 contour (vertical line since Delta depends only on D)
    # Find D_crit where Delta crosses 1
    D_vals_unique = sorted(set(d["D"] for d in sweep_data.values()))
    Deltas_unique = []
    for D_val in D_vals_unique:
        # Get Delta for any A at this D (it's independent of A)
        for key, d in sweep_data.items():
            if d["D"] == D_val:
                Deltas_unique.append(d["Delta"])
                break

    for i in range(len(D_vals_unique) - 1):
        if (Deltas_unique[i] - 1.0) * (Deltas_unique[i + 1] - 1.0) < 0:
            D_crit = D_vals_unique[i] + (1.0 - Deltas_unique[i]) / (
                Deltas_unique[i + 1] - Deltas_unique[i]) * (
                D_vals_unique[i + 1] - D_vals_unique[i])
            ax.axvline(
                D_crit, color="#d6604d", linestyle=":", linewidth=2.0,
                alpha=0.6, label=f"$\\Delta = 1$ ($D \\approx {D_crit:.3f}$)",
                zorder=3,
            )
            # Re-create legend with this line
            legend_handles.append(
                plt.Line2D([0], [0], color="#d6604d", linestyle=":",
                           linewidth=2.0, label=f"$\\Delta = 1$ ($D \\approx {D_crit:.3f}$)")
            )
            ax.legend(handles=legend_handles, fontsize=9, loc="upper right",
                      framealpha=0.9, title="Effective Regime", title_fontsize=10)
            break

    setup_axes(ax, r"Diffusion coefficient $D$",
               r"Perturbation amplitude $A$",
               "2D Regime Map -- $(D, A)$ Plane")
    ax.set_xscale("log")
    ax.set_yscale("log")
    fig.tight_layout()
    fig.savefig(os.path.join(FIG_DIR, "regime_map_2d.png"), dpi=300)
    plt.close(fig)
    print("  Saved: regime_map_2d.png")


# ---------------------------------------------------------------------------
# Figure B: Decay-rate surface sigma(D, A)
# ---------------------------------------------------------------------------
def figure_decay_rate_surface(sweep_data: dict):
    D_vals = sorted(set(d["D"] for d in sweep_data.values()))
    A_vals = sorted(set(d["A"] for d in sweep_data.values()))
    n_D = len(D_vals)
    n_A = len(A_vals)

    sigma_grid = np.full((n_A, n_D), np.nan)
    for (D, A), d in sweep_data.items():
        i_D = D_vals.index(D)
        i_A = A_vals.index(A)
        if d["sigma"] > 0 and not d["inadmissible"]:
            sigma_grid[i_A, i_D] = d["sigma"]

    fig, ax = plt.subplots(figsize=(9, 6))

    # Use log scale for sigma via LogNorm
    valid = sigma_grid[np.isfinite(sigma_grid) & (sigma_grid > 0)]
    if len(valid) == 0:
        ax.text(0.5, 0.5, "No valid decay rates", ha="center", va="center",
                transform=ax.transAxes, fontsize=14, color="0.5")
        setup_axes(ax, "$D$", "$A$", "Decay Rate Surface")
        fig.tight_layout()
        fig.savefig(os.path.join(FIG_DIR, "decay_rate_surface.png"), dpi=300)
        plt.close(fig)
        return

    vmin = max(valid.min(), 1e-6)
    vmax = valid.max()

    im = ax.pcolormesh(
        D_vals, A_vals,
        np.ma.masked_invalid(sigma_grid),
        cmap="YlOrRd",
        norm=mcolors.LogNorm(vmin=vmin, vmax=vmax),
        shading="nearest",
    )
    cbar = fig.colorbar(im, ax=ax, label=r"Decay rate $\sigma$", pad=0.02)
    cbar.ax.tick_params(labelsize=9)

    # Mark inadmissible points
    for (D, A), d in sweep_data.items():
        if d["inadmissible"]:
            ax.plot(D, A, "X", color="black", markersize=10, zorder=5)

    # Annotate sigma values on the grid
    for (D, A), d in sweep_data.items():
        if d["sigma"] > 0 and not d["inadmissible"]:
            ax.text(
                D, A, f"{d['sigma']:.2f}",
                ha="center", va="center", fontsize=7,
                color="black" if d["sigma"] < 0.5 * vmax else "white",
                fontweight="bold",
            )

    setup_axes(ax, r"Diffusion coefficient $D$",
               r"Perturbation amplitude $A$",
               r"Decay-Rate Surface $\sigma(D, A)$")
    ax.set_xscale("log")
    ax.set_yscale("log")
    fig.tight_layout()
    fig.savefig(os.path.join(FIG_DIR, "decay_rate_surface.png"), dpi=300)
    plt.close(fig)
    print("  Saved: decay_rate_surface.png")


# ---------------------------------------------------------------------------
# Figure C: Peak-active-modes surface
# ---------------------------------------------------------------------------
def figure_peak_active_surface(sweep_data: dict):
    D_vals = sorted(set(d["D"] for d in sweep_data.values()))
    A_vals = sorted(set(d["A"] for d in sweep_data.values()))

    peak_grid = np.full((len(A_vals), len(D_vals)), np.nan)
    for (D, A), d in sweep_data.items():
        i_D = D_vals.index(D)
        i_A = A_vals.index(A)
        if not d["inadmissible"]:
            peak_grid[i_A, i_D] = d["peak_active"]

    fig, ax = plt.subplots(figsize=(9, 6))

    valid = peak_grid[np.isfinite(peak_grid)]
    if len(valid) == 0:
        ax.text(0.5, 0.5, "No valid data", ha="center", va="center",
                transform=ax.transAxes, fontsize=14, color="0.5")
        setup_axes(ax, "$D$", "$A$", "Peak Active Modes")
        fig.tight_layout()
        fig.savefig(os.path.join(FIG_DIR, "peak_active_surface.png"), dpi=300)
        plt.close(fig)
        return

    im = ax.pcolormesh(
        D_vals, A_vals,
        np.ma.masked_invalid(peak_grid),
        cmap="viridis",
        shading="nearest",
    )
    cbar = fig.colorbar(im, ax=ax, label="Peak active modes", pad=0.02)
    cbar.ax.tick_params(labelsize=9)

    # Annotate counts
    for (D, A), d in sweep_data.items():
        if not d["inadmissible"]:
            ax.text(
                D, A, str(d["peak_active"]),
                ha="center", va="center", fontsize=7,
                color="white" if d["peak_active"] > 0.6 * valid.max() else "black",
                fontweight="bold",
            )
        else:
            ax.plot(D, A, "X", color="red", markersize=10, zorder=5)

    setup_axes(ax, r"Diffusion coefficient $D$",
               r"Perturbation amplitude $A$",
               "Peak Active Modes -- $(D, A)$ Plane")
    ax.set_xscale("log")
    ax.set_yscale("log")
    fig.tight_layout()
    fig.savefig(os.path.join(FIG_DIR, "peak_active_surface.png"), dpi=300)
    plt.close(fig)
    print("  Saved: peak_active_surface.png")


# ---------------------------------------------------------------------------
# Figure D: Representative modal funnels
# ---------------------------------------------------------------------------
def figure_representative_funnels(runs: dict, sweep_data: dict):
    """Select a few representative (D, A) pairs and plot modal funnels."""
    # Selection strategy: pick corners and center of the grid
    D_vals = sorted(set(d["D"] for d in sweep_data.values()))
    A_vals = sorted(set(d["A"] for d in sweep_data.values()))

    candidates = []

    # Low D, low A (underdamped, weak perturbation)
    candidates.append((D_vals[0], A_vals[0]))
    # Low D, high A (underdamped, strong perturbation)
    candidates.append((D_vals[0], A_vals[-1]))
    # High D, low A (likely overdamped, weak)
    candidates.append((D_vals[-1], A_vals[0]))
    # High D, high A (overdamped, strong)
    candidates.append((D_vals[-1], A_vals[-1]))
    # Middle
    mid_D = D_vals[len(D_vals) // 2]
    mid_A = A_vals[len(A_vals) // 2]
    candidates.append((mid_D, mid_A))

    # Filter to those that exist and are admissible
    selected = []
    for key in candidates:
        if key in runs and not sweep_data.get(key, {}).get("inadmissible", True):
            selected.append(key)
    selected = selected[:6]  # Cap at 6

    if not selected:
        print("  SKIP: no admissible runs for representative funnels.")
        return

    n_sel = len(selected)
    ncols = min(n_sel, 3)
    nrows = (n_sel + ncols - 1) // ncols

    fig, axes = plt.subplots(
        nrows, ncols, figsize=(5.5 * ncols, 4.5 * nrows),
        squeeze=False,
    )

    cmap = plt.cm.viridis

    for idx, (D_val, A_val) in enumerate(selected):
        row = idx // ncols
        col = idx % ncols
        ax = axes[row, col]

        ts = runs[(D_val, A_val)]["data"]
        meta = ts["metadata"]
        modal = ts.get("modal_amplitudes")
        t = ts["t"]

        if modal is None or modal.ndim != 2:
            ax.text(0.5, 0.5, "No modal data", ha="center", va="center",
                    transform=ax.transAxes, fontsize=10, color="0.5")
            ax.set_title(f"$D={D_val}$, $A={A_val}$", fontsize=10)
            continue

        n_snap = min(len(t), modal.shape[0])
        n_modes = modal.shape[1]
        A_pm = meta.get("A_per_mode", A_val)
        thresh = ACTIVATION_FRAC * A_pm ** 2
        peak_amp = np.max(np.abs(modal[:n_snap]), axis=0)
        active = np.where(peak_amp > thresh)[0]

        if len(active) == 0:
            ax.text(0.5, 0.5, "No active modes", ha="center", va="center",
                    transform=ax.transAxes, fontsize=10, color="0.5")
            ax.set_title(f"$D={D_val}$, $A={A_val}$", fontsize=10)
            continue

        k_max = active[-1]
        norm = mcolors.Normalize(vmin=0, vmax=max(k_max, 1))

        for k in active:
            a_k = np.abs(modal[:n_snap, k])
            ax.semilogy(
                t[:n_snap], np.maximum(a_k, 1e-30),
                color=cmap(norm(k)),
                linewidth=0.7, alpha=0.7,
            )

        d = sweep_data[(D_val, A_val)]
        regime = d["effective_regime"].replace("_", " ")
        Delta = d["Delta"]

        ax.set_title(
            f"$D={D_val}$, $A={A_val}$\n"
            f"$\\Delta={Delta:.2f}$, {regime}",
            fontsize=10,
        )
        ax.set_xlabel(r"$t$", fontsize=9)
        ax.set_ylabel(r"$|a_k|$", fontsize=9)
        ax.tick_params(labelsize=8)
        ax.grid(True, alpha=0.25, linewidth=0.4)

    # Turn off unused axes
    for idx in range(n_sel, nrows * ncols):
        row = idx // ncols
        col = idx % ncols
        axes[row, col].set_visible(False)

    fig.suptitle("Representative Modal Funnels -- $(D, A)$ Plane",
                 fontsize=14, fontweight="bold", y=1.01)
    fig.tight_layout()
    fig.savefig(os.path.join(FIG_DIR, "representative_funnels.png"),
                dpi=300, bbox_inches="tight")
    plt.close(fig)
    print("  Saved: representative_funnels.png")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    os.makedirs(FIG_DIR, exist_ok=True)

    print("Discovering 2D regime-map runs...")
    runs = discover_runs()

    if not runs:
        print(f"\nERROR: No regime_D*_A* runs found in:")
        print(f"  {RUNS_DIR}")
        print("\nRun the experiment first:")
        print("  python experiments/regime_map_2d.py")
        sys.exit(1)

    keys = sorted(runs.keys())
    D_vals = sorted(set(k[0] for k in keys))
    A_vals = sorted(set(k[1] for k in keys))
    print(f"  Found {len(runs)} runs")
    print(f"  D grid: {D_vals}")
    print(f"  A grid: {A_vals}")

    # Pre-compute
    print("\nComputing sweep data...")
    sweep_data = compute_sweep_data(runs)

    # --- (A) Regime map ---
    print("\n--- (A) 2D Regime Map ---")
    figure_regime_map(sweep_data)

    # --- (B) Decay-rate surface ---
    print("\n--- (B) Decay-Rate Surface ---")
    figure_decay_rate_surface(sweep_data)

    # --- (C) Peak-active-modes surface ---
    print("\n--- (C) Peak Active Modes Surface ---")
    figure_peak_active_surface(sweep_data)

    # --- (D) Representative funnels ---
    print("\n--- (D) Representative Modal Funnels ---")
    figure_representative_funnels(runs, sweep_data)

    # --- Summary table ---
    print(f"\n{'='*115}")
    print("  2D Regime Map -- Summary Table")
    print(f"{'='*115}")
    print(f"  {'D':<8} {'A':<8} {'Delta':<9} {'Regime':<18} "
          f"{'sigma':<12} {'R^2':<8} {'Peak':<7} "
          f"{'E(0)':<14} {'E(T)':<14} {'Signs':<7}")
    print("  " + "-" * 110)

    for key in sorted(sweep_data.keys()):
        d = sweep_data[key]
        regime = d["effective_regime"][:16]
        print(f"  {d['D']:<8.3f} {d['A']:<8.4f} {d['Delta']:<9.4f} "
              f"{regime:<18} {d['sigma']:<12.6f} {d['R2']:<8.4f} "
              f"{d['peak_active']:<7} {d['E0']:<14.6e} {d['ET']:<14.6e} "
              f"{d['n_sign_changes']:<7}")

    # --- Regime grid (compact) ---
    abbrev = {
        "underdamped": "UD", "underdamped_weak": "UDw",
        "oscillatory": "OSC", "critical": "CR",
        "overdamped": "OD", "transient_oscillatory": "tOSC",
        "inadmissible": "INAD", "unknown": "?",
    }

    print(f"\n  Compact Regime Grid:")
    header = f"  {'D \\ A':<10}"
    for A_val in A_vals:
        header += f" {A_val:<8}"
    print(header)
    print("  " + "-" * (10 + 9 * len(A_vals)))

    for D_val in D_vals:
        row = f"  {D_val:<10.3f}"
        for A_val in A_vals:
            d = sweep_data.get((D_val, A_val))
            if d is None:
                row += f" {'--':<8}"
            else:
                short = abbrev.get(d["effective_regime"], "?")
                row += f" {short:<8}"
        print(row)

    # --- Statistics ---
    regime_counts = {}
    for d in sweep_data.values():
        r = d["effective_regime"]
        regime_counts[r] = regime_counts.get(r, 0) + 1

    n_inad = sum(1 for d in sweep_data.values() if d["inadmissible"])
    print(f"\n  Statistics:")
    print(f"    Total points:    {len(sweep_data)}")
    print(f"    Admissible:      {len(sweep_data) - n_inad}")
    print(f"    Inadmissible:    {n_inad}")
    print(f"\n  Regime distribution:")
    for r in REGIME_ORDER:
        if r in regime_counts:
            print(f"    {r:<24}: {regime_counts[r]}")

    # Sigma statistics for admissible points
    sigmas = [d["sigma"] for d in sweep_data.values()
              if d["sigma"] > 0 and not d["inadmissible"]]
    if sigmas:
        print(f"\n  Decay rate statistics (admissible, sigma > 0):")
        print(f"    min sigma:  {min(sigmas):.6f}")
        print(f"    max sigma:  {max(sigmas):.6f}")
        print(f"    mean sigma: {np.mean(sigmas):.6f}")

    print(f"\nAll figures saved to: {FIG_DIR}")
    print("Done.")


if __name__ == "__main__":
    main()
