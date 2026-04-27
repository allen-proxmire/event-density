# Q.2 Substage — Examination Outline (Memo 00)

**Stage:** Arc Q · Q.2 (gauge group scoping)
**Date opened:** 2026-04-26
**Location:** `arcs/arc-Q/`
**Goal:** Discharge **R-4** (non-Abelian extension scoping) and **R-2 partial** (gauge-quotient individuation structure) for the GRH closure trajectory. Establish what GRH commits to about gauge-group content and what it explicitly defers to empirical inheritance.
**Predecessors:** [`grh_evaluation.md`](grh_evaluation.md) (Q.1 evaluation, GRH = CANDIDATE-strong) · [`00_grh_closure_roadmap.md`](00_grh_closure_roadmap.md) (multi-substage trajectory scoping)
**Status:** Scoping memo. Defines Q.2's question, sub-feature decomposition, structural inputs, forbidden inputs, falsifier inventory, expected deliverables, dependency graph, and honest scope limits. Sets the structural boundary that Q.3, Q.7, and Q.8 will inherit.
**Purpose:** Pin down the Q.2 terrain so subsequent Q.2 memos (Memo 01: non-Abelian admissibility; Memo 02: gauge-quotient individuation; Memo 03: verdict + cascade) can target specific load-bearing items without re-scoping.

---

## 1. The Q.2 Question

### 1.1 Precise statement

Q.2 asks: **What does GRH say about the choice of gauge group — and what does it explicitly not say?**

More formally: given the Q.1 verdict (GRH = CANDIDATE-strong, with all four clauses structurally admissible against the primitive stack and prior closures), what structural conditions does GRH place on the gauge-group content of the rule-type $\tau_g$, and how do those conditions interact with (a) the U(1) baseline already forced by Stage R.1's local-phase-invariance derivation, (b) potential non-Abelian extensions (SU(N) gauge groups, Lie-algebra-valued connections), and (c) Primitive 10's individuation threshold under the gauge equivalence $A_\mu \sim A_\mu + \partial_\mu \alpha$?

The answer must be **scope-precise**: it should specify both what GRH structurally forces and what GRH structurally *does not* force. Both ends of the answer matter for the closure trajectory.

### 1.2 Relation to GRH's four clauses

The Q.1 evaluation established four GRH clauses:

- **(GRH-1)** $\tau_g$ is Case P (bosonic, $\eta = +1$, integer spin)
- **(GRH-2)** $\tau_g$ carries the (1/2, 1/2) Lorentz representation
- **(GRH-3)** $\tau_g$ has an L3 interface enforcing local gauge invariance $A_\mu \to A_\mu + \partial_\mu \alpha$
- **(GRH-4)** $\sigma_{\tau_g} = 0$ via the MR-P mechanism

Q.2 specifically interrogates the *gauge-group content* of (GRH-3). The clause as stated is gauge-group-agnostic — it says only that the L3 interface enforces *some* local gauge invariance, not which gauge group's invariance. Q.2 asks: is the (GRH-3) clause structurally admissible across **all** gauge groups, only U(1), or some delineated subset (e.g., compact Lie groups)?

(GRH-1), (GRH-2), and (GRH-4) are downstream of (GRH-3) in the GRH hierarchy and inherit whatever scope (GRH-3) closes with. Q.2 therefore primarily targets (GRH-3); the other three clauses will be re-confirmed for non-Abelian extensions but are not the load-bearing question.

### 1.3 Relation to the broader closure trajectory

Q.2 is the natural opener of the four-substage GRH closure. Its outputs flow downstream:

- **Q.3** (interaction vertex classification) inherits Q.2's gauge-group-content commitments to specify vertex structure (charged-rule-type / gauge-rule-type interactions). Without Q.2's gauge-quotient-individuation closure, vertex counting cannot respect gauge equivalence.
- **Q.7** (second quantisation) inherits Q.2's admissible-gauge-group classification to scope which non-Abelian rule-type structures the lightlike-worldline reformulation must accommodate.
- **Q.8** (vacuum and zero-point) inherits Q.2's gauge-quotient-individuation structure to define the vacuum state of $\tau_g$ as a gauge-equivalence-class object.

Q.2 is therefore both a **substantive closure stage** (discharging R-4 and R-2 partial) and a **structural-boundary-setting stage** (defining what Q.3 / Q.7 / Q.8 must inherit). The latter role is why the Memo 00 scoping is heavier than a single-arc Memo 00.

---

## 2. Decomposition into Sub-Features

Q.2 packages **five** structurally distinct sub-features. Each must be settled independently for Q.2 closure.

### 2.1 (F1) U(1) Baseline Confirmation

