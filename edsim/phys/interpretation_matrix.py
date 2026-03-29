"""
edsim.phys.interpretation_matrix — Physical interpretation framework for ED.

This module maps the ED PDE's mathematical structure to candidate physical
domains where its dynamics might apply.  It uses the empirical findings
of PHYS-01 through PHYS-07 as scoring criteria.

ED's established properties (from PHYS-01 through PHYS-07):

    P1. Parabolic (diffusive), not hyperbolic (PHYS-02)
    P2. Effective diffusion D_eff = D * M_star (PHYS-01)
    P3. Effective reaction lambda = D * P0 (PHYS-03)
    P4. Telegraph oscillation for H > 0 (PHYS-02)
    P5. No pattern formation (PHYS-04)
    P6. Non-Gaussian spreading from nonlinear mobility (PHYS-05)
    P7. Five simultaneous Lyapunov functionals (PHYS-07)
    P8. NOT a gradient flow (PHYS-07)
    P9. Unique attractor (all laws)
    P10. Degenerate mobility (horizons) (PHYS-06)

Each candidate domain is scored on how many of these 10 properties
it shares (match) and how many it contradicts (mismatch).
"""

from __future__ import annotations

from dataclasses import dataclass, field


# ---------------------------------------------------------------
# Domain dataclass
# ---------------------------------------------------------------

@dataclass
class PhysicalDomain:
    """A candidate physical interpretation of the ED PDE.

    Attributes
    ----------
    name : str
    governing_equation : str
        The PDE or dynamical equation of the domain.
    key_features : list[str]
        Physical properties of this domain.
    matches : dict[str, str]
        ED property -> why it matches this domain.
    mismatches : dict[str, str]
        ED property -> why it does NOT match this domain.
    match_score : int
        Number of matching ED properties (out of 10).
    mismatch_score : int
        Number of contradicting ED properties.
    plausibility : str
        "strong", "moderate", "weak", "poor".
    notes : str
    """

    name: str
    governing_equation: str
    key_features: list
    matches: dict
    mismatches: dict
    match_score: int = 0
    mismatch_score: int = 0
    plausibility: str = ""
    notes: str = ""

    def __post_init__(self):
        self.match_score = len(self.matches)
        self.mismatch_score = len(self.mismatches)
        if self.match_score >= 8:
            self.plausibility = "strong"
        elif self.match_score >= 6:
            self.plausibility = "moderate"
        elif self.match_score >= 4:
            self.plausibility = "weak"
        else:
            self.plausibility = "poor"


# ---------------------------------------------------------------
# Domain definitions
# ---------------------------------------------------------------

def _build_porous_medium() -> PhysicalDomain:
    return PhysicalDomain(
        name="Porous-medium / groundwater flow",
        governing_equation="d u/dt = div(u^m grad u)",
        key_features=[
            "Nonlinear degenerate diffusion",
            "Compact support (free boundaries)",
            "Barenblatt self-similar profiles",
            "No reaction term in pure form",
        ],
        matches={
            "P1_parabolic": "PME is parabolic",
            "P2_diffusion": "PME has effective D(u) = (m+1) u^m",
            "P6_nonGaussian": "PME produces non-Gaussian profiles (Barenblatt)",
            "P7_Lyapunov": "PME has entropy-type Lyapunov functionals",
            "P10_degenerate": "PME mobility vanishes at u=0 (free boundary)",
            "P5_no_patterns": "PME does not form patterns",
        },
        mismatches={
            "P3_reaction": "Pure PME has no reaction term",
            "P4_telegraph": "PME has no global oscillator",
            "P9_attractor": "PME attractor is Barenblatt, not uniform",
            "P8_not_gradflow": "PME IS a gradient flow (Wasserstein)",
        },
        notes="Closest PDE relative (ED-Phys-38). ED = PME + penalty + participation.",
    )


def _build_reaction_diffusion() -> PhysicalDomain:
    return PhysicalDomain(
        name="Reaction-diffusion (chemical kinetics)",
        governing_equation="d u/dt = D Lap(u) + f(u)",
        key_features=[
            "Diffusion + nonlinear reaction",
            "Can form Turing patterns (multi-species)",
            "Bistable or monostable kinetics",
            "Traveling waves possible",
        ],
        matches={
            "P1_parabolic": "RD is parabolic",
            "P2_diffusion": "RD has linear diffusion D Lap(u)",
            "P3_reaction": "RD has reaction term f(u)",
            "P5_no_patterns": "Monostable single-species RD has no patterns",
            "P7_Lyapunov": "Many RD systems have Lyapunov functionals",
            "P9_attractor": "Monostable RD has unique attractor",
        },
        mismatches={
            "P10_degenerate": "Standard RD has constant diffusion (no degeneracy)",
            "P4_telegraph": "Standard RD has no global oscillator",
            "P6_nonGaussian": "Linear diffusion gives Gaussian spreading",
            "P8_not_gradflow": "Some RD are gradient flows (variational)",
        },
        notes="ED is a degenerate reaction-diffusion equation with penalty + participation.",
    )


