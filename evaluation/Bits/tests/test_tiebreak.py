"""Gate 4 - tie-break uniqueness + orientation-blindness.

Recreates the Milestone 1 forced-tie scenario: a center node with leaves of
equal rho (so Sigma ties), resolved by the lexicographic (bw, node_id) key.
Also asserts Sigma is orientation-blind.
"""
import numpy as np

from simulator import (
    ParticipationGraph, NodeState, StateVector, SigmaCoeffs,
    compute_sigma, compute_candidates, apply_tiebreak,
)

CENTER = 0
LEAVES = [1, 2, 3]
COEFFS = SigmaCoeffs(kc=1.0, ks=1.0, kg=1.0, rho_star=0.5)


def _graph(bandwidths):
    g = ParticipationGraph()
    g.add_node(CENTER)
    for v, bw in zip(LEAVES, bandwidths):
        g.add_edge(CENTER, v, bandwidth=bw)
    return g


def _forced_tie_state():
    sv = StateVector()
    sv[CENTER] = NodeState(rho=0.0, orientation=np.array([0.0, 0.0]))
    for v in LEAVES:
        sv[v] = NodeState(rho=0.5, orientation=np.array([0.0, 0.0]))
    return sv


def _sigmas(sv, g):
    return {v: compute_sigma(CENTER, v, sv, g, COEFFS) for v in LEAVES}


def test_forced_tie_is_genuine():
    g = _graph([0.3, 0.5, 0.4])
    sv = _forced_tie_state()
    sig = _sigmas(sv, g)
    assert len({round(s, 12) for s in sig.values()}) == 1, "Sigma not tied"


def test_distinct_bandwidth_winner():
    g = _graph([0.3, 0.5, 0.4])
    sv = _forced_tie_state()
    winner = apply_tiebreak(CENTER, compute_candidates(CENTER, sv, g), g)
    assert winner == 2, "winner should be the max-bandwidth leaf (node 2)"


def test_equal_bandwidth_winner_is_node_id():
    g = _graph([0.5, 0.5, 0.5])
    sv = _forced_tie_state()
    winner = apply_tiebreak(CENTER, compute_candidates(CENTER, sv, g), g)
    assert winner == 3, "winner should be the max node id (node 3)"


def test_tiebreak_deterministic():
    g = _graph([0.5, 0.5, 0.5])
    sv = _forced_tie_state()
    w1 = apply_tiebreak(CENTER, compute_candidates(CENTER, sv, g), g)
    w2 = apply_tiebreak(CENTER, compute_candidates(CENTER, sv, g), g)
    assert w1 == w2


def test_sigma_orientation_blind():
    g = _graph([0.3, 0.5, 0.4])
    sv = _forced_tie_state()
    before = _sigmas(sv, g)
    rng = np.random.default_rng(0)
    for v in LEAVES:
        sv[v].orientation[:] = rng.normal(size=2)
    sv[CENTER].orientation[:] = np.array([7.0, -3.0])
    after = _sigmas(sv, g)
    for v in LEAVES:
        assert abs(before[v] - after[v]) < 1e-15, "Sigma moved under orientation flip"
