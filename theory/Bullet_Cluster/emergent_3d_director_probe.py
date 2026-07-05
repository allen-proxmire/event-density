"""#1: certified Sigma-rule on a 3D LATTICE GRAPH -- lift the 2D cap that blocked O(3) everywhere.

The certified Bits Sigma-rule is graph-based (arbitrary edges) and orientation-blind (reads rho +
graph-local structure only). So running it on a 3D lattice graph is the CERTIFIED RULE, not a
stand-in -- only the edge set changes. On a 3D lattice the spatial commit-flow director is a genuine
3D vector field, so it CAN host pi_2(S^2)=Z hedgehog monopoles (the arc's actual object), which 2D
structurally forbade (2D allows only O(2) vortices).

Measured on the certified 3D run, per the arc's three requirements:
  (a) ORDERING     : does the 3D commit-flow director show long-range order? C(r)=<n.n'> vs shuffle.
  (b) MONOPOLES    : does it carry integer hedgehog windings (topological charge) above a shuffle?
  (c) DISPLACEABLE : is it decoupled from grad-rho?  |cos| vs the 3D-random baseline (=1/2).
Also the accumulated-flow field (sum of ALL commit displacements through a region, a persistent
memory field) is measured alongside the momentary flow -- the emergent-free-energy result showed
momentary flow washes out under sparse becoming, so a persistent field is the natural fix.

DISCIPLINE: the topological-charge code is VALIDATED on a synthetic hedgehog (Q=+1) and a uniform
field (Q=0) before it is trusted on substrate data (chains-as-links lesson: validate the tool first).
"""
import numpy as np
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))), "evaluation", "Bits"))
from simulator import (ParticipationGraph, NodeState, StateVector, SigmaCoeffs,  # noqa: E402
                       assign_stratum_ids, step)

COEFFS = SigmaCoeffs(kc=1.0, ks=1.0, kg=1.0, rho_star=0.5, extinction_threshold=-2.0)


# ---------------------------------------------------------------- topological charge (3D monopole)
# Solid angle of a spherical triangle (Van Oosterom-Strackee); sum over the outward-oriented
# triangulation of a cube's surface; Q = (1/4pi) * sum.  Returns the enclosed monopole charge.
_FACES = [  # each: 4 corner (i,j,k) in CCW order seen from OUTSIDE
    [(0,0,0),(0,0,1),(0,1,1),(0,1,0)],   # x=0, normal -x
    [(1,0,0),(1,1,0),(1,1,1),(1,0,1)],   # x=1, normal +x
    [(0,0,0),(1,0,0),(1,0,1),(0,0,1)],   # y=0, normal -y
    [(0,1,0),(0,1,1),(1,1,1),(1,1,0)],   # y=1, normal +y
    [(0,0,0),(0,1,0),(1,1,0),(1,0,0)],   # z=0, normal -z
    [(0,0,1),(1,0,1),(1,1,1),(0,1,1)],   # z=1, normal +z
]


def _omega(a, b, c):
    num = float(a @ np.cross(b, c))
    den = 1.0 + float(a @ b) + float(b @ c) + float(c @ a)
    return 2.0 * np.arctan2(num, den)


def cube_charge(corner_dirs):
    """corner_dirs: dict (i,j,k)->unit vec for the 8 cube corners. Returns Q ~ integer."""
    s = 0.0
    for f in _FACES:
        v = [corner_dirs[p] for p in f]
        s += _omega(v[0], v[1], v[2]) + _omega(v[0], v[2], v[3])   # split quad into 2 triangles
    return s / (4.0 * np.pi)


def _selftest():
    # hedgehog centred at cube centre (0.5,0.5,0.5): director points radially outward -> Q=+1
    hh = {}
    for i in (0, 1):
        for j in (0, 1):
            for k in (0, 1):
                d = np.array([i - 0.5, j - 0.5, k - 0.5]); hh[(i, j, k)] = d / np.linalg.norm(d)
    q_hh = cube_charge(hh)
    uni = {p: np.array([0, 0, 1.0]) for p in hh}
    q_uni = cube_charge(uni)
    return q_hh, q_uni


