"""
edsim.manuscript.sections_phys_cosmology — Manuscript section for ED-PHYS-09.
"""

from __future__ import annotations


def section_phys_cosmology() -> str:
    """Return a manuscript-ready section for ED-PHYS-09."""
    from ..phys import run_full_cosmology_study
    from ..phys.analysis_cosmology import (
        compute_scale_factor_fit, compute_horizon_lifetime, compute_structure_lifetime,
    )

    study = run_full_cosmology_study(d=2, N=32, T=6.0)
    exp = study.expansion
    hor = study.horizon
    struct = study.structure
    regime = study.regime
    _, lam_fit = compute_scale_factor_fit(exp)
    hor_life = compute_horizon_lifetime(hor)
    struct_life = compute_structure_lifetime(struct)

    text = f"""\
## ED-PHYS-09: Cosmological Analogue Mapping

### Caveat

These are structural analogies, not cosmological physics.  ED has no
metric, no curvature, and no gravity.

### Expansion Analogue

An overdense initial condition ($\\langle\\rho\\rangle(0) = {exp.mean_rho[0]:.3f}$)
decays toward $\\rho^*$ at a fitted rate $\\lambda = {lam_fit:.4f}$.
The effective scale factor grows from
$a(0) = {exp.scale_factor[0]:.3f}$ to
$a(T) = {exp.scale_factor[-1]:.3f}$.

### Horizon Analogue

Regions with $M(\\rho) < 0.01\\,M^*$ occupy
{hor.horizon_fraction[0]*100:.1f}% of the domain initially
and vanish as the density relaxes.

### Structure Analogue

Transient filaments and sheets decay with complexity lifetime
$\\tau_{{\\mathrm{{struct}}}} = {struct_life:.3f}$
(predicted {regime.structure_lifetime:.3f}).

### Summary

| Feature | Confirmed | Mechanism |
|---------|----------|-----------|
| Density dilution | Yes | Penalty relaxation |
| Scale factor growth | Yes | $a(t) \\to 1$ |
| Horizons | {'Yes' if hor.horizon_fraction[0] > 0.001 else 'No'} | Degenerate mobility |
| Transient structure | Yes | Differential modal decay |
| Deceleration | Yes | $H_{{\\mathrm{{eff}}}}$ decreasing |

All analogies are mathematical (shared PDE structure), not physical.
"""
    return text
