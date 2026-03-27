"""
invariant_spectral_entropy.py
==============================
Experiment / Analysis: Invariant Spectral Entropy Structure

Scans all completed regime_D*_A*_Nm* runs, computes the spectral entropy

    H(t) = − Σ_k  p_k(t) log p_k(t)

where p_k(t) = |a_k(t)|² / Σ_j |a_j(t)|² is the normalised modal energy
distribution, and analyses its convergence toward a late-time attractor
value H^*.

The spectral entropy measures how evenly the energy is distributed across
modes.  H = 0 when all energy is in a single mode; H = log(N) when energy
is uniformly distributed.  Its attractor value H^* encodes the asymptotic
spectral shape — a structural invariant of the ED architecture
(Appendix C.4, Proposition C.29).

Produces:
  (A) Spectral Entropy Evolution — H(t) for a representative run.
  (B) Attractor Entropy Profile — H^* vs D for all runs.
  (C) Convergence Heatmap — converged/not across (D, A, Nm).

All figures saved to output/figures/invariants/spectral_entropy/
as PNG (300 dpi).

Usage:
    python experiments/invariant_spectral_entropy.py

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
                        "spectral_entropy")

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
LATE_FRAC = 0.10        # Fraction for late-time average
FIT_FRAC = 0.20         # Fraction for convergence fit
R2_THRESH = 0.95        # R² threshold for convergence
LOG_FLOOR = 1e-30       # Floor inside log to avoid log(0)


# ---------------------------------------------------------------------------
# Discovery (shared pattern)
# ---------------------------------------------------------------------------
def discover_regime_runs() -> list[dict]:
    """Scan RUNS_DIR for regime_D*_A*_Nm* folders with valid modal data."""
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
        if modal.shape[1] < 2:
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
# Spectral entropy computation (streaming)
# ---------------------------------------------------------------------------
def compute_spectral_entropy(modal: np.ndarray) -> np.ndarray:
    """Compute H(t) = −Σ_k p_k log(p_k) from modal amplitudes.

    Parameters
    ----------
    modal : ndarray, shape (n_steps, n_modes)

    Returns
    -------
    H : ndarray, shape (n_steps,)
        Spectral entropy at each time step.

    Uses only modes k >= 1 (excludes the homogeneous mode k = 0, which
    carries mass but not gradient structure).
    """
    # Modal energies E_k = |a_k|^2, k >= 1
    E = modal[:, 1:] ** 2                          # (n_steps, n_modes-1)

    # Total energy per time step
    E_total = np.sum(E, axis=1, keepdims=True)      # (n_steps, 1)
    E_total = np.maximum(E_total, LOG_FLOOR)

    # Normalised distribution
    p = E / E_total                                  # (n_steps, n_modes-1)

    # Entropy: H = −Σ_k p_k log(p_k + floor)
    log_p = np.log(p + LOG_FLOOR)
    H = -np.sum(p * log_p, axis=1)                  # (n_steps,)

    return H


def analyse_run(run: dict) -> dict:
    """Compute spectral entropy and attractor summary for one run.

    Returns dict with:
        H_star, sigma, R2, converged
    """
    modal = run["modal"]
    t = run["t"]

    # Compute entropy (1-D array, same length as t)
    H = compute_spectral_entropy(modal)

    # Late-time average
    start = max(0, int((1.0 - LATE_FRAC) * len(H)))
    H_star = float(np.mean(H[start:]))

    # Convergence fit
    fit = _fit_exponential(t[:len(H)], H, H_star)

    # Maximum possible entropy for reference
    n_active = modal.shape[1] - 1  # modes 1..N-1
    H_max = float(np.log(max(n_active, 1)))

    return {
        "H_star": H_star,
        "H_max": H_max,
        "H_ratio": H_star / max(H_max, 1e-30),
        "sigma": fit["sigma"],
        "R2": fit["R2"],
        "converged": fit["converged"],
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
# Figure A: Spectral Entropy Evolution (representative run)
# ---------------------------------------------------------------------------
def figure_entropy_evolution(runs: list[dict], analyses: list[dict]):
    """Plot H(t) for the run with largest Nm.

    Recomputes H(t) on-the-fly for the single representative run.
    """
    best_idx = max(range(len(runs)), key=lambda i: runs[i]["Nm"])
    run = runs[best_idx]
    ana = analyses[best_idx]

    t = run["t"]
    H = compute_spectral_entropy(run["modal"])
    H_star = ana["H_star"]
    H_max = ana["H_max"]

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.plot(
        t[:len(H)], H,
        color="#2166ac", linewidth=1.5,
        label=r"$H(t)$",
    )

    # Attractor line
    ax.axhline(
        H_star, color="#b2182b", linestyle="--", linewidth=1.0,
        label=rf"$H^* = {H_star:.4f}$",
    )

    # Maximum entropy reference
    ax.axhline(
        H_max, color="0.6", linestyle=":", linewidth=0.8,
        label=rf"$H_{{\max}} = \ln({run['modal'].shape[1]-1}) = {H_max:.4f}$",
    )

    # Convergence annotation
    if ana["converged"]:
        ax.annotate(
            rf"$\sigma = {ana['sigma']:.4f}$, $R^2 = {ana['R2']:.4f}$",
            xy=(0.60, 0.15),
            xycoords="axes fraction",
            fontsize=10, color="#333333",
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#e8f4e8",
                      alpha=0.8, edgecolor="#1b7837"),
        )
    else:
        ax.annotate(
            "Not converged",
            xy=(0.60, 0.15),
            xycoords="axes fraction",
            fontsize=10, color="#b2182b",
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#fde8e8",
                      alpha=0.8, edgecolor="#b2182b"),
        )

    setup_axes(
        ax,
        xlabel=r"Time $t$",
        ylabel=r"Spectral entropy $H(t)$",
        title=(f"Spectral Entropy — D={run['D']}, A={run['A']}, "
               f"Nm={run['Nm']}"),
    )
    ax.legend(fontsize=10, loc="center right", framealpha=0.9)
    ax.set_ylim(bottom=0)
    fig.tight_layout()

    fname = "entropy_evolution.png"
    fig.savefig(os.path.join(FIG_DIR, fname), dpi=300)
    plt.close(fig)
    print(f"  Saved: {fname}")

    del H


# ---------------------------------------------------------------------------
# Figure B: Attractor Entropy Profile (H^* vs D, all runs)
# ---------------------------------------------------------------------------
def figure_attractor_profile(runs: list[dict], analyses: list[dict]):
    """Scatter H^* vs D, colored by A, marker by Nm."""
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

    fig, ax = plt.subplots(figsize=(10, 6))

    # Global mean
    all_H = [ana["H_star"] for ana in analyses
             if not np.isnan(ana["H_star"])]
    global_mean = np.mean(all_H) if all_H else np.nan

    for run, ana in zip(runs, analyses):
        H_star = ana["H_star"]
        if np.isnan(H_star):
            continue

        color = A_cmap(A_norm(run["A"]))
        marker = Nm_markers.get(run["Nm"], "o")

        ax.scatter(
            run["D"], H_star,
            color=color, marker=marker, s=60, alpha=0.7,
            edgecolors="0.3", linewidths=0.4,
        )

    if not np.isnan(global_mean):
        ax.axhline(global_mean, color="0.4", linestyle="--",
                   linewidth=1.0, alpha=0.6)
        ax.annotate(
            rf"mean $H^* = {global_mean:.4f}$",
            xy=(0.98, global_mean),
            xycoords=("axes fraction", "data"),
            fontsize=9, color="0.3", ha="right", va="bottom",
        )

    # Colorbar for A
    sm = plt.cm.ScalarMappable(cmap=A_cmap, norm=A_norm)
    sm.set_array([])
    cbar = fig.colorbar(sm, ax=ax, label=r"Amplitude $A$", pad=0.02)
    cbar.ax.tick_params(labelsize=9)

    # Marker legend for Nm
    legend_handles = []
    for Nm, marker in Nm_markers.items():
        h = plt.Line2D(
            [0], [0], marker=marker, color="0.5", markersize=7,
            linestyle="None", label=rf"$N_m = {Nm}$",
        )
        legend_handles.append(h)
    ax.legend(
        handles=legend_handles, fontsize=9, loc="upper right",
        framealpha=0.9, title="Seed count",
    )

    setup_axes(
        ax,
        xlabel=r"Diffusion $D$",
        ylabel=r"Attractor entropy $H^*$",
        title="Spectral Entropy Attractor — All Admissible Runs",
    )
    ax.set_ylim(bottom=0)
    fig.tight_layout()

    fname = "attractor_profile.png"
    fig.savefig(os.path.join(FIG_DIR, fname), dpi=300)
    plt.close(fig)
    print(f"  Saved: {fname}")


# ---------------------------------------------------------------------------
# Figure C: Convergence Heatmap
# ---------------------------------------------------------------------------
def figure_convergence_heatmap(runs: list[dict], analyses: list[dict]):
    """One panel per Nm; cell color = converged (1) or not (0)."""
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
            grid[di, ai] = 1.0 if ana["converged"] else 0.0

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

        # Annotations
        for di_idx in range(len(D_vals)):
            for ai_idx in range(len(A_vals)):
                val = grid[di_idx, ai_idx]
                if np.isnan(val):
                    ax.text(ai_idx, di_idx, "—", ha="center", va="center",
                            fontsize=9, color="0.5")
                else:
                    label = "Y" if val > 0.5 else "N"
                    txt_color = "black" if val > 0.5 else "white"
                    ax.text(ai_idx, di_idx, label, ha="center",
                            va="center", fontsize=9, color=txt_color,
                            fontweight="bold")

    fig.colorbar(
        plt.cm.ScalarMappable(cmap=plt.cm.RdYlGn,
                              norm=mcolors.Normalize(0, 1)),
        ax=axes.tolist(), label="Converged",
        shrink=0.8, pad=0.04,
    )

    fig.suptitle(
        "Spectral Entropy Convergence — Heatmap by $(D, A, N_m)$",
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
    print(f"\n{'='*100}")
    print("  Invariant Spectral Entropy — Summary Table")
    print(f"{'='*100}")

    print(f"  {'D':<7} {'A':<7} {'Nm':<5} "
          f"{'H*':<12} {'H_max':<10} {'H*/H_max':<10} "
          f"{'sigma':<12} {'R2':<10} {'Conv':<6} {'Regime':<12}")
    print("  " + "-" * 95)

    all_H_star = []

    for run, ana in zip(runs, analyses):
        regime = run["metadata"].get("regime", "—")
        conv_str = "Y" if ana["converged"] else "N"

        print(f"  {run['D']:<7.3f} {run['A']:<7.4f} {run['Nm']:<5d} "
              f"{ana['H_star']:<12.6f} {ana['H_max']:<10.4f} "
              f"{ana['H_ratio']:<10.4f} "
              f"{ana['sigma']:<12.6e} {ana['R2']:<10.4f} "
              f"{conv_str:<6} {regime:<12}")

        if not np.isnan(ana["H_star"]):
            all_H_star.append(ana["H_star"])

    # --- Global statistics ---
    if all_H_star:
        arr = np.array(all_H_star)
        mean_v = np.mean(arr)
        std_v = np.std(arr)
        cv = std_v / max(abs(mean_v), 1e-30)

        if cv < 0.05:
            verdict = "INVARIANT"
        elif cv < 0.15:
            verdict = "WEAKLY INVARIANT"
        else:
            verdict = "NOT INVARIANT"

        print(f"\n  H^* statistics (across {len(arr)} runs):")
        print(f"    Mean:     {mean_v:.6f}")
        print(f"    Std:      {std_v:.6f}")
        print(f"    Min:      {np.min(arr):.6f}")
        print(f"    Max:      {np.max(arr):.6f}")
        print(f"    CV:       {cv:.4f}")
        print(f"    Verdict:  {verdict}")

    # Overall convergence
    total = len(runs)
    total_conv = sum(1 for ana in analyses if ana["converged"])
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
    print("\nComputing spectral entropies...")
    analyses = []
    for i, run in enumerate(runs):
        ana = analyse_run(run)
        analyses.append(ana)
        if (i + 1) % 10 == 0 or i == len(runs) - 1:
            c_str = "Y" if ana["converged"] else "N"
            print(f"  [{i+1}/{len(runs)}] {run['name']}: "
                  f"H*={ana['H_star']:.4f} "
                  f"(σ={ana['sigma']:.4e}, conv={c_str})")

    # --- Figures ---
    print("\n--- (A) Spectral Entropy Evolution ---")
    figure_entropy_evolution(runs, analyses)

    print("\n--- (B) Attractor Entropy Profile ---")
    figure_attractor_profile(runs, analyses)

    print("\n--- (C) Convergence Heatmap ---")
    figure_convergence_heatmap(runs, analyses)

    # --- Summary ---
    print_summary(runs, analyses)

    print(f"\nAll figures saved to: {FIG_DIR}")
    print("Done.")


if __name__ == "__main__":
    main()