def _build_telegraph() -> PhysicalDomain:
    return PhysicalDomain(
        name="Telegraph / Cattaneo relaxation",
        governing_equation="tau u_tt + u_t = D Lap(u)",
        key_features=[
            "Finite propagation speed",
            "Damped oscillation",
            "Transition from wave-like to diffusive",
        ],
        matches={
            "P4_telegraph": "ED's (rho, v) system is telegraph-like for k=0",
            "P1_parabolic": "Telegraph is parabolic in the overdamped limit",
            "P3_reaction": "Damping acts like a reaction term",
        },
        mismatches={
            "P2_diffusion": "Telegraph has finite propagation speed; ED does not",
            "P10_degenerate": "Standard telegraph has constant coefficients",
            "P5_no_patterns": "Telegraph has no pattern formation either (match)",
            "P6_nonGaussian": "Telegraph spreading is different from ED",
            "P9_attractor": "Telegraph attractor is zero, not structured rho*",
            "P7_Lyapunov": "Telegraph energy is standard wave energy, not Phi(rho)",
            "P8_not_gradflow": "Telegraph is NOT a gradient flow either (match)",
        },
        notes="ED's telegraph character is LIMITED to the k=0 (uniform) mode only.",
    )


def _build_population_density() -> PhysicalDomain:
    return PhysicalDomain(
        name="Population / agent density models",
        governing_equation="d rho/dt = div(D(rho) grad rho) + r(rho)",
        key_features=[
            "Density-dependent dispersal",
            "Carrying capacity (saturation)",
            "Logistic or Allee kinetics",
            "Crowding effects",
        ],
        matches={
            "P1_parabolic": "Population models are parabolic",
            "P2_diffusion": "Density-dependent diffusion D(rho)",
            "P3_reaction": "Growth/death kinetics r(rho)",
            "P10_degenerate": "Crowding reduces mobility at high density",
            "P6_nonGaussian": "Nonlinear diffusion gives non-Gaussian fronts",
            "P9_attractor": "Carrying capacity = unique steady state",
            "P5_no_patterns": "Single-species without chemotaxis has no patterns",
            "P7_Lyapunov": "Population models often have Lyapunov functionals",
        },
        mismatches={
            "P4_telegraph": "No global oscillator in standard population models",
            "P8_not_gradflow": "Many population models ARE gradient flows",
        },
        notes="Strong structural match: rho_max = carrying capacity, P = logistic penalty.",
    )


def _build_stat_mech() -> PhysicalDomain:
    return PhysicalDomain(
        name="Statistical mechanics (Fokker-Planck)",
        governing_equation="d p/dt = div(D grad p + p grad V)",
        key_features=[
            "Probability density evolution",
            "Boltzmann equilibrium",
            "Free-energy gradient flow (Wasserstein)",
            "Detailed balance",
        ],
        matches={
            "P1_parabolic": "FP is parabolic",
            "P2_diffusion": "FP has diffusion D grad p",
            "P3_reaction": "Drift p grad V acts like reaction",
            "P7_Lyapunov": "FP has free energy Lyapunov functional",
            "P9_attractor": "Boltzmann distribution is unique attractor",
        },
        mismatches={
            "P10_degenerate": "Standard FP has linear diffusion (no degeneracy)",
            "P4_telegraph": "No global oscillator",
            "P6_nonGaussian": "Linear FP gives Gaussian relaxation",
            "P8_not_gradflow": "FP IS a Wasserstein gradient flow",
            "P5_no_patterns": "FP has no patterns (match, but trivially)",
        },
        notes="Close structural relative. ED differs by degenerate mobility and participation.",
    )


