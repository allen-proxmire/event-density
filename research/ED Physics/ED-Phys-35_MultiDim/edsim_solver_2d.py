"""
edsim_solver_2d.py
==================
2D numerical core for the canonical Event Density PDE system.

Implements:
  - Spatial operators: Laplacian, gradient squared, F[rho]
      * Finite-difference (FD) with Neumann or periodic BCs
      * Spectral (2D DCT-I) with Neumann BCs
  - Time steppers:
      * Primary:   ETD-RK4 (spectral, Cox-Matthews scheme)
      * Secondary:  Crank-Nicolson with ADI splitting (FD)
  - State management: initialization, bounds enforcement, diagnostics

Follows the architecture of edsim_core.py (1D) and the specification in
ED-Phys-35_Architecture.md.

All notation follows Appendix C of the Rigour Paper and the Simulation Suite.
"""

import numpy as np
from dataclasses import dataclass, field
from typing import Optional, Callable, Dict, List, Tuple
from scipy.fft import dctn, idctn
from scipy.linalg import solve_banded


# ===================================================================
#  CONSTITUTIVE FUNCTIONS (dimension-independent, matching edsim_parameters.py)
# ===================================================================

def _mobility(rho: np.ndarray, rho_max: float, M0: float, beta: float) -> np.ndarray:
    """M(rho) = M0 * (rho_max - rho)^beta.  Principle 4: M(rho_max) = 0."""
    return M0 * np.maximum(rho_max - rho, 0.0) ** beta


def _mobility_deriv(rho: np.ndarray, rho_max: float, M0: float, beta: float) -> np.ndarray:
    """M'(rho) = -beta * M0 * (rho_max - rho)^(beta - 1)."""
    return -beta * M0 * np.maximum(rho_max - rho, 0.0) ** (beta - 1.0)


def _penalty(rho: np.ndarray, rho_star: float, P0: float) -> np.ndarray:
    """P(rho) = P0 * (rho - rho*).  Principle 3: unique zero at rho*."""
    return P0 * (rho - rho_star)


# ===================================================================
#  PARAMETER DATACLASS
# ===================================================================

@dataclass
class EDParameters2D:
    """
    Complete parameter specification for the 2D canonical ED system.

    Physics parameters match edsim_parameters.EDParameters.
    Grid parameters are extended to two spatial dimensions.
    """
    # --- Canonical physics parameters ---
    D: float = 0.3
    zeta: float = 0.1
    tau: float = 1.0
    rho_star: float = 0.5
    rho_max: float = 1.0

    # --- Constitutive parameters ---
    M0: float = 1.0
    beta: float = 2.0
    P0: float = 1.0

    # --- 2D grid parameters ---
    Nx: int = 128           # Grid points in x (including boundary for FD)
    Ny: int = 128           # Grid points in y (including boundary for FD)
    Lx: float = 1.0         # Domain length in x
    Ly: float = 1.0         # Domain length in y
    dt: float = 1e-4         # Time step
    T: float = 10.0          # Final time
    method: str = "etdrk4"   # "etdrk4", "crank_nicolson"
    boundary: str = "neumann" # "neumann", "periodic"
    k_out: int = 50          # Output every k_out steps

    # --- Derived quantities (computed in __post_init__) ---
    H: float = field(init=False)
    hx: float = field(init=False)
    hy: float = field(init=False)
    M_star: float = field(init=False)
    M_star_prime: float = field(init=False)
    P_star_prime: float = field(init=False)

    def __post_init__(self):
        self._validate()
        self._compute_derived()

    def _validate(self):
        assert 0.0 < self.D < 1.0, f"D = {self.D} not in (0, 1)"
        assert self.zeta > 0.0
        assert self.tau > 0.0
        assert 0.0 < self.rho_star < self.rho_max
        assert self.rho_max > 0.0
        assert self.M0 > 0.0
        assert self.beta > 1.0
        assert self.P0 > 0.0
        assert self.Nx >= 8
        assert self.Ny >= 8
        assert self.Lx > 0.0
        assert self.Ly > 0.0
        assert self.dt > 0.0
        assert self.T > 0.0
        assert self.boundary in ("neumann", "periodic")
        assert self.method in ("etdrk4", "crank_nicolson")

    def _compute_derived(self):
        self.H = 1.0 - self.D
        self.hx = self.Lx / (self.Nx - 1)
        self.hy = self.Ly / (self.Ny - 1)
        self.M_star = self.M0 * (self.rho_max - self.rho_star) ** self.beta
        self.M_star_prime = -self.beta * self.M0 * (self.rho_max - self.rho_star) ** (self.beta - 1.0)
        self.P_star_prime = self.P0

    def M(self, rho: np.ndarray) -> np.ndarray:
        return _mobility(rho, self.rho_max, self.M0, self.beta)

    def M_prime(self, rho: np.ndarray) -> np.ndarray:
        return _mobility_deriv(rho, self.rho_max, self.M0, self.beta)

    def P(self, rho: np.ndarray) -> np.ndarray:
        return _penalty(rho, self.rho_star, self.P0)

    def summary(self) -> str:
        lines = [
            "=" * 60,
            "ED 2D Canonical Parameters",
            "=" * 60,
            f"  D={self.D}, H={self.H}, zeta={self.zeta}, tau={self.tau}",
            f"  rho*={self.rho_star}, rho_max={self.rho_max}",
            f"  M0={self.M0}, beta={self.beta}, P0={self.P0}",
            f"  M*={self.M_star:.6f}, P*'={self.P_star_prime:.6f}",
            f"  Grid: {self.Nx}x{self.Ny}, Lx={self.Lx}, Ly={self.Ly}",
            f"  hx={self.hx:.6e}, hy={self.hy:.6e}",
            f"  dt={self.dt:.6e}, T={self.T}, method={self.method}",
            f"  boundary={self.boundary}",
            "=" * 60,
        ]
        return "\n".join(lines)


