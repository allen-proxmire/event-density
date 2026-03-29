"""
edsim.math.architecture -- Architectural axiom system and PDE derivation.

Provides a symbolic scaffolding for the architectural proof:

    P1-P7 (axioms) => canonical ED PDE

Each axiom is an explicit mathematical statement.  The derivation tree
shows which axioms are used at each step.  This is a *scaffolding*,
not a formal proof system; it organises the logical dependencies and
records the mathematical content of each axiom in a machine-readable
form.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional


@dataclass(frozen=True)
class Axiom:
    """A single axiom in the ED architectural system.

    Attributes
    ----------
    name : str
        Short identifier (e.g. "P1").
    title : str
        Descriptive title.
    statement : str
        Precise mathematical statement.
    consequence : str
        What this axiom implies for the PDE.
    mathematical_form : str
        LaTeX-formatted mathematical content.
    """

    name: str
    title: str
    statement: str
    consequence: str
    mathematical_form: str


@dataclass(frozen=True)
class DerivationStep:
    """One step in the PDE derivation from axioms.

    Attributes
    ----------
    step : int
        Step number.
    description : str
        What is established at this step.
    uses_axioms : tuple[str, ...]
        Which axioms are invoked.
    mathematical_form : str
        LaTeX of the result.
    """

    step: int
    description: str
    uses_axioms: tuple
    mathematical_form: str


@dataclass
class CanonicalPDE:
    """Symbolic representation of the canonical ED PDE.

    The PDE:
        partial_t rho = D [M(rho) nabla^2 rho + M'(rho) |nabla rho|^2 - P(rho)] + H v

    This class stores the symbolic structure (not a solver).
    """

    operator_form: str = (
        "F[rho] = M(rho) nabla^2 rho + M'(rho) |nabla rho|^2 - P(rho)"
    )
    participation_form: str = (
        "dot{v} = (1/tau)(bar{F} - zeta v)"
    )
    full_form: str = (
        "partial_t rho = D F[rho] + H v"
    )
    mobility: str = "M(rho) = M_0 (rho_max - rho)^beta"
    penalty: str = "P(rho) = P_0 (rho - rho*)"
    lyapunov: str = "E[rho] = int Phi(rho) dV, Phi = int_{rho*}^{rho} P(s)/M(s) ds"

    def latex(self) -> str:
        """Return the full PDE system in LaTeX."""
        return (
            "\\begin{align}\n"
            "\\partial_t \\rho &= D\\,F[\\rho] + H\\,v, \\\\\n"
            "\\dot{v} &= \\frac{1}{\\tau}(\\bar{F} - \\zeta\\,v), \\\\\n"
            "F[\\rho] &= M(\\rho)\\,\\nabla^2\\rho "
            "+ M'(\\rho)\\,|\\nabla\\rho|^2 - P(\\rho), \\\\\n"
            "M(\\rho) &= M_0\\,(\\rho_{\\max} - \\rho)^\\beta, \\\\\n"
            "P(\\rho) &= P_0\\,(\\rho - \\rho^*).\n"
            "\\end{align}"
        )


class ArchitecturalAxioms:
    """The seven axioms of the ED architectural system.

    P1: Locality
    P2: Isotropy
    P3: Gradient-driven flow
    P4: Dissipative structure
    P5: Single scalar field
    P6: Minimal coupling
    P7: Dimensional consistency
    """

    P1 = Axiom(
        name="P1",
        title="Locality",
        statement=(
            "The evolution of rho at each point depends only on rho and "
            "its spatial derivatives evaluated at that point."
        ),
        consequence=(
            "The operator F[rho] is a local differential operator.  "
            "No integral terms, no action at a distance."
        ),
        mathematical_form=(
            "F[\\rho](x) = f(\\rho(x), \\nabla\\rho(x), \\nabla^2\\rho(x))"
        ),
    )

    P2 = Axiom(
        name="P2",
        title="Isotropy",
        statement=(
            "The evolution law has no preferred spatial direction.  "
            "F[rho] is invariant under rotations and reflections."
        ),
        consequence=(
            "F depends on rho, |nabla rho|^2, and nabla^2 rho, but not "
            "on individual partial derivatives.  No anisotropic terms."
        ),
        mathematical_form=(
            "F[\\rho \\circ R] = F[\\rho] \\circ R "
            "\\quad \\forall R \\in O(d)"
        ),
    )

    P3 = Axiom(
        name="P3",
        title="Gradient-driven flow",
        statement=(
            "The flux of rho is proportional to nabla rho, modulated "
            "by a state-dependent mobility M(rho) >= 0."
        ),
        consequence=(
            "The principal part of F is nabla . (M(rho) nabla rho), "
            "which expands to M nabla^2 rho + M' |nabla rho|^2."
        ),
        mathematical_form=(
            "J = -M(\\rho)\\,\\nabla\\rho, \\quad "
            "\\nabla\\!\\cdot\\!J = M\\,\\nabla^2\\rho + M'\\,|\\nabla\\rho|^2"
        ),
    )

    P4 = Axiom(
        name="P4",
        title="Dissipative structure",
        statement=(
            "There exists a Lyapunov functional E[rho] such that "
            "dE/dt <= 0 along all solutions."
        ),
        consequence=(
            "The penalty P(rho) and mobility M(rho) are related via "
            "the density potential Phi(rho) = int P/M ds.  "
            "The system is gradient-flow-like."
        ),
        mathematical_form=(
            "\\frac{dE}{dt} = -\\int \\frac{|\\nabla\\rho|^2}{M(\\rho)} "
            "- \\int \\frac{P(\\rho)^2}{M(\\rho)} \\leq 0"
        ),
    )

    P5 = Axiom(
        name="P5",
        title="Single scalar field",
        statement=(
            "The system evolves a single real-valued scalar field "
            "rho(x, t) on a bounded domain Omega."
        ),
        consequence=(
            "No vector fields, no tensor fields, no multi-component "
            "order parameters.  The PDE is scalar, not a system."
        ),
        mathematical_form=(
            "\\rho: \\Omega \\times [0, T] \\to [0, \\rho_{\\max}]"
        ),
    )

    P6 = Axiom(
        name="P6",
        title="Minimal coupling",
        statement=(
            "The global mode v(t) is driven by the domain-averaged "
            "operator F_bar and feeds back additively into the local PDE."
        ),
        consequence=(
            "The (rho, v) system is the minimal non-local extension "
            "of the local PDE.  The coupling is linear in v."
        ),
        mathematical_form=(
            "\\dot{v} = \\tau^{-1}(\\bar{F} - \\zeta v), \\quad "
            "\\partial_t\\rho \\ni +H\\,v"
        ),
    )

    P7 = Axiom(
        name="P7",
        title="Dimensional consistency",
        statement=(
            "The PDE is well-posed and dimensionally consistent in "
            "all spatial dimensions d = 1, 2, 3, 4.  No d-dependent "
            "constitutive functions are introduced."
        ),
        consequence=(
            "The same M(rho), P(rho), and participation structure "
            "apply in all dimensions.  Dimensional effects enter "
            "only through the Laplacian eigenstructure and mode counting."
        ),
        mathematical_form=(
            "M, P, H, \\tau, \\zeta \\text{ are independent of } d"
        ),
    )

    @classmethod
    def all_axioms(cls) -> list[Axiom]:
        """Return all seven axioms as a list."""
        return [cls.P1, cls.P2, cls.P3, cls.P4, cls.P5, cls.P6, cls.P7]


def derive_canonical_pde() -> list[DerivationStep]:
    """Return the derivation tree showing how P1-P7 imply the canonical PDE.

    Returns
    -------
    list[DerivationStep]
        Ordered derivation steps.
    """
    return [
        DerivationStep(
            step=1,
            description=(
                "By P5, the state is a single scalar rho(x,t) on Omega."
            ),
            uses_axioms=("P5",),
            mathematical_form=(
                "\\rho: \\Omega \\times [0,T] \\to [0, \\rho_{\\max}]"
            ),
        ),
        DerivationStep(
            step=2,
            description=(
                "By P1, the local operator F depends only on rho "
                "and its derivatives at each point."
            ),
            uses_axioms=("P1",),
            mathematical_form=(
                "F[\\rho](x) = f(\\rho, \\nabla\\rho, \\nabla^2\\rho)"
            ),
        ),
        DerivationStep(
            step=3,
            description=(
                "By P2, F is isotropic: it depends on |nabla rho|^2 "
                "and nabla^2 rho, not on individual partials."
            ),
            uses_axioms=("P2",),
            mathematical_form=(
                "F = f(\\rho, |\\nabla\\rho|^2, \\nabla^2\\rho)"
            ),
        ),
        DerivationStep(
            step=4,
            description=(
                "By P3, the flux is J = -M(rho) nabla rho, giving "
                "the divergence-form principal part."
            ),
            uses_axioms=("P3",),
            mathematical_form=(
                "\\nabla\\!\\cdot\\!(M\\nabla\\rho) = "
                "M\\nabla^2\\rho + M'|\\nabla\\rho|^2"
            ),
        ),
        DerivationStep(
            step=5,
            description=(
                "By P4, the system must be dissipative.  The simplest "
                "zeroth-order term compatible with a Lyapunov functional "
                "is a linear penalty P(rho) = P0(rho - rho*)."
            ),
            uses_axioms=("P4",),
            mathematical_form=(
                "F = M\\nabla^2\\rho + M'|\\nabla\\rho|^2 - P(\\rho)"
            ),
        ),
        DerivationStep(
            step=6,
            description=(
                "By P6, the global mode v(t) couples additively, "
                "giving the full PDE and the v-equation."
            ),
            uses_axioms=("P6",),
            mathematical_form=(
                "\\partial_t\\rho = D\\,F[\\rho] + H\\,v, \\quad "
                "\\dot{v} = \\tau^{-1}(\\bar{F} - \\zeta v)"
            ),
        ),
        DerivationStep(
            step=7,
            description=(
                "By P7, the constitutive functions M, P are "
                "dimension-independent.  The PDE is valid for all "
                "d = 1, 2, 3, 4."
            ),
            uses_axioms=("P7",),
            mathematical_form=(
                "M(\\rho) = M_0(\\rho_{\\max}-\\rho)^\\beta, \\quad "
                "P(\\rho) = P_0(\\rho - \\rho^*) \\quad \\forall d"
            ),
        ),
    ]


def derivation_to_markdown() -> str:
    """Format the PDE derivation as a Markdown section."""
    pde = CanonicalPDE()
    steps = derive_canonical_pde()
    axioms = ArchitecturalAxioms.all_axioms()

    lines = [
        "## Architectural Derivation: P1-P7 => Canonical PDE",
        "",
        "### Axioms",
        "",
    ]
    for a in axioms:
        lines.append(f"**{a.name} ({a.title}):** {a.statement}")
        lines.append(f"  - Consequence: {a.consequence}")
        lines.append(f"  - Form: ${a.mathematical_form}$")
        lines.append("")

    lines.append("### Derivation Steps")
    lines.append("")
    for s in steps:
        ax = ", ".join(s.uses_axioms)
        lines.append(f"**Step {s.step}** (uses {ax}): {s.description}")
        lines.append(f"  ${s.mathematical_form}$")
        lines.append("")

    lines.append("### Result")
    lines.append("")
    lines.append(f"$$\n{pde.latex()}\n$$")

    return "\n".join(lines)
