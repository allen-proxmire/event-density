"""
invariants_2d.py
================
2D invariant atlas for the canonical Event Density PDE.

Extends the 1D invariant suite (edsim_diagnostics.py, 16 invariant families)
into two spatial dimensions, and introduces new invariants that exist only in 2D.

Organisation:
  A. Spectral invariants    — modal amplitudes, entropy, complexity, geometric norms
  B. Dynamical invariants   — dissipation channels, decay rates, Lyapunov-like growth
  C. Geometric invariants   — vorticity, filamentarity, anisotropy, curvature, horizons
  D. Correlation invariants — structure functions, correlation lengths
  E. Top-level dispatchers  — compute_invariants_2d(), etc.

All notation follows Appendix C of the Rigour Paper and the Simulation Suite.
"""

import numpy as np
from typing import Dict, Optional, Tuple
from scipy.fft import dctn
from scipy.ndimage import gaussian_filter


# =====================================================================
#  HELPERS
# =====================================================================

def _trap_2d(f: np.ndarray, hx: float, hy: float) -> float:
    """2D trapezoidal integral of f on a uniform grid."""
    Nx, Ny = f.shape
    wx = np.ones(Nx); wx[0] = 0.5; wx[-1] = 0.5
    wy = np.ones(Ny); wy[0] = 0.5; wy[-1] = 0.5
    return hx * hy * np.einsum('i,ij,j->', wx, f, wy)


def _pad_neumann(rho: np.ndarray) -> np.ndarray:
    """One-cell Neumann ghost padding."""
    return np.pad(rho, 1, mode='reflect')


def _grad_components(rho: np.ndarray, hx: float, hy: float):
    """Central-difference gradient components (drho/dx, drho/dy) with Neumann BCs."""
    p = _pad_neumann(rho)
    gx = (p[2:, 1:-1] - p[:-2, 1:-1]) / (2.0 * hx)
    gy = (p[1:-1, 2:] - p[1:-1, :-2]) / (2.0 * hy)
    return gx, gy


# =====================================================================
#  A. SPECTRAL INVARIANTS
# =====================================================================

def modal_amplitudes_2d(rho: np.ndarray, rho_star: float,
                        Lx: float, Ly: float,
                        Kx_max: int = 16, Ky_max: int = 16) -> np.ndarray:
    """
    2D modal amplitudes a_{kx,ky} via DCT-I (Neumann basis).

    The perturbation u = rho - rho* is expanded as:
      u(x,y) = sum_{kx,ky} a_{kx,ky} phi_{kx}(x) phi_{ky}(y)

    where phi_k are the 1D Neumann eigenfunctions.  Amplitudes are
    L^2-normalised so that sum |a_{kx,ky}|^2 = ||u||^2_{L^2}.

    Returns shape (Kx_max, Ky_max).
    """
    u = rho - rho_star
    Nx, Ny = u.shape

    # Raw DCT-I coefficients
    raw = dctn(u, type=1)
    coeffs = raw / ((Nx - 1) * (Ny - 1))
    coeffs[0, :] /= 2.0
    if Nx > 1:
        coeffs[-1, :] /= 2.0
    coeffs[:, 0] /= 2.0
    if Ny > 1:
        coeffs[:, -1] /= 2.0

    Kx = min(Kx_max, Nx)
    Ky = min(Ky_max, Ny)
    a = np.zeros((Kx, Ky))

    # L^2 normalisation factors
    for kx in range(Kx):
        for ky in range(Ky):
            norm_x = np.sqrt(Lx) if kx == 0 else np.sqrt(Lx / 2.0)
            norm_y = np.sqrt(Ly) if ky == 0 else np.sqrt(Ly / 2.0)
            if kx < coeffs.shape[0] and ky < coeffs.shape[1]:
                a[kx, ky] = coeffs[kx, ky] * norm_x * norm_y

    return a


def modal_energy_spectrum_2d(a: np.ndarray) -> np.ndarray:
    """
    Modal energy spectrum: E_{kx,ky} = |a_{kx,ky}|^2.

    Parseval identity: sum E_{kx,ky} = ||u||^2_{L^2}.
    """
    return a ** 2


