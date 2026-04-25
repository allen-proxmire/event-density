# Interaction Vertex Classification

**Stage Q.3 — Arc Q Sub-Memo**
**Status:** Classification + partial-derivation memo. Headline verdict: **U(1) trilinear vertex Ψ̄γ^μΨ A_μ FORCED at primitive level; full Fierz vertex basis enumerated and Lorentz-admissibility per channel established; non-Abelian commutator self-coupling A^a × A^b → F^{abc}A^c FORCED CONDITIONAL on non-Abelian gauge rule-type existence; refinement R-3 (vertex-anchored commitment) CLOSED structurally via commitment-locality argument; R-4 (non-Abelian extension) FULLY CLOSED — gauge-covariant derivative D_μ = ∂_μ + ig A^a_μ T^a structurally forced once SU(N) gauge rule-type admitted. Specific coupling values, gauge-group representation assignments, and Yukawa-like structures remain INHERITED.**

---

## 1. Goal

Stages Q.1 + Q.2 closed GRH structure (CANDIDATE-STRONG) and gauge-group admissibility (U(1) FORCED, SU(N) CANDIDATE-admissible). Five GRH refinements remained outstanding: R-1, R-2 closed at Q.2, R-3 partial, R-4 partial, R-5 deferred to Q.7/Q.8.

Stage Q.3 attacks the two refinements still requiring closure:

- **R-3 (vertex-anchored commitment for τ_g):** how commitment events along the gauge rule-type's worldline are sourced at interaction vertices with charged matter, given the gauge worldline is lightlike.
- **R-4 (non-Abelian extension):** completing the partial Q.2 closure by deriving the gauge-covariant derivative D_μ = ∂_μ + ig A^a_μ T^a structurally for any admitted SU(N) gauge rule-type.

The deliverable is a **classification of all admissible interaction vertices** between matter rule-types (Case P or Case R) and gauge rule-types (Case P, (1/2, 1/2), gauge-invariant L3 per GRH). The classification uses the Fierz basis from R.2.4 §5.1 and produces a per-vertex FORCED / CANDIDATE / REFUTED status.

---

## 2. Inputs

### 2.1 From Stage Q.1 (GRH)

- τ_g is Case P, (1/2, 1/2), gauge-invariant L3, σ = 0 via MR-P.
- GRH = CANDIDATE-STRONG modulo refinements R-1, R-3, R-5.

### 2.2 From Stage Q.2 (gauge-group scoping)

- U(1) FORCED at R.1.
- SU(N) for any finite N CANDIDATE-admissible structurally.
- Gauge-quotient individuation (R-2) CLOSED via adjacency-equivalence-class construction.
- R-4 partially closed (admissibility established; full minimal-coupling extension deferred here).

### 2.3 From Stage R.2.4

- Cl(3,1) frame {γ^μ, γ^ν} = 2η^{μν}.
- 16-dimensional Fierz basis: {𝟙, γ^μ, σ^{μν}, γ^μγ^5, γ^5}.
- Bilinear types: scalar, vector, antisymmetric tensor, axial vector, pseudoscalar.

### 2.4 From Stages R.1, R.3 (minimal coupling)

- U(1) gauge-covariant derivative D_μ = ∂_μ + (iq/ℏ)A_μ from local-phase invariance.
- Conserved current j^μ = Ψ̄γ^μΨ (Dirac) or KG-current (scalar) couples to A_μ.

---

## 3. Vertex anatomy

### 3.1 General trilinear vertex structure

A primitive-level interaction vertex couples:

- **Matter participation measure(s)** Ψ_τ — Case R (Dirac spinor on Cl(3,1) module) or Case P (scalar / vector / tensor).
- **Gauge participation measure(s)** A^a_μ — Case P (1/2, 1/2) carrying possible internal gauge index a.
- **L3 interface coupling** specifying which Lorentz-covariant bilinear / trilinear structure connects them.
- **Commitment dynamics** (Primitive 11) anchoring the vertex at specific event-manifold points.

The general trilinear vertex schema:

  𝒱_3 ~ Ψ̄_τ · Γ · Ψ_τ · A^a_μ · K^μ_a,                                       (1)

