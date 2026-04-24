"""
Monte Carlo implementation of the ED-SC 2.0 r* workflow.

Implements:
  - IMEX SPDE integrator on 64x64 periodic grid
  - Stationary-point detection via 2x2 plaquette sign changes + bilinear refinement
  - ED-SC 2.0 motif filter (delta_thr=0.10, alpha=0.25, L_ray=2, D2 symmetry,
    aspect ratio >= 1.5, orientation alignment)
  - Curvature + r* extraction
  - Bootstrap CI over realisations

Outputs a summary dict to stdout in JSON.
"""
import numpy as np
from numpy.fft import fft2, ifft2
import json
import sys

# ------------------------------------------------------------------
# Parameters
# ------------------------------------------------------------------
M0 = 1.0
M2 = 0.0
P0 = 1.0
P3 = -1.0
SIGMA = 0.0556
DT = 0.05
L = 64          # grid side
DX = 1.0
N_STEPS = 2000
BURN_IN = 500
SNAPSHOT_EVERY = 20
N_REALISATIONS = 10

# Motif-filter pre-registered parameters
DELTA_THR = 0.10
ALPHA = 0.25
L_RAY = 2
ASPECT_MIN = 1.5
SYM_THRESH = 0.20
ORIENT_TOL_DEG = 15.0


def fft_laplacian_symbol(N, dx):
    """Return eigenvalue array -(k_x^2 + k_y^2) for discrete Laplacian in 2D."""
    k = np.fft.fftfreq(N, d=dx) * 2 * np.pi
    kx, ky = np.meshgrid(k, k, indexing='ij')
    return -(kx**2 + ky**2)


def imex_step(delta, dt, lap_sym, rng):
    """Semi-implicit Euler step for:
       dt delta = M0 lap(delta) + M2_nonlin - P0 delta - P3/6 delta^3 + noise
    Implicit: M0 lap(delta) - P0 delta
    Explicit: nonlinear M2 term, cubic penalty, noise
    """
    N = delta.shape[0]
    # Explicit nonlinear part: M2 * div(delta^2 grad delta)  (here M2=0 so zero)
    # and cubic penalty -P3/6 * delta^3 (P3=-1 -> +1/6 * delta^3)
    explicit = -(P3 / 6.0) * delta**3
    # Note: PDE as written is d_t delta = div(M grad delta) - P(delta) + xi
    # Linear part: M0 * lap(delta) - P0 * delta
    # Nonlinear part: - (1/6)*P3*delta^3  (NB sign: P(delta) = P0*delta + P3/6*delta^3)
    # So d_t = M0 lap(delta) - P0 delta - (P3/6) delta^3 + noise
    # With P3 = -1: cubic source is + delta^3/6, which destabilises large delta
    # (intended: bistable penalty)

    # Noise amplitude in lattice units: sqrt(2 sigma^2 dt / dx^2) per site
    noise_amp = np.sqrt(2 * SIGMA**2 * dt / DX**2)
    xi = noise_amp * rng.standard_normal(delta.shape)

    # Construct source in Fourier: delta_hat_new = (delta_hat + dt * explicit_hat + xi_hat)
    #                               / (1 - dt * (M0 * lap_sym - P0))
    src = delta + dt * explicit + xi  # wait -- xi already has sqrt(dt) baked in
    # Actually xi = sqrt(2 sigma^2 dt / dx^2) * N(0,1) -- this is dW, not xi*dt
    # So contribution to delta update is xi directly (already scaled).
    # Recompute: SPDE discretised Euler-Maruyama style,
    # delta_new = delta + dt * F(delta) + sqrt(2 sigma^2 dt / dx^2) N(0,1)
    src_hat = fft2(src)
    denom = 1.0 - dt * (M0 * lap_sym - P0)
    delta_new_hat = src_hat / denom
    delta_new = np.real(ifft2(delta_new_hat))
    return delta_new


