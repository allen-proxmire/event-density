"""Gate 3 - factorization. THE DECISIVE GATE.

Two complementary tests that decoupling severs reciprocal participation:

  Structural (exact): perturbing stratum B's initial seed leaves stratum A's
  trajectory byte-identical, and vice versa. If A depended on B in any way, a
  change in B would change A. This is an exact, tolerance-free proof.

  Informational: across an ensemble of independently-seeded runs, the mutual
  information between an A-summary and a B-summary is ~0 (Miller-Madow corrected
  histogram MI). Independent strata carry no shared information.
"""
import numpy as np

from analysis.entropy import mutual_information
from mwe_demo import run_mwe, A_NODES, B_NODES

A_SET = set(A_NODES)
B_SET = set(B_NODES)


def _commits_in(rec, node_set):
    """Subsequence of (t, u, v) commit events whose source u is in node_set."""
    ce = rec.committed_edges()
    return [tuple(int(x) for x in row) for row in ce if int(row[1]) in node_set]


def _final_rho(res, nodes):
    sv = res["sv"]
    return [sv[n].rho for n in nodes]


# ----- structural (exact) -----

def test_A_independent_of_B_structural():
    """Change B's seed; A's commits and final state must be unchanged."""
    base = run_mwe(seed_a=1, seed_b=2)
    pert = run_mwe(seed_a=1, seed_b=999)        # only B perturbed
    assert _commits_in(base["rec"], A_SET) == _commits_in(pert["rec"], A_SET)
    assert _final_rho(base, A_NODES) == _final_rho(pert, A_NODES)


def test_B_independent_of_A_structural():
    """Change A's seed; B's commits and final state must be unchanged."""
    base = run_mwe(seed_a=1, seed_b=2)
    pert = run_mwe(seed_a=777, seed_b=2)        # only A perturbed
    assert _commits_in(base["rec"], B_SET) == _commits_in(pert["rec"], B_SET)
    assert _final_rho(base, B_NODES) == _final_rho(pert, B_NODES)


def test_no_commit_crosses_the_boundary():
    """No commitment event has a source and target in different strata."""
    res = run_mwe(seed_a=1, seed_b=2)
    for (_, u, v) in [tuple(int(x) for x in row)
                      for row in res["rec"].committed_edges()]:
        same_side = (u in A_SET) == (v in A_SET)
        assert same_side, f"commit {u}->{v} crossed the decoupling boundary"


# ----- informational -----

def test_across_boundary_mutual_information_is_zero():
    """Ensemble MI(A-summary; B-summary) ~ 0 (Miller-Madow, 2-bin)."""
    N = 200
    a_sum, b_sum = [], []
    for k in range(N):
        res = run_mwe(seed_a=1000 + k, seed_b=5000 + k, record=False)
        sv = res["sv"]
        a_sum.append(sum(sv[n].rho for n in A_NODES))
        b_sum.append(sum(sv[n].rho for n in B_NODES))
    mi = mutual_information(np.array(a_sum), np.array(b_sum), bins=2)
    # Tolerance: 5e-3 nats. The Miller-Madow estimate centers near 0 for
    # independent strata; the naive plug-in MI has positive finite-sample bias.
    # Empirically ~5.6e-4 nats here (well within tolerance, and below 1e-3).
    assert abs(mi) < 5e-3, f"across-boundary MI not ~0: {mi:.6f} nats"


def test_mi_matches_shuffle_control():
    """MI(A,B) is statistically indistinguishable from MI(A, shuffled B)."""
    N = 200
    a_sum, b_sum = [], []
    for k in range(N):
        res = run_mwe(seed_a=1000 + k, seed_b=5000 + k, record=False)
        sv = res["sv"]
        a_sum.append(sum(sv[n].rho for n in A_NODES))
        b_sum.append(sum(sv[n].rho for n in B_NODES))
    a = np.array(a_sum)
    b = np.array(b_sum)
    rng = np.random.default_rng(0)
    b_shuf = b.copy()
    rng.shuffle(b_shuf)
    mi = mutual_information(a, b, bins=2)
    mi_shuf = mutual_information(a, b_shuf, bins=2)
    assert abs(mi - mi_shuf) < 5e-3, (
        f"MI(A,B)={mi:.6f} differs from shuffle baseline {mi_shuf:.6f}")