def _build_thin_film() -> PhysicalDomain:
    return PhysicalDomain(
        name="Thin-film / lubrication flow",
        governing_equation="d h/dt = -div(h^n grad Lap h)",
        key_features=[
            "Fourth-order PDE",
            "Degenerate mobility h^n",
            "Contact-line dynamics",
            "Dewetting instabilities",
        ],
        matches={
            "P10_degenerate": "TFE has degenerate mobility h^n -> 0",
            "P6_nonGaussian": "TFE produces non-Gaussian profiles",
            "P7_Lyapunov": "TFE has surface-energy Lyapunov functional",
        },
        mismatches={
            "P1_parabolic": "TFE is fourth-order, not second-order",
            "P2_diffusion": "TFE diffusion scales as k^4, not k^2",
            "P3_reaction": "TFE has no reaction term",
            "P4_telegraph": "No global oscillator",
            "P5_no_patterns": "TFE CAN form dewetting patterns",
            "P9_attractor": "TFE attractor is flat film, different structure",
            "P8_not_gradflow": "TFE IS a gradient flow",
        },
        notes="Shares degeneracy with ED but order mismatch (4th vs 2nd) is fundamental.",
    )


def _build_rg_flow() -> PhysicalDomain:
    return PhysicalDomain(
        name="Renormalisation group (RG) flow",
        governing_equation="d g_i/ds = beta_i(g)",
        key_features=[
            "Flow in coupling-constant space",
            "Fixed points (UV/IR)",
            "Irreversibility (c-theorem)",
            "Dimensional reduction",
        ],
        matches={
            "P9_attractor": "RG flows have fixed-point attractors",
            "P7_Lyapunov": "c-theorem provides Lyapunov function (in 2D)",
            "P8_not_gradflow": "RG flow is generally NOT a gradient flow",
        },
        mismatches={
            "P1_parabolic": "RG flow is ODE in coupling space, not PDE in real space",
            "P2_diffusion": "No spatial diffusion",
            "P3_reaction": "Beta functions are not reaction terms",
            "P4_telegraph": "No telegraph structure",
            "P10_degenerate": "No mobility degeneracy",
            "P5_no_patterns": "Not applicable (no spatial domain)",
            "P6_nonGaussian": "Not applicable",
        },
        notes="Metaphorical analogy only: both are dissipative flows toward fixed points.",
    )


def _build_hydrodynamic() -> PhysicalDomain:
    return PhysicalDomain(
        name="Hydrodynamic limits (coarse-grained fluid)",
        governing_equation="d rho/dt + div(rho u) = 0; Navier-Stokes for u",
        key_features=[
            "Density + velocity fields",
            "Advection-diffusion coupling",
            "Turbulence, instabilities",
            "Reynolds-number dependence",
        ],
        matches={
            "P1_parabolic": "Diffusion part of NS is parabolic",
            "P2_diffusion": "Viscous diffusion",
            "P7_Lyapunov": "Energy dissipation in viscous fluids",
        },
        mismatches={
            "P3_reaction": "NS has no reaction/penalty term",
            "P4_telegraph": "NS velocity is a field, not a global scalar",
            "P5_no_patterns": "NS produces turbulent patterns",
            "P9_attractor": "NS attractors are complex (turbulence)",
            "P10_degenerate": "NS viscosity is not density-dependent (usually)",
            "P6_nonGaussian": "NS non-Gaussianity comes from advection, not mobility",
            "P8_not_gradflow": "NS is NOT a gradient flow (match)",
        },
        notes="ED's v(t) is a scalar, not a velocity field. Structural overlap is limited.",
    )


# ---------------------------------------------------------------
# Matrix builder
# ---------------------------------------------------------------

@dataclass
class InterpretationMatrix:
    """The complete interpretation matrix.

    Attributes
    ----------
    domains : list[PhysicalDomain]
    ed_properties : list[str]
    ranking : list[tuple[str, int, int, str]]
        (name, match_score, mismatch_score, plausibility), sorted by match score.
    """

    domains: list
    ed_properties: list
    ranking: list


ED_PROPERTIES = [
    "P1_parabolic", "P2_diffusion", "P3_reaction", "P4_telegraph",
    "P5_no_patterns", "P6_nonGaussian", "P7_Lyapunov",
    "P8_not_gradflow", "P9_attractor", "P10_degenerate",
]


def build_interpretation_matrix() -> InterpretationMatrix:
    """Build the complete interpretation matrix.

    Returns
    -------
    InterpretationMatrix
    """
    domains = [
        _build_porous_medium(),
        _build_reaction_diffusion(),
        _build_population_density(),
        _build_stat_mech(),
        _build_telegraph(),
        _build_thin_film(),
        _build_hydrodynamic(),
        _build_rg_flow(),
    ]

    ranking = sorted(
        [(d.name, d.match_score, d.mismatch_score, d.plausibility) for d in domains],
        key=lambda x: (-x[1], x[2]),
    )

    return InterpretationMatrix(
        domains=domains,
        ed_properties=ED_PROPERTIES,
        ranking=ranking,
    )
