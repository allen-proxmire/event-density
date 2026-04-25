# Massless Rule-Types

**Stage M.1.2 — Arc M Sub-Memo**
**Status:** Evaluation memo. Existence of an admissible massless class FORCED at primitive level (σ_τ = 0 is a structurally accessible solution of the Stage M.1.1 master formula). Specific identification of which rule-types occupy the massless class **not** structurally forced. Both candidate mechanisms (MR-R chiral, MR-P gauge) survive as CANDIDATE; neither is structurally forced over the other; the choice is rule-type data, not primitive content.

---

## 1. Goal

Stage M.1.1 identified two primitive-level routes by which a rule-type τ can satisfy σ_τ = 0:

- **MR-R (chiral masslessness):** Case-R bilinear |Ψ̄ Γ_τ Ψ| vanishes identically because Ψ is restricted to a (1/2, 0) or (0, 1/2) sub-module — the Weyl projection. The Dirac mass term Ψ̄Ψ vanishes by chirality.
- **MR-P (gauge masslessness):** Case-P bilinear |Ψ|² is constrained to be constant along the worldline by a gauge invariance acting on the participation measure. The Klein-Gordon mass term cannot be added without breaking the gauge symmetry.

Stage M.1.2 evaluates:

(a) Whether ED primitives **force** σ_τ = 0 for any rule-type class.
(b) Whether MR-R or MR-P is the canonical primitive-level route, or both are admissible.
(c) Whether the massless class is identifiable with empirical species (photon, gluon, graviton-candidate, Weyl-neutrino-candidate).
(d) An honest classification of what ED structure can and cannot predict about masslessness.

This memo does **not** predict masses. It evaluates the structural admissibility and forcing of the σ_τ = 0 condition.

---

## 2. Inputs

### 2.1 From Stage M.1.1

Master formula (M):

  σ_τ = ℏ · √( Σ_X w_τ^X · ⟨ (∂_μ ln b_τ^X)(∂^μ ln b_τ^X) ⟩_τ ).                (1)

Massless condition (8)–(9) of M.1.1: σ_τ = 0 iff for every X with w_τ^X > 0, ⟨(∂ ln b^X)²⟩_τ = 0. Hypothesis Mλ: equivalently, no rest-frame commitment (w^com → 0) and no rest-frame internal evolution.

### 2.2 From Stage R.2 + R.3

- (j_L, j_R) representation classification with chiral sub-modules (1/2, 0) and (0, 1/2).
- Cl(3,1) frame; γ^5 generator distinguishing chiral sectors.
- Dirac equation with mass term mc/ℏ; mass-zero limit is structurally clean (Weyl equation).
- Klein-Gordon equation with mass term m²c²/ℏ²; mass-zero limit gives massless wave equation □Ψ = 0.
- Minimal coupling D_μ = ∂_μ + (iq/ℏ)A_μ from local U(1) invariance.

### 2.3 Primitive-level toolkit

Primitives 02, 04, 06, 07, 10, 11, 13. Of these, the most directly relevant to masslessness are:

- **Primitive 06 (four-gradient):** carries Lorentz covariance; lightlike worldlines exist as a limit case.
- **Primitive 11 (commitment dynamics):** w^com → 0 limit corresponds to no rest-frame commitment.
- **Primitive 13 (proper time):** lightlike worldlines have zero proper-time interval — any rule-type whose worldline can be lightlike has no rest frame, and hence no rest-frame commitment events.

---

## 3. Evaluating MR-R (chiral masslessness)

### 3.1 Mechanism

For a Case-R rule-type with internal Lorentz representation containing both (1/2, 0) and (0, 1/2) — the standard Dirac spinor — the mass-relevant scalar bilinear is

  Ψ̄ Ψ = Ψ_L† Ψ_R + Ψ_R† Ψ_L,                                                  (2)

where Ψ_L, Ψ_R are the left- and right-chirality projections. (2) requires both chiralities to be present.

If a rule-type's internal-index structure (Lever L2) restricts Ψ to (1/2, 0) only — i.e., Ψ_R = 0 — then Ψ̄Ψ ≡ 0 identically. The Dirac mass term cannot exist for this rule-type structurally. The bandwidth signature σ_τ via (1) with Γ_τ = 𝟙 is identically zero.

