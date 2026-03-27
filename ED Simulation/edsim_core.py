"""
edsim_core.py
==============
Core numerical engine for the canonical ED PDE system.

Implements three time-stepping schemes:
  - Method A / Implicit Euler    (Suite §1.4.1.1)
  - Method A / Crank-Nicolson    (Suite §1.4.1.2)
  - Method B / ETD-RK4           (Suite §1.4.2.2)

Spatial discretization:
  - Method A: second-order finite differences with Neumann ghost points
  - Method B: spectral (DCT-I) with pseudospectral nonlinear evaluation

All notation follows Appendix C of the Rigour Paper and the Simulation Suite.
"""

import numpy as np
from scipy.linalg import solve_banded
from scipy.fft import dctn, idctn
from edsim_parameters import EDParameters


# ===================================================================
#  GRID CONSTRUCTION
# ===================================================================

def make_grid(params: EDParameters) -> np.ndarray:
    """
    Create the spatial grid x_j = j * h, j = 0, 1, ..., N+1.

    Returns array of length N_grid = N + 2.
    """
    return np.linspace(0.0, params.L, params.N_grid)


# ===================================================================
#  SPATIAL OPERATORS (Method A: Finite Difference)
# ===================================================================

def laplacian_fd(rho: np.ndarray, h: float) -> np.ndarray:
    """
    Discrete Laplacian with Neumann boundary conditions (ghost-point reflection).

    Interior: (rho_{j-1} - 2*rho_j + rho_{j+1}) / h^2
    Boundary: 2*(rho_1 - rho_0)/h^2  and  2*(rho_N - rho_{N+1})/h^2
    """
    lap = np.empty_like(rho)
    h2 = h * h
    # Interior points
    lap[1:-1] = (rho[:-2] - 2.0 * rho[1:-1] + rho[2:]) / h2
    # Neumann boundaries (ghost-point reflection)
    lap[0] = 2.0 * (rho[1] - rho[0]) / h2
    lap[-1] = 2.0 * (rho[-2] - rho[-1]) / h2
    return lap


def grad_squared_fd(rho: np.ndarray, h: float) -> np.ndarray:
    """
    Discrete |grad rho|^2 with central differences.

    Interior: ((rho_{j+1} - rho_{j-1}) / (2h))^2
    Boundary: 0 (Neumann: grad rho = 0 at boundaries)
    """
    gs = np.zeros_like(rho)
    gs[1:-1] = ((rho[2:] - rho[:-2]) / (2.0 * h)) ** 2
    # Boundary values are zero by Neumann condition
    return gs


def operator_F_fd(rho: np.ndarray, params: EDParameters) -> np.ndarray:
    """
    Evaluate the nonlinear density operator F[rho] on the FD grid.

    F[rho] = M(rho) * Lap(rho) + M'(rho) * |grad rho|^2 - P(rho)
    """
    lap = laplacian_fd(rho, params.h)
    gs = grad_squared_fd(rho, params.h)
    M_vals = params.M(rho)
    Mp_vals = params.M_prime(rho)
    P_vals = params.P(rho)
    return M_vals * lap + Mp_vals * gs - P_vals


def spatial_avg_fd(f: np.ndarray, h: float) -> float:
    """Trapezoidal-rule spatial average: (1/L) * integral of f dx."""
    L = h * (len(f) - 1)
    return (h * (0.5 * f[0] + np.sum(f[1:-1]) + 0.5 * f[-1])) / L


# ===================================================================
#  PARTICIPATION VARIABLE UPDATE (exact exponential integrator)
# ===================================================================

def advance_v(v: float, F_bar: float, params: EDParameters) -> float:
    """
    Advance the participation variable v by one time step.

    v^{n+1} = exp(-zeta*dt/tau) * v^n + (1 - exp(-zeta*dt/tau)) * (tau/zeta) * F_bar

    where F_bar = spatial average of F[rho^n].
    """
    decay = np.exp(-params.zeta * params.dt / params.tau)
    return decay * v + (1.0 - decay) * (params.tau / params.zeta) * F_bar


