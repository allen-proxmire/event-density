"""
edsim_solver_3d.py
==================
3D numerical core for the canonical Event Density PDE system.

Implements:
  - Spatial operators: Laplacian (7-point), gradient squared, F[rho]
      * Finite-difference (FD) with Neumann or periodic BCs
      * Spectral (3D DCT-I) with Neumann BCs
  - Time steppers:
      * Primary:   ETD-RK4 (spectral, Cox-Matthews scheme)
      * Secondary:  Crank-Nicolson with Douglas-Gunn ADI splitting (FD)
  - State management: initialization, bounds enforcement, diagnostics

Mirrors edsim_solver_2d.py with 3D extensions.
All notation follows Appendix C of the Rigour Paper and the Simulation Suite.

Memory note: a 128^3 grid at float64 uses ~16 MB per array. The solver
pre-allocates work arrays and minimises temporaries. For N >= 128, the
ETD-RK4 spectral solver (with 3/2-rule de-aliasing) requires ~1-2 GB.
"""

import numpy as np
from dataclasses import dataclass, field
from typing import Optional, Callable, Dict, List, Tuple
from scipy.fft import dctn, idctn
from scipy.linalg import solve_banded


# ===================================================================
#  CONSTITUTIVE FUNCTIONS (dimension-independent)
# ===================================================================

def _mobility(rho, rho_max, M0, beta):
    return M0 * np.maximum(rho_max - rho, 0.0) ** beta

def _mobility_deriv(rho, rho_max, M0, beta):
    return -beta * M0 * np.maximum(rho_max - rho, 0.0) ** (beta - 1.0)

def _penalty(rho, rho_star, P0):
    return P0 * (rho - rho_star)


# ===================================================================
#  PARAMETER DATACLASS
# ===================================================================

@dataclass
class EDParameters3D:
    """Complete parameter specification for the 3D canonical ED system."""

    # --- Canonical physics ---
    D: float = 0.3
    zeta: float = 0.1
    tau: float = 1.0
    rho_star: float = 0.5
    rho_max: float = 1.0

    # --- Constitutive ---
    M0: float = 1.0
    beta: float = 2.0
    P0: float = 1.0

    # --- 3D grid ---
    Nx: int = 32
    Ny: int = 32
    Nz: int = 32
    Lx: float = 1.0
    Ly: float = 1.0
    Lz: float = 1.0
    dt: float = 1e-4
    T: float = 1.0
    method: str = "etdrk4"
    boundary: str = "neumann"
    k_out: int = 50

    # --- Derived ---
    H: float = field(init=False)
    hx: float = field(init=False)
    hy: float = field(init=False)
    hz: float = field(init=False)
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
        for N, name in [(self.Nx, 'Nx'), (self.Ny, 'Ny'), (self.Nz, 'Nz')]:
            assert N >= 8, f"{name} = {N} too small"
        for L, name in [(self.Lx, 'Lx'), (self.Ly, 'Ly'), (self.Lz, 'Lz')]:
            assert L > 0.0, f"{name} not positive"
        assert self.dt > 0.0
        assert self.T > 0.0
        assert self.boundary in ("neumann", "periodic")
        assert self.method in ("etdrk4", "crank_nicolson")

    def _compute_derived(self):
        self.H = 1.0 - self.D
        self.hx = self.Lx / (self.Nx - 1)
        self.hy = self.Ly / (self.Ny - 1)
        self.hz = self.Lz / (self.Nz - 1)
        self.M_star = self.M0 * (self.rho_max - self.rho_star) ** self.beta
        self.M_star_prime = -self.beta * self.M0 * (self.rho_max - self.rho_star) ** (self.beta - 1.0)
        self.P_star_prime = self.P0

    def M(self, rho):
        return _mobility(rho, self.rho_max, self.M0, self.beta)

    def M_prime(self, rho):
        return _mobility_deriv(rho, self.rho_max, self.M0, self.beta)

    def P(self, rho):
        return _penalty(rho, self.rho_star, self.P0)

    def grid_shape(self):
        return (self.Nx, self.Ny, self.Nz)

    def n_points(self):
        return self.Nx * self.Ny * self.Nz

    def memory_estimate_mb(self, n_arrays=10):
        return self.n_points() * 8 * n_arrays / 1e6

    def summary(self) -> str:
        mem = self.memory_estimate_mb()
        return "\n".join([
            "=" * 60,
            "ED 3D Canonical Parameters",
            "=" * 60,
            f"  D={self.D}, H={self.H}, zeta={self.zeta}, tau={self.tau}",
            f"  rho*={self.rho_star}, rho_max={self.rho_max}",
            f"  M0={self.M0}, beta={self.beta}, P0={self.P0}",
            f"  M*={self.M_star:.6f}, P*'={self.P_star_prime:.6f}",
            f"  Grid: {self.Nx}x{self.Ny}x{self.Nz} ({self.n_points():,} pts, ~{mem:.0f} MB)",
            f"  Lx={self.Lx}, Ly={self.Ly}, Lz={self.Lz}",
            f"  hx={self.hx:.4e}, hy={self.hy:.4e}, hz={self.hz:.4e}",
            f"  dt={self.dt:.4e}, T={self.T}, method={self.method}",
            f"  boundary={self.boundary}",
            "=" * 60,
        ])


