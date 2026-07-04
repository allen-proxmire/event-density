"""Is ED's committed order held by geometry, or by the node labels (P11's sequential index)?

The 3D-via-linking bridge rests on one premise: ED holds its committed order by a topological
structure (a spatial link) rather than by a plain sequential/causal index that needs no geometry.
Linking is a 3D phenomenon and the certified simulator is 2D, so the FULL premise is not testable
on certified dynamics (stated honestly). But its NECESSARY PRECONDITION is: the committed order
must be a function of the substrate's geometry/physics at all, not merely of the arbitrary node
labels. If even that fails -- if relabeling the nodes changes the order -- then the order is held
by the label (the sequential index), the cheap geometry-free mechanism, and no topological
structure is doing the holding. This probe tests exactly that precondition on the CERTIFIED sim.

Method: build ONE physical substrate (a 2D grid of chain-loci with fixed positions, bandwidths,
and initial rho/orientation, several seeds -> genuine multi-front interaction). Run the certified
Sigma-rule under the identity node-labeling and under random relabelings that keep every physical
node's state and the graph topology fixed, changing only which integer id each physical node
carries. The Sigma functional reads rho + graph-local structure only (never the id); the id enters
ONLY via the canonical processing order (stratum_id, node_id) and the exact-Sigma-tie tiebreak.
Record, per labeling, the order in which physical nodes first commit; compare via Kendall tau.

Reads:
  tau ~ 1.0  -> order is INVARIANT under relabeling = held by geometry/physics (Sigma-rule).
               The linking premise's precondition is MET (necessary, not sufficient).
  tau ~ 0.5  -> order scrambles with the labels = held by the sequential index, not geometry.
               The linking premise fails its precondition; order is the cheap label mechanism.
  in between -> partially label-dependent; the fraction tells you how load-bearing the labels are.

Controls: identity vs identity must give tau = 1.0 exactly (determinism). No new physics; the
certified Sigma-substrate is used as-is, only node ids are permuted.
"""
import numpy as np
from scipy.stats import kendalltau
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "Bits"))

from simulator import (ParticipationGraph, NodeState, StateVector, SigmaCoeffs,  # noqa: E402
                       assign_stratum_ids, step)

COEFFS = SigmaCoeffs(kc=1.0, ks=1.0, kg=1.0, rho_star=0.5, extinction_threshold=-2.0)


class SeqRec:
    """Minimal recorder: log the (source,target) of each commit in order."""
    def __init__(self):
        self.seq = []
    def log_commit(self, t, u, v):
        self.seq.append((u, v))
    def snapshot(self, t, state):
        pass


def make_physical(side, seed):
    P = side * side
    rng = np.random.default_rng(seed)
    rho0 = rng.uniform(0.0, 0.5, size=P)
    ori0 = rng.normal(size=(P, 2))
    edges = []
    for r in range(side):
        for c in range(side):
            p = r * side + c
            if c + 1 < side:
                edges.append((p, r * side + c + 1))
            if r + 1 < side:
                edges.append((p, (r + 1) * side + c))
    seeds = [0, side - 1, P - side, P - 1, P // 2]  # four corners + centre -> interacting fronts
    return P, rho0, ori0, edges, seeds


def run_under_labeling(P, rho0, ori0, edges, seeds, perm, max_steps=600):
    """perm[p] = integer id assigned to physical node p. Returns the order in which physical
    nodes first receive a commit (list of physical indices)."""
    inv = {perm[p]: p for p in range(P)}
    g = ParticipationGraph()
    for (p, q) in edges:
        g.add_edge(perm[p], perm[q], bandwidth=0.5)
    sv = StateVector()
    for p in range(P):
        sv[perm[p]] = NodeState(rho=float(rho0[p]), orientation=ori0[p].copy())
    for s in seeds:
        sv[perm[s]].active = True
    strata = assign_stratum_ids(sv, g)
    rec = SeqRec()
    for t in range(1, max_steps + 1):
        if step(sv, g, COEFFS, strata=strata, recorder=rec, t=t) == 0:
            break
    seen, order = set(), []
    for (u, v) in rec.seq:
        p = inv[v]
        if p not in seen:
            seen.add(p)
            order.append(p)
    return order


def order_tau(order_a, order_b):
    """Kendall tau between two commit-orders over the physical nodes committed in BOTH."""
    ra = {p: i for i, p in enumerate(order_a)}
    rb = {p: i for i, p in enumerate(order_b)}
    common = [p for p in order_a if p in rb]
    if len(common) < 3:
        return float("nan"), len(common)
    a = [ra[p] for p in common]
    b = [rb[p] for p in common]
    tau, _ = kendalltau(a, b)
    return tau, len(common)


def main():
    side = 9
    P, rho0, ori0, edges, seeds = make_physical(side, seed=1)
    ident = list(range(P))

    print("=" * 84)
    print("ORDER HELD BY GEOMETRY, OR BY LABELS? — relabel nodes on the CERTIFIED sim, compare order")
    print(f"  physical substrate: {side}x{side} grid, {len(seeds)} interacting seeds, certified Sigma-rule")
    print("=" * 84)

    base = run_under_labeling(P, rho0, ori0, edges, seeds, ident)
    print(f"\n  baseline commit-order length: {len(base)} physical nodes")

    # determinism control
    base2 = run_under_labeling(P, rho0, ori0, edges, seeds, ident)
    tctrl, nctrl = order_tau(base, base2)
    print(f"  CONTROL identity vs identity:  tau = {tctrl:.4f}  (must be 1.0000 — determinism)")

    # relabelings
    print("\n  identity vs random relabelings (same physical substrate, permuted ids):")
    taus = []
    for k in range(8):
        rng = np.random.default_rng(100 + k)
        perm = list(rng.permutation(P))
        o = run_under_labeling(P, rho0, ori0, edges, seeds, perm)
        tau, n = order_tau(base, o)
        taus.append(tau)
        print(f"    relabel #{k}:  tau = {tau:+.4f}   (common nodes {n})")

    taus = np.array(taus)
    print("\n  " + "-" * 60)
    print(f"  mean tau over relabelings = {np.nanmean(taus):.4f} +- {np.nanstd(taus):.4f}")
    print("\n  READ:")
    print("   tau ~ 1.00 -> order INVARIANT under relabeling = geometry/physics-held")
    print("                 (linking-premise precondition MET; necessary, not sufficient).")
    print("   tau ~ 0.50 -> order scrambles with labels = held by the sequential index,")
    print("                 not geometry (linking premise fails its precondition).")
    print("   Honest scope: 2D certified sim; the FULL 3D-linking claim is not testable here,")
    print("   only this necessary precondition (is the order geometry-held at all).")
    print("=" * 84)


if __name__ == "__main__":
    main()
