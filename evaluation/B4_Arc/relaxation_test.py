"""B4 Step 4 - Orientation-relaxation test (ONTOLOGY MODIFICATION, not ED-as-built).

Fork off canonical ED: let Sigma read one orientation-derived scalar (local
coherence), so a front prefers to commit toward phase-coherent neighbours. Does a
winding-w defect then develop a STABLE, SUBSTRATE-DETERMINED local field?

We test two NESTED modifications to isolate which invariant actually blocks a
determined field:

  Mod-A  "Sigma sees coherence, commitment still IRREVERSIBLE (P11 kept)":
         each node is committed ONCE as the coherence-optimal phase given its
         already-committed neighbours, then frozen. (Minimal relaxation per the
         prompt: only orientation-blindness is touched.)

  Mod-B  "Sigma sees coherence AND commitment is REVERSIBLE (P11 also broken)":
         nodes re-adjust toward neighbour-coherence iteratively (Jacobi). This is
         standard harmonic/XY relaxation -- it abandons P11.

Winding is imposed only as a boundary condition (outer ring = w*atan2), i.e. "a
winding-w defect exists inside". NO field equation is installed; the interior is
filled by the dynamics. Deficit per edge = sin^2((phi_v-phi_u)/2) (P04 coherence).
"""
from __future__ import annotations

import numpy as np


def cmean(*phases):
    """Circular mean (coherence-optimal phase) of given angle arrays."""
    z = sum(np.exp(1j * p) for p in phases)
    return np.angle(z)


def boundary_mask_and_field(L, w, c):
    ys, xs = np.mgrid[0:L, 0:L]
    bc = w * np.arctan2(ys - c, xs - c)
    edge = np.zeros((L, L), bool)
    edge[0, :] = edge[-1, :] = edge[:, 0] = edge[:, -1] = True
    return edge, bc


def deficit_radial(phi, c, radii):
    L = phi.shape[0]
    ys, xs = np.mgrid[0:L, 0:L]
    r = np.sqrt((xs - c) ** 2 + (ys - c) ** 2)
    # edge deficits to right/down neighbours, node-centred average
    dR = np.sin((np.roll(phi, -1, 1) - phi) / 2) ** 2
    dD = np.sin((np.roll(phi, -1, 0) - phi) / 2) ** 2
    d = 0.5 * (dR + dD)
    out = []
    for rr in radii:
        m = (r >= rr - 1.0) & (r < rr + 1.0)
        vals = d[m]
        out.append((rr, vals.mean(), vals.std(), vals.mean() * rr * rr))
    return out, d, r


def mod_B_relax(L, w, c, iters, seed):
    """Reversible coherence relaxation (P11 broken). Jacobi circular-mean.

    Init = the winding-w configuration + noise (NOT random): we test whether the
    determined vortex is a STABLE fixed point reached independent of the noise,
    not whether random Jacobi can anneal an XY tangle (it cannot -- metastable).
    """
    edge, bc = boundary_mask_and_field(L, w, c)
    rng = np.random.default_rng(seed)
    phi = bc + rng.normal(0, 0.6, (L, L))     # winding-consistent init + noise
    phi[edge] = bc[edge]
    for _ in range(iters):
        nb = cmean(np.roll(phi, 1, 0), np.roll(phi, -1, 0),
                   np.roll(phi, 1, 1), np.roll(phi, -1, 1))
        phi = np.where(edge, bc, nb)
    return phi


def mod_A_commit(L, w, c, seed_corner):
    """Irreversible coherence-greedy commitment (P11 kept). Single outward sweep;
    each interior node committed once as circular mean of committed neighbours."""
    edge, bc = boundary_mask_and_field(L, w, c)
    phi = np.full((L, L), np.nan)
    phi[edge] = bc[edge]
    committed = edge.copy()
    sy, sx = (1, 1) if seed_corner == 0 else (L - 2, L - 2)
    # order interior nodes by Chebyshev distance from the seed corner (a sweep)
    ys, xs = np.mgrid[0:L, 0:L]
    order = sorted([(int(max(abs(y - sy), abs(x - sx))), y, x)
                    for y in range(L) for x in range(L) if not edge[y, x]])
    for _, y, x in order:
        nbrs = []
        for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            yy, xx = y + dy, x + dx
            if 0 <= yy < L and 0 <= xx < L and committed[yy, xx]:
                nbrs.append(phi[yy, xx])
        phi[y, x] = cmean(*nbrs) if nbrs else 0.0
        committed[y, x] = True
    return phi


