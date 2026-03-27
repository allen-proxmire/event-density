"""
invariant_low_mode_collapse.py
===============================
Experiment / Analysis: Invariant Low-Mode Collapse Structure

Scans all completed regime_D*_A*_Nm* runs, extracts the first six modal
amplitudes m_k(t) = |a_k(t)| for k = 0..5, and analyses their convergence
toward late-time attractor values m_k^*.

The low-mode attractor profile (m_0^*, ..., m_5^*) encodes the
asymptotic spectral shape at the largest scales — a structural invariant
of the ED architecture (Appendix C.4, Proposition C.29; Appendix C.7,
Theorem C.76).

Produces:
  (A) Low-Mode Evolution — m_k(t) for a representative run.
  (B) Attractor Low-Mode Profile — 6-point polylines for all runs.
  (C) Convergence Heatmap — fraction converged across (D, A, Nm).

All figures saved to output/figures/invariants/low_mode_collapse/
as PNG (300 dpi).

Usage:
    python experiments/invariant_low_mode_collapse.py

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
                        "low_mode_collapse")

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
N_LOW = 6                # Number of low modes to track (k = 0..5)
LATE_FRAC = 0.10         # Fraction for late-time average
FIT_FRAC = 0.20          # Fraction for convergence fit
R2_THRESH = 0.95         # R² threshold for convergence

MODE_COLORS = ["#1b9e77", "#d95f02", "#7570b3",
               "#e7298a", "#66a61e", "#e6ab02"]
MODE_LABELS = [rf"$|a_{{{k}}}|$" for k in range(N_LOW)]


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
        if modal.shape[1] < N_LOW or n < 50:
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
# Per-run analysis (streaming over modes)
# ---------------------------------------------------------------------------
def analyse_run(run: dict) -> dict:
    """Compute low-mode attractor values and convergence for k = 0..5.

    Processes one mode at a time; retains only scalar summaries.
    """
    modal = run["modal"]
    t = run["t"]

    modes = []
    n_converged = 0

    for k in range(N_LOW):
        m_k = np.abs(modal[:, k])

        # Late-time average
        start = max(0, int((1.0 - LATE_FRAC) * len(m_k)))
        m_star = float(np.mean(m_k[start:]))

        # Convergence fit
        fit = _fit_exponential(t, m_k, m_star)

        modes.append({
            "k": k,
            "m_star": m_star,
            "sigma": fit["sigma"],
            "R2": fit["R2"],
            "converged": fit["converged"],
        })
        if fit["converged"]:
            n_converged += 1

    frac = n_converged / N_LOW

    return {
        "modes": modes,
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
# Figure A: Low-Mode Evolution (representative run)
# ---------------------------------------------------------------------------
def figure_mode_evolution(runs: list[dict], analyses: list[dict]):
    """Plot m_0..m_5(t) on semilog-y for the run with largest Nm.

    Recomputes |a_k(t)| on-the-fly from the stored modal array.
    """
    best_idx = max(range(len(runs)), key=lambda i: runs[i]["Nm"])
    run = runs[best_idx]
    ana = analyses[best_idx]

    t = run["t"]
    modal = run["modal"]

    fig, ax = plt.subplots(figsize=(10, 6))

    for k in range(N_LOW):
        m_k = np.abs(modal[:, k])
        m_star = ana["modes"][k]["m_star"]

        ax.semilogy(
            t, np.maximum(m_k, 1e-30),
            color=MODE_COLORS[k], linewidth=1.5,
            label=MODE_LABELS[k],
        )

        # Attractor line
        if m_star > 1e-30:
            ax.axhline(
                m_star, color=MODE_COLORS[k], linestyle="--",
                linewidth=0.8, alpha=0.5,
            )

    # Annotate attractor region
    ax.annotate(
        "Low-mode attractor",
        xy=(0.75, 0.08),
        xycoords="axes fraction",
        fontsize=10, fontstyle="italic", color="0.35",
        ha="center",
        bbox=dict(boxstyle="round,pad=0.3", facecolor="#ffffcc",
                  alpha=0.8, edgecolor="#999999"),
    )

    setup_axes(
        ax,
        xlabel=r"Time $t$",
        ylabel=r"Modal amplitude $|a_k(t)|$",
        title=(f"Low-Mode Collapse — D={run['D']}, A={run['A']}, "
               f"Nm={run['Nm']}"),
    )
    ax.legend(fontsize=9, loc="upper right", framealpha=0.9, ncol=2)
    fig.tight_layout()

    fname = "mode_evolution.png"
    fig.savefig(os.path.join(FIG_DIR, fname), dpi=300)
    plt.close(fig)
    print(f"  Saved: {fname}")


# ---------------------------------------------------------------------------
# Figure B: Attractor Low-Mode Profile (all runs overlaid)
# ---------------------------------------------------------------------------
def figure_attractor_profile(runs: list[dict], analyses: list[dict]):
    """6-point polylines (m_0^*, ..., m_5^*) for all runs."""
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

    fig, ax = plt.subplots(figsize=(10, 6))

    k_axis = np.arange(N_LOW)

    # Collect all profiles for computing a mean profile
    all_profiles = []

    for run, ana in zip(runs, analyses):
        profile = np.array([ana["modes"][k]["m_star"] for k in range(N_LOW)])
        all_profiles.append(profile)

        color = D_cmap(D_norm(run["D"]))
        marker = Nm_markers.get(run["Nm"], "o")

        ax.semilogy(
            k_axis, np.maximum(profile, 1e-30),
            color=color, marker=marker, markersize=5,
            linewidth=0.8, alpha=0.4,
        )

    # Mean profile (thick black)
    if all_profiles:
        mean_profile = np.mean(all_profiles, axis=0)
        ax.semilogy(
            k_axis, np.maximum(mean_profile, 1e-30),
            color="black", marker="o", markersize=7,
            linewidth=2.5, alpha=0.9, zorder=10,
            label="Mean profile",
        )

    # Colorbar for D
    sm = plt.cm.ScalarMappable(cmap=D_cmap, norm=D_norm)
    sm.set_array([])
    cbar = fig.colorbar(sm, ax=ax, label=r"Diffusion $D$", pad=0.02)
    cbar.ax.tick_params(labelsize=9)

    # Marker legend for Nm
    legend_handles = [
        plt.Line2D([0], [0], marker=m, color="0.5", markersize=7,
                   linestyle="None", label=rf"$N_m = {Nm}$")
        for Nm, m in Nm_markers.items()
    ]
    # Add mean line
    legend_handles.append(
        plt.Line2D([0], [0], color="black", marker="o", markersize=7,
                   linewidth=2.5, label="Mean profile")
    )
    ax.legend(
        handles=legend_handles, fontsize=8, loc="upper right",
        framealpha=0.9, title="Legend",
    )

    ax.set_xticks(k_axis)
    ax.set_xticklabels([rf"$k = {k}$" for k in range(N_LOW)], fontsize=10)

    setup_axes(
        ax,
        xlabel="Mode index $k$",
        ylabel=r"Attractor amplitude $m_k^*$",
        title="Low-Mode Attractor Profile — All Admissible Runs",
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
    """One panel per Nm; cell = fraction of 6 modes converged."""
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

        # Annotations
        for di_idx in range(len(D_vals)):
            for ai_idx in range(len(A_vals)):
                val = grid[di_idx, ai_idx]
                if np.isnan(val):
                    ax.text(ai_idx, di_idx, "—", ha="center", va="center",
                            fontsize=8, color="0.5")
                else:
                    n_conv = int(round(val * N_LOW))
                    txt_color = "white" if val < 0.4 else "black"
                    ax.text(ai_idx, di_idx, f"{n_conv}/{N_LOW}",
                            ha="center", va="center", fontsize=8,
                            color=txt_color, fontweight="bold")

    fig.colorbar(
        plt.cm.ScalarMappable(cmap=plt.cm.RdYlGn,
                              norm=mcolors.Normalize(0, 1)),
        ax=axes.tolist(), label="Fraction of modes converged",
        shrink=0.8, pad=0.04,
    )

    fig.suptitle(
        "Low-Mode Collapse Convergence — Heatmap by $(D, A, N_m)$",
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
    # --- Per-run table ---
    print(f"\n{'='*140}")
    print("  Invariant Low-Mode Collapse — Summary Table")
    print(f"{'='*140}")

    # Header
    mode_hdr = "  ".join(f"m{k}*" for k in range(N_LOW))
    print(f"  {'D':<7} {'A':<7} {'Nm':<5} "
          f"{'Conv':<8} {'Frac':<7} ", end="")
    for k in range(N_LOW):
        print(f"{'m'+str(k)+'*':<12}", end="")
    print()
    print("  " + "-" * 130)

    # Collect per-mode values for global statistics
    all_m = {k: [] for k in range(N_LOW)}

    for run, ana in zip(runs, analyses):
        # Convergence string
        conv_str = ""
        for k in range(N_LOW):
            conv_str += "+" if ana["modes"][k]["converged"] else "."

        print(f"  {run['D']:<7.3f} {run['A']:<7.4f} {run['Nm']:<5d} "
              f"{conv_str:<8} {ana['frac_converged']:<7.1%} ", end="")
        for k in range(N_LOW):
            m_s = ana["modes"][k]["m_star"]
            print(f"{m_s:<12.4e}", end="")
            if not np.isnan(m_s):
                all_m[k].append(m_s)
        print()

    # --- Global statistics per mode ---
    print(f"\n  {'Mode':<8} {'Mean':<14} {'Std':<14} "
          f"{'Min':<14} {'Max':<14} {'CV':<10} {'Verdict'}")
    print("  " + "-" * 80)

    for k in range(N_LOW):
        arr = np.array(all_m[k])
        if len(arr) == 0:
            print(f"  k={k:<5} (no data)")
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

        print(f"  k={k:<5} "
              f"{mean_v:<14.6e} {std_v:<14.6e} "
              f"{np.min(arr):<14.6e} {np.max(arr):<14.6e} "
              f"{cv:<10.4f} {verdict}")

    # Overall convergence
    total = len(runs) * N_LOW
    total_conv = sum(ana["n_converged"] for ana in analyses)
    print(f"\n  Overall convergence: {total_conv}/{total} "
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
    print(f"\nComputing low-mode attractor values (k = 0..{N_LOW-1})...")
    analyses = []
    for i, run in enumerate(runs):
        ana = analyse_run(run)
        analyses.append(ana)
        if (i + 1) % 10 == 0 or i == len(runs) - 1:
            n_c = ana["n_converged"]
            print(f"  [{i+1}/{len(runs)}] {run['name']}: "
                  f"{n_c}/{N_LOW} converged")

    # --- Figures ---
    print("\n--- (A) Low-Mode Evolution ---")
    figure_mode_evolution(runs, analyses)

    print("\n--- (B) Attractor Low-Mode Profile ---")
    figure_attractor_profile(runs, analyses)

    print("\n--- (C) Convergence Heatmap ---")
    figure_convergence_heatmap(runs, analyses)

    # --- Summary ---
    print_summary(runs, analyses)

    print(f"\nAll figures saved to: {FIG_DIR}")
    print("Done.")


if __name__ == "__main__":
    main()
