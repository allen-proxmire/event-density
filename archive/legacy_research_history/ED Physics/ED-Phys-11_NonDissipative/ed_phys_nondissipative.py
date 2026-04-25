"""
ED-Phys-11: Non-Dissipative and Strong-Coupling Regimes
==========================================================
Tests whether aggressive (non-perturbative) extensions can access
wave-like, strong-force, or anisotropic dynamics that the canonical
overdamped regime suppresses.

Three extensions are tested:
  A. Hyperbolic Sector — damped wave equation for rho with reduced dissipation
  B. Strong GMF Coupling — kappa*lambda pushed until force ~ curvature force
  C. Directional Operator — anisotropic phi equation (2D only)

Canonical sources: ED-5, ED-12, ED-12.5, ED-Phys-01 through ED-Phys-10.
"""

import sys
import os
import io
import time
import json
import numpy as np

# Force UTF-8 output on Windows
if sys.stdout.encoding != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
if sys.stderr.encoding != 'utf-8':
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'ED-Phys-02_Simulator'))

from ed_phys_config import EDParams
from ed_phys_operators import (
    discrete_laplacian,
    discrete_grad_squared,
    discrete_grad_magnitude,
    mobility,
    mobility_derivative,
)


# ============================================================
# Safety checks
# ============================================================

def _check_blowup(rho, v=None, phi=None, step=0, label=""):
    """Check for NaN, Inf, or runaway growth. Returns (ok, msg)."""
    if np.any(np.isnan(rho)):
        return False, f"[{label}] NaN in rho at step {step}"
    if np.any(np.isinf(rho)):
        return False, f"[{label}] Inf in rho at step {step}"
    if np.max(np.abs(rho)) > 1e10:
        return False, f"[{label}] rho blowup at step {step}: max={np.max(np.abs(rho)):.2e}"
    if v is not None:
        if np.any(np.isnan(v)) or np.any(np.isinf(v)):
            return False, f"[{label}] NaN/Inf in v at step {step}"
        if np.max(np.abs(v)) > 1e10:
            return False, f"[{label}] v blowup at step {step}: max={np.max(np.abs(v)):.2e}"
    if phi is not None:
        if np.any(np.isnan(phi)) or np.any(np.isinf(phi)):
            return False, f"[{label}] NaN/Inf in phi at step {step}"
        if np.max(np.abs(phi)) > 1e10:
            return False, f"[{label}] phi blowup at step {step}: max={np.max(np.abs(phi)):.2e}"
    return True, ""


# ============================================================
# Extension A: Hyperbolic Sector
# ============================================================
# tau * d^2 rho/dt^2 + zeta * d rho/dt = M(rho)*Lap(rho) + M'(rho)*|grad rho|^2 - alpha*gamma*rho^(gamma-1)
#
# Rewritten as first-order system:
#   d rho/dt = v
#   d v/dt   = (1/tau) * [RHS_canonical - zeta*v]
#
# Key difference from ED-Phys-09: we use MUCH lower zeta and
# moderate tau to push the damping ratio Q = sqrt(tau*omega)/zeta > 1.

def simulate_hyperbolic(
    params: EDParams,
    initial_rho: np.ndarray,
    tau: float = 1.0,
    zeta: float = 0.01,
    snapshot_interval: int = 500,
    label: str = "",
) -> dict:
    """Simulate the hyperbolic extension with reduced damping.

    Returns dict with time series diagnostics.
    """
    rho = initial_rho.copy().astype(np.float64)
    v = np.zeros_like(rho)
    d = rho.ndim
    dx = params.dx
    eps = 1e-10

    # CFL: wave speed c ~ sqrt(M_max / tau), need c*dt < dx
    M_max = params.M_0
    c_wave = np.sqrt(M_max / max(tau, 1e-12))
    eta_wave = 0.3 * dx / max(c_wave, 1e-12)
    eta_diff = params.cfl_safety * dx**2 / (2 * d * M_max) if M_max > 0 else 1.0
    eta = min(eta_wave, eta_diff)
    eta = min(eta, 0.01)  # cap at 0.01 for safety

    diagnostics = []
    blowup_step = None
    blowup_msg = ""

    for step in range(params.n_steps):
        # Safety check every 100 steps
        if step % 100 == 0:
            ok, msg = _check_blowup(rho, v, label=label, step=step)
            if not ok:
                blowup_step = step
                blowup_msg = msg
                break

        # Record diagnostics
        if step % snapshot_interval == 0:
            rho_safe = np.maximum(rho, eps)
            grad_mag = discrete_grad_magnitude(rho_safe, dx, params.boundary, eps)
            diag = {
                'step': step,
                'rho_mean': float(np.mean(rho)),
                'rho_max': float(np.max(rho)),
                'rho_min': float(np.min(rho)),
                'rho_std': float(np.std(rho)),
                'v_rms': float(np.sqrt(np.mean(v**2))),
                'v_max': float(np.max(np.abs(v))),
                'grad_mean': float(np.mean(grad_mag)),
                'kinetic_energy': float(0.5 * tau * np.sum(v**2)),
            }
            # Count peaks (1D only)
            if rho.ndim == 1:
                peaks = []
                for i in range(1, len(rho)-1):
                    if rho[i] > rho[i-1] and rho[i] > rho[i+1] and rho[i] > np.mean(rho) + np.std(rho):
                        peaks.append(i)
                diag['n_peaks'] = len(peaks)
                diag['peak_positions'] = peaks[:10]  # store up to 10
                # v sign changes (oscillation indicator)
                sign_changes = np.sum(np.abs(np.diff(np.sign(v))) > 0)
                diag['v_sign_changes'] = int(sign_changes)
            diagnostics.append(diag)

        # Compute canonical RHS
        rho_safe = np.maximum(rho, eps)
        lap = discrete_laplacian(rho_safe, dx, params.boundary, eps)
        grad_sq = discrete_grad_squared(rho_safe, dx, params.boundary, eps)
        M = mobility(rho_safe, params.M_0, params.rho_max, params.n_mob)
        Mprime = mobility_derivative(rho_safe, params.M_0, params.rho_max, params.n_mob)

        rhs = M * lap + Mprime * grad_sq - params.alpha * params.gamma_exp * rho_safe**(params.gamma_exp - 1)

        # Hyperbolic update
        dv_dt = (1.0 / tau) * (rhs - zeta * v)
        v_new = v + eta * dv_dt
        rho_new = rho + eta * v_new  # use updated v (semi-implicit for stability)

        # Positivity
        rho_new = np.maximum(rho_new, eps)

        rho = rho_new
        v = v_new

    # Final diagnostics
    rho_safe = np.maximum(rho, eps)
    grad_mag = discrete_grad_magnitude(rho_safe, dx, params.boundary, eps)
    final_diag = {
        'step': step if blowup_step is None else blowup_step,
        'rho_mean': float(np.mean(rho)),
        'rho_max': float(np.max(rho)),
        'rho_min': float(np.min(rho)),
        'rho_std': float(np.std(rho)),
        'v_rms': float(np.sqrt(np.mean(v**2))),
        'v_max': float(np.max(np.abs(v))),
        'grad_mean': float(np.mean(grad_mag)),
        'kinetic_energy': float(0.5 * tau * np.sum(v**2)),
    }
    if rho.ndim == 1:
        peaks = []
        for i in range(1, len(rho)-1):
            if rho[i] > rho[i-1] and rho[i] > rho[i+1] and rho[i] > np.mean(rho) + np.std(rho):
                peaks.append(i)
        final_diag['n_peaks'] = len(peaks)
        final_diag['peak_positions'] = peaks[:10]

    return {
        'eta_used': eta,
        'blowup_step': blowup_step,
        'blowup_msg': blowup_msg,
        'diagnostics': diagnostics,
        'final': final_diag,
        'rho_final': rho,
        'v_final': v,
    }


