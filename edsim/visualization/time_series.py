"""
edsim.visualization.time_series — Time-evolution diagnostic plots.
"""

from __future__ import annotations

from typing import Optional

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

from ..core.parameters import EDParameters


def plot_invariants(
    times: np.ndarray,
    invariants: list[dict],
    params: EDParameters,
    **fig_kw,
) -> Figure:
    """Multi-panel time evolution plot of core invariants.

    Panels: energy, mass, complexity, spectral entropy, R_grad.

    Parameters
    ----------
    times : np.ndarray
        Array of time values.
    invariants : list[dict]
        List of invariant dicts from ``compute_atlas()`` at each output step.
    params : EDParameters
        Simulation parameters.

    Returns
    -------
    Figure
    """
    # TODO: extract each invariant series, 5-panel subplot
    pass


def plot_morphology_evolution(
    times: np.ndarray,
    invariants: list[dict],
    params: EDParameters,
    **fig_kw,
) -> Figure:
    """Stacked area plot of morphology fractions vs time.

    Parameters
    ----------
    times : np.ndarray
        Array of time values.
    invariants : list[dict]
        List of invariant dicts with ``morphology_fractions``.
    params : EDParameters
        Simulation parameters.

    Returns
    -------
    Figure
    """
    # TODO: extract fractions, stackplot
    pass


def plot_dissipation_partition(
    times: np.ndarray,
    invariants: list[dict],
    params: EDParameters,
    **fig_kw,
) -> Figure:
    """Plot R_grad, R_pen, R_part vs time.

    Parameters
    ----------
    times : np.ndarray
        Array of time values.
    invariants : list[dict]
        List of invariant dicts with dissipation ratios.
    params : EDParameters
        Simulation parameters.

    Returns
    -------
    Figure
    """
    # TODO: extract ratios, line plot with legend
    pass


def plot_snapshot_evolution(
    states: list[np.ndarray],
    times: np.ndarray,
    params: EDParameters,
    n_snapshots: int = 6,
    **fig_kw,
) -> Figure:
    """Grid of density field snapshots at selected time points.

    Parameters
    ----------
    states : list[np.ndarray]
        Density fields at each output step.
    times : np.ndarray
        Array of time values.
    params : EDParameters
        Simulation parameters.
    n_snapshots : int
        Number of snapshots to display.

    Returns
    -------
    Figure
    """
    # TODO: select evenly-spaced indices, subplot grid, plot each
    pass
