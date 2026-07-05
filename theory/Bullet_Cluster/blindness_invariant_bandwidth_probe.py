"""Test the POSITIVE side of the blindness/common-cause invariant, in the bandwidth sector.

AP's structural invariant:
  - BLIND quantity  -> only common-cause long-range correlation, erased by sparse becoming (faint).
  - NON-BLIND quantity -> can carry genuine INTERACTION long-range correlation, NOT erased.

The Sigma-rule is orientation-BLIND (director sector: confirmed short-range/common-cause only, no
order). But it is NOT blind to the commitment-density rho (Sigma's coherence/strain/gradient all
read rho + graph-local structure). So the invariant PREDICTS the rho / bandwidth sector carries real
long-range interaction correlation that the blind director sector lacks. This is the hopeful sector
for curvature emergence's emergent stiffness.

Direct comparative test on the SAME certified runs:
  - C_rho(r)  : correlation of the (non-blind) block-mean density field.
  - C_flow(r) : correlation of the (blind) commit-flow director.
  each vs a spatial-shuffle baseline (destroys structure). Report the correlation length xi and the
  long-range plateau for each. Prediction (invariant): xi_rho >> xi_flow, C_rho long-range >> C_flow.
Grounded: reads two derived fields off the certified substrate, adds no coupling.
"""
import numpy as np
import sys, os
from collections import defaultdict
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))), "evaluation", "Bits"))
from simulator import (ParticipationGraph, NodeState, StateVector, SigmaCoeffs,  # noqa: E402
                       assign_stratum_ids, step)

COEFFS = SigmaCoeffs(kc=1.0, ks=1.0, kg=1.0, rho_star=0.5, extinction_threshold=-2.0)


def run2d(side, seed, seed_frac=0.04, max_steps=2500):
    P = side * side
    rng = np.random.default_rng(seed)
    g = ParticipationGraph()
    for r in range(side):
        for c in range(side):
            p = r * side + c
            if c + 1 < side: g.add_edge(p, r * side + c + 1, bandwidth=0.5)
            if r + 1 < side: g.add_edge(p, (r + 1) * side + c, bandwidth=0.5)
    sv = StateVector()
    for p in range(P): sv[p] = NodeState(rho=float(rng.uniform(0, 0.5)), orientation=rng.normal(size=2))
    for s in rng.choice(P, size=max(5, int(seed_frac * P)), replace=False): sv[int(s)].active = True

    class Rec:
        def __init__(self): self.seq = []
        def log_commit(self, t, u, v): self.seq.append((u, v))
        def snapshot(self, t, state): pass
    rec = Rec()
    for t in range(1, max_steps + 1):
        if step(sv, g, COEFFS, strata=assign_stratum_ids(sv, g), recorder=rec, t=t) == 0:
            break
    rho = np.array([sv[p].rho for p in range(P)]).reshape(side, side)
    return rec.seq, rho, side


def block_fields(commits, rho, side, B):
    n = side // B
    flow = np.zeros((n, n, 2)); active = np.zeros((n, n), bool)
    for (u, v) in commits:
        ru, cu = divmod(u, side); rv, cv = divmod(v, side)
        br, bc = rv // B, cv // B
        if br < n and bc < n:
            flow[br, bc] += (rv - ru, cv - cu); active[br, bc] = True
    rb = rho[:n*B, :n*B].reshape(n, B, n, B).mean(axis=(1, 3))
    m = np.linalg.norm(flow, axis=-1, keepdims=True)
    uflow = np.divide(flow, m, out=np.zeros_like(flow), where=m > 1e-9)
    return rb, uflow, active


def scalar_corr(field, mask):
    """normalized C(r) = <df(x)df(x+r)>/var, over active cells."""
    pts = np.argwhere(mask)
    vals = np.array([field[tuple(p)] for p in pts], float)
    vals = vals - vals.mean(); var = vals.var()
    if var < 1e-12: return {}
    acc = defaultdict(list)
    for a in range(len(pts)):
        for b in range(a + 1, len(pts)):
            d = int(round(np.linalg.norm(pts[a] - pts[b])))
            if d <= 14: acc[d].append(vals[a] * vals[b])
    return {d: np.mean(v) / var for d, v in sorted(acc.items()) if len(v) >= 30}


def vector_corr(u, mask):
    pts = np.argwhere(mask)
    acc = defaultdict(list)
    for a in range(len(pts)):
        na = u[tuple(pts[a])]
        for b in range(a + 1, len(pts)):
            d = int(round(np.linalg.norm(pts[a] - pts[b])))
            if d <= 14: acc[d].append(float(na @ u[tuple(pts[b])]))
    return {d: np.mean(v) for d, v in sorted(acc.items()) if len(v) >= 30}