- **Definition.** Re-confirm that GRH closes affirmatively for the U(1) gauge group as the minimum gauge-content commitment. U(1) was already forced at Stage R.1 from local-phase invariance; F1 verifies that the GRH framework (rule-type $\tau_g$ with all four GRH clauses) is structurally consistent with the U(1) baseline already in place.
- **Structural commitment.** GRH at minimum commits to U(1) gauge content — i.e., at least one massless Case-P rule-type with U(1)-valued L3 interface enforcing $A_\mu \to A_\mu + \partial_\mu \alpha$ for $\alpha: \mathcal{M} \to \mathbb{R}$.
- **Falsifier.** F1 fails if the GRH framework is structurally inconsistent with R.1's already-forced U(1) content (e.g., if (GRH-1) Case-P statistics conflicts with R.1's vector-field content for U(1)).
- **Out of scope.** F1 does not address whether U(1) is the unique gauge group (that's F2) or how individuation respects gauge equivalence (that's F3).

### 2.2 (F2) Non-Abelian Extension Admissibility

- **Definition.** Determine whether the GRH framework structurally admits non-Abelian gauge groups (SU(N) and other compact Lie groups) — i.e., can $\tau_g$ be extended to carry a Lie-algebra-valued connection $A^a_\mu$ with internal index $a$ running over the Lie algebra dimension, with self-coupling $[A_\mu, A_\nu]$ in the field strength, without primitive-level obstruction?
- **Structural commitment.** Either: (a) GRH structurally admits non-Abelian extensions in principle (specific group choice deferred to empirical inheritance); or (b) GRH structurally restricts to U(1) / Abelian gauge groups (with non-Abelian content requiring additional structural commitments beyond the four GRH clauses); or (c) GRH structurally requires non-Abelian extensions for closure (which would force a richer structure than the Q.1 framing assumed).
- **Falsifier.** F2 fails if non-Abelian extension is *primitive-level blocked* — for instance, if Primitive 07's L2 internal-index structure cannot accommodate Lie-algebra multiplicity, or if the (1/2, 1/2) Lorentz-rep content of (GRH-2) is incompatible with internal-index extension.
- **Out of scope.** F2 does *not* identify the specific Standard Model gauge group $SU(3) \times SU(2) \times U(1)$ — that remains empirical inheritance per Q.0 framing. F2 only addresses *structural admissibility*.
- **This sub-feature directly discharges R-4.**

### 2.3 (F3) Gauge-Quotient Individuation Structure

- **Definition.** Determine how Primitive 10's individuation threshold respects the gauge equivalence $A_\mu \sim A_\mu + \partial_\mu \alpha$ — i.e., are two gauge-equivalent $A_\mu$ configurations automatically counted as one under individuation, or does the framework require an explicit gauge-quotient construction at the individuation level?
- **Structural commitment.** Either: (a) Primitive 10 individuation automatically respects gauge equivalence (no additional structure required); or (b) the framework requires an explicit gauge-quotient $[A_\mu]$ as the individuation-relevant object (with $A_\mu$ itself being a *representative* of the equivalence class). Either outcome closes R-2 partially; the difference is how much structural machinery propagates downstream.
- **Falsifier.** F3 fails if gauge equivalence is *primitive-level incompatible* with Primitive 10 — for instance, if Primitive 10 distinguishes two configurations that gauge invariance must identify, or if the gauge-quotient cannot be defined consistently across the participation-graph kinematic structure.
- **Out of scope.** F3 addresses individuation at the gauge-group-scoping level; the *vertex-level* gauge-quotient (how vertices respect gauge equivalence) is Q.3 content (R-2 completion).
- **This sub-feature directly discharges R-2 partial.**

### 2.4 (F4) Specific-Gauge-Group Deferral (Honest Scoping)

- **Definition.** Establish that GRH structurally does *not* force the specific Standard Model gauge group $SU(3) \times SU(2) \times U(1)$, hypercharge assignments, weak mixing angle, or any other SM-specific gauge content. F4 closes by an honest-scoping statement, not by derivation.
- **Structural commitment.** GRH is gauge-group-agnostic in the sense that admissibility (F2) does not extend to forcing. The choice of gauge group is empirical inheritance via the Dimensional Atlas, parallel to Arc M's "form FORCED, value INHERITED" methodology.
- **Falsifier.** F4 "fails" only in the sense that — counter to the Q.1 expectation — Q.2's substantive work might *force* the SM gauge group from primitives alone (which would be a remarkable result, not a structural failure). The current framing anticipates F4 closing by REFUTED on the "GRH forces SM gauge group" question.
- **Out of scope.** F4 does *not* derive the SM gauge group; it explicitly disclaims any such derivation.

### 2.5 (F5) Downstream Dependency Map

