# NOTE: This is a Layer 4 meta-analysis script.
# It operates on the outputs of all Layer 3 invariant scripts.
# It is NOT a core invariant and should run AFTER all Layer 3 scripts.
# In run_all.py, it belongs to PHASE_5_META, not PHASE_4_INVARIANTS.

"""
invariant_cross_consistency.py
===============================
Experiment / Analysis: Cross-Invariant Consistency

Scans all completed regime_D*_A*_Nm* runs, loads all invariant JSON
summaries, groups the invariant components by family, and analyses
the cross-family correlation structure.

This tests whether the thirteen invariant families (low-mode collapse,
mode ratios, Renyi entropies, dissipation partitions, broadband
cascade, modal correlations, modal overlap, phase dynamics, PAC,
Lyapunov spectrum, attractor manifold, energy-entropy geometry, and
convergence stability) provide mutually consistent information about
the attractor -- or whether some families are redundant (highly
correlated) or contradictory (anti-correlated).

The ED architecture predicts that all invariants derive from the same
underlying fixed point (ρ*, 0) through different projections, so they
should be positively correlated but not perfectly redundant: each
family probes a different aspect of the nine-layer ontology.

Produces:
  (A) Cross-Invariant Correlation Heatmap -- family × family.
  (B) Redundancy Bar Chart -- per family.
  (C) Consistency Scatter -- per-run score vs D.

All figures saved to output/figures/invariants/cross_consistency/
as PNG (300 dpi).

Usage:
    python experiments/invariant_cross_consistency.py

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
INV_DIR = os.path.join(SIM_DIR, "output", "figures", "invariants")
FIG_DIR = os.path.join(SIM_DIR, "output", "figures", "invariants",
                        "cross_consistency")

# ---------------------------------------------------------------------------
# Invariant family definitions
# ---------------------------------------------------------------------------
FAMILY_SOURCES = {
    "low_mode":     "invariant_low_mode_collapse.json",
    "mode_ratios":  "invariant_mode_energy_ratios.json",
    "renyi":        "invariant_spectral_complexity.json",
    "diss_part":    "invariant_dissipation_partitions.json",
    "cascade":      "invariant_broadband_cascade.json",
    "correlations": "invariant_modal_correlations.json",
    "overlap":      "invariant_modal_overlap.json",
    "phase":        "invariant_phase_dynamics.json",
    "PAC":          "invariant_phase_amplitude_coupling.json",
    "lyapunov":     "invariant_lyapunov_spectrum.json",
    "manifold":     "invariant_attractor_manifold.json",
    "E_H_geom":    "invariant_energy_entropy_geometry.json",
    "conv_stab":    "invariant_convergence_stability.json",
}

FAMILY_ORDER = list(FAMILY_SOURCES.keys())

FAMILY_LABELS = {
    "low_mode":     "Low-Mode",
    "mode_ratios":  "Mode Ratios",
    "renyi":        "Renyi",
    "diss_part":    "Dissipation",
    "cascade":      "Cascade",
    "correlations": "Correlations",
    "overlap":      "Overlap",
    "phase":        "Phase",
    "PAC":          "PAC",
    "lyapunov":     "Lyapunov",
    "manifold":     "Manifold",
    "E_H_geom":    "E-H Geom",
    "conv_stab":    "Conv Stab",
}


# ---------------------------------------------------------------------------
# Discovery
# ---------------------------------------------------------------------------
def discover_regime_runs() -> list[dict]:
    pattern = os.path.join(RUNS_DIR, "regime_D*_A*_Nm*")
    dirs = sorted(glob.glob(pattern))

    runs = []
    for d in dirs:
        if "perturb_eps" in os.path.basename(d):
            continue

        meta_path = os.path.join(d, "metadata.json")
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

        # Load invariant summaries per family
        family_data = {}
        for fam, src in FAMILY_SOURCES.items():
            for p in [os.path.join(d, src),
                      os.path.join(d, "invariants", src),
                      os.path.join(INV_DIR, src)]:
                if os.path.isfile(p):
                    with open(p, "r") as f:
                        family_data[fam] = json.load(f)
                    break

        runs.append({
            "dir": d,
            "name": name,
            "D": float(D_val),
            "A": float(A_val),
            "Nm": int(Nm_val),
            "metadata": meta,
            "family_data": family_data,
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
# Flatten JSON into numeric vectors
# ---------------------------------------------------------------------------
def _flatten_json(obj, prefix: str = "") -> list[tuple[str, float]]:
    items = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            items.extend(_flatten_json(v, f"{prefix}.{k}" if prefix else k))
    elif isinstance(obj, (list, tuple)):
        for i, v in enumerate(obj):
            if isinstance(v, (int, float)) and not isinstance(v, bool):
                if np.isfinite(v):
                    items.append((f"{prefix}[{i}]", float(v)))
            elif isinstance(v, dict):
                items.extend(_flatten_json(v, f"{prefix}[{i}]"))
    elif isinstance(obj, (int, float)) and not isinstance(obj, bool):
        if np.isfinite(obj):
            items.append((prefix, float(obj)))
    return items


# ---------------------------------------------------------------------------
# Build per-family matrices
# ---------------------------------------------------------------------------
def build_family_matrices(runs: list[dict]) -> dict:
    """For each family, build an (n_runs × n_components) matrix.

    Returns dict mapping family_name -> {
        "keys": list[str], "matrix": ndarray (n_runs, n_keys)
    }
    Missing values are NaN.
    """
    n_runs = len(runs)
    families = {}

    for fam in FAMILY_ORDER:
        # Collect all keys across runs for this family
        all_keys_set = set()
        all_keys_ordered = []
        run_items = []

        for run in runs:
            data = run["family_data"].get(fam)
            if data is None:
                run_items.append({})
                continue
            items = _flatten_json(data)
            d = dict(items)
            run_items.append(d)
            for k, _ in items:
                if k not in all_keys_set:
                    all_keys_ordered.append(k)
                    all_keys_set.add(k)

        if not all_keys_ordered:
            continue

        n_keys = len(all_keys_ordered)
        matrix = np.full((n_runs, n_keys), np.nan)

        for i, d in enumerate(run_items):
            for j, k in enumerate(all_keys_ordered):
                if k in d:
                    matrix[i, j] = d[k]

        families[fam] = {
            "keys": all_keys_ordered,
            "matrix": matrix,
        }

    return families


def standardize_columns(matrix: np.ndarray) -> np.ndarray:
    """Z-score each column, NaN-robust. Zero-variance columns → 0."""
    Z = np.zeros_like(matrix)
    for j in range(matrix.shape[1]):
        col = matrix[:, j]
        valid = ~np.isnan(col)
        if np.sum(valid) < 2:
            continue
        m = np.nanmean(col)
        s = np.nanstd(col)
        if s < 1e-30:
            continue
        Z[:, j] = np.where(valid, (col - m) / s, 0.0)
    return Z


# ---------------------------------------------------------------------------
# Cross-family correlation
# ---------------------------------------------------------------------------
def compute_family_summary_vectors(families: dict, n_runs: int) -> dict:
    """For each family, compute a single summary vector per run.

    Uses the mean of the standardized components as the summary.
    Returns dict mapping family -> ndarray of shape (n_runs,).
    """
    summaries = {}
    for fam, fdata in families.items():
        Z = standardize_columns(fdata["matrix"])
        # Summary: mean of non-NaN standardized components per run
        with np.errstate(all="ignore"):
            summary = np.nanmean(Z, axis=1)
        summary = np.nan_to_num(summary, nan=0.0)
        summaries[fam] = summary
    return summaries


def compute_cross_family_correlation(summaries: dict) -> tuple:
    """Compute the F × F correlation matrix between family summaries.

    Returns (fam_names, corr_matrix).
    """
    fam_names = [f for f in FAMILY_ORDER if f in summaries]
    F = len(fam_names)

    corr = np.zeros((F, F))
    for i in range(F):
        for j in range(F):
            xi = summaries[fam_names[i]]
            xj = summaries[fam_names[j]]
            # Pearson correlation
            corr[i, j] = _safe_corr(xi, xj)

    return fam_names, corr


def _safe_corr(x: np.ndarray, y: np.ndarray) -> float:
    sx = np.std(x)
    sy = np.std(y)
    if sx < 1e-30 or sy < 1e-30 or len(x) < 3:
        return 0.0
    return float(np.corrcoef(x, y)[0, 1])


def compute_redundancy(fam_names: list[str], corr: np.ndarray) -> dict:
    """Redundancy(A) = mean |corr(A, B)| for B ≠ A."""
    F = len(fam_names)
    redundancy = {}
    for i in range(F):
        others = [abs(corr[i, j]) for j in range(F) if j != i]
        redundancy[fam_names[i]] = float(np.mean(others)) if others else 0.0
    return redundancy


def compute_per_run_consistency(families: dict, fam_names: list[str],
                                 n_runs: int) -> np.ndarray:
    """Per-run consistency: mean |corr| between family pairs within each run.

    Approximated by: for each run, compute the variance of the family
    summary values (low variance → high consistency).
    """
    summaries_matrix = np.zeros((n_runs, len(fam_names)))
    for j, fam in enumerate(fam_names):
        Z = standardize_columns(families[fam]["matrix"])
        with np.errstate(all="ignore"):
            summaries_matrix[:, j] = np.nan_to_num(np.nanmean(Z, axis=1), nan=0.0)

    # Per-run consistency: 1 / (1 + std across families)
    per_run_std = np.std(summaries_matrix, axis=1)
    consistency = 1.0 / (1.0 + per_run_std)

    return consistency


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
# Figure A: Cross-Invariant Correlation Heatmap
# ---------------------------------------------------------------------------
def figure_correlation_heatmap(fam_names: list[str], corr: np.ndarray):
    F = len(fam_names)
    labels = [FAMILY_LABELS.get(f, f) for f in fam_names]

    fig, ax = plt.subplots(figsize=(10, 9))

    im = ax.imshow(
        corr, cmap="RdBu_r", vmin=-1, vmax=1,
        interpolation="nearest",
    )

    ax.set_xticks(range(F))
    ax.set_xticklabels(labels, fontsize=8, rotation=45, ha="right")
    ax.set_yticks(range(F))
    ax.set_yticklabels(labels, fontsize=8)

    # Annotate
    for i in range(F):
        for j in range(F):
            val = corr[i, j]
            txt_color = "white" if abs(val) > 0.6 else "black"
            ax.text(j, i, f"{val:.2f}", ha="center", va="center",
                    fontsize=6, color=txt_color,
                    fontweight="bold" if abs(val) > 0.5 else "normal")

    cbar = fig.colorbar(im, ax=ax, label="Pearson correlation",
                        pad=0.02, shrink=0.85)
    cbar.ax.tick_params(labelsize=9)

    # Global consistency
    mask_off = ~np.eye(F, dtype=bool)
    C = float(np.mean(np.abs(corr[mask_off]))) if F > 1 else 0.0
    ax.annotate(
        f"Consistency $C = {C:.4f}$",
        xy=(0.02, 0.98), xycoords="axes fraction",
        fontsize=10, va="top",
        bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8),
    )

    setup_axes(ax, "", "", "Cross-Invariant Correlation Matrix")
    fig.tight_layout()

    fname = "correlation_heatmap.png"
    fig.savefig(os.path.join(FIG_DIR, fname), dpi=300)
    plt.close(fig)
    print(f"  Saved: {fname}")


# ---------------------------------------------------------------------------
# Figure B: Redundancy Bar Chart
# ---------------------------------------------------------------------------
def figure_redundancy_bars(fam_names: list[str], redundancy: dict):
    F = len(fam_names)
    labels = [FAMILY_LABELS.get(f, f) for f in fam_names]
    values = [redundancy[f] for f in fam_names]

    fig, ax = plt.subplots(figsize=(12, 5))

    colors = []
    for v in values:
        if v > 0.8:
            colors.append("#b2182b")   # redundant
        elif v < 0.2:
            colors.append("#2166ac")   # independent
        else:
            colors.append("#999999")   # intermediate

    bars = ax.bar(range(F), values, color=colors, alpha=0.8, width=0.7)

    # Thresholds
    ax.axhline(0.8, color="#b2182b", linestyle="--", linewidth=1.0,
               alpha=0.5, label="Redundant (> 0.8)")
    ax.axhline(0.2, color="#2166ac", linestyle="--", linewidth=1.0,
               alpha=0.5, label="Independent (< 0.2)")

    ax.set_xticks(range(F))
    ax.set_xticklabels(labels, fontsize=9, rotation=45, ha="right")
    ax.set_ylim(0, 1.05)

    # Value labels
    for i, v in enumerate(values):
        ax.text(i, v + 0.02, f"{v:.2f}", ha="center", va="bottom",
                fontsize=7, fontweight="bold")

    setup_axes(ax, "", r"Redundancy = mean $|\mathrm{corr}|$ with others",
               "Invariant Family Redundancy")
    ax.legend(fontsize=9, loc="upper right", framealpha=0.9)
    fig.tight_layout()

    fname = "redundancy_bars.png"
    fig.savefig(os.path.join(FIG_DIR, fname), dpi=300)
    plt.close(fig)
    print(f"  Saved: {fname}")


# ---------------------------------------------------------------------------
# Figure C: Consistency Scatter
# ---------------------------------------------------------------------------
def figure_consistency_scatter(runs: list[dict],
                                consistency: np.ndarray,
                                C_global: float):
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

    for i, run in enumerate(runs):
        color = A_cmap(A_norm(run["A"]))
        marker = Nm_markers.get(run["Nm"], "o")
        ax.scatter(
            run["D"], consistency[i],
            color=color, marker=marker, s=60, alpha=0.7,
            edgecolors="0.3", linewidths=0.4,
        )

    ax.axhline(np.mean(consistency), color="0.4", linestyle="--",
               linewidth=1.0, alpha=0.6)

    # Verdict
    if C_global > 0.8:
        verdict = "CONSISTENT"
        v_color = "#1b7837"
    elif C_global > 0.5:
        verdict = "PARTIALLY CONSISTENT"
        v_color = "#e6ab02"
    else:
        verdict = "INCONSISTENT"
        v_color = "#b2182b"

    ax.annotate(
        f"$C = {C_global:.4f}$ -- {verdict}",
        xy=(0.98, 0.95), xycoords="axes fraction",
        fontsize=11, fontweight="bold", ha="right", va="top",
        color=v_color,
        bbox=dict(boxstyle="round,pad=0.4", facecolor="white", alpha=0.8),
    )

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
    ax.legend(handles=legend_handles, fontsize=8, loc="lower right",
              framealpha=0.9)

    setup_axes(
        ax,
        xlabel=r"Diffusion $D$",
        ylabel="Per-run consistency score",
        title="Cross-Invariant Consistency -- All Runs",
    )
    ax.set_ylim(0, 1.05)
    fig.tight_layout()

    fname = "consistency_scatter.png"
    fig.savefig(os.path.join(FIG_DIR, fname), dpi=300)
    plt.close(fig)
    print(f"  Saved: {fname}")


# ---------------------------------------------------------------------------
# Summary table
# ---------------------------------------------------------------------------
def print_summary(fam_names: list[str], corr: np.ndarray,
                  redundancy: dict, families: dict,
                  runs: list[dict], C_global: float):
    F = len(fam_names)

    print(f"\n{'='*110}")
    print("  Cross-Invariant Consistency -- Summary")
    print(f"{'='*110}")

    # Per-family table
    print(f"\n  {'Family':<16} {'#Comp':<8} {'Redund':<10} "
          f"{'Top corr partner':<22} {'r_top':<8} "
          f"{'Least corr partner':<22} {'r_min':<8}")
    print("  " + "-" * 100)

    for i, fam in enumerate(fam_names):
        n_comp = len(families[fam]["keys"]) if fam in families else 0
        red = redundancy.get(fam, 0.0)

        # Find top and least correlated partner
        if F > 1:
            corrs_others = [(abs(corr[i, j]), corr[i, j], fam_names[j])
                            for j in range(F) if j != i]
            corrs_others.sort(key=lambda x: x[0], reverse=True)
            top_name = FAMILY_LABELS.get(corrs_others[0][2], corrs_others[0][2])
            top_r = corrs_others[0][1]
            bot_name = FAMILY_LABELS.get(corrs_others[-1][2], corrs_others[-1][2])
            bot_r = corrs_others[-1][1]
        else:
            top_name = "--"
            top_r = 0.0
            bot_name = "--"
            bot_r = 0.0

        label = FAMILY_LABELS.get(fam, fam)
        print(f"  {label:<16} {n_comp:<8d} {red:<10.4f} "
              f"{top_name:<22} {top_r:<+8.4f} "
              f"{bot_name:<22} {bot_r:<+8.4f}")

    # Classification
    redundant = [FAMILY_LABELS.get(f, f) for f in fam_names
                 if redundancy.get(f, 0) > 0.8]
    independent = [FAMILY_LABELS.get(f, f) for f in fam_names
                   if redundancy.get(f, 0) < 0.2]

    if redundant:
        print(f"\n  Highly redundant families: {', '.join(redundant)}")
    if independent:
        print(f"  Independent families: {', '.join(independent)}")

    # Global diagnostics
    mask_off = ~np.eye(F, dtype=bool)
    abs_corr_off = np.abs(corr[mask_off])

    print(f"\n  Cross-family correlation statistics:")
    print(f"    Mean |corr|: {np.mean(abs_corr_off):.4f}")
    print(f"    Min  |corr|: {np.min(abs_corr_off):.4f}")
    print(f"    Max  |corr|: {np.max(abs_corr_off):.4f}")
    print(f"    Consistency score C = {C_global:.4f}")

    if C_global > 0.8:
        print(f"    Verdict: CONSISTENT (C > 0.8)")
    elif C_global > 0.5:
        print(f"    Verdict: PARTIALLY CONSISTENT (C > 0.5)")
    else:
        print(f"    Verdict: INCONSISTENT (C <= 0.5)")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    os.makedirs(FIG_DIR, exist_ok=True)

    print("Discovering regime volume runs and invariant summaries...")
    runs = discover_regime_runs()

    if not runs:
        print(f"\nERROR: No admissible regime_D*_A*_Nm* runs found in:")
        print(f"  {RUNS_DIR}")
        sys.exit(1)

    total_fam = sum(len(r["family_data"]) for r in runs)
    print(f"  Found {len(runs)} runs, {total_fam} family files loaded "
          f"({total_fam / max(len(runs), 1):.1f} per run)")

    if total_fam == 0:
        print("\n  WARNING: No invariant JSON files found.")
        print("  Run the invariant analysis scripts first.")
        print("  Proceeding with empty data...")

    # Build per-family matrices
    print("\nBuilding per-family invariant matrices...")
    families = build_family_matrices(runs)
    active_families = [f for f in FAMILY_ORDER if f in families]
    print(f"  Active families: {len(active_families)}/{len(FAMILY_ORDER)}")

    if len(active_families) < 2:
        print("\n  ERROR: Need at least 2 active families for cross-consistency.")
        print("  Run more invariant analysis scripts first.")
        sys.exit(1)

    # Family summaries and cross-correlation
    print("\nComputing cross-family correlations...")
    summaries = compute_family_summary_vectors(families, len(runs))
    fam_names, corr = compute_cross_family_correlation(summaries)
    redundancy = compute_redundancy(fam_names, corr)

    F = len(fam_names)
    mask_off = ~np.eye(F, dtype=bool)
    C_global = float(np.mean(np.abs(corr[mask_off]))) if F > 1 else 0.0

    # Per-run consistency
    consistency = compute_per_run_consistency(families, fam_names, len(runs))

    # Figures
    print("\n--- (A) Correlation Heatmap ---")
    figure_correlation_heatmap(fam_names, corr)

    print("\n--- (B) Redundancy Bars ---")
    figure_redundancy_bars(fam_names, redundancy)

    print("\n--- (C) Consistency Scatter ---")
    figure_consistency_scatter(runs, consistency, C_global)

    # Summary
    print_summary(fam_names, corr, redundancy, families, runs, C_global)

    print(f"\nAll figures saved to: {FIG_DIR}")
    print("Done.")


if __name__ == "__main__":
    main()
