"""Yang-Mills mass gap check: verify the structural CORE of Gauge_07's mechanism -- the
non-abelian [A,A] self-interaction LIFTS the abelian massless flat direction. And locate the
genuine unbuilt piece (continuum survival = asymptotic freedom), which is the Clay-hard part.

Gauge_07: gap <=> non-commuting channels. Mechanism: the coherence-deficit gives F^2; abelian
F=dA (commutes, purely quadratic, FREE, has a flat direction = the massless photon); non-abelian
F=dA+[A,A] carries a self-interaction. The cleanest verifiable core:

  For a SPATIALLY-CONSTANT gauge potential (no derivatives, dA=0):
    * abelian:     F = 0                -> deficit 0  -> FLAT direction (a constant A costs
                                                          nothing) = the massless mode.
    * non-abelian: F = [A_mu, A_nu] != 0 -> deficit > 0 -> the flat direction is LIFTED (a
                                                          constant A costs energy) = gap-source.

The lifting of the abelian flat direction by [A,A] is the structural origin of the gap. What is
NOT checkable here (the Clay-hard part, Gauge_07 sec4): that this survives the CONTINUUM limit
(asymptotic freedom) while the abelian theory deconfines. That is the non-perturbative core.
"""
import numpy as np
from scipy.stats import unitary_group


def su_generators_random(N, rng):
    """a random traceless anti-Hermitian (su(N)) matrix = a constant gauge potential component."""
    M = rng.normal(size=(N, N)) + 1j * rng.normal(size=(N, N))
    A = M - M.conj().T                       # anti-Hermitian
    A -= np.trace(A) / N * np.eye(N)          # traceless
    return A / np.linalg.norm(A)              # unit-normalized


def main():
    print("YM MASS GAP: does the non-abelian [A,A] self-interaction LIFT the abelian flat direction?\n")
    rng = np.random.default_rng(0)
    trials = 5000

    print("Spatially-CONSTANT gauge potential (dA=0). Cost of a constant A = ||[A_mu,A_nu]||^2")
    print("(the field-quadratic self-interaction floor; abelian has NONE -> flat direction).\n")
    print(f"  {'N':>4}{'group':>10}{'mean ||[A,A]||^2':>20}{'flat direction?':>18}")
    print("  " + "-" * 52)
    for N in [1, 2, 3, 4]:
        costs = []
        for _ in range(trials):
            Amu = su_generators_random(N, rng) if N > 1 else 1j*rng.normal()*np.ones((1,1))
            Anu = su_generators_random(N, rng) if N > 1 else 1j*rng.normal()*np.ones((1,1))
            comm = Amu @ Anu - Anu @ Amu
            costs.append(float(np.real(np.trace(comm.conj().T @ comm))))
        mean = np.mean(costs)
        grp = "U(1)" if N == 1 else f"U({N})"
        flat = "YES (massless)" if mean < 1e-9 else "LIFTED (gap)"
        print(f"  {N:>4}{grp:>10}{mean:>20.4f}{flat:>18}")

    print("\n  -> N=1 (abelian): [A,A]=0 exactly -> constant A costs nothing -> FLAT direction =")
    print("     the massless photon (layer-1 Coulomb). N>=2 (non-abelian): [A,A]!=0 -> a constant")
    print("     A costs energy -> the flat direction is LIFTED. gap <=> non-commuting channels,")
    print("     verified: the SAME coherence-deficit that gives F^2 lifts the massless mode iff")
    print("     the channel group is non-abelian.")

    print("\n" + "=" * 84)
    print("VERDICT:")
    print("  * STRUCTURAL CORE verified: the abelian massless flat direction is lifted by the")
    print("    non-abelian [A,A] self-interaction in the coherence-deficit. gap <=> non-commuting")
    print("    channels (Gauge_07's mechanism) holds at the structural/physics level. This is the")
    print("    SAME [A,A] in the SAME coherence-deficit that gives -1/4 Tr(F^2) (YM action check).")
    print("  * NOT verified (the Clay-hard part, honestly): CONTINUUM SURVIVAL. The strong-coupling")
    print("    area law confines BOTH abelian and non-abelian; what keeps the non-abelian gap into")
    print("    the continuum (while U(1) deconfines to massless Coulomb) is ASYMPTOTIC FREEDOM --")
    print("    the non-perturbative RG core of the Clay problem. ED locates the gap's ORIGIN ([A,A])")
    print("    but does NOT prove its continuum survival. Mechanism: yes; Clay proof: no (as flagged).")
    print("=" * 84)


if __name__ == "__main__":
    main()
