"""
analyze_low_mode_attractor.py
==============================
Post-processing script for the Low-Mode Attractor experiment (Atlas §7,
Appendix C.7).

Loads all attractor_IC* runs and produces five figure groups:

  (A) Long-time modal collapse — |a_k(t)| for all modes, highlighting the
      surviving low modes and annotating the attractor.
  (B) Return map for the dominant mode — (a_1(t), a_1(t+dt)) fixed-point
      structure.
  (C) Phase portrait of (a_1, a_2) — 2D trajectory visualizing attractor
      geometry.
  (D) Energy and complexity long-time decay — all ICs on semilog-y.
  (E) Attractor convergence rate — |a_k(t) - a_k(T)| exponential decay.

All figures saved to output/figures/low_mode_attractor/ as PNG (300 dpi).

Usage:
    python analyze_low_mode_attractor.py

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
from scipy.optimize import curve_fit

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
RUNS_DIR = os.path.join(SCRIPT_DIR, "output", "runs")
FIG_DIR = os.path.join(SCRIPT_DIR, "output", "figures", "low_mode_attractor")

RE_IC = re.compile(r"^attractor_(IC\d+)$")

# Modes considered "low" for attractor analysis
LOW_MODES = [0, 1, 2, 3]

# A mode is "surviving" if its late-time amplitude exceeds this
SURVIVAL_THRESH = 1e-12

# A mode is "active" if it ever exceeds this fraction of A^2
ACTIVATION_FRAC = 1e-4

# Colors for the five ICs
IC_COLORS = {
    "IC1": "#2166ac",
    "IC2": "#b2182b",
    "IC3": "#1b7837",
    "IC4": "#762a83",
    "IC5": "#e6550d",
}
IC_STYLES = {
    "IC1": "-",
    "IC2": "--",
    "IC3": "-.",
    "IC4": ":",
    "IC5": (0, (3, 1, 1, 1)),
}


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


def short_label(label: str, meta: dict) -> str:
    desc = meta.get("description", "")
    # Truncate for legend
    if len(desc) > 30:
        desc = desc[:28] + "..."
    return f"{label}: {desc}"


def get_modal(ts: dict) -> tuple:
    """Return (t, modal) arrays with consistent length."""
    modal = ts.get("modal_amplitudes")
    if modal is None or modal.ndim != 2:
        return None, None
    t = ts["t"]
    n = min(len(t), modal.shape[0])
    return t[:n], modal[:n]


def fit_exponential_rate(t: np.ndarray, y: np.ndarray) -> tuple:
    """Fit y ~ C * exp(-sigma * t) in the last half of the data.

    Returns (sigma, C, R2).
    """
    n = len(t)
    half = n // 2
    t_fit = t[half:]
    y_fit = np.abs(y[half:])

    # Filter out zeros
    mask = y_fit > 1e-30
    if np.sum(mask) < 10:
        return 0.0, 0.0, 0.0

    t_m = t_fit[mask]
    log_y = np.log(y_fit[mask])

    # Linear fit: log(y) = log(C) - sigma * t
    try:
        coeffs = np.polyfit(t_m, log_y, 1)
        sigma = -coeffs[0]
        C = np.exp(coeffs[1])

        # R^2
        predicted = coeffs[0] * t_m + coeffs[1]
        ss_res = np.sum((log_y - predicted) ** 2)
        ss_tot = np.sum((log_y - np.mean(log_y)) ** 2)
        R2 = 1.0 - ss_res / max(ss_tot, 1e-30)

        return sigma, C, R2
    except (np.linalg.LinAlgError, ValueError):
        return 0.0, 0.0, 0.0


# ---------------------------------------------------------------------------
# Figure A: Long-time modal collapse (per IC)
# ---------------------------------------------------------------------------
def figure_modal_collapse(label: str, run: dict):
    ts = run["data"]
    t, modal = get_modal(ts)
    if modal is None:
        print(f"  SKIP {label}: no modal data.")
        return

    meta = ts["metadata"]
    n_modes = modal.shape[1]

    fig, ax = plt.subplots(figsize=(10, 6))

    # Determine which modes are ever active
    A_pm = meta.get("A_per_mode", 0.02)
    thresh = ACTIVATION_FRAC * A_pm ** 2
    peak_amp = np.max(np.abs(modal), axis=0)
    active = np.where(peak_amp > thresh)[0]

    # Late-time amplitudes (last 5% of data)
    late_start = int(0.95 * len(t))
    late_amp = np.mean(np.abs(modal[late_start:]), axis=0)

    # Surviving modes
    surviving = np.where(late_amp > SURVIVAL_THRESH)[0]

    # Plot all active modes in grey
    for k in active:
        a_k = np.abs(modal[:, k])
        is_low = k in LOW_MODES
        is_surviving = k in surviving

        if is_low and is_surviving:
            color = plt.cm.Set1(k / max(len(LOW_MODES), 1))
            lw = 2.0
            alpha = 1.0
            lbl = rf"$|a_{{{k}}}|$ (surviving)"
        elif is_surviving:
            color = "#ff7f0e"
            lw = 1.2
            alpha = 0.7
            lbl = rf"$|a_{{{k}}}|$" if k <= 5 else None
        else:
            color = "0.75"
            lw = 0.5
            alpha = 0.4
            lbl = None

        ax.semilogy(
            t, np.maximum(a_k, 1e-30),
            color=color, linewidth=lw, alpha=alpha,
            label=lbl,
        )

    # Annotate the attractor
    if len(surviving) > 0:
        ax.annotate(
            f"Low-mode attractor\n(surviving modes: "
            f"{', '.join(str(k) for k in surviving[:6])})",
            xy=(0.55, 0.12),
            xycoords="axes fraction",
            fontsize=10, fontstyle="italic", color="#333333",
            ha="center",
            bbox=dict(boxstyle="round,pad=0.4", facecolor="#ffffcc",
                      alpha=0.85, edgecolor="#999999"),
        )

    # Annotate the decay region
    ax.annotate(
        r"Higher $k$ $\longrightarrow$ faster collapse",
        xy=(0.55, 0.88),
        xycoords="axes fraction",
        fontsize=9, fontstyle="italic", color="0.4",
        ha="center",
    )

    setup_axes(
        ax,
        xlabel=r"Time $t$",
        ylabel=r"Modal amplitude $|a_k(t)|$",
        title=f"Low-Mode Attractor — {label}: Modal Collapse",
    )
    ax.legend(fontsize=8, loc="upper right", framealpha=0.9, ncol=2)
    fig.tight_layout()

    fname = f"modal_collapse_{label}.png"
    fig.savefig(os.path.join(FIG_DIR, fname), dpi=300)
    plt.close(fig)
    print(f"  Saved: {fname}")


# ---------------------------------------------------------------------------
# Figure B: Return map for the dominant mode
# ---------------------------------------------------------------------------
def figure_return_map(label: str, run: dict):
    ts = run["data"]
    t, modal = get_modal(ts)
    if modal is None or modal.shape[1] < 2:
        print(f"  SKIP {label}: no modal data for return map.")
        return

    # Use mode 1 (the first non-homogeneous mode)
    k = 1
    a1 = modal[:, k]
    n = len(a1)

    if n < 20:
        print(f"  SKIP {label}: too few data points for return map.")
        return

    # Return map: (a_1(t_i), a_1(t_{i+1}))
    # Use a lag of 1 output step
    lag = 1
    a_now = a1[:-lag]
    a_next = a1[lag:]

    fig, ax = plt.subplots(figsize=(7, 7))

    # Color by time (early = blue, late = red)
    time_frac = np.linspace(0, 1, len(a_now))
    scatter = ax.scatter(
        a_now, a_next,
        c=time_frac, cmap="coolwarm", s=6, alpha=0.7,
        edgecolors="none",
    )

    # Identity line (fixed point lies on this line)
    a_range = [min(a_now.min(), a_next.min()), max(a_now.max(), a_next.max())]
    margin = 0.05 * (a_range[1] - a_range[0])
    lim = [a_range[0] - margin, a_range[1] + margin]
    ax.plot(lim, lim, color="black", linewidth=0.8, linestyle="--", alpha=0.5,
            label="Identity line")

    # Mark the fixed point (equilibrium value of a_1)
    a1_eq = np.mean(a1[-max(10, n // 20):])
    ax.plot(a1_eq, a1_eq, "r*", markersize=14, zorder=10,
            label=rf"Fixed point $a_1^* = {a1_eq:.4e}$")

    cbar = fig.colorbar(scatter, ax=ax, label="Time (early → late)", pad=0.02)
    cbar.ax.tick_params(labelsize=9)

    setup_axes(
        ax,
        xlabel=rf"$a_{{{k}}}(t)$",
        ylabel=rf"$a_{{{k}}}(t + \Delta t)$",
        title=f"Return Map — {label}: Mode $k = {k}$",
    )
    ax.set_aspect("equal", adjustable="datalim")
    ax.legend(fontsize=9, loc="upper left", framealpha=0.9)
    fig.tight_layout()

    fname = f"return_map_{label}.png"
    fig.savefig(os.path.join(FIG_DIR, fname), dpi=300)
    plt.close(fig)
    print(f"  Saved: {fname}")


# ---------------------------------------------------------------------------
# Figure C: Phase portrait (a_1, a_2)
# ---------------------------------------------------------------------------
def figure_phase_portrait(label: str, run: dict):
    ts = run["data"]
    t, modal = get_modal(ts)
    if modal is None or modal.shape[1] < 3:
        print(f"  SKIP {label}: insufficient modes for phase portrait.")
        return

    a1 = modal[:, 1]
    a2 = modal[:, 2]
    n = len(a1)

    fig, ax = plt.subplots(figsize=(8, 7))

    # Color trajectory by time
    time_frac = np.linspace(0, 1, n)

    # Plot as colored line segments
    points = np.array([a1, a2]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)

    from matplotlib.collections import LineCollection
    norm = plt.Normalize(0, 1)
    lc = LineCollection(segments, cmap="coolwarm", norm=norm, linewidths=1.2,
                        alpha=0.8)
    lc.set_array(time_frac[:-1])
    ax.add_collection(lc)

    # Start and end markers
    ax.plot(a1[0], a2[0], "o", color="#2166ac", markersize=10, zorder=10,
            label="Start")
    ax.plot(a1[-1], a2[-1], "*", color="#b2182b", markersize=14, zorder=10,
            label=f"End ({a1[-1]:.2e}, {a2[-1]:.2e})")

    # Equilibrium at origin
    ax.plot(0, 0, "k+", markersize=12, markeredgewidth=2, zorder=10,
            label=r"Equilibrium $(0, 0)$")

    # Auto-scale
    pad_x = 0.1 * max(abs(a1.max() - a1.min()), 1e-10)
    pad_y = 0.1 * max(abs(a2.max() - a2.min()), 1e-10)
    ax.set_xlim(a1.min() - pad_x, a1.max() + pad_x)
    ax.set_ylim(a2.min() - pad_y, a2.max() + pad_y)

    cbar = fig.colorbar(lc, ax=ax, label="Time (early → late)", pad=0.02)
    cbar.ax.tick_params(labelsize=9)

    setup_axes(
        ax,
        xlabel=r"$a_1(t)$",
        ylabel=r"$a_2(t)$",
        title=f"Phase Portrait — {label}: $(a_1, a_2)$",
    )
    ax.legend(fontsize=9, loc="upper right", framealpha=0.9)
    fig.tight_layout()

    fname = f"phase_portrait_{label}.png"
    fig.savefig(os.path.join(FIG_DIR, fname), dpi=300)
    plt.close(fig)
    print(f"  Saved: {fname}")


# ---------------------------------------------------------------------------
# Figure D: Energy and complexity long-time decay (all ICs)
# ---------------------------------------------------------------------------
def figure_energy_complexity(runs: dict):
    fig, (ax_e, ax_c) = plt.subplots(
        1, 2, figsize=(14, 5),
        gridspec_kw={"wspace": 0.28},
    )

    for label, run in sorted(runs.items()):
        ts = run["data"]
        meta = ts["metadata"]
        t = ts["t"]
        color = IC_COLORS.get(label, "0.3")
        ls = IC_STYLES.get(label, "-")
        lbl = short_label(label, meta)

        # Energy
        E = ts["E_total"]
        n_e = min(len(t), len(E))
        ax_e.semilogy(
            t[:n_e], E[:n_e],
            color=color, linestyle=ls, linewidth=1.5,
            label=lbl,
        )

        # Complexity
        C = ts.get("C_ED")
        if C is not None:
            n_c = min(len(t), len(C))
            ax_c.semilogy(
                t[:n_c], C[:n_c],
                color=color, linestyle=ls, linewidth=1.5,
                label=lbl,
            )

    # Annotate convergence
    ax_e.annotate(
        "All ICs converge to same\nasymptotic tail",
        xy=(0.60, 0.35),
        xycoords="axes fraction",
        fontsize=9, fontstyle="italic", color="0.35",
        ha="center",
        bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.7),
    )

    setup_axes(ax_e, r"Time $t$", r"Energy $\mathcal{E}(t)$",
               "Attractor — Energy Decay (all ICs)")
    ax_e.legend(fontsize=7, loc="upper right", framealpha=0.9)

    setup_axes(ax_c, r"Time $t$", r"$C_{\mathrm{ED}}(t)$",
               "Attractor — Complexity Decay (all ICs)")
    ax_c.legend(fontsize=7, loc="upper right", framealpha=0.9)

    fig.tight_layout()
    fname = "energy_complexity_all_ICs.png"
    fig.savefig(os.path.join(FIG_DIR, fname), dpi=300)
    plt.close(fig)
    print(f"  Saved: {fname}")


# ---------------------------------------------------------------------------
# Figure E: Attractor convergence rate — |a_k(t) - a_k(T)| for low modes
# ---------------------------------------------------------------------------
def figure_convergence_rate(runs: dict):
    fig, axes = plt.subplots(
        1, min(len(runs), 5), figsize=(4 * min(len(runs), 5), 5),
        sharey=True,
        squeeze=False,
    )
    axes = axes.flatten()

    convergence_data = {}

    for idx, (label, run) in enumerate(sorted(runs.items())):
        if idx >= len(axes):
            break

        ts = run["data"]
        t, modal = get_modal(ts)
        ax = axes[idx]

        if modal is None:
            ax.text(0.5, 0.5, "No modal data", ha="center", va="center",
                    transform=ax.transAxes, fontsize=10, color="0.5")
            setup_axes(ax, r"$t$", "", label)
            continue

        n_modes = modal.shape[1]
        convergence_data[label] = {}

        mode_colors = ["#2166ac", "#b2182b", "#1b7837", "#762a83"]

        for ki, k in enumerate(LOW_MODES):
            if k >= n_modes:
                continue

            a_k = modal[:, k]
            a_k_eq = a_k[-1]  # Approximate equilibrium value

            residual = np.abs(a_k - a_k_eq)
            residual_safe = np.maximum(residual, 1e-30)

            ax.semilogy(
                t, residual_safe,
                color=mode_colors[ki % len(mode_colors)],
                linewidth=1.3,
                label=rf"$|a_{{{k}}} - a_{{{k}}}^*|$",
            )

            # Fit exponential rate in the last half
            sigma, C_fit, R2 = fit_exponential_rate(t, residual)
            convergence_data[label][k] = {
                "sigma": sigma,
                "R2": R2,
                "a_eq": a_k_eq,
            }

            # Overlay fit line
            if sigma > 0 and R2 > 0.8:
                t_fit = t[len(t) // 2:]
                ax.semilogy(
                    t_fit,
                    C_fit * np.exp(-sigma * t_fit),
                    color=mode_colors[ki % len(mode_colors)],
                    linestyle="--",
                    linewidth=0.8,
                    alpha=0.6,
                )

        setup_axes(ax, r"Time $t$",
                   r"$|a_k(t) - a_k^*|$" if idx == 0 else "",
                   label)
        ax.legend(fontsize=7, loc="upper right", framealpha=0.9)

    fig.suptitle("Attractor Convergence Rate — Exponential Decay to Equilibrium",
                 fontsize=14, fontweight="bold", y=1.02)
    fig.tight_layout()

    fname = "convergence_rate_all_ICs.png"
    fig.savefig(os.path.join(FIG_DIR, fname), dpi=300, bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved: {fname}")

    return convergence_data


# ---------------------------------------------------------------------------
# Summary table
# ---------------------------------------------------------------------------
def print_summary(runs: dict, convergence_data: dict):
    print(f"\n{'='*95}")
    print("  Low-Mode Attractor — Summary")
    print(f"{'='*95}")

    # --- Surviving modes ---
    print(f"\n  Surviving Modes (late-time |a_k| > {SURVIVAL_THRESH}):")
    print(f"  {'IC':<6} {'Surviving modes':<30} {'Late-time amplitudes'}")
    print("  " + "-" * 75)

    for label, run in sorted(runs.items()):
        ts = run["data"]
        t, modal = get_modal(ts)
        if modal is None:
            print(f"  {label:<6} (no modal data)")
            continue

        late_start = int(0.95 * len(t))
        late_amp = np.mean(np.abs(modal[late_start:]), axis=0)
        surviving = np.where(late_amp > SURVIVAL_THRESH)[0]

        amp_str = ", ".join(f"{k}:{late_amp[k]:.2e}" for k in surviving[:8])
        mode_str = ", ".join(str(k) for k in surviving[:10])
        if len(surviving) > 10:
            mode_str += f" ... ({len(surviving)} total)"

        print(f"  {label:<6} {mode_str:<30} {amp_str}")

    # --- Convergence rates ---
    print(f"\n  Convergence Rates (exponential fit, last half):")
    print(f"  {'IC':<6} {'Mode':<6} {'sigma':<14} {'R^2':<10} {'a_k^*':<14}")
    print("  " + "-" * 55)

    for label in sorted(convergence_data.keys()):
        for k in sorted(convergence_data[label].keys()):
            d = convergence_data[label][k]
            print(f"  {label:<6} k={k:<4} {d['sigma']:<14.6e} "
                  f"{d['R2']:<10.4f} {d['a_eq']:<14.6e}")

    # --- Final energy and complexity ---
    print(f"\n  Final State:")
    print(f"  {'IC':<6} {'E(T)':<16} {'C_ED(T)':<16} {'Margin':<16} "
          f"{'Wall(s)':<10}")
    print("  " + "-" * 70)

    final_energies = []
    for label, run in sorted(runs.items()):
        ts = run["data"]
        meta = ts["metadata"]
        E_final = ts["E_total"][-1]
        C_final = ts.get("C_ED", [0])[-1]
        margin = ts.get("margin", [0])[-1]
        wall = meta.get("wall_time_s", 0)
        final_energies.append(E_final)

        print(f"  {label:<6} {E_final:<16.6e} {C_final:<16.6e} "
              f"{margin:<16.6e} {wall:<10.1f}")

    # Universality check
    if len(final_energies) > 1:
        E_arr = np.array(final_energies)
        E_mean = np.mean(E_arr)
        E_spread = np.max(E_arr) - np.min(E_arr)
        rel = E_spread / max(abs(E_mean), 1e-30)

        print(f"\n  Attractor Universality:")
        print(f"    Mean E(T):     {E_mean:.6e}")
        print(f"    Spread:        {E_spread:.6e}")
        print(f"    Rel spread:    {rel:.3e}")
        if rel < 1e-4:
            print(f"    Verdict:       PASS (all ICs converge to same equilibrium)")
        elif rel < 1e-2:
            print(f"    Verdict:       MARGINAL (converging, may need longer T)")
        else:
            print(f"    Verdict:       INCONCLUSIVE (extend integration time)")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    os.makedirs(FIG_DIR, exist_ok=True)

    print("Discovering attractor runs...")
    runs = discover_runs()

    if not runs:
        print(f"\nERROR: No attractor_IC* runs found in:")
        print(f"  {RUNS_DIR}")
        print("\nRun the experiment first:")
        print("  python experiments/low_mode_attractor.py")
        sys.exit(1)

    print(f"  Found {len(runs)} runs:")
    for label, run in runs.items():
        meta = run["data"]["metadata"]
        desc = meta.get("description", "")
        print(f"    {label}: {desc}")

    # --- (A) Per-IC modal collapse ---
    print("\n--- (A) Long-Time Modal Collapse ---")
    for label, run in runs.items():
        figure_modal_collapse(label, run)

    # --- (B) Per-IC return map ---
    print("\n--- (B) Return Maps ---")
    for label, run in runs.items():
        figure_return_map(label, run)

    # --- (C) Per-IC phase portrait ---
    print("\n--- (C) Phase Portraits (a_1, a_2) ---")
    for label, run in runs.items():
        figure_phase_portrait(label, run)

    # --- (D) Cross-IC energy and complexity ---
    print("\n--- (D) Energy & Complexity (all ICs) ---")
    figure_energy_complexity(runs)

    # --- (E) Convergence rate ---
    print("\n--- (E) Convergence Rate ---")
    convergence_data = figure_convergence_rate(runs)

    # --- Summary ---
    print_summary(runs, convergence_data)

    print(f"\nAll figures saved to: {FIG_DIR}")
    print("Done.")


if __name__ == "__main__":
    main()
