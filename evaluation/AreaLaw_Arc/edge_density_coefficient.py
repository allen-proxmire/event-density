"""Edge-density coefficient: at the substrate's own scale, how many straddling cross-chain edges
sit per unit horizon area -- and does it reproduce the Planck-cell TILING (N = A/ell_P^2, Paper_025)?

Context (corrected). The Bekenstein-Hawking 1/4 is now DERIVED thermodynamically
(BH_Thermal2Pi_FromNearHorizonRindler: kappa=1/(2r_s) + the 2pi from the Rindler near-horizon
form, first law -> S=A/4). The area-law FORM is forced by the Planck tiling (Paper_025:
N = 4 pi R^2 / ell_ED^2 Planck cells at the horizon; Paper_043). So this probe is NOT trying to
re-derive the 1/4. It asks a third, independent question: does counting the straddling
entanglement (V5) edges at the substrate scale AGREE with the Planck tiling -- i.e. does it give
of order ONE bit per Planck cell (coefficient ~1, the tiling / holographic-bound-saturated
value), the same ballpark the frozen-state count gave earlier tonight (~0.78)?

Setup: a flat horizon (a plane; no curvature, so a clean density readout). Chain-loci at
substrate density rho (default 1 per unit Planck cell, P08). V5 edges within a reach ell
(default ~1 Planck length, its near-horizon value per Paper_039 tau_V5^BH ~ ell_P/c). Count, per
unit plane area:
  - C_edge  = straddling EDGES per area (pairs may share endpoints; raw edge count)
  - C_chain = straddling CHAINS per area (distinct loci with >=1 edge crossing; the bit-like count)
Sweep the reach ell to expose whether the coefficient is scale-free or scales with ell_V5 (if it
scales with ell_V5, the coefficient is inherited-through-the-reach, the honest caveat stated in
Paper_AreaLawIsTheEdgeCount). Compare both to 1 (Planck tiling) and 1/4 (Bekenstein-Hawking).

Could-say-no / honest reads:
  - C_chain ~ 1 per Planck cell at ell~1  -> edge-count REPRODUCES the Planck tiling; the 1/4 is
    the thermal factor on top (consistent with the frozen-count ~0.78 and the derived thermal 1/4).
  - C ~ 1/4 with a real reason -> a genuine third route to the coefficient (would be a surprise).
  - C scales with ell (no scale-free value) -> the coefficient is inherited via ell_V5, not a
    derivation; the tiling AGREEMENT (its ell~1 value) is still the content.
No new physics: finite-reach V5 (Paper_090) at its stated near-horizon scale.
"""
import numpy as np
from scipy.spatial import cKDTree


def measure(L, rho, reach, seed):
    N = int(rho * L**3)
    rng = np.random.default_rng(seed)
    pts = rng.uniform(0, L, size=(N, 3))
    tree = cKDTree(pts)
    pairs = tree.query_pairs(reach, output_type="ndarray")
    x = pts[:, 0]
    # plane at x = L/2, but only count in the central region to avoid box-edge effects on the
    # OTHER two axes -- restrict the plane-area denominator to a central window
    mid = L / 2.0
    stradd = (x[pairs[:, 0]] - mid) * (x[pairs[:, 1]] - mid) < 0  # opposite sides
    # keep only straddling edges whose crossing point is in the central (y,z) window
    m = 0.2 * L, 0.8 * L  # central 60% x 60% window
    yz0 = pts[pairs[stradd, 0]][:, 1:]
    yz1 = pts[pairs[stradd, 1]][:, 1:]
    yzc = 0.5 * (yz0 + yz1)
    inwin = np.all((yzc > m[0]) & (yzc < m[1]), axis=1)
    strad_edges = pairs[stradd][inwin]
    area = (0.6 * L) ** 2
    c_edge = len(strad_edges) / area
    c_chain = len(np.unique(strad_edges)) / area  # distinct loci with a crossing edge
    return c_edge, c_chain


def main():
    print("=" * 84)
    print("EDGE-DENSITY COEFFICIENT — straddling cross-chain edges per unit horizon area")
    print("  (substrate scale: rho=1 locus per Planck cell; compare to Planck tiling=1 and BH=1/4)")
    print("=" * 84)

    L, rho = 40.0, 1.0
    print(f"\n  reach ell   C_edge/area   C_chain/area   (C_chain vs tiling 1.0, vs BH 0.25)")
    print("  " + "-" * 70)
    rows = []
    for reach in [0.6, 0.8, 1.0, 1.3, 1.6, 2.0]:
        ce = np.mean([measure(L, rho, reach, s)[0] for s in range(1, 5)])
        cc = np.mean([measure(L, rho, reach, s)[1] for s in range(1, 5)])
        rows.append((reach, ce, cc))
        print(f"  {reach:6.2f}     {ce:9.3f}     {cc:9.3f}")

    reaches = np.array([r[0] for r in rows])
    cchain = np.array([r[2] for r in rows])
    cedge = np.array([r[1] for r in rows])
    p_chain = np.polyfit(np.log(reaches), np.log(cchain), 1)[0]
    p_edge = np.polyfit(np.log(reaches), np.log(cedge), 1)[0]
    print("  " + "-" * 70)
    print(f"\n  scaling with reach:  C_chain ~ ell^{p_chain:.2f}   C_edge ~ ell^{p_edge:.2f}")
    print(f"  C_chain at ell=1.0 (substrate near-horizon scale): {rows[2][2]:.3f}")
    print("\n  READ:")
    print("  - C_chain ~ 1 at ell~1  => the straddling-CHAIN count reproduces the Planck TILING")
    print("    (~1 bit per Planck cell); the 1/4 is the thermal factor on top (Thermal2Pi). Third")
    print("    route AGREES with Paper_025 tiling + the derived thermal 1/4.")
    print("  - C_chain ~ ell^1 (not flat) => coefficient is inherited via the V5 reach, not scale-")
    print("    free; the tiling agreement is at the substrate near-horizon reach ell~1.")
    print("  - anything landing on ~0.25 with a reason would be a genuine surprise, reported as such.")
    print("=" * 84)


if __name__ == "__main__":
    main()
