# GRH Closure Roadmap

**Stage:** Arc Q · post-Q.1 (multi-substage closure planning)
**Date opened:** 2026-04-26
**Location:** `arcs/arc-Q/`
**Status:** Roadmap memo. Scopes the four-substage trajectory required to promote GRH from CANDIDATE-strong (Q.1 verdict) to FORCED-unconditional. Sequences Q.2, Q.3, Q.7, Q.8 around the five outstanding refinements. Identifies dependencies, deliverables, and the cascade FORCED-GRH would deliver back into Arc M and the broader QM-emergence inventory.
**Predecessor:** [`grh_evaluation.md`](grh_evaluation.md) (Q.1) — establishes GRH as CANDIDATE-strong with all four clauses (Case P, (1/2,1/2), gauge-invariant L3, σ=0 via MR-P) structurally admissible and no clause REFUTED on any axis. Q.1's closing classification: "REQUIRES REFINEMENT" with R-1 through R-5 distributed across Q.2 / Q.3 / Q.7 / Q.8.
**Purpose:** Lay out the closure trajectory at a glance so subsequent memos (Memo 00 for Q.2 first) can target specific refinements without re-scoping the whole effort each time.

---

## 1. The Question, Re-stated Compactly

GRH (Gauge-field-as-Rule-Type Hypothesis) asserts that the gauge connection $A_\mu$ — the field behind electromagnetism and the other force-carriers — is itself the participation measure of a specific rule-type $\tau_g$ with four properties:

- **(GRH-1)** $\tau_g$ is **Case P** — bosonic ($\eta = +1$, integer spin)
- **(GRH-2)** $\tau_g$ carries the **(1/2, 1/2) Lorentz representation** — four-vector under $\mathrm{SO}^+(3,1)$
- **(GRH-3)** $\tau_g$ has an **L3 interface enforcing local gauge invariance** $A_\mu \to A_\mu + \partial_\mu \alpha$
- **(GRH-4)** $\sigma_{\tau_g} = 0$ (structurally massless) via the MR-P mechanism of Stage M.1.2

Q.1 evaluated these against ED's primitive stack and the closed Phase-1 + Phase-2 (Arc R + Arc M) structural foundation. Verdict: **CANDIDATE-strong; five refinements outstanding.** None blocks closure; each has a natural Arc Q home.

The closure path is the discharge of those five refinements. Once they close affirmatively, Arc Q synthesis promotes GRH from CANDIDATE-strong to FORCED-unconditional, and the cascade promotes Arc M's F-M8 (massless Case-P rule-type existence) from FORCED-conditional to FORCED-unconditional.

---

## 2. The Five Refinements and Their Substage Homes

From `grh_evaluation.md` §6.3 + §7.3:

| Refinement | Description | Discharged at | Substage focus |
|---|---|---|---|
| **R-1** | Lightlike-worldline reformulation. The Stage R.1 commitment-rate construction along $\gamma_K$ assumes a timelike worldline parametrised by proper time. Lightlike worldlines have $d\tau = 0$, breaking this. Per-worldline accounting must be re-anchored in a lightlike affine parameter. | **Q.7** (second quantisation) | Reformulate per-worldline accounting on lightlike $\gamma_{\tau_g}$; affine-parameter machinery |
| **R-2** | Gauge-quotient individuation. Two $A_\mu$ configurations differing by a pure-gauge $\partial_\mu \alpha$ are physically equivalent; Primitive 10 individuation must respect this gauge equivalence. Whether the threshold automatically respects it, or requires an explicit gauge-quotient structure, is the question. | **Q.2** / **Q.3** | Add gauge-quotient structure to individuation; verify counting respects equivalence classes |
| **R-3** | Vertex-anchored commitment. For $\tau_g$ the commitment events are not at intrinsic points along its own worldline (no rest frame for lightlike) but at interaction vertices with charged rule-types. Commitment is *vertex-sourced*, not worldline-intrinsic. | **Q.3** (interaction vertex classification) | Specify vertex structure; classify gauge-rule-type / charged-rule-type interactions |
| **R-4** | Non-Abelian extension scoping. The R.1 minimal-coupling derivation produced $U(1)$. Extension to non-Abelian gauge groups requires enriching $\tau_g$'s internal index space, self-coupling $[A_\mu, A_\nu]$ in $F^a_{\mu\nu}$, and charged rule-types in non-trivial gauge representations. Whether this is primitive-derivable or requires structural extension is open. | **Q.2** (gauge group scoping) | Scope non-Abelian admissibility; scoping memo for SU(N) extension; honest deferral of SM gauge group choice to empirical inheritance |
| **R-5** | Vacuum-vs-particle status. Is $\tau_g$ a "vacuum-occupying" rule-type (global background) or "particle-like" (concentrated near interactions)? Empirically, photons are both — vacuum fluctuations + propagating particles. ED analogue requires Q.7 / Q.8 closure to disambiguate. | **Q.7** / **Q.8** | Reconcile background-field and particle interpretations; discharge via second quantisation framework |

