"""
invariants_3d.py
================
3D invariant atlas for the canonical Event Density PDE.

Extends the 2D invariant suite into three spatial dimensions and adds
new 3D-only geometric and topological diagnostics.

Organisation:
  A. Spectral invariants   — modal amplitudes, entropy, norms, anisotropy
  B. Dynamical invariants  — dissipation, complexity, growth rates, participation
  C. Geometric invariants  — Hessian eigenstructure, morphology (filament/sheet/blob),
                             curvature (mean H, Gaussian K), twist tensor, horizons
  D. Topological invariants— Minkowski functionals (V, S, B, chi)
  E. Correlation invariants— correlation lengths, structure functions
  F. Top-level dispatchers — compute_invariants_3d(), etc.

All notation follows Appendix C of the Rigour Paper and the Simulation Suite.
"""

import numpy as np
from typing import Dict, Optional, Tuple
from scipy.fft import dctn


# =====================================================================
#  HELPERS
# =====================================================================

def _trap_3d(f, hx, hy, hz):
    """3D trapezoidal integral on a uniform grid."""
    Nx, Ny, Nz = f.shape
    wx = np.ones(Nx); wx[0] = 0.5; wx[-1] = 0.5
    wy = np.ones(Ny); wy[0] = 0.5; wy[-1] = 0.5
    wz = np.ones(Nz); wz[0] = 0.5; wz[-1] = 0.5
    return hx * hy * hz * np.einsum('i,j,k,ijk->', wx, wy, wz, f)


def _pad_neumann_3d(rho):
    """One-cell Neumann ghost padding for 3D arrays."""
    return np.pad(rho, 1, mode='reflect')


def _grad_components_3d(rho, hx, hy, hz):
    """Central-difference gradient (drho/dx, drho/dy, drho/dz) with Neumann BCs."""
    p = _pad_neumann_3d(rho)
    gx = (p[2:, 1:-1, 1:-1] - p[:-2, 1:-1, 1:-1]) / (2.0 * hx)
    gy = (p[1:-1, 2:, 1:-1] - p[1:-1, :-2, 1:-1]) / (2.0 * hy)
    gz = (p[1:-1, 1:-1, 2:] - p[1:-1, 1:-1, :-2]) / (2.0 * hz)
    return gx, gy, gz


def _second_derivs_3d(rho, hx, hy, hz):
    """All six unique second derivatives of rho (xx, yy, zz, xy, xz, yz)."""
    p = _pad_neumann_3d(rho)
    c = p[1:-1, 1:-1, 1:-1]
    rxx = (p[2:, 1:-1, 1:-1] + p[:-2, 1:-1, 1:-1] - 2.0 * c) / (hx * hx)
    ryy = (p[1:-1, 2:, 1:-1] + p[1:-1, :-2, 1:-1] - 2.0 * c) / (hy * hy)
    rzz = (p[1:-1, 1:-1, 2:] + p[1:-1, 1:-1, :-2] - 2.0 * c) / (hz * hz)
    rxy = (p[2:, 2:, 1:-1] - p[2:, :-2, 1:-1] - p[:-2, 2:, 1:-1] + p[:-2, :-2, 1:-1]) / (4*hx*hy)
    rxz = (p[2:, 1:-1, 2:] - p[2:, 1:-1, :-2] - p[:-2, 1:-1, 2:] + p[:-2, 1:-1, :-2]) / (4*hx*hz)
    ryz = (p[1:-1, 2:, 2:] - p[1:-1, 2:, :-2] - p[1:-1, :-2, 2:] + p[1:-1, :-2, :-2]) / (4*hy*hz)
    return rxx, ryy, rzz, rxy, rxz, ryz


# =====================================================================
#  A. SPECTRAL INVARIANTS
# =====================================================================

