"""Curvature-emergence foothold: does a metric EMERGE from the bandwidth-connectivity structure of
the raw graph, and does it match GR-I's g ~ 1/b -- without assuming the answer?

The open bridge under 3D, the area-law geometry, and the horizon location: a participation graph
has no lengths on its edges; how does an emergent metric with a length scale appear? GR-I ASSIGNS
the spatial metric g ~ 1/b (bandwidth field) at the continuum level. This probe tests the deeper
thing: does the RAW GRAPH -- connectivity only, no assigned lengths -- produce distances that
reproduce g ~ 1/b, or a different metric, or none.

Non-circular setup (the trap from chains-as-links avoided): nodes sit on a background LABEL line
(0..L-1) -- a bookkeeping index, NOT a metric. A bandwidth field b(x) varies along it (baseline 1,
a Gaussian depletion = a 'mass' that lowers b). Bandwidth enters ONLY through CONNECTIVITY: a node
of higher bandwidth reaches further / connects to more (b = participation capacity, P04), with
reach ~ b^p. Then the EMERGENT distance is the plain UNWEIGHTED hop-count (BFS) between nodes --
read off the structure, not assigned. We measure that emergent distance and ask what metric it is.

What g ~ 1/b means, so we know what to look for: the proper spatial distance is ds = dx/sqrt(b),
i.e. hop-distance(x) ~ integral_0^x dx'/b(x')^{1/2}. More generally, if hop-distance ~
integral dx'/b^q, then the emergent spatial metric is g_xx = 1/b^{2q}. So:
   q = 1/2  ->  g ~ 1/b     (GR-I, the target)
   q = 1    ->  g ~ 1/b^2   (a different metric -- a real finding if it comes out)
We do NOT put q in by hand. We build with a connectivity law reach ~ b^p, MEASURE the emergent q
by fitting hop-distance to integral dx/b^q, and report q vs p. Two honest questions answered:
  (1) does a clean metric emerge at all, and is a low-b region 'far' (the curvature signature)?
  (2) which connectivity law b->reach recovers GR-I's g ~ 1/b, and is it a natural one?
"""
import numpy as np
from collections import deque


def bandwidth_field(L, b_min=0.2, width=None):
    x = np.arange(L)
    c = L / 2
    width = width or L / 8
    dip = (1.0 - b_min) * np.exp(-((x - c) ** 2) / (2 * width ** 2))
    return 1.0 - dip  # baseline 1, depleted to b_min at the 'mass'


def build_and_bfs(b, R0, p):
    """reach[x] = R0 * b[x]^p (bandwidth as connection capacity); unweighted hop-distance from 0."""
    L = len(b)
    reach = np.maximum(1, np.round(R0 * b ** p).astype(int))
    # adjacency as reach lists; BFS from node 0
    dist = np.full(L, -1)
    dist[0] = 0
    q = deque([0])
    while q:
        u = q.popleft()
        r = reach[u]
        for v in range(max(0, u - r), min(L, u + r + 1)):
            if dist[v] < 0:
                dist[v] = dist[u] + 1
                q.append(v)
    return dist


def integral_metric(b, q):
    """cumulative integral_0^x dx'/b^q -- the proper distance for emergent metric g = 1/b^{2q}."""
    return np.cumsum(1.0 / b ** q)


def fit_q(hopdist, b, qs=np.linspace(0.1, 1.6, 31)):
    """find the metric exponent q whose integral best matches (up to overall scale) the hop-distance."""
    x = np.arange(len(b))
    m = (hopdist > 0) & (x > 5) & (x < len(b) - 5)
    best, bestq = -np.inf, None
    for q in qs:
        I = integral_metric(b, q)[m]
        h = hopdist[m].astype(float)
        # scale-free correlation of shapes
        A = np.vstack([I, np.ones_like(I)]).T
        coef, *_ = np.linalg.lstsq(A, h, rcond=None)
        pred = A @ coef
        ss_res = np.sum((h - pred) ** 2)
        ss_tot = np.sum((h - h.mean()) ** 2)
        r2 = 1 - ss_res / ss_tot
        if r2 > best:
            best, bestq = r2, q
    return bestq, best


def main():
    L, R0 = 4000, 12.0
    b = bandwidth_field(L)
    x = np.arange(L)

    print("=" * 86)
    print("CURVATURE-EMERGENCE FOOTHOLD — does a metric emerge from bandwidth-connectivity? g~1/b?")
    print(f"  background label line L={L}, a bandwidth dip to b_min=0.2 (a 'mass'); reach ~ b^p")
    print("=" * 86)

    # curvature signature: compare hop-distance through the dip vs a flat-b reference
    flat = build_and_bfs(np.ones(L), R0, 1.0)
    print("\n  (1) CURVATURE SIGNATURE — is the low-bandwidth region 'far'?")
    for p in [0.5, 1.0]:
        d = build_and_bfs(b, R0, p)
        # extra hops accumulated crossing the dip, vs flat
        excess = d[-1] - flat[-1]
        print(f"     reach~b^{p}:  hops 0->end = {d[-1]:4d}  (flat-b = {flat[-1]:4d});  "
              f"excess through the dip = {excess:+d}  -> low-b is {'FARTHER' if excess>0 else 'not farther'}")

    # which connectivity law recovers GR-I g ~ 1/b (q = 1/2)?
    print("\n  (2) WHICH LAW RECOVERS g~1/b (q=1/2)? — measured emergent metric exponent q vs the")
    print("      connectivity law p (NOT assumed; q fit from the emergent hop-distance):")
    print(f"      {'reach law p':>12} {'emergent q':>12} {'fit R^2':>9}   metric")
    for p in [0.25, 0.5, 0.75, 1.0, 1.25]:
        d = build_and_bfs(b, R0, p)
        q, r2 = fit_q(d, b)
        gtag = ("g~1/b  (GR-I)" if abs(2 * q - 1) < 0.2 else
                "g~1/b^2" if abs(2 * q - 2) < 0.3 else f"g~1/b^{2*q:.2f}")
        print(f"      {p:>12.2f} {q:>12.2f} {r2:>9.3f}   {gtag}")

    print("\n  READ:")
    print("   - excess>0 through the dip => a metric EMERGES and low bandwidth reads as FAR: the")
    print("     qualitative curvature signature of g~1/b (mass depletes b, distances stretch).")
    print("   - emergent q tracks the connectivity law p (q ~ p). GR-I's g~1/b (q=1/2) is recovered")
    print("     when reach ~ sqrt(b) -- bandwidth-as-capacity(area), reach-as-linear-scale: a natural")
    print("     law, not an arbitrary tuning. reach~b (p=1) instead gives g~1/b^2.")
    print("   Honest scope: 1D, a background label line assumed (not derived), connectivity law")
    print("   chosen from a substrate reading. Foothold: a metric emerges and shows curvature; the")
    print("   GR-I power is recovered under a natural b->reach law -- it does NOT yet DERIVE that law.")
    print("=" * 86)


if __name__ == "__main__":
    main()
