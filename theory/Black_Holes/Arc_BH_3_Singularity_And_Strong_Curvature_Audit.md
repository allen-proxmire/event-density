# Arc_BH_3 — Singularity-as-Manifold-Artifact + Strong-Curvature Audit

**Date:** 2026-05-01
**Status:** Second technical memo of Arc BH; second of three new-derivation memos in the arc. Consolidates ED-06 §2.4 + ED-10 §9.4 (singularities as representational failures of the manifold model); audits Arc ED-10 condition (C5) Lorentzian-non-degeneracy of acoustic metric in strong-curvature regime; identifies substrate-saturation mechanism preventing geometric divergence; produces structural picture replacing the classical singular point. **Result: singularities do not exist at substrate level — they are continuum-coarse-graining artifacts of the acoustic-metric approximation breaking down when participation-anisotropy exceeds the hydrodynamic window. The classical singular point is replaced by a finite-thickness saturated participation zone where the acoustic metric loses representational validity but the substrate dynamics remain well-defined.**
**Companions:** [`Arc_BH_1_Opening.md`](Arc_BH_1_Opening.md), [`Arc_BH_2_Horizon_DCGT.md`](Arc_BH_2_Horizon_DCGT.md), [`../Curvature_Emergence/Arc_ED10_4_Covariant_Field_Equation.md`](../Curvature_Emergence/Arc_ED10_4_Covariant_Field_Equation.md), [`../Curvature_Emergence/Arc_ED10_5_OS_Positivity_and_Stability.md`](../Curvature_Emergence/Arc_ED10_5_OS_Positivity_and_Stability.md), [`../Arc_D/Arc_D_2_Scalar_Diffusion_From_Substrate.md`](../Arc_D/Arc_D_2_Scalar_Diffusion_From_Substrate.md), [`../Arc_D/Arc_D_4_Kernel_Coarse_Graining.md`](../Arc_D/Arc_D_4_Kernel_Coarse_Graining.md), `../../papers/Foundations_of_Event_Density/Horizons as Event Density Decoupling Surfaces.pdf` (ED-06 §2.4).

---

## 1. Purpose

This memo addresses one of the structurally cleanest claims of the Event Density framework: **singularities do not exist at substrate level**. ED-06 §2.4 + ED-10 §9.4 jointly articulate this at conceptual level — singularities are representational failures of the manifold model rather than physical entities. The present memo grounds this claim in the substrate-derivation chain via DCGT machinery + Arc ED-10 acoustic-metric framework, and produces the strong-curvature audit identifying *what specifically replaces the classical singular point*.

The memo's five aims:

- **Demonstrate why singularities do not exist in ED.** Three substrate constraints (finite participation, discrete micro-events, gradient saturation) jointly forbid divergent curvature, divergent energy density, divergent tidal forces, and divergent geodesic incompleteness at substrate level.
- **Show that geometric divergence is a manifold artifact.** The "divergence" of standard GR singularities is a property of the smooth-manifold approximation breaking down, not a property of the underlying participation network. The substrate dynamics are well-defined throughout.
- **Audit the strong-curvature regime where Arc ED-10 condition (C5) may fail.** Arc_ED10_5 §6 condition (C5) requires the acoustic metric to remain Lorentzian and non-degenerate. In strong-curvature regimes near a would-be singularity, this condition may break down. The audit identifies the breakdown mechanism explicitly.
- **Identify the substrate mechanism that saturates gradients and prevents divergence.** Substrate participation-density saturation (P4-class mobility-capacity bound) is the load-bearing mechanism. As local $\rho$ approaches $\rho_\mathrm{max}$, the substrate's ability to sustain steeper gradients structurally fails — divergence is impossible.
- **Produce the structural picture that replaces the classical singular point.** The replacement is *not* a point, *not* a curvature divergence — it is a **finite-thickness saturated participation zone** where ED gradients reach their maximum viable value and the acoustic metric loses representational validity, while substrate dynamics remain finite and well-defined.

