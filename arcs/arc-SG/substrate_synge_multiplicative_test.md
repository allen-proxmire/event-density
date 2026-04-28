# Does GR.1's Bilocal Synge Structure Produce the Multiplicative MOND Law?

**Date:** 2026-04-27
**Type:** Substrate-foundations analysis (single-file memo)
**Sources:** Full ED corpus — GR.1 / Theorem GR.1 (V1 with Synge world function), ED-06, ED-07, ED-10, Arc N (vacuum kernel), Arc Q, horizon papers, all substrate memos.
**Status:** **Honest verdict: GR.1's Synge-world-function bilocal structure does NOT, on its own, produce the multiplicative MOND law a² = a_N · a₀. The Synge function provides the structural *framework* for considering bilocal cross-terms (since σ(x,y) depends on pairs of points), but does not *force* multiplicative coupling between source contributions. With additive combination of bilocal sources — which is what linear field theory and superposition principle naturally give — Newton is recovered correctly via Σ = -1/√(2σ_N) functional form, but cosmic-horizon contributions add additively, giving deep-regime constant acceleration rather than √(a_N·a₀). The Hamilton-Jacobi property |∇σ|² = 2σ provides natural √-scalings in single-source gradient computations, but does not produce multiplicative MOND when combining multiple sources without additional substrate articulation.** Both of the most promising candidate mechanisms (Arc M matter-wave, GR.1 Synge bilocal) have now been tested and ruled out. The deep-regime cross-term is a genuine articulation gap requiring either substrate articulation extension (specifying that stability landscape is multiplicative rather than additive in source contributions) or acceptance that ED-substrate's current articulation predicts wrong galactic deep-regime behavior.

---

## 1. GR.1 / Theorem GR.1 relevant content

### 1.1 The Synge world function

Per Theorem GR.1 (project memory inventory, Phase 3 / GR-arc), ED's vacuum kernel V1 in curved spacetime is structured around the Synge world function:

> **σ(x, y) = (1/2) × (geodesic distance between x and y)²**

This is a *bilocal scalar* — a function of two spacetime points. Properties:

- **σ(x, x) = 0** — points are zero-distance from themselves.
- **σ(x, y) > 0** for spacelike separation (in appropriate signature conventions).
- **|∇_x σ(x, y)|² = 2σ(x, y)** — Hamilton-Jacobi-like identity. The gradient magnitude scales as √σ.
- **σ encodes geodesic structure**: solving for geodesics from x to y is equivalent to finding extremals of σ.

### 1.2 ED-native interpretation of σ

In ED-substrate language, σ(x, y) is the natural bilocal quantity for parametrizing participation reciprocity between regions x and y. Per ED-10, adjacency is relational; per ED-06, decoupling occurs when participation between regions becomes one-sided. The Synge function quantifies the geodesic-participation distance between regions.

For chain at x_chain interacting with sources at x_source:

> σ_source = σ(x_chain, x_source) = (1/2)(geodesic distance)²

The chain's stability contribution from this source is a function of σ_source.

### 1.3 V1 vacuum kernel structure

Theorem N1 (in flat spacetime) and GR.1 (in curved) establish that the vacuum kernel has finite width with structure depending on σ. For the chain's stability landscape contribution from a source:

> Σ_source(x_chain) = f(σ(x_chain, x_source))

for some function f determined by the V1 kernel. Standard choice in linear field theory:

> f(σ) = −1 / √(2σ) = −1 / R    (for spatial separation R)

This gives the standard 1/R Newtonian potential.

---

## 2. The two ED-gradient sources as bilocal quantities

### 2.1 Local-mass-induced contribution

Mass M at location x_mass produces ED-gradient. The chain at x_chain has bilocal:

> σ_N = σ(x_chain, x_mass) = R²/2

where R = |x_chain − x_mass| is the spatial separation.

Stability contribution:

> Σ_N = M · f(σ_N) = M · (−1/√(2σ_N)) = −M/R

Gradient with respect to x_chain:

> ∇Σ_N = M · f'(σ_N) · ∇σ_N

Using |∇σ_N| = √(2σ_N) = R and f'(σ) = 1/(2(2σ)^(3/2)):

