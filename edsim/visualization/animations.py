"""
edsim.visualization.animations — Animated visualizations of ED simulations.

Uses matplotlib.animation.FuncAnimation to create animations of
density field evolution and morphology fraction evolution.
"""

from __future__ import annotations

from typing import Optional

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.animation import FuncAnimation

from .style import DEFAULT_CMAP_DENSITY, COLORS, apply_edsim_style


def _extract_2d_slice(
    rho: np.ndarray,
    slice_axis: Optional[int] = None,
    slice_index: Optional[int] = None,
) -> np.ndarray:
    """Extract a 2D slice from a 2D/3D/4D field."""
    d = rho.ndim
    if d == 2:
        return rho
    elif d == 3:
        ax = slice_axis if slice_axis is not None else 0
        idx = slice_index if slice_index is not None else rho.shape[ax] // 2
        sl = [slice(None)] * 3
        sl[ax] = idx
        return rho[tuple(sl)]
    elif d == 4:
        idx0 = rho.shape[0] // 2
        idx1 = rho.shape[1] // 2
        return rho[idx0, idx1, :, :]
    else:
        raise ValueError(f"Cannot animate {d}D field")


def animate_field(
    ts,
    interval: int = 80,
    slice_axis: Optional[int] = None,
    slice_index: Optional[int] = None,
    cmap: str = DEFAULT_CMAP_DENSITY,
) -> FuncAnimation:
    """Animate the density field over time.

    Returns a FuncAnimation object. Display in Jupyter with::

        from IPython.display import HTML
        HTML(ani.to_jshtml())

    Or save::

        ani.save("field.gif", writer="pillow", fps=12)

    Parameters
    ----------
    ts : TimeSeries
        Simulation output.
    interval : int
        Delay between frames in milliseconds.
    slice_axis : int, optional
        For 3D/4D: axis to slice along.
    slice_index : int, optional
        For 3D/4D: index along slice axis.
    cmap : str
        Colormap.

    Returns
    -------
    FuncAnimation
    """
    apply_edsim_style()

    # Precompute all 2D slices and global colour range
    slices = [_extract_2d_slice(f, slice_axis, slice_index) for f in ts.fields]
    vmin = min(s.min() for s in slices)
    vmax = max(s.max() for s in slices)

    fig, ax = plt.subplots(figsize=(6, 5))
    im = ax.imshow(slices[0].T, origin="lower", cmap=cmap,
                   vmin=vmin, vmax=vmax, aspect="equal")
    fig.colorbar(im, ax=ax, shrink=0.8)
    title = ax.set_title(f"t = {ts.times[0]:.4f}")
    ax.set_xlabel("x")
    ax.set_ylabel("y")

    def update(frame):
        im.set_data(slices[frame].T)
        title.set_text(f"t = {ts.times[frame]:.4f}")
        return [im, title]

    ani = FuncAnimation(fig, update, frames=len(slices),
                        interval=interval, blit=False, repeat=True)
    plt.close(fig)  # prevent double display in notebooks
    return ani


def animate_morphology(
    ts,
    interval: int = 80,
) -> FuncAnimation:
    """Animate morphology fractions as a bar chart over time.

    Parameters
    ----------
    ts : TimeSeries
        Simulation output.
    interval : int
        Delay between frames in milliseconds.

    Returns
    -------
    FuncAnimation
    """
    apply_edsim_style()

    if not ts.morphology_fractions:
        raise ValueError("No morphology data in TimeSeries")

    # Determine active classes
    all_keys = set()
    for m in ts.morphology_fractions:
        for k, v in m.items():
            if v > 1e-10:
                all_keys.add(k)
    all_keys.update(["blob", "sheet"])

    _order = ["blob", "sheet", "filament", "pancake"]
    classes = [c for c in _order if c in all_keys]
    colors = [COLORS.get(c, "#999999") for c in classes]

    fig, ax = plt.subplots(figsize=(7, 4))

    # Initial bars
    fracs_0 = [ts.morphology_fractions[0].get(c, 0) for c in classes]
    bars = ax.bar(classes, fracs_0, color=colors, alpha=0.85)
    ax.set_ylim(0, 1.05)
    ax.set_ylabel("volume fraction")
    title = ax.set_title(f"Morphology at t = {ts.times[0]:.4f}")

    def update(frame):
        fracs = [ts.morphology_fractions[frame].get(c, 0) for c in classes]
        for bar, f in zip(bars, fracs):
            bar.set_height(f)
        title.set_text(f"Morphology at t = {ts.times[frame]:.4f}")
        return list(bars) + [title]

    ani = FuncAnimation(fig, update, frames=len(ts.times),
                        interval=interval, blit=False, repeat=True)
    plt.close(fig)
    return ani


