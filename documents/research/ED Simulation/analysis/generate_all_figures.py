"""
generate_all_figures.py
========================
Unified figure-generation pipeline for ED-SIM v1.

Loads all completed runs from output/runs/, extracts time-series data,
metadata, invariants, and regime classifications, and generates every
publication figure for the ED monograph.

Outputs saved to output/figures/ as 300 dpi PNGs.

Usage:
    python analysis/generate_all_figures.py

Requires: numpy, matplotlib.
Optional: scikit-learn (PCA embedding), umap-learn (UMAP embedding).
"""

import os
import sys
import json
import glob
import re
import warnings
from dataclasses import dataclass, field
from typing import Optional

import numpy as np

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.collections import LineCollection
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SIM_DIR = os.path.dirname(SCRIPT_DIR)
RUNS_DIR = os.path.join(SIM_DIR, "output", "runs")
FIG_DIR = os.path.join(SIM_DIR, "output", "figures")

# ---------------------------------------------------------------------------
# Global style
# ---------------------------------------------------------------------------
STYLE = {
    "dpi": 300,
    "figsize_single": (8, 6),
    "figsize_wide": (12, 6),
    "figsize_tall": (8, 10),
    "figsize_square": (7, 7),
    "font_title": 13,
    "font_label": 11,
    "font_tick": 10,
    "font_legend": 9,
    "grid_alpha": 0.3,
    "grid_lw": 0.5,
    "line_lw": 1.5,
    "marker_s": 30,
}

# Regime colors
REGIME_COLORS = {
    "underdamped": "#2166ac",
    "oscillatory": "#2166ac",
    "overdamped": "#b2182b",
    "monotonic": "#b2182b",
    "critical": "#1b7837",
    "inadmissible": "#999999",
}

# Parameter colormaps
D_CMAP = plt.cm.plasma
A_CMAP = plt.cm.viridis
NM_MARKERS = {5: "o", 10: "s", 20: "^", 30: "D"}


# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------
@dataclass
class Run:
    """Container for a single simulation run."""
    name: str
    directory: str
    D: Optional[float] = None
    A: Optional[float] = None
    Nm: Optional[int] = None
    regime: str = "unknown"
    metadata: dict = field(default_factory=dict)
    invariants: dict = field(default_factory=dict)
    t: Optional[np.ndarray] = None
    E_total: Optional[np.ndarray] = None
    C_ED: Optional[np.ndarray] = None
    D_grad: Optional[np.ndarray] = None
    D_pen: Optional[np.ndarray] = None
    D_part: Optional[np.ndarray] = None
    D_total: Optional[np.ndarray] = None
    modal: Optional[np.ndarray] = None
    v: Optional[np.ndarray] = None
    margin: Optional[np.ndarray] = None

    @property
    def admissible(self) -> bool:
        return self.regime not in ("inadmissible", "unknown", "")

    @property
    def has_modal(self) -> bool:
        return self.modal is not None and self.modal.ndim == 2

    @property
    def has_energy(self) -> bool:
        return self.t is not None and self.E_total is not None


# ---------------------------------------------------------------------------
# Discovery and loading
# ---------------------------------------------------------------------------
def discover_runs() -> list[Run]:
    """Scan RUNS_DIR for all run directories and load their data."""
    if not os.path.isdir(RUNS_DIR):
        print(f"ERROR: runs directory not found: {RUNS_DIR}")
        return []

    runs = []
    for name in sorted(os.listdir(RUNS_DIR)):
        run_dir = os.path.join(RUNS_DIR, name)
        if not os.path.isdir(run_dir):
            continue
        ts_path = os.path.join(run_dir, "time_series.npz")
        if not os.path.isfile(ts_path):
            continue
        run = _load_run(name, run_dir)
        if run is not None:
            runs.append(run)

    return runs