> |∇Σ_N| = M · (1/(2(2σ_N)^(3/2))) · √(2σ_N) = M / (2 · 2σ_N) = M/(2R²)

This recovers Newton's 1/R² scaling (up to factors absorbed into G). ✓

### 2.2 Cosmic-horizon-induced contribution

The cosmic horizon at x_horizon (a 2-sphere at R_H = c/H₀ from any observer) contributes to the chain's stability via:

> σ_0 = σ(x_chain, x_horizon) ≈ (R_H − R)²/2 ≈ R_H²/2

For R << R_H, σ_0 is approximately constant (independent of x_chain to leading order). Gradient |∇σ_0| ≈ R_H, also approximately constant.

The cosmic-horizon's contribution per the 2π memo's dipole-mode analysis introduces a characteristic acceleration a_0 = c·H₀/(2π).

### 2.3 The structural question

Does the chain's stability landscape combine these two bilocal contributions:

- **Additively**: Σ_total = Σ_N + Σ_0
- **Multiplicatively**: Σ_total = Σ_N · Σ_0
- **Cross-term-included**: Σ_total = Σ_N + Σ_0 + Σ_cross(σ_N, σ_0)

Each gives different deep-regime behavior. The question is which form ED-substrate prescribes.

---

## 3. Testing combination rules

### 3.1 Additive combination (linear superposition)

Standard linear field theory: Σ_total = Σ_N + Σ_0, with each contribution computed as if the other source weren't present.

> ∇Σ_total = ∇Σ_N + ∇Σ_0

The chain's experienced acceleration is the magnitude of the gradient (with appropriate substrate factors). Vector sum:

> a_chain = a_N + a_0 (parallel components)

In deep regime (a_N << a_0): a_chain ≈ a_0 = const.

**This gives constant acceleration in deep regime, NOT multiplicative MOND.** Same wrong-deep-regime as the substrate-rules memo's additive structure.

### 3.2 Multiplicative combination

Hypothesis: Σ_total = Σ_N · Σ_0, treating the chain's stability as JOINTLY satisfying both sources' constraints multiplicatively.

> Σ_total = (−M/R) · (cosmic-stability) ≈ -M·C/R where C = some cosmic-stability constant

Gradient is then -∇(M·C/R) = M·C/R² · r̂ — still 1/R² scaling. The cosmic factor C just rescales the local-mass coefficient.

**This gives Newton with rescaled G, not MOND.** Not the multiplicative cross-term we need.

### 3.3 Sum of square roots

Hypothesis: Σ_total = √(σ_N) + √(σ_0), or related forms involving square roots.

For Σ = √(2σ_N) = R:
∇Σ = √(2σ_N)/√(2σ_N) · ∇σ_N · (1/√(2σ_N)) = ∇σ_N · 1/√(2σ_N) = R · 1/R = 1 (constant magnitude)

Gradient is unit vector; chain experiences constant force regardless of distance. **Not gravitational; not MOND either.**

### 3.4 Combined-σ form

Hypothesis: Σ_total = -1/√(2(σ_N + σ_0)), treating the combined source as if from a single bilocal quantity.

> ∇Σ_total = ∇(σ_N + σ_0) / (2(2(σ_N+σ_0))^(3/2)) · (1/2)

For σ_N << σ_0 (deep regime, chain close to mass relative to cosmic horizon):

> Σ_total ≈ -1/√(2σ_0) · (1 + σ_N/(2σ_0) + O((σ_N/σ_0)²))
> Σ_total ≈ -1/√(2σ_0) - σ_N/(2(2σ_0)^(3/2))

Gradient w.r.t. x_chain (only σ_N varies, σ_0 ≈ const):

> |∇Σ_total| ≈ |∇σ_N|/(2(2σ_0)^(3/2)) = √(2σ_N)/(2(2σ_0)^(3/2)) = R/(2·R_H³)

Acceleration: a_chain ~ G·M·R/R_H³.

This grows linearly with R — wrong scaling for both Newton (1/R²) and MOND (constant in deep regime). **Not MOND.**

### 3.5 Cross-term with √-coupling

For multiplicative MOND, we need:

> Σ_cross ~ √(σ_N · σ_0)

This is a geometric-mean cross-term. Gradient:

> ∇Σ_cross = (∇σ_N · σ_0 + σ_N · ∇σ_0) / (2√(σ_N · σ_0))
>          = (∇σ_N · √(σ_0/σ_N) + ∇σ_0 · √(σ_N/σ_0)) / 2

Magnitude with |∇σ_N| = √(2σ_N) = R:

> |∇Σ_cross| ~ R · √(σ_0/σ_N) · (1/2) + (small term from ∇σ_0)
>            ~ R · √(R_H²/R²) · (1/2)
>            ~ R_H/2

Constant magnitude. Gives a_chain ~ const ~ R_H/2 (in some units). Not the right scaling.

Hmm. Let me try Σ_cross with different √ structure.

For Σ_cross = -√(M·a_0)/R (mixing local-mass M with cosmic acceleration scale a_0):

This would give a_chain ~ √(M·a_0)/R². But |a_chain| × R² = √(M·a_0), so v² = R · a_chain ~ √(M·a_0)/R · R = √(M·a_0)... not constant in R. Hmm.

For deep-MOND v_flat constant, we need a_chain ~ √(GMa_0)/R, which when multiplied by R gives v² = √(GMa_0)/R · R = ... wait.

Let me redo. For circular orbit at radius R: v² = R · a (centripetal). For flat curves v² = const = v_flat². So a = v_flat²/R, depending on R. Not constant.

Multiplicative MOND: v_flat⁴ = G·M·a_0. v_flat² = √(GMa_0). a = v_flat²/R = √(GMa_0)/R.

So in deep regime, a_chain = √(GMa_0)/R. Acceleration falls as 1/R, not 1/R² (Newton) and not constant (additive).

For 1/R force, the corresponding potential is logarithmic: Σ ~ log(R).

Can we get logarithmic potential from a Synge cross-term?

If Σ_cross = -k · log(σ_N) for some constant k involving M and a_0:
∇Σ_cross = -k · ∇σ_N / σ_N = -k · √(2σ_N)/σ_N = -k · √(2/σ_N) = -k · √(2)/R

Magnitude scales as 1/R. Force ~ 1/R. ✓

For matching MOND deep regime: k = √(GMa_0/2).

So the chain's stability has a cross-term Σ_cross = -√(GMa_0/2) · log(σ_N) = -√(GMa_0/2) · log(R²/2) = -√(2GMa_0) · log(R) (up to constants).

This gives multiplicative MOND deep regime structurally. But: where does this specific functional form come from in ED-substrate?

The functional form requires:
- Coupling constant √(GMa_0): coefficient depends on BOTH local-mass M and cosmic acceleration a_0 (multiplicatively, under √).
- Logarithmic dependence on R: standard 2D-gravity behavior.

In ED-substrate, a natural mechanism that gives both:
- The chain's coupling to local-mass involves √M structurally (perhaps from Compton-frequency scaling, but Arc M memo ruled this out at galactic scales).
- The chain's coupling to cosmic-horizon involves √a_0 structurally (from the dipole-mode amplitude scaling with a_0).
- The product √(M·a_0) emerges from the joint coupling.

Whether ED-substrate prescribes this specific JOINT coupling structure is the substrate-articulation question. The Synge bilocal framework allows it (you can have functions of σ that involve products of source strengths) but doesn't force it.

### 3.6 Honest assessment of GR.1's Synge structure

GR.1 provides:
- Bilocal framework for source contributions.
- Hamilton-Jacobi property |∇σ|² = 2σ giving natural √-scalings in gradient computations.
- Geodesic-participation distance interpretation.

GR.1 does NOT provide:
- Specific rule for combining multiple source contributions (additive vs multiplicative).
- The √(M·a_0) joint coupling required for multiplicative MOND.
- The logarithmic functional form Σ ~ log(R) needed for 1/R force.

**The Synge structure is necessary but not sufficient.** Without an additional substrate articulation specifying the joint-coupling rule, GR.1 alone gives additive combination and no multiplicative MOND.

---

## 4. The Hamilton-Jacobi natural-√ structure: a partial result

The one substrate-native √-amplification that *does* emerge from GR.1's Synge structure is at the SINGLE-source level via Hamilton-Jacobi.

