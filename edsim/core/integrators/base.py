"""
edsim.core.integrators.base — Integrator protocol and factory.

Defines the common interface that all ED time integrators must satisfy,
plus a factory function that returns the appropriate integrator for a
given method name.
"""

from __future__ import annotations

from typing import Any, Protocol, runtime_checkable

import numpy as np

from ..parameters import EDParameters


@runtime_checkable
class Integrator(Protocol):
    """Protocol for ED time integrators.

    All integrators accept (rho, v, t, params, state) and return
    (rho_new, v_new, state_new). The ``state`` argument carries
    integrator-specific data (e.g., SpectralState for ETD-RK4,
    tridiagonal factors for CN).
    """

    def setup(self, params: EDParameters) -> Any:
        """One-time setup: precompute matrices, spectral state, etc.

        Parameters
        ----------
        params : EDParameters
            Simulation parameters.

        Returns
        -------
        Any
            Integrator-specific precomputed state.
        """
        ...

    def step(
        self,
        rho: np.ndarray,
        v: float,
        t: float,
        params: EDParameters,
        state: Any,
    ) -> tuple[np.ndarray, float, Any]:
        """Advance (rho, v) by one time step dt.

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
        state : Any
            Integrator-specific state from ``setup()`` or previous ``step()``.

        Returns
        -------
        tuple[np.ndarray, float, Any]
            ``(rho_new, v_new, state_new)``.
        """
        ...


def get_integrator(params: EDParameters) -> Any:
    """Factory: return an integrator instance for the given parameters.

    Parameters
    ----------
    params : EDParameters
        Simulation parameters. Uses ``params.method`` to select the
        integrator and ``params.d`` to validate dimension support.

    Returns
    -------
    Integrator
        An integrator instance.

    Raises
    ------
    ValueError
        If ``method`` is not recognized or not supported for the
        given dimension.
    """
    method = params.method

    if method == "implicit_euler":
        from .implicit_euler import ImplicitEulerIntegrator
        return ImplicitEulerIntegrator()

    elif method == "etdrk4":
        if params.d != 2:
            raise ValueError(
                f"ETD-RK4 is currently implemented for d=2 only, got d={params.d}. "
                f"Use method='implicit_euler' for d != 2."
            )
        from .etdrk4 import ETDRK4Integrator
        return ETDRK4Integrator()

    elif method == "crank_nicolson":
        from .crank_nicolson import CrankNicolsonIntegrator
        return CrankNicolsonIntegrator()

    else:
        raise ValueError(
            f"Unknown integrator method: '{method}'. "
            f"Choose from: 'implicit_euler', 'etdrk4', 'crank_nicolson'."
        )
