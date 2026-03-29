"""
edsim.phys.quantum_regime — Quantum-like ED parameter regime.

The "quantum-like" regime is defined by three conditions:

1. **High mobility** (M0 large): fast diffusion, strong nonlinear
   mobility gradient M'(rho)|grad rho|^2.
2. **Weak penalty** (P0 small): long-lived transient structure,
   diffusion dominates reaction by ~200x.
3. **Strong participation** (H large): high-Q telegraph oscillation
   of the spatially uniform density component.

These conditions maximise three potentially quantum-like signatures:

- **Anomalous spreading:** nonlinear mobility M(rho) makes the effective
  diffusivity density-dependent, so high-density regions spread more slowly
  than low-density tails, producing non-Gaussian profiles and possibly
  anomalous variance scaling <x^2> ~ t^alpha with alpha != 1.

- **Oscillatory envelope:** the high-Q telegraph oscillation (Q ~ 6)
  modulates the global density, creating an oscillatory envelope over the
  spreading profile — analogous to wave-packet oscillation.

- **Interference-like overlap:** when two bumps overlap, the density-
  dependent mobility creates nonlinear coupling in the overlap region
  that differs from simple linear superposition.

These are STRUCTURAL analogies, not claims of quantum mechanics.  The ED
PDE remains classical, dissipative, and parabolic.
"""

from __future__ import annotations

import math
from dataclasses import dataclass

from ..core.parameters import EDParameters


@dataclass(frozen=True)
class QuantumRegime:
    """Specification of a quantum-like ED parameter regime.

    Attributes
    ----------
    name : str
    parameters : EDParameters
    description : str
    expected_behavior : str
    D_eff : float
        Effective diffusion coefficient D * M_star.
    telegraph_omega : float
        Oscillation frequency of the k=0 mode.
    telegraph_Q : float
        Quality factor of the telegraph oscillation.
    mobility_variation : float
        Fractional mobility reduction at peak: 1 - M(rho_star+A)/M_star.
    ic_amplitude : float
    ic_sigma : float
    """

    name: str
    parameters: EDParameters
    description: str
    expected_behavior: str
    D_eff: float
    telegraph_omega: float
    telegraph_Q: float
    mobility_variation: float
    ic_amplitude: float
    ic_sigma: float


def build_quantum_regime(
    d: int = 2,
    N_per_axis: int = 64,
    M0: float = 4.0,
    P0: float = 0.05,
    H: float = 3.0,
    zeta: float = 0.05,
    A: float = 0.1,
    sigma: float = 0.06,
    T: float = 3.0,
    dt: float = 2e-4,
) -> QuantumRegime:
    """Construct a quantum-like ED regime.

    Parameters
    ----------
    d : int
    N_per_axis : int
    M0 : float
        Mobility prefactor (default 4.0 — 4x canonical).
    P0 : float
        Penalty slope (default 0.05 — very weak).
    H : float
        Participation coupling (default 3.0 — very strong).
    zeta : float
        Damping (default 0.05 — low).
    A : float
        Typical initial amplitude (default 0.1).
    sigma : float
        Typical initial bump width (default 0.06).
    T : float
        Final time (default 3.0).
    dt : float
        Time step (default 2e-4).

    Returns
    -------
    QuantumRegime
    """
    D = 0.3
    tau = 1.0
    beta = 2.0
    rho_star = 0.5
    rho_max = 1.0

    L_tuple = tuple(1.0 for _ in range(d))
    N_tuple = tuple(N_per_axis for _ in range(d))

    params = EDParameters(
        d=d, L=L_tuple, N=N_tuple,
        D=D, H=H, zeta=zeta, tau=tau,
        rho_star=rho_star, rho_max=rho_max,
        M0=M0, beta=beta, P0=P0,
        dt=dt, T=T,
        method="implicit_euler", bc="neumann",
        k_out=max(1, int(T / dt) // 60),
        seed=42,
    )

    M_star = M0 * (rho_max - rho_star) ** beta
    D_eff = D * M_star

    # Telegraph
    gamma = (D * P0 + zeta / tau) / 2.0
    omega0_sq = (D * P0 * zeta + H * P0) / tau
    disc = gamma ** 2 - omega0_sq
    omega_osc = math.sqrt(max(0, -disc))
    Q = omega_osc / (2 * gamma) if gamma > 0 and omega_osc > 0 else 0.0

    # Mobility variation at peak
    M_peak = M0 * (rho_max - (rho_star + A)) ** beta
    mob_var = 1.0 - M_peak / M_star if M_star > 0 else 0.0

    description = (
        f"Quantum-like regime in {d}D: M0={M0}, P0={P0}, H={H}, "
        f"zeta={zeta}.  D_eff={D_eff:.4f}, telegraph omega={omega_osc:.4f} "
        f"(Q={Q:.2f}), mobility variation={mob_var*100:.1f}% at A={A}."
    )

    expected = (
        f"Anomalous spreading from nonlinear mobility (36% variation), "
        f"oscillatory envelope from telegraph coupling (Q={Q:.1f}), "
        f"non-superposition in double-bump overlap region."
    )

    return QuantumRegime(
        name=f"quantum_{d}d",
        parameters=params,
        description=description,
        expected_behavior=expected,
        D_eff=D_eff,
        telegraph_omega=omega_osc,
        telegraph_Q=Q,
        mobility_variation=mob_var,
        ic_amplitude=A,
        ic_sigma=sigma,
    )
