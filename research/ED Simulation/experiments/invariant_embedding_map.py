# NOTE: This is a Layer 4 meta-analysis script.
# It operates on the outputs of all Layer 3 invariant scripts.
# It is NOT a core invariant and should run AFTER all Layer 3 scripts.
# In run_all.py, it belongs to PHASE_5_META, not PHASE_4_INVARIANTS.

"""
invariant_embedding_map.py
===========================
Experiment / Analysis: Invariant Embedding Map

Scans all completed regime_D*_A*_Nm* runs, loads the unified invariant
vectors (produced by invariant_parameter_universality.py), and embeds
them into 2-D using PCA, t-SNE, and optionally UMAP.

The ED architecture (Appendix D) predicts that all systems satisfying
Principles 1-7 converge to the same qualitative attractor structure.
In invariant space, this means the standardised invariant vectors
should collapse to a small cluster -- the "universality point."  The
embedding map visualises this collapse and quantifies its tightness.

Produces:
  (A) PCA Embedding -- first two principal components.
  (B) t-SNE Embedding -- nonlinear neighbourhood-preserving map.
  (C) UMAP Embedding -- topology-preserving map (if available).

All figures saved to output/figures/invariants/embedding_map/
as PNG (300 dpi).

Usage:
    python experiments/invariant_embedding_map.py

Requires: numpy, matplotlib, scikit-learn.
Optional: umap-learn (for UMAP embedding).
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

# Optional imports -- graceful fallback
try:
    from sklearn.decomposition import PCA
    from sklearn.manifold import TSNE
    from sklearn.metrics import silhouette_score
    HAS_SKLEARN = True
except ImportError:
    HAS_SKLEARN = False

try:
    import umap
    HAS_UMAP = True
except ImportError:
    HAS_UMAP = False

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SIM_DIR = os.path.dirname(SCRIPT_DIR)
RUNS_DIR = os.path.join(SIM_DIR, "output", "runs")
INV_DIR = os.path.join(SIM_DIR, "output", "figures", "invariants")
FIG_DIR = os.path.join(SIM_DIR, "output", "figures", "invariants",
                        "embedding_map")

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
PCA_PRE_DIM = 20         # PCA dimensionality before nonlinear embedding
TSNE_PERPLEXITY_FRAC = 3 # perplexity = n_runs / this
TSNE_LR = 200
RANDOM_STATE = 0

# Invariant source files (same as parameter_universality.py)
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


# ---------------------------------------------------------------------------
# Discovery and vector loading
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

        # Load invariant JSONs
        inv_data = {}
        for src in INVARIANT_SOURCES:
            for p in [os.path.join(d, src),
                      os.path.join(d, "invariants", src),
                      os.path.join(INV_DIR, src)]:
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


def build_invariant_matrix(runs: list[dict]) -> tuple:
    """Build aligned, standardized invariant matrix.

    Returns (X_std, all_keys) where X_std is (n_runs, n_keys).
    """
    n_runs = len(runs)

    # Collect all keys
    all_keys_set = set()
    all_keys_ordered = []
    run_dicts = []

    for run in runs:
        flat = {}
        for src, data in run["inv_data"].items():
            prefix = src.replace(".json", "").replace("invariant_", "")
            for k, v in _flatten_json(data, prefix):
                flat[k] = v
                if k not in all_keys_set:
                    all_keys_ordered.append(k)
                    all_keys_set.add(k)
        run_dicts.append(flat)

    n_keys = len(all_keys_ordered)
    key_to_idx = {k: i for i, k in enumerate(all_keys_ordered)}

    # Build matrix
    X = np.full((n_runs, n_keys), np.nan)
    for i, flat in enumerate(run_dicts):
        for k, v in flat.items():
            X[i, key_to_idx[k]] = v

    # Impute NaN with column means
    for j in range(n_keys):
        col = X[:, j]
        mask = np.isnan(col)
        if np.all(mask):
            X[:, j] = 0.0
        elif np.any(mask):
            X[mask, j] = np.nanmean(col)

    # Standardize
    means = np.mean(X, axis=0)
    stds = np.std(X, axis=0)
    stds[stds < 1e-30] = 1.0
    X_std = (X - means) / stds

    return X_std, all_keys_ordered


# ---------------------------------------------------------------------------
# Embedding computations
# ---------------------------------------------------------------------------
def compute_pca_embedding(X: np.ndarray) -> tuple:
    """PCA to 2-D. Returns (coords, explained_variance_ratio)."""
    if not HAS_SKLEARN:
        # Manual PCA fallback
        cov = np.cov(X, rowvar=False)
        eigvals, eigvecs = np.linalg.eigh(cov)
        order = eigvals.argsort()[::-1]
        eigvals = eigvals[order]
        eigvecs = eigvecs[:, order]
        coords = X @ eigvecs[:, :2]
        total = np.sum(np.maximum(eigvals, 0))
        evr = eigvals[:2] / max(total, 1e-30)
        return coords, evr

    pca = PCA(n_components=min(2, X.shape[1]), random_state=RANDOM_STATE)
    coords = pca.fit_transform(X)
    return coords, pca.explained_variance_ratio_


def compute_tsne_embedding(X: np.ndarray) -> np.ndarray | None:
    """t-SNE to 2-D. Returns coords or None if unavailable."""
    if not HAS_SKLEARN:
        return None

    n = X.shape[0]
    if n < 5:
        return None

    perplexity = min(30, max(2, n // TSNE_PERPLEXITY_FRAC))

    # Pre-reduce with PCA if high-dimensional
    if X.shape[1] > PCA_PRE_DIM:
        pca = PCA(n_components=PCA_PRE_DIM, random_state=RANDOM_STATE)
        X_pre = pca.fit_transform(X)
    else:
        X_pre = X

    tsne = TSNE(n_components=2, perplexity=perplexity,
                learning_rate=TSNE_LR, random_state=RANDOM_STATE,
                init="pca")
    return tsne.fit_transform(X_pre)


def compute_umap_embedding(X: np.ndarray) -> np.ndarray | None:
    """UMAP to 2-D. Returns coords or None if unavailable."""
    if not HAS_UMAP:
        return None

    n = X.shape[0]
    if n < 5:
        return None

    # Pre-reduce with PCA
    if HAS_SKLEARN and X.shape[1] > PCA_PRE_DIM:
        pca = PCA(n_components=PCA_PRE_DIM, random_state=RANDOM_STATE)
        X_pre = pca.fit_transform(X)
    else:
        X_pre = X

    n_neighbors = min(15, n - 1)
    reducer = umap.UMAP(n_components=2, n_neighbors=n_neighbors,
                        min_dist=0.1, metric="euclidean",
                        random_state=RANDOM_STATE)
    return reducer.fit_transform(X_pre)


# ---------------------------------------------------------------------------
# Diagnostics
# ---------------------------------------------------------------------------
def cluster_radius(coords: np.ndarray) -> float:
    """Mean distance to centroid."""
    centroid = np.mean(coords, axis=0)
    dists = np.sqrt(np.sum((coords - centroid) ** 2, axis=1))
    return float(np.mean(dists))


def cluster_diameter(coords: np.ndarray) -> float:
    """Max pairwise distance."""
    n = coords.shape[0]
    if n < 2:
        return 0.0
    max_d = 0.0
    for i in range(n):
        for j in range(i + 1, n):
            d = np.sqrt(np.sum((coords[i] - coords[j]) ** 2))
            if d > max_d:
                max_d = d
    return float(max_d)


def pairwise_distances_flat(coords: np.ndarray) -> np.ndarray:
    """Upper-triangle pairwise distances."""
    n = coords.shape[0]
    dists = []
    for i in range(n):
        for j in range(i + 1, n):
            dists.append(np.sqrt(np.sum((coords[i] - coords[j]) ** 2)))
    return np.array(dists)


def embedding_consistency(coords_a: np.ndarray,
                          coords_b: np.ndarray) -> float:
    """Correlation between pairwise distance vectors of two embeddings."""
    da = pairwise_distances_flat(coords_a)
    db = pairwise_distances_flat(coords_b)
    if len(da) < 3:
        return 0.0
    sa = np.std(da)
    sb = np.std(db)
    if sa < 1e-30 or sb < 1e-30:
        return 0.0
    return float(np.corrcoef(da, db)[0, 1])


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
# Figure A: PCA Embedding
# ---------------------------------------------------------------------------
def figure_pca(runs: list[dict], coords: np.ndarray, evr: np.ndarray):
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

    fig, ax = plt.subplots(figsize=(10, 8))

    for i, run in enumerate(runs):
        color = D_cmap(D_norm(run["D"]))
        marker = Nm_markers.get(run["Nm"], "o")
        ax.scatter(coords[i, 0], coords[i, 1],
                   color=color, marker=marker, s=60, alpha=0.7,
                   edgecolors="0.3", linewidths=0.4)

    # Centroid
    centroid = np.mean(coords, axis=0)
    rad = cluster_radius(coords)
    ax.plot(centroid[0], centroid[1], "k+", markersize=16,
            markeredgewidth=2.5, zorder=10, label="Centroid")
    circle = plt.Circle(centroid, rad, fill=False, color="0.4",
                        linestyle="--", linewidth=1.2, alpha=0.6,
                        label=f"Radius = {rad:.3f}")
    ax.add_patch(circle)

    ax.annotate(
        f"PC1: {evr[0]:.1%}, PC2: {evr[1]:.1%}\nradius = {rad:.3f}",
        xy=(0.02, 0.05), xycoords="axes fraction", fontsize=9,
        bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.7),
    )

    # Colorbar
    sm = plt.cm.ScalarMappable(cmap=D_cmap, norm=D_norm)
    sm.set_array([])
    fig.colorbar(sm, ax=ax, label=r"Diffusion $D$", pad=0.02)

    legend_handles = [
        plt.Line2D([0], [0], marker=m, color="0.5", markersize=7,
                   linestyle="None", label=rf"$N_m = {Nm}$")
        for Nm, m in Nm_markers.items()
    ]
    legend_handles.extend(ax.get_legend_handles_labels()[0])
    ax.legend(handles=legend_handles, fontsize=8, loc="upper right",
              framealpha=0.9)

    setup_axes(ax, "PC1", "PC2", "PCA Embedding of Invariant Vectors")
    fig.tight_layout()

    fig.savefig(os.path.join(FIG_DIR, "pca_embedding.png"), dpi=300)
    plt.close(fig)
    print("  Saved: pca_embedding.png")


# ---------------------------------------------------------------------------
# Figure B: t-SNE Embedding
# ---------------------------------------------------------------------------
def figure_tsne(runs: list[dict], coords: np.ndarray):
    A_vals = sorted(set(r["A"] for r in runs))

    A_cmap = plt.cm.viridis
    A_norm = mcolors.Normalize(
        vmin=min(A_vals) * 0.8 if A_vals else 0,
        vmax=max(A_vals) * 1.2 if A_vals else 1,
    )

    fig, ax = plt.subplots(figsize=(10, 8))

    for i, run in enumerate(runs):
        color = A_cmap(A_norm(run["A"]))
        ax.scatter(coords[i, 0], coords[i, 1],
                   color=color, s=60, alpha=0.7,
                   edgecolors="0.3", linewidths=0.4)

    diam = cluster_diameter(coords)
    ax.annotate(
        f"Cluster diameter = {diam:.3f}",
        xy=(0.02, 0.05), xycoords="axes fraction", fontsize=9,
        bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.7),
    )

    sm = plt.cm.ScalarMappable(cmap=A_cmap, norm=A_norm)
    sm.set_array([])
    fig.colorbar(sm, ax=ax, label=r"Amplitude $A$", pad=0.02)

    setup_axes(ax, "t-SNE 1", "t-SNE 2",
               "t-SNE Embedding of Invariant Vectors")
    fig.tight_layout()

    fig.savefig(os.path.join(FIG_DIR, "tsne_embedding.png"), dpi=300)
    plt.close(fig)
    print("  Saved: tsne_embedding.png")


# ---------------------------------------------------------------------------
# Figure C: UMAP Embedding
# ---------------------------------------------------------------------------
def figure_umap(runs: list[dict], coords: np.ndarray, C_emb: float):
    Nm_vals = sorted(set(r["Nm"] for r in runs))

    Nm_cmap = plt.cm.Set1
    Nm_norm = mcolors.Normalize(
        vmin=min(Nm_vals) - 1 if Nm_vals else 0,
        vmax=max(Nm_vals) + 1 if Nm_vals else 1,
    )

    fig, ax = plt.subplots(figsize=(10, 8))

    for i, run in enumerate(runs):
        color = Nm_cmap(Nm_norm(run["Nm"]))
        ax.scatter(coords[i, 0], coords[i, 1],
                   color=color, s=60, alpha=0.7,
                   edgecolors="0.3", linewidths=0.4)

    ax.annotate(
        f"Embedding consistency $C_{{emb}} = {C_emb:.4f}$",
        xy=(0.02, 0.05), xycoords="axes fraction", fontsize=9,
        bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.7),
    )

    sm = plt.cm.ScalarMappable(cmap=Nm_cmap, norm=Nm_norm)
    sm.set_array([])
    fig.colorbar(sm, ax=ax, label=r"Seed count $N_m$", pad=0.02)

    setup_axes(ax, "UMAP 1", "UMAP 2",
               "UMAP Embedding of Invariant Vectors")
    fig.tight_layout()

    fig.savefig(os.path.join(FIG_DIR, "umap_embedding.png"), dpi=300)
    plt.close(fig)
    print("  Saved: umap_embedding.png")


# ---------------------------------------------------------------------------
# Summary
# ---------------------------------------------------------------------------
def print_summary(runs: list[dict],
                  pca_coords: np.ndarray, evr: np.ndarray,
                  tsne_coords: np.ndarray | None,
                  umap_coords: np.ndarray | None,
                  C_emb: float):
    n = len(runs)

    print(f"\n{'='*120}")
    print("  Invariant Embedding Map -- Summary")
    print(f"{'='*120}")

    # Per-run coordinates
    print(f"\n  {'D':<7} {'A':<7} {'Nm':<5} "
          f"{'PCA_x':<10} {'PCA_y':<10} ", end="")
    if tsne_coords is not None:
        print(f"{'tSNE_x':<10} {'tSNE_y':<10} ", end="")
    if umap_coords is not None:
        print(f"{'UMAP_x':<10} {'UMAP_y':<10}", end="")
    print()
    print("  " + "-" * 80)

    for i, run in enumerate(runs):
        print(f"  {run['D']:<7.3f} {run['A']:<7.4f} {run['Nm']:<5d} "
              f"{pca_coords[i,0]:<10.4f} {pca_coords[i,1]:<10.4f} ",
              end="")
        if tsne_coords is not None:
            print(f"{tsne_coords[i,0]:<10.4f} {tsne_coords[i,1]:<10.4f} ",
                  end="")
        if umap_coords is not None:
            print(f"{umap_coords[i,0]:<10.4f} {umap_coords[i,1]:<10.4f}",
                  end="")
        print()

    # Global diagnostics
    rad_pca = cluster_radius(pca_coords)
    diam_pca = cluster_diameter(pca_coords)

    print(f"\n  PCA diagnostics:")
    print(f"    Explained variance: PC1={evr[0]:.1%}, PC2={evr[1]:.1%}")
    print(f"    Cluster radius:   {rad_pca:.4f}")
    print(f"    Cluster diameter: {diam_pca:.4f}")

    if tsne_coords is not None:
        rad_tsne = cluster_radius(tsne_coords)
        diam_tsne = cluster_diameter(tsne_coords)
        print(f"\n  t-SNE diagnostics:")
        print(f"    Cluster radius:   {rad_tsne:.4f}")
        print(f"    Cluster diameter: {diam_tsne:.4f}")

    if umap_coords is not None:
        rad_umap = cluster_radius(umap_coords)
        diam_umap = cluster_diameter(umap_coords)
        print(f"\n  UMAP diagnostics:")
        print(f"    Cluster radius:   {rad_umap:.4f}")
        print(f"    Cluster diameter: {diam_umap:.4f}")

    print(f"\n  Embedding consistency C_emb = {C_emb:.4f}")

    # Verdict based on PCA cluster radius (standardised space)
    if rad_pca < 0.1:
        verdict = "COLLAPSED (universal)"
    elif rad_pca < 0.3:
        verdict = "WEAKLY COLLAPSED"
    else:
        verdict = "NOT COLLAPSED"

    print(f"  Verdict (PCA radius): {verdict}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    os.makedirs(FIG_DIR, exist_ok=True)

    print("Discovering regime volume runs and invariant vectors...")
    runs = discover_regime_runs()

    if not runs:
        print(f"\nERROR: No admissible runs found in {RUNS_DIR}")
        sys.exit(1)

    total_inv = sum(len(r["inv_data"]) for r in runs)
    print(f"  Found {len(runs)} runs, {total_inv} invariant files")

    # Build matrix
    print("\nBuilding invariant matrix...")
    X_std, all_keys = build_invariant_matrix(runs)
    print(f"  Shape: {X_std.shape} ({X_std.shape[1]} components)")

    if X_std.shape[0] < 3:
        print("\n  ERROR: Need at least 3 runs for embedding.")
        sys.exit(1)

    # PCA embedding
    print("\nComputing PCA embedding...")
    pca_coords, evr = compute_pca_embedding(X_std)

    # t-SNE embedding
    print("Computing t-SNE embedding...")
    tsne_coords = compute_tsne_embedding(X_std)
    if tsne_coords is None:
        print("  SKIP: scikit-learn not available or too few runs.")

    # UMAP embedding
    print("Computing UMAP embedding...")
    umap_coords = compute_umap_embedding(X_std)
    if umap_coords is None:
        print("  SKIP: umap-learn not available or too few runs.")

    # Embedding consistency
    C_emb = 0.0
    if umap_coords is not None:
        C_emb = embedding_consistency(pca_coords, umap_coords)
    elif tsne_coords is not None:
        C_emb = embedding_consistency(pca_coords, tsne_coords)

    # Figures
    print("\n--- (A) PCA Embedding ---")
    figure_pca(runs, pca_coords, evr)

    if tsne_coords is not None:
        print("\n--- (B) t-SNE Embedding ---")
        figure_tsne(runs, tsne_coords)

    if umap_coords is not None:
        print("\n--- (C) UMAP Embedding ---")
        figure_umap(runs, umap_coords, C_emb)

    # Summary
    print_summary(runs, pca_coords, evr, tsne_coords, umap_coords, C_emb)

    print(f"\nAll figures saved to: {FIG_DIR}")
    print("Done.")


if __name__ == "__main__":
    main()
