"""
edsim.manuscript.sections_phys_interpretation — Manuscript section for ED-PHYS-08.
"""

from __future__ import annotations


def section_phys_interpretation() -> str:
    """Return a manuscript-ready section for ED-PHYS-08."""
    from ..phys import run_full_interpretation_study

    study = run_full_interpretation_study()
    matrix = study.matrix

    rows = ""
    for name, match, mismatch, plaus in matrix.ranking:
        rows += f"\n| {name} | {match}/10 | {mismatch}/10 | {plaus} |"

    text = f"""\
## ED-PHYS-08: Physical Interpretation Framework

### Methodology

Ten empirically established properties (P1--P10) from PHYS-01 through
PHYS-07 are used as scoring criteria.  Eight candidate physical domains
are evaluated on how many properties they share (match) or contradict
(mismatch).

### Interpretation Matrix

| Domain | Match | Mismatch | Plausibility |
|--------|-------|----------|-------------|{rows}

### Top Interpretation: Population/Agent Density (8/10)

The strongest match is population density models with density-dependent
dispersal and carrying capacity.  The ED parameters map as:

- $\\rho$ = population density
- $M(\\rho) = M_0(\\rho_{{\\max}} - \\rho)^\\beta$ = crowding-reduced dispersal
- $\\rho_{{\\max}}$ = carrying capacity
- $P(\\rho)$ = logistic-like penalty toward equilibrium
- $\\rho^*$ = target/equilibrium density

The only mismatches are the telegraph coupling (P4, absent in standard
population models) and the gradient-flow status (P8, many population models
are variational).

### Synthesis

ED is a **degenerate parabolic reaction-diffusion equation with global
feedback**.  Its natural physical domain spans density-dependent transport,
population dynamics, and porous-medium flow.  It is NOT a wave equation,
NOT a pattern-forming system, NOT a gradient flow, and NOT quantum mechanics.
"""
    return text
