"""
edsim.comparison.frameworks -- Structured descriptions of theoretical frameworks.

Each framework is represented along five comparison axes:
    ontology      -- what exists
    primitives    -- irreducible building blocks
    dynamics      -- evolution or update rules
    invariants    -- conserved or monotone quantities
    epistemology  -- what is observable or measurable

ED is auto-generated from the axiom and law modules to ensure
consistency with the rest of the codebase.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class Framework:
    """Structured description of a theoretical framework.

    Attributes
    ----------
    name : str
        Short identifier.
    full_name : str
        Full descriptive name.
    ontology : list[str]
        What exists in this framework.
    primitives : list[str]
        Irreducible building blocks.
    dynamics : list[str]
        Evolution or update rules.
    invariants : list[str]
        Conserved or monotone quantities.
    epistemology : list[str]
        What is observable or measurable.
    key_equations : list[str]
        Central equations (LaTeX strings).
    references : list[str]
        Key references (author-year).
    notes : str
        Brief contextual notes.
    """

    name: str
    full_name: str
    ontology: tuple = ()
    primitives: tuple = ()
    dynamics: tuple = ()
    invariants: tuple = ()
    epistemology: tuple = ()
    key_equations: tuple = ()
    references: tuple = ()
    notes: str = ""


# ══════════════════════════════════════════════════════════════════════
#  Framework definitions
# ══════════════════════════════════════════════════════════════════════

CAUSAL_SETS = Framework(
    name="causal_sets",
    full_name="Causal Set Theory",
    ontology=(
        "Discrete partial order of events",
        "No continuous manifold",
        "Spacetime is emergent from causal relations",
    ),
    primitives=(
        "Events (elements of the causet)",
        "Causal order (partial order relation)",
        "Valence (local connectivity)",
    ),
    dynamics=(
        "Classical sequential growth (Rideout-Sorkin)",
        "Stochastic element birth with causal constraints",
        "No deterministic PDE; growth is probabilistic",
    ),
    invariants=(
        "Causal diamond volumes (Myrheim-Meyer dimension)",
        "Order-interval counts",
        "Benincasa-Dowker action (discrete Einstein-Hilbert)",
    ),
    epistemology=(
        "Causal relations between events",
        "Spacetime dimension (from order statistics)",
        "Discrete geodesic distance",
    ),
    key_equations=(
        "P(\\text{birth at } e) \\propto \\exp(-S_{BD}[C \\cup e])",
    ),
    references=(
        "Bombelli et al. (1987)",
        "Sorkin (2003)",
        "Surya (2019)",
    ),
    notes=(
        "Fundamentally discrete and Lorentzian.  No density field.  "
        "Dynamics is birth-process, not flow."
    ),
)

ENTROPIC_GRAVITY = Framework(
    name="entropic_gravity",
    full_name="Entropic Gravity (Verlinde)",
    ontology=(
        "Holographic screens encoding information",
        "Entropy as the fundamental quantity",
        "Gravity is an entropic force, not a fundamental interaction",
    ),
    primitives=(
        "Entropy S",
        "Temperature T",
        "Holographic screen area A",
        "Information bits N",
    ),
    dynamics=(
        "F = T dS/dx (entropic force law)",
        "Equipartition: E = (1/2) N k_B T",
        "No PDE for a density field; force emerges from entropy gradients",
    ),
    invariants=(
        "Total energy (first law)",
        "Entropy non-decrease (second law)",
        "Holographic bound (Bekenstein)",
    ),
    epistemology=(
        "Gravitational acceleration",
        "Temperature of holographic screens",
        "Entropy of horizons",
    ),
    key_equations=(
        "F \\Delta x = T \\Delta S",
        "S = \\frac{k_B c^3}{4 G \\hbar} A",
    ),
    references=(
        "Verlinde (2011)",
        "Jacobson (1995)",
        "Padmanabhan (2010)",
    ),
    notes=(
        "Gravity from thermodynamics.  No scalar field evolution.  "
        "Structural similarity to ED via entropy gradients."
    ),
)

CONSTRUCTOR_THEORY = Framework(
    name="constructor_theory",
    full_name="Constructor Theory (Deutsch-Marletto)",
    ontology=(
        "Substrates (physical systems)",
        "Constructors (agents of transformation)",
        "Tasks (possible/impossible transformations)",
    ),
    primitives=(
        "Task T: input state -> output state",
        "Constructor C: enables T without net change to C",
        "Possibility/impossibility as fundamental",
    ),
    dynamics=(
        "No evolution equation",
        "Counterfactual structure: which tasks are possible",
        "Laws constrain the space of possible transformations",
    ),
    invariants=(
        "Constructor invariance (C is unchanged after performing T)",
        "Interoperability (composability of tasks)",
        "Information conservation (in reversible tasks)",
    ),
    epistemology=(
        "Which transformations are possible",
        "Which are impossible and why",
        "Composition of tasks",
    ),
    key_equations=(),
    references=(
        "Deutsch (2013)",
        "Marletto (2015)",
        "Marletto (2020)",
    ),
    notes=(
        "Meta-theory about possibility, not dynamics.  No PDE, no "
        "density field, no time evolution.  Structural parallel: "
        "ED's axioms constrain what dynamics are possible."
    ),
)

HYDRODYNAMICS = Framework(
    name="hydrodynamics",
    full_name="Classical Hydrodynamics (Navier-Stokes)",
    ontology=(
        "Continuous fluid (density, velocity, pressure fields)",
        "Newtonian spacetime",
        "Viscous or inviscid flow",
    ),
    primitives=(
        "Density rho(x,t)",
        "Velocity u(x,t)",
        "Pressure p(x,t)",
        "Viscosity nu",
    ),
    dynamics=(
        "Continuity: partial_t rho + div(rho u) = 0",
        "Navier-Stokes: rho (partial_t u + u.grad u) = -grad p + nu laplacian u",
        "Energy equation (optional)",
    ),
    invariants=(
        "Mass (continuity equation)",
        "Momentum (Navier-Stokes)",
        "Energy (Bernoulli / energy equation)",
        "Circulation (Kelvin's theorem, inviscid)",
    ),
    epistemology=(
        "Velocity fields (PIV, LDV)",
        "Pressure (manometry)",
        "Density (schlieren, interferometry)",
        "Vorticity",
    ),
    key_equations=(
        "\\partial_t \\rho + \\nabla\\!\\cdot\\!(\\rho \\mathbf{u}) = 0",
        "\\rho(\\partial_t \\mathbf{u} + \\mathbf{u}\\!\\cdot\\!\\nabla\\mathbf{u}) "
        "= -\\nabla p + \\nu \\nabla^2 \\mathbf{u}",
    ),
    references=(
        "Landau & Lifshitz (1987)",
        "Batchelor (1967)",
    ),
    notes=(
        "Vector field dynamics (velocity).  ED is scalar (density only).  "
        "Hydrodynamics has advection; ED has diffusion + penalty."
    ),
)

STATISTICAL_MECHANICS = Framework(
    name="statistical_mechanics",
    full_name="Statistical Mechanics (Equilibrium + Non-equilibrium)",
    ontology=(
        "Microstates (phase space configurations)",
        "Macrostates (thermodynamic variables)",
        "Ensembles (microcanonical, canonical, grand canonical)",
    ),
    primitives=(
        "Hamiltonian H(q, p)",
        "Phase space distribution f(q, p, t)",
        "Temperature T, entropy S, free energy F",
    ),
    dynamics=(
        "Liouville equation: partial_t f = {H, f}",
        "Boltzmann equation: partial_t f + v.grad f = C[f]",
        "Fokker-Planck: partial_t p = div(D grad p + p grad V)",
        "Master equations (discrete state spaces)",
    ),
    invariants=(
        "Energy (Hamiltonian conservation)",
        "Entropy non-decrease (H-theorem)",
        "Free energy decrease (canonical ensemble)",
        "Phase space volume (Liouville's theorem)",
    ),
    epistemology=(
        "Thermodynamic observables (T, P, S, F)",
        "Correlation functions",
        "Response functions (susceptibility)",
        "Fluctuation spectra",
    ),
    key_equations=(
        "S = -k_B \\sum p_i \\ln p_i",
        "\\partial_t p = \\nabla\\!\\cdot\\!(D\\nabla p + p \\nabla V)",
    ),
    references=(
        "Landau & Lifshitz (1980)",
        "Pathria & Beale (2011)",
        "Zwanzig (2001)",
    ),
    notes=(
        "Closest established framework to ED's gradient-flow structure.  "
        "Fokker-Planck shares the diffusion + drift architecture.  "
        "ED adds degenerate mobility and participation coupling."
    ),
)

QUANTUM_FOUNDATIONS = Framework(
    name="quantum_foundations",
    full_name="Quantum Foundations (Operational / Information-theoretic)",
    ontology=(
        "Hilbert space states |psi>",
        "Observables (self-adjoint operators)",
        "Measurement outcomes (classical data)",
    ),
    primitives=(
        "State vector |psi> in H",
        "Unitary evolution U(t)",
        "Born rule: P(a) = |<a|psi>|^2",
        "Density matrix rho = |psi><psi|",
    ),
    dynamics=(
        "Schrodinger equation: i hbar partial_t |psi> = H |psi>",
        "von Neumann equation: partial_t rho = -i/hbar [H, rho]",
        "Lindblad equation (open systems)",
        "Measurement collapse (non-unitary)",
    ),
    invariants=(
        "Unitarity (norm conservation)",
        "Trace preservation (density matrix)",
        "von Neumann entropy (constant under unitary evolution)",
        "Energy (for time-independent H)",
    ),
    epistemology=(
        "Measurement outcomes (discrete)",
        "Expectation values <A>",
        "Transition probabilities",
        "Entanglement witnesses",
    ),
    key_equations=(
        "i\\hbar \\partial_t |\\psi\\rangle = \\hat{H}|\\psi\\rangle",
        "P(a) = |\\langle a|\\psi\\rangle|^2",
    ),
    references=(
        "von Neumann (1932)",
        "Nielsen & Chuang (2000)",
        "Hardy (2001)",
    ),
    notes=(
        "Linear, unitary, complex Hilbert space dynamics.  ED is "
        "nonlinear, dissipative, real scalar field.  Structural "
        "parallel: density matrix rho ~ ED density field rho."
    ),
)


def _build_ed_framework() -> Framework:
    """Auto-generate the ED framework description from axioms and laws."""
    from ..math.architecture import ArchitecturalAxioms
    from ..math.laws import ALL_LAWS

    axioms = ArchitecturalAxioms.all_axioms()

    return Framework(
        name="event_density",
        full_name="Event Density (ED)",
        ontology=(
            "Scalar density field rho(x,t) on bounded domain",
            "Global participation variable v(t)",
            "No spacetime geometry assumed; domain is Euclidean",
            "Events are density excursions; becoming is flow",
        ),
        primitives=(
            "Density rho(x,t) in [0, rho_max]",
            "Participation v(t) (scalar)",
            "Mobility M(rho) = M0 (rho_max - rho)^beta",
            "Penalty P(rho) = P0 (rho - rho*)",
            "Diffusion weight D, coupling H, damping zeta, timescale tau",
        ),
        dynamics=(
            "partial_t rho = D [M(rho) laplacian(rho) + M'(rho)|grad rho|^2 - P(rho)] + H v",
            "dot{v} = (1/tau)(bar{F} - zeta v)",
            "Quasilinear parabolic with degenerate mobility",
            "Neumann or periodic boundary conditions",
        ),
        invariants=tuple(
            f"Law {law.number}: {law.name}" for law in ALL_LAWS
        ),
        epistemology=(
            "Lyapunov energy E[rho]",
            "ED-complexity C[rho] = int |grad rho|^2 dV",
            "Spectral entropy H = -sum p_k log p_k",
            "Dissipation channels R_grad, R_pen, R_part",
            "Morphology fractions (blob, sheet, filament, pancake)",
            "Euler characteristic chi",
            "Correlation length xi",
        ),
        key_equations=(
            "\\partial_t \\rho = D\\,F[\\rho] + H\\,v",
            "F[\\rho] = M(\\rho)\\nabla^2\\rho + M'(\\rho)|\\nabla\\rho|^2 - P(\\rho)",
            "\\dot{v} = \\tau^{-1}(\\bar{F} - \\zeta v)",
        ),
        references=(
            "ED-Phys-01 through ED-Phys-40",
            "ED-SIM-02 Architecture Document",
        ),
        notes=(
            "Scalar, nonlinear, dissipative, parabolic PDE with "
            "degenerate mobility and global participation coupling.  "
            "Nine architectural laws.  Verified in d=1,2,3,4."
        ),
    )


_EXTERNAL_FRAMEWORKS = [
    CAUSAL_SETS,
    ENTROPIC_GRAVITY,
    CONSTRUCTOR_THEORY,
    HYDRODYNAMICS,
    STATISTICAL_MECHANICS,
    QUANTUM_FOUNDATIONS,
]


def load_frameworks() -> list[Framework]:
    """Return all frameworks including ED.

    ED is always the last entry.

    Returns
    -------
    list[Framework]
        Six external frameworks + ED.
    """
    return list(_EXTERNAL_FRAMEWORKS) + [_build_ed_framework()]


def get_framework(name: str) -> Framework:
    """Retrieve a framework by name."""
    for f in load_frameworks():
        if f.name == name:
            return f
    raise KeyError(f"Unknown framework: {name}")