def spectral_entropy_2d(a: np.ndarray, floor: float = 1e-30) -> float:
    """
    2D Shannon spectral entropy.

      H = -sum_{kx,ky} p_{kx,ky} log(p_{kx,ky})

    where p_{kx,ky} = E_{kx,ky} / E_total is the normalised modal energy.
    H = 0 when all energy is in one mode; H = log(K) for uniform distribution.
    """
    E = a ** 2
    E_total = np.sum(E)
    if E_total < floor:
        return 0.0
    p = E / E_total
    p = np.maximum(p, floor)
    return -np.sum(p * np.log(p))


def spectral_entropy_radial(a: np.ndarray, Lx: float, Ly: float,
                            n_bins: int = 16, floor: float = 1e-30) -> Tuple[np.ndarray, np.ndarray]:
    """
    Radial spectral entropy: bin modal energy by wavenumber magnitude |k|.

    Returns (k_bins, H_radial) where H_radial is computed from the
    binned energy distribution.
    """
    Kx, Ky = a.shape
    E = a ** 2

    # Wavenumber magnitudes
    kx = np.arange(Kx) * np.pi / Lx
    ky = np.arange(Ky) * np.pi / Ly
    KX, KY = np.meshgrid(kx, ky, indexing='ij')
    k_mag = np.sqrt(KX**2 + KY**2)

    k_max = k_mag.max()
    bin_edges = np.linspace(0, k_max, n_bins + 1)
    binned_E = np.zeros(n_bins)

    for b in range(n_bins):
        mask = (k_mag >= bin_edges[b]) & (k_mag < bin_edges[b + 1])
        binned_E[b] = np.sum(E[mask])

    E_total = np.sum(binned_E)
    if E_total < floor:
        return 0.5 * (bin_edges[:-1] + bin_edges[1:]), np.zeros(n_bins)

    p = binned_E / E_total
    p = np.maximum(p, floor)
    H = -np.sum(p * np.log(p))

    return 0.5 * (bin_edges[:-1] + bin_edges[1:]), binned_E


def renyi_entropy_2d(a: np.ndarray, q: float, floor: float = 1e-30) -> float:
    """
    2D Renyi entropy of order q.

      H_q = (1/(1-q)) log(sum p_k^q)     for q != 1
      H_1 = Shannon entropy               for q = 1
    """
    if abs(q - 1.0) < 1e-10:
        return spectral_entropy_2d(a, floor)
    E = a ** 2
    E_total = np.sum(E)
    if E_total < floor:
        return 0.0
    p = E / E_total
    p = np.maximum(p, floor)
    return np.log(np.sum(p ** q)) / (1.0 - q)


def geometric_norms_2d(a: np.ndarray, Lx: float, Ly: float,
                       alphas: list = None) -> Dict[float, float]:
    """
    Weighted spectral norms (geometric norms).

      G_alpha = sum_{(kx,ky) != (0,0)} |k|^{2*alpha} |a_{kx,ky}|^2

    where |k|^2 = (kx pi/Lx)^2 + (ky pi/Ly)^2.
    Negative alpha -> large-scale structure; positive alpha -> gradient structure.
    """
    if alphas is None:
        alphas = [-2, -1, 0, 1, 2, 3, 4]

    Kx, Ky = a.shape
    kx = np.arange(Kx) * np.pi / Lx
    ky = np.arange(Ky) * np.pi / Ly
    KX, KY = np.meshgrid(kx, ky, indexing='ij')
    k_sq = KX**2 + KY**2
    E = a ** 2

    result = {}
    for alpha in alphas:
        weight = np.where(k_sq > 0, k_sq ** alpha, 0.0)
        result[alpha] = float(np.sum(weight * E))
    return result


def modal_complexity_2d(a: np.ndarray, Lx: float, Ly: float) -> float:
    """
    2D ED-complexity (spectral form): C_ED = sum mu_{kx,ky} |a_{kx,ky}|^2.

    This equals the G_1 geometric norm and also equals integral |grad u|^2 dA
    by Parseval's theorem.
    """
    return geometric_norms_2d(a, Lx, Ly, alphas=[1])[1]


