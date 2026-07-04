"""Local-slope 3D radial metric test -- avoids the cumulative-fit degeneracy.

The cumulative-integral exponent fits were degenerate (high R^2 for many exponents => 'best' jumps).
The LOCAL relation is clean and non-degenerate: if the emergent metric is g_rr = 1/reach^2, the
per-shell hop-speed v(r) = dD/dr (hops per unit radius) satisfies v(r) ~ 1/reach(r), i.e. the
log-log slope d(log v)/d(log reach) = -1. Likewise d(log v)/d(log b) = -q reads the composite
b-exponent directly. These are single regressions over all shells, not a shape-match of similar
integrals, so they actually resolve the exponent.

Test (nothing assumed): build the 3D lattice (wide smooth b-bowl), measure D(r) by BFS, form the
local speed v(r) = dD/dr, regress log v on log reach (expect slope -1: metric = 1/reach^2) and log v
on log b (expect -0.5: g~1/b, if reach~sqrt(b) holds through the rounding). Report slopes + R^2.
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


def shells(side, R0, p=0.5, b_min=0.25):
    S = side
    ax = np.arange(S)
    X, Y, Z = np.meshgrid(ax, ax, ax, indexing="ij")
    c = (S - 1) / 2
    r = np.sqrt((X - c) ** 2 + (Y - c) ** 2 + (Z - c) ** 2)
    b = b_min + (1.0 - b_min) * np.clip(r / c, 0, 1) ** 2
    reach = np.maximum(1, np.round(R0 * b ** p).astype(int)).ravel()
    Rmax = int(np.round(R0))
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
    reach3 = reach.reshape(S, S, S)
    rmax = int(c) - 2
    rs = np.arange(2, rmax)
    D = np.array([d[(rint == rr) & (d > 0)].mean() for rr in rs])
    B = np.array([b[rint == rr].mean() for rr in rs])
    RE = np.array([reach3[rint == rr].mean() for rr in rs])
    ok = np.isfinite(D)
    return rs[ok], D[ok], B[ok], RE[ok]


def slope(logx, logy):
    A = np.vstack([logx, np.ones_like(logx)]).T
    coef, *_ = np.linalg.lstsq(A, logy, rcond=None)
    pred = A @ coef
    r2 = 1 - np.sum((logy - pred) ** 2) / np.sum((logy - logy.mean()) ** 2)
    return coef[0], r2


def main():
    print("=" * 80)
    print("LOCAL-SLOPE 3D radial metric: v=dD/dr;  slope(log v, log reach)=-1 => g_rr=1/reach^2")
    print("=" * 80)
    print(f"\n  {'side':>5} {'R0':>4} | {'slope v~reach^?':>16} {'R^2':>6} | {'slope v~b^?':>13} {'R^2':>6}")
    for side, R0 in [(61, 4), (61, 6), (61, 8), (55, 10)]:
        rs, D, B, RE = shells(side, R0)
        v = np.gradient(D, rs)                       # local hop-speed dD/dr
        m = v > 0
        s_reach, r2r = slope(np.log(RE[m]), np.log(v[m]))
        s_b, r2b = slope(np.log(B[m]), np.log(v[m]))
        gr = "g_rr=1/reach^2" if abs(-s_reach - 1) < 0.15 else f"g_rr=1/reach^{-2*s_reach:.2f}"
        print(f"  {side:>5d} {R0:>4.0f} | v~reach^{s_reach:+.2f}  {gr:>15} {r2r:>6.3f} "
              f"| v~b^{s_b:+.2f} (q={-s_b:.2f}) {r2b:>6.3f}")
    print("\n  READ:")
    print("   slope(v, reach) ~ -1 with good R^2 => the emergent 3D radial metric is g_rr = 1/reach^2")
    print("   (hop-speed is 1/reach): the clean geometric statement, non-degenerate. With the step-2")
    print("   derived reach~sqrt(b) this is g_rr~1/b (GR-I). slope(v, b) ~ -0.5 reads the same through")
    print("   the b-field directly; departures from -0.5 are the integer-rounding of reach vs sqrt(b).")
    print("=" * 80)


if __name__ == "__main__":
    main()
