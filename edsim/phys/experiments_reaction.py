"""
edsim.phys.experiments_reaction — Reaction-regime numerical experiments.

Three experiments:

1. **Uniform decay** — rho starts above rho_star and relaxes exponentially.
2. **Uniform growth** — rho starts below rho_star and grows toward it.
   (In ED, both directions relax *toward* rho_star, so "growth" means
   increasing rho, not instability.)
3. **Localised source** — a localised bump above rho_star decays in place
   while diffusion spreads it laterally.  The competition between reaction
   (penalty) and diffusion is measured.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

import numpy as np

from ..core.parameters import EDParameters
from ..core.constitutive import enforce_bounds
from ..experiments.runner import RunConfig, TimeSeries, run_simulation
from .reaction_regime import ReactionRegime, build_reaction_regime


# ---------------------------------------------------------------
# Result containers
# ---------------------------------------------------------------

@dataclass
class UniformDecayResult:
    """Output of the uniform-decay experiment.

    Attributes
    ----------
    regime : ReactionRegime
    series : TimeSeries
    times : np.ndarray
    delta : np.ndarray
        <rho>(t) - rho_star at each snapshot.
    v_history : np.ndarray
    A0 : float
        Initial offset (positive: above rho_star).
    """

    regime: ReactionRegime
    series: TimeSeries
    times: np.ndarray
    delta: np.ndarray
    v_history: np.ndarray
    A0: float


@dataclass
class UniformGrowthResult:
    """Output of the uniform-growth experiment.

    Same structure as UniformDecayResult but A0 < 0 (below rho_star).
    """

    regime: ReactionRegime
    series: TimeSeries
    times: np.ndarray
    delta: np.ndarray
    v_history: np.ndarray
    A0: float


@dataclass
class LocalisedSourceResult:
    """Output of the localised-source experiment.

    Attributes
    ----------
    regime : ReactionRegime
    series : TimeSeries
    times : np.ndarray
    peak_delta : np.ndarray
        Peak |rho - rho_star| at each snapshot.
    total_excess : np.ndarray
        Integral of |rho - rho_star| at each snapshot.
    widths : np.ndarray
        RMS width of the perturbation along x.
    sigma0 : float
    A0 : float
    """

    regime: ReactionRegime
    series: TimeSeries
    times: np.ndarray
    peak_delta: np.ndarray
    total_excess: np.ndarray
    widths: np.ndarray
    sigma0: float
    A0: float


# ---------------------------------------------------------------
# Experiment 1: uniform decay
# ---------------------------------------------------------------

def run_uniform_decay(
    regime: Optional[ReactionRegime] = None,
    amplitude: float = 0.05,
) -> UniformDecayResult:
    """Evolve a spatially uniform field above rho_star.

    rho(x, 0) = rho_star + A   (A > 0)

    With H = 0 the penalty drives exponential decay:
    delta(t) = A * exp(-D * P0 * t).

    Parameters
    ----------
    regime : ReactionRegime, optional
    amplitude : float
        Initial offset above rho_star (default 0.05).

    Returns
    -------
    UniformDecayResult
    """
    if regime is None:
        regime = build_reaction_regime(d=2)

    params = regime.parameters
    ic = np.full(params.N, params.rho_star + amplitude)
    ic = enforce_bounds(ic, params)

    config = RunConfig(
        params=params,
        ic_type="custom",
        ic_kwargs={"field": ic},
    )

    series = run_simulation(config)
    times = np.array(series.times)
    delta = np.array([float(np.mean(f)) - params.rho_star for f in series.fields])

    return UniformDecayResult(
        regime=regime,
        series=series,
        times=times,
        delta=delta,
        v_history=np.array(series.v_history),
        A0=amplitude,
    )


# ---------------------------------------------------------------
# Experiment 2: uniform growth (toward rho_star from below)
# ---------------------------------------------------------------

def run_uniform_growth(
    regime: Optional[ReactionRegime] = None,
    amplitude: float = -0.05,
) -> UniformGrowthResult:
    """Evolve a spatially uniform field below rho_star.

    rho(x, 0) = rho_star + A   (A < 0)

    The penalty drives delta toward zero: delta(t) = A * exp(-D*P0*t).
    Since A < 0, rho(t) increases toward rho_star.

    Parameters
    ----------
    regime : ReactionRegime, optional
    amplitude : float
        Initial offset (should be negative; default -0.05).

    Returns
    -------
    UniformGrowthResult
    """
    if regime is None:
        regime = build_reaction_regime(d=2)

    params = regime.parameters
    ic = np.full(params.N, params.rho_star + amplitude)
    ic = enforce_bounds(ic, params)

    config = RunConfig(
        params=params,
        ic_type="custom",
        ic_kwargs={"field": ic},
    )

    series = run_simulation(config)
    times = np.array(series.times)
    delta = np.array([float(np.mean(f)) - params.rho_star for f in series.fields])

    return UniformGrowthResult(
        regime=regime,
        series=series,
        times=times,
        delta=delta,
        v_history=np.array(series.v_history),
        A0=amplitude,
    )


# ---------------------------------------------------------------
# Experiment 3: localised source
# ---------------------------------------------------------------

def run_localised_source(
    regime: Optional[ReactionRegime] = None,
    sigma: float = 0.08,
    amplitude: float = 0.05,
) -> LocalisedSourceResult:
    """Evolve a localised Gaussian bump and track reaction vs diffusion.

    rho(x, 0) = rho_star + A * exp(-|x - x_c|^2 / (2 sigma^2))

    The bump decays (reaction) and spreads (diffusion) simultaneously.
    The total excess integral( rho - rho_star ) decays at the reaction
    rate while the width grows at the diffusion rate.

    Parameters
    ----------
    regime : ReactionRegime, optional
    sigma : float
        Gaussian width (default 0.08).
    amplitude : float
        Peak amplitude (default 0.05).

    Returns
    -------
    LocalisedSourceResult
    """
    if regime is None:
        regime = build_reaction_regime(d=2)

    params = regime.parameters
    grid = params.make_grid()
    coords = np.meshgrid(*grid, indexing="ij")

    r2 = np.zeros(params.N)
    for ax in range(params.d):
        centre = params.L[ax] / 2.0
        r2 += (coords[ax] - centre) ** 2

    ic = params.rho_star + amplitude * np.exp(-r2 / (2.0 * sigma ** 2))
    ic = enforce_bounds(ic, params)

    config = RunConfig(
        params=params,
        ic_type="custom",
        ic_kwargs={"field": ic},
    )

    series = run_simulation(config)
    times = np.array(series.times)

    dx_prod = 1.0
    for i in range(params.d):
        dx_prod *= params.dx[i]

    x_1d = grid[0]

    peak_delta = []
    total_excess = []
    widths = []

    for field in series.fields:
        delta_f = field - params.rho_star
        peak_delta.append(float(np.max(np.abs(delta_f))))
        # Signed integral: for a positive bump this tracks the total mass excess
        total_excess.append(float(np.sum(delta_f)) * dx_prod)

        # Width along x
        axes_to_avg = tuple(range(1, params.d))
        if axes_to_avg:
            prof = np.mean(np.abs(delta_f), axis=axes_to_avg)
        else:
            prof = np.abs(delta_f)
        total = float(np.sum(prof) * params.dx[0])
        if total < 1e-30:
            widths.append(0.0)
        else:
            centroid = float(np.sum(x_1d * prof) * params.dx[0]) / total
            w = np.sqrt(
                float(np.sum((x_1d - centroid) ** 2 * prof) * params.dx[0]) / total
            )
            widths.append(w)

    return LocalisedSourceResult(
        regime=regime,
        series=series,
        times=times,
        peak_delta=np.array(peak_delta),
        total_excess=np.array(total_excess),
        widths=np.array(widths),
        sigma0=sigma,
        A0=amplitude,
    )
