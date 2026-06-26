"""B4 / #2 — coherent/incoherent decomposition (testing AP's 'CG = arrow becomes entropy').

The maxwell_continuum_test averaged the DEFICIT (energy ~ (grad phi)^2) = coherent
field energy + incoherent trapped disorder, and reported the SUM as non-Coulomb.
AP's reframe: coarse-graining forgets the arrow, which should RELOCATE to entropy --
the trapped incoherence IS the thermodynamic content, and the COHERENT part may be
clean Maxwell/Coulomb. The real world has both: Coulomb fields AND entropy.

Test: separate them. Ensemble-average the FIELD itself, Z = <e^{i phi}>:
  - coherent field   Phi = angle(Z)          -> its deficit*r^2 ~ const = COULOMB?
  - coherence        |Z| in [0,1]            (1 = fully coherent, 0 = incoherent)
  - incoherence      1 - |Z|                 = the ENTROPY (the arrow's thermo form)

If the COHERENT field is Coulomb, then CGing ED gives Maxwell (coherent) + entropy
(incoherent) -- AP's answer, not a problem. If even the coherent field is non-Coulomb,
the arrow genuinely contaminates the field -- a real deviation.
"""
from __future__ import annotations
import numpy as np

from relaxation_test import boundary_mask_and_field, mod_B_relax
from maxwell_continuum_test import randomized_commit, deficit_field, radial


def coherent_decomp(L, w, c, Nens, seed0=2000):
    Z = np.zeros((L, L), dtype=complex)
    for s in range(Nens):
        phi = randomized_commit(L, w, c, seed=seed0 + s)
        Z += np.exp(1j * phi)
    Z /= Nens
    Phi = np.angle(Z)        # coherent field
    coh = np.abs(Z)          # coherence in [0,1]
    return Phi, coh


def main():
    L, w, c = 61, 1, 30
    radii = [3, 6, 12, 24]
    print("=" * 78)
    print(f"B4 / #2 — coherent/incoherent decomposition  L={L}, w={w}")
    print("  (does the COHERENT part of the CG'd field = Coulomb, with incoherence = entropy?)")
    print("=" * 78)

    # Maxwell reference
    bM = mod_B_relax(L, w, c, iters=4000, seed=1)
    raM = radial(deficit_field(bM), c, radii)
    print("\n[Maxwell ref]  Mod-B XY relaxation deficit*r^2 = [" +
          " ".join(f"{t[3]:.3f}" for t in raM) + "]  (Coulomb ~ const 0.126)")

    ys, xs = np.mgrid[0:L, 0:L]
    r = np.sqrt((xs - c) ** 2 + (ys - c) ** 2)

    print("\n  N    coherent-field deficit*r^2          mean|coherence|   incoherence(1-|Z|) by r")
    for Nens in (8, 32, 128):
        Phi, coh = coherent_decomp(L, w, c, Nens)
        # coherent-field deficit (Maxwell candidate)
        dC = deficit_field(Phi)
        raC = radial(dC, c, radii)
        # incoherence radial profile (entropy candidate)
        inc = 1.0 - coh
        inc_r = [float(inc[(r >= rr-1) & (r < rr+1)].mean()) for rr in radii]
        cohmean = float(coh[(r > 3) & (r < 0.45*L)].mean())
        print(f"  {Nens:>3}  [" + " ".join(f"{t[3]:.3f}" for t in raC) + "]" +
              f"     {cohmean:.3f}        [" + " ".join(f"{v:.3f}" for v in inc_r) + "]")

    print("\n" + "-" * 78)
    print("READ:")
    print("  - coherent-field deficit*r^2 FLAT (~0.13 like Mod-B) -> the COHERENT part IS")
    print("    Coulomb: CGing ED gives Maxwell (coherent) + entropy (incoherence). AP's answer.")
    print("  - coherent-field deficit*r^2 still NOT flat -> the arrow contaminates the field")
    print("    itself, not just adds entropy: a real deviation from Maxwell. My 'problem'.")
    print("  - incoherence(1-|Z|): if it falls toward 0 at large r, the far field is coherent")
    print("    (clean Coulomb far away); if it stays high, disorder pervades.")
    print("-" * 78)
    return True


if __name__ == "__main__":
    import sys
    sys.exit(0 if main() else 1)
