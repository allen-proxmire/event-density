"""
edsim.visualization.spectra — Power spectrum and anisotropy plots.
"""

from __future__ import annotations

from typing import Optional

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

from ..core.parameters import EDParameters


def plot_spectrum_2d(
    rho: np.ndarray,
    params: EDParameters,
    ax: Optional[plt.Axes] = None,
    **fig_kw,
) -> Figure:
    """2D amplitude spectrum |rho_hat(kx, ky)| as a heatmap.

    Parameters
    ----------
    rho : np.ndarray
        2D density field.
    params : EDParameters
        Simulation parameters.

    Returns
    -------
    Figure
    """
    # TODO: forward_transform, log10(|rho_hat|), imshow
    pass


def plot_spectrum_radial(
    rho: np.ndarray,
    params: EDParameters,
    ax: Optional[plt.Axes] = None,
    **fig_kw,
) -> Figure:
    """Radially averaged power spectrum P(k) on log-log axes.

    Works for all dimensions.

    Parameters
    ----------
    rho : np.ndarray
        Density field (any d).
    params : EDParameters
        Simulation parameters.

    Returns
    -------
    Figure
    """
    # TODO: compute radial_spectrum, plot log-log
    pass


def plot_anisotropy_ellipse(
    rho: np.ndarray,
    params: EDParameters,
    ax: Optional[plt.Axes] = None,
    **fig_kw,
) -> Figure:
    """Spectral anisotropy ellipse (2D inertia tensor).

    Parameters
    ----------
    rho : np.ndarray
        2D density field.
    params : EDParameters
        Simulation parameters.

    Returns
    -------
    Figure
    """
    # TODO: compute spectral_anisotropy, draw ellipse from eigenvalues
    pass


def plot_anisotropy_ellipsoid(
    rho: np.ndarray,
    params: EDParameters,
    **fig_kw,
) -> Figure:
    """Spectral anisotropy ellipsoid (3D/4D inertia tensor, projected to 3D).

    Parameters
    ----------
    rho : np.ndarray
        3D or 4D density field.
    params : EDParameters
        Simulation parameters.

    Returns
    -------
    Figure
    """
    # TODO: compute inertia tensor, draw 3D ellipsoid
    pass
