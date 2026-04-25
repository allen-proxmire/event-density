# Clifford Algebra from Spinor Structure

**Stage R.2.4 — Rule-Type Taxonomy Sub-Program**
**Status:** Derivation memo. Algebraic uniqueness of Cl(3,1) as the frame-carrying structure for Case-R rule-types FORCED. CANDIDATE FA (frame-availability, from Stage R.2.3) discharged conditional on one residual CANDIDATE — rule-type interface admits an orientation-sensitive bilinear pairing (MB). MB is structurally motivated by Primitive 07 §7.4 Lever L2 (internal-index content) and expected to close at Stage R.2.5 synthesis.

---

## 1. Goal of Stage R.2.4

Stage R.2.3 identified CANDIDATE **FA (frame-availability)**: every Case-R rule-type carries, at its interface, a local frame in a representation space where 0 and 2π rotations are distinguishable. FA was not derivable from Primitives 02/06/07/10/11 **as written**. Stage R.2.4's job is to identify the algebraic structure that realises FA and to show that this structure is forced — not chosen — by the constraints already on the table.

Specifically, Stage R.2.4 will:

(a) Pose the algebraic problem: what finite-dimensional real algebraic structure is compatible with (i) Lorentz covariance, (ii) half-integer representation content, (iii) the π_1 = ℤ_2 double cover?

(b) Show the unique solution is the real Clifford algebra Cl(3,1) with generators γ^μ satisfying the anticommutation relation {γ^μ, γ^ν} = 2η^{μν}·𝟙.

(c) Identify γ^μ as the frame at the rule-type interface and show D(R(2π)) = −1 on the spinor index automatically.

(d) Show the Lorentz generators σ^{μν} = (i/2)[γ^μ, γ^ν] generate the SL(2,ℂ) action on spinors.

(e) Identify the spinor bilinears (Ψ̄Ψ, Ψ̄γ^μΨ, Ψ̄σ^{μν}Ψ, Ψ̄γ^μγ^5Ψ, Ψ̄γ^5Ψ) as the minimal orientation-sensitive rule-type interface structure.

(f) Record FA status: discharged modulo CANDIDATE MB.

Stage R.2.4 does **not** derive:
- The Dirac equation (→ Stage R.3).
- Specific spinor-mass assignments per rule-type (empirical inheritance).
- Weyl/Majorana reality-structure choice (→ Stage R.2.5 or later).

---

## 2. Primitive-level and upstream inputs

### 2.1 Primitives used

- **Primitive 02 (worldline + ambient 3+1D manifold):** supplies the tangent space at each chain event.
- **Primitive 06 (four-gradient, Lorentz covariance):** supplies η^{μν} = diag(−,+,+,+) as the structural metric on the tangent space.
- **Primitive 07 (rule-type) §7.4, Lever L2 (internal-index content):** permits rule-types to carry finite-dimensional internal indices with their own transformation rules.
- **Primitive 10 (individuation):** excludes same-type coincidence in Case R (already used in R.2.3 §3.4).
- **Primitive 11 (commitment dynamics):** supplies the exchange path whose π_1 class lives in ℤ_2.

### 2.2 Upstream results

- **R.2.2 §3.3:** finite-dimensional Lorentz representations are classified by (j_L, j_R).
- **R.2.2 §3.4:** half-integer (j_L + j_R ∈ ℤ + 1/2) representations require SL(2,ℂ).
- **R.2.3 §3:** π_1 of the two-identical-chain configuration space is ℤ_2 in 3+1D.
- **R.2.3 §4:** the exchange-path generator equals the 2π-rotation generator.
- **R.2.3 CANDIDATE FA:** Case-R rule-types carry a frame making 0 vs 2π distinguishable.

Stage R.2.4 inherits these and answers: *what is the frame?*

---

## 3. The algebraic problem

### 3.1 Formulation

We seek a real, finite-dimensional associative algebra 𝒜 with the following properties:

(P1) **Lorentz tangent-space compatibility.** 𝒜 contains a four-dimensional real subspace V spanned by elements {e_0, e_1, e_2, e_3} that transform as a Lorentz four-vector under a representation ρ: SL(2,ℂ) → Aut(𝒜).

(P2) **Metric compatibility.** The symmetric bilinear combination e_μ e_ν + e_ν e_μ reproduces the Lorentz metric η_{μν}·𝟙_𝒜 (up to an overall real scale), so the algebra encodes the metric structure from Primitive 06.

(P3) **Half-integer representation realisation.** The adjoint action of 𝒜 on itself (or on a faithful module of 𝒜) contains a representation of SL(2,ℂ) of half-integer (j_L, j_R) type — equivalently, a representation on which D(R(2π)) = −𝟙.

