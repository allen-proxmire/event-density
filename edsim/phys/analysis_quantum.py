"""
edsim.phys.analysis_quantum — Quantum-regime analysis: variance scaling,
effective dispersion, and interference features.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Optional

import numpy as np

from .quantum_regime import QuantumRegime, build_quantum_regime
from .experiments_quantum import (
    AnomalousSpreadResult,
    DoubleBumpResult,
    OscillatoryEnvelopeResult,
    run_anomalous_spread,
    run_double_bump_interference,
    run_oscillatory_envelope,
)


# ---------------------------------------------------------------
# Data containers
# ---------------------------------------------------------------

@dataclass
class VarianceScalingFit:
    """Fit of <x^2>(t) ~ t^alpha.

    Attributes
    ----------
    alpha : float
        Variance scaling exponent (1 = normal, <1 = sub, >1 = super).
    r_squared : float
    D_eff_linear : float
        D_eff from a linear fit (assumes alpha=1).
    mean_kurtosis : float
        Mean excess kurtosis (0 = Gaussian, >0 = heavy tails).
    """

    alpha: float
    r_squared: float
    D_eff_linear: float
    mean_kurtosis: float


@dataclass
class InterferenceMetrics:
    """Metrics for the double-bump interference test.

    Attributes
    ----------
    mean_overlap_error : float
        Mean relative L2 error between double-bump and linear superposition.
    max_overlap_error : float
    overlap_grows : bool
        Whether the error increases with time (nonlinear coupling builds up).
    """

    mean_overlap_error: float
    max_overlap_error: float
    overlap_grows: bool


@dataclass
class EnvelopeMetrics:
    """Metrics for the oscillatory envelope test.

    Attributes
    ----------
    n_oscillations : int
    omega_measured : float
    omega_predicted : float
    omega_error : float
    envelope_decay_rate : float
    """

    n_oscillations: int
    omega_measured: float
    omega_predicted: float
    omega_error: float
    envelope_decay_rate: float


@dataclass
class QuantumStudyResult:
    """Complete output of the quantum study."""

    regime: QuantumRegime
    spread_result: AnomalousSpreadResult
    double_result: DoubleBumpResult
    envelope_result: OscillatoryEnvelopeResult
    variance_fit: VarianceScalingFit
    interference: InterferenceMetrics
    envelope_metrics: EnvelopeMetrics
    report: str


# ---------------------------------------------------------------
# Variance scaling
# ---------------------------------------------------------------

def fit_variance_scaling(result: AnomalousSpreadResult) -> VarianceScalingFit:
    """Fit <x^2>(t) ~ t^alpha on a log-log scale.

    Parameters
    ----------
    result : AnomalousSpreadResult

    Returns
    -------
    VarianceScalingFit
    """
    t = result.times
    var = result.variances
    d = result.regime.parameters.d

    # Exclude t=0 for log-log fit
    mask = (t > 1e-10) & (var > 1e-14)
    if np.sum(mask) < 3:
        return VarianceScalingFit(alpha=1.0, r_squared=0.0,
                                  D_eff_linear=0.0, mean_kurtosis=0.0)

    log_t = np.log(t[mask])
    log_v = np.log(var[mask])
    coeffs = np.polyfit(log_t, log_v, 1)
    alpha = coeffs[0]

    fit_vals = np.polyval(coeffs, log_t)
    ss_res = np.sum((log_v - fit_vals) ** 2)
    ss_tot = np.sum((log_v - np.mean(log_v)) ** 2)
    r2 = 1.0 - ss_res / (ss_tot + 1e-30)

    # Linear D_eff (assumes alpha=1)
    t_lin = t[mask]
    var_lin = var[mask]
    c_lin = np.polyfit(t_lin, var_lin, 1)
    D_eff_linear = c_lin[0] / (2.0 * d) if d > 0 else 0.0

    mean_kurt = float(np.mean(result.kurtosis[mask]))

    return VarianceScalingFit(
        alpha=float(alpha), r_squared=float(r2),
        D_eff_linear=float(D_eff_linear), mean_kurtosis=mean_kurt,
    )


# ---------------------------------------------------------------
# Interference features
# ---------------------------------------------------------------

def detect_interference_features(result: DoubleBumpResult) -> InterferenceMetrics:
    """Analyse the double-bump overlap error.

    Parameters
    ----------
    result : DoubleBumpResult

    Returns
    -------
    InterferenceMetrics
    """
    err = result.overlap_error
    mean_err = float(np.mean(err))
    max_err = float(np.max(err))

    # Does the error grow over time?  Check if the second half is larger than the first.
    n = len(err)
    if n > 4:
        first_half = float(np.mean(err[:n // 2]))
        second_half = float(np.mean(err[n // 2:]))
        grows = second_half > first_half * 1.1
    else:
        grows = False

    return InterferenceMetrics(
        mean_overlap_error=mean_err,
        max_overlap_error=max_err,
        overlap_grows=grows,
    )


# ---------------------------------------------------------------
# Envelope oscillation
# ---------------------------------------------------------------

def analyse_envelope(result: OscillatoryEnvelopeResult) -> EnvelopeMetrics:
    """Extract oscillation frequency and decay rate from the envelope.

    Parameters
    ----------
    result : OscillatoryEnvelopeResult

    Returns
    -------
    EnvelopeMetrics
    """
    t = result.times
    delta_mean = result.mean_rho - result.regime.parameters.rho_star
    regime = result.regime

    # Frequency from zero crossings
    crossings = []
    for j in range(len(delta_mean) - 1):
        if delta_mean[j] * delta_mean[j + 1] < 0:
            t_cross = t[j] - delta_mean[j] * (t[j + 1] - t[j]) / (
                delta_mean[j + 1] - delta_mean[j] + 1e-30)
            crossings.append(t_cross)

    if len(crossings) >= 2:
        half_periods = np.diff(crossings)
        omega_meas = math.pi / float(np.mean(half_periods))
    else:
        omega_meas = 0.0

    omega_pred = regime.telegraph_omega
    omega_err = abs(omega_meas - omega_pred) / (omega_pred + 1e-30)

    # Envelope decay from Hilbert transform
    env_decay = 0.0
    abs_delta = np.abs(delta_mean)
    mask = abs_delta > 1e-14
    if np.sum(mask) >= 3:
        c = np.polyfit(t[mask], np.log(abs_delta[mask]), 1)
        env_decay = -c[0]

    return EnvelopeMetrics(
        n_oscillations=result.n_oscillations,
        omega_measured=omega_meas,
        omega_predicted=omega_pred,
        omega_error=omega_err,
        envelope_decay_rate=env_decay,
    )


# ---------------------------------------------------------------
# End-to-end study
# ---------------------------------------------------------------

def run_full_quantum_study(
    d: int = 2,
    N: int = 64,
    T: float = 3.0,
) -> QuantumStudyResult:
    """Run all three quantum experiments, analyse, and produce a report.

    Parameters
    ----------
    d : int
    N : int
    T : float

    Returns
    -------
    QuantumStudyResult
    """
    regime = build_quantum_regime(d=d, N_per_axis=N, T=T)

    spread = run_anomalous_spread(regime=regime)
    var_fit = fit_variance_scaling(spread)

    double = run_double_bump_interference(regime=regime)
    interf = detect_interference_features(double)

    envelope = run_oscillatory_envelope(regime=regime)
    env_m = analyse_envelope(envelope)

    report = _build_report(regime, spread, var_fit, double, interf, envelope, env_m)

    return QuantumStudyResult(
        regime=regime,
        spread_result=spread,
        double_result=double,
        envelope_result=envelope,
        variance_fit=var_fit,
        interference=interf,
        envelope_metrics=env_m,
        report=report,
    )


def _build_report(regime, spread, var_fit, double, interf, envelope, env_m):
    """Build a physics-style Markdown report."""
    params = regime.parameters

    alpha_class = "normal"
    if var_fit.alpha > 1.05:
        alpha_class = "superdiffusive"
    elif var_fit.alpha < 0.95:
        alpha_class = "subdiffusive"

    lines = [
        "# ED-PHYS-05: Quantum-Like Regime Tests for Event Density",
        "",
        "## Regime",
        "",
        f"- Dimension: {params.d}D, grid {params.N[0]}^{params.d}",
        f"- M0 = {params.M0} (high mobility), P0 = {params.P0} (weak penalty)",
        f"- H = {params.H} (strong participation), zeta = {params.zeta}",
        f"- D_eff = {regime.D_eff:.4f}",
        f"- Telegraph: omega = {regime.telegraph_omega:.4f}, "
        f"Q = {regime.telegraph_Q:.2f}",
        f"- Mobility variation at A={regime.ic_amplitude}: "
        f"{regime.mobility_variation*100:.1f}%",
        "",
        "## Experiment 1: Anomalous Spreading",
        "",
        f"- Initial bump: sigma_0 = {spread.sigma0}, A = {spread.A0}",
        f"- Variance scaling exponent: **alpha = {var_fit.alpha:.4f}**",
        f"  (R^2 = {var_fit.r_squared:.4f})",
        f"- Classification: **{alpha_class}**",
        f"- Linear D_eff = {var_fit.D_eff_linear:.6f} "
        f"(predicted {regime.D_eff:.6f})",
        f"- Mean excess kurtosis: {var_fit.mean_kurtosis:.4f} "
        f"({'Gaussian' if abs(var_fit.mean_kurtosis) < 0.5 else 'non-Gaussian'})",
        "",
    ]

    if abs(var_fit.alpha - 1.0) < 0.1:
        lines.extend([
            "The variance growth is consistent with normal diffusion "
            f"(alpha = {var_fit.alpha:.3f} ~ 1).  The nonlinear mobility "
            "correction is too weak at this amplitude to produce measurable "
            "anomalous transport.",
            "",
        ])
    else:
        lines.extend([
            f"The variance growth exponent alpha = {var_fit.alpha:.3f} deviates "
            f"from unity, indicating {'super' if var_fit.alpha > 1 else 'sub'}diffusive "
            "transport.  This arises from the density-dependent mobility: the peak "
            "spreads more slowly than the tails, creating non-Gaussian profiles.",
            "",
        ])

    lines.extend([
        "## Experiment 2: Double-Bump Interference",
        "",
        f"- Separation: {double.separation}",
        f"- Mean overlap error (vs linear superposition): "
        f"**{interf.mean_overlap_error:.4e}**",
        f"- Max overlap error: {interf.max_overlap_error:.4e}",
        f"- Overlap error grows with time: {interf.overlap_grows}",
        "",
    ])

    if interf.mean_overlap_error > 0.01:
        lines.extend([
            "The double-bump profile differs measurably from linear "
            "superposition.  The nonlinear mobility M(rho) makes the overlap "
            "region evolve differently from two independent bumps.  This is "
            "a structural analogue of wave-function interference: the "
            "interaction is nonlinear (density-dependent diffusion), not "
            "quantum (phase coherence).",
            "",
        ])
    else:
        lines.extend([
            "The double-bump profile closely matches linear superposition.  "
            "At this amplitude, the nonlinear coupling is too weak to produce "
            "measurable deviation from linearity.",
            "",
        ])

    lines.extend([
        "## Experiment 3: Oscillatory Envelope",
        "",
        f"- Oscillation count: {env_m.n_oscillations}",
        f"- omega measured: {env_m.omega_measured:.4f} "
        f"(predicted {env_m.omega_predicted:.4f}, "
        f"error {env_m.omega_error*100:.1f}%)",
        f"- Envelope decay rate: {env_m.envelope_decay_rate:.4f}",
        "",
    ])

    if env_m.n_oscillations >= 1:
        lines.extend([
            "The mean density oscillates via the telegraph mechanism "
            f"(Q = {regime.telegraph_Q:.1f}).  This creates an oscillatory "
            "envelope over the spreading profile: the global density modulation "
            "alternately compresses and rarefies the bump.  This is the ED "
            "analogue of wave-packet oscillation.",
            "",
        ])
    else:
        lines.extend([
            "No oscillation detected in the mean density.  The integration "
            "time may be too short or the amplitude too small for the "
            "telegraph mode to manifest visibly.",
            "",
        ])

    lines.extend([
        "## Summary of Quantum-Like Signatures",
        "",
        "| Signature | Detected? | Mechanism |",
        "|-----------|----------|-----------|",
        f"| Anomalous spreading (alpha != 1) | "
        f"{'Yes' if abs(var_fit.alpha - 1.0) > 0.1 else 'No'} "
        f"| Density-dependent mobility |",
        f"| Non-Gaussian profile (kurtosis) | "
        f"{'Yes' if abs(var_fit.mean_kurtosis) > 0.5 else 'No'} "
        f"| Nonlinear M(rho) |",
        f"| Interference-like overlap | "
        f"{'Yes' if interf.mean_overlap_error > 0.01 else 'No'} "
        f"| Nonlinear superposition |",
        f"| Oscillatory envelope | "
        f"{'Yes' if env_m.n_oscillations >= 1 else 'No'} "
        f"| Telegraph coupling |",
        "",
        "## Conclusions",
        "",
        "The ED PDE in the quantum-like regime produces structural analogues "
        "of several quantum transport signatures.  These arise from two "
        "classical mechanisms:",
        "",
        "1. **Nonlinear mobility** M(rho): creates density-dependent "
        "diffusion that can produce non-Gaussian profiles and anomalous "
        "variance scaling.",
        "",
        "2. **Participation coupling** (telegraph mode): creates global "
        "oscillatory modulation of the density field, analogous to "
        "wave-packet oscillation.",
        "",
        "These are structural analogies, not quantum mechanics.  The ED PDE "
        "is classical, dissipative, and parabolic.  There is no Planck "
        "constant, no superposition principle, no entanglement, and no "
        "measurement problem.  The analogies are purely dynamical: "
        "density-dependent diffusion mimics some transport signatures of "
        "quantum probability flow.",
    ])

    return "\n".join(lines)
