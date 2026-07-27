"""
Curvature emergence -- does GR-III's NONLINEAR, horizon-forming rule survive on a
COORDINATE-FREE relational graph? (REDESIGN after adversarial review killed two
legs of the first attempt.)

First-attempt post-mortem (why this version exists):
  * mass-scaling r_s~M^1.00 was a LINEARITY TAUTOLOGY -- in the weak/no-clip
    regime any linear functional of the deficit is ∝ amp, for any profile.
  * area-law exponent was fit over r_s ∈ {6,7} (0.15-decade lever arm) because a
    FIXED-WIDTH source saturates the frozen core -- not a measurement.

This redesign fixes both:
  * BIG, SPARSE graph (long hops => room for r_s to sweep a decade).
  * COMPACT source, sweep the source strength kappa over a decade. The clip makes
    b=0 where the linear deficit (S*kappa/D)*G(r) >= 1, i.e. out to r_s ∝ kappa
    (G~1/r in 3D). So the HORIZON radius grows ∝ kappa -- a genuine, non-tautological
    Schwarzschild r_s~M test, measured FROM THE HORIZON, over a real range.
  * HARD LEVER-ARM GUARD: no exponent is quoted unless log10(r_s) spans >= 0.7
    (a factor of 5). Runs whose horizon reaches the frame are dropped (frame-limited).

Faithful GR-III rule: b += D*(mean_nbr - b) - kappa*rho, b>=0 (P04), frame b=1.
mean_nbr = D_deg^{-1} A b (degree-normalized graph Laplacian = the RGG analog of
the lattice's neighbour-mean stencil; uniform sampling => same Laplace-Beltrami
limit). Coordinates are used ONLY to build the graph and place the source; every
measurement (hop-distance via BFS, edge/node counts) is graph-intrinsic. Scope:
tests the DYNAMICS are relational, NOT that the dimension is derived (graph built
~d-dim = P06 input, accepted). Elliptic rule => Hawking kappa~1/r_h NOT expected.
Nothing tuned to a target.
"""
import numpy as np
from math import pi, gamma
from collections import deque
from scipy.spatial import cKDTree
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components


def build_rgg(N, dim, mean_deg, seed):
    rng = np.random.default_rng(seed)
    pts = rng.random((N, dim))
    Vd = pi ** (dim / 2) / gamma(dim / 2 + 1)
    r = (mean_deg / (N * Vd)) ** (1.0 / dim)
    tree = cKDTree(pts)
    pairs = tree.query_pairs(r, output_type='ndarray')
    ii = np.concatenate([pairs[:, 0], pairs[:, 1]])
    jj = np.concatenate([pairs[:, 1], pairs[:, 0]])
    A = csr_matrix((np.ones(len(ii), np.float64), (ii, jj)), shape=(N, N))
    lab = connected_components(A, directed=False)[1]
    vals, cnt = np.unique(lab, return_counts=True)
    keep = np.where(lab == vals[np.argmax(cnt)])[0]
    return pts[keep], A[keep][:, keep].tocsr()


def bfs_hops(A, src):
    hop = np.full(A.shape[0], -1, np.int32)
    hop[src] = 0
    dq = deque([src]); ip, ix = A.indptr, A.indices
    while dq:
        u = dq.popleft()
        for v in ix[ip[u]:ip[u + 1]]:
            if hop[v] < 0:
                hop[v] = hop[u] + 1; dq.append(v)
    return hop


def solve_steady(A, invdeg, rho, frame, D=0.2, kappa=1.0, steps=9000):
    b = np.ones(A.shape[0])
    kr = kappa * rho
    for _ in range(steps):
        b += D * (invdeg * (A @ b) - b) - kr
        np.clip(b, 0.0, None, out=b)
        b[frame] = 1.0
    return b


def measure(b, hop, A, frame_hop, eps=1e-6):
    frozen = (b < eps)
    Nf = int(frozen.sum())
    if Nf < 8:
        return None
    r_s = int(hop[frozen].max())
    if r_s >= 0.75 * frame_hop:          # frame-limited: horizon reached the boundary
        return dict(frame_limited=True, r_s=r_s, N_frozen=Nf)
    fz = frozen.astype(np.float64)
    N_surface = int(round(fz @ (A @ (1.0 - fz))))
    return dict(frame_limited=False, r_s=r_s, N_frozen=Nf, N_surface=N_surface)


def intrinsic_dim(hop, kmax):
    ks = np.arange(1, kmax + 1)
    ball = np.array([((hop >= 0) & (hop <= k)).sum() for k in ks], float)
    return np.polyfit(np.log(ks[2:]), np.log(ball[2:]), 1)[0]


def deficit_slope(b, hop, frame_hop, sigma):
    """Linear-profile check: deficit(hop) ~ 1/hop in 3D, measured FAR from frame."""
    hmax = hop.max()
    c, dm = [], []
    for k in range(1, hmax + 1):
        m = (hop == k)
        if m.sum() >= 30:
            c.append(float(k)); dm.append(1.0 - b[m].mean())
    c, dm = np.array(c), np.array(dm)
    o = (c > 3 * sigma) & (c < 0.60 * frame_hop) & (dm > 1e-4)   # vacuum, away from frame
    if o.sum() < 5:
        return None, 0
    return np.polyfit(np.log(c[o]), np.log(dm[o]), 1)[0], int(o.sum())