This is the Weyl-fermion / chiral-massless mechanism at the ED primitive level: a Case-R rule-type with a single-chirality L2 assignment is structurally massless (in the Dirac-mass sense).

### 3.2 Is MR-R forced for any rule-type?

The L2 assignment — which (j_L, j_R) the rule-type carries — is rule-type data (Primitive 07 §7.4), **not** primitive-level forced. ED primitives admit:

- Rule-types with full Dirac module (1/2, 0) ⊕ (0, 1/2): can have m ≠ 0 or m = 0 (ordinary fermions; massless fermions if Ψ̄Ψ = 0 dynamically, but this is fine-tuning, not structural).
- Rule-types with single-chirality module (1/2, 0) only: structurally massless via MR-R.
- Rule-types with mixed assignments (e.g., charged + neutral chiral components): partially massive.

The space of rule-type assignments at L2 is not constrained by primitives beyond the (j_L, j_R) ladder of R.2.2. Therefore:

**FORCED:** ED admits the structural possibility of a single-chirality rule-type, which is then automatically massless via MR-R.

**NOT FORCED:** That any specific rule-type makes this assignment. Whether the neutrino-like rule-type is actually single-chirality (pure Weyl) or admits a (small) Majorana-mass sector remains a rule-type-data question.

### 3.3 Majorana refinement

A second mass-related bilinear exists for Case R: the Majorana mass Ψ^T C Ψ (where C is the charge-conjugation matrix). This vanishes structurally iff the rule-type carries a U(1) charge or other symmetry forbidding Ψ^T C Ψ. The full Case-R massless condition is therefore:

  σ_τ^{Case R} = 0  ⟺  Ψ̄Ψ = 0 (chirality)  AND  Ψ^T C Ψ = 0 (no Majorana mass).  (3)

Neither vanishing is forced by ED primitives in the abstract; both are rule-type-data conditions. ED structurally **permits** σ_τ = 0 via (3) but does not force it for any specific rule-type.

### 3.4 Status of MR-R

- **FORCED:** Structural admissibility of the chiral-massless route. Single-chirality assignment ⇒ Ψ̄Ψ = 0 ⇒ Dirac mass term forbidden.
- **CANDIDATE:** Whether any specific ED rule-type makes this assignment. Empirical question.
- **NOT FORCED:** That any rule-type **must** be single-chirality.

---

## 4. Evaluating MR-P (gauge masslessness)

### 4.1 Mechanism

For a Case-P rule-type with a vector or higher-spin representation, the mass term in the Klein-Gordon-type equation has the form m² A_μ A^μ (Proca) or analogue. Such a term **breaks** local gauge invariance of the form A_μ → A_μ + ∂_μα, because A_μ A^μ is not gauge-invariant.

A rule-type whose interface dynamics (Lever L3) requires local gauge invariance therefore cannot carry a mass term — its bandwidth signature σ_τ is forced to zero by the gauge constraint. This is the gauge-massless mechanism (photon, gluon).

### 4.2 What the gauge constraint actually does in ED

Stage R.1's `kg_minimal_coupling_and_current.md` derived the U(1) gauge structure as a consequence of local-phase-invariance of the participation-measure phase π_K. The gauge field A_μ entered as the connection making ∂_μ → D_μ covariant.

For the gauge field A_μ itself (treated as a Case-P rule-type carrying the gauge connection), the analogous covariance requirement is **gauge invariance** A_μ → A_μ + ∂_μα. A mass term m² A_μA^μ violates this; therefore this Case-P rule-type cannot carry a structural mass term.

**Critical caveat:** The gauge field is not an ED primitive object — it appeared in R.1 as the **connection** required by local phase invariance, not as a participation measure with its own b_K. Treating A_μ as a Case-P rule-type with its own bandwidth signature requires identifying A_μ with the participation-measure of some specific rule-type. This identification is **not** forced by current primitives; it is a structural conjecture (the gauge-field-as-rule-type hypothesis, GRH).

### 4.3 Gauge-Field-as-Rule-Type Hypothesis (GRH)

**GRH:** The gauge connection A_μ that appears in minimal coupling is the participation measure of a Case-P rule-type with internal Lorentz representation (1/2, 1/2) and L3 interface content requiring local gauge invariance.