def _load_run(name: str, run_dir: str) -> Optional[Run]:
    """Load a single run from its directory."""
    run = Run(name=name, directory=run_dir)

    # --- Metadata ---
    meta_path = os.path.join(run_dir, "metadata.json")
    if os.path.isfile(meta_path):
        try:
            with open(meta_path, "r") as f:
                run.metadata = json.load(f)
        except (json.JSONDecodeError, IOError):
            pass

    # Extract parameters
    run.D = run.metadata.get("D")
    run.A = run.metadata.get("A") or run.metadata.get("A_per_mode")
    run.Nm = run.metadata.get("Nm") or run.metadata.get("n_seeded") \
        or run.metadata.get("N_modes_seeded")

    # Fallback: parse from directory name (handles "0p05" → 0.05)
    if run.D is None:
        m = re.search(r"D([\d.peE+-]+)", name)
        if m:
            try:
                run.D = float(m.group(1).replace("p", "."))
            except ValueError:
                pass
    if run.A is None:
        m = re.search(r"A([\d.peE+-]+)", name)
        if m:
            try:
                run.A = float(m.group(1).replace("p", "."))
            except ValueError:
                pass
    if run.Nm is None:
        m = re.search(r"Nm(\d+)", name)
        if m:
            try:
                run.Nm = int(m.group(1))
            except ValueError:
                pass

    # --- Regime ---
    # Priority: inadmissible flag → effective_regime → regime → regime.txt
    if run.metadata.get("inadmissible") is True:
        run.regime = "inadmissible"
    elif "effective_regime" in run.metadata:
        run.regime = str(run.metadata["effective_regime"]).lower()
    elif "linear_regime" in run.metadata:
        run.regime = str(run.metadata["linear_regime"]).lower()
    elif "regime" in run.metadata:
        run.regime = str(run.metadata["regime"]).lower()
    else:
        regime_path = os.path.join(run_dir, "regime.txt")
        if os.path.isfile(regime_path):
            try:
                with open(regime_path, "r") as f:
                    run.regime = f.read().strip().lower()
            except IOError:
                pass

    # --- Invariants ---
    inv_path = os.path.join(run_dir, "invariants.json")
    if os.path.isfile(inv_path):
        try:
            with open(inv_path, "r") as f:
                run.invariants = json.load(f)
        except (json.JSONDecodeError, IOError):
            pass

    # --- Time series ---
    ts_path = os.path.join(run_dir, "time_series.npz")
    try:
        ts = np.load(ts_path, allow_pickle=True)
        run.t = ts.get("t")
        run.E_total = ts.get("E_total")
        run.C_ED = ts.get("C_ED")

        # Use first available name (avoid numpy `or` ambiguity)
        run.D_grad = ts.get("D_gradient")
        if run.D_grad is None:
            run.D_grad = ts.get("D_grad")
        run.D_pen = ts.get("D_penalty")
        if run.D_pen is None:
            run.D_pen = ts.get("D_pen")
        run.D_part = ts.get("D_participation")
        if run.D_part is None:
            run.D_part = ts.get("D_part")

        run.D_total = ts.get("D_total")
        run.modal = ts.get("modal_amplitudes")
        run.v = ts.get("v")
        run.margin = ts.get("margin")
    except Exception as e:
        print(f"  WARNING: failed to load {ts_path}: {e}")

    return run


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def setup_axes(ax, xlabel: str, ylabel: str, title: str):
    """Apply consistent axis styling."""
    ax.set_xlabel(xlabel, fontsize=STYLE["font_label"])
    ax.set_ylabel(ylabel, fontsize=STYLE["font_label"])
    ax.set_title(title, fontsize=STYLE["font_title"], fontweight="bold")
    ax.tick_params(labelsize=STYLE["font_tick"])
    ax.grid(True, alpha=STYLE["grid_alpha"], linewidth=STYLE["grid_lw"])


def save_figure(fig, filename: str):
    """Save figure to FIG_DIR and close."""
    path = os.path.join(FIG_DIR, filename)
    fig.savefig(path, dpi=STYLE["dpi"], bbox_inches="tight")
    plt.close(fig)
    return path


def compute_shannon_entropy(modal: np.ndarray) -> np.ndarray:
    """Compute Shannon entropy H(t) from modal amplitudes."""
    E_k = np.abs(modal) ** 2
    E_total = np.sum(E_k, axis=1, keepdims=True)
    E_total = np.maximum(E_total, 1e-30)
    p_k = E_k / E_total
    p_k = np.maximum(p_k, 1e-30)
    H = -np.sum(p_k * np.log(p_k), axis=1)
    return H


def get_regime_color(regime: str) -> str:
    """Map regime string to color."""
    for key, color in REGIME_COLORS.items():
        if key in regime:
            return color
    return "#999999"


def get_nm_marker(nm: Optional[int]) -> str:
    """Map Nm to marker shape."""
    if nm is None:
        return "o"
    return NM_MARKERS.get(nm, "o")


def safe_len(runs: list[Run], attr: str) -> list[Run]:
    """Filter runs that have a non-None attribute."""
    return [r for r in runs if getattr(r, attr, None) is not None]


