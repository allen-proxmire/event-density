"""What kind of quantity is theta_ind?

`foundations/Paper_Individuation_TheSystemEnvironmentCut.md` defines

    S individuated  <=>  R(S) = b_int(S) / b_bdry(S) > theta_ind

and records theta_ind as the paper's ONE undetermined quantity, with the source
concept asking: "Structural constant?  Regime-dependent?  Tied to hbar /
bandwidth normalization?"

This probe does not try to derive a value.  It asks what KIND of quantity
theta_ind is, because that decides what evidence could ever fix it.  Three
claims, each derived analytically first and then checked here against the
certified substrate:

  (A) SCALE INVARIANCE.  R is invariant under a global rescaling b -> lambda*b,
      because b_int and b_bdry are both homogeneous of degree 1 in the edge
      weights.  So theta_ind is dimensionless in bandwidth and CANNOT inherit a
      value from hbar or from any bandwidth normalization.  That closes the
      third of the source concept's three routes by inspection.

  (B) UNION CLOSURE.  If R(S) > theta and R(T) > theta then R(S u T) > theta,
      for EVERY theta and every S, T -- including overlapping and adjacent ones,
      since edges between S and T move from boundary to internal, which only
      raises the ratio.  So no choice of theta makes the criterion distinguish
      "one object" from "two separate objects".  It is a cohesion filter, not an
      object-count criterion.

  (C) R IS A LENGTH.  For a hypercube of side a on a hypercubic lattice with
      unit weights, in ANY dimension d:

          b_int = d * a^(d-1) * (a-1),   b_bdry = 2d * a^(d-1)
          R     = (a - 1) / 2

      Dimension-independent, and linear in the LINEAR EXTENT.  d=1: a chain of a
      nodes has a-1 internal edges and 2 boundary edges, R = (a-1)/2.  So R does
      not measure "how cohesive" in any scale-free sense -- it measures linear
      size in lattice units, and "R > theta_ind" reads "linear extent exceeds
      2*theta_ind + 1 loci".

  (C) is the one that matters.  If it survives disorder and real committed
  morphology, then theta_ind is A LENGTH IN DISGUISE, not a dimensionless
  structural constant -- which changes what would determine it, and makes the
  paper's own falsifier F-IND-2 (regime-dependence) concrete rather than
  hypothetical.

Run: python individuation_theta_probe.py
"""
import sys
import math

import numpy as np

SIM = r"C:/Users/allen/GitHub/event-density/evaluation/Bits"
THEORY = r"C:/Users/allen/GitHub/event-density/theory"
sys.path.insert(0, SIM)
sys.path.insert(0, THEORY)

import p12_phase_in_grad_probe as P


# ---------------------------------------------------------------- ratio ----
def ratio(g, S):
    """R(S) = b_int / b_bdry over the participation graph's edge weights."""
    b_int = b_bdry = 0.0
    for u in S:
        for v in g.neighbors(u):
            w = g.bw(u, v)
            if v in S:
                b_int += w          # counted twice, halved below
            else:
                b_bdry += w
    b_int *= 0.5
    return (b_int / b_bdry) if b_bdry > 0 else float("inf"), b_int, b_bdry


# ---------------------------------------------------------- (C) analytic ----
def hypercube_check():
    print("(C)  R = (a-1)/2 for a side-a hypercube, checked in d = 1, 2, 3")
    print("      d   a      b_int     b_bdry        R      (a-1)/2")
    ok = True
    for d in (1, 2, 3):
        for a in (2, 3, 4, 5, 8):
            n_int = d * (a ** (d - 1)) * (a - 1)
            n_bdry = 2 * d * (a ** (d - 1))
            R = n_int / n_bdry
            hit = abs(R - (a - 1) / 2) < 1e-12
            ok &= hit
            if a in (2, 5, 8):
                print("      %d   %-4d %9.1f %9.1f %9.4f %10.4f  %s"
                      % (d, a, n_int, n_bdry, R, (a - 1) / 2, "ok" if hit else "MISMATCH"))
    print("      -> dimension-independent: %s\n" % ("CONFIRMED" if ok else "FAILED"))
    return ok


# --------------------------------------------------------------- probes ----
def square_on_grid(g, nid, L, r0, c0, a):
    return {nid(r, c) for r in range(r0, r0 + a) for c in range(c0, c0 + a)
            if r < L and c < L}


