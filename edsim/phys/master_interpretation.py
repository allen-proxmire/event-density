"""
edsim.phys.master_interpretation — Master interpretation and synthesis.

Integrates PHYS-01 through PHYS-09 into a single coherent scientific
statement about what the ED PDE *is*, what it *is not*, and what its
structural analogies *mean*.
"""

from __future__ import annotations

from dataclasses import dataclass, field


# ---------------------------------------------------------------
# Structured interpretation object
# ---------------------------------------------------------------

@dataclass
class ExperimentalFinding:
    """One finding from the PHYS programme."""
    number: int
    name: str
    result: str
    accuracy: str
    significance: str


@dataclass
class UniversalityClass:
    """ED's position in the PDE landscape."""
    name: str
    defining_properties: list
    nearest_relatives: list
    distinguishing_features: list


@dataclass
class AnalogueMapping:
    """A structural analogy between ED and another domain."""
    target: str
    mechanism: str
    quality: str
    caveat: str


@dataclass
class MasterInterpretation:
    """Complete scientific interpretation of the ED PDE.

    Attributes
    ----------
    mathematical_identity : str
    physical_identity : str
    universality : UniversalityClass
    findings : list[ExperimentalFinding]
    analogues : list[AnalogueMapping]
    is_not : dict[str, str]
    is_what : str
    limitations : list[str]
    open_questions : list[str]
    """

    mathematical_identity: str
    physical_identity: str
    universality: UniversalityClass
    findings: list
    analogues: list
    is_not: dict
    is_what: str
    limitations: list
    open_questions: list


# ---------------------------------------------------------------
# Builder
# ---------------------------------------------------------------