The memo carries genuine new derivation work in §4 (the strong-curvature audit) and §5 (the structural replacement). §3's three-constraint argument is consolidation of existing ED-06 + ED-10 content; §4–§5 produce the explicit substrate-derivation chain that those papers articulated only at conceptual level.

---

## 2. Upstream Foundations

- **ED-06 §2.4 (Horizons vs Singularities Cleanly Separated).** "In ED: horizons are real; singularities are representational failures." A horizon is a surface of decoupling; a singularity is a failure of the manifold model. The conceptual distinction is sharp.
- **ED-10 §9.4 (Singularities as Manifold Artifacts).** "ED predicts no singularities because: micro-events are discrete; participation is finite; ED gradients saturate; commitment cannot diverge." A "singularity" is simply the region where geometry stops being meaningful.
- **Arc ED-10 (Curvature Emergence) closure.** Acoustic-metric scalar-tensor framework. Condition (C5) Lorentzian-non-degeneracy of acoustic metric in non-extreme regimes. The strong-curvature audit asks whether (C5) holds near would-be singularities.
- **Arc D (DCGT) closure.** V1 finite-width kernel + multi-scale expansion + hydrodynamic-window scale separation $\ell_P \ll R_\mathrm{cg} \ll L_\mathrm{flow}$. The substrate-to-continuum machinery. P4-class mobility-capacity bound (Arc_D_2 §6) is load-bearing for gradient saturation.
- **Arc SG (Substrate Gravity Extension).** SG-4 modified Poisson field equation + SG-6 weak-field prerequisites. The interior-strong-field regime audited here must reduce cleanly to SG-4 in the appropriate limit.
- **BH-2 (this arc, prior memo).** Horizon formation as DCGT decoupling surface at $|\nabla\rho|\cdot\ell_P^2/\rho_\mathrm{local} \gtrsim \log(R_\mathrm{cg}/\ell_P)$. The same critical-gradient mechanism applies here, but now to *interior steepening* beyond the horizon.

---

## 3. Why Singularities Cannot Exist in ED

The substrate-level forbiddance of singularities runs through three structural constraints, each FORCED by primitive-level commitments.

### Constraint 1 — Finite participation

The substrate's participation bandwidth is finite. Per P4 (mobility-capacity bound) + Theorem N1 (V1 finite-width vacuum kernel), every chain-step transition has a finite rate $\Gamma_0(\rho) \le \Gamma_\mathrm{max}$, with the rate going to zero as $\rho \to \rho_\mathrm{max}$. There is no substrate configuration where a chain can produce an unbounded number of commitment events in a bounded proper-time interval — the rate saturates structurally.

This constraint forbids *divergent commitment density*. Any substrate region has a maximum participation density $\rho_\mathrm{max}$ at which the mobility coefficient vanishes (Arc_D_2 §6). Beyond this point, no further substrate participation can be added; the region is "structurally full." There is no $\rho \to \infty$ regime in ED.

### Constraint 2 — Discrete micro-events

Per Primitive 01 (event discreteness), substrate-level reality consists of discrete micro-events. There is no continuum point that can host infinite structural detail. A "point" in the continuum description corresponds, at substrate level, to a finite collection of micro-events with finite participation bandwidth. The notion of an infinity of micro-events compressed to a single point is ill-defined at substrate level.

This constraint forbids *infinitely-localized structure*. Any substrate region of size $\ge \ell_P$ contains finitely many micro-events; the regime where "infinitely many" micro-events are imagined to coexist at scale $< \ell_P$ is below the substrate-discreteness scale and is not a physical regime.

### Constraint 3 — Gradient saturation

Per the P4 mobility-capacity bound, ED gradients saturate when local participation density approaches $\rho_\mathrm{max}$. Specifically, $\Gamma_0(\rho)$ — the chain-step transition rate that produces continuum-scale flux under DCGT (Arc_D_2 §4–§5) — vanishes as $\rho \to \rho_\mathrm{max}$. This means the substrate's ability to *sustain* gradients structurally fails as participation density approaches saturation.