# ---------------------------------------------------------------------------
# Figure A: Energy-Entropy Trajectories
# ---------------------------------------------------------------------------
def figure_energy_entropy(runs: list[Run]) -> Optional[str]:
    """Parametric (E(t), H(t)) trajectories for all admissible runs."""
    valid = [r for r in runs if r.admissible and r.has_modal and r.has_energy]
    if not valid:
        print("  SKIP: no runs with energy + modal data.")
        return None

    D_vals = [r.D for r in valid if r.D is not None]
    if not D_vals:
        print("  SKIP: no D values available.")
        return None

    d_min, d_max = min(D_vals), max(D_vals)
    d_norm = mcolors.Normalize(vmin=d_min * 0.9, vmax=d_max * 1.1)

    fig, ax = plt.subplots(figsize=STYLE["figsize_single"])

    for run in valid:
        n = min(len(run.t), run.modal.shape[0], len(run.E_total))
        H = compute_shannon_entropy(run.modal[:n])
        E = run.E_total[:n]

        color = D_CMAP(d_norm(run.D)) if run.D is not None else "0.5"
        marker = get_nm_marker(run.Nm)

        # Plot trajectory as thin line with endpoint marker
        ax.plot(E, H, color=color, linewidth=0.6, alpha=0.5)
        ax.plot(E[-1], H[-1], marker=marker, color=color,
                markersize=5, markeredgewidth=0.5, markeredgecolor="black",
                zorder=5)

    sm = plt.cm.ScalarMappable(cmap=D_CMAP, norm=d_norm)
    sm.set_array([])
    cbar = fig.colorbar(sm, ax=ax, label=r"Diffusion weight $D$", pad=0.02)
    cbar.ax.tick_params(labelsize=STYLE["font_tick"] - 1)

    # Marker legend
    handles = []
    for nm, marker in NM_MARKERS.items():
        h = plt.Line2D([0], [0], marker=marker, color="0.5", markersize=6,
                        linestyle="None", label=f"$N_m = {nm}$")
        handles.append(h)
    ax.legend(handles=handles, fontsize=STYLE["font_legend"],
              loc="upper right", framealpha=0.9, title="Seed count")

    setup_axes(ax, r"Energy $\mathcal{E}(t)$",
               r"Spectral entropy $H(t)$",
               "Energy-Entropy Trajectories")
    fig.tight_layout()
    return save_figure(fig, "energy_entropy_trajectories.png")


# ---------------------------------------------------------------------------
# Figure B: Lyapunov Spectra
# ---------------------------------------------------------------------------
def figure_lyapunov_spectra(runs: list[Run]) -> Optional[str]:
    """Lyapunov exponents lambda_k vs k for all admissible runs."""
    valid = [r for r in runs if r.admissible and "lyapunov_exponents" in r.invariants]
    if not valid:
        # Fallback: try loading from separate invariant files
        valid = [r for r in runs if r.admissible]
        for run in valid:
            lyap_path = os.path.join(run.directory, "lyapunov_exponents.json")
            if os.path.isfile(lyap_path):
                try:
                    with open(lyap_path, "r") as f:
                        data = json.load(f)
                    run.invariants["lyapunov_exponents"] = data.get(
                        "exponents", data.get("lyapunov_exponents", []))
                except (json.JSONDecodeError, IOError):
                    pass
        valid = [r for r in valid if "lyapunov_exponents" in r.invariants]

    if not valid:
        print("  SKIP: no Lyapunov data available.")
        return None

    D_vals = [r.D for r in valid if r.D is not None]
    d_norm = mcolors.Normalize(
        vmin=min(D_vals) * 0.9 if D_vals else 0,
        vmax=max(D_vals) * 1.1 if D_vals else 1)

    fig, ax = plt.subplots(figsize=STYLE["figsize_single"])

    for run in valid:
        lam = np.array(run.invariants["lyapunov_exponents"], dtype=float)
        k = np.arange(1, len(lam) + 1)
        color = D_CMAP(d_norm(run.D)) if run.D is not None else "0.5"
        marker = get_nm_marker(run.Nm)
        ax.plot(k, lam, color=color, linewidth=0.8, alpha=0.6,
                marker=marker, markersize=3)

    ax.axhline(0, color="black", linewidth=0.8, linestyle="--", alpha=0.5)

    sm = plt.cm.ScalarMappable(cmap=D_CMAP, norm=d_norm)
    sm.set_array([])
    fig.colorbar(sm, ax=ax, label=r"$D$", pad=0.02)

    setup_axes(ax, r"Exponent index $k$", r"Lyapunov exponent $\lambda_k$",
               "Lyapunov Spectra")
    fig.tight_layout()
    return save_figure(fig, "lyapunov_spectra.png")


