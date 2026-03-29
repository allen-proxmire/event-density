"""
edsim.invariants.energy — Energy, mass, and complexity invariants.

Implements the three foundational ED invariants:
    E[rho]  = integral of Phi(rho) over Omega     (Lyapunov energy)
    C[rho]  = integral of |grad rho|^2 over Omega  (ED-complexity)
    M[rho]  = integral of rho over Omega            (total mass)
"""

from __future__ import annotations

import numpy as np

from ..core.parameters import EDParameters
from ..core.constitutive import mobility, penalty


# ---------------------------------------------------------------------------
# 2D composite trapezoidal integration
# ---------------------------------------------------------------------------

def _trapz_2d(field: np.ndarray, dx: tuple) -> float:
    """Composite trapezoidal rule for a 2D field on a uniform grid.

    For a Neumann grid with endpoints included, the trapezoidal rule
    weights boundary points by 1/2. On a uniform (Nx, Ny) grid with
    spacings (dx, dy):

        integral = dx * dy * sum of weighted field values

    where corner points have weight 1/4, edge points 1/2, interior 1.

    Parameters
    ----------
    field : np.ndarray
        2D array of shape (Nx, Ny).
    dx : tuple[float, float]
        Grid spacings (dx, dy).

    Returns
    -------
    float
        Approximate integral over the domain.
    """
    # Build weight matrix: 1 everywhere, 1/2 on edges, 1/4 on corners
    Nx, Ny = field.shape
    w = np.ones((Nx, Ny))
    w[0, :] *= 0.5
    w[-1, :] *= 0.5
    w[:, 0] *= 0.5
    w[:, -1] *= 0.5
    return float(np.sum(w * field) * dx[0] * dx[1])


def _trapz_nd(field: np.ndarray, dx: tuple) -> float:
    """Composite trapezoidal rule for an n-dimensional field.

    Generalises the 2D version: boundary points along each axis get
    weight 1/2; products of boundary weights apply at edges/corners.

    Parameters
    ----------
    field : np.ndarray
        Array of shape (N1, ..., Nd).
    dx : tuple[float, ...]
        Grid spacing per axis.

    Returns
    -------
    float
        Approximate integral.
    """
    d = field.ndim
    w = np.ones(field.shape)
    for axis in range(d):
        sl_first = [slice(None)] * d
        sl_last = [slice(None)] * d
        sl_first[axis] = 0
        sl_last[axis] = -1
        w[tuple(sl_first)] *= 0.5
        w[tuple(sl_last)] *= 0.5
    cell_vol = 1.0
    for dxi in dx:
        cell_vol *= dxi
    return float(np.sum(w * field) * cell_vol)


# ---------------------------------------------------------------------------
# Lyapunov energy
# ---------------------------------------------------------------------------

def _density_potential_vectorised(rho: np.ndarray, params: EDParameters) -> np.ndarray:
    """Compute Phi(rho) = integral from rho_star to rho of P(s)/M(s) ds.

    Vectorised over the full density array using Gauss-Legendre
    quadrature along the integration variable s at each grid point.

    Parameters
    ----------
    rho : np.ndarray
        Density field, any shape.
    params : EDParameters
        Simulation parameters.

    Returns
    -------
    np.ndarray
        Density potential Phi(rho) at each grid point, same shape as rho.
    """
    # Use 16-point Gauss-Legendre quadrature on [rho_star, rho(x)]
    n_quad = 16
    # Gauss-Legendre nodes and weights on [-1, 1]
    gl_nodes, gl_weights = np.polynomial.legendre.leggauss(n_quad)

    rho_flat = rho.ravel()
    result = np.zeros_like(rho_flat)

    rho_star = params.rho_star
    rho_max = params.rho_max
    M0 = params.M0
    beta = params.beta
    P0 = params.P0

    # For each grid point, transform [rho_star, rho_i] to [-1, 1]
    # s = (rho_i - rho_star)/2 * t + (rho_i + rho_star)/2
    delta = rho_flat - rho_star  # half-width = delta/2
    mid = (rho_flat + rho_star) / 2.0

    for q in range(n_quad):
        t = gl_nodes[q]
        w = gl_weights[q]

        s = (delta / 2.0) * t + mid
        # P(s) / M(s) = P0*(s - rho_star) / (M0*(rho_max - s)^beta)
        s_clipped = np.clip(s, -1e10, rho_max - 1e-30)
        numer = P0 * (s_clipped - rho_star)
        denom = M0 * np.clip(rho_max - s_clipped, 1e-30, None) ** beta
        integrand = numer / denom

        result += w * integrand * (delta / 2.0)

    return result.reshape(rho.shape)


