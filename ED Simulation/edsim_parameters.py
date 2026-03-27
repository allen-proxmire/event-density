"""
edsim_parameters.py
====================
Canonical parameter sets and constitutive functions for the ED simulation engine.

Implements the five canonical parameter sets (I–V) from the Simulation Suite §2.2
and the constitutive functions M(rho), P(rho) from the Architectural Canon.

All notation follows Appendix C of the Rigour Paper.
"""

import numpy as np
from dataclasses import dataclass, field
from typing import Optional, Callable


# ---------------------------------------------------------------------------
#  Constitutive functions
# ---------------------------------------------------------------------------

def mobility_default(rho: np.ndarray, rho_max: float, M0: float, beta: float) -> np.ndarray:
    """M(rho) = M0 * (rho_max - rho)^beta.  Principle 4: M(rho_max) = 0."""
    return M0 * np.maximum(rho_max - rho, 0.0) ** beta


def mobility_deriv_default(rho: np.ndarray, rho_max: float, M0: float, beta: float) -> np.ndarray:
    """M'(rho) = -beta * M0 * (rho_max - rho)^(beta - 1)."""
    return -beta * M0 * np.maximum(rho_max - rho, 0.0) ** (beta - 1.0)


def penalty_default(rho: np.ndarray, rho_star: float, P0: float) -> np.ndarray:
    """P(rho) = P0 * (rho - rho*).  Principle 3: unique zero at rho*."""
    return P0 * (rho - rho_star)


def penalty_deriv_default(rho: np.ndarray, rho_star: float, P0: float) -> np.ndarray:
    """P'(rho) = P0 (constant for linear penalty)."""
    return np.full_like(rho, P0)


def density_potential(rho: np.ndarray, rho_star: float, rho_max: float,
                      M0: float, beta: float, P0: float) -> np.ndarray:
    """
    Phi(rho) = integral from rho* to rho of P(r)/M(r) dr.

    For beta=2, P0=M0=1, rho*=0.5, rho_max=1.0:
        Phi(rho) = 0.5/(1 - rho) - ln(0.5/(1 - rho)) - 1

    General case computed via the analytic antiderivative for power-law M and linear P.
    """
    # Default: beta=2, M0=1, P0=1
    if abs(beta - 2.0) < 1e-12 and abs(M0 - 1.0) < 1e-12 and abs(P0 - 1.0) < 1e-12:
        delta = rho_max - rho
        delta_star = rho_max - rho_star
        ratio = delta_star / np.maximum(delta, 1e-15)
        return delta_star / np.maximum(delta, 1e-15) - np.log(ratio) - 1.0
    else:
        # Numerical quadrature fallback for non-default constitutive functions
        from scipy import integrate
        result = np.zeros_like(rho, dtype=float)
        for i, r in enumerate(np.atleast_1d(rho)):
            if abs(r - rho_star) < 1e-15:
                result.flat[i] = 0.0
            else:
                def integrand(s):
                    m = M0 * max(rho_max - s, 1e-15) ** beta
                    p = P0 * (s - rho_star)
                    return p / m
                val, _ = integrate.quad(integrand, rho_star, r)
                result.flat[i] = val
        return result


# ---------------------------------------------------------------------------
#  Parameter dataclass
# ---------------------------------------------------------------------------

