"""
edsim.manuscript.sections_comparison -- Manuscript section for cross-framework comparison.

Generates a publication-ready manuscript section summarising the
cross-framework analysis.  Intended to be called by the manuscript
build pipeline.
"""

from __future__ import annotations

from ..comparison.frameworks import load_frameworks
from ..comparison.matrix import build_comparison_matrix
from ..comparison.analysis import run_analysis


def section_comparison() -> str:
    """Return a manuscript-ready section on cross-framework comparison.

    Returns
    -------
    str
        Markdown text for the comparison section.
    """
    frameworks = load_frameworks()
    matrix = build_comparison_matrix(frameworks)
    result = run_analysis(matrix)

    lines = [
        "## Cross-Framework Comparison",
        "",
        "We compare the ED architecture to six established theoretical "
        "frameworks along five structural axes: ontology, primitives, "
        "dynamics, invariants, and epistemology.  All comparisons are "
        "structural; no claims of equivalence are made.",
        "",
        "### Comparison Matrix",
        "",
        matrix.to_table(),
        "",
        "### Proximity Ranking",
        "",
        "Ranked by total structural overlap with ED:",
        "",
    ]

    for rank, (fw, score) in enumerate(result.proximity_ranking, 1):
        fw_obj = next((f for f in frameworks if f.name == fw), None)
        label = fw_obj.full_name if fw_obj else fw
        lines.append(f"{rank}. **{label}** (score {score}/15)")

    lines.extend([
        "",
        "Statistical mechanics (specifically the Fokker-Planck equation) "
        "is the closest structural relative of ED.  Both share the "
        "gradient-flow architecture, entropy non-decrease, and "
        "correlation-function epistemology.  The key differences are "
        "ED's degenerate mobility (producing horizons), the penalty-driven "
        "unique attractor, and the participation coupling.",
        "",
        "### Key Overlaps",
        "",
    ])

    # Top overlaps
    for o in result.overlaps[:5]:
        fw_obj = next((f for f in frameworks if f.name == o.framework), None)
        label = fw_obj.full_name if fw_obj else o.framework
        lines.append(
            f"- **{label} / {o.axis}** (score {o.score}): "
            f"{o.description[:120]}"
        )

    lines.extend([
        "",
        "### Features Unique to ED",
        "",
        "Seven architectural features distinguish ED from all comparison "
        "frameworks:",
        "",
    ])

    for i, u in enumerate(result.unique_features, 1):
        law_ref = f" (Law {u.law_number})" if u.law_number > 0 else ""
        lines.append(f"{i}. **{u.name}**{law_ref}")

    lines.extend([
        "",
        "These features define the irreducible core of the ED architecture: "
        "the minimum set of properties that cannot be reproduced by any "
        "simpler or more established theoretical framework.",
        "",
        "### Interpretation",
        "",
        "ED is not a replacement for any of the comparison frameworks.  "
        "It is a distinct mathematical architecture that shares structural "
        "features with several of them.  The comparison matrix quantifies "
        "these overlaps and divergences, providing a precise answer to the "
        "question: where does ED sit in the landscape of theoretical physics?",
        "",
        "The answer is: closest to statistical mechanics (gradient-flow "
        "dynamics), with moderate overlap with hydrodynamics (continuous "
        "field PDE) and entropic gravity (entropy-driven dynamics), and "
        "minimal overlap with causal sets, constructor theory, and quantum "
        "foundations.",
    ])

    return "\n".join(lines)