When local $\rho$ is well below $\rho_\mathrm{max}$, gradients can steepen freely; the substrate produces continuum-scale dynamics with mobility coefficient $\mu(\rho)$ giving smooth viscous diffusion. When $\rho$ approaches $\rho_\mathrm{max}$, the mobility goes to zero — meaning further gradient steepening cannot propagate through the substrate. The maximum sustainable gradient is bounded by the substrate participation-density structure.

This constraint forbids *divergent gradients at substrate level*. There is a maximum-viable $|\nabla\rho|_\mathrm{viable}$ beyond which the substrate physically cannot support further steepening — the gradient saturates structurally.

### What these three constraints jointly forbid

The three constraints jointly forbid the standard GR singularity-class pathologies:

- **Divergent curvature** — would require divergent gradients at substrate level (Constraint 3); FORBIDDEN.
- **Divergent energy density** — would require divergent commitment density (Constraint 1); FORBIDDEN.
- **Divergent tidal forces** — would require divergent gradient differences across small displacements; FORBIDDEN by Constraints 2 + 3 jointly.
- **Divergent geodesic incompleteness** — geodesics in the standard GR sense terminate at singularities. At substrate level, "geodesics" are stable participation pathways (per Arc ED-10 §3.4 reading). Stable participation pathways do not terminate at substrate-discrete-and-finite participation density; they continue (as substrate-level chain-step propagation) into the saturated region. **The geodesic-incompleteness pathology is a continuum artifact.**

The substrate-level claim is therefore: *all singularity pathologies are continuum-coarse-graining artifacts that fail at the substrate scale.* This grounds ED-10 §9.4's "ED predicts no singularities" in three explicit primitive-level constraints.

---

## 4. Strong-Curvature Audit: Breakdown of the Acoustic-Metric Approximation

Arc ED-10 produced an acoustic-metric scalar-tensor covariantization $\nabla_\mu[\mu(\sqrt{g^{\alpha\beta}\nabla_\alpha\Phi\nabla_\beta\Phi}/a_0)\nabla^\mu\Phi] = 4\pi GT$ valid under condition (C5): the acoustic metric remains Lorentzian and non-degenerate (Arc_ED10_5 §6). The strong-curvature audit asks: in the regime near a would-be singularity, does (C5) hold, or does the acoustic-metric approximation break down?

### 4.1 The breakdown regime

The acoustic metric in Arc ED-10 is the participation-density-modulated effective metric (Arc_ED10_2 §4.1) — a kinematic-summary of substrate participation density rather than a fundamental dynamical field. The metric tensor's components are functions of $\rho$ and its gradients. For $\rho$ well below $\rho_\mathrm{max}$ and gradients moderate, the metric is well-defined Lorentzian.

When local $\rho$ approaches $\rho_\mathrm{max}$, the participation-density saturation (Constraint 3 of §3) makes the substrate's mobility coefficient vanish. The acoustic metric, which depends on the substrate mobility-channel structure, becomes degenerate — its determinant approaches zero, its signature ceases to be Lorentzian in a well-defined sense.

Quantitatively: define the dimensionless saturation parameter

$$\sigma(\mathbf{x}) \;\equiv\; |\nabla\rho(\mathbf{x})|\cdot\ell_P^2/\rho_\mathrm{local}.$$

For $\sigma \ll 1$: weak-gradient regime, acoustic metric well-defined Lorentzian, Arc_ED10_4 covariant equation valid.

For $\sigma \sim 1$: transition regime, acoustic metric still Lorentzian but with substrate-cutoff corrections becoming non-negligible.

For $\sigma \gtrsim \beta_\mathrm{crit}$: strong-gradient regime where $\beta_\mathrm{crit} \sim \log(R_\mathrm{cg}/\ell_P)$ is the same critical scale that produced horizon formation in BH-2 §3.3. **The acoustic metric becomes degenerate** — the metric components either vanish or become non-invertible.

