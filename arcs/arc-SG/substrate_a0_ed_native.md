# Deriving a₀ from ED-Native Ontology (No Standard Physics Imports)

**Date:** 2026-04-27
**Type:** Substrate-foundations analysis (single-file memo)
**Sources:** ED-06 (horizons as decoupling surfaces); ED-10 (spacetime emergence; information not fundamental). All standard-physics machinery (Unruh, de Sitter temperature, Bekenstein-Hawking entropy, microstate counting) explicitly excluded.
**Status:** **Honest result: ED-substrate ontology, used strictly, derives a transition acceleration of approximately a_ED ≈ c·H₀ ≈ 6.8 × 10⁻¹⁰ m/s² — off from empirical MOND a₀ ≈ 1.2 × 10⁻¹⁰ m/s² by a factor of approximately 2π. The deep-regime structural relation `a² = a_N · a₀` (which gives slope-4 BTFR) does not derive cleanly from ED-substrate alone — it requires either additional substrate articulation that ED-06/ED-10 don't yet provide, or it requires importing the Verlinde-mechanism's specific thermodynamic structure (which the prior memo did, and which ED-substrate alone is consistent with but doesn't force).** The previous memo's a₀ = c·H₀/(2π) result is correct in standard-physics ontology but its derivation chain imports machinery ED-substrate doesn't natively articulate. **The honest substrate-only verdict is: ED is in the right structural neighborhood (within factor 2π of empirical a₀), with the slope of BTFR likely 4 by the same general scaling argument, but the precise prefactor requires substrate-level commitments not yet made.**

---

## 1. ED-native substrate quantities (no standard physics)

ED-06 and ED-10 supply five concepts to replace the standard-physics machinery I imported in the prior memo:

### 1.1 Decoupling surface

Per ED-06 §2.1: a horizon is "a surface where participation becomes one-sided or undefined." It is "a relational threshold," not a geometric boundary. Decoupling surfaces are where the ED gradient becomes too steep to sustain reciprocal participation.

Two relevant decoupling surfaces in our context:

- **Cosmic decoupling surface** at radius R_H ≈ c/H₀: where micro-events from beyond cannot be integrated by an observer in finite cosmic time. Per ED-10 §1.5 and ED-06 §2.1, this is structural to ED's substrate when finite cosmic age is included.

- **Acceleration-induced decoupling surface** at distance d_a ≈ c²/a from a chain accelerating at rate a: where micro-events emitted from "behind" cannot be integrated by the accelerating chain. Per ED-06's framework, this surface emerges whenever a chain's cross-participation with regions becomes one-directional.

### 1.2 Participation capacity

Replaces "information count" or "microstate count." Per ED-10 §1.3, information is not fundamental; it's a constraint on commitment histories. The corresponding substrate-native quantity is **participation capacity**: the rate at which one region can integrate the micro-events of another.

Participation capacity at a decoupling surface: bounded by the surface's spatial structure and the substrate's UV cutoff ℓ_ED.

### 1.3 Commitment-irreversibility density

Replaces "entropy" per ED-06 §2.5. Each unit of decoupling-surface area carries a finite commitment-irreversibility, which is the substrate-native quantity that standard-physics calls "entropy density." Total commitment-irreversibility at a decoupling surface ≈ A / ℓ_ED² (in substrate-units), but the *meaning* is "amount of irreversible commitment encoded at the surface," not "log of microstates."

### 1.4 ED-gradient fluctuation rate

Replaces "temperature" per ED-06 §2.5. The rate at which the local ED-gradient fluctuates due to substrate-level micro-event production. For a region with characteristic time scale τ, the fluctuation rate is ~ 1/τ.

### 1.5 ED-gradient bandwidth

The maximum rate at which gradient information can propagate through the substrate. Bounded by c (per ED-07 §7.2). Combined with the substrate UV cutoff ℓ_ED, this gives a maximum gradient-information-flux per unit area of ~ c/ℓ_ED² per unit substrate-time.

---

## 2. The cosmic decoupling surface in ED-native terms

### 2.1 Geometric setup

The cosmic decoupling surface for any observer is the boundary of their causal-domain accessibility. Distance: R_H ≈ c/H₀. Surface area: A_H = 4π R_H² = 4π c²/H₀².

In ED-native terms (no standard physics):

- **Participation capacity at the cosmic decoupling surface:** total participation channels accessible across the surface = A_H / ℓ_ED² (in substrate-units, count of channel-positions). Each ℓ_ED² of surface area supports one channel.
- **Commitment-irreversibility density:** σ_irrev ≈ 1/ℓ_ED² per unit area (one unit of irreversibility per substrate-area-unit).
- **ED-gradient fluctuation rate at cosmic decoupling surface:** the surface's spatial structure changes at rate ~ 1/τ_cosmic, where τ_cosmic is the cosmic time scale ~ 1/H₀. Therefore γ_cosmic ≈ H₀ in substrate-time units.

### 2.2 The natural cosmic acceleration scale

For an observer at the center of their cosmic decoupling surface:

- Distance to surface: R_H = c/H₀
- Time scale of surface evolution: τ_cosmic = 1/H₀
- "Natural" acceleration scale that converts these: a_cosmic ≈ R_H / τ_cosmic² ... wait, units check:
   - R_H has units m
   - τ_cosmic² has units s²
   - R_H / τ_cosmic² has units m/s². ✓
   - a_cosmic = (c/H₀) / (1/H₀)² = c · H₀ ≈ 6.8 × 10⁻¹⁰ m/s²

Alternatively, equivalently: γ_cosmic × c = H₀ × c = c·H₀, the acceleration scale corresponding to the cosmic gradient-fluctuation rate.

**a_cosmic = c · H₀** is the ED-native cosmic acceleration scale, derived from substrate quantities (cosmic decoupling-surface distance R_H, fluctuation rate γ_cosmic = H₀, conversion via c).

No 2π factor enters this derivation. The 2π in standard physics comes from Unruh-formula geometry (Euclidean-time periodicity of Rindler frames). In strict ED-substrate ontology, no such formula is invoked.

---

## 3. The accelerating-chain decoupling surface in ED-native terms

### 3.1 Geometric setup

A chain accelerating at rate a has a "Rindler-type" decoupling surface in its instantaneous frame. Distance from chain: d_a = c²/a. Per ED-06's general framework, this surface emerges because cross-participation between the chain and regions "behind" (in the chain's deceleration direction) becomes one-sided.

