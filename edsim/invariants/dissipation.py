"""
edsim.invariants.dissipation — Dissipation channel decomposition.

Decomposes dE/dt into gradient, penalty, and participation channels
following the ED-Phys-40 architecture:

    dE/dt = -(gradient channel) - (penalty channel) - (participation channel)

where:
    gradient channel  = D * integral M(rho) * |grad rho|^2 dV
    penalty channel   = D * integral P(rho)^2 / M(rho) dV
    participation ch. = |H * v * integral (P(rho)/M(rho)) dV|

The ratios R_grad, R_pen, R_part are the fractional contributions
and sum to 1.
"""

from __future__ import annotations

import numpy as np

from ..core.parameters import EDParameters
from ..core.constitutive import mobility, penalty
from .energy import _trapz_2d, _trapz_nd


def _integrate(field: np.ndarray, dx: tuple) -> float:
    """Integrate a field over the domain using composite trapezoidal rule."""
    if field.ndim == 2:
        return _trapz_2d(field, dx)
    else:
        return _trapz_nd(field, dx)


def dissipation_channels(
    rho: np.ndarray,
    v: float,
    params: EDParameters,
) -> dict:
    """Decompose the instantaneous energy dissipation rate into three channels.

    Channels (all non-negative):
        G_int = D * integral M(rho) * |grad rho|^2 dV    (gradient diffusion)
        Q_int = D * integral P(rho)^2 / M(rho) dV        (penalty relaxation)
        S     = |H * v * integral P(rho)/M(rho) dV|       (participation)

    Ratios:
        R_grad = G_int / (G_int + Q_int + S)
        R_pen  = Q_int / (G_int + Q_int + S)
        R_part = S     / (G_int + Q_int + S)

    Parameters
    ----------
    rho : np.ndarray
        Density field (2D or 3D).
    v : float
        Participation variable.
    params : EDParameters
        Simulation parameters.

    Returns
    -------
    dict
        {"R_grad": float, "R_pen": float, "R_part": float,
         "grad_rate": float, "pen_rate": float, "part_rate": float,
         "total_rate": float}
    """
    dx = params.dx
    D = params.D
    H = params.H
    eps = 1e-30  # guard against division by zero

    # Constitutive fields
    M = mobility(rho, params)
    P = penalty(rho, params)

    # Gradient of rho: |grad rho|^2
    d = rho.ndim
    grad_sq = np.zeros_like(rho)
    for axis in range(d):
        g = np.gradient(rho, dx[axis], axis=axis)
        grad_sq += g ** 2

    # Gradient channel integrand: M(rho) * |grad rho|^2
    G_field = M * grad_sq
    G_int = D * _integrate(G_field, dx)

    # Penalty channel integrand: P(rho)^2 / M(rho)
    # Guard M > 0 to avoid division by zero near rho_max
    M_safe = np.where(M > eps, M, eps)
    Q_field = P ** 2 / M_safe
    Q_int = D * _integrate(Q_field, dx)

    # Participation channel: |H * v * integral(P/M) dV|
    # P/M is the "chemical potential gradient" that v couples to
    Phi_prime_field = P / M_safe
    Phi_prime_int = _integrate(Phi_prime_field, dx)
    S = abs(H * v * Phi_prime_int)

    # Total dissipation rate
    total = G_int + Q_int + S

    # Ratios (guard against zero total at equilibrium)
    if total < eps:
        R_grad = 1.0 / 3.0
        R_pen = 1.0 / 3.0
        R_part = 1.0 / 3.0
    else:
        R_grad = G_int / total
        R_pen = Q_int / total
        R_part = S / total

    return {
        "R_grad": float(R_grad),
        "R_pen": float(R_pen),
        "R_part": float(R_part),
        "grad_rate": float(G_int),
        "pen_rate": float(Q_int),
        "part_rate": float(S),
        "total_rate": float(total),
    }


def dissipation_rate_total(rho: np.ndarray, v: float, params: EDParameters) -> float:
    """Compute the total energy dissipation rate |dE/dt|.

    Parameters
    ----------
    rho : np.ndarray
        Density field.
    v : float
        Participation variable.
    params : EDParameters
        Simulation parameters.

    Returns
    -------
    float
        Absolute dissipation rate.
    """
    channels = dissipation_channels(rho, v, params)
    return channels["total_rate"]
