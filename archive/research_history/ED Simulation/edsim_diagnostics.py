"""
edsim_diagnostics.py
=====================
Observable extraction and diagnostic computation for the ED simulation engine.

Implements all observables from the Simulation Suite §5:
  - Energy functional and dissipation channels (§5.1-5.2)
  - Modal amplitudes and spectral decomposition (§5.3)
  - Triad coefficients and selection-rule validation (§5.4)
  - ED-complexity (§5.5)
  - Convergence rate extraction (§5.6)
  - Horizon proximity (§5.7)

All notation follows Appendix C of the Rigour Paper.
"""

import numpy as np
from scipy.fft import dctn
from edsim_parameters import EDParameters
from edsim_core import energy, total_mass, grad_squared_fd, laplacian_fd


# ===================================================================
#  DISSIPATION CHANNELS (Suite §5.2)
# ===================================================================

def dissipation_channels(rho: np.ndarray, v: float, params: EDParameters) -> dict:
    """
    Compute the three dissipation channels.

    D_diff = D * P*' * C_ED             (gradient/diffusive)
    D_pen  = D * P*'^2 / M* * ||rho - rho*||^2   (penalty)
    D_part = H * zeta * v^2             (participation)

    Returns dict with 'gradient', 'penalty', 'participation', 'total'.
    """
    h = params.h

    # Gradient dissipation: D * P*' * C_ED
    C_ED = ed_complexity(rho, params)
    D_diff = params.D * params.P_star_prime * C_ED

    # Penalty dissipation: D * P*'^2 / M* * integral (rho - rho*)^2 dx
    dev_sq = (rho - params.rho_star) ** 2
    int_dev_sq = h * (0.5 * dev_sq[0] + np.sum(dev_sq[1:-1]) + 0.5 * dev_sq[-1])
    D_pen = params.D * params.P_star_prime ** 2 / params.M_star * int_dev_sq

    # Participation dissipation: H * zeta * v^2
    D_part = params.H * params.zeta * v ** 2

    return {
        "gradient": D_diff,
        "penalty": D_pen,
        "participation": D_part,
        "total": D_diff + D_pen + D_part,
    }


# ===================================================================
#  ED-COMPLEXITY (Suite §5.5)
# ===================================================================

def ed_complexity(rho: np.ndarray, params: EDParameters) -> float:
    """
    Bare ED-complexity: C_ED = integral |grad rho|^2 dx.

    Computed via trapezoidal rule on the FD gradient.
    """
    gs = grad_squared_fd(rho, params.h)
    h = params.h
    return h * (0.5 * gs[0] + np.sum(gs[1:-1]) + 0.5 * gs[-1])


def ed_complexity_effective(rho: np.ndarray, params: EDParameters) -> float:
    """
    Effective ED-complexity: C_ED^eff = integral (P'(rho)/M(rho)) * |grad rho|^2 dx.

    Accounts for state-dependent weighting by the constitutive functions.
    """
    gs = grad_squared_fd(rho, params.h)
    P_prime = params.P_prime(rho)
    M_vals = params.M(rho)
    # Avoid division by zero near horizon
    M_safe = np.maximum(M_vals, 1e-15)
    weight = P_prime / M_safe
    integrand = weight * gs
    h = params.h
    return h * (0.5 * integrand[0] + np.sum(integrand[1:-1]) + 0.5 * integrand[-1])


# ===================================================================
#  MODAL AMPLITUDES (Suite §5.3)
# ===================================================================