# ===================================================================
#  GRID CONSTRUCTION
# ===================================================================

def make_grid_2d(params: EDParameters2D) -> Tuple[np.ndarray, np.ndarray]:
    """
    Create the 2D spatial grid.

    Returns (X, Y) meshgrid arrays, each of shape (Nx, Ny).
    Grid includes boundary points: x in [0, Lx], y in [0, Ly].
    """
    x = np.linspace(0.0, params.Lx, params.Nx)
    y = np.linspace(0.0, params.Ly, params.Ny)
    return np.meshgrid(x, y, indexing='ij')


# ===================================================================
#  SPATIAL OPERATORS (Finite Difference)
# ===================================================================

def _pad_2d(rho: np.ndarray, boundary: str) -> np.ndarray:
    """Pad 2D array with one ghost cell on each side per boundary type."""
    if boundary == "neumann":
        return np.pad(rho, 1, mode='reflect')
    elif boundary == "periodic":
        return np.pad(rho, 1, mode='wrap')
    else:
        raise ValueError(f"Unknown boundary: {boundary}")


def laplacian_fd_2d(rho: np.ndarray, hx: float, hy: float,
                    boundary: str = "neumann") -> np.ndarray:
    """
    Discrete Laplacian in 2D.

    nabla^2 rho_{i,j} = (rho_{i+1,j} + rho_{i-1,j} - 2*rho_{i,j}) / hx^2
                       + (rho_{i,j+1} + rho_{i,j-1} - 2*rho_{i,j}) / hy^2

    Boundary conditions handled via ghost-cell padding.
    """
    p = _pad_2d(rho, boundary)
    hx2 = hx * hx
    hy2 = hy * hy
    lap = ((p[2:, 1:-1] + p[:-2, 1:-1] - 2.0 * p[1:-1, 1:-1]) / hx2
         + (p[1:-1, 2:] + p[1:-1, :-2] - 2.0 * p[1:-1, 1:-1]) / hy2)
    return lap


def grad_squared_fd_2d(rho: np.ndarray, hx: float, hy: float,
                       boundary: str = "neumann") -> np.ndarray:
    """
    Discrete |grad rho|^2 in 2D using central differences.

    |nabla rho|^2_{i,j} = ((rho_{i+1,j} - rho_{i-1,j}) / (2*hx))^2
                         + ((rho_{i,j+1} - rho_{i,j-1}) / (2*hy))^2
    """
    p = _pad_2d(rho, boundary)
    gx = (p[2:, 1:-1] - p[:-2, 1:-1]) / (2.0 * hx)
    gy = (p[1:-1, 2:] - p[1:-1, :-2]) / (2.0 * hy)
    return gx * gx + gy * gy


def compute_operators_2d(rho: np.ndarray, params: EDParameters2D) -> Dict[str, np.ndarray]:
    """
    Compute all spatial operators at the current state.

    Returns dict with keys: 'lap', 'grad_sq', 'M', 'Mp', 'P_val', 'F'.
    """
    lap = laplacian_fd_2d(rho, params.hx, params.hy, params.boundary)
    gs = grad_squared_fd_2d(rho, params.hx, params.hy, params.boundary)
    M_vals = params.M(rho)
    Mp_vals = params.M_prime(rho)
    P_vals = params.P(rho)
    F = M_vals * lap + Mp_vals * gs - P_vals
    return {
        'lap': lap, 'grad_sq': gs, 'M': M_vals, 'Mp': Mp_vals,
        'P_val': P_vals, 'F': F,
    }


def operator_F_fd_2d(rho: np.ndarray, params: EDParameters2D) -> np.ndarray:
    """
    Evaluate the nonlinear density operator F[rho] on the 2D FD grid.

    F[rho] = M(rho) * Lap(rho) + M'(rho) * |grad rho|^2 - P(rho)
    """
    return compute_operators_2d(rho, params)['F']