def xi(C):
    """correlation length: first r where C(r) falls below C(1)/e (0 if never resolved)."""
    if 1 not in C: return np.nan
    thr = C[1] / np.e
    for d in sorted(C):
        if C[d] < thr: return d
    return max(C)  # still above threshold at max r


def main():
    side, B, NSEED = 60, 3, 12
    rng = np.random.default_rng(0)
    print("=" * 84)
    print("BLINDNESS INVARIANT, POSITIVE SIDE: does the NON-BLIND density field carry long-range")
    print("interaction order that the BLIND director field cannot?  (certified 2D Sigma-substrate)")
    print("=" * 84)
    Rho, Flow, RhoS, FlowS = defaultdict(list), defaultdict(list), defaultdict(list), defaultdict(list)
    xir, xif = [], []
    for s in range(1, NSEED + 1):
        commits, rho, sd = run2d(side, s)
        rb, uflow, active = block_fields(commits, rho, sd, B)
        if active.sum() < 30: continue
        cr = scalar_corr(rb, active); cf = vector_corr(uflow, active)
        # shuffle controls (spatially permute values among active cells)
        idx = np.argwhere(active); perm = rng.permutation(len(idx))
        rsh = rb.copy(); ush = uflow.copy()
        for a, p in zip(idx, perm):
            rsh[tuple(a)] = rb[tuple(idx[p])]; ush[tuple(a)] = uflow[tuple(idx[p])]
        crs = scalar_corr(rsh, active); cfs = vector_corr(ush, active)
        for d in cr: Rho[d].append(cr[d])
        for d in cf: Flow[d].append(cf[d])
        for d in crs: RhoS[d].append(crs[d])
        for d in cfs: FlowS[d].append(cfs[d])
        xir.append(xi(cr)); xif.append(xi(cf))

    def ms(x): return (np.nanmean(x), np.nanstd(x) / max(1, np.sqrt(np.sum(~np.isnan(x))))) if len(x) else (np.nan, 0)
    print(f"\n  {'r':>3} {'C_rho (non-blind)':>20} {'C_flow (blind)':>18} {'rho_shuf':>9} {'flow_shuf':>10}")
    for d in sorted(set(Rho) & set(Flow))[:12]:
        mr, er = ms(Rho[d]); mf, ef = ms(Flow[d])
        print(f"  {d:>3} {mr:>+12.3f}+-{er:.3f} {mf:>+12.3f}+-{ef:.3f} "
              f"{ms(RhoS.get(d,[0]))[0]:>+9.3f} {ms(FlowS.get(d,[0]))[0]:>+10.3f}")
    tR = [v for d in Rho if d >= 5 for v in Rho[d]]; tF = [v for d in Flow if d >= 5 for v in Flow[d]]
    tRs = [v for d in RhoS if d >= 5 for v in RhoS[d]]; tFs = [v for d in FlowS if d >= 5 for v in FlowS[d]]
    mtR, etR = ms(tR); mtF, etF = ms(tF); mtRs, _ = ms(tRs); mtFs, _ = ms(tFs)
    print(f"\n  correlation length xi (blocks):  rho = {ms(xir)[0]:.2f}   flow = {ms(xif)[0]:.2f}")
    print(f"  long-range (r>=5):")
    print(f"    C_rho  = {mtR:+.4f} +- {etR:.4f}   (shuffle {mtRs:+.4f})   excess {mtR-mtRs:+.4f} "
          f"({(mtR-mtRs)/max(1e-9,etR):+.1f}sig)")
    print(f"    C_flow = {mtF:+.4f} +- {etF:.4f}   (shuffle {mtFs:+.4f})   excess {mtF-mtFs:+.4f} "
          f"({(mtF-mtFs)/max(1e-9,etF):+.1f}sig)")
    print("\n  READ (tests AP's invariant, positive side):")
    print("   If C_rho long-range >> C_flow (and xi_rho >> xi_flow): the NON-BLIND density field")
    print("   carries genuine long-range INTERACTION order that the BLIND director field lacks.")
    print("   Confirms the invariant from both sides, and locates emergent organizational structure")
    print("   (curvature emergence's stiffness) in the sector the rule READS -- not the blind one.")
    print("   If C_rho ~ C_flow (both faint): the invariant's positive side fails; even non-blind")
    print("   quantities don't order here.")
    print("=" * 84)


if __name__ == "__main__":
    main()