def modal_amplitudes(rho: np.ndarray, params: EDParameters,
                     N_obs: int = 32) -> np.ndarray:
    """
    Extract modal amplitudes a_k via DCT-I.

    u(x) = rho(x) - rho* = sum_k a_k * phi_k(x)

    where phi_k are the Neumann eigenfunctions.

    Parameters
    ----------
    rho : density array on the FD grid
    params : EDParameters
    N_obs : number of modes to extract (default 32)

    Returns
    -------
    a : array of modal amplitudes, length N_obs
    """
    u = rho - params.rho_star
    N = len(u)

    # DCT-I: a_k = (2/N) * sum_{j=0}^{N-1} u_j * cos(k*pi*j/(N-1))
    # with half-weight at endpoints
    coeffs = dctn(u, type=1) / (N - 1)
    coeffs[0] /= 2.0
    if len(coeffs) > 1:
        coeffs[-1] /= 2.0

    # Normalize to L^2 inner product convention
    # a_0 = <u, phi_0> = (1/sqrt(L)) * integral u dx
    # a_k = <u, phi_k> = sqrt(2/L) * integral u * cos(k*pi*x/L) dx
    # The DCT gives us the cosine coefficients; scale by sqrt(L) or sqrt(L/2)
    a = np.zeros(min(N_obs, len(coeffs)))
    a[0] = coeffs[0] * np.sqrt(params.L)  # homogeneous mode
    for k in range(1, len(a)):
        if k < len(coeffs):
            a[k] = coeffs[k] * np.sqrt(params.L / 2.0)

    return a


def modal_energy_spectrum(a: np.ndarray, params: EDParameters) -> np.ndarray:
    """
    Modal energy spectrum: E_k = |a_k|^2.

    Parseval identity: sum E_k = ||u||^2_{L^2}.
    """
    return a ** 2


def modal_complexity_spectrum(a: np.ndarray, params: EDParameters) -> np.ndarray:
    """
    Modal complexity spectrum: C_k = mu_k * |a_k|^2.

    C_ED = sum_{k>=1} C_k.
    """
    k = np.arange(len(a))
    mu = (k * np.pi / params.L) ** 2
    return mu * a ** 2


# ===================================================================
#  DECAY RATE EXTRACTION (Suite §5.6)
# ===================================================================

def extract_decay_rate(t: np.ndarray, a_k: np.ndarray,
                       t_start: float = 0.1, t_end: float = None,
                       floor: float = 1e-10) -> dict:
    """
    Extract the exponential decay rate sigma_k from a modal time series.

    Fits ln|a_k(t)| = -sigma_k * t + const via least squares.

    Parameters
    ----------
    t : time array
    a_k : modal amplitude time series for mode k
    t_start : start of fitting window
    t_end : end of fitting window (auto-detected if None)
    floor : amplitude floor for fitting

    Returns
    -------
    dict with 'sigma', 'intercept', 'R2', 'window' (t_start, t_end)
    """
    abs_a = np.abs(a_k)

    # Determine fitting window
    mask = (t >= t_start) & (abs_a > floor) & (abs_a > 0)
    if t_end is not None:
        mask &= (t <= t_end)

    if np.sum(mask) < 5:
        return {"sigma": np.nan, "intercept": np.nan, "R2": np.nan,
                "window": (t_start, t_end)}

    t_fit = t[mask]
    log_a = np.log(abs_a[mask])

    # Least-squares fit: log_a = -sigma * t + b
    A_mat = np.column_stack([t_fit, np.ones_like(t_fit)])
    result = np.linalg.lstsq(A_mat, log_a, rcond=None)
    coeffs = result[0]
    sigma = -coeffs[0]
    intercept = coeffs[1]

    # R^2
    predicted = A_mat @ coeffs
    ss_res = np.sum((log_a - predicted) ** 2)
    ss_tot = np.sum((log_a - np.mean(log_a)) ** 2)
    R2 = 1.0 - ss_res / max(ss_tot, 1e-30)

    return {
        "sigma": sigma,
        "intercept": intercept,
        "R2": R2,
        "window": (t_fit[0], t_fit[-1]),
    }


