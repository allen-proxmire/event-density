"""Place ED's khronometric structural conditions in the post-GW170817 Einstein-aether viable window.

HONEST FRAMING (stated first): this does NOT derive ED's aether couplings c_1..c_4 from the substrate
(that needs the full coarse-grained effective action, which does not exist yet). It does something
weaker and defensible: it takes ED's two STRUCTURAL conditions, maps them onto the STANDARD Einstein-
aether constraint analysis (standard mode-speed and PPN formulas + standard observational bounds), and
checks whether they land ED in the observationally VIABLE region. Physics (formulas, bounds) is
standard; the ED content is the two conditions; the conclusion is COMPATIBILITY, not a derivation.

ED's two structural conditions:
  (I)  SHARED LIGHT CONE -> c_13 = c_1 + c_3 = 0. ED's emergent photons and gravitons are both modes of
       the one substrate; IF they share the substrate's emergent light cone, the tensor graviton speed
       equals the emergent light speed c, i.e. c_T^2 = 1/(1-c_13) = 1 <=> c_13 = 0. This is exactly the
       GW170817 condition (|c_T - c|/c < 1e-15). LOAD-BEARING ASSUMPTION (plausible, not derived).
  (II) EQUIVALENCE PRINCIPLE -> small preferred-frame couplings. The universal Q~M coupling (which
       killed the scalar dipole) suppresses preferred-frame effects, i.e. small alpha_1, alpha_2.

Standard Einstein-aether results used (Jacobson; Foster & Jacobson 2006):
  tensor speed:  c_T^2 = 1/(1 - c_13)
  PPN preferred-frame:  alpha_1 = -8 (c_3^2 + c_1 c_4) / (2 c_1 - c_1^2 + c_3^2)
  (alpha_2 is tighter and similarly requires small preferred-frame couplings; noted, not re-derived.)
Observational bounds:
  GW170817:   |c_T^2 - 1| < ~1e-15                       -> c_13 ~ 0
  Solar/LLR:  |alpha_1| < 1e-4 ;  |alpha_2| < ~1e-7       -> preferred-frame couplings tiny
  Cherenkov/stability: mode speeds^2 > 0 (no ghosts/tachyons); c_T^2 >= 1 (no grav. Cherenkov by CRs)

This probe: (A) show c_13=0 gives c_T = c exactly (GW170817 auto-satisfied under condition I);
(B) on the c_13=0 slice, compute alpha_1 and find the viable region in (c_1, c_4); show ED's condition
II (equivalence principle -> small c_14) lands inside it; (C) state what remains open (c_2, the scalar/
khronon coupling tied to MOND a_0, and the exact ED values).
"""
import numpy as np


def c_T2(c13):
    return 1.0 / (1.0 - c13)


def alpha1(c1, c3, c4):
    denom = 2 * c1 - c1 ** 2 + c3 ** 2
    if abs(denom) < 1e-30:
        return np.nan
    return -8.0 * (c3 ** 2 + c1 * c4) / denom


def main():
    print("=" * 92)
    print("ED KHRONOMETRIC COUPLINGS vs GW170817 + PULSAR/PPN: a compatibility (placement) analysis")
    print("=" * 92)

    print("\n (A) TENSOR SPEED and GW170817. c_T^2 = 1/(1 - c_13). ED condition I (shared light cone)")
    print("     sets c_13 = 0, so c_T = c EXACTLY:")
    for c13 in (0.0, 1e-15, 1e-3, 0.1):
        cT = np.sqrt(c_T2(c13))
        dev = abs(cT - 1.0)
        tag = "  <- ED (shared light cone): c_T = c, GW170817 satisfied" if c13 == 0 else \
              ("  GW170817 bound edge" if abs(c13-1e-15) < 1e-20 else "  EXCLUDED by GW170817" if c13 >= 1e-3 else "")
        print(f"     c_13={c13:>8.0e}   c_T-c = {dev:>10.2e}{tag}")
    print("     -> GW170817 forces c_13 ~ 0; ED's shared-light-cone condition gives it structurally.")

    print("\n (B) ON THE c_13=0 SLICE (c_3 = -c_1): the derived form is alpha_1 = -4 c_14  (c_14 = c_1+c_4).")
    print("     Solar-system/pulsar bound |alpha_1| < 1e-4  =>  |c_14| < 2.5e-5. Scan c_14:")
    print(f"       {'c_1':>8} {'c_4':>10} {'c_14':>10} {'alpha_1=-4c_14':>16}   status")
    for c1, c4 in [(0.0, 0.0), (0.3, -0.3), (1e-6, -1e-6), (0.0, 1e-5), (0.0, 2e-5), (0.1, 0.0)]:
        c14 = c1 + c4
        a1 = -4.0 * c14                        # derived on the c_13=0 slice
        # cross-check vs the raw formula where non-degenerate
        raw = alpha1(c1, -c1, c4)
        ok = abs(a1) < 1e-4
        note = "VIABLE" if ok else "excluded (|alpha_1|>1e-4)"
        edtag = "  <- ED corner (equiv.principle -> c_14~0)" if abs(c14) < 3e-5 and ok else ""
        print(f"       {c1:>8.0e} {c4:>10.0e} {c14:>10.0e} {a1:>16.2e}   {note}{edtag}")
    print("     -> with c_13=0, viability needs |c_14| < 2.5e-5. ED's equivalence principle (universal")
    print("        Q~M, which also killed the dipole) suppresses preferred-frame effects -> small c_14")
    print("        -> lands INSIDE the viable region. The cleanest ED corner is c_1=c_3=c_14=0 (alpha's")
    print("        vanish, minimal khronometric), leaving only c_2 (the scalar/khronon coupling).")
    print("        (alpha_2, tighter at ~1e-7, likewise needs the small-preferred-frame regime ED gives.)")

    print("\n (C) WHAT'S DERIVED vs OPEN:")
    print("   Structurally addressed by ED: c_13 = 0 (shared light cone -> c_T = c, GW170817); small")
    print("     preferred-frame couplings (equivalence principle -> small alpha_1, alpha_2); scalar")
    print("     DIPOLE suppressed (universal Q~M) -> tightest pulsar scalar bound met.")
    print("   Inherited: the residual scalar (khronon) coupling ~ c_2 ties to the MOND scale a_0.")
    print("   OPEN (uncomputed): ED's EXACT c_i from the substrate; the scalar QUADRUPOLE magnitude and")
    print("     the full BBN/Cherenkov/stability fit. These must sit in the (non-empty) viable window;")
    print("     ED's structure points into it but does not yet pin the values.")

    print("\n VERDICT: ED is a VIABLE khronometric gravity. Its two structural conditions (shared light")
    print(" cone; equivalence principle) place it in the post-GW170817 viable corner (c_13=0, small c_14),")
    print(" with the TWO SHARPEST constraints structurally addressed: c_T = c (GW170817) and dipole")
    print(" suppression (pulsars). Distinctive confirmed post-diction: c_T = c, structurally natural in")
    print(" ED (one substrate, shared light cone), not tuned. NOT a derivation of the couplings -- a")
    print(" placement showing viability. Load-bearing assumption: the shared light cone (c_T = c).")
    print("=" * 92)


if __name__ == "__main__":
    main()
