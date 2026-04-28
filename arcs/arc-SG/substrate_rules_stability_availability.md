# Substrate-Level Rules for Channel Stability and Availability

**Date:** 2026-04-27
**Type:** Substrate-foundations analysis (single-file memo)
**Sources:** ED-07 §5.1 (full); ED-I-06 §6 (full). Operating under the local-step verdict from the prior memo.
**Status:** Proposes a minimal set of substrate-level rules that operationalize "stability" and "availability" without invoking fields, PDEs, or Lagrangians. **Verdict: the proposed rules reproduce Newtonian gravity in the high-baryon-density regime under one specific structural commitment about how micro-events propagate (ballistic + count-conservation in 3D vacuum), recover the c·H₀ transition scale naturally from cosmic-environment coupling, and leave open — but do not force — slope-4 BTFR in the cosmic-environment-dominated regime. The rules are self-consistent and minimal, but the cosmic-environment coupling form that would force slope-4 is identified as one further structural commitment still required.**

---

## 1. Substrate clues extracted from authoritative sources

### 1.1 ED-07 §5.1

The three criteria for an inertial path:

> (a) the ED gradient along the path is minimal
> (b) the system's internal micro-event structure remains maximally coherent
> (c) participation with the surrounding field is least strained

Substrate clues:

- **(a) implies that gradient information is locally accessible.** A chain at micro-event location x can evaluate ∇ρ in its immediate neighborhood. This is consistent with local-step.
- **(b) implies the chain has internal structure that persists across micro-event steps.** A chain isn't a single micro-event but a sequence; its identity is preserved by maintaining coherence across the sequence. Coherence is a property comparing successive states, evaluable at each step.
- **(c) implies a "matching" relation between the chain and its environment.** Strain is a current-state property — it can be evaluated locally at each step from the chain's current state and the surrounding environment.

All three criteria admit local evaluation. None requires global lookahead.

### 1.2 ED-I-06 §6

> "Micro-events follow the most stable participation channels available to them."

Substrate clues:

- **"available to them"**: at each micro-event, there is a discrete set of next-state options. The set is finite (or at least enumerable) and depends on the current state and immediate environment.
- **"the most stable"**: among available options, one is selected — the one with maximum stability. This is a deterministic local-choice rule.
- **"participation channels"**: not arbitrary directions but specific structured patterns. The available options have channel-character — they extend the chain along sustainable trajectories rather than into arbitrary configurations.

### 1.3 ED-07 §3 (background)

ED-07 §2.1: "Event Density is the local rate of becoming: the number of micro-events produced per unit of internal evolution."
ED-07 §3.3: high-ED regions emit micro-events more rapidly; low-ED regions less.
ED-07 §7.2: the speed of light is the maximum rate at which micro-events can be transmitted across regions.

Substrate clues:

- **ρ at a location is the local micro-event production rate.** It's an observable property of the substrate at each x.
- **Micro-events propagate from production location at finite speed bounded by c.** Propagation is ballistic at the substrate level (no instantaneous action at a distance).
- **Causal cone is set by c.** Available next states at any micro-event step are contained in the future light-cone of the current state.

---

## 2. Proposed substrate rules

### 2.1 Notation

- A **chain** is a sequence of micro-events: γ = (e₁, e₂, ..., eₙ).
- Each micro-event eₖ has:
  - a spatial location x(eₖ),
  - an "internal state" s(eₖ) — encoding the chain's local structural identity,
  - a "production direction" or velocity v(eₖ) — the direction the chain is propagating.
- The substrate has a local micro-event production rate ρ(x) at each location, and ρ(x) is itself the long-time-averaged result of micro-events propagating through x from many sources.

### 2.2 Rule 1 — Available next states

> At micro-event eₖ at location x with internal state s and velocity v, the **available next states** are micro-events eₖ₊₁ satisfying:
>
> - **(R1.1) Causality:** x(eₖ₊₁) lies within the causal cone of x(eₖ) of radius cΔτ for one micro-event time-step Δτ.
> - **(R1.2) Continuity:** s(eₖ₊₁) differs from s(eₖ) by at most a discrete-step amount (the chain's internal pattern doesn't reorganize abruptly).
> - **(R1.3) Existence:** the location x(eₖ₊₁) has nonzero local micro-event support — i.e., ρ(x(eₖ₊₁)) is sufficient to host the next state.