# ============================================================
# Extension B: Strong GMF Coupling
# ============================================================
# Same coupled system as ED-Phys-10, but with kappa and lambda
# pushed into the regime where force_rms ~ canonical curvature force.
#
# From ED-Phys-10: force_rms = 3.1 * kappa * lambda
# Canonical curvature force: M(rho)*Lap(rho) ~ O(0.1-1.0)
# => need kappa*lambda ~ 0.1/3.1 ~ 0.03 at minimum
# => try kappa*lambda up to 1.0 (kappa=lambda=1.0)
#
# Stability: use adaptive substeps if needed.

def _compute_force_term_1d(rho, phi, dx, boundary, eps):
    """Compute div(rho * grad(phi)) = rho*Lap(phi) + grad(rho).grad(phi) in 1D."""
    lap_phi = discrete_laplacian(phi, dx, boundary, eps)
    rho_p = np.pad(rho, 1, mode='wrap') if boundary == 'periodic' else np.pad(rho, 1, mode='reflect')
    phi_p = np.pad(phi, 1, mode='wrap') if boundary == 'periodic' else np.pad(phi, 1, mode='reflect')
    grad_rho = (rho_p[2:] - rho_p[:-2]) / (2.0 * dx)
    grad_phi = (phi_p[2:] - phi_p[:-2]) / (2.0 * dx)
    return rho * lap_phi + grad_rho * grad_phi


def _compute_force_term_2d(rho, phi, dx, boundary, eps):
    """Compute div(rho * grad(phi)) in 2D."""
    lap_phi = discrete_laplacian(phi, dx, boundary, eps)
    pad_mode = 'wrap' if boundary == 'periodic' else 'reflect'
    rho_p = np.pad(rho, 1, mode=pad_mode)
    phi_p = np.pad(phi, 1, mode=pad_mode)
    two_dx = 2.0 * dx
    grad_rho_x = (rho_p[2:, 1:-1] - rho_p[:-2, 1:-1]) / two_dx
    grad_rho_y = (rho_p[1:-1, 2:] - rho_p[1:-1, :-2]) / two_dx
    grad_phi_x = (phi_p[2:, 1:-1] - phi_p[:-2, 1:-1]) / two_dx
    grad_phi_y = (phi_p[1:-1, 2:] - phi_p[1:-1, :-2]) / two_dx
    return rho * lap_phi + grad_rho_x * grad_phi_x + grad_rho_y * grad_phi_y


