"""Milestone 1 - Gate 4 (tie-break uniqueness) + orientation-blindness +
irreversibility chokepoint.

Runs with only graph.py, state.py, sigma.py, update.py. No update loop, no
strata, no boundaries, no recorder.

Topology: one center node (0) with three admissible leaves (1, 2, 3). Leaf rho
is set equal so Sigma is identical across leaves -> a forced Sigma-tie. The
tie-break then decides:
  Case A (distinct bandwidths): winner by bandwidth.
  Case B (equal bandwidths):    winner by node id (the B1-distinctness key).
"""
import os
import sys

import numpy as np

# Make Bits/ importable so `simulator` resolves regardless of CWD.
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from simulator import (  # noqa: E402
    ParticipationGraph,
    NodeState,
    StateVector,
    compute_sigma,
    compute_candidates,
    SigmaCoeffs,
    apply_tiebreak,
)

CENTER = 0
LEAVES = [1, 2, 3]


def build(bandwidths):
    g = ParticipationGraph()
    g.add_node(CENTER)
    for v, bw in zip(LEAVES, bandwidths):
        g.add_edge(CENTER, v, bandwidth=bw)
    return g


def forced_tie_state(rho_leaf=0.5, rho_center=0.0):
    sv = StateVector()
    sv[CENTER] = NodeState(rho=rho_center, orientation=np.array([0.0, 0.0]))
    for v in LEAVES:
        # identical rho on every leaf -> identical Sigma -> forced tie
        sv[v] = NodeState(rho=rho_leaf, orientation=np.array([0.0, 0.0]))
    return sv


def sigmas(sv, g, coeffs):
    return {v: compute_sigma(CENTER, v, sv, g, coeffs) for v in LEAVES}


def main():
    coeffs = SigmaCoeffs(kc=1.0, ks=1.0, kg=1.0, rho_star=0.5)

    print("=" * 64)
    print("MILESTONE 1 - Gate 4 (tie-break) + orientation-blindness + B7")
    print("=" * 64)

    # ---- Case A: distinct bandwidths -> winner by bandwidth ----
    gA = build(bandwidths=[0.3, 0.5, 0.4])
    svA = forced_tie_state()
    sigA = sigmas(svA, gA, coeffs)
    candsA = compute_candidates(CENTER, svA, gA)
    tiedA = len({round(s, 12) for s in sigA.values()}) == 1
    winnerA = apply_tiebreak(CENTER, candsA, gA)
    print("\nCase A - distinct bandwidths")
    print(f"  Sigma per candidate : {sigA}")
    print(f"  Sigma tied          : {tiedA}")
    print("  bandwidths          : " +
          ", ".join(f"{v}:{gA.bw(CENTER, v)}" for v in LEAVES))
    print(f"  winner              : {winnerA}   (expected 2, bw=0.5)")

    # ---- Case B: equal bandwidths -> winner by node id ----
    gB = build(bandwidths=[0.5, 0.5, 0.5])
    svB = forced_tie_state()
    sigB = sigmas(svB, gB, coeffs)
    candsB = compute_candidates(CENTER, svB, gB)
    tiedB = len({round(s, 12) for s in sigB.values()}) == 1
    winnerB = apply_tiebreak(CENTER, candsB, gB)
    print("\nCase B - equal bandwidths (sigma=node_id final key)")
    print(f"  Sigma per candidate : {sigB}")
    print(f"  Sigma tied          : {tiedB}")
    print("  bandwidths          : all 0.5")
    print(f"  winner              : {winnerB}   (expected 3, max node id)")

    # ---- determinism: re-run -> identical ----
    winnerA2 = apply_tiebreak(CENTER, compute_candidates(CENTER, svA, gA), gA)
    winnerB2 = apply_tiebreak(CENTER, compute_candidates(CENTER, svB, gB), gB)
    det = (winnerA2 == winnerA) and (winnerB2 == winnerB)
    print("\nDeterminism (re-run)")
    print(f"  Case A winner again : {winnerA2}  (identical: {winnerA2 == winnerA})")
    print(f"  Case B winner again : {winnerB2}  (identical: {winnerB2 == winnerB})")

    # ---- orientation-blindness ----
    before = sigmas(svA, gA, coeffs)
    rng = np.random.default_rng(0)
    for v in LEAVES:
        svA[v].orientation[:] = rng.normal(size=2)
    svA[CENTER].orientation[:] = np.array([7.0, -3.0])
    after = sigmas(svA, gA, coeffs)
    blind = all(abs(before[v] - after[v]) < 1e-15 for v in LEAVES)
    print("\nOrientation-blindness")
    print(f"  Sigma before flip   : {before}")
    print(f"  Sigma after  flip   : {after}")
    print(f"  unchanged           : {blind}")

    # ---- irreversibility chokepoint ----
    n = NodeState(rho=1.0)
    n.commit(0.5)
    rose = (n.rho == 1.5)
    rejected = False
    try:
        n.commit(-0.1)
    except ValueError:
        rejected = True
    print("\nIrreversibility chokepoint (commit)")
    print(f"  commit(+0.5)        : rho 1.0 -> {n.rho}  (increment ok: {rose})")
    print(f"  commit(-0.1)        : rejected = {rejected}")

    # ---- verdict ----
    passed = (
        tiedA and tiedB
        and winnerA == 2 and winnerB == 3
        and det and blind and rose and rejected
    )
    print("\n" + "=" * 64)
    print(f"MILESTONE 1: {'PASS' if passed else 'FAIL'}")
    print("=" * 64)
    return passed


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
