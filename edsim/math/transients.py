"""
edsim.math.transients -- Transient classification for ED dynamics.

Classifies the transient behaviour of an ED simulation into one of
four canonical families based on energy curvature, modal turnover,
and entropy evolution.

Transient Types
---------------
Type I   -- Monotone relaxation: smooth, concave energy decay
Type II  -- Modal cascade: sequential mode-to-mode energy transfer
Type III -- Metastable plateau: extended near-constant energy phase
Type IV  -- Multi-scale burst: rapid, multi-mode energy redistribution
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

import numpy as np

from ..experiments.runner import TimeSeries
from ..core.parameters import EDParameters
from .modal import ModalSpectrum, ModalHierarchy


class TransientType(Enum):
    """Canonical transient types."""
    MONOTONE_RELAXATION = "Type I: Monotone relaxation"
    MODAL_CASCADE = "Type II: Modal cascade"
    METASTABLE_PLATEAU = "Type III: Metastable plateau"
    MULTI_SCALE_BURST = "Type IV: Multi-scale burst"


@dataclass
class TransientInvariants:
    """Scalar invariants characterising the transient.

    Attributes
    ----------
    relaxation_time : float
        Time for energy to decay to 1/e of initial.
    modal_turnover_rate : float
        Rate at which the dominant mode index changes.
    entropy_drop : float
        Total decrease in spectral entropy over the transient.
    entropy_slope : float
        Mean rate of spectral entropy change (dH/dt).
    correlation_growth_exponent : float
        Exponent alpha in xi(t) ~ t^alpha.
    energy_curvature : float
        Mean second derivative of E(t) (positive = convex, negative = concave).
    plateau_fraction : float
        Fraction of time during which |dE/dt| < threshold.
    mode_switches : int
        Number of times the dominant mode index changes.
    """

    relaxation_time: float = 0.0
    modal_turnover_rate: float = 0.0
    entropy_drop: float = 0.0
    entropy_slope: float = 0.0
    correlation_growth_exponent: float = 0.0
    energy_curvature: float = 0.0
    plateau_fraction: float = 0.0
    mode_switches: int = 0


@dataclass
class TransientClassification:
    """Full transient classification result.

    Attributes
    ----------
    transient_type : TransientType
        The assigned transient type.
    confidence : float
        Classification confidence in [0, 1].
    invariants : TransientInvariants
        Scalar invariants used in the classification.
    evidence : dict
        Detailed evidence for each criterion.
    """

    transient_type: TransientType
    confidence: float
    invariants: TransientInvariants
    evidence: dict


def compute_transient_invariants(
    ts: TimeSeries,
    modal_spectrum: ModalSpectrum = None,
) -> TransientInvariants:
    """Compute scalar transient invariants from a TimeSeries.

    Parameters
    ----------
    ts : TimeSeries
        Completed simulation output.
    modal_spectrum : ModalSpectrum, optional
        Pre-computed modal spectrum (avoids recomputation).

    Returns
    -------
    TransientInvariants
    """
    n = len(ts.times)
    if n < 3:
        return TransientInvariants()

    t = np.array(ts.times)
    E = np.array(ts.energy)
    H = np.array(ts.spectral_entropy) if ts.spectral_entropy else np.zeros(n)
    xi = np.array(ts.correlation_length) if ts.correlation_length else np.zeros(n)

    dt_arr = np.diff(t)
    dt_arr[dt_arr < 1e-30] = 1e-30

    # Relaxation time: time for E to drop to E[0]/e
    E_threshold = E[0] / np.e
    below = np.where(E <= E_threshold)[0]
    tau_relax = float(t[below[0]]) if below.size > 0 else float(t[-1])

    # Entropy slope and drop
    entropy_drop = float(H[0] - H[-1]) if H.size == n else 0.0
    T_total = t[-1] - t[0]
    entropy_slope = entropy_drop / T_total if T_total > 1e-30 else 0.0

    # Energy curvature (mean d^2E/dt^2)
    dE = np.diff(E) / dt_arr
    if dE.size > 1:
        d2E = np.diff(dE) / dt_arr[:-1]
        energy_curvature = float(np.mean(d2E))
    else:
        energy_curvature = 0.0

    # Plateau fraction: fraction of time where |dE/dt| < 1% of initial rate
    if dE.size > 0 and abs(dE[0]) > 1e-30:
        plateau_threshold = 0.01 * abs(dE[0])
        plateau_mask = np.abs(dE) < plateau_threshold
        plateau_fraction = float(plateau_mask.sum()) / dE.size
    else:
        plateau_fraction = 0.0

    # Modal turnover: count dominant-mode switches
    mode_switches = 0
    if modal_spectrum is not None and modal_spectrum.dominant_mode_idx.size > 1:
        dom = modal_spectrum.dominant_mode_idx
        mode_switches = int(np.sum(dom[1:] != dom[:-1]))

    turnover_rate = mode_switches / T_total if T_total > 1e-30 else 0.0

    # Correlation growth exponent: fit log(xi) vs log(t)
    corr_exp = 0.0
    if xi.size == n and n > 3:
        valid = (t > 1e-30) & (xi > 1e-30)
        if valid.sum() > 3:
            log_t = np.log(t[valid])
            log_xi = np.log(xi[valid])
            coeffs = np.polyfit(log_t, log_xi, 1)
            corr_exp = float(coeffs[0])

    return TransientInvariants(
        relaxation_time=tau_relax,
        modal_turnover_rate=turnover_rate,
        entropy_drop=entropy_drop,
        entropy_slope=entropy_slope,
        correlation_growth_exponent=corr_exp,
        energy_curvature=energy_curvature,
        plateau_fraction=plateau_fraction,
        mode_switches=mode_switches,
    )


def classify_transient(
    ts: TimeSeries,
    modal_hierarchy: ModalHierarchy = None,
    modal_spectrum: ModalSpectrum = None,
) -> TransientClassification:
    """Classify the transient into one of four canonical types.

    Classification criteria (applied in order of priority):

    Type III (Metastable plateau):
        plateau_fraction > 0.3

    Type IV (Multi-scale burst):
        mode_switches >= 3 AND energy_curvature > 0 (convex phases)

    Type II (Modal cascade):
        mode_switches >= 1 AND hierarchy_ratio < 3.0

    Type I (Monotone relaxation):
        Default when no other type matches.  Energy curvature is
        negative (concave), entropy decreases monotonically.

    Parameters
    ----------
    ts : TimeSeries
        Completed simulation output.
    modal_hierarchy : ModalHierarchy, optional
        Pre-computed hierarchy.
    modal_spectrum : ModalSpectrum, optional
        Pre-computed spectrum.

    Returns
    -------
    TransientClassification
    """
    inv = compute_transient_invariants(ts, modal_spectrum)

    h_ratio = modal_hierarchy.hierarchy_ratio if modal_hierarchy else 100.0

    evidence = {
        "energy_curvature": inv.energy_curvature,
        "plateau_fraction": inv.plateau_fraction,
        "mode_switches": inv.mode_switches,
        "hierarchy_ratio": h_ratio,
        "entropy_slope": inv.entropy_slope,
    }

    # Type III: metastable plateau
    if inv.plateau_fraction > 0.3:
        confidence = min(1.0, inv.plateau_fraction / 0.5)
        return TransientClassification(
            transient_type=TransientType.METASTABLE_PLATEAU,
            confidence=confidence,
            invariants=inv,
            evidence=evidence,
        )

    # Type IV: multi-scale burst
    if inv.mode_switches >= 3 and inv.energy_curvature > 0:
        confidence = min(1.0, inv.mode_switches / 5.0)
        return TransientClassification(
            transient_type=TransientType.MULTI_SCALE_BURST,
            confidence=confidence,
            invariants=inv,
            evidence=evidence,
        )

    # Type II: modal cascade
    if inv.mode_switches >= 1 and h_ratio < 3.0:
        confidence = min(1.0, inv.mode_switches / 3.0)
        return TransientClassification(
            transient_type=TransientType.MODAL_CASCADE,
            confidence=confidence,
            invariants=inv,
            evidence=evidence,
        )

    # Type I: monotone relaxation (default)
    confidence = min(1.0, abs(inv.energy_curvature) * 100 + 0.5)
    return TransientClassification(
        transient_type=TransientType.MONOTONE_RELAXATION,
        confidence=min(confidence, 1.0),
        invariants=inv,
        evidence=evidence,
    )
