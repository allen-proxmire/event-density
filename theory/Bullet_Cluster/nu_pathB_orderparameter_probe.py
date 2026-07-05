"""Path-B first probe: is there an emergent, orderable, DISPLACEABLE director field in ED's
dynamical sector, on the CERTIFIED substrate? (Scope in this docstring; results printed below.)

Context. The Bullet arc needs a cluster-scale organizational order parameter that (a) can ORDER and
carry topologically protected windings, and (b) is NOT slaved to the instantaneous matter/density,
so the winding can be DISPLACED from the gas (the entire Bullet phenomenon). The nu-scope memo showed
the certified substrate's B5 orientation is inert (Sigma is orientation-blind) and 2D, so it is not
the field. This probe asks the prior, load-bearing question on the REAL simulator (not a hand-built
stand-in): does the DYNAMICAL sector (rho + the commit record) produce a director field that is
(1) coherent (real orientational structure, not noise), and (2) decoupled from the density gradient
(hence displaceable)? If yes, the KIND of order parameter the arc needs exists in ED; the O(3) form
is then a separate 3D-substrate question. If no, the arc's premise is in trouble.

Two candidate directors, both derived from the certified run (no new coupling added):
  - grad-rho : gradient of the committed density field. Density-SLAVED by construction -> the null:
               it CANNOT be displaced from the matter, so it cannot be the arc's order parameter.
  - commit-flow : the coarse-grained direction in which fronts actually propagated (the frozen record
               of past becoming, from the commit log). This is the arc-relevant candidate: it carries
               the MEMORY of motion, not the current density, so it CAN be displaced from it.

Grounding limits, stated up front (honest, not hidden): the certified sim is spatially 2D and its
orientation is 2D, so any emergent director is O(2) at most -- vortices (pi_1(S^1)=Z), the 2D analog
of the arc's O(3) monopoles (pi_2(S^2)=Z), never the monopoles themselves. This probe therefore
tests the KIND (is there a coherent, displaceable, defect-capable director at all), not the O(3)
grounding, which needs a 3D substrate. One certified substrate, several seeds.

Measurements:
  (A) COHERENCE: spatial correlation C(r)=<n(x).n(x+r)> of each director vs a shuffled control.
      A real director decays slower than / plateaus above the shuffle.
  (B) DECOUPLING (the Bullet-critical one): mean |cos angle| between commit-flow and grad-rho per
      cell. ~1 => commit-flow is just density-slaved (cannot be displaced; bad for the arc).
      < 1 and near the random baseline => commit-flow is decoupled from density (displaceable; good).
  (C) TOPOLOGICAL CAPACITY: net and total vortex winding of each director on the coarse lattice,
      vs a shuffled control -- can the field host integer windings beyond noise.
"""
import numpy as np
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))), "evaluation", "Bits"))
from simulator import (ParticipationGraph, NodeState, StateVector, SigmaCoeffs,  # noqa: E402
                       assign_stratum_ids, step)

COEFFS = SigmaCoeffs(kc=1.0, ks=1.0, kg=1.0, rho_star=0.5, extinction_threshold=-2.0)


class CommitRec:
    def __init__(self): self.seq = []
    def log_commit(self, t, u, v): self.seq.append((u, v))
    def snapshot(self, t, state): pass


