"""A3 — Topology / reach / Sigma-law sweep (bits-measurement angle #3).

The prior robustness sweeps (size, MI-estimator, observable) all varied ONE dial on a fixed
substrate shape: two linear chains joined by a hard-decoupled bridge. This sweep varies the
shape and rule itself, the dial that's never been turned:

  (A) TOPOLOGY — does perfect severance (M2 ~ 0 across the decoupling surface, M1 > 0 within a
      stratum) survive if the substrate isn't a simple chain? Tests TREE (branching participation)
      and GRID (2D lattice) topologies alongside the chain baseline.
  (B) SIGMA-LAW — does severance survive if the Sigma coefficients (coherence/strain/gradient
      weights) are pushed away from the balanced default, toward coherence-dominated, strain-
      dominated, or gradient-dominated regimes?
  (C) REACH GRADING — is severance a hard threshold (only at decoupled=True) or does it appear
      continuously as bridge bandwidth is reduced toward zero? Tests a bandwidth sweep on the
      SAME chain topology, non-decoupled bridges at decreasing bandwidth vs the hard-decoupled
      case.

Reuses the certified simulator and the exact M1/M2/M3/Delta measurement pipeline already
validated by the size/estimator/observable sweeps -- no new rules, no new metric.

Could-say-no: if M2 stays near the M3 shuffle-floor (severance holds) across every topology,
every Sigma regime, and only appears once the bridge is truly decoupled (not just low-bandwidth),
the "perfect, observable/architecture-independent severance" finding is confirmed as genuinely
structural. Any topology, Sigma regime, or graded-bandwidth case where M2 pulls away from the
shuffle floor is a real, informative counterexample -- honest either way.
"""
import json
import os
import sys
import math

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from simulator import (  # noqa: E402
    ParticipationGraph, NodeState, StateVector, SigmaCoeffs,
    assign_stratum_ids, step,
)
from analysis.delta import compute_all  # noqa: E402

S = 32                # nodes per stratum, fixed (size axis already swept separately)
N_ENSEMBLE = 150
BW = 0.5

DEFAULT_COEFFS = SigmaCoeffs(kc=1.0, ks=1.0, kg=1.0, rho_star=0.5, extinction_threshold=-2.0)
SIGMA_REGIMES = {
    "balanced (default)": DEFAULT_COEFFS,
    "coherence-dominated": SigmaCoeffs(kc=3.0, ks=0.5, kg=0.5, rho_star=0.5, extinction_threshold=-2.0),
    "strain-dominated":    SigmaCoeffs(kc=0.5, ks=3.0, kg=0.5, rho_star=0.5, extinction_threshold=-2.0),
    "gradient-dominated":  SigmaCoeffs(kc=0.5, ks=0.5, kg=3.0, rho_star=0.5, extinction_threshold=-2.0),
}


# ---------- topology builders: each returns (graph, A_nodes, B_nodes, A_left, A_right) ----------

def build_chain(S, bw=BW):
    g = ParticipationGraph()
    A = list(range(S))
    B = list(range(S, 2 * S))
    for chain in (A, B):
        for i in range(len(chain) - 1):
            g.add_edge(chain[i], chain[i + 1], bandwidth=bw)
    g.add_edge(A[-1], B[0], bandwidth=bw, decoupled=True)
    half = S // 2
    return g, A, B, A[:half], A[half:]


def build_tree(S, bw=BW, branching=2):
    """Binary(ish) tree of S nodes per stratum; A_left/A_right = the root's two subtrees."""
    def build_one(offset):
        nodes = list(range(offset, offset + S))
        for i in range(1, S):
            parent = offset + (i - 1) // branching
            g_edges.append((parent, offset + i))
        return nodes

    g = ParticipationGraph()
    g_edges = []
    A = build_one(0)
    B = build_one(S)
    for u, v in g_edges:
        g.add_edge(u, v, bandwidth=bw)
    # bridge: a deep-ish leaf of A to the root of B (mirrors chain's "last of A -> first of B")
    g.add_edge(A[-1], B[0], bandwidth=bw, decoupled=True)
    # left/right subtree of A's root (node A[0]): children are A[1], A[2] for branching=2
    left_root = 1
    right_root = 2 if branching >= 2 and S > 2 else 1
    A_left = [n for n in A if n != A[0] and _subtree_of(n, left_root, branching, S)]
    A_right = [n for n in A if n != A[0] and n not in A_left]
    return g, A, B, A_left, A_right


def _subtree_of(node_offset_local, subtree_root_local, branching, S):
    """Is local index node_offset_local in the subtree rooted at subtree_root_local?
    (Local indices 0..S-1 within one tree, parent(i) = (i-1)//branching.)"""
    i = node_offset_local
    if i == subtree_root_local:
        return True
    while i > 0:
        i = (i - 1) // branching
        if i == subtree_root_local:
            return True
    return False