# ---------------------------------------------------------------------------
# Figure C: Regime Map (3D)
# ---------------------------------------------------------------------------
def figure_regime_volume_3d(runs: list[Run]) -> Optional[str]:
    """3D scatter of (D, A, Nm) colored by regime."""
    valid = [r for r in runs
             if r.D is not None and r.A is not None and r.Nm is not None]
    if not valid:
        print("  SKIP: no runs with (D, A, Nm).")
        return None

    fig = plt.figure(figsize=(9, 7))
    ax = fig.add_subplot(111, projection="3d")

    for run in valid:
        color = get_regime_color(run.regime)
        marker = get_nm_marker(run.Nm)
        ax.scatter(run.D, run.A, run.Nm, c=color, marker=marker,
                   s=STYLE["marker_s"], edgecolors="black", linewidths=0.3,
                   alpha=0.8)

    ax.set_xlabel(r"$D$", fontsize=STYLE["font_label"])
    ax.set_ylabel(r"$A$", fontsize=STYLE["font_label"])
    ax.set_zlabel(r"$N_m$", fontsize=STYLE["font_label"])
    ax.set_title("Regime Volume", fontsize=STYLE["font_title"],
                 fontweight="bold")

    # Legend
    handles = []
    for regime, color in REGIME_COLORS.items():
        if any(regime in r.regime for r in valid):
            h = plt.Line2D([0], [0], marker="o", color=color, markersize=7,
                            linestyle="None", label=regime.capitalize(),
                            markeredgecolor="black", markeredgewidth=0.3)
            handles.append(h)
    ax.legend(handles=handles, fontsize=STYLE["font_legend"],
              loc="upper left", framealpha=0.9)

    fig.tight_layout()
    return save_figure(fig, "regime_volume_3d.png")


# ---------------------------------------------------------------------------
# Figure D: Regime Map (2D slices)
# ---------------------------------------------------------------------------
def figure_regime_slices(runs: list[Run]) -> list[str]:
    """2D slices of the regime map at fixed Nm."""
    valid = [r for r in runs
             if r.D is not None and r.A is not None and r.Nm is not None]
    if not valid:
        print("  SKIP: no runs with (D, A, Nm) for slices.")
        return []

    nm_vals = sorted(set(r.Nm for r in valid))
    saved = []

    for nm in nm_vals:
        subset = [r for r in valid if r.Nm == nm]
        if not subset:
            continue

        fig, ax = plt.subplots(figsize=(7, 5))

        for run in subset:
            color = get_regime_color(run.regime)
            ax.scatter(run.D, run.A, c=color, s=80, edgecolors="black",
                       linewidths=0.5, zorder=5)

        # Legend
        seen = set()
        handles = []
        for run in subset:
            rkey = run.regime.split()[0] if run.regime else "unknown"
            if rkey not in seen:
                seen.add(rkey)
                h = plt.Line2D(
                    [0], [0], marker="o",
                    color=get_regime_color(run.regime),
                    markersize=8, linestyle="None",
                    label=rkey.capitalize(),
                    markeredgecolor="black", markeredgewidth=0.5)
                handles.append(h)
        ax.legend(handles=handles, fontsize=STYLE["font_legend"],
                  loc="upper right", framealpha=0.9)

        setup_axes(ax, r"Diffusion weight $D$", r"Amplitude $A$",
                   rf"Regime Map -- $N_m = {nm}$")
        fig.tight_layout()
        fname = f"regime_map_slice_Nm{nm:02d}.png"
        saved.append(save_figure(fig, fname))

    return saved