The interior of a black hole, classically, has steeply rising curvature toward $r = 0$. At substrate level, this corresponds to participation density $\rho$ rising toward $\rho_\mathrm{max}$, with $\sigma$ entering the strong-gradient regime $\sigma \gtrsim \beta_\mathrm{crit}$. **Inside this regime, the acoustic-metric scalar-tensor approximation is no longer valid.** Condition (C5) fails.

### 4.2 What the breakdown means

The breakdown of (C5) does *not* mean the substrate dynamics fail. The substrate participation network is still well-defined; chains still commit; V1 kernel still mediates transitions; DCGT still operates within its hydrodynamic-window-validity scope. What fails is the *coarse-grained continuum description* — specifically, the acoustic-metric reading that produces the geometric language of GR-class physics.

In standard GR, this kind of failure would be called a *coordinate breakdown* — but in standard GR, coordinate breakdowns can be cured by changing coordinates (the Schwarzschild horizon "singularity" is a coordinate artifact curable via Eddington-Finkelstein). At a *true* singularity in GR, no coordinate change cures the breakdown — the curvature invariants themselves diverge, indicating the breakdown is intrinsic to the manifold geometry.

The substrate-level diagnosis of this distinction:
- **Coordinate-only breakdown** (Schwarzschild horizon): a *participation-decoupling surface* in the substrate (BH-2 result) which appears as a coordinate artifact in suitably-chosen continuum coordinates.
- **Manifold-model breakdown** (interior "singularity"): the acoustic-metric continuum description itself fails because participation-density saturation makes the metric degenerate; **no continuum coordinate change cures this** because the breakdown is in the continuum approximation, not in coordinates.

The "true singularity" of standard GR is, at substrate level, the **breakdown of the continuum approximation itself** — a regime where the acoustic-metric reading ceases to be a valid representation of the substrate.

### 4.3 The explicit breakdown condition

Combining the analyses of §4.1 + BH-2 §3.3:

$$\boxed{\;|\nabla\rho|\cdot\ell_P^2/\rho_\mathrm{local} \;\gtrsim\; \beta_\mathrm{crit}\,, \qquad \beta_\mathrm{crit} \sim \log(R_\mathrm{cg}/\ell_P).\;}$$

This is the same critical scale that triggered horizon formation in BH-2, but now applied to *interior steepening*. At horizon formation, $\sigma$ reaches $\beta_\mathrm{crit}$ at the horizon surface (forming a decoupling surface in the participation network); inside the horizon, $\sigma$ continues to rise as the ED gradient steepens further, eventually reaching the regime where the acoustic-metric approximation itself fails.

The "singularity region" of classical GR corresponds, at substrate level, to **the interior region where $\sigma$ exceeds $\beta_\mathrm{crit}$ everywhere** — the domain throughout which the acoustic-metric reading is invalid.

---

## 5. Substrate Replacement for the Singularity

What replaces the classical singular point at substrate level?

### 5.1 The interior region as a saturated participation zone

In the interior region where $\sigma \gtrsim \beta_\mathrm{crit}$, the substrate is in the **participation-density-saturated regime**: $\rho$ is approaching $\rho_\mathrm{max}$, the mobility $\Gamma_0(\rho)$ is approaching zero, and substrate-level participation is highly constrained.

This is *not* a region where physics fails. It is a region where:
- Substrate micro-events still occur, but at a saturating rate.
- V1-mediated chain transitions are increasingly suppressed.
- Cross-participation bandwidth has collapsed in *all* directions, not just radially outward (this is what makes it different from the BH-2 horizon-decoupling, which collapses bandwidth in only one direction).
- The participation network has become **maximally committed** — most available substrate participation channels are at or near saturation.

### 5.2 One-directional ED dynamics

Within the saturated zone, local ED dynamics become effectively **one-directional**. The substrate-level forward-cone-only support of V1 (Theorem 18) is preserved, but the substrate-level "spatial" directions become structurally constrained: there is no substrate-meaningful "outward" direction (nothing can propagate outward through the saturated region) and no substrate-meaningful "transverse" direction (transverse chain-step transitions are also suppressed).