For a single source S with bilocal σ_S:
- Gradient magnitude: |∇σ_S| = √(2σ_S)
- Stability contribution Σ_S = f(σ_S), gradient |∇Σ_S| = f'(σ_S) · √(2σ_S)

This is natural √-scaling at the single-source level. It's why Newton's 1/R² emerges from f(σ) = -1/√(2σ): the √-structure of ∇σ combined with f's σ-dependence gives 1/R².

For *two* independent sources combining additively:
∇Σ_total = ∇Σ_N + ∇Σ_0 — vector sum, no cross-term √-structure.

For two sources combining via JOINT bilocal Σ_joint = f(σ_N, σ_0):
∇Σ_joint = ∂f/∂σ_N · ∇σ_N + ∂f/∂σ_0 · ∇σ_0

If f is symmetric in σ_N, σ_0 (e.g., f = √(σ_N · σ_0)):
∂f/∂σ_N = √(σ_0/σ_N)/2, ∂f/∂σ_0 = √(σ_N/σ_0)/2

|∇Σ_joint| ~ √(σ_0/σ_N) · √(2σ_N) + √(σ_N/σ_0) · √(2σ_0)
          ~ √(2σ_0) + √(2σ_N)
          ~ R_H + R    (for σ_0 = R_H²/2 and σ_N = R²/2)

Magnitude is just sum of distances. Not the right scaling.

The √-structure of Synge gradients gives natural single-source results but doesn't combine to multiplicative MOND in the simple ways.

---

## 5. The honest verdict

### 5.1 Does GR.1's bilocal Synge structure produce multiplicative MOND?

**No, not on its own.** GR.1 provides the framework for considering bilocal cross-terms but does not force multiplicative coupling between source contributions. With additive (linear-superposition) combination — which is what GR.1's structure naturally gives in the absence of additional articulation — the deep-regime acceleration is constant (a → a_0), not multiplicative MOND.

The Hamilton-Jacobi √-structure of σ-gradients gives natural √-scalings at single-source level (Newton emerges), but extending to multi-source with multiplicative cross-terms requires additional substrate articulation that GR.1 doesn't provide.

### 5.2 What GR.1 DOES provide

