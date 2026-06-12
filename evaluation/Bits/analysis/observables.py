"""Observables - different ways to read out a stratum's final state.

The Δ measurement contrasts within-stratum vs across-boundary mutual information.
That contrast is computed on *some* readout of each region's state. If Δ depends
on which readout we choose, Δ is an artifact of the observable, not a property of
the substrate. This module supplies several genuinely different observables so
the observable-sweep can test exactly that.

Each function takes a StateVector and a list of node ids, and returns a feature
(scalar -> shape (), or vector -> shape (d,)) summarizing those nodes' final
state. The Δ machinery stacks per-run features into an ensemble array.
"""
from __future__ import annotations

import numpy as np


def get_summed_rho(sv, nodes) -> float:
    """(A) Baseline scalar: total commitment density over the nodes."""
    return float(sum(sv[n].rho for n in nodes))


def get_half_vectors(sv, nodes) -> np.ndarray:
    """(B) Per-node rho vector over the nodes (full-resolution, vector-valued).
    Shape (len(nodes),). KSG handles the multi-dimensional MI directly."""
    return np.array([sv[n].rho for n in nodes], dtype=float)


def get_subregion_rho(sv, nodes, window: int = 4) -> float:
    """(C) Scalar: summed rho over only a contiguous window of the nodes
    (first `window` nodes). A coarse, *local* readout - deliberately discards
    most of the region, unlike the global sum (A)."""
    w = nodes[:window] if len(nodes) >= window else nodes
    return float(sum(sv[n].rho for n in w))


def get_gradient_rho(sv, nodes) -> np.ndarray:
    """(D) Vector: discrete gradient of rho along the (ordered) nodes,
    i.e. successive differences rho[i+1]-rho[i]. Shape (len(nodes)-1,).
    A derivative readout - sensitive to structure the level (A) is blind to."""
    vals = [sv[n].rho for n in nodes]
    return np.diff(np.asarray(vals, dtype=float))


# Registry: name -> (function, kind). "scalar" features stack to shape (N,);
# "vector" features stack to shape (N, d).
OBSERVABLES = {
    "summed_rho":   (get_summed_rho,   "scalar"),
    "half_vectors": (get_half_vectors, "vector"),
    "subregion_rho": (get_subregion_rho, "scalar"),
    "gradient_rho": (get_gradient_rho, "vector"),
}
