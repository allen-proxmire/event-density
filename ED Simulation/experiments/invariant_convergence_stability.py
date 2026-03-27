"""
invariant_convergence_stability.py
====================================
Experiment / Analysis: Invariant Convergence Stability

Scans all completed regime_D*_A*_Nm* runs, computes the convergence
error signals

    e_E(t) = |E(t) − E*|
    e_H(t) = |H(t) − H*|
    e_D(t) = |D_total(t) − D*|

and analyses the three-stage convergence structure predicted by
Theorem C.76:

    Stage 1 (fast transient):     first 20% of time
    Stage 2 (drift / algebraic):  middle 60%
    Stage 3 (exponential):        last 20%

For each stage, a local slope on log(e) vs t is extracted and
classified as fast / drift / exponential / flat / noisy.

Produces:
  (A) Convergence Curves — e(t) for a representative run with stages shaded.
  (B) Attractor Stability Scatter — Stage-3 slopes for all runs.
  (C) Stability Heatmap — fraction of clean exponential Stage-3 signals.

All figures saved to output/figures/invariants/convergence_stability/
as PNG (300 dpi).

Usage:
    python experiments/invariant_convergence_stability.py

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
                        "convergence_stability")

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
LATE_FRAC = 0.10         # Fraction for attractor value
LOG_FLOOR = 1e-30

# Stage boundaries (fraction of total time)
STAGE_1_END = 0.20       # Fast transient
STAGE_2_END = 0.80       # Drift / algebraic
# Stage 3: 0.80 – 1.00   # Exponential

# Slope classification thresholds
SLOPE_EXP_MIN = 0.01     # |slope| must exceed this for "exponential"
R2_CLEAN = 0.90          # R² must exceed this for "clean" fit
SLOPE_FAST_MIN = 0.5     # |slope| above this in Stage 1 → "fast"

SIGNAL_NAMES = ["E", "H", "D"]
SIGNAL_LABELS = {
    "E": r"$|E(t) - E^*|$",
    "H": r"$|H(t) - H^*|$",
    "D": r"$|\mathcal{D}(t) - \mathcal{D}^*|$",
}
SIGNAL_COLORS = {
    "E": "#2166ac",
    "H": "#7570b3",
    "D": "#b2182b",
}

STAGE_COLORS = ["#fee8c8", "#fdbb84", "#e34a33"]  # light→dark for shading
STAGE_LABELS = ["Stage 1 (fast)", "Stage 2 (drift)", "Stage 3 (exp)"]


# ---------------------------------------------------------------------------
# Discovery
# ---------------------------------------------------------------------------
def discover_regime_runs() -> list[dict]:
    """Scan RUNS_DIR for regime_D*_A*_Nm* folders with required data."""
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

        if meta.get("regime") == "inadmissible":
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
        t = ts.get("t")
        E = ts.get("E_total")
        modal = ts.get("modal_amplitudes")
        D_total = ts.get("D_total")

        if t is None or E is None:
            continue

        # Reconstruct D_total if missing
        if D_total is None:
            D_grad = ts.get("D_gradient")
            D_pen = ts.get("D_penalty")
            D_part = ts.get("D_participation")
            if D_grad is not None and D_pen is not None and D_part is not None:
                D_total = D_grad + D_pen + D_part
            else:
                continue

        n = min(len(t), len(E), len(D_total))

        # Shannon entropy (optional — compute from modal if available)
        H = None
        if modal is not None and modal.ndim == 2:
            n = min(n, modal.shape[0])
            if modal.shape[1] >= 3:
                H = _compute_shannon(modal[:n])

        if n < 50:
            continue

        run_data = {
            "dir": d,
            "name": name,
            "D": float(D_val),
            "A": float(A_val),
            "Nm": int(Nm_val),
            "metadata": meta,
            "t": t[:n],
            "E": E[:n],
            "D_total": D_total[:n],
            "H": H[:n] if H is not None else None,
        }
        runs.append(run_data)

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


def _compute_shannon(modal: np.ndarray) -> np.ndarray:
    """Shannon entropy from modal amplitudes (k >= 1)."""
    E_k = modal[:, 1:] ** 2
    E_total = np.sum(E_k, axis=1, keepdims=True)
    E_total = np.maximum(E_total, LOG_FLOOR)
    p = E_k / E_total
    return -np.sum(p * np.log(p + LOG_FLOOR), axis=1)


# ---------------------------------------------------------------------------
# Slope fitting and classification
# ---------------------------------------------------------------------------
def fit_log_slope(t: np.ndarray, e: np.ndarray) -> dict:
    """Fit slope on log(e) vs t.  Returns slope, R², regime label."""
    result = {"slope": 0.0, "R2": 0.0, "regime": "flat"}

    valid = e > LOG_FLOOR
    if np.sum(valid) < 5:
        result["regime"] = "noisy"
        return result

    log_e = np.log(e[valid])
    t_v = t[valid]

    try:
        coeffs = np.polyfit(t_v, log_e, 1)
        slope = coeffs[0]

        predicted = coeffs[0] * t_v + coeffs[1]
        ss_res = np.sum((log_e - predicted) ** 2)
        ss_tot = np.sum((log_e - np.mean(log_e)) ** 2)
        R2 = 1.0 - ss_res / max(ss_tot, 1e-30)

        result["slope"] = float(slope)
        result["R2"] = float(R2)
    except (np.linalg.LinAlgError, ValueError):
        result["regime"] = "noisy"
        return result

    # Classification
    abs_slope = abs(result["slope"])

    if result["R2"] < 0.5:
        result["regime"] = "noisy"
    elif abs_slope < SLOPE_EXP_MIN:
        result["regime"] = "flat"
    elif abs_slope > SLOPE_FAST_MIN:
        result["regime"] = "fast"
    elif result["R2"] > R2_CLEAN and result["slope"] < -SLOPE_EXP_MIN:
        result["regime"] = "exponential"
    else:
        result["regime"] = "drift"

    return result


# ---------------------------------------------------------------------------
# Per-run analysis
# ---------------------------------------------------------------------------
def analyse_run(run: dict) -> dict:
    """Compute convergence error signals, stage slopes, and classifications."""
    t = run["t"]
    n = len(t)

    # Attractor values (last LATE_FRAC)
    late_start = max(0, int((1.0 - LATE_FRAC) * n))

    E_star = float(np.mean(run["E"][late_start:]))
    D_star = float(np.mean(run["D_total"][late_start:]))
    H_star = float(np.mean(run["H"][late_start:])) if run["H"] is not None else np.nan

    # Error signals
    e_E = np.abs(run["E"] - E_star)
    e_D = np.abs(run["D_total"] - D_star)
    e_H = np.abs(run["H"] - H_star) if run["H"] is not None else None

    signals = {"E": e_E, "D": e_D}
    if e_H is not None:
        signals["H"] = e_H

    # Stage boundaries (index-based)
    i1 = int(STAGE_1_END * n)
    i2 = int(STAGE_2_END * n)

    stages_idx = [
        (0, i1),        # Stage 1
        (i1, i2),       # Stage 2
        (i2, n),        # Stage 3
    ]

    # Fit each signal in each stage
    stage_results = {}  # {signal: [stage1_fit, stage2_fit, stage3_fit]}

    for sig_name, e_sig in signals.items():
        fits = []
        for s_start, s_end in stages_idx:
            if s_end - s_start < 5:
                fits.append({"slope": 0.0, "R2": 0.0, "regime": "noisy"})
            else:
                fits.append(fit_log_slope(t[s_start:s_end], e_sig[s_start:s_end]))
        stage_results[sig_name] = fits

    # Count clean exponential Stage-3 signals
    n_exp3 = 0
    n_signals = len(signals)
    for sig_name in signals:
        s3 = stage_results[sig_name][2]
        if s3["regime"] == "exponential":
            n_exp3 += 1

    frac_exp3 = n_exp3 / max(n_signals, 1)

    return {
        "E_star": E_star,
        "H_star": H_star,
        "D_star": D_star,
        "stage_results": stage_results,
        "n_signals": n_signals,
        "n_exp3": n_exp3,
        "frac_exp3": frac_exp3,
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
# Figure A: Convergence Curves (representative run)
# ---------------------------------------------------------------------------
def figure_convergence_curves(runs: list[dict], analyses: list[dict]):
    """Plot e_E, e_H, e_D on semilog-y with stage shading."""
    best_idx = max(range(len(runs)), key=lambda i: runs[i]["Nm"])
    run = runs[best_idx]
    ana = analyses[best_idx]

    t = run["t"]
    n = len(t)

    # Error signals
    E_star = ana["E_star"]
    D_star = ana["D_star"]
    H_star = ana["H_star"]

    e_E = np.abs(run["E"] - E_star)
    e_D = np.abs(run["D_total"] - D_star)
    e_H = np.abs(run["H"] - H_star) if run["H"] is not None else None

    fig, ax = plt.subplots(figsize=(12, 6))

    # Stage shading
    i1 = int(STAGE_1_END * n)
    i2 = int(STAGE_2_END * n)

    for s_idx, (s_start, s_end, color, label) in enumerate([
        (0, i1, STAGE_COLORS[0], STAGE_LABELS[0]),
        (i1, i2, STAGE_COLORS[1], STAGE_LABELS[1]),
        (i2, n - 1, STAGE_COLORS[2], STAGE_LABELS[2]),
    ]):
        ax.axvspan(t[s_start], t[min(s_end, n - 1)],
                   alpha=0.2, color=color, label=label)

    # Plot signals
    ax.semilogy(t, np.maximum(e_E, LOG_FLOOR),
                color=SIGNAL_COLORS["E"], linewidth=1.4,
                label=SIGNAL_LABELS["E"])
    ax.semilogy(t, np.maximum(e_D, LOG_FLOOR),
                color=SIGNAL_COLORS["D"], linewidth=1.4,
                label=SIGNAL_LABELS["D"])
    if e_H is not None:
        ax.semilogy(t, np.maximum(e_H, LOG_FLOOR),
                    color=SIGNAL_COLORS["H"], linewidth=1.4,
                    label=SIGNAL_LABELS["H"])

    # Annotate Stage-3 slopes
    y_pos = 0.85
    for sig_name in ana["stage_results"]:
        s3 = ana["stage_results"][sig_name][2]
        color = SIGNAL_COLORS.get(sig_name, "0.3")
        ax.annotate(
            rf"{sig_name}: $\sigma_3 = {-s3['slope']:.4f}$ "
            rf"($R^2 = {s3['R2']:.3f}$, {s3['regime']})",
            xy=(0.02, y_pos), xycoords="axes fraction",
            fontsize=8, color=color,
            bbox=dict(boxstyle="round,pad=0.2", facecolor="white", alpha=0.7),
        )
        y_pos -= 0.06

    setup_axes(
        ax,
        xlabel=r"Time $t$",
        ylabel="Convergence error",
        title=(f"Three-Stage Convergence — D={run['D']}, A={run['A']}, "
               f"Nm={run['Nm']}"),
    )
    ax.legend(fontsize=8, loc="upper right", framealpha=0.9, ncol=2)
    fig.tight_layout()

    fname = "convergence_curves.png"
    fig.savefig(os.path.join(FIG_DIR, fname), dpi=300)
    plt.close(fig)
    print(f"  Saved: {fname}")


# ---------------------------------------------------------------------------
# Figure B: Attractor Stability Scatter (Stage-3 slopes)
# ---------------------------------------------------------------------------
def figure_stability_scatter(runs: list[dict], analyses: list[dict]):
    """Scatter Stage-3 slopes for E, H, D."""
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

    active_signals = list(set(
        sig for ana in analyses for sig in ana["stage_results"]
    ))
    active_signals.sort(key=lambda s: SIGNAL_NAMES.index(s)
                        if s in SIGNAL_NAMES else 99)

    n_sig = len(active_signals)
    fig, axes = plt.subplots(1, n_sig, figsize=(5 * n_sig, 5), squeeze=False)
    axes = axes.flatten()

    for panel_idx, sig_name in enumerate(active_signals):
        ax = axes[panel_idx]

        all_slopes = []

        for run, ana in zip(runs, analyses):
            if sig_name not in ana["stage_results"]:
                continue
            s3 = ana["stage_results"][sig_name][2]
            sigma_3 = -s3["slope"]  # Convention: positive = decaying

            color = D_cmap(D_norm(run["D"]))
            marker = Nm_markers.get(run["Nm"], "o")

            ax.scatter(
                run["D"], sigma_3,
                color=color, marker=marker, s=50, alpha=0.7,
                edgecolors="0.3", linewidths=0.3,
            )
            all_slopes.append(sigma_3)

        # Global mean and std
        if all_slopes:
            mean_s = np.mean(all_slopes)
            std_s = np.std(all_slopes)
            ax.axhline(mean_s, color="0.4", linestyle="--",
                       linewidth=1.0, alpha=0.6)
            ax.axhspan(mean_s - std_s, mean_s + std_s,
                       color="0.7", alpha=0.1)
            ax.annotate(
                rf"$\bar{{\sigma}}_3 = {mean_s:.4f} \pm {std_s:.4f}$",
                xy=(0.02, 0.95), xycoords="axes fraction",
                fontsize=9, color="0.3", va="top",
            )

        setup_axes(
            ax,
            xlabel=r"Diffusion $D$",
            ylabel=rf"Stage-3 rate $\sigma_3$ ({sig_name})",
            title=SIGNAL_LABELS.get(sig_name, sig_name),
        )

    # Colorbar
    sm = plt.cm.ScalarMappable(cmap=D_cmap, norm=D_norm)
    sm.set_array([])
    fig.colorbar(sm, ax=axes.tolist(), label=r"Diffusion $D$",
                 shrink=0.8, pad=0.03)

    fig.suptitle("Stage-3 Convergence Rates — All Admissible Runs",
                 fontsize=14, fontweight="bold", y=1.02)
    fig.tight_layout()

    fname = "stability_scatter.png"
    fig.savefig(os.path.join(FIG_DIR, fname), dpi=300, bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved: {fname}")


# ---------------------------------------------------------------------------
# Figure C: Stability Heatmap
# ---------------------------------------------------------------------------
def figure_stability_heatmap(runs: list[dict], analyses: list[dict]):
    """One panel per Nm; cell = fraction of signals with clean exp Stage 3."""
    Nm_vals = sorted(set(r["Nm"] for r in runs))
    D_vals = sorted(set(r["D"] for r in runs))
    A_vals = sorted(set(r["A"] for r in runs))

    n_Nm = len(Nm_vals)
    if n_Nm == 0:
        print("  SKIP stability heatmap: no data.")
        return

    fig, axes = plt.subplots(
        1, n_Nm,
        figsize=(4.5 * n_Nm + 1, max(3, 0.6 * len(D_vals) + 1.5)),
        squeeze=False,
    )
    axes = axes.flatten()

    for panel_idx, Nm in enumerate(Nm_vals):
        ax = axes[panel_idx]
        grid = np.full((len(D_vals), len(A_vals)), np.nan)

        for run, ana in zip(runs, analyses):
            if run["Nm"] != Nm:
                continue
            di = D_vals.index(run["D"]) if run["D"] in D_vals else None
            ai = A_vals.index(run["A"]) if run["A"] in A_vals else None
            if di is None or ai is None:
                continue
            grid[di, ai] = ana["frac_exp3"]

        ax.imshow(
            grid, aspect="auto", origin="lower",
            cmap=plt.cm.RdYlGn, vmin=0.0, vmax=1.0,
            interpolation="nearest",
        )

        ax.set_xticks(range(len(A_vals)))
        ax.set_xticklabels([f"{a:.3f}" for a in A_vals],
                           fontsize=8, rotation=45)
        ax.set_yticks(range(len(D_vals)))
        ax.set_yticklabels([f"{d:.3f}" for d in D_vals], fontsize=8)

        ax.set_xlabel(r"Amplitude $A$", fontsize=10)
        if panel_idx == 0:
            ax.set_ylabel(r"Diffusion $D$", fontsize=10)
        ax.set_title(rf"$N_m = {Nm}$", fontsize=12, fontweight="bold")

        for di_idx in range(len(D_vals)):
            for ai_idx in range(len(A_vals)):
                val = grid[di_idx, ai_idx]
                if np.isnan(val):
                    ax.text(ai_idx, di_idx, "—", ha="center", va="center",
                            fontsize=8, color="0.5")
                else:
                    n_s = 3  # E, H, D
                    n_conv = int(round(val * n_s))
                    txt_color = "white" if val < 0.4 else "black"
                    ax.text(ai_idx, di_idx, f"{n_conv}/{n_s}",
                            ha="center", va="center", fontsize=8,
                            color=txt_color, fontweight="bold")

    fig.colorbar(
        plt.cm.ScalarMappable(cmap=plt.cm.RdYlGn,
                              norm=mcolors.Normalize(0, 1)),
        ax=axes.tolist(),
        label="Fraction with exponential Stage 3",
        shrink=0.8, pad=0.04,
    )

    fig.suptitle(
        "Convergence Stability — Heatmap by $(D, A, N_m)$",
        fontsize=14, fontweight="bold", y=1.03,
    )
    fig.tight_layout()

    fname = "stability_heatmap.png"
    fig.savefig(os.path.join(FIG_DIR, fname), dpi=300, bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved: {fname}")


# ---------------------------------------------------------------------------
# Summary table and invariance verdict
# ---------------------------------------------------------------------------
def print_summary(runs: list[dict], analyses: list[dict]):
    print(f"\n{'='*150}")
    print("  Invariant Convergence Stability — Summary Table")
    print(f"{'='*150}")

    # Header
    print(f"  {'D':<7} {'A':<7} {'Nm':<5} ", end="")
    for sig in SIGNAL_NAMES:
        for stage in [1, 2, 3]:
            print(f"{'s'+str(stage)+'_'+sig:<10}", end="")
    print(f"{'Exp3':<6} {'Frac':<7}")
    print("  " + "-" * 140)

    # Collect Stage-3 slopes for global statistics
    all_s3 = {sig: [] for sig in SIGNAL_NAMES}

    for run, ana in zip(runs, analyses):
        sr = ana["stage_results"]

        print(f"  {run['D']:<7.3f} {run['A']:<7.4f} {run['Nm']:<5d} ",
              end="")

        for sig in SIGNAL_NAMES:
            if sig in sr:
                for stage_idx in range(3):
                    fit = sr[sig][stage_idx]
                    regime_char = fit["regime"][0].upper()  # F/D/E/N
                    slope = -fit["slope"]  # positive = decaying
                    print(f"{slope:+7.4f}{regime_char:<3}", end="")

                # Collect Stage-3 slope
                s3_slope = -sr[sig][2]["slope"]
                if sr[sig][2]["regime"] == "exponential":
                    all_s3[sig].append(s3_slope)
            else:
                print(f"{'—':<30}", end="")

        n_exp = ana["n_exp3"]
        print(f"{n_exp:<6d} {ana['frac_exp3']:<7.1%}")

    # --- Global statistics for Stage-3 slopes ---
    print(f"\n  Stage-3 Exponential Rates (clean exponential runs only):")
    print(f"  {'Signal':<10} {'Mean':<12} {'Std':<12} "
          f"{'Min':<12} {'Max':<12} {'CV':<10} {'N':<6} {'Verdict'}")
    print("  " + "-" * 80)

    for sig in SIGNAL_NAMES:
        arr = np.array(all_s3[sig])
        if len(arr) == 0:
            print(f"  {sig:<10} (no clean exponential fits)")
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

        print(f"  {sig:<10} "
              f"{mean_v:<12.6f} {std_v:<12.6f} "
              f"{np.min(arr):<12.6f} {np.max(arr):<12.6f} "
              f"{cv:<10.4f} {len(arr):<6d} {verdict}")

    # Overall
    total_signals = sum(ana["n_signals"] for ana in analyses)
    total_exp3 = sum(ana["n_exp3"] for ana in analyses)
    print(f"\n  Overall Stage-3 exponential: {total_exp3}/{total_signals} "
          f"({100*total_exp3/max(total_signals,1):.1f}%)")


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
    print(f"  D range:  {min(r['D'] for r in runs):.3f} – "
          f"{max(r['D'] for r in runs):.3f}")
    print(f"  A range:  {min(r['A'] for r in runs):.4f} – "
          f"{max(r['A'] for r in runs):.4f}")
    print(f"  Nm range: {min(r['Nm'] for r in runs)} – "
          f"{max(r['Nm'] for r in runs)}")

    # Analyse all runs
    print("\nAnalysing convergence stability...")
    analyses = []
    for i, run in enumerate(runs):
        ana = analyse_run(run)
        analyses.append(ana)
        if (i + 1) % 10 == 0 or i == len(runs) - 1:
            n_e = ana["n_exp3"]
            n_s = ana["n_signals"]
            print(f"  [{i+1}/{len(runs)}] {run['name']}: "
                  f"{n_e}/{n_s} exponential Stage 3")

    # Figures
    print("\n--- (A) Convergence Curves ---")
    figure_convergence_curves(runs, analyses)

    print("\n--- (B) Stability Scatter ---")
    figure_stability_scatter(runs, analyses)

    print("\n--- (C) Stability Heatmap ---")
    figure_stability_heatmap(runs, analyses)

    # Summary
    print_summary(runs, analyses)

    print(f"\nAll figures saved to: {FIG_DIR}")
    print("Done.")


if __name__ == "__main__":
    main()
