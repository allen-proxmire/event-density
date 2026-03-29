"""
edsim.units.wrapper -- Physical-units wrapper around the ED-SIM-02 solver.

Provides run_physical_simulation(), which:
    1. Accepts physical parameters (lengths in metres, times in seconds, etc.)
    2. Converts them to nondimensional ED parameters.
    3. Runs the solver via run_atlas().
    4. Converts all outputs back to physical units.
    5. Returns a PhysicalTimeSeries with SI quantities.

The solver itself is never modified; all physical units are handled
at the interface layer.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

import numpy as np

from ..core.parameters import EDParameters
from ..experiments.runner import RunConfig, TimeSeries, run_simulation
from ..experiments.scenarios import Scenario
from ..experiments.atlas import run_atlas, summarize_time_series
from .scales import Scales, compute_scales, custom_scales
from .mapping import (
    ed_to_physical_rho,
    ed_to_physical_time,
    ed_to_physical_length,
    ed_to_physical_velocity,
    ed_to_physical_energy,
    ed_to_physical_complexity,
    ed_to_physical_mass,
    ed_to_physical_correlation_length,
)


# ══════════════════════════════════════════════════════════════════════
#  Physical parameter specification
# ══════════════════════════════════════════════════════════════════════

@dataclass(frozen=True)
class PhysicalParameters:
    """Physical-units specification for an ED simulation.

    All quantities in SI.  The wrapper converts these to nondimensional
    EDParameters using the provided characteristic scales.

    Attributes
    ----------
    d : int
        Spatial dimension.
    L_phys : tuple[float, ...]
        Domain size per axis [m].
    N : tuple[int, ...]
        Grid points per axis (dimensionless -- same as nondimensional).
    D_phys : float
        Physical diffusivity [m^2 s^-1].
    H_phys : float
        Participation coupling [m s^-1].
    tau_phys : float
        Participation timescale [s].
    zeta : float
        Participation damping (dimensionless rate ratio).
    rho_star_phys : float
        Equilibrium density [kg m^-3].
    rho_max_phys : float
        Capacity bound [kg m^-3].
    M0 : float
        Mobility prefactor (dimensionless).
    beta : float
        Mobility exponent (dimensionless).
    P0 : float
        Penalty slope (dimensionless).
    dt_phys : float
        Time step [s].
    T_phys : float
        Final time [s].
    method : str
        Integrator: "implicit_euler" or "etdrk4".
    bc : str
        Boundary conditions: "neumann" or "periodic".
    k_out : int
        Snapshot interval (in steps).
    seed : int
        RNG seed.
    """

    d: int = 2
    L_phys: tuple = (1e-6, 1e-6)
    N: tuple = (64, 64)
    D_phys: float = 1e-12
    H_phys: float = 1e-7
    tau_phys: float = 1e-9
    zeta: float = 0.1
    rho_star_phys: float = 500.0
    rho_max_phys: float = 1000.0
    M0: float = 1.0
    beta: float = 2.0
    P0: float = 1.0
    dt_phys: float = 1e-15
    T_phys: float = 1e-9
    method: str = "implicit_euler"
    bc: str = "neumann"
    k_out: int = 100
    seed: int = 42

    def to_ed_parameters(self) -> tuple[EDParameters, Scales]:
        """Convert physical parameters to nondimensional EDParameters + Scales.

        Nondimensionalization:
            x_nd = x_phys / L0     where L0 = L_phys[0]
            t_nd = t_phys / T0     where T0 = L0^2 / D_phys
            rho_nd = rho_phys / R0 where R0 = rho_max_phys

        Returns
        -------
        (EDParameters, Scales)
        """
        L0 = self.L_phys[0]
        R0 = self.rho_max_phys
        T0 = L0 ** 2 / self.D_phys

        # Nondimensional domain
        L_nd = tuple(Li / L0 for Li in self.L_phys)

        # Nondimensional parameters
        D_nd = self.D_phys * T0 / L0 ** 2  # = 1.0 by construction
        H_nd = self.H_phys * T0 / L0
        tau_nd = self.tau_phys / T0
        rho_star_nd = self.rho_star_phys / R0
        rho_max_nd = self.rho_max_phys / R0  # = 1.0 by construction
        dt_nd = self.dt_phys / T0
        T_nd = self.T_phys / T0

        params = EDParameters(
            d=self.d,
            L=L_nd,
            N=self.N,
            D=D_nd,
            H=H_nd,
            zeta=self.zeta,
            tau=tau_nd,
            rho_star=rho_star_nd,
            rho_max=rho_max_nd,
            M0=self.M0,
            beta=self.beta,
            P0=self.P0,
            dt=dt_nd,
            T=T_nd,
            method=self.method,
            bc=self.bc,
            k_out=self.k_out,
            seed=self.seed,
        )

        V0 = L0 / T0
        E0 = R0 * L0 ** self.d

        scales = Scales(
            L0=L0, T0=T0, R0=R0, V0=V0, E0=E0,
            d=self.d, regime="from_physical",
        )

        return params, scales


# ══════════════════════════════════════════════════════════════════════
#  Physical time series
# ══════════════════════════════════════════════════════════════════════

@dataclass
class PhysicalTimeSeries:
    """TimeSeries with all quantities in physical (SI) units.

    Attributes mirror TimeSeries but carry physical dimensions.
    Dimensionless invariants (R_grad, R_pen, R_part, spectral_entropy,
    morphology_fractions, euler_characteristic, betti_numbers) are
    passed through unchanged.
    """

    # Physical quantities
    times_s: list[float] = field(default_factory=list)
    fields_kg_m3: list[np.ndarray] = field(default_factory=list)
    v_m_s: list[float] = field(default_factory=list)
    energy_J: list[float] = field(default_factory=list)
    complexity_phys: list[float] = field(default_factory=list)
    mass_kg: list[float] = field(default_factory=list)
    correlation_length_m: list[float] = field(default_factory=list)

    # Dimensionless (passed through)
    spectral_entropy: list[float] = field(default_factory=list)
    modal_hierarchy: list = field(default_factory=list)
    morphology_fractions: list[dict] = field(default_factory=list)
    R_grad: list[float] = field(default_factory=list)
    R_pen: list[float] = field(default_factory=list)
    R_part: list[float] = field(default_factory=list)
    euler_characteristic: list[int] = field(default_factory=list)
    betti_numbers: list[list[int]] = field(default_factory=list)
    structure_r_m: list[np.ndarray] = field(default_factory=list)
    structure_S2_phys: list[np.ndarray] = field(default_factory=list)

    # Metadata
    scales: Optional[Scales] = None
    params_nd: Optional[EDParameters] = None


def convert_time_series(ts: TimeSeries, scales: Scales) -> PhysicalTimeSeries:
    """Convert a nondimensional TimeSeries to physical units.

    Parameters
    ----------
    ts : TimeSeries
        Nondimensional output from run_simulation().
    scales : Scales
        Characteristic scales for the conversion.

    Returns
    -------
    PhysicalTimeSeries
        Output with all dimensional quantities in SI.
    """
    pts = PhysicalTimeSeries(scales=scales)

    for t_nd in ts.times:
        pts.times_s.append(float(ed_to_physical_time(t_nd, scales)))
    for rho_nd in ts.fields:
        pts.fields_kg_m3.append(ed_to_physical_rho(rho_nd, scales))
    for v_nd in ts.v_history:
        pts.v_m_s.append(float(ed_to_physical_velocity(v_nd, scales)))
    for E_nd in ts.energy:
        pts.energy_J.append(float(ed_to_physical_energy(E_nd, scales)))
    for C_nd in ts.complexity:
        pts.complexity_phys.append(float(ed_to_physical_complexity(C_nd, scales)))
    for M_nd in ts.mass:
        pts.mass_kg.append(float(ed_to_physical_mass(M_nd, scales)))
    for xi_nd in ts.correlation_length:
        pts.correlation_length_m.append(
            float(ed_to_physical_correlation_length(xi_nd, scales))
        )

    # Structure function: convert r bins to physical, S2 to physical
    for r_nd in ts.structure_r:
        pts.structure_r_m.append(ed_to_physical_length(r_nd, scales))
    for S2_nd in ts.structure_S2:
        # S2 ~ <|delta rho|^2> has dimensions R0^2
        pts.structure_S2_phys.append(S2_nd * scales.R0 ** 2)

    # Dimensionless pass-through
    pts.spectral_entropy = list(ts.spectral_entropy)
    pts.modal_hierarchy = list(ts.modal_hierarchy)
    pts.morphology_fractions = list(ts.morphology_fractions)
    pts.R_grad = list(ts.R_grad)
    pts.R_pen = list(ts.R_pen)
    pts.R_part = list(ts.R_part)
    pts.euler_characteristic = list(ts.euler_characteristic)
    pts.betti_numbers = list(ts.betti_numbers)

    return pts


# ══════════════════════════════════════════════════════════════════════
#  High-level runner
# ══════════════════════════════════════════════════════════════════════

def run_physical_simulation(
    physical_params: PhysicalParameters,
    ic_type: str = "cosine",
    ic_kwargs: Optional[dict] = None,
) -> PhysicalTimeSeries:
    """Run an ED simulation in physical units.

    1. Convert PhysicalParameters -> (EDParameters, Scales).
    2. Build RunConfig and call run_simulation().
    3. Convert TimeSeries -> PhysicalTimeSeries.

    Parameters
    ----------
    physical_params : PhysicalParameters
        Simulation specification in SI units.
    ic_type : str
        Initial condition type (passed to generate_ic).
    ic_kwargs : dict, optional
        Additional IC keyword arguments.

    Returns
    -------
    PhysicalTimeSeries
        Full simulation output in physical units.
    """
    params_nd, scales = physical_params.to_ed_parameters()

    config = RunConfig(
        params=params_nd,
        ic_type=ic_type,
        ic_kwargs=ic_kwargs or {"A": 0.03, "Nm": 2},
    )

    ts = run_simulation(config)

    pts = convert_time_series(ts, scales)
    pts.params_nd = params_nd

    return pts


def run_physical_atlas(
    scenario: Scenario,
    scales: Scales,
) -> tuple[EDParameters, PhysicalTimeSeries]:
    """Run a standard scenario and convert to physical units.

    Parameters
    ----------
    scenario : Scenario
        Standard ED-SIM-02 scenario (nondimensional).
    scales : Scales
        Physical scales to apply to the output.

    Returns
    -------
    (EDParameters, PhysicalTimeSeries)
    """
    params, ts = run_atlas(scenario)
    pts = convert_time_series(ts, scales)
    pts.params_nd = params
    return params, pts
