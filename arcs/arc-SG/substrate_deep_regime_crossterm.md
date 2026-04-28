# Deriving the Deep-Regime Cross-Term Structure in ED-Substrate Gravity

**Date:** 2026-04-27
**Type:** Substrate-foundations analysis (single-file memo)
**Sources:** Full ED corpus — ED-06, ED-07, ED-10, ED-I-06, Arc R, Arc M, Arc N, Arc Q, GR papers, horizon papers, and prior substrate memos.
**Status:** **Honest verdict: ED-substrate, with current articulation, does not uniquely derive the multiplicative MOND law a² = a_N · a₀. The chain's stability landscape under the substrate-rules memo gives additive (a = a_N + a₀), perpendicular-Pythagorean (a = √(a_N² + a₀²)), or other non-multiplicative combinations — none of which produces MOND deep-regime structure or slope-4 BTFR. Three candidate substrate mechanisms that *would* derive multiplicative MOND are identified: (i) logarithmic stability landscape with multiplicative participation-count structure, (ii) hierarchical chain-response with geometric-mean combination of perpendicular strains, (iii) holographic-screen-like substrate thermodynamics. Each is consistent with ED's existing corpus but not uniquely forced. Without committing to one, ED-substrate predicts flat rotation curves at large R with transition at a₀ = c·H₀/(2π), but the BTFR slope is not derived. The deep-regime cross-term remains the substantive articulation gap. This is parallel to the pre-resolution status of the 2π factor: the structural mechanism likely exists in ED-substrate, but identifying it requires specific work that the existing corpus content does not yet uniquely fix.**

---

## 1. Summary of relevant ED structures

### 1.1 ED-06 (decoupling surfaces)

A horizon is "a surface where participation becomes one-sided or undefined." Cosmic decoupling surface and chain-acceleration-induced decoupling surface are both 2-spheres with 4π solid-angle structure.

### 1.2 ED-10 (relational adjacency)

Adjacency is relational; space emerges from "stable participation adjacency." A chain's acceleration breaks 3D-isotropic adjacency, creating an axial direction.

### 1.3 Substrate-rules memo (Newton recovery)

Chain stability score:

> Σ(eₖ₊₁ | eₖ) = Coh(eₖ₊₁, eₖ) − Str(eₖ₊₁, ρ_local) − Grad(eₖ₊₁, ∇ρ)

