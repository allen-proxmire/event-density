"""Gauge program, the uniqueness {1,2,3}: does channel-family STABILITY bound N<=3?

Gauge_01 derives the gauge-group FORM: N indistinguishable same-rule-type channels +
bandwidth conservation (P04) -> U(N)=SU(N)xU(1). The SM U(1)xSU(2)xSU(3) <-> multiplicities
{1,2,3}. But the framework gives SU(N) for ANY N. Gauge_04 REFUTED the spatial-dimension
bound (category error: SU(N) is complex-internal, not real-spatial). Gauge_03 sec5-6 flags
the STABILITY route as "the next concrete target": does a coherence-stability constraint on
N-channel families forbid N>3? We test it directly.

MODEL (P12-native): a same-rule-type family = N channels with amplitudes a_i (b_i=a_i^2),
total bandwidth conserved sum a_i^2 = B (P04). The unbroken-SU(N) multiplet is the SYMMETRIC
state a_i = sqrt(B/N), all phases aligned (mutually coherent). Family stability = this
symmetric state is a stable extremum of the P12 stability functional
    F = -Coh + lambda*Str,   Coh = sum_{i<j} a_i a_j  (pairwise coherence, aligned),
                             Str = sum_i a_i^4        (concentration/strain cost).
(Minimizing F = maximizing coherence, penalizing concentration.) Two tests:
  (1) constrained Hessian of F at the symmetric point (perturbations on sum a_i^2=B):
      all eigenvalues > 0 => STABLE (a min) => the multiplet survives at that N.
  (2) single-channel decoherence cost: misalign one channel's phase by delta; the coherence
      energy cost vs N tells us whether large families are HARDER (corpus intuition) or
      EASIER (more coherence-binding) to hold together.

If a clean stability transition at N=3 appears -> a candidate derivation of the SM group.
If the symmetric multiplet is stable for all N -> the stability route does NOT bound N.
"""
import numpy as np


def constrained_hessian_eigs(N, lam, B=1.0):
    """eigenvalues of the Hessian of F on the constraint surface sum a_i^2 = B, at the
    symmetric point a_i = s = sqrt(B/N). Perturbations delta with delta . a = 0 (stay on
    the sphere). Returns the constrained eigenvalues."""
    s = np.sqrt(B / N)
    # F = -1/2[(sum a)^2 - sum a^2] + lam sum a^4
    # Hessian H_jk = -1 + delta_jk (1 + 12 lam a_k^2); at symmetric: H = (1+12 lam s^2) I - J
    H = (1 + 12 * lam * s**2) * np.eye(N) - np.ones((N, N))
    a = s * np.ones(N)                                  # symmetric amplitude vector
    # project onto the tangent space of the sphere (perp to a)
    P = np.eye(N) - np.outer(a, a) / (a @ a)
    Hc = P @ H @ P
    eigs = np.linalg.eigvalsh(Hc)
    # drop the ~0 eigenvalue from the removed radial direction
    return np.sort(eigs)[1:]                             # N-1 tangent eigenvalues


def decoherence_cost(N, delta, B=1.0):
    """coherence energy cost of misaligning ONE channel's phase by delta (others aligned)."""
    s2 = B / N                                           # b_i = B/N
    # aligned Coh_full = C(N,2)*(B/N); misaligning channel k: its (N-1) pair terms get cos(delta)
    coh_aligned = (N * (N - 1) / 2) * s2
    coh_misaligned = coh_aligned - (N - 1) * s2 * (1 - np.cos(delta))
    return coh_aligned - coh_misaligned                 # = (N-1)*(B/N)*(1-cos delta)


def main():
    print("GAUGE UNIQUENESS {1,2,3}: does channel-family stability bound N?\n")
    print("(1) Symmetric SU(N) multiplet: constrained-Hessian eigenvalues (min eig) vs N")
    print("    (all > 0 => the multiplet is a STABLE min => survives at that N)\n")
    print(f"    {'N':>4}", end="")
    for lam in [0.0, 0.5, 1.0, 2.0]:
        print(f"   min-eig(lam={lam})", end="")
    print()
    for N in range(2, 9):
        print(f"    {N:>4}", end="")
        for lam in [0.0, 0.5, 1.0, 2.0]:
            e = constrained_hessian_eigs(N, lam)
            print(f"   {e.min():>13.3f}", end="")
        print()
    print("\n    -> min-eig > 0 for ALL N and all lambda: the symmetric SU(N) multiplet is a")
    print("       stable minimum at every N. Coherence-stability does NOT bound N.")

    print("\n(2) Single-channel decoherence cost vs N (delta=pi/2): does large-N cost MORE?")
    print(f"    {'N':>4}{'decoherence cost':>20}")
    for N in range(2, 9):
        print(f"    {N:>4}{decoherence_cost(N, np.pi/2):>20.4f}")
    print("    -> cost GROWS with N: larger multiplets are MORE coherence-bound, i.e. HARDER")
    print("       to break, not easier. The corpus intuition ('large-N harder to maintain')")
    print("       is BACKWARDS: coherence-binding favors large N.")

    print("\n" + "=" * 78)
    print("VERDICT: the stability route does NOT give {1,2,3}. The symmetric SU(N) multiplet")
    print("is stable for all N, and coherence-binding INCREASES with N (large multiplets more")
    print("stable). Both flagged candidates now fail: spatial-dimension bound (refuted,")
    print("Gauge_04) and coherence-stability (refuted here, points the wrong way). The SM")
    print("gauge-group uniqueness {1,2,3} remains a genuine OPEN WALL in ED -- as in standard")
    print("physics, which also does not derive it. The gauge-group FORM (SU(N) from")
    print("multiplicity, Gauge_01) stands; the uniqueness does not follow from stability.")
    print("=" * 78)


if __name__ == "__main__":
    main()
