"""
edsim.roadmap.manuscript -- Manuscript outline for the ED-SIM-03 paper.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class Section:
    """One section of the manuscript outline.

    Attributes
    ----------
    number : str
        Section number (e.g. "1", "2.1").
    title : str
        Section title.
    content : str
        Summary of what this section covers.
    figures : tuple[str, ...]
        Expected figures.
    tables : tuple[str, ...]
        Expected tables.
    """

    number: str
    title: str
    content: str
    figures: tuple = ()
    tables: tuple = ()


@dataclass
class ManuscriptOutline:
    """Structured outline for the ED-SIM-03 paper.

    Attributes
    ----------
    title : str
        Paper title.
    sections : list[Section]
        Ordered sections.
    """

    title: str = ""
    sections: list = field(default_factory=list)

    def to_markdown(self) -> str:
        """Format as a Markdown outline."""
        lines = [f"# {self.title}", ""]
        for s in self.sections:
            depth = s.number.count(".") + 2
            lines.append(f"{'#' * depth} {s.number}  {s.title}")
            lines.append("")
            lines.append(s.content)
            if s.figures:
                lines.append(f"  Figures: {', '.join(s.figures)}")
            if s.tables:
                lines.append(f"  Tables: {', '.join(s.tables)}")
            lines.append("")
        return "\n".join(lines)


def build_edsim3_manuscript_outline() -> ManuscriptOutline:
    """Produce the structured outline for the ED-SIM-03 paper.

    Returns
    -------
    ManuscriptOutline
    """
    return ManuscriptOutline(
        title="ED-SIM-03: A Multi-Scale Simulation Platform for Event Density",
        sections=[
            Section(
                number="1",
                title="Introduction",
                content=(
                    "Motivate the extension from ED-SIM-02 to ED-SIM-03.  "
                    "Summarise the nine architectural laws and their verification "
                    "in d=1-4.  State the goals: multi-field coupling, stochastic "
                    "forcing, GPU solvers, higher dimensions, experimental bridge."
                ),
            ),
            Section(
                number="2",
                title="Architecture",
                content=(
                    "Present the ED-SIM-03 component architecture.  Describe "
                    "each of the 10 components, their motivations, and their "
                    "inter-dependencies.  Show the dependency graph."
                ),
                figures=("Dependency graph (Mermaid or TikZ)",),
                tables=("Component summary table",),
            ),
            Section(
                number="3",
                title="Multi-Field ED",
                content=(
                    "Define the multi-field extension: coupled (rho_1, rho_2) "
                    "system with cross-mobility.  Derive the coupled Lyapunov "
                    "functional.  Present attractor existence results."
                ),
                figures=("Coupled field evolution", "Cross-mobility landscape"),
            ),
            Section(
                number="4",
                title="Stochastic ED",
                content=(
                    "Add multiplicative noise to the ED PDE.  Derive the modified "
                    "Lyapunov inequality.  Characterise the noise-sustained "
                    "steady state.  Identify which of the nine laws survive."
                ),
                figures=("Fluctuation spectrum", "Law survival table"),
            ),
            Section(
                number="5",
                title="Computational Extensions",
                content=(
                    "GPU-native solver benchmarks.  Spectral-FD IMEX integrator "
                    "validation.  Adaptive mesh refinement results.  5D/6D "
                    "dimensional law tests."
                ),
                figures=("GPU speedup plot", "AMR cost reduction", "d=5,6 complexity"),
                tables=("Benchmark table (CPU vs GPU vs AMR)",),
            ),
            Section(
                number="6",
                title="Higher-Dimensional Results",
                content=(
                    "Present the factorial law at d=5,6.  Verify R_grad predictions.  "
                    "Characterise 5D/6D morphology.  Test horizon suppression."
                ),
                figures=("Complexity vs d (1-6)", "R_grad vs d", "Morphology fractions vs d"),
            ),
            Section(
                number="7",
                title="Experimental Bridge",
                content=(
                    "Map ED predictions to thin-film experiments and galactic "
                    "rotation curves.  Present the prediction catalogue with "
                    "quantitative values and error bars."
                ),
                tables=("Prediction catalogue",),
            ),
            Section(
                number="8",
                title="Formal Proofs",
                content=(
                    "Present the Lean 4 proofs of Laws 2 and 5.  Summarise "
                    "the proof sketch for Law 1.  Discuss the formal specification "
                    "of the ED axiom system."
                ),
            ),
            Section(
                number="9",
                title="Discussion",
                content=(
                    "Assess the state of the ED programme.  What has been "
                    "established, what remains open.  Compare to the cross-framework "
                    "analysis of ED-Phys-38.  Discuss the experimental falsifiability "
                    "of ED predictions."
                ),
            ),
            Section(
                number="10",
                title="Future Work",
                content=(
                    "Identify the open questions that ED-SIM-04 would address: "
                    "full coarse-graining derivation, quantum-classical bridge, "
                    "cosmological-scale validation, and formal proof completion."
                ),
            ),
        ],
    )