def spatial_avg_2d(f: np.ndarray, hx: float, hy: float) -> float:
    """
    2D spatial average using the trapezoidal rule.

    For a grid of Nx x Ny points on [0, Lx] x [0, Ly]:
    avg = (1 / (Lx * Ly)) * integral f dA
    """
    Nx, Ny = f.shape
    Lx = hx * (Nx - 1)
    Ly = hy * (Ny - 1)
    # Trapezoidal weights: 1/2 at edges, 1 at interior
    wx = np.ones(Nx)
    wx[0] = 0.5
    wx[-1] = 0.5
    wy = np.ones(Ny)
    wy[0] = 0.5
    wy[-1] = 0.5
    return hx * hy * np.einsum('i,ij,j->', wx, f, wy) / (Lx * Ly)


# ===================================================================
#  PARTICIPATION VARIABLE UPDATE (exact exponential integrator)
# ===================================================================

def advance_v(v: float, F_bar: float, zeta: float, tau: float, dt: float) -> float:
    """
    Advance the participation variable v by one time step.

    v^{n+1} = exp(-zeta*dt/tau) * v^n + (1 - exp(-zeta*dt/tau)) * (tau/zeta) * F_bar
    """
    decay = np.exp(-zeta * dt / tau)
    return decay * v + (1.0 - decay) * (tau / zeta) * F_bar


def _advance_v_dt(v: float, F_bar: float, zeta: float, tau: float, dt: float) -> float:
    """Advance v with a custom time step (convenience alias)."""
    return advance_v(v, F_bar, zeta, tau, dt)


# ===================================================================
#  POSITIVITY & CAPACITY ENFORCEMENT
# ===================================================================

def enforce_bounds_2d(rho: np.ndarray, rho_max: float,
                      eps_pos: float = 1e-12, eps_cap: float = 1e-12):
    """
    Project rho into the admissible region (eps_pos, rho_max - eps_cap).

    Returns (rho_clamped, n_pos_violations, n_cap_violations).
    """
    n_pos = int(np.sum(rho <= eps_pos))
    n_cap = int(np.sum(rho >= rho_max - eps_cap))
    rho_out = np.clip(rho, eps_pos, rho_max - eps_cap)
    return rho_out, n_pos, n_cap


# ===================================================================
#  ENERGY FUNCTIONAL
# ===================================================================

def energy_2d(rho: np.ndarray, v: float, params: EDParameters2D) -> Dict[str, float]:
    """
    Compute the energy functional E[rho, v].

    E = integral Phi(rho) dA + (tau * H / 2) * v^2

    Uses trapezoidal rule for the 2D integral.
    """
    # Density potential Phi(rho) = integral_rho* ^rho P(s)/M(s) ds
    # For canonical parameters (beta=2, M0=P0=1, rho_max=1):
    #   Phi(rho) = (rho_max - rho_star)/(rho_max - rho) - ln((rho_max - rho_star)/(rho_max - rho)) - 1
    delta = np.maximum(params.rho_max - rho, 1e-15)
    delta_star = params.rho_max - params.rho_star
    if (abs(params.beta - 2.0) < 1e-12 and abs(params.M0 - 1.0) < 1e-12
            and abs(params.P0 - 1.0) < 1e-12):
        ratio = delta_star / delta
        Phi_vals = ratio - np.log(ratio) - 1.0
    else:
        # General case: numerical quadrature (slow, for non-default constitutive functions)
        from scipy import integrate
        Phi_vals = np.zeros_like(rho)
        for idx in np.ndindex(rho.shape):
            r = rho[idx]
            if abs(r - params.rho_star) < 1e-15:
                continue
            def integrand(s):
                m = params.M0 * max(params.rho_max - s, 1e-15) ** params.beta
                p = params.P0 * (s - params.rho_star)
                return p / m
            Phi_vals[idx], _ = integrate.quad(integrand, params.rho_star, r)

    Lx = params.hx * (params.Nx - 1)
    Ly = params.hy * (params.Ny - 1)
    E_pot = spatial_avg_2d(Phi_vals, params.hx, params.hy) * Lx * Ly
    E_kin = 0.5 * params.tau * params.H * v ** 2
    return {"total": E_pot + E_kin, "potential": E_pot, "kinetic": E_kin}


# ===================================================================
#  TOTAL MASS
# ===================================================================

def total_mass_2d(rho: np.ndarray, hx: float, hy: float) -> float:
    """Total mass: integral of rho dA (trapezoidal rule)."""
    Nx, Ny = rho.shape
    wx = np.ones(Nx); wx[0] = 0.5; wx[-1] = 0.5
    wy = np.ones(Ny); wy[0] = 0.5; wy[-1] = 0.5
    return hx * hy * np.einsum('i,ij,j->', wx, rho, wy)


# ===================================================================
#  ETD-RK4 PHI FUNCTIONS
# ===================================================================

