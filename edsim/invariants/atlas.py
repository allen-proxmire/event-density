"""
edsim.invariants.atlas — Invariant atlas computation.

Top-level function that calls invariant families and returns
a merged dictionary. Currently implements:
    - Energy layer: Lyapunov energy, ED-complexity, mass
    - Spectral layer: spectral entropy, modal hierarchy
    - Morphology layer: Hessian eigenvalues, morphology fractions
    - Dissipation layer: R_grad, R_pen, R_part channels
    - Correlation layer: correlation length, structure function S_2
    - Topology layer: Euler characteristic, Betti numbers
"""

from __future__ import annotations

import numpy as np

from ..core.parameters import EDParameters
from .energy import lyapunov_energy, ed_complexity, total_mass
from .spectral import spectral_entropy, modal_hierarchy
from .morphology import hessian_eigenvalues, morphology_fractions
from .dissipation import dissipation_channels
from .correlation import correlation_length, structure_function_2
from .topology import euler_characteristic, betti_numbers


def compute_atlas(
    rho: np.ndarray,
    v: float,
    params: EDParameters,
) -> dict:
    """Compute the invariant atlas for the current state (rho, v).

    Returns all implemented invariant layers:
        - energy:              Lyapunov functional E[rho]
        - complexity:          ED-complexity C[rho]
        - mass:                Total mass M[rho]
        - spectral_entropy:    H = -sum(p_k * log p_k)
        - modal_hierarchy:     Sorted |rho_hat_k|, descending
        - morphology_fractions: {blob, sheet, filament, pancake}
        - R_grad, R_pen, R_part: dissipation channel ratios
        - correlation_length:  xi from autocorrelation
        - structure_r, structure_S2: second-order structure function
        - euler_characteristic: chi of excursion set {rho >= rho_star}
        - betti_numbers: [beta_0, ..., beta_{d-1}]

    Parameters
    ----------
    rho : np.ndarray
        Density field of shape params.N.
    v : float
        Participation variable.
    params : EDParameters
        Simulation parameters.

    Returns
    -------
    dict
        Invariant dictionary.
    """
    E = lyapunov_energy(rho, params)
    C = ed_complexity(rho, params)
    M = total_mass(rho, params)
    H = spectral_entropy(rho, params)
    modes = modal_hierarchy(rho, params, max_modes=64)

    eigvals = hessian_eigenvalues(rho, params)
    morph = morphology_fractions(eigvals, params)

    diss = dissipation_channels(rho, v, params)

    xi = correlation_length(rho, params)
    r_bins, S2 = structure_function_2(rho, params, n_bins=16)

    chi = euler_characteristic(rho, params)
    betti = betti_numbers(rho, params)

    return {
        "energy": E,
        "complexity": C,
        "mass": M,
        "spectral_entropy": H,
        "modal_hierarchy": modes,
        "morphology_fractions": morph,
        "R_grad": diss["R_grad"],
        "R_pen": diss["R_pen"],
        "R_part": diss["R_part"],
        "correlation_length": xi,
        "structure_r": r_bins,
        "structure_S2": S2,
        "euler_characteristic": chi,
        "betti_numbers": betti,
        "v": v,
    }
