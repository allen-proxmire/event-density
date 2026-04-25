# GRH Evaluation

**Stage Q.1 — Arc Q Sub-Memo**
**Status:** Evaluation memo. Headline verdict: **GRH = CANDIDATE-STRONG REQUIRES REFINEMENT.** GRH is structurally admissible, primitive-consistent, and uniquely closes the M.1.2 conditional massless-slot existence. It is not yet FORCED — three refinements are required (lightlike-worldline reformulation, non-Abelian extension scoping, vacuum-state status of the gauge rule-type) before promotion to unconditional FORCED. None of the refinements is a structural blocker; all are deferred to specific later stages. GRH is not REFUTED on any axis examined.

---

## 1. Goal

Stage Q.0 introduced GRH (Gauge-field-as-Rule-Type Hypothesis) as the first major CANDIDATE of Arc Q. Stage Q.1 evaluates it against ED's primitive stack and the closed Phase-1 + Phase-2 (Arc R + Arc M) structural foundation.

Specifically:

(a) Restate GRH precisely as a four-clause structural commitment.
(b) Evaluate each clause against Primitives 02, 04, 06, 07, 10, 11 and against Stages R.2 and M.2.
(c) Identify what GRH would FORCE if affirmatively closed.
(d) Identify what GRH leaves open as downstream Arc Q work or empirical inheritance.
(e) Produce a per-clause FORCED / CANDIDATE / REFUTED table.
(f) Issue a closing verdict: FORCED / CANDIDATE-strong / CANDIDATE-weak / REQUIRES REFINEMENT / REFUTED.

This memo does **not** derive specific gauge groups, coupling constants, or non-Abelian extensions. Those are downstream (Q.2 onward).

---

## 2. GRH restated precisely

**GRH (formal four-clause statement):**

The gauge connection A_μ that appears in Stage R.1 / R.3 minimal coupling D_μ = ∂_μ + (iq/ℏ)A_μ is the participation measure of a specific rule-type τ_g satisfying:

- **(GRH-1)** τ_g is a **Case-P rule-type** — bosonic (η = +1, integer spin).
- **(GRH-2)** τ_g carries the **(1/2, 1/2) Lorentz representation** — a four-vector under SO⁺(3,1).
- **(GRH-3)** τ_g has an **L3 interface enforcing local gauge invariance** A_μ → A_μ + ∂_μα.
- **(GRH-4)** **σ_{τ_g} = 0** (structurally massless) via the MR-P mechanism of Stage M.1.2.

Equivalently: A_μ is not an abstract structural connection imposed externally on the participation measure; A_μ is itself a participation measure with its own four-band content, its own rule-type, its own (massless) dynamical equations, and its own coupling structure to other rule-types via the existing Stage R.1 minimal-coupling derivation.

The four clauses are interdependent but not redundant: (GRH-2) fixes the Lorentz-rep slot, (GRH-1) fixes the statistics, (GRH-3) fixes the interface constraint that produces masslessness, and (GRH-4) records the consequence. Refuting any one clause refutes GRH; all four must close affirmatively.

---

## 3. Primitive-by-primitive evaluation

### 3.1 Primitive 02 (worldline + ambient 3+1D manifold)

**Question.** Does Primitive 02 admit a rule-type whose worldline is lightlike — i.e., compatible with massless τ_g?

**Evaluation.** Primitive 02 specifies the worldline structure but does not exclude lightlike worldlines. Indeed, lightlike trajectories are a structural feature of 3+1D Minkowski manifolds and Primitive 06's four-gradient covariance permits them.

However, the standard Stage R.1 commitment-rate construction along γ_K assumes a timelike worldline parametrised by proper time τ_K (Primitive 13). Lightlike worldlines have dτ = 0, breaking this parametrisation. This is a **real refinement requirement** — the per-worldline accounting that worked for massive rule-types must be re-anchored in a lightlike affine parameter.

**Status:** Primitive 02 admits lightlike rule-types in principle; commitment / proper-time machinery requires reformulation. **Refinement R-1 (lightlike-worldline reformulation)** flagged for Stage Q.1.5 or Q.7.

**Verdict:** CANDIDATE compatible — refinement needed but not blocking.

### 3.2 Primitive 04 (bandwidth fields)

**Question.** Can a rule-type carrying the gauge connection A_μ have its own four-band bandwidth content b_K^{int}, b_K^{adj}, b_K^{env}, b_K^{com}?