def _phi_functions(z: np.ndarray):
    """
    Compute ETD weight functions phi_1, phi_2, phi_3.

    phi_1(z) = (exp(z) - 1) / z
    phi_2(z) = (exp(z) - 1 - z) / z^2
    phi_3(z) = (exp(z) - 1 - z - z^2/2) / z^3

    Uses Taylor expansion for small |z| to avoid catastrophic cancellation.
    """
    ez = np.exp(z)
    small = np.abs(z) < 1e-4
    # Use safe division: replace z=0 with 1.0 to avoid warnings,
    # then overwrite those entries with the Taylor expansion.
    z_safe = np.where(small, 1.0, z)
    phi1 = np.where(small,
                    1.0 + z / 2.0 + z**2 / 6.0 + z**3 / 24.0,
                    (ez - 1.0) / z_safe)
    phi2 = np.where(small,
                    0.5 + z / 6.0 + z**2 / 24.0 + z**3 / 120.0,
                    (ez - 1.0 - z) / z_safe**2)
    phi3 = np.where(small,
                    1.0/6.0 + z / 24.0 + z**2 / 120.0 + z**3 / 720.0,
                    (ez - 1.0 - z - 0.5 * z**2) / z_safe**3)
    return phi1, phi2, phi3


# ===================================================================
#  SPECTRAL STATE (2D DCT-I for Neumann BCs)
# ===================================================================

class SpectralState2D:
    """
    State container for the 2D spectral (ETD-RK4) solver.

    Uses 2D DCT-I (Neumann boundary conditions).
    Eigenvalues: mu_{kx,ky} = (kx*pi/Lx)^2 + (ky*pi/Ly)^2.
    De-aliasing via the 3/2-rule in each axis.
    """

    def __init__(self, params: EDParameters2D):
        self.params = params
        self.Kx = params.Nx    # Spectral modes in x
        self.Ky = params.Ny    # Spectral modes in y
        self.Lx = params.Lx
        self.Ly = params.Ly

        # De-aliased physical grid sizes (3/2 rule per axis)
        self.Npx = int(np.floor(1.5 * self.Kx))
        self.Npy = int(np.floor(1.5 * self.Ky))
        # Ensure odd for symmetry (DCT-I grid)
        if self.Npx < self.Kx:
            self.Npx = self.Kx
        if self.Npy < self.Ky:
            self.Npy = self.Ky

        self.hx_phys = self.Lx / (self.Npx - 1)
        self.hy_phys = self.Ly / (self.Npy - 1)

        # 2D Neumann eigenvalues: mu_{kx,ky} = (kx*pi/Lx)^2 + (ky*pi/Ly)^2
        kx = np.arange(self.Kx)
        ky = np.arange(self.Ky)
        mu_x = (kx * np.pi / self.Lx) ** 2  # shape (Kx,)
        mu_y = (ky * np.pi / self.Ly) ** 2  # shape (Ky,)
        self.mu = mu_x[:, np.newaxis] + mu_y[np.newaxis, :]  # shape (Kx, Ky)

        # Linear decay constants: c_{kx,ky} = -D * M* * mu_{kx,ky}
        self.c = -params.D * params.M_star * self.mu  # shape (Kx, Ky)

        # Precompute ETD weights
        dt = params.dt
        z_full = self.c * dt
        z_half = self.c * dt / 2.0

        self.exp_full = np.exp(z_full)
        self.exp_half = np.exp(z_half)

        self.phi1_full, self.phi2_full, self.phi3_full = _phi_functions(z_full)
        self.phi1_half, _, _ = _phi_functions(z_half)

    def to_spectral(self, u_phys: np.ndarray) -> np.ndarray:
        """
        Transform physical-space perturbation u = rho - rho* to spectral coefficients.

        Uses 2D DCT-I with normalization convention:
          a_{kx,ky} = DCT2D(u) / ((Npx-1)*(Npy-1))
          with boundary modes halved per axis.
        """
        Npx, Npy = u_phys.shape
        raw = dctn(u_phys, type=1)
        norm = (Npx - 1) * (Npy - 1)
        coeffs = raw / norm
        # Halve boundary modes per axis
        coeffs[0, :] /= 2.0
        if Npx > 1:
            coeffs[-1, :] /= 2.0
        coeffs[:, 0] /= 2.0
        if Npy > 1:
            coeffs[:, -1] /= 2.0
        return coeffs[:self.Kx, :self.Ky]

    def to_physical(self, u_hat: np.ndarray,
                    Npx_out: Optional[int] = None,
                    Npy_out: Optional[int] = None) -> np.ndarray:
        """
        Transform spectral coefficients to physical space.

        Inverse of to_spectral (exact roundtrip when no truncation).
        """
        if Npx_out is None:
            Npx_out = self.Npx
        if Npy_out is None:
            Npy_out = self.Npy

        Kx_in, Ky_in = u_hat.shape

        # Zero-pad to output size
        padded = np.zeros((Npx_out, Npy_out))
        padded[:Kx_in, :Ky_in] = u_hat

        # Undo boundary halving
        padded[0, :] *= 2.0
        if Kx_in == Npx_out:
            padded[-1, :] *= 2.0
        padded[:, 0] *= 2.0
        if Ky_in == Npy_out:
            padded[:, -1] *= 2.0

        # Inverse DCT-I with normalization
        norm = (Npx_out - 1) * (Npy_out - 1)
        return idctn(padded * norm, type=1)

    def nonlinear_rhs(self, u_hat: np.ndarray, v: float) -> np.ndarray:
        """
        Compute the nonlinear residual N_hat in spectral space.

        The full RHS of the perturbation equation is:
          du_hat/dt = c * u_hat + D * N_hat + H * v * delta_{k=0}

        where ETD handles c * u_hat. This function returns:
          D * N_hat + H * v * delta_{k=0}

        with N = [M(rho) - M*] * Lap(u) + M'(rho) * |grad u|^2 - [P(rho) - P*' * u]
        """
        params = self.params

        # Transform to de-aliased physical grid
        u_phys = self.to_physical(u_hat, self.Npx, self.Npy)
        rho_phys = u_phys + params.rho_star
        rho_phys = np.clip(rho_phys, 1e-14, params.rho_max - 1e-14)
        u_phys = rho_phys - params.rho_star

        # Laplacian in spectral space, then to physical
        lap_hat = -self.mu * u_hat
        lap_phys = self.to_physical(lap_hat, self.Npx, self.Npy)

        # |grad u|^2 via FD on the de-aliased physical grid (Neumann BCs)
        gs_phys = grad_squared_fd_2d(rho_phys, self.hx_phys, self.hy_phys,
                                     boundary="neumann")

        # Pointwise constitutive evaluations
        M_phys = params.M(rho_phys)
        Mp_phys = params.M_prime(rho_phys)
        P_phys = params.P(rho_phys)

        # Nonlinear residual: N = (M - M*) * Lap + M' * |grad|^2 - (P - P*' * u)
        N_phys = ((M_phys - params.M_star) * lap_phys
                  + Mp_phys * gs_phys
                  - (P_phys - params.P_star_prime * u_phys))

        # Transform back to spectral
        N_hat = self.to_spectral(N_phys)

        # Full RHS: D * N_hat + H * v * delta_{k=(0,0)}
        rhs = params.D * N_hat
        rhs[0, 0] += params.H * v
        return rhs


