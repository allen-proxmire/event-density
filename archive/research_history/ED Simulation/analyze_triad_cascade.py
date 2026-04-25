"""
analyze_triad_cascade.py
=========================
Post-processing script for the Triad Cascade experiment (Atlas §4).

Loads all triad_cascade_IC* runs, extracts modal amplitude time series,
and produces publication-quality figures showing:

  Per-IC figures:   |a_k(t)| for all activated modes, with triad-generated
                    modes highlighted as dashed lines.
  Detail figure:    For IC1 ({1,2}), a two-panel layout showing parent modes
                    (solid) and child modes (dashed) with annotated triad
                    relations.

All figures saved to output/figures/triad_cascade/ as PNG (300 dpi).

Usage:
    python analyze_triad_cascade.py

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
FIG_DIR = os.path.join(SCRIPT_DIR, "output", "figures", "triad_cascade")

RE_IC = re.compile(r"^triad_cascade_(IC\d+)$")

# Activation threshold: a mode is considered "activated" if its peak
# amplitude exceeds this fraction of the seeded per-mode amplitude squared.
ACTIVATION_FRAC = 1e-4

# Visual config
PARENT_COLORS = {
    0: "#636363", 1: "#2166ac", 2: "#b2182b", 3: "#1b7837",
    4: "#762a83", 5: "#e08214", 6: "#35978f", 7: "#bf812d",
}
CHILD_ALPHA = 0.85


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def load_run(run_dir: str) -> dict | None:
    """Load time_series.npz and metadata.json."""
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
    """Find all triad_cascade_IC* directories.

    Returns dict {label: {"dir", "data"}} sorted by label.
    """
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


def triad_targets(seeded: list[int]) -> dict:
    """Compute all pairwise triad-predicted target modes.

    Returns {(m,n): [target1, target2]} for each unordered pair.
    """
    targets = {}
    for i, m in enumerate(seeded):
        for j, n in enumerate(seeded):
            if j <= i:
                continue
            targets[(m, n)] = sorted({m + n, abs(m - n)})
    return targets


def all_child_modes(seeded: list[int]) -> set[int]:
    """Set of all triad-generated modes (excluding the parents)."""
    children = set()
    for pair_targets in triad_targets(seeded).values():
        children.update(pair_targets)
    children -= set(seeded)
    return children


def activated_modes(modal: np.ndarray, seeded: list[int],
                    A: float) -> list[int]:
    """Return sorted list of mode indices whose peak amplitude exceeds
    the activation threshold, excluding seeded modes."""
    thresh = ACTIVATION_FRAC * A ** 2
    peak = np.max(np.abs(modal), axis=0)
    seeded_set = set(seeded)
    return sorted(
        k for k in range(modal.shape[1])
        if peak[k] > thresh and k not in seeded_set
    )


def mode_color(k: int) -> str:
    """Deterministic color for mode k."""
    if k in PARENT_COLORS:
        return PARENT_COLORS[k]
    # Cycle through a secondary palette for higher modes
    secondary = ["#d6604d", "#4393c3", "#5aae61", "#9970ab",
                  "#f4a582", "#92c5de", "#66c2a5", "#fc8d62"]
    return secondary[k % len(secondary)]


def setup_axes(ax, xlabel: str, ylabel: str, title: str):
    ax.set_xlabel(xlabel, fontsize=11)
    ax.set_ylabel(ylabel, fontsize=11)
    ax.set_title(title, fontsize=13, fontweight="bold")
    ax.tick_params(labelsize=10)
    ax.grid(True, alpha=0.3, linewidth=0.5)


# ---------------------------------------------------------------------------
# Per-IC figure: all activated modes
# ---------------------------------------------------------------------------
def figure_per_ic(label: str, run: dict):
    """Semilog-y plot of |a_k(t)| for all activated modes.

    Seeded (parent) modes drawn solid; triad-generated (child) modes dashed.
    """
    ts = run["data"]
    meta = ts["metadata"]
    modal = ts.get("modal_amplitudes")

    if modal is None or modal.ndim != 2:
        print(f"  SKIP {label}: no modal_amplitudes.")
        return

    seeded = meta.get("seeded_modes", [])
    A_pm = meta.get("A_per_mode", 0.05)
    t = ts["t"]
    n_snap = min(len(t), modal.shape[0])

    children = all_child_modes(seeded)
    active = activated_modes(modal[:n_snap], seeded, A_pm)

    # Combine: seeded + children + any other activated modes
    modes_to_plot = sorted(set(seeded) | children | set(active))

    fig, ax = plt.subplots(figsize=(9, 6))

    for k in modes_to_plot:
        if k >= modal.shape[1]:
            continue

        a_k = np.abs(modal[:n_snap, k])
        is_parent = k in seeded
        is_child = k in children

        ls = "-" if is_parent else "--" if is_child else ":"
        lw = 1.8 if is_parent else 1.5 if is_child else 1.0
        alpha = 1.0 if is_parent else CHILD_ALPHA if is_child else 0.5

        suffix = ""
        if is_parent:
            suffix = " (seeded)"
        elif is_child:
            suffix = " (triad)"

        ax.semilogy(
            t[:n_snap],
            np.maximum(a_k, 1e-30),
            color=mode_color(k),
            linestyle=ls,
            linewidth=lw,
            alpha=alpha,
            label=rf"$|a_{{{k}}}|${suffix}",
        )

    setup_axes(
        ax,
        xlabel=r"Time $t$",
        ylabel=r"Modal amplitude $|a_k(t)|$",
        title=f"Triad Cascade -- {label}: seeded modes {seeded}",
    )
    ax.legend(fontsize=8, loc="upper right", framealpha=0.9, ncol=2)
    fig.tight_layout()

    fname = f"cascade_{label}.png"
    fig.savefig(os.path.join(FIG_DIR, fname), dpi=300)
    plt.close(fig)
    print(f"  Saved: {fname}")


# ---------------------------------------------------------------------------
# Detail figure: parent vs child with triad annotations (IC1)
# ---------------------------------------------------------------------------
def figure_detail(label: str, run: dict):
    """Two-panel figure for a single IC showing triad anatomy.

    Top panel:  parent (seeded) modes -- solid lines.
    Bottom panel: child (triad-generated) modes -- dashed lines,
                  with annotations of the triad relations.
    """
    ts = run["data"]
    meta = ts["metadata"]
    modal = ts.get("modal_amplitudes")

    if modal is None or modal.ndim != 2:
        print(f"  SKIP detail for {label}: no modal_amplitudes.")
        return

    seeded = meta.get("seeded_modes", [])
    t = ts["t"]
    n_snap = min(len(t), modal.shape[0])

    children = all_child_modes(seeded)
    targets = triad_targets(seeded)

    fig, (ax_top, ax_bot) = plt.subplots(
        2, 1, figsize=(9, 8), sharex=True,
        gridspec_kw={"hspace": 0.15},
    )

    # --- Top panel: parent modes ---
    for k in sorted(seeded):
        if k >= modal.shape[1]:
            continue
        a_k = np.abs(modal[:n_snap, k])
        ax_top.semilogy(
            t[:n_snap],
            np.maximum(a_k, 1e-30),
            color=mode_color(k),
            linewidth=2.0,
            label=rf"$|a_{{{k}}}|$ (seeded)",
        )

    setup_axes(
        ax_top,
        xlabel="",
        ylabel=r"$|a_k(t)|$",
        title=f"Triad Cascade Detail -- {label}: seeded modes {seeded}",
    )
    ax_top.legend(fontsize=10, loc="upper right", framealpha=0.9)

    # --- Bottom panel: child modes + annotations ---
    # Also plot parents as faint reference
    for k in sorted(seeded):
        if k >= modal.shape[1]:
            continue
        a_k = np.abs(modal[:n_snap, k])
        ax_bot.semilogy(
            t[:n_snap],
            np.maximum(a_k, 1e-30),
            color=mode_color(k),
            linewidth=0.8,
            alpha=0.3,
            linestyle=":",
        )

    child_labels_plotted = set()
    for k in sorted(children):
        if k >= modal.shape[1]:
            continue
        a_k = np.abs(modal[:n_snap, k])
        ax_bot.semilogy(
            t[:n_snap],
            np.maximum(a_k, 1e-30),
            color=mode_color(k),
            linewidth=2.0,
            linestyle="--",
            alpha=CHILD_ALPHA,
            label=rf"$|a_{{{k}}}|$ (triad-generated)",
        )
        child_labels_plotted.add(k)

    # Build annotation strings from triad relations
    annotations = []
    for (m, n), tgt_list in sorted(targets.items()):
        for tgt in tgt_list:
            if tgt in children:
                if tgt == m + n:
                    annotations.append(rf"${m}+{n}\to{tgt}$")
                elif tgt == abs(m - n):
                    annotations.append(rf"$|{m}-{n}|\to{tgt}$")

    if annotations:
        annotation_text = "Triad rules:\n" + "\n".join(annotations)
        ax_bot.text(
            0.02, 0.05,
            annotation_text,
            transform=ax_bot.transAxes,
            fontsize=9,
            verticalalignment="bottom",
            fontfamily="monospace",
            bbox=dict(
                boxstyle="round,pad=0.4",
                facecolor="wheat",
                alpha=0.7,
                edgecolor="0.6",
            ),
        )

    setup_axes(
        ax_bot,
        xlabel=r"Time $t$",
        ylabel=r"$|a_k(t)|$",
        title="Triad-Generated Modes",
    )
    ax_bot.legend(fontsize=10, loc="upper right", framealpha=0.9)

    fig.tight_layout()
    fname = f"cascade_detail_{label}.png"
    fig.savefig(os.path.join(FIG_DIR, fname), dpi=300)
    plt.close(fig)
    print(f"  Saved: {fname}")


# ---------------------------------------------------------------------------
# Comparison figure: energy across all ICs
# ---------------------------------------------------------------------------
def figure_energy_comparison(runs: dict):
    """Single plot of E(t) for all ICs on semilog-y."""
    fig, ax = plt.subplots(figsize=(9, 5))

    ic_colors = {"IC1": "#2166ac", "IC2": "#b2182b", "IC3": "#1b7837", "IC4": "#762a83"}
    ic_styles = {"IC1": "-", "IC2": "--", "IC3": "-.", "IC4": ":"}

    for label, run in sorted(runs.items()):
        ts = run["data"]
        meta = ts["metadata"]
        seeded = meta.get("seeded_modes", [])
        t = ts["t"]
        E = ts["E_total"]
        n = min(len(t), len(E))

        ax.semilogy(
            t[:n], E[:n],
            color=ic_colors.get(label, "0.3"),
            linestyle=ic_styles.get(label, "-"),
            linewidth=1.5,
            label=f"{label}: modes {seeded}",
        )

    setup_axes(
        ax,
        xlabel=r"Time $t$",
        ylabel=r"Energy $\mathcal{E}(t)$",
        title="Triad Cascade -- Energy Decay Comparison",
    )
    ax.legend(fontsize=10, loc="upper right", framealpha=0.9)
    fig.tight_layout()

    fname = "cascade_energy_comparison.png"
    fig.savefig(os.path.join(FIG_DIR, fname), dpi=300)
    plt.close(fig)
    print(f"  Saved: {fname}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    os.makedirs(FIG_DIR, exist_ok=True)

    print("Discovering triad cascade runs...")
    runs = discover_runs()

    if not runs:
        print(f"\nERROR: No triad_cascade_IC* runs found in:")
        print(f"  {RUNS_DIR}")
        print("\nRun the experiment first:")
        print("  python experiments/triad_cascade.py")
        sys.exit(1)

    print(f"  Found {len(runs)} runs:")
    for label, run in runs.items():
        meta = run["data"]["metadata"]
        seeded = meta.get("seeded_modes", "?")
        print(f"    {label}: seeded modes = {seeded}")

    # --- Per-IC figures ---
    print("\n--- Per-IC Modal Cascade Figures ---")
    for label, run in runs.items():
        figure_per_ic(label, run)

    # --- Detail figure for IC1 (or first available) ---
    print("\n--- Detail Figure (parent/child anatomy) ---")
    detail_label = "IC1" if "IC1" in runs else next(iter(runs))
    figure_detail(detail_label, runs[detail_label])

    # --- Energy comparison ---
    print("\n--- Energy Comparison ---")
    figure_energy_comparison(runs)

    # --- Summary table ---
    print(f"\n{'='*70}")
    print("  Triad Cascade Analysis Summary")
    print(f"{'='*70}")
    print(f"  {'IC':<6} {'Seeded':<12} {'Children':<16} {'Active (other)':<16}")
    print("  " + "-" * 50)

    for label, run in sorted(runs.items()):
        ts = run["data"]
        meta = ts["metadata"]
        seeded = meta.get("seeded_modes", [])
        modal = ts.get("modal_amplitudes")
        A_pm = meta.get("A_per_mode", 0.05)

        children = sorted(all_child_modes(seeded))
        if modal is not None and modal.ndim == 2:
            n_snap = min(len(ts["t"]), modal.shape[0])
            active = activated_modes(modal[:n_snap], seeded, A_pm)
            other = sorted(set(active) - set(children))
        else:
            other = []

        print(f"  {label:<6} {str(seeded):<12} {str(children):<16} "
              f"{str(other) if other else '--':<16}")

    print(f"\nAll figures saved to: {FIG_DIR}")
    print("Done.")


if __name__ == "__main__":
    main()
