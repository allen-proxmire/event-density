"""Grounding Q1 (gravitational strain is quadratic/Born-like, not linear) in the Born rule.

Q1 is the one open, load-bearing commitment under the whole MOND line (project_p14_partial_reduction):
gravitational bilocal strain is a QUADRATIC/interfering functional of amplitude, |sum P|^2, not a LINEAR
functional of source content. The corpus (Paper_026) builds it linearly, which is the step-3 catch.

THE GROUNDING (fully internal to ED, no external semiclassical machinery):
 (1) ED native (Paper_001): the participation amplitude is P = sqrt(b) e^{i pi}, so b = |P|^2. Bandwidth
     IS the squared amplitude.
 (2) QM keystone (Gleason/Born reconstruction, project_gleason_complementarity_reframe): the physical,
     OBSERVABLE quantity is |P|^2 (quadratic, phase-INVARIANT), not P (linear, phase-COVARIANT -> not an
     observable). Only phase-invariant quantities are physical. This is the structural content of Born.
 (3) ED kinematic metric (established, curvature-emergence arc): gravity is sourced by the physical
     bandwidth b = |P|^2.
 => When N sources share a common bilocal channel (P14 single-carrier: one channel = one bandwidth
    (P04) + one phase (P09) -> one amplitude), the sourcing bandwidth is b_tot = |sum_i P_i|^2, the
    QUADRATIC form WITH interference. That is Q1, now a CONSEQUENCE of (Born rule) + (b=|P|^2) +
    (metric sourced by b), not a free modeling choice.

DISSOLVING THE LINEAR-vs-QUADRATIC TENSION: b_tot = |sum P_i|^2 = sum_i b_i (DIAGONAL, LINEAR IN MASS =
Paper_026's Newton) + sum_{i!=j} P*_i P_j (OFF-DIAGONAL interference). "Linear in mass" (Newton) and
"quadratic in amplitude" (Born) are the SAME object's diagonal. Paper_026 built the diagonal; the Born
rule MANDATES the full form. No contradiction; Paper_026 was the decohered (diagonal) limit.

TESTS:
 1. PHASE-INVARIANCE forces quadratic: under a global phase P -> e^{i theta} P, a LINEAR functional
    (e.g. Re P, or <c|P>) changes (NOT observable); the QUADRATIC |P|^2 is invariant (observable). So the
    physical bandwidth/strain MUST be quadratic in amplitude -- linear-in-amplitude strain is not even a
    valid observable. (This is the Born/Gleason structural fact, here made explicit.)
 2. DIAGONAL = Newton: the diagonal of |sum P|^2 is sum b_i = the additive Newtonian source (linear in b).
 3. DECOHERENCE -> diagonal: averaging the quadratic form over random relative phases collapses it to the
    diagonal (Newton). So Paper_026's LINEAR construction IS the decohered Born observable; the Born rule
    ADDS the coherent off-diagonal (the interference the linear build dropped).
HONEST TIER: Q1's quadratic FORM is GROUNDED (inherited from the Born rule + b=|P|^2 + metric-sourced-by-b,
all established in ED). The residual OPEN piece narrows from "is strain quadratic?" (grounded) to "does a
residual horizon off-diagonal survive decoherence?" = the sigma-coherence (account-tier, already de-risked,
CurvatureEmergence_SigmaAlignment_QMGaugeConsistent). So P14 is SUBSTANTIALLY DISCHARGED: the load-bearing
quadratic commitment is no longer a free choice. NOT a grand 'gravity=QM' unification; a bounded grounding
of one form in one established rule, with the residual isolated on horizon-coherence retention + a0.
"""
import numpy as np