def simulate_strong_gmf(
    params: EDParams,
    initial_rho: np.ndarray,
    initial_phi: np.ndarray = None,
    D_phi: float = 1.0,
    mu: float = 0.1,
    kappa: float = 1.0,
    lam: float = 1.0,
    snapshot_interval: int = 500,
    label: str = "",
) -> dict:
    """Simulate the strong-coupling GMF system.

    Like ED-Phys-10 simulate_multifield but with stronger coupling
    and adaptive sub-stepping for stability.
    """
    rho = initial_rho.copy().astype(np.float64)
    d = rho.ndim
    dx = params.dx
    eps = 1e-10

    if initial_phi is None:
        phi = np.zeros_like(rho)
    else:
        phi = initial_phi.copy().astype(np.float64)

    # Timestep: constrained by diffusion, phi diffusion, and coupling
    M_max = params.M_0
    eta_rho = params.cfl_safety * dx**2 / (2 * d * M_max) if M_max > 0 else 1.0
    eta_phi = 0.1 * dx**2 / (2 * d * D_phi) if D_phi > 0 else 1.0
    # Coupling constraint: lam * rho_max * max_grad_phi / dx
    # More conservative for strong coupling
    rho_scale = float(np.max(initial_rho)) + 1.0
    eta_coupling = 0.02 * dx / (lam * rho_scale) if lam > 0 else 1.0
    eta = min(eta_rho, eta_phi, eta_coupling)
    eta = min(eta, 0.005)  # cap for strong coupling safety

    diagnostics = []
    blowup_step = None
    blowup_msg = ""

    force_fn = _compute_force_term_1d if d == 1 else _compute_force_term_2d

    for step in range(params.n_steps):
        if step % 100 == 0:
            ok, msg = _check_blowup(rho, phi=phi, label=label, step=step)
            if not ok:
                blowup_step = step
                blowup_msg = msg
                break

        if step % snapshot_interval == 0:
            rho_safe = np.maximum(rho, eps)
            force = force_fn(rho_safe, phi, dx, params.boundary, eps)
            grad_mag = discrete_grad_magnitude(rho_safe, dx, params.boundary, eps)
            # Curvature force for comparison
            lap_rho = discrete_laplacian(rho_safe, dx, params.boundary, eps)
            M = mobility(rho_safe, params.M_0, params.rho_max, params.n_mob)
            curv_force = M * lap_rho
            diag = {
                'step': step,
                'rho_mean': float(np.mean(rho)),
                'rho_max': float(np.max(rho)),
                'rho_min': float(np.min(rho)),
                'rho_std': float(np.std(rho)),
                'phi_rms': float(np.sqrt(np.mean(phi**2))),
                'phi_max': float(np.max(np.abs(phi))),
                'force_rms': float(np.sqrt(np.mean(force**2))),
                'force_max': float(np.max(np.abs(force))),
                'curv_force_rms': float(np.sqrt(np.mean(curv_force**2))),
                'force_ratio': float(np.sqrt(np.mean(force**2)) / max(np.sqrt(np.mean(curv_force**2)), 1e-20)),
                'grad_mean': float(np.mean(grad_mag)),
            }
            if rho.ndim == 1:
                peaks = []
                for i in range(1, len(rho)-1):
                    if rho[i] > rho[i-1] and rho[i] > rho[i+1] and rho[i] > np.mean(rho) + 0.5*np.std(rho):
                        peaks.append(i)
                diag['n_peaks'] = len(peaks)
                diag['peak_positions'] = peaks[:10]
            diagnostics.append(diag)

        # Compute canonical RHS
        rho_safe = np.maximum(rho, eps)
        lap_rho = discrete_laplacian(rho_safe, dx, params.boundary, eps)
        grad_sq = discrete_grad_squared(rho_safe, dx, params.boundary, eps)
        M = mobility(rho_safe, params.M_0, params.rho_max, params.n_mob)
        Mprime = mobility_derivative(rho_safe, params.M_0, params.rho_max, params.n_mob)

        rhs_canonical = M * lap_rho + Mprime * grad_sq - params.alpha * params.gamma_exp * rho_safe**(params.gamma_exp - 1)

        # Phi evolution: d phi/dt = D_phi*Lap(phi) - mu*phi + kappa*(rho - rho_mean)
        lap_phi = discrete_laplacian(phi, dx, params.boundary, eps)
        rho_bar = float(np.mean(rho))
        dphi_dt = D_phi * lap_phi - mu * phi + kappa * (rho_safe - rho_bar)

        # Force term: -lam * div(rho * grad(phi))
        force = force_fn(rho_safe, phi, dx, params.boundary, eps)

        drho_dt = rhs_canonical - lam * force
        phi_new = phi + eta * dphi_dt
        rho_new = rho + eta * drho_dt

        rho_new = np.maximum(rho_new, eps)

        rho = rho_new
        phi = phi_new

    # Final snapshot
    rho_safe = np.maximum(rho, eps)
    force = force_fn(rho_safe, phi, dx, params.boundary, eps)
    lap_rho = discrete_laplacian(rho_safe, dx, params.boundary, eps)
    M = mobility(rho_safe, params.M_0, params.rho_max, params.n_mob)
    curv_force = M * lap_rho

    final = {
        'step': step if blowup_step is None else blowup_step,
        'rho_mean': float(np.mean(rho)),
        'rho_max': float(np.max(rho)),
        'rho_min': float(np.min(rho)),
        'rho_std': float(np.std(rho)),
        'phi_rms': float(np.sqrt(np.mean(phi**2))),
        'force_rms': float(np.sqrt(np.mean(force**2))),
        'curv_force_rms': float(np.sqrt(np.mean(curv_force**2))),
        'force_ratio': float(np.sqrt(np.mean(force**2)) / max(np.sqrt(np.mean(curv_force**2)), 1e-20)),
    }
    if rho.ndim == 1:
        peaks = []
        for i in range(1, len(rho)-1):
            if rho[i] > rho[i-1] and rho[i] > rho[i+1] and rho[i] > np.mean(rho) + 0.5*np.std(rho):
                peaks.append(i)
        final['n_peaks'] = len(peaks)
        final['peak_positions'] = peaks[:10]

    return {
        'eta_used': eta,
        'blowup_step': blowup_step,
        'blowup_msg': blowup_msg,
        'diagnostics': diagnostics,
        'final': final,
        'rho_final': rho,
        'phi_final': phi,
    }


# ============================================================
# Extension C: Directional Operator (2D only)
# ============================================================
# Modify the phi equation to have anisotropic diffusion:
#   d phi/dt = D_x * d^2 phi/dx^2 + D_y * d^2 phi/dy^2 - mu*phi + kappa*(rho - rho_bar)
# with D_x >> D_y (or D_y = 0) to create directional bias.
#
# Additionally, introduce a directional source:
#   source = kappa * d rho/dx  (x-derivative of rho, not rho itself)
# This breaks isotropy by coupling phi to the gradient direction.