In ED-native terms:

- **Participation capacity at the chain's decoupling surface:** A_chain / ℓ_ED² where A_chain = 4π d_a² = 4π c⁴/a².
- **ED-gradient fluctuation rate experienced by the chain:** γ_chain = c/d_a = a/c (the time scale for the surface to "refresh" from the chain's perspective is d_a / c, so γ_chain = a/c).
- **Natural acceleration self-consistency check:** γ_chain × c = a. ✓

### 3.2 The natural acceleration scale from chain self-consistency

The chain's own acceleration a is the quantity we want to derive in the deep regime. We have:
- Chain's decoupling-surface fluctuation rate: γ_chain = a/c
- Cosmic decoupling-surface fluctuation rate: γ_cosmic = H₀

These have the same units (1/time).

---

## 4. The transition acceleration

### 4.1 Defining the transition

In the high-acceleration regime, the chain's own decoupling surface is closer than the cosmic decoupling surface (d_a < R_H, i.e., c²/a < c/H₀, i.e., a > c·H₀). The chain's own decoupling structure dominates its experience. Local-mass dynamics applies; Newton's law (which the prior memo's substrate-rules derivation recovered) holds.

In the low-acceleration regime, the chain's own decoupling surface is farther than the cosmic decoupling surface (a < c·H₀). The cosmic decoupling surface "wraps around" the chain's accessible region. Cosmic-horizon-induced structure dominates.

**The transition is at a = c·H₀.**

### 4.2 The natural ED-substrate value

