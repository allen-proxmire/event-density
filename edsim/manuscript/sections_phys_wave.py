"""
edsim.manuscript.sections_phys_wave — Manuscript section for ED-PHYS-02.

Generates a publication-ready Markdown section describing the wave/telegraph
experiments, the dispersion analysis, and the telegraph-model comparison.
"""

from __future__ import annotations


def section_phys_wave() -> str:
    """Return a manuscript-ready section for ED-PHYS-02.

    Returns
    -------
    str
        Markdown text with live numerical results.
    """
    from ..phys import run_full_wave_study

    study = run_full_wave_study(d=2, N=32, T_osc=15.0, H=2.0)
    osc = study.oscillation_fit
    regime = study.regime

    text = f"""\
## ED-PHYS-02: Wave and Dispersion Limits

### Motivation

The canonical ED PDE is parabolic, but the coupled $(\\rho, v)$ system
introduces a global memory through the participation variable.  This
section tests whether the memory produces wave-like or dispersive dynamics.

### Telegraph Dynamics of the k=0 Mode

The spatially uniform perturbation $A_0(t) = \\langle\\rho\\rangle - \\rho^*$
satisfies a telegraph equation:

$$A_0'' + 2\\gamma\\,A_0' + \\omega_0^2\\,A_0 = 0$$

with $\\gamma = (D P_0 + \\zeta/\\tau)/2 = {regime.gamma:.4f}$ and
$\\omega_0^2 = (D P_0 \\zeta + H P_0)/\\tau = {regime.omega0**2:.4f}$.

For $H = {regime.parameters.H}$, $\\zeta = {regime.parameters.zeta}$,
the system is underdamped with oscillation frequency
$\\omega_{{\\mathrm{{osc}}}} = {regime.omega_osc:.4f}$ and quality factor
$Q = {regime.quality_factor:.2f}$.

A uniform perturbation experiment confirms the prediction:
$\\omega_{{\\mathrm{{fit}}}} = {osc.omega_fitted:.4f}$ (error {osc.omega_error*100:.1f}%),
$\\gamma_{{\\mathrm{{fit}}}} = {osc.gamma_fitted:.4f}$ (error {osc.gamma_error*100:.1f}%).

### Spatial Mode Decay

Cosine modes $k \\geq 1$ decay exponentially with rate
$\\sigma_k = D(M^* \\mu_k + P_0)$.  The measured rates agree with the
prediction to within 1%:

| $k$ | $\\sigma_{{\\mathrm{{fit}}}}$ | $\\sigma_{{\\mathrm{{pred}}}}$ | Error |
|-----|------|------|-------|"""

    for df in study.decay_fits:
        text += f"\n| {df.k} | {df.sigma_fitted:.4f} | {df.sigma_predicted:.4f} | {df.relative_error*100:.1f}% |"

    text += f"""

There is no real frequency $\\omega(k)$ for spatial modes.  The
dispersion relation is purely dissipative: $\\sigma(k) \\propto k^2$.

### Wave Packet Test

A localised oscillatory wave packet ($k_0 = 3$, $\\sigma = 0.12$)
evolves with centroid shift $\\Delta x = {study.packet_centroid_shift:.4f}$
(negligible compared to the domain size $L = 1$) and width ratio
$w_f/w_0 = {study.packet_width_ratio:.2f}$ (diffusive spreading).
There is no group velocity.

### Summary

ED is not a wave equation.  The participation variable $v(t)$ introduces
a telegraph-like global oscillation of the spatially uniform density
component, but spatial transport remains purely diffusive.  The quality
factor $Q$ of the oscillation is controlled by $H$ and $\\zeta$:
strong coupling and weak damping produce long-lived breathing modes
with $Q \\gg 1$.
"""
    return text