def animate_invariant_dashboard(
    ts,
    interval: int = 100,
) -> FuncAnimation:
    """Animate a three-panel dashboard: field, energy+complexity, morphology.

    Parameters
    ----------
    ts : TimeSeries
        Simulation output.
    interval : int
        Delay between frames in milliseconds.

    Returns
    -------
    FuncAnimation
    """
    apply_edsim_style()

    slices = [_extract_2d_slice(f) for f in ts.fields]
    vmin = min(s.min() for s in slices)
    vmax = max(s.max() for s in slices)

    fig, axes = plt.subplots(1, 3, figsize=(15, 4.5))

    # Panel 1: field
    im = axes[0].imshow(slices[0].T, origin="lower", cmap=DEFAULT_CMAP_DENSITY,
                        vmin=vmin, vmax=vmax, aspect="equal")
    fig.colorbar(im, ax=axes[0], shrink=0.7)
    axes[0].set_xlabel("x")
    axes[0].set_ylabel("y")
    field_title = axes[0].set_title(f"rho (t={ts.times[0]:.4f})")

    # Panel 2: energy + complexity traces
    axes[1].semilogy(ts.times, ts.energy, color=COLORS["energy"], alpha=0.3, label="E")
    axes[1].semilogy(ts.times, ts.complexity, color=COLORS["complexity"], alpha=0.3, label="C")
    e_marker, = axes[1].semilogy([ts.times[0]], [ts.energy[0]], "o",
                                  color=COLORS["energy"], markersize=6)
    c_marker, = axes[1].semilogy([ts.times[0]], [ts.complexity[0]], "o",
                                  color=COLORS["complexity"], markersize=6)
    axes[1].set_xlabel("t")
    axes[1].set_ylabel("value")
    axes[1].set_title("Energy + Complexity")
    axes[1].legend(fontsize=8)

    # Panel 3: morphology bars
    _order = ["blob", "sheet", "filament", "pancake"]
    all_keys = set()
    for m in ts.morphology_fractions:
        for k, v in m.items():
            if v > 1e-10:
                all_keys.add(k)
    all_keys.update(["blob", "sheet"])
    classes = [c for c in _order if c in all_keys]
    morph_colors = [COLORS.get(c, "#999") for c in classes]
    fracs_0 = [ts.morphology_fractions[0].get(c, 0) for c in classes]
    bars = axes[2].bar(classes, fracs_0, color=morph_colors, alpha=0.85)
    axes[2].set_ylim(0, 1.05)
    axes[2].set_ylabel("fraction")
    morph_title = axes[2].set_title("Morphology")

    fig.tight_layout()

    def update(frame):
        # Field
        im.set_data(slices[frame].T)
        field_title.set_text(f"rho (t={ts.times[frame]:.4f})")
        # Markers
        e_marker.set_data([ts.times[frame]], [ts.energy[frame]])
        c_marker.set_data([ts.times[frame]], [ts.complexity[frame]])
        # Bars
        fracs = [ts.morphology_fractions[frame].get(c, 0) for c in classes]
        for bar, f in zip(bars, fracs):
            bar.set_height(f)
        morph_title.set_text(f"Morphology (t={ts.times[frame]:.4f})")
        return [im, field_title, e_marker, c_marker, morph_title] + list(bars)

    ani = FuncAnimation(fig, update, frames=len(ts.times),
                        interval=interval, blit=False, repeat=True)
    plt.close(fig)
    return ani
