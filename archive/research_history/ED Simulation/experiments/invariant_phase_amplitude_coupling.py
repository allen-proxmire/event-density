"""
invariant_phase_amplitude_coupling.py
======================================
Experiment / Analysis: Invariant Phase-Amplitude Coupling (PAC)

Scans all completed regime_D*_A*_Nm* runs, extracts complex modal
amplitudes a_k(t), and analyses the coupling between amplitude and
phase degrees of freedom:

  - Self PAC: ρ_k = corr(A_k, φ_k)
  - Cross PAC: PAC_ij = corr(A_i, φ_j)
  - Triad PAC closure: PAC_ijk = corr(A_k, Δφ_ijk)

Phase-amplitude coupling reveals whether the nonlinear term
M'(ρ)|∇ρ|² (Principle 7) creates systematic relationships between
a mode's amplitude and the phase structure of the spectral field.
In the ED architecture, the triad selection rule (Theorem C.34)
predicts specific PAC patterns among triad-connected modes.

Note: for real-valued Neumann eigenbasis data, phases are 0 or π,
so PAC becomes the correlation between amplitude and sign -- still
meaningful as a measure of amplitude-polarity coupling.

Produces:
  (A) Self PAC Profile -- ρ_k vs k for a representative run.
  (B) Cross-Mode PAC Matrix -- |PAC_ij| heatmap.
  (C) Triad PAC Closure -- scatter for all runs.

All figures saved to output/figures/invariants/phase_amplitude_coupling/
as PNG (300 dpi).

Usage:
    python experiments/invariant_phase_amplitude_coupling.py

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
                        "phase_amplitude_coupling")

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
K_MAX = 20
ATTRACTOR_FRAC = 0.20
AMP_FLOOR = 1e-20
MIN_STD = 1e-30          # Floor for std in correlation to avoid NaN


# ---------------------------------------------------------------------------
# Discovery
# ---------------------------------------------------------------------------
def discover_regime_runs() -> list[dict]:
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
# Correlation utility
# ---------------------------------------------------------------------------
def safe_corr(x: np.ndarray, y: np.ndarray) -> float:
    """Pearson correlation, returning 0 if either series is constant."""
    n = len(x)
    if n < 5:
        return 0.0
    sx = np.std(x)
    sy = np.std(y)
    if sx < MIN_STD or sy < MIN_STD:
        return 0.0
    return float(np.corrcoef(x, y)[0, 1])


# ---------------------------------------------------------------------------
# Phase extraction
# ---------------------------------------------------------------------------
def extract_amp_phase(modal_window: np.ndarray, K: int) -> tuple:
    """Extract amplitude and unwrapped phase from attractor-window modal data.

    Returns (A, phi, is_complex) where A and phi have shape (n_window, K).
    """
    a = modal_window[:, 1:K+1]

    is_complex = np.iscomplexobj(a)

    A = np.abs(a)

    if is_complex:
        phi_raw = np.angle(a)
    else:
        phi_raw = np.where(a >= 0, 0.0, np.pi)

    phi = np.unwrap(phi_raw, axis=0)

    return A, phi, is_complex


# ---------------------------------------------------------------------------
# Triad enumeration
# ---------------------------------------------------------------------------
def enumerate_triads(K: int) -> list[tuple]:
    triads = []
    for i in range(1, K + 1):
        for j in range(i, K + 1):
            k = i + j
            if k <= K:
                triads.append((i, j, k))
    return triads


# ---------------------------------------------------------------------------
# Per-run analysis
# ---------------------------------------------------------------------------
def analyse_run(run: dict) -> dict:
    """Compute self-PAC, cross-PAC matrix, and triad PAC closure."""
    modal = run["modal"]
    t = run["t"]
    n = len(t)
    n_modes = modal.shape[1]
    K = min(K_MAX, n_modes - 1)

    # Attractor window
    start = max(0, int((1.0 - ATTRACTOR_FRAC) * n))
    modal_win = modal[start:]

    A, phi, is_complex = extract_amp_phase(modal_win, K)

    # --- (A) Self PAC: ρ_k = corr(A_k, φ_k) ---
    rho_self = []
    for k_idx in range(K):
        if np.mean(A[:, k_idx]) < AMP_FLOOR:
            rho_self.append(0.0)
        else:
            rho_self.append(safe_corr(A[:, k_idx], phi[:, k_idx]))

    mean_abs_rho = float(np.mean(np.abs(rho_self)))
    max_abs_rho = float(np.max(np.abs(rho_self)))

    # --- (B) Cross-Mode PAC: PAC_ij = corr(A_i, φ_j) ---
    pac_matrix = np.zeros((K, K))
    for i in range(K):
        if np.mean(A[:, i]) < AMP_FLOOR:
            continue
        for j in range(K):
            if np.mean(A[:, j]) < AMP_FLOOR:
                continue
            pac_matrix[i, j] = safe_corr(A[:, i], phi[:, j])

    mask_off = ~np.eye(K, dtype=bool)
    off_diag = np.abs(pac_matrix[mask_off])
    mean_cross_pac = float(np.mean(off_diag)) if len(off_diag) > 0 else 0.0

    # --- (C) Triad PAC Closure: PAC_ijk = corr(A_k, Δφ_ijk) ---
    triads = enumerate_triads(K)
    triad_pacs = []

    for (i, j, k) in triads:
        # 1-based → 0-based index
        A_k_arr = A[:, k - 1]
        if np.mean(A_k_arr) < AMP_FLOOR:
            triad_pacs.append({"triad": (i, j, k), "pac": 0.0})
            continue

        delta_phi = phi[:, i - 1] + phi[:, j - 1] - phi[:, k - 1]
        pac_val = safe_corr(A_k_arr, delta_phi)

        triad_pacs.append({"triad": (i, j, k), "pac": pac_val})

    mean_triad_pac = (float(np.mean([abs(tp["pac"]) for tp in triad_pacs]))
                      if triad_pacs else 0.0)

    del A, phi  # free

    return {
        "K": K,
        "is_complex": is_complex,
        "rho_self": rho_self,
        "mean_abs_rho": mean_abs_rho,
        "max_abs_rho": max_abs_rho,
        "pac_matrix": pac_matrix,
        "mean_cross_pac": mean_cross_pac,
        "triad_pacs": triad_pacs,
        "mean_triad_pac": mean_triad_pac,
        "n_triads": len(triad_pacs),
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
# Figure A: Self PAC Profile
# ---------------------------------------------------------------------------
def figure_self_pac(runs: list[dict], analyses: list[dict]):
    """Bar chart of ρ_k for representative run, with all-run mean ± σ."""
    best_idx = max(range(len(runs)), key=lambda i: runs[i]["Nm"])
    run = runs[best_idx]
    ana = analyses[best_idx]

    K = ana["K"]
    k_axis = np.arange(1, K + 1)
    rho = np.array(ana["rho_self"])

    fig, ax = plt.subplots(figsize=(10, 6))

    # Representative run
    colors = ["#b2182b" if r < 0 else "#2166ac" for r in rho]
    ax.bar(k_axis, rho, color=colors, alpha=0.7, width=0.6,
           label=f"D={run['D']}, Nm={run['Nm']}")

    # All-run statistics
    max_K = max(a["K"] for a in analyses)
    all_rho = []
    for ana2 in analyses:
        padded = np.full(max_K, np.nan)
        padded[:ana2["K"]] = ana2["rho_self"]
        all_rho.append(padded)

    stacked = np.array(all_rho)
    with np.errstate(all="ignore"):
        mean_rho = np.nanmean(stacked, axis=0)
        std_rho = np.nanstd(stacked, axis=0)

    k_full = np.arange(1, max_K + 1)
    valid = ~np.isnan(mean_rho)

    ax.errorbar(
        k_full[valid], mean_rho[valid],
        yerr=std_rho[valid],
        color="black", marker="o", markersize=4,
        linewidth=1.5, capsize=3, capthick=1,
        label=r"All-run mean $\pm 1\sigma$",
        zorder=10,
    )

    ax.axhline(0, color="0.5", linestyle=":", linewidth=0.7)
    ax.set_ylim(-1.05, 1.05)

    phase_type = "complex" if ana["is_complex"] else "real (0/π)"
    ax.annotate(
        f"Phase type: {phase_type}\n"
        rf"mean $|\rho_k|$ = {ana['mean_abs_rho']:.4f}",
        xy=(0.98, 0.95), xycoords="axes fraction",
        fontsize=9, ha="right", va="top",
        bbox=dict(boxstyle="round,pad=0.3", facecolor="wheat", alpha=0.7),
    )

    setup_axes(
        ax,
        xlabel="Mode index $k$",
        ylabel=r"Self PAC $\rho_k = \mathrm{corr}(A_k, \varphi_k)$",
        title=f"Phase-Amplitude Coupling -- D={run['D']}, A={run['A']}, Nm={run['Nm']}",
    )
    ax.legend(fontsize=9, loc="upper left", framealpha=0.9)
    fig.tight_layout()

    fname = "self_pac_profile.png"
    fig.savefig(os.path.join(FIG_DIR, fname), dpi=300)
    plt.close(fig)
    print(f"  Saved: {fname}")


# ---------------------------------------------------------------------------
# Figure B: Cross-Mode PAC Matrix
# ---------------------------------------------------------------------------
def figure_cross_pac_matrix(runs: list[dict], analyses: list[dict]):
    """Heatmap of |PAC_ij| for the largest-Nm run."""
    best_idx = max(range(len(runs)), key=lambda i: runs[i]["Nm"])
    run = runs[best_idx]
    ana = analyses[best_idx]

    PAC = np.abs(ana["pac_matrix"])
    K = ana["K"]

    fig, ax = plt.subplots(figsize=(9, 8))

    im = ax.imshow(
        PAC, cmap="YlOrRd", vmin=0, vmax=1,
        interpolation="nearest", origin="lower",
    )

    ticks = np.arange(K)
    tick_labels = [str(k + 1) for k in range(K)]
    ax.set_xticks(ticks)
    ax.set_xticklabels(tick_labels, fontsize=7, rotation=45)
    ax.set_yticks(ticks)
    ax.set_yticklabels(tick_labels, fontsize=7)

    # Annotate strong couplings
    for i in range(K):
        for j in range(K):
            val = PAC[i, j]
            if val > 0.3:
                txt_color = "white" if val > 0.6 else "black"
                ax.text(j, i, f"{val:.2f}", ha="center", va="center",
                        fontsize=5, color=txt_color, fontweight="bold")

    cbar = fig.colorbar(im, ax=ax, label=r"$|\mathrm{PAC}_{ij}|$",
                        pad=0.02, shrink=0.85)
    cbar.ax.tick_params(labelsize=9)

    ax.annotate(
        f"mean off-diag |PAC| = {ana['mean_cross_pac']:.4f}",
        xy=(0.02, 0.98), xycoords="axes fraction",
        fontsize=9, va="top",
        bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8),
    )

    setup_axes(
        ax,
        xlabel=r"Mode $j$ (phase donor)",
        ylabel=r"Mode $i$ (amplitude)",
        title=(f"Cross-Mode PAC -- D={run['D']}, A={run['A']}, "
               f"Nm={run['Nm']}"),
    )
    fig.tight_layout()

    fname = "cross_pac_matrix.png"
    fig.savefig(os.path.join(FIG_DIR, fname), dpi=300)
    plt.close(fig)
    print(f"  Saved: {fname}")


# ---------------------------------------------------------------------------
# Figure C: Triad PAC Closure
# ---------------------------------------------------------------------------
def figure_triad_pac_closure(runs: list[dict], analyses: list[dict]):
    """Scatter |PAC_ijk| vs triad index for all runs."""
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

    all_pac = []

    for run, ana in zip(runs, analyses):
        tps = ana["triad_pacs"]
        if not tps:
            continue

        indices = np.arange(len(tps))
        values = np.array([abs(tp["pac"]) for tp in tps])
        all_pac.extend(values.tolist())

        color = D_cmap(D_norm(run["D"]))
        marker = Nm_markers.get(run["Nm"], "o")

        ax.scatter(
            indices, values,
            color=color, marker=marker, s=12, alpha=0.3,
            edgecolors="none",
        )

    # Global mean
    if all_pac:
        mean_pac = np.mean(all_pac)
        ax.axhline(mean_pac, color="black", linestyle="--",
                   linewidth=1.5, alpha=0.7,
                   label=rf"Global mean $|\mathrm{{PAC}}| = {mean_pac:.4f}$")

    # Colorbar
    sm = plt.cm.ScalarMappable(cmap=D_cmap, norm=D_norm)
    sm.set_array([])
    cbar = fig.colorbar(sm, ax=ax, label=r"Diffusion $D$", pad=0.02)
    cbar.ax.tick_params(labelsize=9)

    # Legend
    legend_handles = [
        plt.Line2D([0], [0], marker=m, color="0.5", markersize=7,
                   linestyle="None", label=rf"$N_m = {Nm}$")
        for Nm, m in Nm_markers.items()
    ]
    legend_handles.extend(ax.get_legend_handles_labels()[0])
    ax.legend(handles=legend_handles, fontsize=8, loc="upper right",
              framealpha=0.9)

    setup_axes(
        ax,
        xlabel="Triad index",
        ylabel=r"$|\mathrm{PAC}_{ijk}| = |\mathrm{corr}(A_k, \Delta\varphi_{ijk})|$",
        title="Triad PAC Closure -- All Admissible Runs",
    )
    ax.set_ylim(-0.05, 1.05)
    fig.tight_layout()

    fname = "triad_pac_closure.png"
    fig.savefig(os.path.join(FIG_DIR, fname), dpi=300)
    plt.close(fig)
    print(f"  Saved: {fname}")


# ---------------------------------------------------------------------------
# Summary table and invariance verdict
# ---------------------------------------------------------------------------
def print_summary(runs: list[dict], analyses: list[dict]):
    print(f"\n{'='*110}")
    print("  Invariant Phase-Amplitude Coupling -- Summary Table")
    print(f"{'='*110}")

    print(f"  {'D':<7} {'A':<7} {'Nm':<5} {'K':<4} {'Phase':<7} "
          f"{'mean|ρ|':<10} {'max|ρ|':<10} "
          f"{'cross_PAC':<10} {'triad_PAC':<10} {'#triads':<8}")
    print("  " + "-" * 90)

    inv_names = ["mean_abs_rho", "max_abs_rho", "mean_cross_pac",
                 "mean_triad_pac"]
    all_inv = {name: [] for name in inv_names}

    for run, ana in zip(runs, analyses):
        phase_type = "cplx" if ana["is_complex"] else "real"

        print(f"  {run['D']:<7.3f} {run['A']:<7.4f} {run['Nm']:<5d} "
              f"{ana['K']:<4d} {phase_type:<7} "
              f"{ana['mean_abs_rho']:<10.4f} "
              f"{ana['max_abs_rho']:<10.4f} "
              f"{ana['mean_cross_pac']:<10.4f} "
              f"{ana['mean_triad_pac']:<10.4f} "
              f"{ana['n_triads']:<8d}")

        for name in inv_names:
            val = ana[name]
            if not np.isnan(val):
                all_inv[name].append(val)

    # Global statistics
    print(f"\n  {'Invariant':<16} {'Mean':<12} {'Std':<12} "
          f"{'Min':<12} {'Max':<12} {'CV':<10} {'Verdict'}")
    print("  " + "-" * 80)

    for name in inv_names:
        arr = np.array(all_inv[name])
        if len(arr) == 0:
            print(f"  {name:<16} (no data)")
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

        print(f"  {name:<16} "
              f"{mean_v:<12.6f} {std_v:<12.6f} "
              f"{np.min(arr):<12.6f} {np.max(arr):<12.6f} "
              f"{cv:<10.4f} {verdict}")


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

    # Analyse
    print(f"\nAnalysing phase-amplitude coupling (K <= {K_MAX})...")
    analyses = []
    for i, run in enumerate(runs):
        ana = analyse_run(run)
        analyses.append(ana)
        if (i + 1) % 10 == 0 or i == len(runs) - 1:
            pt = "cplx" if ana["is_complex"] else "real"
            print(f"  [{i+1}/{len(runs)}] {run['name']}: "
                  f"K={ana['K']} ({pt}), "
                  f"|ρ|={ana['mean_abs_rho']:.4f}, "
                  f"triad={ana['mean_triad_pac']:.4f}")

    # Figures
    print("\n--- (A) Self PAC Profile ---")
    figure_self_pac(runs, analyses)

    print("\n--- (B) Cross-Mode PAC Matrix ---")
    figure_cross_pac_matrix(runs, analyses)

    print("\n--- (C) Triad PAC Closure ---")
    figure_triad_pac_closure(runs, analyses)

    # Summary
    print_summary(runs, analyses)

    print(f"\nAll figures saved to: {FIG_DIR}")
    print("Done.")


if __name__ == "__main__":
    main()
