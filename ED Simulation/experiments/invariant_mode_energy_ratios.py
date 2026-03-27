"""
invariant_mode_energy_ratios.py
================================
Experiment / Analysis: Invariant Mode-Energy Ratio Structure

Scans all completed regime_D*_A*_Nm* runs, computes the mode-energy
ratios

    R_k(t) = E_k(t) / E_total(t)  =  |a_k(t)|² / Σ_j |a_j(t)|²

for k = 1..K (K = min(20, n_modes−1)), and analyses their convergence
toward late-time attractor values R_k^*.

The attractor ratio profile (R_1^*, ..., R_K^*) is the normalised
spectral fingerprint of the ED equilibrium — a structural invariant
whose shape is determined by the modal hierarchy (Proposition C.29)
and whose uniqueness follows from the Lyapunov stability (Theorem C.43).

Produces:
  (A) Mode-Energy Ratio Evolution — R_k(t) for a representative run.
  (B) Attractor Ratio Profile — polylines for all runs overlaid.
  (C) Convergence Heatmap — fraction converged across (D, A, Nm).

All figures saved to output/figures/invariants/mode_energy_ratios/
as PNG (300 dpi).

Usage:
    python experiments/invariant_mode_energy_ratios.py

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
                        "mode_energy_ratios")

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
K_MAX = 20               # Maximum number of modes to analyse
LATE_FRAC = 0.10         # Fraction for late-time average
FIT_FRAC = 0.20          # Fraction for convergence fit
R2_THRESH = 0.95         # R² threshold for convergence
E_FLOOR = 1e-30          # Floor to avoid division by zero


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
# Per-run analysis (streaming over modes)
# ---------------------------------------------------------------------------
def analyse_run(run: dict) -> dict:
    """Compute mode-energy ratios and attractor summaries.

    Streams one mode at a time: computes E_k / E_total, extracts
    R_k^*, fits convergence, discards the ratio array.
    """
    modal = run["modal"]       # (n_steps, n_modes)
    t = run["t"]
    n_steps, n_modes = modal.shape

    K = min(K_MAX, n_modes - 1)  # modes 1..K

    # Pre-compute total energy per step (modes >= 1)
    E_total = np.sum(modal[:, 1:] ** 2, axis=1)     # (n_steps,)
    E_total = np.maximum(E_total, E_FLOOR)

    modes = []
    n_converged = 0

    for k in range(1, K + 1):
        # Energy ratio for mode k (temporary 1-D array)
        R_k = modal[:, k] ** 2 / E_total

        # Late-time average
        start = max(0, int((1.0 - LATE_FRAC) * len(R_k)))
        R_star = float(np.mean(R_k[start:]))

        # Convergence fit
        fit = _fit_exponential(t, R_k, R_star)

        modes.append({
            "k": k,
            "R_star": R_star,
            "sigma": fit["sigma"],
            "R2": fit["R2"],
            "converged": fit["converged"],
        })
        if fit["converged"]:
            n_converged += 1

        del R_k  # discard

    del E_total

    frac = n_converged / max(K, 1)

    return {
        "modes": modes,
        "K": K,
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
# Figure A: Mode-Energy Ratio Evolution (representative run)
# ---------------------------------------------------------------------------
def figure_ratio_evolution(runs: list[dict], analyses: list[dict]):
    """Plot R_k(t) for k = 1..K on semilog-y for the run with largest Nm.

    Recomputes ratios on-the-fly.
    """
    best_idx = max(range(len(runs)), key=lambda i: runs[i]["Nm"])
    run = runs[best_idx]
    ana = analyses[best_idx]

    t = run["t"]
    modal = run["modal"]
    n_steps, n_modes = modal.shape
    K = ana["K"]

    E_total = np.maximum(np.sum(modal[:, 1:] ** 2, axis=1), E_FLOOR)

    # Use viridis for K modes
    cmap = plt.cm.viridis
    norm = plt.Normalize(1, K)

    fig, ax = plt.subplots(figsize=(12, 6))

    for idx, mode_info in enumerate(ana["modes"]):
        k = mode_info["k"]
        R_star = mode_info["R_star"]

        R_k = modal[:, k] ** 2 / E_total
        color = cmap(norm(k))

        ax.semilogy(
            t, np.maximum(R_k, 1e-30),
            color=color, linewidth=0.9, alpha=0.8,
        )

        # Attractor line (only for first few to avoid clutter)
        if k <= 6 and R_star > 1e-20:
            ax.axhline(
                R_star, color=color, linestyle="--",
                linewidth=0.6, alpha=0.4,
            )

        del R_k

    del E_total

    # Colorbar
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])
    cbar = fig.colorbar(sm, ax=ax, label="Mode index $k$", pad=0.02)
    cbar.ax.tick_params(labelsize=9)

    setup_axes(
        ax,
        xlabel=r"Time $t$",
        ylabel=r"Energy ratio $R_k(t) = E_k / E_{\mathrm{total}}$",
        title=(f"Mode-Energy Ratios — D={run['D']}, A={run['A']}, "
               f"Nm={run['Nm']} (K={K})"),
    )
    fig.tight_layout()

    fname = "ratio_evolution.png"
    fig.savefig(os.path.join(FIG_DIR, fname), dpi=300)
    plt.close(fig)
    print(f"  Saved: {fname}")


# ---------------------------------------------------------------------------
# Figure B: Attractor Ratio Profile (all runs overlaid)
# ---------------------------------------------------------------------------
def figure_attractor_profile(runs: list[dict], analyses: list[dict]):
    """Polylines (R_1^*, ..., R_K^*) for all runs on semilog-y."""
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

    fig, ax = plt.subplots(figsize=(12, 6))

    # Collect profiles (variable length — use max K)
    max_K = max(ana["K"] for ana in analyses)
    all_profiles = []

    for run, ana in zip(runs, analyses):
        K = ana["K"]
        k_axis = np.arange(1, K + 1)
        profile = np.array([m["R_star"] for m in ana["modes"]])

        color = D_cmap(D_norm(run["D"]))
        marker = Nm_markers.get(run["Nm"], "o")

        ax.semilogy(
            k_axis, np.maximum(profile, 1e-30),
            color=color, marker=marker, markersize=3,
            linewidth=0.6, alpha=0.35,
        )

        # Pad to max_K for mean computation
        padded = np.full(max_K, np.nan)
        padded[:K] = profile
        all_profiles.append(padded)

    # Mean profile (ignoring NaN from shorter runs)
    if all_profiles:
        stacked = np.array(all_profiles)
        with np.errstate(all="ignore"):
            mean_profile = np.nanmean(stacked, axis=0)
        k_full = np.arange(1, max_K + 1)
        valid = ~np.isnan(mean_profile) & (mean_profile > 1e-30)

        ax.semilogy(
            k_full[valid], mean_profile[valid],
            color="black", marker="o", markersize=5,
            linewidth=2.5, alpha=0.9, zorder=10,
            label="Mean profile",
        )

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
        plt.Line2D([0], [0], color="black", marker="o", markersize=5,
                   linewidth=2.5, label="Mean profile")
    )
    ax.legend(
        handles=legend_handles, fontsize=8, loc="upper right",
        framealpha=0.9, title="Legend",
    )

    setup_axes(
        ax,
        xlabel="Mode index $k$",
        ylabel=r"Attractor ratio $R_k^*$",
        title="Mode-Energy Ratio Attractor Profile — All Admissible Runs",
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
    """One panel per Nm; cell = fraction of K ratios converged."""
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
                    # Find the K for this (D, A, Nm) cell
                    K_cell = K_MAX
                    for run2, ana2 in zip(runs, analyses):
                        if (run2["Nm"] == Nm and
                                run2["D"] == D_vals[di_idx] and
                                run2["A"] == A_vals[ai_idx]):
                            K_cell = ana2["K"]
                            break
                    n_conv = int(round(val * K_cell))
                    txt_color = "white" if val < 0.4 else "black"
                    ax.text(ai_idx, di_idx, f"{n_conv}/{K_cell}",
                            ha="center", va="center", fontsize=7,
                            color=txt_color, fontweight="bold")

    fig.colorbar(
        plt.cm.ScalarMappable(cmap=plt.cm.RdYlGn,
                              norm=mcolors.Normalize(0, 1)),
        ax=axes.tolist(), label="Fraction of ratios converged",
        shrink=0.8, pad=0.04,
    )

    fig.suptitle(
        "Mode-Energy Ratio Convergence — Heatmap by $(D, A, N_m)$",
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
    max_K = max(ana["K"] for ana in analyses)

    print(f"\n{'='*140}")
    print("  Invariant Mode-Energy Ratios — Summary Table")
    print(f"{'='*140}")

    # Compact header: show first 10 R_k^* columns
    n_show = min(10, max_K)
    hdr_modes = "  ".join(f"R{k}*" for k in range(1, n_show + 1))
    print(f"  {'D':<7} {'A':<7} {'Nm':<5} {'K':<4} "
          f"{'Conv':<8} {'Frac':<7} {hdr_modes}")
    print("  " + "-" * (55 + 10 * n_show))

    # Collect per-mode values
    all_R = {k: [] for k in range(1, max_K + 1)}

    for run, ana in zip(runs, analyses):
        K = ana["K"]

        # Convergence string (first 10 modes)
        conv_str = ""
        for m in ana["modes"][:10]:
            conv_str += "+" if m["converged"] else "."
        if K > 10:
            conv_str += f"..({ana['n_converged']}/{K})"

        print(f"  {run['D']:<7.3f} {run['A']:<7.4f} {run['Nm']:<5d} "
              f"{K:<4d} {conv_str:<8} {ana['frac_converged']:<7.1%} ",
              end="")

        for i, m in enumerate(ana["modes"][:n_show]):
            print(f"{m['R_star']:<10.3e}", end="")
            all_R[m["k"]].append(m["R_star"])

        # Also collect modes beyond n_show for statistics
        for m in ana["modes"][n_show:]:
            all_R[m["k"]].append(m["R_star"])

        print()

    # --- Global statistics per mode ---
    print(f"\n  {'Mode':<8} {'Mean':<14} {'Std':<14} "
          f"{'Min':<14} {'Max':<14} {'CV':<10} {'Verdict'}")
    print("  " + "-" * 80)

    for k in range(1, max_K + 1):
        arr = np.array(all_R[k])
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

        # Only print if there's meaningful data
        if mean_v > 1e-25:
            print(f"  k={k:<5} "
                  f"{mean_v:<14.6e} {std_v:<14.6e} "
                  f"{np.min(arr):<14.6e} {np.max(arr):<14.6e} "
                  f"{cv:<10.4f} {verdict}")

    # Overall convergence
    total = sum(ana["K"] for ana in analyses)
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

    # --- Analyse all runs (streaming) ---
    print(f"\nComputing mode-energy ratios (K ≤ {K_MAX})...")
    analyses = []
    for i, run in enumerate(runs):
        ana = analyse_run(run)
        analyses.append(ana)
        if (i + 1) % 10 == 0 or i == len(runs) - 1:
            n_c = ana["n_converged"]
            K = ana["K"]
            print(f"  [{i+1}/{len(runs)}] {run['name']}: "
                  f"K={K}, {n_c}/{K} converged")

    # --- Figures ---
    print("\n--- (A) Mode-Energy Ratio Evolution ---")
    figure_ratio_evolution(runs, analyses)

    print("\n--- (B) Attractor Ratio Profile ---")
    figure_attractor_profile(runs, analyses)

    print("\n--- (C) Convergence Heatmap ---")
    figure_convergence_heatmap(runs, analyses)

    # --- Summary ---
    print_summary(runs, analyses)

    print(f"\nAll figures saved to: {FIG_DIR}")
    print("Done.")


if __name__ == "__main__":
    main()