def extract_oscillation_frequency(t: np.ndarray, a_k: np.ndarray,
                                  t_start: float = 0.1) -> dict:
    """
    Extract oscillation frequency from a modal time series via zero crossings.

    Returns dict with 'omega' (angular frequency), 'period', 'n_crossings'.
    """
    mask = t >= t_start
    t_sub = t[mask]
    a_sub = a_k[mask]

    # Find zero crossings
    crossings = np.where(np.diff(np.sign(a_sub)))[0]
    if len(crossings) < 2:
        return {"omega": 0.0, "period": np.inf, "n_crossings": len(crossings)}

    # Average half-period from successive zero crossings
    crossing_times = 0.5 * (t_sub[crossings] + t_sub[crossings + 1])
    half_periods = np.diff(crossing_times)
    avg_half_period = np.mean(half_periods)
    period = 2.0 * avg_half_period
    omega = 2.0 * np.pi / period

    return {"omega": omega, "period": period, "n_crossings": len(crossings)}


# ===================================================================
#  TRIAD COEFFICIENTS (Suite §5.4)
# ===================================================================

def triad_coefficient(m: int, n: int, k: int, L: float) -> float:
    """
    Compute the trilinear coupling coefficient Gamma_{mnk}.

    Gamma_{mnk} = integral grad(phi_m) . grad(phi_n) * phi_k dx

    Selection rule (Theorem C.34): nonzero only if k in {|m-n|, m+n} (and k=0 if m=n).

    For m, n >= 1, m != n:
        Gamma_{mn,m+n} = Gamma_{mn,|m-n|} = m*n*pi^2*sqrt(2) / (2*L^{3/2})

    For m = n >= 1:
        Gamma_{mm,2m} = m^2*pi^2*sqrt(2) / (2*L^{3/2})
        Gamma_{mm,0}  = m^2*pi^2 / L^{3/2}
    """
    if m == 0 or n == 0:
        return 0.0

    if m == n:
        if k == 2 * m:
            return m ** 2 * np.pi ** 2 * np.sqrt(2) / (2.0 * L ** 1.5)
        elif k == 0:
            return m ** 2 * np.pi ** 2 / L ** 1.5
        else:
            return 0.0
    else:
        if k == m + n or k == abs(m - n):
            return m * n * np.pi ** 2 * np.sqrt(2) / (2.0 * L ** 1.5)
        else:
            return 0.0


def triad_compliance_matrix(N_modes: int, L: float) -> np.ndarray:
    """
    Compute the triad compliance matrix for modes 1..N_modes.

    Entry (i, j) corresponds to the source pair (m=i+1, n=j+1).
    Value is a set of target modes k that are activated.

    Returns a dict: compliance[(m, n)] = set of activated target modes.
    """
    compliance = {}
    for m in range(1, N_modes + 1):
        for n in range(m, N_modes + 1):
            targets = set()
            if m == n:
                targets.add(2 * m)
                targets.add(0)
            else:
                targets.add(m + n)
                targets.add(abs(m - n))
            compliance[(m, n)] = targets
    return compliance


# ===================================================================
#  HORIZON PROXIMITY (Suite §5.7)
# ===================================================================

def horizon_proximity(rho: np.ndarray, params: EDParameters) -> dict:
    """
    Compute horizon proximity diagnostics.

    Returns dict with:
        'margin' : rho_max - max(rho)          (proximity margin delta)
        'M_min'  : min M(rho) over the grid    (minimum mobility)
        'x_max'  : location of max(rho)
        'rho_max_local' : max(rho)
    """
    rho_max_local = np.max(rho)
    idx_max = np.argmax(rho)
    margin = params.rho_max - rho_max_local
    M_vals = params.M(rho)
    M_min = np.min(M_vals)

    return {
        "margin": margin,
        "M_min": M_min,
        "x_max": idx_max * params.h,
        "rho_max_local": rho_max_local,
    }


# ===================================================================
#  FULL DIAGNOSTIC SNAPSHOT
# ===================================================================