where Γ ∈ Cl(3,1) Fierz basis and K^μ_a is a Lorentz-vector-valued tensor in gauge index a.

### 3.2 Vertex anchoring (R-3)

Stage Q.1 §3.6 flagged that gauge rule-types have lightlike worldlines, so commitment for τ_g cannot be intrinsic-along-its-own-worldline. Primitive 11 commitment events for τ_g are **vertex-anchored** — sourced at points where τ_g participates in a vertex with a charged-matter rule-type.

**Structural consequence.** A gauge-rule-type "exists" between two vertices in a propagation sense (lightlike geodesic on the event manifold) but its commitment events are exclusively at vertices. This matches photon emission/absorption phenomenology.

### 3.3 Locality requirement

Primitive 11 commitment events are local — they occur at single event-manifold points. Therefore vertices are **point-local** in the event manifold: the matter participation Ψ̄ΓΨ and the gauge participation A^a_μ are evaluated at the same x^μ.

This rules out non-local structures (e.g., bilocal couplings Ψ̄(x)ΓΨ(y)A_μ(z)). Any admissible vertex is localised at one event.

---

## 4. Fierz classification of vertex types

### 4.1 Bilinear scalars Ψ̄ΓΨ

The 16-dim Fierz basis from R.2.4 §5.1 produces five Lorentz types of fermion bilinears:

| # | Bilinear | Lorentz type | Component count |
|---|----------|--------------|-----------------|
| 1 | Ψ̄ Ψ | scalar | 1 |
| 2 | Ψ̄ γ^μ Ψ | vector | 4 |
| 3 | Ψ̄ σ^{μν} Ψ | antisym tensor | 6 |
| 4 | Ψ̄ γ^μ γ^5 Ψ | axial vector | 4 |
| 5 | Ψ̄ γ^5 Ψ | pseudoscalar | 1 |

For a vertex coupling Ψ̄ΓΨ to A^a_μ, only structures producing a Lorentz scalar (scalar Lagrangian) are admissible. The available contractions:

| Bilinear contracted with | Lorentz-scalar combination | Status |
|--------------------------|---------------------------|--------|
| Ψ̄ Ψ × A · A | Ψ̄Ψ · A_μA^μ (mass-like) | ALLOWED but breaks gauge invariance |
| Ψ̄ γ^μ Ψ × A_μ | Ψ̄γ^μΨ · A_μ (vector current) | **STANDARD QED VERTEX** |
| Ψ̄ σ^{μν} Ψ × F_{μν} | Ψ̄σ^{μν}Ψ · F_{μν} (Pauli moment) | ADMISSIBLE; non-renormalisable |
| Ψ̄ γ^μ γ^5 Ψ × A_μ | Ψ̄γ^μγ^5Ψ · A_μ (axial current) | ADMISSIBLE (chiral coupling) |
| Ψ̄ γ^5 Ψ × ∂_μ A^μ | Ψ̄γ^5Ψ · ∂·A | ADMISSIBLE; vanishes on Lorenz gauge |

### 4.2 Vertex types per channel

#### 4.2.1 Vector vertex (Ψ̄γ^μΨ A_μ)

The standard QED-analogue vertex. **FORCED at primitive level** for U(1) coupling: this is the vertex produced by minimal coupling in the Dirac equation (Stage R.3), via D_μ = ∂_μ + (iq/ℏ)A_μ.

**Status:** **FORCED.** Vector vertex is the primitive-level realisation of U(1) gauge coupling for charged Dirac matter.

#### 4.2.2 Scalar vertex (Ψ̄Ψ × A·A)

Couples scalar bilinear to a gauge-scalar built from A_μA^μ. Such a term is gauge-non-invariant under A_μ → A_μ + ∂_μα (A_μA^μ is not gauge-invariant). It would correspond to a Stueckelberg-style or Higgs-VEV mass term.

**Status:** **REFUTED at primitive level for unbroken gauge symmetry.** This vertex breaks GRH-3. Admissible only if gauge symmetry is broken (Higgs SSB, Q.4 content).

#### 4.2.3 Tensor vertex (Ψ̄σ^{μν}Ψ F_{μν})