@dataclass
class EDParameters:
    """
    Complete parameter specification for the canonical ED system.

    Canonical parameters: D, zeta, tau, rho_star, rho_max
    Constitutive parameters: M0, beta, P0
    Numerical parameters: N, L, dt, T, method
    """
    # --- Canonical parameters ---
    D: float = 0.3              # Direct-channel weight (0, 1)
    zeta: float = 0.1           # Participation damping (0, inf)
    tau: float = 1.0            # Participation time scale (0, inf)
    rho_star: float = 0.5       # Penalty equilibrium
    rho_max: float = 1.0        # Capacity bound

    # --- Constitutive parameters ---
    M0: float = 1.0             # Mobility prefactor
    beta: float = 2.0           # Mobility exponent
    P0: float = 1.0             # Penalty slope

    # --- Numerical parameters ---
    # Stability patch: smaller dt + higher resolution + CN eliminates energy drift.
    N: int = 768                # Interior grid points (Method A) or modes (Method B)
    L: float = 1.0              # Domain length
    # Second-stage stability patch: dt reduced ×4 to eliminate late-time drift.
    dt: float = 3.125e-5         # Time step
    T: float = 50.0             # Final time
    method: str = "crank_nicolson"  # "implicit_euler", "crank_nicolson", "etdrk4"
    k_out: int = 50             # Output every k_out steps

    # --- Derived quantities (computed in __post_init__) ---
    H: float = field(init=False)
    h: float = field(init=False)
    N_grid: int = field(init=False)
    M_star: float = field(init=False)
    M_star_prime: float = field(init=False)
    P_star_prime: float = field(init=False)
    Delta: float = field(init=False)
    gamma_0: float = field(init=False)
    D_0: float = field(init=False)       # Discriminant D_0
    omega: float = field(init=False)      # Oscillation frequency (if D_0 < 0)

    def __post_init__(self):
        self._validate()
        self._compute_derived()

    def _validate(self):
        """Level 1 + Level 2 validation from Suite §2.2."""
        # Level 1: type and range
        assert 0.0 < self.D < 1.0, f"D = {self.D} not in (0, 1)"
        assert self.zeta > 0.0, f"zeta = {self.zeta} not positive"
        assert self.tau > 0.0, f"tau = {self.tau} not positive"
        assert 0.0 < self.rho_star < self.rho_max, \
            f"rho_star = {self.rho_star} not in (0, rho_max={self.rho_max})"
        assert self.rho_max > 0.0, f"rho_max = {self.rho_max} not positive"
        assert self.M0 > 0.0, f"M0 = {self.M0} not positive"
        assert self.beta > 1.0, f"beta = {self.beta} not > 1"
        assert self.P0 > 0.0, f"P0 = {self.P0} not positive"
        assert self.N >= 16, f"N = {self.N} too small"
        assert self.L > 0.0, f"L = {self.L} not positive"
        assert self.dt > 0.0, f"dt = {self.dt} not positive"
        assert self.T > 0.0, f"T = {self.T} not positive"

        # Level 2: constitutive consistency
        # M(rho_star) > 0
        m_star = self.M0 * (self.rho_max - self.rho_star) ** self.beta
        assert m_star > 0.0, f"M(rho*) = {m_star} not positive"

        # P(rho_star) = 0 (by construction for linear penalty)
        p_star = self.P0 * (self.rho_star - self.rho_star)
        assert abs(p_star) < 1e-15, f"P(rho*) = {p_star} not zero"

        # P'(rho_star) > 0 (Principle 3: strict penalty monotonicity)
        assert self.P0 > 0.0, f"P'(rho*) = {self.P0} not positive"

    def _compute_derived(self):
        """Compute all derived quantities at initialization."""
        self.H = 1.0 - self.D
        self.h = self.L / (self.N + 1)
        self.N_grid = self.N + 2  # Including boundary points

        # Constitutive values at equilibrium
        self.M_star = self.M0 * (self.rho_max - self.rho_star) ** self.beta
        self.M_star_prime = -self.beta * self.M0 * (self.rho_max - self.rho_star) ** (self.beta - 1.0)
        self.P_star_prime = self.P0

        # Damping and spectral quantities
        self.Delta = self.D + 2.0 * self.zeta  # Not the discriminant, just shorthand
        self.gamma_0 = 0.5 * (self.D * self.P_star_prime + self.zeta / self.tau)
        self.D_0 = (self.D * self.P_star_prime - self.zeta / self.tau) ** 2 \
                   - 4.0 * self.H * self.P_star_prime / self.tau

        if self.D_0 < 0.0:
            self.omega = 0.5 * np.sqrt(abs(self.D_0))
        else:
            self.omega = 0.0

    # --- Constitutive function evaluators ---

    def M(self, rho: np.ndarray) -> np.ndarray:
        """Evaluate mobility M(rho)."""
        return mobility_default(rho, self.rho_max, self.M0, self.beta)

    def M_prime(self, rho: np.ndarray) -> np.ndarray:
        """Evaluate mobility derivative M'(rho)."""
        return mobility_deriv_default(rho, self.rho_max, self.M0, self.beta)

    def P(self, rho: np.ndarray) -> np.ndarray:
        """Evaluate penalty P(rho)."""
        return penalty_default(rho, self.rho_star, self.P0)

    def P_prime(self, rho: np.ndarray) -> np.ndarray:
        """Evaluate penalty derivative P'(rho)."""
        return penalty_deriv_default(rho, self.rho_star, self.P0)

    def Phi(self, rho: np.ndarray) -> np.ndarray:
        """Evaluate density potential Phi(rho) for the energy functional."""
        return density_potential(rho, self.rho_star, self.rho_max,
                                self.M0, self.beta, self.P0)

    # --- Eigenvalue computations ---

    def mu(self, k: int) -> float:
        """Neumann eigenvalue mu_k = (k*pi/L)^2."""
        return (k * np.pi / self.L) ** 2

    def alpha(self, k: int) -> float:
        """Modal constant alpha_k = M* * mu_k + P*'."""
        return self.M_star * self.mu(k) + self.P_star_prime

    def modal_decay_rate(self, k: int) -> float:
        """Linear decay rate D * alpha_k for mode k."""
        return self.D * self.alpha(k)

    def eigenvalues_homogeneous(self):
        """
        Eigenvalues of the linearized homogeneous (k=0) system.

        Characteristic polynomial: lambda^2 + 2*gamma_0*lambda + (D*P*'*zeta/tau + H*P*'/tau) = 0

        Returns (lambda_plus, lambda_minus) as complex numbers.
        """
        a = 1.0
        b = 2.0 * self.gamma_0
        c = self.D * self.P_star_prime * self.zeta / self.tau \
            + self.H * self.P_star_prime / self.tau
        disc = b ** 2 - 4.0 * a * c
        sqrt_disc = np.sqrt(complex(disc))
        lam_plus = (-b + sqrt_disc) / (2.0 * a)
        lam_minus = (-b - sqrt_disc) / (2.0 * a)
        return lam_plus, lam_minus

    def is_oscillatory(self) -> bool:
        """True if the homogeneous mode is oscillatory (D_0 < 0)."""
        return self.D_0 < 0.0

    def regime_label(self) -> str:
        """Classify the regime: 'spiral', 'monotonic', or 'critical'."""
        if abs(self.D_0) < 1e-10:
            return "critical"
        elif self.D_0 < 0.0:
            return "spiral"
        else:
            return "monotonic"

    def spectral_gap(self) -> float:
        """
        Spectral gap: D * (alpha_1 - alpha_0) = D * M* * mu_1.

        The gap between the slowest inhomogeneous mode and the homogeneous mode.
        """
        return self.D * self.M_star * self.mu(1)

    # --- Summary ---

    def summary(self) -> str:
        """Human-readable summary of parameters and derived quantities."""
        lines = [
            "=" * 60,
            "ED Canonical Parameters",
            "=" * 60,
            f"  D      = {self.D}",
            f"  H      = {self.H}",
            f"  zeta   = {self.zeta}",
            f"  tau    = {self.tau}",
            f"  rho*   = {self.rho_star}",
            f"  rho_max= {self.rho_max}",
            "",
            "Constitutive:",
            f"  M0     = {self.M0}",
            f"  beta   = {self.beta}",
            f"  P0     = {self.P0}",
            f"  M*     = {self.M_star:.6f}",
            f"  M*'    = {self.M_star_prime:.6f}",
            f"  P*'    = {self.P_star_prime:.6f}",
            "",
            "Spectral:",
            f"  gamma_0= {self.gamma_0:.6f}",
            f"  D_0    = {self.D_0:.6f}",
            f"  omega  = {self.omega:.6f}",
            f"  regime = {self.regime_label()}",
            f"  gap    = {self.spectral_gap():.6f}",
            "",
            "Numerical:",
            f"  N      = {self.N}",
            f"  L      = {self.L}",
            f"  h      = {self.h:.6e}",
            f"  dt     = {self.dt:.6e}",
            f"  T      = {self.T}",
            f"  method = {self.method}",
            f"  k_out  = {self.k_out}",
            "=" * 60,
        ]
        return "\n".join(lines)


