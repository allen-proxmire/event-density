# Dirac Emergence

**Stage R.3 — Arc R Main Derivation Memo**
**Status:** Derivation memo. Dirac equation (iγ^μ∂_μ − mc/ℏ)Ψ = 0 is FORCED at primitive level for Case-R rule-types, conditional on the inherited constants (m, q, ℏ, c). Gauge-covariant extension, conserved current j^μ = Ψ̄γ^μΨ, and non-relativistic reduction to Pauli and Schrödinger equations are all FORCED. Stage R.3 closes Arc R's structural content; remaining work (mass value, gauge group, generations) is Arc M / Arc Q / empirical inheritance.

---

## 1. Purpose and starting point

### 1.1 What Stage R.3 does

Stage R.1 derived the Lorentz-covariant scalar participation measure and the Klein-Gordon equation for the (0,0)-representation (spin-0) case. Stage R.2 derived the full rule-type taxonomy — including the Cl(3,1) frame, the SL(2,ℂ) double cover, and the spin-statistics correspondence η = (−1)^{2s} — making half-integer representations (spinors) structurally admissible for Case-R rule-types.

Stage R.3 assembles these into the **relativistic dynamical equation for Case-R rule-types**: the Dirac equation. The derivation is largely assembly — the structural content lives in R.1 + R.2 — but with one genuinely non-trivial step (the square-root factorisation of Klein-Gordon on the Cl(3,1) module).

### 1.2 Starting-point summary

**From Stage R.1:**
- Lorentz-covariant participation measure on (0,0) rep: P_K(x^μ) = √(b_K) · e^{iπ_K}.
- Klein-Gordon equation: (□ + m²c²/ℏ²)Ψ = 0 with □ ≡ η^{μν}∂_μ∂_ν.
- Minimal coupling: ∂_μ → D_μ = ∂_μ + (iq/ℏ)A_μ.
- Conserved current: j^μ = (iℏ/2m)[Ψ* D^μ Ψ − Ψ (D^μ Ψ)*].

**From Stage R.2:**
- Cl(3,1) algebraic frame: {γ^μ, γ^ν} = 2η^{μν}·𝟙.
- Lorentz generators: σ^{μν} = (i/2)[γ^μ, γ^ν].
- SL(2,ℂ) action on 4-dimensional spinor module.
- D(R(2π)) = −𝟙 on spinor module (automatic from half-angle in exp(−iθσ^{12}/2)).
- Case-R rule-type interface admits Fierz-bilinear coupling structure.

**New object for Stage R.3:** The participation measure for a Case-R rule-type is a **spinor-valued** field

  Ψ_α(x^μ),     α = 1, 2, 3, 4,                                                 (1)

on the 4-dimensional Cl(3,1) spinor module. α indexes the internal (spinor) index; x^μ is the ambient event-manifold coordinate. Under Lorentz transformations,

  Ψ(x) → S(Λ) Ψ(Λ^{-1} x),     S(Λ) = exp(−(i/4) ω_{μν} σ^{μν}) ∈ SL(2,ℂ).      (2)

The bar operation is Ψ̄ ≡ Ψ†γ^0 (standard Dirac adjoint, forced by the metric signature).

---

## 2. The Dirac equation as square root of Klein-Gordon

### 2.1 Problem statement

Case-R participation measures Ψ(x) live on the spinor module. Stage R.1's Klein-Gordon equation applies component-wise — each spinor component satisfies (□ + m²c²/ℏ²)Ψ_α = 0 — but this is a **second-order** equation, and a second-order equation on a spinor field does not use the Cl(3,1) frame structure non-trivially. It is blind to the γ^μ generators.

Stage R.2.4 established that the γ^μ are structurally present at the Case-R interface. A dynamical equation that **uses** this structure must be first-order in ∂_μ and must contain the γ^μ.

### 2.2 The factorisation

Consider the operator (iγ^μ∂_μ). Squaring:

  (iγ^μ∂_μ)(iγ^ν∂_ν) = −γ^μγ^ν ∂_μ∂_ν
                     = −(1/2){γ^μ, γ^ν} ∂_μ∂_ν − (1/2)[γ^μ, γ^ν] ∂_μ∂_ν
                     = −η^{μν}·𝟙 ∂_μ∂_ν − 0
                     = −□.                                                      (3)

