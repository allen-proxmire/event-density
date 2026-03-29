"""
edsim.phys.experiments_phase — Phase-diagram numerical validation.

Runs short diagnostic simulations at selected phase points to validate
the analytical classification.  Each diagnostic run uses a small grid
(N=32) and short time (T ~ 2/sigma_k1) to confirm the dominant behaviour.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

import numpy as np

from ..core.parameters import EDParameters
from ..core.constitutive import enforce_bounds
from ..experiments.runner import RunConfig, TimeSeries, run_simulation
from .phase_diagram import PhasePoint, PhaseMetrics, compute_phase_metrics


@dataclass
class PhaseValidation:
    """Numerical validation of a phase classification.

    Attributes
    ----------
    point : PhasePoint
    energy_monotone : bool
    complexity_decays : bool
    mean_rho_oscillates : bool
    n_oscillations : int
    final_std : float
        std(rho) at final time (should approach 0 for attractor).
    """

    point: PhasePoint
    energy_monotone: bool
    complexity_decays: bool
    mean_rho_oscillates: bool
    n_oscillations: int
    final_std: float


def run_phase_validation(
    point: PhasePoint,
    N: int = 32,
) -> PhaseValidation:
    """Run a short diagnostic simulation at a phase point.

    Uses a Gaussian bump IC and tracks energy, complexity, and
    mean-density oscillation.

    Parameters
    ----------
    point : PhasePoint
    N : int
        Grid points per axis (default 32).

    Returns
    -------
    PhaseValidation
    """
    m = point.metrics
    T = min(10.0, max(0.5, 3.0 / (m.sigma_k1 + 1e-10)))
    dt = min(1e-3, T / 200.0)

    params = EDParameters(
        d=2,
        L=(1.0, 1.0),
        N=(N, N),
        D=0.3,
        H=point.H,
        zeta=0.1,
        tau=1.0,
        rho_star=0.5,
        rho_max=1.0,
        M0=point.M0,
        beta=2.0,
        P0=point.P0,
        dt=dt,
        T=T,
        method="implicit_euler",
        bc="neumann",
        k_out=max(1, int(T / dt) // 30),
        seed=42,
    )

    # Gaussian IC
    grid = params.make_grid()
    coords = np.meshgrid(*grid, indexing="ij")
    r2 = np.zeros(params.N)
    for ax in range(params.d):
        r2 += (coords[ax] - params.L[ax] / 2.0) ** 2
    ic = params.rho_star + 0.05 * np.exp(-r2 / (2.0 * 0.08 ** 2))
    ic = enforce_bounds(ic, params)

    config = RunConfig(params=params, ic_type="custom", ic_kwargs={"field": ic})
    series = run_simulation(config)

    # Check energy monotonicity
    E = series.energy
    E_mono = all(E[i] >= E[i + 1] - 1e-10 for i in range(len(E) - 1))

    # Check complexity decay
    C = series.complexity
    C_decays = C[-1] < C[0] * 1.01 if len(C) >= 2 else True

    # Check mean-density oscillation
    mean_rho = np.array([float(np.mean(f)) for f in series.fields])
    delta = mean_rho - params.rho_star
    crossings = 0
    for j in range(len(delta) - 1):
        if delta[j] * delta[j + 1] < 0:
            crossings += 1
    n_osc = crossings // 2
    oscillates = n_osc >= 1

    final_std = float(np.std(series.fields[-1] - params.rho_star))

    return PhaseValidation(
        point=point,
        energy_monotone=E_mono,
        complexity_decays=C_decays,
        mean_rho_oscillates=oscillates,
        n_oscillations=n_osc,
        final_std=final_std,
    )


def validate_phase_diagram(
    points: list[PhasePoint],
    sample: int = 8,
    N: int = 32,
) -> list[PhaseValidation]:
    """Validate a sample of phase points numerically.

    Selects ``sample`` points spread across phases and runs diagnostics.

    Parameters
    ----------
    points : list[PhasePoint]
    sample : int
    N : int

    Returns
    -------
    list[PhaseValidation]
    """
    # Select points: one from each phase, then fill remaining from largest phase
    by_phase = {}
    for p in points:
        by_phase.setdefault(p.classification, []).append(p)

    selected = []
    for phase, pts in by_phase.items():
        selected.append(pts[0])

    # Fill remaining slots
    remaining = sample - len(selected)
    all_pts = [p for p in points if p not in selected]
    rng = np.random.default_rng(42)
    if remaining > 0 and all_pts:
        indices = rng.choice(len(all_pts), size=min(remaining, len(all_pts)), replace=False)
        for idx in indices:
            selected.append(all_pts[idx])

    return [run_phase_validation(p, N=N) for p in selected]
