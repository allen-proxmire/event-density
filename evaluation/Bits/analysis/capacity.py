"""Channel-capacity estimation for the ED substrate (A1).

The observable sweep showed single-observable mutual information is observable-
DEPENDENT, so there is no intrinsic scalar Delta. Channel *capacity* is the
supremum of transmitted information over inputs/readouts, so it is observable-
INDEPENDENT by construction. This module estimates a capacity proxy by coding:
encode a K-ary message into a source region's initial condition, evolve, and try
to decode it from a target region. The recovered mutual information I(m; Y) as K
grows distinguishes two regimes:

  - plateau at C*  -> intrinsic capacity ceiling (an ED-native invariant);
  - tracks log2(K) -> near-lossless channel, capacity = input-limited
    (setup-dependent, NOT intrinsic).

Across a decoupling boundary, I(m; Y) ~ 0 for all K -> capacity 0, an
observable-INDEPENDENT statement of severance.

BIAS CORRECTION (load-bearing): a leave-one-out k-NN decoder MI is positively
biased when K >> k (only ~k classes appear among k neighbours, so H(m|y) maxes
near log2(k), inflating I by ~log2(K)-log2(k) even on INDEPENDENT data). We
remove this with a shuffle null: corrected I = I(m;Y) - mean_pi I(pi(m);Y).
On independent data the two cancel -> ~0; real signal survives.
"""
from __future__ import annotations

import numpy as np


def _knn_neighbors(Y: np.ndarray, k: int) -> np.ndarray:
    """Leave-one-out k nearest-neighbour indices for each row of Y (N, k)."""
    Y = np.asarray(Y, dtype=float)
    if Y.ndim == 1:
        Y = Y[:, None]
    Y = (Y - Y.mean(axis=0)) / (Y.std(axis=0) + 1e-9)
    D = ((Y[:, None, :] - Y[None, :, :]) ** 2).sum(axis=2)
    np.fill_diagonal(D, np.inf)
    return np.argpartition(D, k, axis=1)[:, :k]


def _mi_from_neighbors(nbr: np.ndarray, m: np.ndarray, K: int) -> float:
    """Raw decoder MI (bits) from precomputed neighbour indices: I = log2(K) -
    mean_i H(m | neighbours of i)."""
    n = len(m)
    h = np.empty(n)
    for i in range(n):
        counts = np.bincount(m[nbr[i]], minlength=K).astype(float)
        p = counts / counts.sum()
        p = p[p > 0]
        h[i] = -np.sum(p * np.log2(p))
    return float(np.log2(K) - h.mean())


def knn_decoder_mi(Y: np.ndarray, m: np.ndarray, K: int, k: int = 7,
                   n_shuffle: int = 6, seed: int = 0) -> float:
    """Bias-corrected leave-one-out k-NN decoder MI, in bits.

    corrected = I(m;Y) - mean over n_shuffle permutations of I(pi(m);Y).
    Reuses one neighbour computation for the real and shuffled estimates.
    """
    m = np.asarray(m, dtype=int)
    nbr = _knn_neighbors(Y, k)
    raw = _mi_from_neighbors(nbr, m, K)
    rng = np.random.default_rng(seed)
    null = np.mean([_mi_from_neighbors(nbr, rng.permutation(m), K)
                    for _ in range(n_shuffle)])
    return raw - null
