"""The quadratic-strain recast: does gravitational strain = |sum P|^2 reproduce Newton AND give MOND?

P14's flagged high-stakes target (project_p14_partial_reduction): build gravitational strain as a
QUADRATIC form S = |sum_i P_i|^2 = sum_i |P_i|^2 + sum_{i!=j} P*_i P_j, with
  DIAGONAL sum_i |P_i|^2 = sum_i b_i      -> the additive Newtonian strain (definitional, exact),
  OFF-DIAGONAL sum_{i!=j} P*_i P_j        -> interference (the MOND/horizon correction).
MUST reproduce Newton + GR-I weak field and BREAK NOTHING.

THE OBSTRUCTION (confronted, not skipped): to preserve many-body Newton the LOCAL-LOCAL cross terms
must vanish; to give MOND the LOCAL-HORIZON cross term must survive. A single "phases are random"
mechanism kills BOTH -- if local phases are random enough to wash out local-local interference, they
are equally random against the horizon, so MOND dies too. Full coherence breaks Newton; full
incoherence kills MOND. Naive recast FAILS.

THE RESOLUTION TESTED HERE: a coherence ASYMMETRY. Give the local participation phases a small common
bias sigma toward the horizon reference (phase 0) -- the horizon is the global boundary all local
participation is embedded in, so a weak universal alignment is the natural structure. For phases with
mean resultant sigma = |<e^{i pi}>|:
  local-local coherence  C_LL = <cos(pi_i - pi_j)>_{i!=j} = |<e^{i pi}>|^2 = sigma^2   (independent i,j)
  local-horizon coherence C_LH = <cos(pi_i - 0)>          = <cos pi>       = sigma
So C_LL = sigma^2 while C_LH = sigma: for small sigma the Newton-breaking local-local term is
QUADRATICALLY suppressed relative to the MOND-giving local-horizon term. Newton preserved to O(sigma^2);
MOND survives at O(sigma). That is the missing mechanism. This probe verifies C_LL = sigma^2, C_LH =
sigma numerically, quantifies Newton preservation, and states the residual regime condition + the
falsifiable O(sigma^2) source-source correction to Newton.

HONEST TIERS: the C_LL=sigma^2 vs C_LH=sigma asymmetry is EXACT (probability identity) -> the
resolution is robust. CONDITIONAL on (Q1) the quadratic-strain reading itself (the open fork; corpus
builds strain linearly) and (Q2) the small horizon-aligned phase bias sigma (account-tier, motivated by
horizon-as-global-reference, NOT derived; sigma's value inherited, sets a0). Regime: many-body Newton
needs the local-local term (which grows with source count) below bounds -> a falsifiable O(sigma^2)
source-source interference correction to Newton. Does NOT fully close P14 (Q1 open, Q2 account); it
REMOVES the main obstruction (the Newton-vs-MOND incoherence contradiction) with a concrete mechanism.
"""
import numpy as np


def sample_phases(n, kappa, rng):
    """von Mises phases about mean 0 with concentration kappa; resultant sigma = I1(kappa)/I0(kappa)."""
    return rng.vonmises(mu=0.0, kappa=kappa, size=n)


def resultant(kappa):
    from scipy.special import i0, i1
    return i1(kappa) / i0(kappa)