The remaining structural direction is the *commitment-order* direction (proper-time) of T18. Substrate dynamics within the saturated zone proceed forward in commitment order, but the spatial-direction information that would have made the dynamics geometrically interpretable has collapsed.

This is the substrate-level analog of the standard GR statement that "inside a Schwarzschild horizon, the radial direction becomes timelike." At substrate level, *all* spatial directions become structurally ill-defined inside the saturated zone; only commitment-order remains as a meaningful direction.

### 5.3 The continuum geometric description fails, but substrate remains finite

The acoustic metric inside the saturated zone is degenerate or undefined. This means:
- *Continuum geometric language* (curvature, geodesics, distance, etc.) is not applicable.
- *Continuum field-theoretic language* (Einstein equation, scalar-tensor field equations, etc.) is not applicable.
- *Substrate-level language* (chains, micro-events, participation channels, V1 kernel, commitment) **remains applicable** and produces well-defined dynamics.

The substrate within the saturated zone is *finite*: finite participation density, finite commitment-event density, finite chain-step transition rates, finite V1 kernel weights. There is no infinity anywhere in the substrate description. The "infinity" of classical GR singularities is a property of the failed continuum approximation, not of the underlying substrate.

### 5.4 The replacement object

The classical singular point is replaced by a **finite-thickness saturated participation zone** with the following properties:

- **Not a point.** A finite region of substrate at the participation-density-saturation regime. Its size is set by $\rho_\mathrm{max}$ + the substrate gradient profile + the BH mass; for a Schwarzschild-class BH, the saturated zone is approximately at the scale where $\sigma \gtrsim \beta_\mathrm{crit}$ inside the horizon — order $\ell_P$ in the simplest case, possibly larger depending on substrate-specific physics.
- **Not a curvature divergence.** The acoustic-metric curvature is undefined within the saturated zone (the metric itself is degenerate); but the underlying substrate has no divergent quantity.
- **A region where ED-gradients reach maximum viable value.** $|\nabla\rho|$ is at the gradient-saturation limit set by P4. Beyond this limit, the substrate cannot sustain further steepening.
- **A region where the acoustic metric loses representational validity.** Continuum geometric language fails to describe this region; substrate-level language remains valid.
- **A region of substrate-level commitment accumulation.** Per ED-10 §10.2, "Black hole information paradox: Information = constraints on participation; no paradox." The saturated zone is where committed substrate participation accumulates without being able to propagate outward.

