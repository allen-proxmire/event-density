"""
edsim.manuscript.figures — Auto-generated figures for the ED-SIM-02 manuscript.

Each function runs a scenario, generates a figure via the visualization
layer, saves it as a PNG, and returns the relative path.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from ..experiments.scenarios import get_scenario
from ..experiments.atlas import run_atlas, summarize_time_series
from ..visualization.fields import plot_field_comparison
from ..visualization.invariants import (
    plot_energy,
    plot_complexity,
    plot_spectral_entropy,
    plot_dissipation_channels,
    plot_correlation_length,
)
from ..visualization.morphology import plot_morphology_fractions
from ..visualization.style import apply_edsim_style


# Default output directory for figures
DEFAULT_FIG_DIR = Path("manuscript/figures")


def _ensure_dir(fig_dir: Path) -> None:
    fig_dir.mkdir(parents=True, exist_ok=True)


def _save(fig, path: Path, dpi: int = 150) -> str:
    fig.savefig(str(path), dpi=dpi, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    return str(path)


def fig_energy_complexity(fig_dir: Path = DEFAULT_FIG_DIR) -> str:
    """Generate energy + complexity time series figure.

    Returns
    -------
    str
        Path to the saved PNG.
    """
    _ensure_dir(fig_dir)
    _, ts = run_atlas(get_scenario("A_2d_cosine"))

    apply_edsim_style()
    fig, axes = plt.subplots(1, 2, figsize=(11, 4))
    plot_energy(ts, ax=axes[0])
    plot_complexity(ts, ax=axes[1])
    fig.tight_layout()

    return _save(fig, fig_dir / "energy_complexity.png")


def fig_spectral_entropy(fig_dir: Path = DEFAULT_FIG_DIR) -> str:
    """Generate spectral entropy time series figure.

    Returns
    -------
    str
        Path to the saved PNG.
    """
    _ensure_dir(fig_dir)
    _, ts = run_atlas(get_scenario("A_2d_cosine"))

    fig = plot_spectral_entropy(ts)
    return _save(fig, fig_dir / "spectral_entropy.png")


def fig_morphology_evolution(fig_dir: Path = DEFAULT_FIG_DIR) -> str:
    """Generate morphology fraction evolution figure.

    Returns
    -------
    str
        Path to the saved PNG.
    """
    _ensure_dir(fig_dir)
    _, ts = run_atlas(get_scenario("A_2d_cosine"))

    fig = plot_morphology_fractions(ts)
    return _save(fig, fig_dir / "morphology_evolution.png")


def fig_field_evolution_2d(fig_dir: Path = DEFAULT_FIG_DIR) -> str:
    """Generate field evolution comparison (t=0, t=T/2, t=T).

    Returns
    -------
    str
        Path to the saved PNG.
    """
    _ensure_dir(fig_dir)
    _, ts = run_atlas(get_scenario("A_2d_cosine"))

    fig = plot_field_comparison(ts, steps=[0, len(ts.times) // 2, -1])
    return _save(fig, fig_dir / "field_evolution_2d.png")


def fig_dissipation_channels(fig_dir: Path = DEFAULT_FIG_DIR) -> str:
    """Generate dissipation channel decomposition figure.

    Returns
    -------
    str
        Path to the saved PNG.
    """
    _ensure_dir(fig_dir)
    _, ts = run_atlas(get_scenario("A_2d_cosine"))

    apply_edsim_style()
    fig, axes = plt.subplots(1, 2, figsize=(11, 4))
    plot_dissipation_channels(ts, ax=axes[0])
    plot_correlation_length(ts, ax=axes[1])
    fig.tight_layout()

    return _save(fig, fig_dir / "dissipation_correlation.png")


def fig_dimensional_scaling(fig_dir: Path = DEFAULT_FIG_DIR) -> str:
    """Generate dimensional comparison figure (2D/3D/4D).

    Shows spectral entropy and correlation length at t=0 across dimensions.

    Returns
    -------
    str
        Path to the saved PNG.
    """
    _ensure_dir(fig_dir)

    _, ts_2d = run_atlas(get_scenario("A_2d_cosine"))
    _, ts_3d = run_atlas(get_scenario("B_3d_cosine"))
    _, ts_4d = run_atlas(get_scenario("C_4d_cosine"))

    dims = [2, 3, 4]
    H_vals = [ts_2d.spectral_entropy[0], ts_3d.spectral_entropy[0], ts_4d.spectral_entropy[0]]
    xi_vals = [ts_2d.correlation_length[0], ts_3d.correlation_length[0], ts_4d.correlation_length[0]]

    apply_edsim_style()
    fig, axes = plt.subplots(1, 2, figsize=(10, 4))

    axes[0].bar(dims, H_vals, color=["#1f77b4", "#ff7f0e", "#2ca02c"], alpha=0.85)
    axes[0].set_xlabel("dimension d")
    axes[0].set_ylabel("H (spectral entropy)")
    axes[0].set_title("Spectral Entropy at t=0")
    axes[0].set_xticks(dims)

    axes[1].bar(dims, xi_vals, color=["#1f77b4", "#ff7f0e", "#2ca02c"], alpha=0.85)
    axes[1].set_xlabel("dimension d")
    axes[1].set_ylabel("xi (correlation length)")
    axes[1].set_title("Correlation Length at t=0")
    axes[1].set_xticks(dims)

    fig.tight_layout()
    return _save(fig, fig_dir / "dimensional_scaling.png")


def generate_all_figures(fig_dir: Path = DEFAULT_FIG_DIR) -> dict[str, str]:
    """Generate all manuscript figures and return a path dictionary.

    Returns
    -------
    dict[str, str]
        Mapping from figure name to file path.
    """
    _ensure_dir(fig_dir)

    paths = {
        "energy": fig_energy_complexity(fig_dir),
        "entropy": fig_spectral_entropy(fig_dir),
        "morphology": fig_morphology_evolution(fig_dir),
        "field_evolution": fig_field_evolution_2d(fig_dir),
        "dissipation": fig_dissipation_channels(fig_dir),
        "dimensional_scaling": fig_dimensional_scaling(fig_dir),
    }

    # Also generate complexity path (same file as energy)
    paths["complexity"] = paths["energy"]

    return paths