# ===================================================================
#  GRID CONSTRUCTION
# ===================================================================

def make_grid_3d(params: EDParameters3D):
    """Create 3D spatial grid.  Returns (X, Y, Z) meshgrids, each (Nx, Ny, Nz)."""
    x = np.linspace(0, params.Lx, params.Nx)
    y = np.linspace(0, params.Ly, params.Ny)
    z = np.linspace(0, params.Lz, params.Nz)
    return np.meshgrid(x, y, z, indexing='ij')


# ===================================================================
#  SPATIAL OPERATORS (Finite Difference)
# ===================================================================

def _pad_3d(rho, boundary):
    """Pad 3D array with one ghost cell on each side."""
    if boundary == "neumann":
        return np.pad(rho, 1, mode='reflect')
    elif boundary == "periodic":
        return np.pad(rho, 1, mode='wrap')
    raise ValueError(f"Unknown boundary: {boundary}")


def laplacian_fd_3d(rho, hx, hy, hz, boundary="neumann"):
    """
    7-point discrete Laplacian in 3D.

    nabla^2 rho = d_xx + d_yy + d_zz

    Each second derivative uses the standard 3-point stencil along its axis.
    BCs handled via ghost-cell padding.
    """
    p = _pad_3d(rho, boundary)
    c = p[1:-1, 1:-1, 1:-1]  # centre values (alias, no copy)
    lap = ((p[2:, 1:-1, 1:-1] + p[:-2, 1:-1, 1:-1] - 2.0 * c) / (hx * hx)
         + (p[1:-1, 2:, 1:-1] + p[1:-1, :-2, 1:-1] - 2.0 * c) / (hy * hy)
         + (p[1:-1, 1:-1, 2:] + p[1:-1, 1:-1, :-2] - 2.0 * c) / (hz * hz))
    return lap


def grad_squared_fd_3d(rho, hx, hy, hz, boundary="neumann"):
    """
    Discrete |grad rho|^2 in 3D using central differences.

    |nabla rho|^2 = (d_x rho)^2 + (d_y rho)^2 + (d_z rho)^2
    """
    p = _pad_3d(rho, boundary)
    gx = (p[2:, 1:-1, 1:-1] - p[:-2, 1:-1, 1:-1]) / (2.0 * hx)
    gy = (p[1:-1, 2:, 1:-1] - p[1:-1, :-2, 1:-1]) / (2.0 * hy)
    gz = (p[1:-1, 1:-1, 2:] - p[1:-1, 1:-1, :-2]) / (2.0 * hz)
    return gx * gx + gy * gy + gz * gz


def compute_operators_3d(rho, params):
    """Compute all spatial operators.  Returns dict with lap, grad_sq, M, Mp, P_val, F."""
    lap = laplacian_fd_3d(rho, params.hx, params.hy, params.hz, params.boundary)
    gs = grad_squared_fd_3d(rho, params.hx, params.hy, params.hz, params.boundary)
    M_v = params.M(rho)
    Mp_v = params.M_prime(rho)
    P_v = params.P(rho)
    F = M_v * lap + Mp_v * gs - P_v
    return {'lap': lap, 'grad_sq': gs, 'M': M_v, 'Mp': Mp_v, 'P_val': P_v, 'F': F}


