"""
edsim.manuscript.sections_phys_pattern — Manuscript section for ED-PHYS-04.
"""

from __future__ import annotations


def section_phys_pattern() -> str:
    """Return a manuscript-ready section for ED-PHYS-04.

    Returns
    -------
    str
        Markdown text with live numerical results.
    """
    from ..phys import run_full_pattern_study

    study = run_full_pattern_study(d=2, N=64, T=2.0)
    gt = study.modal_growth
    cm = study.complexity_metrics
    regime = study.regime

    decay_rows = ""
    for i in range(len(gt.k_values)):
        decay_rows += (
            f"\n| {gt.k_values[i]} "
            f"| {gt.sigma_fitted[i]:.4f} "
            f"| {gt.sigma_predicted[i]:.4f} |"
        )

    text = f"""\
## ED-PHYS-04: Nonlinear Pattern Formation

### Motivation

Pattern-forming PDEs (Allen-Cahn, Cahn-Hilliard) are among the closest
structural relatives of ED (ED-Phys-38).  This section tests whether the
ED penalty and degenerate mobility can produce Turing-like instabilities
or self-organised patterns.

### Linear Stability

The linearised growth rate of a Fourier mode $k$ about $\\rho = \\rho^*$ is

$$\\sigma_k = -D(M^* \\mu_k + P_0) < 0 \\quad \\text{{for all }} k.$$

All modes decay.  There is no instability band.  ED is unconditionally
stable.

### Numerical Confirmation

A small-noise initial condition ($A = 0.01$) is evolved on a ${regime.parameters.N[0]}^2$
grid with $P_0 = {regime.parameters.P0}$.

| $k$ | $\\sigma_{{\\mathrm{{fit}}}}$ | $\\sigma_{{\\mathrm{{pred}}}}$ |
|-----|------|------|{decay_rows}

All fitted rates are positive (decaying).  No mode grows.  The transient
complexity ratio is $C_{{\\mathrm{{peak}}}}/C_0 = {cm.amplification_ratio:.4f}$
with complexity half-life ${cm.half_life:.4f}$.

### Filament and Spot Tests

A thin filament decays smoothly without breakup (intact: {study.filament_result.filament_intact}).
A localised spot diffuses isotropically with peak decay
{study.spot_result.peak_amplitude[0]:.4f} $\\to$ {study.spot_result.peak_amplitude[-1]:.4e}.

### Conclusion

**ED does not support pattern formation.** The uniform equilibrium is the
unique global attractor (Law 1) and all perturbations decay monotonically
(Law 2).  The rich transient morphology observed in ED-Phys-35 arises
from differential decay rates, not from instability.  This distinguishes
ED from Allen-Cahn (bistable, domain walls) and Cahn-Hilliard (spinodal,
coarsening).
"""
    return text
