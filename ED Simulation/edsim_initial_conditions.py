"""
edsim_initial_conditions.py
============================
Initial condition generators for the canonical ED system.

Implements IC-A through IC-D from the Simulation Suite §2.1.
All initial conditions satisfy:
  - 0 < rho(x, 0) < rho_max  (positivity and sub-capacity)
  - Neumann compatibility: d rho/dx = 0 at x = 0, L
  - Mass consistency: integral of rho is well-defined

Notation follows Appendix C of the Rigour Paper.
"""

import numpy as np
from edsim_parameters import EDParameters


def ic_single_mode(x: np.ndarray, params: EDParameters,
                   A: float = 0.05, n: int = 1, v0: float = 0.0):
    """
    IC-A: Single-mode cosine perturbation.

    rho(x, 0) = rho* + A * cos(n * pi * x / L)
    v(0) = v0

    Parameters
    ----------
    x : grid array
    params : EDParameters
    A : perturbation amplitude
    n : mode number (n >= 1)
    v0 : initial participation

    Returns
    -------
    rho0 : density array
    v0_val : scalar participation value
    """
    rho0 = params.rho_star + A * np.cos(n * np.pi * x / params.L)
    _validate_ic(rho0, params, "IC-A")
    return rho0, v0


def ic_multi_mode(x: np.ndarray, params: EDParameters,
                  A: float = 0.05, N_m: int = 8, v0: float = 0.0):
    """
    IC-B: Multi-mode cosine superposition.

    rho(x, 0) = rho* + sum_{k=1}^{N_m} A_k * cos(k * pi * x / L)

    where A_k = A / sqrt(N_m) for equal energy per mode.

    Parameters
    ----------
    x : grid array
    params : EDParameters
    A : total perturbation amplitude
    N_m : number of modes
    v0 : initial participation

    Returns
    -------
    rho0 : density array
    v0_val : scalar participation value
    """
    A_k = A / np.sqrt(N_m)
    rho0 = np.full_like(x, params.rho_star)
    for k in range(1, N_m + 1):
        rho0 += A_k * np.cos(k * np.pi * x / params.L)
    _validate_ic(rho0, params, "IC-B")
    return rho0, v0


def ic_gaussian(x: np.ndarray, params: EDParameters,
                A: float = 0.3, x0: float = None, sigma: float = 0.06,
                v0: float = 0.0):
    """
    IC-C: Localized Gaussian perturbation.

    rho(x, 0) = rho* + A * exp(-(x - x0)^2 / (2 * sigma^2))
    v(0) = v0

    Parameters
    ----------
    x : grid array
    params : EDParameters
    A : peak amplitude
    x0 : center (default: L/2)
    sigma : width
    v0 : initial participation

    Returns
    -------
    rho0 : density array
    v0_val : scalar participation value
    """
    if x0 is None:
        x0 = params.L / 2.0
    rho0 = params.rho_star + A * np.exp(-(x - x0) ** 2 / (2.0 * sigma ** 2))
    _validate_ic(rho0, params, "IC-C")
    return rho0, v0


def ic_near_capacity(x: np.ndarray, params: EDParameters,
                     delta: float = 0.05, A: float = 0.02, v0: float = 0.0):
    """
    IC-D: Near-capacity perturbation (horizon exploration).

    rho(x, 0) = rho_max - delta + A * cos(pi * x / L)
    v(0) = v0

    Parameters
    ----------
    x : grid array
    params : EDParameters
    delta : distance below rho_max for the baseline
    A : perturbation amplitude (must satisfy A < delta)
    v0 : initial participation

    Returns
    -------
    rho0 : density array
    v0_val : scalar participation value
    """
    assert A < delta, f"IC-D requires A={A} < delta={delta}"
    rho0 = (params.rho_max - delta) + A * np.cos(np.pi * x / params.L)
    _validate_ic(rho0, params, "IC-D")
    return rho0, v0


def ic_custom(x: np.ndarray, params: EDParameters,
              rho_func, v0: float = 0.0):
    """
    Custom initial condition from a user-provided function.

    Parameters
    ----------
    x : grid array
    params : EDParameters
    rho_func : callable, rho_func(x, params) -> np.ndarray
    v0 : initial participation

    Returns
    -------
    rho0 : density array
    v0_val : scalar participation value
    """
    rho0 = rho_func(x, params)
    _validate_ic(rho0, params, "IC-custom")
    return rho0, v0


# ---------------------------------------------------------------------------
#  Validation
# ---------------------------------------------------------------------------

def _validate_ic(rho0: np.ndarray, params: EDParameters, label: str):
    """
    Validate initial condition against the admissible region O.

    Checks:
    1. Positivity: rho(x, 0) > 0 everywhere
    2. Sub-capacity: rho(x, 0) < rho_max everywhere
    3. Finite energy: no NaN or Inf values
    """
    if np.any(np.isnan(rho0)) or np.any(np.isinf(rho0)):
        raise ValueError(f"{label}: initial condition contains NaN or Inf")
    if np.any(rho0 <= 0.0):
        raise ValueError(
            f"{label}: positivity violated. min(rho0) = {np.min(rho0):.6e}")
    if np.any(rho0 >= params.rho_max):
        raise ValueError(
            f"{label}: sub-capacity violated. max(rho0) = {np.max(rho0):.6e}, "
            f"rho_max = {params.rho_max}")


# ---------------------------------------------------------------------------
#  Convenience: lookup by name
# ---------------------------------------------------------------------------

IC_REGISTRY = {
    "A": ic_single_mode,
    "B": ic_multi_mode,
    "C": ic_gaussian,
    "D": ic_near_capacity,
}


def load_ic(name: str, x: np.ndarray, params: EDParameters, **kwargs):
    """
    Load an initial condition by name ('A', 'B', 'C', 'D').

    Parameters
    ----------
    name : IC identifier
    x : grid array
    params : EDParameters
    **kwargs : passed to the IC generator

    Returns
    -------
    rho0, v0
    """
    if name not in IC_REGISTRY:
        raise ValueError(f"Unknown IC '{name}'. Choose from {list(IC_REGISTRY.keys())}")
    return IC_REGISTRY[name](x, params, **kwargs)
