# Lorentz Representations from Primitives

**Stage R.2.2 — Rule-Type Taxonomy Sub-Program**
**Status:** Partial derivation memo. Integer-representation content FORCED modulo Stage R.1 scope. Half-integer content CANDIDATE pending Stage R.2.3 (rotational double-cover). Spin-value assignment structurally FORCED via Casimir labelling; numerical spin quantum number inherited (not derived here).

---

## 1. Goal of Stage R.2.2

Derive from Primitives 02, 06, and 13 — together with the Stage R.1 Lorentz-covariant participation measure and the Stage R.2.1 exchange-symmetry dichotomy — the allowed Lorentz-group representation content of participation measures.

Specifically:

(a) Show that the transformation law of a participation measure under the Lorentz group is a **representation** of that group on the internal index space.

(b) Show that the representation must be **finite-dimensional and non-unitary on internal indices** (or unitary on the infinite-dimensional field Hilbert space, but finite on internal indices) — the standard "spin" representations.

(c) Classify the representations by Casimir invariants into (j_L, j_R) labels with j_L, j_R ∈ {0, 1/2, 1, 3/2, …}.

(d) Identify why half-integer representations require the double-cover SL(2, ℂ), deferring the primitive-level origin of the double-cover itself to Stage R.2.3.

(e) Connect the representation-content split to the Stage R.2.1 exchange-symmetry dichotomy: Case P ↔ integer-spin, Case R ↔ half-integer-spin (connection FORCED only after Stage R.2.3 closes).

This memo does **not** derive:
- The specific minus-sign origin of half-integer behaviour (→ Stage R.2.3).
- The spin-statistics theorem as a primitive-level equality (→ Stage R.2.5 synthesis).
- The Dirac equation (→ Stage R.3).

---

## 2. Primitive-level inputs

### 2.1 Primitive 02 — Worldline structure

Each chain K carries a worldline γ_K: τ ↦ x^μ(τ) parametrised by proper time τ (via Primitive 13). Participation events are localised on or near γ_K; the participation measure P_K(x^μ) is defined on the ambient 3+1D event manifold and is non-trivial in a neighbourhood of γ_K.

### 2.2 Primitive 06 — Four-gradient and Lorentz covariance

Updates are expressed in terms of four-gradients ∂_μ acting on P_K, and the dynamical content is Lorentz-covariant: for every Λ ∈ SO⁺(3,1) (proper orthochronous), the update rule transforms covariantly under x^μ → Λ^μ_ν x^ν. This is the Stage R.1 structural input.

### 2.3 Primitive 13 — Proper-time relational timing

Proper time τ_K along γ_K is the invariant relational clock; Lorentz boosts do not change τ_K-intervals. Combined with Primitive 06, this promotes SO⁺(3,1) from a convenience to a **structural symmetry** of the update law.

### 2.4 Stage R.1 input — Scalar participation measure

Stage R.1 derived P_K(x^μ) = √(b_K(x^μ)) · e^{iπ_K(x^μ)} ∈ ℂ, a complex scalar under SO⁺(3,1). This is the **minimal** (spin-0) representation. Stage R.2.2 asks: what else is structurally permitted?

### 2.5 Stage R.2.1 input — Exchange-symmetry dichotomy

Rule-types split into two categories:
- **Case P:** symmetric joint participation, η = +1
- **Case R:** antisymmetric joint participation, η = −1

Stage R.2.1 established this dichotomy at the exchange level without yet identifying its Lorentz-representation content.

---

## 3. Derivation

### 3.1 Lorentz action on participation measures

Let P_K^a(x^μ) be a participation measure carrying an internal index a (which may be trivial, a = 1, recovering the Stage R.1 scalar). Under a Lorentz transformation Λ,

  P_K^a(x^μ) → D(Λ)^a_b · P_K^b(Λ^{-1} x^μ),                                    (1)

where D(Λ) is a linear map on the internal index space. Covariance of the update law (Primitive 06) requires that D be compatible with composition:

  D(Λ_1 Λ_2) = D(Λ_1) D(Λ_2),     D(1) = 1.                                     (2)

Equation (2) is the **definition** of a linear representation of SO⁺(3,1) (or of its cover) on the internal index space. Thus the question "what internal structure can a participation measure carry?" reduces to "what representations of the Lorentz group are structurally admissible?"