def modal_amplitudes_3d(rho, rho_star, Lx, Ly, Lz,
                        Kx_max=8, Ky_max=8, Kz_max=8):
    """
    3D modal amplitudes a_{kx,ky,kz} via DCT-I (Neumann basis).

    L^2-normalised: sum |a|^2 = ||rho - rho*||^2_{L^2}.
    Returns shape (Kx_max, Ky_max, Kz_max).
    """
    u = rho - rho_star
    Nx, Ny, Nz = u.shape
    raw = dctn(u, type=1)
    norm = (Nx - 1) * (Ny - 1) * (Nz - 1)
    coeffs = raw / norm

    # Halve boundary modes per axis
    coeffs[0, :, :] /= 2.0;  coeffs[-1, :, :] /= 2.0
    coeffs[:, 0, :] /= 2.0;  coeffs[:, -1, :] /= 2.0
    coeffs[:, :, 0] /= 2.0;  coeffs[:, :, -1] /= 2.0

    Kx = min(Kx_max, Nx); Ky = min(Ky_max, Ny); Kz = min(Kz_max, Nz)
    a = np.zeros((Kx, Ky, Kz))
    Ls = [Lx, Ly, Lz]
    for kx in range(Kx):
        nx = np.sqrt(Lx) if kx == 0 else np.sqrt(Lx / 2.0)
        for ky in range(Ky):
            ny = np.sqrt(Ly) if ky == 0 else np.sqrt(Ly / 2.0)
            for kz in range(Kz):
                nz = np.sqrt(Lz) if kz == 0 else np.sqrt(Lz / 2.0)
                if kx < coeffs.shape[0] and ky < coeffs.shape[1] and kz < coeffs.shape[2]:
                    a[kx, ky, kz] = coeffs[kx, ky, kz] * nx * ny * nz
    return a


def spectral_entropy_3d(a, floor=1e-30):
    """Shannon spectral entropy: H = -sum p_k log(p_k)."""
    E = a ** 2
    E_total = np.sum(E)
    if E_total < floor:
        return 0.0
    p = np.maximum(E / E_total, floor)
    return float(-np.sum(p * np.log(p)))


def renyi_entropy_3d(a, q, floor=1e-30):
    """Renyi entropy of order q.  H_1 = Shannon entropy."""
    if abs(q - 1.0) < 1e-10:
        return spectral_entropy_3d(a, floor)
    E = a ** 2
    E_total = np.sum(E)
    if E_total < floor:
        return 0.0
    p = np.maximum(E / E_total, floor)
    return float(np.log(np.sum(p ** q)) / (1.0 - q))


def geometric_norms_3d(a, Lx, Ly, Lz, alphas=None):
    """
    Weighted spectral norms G_alpha = sum |k|^{2 alpha} |a_k|^2.

    |k|^2 = (kx pi/Lx)^2 + (ky pi/Ly)^2 + (kz pi/Lz)^2.
    """
    if alphas is None:
        alphas = [-2, -1, 0, 1, 2, 3, 4]
    Kx, Ky, Kz = a.shape
    kx = np.arange(Kx) * np.pi / Lx
    ky = np.arange(Ky) * np.pi / Ly
    kz = np.arange(Kz) * np.pi / Lz
    k_sq = kx[:, None, None]**2 + ky[None, :, None]**2 + kz[None, None, :]**2
    E = a ** 2
    result = {}
    for alpha in alphas:
        w = np.where(k_sq > 0, k_sq ** alpha, 0.0)
        result[alpha] = float(np.sum(w * E))
    return result


