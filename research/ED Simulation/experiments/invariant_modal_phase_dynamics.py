"""
invariant_modal_phase_dynamics.py
==================================
Experiment / Analysis: Invariant Modal Phase Dynamics

Scans all completed regime_D*_A*_Nm* runs, extracts the complex modal
amplitudes a_k(t), and analyses the phase structure:

  - Phase drift rates dφ_k/dt
  - Pairwise phase coherence C_ij = |⟨exp(i(φ_i − φ_j))⟩|
  - Triad phase closure coherence for (i,j,k) with i+j=k

The phase dynamics complement the amplitude-based invariants: while
amplitudes encode the energy distribution, phases encode the coupling
geometry and synchronisation structure at equilibrium.  In the ED
architecture, the triad selection rule (Theorem C.34) predicts specific
phase-locking patterns among modes connected by the nonlinear term.

Note: if the solver stores only real modal amplitudes (Neumann cosine
eigenbasis), the phases are either 0 or π (positive or negative
coefficients).  The script handles both the fully complex case and the
real-valued case.

Produces:
  (A) Phase Drift Rates -- dφ_k/dt vs k for a representative run.
  (B) Phase Coherence Matrix -- heatmap of C_ij.
  (C) Triad Closure Coherence -- scatter for all runs.

All figures saved to output/figures/invariants/modal_phase_dynamics/
as PNG (300 dpi).

Usage:
    python experiments/invariant_modal_phase_dynamics.py

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
                        "modal_phase_dynamics")

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
K_MAX = 20
ATTRACTOR_FRAC = 0.20    # Last 20% for phase analysis
AMP_FLOOR = 1e-20        # Modes below this amplitude are phase-undefined


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
# Phase extraction
# ---------------------------------------------------------------------------
def extract_phases(modal_window: np.ndarray) -> tuple:
    """Extract unwrapped phases from modal amplitudes in the attractor window.

    Parameters
    ----------
    modal_window : ndarray, shape (n_window, n_modes)
        Modal amplitudes restricted to the attractor window.
        May be real-valued (Neumann basis) or complex.

    Returns
    -------
    phases : ndarray, shape (n_window, K), unwrapped phases for modes 1..K
    is_complex : bool, True if the data is genuinely complex
    K : int, number of modes analysed
    """
    n_window, n_modes = modal_window.shape
    K = min(K_MAX, n_modes - 1)

    a = modal_window[:, 1:K+1]  # modes 1..K

    is_complex = np.iscomplexobj(a)

    if is_complex:
        phases_raw = np.angle(a)
    else:
        # Real-valued: phase is 0 (positive) or π (negative)
        # Use sign to define a continuous "phase" via atan2(0, a_k)
        phases_raw = np.where(a >= 0, 0.0, np.pi)

    # Unwrap along time axis for each mode
    phases = np.unwrap(phases_raw, axis=0)

    return phases, is_complex, K


# ---------------------------------------------------------------------------
# Triad enumeration
# ---------------------------------------------------------------------------
def enumerate_triads(K: int) -> list[tuple]:
    """All (i, j, k) with 1 <= i < j, i+j = k <= K."""
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
    """Compute phase drift, coherence matrix, and triad closure."""
    modal = run["modal"]
    t = run["t"]
    n = len(t)
    n_modes = modal.shape[1]

    # Attractor window
    start = max(0, int((1.0 - ATTRACTOR_FRAC) * n))
    t_win = t[start:]
    modal_win = modal[start:]
    n_win = len(t_win)

    phases, is_complex, K = extract_phases(modal_win)

    # --- (A) Phase drift rates ---
    drift_rates = []
    for k_idx in range(K):
        phi = phases[:, k_idx]

        # Check if mode has sufficient amplitude
        amp = np.abs(modal_win[:, k_idx + 1])
        if np.mean(amp) < AMP_FLOOR:
            drift_rates.append(0.0)
            continue

        # Linear fit: phi = omega * t + phi0
        try:
            coeffs = np.polyfit(t_win, phi, 1)
            drift_rates.append(float(coeffs[0]))
        except (np.linalg.LinAlgError, ValueError):
            drift_rates.append(0.0)

    # --- (B) Pairwise phase coherence ---
    # C_ij = |mean(exp(i(phi_i - phi_j)))|
    # For real data: exp(i*0) = 1 or exp(i*pi) = -1
    coherence_matrix = np.zeros((K, K))

    for i in range(K):
        for j in range(K):
            if i == j:
                coherence_matrix[i, j] = 1.0
                continue
            delta_phi = phases[:, i] - phases[:, j]
            coherence_matrix[i, j] = float(
                np.abs(np.mean(np.exp(1j * delta_phi)))
            )

    # Off-diagonal statistics
    mask_off = ~np.eye(K, dtype=bool)
    off_diag = coherence_matrix[mask_off]
    mean_coherence = float(np.mean(off_diag)) if len(off_diag) > 0 else 0.0
    max_coherence = float(np.max(off_diag)) if len(off_diag) > 0 else 0.0
    min_coherence = float(np.min(off_diag)) if len(off_diag) > 0 else 0.0

    # --- (C) Triad phase closure ---
    triads = enumerate_triads(K)
    triad_closures = []

    for (i, j, k) in triads:
        # Closure: Δ = φ_i + φ_j − φ_k  (1-based → 0-based index: subtract 1)
        Delta = phases[:, i-1] + phases[:, j-1] - phases[:, k-1]
        coh = float(np.abs(np.mean(np.exp(1j * Delta))))
        triad_closures.append({
            "triad": (i, j, k),
            "coherence": coh,
        })

    mean_triad_coh = (float(np.mean([tc["coherence"] for tc in triad_closures]))
                      if triad_closures else 0.0)

    return {
        "K": K,
        "is_complex": is_complex,
        "drift_rates": drift_rates,
        "coherence_matrix": coherence_matrix,
        "mean_coherence": mean_coherence,
        "max_coherence": max_coherence,
        "min_coherence": min_coherence,
        "triad_closures": triad_closures,
        "mean_triad_coherence": mean_triad_coh,
        "n_triads": len(triad_closures),
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
# Figure A: Phase Drift Rates
# ---------------------------------------------------------------------------
def figure_drift_rates(runs: list[dict], analyses: list[dict]):
    """Plot dφ_k/dt vs k for representative run, with all-run mean ± σ."""
    best_idx = max(range(len(runs)), key=lambda i: runs[i]["Nm"])
    run = runs[best_idx]
    ana = analyses[best_idx]

    K = ana["K"]
    k_axis = np.arange(1, K + 1)
    drift = np.array(ana["drift_rates"])

    fig, ax = plt.subplots(figsize=(10, 6))

    # Representative run
    ax.bar(
        k_axis, drift,
        color="#2166ac", alpha=0.7, width=0.6,
        label=f"D={run['D']}, Nm={run['Nm']}",
    )

    # All-run statistics
    max_K = max(a["K"] for a in analyses)
    all_drifts = []
    for ana2 in analyses:
        padded = np.full(max_K, np.nan)
        padded[:ana2["K"]] = ana2["drift_rates"]
        all_drifts.append(padded)

    stacked = np.array(all_drifts)
    with np.errstate(all="ignore"):
        mean_drift = np.nanmean(stacked, axis=0)
        std_drift = np.nanstd(stacked, axis=0)

    k_full = np.arange(1, max_K + 1)
    valid = ~np.isnan(mean_drift)

    ax.errorbar(
        k_full[valid], mean_drift[valid],
        yerr=std_drift[valid],
        color="black", marker="o", markersize=4,
        linewidth=1.5, capsize=3, capthick=1,
        label=r"All-run mean $\pm 1\sigma$",
        zorder=10,
    )

    ax.axhline(0, color="0.5", linestyle=":", linewidth=0.7)

    # Phase type annotation
    phase_type = "complex" if ana["is_complex"] else "real (0/π)"
    ax.annotate(
        f"Phase type: {phase_type}",
        xy=(0.98, 0.95), xycoords="axes fraction",
        fontsize=9, ha="right", va="top",
        bbox=dict(boxstyle="round,pad=0.3", facecolor="wheat", alpha=0.7),
    )

    setup_axes(
        ax,
        xlabel="Mode index $k$",
        ylabel=r"Phase drift rate $d\varphi_k/dt$",
        title=f"Phase Drift Rates -- D={run['D']}, A={run['A']}, Nm={run['Nm']}",
    )
    ax.legend(fontsize=9, loc="upper left", framealpha=0.9)
    fig.tight_layout()

    fname = "drift_rates.png"
    fig.savefig(os.path.join(FIG_DIR, fname), dpi=300)
    plt.close(fig)
    print(f"  Saved: {fname}")


# ---------------------------------------------------------------------------
# Figure B: Phase Coherence Matrix
# ---------------------------------------------------------------------------
def figure_coherence_matrix(runs: list[dict], analyses: list[dict]):
    """Heatmap of C_ij for the largest-Nm run."""
    best_idx = max(range(len(runs)), key=lambda i: runs[i]["Nm"])
    run = runs[best_idx]
    ana = analyses[best_idx]

    C = ana["coherence_matrix"]
    K = ana["K"]

    fig, ax = plt.subplots(figsize=(9, 8))

    im = ax.imshow(
        C, cmap="YlOrRd", vmin=0, vmax=1,
        interpolation="nearest", origin="lower",
    )

    ticks = np.arange(K)
    tick_labels = [str(k + 1) for k in range(K)]
    ax.set_xticks(ticks)
    ax.set_xticklabels(tick_labels, fontsize=7, rotation=45)
    ax.set_yticks(ticks)
    ax.set_yticklabels(tick_labels, fontsize=7)

    # Annotate strong coherence
    for i in range(K):
        for j in range(K):
            if i == j:
                continue
            val = C[i, j]
            if val > 0.7:
                ax.text(j, i, f"{val:.2f}", ha="center", va="center",
                        fontsize=5, color="white", fontweight="bold")

    cbar = fig.colorbar(im, ax=ax, label="Phase coherence $C_{ij}$",
                        pad=0.02, shrink=0.85)
    cbar.ax.tick_params(labelsize=9)

    ax.annotate(
        (f"mean off-diag = {ana['mean_coherence']:.4f}\n"
         f"max = {ana['max_coherence']:.4f}\n"
         f"min = {ana['min_coherence']:.4f}"),
        xy=(0.02, 0.98), xycoords="axes fraction",
        fontsize=8, va="top",
        bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8),
    )

    setup_axes(
        ax,
        xlabel="Mode index $k$",
        ylabel="Mode index $k$",
        title=(f"Phase Coherence Matrix -- D={run['D']}, A={run['A']}, "
               f"Nm={run['Nm']}"),
    )
    fig.tight_layout()

    fname = "coherence_matrix.png"
    fig.savefig(os.path.join(FIG_DIR, fname), dpi=300)
    plt.close(fig)
    print(f"  Saved: {fname}")


# ---------------------------------------------------------------------------
# Figure C: Triad Closure Coherence
# ---------------------------------------------------------------------------
def figure_triad_closure(runs: list[dict], analyses: list[dict]):
    """Scatter triad closure coherence vs triad index for all runs."""
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

    all_coh = []

    for run, ana in zip(runs, analyses):
        tc = ana["triad_closures"]
        if not tc:
            continue

        indices = np.arange(len(tc))
        values = np.array([t["coherence"] for t in tc])
        all_coh.extend(values.tolist())

        color = D_cmap(D_norm(run["D"]))
        marker = Nm_markers.get(run["Nm"], "o")

        ax.scatter(
            indices, values,
            color=color, marker=marker, s=12, alpha=0.3,
            edgecolors="none",
        )

    # Global mean
    if all_coh:
        mean_coh = np.mean(all_coh)
        ax.axhline(mean_coh, color="black", linestyle="--",
                   linewidth=1.5, alpha=0.7,
                   label=rf"Global mean = {mean_coh:.4f}")

    # Perfect closure reference
    ax.axhline(1.0, color="0.6", linestyle=":", linewidth=0.7, alpha=0.5,
               label="Perfect closure")

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
    ax.legend(handles=legend_handles, fontsize=8, loc="lower right",
              framealpha=0.9)

    setup_axes(
        ax,
        xlabel="Triad index",
        ylabel=r"Closure coherence $|\langle e^{i\Delta_{ijk}} \rangle|$",
        title="Triad Phase Closure -- All Admissible Runs",
    )
    ax.set_ylim(-0.05, 1.05)
    fig.tight_layout()

    fname = "triad_closure.png"
    fig.savefig(os.path.join(FIG_DIR, fname), dpi=300)
    plt.close(fig)
    print(f"  Saved: {fname}")


# ---------------------------------------------------------------------------
# Summary table and invariance verdict
# ---------------------------------------------------------------------------
def print_summary(runs: list[dict], analyses: list[dict]):
    print(f"\n{'='*110}")
    print("  Invariant Modal Phase Dynamics -- Summary Table")
    print(f"{'='*110}")

    print(f"  {'D':<7} {'A':<7} {'Nm':<5} {'K':<4} {'Phase':<7} "
          f"{'mean_coh':<10} {'max_coh':<10} {'min_coh':<10} "
          f"{'triad_coh':<10} {'#triads':<8} {'mean_drift':<12}")
    print("  " + "-" * 100)

    inv_names = ["mean_coherence", "max_coherence", "min_coherence",
                 "mean_triad_coherence"]
    all_inv = {name: [] for name in inv_names}
    all_inv["mean_drift"] = []

    for run, ana in zip(runs, analyses):
        phase_type = "cplx" if ana["is_complex"] else "real"
        mean_drift = float(np.mean(np.abs(ana["drift_rates"])))

        print(f"  {run['D']:<7.3f} {run['A']:<7.4f} {run['Nm']:<5d} "
              f"{ana['K']:<4d} {phase_type:<7} "
              f"{ana['mean_coherence']:<10.4f} "
              f"{ana['max_coherence']:<10.4f} "
              f"{ana['min_coherence']:<10.4f} "
              f"{ana['mean_triad_coherence']:<10.4f} "
              f"{ana['n_triads']:<8d} "
              f"{mean_drift:<12.6e}")

        for name in inv_names:
            val = ana[name]
            if not np.isnan(val):
                all_inv[name].append(val)
        all_inv["mean_drift"].append(mean_drift)

    # Global statistics
    all_keys = inv_names + ["mean_drift"]
    print(f"\n  {'Invariant':<20} {'Mean':<12} {'Std':<12} "
          f"{'Min':<12} {'Max':<12} {'CV':<10} {'Verdict'}")
    print("  " + "-" * 84)

    for name in all_keys:
        arr = np.array(all_inv[name])
        if len(arr) == 0:
            print(f"  {name:<20} (no data)")
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

        print(f"  {name:<20} "
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
    print(f"\nAnalysing modal phase dynamics (K <= {K_MAX})...")
    analyses = []
    for i, run in enumerate(runs):
        ana = analyse_run(run)
        analyses.append(ana)
        if (i + 1) % 10 == 0 or i == len(runs) - 1:
            pt = "cplx" if ana["is_complex"] else "real"
            print(f"  [{i+1}/{len(runs)}] {run['name']}: "
                  f"K={ana['K']} ({pt}), "
                  f"coh={ana['mean_coherence']:.4f}, "
                  f"triad={ana['mean_triad_coherence']:.4f}")

    # Figures
    print("\n--- (A) Phase Drift Rates ---")
    figure_drift_rates(runs, analyses)

    print("\n--- (B) Phase Coherence Matrix ---")
    figure_coherence_matrix(runs, analyses)

    print("\n--- (C) Triad Closure Coherence ---")
    figure_triad_closure(runs, analyses)

    # Summary
    print_summary(runs, analyses)

    print(f"\nAll figures saved to: {FIG_DIR}")
    print("Done.")


if __name__ == "__main__":
    main()