# ===================================================================
#  TIME STEPPING: IMPLICIT EULER (Method A)
# ===================================================================

def step_implicit_euler(rho: np.ndarray, v: float, params: EDParameters):
    """
    One step of implicit Euler.

    Diffusion treated implicitly (tridiagonal solve).
    Nonlinear terms (M'|grad rho|^2, P) and participation coupling treated explicitly.

    Returns (rho_new, v_new, F_rho)
    """
    N_grid = len(rho)
    h = params.h
    dt = params.dt
    D = params.D
    H = params.H

    # Evaluate explicit terms at current state
    M_vals = params.M(rho)
    Mp_vals = params.M_prime(rho)
    P_vals = params.P(rho)
    gs = grad_squared_fd(rho, h)
    F_rho = operator_F_fd(rho, params)
    F_bar = spatial_avg_fd(F_rho, h)

    # Right-hand side: rho + dt * (D * M'|grad|^2 - D*P + H*v)
    rhs = rho + dt * (D * Mp_vals * gs - D * P_vals + H * v)

    # Tridiagonal system: (I - dt*D*diag(M)*L_h) * rho_new = rhs
    # Diagonal: 1 + 2*dt*D*M/h^2
    # Off-diagonal: -dt*D*M/h^2
    h2 = h * h
    coeff = dt * D / h2

    # Build banded matrix for scipy.linalg.solve_banded
    # Format: (1 lower, 1 upper) diagonals
    ab = np.zeros((3, N_grid))

    # Main diagonal
    ab[1, :] = 1.0 + 2.0 * coeff * M_vals
    # Neumann BCs: boundary points have coefficient 2*(rho_1 - rho_0)/h^2
    # so the implicit matrix at j=0 has: 1 + 2*coeff*M_0 on diagonal,
    # -2*coeff*M_0 on upper off-diagonal
    ab[1, 0] = 1.0 + 2.0 * coeff * M_vals[0]
    ab[1, -1] = 1.0 + 2.0 * coeff * M_vals[-1]

    # Upper diagonal (ab[0, 1:])
    ab[0, 1:] = -coeff * M_vals[:-1]
    ab[0, 1] = -2.0 * coeff * M_vals[0]  # Neumann at left

    # Lower diagonal (ab[2, :-1])
    ab[2, :-1] = -coeff * M_vals[1:]
    ab[2, -2] = -2.0 * coeff * M_vals[-1]  # Neumann at right

    rho_new = solve_banded((1, 1), ab, rhs)

    # Advance participation
    v_new = advance_v(v, F_bar, params)

    return rho_new, v_new, F_rho


# ===================================================================
#  TIME STEPPING: CRANK-NICOLSON (Method A)
# ===================================================================

def step_crank_nicolson(rho: np.ndarray, v: float, params: EDParameters):
    """
    One step of Crank-Nicolson.

    Diffusion treated with half-weight implicit/explicit.
    Nonlinear terms treated explicitly.

    Returns (rho_new, v_new, F_rho)
    """
    N_grid = len(rho)
    h = params.h
    dt = params.dt
    D = params.D
    H = params.H
    h2 = h * h

    # Evaluate at current state
    M_vals = params.M(rho)
    Mp_vals = params.M_prime(rho)
    P_vals = params.P(rho)
    gs = grad_squared_fd(rho, h)
    lap = laplacian_fd(rho, h)
    F_rho = M_vals * lap + Mp_vals * gs - P_vals
    F_bar = spatial_avg_fd(F_rho, h)

    coeff = 0.5 * dt * D / h2

    # Explicit part: B_CN * rho + dt * (nonlinear + penalty + participation)
    # B_CN = I + (dt*D/2) * diag(M) * L_h
    B_rho = rho + 0.5 * dt * D * M_vals * lap
    rhs = B_rho + dt * (D * Mp_vals * gs - D * P_vals + H * v)

    # Implicit matrix: A_CN = I - (dt*D/2) * diag(M) * L_h
    ab = np.zeros((3, N_grid))

    # Main diagonal
    ab[1, :] = 1.0 + 2.0 * coeff * M_vals
    ab[1, 0] = 1.0 + 2.0 * coeff * M_vals[0]
    ab[1, -1] = 1.0 + 2.0 * coeff * M_vals[-1]

    # Upper diagonal
    ab[0, 1:] = -coeff * M_vals[:-1]
    ab[0, 1] = -2.0 * coeff * M_vals[0]

    # Lower diagonal
    ab[2, :-1] = -coeff * M_vals[1:]
    ab[2, -2] = -2.0 * coeff * M_vals[-1]

    rho_new = solve_banded((1, 1), ab, rhs)

    # Advance participation
    v_new = advance_v(v, F_bar, params)

    return rho_new, v_new, F_rho