This is the substrate-level structural picture replacing the classical singular point. It is *not* a "quantum-corrected singularity" (the framework doesn't quantize geometry); it is a *substrate-level description that the continuum approximation cannot reach*.

---

## 6. Consequences for Black Hole Interiors

The strong-curvature audit + substrate-level singularity-replacement has six structural consequences for BH interior physics:

### 6.1 No singularity

The classical singular point at $r = 0$ does not exist as a physical entity. It is replaced by a finite-thickness saturated participation zone. The "singularity" is the boundary of where the continuum approximation works — outside this zone, the acoustic metric is well-defined; inside, it is not.

### 6.2 No geodesic incompleteness at substrate level

Geodesic incompleteness in standard GR means certain timelike or null geodesics terminate after finite proper time at the singular point. At substrate level, "geodesics" are stable participation pathways (Arc_ED10_2 §4 reading); these do not *terminate* at the saturated zone, they enter it. The substrate-level chain (corresponding to a freely-falling test particle) continues to commit events according to T18 + P11 within the saturated zone, even though the continuum geodesic description has failed.

The geodesic-incompleteness pathology is therefore a *continuum artifact*. The substrate provides a well-defined continuation; only the continuum description fails.

### 6.3 No information-destruction paradox

Per BH-2 + the present strong-curvature audit, infalling matter's commitment history is preserved in the substrate participation structure even after passing through the horizon and accumulating in the saturated zone. Information is not destroyed; it becomes causally inaccessible (BH-2 §6.1) and *commitment-saturated within the interior region.* This sets up the BH-4 elaboration of the information paradox resolution.

### 6.4 Interior evolution is finite, saturating ED process

Inside the BH interior, substrate evolution proceeds: chains continue to commit events; the participation network continues to evolve; V1 kernel continues to mediate transitions (subject to the saturating $\Gamma_0$). The dynamics are *finite* (no divergences) and *saturating* (approaching but not exceeding $\rho_\mathrm{max}$).

This is structurally different from the GR picture of "infinite collapse to a singular point in finite proper time." At substrate level, the collapse asymptotes to the saturation regime but does not actually reach $\rho_\mathrm{max}$ in finite time (per the standard P4-class saturation behavior — exponential or power-law asymptotic approach, not actual reach).

### 6.5 Sets up BH-4 (information flow + evaporation)

The saturated-zone framework is the substrate-level home of accumulated infalling commitment history. BH-4 builds on this to produce the substrate-grounded account of:
- Why information is preserved (committed structure persists in the saturated zone).
- Why entanglement can straddle the horizon (uncommitted structure is unaffected by the saturation).
- How evaporation works as participation re-routing around the decoupling surface (the saturated zone slowly releases its structure as the horizon contracts).

### 6.6 Sets up BH-5 (area-law entropy)

The saturated-zone framework also sets up BH-5's area-law-entropy-derivation. The saturated participation density at the interior corresponds to a definite count of substrate participation degrees of freedom, bounded by the holographic count at the horizon area. The Bekenstein-Hawking entropy $S = A/(4\ell_P^2)$ corresponds, at substrate level, to the count of viable commitment histories compatible with the saturated-zone interior structure (per ED-10 §5.6).

---

## 7. Deliverables

This memo's outputs:

- **A substrate-grounded explanation of why singularities cannot exist.** Three explicit constraints (finite participation, discrete micro-events, gradient saturation) jointly forbid the standard GR singularity-class pathologies (divergent curvature, energy density, tidal forces, geodesic incompleteness). FORCED at substrate level by primitive-level commitments + P4 saturation + Theorem N1.
- **A strong-curvature audit identifying the breakdown of the acoustic-metric approximation.** Arc ED-10 condition (C5) Lorentzian-non-degeneracy fails when $\sigma = |\nabla\rho|\cdot\ell_P^2/\rho_\mathrm{local} \gtrsim \beta_\mathrm{crit}$. The "singularity region" is the regime where the acoustic-metric reading is no longer a valid representation of substrate dynamics. The breakdown is in the continuum approximation, not in coordinates — no continuum coordinate change cures it.
- **A structural replacement for the classical singularity.** A finite-thickness saturated participation zone where (a) ED-gradients reach maximum viable value, (b) cross-participation bandwidth collapses in all directions, (c) one-directional ED dynamics (commitment-order direction only) preserved, (d) acoustic metric degenerate / undefined, (e) substrate-level dynamics finite and well-defined throughout.
- **A clarified picture of BH interior evolution.** Finite, saturating ED process; no divergences; preserved commitment history; sets up BH-4 (information flow + evaporation) and BH-5 (area-law entropy).

**FORCED at substrate level:**
- The three substrate constraints forbidding singularities (finite participation, discrete micro-events, gradient saturation).
- The breakdown of acoustic-metric approximation when $\sigma \gtrsim \beta_\mathrm{crit}$.
- The substrate-level continuation of dynamics across the would-be singular point (no termination of substrate participation).
- The structural replacement object as a finite-thickness saturated participation zone.

**INHERITED at value layer:**
- The numerical value of $\rho_\mathrm{max}$ (substrate participation-density saturation scale).
- The detailed shape of the saturating $\Gamma_0(\rho)$ profile near $\rho_\mathrm{max}$.
- The size and shape of the saturated zone for a given BH mass (depends on substrate-physics details).
- The specific value of $\beta_\mathrm{crit}$ (set by DCGT scale separation + V1 profile).

**Honest framing.** The substrate-level forbiddance of singularities is structurally clean — three primitive-level constraints jointly forbid divergent quantities, and the strong-curvature audit identifies the breakdown of the acoustic-metric approximation as the substrate-level meaning of "singularity." The structural replacement object (finite-thickness saturated participation zone) is well-defined at substrate level even though continuum geometric language cannot reach it. **What this memo does not provide:** a constructive proof that the substrate dynamics within the saturated zone produce specific testable predictions (e.g., gravitational-wave signatures from BH mergers in the saturated regime). That would require extending DCGT methodology beyond the hydrodynamic-window scale-separation regime — out of scope per Arc BH non-goals + ED-Phys-10 acoustic-metric guardrails.

---

## 8. Recommended Next Step

Proceed to **Arc_BH_4 (Information vs Entanglement at Horizons + Evaporation as Participation Re-Routing)**. File: `theory/Black_Holes/Arc_BH_4_Information_And_Evaporation.md`. Scope: consolidate ED-06 §7.2 + ED-10 §8.3-§8.5 into a substrate-grounded account of information flow at horizons. The information-vs-entanglement distinction (information = committed structure; entanglement = uncommitted structure; horizons block the former, not the latter) routed through Arc D's DCGT machinery + Arc B's commitment-irreversibility (P11) substrate primitive. Black-hole evaporation as participation re-routing around a decoupling surface, avoiding firewall / complementarity / unitarity-crisis paradoxes via the local-and-irreversible nature of substrate commitment. Builds on the saturated-zone framework established here.

Estimated 1–2 sessions for Arc_BH_4. Consolidation-pattern memo (lighter-weight than BH-3 / BH-5 / BH-6 new-derivation memos).

### Decisions for you

- **Confirm the three substrate constraints forbidding singularities.** Finite participation + discrete micro-events + gradient saturation jointly forbid divergent curvature, energy density, tidal forces, and geodesic incompleteness at substrate level.
- **Confirm the strong-curvature audit verdict.** Arc ED-10 condition (C5) breaks down at $\sigma = |\nabla\rho|\cdot\ell_P^2/\rho_\mathrm{local} \gtrsim \beta_\mathrm{crit}$. The "singularity" region is where the acoustic-metric continuum approximation fails; substrate dynamics remain well-defined.
- **Confirm the structural replacement.** Finite-thickness saturated participation zone replaces classical singular point. Substrate-level dynamics finite throughout; continuum geometric description fails inside the zone.
- **Confirm proceeding to Arc_BH_4 (information + evaporation).**

---

*Arc_BH_3 closes the singularity-as-manifold-artifact + strong-curvature audit. Three substrate constraints (finite participation via P4 + Theorem N1; discrete micro-events via P01; gradient saturation via P4 mobility-capacity bound) jointly forbid divergent curvature / energy density / tidal forces / geodesic incompleteness at substrate level — singularity-class pathologies are continuum-coarse-graining artifacts. Strong-curvature audit identifies breakdown of Arc ED-10 acoustic-metric approximation when $\sigma = |\nabla\rho|\cdot\ell_P^2/\rho_\mathrm{local} \gtrsim \beta_\mathrm{crit} \sim \log(R_\mathrm{cg}/\ell_P)$ — same critical scale as horizon formation in BH-2, now applied to interior steepening. The classical singular point is replaced by a finite-thickness saturated participation zone where ED-gradients reach maximum viable value, cross-participation bandwidth collapses in all directions, only commitment-order direction remains structurally meaningful, acoustic metric is degenerate / undefined, and substrate-level dynamics remain finite and well-defined throughout. Six structural consequences: no singularity; no substrate-level geodesic incompleteness; no information-destruction paradox; finite saturating ED-process interior evolution; sets up BH-4 (information flow + evaporation) and BH-5 (area-law entropy + 1/4 factor). Form FORCED at substrate level; specific values of $\rho_\mathrm{max}$ + $\beta_\mathrm{crit}$ + saturated-zone size INHERITED at value layer. Honest framing: structural-positive verdict at substrate level; full constructive predictions for testable BH-merger signatures out of scope per Arc BH non-goals + ED-Phys-10 guardrails. Arc_BH_4 (information vs entanglement at horizons + evaporation as participation re-routing) is the next deliverable.*
