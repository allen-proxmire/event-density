"""
edsim.phys.energy_regime — Energy, entropy, and Lyapunov structure of ED.

The canonical ED PDE (with H=0) possesses a Lyapunov functional:

    E[rho] = integral Phi(rho) dV

where the density potential is

    Phi(rho) = integral_{rho*}^{rho} P(s) / M(s) ds.

The time derivative satisfies

    dE/dt = -D integral (P/M)' M |grad rho|^2 dV  -  D integral P^2/M dV
          <= 0

Both integrands are non-negative (for rho near rho_star), so E is
monotonically non-increasing.  This is Law 2.

For H > 0, the participation term +H v adds a signed contribution
to dE/dt that can be positive, so E is NOT monotone in general.

GRADIENT-FLOW STRUCTURE:

The H=0 PDE is NOT exactly a gradient flow of E.  The gradient flow
would be rho_t = div(M grad(delta E / delta rho)) = div(M grad(P/M)),
which differs from the ED operator div(M grad rho) - P by higher-order
gradient terms.  However, the dissipation inequality dE/dt <= 0 still
holds.

ENTROPY:

The Boltzmann entropy S[rho] = -integral rho log rho dV is NOT
monotone under the ED flow.  ED is not a detailed-balance system.

This module defines the candidate functionals and tests their
properties numerically.
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import Optional

import numpy as np

from ..core.parameters import EDParameters
from ..core.constitutive import mobility, penalty, density_potential


# ---------------------------------------------------------------
# Candidate functionals
# ---------------------------------------------------------------

def lyapunov_energy(rho: np.ndarray, params: EDParameters) -> float:
    """Compute E[rho] = integral Phi(rho) dV using the existing density_potential."""
    phi = density_potential(rho, params)
    dx_prod = 1.0
    for i in range(params.d):
        dx_prod *= params.dx[i]
    return float(np.sum(phi)) * dx_prod


def gradient_energy(rho: np.ndarray, params: EDParameters) -> float:
    """E_grad = integral |grad rho|^2 dV (= ED-complexity)."""
    dx = [params.dx[i] for i in range(params.d)]
    grads = np.gradient(rho - params.rho_star, *dx)
    grad_sq = sum(g ** 2 for g in grads)
    dx_prod = 1.0
    for i in range(params.d):
        dx_prod *= params.dx[i]
    return float(np.sum(grad_sq)) * dx_prod


def penalty_energy(rho: np.ndarray, params: EDParameters) -> float:
    """E_pen = integral (rho - rho_star)^2 dV."""
    delta = rho - params.rho_star
    dx_prod = 1.0
    for i in range(params.d):
        dx_prod *= params.dx[i]
    return float(np.sum(delta ** 2)) * dx_prod


def participation_energy(v: float) -> float:
    """E_part = v^2 / 2."""
    return 0.5 * v ** 2


def boltzmann_entropy(rho: np.ndarray, params: EDParameters) -> float:
    """S[rho] = -integral rho log(rho) dV. Clamp rho > eps for log."""
    rho_safe = np.clip(rho, 1e-30, None)
    integrand = -rho_safe * np.log(rho_safe)
    dx_prod = 1.0
    for i in range(params.d):
        dx_prod *= params.dx[i]
    return float(np.sum(integrand)) * dx_prod


def fisher_information(rho: np.ndarray, params: EDParameters) -> float:
    """I[rho] = integral |grad rho|^2 / rho dV (Fisher information)."""
    rho_safe = np.clip(rho, 1e-30, None)
    dx = [params.dx[i] for i in range(params.d)]
    grads = np.gradient(rho, *dx)
    grad_sq = sum(g ** 2 for g in grads)
    integrand = grad_sq / rho_safe
    dx_prod = 1.0
    for i in range(params.d):
        dx_prod *= params.dx[i]
    return float(np.sum(integrand)) * dx_prod


def free_energy(rho: np.ndarray, params: EDParameters, kappa: float = 0.01) -> float:
    """F[rho] = E_Lyapunov + kappa * E_gradient (Ginzburg-Landau-type)."""
    return lyapunov_energy(rho, params) + kappa * gradient_energy(rho, params)


# ---------------------------------------------------------------
# Energy regime specification
# ---------------------------------------------------------------

@dataclass(frozen=True)
class EnergyRegime:
    """Specification of a regime for energy/entropy testing.

    Attributes
    ----------
    name : str
    parameters : EDParameters
    description : str
    H_zero : bool
        Whether H = 0 (Lyapunov monotonicity guaranteed).
    """

    name: str
    parameters: EDParameters
    description: str
    H_zero: bool


def build_energy_regime(
    d: int = 2,
    N: int = 64,
    H: float = 0.0,
    T: float = 3.0,
    dt: float = 5e-4,
) -> EnergyRegime:
    """Build a regime for energy/Lyapunov testing.

    Parameters
    ----------
    d : int
    N : int
    H : float
        Participation coupling. Set to 0 for guaranteed Lyapunov monotonicity.
    T : float
    dt : float

    Returns
    -------
    EnergyRegime
    """
    params = EDParameters(
        d=d, L=tuple(1.0 for _ in range(d)), N=tuple(N for _ in range(d)),
        D=0.3, H=H, zeta=0.1, tau=1.0,
        rho_star=0.5, rho_max=1.0, M0=1.0, beta=2.0, P0=1.0,
        dt=dt, T=T, method="implicit_euler", bc="neumann",
        k_out=max(1, int(T / dt) // 50), seed=42,
    )

    desc = (
        f"Energy regime in {d}D: H={H} "
        f"({'Lyapunov monotone guaranteed' if H == 0 else 'Lyapunov NOT guaranteed'})."
    )

    return EnergyRegime(name=f"energy_{d}d", parameters=params,
                        description=desc, H_zero=(H == 0.0))