# ===================================================================
#  TIME STEPPING: ETD-RK4 (spectral, Cox-Matthews)
# ===================================================================

def step_etdrk4_2d(u_hat: np.ndarray, v: float,
                   spectral: SpectralState2D) -> Tuple[np.ndarray, float, float]:
    """
    One step of ETD-RK4 (Cox-Matthews scheme) in 2D spectral space.

    Parameters
    ----------
    u_hat : (Kx, Ky) spectral coefficients of u = rho - rho*
    v : participation variable
    spectral : SpectralState2D with precomputed weights

    Returns
    -------
    u_hat_new : updated spectral coefficients
    v_new : updated participation variable
    F_bar : spatial average of F[rho] (for diagnostics)
    """
    params = spectral.params
    dt = params.dt

    # Compute F_bar for participation update (on the de-aliased grid)
    u_phys = spectral.to_physical(u_hat, spectral.Npx, spectral.Npy)
    rho_phys = np.clip(u_phys + params.rho_star, 1e-14, params.rho_max - 1e-14)
    F_phys = operator_F_fd_2d_raw(rho_phys, spectral.hx_phys, spectral.hy_phys,
                                  params, boundary="neumann")
    F_bar = spatial_avg_2d(F_phys, spectral.hx_phys, spectral.hy_phys)

    # Participation at half-step and full-step
    v_half = _advance_v_dt(v, F_bar, params.zeta, params.tau, dt / 2.0)
    v_full = advance_v(v, F_bar, params.zeta, params.tau, dt)

    # Stage 1: a = N(u^n, v^n)
    a = spectral.nonlinear_rhs(u_hat, v)

    # Stage 2
    u_a = spectral.exp_half * u_hat + spectral.phi1_half * (dt / 2.0) * a
    b = spectral.nonlinear_rhs(u_a, v_half)

    # Stage 3
    u_b = spectral.exp_half * u_hat + spectral.phi1_half * (dt / 2.0) * b
    c = spectral.nonlinear_rhs(u_b, v_half)

    # Stage 4
    u_d = spectral.exp_half * u_a + spectral.phi1_half * (dt / 2.0) * c
    d = spectral.nonlinear_rhs(u_d, v_full)

    # Final update
    u_hat_new = (spectral.exp_full * u_hat
                 + dt * (spectral.phi1_full * a
                         + 2.0 * spectral.phi2_full * (b + c)
                         + spectral.phi3_full * d))

    return u_hat_new, v_full, F_bar


