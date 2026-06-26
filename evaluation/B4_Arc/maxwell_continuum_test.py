"""B4 / #2 — does ED's COARSE-GRAINING select the Maxwell/Coulomb field?

The B4 charge paper (§7) leaves one open question: a single ED-as-built commit
(orientation-blind Σ, P11 kept / irreversible) gives a sweep-dependent ANISOTROPIC
SEAM — no determined local field per config. But in lattice gauge theory the
determined field is the gauge-invariant EXPECTATION of the link variables across
the ensemble. The per-edge config is gauge-redundant; the seam sits in a DIFFERENT
place for each commit order. So the ED-native question is:

  does the ENSEMBLE-AVERAGE of the ED-as-built configs (P11 kept) converge to the
  isotropic Coulomb 1/r^2 (= the Maxwell-action minimizer), or stay anisotropic /
  non-1/r^2 ?

  -> averages to 1/r^2 : Maxwell emerges as the coarse-grained limit (§7 hope; the
     seams are gauge, washing out). A positive result for #2.
  -> stays anisotropic : ED's coarse-graining does NOT select Maxwell -- the same
     committal/trapping wall that blocked diffusion (#3) and Gaussianity (#5c).

Prior (committal/trapping, #5c non-Gaussian): be skeptical of a clean Maxwell.
BUT the commit-to-coherent-mean is a harmonic-like operation (unlike the ballistic
deposit dynamics of #5c), so it MIGHT coarse-grain to harmonic/Coulomb. Genuinely
open -- could-say-no.

Target (the Maxwell answer): Mod-B XY relaxation gives isotropic deficit*r^2 ~ 0.126
(B4 §5). The test is whether the ED-as-built ENSEMBLE-AVERAGE reaches that, WITHOUT
breaking P11.
"""
from __future__ import annotations
import heapq
import numpy as np

from relaxation_test import cmean, boundary_mask_and_field, deficit_radial, mod_B_relax


def randomized_commit(L, w, c, seed):
    """ED-as-built (orientation-blind Σ relaxed, P11 KEPT / irreversible) with a
    RANDOM commit order: a random-order flood from the boundary inward; each interior
    node is committed ONCE to the circular mean of its already-committed neighbours.
    Different seeds = different gauge-redundant configs (same loop holonomies = 2*pi*w)."""
    edge, bc = boundary_mask_and_field(L, w, c)
    rng = np.random.default_rng(seed)
    phi = np.where(edge, bc, 0.0).astype(float)
    committed = edge.copy()
    heap = []
    # seed the frontier: interior nodes adjacent to the boundary
    for y in range(L):
        for x in range(L):
            if edge[y, x]:
                continue
            if any(0 <= y+dy < L and 0 <= x+dx < L and edge[y+dy, x+dx]
                   for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1))):
                heapq.heappush(heap, (rng.random(), y, x))
    seen = committed.copy()
    while heap:
        _, y, x = heapq.heappop(heap)
        if committed[y, x]:
            continue
        nbrs = [phi[y+dy, x+dx] for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1))
                if 0 <= y+dy < L and 0 <= x+dx < L and committed[y+dy, x+dx]]
        phi[y, x] = cmean(*nbrs) if nbrs else 0.0
        committed[y, x] = True
        for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            yy, xx = y+dy, x+dx
            if 0 <= yy < L and 0 <= xx < L and not committed[yy, xx] and not seen[yy, xx]:
                heapq.heappush(heap, (rng.random(), yy, xx))
                seen[yy, xx] = True
    return phi


def deficit_field(phi):
    dR = np.sin((np.roll(phi, -1, 1) - phi) / 2) ** 2
    dD = np.sin((np.roll(phi, -1, 0) - phi) / 2) ** 2
    return 0.5 * (dR + dD)


def radial(dfield, c, radii):
    L = dfield.shape[0]
    ys, xs = np.mgrid[0:L, 0:L]
    r = np.sqrt((xs - c) ** 2 + (ys - c) ** 2)
    out = []
    for rr in radii:
        m = (r >= rr - 1.0) & (r < rr + 1.0)
        v = dfield[m]
        out.append((rr, v.mean(), v.std(), v.mean() * rr * rr))
    return out


def main():
    L, w, c = 61, 1, 30
    radii = [3, 6, 12, 24]
    print("=" * 78)
    print(f"B4 / #2 — does the ED-as-built ENSEMBLE coarse-grain to Maxwell/Coulomb?  L={L}, w={w}")
    print("=" * 78)

    # Maxwell target: Mod-B (XY relaxation, P11 broken) — the action minimizer
    bM = mod_B_relax(L, w, c, iters=4000, seed=1)
    raM = radial(deficit_field(bM), c, radii)
    print("\n[target]  Mod-B XY relaxation (P11 BROKEN) = the Maxwell-action minimizer:")
    print(f"   {'r':>4} {'deficit':>10} {'ang.std':>10} {'deficit*r^2':>12}")
    for rr, m, s, mr2 in raM:
        print(f"   {rr:>4} {m:>10.5f} {s:>10.5f} {mr2:>12.4f}")
    print("   (isotropic, deficit*r^2 ~ const = Coulomb 1/r^2)")

    # the test: ENSEMBLE-AVERAGE of ED-as-built (P11 KEPT), random commit orders
    print("\n[test]  ED-as-built ensemble (orientation-blind, P11 KEPT), random commit orders:")
    for Nens in (1, 8, 32, 128):
        acc = np.zeros((L, L))
        for s in range(Nens):
            acc += deficit_field(randomized_commit(L, w, c, seed=1000 + s))
        acc /= Nens
        ra = radial(acc, c, radii)
        # isotropy at r=12: angular spread of <d> relative to mean
        L_, = (L,)
        ys, xs = np.mgrid[0:L, 0:L]
        rr_ = np.sqrt((xs - c) ** 2 + (ys - c) ** 2)
        ring = (rr_ >= 11) & (rr_ < 13)
        iso = acc[ring].std() / max(acc[ring].mean(), 1e-12)
        mr2_flat = np.std([t[3] for t in ra]) / max(np.mean([t[3] for t in ra]), 1e-12)
        print(f"   N={Nens:>4}: deficit*r^2 = [" +
              " ".join(f"{t[3]:.3f}" for t in ra) +
              f"]  flatness(cv)={mr2_flat:.2f}  iso(cv@r12)={iso:.2f}")

    print("\n" + "-" * 78)
    print("READ:")
    print("  - deficit*r^2 FLAT across r (cv small) AND iso small  -> converges to Coulomb")
    print("    1/r^2: Maxwell EMERGES as the coarse-grained/ensemble limit WITHOUT breaking")
    print("    P11 (the §7 hope; per-config seams are gauge, washed out).")
    print("  - deficit*r^2 NOT flat, or iso stays large  -> ED's coarse-graining does NOT")
    print("    select Maxwell: the committal/trapping wall (cf. #3 diffusion, #5c Gaussianity).")
    print("  Compare the ensemble deficit*r^2 to the Mod-B target above.")
    print("-" * 78)
    return True


if __name__ == "__main__":
    import sys
    sys.exit(0 if main() else 1)