def simulate_directional(
    params: EDParams,
    initial_rho: np.ndarray,
    initial_phi: np.ndarray = None,
    D_phi_x: float = 5.0,
    D_phi_y: float = 0.0,
    mu: float = 0.1,
    kappa: float = 0.1,
    lam: float = 0.1,
    use_grad_source: bool = True,
    snapshot_interval: int = 500,
    label: str = "",
) -> dict:
    """Simulate the directional-operator extension (2D only).

    phi diffuses only in x-direction and is sourced by d(rho)/dx,
    creating a preferred direction.
    """
    assert initial_rho.ndim == 2, "Directional operator requires 2D"

    rho = initial_rho.copy().astype(np.float64)
    d = 2
    dx = params.dx
    eps = 1e-10
    Ny, Nx = rho.shape

    if initial_phi is None:
        phi = np.zeros_like(rho)
    else:
        phi = initial_phi.copy().astype(np.float64)

    # Timestep
    M_max = params.M_0
    D_max = max(D_phi_x, D_phi_y, 1e-12)
    eta_rho = params.cfl_safety * dx**2 / (2 * d * M_max) if M_max > 0 else 1.0
    eta_phi = 0.1 * dx**2 / (2 * D_max) if D_max > 0 else 1.0
    rho_scale = float(np.max(initial_rho)) + 1.0
    eta_coupling = 0.02 * dx / (lam * rho_scale) if lam > 0 else 1.0
    eta = min(eta_rho, eta_phi, eta_coupling, 0.005)

    diagnostics = []
    blowup_step = None
    blowup_msg = ""

    pad_mode = 'wrap' if params.boundary == 'periodic' else 'reflect'

    for step in range(params.n_steps):
        if step % 100 == 0:
            ok, msg = _check_blowup(rho, phi=phi, label=label, step=step)
            if not ok:
                blowup_step = step
                blowup_msg = msg
                break

        if step % snapshot_interval == 0:
            rho_safe = np.maximum(rho, eps)
            # Measure anisotropy: variance of rho along x vs y
            x_profile = np.var(rho, axis=0)  # variance across rows for each column
            y_profile = np.var(rho, axis=1)  # variance across columns for each row
            x_var = float(np.mean(x_profile))
            y_var = float(np.mean(y_profile))

            # Growth rates along x vs y: std of gradient in each direction
            rho_p = np.pad(rho_safe, 1, mode=pad_mode)
            grad_x = (rho_p[2:, 1:-1] - rho_p[:-2, 1:-1]) / (2*dx)
            grad_y = (rho_p[1:-1, 2:] - rho_p[1:-1, :-2]) / (2*dx)

            diag = {
                'step': step,
                'rho_mean': float(np.mean(rho)),
                'rho_max': float(np.max(rho)),
                'rho_std': float(np.std(rho)),
                'phi_rms': float(np.sqrt(np.mean(phi**2))),
                'x_variance': x_var,
                'y_variance': y_var,
                'anisotropy_ratio': x_var / max(y_var, 1e-20),
                'grad_x_rms': float(np.sqrt(np.mean(grad_x**2))),
                'grad_y_rms': float(np.sqrt(np.mean(grad_y**2))),
                'grad_anisotropy': float(np.sqrt(np.mean(grad_x**2)) / max(np.sqrt(np.mean(grad_y**2)), 1e-20)),
            }
            diagnostics.append(diag)

        # Canonical RHS for rho
        rho_safe = np.maximum(rho, eps)
        lap_rho = discrete_laplacian(rho_safe, dx, params.boundary, eps)
        grad_sq = discrete_grad_squared(rho_safe, dx, params.boundary, eps)
        M = mobility(rho_safe, params.M_0, params.rho_max, params.n_mob)
        Mprime = mobility_derivative(rho_safe, params.M_0, params.rho_max, params.n_mob)
        rhs_canonical = M * lap_rho + Mprime * grad_sq - params.alpha * params.gamma_exp * rho_safe**(params.gamma_exp - 1)

        # Anisotropic phi evolution
        phi_p = np.pad(phi, 1, mode=pad_mode)
        lap_phi_x = (phi_p[2:, 1:-1] - 2*phi_p[1:-1, 1:-1] + phi_p[:-2, 1:-1]) / dx**2
        lap_phi_y = (phi_p[1:-1, 2:] - 2*phi_p[1:-1, 1:-1] + phi_p[1:-1, :-2]) / dx**2

        # Source term: either gradient-based or density-based
        rho_bar = float(np.mean(rho))
        if use_grad_source:
            rho_p = np.pad(rho_safe, 1, mode=pad_mode)
            source = kappa * (rho_p[2:, 1:-1] - rho_p[:-2, 1:-1]) / (2*dx)  # d(rho)/dx
        else:
            source = kappa * (rho_safe - rho_bar)

        dphi_dt = D_phi_x * lap_phi_x + D_phi_y * lap_phi_y - mu * phi + source

        # Force term (uses full 2D gradient)
        force = _compute_force_term_2d(rho_safe, phi, dx, params.boundary, eps)

        drho_dt = rhs_canonical - lam * force
        phi_new = phi + eta * dphi_dt
        rho_new = rho + eta * drho_dt
        rho_new = np.maximum(rho_new, eps)

        rho = rho_new
        phi = phi_new

    # Final
    rho_safe = np.maximum(rho, eps)
    rho_p = np.pad(rho_safe, 1, mode=pad_mode)
    grad_x = (rho_p[2:, 1:-1] - rho_p[:-2, 1:-1]) / (2*dx)
    grad_y = (rho_p[1:-1, 2:] - rho_p[1:-1, :-2]) / (2*dx)
    x_var = float(np.mean(np.var(rho, axis=0)))
    y_var = float(np.mean(np.var(rho, axis=1)))

    final = {
        'step': step if blowup_step is None else blowup_step,
        'rho_mean': float(np.mean(rho)),
        'rho_max': float(np.max(rho)),
        'rho_std': float(np.std(rho)),
        'phi_rms': float(np.sqrt(np.mean(phi**2))),
        'x_variance': x_var,
        'y_variance': y_var,
        'anisotropy_ratio': x_var / max(y_var, 1e-20),
        'grad_x_rms': float(np.sqrt(np.mean(grad_x**2))),
        'grad_y_rms': float(np.sqrt(np.mean(grad_y**2))),
        'grad_anisotropy': float(np.sqrt(np.mean(grad_x**2)) / max(np.sqrt(np.mean(grad_y**2)), 1e-20)),
    }

    return {
        'eta_used': eta,
        'blowup_step': blowup_step,
        'blowup_msg': blowup_msg,
        'diagnostics': diagnostics,
        'final': final,
        'rho_final': rho,
        'phi_final': phi,
    }


