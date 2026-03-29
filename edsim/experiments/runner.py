"""
edsim.experiments.runner — Core simulation runner.

Defines RunConfig, TimeSeries, and the unified run_simulation() entry point.
Computes the invariant atlas (energy, complexity, mass) at each snapshot.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

import numpy as np

from ..core.parameters import EDParameters
from ..core.constitutive import enforce_bounds
from ..core.integrators.base import get_integrator
from ..invariants.atlas import compute_atlas


@dataclass
class RunConfig:
    """Complete specification of a simulation run.

    Attributes
    ----------
    params : EDParameters
        Simulation parameters.
    ic_type : str
        Initial condition type: "cosine", "random", "gaussian", "custom".
    ic_kwargs : dict
        IC-specific arguments (e.g., A, Nm, sigma).
    output_dir : str
        Output directory for results.
    save_checkpoints : bool
        Whether to save periodic checkpoints.
    checkpoint_interval : int
        Save checkpoint every N steps.
    """

    params: EDParameters
    ic_type: str = "cosine"
    ic_kwargs: dict = field(default_factory=lambda: {"A": 0.03, "Nm": 2})
    output_dir: str = "./output"
    save_checkpoints: bool = False
    checkpoint_interval: int = 1000


@dataclass
class TimeSeries:
    """Storage for simulation output.

    Attributes
    ----------
    times : list[float]
        Time values at each output step.
    fields : list[np.ndarray]
        Density field snapshots.
    v_history : list[float]
        Participation variable at each output step.
    energy : list[float]
        Lyapunov energy E[rho] at each output step.
    complexity : list[float]
        ED-complexity C[rho] at each output step.
    mass : list[float]
        Total mass M[rho] at each output step.
    spectral_entropy : list[float]
        Spectral entropy H at each output step.
    modal_hierarchy : list
        Sorted modal amplitudes at each output step.
    morphology_fractions : list[dict]
        Morphology fractions {blob, sheet, filament} at each output step.
    R_grad : list[float]
        Gradient dissipation fraction at each output step.
    R_pen : list[float]
        Penalty dissipation fraction at each output step.
    R_part : list[float]
        Participation dissipation fraction at each output step.
    correlation_length : list[float]
        Correlation length xi at each output step.
    structure_r : list[np.ndarray]
        Radial bin centres for S_2(r) at each output step.
    structure_S2 : list[np.ndarray]
        Second-order structure function values at each output step.
    euler_characteristic : list[int]
        Euler characteristic chi at each output step.
    betti_numbers : list[list[int]]
        Betti numbers [beta_0, ...] at each output step.
    """

    times: list = field(default_factory=list)
    fields: list = field(default_factory=list)
    v_history: list = field(default_factory=list)
    energy: list = field(default_factory=list)
    complexity: list = field(default_factory=list)
    mass: list = field(default_factory=list)
    spectral_entropy: list = field(default_factory=list)
    modal_hierarchy: list = field(default_factory=list)
    morphology_fractions: list = field(default_factory=list)
    R_grad: list = field(default_factory=list)
    R_pen: list = field(default_factory=list)
    R_part: list = field(default_factory=list)
    correlation_length: list = field(default_factory=list)
    structure_r: list = field(default_factory=list)
    structure_S2: list = field(default_factory=list)
    euler_characteristic: list = field(default_factory=list)
    betti_numbers: list = field(default_factory=list)


def _record_snapshot(
    series: TimeSeries,
    t: float,
    rho: np.ndarray,
    v: float,
    params: EDParameters,
) -> None:
    """Record a single snapshot into the TimeSeries.

    Computes the invariant atlas and appends all data.

    Parameters
    ----------
    series : TimeSeries
        Output storage to append to.
    t : float
        Current time.
    rho : np.ndarray
        Current density field.
    v : float
        Current participation variable.
    params : EDParameters
        Simulation parameters.
    """
    atlas = compute_atlas(rho, v, params)
    series.times.append(t)
    series.fields.append(rho.copy())
    series.v_history.append(v)
    series.energy.append(atlas["energy"])
    series.complexity.append(atlas["complexity"])
    series.mass.append(atlas["mass"])
    series.spectral_entropy.append(atlas["spectral_entropy"])
    series.modal_hierarchy.append(atlas["modal_hierarchy"])
    series.morphology_fractions.append(atlas["morphology_fractions"])
    series.R_grad.append(atlas["R_grad"])
    series.R_pen.append(atlas["R_pen"])
    series.R_part.append(atlas["R_part"])
    series.correlation_length.append(atlas["correlation_length"])
    series.structure_r.append(atlas["structure_r"])
    series.structure_S2.append(atlas["structure_S2"])
    series.euler_characteristic.append(atlas["euler_characteristic"])
    series.betti_numbers.append(atlas["betti_numbers"])


def generate_ic(
    ic_type: str,
    grid: tuple,
    params: EDParameters,
    **kwargs,
) -> np.ndarray:
    """Generate initial condition for rho.

    Parameters
    ----------
    ic_type : str
        "cosine", "random", "gaussian", or "custom".
    grid : tuple
        Coordinate arrays from params.make_grid().
    params : EDParameters
        Simulation parameters.
    **kwargs
        IC-specific: A (amplitude), Nm (modes per axis), sigma, field.

    Returns
    -------
    np.ndarray
        Initial density field of shape params.N.
    """
    A = kwargs.get("A", 0.03)
    Nm = kwargs.get("Nm", 2)

    if ic_type == "cosine":
        # Build meshgrid from 1D coordinate arrays
        if params.d == 1:
            x = grid[0]
            rho = np.full_like(x, params.rho_star)
            for k in range(1, Nm + 1):
                rho += A * np.cos(k * np.pi * x / params.L[0])
            return enforce_bounds(rho, params)

        elif params.d == 2:
            x, y = grid
            X, Y = np.meshgrid(x, y, indexing="ij")
            rho = np.full_like(X, params.rho_star)
            for kx in range(Nm + 1):
                for ky in range(Nm + 1):
                    if kx == 0 and ky == 0:
                        continue
                    rho += A * (
                        np.cos(kx * np.pi * X / params.L[0])
                        * np.cos(ky * np.pi * Y / params.L[1])
                    )
            return enforce_bounds(rho, params)

        else:
            # Generic d-dimensional cosine IC
            coords = np.meshgrid(*grid, indexing="ij")
            rho = np.full(params.N, params.rho_star)
            mode_range = range(Nm + 1)
            import itertools
            for k_vec in itertools.product(mode_range, repeat=params.d):
                if all(k == 0 for k in k_vec):
                    continue
                mode = np.ones(params.N)
                for axis, k in enumerate(k_vec):
                    mode *= np.cos(k * np.pi * coords[axis] / params.L[axis])
                rho += A * mode
            return enforce_bounds(rho, params)

    elif ic_type == "random":
        rng = np.random.default_rng(params.seed)
        rho = params.rho_star + A * (2.0 * rng.random(params.N) - 1.0)
        return enforce_bounds(rho, params)

    elif ic_type == "gaussian":
        sigma = kwargs.get("sigma", 0.1)
        coords = np.meshgrid(*grid, indexing="ij")
        r2 = np.zeros(params.N)
        for axis in range(params.d):
            center = params.L[axis] / 2.0
            r2 += (coords[axis] - center) ** 2
        rho = params.rho_star + A * np.exp(-r2 / (2.0 * sigma ** 2))
        return enforce_bounds(rho, params)

    elif ic_type == "custom":
        return kwargs["field"].copy()

    else:
        raise ValueError(f"Unknown IC type: {ic_type}")


def run_simulation(config: RunConfig) -> TimeSeries:
    """Execute a single ED simulation with invariant tracking.

    Parameters
    ----------
    config : RunConfig
        Full run specification.

    Returns
    -------
    TimeSeries
        Simulation output (times, fields, v, energy, complexity, mass).
    """
    params = config.params
    grid = params.make_grid()

    # Generate initial condition
    rho = generate_ic(config.ic_type, grid, params, **config.ic_kwargs)

    # Set up integrator via factory (dispatches on params.method)
    integrator = get_integrator(params)
    state = integrator.setup(params)

    # Participation variable
    v = 0.0

    # Output storage
    series = TimeSeries()

    # Store initial state with invariants
    _record_snapshot(series, 0.0, rho, v, params)

    # Time-stepping loop
    t = 0.0
    for step_idx in range(1, params.n_steps + 1):
        rho, v, state = integrator.step(rho, v, t, params, state)
        t = step_idx * params.dt

        # Store snapshot every k_out steps
        if step_idx % params.k_out == 0:
            _record_snapshot(series, t, rho, v, params)

    # Always store final state if not already stored
    if len(series.times) == 0 or abs(series.times[-1] - t) > 1e-15:
        _record_snapshot(series, t, rho, v, params)

    return series