# ===================================================================
#  TIME STEPPING: ETD-RK4 (Method B -- Spectral)
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
    phi1 = np.where(np.abs(z) > 1e-4,
                    (ez - 1.0) / z,
                    1.0 + z / 2.0 + z ** 2 / 6.0 + z ** 3 / 24.0)
    phi2 = np.where(np.abs(z) > 1e-4,
                    (ez - 1.0 - z) / z ** 2,
                    0.5 + z / 6.0 + z ** 2 / 24.0 + z ** 3 / 120.0)
    phi3 = np.where(np.abs(z) > 1e-4,
                    (ez - 1.0 - z - 0.5 * z ** 2) / z ** 3,
                    1.0 / 6.0 + z / 24.0 + z ** 2 / 120.0 + z ** 3 / 720.0)
    return phi1, phi2, phi3


class SpectralState:
    """State container for the spectral (Method B) solver."""

    def __init__(self, params: EDParameters):
        self.params = params
        self.N_modes = params.N
        self.L = params.L

        # Neumann eigenvalues mu_k = (k*pi/L)^2
        k = np.arange(self.N_modes)
        self.mu = (k * np.pi / self.L) ** 2

        # Linear decay constants: c_k = -D * M* * mu_k
        self.c = -params.D * params.M_star * self.mu

        # alpha_k = M* * mu_k + P*'
        self.alpha = params.M_star * self.mu + params.P_star_prime

        # Precompute ETD weights
        dt = params.dt
        z_full = self.c * dt
        z_half = self.c * dt / 2.0

        self.exp_full = np.exp(z_full)
        self.exp_half = np.exp(z_half)

        self.phi1_full, self.phi2_full, self.phi3_full = _phi_functions(z_full)
        self.phi1_half, _, _ = _phi_functions(z_half)

        # Physical grid for pseudospectral evaluation
        # DCT-I grid: x_j = j * L / (N_modes - 1), j = 0, ..., N_modes - 1
        self.N_phys = int(np.floor(1.5 * self.N_modes))  # 3/2-rule de-aliasing
        self.x_phys = np.linspace(0, self.L, self.N_phys)

    def to_spectral(self, u_phys: np.ndarray) -> np.ndarray:
        """Transform physical-space perturbation u = rho - rho* to spectral coefficients."""
        # DCT-I with normalization
        coeffs = dctn(u_phys, type=1) / (len(u_phys) - 1)
        coeffs[0] /= 2.0
        coeffs[-1] /= 2.0
        return coeffs[:self.N_modes]

    def to_physical(self, u_hat: np.ndarray, N_out: int = None) -> np.ndarray:
        """Transform spectral coefficients to physical space."""
        if N_out is None:
            N_out = self.N_phys
        # Zero-pad to N_out
        padded = np.zeros(N_out)
        padded[:len(u_hat)] = u_hat
        padded[0] *= 2.0
        if len(u_hat) == N_out:
            padded[-1] *= 2.0
        return idctn(padded * (N_out - 1), type=1) / 2.0

    def nonlinear_rhs(self, u_hat: np.ndarray, v: float) -> np.ndarray:
        """
        Compute the nonlinear residual N_hat in spectral space.

        N_k = DCT{ [M(rho) - M*]*Lap(u) + M'(rho)*|grad u|^2 - [P(rho) - P*'*u] }

        The linear part (-D*alpha_k*u_hat_k + H*v*delta_{k0}) is handled by ETD;
        this function returns only the nonlinear remainder.
        """
        params = self.params

        # Transform to physical space (de-aliased grid)
        u_phys = self.to_physical(u_hat, self.N_phys)
        rho_phys = u_phys + params.rho_star

        # Clamp rho to admissible range for constitutive evaluation
        rho_phys = np.clip(rho_phys, 1e-14, params.rho_max - 1e-14)

        # Compute Laplacian in spectral space, then transform
        lap_hat = -self.mu[:len(u_hat)] * u_hat
        lap_phys = self.to_physical(lap_hat, self.N_phys)

        # Compute gradient in spectral space via DST
        # d/dx cos(k*pi*x/L) = -(k*pi/L) * sin(k*pi*x/L)
        k = np.arange(len(u_hat))
        grad_hat_sin = -(k * np.pi / self.L) * u_hat
        # Transform sine coefficients to physical space
        # Use DST-I for sine modes
        from scipy.fft import dstn
        grad_pad = np.zeros(self.N_phys)
        grad_pad[:len(grad_hat_sin)] = grad_hat_sin
        grad_phys = dstn(grad_pad * (self.N_phys - 1), type=1) / (2.0 * (self.N_phys - 1))

        grad_sq_phys = grad_phys ** 2

        # Nonlinear residual pointwise
        M_phys = params.M(rho_phys)
        Mp_phys = params.M_prime(rho_phys)
        P_phys = params.P(rho_phys)

        # N(x) = [M(rho) - M*] * Lap(u) + M'(rho) * |grad u|^2 - [P(rho) - P*' * u]
        N_phys = ((M_phys - params.M_star) * lap_phys
                  + Mp_phys * grad_sq_phys
                  - (P_phys - params.P_star_prime * u_phys))

        # Transform back to spectral space (truncate to N_modes)
        N_hat = self.to_spectral(N_phys)

        # Add the participation coupling (only affects k=0 mode)
        # The full RHS is: -D*alpha_k*u_hat_k + D*N_hat_k + H*v*delta_{k0}*sqrt(L)
        # ETD handles -D*alpha_k*u_hat_k. We return D*N_hat_k + H*v*delta_{k0}*...
        # Actually: the participation couples as H*v uniformly in physical space,
        # which projects onto the k=0 mode.
        rhs = params.D * N_hat
        rhs[0] += params.H * v * np.sqrt(self.L)

        return rhs