**Substage load summary:**

- **Q.2:** R-2 (partial), R-4 — heaviest single-substage load; opens the closure trajectory
- **Q.3:** R-2 (completion), R-3 — vertex-classification work; depends on Q.2
- **Q.7:** R-1, R-5 (partial) — second-quantisation reformulation; depends on Q.2 / Q.3
- **Q.8:** R-5 (completion) — vacuum / zero-point closure; depends on Q.7

---

## 3. Sequencing

The dependency structure forces a specific order:

```
Q.2 (gauge group scoping)            ← discharges R-2 (partial) + R-4
   ↓
Q.3 (interaction vertex classification)  ← discharges R-2 (completion) + R-3
   ↓
Q.7 (second quantisation)            ← discharges R-1 + R-5 (partial)
   ↓
Q.8 (vacuum and zero-point)          ← discharges R-5 (completion)
   ↓
Arc Q synthesis                      ← promotes GRH to FORCED-unconditional
   ↓
Cascade back to Arc M                ← F-M8 (massless slot existence) promoted to FORCED-unconditional
```

The arrows are dependency arrows, not strict sequencing — Q.7 could in principle proceed in parallel with Q.3 if R-3 and R-1 don't interact. But the cleanest serial order is Q.2 → Q.3 → Q.7 → Q.8 → synthesis.

---

## 4. Per-Substage Scope Sketch

### Q.2 — Gauge Group Scoping

**Goal.** Address R-4 (non-Abelian extension scoping) and R-2 (gauge-quotient individuation, partial) at the level of the gauge group itself. Establish what GRH says — and doesn't say — about the choice of gauge group.

**Anticipated content:**
- Explicit enumeration of the U(1) case (already FORCED at Stage R.1 from local-phase invariance) as the GRH baseline
- Non-Abelian admissibility scoping: structural conditions under which $\tau_g$ extends to SU(N) — internal-index enrichment, self-coupling structure, charged-rule-type representation
- Honest deferral of the specific Standard Model gauge group $SU(3) \times SU(2) \times U(1)$ to empirical inheritance (per Q.0 framing)
- Gauge-quotient individuation structure: how Primitive 10 individuation respects $A_\mu \sim A_\mu + \partial_\mu \alpha$ equivalence
- Forbidden-input discipline: no SM-specific gauge content used as derivation premise

**Anticipated verdict:** R-4 closes as "non-Abelian admissible at structural level; specific gauge group inherited"; R-2 partially closes ("gauge-quotient individuation structurally available; specific quotient construction deferred to Q.3"). Memo plan: 3–4 memos parallel to U3 arc structure.

### Q.3 — Interaction Vertex Classification

**Goal.** Address R-3 (vertex-anchored commitment) and R-2 (completion). Specify the vertex structure for charged-rule-type / gauge-rule-type interactions, including how commitment events are sourced at vertices rather than along $\gamma_{\tau_g}$.

