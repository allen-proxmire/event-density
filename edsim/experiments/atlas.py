"""
edsim.experiments.atlas — Full invariant atlas generation.

Runs individual scenarios or parameter sweeps, collects full invariant
time series, and provides summary extraction utilities.
"""

from __future__ import annotations

from typing import Callable, Optional

import numpy as np

from ..core.parameters import EDParameters
from .runner import RunConfig, TimeSeries, run_simulation
from .scenarios import Scenario, _replace_params
from .sweeps import run_sweep, SweepResult


def run_atlas(
    scenario: Scenario,
    modifier: Optional[Callable[[EDParameters], EDParameters]] = None,
) -> tuple[EDParameters, TimeSeries]:
    """Run a single, fully instrumented simulation for a given scenario.

    Parameters
    ----------
    scenario : Scenario
        Experiment specification.
    modifier : callable, optional
        Function that takes EDParameters and returns modified EDParameters.
        Applied after the scenario's make_config().

    Returns
    -------
    tuple[EDParameters, TimeSeries]
        (params, time_series) for the completed run.
    """
    config = scenario.make_config()

    if modifier is not None:
        new_params = modifier(config.params)
        config = RunConfig(
            params=new_params,
            ic_type=config.ic_type,
            ic_kwargs=config.ic_kwargs,
            output_dir=config.output_dir,
        )

    series = run_simulation(config)
    return config.params, series


def run_atlas_sweep(
    scenario: Scenario,
    vary: str,
    values: list,
) -> list[tuple[EDParameters, TimeSeries, dict]]:
    """Run a parameter sweep and compute summaries for each run.

    Parameters
    ----------
    scenario : Scenario
        Baseline experiment.
    vary : str
        Parameter to vary (EDParameters field or "ic_X" for IC kwargs).
    values : list
        Values to sweep.

    Returns
    -------
    list[tuple[EDParameters, TimeSeries, dict]]
        List of (params, series, summary) for each sweep point.
    """
    sweep_results = run_sweep(scenario, vary, values)

    output = []
    for sr in sweep_results:
        summary = summarize_time_series(sr.series)
        summary["label"] = sr.label
        output.append((sr.params, sr.series, summary))

    return output


def summarize_time_series(ts: TimeSeries) -> dict:
    """Extract a compact summary from a TimeSeries.

    Returns key invariant values at initial and final time,
    plus derived quantities like decay ratios and growth factors.

    Parameters
    ----------
    ts : TimeSeries
        Completed simulation time series.

    Returns
    -------
    dict
        Summary with keys:
        - "T": final time
        - "n_snapshots": number of snapshots
        - "energy_initial", "energy_final", "energy_ratio"
        - "complexity_initial", "complexity_final", "complexity_ratio"
        - "mass_initial", "mass_final", "mass_change"
        - "spectral_entropy_initial", "spectral_entropy_final"
        - "R_grad_mean", "R_pen_mean", "R_part_mean"
        - "morphology_initial", "morphology_final"
        - "correlation_length_initial", "correlation_length_final", "xi_ratio"
        - "euler_chi_initial", "euler_chi_final", "chi_constant"
        - "v_final"
        - "energy_monotone"
    """
    n = len(ts.times)
    if n == 0:
        return {"error": "empty time series"}

    E0 = ts.energy[0]
    Ef = ts.energy[-1]
    C0 = ts.complexity[0]
    Cf = ts.complexity[-1]
    M0 = ts.mass[0]
    Mf = ts.mass[-1]

    # Energy monotonicity check
    E_mono = all(
        ts.energy[i] >= ts.energy[i + 1] - 1e-12
        for i in range(n - 1)
    )

    # Chi conservation check
    chi_vals = ts.euler_characteristic if hasattr(ts, "euler_characteristic") and ts.euler_characteristic else []
    chi_const = len(set(chi_vals)) <= 1 if chi_vals else None

    # Correlation length ratio
    xi0 = ts.correlation_length[0] if ts.correlation_length else 0.0
    xif = ts.correlation_length[-1] if ts.correlation_length else 0.0

    return {
        "T": ts.times[-1],
        "n_snapshots": n,
        # Energy
        "energy_initial": E0,
        "energy_final": Ef,
        "energy_ratio": Ef / E0 if abs(E0) > 1e-30 else 0.0,
        "energy_monotone": E_mono,
        # Complexity
        "complexity_initial": C0,
        "complexity_final": Cf,
        "complexity_ratio": Cf / C0 if abs(C0) > 1e-30 else 0.0,
        # Mass
        "mass_initial": M0,
        "mass_final": Mf,
        "mass_change": abs(Mf - M0) / abs(M0) if abs(M0) > 1e-30 else 0.0,
        # Spectral
        "spectral_entropy_initial": ts.spectral_entropy[0] if ts.spectral_entropy else 0.0,
        "spectral_entropy_final": ts.spectral_entropy[-1] if ts.spectral_entropy else 0.0,
        # Dissipation (mean over all snapshots)
        "R_grad_mean": float(np.mean(ts.R_grad)) if ts.R_grad else 0.0,
        "R_pen_mean": float(np.mean(ts.R_pen)) if ts.R_pen else 0.0,
        "R_part_mean": float(np.mean(ts.R_part)) if ts.R_part else 0.0,
        # Morphology
        "morphology_initial": ts.morphology_fractions[0] if ts.morphology_fractions else {},
        "morphology_final": ts.morphology_fractions[-1] if ts.morphology_fractions else {},
        # Correlation
        "correlation_length_initial": xi0,
        "correlation_length_final": xif,
        "xi_ratio": xif / xi0 if abs(xi0) > 1e-30 else 0.0,
        # Topology
        "euler_chi_initial": chi_vals[0] if chi_vals else None,
        "euler_chi_final": chi_vals[-1] if chi_vals else None,
        "chi_constant": chi_const,
        # Participation
        "v_final": ts.v_history[-1] if ts.v_history else 0.0,
    }
