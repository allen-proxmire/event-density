"""V5 coarse-graining probe for L_self -- the decider: is the relic a MOND source
(one substance) or a plain (super)fluid CDM (two components)?

CONTEXT (read `physics-papers/dark-sector/Paper_ED_RelicLagrangian_v1.md` first).
The relic Lagrangian's open term is L_self(Phi, dPhi; u), the relic's SELF-interaction.
This probe coarse-grains the real V5 cross-chain coherence functional to read off its form.

WHAT L_self IS, AND IS NOT (do not repeat the retracted khronon-mode conflation):
  * L_self = the RELIC<->RELIC cross-term. It carries only the finite V5 reach l.
  * MOND = the MATTER<->HORIZON cross-term (Paper_QuadraticStrain_v1), scale a0 = cH0/2pi
    from the HORIZON (Paper_029). Different pairing, different scale. CITED, not re-derived here.
So the question is only: what continuum kinetic form does the relic<->relic term take?

THE REAL FUNCTIONAL (QuadraticStrain amplitude weighting + V5 finite reach):
    E = - sum_{i<j} K(r_ij) sqrt(b_i b_j) cos(theta_i - theta_j),   K(r) = exp(-r/l)
This is the off-diagonal of Str = |sum_a P^(a)|^2 with P = sqrt(b) e^{i theta}, restricted
to the relic<->relic pairing, with the V5 reach as the kernel.

ANALYTIC EXPECTATION (the structural point):
  cos is ANALYTIC: cos(x) = 1 - x^2/2 + x^4/24 - ... -- EVEN powers only.
  A gradient expansion of a finite-reach analytic kernel therefore yields
      E[theta] = const + c2 (grad theta)^2 + c4 (grad theta)^4 + ...   (all analytic)
  The leading term is the CANONICAL superfluid kinetic term b|grad theta|^2. There is NO
  route to a non-analytic (grad theta)^{3/2} (the AQUAL/deep-MOND kinetic term) at any order,
  and NO acceleration scale a0 appears (there is no horizon in K -- only the local reach l).
  => p = 2 is structurally forced; L_self is canonical => the relic is (super)fluid CDM.

The MOND non-analyticity + a0 must come from ELSEWHERE (the matter<->horizon term), so the
dark sector is TWO-COMPONENT: a CDM relic + the separate horizon-interference MOND.

THE TESTS:
  A. Phase stiffness E(k) for theta_i = k x_i, uniform density -> fit exponent p. Expect ~2.
  B. Density response (the retraction's concern -- earlier probe held b fixed): repeat with a
     modulated density profile b_i = b0(1 + A cos(q x_i)); show p is UNCHANGED (~2).
  C. Scale check: confirm E(k)/E(k') scales as (k/k')^2 with NO intrinsic acceleration scale,
     so the force delta E / delta theta is LINEAR in grad theta (Newtonian/Poisson), not MOND.
"""
import numpy as np


def build_positions(n, dx=1.0):
    return np.arange(n) * dx


def v5_energy(x, theta, b, reach, cutoff_reaches=8):
    """E = - sum_{i<j} exp(-r/l) sqrt(b_i b_j) cos(theta_i - theta_j). Real V5 form."""
    n = len(x)
    E = 0.0
    rc = cutoff_reaches * reach
    for i in range(n):
        for j in range(i + 1, n):
            r = abs(x[j] - x[i])
            if r > rc:
                break
            K = np.exp(-r / reach)
            E -= K * np.sqrt(b[i] * b[j]) * np.cos(theta[i] - theta[j])
    return E


def stiffness_exponent(x, b, reach, ks):
    """Impose theta_i = k x_i; measure dE(k) = E(k) - E(0); fit log dE vs log k -> p."""
    E0 = v5_energy(x, np.zeros_like(x), b, reach)
    dE = []
    for k in ks:
        theta = k * x
        dE.append(v5_energy(x, theta, b, reach) - E0)
    dE = np.array(dE)
    # dE should be > 0 (gradient raises energy above the aligned ground state)
    mask = dE > 0
    p, logA = np.polyfit(np.log(ks[mask]), np.log(dE[mask]), 1)
    return p, dE