Pauli-moment-like coupling. F_{μν} = ∂_μA_ν − ∂_νA_μ is gauge-invariant; σ^{μν} bilinear is Lorentz-invariant when contracted with F_{μν}. The full structure is gauge-invariant.

**Status:** **ADMISSIBLE.** Not forced by minimal coupling (which produces vector vertex only) but admissible at primitive level. In QFT this is a non-renormalisable dimension-5 operator generating anomalous magnetic moments. ED admits it structurally; whether it appears at lowest order or only as effective-theory coupling is rule-type / empirical data.

#### 4.2.4 Axial-vector vertex (Ψ̄γ^μγ^5Ψ A_μ)

Chiral coupling. Structurally admissible as a Lorentz-scalar combination. In the SM, axial-vector couplings appear in weak interactions (V−A structure of charged-current vertices).

**Status:** **ADMISSIBLE.** Specific Case-R rule-types may have axial coupling at L3 instead of (or in addition to) vector coupling. Choice is rule-type data.

#### 4.2.5 Pseudoscalar vertex

Ψ̄γ^5Ψ contracted with a pseudoscalar built from gauge fields (e.g., ∂_μA^μ on Lorenz gauge, or *F·F dual structure). Admissible structurally.

**Status:** **ADMISSIBLE.** Relevant for axion-like couplings; appears in SM as anomaly contribution.

### 4.3 Gauge-invariance filter

Of the five vertex types in §4.2, those compatible with **unbroken gauge invariance** (GRH-3) are:

- **Vector vertex Ψ̄γ^μΨ A_μ:** gauge-invariant when combined with the matter kinetic term (provides the divergence cancellation).
- **Tensor vertex Ψ̄σ^{μν}Ψ F_{μν}:** built from gauge-invariant F_{μν}.
- **Axial-vector vertex Ψ̄γ^μγ^5Ψ A_μ:** gauge-invariant by same argument as vector.
- **Pseudoscalar coupling to *F·F:** gauge-invariant.

Forbidden under unbroken gauge:
- **Ψ̄Ψ A_μA^μ** (gauge-non-invariant mass-like term).

### 4.4 Vertex classification summary

| Vertex | Lorentz status | Gauge status | Primitive admissibility |
|--------|---------------|--------------|------------------------|
| Ψ̄γ^μΨ A_μ (vector) | scalar | invariant | **FORCED** (R.1/R.3 minimal coupling) |
| Ψ̄γ^μγ^5Ψ A_μ (axial) | scalar | invariant | **ADMISSIBLE** (rule-type data) |
| Ψ̄σ^{μν}Ψ F_{μν} (tensor/Pauli) | scalar | invariant | **ADMISSIBLE** (effective only) |
| Ψ̄γ^5Ψ · pseudoscalar(A) | scalar | invariant | **ADMISSIBLE** (axion-like) |
| Ψ̄Ψ · A·A (mass-like) | scalar | NOT invariant | **REFUTED under unbroken gauge** |

---

## 5. Minimal-coupling derivation: U(1) and SU(N)

### 5.1 U(1) recap

For Dirac matter Ψ with U(1) charge q, local-phase invariance Ψ → e^{iqα(x)/ℏ}Ψ forces the connection A_μ to transform as A_μ → A_μ − ∂_μα, and the covariant derivative

  D_μ Ψ = (∂_μ + (iq/ℏ) A_μ) Ψ                                                (2)

transforms covariantly: D_μΨ → e^{iqα/ℏ} D_μΨ. Substituting D_μ for ∂_μ in the Dirac kinetic term gives

  Ψ̄ iℏγ^μ D_μ Ψ = Ψ̄ iℏγ^μ ∂_μ Ψ − q Ψ̄γ^μ Ψ A_μ,                              (3)

and the second term is the FORCED vector vertex.

### 5.2 SU(N) extension — local-phase generalisation

For a charged matter rule-type carrying an SU(N) representation, the participation measure has an additional internal index: Ψ^i_K (i = 1, …, dim(R)) for representation R. Local SU(N) invariance is

  Ψ^i(x) → U^i_j(x) Ψ^j(x),     U(x) = exp(iα^a(x) T^a) ∈ SU(N),               (4)

where T^a are the generators in representation R.