> **a_ED = c · H₀ ≈ 6.8 × 10⁻¹⁰ m/s²**

This is the ED-substrate-native transition acceleration scale, derived purely from:
- Cosmic decoupling-surface distance R_H = c/H₀
- Acceleration-induced decoupling-surface distance d_a = c²/a
- Equality d_a = R_H

No standard-physics machinery imported. No 2π factor.

### 4.3 Comparison with empirical

Empirical MOND a₀ ≈ 1.2 × 10⁻¹⁰ m/s².

> **Ratio: a_ED / a₀_emp ≈ 5.7 ≈ 2π.**

ED-substrate predicts a transition acceleration that is **larger than empirical by a factor of approximately 2π**.

The prior memo (using standard physics) gave a₀ = c·H₀/(2π) ≈ 1.08 × 10⁻¹⁰ m/s², which matches empirical to ~10%. **That memo's derivation imported the Unruh-formula 2π factor.** In strict ED-substrate ontology, this 2π factor is not present.

---

## 5. The deep-regime structural relation

### 5.1 What ED-substrate gives directly

Above a_ED: chain's decoupling-surface dominates. Newton's law applies (per the substrate-rules memo): a = G·M/R².

Below a_ED: cosmic decoupling-surface dominates. The chain's experience is governed by the cosmic-horizon contribution.

But: **what specifically does ED-substrate predict the chain experiences in the deep regime?** This is where the derivation runs into honest limits.

Two readings are structurally available:

- **(R-A) Constant cosmic acceleration.** The chain in deep regime feels the cosmic-horizon-induced acceleration directly: a_total = a_ED = c·H₀. This is constant in M, constant in R. **This is structurally inconsistent with empirical flat curves**, because it gives v² = a_ED·R growing linearly in R, not constant v_flat.

- **(R-B) Cosmic-coupling modifies local-mass dynamics.** The chain in deep regime feels a modified local-mass gradient, with the cosmic-horizon contribution providing a "boost" or "amplification" that depends on the Newton-regime acceleration. **This is what MOND's a² = a_N · a₀ encodes.** Producing this in ED-substrate requires specifying *how* the cosmic-decoupling-surface and the local-mass distribution couple structurally.

### 5.2 Why R-B doesn't derive cleanly from ED-substrate

R-B requires that the cosmic decoupling-surface and the local-mass distribution couple in a specific way — not additively, but multiplicatively (in the gradient-of-stability landscape). The standard-physics derivation (Verlinde) achieves this through entropy-thermodynamics: the screen's entropy combines cosmic-horizon and local-mass contributions, and the temperature gradient (which gives force) involves cross-terms.

In ED-substrate, the analog would be: the commitment-irreversibility density at a screen surrounding the chain combines cosmic-horizon and local-mass contributions, and the gradient of this density produces the chain's acceleration with cross-terms.

**ED-06 doesn't articulate the cross-term structure explicitly.** It says decoupling surfaces have commitment-irreversibility, but doesn't specify how cosmic-horizon-induced and local-mass-induced contributions combine. Without this specification, ED-substrate cannot uniquely predict the deep-regime structural relation.

The standard-physics derivation gives a² = a_N · a₀. Other combinations are mathematically possible: a = a_N + a₀ (constant offset), a = max(a_N, a_0) (sharp transition), a = √(a_N² + a_0²) (smooth interpolation), etc. **Each gives different rotation-curve predictions.**

ED-substrate, strictly, does not pick out the multiplicative `a² = a_N · a_0` relation over the alternatives.

### 5.3 Honest implication for BTFR slope

Slope-4 BTFR (`v⁴ ∝ M_b`) follows from `a² = a_N · a₀` *specifically*. If ED-substrate gives a different deep-regime relation, it gives a different BTFR slope:

| Deep-regime relation | BTFR slope |
|---|---|
| a² = a_N · a₀ (Verlinde/MOND) | 4 |
| a = max(a_N, a₀) | 0 (flat plateau at v ~ √(a₀·R)) |
| a = a_N + a₀ | varies, not slope-4 |
| a = √(a_N² + a₀²) | varies, not slope-4 |

