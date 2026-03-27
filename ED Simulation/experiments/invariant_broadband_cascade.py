"""
invariant_broadband_cascade.py
===============================
Experiment / Analysis: Invariant Broadband Cascade Structure

Scans all completed regime_D*_A*_Nm* runs, groups modal energies into
logarithmic spectral bins, computes the bin energy ratios

    R_b(t) = B_b(t) / E_total(t)

where B_b(t) = Σ_{k in bin b} |a_k(t)|², and analyses their convergence
toward late-time attractor values R_b^*.

The logarithmic binning compresses the full modal spectrum into a small
number of scale-ordered bins, revealing the broadband cascade structure:
how energy is distributed across octaves of wavenumber.  The attractor
profile (R_1^*, ..., R_B^*) is a coarse-grained spectral invariant of
the ED architecture (Appendix C.4, Proposition C.29).

Bin definitions:
  Bin 1:  k = 1–2     (largest scales)
  Bin 2:  k = 3–4
  Bin 3:  k = 5–8
  Bin 4:  k = 9–16
  Bin 5:  k = 17–32   (smallest scales in the Atlas)

Produces:
  (A) Cascade Evolution — R_b(t) for a representative run.
  (B) Attractor Cascade Profile — polylines for all runs.
  (C) Convergence Heatmap — fraction converged across (D, A, Nm).

All figures saved to output/figures/invariants/broadband_cascade/
as PNG (300 dpi).

Usage:
    python experiments/invariant_broadband_cascade.py

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
                        "broadband_cascade")

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
# Logarithmic bin edges (inclusive): (k_lo, k_hi)
BIN_DEFS = [
    (1, 2),
    (3, 4),
    (5, 8),
    (9, 16),
    (17, 32),
]
BIN_LABELS = [
    "1–2", "3–4", "5–8", "9–16", "17–32",
]

LATE_FRAC = 0.10
FIT_FRAC = 0.20
R2_THRESH = 0.95
E_FLOOR = 1e-30

BIN_COLORS = ["#1b9e77", "#d95f02", "#7570b3", "#e7298a", "#66a61e"]


# ---------------------------------------------------------------------------
# Discovery
# ---------------------------------------------------------------------------
def discover_regime_runs() -> list[dict]:
    """Scan RUNS_DIR for regime_D*_A*_Nm* folders with modal data."""
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
        modal = ts.get("modal_amplitudes")
        t = ts.get("t")

        if modal is None or t is None or modal.ndim != 2:
            continue

        n = min(len(t), modal.shape[0])
        if modal.shape[1] < 3 or n < 50:
            continue

        runs.append({
            "dir": d,
            "name": name,
            "D": float(D_val),
            "A": float(A_val),
            "Nm": int(Nm_val),
            "metadata": meta,
            "t": t[:n],
            "modal": modal[:n],
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
# Bin construction
# ---------------------------------------------------------------------------
def get_active_bins(n_modes: int) -> list[dict]:
    """Return the list of active bins given the number of available modes.

    Each entry: {"idx": int, "label": str, "k_lo": int, "k_hi": int,
                 "cols": list[int]}
    where cols are the column indices into the modal array (0-based).
    """
    bins = []
    for idx, (k_lo, k_hi) in enumerate(BIN_DEFS):
        if k_lo >= n_modes:
            break  # no modes in this bin
        k_hi_clamp = min(k_hi, n_modes - 1)
        cols = list(range(k_lo, k_hi_clamp + 1))
        if not cols:
            break
        bins.append({
            "idx": idx,
            "label": BIN_LABELS[idx],
            "k_lo": k_lo,
            "k_hi": k_hi_clamp,
            "cols": cols,
        })
    return bins


# ---------------------------------------------------------------------------
# Per-run analysis (streaming over bins)
# ---------------------------------------------------------------------------
def analyse_run(run: dict) -> dict:
    """Compute bin energy ratios and attractor summaries.

    Streams one bin at a time: sums E_k over the bin's modes, divides
    by E_total, extracts R_b^*, fits convergence, discards ratio array.
    """
    modal = run["modal"]
    t = run["t"]
    n_steps, n_modes = modal.shape

    active_bins = get_active_bins(n_modes)
    n_bins = len(active_bins)

    # Total energy (k >= 1)
    E_total = np.sum(modal[:, 1:] ** 2, axis=1)
    E_total = np.maximum(E_total, E_FLOOR)

    bins_result = []
    n_converged = 0

    for b in active_bins:
        # Bin energy: sum of |a_k|^2 over the bin's modes
        B_b = np.sum(modal[:, b["cols"]] ** 2, axis=1)

        # Bin ratio
        R_b = B_b / E_total

        # Late-time average
        start = max(0, int((1.0 - LATE_FRAC) * len(R_b)))
        R_star = float(np.mean(R_b[start:]))

        # Convergence fit
        fit = _fit_exponential(t, R_b, R_star)

        bins_result.append({
            "idx": b["idx"],
            "label": b["label"],
            "R_star": R_star,
            "sigma": fit["sigma"],
            "R2": fit["R2"],
            "converged": fit["converged"],
        })
        if fit["converged"]:
            n_converged += 1

        del B_b, R_b

    del E_total

    frac = n_converged / max(n_bins, 1)

    return {
        "bins": bins_result,
        "n_bins": n_bins,
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
# Figure A: Cascade Evolution (representative run)
# ---------------------------------------------------------------------------
def figure_cascade_evolution(runs: list[dict], analyses: list[dict]):
    """Plot R_b(t) for all bins on semilog-y for the run with largest Nm.

    Recomputes ratios on-the-fly.
    """
    best_idx = max(range(len(runs)), key=lambda i: runs[i]["Nm"])
    run = runs[best_idx]
    ana = analyses[best_idx]

    t = run["t"]
    modal = run["modal"]
    n_steps, n_modes = modal.shape

    active_bins = get_active_bins(n_modes)
    E_total = np.maximum(np.sum(modal[:, 1:] ** 2, axis=1), E_FLOOR)

    fig, ax = plt.subplots(figsize=(10, 6))

    for b_info, b_result in zip(active_bins, ana["bins"]):
        B_b = np.sum(modal[:, b_info["cols"]] ** 2, axis=1)
        R_b = B_b / E_total
        R_star = b_result["R_star"]

        color = BIN_COLORS[b_info["idx"] % len(BIN_COLORS)]

        ax.semilogy(
            t, np.maximum(R_b, 1e-30),
            color=color, linewidth=1.5,
            label=rf"Bin {b_info['idx']+1}: $k = {b_info['label']}$",
        )

        if R_star > 1e-20:
            ax.axhline(
                R_star, color=color, linestyle="--",
                linewidth=0.8, alpha=0.5,
            )

        del B_b, R_b

    del E_total

    # Partition-sum annotation
    total_R = sum(b["R_star"] for b in ana["bins"])
    ax.annotate(
        rf"$\Sigma R_b^* = {total_R:.4f}$",
        xy=(0.02, 0.05), xycoords="axes fraction",
        fontsize=9, color="0.4",
        bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.7),
    )

    setup_axes(
        ax,
        xlabel=r"Time $t$",
        ylabel=r"Bin ratio $R_b(t) = B_b / E_{\mathrm{total}}$",
        title=(f"Broadband Cascade — D={run['D']}, A={run['A']}, "
               f"Nm={run['Nm']} ({ana['n_bins']} bins)"),
    )
    ax.legend(fontsize=9, loc="center right", framealpha=0.9)
    fig.tight_layout()

    fname = "cascade_evolution.png"
    fig.savefig(os.path.join(FIG_DIR, fname), dpi=300)
    plt.close(fig)
    print(f"  Saved: {fname}")


# ---------------------------------------------------------------------------
# Figure B: Attractor Cascade Profile (all runs overlaid)
# ---------------------------------------------------------------------------
def figure_attractor_profile(runs: list[dict], analyses: list[dict]):
    """Polylines (R_1^*, ..., R_B^*) for all runs on semilog-y."""
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

    max_bins = max(ana["n_bins"] for ana in analyses)

    fig, ax = plt.subplots(figsize=(10, 6))

    all_profiles = []

    for run, ana in zip(runs, analyses):
        n_b = ana["n_bins"]
        x_axis = np.arange(n_b)
        profile = np.array([b["R_star"] for b in ana["bins"]])

        color = D_cmap(D_norm(run["D"]))
        marker = Nm_markers.get(run["Nm"], "o")

        ax.semilogy(
            x_axis, np.maximum(profile, 1e-30),
            color=color, marker=marker, markersize=5,
            linewidth=0.7, alpha=0.4,
        )

        padded = np.full(max_bins, np.nan)
        padded[:n_b] = profile
        all_profiles.append(padded)

    # Mean profile
    if all_profiles:
        stacked = np.array(all_profiles)
        with np.errstate(all="ignore"):
            mean_profile = np.nanmean(stacked, axis=0)
        x_full = np.arange(max_bins)
        valid = ~np.isnan(mean_profile) & (mean_profile > 1e-30)

        ax.semilogy(
            x_full[valid], mean_profile[valid],
            color="black", marker="o", markersize=7,
            linewidth=2.5, alpha=0.9, zorder=10,
            label="Mean profile",
        )

    # X-axis labels
    tick_labels = BIN_LABELS[:max_bins]
    ax.set_xticks(range(max_bins))
    ax.set_xticklabels(tick_labels, fontsize=10)

    # Colorbar
    sm = plt.cm.ScalarMappable(cmap=D_cmap, norm=D_norm)
    sm.set_array([])
    cbar = fig.colorbar(sm, ax=ax, label=r"Diffusion $D$", pad=0.02)
    cbar.ax.tick_params(labelsize=9)

    # Marker legend
    legend_handles = [
        plt.Line2D([0], [0], marker=m, color="0.5", markersize=7,
                   linestyle="None", label=rf"$N_m = {Nm}$")
        for Nm, m in Nm_markers.items()
    ]
    legend_handles.append(
        plt.Line2D([0], [0], color="black", marker="o", markersize=7,
                   linewidth=2.5, label="Mean profile")
    )
    ax.legend(
        handles=legend_handles, fontsize=8, loc="upper right",
        framealpha=0.9, title="Legend",
    )

    setup_axes(
        ax,
        xlabel="Spectral bin (mode range)",
        ylabel=r"Attractor bin ratio $R_b^*$",
        title="Broadband Cascade Attractor — All Admissible Runs",
    )
    fig.tight_layout()

    fname = "attractor_profile.png"
    fig.savefig(os.path.join(FIG_DIR, fname), dpi=300)
    plt.close(fig)
    print(f"  Saved: {fname}")


# ---------------------------------------------------------------------------
# Figure C: Convergence Heatmap
# ---------------------------------------------------------------------------
def figure_convergence_heatmap(runs: list[dict], analyses: list[dict]):
    """One panel per Nm; cell = fraction of bins converged."""
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
                    # Find n_bins for this cell
                    n_b = len(BIN_DEFS)
                    for run2, ana2 in zip(runs, analyses):
                        if (run2["Nm"] == Nm and
                                run2["D"] == D_vals[di_idx] and
                                run2["A"] == A_vals[ai_idx]):
                            n_b = ana2["n_bins"]
                            break
                    n_conv = int(round(val * n_b))
                    txt_color = "white" if val < 0.4 else "black"
                    ax.text(ai_idx, di_idx, f"{n_conv}/{n_b}",
                            ha="center", va="center", fontsize=8,
                            color=txt_color, fontweight="bold")

    fig.colorbar(
        plt.cm.ScalarMappable(cmap=plt.cm.RdYlGn,
                              norm=mcolors.Normalize(0, 1)),
        ax=axes.tolist(), label="Fraction of bins converged",
        shrink=0.8, pad=0.04,
    )

    fig.suptitle(
        "Broadband Cascade Convergence — Heatmap by $(D, A, N_m)$",
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
    max_bins = max(ana["n_bins"] for ana in analyses)

    print(f"\n{'='*120}")
    print("  Invariant Broadband Cascade — Summary Table")
    print(f"{'='*120}")

    bin_hdr = "  ".join(f"R_{BIN_LABELS[i]}" for i in range(max_bins))
    print(f"  {'D':<7} {'A':<7} {'Nm':<5} {'#B':<4} "
          f"{'Conv':<8} {'Frac':<7} ", end="")
    for i in range(max_bins):
        print(f"{'R_'+BIN_LABELS[i]:<12}", end="")
    print()
    print("  " + "-" * (48 + 12 * max_bins))

    all_R = {i: [] for i in range(max_bins)}

    for run, ana in zip(runs, analyses):
        n_b = ana["n_bins"]

        conv_str = ""
        for b in ana["bins"]:
            conv_str += "+" if b["converged"] else "."

        print(f"  {run['D']:<7.3f} {run['A']:<7.4f} {run['Nm']:<5d} "
              f"{n_b:<4d} {conv_str:<8} {ana['frac_converged']:<7.1%} ",
              end="")

        for i in range(max_bins):
            if i < n_b:
                R_s = ana["bins"][i]["R_star"]
                print(f"{R_s:<12.6f}", end="")
                all_R[i].append(R_s)
            else:
                print(f"{'—':<12}", end="")
        print()

    # --- Global statistics per bin ---
    print(f"\n  {'Bin':<12} {'Mean':<12} {'Std':<12} "
          f"{'Min':<12} {'Max':<12} {'CV':<10} {'Verdict'}")
    print("  " + "-" * 76)

    for i in range(max_bins):
        arr = np.array(all_R[i])
        if len(arr) == 0:
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

        print(f"  k={BIN_LABELS[i]:<8} "
              f"{mean_v:<12.6f} {std_v:<12.6f} "
              f"{np.min(arr):<12.6f} {np.max(arr):<12.6f} "
              f"{cv:<10.4f} {verdict}")

    # Partition sum check
    means = [np.mean(all_R[i]) for i in range(max_bins) if len(all_R[i]) > 0]
    total_mean = sum(means)
    print(f"\n  Partition sum check: Σ R_b^* = {total_mean:.6f} "
          f"(expected: ≤ 1.000000)")

    # Overall convergence
    total = sum(ana["n_bins"] for ana in analyses)
    total_conv = sum(ana["n_converged"] for ana in analyses)
    print(f"  Overall convergence: {total_conv}/{total} "
          f"({100*total_conv/max(total,1):.1f}%)")


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

    # --- Analyse all runs ---
    print("\nComputing broadband cascade ratios...")
    analyses = []
    for i, run in enumerate(runs):
        ana = analyse_run(run)
        analyses.append(ana)
        if (i + 1) % 10 == 0 or i == len(runs) - 1:
            n_c = ana["n_converged"]
            n_b = ana["n_bins"]
            print(f"  [{i+1}/{len(runs)}] {run['name']}: "
                  f"{n_b} bins, {n_c}/{n_b} converged")

    # --- Figures ---
    print("\n--- (A) Cascade Evolution ---")
    figure_cascade_evolution(runs, analyses)

    print("\n--- (B) Attractor Cascade Profile ---")
    figure_attractor_profile(runs, analyses)

    print("\n--- (C) Convergence Heatmap ---")
    figure_convergence_heatmap(runs, analyses)

    # --- Summary ---
    print_summary(runs, analyses)

    print(f"\nAll figures saved to: {FIG_DIR}")
    print("Done.")


if __name__ == "__main__":
    main()