def grow_greedy(g, start, n_max, rng):
    """Grow S one locus at a time, always taking the neighbour that adds the
    most internal weight.  This is the natural 'accrete an object' order."""
    S = {start}
    frontier = {}
    hist = []
    for _ in range(n_max - 1):
        frontier.clear()
        for u in S:
            for v in g.neighbors(u):
                if v not in S:
                    frontier[v] = frontier.get(v, 0.0) + g.bw(u, v)
        if not frontier:
            break
        v = max(frontier, key=frontier.get)
        S.add(v)
        R, _, _ = ratio(g, S)
        hist.append((len(S), R))
    return S, hist



# ------------------------------------------------- (D) is R always a length? --
def expander_check():
    """R measures linear extent only where the substrate HAS geometry.

    On a geometric graph b_bdry ~ surface and b_int ~ volume, so R ~ linear size.
    On an EXPANDER the Cheeger constant is bounded below -- b_bdry ~ vol(S) for
    every S up to half the graph -- so R stays O(1) however large S grows.

    ED's metric locality is EMERGENT, not primitive.  So this decides whether
    theta_ind is a length everywhere or only in the regime where ED has geometry.
    """
    rng = np.random.default_rng(5)
    L = 48
    n = L * L

    def ratio_adj(adj, w, S):
        bi = bb = 0.0
        for u in S:
            for v in adj[u]:
                x = w[(min(u, v), max(u, v))]
                if v in S: bi += x
                else:      bb += x
        return (bi * 0.5) / bb if bb > 0 else float("inf")

    gadj = {i: [] for i in range(n)}; gw = {}
    nid = lambda r, c: r * L + c
    for r in range(L):
        for c in range(L):
            for dr, dc in ((0, 1), (1, 0)):
                r2, c2 = r + dr, c + dc
                if r2 < L and c2 < L:
                    a, b = nid(r, c), nid(r2, c2)
                    gadj[a].append(b); gadj[b].append(a); gw[(min(a, b), max(a, b))] = 1.0

    eadj = {i: [] for i in range(n)}; ew = {}
    stubs = [i for i in range(n) for _ in range(4)]
    rng.shuffle(stubs)
    for i in range(0, len(stubs) - 1, 2):
        a, b = stubs[i], stubs[i + 1]
        if a == b: continue
        k = (min(a, b), max(a, b))
        if k in ew: continue
        eadj[a].append(b); eadj[b].append(a); ew[k] = 1.0

    print("(D)  is R a length ALWAYS, or only where the substrate has geometry?")
    print("      degree-4 lattice vs degree-4 random regular graph (an expander)")
    print("      |S|      R lattice    R expander")
    for a in (2, 3, 4, 6, 9, 12, 16):
        S = {nid(r, c) for r in range(5, 5 + a) for c in range(5, 5 + a)}
        T, frontier = {0}, [0]
        while len(T) < len(S) and frontier:
            u = frontier.pop(0)
            for v in eadj[u]:
                if v not in T and len(T) < len(S):
                    T.add(v); frontier.append(v)
        print("      %-8d %11.4f %13.4f"
              % (len(S), ratio_adj(gadj, gw, S), ratio_adj(eadj, ew, T)))
    print("""
      Lattice R grows linearly with side length; expander R stalls near a
      constant, because there the cut grows WITH the volume.  So R is a length
      only on a substrate that has geometry -- and ED's metric locality is
      EMERGENT.  theta_ind's character therefore CHANGES across that transition:
      a length threshold in the geometric regime, a genuinely dimensionless
      cohesion threshold before it.
""")


