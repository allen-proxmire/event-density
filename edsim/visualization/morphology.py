"""
edsim.visualization.morphology — Morphology fraction plots.

Provides stacked area and line plots of morphology fractions over time,
adapting to the number of classes available (2D: 2, 3D: 3, 4D: 4).
"""

from __future__ import annotations

from typing import Optional

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

from .style import COLORS, DEFAULT_FIGSIZE, apply_edsim_style


# Ordered list of morphology classes and their colours
_MORPH_CLASSES = [
    ("blob", COLORS["blob"]),
    ("sheet", COLORS["sheet"]),
    ("filament", COLORS["filament"]),
    ("pancake", COLORS["pancake"]),
]


def plot_morphology_fractions(
    ts,
    ax: Optional[plt.Axes] = None,
    style: str = "stacked",
) -> Figure:
    """Plot morphology fractions over time.

    Automatically adapts to the classes present in the data:
    - 2D: blob, sheet
    - 3D: blob, sheet, filament
    - 4D: blob, sheet, filament, pancake

    Parameters
    ----------
    ts : TimeSeries
        Simulation output with ``morphology_fractions`` attribute.
    ax : plt.Axes, optional
        Existing axes.
    style : str
        "stacked" for stackplot, "lines" for individual lines.

    Returns
    -------
    Figure
    """
    apply_edsim_style()
    if ax is None:
        fig, ax = plt.subplots(figsize=DEFAULT_FIGSIZE)
    else:
        fig = ax.figure

    if not ts.morphology_fractions:
        ax.set_title("Morphology (no data)")
        return fig

    # Determine which classes are present (nonzero in any snapshot)
    all_keys = set()
    for m in ts.morphology_fractions:
        for k, v in m.items():
            if v > 1e-10:
                all_keys.add(k)

    # Always include at least blob and sheet
    all_keys.add("blob")
    all_keys.add("sheet")

    # Order consistently
    active = [(name, color) for name, color in _MORPH_CLASSES if name in all_keys]

    times = np.array(ts.times)
    data = {}
    for name, _ in active:
        data[name] = np.array([m.get(name, 0.0) for m in ts.morphology_fractions])

    if style == "stacked":
        arrays = [data[name] for name, _ in active]
        labels = [name for name, _ in active]
        colors = [color for _, color in active]
        ax.stackplot(times, *arrays, labels=labels, colors=colors, alpha=0.8)
        ax.set_ylim(0, 1.05)
    else:
        for name, color in active:
            ax.plot(times, data[name], label=name, color=color, linewidth=1.5)

    ax.set_xlabel("t")
    ax.set_ylabel("volume fraction")
    ax.set_title("Morphology Fractions")
    ax.legend(loc="center right", fontsize=9)

    return fig


def plot_morphology_snapshot(
    classification_map: np.ndarray,
    ax: Optional[plt.Axes] = None,
    title: Optional[str] = None,
) -> Figure:
    """Plot a spatial morphology classification map (2D only).

    Parameters
    ----------
    classification_map : np.ndarray
        Integer labels from morphology classification at each grid point.
    ax : plt.Axes, optional
        Existing axes.
    title : str, optional
        Plot title.

    Returns
    -------
    Figure
    """
    apply_edsim_style()
    if ax is None:
        fig, ax = plt.subplots(figsize=DEFAULT_FIGSIZE)
    else:
        fig = ax.figure

    im = ax.imshow(classification_map.T, origin="lower", cmap="Set2", aspect="equal")
    fig.colorbar(im, ax=ax, shrink=0.8)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title(title or "Morphology Map")

    return fig
