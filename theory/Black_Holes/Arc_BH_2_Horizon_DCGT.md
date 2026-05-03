# Arc_BH_2 — Horizon-as-Decoupling-Surface under DCGT

**Date:** 2026-05-01
**Status:** First technical memo of Arc BH. Consolidates ED-06 + ED-10 §4.4 + §8.2 horizon-as-decoupling-surface content; grounds in DCGT substrate-to-continuum machinery; derives horizon formation as a participation-bandwidth-collapse surface emerging from V1 finite-width kernel + multi-scale expansion under steep ED gradients. **Result: horizon-as-decoupling-surface FORCED at substrate level via DCGT-derived bandwidth-collapse mechanism; universalization across BH / Rindler / cosmological / acoustic horizons FORCED as the same structural object; geometric "event horizon" is the continuum-emergent shadow of the substrate decoupling surface.**
**Companions:** [`Arc_BH_1_Opening.md`](Arc_BH_1_Opening.md), [`../Arc_D/Arc_D_2_Scalar_Diffusion_From_Substrate.md`](../Arc_D/Arc_D_2_Scalar_Diffusion_From_Substrate.md), [`../Arc_D/Arc_D_4_Kernel_Coarse_Graining.md`](../Arc_D/Arc_D_4_Kernel_Coarse_Graining.md), [`../Arc_D/Arc_D_6_Synthesis_And_Theorem.md`](../Arc_D/Arc_D_6_Synthesis_And_Theorem.md), [`../Curvature_Emergence/Arc_ED10_4_Covariant_Field_Equation.md`](../Curvature_Emergence/Arc_ED10_4_Covariant_Field_Equation.md), [`../Substrate_Gravity/Arc_SG_3_Transition_Acceleration_Scaling.md`](../Substrate_Gravity/Arc_SG_3_Transition_Acceleration_Scaling.md), `../../papers/Foundations_of_Event_Density/Horizons as Event Density Decoupling Surfaces.pdf` (ED-06).

---

## 1. Purpose

This memo performs the first technical-derivation step of Arc BH. The aim is fourfold:

- **Derive horizon formation as a participation-decoupling surface using DCGT.** Take ED-06's interpretive definition of a horizon ("the surface at which cross-participation between two regions becomes one-way due to an extreme ED gradient") and produce the substrate-derivation chain that shows this is a FORCED structural consequence of the substrate primitives + V1 finite-width kernel + multi-scale expansion.
- **Show how steep ED-gradients + finite-width kernels + multi-scale expansion force a decoupling surface.** The mechanism: when ED gradients exceed a critical scale set by the V1 kernel width, the multi-scale expansion of cross-region V1-mediated chain-step propagation produces an exponentially-suppressed cross-participation bandwidth, leaving the surface effectively one-way for substrate signal flow.
- **Demonstrate that BH / Rindler / cosmological / acoustic horizons are the same structural object under DCGT.** Each is a surface where the same bandwidth-collapse mechanism produces the same one-way participation, with only the source of the steep ED gradient differing (mass/curvature, acceleration, cosmic expansion, fluid gradient). The unification is FORCED by the substrate mechanism.
- **Establish the substrate-level mechanism that replaces geometric "event horizons."** In standard GR, an event horizon is a global causal feature of the spacetime — a null surface separating regions that can communicate from regions that cannot. In the ED substrate, the surface is *not* a property of spacetime; it is a property of the participation network. The geometric event horizon is the continuum-emergent shadow of the substrate decoupling surface under acoustic-metric coarse-graining.

The memo is methodologically a **consolidation + DCGT-grounding memo** — most of the conceptual content is already articulated in ED-06 + ED-10 + Arc ED-10. The contribution of this memo is the explicit substrate-derivation chain routing those claims through Arc D's machinery.

---

## 2. Upstream Foundations

