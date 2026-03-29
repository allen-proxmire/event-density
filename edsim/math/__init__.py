"""
edsim.math -- Formal mathematical development layer for ED-SIM-02.

Provides modal decomposition, transient classification, architectural
axiom scaffolding, formal law statements, and auto-generated appendix.

Submodules
----------
modal
    Time-resolved spectral decomposition and hierarchy extraction.
transients
    Transient classification into four canonical families.
architecture
    Axioms P1-P7 and the derivation tree to the canonical PDE.
laws
    The nine architectural laws with verification functions.
appendix
    Auto-generated mathematical appendix for the manuscript.
"""

from .modal import (
    ModalSpectrum,
    ModalHierarchy,
    compute_modal_spectrum,
    extract_modal_hierarchy,
    modal_decay_rates,
)
from .transients import (
    TransientType,
    TransientInvariants,
    TransientClassification,
    compute_transient_invariants,
    classify_transient,
)
from .architecture import (
    Axiom,
    DerivationStep,
    CanonicalPDE,
    ArchitecturalAxioms,
    derive_canonical_pde,
    derivation_to_markdown,
)
from .laws import (
    Law,
    ALL_LAWS,
    LAW_1, LAW_2, LAW_3, LAW_4, LAW_5,
    LAW_6, LAW_7, LAW_8, LAW_9,
    verify_law,
    verify_all_laws,
    laws_to_markdown,
)
from .appendix import build_math_appendix

__all__ = [
    # Modal
    "ModalSpectrum", "ModalHierarchy",
    "compute_modal_spectrum", "extract_modal_hierarchy", "modal_decay_rates",
    # Transients
    "TransientType", "TransientInvariants", "TransientClassification",
    "compute_transient_invariants", "classify_transient",
    # Architecture
    "Axiom", "DerivationStep", "CanonicalPDE", "ArchitecturalAxioms",
    "derive_canonical_pde", "derivation_to_markdown",
    # Laws
    "Law", "ALL_LAWS",
    "LAW_1", "LAW_2", "LAW_3", "LAW_4", "LAW_5",
    "LAW_6", "LAW_7", "LAW_8", "LAW_9",
    "verify_law", "verify_all_laws", "laws_to_markdown",
    # Appendix
    "build_math_appendix",
]