(The commutator term vanishes because ∂_μ∂_ν is symmetric in μ↔ν while [γ^μ,γ^ν] is antisymmetric.)

Therefore

  (iγ^μ∂_μ − mc/ℏ)(iγ^μ∂_μ + mc/ℏ) = −□ − m²c²/ℏ² = −(□ + m²c²/ℏ²).              (4)

If Ψ satisfies the **first-order** equation

  (iγ^μ∂_μ − mc/ℏ) Ψ = 0,                                                       (5)

then by applying (iγ^μ∂_μ + mc/ℏ) from the left,

  (−□ − m²c²/ℏ²) Ψ = 0     ⟺     (□ + m²c²/ℏ²) Ψ = 0.                          (6)

Each component of Ψ satisfies Klein-Gordon. Equation (5) is the **Dirac equation**.

### 2.3 Why the first-order form is FORCED for Case-R

Three independent arguments force (5) over the plain component-wise Klein-Gordon:

**(A) Use of the Cl(3,1) structure.** Stage R.2.4 established the γ^μ as primitive-level frame generators at the Case-R interface. A dynamical equation that does not contain γ^μ leaves this structure inert. Equation (5) is the unique Lorentz-covariant first-order linear operator on Ψ constructible from γ^μ, ∂_μ, and a mass scale.

**(B) Single time-derivative (unitarity / positive-norm evolution).** Klein-Gordon as a second-order equation on the spinor module gives a Klein-Gordon inner product that is indefinite (negative-energy / negative-norm sector). The first-order form (5) is needed for a positive-definite current (see §4) and for a Hilbert-space evolution compatible with the Stage R.1 participation-measure inner product structure.

**(C) Half-integer representation content.** Klein-Gordon is the natural equation for (0,0). For (1/2, 0) ⊕ (0, 1/2) (the Dirac spinor), the minimal covariant first-order equation using the Cl(3,1) frame is exactly (5). This is a Lorentz-representation-theoretic statement; the Dirac equation is the unique (up to equivalence) first-order Lorentz-covariant wave equation on the Dirac spinor module.

**FORCED:** Given Stage R.2 (spinor module + Cl(3,1) frame) and Stage R.1 (Klein-Gordon), the Dirac equation (5) is the unique structurally admissible first-order dynamical equation for Case-R rule-type participation measures.

### 2.4 Dimensional consistency

Rewriting (5) in SI-standard form:

  (iℏγ^μ∂_μ − mc) Ψ = 0.                                                        (7)

Here ℏ, m, c enter as dimensional anchors inherited from the Dimensional Atlas — ℏ from Stage Q.2 (U3 evolution derivation), m from the rule-type's empirical mass content, c from the Stage R.1 Lorentz metric normalisation. The **form** of (7) is FORCED; the **numerical values** of (ℏ, m, c) are inherited.

---

## 3. Minimal coupling

### 3.1 Gauge-covariant derivative

Following Stage R.1's minimal-coupling procedure (`kg_minimal_coupling_and_current.md`), promote

  ∂_μ → D_μ ≡ ∂_μ + (iq/ℏ) A_μ,                                                 (8)

where A_μ is a U(1) gauge field and q is the rule-type's charge. Primitive-level origin of (8) at the KG level: requiring invariance under local phase rotations Ψ → e^{iqα(x)/ℏ} Ψ. For a Case-R spinor rule-type, the same local-phase-invariance argument applies to the overall phase of Ψ (the spinor index is untouched by U(1)). Therefore (8) extends to the Dirac case unchanged.

### 3.2 Interacting Dirac equation

Substituting (8) into (5):

  (iγ^μ D_μ − mc/ℏ) Ψ = 0,                                                     (9)

or equivalently

  (iℏγ^μ ∂_μ − qγ^μ A_μ − mc) Ψ = 0.                                           (10)

### 3.3 Gauge covariance

Under local U(1),
  Ψ(x) → e^{iqα(x)/ℏ} Ψ(x),     A_μ(x) → A_μ(x) − ∂_μ α(x).

Then D_μ Ψ → e^{iqα/ℏ} D_μ Ψ (standard computation), so the left-hand side of (9) transforms as
  (iγ^μ D_μ − mc/ℏ) Ψ → e^{iqα/ℏ} · (iγ^μ D_μ − mc/ℏ) Ψ = 0.

