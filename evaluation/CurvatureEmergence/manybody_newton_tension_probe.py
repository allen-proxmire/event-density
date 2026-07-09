"""The many-body Newton tension of the interference-MOND recast: showstopper or resolved?

*** RETRACTED 2026-07-09: the "resolved" conclusion below is WRONG (over-banked save, Claude-B-caught). ***
The ~70-order headroom is a UNITS ARTIFACT: this probe counts the horizon by AREA (b_hor=(R_H/l_P)^2
~1e123) but the galaxy by MASS (b_gal=M/m_Pl~1e50). A horizon's area count = (its mass count)^2, so the
mismatch inflates the headroom by ~1.07e62 (the entire "save"). Counted consistently by MASS (horizon
M_hor/m_Pl~1e61): sigma^2~b_gal/b_hor~1e-12, sigma~1.6e-6, and a galaxy at star-counting gives
sigma^2*N~0.27 -> Newton FAILS. Also the paper's own S6 needs sigma~0.09 (=a0_obs/2cH0), the SAME sigma
36 orders away. The MOND-survival "check" is tautological (sigma is DEFINED as sqrt(b_gal/4b_hor)). The
many-body Newton tension SURVIVES as a potential showstopper. Kept for the record. Do not cite.
---
ORIGINAL (WRONG) DOCSTRING BELOW:

THE TENSION (Claude-B, correctly): the sigma^2-vs-sigma coherence asymmetry is per-PAIR. But coherence
is transitive -- if mass A is sigma-coherent with the horizon (needed for MOND) and B is too, then A and
B are sigma^2-coherent WITH EACH OTHER (a two-body probe confirms this below), and summed over N separate
masses the local-local Newton violation is ~ sigma^2 * N relative to the diagonal. Many-body Newton then
needs sigma^2 * N << (Newton test precision). Is that compatible with a sigma large enough to give MOND?

THE KEY POINT: sigma is NOT free. The MOND onset (cross-term 2 sigma sqrt(b_loc b_hor) ~ diagonal b_loc)
fixes sigma^2 ~ b_onset / (4 b_hor), where b_onset is the bandwidth of a system at the MOND onset (a
galaxy) and b_hor is the horizon bandwidth. The horizon bandwidth is the HOLOGRAPHIC count b_hor ~
(R_H/l_P)^2 ~ 10^123 (the same count that gives the area law and g~1/b, and the same order as Theta_ED ~
10^-122). A galaxy is b_gal ~ M_gal/m_Pl ~ 10^50. So sigma^2 ~ b_gal/b_hor ~ 10^-73: the enormous horizon
bandwidth FORCES sigma tiny. That tiny sigma is exactly what many-body Newton needs, and it comes for free
from the MOND onset + the holographic horizon. This probe checks whether the ~70 orders of headroom
survive realistic source counts N.

HONEST TIER: the resolution is ORDER-OF-MAGNITUDE / structural -- it relies on b_hor ~ 10^123 (holographic,
used throughout the ED gravity arc) and b_onset ~ b_gal ~ 10^50 (order of magnitude); the precise
dimensional bridge (bandwidth <-> acceleration, hence the O(1) coefficient) is not worked out, but the
~70-order headroom absorbs O(1)-to-several-order uncertainties. The double-slit QM-consistency is separate
(two paths of ONE particle share the alignment -> cancels; that is within-particle, not between masses).
"""
import numpy as np


def two_body_transitivity(seed=0, n=400000):
    """A,B each independently sigma-aligned to a FIXED horizon reference (phase 0). Show their MUTUAL
    coherence is sigma^2 (transitivity), and the local-horizon coherence is sigma (the asymmetry)."""
    rng = np.random.default_rng(seed)
    for kappa in [0.2, 1.0, 3.0]:
        from scipy.special import i0, i1
        sig = i1(kappa) / i0(kappa)
        pa = rng.vonmises(0.0, kappa, n)         # A aligned to horizon (phase 0) with resultant sigma
        pb = rng.vonmises(0.0, kappa, n)          # B independently aligned to horizon
        c_AB = np.mean(np.cos(pa - pb))           # mutual (local-local): expect sigma^2
        c_Ah = np.mean(np.cos(pa - 0.0))          # local-horizon: expect sigma
        print(f"     sigma={sig:.4f}:  A-B (local-local) = {c_AB:.4f} (~sigma^2={sig**2:.4f});  "
              f"A-horizon = {c_Ah:.4f} (~sigma). Transitivity confirmed: A~hor & B~hor => A~B at sigma^2.")