(P4) **Minimal dimension.** Among algebras satisfying (P1)–(P3), 𝒜 is the smallest (to avoid introducing structure not forced by the primitives).

(P1) + (P2) are direct transcriptions of the Primitive 06 covariance + metric content into algebraic language. (P3) is what FA requires: an algebraic frame in which 0 and 2π rotations act differently. (P4) is Occam at the structural level — we do not introduce superfluous representation content.

### 3.2 Why an **anti**commutation relation is forced

Suppose (P2) is satisfied with a **commutation** relation e_μ e_ν = e_ν e_μ (commutative 𝒜). Then the only symmetric bilinear on V taking values in 𝟙 is the symmetric product, and (P2) reduces to e_μ e_ν = (η_{μν}/2)·𝟙 for all μ, ν — but this forces e_μ = 0 unless μ = ν, and even then the products are rigid scalars. The resulting algebra is the quotient of the polynomial ring by these relations, which does not support a non-trivial SL(2,ℂ) representation of half-integer type. (P3) fails.

Suppose instead that e_μ e_ν = −e_ν e_μ **strictly** (purely antisymmetric). Then e_μ e_μ = 0 for each μ (no squared elements), so (P2) with diagonal η fails: we get 0 = η_{μν}·𝟙 on the diagonal, contradiction.

The only remaining possibility is a **mixed** relation of the form

  e_μ e_ν + e_ν e_μ = 2η_{μν}·𝟙,                                                (1)

which is neither purely commutative nor purely anticommutative. This is the **defining relation of the real Clifford algebra Cl(3,1)**. (P2) reduces to (1) exactly, with the factor 2 a convention.

**FORCED:** Under (P1) + (P2), the generator algebra is Cl(3,1) up to convention. The anticommutator, not the commutator, is the structurally mandatory pairing.

### 3.3 Uniqueness up to isomorphism

The real Clifford algebra Cl(3,1) is unique up to isomorphism once the metric signature is fixed. As a real algebra it is isomorphic to the 4×4 real matrix algebra M_4(ℝ). Its dimension as a real vector space is 2^4 = 16, with basis

  {𝟙, γ^μ, γ^{μν}, γ^{μνρ}, γ^5} = {1 scalar, 4 vectors, 6 bivectors, 4 trivectors, 1 pseudoscalar}. (2)

This is the exhaustive grading; nothing further is generated. The basis (2) is the minimal generating set compatible with (P1)–(P4).

### 3.4 Complex versus real

For practical calculation one often complexifies to Cl(3,1)_ℂ ≅ M_4(ℂ). The complexification is a tool, not a structural commitment; the primitive-level algebra is real Cl(3,1). This distinction matters when discussing Majorana spinors (which exist structurally in Cl(3,1) because it is M_4(ℝ)) versus Weyl spinors (which require complex structure). Stage R.2.4 notes but does not resolve this; the reality-structure choice is downstream.

---

## 4. Frame, rotation, and the 2π sign

### 4.1 γ^μ as the frame at the rule-type interface

Identify e_μ ≡ γ^μ. Then {γ^μ} is a four-component object transforming as a Lorentz vector (by (P1)) and squaring via (1) to the metric. This is precisely a **local tetrad** at the rule-type interface: an orthonormal frame in which inner products reproduce η_{μν}.

Candidate (i) of Stage R.2.3 — worldline-framing at the rule-type interface — is thus realised algebraically by γ^μ. The frame is not a superimposed structure; it is the generating set of the minimal algebra compatible with Primitive 06 + half-integer representation content.

**FORCED:** γ^μ is the algebraic frame postulated abstractly in R.2.3 candidate (i).

### 4.2 Lorentz generators

Define

  σ^{μν} ≡ (i/2) [γ^μ, γ^ν].                                                    (3)

Using (1), one computes (standard calculation):

  [σ^{μν}, σ^{ρσ}] = i(η^{μρ}σ^{νσ} − η^{νρ}σ^{μσ} − η^{μσ}σ^{νρ} + η^{νσ}σ^{μρ}). (4)

Relation (4) is the Lorentz-algebra commutation relation. Therefore {σ^{μν}} generate a representation of so(3,1) on the 4-dimensional spinor module of Cl(3,1). Exponentiation exp(−(i/4) ω_{μν} σ^{μν}) produces a representation of the Lorentz group.

Crucially, because σ^{μν} are **quadratic** in γ^μ, the exponent exp(−(i/4) ω_{μν} σ^{μν}) for a finite rotation ω_{μν} generates not SO⁺(3,1) directly but its double cover SL(2,ℂ) acting on the spinor module. This is the standard Dirac-spinor construction.

**FORCED:** σ^{μν} generates SL(2,ℂ) on the spinor module.

### 4.3 The 2π sign

