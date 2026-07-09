"""Spontaneous-homochirality gate: does ED's coupling prefer SAME handedness (kappa_h)?

T4 established ED does not FORCE chirality. Fork (b) redirect: can parity violation
EMERGE via spontaneous breaking + amplification (Frank / homochirality)? The one open,
decidable gate is kappa_h: do same-handedness chiral composites couple more strongly than
opposite-handedness ones? kappa_h > 0 (parity-EVEN, allowed) is the Frank autocatalysis
ingredient -> per-run spontaneous homochirality. kappa_h = 0 (handedness-blind) -> racemic.

FAITHFUL SETUP (not rigged):
- A chiral composite = 4 vertices (a handed tetrahedron; handedness = sign of the signed
  volume). Enantiomer = mirror (flip one axis).
- Phase per vertex DERIVED from a PARITY-EVEN substrate rule: phi_i = (sum_{j!=i} 1/|r_i-r_j|)
  mod 2pi -- a distance-based "potential", identical for a composite and its mirror
  (distances are parity-invariant). No handedness put into the phases by hand.
- V5-like coherence between two composites = PROXIMITY-weighted phase overlap after best
  PROPER-rotation docking (physical: only proper rotations, no mirrors). Same-handed copies
  of a template are congruent by proper rotation (dock perfectly); opposite-handed (a copy
  vs a mirror-copy = enantiomers) are NOT congruent by proper rotation (docking frustrated).
- kappa_h is thus a PARITY-EVEN diastereomeric effect (LL/RR vs LR), the real mechanism
  behind biological homochirality, and it is ALLOWED without breaking ensemble parity.

Prediction under test: is coherence(same) > coherence(opposite)? If yes, kappa_h>0 and the
Frank amplifier (ED's winner-take-all competition) can fix a handedness per run.
"""
import numpy as np
from itertools import permutations

MIRROR = np.diag([-1.0, 1.0, 1.0])


def vertex_phases(T):
    """parity-even, distance-based phase per vertex (mod 2pi)."""
    n = len(T)
    phi = np.zeros(n)
    for i in range(n):
        s = sum(1.0 / np.linalg.norm(T[i] - T[j]) for j in range(n) if j != i)
        phi[i] = s % (2 * np.pi)
    return phi


def proper_kabsch(P, Q):
    """optimal PROPER rotation R (det=+1) rotating Q onto P; returns R."""
    H = Q.T @ P
    U, S, Vt = np.linalg.svd(H)
    d = np.sign(np.linalg.det(Vt.T @ U.T))
    D = np.diag([1.0, 1.0, d])
    return Vt.T @ D @ U.T


def dock_coherence(A, phiA, B, phiB, sigma=0.6):
    """best proper-rotation docking of B onto A over vertex permutations; returns the
    proximity-weighted phase coherence sum_i w_i cos(phiA_i - phiB_pi(i))."""
    A = A - A.mean(0); B = B - B.mean(0)
    best = -np.inf
    for perm in permutations(range(len(B))):
        Bp = B[list(perm)]; phiBp = phiB[list(perm)]
        R = proper_kabsch(A, Bp)
        Br = Bp @ R.T
        d2 = np.sum((A - Br) ** 2, axis=1)
        w = np.exp(-d2 / sigma ** 2)
        coh = np.sum(w * np.cos(phiA - phiBp))
        best = max(best, coh)
    return best


def random_template(rng, chiral=True):
    while True:
        T = rng.normal(size=(4, 3))
        T = T - T.mean(0)
        T = T / np.sqrt(np.mean(np.sum(T ** 2, axis=1)))   # normalize scale
        vol = np.linalg.det(np.stack([T[1] - T[0], T[2] - T[0], T[3] - T[0]]))
        if chiral and abs(vol) > 0.3:
            if vol < 0: T = T @ MIRROR                     # make handedness +
            return T
        if not chiral and abs(vol) < 0.05:
            return T