# ---------------------------------------------------------------------------
# Figure E: Invariant Correlation Heatmap
# ---------------------------------------------------------------------------
def figure_invariant_correlation(runs: list[Run]) -> Optional[str]:
    """Correlation heatmap of scalar invariants across admissible runs."""
    valid = [r for r in runs if r.admissible and r.has_energy]

    if len(valid) < 5:
        print("  SKIP: fewer than 5 admissible runs for correlation.")
        return None

    # Collect scalar invariants per run
    labels = []
    vectors = []

    for run in valid:
        vec = []

        # E_final
        if run.E_total is not None and len(run.E_total) > 0:
            vec.append(float(run.E_total[-1]))
        else:
            vec.append(np.nan)

        # H_final (spectral entropy)
        if run.has_modal:
            n = min(len(run.t), run.modal.shape[0])
            H = compute_shannon_entropy(run.modal[:n])
            vec.append(float(H[-1]) if len(H) > 0 else np.nan)
        else:
            vec.append(np.nan)

        # Participation final
        if run.v is not None and len(run.v) > 0:
            vec.append(float(run.v[-1]))
        else:
            vec.append(np.nan)

        # Lyapunov lambda_1
        lam = run.invariants.get("lyapunov_exponents")
        if lam and len(lam) > 0:
            vec.append(float(lam[0]))
        else:
            vec.append(np.nan)

        # Discriminant
        delta = run.invariants.get("discriminant") or run.metadata.get(
            "discriminant")
        vec.append(float(delta) if delta is not None else np.nan)

        vectors.append(vec)

    col_labels = [r"$E^*$", r"$H^*$", r"$v^*$", r"$\lambda_1$",
                  r"$\Delta$"]

    X = np.array(vectors)

    # Remove columns that are all NaN
    valid_cols = ~np.all(np.isnan(X), axis=0)
    X = X[:, valid_cols]
    col_labels = [l for l, v in zip(col_labels, valid_cols) if v]

    if X.shape[1] < 2:
        print("  SKIP: fewer than 2 non-NaN invariant columns.")
        return None

    # Compute correlation (NaN-safe)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        n_cols = X.shape[1]
        C = np.full((n_cols, n_cols), np.nan)
        for i in range(n_cols):
            for j in range(n_cols):
                mask = ~np.isnan(X[:, i]) & ~np.isnan(X[:, j])
                if np.sum(mask) > 2:
                    xi = X[mask, i]
                    xj = X[mask, j]
                    if np.std(xi) > 0 and np.std(xj) > 0:
                        C[i, j] = np.corrcoef(xi, xj)[0, 1]

    fig, ax = plt.subplots(figsize=(6, 5))
    im = ax.imshow(C, cmap="RdBu_r", vmin=-1, vmax=1, aspect="equal")

    ax.set_xticks(range(len(col_labels)))
    ax.set_xticklabels(col_labels, fontsize=STYLE["font_tick"],
                       rotation=45, ha="right")
    ax.set_yticks(range(len(col_labels)))
    ax.set_yticklabels(col_labels, fontsize=STYLE["font_tick"])

    # Annotate cells
    for i in range(len(col_labels)):
        for j in range(len(col_labels)):
            val = C[i, j]
            if not np.isnan(val):
                txt_color = "white" if abs(val) > 0.6 else "black"
                ax.text(j, i, f"{val:.2f}", ha="center", va="center",
                        fontsize=8, color=txt_color)

    fig.colorbar(im, ax=ax, label="Pearson correlation", shrink=0.8)
    ax.set_title("Invariant Correlation Heatmap",
                 fontsize=STYLE["font_title"], fontweight="bold")
    fig.tight_layout()
    return save_figure(fig, "invariant_correlation_heatmap.png")


