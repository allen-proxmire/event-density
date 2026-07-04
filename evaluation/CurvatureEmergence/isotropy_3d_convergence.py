"""Is the 3D radial exponent q=0.8 (and the axis/diagonal anisotropy) REAL, or integer-reach
discretization? Decisive test: make the reach finer (raise R0) and watch q and the anisotropy.

First 3D run (R0=3, reach in {1,2,3}) gave isotropy CoV~0.06 but radial q~0.8 (g~1/b^1.6), not the
q=0.5 the 1D and holographic probes gave cleanly. Prime suspect: with reach = round(R0*b^p) taking
only 3 integer values, the rounding (esp. the floor to 1 at low b) STEEPENS the effective law past
b^p. The 1D probe used reach up to 12 (fine) -> clean 0.5. If discretization is the cause, then as
R0 grows (reach finer) q must fall toward 0.5 and the axis/diagonal anisotropy must shrink. If q
stays ~0.8, the 3D result genuinely departs from the 1D derivation and step 2 needs revisiting.

Honest either way: this sweep decides it, it is not tuned to a hoped answer.
"""
import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.csgraph import shortest_path


def build_offsets(Rmax):
    rng = range(-Rmax, Rmax + 1)
    offs, lens = [], []
    for dx in rng:
        for dy in rng:
            for dz in rng:
                d = np.sqrt(dx * dx + dy * dy + dz * dz)
                if 0 < d <= Rmax:
                    offs.append((dx, dy, dz)); lens.append(d)
    return np.array(offs), np.array(lens)


def run(side, R0, p=0.5, b_min=0.2):
    S = side
    ax = np.arange(S)
    X, Y, Z = np.meshgrid(ax, ax, ax, indexing="ij")
    c = (S - 1) / 2
    r = np.sqrt((X - c) ** 2 + (Y - c) ** 2 + (Z - c) ** 2)
    w = S / 6.0
    b = 1.0 - (1.0 - b_min) * np.exp(-(r ** 2) / (2 * w ** 2))
    reach = np.maximum(1, np.round(R0 * b ** p).astype(int)).ravel()
    Rmax = int(np.round(R0 * 1.0))
    offs, lens = build_offsets(Rmax)
    N = S ** 3
    lin = np.arange(N)
    coords = np.stack([X.ravel(), Y.ravel(), Z.ravel()], axis=1)
    rows, cols = [], []
    for (o, dlen) in zip(offs, lens):
        nb = coords + o
        inb = np.all((nb >= 0) & (nb < S), axis=1)
        src = lin[inb]
        dst = (nb[inb, 0] * S + nb[inb, 1]) * S + nb[inb, 2]
        keep = reach[src] >= dlen
        rows.append(src[keep]); cols.append(dst[keep])
    rows = np.concatenate(rows); cols = np.concatenate(cols)
    G = coo_matrix((np.ones(len(rows), np.int8), (rows, cols)), shape=(N, N)).tocsr()
    cc = int(round(c)); centre = (cc * S + cc) * S + cc
    d = shortest_path(G, method="D", unweighted=True, indices=centre).reshape(S, S, S)

    rint = np.round(r).astype(int)
    rmax = int(c) - 1
    # radial exponent
    rs = np.arange(2, rmax)
    bshell = np.array([b[rint == rr].mean() for rr in rs])
    hshell = np.array([d[(rint == rr) & (d > 0)].mean() if (rint == rr).any() else np.nan for rr in rs])
    ok = np.isfinite(hshell) & (hshell > 0)
    rs2, bshell, hshell = rs[ok], bshell[ok], hshell[ok]
    best, bestq = -np.inf, None
    for q in np.linspace(0.1, 1.6, 61):
        integ = np.cumsum(1.0 / bshell ** q)
        A = np.vstack([integ, np.ones_like(integ)]).T
        coef, *_ = np.linalg.lstsq(A, hshell, rcond=None)
        r2 = 1 - np.sum((hshell - A @ coef) ** 2) / np.sum((hshell - hshell.mean()) ** 2)
        if r2 > best:
            best, bestq = r2, q
    # anisotropy: axis vs body-diagonal at mid radius
    rr = int(0.7 * rmax)
    a = c + np.array([rr, 0, 0]); g = c + rr / np.sqrt(3) * np.array([1, 1, 1])
    ha = float(d[tuple(np.round(a).astype(int))]); hg = float(d[tuple(np.round(g).astype(int))])
    aniso = abs(ha - hg) / (0.5 * (ha + hg))
    # mean shell CoV
    covs = []
    for rrr in range(5, rmax, 3):
        m = (rint == rrr) & (d > 0)
        if m.sum() > 20:
            hh = d[m].astype(float); covs.append(hh.std() / hh.mean())
    return bestq, best, aniso, float(np.mean(covs)), reach.max()


def main():
    print("=" * 82)
    print("3D CONVERGENCE: does radial q -> 0.5 and anisotropy -> 0 as reach gets finer?")
    print("  (if yes, q=0.8 was integer-reach discretization and the 1D/holographic 0.5 stands)")
    print("=" * 82)
    print(f"\n  {'side':>5} {'R0':>4} {'max reach':>10} {'radial q':>9} {'R^2':>7} "
          f"{'axis/diag aniso':>16} {'shell CoV':>10}")
    # keep memory bounded: shrink side as R0 (hence reach-ball) grows
    configs = [(45, 2), (45, 3), (45, 4), (45, 5), (41, 6), (37, 8)]
    qs = []
    for side, R0 in configs:
        q, r2, aniso, cov, mr = run(side, R0)
        qs.append((R0, q))
        print(f"  {side:>5d} {R0:>4.0f} {mr:>10d} {q:>9.3f} {r2:>7.3f} {aniso:>16.3f} {cov:>10.3f}")
    print("\n  READ:")
    trend = "FALLS toward 0.5" if qs[-1][1] < qs[0][1] - 0.05 else "does NOT fall"
    print(f"   radial q {trend} as reach gets finer (R0 2 -> 8).")
    print("   If q -> ~0.5 and aniso -> small: the 3D metric is g~1/b (GR-I), isotropic; the earlier")
    print("   q=0.8 was integer-reach discretization (rounding floors the low-b reach, steepening the")
    print("   effective law). If q stays ~0.8: a genuine 3D departure -- step 2 would need revisiting.")
    print("=" * 82)


if __name__ == "__main__":
    main()