def detect_stationary_points(delta):
    """Find stationary points via 2x2 plaquette sign changes on discrete gradient.
    Returns list of (x0, y0, i, j) with sub-grid (x0, y0) and grid anchor (i, j)."""
    N = delta.shape[0]
    # Periodic gradients
    gx = (np.roll(delta, -1, axis=0) - np.roll(delta, 1, axis=0)) / (2 * DX)
    gy = (np.roll(delta, -1, axis=1) - np.roll(delta, 1, axis=1)) / (2 * DX)

    points = []
    # Iterate over plaquettes. A plaquette is (i,j)-(i+1,j)-(i,j+1)-(i+1,j+1)
    for i in range(N):
        ip = (i + 1) % N
        for j in range(N):
            jp = (j + 1) % N
            gx_vals = np.array([gx[i, j], gx[ip, j], gx[i, jp], gx[ip, jp]])
            gy_vals = np.array([gy[i, j], gy[ip, j], gy[i, jp], gy[ip, jp]])
            # Require both components to change sign across plaquette
            if gx_vals.min() * gx_vals.max() >= 0: continue
            if gy_vals.min() * gy_vals.max() >= 0: continue

            # Bilinear fit: f(xi, eta) = a + b*xi + c*eta + d*xi*eta
            # corners: (0,0)->v00, (1,0)->v10, (0,1)->v01, (1,1)->v11
            g00x, g10x, g01x, g11x = gx_vals
            g00y, g10y, g01y, g11y = gy_vals
            # Solve gx(xi,eta)=0 and gy(xi,eta)=0 by Newton from (0.5, 0.5)
            xi, eta = 0.5, 0.5
            for _ in range(8):
                gxv = g00x*(1-xi)*(1-eta) + g10x*xi*(1-eta) + g01x*(1-xi)*eta + g11x*xi*eta
                gyv = g00y*(1-xi)*(1-eta) + g10y*xi*(1-eta) + g01y*(1-xi)*eta + g11y*xi*eta
                # Jacobian
                dgx_dxi = -g00x*(1-eta) + g10x*(1-eta) - g01x*eta + g11x*eta
                dgx_deta = -g00x*(1-xi) - g10x*xi + g01x*(1-xi) + g11x*xi
                dgy_dxi = -g00y*(1-eta) + g10y*(1-eta) - g01y*eta + g11y*eta
                dgy_deta = -g00y*(1-xi) - g10y*xi + g01y*(1-xi) + g11y*xi
                J = np.array([[dgx_dxi, dgx_deta], [dgy_dxi, dgy_deta]])
                F = np.array([gxv, gyv])
                try:
                    step = np.linalg.solve(J, F)
                except np.linalg.LinAlgError:
                    break
                xi -= step[0]
                eta -= step[1]
                if abs(step[0]) + abs(step[1]) < 1e-8: break
            if not (0 <= xi <= 1 and 0 <= eta <= 1): continue
            x0 = (i + xi) % N
            y0 = (j + eta) % N
            points.append((x0, y0, i, j))
    return points


def compute_hessian(delta, i, j):
    """Centred-difference 2x2 spatial Hessian at grid site (i,j) with periodic BCs."""
    N = delta.shape[0]
    ip, im = (i+1) % N, (i-1) % N
    jp, jm = (j+1) % N, (j-1) % N
    Kxx = (delta[ip, j] - 2*delta[i, j] + delta[im, j]) / DX**2
    Kyy = (delta[i, jp] - 2*delta[i, j] + delta[i, jm]) / DX**2
    Kxy = (delta[ip, jp] - delta[ip, jm] - delta[im, jp] + delta[im, jm]) / (4 * DX**2)
    return np.array([[Kxx, Kxy], [Kxy, Kyy]])


def interpolate_delta(delta, x0, y0):
    """Bilinear interpolation of delta at sub-grid point (x0, y0)."""
    N = delta.shape[0]
    i = int(np.floor(x0)) % N
    j = int(np.floor(y0)) % N
    xi = x0 - np.floor(x0)
    eta = y0 - np.floor(y0)
    ip = (i + 1) % N
    jp = (j + 1) % N
    return (delta[i, j]*(1-xi)*(1-eta) + delta[ip, j]*xi*(1-eta)
            + delta[i, jp]*(1-xi)*eta + delta[ip, jp]*xi*eta)