# ---------------------------------------------------------------------------
# Figure F: Embedding Map
# ---------------------------------------------------------------------------
def figure_embedding_map(runs: list[Run]) -> Optional[str]:
    """PCA (or UMAP) embedding of invariant vectors, colored by regime."""
    valid = [r for r in runs if r.admissible and r.has_energy]
    if len(valid) < 5:
        print("  SKIP: fewer than 5 runs for embedding.")
        return None

    # Build invariant vectors
    vectors = []
    for run in valid:
        vec = []
        # Energy final
        vec.append(float(run.E_total[-1]) if run.E_total is not None
                   and len(run.E_total) > 0 else 0.0)
        # Entropy final
        if run.has_modal:
            n = min(len(run.t), run.modal.shape[0])
            H = compute_shannon_entropy(run.modal[:n])
            vec.append(float(H[-1]) if len(H) > 0 else 0.0)
        else:
            vec.append(0.0)
        # Participation
        vec.append(float(run.v[-1]) if run.v is not None
                   and len(run.v) > 0 else 0.0)
        # D, A, Nm
        vec.append(float(run.D) if run.D is not None else 0.0)
        vec.append(float(run.A) if run.A is not None else 0.0)
        vec.append(float(run.Nm) if run.Nm is not None else 0.0)
        vectors.append(vec)

    X = np.array(vectors)

    # Standardize
    mu = np.nanmean(X, axis=0)
    sigma = np.nanstd(X, axis=0)
    sigma[sigma < 1e-12] = 1.0
    X_std = (X - mu) / sigma

    # Replace any remaining NaN
    X_std = np.nan_to_num(X_std, nan=0.0)

    # Try UMAP, fall back to PCA
    method = "PCA"
    try:
        from umap import UMAP
        reducer = UMAP(n_components=2, n_neighbors=min(15, len(valid) - 1),
                       min_dist=0.1, random_state=0)
        X_2d = reducer.fit_transform(X_std)
        method = "UMAP"
    except ImportError:
        try:
            from sklearn.decomposition import PCA
            pca = PCA(n_components=2, random_state=0)
            X_2d = pca.fit_transform(X_std)
            method = f"PCA ({pca.explained_variance_ratio_[0]:.0%} + " \
                     f"{pca.explained_variance_ratio_[1]:.0%})"
        except ImportError:
            # Manual PCA via SVD
            U, S, Vt = np.linalg.svd(X_std - X_std.mean(axis=0),
                                      full_matrices=False)
            X_2d = U[:, :2] * S[:2]

    fig, ax = plt.subplots(figsize=STYLE["figsize_square"])

    for i, run in enumerate(valid):
        color = get_regime_color(run.regime)
        marker = get_nm_marker(run.Nm)
        ax.scatter(X_2d[i, 0], X_2d[i, 1], c=color, marker=marker,
                   s=50, edgecolors="black", linewidths=0.4, zorder=5)

    # Centroid
    cx, cy = np.mean(X_2d, axis=0)
    ax.plot(cx, cy, "k+", markersize=14, markeredgewidth=2, zorder=10,
            label="Centroid")

    # Cluster radius
    dists = np.sqrt((X_2d[:, 0] - cx) ** 2 + (X_2d[:, 1] - cy) ** 2)
    radius = np.mean(dists)
    circle = plt.Circle((cx, cy), radius, fill=False, color="0.5",
                         linestyle="--", linewidth=0.8, label=f"r = {radius:.2f}")
    ax.add_patch(circle)

    # Legend
    handles = [circle]
    seen_regimes = set()
    for run in valid:
        rkey = run.regime.split()[0]
        if rkey not in seen_regimes:
            seen_regimes.add(rkey)
            h = plt.Line2D([0], [0], marker="o",
                            color=get_regime_color(run.regime),
                            markersize=7, linestyle="None",
                            label=rkey.capitalize(),
                            markeredgecolor="black", markeredgewidth=0.4)
            handles.append(h)
    ax.legend(handles=handles, fontsize=STYLE["font_legend"],
              loc="upper right", framealpha=0.9)

    setup_axes(ax, f"{method} -- Component 1", f"{method} -- Component 2",
               f"Embedding Map ({method})")
    ax.set_aspect("equal", adjustable="datalim")
    fig.tight_layout()
    return save_figure(fig, "embedding_map.png")


# ---------------------------------------------------------------------------
# Figure G: Broadband Cascade
# ---------------------------------------------------------------------------
def figure_broadband_cascade(runs: list[Run]) -> Optional[str]:
    """Log-log modal energy spectrum E_k for all admissible runs."""
    valid = [r for r in runs if r.admissible and r.has_modal]
    if not valid:
        print("  SKIP: no runs with modal data.")
        return None

    D_vals = [r.D for r in valid if r.D is not None]
    d_norm = mcolors.Normalize(
        vmin=min(D_vals) * 0.9 if D_vals else 0,
        vmax=max(D_vals) * 1.1 if D_vals else 1)

    fig, ax = plt.subplots(figsize=STYLE["figsize_single"])

    for run in valid:
        n = min(len(run.t), run.modal.shape[0])
        n_modes = run.modal.shape[1]

        # Late-time average energy spectrum
        late_start = int(0.9 * n)
        if late_start >= n:
            late_start = max(0, n - 10)
        E_k = np.mean(np.abs(run.modal[late_start:n]) ** 2, axis=0)

        k = np.arange(1, n_modes + 1)
        mask = E_k > 1e-30

        color = D_CMAP(d_norm(run.D)) if run.D is not None else "0.5"
        ax.loglog(k[mask], E_k[mask], color=color, linewidth=0.6,
                  alpha=0.5)

    sm = plt.cm.ScalarMappable(cmap=D_CMAP, norm=d_norm)
    sm.set_array([])
    fig.colorbar(sm, ax=ax, label=r"$D$", pad=0.02)

    # Reference slopes
    k_ref = np.logspace(0.3, 1.5, 50)
    ax.loglog(k_ref, 0.01 * k_ref ** (-2), "k--", linewidth=0.8, alpha=0.4,
              label=r"$k^{-2}$")
    ax.loglog(k_ref, 0.001 * k_ref ** (-4), "k:", linewidth=0.8, alpha=0.4,
              label=r"$k^{-4}$")

    ax.legend(fontsize=STYLE["font_legend"], loc="lower left",
              framealpha=0.9)
    setup_axes(ax, r"Mode index $k$",
               r"Modal energy $\langle E_k \rangle_{\mathrm{att}}$",
               "Broadband Cascade -- Late-Time Energy Spectrum")
    fig.tight_layout()
    return save_figure(fig, "broadband_cascade.png")