def step_etdrk4(u_hat: np.ndarray, v: float, spectral: SpectralState):
    """
    One step of ETD-RK4 (Cox-Matthews scheme) in spectral space.

    Parameters
    ----------
    u_hat : spectral coefficients of u = rho - rho*
    v : participation variable
    spectral : SpectralState with precomputed weights

    Returns
    -------
    u_hat_new : updated spectral coefficients
    v_new : updated participation
    F_bar : spatial average of F[rho]
    """
    params = spectral.params
    dt = params.dt

    # Compute F_bar for participation update
    rho_phys = spectral.to_physical(u_hat, spectral.N_phys) + params.rho_star
    rho_phys_clamped = np.clip(rho_phys, 1e-14, params.rho_max - 1e-14)
    h_phys = spectral.params.L / (spectral.N_phys - 1)
    F_phys = (params.M(rho_phys_clamped) * laplacian_fd(rho_phys_clamped, h_phys)
              + params.M_prime(rho_phys_clamped) * grad_squared_fd(rho_phys_clamped, h_phys)
              - params.P(rho_phys_clamped))
    F_bar = spatial_avg_fd(F_phys, h_phys)

    # Participation at half-step and full-step
    v_half = advance_v(v, F_bar, EDParameters(
        **{**params.__dict__, 'dt': dt / 2.0,
           'H': params.H, 'h': params.h, 'N_grid': params.N_grid,
           'M_star': params.M_star, 'M_star_prime': params.M_star_prime,
           'P_star_prime': params.P_star_prime, 'Delta': params.Delta,
           'gamma_0': params.gamma_0, 'D_0': params.D_0, 'omega': params.omega}
    )) if False else _advance_v_dt(v, F_bar, params, dt / 2.0)
    v_full = advance_v(v, F_bar, params)

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