- **ED-06 (*Horizons as Event Density Decoupling Surfaces*, Feb 2026).** Formal definition: *"A horizon is the surface at which cross-participation between two regions becomes one-way due to an extreme ED gradient."* Two-observer reconciliation: infaller experiences smooth local ED, external observer experiences extreme mismatch — both descriptions arise from the same underlying ED gradient. Horizons cleanly separated from singularities (§2.4): horizons are real decoupling surfaces; singularities are representational failures.
- **ED-10 §4.4 (Horizons as Decoupling Surfaces).** A horizon forms when ED gradients become steep + participation bandwidth across the surface collapses + commitment histories diverge irreversibly. Produces causal disconnection, information inaccessibility, thermal behavior (Hawking/Unruh), entanglement across the boundary.
- **ED-10 §8.2 (Causal-Structure Emergence).** A horizon is a participation bottleneck. The participation network *splits into two disconnected regions* rather than anything physical "falling behind." This reframes BH / Rindler / cosmological / acoustic horizons as participation bottlenecks under a single structural mechanism.
- **Arc D (DCGT) closure.** V1 finite-width kernel + multi-scale expansion + hydrodynamic-window scale separation $\ell_P \ll R_\mathrm{cg} \ll L_\mathrm{flow}$. The methodology used here. Specifically Arc_D_2 (scalar diffusion from event-flux statistics) + Arc_D_4 (kernel coarse-graining) supply the bandwidth-collapse derivation chain.
- **Arc SG (Substrate Gravity Extension) closure.** SG-4 modified Poisson field equation + SG-6 weak-field prerequisites. The horizon machinery here must be consistent with the closed substrate-gravity baseline.
- **Arc ED-10 closure.** Acoustic-metric scalar-tensor structure — the metric is kinematic-summary of substrate participation density, not fundamental dynamical field. The continuum-limit interpretation of the substrate decoupling surface uses this framework.
- **Arc B (T18) closure.** V1 forward-cone-only support; the kernel-level arrow of time. Required because horizon formation is fundamentally directional — the one-way nature of cross-participation across the surface inherits from T18's primitive-level forward-cone causality.

---

## 3. Substrate Mechanism: Gradient Steepening + Bandwidth Collapse

The core substrate-derivation chain runs in three steps.

### 3.1 Steep ED-gradients produce local participation anisotropy

Consider two adjacent substrate regions $R_-$ and $R_+$ with cell-averaged participation densities $\rho_-$ and $\rho_+$, separated by a boundary surface $\Sigma$. Under DCGT (Arc_D_2 §3), the V1-mediated chain-step transition rate from $R_-$ to a substrate site at displacement $\boldsymbol{\delta}$ into $R_+$ is

$$\Gamma(\boldsymbol{\delta}; \rho_-, \rho_+) \;=\; \Gamma_0(\rho_\mathrm{local})\,K_{V1}(|\boldsymbol{\delta}|),$$

where $\Gamma_0$ is the local participation-bandwidth-modulated rate and $K_{V1}$ is the V1 finite-width spatial kernel.

When the ED-gradient $\nabla\rho$ across $\Sigma$ is small (gentle gradient), $\rho_-$ and $\rho_+$ are similar, $\Gamma_0$ is comparable on both sides, and chain-step transitions in both directions are roughly balanced. This is the standard substrate regime where DCGT scalar-diffusion (Arc_D_2) produces the canonical $\nabla\cdot(M(\rho)\nabla\rho)$ continuum-scale flux.

When the gradient becomes steep — specifically when $|\nabla\rho| \cdot \ell_P / \rho_\mathrm{local} \gtrsim 1$ — the local participation environment of a chain near $\Sigma$ is dominated by the gradient direction. The chain's available next-states are no longer isotropic; they are biased along the gradient. This is *local participation anisotropy* and it is the substrate-level analog of strong-curvature in GR.

### 3.2 V1 finite-width kernel suppresses cross-surface commitment