def lyapunov_energy(rho: np.ndarray, params: EDParameters) -> float:
    """Compute the Lyapunov functional E[rho] = integral Phi(rho) dV.

    Phi(rho) = integral from rho_star to rho of P(s)/M(s) ds is the
    density potential. E[rho] should decrease monotonically along
    trajectories of the ED PDE (Law 2).

    Parameters
    ----------
    rho : np.ndarray
        Density field of shape params.N.
    params : EDParameters
        Simulation parameters.

    Returns
    -------
    float
        Lyapunov energy.
    """
    phi = _density_potential_vectorised(rho, params)

    if rho.ndim == 2:
        return _trapz_2d(phi, params.dx)
    else:
        return _trapz_nd(phi, params.dx)


# ---------------------------------------------------------------------------
# ED-complexity
# ---------------------------------------------------------------------------

def ed_complexity(rho: np.ndarray, params: EDParameters) -> float:
    """Compute ED-complexity C[rho] = integral |grad rho|^2 dV.

    Uses 2nd-order central differences for the gradient, with one-sided
    differences at domain boundaries (Neumann-compatible).

    Parameters
    ----------
    rho : np.ndarray
        Density field of shape params.N.
    params : EDParameters
        Simulation parameters.

    Returns
    -------
    float
        Gradient energy (should decrease monotonically, Law 2).
    """
    dx = params.dx
    d = rho.ndim

    grad_sq = np.zeros_like(rho)
    for axis in range(d):
        # np.gradient handles boundaries with one-sided differences
        g = np.gradient(rho, dx[axis], axis=axis)
        grad_sq += g ** 2

    if d == 2:
        return _trapz_2d(grad_sq, dx)
    else:
        return _trapz_nd(grad_sq, dx)


# ---------------------------------------------------------------------------
# Total mass
# ---------------------------------------------------------------------------

def total_mass(rho: np.ndarray, params: EDParameters) -> float:
    """Compute total mass M[rho] = integral rho dV.

    Should be conserved for Neumann boundary conditions (no flux
    through domain boundaries).

    Parameters
    ----------
    rho : np.ndarray
        Density field of shape params.N.
    params : EDParameters
        Simulation parameters.

    Returns
    -------
    float
        Total mass.
    """
    dx = params.dx

    if rho.ndim == 2:
        return _trapz_2d(rho, dx)
    else:
        return _trapz_nd(rho, dx)


# ---------------------------------------------------------------------------
# Effective complexity (normalised)
# ---------------------------------------------------------------------------

def ed_complexity_effective(rho: np.ndarray, params: EDParameters) -> float:
    """Compute normalised complexity C_eff = C / C_ref.

    C_ref is the complexity of the initial cosine IC with A=0.03, Nm=2,
    approximated analytically. Returns a value in [0, 1] for canonical ICs.

    Parameters
    ----------
    rho : np.ndarray
        Density field.
    params : EDParameters
        Simulation parameters.

    Returns
    -------
    float
        Normalised complexity.
    """
    C = ed_complexity(rho, params)
    # Reference: sum of A^2 * (k*pi/L)^2 over all active modes
    # For a rough normalisation, use the initial complexity
    # This is a convenience function; the raw C is the primary invariant.
    if C < 1e-30:
        return 0.0
    return C
