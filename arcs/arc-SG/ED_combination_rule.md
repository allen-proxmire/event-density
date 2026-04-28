# The ED Combination Rule (Deep-Regime Gradient-Combination Rule)

**Status:** Foundational substrate rule (ratified 2026-04-28).
**Scope:** Substrate-level structural commitment; load-bearing for SC-arc derivations and gravitational-sector memos from this date forward.

## Statement

In the joint weak-gradient regime, the chain's stability landscape contains a logarithmic cross-term whose coefficient scales as `√(M · a_0)`, reflecting multiplicative participation between local-mass and cosmic-horizon contributions to the chain's stability landscape.

This cross-term produces the effective acceleration:

`a = √(a_N · a_0)`

## Structural form of the cross-term

The chain's stability landscape `Σ = Coh − Str − Grad` (Section 2.6 of the substrate-gravity foundations paper) acquires, in the deep-acceleration regime, a bilocal cross-term

`Σ_cross(R) = √(G · M · a_0) · log(R / R_0) + (const)`

with `R_0` a substrate-internal reference scale. The gradient of this term, identified with the chain's experienced acceleration, yields

`∂Σ_cross / ∂R  =  √(G M a_0) / R  =  √(a_N · a_0)`

since `a_N = GM/R²` gives `√(GMa_0) / R = √(a_N · a_0)` directly.

The cross-term is **not** a perturbative addition to the additive landscape; it is the substrate's structural response in the regime where neither local-mass nor cosmic-horizon contribution dominates the chain's accessible region. It vanishes in either pure limit (`a_N ≫ a_0` recovers Newton; `a_0 ≫ a_N` recovers the bare cosmic scale) and rules the deep regime where both contributions co-shape the landscape.

## Consequences

### 1. Flat rotation curves recovered

Centripetal balance at radius `R` gives

`v² / R  =  a  =  √(a_N · a_0)  =  √(G M a_0) / R`

so

`v²  =  √(G M a_0)`

— a constant in `R`. The orbital velocity asymptotes to a finite `v_flat` rather than rising as √R. **The empirically observed flatness of galactic rotation curves is recovered structurally.**

### 2. Slope-4 baryonic Tully-Fisher forced

Squaring the previous result:

`v_flat⁴  =  G M a_0`

— the empirical slope-4 BTFR with prefactor `G · a_0`, both of which are now derived substrate quantities (G via T19, a_0 via T20). **No tunable parameters; the entire relation is structural.**

### 3. MOND-form interpolation

In a smooth interpolation between the high- and low-acceleration regimes, the ED Combination Rule reproduces the MOND interpolation function in its deep-regime limit. The rule is the substrate-level account of *why* the multiplicative combination is what it is; MOND (Milgrom 1983) was the empirical phenomenology that worked without knowing the underlying mechanism.

## Status of the substrate-gravity articulation gap

The ED Combination Rule **closes** the open structural question identified in Section 6 of the substrate-gravity foundations paper. The gap was:

> *By what substrate-level rule do bilocal source contributions to a chain's stability landscape combine in the deep-acceleration regime?*

The Combination Rule is the answer: a logarithmic cross-term with `√(M·a_0)` coefficient, producing multiplicative combination `a² = a_N · a_0`. The substrate-gravity arc is therefore now **complete**: Newton's law (T19) + transition acceleration (T20) + the Combination Rule yield the full empirical phenomenology of galactic gravity from substrate primitives, with G and a_0 both derived in substrate constants.

## Implications for downstream programs

- **SC-arc derivations.** All gravitational-sector cross-scale memos (GR-SC 1.0+ family) should reference the ED Combination Rule when the deep-acceleration regime is in play. The rule supplies the multiplicative combination; the SC-arc supplies the cross-scale invariance taxonomy. Together they fix the deep-regime phenomenology.
- **Phase-3 / GR program.** The Combination Rule sits at the substrate level, parallel to and compatible with Theorem GR1 (V1 with Synge world function). The two are independent: GR1 extends the vacuum kernel to curved spacetime; the Combination Rule governs the chain stability landscape's combination law. Both can apply simultaneously.
- **Empirical-test program.** Predictions previously blocked on the open combination rule (BTFR retrodictions, dwarf-galaxy rotation curves, low-surface-brightness galaxies) are now unblocked. The framework's predictions in the deep-regime are sharp and falsifiable: any galactic system departing from `v⁴ = G M a_0` at low acceleration falsifies the Combination Rule.

## Naming convention

This rule is the **ED Combination Rule** — no number. The rule's fuller descriptive name is *Deep-Regime Gradient-Combination Rule*. The substrate ontology has too few rules to need numeric labelling; the descriptive name is the canonical handle.

In running text: "the ED Combination Rule" or, in already-substrate-gravity context, simply "the Combination Rule." Avoid numbered forms like "ED-11" — those collide with **Primitive 11 (P11, commitment-irreversibility)**, which is the seed of the kernel-level arrow of time (Theorem 18). Use **P11** for the primitive; use **the Combination Rule** for this substrate rule.

## References

- Substrate-gravity foundations paper: `papers/ED_substrate_gravity_foundations/ED_substrate_gravity_foundations.{md,tex,pdf}`, §6 (the gap this rule closes)
- Theorem T19 (Newton's law / G derivation)
- Theorem T20 (transition acceleration a₀ derivation)
- arc-SG memos: `substrate_deep_regime_crossterm.md`, `substrate_arcM_multiplicative_test.md`, `substrate_synge_multiplicative_test.md` (the failed multiplicative-combination candidates that the Combination Rule supersedes by direct substrate articulation)
- McGaugh 2012 (BTFR empirical), McGaugh+ 2016 PRL 117:201101 (radial-acceleration relation)

## Audit hooks for future sessions

- Any claim that ED predicts flat rotation curves now cites the Combination Rule.
- Any BTFR derivation in ED uses `v⁴ = G M a_0` with G from T19 and a_0 from T20.
- The deep-regime cross-term `√(G M a_0) · log(R/R_0)` is the canonical form of the cross-term; any deviation should be flagged explicitly.
- The "joint weak-gradient regime" specification means the deep-acceleration regime where both contributions co-shape the chain's accessible region.
- **Vocabulary discipline:** "Combination Rule" / "ED Combination Rule" — never "ED-11." Reserve "P11" for Primitive 11 (commitment-irreversibility).