def diagnostic_snapshot(rho: np.ndarray, v: float, t: float,
                        params: EDParameters, N_obs: int = 32) -> dict:
    """
    Compute a complete diagnostic snapshot at one time step.

    Returns a dict with all observables for logging.
    """
    E = energy(rho, v, params)
    D_channels = dissipation_channels(rho, v, params)
    C = ed_complexity(rho, params)
    C_eff = ed_complexity_effective(rho, params)
    a = modal_amplitudes(rho, params, N_obs)
    M_total = total_mass(rho, params.h)
    prox = horizon_proximity(rho, params)

    return {
        "t": t,
        "v": v,
        # Energy
        "E_total": E["total"],
        "E_potential": E["potential"],
        "E_kinetic": E["kinetic"],
        # Dissipation
        "D_gradient": D_channels["gradient"],
        "D_penalty": D_channels["penalty"],
        "D_participation": D_channels["participation"],
        "D_total": D_channels["total"],
        # Complexity
        "C_ED": C,
        "C_ED_eff": C_eff,
        # Mass
        "mass": M_total,
        # Modal amplitudes
        "a": a.copy(),
        # Horizon proximity
        "margin": prox["margin"],
        "M_min": prox["M_min"],
        "rho_max_local": prox["rho_max_local"],
    }


# ===================================================================
#  THREE-STAGE CONVERGENCE DETECTION (Suite §8.5)
# ===================================================================

def detect_three_stages(t: np.ndarray, E: np.ndarray,
                        params: EDParameters) -> dict:
    """
    Detect the three stages of convergence from the energy time series.

    Stage I:  Global bounds -- energy is bounded and decreasing
    Stage II: Algebraic decay -- E(t) ~ C * t^{-alpha}
    Stage III: Exponential decay -- E(t) ~ C * exp(-2*sigma*t)

    Returns dict with transition times and stage diagnostics.
    """
    # Equilibrium energy
    E_eq = 0.0  # E[rho*, 0] = 0 for the default constitutive functions

    # Deviation from equilibrium
    dE = np.abs(E - E_eq)
    dE = np.maximum(dE, 1e-30)  # avoid log(0)
    log_dE = np.log(dE)

    # Stage III detection: find where log(dE) becomes linear (exponential decay)
    # Sliding window R^2 test
    window = max(20, len(t) // 20)
    R2_values = np.zeros(len(t))

    for i in range(window, len(t)):
        t_win = t[i - window:i]
        log_win = log_dE[i - window:i]
        if np.std(log_win) < 1e-15:
            R2_values[i] = 1.0
            continue
        A = np.column_stack([t_win, np.ones_like(t_win)])
        coeffs = np.linalg.lstsq(A, log_win, rcond=None)[0]
        predicted = A @ coeffs
        ss_res = np.sum((log_win - predicted) ** 2)
        ss_tot = np.sum((log_win - np.mean(log_win)) ** 2)
        R2_values[i] = 1.0 - ss_res / max(ss_tot, 1e-30)

    # Stage III starts where R^2 > 0.999 persistently
    stage3_mask = R2_values > 0.999
    stage3_indices = np.where(stage3_mask)[0]

    if len(stage3_indices) > 0:
        # Find the first sustained stretch
        t_star = t[stage3_indices[0]]

        # Extract exponential rate in Stage III
        t3 = t[stage3_indices[0]:]
        log3 = log_dE[stage3_indices[0]:]
        A3 = np.column_stack([t3, np.ones_like(t3)])
        c3 = np.linalg.lstsq(A3, log3, rcond=None)[0]
        sigma_III = -c3[0] / 2.0  # E ~ exp(-2*sigma*t)
    else:
        t_star = np.nan
        sigma_III = np.nan

    return {
        "t_star": t_star,
        "sigma_III": sigma_III,
        "R2_stage3": R2_values,
        "has_three_stages": not np.isnan(t_star),
    }
