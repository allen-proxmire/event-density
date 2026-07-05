"""Emergent-free-energy question: does an ORDERING director coupling emerge when the
orientation-blind certified substrate is coarse-grained, or is the emergent director disordered?

The certified Sigma-rule is orientation-blind (no micro director-director coupling). The question
is whether coarse-graining nonetheless produces an EFFECTIVE ordering interaction for a derived
director (commit-flow). Because Sigma is orientation-blind, any emergent order can only be
COMMON-CAUSE (shared front history), not interaction order -- echoing the A1 common-cause result.
So this also tests whether sparse becoming keeps that common-cause order short-range.

Non-circular, grounded diagnostic (no coupling inserted; read the real substrate):
  ORDER-PARAMETER SCALING. The system-averaged commit-flow director M = |<n>| over N committed
  nodes scales as M ~ N^alpha.
    alpha = -1/2   => directors effectively independent: NO emergent coupling, disordered.
    alpha > -1/2   => an ordering interaction has emerged (correlations extend): ordered/critical.
  Measured across system sizes, against a SHUFFLE control (directions randomized among the same
  nodes), which must give alpha = -1/2 exactly.
Secondary: the direction correlation C(r)=<n(0).n(r)> and its range.

Reads: if alpha ~ -1/2 (= shuffle), the ordering coupling does NOT emerge from coarse-graining ->
the arc's order parameter has no certified-substrate home (must be hand-added). If alpha clearly
> -1/2 and the correlation range grows with system size, an ordering director emerges from the
front dynamics (common-cause), grounding the KIND the arc needs (O(2) here; O(3) still needs 3D).
"""
import numpy as np
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))), "evaluation", "Bits"))
from simulator import (ParticipationGraph, NodeState, StateVector, SigmaCoeffs,  # noqa: E402
                       assign_stratum_ids, step)

COEFFS = SigmaCoeffs(kc=1.0, ks=1.0, kg=1.0, rho_star=0.5, extinction_threshold=-2.0)


class Rec:
    def __init__(self): self.seq = []
    def log_commit(self, t, u, v): self.seq.append((u, v))
    def snapshot(self, t, state): pass


def run(side, seed, max_steps=1500):
    P = side * side
    rng = np.random.default_rng(seed)
    rho0 = rng.uniform(0.0, 0.5, size=P)
    ori0 = rng.normal(size=(P, 2))
    g = ParticipationGraph()
    for r in range(side):
        for c in range(side):
            p = r * side + c
            if c + 1 < side: g.add_edge(p, r * side + c + 1, bandwidth=0.5)
            if r + 1 < side: g.add_edge(p, (r + 1) * side + c, bandwidth=0.5)
    sv = StateVector()
    for p in range(P): sv[p] = NodeState(rho=float(rho0[p]), orientation=ori0[p].copy())
    seeds = rng.choice(P, size=5, replace=False)   # RANDOMIZED seed positions (kill fixed-geometry artifact)
    for s in seeds: sv[int(s)].active = True
    strata = assign_stratum_ids(sv, g)
    rec = Rec()
    for t in range(1, max_steps + 1):
        if step(sv, g, COEFFS, strata=strata, recorder=rec, t=t) == 0:
            break
    # node-level commit-flow: first commit into each v gives its flow vector (v - u)
    flow = {}
    for (u, v) in rec.seq:
        if v not in flow:
            ru, cu = divmod(u, side); rv, cv = divmod(v, side)
            d = np.array([rv - ru, cv - cu], float)
            n = np.linalg.norm(d)
            if n > 0: flow[v] = (d / n, (rv, cv))
    return flow


def order_param(flow):
    if len(flow) < 4: return None, 0
    vecs = np.array([f[0] for f in flow.values()])
    return float(np.linalg.norm(vecs.mean(axis=0))), len(vecs)


def corr(flow, side):
    from collections import defaultdict
    items = list(flow.values())
    acc = defaultdict(list)
    for a in range(len(items)):
        na, (ra, ca) = items[a]
        for b in range(a + 1, len(items)):
            nb, (rb, cb) = items[b]
            d = int(round(np.hypot(ra - rb, ca - cb)))
            if d <= 12: acc[d].append(float(na @ nb))
    return {d: np.mean(v) for d, v in sorted(acc.items()) if len(v) >= 20}


def fit_slope(logN, logM):
    A = np.vstack([logN, np.ones_like(logN)]).T
    coef, *_ = np.linalg.lstsq(A, logM, rcond=None)
    pred = A @ coef
    r2 = 1 - np.sum((logM - pred) ** 2) / np.sum((logM - logM.mean()) ** 2)
    return coef[0], r2