def chirality_measure(T, phi):
    """how far T is from achiral = 1 - coherence(T, mirror T)/4 (in [0,1])."""
    Tm = T @ MIRROR
    c_opp = dock_coherence(T, phi, Tm, phi)
    return 1 - c_opp / 4, c_opp


def main():
    rng = np.random.default_rng(3)
    print("HOMOCHIRALITY GATE: does same-handedness couple more strongly (kappa_h)?")
    print("coherence(same) is 4 by construction (congruent copies dock perfectly).")
    print("Test: coherence(opposite) < 4 ? (enantiomers can't proper-dock => kappa_h>0)\n")

    print("=== chiral templates (|signed volume| > 0.3) ===")
    kappas, copps, chis = [], [], []
    for k in range(12):
        T = random_template(rng, chiral=True)
        phi = vertex_phases(T)
        chi, c_opp = chirality_measure(T, phi)
        kappa = 4 - c_opp
        kappas.append(kappa); copps.append(c_opp); chis.append(chi)
        print(f"  template {k:2d}: coh(same)=4.00  coh(opp)={c_opp:+.3f}  "
              f"kappa_h={kappa:+.3f}  chirality={chi:.3f}")
    print(f"\n  MEAN over chiral templates: coh(opp)={np.mean(copps):.3f}  "
          f"kappa_h={np.mean(kappas):+.3f}  (kappa_h>0 => same-handedness preference)")

    print("\n=== achiral control (|signed volume| < 0.05, near-planar) ===")
    ka = []
    for k in range(6):
        T = random_template(rng, chiral=False)
        phi = vertex_phases(T)
        _, c_opp = chirality_measure(T, phi)
        ka.append(4 - c_opp)
        print(f"  control {k}: coh(opp)={c_opp:+.3f}  kappa_h={4-c_opp:+.3f}")
    print(f"  MEAN kappa_h (achiral) = {np.mean(ka):+.3f}  (expect ~0: no handedness to prefer)")

    # ---- Frank amplification: given kappa_h>0, does competition fix a handedness? ----
    print("\n=== Frank amplification test (given the measured kappa_h) ===")
    kappa = float(np.mean(kappas))
    print(f"Using measured same-handedness advantage kappa_h={kappa:.3f}.")
    print("Population of L,R copies: replication rate ~ same-handedness coherence support;")
    print("winner-take-all resource competition. Start NEAR-racemic + tiny fluctuation.\n")
    for seed in range(5):
        r = np.random.default_rng(100 + seed)
        L, R = 50.0 + r.normal(0, 1), 50.0 + r.normal(0, 1)   # near-racemic start
        for _ in range(200):
            # same-handedness autocatalysis: each grows ~ (base + kappa*own_fraction),
            # capacity-limited (mutual competition = the P11 winner-take-all analogue).
            fL = L / (L + R); fR = R / (L + R)
            gL = L * (1 + kappa * fL); gR = R * (1 + kappa * fR)
            tot = gL + gR
            L, R = 100 * gL / tot, 100 * gR / tot            # renormalize to fixed capacity
        ee = (L - R) / (L + R)                                # enantiomeric excess
        state = "HOMOCHIRAL-L" if ee > 0.9 else "HOMOCHIRAL-R" if ee < -0.9 else "racemic"
        print(f"  run {seed}: final L={L:5.1f} R={R:5.1f}  enantiomeric excess={ee:+.3f}  {state}")

    print("\n" + "=" * 88)
    print("READ: if coh(opp)<4 for chiral templates (kappa_h>0) and ~4 for achiral (kappa_h~0),")
    print("then ED's proximity+phase coupling is diastereomeric (same-handedness preferred) --")
    print("a PARITY-EVEN effect that does NOT break ensemble parity, but lets the Frank amplifier")
    print("(winner-take-all competition) fix ONE handedness PER RUN from a tiny fluctuation =")
    print("spontaneous homochirality = per-run parity violation from a parity-symmetric theory.")
    print("Ensemble stays 50/50 (which handedness wins is random across runs). Route (b) LIVES.")
    print("=" * 88)


if __name__ == "__main__":
    main()