def motif_filter_check(delta, x0, y0, i, j, K, kappa_par_vec):
    """Return (accept: bool, diagnostics dict)."""
    N = delta.shape[0]
    d_pt = interpolate_delta(delta, x0, y0)

    # 3.1 amplitude threshold
    if abs(d_pt) < DELTA_THR:
        return False, {'reason': 'amplitude', 'd_pt': d_pt}

    # 3.2 / 3.3: build alpha-contour on a neighbourhood
    # Extract window of size 2*W+1 around (i,j)
    W = 8  # half-window size
    ii = (np.arange(-W, W+1) + i) % N
    jj = (np.arange(-W, W+1) + j) % N
    window = delta[np.ix_(ii, jj)]
    thresh = ALPHA * d_pt
    mask = (window >= thresh) if d_pt > 0 else (window <= thresh)
    if not mask[W, W]:
        return False, {'reason': 'alpha_mask_centre'}

    # Connected component containing centre via simple flood fill
    from collections import deque
    cc = np.zeros_like(mask)
    q = deque([(W, W)])
    cc[W, W] = True
    while q:
        a, b = q.popleft()
        for da, db in [(-1,0),(1,0),(0,-1),(0,1)]:
            na, nb = a+da, b+db
            if 0 <= na < mask.shape[0] and 0 <= nb < mask.shape[1]:
                if mask[na, nb] and not cc[na, nb]:
                    cc[na, nb] = True
                    q.append((na, nb))

    coords = np.argwhere(cc)
    if coords.shape[0] < 4:
        return False, {'reason': 'cc_too_small', 'size': coords.shape[0]}

    # PCA on cc coordinates for major/minor axis
    centred = coords - coords.mean(axis=0)
    cov = centred.T @ centred / max(1, coords.shape[0] - 1)
    evals, evecs = np.linalg.eigh(cov)
    L_min = 2 * np.sqrt(max(evals[0], 1e-10))  # ~ 2*std of projection
    L_maj = 2 * np.sqrt(max(evals[1], 1e-10))
    major_vec = evecs[:, 1]

    # 3.3 ray length
    if L_maj < L_RAY * DX:
        return False, {'reason': 'L_maj', 'L_maj': L_maj}

    # 3.4 aspect ratio
    aspect = L_maj / max(L_min, 1e-10)
    if aspect < ASPECT_MIN:
        return False, {'reason': 'aspect', 'aspect': aspect}

    # 3.4 (continued) D2 reflection symmetry: compare window to its 180 rotation about centre
    rot = window[::-1, ::-1]
    num = np.abs(window - rot).sum()
    den = np.abs(window).sum() + 1e-10
    sym_err = num / den
    if sym_err > SYM_THRESH:
        return False, {'reason': 'sym', 'sym_err': sym_err}

    # 3.5 orientation alignment: major_vec of alpha-contour vs eigenvector of K for kappa_par
    # kappa_par_vec in (x,y); major_vec in (i,j) of window, need to map to (x,y)
    # In this code (i,j) indexes (x,y) so major_vec already in (x,y).
    cos_angle = abs(float(major_vec @ kappa_par_vec))
    # angle between them
    angle_deg = np.degrees(np.arccos(np.clip(cos_angle, 0, 1)))
    if angle_deg > ORIENT_TOL_DEG:
        return False, {'reason': 'orientation', 'angle_deg': angle_deg}

    return True, {
        'd_pt': d_pt, 'L_maj': L_maj, 'L_min': L_min, 'aspect': aspect,
        'sym_err': sym_err, 'angle_deg': angle_deg, 'cc_size': int(coords.shape[0])
    }


def process_snapshot(delta):
    """Extract motif records from one snapshot."""
    records = []
    sp = detect_stationary_points(delta)
    for x0, y0, i, j in sp:
        K = compute_hessian(delta, i, j)
        evals, evecs = np.linalg.eigh(K)
        # Order by |eigenvalue| descending -> kappa_par = larger |eig|, kappa_perp = smaller
        order = np.argsort(-np.abs(evals))
        kappa_par = evals[order[0]]
        kappa_perp = evals[order[1]]
        kappa_par_vec = evecs[:, order[0]]

        # Saddle condition
        if kappa_par * kappa_perp >= 0: continue

        accept, diag = motif_filter_check(delta, x0, y0, i, j, K, kappa_par_vec)
        if not accept: continue

        d_pt = diag['d_pt']
        mu = M0 + 0.5 * M2 * d_pt**2
        pi_coef = P0 + 0.5 * P3 * d_pt**2
        chi = 2 * mu * kappa_perp**2 / P0
        denom = 2*chi - 1
        r_star_pt = -2*chi / denom if abs(denom) > 1e-3 else np.nan

        records.append({
            'x0': x0, 'y0': y0, 'd_pt': d_pt,
            'kappa_par': kappa_par, 'kappa_perp': kappa_perp,
            's': kappa_par / kappa_perp,
            'mu': mu, 'pi': pi_coef, 'chi': chi, 'r_star_pt': r_star_pt,
            'L_maj': diag['L_maj'], 'aspect': diag['aspect']
        })
    return records


def run_realisation(seed):
    rng = np.random.default_rng(seed)
    delta = 0.3 + 0.4 * rng.random((L, L))
    lap_sym = fft_laplacian_symbol(L, DX)
    all_records = []
    for step in range(N_STEPS):
        delta = imex_step(delta, DT, lap_sym, rng)
        if step >= BURN_IN and (step - BURN_IN) % SNAPSHOT_EVERY == 0:
            recs = process_snapshot(delta)
            for r in recs:
                r['step'] = step
                r['seed'] = seed
            all_records.extend(recs)
    return all_records