def operator_F_fd_2d_raw(rho: np.ndarray, hx: float, hy: float,
                         params: EDParameters2D,
                         boundary: str = "neumann") -> np.ndarray:
    """Evaluate F[rho] using FD operators with given grid spacing and BCs."""
    lap = laplacian_fd_2d(rho, hx, hy, boundary)
    gs = grad_squared_fd_2d(rho, hx, hy, boundary)
    M_vals = params.M(rho)
    Mp_vals = params.M_prime(rho)
    P_vals = params.P(rho)
    return M_vals * lap + Mp_vals * gs - P_vals


# ===================================================================
#  TIME STEPPING: CRANK-NICOLSON with ADI (FD)
# ===================================================================

def _build_tridiag_neumann(M_line: np.ndarray, coeff: float) -> np.ndarray:
    """
    Build banded matrix for the implicit diffusion solve along one axis.

    System: (I - coeff * diag(M) * L_h) * u_new = rhs
    where L_h is the 1D Laplacian stencil (divided by h^2 already absorbed into coeff).

    Parameters
    ----------
    M_line : (N,) mobility values along the line
    coeff : dt * D / (2 * h^2)

    Returns
    -------
    ab : (3, N) banded matrix for scipy.linalg.solve_banded
    """
    N = len(M_line)
    ab = np.zeros((3, N))

    # Main diagonal: 1 + 2 * coeff * M_i
    ab[1, :] = 1.0 + 2.0 * coeff * M_line

    # Upper diagonal: ab[0, j] = A[j-1, j] = -coeff * M_{j-1}
    ab[0, 1:] = -coeff * M_line[:-1]

    # Lower diagonal: ab[2, j] = A[j+1, j] = -coeff * M_{j+1}
    ab[2, :-1] = -coeff * M_line[1:]

    # Neumann boundary modifications (ghost-point reflection)
    # At j=0: factor of 2 on upper off-diagonal
    ab[0, 1] = -2.0 * coeff * M_line[0]
    # At j=N-1: factor of 2 on lower off-diagonal
    ab[2, -2] = -2.0 * coeff * M_line[-1]

    return ab


def _explicit_lap_1d_neumann(rho_line: np.ndarray, h: float) -> np.ndarray:
    """1D Laplacian along a single line with Neumann BCs."""
    N = len(rho_line)
    lap = np.empty(N)
    h2 = h * h
    lap[1:-1] = (rho_line[:-2] - 2.0 * rho_line[1:-1] + rho_line[2:]) / h2
    lap[0] = 2.0 * (rho_line[1] - rho_line[0]) / h2
    lap[-1] = 2.0 * (rho_line[-2] - rho_line[-1]) / h2
    return lap


def step_cn_fd_2d(rho: np.ndarray, v: float,
                  params: EDParameters2D) -> Tuple[np.ndarray, float, np.ndarray]:
    """
    One step of Crank-Nicolson with Peaceman-Rachford ADI splitting in 2D.

    Diffusion treated semi-implicitly (mobility frozen at time n).
    Nonlinear terms (M'|grad rho|^2, P) and participation treated explicitly.

    Half-step 1 (x-implicit):
      (I - coeff_x * M^n * L_xx) rho^* = rho^n + coeff_y * M^n * L_yy rho^n
                                          + dt * (D * M' * gs - D * P + H * v)

    Half-step 2 (y-implicit):
      (I - coeff_y * M^n * L_yy) rho^{n+1} = rho^* - coeff_y * M^n * L_yy rho^n

    Returns (rho_new, v_new, F_rho).
    """
    Nx, Ny = rho.shape
    dt = params.dt
    D_val = params.D
    H_val = params.H
    hx = params.hx
    hy = params.hy

    coeff_x = 0.5 * dt * D_val / (hx * hx)
    coeff_y = 0.5 * dt * D_val / (hy * hy)

    # Evaluate all operators at current state
    ops = compute_operators_2d(rho, params)
    M_vals = ops['M']
    F_rho = ops['F']
    F_bar = spatial_avg_2d(F_rho, hx, hy)

    # Explicit y-diffusion: M^n * L_yy rho^n (computed per-row)
    M_lap_y = np.zeros_like(rho)
    for i in range(Nx):
        M_lap_y[i, :] = M_vals[i, :] * _explicit_lap_1d_neumann(rho[i, :], hy)

    # Source terms (explicit)
    S = D_val * ops['Mp'] * ops['grad_sq'] - D_val * ops['P_val'] + H_val * v

    # --- Half-step 1: x-implicit, y-explicit ---
    rhs1 = rho + coeff_y * M_lap_y * (hy * hy) + dt * S
    # Note: coeff_y * M * L_yy * hy^2 = (dt*D/2) * M * L_yy_unnorm
    # where L_yy_unnorm is (rho_{j+1} - 2*rho_j + rho_{j-1}) without /hy^2.
    # But M_lap_y already includes M and /hy^2, so:
    # rhs1 = rho + (dt*D/2) * M_lap_y + dt * S
    rhs1 = rho + 0.5 * dt * D_val * M_lap_y + dt * S

    rho_star = np.empty_like(rho)
    for j in range(Ny):
        ab = _build_tridiag_neumann(M_vals[:, j], coeff_x)
        rho_star[:, j] = solve_banded((1, 1), ab, rhs1[:, j])

    # --- Half-step 2: y-implicit, x-explicit ---
    # rhs2 = rho^* - coeff_y_scaled * M^n * L_yy rho^n
    # This subtracts the explicit y-diffusion that was added in step 1,
    # so the net effect is: implicit y-diffusion replaces explicit y-diffusion.
    rhs2 = rho_star - 0.5 * dt * D_val * M_lap_y

    rho_new = np.empty_like(rho)
    for i in range(Nx):
        ab = _build_tridiag_neumann(M_vals[i, :], coeff_y)
        rho_new[i, :] = solve_banded((1, 1), ab, rhs2[i, :])

    # Advance participation
    v_new = advance_v(v, F_bar, params.zeta, params.tau, dt)

    return rho_new, v_new, F_rho