The gauge-covariant derivative must satisfy D_μΨ → U(x) · D_μΨ. The form

  **D_μ Ψ = (∂_μ + ig A^a_μ T^a) Ψ**                                          (5)

works iff A^a_μ transforms as

  A^a_μ → A^a_μ + (1/g) ∂_μα^a − f^{abc} α^b A^c_μ.                            (6)

The non-Abelian inhomogeneous term −f^{abc}α^b A^c_μ is the new structural content — it ensures D_μ remains gauge-covariant when the gauge transformation does not commute.

### 5.3 R-4 closure: is (5) FORCED?

**Argument:** Given GRH (gauge field is a participation rule-type) + GRH-3 (L3 enforces gauge invariance) + a charged matter rule-type carrying SU(N) representation R, the unique linear connection making D_μΨ transform covariantly under (4) is exactly (5) with T^a in representation R, and the gauge-field transformation (6) is unique (up to overall sign convention).

This is a structural theorem — no additional freedom exists once the SU(N) gauge structure is admitted and matter carries representation R.

**FORCED conditional:** D_μ = ∂_μ + ig A^a_μ T^a is the unique structural realisation of SU(N) gauge coupling **conditional on**:
- SU(N) gauge rule-type τ_g^a being admitted at primitive level (Q.2 admissibility).
- Charged matter rule-type τ_q carrying SU(N) representation R existing at primitive level (rule-type empirical data).

Conditional on these two existence claims, (5) is FORCED. **R-4 is fully closed at primitive level**: ED's structural framework forces the unique non-Abelian minimal-coupling structure once non-Abelian content is admitted.

### 5.4 Non-Abelian commutator self-interaction

Equation (6) implies the gauge field strength

  F^a_{μν} = ∂_μ A^a_ν − ∂_ν A^a_μ + g f^{abc} A^b_μ A^c_ν                     (7)

contains the **non-linear commutator term** g f^{abc} A^b_μ A^c_ν. This term produces:

- **Three-gauge-boson vertex** AAA from F^a_{μν} F^{a μν} expansion.
- **Four-gauge-boson vertex** AAAA from the same expansion.

These are the gluon self-interactions of QCD-analogue, and the W-W-Z, W-W-γ vertices of EW-analogue. **They are FORCED** by gauge invariance once the non-Abelian gauge group is admitted — there is no consistent SU(N) gauge theory without them.

**Structural status:** The non-Abelian self-coupling structure F^{abc} A^b A^c ⊂ F^a_{μν} is **FORCED-conditional** on SU(N) admittance. This is a primitive-level theorem.

---

## 6. Refinement R-3 closure (vertex-anchored commitment)

### 6.1 The construction

Stage Q.1 §3.6 identified that gauge rule-types' commitment events (Primitive 11) cannot be intrinsic-along-worldline (lightlike worldlines have no proper-time intervals). Vertices supply the structural anchor.

**Definition (vertex-anchored commitment for τ_g):** Each commitment event of τ_g occurs at an interaction vertex with at least one charged-matter rule-type. Between vertices, τ_g propagates lightlike with no commitment events; commitment occurs precisely at vertex insertions on the event manifold.

This matches photon phenomenology: photons have no "intrinsic clock" but emit/absorb events occur at specific event-manifold points where they couple to charged matter.

### 6.2 Locality and gauge covariance

The vertex-anchored construction enforces:

- **Locality:** commitment events are point-events on the event manifold (Primitive 11).
- **Gauge covariance:** vertices are built from gauge-invariant (or gauge-covariant in matched pairs) Lorentz scalars per §4.4. The commitment statistic at a vertex is a gauge-invariant quantity.

These two properties are jointly forced by Primitives 06 + 07 + 11 once GRH is admitted.

### 6.3 Does vertex-anchoring force any specific interaction types?

R-3's secondary question: does the vertex-anchoring construction *force* specific vertex types to be present?

**Argument:** A gauge rule-type τ_g must commit *somewhere* (no rule-type is structurally allowed to never commit — this would render its participation undetectable, and Primitive 11 admits no such "ghost" rule-types). Therefore at least one vertex type must couple τ_g to some matter rule-type.

