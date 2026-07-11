# §7 — Gauge Structure: the shape is derived, the multiplicities are the wall

*Draft v1, 2026-07-10. Register: peer-facing. Tiers (per the source paper's audit): SU(N) form **derived-conditional** (on the ℂ-amplitude); non-abelian gauging **account**; F² action **derived-given-inputs**; mass gap a **mechanism** (not a Yang–Mills proof); single hypercharge **grounded (identification)**; the {1,2,3} multiplicities a **wall** (ED's stability route refuted). Point-toward. Primary source (read-first): `Paper_GaugeStructure_FromChannelTransport`. This section plants the rep-spectrum wall (#1) that §8, §9, and §10 refer back to.*

---

**The arrow's job here.** The arrow's gauge-sector role is the single hypercharge. The Standard Model has exactly one gauged `U(1)`, and no conventional account says why one. In ED there is one because P09 polarity is one primitive phased against one external flow, the commitment arrow (§3). Hypercharge is the arrow wearing a phase. The rest of this section is the channel structure, and it sets a clean, honest boundary: ED derives the *shape* of the gauge sector that the Standard Model postulates wholesale, and inherits the one piece the Standard Model also does not explain.

## What the substrate fixes

Assemble the substrate into a bundle: the base is emergent spacetime, the fiber at each locus is the channel family (P07), the connection is polarity-transport (P05). The gauge group is the fiber's structure group. For a family of `N` dynamically-indistinguishable channels carrying a complex amplitude `ψ ∈ ℂ^N`, the transport that mixes the channels while preserving total bandwidth (a P05 isometry) is the unitary group `U(N) = SU(N) × U(1)`. So **non-abelian SU(N) is the structure group of the channel fiber** — conditional, and the paper is precise about the condition: indistinguishability *alone* gives only the permutation group `S_N`; the continuous `U(N)` needs the ℂ-amplitude (from the quantum-logic keystone, §4) and total bandwidth as the sole invariant.

On that structure the rest of the gauge sector's shape follows:
- The **gauging is genuinely non-abelian**: position-dependent transport gives non-commuting holonomies, reconciled with einselection because the `N` channels within a family have no accessible label, so transport is free to mix them while the arrow pins the basis for the SU(N)-invariant observables across families.
- The **action is F²**: the substrate's coherence-deficit on the plaquette holonomy is the Wilson action, `1 − (1/N)Re Tr U_□`, which coarse-grains to `−¼∫Tr(F²)` — the Wilson trace being the matter-averaged per-chain deficit by Schur's lemma, given the effective-action prescription. (The abelian case is grounded on the certified substrate; the non-abelian lift is analytic.)
- The **mass gap has a clean origin**: the same coherence-deficit carries the self-interaction `[A,A]`, which is zero for commuting (abelian) channels and nonzero for non-commuting ones. So in pure Yang–Mills the classical massless flat direction is lifted exactly when the channels are non-abelian — Maxwell is massless because its channels commute, Yang–Mills gaps because they do not. This is the gap's *mechanism*, verified at tree level; the continuum survival (asymptotic freedom, the Clay problem) is a different and harder question, not claimed.
- The **single hypercharge** is the arrow's job above: one P09 phase against one arrow gives one `U(1)_Y`.

Put together: `∏_i SU(N_i) × U(1)_Y`. The Standard Model takes `SU(3) × SU(2) × U(1)` as a postulate. ED derives that this is the *kind* of object the channel substrate produces — non-abelian, F²-acting, gap-carrying, with a single hypercharge — given its amplitude structure. That is a real accounting of structure the Standard Model simply assumes.

## The wall: why {1, 2, 3}

What ED does not do is select the multiplicities. The framework gives `SU(N)` for any `N`; it does not say why the stable channel-families are singlets, doublets, and triplets and stop there. This is the report's largest genuine open structural question (#1), and three things should be said about it plainly.

First, ED's natural route to it *failed*, and that is reported as a failure, not smoothed over: channel-family stability does not select {1,2,3} — a symmetric multiplet is stable for all `N` (the binding energy grows with `N`, the Hessian stays positive). ED does not currently derive the multiplicities.

Second, the Standard Model does not explain them either. The gauge group and its representation content are inputs there. So ED's status on this specific question — the shape derived, the multiplicities inherited — is not *worse* than the Standard Model's; it is the same inheritance, on top of a derivation of the surrounding structure the Standard Model does not attempt.

Third, the open question is bounded and well-posed, not a vague deficiency. It reduces to a single sharp question — why the internal channel-amplitude dimension is three — and the one live route to it (a 3D-linking argument that would tie the internal dimension to the spatial one) turns on a standard, non-ED-specific mathematical task: detecting whether the substrate's participation graph is intrinsically linked, which requires an established linkless-embedding-detection algorithm rather than any new ED insight. That is a tooling task that someone with the right computational geometry tools could run; it does not require the theory to say anything further. So #1 is an open problem with a delegatable next step, held honestly as unbuilt.

## What is inherited or gated

- **Couplings and scales** (`g`, the effective graph scale `a`) set the normalization; inherited.
- **Charge values** (per-particle hypercharge) are the per-channel P09 advance rates; inherited. The single `U(1)_Y` is grounded, but its charge normalization is not derived.
- **Electroweak breaking** (`SU(2) × U(1)_Y → U(1)_EM`, the Weinberg angle, the W/Z masses) rides on the substrate-Higgs and is Higgs-gated. The unbroken group is derived; the breaking is not.

## Scope

- SU(N) is derived-conditional on the ℂ-amplitude, not from indistinguishability alone (which gives `S_N`).
- The F² action's non-abelian form is at the gauge-program (analytic) tier; only the abelian case is simulator-grounded.
- The mass gap is a mechanism, not a Yang–Mills existence proof; continuum survival is open.
- The single hypercharge is a grounded identification (P09 is one primitive), not a forced collapse.
- Spin-SU(2) (the spacetime frame bundle) is a separate object, not this internal gauge structure (§10 handles the spinor).

## What this buys the report

This section plants the wall the whole Standard Model quarter refers back to. The inherited casting of §9 (which force is chiral = SU(2) pseudoreality), the inherited charge magnitudes of §8, and the inherited generation spectrum of §10 are all the *same* rep-spectrum wall, #1, and it lives here: ED derives the gauge sector's shape and inherits its multiplicities. Framed correctly, that is one bounded, delegatable open problem sitting underneath a genuine derivation of structure — not three separate gaps, and not a vague failure.

---

*Draft notes for finalization:*
- *Hold every conditional: SU(N) derived-CONDITIONAL (ℂ-amplitude; S_N without it); F² derived-GIVEN-INPUTS; gap = mechanism NOT Clay proof; non-abelian = analytic tier; single hypercharge = identification. The source paper's preamble is strict on all of these — do not upgrade any to "derived from nothing."*
- *The {1,2,3} wall must stay a reported failure (stability route refuted), THEN the two mitigations (SM doesn't explain it either; reduces to a delegatable linkless-embedding task). Do not let the mitigations erase the failure — the honest line is "open, ED's route failed, but bounded and not ED-specific."*
- *Keep "#1 / same wall" language identical to §8, §9, §10, §13 so the report reads as one inheritance.*
- *The SM-postulates-this-wholesale framing is fair and strong — keep it, it is the section's best honest point (ED derives shape the SM assumes).*
- *Length ~1250 words. Register OK: structure group, U(N)=SU(N)×U(1), Wilson action, Schur's lemma, [A,A], asymptotic freedom, linkless embedding named flat-out.*
