"""
edsim.experiments.sweeps — Parameter sweeps and batch execution.

Provides functions to systematically vary one or two parameters
across a baseline scenario and collect full invariant time series.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Optional

import numpy as np

from ..core.parameters import EDParameters
from .runner import RunConfig, TimeSeries, run_simulation
from .scenarios import Scenario, _replace_params


@dataclass
class SweepResult:
    """Result of a single sweep point.

    Attributes
    ----------
    params : EDParameters
        Parameters used for this run.
    series : TimeSeries
        Full invariant time series.
    label : str
        Human-readable label (e.g., "D=0.30").
    """

    params: EDParameters
    series: TimeSeries
    label: str


def run_sweep(
    base_scenario: Scenario,
    vary: str,
    values: Iterable,
) -> list[SweepResult]:
    """Run a 1D parameter sweep over a single EDParameters field.

    For each value, builds a modified RunConfig from the base scenario,
    runs the simulation, and collects the result.

    Parameters
    ----------
    base_scenario : Scenario
        Baseline scenario providing default parameters and IC.
    vary : str
        Name of the EDParameters field to vary (e.g., "D", "P0", "beta").
        Can also be an IC parameter prefixed with "ic_": e.g., "ic_A"
        varies the amplitude A in the IC kwargs.
    values : Iterable
        Values to assign to the varied parameter.

    Returns
    -------
    list[SweepResult]
        One SweepResult per value, in order.
    """
    results = []

    for val in values:
        config = base_scenario.make_config()

        if vary.startswith("ic_"):
            # Vary an IC parameter (e.g., ic_A -> ic_kwargs["A"])
            ic_key = vary[3:]
            new_kwargs = dict(config.ic_kwargs)
            new_kwargs[ic_key] = val
            config = RunConfig(
                params=config.params,
                ic_type=config.ic_type,
                ic_kwargs=new_kwargs,
                output_dir=config.output_dir,
            )
            label = f"{ic_key}={val}"
        else:
            # Vary an EDParameters field
            new_params = _replace_params(config.params, **{vary: val})
            config = RunConfig(
                params=new_params,
                ic_type=config.ic_type,
                ic_kwargs=config.ic_kwargs,
                output_dir=config.output_dir,
            )
            label = f"{vary}={val}"

        series = run_simulation(config)
        results.append(SweepResult(params=config.params, series=series, label=label))

    return results


def run_grid_sweep(
    base_scenario: Scenario,
    vary1: str,
    values1: Iterable,
    vary2: str,
    values2: Iterable,
) -> list[SweepResult]:
    """Run a 2D grid sweep over two parameters.

    Iterates over the Cartesian product of values1 x values2.

    Parameters
    ----------
    base_scenario : Scenario
        Baseline scenario.
    vary1 : str
        First parameter to vary.
    values1 : Iterable
        Values for the first parameter.
    vary2 : str
        Second parameter to vary.
    values2 : Iterable
        Values for the second parameter.

    Returns
    -------
    list[SweepResult]
        One SweepResult per (v1, v2) pair, in row-major order.
    """
    results = []

    for v1 in values1:
        for v2 in values2:
            config = base_scenario.make_config()

            overrides = {}
            ic_overrides = {}

            for var, val in [(vary1, v1), (vary2, v2)]:
                if var.startswith("ic_"):
                    ic_overrides[var[3:]] = val
                else:
                    overrides[var] = val

            if overrides:
                new_params = _replace_params(config.params, **overrides)
            else:
                new_params = config.params

            if ic_overrides:
                new_kwargs = dict(config.ic_kwargs)
                new_kwargs.update(ic_overrides)
            else:
                new_kwargs = config.ic_kwargs

            config = RunConfig(
                params=new_params,
                ic_type=config.ic_type,
                ic_kwargs=new_kwargs,
                output_dir=config.output_dir,
            )

            label = f"{vary1}={v1}, {vary2}={v2}"
            series = run_simulation(config)
            results.append(SweepResult(params=config.params, series=series, label=label))

    return results


def run_batch(
    configs: list[RunConfig],
    parallel: bool = False,
    n_workers: Optional[int] = None,
) -> list[TimeSeries]:
    """Run multiple simulations sequentially (parallel not yet implemented).

    Parameters
    ----------
    configs : list[RunConfig]
        List of run configurations.
    parallel : bool
        Reserved for future multiprocessing support. Currently ignored.
    n_workers : int, optional
        Reserved for future use.

    Returns
    -------
    list[TimeSeries]
        Results in the same order as configs.
    """
    return [run_simulation(config) for config in configs]