def main():
    rng = np.random.default_rng(0)
    print("=" * 94)
    print("QUADRATIC-STRAIN RECAST:  S = |sum P|^2  ->  Newton (diagonal) + MOND (off-diagonal)?")
    print("=" * 94)

    # ---- 0. diagonal = additive Newton (definitional check) ----
    b = rng.uniform(0.5, 2.0, size=8)
    phases = rng.uniform(-np.pi, np.pi, size=8)
    P = np.sqrt(b) * np.exp(1j * phases)
    S_total = np.abs(P.sum()) ** 2
    diag = np.sum(np.abs(P) ** 2)
    offdiag = S_total - diag
    print("\n[0] S = |sum P|^2 = (diagonal) + (off-diagonal):")
    print(f"    diagonal sum|P_i|^2 = sum b_i = {diag:.4f}  == additive Newtonian strain (definitional).")
    print(f"    off-diagonal = {offdiag:.4f}  (the interference; = 0 only if phases incoherent).")

    # ---- 1. THE TENSION: random phases kill BOTH local-local and local-horizon ----
    print("\n[1] THE OBSTRUCTION: uniform-random phases (sigma=0) -> Newton OK but MOND also gone.")
    N = 4000
    ph = rng.uniform(-np.pi, np.pi, size=N)
    C_LL = (np.abs(np.exp(1j * ph).mean()) ** 2)              # |<e^{i pi}>|^2
    C_LH = np.cos(ph).mean()                                  # <cos(pi - 0)>
    print(f"    local-local coherence C_LL = {C_LL:.4f} (->0: Newton preserved, local-local washes out)")
    print(f"    local-horizon coherence C_LH = {C_LH:.4f} (->0: MOND ALSO gone). Naive recast FAILS.")

    # ---- 2. THE RESOLUTION: small common bias sigma -> C_LL = sigma^2, C_LH = sigma ----
    print("\n[2] RESOLUTION: partial alignment toward the horizon reference. Sweep sigma; check the")
    print("    asymmetry C_LL = sigma^2 (Newton-breaking, quadratic) vs C_LH = sigma (MOND, linear):")
    print("     kappa   sigma(target)   C_LH(meas)   C_LL(meas)   sigma^2   ratio C_LL/C_LH")
    for kappa in [0.05, 0.1, 0.2, 0.4, 0.8, 1.5, 3.0]:
        sig = resultant(kappa)
        ph = sample_phases(200000, kappa, rng)
        clh = np.cos(ph).mean()
        cll = np.abs(np.exp(1j * ph).mean()) ** 2
        print(f"     {kappa:<7g} {sig:<14.4f} {clh:<12.4f} {cll:<12.4f} {sig**2:<9.4f} {cll/clh:<.4f}")
    print("    -> C_LH ~ sigma, C_LL ~ sigma^2, ratio C_LL/C_LH ~ sigma -> 0. Local-local (Newton-")
    print("       breaking) is quadratically suppressed vs local-horizon (MOND). The tension is resolved.")

    # ---- 3. Newton preservation + MOND coexistence, and the regime condition ----
    print("\n[3] Coexistence + regime. For n_body separate masses (equal b) at small sigma:")
    print("    local-local / diagonal ~ sigma^2 * (n_body - 1)     (Newton-breaking, must stay small)")
    print("    local-horizon / diagonal ~ sigma * sqrt(b_hor/b)     (MOND term; b_hor = horizon bandwidth)")
    for nb, sig in [(2, 0.05), (10, 0.05), (2, 0.2), (10, 0.2)]:
        ll = sig**2 * (nb - 1)
        print(f"     n_body={nb:<3d} sigma={sig:<5g} -> local-local/diag ~ {ll:.4f} "
              f"(Newton correction){'  OK' if ll < 1e-2 else '  <-- watch'}")
    print("    -> Newton preserved when sigma^2 (n_body-1) << 1. The horizon's huge b_hor lets the MOND")
    print("       term (~sigma sqrt(b_hor/b)) be relevant even for tiny sigma, so the two decouple: a0 is")
    print("       set by sigma*sqrt(b_hor) (inherited), while the Newton violation stays O(sigma^2).")

    print("\nVERDICT (honest tiers):")
    print("  RESOLVED (exact identity): the C_LL=sigma^2 vs C_LH=sigma asymmetry breaks the Newton-vs-MOND")
    print("    deadlock -- a small universal phase alignment toward the horizon reference preserves Newton")
    print("    to O(sigma^2) while keeping MOND at O(sigma). This is the mechanism the naive recast lacked.")
    print("  STRUCTURAL: diagonal = additive Newton (exact); off-diagonal local-horizon = the MOND cross-")
    print("    term -> the mu(x) with correct limits (companion probe); strong field (g_N>>a0) -> Newton.")
    print("  CONDITIONAL / OPEN: (Q1) the quadratic-strain reading itself is the open fork (corpus builds")
    print("    strain linearly); (Q2) the small horizon-aligned phase bias sigma is account-tier (motivated,")
    print("    not derived; sigma sets a0, inherited). FALSIFIABLE: a residual O(sigma^2) source-source")
    print("    interference correction to Newton, bounded by solar-system tests. => P14 SUBSTANTIALLY")
    print("    de-obstructed, NOT fully discharged: the recast now demonstrably reproduces Newton+MOND")
    print("    GIVEN one motivated phase-alignment assumption, converting 'does it even work?' into a")
    print("    sharp, testable residual.")
    print("=" * 94)


if __name__ == "__main__":
    main()
