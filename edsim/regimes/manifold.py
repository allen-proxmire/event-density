"""
edsim.regimes.manifold -- Physical regime definitions for Event Density.

Defines five canonical regimes spanning 60 orders of magnitude in
length scale.  Each regime specifies characteristic scale ranges,
relevant dimensionless groups, and physical analogues.

The regime manifold is the space of all (L0, R0, T0) triples.
Each point in this space corresponds to a physical interpretation
of the nondimensional ED simulation.
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import Callable, Optional

from ..units import constants as C
from ..units.scales import Scales


@dataclass(frozen=True)
class Regime:
    """A physical regime in the ED parameter space.

    Attributes
    ----------
    name : str
        Short identifier (e.g. "quantum").
    label : str
        Display label (e.g. "Quantum-like").
    description : str
        One-paragraph description of the regime.
    L0_range : tuple[float, float]
        Characteristic length range [m] (min, max).
    R0_range : tuple[float, float]
        Characteristic density range [kg m^-3] (min, max).
    T0_range : tuple[float, float]
        Characteristic time range [s] (min, max).
    dimensionless_groups : dict[str, str]
        Key dimensionless ratios and their physical meaning.
    physical_examples : list[str]
        Concrete physical systems this regime could describe.
    color : str
        Matplotlib colour for plotting.
    """

    name: str
    label: str
    description: str
    L0_range: tuple[float, float]
    R0_range: tuple[float, float]
    T0_range: tuple[float, float] = (0.0, math.inf)
    dimensionless_groups: dict = field(default_factory=dict)
    physical_examples: list = field(default_factory=list)
    color: str = "grey"

    def contains(self, scales: Scales) -> bool:
        """Return True if the given Scales fall within this regime."""
        L_ok = self.L0_range[0] <= scales.L0 <= self.L0_range[1]
        R_ok = self.R0_range[0] <= scales.R0 <= self.R0_range[1]
        return L_ok and R_ok


# ══════════════════════════════════════════════════════════════════════
#  Canonical regimes
# ══════════════════════════════════════════════════════════════════════

QUANTUM = Regime(
    name="quantum",
    label="Quantum-like",
    description=(
        "Sub-nanometre length scales where the ED density field "
        "is interpreted as a probability density or wave-function "
        "amplitude.  The diffusion coefficient maps to hbar/2m and "
        "the penalty term to a confining potential.  Mobility "
        "degeneracy at rho_max corresponds to an exclusion principle."
    ),
    L0_range=(1e-36, 1e-9),
    R0_range=(1e10, 1e100),
    dimensionless_groups={
        "L0 / lambda_C": "Domain size / Compton wavelength",
        "R0 * L0^d": "Normalisation (should be O(1) for probability)",
        "D * T0 / L0^2": "Diffusive Peclet number (= 1 by construction)",
    },
    physical_examples=[
        "Electron probability density in a confining potential",
        "Quantum decoherence as mobility-driven diffusion",
        "Pilot-wave density evolution",
        "Planck-scale density fluctuations",
    ],
    color="#7B2FBE",
)

MESOSCOPIC = Regime(
    name="mesoscopic",
    label="Mesoscopic",
    description=(
        "Nanometre to hundred-micrometre length scales.  The ED "
        "density field is interpreted as a particle concentration or "
        "order parameter.  The mobility maps to a transport "
        "coefficient and the penalty to a free-energy restoring "
        "force.  Horizon formation corresponds to jamming or "
        "glass transitions."
    ),
    L0_range=(1e-9, 1e-4),
    R0_range=(1e-3, 1e6),
    dimensionless_groups={
        "L0 / a_0": "Domain size / Bohr radius",
        "R0 / rho_water": "Density relative to water",
        "Pe = V0 * L0 / D0": "Peclet number",
    },
    physical_examples=[
        "Colloidal suspension dynamics",
        "Block copolymer self-assembly",
        "Nanoparticle concentration fields",
        "Biological cell-density evolution",
    ],
    color="#2196F3",
)

CONDENSED_MATTER = Regime(
    name="condensed_matter",
    label="Condensed-matter-like",
    description=(
        "Micrometre to metre length scales with moderate densities.  "
        "The ED PDE maps to a porous-medium or thin-film equation "
        "with the mobility acting as a state-dependent conductivity "
        "or viscosity.  Horizons correspond to material interfaces "
        "where transport ceases."
    ),
    L0_range=(1e-6, 1e1),
    R0_range=(1e-1, 1e5),
    dimensionless_groups={
        "Re = V0 * L0 / nu": "Reynolds number (if nu ~ D0)",
        "M_star / M0": "Mobility contrast",
        "rho_star / rho_max": "Packing fraction",
    },
    physical_examples=[
        "Heat conduction in porous media",
        "Thin-film spreading and rupture",
        "Groundwater density transport",
        "Solidification front dynamics",
    ],
    color="#4CAF50",
)

GRAVITATIONAL = Regime(
    name="gravitational",
    label="Gravitational-like",
    description=(
        "Kiloparsec to megaparsec length scales with densities "
        "near the cosmic critical density.  The ED density field "
        "is interpreted as a dark-matter or baryon density.  The "
        "penalty term acts as a Hubble-expansion restoring force "
        "and horizons correspond to virialised structures."
    ),
    L0_range=(1e15, 1e23),
    R0_range=(1e-30, 1e-20),
    dimensionless_groups={
        "L0 / kpc": "Domain size in kiloparsecs",
        "R0 / rho_crit": "Density parameter Omega",
        "T0 * H_0": "Time in Hubble units",
    },
    physical_examples=[
        "Dark-matter halo density profiles",
        "Galaxy cluster baryon distribution",
        "Intracluster medium evolution",
        "Filamentary large-scale structure",
    ],
    color="#FF9800",
)

COSMOLOGICAL = Regime(
    name="cosmological",
    label="Cosmological-like",
    description=(
        "Hubble-scale lengths with critical-density normalisation.  "
        "The ED PDE describes the evolution of the large-scale "
        "density field.  Morphological fractions (filament, sheet, "
        "blob) map to the cosmic web classification.  The penalty "
        "drives the density toward the mean, analogous to Hubble "
        "expansion smoothing."
    ),
    L0_range=(1e23, 1e30),
    R0_range=(1e-30, 1e-24),
    dimensionless_groups={
        "L0 / (c / H_0)": "Domain size / Hubble length",
        "R0 / rho_crit": "Density parameter",
        "T0 / (1/H_0)": "Time / Hubble time",
    },
    physical_examples=[
        "Cosmic web filament and void evolution",
        "Large-scale density field smoothing",
        "BAO-scale density fluctuations",
        "Cosmic microwave background analogues",
    ],
    color="#F44336",
)


# ══════════════════════════════════════════════════════════════════════
#  Manifold
# ══════════════════════════════════════════════════════════════════════

_ALL_REGIMES = [QUANTUM, MESOSCOPIC, CONDENSED_MATTER, GRAVITATIONAL, COSMOLOGICAL]


def build_regime_manifold() -> list[Regime]:
    """Return the list of canonical regimes.

    The five regimes span approximately 60 orders of magnitude in L0
    and 130 orders of magnitude in R0, covering the full range of
    physical systems that the ED PDE can structurally describe.

    Returns
    -------
    list[Regime]
        [quantum, mesoscopic, condensed_matter, gravitational, cosmological]
    """
    return list(_ALL_REGIMES)


def get_regime(name: str) -> Regime:
    """Retrieve a regime by name.

    Parameters
    ----------
    name : str
        One of: "quantum", "mesoscopic", "condensed_matter",
        "gravitational", "cosmological".

    Raises
    ------
    KeyError
        If the name is not recognised.
    """
    for r in _ALL_REGIMES:
        if r.name == name:
            return r
    raise KeyError(
        f"Unknown regime '{name}'.  "
        f"Available: {[r.name for r in _ALL_REGIMES]}"
    )


def regime_table() -> str:
    """Return a formatted Markdown table summarising all regimes."""
    lines = [
        "| Regime | L0 range | R0 range | Examples |",
        "|--------|----------|----------|----------|",
    ]
    for r in _ALL_REGIMES:
        L_lo, L_hi = r.L0_range
        R_lo, R_hi = r.R0_range
        ex = "; ".join(r.physical_examples[:2])
        lines.append(
            f"| {r.label} | {L_lo:.0e} -- {L_hi:.0e} m "
            f"| {R_lo:.0e} -- {R_hi:.0e} kg/m^3 | {ex} |"
        )
    return "\n".join(lines)