### 3.2 Why the representation must be finite-dimensional on internal indices

The internal index a labels discrete structural channels of the rule-type (Primitive 07 §7.4): band partitions, adjacency sub-channels, exchange-symmetry categories. These are all finite in count at the primitive level — the rule-type taxonomy is a discrete classification. Therefore the internal index space is finite-dimensional, and D(Λ) is a finite-dimensional representation.

(Unitarity is **not** required of D on internal indices: unitarity applies to the full field Hilbert space inner product, which for non-compact SO⁺(3,1) cannot be finite-dimensional and unitary simultaneously. This is a standard Lorentz-representation fact; ED inherits it because the internal-index space is finite.)

### 3.3 Representation content from transformation properties

The finite-dimensional representations of the (complexified) Lorentz Lie algebra so(3,1)_ℂ ≅ su(2)_ℂ ⊕ su(2)_ℂ are labelled by pairs

  (j_L, j_R),     j_L, j_R ∈ {0, 1/2, 1, 3/2, …},                                (3)

with dimension (2j_L + 1)(2j_R + 1). This is a theorem of Lie algebra theory, not a separate postulate. Given that the primitive-level admissible representations are exactly the finite-dimensional ones (§3.2), the classification (3) is FORCED.

The low-lying cases relevant to ED:

| (j_L, j_R) | Dimension | Physical name                  |
|------------|-----------|--------------------------------|
| (0, 0)     | 1         | scalar                         |
| (1/2, 0)   | 2         | left-handed Weyl spinor        |
| (0, 1/2)   | 2         | right-handed Weyl spinor       |
| (1/2, 1/2) | 4         | four-vector                    |
| (1, 0)     | 3         | self-dual rank-2 antisym tens. |
| (0, 1)     | 3         | anti-self-dual                 |
| (1, 1/2) ⊕ (1/2, 1) | 8| Rarita-Schwinger (spin-3/2)    |
| (1, 1)     | 9         | symmetric traceless rank-2     |

### 3.4 Integer vs. half-integer: the double-cover

The group SO⁺(3,1) has fundamental group ℤ_2. Its universal cover is SL(2, ℂ), which is a double cover: two elements of SL(2, ℂ) project onto each element of SO⁺(3,1).

A representation D of SL(2, ℂ) descends to a representation of SO⁺(3,1) iff D(−1) = +1 on the internal index space. The (j_L, j_R) representation has D(−1) = (−1)^{2(j_L + j_R)}, so:

- **Integer j_L + j_R** (scalar, vector, rank-2 tensor, …): D descends to SO⁺(3,1). These are "true" Lorentz representations.
- **Half-integer j_L + j_R** (Weyl, Dirac, Rarita-Schwinger, …): D does **not** descend. These are representations of SL(2, ℂ) only.

**Stage R.2.2 closure point.** The question "is SL(2, ℂ) structurally admissible, or must ED restrict to SO⁺(3,1)?" is the content of Stage R.2.3 (rotational double-cover). In this memo we record:

(S) If SL(2, ℂ) is the admissible covariance group, all (j_L, j_R) with j_L, j_R ∈ {0, 1/2, 1, …} are structurally permitted.

(O) If only SO⁺(3,1) is admissible, half-integer representations are structurally forbidden.

The empirical existence of fermions forces (S) phenomenologically; the primitive-level derivation of (S) is Stage R.2.3's job.

### 3.5 Why only these representations in 3+1D

The classification (3) is exhaustive for finite-dimensional representations of so(3,1)_ℂ. There is no room for "exotic" finite-dimensional representations — this is a rigidity theorem of semisimple Lie algebras. The primitive-level input that fixes this is dimension 3+1 and the Lorentz signature (−, +, +, +), both of which are inherited from Primitives 02, 06, 13 (spatial locality + proper-time relational timing + four-gradient covariance).

In 2+1D, 4+1D, or Euclidean signature, the representation zoology is different. ED's commitment to 3+1D Lorentz signature, entering through the four-gradient structure of Primitive 06, is what forces the (j_L, j_R) ladder.

---

## 4. Spin-value assignment

### 4.1 Casimir labelling

