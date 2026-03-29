"""
edsim.visualization.style — ED-SIM style conventions for all plots.

Defines colormaps, figure sizes, font sizes, and colour palettes
used consistently across all visualization functions.
"""

from __future__ import annotations

import matplotlib as mpl
import matplotlib.pyplot as plt

# --- ED-SIM default style constants ---

DEFAULT_FIGSIZE = (8, 5)
DEFAULT_FIGSIZE_WIDE = (12, 5)
DEFAULT_FIGSIZE_TALL = (8, 8)
DEFAULT_DPI = 150
DEFAULT_CMAP_DENSITY = "viridis"
DEFAULT_CMAP_SIGNED = "RdBu_r"
DEFAULT_CMAP_MORPHOLOGY = "Set2"
DEFAULT_FONTSIZE_TITLE = 13
DEFAULT_FONTSIZE_LABEL = 11
DEFAULT_FONTSIZE_TICK = 9

# Colour palette for invariant curves
COLORS = {
    "energy": "#1f77b4",
    "complexity": "#d62728",
    "entropy": "#2ca02c",
    "mass": "#9467bd",
    "R_grad": "#1f77b4",
    "R_pen": "#ff7f0e",
    "R_part": "#2ca02c",
    "xi": "#e377c2",
    "blob": "#1f77b4",
    "sheet": "#ff7f0e",
    "filament": "#2ca02c",
    "pancake": "#d62728",
}


def apply_edsim_style() -> None:
    """Apply the ED-SIM matplotlib style globally."""
    plt.rcParams.update({
        "font.size": DEFAULT_FONTSIZE_LABEL,
        "axes.titlesize": DEFAULT_FONTSIZE_TITLE,
        "axes.labelsize": DEFAULT_FONTSIZE_LABEL,
        "xtick.labelsize": DEFAULT_FONTSIZE_TICK,
        "ytick.labelsize": DEFAULT_FONTSIZE_TICK,
        "legend.fontsize": DEFAULT_FONTSIZE_TICK,
        "figure.dpi": DEFAULT_DPI,
        "axes.grid": True,
        "grid.alpha": 0.3,
        "grid.linestyle": "--",
    })


def get_cmap(name: str) -> mpl.colors.Colormap:
    """Return an ED-SIM colormap by semantic name.

    Parameters
    ----------
    name : str
        One of "density", "signed", "morphology".

    Returns
    -------
    matplotlib.colors.Colormap
    """
    mapping = {
        "density": DEFAULT_CMAP_DENSITY,
        "signed": DEFAULT_CMAP_SIGNED,
        "morphology": DEFAULT_CMAP_MORPHOLOGY,
    }
    return plt.get_cmap(mapping.get(name, name))