For U(1), the minimal coupling derivation at R.1 forces the vector vertex Ψ̄γ^μΨ A_μ to exist whenever charged matter exists. This satisfies the "must commit somewhere" constraint structurally.

For SU(N), the analogous minimal-coupling structure forces the corresponding non-Abelian vector vertex iff charged matter in non-trivial representation exists.

**R-3 closure summary:** Vertex-anchored commitment for τ_g is structurally FORCED (the construction is admissible at primitive level and necessary for τ_g to participate in commitment dynamics at all). The specific vertex type that anchors τ_g's commitment is forced for U(1) (vector vertex) and conditionally forced for SU(N).

**R-3: CLOSED** structurally.

---

## 7. Vertex-type FORCED / CANDIDATE / REFUTED table

### 7.1 Per channel

| Vertex | U(1) status | SU(N) status |
|--------|------------|--------------|
| Vector Ψ̄γ^μΨ A_μ (or Ψ̄γ^μT^aΨ A^a_μ) | **FORCED** (R.1/R.3) | **FORCED conditional on charged matter** |
| Axial-vector Ψ̄γ^μγ^5Ψ A_μ | **ADMISSIBLE** | **ADMISSIBLE** |
| Tensor Ψ̄σ^{μν}Ψ F_{μν} | **ADMISSIBLE** (effective) | **ADMISSIBLE** (effective) |
| Pseudoscalar Ψ̄γ^5Ψ × pseudo-A | **ADMISSIBLE** | **ADMISSIBLE** |
| Mass-like Ψ̄Ψ A·A | **REFUTED** (breaks GRH-3) | **REFUTED** (breaks GRH-3) |

### 7.2 Pure-gauge self-coupling

| Vertex | U(1) status | SU(N) status |
|--------|------------|--------------|
| AAA (three-gauge-boson) | **REFUTED** (Abelian; no f^{abc}) | **FORCED conditional on SU(N)** |
| AAAA (four-gauge-boson) | **REFUTED** (Abelian) | **FORCED conditional on SU(N)** |
| Higher-order pure-gauge | **REFUTED** (Abelian); **CANDIDATE** for non-Abelian effective | non-Abelian: only AAA, AAAA structurally; higher orders effective |

### 7.3 Mixed / multi-matter vertices

