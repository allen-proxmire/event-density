"""
edsim.manuscript.sections_phys_phase — Manuscript section for ED-PHYS-06.
"""

from __future__ import annotations


def section_phys_phase() -> str:
    """Return a manuscript-ready section for ED-PHYS-06."""
    from ..phys import build_phase_diagram

    diagram = build_phase_diagram()
    n = len(diagram.points)
    counts = diagram.phase_counts

    text = f"""\
## ED-PHYS-06: Global Phase Diagram

### Parameter Space

The ED PDE is controlled by three parameters: mobility $M_0$, penalty $P_0$,
and participation $H$.  We evaluate a $4 \\times 4 \\times 4 = {n}$ grid
spanning $M_0 \\in {diagram.M0_values}$, $P_0 \\in {diagram.P0_values}$,
$H \\in {diagram.H_values}$.

### Phase Classification

| Phase | Count | Fraction | Defining criterion |
|-------|-------|----------|--------------------|
| Diffusion | {counts.get('diffusion', 0)} | {counts.get('diffusion', 0)/n:.0%} | $R = M^* \\pi^2 / P_0 \\geq 5$, $H = 0$ |
| Reaction | {counts.get('reaction', 0)} | {counts.get('reaction', 0)/n:.0%} | $R < 1$, $H = 0$ |
| Telegraph | {counts.get('telegraph', 0)} | {counts.get('telegraph', 0)/n:.0%} | $Q \\geq 1$ |
| Transient | {counts.get('transient', 0)} | {counts.get('transient', 0)/n:.0%} | $1 < R < 5$, $H = 0$ |
| Quantum-like | {counts.get('quantum_like', 0)} | {counts.get('quantum_like', 0)/n:.0%} | $M_0 \\geq 2$, $P_0 \\leq 0.1$, $H \\geq 1$ |

### Key Finding

The telegraph phase dominates ({counts.get('telegraph', 0)}/{n} points)
because the threshold for underdamped oscillation is low: any nonzero $H$
produces $Q \\geq 1$ for most $P_0$ values.  The diffusion and reaction
phases occupy the $H = 0$ hyperplane exclusively.

The five phases reproduce the phenomenology of ED-PHYS-01 through
ED-PHYS-05: each experiment probes a different region of the phase
diagram.

### Phase Boundaries

The diffusion--reaction boundary is $R = M^* \\pi^2 / P_0 = 1$, which
gives $P_0 = M_0 \\cdot 0.25 \\cdot \\pi^2 \\approx 2.47\\,M_0$.  The
telegraph boundary is $Q = 1$, which for canonical $\\zeta = 0.1$,
$\\tau = 1$ requires $H \\gtrsim 0.01$--$0.1$ depending on $P_0$.  The
quantum-like phase is defined by a joint condition that restricts it to
a small corner of the space.
"""
    return text