Take a pure spatial rotation by angle θ about the z-axis: ω_{12} = θ, others zero. Then

  U(θ) = exp(−(i/2) θ σ^{12}).                                                  (5)

Using (σ^{12})² = 𝟙 on the 4-dimensional spinor module (direct computation from (1)),

  U(θ) = cos(θ/2)·𝟙 − i sin(θ/2)·σ^{12}.                                       (6)

At θ = 2π:

  U(2π) = cos(π)·𝟙 − i sin(π)·σ^{12} = −𝟙.                                     (7)

At θ = 4π:

  U(4π) = +𝟙.                                                                   (8)

So D(R(2π)) = −𝟙 on the spinor module automatically. The half-angle in (5) is structurally forced by σ^{μν} being quadratic in γ^μ and the γ^μ anticommuting — there is no tuning.

**FORCED:** On the Cl(3,1) spinor module, 2π rotations act as −𝟙; 4π rotations as +𝟙. This is the double-cover realisation R.2.3 required for CANDIDATE FA.

### 4.4 Discharge of FA

Under the identification e_μ ≡ γ^μ at the rule-type interface, the Cl(3,1) algebra provides:

- A local frame (γ^μ) — R.2.3 candidate (i) realisation.
- A representation space (the spinor module, 4-dim) — finite-dimensional per R.2.2 §3.2.
- An SL(2,ℂ) action via σ^{μν} — R.2.2 §3.4 half-integer content.
- Automatic D(R(2π)) = −𝟙 — R.2.3 §4.2 requirement.

These are the four ingredients FA called for. CANDIDATE FA is **discharged**, conditional on one residual structural question addressed in §6 below: whether the rule-type interface admits the **bilinear pairing** needed to couple Case-R rule-types to this algebraic frame.

---

## 5. Spinor bilinears as the orientation-sensitive interface structure

### 5.1 The five Dirac bilinears

For two spinors Ψ_1, Ψ_2 on the 4-dim Cl(3,1) module, with Ψ̄ ≡ Ψ†γ^0, the independent Lorentz-covariant bilinears are:

| Bilinear                     | Lorentz type     | Count |
|------------------------------|------------------|-------|
| Ψ̄_1 Ψ_2                       | scalar           | 1     |
| Ψ̄_1 γ^μ Ψ_2                    | vector           | 4     |
| Ψ̄_1 σ^{μν} Ψ_2                 | antisym tensor   | 6     |
| Ψ̄_1 γ^μ γ^5 Ψ_2                 | axial vector     | 4     |
| Ψ̄_1 γ^5 Ψ_2                    | pseudoscalar     | 1     |
|                              | **Total**        | **16**|

Total = 16, which equals dim_ℝ Cl(3,1). This is Fierz-decomposition completeness: the bilinears span every Lorentz-covariant local pairing available from two spinors.

### 5.2 Why this is the minimal orientation-sensitive structure

A Case-R rule-type's interface must discriminate the orientation content that integer-spin interfaces cannot. The key markers are:

- **Pseudoscalar Ψ̄γ^5Ψ** — sensitive to spatial parity. Scalar Ψ̄Ψ is not.
- **Axial vector Ψ̄γ^μγ^5Ψ** — sensitive to parity distinct from vector Ψ̄γ^μΨ.
- **Antisymmetric tensor Ψ̄σ^{μν}Ψ** — carries spin-angular-momentum density; minimal object with rotation-generator structure.

These parity-distinguishing and spin-carrying bilinears are absent from any purely tensorial (integer-representation) interface. They are what lets a Case-R rule-type see "0 ≠ 2π" locally.

**FORCED under MB (see §6):** The spinor bilinears (§5.1) are the complete, minimal set of Lorentz-covariant interface couplings for Case-R rule-types. No further structure is forced; none is available algebraically.

### 5.3 Rule-type interface realisation

A Case-R rule-type interface is specified by a choice of which bilinears couple at the interface and with what relative strengths. The choice is rule-type data (Primitive 07 §7.4 Lever L3: interface content). The **set of admissible choices** is FORCED to be the 16-dimensional Fierz basis; the **specific choice per rule-type** is empirical.

This separation preserves the standard ED discipline: structure fixes the taxonomy; occupancy is empirical.

---

## 6. Residual CANDIDATE MB

### 6.1 Statement

**CANDIDATE MB (Minimal Bilinear pairing).** The rule-type interface (Primitive 07 §7.4) admits a real or complex bilinear pairing between two same-type chain indices, i.e., a map

  m: V_rule × V_rule → 𝒜 (or some grading of 𝒜),

where V_rule is the rule-type's internal index space and 𝒜 = Cl(3,1). Equivalently: the rule-type carries interface content capable of being written as a Fierz-style bilinear on spinor indices.

