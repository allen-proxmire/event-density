"""Consistency check: does the horizon-aligned phase bias sigma (required by the quadratic-strain
recast) break the QM / gauge phase sector (P09, double-slit, U(1) gauge invariance)?

The recast (quadratic_strain_recast_probe) needs local participation phases to carry a small common
bias sigma toward the horizon reference (phase 0), to give local-local coherence sigma^2 (Newton-safe)
and local-horizon coherence sigma (MOND). WORRY: a universal preferred phase could (a) break global
U(1) gauge invariance / make the global phase observable, or (b) shift double-slit interference.

THE RESOLUTION TO TEST: sigma is a source-HORIZON RELATIVE-phase coherence. It is gauge-invariant
(a global phase rotation shifts source AND horizon equally -> sigma unchanged), and it is invisible to
LOCAL interference IF the horizon-bias is smooth on local scales (two co-local paths share the same
bias, which cancels in their relative phase Delta pi). That smoothness is the SAME assumption the
recast already needs (it is why local-local cross-terms are sigma^2-suppressed). One assumption, both
consequences. Then: global phase stays unobservable; local gauge invariance is untouched (a global
reference is not a local breaking -> no photon mass); double-slit visibility is unchanged; the sigma
effect appears ONLY in the local-vs-horizon (different-scale) relative phase = MOND.

MODEL: a phase is pi = pi_loc(location's horizon-biased common phase) + delta(path/intrinsic phase).
 - pi_loc is biased toward the horizon reference 0 with resultant sigma (von Mises), and is COMMON to
   co-local paths (smooth horizon coupling).
 - delta is the path-specific / intrinsic phase (slit geometry, gauge-dependent), independent of sigma.

TESTS:
 1. DOUBLE-SLIT: two co-local paths A,B share pi_loc; visibility V=|<e^{i(pi_A-pi_B)}>| depends only on
    delta_A-delta_B -> INVARIANT to sigma (the horizon bias cancels). Contrast: if the bias did NOT
    cancel (paths biased differently), V would change -> shows the cancellation is load-bearing.
 2. GAUGE INVARIANCE: global phase rotation pi->pi+theta on sources AND horizon leaves sigma (source-
    horizon coherence), V (double-slit), and the MOND cross-term all invariant -> global phase
    unobservable, no gauge breaking.
 3. SCALE-SELECTIVITY: the sigma cross-term between two amplitudes scales with the DIFFERENCE of their
    horizon-couplings. Co-local (same coupling) -> 0 (QM/Newton safe). Local-vs-horizon (max diff) ->
    full sigma (MOND). So the sigma effect is confined to the cosmological-scale relative phase.

HONEST TIER: consistency HOLDS given the horizon-bias is smooth on local scales (co-local systems share
it) -- the SAME assumption the recast needs. Residual (flagged, not resolved): a possible tiny
preferred-phase effect in the EM sector (photon in a global phase reference); argued not a local-gauge
breaking (global != local, no photon mass) and sigma-suppressed, but not fully worked out.
"""
import numpy as np
from scipy.special import i0, i1


def resultant(kappa):
    return i1(kappa) / i0(kappa)


