"""Off-diagonal relic probe (dark-sector) -- what the relic does INSIDE ED's interference gravity.

NOT a re-derivation: baryon<->horizon off-diagonal = MOND (a=sqrt(a_N a0)) is already done in
Paper_QuadraticStrain_v1. The new question: add the RELIC as a source to the quadratic strain
Str = |sum_a P^(a)|^2 (P=sqrt(b)) and ask whether the interference structure resolves or worsens
the galactic double-counting.

Sources in a galaxy: baryons (a_N,B), the relic (a_N,R if it clumps there), the horizon (a0).
  * DIAGONAL (Newton): each source's self-gravity. Relic diagonal = a_N,R (a halo -> double-count).
  * OFF-DIAGONAL (interference): sqrt(a_N,B a0) [=MOND], sqrt(a_N,R a0) [relic<->horizon],
    sqrt(a_N,B a_N,R) [baryon<->relic].

Key comparison in the DEEP-MOND regime (a_N << a0), where galaxies live:
  the relic's interference contribution sqrt(a_N,R a0) vs its naive Newtonian halo a_N,R.
  Ratio = sqrt(a0 / a_N,R) >> 1 in deep MOND  ->  interference AMPLIFIES the relic's pull.
So a relic that clumps in a galaxy double-counts even HARDER than a naive halo would.
"""
import numpy as np

a0 = 1.2e-10  # m/s^2, cH0/2pi (Paper_029), value-inherited


def a_N(M, R):
    G = 6.674e-11
    return G * M / R**2


def main():
    Msun = 1.989e30
    kpc = 3.086e19
    # a Milky-Way-like point: baryonic mass inside R, at galactic radius
    M_B = 6e10 * Msun
    R = 10 * kpc
    aNB = a_N(M_B, R)

    print(f"galactic test point: a_N(baryon) = {aNB:.2e} m/s^2,  a0 = {a0:.2e} m/s^2")
    print(f"  regime: a_N/a0 = {aNB/a0:.2f}  ({'deep-MOND' if aNB < a0 else 'Newtonian'})\n")

    # MOND from baryon<->horizon off-diagonal (the established result)
    aMOND = np.sqrt(aNB * a0)
    print(f"baryon<->horizon off-diagonal (MOND, established): sqrt(a_N,B a0) = {aMOND:.2e} m/s^2")
    print(f"  (this alone fits rotation curves; NO relic needed for galaxies)\n")

    # now add a relic that CLUMPS in the galaxy, tracking the ~5x cosmic ratio
    print("if the relic CLUMPS in the galaxy (cold), with a_N,R = f * a_N,B:")
    print("  f     a_N,R(halo)   relic off-diag sqrt(a_N,R a0)   amplification   double-count vs MOND")
    for f in [0.2, 1.0, 5.0]:
        aNR = f * aNB
        halo = aNR                     # naive Newtonian relic halo (diagonal)
        offdiag = np.sqrt(aNR * a0)    # relic<->horizon interference (off-diagonal, dominant in deep-MOND)
        amp = offdiag / halo           # = sqrt(a0/a_N,R)
        dc = offdiag / aMOND           # relic's interference pull as a fraction of the baryon MOND
        print(f"  {f:4.1f}  {halo:.2e}     {offdiag:.2e}                {amp:6.1f}x         +{dc:.1f}x MOND")

    print("\n" + "=" * 78)
    print("READ:")
    print("  * MOND (galaxies) = baryon<->horizon interference, relic-free. Established, unchanged.")
    print("  * A relic that clumps in the galaxy adds sqrt(a_N,R a0) via its own interference with")
    print("    the horizon -- here +0.4x to +2.2x the baryon MOND acceleration. That is a large")
    print("    double-count: even a relic merely tracking the baryons (f=1) DOUBLES the pull.")
    print("  * Amplification vs a naive Newtonian halo is sqrt(a0/a_N,R): >1 where the relic is")
    print("    dilute (a_N,R < a0, deeper-MOND dwarfs -- 'tens of times' only there), ~1 near the")
    print("    transition, <1 for a dense relic. Either way the ABSOLUTE double-count is significant.")
    print("  * Consequence: the interference mechanism does NOT dissolve the double-counting; the")
    print("    relic must be absent/diffuse in galaxies (warm / free-streaming). The two-component")
    print("    reality stands, and the galactic constraint on the relic is if anything sharpened.")
    print("=" * 78)


if __name__ == "__main__":
    main()