def operator_F_fd_3d(rho, params):
    """Evaluate F[rho] = M Lap + M' |grad|^2 - P."""
    return compute_operators_3d(rho, params)['F']


def spatial_avg_3d(f, hx, hy, hz):
    """3D spatial average using the trapezoidal rule."""
    Nx, Ny, Nz = f.shape
    Lx = hx * (Nx - 1); Ly = hy * (Ny - 1); Lz = hz * (Nz - 1)
    wx = np.ones(Nx); wx[0] = 0.5; wx[-1] = 0.5
    wy = np.ones(Ny); wy[0] = 0.5; wy[-1] = 0.5
    wz = np.ones(Nz); wz[0] = 0.5; wz[-1] = 0.5
    return hx * hy * hz * np.einsum('i,j,k,ijk->', wx, wy, wz, f) / (Lx * Ly * Lz)


def _operator_F_raw_3d(rho, hx, hy, hz, params, boundary="neumann"):
    """F[rho] with explicit grid spacing and boundary."""
    lap = laplacian_fd_3d(rho, hx, hy, hz, boundary)
    gs = grad_squared_fd_3d(rho, hx, hy, hz, boundary)
    return params.M(rho) * lap + params.M_prime(rho) * gs - params.P(rho)


# ===================================================================
#  PARTICIPATION VARIABLE (exact exponential integrator)
# ===================================================================

def advance_v(v, F_bar, zeta, tau, dt):
    decay = np.exp(-zeta * dt / tau)
    return decay * v + (1.0 - decay) * (tau / zeta) * F_bar


# ===================================================================
#  POSITIVITY & CAPACITY ENFORCEMENT
# ===================================================================

def enforce_bounds_3d(rho, rho_max, eps_pos=1e-12, eps_cap=1e-12):
    n_pos = int(np.sum(rho <= eps_pos))
    n_cap = int(np.sum(rho >= rho_max - eps_cap))
    return np.clip(rho, eps_pos, rho_max - eps_cap), n_pos, n_cap


# ===================================================================
#  ENERGY FUNCTIONAL
# ===================================================================

def energy_3d(rho, v, params):
    """E = integral Phi(rho) dV + (tau H / 2) v^2."""
    delta = np.maximum(params.rho_max - rho, 1e-15)
    delta_star = params.rho_max - params.rho_star
    if abs(params.beta - 2.0) < 1e-12 and abs(params.M0 - 1.0) < 1e-12 and abs(params.P0 - 1.0) < 1e-12:
        ratio = delta_star / delta
        Phi = ratio - np.log(ratio) - 1.0
    else:
        Phi = np.zeros_like(rho)

    V = params.hx * (params.Nx - 1) * params.hy * (params.Ny - 1) * params.hz * (params.Nz - 1)
    E_pot = spatial_avg_3d(Phi, params.hx, params.hy, params.hz) * V
    E_kin = 0.5 * params.tau * params.H * v ** 2
    return {"total": E_pot + E_kin, "potential": E_pot, "kinetic": E_kin}


def total_mass_3d(rho, hx, hy, hz):
    Nx, Ny, Nz = rho.shape
    wx = np.ones(Nx); wx[0] = 0.5; wx[-1] = 0.5
    wy = np.ones(Ny); wy[0] = 0.5; wy[-1] = 0.5
    wz = np.ones(Nz); wz[0] = 0.5; wz[-1] = 0.5
    return hx * hy * hz * np.einsum('i,j,k,ijk->', wx, wy, wz, rho)


# ===================================================================
#  ETD-RK4 PHI FUNCTIONS
# ===================================================================

def _phi_functions(z):
    ez = np.exp(z)
    small = np.abs(z) < 1e-4
    z_safe = np.where(small, 1.0, z)
    phi1 = np.where(small, 1.0 + z/2 + z**2/6 + z**3/24,       (ez - 1.0) / z_safe)
    phi2 = np.where(small, 0.5 + z/6 + z**2/24 + z**3/120,      (ez - 1.0 - z) / z_safe**2)
    phi3 = np.where(small, 1/6 + z/24 + z**2/120 + z**3/720,    (ez - 1.0 - z - 0.5*z**2) / z_safe**3)
    return phi1, phi2, phi3


# ===================================================================
#  SPECTRAL STATE (3D DCT-I for Neumann BCs)
# ===================================================================