# ---------------------------------------------------------------------------
#  Canonical parameter sets I–V (Simulation Suite §2.2, Atlas §10.2)
# ---------------------------------------------------------------------------

def parameter_set_I(**overrides) -> EDParameters:
    """Set I — Deep Oscillatory. D=0.3, zeta=0.1, tau=1.0."""
    defaults = dict(D=0.3, zeta=0.1, tau=1.0, rho_star=0.5, rho_max=1.0,
                    M0=1.0, beta=2.0, P0=1.0)
    defaults.update(overrides)
    return EDParameters(**defaults)


def parameter_set_II(**overrides) -> EDParameters:
    """Set II — Moderate Oscillatory. D=0.6, zeta=0.5, tau=1.0."""
    defaults = dict(D=0.6, zeta=0.5, tau=1.0, rho_star=0.5, rho_max=1.0,
                    M0=1.0, beta=2.0, P0=1.0)
    defaults.update(overrides)
    return EDParameters(**defaults)


def parameter_set_III(**overrides) -> EDParameters:
    """Set III — Near-Critical. D=0.8, zeta=1.8, tau=1.0."""
    defaults = dict(D=0.8, zeta=1.8, tau=1.0, rho_star=0.5, rho_max=1.0,
                    M0=1.0, beta=2.0, P0=1.0)
    defaults.update(overrides)
    return EDParameters(**defaults)


def parameter_set_IV(**overrides) -> EDParameters:
    """Set IV — Deep Monotonic. D=0.9, zeta=5.0, tau=1.0."""
    defaults = dict(D=0.9, zeta=5.0, tau=1.0, rho_star=0.5, rho_max=1.0,
                    M0=1.0, beta=2.0, P0=1.0)
    defaults.update(overrides)
    return EDParameters(**defaults)


def parameter_set_V(**overrides) -> EDParameters:
    """Set V — High Participation Coupling. D=0.2, zeta=0.3, tau=0.5."""
    defaults = dict(D=0.2, zeta=0.3, tau=0.5, rho_star=0.5, rho_max=1.0,
                    M0=1.0, beta=2.0, P0=1.0)
    defaults.update(overrides)
    return EDParameters(**defaults)


ALL_PARAMETER_SETS = {
    "I":   parameter_set_I,
    "II":  parameter_set_II,
    "III": parameter_set_III,
    "IV":  parameter_set_IV,
    "V":   parameter_set_V,
}


def load_parameter_set(name: str, **overrides) -> EDParameters:
    """Load a canonical parameter set by name ('I' through 'V')."""
    if name not in ALL_PARAMETER_SETS:
        raise ValueError(f"Unknown parameter set '{name}'. Choose from {list(ALL_PARAMETER_SETS.keys())}")
    return ALL_PARAMETER_SETS[name](**overrides)
