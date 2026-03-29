"""
edsim.visualization.geometry — Hessian, curvature, and morphology maps.
"""

from __future__ import annotations

from typing import Optional

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

from ..core.parameters import EDParameters


def plot_morphology_map(
    classification_map: np.ndarray,
    params: EDParameters,
    ax: Optional[plt.Axes] = None,
    **fig_kw,
) -> Figure:
    """Plot the spatial morphology classification map.

    Colour-codes each grid point by its morphological type
    (filament, sheet, pancake, blob).

    Parameters
    ----------
    classification_map : np.ndarray
        Integer labels from ``morphology_fractions()``.
    params : EDParameters
        Simulation parameters (for axis extents).

    Returns
    -------
    Figure
    """
    # TODO: discrete colormap, imshow (2D) or slice (3D/4D)
    pass


def plot_hessian_eigenvalues(
    eigenvalues: np.ndarray,
    params: EDParameters,
    which: int = 0,
    **fig_kw,
) -> Figure:
    """Plot a single Hessian eigenvalue field as a heatmap/slice.

    Parameters
    ----------
    eigenvalues : np.ndarray
        Hessian eigenvalues of shape ``(*N, d)``.
    params : EDParameters
        Simulation parameters.
    which : int
        Which eigenvalue to plot (0 = largest, d-1 = smallest).

    Returns
    -------
    Figure
    """
    # TODO: extract eigenvalues[..., which], plot as heatmap/slice
    pass


def plot_curvature_field(
    rho: np.ndarray,
    params: EDParameters,
    **fig_kw,
) -> Figure:
    """Plot the curvature of level sets of rho.

    For 2D: kappa = div(grad rho / |grad rho|).
    For 3D: mean curvature of the isosurface.

    Parameters
    ----------
    rho : np.ndarray
        Density field.
    params : EDParameters
        Simulation parameters.

    Returns
    -------
    Figure
    """
    # TODO: compute curvature, plot as heatmap/slice
    pass
