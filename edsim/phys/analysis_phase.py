"""
edsim.phys.analysis_phase — Phase diagram analysis and report generation.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

import numpy as np

from .phase_diagram import (
    PhaseDiagram,
    PhasePoint,
    build_phase_diagram,
)
from .experiments_phase import (
    PhaseValidation,
    validate_phase_diagram,
)


@dataclass
class PhaseStudyResult:
    """Complete output of the phase diagram study."""

    diagram: PhaseDiagram
    validations: list
    report: str


def run_full_phase_study(
    M0_values: Optional[list] = None,
    P0_values: Optional[list] = None,
    H_values: Optional[list] = None,
    n_validate: int = 8,
) -> PhaseStudyResult:
    """Build the phase diagram, validate a sample, and report.

    Parameters
    ----------
    M0_values, P0_values, H_values : list[float], optional
    n_validate : int
        Number of points to validate numerically (default 8).

    Returns
    -------
    PhaseStudyResult
    """
    diagram = build_phase_diagram(M0_values, P0_values, H_values)
    validations = validate_phase_diagram(diagram.points, sample=n_validate)
    report = _build_report(diagram, validations)

    return PhaseStudyResult(
        diagram=diagram,
        validations=validations,
        report=report,
    )


def _build_report(diagram: PhaseDiagram, validations: list) -> str:
    """Build a physics-style Markdown report."""

    n_total = len(diagram.points)
    lines = [
        "# ED-PHYS-06: Global Phase Diagram of Event Density",
        "",
        "## Parameter Space",
        "",
        f"- M0 values: {diagram.M0_values}",
        f"- P0 values: {diagram.P0_values}",
        f"- H values:  {diagram.H_values}",
        f"- Total grid points: {n_total}",
        "",
        "## Phase Classification",
        "",
        "| Phase | Count | Fraction |",
        "|-------|-------|----------|",
    ]

    for phase in ["diffusion", "reaction", "telegraph", "transient", "quantum_like"]:
        count = diagram.phase_counts.get(phase, 0)
        frac = count / n_total if n_total > 0 else 0
        lines.append(f"| {phase} | {count} | {frac:.1%} |")

    # Phase boundary analysis
    lines.extend([
        "",
        "## Phase Boundaries",
        "",
        "### Diffusion vs Reaction",
        "",
        "The boundary is determined by the diffusion-reaction ratio "
        "R = D_eff * pi^2 / (D * P0) = M_star * pi^2 / P0.",
        "",
        "- R >> 1: diffusion-dominated",
        "- R << 1: reaction-dominated",
        "- R ~ 1: transient (competing timescales)",
        "",
        "### Telegraph Boundary",
        "",
        "Underdamped oscillation requires omega_0^2 > gamma^2, which "
        "gives Q >= 1.  For most P0 values, even small H > 0 is sufficient "
        "because gamma is small.  The telegraph phase therefore occupies "
        "most of the H > 0 region.",
        "",
        "### Quantum-Like Region",
        "",
        "Defined by high mobility (M0 >= 2), weak penalty (P0 <= 0.1), "
        "and strong participation (H >= 1).  This is a corner of the "
        "parameter space where nonlinear mobility effects and telegraph "
        "oscillation are both strong.",
        "",
        "## Full Grid (sorted by phase)",
        "",
        "| M0 | P0 | H | Phase | D_eff | lambda | Q | tau_morph |",
        "|----|----|---|-------|-------|--------|---|----------|",
    ])

    sorted_pts = sorted(diagram.points, key=lambda p: (p.classification, p.M0, p.P0, p.H))
    for p in sorted_pts:
        m = p.metrics
        lines.append(
            f"| {p.M0:.1f} | {p.P0:.2f} | {p.H:.1f} "
            f"| {p.classification} "
            f"| {m.D_eff:.4f} | {m.lambda_eff:.4f} "
            f"| {m.Q:.2f} | {m.complexity_lifetime:.3f} |"
        )

    # Validation results
    lines.extend([
        "",
        "## Numerical Validation",
        "",
        f"Validated {len(validations)} points with short diagnostic simulations.",
        "",
        "| M0 | P0 | H | Phase | E mono | C decays | Oscillates | n_osc |",
        "|----|----|---|-------|--------|----------|------------|-------|",
    ])

    for v in validations:
        p = v.point
        lines.append(
            f"| {p.M0:.1f} | {p.P0:.2f} | {p.H:.1f} "
            f"| {p.classification} "
            f"| {v.energy_monotone} | {v.complexity_decays} "
            f"| {v.mean_rho_oscillates} | {v.n_oscillations} |"
        )

    # Check consistency
    n_valid = len(validations)
    n_E_ok = sum(1 for v in validations if v.energy_monotone)
    n_C_ok = sum(1 for v in validations if v.complexity_decays)
    n_osc_match = sum(
        1 for v in validations
        if (v.point.classification == "telegraph" and v.mean_rho_oscillates) or
           (v.point.classification != "telegraph" and v.point.H == 0.0)
    )

    lines.extend([
        "",
        f"- Energy monotone: {n_E_ok}/{n_valid}",
        f"- Complexity decays: {n_C_ok}/{n_valid}",
        "",
        "## Summary",
        "",
        "The ED PDE parameter space is partitioned into five phases "
        "with clear analytical boundaries:",
        "",
        f"- **Diffusion** ({diagram.phase_counts.get('diffusion', 0)} points): "
        "low P0/M0 ratio, Laplacian dominates.",
        f"- **Reaction** ({diagram.phase_counts.get('reaction', 0)} points): "
        "high P0/M0 ratio, penalty dominates.",
        f"- **Telegraph** ({diagram.phase_counts.get('telegraph', 0)} points): "
        "H large enough for underdamped oscillation (Q >= 1).",
        f"- **Transient** ({diagram.phase_counts.get('transient', 0)} points): "
        "competing diffusion and reaction timescales.",
        f"- **Quantum-like** ({diagram.phase_counts.get('quantum_like', 0)} points): "
        "high mobility + weak penalty + strong participation.",
        "",
        "The telegraph phase dominates because even small H produces "
        "underdamped oscillation.  The quantum-like phase is a narrow "
        "corner requiring all three conditions simultaneously.",
    ])

    return "\n".join(lines)
