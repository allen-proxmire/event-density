"""
edsim.core.parameters — Unified parameter specification for ED-SIM-02.

Defines the EDParameters frozen dataclass that fully specifies an ED
simulation across all dimensions d = 1..4. Includes validation,
derived quantities, and canonical defaults from ED-Phys-40.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Optional

import numpy as np


@dataclass(frozen=True)
class EDParameters:
    """Complete specification of an ED simulation.

    Parameters
    ----------
    d : int
        Spatial dimension (1, 2, 3, or 4).
    L : tuple[float, ...]
        Domain size per axis. Length must equal ``d``.
    N : tuple[int, ...]
        Grid points per axis. Length must equal ``d``.
    D : float
        Diffusion weight (direct channel).
    H : float
        Participation coupling strength.
    zeta : float
        Participation damping coefficient.
    tau : float
        Participation timescale.
    rho_star : float
        Penalty equilibrium density.
    rho_max : float
        Capacity bound (upper density limit).
    M0 : float
        Mobility prefactor.
    beta : float
        Mobility exponent.
    P0 : float
        Penalty slope.
    dt : float
        Time step size.
    T : float
        Final simulation time.
    method : str
        Integrator selection.
    bc : str
        Boundary condition type.
    k_out : int
        Output snapshot every ``k_out`` time steps.
    seed : int
        RNG seed for stochastic initial conditions.
    """

    # --- Dimension ---
    d: int = 1

    # --- Domain ---
    L: tuple = (1.0,)
    N: tuple = (128,)

    # --- Constitutive parameters (canonical defaults from ED-Phys-40) ---
    D: float = 0.3
    H: float = 0.15
    zeta: float = 0.1
    tau: float = 1.0
    rho_star: float = 0.5
    rho_max: float = 1.0
    M0: float = 1.0
    beta: float = 2.0
    P0: float = 1.0

    # --- Numerical parameters ---
    dt: float = 1e-4
    T: float = 1.0
    method: str = "implicit_euler"
    bc: str = "neumann"
    k_out: int = 100
    seed: int = 42
    backend: str = "numpy"  # "numpy", "numba", or "jax"

    def __post_init__(self) -> None:
        """Validate parameter constraints."""
        if self.d not in {1, 2, 3, 4}:
            raise ValueError(f"d must be 1, 2, 3, or 4, got {self.d}")
        if len(self.L) != self.d:
            raise ValueError(f"len(L)={len(self.L)} must equal d={self.d}")
        if len(self.N) != self.d:
            raise ValueError(f"len(N)={len(self.N)} must equal d={self.d}")
        if not (0 < self.rho_star < self.rho_max):
            raise ValueError("Need 0 < rho_star < rho_max")
        if self.beta <= 0 or self.M0 <= 0 or self.P0 <= 0:
            raise ValueError("beta, M0, P0 must be positive")
        if self.dt <= 0 or self.T <= 0:
            raise ValueError("dt and T must be positive")

    # --- Derived quantities ---

    @property
    def dx(self) -> tuple:
        """Grid spacing per axis: dx_i = L_i / (N_i - 1) for Neumann."""
        if self.bc == "periodic":
            return tuple(self.L[i] / self.N[i] for i in range(self.d))
        return tuple(self.L[i] / (self.N[i] - 1) for i in range(self.d))

    @property
    def M_star(self) -> float:
        """Equilibrium mobility: M(rho_star) = M0 * (rho_max - rho_star)^beta."""
        return self.M0 * (self.rho_max - self.rho_star) ** self.beta

    @property
    def R_grad_predicted(self) -> float:
        """Predicted gradient-dissipation ratio from ED-Phys-36 formula."""
        dpi2 = self.d * math.pi ** 2
        return dpi2 / (dpi2 + self.P0 ** 2 / self.M_star)

    @property
    def total_grid_points(self) -> int:
        """Total number of grid points: prod(N)."""
        return int(np.prod(self.N))

    @property
    def n_steps(self) -> int:
        """Total number of time steps: ceil(T / dt)."""
        return int(math.ceil(self.T / self.dt))

    def make_grid(self) -> tuple:
        """Construct coordinate arrays for the domain.

        Returns
        -------
        tuple of np.ndarray
            One 1D coordinate array per axis, each of shape (N_i,).
        """
        grids = []
        for i in range(self.d):
            if self.bc == "periodic":
                grids.append(np.linspace(0, self.L[i], self.N[i], endpoint=False))
            else:
                grids.append(np.linspace(0, self.L[i], self.N[i]))
        return tuple(grids)

    def to_dict(self) -> dict:
        """Serialize all parameters to a JSON-compatible dict."""
        return {
            "d": self.d,
            "L": list(self.L),
            "N": list(self.N),
            "D": self.D,
            "H": self.H,
            "zeta": self.zeta,
            "tau": self.tau,
            "rho_star": self.rho_star,
            "rho_max": self.rho_max,
            "M0": self.M0,
            "beta": self.beta,
            "P0": self.P0,
            "dt": self.dt,
            "T": self.T,
            "method": self.method,
            "bc": self.bc,
            "k_out": self.k_out,
            "seed": self.seed,
            "backend": self.backend,
        }

    @classmethod
    def from_dict(cls, d: dict) -> "EDParameters":
        """Reconstruct EDParameters from a dict."""
        d2 = dict(d)
        d2["L"] = tuple(d2["L"])
        d2["N"] = tuple(d2["N"])
        return cls(**d2)
