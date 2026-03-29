"""
edsim.regimes -- Physical regime classification and exploration.

This package classifies ED simulations into physical regimes based on
characteristic scales, computes physical observables, and produces
cross-regime comparison atlases.

Submodules
----------
manifold
    Regime definitions (quantum, mesoscopic, condensed_matter,
    gravitational, cosmological).
classifier
    Scale-based and parameter-based regime classification.
observables
    Physical observable extraction from PhysicalTimeSeries.
atlas
    Multi-regime atlas construction with figures and tables.
"""

from .manifold import (
    Regime,
    build_regime_manifold,
    get_regime,
    regime_table,
    QUANTUM,
    MESOSCOPIC,
    CONDENSED_MATTER,
    GRAVITATIONAL,
    COSMOLOGICAL,
)
from .classifier import (
    classify_scales,
    classify_params,
    classify_timeseries,
    compute_dimensionless_groups,
    regime_summary,
)
from .observables import (
    PhysicalObservables,
    compute_observables,
    observables_table,
    compare_observables,
)
from .atlas import (
    RegimeEntry,
    RegimeAtlas,
    run_regime_atlas,
    quick_regime_atlas,
)

__all__ = [
    # Manifold
    "Regime", "build_regime_manifold", "get_regime", "regime_table",
    "QUANTUM", "MESOSCOPIC", "CONDENSED_MATTER", "GRAVITATIONAL", "COSMOLOGICAL",
    # Classifier
    "classify_scales", "classify_params", "classify_timeseries",
    "compute_dimensionless_groups", "regime_summary",
    # Observables
    "PhysicalObservables", "compute_observables",
    "observables_table", "compare_observables",
    # Atlas
    "RegimeEntry", "RegimeAtlas",
    "run_regime_atlas", "quick_regime_atlas",
]