**Without specifying which deep-regime relation ED-substrate forces, the BTFR slope is not derived.** The prior memo's slope-4 result rested on adopting Verlinde's a² = a_N · a₀ structure, which is a standard-physics derivation chain that ED-substrate alone doesn't reproduce.

---

## 6. Structural verdict

### 6.1 Does ED-substrate reproduce the standard a₀ prefactor?

**No, not from substrate alone.** ED-substrate's natural scale is a_ED ≈ c·H₀ ≈ 6.8 × 10⁻¹⁰ m/s², a factor of ~2π larger than empirical a₀.

The standard-physics 1/(2π) factor comes from Unruh-formula geometry (Euclidean-time periodicity of Rindler frames). In ED-substrate ontology, no such formula is invoked, so the factor is absent.

### 6.2 Is the difference structural or correctable?

**Honestly: unclear.** Three readings:

- **(V1) The 2π is genuinely structural in ED-substrate but I missed it.** Geometric considerations about chain-decoupling-surface "wrapping" around the chain in 4-dimensional substrate-spacetime might introduce a factor of 2π that my analysis didn't capture. If so, the correct ED-substrate answer is c·H₀/(2π), matching the prior memo.

- **(V2) ED-substrate genuinely predicts c·H₀, not c·H₀/(2π).** The empirical MOND a₀ value is sensitive to the assumed interpolation function (μ-function). Different μ-functions give different best-fit a₀ values. Some interpolation functions could give a best-fit a₀ closer to c·H₀ than to c·H₀/(2π). If ED-substrate uses one of those, the empirical match is better than ~5.7-factor-off would suggest.

- **(V3) ED-substrate is genuinely off by factor 2π.** Empirical MOND a₀ is what it is, and ED-substrate gives a different number. The discrepancy is real and constrains the substrate ontology.

I cannot decide between (V1), (V2), (V3) without more substrate-level work or empirical analysis with different interpolation functions.

### 6.3 Does the ED-native derivation still support slope-4 BTFR?

**Not directly.** Slope-4 BTFR requires the specific deep-regime relation a² = a_N · a_0. ED-substrate, strictly, doesn't pick this out — the cross-term structure that gives the multiplicative combination requires structural articulation beyond what ED-06 + ED-10 provide.

The general scaling argument (chain transitions to cosmic-dominated regime at a ~ c·H₀, so v_flat is set by cosmic-horizon scale) supports *some* form of flat rotation curve, but the specific scaling with M_b depends on the deep-regime structure that isn't yet articulated.

If ED-substrate eventually articulates the cross-term structure such that a² = a_N · a_0, slope-4 BTFR follows. If it articulates a different structure, BTFR slope differs.

### 6.4 Aggregate

> **ED-substrate, used strictly, gives a transition acceleration of c·H₀ — within factor of 2π of empirical MOND a_0 — and supports flat rotation curves at large R, but does not uniquely derive slope-4 BTFR or the specific a_0 prefactor without additional substrate-level commitments.**
>
> **The prior memo's a_0 = c·H_0/(2π) result was derived using standard-physics machinery (Unruh, equipartition, Bekenstein-Hawking).** ED-substrate is consistent with that result but doesn't force it from its own ontology alone. The 2π factor is the visible signature of imported standard-physics geometric structure.
>
> **The honest position:** ED-substrate is in the right structural neighborhood for galactic-scale gravity but is not yet articulated finely enough to derive the empirical a_0 prefactor or slope-4 BTFR uniquely. Either ED's substrate must be sharpened (to derive the Verlinde-style cross-term structure from native ontology), or the standard-physics derivation must be accepted as ED-compatible (which is the previous memo's position) — but the latter inherits standard-physics caveats and is not "derived from ED" in the strict sense.

---

## 7. What this revision changes about the program

### 7.1 The program-level picture, more honestly