# ============================================================
# Experiment runner
# ============================================================

def run_nondissipative_experiments(output_dir="results"):
    os.makedirs(output_dir, exist_ok=True)
    all_results = {}
    t_total = time.time()

    # ========================================================
    # EXP A1: Hyperbolic Wave Test (1D, N=512, 50K steps)
    # ========================================================
    print("\n>>> EXP A1: Hyperbolic Wave Test -- low damping (1D)")
    exp_a1 = []

    # Key insight from ED-Phys-09: at canonical params, zeta_eff from
    # the canonical PDE ~ O(1). We need zeta << 1 AND tau chosen so
    # that Q = sqrt(M*k^2 / tau) / zeta > 1.
    # Characteristic k ~ 2*pi/512 ~ 0.012, M ~ 1.0
    # omega ~ sqrt(M*k^2/tau) = sqrt(1.0 * 0.00015 / tau) = sqrt(0.00015/tau)
    # For tau=0.001: omega ~ 0.39, Q = omega/zeta
    # Need zeta < 0.39 for Q > 1 => try zeta = 0.001 to 0.1

    for tau in [0.001, 0.01, 0.1]:
        for zeta in [0.001, 0.01, 0.1]:
            Q_est = np.sqrt(1.0 * (2*np.pi/512)**2 / tau) / max(zeta, 1e-12)
            p = EDParams(
                alpha=0.1, gamma_exp=0.5, M_0=1.0, rho_max=100.0, n_mob=2,
                dimensions=1, N=512, dx=1.0, cfl_safety=0.4,
                n_steps=50000, record_interval=500, boundary="periodic",
            )
            # IC: sharp Gaussian pulse on uniform background
            x = np.arange(512, dtype=np.float64)
            rho0 = 5.0 + 15.0 * np.exp(-(x - 256)**2 / (2 * 10**2))

            label = f"hyp_t{tau}_z{zeta}"
            t0 = time.time()
            result = simulate_hyperbolic(p, rho0, tau=tau, zeta=zeta,
                                         snapshot_interval=500, label=label)
            elapsed = time.time() - t0

            # Analyze: did the peak move? Any new peaks? Oscillations?
            diags = result['diagnostics']
            init_peaks = diags[0].get('peak_positions', [])
            final_peaks = result['final'].get('peak_positions', [])
            init_n = diags[0].get('n_peaks', 0)
            final_n = result['final'].get('n_peaks', 0)

            # Check for v oscillations: does v_rms have local maxima?
            v_rms_series = [d['v_rms'] for d in diags]
            n_oscillations = 0
            for i in range(1, len(v_rms_series)-1):
                if v_rms_series[i] > v_rms_series[i-1] and v_rms_series[i] > v_rms_series[i+1]:
                    n_oscillations += 1

            # Peak displacement
            peak_shift = 0
            if init_peaks and final_peaks:
                peak_shift = abs(final_peaks[0] - init_peaks[0])

            entry = {
                'tau': tau, 'zeta': zeta, 'Q_est': round(Q_est, 2),
                'eta_used': result['eta_used'],
                'elapsed_s': round(elapsed, 1),
                'blowup': result['blowup_step'],
                'v_rms_final': result['final']['v_rms'],
                'v_max_final': result['final']['v_max'],
                'KE_final': result['final']['kinetic_energy'],
                'peaks_initial': init_n, 'peaks_final': final_n,
                'peak_shift': peak_shift,
                'v_sign_changes_final': diags[-1].get('v_sign_changes', 0) if diags else 0,
                'n_oscillations': n_oscillations,
                'rho_max_final': result['final']['rho_max'],
                'rho_min_final': result['final']['rho_min'],
            }
            exp_a1.append(entry)
            status = "BLOWUP" if result['blowup_step'] else "ok"
            print(f"  {label}... {status} ({elapsed:.1f}s) Q~{Q_est:.1f} v_rms={result['final']['v_rms']:.4f} "
                  f"peaks={init_n}->{final_n} shift={peak_shift} osc={n_oscillations}")

    all_results['exp_a1_hyperbolic_wave'] = exp_a1

    # ========================================================
    # EXP A2: Hyperbolic Oscillation Test (sinusoidal IC)
    # ========================================================
    print("\n>>> EXP A2: Hyperbolic Oscillation Test -- sinusoidal IC (1D)")
    exp_a2 = []
    for tau in [0.001, 0.01]:
        for zeta in [0.001, 0.01]:
            p = EDParams(
                alpha=0.1, gamma_exp=0.5, M_0=1.0, rho_max=100.0, n_mob=2,
                dimensions=1, N=512, dx=1.0, cfl_safety=0.4,
                n_steps=50000, record_interval=500, boundary="periodic",
            )
            x = np.arange(512, dtype=np.float64)
            rho0 = 5.0 + 3.0 * np.sin(2 * np.pi * x / 512) + 1.5 * np.sin(4 * np.pi * x / 512)
            rho0 = np.maximum(rho0, 0.01)

            label = f"osc_t{tau}_z{zeta}"
            t0 = time.time()
            result = simulate_hyperbolic(p, rho0, tau=tau, zeta=zeta,
                                         snapshot_interval=500, label=label)
            elapsed = time.time() - t0

            diags = result['diagnostics']
            v_rms_series = [d['v_rms'] for d in diags]
            n_oscillations = 0
            for i in range(1, len(v_rms_series)-1):
                if v_rms_series[i] > v_rms_series[i-1] and v_rms_series[i] > v_rms_series[i+1]:
                    n_oscillations += 1

            # Check gradient energy oscillation
            grad_series = [d['grad_mean'] for d in diags]
            grad_osc = 0
            for i in range(1, len(grad_series)-1):
                if grad_series[i] > grad_series[i-1] and grad_series[i] > grad_series[i+1]:
                    grad_osc += 1

            entry = {
                'tau': tau, 'zeta': zeta,
                'elapsed_s': round(elapsed, 1),
                'blowup': result['blowup_step'],
                'v_rms_final': result['final']['v_rms'],
                'n_v_oscillations': n_oscillations,
                'n_grad_oscillations': grad_osc,
                'rho_std_final': result['final']['rho_std'],
                'grad_mean_final': result['final']['grad_mean'],
            }
            exp_a2.append(entry)
            status = "BLOWUP" if result['blowup_step'] else "ok"
            print(f"  {label}... {status} ({elapsed:.1f}s) v_osc={n_oscillations} grad_osc={grad_osc} v_rms={result['final']['v_rms']:.4f}")

    all_results['exp_a2_hyperbolic_oscillation'] = exp_a2

    # ========================================================
    # EXP A3: Hyperbolic Stability Test (50K steps, extreme params)
    # ========================================================
    print("\n>>> EXP A3: Hyperbolic Stability Test -- extreme low damping")
    exp_a3 = []
    for tau in [0.001, 0.0001]:
        for zeta in [0.0001, 0.001]:
            p = EDParams(
                alpha=0.1, gamma_exp=0.5, M_0=1.0, rho_max=100.0, n_mob=2,
                dimensions=1, N=512, dx=1.0, cfl_safety=0.4,
                n_steps=50000, record_interval=1000, boundary="periodic",
            )
            x = np.arange(512, dtype=np.float64)
            rho0 = 5.0 + 10.0 * np.exp(-(x - 256)**2 / (2 * 15**2))

            label = f"stab_t{tau}_z{zeta}"
            t0 = time.time()
            result = simulate_hyperbolic(p, rho0, tau=tau, zeta=zeta,
                                         snapshot_interval=1000, label=label)
            elapsed = time.time() - t0

            entry = {
                'tau': tau, 'zeta': zeta,
                'elapsed_s': round(elapsed, 1),
                'blowup': result['blowup_step'],
                'blowup_msg': result['blowup_msg'],
                'rho_max_final': result['final']['rho_max'],
                'rho_min_final': result['final']['rho_min'],
                'v_rms_final': result['final']['v_rms'],
                'v_max_final': result['final']['v_max'],
            }
            exp_a3.append(entry)
            status = f"BLOWUP@{result['blowup_step']}" if result['blowup_step'] else "ok"
            print(f"  {label}... {status} ({elapsed:.1f}s) rho=[{result['final']['rho_min']:.2f},{result['final']['rho_max']:.2f}] v_max={result['final']['v_max']:.4f}")

    all_results['exp_a3_hyperbolic_stability'] = exp_a3

    # ========================================================
    # EXP B1: Strong GMF -- Force Test (two peaks, 1D)
    # ========================================================
    print("\n>>> EXP B1: Strong GMF Force Test -- two peaks (1D)")
    exp_b1 = []
    for kappa in [0.5, 1.0, 2.0, 5.0]:
        for lam in [0.5, 1.0, 2.0]:
            p = EDParams(
                alpha=0.1, gamma_exp=0.5, M_0=1.0, rho_max=100.0, n_mob=2,
                dimensions=1, N=512, dx=1.0, cfl_safety=0.4,
                n_steps=30000, record_interval=500, boundary="periodic",
            )
            x = np.arange(512, dtype=np.float64)
            rho0 = 2.0 + 15.0*np.exp(-(x-179)**2/(2*15**2)) + 15.0*np.exp(-(x-332)**2/(2*15**2))

            label = f"force_k{kappa}_l{lam}"
            t0 = time.time()
            result = simulate_strong_gmf(p, rho0, kappa=kappa, lam=lam,
                                          D_phi=1.0, mu=0.1,
                                          snapshot_interval=500, label=label)
            elapsed = time.time() - t0

            diags = result['diagnostics']
            init_peaks = diags[0].get('peak_positions', []) if diags else []
            final_peaks = result['final'].get('peak_positions', [])
            init_sep = abs(init_peaks[1] - init_peaks[0]) if len(init_peaks) >= 2 else 0
            final_sep = abs(final_peaks[1] - final_peaks[0]) if len(final_peaks) >= 2 else 0

            # Track separation over time
            sep_series = []
            for d_entry in diags:
                pp = d_entry.get('peak_positions', [])
                if len(pp) >= 2:
                    sep_series.append(abs(pp[1] - pp[0]))
                else:
                    sep_series.append(0)

            # Force vs curvature comparison
            force_ratio_final = result['final'].get('force_ratio', 0)

            entry = {
                'kappa': kappa, 'lam': lam,
                'elapsed_s': round(elapsed, 1),
                'blowup': result['blowup_step'],
                'blowup_msg': result['blowup_msg'],
                'peaks_initial': diags[0].get('n_peaks', 0) if diags else 0,
                'peaks_final': result['final'].get('n_peaks', 0),
                'sep_initial': init_sep,
                'sep_final': final_sep,
                'sep_change': final_sep - init_sep if init_sep > 0 and final_sep > 0 else None,
                'force_rms_final': result['final']['force_rms'],
                'curv_force_rms_final': result['final']['curv_force_rms'],
                'force_ratio': force_ratio_final,
                'sep_series': sep_series,
            }
            exp_b1.append(entry)
            status = f"BLOWUP@{result['blowup_step']}" if result['blowup_step'] else "ok"
            sc = f"sep={init_sep}->{final_sep}" if init_sep > 0 else "peaks lost"
            print(f"  {label}... {status} ({elapsed:.1f}s) {sc} F/curv={force_ratio_final:.3f} F_rms={result['final']['force_rms']:.4f}")

    all_results['exp_b1_strong_gmf_force'] = exp_b1

    # ========================================================
    # EXP B2: Strong GMF -- Cosmology modification (1D)
    # ========================================================
    print("\n>>> EXP B2: Strong GMF Cosmology -- inflation modification (1D)")
    exp_b2 = []
    np.random.seed(42)
    rho0_cosmo = np.random.uniform(0.1, 10.0, 512).astype(np.float64)

    for kappa, lam in [(0, 0), (0.5, 0.5), (1.0, 1.0), (2.0, 2.0), (5.0, 5.0)]:
        p = EDParams(
            alpha=0.1, gamma_exp=0.5, M_0=1.0, rho_max=100.0, n_mob=2,
            dimensions=1, N=512, dx=1.0, cfl_safety=0.4,
            n_steps=30000, record_interval=300, boundary="periodic",
        )
        label = f"cosmo_k{kappa}_l{lam}"
        t0 = time.time()
        result = simulate_strong_gmf(p, rho0_cosmo.copy(), kappa=kappa, lam=lam,
                                      D_phi=1.0, mu=0.1,
                                      snapshot_interval=300, label=label)
        elapsed = time.time() - t0

        diags = result['diagnostics']
        # Fit lambda_1 from grad_mean time series
        grad_series = [(d['step'], d['grad_mean']) for d in diags if d['grad_mean'] > 1e-8]
        lambda_1 = 0.0
        r_squared = 0.0
        if len(grad_series) > 5:
            steps = np.array([g[0] for g in grad_series])
            grads = np.array([g[1] for g in grad_series])
            log_grads = np.log(grads + 1e-20)
            # Linear fit: log(G) = -lambda_1 * step + c
            if len(steps) > 2:
                coeffs = np.polyfit(steps, log_grads, 1)
                lambda_1 = -coeffs[0]
                predicted = np.polyval(coeffs, steps)
                ss_res = np.sum((log_grads - predicted)**2)
                ss_tot = np.sum((log_grads - np.mean(log_grads))**2)
                r_squared = 1 - ss_res / max(ss_tot, 1e-20)

        # Basin count (using gradient threshold)
        rho_f = result['rho_final']
        grad_f = discrete_grad_magnitude(np.maximum(rho_f, 1e-10), 1.0, 'periodic', 1e-10)
        basins_final = int(np.sum(grad_f < 0.01))

        entry = {
            'kappa': kappa, 'lam': lam,
            'elapsed_s': round(elapsed, 1),
            'blowup': result['blowup_step'],
            'blowup_msg': result['blowup_msg'],
            'lambda_1': round(lambda_1, 5),
            'r_squared': round(r_squared, 4),
            'rho_std_final': result['final']['rho_std'],
            'rho_max_final': result['final']['rho_max'],
        }
        exp_b2.append(entry)
        status = f"BLOWUP@{result['blowup_step']}" if result['blowup_step'] else "ok"
        print(f"  {label}... {status} ({elapsed:.1f}s) lam1={lambda_1:.5f} R2={r_squared:.4f}")

    all_results['exp_b2_strong_gmf_cosmology'] = exp_b2

    # ========================================================
    # EXP B3: Strong GMF -- Stability boundary (1D, 50K steps)
    # ========================================================
    print("\n>>> EXP B3: Strong GMF Stability -- long-time (1D, 50K steps)")
    exp_b3 = []
    for kappa, lam in [(1.0, 1.0), (5.0, 5.0), (10.0, 10.0), (20.0, 20.0)]:
        p = EDParams(
            alpha=0.1, gamma_exp=0.5, M_0=1.0, rho_max=100.0, n_mob=2,
            dimensions=1, N=512, dx=1.0, cfl_safety=0.4,
            n_steps=50000, record_interval=1000, boundary="periodic",
        )
        x = np.arange(512, dtype=np.float64)
        rho0 = 5.0 + 10.0 * np.exp(-(x - 256)**2 / (2 * 20**2))

        label = f"stab_k{kappa}_l{lam}"
        t0 = time.time()
        result = simulate_strong_gmf(p, rho0, kappa=kappa, lam=lam,
                                      D_phi=1.0, mu=0.1,
                                      snapshot_interval=1000, label=label)
        elapsed = time.time() - t0

        entry = {
            'kappa': kappa, 'lam': lam,
            'elapsed_s': round(elapsed, 1),
            'blowup': result['blowup_step'],
            'blowup_msg': result['blowup_msg'],
            'rho_max_final': result['final']['rho_max'],
            'rho_min_final': result['final']['rho_min'],
            'force_ratio': result['final'].get('force_ratio', 0),
        }
        exp_b3.append(entry)
        status = f"BLOWUP@{result['blowup_step']}" if result['blowup_step'] else "ok"
        print(f"  {label}... {status} ({elapsed:.1f}s) rho=[{result['final']['rho_min']:.2f},{result['final']['rho_max']:.2f}] F/curv={result['final'].get('force_ratio',0):.3f}")

    all_results['exp_b3_strong_gmf_stability'] = exp_b3

    # ========================================================
    # EXP C1: Directional Operator -- anisotropy (2D, 128x128)
    # ========================================================
    print("\n>>> EXP C1: Directional Operator -- anisotropy test (2D)")
    exp_c1 = []
    np.random.seed(99)
    rho0_2d = np.random.uniform(0.1, 10.0, (128, 128)).astype(np.float64)

    configs = [
        # (D_x, D_y, kappa, lam, use_grad_source, name)
        (1.0, 1.0, 0.1, 0.1, False, "isotropic_control"),
        (5.0, 0.0, 0.1, 0.1, True, "dir_Dx5_Dy0_grad"),
        (5.0, 0.0, 0.5, 0.5, True, "dir_Dx5_Dy0_strong"),
        (10.0, 0.0, 1.0, 1.0, True, "dir_Dx10_Dy0_vstrong"),
        (5.0, 0.0, 0.5, 0.5, False, "dir_Dx5_Dy0_dens_source"),
    ]

    for D_x, D_y, kappa, lam, grad_src, name in configs:
        p = EDParams(
            alpha=0.1, gamma_exp=0.5, M_0=1.0, rho_max=100.0, n_mob=2,
            dimensions=2, N=128, dx=1.0, cfl_safety=0.4,
            n_steps=10000, record_interval=500, boundary="periodic",
        )
        label = f"dir_{name}"
        t0 = time.time()
        result = simulate_directional(p, rho0_2d.copy(), D_phi_x=D_x, D_phi_y=D_y,
                                       kappa=kappa, lam=lam, mu=0.1,
                                       use_grad_source=grad_src,
                                       snapshot_interval=500, label=label)
        elapsed = time.time() - t0

        entry = {
            'name': name, 'D_phi_x': D_x, 'D_phi_y': D_y,
            'kappa': kappa, 'lam': lam, 'grad_source': grad_src,
            'elapsed_s': round(elapsed, 1),
            'blowup': result['blowup_step'],
            'blowup_msg': result['blowup_msg'],
            'anisotropy_ratio': result['final']['anisotropy_ratio'],
            'x_variance': result['final']['x_variance'],
            'y_variance': result['final']['y_variance'],
            'grad_anisotropy': result['final']['grad_anisotropy'],
            'grad_x_rms': result['final']['grad_x_rms'],
            'grad_y_rms': result['final']['grad_y_rms'],
            'phi_rms': result['final']['phi_rms'],
            'rho_std': result['final']['rho_std'],
        }
        exp_c1.append(entry)
        status = f"BLOWUP@{result['blowup_step']}" if result['blowup_step'] else "ok"
        print(f"  {name}... {status} ({elapsed:.1f}s) aniso={result['final']['anisotropy_ratio']:.4f} "
              f"grad_aniso={result['final']['grad_anisotropy']:.4f} phi_rms={result['final']['phi_rms']:.4f}")

        # Save 2D snapshots
        if result['blowup_step'] is None:
            np.save(os.path.join(output_dir, f"2d_{name}_rho.npy"), result['rho_final'])
            np.save(os.path.join(output_dir, f"2d_{name}_phi.npy"), result['phi_final'])

    all_results['exp_c1_directional'] = exp_c1

    # ========================================================
    # EXP C2: Directional Operator -- stability (2D, long run)
    # ========================================================
    print("\n>>> EXP C2: Directional Operator -- stability (2D, 20K steps)")
    exp_c2 = []
    for D_x, kappa, lam in [(10.0, 1.0, 1.0), (20.0, 2.0, 2.0)]:
        p = EDParams(
            alpha=0.1, gamma_exp=0.5, M_0=1.0, rho_max=100.0, n_mob=2,
            dimensions=2, N=128, dx=1.0, cfl_safety=0.4,
            n_steps=20000, record_interval=1000, boundary="periodic",
        )
        name = f"dir_stab_Dx{D_x}_k{kappa}_l{lam}"
        label = name
        t0 = time.time()
        result = simulate_directional(p, rho0_2d.copy(), D_phi_x=D_x, D_phi_y=0.0,
                                       kappa=kappa, lam=lam, mu=0.1,
                                       use_grad_source=True,
                                       snapshot_interval=1000, label=label)
        elapsed = time.time() - t0

        # Track anisotropy over time
        aniso_series = [d['anisotropy_ratio'] for d in result['diagnostics']]
        grad_aniso_series = [d['grad_anisotropy'] for d in result['diagnostics']]

        entry = {
            'name': name, 'D_phi_x': D_x, 'kappa': kappa, 'lam': lam,
            'elapsed_s': round(elapsed, 1),
            'blowup': result['blowup_step'],
            'blowup_msg': result['blowup_msg'],
            'anisotropy_final': result['final']['anisotropy_ratio'],
            'grad_anisotropy_final': result['final']['grad_anisotropy'],
            'aniso_series': [round(a, 4) for a in aniso_series],
            'grad_aniso_series': [round(a, 4) for a in grad_aniso_series],
        }
        exp_c2.append(entry)
        status = f"BLOWUP@{result['blowup_step']}" if result['blowup_step'] else "ok"
        print(f"  {name}... {status} ({elapsed:.1f}s) aniso={result['final']['anisotropy_ratio']:.4f} "
              f"grad_aniso={result['final']['grad_anisotropy']:.4f}")

    all_results['exp_c2_directional_stability'] = exp_c2

    # ========================================================
    # Save all results
    # ========================================================
    elapsed_total = time.time() - t_total
    results_path = os.path.join(output_dir, "nondissipative_results.json")
    with open(results_path, 'w') as f:
        json.dump(all_results, f, indent=2, default=str)

    print(f"\n{'='*70}")
    print(f"  All ED-Phys-11 experiments complete in {elapsed_total:.1f}s")
    print(f"  Results saved to {os.path.abspath(results_path)}")
    print(f"{'='*70}")


# ============================================================
# Main
# ============================================================

if __name__ == "__main__":
    print("=" * 70)
    print("  ED-Phys-11: Non-Dissipative and Strong-Coupling Regimes")
    print("=" * 70)
    output_dir = os.path.join(os.path.dirname(__file__), "results")
    run_nondissipative_experiments(output_dir=output_dir)