# ---------------------------------------------------------------------------
# Figure H: Three-Stage Convergence
# ---------------------------------------------------------------------------
def figure_three_stage(runs: list[Run]) -> Optional[str]:
    """Three-stage convergence plot for a representative oscillatory run."""
    # Pick the best oscillatory run (prefer high Nm, then alphabetical)
    candidates = [r for r in runs
                  if r.admissible and r.has_energy
                  and ("osc" in r.regime or "underdamp" in r.regime)]
    if not candidates:
        candidates = [r for r in runs if r.admissible and r.has_energy]
    if not candidates:
        print("  SKIP: no runs for three-stage convergence.")
        return None

    candidates.sort(key=lambda r: (-(r.Nm or 0), r.name))
    run = candidates[0]

    t = run.t
    E = run.E_total
    n = min(len(t), len(E))
    t, E = t[:n], E[:n]

    # Approximate E* as the final value
    E_star = E[-1]
    residual = np.abs(E - E_star)
    residual_safe = np.maximum(residual, 1e-30)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(9, 8),
                                    gridspec_kw={"hspace": 0.3})

    # Top panel: E(t)
    ax1.semilogy(t, E, color="#2166ac", linewidth=STYLE["line_lw"])
    ax1.axhline(E_star, color="#b2182b", linestyle="--", linewidth=0.8,
                alpha=0.6, label=rf"$E^* = {E_star:.3e}$")

    # Mark approximate stage boundaries
    # Stage I/II: energy drops below 50% of initial
    idx_half = np.where(E < 0.5 * E[0])[0]
    t1 = t[idx_half[0]] if len(idx_half) > 0 else t[n // 4]

    # Stage II/III: residual begins clean exponential
    # Heuristic: last 30% fits well
    t2 = t[int(0.7 * n)]

    for boundary, label in [(t1, "I / II"), (t2, "II / III")]:
        ax1.axvline(boundary, color="0.5", linestyle=":", linewidth=0.8,
                    alpha=0.5)
        ax1.text(boundary, ax1.get_ylim()[1] * 0.7, f" {label}",
                 fontsize=8, color="0.4", va="top")

    ax1.legend(fontsize=STYLE["font_legend"], loc="upper right",
               framealpha=0.9)
    setup_axes(ax1, r"Time $t$", r"Energy $\mathcal{E}(t)$",
               f"Three-Stage Convergence -- {run.name}")

    # Bottom panel: |E - E*|
    ax2.semilogy(t, residual_safe, color="#1b7837",
                 linewidth=STYLE["line_lw"])

    # Shade stages
    ax2.axvspan(t[0], t1, alpha=0.06, color="#2166ac", label="Stage I")
    ax2.axvspan(t1, t2, alpha=0.06, color="#ff7f0e", label="Stage II")
    ax2.axvspan(t2, t[-1], alpha=0.06, color="#1b7837", label="Stage III")

    # Fit exponential in Stage III
    fit_start = int(0.75 * n)
    t_fit = t[fit_start:]
    log_r_fit = np.log(residual_safe[fit_start:])
    valid_mask = np.isfinite(log_r_fit)
    if np.sum(valid_mask) > 10:
        coeffs = np.polyfit(t_fit[valid_mask], log_r_fit[valid_mask], 1)
        sigma = -coeffs[0]
        C_fit = np.exp(coeffs[1])
        ax2.semilogy(t_fit, C_fit * np.exp(-sigma * t_fit),
                     "r--", linewidth=1.0, alpha=0.7,
                     label=rf"$\sigma = {sigma:.3f}$")

    ax2.legend(fontsize=STYLE["font_legend"], loc="upper right",
               framealpha=0.9, ncol=2)
    setup_axes(ax2, r"Time $t$", r"$|\mathcal{E}(t) - \mathcal{E}^*|$",
               "Energy Residual -- Stage Decomposition")

    fig.tight_layout()
    return save_figure(fig, "three_stage_convergence.png")


# ---------------------------------------------------------------------------
# Figure I: Attractor Stability
# ---------------------------------------------------------------------------
def figure_attractor_stability(runs: list[Run]) -> Optional[str]:
    """Distance to equilibrium vs time for all admissible runs."""
    valid = [r for r in runs if r.admissible and r.has_energy]
    if not valid:
        print("  SKIP: no runs for attractor stability.")
        return None

    D_vals = [r.D for r in valid if r.D is not None]
    d_norm = mcolors.Normalize(
        vmin=min(D_vals) * 0.9 if D_vals else 0,
        vmax=max(D_vals) * 1.1 if D_vals else 1)

    fig, ax = plt.subplots(figsize=STYLE["figsize_single"])

    for run in valid:
        t = run.t
        E = run.E_total
        n = min(len(t), len(E))
        E_star = E[n - 1]
        residual = np.maximum(np.abs(E[:n] - E_star), 1e-30)

        color = D_CMAP(d_norm(run.D)) if run.D is not None else "0.5"
        ax.semilogy(t[:n], residual, color=color, linewidth=0.6,
                    alpha=0.5)

    sm = plt.cm.ScalarMappable(cmap=D_CMAP, norm=d_norm)
    sm.set_array([])
    fig.colorbar(sm, ax=ax, label=r"$D$", pad=0.02)

    ax.annotate(
        r"All trajectories $\to (\rho^*, 0)$",
        xy=(0.55, 0.12), xycoords="axes fraction",
        fontsize=10, fontstyle="italic", color="0.35", ha="center",
        bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.7))

    setup_axes(ax, r"Time $t$",
               r"$|\mathcal{E}(t) - \mathcal{E}^*|$",
               "Attractor Stability -- Distance to Equilibrium")
    fig.tight_layout()
    return save_figure(fig, "attractor_stability.png")


