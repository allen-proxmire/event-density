"""
edsim.visualization.horizons — Horizon mask and proximity field plots.
"""

from __future__ import annotations

from typing import Optional

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

from ..core.parameters import EDParameters


def plot_horizon_mask(
    rho: np.ndarray,
    params: EDParameters,
    threshold: float = 0.95,
    ax: Optional[plt.Axes] = None,
    **fig_kw,
) -> Figure:
    """Plot the binary horizon mask: regions where rho/rho_max > threshold.

    Parameters
    ----------
    rho : np.ndarray
        Density field.
    params : EDParameters
        Simulation parameters.
    threshold : float
        Fraction of rho_max defining the horizon.

    Returns
    -------
    Figure
    """
    # TODO: compute mask, overlay on density field
    pass


def plot_proximity_field(
    rho: np.ndarray,
    params: EDParameters,
    ax: Optional[plt.Axes] = None,
    **fig_kw,
) -> Figure:
    """Plot the proximity field: (rho_max - rho) / rho_max.

    Low values indicate nearness to the capacity bound (horizon formation).

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
    # TODO: compute proximity, plot as heatmap/slice
    pass