**Evaluation.** Primitive 04's four-band decomposition is rule-type-agnostic — it applies to any participation measure. The gauge-rule-type's bandwidth content would track:

- **b^{int}:** internal four-vector content of A_μ.
- **b^{adj}:** adjacency to charged rule-types via the minimal-coupling vertex.
- **b^{env}:** environment dissipation (radiation field decoherence).
- **b^{com}:** commitment events along γ_{τ_g}.

For a massless rule-type with lightlike worldline, b^{com} → 0 in the rest frame is consistent with M.1.2 hypothesis Mλ. The remaining three bands are well-defined.

**Status:** Primitive 04 is fully compatible with GRH. No refinement needed.

**Verdict:** CANDIDATE compatible — clean.

### 3.3 Primitive 06 (four-gradient + Lorentz covariance)

**Question.** Does Primitive 06's four-gradient and Lorentz-covariance structure support a (1/2, 1/2) participation measure?

**Evaluation.** Stage R.2.2 established the (j_L, j_R) ladder including (1/2, 1/2) — the four-vector representation. The participation measure for this representation is exactly an A_μ-like four-component object transforming via the standard SO⁺(3,1) defining representation. This is structurally clean and built into Primitive 06.

(GRH-2) is **directly compatible** with Primitive 06.

**Verdict:** FORCED-compatible. (GRH-2) is structurally admissible without refinement.

### 3.4 Primitive 07 (rule-type taxonomy, Levers L1–L4)

**Question.** Can rule-type taxonomy (L1 bandwidth partition, L2 internal-index, L3 interface, L4 statistics class) support a τ_g with the GRH properties?

**Evaluation.**

- **L1 (bandwidth partition):** w_{τ_g}^X is rule-type data; any non-negative partition is admissible. No constraint from primitives.
- **L2 (internal index):** (1/2, 1/2) is a valid Lorentz representation (R.2.2). Compatible.
- **L3 (interface):** This is the critical lever. (GRH-3) requires the L3 interface to enforce **local gauge invariance** A_μ → A_μ + ∂_μα. Stage R.2.4 §5.1 established that interface content for Case-P rule-types is specified by Lorentz-covariant bilinears or tensor structures. Gauge-invariance is a **structurally available constraint** at the L3 level — it amounts to saying the rule-type's interface content is invariant under the addition of pure-gauge ∂_μα to A_μ. No primitive-level obstruction. Whether the **specific** gauge constraint is FORCED for τ_g, or merely admissible as one option among many for L3, is the open question — Stage M.1.2 §4.3 left this as part of CANDIDATE GRH itself.
- **L4 (statistics class):** Case P (η = +1) consistent with integer spin s = 1 (from (1/2, 1/2)).

**Status:** All four levers admit a τ_g with GRH properties. L3 is the lever that carries GRH's load — gauge-invariance must be the L3 interface's specific content, which is rule-type data not primitive-forced.

**Verdict:** CANDIDATE compatible. L3 specifically is rule-type data; primitives admit it but do not force it.

### 3.5 Primitive 10 (individuation threshold)

**Question.** How does individuation apply to a massless gauge rule-type?

**Evaluation.** Primitive 10's individuation threshold tests whether two same-type chains remain distinguishable. For Case-R rule-types, individuation excludes coincidence (vanishing-on-coincidence). For Case-P rule-types (including τ_g), coincidence is permitted.

Two photon-like chains can occupy the same event-manifold neighbourhood without violating individuation — this is consistent with Bose-Einstein statistics and photon coherence. No structural obstruction.

A subtlety: gauge invariance A_μ → A_μ + ∂_μα is a **continuous** local symmetry, meaning two A_μ configurations differing by a pure-gauge term are physically equivalent. Individuation must respect this — two gauge-equivalent A_μ configurations should not be counted as distinct. Whether Primitive 10's individuation threshold automatically respects gauge-equivalence, or requires an additional gauge-quotient structure at the individuation level, is **Refinement R-2 (gauge-quotient individuation)**.

**Status:** Primitive 10 is compatible. Refinement R-2 (gauge-quotient at individuation level) flagged for Q.2 / Q.3 detail.

**Verdict:** CANDIDATE compatible — minor refinement.

### 3.6 Primitive 11 (commitment dynamics)

**Question.** Does τ_g carry commitment events?