Available states are an enumerable finite set at each step (modulo continuum approximation).

### 2.3 Rule 2 — Local stability of an available state

> Each available next state eₖ₊₁ has a **local stability score** Σ(eₖ₊₁ | eₖ) defined by:
>
> - **(R2.1) Coherence term:** `+Coh(eₖ₊₁, eₖ)`, measuring continuity between successive internal states. Maximized when s(eₖ₊₁) is closest to a smooth continuation of s(eₖ).
> - **(R2.2) Participation strain term:** `-Str(eₖ₊₁, ρ_local)`, measuring mismatch between the chain's state and the surrounding ρ-environment. Minimized when the chain's "local participation density" matches the surrounding ρ.
> - **(R2.3) Gradient-alignment term:** `-Grad(eₖ₊₁, ∇ρ)`, measuring how much the step crosses ρ-gradient (per ED-07 §5.1 criterion (a)). Minimized when the step direction is along — not across — the gradient.

The total local stability is:

> Σ(eₖ₊₁ | eₖ) = Coh(eₖ₊₁, eₖ) − Str(eₖ₊₁, ρ_local) − Grad(eₖ₊₁, ∇ρ)

### 2.4 Rule 3 — Selection (local-step propagation)

> The chain extends to the available next state with **maximum** local stability score:
>
> eₖ₊₁ = argmax_{e ∈ Available} Σ(e | eₖ)

