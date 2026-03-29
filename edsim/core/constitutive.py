"""
edsim.core.constitutive — Constitutive functions for the ED PDE.

Implements the canonical mobility M(rho), penalty P(rho), and density
potential Phi(rho) from ED-Phys-40. All functions are vectorised over
NumPy arrays and are pure (no side effects).
"""

from __future__ import annotations

import numpy as np

from .parameters import EDParameters


def mobility(rho: np.ndarray, params: EDParameters) -> np.ndarray:
    """Compute mobility M(rho) = M0 * (rho_max - rho)^beta.

    Returns
    -------
    np.ndarray
        Mobility values, same shape as ``rho``. Clipped to [0, inf).
    """
    delta = np.clip(params.rho_max - rho, 0.0, None)
    return params.M0 * delta ** params.beta


def mobility_deriv(rho: np.ndarray, params: EDParameters) -> np.ndarray:
    """Compute mobility derivative M'(rho) = -beta * M0 * (rho_max - rho)^(beta-1)."""
    delta = np.clip(params.rho_max - rho, 0.0, None)
    return -params.beta * params.M0 * delta ** (params.beta - 1.0)


def penalty(rho: np.ndarray, params: EDParameters) -> np.ndarray:
    """Compute penalty P(rho) = P0 * (rho - rho_star)."""
    return params.P0 * (rho - params.rho_star)


def penalty_deriv(rho: np.ndarray, params: EDParameters) -> np.ndarray:
    """Compute penalty derivative P'(rho) = P0."""
    return np.full_like(rho, params.P0)


def density_potential(rho: np.ndarray, params: EDParameters) -> np.ndarray:
    """Compute density potential Phi(rho) = integral of P(s)/M(s) ds from rho_star to rho.

    Used in the Lyapunov functional E[rho] = integral of Phi(rho) over Omega.
    For now uses simple trapezoidal quadrature along the rho axis.
    """
    # Numerical quadrature: integrate P(s)/M(s) from rho_star to rho(x)
    n_quad = 64
    result = np.zeros_like(rho)
    flat_rho = rho.ravel()
    for idx in range(flat_rho.size):
        r = flat_rho[idx]
        if abs(r - params.rho_star) < 1e-15:
            continue
        s = np.linspace(params.rho_star, r, n_quad)
        M_s = params.M0 * np.clip(params.rho_max - s, 1e-30, None) ** params.beta
        P_s = params.P0 * (s - params.rho_star)
        integrand = P_s / M_s
        _trapz = getattr(np, 'trapezoid', getattr(np, 'trapz', None))
        result.ravel()[idx] = _trapz(integrand, s)
    return result


def enforce_bounds(rho: np.ndarray, params: EDParameters) -> np.ndarray:
    """Clip density to [0, rho_max]."""
    return np.clip(rho, 0.0, params.rho_max)
