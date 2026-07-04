"""Straddling-edge / area-law probe: is a surface's entropy just the count of V5 cross-chain
(entanglement) edges that pierce it, and does that count reproduce the MEASURED area law S ~ A?

Idea (LengthInED_FreeWrite): in ED, distance is an emergent shadow read off bandwidth; the V5
cross-chain correlation kernel (Paper_090) is the SAME substrate object carrying entanglement and
the BH interior/exterior connection (the ER=EPR echo, Paper_071). Entanglement across a surface is
carried by V5 edges that straddle it (Paper_039 sec.3.5). So: draw a surface, count the V5 edges
with one endpoint inside and one outside, and ask whether that count scales as the surface's AREA
(r^2) or its VOLUME (r^3).

The physics this tests, stated before running:
  - SHORT-RANGE V5 (finite reach ell_V5, most correlations local): only edges within ~ell of the
    surface can straddle it, so the straddling count ~ (surface area) x (shell thickness ell) x
    (edge density) ~ r^2. THE AREA LAW. This is the standard entanglement-area-law mechanism
    (local/gapped systems entangle only across the boundary) told in ED's own graph language.
  - FULLY LONG-RANGE V5 (any pair linked regardless of distance): edges from deep inside reach
    outside, straddling ~ (points inside) x (points outside) ~ r^3 for small r. VOLUME LAW.
  - MIXED (dominantly short-range + a sparse long tail): area law survives while the short-range
    part dominates; the sparse long links are the ER=EPR "wormhole" edges (a single pair at
    arbitrary emergent distance) and do not, if sparse, spoil the bulk area scaling.

Could-say-no: if short-range V5 gives r^3 (volume) not r^2 (area), the "surface entropy = straddling
edge count" identification is wrong and the area law is NOT the straddling-edge count. Honest either
way. Controls: points-inside(r) must scale r^3 (confirms geometry), a sphere-surface area ~ r^2.

Also connects to the chains-as-links result (2026-07-01): there, coupling LOCALITY did not matter
for the K6 topological-minor (linking) structure. Here, locality is expected to matter decisively
for the GEOMETRIC area law. If both hold, entanglement's TOPOLOGY (can it link -> 3D) is
locality-independent while its GEOMETRY (area law) is locality-dependent -- two different faces.

No new physics: V5 is modeled at its stated character (a finite-reach pairwise cross-chain kernel,
Paper_090). Reach and long-range fraction are swept, not tuned to an answer.
"""
import numpy as np
from scipy.spatial import cKDTree


def build_points(N, L, seed):
    rng = np.random.default_rng(seed)
    return rng.uniform(0.0, L, size=(N, 3))


def short_range_edges(pts, reach):
    """V5 edges between all chain-loci pairs within `reach` (finite-reach cross-chain kernel)."""
    tree = cKDTree(pts)
    return tree.query_pairs(reach, output_type="ndarray")


def long_range_edges(pts, n_edges, rng):
    """A sparse tail of distance-independent V5 links (the ER=EPR 'wormhole' edges)."""
    N = len(pts)
    a = rng.integers(0, N, size=n_edges)
    b = rng.integers(0, N, size=n_edges)
    keep = a != b
    return np.stack([a[keep], b[keep]], axis=1)


def straddle_count(pts, edges, center, r):
    d = np.linalg.norm(pts - center, axis=1)
    inside = d < r
    return int(np.sum(inside[edges[:, 0]] != inside[edges[:, 1]]))


def points_inside(pts, center, r):
    return int(np.sum(np.linalg.norm(pts - center, axis=1) < r))


def slope(rs, ys):
    rs, ys = np.asarray(rs, float), np.asarray(ys, float)
    m = ys > 0
    return np.polyfit(np.log(rs[m]), np.log(ys[m]), 1)[0]


def run_case(label, pts, edges, center, radii):
    strad = [straddle_count(pts, edges, center, r) for r in radii]
    p = slope(radii, strad)
    tag = ("AREA law (r^2)" if abs(p - 2) < 0.35 else
           "VOLUME law (r^3)" if abs(p - 3) < 0.35 else
           f"neither (p={p:.2f})")
    print(f"  {label:34s} edges={len(edges):8d}  straddle~r^{p:.2f}   -> {tag}")
    return p, strad


def main():
    L, N = 100.0, 40000
    center = np.array([L / 2] * 3)
    radii = np.linspace(16, 40, 13)
    pts = build_points(N, L, seed=1)
    rng = np.random.default_rng(7)

    print("=" * 90)
    print("STRADDLING-EDGE AREA-LAW PROBE — do V5 edges piercing a surface count like its AREA?")
    print(f"  {N} chain-loci in a {L:.0f}^3 box; sphere-surface swept r=16..40 (well inside box)")
    print("=" * 90)

    # geometry controls
    pin = [points_inside(pts, center, r) for r in radii]
    print(f"\n  CONTROL  points-inside ~ r^{slope(radii, pin):.2f}   (must be ~3.00: confirms 3D geometry)")
    print(f"  CONTROL  a sphere's area ~ r^2.00, its volume ~ r^3.00  (the two hypotheses)\n")

    # (A) pure short-range V5 at several reaches
    print("(A) SHORT-RANGE V5 only (finite reach; expect AREA law r^2):")
    for reach in [4.0, 6.0, 9.0]:
        e = short_range_edges(pts, reach)
        run_case(f"reach={reach}", pts, e, center, radii)

    # (B) fully long-range V5 (distance-independent; expect VOLUME law r^3)
    print("\n(B) FULLY LONG-RANGE V5 (distance-independent links; expect VOLUME law r^3):")
    base = short_range_edges(pts, 6.0)
    e_long = long_range_edges(pts, n_edges=len(base), rng=rng)
    run_case("random pairs, any distance", pts, e_long, center, radii)

    # (C) mixed: short-range bulk + a sparse long tail (the ER=EPR wormhole edges)
    print("\n(C) MIXED: short-range bulk (reach=6) + a sparse long-range tail (expect AREA survives):")
    for frac in [0.0, 0.02, 0.10, 0.30, 1.0]:
        tail = long_range_edges(pts, n_edges=int(frac * len(base)), rng=rng) if frac > 0 else np.empty((0, 2), int)
        e_mix = np.vstack([base, tail]) if len(tail) else base
        run_case(f"long-tail fraction={frac:.2f}", pts, e_mix, center, radii)

    print("\n" + "=" * 90)
    print("READ: (A) short-range -> r^2 confirms 'surface entropy = straddling-edge count' gives the")
    print("AREA LAW. (B) fully long-range -> r^3 is the could-say-no (would break the identification).")
    print("(C) shows how much long-range tail the area law tolerates before volume-law creeps in.")
    print("=" * 90)


if __name__ == "__main__":
    main()