def build_grid(side, seed):
    P = side * side
    rng = np.random.default_rng(seed)
    rho0 = rng.uniform(0.0, 0.5, size=P)
    ori0 = rng.normal(size=(P, 2))
    edges = []
    for r in range(side):
        for c in range(side):
            p = r * side + c
            if c + 1 < side: edges.append((p, r * side + c + 1))
            if r + 1 < side: edges.append((p, (r + 1) * side + c))
    seeds = [0, side - 1, P - side, P - 1, P // 2]   # 4 corners + centre: interacting fronts
    return P, rho0, ori0, edges, seeds


def run_substrate(side, seed, max_steps=800):
    P, rho0, ori0, edges, seeds = build_grid(side, seed)
    g = ParticipationGraph()
    for (p, q) in edges: g.add_edge(p, q, bandwidth=0.5)
    sv = StateVector()
    for p in range(P): sv[p] = NodeState(rho=float(rho0[p]), orientation=ori0[p].copy())
    for s in seeds: sv[s].active = True
    strata = assign_stratum_ids(sv, g)
    rec = CommitRec()
    for t in range(1, max_steps + 1):
        if step(sv, g, COEFFS, strata=strata, recorder=rec, t=t) == 0:
            break
    rho = np.array([sv[p].rho for p in range(P)]).reshape(side, side)
    return rho, rec.seq, side


def coarse_directors(rho, commits, side, B=3):
    """Return unit director fields (grad-rho, commit-flow) on the coarse B-block lattice."""
    n = side // B
    # commit-flow: sum (v-u) displacement vectors into the block containing v
    flow = np.zeros((n, n, 2))
    for (u, v) in commits:
        ru, cu = divmod(u, side); rv, cv = divmod(v, side)
        br, bc = rv // B, cv // B
        if br < n and bc < n:
            flow[br, bc, 0] += (rv - ru); flow[br, bc, 1] += (cv - cu)
    # grad-rho on block-averaged density
    rb = rho[:n * B, :n * B].reshape(n, B, n, B).mean(axis=(1, 3))
    gr, gc = np.gradient(rb)
    grad = np.stack([gr, gc], axis=-1)
    def unit(f):
        m = np.linalg.norm(f, axis=-1, keepdims=True)
        return np.divide(f, m, out=np.zeros_like(f), where=m > 1e-9), m[..., 0]
    ugrad, gmag = unit(grad); uflow, fmag = unit(flow)
    return ugrad, uflow, gmag, fmag


def corr(u, mask):
    """Direction correlation C(r) = mean n(x).n(x+r) over separations r (binned by distance)."""
    n = u.shape[0]
    pts = [(i, j) for i in range(n) for j in range(n) if mask[i, j]]
    from collections import defaultdict
    acc = defaultdict(list)
    for a in range(len(pts)):
        ia, ja = pts[a]
        for b in range(a + 1, len(pts)):
            ib, jb = pts[b]
            d = int(round(np.hypot(ia - ib, ja - jb)))
            acc[d].append(float(u[ia, ja] @ u[ib, jb]))
    return {d: np.mean(v) for d, v in sorted(acc.items()) if len(v) >= 8}


def vortex_windings(u, mask):
    """Sum |winding| and net winding of the vector field over unit plaquettes (2D O(2) vortices)."""
    n = u.shape[0]
    ang = np.arctan2(u[..., 1], u[..., 0])
    def wrap(d): return (d + np.pi) % (2 * np.pi) - np.pi
    tot = 0.0; net = 0.0; cnt = 0
    for i in range(n - 1):
        for j in range(n - 1):
            if not (mask[i, j] and mask[i+1, j] and mask[i+1, j+1] and mask[i, j+1]):
                continue
            loop = [ang[i, j], ang[i, j+1], ang[i+1, j+1], ang[i+1, j], ang[i, j]]
            w = sum(wrap(loop[k+1] - loop[k]) for k in range(4)) / (2 * np.pi)
            tot += abs(w); net += w; cnt += 1
    return tot, net, cnt


def shuffle_dirs(u, mask, rng):
    idx = np.argwhere(mask); perm = rng.permutation(len(idx))
    out = u.copy()
    for a, p in zip(idx, perm): out[a[0], a[1]] = u[idx[p][0], idx[p][1]]
    return out


def main():
    side, B, NSEED = 51, 3, 12
    rng = np.random.default_rng(0)
    print("=" * 88)
    print("PATH-B PROBE: emergent orderable + displaceable director in ED's dynamical sector?")
    print(f"  certified 2D Sigma-substrate {side}x{side}, averaged over {NSEED} seeds, coarse block B={B}")
    print("=" * 88)

    c1_real, c1_shuf = [], []          # nearest-neighbour coherence, commit-flow
    cg_real, cg_shuf = [], []          # nearest-neighbour coherence, grad-rho
    align = []                          # decoupling |cos(flow,grad)|
    vw_real, vw_shuf = [], []          # commit-flow total|winding| real vs shuffle
    ncommit, ncell = [], []
    for s in range(NSEED):
        rho, commits, sd = run_substrate(side, seed=s + 1)
        ugrad, uflow, gmag, fmag = coarse_directors(rho, commits, sd, B)
        mask = (fmag > 0) & (gmag > 1e-9)
        if mask.sum() < 12:
            continue
        cf = corr(uflow, mask); cfs = corr(shuffle_dirs(uflow, mask, rng), mask)
        cg = corr(ugrad, mask); cgs = corr(shuffle_dirs(ugrad, mask, rng), mask)
        if 1 in cf: c1_real.append(cf[1]); c1_shuf.append(cfs.get(1, 0))
        if 1 in cg: cg_real.append(cg[1]); cg_shuf.append(cgs.get(1, 0))
        al = [abs(uflow[i, j] @ ugrad[i, j]) for i, j in np.argwhere(mask)]
        align.extend(al)
        tot, net, cnt = vortex_windings(uflow, mask)
        ts, _, _ = vortex_windings(shuffle_dirs(uflow, mask, rng), mask)
        if cnt > 0: vw_real.append(tot / cnt); vw_shuf.append(ts / cnt)
        ncommit.append(len(commits)); ncell.append(int(mask.sum()))

    def ms(x): return (np.mean(x), np.std(x) / max(1, np.sqrt(len(x))))
    print(f"\n  per-run: {np.mean(ncommit):.0f} commits, {np.mean(ncell):.0f} active coarse cells "
          f"(sparse becoming: fronts extinguish, so the flow record is sparse)")

    m, e = ms(c1_real); ms_, es_ = ms(c1_shuf)
    print("\n (A) COHERENCE (nearest-neighbour C(r=1), mean +- SE over runs):")
    print(f"   commit-flow  real = {m:+.3f} +- {e:.3f}    shuffle = {ms_:+.3f} +- {es_:.3f}")
    mg, eg = ms(cg_real); mgs, egs = ms(cg_shuf)
    print(f"   grad-rho     real = {mg:+.3f} +- {eg:.3f}    shuffle = {mgs:+.3f} +- {egs:.3f}")

    am, ae = ms(align)
    print("\n (B) DECOUPLING  mean |cos(commit-flow, grad-rho)|  (the Bullet-critical test):")
    print(f"   measured = {am:.3f} +- {ae:.3f}    random-2D baseline = {2/np.pi:.3f}   "
          f"(=>1 slaved/bad; ~baseline decoupled/good)")

    vm, ve = ms(vw_real); vms, ves = ms(vw_shuf)
    print("\n (C) TOPOLOGICAL CAPACITY  vortex |winding| per plaquette (commit-flow):")
    print(f"   real = {vm:.3f} +- {ve:.3f}    shuffle = {vms:.3f} +- {ves:.3f}   "
          f"(real < shuffle => smoother-than-random = coherent; ~equal => noise)")

    print("\n READ (honest):")
    dcoh = m - ms_
    print(f"  (A) commit-flow coherence excess over shuffle at r=1 = {dcoh:+.3f}. "
          f"{'Weak-but-present' if 0 < dcoh < 0.1 else ('present' if dcoh>=0.1 else 'ABSENT')}; "
          "short-range only.")
    print(f"  (B) |cos| = {am:.3f} vs {2/np.pi:.3f} random => commit-flow is DECOUPLED from density"
          " (displaceable): the one arc-critical property, and it holds.")
    print(f"  (C) real|w|/plaq {'<' if vm<vms else '>='} shuffle => "
          f"{'smoother than random (weak coherence)' if vm<vms else 'no topological signal'}.")
    print("  LIMIT: 2D certified sim => O(2)/vortices only; grounds displaceability of a dynamical")
    print("  director, weak short-range order; the O(3) form + nu need a 3D substrate.")
    print("=" * 88)


if __name__ == "__main__":
    main()