Under GRH:
- The gauge invariance is a structural property of the gauge-rule-type's L3 interface.
- σ_τ = 0 is FORCED for the gauge rule-type, because mass term breaks the L3 gauge constraint.
- MR-P is the canonical mechanism for the gauge rule-type's masslessness.

**Status of GRH:** CANDIDATE. It is structurally plausible — gauge fields naturally fit the (1/2, 1/2) vector representation, and minimal coupling already inserts them as connection-like participation content — but ED primitives do not currently force the identification. Stage Arc-Q is the natural place to discharge GRH if at all.

### 4.4 Without GRH

Without GRH, MR-P is a **structurally available mechanism** but is not tied to any specific ED rule-type. ED primitives admit Case-P rule-types whose L3 interface includes gauge-invariance constraints, and any such rule-type is automatically massless. But ED does not currently identify any specific rule-type as the gauge-rule-type.

### 4.5 Status of MR-P

- **FORCED:** Structural admissibility of the gauge-massless route. A Case-P rule-type with gauge-invariant L3 interface has σ_τ = 0 structurally.
- **CANDIDATE:** GRH — that the minimal-coupling A_μ corresponds to a specific Case-P rule-type. Probably resolves at Arc Q.
- **NOT FORCED:** That ED has any specific rule-type forced to have gauge-invariant L3.

---

## 5. Are MR-R and MR-P distinct, exhaustive, or overlapping?

### 5.1 Distinctness

MR-R and MR-P operate on different statistics classes:
- MR-R: Case R (η = −1, half-integer spin).
- MR-P: Case P (η = +1, integer spin).

They cannot apply to the same rule-type. They are mutually exclusive realisations of σ_τ = 0.

### 5.2 Exhaustiveness

Are there other primitive-level routes to σ_τ = 0 besides MR-R and MR-P?

A third candidate: **MR-Λ (lightlike-only worldline).** A rule-type whose worldline is structurally lightlike has no rest frame, so the rest-frame commitment rate w^com is undefined / vanishes by default, and condition (Mλ) is satisfied trivially.

MR-Λ is closely related to but logically distinct from MR-R and MR-P:
- MR-R is a chirality condition on the spinor module.
- MR-P is a gauge condition on the integer-spin module.
- MR-Λ is a worldline-geometry condition on Primitive 02.

In the Standard Model, photons (massless) satisfy both MR-P (gauge) and MR-Λ (lightlike); these are not independent — gauge invariance forces lightlike propagation for the massless excitation. So MR-P ⇒ MR-Λ for gauge bosons. Similarly for chiral fermions, MR-R ⇒ MR-Λ in flat spacetime.

**Tentative claim (CANDIDATE):** MR-Λ is implied by either MR-R or MR-P; the three conditions are not independent. Exhaustiveness of {MR-R, MR-P} as primitive-level massless mechanisms is conjectural but plausible.

### 5.3 Overlap and rule-type assignment

A given rule-type belongs to either Case P or Case R, not both. Therefore at most one of MR-R or MR-P applies per rule-type. The two mechanisms partition the massless rule-type space:

- Massless Case-R rule-types: massless via MR-R (chirality).
- Massless Case-P rule-types: massless via MR-P (gauge).

This is consistent with Standard-Model phenomenology: massless fermion candidates (Weyl neutrinos, hypothetical) are chiral; massless gauge bosons (photon, gluon) are gauge-protected.

---

## 6. Does ED structurally force a massless class to be **occupied**?

### 6.1 Statement of the question

A massless **class** is structurally available (§3, §4 establish admissibility). The further question is whether ED primitives force at least one rule-type to **occupy** that class.

This is the question (Q-M.3) flagged in `chain_mass_scoping.md`: are massless rule-types structurally forced for specific classes?

### 6.2 Argument for occupation: minimal-coupling forces a gauge rule-type

The minimal-coupling derivation in `kg_minimal_coupling_and_current.md` established that local-phase-invariance of the participation measure forces the existence of a gauge connection A_μ. If this connection is treated as a participation measure (GRH), then ED primitives force the existence of a gauge-Case-P rule-type, which is automatically massless via MR-P.

**Conditional FORCED:** Under GRH, ED structurally requires at least one massless Case-P rule-type — the gauge-mediator of the U(1) phase invariance.

