"""
edsim.visualization — Visualization engine for ED-SIM-02.

Provides field snapshots, invariant time-series plots, morphology
evolution, and animations for all dimensions d = 2..4.
"""

from .fields import plot_field_snapshot, plot_field_timeseries, plot_field_comparison
from .invariants import (
    plot_energy,
    plot_complexity,
    plot_spectral_entropy,
    plot_dissipation_channels,
    plot_correlation_length,
    plot_structure_function,
    plot_atlas_dashboard,
)
from .morphology import plot_morphology_fractions, plot_morphology_snapshot
from .animations import animate_field, animate_morphology, animate_invariant_dashboard

__all__ = [
    # Fields
    "plot_field_snapshot",
    "plot_field_timeseries",
    "plot_field_comparison",
    # Invariants
    "plot_energy",
    "plot_complexity",
    "plot_spectral_entropy",
    "plot_dissipation_channels",
    "plot_correlation_length",
    "plot_structure_function",
    "plot_atlas_dashboard",
    # Morphology
    "plot_morphology_fractions",
    "plot_morphology_snapshot",
    # Animations
    "animate_field",
    "animate_morphology",
    "animate_invariant_dashboard",
]