The V1 kernel has finite spatial width $\sim\ell_P$ (Theorem N1; Arc_D_4 §3). For chain-step transitions across $\Sigma$, the V1 kernel weights paths by their substrate displacement. In the regime where $\rho$ varies across the kernel's width — i.e., when $|\Delta\rho|_{\text{across width}} \sim |\nabla\rho|\cdot\ell_P \gtrsim \rho_\mathrm{local}$ — the kernel's effective support across $\Sigma$ is asymmetric: the chain finds it relatively easy to step *along* the gradient direction (toward higher $\rho$) but finds steps *against* the gradient (from high-$\rho$ to low-$\rho$ side) progressively suppressed.

The mechanism: $\Gamma_0(\rho)$ is a P4-class participation-bandwidth-modulated transition rate (Arc_D_2 §6). At high $\rho$, $\Gamma_0$ saturates toward zero (P4 mobility-capacity bound). A chain on the high-$\rho$ side near $\Sigma$ sees its forward (toward higher $\rho$) and backward (toward lower $\rho$) transition rates differ by a factor $\Gamma_0(\rho_+)/\Gamma_0(\rho_-)$. As $\rho_+ \to \rho_\mathrm{max}$ (P4 saturation), the forward rate goes to zero but the backward rate (chain on high-$\rho$ side stepping back to low-$\rho$ side) can also be suppressed by an effective potential barrier from the steep gradient.

Quantitatively: the V1-mediated transition rate across $\Sigma$ at gradient scale $|\nabla\rho|$ takes the form

$$\Gamma_{\mathrm{cross}}(\nabla\rho) \;\sim\; \Gamma_0(\rho_\mathrm{local})\cdot K_{V1}(\ell_P)\cdot \exp\bigl[-\alpha\,|\nabla\rho|\cdot\ell_P^2/\rho_\mathrm{local}\bigr],$$

with $\alpha$ a dimensionless V1-profile coefficient (INHERITED at value layer, set by the kernel shape). The exponential suppression is FORCED by the multi-scale expansion: substrate displacements crossing the gradient at scale $\ell_P$ accumulate exponential phase-decoherence in the V1-mediated chain-step propagation.

When $|\nabla\rho|\cdot\ell_P^2/\rho_\mathrm{local} \gg 1$ — the *steep-gradient regime* — the cross-participation bandwidth $\Gamma_\mathrm{cross}$ is exponentially suppressed.

### 3.3 DCGT multi-scale expansion yields surface of vanishing cross-participation bandwidth

Apply DCGT multi-scale expansion (Arc_D_2 §4 + Arc_D_4 §4) to the participation flux across $\Sigma$. The cell-averaged flux across the boundary,

$$\langle\mathbf{J}_\rho\cdot\hat n\rangle_{R_\mathrm{cg}} \;=\; \int_{\Sigma\cap\Omega} d^2A\;\rho_\mathrm{local}\cdot\Gamma_\mathrm{cross}(\nabla\rho),$$

becomes exponentially suppressed in the steep-gradient regime. There exists a critical gradient scale $|\nabla\rho|_c$ above which the flux is below the DCGT hydrodynamic-window threshold — meaning the substrate-to-continuum coarse-graining at scale $R_\mathrm{cg}$ cannot resolve any nonzero cross-participation bandwidth across $\Sigma$.

**Definition.** A *decoupling surface* $\Sigma_\mathrm{decouple}$ is a surface where $|\nabla\rho| \ge |\nabla\rho|_c$ and the cross-participation bandwidth is exponentially suppressed below DCGT resolution. Formally:

$$\Sigma_\mathrm{decouple} \;\equiv\; \bigl\{\,\mathbf{x} \;:\; |\nabla\rho(\mathbf{x})|\cdot\ell_P^2/\rho_\mathrm{local} \;\gtrsim\; \log(R_\mathrm{cg}/\ell_P)\,\bigr\}.$$

The logarithmic factor $\log(R_\mathrm{cg}/\ell_P)$ is set by the DCGT hydrodynamic-window scale separation: cross-participation bandwidth is below DCGT resolution when the exponential suppression exceeds the dynamic range of the multi-scale expansion.

This is the **substrate-derivation of horizon-as-decoupling-surface.**

