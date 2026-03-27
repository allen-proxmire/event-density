"""
analyze_broadband_cascade.py
=============================
Post-processing script for the Broadband Cascade experiment (Atlas §4).

Loads all broadband_IC* runs and produces:

  Per-IC figures:
    (A) Modal collapse -- |a_k(t)| for all activated modes, colored by k.
    (B) Network density -- number of modes above threshold vs time.

  Cross-IC figures:
    (C) Energy and complexity comparison.
    (D) Dissipation channels for the largest IC.

All figures saved to output/figures/broadband_cascade/ as PNG (300 dpi).

Usage:
    python analyze_broadband_cascade.py

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
from matplotlib.collections import LineCollection
import matplotlib.colors as mcolors

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
RUNS_DIR = os.path.join(SCRIPT_DIR, "output", "runs")
FIG_DIR = os.path.join(SCRIPT_DIR, "output", "figures", "broadband_cascade")

RE_IC = re.compile(r"^broadband_(IC\d+)$")

# A mode is "active" if |a_k| exceeds this fraction of A^2
ACTIVATION_FRAC = 1e-4


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
    runs = {}
    if not os.path.isdir(RUNS_DIR):
        print(f"ERROR: runs directory not found: {RUNS_DIR}")
        sys.exit(1)
    for name in sorted(os.listdir(RUNS_DIR)):
        m = RE_IC.match(name)
        if not m:
            continue
        run_dir = os.path.join(RUNS_DIR, name)
        if not os.path.isdir(run_dir):
            continue
        data = load_run(run_dir)
        if data is not None:
            runs[m.group(1)] = {"dir": run_dir, "name": name, "data": data}
    return dict(sorted(runs.items()))


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def setup_axes(ax, xlabel: str, ylabel: str, title: str):
    ax.set_xlabel(xlabel, fontsize=11)
    ax.set_ylabel(ylabel, fontsize=11)
    ax.set_title(title, fontsize=13, fontweight="bold")
    ax.tick_params(labelsize=10)
    ax.grid(True, alpha=0.3, linewidth=0.5)


def activated_mask(modal: np.ndarray, A: float) -> np.ndarray:
    """Boolean array of shape (n_modes,): True if mode ever exceeds threshold."""
    thresh = ACTIVATION_FRAC * A ** 2
    peak = np.max(np.abs(modal), axis=0)
    return peak > thresh


def active_count_vs_time(modal: np.ndarray, A: float) -> np.ndarray:
    """Number of modes above threshold at each time step."""
    thresh = ACTIVATION_FRAC * A ** 2
    return np.sum(np.abs(modal) > thresh, axis=1)


# ---------------------------------------------------------------------------
# Figure A (per IC): Modal collapse -- |a_k(t)| colored by k
# ---------------------------------------------------------------------------
def figure_modal_collapse(label: str, run: dict):
    ts = run["data"]
    meta = ts["metadata"]
    modal = ts.get("modal_amplitudes")

    if modal is None or modal.ndim != 2:
        print(f"  SKIP {label}: no modal_amplitudes.")
        return

    seeded = meta.get("seeded_modes", [])
    A_pm = meta.get("A_per_mode", 0.02)
    t = ts["t"]
    n_snap = min(len(t), modal.shape[0])
    n_modes = modal.shape[1]

    mask = activated_mask(modal[:n_snap], A_pm)
    active_indices = np.where(mask)[0]

    if len(active_indices) == 0:
        print(f"  SKIP {label}: no activated modes.")
        return

    k_max_active = active_indices[-1]

    fig, ax = plt.subplots(figsize=(10, 6))

    # Colormap: viridis by mode index
    norm = mcolors.Normalize(vmin=0, vmax=max(k_max_active, 1))
    cmap = plt.cm.viridis

    for k in active_indices:
        a_k = np.abs(modal[:n_snap, k])
        color = cmap(norm(k))

        # Seeded modes slightly thicker
        lw = 1.4 if k in seeded else 0.8
        alpha = 0.9 if k in seeded else 0.6

        ax.semilogy(
            t[:n_snap],
            np.maximum(a_k, 1e-30),
            color=color,
            linewidth=lw,
            alpha=alpha,
        )

    # Colorbar
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])
    cbar = fig.colorbar(sm, ax=ax, label="Mode index $k$", pad=0.02)
    cbar.ax.tick_params(labelsize=9)

    # Funnel annotation
    ax.annotate(
        r"Higher $k$ $\longrightarrow$ faster decay",
        xy=(0.50, 0.08),
        xycoords="axes fraction",
        fontsize=10, fontstyle="italic", color="0.35",
        ha="center",
        bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.7),
    )

    # Seed range annotation
    if seeded:
        ax.annotate(
            f"Seeded: modes {seeded[0]}-{seeded[-1]} ({len(seeded)} modes)",
            xy=(0.02, 0.95),
            xycoords="axes fraction",
            fontsize=9, va="top",
            bbox=dict(boxstyle="round,pad=0.3",
                      facecolor="wheat", alpha=0.7, edgecolor="0.6"),
        )

    setup_axes(
        ax,
        xlabel=r"Time $t$",
        ylabel=r"Modal amplitude $|a_k(t)|$",
        title=f"Broadband Cascade -- {label}: modes {seeded[0]}-{seeded[-1]}",
    )
    fig.tight_layout()

    fname = f"modal_collapse_{label}.png"
    fig.savefig(os.path.join(FIG_DIR, fname), dpi=300)
    plt.close(fig)
    print(f"  Saved: {fname}")


# ---------------------------------------------------------------------------
# Figure B (per IC): Network density -- active mode count vs time
# ---------------------------------------------------------------------------
def figure_network_density(label: str, run: dict):
    ts = run["data"]
    meta = ts["metadata"]
    modal = ts.get("modal_amplitudes")

    if modal is None or modal.ndim != 2:
        print(f"  SKIP {label}: no modal_amplitudes.")
        return

    A_pm = meta.get("A_per_mode", 0.02)
    seeded = meta.get("seeded_modes", [])
    t = ts["t"]
    n_snap = min(len(t), modal.shape[0])

    count = active_count_vs_time(modal[:n_snap], A_pm)

    fig, ax = plt.subplots(figsize=(9, 5))

    ax.plot(
        t[:n_snap], count,
        color="#2166ac", linewidth=1.8,
    )

    # Horizontal line at the seeded count
    n_seeded = len(seeded)
    ax.axhline(
        n_seeded, color="#b2182b", linestyle="--", linewidth=1.0, alpha=0.6,
        label=f"Seeded count ({n_seeded})",
    )

    # Fill between to highlight network expansion then collapse
    ax.fill_between(
        t[:n_snap], n_seeded, count,
        where=count > n_seeded,
        color="#2166ac", alpha=0.12,
        label="Triad-generated excess",
    )

    setup_axes(
        ax,
        xlabel=r"Time $t$",
        ylabel="Number of active modes",
        title=f"Triad Network Density -- {label}: modes {seeded[0]}-{seeded[-1]}",
    )
    ax.legend(fontsize=10, loc="upper right", framealpha=0.9)
    ax.set_ylim(bottom=0)
    fig.tight_layout()

    fname = f"network_density_{label}.png"
    fig.savefig(os.path.join(FIG_DIR, fname), dpi=300)
    plt.close(fig)
    print(f"  Saved: {fname}")


# ---------------------------------------------------------------------------
# Figure C: Energy and complexity comparison across ICs
# ---------------------------------------------------------------------------
def figure_cross_ic_comparison(runs: dict):
    ic_colors = {"IC1": "#2166ac", "IC2": "#b2182b", "IC3": "#1b7837", "IC4": "#762a83"}
    ic_styles = {"IC1": "-", "IC2": "--", "IC3": "-.", "IC4": ":"}

    fig, (ax_e, ax_c) = plt.subplots(
        1, 2, figsize=(14, 5),
        gridspec_kw={"wspace": 0.28},
    )

    for label, run in sorted(runs.items()):
        ts = run["data"]
        meta = ts["metadata"]
        seeded = meta.get("seeded_modes", [])
        t = ts["t"]

        color = ic_colors.get(label, "0.3")
        ls = ic_styles.get(label, "-")
        range_str = f"{seeded[0]}-{seeded[-1]}" if seeded else "?"

        # Energy
        E = ts["E_total"]
        n = min(len(t), len(E))
        ax_e.semilogy(
            t[:n], E[:n],
            color=color, linestyle=ls, linewidth=1.5,
            label=f"{label}: {range_str}",
        )

        # Complexity
        C = ts.get("C_ED")
        if C is not None:
            n_c = min(len(t), len(C))
            ax_c.semilogy(
                t[:n_c], C[:n_c],
                color=color, linestyle=ls, linewidth=1.5,
                label=f"{label}: {range_str}",
            )

    setup_axes(ax_e, r"Time $t$", r"Energy $\mathcal{E}(t)$",
               "Energy Decay -- Broadband Cascade")
    ax_e.legend(fontsize=9, loc="upper right", framealpha=0.9)

    setup_axes(ax_c, r"Time $t$", r"$C_{\mathrm{ED}}(t)$",
               "Complexity Decay -- Broadband Cascade")
    ax_c.legend(fontsize=9, loc="upper right", framealpha=0.9)

    fig.tight_layout()
    fname = "cross_ic_energy_complexity.png"
    fig.savefig(os.path.join(FIG_DIR, fname), dpi=300)
    plt.close(fig)
    print(f"  Saved: {fname}")


# ---------------------------------------------------------------------------
# Figure D: Dissipation channels for the largest IC
# ---------------------------------------------------------------------------
def figure_dissipation_largest(runs: dict):
    # Find the IC with the most seeded modes
    best_label = None
    best_count = 0
    for label, run in runs.items():
        meta = run["data"]["metadata"]
        n = meta.get("n_seeded", len(meta.get("seeded_modes", [])))
        if n > best_count:
            best_count = n
            best_label = label

    if best_label is None:
        print("  SKIP: no runs available for dissipation plot.")
        return

    ts = runs[best_label]["data"]
    meta = ts["metadata"]
    seeded = meta.get("seeded_modes", [])
    t = ts["t"]

    fig, ax = plt.subplots(figsize=(9, 6))

    channels = [
        (r"Gradient $\mathcal{D}_{\mathrm{grad}}$", "D_gradient", "#2166ac", "-"),
        (r"Penalty $\mathcal{D}_{\mathrm{pen}}$",   "D_penalty",  "#b2182b", "-"),
        (r"Participation $\mathcal{D}_{\mathrm{part}}$", "D_participation", "#1b7837", "-"),
        (r"Total $\mathcal{D}$", "D_total", "black", "--"),
    ]

    plotted = False
    for ch_label, field, color, ls in channels:
        if field in ts:
            data = ts[field]
            n = min(len(t), len(data))
            ax.semilogy(
                t[:n],
                np.maximum(data[:n], 1e-30),
                color=color,
                linestyle=ls,
                linewidth=1.5 if ls == "-" else 1.2,
                label=ch_label,
                alpha=1.0 if ls == "-" else 0.7,
            )
            plotted = True

    if not plotted:
        ax.text(
            0.5, 0.5,
            "Dissipation channel data not available",
            ha="center", va="center", fontsize=12, color="0.5",
            transform=ax.transAxes,
        )

    setup_axes(
        ax,
        xlabel=r"Time $t$",
        ylabel="Dissipation rate",
        title=f"Dissipation Channels -- {best_label}: modes "
              f"{seeded[0]}-{seeded[-1]} ({best_count} modes)",
    )
    ax.legend(fontsize=10, loc="upper right", framealpha=0.9)
    fig.tight_layout()

    fname = f"dissipation_{best_label}.png"
    fig.savefig(os.path.join(FIG_DIR, fname), dpi=300)
    plt.close(fig)
    print(f"  Saved: {fname}")


# ---------------------------------------------------------------------------
# Figure E (bonus): Network density comparison across ICs
# ---------------------------------------------------------------------------
def figure_network_density_comparison(runs: dict):
    ic_colors = {"IC1": "#2166ac", "IC2": "#b2182b", "IC3": "#1b7837", "IC4": "#762a83"}
    ic_styles = {"IC1": "-", "IC2": "--", "IC3": "-.", "IC4": ":"}

    fig, ax = plt.subplots(figsize=(9, 5))

    for label, run in sorted(runs.items()):
        ts = run["data"]
        meta = ts["metadata"]
        modal = ts.get("modal_amplitudes")
        if modal is None or modal.ndim != 2:
            continue

        seeded = meta.get("seeded_modes", [])
        A_pm = meta.get("A_per_mode", 0.02)
        t = ts["t"]
        n_snap = min(len(t), modal.shape[0])

        count = active_count_vs_time(modal[:n_snap], A_pm)
        range_str = f"{seeded[0]}-{seeded[-1]}" if seeded else "?"

        ax.plot(
            t[:n_snap], count,
            color=ic_colors.get(label, "0.3"),
            linestyle=ic_styles.get(label, "-"),
            linewidth=1.5,
            label=f"{label}: {range_str} ({len(seeded)} modes)",
        )

    setup_axes(
        ax,
        xlabel=r"Time $t$",
        ylabel="Number of active modes",
        title="Triad Network Density -- All Broadband ICs",
    )
    ax.legend(fontsize=9, loc="upper right", framealpha=0.9)
    ax.set_ylim(bottom=0)
    fig.tight_layout()

    fname = "network_density_comparison.png"
    fig.savefig(os.path.join(FIG_DIR, fname), dpi=300)
    plt.close(fig)
    print(f"  Saved: {fname}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    os.makedirs(FIG_DIR, exist_ok=True)

    print("Discovering broadband cascade runs...")
    runs = discover_runs()

    if not runs:
        print(f"\nERROR: No broadband_IC* runs found in:")
        print(f"  {RUNS_DIR}")
        print("\nRun the experiment first:")
        print("  python experiments/broadband_cascade.py")
        sys.exit(1)

    print(f"  Found {len(runs)} runs:")
    for label, run in runs.items():
        meta = run["data"]["metadata"]
        seeded = meta.get("seeded_modes", [])
        tri = meta.get("triad_statistics", {})
        print(f"    {label}: modes {seeded[0]}-{seeded[-1]} "
              f"({len(seeded)} modes, {tri.get('n_triads', '?')} triads)")

    # --- (A) Per-IC modal collapse ---
    print("\n--- (A) Modal Collapse Figures ---")
    for label, run in runs.items():
        figure_modal_collapse(label, run)

    # --- (B) Per-IC network density ---
    print("\n--- (B) Network Density Figures ---")
    for label, run in runs.items():
        figure_network_density(label, run)

    # --- (C) Cross-IC energy and complexity ---
    print("\n--- (C) Energy & Complexity Comparison ---")
    figure_cross_ic_comparison(runs)

    # --- (D) Dissipation channels (largest IC) ---
    print("\n--- (D) Dissipation Channels (Largest IC) ---")
    figure_dissipation_largest(runs)

    # --- (E) Network density comparison ---
    print("\n--- (E) Network Density Comparison ---")
    figure_network_density_comparison(runs)

    # --- Summary table ---
    print(f"\n{'='*80}")
    print("  Broadband Cascade Analysis Summary")
    print(f"{'='*80}")
    print(f"  {'IC':<6} {'Range':<10} {'#Seed':<7} {'#Triads':<9} "
          f"{'Peak active':<13} {'E(0)':<14} {'E(T)':<14}")
    print("  " + "-" * 73)

    for label, run in sorted(runs.items()):
        ts = run["data"]
        meta = ts["metadata"]
        seeded = meta.get("seeded_modes", [])
        tri = meta.get("triad_statistics", {})
        modal = ts.get("modal_amplitudes")
        A_pm = meta.get("A_per_mode", 0.02)

        peak_active = "--"
        if modal is not None and modal.ndim == 2:
            n_snap = min(len(ts["t"]), modal.shape[0])
            count = active_count_vs_time(modal[:n_snap], A_pm)
            peak_active = str(int(np.max(count)))

        print(f"  {label:<6} {seeded[0]}-{seeded[-1]:<7} {len(seeded):<7} "
              f"{tri.get('n_triads', '?'):<9} {peak_active:<13} "
              f"{ts['E_total'][0]:<14.6e} {ts['E_total'][-1]:<14.6e}")

    print(f"\nAll figures saved to: {FIG_DIR}")
    print("Done.")


if __name__ == "__main__":
    main()
