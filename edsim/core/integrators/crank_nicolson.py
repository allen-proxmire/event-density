"""
edsim.core.integrators.crank_nicolson — Crank-Nicolson / ADI integrator.

Secondary integrator for the ED PDE. Uses Crank-Nicolson time stepping
with alternating-direction implicit (ADI) splitting for d >= 2.

In 1D: tridiagonal solve (Thomas algorithm).
In 2D/3D/4D: d sequential tridiagonal solves per step (ADI splitting).
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Optional

import numpy as np

from ..parameters import EDParameters


@dataclass
class CNState:
    """Precomputed data for the Crank-Nicolson integrator.

    Attributes
    ----------
    tri_diags : list[tuple[np.ndarray, np.ndarray, np.ndarray]]
        Tridiagonal matrix factors (lower, main, upper) per axis.
        Each tuple contains arrays for the implicit half of CN.
    """

    tri_diags: list


class CrankNicolsonIntegrator:
    """Crank-Nicolson / ADI finite-difference integrator."""

    def __init__(self) -> None:
        self.cn_state: CNState | None = None

    def setup(self, params: EDParameters) -> CNState:
        """Precompute tridiagonal matrices for implicit solves.

        For each axis i, constructs the matrix for:
            (I - dt/2 * L_i) * rho^{n+1} = (I + dt/2 * L_i) * rho^n + dt * N_explicit

        Parameters
        ----------
        params : EDParameters
            Simulation parameters.

        Returns
        -------
        CNState
            Precomputed tridiagonal factors.
        """
        # TODO: build tridiagonal matrices per axis
        # - use linearised diffusion coefficient D*M_star
        # - incorporate BC ghost-cell structure
        pass

    def step(
        self,
        rho: np.ndarray,
        v: float,
        t: float,
        params: EDParameters,
        state: CNState,
    ) -> tuple[np.ndarray, float, CNState]:
        """Advance one Crank-Nicolson / ADI step.

        For d = 1: single tridiagonal solve.
        For d >= 2: d sequential ADI sub-steps, one per axis.

        Parameters
        ----------
        rho : np.ndarray
            Current density field.
        v : float
            Current participation variable.
        t : float
            Current time.
        params : EDParameters
            Simulation parameters.
        state : CNState
            Precomputed tridiagonal factors.

        Returns
        -------
        tuple[np.ndarray, float, CNState]
            ``(rho_new, v_new, state)`` — state is unchanged.
        """
        # TODO: implement ADI splitting loop
        # For each axis i:
        #   1. Compute explicit RHS from other axes
        #   2. Solve tridiagonal system along axis i
        # Then advance v
        pass


def _solve_tridiagonal(
    lower: np.ndarray,
    main: np.ndarray,
    upper: np.ndarray,
    rhs: np.ndarray,
) -> np.ndarray:
    """Solve a tridiagonal system Ax = rhs using Thomas' algorithm.

    Parameters
    ----------
    lower, main, upper : np.ndarray
        Tridiagonal matrix diagonals.
    rhs : np.ndarray
        Right-hand side vector.

    Returns
    -------
    np.ndarray
        Solution vector.
    """
    # TODO: implement Thomas algorithm or use scipy.linalg.solve_banded
    pass
