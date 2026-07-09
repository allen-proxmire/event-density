"""Verify kappa_h on the REAL V5 coherence coupling (not the Probe-1 docking caricature).

Probe 1 modeled the coupling as a proper-rotation docking search and got kappa_h>0. The
load-bearing caveat: if ED's actual V5 coupling is PURELY PHASE-BASED (independent of
geometric alignment), kappa_h could collapse to 0. This probe uses the genuine V5
coherence functional and DECOMPOSES the result to see where (if anywhere) kappa_h lives.

REAL V5 COUPLING between two composites A, B (each = 4 chains with positions + P09 phases):
    E(R) = sum_{i in A, j in B} w(|r^A_i - R r^B_j|) * cos(phi^A_i - phi^B_j)
  * w(r) = exp(-r/ell_V5): V5's DEFINING finite reach (proximity). No vertex hand-matching;
    every cross-pair contributes, reach-weighted. This is the actual coherence functional.
  * phases phi are each composite's INTERNAL committed texture (P11: frozen), derived from
    a PARITY-EVEN rule (distance-based), so nothing handed is put in by hand.
  * physical binding = relax B's orientation (PROPER rotations only) to maximize coherence.
    coherence(A,B) = max_R E(R).

DECOMPOSITION (the honest test of the caveat):
  * FULL     : w=exp(-r/ell), phase=cos(dphi)   -- the real V5 coupling
  * PHASE-ONLY: w=1 (no reach),  phase=cos(dphi) -- "purely phase-based" -> expect kappa_h~0
  * PROX-ONLY : w=exp(-r/ell),   phase=1         -- pure steric/reach -> where kappa_h should live

kappa_h = coherence(same-handed) - coherence(opposite-handed), averaged over chiral
templates; achiral control must give kappa_h~0.
"""
import numpy as np
from scipy.spatial.transform import Rotation

MIRROR = np.diag([-1.0, 1.0, 1.0])
ELL = 1.0
SEP = 1.3          # centroid separation of the two composites (adjacent, interacting)
NROT = 400         # proper-rotation samples for the binding relaxation


def vertex_phases(T):
    n = len(T); phi = np.zeros(n)
    for i in range(n):
        phi[i] = sum(1.0 / np.linalg.norm(T[i] - T[j]) for j in range(n) if j != i) % (2*np.pi)
    return phi


def random_template(rng, chiral=True):
    while True:
        T = rng.normal(size=(4, 3)); T -= T.mean(0)
        T /= np.sqrt(np.mean(np.sum(T**2, axis=1)))
        vol = np.linalg.det(np.stack([T[1]-T[0], T[2]-T[0], T[3]-T[0]]))
        if chiral and abs(vol) > 0.3:
            return T @ MIRROR if vol < 0 else T
        if not chiral and abs(vol) < 0.05:
            return T


def coherence(A, phiA, B, phiB, rots, mode="full"):
    """max over proper rotations of the V5 coherence functional between A and B."""
    A = A - A.mean(0)
    B = B - B.mean(0)
    offset = np.array([SEP, 0.0, 0.0])
    best = -np.inf
    dphi = phiA[:, None] - phiB[None, :]                 # (4,4)
    phase = np.cos(dphi) if mode != "prox" else np.ones_like(dphi)
    for R in rots:
        Br = B @ R.T + offset
        d = np.linalg.norm(A[:, None, :] - Br[None, :, :], axis=2)   # (4,4)
        w = np.exp(-d / ELL) if mode != "phase" else np.ones_like(d)
        best = max(best, float(np.sum(w * phase)))
    return best


def main():
    rng = np.random.default_rng(5)
    rots = Rotation.random(NROT, random_state=7).as_matrix()   # uniform proper rotations
    print(f"REAL V5 coupling: E = sum_ij exp(-r_ij/ell)*cos(dphi_ij), ell={ELL}, sep={SEP}.")
    print("Composites relax orientation (proper rotations) to max coherence. Decomposed.\n")

    def kappa_set(templates, tag):
        rows = {"full": [], "phase": [], "prox": []}
        for T in templates:
            phi = vertex_phases(T)
            Tm = T @ MIRROR                                # enantiomer (same phases: distances preserved)
            for mode in rows:
                c_same = coherence(T, phi, T, phi, rots, mode)      # same handedness
                c_opp = coherence(T, phi, Tm, phi, rots, mode)      # opposite handedness
                rows[mode].append(c_same - c_opp)
        print(f"=== {tag} ===")
        for mode in ("full", "phase", "prox"):
            arr = np.array(rows[mode])
            print(f"  {mode:6s}: kappa_h mean={arr.mean():+.3f}  (per-template: "
                  + " ".join(f"{v:+.2f}" for v in arr) + ")")
        return rows

    chiral = [random_template(rng, True) for _ in range(8)]
    achiral = [random_template(rng, False) for _ in range(6)]
    kc = kappa_set(chiral, "CHIRAL templates")
    print()
    ka = kappa_set(achiral, "ACHIRAL control")

    print("\n" + "=" * 90)
    print("READ:")
    fm = np.mean(kc['full']); pm = np.mean(kc['phase']); xm = np.mean(kc['prox'])
    am = np.mean(ka['full'])
    print(f"  full kappa_h (chiral)   = {fm:+.3f}   achiral = {am:+.3f}")
    print(f"  phase-only kappa_h      = {pm:+.3f}   (if ~0: V5's PHASE part is handedness-BLIND)")
    print(f"  proximity-only kappa_h  = {xm:+.3f}   (if >0: kappa_h lives in V5's finite REACH)")
    verdict = ("REAL V5 COUPLING GIVES kappa_h>0 (route b survives on the real functional)"
               if fm > 0.05 and am < 0.05 else
               "kappa_h collapses on the real V5 coupling (route b does NOT survive)")
    print(f"  VERDICT: {verdict}")
    print("=" * 90)


if __name__ == "__main__":
    main()
