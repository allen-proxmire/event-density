"""
ED-Phys-02: Simulation Parameters and Configuration
=====================================================
Canonical sources: ED-Phys-01 (Update Rule), ED-12, ED-12.5

All parameter names, defaults, and constraints trace directly to
ED-Phys-01 Sections 7, 8, and 12.
"""

from dataclasses import dataclass, field
from typing import Literal
import numpy as np


@dataclass
class EDParams:
    """Complete parameter set for the ED cosmology simulator.

    Every field maps to a named quantity in ED-Phys-01_UpdateRule.md.
    """

    # --- Physics: Relational Penalty (ED-12 §3.1) ---
    alpha: float = 0.1
    """Relational penalty coupling strength (α > 0)."""

    gamma_exp: float = 0.5
    """Concavity exponent in f(ρ) = ρ^γ_exp.  Must satisfy 0 < γ_exp < 1.
    Controls structure formation: lower → weaker instability,
    higher → nearly linear (loses concave amplification)."""

    # --- Physics: Mobility / Diffusion (ED-12.5 §4.1) ---
    M_0: float = 1.0
    """Bare mobility (maximum diffusion rate, at ρ = 0)."""

    rho_max: float = 100.0
    """Saturation density ceiling.  M(ρ) → 0 as ρ → ρ_max.
    Sets the horizon / black-hole scale."""

    n_mob: int = 2
    """Mobility exponent: M(ρ) = M_0 · (1 − ρ/ρ_max)^n_mob.
    Higher → sharper saturation cutoff."""

    # --- Physics: Boundary Penalty (ED-12 §3.3) ---
    gamma_b: float = 0.0
    """Boundary penalty coupling.  Set to 0 for bulk-only cosmological runs
    with periodic BCs (boundary term is identically zero)."""

    h_max: float = 1.0
    """Saturation ceiling for boundary function h(u) = h_max·u/(u+u_0)."""

    u_0: float = 1.0
    """Half-saturation gradient scale for boundary function."""

    # --- Numerics ---
    dimensions: Literal[1, 2] = 1
    """Lattice dimensionality: 1 or 2."""

    N: int = 256
    """Lattice size.  1D: N sites.  2D: N×N grid."""

    dx: float = 1.0
    """Grid spacing (normalized)."""

    eta: float | None = None
    """Timestep.  If None, auto-set to 10% of CFL limit."""

    cfl_safety: float = 0.1
    """Fraction of CFL limit to use for auto-timestep (default 10%)."""

    eps: float = 1e-10
    """Density floor to prevent divergence in ρ^(γ_exp − 1)."""

    n_steps: int = 10000
    """Number of time steps to run."""

    record_interval: int = 100
    """Record diagnostics every this many steps."""

    boundary: Literal["periodic", "absorbing", "reflecting"] = "periodic"
    """Boundary condition type."""

    rho_min_absorbing: float = 0.01
    """Fixed density at absorbing boundaries (if used)."""

    # --- Early Stopping ---
    early_stop_gradient: float | None = None
    """Stop simulation if mean |∇ρ| drops below this threshold.
    None = no early stopping."""

    def __post_init__(self):
        """Validate constraints and auto-compute timestep."""
        assert 0 < self.gamma_exp < 1, \
            f"gamma_exp must be in (0,1), got {self.gamma_exp}"
        assert self.alpha > 0, f"alpha must be > 0, got {self.alpha}"
        assert self.M_0 > 0, f"M_0 must be > 0, got {self.M_0}"
        assert self.rho_max > 0, f"rho_max must be > 0, got {self.rho_max}"
        assert self.n_mob >= 1, f"n_mob must be >= 1, got {self.n_mob}"
        assert self.dimensions in (1, 2), \
            f"dimensions must be 1 or 2, got {self.dimensions}"

        if self.eta is None:
            self.eta = self._compute_cfl_timestep()

    def _compute_cfl_timestep(self) -> float:
        """Compute timestep from combined stability criterion (ED-Phys-01 §8.3).

        η < min(
            Δx² / (2D · M_0),                  ... diffusion CFL
            ε^{1−γ_exp} / (α · γ_exp)          ... relational term bound
        )
        """
        D = self.dimensions
        cfl_diffusion = self.dx ** 2 / (2 * D * self.M_0)
        cfl_relational = self.eps ** (1 - self.gamma_exp) / \
            (self.alpha * self.gamma_exp)
        eta_max = min(cfl_diffusion, cfl_relational)
        return self.cfl_safety * eta_max

    @property
    def grid_shape(self) -> tuple:
        """Return the lattice shape as a tuple."""
        if self.dimensions == 1:
            return (self.N,)
        return (self.N, self.N)


# --- Preset Configurations ---

def default_cosmology_1d(N: int = 256) -> EDParams:
    """ED-Phys-01 §13.3 recommended starting parameters, 1D."""
    return EDParams(
        alpha=0.1,
        gamma_exp=0.5,
        M_0=1.0,
        rho_max=100.0,
        n_mob=2,
        gamma_b=0.0,
        dimensions=1,
        N=N,
        dx=1.0,
        n_steps=10000,
        record_interval=100,
        boundary="periodic",
    )


def default_cosmology_2d(N: int = 128) -> EDParams:
    """ED-Phys-01 §13.3 recommended starting parameters, 2D."""
    return EDParams(
        alpha=0.1,
        gamma_exp=0.5,
        M_0=1.0,
        rho_max=100.0,
        n_mob=2,
        gamma_b=0.0,
        dimensions=2,
        N=N,
        dx=1.0,
        n_steps=10000,
        record_interval=100,
        boundary="periodic",
    )
