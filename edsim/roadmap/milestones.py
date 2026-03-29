"""
edsim.roadmap.milestones -- Milestone plan for ED-SIM-03 development.

Organises the dependency graph into five phases with explicit
tasks, outputs, and acceptance criteria.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from .dependencies import DependencyGraph


@dataclass(frozen=True)
class Task:
    """One task within a milestone.

    Attributes
    ----------
    id : str
        Task identifier.
    title : str
        Descriptive title.
    component : str
        Component or question ID this task belongs to.
    outputs : tuple[str, ...]
        Deliverables.
    acceptance : str
        Criterion for marking the task complete.
    """

    id: str
    title: str
    component: str
    outputs: tuple = ()
    acceptance: str = ""


@dataclass(frozen=True)
class Milestone:
    """A development phase containing multiple tasks.

    Attributes
    ----------
    phase : str
        Phase identifier (e.g. "A", "B").
    title : str
        Phase title.
    description : str
        What this phase accomplishes.
    tasks : tuple[Task, ...]
        Ordered tasks within the phase.
    """

    phase: str
    title: str
    description: str
    tasks: tuple = ()


@dataclass
class MilestonePlan:
    """Complete milestone plan for ED-SIM-03.

    Attributes
    ----------
    milestones : list[Milestone]
        Ordered phases.
    """

    milestones: list = field(default_factory=list)

    def to_table(self) -> str:
        """Format as a Markdown table."""
        lines = [
            "| Phase | Title | Tasks | Key outputs |",
            "|-------|-------|-------|-------------|",
        ]
        for m in self.milestones:
            n = len(m.tasks)
            outputs = "; ".join(t.outputs[0] for t in m.tasks if t.outputs)[:80]
            lines.append(f"| {m.phase} | {m.title} | {n} | {outputs} |")
        return "\n".join(lines)

    def to_detailed_markdown(self) -> str:
        """Format as a detailed Markdown document."""
        lines = []
        for m in self.milestones:
            lines.append(f"### Phase {m.phase}: {m.title}")
            lines.append("")
            lines.append(m.description)
            lines.append("")
            for t in m.tasks:
                outputs = ", ".join(t.outputs) if t.outputs else "(none)"
                lines.append(f"- **{t.id}: {t.title}** ({t.component})")
                lines.append(f"  Outputs: {outputs}")
                lines.append(f"  Acceptance: {t.acceptance}")
            lines.append("")
        return "\n".join(lines)


def build_milestone_plan(graph: DependencyGraph) -> MilestonePlan:
    """Produce a phased milestone plan from the dependency graph.

    Parameters
    ----------
    graph : DependencyGraph

    Returns
    -------
    MilestonePlan
        Five phases: A (Foundations), B (Engineering), C (Physics),
        D (Mathematics), E (Documentation + Manuscript).
    """
    milestones = [
        Milestone(
            phase="A",
            title="Foundations",
            description=(
                "Establish the core infrastructure for ED-SIM-03: "
                "GPU backend, spectral-FD hybrid integrator, and "
                "multi-field coupling framework."
            ),
            tasks=(
                Task(
                    id="A1",
                    title="GPU-native solver backend (JAX/CuPy)",
                    component="gpu_solver",
                    outputs=("JAX solver backend", "CPU vs GPU benchmark"),
                    acceptance="3D simulation at N=64 runs on GPU with <5% invariant error",
                ),
                Task(
                    id="A2",
                    title="Spectral-FD IMEX integrator for d=1..4",
                    component="spectral_fd_hybrid",
                    outputs=("IMEX-RK4 integrator", "Stability analysis"),
                    acceptance="ETD-RK4 accuracy in d=2,3,4 with IMEX framework",
                ),
                Task(
                    id="A3",
                    title="Multi-field coupling framework",
                    component="multi_field",
                    outputs=("Multi-field solver", "Cross-mobility library"),
                    acceptance="2-field simulation converges to coupled attractor",
                ),
                Task(
                    id="A4",
                    title="Stochastic forcing module",
                    component="stochastic",
                    outputs=("Euler-Maruyama integrator", "Noise-aware atlas"),
                    acceptance="Stochastic simulation matches expected fluctuation spectrum",
                ),
            ),
        ),
        Milestone(
            phase="B",
            title="Engineering",
            description=(
                "Scale the platform: adaptive grids, higher dimensions, "
                "and real-time visualisation."
            ),
            tasks=(
                Task(
                    id="B1",
                    title="Adaptive mesh refinement (AMR)",
                    component="adaptive_grid",
                    outputs=("AMR data structure", "Refinement criteria"),
                    acceptance="4D simulation with AMR achieves 10x cost reduction at 1% error",
                ),
                Task(
                    id="B2",
                    title="5D/6D solver and invariant atlas",
                    component="high_dim",
                    outputs=("5D solver", "6D solver", "Dimensional law verification"),
                    acceptance="Factorial law verified at d=5,6 within 10%",
                ),
                Task(
                    id="B3",
                    title="Real-time 3D visualisation",
                    component="realtime_viz",
                    outputs=("Interactive 3D viewer", "Live dashboard"),
                    acceptance="3D field at N=64 rendered at >10 fps",
                ),
                Task(
                    id="B4",
                    title="Interactive parameter explorer notebooks",
                    component="interactive_nb",
                    outputs=("Parameter explorer", "Regime navigator"),
                    acceptance="Notebooks run without errors in JupyterLab",
                ),
            ),
        ),
        Milestone(
            phase="C",
            title="Physics",
            description=(
                "Address the core physics questions: multi-field attractor, "
                "stochastic steady states, and experimental bridge."
            ),
            tasks=(
                Task(
                    id="C1",
                    title="Multi-field attractor analysis",
                    component="multi_field",
                    outputs=("Attractor existence proof/evidence", "Coupled invariant atlas"),
                    acceptance="2-field system converges for 10+ parameter sets",
                ),
                Task(
                    id="C2",
                    title="Stochastic steady-state characterisation",
                    component="stochastic",
                    outputs=("Steady-state distribution", "Fluctuation spectrum"),
                    acceptance="Non-trivial steady state identified and characterised",
                ),
                Task(
                    id="C3",
                    title="Experimental bridge: thin-film predictions",
                    component="experimental_bridge",
                    outputs=("Prediction catalogue", "Experimental design document"),
                    acceptance="3 falsifiable predictions with quantitative values",
                ),
                Task(
                    id="C4",
                    title="Horizon threshold physical mapping",
                    component="experimental_bridge",
                    outputs=("A_crit physical analogue table",),
                    acceptance="A_crit mapped to at least 2 physical thresholds",
                ),
            ),
        ),
        Milestone(
            phase="D",
            title="Mathematics",
            description=(
                "Formal proofs, rigorous derivations, and mathematical "
                "extensions of the architectural laws."
            ),
            tasks=(
                Task(
                    id="D1",
                    title="Formal proof of Law 2 (energy monotonicity)",
                    component="formal_proofs",
                    outputs=("Lean 4 proof file",),
                    acceptance="Proof compiles without errors in Lean 4",
                ),
                Task(
                    id="D2",
                    title="Formal proof of Law 5 (gradient dominance)",
                    component="formal_proofs",
                    outputs=("Lean 4 proof file",),
                    acceptance="Proof compiles without errors in Lean 4",
                ),
                Task(
                    id="D3",
                    title="Attractor uniqueness proof sketch",
                    component="formal_proofs",
                    outputs=("Proof sketch document",),
                    acceptance="Sketch identifies all gaps and required lemmas",
                ),
                Task(
                    id="D4",
                    title="Factorial law rigorous derivation",
                    component="formal_proofs",
                    outputs=("Derivation with explicit error bounds",),
                    acceptance="Error bounds consistent with d=5,6 numerics",
                ),
            ),
        ),
        Milestone(
            phase="E",
            title="Documentation and Manuscript",
            description=(
                "Write the ED-SIM-03 paper, update documentation, "
                "and produce the reproducibility certificate."
            ),
            tasks=(
                Task(
                    id="E1",
                    title="ED-SIM-03 paper: architecture + results",
                    component="interactive_nb",
                    outputs=("Manuscript draft",),
                    acceptance="Complete draft with all figures and tables",
                ),
                Task(
                    id="E2",
                    title="Updated documentation for all new modules",
                    component="interactive_nb",
                    outputs=("docs/ updates",),
                    acceptance="All new modules documented with examples",
                ),
                Task(
                    id="E3",
                    title="Extended reproducibility pipeline (v3)",
                    component="interactive_nb",
                    outputs=("run_all_v3.py", "Certificate v3"),
                    acceptance="All phases pass on CI with GPU and CPU",
                ),
                Task(
                    id="E4",
                    title="Release engineering (v0.2.0)",
                    component="interactive_nb",
                    outputs=("pyproject.toml v0.2.0", "CHANGELOG update"),
                    acceptance="pip install succeeds; CLI runs all new commands",
                ),
            ),
        ),
    ]

    return MilestonePlan(milestones=milestones)
