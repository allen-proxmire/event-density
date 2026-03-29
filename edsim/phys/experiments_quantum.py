"""
edsim.phys.experiments_quantum — Quantum-regime numerical experiments.

Three experiments:

1. **Anomalous spread** — a narrow bump evolves under the nonlinear-mobility
   ED PDE.  The variance growth exponent alpha is extracted: alpha = 1 for
   normal diffusion; alpha != 1 indicates anomalous transport.

2. **Double-bump interference** — two identical bumps separated by a gap
   evolve and overlap.  The overlap profile is compared to the linear
   superposition of two independently evolving bumps.

3. **Oscillatory envelope** — a bump evolves with strong participation
   coupling.  The mean density <rho>(t) oscillates via the telegraph
   mode, modulating the spreading profile.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

import numpy as np

from ..core.parameters import EDParameters
from ..core.constitutive import enforce_bounds
from ..experiments.runner import RunConfig, TimeSeries, run_simulation
from .quantum_regime import QuantumRegime, build_quantum_regime


# ---------------------------------------------------------------
# Result containers
# ---------------------------------------------------------------

@dataclass
class AnomalousSpreadResult:
    regime: QuantumRegime
    series: TimeSeries
    times: np.ndarray
    variances: np.ndarray
    peak_values: np.ndarray
    kurtosis: np.ndarray
    sigma0: float
    A0: float


@dataclass
class DoubleBumpResult:
    regime: QuantumRegime
    series_double: TimeSeries
    series_single: TimeSeries
    times: np.ndarray
    overlap_error: np.ndarray
    separation: float
    A0: float
    sigma0: float


@dataclass
class OscillatoryEnvelopeResult:
    regime: QuantumRegime
    series: TimeSeries
    times: np.ndarray
    mean_rho: np.ndarray
    peak_values: np.ndarray
    v_history: np.ndarray
    n_oscillations: int
    A0: float


# ---------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------

def _compute_moments(rho, params):
    """Compute variance and excess kurtosis of delta_rho along axis 0."""
    grid = params.make_grid()
    coords = np.meshgrid(*grid, indexing="ij")
    delta = rho - params.rho_star

    dx_prod = 1.0
    for i in range(params.d):
        dx_prod *= params.dx[i]

    # Moments relative to domain centre
    r2 = np.zeros(params.N)
    for ax in range(params.d):
        centre = params.L[ax] / 2.0
        r2 += (coords[ax] - centre) ** 2

    total = float(np.sum(delta)) * dx_prod
    if abs(total) < 1e-30:
        return 0.0, 0.0

    var = float(np.sum(r2 * delta)) * dx_prod / total

    # Fourth moment for kurtosis
    r4 = r2 ** 2
    m4 = float(np.sum(r4 * delta)) * dx_prod / total
    if var > 1e-30:
        kurt = m4 / (var ** 2) - 3.0  # excess kurtosis (0 for Gaussian)
    else:
        kurt = 0.0

    return max(var, 0.0), kurt


# ---------------------------------------------------------------
# Experiment 1: anomalous spreading
# ---------------------------------------------------------------

def run_anomalous_spread(
    regime: Optional[QuantumRegime] = None,
) -> AnomalousSpreadResult:
    """Evolve a narrow Gaussian bump and track variance scaling.

    Parameters
    ----------
    regime : QuantumRegime, optional

    Returns
    -------
    AnomalousSpreadResult
    """
    if regime is None:
        regime = build_quantum_regime(d=2)

    params = regime.parameters
    A = regime.ic_amplitude
    sigma = regime.ic_sigma

    grid = params.make_grid()
    coords = np.meshgrid(*grid, indexing="ij")
    r2 = np.zeros(params.N)
    for ax in range(params.d):
        r2 += (coords[ax] - params.L[ax] / 2.0) ** 2
    ic = params.rho_star + A * np.exp(-r2 / (2.0 * sigma ** 2))
    ic = enforce_bounds(ic, params)

    config = RunConfig(params=params, ic_type="custom", ic_kwargs={"field": ic})
    series = run_simulation(config)
    times = np.array(series.times)

    variances = []
    peaks = []
    kurtoses = []
    for field in series.fields:
        var, kurt = _compute_moments(field, params)
        variances.append(var)
        kurtoses.append(kurt)
        peaks.append(float(np.max(field - params.rho_star)))

    return AnomalousSpreadResult(
        regime=regime, series=series, times=times,
        variances=np.array(variances), peak_values=np.array(peaks),
        kurtosis=np.array(kurtoses), sigma0=sigma, A0=A,
    )


# ---------------------------------------------------------------
# Experiment 2: double-bump interference
# ---------------------------------------------------------------

def run_double_bump_interference(
    regime: Optional[QuantumRegime] = None,
    separation: float = 0.3,
) -> DoubleBumpResult:
    """Evolve two bumps and compare to linear superposition.

    The "interference" metric is the L2 difference between the
    two-bump simulation and the sum of two single-bump simulations.

    Parameters
    ----------
    regime : QuantumRegime, optional
    separation : float
        Distance between bump centres (default 0.3).

    Returns
    -------
    DoubleBumpResult
    """
    if regime is None:
        regime = build_quantum_regime(d=2)

    params = regime.parameters
    A = regime.ic_amplitude
    sigma = regime.ic_sigma
    grid = params.make_grid()
    coords = np.meshgrid(*grid, indexing="ij")

    xc = params.L[0] / 2.0
    x_left = xc - separation / 2.0
    x_right = xc + separation / 2.0

    def _make_bump(x0):
        r2 = (coords[0] - x0) ** 2
        for ax in range(1, params.d):
            r2 += (coords[ax] - params.L[ax] / 2.0) ** 2
        return A * np.exp(-r2 / (2.0 * sigma ** 2))

    # Double bump IC
    ic_double = params.rho_star + _make_bump(x_left) + _make_bump(x_right)
    ic_double = enforce_bounds(ic_double, params)

    # Single bump at left (for superposition reference)
    ic_single = params.rho_star + _make_bump(x_left)
    ic_single = enforce_bounds(ic_single, params)

    config_d = RunConfig(params=params, ic_type="custom", ic_kwargs={"field": ic_double})
    config_s = RunConfig(params=params, ic_type="custom", ic_kwargs={"field": ic_single})

    series_d = run_simulation(config_d)
    series_s = run_simulation(config_s)

    times = np.array(series_d.times)

    # Overlap error: ||rho_double - (rho_left + rho_right - rho_star)|| / ||rho_double - rho_star||
    # By symmetry, rho_right(x, t) = rho_left(L-x, t) for our symmetric domain.
    overlap_err = []
    for i in range(len(times)):
        f_double = series_d.fields[i]
        f_single = series_s.fields[i]
        # Mirror the single bump to get the right bump
        f_right = np.flip(f_single, axis=0)
        f_super = (f_single - params.rho_star) + (f_right - params.rho_star) + params.rho_star

        diff = f_double - f_super
        norm = np.sqrt(np.sum((f_double - params.rho_star) ** 2))
        overlap_err.append(np.sqrt(np.sum(diff ** 2)) / (norm + 1e-30))

    return DoubleBumpResult(
        regime=regime,
        series_double=series_d, series_single=series_s,
        times=times, overlap_error=np.array(overlap_err),
        separation=separation, A0=A, sigma0=sigma,
    )


# ---------------------------------------------------------------
# Experiment 3: oscillatory envelope
# ---------------------------------------------------------------

def run_oscillatory_envelope(
    regime: Optional[QuantumRegime] = None,
) -> OscillatoryEnvelopeResult:
    """Evolve a bump with strong participation and track oscillations.

    Parameters
    ----------
    regime : QuantumRegime, optional

    Returns
    -------
    OscillatoryEnvelopeResult
    """
    if regime is None:
        regime = build_quantum_regime(d=2)

    params = regime.parameters
    A = regime.ic_amplitude
    sigma = regime.ic_sigma

    grid = params.make_grid()
    coords = np.meshgrid(*grid, indexing="ij")
    r2 = np.zeros(params.N)
    for ax in range(params.d):
        r2 += (coords[ax] - params.L[ax] / 2.0) ** 2
    ic = params.rho_star + A * np.exp(-r2 / (2.0 * sigma ** 2))
    ic = enforce_bounds(ic, params)

    config = RunConfig(params=params, ic_type="custom", ic_kwargs={"field": ic})
    series = run_simulation(config)
    times = np.array(series.times)

    mean_rho = np.array([float(np.mean(f)) for f in series.fields])
    peaks = np.array([float(np.max(f - params.rho_star)) for f in series.fields])
    v_hist = np.array(series.v_history)

    # Count zero crossings of (mean_rho - rho_star) to estimate oscillation count
    delta_mean = mean_rho - params.rho_star
    crossings = 0
    for j in range(len(delta_mean) - 1):
        if delta_mean[j] * delta_mean[j + 1] < 0:
            crossings += 1
    n_osc = crossings // 2

    return OscillatoryEnvelopeResult(
        regime=regime, series=series, times=times,
        mean_rho=mean_rho, peak_values=peaks, v_history=v_hist,
        n_oscillations=n_osc, A0=A,
    )
