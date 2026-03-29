"""
edsim.visualization.fields — Density field visualizations.

Provides snapshot and time-indexed field plots for 2D/3D/4D.
For 3D and 4D, shows slices through the volume.
"""

from __future__ import annotations

from typing import Optional

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

from .style import DEFAULT_CMAP_DENSITY, DEFAULT_FIGSIZE, apply_edsim_style


def plot_field_snapshot(
    rho: np.ndarray,
    title: Optional[str] = None,
    slice_axis: Optional[int] = None,
    slice_index: Optional[int] = None,
    cmap: str = DEFAULT_CMAP_DENSITY,
    ax: Optional[plt.Axes] = None,
) -> Figure:
    """Plot a single snapshot of the density field.

    - 2D: full heatmap via imshow.
    - 3D: slice along ``slice_axis`` at ``slice_index`` (default: midplane along axis 0).
    - 4D: two sequential slices (axes 0 and 1) at midpoints, showing a 2D cut.

    Parameters
    ----------
    rho : np.ndarray
        Density field (2D, 3D, or 4D).
    title : str, optional
        Plot title.
    slice_axis : int, optional
        Axis to slice along (3D/4D). Default: 0.
    slice_index : int, optional
        Index along the slice axis. Default: midpoint.
    cmap : str
        Colormap name.
    ax : plt.Axes, optional
        Existing axes to plot into.

    Returns
    -------
    Figure
    """
    apply_edsim_style()
    d = rho.ndim

    if d == 2:
        field_2d = rho
        slice_label = ""
    elif d == 3:
        ax_s = slice_axis if slice_axis is not None else 0
        idx = slice_index if slice_index is not None else rho.shape[ax_s] // 2
        sl = [slice(None)] * 3
        sl[ax_s] = idx
        field_2d = rho[tuple(sl)]
        slice_label = f" (axis {ax_s}, index {idx})"
    elif d == 4:
        ax0 = 0
        ax1 = 1
        idx0 = rho.shape[ax0] // 2
        idx1 = rho.shape[ax1] // 2
        field_2d = rho[idx0, idx1, :, :]
        slice_label = f" (axes 0={idx0}, 1={idx1})"
    else:
        raise ValueError(f"Cannot plot {d}D field")

    if ax is None:
        fig, ax = plt.subplots(figsize=DEFAULT_FIGSIZE)
    else:
        fig = ax.figure

    im = ax.imshow(field_2d.T, origin="lower", cmap=cmap, aspect="equal")
    fig.colorbar(im, ax=ax, shrink=0.8)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    if title:
        ax.set_title(title + slice_label)
    else:
        ax.set_title(f"rho{slice_label}")

    return fig


def plot_field_timeseries(
    ts,
    step: int = 0,
    **kwargs,
) -> Figure:
    """Plot a single field snapshot from a TimeSeries at the given step index.

    Parameters
    ----------
    ts : TimeSeries
        Simulation output.
    step : int
        Snapshot index (0 = initial, -1 = final).
    **kwargs
        Passed to ``plot_field_snapshot``.

    Returns
    -------
    Figure
    """
    rho = ts.fields[step]
    t = ts.times[step]
    title = kwargs.pop("title", f"t = {t:.4f}")
    return plot_field_snapshot(rho, title=title, **kwargs)


def plot_field_comparison(
    ts,
    steps: Optional[list] = None,
    ncols: int = 3,
    **kwargs,
) -> Figure:
    """Plot multiple field snapshots side by side.

    Parameters
    ----------
    ts : TimeSeries
        Simulation output.
    steps : list[int], optional
        Snapshot indices. Default: [0, len//2, -1].
    ncols : int
        Number of columns in the subplot grid.
    **kwargs
        Passed to ``plot_field_snapshot``.

    Returns
    -------
    Figure
    """
    apply_edsim_style()

    if steps is None:
        n = len(ts.times)
        steps = [0, n // 2, n - 1]

    nrows = (len(steps) + ncols - 1) // ncols
    fig, axes = plt.subplots(nrows, ncols, figsize=(5 * ncols, 4.5 * nrows))
    if len(steps) == 1:
        axes = [axes]
    else:
        axes = axes.ravel() if hasattr(axes, 'ravel') else [axes]

    for i, step in enumerate(steps):
        if i < len(axes):
            rho = ts.fields[step]
            t = ts.times[step]
            plot_field_snapshot(rho, title=f"t = {t:.4f}", ax=axes[i], **kwargs)

    # Hide unused axes
    for j in range(len(steps), len(axes)):
        axes[j].set_visible(False)

    fig.tight_layout()
    return fig