class SpectralState3D:
    """
    State container for the 3D spectral ETD-RK4 solver.

    Eigenvalues: mu_{kx,ky,kz} = (kx pi/Lx)^2 + (ky pi/Ly)^2 + (kz pi/Lz)^2.
    De-aliasing via the 3/2-rule in each axis.
    """

    def __init__(self, params: EDParameters3D):
        self.params = params
        self.Kx, self.Ky, self.Kz = params.Nx, params.Ny, params.Nz

        # De-aliased physical grid (3/2 rule)
        self.Npx = max(int(np.floor(1.5 * self.Kx)), self.Kx)
        self.Npy = max(int(np.floor(1.5 * self.Ky)), self.Ky)
        self.Npz = max(int(np.floor(1.5 * self.Kz)), self.Kz)

        self.hx_p = params.Lx / (self.Npx - 1)
        self.hy_p = params.Ly / (self.Npy - 1)
        self.hz_p = params.Lz / (self.Npz - 1)

        # 3D Neumann eigenvalues (tensor-product sum)
        mu_x = (np.arange(self.Kx) * np.pi / params.Lx) ** 2
        mu_y = (np.arange(self.Ky) * np.pi / params.Ly) ** 2
        mu_z = (np.arange(self.Kz) * np.pi / params.Lz) ** 2
        self.mu = (mu_x[:, None, None] + mu_y[None, :, None] + mu_z[None, None, :])

        # Linear decay constants
        self.c = -params.D * params.M_star * self.mu

        # Precompute ETD weights
        z_full = self.c * params.dt
        z_half = self.c * params.dt / 2.0
        self.exp_full = np.exp(z_full)
        self.exp_half = np.exp(z_half)
        self.phi1_full, self.phi2_full, self.phi3_full = _phi_functions(z_full)
        self.phi1_half, _, _ = _phi_functions(z_half)

    def to_spectral(self, u_phys):
        """3D DCT-I forward transform with ED normalization."""
        shape = u_phys.shape
        raw = dctn(u_phys, type=1)
        norm = np.prod([s - 1 for s in shape])
        coeffs = raw / norm
        # Halve boundary modes per axis
        coeffs[0, :, :] /= 2.0;  coeffs[-1, :, :] /= 2.0
        coeffs[:, 0, :] /= 2.0;  coeffs[:, -1, :] /= 2.0
        coeffs[:, :, 0] /= 2.0;  coeffs[:, :, -1] /= 2.0
        return coeffs[:self.Kx, :self.Ky, :self.Kz]

    def to_physical(self, u_hat, Npx=None, Npy=None, Npz=None):
        """3D DCT-I inverse transform."""
        if Npx is None: Npx = self.Npx
        if Npy is None: Npy = self.Npy
        if Npz is None: Npz = self.Npz

        Kx_in, Ky_in, Kz_in = u_hat.shape
        padded = np.zeros((Npx, Npy, Npz))
        padded[:Kx_in, :Ky_in, :Kz_in] = u_hat

        # Undo boundary halving
        padded[0, :, :] *= 2.0
        if Kx_in == Npx: padded[-1, :, :] *= 2.0
        padded[:, 0, :] *= 2.0
        if Ky_in == Npy: padded[:, -1, :] *= 2.0
        padded[:, :, 0] *= 2.0
        if Kz_in == Npz: padded[:, :, -1] *= 2.0

        norm = (Npx - 1) * (Npy - 1) * (Npz - 1)
        return idctn(padded * norm, type=1)

    def nonlinear_rhs(self, u_hat, v):
        """Nonlinear residual D*N_hat + H*v*delta_{k=0}."""
        params = self.params
        u_p = self.to_physical(u_hat)
        rho_p = np.clip(u_p + params.rho_star, 1e-14, params.rho_max - 1e-14)
        u_p = rho_p - params.rho_star

        lap_p = self.to_physical(-self.mu * u_hat)
        gs_p = grad_squared_fd_3d(rho_p, self.hx_p, self.hy_p, self.hz_p, "neumann")

        M_p = params.M(rho_p)
        Mp_p = params.M_prime(rho_p)
        P_p = params.P(rho_p)

        N_p = ((M_p - params.M_star) * lap_p + Mp_p * gs_p
               - (P_p - params.P_star_prime * u_p))
        N_hat = self.to_spectral(N_p)

        rhs = params.D * N_hat
        rhs[0, 0, 0] += params.H * v
        return rhs