- **Definition.** Specify what Q.3, Q.7, and Q.8 must inherit from Q.2's closure — i.e., produce the precise structural-content handoffs that downstream substages will use as background.
- **Structural commitment.** Q.2 issues a closure-state inventory: which gauge-group content is settled (admissibility, individuation), which is deferred (specific group choice), and what each downstream substage will use.
- **Falsifier.** F5 fails if Q.2's closure cannot be cleanly handed off — for example, if the gauge-quotient individuation structure requires Q.3 vertex content for its own definition (creating a Q.2 ⟷ Q.3 circular dependency).
- **Out of scope.** F5 does not execute the downstream substages; it only specifies what they inherit.

### 2.6 Status Classification

| Sub-feature | Status | Reasoning |
|---|---|---|
| **F1** U(1) baseline | **forced-via-confirmation** | R.1 already forces U(1); F1 verifies GRH framework consistency, expected to close cleanly |
| **F2** Non-Abelian admissibility | **load-bearing** | The substantive R-4 question; closure determines whether GRH extends beyond U(1) at the structural level |
| **F3** Gauge-quotient individuation | **load-bearing** | The substantive R-2-partial question; closure determines downstream individuation machinery |
| **F4** Specific-group deferral | **honest-scoping closure** | Anticipated to close by REFUTED; serves to bound GRH's claims |
| **F5** Downstream dependency map | **forced-via-derivation** | Bookkeeping; assembled from F1-F4 outputs |

Two genuinely substantive items (F2, F3); two confirmation/scoping items (F1, F4); one bookkeeping item (F5).

---

## 3. Refinement Mapping

The two refinements assigned to Q.2 map cleanly onto the sub-features:

| Refinement | Maps to | Closure expected at |
|---|---|---|
| **R-4** Non-Abelian extension scoping | **F2** | Q.2 Memo 01 (anticipated) |
| **R-2 partial** Gauge-quotient individuation | **F3** | Q.2 Memo 02 (anticipated) |

R-4 closes if F2 either affirmatively admits non-Abelian extension (with specific group deferred to inheritance) or affirmatively restricts to U(1). Both outcomes discharge R-4; the difference is whether the FORCED-GRH content extends to non-Abelian gauge groups or restricts to U(1).

R-2 closes *partially* at Q.2 (the gauge-group-scoping individuation structure); R-2 *completion* (the vertex-level gauge-quotient) is Q.3 content per the closure roadmap.

**Load-bearing items: F2 and F3.** F1, F4, F5 are bookkeeping or honest-scoping work.

---

## 4. Structural Inputs

### 4.1 Primitives drawn upon

- **Primitive 02** (worldline + ambient 3+1D manifold). Supplies the spacetime structure on which $A_\mu$ lives.
- **Primitive 04** (bandwidth fields). Supplies the four-band content $b^{\mathrm{int}}$, $b^{\mathrm{adj}}$, $b^{\mathrm{env}}$, $b^{\mathrm{com}}$ for $\tau_g$.
- **Primitive 06** (four-gradient + Lorentz covariance). Supplies the $\partial_\mu$ that appears in the gauge transformation $A_\mu \to A_\mu + \partial_\mu \alpha$ and the Lorentz-rep ladder including (1/2, 1/2).
- **Primitive 07** (rule-type taxonomy, Levers L1–L4). Supplies the structural slots for $\tau_g$ — bandwidth partition (L1), internal index (L2), interface (L3), statistics class (L4). **L3 is the load-bearing lever for Q.2.**
- **Primitive 10** (individuation threshold). Supplies the counting structure that must respect gauge equivalence (F3).
- **Primitive 11** (commitment dynamics). Background; commitment-content for $\tau_g$ is Q.3 content, not Q.2.

For each primitive Q.2 commits to using its admissibility content (e.g., "Primitive 06 admits the (1/2, 1/2) representation") **but not** any further specification (e.g., "Primitive 06 forces the SM electroweak structure"). The line between admissibility and forcing is the discipline that preserves honest scoping.

### 4.2 Inherited FORCED upstream items

- **Theorem 1** (spin-statistics, R.2.5): $\eta = (-1)^{2s}$. Confirms (GRH-1) Case P is consistent with $s = 1$ from (GRH-2) (1/2, 1/2).
- **Theorem 2** (Cl(3,1) uniqueness, R.2.4): supplies the Lorentz-rep ladder including (1/2, 1/2). Confirms (GRH-2).
- **Theorem 3** (anyon prohibition, R.2.3): excludes exotic statistics; consistent with (GRH-1).
- **Theorem 4** (Dirac emergence with $g=2$, R.3): not directly used; background.
- **Theorem 6** (canonical (anti-)commutation, Q.7): may be invoked in F2 for non-Abelian commutation structure, with the discipline that Q.2 uses Theorem 6 as background, not as derivation premise (Q.7 closure is downstream).
- **Theorem 7** (UV-FIN, Q.8): background; Q.2 does not use UV-FIN as a derivation step.
- **Theorem 8** (V₁ finite-width vacuum kernel, Arc N): background; vacuum-state work is Q.8.
- **Theorems 10–16** (Phase-1 closure: Born, U2-D, U2-C, U5, U1, U4, U3): background; Q.2 operates on the Hilbert-space framework these establish without invoking specific Phase-1 results as derivation steps.
- **M.2** (chain-mass synthesis): explicitly expected to feedback from GRH closure (F-M8 cascade); Q.2 may not invoke M.2 as a derivation premise.

