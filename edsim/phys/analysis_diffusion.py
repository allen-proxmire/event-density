"""
edsim.phys.analysis_diffusion — Effective diffusion coefficient extraction
and heat-equation comparison.

This module provides two core analyses:

1. **fit_effective_diffusion_coefficient** — fits D_eff from the variance
   growth of a Gaussian-spread experiment via the relation
   <x^2>(t) ~ <x^2>(0) + 2 * d * D_eff * t.

2. **compare_to_heat_equation** — solves the heat equation analytically
   (Gaussian or error-function) with the fitted D_eff and computes the
   L2 error, shape similarity, and variance trajectory agreement between
   the ED solution and the heat-equation reference.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

import numpy as np
from scipy.special import erfc

from ..core.parameters import EDParameters
from ..core.constitutive import enforce_bounds
from .experiments_diffusion import (
    GaussianSpreadResult,
    StepRelaxationResult,
)
from .diffusion_regime import DiffusionRegime, build_diffusion_regime


# ---------------------------------------------------------------
# Data container
# ---------------------------------------------------------------

@dataclass
class DiffusionComparisonResult:
    """Result of comparing ED to the heat equation.

    Attributes
    ----------
    D_eff_fitted : float
        Effective diffusion coefficient from variance fit.
    D_eff_predicted : float
        Predicted D_eff = D * M_star.
    D_eff_relative_error : float
        |fitted - predicted| / predicted.
    variance_fit_r2 : float
        R^2 of the linear fit to <x^2>(t).
    l2_errors : np.ndarray
        Relative L2 error between ED and heat-equation profiles at each
        snapshot (length S).
    mean_l2_error : float
        Mean relative L2 error over all snapshots.
    peak_errors : np.ndarray
        Relative error in peak amplitude at each snapshot (Gaussian only;
        NaN for step experiments).
    variance_errors : np.ndarray
        Relative error in variance at each snapshot (Gaussian only;
        NaN for step experiments).
    times : np.ndarray
        Snapshot times.
    regime : DiffusionRegime
        Regime used.
    experiment_type : str
        "gaussian" or "step".
    """

    D_eff_fitted: float
    D_eff_predicted: float
    D_eff_relative_error: float
    variance_fit_r2: float
    l2_errors: np.ndarray
    mean_l2_error: float
    peak_errors: np.ndarray
    variance_errors: np.ndarray
    times: np.ndarray
    regime: DiffusionRegime
    experiment_type: str


# ---------------------------------------------------------------
# Effective diffusion coefficient fit
# ---------------------------------------------------------------

def fit_effective_diffusion_coefficient(
    result: GaussianSpreadResult,
) -> tuple[float, float]:
    """Fit D_eff from the variance trajectory of a Gaussian-spread run.

    The heat equation predicts

        <x^2>(t) = <x^2>(0) + 2 * d * D_eff * t

    so a linear fit of <x^2> vs t gives slope = 2 * d * D_eff.

    Parameters
    ----------
    result : GaussianSpreadResult
        Output of run_gaussian_spread().

    Returns
    -------
    tuple[float, float]
        (D_eff, R_squared) where D_eff is the fitted coefficient and
        R_squared is the goodness of fit.
    """
    t = result.times
    var = result.variances
    d = result.regime.parameters.d

    # Linear least-squares fit: var = a + b * t
    # b = 2 * d * D_eff  =>  D_eff = b / (2 * d)
    A = np.vstack([np.ones_like(t), t]).T
    coeffs, residuals, _, _ = np.linalg.lstsq(A, var, rcond=None)
    intercept, slope = coeffs

    D_eff = slope / (2.0 * d)

    # R^2
    ss_res = np.sum((var - (intercept + slope * t)) ** 2)
    ss_tot = np.sum((var - np.mean(var)) ** 2)
    R2 = 1.0 - ss_res / (ss_tot + 1e-30)

    return float(D_eff), float(R2)


# ---------------------------------------------------------------
# Heat-equation analytical solutions
# ---------------------------------------------------------------

def _heat_gaussian(
    params: EDParameters,
    sigma0: float,
    A0: float,
    D_eff: float,
    t: float,
) -> np.ndarray:
    """Analytical Gaussian solution to the heat equation on R^d.

    rho(x, t) = rho_star + A(t) * exp(-|x - x_c|^2 / (2 sigma(t)^2))

    where sigma(t)^2 = sigma0^2 + 2 * D_eff * t
    and   A(t) = A0 * (sigma0 / sigma(t))^d   (mass conservation).

    The infinite-domain solution is used; boundary effects are negligible
    for short times and moderate sigma relative to the domain size.
    """
    grid = params.make_grid()
    coords = np.meshgrid(*grid, indexing="ij")
    r2 = np.zeros(params.N)
    for axis in range(params.d):
        centre = params.L[axis] / 2.0
        r2 += (coords[axis] - centre) ** 2

    sigma_t2 = sigma0 ** 2 + 2.0 * D_eff * t
    sigma_t = np.sqrt(sigma_t2)
    A_t = A0 * (sigma0 / sigma_t) ** params.d

    rho = params.rho_star + A_t * np.exp(-r2 / (2.0 * sigma_t2))
    return rho


def _heat_step(
    x: np.ndarray,
    params: EDParameters,
    delta: float,
    width: float,
    D_eff: float,
    t: float,
) -> np.ndarray:
    """Analytical error-function solution for the step relaxation.

    The initial profile is approximately

        rho(x,0) ~ rho_star + delta * tanh((x - L/2) / width)

    For small width the tanh is nearly a step, and the heat-equation
    solution is

        rho(x,t) = rho_star + delta * erf((x - L/2) / sqrt(4 D_eff t + 2 width^2))

    We use erf rather than erfc for notational clarity.
    """
    centre = params.L[0] / 2.0
    effective_width = np.sqrt(2.0 * width ** 2 + 4.0 * D_eff * t)
    from scipy.special import erf
    return params.rho_star + delta * erf((x - centre) / effective_width)


# ---------------------------------------------------------------
# Comparison driver
# ---------------------------------------------------------------

def compare_to_heat_equation(
    result,
    D_eff: float,
) -> DiffusionComparisonResult:
    """Compare ED profiles to heat-equation analytical solutions.

    Parameters
    ----------
    result : GaussianSpreadResult or StepRelaxationResult
        Output of either experiment.
    D_eff : float
        Effective diffusion coefficient (from fit or prediction).

    Returns
    -------
    DiffusionComparisonResult
        Full comparison output.
    """
    regime = result.regime
    params = regime.parameters
    times = result.times

    if isinstance(result, GaussianSpreadResult):
        return _compare_gaussian(result, D_eff, regime, params, times)
    elif isinstance(result, StepRelaxationResult):
        return _compare_step(result, D_eff, regime, params, times)
    else:
        raise TypeError(f"Unknown result type: {type(result)}")


def _compare_gaussian(
    result: GaussianSpreadResult,
    D_eff: float,
    regime: DiffusionRegime,
    params: EDParameters,
    times: np.ndarray,
) -> DiffusionComparisonResult:
    """Compare Gaussian-spread ED profiles to the analytical Gaussian."""

    l2_errors = []
    peak_errors = []
    variance_errors = []

    for i, t in enumerate(times):
        rho_ed = result.series.fields[i]
        rho_heat = _heat_gaussian(params, result.sigma0, result.A0, D_eff, t)

        # Relative L2 error
        diff = rho_ed - rho_heat
        norm_heat = np.sqrt(np.sum((rho_heat - params.rho_star) ** 2))
        norm_diff = np.sqrt(np.sum(diff ** 2))
        rel_l2 = norm_diff / (norm_heat + 1e-30)
        l2_errors.append(rel_l2)

        # Peak error
        peak_ed = float(np.max(rho_ed - params.rho_star))
        sigma_t = np.sqrt(result.sigma0 ** 2 + 2.0 * D_eff * t)
        peak_heat = result.A0 * (result.sigma0 / sigma_t) ** params.d
        rel_peak = abs(peak_ed - peak_heat) / (peak_heat + 1e-30)
        peak_errors.append(rel_peak)

        # Variance error
        var_heat = result.sigma0 ** 2 + 2.0 * D_eff * t
        var_ed = result.variances[i]
        rel_var = abs(var_ed - var_heat) / (var_heat + 1e-30)
        variance_errors.append(rel_var)

    l2_arr = np.array(l2_errors)
    peak_arr = np.array(peak_errors)
    var_arr = np.array(variance_errors)

    D_eff_fitted, R2 = fit_effective_diffusion_coefficient(result)
    D_pred = regime.expected_D_eff

    return DiffusionComparisonResult(
        D_eff_fitted=D_eff_fitted,
        D_eff_predicted=D_pred,
        D_eff_relative_error=abs(D_eff_fitted - D_pred) / (D_pred + 1e-30),
        variance_fit_r2=R2,
        l2_errors=l2_arr,
        mean_l2_error=float(np.mean(l2_arr)),
        peak_errors=peak_arr,
        variance_errors=var_arr,
        times=times,
        regime=regime,
        experiment_type="gaussian",
    )


def _compare_step(
    result: StepRelaxationResult,
    D_eff: float,
    regime: DiffusionRegime,
    params: EDParameters,
    times: np.ndarray,
) -> DiffusionComparisonResult:
    """Compare step-relaxation ED profiles to the analytical erf solution."""

    # Infer delta and width from the initial midline profile
    x = result.x_coords
    prof0 = result.midline_profiles[0]
    delta = float(np.max(prof0) - params.rho_star)
    # Estimate initial width from the midline gradient
    grad_max = float(np.max(np.abs(np.gradient(prof0, x))))
    width_est = delta / (grad_max + 1e-30)

    l2_errors = []

    for i, t in enumerate(times):
        prof_ed = result.midline_profiles[i]
        prof_heat = _heat_step(x, params, delta, width_est, D_eff, t)

        diff = prof_ed - prof_heat
        norm_heat = np.sqrt(np.sum((prof_heat - params.rho_star) ** 2))
        norm_diff = np.sqrt(np.sum(diff ** 2))
        rel_l2 = norm_diff / (norm_heat + 1e-30)
        l2_errors.append(rel_l2)

    l2_arr = np.array(l2_errors)

    return DiffusionComparisonResult(
        D_eff_fitted=D_eff,
        D_eff_predicted=regime.expected_D_eff,
        D_eff_relative_error=abs(D_eff - regime.expected_D_eff) / (regime.expected_D_eff + 1e-30),
        variance_fit_r2=float("nan"),  # no variance fit for step
        l2_errors=l2_arr,
        mean_l2_error=float(np.mean(l2_arr)),
        peak_errors=np.full(len(times), np.nan),
        variance_errors=np.full(len(times), np.nan),
        times=times,
        regime=regime,
        experiment_type="step",
    )


# ---------------------------------------------------------------
# End-to-end convenience
# ---------------------------------------------------------------

@dataclass
class FullDiffusionStudy:
    """Complete output of the diffusion study.

    Attributes
    ----------
    regime : DiffusionRegime
    gaussian_result : GaussianSpreadResult
    step_result : StepRelaxationResult
    gaussian_comparison : DiffusionComparisonResult
    step_comparison : DiffusionComparisonResult
    report : str
        Human-readable physics report.
    """

    regime: DiffusionRegime
    gaussian_result: GaussianSpreadResult
    step_result: StepRelaxationResult
    gaussian_comparison: DiffusionComparisonResult
    step_comparison: DiffusionComparisonResult
    report: str


def run_full_diffusion_study(
    d: int = 2,
    N: int = 64,
    T: float = 0.5,
) -> FullDiffusionStudy:
    """Run both diffusion experiments, fit D_eff, compare, and report.

    Parameters
    ----------
    d : int
        Spatial dimension (default 2).
    N : int
        Grid points per axis (default 64).
    T : float
        Final time (default 0.5).

    Returns
    -------
    FullDiffusionStudy
        Complete study output.
    """
    from .experiments_diffusion import run_gaussian_spread, run_step_relaxation

    regime = build_diffusion_regime(d=d, N_per_axis=N, T=T)

    # Experiment 1: Gaussian spread
    gauss = run_gaussian_spread(regime=regime, sigma=0.08, amplitude=0.03)

    # Fit D_eff from variance growth
    D_eff_fitted, R2 = fit_effective_diffusion_coefficient(gauss)

    # Compare Gaussian to heat equation using fitted D_eff
    gauss_cmp = compare_to_heat_equation(gauss, D_eff_fitted)

    # Experiment 2: Step relaxation
    step = run_step_relaxation(regime=regime, delta=0.03, width=0.02)

    # Compare step to heat equation using the same fitted D_eff
    step_cmp = compare_to_heat_equation(step, D_eff_fitted)

    # Build report
    report = _build_report(regime, gauss, gauss_cmp, step, step_cmp)

    return FullDiffusionStudy(
        regime=regime,
        gaussian_result=gauss,
        step_result=step,
        gaussian_comparison=gauss_cmp,
        step_comparison=step_cmp,
        report=report,
    )


def _build_report(
    regime: DiffusionRegime,
    gauss: GaussianSpreadResult,
    gauss_cmp: DiffusionComparisonResult,
    step: StepRelaxationResult,
    step_cmp: DiffusionComparisonResult,
) -> str:
    """Build a physics-style Markdown report."""

    params = regime.parameters
    d = params.d

    lines = [
        "# ED-PHYS-01: ED as an Effective Diffusion Equation",
        "",
        "## Regime",
        "",
        f"- Dimension: {d}D",
        f"- Grid: {params.N[0]} per axis ({params.total_grid_points} points)",
        f"- D = {params.D}, M_star = {params.M_star:.4f}, P0 = {params.P0}",
        f"- H = {params.H} (no participation)",
        f"- Predicted D_eff = D * M_star = {regime.expected_D_eff:.6f}",
        "",
        "## Experiment 1: Gaussian Spread",
        "",
        f"- Initial width: sigma_0 = {gauss.sigma0}",
        f"- Initial amplitude: A_0 = {gauss.A0}",
        f"- Variance at t=0: {gauss.variances[0]:.6f}",
        f"- Variance at t={gauss.times[-1]:.4f}: {gauss.variances[-1]:.6f}",
        f"- Fitted D_eff = {gauss_cmp.D_eff_fitted:.6f}",
        f"- Predicted D_eff = {gauss_cmp.D_eff_predicted:.6f}",
        f"- Relative error: {gauss_cmp.D_eff_relative_error:.4f} "
        f"({gauss_cmp.D_eff_relative_error*100:.2f}%)",
        f"- Variance fit R^2 = {gauss_cmp.variance_fit_r2:.6f}",
        "",
        "### Profile Comparison (Gaussian vs Heat Equation)",
        "",
        "| Snapshot | Time | Rel L2 Error | Peak Error | Variance Error |",
        "|----------|------|-------------|------------|----------------|",
    ]

    for i in range(len(gauss_cmp.times)):
        lines.append(
            f"| {i} | {gauss_cmp.times[i]:.4f} "
            f"| {gauss_cmp.l2_errors[i]:.4e} "
            f"| {gauss_cmp.peak_errors[i]:.4e} "
            f"| {gauss_cmp.variance_errors[i]:.4e} |"
        )

    lines.extend([
        "",
        f"**Mean relative L2 error: {gauss_cmp.mean_l2_error:.4e}**",
        "",
        "## Experiment 2: Step Relaxation",
        "",
        f"- Step half-amplitude: delta = 0.03",
        f"- Initial smoothing width: w = 0.02",
        f"- D_eff used: {step_cmp.D_eff_fitted:.6f} (from Gaussian fit)",
        "",
        "### Midline Profile Comparison (Step vs erfc)",
        "",
        "| Snapshot | Time | Rel L2 Error |",
        "|----------|------|-------------|",
    ])

    for i in range(len(step_cmp.times)):
        lines.append(
            f"| {i} | {step_cmp.times[i]:.4f} "
            f"| {step_cmp.l2_errors[i]:.4e} |"
        )

    lines.extend([
        "",
        f"**Mean relative L2 error: {step_cmp.mean_l2_error:.4e}**",
        "",
        "## Conclusions",
        "",
    ])

    # Assess success
    gauss_ok = gauss_cmp.D_eff_relative_error < 0.15
    step_ok = step_cmp.mean_l2_error < 0.2
    r2_ok = gauss_cmp.variance_fit_r2 > 0.95

    if gauss_ok and step_ok and r2_ok:
        lines.append(
            "**The ED PDE in the weak-penalty, zero-participation regime "
            "behaves as an effective diffusion equation.**"
        )
        lines.append("")
        lines.append(
            f"The fitted D_eff = {gauss_cmp.D_eff_fitted:.6f} agrees with the "
            f"prediction D * M_star = {gauss_cmp.D_eff_predicted:.6f} to within "
            f"{gauss_cmp.D_eff_relative_error*100:.1f}%.  The variance grows "
            f"linearly (R^2 = {gauss_cmp.variance_fit_r2:.4f}).  The Gaussian "
            f"and step profiles match the heat-equation solutions with mean "
            f"relative L2 errors of {gauss_cmp.mean_l2_error:.2e} and "
            f"{step_cmp.mean_l2_error:.2e} respectively."
        )
    else:
        lines.append(
            "**The diffusion approximation is only partially successful.**"
        )
        lines.append("")
        if not gauss_ok:
            lines.append(
                f"- D_eff error ({gauss_cmp.D_eff_relative_error*100:.1f}%) "
                f"exceeds the 15% threshold."
            )
        if not r2_ok:
            lines.append(
                f"- Variance fit R^2 = {gauss_cmp.variance_fit_r2:.4f} < 0.95."
            )
        if not step_ok:
            lines.append(
                f"- Step mean L2 error ({step_cmp.mean_l2_error:.2e}) "
                f"exceeds the 0.2 threshold."
            )
        lines.append("")
        lines.append(
            "Residual nonlinearity (mobility variation, weak penalty) "
            "prevents exact agreement with the linear heat equation."
        )

    lines.extend([
        "",
        "## Limitations",
        "",
        "- Comparison uses the infinite-domain Gaussian solution; Neumann "
        "boundaries introduce reflections that grow with time.",
        "- The mobility M(rho) is not exactly constant at rho = rho_star; "
        "deviations scale as O(A^2 / (rho_max - rho_star)^2).",
        "- The weak penalty P0 = 0.01 produces a slow drift toward rho_star "
        "that is absent in the pure heat equation.",
        "- For large amplitudes or long times the nonlinear terms dominate "
        "and the diffusion approximation breaks down.",
    ])

    return "\n".join(lines)
