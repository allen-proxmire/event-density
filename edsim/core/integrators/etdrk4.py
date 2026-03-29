"""
edsim.core.integrators.etdrk4 — Exponential Time Differencing RK4.

Treats the linear part of the ED PDE exactly via matrix exponentials
in spectral space, and integrates the nonlinear remainder with a
4-stage explicit Runge-Kutta scheme.

Currently supports d = 2 with Neumann BCs (DCT-II basis).

The splitting is:
    d(rho)/dt = L*rho + N(rho, v)

where:
    L*rho  = D * (-M_star * mu_k - P0) * rho_hat_k   (in spectral space)
    N(rho) = D * [(M(rho) - M_star)*Lap(rho) + M'(rho)*|grad rho|^2
                  - (P(rho) - P0*rho)] + H*v           (in physical space)

The linear operator L is integrated exactly; N is treated explicitly.
"""

from __future__ import annotations

from typing import Any

import numpy as np

from ..parameters import EDParameters
from ..spectral import (
    SpectralState,
    build_spectral_state,
    forward_transform_2d,
    inverse_transform_2d,
)
from ..constitutive import mobility, mobility_deriv, penalty, enforce_bounds
from ..participation import advance_v, spatial_average
from ..operators import grad_squared_fd_2d


class ETDRK4Integrator:
    """ETD-RK4 spectral integrator for 2D Neumann problems.

    Attributes
    ----------
    sstate : SpectralState or None
        Precomputed spectral data. Set by ``setup()``.
    """

    def __init__(self) -> None:
        self.sstate: SpectralState | None = None

    def setup(self, params: EDParameters) -> SpectralState:
        """Precompute spectral state (eigenvalues, ETD coefficients).

        Parameters
        ----------
        params : EDParameters
            Simulation parameters (must have d == 2).

        Returns
        -------
        SpectralState
            Precomputed data, also stored as self.sstate.
        """
        self.sstate = build_spectral_state(params)
        return self.sstate

    def _spectral_laplacian(self, rho: np.ndarray) -> np.ndarray:
        """Compute the Laplacian of rho using spectral (DCT) eigenvalues.

        This ensures consistency between the linear part (handled by the
        exponential integrator) and the nonlinear part.

        Parameters
        ----------
        rho : np.ndarray
            Density field in physical space, shape (Nx, Ny).

        Returns
        -------
        np.ndarray
            Laplacian in physical space, same shape.
        """
        rho_hat = forward_transform_2d(rho)
        lap_hat = -self.sstate.eigenvalues * rho_hat
        return inverse_transform_2d(lap_hat)

    def _nonlinear_rhs(
        self,
        rho: np.ndarray,
        v: float,
        params: EDParameters,
    ) -> np.ndarray:
        """Compute the nonlinear remainder N(rho, v) in spectral space.

        The splitting is:
            full RHS = L*rho + N(rho, v)

        where L*rho = -D*(M_star*mu_k + P0)*rho_hat  (in spectral space)

        So in physical space:
            N(rho) = D * [M(rho)*Lap(rho) + M'(rho)*|grad rho|^2 - P(rho)]
                   + H*v
                   - L*rho   (subtract the linear part)

        Equivalently:
            N(rho) = D * [(M(rho) - M_star)*Lap(rho) + M'(rho)*|grad rho|^2
                        - (P(rho) - P0*rho)]
                   + H*v

        IMPORTANT: Uses the spectral Laplacian (not FD) so the splitting
        is exactly consistent with the linear exponential integrator.

        Parameters
        ----------
        rho : np.ndarray
            Density field in physical space, shape (Nx, Ny).
        v : float
            Participation variable.
        params : EDParameters
            Simulation parameters.

        Returns
        -------
        np.ndarray
            N(rho, v) in spectral space, shape (Nx, Ny).
        """
        D = params.D
        H = params.H
        M_star = params.M_star
        P0 = params.P0

        # Constitutive fields
        M = mobility(rho, params)
        Mp = mobility_deriv(rho, params)
        P = penalty(rho, params)

        # Spectral Laplacian (consistent with the linear part)
        lap = self._spectral_laplacian(rho)

        # Gradient squared (FD is fine here — it's only in the nonlinear term
        # and the gradient is not part of the linear splitting)
        gs = grad_squared_fd_2d(rho, params.dx)

        # Nonlinear remainder in physical space
        N_phys = D * (
            (M - M_star) * lap
            + Mp * gs
            - (P - P0 * rho)
        ) + H * v

        # Transform to spectral space
        return forward_transform_2d(N_phys)

    def step(
        self,
        rho: np.ndarray,
        v: float,
        t: float,
        params: EDParameters,
        state: SpectralState,
    ) -> tuple[np.ndarray, float, SpectralState]:
        """Advance one ETD-RK4 step for the coupled (rho, v) system.

        The 4-stage ETD-RK4 scheme (Cox-Matthews / Kassam-Trefethen):

            N_u = N(u)
            a = E2*u_hat + f1*N_u                          [half step]
            N_a = N(IDCT(a))
            b = E2*u_hat + f1*N_a                          [half step]
            N_b = N(IDCT(b))
            c = E2*a + f1*(2*N_b - N_u)                    [half step from a]
            N_c = N(IDCT(c))
            u_new = E*u_hat + f1*N_u + 2*f2*(N_a + N_b) + f3*N_c  [full step]

        Parameters
        ----------
        rho : np.ndarray
            Current density field in physical space.
        v : float
            Current participation variable.
        t : float
            Current time.
        params : EDParameters
            Simulation parameters.
        state : SpectralState
            Precomputed spectral data.

        Returns
        -------
        tuple[np.ndarray, float, SpectralState]
            (rho_new, v_new, state) — state is unchanged.
        """
        ss = state
        E = ss.E
        E2 = ss.E2
        Q = ss.Q      # half-step nonlinear weight
        f1 = ss.f1    # full-step combination coefficients
        f2 = ss.f2
        f3 = ss.f3

        # Current state in spectral space
        u_hat = forward_transform_2d(rho)

        # Stage 1: evaluate N at current state
        N_u = self._nonlinear_rhs(rho, v, params)

        # Stage 2: half-step prediction a (Euler with half-step exp)
        a_hat = E2 * u_hat + Q * N_u
        a_phys = inverse_transform_2d(a_hat)
        a_phys = enforce_bounds(a_phys, params)
        N_a = self._nonlinear_rhs(a_phys, v, params)

        # Stage 3: half-step prediction b (Euler from u with N_a)
        b_hat = E2 * u_hat + Q * N_a
        b_phys = inverse_transform_2d(b_hat)
        b_phys = enforce_bounds(b_phys, params)
        N_b = self._nonlinear_rhs(b_phys, v, params)

        # Stage 4: full-step prediction c (half-step from a with 2*N_b - N_u)
        c_hat = E2 * a_hat + Q * (2.0 * N_b - N_u)
        c_phys = inverse_transform_2d(c_hat)
        c_phys = enforce_bounds(c_phys, params)
        N_c = self._nonlinear_rhs(c_phys, v, params)

        # Combine: Cox-Matthews ETD-RK4 full-step update
        u_new_hat = E * u_hat + N_u * f1 + 2.0 * (N_a + N_b) * f2 + N_c * f3
        rho_new = inverse_transform_2d(u_new_hat)
        rho_new = enforce_bounds(rho_new, params)

        # Update participation variable v
        # Compute F_local at the new state for F_avg
        M_new = mobility(rho_new, params)
        Mp_new = mobility_deriv(rho_new, params)
        P_new = penalty(rho_new, params)
        lap_new = self._spectral_laplacian(rho_new)
        gs_new = grad_squared_fd_2d(rho_new, params.dx)
        F_local_new = M_new * lap_new + Mp_new * gs_new - P_new
        F_avg = spatial_average(F_local_new, params.dx)
        v_new = advance_v(v, F_avg, params)

        return rho_new, v_new, state