def main():
    rng = np.random.default_rng(0)
    N = 400000
    print("=" * 94)
    print("QM / GAUGE CONSISTENCY of the horizon-aligned phase bias sigma (the recast's assumption)")
    print("=" * 94)

    # ---- 1. DOUBLE-SLIT visibility is invariant to sigma (co-local paths share the horizon bias) ----
    print("\n[1] DOUBLE-SLIT: two co-local paths A,B. pi = pi_loc(horizon-biased, COMMON) + delta(path).")
    print("    Visibility V = |<e^{i(pi_A - pi_B)}>| should depend only on delta_A-delta_B (bias cancels).")
    # fixed path-phase offset between slits (the interference-carrying relative phase), plus small jitter
    dslit_offset = 0.8                              # the physical slit relative phase
    delta_A = rng.normal(0.0, 0.2, N)
    delta_B = rng.normal(-dslit_offset, 0.2, N)     # B has a systematic path offset
    print("     sigma(bias)   V (bias COMMON to A,B)   V (bias DIFFERENT: not co-local)   V_ideal(no bias)")
    for kappa in [0.0, 0.2, 0.8, 2.0, 5.0]:
        sig = resultant(kappa) if kappa > 0 else 0.0
        pil = rng.vonmises(0.0, kappa, N) if kappa > 0 else np.zeros(N)   # common horizon-biased phase
        # (a) co-local: A and B share the SAME pi_loc -> cancels in the difference
        piA = pil + delta_A
        piB = pil + delta_B
        V_common = np.abs(np.mean(np.exp(1j * (piA - piB))))
        # (b) NOT co-local: A and B get INDEPENDENT horizon biases (wrong physics, for contrast)
        pil2 = rng.vonmises(0.0, kappa, N) if kappa > 0 else np.zeros(N)
        V_diff = np.abs(np.mean(np.exp(1j * ((pil + delta_A) - (pil2 + delta_B)))))
        # ideal: no bias at all
        V_ideal = np.abs(np.mean(np.exp(1j * (delta_A - delta_B))))
        print(f"     {sig:<13.4f} {V_common:<24.4f} {V_diff:<34.4f} {V_ideal:.4f}")
    print("    -> V(bias common) == V(no bias): sigma is INVISIBLE to co-local double-slit interference.")
    print("       V(bias different) DROPS: confirms the cancellation (co-local shared bias) is load-bearing.")

    # ---- 2. GAUGE INVARIANCE: global phase rotation leaves everything invariant ----
    print("\n[2] GAUGE INVARIANCE: rotate ALL phases (sources + horizon) by theta. Observables invariant?")
    kappa = 1.0
    sig = resultant(kappa)
    pil = rng.vonmises(0.0, kappa, N)
    piloc = pil + rng.normal(0, 0.2, N)             # a local source phase
    for theta in [0.0, 0.7, 2.5]:
        # source-horizon coherence sigma: horizon ref shifts by theta too
        s = np.abs(np.mean(np.exp(1j * ((piloc + theta) - (0.0 + theta)))))
        # double-slit V (both paths + nothing external): shift cancels in the difference
        V = np.abs(np.mean(np.exp(1j * ((pil + delta_A + theta) - (pil + delta_B + theta)))))
        # MOND cross-term (source vs horizon), both shifted
        mond = np.mean(np.cos((piloc + theta) - (0.0 + theta)))
        print(f"     theta={theta:<5g}: source-horizon coh={s:.4f}   double-slit V={V:.4f}   MOND cross={mond:.4f}")
    print("    -> all invariant under global rotation: the global phase stays UNOBSERVABLE, sigma is a")
    print("       gauge-invariant source-horizon RELATIVE coherence, no global-U(1) breaking. Local gauge")
    print("       invariance is untouched (a global reference is not a local rotation -> no photon mass).")

    # ---- 3. SCALE-SELECTIVITY: co-local pair (shared bias cancels) vs local-horizon pair (bias survives) ----
    print("\n[3] SCALE-SELECTIVITY: does the coherent sigma cross-term survive? Depends on whether the two")
    print("    amplitudes SHARE the horizon bias (co-local -> cancels) or not (local-vs-horizon -> survives).")
    print("    Sweep sigma; report the coherent cross-term for each pairing (should be sigma-INDEPENDENT for")
    print("    co-local, and ~sigma for local-vs-horizon):")
    intr_A = rng.uniform(-np.pi, np.pi, N)          # intrinsic (gauge/path) phases, independent uniform
    intr_B = rng.uniform(-np.pi, np.pi, N)
    print("     sigma     co-local pair <cos(dPi)>   local-horizon pair <cos(dPi)>")
    for kappa in [0.0, 0.2, 0.8, 2.0, 5.0]:
        sig = resultant(kappa) if kappa > 0 else 0.0
        pil = rng.vonmises(0.0, kappa, N) if kappa > 0 else rng.uniform(-np.pi, np.pi, N)
        # co-local pair: BOTH carry the SAME horizon bias pil (+ independent intrinsic) -> pil cancels
        colocal = np.mean(np.cos((pil + intr_A) - (pil + intr_B)))
        # local-horizon pair: source (pil, horizon-biased) vs horizon reference (phase 0) -> bias survives
        localhor = np.mean(np.cos(pil - 0.0))
        print(f"     {sig:<9.4f} {colocal:<24.4f} {localhor:.4f}")
    print("    -> co-local cross-term is ~0 and sigma-INDEPENDENT (shared bias cancels: QM/Newton safe);")
    print("       local-horizon cross-term tracks sigma (the MOND term). The sigma effect is confined to")
    print("       the local-vs-cosmological relative phase, exactly where MOND lives.")

    print("\nVERDICT (honest tiers):")
    print("  CONSISTENT: sigma is a gauge-invariant source-HORIZON relative-phase coherence. It is invisible")
    print("    to co-local double-slit interference (shared bias cancels in Delta pi), invariant under global")
    print("    phase rotation (global phase stays unobservable, no global-U(1) breaking), and does not touch")
    print("    LOCAL gauge invariance (a global reference is not a local rotation -> no photon mass). The")
    print("    sigma effect is confined to the local-vs-cosmological relative phase = the MOND sector.")
    print("  ONE ASSUMPTION, BOTH JOBS: the required smoothness of the horizon-bias on local scales (co-local")
    print("    systems share it) is the SAME assumption that makes the recast's local-local term sigma^2-")
    print("    suppressed. So QM-safety and Newton-safety come from one physical input, not two.")
    print("  RESIDUAL (flagged, not resolved): a possible tiny preferred-phase effect in the EM sector")
    print("    (photon in a global phase reference) -- argued not a local-gauge breaking and sigma-suppressed,")
    print("    but not fully worked out. => the recast's sigma-alignment PASSES the QM/gauge consistency")
    print("    check; the de-risk succeeds. It does NOT discharge (Q1) the quadratic-strain fork.")
    print("=" * 94)


if __name__ == "__main__":
    main()