def _advance_v_dt(v: float, F_bar: float, params: EDParameters, dt: float) -> float:
    """Advance v with a custom time step (not params.dt)."""
    decay = np.exp(-params.zeta * dt / params.tau)
    return decay * v + (1.0 - decay) * (params.tau / params.zeta) * F_bar


# ===================================================================
#  POSITIVITY & CAPACITY ENFORCEMENT (Suite §1.7)
# ===================================================================

def enforce_bounds(rho: np.ndarray, params: EDParameters,
                   eps_pos: float = 1e-12, eps_cap: float = 1e-12):
    """
    Project rho into the admissible region (eps_pos, rho_max - eps_cap).

    Returns (rho_clamped, n_pos_violations, n_cap_violations).
    """
    n_pos = int(np.sum(rho <= eps_pos))
    n_cap = int(np.sum(rho >= params.rho_max - eps_cap))
    rho_out = np.clip(rho, eps_pos, params.rho_max - eps_cap)
    return rho_out, n_pos, n_cap


# ===================================================================
#  ENERGY FUNCTIONAL (Appendix C.2, Suite §5.1)
# ===================================================================

def energy(rho: np.ndarray, v: float, params: EDParameters) -> dict:
    """
    Compute the energy functional E[rho, v].

    E = integral Phi(rho) dx + (tau * H / 2) * v^2

    Returns dict with 'total', 'potential', 'kinetic' (participation).
    """
    Phi_vals = params.Phi(rho)
    h = params.h
    E_pot = h * (0.5 * Phi_vals[0] + np.sum(Phi_vals[1:-1]) + 0.5 * Phi_vals[-1])
    E_kin = 0.5 * params.tau * params.H * v ** 2
    return {
        "total": E_pot + E_kin,
        "potential": E_pot,
        "kinetic": E_kin,
    }


# ===================================================================
#  MASS INTEGRAL
# ===================================================================

def total_mass(rho: np.ndarray, h: float) -> float:
    """Compute total mass: integral of rho dx (trapezoidal rule)."""
    return h * (0.5 * rho[0] + np.sum(rho[1:-1]) + 0.5 * rho[-1])


# ===================================================================
#  SINGLE-STEP DISPATCHER
# ===================================================================

def step(rho: np.ndarray, v: float, params: EDParameters,
         spectral: SpectralState = None, u_hat: np.ndarray = None):
    """
    Dispatch one time step to the appropriate method.

    For Method A (FD): uses rho array directly.
    For Method B (spectral): uses u_hat (spectral coefficients).

    Returns dict with updated state and diagnostics.
    """
    method = params.method.lower()

    if method == "implicit_euler":
        rho_new, v_new, F_rho = step_implicit_euler(rho, v, params)
    elif method == "crank_nicolson":
        rho_new, v_new, F_rho = step_crank_nicolson(rho, v, params)
    elif method == "etdrk4":
        if spectral is None or u_hat is None:
            raise ValueError("ETD-RK4 requires SpectralState and u_hat")
        u_hat_new, v_new, F_bar = step_etdrk4(u_hat, v, spectral)
        rho_new = spectral.to_physical(u_hat_new, params.N_grid) + params.rho_star
        return {
            "rho": rho_new, "v": v_new, "u_hat": u_hat_new, "F_bar": F_bar,
        }
    else:
        raise ValueError(f"Unknown method: {method}")

    # Enforce bounds
    rho_new, n_pos, n_cap = enforce_bounds(rho_new, params)

    F_bar = spatial_avg_fd(F_rho, params.h) if method != "etdrk4" else None

    return {
        "rho": rho_new, "v": v_new, "F_bar": F_bar,
        "n_pos_violations": n_pos, "n_cap_violations": n_cap,
    }