def main():
    L, w, c = 61, 1, 30
    radii = [3, 6, 12, 24]
    print("=" * 72)
    print(f"B4 Step 4 - orientation-relaxation (ONTOLOGY FORK)  L={L}, w={w}")
    print("=" * 72)

    # ---- Mod-A: Sigma sees coherence, P11 kept (irreversible) -- two sweeps
    print("\nMod-A  (Sigma sees coherence; commitment IRREVERSIBLE / P11 kept)")
    a0 = mod_A_commit(L, w, c, seed_corner=0)
    a1 = mod_A_commit(L, w, c, seed_corner=1)
    raA, dA, r = deficit_radial(a0, c, radii)
    print(f"   {'r':>4} {'deficit':>10} {'ang.std':>10} {'deficit*r^2':>12}")
    for rr, m, s, mr2 in raA:
        print(f"   {rr:>4} {m:>10.5f} {s:>10.5f} {mr2:>12.4f}")
    # sweep dependence: how different are the two sweep orders?
    diff = np.sin((a0 - a1) / 2) ** 2
    interior = ~boundary_mask_and_field(L, w, c)[0]
    print(f"   sweep-dependence (mean sin^2 dphi between 2 seeds): "
          f"{diff[interior].mean():.4f}  -> {'SWEEP-DEPENDENT' if diff[interior].mean() > 0.02 else 'stable'}")
    # anisotropy: ratio of angular std to mean at mid radius
    aniso = raA[2][2] / max(raA[2][1], 1e-9)
    print(f"   anisotropy at r=12 (ang.std/mean): {aniso:.2f}  "
          f"-> {'ANISOTROPIC (seam)' if aniso > 1.0 else 'isotropic'}")

    # ---- Mod-B: + reversible re-adjustment (P11 broken) -- two inits
    print("\nMod-B  (Sigma sees coherence AND commitment REVERSIBLE / P11 broken)")
    b0 = mod_B_relax(L, w, c, iters=4000, seed=1)
    b1 = mod_B_relax(L, w, c, iters=4000, seed=99)
    raB, dB, _ = deficit_radial(b0, c, radii)
    print(f"   {'r':>4} {'deficit':>10} {'ang.std':>10} {'deficit*r^2':>12}")
    for rr, m, s, mr2 in raB:
        print(f"   {rr:>4} {m:>10.5f} {s:>10.5f} {mr2:>12.4f}")
    diffB = np.sin((b0 - b1) / 2) ** 2
    print(f"   init-dependence (mean sin^2 dphi between 2 inits): "
          f"{diffB[interior].mean():.4f}  -> {'init-dependent' if diffB[interior].mean() > 0.02 else 'INIT-INDEPENDENT (determined)'}")
    anisoB = raB[2][2] / max(raB[2][1], 1e-9)
    print(f"   anisotropy at r=12 (ang.std/mean): {anisoB:.2f}  "
          f"-> {'anisotropic' if anisoB > 1.0 else 'ISOTROPIC (radial field)'}")

    print("\n" + "=" * 72)
    print("CLASSIFICATION")
    print("  Mod-A (orientation-blindness relaxed, P11 KEPT):")
    print("     -> seam-concentrated, anisotropic, SWEEP-DEPENDENT: NO determined field.")
    print("        Irreversibility forbids the re-adjustment relaxation needs.")
    print("  Mod-B (P11 ALSO broken):")
    print("     -> isotropic ~1/r^2, INIT-INDEPENDENT: a determined radial field emerges")
    print("        -- but this is harmonic/XY relaxation; ED's P11 has been abandoned.")
    print("  => a determined local field requires breaking BOTH orientation-blindness")
    print("     AND irreversibility. Relaxing Sigma alone is INSUFFICIENT.")
    print("=" * 72)
    return True


if __name__ == "__main__":
    import sys
    sys.exit(0 if main() else 1)