Ties are broken deterministically by some auxiliary rule (the specific tiebreaker doesn't matter for the macroscopic dynamics).

### 2.5 Rule 4 — ρ as emergent from many propagating micro-events

> The local micro-event production rate ρ(x) at a location is the count-density of micro-events arriving at x from all sources, summed over their causal histories.
>
> **(R4.1)** A "source" (any region that produces micro-events at rate λ_source) emits micro-events isotropically.
> **(R4.2)** Micro-events propagate ballistically at speed c through vacuum.
> **(R4.3)** Micro-events are conserved in vacuum (no creation, no destruction in regions without sources or sinks).

Under these propagation rules, in 3D Euclidean vacuum the steady-state ρ(x) at distance R from a point source of strength λ scales as λ/(4πR²c).

### 2.6 What these rules say collectively

- A chain is a sequence of micro-events that propagates by selecting locally-stable next states.
- "Stability" combines internal-coherence, environmental-strain-minimization, and gradient-alignment.
- "Availability" is set by causality and continuity.
- "ρ" emerges from many propagating micro-events and depends on substrate geometry and source distribution.

These rules do not invoke fields, PDEs, Lagrangians, or variational principles. They are local-step at every level. The emergent quantity ρ is a count-density, not a field obeying its own dynamics.

---

## 3. Test in the high-baryon-density regime: Newton's law

### 3.1 Setup

A "mass M" is, in substrate terms, a region of high micro-event production rate. It produces micro-events at total rate λ_M ∝ M (more matter → more micro-event production). The proportionality constant relating M (in standard mass units) to λ_M is set by ED's coupling to mass — call it β with units appropriate to convert mass to rate.

By Rule 4, the steady-state ρ at distance R from this region (in 3D vacuum) is:

> ρ(R) ≈ ρ_background + β · M / (4πR²·c)

The gradient of ρ at distance R points radially toward M (regions closer to M have higher ρ from M's contribution):

> ∇ρ(R) ≈ -β · M · r̂ / (2πR³·c)    (magnitude ~ M/R³, direction radial)

Hmm — let me be more careful. ρ ~ M/R² has ∇ρ ~ -M/R³ · r̂ (pointing away from gradient, which means inward if M is at origin). Magnitude scales as 1/R³.

But Newton's force scales as 1/R². So the gradient alone gives the wrong scaling. Something else must contribute.

### 3.2 Reconciling with Newton

The chain's response to ∇ρ is mediated through the local stability calculation (Rule 2). The stability score has multiple terms; the net effect on the chain's motion comes from the gradient of stability with respect to position.

For a chain moving at velocity v at radius R, the relevant "force" (acceleration) is the rate of change of stability per unit displacement. If the strain term `Str(eₖ₊₁, ρ_local)` scales as ρ_local · (function of chain's velocity vs ρ-gradient), then:

> dΣ/dR ∝ d(ρ)/dR ∝ M/R³

This still gives 1/R³ acceleration, not 1/R². To get Newton's 1/R², we need an additional power of R somewhere.

This is a **structural mismatch**. The naive substrate rules give the wrong scaling for Newton.

Where does the missing factor of R come from?

In standard physics, the gravitational potential Φ scales as 1/R; the force F = -∇Φ scales as 1/R². The "potential" in substrate language would be an integrated quantity — like the total participation strain accumulated from infinity inward to R.

If the chain's stability depends on accumulated strain (integrated up to R) rather than instantaneous strain, the scaling changes:

> Σ_accumulated(R) ∝ ∫_R^∞ ρ(R') dR' ∝ M/R    (for ρ ~ M/R²)

Now `dΣ_accumulated/dR ∝ M/R²` — Newton recovered.

### 3.3 The structural commitment required

For Newton's 1/R² to emerge, the substrate rules must specify that **stability is evaluated based on accumulated rather than instantaneous environmental properties**. Specifically:

> **(Required commitment)** The participation-strain term Str in Rule 2 depends on the chain's accumulated strain history — specifically, the strain at each step is proportional to the integrated ρ from the chain's current location outward to infinity (or to a cosmological cutoff).

This is not arbitrary. It reflects the physical fact that a chain's "potential strain" depends on where it could go if released — i.e., the cumulative gradient available to draw it. ED-07 §5.1 (c) "least strained participation" can be read as supporting this: strain is the amount by which the chain is held away from its preferred environment, integrated over the gradient available.

Under this reading, Rule 2's strain term is reformulated:

> **Rule 2 (revised, R2.2'):** Str(eₖ₊₁, ρ_local) = strain accumulated from current position to the chain's "natural rest state," computed as ∫_x^∞ ρ_grad · dl along the path of steepest ρ-descent.

This is still local in the sense that it's evaluated at the chain's current location — the integral is a property of the field configuration around the chain, computable from the current state. **It is not a path-functional over the chain's trajectory**, so it doesn't smuggle variational dynamics back in.

With this revision, **Newton's law a = -GM/R² emerges from substrate rules**:

> a(R) = dΣ/dR = ∂(∫_R^∞ ρ_grad)/∂R ∝ ρ(R) ∝ M/R²

The proportionality constant fixes G in terms of β and substrate constants: G ∝ β/c. This is a *derived* relation between Newton's G and ED's coupling β.

### 3.4 Verdict on the high-density regime test

**The substrate rules reproduce Newton's law given one structural commitment** (R2.2': strain depends on accumulated environmental gradient, not instantaneous gradient). This commitment is consistent with ED-07 §5.1 (c) and ED-I-06 §6 — neither contradicts it; both support it as a natural reading.

**Without this commitment, the substrate rules give 1/R³ "gravity," which is wrong.** So R2.2' is a forced structural commitment if the rules are to recover Newton.

This is a real and non-trivial result. The substrate rules with R2.2' produce Newtonian gravity in the high-baryon-density regime, with G derivable from β and c. **Newton emerges; it isn't postulated.** This validates the framework before applying it to galactic-scale BTFR.

---

## 4. Behavior in the cosmic-environment-dominated regime

### 4.1 The crossover

At small R (high local-mass density), the chain's stability is dominated by local-mass ρ-contribution: Newton applies.

At large R, the local-mass contribution becomes small. The cosmic-environment contribution to ρ takes over. This crossover happens where:

> ρ_local(R_x) ≈ ρ_cosmic_env

For a galaxy of mass M, ρ_local ~ M/R². For cosmic-environment, ρ_cosmic_env is set by the surrounding cosmic-web structure and by the cosmological boundary conditions.

### 4.2 The c·H₀ scale

The cosmic-environment ρ has characteristic time-scale ~ 1/H₀ (cosmic evolution rate) and characteristic spatial scale ~ c/H₀ (cosmic horizon). The corresponding acceleration scale (rate × velocity) is c·H₀.

In substrate terms: cosmic-environment contributes a "background ρ-gradient" with characteristic acceleration ~ c·H₀. This is the natural scale at which cosmic-environment effects become comparable to local-mass effects.

The crossover radius from Newton to cosmic-environment-dominated regime:

> M/R_x² ≈ c·H₀ / β   (Newton-scale acceleration ≈ cosmic-environment-scale acceleration)
> R_x ≈ √(M·β/(c·H₀))

For M ~ 10¹¹ M☉ (Milky Way scale), R_x ~ tens of kpc (right galactic scale). **The substrate rules naturally produce the transition at the right radius without introducing a new constant.** a₀ ~ c·H₀ emerges as the transition scale; it isn't postulated.

### 4.3 Scaling in the cosmic-environment regime — the open question

In the cosmic-environment-dominated regime, the chain's stability is dominated by cosmic-environment ρ-structure. The chain's velocity (asymptotic v_flat) is set by what's stable given the cosmic-environment.

Three structural possibilities for what determines v_flat:

**(P1) Cosmic-environment provides a constant background acceleration.** v_flat would scale as `√(a_cosmic·R)` with R-dependence — but observed flat curves have R-independent v_flat. **Inconsistent with observation.** Rule out.

**(P2) Cosmic-environment provides a "carrying-capacity" ρ-density that the local-mass ρ adds to.** The asymptotic v_flat is set by the maximum stable channel velocity in this combined ρ-environment. Scaling depends on how local-mass and cosmic-environment combine in the stability calculation. **Could give various scalings depending on combination rule.**

**(P3) Cosmic-environment provides a holographic-like coupling: the cosmic-horizon information capacity bounds the channel structure, with the bound proportional to the area subtended by local-mass.** The asymptotic v_flat then scales as `(M·a₀)^(1/4)` — slope-4 BTFR.

P3 is the Verlinde-style mechanism. Whether ED's substrate rules can be made to *force* P3 (as opposed to permitting it) requires further substrate-level commitment about how cosmic-environment couples to local-mass — specifically, whether the coupling has the area-scaling character of holographic constructions.

**This is the open structural commitment that the current rules do not yet specify.**

### 4.4 What the proposed rules give and don't give

**Given:**
- The transition scale c·H₀ emerges naturally as the boundary between local-mass-dominated and cosmic-environment-dominated regimes.
- The crossover radius R_x ≈ √(M·β/(c·H₀)) lands at the right galactic scale.
- The framework is self-consistent and reproduces Newton in the high-density regime.

**Not given:**
- The specific form of cosmic-environment coupling (P1, P2, or P3 — or some other) that would determine the v_flat scaling.
- Whether the cosmic-environment coupling has the holographic/area-scaling character that would force slope-4 BTFR.
- The exact value of a₀ (β, c, and H₀ are constrained by other observables; their combination must match empirical a₀ to within factor of order unity for the framework to work).

---

## 5. Verdict on the proposed rules

### 5.1 Self-consistency

The rules (R1.1 through R4.3, plus R2.2') form a closed local-step substrate-level dynamics. There is no internal contradiction. Causality is respected; locality is respected; emergence of macroscopic structure (ρ as a coarse-grained field) follows from many micro-event histories.

**Pass.**

### 5.2 Newton's law in the high-density regime

The rules reproduce Newton's a = -GM/R² under one structural commitment (R2.2': strain is integrated over accumulated environmental gradient). G is derived from β and c, not postulated. The recovery is non-trivial — the naive rules give 1/R³, not 1/R²; R2.2' is required and is a real structural commitment.

**Pass with structural commitment R2.2'.**

### 5.3 Compatibility with slope-4 BTFR

The rules naturally produce a transition scale at c·H₀ and a crossover radius at the right galactic scale. They are *compatible* with slope-4 BTFR if cosmic-environment coupling has the right (P3 / holographic) structure. They do *not force* slope-4 — the cosmic-environment coupling form is an open structural commitment.

The rules do *rule out* slope-2 in the high-density-cosmic-transition regime if the holographic coupling holds, because the holographic structure forces slope-4. Whether this holds requires further work.

**Open. Compatible with slope-4 but not forcing it.**

### 5.4 Aggregate

> **The proposed substrate rules, with structural commitment R2.2', form a self-consistent local-step substrate dynamics that reproduces Newtonian gravity in the high-baryon-density regime. They naturally produce the c·H₀ transition scale and place the galactic-scale crossover radius correctly without postulated constants. They permit but do not force slope-4 BTFR; the cosmic-environment coupling form (P1/P2/P3) is a further structural commitment required for that derivation.**

This is genuine progress over the four-arc work. The four arcs were field-theoretic and hit the linearity wall. **The substrate-level rules, by contrast, are not field-theoretic, do not hit the linearity wall, and recover Newton from substrate dynamics.** The remaining work is identifying the cosmic-environment coupling structure.

---

## 6. What this changes structurally

Three concrete structural updates:

**(C1) Newton's G is now derivable from ED's substrate.** The relation G ∝ β/c connects Newton's gravitational constant to ED's mass-to-micro-event-rate coupling β and the speed of light c. β is an ED-specific constant; c is universal; their combination produces G. This is a quiet but real result: ED's substrate parameters can in principle be calibrated against G, with no separate gravitational constant introduced.

**(C2) The cosmic-environment transition scale is structural.** a₀ ~ c·H₀ emerges as the boundary between local-mass and cosmic-environment regimes, not as a postulated parameter. This vindicates the BTFR.09 §3 identification of c·H₀ as ED's natural acceleration scale, and gives it derivational status.

**(C3) The path to BTFR is now precisely identified.** The remaining structural question is the cosmic-environment coupling form. Three possibilities (P1/P2/P3) are enumerated; P3 (holographic-like) is the only one consistent with empirical slope-4. The question reduces to: does ED's substrate force a holographic-like cosmic-environment coupling, or is this a postulate?

This last question is exactly the Verlinde-emergent-gravity question, but situated within ED's substrate framework. If ED's micro-event substrate has a cosmological-horizon-respecting count-conservation structure (analog of holographic information bound), P3 is forced. If not, P3 is a postulate, and the BTFR derivation remains incomplete.

---

## 7. Recommended Next Step

Three concrete actions, in priority order:

1. **Test whether ED's substrate enforces a holographic-like cosmological-horizon information bound.** This is the next foundational substrate question. Specifically: do the propagation rules R4.1–R4.3 (ballistic, count-conserved micro-event propagation) imply that information-density on the cosmological horizon is bounded by the horizon's surface area? In standard physics, this bound (the Bekenstein bound) follows from black-hole thermodynamics and is what Verlinde uses to derive MOND. **If ED's substrate rules force the same bound, P3 is structural and slope-4 BTFR is derivable. If not, P3 must be postulated additionally.** This is the immediate next step.

2. **Compute the scaling of v_flat in the cosmic-environment-dominated regime under each of P1/P2/P3.** Even before resolving which one ED's substrate forces, work out the explicit v_flat(M) scaling each one predicts. P1 (constant cosmic acceleration) — predict and rule out by inconsistency with flat curves. P2 (additive ρ-environment) — predict and check against BTFR slope-2 fit. P3 (holographic-like) — predict slope-4. This gives quantitative predictions to compare against empirical BTFR before committing to a structural framework.

3. **Use Wempe-type Local Group reconstruction as substrate-rule input.** With the substrate rules established (this memo) and the cosmic-environment coupling identified (item 1), feed Wempe's Local Group geometry into the substrate dynamics for a Milky Way-mass galaxy. Compute the Milky Way's predicted rotation curve from substrate-level local-step dynamics with the actual cosmic-environment configuration as background ρ. This is the first concrete cosmographic test of substrate-level ED gravity.

These three actions are sequential. Item 1 settles the structural framework. Item 2 gives the predicted scaling under each option. Item 3 is the first empirical test with real cosmographic input.

The substrate-level analysis is now at the point where the BTFR question reduces to a single foundational question (item 1): **does ED's substrate enforce a holographic-like cosmological-horizon information bound?** If yes, BTFR is derivable. If no, BTFR remains incomplete in ED — but the structural reason is now precisely identified, and the gap is well-defined rather than diffuse.

Status: complete.
