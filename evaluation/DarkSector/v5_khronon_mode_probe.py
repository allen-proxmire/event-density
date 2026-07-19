"""Khronon-mode probe (dark-sector / superfluid-relic program) -- the decisive unification test.

QUESTION: does the V5-condensed relic's collective mode reproduce the MOND force (the khronon),
or a standard (Newtonian) force?

METHOD: the effective field theory of the condensed phase phi is read off its energy cost under
an imposed uniform gradient k. Kinetic term ~ |grad phi|^p:
    p = 2  ->  standard: EOM grad^2 phi = rho  (Poisson) -> NEWTONIAN (1/r^2 force).
    p = 3  ->  AQUAL/deep-MOND: div(|grad phi| grad phi) = rho -> MOND (a = sqrt(a_N a0)).
So the exponent p in DeltaE(k) ~ k^p decides it directly.

REAL V5 functional (ChiralGauge/homochirality_v5_verify.py, Paper_090):
    E(k) = -sum_{i<j} w(r_ij) cos(phi_i - phi_j),  w=exp(-r/ell),  phi_i = k * x_i  (uniform gradient).
No time, static; positions fixed; relics condensed (phases set by the gradient).
"""
import numpy as np


def energy(pos, W_upper, dx, k):
    # E = -sum_{i<j} w_ij cos(k * dx_ij)   (only upper-triangle pairs)
    return -float(np.sum(W_upper * np.cos(k * dx)))


def main():
    rng = np.random.default_rng(1)
    N, L, ell = 400, 4.0, 1.0
    pos = rng.uniform(0.0, L, (N, 3))
    d = pos[:, None, :] - pos[None, :, :]
    r = np.linalg.norm(d, axis=2)
    W = np.exp(-r / ell)
    iu = np.triu_indices(N, 1)
    W_upper = W[iu]
    dx = d[iu][:, 0]                 # coordinate difference along the gradient direction

    ks = np.array([0.03, 0.05, 0.08, 0.12, 0.2, 0.3, 0.5, 0.8, 1.2])
    E0 = energy(pos, W_upper, dx, 0.0)
    dE = np.array([energy(pos, W_upper, dx, k) - E0 for k in ks])

    print("V5-condensed collective mode: energy cost of an imposed phase gradient k.\n")
    print("   k :  " + "  ".join(f"{k:5.2f}" for k in ks))
    print("  dE :  " + "  ".join(f"{e:6.2f}" for e in dE))

    # local log-log slope p(k) = d ln dE / d ln k
    lnk, lndE = np.log(ks), np.log(dE)
    p_small = np.polyfit(lnk[:4], lndE[:4], 1)[0]   # deep (small-gradient) regime
    p_all = np.polyfit(lnk, lndE, 1)[0]

    print(f"\n  exponent p (small k, 'deep' regime): {p_small:.2f}")
    print(f"  exponent p (full range):             {p_all:.2f}")
    print("\n" + "=" * 74)
    print("READ:  p=2 -> standard kinetic term -> Poisson -> NEWTONIAN (not MOND).")
    print("       p=3 -> AQUAL/non-analytic     -> deep-MOND (a = sqrt(a_N a0)).")
    if abs(p_small - 2.0) < 0.3:
        verdict = ("STANDARD (Newtonian). The V5-condensed collective mode does NOT reproduce MOND: "
                   "its kinetic term is the generic |grad phi|^2, which gives a Newtonian force, "
                   "not the non-analytic sqrt structure MOND requires.")
    elif abs(p_small - 3.0) < 0.4:
        verdict = "MOND-LIKE. The condensed mode has the AQUAL structure -- it could BE the khronon."
    else:
        verdict = f"NON-STANDARD (p={p_small:.2f}); needs interpretation."
    print("  VERDICT:", verdict)
    print("=" * 74)


if __name__ == "__main__":
    main()
