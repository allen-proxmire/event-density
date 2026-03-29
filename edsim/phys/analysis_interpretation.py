"""
edsim.phys.analysis_interpretation — Interpretation analysis and report.
"""

from __future__ import annotations

from dataclasses import dataclass

from .interpretation_matrix import (
    InterpretationMatrix,
    PhysicalDomain,
    build_interpretation_matrix,
    ED_PROPERTIES,
)


@dataclass
class InterpretationStudyResult:
    """Complete output of the interpretation study."""

    matrix: InterpretationMatrix
    top_domains: list
    report: str


def identify_plausible_domains(
    matrix: InterpretationMatrix,
    min_matches: int = 5,
) -> list[PhysicalDomain]:
    """Return domains with at least min_matches matching properties."""
    return [d for d in matrix.domains if d.match_score >= min_matches]


def run_full_interpretation_study() -> InterpretationStudyResult:
    """Build interpretation matrix, identify top domains, and report."""
    matrix = build_interpretation_matrix()
    top = identify_plausible_domains(matrix, min_matches=5)
    report = _build_report(matrix, top)

    return InterpretationStudyResult(
        matrix=matrix, top_domains=top, report=report,
    )


def _build_report(matrix: InterpretationMatrix, top: list) -> str:
    lines = [
        "# ED-PHYS-08: Physical Interpretation Framework",
        "",
        "## ED Properties Used for Scoring",
        "",
        "| # | Property | Source |",
        "|---|----------|--------|",
        "| P1 | Parabolic (diffusive) | PHYS-02 |",
        "| P2 | Effective diffusion D_eff = D M_star | PHYS-01 |",
        "| P3 | Effective reaction lambda = D P0 | PHYS-03 |",
        "| P4 | Telegraph oscillation (H > 0) | PHYS-02 |",
        "| P5 | No pattern formation | PHYS-04 |",
        "| P6 | Non-Gaussian spreading | PHYS-05 |",
        "| P7 | Five Lyapunov functionals | PHYS-07 |",
        "| P8 | NOT a gradient flow | PHYS-07 |",
        "| P9 | Unique attractor | All laws |",
        "| P10 | Degenerate mobility (horizons) | PHYS-06 |",
        "",
        "## Interpretation Matrix",
        "",
        "| Domain | Match | Mismatch | Plausibility |",
        "|--------|-------|----------|-------------|",
    ]

    for name, match, mismatch, plaus in matrix.ranking:
        lines.append(f"| {name} | {match}/10 | {mismatch}/10 | {plaus} |")

    lines.extend([
        "",
        "## Top Candidate Interpretations",
        "",
    ])

    for d in top:
        lines.extend([
            f"### {d.name} ({d.match_score}/10 matches)",
            "",
            f"**Governing equation:** {d.governing_equation}",
            "",
            "**Matches:**",
            "",
        ])
        for prop, reason in sorted(d.matches.items()):
            lines.append(f"- {prop}: {reason}")

        lines.extend(["", "**Mismatches:**", ""])
        for prop, reason in sorted(d.mismatches.items()):
            lines.append(f"- {prop}: {reason}")

        lines.extend(["", f"**Notes:** {d.notes}", ""])

    # Synthesis
    lines.extend([
        "## Synthesis",
        "",
        "The ED PDE is best interpreted as a **degenerate nonlinear "
        "reaction-diffusion equation** with the following physical readings:",
        "",
        "1. **Population/agent density** (8/10): rho is a population density "
        "with density-dependent dispersal, carrying capacity rho_max, and "
        "logistic-like penalty toward equilibrium rho_star.  This is the "
        "strongest single-domain interpretation.",
        "",
        "2. **Porous-medium flow with reaction** (6/10): rho is a fluid "
        "density in a porous medium with degenerate permeability and a "
        "linear sink/source term.  The PME is ED's closest PDE relative.",
        "",
        "3. **Reaction-diffusion** (6/10): rho is a chemical concentration "
        "with monostable kinetics.  The degenerate mobility is unusual but "
        "not unprecedented in biochemical models.",
        "",
        "4. **Statistical mechanics** (5/10): rho is a probability density "
        "evolving under a modified Fokker-Planck equation.  The key "
        "mismatch is that ED is NOT a Wasserstein gradient flow.",
        "",
        "## What ED is NOT",
        "",
        "- **NOT a wave equation** (PHYS-02): no spatial propagation.",
        "- **NOT a pattern-forming system** (PHYS-04): no Turing instability.",
        "- **NOT a gradient flow** (PHYS-07): dissipative but not variational.",
        "- **NOT quantum mechanics** (PHYS-05): classical, dissipative, "
        "no superposition principle.",
        "",
        "## Conclusion",
        "",
        "The ED PDE is a **degenerate parabolic reaction-diffusion equation "
        "with global feedback**.  Its natural physical domain is "
        "density-dependent transport with carrying capacity and relaxation "
        "— a mathematical framework that spans porous media, population "
        "dynamics, and coarse-grained statistical mechanics.",
    ])

    return "\n".join(lines)
