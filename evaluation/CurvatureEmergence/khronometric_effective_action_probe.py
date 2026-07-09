"""ED's gravitational effective action: FORM + parameter reduction, and the c_14 -> 0 scalar decoupling.

HONEST FRAMING FIRST: this does NOT derive ED's coupling coefficients from the substrate (a research-
program-scale computation needing the coarse-grained effective action, which does not exist). It does
two honest things: (1) fixes the FORM of the action (khronometric / Horava, because ED has a dynamical
metric + a preferred frame = the arrow); (2) shows how ED's structural conditions reduce the free
parameters, and computes one consequence that matters: in ED's equivalence-principle limit (c_14 -> 0)
the SCALAR mode speed diverges, so the scalar decouples from RADIATION, leaving near-pure-tensor
(GR-like) gravitational waves plus a static (non-radiating) scalar that can still give MOND.

ED gravity's effective action FORM (khronometric, aether u = the arrow):
  S = (1/16 pi G) integral N sqrt(h) [ K_ij K^ij - lambda K^2 + xi ^3R + eta a_i a^i ]
  (ADM form of hypersurface-orthogonal Einstein-aether; parameters (lambda, xi, eta) <-> (c_i).)
  GR is the point lambda = xi = 1, eta = 0 (general covariance restored).

Parameter reduction from ED's structural conditions:
  - xi = 1  (equivalently c_13 = 0): the shared photon/graviton light cone -> tensor speed c_T = c,
    which GW170817 requires. (Structural: one substrate, universal coupling protects the shared cone.)
  - eta -> 0 (equivalently c_14 -> 0): the equivalence principle (universal Q~M) suppresses the
    acceleration/preferred-frame coupling -> small PPN alpha_1, alpha_2.
  - lambda != 1 (equivalently c_2): the ONE distinctive parameter, the GR-deviation, carrying the
    extra scalar sector. NOT derived here; its value is the open number (plausibly tied to MOND a_0).

Standard khronometric scalar-mode speed (Einstein-aether, c_13 = 0, c_3 = -c_1 so c_123 = c_2):
  c_S^2 = c_2 (2 - c_14) / [ c_14 (2 + 3 c_2) ]
As c_14 -> 0 (ED's equivalence-principle limit) c_S^2 -> infinity: the scalar becomes non-dynamical
(instantaneous), decoupling from radiation. So ED's near-exact equivalence principle -> near-pure-
tensor (GR-like) radiation + a static MOND scalar. (The limit is singular; small-but-nonzero c_14 ->
large-but-finite c_S -> tiny scalar radiation. Suggestive, flagged.)
"""
import numpy as np


def c_S2(c14, c2):
    """Khronometric scalar mode speed^2 on the c_13=0 (xi=1) slice."""
    denom = c14 * (2 + 3 * c2)
    if abs(denom) < 1e-300:
        return np.inf
    return c2 * (2 - c14) / denom


def main():
    print("=" * 92)
    print("ED GRAVITATIONAL EFFECTIVE ACTION: form (khronometric) + parameter reduction + c_14->0 decoupling")
    print("=" * 92)

    print("\n Effective action FORM (fixed by ED being khronometric: dynamical metric + preferred frame):")
    print("   S = (1/16 pi G) integral N sqrt(h) [ K_ij K^ij  -  lambda K^2  +  xi ^3R  +  eta a_i a^i ]")
    print("   GR = (lambda, xi, eta) = (1, 1, 0). ED's structural conditions reduce the parameters:")
    print("     xi  = 1     <- shared light cone (c_13=0)  => tensor speed c_T = c  (GW170817)")
    print("     eta -> 0    <- equivalence principle (c_14->0) => small PPN alpha_1, alpha_2")
    print("     lambda      <- the ONE distinctive parameter (GR-deviation, scalar sector); OPEN")

    print("\n THE c_14 -> 0 SCALAR DECOUPLING (equivalence-principle limit): c_S^2 = c_2(2-c_14)/[c_14(2+3c_2)]")
    print(f"   {'c_14 (eta-like)':>16} {'c_S^2 (c_2=0.1)':>18} {'c_S^2 (c_2=1.0)':>18}   note")
    for c14 in (1e-1, 1e-2, 1e-3, 1e-4, 1e-5):
        s1 = c_S2(c14, 0.1); s2 = c_S2(c14, 1.0)
        note = "scalar decoupling (c_S -> inf)" if c14 <= 1e-3 else ""
        print(f"   {c14:>16.0e} {s1:>18.2e} {s2:>18.2e}   {note}")
    print("   -> as c_14 -> 0 the scalar mode speed DIVERGES: the scalar becomes non-dynamical")
    print("      (instantaneous), so it does NOT radiate. ED's near-exact equivalence principle ->")
    print("      near-pure-TENSOR (GR-like) gravitational waves + a static (non-radiating) scalar that")
    print("      can still give MOND. (Singular limit; small c_14 -> tiny scalar radiation. Suggestive.)")

    print("\n WHERE EACH ACTION TERM PLAUSIBLY COMES FROM (substrate roadmap, a correspondence to build,")
    print(" NOT yet a derivation):")
    print("   K_ij K^ij - lambda K^2 : the kinetic term = time-evolution of the geometry along the ARROW")
    print("                            (the foliation's extrinsic curvature); the arrow (P11) is u.")
    print("   xi ^3R                 : spatial curvature = the emergent g~1/b metric's spatial Ricci.")
    print("   eta a_i a^i            : acceleration of the foliation; suppressed by universal coupling.")
    print("   lambda (K^2 coeff)     : the substrate's rigidity for foliation-expansion; the OPEN number,")
    print("                            = how much the arrow resists changing its expansion rate. Computing")
    print("                            it from the P12 stability landscape (Sigma = Coh - Str - Grad) is")
    print("                            the actual open derivation.")

    print("\n VERDICT: the effective action's FORM is determined (khronometric, aether = the arrow), and")
    print(" ED's structural conditions reduce it to essentially ONE distinctive parameter, lambda (the")
    print(" GR-deviation / scalar sector), with xi=1 (GW170817) and eta->0 (equivalence principle) near-")
    print(" GR. The equivalence-principle limit c_14->0 decouples the scalar from radiation -> near-pure-")
    print(" tensor GW + static MOND scalar. NOT a derivation of lambda: computing lambda (and confirming")
    print(" xi=1, eta=0) by coarse-graining the substrate Sigma dynamics is the stated open problem, with")
    print(" the obstruction named (the arrow-foliation's rigidity / the K^2 coefficient).")
    print("=" * 92)


if __name__ == "__main__":
    main()