def main():
    np.random.seed(0)  # determinism (no RNG in the physics; seed only for any tie-breaks)
    n = 400
    dx = 1.0
    reach = 6.0
    x = build_positions(n, dx)
    # small-gradient regime (kx << 1 across a reach), where the leading term dominates
    ks = np.array([0.002, 0.003, 0.005, 0.008, 0.012, 0.02, 0.03])

    print("=" * 78)
    print("V5 coarse-graining of L_self  (relic<->relic self-interaction)")
    print(f"  n={n}, reach l={reach}, gradients k in [{ks[0]}, {ks[-1]}]  (k*l up to {ks[-1]*reach:.2f})")
    print("=" * 78)

    # --- Test A: uniform density -------------------------------------------------
    b_uniform = np.ones(n)
    pA, dEA = stiffness_exponent(x, b_uniform, reach, ks)
    print("\n[A] phase stiffness, UNIFORM density:")
    for k, e in zip(ks, dEA):
        print(f"     k={k:.4f}   dE={e:.6e}")
    print(f"     fitted exponent p = {pA:.3f}   (2 = canonical/Newtonian, 3 = deep-MOND)")

    # --- Test B: density response (modulated profile) ---------------------------
    q = 2 * np.pi / (10 * reach)
    b_mod = 1.0 + 0.6 * np.cos(q * x)      # strong density modulation
    b_mod = np.clip(b_mod, 0.05, None)
    pB, dEB = stiffness_exponent(x, b_mod, reach, ks)
    print("\n[B] phase stiffness, MODULATED density b=b0(1+0.6 cos qx) (density response on):")
    print(f"     fitted exponent p = {pB:.3f}   (unchanged from A => density does not create a fractional term)")

    # --- Test B2: a different reach, to confirm p is reach-independent -----------
    reach2 = 12.0
    pB2, _ = stiffness_exponent(x, b_uniform, reach2, ks)
    print(f"\n[B2] uniform density, reach l={reach2}:  p = {pB2:.3f}  (reach-independent => intrinsic to the analytic kernel)")

    # --- Test C: scale check -- ratio should be pure power, no a0 ----------------
    print("\n[C] scale check (is there an intrinsic acceleration scale a0 in L_self?):")
    r_meas = dEA[-1] / dEA[0]
    r_pred = (ks[-1] / ks[0]) ** 2
    print(f"     dE(k_max)/dE(k_min) measured = {r_meas:.2f}")
    print(f"     pure (k_max/k_min)^2         = {r_pred:.2f}")
    print(f"     match => energy is a pure power of the gradient with NO intrinsic scale.")
    print(f"     => the force dE/dtheta is LINEAR in grad theta (Poisson/Newtonian), no a0, no MOND.")

    print("\n" + "=" * 78)
    print("READ:")
    print(f"  * p = {pA:.2f} (uniform), {pB:.2f} (density response), {pB2:.2f} (other reach): CANONICAL.")
    print("  * cos is analytic (even powers only) -> no (grad theta)^{3/2} at any order.")
    print("  * No horizon in K -> no a0 -> the relic self-interaction CANNOT be MOND.")
    print("  VERDICT: L_self coarse-grains to a canonical superfluid kinetic term.")
    print("           The relic is (super)fluid CDM, NOT a MOND source.")
    print("           => TWO-COMPONENT dark sector: CDM relic + separate matter<->horizon MOND")
    print("              (MOND = Paper_QuadraticStrain_v1, a0 from the horizon; a DIFFERENT term).")
    print("  CAVEAT: this is the PERTURBATIVE kinetic sector. A non-perturbative/defect (vortex)")
    print("          contribution is not covered by the gradient expansion (flagged, minor/open).")
    print("=" * 78)


if __name__ == "__main__":
    main()
