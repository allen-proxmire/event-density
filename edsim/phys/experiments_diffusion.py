"""
edsim.phys.experiments_diffusion — Diffusion-regime numerical experiments.

Two canonical experiments:

1. **Gaussian spread** — a localised bump evolves and spreads.  The variance
   of the profile should grow linearly in time if the system is diffusion-like.

2. **Step relaxation** — a smoothed step-function initial condition evolves.
   The profile at later times should approach the complementary error function
   solution of the heat equation.

Both experiments use the DiffusionRegime parameters, override the initial
condition with a custom field, and return a TimeSeries together with
auxiliary profile data needed for the analysis layer.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

import numpy as np

from ..core.parameters import EDParameters
from ..core.constitutive import enforce_bounds
from ..experiments.runner import RunConfig, TimeSeries, run_simulation
from .diffusion_regime import DiffusionRegime, build_diffusion_regime


# ---------------------------------------------------------------
# Data containers for experiment outputs
# ---------------------------------------------------------------

@dataclass
class GaussianSpreadResult:
    """Output of the Gaussian-spread experiment.

    Attributes
    ----------
    regime : DiffusionRegime
        Regime used.
    series : TimeSeries
        Full ED time series.
    times : np.ndarray
        Output times (float array, length S).
    variances : np.ndarray
        Spatial variance <x^2>(t) of (rho - rho_star) at each snapshot.
    peak_values : np.ndarray
        Peak value of (rho - rho_star) at each snapshot.
    sigma0 : float
        Initial Gaussian width (standard deviation).
    A0 : float
        Initial Gaussian amplitude.
    """

    regime: DiffusionRegime
    series: TimeSeries
    times: np.ndarray
    variances: np.ndarray
    peak_values: np.ndarray
    sigma0: float
    A0: float


@dataclass
class StepRelaxationResult:
    """Output of the step-relaxation experiment.

    Attributes
    ----------
    regime : DiffusionRegime
        Regime used.
    series : TimeSeries
        Full ED time series.
    times : np.ndarray
        Output times.
    midline_profiles : list[np.ndarray]
        1D profile along the x-axis (through domain centre) at each snapshot.
    x_coords : np.ndarray
        x-coordinate array for the midline profile.
    step_direction : int
        Axis along which the step is oriented (0 = x).
    """

    regime: DiffusionRegime
    series: TimeSeries
    times: np.ndarray
    midline_profiles: list
    x_coords: np.ndarray
    step_direction: int


# ---------------------------------------------------------------
# Gaussian-spread experiment
# ---------------------------------------------------------------

def _make_gaussian_ic(
    params: EDParameters,
    sigma: float,
    amplitude: float,
) -> np.ndarray:
    """Build a Gaussian bump centred in the domain.

    rho(x) = rho_star + A * exp(-|x - x_c|^2 / (2 sigma^2))
    """
    grid = params.make_grid()
    coords = np.meshgrid(*grid, indexing="ij")
    r2 = np.zeros(params.N)
    for axis in range(params.d):
        centre = params.L[axis] / 2.0
        r2 += (coords[axis] - centre) ** 2
    rho = params.rho_star + amplitude * np.exp(-r2 / (2.0 * sigma ** 2))
    return enforce_bounds(rho, params)


def _compute_variance(
    rho: np.ndarray,
    params: EDParameters,
) -> float:
    """Spatial variance of the perturbation delta_rho = rho - rho_star.

    var = integral( |x - x_c|^2 * delta_rho dV ) / integral( delta_rho dV )

    Uses composite trapezoidal quadrature.
    """
    grid = params.make_grid()
    coords = np.meshgrid(*grid, indexing="ij")
    delta = rho - params.rho_star

    # r^2 from domain centre
    r2 = np.zeros(params.N)
    for axis in range(params.d):
        centre = params.L[axis] / 2.0
        r2 += (coords[axis] - centre) ** 2

    # Trapezoidal weights (uniform grid)
    dx_prod = 1.0
    for i in range(params.d):
        dx_prod *= params.dx[i]

    numerator = float(np.sum(r2 * delta)) * dx_prod
    denominator = float(np.sum(delta)) * dx_prod

    if abs(denominator) < 1e-30:
        return 0.0
    return numerator / denominator


def run_gaussian_spread(
    regime: Optional[DiffusionRegime] = None,
    sigma: float = 0.08,
    amplitude: float = 0.03,
) -> GaussianSpreadResult:
    """Run a Gaussian-spread experiment in the diffusion regime.

    A localised Gaussian bump is initialised at the domain centre
    and evolved under the ED PDE with weak penalty and no participation.
    The spatial variance is tracked at each snapshot.

    Parameters
    ----------
    regime : DiffusionRegime, optional
        If None, the default 2D diffusion regime is built.
    sigma : float
        Initial Gaussian standard deviation (default 0.08).
    amplitude : float
        Initial Gaussian amplitude above rho_star (default 0.03).

    Returns
    -------
    GaussianSpreadResult
        Experiment output with variance time series.
    """
    if regime is None:
        regime = build_diffusion_regime(d=2)

    params = regime.parameters
    ic = _make_gaussian_ic(params, sigma, amplitude)

    config = RunConfig(
        params=params,
        ic_type="custom",
        ic_kwargs={"field": ic},
    )

    series = run_simulation(config)

    # Extract variances and peak values from stored fields
    times_arr = np.array(series.times)
    variances = np.array([_compute_variance(f, params) for f in series.fields])
    peak_values = np.array([
        float(np.max(f - params.rho_star)) for f in series.fields
    ])

    return GaussianSpreadResult(
        regime=regime,
        series=series,
        times=times_arr,
        variances=variances,
        peak_values=peak_values,
        sigma0=sigma,
        A0=amplitude,
    )


# ---------------------------------------------------------------
# Step-relaxation experiment
# ---------------------------------------------------------------

def _make_step_ic(
    params: EDParameters,
    delta: float,
    width: float,
) -> np.ndarray:
    """Build a smoothed step profile along the first axis.

    rho(x) = rho_star + delta * tanh((x - L/2) / width)

    This gives rho ~ rho_star - delta on the left and rho_star + delta
    on the right, with a smooth transition of characteristic width ``width``.
    """
    grid = params.make_grid()
    coords = np.meshgrid(*grid, indexing="ij")
    x = coords[0]
    centre = params.L[0] / 2.0
    rho = params.rho_star + delta * np.tanh((x - centre) / width)
    return enforce_bounds(rho, params)


def run_step_relaxation(
    regime: Optional[DiffusionRegime] = None,
    delta: float = 0.03,
    width: float = 0.02,
) -> StepRelaxationResult:
    """Run a step-relaxation experiment in the diffusion regime.

    A smoothed step profile along the x-axis is evolved under the ED PDE.
    The midline profile (through the domain centre along y, z, ...) is
    recorded at each snapshot for comparison with the error-function
    solution of the heat equation.

    Parameters
    ----------
    regime : DiffusionRegime, optional
        If None, the default 2D diffusion regime is built.
    delta : float
        Half-amplitude of the step (default 0.03).
    width : float
        Initial smoothing width (default 0.02).

    Returns
    -------
    StepRelaxationResult
        Experiment output with midline profile time series.
    """
    if regime is None:
        regime = build_diffusion_regime(d=2)

    params = regime.parameters
    ic = _make_step_ic(params, delta, width)

    config = RunConfig(
        params=params,
        ic_type="custom",
        ic_kwargs={"field": ic},
    )

    series = run_simulation(config)

    # Extract midline profiles along x at y=centre (and z=centre, w=centre)
    grid = params.make_grid()
    x_coords = grid[0]

    midline_profiles = []
    for field in series.fields:
        # Index through the centre of all axes except the first
        idx = [slice(None)]  # all x
        for ax in range(1, params.d):
            mid = params.N[ax] // 2
            idx.append(mid)
        midline_profiles.append(field[tuple(idx)].copy())

    times_arr = np.array(series.times)

    return StepRelaxationResult(
        regime=regime,
        series=series,
        times=times_arr,
        midline_profiles=midline_profiles,
        x_coords=x_coords,
        step_direction=0,
    )