def spectral_anisotropy_3d(a, Lx, Ly, Lz):
    """
    3D spectral anisotropy from the spectral inertia tensor.

    I_{ij} = <k_i k_j>_E.  Returns eigenvalues and derived measures:
      - planarity P = 1 - lam2/lam1  (degree of planar anisotropy)
      - linearity L = 1 - lam3/lam2  (degree of linear anisotropy)
      - isotropy  S = lam3/lam1      (sphericity)
    """
    E = a ** 2
    Kx, Ky, Kz = a.shape
    kx = np.arange(Kx) * np.pi / Lx
    ky = np.arange(Ky) * np.pi / Ly
    kz = np.arange(Kz) * np.pi / Lz
    KX = kx[:, None, None]; KY = ky[None, :, None]; KZ = kz[None, None, :]
    E_total = max(np.sum(E), 1e-30)

    I = np.zeros((3, 3))
    comps = [KX, KY, KZ]
    for i in range(3):
        for j in range(i, 3):
            I[i, j] = np.sum(comps[i] * comps[j] * E) / E_total
            I[j, i] = I[i, j]

    eigvals = np.sort(np.linalg.eigvalsh(I))[::-1]  # lam1 >= lam2 >= lam3
    lam1, lam2, lam3 = eigvals

    return {
        'eigenvalues': eigvals,
        'planarity': float(1.0 - lam2 / max(lam1, 1e-30)),
        'linearity': float(1.0 - lam3 / max(lam2, 1e-30)),
        'isotropy': float(lam3 / max(lam1, 1e-30)),
        'inertia_tensor': I,
    }


