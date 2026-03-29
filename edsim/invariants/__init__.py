"""
edsim.invariants — Invariant computation engine for ED-SIM-02.

Computes the full ED invariant atlas: energy, spectral, dissipation,
morphology, topology, and correlation invariants.
"""

from .atlas import compute_atlas
from .energy import lyapunov_energy, total_mass, ed_complexity
from .spectral import spectral_entropy, modal_hierarchy, spectral_anisotropy
from .dissipation import dissipation_channels
from .morphology import hessian_eigenvalues, morphology_fractions
from .topology import euler_characteristic, betti_numbers
from .correlation import correlation_length, structure_function

__all__ = [
    "compute_atlas",
    "lyapunov_energy", "total_mass", "ed_complexity",
    "spectral_entropy", "modal_hierarchy", "spectral_anisotropy",
    "dissipation_channels",
    "hessian_eigenvalues", "morphology_fractions",
    "euler_characteristic", "betti_numbers",
    "correlation_length", "structure_function",
]