Strain depends on accumulated environmental gradient (R2.2': cumulative-strain reading). With cumulative-strain, Newton's a = -GM/R² is recovered structurally.

### 1.4 2π memo (cosmic-dipole mechanism)

The 2π factor in a₀ = c·H₀/(2π) arises from the chain's accelerated frame breaking 3D-isotropic adjacency, with the cosmic-horizon contribution projected onto the chain's axial-symmetric leading mode (l=1, m=0 dipole). The dipole's azimuthal periodicity 2π gives the factor.

### 1.5 ED-I-06 (forces from stability gradients)

"Force is what it feels like when the stability landscape changes." Gradients of stability produce experienced acceleration. Multiple contributions to the landscape must combine through some rule.

### 1.6 Arc R / Arc M / Arc Q

Arc R provides spin-statistics structure. Arc M provides matter-wave σ_τ form. Arc Q provides UV-FIN and canonical commutation. None directly articulates the deep-regime cross-term combination rule for the chain's stability landscape.

---

## 2. The two ED-gradient sources

A chain at radius R from a galactic-mass distribution M, accelerating at instantaneous rate a:

### 2.1 Local-mass-induced ED gradient (radial)

Per the substrate-rules memo: M produces ED-gradient ∇ρ_local with magnitude scaling as M/R³, and the cumulative-strain reading converts this to effective acceleration:

> a_N = G·M/R²    (Newton, derived structurally with G = c³ℓ_P²/ℏ)

This gradient is **radial** — it points toward (or away from) the central mass.

### 2.2 Cosmic-horizon dipole-mode ED gradient (axial)

Per the 2π memo: the cosmic horizon contributes via its leading anisotropic mode aligned with the chain's acceleration axis. The effective characteristic acceleration:

> a₀ = c·H₀/(2π)    (derived structurally from azimuthal-mode projection)

This contribution is **axial** — its symmetry axis is set by the chain's acceleration direction.

For circular orbital motion, the chain's acceleration (centripetal) points radially toward the central mass. So the radial direction (local-mass gradient) and the axial direction (cosmic dipole) are *parallel* — both pointing radially.

(For non-circular orbits, the directions can differ; this complicates the analysis but the leading-order behavior on circular orbits is what determines BTFR slope.)

---

## 3. Combination rules: what does ED-substrate prescribe?

The chain's stability score Σ must combine contributions from both sources. The chain's experienced acceleration is the gradient of Σ. The combination rule for Σ determines how the two acceleration scales combine.

### 3.1 Possibility A: Additive Σ

> Σ_total = Σ_local + Σ_cosmic
> ∇Σ_total = ∇Σ_local + ∇Σ_cosmic
> a_chain = a_N + a₀

For a_N >> a₀ (Newton regime): a_chain ≈ a_N. ✓
For a_N << a₀ (deep regime): a_chain ≈ a₀ = const. **v² = a₀·R, NOT BTFR.**

This is what the substrate-rules memo's stability-score structure naturally gives. **Predicts wrong deep-regime behavior.**

### 3.2 Possibility B: Perpendicular Pythagorean

> a_chain² = a_N² + a₀²    (radial and axial gradients summed in quadrature)

This applies if the local and cosmic gradients are *perpendicular* (radial vs azimuthal). For circular orbits with parallel directions (both radial), this doesn't apply — but for general motion, parts of the cosmic dipole are perpendicular to the radial gradient.

For a_N >> a₀: a_chain ≈ a_N. ✓
For a_N << a₀: a_chain ≈ a₀ = const. **Same wrong deep-regime as Possibility A.**

### 3.3 Possibility C: Multiplicative MOND

> a_chain² = a_N · a₀    (geometric-mean cross-term)

For a_N >> a₀: a_chain² ≈ a_N · a₀ → a_chain ≈ √(a_N · a₀). **Wrong** — should be a_N for Newton regime.

So pure multiplicative isn't the right form. The *interpolated* form that gives both regimes correctly:

> a_chain · μ(a_chain/a₀) = a_N
>
> with μ(x) → 1 for x >> 1 (Newton) and μ(x) → x for x << 1 (deep MOND).

In deep regime: (a_chain/a₀)·a_chain = a_N → **a_chain² = a_N · a₀**. ✓

This is the standard MOND interpolation. It gives flat rotation curves and slope-4 BTFR.

### 3.4 What ED-substrate naturally produces

The substrate-rules memo's stability score is **additive in contributions**. Adding local and cosmic strain terms gives additive combination (Possibility A), not multiplicative (Possibility C).

**The current ED-substrate articulation predicts Possibility A** — additive combination, with deep-regime behavior a_total → a₀ (constant). This gives flat *acceleration*, but NOT flat *velocity*: v² = a₀·R grows linearly in R, not constant.

This is empirically wrong. Real galactic rotation curves are flat in v at large R, consistent with multiplicative MOND, not constant a.

**ED-substrate's current articulation does not produce empirical flat rotation curves.**

---

## 4. Searching ED corpus for substrate-native multiplicative structure

The natural follow-up: is there a substrate-native mechanism in the existing ED corpus that produces multiplicative combination, that the substrate-rules memo missed?

### 4.1 Candidate mechanism (i): Logarithmic stability with multiplicative participation count

Hypothesis: the chain's stability score Σ is a logarithm of an underlying multiplicative "participation count" W:

> Σ = log(W),  W = W_cosmic · W_local

Then Σ = log(W_cosmic) + log(W_local) — **additive in Σ, multiplicative in W**. The chain's response to gradients is via ∇Σ, which is additive, giving additive combination of acceleration scales. **Does not produce multiplicative MOND.**

If instead the chain's response is via ∇W rather than ∇Σ:

> ∇W = W · ∇Σ = W_cosmic · W_local · (∇log(W_cosmic) + ∇log(W_local))

Magnitudes scale as W_cosmic·W_local. With local ∇log(W_local) ~ a_N/c and cosmic ∇log(W_cosmic) ~ a₀/c... the chain's experienced acceleration is c × ∇W/W = c × (∇log(W_cosmic) + ∇log(W_local)) = a_N + a₀. Still additive.

**Logarithmic-stability with multiplicative-W doesn't naturally give multiplicative MOND.**

### 4.2 Candidate mechanism (ii): Hierarchical chain response

Hypothesis: the chain's stability response is set by a *hierarchical* structure where cosmic-horizon contribution is the baseline, and local-mass perturbs the baseline. The chain's effective "operating point" depends on the cosmic baseline.

Specifically: the chain's response sensitivity to local-mass gradients is *modulated* by the cosmic baseline. At high cosmic baseline (relative to local): the chain's local-response is amplified by √(cosmic/local) = √(a₀/a_N).

> a_chain (response to local ∇) = (a_N) · √(a₀/a_N) = √(a_N · a₀)    (deep regime)

For a_N << a₀: a_chain → √(a_N · a₀) ≈ MOND deep regime. ✓
For a_N >> a₀: amplification factor goes below 1, and a_chain → a_N (Newton). ✓

This gives multiplicative MOND. **The mechanism: amplification of local-response by cosmic baseline.**

But: why √(a₀/a_N)? Why this specific functional form? ED-substrate doesn't currently articulate the chain's response function as having this form. It's a postulate.

The structural plausibility argument: the chain's response to local gradient is bounded by both the chain's own internal structure AND the participation environment. When the participation environment is dominated by cosmic-horizon (deep regime), the chain's effective "leverage" against local gradient is set by the cosmic-environment scale. The √-scaling could come from a fluctuation-dissipation-like relation between the cosmic-horizon-induced fluctuations (rate H₀/(2π) = a₀/c) and the chain's response amplitude.

**This is the most plausible candidate mechanism, but it requires substrate articulation that current ED doesn't uniquely provide.**

### 4.3 Candidate mechanism (iii): Holographic-screen-like substrate thermodynamics

Hypothesis: the chain's stability landscape has a holographic-screen structure, where the chain "feels" the cosmic-horizon contribution through screens at multiple radii. Each screen has a participation-flux that contributes to the chain's stability gradient.

This is structurally Verlinde's mechanism, ported into ED-substrate language. The cross-term structure that gives multiplicative MOND emerges from the way local-mass perturbations to screen participation-density combine with the cosmic-horizon's volume contribution.

ED-substrate has the ingredients (decoupling surfaces ED-06, holographic information bound substrate-holographic memo). Whether the *thermodynamic-like* combination rule that gives multiplicative MOND is forced by ED-substrate is the question.

In standard physics, the thermodynamic-like rule comes from: temperature is the derivative of entropy with respect to energy. Local-mass adds energy to the screen; cosmic-horizon contributes to the entropy baseline. The temperature gradient (which gives gravity) involves a cross-derivative that produces the multiplicative MOND structure.

In ED-substrate without thermodynamic primitives, the analog would be: chain-response is set by the ratio of (local-perturbation-to-participation-density) over (cosmic-baseline-participation-density). This ratio enters the chain's experienced acceleration with a √-amplification factor (mechanism ii above).

**Mechanism (iii) reduces to mechanism (ii) when ED-substrate doesn't have explicit thermodynamic primitives.** The structural source is the same: hierarchical chain-response with cosmic baseline modulating local response.

### 4.4 Aggregate verdict on substrate-native multiplicative structure

ED's existing corpus does not uniquely force any of mechanisms (i), (ii), (iii). The substrate-rules memo's minimal stability score gives additive combination (no MOND). To get multiplicative MOND, ED-substrate must articulate one of:

- **Hierarchical chain-response with √(a₀/a_N) amplification** in deep regime (mechanism ii). Most plausible structurally.
- **Holographic-screen-like thermodynamic structure** equivalent to Verlinde (mechanism iii). Not currently articulated.
- **Some other substrate-native mechanism** not yet identified.

The 2π memo found the mechanism for that factor by identifying the dipole-mode projection structure already implicit in ED-10 + ED-06. The deep-regime cross-term might similarly be implicit in some ED structure not yet identified — but I can't find it in current corpus content.

---

## 5. What ED-substrate predicts under additive combination (current articulation)

If we accept the substrate-rules memo's additive combination as the ED-substrate prediction, the deep-regime relation is:

> a_chain ≈ a₀ = c·H₀/(2π) = constant in R    (deep regime, a_N << a₀)

For circular orbital motion: v²/R = a₀ → v² = a₀ · R.

> v² = a₀ · R
> v⁴ = a₀² · R²

For BTFR: v_flat at large R is set by where a₀ · R becomes comparable to v² (which depends on M_b through the inner-disc dynamics). Detailed analysis depends on disc structure.

For an order-of-magnitude estimate: at large R, the chain is in deep regime, and v² ≈ a₀ · R. The "v_flat" for a galaxy of size ~R_d is v_flat² ≈ a₀ · R_d. If R_d ~ √(M_b) (rough self-gravitating disc relation), then v_flat² ~ a₀·√(M_b), giving v_flat⁴ ∝ a₀²·M_b. **This is BTFR slope-4** with proportionality constant a₀² rather than G·a₀.

Hmm. Wait — let me reconsider. With additive combination giving a → a₀ (constant) at large R, v² = a₀·R is *not* flat in v. v grows as √R. That's empirically wrong.

But: for empirical BTFR, we observe v_flat at the OUTERMOST measured radii. If those radii are not asymptotically large but finite, v at finite R is finite. The "v_flat" might be a finite-R artifact of v growing as √R at large R rather than truly flat.

For McGaugh-style BTFR: v_flat is measured roughly where rotation curves "flatten." If ED-substrate predicts v growing as √R rather than truly flat, the "v_flat" depends on R, which depends on M_b through R_d ~ M_b^α for some α. The scaling depends on R_d-vs-M_b relation, which is empirical.

For R_d ~ M_b^(1/3) (typical scaling): v(R_d)² = a₀·R_d ~ a₀·M_b^(1/3). v⁴ ~ a₀²·M_b^(4/3). BTFR slope 4/3, NOT 4.

For R_d ~ M_b^(1/2) (alternative scaling): v⁴ ~ a₀²·M_b². BTFR slope 2.

Neither matches empirical slope-4.

**ED-substrate under additive combination predicts BTFR slope between 4/3 and 2, depending on R_d scaling. Not slope-4.**

---

## 6. Structural verdict

### 6.1 Does ED-substrate gravity produce the MOND/Verlinde multiplicative law?

**Not from current articulation.** The substrate-rules memo's additive stability score combines local-mass and cosmic-horizon contributions linearly. This gives:

- Newton in high-acceleration regime ✓
- Constant acceleration a₀ in deep regime ✗ (doesn't give flat v)
- BTFR slope between 4/3 and 2 depending on R_d-M_b relation, NOT slope-4

To produce multiplicative MOND (and hence slope-4 BTFR), ED-substrate must articulate a mechanism that gives the chain a hierarchical response — local-gradient-response amplified by √(a₀/a_N) when cosmic baseline dominates.

### 6.2 What would the substrate articulation look like?

The most plausible candidate: **chain-response amplification by the cosmic-baseline-to-local-gradient ratio**. Specifically, the chain's effective acceleration in response to a local gradient ∇ρ_local with characteristic acceleration scale a_N is:

> a_chain = a_N · ν(a_N/a₀)

where ν → 1 for a_N >> a₀ (Newton recovered) and ν → √(a₀/a_N) for a_N << a₀ (giving a_chain² = a_N·a₀).

The substrate justification for ν having this form would have to come from how the chain's local-gradient response is bounded by cosmic-environment participation structure. This is plausible (the cosmic-environment provides the "background stiffness" that amplifies the chain's response to local perturbations) but not currently derived.

### 6.3 Honest level of the result

**ED-substrate gravity, with current articulation:**
- Recovers Newton structurally.
- Recovers a₀ ≈ c·H₀/(2π) structurally.
- Does NOT recover slope-4 BTFR. Predicts slope between 4/3 and 2.

**ED-substrate gravity with one additional mechanism (chain-response amplification):**
- Recovers Newton structurally.
- Recovers a₀ ≈ c·H₀/(2π) structurally.
- Recovers slope-4 BTFR via multiplicative MOND.

The additional mechanism is plausibly substrate-native (hierarchical chain-response is consistent with ED-substrate's relational ontology) but is not uniquely forced by current corpus content. **It is the next foundational substrate-physics articulation needed to close the BTFR derivation.**

---

## 7. Implications for the program

### 7.1 The position now

After this memo, the substrate-level program is:

| Result | Status |
|---|---|
| Newton's law | Derived structurally (substrate-rules memo) |
| ℓ_ED = ℓ_P | Derived from Newton matching |
| a₀ = c·H₀/(2π) | Derived structurally (2π memo, dipole-mode mechanism) |
| Multiplicative MOND a² = a_N · a₀ | NOT derived from current substrate; requires articulation extension (this memo) |
| Slope-4 BTFR | NOT derived; conditional on multiplicative MOND |

The 2π factor and Newton's law are clean substrate derivations. The deep-regime cross-term — which determines BTFR slope — is the remaining articulation gap.

### 7.2 Comparison to prior status

Before the 2π memo, both the 2π factor and the deep-regime cross-term were articulation gaps. The 2π memo identified the dipole-mode mechanism that closes the 2π gap. **This memo finds the deep-regime cross-term remains genuinely open.**

### 7.3 What this gap means for empirical comparison

ED-substrate in its current articulation predicts:
- Newton at high acceleration ✓ (matches observation)
- a₀ ≈ c·H₀/(2π) at transition ✓ (matches observation within 10%)
- Constant acceleration at very low a_N (NOT matching observation; observed deep-regime is multiplicative MOND with v_flat = const)

So ED-substrate's current articulation matches Newton + transition but **predicts wrong deep-regime behavior**. It doesn't match flat rotation curves or BTFR slope-4.

This is a more honest empirical position than the prior memos suggested. ED-substrate is in the right neighborhood at the *transition*, but its deep-regime prediction is not yet correct.

### 7.4 The honest path forward

To close the deep-regime gap, ED-substrate must articulate the chain-response amplification mechanism (or equivalent). This is foundational substrate-physics work — the kind of writing-and-derivation that Allen does on the framework, not LLM-derivation work.

The 2π memo's success (identifying the dipole-mode mechanism) suggests the deep-regime mechanism is plausibly within reach with careful structural analysis. But it requires the same kind of work: looking at ED-substrate's existing structure and finding the implicit mechanism that produces the desired result. I haven't found it in this memo's analysis. **It might be there; I haven't located it.**

---

## 8. Recommended Next Step

Three concrete actions, in priority order:

1. **Look for the chain-response amplification mechanism in ED's matter-wave (Arc M) structure.** Arc M's σ_τ form gives the chain a natural temporal-width that depends on its rest mass. The chain's response to local gradients, in the deep-acceleration regime, may be set by how the cosmic-horizon-induced fluctuations couple to the chain's matter-wave structure. Specifically: when the chain's rest matter-wave-frequency (mc²/ℏ, very fast) is much larger than the cosmic-horizon-induced perturbation rate (H₀/(2π), very slow), the chain may respond with an amplification factor set by the ratio of these rates. This could naturally produce √(cosmic/local)-type amplification. **This is a concrete substrate-derivation task that would close the deep-regime gap if it works.**

2. **Examine whether ED's GR.1 / Synge-world-function structure provides multiplicative gradient combination.** Theorem GR.1 establishes V1 with Synge world function for ED's vacuum kernel in curved spacetime. The Synge world function is a bilocal quantity (squared geodesic distance). Bilocal quantities naturally produce multiplicative cross-terms when combining contributions from multiple sources. If ED-substrate's chain-response is grounded in bilocal Synge-like quantities rather than local-only stability, multiplicative MOND might emerge structurally.

3. **If neither (1) nor (2) works, accept the honest position:** ED-substrate gravity recovers Newton and the transition scale c·H₀/(2π) cleanly, but produces a deep-regime acceleration of a₀ (constant) rather than the multiplicative-MOND √(a_N · a₀). This predicts BTFR slope between 4/3 and 2 rather than slope-4. This is empirically wrong but structurally clean — it makes a definite prediction that disagrees with empirical galactic-rotation data, which is testable. Whether the deep-regime mechanism exists in ED-substrate (waiting to be identified) or doesn't is then a matter for future foundational work.

The substrate-level program has now done what current ED corpus content can do. Newton and 2π are derived. The deep-regime cross-term either has a substrate-native mechanism we haven't yet found (items 1 and 2 are the remaining places to look) or it requires substrate-articulation extension that is genuinely new work beyond current ED.

Status: complete.