# ===================================================================
#  TIME STEPPING: ETD-RK4 (spectral, Cox-Matthews)
# ===================================================================

def step_etdrk4_3d(u_hat, v, spectral):
    """One step of ETD-RK4 in 3D spectral space.  Returns (u_hat_new, v_new, F_bar)."""
    params = spectral.params
    dt = params.dt

    u_p = spectral.to_physical(u_hat)
    rho_p = np.clip(u_p + params.rho_star, 1e-14, params.rho_max - 1e-14)
    F_p = _operator_F_raw_3d(rho_p, spectral.hx_p, spectral.hy_p, spectral.hz_p,
                              params, "neumann")
    F_bar = spatial_avg_3d(F_p, spectral.hx_p, spectral.hy_p, spectral.hz_p)

    v_half = advance_v(v, F_bar, params.zeta, params.tau, dt / 2.0)
    v_full = advance_v(v, F_bar, params.zeta, params.tau, dt)

    a = spectral.nonlinear_rhs(u_hat, v)
    u_a = spectral.exp_half * u_hat + spectral.phi1_half * (dt / 2.0) * a
    b = spectral.nonlinear_rhs(u_a, v_half)
    u_b = spectral.exp_half * u_hat + spectral.phi1_half * (dt / 2.0) * b
    c = spectral.nonlinear_rhs(u_b, v_half)
    u_d = spectral.exp_half * u_a + spectral.phi1_half * (dt / 2.0) * c
    d = spectral.nonlinear_rhs(u_d, v_full)

    u_hat_new = (spectral.exp_full * u_hat
                 + dt * (spectral.phi1_full * a
                         + 2.0 * spectral.phi2_full * (b + c)
                         + spectral.phi3_full * d))
    return u_hat_new, v_full, F_bar


# ===================================================================
#  TIME STEPPING: CRANK-NICOLSON with DOUGLAS-GUNN ADI (FD)
# ===================================================================

def _build_tridiag_neumann(M_line, coeff):
    """Banded matrix for implicit 1D diffusion solve (Neumann BCs)."""
    N = len(M_line)
    ab = np.zeros((3, N))
    ab[1, :] = 1.0 + 2.0 * coeff * M_line
    ab[0, 1:] = -coeff * M_line[:-1]
    ab[2, :-1] = -coeff * M_line[1:]
    ab[0, 1] = -2.0 * coeff * M_line[0]
    ab[2, -2] = -2.0 * coeff * M_line[-1]
    return ab


def _lap_1d_neumann(f_line, h):
    """1D Laplacian along a line with Neumann BCs."""
    N = len(f_line)
    lap = np.empty(N)
    h2 = h * h
    lap[1:-1] = (f_line[:-2] - 2.0 * f_line[1:-1] + f_line[2:]) / h2
    lap[0] = 2.0 * (f_line[1] - f_line[0]) / h2
    lap[-1] = 2.0 * (f_line[-2] - f_line[-1]) / h2
    return lap