# ---------------------------------------------------------------------------
# Main pipeline
# ---------------------------------------------------------------------------
def main():
    os.makedirs(FIG_DIR, exist_ok=True)

    print("=" * 70)
    print("  ED-SIM v1 -- Unified Figure Generation Pipeline")
    print("=" * 70)

    # Discover runs
    print(f"\nScanning: {RUNS_DIR}")
    runs = discover_runs()

    if not runs:
        print(f"\nERROR: No runs found in {RUNS_DIR}")
        print("Run experiments first:")
        print("  python experiments/regime_volume_3d.py")
        sys.exit(1)

    n_admissible = sum(1 for r in runs if r.admissible)
    n_modal = sum(1 for r in runs if r.has_modal)
    n_energy = sum(1 for r in runs if r.has_energy)

    print(f"  Found {len(runs)} runs "
          f"({n_admissible} admissible, "
          f"{n_modal} with modal data, "
          f"{n_energy} with energy data)")

    # Regime breakdown
    regime_counts = {}
    for r in runs:
        key = r.regime.split()[0] if r.regime else "unknown"
        regime_counts[key] = regime_counts.get(key, 0) + 1
    for regime, count in sorted(regime_counts.items()):
        print(f"    {regime}: {count}")

    # Generate figures
    generated = []
    skipped = []

    def run_figure(name: str, func, *args):
        print(f"\n--- {name} ---")
        try:
            result = func(*args)
            if result is None:
                skipped.append(name)
            elif isinstance(result, list):
                for r in result:
                    generated.append(r)
                    print(f"  -> {os.path.basename(r)}")
            else:
                generated.append(result)
                print(f"  -> {os.path.basename(result)}")
        except Exception as e:
            print(f"  ERROR: {e}")
            skipped.append(name)

    run_figure("(A) Energy-Entropy Trajectories",
               figure_energy_entropy, runs)
    run_figure("(B) Lyapunov Spectra",
               figure_lyapunov_spectra, runs)
    run_figure("(C) Regime Volume (3D)",
               figure_regime_volume_3d, runs)
    run_figure("(D) Regime Map Slices",
               figure_regime_slices, runs)
    run_figure("(E) Invariant Correlation Heatmap",
               figure_invariant_correlation, runs)
    run_figure("(F) Embedding Map",
               figure_embedding_map, runs)
    run_figure("(G) Broadband Cascade",
               figure_broadband_cascade, runs)
    run_figure("(H) Three-Stage Convergence",
               figure_three_stage, runs)
    run_figure("(I) Attractor Stability",
               figure_attractor_stability, runs)

    # Summary
    print("\n" + "=" * 70)
    print("  Figure Generation Summary")
    print("=" * 70)
    print(f"\n  Generated: {len(generated)} figures")
    for path in generated:
        print(f"    {os.path.basename(path)}")

    if skipped:
        print(f"\n  Skipped: {len(skipped)} figures")
        for name in skipped:
            print(f"    {name}")

    print(f"\n  All figures saved to: {FIG_DIR}")
    print("  Done.")


if __name__ == "__main__":
    main()