The Pauli-Lubanski Casimir W^2 on a (j_L, j_R) representation in a massive frame evaluates to −m² s(s+1)ℏ² with

  s ∈ {|j_L − j_R|, |j_L − j_R| + 1, …, j_L + j_R}.                              (4)

The label s is the **spin quantum number**. Assignment:

| Representation       | Spin s             |
|----------------------|--------------------|
| (0, 0) scalar        | 0                  |
| (1/2, 0) or (0, 1/2) | 1/2                |
| (1/2, 1/2) vector    | 0 or 1 (splits)    |
| (1, 0) or (0, 1)     | 1                  |
| (1, 1/2) ⊕ (1/2, 1)  | 1/2 or 3/2 (splits)|
| (1, 1)               | 0, 1, or 2         |

For an **irreducible** covariant equation (à la Klein-Gordon, Dirac, Proca, Rarita-Schwinger), a subsidiary condition projects onto a single s. The Klein-Gordon case (Stage R.1) projects (0,0) onto s = 0; the Dirac case (Stage R.3) will project (1/2, 0) ⊕ (0, 1/2) onto s = 1/2; Proca onto (1/2, 1/2) with ∂·A = 0 projects onto s = 1.

### 4.2 Structural status of the assignment

The Casimir label s is FORCED once the (j_L, j_R) representation and Poincaré covariance are fixed. The numerical spin quantum number per particle species is **not** derived at the primitive level — it is an empirical input per rule-type, like mass. Stage R.2.2 derives the **ladder of permitted s values**, not the spin of any specific particle.

### 4.3 Why only s ∈ {0, 1/2, 1, 3/2, 2, …}

The ladder is a direct consequence of the (j_L, j_R) classification (§3.3) and the Casimir formula (4). No half-odd-half values (e.g., 1/4, 2/3) appear because su(2) representations are labelled by half-integers. This rigidity is Lie-algebraic, inherited through Primitive 06.

---

## 5. Connection to Stage R.2.1

### 5.1 Provisional map

Stage R.2.1 established two rule-type categories:
- **Case P:** η = +1, symmetric joint participation.
- **Case R:** η = −1, antisymmetric joint participation.

Stage R.2.2 establishes two representation classes:
- **Integer class:** j_L + j_R ∈ ℤ, s ∈ {0, 1, 2, …}.
- **Half-integer class:** j_L + j_R ∈ ℤ + 1/2, s ∈ {1/2, 3/2, …}.

The spin-statistics correspondence is:
  Case P ↔ integer class,     Case R ↔ half-integer class.                       (5)

### 5.2 Status of the map

Equation (5) is **not yet FORCED at the primitive level**. It is the content of the spin-statistics theorem, whose primitive-level derivation requires:

(a) The rotational double-cover SL(2) → SO(3) structure, showing that half-integer representations acquire a minus sign under 2π rotation (Stage R.2.3, Lever L4).

(b) A locality/microcausality argument showing that the 2π-rotation sign equals the exchange sign η (Stage R.2.5 synthesis).

Stage R.2.2 records the map (5) as a **structurally expected correspondence** but defers its proof. What Stage R.2.2 establishes unconditionally:

- Integer and half-integer representation classes are both mathematically well-defined.
- The dichotomy in representation content matches the dichotomy in exchange-symmetry content at the counting level (both are ℤ_2 classifications).
- No third category exists at either level.

The ℤ_2-ℤ_2 matching is suggestive but not a proof. The proof runs through Stage R.2.3's derivation of the rotational double-cover from Primitive 07 / 10 rule-type interaction content.

---

## 6. FORCED / CANDIDATE / SPECULATIVE / deferred

### 6.1 FORCED by primitives

- **F1.** Participation-measure transformation law under SO⁺(3,1) is a linear representation (from Primitive 06 covariance + composition law).
- **F2.** The internal-index representation is finite-dimensional (from discrete rule-type taxonomy, Primitive 07 §7.4).
- **F3.** Finite-dimensional representations of the complexified Lorentz algebra are exhaustively classified by (j_L, j_R), j_L, j_R ∈ {0, 1/2, 1, …} (Lie-algebraic theorem; primitive input is 3+1D Lorentz signature).
- **F4.** The spin quantum number s runs through s ∈ {|j_L − j_R|, …, j_L + j_R} via the Pauli-Lubanski Casimir (Poincaré-covariance theorem).
- **F5.** The spin ladder s ∈ {0, 1/2, 1, 3/2, 2, …} is exhaustive in 3+1D.
- **F6.** Stage R.1 scalar participation measure realises the (0, 0) / s = 0 case.

