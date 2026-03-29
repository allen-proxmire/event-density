"""
edsim.visualization.invariants — Time-evolution plots for ED invariants.

Provides individual and combined plots for energy, complexity,
spectral entropy, dissipation channels, correlation length,
and structure functions.
"""

from __future__ import annotations

from typing import Optional

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

from .style import COLORS, DEFAULT_FIGSIZE, DEFAULT_FIGSIZE_WIDE, apply_edsim_style


def plot_energy(ts, ax: Optional[plt.Axes] = None) -> Figure:
    """Plot Lyapunov energy E[rho] vs time on a semilog scale.

    Parameters
    ----------
    ts : TimeSeries
        Simulation output.
    ax : plt.Axes, optional
        Existing axes.

    Returns
    -------
    Figure
    """
    apply_edsim_style()
    if ax is None:
        fig, ax = plt.subplots(figsize=DEFAULT_FIGSIZE)
    else:
        fig = ax.figure

    ax.semilogy(ts.times, ts.energy, color=COLORS["energy"], linewidth=1.5)
    ax.set_xlabel("t")
    ax.set_ylabel("E[rho]")
    ax.set_title("Lyapunov Energy (Law 2: monotone decreasing)")
    return fig


def plot_complexity(ts, ax: Optional[plt.Axes] = None) -> Figure:
    """Plot ED-complexity C[rho] vs time on a semilog scale.

    Parameters
    ----------
    ts : TimeSeries
        Simulation output.
    ax : plt.Axes, optional
        Existing axes.

    Returns
    -------
    Figure
    """
    apply_edsim_style()
    if ax is None:
        fig, ax = plt.subplots(figsize=DEFAULT_FIGSIZE)
    else:
        fig = ax.figure

    ax.semilogy(ts.times, ts.complexity, color=COLORS["complexity"], linewidth=1.5)
    ax.set_xlabel("t")
    ax.set_ylabel("C[rho]")
    ax.set_title("ED-Complexity")
    return fig


def plot_spectral_entropy(ts, ax: Optional[plt.Axes] = None) -> Figure:
    """Plot spectral entropy H vs time.

    Parameters
    ----------
    ts : TimeSeries
        Simulation output.
    ax : plt.Axes, optional
        Existing axes.

    Returns
    -------
    Figure
    """
    apply_edsim_style()
    if ax is None:
        fig, ax = plt.subplots(figsize=DEFAULT_FIGSIZE)
    else:
        fig = ax.figure

    ax.plot(ts.times, ts.spectral_entropy, color=COLORS["entropy"], linewidth=1.5)
    ax.set_xlabel("t")
    ax.set_ylabel("H")
    ax.set_title("Spectral Entropy (Law 3: concentration)")
    return fig


def plot_dissipation_channels(ts, ax: Optional[plt.Axes] = None) -> Figure:
    """Plot dissipation channel ratios R_grad, R_pen, R_part vs time.

    Parameters
    ----------
    ts : TimeSeries
        Simulation output.
    ax : plt.Axes, optional
        Existing axes.

    Returns
    -------
    Figure
    """
    apply_edsim_style()
    if ax is None:
        fig, ax = plt.subplots(figsize=DEFAULT_FIGSIZE)
    else:
        fig = ax.figure

    ax.plot(ts.times, ts.R_grad, label="R_grad", color=COLORS["R_grad"], linewidth=1.5)
    ax.plot(ts.times, ts.R_pen, label="R_pen", color=COLORS["R_pen"], linewidth=1.5)
    ax.plot(ts.times, ts.R_part, label="R_part", color=COLORS["R_part"], linewidth=1.5)
    ax.set_xlabel("t")
    ax.set_ylabel("fraction")
    ax.set_title("Dissipation Channels (Law 5)")
    ax.legend(loc="center right")
    ax.set_ylim(-0.02, 1.05)
    return fig


def plot_correlation_length(ts, ax: Optional[plt.Axes] = None) -> Figure:
    """Plot correlation length xi vs time.

    Parameters
    ----------
    ts : TimeSeries
        Simulation output.
    ax : plt.Axes, optional
        Existing axes.

    Returns
    -------
    Figure
    """
    apply_edsim_style()
    if ax is None:
        fig, ax = plt.subplots(figsize=DEFAULT_FIGSIZE)
    else:
        fig = ax.figure

    ax.plot(ts.times, ts.correlation_length, color=COLORS["xi"], linewidth=1.5)
    ax.set_xlabel("t")
    ax.set_ylabel("xi")
    ax.set_title("Correlation Length")
    return fig


def plot_structure_function(ts, step: int = -1, ax: Optional[plt.Axes] = None) -> Figure:
    """Plot the second-order structure function S_2(r) at a given snapshot.

    Parameters
    ----------
    ts : TimeSeries
        Simulation output.
    step : int
        Snapshot index.
    ax : plt.Axes, optional
        Existing axes.

    Returns
    -------
    Figure
    """
    apply_edsim_style()
    if ax is None:
        fig, ax = plt.subplots(figsize=DEFAULT_FIGSIZE)
    else:
        fig = ax.figure

    r = ts.structure_r[step]
    S2 = ts.structure_S2[step]
    t = ts.times[step]

    ax.plot(r, S2, "o-", color=COLORS["complexity"], markersize=3, linewidth=1)
    ax.set_xlabel("r")
    ax.set_ylabel("S_2(r)")
    ax.set_title(f"Structure Function at t = {t:.4f}")
    return fig


def plot_atlas_dashboard(ts) -> Figure:
    """Six-panel dashboard of core invariants over time.

    Panels: energy, complexity, spectral entropy,
    dissipation channels, correlation length, morphology fractions.

    Parameters
    ----------
    ts : TimeSeries
        Simulation output.

    Returns
    -------
    Figure
    """
    apply_edsim_style()
    fig, axes = plt.subplots(2, 3, figsize=(15, 9))

    plot_energy(ts, ax=axes[0, 0])
    plot_complexity(ts, ax=axes[0, 1])
    plot_spectral_entropy(ts, ax=axes[0, 2])
    plot_dissipation_channels(ts, ax=axes[1, 0])
    plot_correlation_length(ts, ax=axes[1, 1])

    # Morphology in the last panel
    from .morphology import plot_morphology_fractions
    plot_morphology_fractions(ts, ax=axes[1, 2])

    fig.tight_layout()
    return fig
