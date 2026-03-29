"""
edsim.phys.wave_regime — Wave/telegraph-like ED parameter regime.

The canonical ED PDE is parabolic (diffusive) and does NOT support true
wave propagation.  However, the coupled (rho, v) system can exhibit
*damped temporal oscillations* for the spatially uniform (k=0) mode.

Linearising about (rho_star, 0):

    dA_0/dt = -D P0 A_0 + H v
    dv/dt   = (-P0 A_0 - zeta v) / tau

This is a second-order telegraph-type ODE:

    A_0'' + 2 gamma A_0' + omega_0^2 A_0 = 0

with  gamma   = (D P0 + zeta/tau) / 2
and   omega_0^2 = (D P0 zeta + H P0) / tau.

The system is **underdamped** (oscillatory) when omega_0^2 > gamma^2,
which requires sufficiently strong participation coupling H.

For spatial modes k >= 1, the Neumann average of cos(k pi x / L)
vanishes, so F_bar does not couple to individual modes in the linear
regime.  Each k-mode decays exponentially at rate
sigma_k = D (M_star mu_k + P0) without oscillation.

The "wave regime" therefore maximises oscillatory behaviour by:
    - using strong H (participation coupling)
    - using moderate P0 (penalty drives the oscillation)
    - using small zeta/tau (low damping)

The resulting dynamics resemble a *telegraph equation* for the uniform
component, overlaid on diffusive decay of spatial modes.
"""

from __future__ import annotations

import math
from dataclasses import dataclass

from ..core.parameters import EDParameters


@dataclass(frozen=True)
class WaveRegime:
    """Specification of an ED regime that exhibits oscillatory behaviour.

    Attributes
    ----------
    name : str
        Human-readable regime label.
    parameters : EDParameters
        ED parameters tuned for the wave/telegraph limit.
    description : str
        Narrative description.
    expected_behavior : str
        Summary of expected dynamical behaviour.
    gamma : float
        Damping rate of the telegraph system.
    omega0 : float
        Natural frequency sqrt(omega_0^2).
    omega_osc : float
        Oscillation frequency sqrt(omega_0^2 - gamma^2).
        Zero if overdamped.
    period : float
        Oscillation period 2 pi / omega_osc (inf if overdamped).
    quality_factor : float
        Q = omega_osc / (2 gamma).
    """

    name: str
    parameters: EDParameters
    description: str
    expected_behavior: str
    gamma: float
    omega0: float
    omega_osc: float
    period: float
    quality_factor: float


def build_wave_regime(
    d: int = 2,
    N_per_axis: int = 64,
    H: float = 2.0,
    zeta: float = 0.05,
    tau: float = 1.0,
    P0: float = 1.0,
    T: float = 20.0,
    dt: float = 1e-3,
) -> WaveRegime:
    """Construct a wave/telegraph-like ED regime.

    The regime uses strong participation coupling H and low damping zeta
    to maximise the quality factor Q of the oscillatory mode.

    Parameters
    ----------
    d : int
        Spatial dimension (default 2).
    N_per_axis : int
        Grid points per axis (default 64).
    H : float
        Participation coupling (default 2.0 — much stronger than canonical 0.15).
    zeta : float
        Damping coefficient (default 0.05 — lower than canonical 0.1).
    tau : float
        Participation timescale (default 1.0).
    P0 : float
        Penalty slope (default 1.0).
    T : float
        Final time (default 20.0 — long enough for several oscillation periods).
    dt : float
        Time step (default 1e-3).

    Returns
    -------
    WaveRegime
        Complete regime specification.
    """
    D = 0.3
    L_tuple = tuple(1.0 for _ in range(d))
    N_tuple = tuple(N_per_axis for _ in range(d))

    params = EDParameters(
        d=d,
        L=L_tuple,
        N=N_tuple,
        D=D,
        H=H,
        zeta=zeta,
        tau=tau,
        rho_star=0.5,
        rho_max=1.0,
        M0=1.0,
        beta=2.0,
        P0=P0,
        dt=dt,
        T=T,
        method="implicit_euler",
        bc="neumann",
        k_out=max(1, int(T / dt) // 200),  # ~200 snapshots
        seed=42,
    )

    # Telegraph coefficients
    gamma = (D * P0 + zeta / tau) / 2.0
    omega0_sq = (D * P0 * zeta + H * P0) / tau
    omega0 = math.sqrt(omega0_sq)

    disc = gamma ** 2 - omega0_sq
    if disc < 0:
        omega_osc = math.sqrt(-disc)
        period = 2.0 * math.pi / omega_osc
        Q = omega_osc / (2.0 * gamma)
    else:
        omega_osc = 0.0
        period = float("inf")
        Q = 0.0

    if omega_osc > 0:
        dyn_desc = (
            f"Underdamped telegraph oscillation: "
            f"omega_osc = {omega_osc:.4f}, period = {period:.2f}, "
            f"Q = {Q:.2f}."
        )
        expect = (
            f"The spatially uniform component of rho oscillates around "
            f"rho_star with period ~{period:.1f} and decays with "
            f"e-folding time ~{1.0/gamma:.1f}.  "
            f"Spatial modes k >= 1 decay exponentially without oscillation."
        )
    else:
        dyn_desc = "Overdamped: no oscillation possible."
        expect = "All modes decay exponentially."

    description = (
        f"Wave/telegraph regime in {d}D: H={H}, zeta={zeta}, tau={tau}, "
        f"P0={P0}, D={D}.  {dyn_desc}"
    )

    return WaveRegime(
        name=f"wave_{d}d",
        parameters=params,
        description=description,
        expected_behavior=expect,
        gamma=gamma,
        omega0=omega0,
        omega_osc=omega_osc,
        period=period,
        quality_factor=Q,
    )
