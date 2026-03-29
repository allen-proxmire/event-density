"""
edsim.phys.experiments_cosmology — Cosmological-analogue experiments.

Three experiments:

1. **Expansion analogue:** track global density decay and effective scale factor.
2. **Horizon analogue:** track regions where M(rho) is near zero.
3. **Structure analogue:** track transient filament/sheet formation and decay.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional
import itertools

import numpy as np

from ..core.parameters import EDParameters
from ..core.constitutive import enforce_bounds, mobility
from ..experiments.runner import RunConfig, TimeSeries, run_simulation
from .cosmology_regime import CosmologyRegime, build_cosmology_regime


# ---------------------------------------------------------------
# Result containers
# ---------------------------------------------------------------

@dataclass
class ExpansionResult:
    regime: CosmologyRegime
    series: TimeSeries
    times: np.ndarray
    mean_rho: np.ndarray
    scale_factor: np.ndarray
    hubble_rate: np.ndarray


@dataclass
class HorizonResult:
    regime: CosmologyRegime
    series: TimeSeries
    times: np.ndarray
    horizon_fraction: np.ndarray
    mean_mobility: np.ndarray
    min_mobility: np.ndarray


@dataclass
class StructureResult:
    regime: CosmologyRegime
    series: TimeSeries
    times: np.ndarray
    complexity: np.ndarray
    spectral_entropy: np.ndarray
    filament_fraction: np.ndarray
    sheet_fraction: np.ndarray


# ---------------------------------------------------------------
# Shared IC builder
# ---------------------------------------------------------------

def _make_overdense_ic(params: EDParameters, A: float, Nm: int) -> np.ndarray:
    """Build an overdense multi-modal IC centred above rho_star."""
    grid = params.make_grid()
    coords = np.meshgrid(*grid, indexing="ij")

    # Start at rho_star + offset (overdense) then add modes
    offset = A * 0.5  # base overdensity
    rho = np.full(params.N, params.rho_star + offset, dtype=float)

    for k_vec in itertools.product(range(Nm + 1), repeat=params.d):
        if all(k == 0 for k in k_vec):
            continue
        mode = np.ones(params.N)
        for ax, k in enumerate(k_vec):
            mode *= np.cos(k * np.pi * coords[ax] / params.L[ax])
        rho += A * 0.5 / (Nm ** params.d) * mode

    return enforce_bounds(rho, params)


# ---------------------------------------------------------------
# Experiment 1: expansion
# ---------------------------------------------------------------

def run_expansion_analogue(
    regime: Optional[CosmologyRegime] = None,
) -> ExpansionResult:
    """Track global density decay and effective scale factor.

    a(t) = (rho_star / <rho>(t))^(1/d)
    H_eff(t) = d a/dt / a

    Parameters
    ----------
    regime : CosmologyRegime, optional

    Returns
    -------
    ExpansionResult
    """
    if regime is None:
        regime = build_cosmology_regime()

    params = regime.parameters
    ic = _make_overdense_ic(params, regime.ic_amplitude, regime.ic_modes)

    config = RunConfig(params=params, ic_type="custom", ic_kwargs={"field": ic})
    series = run_simulation(config)
    times = np.array(series.times)

    mean_rho = np.array([float(np.mean(f)) for f in series.fields])
    d = params.d
    rho_star = params.rho_star

    # Scale factor: a = (rho_star / <rho>)^(1/d), clamped for safety
    safe_ratio = np.clip(rho_star / (mean_rho + 1e-30), 0.01, 100.0)
    scale_factor = safe_ratio ** (1.0 / d)

    # Hubble rate: H = da/dt / a (numerical derivative)
    if len(times) >= 3:
        da_dt = np.gradient(scale_factor, times)
        hubble = da_dt / (scale_factor + 1e-30)
    else:
        hubble = np.zeros_like(times)

    return ExpansionResult(
        regime=regime, series=series, times=times,
        mean_rho=mean_rho, scale_factor=scale_factor, hubble_rate=hubble,
    )


# ---------------------------------------------------------------
# Experiment 2: horizons
# ---------------------------------------------------------------

def run_horizon_analogue(
    regime: Optional[CosmologyRegime] = None,
) -> HorizonResult:
    """Track regions where mobility vanishes (horizon analogue).

    Parameters
    ----------
    regime : CosmologyRegime, optional

    Returns
    -------
    HorizonResult
    """
    if regime is None:
        regime = build_cosmology_regime()

    params = regime.parameters
    ic = _make_overdense_ic(params, regime.ic_amplitude, regime.ic_modes)

    config = RunConfig(params=params, ic_type="custom", ic_kwargs={"field": ic})
    series = run_simulation(config)
    times = np.array(series.times)

    M_star = params.M_star
    M_crit = 0.01 * M_star  # horizon = M < 1% of equilibrium mobility

    horiz_frac = []
    mean_mob = []
    min_mob = []

    for field in series.fields:
        M = mobility(field, params)
        horiz_frac.append(float(np.mean(M < M_crit)))
        mean_mob.append(float(np.mean(M)))
        min_mob.append(float(np.min(M)))

    return HorizonResult(
        regime=regime, series=series, times=times,
        horizon_fraction=np.array(horiz_frac),
        mean_mobility=np.array(mean_mob),
        min_mobility=np.array(min_mob),
    )


# ---------------------------------------------------------------
# Experiment 3: structure
# ---------------------------------------------------------------

def run_structure_analogue(
    regime: Optional[CosmologyRegime] = None,
) -> StructureResult:
    """Track transient filament/sheet structure.

    Parameters
    ----------
    regime : CosmologyRegime, optional

    Returns
    -------
    StructureResult
    """
    if regime is None:
        regime = build_cosmology_regime()

    params = regime.parameters
    ic = _make_overdense_ic(params, regime.ic_amplitude, regime.ic_modes)

    config = RunConfig(params=params, ic_type="custom", ic_kwargs={"field": ic})
    series = run_simulation(config)
    times = np.array(series.times)

    complexity = np.array(series.complexity)
    entropy = np.array(series.spectral_entropy)

    fil_frac = []
    sht_frac = []
    for morph in series.morphology_fractions:
        fil_frac.append(morph.get("filament", 0.0))
        sht_frac.append(morph.get("sheet", 0.0))

    return StructureResult(
        regime=regime, series=series, times=times,
        complexity=complexity, spectral_entropy=entropy,
        filament_fraction=np.array(fil_frac),
        sheet_fraction=np.array(sht_frac),
    )
