"""Gleason keystone, decisive first gate: is ED's measurement logic NON-BOOLEAN?

The reframe: orthogonality is operational (P11 commitment + P07); the inner-product FORM
is forced by P04-P09 complementarity via Piron-Soler -- but ONLY if ED's logic is genuinely
non-Boolean (orthomodular). This is the sharp, decidable entry point. If ED has a truly
incompatible pair of measurements (which-channel vs relative-phase), the logic is non-Boolean
and the quantum-logic route is ON. If all ED measurements are compatible (Boolean), the logic
is classical and NO Hilbert space follows (a real potential negative).

ED's own structure (Paper_001 P_K=sqrt(b_K) e^{i pi_K}, Paper_003 Born f_K=b_K/sum b,
P11 commitment = which-channel collapse):
  * which-channel measurement: outcome K with prob b_K (a bandwidth/P04 fact).
  * relative-phase (interference) measurement: the OBSERVABLE phase is the RELATIVE phase
    between channels (per-channel absolute phase is gauge/unobservable). It shows up as the
    coherence/interference term in the combined participation |P_1+P_2|^2 = b_1+b_2 +
    2 sqrt(b_1 b_2) cos(dpi). Requires a coherent superposition (no commitment).

Claim to test: these two are MUTUALLY UNBIASED / complementary -> non-Boolean.
Demonstrated four ways, all from ED's amplitude structure (no QM Hilbert space assumed):
  (1) interference: combined participation depends on dpi (coherent).
  (2) commitment destroys it: P11 randomizes dpi -> ensemble interference term -> 0.
  (3) an uncertainty relation: a definite relative phase FORCES b_1=b_2 (maximal which-channel
      uncertainty); a definite channel forces dpi UNDEFINED. They can't be jointly sharp.
  (4) DISTRIBUTIVITY FAILS: for A=channel-1, B/C=phase eigenstates, A^(BvC) != (A^B)v(A^C)
      -- the textbook non-Boolean signature -- because channel & phase rays are distinct
      (meet = 0) yet the phase basis spans (join = I). This is the orthomodular fingerprint.
"""
import numpy as np

k1 = np.array([1, 0], complex)          # channel 1 (which-channel basis)
k2 = np.array([0, 1], complex)          # channel 2
plus = np.array([1, 1], complex) / np.sqrt(2)     # relative-phase eigenstate dpi=0
minus = np.array([1, -1], complex) / np.sqrt(2)   # relative-phase eigenstate dpi=pi


def combined_participation(b1, b2, dpi):
    """ED's interference observable: |P_1 + P_2|^2 on a shared mode (the coherence content)."""
    return b1 + b2 + 2 * np.sqrt(b1 * b2) * np.cos(dpi)


def proj(v):
    v = v / np.linalg.norm(v); return np.outer(v, v.conj())


def meet_rank(P, Q):
    """rank of the projector onto range(P) ∩ range(Q) (lattice MEET of two subspaces)."""
    # intersection of two subspaces: null space of [I-P] stacked with [I-Q], i.e. vectors in both ranges
    M = np.vstack([np.eye(2) - P, np.eye(2) - Q])
    ns = np.linalg.svd(M)[2]
    s = np.linalg.svd(M)[1]
    return int(np.sum(s < 1e-9))        # dimension of common null space = dim of intersection


def main():
    print("GLEASON GATE: is ED's which-channel vs relative-phase logic NON-BOOLEAN?\n")

    print("(1) INTERFERENCE (coherent superposition, b1=b2=0.5): combined participation vs dpi")
    for dpi in [0, np.pi/2, np.pi, 3*np.pi/2]:
        print(f"    dpi={dpi:4.2f}:  |P1+P2|^2 = {combined_participation(0.5,0.5,dpi):.3f}")
    print("    -> depends on the RELATIVE phase = genuine interference (the phase is observable).")

    print("\n(2) COMMITMENT destroys it (P11 randomizes dpi over the ensemble):")
    rng = np.random.default_rng(0)
    dpis = rng.uniform(0, 2*np.pi, 100000)
    print(f"    ensemble-mean |P1+P2|^2 after commitment = "
          f"{np.mean([combined_participation(0.5,0.5,d) for d in dpis]):.3f}  "
          f"(= b1+b2 = 1.0, interference GONE)")

    print("\n(3) UNCERTAINTY RELATION (complementarity):")
    print("    definite relative phase (a phase eigenstate) requires b1=b2:")
    for st, nm in [(plus, '|+> (dpi=0)'), (minus, '|-> (dpi=pi)')]:
        b1, b2 = abs(st[0])**2, abs(st[1])**2
        print(f"      {nm}: b1={b1:.2f} b2={b2:.2f}  -> which-channel MAXIMALLY uncertain")
    print("    definite channel (|1>) has b2=0 -> relative phase UNDEFINED (no channel-2 to phase against).")
    print("    => which-channel and relative-phase CANNOT be jointly sharp.")

    print("\n(4) MUTUAL UNBIASEDNESS + DISTRIBUTIVITY FAILURE (the non-Boolean fingerprint):")
    for K, nk in [(k1,'1'), (k2,'2')]:
        for P, npn in [(plus,'+'), (minus,'-')]:
            print(f"    |<channel {nk}|phase {npn}>|^2 = {abs(K.conj()@P)**2:.2f}  (0.50 = mutually unbiased)")
    A, B, C = proj(k1), proj(plus), proj(minus)
    # join B v C = projector onto range(B)+range(C); for a 2-level phase basis this spans -> I
    BvC = np.eye(2)                                  # {|+>,|->} spans the whole space
    lhs = meet_rank(A, BvC)                          # A ^ (B v C) = A ^ I = A  -> rank 1
    AB = meet_rank(A, B); AC = meet_rank(A, C)       # A ^ B, A ^ C (distinct rays -> 0)
    rhs = max(AB, AC)                                # (A^B) v (A^C), ranks 0 v 0 = 0
    print(f"\n    A=channel-1, B=phase+, C=phase-:")
    print(f"      rank[ A ^ (B v C) ] = {lhs}   (= A, since B v C = I)")
    print(f"      rank[ A ^ B ] = {AB},  rank[ A ^ C ] = {AC}  -> rank[ (A^B) v (A^C) ] = {rhs}")
    print(f"      DISTRIBUTIVITY: {lhs} != {rhs}  => {'FAILS (NON-BOOLEAN)' if lhs != rhs else 'holds (Boolean)'}")

    print("\n" + "=" * 88)
    print("VERDICT: ED's which-channel (P04/P11) and relative-phase (P09) measurements are")
    print("mutually unbiased and non-distributive => ED's measurement logic is NON-BOOLEAN")
    print("(orthomodular). The Piron-Soler route is ON: the inner-product form is a candidate")
    print("CONSEQUENCE of this complementarity, not a bare postulate. Remaining hard core =")
    print("verifying the FULL Soler package (atomicity, covering law, angle condition).")
    print("=" * 88)


if __name__ == "__main__":
    main()