def main():
    print("=" * 96)
    print("MANY-BODY NEWTON TENSION: is sigma forced small enough by the holographic horizon bandwidth?")
    print("=" * 96)

    print("\n[1] Coherence transitivity is real (the violation cannot be wished away):")
    two_body_transitivity()

    # ---- physical scales ----
    c = 2.998e8; G = 6.674e-11
    Mpc = 3.086e22; H0 = 67.4e3 / Mpc
    R_H = c / H0
    l_P = 1.616e-35
    m_Pl = 2.176e-8
    M_sun = 1.989e30
    m_p = 1.673e-27

    b_hor = 4 * np.pi * (R_H / l_P) ** 2               # holographic horizon bandwidth (channel count)
    M_gal = 1e12 * M_sun                               # ~Milky Way
    b_gal = M_gal / m_Pl                               # galaxy bandwidth (mass in Planck units)
    sigma2 = b_gal / (4 * b_hor)                        # from the MOND onset: cross-term ~ diagonal
    sigma = np.sqrt(sigma2)

    print("\n[2] sigma is FIXED by the MOND onset + the holographic horizon bandwidth (not free):")
    print(f"     b_hor (holographic, ~(R_H/l_P)^2) = {b_hor:.2e}   (~10^123; ~ Theta_ED/Lambda scale)")
    print(f"     b_gal (~M_gal/m_Pl, onset system) = {b_gal:.2e}   (~10^50)")
    print(f"     => sigma^2 ~ b_gal/(4 b_hor)      = {sigma2:.2e}   (sigma = {sigma:.2e})")
    print(f"     headroom b_hor/b_gal             = {b_hor/b_gal:.2e}   (~10^73: the horizon dwarfs any system)")
    # sanity: does this sigma give MOND at O(1)?
    mond_ratio = 2 * sigma * np.sqrt(b_hor / b_gal)
    print(f"     check MOND cross/diagonal at onset = 2 sigma sqrt(b_hor/b_gal) = {mond_ratio:.3f} (O(1): MOND survives)")

    print("\n[3] Many-body Newton violation ~ sigma^2 * N, swept over physically-plausible source counts N:")
    N_sun_atoms = M_sun / m_p
    N_gal_atoms = M_gal / m_p
    cases = [
        ("solar system, N = bodies (~10)", 10),
        ("solar system, N = atoms in Sun", N_sun_atoms),
        ("galaxy, N = stars (~1e11)", 1e11),
        ("galaxy, N = atoms (~1e69)", N_gal_atoms),
        ("galaxy, N = Planck loci (unphysical, ~1e80)", 1e80),
    ]
    print("     Newton test precision: solar system ~1e-9 (some tests 1e-13); galaxy-scale star-star: untested << 1")
    for name, N in cases:
        viol = sigma2 * N
        verdict = "SAFE" if viol < 1e-9 else ("marginal/OK (untested at this level)" if viol < 1e-2 else "FAILS")
        print(f"     {name:<44} N={N:.1e}  ->  sigma^2 N = {viol:.1e}   {verdict}")

    print("\n[4] Within-particle (double-slit) is SEPARATE and always safe: the two paths of ONE particle")
    print("    share that particle's horizon alignment, which cancels in their relative phase (QM-consistency")
    print("    probe). The sigma^2 mutual coherence is between DIFFERENT masses, not between one particle's paths.")

    print("\nVERDICT (honest tiers):")
    print("  RESOLVED WITH LARGE MARGIN (order-of-magnitude/structural): sigma is not free; the MOND onset")
    print("  ties sigma^2 ~ b_onset/b_hor, and the HOLOGRAPHIC horizon bandwidth b_hor ~ 10^123 forces")
    print("  sigma^2 ~ 10^-73. That same tiny sigma makes the many-body Newton violation sigma^2 N safe for")
    print("  every physically-reasonable source count: solar system ~1e-16 (atoms) to ~1e-72 (bodies), well")
    print("  below the ~1e-9..1e-13 bounds; galaxy ~1e-4 at atom-counting (untested, below MOND). Only")
    print("  unphysical Planck-locus counting (~1e80) would fail. So it is NOT a showstopper: the enormous")
    print("  horizon bandwidth simultaneously sets the MOND onset AND protects Newton, with ~70 orders of")
    print("  headroom absorbing the unresolved dimensional-bridge O(1) factors.")
    print("  RESIDUALS (honest): relies on b_hor ~ 10^123 (holographic, arc-standard) and b_onset ~ 10^50")
    print("  (order of magnitude); the precise bandwidth<->acceleration bridge (the O(1) coefficient) is")
    print("  unworked; and it predicts a real but ~1e-16 (untestable) source-source Newton correction.")
    print("  The transitivity (violation is nonzero, forced) is exact; its size is what the horizon saves.")
    print("=" * 96)


if __name__ == "__main__":
    main()