def spectral_anisotropy(a: np.ndarray, Lx: float, Ly: float) -> Dict[str, float]:
    """
    Spectral anisotropy: ratio of energy in x-modes vs y-modes.

      A_spec = (E_x - E_y) / (E_x + E_y)

    where E_x = sum_{kx>0, ky=0} E_{kx,0} and E_y = sum_{kx=0, ky>0} E_{0,ky}.

    A_spec = 0 for isotropic fields, +1 for pure x-modes, -1 for pure y-modes.

    Also computes the spectral eccentricity via the inertia tensor of
    the spectral energy distribution.
    """
    E = a ** 2
    Kx, Ky = a.shape

    E_x = np.sum(E[1:, 0]) if Kx > 1 else 0.0
    E_y = np.sum(E[0, 1:]) if Ky > 1 else 0.0
    E_diag = np.sum(E[1:, 1:]) if Kx > 1 and Ky > 1 else 0.0
    denom = E_x + E_y + E_diag
    A_spec = (E_x - E_y) / max(denom, 1e-30)

    # Spectral inertia tensor
    kx_arr = np.arange(Kx) * np.pi / Lx
    ky_arr = np.arange(Ky) * np.pi / Ly
    KX, KY = np.meshgrid(kx_arr, ky_arr, indexing='ij')
    E_total = max(np.sum(E), 1e-30)

    Ixx = np.sum(KX**2 * E) / E_total
    Iyy = np.sum(KY**2 * E) / E_total
    Ixy = np.sum(KX * KY * E) / E_total

    # Eccentricity from eigenvalues
    trace = Ixx + Iyy
    det = Ixx * Iyy - Ixy**2
    disc = max(trace**2 - 4 * det, 0.0)
    lam1 = 0.5 * (trace + np.sqrt(disc))
    lam2 = 0.5 * (trace - np.sqrt(disc))
    eccentricity = 1.0 - min(lam1, lam2) / max(max(lam1, lam2), 1e-30)

    return {
        'anisotropy': A_spec,
        'eccentricity': eccentricity,
        'E_x': E_x,
        'E_y': E_y,
        'E_diagonal': E_diag,
        'Ixx': Ixx, 'Iyy': Iyy, 'Ixy': Ixy,
    }