**Evaluation.** For massless rule-types via M.1.2 hypothesis Mλ, w^{com} → 0 in the rest frame. But there is no rest frame for a lightlike worldline. So the question becomes: is commitment well-defined in any frame for τ_g?

Empirical analogue: photon emission and absorption are clearly events — they are commitment-event analogues. So commitment for τ_g exists, but it is sourced **off-worldline** — emission from a charged-rule-type-worldline and absorption onto another charged-rule-type-worldline. The gauge rule-type's commitment events are at the **interaction vertices** with charged rule-types, not at intrinsic points along its own worldline.

This is a structural shift from Phase-1's single-rule-type picture. A gauge rule-type's commitment is *vertex-anchored*, not worldline-intrinsic. **Refinement R-3 (vertex-anchored commitment for gauge rule-types)** flagged for Q.3 (vertex classification).

**Status:** Primitive 11 is compatible but with a structural reformulation: commitment for τ_g is sourced at interaction vertices with charged rule-types. This is consistent with photon emission/absorption phenomenology.

**Verdict:** CANDIDATE compatible — structural reformulation needed.

### 3.7 Stage R.2 (spin-statistics + Clifford)

**Question.** Does R.2 admit τ_g as constructed?

**Evaluation.**

- (GRH-1) Case P: matches s = 1 integer spin, η = +1 by R.2.5 spin-statistics. **FORCED-compatible.**
- (GRH-2) (1/2, 1/2): this is the (j_L, j_R) = (1/2, 1/2) representation, dimension 4, transforming as a four-vector. **FORCED-admissible** by R.2.2 §3.3.
- (GRH-3) Gauge invariance at L3: structurally admissible interface content. CANDIDATE compatible.
- (GRH-4) σ = 0 via MR-P: established in M.1.2 §4 as the gauge-massless mechanism. **FORCED-compatible.**

R.2's framework cleanly accommodates τ_g across all four GRH clauses. No conflict.

**Verdict:** GRH is consistent with R.2 closure on all four clauses.

### 3.8 Stage M.2 (chain-mass closure)

**Question.** Does M.2 support GRH?

**Evaluation.** M.2 explicitly identified GRH as the conditional closure point for the massless-slot existence claim:

> *"Massless Case-P rule-types: FORCED conditional on GRH"* (M.1.2 §6.4)
> *"GRH closure → F-M8 unconditional FORCED"* (M.2 dependency diagram §9)

GRH is the **already-recognised** closure point for Arc M's conditional structural prediction. M.2 explicitly hands the question to Arc Q with the expectation that Q.1 will discharge it.

If GRH closes affirmatively at Q.1, M.1.2's F-GRH-1 and F-GRH-2 promote from "FORCED conditional on CANDIDATE" to "unconditional FORCED" — the chain closes back to M.

**Verdict:** GRH is structurally **expected** by M.2. Arc Q.1 closure feeds back into Arc M cleanly.

---

## 4. What GRH would FORCE if affirmatively closed

Affirmative GRH closure would promote the following from CANDIDATE / conditional to FORCED:

### 4.1 (F-GRH-A) Existence of at least one massless Case-P rule-type

The gauge-rule-type τ_g is structurally required by minimal coupling (Stage R.1) and satisfies all four GRH clauses ⇒ exists with σ = 0.

This is the headline FORCED-by-GRH content. It is ED's first structural prediction of a specific massless particle class.

### 4.2 (F-GRH-B) Gauge invariance as a rule-type interface property

Local gauge invariance is not an externally-imposed symmetry but a structural property of the τ_g rule-type's L3 interface. This recasts gauge invariance from "fundamental symmetry principle" to "rule-type interface specification."

This is a substantive ontological reframing: ED treats gauge invariance as a *consequence* of rule-type structure, not a *postulate*.

### 4.3 (F-GRH-C) A_μ transformation law as a rule-type update rule

A_μ → A_μ + ∂_μα is a local update rule on the gauge rule-type's participation measure. The pure-gauge ∂_μα is a structural redundancy at the L3 interface — different A_μ configurations differing by a pure-gauge term represent the same primitive content.

This makes the gauge equivalence class [A_μ] a primitive-level object, not a derived one.

### 4.4 (F-GRH-D) Minimal coupling as a structural interaction