MB is motivated by Primitive 07 §7.4 Lever L2 (internal-index structure) and Primitive 10 (individuation's two-chain interaction structure). It is not, however, **syntactically derivable** from the primitive stack as currently articulated — we need a bilinear, which presupposes two slots for chain indices of the same rule-type.

### 6.2 Why MB is structurally light

Under MB, everything in §§3–5 is FORCED. Without MB, the Cl(3,1) structure exists algebraically but has no hook into rule-type content.

MB is structurally lighter than FA because it asks for *any* bilinear pairing, which is already almost-trivially present in any two-chain interaction structure (exchange, individuation, commitment all involve two-chain content). Explicit derivation of MB from Primitives 10 + 11 is an exercise in writing Primitive 10's individuation pairing in bilinear form; expected to be routine at Stage R.2.5 synthesis.

### 6.3 Status

MB is recorded here as the residual CANDIDATE. It is expected to close at Stage R.2.5 without difficulty. If it does, the full chain

  Primitives ⟹ Cl(3,1) at Case-R interface ⟹ FA ⟹ spin-statistics map

becomes unconditionally FORCED.

---

## 7. FORCED / CANDIDATE / SPECULATIVE

### 7.1 FORCED by primitives + upstream

- **F1.** (P1)+(P2) admit a unique solution up to isomorphism: Cl(3,1) with {γ^μ, γ^ν} = 2η^{μν}. (§3)
- **F2.** Neither pure commutation nor pure anticommutation works; the anticommutator is structurally mandatory. (§3.2)
- **F3.** dim_ℝ Cl(3,1) = 16; grading is {scalar, vector, bivector, trivector, pseudoscalar}. (§3.3)
- **F4.** γ^μ realises the algebraic frame at the rule-type interface. (§4.1)
- **F5.** σ^{μν} = (i/2)[γ^μ, γ^ν] satisfies the Lorentz-algebra commutation relations; generates SL(2,ℂ) on the spinor module. (§4.2)
- **F6.** D(R(2π)) = −𝟙, D(R(4π)) = +𝟙 on the spinor module. (§4.3)
- **F7.** The 16-dimensional Fierz basis exhausts Lorentz-covariant two-spinor bilinears. (§5.1)

### 7.2 FORCED conditional on CANDIDATE MB

- **F-MB-1.** Case-R rule-type interfaces are realised by the Fierz basis of spinor bilinears. (§5.2–5.3)
- **F-MB-2.** CANDIDATE FA (from R.2.3) is fully discharged.
- **F-MB-3.** The spin-statistics map Case P ↔ integer / Case R ↔ half-integer is unconditionally forced.

### 7.3 CANDIDATE

- **CANDIDATE MB.** Rule-type interface admits a bilinear pairing on same-type chain internal indices. Expected to close at Stage R.2.5 via Primitive 10 + 11 pairing structure.

### 7.4 SPECULATIVE / deferred

- **S1.** Specific per-rule-type choice of Fierz coupling is empirical.
- **S2.** Weyl vs. Majorana vs. Dirac reality structure — downstream of Stage R.2.5.
- **S3.** Higher-generation / flavour structure — downstream of Arc-M (chain-mass) and Arc-Q (QFT).
- **D1.** Dirac equation emergence: deferred to Stage R.3.
- **D2.** Coupling γ^μ-frame to gauge structure (spinor connection, spin-gauge interplay) — Arc-Q.

---

## 8. Summary

Stage R.2.4 establishes:

1. The algebraic structure compatible with Lorentz covariance, half-integer representations, and the π_1 = ℤ_2 double cover is **uniquely** the real Clifford algebra Cl(3,1). (F1–F3)
2. γ^μ is the algebraic frame at the rule-type interface; σ^{μν} generates SL(2,ℂ); 2π rotation acts as −𝟙 automatically. (F4–F6)
3. The 16-dimensional Fierz basis exhausts admissible Lorentz-covariant bilinears; specific couplings are rule-type data. (F7)
4. **CANDIDATE FA from Stage R.2.3 is discharged**, conditional on CANDIDATE MB (a bilinear pairing on same-type chain indices). MB is structurally light and expected to close at Stage R.2.5.
5. The primitive-level chain from exchange-symmetry dichotomy (R.2.1) through Lorentz-representation ladder (R.2.2) through rotational double cover (R.2.3) through algebraic frame (R.2.4) is now structurally complete modulo MB.
6. The Dirac equation is **not** derived here; that is Stage R.3, and it proceeds from the Cl(3,1) frame and the Stage R.1 covariant update law by the standard linear-square-root-of-Klein-Gordon construction, now primitive-justified at every step.

Stage R.2.4 closes its scoping + derivation responsibility. The remaining rule-type taxonomy work is assembly (Stage R.2.5) rather than new structural derivation.
