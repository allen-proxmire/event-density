"""Spectral-dimension poke on the EXISTING curvature-emergence arena.

Graph construction is copied verbatim in spirit from
  event-density/evaluation/CurvatureEmergence/isotropy_3d_probe.py :: build_graph_bfs
(bandwidth enters ONLY through connectivity: reach ~ b^p; nodes connect to lattice
neighbours within their Euclidean reach). Nothing about the substrate is changed.

Question: does the spectral dimension d_s of that graph RUN with scale, or sit flat at 3?

Method (no dynamics required -- pure connectivity):
  lazy random walk W = (I + D^-1 A)/2 on the symmetrised graph
  return probability P(t) = Tr(W^t)/N, via Rademacher stochastic trace estimation
  d_s(t) = -2 dlog P / dlog t

Controls:
  (a) b_min = 1.0  -> NO mass, uniform reach = a regular lattice graph. Must give d_s ~ 3.
      If this control fails, the measurement is broken and nothing else is readable.
  (b) b_min = 0.2  -> the 'point mass' arena the isotropy probe actually uses.
"""
import numpy as np
from scipy.sparse import coo_matrix, identity, diags


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


def build_graph(side, R0, p, b_min):
    """Adjacency only -- the isotropy probe's construction, returning G instead of BFS distances."""
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
    data = np.ones(len(rows), dtype=np.float32)
    G = coo_matrix((data, (rows, cols)), shape=(N, N)).tocsr()
    G = G.maximum(G.T)            # symmetrise: reach is asymmetric, walks want undirected
    return G, b.ravel(), N


def return_probability(G, N, tmax, nprobe=12, seed=0):
    """P(t) = Tr(W^t)/N for the LAZY walk W = (I + D^-1 A)/2, Rademacher trace estimator."""
    deg = np.asarray(G.sum(axis=1)).ravel()
    deg[deg == 0] = 1.0
    Dinv = diags(1.0 / deg)
    P = (Dinv @ G).astype(np.float32)
    I = identity(N, format="csr", dtype=np.float32)
    W = (0.5 * (I + P)).tocsr()

    rng = np.random.default_rng(seed)
    Z = rng.choice([-1.0, 1.0], size=(N, nprobe)).astype(np.float32)
    V = Z.copy()
    out = np.zeros(tmax + 1)
    for t in range(1, tmax + 1):
        V = W @ V
        out[t] = float((Z * V).sum() / (nprobe * N))
    return out


def spectral_dim(Pt, lo, hi):
    """d_s = -2 dlogP/dlogt, least-squares slope over the window [lo,hi]."""
    t = np.arange(lo, hi + 1)
    y = np.log(Pt[lo:hi + 1])
    x = np.log(t)
    A = np.vstack([x, np.ones_like(x)]).T
    slope = np.linalg.lstsq(A, y, rcond=None)[0][0]
    return -2.0 * slope


def run(label, side, R0, p, b_min, tmax=40):
    G, b, N = build_graph(side, R0, p, b_min)
    nnz = G.nnz
    Pt = return_probability(G, N, tmax)
    print(f"\n--- {label} ---")
    print(f"  {side}^3 = {N} loci, R0={R0}, reach~b^{p}, b_min={b_min}")
    print(f"  edges (symmetrised): {nnz}, mean degree {nnz/N:.1f}")
    print(f"  {'t':>4} {'P(t)':>12} {'d_s(local)':>12}")
    for t in [2, 3, 4, 6, 8, 11, 15, 20, 27, 35]:
        if t + 1 > tmax:
            continue
        ds = -2 * (np.log(Pt[t + 1]) - np.log(Pt[t - 1])) / (np.log(t + 1) - np.log(t - 1))
        print(f"  {t:>4} {Pt[t]:>12.6f} {ds:>12.3f}")
    for (lo, hi) in [(3, 8), (8, 18), (15, 30)]:
        if hi <= tmax:
            print(f"  fitted d_s over t=[{lo},{hi}]: {spectral_dim(Pt, lo, hi):.3f}")
    return Pt


if __name__ == "__main__":
    print("Spectral dimension on the existing curvature-emergence arena")
    print("(graph construction unchanged from isotropy_3d_probe.build_graph_bfs)")
    # METHOD CHECK first: nearest-neighbour graph, where d_s MUST be 3.
    # This is the run the scoping note cites as validating the measurement (d_s ~ 3.10).
    run("METHOD CHECK: R0=1.0 nearest-neighbour, uniform -- must read ~3", side=81, R0=1.0, p=0.5, b_min=1.0, tmax=60)
    run("CONTROL: uniform bandwidth at arena settings (b_min=1.0) -- FAILS, see note S3", side=61, R0=2.0, p=0.5, b_min=1.0)
    run("ARENA: point mass (b_min=0.2) -- the isotropy probe's setup", side=61, R0=2.0, p=0.5, b_min=0.2)
    run("ARENA: deeper mass (b_min=0.05)", side=61, R0=2.0, p=0.5, b_min=0.05)

    print("")
    print("--- COUPLING FLOOR: does bandwidth reach connectivity at all? ---")
    print("  reach = max(1, round(R0 * b^p)) is INTEGER, and b <= 1, so small R0 cannot resolve b.")
    for R0 in [1.0, 2.0, 4.0]:
        G1, _, N = build_graph(31, R0, 0.5, 1.0)
        G2, _, _ = build_graph(31, R0, 0.5, 0.05)
        print(f"  R0={R0}: mass changes {100*(1-G2.nnz/G1.nnz):5.2f}% of edges")
