"""
ED-Phys-02: Lattice Construction and Initial Conditions
=========================================================
Canonical source: ED-Phys-01 §7.1, §13.3

Provides lattice initialization with three IC modes:
  1. uniform + noise  (default cosmological IC)
  2. single localized gradient  (perturbation study)
  3. random perturbations  (structure formation study)
"""

import numpy as np
from typing import Literal
from ed_phys_config import EDParams


def create_initial_condition(
    params: EDParams,
    mode: Literal["uniform_noise", "localized_gradient", "random"] = "uniform_noise",
    rho_mean: float = 50.0,
    noise_amplitude: float = 0.1,
    seed: int | None = 42,
) -> np.ndarray:
    """Create initial density field ρ(x, 0).

    Parameters
    ----------
    params : EDParams
        Simulation parameters (determines grid shape).
    mode : str
        "uniform_noise"       — uniform ρ_mean + Gaussian noise (ED-Phys-01 §13.3)
        "localized_gradient"  — uniform background + single Gaussian bump
        "random"              — uniform ρ_mean + larger random perturbations
    rho_mean : float
        Mean initial density.
    noise_amplitude : float
        Standard deviation of noise (for uniform_noise/random) or
        bump height (for localized_gradient).
    seed : int or None
        Random seed for reproducibility.

    Returns
    -------
    rho : np.ndarray
        Initial density field, shape = params.grid_shape.
    """
    rng = np.random.default_rng(seed)
    shape = params.grid_shape

    if mode == "uniform_noise":
        # ED-Phys-01 §13.3: uniform ρ=50 with small Gaussian noise (~0.1)
        rho = rho_mean + noise_amplitude * rng.standard_normal(shape)

    elif mode == "localized_gradient":
        rho = np.full(shape, rho_mean, dtype=np.float64)
        if params.dimensions == 1:
            center = params.N // 2
            x = np.arange(params.N)
            bump = noise_amplitude * rho_mean * np.exp(
                -0.5 * ((x - center) / (params.N * 0.05)) ** 2
            )
            rho += bump
        else:
            cx, cy = params.N // 2, params.N // 2
            x, y = np.meshgrid(np.arange(params.N), np.arange(params.N),
                               indexing='ij')
            r2 = (x - cx) ** 2 + (y - cy) ** 2
            sigma = params.N * 0.05
            bump = noise_amplitude * rho_mean * np.exp(-0.5 * r2 / sigma ** 2)
            rho += bump

    elif mode == "random":
        # Larger perturbations for structure formation studies
        rho = rho_mean + (noise_amplitude * rho_mean) * rng.standard_normal(shape)

    else:
        raise ValueError(f"Unknown IC mode: {mode!r}")

    # Enforce positivity (ED-Phys-01 §8.4)
    np.clip(rho, 0.0, None, out=rho)

    return rho
