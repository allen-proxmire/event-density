"""
analyze_modal_hierarchy.py
==========================
Post-processing script for the Modal Hierarchy experiments (Atlas §3).

Scans output/runs/ for all modal-hierarchy runs, loads diagnostics,
and produces four publication-quality figures:

  Figure A:  Single-mode decay -- |a_k(t)| for each single-mode run,
             with predicted slopes -D*alpha_k overlaid.
  Figure B:  Modal funnel -- |a_k(t)| for k = 0..10 from the multi-mode run,
             demonstrating the spectral gap (higher modes collapse first).
  Figure C:  Triad activation -- if a two-mode IC run is present,
             plot |a_1|, |a_2|, |a_3| showing nonlinear generation of a_3.
  Figure D:  Dissipation channels -- D_grad, D_pen, D_part, D_total
             for a representative run.

All figures saved to output/figures/modal_hierarchy/ as PNG (300 dpi).

Usage:
    python analyze_modal_hierarchy.py

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

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
RUNS_DIR = os.path.join(SCRIPT_DIR, "output", "runs")
FIG_DIR = os.path.join(SCRIPT_DIR, "output", "figures", "modal_hierarchy")

# Regex patterns for run discovery
RE_SINGLE = re.compile(r"^modal_single_([IVX]+)_n(\d+)$")
RE_MULTI = re.compile(r"^modal_multi_([IVX]+)_Nm(\d+)$")


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def load_run(run_dir: str) -> dict:
    """Load time_series.npz and metadata.json from a run directory."""
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


def discover_runs():
    """Scan output/runs/ and classify all modal-hierarchy runs.

    Returns
    -------
    single_runs : dict  {(param_set, mode_n): {"dir": ..., "data": ...}}
    multi_runs  : dict  {(param_set, N_m):    {"dir": ..., "data": ...}}
    """
    single_runs = {}
    multi_runs = {}

    if not os.path.isdir(RUNS_DIR):
        print(f"ERROR: runs directory not found: {RUNS_DIR}")
        sys.exit(1)

    for name in sorted(os.listdir(RUNS_DIR)):
        run_dir = os.path.join(RUNS_DIR, name)
        if not os.path.isdir(run_dir):
            continue

        m_single = RE_SINGLE.match(name)
        m_multi = RE_MULTI.match(name)

        if m_single:
            param_set = m_single.group(1)
            mode_n = int(m_single.group(2))
            data = load_run(run_dir)
            if data is not None:
                single_runs[(param_set, mode_n)] = {
                    "dir": run_dir,
                    "name": name,
                    "data": data,
                }

        elif m_multi:
            param_set = m_multi.group(1)
            n_m = int(m_multi.group(2))
            data = load_run(run_dir)
            if data is not None:
                multi_runs[(param_set, n_m)] = {
                    "dir": run_dir,
                    "name": name,
                    "data": data,
                }

    return single_runs, multi_runs


def predicted_decay_rate(meta: dict, k: int) -> float:
    """Compute the predicted linear decay rate D * alpha_k from metadata.

    alpha_k = M_star * mu_k + P_star_prime
    mu_k    = (k * pi / L)^2
    """
    D = meta.get("D", 0.3)
    L = meta.get("L", 1.0)
    rho_star = meta.get("rho_star", 0.5)
    rho_max = meta.get("rho_max", 1.0)
    M0 = meta.get("M0", 1.0)
    beta = meta.get("beta", 2.0)
    P0 = meta.get("P0", 1.0)

    M_star = M0 * (rho_max - rho_star) ** beta
    P_star_prime = P0
    mu_k = (k * np.pi / L) ** 2
    alpha_k = M_star * mu_k + P_star_prime
    return D * alpha_k


def setup_axes(ax, xlabel: str, ylabel: str, title: str):
    """Standard axis formatting."""
    ax.set_xlabel(xlabel, fontsize=11)
    ax.set_ylabel(ylabel, fontsize=11)
    ax.set_title(title, fontsize=13, fontweight="bold")
    ax.tick_params(labelsize=10)
    ax.grid(True, alpha=0.3, linewidth=0.5)


# ---------------------------------------------------------------------------
# Figure A: Single-Mode Decay
# ---------------------------------------------------------------------------
def figure_single_mode_decay(single_runs: dict):
    """Plot |a_k(t)| for each single-mode run with predicted slopes."""
    if not single_runs:
        print("  SKIP: no single-mode runs found.")
        return

    # Group by parameter set
    by_set = {}
    for (param_set, mode_n), run in single_runs.items():
        by_set.setdefault(param_set, []).append((mode_n, run))

    for param_set in sorted(by_set.keys()):
        entries = sorted(by_set[param_set], key=lambda x: x[0])

        fig, ax = plt.subplots(figsize=(9, 6))
        cmap = plt.cm.viridis(np.linspace(0.1, 0.9, len(entries)))

        for idx, (mode_n, run) in enumerate(entries):
            ts = run["data"]
            meta = ts["metadata"]
            t = ts["t"]

            # Extract modal amplitude for mode n
            modal = ts.get("modal_amplitudes")
            if modal is None or modal.ndim != 2:
                continue

            k_idx = min(mode_n, modal.shape[1] - 1)
            a_k = np.abs(modal[:, k_idx])
            n_snap = min(len(t), len(a_k))

            ax.semilogy(
                t[:n_snap],
                np.maximum(a_k[:n_snap], 1e-30),
                color=cmap[idx],
                linewidth=1.5,
                label=rf"$|a_{{{mode_n}}}|$ (measured)",
            )

            # Predicted slope: a_k(t) ~ a_k(0) * exp(-D * alpha_k * t)
            sigma_pred = predicted_decay_rate(meta, mode_n)
            if a_k[0] > 1e-30 and sigma_pred > 0:
                t_line = np.linspace(t[0], t[min(n_snap - 1, len(t) - 1)], 200)
                a_pred = a_k[0] * np.exp(-sigma_pred * t_line)
                ax.semilogy(
                    t_line,
                    np.maximum(a_pred, 1e-30),
                    color=cmap[idx],
                    linewidth=1.0,
                    linestyle="--",
                    alpha=0.6,
                    label=rf"$D\alpha_{{{mode_n}}} = {sigma_pred:.3f}$ (predicted)",
                )

        setup_axes(
            ax,
            xlabel=r"Time $t$",
            ylabel=r"Modal amplitude $|a_k(t)|$",
            title=f"Single-Mode Decay -- Parameter Set {param_set}",
        )
        ax.legend(fontsize=8, loc="upper right", framealpha=0.9, ncol=2)
        fig.tight_layout()

        fname = f"single_mode_decay_{param_set}.png"
        fig.savefig(os.path.join(FIG_DIR, fname), dpi=300)
        plt.close(fig)
        print(f"  Saved: {fname}")


# ---------------------------------------------------------------------------
# Figure B: Modal Funnel (Multi-Mode)
# ---------------------------------------------------------------------------
def figure_modal_funnel(multi_runs: dict):
    """Plot |a_k(t)| for k = 0..10 from the multi-mode run."""
    if not multi_runs:
        print("  SKIP: no multi-mode runs found.")
        return

    for (param_set, n_m), run in sorted(multi_runs.items()):
        ts = run["data"]
        meta = ts["metadata"]
        t = ts["t"]

        modal = ts.get("modal_amplitudes")
        if modal is None or modal.ndim != 2:
            print(f"  SKIP: no modal_amplitudes in {run['name']}")
            continue

        n_modes_plot = min(11, modal.shape[1])  # k = 0..10
        n_snap = min(len(t), modal.shape[0])

        fig, ax = plt.subplots(figsize=(9, 6))
        cmap = plt.cm.plasma(np.linspace(0.1, 0.9, n_modes_plot))

        for k in range(n_modes_plot):
            a_k = np.abs(modal[:n_snap, k])
            ax.semilogy(
                t[:n_snap],
                np.maximum(a_k, 1e-30),
                color=cmap[k],
                linewidth=1.3,
                label=rf"$|a_{{{k}}}|$",
            )

        # Annotate the funnel: higher modes decay faster
        ax.annotate(
            r"Higher $k$ $\longrightarrow$ faster decay",
            xy=(0.55, 0.15),
            xycoords="axes fraction",
            fontsize=10,
            fontstyle="italic",
            color="0.4",
            ha="center",
        )

        setup_axes(
            ax,
            xlabel=r"Time $t$",
            ylabel=r"Modal amplitude $|a_k(t)|$",
            title=f"Modal Funnel -- Set {param_set}, $N_m = {n_m}$",
        )
        ax.legend(fontsize=8, loc="upper right", framealpha=0.9, ncol=2)
        fig.tight_layout()

        fname = f"modal_funnel_{param_set}_Nm{n_m}.png"
        fig.savefig(os.path.join(FIG_DIR, fname), dpi=300)
        plt.close(fig)
        print(f"  Saved: {fname}")


# ---------------------------------------------------------------------------
# Figure C: Triad Activation
# ---------------------------------------------------------------------------
def figure_triad_activation(single_runs: dict, multi_runs: dict):
    """If a two-mode IC run is present, show triad generation of a_3.

    Strategy: look for a multi-mode run with N_m=2, or use a single-mode
    run where we can observe the triad-generated mode. Alternatively, look
    for any run whose IC seeded exactly modes 1 and 2.
    """
    # Prefer a multi-mode run with N_m = 2 (seeds modes 1 and 2)
    triad_run = None
    triad_label = ""

    for (param_set, n_m), run in multi_runs.items():
        if n_m == 2:
            triad_run = run
            triad_label = f"Set {param_set}, IC-B ($N_m = 2$)"
            break

    # Fallback: look for single-mode runs with modes 1 and 2 in the same set
    if triad_run is None:
        sets_with_modes = {}
        for (param_set, mode_n), run in single_runs.items():
            sets_with_modes.setdefault(param_set, {})[mode_n] = run
        for ps, modes in sets_with_modes.items():
            if 1 in modes and 2 in modes:
                # Use mode-1 run (it will show triad generation into mode 2)
                triad_run = modes[1]
                triad_label = f"Set {ps}, IC-A ($n = 1$)"
                break

    if triad_run is None:
        print("  SKIP: no suitable two-mode or triad run found.")
        return

    ts = triad_run["data"]
    t = ts["t"]
    modal = ts.get("modal_amplitudes")

    if modal is None or modal.ndim != 2 or modal.shape[1] < 4:
        print("  SKIP: insufficient modal data for triad plot.")
        return

    n_snap = min(len(t), modal.shape[0])

    fig, ax = plt.subplots(figsize=(9, 6))

    # Plot modes 1, 2, 3 (the fundamental triad: 1+2=3, |2-1|=1)
    mode_colors = {1: "#2166ac", 2: "#b2182b", 3: "#1b7837"}
    mode_styles = {1: "-", 2: "-", 3: "--"}

    for k in (1, 2, 3):
        if k >= modal.shape[1]:
            continue
        a_k = np.abs(modal[:n_snap, k])
        style = mode_styles.get(k, "-")
        color = mode_colors.get(k, "0.3")

        lw = 2.0 if k == 3 else 1.5
        label = rf"$|a_{{{k}}}|$"
        if k == 3:
            label += r" (triad-generated)"

        ax.semilogy(
            t[:n_snap],
            np.maximum(a_k, 1e-30),
            color=color,
            linestyle=style,
            linewidth=lw,
            label=label,
        )

    # Also plot mode 0 (homogeneous) for reference
    if modal.shape[1] > 0:
        a_0 = np.abs(modal[:n_snap, 0])
        ax.semilogy(
            t[:n_snap],
            np.maximum(a_0, 1e-30),
            color="0.5",
            linestyle=":",
            linewidth=1.0,
            label=r"$|a_0|$ (homogeneous)",
            alpha=0.6,
        )

    # Annotation: triad selection rule
    ax.annotate(
        r"Triad: $1 + 2 = 3$, $|2 - 1| = 1$",
        xy=(0.5, 0.08),
        xycoords="axes fraction",
        fontsize=10,
        fontstyle="italic",
        color="0.3",
        ha="center",
        bbox=dict(boxstyle="round,pad=0.3", facecolor="wheat", alpha=0.5),
    )

    setup_axes(
        ax,
        xlabel=r"Time $t$",
        ylabel=r"Modal amplitude $|a_k(t)|$",
        title=f"Triad Activation -- {triad_label}",
    )
    ax.legend(fontsize=10, loc="upper right", framealpha=0.9)
    fig.tight_layout()

    fname = "triad_activation.png"
    fig.savefig(os.path.join(FIG_DIR, fname), dpi=300)
    plt.close(fig)
    print(f"  Saved: {fname}")


# ---------------------------------------------------------------------------
# Figure D: Dissipation Channels (Representative Run)
# ---------------------------------------------------------------------------
def figure_dissipation_channels(single_runs: dict, multi_runs: dict):
    """Plot dissipation channels for a representative run.

    Prefers the multi-mode run (richer dynamics). Falls back to
    the single-mode run with the lowest mode number.
    """
    # Pick a representative run
    rep_run = None
    rep_label = ""

    # Prefer multi-mode
    for (param_set, n_m), run in sorted(multi_runs.items()):
        rep_run = run
        rep_label = f"Set {param_set}, IC-B ($N_m = {n_m}$)"
        break

    # Fallback: first single-mode
    if rep_run is None:
        for (param_set, mode_n), run in sorted(single_runs.items()):
            rep_run = run
            rep_label = f"Set {param_set}, IC-A ($n = {mode_n}$)"
            break

    if rep_run is None:
        print("  SKIP: no runs available for dissipation plot.")
        return

    ts = rep_run["data"]
    t = ts["t"]

    fig, ax = plt.subplots(figsize=(9, 6))

    channels = [
        (r"Gradient $\mathcal{D}_{\mathrm{grad}}$", "D_gradient", "#2166ac", "-"),
        (r"Penalty $\mathcal{D}_{\mathrm{pen}}$",   "D_penalty",  "#b2182b", "-"),
        (r"Participation $\mathcal{D}_{\mathrm{part}}$", "D_participation", "#1b7837", "-"),
        (r"Total $\mathcal{D}$", "D_total", "black", "--"),
    ]

    plotted = False
    for label, field, color, ls in channels:
        if field in ts:
            data = ts[field]
            n = min(len(t), len(data))
            ax.semilogy(
                t[:n],
                np.maximum(data[:n], 1e-30),
                color=color,
                linestyle=ls,
                linewidth=1.5 if ls == "-" else 1.2,
                label=label,
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
        ylabel=r"Dissipation rate",
        title=f"Dissipation Channels -- {rep_label}",
    )
    ax.legend(fontsize=10, loc="upper right", framealpha=0.9)
    fig.tight_layout()

    fname = "dissipation_channels.png"
    fig.savefig(os.path.join(FIG_DIR, fname), dpi=300)
    plt.close(fig)
    print(f"  Saved: {fname}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    os.makedirs(FIG_DIR, exist_ok=True)

    print("Discovering modal-hierarchy runs...")
    single_runs, multi_runs = discover_runs()

    n_single = len(single_runs)
    n_multi = len(multi_runs)
    print(f"  Found {n_single} single-mode runs, {n_multi} multi-mode runs.")

    if n_single == 0 and n_multi == 0:
        print("\nERROR: No modal-hierarchy runs found in:")
        print(f"  {RUNS_DIR}")
        print("\nExpected directories matching:")
        print("  modal_single_{I,II,...}_n{k}")
        print("  modal_multi_{I,II,...}_Nm{N}")
        sys.exit(1)

    # List discovered runs
    if single_runs:
        print("\n  Single-mode runs:")
        for (ps, n), run in sorted(single_runs.items()):
            print(f"    Set {ps}, n = {n}: {run['name']}")
    if multi_runs:
        print("\n  Multi-mode runs:")
        for (ps, nm), run in sorted(multi_runs.items()):
            print(f"    Set {ps}, N_m = {nm}: {run['name']}")

    # Generate figures
    print("\n--- Figure A: Single-Mode Decay ---")
    figure_single_mode_decay(single_runs)

    print("\n--- Figure B: Modal Funnel ---")
    figure_modal_funnel(multi_runs)

    print("\n--- Figure C: Triad Activation ---")
    figure_triad_activation(single_runs, multi_runs)

    print("\n--- Figure D: Dissipation Channels ---")
    figure_dissipation_channels(single_runs, multi_runs)

    # Summary
    print(f"\nAll figures saved to: {FIG_DIR}")
    print("Done.")


if __name__ == "__main__":
    main()