def build_master_interpretation() -> MasterInterpretation:
    """Construct the complete scientific interpretation of ED."""

    # ------ Findings ------
    findings = [
        ExperimentalFinding(
            1, "Diffusion limit",
            "D_eff = D * M_star with 7.5% accuracy",
            "7.5%",
            "ED's principal operator is a nonlinear diffusion.",
        ),
        ExperimentalFinding(
            2, "Wave/telegraph limit",
            "Telegraph oscillation omega = 0.0% error; no spatial waves",
            "omega: 0.0%, sigma(k): 0.1-0.8%",
            "Participation creates temporal oscillation, not spatial propagation.",
        ),
        ExperimentalFinding(
            3, "Reaction limit",
            "lambda = D * P0 with 0.03% accuracy, perfect symmetry",
            "0.03%",
            "The penalty is a linear reaction term.",
        ),
        ExperimentalFinding(
            4, "Pattern formation",
            "No instability: all sigma_k < 0 for all k",
            "Decisive negative",
            "ED cannot form Turing patterns. All structure is transient.",
        ),
        ExperimentalFinding(
            5, "Quantum-like regime",
            "Non-Gaussian profiles, nonlinear superposition breakdown",
            "Qualitative",
            "Density-dependent mobility mimics some quantum transport signatures.",
        ),
        ExperimentalFinding(
            6, "Phase diagram",
            "5 phases: telegraph (69%), diffusion (14%), transient (8%), "
            "quantum-like (6%), reaction (3%)",
            "64-point grid, 6 validated",
            "Telegraph dominates; diffusion/reaction are H=0 only.",
        ),
        ExperimentalFinding(
            7, "Energy/Lyapunov structure",
            "5 simultaneous Lyapunov functionals; NOT a gradient flow "
            "(995% residual); Boltzmann entropy increases",
            "Machine precision for monotonicity",
            "ED is dissipative but not variational.",
        ),
        ExperimentalFinding(
            8, "Physical interpretation",
            "Population/agent density is strongest match (8/10)",
            "Scoring matrix, 8 domains",
            "ED is a degenerate reaction-diffusion with carrying capacity.",
        ),
        ExperimentalFinding(
            9, "Cosmological analogues",
            "All 5 structural analogues confirmed: expansion, horizons, "
            "structure, deceleration, scale factor",
            "Qualitative confirmation",
            "Mathematical analogies via shared PDE structure.",
        ),
    ]

    # ------ Universality class ------
    universality = UniversalityClass(
        name="Degenerate parabolic reaction-diffusion with global feedback",
        defining_properties=[
            "Second-order quasilinear parabolic",
            "Degenerate mobility M(rho) -> 0 at capacity bound",
            "Monostable linear penalty (unique attractor)",
            "Global scalar feedback (participation variable v)",
            "Five simultaneous Lyapunov functionals (H=0)",
            "No pattern formation (unconditionally stable)",
        ],
        nearest_relatives=[
            ("Porous-medium equation", "Identical principal operator"),
            ("Monostable reaction-diffusion", "Same diffusion + penalty structure"),
            ("Population density with crowding", "8/10 property match"),
            ("Fokker-Planck", "Gradient-flow relative, differs by degeneracy"),
        ],
        distinguishing_features=[
            "Participation coupling v(t) — no other comparison PDE has this",
            "Telegraph oscillation of the k=0 mode",
            "Five simultaneous Lyapunov functionals",
            "NOT a gradient flow despite being dissipative",
            "Degenerate mobility creating horizon-like free boundaries",
        ],
    )

    # ------ Analogues ------
    analogues = [
        AnalogueMapping(
            "Cosmological expansion", "Penalty-driven density decay",
            "Strong (exponential decay matches qualitatively)",
            "No metric, no curvature, not physical expansion",
        ),
        AnalogueMapping(
            "Causal horizons", "Degenerate mobility M -> 0",
            "Strong (regions dynamically isolated)",
            "Diffusion barrier, not null surface",
        ),
        AnalogueMapping(
            "Cosmic web", "Hessian eigenvalue morphology",
            "Moderate (filament/sheet/blob taxonomy matches)",
            "ED structure decays; cosmic structure grows",
        ),
        AnalogueMapping(
            "Quantum spreading", "Density-dependent mobility",
            "Weak (non-Gaussian profiles)",
            "Classical nonlinear diffusion, not quantum",
        ),
        AnalogueMapping(
            "Telegraph communication", "Participation coupling",
            "Strong (exact telegraph equation for k=0 mode)",
            "Only the uniform mode oscillates",
        ),
    ]

    # ------ What ED is NOT ------
    is_not = {
        "quantum": (
            "ED is classical, dissipative, and parabolic.  It has no "
            "Planck constant, no superposition principle, no entanglement, "
            "and no measurement problem.  The non-Gaussian spreading is "
            "a porous-medium effect, not a quantum signature."
        ),
        "hydrodynamic": (
            "ED evolves a scalar density, not a velocity field.  There is "
            "no advection, no Reynolds number, no turbulence.  The "
            "participation variable v(t) is a global scalar, not a "
            "spatially resolved velocity."
        ),
        "thermodynamic": (
            "ED does not maximise entropy.  Boltzmann entropy increases "
            "but is not a Lyapunov functional.  ED is not a "
            "detailed-balance system and cannot be derived from a "
            "partition function."
        ),
        "variational": (
            "ED possesses five Lyapunov functionals but is NOT a gradient "
            "flow of any of them.  The operator residual between ED and "
            "the gradient flow of its Lyapunov functional is ~995%.  "
            "ED is dissipative but not variational."
        ),
        "relativistic": (
            "ED has no metric tensor, no curvature tensor, no geodesics, "
            "no Lorentz invariance.  The cosmological analogues are "
            "structural (shared PDE features), not physical (no gravity)."
        ),
    }

    # ------ What ED IS ------
    is_what = (
        "The ED PDE is a degenerate parabolic reaction-diffusion equation "
        "with global feedback.  Its natural interpretation is as a model "
        "of DENSITY-DEPENDENT TRANSPORT WITH CARRYING CAPACITY:\n\n"
        "- rho(x,t) is a density field (population, concentration, probability)\n"
        "- M(rho) = M0 (rho_max - rho)^beta is crowding-reduced mobility\n"
        "- P(rho) = P0 (rho - rho*) is a restoring force toward equilibrium\n"
        "- v(t) is a global feedback variable (resource, environment)\n"
        "- rho_max is the carrying capacity / packing limit\n\n"
        "This framework is mathematically unique: no other PDE in the "
        "comparison set (PME, AC, CH, FP, TFE, MCF) combines all five "
        "of ED's distinguishing features (degenerate mobility, monostable "
        "penalty, participation coupling, five Lyapunov functionals, "
        "non-gradient-flow dissipation)."
    )

    # ------ Limitations ------
    limitations = [
        "No experimental validation against physical data.",
        "Constitutive functions (M, P) are postulated, not derived.",
        "No microscopic derivation from statistical mechanics.",
        "Deterministic only: no noise term.",
        "Single scalar field: no multi-component coupling.",
        "The cosmological analogues are structural, not physical.",
        "The quantum-like signatures are classical nonlinear effects.",
    ]

    # ------ Open questions ------
    open_questions = [
        "Can ED be derived as a hydrodynamic limit of a microscopic model?",
        "What physical system has exactly the ED constitutive structure?",
        "Does stochastic ED (with noise) produce qualitatively new phenomena?",
        "Can the participation coupling be given a thermodynamic interpretation?",
        "Do the five Lyapunov functionals have independent physical meanings?",
        "Is there a natural generalisation of ED to multi-field coupling?",
        "Can the cosmological analogues be sharpened to quantitative predictions?",
    ]

    return MasterInterpretation(
        mathematical_identity=(
            "Quasilinear degenerate parabolic PDE with monostable penalty "
            "and global scalar feedback."
        ),
        physical_identity=(
            "Density-dependent transport with carrying capacity, "
            "relaxation toward equilibrium, and global feedback."
        ),
        universality=universality,
        findings=findings,
        analogues=analogues,
        is_not=is_not,
        is_what=is_what,
        limitations=limitations,
        open_questions=open_questions,
    )


