"""
analyze_three_stage_I.py
========================
Post-processing script for the Three-Stage Convergence experiment, Parameter Set I.

Loads the three complexity runs (low, medium, high), extracts diagnostics from
the time_series.npz files, and produces four publication-quality figures:

  Figure 1:  Energy vs time (all three amplitudes, log-y)
  Figure 2:  ED-complexity vs time (all three, log-y, with stage transitions)
  Figure 3:  Dissipation channels vs time (medium case)
  Figure 4:  Modal amplitudes vs time (medium case, first 6 modes)

All figures saved to output/figures/three_stage_I/ as PNG (300 dpi).

Usage:
    python analyze_three_stage_I.py

Requires: numpy, matplotlib.
"""

import os
import sys
import json
import numpy as np
import matplotlib
matplotlib.use("Agg")  # Non-interactive backend
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
RUNS_DIR = os.path.join(SCRIPT_DIR, "output", "runs")
FIG_DIR = os.path.join(SCRIPT_DIR, "output", "figures", "three_stage_I")

RUN_NAMES = {
    "low":    "three_stage_I_low",
    "medium": "three_stage_I_medium",
    "high":   "three_stage_I_high",
}

LABELS = {
    "low":    r"Low ($A = 0.01$)",
    "medium": r"Medium ($A = 0.1$)",
    "high":   r"High ($A = 0.3$)",
}

COLORS = {
    "low":    "#2166ac",   # blue
    "medium": "#b2182b",   # red
    "high":   "#1b7837",   # green
}

