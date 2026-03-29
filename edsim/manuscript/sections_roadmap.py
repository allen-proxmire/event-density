"""
edsim.manuscript.sections_roadmap -- Manuscript section for the ED-SIM-03 roadmap.

Generates a publication-ready future-work section summarising the
ED-SIM-03 architecture, research questions, and milestone plan.
"""

from __future__ import annotations

from ..roadmap.architecture import build_edsim3_architecture
from ..roadmap.questions import list_research_questions, questions_by_theme
from ..roadmap.dependencies import build_dependency_graph
from ..roadmap.milestones import build_milestone_plan
from ..roadmap.manuscript import build_edsim3_manuscript_outline


def section_roadmap() -> str:
    """Return a manuscript-ready section on the ED-SIM-03 roadmap.

    Returns
    -------
    str
        Markdown text for the future-work / roadmap section.
    """
    arch = build_edsim3_architecture()
    questions = list_research_questions()
    graph = build_dependency_graph(arch, questions)
    plan = build_milestone_plan(graph)

    by_theme = questions_by_theme()
    n_physics = len(by_theme.get("Physics", []))
    n_math = len(by_theme.get("Mathematics", []))
    n_comp = len(by_theme.get("Computation", []))
    n_arch = len(by_theme.get("Architecture", []))
    n_interp = len(by_theme.get("Interpretation", []))

    lines = [
        "## Future Work: ED-SIM-03",
        "",
        "The next-generation platform extends ED-SIM-02 along five axes.",
        "",
        "### Architecture",
        "",
        f"ED-SIM-03 comprises {len(arch.components)} components:",
        "",
    ]

    for c in arch.components:
        lines.append(f"- **{c.title}**: {c.description[:100]}...")

    lines.extend([
        "",
        "### Research Questions",
        "",
        f"We identify {len(questions)} open questions across five themes: "
        f"physics ({n_physics}), mathematics ({n_math}), "
        f"computation ({n_comp}), architecture ({n_arch}), "
        f"and interpretation ({n_interp}).",
        "",
        "The highest-priority questions are:",
        "",
    ])

    # Top 5 by difficulty
    hard = [q for q in questions if q.difficulty in ("high", "very_high")]
    for q in hard[:5]:
        lines.append(f"- **{q.id}** [{q.difficulty}]: {q.question}")

    lines.extend([
        "",
        "### Development Plan",
        "",
        f"The {len(plan.milestones)}-phase milestone plan organises "
        "work into foundations, engineering, physics, mathematics, "
        "and documentation:",
        "",
        plan.to_table(),
        "",
        "### Dependency Structure",
        "",
        f"The dependency graph contains {len(graph.nodes)} nodes and "
        f"{len(graph.edges)} prerequisite edges.  "
        f"{len(graph.roots())} root nodes (no prerequisites) can begin "
        "immediately.",
        "",
        "### Expected Outcomes",
        "",
        "ED-SIM-03 will deliver:",
        "",
        "1. Multi-field and stochastic ED solvers",
        "2. GPU-native performance for 3D/4D",
        "3. Dimensional law verification at d=5,6",
        "4. Formal proofs of Laws 2 and 5",
        "5. An experimental bridge to thin-film and astrophysical measurements",
        "6. A publication-ready manuscript",
    ])

    return "\n".join(lines)