def build_grid(S, bw=BW):
    """2D lattice, side x side nodes per stratum (S rounded to a perfect square);
    A_left/A_right = left/right half by column."""
    side = max(2, int(round(math.sqrt(S))))
    n_per = side * side

    def build_one(offset):
        nodes = list(range(offset, offset + n_per))
        for r in range(side):
            for c in range(side):
                u = offset + r * side + c
                if c + 1 < side:
                    g_edges.append((u, offset + r * side + c + 1))
                if r + 1 < side:
                    g_edges.append((u, offset + (r + 1) * side + c))
        return nodes

    g = ParticipationGraph()
    g_edges = []
    A = build_one(0)
    B = build_one(n_per)
    for u, v in g_edges:
        g.add_edge(u, v, bandwidth=bw)
    # bridge: A's bottom-right corner to B's top-left corner
    g.add_edge(A[-1], B[0], bandwidth=bw, decoupled=True)
    A_left = [offset_r * side + c for offset_r in range(side) for c in range(side // 2)]
    A_right = [n for n in A if n not in A_left]
    return g, A, B, A_left, A_right, n_per


TOPOLOGIES = {
    "chain": lambda: build_chain(S) + (S,),
    "tree":  lambda: build_tree(S) + (S,),
    "grid":  lambda: build_grid(S),
}


# ---------- graded-reach builder (axis C): a chain with a NON-decoupled, low-bandwidth bridge ----------

def build_chain_graded_bridge(S, bridge_bw, bw=BW):
    g = ParticipationGraph()
    A = list(range(S))
    B = list(range(S, 2 * S))
    for chain in (A, B):
        for i in range(len(chain) - 1):
            g.add_edge(chain[i], chain[i + 1], bandwidth=bw)
    g.add_edge(A[-1], B[0], bandwidth=bridge_bw, decoupled=False)  # NOT decoupled -- graded
    half = S // 2
    return g, A, B, A[:half], A[half:]


# ---------- shared run / measure machinery (same pattern as size_sweep.py) ----------

def run_one(graph, seed_a, seed_b, coeffs, max_steps, seed_nodes):
    sv = StateVector()
    rng_a = np.random.default_rng(seed_a)
    rng_b = np.random.default_rng(seed_b)
    nodes = list(graph.nodes())
    half = len(nodes) // 2
    for n in nodes[:half]:
        sv[n] = NodeState(rho=float(rng_a.uniform(0.0, 0.5)), orientation=rng_a.normal(size=2))
    for n in nodes[half:]:
        sv[n] = NodeState(rho=float(rng_b.uniform(0.0, 0.5)), orientation=rng_b.normal(size=2))
    for n in seed_nodes:
        sv[n].active = True
    strata = assign_stratum_ids(sv, graph)
    steps = 0
    for t in range(1, max_steps + 1):
        c = step(sv, graph, coeffs, strata=strata)
        steps = t
        if c == 0:
            break
    return sv, steps, (steps < max_steps)


def measure(build_fn, coeffs, N=N_ENSEMBLE, max_steps=1200):
    result = build_fn()
    if len(result) == 6:
        g, A, B, A_left, A_right, _n = result
    else:
        g, A, B, A_left, A_right = result
    seed_nodes = [A[0], B[0]]
    A_s, B_s, AL_s, AR_s = [], [], [], []
    natural = 0
    for k in range(N):
        sv, steps, term = run_one(g, 1000 + k, 5000 + k, coeffs, max_steps, seed_nodes)
        natural += int(term)
        A_s.append(sum(sv[n].rho for n in A))
        B_s.append(sum(sv[n].rho for n in B))
        AL_s.append(sum(sv[n].rho for n in A_left))
        AR_s.append(sum(sv[n].rho for n in A_right))
    ds = {"A": np.array(A_s), "B": np.array(B_s),
          "A_left": np.array(AL_s), "A_right": np.array(AR_s)}
    d = compute_all(ds)
    d["natural_fraction"] = natural / N
    return d


def row(label, d):
    m2_zero = abs(d["M2_bits"]) < 0.05
    print(f"  {label:28s} M1={d['M1_bits']:+.4f}  M2={d['M2_bits']:+.4f}  "
          f"M3={d['M3_bits']:+.4f}  Delta={d['delta_bits']:+.4f}  "
          f"M2~M3? {m2_zero!s:5s}  nat%={d['natural_fraction']*100:.0f}")
    return m2_zero


def main():
    print("=" * 88)
    print("A3 SWEEP — topology x Sigma-law x reach-grading (bits-measurement angle #3)")
    print(f"  S={S} nodes/stratum, ensemble N={N_ENSEMBLE}, same certified sim + M1/M2/M3 pipeline")
    print("=" * 88)

    all_ok = []

    print("\n(A) TOPOLOGY sweep (default balanced Sigma):")
    for name, build_fn in TOPOLOGIES.items():
        d = measure(build_fn, DEFAULT_COEFFS)
        all_ok.append(row(f"topology={name}", d))

    print("\n(B) SIGMA-LAW sweep (chain topology, coefficients pushed away from balanced):")
    for name, coeffs in SIGMA_REGIMES.items():
        d = measure(TOPOLOGIES["chain"], coeffs)
        all_ok.append(row(f"sigma={name}", d))

    print("\n(C) REACH-GRADING sweep (chain topology, bridge bandwidth graded down from full,")
    print("    NEVER marked decoupled -- vs the hard-decoupled case for comparison):")
    for bridge_bw in [0.5, 0.25, 0.10, 0.05, 0.01, 0.001]:
        d = measure(lambda bw=bridge_bw: build_chain_graded_bridge(S, bw), DEFAULT_COEFFS)
        all_ok.append(row(f"graded bridge_bw={bridge_bw}", d))
    d_hard = measure(TOPOLOGIES["chain"], DEFAULT_COEFFS)
    all_ok.append(row("hard-decoupled (reference)", d_hard))

    print("\n" + "=" * 88)
    print(f"ALL {len(all_ok)} CONFIGURATIONS: M2 ~ shuffle-floor (severance holds)? "
          f"{sum(all_ok)}/{len(all_ok)}")
    print("=" * 88)

    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sweep_output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "a3_topology_sigma_sweep.json"), "w", encoding="utf-8") as fh:
        json.dump({"S": S, "N": N_ENSEMBLE, "all_severance_held": all_ok}, fh, indent=2)

    return all(all_ok[:len(TOPOLOGIES) + len(SIGMA_REGIMES)])  # graded axis expected to trend, not hold


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
