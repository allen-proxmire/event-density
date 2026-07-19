"""Bound (not pin) the ED committed-relic mass from two-component consistency.

ED gives no relic mass value (Paper_MassWithoutMass -> binding mass, no numbers), so this
BOUNDS it from the requirements the two-component picture imposes, using standard
warm-dark-matter (WDM) free-streaming cosmology for the mass<->scale mapping (inherited,
not ED-specific). The ED content is the two CONSTRAINTS:

  UPPER mass bound (warmer side):  the relic must be DIFFUSE in galaxies, or it double-counts
      against MOND (which already fits galaxies with no dark particle). So its free-streaming
      must erase relic structure at/below galaxy scale (~1e12 Msun). Heavier = colder =
      shorter free-streaming = clumps in galaxies => an UPPER bound on the mass.

  LOWER mass bound (colder side):  the relic must CLUSTER at cluster scale (~1e14 Msun, the
      missing cluster mass) and be non-relativistic pressureless dust by recombination (the
      CMB peaks). Lighter = warmer = longer free-streaming = won't cluster / stays hot =>
      a LOWER bound on the mass.

Mass<->half-mode-scale (thermal WDM, standard; e.g. Schneider et al.):
    M_hm(m) ~ 2.7e11 * (m/keV)^(-10/3)  Msun/h        (structure suppressed BELOW M_hm)
Invert to get the mass that puts M_hm at a target halo scale.
"""
import numpy as np

A = 2.7e11   # Msun/h, half-mode mass normalization for thermal WDM
SLOPE = 10.0 / 3.0


def m_for_scale(M_hm):
    """keV mass whose half-mode (suppression) scale is M_hm [Msun]."""
    return (M_hm / A) ** (-1.0 / SLOPE)


def main():
    print("=" * 74)
    print("ED committed-relic mass: BOUND from two-component consistency")
    print("=" * 74)

    # target halo scales
    M_gal = 1e12    # galaxy scale: relic must be ERASED at/below this (diffuse in galaxies)
    M_grp = 1e13    # group scale
    M_clus = 1e14   # cluster scale: relic must still CLUSTER here

    m_gal = m_for_scale(M_gal)     # UPPER bound: erase galaxy-scale relic structure
    m_grp = m_for_scale(M_grp)
    m_clus = m_for_scale(M_clus)   # LOWER bound: still cluster at cluster scale

    print("\nMass that puts the WDM suppression scale AT a given halo mass:")
    for label, M, m in [("galaxy  ~1e12 Msun (UPPER bound: diffuse in galaxies)", M_gal, m_gal),
                        ("group   ~1e13 Msun", M_grp, m_grp),
                        ("cluster ~1e14 Msun (LOWER bound: still clusters here)", M_clus, m_clus)]:
        print(f"   {label:52s}  m ~ {m:5.2f} keV")

    print("\n" + "-" * 74)
    print(f"ALLOWED WINDOW (order-of-magnitude):  {m_clus:.2f}  <  m  <  {m_gal:.2f}  keV")
    print(f"  center ~ {np.sqrt(m_clus*m_gal):.2f} keV  -> a WARM (keV-scale) relic, i.e. WDM, not cold CDM.")
    print(f"  This coincides with the keV sterile-neutrino WDM candidate (neutral, warm).")
    print("-" * 74)

    # tension with ED's natural mass scales
    keV = 1.0
    GeV = 1e6 * keV
    m_planck = 1.22e19 * 1e6 * keV  # 1.22e19 GeV in keV
    m_center = np.sqrt(m_clus * m_gal)
    print("\nTENSION with ED's natural (inherited) mass scales (the live risk):")
    print(f"   required window center        ~ {m_center:.2f} keV")
    print(f"   baryon-sibling binding scale  ~ 1 GeV      = {GeV/keV:.0e} keV   ({np.log10(GeV/m_center):.0f} orders too heavy)")
    print(f"   substrate (Planck) scale      ~ 1.2e19 GeV = {m_planck/keV:.0e} keV   ({np.log10(m_planck/m_center):.0f} orders too heavy)")
    print("   => ED's mass MECHANISM leans cold/heavy; consistency DEMANDS warm/keV. That gap")
    print("      is the sector's live risk, now quantified.")

    print("\nWhat the bound is, honestly:")
    print("  * NOT a pin: ED derives no mass value; this is a window from consistency + WDM cosmology.")
    print("  * A falsifiable PREDICTION of direction: ED's dark sector must be WARM (~keV), not cold")
    print("    WIMP-like CDM. If DM is shown cold/heavy (WIMP) or perfectly cold, this picture fails.")
    print("  * Lyman-alpha CAVEAT (loosens the light side): the standard Ly-a bound (m_WDM > 3-5 keV)")
    print("    assumes the relic makes small-scale structure. In ED, MOND (not the relic) makes it,")
    print("    so that bound does NOT directly apply -- the relic may be warmer/lighter than Ly-a")
    print("    would otherwise allow. This ties the relic's viability to MOND's small-scale success.")
    print("  * Tremaine-Gunn fermionic floor ~ a few hundred eV is consistent with the window.")
    print("=" * 74)


if __name__ == "__main__":
    main()