def modal_hierarchy_2d(a: np.ndarray, Lx: float, Ly: float) -> Dict[str, object]:
    """
    Modal energy hierarchy: sort modes by radial wavenumber and check
    that energy decays monotonically with |k|.

    Returns dict with:
      'radial_spectrum': (k_bins, E_binned)
      'is_monotone': bool
      'decay_rate': fitted slope of log(E) vs log(|k|)
    """
    Kx, Ky = a.shape
    E = a ** 2

    kx = np.arange(Kx) * np.pi / Lx
    ky = np.arange(Ky) * np.pi / Ly
    KX, KY = np.meshgrid(kx, ky, indexing='ij')
    k_mag = np.sqrt(KX**2 + KY**2).ravel()
    E_flat = E.ravel()

    # Sort by |k| and bin
    order = np.argsort(k_mag)
    k_sorted = k_mag[order]
    E_sorted = E_flat[order]

    # Skip k=0 mode
    mask = k_sorted > 0
    k_pos = k_sorted[mask]
    E_pos = E_sorted[mask]

    n_bins = min(20, len(k_pos) // 2)
    if n_bins < 2:
        return {'radial_spectrum': (np.array([]), np.array([])),
                'is_monotone': True, 'decay_rate': 0.0}

    bin_edges = np.linspace(k_pos[0], k_pos[-1], n_bins + 1)
    k_bins = 0.5 * (bin_edges[:-1] + bin_edges[1:])
    E_binned = np.zeros(n_bins)
    for b in range(n_bins):
        m = (k_pos >= bin_edges[b]) & (k_pos < bin_edges[b + 1])
        E_binned[b] = np.sum(E_pos[m])

    is_mono = all(E_binned[i] >= E_binned[i+1] for i in range(n_bins - 1)
                  if E_binned[i] > 1e-30)

    # Power-law fit: log(E) = -beta * log(k) + const
    mask_fit = E_binned > 1e-30
    if np.sum(mask_fit) >= 3:
        log_k = np.log(k_bins[mask_fit])
        log_E = np.log(E_binned[mask_fit])
        A = np.column_stack([log_k, np.ones_like(log_k)])
        coeff, _, _, _ = np.linalg.lstsq(A, log_E, rcond=None)
        decay_rate = -coeff[0]
    else:
        decay_rate = 0.0

    return {
        'radial_spectrum': (k_bins, E_binned),
        'is_monotone': is_mono,
        'decay_rate': decay_rate,
    }


# =====================================================================
#  B. DYNAMICAL INVARIANTS
# =====================================================================

def ed_complexity_2d(rho: np.ndarray, hx: float, hy: float) -> float:
    """
    Bare ED-complexity: C_ED = integral |grad rho|^2 dA.
    """
    gx, gy = _grad_components(rho, hx, hy)
    return _trap_2d(gx**2 + gy**2, hx, hy)


def ed_complexity_effective_2d(rho: np.ndarray, hx: float, hy: float,
                               params) -> float:
    """
    Effective ED-complexity: C_ED^eff = integral (P'(rho)/M(rho)) |grad rho|^2 dA.
    """
    gx, gy = _grad_components(rho, hx, hy)
    gs = gx**2 + gy**2
    P_prime = np.full_like(rho, params.P0)
    M_vals = np.maximum(params.M(rho), 1e-15)
    return _trap_2d((P_prime / M_vals) * gs, hx, hy)


def dissipation_channels_2d(rho: np.ndarray, v: float, params) -> Dict[str, float]:
    """
    Three dissipation channels in 2D.

      D_grad = D * P*' * C_ED
      D_pen  = D * P*'^2 / M* * integral (rho - rho*)^2 dA
      D_part = H * zeta * v^2

    Returns dict with 'gradient', 'penalty', 'participation', 'total'.
    """
    C_ED = ed_complexity_2d(rho, params.hx, params.hy)
    D_grad = params.D * params.P_star_prime * C_ED

    dev_sq = (rho - params.rho_star) ** 2
    int_dev_sq = _trap_2d(dev_sq, params.hx, params.hy)
    D_pen = params.D * params.P_star_prime**2 / params.M_star * int_dev_sq

    D_part = params.H * params.zeta * v ** 2

    return {
        'gradient': D_grad,
        'penalty': D_pen,
        'participation': D_part,
        'total': D_grad + D_pen + D_part,
    }


def dissipation_ratios_2d(rho: np.ndarray, v: float, params) -> Dict[str, float]:
    """
    Normalised dissipation ratios: R_grad, R_pen, R_part.

    Each is the fraction of total dissipation in that channel.
    """
    D = dissipation_channels_2d(rho, v, params)
    D_total = max(D['total'], 1e-30)
    return {
        'R_grad': D['gradient'] / D_total,
        'R_pen': D['penalty'] / D_total,
        'R_part': D['participation'] / D_total,
    }


def local_growth_rate_2d(rho: np.ndarray, params) -> np.ndarray:
    """
    Lyapunov-like local growth rate field.

      sigma(x,y) = (1/rho) * dF/drho evaluated at rho(x,y)

    For the linearised ED PDE at each spatial point, this gives the
    instantaneous local growth/decay rate.  Negative everywhere for
    a stable attractor.

      sigma = M''/M * |grad rho|^2 + M'/M * Lap(rho) - P'/M
    """
    gx, gy = _grad_components(rho, params.hx, params.hy)
    gs = gx**2 + gy**2

    from edsim_solver_2d import laplacian_fd_2d
    lap = laplacian_fd_2d(rho, params.hx, params.hy, params.boundary)

    M_vals = np.maximum(params.M(rho), 1e-15)
    Mp_vals = params.M_prime(rho)
    P_prime = np.full_like(rho, params.P0)

    # sigma ≈ M'*lap/M + (M'' - M'^2/M)*|grad|^2/M - P'/M
    # Simplified: dominant term is -P'/M (penalty drives decay)
    sigma = Mp_vals * lap / M_vals - P_prime / M_vals
    return sigma


def transient_complexity_2d(rho_history: list, hx: float, hy: float) -> np.ndarray:
    """
    Transient complexity from a sequence of rho snapshots.

      T_C(t) = d/dt C_ED(t)

    Approximated via centred differences on the stored snapshots.
    Negative T_C indicates gradient smoothing (inflation-like); positive
    indicates gradient growth (structure formation).
    """
    C_series = np.array([ed_complexity_2d(r, hx, hy) for r in rho_history])
    dC = np.gradient(C_series)
    return dC


def participation_metrics_2d(v: float, F_bar: float, params) -> Dict[str, float]:
    """
    Participation channel metrics.

      v_ss     = (tau/zeta) * F_bar            (steady-state v)
      v_excess = v - v_ss                      (deviation from steady state)
      P_rate   = H * F_bar                     (participation pumping rate)
      P_damp   = H * zeta * v / tau            (participation damping rate)
    """
    v_ss = (params.tau / params.zeta) * F_bar
    return {
        'v': v,
        'v_steady_state': v_ss,
        'v_excess': v - v_ss,
        'pumping_rate': params.H * F_bar,
        'damping_rate': params.H * params.zeta * v / params.tau,
    }


# =====================================================================
#  C. GEOMETRIC INVARIANTS (2D-only)
# =====================================================================

def vorticity_structure_2d(rho: np.ndarray, hx: float, hy: float) -> Dict[str, object]:
    """
    Vorticity-like structure of the gradient field.

    The density gradient (g_x, g_y) = nabla rho defines a vector field.
    Its curl (scalar in 2D) is:

      omega(x,y) = dg_y/dx - dg_x/dy = d^2 rho / (dx dy) - d^2 rho / (dy dx) = 0

    For a scalar field, the curl of the gradient is identically zero.  However,
    the MOBILITY-WEIGHTED flux J = M(rho) * nabla rho has nonzero curl when
    grad(M) and grad(rho) are not parallel:

      curl(J) = M'(rho) * (g_x * d_rho/dy - g_y * d_rho/dx) + M(rho) * 0
              = M'(rho) * (g_x * g_y - g_y * g_x) = 0

    Actually this is also zero. The meaningful vorticity-like measure for
    a scalar field is the Hessian structure:

      omega_H = d^2 rho/(dx dy)

    which measures the twist (off-diagonal curvature) of the density field.
    Regions with large |omega_H| have saddle-like or twisting structure.

    Returns dict with:
      'twist_field': omega_H (Nx, Ny)
      'twist_rms': RMS of omega_H
      'twist_max': max |omega_H|
    """
    p = _pad_neumann(rho)
    # Mixed partial: d^2 rho / (dx dy) via central differences
    # (p[i+1,j+1] - p[i+1,j-1] - p[i-1,j+1] + p[i-1,j-1]) / (4 hx hy)
    omega_H = (p[2:, 2:] - p[2:, :-2] - p[:-2, 2:] + p[:-2, :-2]) / (4.0 * hx * hy)
    # The padded array gives output of shape (Nx, Ny) at interior
    # but we need to be careful: p has shape (Nx+2, Ny+2), so
    # omega_H has shape (Nx, Ny) — correct.

    return {
        'twist_field': omega_H,
        'twist_rms': float(np.sqrt(np.mean(omega_H**2))),
        'twist_max': float(np.max(np.abs(omega_H))),
    }


def hessian_eigenvalues_2d(rho: np.ndarray, hx: float, hy: float) -> Tuple[np.ndarray, np.ndarray]:
    """
    Eigenvalues of the Hessian of rho at each grid point.

    H = [[rho_xx, rho_xy], [rho_xy, rho_yy]]

    Returns (lam1, lam2) where lam1 >= lam2.

    lam1 > 0, lam2 > 0: local minimum (valley)
    lam1 < 0, lam2 < 0: local maximum (peak)
    lam1 * lam2 < 0:    saddle point
    """
    p = _pad_neumann(rho)
    hx2 = hx * hx
    hy2 = hy * hy

    rho_xx = (p[2:, 1:-1] + p[:-2, 1:-1] - 2.0 * p[1:-1, 1:-1]) / hx2
    rho_yy = (p[1:-1, 2:] + p[1:-1, :-2] - 2.0 * p[1:-1, 1:-1]) / hy2
    rho_xy = (p[2:, 2:] - p[2:, :-2] - p[:-2, 2:] + p[:-2, :-2]) / (4.0 * hx * hy)

    trace = rho_xx + rho_yy
    det = rho_xx * rho_yy - rho_xy**2
    disc = np.maximum(trace**2 - 4.0 * det, 0.0)
    sqrt_disc = np.sqrt(disc)

    lam1 = 0.5 * (trace + sqrt_disc)
    lam2 = 0.5 * (trace - sqrt_disc)
    return lam1, lam2


def filamentarity_2d(rho: np.ndarray, hx: float, hy: float) -> Dict[str, float]:
    """
    Filamentarity and sheetness from the Hessian eigenvalues.

    At each point with |lam1| > |lam2|:
      filamentarity F = 1 - |lam2| / |lam1|

    F = 0: isotropic (sheet-like or peak-like)
    F = 1: perfectly filamentary (all curvature in one direction)

    We also compute sheetness = fraction of domain where
    both eigenvalues have the same sign (concave or convex sheet).
    """
    lam1, lam2 = hessian_eigenvalues_2d(rho, hx, hy)
    abs1 = np.abs(lam1)
    abs2 = np.abs(lam2)

    # Ensure lam1 is the larger in magnitude
    abs_max = np.maximum(abs1, abs2)
    abs_min = np.minimum(abs1, abs2)

    F_field = np.where(abs_max > 1e-15, 1.0 - abs_min / abs_max, 0.0)

    # Volume-weighted averages
    Nx, Ny = rho.shape
    Lx = hx * (Nx - 1)
    Ly = hy * (Ny - 1)
    area = Lx * Ly

    F_mean = _trap_2d(F_field, hx, hy) / area

    # Sheetness: fraction where both eigenvalues have same sign
    same_sign = (lam1 * lam2 > 0).astype(float)
    sheet_frac = _trap_2d(same_sign, hx, hy) / area

    # Saddle fraction: fraction where eigenvalues have opposite sign
    saddle_frac = 1.0 - sheet_frac - _trap_2d((np.abs(lam1 * lam2) < 1e-30).astype(float), hx, hy) / area

    return {
        'filamentarity_mean': float(F_mean),
        'filamentarity_max': float(np.max(F_field)),
        'sheetness_fraction': float(sheet_frac),
        'saddle_fraction': float(max(saddle_frac, 0.0)),
    }


def anisotropy_geometric_2d(rho: np.ndarray, hx: float, hy: float) -> Dict[str, float]:
    """
    Geometric anisotropy from the gradient field.

    The structure tensor (gradient outer product averaged over the domain):
      T = <nabla rho (x) nabla rho^T>

    has eigenvalues sigma_1 >= sigma_2.  The anisotropy index:
      A_geom = 1 - sigma_2 / sigma_1

    A_geom = 0: isotropic gradients.
    A_geom = 1: all gradients aligned in one direction.
    """
    gx, gy = _grad_components(rho, hx, hy)
    Nx, Ny = rho.shape
    area = hx * (Nx - 1) * hy * (Ny - 1)

    Txx = _trap_2d(gx * gx, hx, hy) / area
    Tyy = _trap_2d(gy * gy, hx, hy) / area
    Txy = _trap_2d(gx * gy, hx, hy) / area

    trace = Txx + Tyy
    det = Txx * Tyy - Txy**2
    disc = max(trace**2 - 4 * det, 0.0)
    sig1 = 0.5 * (trace + np.sqrt(disc))
    sig2 = 0.5 * (trace - np.sqrt(disc))

    A_geom = 1.0 - sig2 / max(sig1, 1e-30)

    return {
        'anisotropy_geometric': float(A_geom),
        'sigma_1': float(sig1),
        'sigma_2': float(sig2),
        'Txx': float(Txx), 'Tyy': float(Tyy), 'Txy': float(Txy),
    }


def level_set_curvature_2d(rho: np.ndarray, hx: float, hy: float) -> Dict[str, float]:
    """
    Mean curvature of level sets of rho.

    The curvature of the level set rho(x,y) = c passing through (x,y) is:

      kappa = (rho_xx * rho_y^2 - 2 rho_xy rho_x rho_y + rho_yy rho_x^2)
              / |nabla rho|^3

    We compute this everywhere and take the RMS and max, weighted by
    |nabla rho| to avoid singularities at critical points.
    """
    gx, gy = _grad_components(rho, hx, hy)
    grad_mag = np.sqrt(gx**2 + gy**2)

    p = _pad_neumann(rho)
    hx2 = hx * hx
    hy2 = hy * hy
    rho_xx = (p[2:, 1:-1] + p[:-2, 1:-1] - 2.0 * p[1:-1, 1:-1]) / hx2
    rho_yy = (p[1:-1, 2:] + p[1:-1, :-2] - 2.0 * p[1:-1, 1:-1]) / hy2
    rho_xy = (p[2:, 2:] - p[2:, :-2] - p[:-2, 2:] + p[:-2, :-2]) / (4.0 * hx * hy)

    num = rho_xx * gy**2 - 2.0 * rho_xy * gx * gy + rho_yy * gx**2
    denom = grad_mag**3 + 1e-15

    kappa = num / denom

    # Weight by |grad rho| to focus on regions with actual level-set structure
    weight = grad_mag / max(np.max(grad_mag), 1e-15)
    kappa_weighted = kappa * weight

    return {
        'curvature_rms': float(np.sqrt(np.mean(kappa_weighted**2))),
        'curvature_max': float(np.max(np.abs(kappa))),
        'curvature_mean': float(np.mean(kappa_weighted)),
    }


def horizon_detector_2d(rho: np.ndarray, params,
                        threshold: float = 0.1) -> Dict[str, object]:
    """
    Spatial horizon detector: regions where M(rho) -> 0.

    A horizon forms where rho -> rho_max and the mobility vanishes.
    We define the horizon proximity field:

      H_prox(x,y) = 1 - M(rho) / M*

    H_prox = 0 at rho = rho* (equilibrium), H_prox = 1 at rho = rho_max (horizon).
    The horizon region is where H_prox > (1 - threshold).

    Returns dict with:
      'proximity_field': H_prox (Nx, Ny)
      'max_proximity': max H_prox
      'horizon_fraction': area fraction where H_prox > 1-threshold
      'horizon_margin': min(rho_max - rho)
    """
    M_vals = params.M(rho)
    M_star = params.M_star
    H_prox = 1.0 - M_vals / max(M_star, 1e-15)
    H_prox = np.clip(H_prox, 0.0, 1.0)

    near_horizon = (H_prox > (1.0 - threshold)).astype(float)
    area = params.hx * (params.Nx - 1) * params.hy * (params.Ny - 1)
    horizon_frac = _trap_2d(near_horizon, params.hx, params.hy) / area

    return {
        'proximity_field': H_prox,
        'max_proximity': float(np.max(H_prox)),
        'horizon_fraction': float(horizon_frac),
        'horizon_margin': float(np.min(params.rho_max - rho)),
    }


# =====================================================================
#  D. CORRELATION INVARIANTS (2D-only)
# =====================================================================

def correlation_lengths_2d(rho: np.ndarray, hx: float, hy: float) -> Dict[str, float]:
    """
    2D correlation lengths from the autocorrelation function.

    C(r_x, r_y) = <u(x,y) u(x+r_x, y+r_y)> / <u^2>

    where u = rho - mean(rho).  The correlation lengths xi_x, xi_y are
    defined as the e-folding distances of C along each axis:

      C(xi_x, 0) = C(0,0) / e
      C(0, xi_y) = C(0,0) / e
    """
    u = rho - np.mean(rho)
    var = np.mean(u**2)
    if var < 1e-30:
        return {'xi_x': 0.0, 'xi_y': 0.0, 'xi_ratio': 1.0}

    Nx, Ny = rho.shape

    # Autocorrelation via FFT
    from numpy.fft import fft2, ifft2
    U = fft2(u)
    C_full = np.real(ifft2(U * np.conj(U))) / (Nx * Ny)
    C_norm = C_full / C_full[0, 0]

    # x-axis autocorrelation (ry=0)
    Cx = C_norm[:Nx//2, 0]
    lags_x = np.arange(len(Cx)) * hx

    # y-axis autocorrelation (rx=0)
    Cy = C_norm[0, :Ny//2]
    lags_y = np.arange(len(Cy)) * hy

    # Find e-folding distance
    def e_fold(C_1d, lags):
        target = 1.0 / np.e
        below = np.where(C_1d < target)[0]
        if len(below) == 0:
            return lags[-1]
        idx = below[0]
        if idx == 0:
            return lags[0]
        # Linear interpolation
        t = (target - C_1d[idx-1]) / (C_1d[idx] - C_1d[idx-1] + 1e-30)
        return lags[idx-1] + t * (lags[idx] - lags[idx-1])

    xi_x = e_fold(Cx, lags_x)
    xi_y = e_fold(Cy, lags_y)

    return {
        'xi_x': float(xi_x),
        'xi_y': float(xi_y),
        'xi_ratio': float(xi_x / max(xi_y, 1e-15)),
    }


def structure_functions_2d(rho: np.ndarray, hx: float, hy: float,
                           orders: list = None,
                           n_lags: int = 16) -> Dict[int, np.ndarray]:
    """
    Isotropic structure functions of order p.

      S_p(r) = <|rho(x+r) - rho(x)|^p>

    averaged over all directions.  For a smooth field, S_p(r) ~ r^p
    at small r.  Anomalous scaling (S_p ~ r^{zeta_p} with zeta_p != p)
    indicates intermittency.

    Returns dict mapping order p to array S_p(r) of length n_lags.
    Also returns 'r_lags': the lag distances.
    """
    if orders is None:
        orders = [1, 2, 3, 4]

    Nx, Ny = rho.shape
    max_lag = min(Nx, Ny) // 4
    n_lags = min(n_lags, max_lag)
    lags = np.arange(1, n_lags + 1)
    h_avg = 0.5 * (hx + hy)

    result = {'r_lags': lags * h_avg}

    for p in orders:
        S = np.zeros(n_lags)
        for idx, lag in enumerate(lags):
            # Average over 4 directions: +x, +y, +x+y, +x-y
            diffs = []
            if lag < Nx:
                diffs.append((rho[lag:, :] - rho[:-lag, :]).ravel())
            if lag < Ny:
                diffs.append((rho[:, lag:] - rho[:, :-lag]).ravel())
            if lag < Nx and lag < Ny:
                diffs.append((rho[lag:, lag:] - rho[:-lag, :-lag]).ravel())
                diffs.append((rho[lag:, :-lag] - rho[:-lag, lag:]).ravel())
            if len(diffs) > 0:
                all_diffs = np.concatenate(diffs)
                S[idx] = np.mean(np.abs(all_diffs) ** p)
        result[p] = S

    return result


# =====================================================================
#  E. TOP-LEVEL DISPATCHERS
# =====================================================================

def compute_spectral_invariants_2d(rho: np.ndarray, params,
                                   Kx_max: int = 16, Ky_max: int = 16) -> Dict:
    """Compute all spectral invariants."""
    a = modal_amplitudes_2d(rho, params.rho_star, params.Lx, params.Ly, Kx_max, Ky_max)
    E_spectrum = modal_energy_spectrum_2d(a)

    return {
        'modal_amplitudes': a,
        'modal_energy': E_spectrum,
        'spectral_entropy': spectral_entropy_2d(a),
        'renyi_2': renyi_entropy_2d(a, 2.0),
        'renyi_05': renyi_entropy_2d(a, 0.5),
        'geometric_norms': geometric_norms_2d(a, params.Lx, params.Ly),
        'spectral_anisotropy': spectral_anisotropy(a, params.Lx, params.Ly),
        'modal_hierarchy': modal_hierarchy_2d(a, params.Lx, params.Ly),
        'ed_complexity_spectral': modal_complexity_2d(a, params.Lx, params.Ly),
    }


def compute_geometric_invariants_2d(rho: np.ndarray, params) -> Dict:
    """Compute all geometric invariants."""
    hx, hy = params.hx, params.hy
    return {
        'vorticity_structure': vorticity_structure_2d(rho, hx, hy),
        'filamentarity': filamentarity_2d(rho, hx, hy),
        'anisotropy_geometric': anisotropy_geometric_2d(rho, hx, hy),
        'level_set_curvature': level_set_curvature_2d(rho, hx, hy),
        'horizon': horizon_detector_2d(rho, params),
        'correlation_lengths': correlation_lengths_2d(rho, hx, hy),
    }


def compute_dynamical_invariants_2d(rho: np.ndarray, v: float,
                                    F_bar: float, params) -> Dict:
    """Compute all dynamical invariants."""
    return {
        'ed_complexity': ed_complexity_2d(rho, params.hx, params.hy),
        'ed_complexity_effective': ed_complexity_effective_2d(rho, params.hx, params.hy, params),
        'dissipation_channels': dissipation_channels_2d(rho, v, params),
        'dissipation_ratios': dissipation_ratios_2d(rho, v, params),
        'participation': participation_metrics_2d(v, F_bar, params),
        'local_growth_rate_stats': {
            'min': float(np.min(local_growth_rate_2d(rho, params))),
            'max': float(np.max(local_growth_rate_2d(rho, params))),
            'mean': float(np.mean(local_growth_rate_2d(rho, params))),
        },
    }


def compute_invariants_2d(rho: np.ndarray, v: float, F_bar: float, params,
                          Kx_max: int = 16, Ky_max: int = 16) -> Dict:
    """
    Master dispatcher: compute all 2D invariants.

    Parameters
    ----------
    rho : (Nx, Ny) density field
    v : participation variable
    F_bar : spatial average of F[rho]
    params : EDParameters2D

    Returns
    -------
    dict with keys: 'spectral', 'geometric', 'dynamical', 'structure_functions'
    """
    return {
        'spectral': compute_spectral_invariants_2d(rho, params, Kx_max, Ky_max),
        'geometric': compute_geometric_invariants_2d(rho, params),
        'dynamical': compute_dynamical_invariants_2d(rho, v, F_bar, params),
        'structure_functions': structure_functions_2d(rho, params.hx, params.hy),
    }
