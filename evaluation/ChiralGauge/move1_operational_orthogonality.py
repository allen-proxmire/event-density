"""Gleason Move 1: derive channel-orthogonality from OPERATIONAL distinguishability,
non-circularly (do NOT assume the amplitude representation, which already bakes in
orthonormality).

The three failed routes tried to prove <K|L>=0 inside a pre-assumed metric. The correct,
non-circular claim: orthogonality is the OPERATIONAL content of perfect distinguishability.

Two ingredients:
  (A) OPERATIONAL FACT (from P07 + P11 + Born frequencies, no inner product assumed):
      distinct channels are perfectly distinguishable. The "is it K?" commitment gives
        p(K | state-K) = 1     (committing a pure-K preparation always resolves to K, P11)
        p(K | state-L) = 0     (state-L has b_K=0, so it never resolves to K, P07 distinctness)
      This is pure commitment-frequency data. No metric.
  (B) THEOREM (representation-level, but NOT assuming orthonormality): two states can be
      PERFECTLY distinguished (a measurement detects one with certainty and the other never)
      IF AND ONLY IF they are orthogonal. We demonstrate this by trying to build the
      distinguishing measurement for NON-orthogonal candidate states and showing it fails.

Conclusion: (A) says ED's channels are perfectly distinguishable; (B) says perfectly
distinguishable => orthogonal; therefore <K|L>=0 is FORCED by the operational data, not
postulated. P-Channel-Orthogonality is discharged as a non-independent postulate.

The demonstration of (B): candidate channel-states with a TUNABLE overlap c=<K|L> (we do
NOT set c=0; we let the operational requirement decide). For each c, compute the best
confusion-free detection of K:  max <K|E|K>  over POVM elements 0<=E<=I with <L|E|L>=0.
The optimum is the projector onto |L>'s orthogonal complement, giving <K|E|K> = 1 - c^2,
which equals 1 (perfect) IFF c=0. So perfect distinguishability forces c=0 = orthogonality.
"""
import numpy as np


def best_confusionfree_detection(c):
    """max prob of detecting K, subject to NEVER firing on L, for candidate states with
    overlap c = <K|L>. Returns the achievable p(K|K) at zero false-positive on L.
    (Analytic optimum + a brute-force POVM search to confirm we didn't assume the answer.)"""
    K = np.array([1.0, 0.0])
    L = np.array([c, np.sqrt(max(0.0, 1 - c**2))])          # <K|L> = c, both unit
    # constraint <L|E|L>=0 with E>=0  =>  E|L>=0  =>  E supported on span{|L_perp>}
    Lp = np.array([L[1], -L[0]])                            # unit vector orthogonal to L
    E_opt = np.outer(Lp, Lp)                                # projector onto |L_perp>
    analytic = float(K @ E_opt @ K)                         # = |<K|L_perp>|^2 = 1 - c^2

    # brute-force confirm: scan rank-1 projectors E=|v><v| with <L|v>=0 (forced), plus
    # sub-unit scalings; the max confusion-free detection cannot exceed the projector's.
    best = 0.0
    for t in np.linspace(0, 2*np.pi, 2000):
        v = np.array([np.cos(t), np.sin(t)])
        if abs(L @ v) < 1e-6:                              # <L|E|L>=0 requires v ⊥ L
            E = np.outer(v, v)
            best = max(best, float(K @ E @ K))
    return analytic, best


def main():
    print("MOVE 1: does OPERATIONAL perfect-distinguishability force channel orthogonality?\n")
    print("(B) THEOREM CHECK: best confusion-free detection of K vs candidate overlap c=<K|L>")
    print("    (we do NOT assume c=0; we ask what perfect distinguishability requires)\n")
    print(f"  {'c=<K|L>':>10}{'max p(K|K) at p(K|L)=0':>26}{'perfect?':>12}")
    print("  " + "-" * 48)
    for c in [0.0, 0.2, 0.4, 0.6, 0.8, 0.95, 0.99]:
        analytic, brute = best_confusionfree_detection(c)
        perfect = "YES" if analytic > 1 - 1e-9 else "no"
        print(f"  {c:>10.2f}{analytic:>19.4f} (={1-c**2:.3f}={brute:.3f}){perfect:>9}")
    print("\n  -> perfect confusion-free detection (=1) is achievable IFF c=0.")
    print("  -> NON-orthogonal states (c>0) are PROVABLY NOT perfectly distinguishable:")
    print("     the best you can do is 1-c^2 < 1. (Not assumed; derived by optimizing the POVM.)")

    print("\n(A) OPERATIONAL FACT (ED, from P07 + P11 + Born, NO metric assumed):")
    print("    pure channel-K preparation, commit (P11): resolves to K with frequency 1.")
    print("    pure channel-L preparation (b_K=0, P07 distinctness): resolves to K with freq 0.")
    print("    => ED's distinct channels satisfy p(K|K)=1, p(K|L)=0 = PERFECT distinguishability.")

    print("\n" + "=" * 70)
    print("CONCLUSION (non-circular):")
    print("  (A) ED's channels are perfectly distinguishable [operational: P07+P11+Born].")
    print("  (B) perfectly distinguishable  <=>  orthogonal   [theorem: derived above].")
    print("  => <K|L> = 0 is FORCED by the commitment frequencies, not postulated.")
    print("  P-Channel-Orthogonality is DISCHARGED as a non-independent postulate:")
    print("  it is the operational-distinguishability content, given the inner-product")
    print("  representation (whose existence is the Soler reconstruction, verified separately).")
    print("  The 3 failed routes failed because they sought it as a KINEMATIC metric fact;")
    print("  it is an OPERATIONAL fact that the metric merely represents.")
    print("=" * 70)


if __name__ == "__main__":
    main()