# ------------------------------------------------------------------------- certified 3D substrate
def run3d(side, seed, seed_frac=0.05, max_steps=4000):
    P = side ** 3
    def idx(x, y, z): return (x * side + y) * side + z
    rng = np.random.default_rng(seed)
    g = ParticipationGraph()
    for x in range(side):
        for y in range(side):
            for z in range(side):
                p = idx(x, y, z)
                if x + 1 < side: g.add_edge(p, idx(x+1, y, z), bandwidth=0.5)
                if y + 1 < side: g.add_edge(p, idx(x, y+1, z), bandwidth=0.5)
                if z + 1 < side: g.add_edge(p, idx(x, y, z+1), bandwidth=0.5)
    sv = StateVector()
    rho0 = rng.uniform(0.0, 0.5, size=P)
    for p in range(P): sv[p] = NodeState(rho=float(rho0[p]), orientation=rng.normal(size=2))
    nseed = max(5, int(seed_frac * P))
    for s in rng.choice(P, size=nseed, replace=False): sv[int(s)].active = True

    class Rec:
        def __init__(self): self.seq = []
        def log_commit(self, t, u, v): self.seq.append((u, v))
        def snapshot(self, t, state): pass
    rec = Rec()
    for t in range(1, max_steps + 1):
        if step(sv, g, COEFFS, strata=assign_stratum_ids(sv, g), recorder=rec, t=t) == 0:
            break
    rho = np.array([sv[p].rho for p in range(P)]).reshape(side, side, side)
    return rec.seq, rho, side


def coords(v, side):
    x = v // (side * side); r = v % (side * side); return x, r // side, r % side


def block_fields(commits, rho, side, B):
    """Coarse block directors: momentary (first commit into a node) and accumulated (all commits)."""
    n = side // B
    mom = np.zeros((n, n, n, 3)); acc = np.zeros((n, n, n, 3))
    seen = set()
    for (u, v) in commits:
        xu, yu, zu = coords(u, side); xv, yv, zv = coords(v, side)
        d = np.array([xv - xu, yv - yu, zv - zu], float)
        bx, by, bz = xv // B, yv // B, zv // B
        if bx < n and by < n and bz < n:
            acc[bx, by, bz] += d
            if v not in seen:
                seen.add(v); mom[bx, by, bz] += d
    rb = rho[:n*B, :n*B, :n*B].reshape(n, B, n, B, n, B).mean(axis=(1, 3, 5))
    gx, gy, gz = np.gradient(rb); grad = np.stack([gx, gy, gz], axis=-1)
    def unit(f):
        m = np.linalg.norm(f, axis=-1, keepdims=True)
        return np.divide(f, m, out=np.zeros_like(f), where=m > 1e-9), m[..., 0]
    umom, mmom = unit(mom); uacc, macc = unit(acc); ugrad, _ = unit(grad)
    return umom, mmom, uacc, macc, ugrad


def corr3d(u, mag):
    from collections import defaultdict
    pts = np.argwhere(mag > 0)
    acc = defaultdict(list)
    for a in range(len(pts)):
        pa = pts[a]; na = u[tuple(pa)]
        for b in range(a + 1, len(pts)):
            pb = pts[b]; d = int(round(np.linalg.norm(pa - pb)))
            if d <= 10: acc[d].append(float(na @ u[tuple(pb)]))
    return {d: (np.mean(v), len(v)) for d, v in sorted(acc.items()) if len(v) >= 20}


def total_charge(u, mag):
    n = u.shape[0]; filled = mag > 0
    tot = 0.0; net = 0.0; cnt = 0
    for i in range(n-1):
        for j in range(n-1):
            for k in range(n-1):
                cds = {}
                ok = True
                for di in (0,1):
                    for dj in (0,1):
                        for dk in (0,1):
                            if not filled[i+di, j+dj, k+dk]: ok = False; break
                            cds[(di,dj,dk)] = u[i+di, j+dj, k+dk]
                if not ok: continue
                q = cube_charge(cds); tot += abs(q); net += q; cnt += 1
    return tot, net, cnt