The equation is gauge-covariant.

**FORCED:** Local-phase invariance of the Case-R participation measure forces the replacement (8) and produces the interacting Dirac equation (9). This is the Stage R.1 minimal-coupling argument applied on the spinor module; no new structural input required.

### 3.4 Status of non-Abelian extension

Extension from U(1) to SU(N) gauge groups replaces the single phase by an N-component internal index and A_μ by a Lie-algebra-valued gauge field. The structural machinery is the same (local invariance ⇒ covariant derivative), but:
- The choice of gauge group is **not** primitive-derivable — it enters as rule-type data at Primitive 07 Lever L2 (internal-index content).
- Specific assignment of Case-R rule-types to gauge-group representations (e.g., SU(3) triplet for quark-like, SU(2) doublet for lepton-like) is empirical.

**SPECULATIVE/deferred:** Gauge-group specification is Arc Q content.

---

## 4. Conserved current

### 4.1 Construction

Multiply (9) from the left by Ψ̄:
  Ψ̄ iγ^μ D_μ Ψ = (mc/ℏ) Ψ̄ Ψ.                                                 (11)

Take the Hermitian conjugate of (9):
  (−iγ^μ D_μ)† Ψ† = (mc/ℏ) Ψ†,
which using (γ^μ)† = γ^0 γ^μ γ^0 and multiplying by γ^0 from the right gives the adjoint equation
  Ψ̄ (iγ^μ D̄_μ + mc/ℏ) = 0,                                                    (12)

with D̄_μ the conjugate covariant derivative acting to the left.

Subtracting (11) from Ψ̄ multiplied into the adjoint, the mass terms cancel, leaving

  ∂_μ (Ψ̄ γ^μ Ψ) = 0.                                                          (13)

So

  **j^μ ≡ Ψ̄ γ^μ Ψ**                                                           (14)

is conserved: ∂_μ j^μ = 0.

### 4.2 Positive-definite density

The time component:
  j^0 = Ψ̄ γ^0 Ψ = Ψ† γ^0 γ^0 Ψ = Ψ† Ψ = Σ_α |Ψ_α|² ≥ 0.                       (15)

This is **positive-definite**, unlike the Klein-Gordon current (iℏ/2m)(Ψ*∂_0Ψ − Ψ∂_0Ψ*), which is indefinite. This resolves the Klein-Gordon negative-probability pathology for Case-R fields: the Dirac current gives a bona fide probability / participation-measure-amplitude density.

**FORCED:** j^μ = Ψ̄γ^μΨ is conserved and j^0 is positive-definite. This is the spinor analogue of Stage R.1's scalar conserved current, with improved positivity structure inherent to the first-order spinor form.

### 4.3 Connection to Stage R.1 scalar current

For a (0,0) scalar rule-type, the conserved current is the Klein-Gordon current (iℏ/2m)[Ψ* D^μ Ψ − Ψ (D^μ Ψ)*]. For a (1/2,0) ⊕ (0,1/2) spinor rule-type, the conserved current is Ψ̄γ^μΨ. Both are Lorentz four-vectors, both arise from global U(1) symmetry (Noether), both couple to A_μ via minimal coupling.

The spinor current's positivity is structurally linked to the first-order form of Dirac; the scalar current's indefiniteness is structurally linked to the second-order form of Klein-Gordon. This is the field-theory-level statement that Case-R rule-types (fermions) admit single-particle probabilistic interpretations, while Case-P rule-types (bosons) require field-theoretic interpretation — a well-known fact now traced to rule-type structure.

---

## 5. Non-relativistic reduction

### 5.1 Setup

Write the spinor as

  Ψ = (φ, χ)ᵀ · e^{−imc²t/ℏ}                                                   (16)

where φ, χ are 2-component Pauli spinors and the phase factor removes the rest-energy oscillation. In the Dirac representation (γ^0 = diag(𝟙, −𝟙), γ^i = off-diagonal with Pauli σ^i), equation (9) becomes coupled equations for φ and χ.

### 5.2 First-order elimination