# ---------------------------------------------------------------
# Report generator
# ---------------------------------------------------------------

def build_master_report() -> str:
    """Generate the full ED-PHYS-10 report."""
    mi = build_master_interpretation()
    lines = [
        "# ED-PHYS-10: Master Interpretation and Synthesis",
        "",
        "## Mathematical Identity",
        "",
        mi.mathematical_identity,
        "",
        "## Physical Identity",
        "",
        mi.physical_identity,
        "",
        "## Experimental Programme Summary",
        "",
        "| # | Experiment | Key Result | Accuracy |",
        "|---|-----------|------------|----------|",
    ]

    for f in mi.findings:
        lines.append(f"| {f.number} | {f.name} | {f.result} | {f.accuracy} |")

    lines.extend([
        "",
        "## Universality Class",
        "",
        f"**{mi.universality.name}**",
        "",
        "### Defining Properties",
        "",
    ])
    for p in mi.universality.defining_properties:
        lines.append(f"- {p}")

    lines.extend(["", "### Nearest Relatives", ""])
    for name, reason in mi.universality.nearest_relatives:
        lines.append(f"- **{name}:** {reason}")

    lines.extend(["", "### Distinguishing Features", ""])
    for feat in mi.universality.distinguishing_features:
        lines.append(f"- {feat}")

    lines.extend([
        "",
        "## What ED Is",
        "",
        mi.is_what,
        "",
        "## What ED Is Not",
        "",
    ])
    for domain, reason in mi.is_not.items():
        lines.extend([f"### Not {domain.title()}", "", reason, ""])

    lines.extend(["## Structural Analogues", ""])
    for a in mi.analogues:
        lines.extend([
            f"### {a.target}",
            "",
            f"- **Mechanism:** {a.mechanism}",
            f"- **Quality:** {a.quality}",
            f"- **Caveat:** {a.caveat}",
            "",
        ])

    lines.extend(["## Limitations", ""])
    for lim in mi.limitations:
        lines.append(f"- {lim}")

    lines.extend(["", "## Open Questions", ""])
    for q in mi.open_questions:
        lines.append(f"- {q}")

    lines.extend([
        "",
        "## Closing Statement",
        "",
        "The Event Density PDE is a mathematically well-defined object "
        "whose structure has been characterised across nine experiments.  "
        "It is a degenerate parabolic reaction-diffusion equation with "
        "global feedback — the simplest PDE that simultaneously exhibits "
        "degenerate mobility, monostable penalty, five Lyapunov functionals, "
        "telegraph-like oscillation, and transient morphological structure.  "
        "Its natural physical domain is density-dependent transport with "
        "carrying capacity.  Its structural analogies to cosmology, "
        "statistical mechanics, and population dynamics are mathematically "
        "precise but physically non-committal.  The framework is complete, "
        "reproducible, and falsifiable.",
    ])

    return "\n".join(lines)