### 4.3 GRH-1 through GRH-4 (Q.1 conditional content)

Q.2 takes the four GRH clauses as its starting point:

- (GRH-1) Case P statistics — Q.2 verifies for non-Abelian extensions (F2 sub-content)
- (GRH-2) (1/2, 1/2) Lorentz rep — Q.2 verifies for non-Abelian extensions (F2 sub-content)
- (GRH-3) L3 enforces gauge invariance — **Q.2's primary target** (F2 + F3)
- (GRH-4) $\sigma_{\tau_g} = 0$ via MR-P — Q.2 verifies for non-Abelian extensions (F2 sub-content)

The Q.1 verdict treated (GRH-1), (GRH-2), (GRH-4) as CANDIDATE-FORCED conditional on (GRH-3). Q.2's gauge-group-scoping work tests this conditionality: if non-Abelian extensions force structural changes to (GRH-1), (GRH-2), or (GRH-4), the conditionality structure shifts.

### 4.4 R.1 minimal coupling content (background, not premise)

Stage R.1's `kg_minimal_coupling_and_current.md` derived $D_\mu = \partial_\mu + (iq/\hbar) A_\mu$ from local-phase invariance, forcing the existence of $A_\mu$ as a structural object for the U(1) case. Q.2 uses R.1's *content* as background (the U(1) $A_\mu$ exists) but does not use R.1's *derivation chain* as a premise for new GRH content (that would re-derive what GRH is meant to identify).

The discipline: **R.1 establishes that $A_\mu$ exists; GRH establishes what $A_\mu$ is.** Q.2 may use the existence but not re-derive the identification.

### 4.5 Mathematical infrastructure

- **Compact Lie group theory** (standard; Hall, Lie Groups, Lie Algebras, and Representations).
- **Lie-algebra-valued differential forms** (standard; Nakahara, Geometry, Topology, and Physics).
- **Principal bundle / connection theory** (standard; Kobayashi-Nomizu).
- **Standard QFT gauge structure** as background only — Q.2 may verify consistency with standard gauge-theory results but may not invoke them as derivation steps.

### 4.6 Scope conditions