Without GRH, the gauge connection is a structural artefact (a Christoffel-like object) without a rule-type identity; ED has no forced massless rule-type.

### 6.3 Argument against occupation: chirality is rule-type data

For Case-R, single-chirality is admissible but not forced. ED primitives admit both single-chirality and full-Dirac assignments; nothing in Primitives 02–13 picks single-chirality as the structural canonical case. So MR-R does not force any massless Case-R rule-type.

### 6.4 Tentative verdict on occupation

- **Massless Case-R rule-types: NOT structurally forced.** Admissible, occupant if rule-type data assigns single-chirality, but no primitive forces such assignment.
- **Massless Case-P rule-types: FORCED conditional on GRH.** The gauge connection from minimal coupling is forced; whether it counts as a rule-type with σ_τ = 0 is the GRH question.

If GRH closes affirmatively at Arc Q, then ED structurally forces the existence of a massless Case-P (gauge) rule-type — paralleling the photon. This would be ED's first structural prediction of a specific rule-type's mass: zero.

---

## 7. Can ED identify which rule-types are massless?

### 7.1 The identification question

Even if ED forces the existence of a massless class (§6.4), can it identify **which** ED rule-types occupy it? E.g., is there a structural feature distinguishing the photon-rule-type from the electron-rule-type other than empirical assignment?

### 7.2 Available structural distinctions

From R.2 taxonomy:
- (j_L, j_R) representation: rule-type data.
- Statistics class P/R: rule-type data.
- L1 bandwidth partition: rule-type data.
- L3 Fierz / interface class: rule-type data.

All of these are inputs, not derivations. ED's primitives do not pick a specific rule-type as "this is the photon" or "this is the electron"; they specify the **space** of admissible rule-types, and empirical data fills in occupancy.

### 7.3 Verdict

**ED cannot identify which rule-types are massless beyond the level of class membership.** Specifically:
- Whether the massless Case-P class is occupied by photon-, gluon-, graviton-, or Higgs-like rule-types is an Arc Q + empirical question.
- Whether any specific Case-R rule-type is single-chirality is empirical (informed by neutrino-physics data).

This is the honest closure: ED forces the **existence** of a massless slot (under GRH); occupancy and identity are empirical.

---

## 8. FORCED / CANDIDATE / SPECULATIVE

### 8.1 FORCED

- **F1.** σ_τ = 0 is structurally accessible (admissible solution of M.1.1's master formula). (§2.1)
- **F2.** MR-R (chiral) is a structurally available mechanism for Case-R rule-types. (§3)
- **F3.** MR-P (gauge) is a structurally available mechanism for Case-P rule-types. (§4)
- **F4.** MR-R and MR-P are mutually exclusive per rule-type. (§5.1)
- **F5.** Spin alone does not force masslessness; statistics alone does not force masslessness. (§5.3)
- **F6.** ED cannot identify which rule-types are massless beyond class membership. (§7.3)

### 8.2 FORCED conditional on CANDIDATE GRH

- **F-GRH-1.** ED structurally requires the existence of at least one massless Case-P rule-type — the gauge-mediator of local-phase invariance.
- **F-GRH-2.** This rule-type is massless via MR-P (gauge route).

### 8.3 CANDIDATE

- **GRH (Gauge-field-as-Rule-Type Hypothesis).** The minimal-coupling connection A_μ is the participation measure of a specific Case-P rule-type with (1/2, 1/2) representation and gauge-invariant L3 interface. (§4.3)
- **Mλ from M.1.1.** σ_τ = 0 ⟺ no rest-frame commitment AND no rest-frame internal evolution. Now refined: equivalent to MR-R or MR-P (or MR-Λ via either implication).
- **Exhaustiveness of {MR-R, MR-P}** as primitive-level massless mechanisms in 3+1D. (§5.2)
- **MR-Λ implied by MR-R / MR-P:** worldline lightlike-ness is a consequence of one of the two structural mechanisms, not an independent third route.

### 8.4 SPECULATIVE

- **S1.** Specific empirical identification of ED's massless rule-types with photon / gluon / graviton / Weyl neutrino species — Arc Q + empirical.
- **S2.** Existence of a graviton-like rule-type at all in ED's primitive structure (graviton is currently outside ED's Phase-2 scope; the kinematic-curvature programme `project_ed10_geometry_qft_scope.md` did not produce one).
- **S3.** Whether neutrino mass smallness reflects a near-MR-R structure (small Majorana sector, dominant single-chirality content) or is fully empirical.
- **S4.** Whether the Higgs mechanism has an ED-primitive analogue — Arc Q.