def main():
    print("=" * 86)
    print("CERTIFIED SIGMA-RULE ON A 3D LATTICE: does an ordering, monopole-capable, displaceable")
    print("director emerge?  (lifts the 2D cap; same certified rule, 3D graph)")
    print("=" * 86)
    qhh, quni = _selftest()
    print(f"\n  TOOL SELF-TEST (before trusting it): hedgehog Q = {qhh:+.3f} (expect +1.000), "
          f"uniform Q = {quni:+.3f} (expect 0.000)  -> {'PASS' if abs(qhh-1)<1e-6 and abs(quni)<1e-6 else 'FAIL'}")

    side, B, NSEED = 24, 3, 6
    rng = np.random.default_rng(0)
    from collections import defaultdict
    Cm, Ca, Cs = defaultdict(list), defaultdict(list), defaultdict(list)
    align_mom, align_acc = [], []
    chg_acc_tot, chg_acc_net, chg_shuf_tot, ncube = [], [], [], []
    ncommit, nfill = [], []
    for s in range(1, NSEED + 1):
        commits, rho, sd = run3d(side, s)
        umom, mmom, uacc, macc, ugrad = block_fields(commits, rho, sd, B)
        ncommit.append(len(commits)); nfill.append(int((macc > 0).sum()))
        for d, (val, _) in corr3d(umom, mmom).items(): Cm[d].append(val)
        for d, (val, _) in corr3d(uacc, macc).items(): Ca[d].append(val)
        # shuffle control on accumulated field
        idxf = np.argwhere(macc > 0); perm = rng.permutation(len(idxf))
        ush = uacc.copy()
        for a, p in zip(idxf, perm): ush[tuple(a)] = uacc[tuple(idxf[p])]
        for d, (val, _) in corr3d(ush, macc).items(): Cs[d].append(val)
        gmask = np.linalg.norm(ugrad, axis=-1) > 1e-9
        for a in np.argwhere((mmom > 0) & gmask): align_mom.append(abs(umom[tuple(a)] @ ugrad[tuple(a)]))
        for a in np.argwhere((macc > 0) & gmask): align_acc.append(abs(uacc[tuple(a)] @ ugrad[tuple(a)]))
        tot, net, cnt = total_charge(uacc, macc)
        ts, _, _ = total_charge(ush, macc)
        if cnt > 0: chg_acc_tot.append(tot/cnt); chg_acc_net.append(net); chg_shuf_tot.append(ts/cnt); ncube.append(cnt)

    def ms(x): return (np.mean(x), np.std(x)/max(1, np.sqrt(len(x)))) if len(x) else (float('nan'), 0)
    print(f"\n  per-run: {np.mean(ncommit):.0f} commits, {np.mean(nfill):.0f} filled blocks, "
          f"{np.mean(ncube):.0f} closed cubes for charge")

    print("\n (a) ORDERING  C(r) of the 3D director (accumulated), vs shuffle:")
    for d in sorted(Ca)[:8]:
        ma, ea = ms(Ca[d]); msf, _ = ms(Cs.get(d, [0]))
        print(f"    r={d}: acc={ma:+.3f}+-{ea:.3f}  shuffle={msf:+.3f}  (mom={ms(Cm.get(d,[0]))[0]:+.3f})")
    tailA = [v for d in Ca if d >= 4 for v in Ca[d]]; tailS = [v for d in Cs if d >= 4 for v in Cs[d]]
    mta, eta = ms(tailA); mts, ets = ms(tailS)
    print(f"    long-range (r>=4): acc={mta:+.4f}+-{eta:.4f}  shuffle={mts:+.4f}  "
          f"diff={mta-mts:+.4f} ({(mta-mts)/max(1e-9,np.hypot(eta,ets)):+.1f}sig)")

    am, ae = ms(align_acc); amm, aem = ms(align_mom)
    print("\n (c) DISPLACEABILITY  |cos(flow, grad-rho)| vs 3D-random baseline 0.500:")
    print(f"    accumulated = {am:.3f}+-{ae:.3f}   momentary = {amm:.3f}+-{aem:.3f}   "
          f"(=>1 slaved; ~0.5 decoupled)")

    ct, et = ms(chg_acc_tot); cs, es = ms(chg_shuf_tot); cn, en = ms(chg_acc_net)
    print("\n (b) MONOPOLES  topological charge of the 3D director (accumulated):")
    print(f"    total|Q|/cube = {ct:.3f}+-{et:.3f}   shuffle = {cs:.3f}+-{es:.3f}   "
          f"net Q/run = {cn:+.2f}")
    print(f"    (real>shuffle => hosts hedgehog windings beyond noise; ~equal => none)")

    print("\n  READ: (a) long-range acc vs shuffle => ordering or not; (b) charge vs shuffle =>")
    print("  monopole capacity or not; (c) |cos|~0.5 => displaceable. This is the CERTIFIED rule on")
    print("  a 3D graph -- O(3)/monopoles are now reachable, unlike every 2D probe before.")
    print("=" * 86)


if __name__ == "__main__":
    main()