In the non-relativistic limit, χ is small (of order v/c) compared to φ. Solving the χ equation algebraically and substituting back (standard Dirac-to-Pauli reduction), keeping terms to lowest non-trivial order:

  iℏ ∂_t φ = [(p − qA)²/(2m) + qA^0 − (qℏ/2m) σ·B] φ,                          (17)

with B = ∇×A the magnetic field. Equation (17) is the **Pauli equation**: Schrödinger with an explicit Zeeman term coupling spin σ to the magnetic field.

### 5.3 Gyromagnetic ratio

The Zeeman coefficient (qℏ/2m) = g·μ_B/ℏ · ℏ, with g = 2 the Dirac-predicted gyromagnetic ratio. **This is a structural prediction of Stage R.3**: g_Dirac = 2 emerges from the Cl(3,1) frame + first-order form + non-relativistic reduction, without empirical tuning. Higher-order QED corrections (g − 2 ≈ α/π + …) are Arc Q content, not primitive-level content.

**FORCED:** Dirac g = 2 as the leading-order gyromagnetic ratio is FORCED by Stage R.3. Deviations from g = 2 are inherited from QFT radiative structure (Arc Q).

### 5.4 Further reduction: spin-orbit, Darwin, Schrödinger

Higher orders in v/c (via Foldy-Wouthuysen transformation) produce:
- Kinetic energy correction −p⁴/(8m³c²).
- Spin-orbit coupling (qℏ/4m²c²) σ·(E × p).
- Darwin term (qℏ²/8m²c²) ∇·E.

Dropping all spin-dependent terms (setting σ → 0 formally, i.e., reducing to a single Pauli component or projecting onto spinless participation) and taking only the leading kinetic term yields

  iℏ ∂_t ψ = [(p − qA)²/(2m) + qA^0] ψ,                                         (18)

which is the **Schrödinger equation** — Phase-1 consistency check.

**Consistency with Phase-1:** Stage R.3's non-relativistic reduction recovers the Stage Q.2 Schrödinger equation (from `u3_evolution_derivation.md`) in the spinless limit. The Phase-1 scalar-participation-measure Schrödinger derivation and the Stage R.3 Dirac non-relativistic reduction agree on the form of the low-energy dynamics. This closes a consistency-check loop across the entire QM-emergence program.

---

## 6. FORCED / inherited / deferred

### 6.1 FORCED at primitive level (conditional on inherited constants)

- **F1.** First-order Lorentz-covariant equation (iγ^μ∂_μ − mc/ℏ)Ψ = 0 from R.1 + R.2. (§2)
- **F2.** Squaring recovers Klein-Gordon component-wise. (§2.2)
- **F3.** Minimal coupling D_μ = ∂_μ + (iq/ℏ)A_μ extends from Stage R.1 unchanged. (§3)
- **F4.** Gauge-covariant Dirac equation (iγ^μD_μ − mc/ℏ)Ψ = 0. (§3)
- **F5.** Conserved current j^μ = Ψ̄γ^μΨ; ∂_μj^μ = 0. (§4)
- **F6.** Positive-definite density j^0 = Ψ†Ψ ≥ 0 (resolves KG negative-probability for Case R). (§4.2)
- **F7.** Pauli equation (17) from non-relativistic reduction; Dirac g = 2 predicted. (§5)
- **F8.** Schrödinger equation recovered in spinless limit (Phase-1 consistency). (§5.4)

### 6.2 Inherited (dimensional / empirical)

- **I1.** Numerical values of ℏ, c (set by Dimensional Atlas / Stage R.1 metric normalisation).
- **I2.** Mass m per rule-type (empirical; Arc M may derive structural constraints but not the specific value).
- **I3.** Charge q per rule-type (empirical; gauge-representation assignment is Arc Q).
- **I4.** Choice of Dirac vs. Weyl vs. Majorana representation (algebraic refinement, not primitive-forced).

### 6.3 Deferred

- **D1.** Mass origin (structural): Arc M (`chain_mass_scoping.md` and downstream).
- **D2.** Gauge-group specification beyond U(1): Arc Q.
- **D3.** QED radiative corrections (g − 2, Lamb shift, vacuum polarisation): Arc Q.
- **D4.** Multi-particle / second quantisation: Arc Q.
- **D5.** Number of fermion generations: open; possibly Arc M or empirical.
- **D6.** CP violation, flavour mixing, Yukawa couplings: Arc Q + empirical.