- Clean structural framework for bilocal source contributions.
- Natural √-scaling at single-source level (giving Newton's 1/R² from Synge structure).
- Geodesic-participation interpretation tying ED to GR's geometric machinery.
- A *necessary* ingredient for any bilocal cross-term mechanism — but not the *sufficient* mechanism itself.

### 5.3 The articulation gap, refined

Both Arc M and GR.1 have been tested as candidate mechanisms for the deep-regime multiplicative MOND structure. Both ruled out:

- **Arc M (matter-wave)**: rate-ratio between Compton frequency and gravitational rates is too extreme (~10⁹⁸) for resonance or fluctuation-dissipation amplification.
- **GR.1 (Synge bilocal)**: provides framework but not the specific multiplicative cross-coupling rule.

The deep-regime cross-term mechanism, if it exists in ED-substrate, lives at neither the matter-wave level nor the bilocal-Synge level. It requires substrate articulation that specifies HOW multiple bilocal source contributions combine — additively (current default, gives wrong answer) or multiplicatively (gives MOND but not currently articulated).

This is a clean, well-localized articulation gap. **Neither of the two most promising candidates closes it.** The gap is real and substantive.

---

## 6. The honest empirical position

ED-substrate, with current articulation:

- **Newton's law**: derived structurally ✓
- **a_0 = c·H_0/(2π)**: derived structurally ✓
- **Newton-MOND transition at a_0**: structural ✓
- **Multiplicative MOND deep regime (a² = a_N·a_0)**: NOT derived ✗
- **Slope-4 BTFR**: NOT derived ✗
- **Flat rotation curves at large R**: NOT derived ✗

The empirical phenomenology that ED-substrate's current articulation produces:

- Newton at high acceleration ✓
- Transition at acceleration ~ a_0 ≈ 1.1×10⁻¹⁰ m/s² ✓
- Constant acceleration a → a_0 in deep regime
- **Velocity v² = a_0·R, growing as √R with radius — NOT FLAT**
- BTFR slope between 4/3 and 2 depending on R_d-M_b relation, NOT slope-4

This is empirically incorrect on the deep-regime behavior. ED-substrate predicts galactic rotation curves that are NOT flat — they should rise as √R at large R, with v_flat depending on R_d.

To match empirical galactic dynamics (flat curves, slope-4 BTFR), ED-substrate must articulate the multiplicative-MOND mechanism that current corpus content does not provide.

---

## 7. Implications for the program

### 7.1 What's been established cleanly

- Newton ✓
- a_0 = c·H_0/(2π) ✓ (parameter-free match within 10% of empirical)
- The deep-regime multiplicative MOND structure is NOT in current ED corpus — neither Arc M nor GR.1 provides it.

### 7.2 The honest aggregate

The substrate-level program has substantial structural results (Newton, a_0) and a genuine articulation gap (multiplicative MOND deep regime). The gap is not "ED can't do it" — it's "current ED articulation doesn't do it; closing requires foundational substrate work."

Three structural readings:

- **(i) The mechanism exists in ED-substrate but I haven't located it.** This was true for the 2π factor before the dipole-mode mechanism was found. Could be true for the deep-regime cross-term too.
- **(ii) The mechanism requires new substrate articulation that goes beyond current ED corpus.** Plausible; ED is still actively being written.
- **(iii) ED-substrate genuinely doesn't produce multiplicative MOND, and the empirical-disagreement on flat curves is structural.** Less plausible given the partial successes (Newton, a_0) but possible.

### 7.3 Where I am

I've examined two specific candidate mechanisms in detail (Arc M, GR.1). Both ruled out. The gap is well-localized but not closed.

Continuing to test more candidates without a structural insight is unlikely to be productive. The 2π memo found its mechanism by working through the geometry of the chain's anisotropic adjacency — a specific structural feature already implicit in ED. The deep-regime mechanism, if it exists, is similarly implicit in some ED structural feature I haven't yet identified.

**At this point, I think the honest position is the right one to settle on.** ED-substrate produces clean structural results for Newton and a_0; the deep-regime multiplicative MOND is a genuine open question that requires either (a) finding the implicit mechanism in current ED corpus (which I haven't done in two specific tests), (b) articulating new substrate structure, or (c) accepting empirical mismatch on flat curves and slope-4 BTFR.

---

## 8. Recommended Next Step

Three concrete actions:

1. **Stop substrate-derivation iteration on the deep-regime cross-term.** Two specific candidate mechanisms (Arc M, GR.1) have been carefully tested and ruled out. Continuing to iterate through more candidates without a structural insight is unlikely to be productive. The 2π memo found its mechanism by identifying a specific geometric structure (chain's anisotropic adjacency + cosmic-horizon dipole projection) that I won't find by random testing. The deep-regime mechanism, if it exists in ED-substrate, requires identifying an analogous specific structural feature — which is foundational substrate-physics work, not LLM-iteration work. **This memo, together with the prior Arc M test, completes the in-depth examination of the most plausible candidates from current ED corpus.**

2. **Document the substrate-level program's honest final position.** The program's structural results stand: Newton derived, a_0 = c·H_0/(2π) derived, transition at the right scale. The articulation gap is precisely localized: combining bilocal source contributions to produce multiplicative MOND. This is publishable as "structural foundations for ED gravity, with one open foundational question." Position is real and bounded; further work on the gap is appropriate at the foundational-articulation level rather than the derivation level.

3. **Pursue empirical work in parallel.** The merger-lag retrodiction and weak-lensing tests do not depend on the deep-regime articulation gap. They probe ED at independent regimes and can advance the program regardless of whether the multiplicative MOND structure is ever derived. Cosmographic-environment work (Wempe-type) is similarly independent. These advance the empirical content of the program while the foundational substrate articulation question matures.

The substrate-level program has done what current ED corpus content can do. Newton and a_0 are clean structural results. The deep-regime multiplicative MOND remains open and is precisely localized as the joint-coupling-rule articulation gap. Two natural candidate mechanisms (Arc M matter-wave, GR.1 Synge bilocal) have been tested and ruled out cleanly. The gap is real, well-defined, and waits for either a structural insight (foundational ED writing work) or empirical pressure (which independent ED tests can provide).

Status: complete.