**Anticipated content:**
- Vertex taxonomy: emission vertex (charged → charged + gauge), absorption vertex (charged + gauge → charged), self-interaction vertex (gauge × gauge → gauge for non-Abelian cases)
- Commitment-event localization at vertices, with the lightlike $\gamma_{\tau_g}$ between vertices being commitment-free
- Gauge-quotient at the vertex level: vertices are well-defined modulo gauge equivalence
- Connection to standard QFT vertex factors (verify ED's vertex content reduces to standard QED / QCD vertex content in the appropriate limit, without forcing the SM gauge structure)

**Anticipated verdict:** R-3 closes; R-2 fully closes. Memo plan: 3 memos.

### Q.7 — Second Quantisation

**Goal.** Address R-1 (lightlike-worldline reformulation) and R-5 (vacuum-vs-particle status, partial). Develop the second-quantisation framework for ED, with affine-parameter accounting for lightlike rule-types.

**Anticipated content:**
- Affine-parameter machinery for lightlike $\gamma_{\tau_g}$ replacing the proper-time parametrisation
- Per-worldline commitment-rate reformulation in the affine-parameter framework
- Creation / annihilation operator structure for $\tau_g$ (and for charged rule-types) in the ED participation-measure formalism
- Initial reconciliation of vacuum-field and particle interpretations
- Connection to Theorem 6 (canonical (anti-)commutation) — verify consistency

**Anticipated verdict:** R-1 closes; R-5 partially closes (vacuum-field aspect established, zero-point aspect deferred to Q.8). Memo plan: 4–5 memos (substantively heavier than Q.2 / Q.3).

### Q.8 — Vacuum and Zero-Point

**Goal.** Address R-5 (completion). Establish the vacuum state and zero-point structure for $\tau_g$, fully reconciling the vacuum-occupying and particle-like aspects.

**Anticipated content:**
- Vacuum state of $\tau_g$ as a specific participation-measure configuration (not zero-everywhere)
- Zero-point fluctuations as primitive-level structural content of the vacuum, not artifacts of normal-ordering
- Connection to Theorem 7 (UV-FIN) — vacuum-energy contributions are finite by construction
- Connection to Theorem 8 (V₁ finite-width vacuum kernel, Arc N) — the $V_1$ kernel governs vacuum-state two-point correlations; closure consistency check
- Connection to Theorem 9 (V₁ with Synge world function, Phase-3) — vacuum kernel extends to curved spacetime; gauge-vacuum compatibility check
- Connection to the Λ-from-V₁ derivation (cosmological constant)

**Anticipated verdict:** R-5 fully closes. Memo plan: 3–4 memos.

### Arc Q Synthesis

**Goal.** Promote GRH from CANDIDATE-strong to FORCED-unconditional. Cascade-promote Arc M's F-M8 to FORCED-unconditional.

**Anticipated content:**
- Synthesis of Q.2, Q.3, Q.7, Q.8 results
- Verification that all five refinements close affirmatively
- Verification that no new CANDIDATEs are introduced
- Acyclicity audit for the GRH closure cycle (analogous to U3 acyclicity audit for U3 ↔ U4 loop)
- Statement of the FORCED GRH theorem
- Cascade promotion of Arc M's F-M8
- Update to the structural-foundations theorem inventory (16 → 17 forced theorems)

---

## 5. What FORCED-GRH Would Deliver (Cascade)

Per `grh_evaluation.md` §4:

| Promoted item | From | To |
|---|---|---|
| **F-GRH-A** | Existence of at least one massless Case-P rule-type | CANDIDATE → FORCED |
| **F-GRH-B** | Gauge invariance as a rule-type interface property | reframe ratified |
| **F-GRH-C** | $A_\mu$ transformation law as primitive-level structural redundancy | reframe ratified |
| **F-GRH-D** | Minimal coupling as a structural interaction (not an add-on procedure) | reframe ratified |
| **F-GRH-E** | M.1.2's F-M8 (massless slot existence) | FORCED-conditional → FORCED-unconditional |

In the structural-foundations inventory, this would add **Theorem 17 (GRH)** to the 16 existing forced theorems, with M.2's F-M8 retroactively promoted from conditional to unconditional.

---

## 6. What GRH Closure Will NOT Deliver (Honest Scoping)

Per `grh_evaluation.md` §5, GRH is narrowly scoped to the massless-slot identification. The following are **not** within GRH's content and remain outside the closure trajectory:

- **Specific gauge group choice** ($SU(3) \times SU(2) \times U(1)$). Empirical inheritance per Q.2.
- **Coupling constants** ($q$, $g_s$, $g_w$). Empirical inheritance via the Dimensional Atlas.
- **Higgs sector / mass-generation**. Q.4 content; SPECULATIVE.
- **Generations / flavour**. Q.6 / empirical.
- **Charge quantisation** ($e/3$ for quarks). Possibly Q.2 partial; possibly empirical.

These are honest scope limits, not failures. ED's program treats Standard Model specifics as empirical inheritance — same methodology as Arc M's "form FORCED, value INHERITED" framing.

---

## 7. Forbidden-Input Discipline (Acyclicity)

The same discipline that closed U3 ↔ U4 acyclically applies to GRH closure. In particular:

- **R.1 minimal coupling** is the *origin* of $A_\mu$ as a structural object. GRH closure may use R.1 as background but cannot circularly invoke "GRH closes therefore R.1's $A_\mu$ is a rule-type" as a derivation step.
- **M.1.2 conditional results (F-M8)** are the *target* of the GRH cascade. GRH closure may not use F-M8 as a derivation premise.
- **SM gauge group, Higgs, generations** are explicitly forbidden as derivation premises (per Q.0 § scoping).
- **Standard QFT machinery** (canonical-quantization-as-procedure, Feynman rules as postulates) is forbidden — Q.7's second quantisation must derive from primitives, not import.

Each Q.2 / Q.3 / Q.7 / Q.8 memo will carry an explicit forbidden-input audit, following the U3 Memo 01 §2 + Memo 03 §1.4 templates.

---

## 8. Comparison to U3 Closure Pattern

The GRH closure trajectory mirrors the U3 arc structure but spans four substages instead of one arc:

| Aspect | U3 arc | GRH closure |
|---|---|---|
| Starting status | CANDIDATE | CANDIDATE-strong |
| Sub-features / refinements | 5 (F1–F5) | 5 (R-1 to R-5) |
| Forbidden-input discipline | U4 forbidden as derivation premise | R.1 / F-M8 / SM specifics forbidden |
| Load-bearing item | F5 (compatibility with U4) | R-4 (non-Abelian extension) and R-5 (vacuum-vs-particle) |
| Cascade on closure | U4 promoted retroactively | F-M8 promoted retroactively |
| Number of memos | 4 (00–03) + closure | Anticipated 13–17 across Q.2 / Q.3 / Q.7 / Q.8 + synthesis |
| Methodology | Stone's theorem on time-translation + Galilean closure | Discharge each refinement via its substage; synthesis ties them together |

The methodological pattern is the same; the scope is broader because the closure is multi-substage rather than single-arc.

---

## 9. Recommended Next Steps

**(a) Open Q.2 (gauge group scoping) Memo 00.** The natural next deliverable. Memo 00 should:

- Restate Q.2's question precisely: what does GRH say about the choice of gauge group, and what does it not say?
- Decompose Q.2 into sub-features (likely: R-4 substructure, R-2 partial, U(1) baseline confirmation, non-Abelian admissibility, gauge-quotient individuation structure)
- Inventory structural inputs (R.1 minimal coupling as background, R.2 Lorentz-rep ladder, Primitives 02/06/07/10)
- Set forbidden-input discipline (no SM gauge content, no specific coupling values, no F-M8 invocation)
- Falsifier inventory for what would refute GRH at the gauge-group-scoping level

Anticipated length: comparable to U3 Memo 00. Format: same template as `arcs/U3/00_arc_outline.md`.

**(b) Pre-Memo-00 audit of Q.0 + Q.1 framings.** Short audit (15–30 minutes) to confirm that Q.2's scope as I've sketched it here is consistent with what Q.0 originally scoped. Specifically: verify that R-4 (non-Abelian extension scoping) is treated as Q.2 content per Q.0, not deferred to a later substage. The GRH evaluation memo §5.3 supports this (R-4 flagged for Q.2), but a quick check of `qft_extension_scoping.md` (Q.0) would be due diligence.

**(c) Defer memory-record update until Q.2 closure.** Per the discipline established in U3 / U1 / U4 / U5 arcs. The bundled memory update should capture the post-Q.2 state including R-4 + R-2 (partial) discharge, gauge-group scoping verdict, and any new CANDIDATEs introduced (anticipated: zero, mirroring the prior arcs).

---

## 10. Cross-References

- Q.1 evaluation (immediate predecessor): [`grh_evaluation.md`](grh_evaluation.md)
- Q.0 scoping: `qft_extension_scoping.md` (need to confirm path; referenced in §10 of GRH eval)
- R.1 minimal coupling: `kg_minimal_coupling_and_current.md` (origin of $A_\mu$)
- R.2 spin-statistics + Cl(3,1): `clifford_algebra_from_spinor_structure.md`, `rule_type_taxonomy_synthesis.md`
- M.1.2 massless rule-types (origin of GRH): `massless_rule_types.md`
- M.2 chain-mass synthesis (cascade target): `chain_mass_synthesis.md`
- U3 Memo 00 (template for Q.2 Memo 00): `../U3/00_arc_outline.md`
- Project memory: `memory/project_qm_emergence_arc.md`

---

## 11. One-Line Roadmap Summary

> GRH closure is a four-substage trajectory (Q.2 → Q.3 → Q.7 → Q.8 → Arc Q synthesis) discharging the five refinements (R-1 through R-5) Q.1 left outstanding; each substage carries 1–2 refinements with explicit dependencies; closure promotes GRH from CANDIDATE-strong to FORCED-unconditional and cascades-promotes Arc M's F-M8 (massless slot existence) from conditional to unconditional, adding a 17th forced theorem to the structural-foundations inventory; methodology mirrors the U3 closure arc but spans four substages instead of one; explicit forbidden-input discipline preserves acyclicity (R.1 / F-M8 / SM specifics may not be derivation premises); the natural next step is Q.2 Memo 00 (gauge group scoping, discharging R-4 + R-2 partial).