### 6.4 CANDIDATE

- *None.* Stage R.3 opens no new CANDIDATEs. All structural content is FORCED on the R.1 + R.2 foundation; everything else is inherited or deferred to downstream arcs.

### 6.5 SPECULATIVE

- **S1.** Primitive-level origin of the fermion mass spectrum and generation count.
- **S2.** Primitive-level origin of specific gauge group SU(3)×SU(2)×U(1).
- **S3.** Supersymmetric pairing of Case-P and Case-R rule-types (not addressed; ED neither requires nor forbids it structurally).

---

## 7. Closure of Stage R.3

### 7.1 What Stage R.3 achieves

Stage R.3 delivers the relativistic quantum dynamical equation for Case-R rule-types as a primitive-level consequence of ED. Specifically:

- The Dirac equation (iγ^μ∂_μ − mc/ℏ)Ψ = 0 is structurally FORCED on Stage R.1 + Stage R.2 foundations.
- Minimal gauge coupling, conserved current, gyromagnetic g = 2, and non-relativistic reductions to Pauli and Schrödinger all follow FORCED.
- No new CANDIDATEs opened at the R.3 level.

Combined with Stage R.1 (scalar Klein-Gordon + minimal coupling + scalar conserved current) and Stage R.2 (spin-statistics), Arc R delivers ED's structural foundation for relativistic quantum kinematics and dynamics for both bosonic and fermionic rule-types.

### 7.2 Remaining arcs

- **Arc M (chain-mass):** Derive structural constraints on mass values / ratios / scales for ED rule-types. Contingent on R.3 (uses Dirac mass term as the anchor).
- **Arc Q (QFT):** Second-quantise Dirac + Klein-Gordon fields; gauge-group content; QED/EW/QCD analogues; radiative corrections. Contingent on R.3 + Arc M.
- **Arc N (non-Markovian):** Platform-specific memory-kernel derivations. Independent of R.3 linearly but ties in at QFT level.
- **Gauge-group structure, generations, Yukawa, CP violation:** Mixed structural/empirical; primarily Arc Q with empirical inheritance.

### 7.3 Status

**Stage R.3 is structurally complete** modulo inherited constants (m, q, ℏ, c). The relativistic quantum dynamical content of ED for both spin-0 and spin-1/2 rule-types is now primitive-level derived.

Arc R as a whole (R.1 + R.2 + R.3) is the **relativistic closure** of the QM-emergence program, paralleling the Phase-1 non-relativistic closure. Together they establish that ED's primitive stack produces:

- Scalar wave equations (Klein-Gordon, Schrödinger) for Case-P / bosonic content.
- Spinor wave equations (Dirac, Pauli) for Case-R / fermionic content.
- Spin-statistics correspondence η = (−1)^{2s}.
- Positive-definite conserved currents for fermions; field-theoretic current for bosons.
- Gauge-covariant minimal coupling via local-phase invariance.
- Non-relativistic reduction consistent with Phase-1 Schrödinger derivation.

All structurally FORCED; all numerical values inherited.

---

## 8. Cross-references

- Stage R.1: `arc_r_stage1_synthesis.md`, `klein_gordon_emergence.md`, `kg_minimal_coupling_and_current.md`.
- Stage R.2: `rule_type_taxonomy.md`, `rule_type_exchange_symmetry.md`, `lorentz_representations_from_primitives.md`, `rotational_double_cover_scoping.md`, `clifford_algebra_from_spinor_structure.md`, `rule_type_taxonomy_synthesis.md`.
- Phase-1 consistency: `schrodinger_emergence.md`, `u3_evolution_derivation.md`, `qm_emergence_closure.md`.
- Downstream: Arc M scoping (forthcoming `chain_mass_scoping.md`), Arc Q scoping (forthcoming).

---

## 9. One-line summary

**Stage R.3 closes Arc R: the Dirac equation (iγ^μ∂_μ − mc/ℏ)Ψ = 0, its gauge-covariant extension, the conserved current Ψ̄γ^μΨ, the Dirac g = 2, and the non-relativistic Pauli / Schrödinger reductions are all FORCED at primitive level for Case-R rule-types — with only mass, charge, ℏ, and c inherited.**