### 3.4 Why this surface is observer-independent

ED-06's two-observer reconciliation states: infaller sees smooth local ED, external observer sees extreme mismatch — both arise from the same underlying ED gradient. The DCGT-grounded version of this reconciliation:

- **Infaller:** Local $\rho(\mathbf{x})$ near the chain is smooth and finite. The chain's local participation environment is well-defined; cell-averaging at scale $R_\mathrm{cg}$ produces the canonical DCGT continuum dynamics. The chain experiences nothing pathological at $\Sigma_\mathrm{decouple}$ because the surface is not a feature of the chain's local participation environment.
- **External observer:** Cross-participation flux from the chain (now on the high-$\rho$ side of $\Sigma$) to the external observer (on the low-$\rho$ side) is exponentially suppressed via the mechanism of §3.2. The external observer cannot integrate the chain's micro-events at the rate the chain produces them. The chain appears to freeze, fade, redshift.

**Both descriptions arise from the same ED gradient**, and the location of $\Sigma_\mathrm{decouple}$ is determined by the gradient — not by either observer's frame. The surface is **observer-independent at the ontological level** (the gradient is what it is) and **observer-dependent only at the level of participation** (which side of the gradient the observer is on determines what they experience).

This grounds ED-06 §7.1's two-observer reconciliation in the DCGT substrate-derivation chain.

---

## 4. Universalization Across Horizon Types

The substrate mechanism of Section 3 is *generic* — it depends only on the existence of a steep ED gradient, not on the source of that gradient. Different physical situations produce steep ED gradients via different mechanisms, but the resulting decoupling surface is structurally identical.

### 4.1 Black hole horizons (strong curvature)