| Vertex | Status |
|--------|--------|
| Ψ̄_τ Γ Ψ_τ' A_μ (matter-flavour-changing) | **ADMISSIBLE** if τ, τ' have matching gauge representations |
| Yukawa Ψ̄_τ Γ Ψ_τ' φ (matter-Higgs) | Q.4 deliverable; ADMISSIBLE structurally |
| Multi-current 4-fermion (Ψ̄ΓΨ)(Ψ̄Γ'Ψ) | **ADMISSIBLE** as effective vertex; non-renormalisable |

### 7.4 Higher-order vertices

| Vertex order | Status |
|-------------|--------|
| 3-point | FORCED for vector U(1)/SU(N); ADMISSIBLE for tensor / axial / pseudo |
| 4-point | FORCED for AAAA non-Abelian; ADMISSIBLE for matter-multi-vertex effective |
| 5+ point | ADMISSIBLE only as effective theory; not structurally forced |

### 7.5 Forbidden structures

| Structure | Status |
|-----------|--------|
| Non-local vertex Ψ̄(x)ΓΨ(y)A(z) (x ≠ y ≠ z) | **REFUTED** (Primitive 11 locality) |
| Gauge-non-invariant ΨΨAA mass-like | **REFUTED** under unbroken gauge (GRH-3) |
| Lorentz-non-scalar combinations | **REFUTED** (Primitive 06 covariance) |
| Anyonic-statistics vertices | **REFUTED** (R.2.3 π_1 = ℤ_2) |

---

## 8. Verdict

### 8.1 What is structurally FORCED?

- **U(1) vector vertex Ψ̄γ^μΨ A_μ** — FORCED by R.1/R.3 minimal coupling whenever charged Dirac matter exists.
- **Non-Abelian gauge-covariant derivative** D_μ = ∂_μ + ig A^a_μ T^a — FORCED conditional on SU(N) admittance + non-trivial-representation matter.
- **Non-Abelian self-interaction** F^a_{μν} containing g f^{abc} A^b A^c — FORCED conditional on SU(N) admittance.
- **Vertex-anchored commitment** for gauge rule-types — FORCED structurally.
- **Vertex locality** — FORCED by Primitive 11.
- **Lorentz-scalar Lagrangian** — FORCED by Primitive 06.
- **Gauge-invariant vertices** for unbroken gauge — FORCED by GRH-3.

### 8.2 What is admissible but not forced?

- Axial-vector, tensor (Pauli-moment), pseudoscalar vertices — ADMISSIBLE per Fierz basis; specific occupancy is rule-type / L3-data.
- Effective higher-order (5+ point) vertices — ADMISSIBLE as low-energy effective theory; not structurally fundamental.
- Yukawa vertices — ADMISSIBLE (Q.4 detailed).
- Mixed-flavour vertices — ADMISSIBLE if gauge representations match.

### 8.3 What is forbidden?

- Gauge-non-invariant mass-like vertex Ψ̄ΨA·A under unbroken gauge.
- Non-local vertices.
- Lorentz-non-scalar combinations.
- Anyonic vertices.
- Non-Abelian self-coupling for U(1) (Abelian f^{abc} = 0 trivially).

### 8.4 What remains inherited?

- **Specific gauge-group representation assignments per matter rule-type** (which τ_q carries SU(3)-fundamental, SU(2)-doublet, etc.).
- **Numerical coupling constants** g, q, g_s, g_w.
- **Specific Yukawa coupling values and matrices** (Q.4 content).
- **Choice of axial vs vector dominance** at L3 per matter rule-type.
- **Effective-theory operator coefficients** (anomalous magnetic moments, etc.).

### 8.5 Refinement closures

| Refinement | Pre-Q.3 status | Post-Q.3 status |
|-----------|----------------|-----------------|
| R-1 (lightlike-worldline) | open | open (Q.7) |
| R-2 (gauge-quotient individuation) | closed at Q.2 | closed (Q.2) |
| **R-3 (vertex-anchored commitment)** | partial | **CLOSED** (this memo, §6) |
| **R-4 (non-Abelian extension)** | partial (Q.2) | **CLOSED** (this memo, §5) |
| R-5 (vacuum/particle status) | open | open (Q.7/Q.8) |

**Two of five GRH refinements remain open: R-1 and R-5.** Both are Q.7 / Q.8 deliverables (second quantisation + vacuum structure). After Q.7/Q.8 close, GRH should be promotable to unconditional FORCED.

---

## 9. Implications for downstream substages

### 9.1 To Q.4 (Higgs-like SSB)

Q.3 establishes that **mass-like vertex Ψ̄ΨA·A is REFUTED under unbroken gauge** but is the natural target of Higgs-like SSB. Q.4 will evaluate whether ED admits an SSB mechanism that:
- Produces an effective mass term for non-Abelian gauge bosons.
- Produces Yukawa-like fermion mass generation.
- Has a primitive-level analogue or is fully empirical.

Q.4 inherits from Q.3 the vertex catalogue and the gauge-invariance filter.

### 9.2 To Q.5 (radiative corrections)

Q.5 will compute one-loop corrections using the vertex types FORCED here. The vector vertex sets the leading-order QED-analogue diagrams (g − 2 from one-loop vertex correction); non-Abelian self-couplings produce non-Abelian RG flow (asymptotic freedom for SU(3)).

Q.5's structural framework is supplied by Q.3 + Q.7 second quantisation.

### 9.3 Back-flow to Arc M

GRH refinements R-3 and R-4 closure does not yet promote F-M8 to unconditional FORCED — R-1 and R-5 remain. Q.7/Q.8 closure will complete the chain.

### 9.4 To Arc Q synthesis

After Q.4–Q.8, the synthesis will integrate:
- Q.1 GRH structure.
- Q.2 gauge group admissibility.
- Q.3 vertex classification (this memo).
- Q.4 SSB / Higgs.
- Q.5 radiative corrections.
- Q.6 generations / flavour.
- Q.7 second quantisation.
- Q.8 vacuum.

Q.3's vertex catalogue is one of the foundational layers entering the synthesis.

---

## 10. FORCED / CANDIDATE / REFUTED summary

### 10.1 FORCED

- **F-Q3.1.** Vector vertex Ψ̄γ^μΨ A_μ for U(1) (R.1/R.3 minimal coupling).
- **F-Q3.2.** Non-Abelian D_μ = ∂_μ + ig A^a_μ T^a structure (R-4 closure, conditional on SU(N) admittance + charged matter).
- **F-Q3.3.** Non-Abelian self-coupling AAA + AAAA from f^{abc} structure constants.
- **F-Q3.4.** Vertex-anchored commitment for τ_g (R-3 closure).
- **F-Q3.5.** Vertex locality from Primitive 11.
- **F-Q3.6.** Lorentz-scalar Lagrangian from Primitive 06.
- **F-Q3.7.** Gauge-invariance filter on admissible vertices from GRH-3.
- **F-Q3.8.** No-anyon constraint from R.2.3.

### 10.2 CANDIDATE

- **C-Q3.1.** Tensor (Pauli-moment) vertex Ψ̄σ^{μν}Ψ F_{μν} as primitive-fundamental rather than effective. Plausible at primitive level; not forced.
- **C-Q3.2.** Axial-vector dominance for specific Case-R rule-types (e.g., V−A weak coupling). Rule-type data; structurally admissible.
- **C-Q3.3.** Pseudoscalar (axion-like) coupling for specific rule-types.

### 10.3 REFUTED

- **R-Q3.1.** Mass-like vertex Ψ̄ΨA·A under unbroken gauge symmetry.
- **R-Q3.2.** Non-local vertices.
- **R-Q3.3.** Lorentz-non-scalar vertex structures.
- **R-Q3.4.** Anyonic-statistics vertex structures.
- **R-Q3.5.** Pure-gauge self-coupling for U(1) (trivial; no non-Abelian content).

### 10.4 INHERITED

- **I-Q3.1.** Specific gauge-group representation assignments per matter rule-type.
- **I-Q3.2.** Numerical coupling constants.
- **I-Q3.3.** Specific axial / vector / tensor / pseudoscalar dominance per rule-type.
- **I-Q3.4.** Yukawa matrix values (Q.4 detail).
- **I-Q3.5.** Effective-theory operator coefficients.

---

## 11. Cross-references

- Upstream: `gauge_group_scoping.md` (Q.2), `grh_evaluation.md` (Q.1), `qft_extension_scoping.md` (Q.0), `dirac_emergence.md` (R.3), `kg_minimal_coupling_and_current.md` (R.1), `clifford_algebra_from_spinor_structure.md` (R.2.4).
- Downstream placeholders: `higgs_mechanism_scoping.md` (Q.4 — uses §4.4 mass-like-REFUTED for SSB target), `radiative_corrections.md` (Q.5 — uses Q.3 vertex catalogue), `second_quantisation.md` (Q.7 — closes R-1, R-5), `vacuum_and_zero_point.md` (Q.8 — closes R-5).
- Refinement tracking: R-1 open (Q.7); R-2 closed (Q.2); R-3 **CLOSED** (this memo); R-4 **CLOSED** (this memo); R-5 open (Q.7/Q.8).

---

## 12. One-line summary

**Stage Q.3 classifies admissible interaction vertices via the Cl(3,1) Fierz basis and shows that the U(1) vector vertex Ψ̄γ^μΨ A_μ is FORCED at primitive level via R.1/R.3 minimal coupling, the non-Abelian gauge-covariant derivative D_μ = ∂_μ + ig A^a_μ T^a and self-coupling F^{abc}A^b A^c are FORCED conditional on SU(N) admittance + charged matter (closing R-4 fully), vertex-anchored commitment for gauge rule-types is FORCED structurally (closing R-3), gauge-non-invariant mass-like Ψ̄ΨA·A vertices are REFUTED under unbroken gauge (becoming Q.4's Higgs-SSB target), tensor / axial / pseudoscalar vertices are ADMISSIBLE-per-rule-type, all specific coupling values and gauge-representation assignments remain INHERITED — leaving R-1 (lightlike worldline) and R-5 (vacuum status) as the two remaining GRH refinements for Q.7 / Q.8 to close before GRH promotes to unconditional FORCED.**
