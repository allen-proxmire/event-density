"""
edsim.phys.experiments_energy — Energy/entropy/Lyapunov experiments.

Four experiments:

1. **Lyapunov monotonicity** (H=0): track E_Lyapunov(t), verify dE/dt <= 0.
2. **Participation violation** (H>0): track E_Lyapunov(t), identify violations.
3. **Entropy trajectory**: track S[rho] = -integral rho log rho.
4. **Gradient-flow test**: compare ED operator to the formal gradient flow
   of the Lyapunov functional.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

import numpy as np

from ..core.parameters import EDParameters
from ..core.constitutive import enforce_bounds, mobility, penalty
from ..experiments.runner import RunConfig, TimeSeries, run_simulation
from .energy_regime import (
    EnergyRegime, build_energy_regime,
    lyapunov_energy, gradient_energy, penalty_energy,
    participation_energy, boltzmann_entropy, fisher_information, free_energy,
)


@dataclass
class EnergyTrajectory:
    """Time trajectories of all candidate functionals.

    Attributes
    ----------
    regime : EnergyRegime
    times : np.ndarray
    E_lyapunov : np.ndarray
    E_gradient : np.ndarray
    E_penalty : np.ndarray
    E_participation : np.ndarray
    S_boltzmann : np.ndarray
    I_fisher : np.ndarray
    F_free : np.ndarray
    series : TimeSeries
    """

    regime: EnergyRegime
    times: np.ndarray
    E_lyapunov: np.ndarray
    E_gradient: np.ndarray
    E_penalty: np.ndarray
    E_participation: np.ndarray
    S_boltzmann: np.ndarray
    I_fisher: np.ndarray
    F_free: np.ndarray
    series: TimeSeries


@dataclass
class GradientFlowTest:
    """Comparison of ED operator to the gradient flow of E_Lyapunov.

    Attributes
    ----------
    regime : EnergyRegime
    times : np.ndarray
    residual_l2 : np.ndarray
        ||F_ED - F_gradflow|| / ||F_ED|| at each snapshot.
    mean_residual : float
    """

    regime: EnergyRegime
    times: np.ndarray
    residual_l2: np.ndarray
    mean_residual: float


def _run_and_track(regime: EnergyRegime, ic: np.ndarray) -> EnergyTrajectory:
    """Run simulation and compute all functionals at each snapshot."""
    params = regime.parameters
    config = RunConfig(params=params, ic_type="custom", ic_kwargs={"field": ic})
    series = run_simulation(config)
    times = np.array(series.times)

    E_ly, E_gr, E_pe, E_pa, S_bo, I_fi, F_fr = [], [], [], [], [], [], []
    for i, field in enumerate(series.fields):
        v = series.v_history[i]
        E_ly.append(lyapunov_energy(field, params))
        E_gr.append(gradient_energy(field, params))
        E_pe.append(penalty_energy(field, params))
        E_pa.append(participation_energy(v))
        S_bo.append(boltzmann_entropy(field, params))
        I_fi.append(fisher_information(field, params))
        F_fr.append(free_energy(field, params))

    return EnergyTrajectory(
        regime=regime, times=times, series=series,
        E_lyapunov=np.array(E_ly), E_gradient=np.array(E_gr),
        E_penalty=np.array(E_pe), E_participation=np.array(E_pa),
        S_boltzmann=np.array(S_bo), I_fisher=np.array(I_fi),
        F_free=np.array(F_fr),
    )


def _make_cosine_ic(params: EDParameters, A: float = 0.05, Nm: int = 2) -> np.ndarray:
    """Multi-mode cosine IC."""
    import itertools
    grid = params.make_grid()
    coords = np.meshgrid(*grid, indexing="ij")
    rho = np.full(params.N, params.rho_star, dtype=float)
    for k_vec in itertools.product(range(Nm + 1), repeat=params.d):
        if all(k == 0 for k in k_vec):
            continue
        mode = np.ones(params.N)
        for ax, k in enumerate(k_vec):
            mode *= np.cos(k * np.pi * coords[ax] / params.L[ax])
        rho += A * mode
    return enforce_bounds(rho, params)


def run_energy_monotonicity(
    H: float = 0.0,
    d: int = 2,
    N: int = 64,
) -> EnergyTrajectory:
    """Track all energy functionals for a cosine IC.

    Parameters
    ----------
    H : float
        Participation coupling. 0 for guaranteed monotonicity.
    d : int
    N : int

    Returns
    -------
    EnergyTrajectory
    """
    regime = build_energy_regime(d=d, N=N, H=H)
    ic = _make_cosine_ic(regime.parameters)
    return _run_and_track(regime, ic)


def run_entropy_test(
    d: int = 2,
    N: int = 64,
) -> EnergyTrajectory:
    """Track Boltzmann entropy for a cosine IC (H=0)."""
    return run_energy_monotonicity(H=0.0, d=d, N=N)


def run_gradient_flow_test(
    d: int = 2,
    N: int = 32,
) -> GradientFlowTest:
    """Compare the ED operator to the gradient flow of E_Lyapunov.

    The gradient flow is: rho_t = D * div(M * grad(P/M))
    The ED operator is:   rho_t = D * [div(M * grad rho) - P]

    We compute the residual ||F_ED - F_gf|| / ||F_ED|| at each snapshot.
    """
    regime = build_energy_regime(d=d, N=N, H=0.0, T=1.0)
    params = regime.parameters
    ic = _make_cosine_ic(params)
    config = RunConfig(params=params, ic_type="custom", ic_kwargs={"field": ic})
    series = run_simulation(config)
    times = np.array(series.times)

    dx = [params.dx[i] for i in range(params.d)]
    residuals = []

    for field in series.fields:
        M_val = mobility(field, params)
        P_val = penalty(field, params)

        # ED operator: div(M grad rho) - P
        # = M * Lap(rho) + M' |grad rho|^2 - P
        # Already available as the RHS of the PDE.
        grads_rho = np.gradient(field, *dx)
        lap_rho = sum(np.gradient(g, dx[i], axis=i) for i, g in enumerate(grads_rho))
        from ..core.constitutive import mobility_deriv
        M_prime = mobility_deriv(field, params)
        grad_sq = sum(g ** 2 for g in grads_rho)
        F_ed = params.D * (M_val * lap_rho + M_prime * grad_sq - P_val)

        # Gradient flow of E: div(M * grad(P/M))
        P_over_M = P_val / (M_val + 1e-30)
        grads_PoverM = np.gradient(P_over_M, *dx)
        flux_components = [M_val * g for g in grads_PoverM]
        div_flux = sum(
            np.gradient(flux_components[i], dx[i], axis=i)
            for i in range(params.d)
        )
        F_gf = params.D * div_flux

        diff = F_ed - F_gf
        norm_ed = np.sqrt(np.sum(F_ed ** 2))
        norm_diff = np.sqrt(np.sum(diff ** 2))
        residuals.append(norm_diff / (norm_ed + 1e-30))

    res_arr = np.array(residuals)

    return GradientFlowTest(
        regime=regime, times=times,
        residual_l2=res_arr, mean_residual=float(np.mean(res_arr)),
    )