### 6.2 CANDIDATE (pending Stage R.2.3)

- **C1.** SL(2, ℂ) — the double cover — is the admissible primitive-level covariance group (not merely SO⁺(3,1)). This is required for half-integer representations to exist structurally. Stage R.2.3 will either derive or refute (C1) from primitives; empirically C1 is forced by the existence of fermions.
- **C2.** The map (5) Case P ↔ integer, Case R ↔ half-integer is the primitive-level spin-statistics correspondence. Proof deferred to Stage R.2.3 + R.2.5.

### 6.3 SPECULATIVE

- **S1.** Specific spin values for specific ED rule-types (e.g., "the electron rule-type carries s = 1/2") are empirical inputs per rule-type, not primitive-derivable. The ladder is derived; the occupied rungs are inherited.
- **S2.** Higher-spin representations (s ≥ 2) and their consistency constraints (Weinberg-Witten no-go for interacting massless s > 2) are outside Stage R.2.2 scope.

### 6.4 Deferred

- **D1.** Rotational double-cover origin → Stage R.2.3.
- **D2.** Clifford algebra / γ-matrix structure → Stage R.2.4.
- **D3.** Spin-statistics theorem synthesis → Stage R.2.5.
- **D4.** Dirac equation emergence → Stage R.3.

---

## 7. Next step

Stage R.2.3 — `rotational_double_cover_scoping.md` (Lever L4, hardest lever in the rule-type taxonomy).

**Scope of R.2.3:** Identify the primitive-level origin of the 2π-rotation sign on half-integer representations. Candidate sources:

(i) Worldline-framing structure at the rule-type interface (Primitive 02 + 07): if rule-type interactions carry an orientation-frame, rotation by 2π of the frame may not be the identity on the interaction pattern.

(ii) Adjacency-graph topology at sub-rule-type resolution (Primitive 10): the local adjacency graph around a chain may support ℤ_2 non-trivial loops.

(iii) Exchange-braiding structure (Primitive 11): in 3+1D, the exchange path τ ↦ τ' is homotopically ℤ_2-classified; this is the standard configuration-space π_1 argument.

R.2.3 will evaluate each candidate for primitive-level grounding and identify which (if any) force the double-cover without appeal to external topology theorems.

**Contingent downstream:**
- R.2.4 (Clifford algebra) needs R.2.3 to fix the spinor structure.
- R.2.5 (taxonomy synthesis) needs R.2.2 + R.2.3 + R.2.4.
- R.3 (Dirac emergence) needs R.2.2 + R.2.3 + R.2.4 closed.
- Arc M (chain-mass) is contingent on R.2.5 for spin-mass assignment rules.
- Arc Q (QFT) is contingent on R.3 + M.

Estimated scope of R.2.3: 2–4 sessions (it is the hardest lever; may require a scoping-only first pass followed by derivation passes).

---

## 8. Summary

Stage R.2.2 establishes the ladder of permitted Lorentz representations for ED participation measures:

- Transformation covariance + finite internal index space ⇒ finite-dimensional Lorentz representation.
- Lie-algebraic classification ⇒ (j_L, j_R) labels with j_L, j_R half-integer.
- Casimir labelling ⇒ spin ladder s ∈ {0, 1/2, 1, 3/2, 2, …} exhaustive.
- Stage R.1 realises s = 0; higher-spin rule-types occupy higher rungs.
- Integer vs. half-integer split matches Case P vs. Case R split at the ℤ_2 counting level; proof of the match (spin-statistics) is deferred.
- Half-integer existence requires SL(2, ℂ) over SO⁺(3,1); primitive-level origin of the double cover is Stage R.2.3.

Stage R.2.2 closes with the integer-spin content FORCED and the half-integer content CANDIDATE — exactly the expected closure for a Lever-L2 memo under the rule-type taxonomy.
