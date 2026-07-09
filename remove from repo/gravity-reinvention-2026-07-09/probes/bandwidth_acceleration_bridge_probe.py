"""Working the bandwidth<->acceleration bridge: does the interference-MOND mechanism survive it?

The many-body Newton tension hinges on sigma, which is fixed by the MOND onset (cross-term ~ diagonal).
The onset in the STRAIN (bandwidth) picture reads sigma ~ sqrt(b_loc/b_hor). Everything turns on what
'b_hor' (and 'b_loc') are counted in. This probe works it consistently and checks Newton-safety.

THREE COUNTINGS of the local source (a galaxy) vs the horizon:
  (A) BOTH by MASS  (participation count M/m_Pl): b_gal ~ 1e50,  b_hor ~ 1e61.
  (B) BOTH by AREA  (holographic surface count (R/l_P)^2): b_gal ~ 1e111, b_hor ~ 1e123.
  (X) MIX (galaxy mass, horizon area) -- the INCONSISTENT choice I used in the retracted 'resolution':
      b_gal ~ 1e50, b_hor ~ 1e123.
The cross-term sqrt(b_loc b_hor) lives on ONE shared bilocal channel (P14 single-carrier: one channel,
one bandwidth), so b_loc and b_hor MUST be the same kind of dof. (A) and (B) are consistent; (X) mixes a
bulk-mass dof with a boundary-area dof, which is NOT a single carrier -> if (X) is what you need, the
single-carrier premise (that gives interference at all, section 3) is broken. So (X) is not a physical option.

For each: sigma ~ sqrt(b_loc/b_hor) at onset, then the many-body Newton violation sigma^2 * N (N = sources).
Also the ACCELERATION picture (strain = field energy, S ~ g^2, onset at g_N ~ a0): there S_hor ~ a0^2 ~
S_loc at onset (since a0 IS the horizon acceleration and the onset is at g_N ~ a0), so cross/diagonal ~
2 sigma -> sigma ~ O(1). Independent route to the same conclusion.

VERDICT PREVIEW: consistent counting (A) or (B) gives sigma ~ 1e-6, at which a galaxy (N ~ 1e11 stars)
has sigma^2 N ~ 1 -> Newton FAILS. The acceleration picture gives sigma ~ O(1) -> fails worse. Only the
INCONSISTENT mix (X) gives sigma ~ 1e-37 (the retracted save), and (X) has no valid single-carrier channel.
So the interference-MOND mechanism FAILS the many-body Newton test under every consistent reading: it is
falsified as formulated. (The surviving MOND route is the companion khronometric SCALAR mode, a different
mechanism that does not rely on this source-horizon phase coherence.)
"""
import numpy as np

c = 2.998e8; G = 6.674e-11; Mpc = 3.086e22; H0 = 67.4e3 / Mpc
l_P = 1.616e-35; m_Pl = 2.176e-8; Msun = 1.989e30
R_H = c / H0
M_hor = c ** 3 / (G * H0)                 # Hubble mass
R_gal = 15e3 * 3.086e16                    # ~15 kpc in m
M_gal = 1e12 * Msun


def main():
    print("=" * 96)
    print("BANDWIDTH<->ACCELERATION BRIDGE: does interference-MOND survive a consistent counting?")
    print("=" * 96)

    b_hor_mass = M_hor / m_Pl
    b_hor_area = 4 * np.pi * (R_H / l_P) ** 2
    b_gal_mass = M_gal / m_Pl
    b_gal_area = 4 * np.pi * (R_gal / l_P) ** 2
    N_stars = 1e11

    print("\n counts:")
    print(f"   horizon: mass M_hor/m_Pl = {b_hor_mass:.1e}   area (R_H/l_P)^2 = {b_hor_area:.1e}")
    print(f"   galaxy : mass M_gal/m_Pl = {b_gal_mass:.1e}   area (R_gal/l_P)^2 = {b_gal_area:.1e}")

    print("\n [onset] sigma ~ sqrt(b_loc/b_hor); [Newton] sigma^2 * N_stars (N=1e11):")
    rows = [
        ("(A) BOTH MASS  (consistent)", b_gal_mass, b_hor_mass, True),
        ("(B) BOTH AREA  (consistent)", b_gal_area, b_hor_area, True),
        ("(X) galaxy MASS, horizon AREA (INCONSISTENT: no single carrier)", b_gal_mass, b_hor_area, False),
    ]
    for name, bl, bh, consistent in rows:
        sig = np.sqrt(bl / (4 * bh))
        viol = sig ** 2 * N_stars
        tag = ("NEWTON FAILS" if viol > 1e-2 else ("marginal" if viol > 1e-6 else "safe"))
        note = "" if consistent else "  <- not a valid single-carrier channel; MOND premise broken"
        print(f"   {name:<62} sigma={sig:.1e}  sigma^2 N={viol:.1e}  {tag}{note}")

    print("\n [acceleration picture] strain = field energy S~g^2; onset at g_N ~ a0:")
    print("   S_hor ~ a0^2 ~ S_loc at onset (a0 IS the horizon accel, onset at g_N~a0), so")
    print("   cross/diagonal|onset = 2 sigma sqrt(S_hor/S_loc) ~ 2 sigma ~ 1  =>  sigma ~ 0.5 (O(1)).")
    sig_acc = 0.5
    print(f"   sigma ~ {sig_acc}: two-body Newton violation ~ sigma^2 ~ {sig_acc**2:.2f} (25%) -> ruled out by ~1e-9.")
    print("   (section 6 of the paper independently gives 2 sigma = a0/cH0 ~ 0.18 -> sigma ~ 0.09, same order.)")

    print("\n [why the retracted save was fake] the only reading giving sigma ~ 1e-37 is the MIX (X),")
    print("   which counts the galaxy by mass and the horizon by area. Since a horizon's area = (its mass)^2,")
    print(f"   that mix inflates b_hor by ~{b_hor_area/b_hor_mass:.0e} relative to a consistent count -- a units")
    print("   artifact, not physics. And a mass-dof x area-dof geometric mean is not a single-carrier channel,")
    print("   so (X) also breaks the very premise (section 3) that produces interference. Incoherent either way.")

    print("\n VERDICT (held to the reverse-crank bar):")
    print("   Working the bridge CONSISTENTLY kills the interference-MOND mechanism on Newton:")
    print("   - (A)/(B) consistent counting: sigma ~ 1e-6, galaxy sigma^2 N ~ 1 -> NEWTON FAILS.")
    print("   - acceleration picture: sigma ~ O(1), even two-body Newton violated ~25% -> FAILS worse.")
    print("   - (X) the sigma~1e-37 save: a units mismatch AND breaks single-carrier -> not physical.")
    print("   So the source-horizon INTERFERENCE recast of MOND is FALSIFIED as formulated: the coherence")
    print("   that gives MOND (sigma) unavoidably gives an O(sigma^2) inter-mass Newton violation, and no")
    print("   consistent counting makes sigma both MOND-sized and Newton-safe.")
    print("   SURVIVING ROUTE: the companion khronometric SCALAR mode (a dynamical field, NOT source-horizon")
    print("   phase coherence) is a DIFFERENT mechanism and is not killed by this. ED-MOND, if viable, is")
    print("   the khronometric scalar, not the interference recast.")
    print("   ONLY (speculative, unbuilt) escapes: the horizon carries many independent phase channels and")
    print("   different local masses couple to different ones (decorrelating local-local while keeping local-")
    print("   horizon) -- but that would dilute MOND and is not demonstrated. Barring it, the recast is dead.")
    print("=" * 96)


if __name__ == "__main__":
    main()