def step_cn_fd_3d(rho, v, params):
    """
    One step of CN with Douglas-Gunn ADI splitting in 3D.

    Three sub-steps, each treating one direction implicitly:
      Step 1 (x-implicit): adds all explicit terms + explicit y,z diffusion
      Step 2 (y-implicit): corrects y-diffusion from explicit to implicit
      Step 3 (z-implicit): corrects z-diffusion from explicit to implicit

    Returns (rho_new, v_new, F_rho).
    """
    Nx, Ny, Nz = rho.shape
    dt = params.dt
    D_v = params.D
    H_v = params.H
    hx, hy, hz = params.hx, params.hy, params.hz

    cx = 0.5 * dt * D_v / (hx * hx)
    cy = 0.5 * dt * D_v / (hy * hy)
    cz = 0.5 * dt * D_v / (hz * hz)

    ops = compute_operators_3d(rho, params)
    M_v = ops['M']
    F_rho = ops['F']
    F_bar = spatial_avg_3d(F_rho, hx, hy, hz)

    # Explicit directional diffusion: M * L_yy rho, M * L_zz rho
    M_lap_y = np.empty_like(rho)
    M_lap_z = np.empty_like(rho)
    for i in range(Nx):
        for k in range(Nz):
            M_lap_y[i, :, k] = M_v[i, :, k] * _lap_1d_neumann(rho[i, :, k], hy)
    for i in range(Nx):
        for j in range(Ny):
            M_lap_z[i, j, :] = M_v[i, j, :] * _lap_1d_neumann(rho[i, j, :], hz)

    S = D_v * ops['Mp'] * ops['grad_sq'] - D_v * ops['P_val'] + H_v * v

    # --- Step 1: x-implicit ---
    rhs1 = rho + 0.5 * dt * D_v * (M_lap_y + M_lap_z) + dt * S
    rho_star = np.empty_like(rho)
    for j in range(Ny):
        for k in range(Nz):
            ab = _build_tridiag_neumann(M_v[:, j, k], cx)
            rho_star[:, j, k] = solve_banded((1, 1), ab, rhs1[:, j, k])

    # --- Step 2: y-implicit ---
    rhs2 = rho_star - 0.5 * dt * D_v * M_lap_y
    rho_dstar = np.empty_like(rho)
    for i in range(Nx):
        for k in range(Nz):
            ab = _build_tridiag_neumann(M_v[i, :, k], cy)
            rho_dstar[i, :, k] = solve_banded((1, 1), ab, rhs2[i, :, k])

    # --- Step 3: z-implicit ---
    rhs3 = rho_dstar - 0.5 * dt * D_v * M_lap_z
    rho_new = np.empty_like(rho)
    for i in range(Nx):
        for j in range(Ny):
            ab = _build_tridiag_neumann(M_v[i, j, :], cz)
            rho_new[i, j, :] = solve_banded((1, 1), ab, rhs3[i, j, :])

    v_new = advance_v(v, F_bar, params.zeta, params.tau, dt)
    return rho_new, v_new, F_rho


# ===================================================================
#  STATE INITIALIZATION
# ===================================================================

def initialize_state_3d(params, rho_init=None,
                        perturbation="gaussian", amplitude=0.01, seed=None):
    """Initialize the 3D simulation state."""
    X, Y, Z = make_grid_3d(params)
    shape = params.grid_shape()

    if rho_init is not None:
        rho = rho_init.copy()
    else:
        rho = np.full(shape, params.rho_star)
        if perturbation == "gaussian":
            cx, cy, cz = params.Lx/2, params.Ly/2, params.Lz/2
            sx, sy, sz = params.Lx/10, params.Ly/10, params.Lz/10
            rho += amplitude * np.exp(-(
                (X - cx)**2 / (2*sx**2) +
                (Y - cy)**2 / (2*sy**2) +
                (Z - cz)**2 / (2*sz**2)))
        elif perturbation == "cosine":
            rho += amplitude * (np.cos(np.pi * X / params.Lx)
                              * np.cos(np.pi * Y / params.Ly)
                              * np.cos(np.pi * Z / params.Lz))
        elif perturbation == "random":
            rng = np.random.default_rng(seed)
            rho += amplitude * rng.standard_normal(shape)
        elif perturbation == "uniform":
            pass
        else:
            raise ValueError(f"Unknown perturbation: {perturbation}")

    rho, _, _ = enforce_bounds_3d(rho, params.rho_max)
    state = {'rho': rho, 'v': 0.0, 't': 0.0}

    if params.method == "etdrk4":
        spectral = SpectralState3D(params)
        if (params.Nx == spectral.Npx and params.Ny == spectral.Npy
                and params.Nz == spectral.Npz):
            u_phys = rho - params.rho_star
        else:
            from scipy.interpolate import RegularGridInterpolator
            x = np.linspace(0, params.Lx, params.Nx)
            y = np.linspace(0, params.Ly, params.Ny)
            z = np.linspace(0, params.Lz, params.Nz)
            interp = RegularGridInterpolator((x, y, z), rho - params.rho_star)
            xs = np.linspace(0, params.Lx, spectral.Npx)
            ys = np.linspace(0, params.Ly, spectral.Npy)
            zs = np.linspace(0, params.Lz, spectral.Npz)
            Xs, Ys, Zs = np.meshgrid(xs, ys, zs, indexing='ij')
            pts = np.column_stack([Xs.ravel(), Ys.ravel(), Zs.ravel()])
            u_phys = interp(pts).reshape(spectral.Npx, spectral.Npy, spectral.Npz)
        state['u_hat'] = spectral.to_spectral(u_phys)
        state['spectral'] = spectral

    return state


