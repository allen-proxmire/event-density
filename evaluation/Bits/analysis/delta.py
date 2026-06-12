"""Delta - the determinability-boundary bits measure.

Delta contrasts predictability WITHIN a reach stratum against predictability
ACROSS the decoupling boundary:

    Delta = M1 - M2          (bits)

  M1 = within-stratum predictability  = MI(A_left ; A_right)   (two halves of one
       stratum, reach-connected -> should share information)
  M2 = across-boundary predictability = MI(A ; B)              (two strata, reach-
       decoupled -> should share ~no information)
  M3 = shuffle/null control           = MI(A ; shuffled B)     (the finite-sample
       floor of the estimator; M2 should match M3)

A positive Delta is the bits of determination the architecture forfeits at the
decoupling surface: information that propagates within a stratum but does not
cross it. M1, M2, M3 use the SAME Miller-Madow-corrected histogram estimator and
the SAME binning, so Delta differences out the estimator's finite-sample bias.

This module computes; it does not run the simulator. The dataset is supplied by
the caller (ensemble of MWE runs). Deterministic given the ensemble seeds.
"""
from __future__ import annotations

import numpy as np

from .entropy import mutual_information, mutual_information_ksg

# 1 nat = 1 / ln(2) bits.
NATS_TO_BITS = 1.0 / np.log(2.0)


def _mi_bits(x, y, estimator: str = "hist", bins: int = 2, k: int = 5) -> float:
    """MI in bits, via the chosen estimator.

    estimator="hist": Miller-Madow corrected histogram (bin-based; saturates on
                      near-deterministic pairs).
    estimator="ksg":  Kraskov k-NN (binning-free; handles vectors and strong
                      dependence). Required for the observable sweep.
    """
    x = np.asarray(x)
    y = np.asarray(y)
    if estimator == "ksg":
        return float(mutual_information_ksg(x, y, k=k) * NATS_TO_BITS)
    return float(mutual_information(x, y, bins=bins) * NATS_TO_BITS)


def _shuffle(arr, seed: int = 0):
    """Shuffle along the sample axis (rows), preserving feature structure."""
    rng = np.random.default_rng(seed)
    a = np.asarray(arr).copy()
    idx = rng.permutation(len(a))
    return a[idx]


def compute_M1(dataset: dict, estimator: str = "hist", bins: int = 2, k: int = 5) -> float:
    """Within-stratum predictability: MI between two halves of stratum A.

    dataset["A_left"], dataset["A_right"]: per-run features of the two halves of
    stratum A (reach-connected). Reach-connected halves share information, so
    M1 > 0. Features may be scalar (shape (N,)) or vector (shape (N, d)).
    """
    return _mi_bits(dataset["A_left"], dataset["A_right"], estimator, bins, k)


def compute_M2(dataset: dict, estimator: str = "hist", bins: int = 2, k: int = 5) -> float:
    """Across-boundary predictability: MI(A_feature ; B_feature). ~0 expected."""
    return _mi_bits(dataset["A"], dataset["B"], estimator, bins, k)


def compute_M3(dataset: dict, estimator: str = "hist", bins: int = 2, k: int = 5,
               seed: int = 0) -> float:
    """Shuffle/null control: MI(A_feature ; shuffled B_feature). Estimator floor."""
    return _mi_bits(dataset["A"], _shuffle(dataset["B"], seed), estimator, bins, k)


def compute_delta(M1: float, M2: float, M3: float | None = None) -> dict:
    """Delta = M1 - M2 (bits). Returns the contrast plus the components and, if
    M3 is given, the across-vs-null residual (M2 - M3, which should be ~0)."""
    out = {"delta_bits": float(M1 - M2), "M1_bits": float(M1), "M2_bits": float(M2)}
    if M3 is not None:
        out["M3_bits"] = float(M3)
        out["M2_minus_M3_bits"] = float(M2 - M3)
    return out


def compute_all(dataset: dict, estimator: str = "hist", bins: int = 2, k: int = 5,
                shuffle_seed: int = 0) -> dict:
    """Convenience: compute M1, M2, M3, and Delta from a dataset in one call.
    estimator="ksg" (with k) for the observable sweep; default "hist" preserves
    the original histogram behaviour for existing callers."""
    M1 = compute_M1(dataset, estimator=estimator, bins=bins, k=k)
    M2 = compute_M2(dataset, estimator=estimator, bins=bins, k=k)
    M3 = compute_M3(dataset, estimator=estimator, bins=bins, k=k, seed=shuffle_seed)
    return compute_delta(M1, M2, M3)
