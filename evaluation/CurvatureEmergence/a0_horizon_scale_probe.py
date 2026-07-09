"""a0, the MOND scale: is it forced to be a horizon (cosmological) acceleration scale in ED's recast?

In the quadratic-strain recast, MOND is literally the local-vs-cosmic-HORIZON interference sector: the
off-diagonal cross-term between the local field and the horizon reference. So the MOND ONSET (where the
cross-term becomes comparable to the local Newtonian diagonal, g_N ~ a0) is where the local acceleration
drops to the HORIZON's own acceleration scale. The horizon is ED's b->0 SCBU boundary at R_H ~ c/H0; the
only acceleration you can build from c and R_H is c^2/R_H = c H0. So a0 ~ c^2/R_H = c H0 is FORCED by the
mechanism (a0 is a horizon scale, not a new local constant), which is the deep content of the observed
"a0 ~ c H0" coincidence: in ED it is not a coincidence, the horizon IS the MOND interference partner.

HONEST SEPARATION (crank-rail; a0 ~ cH0 is a KNOWN, near-generic result for any horizon-based MOND):
 - ED-SPECIFIC (the contribution): the recast's mechanism FORCES a0 to be the horizon acceleration scale
   (MOND = local-horizon interference), so a0 cosmological is structural, not fitted.
 - GENERIC (NOT an ED discovery): the numerical fact a0 ~ cH0 itself; many frameworks reach it.
 - NOT DERIVED (numerology risk, flagged): the exact O(1) factor (observed a0 ~ cH0/2pi ~ cH0/6).

This probe computes the numbers, shows a0 ~ cH0 within an O(1) factor of a few, and states the tiers +
the falsifiable handle (does a0 track the horizon -> redshift/Lambda dependence?).
"""
import numpy as np

# constants (SI)
c = 2.998e8                      # m/s
Mpc = 3.086e22                   # m
H0_kms_Mpc = 67.4                # km/s/Mpc (Planck-ish)
H0 = H0_kms_Mpc * 1e3 / Mpc      # s^-1
a0_obs = 1.2e-10                 # m/s^2 (MOND, McGaugh)
Lambda = 1.1e-52                 # m^-2 (cosmological constant, ~ 3 Omega_L H0^2 / c^2)


def main():
    print("=" * 92)
    print("a0 as a HORIZON acceleration scale:  is a0 ~ c^2/R_H = c H0 forced by the recast?")
    print("=" * 92)

    R_H = c / H0                                  # Hubble radius
    cH0 = c * H0                                  # = c^2 / R_H exactly
    c2_over_RH = c**2 / R_H
    a_dS = c**2 * np.sqrt(Lambda / 3.0)           # de Sitter / Lambda horizon acceleration scale

    print(f"\n  H0            = {H0:.3e} s^-1   ({H0_kms_Mpc} km/s/Mpc)")
    print(f"  R_H = c/H0    = {R_H:.3e} m")
    print(f"  a0 (observed) = {a0_obs:.3e} m/s^2")
    print(f"  c H0 = c^2/R_H= {cH0:.3e} m/s^2   (identical: c^2/R_H = c H0 = {c2_over_RH:.3e})")
    print(f"  c^2 sqrt(L/3) = {a_dS:.3e} m/s^2   (de Sitter / Lambda-horizon scale)")

    print("\n  RATIOS (the O(1) factor that is NOT derived):")
    print(f"    a0 / (c H0)        = {a0_obs/cH0:.4f}   ~ 1/{cH0/a0_obs:.1f}   (compare 1/(2pi)={1/(2*np.pi):.4f}, 1/6={1/6:.4f})")
    print(f"    a0 / (c H0/2pi)    = {a0_obs/(cH0/(2*np.pi)):.4f}   (=1 would be exact a0 = cH0/2pi)")
    print(f"    a0 / (c^2 sqrt(L/3))= {a0_obs/a_dS:.4f}   ~ 1/{a_dS/a0_obs:.1f}")

    print("\n  STRUCTURAL RESULT (ED-specific, the contribution):")
    print("    In the recast MOND = local-vs-horizon interference, so the MOND ONSET (g_N ~ a0) is where")
    print("    the local acceleration falls to the HORIZON's own acceleration scale. The horizon is ED's")
    print("    b->0 boundary at R_H; the only acceleration from c and R_H is c^2/R_H = c H0. So a0 ~ c H0")
    print("    is FORCED by the mechanism -- a0 is a HORIZON scale, not a new local constant. That is the")
    print("    content of the 'a0 ~ c H0' coincidence: in ED it is not a coincidence.")

    print("\n  HONEST TIERS:")
    print("    GROUNDED (ED-specific): a0 is cosmological/horizon-set (the recast's MOND is the horizon")
    print("      interference sector) -> a0 ~ c^2/R_H ~ c H0 is STRUCTURAL, not fitted. This explains WHY")
    print("      the MOND scale is tied to the universe's size (the standard deep puzzle).")
    print(f"    ORDER-OF-MAGNITUDE (predicted): a0 ~ c H0 to within an O(1) factor (~1/{cH0/a0_obs:.0f}); MATCHES.")
    print("    GENERIC (NOT an ED discovery): the number a0 ~ c H0 itself -- near-automatic for horizon-MOND.")
    print("      The ED novelty is the MECHANISM (interference) forcing it, not the coincidence.")
    print("    NOT DERIVED (numerology risk, flagged): the exact O(1) factor (~1/2pi..1/6). Claiming it")
    print("      would be numerology; ED gives the SCALE, not the coefficient.")

    print("\n  FALSIFIABLE HANDLE:")
    print("    a0 is set by the cosmic horizon, so which horizon matters. If the HUBBLE horizon (R_H=c/H)")
    print("    -> a0(z) evolves (larger at high z, smaller horizon) -> testable vs high-z rotation curves/")
    print("    RAR (standard MOND: a0=const). If the de Sitter/Lambda (future) horizon -> a0 ~ const. ED")
    print("    must identify which its b->0 SCBU boundary is (open); either way a0 TRACKS a horizon, a")
    print("    distinguishing prediction from 'a0 is a fundamental constant.'")

    print("\n  VERDICT: a0 is CONVERTED from an inherited fundamental constant to a PREDICTED horizon")
    print("    acceleration scale (~c H0), because ED's MOND IS the local-horizon interference sector.")
    print("    The cosmic-coincidence puzzle is explained (structural), the magnitude matches within O(1),")
    print("    the exact factor stays open, and a0-tracks-a-horizon is a falsifiable handle. NOT a claim to")
    print("    have derived a0's number -- a grounding of its SCALE and ORIGIN.")
    print("=" * 92)


if __name__ == "__main__":
    main()