- **Newton's law:** derived cleanly from ED-substrate (substrate-rules memo). Robust.
- **Transition scale ~ c·H₀:** derived cleanly from ED-substrate (this memo). Within factor 2π of empirical a_0.
- **Specific a_0 prefactor:** not derivable from ED-substrate alone. Standard-physics derivation gives c·H_0/(2π); ED-substrate alone gives c·H_0.
- **Deep-regime structural relation a² = a_N · a_0:** not derivable from ED-substrate alone. Standard-physics (Verlinde) derives it; ED-substrate-only analysis leaves the deep-regime relation underspecified.
- **Slope-4 BTFR:** follows from Verlinde's deep-regime relation, not from ED-substrate alone.

### 7.2 Compared to the four-arc closure

The four-arc closure (DM.0/1/G/MCD) ruled out field-theoretic ED gravity. The substrate-level analysis improves on that:

- Newton recovered structurally.
- Transition scale c·H₀ derived from ED-native ontology.
- Slope-4 BTFR is plausibly compatible (within factor 2π) with the substrate framework, if the Verlinde-style deep-regime structure is accepted.

But the substrate-level analysis is **not yet a clean substrate-only derivation of empirical galactic dynamics.** It's substrate-compatible-with-standard-MOND-physics rather than substrate-derives-MOND.

### 7.3 What the prior memo was actually showing

The prior memo's a_0 = c·H_0/(2π) result, which matched empirical to ~10%, was real — but it was a calculation showing **ED is consistent with standard physics' MOND derivation**, not **ED forces MOND from its own ontology**. The 2π factor was imported via Unruh, not derived from ED-substrate.

This is a more honest characterization than I gave earlier. The position is still strong (ED is consistent with empirical galactic dynamics), but it's a different kind of result than I claimed.

---

## 8. Recommended Next Step

Three concrete actions, in priority order:

1. **Resolve the 2π question by sharpening ED-substrate's geometric structure.** The 2π factor in standard physics comes from Euclidean-time periodicity in Rindler frames. The ED-substrate analog would come from how chain-decoupling-surfaces "wrap" the chain in the substrate's relational adjacency structure. This is a foundational substrate question: does ED's local-step dynamics naturally produce a 2π factor in the chain's experienced fluctuation rate (giving γ_chain = a/(2π·c) instead of a/c)? If yes, ED-substrate gives a_0 = c·H_0/(2π) natively. If no, ED-substrate gives a_0 = c·H_0, and the discrepancy with empirical is structural. **This is the immediate next step.**

2. **Articulate the cosmic-horizon / local-mass cross-term structure in ED-native terms.** ED-06 + ED-10 don't specify how commitment-irreversibility density at a screen combines cosmic-horizon and local-mass contributions. This specification is what determines the deep-regime relation (a² = a_N · a_0 vs alternatives) and therefore the BTFR slope. The articulation should be derived from ED-substrate principles (decoupling surfaces, ED-gradient fluctuation rates, participation-bandwidth bounds), not imported from Verlinde-thermodynamics.

3. **Empirically test the ED-substrate prediction a_0 = c·H_0 against rotation-curve fits using different interpolation functions.** Empirical MOND a_0 ≈ 1.2 × 10⁻¹⁰ m/s² is determined using a specific μ-function (typically the "simple" or "standard" one). Different μ-functions give different best-fit a_0 values. If any reasonable μ-function gives best-fit a_0 ≈ c·H_0 ≈ 7 × 10⁻¹⁰ m/s², ED-substrate's prediction is empirically viable without requiring the 2π factor. If no reasonable μ-function gives this, the discrepancy is real and constrains the substrate ontology.

The substrate-level program is now more honestly characterized. **ED is in the right structural neighborhood for galactic gravity, with the transition scale derivable from native ontology. The specific a_0 prefactor and the deep-regime structural relation remain dependent on either substrate articulation not yet done (item 1, item 2) or on importing standard-physics machinery (the prior memo's approach, which is consistent but not strictly substrate-derived).**

Status: complete.
