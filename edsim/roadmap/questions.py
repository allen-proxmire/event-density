"""
edsim.roadmap.questions -- Research questions for ED-SIM-03 and beyond.

Organises open questions into five themes: physics, mathematics,
computation, architecture, and interpretation.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class Theme(Enum):
    PHYSICS = "Physics"
    MATHEMATICS = "Mathematics"
    COMPUTATION = "Computation"
    ARCHITECTURE = "Architecture"
    INTERPRETATION = "Interpretation"


@dataclass(frozen=True)
class ResearchQuestion:
    """An open research question for the ED programme.

    Attributes
    ----------
    id : str
        Short identifier (e.g. "P1", "M3").
    theme : Theme
        Research theme.
    question : str
        The question, stated precisely.
    rationale : str
        Why this question matters.
    difficulty : str
        "low", "medium", "high", or "very_high".
    dependencies : tuple[str, ...]
        Component names or question IDs that must be addressed first.
    """

    id: str
    theme: Theme
    question: str
    rationale: str
    difficulty: str = "medium"
    dependencies: tuple = ()


def list_research_questions() -> list[ResearchQuestion]:
    """Return all open research questions grouped by theme.

    Returns
    -------
    list[ResearchQuestion]
    """
    return [
        # ── Physics ──────────────────────────────────────────────
        ResearchQuestion(
            id="P1",
            theme=Theme.PHYSICS,
            question=(
                "Can the ED PDE be derived as an effective equation "
                "from a microscopic Hamiltonian via coarse-graining?"
            ),
            rationale=(
                "This would establish ED as a hydrodynamic limit of a "
                "deeper theory, analogous to Navier-Stokes from Boltzmann."
            ),
            difficulty="very_high",
            dependencies=(),
        ),
        ResearchQuestion(
            id="P2",
            theme=Theme.PHYSICS,
            question=(
                "What happens when two ED fields are coupled with "
                "cross-mobility terms?  Does the attractor survive?"
            ),
            rationale=(
                "Multi-field ED could model matter-radiation or "
                "dark-matter-baryon interactions."
            ),
            difficulty="high",
            dependencies=("multi_field",),
        ),
        ResearchQuestion(
            id="P3",
            theme=Theme.PHYSICS,
            question=(
                "Does stochastic forcing produce a non-trivial steady "
                "state that is distinct from rho*?"
            ),
            rationale=(
                "Noise-sustained structure would give ED a fluctuation "
                "theory analogous to thermal equilibrium."
            ),
            difficulty="medium",
            dependencies=("stochastic",),
        ),
        ResearchQuestion(
            id="P4",
            theme=Theme.PHYSICS,
            question=(
                "Can ED reproduce the Tully-Fisher or baryonic "
                "Tully-Fisher relation in a galactic-scale simulation?"
            ),
            rationale=(
                "A quantitative match to galaxy rotation curves would "
                "be a strong falsifiable prediction."
            ),
            difficulty="very_high",
            dependencies=("multi_field", "experimental_bridge"),
        ),
        ResearchQuestion(
            id="P5",
            theme=Theme.PHYSICS,
            question=(
                "Does the horizon formation threshold A_crit have a "
                "physical analogue (e.g., Chandrasekhar limit, "
                "Jeans mass)?"
            ),
            rationale=(
                "Mapping A_crit to a physical threshold would anchor "
                "the horizon concept to measurable physics."
            ),
            difficulty="high",
            dependencies=("experimental_bridge",),
        ),

        # ── Mathematics ──────────────────────────────────────────
        ResearchQuestion(
            id="M1",
            theme=Theme.MATHEMATICS,
            question=(
                "Is the attractor rho* globally unique for all initial "
                "conditions in [0, rho_max], including non-smooth data?"
            ),
            rationale=(
                "Law 1 is only partially derived.  A full proof would "
                "be a major mathematical result."
            ),
            difficulty="very_high",
            dependencies=("formal_proofs",),
        ),
        ResearchQuestion(
            id="M2",
            theme=Theme.MATHEMATICS,
            question=(
                "Does the factorial complexity law C^(d) = C^(1)/d! "
                "hold exactly, or only asymptotically?"
            ),
            rationale=(
                "ED-Phys-36 provides a structural argument.  A rigorous "
                "derivation would clarify the O(1) corrections."
            ),
            difficulty="high",
            dependencies=("high_dim",),
        ),
        ResearchQuestion(
            id="M3",
            theme=Theme.MATHEMATICS,
            question=(
                "Can the topological conservation law d chi/dt = 0 be "
                "proved rigorously for the degenerate ED PDE?"
            ),
            rationale=(
                "The Morse-theoretic argument assumes non-degenerate "
                "critical points.  Degeneracy near rho_max may break it."
            ),
            difficulty="high",
            dependencies=("formal_proofs",),
        ),
        ResearchQuestion(
            id="M4",
            theme=Theme.MATHEMATICS,
            question=(
                "What is the basin of attraction for the sheet-filament "
                "oscillation?  Is it generic or fine-tuned?"
            ),
            rationale=(
                "Law 9 is empirical.  Understanding its basin would "
                "determine whether it is an architectural law or a "
                "parameter-dependent phenomenon."
            ),
            difficulty="medium",
            dependencies=(),
        ),

        # ── Computation ──────────────────────────────────────────
        ResearchQuestion(
            id="C1",
            theme=Theme.COMPUTATION,
            question=(
                "Can a GPU-native JAX solver achieve 100x speedup "
                "for 3D simulations at N=128?"
            ),
            rationale=(
                "This would enable large-scale 3D parameter sweeps "
                "and real-time exploration."
            ),
            difficulty="medium",
            dependencies=("gpu_solver",),
        ),
        ResearchQuestion(
            id="C2",
            theme=Theme.COMPUTATION,
            question=(
                "Can AMR reduce 4D computation from O(N^4) to O(N^2 log N) "
                "while preserving invariant accuracy to 1%?"
            ),
            rationale=(
                "4D at N=64 is barely feasible.  AMR could push to N_eff=128."
            ),
            difficulty="high",
            dependencies=("adaptive_grid",),
        ),
        ResearchQuestion(
            id="C3",
            theme=Theme.COMPUTATION,
            question=(
                "Can a spectral-FD IMEX integrator be stable and accurate "
                "in d=4,5,6 with degenerate mobility?"
            ),
            rationale=(
                "ETD-RK4 is 2D-only.  A general IMEX would unify "
                "all dimensions under one integrator."
            ),
            difficulty="medium",
            dependencies=("spectral_fd_hybrid",),
        ),

        # ── Architecture ─────────────────────────────────────────
        ResearchQuestion(
            id="A1",
            theme=Theme.ARCHITECTURE,
            question=(
                "What is the minimal extension of the ED axiom system "
                "that admits multi-field coupling?"
            ),
            rationale=(
                "P5 (single scalar field) must be relaxed.  The question "
                "is what replaces it while preserving the Lyapunov structure."
            ),
            difficulty="high",
            dependencies=("multi_field",),
        ),
        ResearchQuestion(
            id="A2",
            theme=Theme.ARCHITECTURE,
            question=(
                "Can the nine laws be extended to stochastic ED?  "
                "Which laws survive, which break?"
            ),
            rationale=(
                "Noise will likely break Laws 2 (monotone energy) and 6 "
                "(topology).  Understanding which laws are robust determines "
                "the stochastic architectural skeleton."
            ),
            difficulty="medium",
            dependencies=("stochastic",),
        ),

        # ── Interpretation ───────────────────────────────────────
        ResearchQuestion(
            id="I1",
            theme=Theme.INTERPRETATION,
            question=(
                "Can ED be interpreted as a pilot-wave theory for a "
                "classical probability density?"
            ),
            rationale=(
                "The ED PDE resembles a nonlinear Schrodinger-like "
                "equation in the quantum-scale regime.  A pilot-wave "
                "interpretation would connect ED to de Broglie-Bohm theory."
            ),
            difficulty="high",
            dependencies=(),
        ),
        ResearchQuestion(
            id="I2",
            theme=Theme.INTERPRETATION,
            question=(
                "Is the ED participation variable v(t) interpretable "
                "as a gravitational potential or a cosmological expansion rate?"
            ),
            rationale=(
                "v is the only global mode.  Mapping it to a physical "
                "quantity would anchor the non-local coupling."
            ),
            difficulty="medium",
            dependencies=("experimental_bridge",),
        ),
        ResearchQuestion(
            id="I3",
            theme=Theme.INTERPRETATION,
            question=(
                "Can the ED morphological taxonomy (filament/sheet/blob) "
                "be mapped quantitatively to the cosmic web?"
            ),
            rationale=(
                "ED-Phys-37 identifies a structural analogy.  A quantitative "
                "match would be a strong validation."
            ),
            difficulty="very_high",
            dependencies=("multi_field", "experimental_bridge"),
        ),
    ]


def questions_by_theme() -> dict[str, list[ResearchQuestion]]:
    """Group questions by theme."""
    qs = list_research_questions()
    grouped: dict[str, list[ResearchQuestion]] = {}
    for q in qs:
        key = q.theme.value
        grouped.setdefault(key, []).append(q)
    return grouped
