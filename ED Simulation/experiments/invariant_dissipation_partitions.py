"""
invariant_dissipation_partitions.py
====================================
Experiment / Analysis: Invariant Dissipation Partition Structure

Scans all completed regime_D*_A*_Nm* runs, computes the three dissipation
ratios

    R_grad(t) = D_grad(t) / D_total(t)
    R_pen(t)  = D_pen(t)  / D_total(t)
    R_part(t) = D_part(t) / D_total(t)

and analyses their convergence toward late-time attractor values.

Produces:
  (A) Dissipation Ratio Evolution -- R(t) for a representative run.
  (B) Attractor Partition Profile -- R^* vs D for all runs.
  (C) Convergence Heatmap -- fraction converged across (D, A, Nm).

Also prints a summary table with invariance verdicts.

All figures saved to output/figures/invariants/dissipation_partitions/
as PNG (300 dpi).

Usage:
    python experiments/invariant_dissipation_partitions.py

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
SIM_DIR = os.path.dirname(SCRIPT_DIR)  # ED Simulation/
RUNS_DIR = os.path.join(SIM_DIR, "output", "runs")
FIG_DIR = os.path.join(SIM_DIR, "output", "figures", "invariants",
                        "dissipation_partitions")

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
LATE_FRAC = 0.10        # Fraction of time series for late-time average
FIT_FRAC = 0.20         # Fraction for convergence-rate fit
R2_THRESH = 0.95        # R^2 threshold for declaring convergence
D_TOTAL_FLOOR = 1e-30   # Floor to avoid division by zero in ratios

CHANNEL_NAMES = ["grad", "pen", "part"]
CHANNEL_FIELDS = {
    "grad": "D_gradient",
    "pen":  "D_penalty",
    "part": "D_participation",
}
CHANNEL_LABELS = {
    "grad": r"$R_{\mathrm{grad}}$",
    "pen":  r"$R_{\mathrm{pen}}$",
    "part": r"$R_{\mathrm{part}}$",
}
CHANNEL_COLORS = {
    "grad": "#2166ac",
    "pen":  "#b2182b",
    "part": "#1b7837",
}


# ---------------------------------------------------------------------------
# Discovery (shared pattern)
# ---------------------------------------------------------------------------
def discover_regime_runs() -> list[dict]:
    """Scan RUNS_DIR for regime_D*_A*_Nm* folders with valid dissipation data.

    Returns a sorted list of dicts with keys:
        dir, name, D, A, Nm, metadata, t, channels
    where channels = {"grad": array, "pen": array, "part": array,
                      "total": array}.
    """
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

        if meta.get("inadmissible", False):
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
        if t is None:
            continue

        # Load dissipation channels
        channels = {}
        missing = False
        for ch_name, field in CHANNEL_FIELDS.items():
            arr = ts.get(field)
            if arr is None:
                missing = True
                break
            channels[ch_name] = arr
        if missing:
            continue

        D_total = ts.get("D_total")
        if D_total is None:
            # Reconstruct from components
            D_total = (channels["grad"] + channels["pen"] + channels["part"])
        channels["total"] = D_total

        # Trim to consistent length
        n = min(len(t), *(len(channels[c]) for c in channels))
        if n < 50:
            continue

        trimmed = {c: channels[c][:n] for c in channels}

        runs.append({
            "dir": d,
            "name": name,
            "D": float(D_val),
            "A": float(A_val),
            "Nm": int(Nm_val),
            "metadata": meta,
            "t": t[:n],
            "channels": trimmed,
        })

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


# ---------------------------------------------------------------------------
# Streaming per-run analysis (no bulk storage of ratio time series)
# ---------------------------------------------------------------------------
def analyse_run(run: dict) -> dict:
    """Compute dissipation ratios and their attractor summaries.

    Streams through the three channels, computes ratio, extracts summary,
    discards the ratio time series.  Peak memory: O(n_timesteps).

    Returns dict with:
        partition: {"grad": {...}, "pen": {...}, "part": {...}}
            each containing: R_star, sigma, R2, converged
        n_converged, frac_converged
    """
    t = run["t"]
    ch = run["channels"]
    D_total = np.maximum(ch["total"], D_TOTAL_FLOOR)

    partition = {}
    n_converged = 0

    for ch_name in CHANNEL_NAMES:
        # Compute ratio (temporary)
        R = ch[ch_name] / D_total

        # Late-time average
        start = max(0, int((1.0 - LATE_FRAC) * len(R)))
        R_star = float(np.mean(R[start:]))

        # Convergence fit
        fit = _fit_exponential(t, R, R_star)

        partition[ch_name] = {
            "R_star": R_star,
            "sigma": fit["sigma"],
            "R2": fit["R2"],
            "converged": fit["converged"],
        }
        if fit["converged"]:
            n_converged += 1

        del R  # discard ratio array

    frac = n_converged / 3.0

    return {
        "partition": partition,
        "n_converged": n_converged,
        "frac_converged": frac,
    }


def _fit_exponential(t: np.ndarray, arr: np.ndarray,
                     target: float) -> dict:
    """Fit |arr(t) - target| ~ C exp(-sigma t) over the last FIT_FRAC."""
    result = {"sigma": 0.0, "R2": 0.0, "converged": False}

    n = len(t)
    start = max(0, int((1.0 - FIT_FRAC) * n))
    t_fit = t[start:]
    residual = np.abs(arr[start:] - target)

    valid = residual > 1e-30
    if np.sum(valid) < 10:
        return result

    log_r = np.log(residual[valid])
    t_v = t_fit[valid]

    try:
        coeffs = np.polyfit(t_v, log_r, 1)
        sigma = -coeffs[0]

        predicted = coeffs[0] * t_v + coeffs[1]
        ss_res = np.sum((log_r - predicted) ** 2)
        ss_tot = np.sum((log_r - np.mean(log_r)) ** 2)
        R2 = 1.0 - ss_res / max(ss_tot, 1e-30)

        result["sigma"] = float(sigma)
        result["R2"] = float(R2)
        result["converged"] = R2 > R2_THRESH and sigma > 0
    except (np.linalg.LinAlgError, ValueError):
        pass

    return result


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
# Figure A: Dissipation Ratio Evolution (representative run)
# ---------------------------------------------------------------------------
def figure_ratio_evolution(runs: list[dict], analyses: list[dict]):
    """Plot R_grad(t), R_pen(t), R_part(t) for the run with largest Nm.

    Recomputes ratio time series on-the-fly for the single representative
    run.  Memory: O(n_timesteps).
    """
    best_idx = max(range(len(runs)), key=lambda i: runs[i]["Nm"])
    run = runs[best_idx]
    ana = analyses[best_idx]

    t = run["t"]
    ch = run["channels"]
    D_total = np.maximum(ch["total"], D_TOTAL_FLOOR)

    fig, ax = plt.subplots(figsize=(10, 6))

    for ch_name in CHANNEL_NAMES:
        R = ch[ch_name] / D_total
        R_star = ana["partition"][ch_name]["R_star"]

        ax.plot(
            t, R,
            color=CHANNEL_COLORS[ch_name], linewidth=1.4,
            label=CHANNEL_LABELS[ch_name],
        )

        # Horizontal dashed line at attractor value
        ax.axhline(
            R_star,
            color=CHANNEL_COLORS[ch_name], linestyle="--",
            linewidth=0.9, alpha=0.6,
        )

        # Annotate the attractor value
        ax.annotate(
            rf"{R_star:.3f}",
            xy=(t[-1], R_star),
            xytext=(8, 0), textcoords="offset points",
            fontsize=8, color=CHANNEL_COLORS[ch_name],
            va="center",
        )

        del R

    # Verification: R_grad + R_pen + R_part ~= 1
    ax.axhline(1.0, color="0.6", linestyle=":", linewidth=0.6, alpha=0.4)

    setup_axes(
        ax,
        xlabel=r"Time $t$",
        ylabel="Dissipation ratio",
        title=(f"Dissipation Partitions -- D={run['D']}, A={run['A']}, "
               f"Nm={run['Nm']}"),
    )
    ax.legend(fontsize=10, loc="center right", framealpha=0.9)
    ax.set_ylim(-0.05, 1.05)
    fig.tight_layout()

    fname = "ratio_evolution.png"
    fig.savefig(os.path.join(FIG_DIR, fname), dpi=300)
    plt.close(fig)
    print(f"  Saved: {fname}")


# ---------------------------------------------------------------------------
# Figure B: Attractor Partition Profile (R^* vs D, all runs)
# ---------------------------------------------------------------------------
def figure_attractor_profile(runs: list[dict], analyses: list[dict]):
    """Three-panel scatter: R_grad^*, R_pen^*, R_part^* vs D."""
    A_vals = sorted(set(r["A"] for r in runs))
    Nm_vals = sorted(set(r["Nm"] for r in runs))

    A_cmap = plt.cm.viridis
    A_norm = mcolors.Normalize(
        vmin=min(A_vals) * 0.8 if A_vals else 0,
        vmax=max(A_vals) * 1.2 if A_vals else 1,
    )
    Nm_markers = {Nm_vals[i]: m for i, m in
                  zip(range(len(Nm_vals)),
                      ["o", "s", "^", "D", "v", "P", "*"])}

    fig, axes = plt.subplots(1, 3, figsize=(16, 5), sharey=True)

    for panel_idx, ch_name in enumerate(CHANNEL_NAMES):
        ax = axes[panel_idx]

        # Compute global mean for this channel
        all_R = [ana["partition"][ch_name]["R_star"]
                 for ana in analyses
                 if not np.isnan(ana["partition"][ch_name]["R_star"])]
        global_mean = np.mean(all_R) if all_R else np.nan

        for run, ana in zip(runs, analyses):
            R_star = ana["partition"][ch_name]["R_star"]
            if np.isnan(R_star):
                continue

            color = A_cmap(A_norm(run["A"]))
            marker = Nm_markers.get(run["Nm"], "o")

            ax.scatter(
                run["D"], R_star,
                color=color, marker=marker, s=50, alpha=0.7,
                edgecolors="0.3", linewidths=0.4,
            )

        # Global mean line
        if not np.isnan(global_mean):
            ax.axhline(global_mean, color="0.4", linestyle="--",
                       linewidth=1.0, alpha=0.6)
            ax.annotate(
                rf"mean = {global_mean:.4f}",
                xy=(0.98, global_mean),
                xycoords=("axes fraction", "data"),
                fontsize=8, color="0.3", ha="right",
                va="bottom" if panel_idx != 2 else "top",
            )

        setup_axes(
            ax,
            xlabel=r"Diffusion $D$",
            ylabel=CHANNEL_LABELS[ch_name] + r"$^*$" if panel_idx == 0 else "",
            title=CHANNEL_LABELS[ch_name] + r"$^*$ vs $D$",
        )

    # Shared colorbar for A
    sm = plt.cm.ScalarMappable(cmap=A_cmap, norm=A_norm)
    sm.set_array([])
    cbar = fig.colorbar(sm, ax=axes.tolist(), label=r"Amplitude $A$",
                        shrink=0.8, pad=0.03)
    cbar.ax.tick_params(labelsize=9)

    # Marker legend for Nm
    legend_handles = []
    for Nm, marker in Nm_markers.items():
        h = plt.Line2D(
            [0], [0], marker=marker, color="0.5", markersize=7,
            linestyle="None", label=rf"$N_m = {Nm}$",
        )
        legend_handles.append(h)
    axes[2].legend(
        handles=legend_handles, fontsize=8, loc="upper right",
        framealpha=0.9, title="Seed count",
    )

    fig.suptitle("Dissipation Partition Attractor Profile -- All Admissible Runs",
                 fontsize=14, fontweight="bold", y=1.02)
    fig.tight_layout()

    fname = "attractor_profile.png"
    fig.savefig(os.path.join(FIG_DIR, fname), dpi=300, bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved: {fname}")


# ---------------------------------------------------------------------------
# Figure C: Convergence Heatmap
# ---------------------------------------------------------------------------
def figure_convergence_heatmap(runs: list[dict], analyses: list[dict]):
    """One panel per Nm; cell color = fraction of 3 ratios that converged."""
    Nm_vals = sorted(set(r["Nm"] for r in runs))
    D_vals = sorted(set(r["D"] for r in runs))
    A_vals = sorted(set(r["A"] for r in runs))

    n_Nm = len(Nm_vals)
    if n_Nm == 0:
        print("  SKIP convergence heatmap: no data.")
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
            grid[di, ai] = ana["frac_converged"]

        im = ax.imshow(
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

        # Cell annotations
        for di_idx in range(len(D_vals)):
            for ai_idx in range(len(A_vals)):
                val = grid[di_idx, ai_idx]
                if np.isnan(val):
                    ax.text(ai_idx, di_idx, "--", ha="center", va="center",
                            fontsize=8, color="0.5")
                else:
                    txt_color = "white" if val < 0.4 else "black"
                    # Show as fraction out of 3 (e.g., "3/3", "2/3")
                    n_conv = int(round(val * 3))
                    ax.text(ai_idx, di_idx, f"{n_conv}/3", ha="center",
                            va="center", fontsize=8, color=txt_color,
                            fontweight="bold")

    fig.colorbar(
        plt.cm.ScalarMappable(cmap=plt.cm.RdYlGn,
                              norm=mcolors.Normalize(0, 1)),
        ax=axes.tolist(), label="Fraction of ratios converged",
        shrink=0.8, pad=0.04,
    )

    fig.suptitle(
        "Dissipation Partition Convergence -- Heatmap by $(D, A, N_m)$",
        fontsize=14, fontweight="bold", y=1.03,
    )
    fig.tight_layout()

    fname = "convergence_heatmap.png"
    fig.savefig(os.path.join(FIG_DIR, fname), dpi=300, bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved: {fname}")


# ---------------------------------------------------------------------------
# Summary table and invariance verdict
# ---------------------------------------------------------------------------
def print_summary(runs: list[dict], analyses: list[dict]):
    print(f"\n{'='*110}")
    print("  Invariant Dissipation Partitions -- Summary Table")
    print(f"{'='*110}")

    header = (f"  {'D':<7} {'A':<7} {'Nm':<5} "
              f"{'R_grad*':<10} {'R_pen*':<10} {'R_part*':<10} "
              f"{'Conv':<6} {'Frac':<8} {'Regime':<12}")
    print(header)
    print("  " + "-" * 80)

    # Collect per-channel attractor values for global statistics
    all_R = {ch: [] for ch in CHANNEL_NAMES}

    for run, ana in zip(runs, analyses):
        p = ana["partition"]
        regime = run["metadata"].get("effective_regime", run["metadata"].get("regime", "--"))

        # Convergence flag string (e.g., "GPC" = grad+pen+part converged)
        conv_str = ""
        for ch in CHANNEL_NAMES:
            conv_str += ch[0].upper() if p[ch]["converged"] else "."

        print(f"  {run['D']:<7.3f} {run['A']:<7.4f} {run['Nm']:<5d} "
              f"{p['grad']['R_star']:<10.6f} "
              f"{p['pen']['R_star']:<10.6f} "
              f"{p['part']['R_star']:<10.6f} "
              f"{conv_str:<6} "
              f"{ana['frac_converged']:<8.1%} "
              f"{regime:<12}")

        for ch in CHANNEL_NAMES:
            val = p[ch]["R_star"]
            if not np.isnan(val):
                all_R[ch].append(val)

    # --- Global statistics and invariance verdict ---
    print(f"\n  {'Channel':<16} {'Mean':<12} {'Std':<12} "
          f"{'Min':<12} {'Max':<12} {'CV':<10} {'Verdict'}")
    print("  " + "-" * 86)

    for ch in CHANNEL_NAMES:
        arr = np.array(all_R[ch])
        if len(arr) == 0:
            print(f"  {CHANNEL_LABELS[ch]:<16} (no data)")
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

        print(f"  {CHANNEL_LABELS[ch]:<16} "
              f"{mean_v:<12.6f} {std_v:<12.6f} "
              f"{np.min(arr):<12.6f} {np.max(arr):<12.6f} "
              f"{cv:<10.4f} {verdict}")

    # Partition sum check
    sum_means = sum(np.mean(all_R[ch]) for ch in CHANNEL_NAMES
                    if len(all_R[ch]) > 0)
    print(f"\n  Partition sum check: "
          f"R_grad* + R_pen* + R_part* = {sum_means:.6f} "
          f"(expected: 1.000000)")

    # Overall convergence
    total_ratios = len(runs) * 3
    total_conv = sum(ana["n_converged"] for ana in analyses)
    print(f"  Overall convergence: {total_conv}/{total_ratios} "
          f"({100*total_conv/max(total_ratios,1):.1f}%)")


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
    print(f"  D range:  {min(r['D'] for r in runs):.3f} - "
          f"{max(r['D'] for r in runs):.3f}")
    print(f"  A range:  {min(r['A'] for r in runs):.4f} - "
          f"{max(r['A'] for r in runs):.4f}")
    print(f"  Nm range: {min(r['Nm'] for r in runs)} - "
          f"{max(r['Nm'] for r in runs)}")

    # --- Analyse all runs (streaming) ---
    print("\nComputing dissipation partitions...")
    analyses = []
    for i, run in enumerate(runs):
        ana = analyse_run(run)
        analyses.append(ana)
        if (i + 1) % 10 == 0 or i == len(runs) - 1:
            p = ana["partition"]
            print(f"  [{i+1}/{len(runs)}] {run['name']}: "
                  f"R_g={p['grad']['R_star']:.4f} "
                  f"R_p={p['pen']['R_star']:.4f} "
                  f"R_v={p['part']['R_star']:.4f} "
                  f"({ana['n_converged']}/3 converged)")

    # --- Figures ---
    print("\n--- (A) Dissipation Ratio Evolution ---")
    figure_ratio_evolution(runs, analyses)

    print("\n--- (B) Attractor Partition Profile ---")
    figure_attractor_profile(runs, analyses)

    print("\n--- (C) Convergence Heatmap ---")
    figure_convergence_heatmap(runs, analyses)

    # --- Summary ---
    print_summary(runs, analyses)

    print(f"\nAll figures saved to: {FIG_DIR}")
    print("Done.")


if __name__ == "__main__":
    main()
