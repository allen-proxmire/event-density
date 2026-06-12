"""Graph-general information-theoretic estimators for the Δ program.

NOT spectral: these operate on arbitrary samples (region-state vectors,
summaries), not on Cartesian-grid Fourier spectra. ed-lab's spectral entropy is
grid-specific; only the Shannon kernel idiom is shared. Mutual information uses
a binned (histogram) estimator with a Miller-Madow bias correction, because the
naive plug-in MI is positively biased at finite sample size — truly independent
variables yield a small positive MI without correction.
"""
from __future__ import annotations

import numpy as np


def _entropy_counts(counts: np.ndarray) -> float:
    """Plug-in Shannon entropy (nats) from a count array."""
    n = counts.sum()
    if n == 0:
        return 0.0
    p = counts[counts > 0] / n
    return float(-np.sum(p * np.log(p)))


def _miller_madow(counts: np.ndarray) -> float:
    """Miller-Madow corrected entropy: H_plugin + (K-1)/(2N), K = nonempty bins."""
    n = counts.sum()
    if n == 0:
        return 0.0
    k = int(np.count_nonzero(counts))
    return _entropy_counts(counts) + (k - 1) / (2.0 * n)


def mutual_information(x: np.ndarray, y: np.ndarray, bins: int = 2,
                       correct: bool = True) -> float:
    """Estimate MI(x; y) in nats from paired samples via a 2D histogram.

    x, y          : 1-D arrays of equal length (the ensemble samples).
    bins          : number of bins per axis (quantile-edged for balance).
    correct       : apply Miller-Madow bias correction (recommended).

    MI = H(x) + H(y) - H(x, y). With correction each marginal/joint entropy is
    Miller-Madow corrected, which centers the estimate near 0 for independent
    data (the naive estimator is positively biased).
    """
    x = np.asarray(x, dtype=float).ravel()
    y = np.asarray(y, dtype=float).ravel()
    assert x.shape == y.shape and x.size > 0

    xe = _quantile_edges(x, bins)
    ye = _quantile_edges(y, bins)
    xi = np.clip(np.digitize(x, xe[1:-1]), 0, bins - 1)
    yi = np.clip(np.digitize(y, ye[1:-1]), 0, bins - 1)

    joint = np.zeros((bins, bins), dtype=float)
    for a, b in zip(xi, yi):
        joint[a, b] += 1.0
    cx = joint.sum(axis=1)
    cy = joint.sum(axis=0)

    if correct:
        hx = _miller_madow(cx)
        hy = _miller_madow(cy)
        hxy = _miller_madow(joint.ravel())
    else:
        hx = _entropy_counts(cx)
        hy = _entropy_counts(cy)
        hxy = _entropy_counts(joint.ravel())
    return hx + hy - hxy


def mutual_information_ksg(x: np.ndarray, y: np.ndarray, k: int = 3) -> float:
    """Kraskov-Stoegbauer-Grassberger (KSG, estimator 1) mutual information, nats.

    Binning-free k-nearest-neighbour estimator (Kraskov et al. 2004), suited to
    continuous and strongly-dependent variables where histogram MI saturates or
    is bin-dependent. For each point, find the k-th neighbour distance in the
    joint space (max-norm), then count marginal neighbours within that radius:

        MI = psi(k) + psi(N) - < psi(n_x + 1) + psi(n_y + 1) >

    A tiny deterministic jitter breaks ties (continuous-variable assumption).
    Returns max(MI, 0): MI is non-negative; KSG can dip slightly below 0 on
    independent data, which we clip.
    """
    try:
        from scipy.special import digamma
    except Exception:  # pragma: no cover - fallback if scipy absent
        digamma = _digamma_fallback

    x = np.asarray(x, dtype=float).reshape(len(x), -1)
    y = np.asarray(y, dtype=float).reshape(len(y), -1)
    n = len(x)
    assert len(y) == n and n > k

    # Deterministic jitter (scaled to data) to break exact ties.
    rng = np.random.default_rng(12345)
    x = x + rng.normal(0.0, 1e-10, x.shape) * (np.std(x) + 1e-12)
    y = y + rng.normal(0.0, 1e-10, y.shape) * (np.std(y) + 1e-12)
    z = np.hstack([x, y])

    # Pairwise max-norm (Chebyshev) distances.
    dz = np.max(np.abs(z[:, None, :] - z[None, :, :]), axis=2)
    dx = np.max(np.abs(x[:, None, :] - x[None, :, :]), axis=2)
    dy = np.max(np.abs(y[:, None, :] - y[None, :, :]), axis=2)

    nx = np.empty(n)
    ny = np.empty(n)
    for i in range(n):
        d = dz[i].copy()
        d[i] = np.inf
        eps = np.partition(d, k - 1)[k - 1]      # distance to k-th neighbour
        nx[i] = np.sum(dx[i] < eps) - 1          # exclude self
        ny[i] = np.sum(dy[i] < eps) - 1

    mi = (digamma(k) + digamma(n)
          - np.mean(digamma(nx + 1) + digamma(ny + 1)))
    return max(float(mi), 0.0)


def _digamma_fallback(z):
    """Digamma approximation (used only if scipy is unavailable)."""
    z = np.asarray(z, dtype=float)
    result = np.zeros_like(z)
    # Shift up to z >= 6 using recurrence psi(z) = psi(z+1) - 1/z.
    zz = z.copy()
    while np.any(zz < 6):
        m = zz < 6
        result[m] -= 1.0 / zz[m]
        zz[m] += 1.0
    # Asymptotic series for large z.
    f = 1.0 / zz
    result += (np.log(zz) - 0.5 * f
               - f * f * (1.0 / 12 - f * f * (1.0 / 120 - f * f / 252)))
    return result


def _quantile_edges(v: np.ndarray, bins: int) -> np.ndarray:
    """Bin edges at quantiles, so each bin holds ~equal mass (robust to scale)."""
    qs = np.linspace(0.0, 1.0, bins + 1)
    edges = np.quantile(v, qs)
    # Ensure strictly increasing edges (degenerate if v is constant).
    eps = 1e-12
    for i in range(1, len(edges)):
        if edges[i] <= edges[i - 1]:
            edges[i] = edges[i - 1] + eps
    return edges
