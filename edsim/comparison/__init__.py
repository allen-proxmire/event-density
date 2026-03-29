"""
edsim.comparison -- Cross-framework comparison engine for Event Density.

Compares ED to six theoretical frameworks along five structural axes,
identifies overlaps and divergences, extracts unique features, and
generates comparison reports.

Submodules
----------
frameworks
    Structured descriptions of ED and six comparison frameworks.
matrix
    Cross-framework comparison matrix construction.
analysis
    Overlap, divergence, and uniqueness extraction.
report
    Auto-generated Markdown comparison report.
"""

from .frameworks import (
    Framework,
    load_frameworks,
    get_framework,
    CAUSAL_SETS,
    ENTROPIC_GRAVITY,
    CONSTRUCTOR_THEORY,
    HYDRODYNAMICS,
    STATISTICAL_MECHANICS,
    QUANTUM_FOUNDATIONS,
)
from .matrix import (
    CellEntry,
    ComparisonMatrix,
    build_comparison_matrix,
)
from .analysis import (
    OverlapEntry,
    DivergenceEntry,
    UniqueFeature,
    AnalysisResult,
    identify_overlaps,
    identify_divergences,
    extract_unique_features,
    run_analysis,
)
from .report import build_cross_framework_report

__all__ = [
    # Frameworks
    "Framework", "load_frameworks", "get_framework",
    "CAUSAL_SETS", "ENTROPIC_GRAVITY", "CONSTRUCTOR_THEORY",
    "HYDRODYNAMICS", "STATISTICAL_MECHANICS", "QUANTUM_FOUNDATIONS",
    # Matrix
    "CellEntry", "ComparisonMatrix", "build_comparison_matrix",
    # Analysis
    "OverlapEntry", "DivergenceEntry", "UniqueFeature", "AnalysisResult",
    "identify_overlaps", "identify_divergences", "extract_unique_features",
    "run_analysis",
    # Report
    "build_cross_framework_report",
]