# ===================================================================
#  SINGLE-STEP DISPATCHER
# ===================================================================

def step_3d(state, params):
    """Dispatch one time step."""
    method = params.method.lower()
    rho = state['rho']
    v = state['v']

    if method == "etdrk4":
        spectral = state['spectral']
        u_hat_new, v_new, F_bar = step_etdrk4_3d(state['u_hat'], v, spectral)

        rho_new = spectral.to_physical(u_hat_new,
                                       params.Nx, params.Ny, params.Nz) + params.rho_star
        rho_new, n_pos, n_cap = enforce_bounds_3d(rho_new, params.rho_max)

        if n_pos > 0 or n_cap > 0:
            u_new = rho_new - params.rho_star
            if (params.Nx != spectral.Npx or params.Ny != spectral.Npy
                    or params.Nz != spectral.Npz):
                from scipy.interpolate import RegularGridInterpolator
                x = np.linspace(0, params.Lx, params.Nx)
                y = np.linspace(0, params.Ly, params.Ny)
                z = np.linspace(0, params.Lz, params.Nz)
                interp = RegularGridInterpolator((x, y, z), u_new)
                xs = np.linspace(0, params.Lx, spectral.Npx)
                ys = np.linspace(0, params.Ly, spectral.Npy)
                zs = np.linspace(0, params.Lz, spectral.Npz)
                Xs, Ys, Zs = np.meshgrid(xs, ys, zs, indexing='ij')
                pts = np.column_stack([Xs.ravel(), Ys.ravel(), Zs.ravel()])
                u_new = interp(pts).reshape(spectral.Npx, spectral.Npy, spectral.Npz)
            u_hat_new = spectral.to_spectral(u_new)

        state['rho'] = rho_new
        state['v'] = v_new
        state['u_hat'] = u_hat_new
        state['F_bar'] = F_bar
        state['n_pos'] = n_pos
        state['n_cap'] = n_cap

    elif method == "crank_nicolson":
        rho_new, v_new, F_rho = step_cn_fd_3d(rho, v, params)
        rho_new, n_pos, n_cap = enforce_bounds_3d(rho_new, params.rho_max)
        F_bar = spatial_avg_3d(F_rho, params.hx, params.hy, params.hz)

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

def run_simulation_3d(params, rho_init=None, perturbation="gaussian",
                      amplitude=0.01, seed=None, callbacks=None,
                      verbose=True, store_snapshots=False):
    """
    Run the full 3D ED simulation.

    Parameters
    ----------
    store_snapshots : bool
        If False (default), only store the final state to save memory.
        If True, store rho snapshots at each output step (WARNING: large memory).
    """
    state = initialize_state_3d(params, rho_init, perturbation, amplitude, seed)
    n_steps = int(np.ceil(params.T / params.dt))

    times = [0.0]
    v_history = [state['v']]
    F_bar_history = [0.0]
    energy_history = [energy_3d(state['rho'], state['v'], params)]
    mass_history = [total_mass_3d(state['rho'], params.hx, params.hy, params.hz)]
    rho_snapshots = [state['rho'].copy()] if store_snapshots else []

    if verbose:
        print(params.summary())
        print(f"Running {n_steps} steps...")

    for n in range(1, n_steps + 1):
        state = step_3d(state, params)

        if callbacks:
            for cb in callbacks:
                cb(state, n, params)

        if n % params.k_out == 0 or n == n_steps:
            times.append(state['t'])
            v_history.append(state['v'])
            F_bar_history.append(state.get('F_bar', 0.0))
            energy_history.append(energy_3d(state['rho'], state['v'], params))
            mass_history.append(total_mass_3d(state['rho'], params.hx, params.hy, params.hz))
            if store_snapshots:
                rho_snapshots.append(state['rho'].copy())

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
        'v_history': v_history,
        'F_bar_history': F_bar_history,
        'energy_history': energy_history,
        'mass_history': mass_history,
        'rho_snapshots': rho_snapshots,
        'final_state': state,
    }
