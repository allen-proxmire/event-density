"""
edsim.comparison.report -- Auto-generated cross-framework comparison report.

Assembles the comparison matrix, overlap/divergence analysis, and
uniqueness extraction into a single Markdown document.
"""

from __future__ import annotations

from pathlib import Path

from .frameworks import load_frameworks
from .matrix import build_comparison_matrix
from .analysis import run_analysis, AnalysisResult


def _section(title: str, level: int = 2) -> str:
    return f"\n{'#' * level} {title}\n"


def _framework_profiles(frameworks) -> str:
    """Generate framework profile summaries."""
    lines = [_section("Framework Profiles", 2)]
    for fw in frameworks:
        lines.append(f"### {fw.full_name}")
        lines.append("")
        lines.append(f"**Ontology:** {'; '.join(fw.ontology[:2])}")
        lines.append(f"**Primitives:** {'; '.join(fw.primitives[:3])}")
        lines.append(f"**Dynamics:** {'; '.join(fw.dynamics[:2])}")
        lines.append(f"**Invariants:** {'; '.join(fw.invariants[:3])}")
        lines.append(f"**Epistemology:** {'; '.join(fw.epistemology[:3])}")
        if fw.notes:
            lines.append(f"**Notes:** {fw.notes}")
        lines.append("")
    return "\n".join(lines)


def _matrix_section(matrix) -> str:
    """Generate the comparison matrix section."""
    lines = [
        _section("Comparison Matrix", 2),
        "Overlap scores: 0 = none, 1 = weak, 2 = moderate, 3 = strong.",
        "",
        matrix.to_table(),
        "",
    ]
    return "\n".join(lines)


def _detail_section(matrix) -> str:
    """Generate detailed cell-by-cell notes."""
    lines = [_section("Detailed Comparison", 2)]
    current_fw = None
    for (fw, axis), entry in sorted(matrix.entries.items()):
        if fw != current_fw:
            lines.append(f"### {fw}")
            lines.append("")
            current_fw = fw
        lines.append(
            f"**{axis}** (score {entry.score}): {entry.note}"
        )
        lines.append("")
    return "\n".join(lines)


def _overlap_section(result: AnalysisResult) -> str:
    """Generate the overlap section."""
    lines = [
        _section("Structural Overlaps (score >= 2)", 2),
    ]
    if not result.overlaps:
        lines.append("No strong overlaps found.")
    for o in result.overlaps:
        lines.append(
            f"- **{o.framework} / {o.axis}** (score {o.score}): {o.description}"
        )
    lines.append("")
    return "\n".join(lines)


def _divergence_section(result: AnalysisResult) -> str:
    """Generate the divergence section."""
    lines = [
        _section("Structural Divergences (score <= 1)", 2),
    ]
    for d in result.divergences[:10]:  # limit to top 10
        lines.append(f"- **{d.framework} / {d.axis}:** {d.description}")
    lines.append("")
    return "\n".join(lines)


def _uniqueness_section(result: AnalysisResult) -> str:
    """Generate the ED uniqueness section."""
    lines = [
        _section("Features Unique to ED", 2),
        "The following features are present in ED and absent from all "
        "comparison frameworks:",
        "",
    ]
    for i, u in enumerate(result.unique_features, 1):
        law_ref = f" (Law {u.law_number})" if u.law_number > 0 else ""
        lines.append(f"**{i}. {u.name}{law_ref}**")
        lines.append(f"  {u.description}")
        lines.append("")
    return "\n".join(lines)


def _proximity_section(result: AnalysisResult) -> str:
    """Generate the proximity ranking section."""
    lines = [
        _section("Proximity Ranking", 2),
        "Frameworks ranked by total overlap score with ED:",
        "",
        "| Rank | Framework | Total score |",
        "|------|-----------|-------------|",
    ]
    for rank, (fw, score) in enumerate(result.proximity_ranking, 1):
        lines.append(f"| {rank} | {fw} | {score} |")
    lines.append("")
    return "\n".join(lines)


def build_cross_framework_report(
    output_path: str = "manuscript/ED-SIM-02-Comparison.md",
) -> str:
    """Build the complete cross-framework comparison report.

    Parameters
    ----------
    output_path : str
        Path to write the report.

    Returns
    -------
    str
        Path to the written file.
    """
    frameworks = load_frameworks()
    matrix = build_comparison_matrix(frameworks)
    result = run_analysis(matrix)

    sections = [
        "# Cross-Framework Comparison: Event Density",
        "",
        "This report compares the Event Density (ED) framework to six "
        "established theoretical frameworks along five structural axes: "
        "ontology, primitives, dynamics, invariants, and epistemology.",
        "",
        "All comparisons are structural, not rhetorical.  No claims of "
        "equivalence or superiority are made.",
        "",
        _framework_profiles(frameworks),
        _matrix_section(matrix),
        _detail_section(matrix),
        _overlap_section(result),
        _divergence_section(result),
        _uniqueness_section(result),
        _proximity_section(result),
        _section("Summary", 2),
        "**Closest framework:** Statistical Mechanics (Fokker-Planck).  "
        "Shared gradient-flow structure, entropy non-decrease, and "
        "correlation functions.  Key difference: ED has degenerate "
        "mobility and participation coupling.",
        "",
        "**Most distant:** Constructor Theory and Causal Sets.  "
        "Fundamentally different mathematical objects (tasks vs PDE, "
        "discrete vs continuous).",
        "",
        "**Irreducible ED core:** Seven features not shared by any "
        "comparison framework define ED as a distinct mathematical "
        "architecture.",
    ]

    content = "\n".join(sections)

    out = Path(output_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(content, encoding="utf-8")

    return str(out)
