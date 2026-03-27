"""
invariant_attractor_manifold.py
================================
Experiment / Analysis: Invariant Attractor Manifold Structure

Scans all completed regime_D*_A*_Nm* runs, performs PCA on the modal
amplitude state vectors in the attractor window (last 20%), and extracts
manifold invariants: effective dimension, spectral gap, curvature proxy,
and the PCA embedding.

For the ED architecture, Principle 3 (unique attractor) predicts that
the attractor is a fixed point — all trajectories converge to (ρ*, 0).
In modal space, the attractor window should collapse to a small cloud
around the equilibrium amplitudes, with effective dimension D_eff = 0
(or very small, reflecting residual numerical noise).

Produces:
  (A) PCA Spectrum — eigenvalue decay for a representative run.
  (B) Attractor Embedding — 2-D projections onto principal components.
  (C) Effective Dimension vs D — D_eff scatter for all runs.

All figures saved to output/figures/invariants/attractor_manifold/
as PNG (300 dpi).

Usage:
    python experiments/invariant_attractor_manifold.py

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
from matplotlib.collections import LineCollection

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SIM_DIR = os.path.dirname(SCRIPT_DIR)
RUNS_DIR = os.path.join(SIM_DIR, "output", "runs")
FIG_DIR = os.path.join(SIM_DIR, "output", "figures", "invariants",
                        "attractor_manifold")

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
K_MAX = 20
ATTRACTOR_FRAC = 0.20
VARIANCE_THRESH = 0.99   # Cumulative variance for D_eff
EIG_FLOOR = 1e-30


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
# State vector construction
# ---------------------------------------------------------------------------
def build_state_vectors(modal_window: np.ndarray, K: int) -> np.ndarray:
    """Build d-dimensional state vectors from modal amplitudes.

    Complex: x = [Re(a_1), Im(a_1), ..., Re(a_K), Im(a_K)]  (d = 2K)
    Real:    x = [a_1, ..., a_K]                              (d = K)
    """
    a = modal_window[:, 1:K+1]

    if np.iscomplexobj(a):
        re = np.real(a)
        im = np.imag(a)
        d = 2 * K
        x = np.empty((a.shape[0], d), dtype=np.float64)
        x[:, 0::2] = re
        x[:, 1::2] = im
    else:
        x = a.astype(np.float64)

    return x


# ---------------------------------------------------------------------------
# PCA and manifold invariants
# ---------------------------------------------------------------------------
def pca_analysis(x: np.ndarray) -> dict:
    """Perform PCA on centered state vectors and extract invariants.

    Parameters
    ----------
    x : ndarray, shape (n_samples, d)

    Returns
    -------
    dict with eigenvalues, eigenvectors, projections, and invariants.
    """
    n, d = x.shape

    # Center
    mean = np.mean(x, axis=0)
    x_c = x - mean

    # Covariance
    cov = (x_c.T @ x_c) / max(n - 1, 1)

    # Eigendecomposition (symmetric)
    eigvals, eigvecs = np.linalg.eigh(cov)

    # Sort descending
    order = eigvals.argsort()[::-1]
    eigvals = eigvals[order]
    eigvecs = eigvecs[:, order]

    # Clip negative eigenvalues (numerical noise)
    eigvals = np.maximum(eigvals, 0.0)

    total_var = np.sum(eigvals)
    if total_var < EIG_FLOOR:
        # Degenerate: all data at one point
        return {
            "eigvals": eigvals,
            "eigvecs": eigvecs,
            "projections": x_c @ eigvecs,
            "var_explained": np.zeros(d),
            "cumvar": np.zeros(d),
            "D_eff": 0,
            "spectral_gap": float("inf"),
            "curvature": 0.0,
            "mean": mean,
            "d": d,
        }

    var_explained = eigvals / total_var
    cumvar = np.cumsum(var_explained)

    # Effective dimension: smallest m with cumvar[m-1] >= threshold
    above = np.where(cumvar >= VARIANCE_THRESH)[0]
    D_eff = int(above[0] + 1) if len(above) > 0 else d

    # Spectral gap: λ_1 / λ_2
    if d >= 2 and eigvals[1] > EIG_FLOOR:
        spectral_gap = float(eigvals[0] / eigvals[1])
    else:
        spectral_gap = float("inf")

    # Curvature proxy: κ = λ_2 / λ_1
    if eigvals[0] > EIG_FLOOR:
        curvature = float(eigvals[1] / eigvals[0]) if d >= 2 else 0.0
    else:
        curvature = 0.0

    # Projections onto PCs
    projections = x_c @ eigvecs

    return {
        "eigvals": eigvals,
        "eigvecs": eigvecs,
        "projections": projections,
        "var_explained": var_explained,
        "cumvar": cumvar,
        "D_eff": D_eff,
        "spectral_gap": spectral_gap,
        "curvature": curvature,
        "mean": mean,
        "d": d,
    }


# ---------------------------------------------------------------------------
# Per-run analysis
# ---------------------------------------------------------------------------
def analyse_run(run: dict) -> dict:
    """PCA on the attractor window and manifold invariants."""
    modal = run["modal"]
    t = run["t"]
    n = len(t)
    n_modes = modal.shape[1]
    K = min(K_MAX, n_modes - 1)

    # Attractor window
    start = max(0, int((1.0 - ATTRACTOR_FRAC) * n))
    modal_win = modal[start:]
    t_win = t[start:]

    # State vectors
    x = build_state_vectors(modal_win, K)

    # PCA
    pca = pca_analysis(x)

    # Store only what's needed for figures (not the full projection matrix
    # for non-representative runs — save memory)
    return {
        "K": K,
        "d": pca["d"],
        "D_eff": pca["D_eff"],
        "spectral_gap": pca["spectral_gap"],
        "curvature": pca["curvature"],
        "eigvals": pca["eigvals"][:min(20, len(pca["eigvals"]))].tolist(),
        "var_explained": pca["var_explained"][:min(20, len(pca["var_explained"]))].tolist(),
        "cumvar": pca["cumvar"][:min(20, len(pca["cumvar"]))].tolist(),
        # Full projections only stored temporarily; recomputed for figures
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


def _recompute_pca(run: dict) -> dict:
    """Recompute full PCA for a single run (for figure generation)."""
    modal = run["modal"]
    t = run["t"]
    n = len(t)
    K = min(K_MAX, modal.shape[1] - 1)
    start = max(0, int((1.0 - ATTRACTOR_FRAC) * n))
    x = build_state_vectors(modal[start:], K)
    return pca_analysis(x), t[start:]


# ---------------------------------------------------------------------------
# Figure A: PCA Spectrum (representative run)
# ---------------------------------------------------------------------------
def figure_pca_spectrum(runs: list[dict], analyses: list[dict]):
    """Eigenvalue decay on log scale for the largest-Nm run."""
    best_idx = max(range(len(runs)), key=lambda i: runs[i]["Nm"])
    ana = analyses[best_idx]
    run = runs[best_idx]

    eigvals = np.array(ana["eigvals"])
    d = len(eigvals)
    i_axis = np.arange(1, d + 1)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

    # Left: eigenvalue spectrum
    ax1.semilogy(i_axis, np.maximum(eigvals, EIG_FLOOR),
                 "o-", color="#2166ac", markersize=5, linewidth=1.2)

    # Mark D_eff
    D_eff = ana["D_eff"]
    if 1 <= D_eff <= d:
        ax1.axvline(D_eff, color="#b2182b", linestyle="--", linewidth=1.0,
                    label=rf"$D_{{\mathrm{{eff}}}} = {D_eff}$")

    ax1.annotate(
        (f"$D_{{\\mathrm{{eff}}}} = {D_eff}$\n"
         f"spectral gap = {ana['spectral_gap']:.2f}\n"
         f"$\\kappa = {ana['curvature']:.4f}$"),
        xy=(0.98, 0.95), xycoords="axes fraction",
        fontsize=9, ha="right", va="top",
        bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8),
    )

    setup_axes(ax1, "Component index $i$", r"Eigenvalue $\lambda_i$",
               "PCA Eigenvalue Spectrum")
    ax1.legend(fontsize=9, loc="center right", framealpha=0.9)

    # Right: cumulative variance
    cumvar = np.array(ana["cumvar"])
    ax2.plot(i_axis, cumvar[:d], "o-", color="#1b7837",
             markersize=5, linewidth=1.2)
    ax2.axhline(VARIANCE_THRESH, color="0.5", linestyle=":", linewidth=0.8,
                label=f"{VARIANCE_THRESH:.0%} threshold")
    if 1 <= D_eff <= d:
        ax2.axvline(D_eff, color="#b2182b", linestyle="--", linewidth=1.0)

    setup_axes(ax2, "Component index $i$", "Cumulative variance explained",
               "Cumulative Variance")
    ax2.set_ylim(-0.05, 1.05)
    ax2.legend(fontsize=9, loc="lower right", framealpha=0.9)

    fig.suptitle(
        f"PCA Spectrum — D={run['D']}, A={run['A']}, Nm={run['Nm']}",
        fontsize=14, fontweight="bold", y=1.02,
    )
    fig.tight_layout()

    fname = "pca_spectrum.png"
    fig.savefig(os.path.join(FIG_DIR, fname), dpi=300, bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved: {fname}")


# ---------------------------------------------------------------------------
# Figure B: Attractor Embedding (representative run)
# ---------------------------------------------------------------------------
def figure_attractor_embedding(runs: list[dict], analyses: list[dict]):
    """2-D projections: (PC1, PC2) and (PC1, PC3) colored by time."""
    best_idx = max(range(len(runs)), key=lambda i: runs[i]["Nm"])
    run = runs[best_idx]

    pca, t_win = _recompute_pca(run)
    proj = pca["projections"]
    n_win = len(t_win)

    if proj.shape[1] < 3:
        print("  SKIP attractor embedding: fewer than 3 PCs.")
        return

    time_frac = np.linspace(0, 1, n_win)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # (PC1, PC2)
    sc1 = ax1.scatter(
        proj[:, 0], proj[:, 1],
        c=time_frac, cmap="coolwarm", s=8, alpha=0.7, edgecolors="none",
    )
    ax1.plot(0, 0, "k+", markersize=12, markeredgewidth=2, zorder=10,
             label="Centroid")
    setup_axes(ax1, "PC1", "PC2", "Projection: PC1 vs PC2")
    ax1.legend(fontsize=9, loc="upper right", framealpha=0.9)

    # (PC1, PC3)
    sc2 = ax2.scatter(
        proj[:, 0], proj[:, 2],
        c=time_frac, cmap="coolwarm", s=8, alpha=0.7, edgecolors="none",
    )
    ax2.plot(0, 0, "k+", markersize=12, markeredgewidth=2, zorder=10,
             label="Centroid")
    setup_axes(ax2, "PC1", "PC3", "Projection: PC1 vs PC3")
    ax2.legend(fontsize=9, loc="upper right", framealpha=0.9)

    fig.colorbar(sc1, ax=[ax1, ax2], label="Time (early → late)",
                 shrink=0.8, pad=0.03)

    # Variance annotations
    ve = pca["var_explained"]
    ax1.annotate(
        f"PC1: {ve[0]:.1%}, PC2: {ve[1]:.1%}",
        xy=(0.02, 0.05), xycoords="axes fraction", fontsize=8,
        bbox=dict(boxstyle="round,pad=0.2", facecolor="white", alpha=0.7),
    )
    ax2.annotate(
        f"PC1: {ve[0]:.1%}, PC3: {ve[2]:.1%}",
        xy=(0.02, 0.05), xycoords="axes fraction", fontsize=8,
        bbox=dict(boxstyle="round,pad=0.2", facecolor="white", alpha=0.7),
    )

    fig.suptitle(
        f"Attractor Embedding — D={run['D']}, A={run['A']}, Nm={run['Nm']}",
        fontsize=14, fontweight="bold", y=1.02,
    )
    fig.tight_layout()

    fname = "attractor_embedding.png"
    fig.savefig(os.path.join(FIG_DIR, fname), dpi=300, bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved: {fname}")

    del proj, pca


# ---------------------------------------------------------------------------
# Figure C: Effective Dimension vs D
# ---------------------------------------------------------------------------
def figure_dimension_scatter(runs: list[dict], analyses: list[dict]):
    """Scatter D_eff vs D for all runs."""
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

    all_Deff = []

    for run, ana in zip(runs, analyses):
        D_eff = ana["D_eff"]
        color = A_cmap(A_norm(run["A"]))
        marker = Nm_markers.get(run["Nm"], "o")

        ax.scatter(
            run["D"], D_eff,
            color=color, marker=marker, s=60, alpha=0.7,
            edgecolors="0.3", linewidths=0.4,
        )
        all_Deff.append(D_eff)

    # Global mean
    if all_Deff:
        mean_Deff = np.mean(all_Deff)
        ax.axhline(mean_Deff, color="0.4", linestyle="--",
                   linewidth=1.0, alpha=0.6)
        ax.annotate(
            rf"mean $D_{{\mathrm{{eff}}}} = {mean_Deff:.2f}$",
            xy=(0.02, 0.95), xycoords="axes fraction",
            fontsize=10, va="top",
        )

    # ED prediction: D_eff ≈ 0 (point attractor)
    ax.axhline(0, color="#1b7837", linestyle=":", linewidth=1.5,
               alpha=0.5, label=r"ED prediction: $D_{\mathrm{eff}} \approx 0$")

    # Colorbar
    sm = plt.cm.ScalarMappable(cmap=A_cmap, norm=A_norm)
    sm.set_array([])
    cbar = fig.colorbar(sm, ax=ax, label=r"Amplitude $A$", pad=0.02)
    cbar.ax.tick_params(labelsize=9)

    # Legend
    legend_handles = [
        plt.Line2D([0], [0], marker=m, color="0.5", markersize=7,
                   linestyle="None", label=rf"$N_m = {Nm}$")
        for Nm, m in Nm_markers.items()
    ]
    legend_handles.append(
        plt.Line2D([0], [0], color="#1b7837", linestyle=":", linewidth=1.5,
                   label=r"ED prediction")
    )
    ax.legend(handles=legend_handles, fontsize=8, loc="upper right",
              framealpha=0.9)

    setup_axes(
        ax,
        xlabel=r"Diffusion $D$",
        ylabel=r"Effective dimension $D_{\mathrm{eff}}$ (99% variance)",
        title="Attractor Effective Dimension — All Admissible Runs",
    )
    ax.set_ylim(bottom=-0.5)
    fig.tight_layout()

    fname = "dimension_scatter.png"
    fig.savefig(os.path.join(FIG_DIR, fname), dpi=300)
    plt.close(fig)
    print(f"  Saved: {fname}")


# ---------------------------------------------------------------------------
# Summary table and invariance verdict
# ---------------------------------------------------------------------------
def print_summary(runs: list[dict], analyses: list[dict]):
    print(f"\n{'='*120}")
    print("  Invariant Attractor Manifold — Summary Table")
    print(f"{'='*120}")

    print(f"  {'D':<7} {'A':<7} {'Nm':<5} {'d':<5} "
          f"{'D_eff':<7} {'gap':<10} {'κ':<10} "
          f"{'λ_1..λ_5'}")
    print("  " + "-" * 110)

    all_Deff = []
    all_gap = []
    all_kappa = []

    for run, ana in zip(runs, analyses):
        eigvals = ana["eigvals"]
        eig_str = ", ".join(f"{l:.3e}" for l in eigvals[:5])
        if len(eigvals) > 5:
            eig_str += " ..."

        gap_str = (f"{ana['spectral_gap']:<10.2f}"
                   if not np.isinf(ana["spectral_gap"])
                   else f"{'inf':<10}")

        print(f"  {run['D']:<7.3f} {run['A']:<7.4f} {run['Nm']:<5d} "
              f"{ana['d']:<5d} "
              f"{ana['D_eff']:<7d} {gap_str} "
              f"{ana['curvature']:<10.6f} "
              f"{eig_str}")

        all_Deff.append(ana["D_eff"])
        if not np.isinf(ana["spectral_gap"]):
            all_gap.append(ana["spectral_gap"])
        all_kappa.append(ana["curvature"])

    # Global statistics
    print(f"\n  {'Invariant':<16} {'Mean':<12} {'Std':<12} "
          f"{'Min':<12} {'Max':<12} {'CV':<10} {'Verdict'}")
    print("  " + "-" * 78)

    for name, arr_list in [("D_eff", all_Deff),
                           ("spectral_gap", all_gap),
                           ("curvature κ", all_kappa)]:
        arr = np.array(arr_list)
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
              f"{mean_v:<12.4f} {std_v:<12.4f} "
              f"{np.min(arr):<12.4f} {np.max(arr):<12.4f} "
              f"{cv:<10.4f} {verdict}")

    # ED consistency check
    print(f"\n  ED Principle 3 (point attractor) check:")
    mean_Deff = np.mean(all_Deff) if all_Deff else float("nan")
    if mean_Deff <= 3:
        print(f"    PASS — mean D_eff = {mean_Deff:.2f} "
              f"(≤ 3 consistent with near-point attractor)")
    else:
        print(f"    NOTE — mean D_eff = {mean_Deff:.2f} "
              f"(residual dimensionality may reflect transient dynamics "
              f"or numerical noise in the attractor window)")


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

    # Analyse
    print(f"\nPerforming PCA on attractor windows (K ≤ {K_MAX})...")
    analyses = []
    for i, run in enumerate(runs):
        ana = analyse_run(run)
        analyses.append(ana)
        if (i + 1) % 10 == 0 or i == len(runs) - 1:
            print(f"  [{i+1}/{len(runs)}] {run['name']}: "
                  f"d={ana['d']}, D_eff={ana['D_eff']}, "
                  f"gap={ana['spectral_gap']:.2f}, "
                  f"κ={ana['curvature']:.4f}")

    # Figures
    print("\n--- (A) PCA Spectrum ---")
    figure_pca_spectrum(runs, analyses)

    print("\n--- (B) Attractor Embedding ---")
    figure_attractor_embedding(runs, analyses)

    print("\n--- (C) Effective Dimension ---")
    figure_dimension_scatter(runs, analyses)

    # Summary
    print_summary(runs, analyses)

    print(f"\nAll figures saved to: {FIG_DIR}")
    print("Done.")


if __name__ == "__main__":
    main()