def run_case(dim, N, mean_deg, kappas, seed=7, D=0.2, sigma_hop=1.2, steps=9000):
    pts, A = build_rgg(N, dim, mean_deg, seed)
    Nc = A.shape[0]
    deg = np.asarray(A.sum(1)).ravel()
    invdeg = 1.0 / np.maximum(deg, 1)
    src = int(np.argmin(((pts - pts.mean(0)) ** 2).sum(1)))
    hop = bfs_hops(A, src)
    hmax = int(hop.max())
    frame = hop >= int(0.88 * hmax)
    frame_hop = 0.88 * hmax
    d_meas = intrinsic_dim(hop, int(0.55 * hmax))
    rho = np.exp(-(hop.astype(float) ** 2) / (2 * sigma_hop ** 2)); rho[frame] = 0.0
    print(f"[{dim}D] nodes={Nc}  mean_deg={deg.mean():.1f}  hop_diam={hmax}  "
          f"intrinsic_dim={d_meas:.2f} (target {dim})")
    rows, defslope = [], None
    for kap in kappas:
        b = solve_steady(A, invdeg, rho, frame, D=D, kappa=kap, steps=steps)
        m = measure(b, hop, A, frame_hop)
        tag = ""
        if m is None:
            tag = f"no horizon (min b={b.min():.2e})"
            if defslope is None:                       # use weakest no-horizon run for the profile
                defslope, npts = deficit_slope(b, hop, frame_hop, sigma_hop)
                if defslope is not None:
                    tag += f"  [deficit-slope {defslope:+.2f} over {npts} shells]"
        elif m['frame_limited']:
            tag = f"FRAME-LIMITED r_s={m['r_s']} (dropped)"
        else:
            rows.append((kap, m['r_s'], m['N_frozen'], m['N_surface']))
            tag = f"r_s={m['r_s']:3d}  N_frozen={m['N_frozen']:7d}  N_surface={m['N_surface']:7d}"
        print(f"   kappa={kap:7.3f}   {tag}")

    out = dict(dim=dim, d=d_meas, defslope=defslope, n=len(rows))
    if len(rows) >= 4:
        kap = np.array([r[0] for r in rows]); rs = np.array([r[1] for r in rows], float)
        Nf = np.array([r[2] for r in rows], float); Ns = np.array([r[3] for r in rows], float)
        lever = np.log10(rs.max() / rs.min())
        out['lever'] = lever
        print(f"   r_s range {rs.min():.0f}..{rs.max():.0f}  (lever arm {lever:.2f} decades)")
        if lever >= 0.7:
            out['p_rsM'] = np.polyfit(np.log(kap), np.log(rs), 1)[0]
            out['p_area'] = np.polyfit(np.log(rs), np.log(Ns), 1)[0]
            out['p_vol'] = np.polyfit(np.log(rs), np.log(Nf), 1)[0]
            print(f"   --> r_s ~ kappa^{out['p_rsM']:.2f} (mass-scaling=1)   "
                  f"N_surface ~ r_s^{out['p_area']:.2f} (AREA={dim-1})   "
                  f"N_frozen ~ r_s^{out['p_vol']:.2f} (VOL={dim})")
        else:
            print("   --> LEVER ARM TOO SHORT (<0.7 decade): no exponent quoted (inconclusive)")
    else:
        print(f"   --> only {len(rows)} clean horizon runs: no fit")
    return out


if __name__ == '__main__':
    np.set_printoptions(precision=4, suppress=True)
    print("=" * 78)
    print("RELATIONAL NONLINEAR HORIZON v2 -- GR-III on a coordinate-free graph")
    print("=" * 78)
    print("\n### 3D coordinate-free graph (sparse; kappa swept a decade) ###", flush=True)
    r3 = run_case(dim=3, N=120000, mean_deg=8, sigma_hop=1.2, steps=6000,
                  kappas=[0.8, 1.6, 3.0, 5.5, 10.0, 18.0, 32.0], seed=7)
    print("\n### 2D control (area-exp should track d-1 = 1) ###", flush=True)
    r2 = run_case(dim=2, N=120000, mean_deg=6, sigma_hop=1.2, steps=6000,
                  kappas=[0.4, 0.8, 1.5, 2.8, 5.2, 9.5, 17.0], seed=7)

    print("\n" + "=" * 78)
    print("READ (graph-intrinsic; coords discarded):")
    for r in (r3, r2):
        d = r['dim']
        if 'p_area' in r:
            print(f"  {d}D: r_s~kappa^{r['p_rsM']:.2f} (mass=1); AREA r_s^{r['p_area']:.2f} "
                  f"(target {d-1}); VOL r_s^{r['p_vol']:.2f} (target {d}); "
                  f"lever {r['lever']:.2f} dec; def-slope {r['defslope']}")
        else:
            print(f"  {d}D: INCONCLUSIVE (lever/fit insufficient); def-slope {r['defslope']}")
    print("=" * 78)