def modal_hierarchy_3d(a, Lx, Ly, Lz):
    """Radially-binned energy spectrum and power-law decay rate."""
    E = a ** 2
    Kx, Ky, Kz = a.shape
    kx = np.arange(Kx) * np.pi / Lx
    ky = np.arange(Ky) * np.pi / Ly
    kz = np.arange(Kz) * np.pi / Lz
    k_mag = np.sqrt(kx[:, None, None]**2 + ky[None, :, None]**2 + kz[None, None, :]**2).ravel()
    E_flat = E.ravel()
    order = np.argsort(k_mag)
    k_s = k_mag[order]; E_s = E_flat[order]
    mask = k_s > 0; k_p = k_s[mask]; E_p = E_s[mask]
    n_bins = min(20, max(2, len(k_p) // 4))
    if n_bins < 2:
        return {'radial_spectrum': (np.array([]), np.array([])), 'decay_rate': 0.0}
    edges = np.linspace(k_p[0], k_p[-1], n_bins + 1)
    k_bins = 0.5 * (edges[:-1] + edges[1:])
    E_binned = np.array([np.sum(E_p[(k_p >= edges[b]) & (k_p < edges[b+1])]) for b in range(n_bins)])
    m = E_binned > 1e-30
    if np.sum(m) >= 3:
        A = np.column_stack([np.log(k_bins[m]), np.ones(np.sum(m))])
        c, *_ = np.linalg.lstsq(A, np.log(E_binned[m]), rcond=None)
        rate = -c[0]
    else:
        rate = 0.0
    return {'radial_spectrum': (k_bins, E_binned), 'decay_rate': float(rate)}


# =====================================================================
#  B. DYNAMICAL INVARIANTS
# =====================================================================

def ed_complexity_3d(rho, hx, hy, hz):
    """Bare ED-complexity: C_ED = integral |grad rho|^2 dV."""
    gx, gy, gz = _grad_components_3d(rho, hx, hy, hz)
    return float(_trap_3d(gx**2 + gy**2 + gz**2, hx, hy, hz))


def ed_complexity_effective_3d(rho, hx, hy, hz, params):
    """Effective ED-complexity: integral (P'/M) |grad rho|^2 dV."""
    gx, gy, gz = _grad_components_3d(rho, hx, hy, hz)
    gs = gx**2 + gy**2 + gz**2
    M_v = np.maximum(params.M(rho), 1e-15)
    return float(_trap_3d((params.P0 / M_v) * gs, hx, hy, hz))


def dissipation_channels_3d(rho, v, params):
    """Three dissipation channels: gradient, penalty, participation."""
    C_ED = ed_complexity_3d(rho, params.hx, params.hy, params.hz)
    D_grad = params.D * params.P_star_prime * C_ED
    dev_sq = (rho - params.rho_star) ** 2
    int_dev_sq = _trap_3d(dev_sq, params.hx, params.hy, params.hz)
    D_pen = params.D * params.P_star_prime**2 / params.M_star * int_dev_sq
    D_part = params.H * params.zeta * v ** 2
    return {'gradient': D_grad, 'penalty': D_pen, 'participation': D_part,
            'total': D_grad + D_pen + D_part}


def dissipation_ratios_3d(rho, v, params):
    D = dissipation_channels_3d(rho, v, params)
    Dt = max(D['total'], 1e-30)
    return {'R_grad': D['gradient']/Dt, 'R_pen': D['penalty']/Dt, 'R_part': D['participation']/Dt}


def local_growth_rate_3d(rho, params):
    """Pointwise Lyapunov-like growth rate sigma = M'*Lap/M - P'/M."""
    from edsim_solver_3d import laplacian_fd_3d
    lap = laplacian_fd_3d(rho, params.hx, params.hy, params.hz, params.boundary)
    M_v = np.maximum(params.M(rho), 1e-15)
    Mp = params.M_prime(rho)
    return Mp * lap / M_v - params.P0 / M_v


def participation_metrics_3d(v, F_bar, params):
    v_ss = (params.tau / params.zeta) * F_bar
    return {'v': v, 'v_steady_state': v_ss, 'v_excess': v - v_ss,
            'pumping_rate': params.H * F_bar,
            'damping_rate': params.H * params.zeta * v / params.tau}


# =====================================================================
#  C. GEOMETRIC INVARIANTS (3D)
# =====================================================================

def hessian_eigenvalues_3d(rho, hx, hy, hz):
    """
    Eigenvalues of the 3x3 Hessian at each grid point.

    Returns (lam1, lam2, lam3) with lam1 >= lam2 >= lam3.
    Uses the analytic cubic formula via numpy.linalg.eigvalsh on the
    vectorised 3x3 symmetric matrix.
    """
    rxx, ryy, rzz, rxy, rxz, ryz = _second_derivs_3d(rho, hx, hy, hz)
    shape = rho.shape
    n = np.prod(shape)

    # Build (n, 3, 3) array of symmetric Hessians
    H = np.empty((n, 3, 3))
    H[:, 0, 0] = rxx.ravel(); H[:, 1, 1] = ryy.ravel(); H[:, 2, 2] = rzz.ravel()
    H[:, 0, 1] = rxy.ravel(); H[:, 1, 0] = rxy.ravel()
    H[:, 0, 2] = rxz.ravel(); H[:, 2, 0] = rxz.ravel()
    H[:, 1, 2] = ryz.ravel(); H[:, 2, 1] = ryz.ravel()

    eigvals = np.linalg.eigvalsh(H)  # (n, 3), sorted ascending
    lam3 = eigvals[:, 0].reshape(shape)
    lam2 = eigvals[:, 1].reshape(shape)
    lam1 = eigvals[:, 2].reshape(shape)
    return lam1, lam2, lam3


def morphology_3d(rho, hx, hy, hz):
    """
    3D morphological classification from Hessian eigenvalues.

    At each point with eigenvalues lam1 >= lam2 >= lam3:
      filamentarity F = (lam2 - lam3) / max(|lam1|, eps)
      sheetness     S = (lam1 - lam2) / max(|lam1|, eps)
      blobness      B = |lam3| / max(|lam1|, eps)

    Classification:
      BLOB:     lam1 ~ lam2 ~ lam3  (S small, F small)
      SHEET:    lam1 >> lam2 ~ lam3  (S large)
      FILAMENT: lam1 ~ lam2 >> lam3  (F large)

    Also reports volume fractions of each morphology.
    """
    lam1, lam2, lam3 = hessian_eigenvalues_3d(rho, hx, hy, hz)
    # Sort by MAGNITUDE: a1 >= a2 >= a3
    a1_raw = np.abs(lam1); a2_raw = np.abs(lam2); a3_raw = np.abs(lam3)
    stacked = np.sort(np.stack([a1_raw, a2_raw, a3_raw], axis=-1), axis=-1)
    a3_s = stacked[..., 0]; a2_s = stacked[..., 1]; a1_s = stacked[..., 2]
    a1_safe = np.maximum(a1_s, 1e-15)

    F_field = (a2_s - a3_s) / a1_safe
    S_field = (a1_s - a2_s) / a1_safe
    B_field = a3_s / a1_safe

    F_field = np.clip(F_field, 0, 1)
    S_field = np.clip(S_field, 0, 1)
    B_field = np.clip(B_field, 0, 1)

    vol = hx * (rho.shape[0]-1) * hy * (rho.shape[1]-1) * hz * (rho.shape[2]-1)

    # Dominant morphology at each point
    is_filament = (F_field > S_field) & (F_field > B_field)
    is_sheet = (S_field > F_field) & (S_field > B_field)
    is_blob = ~is_filament & ~is_sheet

    return {
        'filamentarity_mean': float(_trap_3d(F_field, hx, hy, hz) / vol),
        'sheetness_mean': float(_trap_3d(S_field, hx, hy, hz) / vol),
        'blobness_mean': float(_trap_3d(B_field, hx, hy, hz) / vol),
        'filament_fraction': float(_trap_3d(is_filament.astype(float), hx, hy, hz) / vol),
        'sheet_fraction': float(_trap_3d(is_sheet.astype(float), hx, hy, hz) / vol),
        'blob_fraction': float(_trap_3d(is_blob.astype(float), hx, hy, hz) / vol),
    }


def curvature_invariants_3d(rho, hx, hy, hz):
    """
    Mean curvature H and Gaussian curvature K of iso-surfaces.

    For a scalar field rho, the mean curvature of the level set
    rho(x,y,z) = c is:

      H = div(grad rho / |grad rho|) / 2

    and the Gaussian curvature is:

      K = (rho_xx*(rho_yy*rho_zz - rho_yz^2)
         - rho_xy*(rho_xy*rho_zz - rho_yz*rho_xz)
         + rho_xz*(rho_xy*rho_yz - rho_yy*rho_xz)) / |grad rho|^4

    We report RMS and max of both, weighted by |grad rho| to suppress
    singularities at critical points.
    """
    gx, gy, gz = _grad_components_3d(rho, hx, hy, hz)
    grad_mag = np.sqrt(gx**2 + gy**2 + gz**2)
    rxx, ryy, rzz, rxy, rxz, ryz = _second_derivs_3d(rho, hx, hy, hz)

    # Mean curvature (div of unit normal)
    g2 = grad_mag**2 + 1e-30
    g3 = g2 * np.sqrt(g2)
    H_field = ((ryy + rzz)*gx**2 + (rxx + rzz)*gy**2 + (rxx + ryy)*gz**2
               - 2*(rxy*gx*gy + rxz*gx*gz + ryz*gy*gz)) / (2.0 * g3)

    # Gaussian curvature
    g4 = g2**2
    K_field = (rxx*(ryy*rzz - ryz**2)
             - rxy*(rxy*rzz - ryz*rxz)
             + rxz*(rxy*ryz - ryy*rxz)) / (g4 + 1e-30)

    w = grad_mag / max(np.max(grad_mag), 1e-15)
    Hw = H_field * w
    Kw = K_field * w

    return {
        'mean_curvature_rms': float(np.sqrt(np.mean(Hw**2))),
        'mean_curvature_max': float(np.max(np.abs(H_field))),
        'gaussian_curvature_rms': float(np.sqrt(np.mean(Kw**2))),
        'gaussian_curvature_max': float(np.max(np.abs(K_field))),
    }


def twist_tensor_3d(rho, hx, hy, hz):
    """
    Twist tensor: the three off-diagonal second derivatives.

    omega_xy = d^2 rho / (dx dy)
    omega_xz = d^2 rho / (dx dz)
    omega_yz = d^2 rho / (dy dz)

    The Frobenius norm of the off-diagonal block measures total twist.
    """
    _, _, _, rxy, rxz, ryz = _second_derivs_3d(rho, hx, hy, hz)
    twist_mag = np.sqrt(rxy**2 + rxz**2 + ryz**2)
    return {
        'twist_rms': float(np.sqrt(np.mean(twist_mag**2))),
        'twist_max': float(np.max(twist_mag)),
        'omega_xy_rms': float(np.sqrt(np.mean(rxy**2))),
        'omega_xz_rms': float(np.sqrt(np.mean(rxz**2))),
        'omega_yz_rms': float(np.sqrt(np.mean(ryz**2))),
    }


def anisotropy_geometric_3d(rho, hx, hy, hz):
    """
    Geometric anisotropy from the 3x3 structure tensor T_{ij} = <g_i g_j>.

    Returns eigenvalues sigma_1 >= sigma_2 >= sigma_3 and derived indices:
      planarity = 1 - sigma_2/sigma_1
      linearity = 1 - sigma_3/sigma_2
      isotropy  = sigma_3/sigma_1
    """
    gx, gy, gz = _grad_components_3d(rho, hx, hy, hz)
    vol = hx*(rho.shape[0]-1) * hy*(rho.shape[1]-1) * hz*(rho.shape[2]-1)

    T = np.zeros((3, 3))
    g = [gx, gy, gz]
    for i in range(3):
        for j in range(i, 3):
            T[i, j] = _trap_3d(g[i] * g[j], hx, hy, hz) / vol
            T[j, i] = T[i, j]

    eigvals = np.sort(np.linalg.eigvalsh(T))[::-1]
    s1, s2, s3 = eigvals
    return {
        'eigenvalues': eigvals,
        'planarity': float(1.0 - s2 / max(s1, 1e-30)),
        'linearity': float(1.0 - s3 / max(s2, 1e-30)),
        'isotropy': float(s3 / max(s1, 1e-30)),
    }


def horizon_detector_3d(rho, params, threshold=0.1):
    """
    Horizon detector in 3D: regions where M(rho) -> 0.

    H_prox = 1 - M(rho)/M*.  Reports max proximity, volume fraction,
    margin, and number of connected components (via simple flood fill).
    """
    M_v = params.M(rho)
    H_prox = np.clip(1.0 - M_v / max(params.M_star, 1e-15), 0.0, 1.0)
    near = (H_prox > (1.0 - threshold)).astype(float)
    vol = params.hx*(params.Nx-1) * params.hy*(params.Ny-1) * params.hz*(params.Nz-1)
    frac = _trap_3d(near, params.hx, params.hy, params.hz) / vol

    # Count connected components via scipy label (if available)
    n_components = 0
    try:
        from scipy.ndimage import label
        labelled, n_components = label(near > 0.5)
    except ImportError:
        pass

    return {
        'max_proximity': float(np.max(H_prox)),
        'horizon_fraction': float(frac),
        'horizon_margin': float(np.min(params.rho_max - rho)),
        'n_components': int(n_components),
    }


# =====================================================================
#  D. TOPOLOGICAL INVARIANTS — MINKOWSKI FUNCTIONALS
# =====================================================================

def minkowski_functionals_3d(rho, hx, hy, hz, threshold=None):
    """
    Approximate Minkowski functionals for the excursion set {rho > threshold}.

    In 3D there are four Minkowski functionals:
      V  = volume of the excursion set
      S  = surface area (boundary area)
      B  = integrated mean curvature of the boundary
      chi = Euler characteristic

    We compute V exactly, S via a voxel-face counting approximation,
    and chi via the Euler formula on the binary grid.

    If threshold is None, defaults to mean(rho).
    """
    if threshold is None:
        threshold = np.mean(rho)

    binary = (rho > threshold).astype(np.int8)
    Nx, Ny, Nz = rho.shape
    voxel_vol = hx * hy * hz

    # V: volume
    V = float(np.sum(binary)) * voxel_vol

    # S: surface area (count exposed faces between 0 and 1 voxels)
    n_faces = 0
    # x-faces
    n_faces += np.sum(binary[1:, :, :] != binary[:-1, :, :]) * (hy * hz)
    # y-faces
    n_faces += np.sum(binary[:, 1:, :] != binary[:, :-1, :]) * (hx * hz)
    # z-faces
    n_faces += np.sum(binary[:, :, 1:] != binary[:, :, :-1]) * (hx * hy)
    S = float(n_faces)

    # B: integrated mean curvature (edge-based approximation)
    # Count exposed edges (edge shared by exactly one excursion voxel)
    # Approximate via difference of face counts in orthogonal directions
    B = S / (4.0 * np.pi) if S > 0 else 0.0  # rough normalised estimate

    # chi: Euler characteristic via voxel counting (vertices - edges + faces - cells)
    # Use the digital topology formula for 6-connectivity
    V_count = int(np.sum(binary))
    # Edges (6-connected pairs)
    E_count = (int(np.sum(binary[1:, :, :] & binary[:-1, :, :]))
             + int(np.sum(binary[:, 1:, :] & binary[:, :-1, :]))
             + int(np.sum(binary[:, :, 1:] & binary[:, :, :-1])))
    # Faces (4-connected squares in each plane)
    F_count = (int(np.sum(binary[1:, 1:, :] & binary[:-1, 1:, :] & binary[1:, :-1, :] & binary[:-1, :-1, :]))
             + int(np.sum(binary[1:, :, 1:] & binary[:-1, :, 1:] & binary[1:, :, :-1] & binary[:-1, :, :-1]))
             + int(np.sum(binary[:, 1:, 1:] & binary[:, :-1, 1:] & binary[:, 1:, :-1] & binary[:, :-1, :-1])))
    # Cubes (8-connected)
    C_count = int(np.sum(
        binary[1:, 1:, 1:] & binary[:-1, 1:, 1:] & binary[1:, :-1, 1:] & binary[1:, 1:, :-1]
        & binary[:-1, :-1, 1:] & binary[:-1, 1:, :-1] & binary[1:, :-1, :-1] & binary[:-1, :-1, :-1]))
    chi = V_count - E_count + F_count - C_count

    return {'V': V, 'S': S, 'B': float(B), 'chi': int(chi)}


# =====================================================================
#  E. CORRELATION INVARIANTS
# =====================================================================

def correlation_lengths_3d(rho, hx, hy, hz):
    """3D correlation lengths xi_x, xi_y, xi_z (e-folding of autocorrelation)."""
    u = rho - np.mean(rho)
    var = np.mean(u**2)
    if var < 1e-30:
        return {'xi_x': 0.0, 'xi_y': 0.0, 'xi_z': 0.0}

    Nx, Ny, Nz = rho.shape
    from numpy.fft import fftn, ifftn
    U = fftn(u)
    C = np.real(ifftn(U * np.conj(U))) / (Nx * Ny * Nz)
    C_norm = C / C[0, 0, 0]

    def e_fold(C_1d, h):
        lags = np.arange(len(C_1d)) * h
        target = 1.0 / np.e
        below = np.where(C_1d < target)[0]
        if len(below) == 0:
            return lags[-1]
        idx = below[0]
        if idx == 0:
            return lags[0]
        t = (target - C_1d[idx-1]) / (C_1d[idx] - C_1d[idx-1] + 1e-30)
        return float(lags[idx-1] + t * (lags[idx] - lags[idx-1]))

    xi_x = e_fold(C_norm[:Nx//2, 0, 0], hx)
    xi_y = e_fold(C_norm[0, :Ny//2, 0], hy)
    xi_z = e_fold(C_norm[0, 0, :Nz//2], hz)
    return {'xi_x': xi_x, 'xi_y': xi_y, 'xi_z': xi_z}


def structure_functions_3d(rho, hx, hy, hz, orders=None, n_lags=8):
    """Isotropic structure functions S_p(r) averaged over 6 axis directions."""
    if orders is None:
        orders = [2, 4]
    Nx, Ny, Nz = rho.shape
    max_lag = min(Nx, Ny, Nz) // 4
    n_lags = min(n_lags, max(1, max_lag))
    lags = np.arange(1, n_lags + 1)
    h_avg = (hx + hy + hz) / 3.0
    result = {'r_lags': lags * h_avg}
    for p in orders:
        S = np.zeros(n_lags)
        for idx, lag in enumerate(lags):
            diffs = []
            if lag < Nx: diffs.append((rho[lag:,:,:] - rho[:-lag,:,:]).ravel())
            if lag < Ny: diffs.append((rho[:,lag:,:] - rho[:,:-lag,:]).ravel())
            if lag < Nz: diffs.append((rho[:,:,lag:] - rho[:,:,:-lag]).ravel())
            if diffs:
                S[idx] = np.mean(np.abs(np.concatenate(diffs)) ** p)
        result[p] = S
    return result


# =====================================================================
#  F. TOP-LEVEL DISPATCHERS
# =====================================================================

def compute_spectral_invariants_3d(rho, params, K_max=8):
    a = modal_amplitudes_3d(rho, params.rho_star, params.Lx, params.Ly, params.Lz,
                            K_max, K_max, K_max)
    return {
        'modal_amplitudes': a,
        'spectral_entropy': spectral_entropy_3d(a),
        'renyi_2': renyi_entropy_3d(a, 2.0),
        'geometric_norms': geometric_norms_3d(a, params.Lx, params.Ly, params.Lz),
        'spectral_anisotropy': spectral_anisotropy_3d(a, params.Lx, params.Ly, params.Lz),
        'modal_hierarchy': modal_hierarchy_3d(a, params.Lx, params.Ly, params.Lz),
    }


def compute_geometric_invariants_3d(rho, params):
    hx, hy, hz = params.hx, params.hy, params.hz
    return {
        'morphology': morphology_3d(rho, hx, hy, hz),
        'curvature': curvature_invariants_3d(rho, hx, hy, hz),
        'twist': twist_tensor_3d(rho, hx, hy, hz),
        'anisotropy_geometric': anisotropy_geometric_3d(rho, hx, hy, hz),
        'horizon': horizon_detector_3d(rho, params),
        'correlation_lengths': correlation_lengths_3d(rho, hx, hy, hz),
        'minkowski': minkowski_functionals_3d(rho, hx, hy, hz),
    }


def compute_dynamical_invariants_3d(rho, v, F_bar, params):
    hx, hy, hz = params.hx, params.hy, params.hz
    sigma = local_growth_rate_3d(rho, params)
    return {
        'ed_complexity': ed_complexity_3d(rho, hx, hy, hz),
        'ed_complexity_effective': ed_complexity_effective_3d(rho, hx, hy, hz, params),
        'dissipation_channels': dissipation_channels_3d(rho, v, params),
        'dissipation_ratios': dissipation_ratios_3d(rho, v, params),
        'participation': participation_metrics_3d(v, F_bar, params),
        'local_growth_rate_stats': {
            'min': float(np.min(sigma)),
            'max': float(np.max(sigma)),
            'mean': float(np.mean(sigma)),
        },
    }


def compute_invariants_3d(rho, v, F_bar, params, K_max=8):
    """Master dispatcher: compute all 3D invariants."""
    return {
        'spectral': compute_spectral_invariants_3d(rho, params, K_max),
        'geometric': compute_geometric_invariants_3d(rho, params),
        'dynamical': compute_dynamical_invariants_3d(rho, v, F_bar, params),
        'structure_functions': structure_functions_3d(rho, params.hx, params.hy, params.hz),
    }
