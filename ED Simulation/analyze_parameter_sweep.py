"""
analyze_parameter_sweep.py
===========================
Post-processing script for the Diffusion-Coefficient Sweep experiment
(Atlas §8.3, Suite §4.1).

Loads all param_D* runs and produces:

  Per-D figures:
    (A) Modal funnel -- |a_k(t)| colored by k, annotated with decay ordering.

  Cross-D figures:
    (B) Energy and complexity vs time -- all D values on common axes.
    (C) Dissipation channels -- one sub-panel per D.
    (D) Regime map -- fitted decay rate and peak active modes vs D.

All figures saved to output/figures/parameter_sweep/ as PNG (300 dpi).

Usage:
    python analyze_parameter_sweep.py

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

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
RUNS_DIR = os.path.join(SCRIPT_DIR, "output", "runs")
FIG_DIR = os.path.join(SCRIPT_DIR, "output", "figures", "parameter_sweep")

RE_PARAM_D = re.compile(r"^param_D(\d+p\d+)$")

# Activation threshold: mode is "active" if |a_k| ever exceeds this
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


def folder_to_D(folder_name: str) -> float:
    """Convert folder name back to D value: 'param_D0p1' -> 0.1."""
    m = RE_PARAM_D.match(folder_name)
    if m:
        return float(m.group(1).replace("p", "."))
    return -1.0


def discover_runs() -> dict:
    """Discover all param_D* runs, keyed by D value (float)."""
    runs = {}
    if not os.path.isdir(RUNS_DIR):
        print(f"ERROR: runs directory not found: {RUNS_DIR}")
        sys.exit(1)
    for name in sorted(os.listdir(RUNS_DIR)):
        m = RE_PARAM_D.match(name)
        if not m:
            continue
        run_dir = os.path.join(RUNS_DIR, name)
        if not os.path.isdir(run_dir):
            continue
        data = load_run(run_dir)
        if data is not None:
            D_val = folder_to_D(name)
            runs[D_val] = {"dir": run_dir, "name": name, "data": data}
    # Sort by D value
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


def get_modal(ts: dict) -> tuple:
    """Return (t, modal) with consistent length, or (None, None)."""
    modal = ts.get("modal_amplitudes")
    if modal is None or modal.ndim != 2:
        return None, None
    t = ts["t"]
    n = min(len(t), modal.shape[0])
    return t[:n], modal[:n]


def activated_mask(modal: np.ndarray, A: float) -> np.ndarray:
    """Boolean mask: True if mode ever exceeds activation threshold."""
    thresh = ACTIVATION_FRAC * A ** 2
    return np.max(np.abs(modal), axis=0) > thresh


def active_count_vs_time(modal: np.ndarray, A: float) -> np.ndarray:
    """Number of modes above threshold at each snapshot."""
    thresh = ACTIVATION_FRAC * A ** 2
    return np.sum(np.abs(modal) > thresh, axis=1)


def fit_energy_decay_rate(t: np.ndarray, E: np.ndarray) -> tuple:
    """Fit E ~ C * exp(-sigma * t) in the last half of the time series.

    Returns (sigma, C_fit, R2).
    """
    n = len(t)
    half = n // 2
    t_fit = t[half:]
    E_fit = np.abs(E[half:])

    mask = E_fit > 1e-30
    if np.sum(mask) < 10:
        return 0.0, 0.0, 0.0

    t_m = t_fit[mask]
    log_E = np.log(E_fit[mask])

    try:
        coeffs = np.polyfit(t_m, log_E, 1)
        sigma = -coeffs[0]
        C_fit = np.exp(coeffs[1])
        predicted = coeffs[0] * t_m + coeffs[1]
        ss_res = np.sum((log_E - predicted) ** 2)
        ss_tot = np.sum((log_E - np.mean(log_E)) ** 2)
        R2 = 1.0 - ss_res / max(ss_tot, 1e-30)
        return sigma, C_fit, R2
    except (np.linalg.LinAlgError, ValueError):
        return 0.0, 0.0, 0.0


# Color palette for D values (sequential, dark-to-light as D increases)
def d_color(D_val: float, D_all: list) -> str:
    """Map D value to a color from a perceptually uniform palette."""
    palette = ["#2166ac", "#4393c3", "#92c5de", "#d6604d", "#b2182b"]
    idx = D_all.index(D_val) if D_val in D_all else 0
    return palette[idx % len(palette)]


def d_linestyle(D_val: float, D_all: list) -> str:
    styles = ["-", "--", "-.", ":", (0, (3, 1, 1, 1))]
    idx = D_all.index(D_val) if D_val in D_all else 0
    return styles[idx % len(styles)]


# ---------------------------------------------------------------------------
# Figure A (per D): Modal funnel
# ---------------------------------------------------------------------------
def figure_modal_funnel(D_val: float, run: dict):
    ts = run["data"]
    meta = ts["metadata"]
    t, modal = get_modal(ts)
    if modal is None:
        print(f"  SKIP D={D_val}: no modal data.")
        return

    A_pm = meta.get("A_per_mode", 0.02)
    n_modes = modal.shape[1]
    mask = activated_mask(modal, A_pm)
    active = np.where(mask)[0]

    if len(active) == 0:
        print(f"  SKIP D={D_val}: no activated modes.")
        return

    k_max_active = active[-1]

    fig, ax = plt.subplots(figsize=(10, 6))

    norm = mcolors.Normalize(vmin=0, vmax=max(k_max_active, 1))
    cmap = plt.cm.viridis

    seeded = meta.get("seeded_modes", [])
    seeded_set = set(seeded)

    for k in active:
        a_k = np.abs(modal[:, k])
        color = cmap(norm(k))
        lw = 1.3 if k in seeded_set else 0.7
        alpha = 0.9 if k in seeded_set else 0.5
        ax.semilogy(t, np.maximum(a_k, 1e-30),
                     color=color, linewidth=lw, alpha=alpha)

    # Colorbar
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])
    cbar = fig.colorbar(sm, ax=ax, label="Mode index $k$", pad=0.02)
    cbar.ax.tick_params(labelsize=9)

    # Funnel annotation
    ax.annotate(
        r"Higher $k$ $\longrightarrow$ faster decay",
        xy=(0.50, 0.08), xycoords="axes fraction",
        fontsize=10, fontstyle="italic", color="0.35", ha="center",
        bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.7),
    )

    # Discriminant annotation
    Delta = meta.get("discriminant_Delta", None)
    regime = meta.get("regime", "")
    regime_short = regime.split("(")[0].strip() if regime else ""
    if Delta is not None:
        ax.annotate(
            f"$D = {D_val}$,  $\\Delta = {Delta:.3f}$\n{regime_short}",
            xy=(0.02, 0.95), xycoords="axes fraction",
            fontsize=9, va="top",
            bbox=dict(boxstyle="round,pad=0.3",
                      facecolor="wheat", alpha=0.7, edgecolor="0.6"),
        )

    setup_axes(ax, r"Time $t$", r"Modal amplitude $|a_k(t)|$",
               f"Modal Funnel -- $D = {D_val}$")
    fig.tight_layout()

    fname = f"modal_funnel_D{D_val:.1f}.png".replace(".", "p", 1)
    # Fix: only replace the first dot (in D value), keep .png
    fname = f"modal_funnel_D{str(D_val).replace('.', 'p')}.png"
    fig.savefig(os.path.join(FIG_DIR, fname), dpi=300)
    plt.close(fig)
    print(f"  Saved: {fname}")


# ---------------------------------------------------------------------------
# Figure B: Energy and complexity vs time (all D)
# ---------------------------------------------------------------------------
def figure_energy_complexity(runs: dict):
    D_all = sorted(runs.keys())

    fig, (ax_e, ax_c) = plt.subplots(
        1, 2, figsize=(14, 5),
        gridspec_kw={"wspace": 0.28},
    )

    for D_val, run in sorted(runs.items()):
        ts = run["data"]
        t = ts["t"]
        color = d_color(D_val, D_all)
        ls = d_linestyle(D_val, D_all)
        lbl = f"$D = {D_val}$"

        # Energy
        E = ts["E_total"]
        n_e = min(len(t), len(E))
        ax_e.semilogy(t[:n_e], E[:n_e],
                       color=color, linestyle=ls, linewidth=1.5, label=lbl)

        # Complexity
        C = ts.get("C_ED")
        if C is not None:
            n_c = min(len(t), len(C))
            ax_c.semilogy(t[:n_c], C[:n_c],
                           color=color, linestyle=ls, linewidth=1.5, label=lbl)

    # Annotation
    ax_e.annotate(
        r"Larger $D$ $\longrightarrow$ faster energy decay",
        xy=(0.50, 0.12), xycoords="axes fraction",
        fontsize=9, fontstyle="italic", color="0.35", ha="center",
        bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.7),
    )

    setup_axes(ax_e, r"Time $t$", r"Energy $\mathcal{E}(t)$",
               "Energy Decay -- D Sweep")
    ax_e.legend(fontsize=9, loc="upper right", framealpha=0.9)

    setup_axes(ax_c, r"Time $t$", r"$C_{\mathrm{ED}}(t)$",
               "Complexity Decay -- D Sweep")
    ax_c.legend(fontsize=9, loc="upper right", framealpha=0.9)

    fig.tight_layout()
    fig.savefig(os.path.join(FIG_DIR, "energy_complexity_sweep.png"), dpi=300)
    plt.close(fig)
    print("  Saved: energy_complexity_sweep.png")


# ---------------------------------------------------------------------------
# Figure C: Dissipation channels (one sub-panel per D)
# ---------------------------------------------------------------------------
def figure_dissipation_channels(runs: dict):
    D_all = sorted(runs.keys())
    n_D = len(D_all)

    fig, axes = plt.subplots(
        1, n_D, figsize=(4.5 * n_D, 5),
        sharey=True, squeeze=False,
    )
    axes = axes.flatten()

    channel_specs = [
        (r"$\mathcal{D}_{\mathrm{grad}}$", "D_gradient", "#2166ac", "-"),
        (r"$\mathcal{D}_{\mathrm{pen}}$",  "D_penalty",  "#b2182b", "-"),
        (r"$\mathcal{D}_{\mathrm{part}}$", "D_participation", "#1b7837", "-"),
        (r"$\mathcal{D}$",                 "D_total",    "black",   "--"),
    ]

    for idx, D_val in enumerate(D_all):
        ax = axes[idx]
        ts = runs[D_val]["data"]
        t = ts["t"]

        for ch_label, field, color, ls in channel_specs:
            if field in ts:
                data = ts[field]
                n = min(len(t), len(data))
                ax.semilogy(
                    t[:n], np.maximum(data[:n], 1e-30),
                    color=color, linestyle=ls,
                    linewidth=1.3 if ls == "-" else 1.0,
                    label=ch_label if idx == 0 else None,
                    alpha=1.0 if ls == "-" else 0.7,
                )

        meta = ts["metadata"]
        Delta = meta.get("discriminant_Delta", 0)
        ax.set_title(f"$D = {D_val}$\n$\\Delta = {Delta:.2f}$", fontsize=11)
        ax.set_xlabel(r"Time $t$", fontsize=10)
        ax.tick_params(labelsize=9)
        ax.grid(True, alpha=0.3, linewidth=0.5)

        if idx == 0:
            ax.set_ylabel("Dissipation rate", fontsize=11)

    # Shared legend from the first axis
    handles, labels = axes[0].get_legend_handles_labels()
    if handles:
        fig.legend(handles, labels, loc="upper center",
                   ncol=4, fontsize=9, framealpha=0.9,
                   bbox_to_anchor=(0.5, 1.02))

    fig.suptitle("Dissipation Channels -- D Sweep", fontsize=14,
                 fontweight="bold", y=1.06)
    fig.tight_layout()
    fig.savefig(os.path.join(FIG_DIR, "dissipation_channels_sweep.png"),
                dpi=300, bbox_inches="tight")
    plt.close(fig)
    print("  Saved: dissipation_channels_sweep.png")


# ---------------------------------------------------------------------------
# Figure D: Regime map -- decay rate and peak active modes vs D
# ---------------------------------------------------------------------------
def figure_regime_map(runs: dict, sweep_data: dict):
    D_all = sorted(sweep_data.keys())
    sigmas = [sweep_data[D]["sigma"] for D in D_all]
    peaks = [sweep_data[D]["peak_active"] for D in D_all]
    Deltas = [sweep_data[D]["Delta"] for D in D_all]

    fig, (ax_s, ax_p) = plt.subplots(
        1, 2, figsize=(13, 5),
        gridspec_kw={"wspace": 0.30},
    )

    # --- Decay rate vs D ---
    ax_s.plot(D_all, sigmas, "o-", color="#2166ac", linewidth=2.0,
              markersize=8, markeredgecolor="white", markeredgewidth=1.5,
              label=r"Fitted $\sigma$")
    ax_s.set_yscale("log")

    # Annotate discriminant values
    for i, D_val in enumerate(D_all):
        ax_s.annotate(
            f"$\\Delta={Deltas[i]:.2f}$",
            xy=(D_val, sigmas[i]),
            xytext=(8, 10), textcoords="offset points",
            fontsize=8, color="0.4",
            arrowprops=dict(arrowstyle="-", color="0.6", lw=0.5),
        )

    # Mark regime boundary (Delta = 1) if it falls within the sweep
    # Find where Delta crosses 1
    for i in range(len(D_all) - 1):
        if (Deltas[i] - 1.0) * (Deltas[i + 1] - 1.0) < 0:
            # Linearly interpolate D at Delta = 1
            D_crit = D_all[i] + (1.0 - Deltas[i]) / (Deltas[i + 1] - Deltas[i]) * (
                D_all[i + 1] - D_all[i])
            ax_s.axvline(D_crit, color="#d6604d", linestyle=":", linewidth=1.5,
                         alpha=0.7, label=f"$\\Delta = 1$ at $D \\approx {D_crit:.2f}$")

    setup_axes(ax_s, r"Diffusion coefficient $D$",
               r"Energy decay rate $\sigma$",
               "Decay Rate vs $D$")
    ax_s.legend(fontsize=9, loc="upper left", framealpha=0.9)

    # --- Peak active modes vs D ---
    ax_p.plot(D_all, peaks, "s-", color="#b2182b", linewidth=2.0,
              markersize=8, markeredgecolor="white", markeredgewidth=1.5,
              label="Peak active modes")

    # Annotate
    for i, D_val in enumerate(D_all):
        ax_p.annotate(
            str(peaks[i]),
            xy=(D_val, peaks[i]),
            xytext=(0, 10), textcoords="offset points",
            fontsize=9, ha="center", color="#b2182b",
        )

    setup_axes(ax_p, r"Diffusion coefficient $D$",
               "Peak active mode count",
               "Cascade Breadth vs $D$")
    ax_p.legend(fontsize=9, loc="upper right", framealpha=0.9)
    ax_p.set_ylim(bottom=0)

    fig.suptitle("Regime Map -- D Sweep", fontsize=14, fontweight="bold", y=1.02)
    fig.tight_layout()
    fig.savefig(os.path.join(FIG_DIR, "regime_map_D.png"),
                dpi=300, bbox_inches="tight")
    plt.close(fig)
    print("  Saved: regime_map_D.png")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    os.makedirs(FIG_DIR, exist_ok=True)

    print("Discovering D-sweep runs...")
    runs = discover_runs()

    if not runs:
        print(f"\nERROR: No param_D* runs found in:")
        print(f"  {RUNS_DIR}")
        print("\nRun the experiment first:")
        print("  python experiments/parameter_sweep.py")
        sys.exit(1)

    D_all = sorted(runs.keys())
    print(f"  Found {len(runs)} runs: D = {D_all}")

    # --- Pre-compute sweep data for summary and Figure D ---
    sweep_data = {}
    for D_val, run in sorted(runs.items()):
        ts = run["data"]
        meta = ts["metadata"]
        t = ts["t"]
        E = ts["E_total"]

        # Fit decay rate
        n_e = min(len(t), len(E))
        sigma, C_fit, R2 = fit_energy_decay_rate(t[:n_e], E[:n_e])

        # Peak active modes
        t_m, modal = get_modal(ts)
        peak_active = 0
        if modal is not None:
            A_pm = meta.get("A_per_mode", 0.02)
            count = active_count_vs_time(modal, A_pm)
            peak_active = int(np.max(count))

        Delta = meta.get("discriminant_Delta", 0)
        regime = meta.get("regime", "")

        sweep_data[D_val] = {
            "sigma": sigma,
            "C_fit": C_fit,
            "R2": R2,
            "peak_active": peak_active,
            "Delta": Delta,
            "regime": regime,
            "E0": E[0],
            "ET": E[-1],
        }

    # --- (A) Per-D modal funnels ---
    print("\n--- (A) Modal Funnel Figures ---")
    for D_val, run in sorted(runs.items()):
        figure_modal_funnel(D_val, run)

    # --- (B) Cross-D energy and complexity ---
    print("\n--- (B) Energy & Complexity vs Time ---")
    figure_energy_complexity(runs)

    # --- (C) Dissipation channels ---
    print("\n--- (C) Dissipation Channels ---")
    figure_dissipation_channels(runs)

    # --- (D) Regime map ---
    print("\n--- (D) Regime Map ---")
    figure_regime_map(runs, sweep_data)

    # --- Summary table ---
    print(f"\n{'='*100}")
    print("  Parameter Sweep Summary: D")
    print(f"{'='*100}")
    print(f"  {'D':<8} {'Delta':<9} {'Regime':<14} {'sigma':<12} "
          f"{'R^2':<8} {'Peak act':<10} {'E(0)':<14} {'E(T)':<14} "
          f"{'E(T)/E(0)':<12}")
    print("  " + "-" * 98)

    for D_val in D_all:
        d = sweep_data[D_val]
        regime_short = d["regime"].split("(")[0].strip()[:12]
        ratio = d["ET"] / max(d["E0"], 1e-30)

        print(f"  {D_val:<8.1f} {d['Delta']:<9.4f} {regime_short:<14} "
              f"{d['sigma']:<12.6f} {d['R2']:<8.4f} {d['peak_active']:<10} "
              f"{d['E0']:<14.6e} {d['ET']:<14.6e} {ratio:<12.4e}")

    # --- Scaling analysis ---
    print("\n  Scaling analysis:")
    if len(D_all) >= 3:
        D_arr = np.array(D_all)
        sigma_arr = np.array([sweep_data[D]["sigma"] for D in D_all])

        # Check if sigma ~ D (linear) or sigma ~ D^alpha
        valid = sigma_arr > 0
        if np.sum(valid) >= 3:
            log_D = np.log(D_arr[valid])
            log_s = np.log(sigma_arr[valid])
            try:
                coeffs = np.polyfit(log_D, log_s, 1)
                alpha = coeffs[0]
                print(f"    sigma ~ D^alpha with alpha = {alpha:.3f}")
                if abs(alpha - 1.0) < 0.15:
                    print(f"    => Consistent with sigma ~ D (linear scaling)")
                else:
                    print(f"    => Non-linear scaling (alpha != 1)")
            except (np.linalg.LinAlgError, ValueError):
                print(f"    (scaling fit failed)")

    # --- Regime transitions ---
    print("\n  Regime transitions:")
    prev = None
    for D_val in D_all:
        regime = sweep_data[D_val]["regime"]
        if prev is not None and regime != prev:
            print(f"    D = {D_all[D_all.index(D_val)-1]} -> {D_val}: "
                  f"{prev.split('(')[0].strip()} -> {regime.split('(')[0].strip()}")
        prev = regime

    if all(sweep_data[D]["regime"] == sweep_data[D_all[0]]["regime"] for D in D_all):
        print(f"    No regime transition in sweep range "
              f"D in [{D_all[0]}, {D_all[-1]}]")
        print(f"    All runs: {sweep_data[D_all[0]]['regime']}")

    print(f"\nAll figures saved to: {FIG_DIR}")
    print("Done.")


if __name__ == "__main__":
    main()