LINE_STYLES = {
    "low":    "-",
    "medium": "--",
    "high":   "-.",
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def load_run(name: str) -> dict:
    """Load time_series.npz and metadata.json for a named run.

    Returns a dict with numpy arrays and metadata fields.
    """
    run_dir = os.path.join(RUNS_DIR, name)
    if not os.path.isdir(run_dir):
        print(f"ERROR: run directory not found: {run_dir}")
        sys.exit(1)

    # Time series
    ts_path = os.path.join(run_dir, "time_series.npz")
    if not os.path.isfile(ts_path):
        print(f"ERROR: time_series.npz not found in {run_dir}")
        sys.exit(1)
    ts = dict(np.load(ts_path, allow_pickle=True))

    # Metadata
    meta_path = os.path.join(run_dir, "metadata.json")
    meta = {}
    if os.path.isfile(meta_path):
        with open(meta_path, "r") as f:
            meta = json.load(f)

    ts["metadata"] = meta
    return ts


def detect_stage_transitions(t: np.ndarray, E: np.ndarray) -> dict:
    """Heuristic detection of the three convergence stages.

    Stage I   (global bounds):  E decays but not yet algebraically.
    Stage II  (algebraic decay): E ~ t^{-p} on a log-log plot.
    Stage III (exponential decay): E ~ exp(-sigma * t) on a semilog plot.

    Returns dict with keys 't_I_II' and 't_II_III' (or None if not detected).

    Detection method:
      - Compute the instantaneous logarithmic decay rate: r(t) = -d(log E)/dt.
      - Stage III begins when r(t) stabilises (std over a window < threshold).
      - Stage I/II boundary is the first time the energy drops below 50% of its
        initial value (a simple heuristic for the global-bound phase ending).
    """
    result = {"t_I_II": None, "t_II_III": None}

    # Require at least 50 points
    if len(t) < 50 or len(E) < 50:
        return result

    # Clip energy to positive values for log
    E_pos = np.maximum(E, 1e-30)
    log_E = np.log(E_pos)

    # --- Stage I → II: energy drops below 50% of E(0) ---
    E0 = E_pos[0]
    idx_half = np.where(E_pos < 0.5 * E0)[0]
    if len(idx_half) > 0:
        result["t_I_II"] = t[idx_half[0]]

    # --- Stage II → III: instantaneous rate stabilises ---
    # Compute rate via finite differences
    dt_arr = np.diff(t)
    dt_arr[dt_arr == 0] = 1e-30
    rate = -np.diff(log_E) / dt_arr

    # Sliding window standard deviation
    win = max(len(rate) // 20, 10)
    if len(rate) < 2 * win:
        return result

    rate_std = np.array([
        np.std(rate[max(0, i - win):i + 1])
        for i in range(len(rate))
    ])

    # Median rate in the last quarter as the "stable" reference
    last_quarter = rate[3 * len(rate) // 4:]
    if len(last_quarter) == 0:
        return result
    median_rate = np.median(last_quarter)

    if median_rate <= 0:
        return result

    # Threshold: rate_std < 10% of median rate
    threshold = 0.10 * abs(median_rate)
    stable_idx = np.where(rate_std < threshold)[0]

    if len(stable_idx) > 0:
        # First time the rate becomes stable -- that's the start of Stage III
        idx = stable_idx[0]
        # Only accept if it's after Stage I→II
        t_candidate = 0.5 * (t[idx] + t[min(idx + 1, len(t) - 1)])
        if result["t_I_II"] is not None and t_candidate > result["t_I_II"]:
            result["t_II_III"] = t_candidate
        elif result["t_I_II"] is None:
            result["t_II_III"] = t_candidate

    return result


def setup_axes(ax, xlabel: str, ylabel: str, title: str):
    """Standard axis formatting."""
    ax.set_xlabel(xlabel, fontsize=11)
    ax.set_ylabel(ylabel, fontsize=11)
    ax.set_title(title, fontsize=13, fontweight="bold")
    ax.tick_params(labelsize=10)
    ax.grid(True, alpha=0.3, linewidth=0.5)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    # Ensure output directory exists
    os.makedirs(FIG_DIR, exist_ok=True)

    # Load all three runs
    print("Loading runs...")
    runs = {}
    for key, name in RUN_NAMES.items():
        print(f"  {key}: {name}")
        runs[key] = load_run(name)

    # -----------------------------------------------------------------------
    # Figure 1: Energy vs time (all three, log-y)
    # -----------------------------------------------------------------------
    print("Generating Figure 1: Energy vs time...")
    fig1, ax1 = plt.subplots(figsize=(8, 5))

    for key in ("low", "medium", "high"):
        ts = runs[key]
        t = ts["t"]
        E = ts["E_total"]
        ax1.semilogy(
            t, E,
            color=COLORS[key],
            linestyle=LINE_STYLES[key],
            linewidth=1.5,
            label=LABELS[key],
        )

    setup_axes(
        ax1,
        xlabel=r"Time $t$",
        ylabel=r"Energy $\mathcal{E}(t)$",
        title="Three-Stage Convergence, Set I -- Energy Decay",
    )
    ax1.legend(fontsize=10, loc="upper right", framealpha=0.9)
    fig1.tight_layout()
    fig1.savefig(os.path.join(FIG_DIR, "energy_vs_time.png"), dpi=300)
    plt.close(fig1)
    print("  Saved: energy_vs_time.png")

    # -----------------------------------------------------------------------
    # Figure 2: Complexity vs time (all three, log-y, with transitions)
    # -----------------------------------------------------------------------
    print("Generating Figure 2: Complexity vs time...")
    fig2, ax2 = plt.subplots(figsize=(8, 5))

    for key in ("low", "medium", "high"):
        ts = runs[key]
        t = ts["t"]
        C = ts["C_ED"]
        ax2.semilogy(
            t, C,
            color=COLORS[key],
            linestyle=LINE_STYLES[key],
            linewidth=1.5,
            label=LABELS[key],
        )

        # Detect and mark stage transitions
        E = ts["E_total"]
        transitions = detect_stage_transitions(t, E)

        if transitions["t_I_II"] is not None:
            ax2.axvline(
                transitions["t_I_II"],
                color=COLORS[key],
                linestyle=":",
                linewidth=0.8,
                alpha=0.6,
            )
        if transitions["t_II_III"] is not None:
            ax2.axvline(
                transitions["t_II_III"],
                color=COLORS[key],
                linestyle=":",
                linewidth=0.8,
                alpha=0.6,
            )

    # Add stage labels at the top
    # Use the medium run's transitions for label placement
    E_med = runs["medium"]["E_total"]
    t_med = runs["medium"]["t"]
    trans_med = detect_stage_transitions(t_med, E_med)

    y_top = ax2.get_ylim()[1]
    label_y = y_top * 0.5

    if trans_med["t_I_II"] is not None and trans_med["t_II_III"] is not None:
        t1 = trans_med["t_I_II"]
        t2 = trans_med["t_II_III"]
        t_max = t_med[-1]

        ax2.text(
            0.5 * t1, label_y, "Stage I",
            ha="center", va="top", fontsize=9, fontstyle="italic", color="0.4",
        )
        ax2.text(
            0.5 * (t1 + t2), label_y, "Stage II",
            ha="center", va="top", fontsize=9, fontstyle="italic", color="0.4",
        )
        ax2.text(
            0.5 * (t2 + t_max), label_y, "Stage III",
            ha="center", va="top", fontsize=9, fontstyle="italic", color="0.4",
        )

    setup_axes(
        ax2,
        xlabel=r"Time $t$",
        ylabel=r"ED-Complexity $C_{\mathrm{ED}}(t)$",
        title="Three-Stage Convergence, Set I -- Complexity Decay",
    )
    ax2.legend(fontsize=10, loc="upper right", framealpha=0.9)
    fig2.tight_layout()
    fig2.savefig(os.path.join(FIG_DIR, "complexity_vs_time.png"), dpi=300)
    plt.close(fig2)
    print("  Saved: complexity_vs_time.png")

    # -----------------------------------------------------------------------
    # Figure 3: Dissipation channels vs time (medium case)
    # -----------------------------------------------------------------------
    print("Generating Figure 3: Dissipation channels (medium)...")
    fig3, ax3 = plt.subplots(figsize=(8, 5))

    ts_med = runs["medium"]
    t = ts_med["t"]

    channels = {
        r"Gradient $\mathcal{D}_{\mathrm{grad}}$": ("D_gradient", "#2166ac"),
        r"Penalty $\mathcal{D}_{\mathrm{pen}}$":   ("D_penalty",  "#b2182b"),
        r"Participation $\mathcal{D}_{\mathrm{part}}$": ("D_participation", "#1b7837"),
    }

    for label, (field, color) in channels.items():
        if field in ts_med:
            D_chan = ts_med[field]
            ax3.semilogy(
                t, np.maximum(D_chan, 1e-30),
                color=color,
                linewidth=1.5,
                label=label,
            )

    # Total dissipation (dashed black)
    if "D_total" in ts_med:
        ax3.semilogy(
            t, np.maximum(ts_med["D_total"], 1e-30),
            color="black",
            linestyle="--",
            linewidth=1.2,
            label=r"Total $\mathcal{D}$",
            alpha=0.7,
        )

    setup_axes(
        ax3,
        xlabel=r"Time $t$",
        ylabel=r"Dissipation rate",
        title=r"Three-Stage Convergence, Set I -- Dissipation Channels ($A = 0.1$)",
    )
    ax3.legend(fontsize=10, loc="upper right", framealpha=0.9)
    fig3.tight_layout()
    fig3.savefig(os.path.join(FIG_DIR, "dissipation_channels_medium.png"), dpi=300)
    plt.close(fig3)
    print("  Saved: dissipation_channels_medium.png")

    # -----------------------------------------------------------------------
    # Figure 4: Modal amplitudes vs time (medium case, first 6 modes)
    # -----------------------------------------------------------------------
    print("Generating Figure 4: Modal amplitudes (medium)...")
    fig4, ax4 = plt.subplots(figsize=(8, 5))

    if "modal_amplitudes" in ts_med:
        modal = ts_med["modal_amplitudes"]  # shape: (n_snapshots, N_obs)
        n_snapshots, n_modes_available = modal.shape
        n_modes_plot = min(6, n_modes_available)

        mode_colors = plt.cm.viridis(np.linspace(0.1, 0.9, n_modes_plot))

        for k in range(n_modes_plot):
            a_k = np.abs(modal[:, k])
            ax4.semilogy(
                t[:n_snapshots], np.maximum(a_k, 1e-30),
                color=mode_colors[k],
                linewidth=1.3,
                label=rf"$|a_{{{k}}}|$",
            )

        setup_axes(
            ax4,
            xlabel=r"Time $t$",
            ylabel=r"Modal amplitude $|a_k(t)|$",
            title=r"Three-Stage Convergence, Set I -- Modal Amplitudes ($A = 0.1$)",
        )
        ax4.legend(fontsize=9, loc="upper right", framealpha=0.9, ncol=2)
    else:
        ax4.text(
            0.5, 0.5,
            "Modal amplitude data not available\n(modal_amplitudes not found in time_series.npz)",
            ha="center", va="center",
            fontsize=12, color="0.5",
            transform=ax4.transAxes,
        )
        setup_axes(
            ax4,
            xlabel=r"Time $t$",
            ylabel=r"Modal amplitude $|a_k(t)|$",
            title=r"Three-Stage Convergence, Set I -- Modal Amplitudes ($A = 0.1$)",
        )

    fig4.tight_layout()
    fig4.savefig(os.path.join(FIG_DIR, "modal_amplitudes_medium.png"), dpi=300)
    plt.close(fig4)
    print("  Saved: modal_amplitudes_medium.png")

    # -----------------------------------------------------------------------
    # Summary
    # -----------------------------------------------------------------------
    print(f"\nAll figures saved to: {FIG_DIR}")
    print("  1. energy_vs_time.png")
    print("  2. complexity_vs_time.png")
    print("  3. dissipation_channels_medium.png")
    print("  4. modal_amplitudes_medium.png")

    # Print run metadata summary
    print("\nRun summaries:")
    for key in ("low", "medium", "high"):
        meta = runs[key].get("metadata", {})
        print(f"  {key}:")
        print(f"    termination: {meta.get('termination_reason', 'N/A')}")
        print(f"    steps:       {meta.get('n_steps', 'N/A')}")
        print(f"    wall time:   {meta.get('wall_time_s', 'N/A'):.1f} s"
              if isinstance(meta.get('wall_time_s'), (int, float))
              else f"    wall time:   N/A")
        print(f"    final t:     {meta.get('final_t', 'N/A')}")


if __name__ == "__main__":
    main()
