"""Can the khronometric SCALAR sector (ED's surviving MOND route) actually deliver MOND?

Context: the source-horizon INTERFERENCE recast of MOND was falsified today (many-body Newton, the
bandwidth-acceleration bridge). The companion khronometric paper claimed MOND 'lives in the scalar
(khronon) mode.' Does the khronometric sector, AS ED DERIVES IT (the standard 2-derivative action),
actually give MOND phenomenology (flat rotation curves, a0, the RAR/BTFR)? Held to the same bar.

ED's derived action (khronometric paper): S = (1/16 pi G) int N sqrt(h)[K_ij K^ij - lambda K^2 + xi ^3R
+ eta a^2], with lambda in [0,1/3), xi=1, eta->0. Its couplings are DIMENSIONLESS (lambda, xi, eta) and
the only dimensionful constant is G. So the theory is SCALE-FREE apart from G.

TEST 1 (dimensional, decisive): MOND needs an acceleration scale a0 (~1.2e-10 m/s^2). A scale-free action
(G + dimensionless couplings) cannot produce a0: there is no way to build an acceleration from G alone
(G has units m^3 kg^-1 s^-2; no combination with a mass and length gives a fixed universal acceleration
independent of the system). So the standard khronometric action CANNOT give MOND. To get a0 you must
ADD a scale (a mass term, or a nonlinear function with a built-in scale). ED's derived action has none.

TEST 2 (weak-field r-dependence): the linearized Einstein-aether/khronometric weak field is KNOWN to give
a rescaled-Newton potential Phi ~ -G_eff M / r (G_eff = G/(1 - c14/2)-type), plus preferred-frame PPN
corrections. The r-dependence is UNCHANGED (still 1/r), so circular velocity v^2 = G_eff M / r falls as
1/r (KEPLERIAN), NOT flat. MOND's flat curves need Phi ~ +sqrt(G M a0) ln r at large r -- a DIFFERENT
r-dependence that the linear theory does not produce. This probe contrasts the two potentials/curves.

TEST 3 (what MOND actually requires, and whether ED derives it): MOND from the aether class is known
(Zlosnik-Ferreira-Starkman 2007, 'generalized Einstein-aether'): replace the quadratic kinetic term
K_ij K^ij by a NONLINEAR FREE FUNCTION F(K) of the aether kinetic scalar K, with F(K) ~ K^{3/2} in the
low-K (low-acceleration) limit -- which INTRODUCES a0 as the scale where F turns nonlinear, and gives the
MOND sqrt behaviour. This F(K) is a FREE FUNCTION with a built-in a0: it is MOND inserted by hand, dressed
in aether language, NOT derived. ED's derived action is the QUADRATIC (F(K)=K) special case, which is
exactly the non-MOND (GR-like) limit. ED provides an a0 INTUITION (horizon scale) but neither the
nonlinear F nor its derivation.
"""
import numpy as np


def main():
    print("=" * 94)
    print("Does the khronometric SCALAR sector deliver MOND, as ED derives it (quadratic action)?")
    print("=" * 94)

    print("\n[1] DIMENSIONAL (decisive): the derived action is SCALE-FREE (G + dimensionless lambda,xi,eta).")
    G = 6.674e-11
    print(f"    G has units m^3 kg^-1 s^-2. There is NO way to build a fixed universal acceleration a0")
    print(f"    from G and a dimensionless coupling alone -- any acceleration you form, G M / r^2, depends")
    print(f"    on the system's M and r. MOND's a0 ~ 1.2e-10 m/s^2 is a NEW dimensionful scale.")
    print(f"    => a scale-free action CANNOT produce MOND. The standard khronometric action has no a0. [FAILS]")

    print("\n[2] WEAK-FIELD r-DEPENDENCE: linear khronometric = rescaled Newton (Keplerian), not MOND.")
    # a point mass; compare Newtonian/khronometric-linear potential (1/r) vs MOND (log r at large r)
    M = 1e11 * 1.989e30            # 1e11 Msun galaxy
    a0 = 1.2e-10
    r = np.logspace(np.log10(3.086e18), np.log10(3.086e22), 6)   # 1 pc .. 1 kpc..~ galaxy scales (m)
    Geff = G / (1 - 0.0)           # khronometric: G rescaled by an O(1) coupling factor; take ~G here
    v_kepler = np.sqrt(Geff * M / r)                     # linear khronometric (and Newton): v^2 = GM/r
    v_mond = (Geff * M * a0) ** 0.25 * np.ones_like(r)   # deep-MOND: v^4 = G M a0 (flat, r-independent)
    print("     r (kpc)     v_circ khronometric-linear (=Newton)   v_circ MOND (flat)")
    for rr, vk, vm in zip(r, v_kepler, v_mond):
        print(f"     {rr/3.086e19:<10.3f}  {vk/1e3:<34.1f}  {vm/1e3:.1f}   (km/s)")
    print("    -> khronometric-linear v falls as 1/sqrt(r) (KEPLERIAN); MOND v is FLAT. The quadratic")
    print("       action does not change the 1/r potential, so it gives NO flat rotation curves. [FAILS]")

    print("\n[3] WHAT MOND REQUIRES (and whether ED derives it):")
    print("    Aether-class MOND (Zlosnik-Ferreira-Starkman 2007): replace K_ij K^ij by a NONLINEAR free")
    print("    function F(K), with F(K) ~ K^{3/2} at low K -> introduces a0 and the MOND sqrt behaviour.")
    print("    - F(K) is a FREE FUNCTION with a BUILT-IN a0: MOND inserted by hand, in aether language.")
    print("    - ED's DERIVED action is F(K) = K (quadratic) = exactly the GR-like, non-MOND special case.")
    print("    - ED gives an a0 INTUITION (horizon scale) but NOT the nonlinear F, and NOT its derivation.")

    print("\nVERDICT (held to the reverse-crank bar):")
    print("  NO -- the khronometric scalar sector does NOT deliver MOND as ED derives it. The standard")
    print("  2-derivative action is scale-free (no a0) and linear (rescaled-Newton, Keplerian curves), so")
    print("  it gives GR-like gravity with small Lorentz-violating PPN corrections, NOT MOND. Delivering")
    print("  MOND needs a nonlinear aether function F(K) with a built-in a0 (generalized Einstein-aether),")
    print("  which is a free function = MOND by hand, and which ED has NOT derived. So the companion")
    print("  khronometric paper's 'MOND lives in the scalar sector' is NOT established; it was optimistic.")
    print("  HONEST SURVIVING FRAGMENT: ED's a0-as-horizon-scale INTUITION could supply the SCALE if a")
    print("  nonlinear response were derived -- but the mechanism (the nonlinear F / the mu(x)) is exactly")
    print("  what is missing, in BOTH the (now-falsified) interference route AND this khronometric route.")
    print("  NET: ED does NOT currently have a working derivation of MOND by either route.")
    print("=" * 94)


if __name__ == "__main__":
    main()