Minimal coupling D_μ = ∂_μ + (iq/ℏ)A_μ is no longer "an add-on procedure" but the primitive-level interaction vertex between the gauge rule-type and charged rule-types. It is a Stage R.1-derived consequence of local-phase invariance, not a postulate.

This was already implicit in Stage R.1's `kg_minimal_coupling_and_current.md`; GRH closes it explicitly by giving A_μ rule-type status.

### 4.5 (F-GRH-E) Promotion of M.1.2 conditional results

- F-M8 (massless Case-P rule-type forced) → unconditional FORCED.
- M.1.2 §9.1: existence of massless species → FORCED unconditionally.
- This is the back-flow into Arc M's closure.

---

## 5. What GRH leaves open

GRH is a structural commitment about A_μ's status as a rule-type. It does **not** close the following:

### 5.1 Gauge group (U(1) vs SU(2) vs SU(3) vs combinations)

GRH says A_μ is a rule-type with gauge-invariant L3 interface. It does **not** specify which gauge group's invariance is enforced. U(1) is the minimum (already FORCED at Stage R.1 from local-phase invariance); whether non-Abelian groups are forced or admissible-but-not-required is **Q.2** content.

**Status:** Q.2 deliverable. Likely empirical-inheritance closure.

### 5.2 Coupling constants

The numerical value of q (electromagnetic charge), g_s (strong coupling), g_w (weak coupling), etc. is rule-type data per the charge spectrum. GRH does not constrain these values.

**Status:** Empirical inheritance via the Dimensional Atlas. Numerical values not predicted.

### 5.3 Non-Abelian structure

For non-Abelian gauge groups, A_μ is Lie-algebra-valued, with internal index a (for SU(N), a runs over the Lie-algebra dimension N²−1). The Stage R.1 minimal-coupling derivation produced U(1); extension to non-Abelian requires:

- Enriching τ_g's internal index space beyond (1/2, 1/2) to carry the Lie-algebra multiplicity.
- Self-coupling of A^a_μ via [A_μ, A_ν] terms in F^a_{μν}.
- Charged rule-types transforming in non-trivial gauge representations.

**Refinement R-4 (non-Abelian extension):** flagged for Q.2. Whether non-Abelian gauge structure is primitive-derivable or requires structural extension is genuinely open.

### 5.4 Higgs-like mass generation

GRH establishes that gauge rule-types are **massless**; how mass is then *given* to W/Z-like gauge bosons via SSB is Q.4 content. This is independent of GRH.

**Status:** Q.4 deliverable. Likely SPECULATIVE per Arc M / Q.0 framing.

### 5.5 Generations

GRH says nothing about fermion-rule-type multiplicity. The number of generations is unaffected by GRH closure.

**Status:** Q.6 / empirical.

### 5.6 Charge quantisation

Why charges come in integer multiples of e/3 (or e for leptons) is not addressed by GRH. Possibly Dirac-monopole-style argument or topological; possibly empirical.

**Status:** SPECULATIVE; possibly Q.2 partial.

---

## 6. Per-clause FORCED / CANDIDATE / REFUTED table

### 6.1 GRH clauses

| Clause | Statement | Status | Reason |
|--------|-----------|--------|--------|
| GRH-1 | τ_g is Case P | **CANDIDATE-FORCED** | s = 1 ⇒ η = +1 by R.2.5 spin-statistics |
| GRH-2 | τ_g carries (1/2, 1/2) | **CANDIDATE-FORCED** | (1/2, 1/2) admissible by R.2.2; vector-rep matches A_μ four-component structure |
| GRH-3 | L3 enforces gauge invariance | **CANDIDATE** | Structurally admissible; not primitive-forced beyond U(1); rule-type data |
| GRH-4 | σ_{τ_g} = 0 via MR-P | **CANDIDATE-FORCED** | Direct consequence of GRH-3 + M.1.2 §4 |

"CANDIDATE-FORCED" = forced conditional on GRH-3, which is the load-bearing clause.

### 6.2 GRH-3 sub-evaluation

GRH-3 itself decomposes into:

| Sub-claim | Status | Reason |
|-----------|--------|--------|
| Gauge invariance is structurally admissible at L3 | **FORCED** | Primitive 07 + R.2.4 admit it as one possible interface content |
| Gauge invariance is forced on at least one rule-type | **CANDIDATE-FORCED** | R.1 minimal-coupling forces existence of A_μ; identification with rule-type is GRH itself |
| Specific gauge group is forced | **REFUTED** | Q.0 §5.2; SM gauge group expected empirical |