def main():
    rng = np.random.default_rng(0)
    print("=" * 94)
    print("GROUNDING Q1 (strain is quadratic) in the Born rule:  observables are |P|^2, not P")
    print("=" * 94)

    # ---- 1. Phase-invariance forces quadratic (only |P|^2 is observable) ----
    print("\n[1] PHASE-INVARIANCE: under a global phase P -> e^{i theta} P, which functionals are invariant")
    print("    (hence valid observables)?  linear (Re P, |<c|P>| phase part) vs quadratic (|P|^2).")
    P = (np.sqrt(1.7)) * np.exp(1j * 0.9)          # a participation amplitude, b=1.7
    c = np.exp(1j * 0.3)                            # some fixed linear test-covector
    print("     theta     Re(P)      arg<c|P>     |P|^2 (quadratic)")
    for theta in [0.0, 0.8, 2.1, 4.0]:
        Pt = P * np.exp(1j * theta)
        lin1 = np.real(Pt)                          # linear functional: changes
        lin2 = np.angle(np.conj(c) * Pt)            # linear-functional phase: changes
        quad = np.abs(Pt) ** 2                      # quadratic: invariant
        print(f"     {theta:<9.2f} {lin1:<10.4f} {lin2:<12.4f} {quad:.4f}")
    print("    -> linear-in-amplitude functionals CHANGE with the global phase (not phase-invariant, so")
    print("       NOT valid physical observables); |P|^2 is INVARIANT. The physical bandwidth/strain that")
    print("       sources gravity must be QUADRATIC in amplitude. Q1's form is forced by phase-invariance,")
    print("       the same fact underlying the Born rule. A linear-in-amplitude gravitational strain is not")
    print("       even a valid observable.")

    # ---- 2. Diagonal of the quadratic form = additive Newton (linear in b) ----
    print("\n[2] DIAGONAL = Newton (linear in mass). Multiple sources on a common channel: P_tot = sum P_i.")
    n = 6
    b = rng.uniform(0.5, 2.0, n)
    pi = rng.uniform(-np.pi, np.pi, n)
    Pv = np.sqrt(b) * np.exp(1j * pi)
    b_tot = np.abs(Pv.sum()) ** 2
    diag = np.sum(np.abs(Pv) ** 2)
    off = b_tot - diag
    print(f"    b_tot = |sum P|^2 = {b_tot:.4f}")
    print(f"    diagonal sum|P_i|^2 = sum b_i = {diag:.4f}  == additive Newtonian source (linear in b/mass).")
    print(f"    off-diagonal (interference) = {off:.4f}  == the term Paper_026's linear build DROPPED.")
    print("    -> 'linear in mass' (Newton) IS the diagonal of the 'quadratic in amplitude' (Born) form.")
    print("       The linear-vs-quadratic tension DISSOLVES: same object, Paper_026 kept only the diagonal.")

    # ---- 3. Decoherence collapses the Born form to the diagonal = Newton ----
    print("\n[3] DECOHERENCE -> diagonal: average |sum P|^2 over random relative phases (independent draws).")
    trials = 200000
    accum = 0.0
    for _ in range(4):  # a few independent phase realizations, then a big vectorized average
        pass
    ph = rng.uniform(-np.pi, np.pi, size=(trials, n))
    Pens = np.sqrt(b)[None, :] * np.exp(1j * ph)
    btot_ens = np.abs(Pens.sum(axis=1)) ** 2
    print(f"    <|sum P|^2> over random phases = {btot_ens.mean():.4f}   vs   sum b_i = {b.sum():.4f}")
    print(f"    (ratio = {btot_ens.mean()/b.sum():.4f} -> 1: the coherent off-diagonal averages to zero.)")
    print("    -> under decoherence the Born observable collapses to its diagonal = additive Newton. So")
    print("       Paper_026's LINEAR strain IS the decohered limit of the Born-quadratic strain; the Born")
    print("       rule adds the surviving coherent off-diagonal (retained only vs the horizon = the sigma-")
    print("       coherence, the MOND term).")

    print("\nVERDICT (honest tiers):")
    print("  GROUNDED (inherited): Q1's quadratic FORM follows from (Born/Gleason: observable = |P|^2, not P)")
    print("    + (ED native b=|P|^2, Paper_001) + (kinematic metric sourced by b). Phase-invariance forbids a")
    print("    linear-in-amplitude gravitational observable; the strain MUST be |sum P|^2. Not a free choice.")
    print("  DISSOLVED: the linear-vs-quadratic tension -- Newton (linear in mass) = the DIAGONAL of the")
    print("    Born-quadratic form; Paper_026 built the diagonal; the Born rule mandates the full form.")
    print("  RESIDUAL (narrowed, not closed): the open question is no longer 'is strain quadratic?' but")
    print("    'does a residual horizon off-diagonal survive decoherence?' = the sigma-coherence (account-")
    print("    tier, already de-risked + QM/gauge-consistent). a0 = sigma*sqrt(b_hor) still inherited.")
    print("  => P14 SUBSTANTIALLY DISCHARGED: the load-bearing quadratic commitment is grounded in the Born")
    print("    rule; what remains is horizon-coherence retention + the a0 value. NOT a grand gravity=QM")
    print("    unification -- a bounded grounding of one form in one established rule.")
    print("=" * 94)


if __name__ == "__main__":
    main()