# ===================================================================
#  STATE INITIALIZATION
# ===================================================================

def initialize_state_2d(params: EDParameters2D,
                        rho_init: Optional[np.ndarray] = None,
                        perturbation: str = "gaussian",
                        amplitude: float = 0.01,
                        seed: Optional[int] = None) -> Dict:
    """
    Initialize the 2D simulation state.

    Parameters
    ----------
    params : EDParameters2D
    rho_init : optional (Nx, Ny) array; overrides perturbation if given
    perturbation : "gaussian", "cosine", "random", "uniform"
    amplitude : perturbation amplitude relative to rho_star
    seed : RNG seed for "random" perturbation

    Returns
    -------
    state : dict with 'rho', 'v', 'u_hat' (if spectral), 'spectral' (if spectral)
    """
    X, Y = make_grid_2d(params)

    if rho_init is not None:
        rho = rho_init.copy()
    else:
        rho = np.full((params.Nx, params.Ny), params.rho_star)

        if perturbation == "gaussian":
            cx, cy = params.Lx / 2.0, params.Ly / 2.0
            sx = params.Lx / 10.0
            sy = params.Ly / 10.0
            rho += amplitude * np.exp(-((X - cx)**2 / (2*sx**2) + (Y - cy)**2 / (2*sy**2)))

        elif perturbation == "cosine":
            rho += amplitude * np.cos(np.pi * X / params.Lx) * np.cos(np.pi * Y / params.Ly)

        elif perturbation == "random":
            rng = np.random.default_rng(seed)
            rho += amplitude * rng.standard_normal((params.Nx, params.Ny))

        elif perturbation == "uniform":
            pass  # No perturbation: rho = rho_star everywhere

        else:
            raise ValueError(f"Unknown perturbation: {perturbation}")

    # Enforce bounds
    rho, _, _ = enforce_bounds_2d(rho, params.rho_max)

    state = {
        'rho': rho,
        'v': 0.0,
        'X': X,
        'Y': Y,
        't': 0.0,
    }

    # Initialize spectral state if using ETD-RK4
    if params.method == "etdrk4":
        spectral = SpectralState2D(params)
        # Transform initial perturbation to spectral space
        # The spectral grid has Npx x Npy points; resample rho onto it
        if params.Nx == spectral.Npx and params.Ny == spectral.Npy:
            u_phys = rho - params.rho_star
        else:
            # Interpolate rho onto the de-aliased physical grid
            from scipy.interpolate import RegularGridInterpolator
            x_fd = np.linspace(0.0, params.Lx, params.Nx)
            y_fd = np.linspace(0.0, params.Ly, params.Ny)
            interp = RegularGridInterpolator((x_fd, y_fd), rho - params.rho_star)
            x_sp = np.linspace(0.0, params.Lx, spectral.Npx)
            y_sp = np.linspace(0.0, params.Ly, spectral.Npy)
            Xsp, Ysp = np.meshgrid(x_sp, y_sp, indexing='ij')
            pts = np.column_stack([Xsp.ravel(), Ysp.ravel()])
            u_phys = interp(pts).reshape(spectral.Npx, spectral.Npy)

        u_hat = spectral.to_spectral(u_phys)
        state['u_hat'] = u_hat
        state['spectral'] = spectral

    return state


# ===================================================================
#  SINGLE-STEP DISPATCHER
# ===================================================================