The middle row is the structural content of GRH proper. It closes affirmatively if and only if the identification of the R.1-forced A_μ with a participation rule-type is structurally consistent — which §3 of this memo established it is, modulo three refinements.

### 6.3 Refinements required (not blockers)

| Refinement | Source | Deferred to |
|-----------|--------|------------|
| R-1: Lightlike-worldline reformulation | §3.1 | Q.1.5 or Q.7 |
| R-2: Gauge-quotient individuation | §3.5 | Q.2 / Q.3 |
| R-3: Vertex-anchored commitment | §3.6 | Q.3 |
| R-4: Non-Abelian extension scoping | §5.3 | Q.2 |

None of R-1 through R-4 is a structural blocker for GRH closure. Each is a downstream refinement that becomes natural once GRH is admitted.

### 6.4 Vacuum-state status of τ_g

Open question not directly addressed by GRH-1 through GRH-4: is τ_g a "vacuum-occupying" rule-type whose participation field A_μ is a global background structure of the event manifold, or is it a "particle-like" rule-type whose participation is concentrated near interactions?

Empirically, photons can be both — vacuum field fluctuations + propagating particles. ED's analogue requires Q.7 / Q.8 closure to disambiguate.

**Refinement R-5 (vacuum vs. particle status of τ_g):** flagged for Q.7 / Q.8.

---

## 7. Verdict

### 7.1 Summary

- **GRH is CANDIDATE-STRONG.** All four clauses are structurally admissible against every primitive examined. Three GRH clauses (GRH-1, GRH-2, GRH-4) are CANDIDATE-FORCED conditional on GRH-3; GRH-3 itself is admissible at primitive level and consistent with R.2 + M.2. No clause is REFUTED.
- **Refinements R-1 through R-5 are required** before GRH can be promoted to unconditional FORCED. None is a structural blocker; all are well-localised and have natural Arc Q homes.
- **No primitive-level obstruction identified.** Primitives 02, 04, 06, 07, 10, 11 all admit τ_g with GRH properties. Stage R.2 fully accommodates τ_g; Stage M.2 explicitly expects GRH closure.

### 7.2 Closing classification

| Verdict option | Choice |
|---------------|--------|
| FORCED | **Not yet** — five refinements outstanding |
| CANDIDATE-strong | **YES** — admissible across all primitive checks, no obstruction |
| CANDIDATE-weak | No — too well-supported for "weak" |
| REQUIRES REFINEMENT | **YES** — R-1 through R-5 needed before unconditional FORCED |
| REFUTED | No — no clause REFUTED on any axis |

**Final verdict: GRH = CANDIDATE-STRONG, REQUIRES REFINEMENT.**

This is the strongest possible Q.1 closure given the residual refinement work. GRH is structurally well-grounded but not yet airtight; promotion to unconditional FORCED requires the five refinements to land affirmatively.

### 7.3 Implications for downstream Arc Q substages

- **M.2 closure update:** F-M8 remains "FORCED conditional on GRH" until refinements close. Arc M's H1-dominant verdict is unchanged at this stage.
- **Q.2 (gauge group):** proceeds with GRH as working hypothesis; the U(1)-vs-SU(N) question and R-4 are addressed jointly.
- **Q.3 (vertices):** uses GRH + R-3 to specify vertex structure for charged-rule-type / gauge-rule-type interactions.
- **Q.7 (second quantisation):** discharges R-1 (lightlike-worldline reformulation) and R-5 (vacuum status).
- **Q.8 (vacuum):** discharges R-5 fully and clarifies zero-point participation.

The five refinements distribute naturally across Q.2, Q.3, Q.7, Q.8 — each downstream substage carries one or two pieces of the GRH-completion work, and the Arc Q synthesis at the end will integrate them.

---

## 8. Comparison with other ED CANDIDATE evaluations

GRH's CANDIDATE-strong verdict places it among ED's well-supported but not-yet-FORCED structural conjectures:

| CANDIDATE | Stage | Status |
|-----------|-------|--------|
| FA (frame-availability) | R.2.3 | Discharged at R.2.4 via Cl(3,1) |
| MB (minimal bilinear) | R.2.4 | Discharged at R.2.5 via Primitive 10 pairing |
| Mλ (massless ⟺ no commitment) | M.1.1 | Standing CANDIDATE |
| GRH (gauge-field-as-rule-type) | M.1.2, Q.0, Q.1 | **CANDIDATE-STRONG; refinements R-1 through R-5** |
| Q-couplings to specific gauge group | Q.0 | Expected empirical |

GRH is structurally healthier than Mλ (which has no clear closure path) and on par with FA / MB at their pre-discharge stages. Expected closure trajectory: refinements close at Q.2, Q.3, Q.7, Q.8 → Arc Q synthesis promotes GRH to FORCED.

---

## 9. FORCED / CANDIDATE / REFUTED summary

### 9.1 FORCED

- **F-Q1.1.** (1/2, 1/2) Lorentz representation is admissible per R.2.2; corresponds structurally to A_μ's four-vector content.
- **F-Q1.2.** Spin-statistics (s = 1, η = +1, Case P) for τ_g is consistent with GRH-1 by R.2.5.
- **F-Q1.3.** Gauge invariance is structurally admissible as L3 interface content per R.2.4 §5.
- **F-Q1.4.** R.1 minimal coupling forces existence of A_μ as a structural object (already FORCED, recap).
- **F-Q1.5.** σ_{τ_g} = 0 follows from GRH-3 + M.1.2 §4 (MR-P mechanism).
- **F-Q1.6.** Primitives 02, 04, 06, 07, 10, 11 are all individually compatible with τ_g (per §3 evaluation).

### 9.2 CANDIDATE

- **C-Q1.1.** GRH proper: identification of R.1-forced A_μ with a participation rule-type τ_g. CANDIDATE-strong.
- **C-Q1.2.** Refinement R-1 (lightlike-worldline reformulation): expected to close at Q.7.
- **C-Q1.3.** Refinement R-2 (gauge-quotient individuation): expected to close at Q.2/Q.3.
- **C-Q1.4.** Refinement R-3 (vertex-anchored commitment for τ_g): expected to close at Q.3.
- **C-Q1.5.** Refinement R-4 (non-Abelian extension): open; Q.2 deliverable.
- **C-Q1.6.** Refinement R-5 (vacuum vs particle status): open; Q.7/Q.8 deliverable.

### 9.3 REFUTED

- **R-Q1.1.** GRH alone does not force the SM gauge group. Specific gauge-group choice is not GRH content.
- **R-Q1.2.** GRH does not constrain coupling constants. Numerical q, g_s, g_w inherited.
- **R-Q1.3.** GRH does not address generations, flavour, or Higgs mass-generation. These are Q.4–Q.6.

These "REFUTED" entries are not refutations of GRH itself; they are clarifications that GRH's scope is narrower than sometimes assumed. GRH closes the **massless-slot identification**, not the full Standard-Model content.

---

## 10. Cross-references

- Upstream: `qft_extension_scoping.md` (Q.0), `chain_mass_synthesis.md` (M.2), `massless_rule_types.md` (M.1.2 — GRH origin), `kg_minimal_coupling_and_current.md` (R.1 — A_μ origin), `rule_type_taxonomy_synthesis.md` (R.2.5), `clifford_algebra_from_spinor_structure.md` (R.2.4).
- Downstream placeholders: `gauge_group_scoping.md` (Q.2 — discharges R-2, R-4), `interaction_vertex_classification.md` (Q.3 — discharges R-3), `second_quantisation.md` (Q.7 — discharges R-1, R-5 partially), `vacuum_and_zero_point.md` (Q.8 — discharges R-5 fully), `arc_q_synthesis.md`.

---

## 11. One-line summary

**Stage Q.1 evaluates GRH against ED primitives + R.2/M.2 closures and finds it CANDIDATE-STRONG with no clause REFUTED on any axis: all four clauses (Case P, (1/2, 1/2) representation, gauge-invariant L3, σ = 0 via MR-P) are structurally admissible and primitive-consistent, but unconditional FORCED status awaits five refinements (lightlike-worldline reformulation, gauge-quotient individuation, vertex-anchored commitment, non-Abelian extension, vacuum-vs-particle status) distributed naturally across Q.2 / Q.3 / Q.7 / Q.8 — GRH is the strongest non-FORCED CANDIDATE in Arc Q's pipeline and its expected closure trajectory promotes M.1.2's conditional massless-slot existence to unconditional FORCED.**
