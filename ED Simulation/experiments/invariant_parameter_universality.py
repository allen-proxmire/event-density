"""
invariant_parameter_universality.py
====================================
Experiment / Analysis: Parameter Universality of ED Invariants

Scans all completed regime_D*_A*_Nm* runs, loads the summary invariants
produced by each invariant analysis script, constructs a unified
invariant vector per run, and tests whether the invariant vectors are
universal across the (D, A, Nm) parameter space.

The universality hypothesis (Appendix D, Theorems D.7–D.19) predicts
that all systems satisfying Principles 1–7 share the same qualitative
invariant structure.  This script quantifies the degree of universality
by measuring the pairwise distance between standardised invariant
vectors and computing a scalar universality score U.

Produces:
  (A) Distance Matrix Heatmap — pairwise distances with clustered ordering.
  (B) Dendrogram — hierarchical clustering coloured by parameters.
  (C) Universality Scatter — U vs D for all runs.

All figures saved to output/figures/invariants/parameter_universality/
as PNG (300 dpi).

Usage:
    python experiments/invariant_parameter_universality.py

Requires: numpy, matplotlib, scipy.
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

# Optional: scipy for clustering — graceful fallback if unavailable
try:
    from scipy.cluster.hierarchy import linkage, dendrogram, fcluster
    from scipy.spatial.distance import pdist, squareform
    HAS_SCIPY = True
except ImportError:
    HAS_SCIPY = False

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SIM_DIR = os.path.dirname(SCRIPT_DIR)
RUNS_DIR = os.path.join(SIM_DIR, "output", "runs")
INV_DIR = os.path.join(SIM_DIR, "output", "figures", "invariants")
FIG_DIR = os.path.join(SIM_DIR, "output", "figures", "invariants",
                        "parameter_universality")

# ---------------------------------------------------------------------------
# Invariant source files (one per analysis script)
# ---------------------------------------------------------------------------
INVARIANT_SOURCES = [
    "invariant_low_mode_collapse.json",
    "invariant_mode_energy_ratios.json",
    "invariant_spectral_complexity.json",
    "invariant_dissipation_partitions.json",
    "invariant_energy_entropy_geometry.json",
    "invariant_broadband_cascade.json",
    "invariant_convergence_stability.json",
    "invariant_modal_correlations.json",
    "invariant_modal_overlap.json",
    "invariant_phase_dynamics.json",
    "invariant_phase_amplitude_coupling.json",
    "invariant_lyapunov_spectrum.json",
    "invariant_attractor_manifold.json",
]

# Clustering parameters
DISSIMILARITY_THRESH = 0.05  # 5% relative dissimilarity for cluster count


# ---------------------------------------------------------------------------
# Discovery
# ---------------------------------------------------------------------------
def discover_regime_runs() -> list[dict]:
    """Scan for base regime runs and load their invariant summaries."""
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

        # Load invariant summaries
        inv_data = {}
        for src in INVARIANT_SOURCES:
            # Try: in the run directory
            path1 = os.path.join(d, src)
            # Try: in a global invariants summary directory
            path2 = os.path.join(INV_DIR, src)
            # Try: with the run name embedded
            path3 = os.path.join(d, "invariants", src)

            for p in [path1, path3, path2]:
                if os.path.isfile(p):
                    with open(p, "r") as f:
                        inv_data[src] = json.load(f)
                    break

        runs.append({
            "dir": d,
            "name": name,
            "D": float(D_val),
            "A": float(A_val),
            "Nm": int(Nm_val),
            "metadata": meta,
            "inv_data": inv_data,
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
# Invariant vector construction
# ---------------------------------------------------------------------------
def _flatten_json(obj, prefix: str = "") -> list[tuple[str, float]]:
    """Recursively flatten a JSON object into (key, value) pairs.

    Only extracts numeric leaves; skips strings, booleans, lists of
    non-numeric items, and nested structures deeper than 4 levels.
    """
    items = []

    if isinstance(obj, dict):
        for k, v in obj.items():
            new_key = f"{prefix}.{k}" if prefix else k
            items.extend(_flatten_json(v, new_key))

    elif isinstance(obj, (list, tuple)):
        for i, v in enumerate(obj):
            new_key = f"{prefix}[{i}]"
            if isinstance(v, (int, float)) and not isinstance(v, bool):
                if np.isfinite(v):
                    items.append((new_key, float(v)))
            elif isinstance(v, dict):
                items.extend(_flatten_json(v, new_key))

    elif isinstance(obj, (int, float)) and not isinstance(obj, bool):
        if np.isfinite(obj):
            items.append((prefix, float(obj)))

    return items


def build_invariant_vector(run: dict) -> tuple:
    """Construct a unified invariant vector from all loaded JSON summaries.

    Returns (keys, values) where keys is a list of string labels and
    values is a 1-D numpy array.
    """
    all_items = []

    for src, data in run["inv_data"].items():
        prefix = src.replace(".json", "").replace("invariant_", "")
        items = _flatten_json(data, prefix)
        all_items.extend(items)

    if not all_items:
        return [], np.array([])

    keys = [item[0] for item in all_items]
    values = np.array([item[1] for item in all_items])

    return keys, values


def align_vectors(runs: list[dict]) -> tuple:
    """Build aligned invariant matrices from all runs.

    Returns:
        all_keys: list of all unique keys across all runs
        matrix: ndarray of shape (n_runs, n_keys), NaN where missing
        key_counts: dict mapping key -> number of runs that have it
    """
    # Collect all key sets
    run_vectors = []
    for run in runs:
        keys, values = build_invariant_vector(run)
        run_vectors.append((keys, values))

    # Union of all keys (preserving order of first appearance)
    all_keys = []
    key_set = set()
    for keys, _ in run_vectors:
        for k in keys:
            if k not in key_set:
                all_keys.append(k)
                key_set.add(k)

    n_runs = len(runs)
    n_keys = len(all_keys)
    key_to_idx = {k: i for i, k in enumerate(all_keys)}

    matrix = np.full((n_runs, n_keys), np.nan)
    key_counts = {k: 0 for k in all_keys}

    for run_idx, (keys, values) in enumerate(run_vectors):
        for k, v in zip(keys, values):
            col = key_to_idx[k]
            matrix[run_idx, col] = v
            key_counts[k] += 1

    return all_keys, matrix, key_counts


def standardize_matrix(matrix: np.ndarray) -> np.ndarray:
    """Z-score each column, handling NaN robustly.

    Columns with zero variance or all-NaN are set to 0.
    """
    n_runs, n_keys = matrix.shape
    Z = np.full_like(matrix, 0.0)

    for j in range(n_keys):
        col = matrix[:, j]
        valid = ~np.isnan(col)
        if np.sum(valid) < 2:
            continue
        mean_j = np.nanmean(col)
        std_j = np.nanstd(col)
        if std_j < 1e-30:
            continue
        Z[:, j] = np.where(valid, (col - mean_j) / std_j, 0.0)

    return Z


# ---------------------------------------------------------------------------
# Distance and clustering
# ---------------------------------------------------------------------------
def compute_distance_matrix(Z: np.ndarray) -> np.ndarray:
    """Pairwise Euclidean distance, treating NaN-zeroed columns correctly."""
    n = Z.shape[0]
    D = np.zeros((n, n))
    for i in range(n):
        for j in range(i + 1, n):
            diff = Z[i] - Z[j]
            d = np.sqrt(np.sum(diff ** 2))
            D[i, j] = d
            D[j, i] = d
    return D


def universality_score(dist_matrix: np.ndarray) -> float:
    """U = 1 / (1 + CV(upper-triangle distances))."""
    n = dist_matrix.shape[0]
    if n < 2:
        return 1.0
    upper = dist_matrix[np.triu_indices(n, k=1)]
    if len(upper) == 0:
        return 1.0
    mean_d = np.mean(upper)
    std_d = np.std(upper)
    cv = std_d / max(mean_d, 1e-30)
    return 1.0 / (1.0 + cv)


def per_run_universality(dist_matrix: np.ndarray) -> np.ndarray:
    """Mean distance from each run to all others."""
    n = dist_matrix.shape[0]
    means = np.zeros(n)
    for i in range(n):
        others = np.concatenate([dist_matrix[i, :i], dist_matrix[i, i+1:]])
        means[i] = np.mean(others) if len(others) > 0 else 0.0
    return means


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
# Figure A: Distance Matrix Heatmap
# ---------------------------------------------------------------------------
def figure_distance_matrix(runs: list[dict], dist_matrix: np.ndarray,
                           order: np.ndarray | None):
    """Heatmap of pairwise distances with clustered ordering."""
    n = len(runs)

    if order is not None:
        D_ord = dist_matrix[np.ix_(order, order)]
        labels = [runs[i]["name"][:20] for i in order]
    else:
        D_ord = dist_matrix
        labels = [r["name"][:20] for r in runs]

    upper = dist_matrix[np.triu_indices(n, k=1)]
    mean_d = np.mean(upper) if len(upper) > 0 else 0
    min_d = np.min(upper) if len(upper) > 0 else 0
    max_d = np.max(upper) if len(upper) > 0 else 0

    fig, ax = plt.subplots(figsize=(10, 9))

    im = ax.imshow(D_ord, cmap="viridis", interpolation="nearest")

    if n <= 30:
        ax.set_xticks(range(n))
        ax.set_xticklabels(labels, fontsize=5, rotation=90)
        ax.set_yticks(range(n))
        ax.set_yticklabels(labels, fontsize=5)

    cbar = fig.colorbar(im, ax=ax, label="Euclidean distance", pad=0.02,
                        shrink=0.85)
    cbar.ax.tick_params(labelsize=9)

    ax.annotate(
        (f"mean = {mean_d:.2f}\n"
         f"min = {min_d:.2f}\n"
         f"max = {max_d:.2f}"),
        xy=(0.02, 0.98), xycoords="axes fraction",
        fontsize=9, va="top",
        bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8),
    )

    setup_axes(ax, "Run", "Run",
               f"Pairwise Invariant Distance ({n} runs)")
    fig.tight_layout()

    fname = "distance_matrix.png"
    fig.savefig(os.path.join(FIG_DIR, fname), dpi=300)
    plt.close(fig)
    print(f"  Saved: {fname}")


# ---------------------------------------------------------------------------
# Figure B: Dendrogram
# ---------------------------------------------------------------------------
def figure_dendrogram(runs: list[dict], Z_linkage: np.ndarray | None):
    """Hierarchical clustering dendrogram."""
    if Z_linkage is None:
        print("  SKIP dendrogram: scipy not available or insufficient data.")
        return

    n = len(runs)
    labels = [f"D={r['D']:.2f}" for r in runs]

    # Colour leaves by D
    D_vals = np.array([r["D"] for r in runs])
    D_norm = mcolors.Normalize(vmin=D_vals.min() * 0.9,
                                vmax=D_vals.max() * 1.1)
    D_cmap = plt.cm.plasma

    fig, ax = plt.subplots(figsize=(max(12, n * 0.3), 6))

    dend = dendrogram(
        Z_linkage,
        labels=labels if n <= 40 else None,
        ax=ax,
        leaf_rotation=90,
        leaf_font_size=6 if n <= 40 else 4,
        color_threshold=0,
        above_threshold_color="0.5",
    )

    # Number of clusters at threshold
    if n >= 2:
        max_dist = Z_linkage[-1, 2]
        thresh = DISSIMILARITY_THRESH * max_dist
        clusters = fcluster(Z_linkage, t=thresh, criterion="distance")
        n_clusters = len(set(clusters))

        ax.axhline(thresh, color="#b2182b", linestyle="--", linewidth=1.0,
                   label=f"{DISSIMILARITY_THRESH:.0%} threshold → "
                         f"{n_clusters} cluster(s)")
        ax.legend(fontsize=9, loc="upper right", framealpha=0.9)

    setup_axes(ax, "Run", "Distance",
               f"Invariant Dendrogram ({n} runs)")
    fig.tight_layout()

    fname = "dendrogram.png"
    fig.savefig(os.path.join(FIG_DIR, fname), dpi=300)
    plt.close(fig)
    print(f"  Saved: {fname}")


# ---------------------------------------------------------------------------
# Figure C: Universality Scatter
# ---------------------------------------------------------------------------
def figure_universality_scatter(runs: list[dict],
                                 mean_dists: np.ndarray,
                                 U_global: float):
    """Scatter of per-run mean distance vs D, colored by A."""
    A_vals = sorted(set(r["A"] for r in runs))

    A_cmap = plt.cm.viridis
    A_norm = mcolors.Normalize(
        vmin=min(A_vals) * 0.8 if A_vals else 0,
        vmax=max(A_vals) * 1.2 if A_vals else 1,
    )

    fig, ax = plt.subplots(figsize=(10, 6))

    for i, run in enumerate(runs):
        color = A_cmap(A_norm(run["A"]))
        ax.scatter(
            run["D"], mean_dists[i],
            color=color, s=60, alpha=0.7,
            edgecolors="0.3", linewidths=0.4,
        )

    # Global mean
    global_mean = np.mean(mean_dists)
    ax.axhline(global_mean, color="0.4", linestyle="--", linewidth=1.0,
               alpha=0.6)

    ax.annotate(
        (f"Global $U = {U_global:.4f}$\n"
         f"mean dist = {global_mean:.2f}"),
        xy=(0.02, 0.95), xycoords="axes fraction",
        fontsize=10, va="top",
        bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8),
    )

    # Verdict
    if U_global > 0.9:
        verdict = "UNIVERSAL"
        v_color = "#1b7837"
    elif U_global > 0.75:
        verdict = "WEAKLY UNIVERSAL"
        v_color = "#e6ab02"
    else:
        verdict = "NOT UNIVERSAL"
        v_color = "#b2182b"

    ax.annotate(
        verdict,
        xy=(0.98, 0.95), xycoords="axes fraction",
        fontsize=12, fontweight="bold", ha="right", va="top",
        color=v_color,
        bbox=dict(boxstyle="round,pad=0.4", facecolor="white", alpha=0.8),
    )

    # Colorbar
    sm = plt.cm.ScalarMappable(cmap=A_cmap, norm=A_norm)
    sm.set_array([])
    cbar = fig.colorbar(sm, ax=ax, label=r"Amplitude $A$", pad=0.02)
    cbar.ax.tick_params(labelsize=9)

    setup_axes(
        ax,
        xlabel=r"Diffusion $D$",
        ylabel="Mean distance to other runs",
        title="Parameter Universality — All Admissible Runs",
    )
    fig.tight_layout()

    fname = "universality_scatter.png"
    fig.savefig(os.path.join(FIG_DIR, fname), dpi=300)
    plt.close(fig)
    print(f"  Saved: {fname}")


# ---------------------------------------------------------------------------
# Summary table
# ---------------------------------------------------------------------------
def print_summary(runs: list[dict], mean_dists: np.ndarray,
                  all_keys: list[str], key_counts: dict,
                  dist_matrix: np.ndarray, U_global: float):
    n = len(runs)
    n_keys = len(all_keys)

    print(f"\n{'='*100}")
    print("  Parameter Universality — Summary")
    print(f"{'='*100}")

    print(f"\n  Invariant vector: {n_keys} components from "
          f"{sum(1 for s in INVARIANT_SOURCES if any(s in r['inv_data'] for r in runs))} "
          f"source files")

    # Key coverage
    full_keys = sum(1 for k, c in key_counts.items() if c == n)
    partial_keys = sum(1 for k, c in key_counts.items() if 0 < c < n)
    print(f"  Key coverage: {full_keys} full ({n}/{n} runs), "
          f"{partial_keys} partial, {n_keys} total")

    # Per-run table
    print(f"\n  {'D':<7} {'A':<7} {'Nm':<5} {'#inv':<6} "
          f"{'mean_dist':<12} {'U_run':<10}")
    print("  " + "-" * 55)

    for i, run in enumerate(runs):
        n_inv = sum(1 for s in INVARIANT_SOURCES if s in run["inv_data"])
        U_run = 1.0 / (1.0 + mean_dists[i] / max(np.mean(mean_dists), 1e-30))

        print(f"  {run['D']:<7.3f} {run['A']:<7.4f} {run['Nm']:<5d} "
              f"{n_inv:<6d} "
              f"{mean_dists[i]:<12.4f} {U_run:<10.4f}")

    # Global diagnostics
    upper = dist_matrix[np.triu_indices(n, k=1)]
    mean_d = np.mean(upper) if len(upper) > 0 else 0
    std_d = np.std(upper) if len(upper) > 0 else 0
    cv_d = std_d / max(mean_d, 1e-30)

    print(f"\n  Pairwise distance statistics ({len(upper)} pairs):")
    print(f"    Mean:   {mean_d:.4f}")
    print(f"    Std:    {std_d:.4f}")
    print(f"    Min:    {np.min(upper):.4f}" if len(upper) > 0 else "    Min:    —")
    print(f"    Max:    {np.max(upper):.4f}" if len(upper) > 0 else "    Max:    —")
    print(f"    CV:     {cv_d:.4f}")

    print(f"\n  Universality Score: U = {U_global:.4f}")
    if U_global > 0.9:
        print(f"    Verdict: UNIVERSAL (U > 0.9)")
    elif U_global > 0.75:
        print(f"    Verdict: WEAKLY UNIVERSAL (U > 0.75)")
    else:
        print(f"    Verdict: NOT UNIVERSAL (U ≤ 0.75)")

    # Clustering summary (if scipy available)
    if HAS_SCIPY and n >= 2:
        condensed = pdist(dist_matrix)
        # Use precomputed distances — need to convert dist_matrix to condensed
        condensed = squareform(dist_matrix)
        Z_link = linkage(condensed, method="ward")
        max_dist = Z_link[-1, 2]
        thresh = DISSIMILARITY_THRESH * max_dist
        clusters = fcluster(Z_link, t=thresh, criterion="distance")
        n_clusters = len(set(clusters))

        print(f"\n  Hierarchical clustering (Ward, {DISSIMILARITY_THRESH:.0%} threshold):")
        print(f"    Number of clusters: {n_clusters}")
        if n_clusters == 1:
            print(f"    All runs in a single cluster — CONSISTENT with universality")
        else:
            print(f"    Multiple clusters — check if they correspond to parameter regions")


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

    # Count invariant coverage
    total_inv = sum(len(r["inv_data"]) for r in runs)
    print(f"  Found {len(runs)} runs, {total_inv} invariant files loaded "
          f"({total_inv / max(len(runs), 1):.1f} per run)")

    if total_inv == 0:
        print("\n  WARNING: No invariant JSON files found.")
        print("  Run the invariant analysis scripts first:")
        for src in INVARIANT_SOURCES:
            name = src.replace(".json", "").replace("invariant_", "")
            print(f"    python experiments/invariant_{name}.py")
        print("\n  Each script should save a JSON summary in the run directory.")
        print("  Proceeding with empty vectors (figures will be trivial)...")

    # Build aligned invariant matrix
    print("\nConstructing invariant vectors...")
    all_keys, matrix, key_counts = align_vectors(runs)
    print(f"  Vector dimension: {len(all_keys)} components")
    print(f"  Matrix shape: {matrix.shape}")

    # Standardize
    Z = standardize_matrix(matrix)

    # Distance matrix
    print("\nComputing distance matrix...")
    dist_matrix = compute_distance_matrix(Z)

    # Universality score
    U_global = universality_score(dist_matrix)
    mean_dists = per_run_universality(dist_matrix)

    # Clustering (if scipy available)
    Z_linkage = None
    cluster_order = None
    if HAS_SCIPY and len(runs) >= 2:
        condensed = squareform(dist_matrix)
        Z_linkage = linkage(condensed, method="ward")
        dend = dendrogram(Z_linkage, no_plot=True)
        cluster_order = np.array(dend["leaves"])

    # Figures
    print("\n--- (A) Distance Matrix ---")
    figure_distance_matrix(runs, dist_matrix, cluster_order)

    print("\n--- (B) Dendrogram ---")
    figure_dendrogram(runs, Z_linkage)

    print("\n--- (C) Universality Scatter ---")
    figure_universality_scatter(runs, mean_dists, U_global)

    # Summary
    print_summary(runs, mean_dists, all_keys, key_counts,
                  dist_matrix, U_global)

    print(f"\nAll figures saved to: {FIG_DIR}")
    print("Done.")


if __name__ == "__main__":
    main()