def step_2d(state: Dict, params: EDParameters2D) -> Dict:
    """
    Dispatch one time step to the appropriate method.

    Modifies and returns the state dict.
    """
    method = params.method.lower()
    rho = state['rho']
    v = state['v']

    if method == "etdrk4":
        spectral = state['spectral']
        u_hat = state['u_hat']
        u_hat_new, v_new, F_bar = step_etdrk4_2d(u_hat, v, spectral)

        # Reconstruct physical density on the FD grid
        rho_new = spectral.to_physical(u_hat_new, params.Nx, params.Ny) + params.rho_star
        rho_new, n_pos, n_cap = enforce_bounds_2d(rho_new, params.rho_max)

        # Update spectral coefficients from the clamped field
        if n_pos > 0 or n_cap > 0:
            u_phys_new = rho_new - params.rho_star
            # Resample to de-aliased grid if sizes differ
            if params.Nx != spectral.Npx or params.Ny != spectral.Npy:
                from scipy.interpolate import RegularGridInterpolator
                x_fd = np.linspace(0.0, params.Lx, params.Nx)
                y_fd = np.linspace(0.0, params.Ly, params.Ny)
                interp = RegularGridInterpolator((x_fd, y_fd), u_phys_new)
                x_sp = np.linspace(0.0, params.Lx, spectral.Npx)
                y_sp = np.linspace(0.0, params.Ly, spectral.Npy)
                Xsp, Ysp = np.meshgrid(x_sp, y_sp, indexing='ij')
                pts = np.column_stack([Xsp.ravel(), Ysp.ravel()])
                u_phys_sp = interp(pts).reshape(spectral.Npx, spectral.Npy)
                u_hat_new = spectral.to_spectral(u_phys_sp)
            else:
                u_hat_new = spectral.to_spectral(u_phys_new)

        state['rho'] = rho_new
        state['v'] = v_new
        state['u_hat'] = u_hat_new
        state['F_bar'] = F_bar
        state['n_pos'] = n_pos
        state['n_cap'] = n_cap

    elif method == "crank_nicolson":
        rho_new, v_new, F_rho = step_cn_fd_2d(rho, v, params)
        rho_new, n_pos, n_cap = enforce_bounds_2d(rho_new, params.rho_max)
        F_bar = spatial_avg_2d(F_rho, params.hx, params.hy)

        state['rho'] = rho_new
        state['v'] = v_new
        state['F_bar'] = F_bar
        state['n_pos'] = n_pos
        state['n_cap'] = n_cap

    else:
        raise ValueError(f"Unknown method: {method}")

    state['t'] += params.dt
    return state


# ===================================================================
#  SIMULATION RUNNER
# ===================================================================

def run_simulation_2d(params: EDParameters2D,
                      rho_init: Optional[np.ndarray] = None,
                      perturbation: str = "gaussian",
                      amplitude: float = 0.01,
                      seed: Optional[int] = None,
                      callbacks: Optional[List[Callable]] = None,
                      verbose: bool = True) -> Dict:
    """
    Run the full 2D ED simulation.

    Parameters
    ----------
    params : EDParameters2D
    rho_init : optional initial density field
    perturbation : initial condition type (if rho_init is None)
    amplitude : perturbation amplitude
    seed : RNG seed
    callbacks : list of callables, called as cb(state, step_num, params)
    verbose : print progress

    Returns
    -------
    results : dict with keys:
        'params' : EDParameters2D
        'times' : list of output times
        'rho_snapshots' : list of (Nx, Ny) arrays
        'v_history' : list of v values
        'F_bar_history' : list of F_bar values
        'energy_history' : list of energy dicts
        'mass_history' : list of total mass values
        'final_state' : last state dict
    """
    state = initialize_state_2d(params, rho_init, perturbation, amplitude, seed)

    n_steps = int(np.ceil(params.T / params.dt))

    # Output storage
    times = [0.0]
    rho_snapshots = [state['rho'].copy()]
    v_history = [state['v']]
    F_bar_history = [0.0]
    energy_history = [energy_2d(state['rho'], state['v'], params)]
    mass_history = [total_mass_2d(state['rho'], params.hx, params.hy)]

    if verbose:
        print(params.summary())
        print(f"Running {n_steps} steps...")

    for n in range(1, n_steps + 1):
        state = step_2d(state, params)

        if callbacks:
            for cb in callbacks:
                cb(state, n, params)

        if n % params.k_out == 0 or n == n_steps:
            times.append(state['t'])
            rho_snapshots.append(state['rho'].copy())
            v_history.append(state['v'])
            F_bar_history.append(state.get('F_bar', 0.0))
            energy_history.append(energy_2d(state['rho'], state['v'], params))
            mass_history.append(total_mass_2d(state['rho'], params.hx, params.hy))

            if verbose and n % (10 * params.k_out) == 0:
                E = energy_history[-1]['total']
                m = mass_history[-1]
                print(f"  step {n:>8d}/{n_steps}, t={state['t']:.4f}, "
                      f"E={E:.6e}, mass={m:.6e}, v={state['v']:.6e}")

    if verbose:
        print("Done.")

    return {
        'params': params,
        'times': times,
        'rho_snapshots': rho_snapshots,
        'v_history': v_history,
        'F_bar_history': F_bar_history,
        'energy_history': energy_history,
        'mass_history': mass_history,
        'final_state': state,
    }