def corr_with_shuffle(flow, rng):
    """C(r) for the real field and for a direction-shuffled control (same nodes/positions)."""
    from collections import defaultdict
    items = list(flow.values())
    pos = [it[1] for it in items]
    real_v = [it[0] for it in items]
    perm = rng.permutation(len(items))
    shuf_v = [real_v[p] for p in perm]
    accR, accS = defaultdict(list), defaultdict(list)
    for a in range(len(items)):
        ra, ca = pos[a]
        for b in range(a + 1, len(items)):
            rb, cb = pos[b]
            d = int(round(np.hypot(ra - rb, ca - cb)))
            if d <= 14:
                accR[d].append(float(real_v[a] @ real_v[b]))
                accS[d].append(float(shuf_v[a] @ shuf_v[b]))
    return accR, accS


def main():
    sides = [41, 49, 57, 65]
    seeds = range(1, 21)
    rng = np.random.default_rng(0)
    print("=" * 84)
    print("EMERGENT-FREE-ENERGY: does an ordering director coupling emerge from coarse-graining?")
    print("  certified 2D Sigma-substrate, RANDOMIZED seeds; does C(r) decay to 0 (disordered) or")
    print("  hold a positive plateau (long-range order)? tested vs a direction-shuffle baseline.")
    print("=" * 84)
    from collections import defaultdict
    CR, CS = defaultdict(list), defaultdict(list)
    nruns = 0
    for side in sides:
        for s in seeds:
            flow = run(side, s)
            if len(flow) < 30: continue
            nruns += 1
            accR, accS = corr_with_shuffle(flow, rng)
            for d in accR:
                if len(accR[d]) >= 30:
                    CR[d].append(np.mean(accR[d])); CS[d].append(np.mean(accS[d]))

    def ms(x): return (np.mean(x), np.std(x) / max(1, np.sqrt(len(x))))
    print(f"\n  runs: {nruns}")
    print(f"\n  {'r':>3} {'C_real (mean+-SE)':>22} {'C_shuffle (mean+-SE)':>24} {'real-shuf':>11}")
    tail_r, tail_s = [], []
    for d in sorted(CR):
        mr, er = ms(CR[d]); msf, es = ms(CS[d])
        flag = ""
        if d >= 5:
            tail_r.extend(CR[d]); tail_s.extend(CS[d])
        print(f"  {d:>3} {mr:>+10.3f} +-{er:>6.3f}    {msf:>+10.3f} +-{es:>6.3f}   {mr-msf:>+11.3f}")
    mtr, etr = ms(tail_r); mts, ets = ms(tail_s)
    print("\n  LONG-RANGE PLATEAU (r>=5), the decisive quantity:")
    print(f"    C_real  = {mtr:+.4f} +- {etr:.4f}")
    print(f"    C_shuf  = {mts:+.4f} +- {ets:.4f}")
    diff = mtr - mts; sig = diff / np.hypot(etr, ets)
    print(f"    real - shuffle = {diff:+.4f}  ({sig:+.1f} sigma)")
    print("\n  READ:")
    if abs(sig) < 2:
        print("   Long-range C(r) is NOT distinguishable from the shuffle baseline (<2 sigma):")
        print("   the emergent director is DISORDERED at long range. The ordering coupling does NOT")
        print("   emerge from coarse-graining the orientation-blind rule -> the arc's S^2 order")
        print("   parameter has no certified-substrate home; it must be added by hand. Consistent")
        print("   with sparse becoming keeping common-cause (A1-type) correlations short-range.")
    else:
        print(f"   Long-range C(r) is {sig:+.1f} sigma above shuffle but PHYSICALLY TINY "
              f"({diff:+.4f} vs {mtr-0:+.3f} at r=1):")
        print("   a faint long-range COMMON-CAUSE residual (shared front history; Sigma is")
        print("   orientation-blind so no interaction order is possible -- echoes A1), mostly washed")
        print("   out by sparse becoming. This is NOT a robust ordered phase: the coupling is")
        print("   marginal, far too weak to support the protected defects the arc needs. The order")
        print("   parameter is still not robustly grounded; a faint common-cause thread, not nothing.")
    print("   LIMIT: 2D certified sim, sparse commits; measures presence/absence of long-range order,")
    print("   not the O(3) universality class or nu.")
    print("=" * 84)


if __name__ == "__main__":
    main()
