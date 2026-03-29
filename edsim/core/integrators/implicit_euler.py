"""
edsim.core.integrators.implicit_euler — Implicit Euler integrator.

Solves the coupled (rho, v) system for any dimension d:
    rho^{n+1} = rho^n + dt * [D * F_local(rho^{n+1}) + H * v^n]
    v^{n+1}   = exact exponential update using F_avg from rho^{n+1}

The density equation is solved via fixed-point (Picard) iteration.
The participation variable is updated after rho converges.
"""

from __future__ import annotations

from typing import Any

import numpy as np

from ..parameters import EDParameters
from ..operators import operator_F_split_fd
from ..constitutive import enforce_bounds
from ..participation import advance_v, spatial_average


class ImplicitEulerIntegrator:
    """Fully implicit Euler integrator with fixed-point iteration.

    Dimension-agnostic: works for d = 1, 2, 3, 4 via the unified
    operator_F_split_fd dispatcher.
    """

    def __init__(self, tol: float = 1e-6, max_iter: int = 200) -> None:
        """
        Parameters
        ----------
        tol : float
            Fixed-point iteration convergence tolerance (L-inf norm).
        max_iter : int
            Maximum iterations per step.
        """
        self.tol = tol
        self.max_iter = max_iter

    def setup(self, params: EDParameters) -> None:
        """No precomputation needed for implicit Euler."""
        return None

    def step(
        self,
        rho: np.ndarray,
        v: float,
        t: float,
        params: EDParameters,
        state: None = None,
    ) -> tuple[np.ndarray, float, None]:
        """Advance one implicit Euler step for the coupled (rho, v) system.

        Density update (fixed-point iteration):
            rho_{k+1} = rho^n + dt * [D * F_local(rho_k) + H * v^n]

        Participation update (after rho converges):
            F_avg = spatial_average(F_local(rho^{n+1}))
            v^{n+1} = exact exponential integration using F_avg

        Parameters
        ----------
        rho : np.ndarray
            Current density field (2D or 3D).
        v : float
            Current participation variable.
        t : float
            Current time.
        params : EDParameters
            Simulation parameters.
        state : None
            No precomputed state.

        Returns
        -------
        tuple[np.ndarray, float, None]
            (rho_new, v_new, None).
        """
        dt = params.dt

        # --- Step 1: Solve for rho^{n+1} via fixed-point iteration ---
        _, F_total_n = operator_F_split_fd(rho, params, v)

        # Initial guess: explicit Euler prediction
        rho_new = rho + dt * F_total_n
        rho_new = enforce_bounds(rho_new, params)

        # Fixed-point iteration
        for iteration in range(self.max_iter):
            _, F_total_new = operator_F_split_fd(rho_new, params, v)

            rho_next = rho + dt * F_total_new
            rho_next = enforce_bounds(rho_next, params)

            # Check convergence
            diff = np.max(np.abs(rho_next - rho_new))
            rho_new = rho_next

            if diff < self.tol:
                break

        # --- Step 2: Update participation variable v ---
        F_local_final, _ = operator_F_split_fd(rho_new, params, v)
        F_avg = spatial_average(F_local_final, params.dx)
        v_new = advance_v(v, F_avg, params)

        return rho_new, v_new, None
