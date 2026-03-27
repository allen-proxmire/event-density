"""
analyze_overlap_cascade.py
===========================
Post-processing script for the Overlapping Triad Cascade experiment (Atlas §4).

Loads all overlap_cascade_IC* runs, classifies modes by their role in the
triad network (seeded / first-generation child / higher network), and produces
publication-quality figures showing the coupled energy-transfer pathways.

Figures produced:
  Per-IC:   Modal cascade with role-based styling (solid / dashed / dotted).
  Detail:   Two-panel parent/child anatomy for IC2 (the richest network).
  Compare:  Energy decay across all ICs.

All figures saved to output/figures/overlap_cascade/ as PNG (300 dpi).

Usage:
    python analyze_overlap_cascade.py

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
FIG_DIR = os.path.join(SCRIPT_DIR, "output", "figures", "overlap_cascade")

RE_IC = re.compile(r"^overlap_cascade_(IC\d+)$")

# A mode is "activated" if its peak amplitude exceeds this fraction of A^2
ACTIVATION_FRAC = 1e-4


# ---------------------------------------------------------------------------
# Color palette — deterministic per mode index
# ---------------------------------------------------------------------------
_PALETTE = [
    "#636363",  # 0  grey
    "#2166ac",  # 1  blue
    "#b2182b",  # 2  red
    "#1b7837",  # 3  green
    "#762a83",  # 4  purple
    "#e08214",  # 5  orange
    "#35978f",  # 6  teal
    "#bf812d",  # 7  brown
    "#d6604d",  # 8  salmon
    "#4393c3",  # 9  sky
    "#5aae61",  # 10 lime
    "#9970ab",  # 11 lavender
    "#f4a582",  # 12 peach
    "#92c5de",  # 13 ice
    "#66c2a5",  # 14 mint
    "#fc8d62",  # 15 coral
]


def mode_color(k: int) -> str:
    return _PALETTE[k % len(_PALETTE)]


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
# Triad network analysis
# ---------------------------------------------------------------------------
def pairwise_targets(modes: list) -> dict:
    """All unordered-pair triad targets: {(m,n): sorted([m+n, |m-n|])}."""
    targets = {}
    for i, m in enumerate(modes):
        for j, n in enumerate(modes):
            if j <= i:
                continue
            targets[(m, n)] = sorted({m + n, abs(m - n)})
    return targets


def classify_modes(seeded: list, modal: np.ndarray, A: float):
    """Classify every mode by its role in the triad network.

    Returns
    -------
    roles : dict  {mode_index: role_string}
        Possible roles:
          "seeded"       — in the initial condition
          "first_gen"    — direct pairwise target of two seeded modes
                           (i.e. a first-generation child)
          "network"      — activated but not seeded or first-gen
                           (second-generation or higher cascade product)
          "inactive"     — below threshold
    first_gen_set : set of int
    network_set   : set of int
    """
    seeded_set = set(seeded)
    tmap = pairwise_targets(seeded)

    # First-generation children: targets of seeded pairs, excluding seeds
    first_gen = set()
    for tlist in tmap.values():
        first_gen.update(tlist)
    first_gen -= seeded_set

    # Activated modes (peak > threshold)
    thresh = ACTIVATION_FRAC * A ** 2
    peak = np.max(np.abs(modal), axis=0)
    activated = set(k for k in range(modal.shape[1]) if peak[k] > thresh)

    # Network modes: activated but neither seeded nor first-gen
    network = activated - seeded_set - first_gen

    roles = {}
    for k in range(modal.shape[1]):
        if k in seeded_set:
            roles[k] = "seeded"
        elif k in first_gen and k in activated:
            roles[k] = "first_gen"
        elif k in network:
            roles[k] = "network"
        else:
            roles[k] = "inactive"

    return roles, first_gen, network


def triad_annotations(seeded: list, child_set: set) -> list:
    """Build human-readable triad-relation strings for child modes.

    Returns list of (target_mode, annotation_string) tuples.
    """
    tmap = pairwise_targets(seeded)
    annots = []
    seen = set()
    for (m, n), tlist in sorted(tmap.items()):
        for tgt in tlist:
            if tgt in child_set and tgt not in seen:
                if tgt == m + n:
                    annots.append((tgt, rf"${m}+{n}\to{tgt}$"))
                elif tgt == abs(m - n):
                    annots.append((tgt, rf"$|{m}-{n}|\to{tgt}$"))
                seen.add(tgt)
    return sorted(annots, key=lambda x: x[0])


# ---------------------------------------------------------------------------
# Styling
# ---------------------------------------------------------------------------
ROLE_STYLE = {
    "seeded":    {"ls": "-",  "lw": 2.0, "alpha": 1.0},
    "first_gen": {"ls": "--", "lw": 1.6, "alpha": 0.85},
    "network":   {"ls": ":",  "lw": 1.2, "alpha": 0.6},
}

ROLE_SUFFIX = {
    "seeded":    " (seeded)",
    "first_gen": " (1st-gen triad)",
    "network":   " (network)",
}


def setup_axes(ax, xlabel: str, ylabel: str, title: str):
    ax.set_xlabel(xlabel, fontsize=11)
    ax.set_ylabel(ylabel, fontsize=11)
    ax.set_title(title, fontsize=13, fontweight="bold")
    ax.tick_params(labelsize=10)
    ax.grid(True, alpha=0.3, linewidth=0.5)


# ---------------------------------------------------------------------------
# Figure 1 (per IC): modal cascade with role-based styling
# ---------------------------------------------------------------------------
def figure_per_ic(label: str, run: dict):
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

    roles, first_gen, network = classify_modes(seeded, modal[:n_snap], A_pm)

    # Modes to plot: everything that is not inactive
    modes_to_plot = sorted(k for k, r in roles.items() if r != "inactive")

    fig, ax = plt.subplots(figsize=(10, 6))

    for k in modes_to_plot:
        role = roles[k]
        sty = ROLE_STYLE[role]
        a_k = np.abs(modal[:n_snap, k])

        ax.semilogy(
            t[:n_snap],
            np.maximum(a_k, 1e-30),
            color=mode_color(k),
            linestyle=sty["ls"],
            linewidth=sty["lw"],
            alpha=sty["alpha"],
            label=rf"$|a_{{{k}}}|${ROLE_SUFFIX[role]}",
        )

    setup_axes(
        ax,
        xlabel=r"Time $t$",
        ylabel=r"Modal amplitude $|a_k(t)|$",
        title=f"Overlapping Triad Cascade — {label}: seeded {seeded}",
    )

    # Two-column legend to keep it compact
    handles, labels = ax.get_legend_handles_labels()
    ncol = 2 if len(handles) > 6 else 1
    ax.legend(fontsize=7.5, loc="upper right", framealpha=0.9, ncol=ncol)

    fig.tight_layout()
    fname = f"overlap_{label}.png"
    fig.savefig(os.path.join(FIG_DIR, fname), dpi=300)
    plt.close(fig)
    print(f"  Saved: {fname}")


# ---------------------------------------------------------------------------
# Figure 2: detail (two-panel parent / child anatomy)
# ---------------------------------------------------------------------------
def figure_detail(label: str, run: dict):
    ts = run["data"]
    meta = ts["metadata"]
    modal = ts.get("modal_amplitudes")

    if modal is None or modal.ndim != 2:
        print(f"  SKIP detail for {label}: no modal_amplitudes.")
        return

    seeded = meta.get("seeded_modes", [])
    A_pm = meta.get("A_per_mode", 0.05)
    t = ts["t"]
    n_snap = min(len(t), modal.shape[0])

    roles, first_gen, network = classify_modes(seeded, modal[:n_snap], A_pm)

    fig, (ax_top, ax_bot) = plt.subplots(
        2, 1, figsize=(10, 9), sharex=True,
        gridspec_kw={"hspace": 0.12},
    )

    # --- Top panel: seeded modes ---
    for k in sorted(seeded):
        if k >= modal.shape[1]:
            continue
        a_k = np.abs(modal[:n_snap, k])
        ax_top.semilogy(
            t[:n_snap],
            np.maximum(a_k, 1e-30),
            color=mode_color(k),
            linewidth=2.2,
            label=rf"$|a_{{{k}}}|$ (seeded)",
        )

    setup_axes(
        ax_top, xlabel="",
        ylabel=r"$|a_k(t)|$",
        title=f"Overlap Cascade Detail — {label}: seeded {seeded}",
    )
    ax_top.legend(fontsize=10, loc="upper right", framealpha=0.9)

    # --- Bottom panel: first-gen children + network, with annotations ---
    # Faint reference of seeded modes
    for k in sorted(seeded):
        if k >= modal.shape[1]:
            continue
        a_k = np.abs(modal[:n_snap, k])
        ax_bot.semilogy(
            t[:n_snap], np.maximum(a_k, 1e-30),
            color=mode_color(k), linewidth=0.7, alpha=0.25, linestyle=":",
        )

    # First-gen children
    child_set = set()
    for k in sorted(first_gen):
        if k >= modal.shape[1]:
            continue
        if roles.get(k) == "inactive":
            continue
        a_k = np.abs(modal[:n_snap, k])
        ax_bot.semilogy(
            t[:n_snap], np.maximum(a_k, 1e-30),
            color=mode_color(k), linewidth=2.0, linestyle="--", alpha=0.85,
            label=rf"$|a_{{{k}}}|$ (1st-gen)",
        )
        child_set.add(k)

    # Network modes
    for k in sorted(network):
        if k >= modal.shape[1]:
            continue
        a_k = np.abs(modal[:n_snap, k])
        ax_bot.semilogy(
            t[:n_snap], np.maximum(a_k, 1e-30),
            color=mode_color(k), linewidth=1.3, linestyle=":", alpha=0.6,
            label=rf"$|a_{{{k}}}|$ (network)",
        )

    # Annotation box: triad relations for first-gen children
    all_children = child_set | network
    annots = triad_annotations(seeded, first_gen | network)
    if annots:
        lines = ["Triad relations:"]
        for tgt, text in annots:
            # Mark feedback targets
            if tgt in set(seeded):
                text += r" $\circlearrowleft$"
            lines.append(f"  {text}")
        annotation_text = "\n".join(lines)

        ax_bot.text(
            0.02, 0.05,
            annotation_text,
            transform=ax_bot.transAxes,
            fontsize=8.5,
            verticalalignment="bottom",
            fontfamily="monospace",
            bbox=dict(
                boxstyle="round,pad=0.4",
                facecolor="wheat", alpha=0.7, edgecolor="0.6",
            ),
        )

    # Feedback annotation on seeded modes that are also triad targets
    overlap_info = meta.get("overlap_analysis", {})
    feedback = overlap_info.get("feedback_targets", [])
    if feedback:
        fb_text = "Feedback modes (seeded & target): " + ", ".join(
            str(k) for k in feedback
        )
        ax_bot.text(
            0.98, 0.95, fb_text,
            transform=ax_bot.transAxes,
            fontsize=8, ha="right", va="top",
            fontstyle="italic", color="#b2182b",
            bbox=dict(boxstyle="round,pad=0.3",
                      facecolor="#fddbc7", alpha=0.7, edgecolor="#b2182b"),
        )

    setup_axes(
        ax_bot,
        xlabel=r"Time $t$",
        ylabel=r"$|a_k(t)|$",
        title="Triad Children and Network Modes",
    )
    handles, labels_leg = ax_bot.get_legend_handles_labels()
    ncol = 2 if len(handles) > 5 else 1
    ax_bot.legend(fontsize=8, loc="upper right", framealpha=0.9, ncol=ncol)

    fig.tight_layout()
    fname = f"overlap_detail_{label}.png"
    fig.savefig(os.path.join(FIG_DIR, fname), dpi=300)
    plt.close(fig)
    print(f"  Saved: {fname}")


# ---------------------------------------------------------------------------
# Figure 3: energy comparison across ICs
# ---------------------------------------------------------------------------
def figure_energy_comparison(runs: dict):
    fig, ax = plt.subplots(figsize=(9, 5))

    ic_colors = {"IC1": "#2166ac", "IC2": "#b2182b", "IC3": "#1b7837",
                 "IC4": "#762a83", "IC5": "#e08214"}
    ic_styles = {"IC1": "-", "IC2": "--", "IC3": "-.", "IC4": ":", "IC5": "-"}

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
            label=f"{label}: {seeded}",
        )

    setup_axes(
        ax,
        xlabel=r"Time $t$",
        ylabel=r"Energy $\mathcal{E}(t)$",
        title="Overlapping Triad Cascade — Energy Decay Comparison",
    )
    ax.legend(fontsize=10, loc="upper right", framealpha=0.9)
    fig.tight_layout()

    fname = "overlap_energy_comparison.png"
    fig.savefig(os.path.join(FIG_DIR, fname), dpi=300)
    plt.close(fig)
    print(f"  Saved: {fname}")


# ---------------------------------------------------------------------------
# Figure 4: complexity comparison across ICs
# ---------------------------------------------------------------------------
def figure_complexity_comparison(runs: dict):
    fig, ax = plt.subplots(figsize=(9, 5))

    ic_colors = {"IC1": "#2166ac", "IC2": "#b2182b", "IC3": "#1b7837",
                 "IC4": "#762a83", "IC5": "#e08214"}
    ic_styles = {"IC1": "-", "IC2": "--", "IC3": "-.", "IC4": ":", "IC5": "-"}

    for label, run in sorted(runs.items()):
        ts = run["data"]
        meta = ts["metadata"]
        seeded = meta.get("seeded_modes", [])
        t = ts["t"]
        C = ts.get("C_ED")
        if C is None:
            continue
        n = min(len(t), len(C))

        ax.semilogy(
            t[:n], C[:n],
            color=ic_colors.get(label, "0.3"),
            linestyle=ic_styles.get(label, "-"),
            linewidth=1.5,
            label=f"{label}: {seeded}",
        )

    setup_axes(
        ax,
        xlabel=r"Time $t$",
        ylabel=r"$C_{\mathrm{ED}}(t)$",
        title="Overlapping Triad Cascade — Complexity Decay Comparison",
    )
    ax.legend(fontsize=10, loc="upper right", framealpha=0.9)
    fig.tight_layout()

    fname = "overlap_complexity_comparison.png"
    fig.savefig(os.path.join(FIG_DIR, fname), dpi=300)
    plt.close(fig)
    print(f"  Saved: {fname}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    os.makedirs(FIG_DIR, exist_ok=True)

    print("Discovering overlap cascade runs...")
    runs = discover_runs()

    if not runs:
        print(f"\nERROR: No overlap_cascade_IC* runs found in:")
        print(f"  {RUNS_DIR}")
        print("\nRun the experiment first:")
        print("  python experiments/overlap_cascade.py")
        sys.exit(1)

    print(f"  Found {len(runs)} runs:")
    for label, run in runs.items():
        meta = run["data"]["metadata"]
        seeded = meta.get("seeded_modes", "?")
        overlap = meta.get("overlap_analysis", {})
        novel = overlap.get("novel_targets", [])
        feedback = overlap.get("feedback_targets", [])
        print(f"    {label}: seeded={seeded}, novel={novel}, feedback={feedback}")

    # --- Per-IC cascade figures ---
    print("\n--- Per-IC Modal Cascade Figures ---")
    for label, run in runs.items():
        figure_per_ic(label, run)

    # --- Detail figure for IC2 (richest network), fallback to first available ---
    print("\n--- Detail Figure (parent/child/network anatomy) ---")
    detail_label = "IC2" if "IC2" in runs else next(iter(runs))
    figure_detail(detail_label, runs[detail_label])

    # If IC3 is also available, produce a second detail
    if "IC3" in runs and detail_label != "IC3":
        figure_detail("IC3", runs["IC3"])

    # --- Energy comparison ---
    print("\n--- Energy Comparison ---")
    figure_energy_comparison(runs)

    # --- Complexity comparison ---
    print("\n--- Complexity Comparison ---")
    figure_complexity_comparison(runs)

    # --- Summary table ---
    print(f"\n{'='*78}")
    print("  Overlap Cascade Analysis Summary")
    print(f"{'='*78}")
    print(f"  {'IC':<6} {'Seeded':<16} {'1st-gen':<16} {'Network':<14} "
          f"{'Feedback':<12}")
    print("  " + "-" * 64)

    for label, run in sorted(runs.items()):
        ts = run["data"]
        meta = ts["metadata"]
        seeded = meta.get("seeded_modes", [])
        A_pm = meta.get("A_per_mode", 0.05)
        modal = ts.get("modal_amplitudes")

        if modal is not None and modal.ndim == 2:
            n_snap = min(len(ts["t"]), modal.shape[0])
            roles, fg, nw = classify_modes(seeded, modal[:n_snap], A_pm)
            fg_active = sorted(k for k in fg
                               if roles.get(k) in ("first_gen",))
            nw_active = sorted(nw)
        else:
            fg_active = []
            nw_active = []

        overlap = meta.get("overlap_analysis", {})
        feedback = overlap.get("feedback_targets", [])

        print(f"  {label:<6} {str(seeded):<16} {str(fg_active):<16} "
              f"{str(nw_active) if nw_active else '—':<14} "
              f"{str(feedback) if feedback else '—':<12}")

    print(f"\nAll figures saved to: {FIG_DIR}")
    print("Done.")


if __name__ == "__main__":
    main()