A localized mass $M$ produces a steep ED-gradient via the cumulative-strain mechanism of T19 (substrate origin of Newton's $G$). At the radius where the gradient reaches the critical scale $|\nabla\rho|_c$ of §3.3, a decoupling surface forms. This radius corresponds approximately to the standard Schwarzschild radius $r_S = 2GM/c^2$ in the weak-field limit, with substrate-cutoff corrections of order $\ell_P^2 / r_S^2$ (negligible at astrophysical scales).

### 4.2 Rindler horizons (uniform acceleration)

A uniformly accelerating chain (Arc_SG_3 §3.4) breaks 3D participation isotropy along the acceleration direction; the acceleration-induced decoupling surface lies at distance $d_a = c^2/a$ behind the chain. The substrate mechanism is the same — the chain's acceleration produces a participation-density gradient that, at distance $d_a$, exceeds the critical scale and produces a decoupling surface. The $c^2/a$ scaling is FORCED by the substrate-level retardation argument of T18 + the participation-anisotropy of an accelerating chain.

### 4.3 Cosmological horizons (expanding background)

The cosmic horizon at $R_H = c/H_0$ is the participation-density boundary of the universe at cosmological scale (Arc_SG_3 §3 + T20). The Hubble-rate $H_0$ produces a substrate-level participation-density gradient at scale $R_H$. The decoupling surface mechanism is the same; the gradient source is cosmological expansion rather than mass or acceleration.

### 4.4 Acoustic / analog horizons (fluid / condensed-matter analogues)

In analog-gravity systems (transonic fluid flow, Bose-Einstein condensates with sonic horizons, optical analog systems), the participation-density analog is the local fluid density / refractive index / etc. The mechanism is identical: when the gradient of the analog-density variable exceeds a critical scale (e.g., when the fluid speed exceeds the local sound speed), a decoupling surface forms for the relevant participation-mediated signals (sound waves, light waves, etc.). This is why analog gravity reproduces horizon-like phenomena despite involving no actual GR curvature.

### 4.5 Structural identification

All four horizon types are **structurally identical under DCGT**: each is a surface where cross-participation bandwidth collapses below the DCGT hydrodynamic-window resolution. The identification is FORCED by the universalized mechanism of Section 3.

| Horizon type | Source of steep ED gradient |
|---|---|
| Black hole | Mass-induced participation-density gradient (T19) |
| Rindler | Acceleration-induced participation anisotropy (T18 + Arc_SG_3) |
| Cosmological | Hubble-rate cosmological expansion (T20) |
| Acoustic / analog | Fluid-density / index gradient in analog-gravity systems |

**Status of universalization:** FORCED at substrate level. The DCGT mechanism is universal; only the gradient-source is system-specific. This is one of the cleanest universalization results in the program — comparable to Arc_SG_3's $\ell_P$-invariance of $a_0$ as a horizon-anchored substrate quantity.

---

## 5. Continuum Limit: Acoustic-Metric Interpretation

How does the DCGT-derived decoupling surface relate to the standard GR notion of an event horizon?

### 5.1 Null surface in acoustic-metric scalar-tensor approximation

Under the acoustic-metric reading of Arc ED-10, the substrate participation density modulates an effective metric $g_{\mu\nu}^\mathrm{acoustic}$ that propagates substrate-level signals (ED-I-06 §3 directional-field-class propagation). At a decoupling surface $\Sigma_\mathrm{decouple}$, the cross-participation bandwidth is exponentially suppressed — meaning substrate-mediated signal propagation across $\Sigma$ is suppressed.

Translated to the acoustic-metric continuum description: the effective null cone tilts so that signal-cone-future-of-$\Sigma$ no longer intersects the external region. This is the standard GR statement of "null surface separating causally connected from causally disconnected regions" — but in the substrate framework, the null surface is the *continuum-emergent shadow* of the underlying participation-bandwidth-collapse, not a fundamental geometric object.

### 5.2 Causal boundary in the emergent continuum description

In the continuum acoustic-metric description, the decoupling surface appears as a *causal boundary*: signals from one side cannot propagate to the other side within the effective acoustic-metric light cone. This is what GR calls an "event horizon."

The key structural point: in standard GR, the event horizon is a *global* feature of the spacetime — its location depends on the full future history of the spacetime. In the substrate framework, the decoupling surface is *local* — it is a surface where the local ED gradient exceeds the critical scale. The global causal feature emerges only after coarse-graining; at substrate level, the surface is determined by the local gradient configuration.

### 5.3 The "geometric horizon" is a continuum artifact

Standard GR treats the event horizon as a fundamental geometric object — a feature of spacetime geometry. The substrate framework reveals this as a *continuum artifact* of the underlying participation-decoupling surface. The geometric horizon exists at the acoustic-metric continuum level; the substrate has only the bandwidth-collapse surface, which is a property of the participation network rather than spacetime.

Three structural consequences of this reframing:

- **Horizon teleology dissolved.** Standard GR's "global future" definition of event horizons creates a teleological-feeling structure (the horizon "knows" about its own future). In the substrate framework, the decoupling surface is local and immediate; teleological feeling is an artifact of continuum coarse-graining.
- **Horizon dynamics are participation-network reconfiguration.** When matter falls into a BH and the horizon grows, what's happening at substrate level is participation-network reconfiguration — the boundary of the bandwidth-collapse region expands as more substrate participation density becomes part of the high-$\rho$ region. The geometric "growth of horizon area" is the continuum description of this.
- **No global Cauchy data needed.** Standard GR's event horizon definition requires global Cauchy data (you need to know the future to know if a point is behind the horizon now). Substrate-level decoupling surfaces require only local gradient configuration; global Cauchy data is a coarse-graining artifact.

---

## 6. Structural Consequences

The DCGT-grounded horizon framework has four direct structural consequences for the rest of Arc BH:

### 6.1 No information crosses the decoupling surface as committed structure

Information (in the ED-10 §8 reading) is committed substrate participation structure. Committed structure requires substrate-level integration of micro-events across regions. At a decoupling surface, cross-participation bandwidth is exponentially suppressed below DCGT resolution — meaning committed substrate structure cannot be transmitted across the surface in the "outward" direction (high-$\rho$ to low-$\rho$).

This grounds ED-06 §7.2 + ED-10 §8.3's information-preservation claim: information is not destroyed at the horizon; it becomes causally inaccessible because the substrate decoupling surface blocks committed-structure transmission. The full elaboration of this is the subject of BH-4.

### 6.2 Entanglement (uncommitted structure) can straddle the surface

Entanglement is *uncommitted* substrate participation structure — shared participation channels that have not yet committed to definite outcomes. Uncommitted structure does not require the same substrate-level integration as committed structure; it can be shared across regions even when those regions cannot exchange committed signals.

Hence: at a decoupling surface, committed-information transmission is suppressed (§6.1) but uncommitted-entanglement structure can persist. This is the substrate-level explanation of why entanglement can straddle a horizon while signals cannot — articulated at conceptual level in ED-10 §8.4 and now grounded in DCGT.

### 6.3 Thermal behavior (Hawking / Unruh) is expected but not derived here

The substrate decoupling surface produces asymmetric participation: the high-$\rho$ side is a "participation sink" (commitment histories accumulate without being able to propagate outward). ED-06 §2.5 + ED-10 §8.5 argue this asymmetry produces thermal behavior — pair-creation-like phenomena at the boundary, with the standard Hawking spectrum as the expected result.

**This memo does not derive the Hawking spectrum.** The structural setup is in place (decoupling surface + asymmetric participation + commitment-irreversibility); the derivation chain to $T_H = \kappa/(2\pi)$ via V5 cross-chain correlations is the future-arc work flagged in Arc_BH_1 §3 (Hawking spectrum derivation explicitly NOT part of Arc BH).

### 6.4 Horizon area corresponds to participation capacity

ED-10 §5.6 states: "the boundary encodes the constraints on participation across it; the area law reflects the participation capacity of the boundary." Under the DCGT-grounded framework, this is now substrate-derivable: the horizon area $A$ counts the number of substrate-level participation channels at the boundary, and the participation-capacity scales as $A/\ell_P^2$ (holographic count, the same bound used in T19's substrate derivation of $G$).

This sets up BH-5 (Area-Law Entropy + 1/4 Factor Derivation) — the genuine new-derivation memo where the standard Bekenstein-Hawking $S = A/(4\ell_P^2)$ proportionality constant is derived (or its INHERITED-at-value-layer status is documented with explicit structural reason).

---

## 7. Deliverables

This memo's outputs:

- **A DCGT-grounded derivation of horizon formation.** The substrate-derivation chain (§3) shows horizon-as-decoupling-surface emerges from steep ED-gradients + V1 finite-width kernel + multi-scale expansion. The cross-participation bandwidth is exponentially suppressed in the steep-gradient regime; the surface where the suppression exceeds DCGT hydrodynamic-window resolution is the decoupling surface. Form FORCED at substrate level; specific gradient threshold $|\nabla\rho|_c$ INHERITED at value layer (set by V1 profile + DCGT scale separation).
- **A universalized horizon framework across BH / Rindler / cosmic / acoustic cases.** Section 4 shows all four horizon types are structurally identical under DCGT — each is a bandwidth-collapse surface differing only in the source of the steep gradient. Universalization FORCED at substrate level.
- **A substrate-to-continuum map showing how the decoupling surface becomes a geometric horizon.** Section 5 shows the geometric event horizon of GR is the continuum-emergent shadow of the substrate decoupling surface under acoustic-metric coarse-graining. Three structural consequences: horizon teleology dissolved; horizon dynamics are participation-network reconfiguration; no global Cauchy data needed at substrate level.
- **Structural consequences for information flow.** Information cannot cross the decoupling surface (committed structure blocked); entanglement can (uncommitted structure preserved); thermal behavior is expected at the surface (substrate asymmetric participation); horizon area corresponds to participation capacity (sets up BH-5).

**FORCED at substrate level:**
- Horizon-as-decoupling-surface mechanism (gradient steepening + bandwidth collapse + DCGT multi-scale expansion).
- Universalization across BH / Rindler / cosmic / acoustic horizons.
- Observer-independence at ontological level.
- Geometric horizon as continuum-emergent shadow of substrate decoupling surface.

**INHERITED at value layer:**
- Critical gradient scale $|\nabla\rho|_c$ (set by V1 profile + DCGT scale separation).
- Specific shape of V1 kernel beyond admissibility-class constraints.
- Numerical value of $\alpha$ (dimensionless V1-profile coefficient in §3.2 exponential suppression).

**Honest framing.** This memo's contribution is the *substrate-derivation chain* grounding the existing ED-I horizon content (already articulated in ED-06 + ED-10) in DCGT machinery. The conceptual content was already in place; the originality here is the explicit substrate-derivation pathway. Same structural pattern as Arc SG (consolidation under DCGT of closed substrate-gravity content): conceptual content existed; arc grounds it under DCGT methodology.

---

## 8. Recommended Next Step

After this memo, proceed to **Arc_BH_3 (Singularity-as-Manifold-Artifact + Strong-Curvature Audit)**. File: `theory/Black_Holes/Arc_BH_3_Singularity_And_Strong_Curvature_Audit.md`. Scope: consolidate ED-06 §2.4 + ED-10 §9.4 (singularities as representational failures of the manifold model, not physical entities); audit Arc ED-10's condition (C5) Lorentzian-non-degeneracy of the acoustic metric in the strong-curvature regime; identify the substrate-saturation mechanism that prevents geometric divergence; produce structural picture replacing the singular point. Includes genuine new derivation work for the strong-curvature audit. Estimated 2 sessions; second of three new-derivation memos in Arc BH (BH-3 + BH-5 + BH-6).

### Decisions for you

- **Confirm horizon-as-decoupling-surface DCGT-derivation.** Substrate-derivation chain through gradient-steepening + V1 finite-width kernel + multi-scale expansion produces decoupling surface FORCED at substrate level. Cross-participation bandwidth exponentially suppressed in steep-gradient regime; surface where suppression exceeds DCGT resolution is the decoupling surface.
- **Confirm universalization across horizon types.** BH / Rindler / cosmic / acoustic horizons are structurally identical under DCGT — same bandwidth-collapse mechanism, different gradient sources.
- **Confirm continuum-emergent geometric horizon framing.** Geometric event horizon is the continuum shadow of substrate decoupling surface under acoustic-metric coarse-graining; standard GR's global teleological event-horizon definition is dissolved at substrate level.
- **Confirm proceeding to Arc_BH_3 (singularity + strong-curvature audit) as the next deliverable.**

---

*Arc_BH_2 closes the horizon-as-decoupling-surface DCGT-grounding. Substrate-derivation chain: steep ED-gradients (gradient × $\ell_P^2$ / $\rho_\mathrm{local}$ exceeds critical scale) → V1 finite-width kernel produces exponential cross-surface bandwidth suppression $\Gamma_\mathrm{cross} \sim \exp[-\alpha|\nabla\rho|\ell_P^2/\rho_\mathrm{local}]$ → DCGT multi-scale expansion identifies surface where suppression exceeds hydrodynamic-window resolution as decoupling surface. Universalization across BH (mass-induced gradient via T19) / Rindler (acceleration anisotropy via T18) / cosmological (Hubble expansion via T20) / acoustic (analog-gravity systems) FORCED — same structural mechanism, different gradient sources. Observer-independence at ontological level FORCED (gradient is what it is); observer-dependent only at participation level (which side determines experience). Continuum-limit reading: geometric event horizon is the acoustic-metric-coarse-grained shadow of substrate decoupling surface; standard GR teleological global definition dissolves. Structural consequences set up BH-3 (strong-curvature audit), BH-4 (information / entanglement at horizon), BH-5 (area-law entropy + 1/4 factor — load-bearing new derivation). Hawking spectrum derivation NOT in scope. Arc_BH_3 (singularity-as-manifold-artifact + strong-curvature audit) is the next deliverable.*
