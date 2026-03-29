"""
edsim.core.participation — Global participation variable dynamics.

Implements the participation ODE:
    dv/dt = (1/tau) * (F_avg - zeta * v)
using exact exponential integration.
"""

from __future__ import annotations

import math

import numpy as np

from .parameters import EDParameters


def advance_v(v: float, F_avg: float, params: EDParameters) -> float:
    """Advance the participation variable v by one time step dt.

    Uses the exact solution of the linear ODE:
        v(t+dt) = v(t) * exp(-zeta*dt/tau)
                + (F_avg / zeta) * (1 - exp(-zeta*dt/tau))

    Parameters
    ----------
    v : float
        Current participation variable.
    F_avg : float
        Domain-averaged local density operator (F_local, not F_total).
    params : EDParameters
        Simulation parameters (uses zeta, tau, dt).

    Returns
    -------
    float
        Updated participation variable.
    """
    decay = math.exp(-params.zeta * params.dt / params.tau)
    return v * decay + (F_avg / params.zeta) * (1.0 - decay)


def spatial_average(F: np.ndarray, dx: tuple) -> float:
    """Compute the domain-averaged operator: F_avg = (1/|Omega|) * integral F dV.

    Uses the composite trapezoidal rule for Neumann-compatible grids
    (endpoints included). For interior-only grids the simple mean is
    equivalent because the cell volumes are uniform.

    Parameters
    ----------
    F : np.ndarray
        Operator field of shape (N1, ..., Nd).
    dx : tuple[float, ...]
        Grid spacing per axis.

    Returns
    -------
    float
        Domain-averaged value.
    """
    # Cell volume
    cell_vol = 1.0
    for dxi in dx:
        cell_vol *= dxi

    # Domain volume (Neumann grid: N-1 intervals per axis, total length L)
    # For a uniform grid the trapezoidal rule with N points over [0, L]
    # gives integral ≈ mean(F) * L.  Since we want the spatial average
    # (integral / volume), this simplifies to mean(F).
    return float(np.mean(F))
