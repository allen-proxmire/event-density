"""
ED-Phys-02: Core Simulation Engine
=====================================
Canonical source: ED-Phys-01 §6, §7.5, §8, §11

Implements the explicit update rule:

    ρ_{t+1}(x) = ρ_t(x) + η · [
        M(ρ)·∇²ρ  +  M'(ρ)·|∇ρ|²  −  α·γ_exp·max(ρ, ε)^{γ_exp − 1}
    ]

with positivity enforcement and CFL-bounded timestep.
"""

import numpy as np
from dataclasses import dataclass, field
from typing import Any

from ed_phys_config import EDParams
from ed_phys_operators import (
    discrete_laplacian,
    discrete_grad_squared,
    discrete_grad_magnitude,
    mobility,
    mobility_derivative,
)


@dataclass
class DiagnosticRecord:
    """One snapshot of simulation observables (ED-Phys-01 §9)."""
    step: int
    rho_total: float        # Σ ρ_i
    rho_mean: float         # (1/N) Σ ρ_i
    rho_max: float          # max_i ρ_i
    rho_min: float          # min_i ρ_i
    grad_mean: float        # (1/N) Σ |∇ρ|_i
    grad_max: float         # max_i |∇ρ|_i
    grad_energy: float      # Σ |∇ρ|²_i
    thinning_rate: float    # Δ(Σρ) since last record
    n_basins: int           # number of local minima (1D) or local min regions (2D)


@dataclass
class SimulationResult:
    """Complete output of a simulation run."""
    rho_final: np.ndarray
    history: list[DiagnosticRecord]
    params: EDParams
    rho_snapshots: list[np.ndarray] = field(default_factory=list)
    """Selected full-field snapshots for visualization."""
    converged: bool = False
    """True if early-stopping triggered."""
    final_step: int = 0


def _count_basins_1d(rho: np.ndarray) -> int:
    """Count local minima in a 1D field (with periodic wrapping)."""
    N = len(rho)
    count = 0
    for i in range(N):
        left = rho[(i - 1) % N]
        right = rho[(i + 1) % N]
        if rho[i] < left and rho[i] < right:
            count += 1
    return count


def _count_basins_2d(rho: np.ndarray) -> int:
    """Count local minima in a 2D field (with periodic wrapping).

    A cell is a local minimum if it is strictly less than all 4 neighbors.
    """
    N = rho.shape[0]
    padded = np.pad(rho, 1, mode='wrap')
    center = padded[1:-1, 1:-1]
    is_min = (
        (center < padded[:-2, 1:-1]) &   # above
        (center < padded[2:, 1:-1]) &     # below
        (center < padded[1:-1, :-2]) &    # left
        (center < padded[1:-1, 2:])       # right
    )
    return int(np.sum(is_min))


def _count_basins(rho: np.ndarray) -> int:
    """Count local minima / basins in the density field."""
    if rho.ndim == 1:
        return _count_basins_1d(rho)
    return _count_basins_2d(rho)


def simulate(
    params: EDParams,
    initial_rho: np.ndarray,
    snapshot_interval: int | None = None,
) -> SimulationResult:
    """Run the ED cosmology simulation.

    Parameters
    ----------
    params : EDParams
        Full parameter set.
    initial_rho : np.ndarray
        Initial density field, shape matching params.grid_shape.
    snapshot_interval : int or None
        If set, store full rho snapshots every this many steps.
        Useful for visualization. None = no snapshots stored.

    Returns
    -------
    SimulationResult
        Contains final field, diagnostic history, and metadata.
    """
    assert initial_rho.shape == params.grid_shape, (
        f"IC shape {initial_rho.shape} != grid shape {params.grid_shape}"
    )

    # Unpack parameters
    alpha = params.alpha
    gamma_exp = params.gamma_exp
    M_0 = params.M_0
    rho_max_param = params.rho_max
    n_mob = params.n_mob
    eta = params.eta
    dx = params.dx
    eps = params.eps
    boundary = params.boundary
    rho_min_abs = params.rho_min_absorbing

    # Initialize
    rho = initial_rho.astype(np.float64).copy()
    history: list[DiagnosticRecord] = []
    snapshots: list[np.ndarray] = []
    prev_total = float(np.sum(rho))
    converged = False
    final_step = 0

    for t in range(params.n_steps):

        # --- 1. Compute discrete Laplacian (ED-Phys-01 §7.2) ---
        lap = discrete_laplacian(rho, dx, boundary, rho_min_abs)

        # --- 2. Compute |∇ρ|² (ED-Phys-01 §7.2) ---
        grad_sq = discrete_grad_squared(rho, dx, boundary, rho_min_abs)

        # --- 3. Mobility M(ρ) (ED-Phys-01 §7.3) ---
        M = mobility(rho, M_0, rho_max_param, n_mob)

        # --- 4. Mobility derivative M'(ρ) (ED-Phys-01 §7.4) ---
        M_prime = mobility_derivative(rho, M_0, rho_max_param, n_mob)

        # --- 5. Relational penalty derivative (ED-Phys-01 §5.1) ---
        rho_safe = np.maximum(rho, eps)
        rel_penalty = alpha * gamma_exp * rho_safe ** (gamma_exp - 1.0)

        # --- 6. Assemble RHS (ED-Phys-01 §7.5) ---
        drho = M * lap + M_prime * grad_sq - rel_penalty

        # --- 7. Explicit Euler update ---
        rho = rho + eta * drho

        # --- 8. Enforce positivity (ED-Phys-01 §8.4) ---
        np.clip(rho, 0.0, None, out=rho)

        final_step = t + 1

        # --- 9. Record diagnostics ---
        if t % params.record_interval == 0:
            current_total = float(np.sum(rho))
            grad_mag = np.sqrt(grad_sq)

            rec = DiagnosticRecord(
                step=t,
                rho_total=current_total,
                rho_mean=float(np.mean(rho)),
                rho_max=float(np.max(rho)),
                rho_min=float(np.min(rho)),
                grad_mean=float(np.mean(grad_mag)),
                grad_max=float(np.max(grad_mag)),
                grad_energy=float(np.sum(grad_sq)),
                thinning_rate=current_total - prev_total,
                n_basins=_count_basins(rho),
            )
            history.append(rec)
            prev_total = current_total

        # --- 10. Store snapshot ---
        if snapshot_interval and t % snapshot_interval == 0:
            snapshots.append(rho.copy())

        # --- 11. Early stopping ---
        if params.early_stop_gradient is not None:
            mean_grad = float(np.mean(np.sqrt(grad_sq)))
            if mean_grad < params.early_stop_gradient:
                converged = True
                break

    return SimulationResult(
        rho_final=rho,
        history=history,
        params=params,
        rho_snapshots=snapshots,
        converged=converged,
        final_step=final_step,
    )