### 8.5 NOT FORCED (negative results)

- **N1.** No specific ED rule-type is structurally forced to be massless on the basis of primitives 02, 04, 06, 07, 10, 11, 13 alone (without GRH).
- **N2.** ED does not pick MR-R over MR-P (or vice versa) as the canonical massless route; both are admissible.
- **N3.** ED does not predict the **count** of massless rule-types; only the existence of the slot.

---

## 9. Verdict on Arc M's predictive scope (re: masslessness)

### 9.1 (a) Existence of massless species

**Verdict: FORCED conditional on GRH; otherwise NOT FORCED.**

Under GRH (which is the natural Arc Q closure of the gauge-field/rule-type identification), ED structurally requires at least one massless Case-P rule-type. Without GRH, ED admits massless rule-types but does not force them to exist.

### 9.2 (b) Which rule-types are massless

**Verdict: NOT FORCED.** ED's primitives partition rule-type space into classes (P/R, spin, Fierz, etc.) but do not pick out specific occupants. Identification of "the photon-rule-type", "the gluon-rule-type", etc., is empirical / Arc Q content.

### 9.3 (c) Massless route (chiral vs. gauge)

**Verdict: PARTIALLY FORCED.** Within Case R, masslessness goes via MR-R; within Case P, via MR-P. Neither route is canonical for ED as a whole; the rule-type's statistics class determines which route applies.

### 9.4 Bottom line for Arc M

Arc M's structural prediction re: masslessness is:

- **Existence of a massless slot:** likely FORCED (conditional on GRH).
- **Identification of occupants:** NOT FORCED.
- **Mechanism per occupant:** PARTIALLY FORCED (statistics-class-determined).

This is a genuine but limited structural prediction. ED *predicts* that massless rule-types exist (under GRH); it *does not predict* what they are or how many; it *does predict* which mechanism produces masslessness once the rule-type's statistics class is known.

---

## 10. Hand-off

### 10.1 To Stage M.1.3

`mass_ratio_constraints.md` will evaluate whether structural mass-ratio constraints exist for the **massive** rule-types (those not in the massless slot). The massless analysis is largely complete here; M.1.3 focuses on rule-types with σ_τ > 0.

### 10.2 To Stage M.1.4

`mass_signature_identity.md` (contingent) will evaluate the m_τ = σ_τ / c² identity for massive rule-types using the M.1.1 master formula. Massless cases are trivial there: σ_τ = 0 ⇒ m_τ = 0 trivially.

### 10.3 To Arc Q

GRH closure is naturally Arc Q content. If GRH closes affirmatively, F-GRH-1 and F-GRH-2 promote to unconditional FORCED, and Arc M can claim ED structurally requires the existence of the gauge-massless slot.

---

## 11. Cross-references

- Upstream: `bandwidth_signature_construction.md` (M.1.1), `chain_mass_scoping.md` (M.0), `kg_minimal_coupling_and_current.md` (R.1), `dirac_emergence.md` (R.3), `rule_type_taxonomy_synthesis.md` (R.2.5).
- Phase-1: `qm_emergence_closure.md`.
- Downstream: `mass_ratio_constraints.md` (M.1.3), `mass_signature_identity.md` (M.1.4), `chain_mass_synthesis.md` (M.2), Arc Q scoping (forthcoming).

---

## 12. One-line summary

**Stage M.1.2 establishes that ED primitives admit two structurally distinct massless mechanisms — MR-R chirality (Case R) and MR-P gauge (Case P) — both FORCED as available routes; the existence of a massless slot is FORCED conditional on the gauge-field-as-rule-type hypothesis (GRH); but no specific ED rule-type is structurally forced to occupy the massless class without GRH, and identification of empirical massless species (photon, gluon, Weyl neutrino) remains rule-type data inherited from Arc Q + empirics, not primitive-level prediction.**