def bootstrap_ci(values, B=1000, alpha=0.05, rng=None):
    if rng is None: rng = np.random.default_rng(12345)
    values = np.asarray(values)
    values = values[np.isfinite(values)]
    if len(values) < 3:
        return (np.nan, np.nan, np.nan)
    medians = []
    for _ in range(B):
        sample = rng.choice(values, size=len(values), replace=True)
        medians.append(np.median(sample))
    medians = np.array(medians)
    return (np.quantile(medians, alpha/2), np.median(values), np.quantile(medians, 1-alpha/2))


def main():
    rng_seed = np.random.default_rng(2026)
    seeds = [77, 123, 456, 789, 1011, 1213, 1415, 1617, 1819, 2021]
    all_recs = []
    per_real_medians = []
    for s in seeds:
        recs = run_realisation(s)
        all_recs.extend(recs)
        if recs:
            per_real_medians.append({
                'seed': s,
                'n_motifs': len(recs),
                'kappa_perp_med': float(np.median([abs(r['kappa_perp']) for r in recs])),
                's_med': float(np.median([r['s'] for r in recs])),
                'r_star_med': float(np.nanmedian([r['r_star_pt'] for r in recs]))
            })
        print(f"  seed={s}: n_motifs={len(recs)}", file=sys.stderr)

    # Aggregate
    kappa_perp_all = [abs(r['kappa_perp']) for r in all_recs]
    s_all = [r['s'] for r in all_recs]
    r_star_all = [r['r_star_pt'] for r in all_recs]
    d_pt_all = [r['d_pt'] for r in all_recs]

    # Bootstrap over realisations (resample per-realisation medians)
    B = 2000
    rng_bs = np.random.default_rng(99)
    def bs_over_reals(key):
        vals = [m[key] for m in per_real_medians if np.isfinite(m[key])]
        if len(vals) < 3: return (np.nan, np.nan, np.nan)
        vals = np.array(vals)
        meds = []
        for _ in range(B):
            smp = rng_bs.choice(vals, size=len(vals), replace=True)
            meds.append(np.median(smp))
        meds = np.array(meds)
        return (float(np.quantile(meds, 0.025)), float(np.median(vals)), float(np.quantile(meds, 0.975)))

    summary = {
        'parameters': {
            'L': L, 'DX': DX, 'DT': DT, 'SIGMA': SIGMA,
            'M0': M0, 'M2': M2, 'P0': P0, 'P3': P3,
            'N_STEPS': N_STEPS, 'BURN_IN': BURN_IN,
            'SNAPSHOT_EVERY': SNAPSHOT_EVERY,
            'N_REALISATIONS': len(seeds),
            'ALPHA': ALPHA, 'L_RAY': L_RAY, 'DELTA_THR': DELTA_THR,
            'ASPECT_MIN': ASPECT_MIN, 'SYM_THRESH': SYM_THRESH,
            'ORIENT_TOL_DEG': ORIENT_TOL_DEG
        },
        'n_motifs_total': len(all_recs),
        'n_motifs_per_realisation': [m['n_motifs'] for m in per_real_medians],
        'per_realisation_medians': per_real_medians,
        'pooled': {
            'kappa_perp_median': float(np.median(kappa_perp_all)) if kappa_perp_all else None,
            's_median': float(np.median(s_all)) if s_all else None,
            'r_star_median': float(np.nanmedian(r_star_all)) if r_star_all else None,
            'd_pt_median': float(np.median(d_pt_all)) if d_pt_all else None,
            'kappa_perp_iqr': [float(np.quantile(kappa_perp_all, 0.25)), float(np.quantile(kappa_perp_all, 0.75))] if kappa_perp_all else None,
            's_iqr': [float(np.quantile(s_all, 0.25)), float(np.quantile(s_all, 0.75))] if s_all else None,
            'r_star_iqr': [float(np.nanquantile(r_star_all, 0.25)), float(np.nanquantile(r_star_all, 0.75))] if r_star_all else None,
        },
        'bootstrap_95CI_over_realisations': {
            'kappa_perp': bs_over_reals('kappa_perp_med'),
            's': bs_over_reals('s_med'),
            'r_star': bs_over_reals('r_star_med')
        }
    }
    # Chain estimator
    if summary['pooled']['kappa_perp_median'] is not None:
        kp = summary['pooled']['kappa_perp_median']
        mu_eff = M0 + 0.5 * M2 * (summary['pooled']['d_pt_median'] or 0)**2
        chi = 2 * mu_eff * kp**2 / P0
        summary['r_star_chain_from_median_kappa_perp'] = -2*chi/(2*chi-1) if abs(2*chi-1) > 1e-3 else None
        summary['chi_from_median_kappa_perp'] = chi

    print(json.dumps(summary, indent=2))


if __name__ == '__main__':
    main()