- **Non-relativistic single-particle scope** (inherited from Phase-1; relevant for downstream consistency checks but not directly for Q.2's gauge-group work).
- **Relativistic single-particle scope** (inherited from Arc R; relevant for $\tau_g$ as a relativistic rule-type).
- **3+1D Minkowski background** (inherited; gauge group scoping is dimension-specific).

---

## 5. Forbidden Inputs (Acyclicity Discipline)

Per the GRH closure roadmap §7 + the U3 closure pattern, the following inputs are explicitly forbidden as Q.2 derivation premises:

### 5.1 Substage-cross-contamination forbidden inputs

- **R-1 (lightlike worldline reformulation)** — Q.7 content. *Justification:* Q.7's affine-parameter machinery is downstream; assuming it here would create a Q.2 → Q.7 → Q.2 dependency loop.
- **R-3 (vertex-anchored commitment)** — Q.3 content. *Justification:* Q.3's vertex classification depends on Q.2's gauge-group scoping; assuming Q.3's results would invert the dependency.
- **R-5 (vacuum vs particle status of $\tau_g$)** — Q.7 / Q.8 content. *Justification:* The vacuum state of $\tau_g$ is Q.8's load-bearing question; Q.2 may scope gauge-quotient individuation without resolving vacuum status.

### 5.2 Standard Model specifics forbidden inputs

- **U(1) hypercharge assignments** — empirical SM content. *Justification:* Q.2 establishes U(1) admissibility; the *specific* U(1) embedding in $SU(3) \times SU(2) \times U(1)$ is empirical.
- **SU(2) weak isospin identification** — empirical SM content. *Justification:* Q.2 may scope SU(2) as a non-Abelian admissibility example but may not assume the SM-specific SU(2)_L identification.
- **SU(3) color identification** — empirical SM content. *Justification:* Same as SU(2); SU(3) is a non-Abelian admissibility example, not a forced choice.
- **Weak mixing angle, Cabibbo angle, CKM matrix** — empirical SM parameters. *Justification:* Pure empirical inheritance; out of scope.
- **Electroweak symmetry breaking pattern** — Q.4 content. *Justification:* SSB is downstream and SPECULATIVE per Q.0 framing.

### 5.3 Higgs sector forbidden inputs

- **Higgs field, Higgs vacuum expectation value, Higgs mass** — Q.4 content. *Justification:* Higgs mass-generation is independent of GRH per Q.1 §5.4; out of Q.2 scope.
- **Spontaneous symmetry breaking machinery** — Q.4 content.

### 5.4 Generation structure forbidden inputs

- **Number of fermion generations** — Q.6 / empirical. *Justification:* Per Q.1 §5.5, GRH says nothing about generation multiplicity.
- **Flavor structure** — Q.6 / empirical.

### 5.5 Empirical coupling constants forbidden inputs

- **$q$ (electromagnetic charge)**, **$g_s$ (strong coupling)**, **$g_w$ (weak coupling)** — empirical inheritance via Dimensional Atlas. *Justification:* Numerical values are not GRH content; Q.2 establishes structural admissibility, values are inherited.
- **Charge quantization** ($e/3$ for quarks, $e$ for leptons) — possibly Q.2 partial, possibly empirical. *Discipline:* Q.2 may scope whether structural arguments (Dirac monopole, topological) admit charge quantization, but may not force the specific quantization pattern.

### 5.6 Cascade-target forbidden inputs

- **F-M8 (massless slot existence, FORCED-conditional)** — the cascade target, not a premise. *Justification:* Using F-M8 as a Q.2 input would be circular (GRH closure promotes F-M8 to unconditional; F-M8 cannot then be a derivation step in GRH closure).

### 5.7 Standard QFT machinery forbidden inputs

- **Yang–Mills Lagrangian as a postulate** — derivation target, not premise. *Justification:* If GRH closes affirmatively, Yang–Mills emerges; using it as input inverts the derivation.
- **Faddeev-Popov ghosts, BRST quantization** — Q.7 content. *Justification:* Ghost machinery is part of the second-quantisation framework Q.7 addresses.
- **Renormalization group as procedure** — Q.7/Q.8 content. *Justification:* Out of Q.2 scope.

---

## 6. Falsifier Inventory

Q.2 closes affirmatively if all five sub-features (F1–F5) close uniquely under the available structural inputs. The following falsifiers state how each sub-feature could fail.

### 6.1 Per-sub-feature falsifiers

- **(Fal-1) U(1) baseline incompatibility.** GRH framework structurally inconsistent with R.1's already-forced U(1) content — for instance, (GRH-1) Case P statistics conflicts with R.1's vector-field structure. *Targets F1.* *Source:* primitive-level (R.1 + Theorem 1). *Anticipated dispatch:* §3.7 of `grh_evaluation.md` already confirms compatibility; F1 verification is bookkeeping.

- **(Fal-2) Non-Abelian extension primitive-level blocked.** Primitive 07's L2 internal-index structure cannot accommodate Lie-algebra multiplicity, OR the (1/2, 1/2) Lorentz rep is structurally incompatible with internal-index extension, OR Primitive 04's bandwidth structure cannot carry Lie-algebra-valued connections. *Targets F2.* *Source:* primitive-level (Primitives 04, 06, 07). *Anticipated dispatch:* primitive-by-primitive admissibility check parallel to `grh_evaluation.md` §3.

- **(Fal-3) Primitive 10 individuation incompatible with gauge equivalence.** Primitive 10's individuation threshold structurally distinguishes two $A_\mu$ configurations that gauge invariance must identify, OR the gauge-quotient cannot be defined consistently across the participation-graph kinematic structure. *Targets F3.* *Source:* primitive-level (Primitive 10). *Anticipated dispatch:* explicit gauge-quotient construction; verify Primitive 10 respects equivalence classes.

- **(Fal-4) GRH forces SM gauge group from primitives alone.** Q.2's substantive work somehow derives $SU(3) \times SU(2) \times U(1)$ from primitives without empirical input. *Targets F4.* *Source:* would represent overstatement of GRH's claims. *Anticipated dispatch:* none needed; F4 closes by REFUTED on this question (i.e., GRH does *not* force the SM gauge group, which is the honest-scoping claim).

- **(Fal-5) Q.2 ⟷ Q.3 circular dependency.** Q.2's gauge-quotient individuation structure requires Q.3 vertex content for its own definition, creating a circular dependency. *Targets F5.* *Source:* methodological. *Anticipated dispatch:* explicit dependency-map audit; verify Q.2 closes without Q.3 inputs.

### 6.2 Cross-cutting falsifiers

- **(Fal-6) Non-Abelian extension forces structural changes to GRH-1, GRH-2, or GRH-4.** If non-Abelian extension requires (GRH-1) to admit non-bosonic statistics, OR (GRH-2) to admit higher Lorentz reps, OR (GRH-4) to admit massive gauge content (without SSB), the Q.1 conditionality structure shifts. *Targets F2 cross-contamination.* *Anticipated dispatch:* verify that non-Abelian extension preserves GRH-1, GRH-2, GRH-4 as stated, with the L3 interface (GRH-3) carrying all the non-Abelian-specific structure.

- **(Fal-7) Gauge-quotient individuation requires vacuum-state machinery.** Defining the gauge equivalence class $[A_\mu]$ requires Q.8 vacuum content — would create a Q.2 → Q.8 circular dependency. *Targets F3.* *Anticipated dispatch:* verify the gauge-quotient can be defined kinematically (at fixed time, on the participation graph) without vacuum-state input.

### 6.3 Falsifier-source taxonomy

| Falsifier | Targets | Source layer | Anticipated dispatch |
|---|---|---|---|
| Fal-1 (U(1) baseline) | F1 | Primitive (R.1 + T1) | Q.2 Memo 01 — bookkeeping |
| Fal-2 (non-Abelian blocked) | F2 | Primitive (P-04, P-06, P-07) | Q.2 Memo 01 — substantive |
| Fal-3 (P-10 incompat.) | F3 | Primitive (P-10) | Q.2 Memo 02 — substantive |
| Fal-4 (forces SM group) | F4 | Methodological | Q.2 Memo 03 — honest-scoping |
| Fal-5 (Q.2 ⟷ Q.3 circular) | F5 | Methodological | Q.2 Memo 03 — dependency audit |
| Fal-6 (non-Abelian breaks GRH-1/2/4) | F2 cross-cut | Primitive | Q.2 Memo 01 — verification |
| Fal-7 (gauge-quotient needs vacuum) | F3 cross-cut | Methodological | Q.2 Memo 02 — verification |

Two genuinely substantive falsifiers (Fal-2, Fal-3); two methodological (Fal-4, Fal-5); two verifications (Fal-6, Fal-7); one bookkeeping (Fal-1). Pattern matches the U3 arc's load distribution.

---

## 7. Expected Deliverables

Q.2 closure must produce:

### 7.1 Structural classification of admissible gauge-group forms

A clean statement of which gauge-group structures GRH structurally admits — anticipated forms:

- **U(1)** (Abelian): admitted at minimum (already R.1-forced; F1 verification)
- **Compact Abelian groups** ($U(1)^n$): admitted as direct products of U(1)
- **Compact non-Abelian groups** (SU(N), SO(N), etc.): admitted iff F2 closes affirmatively (anticipated yes, with R-4 discharged)
- **Non-compact groups, infinite-dimensional groups, etc.**: anticipated structurally inadmissible (gauge structure on participation graph requires compactness)

### 7.2 Statement of what GRH commits to about gauge groups

A precise statement of the GRH gauge-group content. Anticipated form: "GRH commits to the existence of at least one massless Case-P rule-type with gauge-invariant L3 interface enforcing local gauge transformations under a compact Lie group; specific group choice (Abelian or non-Abelian, dimension, embedding) is empirical inheritance."

### 7.3 Statement of what GRH does NOT commit to

A precise statement of the deferral. Anticipated form: "GRH does not force the Standard Model gauge group $SU(3) \times SU(2) \times U(1)$, the hypercharge assignments, the weak mixing angle, the strong / weak coupling constants, the Higgs sector, the generation structure, the flavor matrices, or the charge quantization pattern. These are empirical inheritance."

### 7.4 Closure plan for R-4 and R-2 (partial)

- **R-4 closure statement:** non-Abelian extension is structurally admissible (specific group inherited); load-bearing items: F2 affirmative closure.
- **R-2 partial closure statement:** Primitive 10 individuation respects gauge equivalence either automatically or via an explicit gauge-quotient construction (F3 outcome); R-2 completion deferred to Q.3.

### 7.5 Dependency map for Q.3, Q.7, Q.8

A precise inventory of what each downstream substage inherits from Q.2:

| Downstream | Inherits from Q.2 | Used for |
|---|---|---|
| **Q.3** | Gauge-group admissibility; gauge-quotient structure (partial) | Vertex classification respecting gauge equivalence |
| **Q.7** | Admissible gauge-group classification | Lightlike-worldline reformulation must accommodate Lie-algebra-valued $A_\mu^a$ |
| **Q.8** | Gauge-quotient individuation structure | Vacuum state defined as gauge-equivalence-class object |

### 7.6 Verdict

Anticipated: **R-4 and R-2 partial both close affirmatively; Q.2 substage CLOSED; GRH closure trajectory advances to Q.3.**

If F2 fails (non-Abelian extension blocked): GRH content restricts to U(1); Q.3 / Q.7 / Q.8 proceed under U(1)-only scope; eventual FORCED-GRH covers U(1) only.

If F3 fails (gauge-quotient incompatible): GRH closure stalls; would require either revising Primitive 10 (re-opening foundational primitive) or revising GRH-3 (relaxing gauge invariance to a weaker constraint).

---

## 8. Dependency Graph

### 8.1 Substage dependencies

```
                  Q.0 (scoping)        ← background
                       ↓
                  Q.1 (GRH evaluation) ← background; CANDIDATE-strong verdict
                       ↓
            ┌─────  Q.2 (THIS substage)  ─────┐
            │  F1 (U(1) baseline)             │
            │  F2 (non-Abelian admissibility) │  ← discharges R-4
            │  F3 (gauge-quotient individ.)   │  ← discharges R-2 partial
            │  F4 (specific-group deferral)   │
            │  F5 (downstream dep map)        │
            └────────────┬────────────────────┘
                         ↓
              Q.3 (vertex classification)     ← discharges R-3, R-2 completion
                         ↓
              Q.7 (second quantisation)       ← discharges R-1, R-5 partial
                         ↓
              Q.8 (vacuum and zero-point)     ← discharges R-5 completion
                         ↓
              Arc Q synthesis                 ← promotes GRH to FORCED-uncond.
                         ↓
              Cascade to Arc M                ← F-M8 promoted to FORCED-uncond.
                         ↓
              Theorem 17 added to inventory
```

### 8.2 Refinement-to-substage closure map

| Refinement | Starts at | Closed at |
|---|---|---|
| R-1 (lightlike worldline) | Q.7 | Q.7 |
| R-2 partial (gauge-quotient individ.) | **Q.2** (F3) | **Q.2** |
| R-2 completion (vertex gauge-quotient) | Q.3 | Q.3 |
| R-3 (vertex-anchored commitment) | Q.3 | Q.3 |
| R-4 (non-Abelian extension scoping) | **Q.2** (F2) | **Q.2** |
| R-5 partial (vacuum-field aspect) | Q.7 | Q.7 |
| R-5 completion (zero-point aspect) | Q.8 | Q.8 |

### 8.3 Structural commitment flow

What flows from Q.2 downstream:

- **To Q.3:** admissible-gauge-group classification (set of structurally permitted gauge groups); gauge-quotient individuation structure (at the gauge-group-scoping level).
- **To Q.7:** internal-index space scope (how many gauge-rule-type internal indices Q.7's second-quantisation framework must support).
- **To Q.8:** gauge-equivalence-class structure for vacuum-state definition.

What does NOT flow from Q.2 downstream (deferred or inherited):

- Specific gauge group choice (deferred to empirical inheritance).
- Coupling constant values (empirical inheritance).
- Higgs sector (Q.4, SPECULATIVE).
- Generation structure (Q.6 / empirical).
- Charge quantization pattern (possibly Q.2 partial; possibly empirical).

---

## 9. Honest Scope Limits

Q.2 explicitly cannot resolve the following — these are empirical inheritance or downstream-substage content:

- **Specific gauge group choice.** Whether the universe's gauge group is $SU(3) \times SU(2) \times U(1)$, $SU(5)$ (GUT), $SO(10)$ (GUT), $E_6$ (GUT), or something else entirely. Q.2 establishes admissibility; experiment establishes choice.

- **Coupling constants.** Numerical values of $q$, $g_s$, $g_w$, the weak mixing angle $\theta_W$, etc. Empirical inheritance via the Dimensional Atlas.

- **Higgs sector.** Higgs field existence, vacuum expectation value, Higgs mass, spontaneous-symmetry-breaking pattern. Q.4 content; SPECULATIVE per Q.0 framing; independent of GRH.

- **Generation structure.** Number of fermion generations (3 in our universe), flavor structure, CKM/PMNS matrices. Q.6 / empirical inheritance.

- **Charge quantization.** Why charges come in integer multiples of $e/3$ (quarks) or $e$ (leptons). Possibly Q.2 partial (Dirac-monopole-style topological argument), possibly empirical. Q.2 may scope but cannot be expected to force.

- **Empirical Standard Model inheritance generally.** Anything that is not structural admissibility (F2) or gauge-quotient individuation structure (F3) is downstream or empirical.

These scope limits are not failures — they are honest structural boundaries. The GRH closure trajectory (per the roadmap) explicitly treats SM specifics as empirical inheritance, parallel to Arc M's "form FORCED, value INHERITED" methodology.

---

## 10. Recommended Next Memo

The natural next deliverable after this Memo 00 is:

**Q.2 Memo 01 — Non-Abelian Extension Admissibility (R-4 closure)**

Memo 01 should:

- Derive F1 (U(1) baseline confirmation) — bookkeeping verification that R.1's already-forced U(1) content is consistent with the GRH framework
- Derive F2 (non-Abelian admissibility) — substantive primitive-by-primitive check that Lie-algebra-valued $A^a_\mu$ is structurally admissible:
  - Primitive 04 admits Lie-algebra-valued bandwidth content
  - Primitive 06 admits the (1/2, 1/2) Lorentz rep with internal index $a$
  - Primitive 07 L2 admits Lie-algebra-multiplicity internal indices
  - Primitive 07 L3 admits non-Abelian gauge-invariance structure (with $[A_\mu, A_\nu]$ self-coupling in $F^a_{\mu\nu}$)
- Dispatch Falsifiers Fal-1, Fal-2, Fal-6
- State R-4 closure verdict (anticipated: affirmative, with structural admissibility for compact Lie groups; specific group deferred to inheritance)

Anticipated length: comparable to U3 Memo 02 (substantive primitive-by-primitive derivation work).

After Memo 01, Memo 02 would address F3 (gauge-quotient individuation, R-2 partial closure), and Memo 03 would address F4 (honest scoping) + F5 (downstream dependency map) + verdict.

---

## 11. One-Line Summary

> Q.2 scopes what GRH commits to about gauge-group content (and what it explicitly defers to empirical inheritance) by decomposing into five sub-features — U(1) baseline confirmation (F1), non-Abelian extension admissibility (F2, load-bearing, discharges R-4), gauge-quotient individuation structure (F3, load-bearing, discharges R-2 partial), specific-gauge-group deferral (F4, honest-scoping), downstream dependency map (F5, bookkeeping) — operating on Primitives 02/04/06/07/10/11 plus inherited FORCED items (Theorems 1–16) plus the Q.1 GRH conditional content, with strict forbidden-input discipline (R-1, R-3, R-5, all SM specifics, Higgs, generations, coupling constants, F-M8 cascade target, standard QFT machinery as derivation premise) preserving acyclicity, anticipated to close affirmatively with non-Abelian admissibility forced (specific group inherited) and gauge-quotient individuation respecting Primitive 10 either automatically or via explicit gauge-quotient construction, advancing the GRH closure trajectory to Q.3 (vertex classification) and ultimately to Arc Q synthesis (GRH promoted to FORCED-unconditional, F-M8 cascade-promoted, Theorem 17 added to the structural-foundations inventory).

---

## Recommended Next Steps

**(a) Begin Q.2 Memo 01 (non-Abelian extension admissibility, R-4 closure).** The natural next deliverable. Following the section outline in §10, Memo 01 should derive F1 (bookkeeping) and F2 (substantive primitive-by-primitive check), dispatch Fal-1 / Fal-2 / Fal-6, and state R-4's closure verdict. Anticipated length: comparable to U3 Memo 02. Format: same template as `arcs/U3/02_F1_F2_F3_F4_derivations.md`.

**(b) Pre-Memo-01 audit of Primitive 07's L2 (internal-index lever).** A short audit (15–30 minutes) of Primitive 07's L2 specification to confirm what kinds of internal-index structures are admissible. Specifically: does L2 admit Lie-algebra-multiplicity indices natively, or does it specify a more restrictive structure that would need to be re-scoped for non-Abelian extensions? The Q.1 evaluation memo §3.4 says "L2: (1/2, 1/2) is a valid Lorentz representation. Compatible." but doesn't address Lie-algebra extension. A pre-Memo-01 check would either confirm clean L2 admissibility or flag a refinement.

**(c) Confirm or revise the Q.2 sub-feature decomposition with the GRH closure roadmap.** A 10-minute audit of `00_grh_closure_roadmap.md` §4 (Q.2 scope sketch) against this Memo 00's five-sub-feature decomposition. Verify that F1–F5 fully cover the roadmap's anticipated Q.2 deliverables and that no Q.2-relevant content has been deferred to Q.3 / Q.7 / Q.8 inadvertently.

**(d) Defer memory-record update until Q.2 closure (Memo 03).** Per the discipline established in U3 / U4 / U5 arcs. The bundled memory update should capture the post-Q.2 state: F1–F5 verdicts, R-4 closure, R-2 partial closure, downstream dependency map, any new CANDIDATEs introduced (anticipated: zero), and explicit handoffs to Q.3.

**(e) (Optional) Write the Q.2 falsifier-status table once Memos 01 + 02 close.** A compact table tracking Fal-1 through Fal-7 dispatch status across Memos 01, 02, 03 — useful for the Memo 03 verdict statement and the eventual Arc Q synthesis. Pattern matches the U3 arc's Memo-by-memo falsifier table from `arcs/U3/02_F1_F2_F3_F4_derivations.md` §8.