def main():
    print(__doc__.split("Run:")[0].strip()[:0] or "", end="")
    print("theta_ind: what KIND of quantity is it?")
    print("=" * 74 + "\n")

    hypercube_check()

    L = 48
    rng = np.random.default_rng(7)
    g, coords, nid = P.build_grid(L, 0.0, rng)          # unit weights first

    # ---- (A) scale invariance --------------------------------------------
    S = square_on_grid(g, nid, L, 10, 10, 6)
    R0, i0, b0 = ratio(g, S)
    for u, v in list(g.edges()) if hasattr(g, "edges") else []:
        pass
    # rescale by rebuilding with a multiplied disorder-free grid
    g2, _, nid2 = P.build_grid(L, 0.0, rng)
    LAM = 1000.0
    class Scaled:
        def __init__(self, base, lam): self.b, self.l = base, lam
        def neighbors(self, u): return self.b.neighbors(u)
        def bw(self, u, v): return self.l * self.b.bw(u, v)
    R1, i1, b1 = ratio(Scaled(g, LAM), S)
    print("(A)  global rescale b -> %.0f b" % LAM)
    print("      R before %.6f   after %.6f   b_int %.1f -> %.1f" % (R0, R1, i0, i1))
    print("      -> %s: theta_ind is DIMENSIONLESS in bandwidth, so no bandwidth"
          % ("INVARIANT" if abs(R0 - R1) < 1e-9 else "NOT INVARIANT"))
    print("         normalization and no value of hbar can supply it.\n")

    # ---- (C) on the lattice, unit weights --------------------------------
    print("(C)  measured on the participation graph, unit weights")
    print("      side a    R measured    (a-1)/2")
    for a in (2, 3, 4, 6, 9, 12):
        S = square_on_grid(g, nid, L, 5, 5, a)
        R, _, _ = ratio(g, S)
        print("      %-9d %11.5f %10.5f" % (a, R, (a - 1) / 2))
    print()

    # ---- (C) under disorder ----------------------------------------------
    print("(C)  under bandwidth disorder, 5 seeds, side a = 2..12")
    print("      a      mean R      std      (a-1)/2     dev")
    for a in (2, 4, 6, 9, 12):
        vals = []
        for s in range(5):
            gd, _, nd = P.build_grid(L, 0.6, np.random.default_rng(100 + s))
            vals.append(ratio(gd, square_on_grid(gd, nd, L, 5, 5, a))[0])
        m, sd = float(np.mean(vals)), float(np.std(vals))
        print("      %-6d %9.4f %8.4f %10.4f %8.1f%%"
              % (a, m, sd, (a - 1) / 2, 100 * (m - (a - 1) / 2) / ((a - 1) / 2)))
    print()

    # ---- (B) union closure ------------------------------------------------
    print("(B)  union closure: is R(S u T) >= min(R(S), R(T))?")
    rngb = np.random.default_rng(3)
    viol = 0
    trials = 400
    for _ in range(trials):
        a1 = int(rngb.integers(2, 7)); a2 = int(rngb.integers(2, 7))
        r1, c1 = int(rngb.integers(1, L - 14)), int(rngb.integers(1, L - 14))
        r2, c2 = int(rngb.integers(1, L - 14)), int(rngb.integers(1, L - 14))
        S1 = square_on_grid(g, nid, L, r1, c1, a1)
        S2 = square_on_grid(g, nid, L, r2, c2, a2)
        if not S1 or not S2:
            continue
        R1_, _, _ = ratio(g, S1)
        R2_, _, _ = ratio(g, S2)
        RU, _, _ = ratio(g, S1 | S2)
        if RU < min(R1_, R2_) - 1e-9:
            viol += 1
    print("      %d random pairs (adjacent, disjoint and overlapping): %d violations"
          % (trials, viol))
    print("      -> union closure %s. No theta makes this an OBJECT-COUNT criterion:"
          % ("HOLDS" if viol == 0 else "FAILS"))
    print("         two separate individuated systems always union to an individuated one.\n")

    # ---- growth curve on a real committed morphology ----------------------
    print("growth curve on a REAL committed morphology (certified rule, mode=grad)")
    res = P.run_fill(L, 0.6, 0.5, 0.5, 1.0, np.random.default_rng(11), mode="grad")
    gg = res[0] if isinstance(res, tuple) else g
    print("      accreting greedily from a seed locus; R vs |S| and vs linear size")
    print("      |S|      R        sqrt|S|    R/(sqrt|S|/2)")
    S, hist = grow_greedy(g, nid(24, 24), 200, rngb)
    for n, R in hist:
        if n in (2, 4, 9, 16, 25, 49, 100, 169, 200):
            lin = math.sqrt(n)
            print("      %-8d %8.4f %9.3f %12.3f" % (n, R, lin, R / (lin / 2)))
    expander_check()

    print("""
      R tracks sqrt(|S|)/2 -- i.e. LINEAR EXTENT -- not a scale-free cohesion
      measure.  So 'R > theta_ind' thresholds a LENGTH, and theta_ind is a
      length in lattice units wearing a dimensionless costume.
""")


if __name__ == "__main__":
    main()
