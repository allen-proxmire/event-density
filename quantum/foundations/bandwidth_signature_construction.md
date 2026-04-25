# Bandwidth Signature Construction

**Stage M.1.1 — Arc M Sub-Memo**
**Status:** Construction memo. Defines the candidate bandwidth signature σ_τ as a rule-type-invariant functional of the four-band structure. Lorentz-covariant scalar form FORCED. Specific weighting coefficients between bands CANDIDATE. Per-rule-type numerical value of σ_τ inherited via b_K initial-condition amplitude. The construction is provisional — its job is to give Stage M.1.2 (massless rule-types) and Stage M.1.3 (ratios) a concrete object to evaluate, not to predict masses.

---

## 1. Goal

Construct, from Primitive 04 (bandwidth fields b_K with four-band decomposition b = b^int + b^adj + b^env + b^com) and Primitive 07 (rule-type structure, post R.2 closure), a rule-type-invariant scalar σ_τ — the **bandwidth signature** — that is a candidate for the rule-type's structural energy scale.

Specifically, σ_τ should:

(a) Be a Lorentz scalar (so that mc² ↔ σ_τ has a chance of holding covariantly).
(b) Depend only on rule-type-level structural data, not on the chain-specific dynamical state.
(c) Be defined for both Case-P and Case-R rule-types (with possibly different formulae).
(d) Permit σ_τ = 0 for at least one rule-type class (to allow massless rule-types).
(e) Be additive or multiplicative under the four-band decomposition in a primitive-justified way.

The target is the cleanest provisional formula consistent with these requirements, plus an honest accounting of what is FORCED vs. CANDIDATE vs. inherited.

This memo does **not** predict any specific m_τ value; it constructs the structural object.

---

## 2. Inputs

### 2.1 Primitive 04 — bandwidth fields

For each chain K, the bandwidth field b_K(x^μ) ≥ 0 admits the four-band decomposition

  b_K = b_K^int + b_K^adj + b_K^env + b_K^com,                                  (1)

with:
- **b^int** (internal): rule-type-internal bandwidth content; structural per τ.
- **b^adj** (adjacency): bandwidth shared with adjacent chains via Primitive 10's individuation pairing.
- **b^env** (environment): bandwidth absorbed into / exchanged with the environment.
- **b^com** (commitment): bandwidth allocated to commitment events along γ_K (Primitive 11).

Each b_K^X(x) is a non-negative real scalar field on the event manifold.

### 2.2 Primitive 07 — rule-type structure

Post R.2.5 closure, a rule-type τ is specified by:
- **L1 (bandwidth partition):** a rule-type-specific weighting w_τ^X over the four bands X ∈ {int, adj, env, com}.
- **L2 (internal-index content):** a finite-dimensional Lorentz representation (j_L, j_R)_τ.
- **L3 (interface content):** a Fierz-class element Γ_τ ∈ Cl(3,1) for Case R; equivalent tensor structure for Case P.
- **L4 (double-cover sector):** Case P (η = +1) or Case R (η = −1).

Of these, L1 is the most directly mass-relevant — it dictates how rule-type τ partitions its bandwidth across the four bands.

### 2.3 R.2 taxonomy outputs

- (j_L, j_R)_τ fixes spin s_τ.
- Cl(3,1) frame for Case R supplies γ^μ.
- Spin-statistics fixes η_τ = (−1)^{2s_τ}.

### 2.4 Stage R.1 anchoring

The participation measure carries dimensions [P_K] such that |P_K|² = b_K. Stage R.1 / Stage Q.2 fix the Planck relation E ↔ ℏω with ω the participation-measure phase rate. Bandwidth × frequency → energy is the dimensional path.

---

## 3. Construction strategy

### 3.1 What σ_τ should look like dimensionally

We need σ_τ to have units of energy. The available primitive-level objects are:
- b^X (dimensionless or [length]^{-3}, depending on normalisation convention; treat as a density).
- Rule-type weights w_τ^X (dimensionless).
- ℏ (energy × time, inherited).
- A characteristic frequency ω_τ extracted from the rule-type's bandwidth spectral structure (units [time]^{-1}).
- c (length / time, inherited).

The minimal Lorentz-scalar energy invariant constructible from these is

  σ_τ = ℏ · Ω_τ,                                                                (2)

where Ω_τ is a rule-type-specific frequency invariant built from the four-band content. This reduces the mass problem to: **what is Ω_τ?**

### 3.2 Lorentz-scalar requirement

Each b_K^X(x) is a Lorentz scalar (a density on the event manifold). Its four-gradient ∂_μ b_K^X is a four-vector. The natural Lorentz-scalar combinations available are:

(i) b_K^X itself (scalar).
(ii) ∂_μ b_K^X · ∂^μ b_K^X (squared four-gradient, scalar).
(iii) Time integrals along γ_K of (i)–(ii) per dτ_K.
(iv) Spatial integrals of (i)–(ii) on a τ_K-constant slice.

For σ_τ to be a **rule-type invariant** (not chain-specific), we need a construction that averages out chain-specific data and retains only τ-dependent content. The natural averaging is along the rule-type's worldline at rest (proper-time average) and across the rule-type's structural bandwidth content (band-weighted sum).

### 3.3 Candidate scalar functional

Define, for a chain K of rule-type τ in its rest frame:

  Ω_τ² ≡ ⟨ Σ_X w_τ^X · (∂_μ ln b_K^X)(∂^μ ln b_K^X) ⟩_τ,                         (3)

where ⟨·⟩_τ denotes the rule-type-structural average (proper-time average along γ_K + rule-type-canonical bandwidth normalisation).

The logarithmic derivative ∂_μ ln b is chosen because:
- It is invariant under overall rescaling of b (which is chain-specific initial-condition data, not rule-type-structural).
- It has units of inverse length / inverse time, so its Lorentz-square has units of [time]^{-2}.
- It localises the spectral content of b_K^X to its **structural rate of variation**, not its amplitude.

Then by §3.1:

  **σ_τ = ℏ · √Ω_τ²  =  ℏ · √( Σ_X w_τ^X · ⟨ (∂ ln b^X)² ⟩_τ ).**                (4)

Equation (4) is the candidate formula for the bandwidth signature.

### 3.4 What (4) does and does not capture

**Captures:**
- Dimensional correctness ([energy]).
- Lorentz scalar form.
- Independence from overall b-amplitude (via logarithmic derivative).
- Rule-type-specific weighting via w_τ^X.
- Additivity across the four bands.

**Does not capture (yet):**
- Specific values of w_τ^X (rule-type data; these are Lever L1 outputs, see §4).
- Spin / Lorentz-rep dependence (L2): does the (j_L, j_R) representation modify σ_τ? Currently absent from (4); see §5.
- Interface Fierz dependence (L3): does the γ^5-class vs. scalar-class affect σ_τ? Absent; §5.
- Statistics-class (L4) dependence: does Case P vs. R differ? Examined in §6.

So (4) is a **first-pass** scalar; it captures the bandwidth-spectral content but leaves rule-type taxonomy levers L2–L4 to be folded in.

---

## 4. Status of the band weights w_τ^X

### 4.1 Primitive-level constraints on w_τ^X

The rule-type bandwidth-partition weights w_τ^X (Lever L1) satisfy:

(W1) w_τ^X ≥ 0 (bandwidths are non-negative).
(W2) Σ_X w_τ^X = 1 (normalisation; w is a probability distribution over bands).
(W3) For Case R, w_τ^adj > 0 (adjacency must be active for individuation pairing — required by R.2.5 §3 MB discharge).
(W4) For massless candidates, w_τ^com → 0 (no commitment in the rest frame — see §6 below).

(W1), (W2) are FORCED by Primitive 04. (W3) is FORCED by R.2.5 closure. (W4) is **CANDIDATE** — a structural conjecture about how masslessness arises, evaluated in Stage M.1.2.

### 4.2 What is forced vs. inherited

**FORCED:** The functional form (4) — bandwidth signature is a weighted sum of band-spectral-rate squares. The four bands and their non-negativity are primitive content.

**INHERITED:** The actual values of w_τ^X for any specific rule-type. These come from rule-type empirical data (which τ is the electron-like rule-type? which τ is the photon-like? what are their band partitions?). ED structure does not pick out a specific point in the (w^int, w^adj, w^env, w^com)-simplex.

**CANDIDATE:** The specific form of the spectral-rate average ⟨(∂ ln b^X)²⟩_τ. The logarithmic-derivative choice in §3.3 is structurally motivated but not uniquely forced; alternative scalar invariants (e.g., the Laplacian ⟨(□ ln b^X)⟩_τ, or higher-order combinations) could in principle compete. Selection criteria in §7.

---

## 5. Folding in L2 and L3 (spin and Fierz dependence)

### 5.1 Why spin might enter

For Case R rule-types, the participation measure is spinor-valued, and the relevant amplitude squared is Ψ̄Ψ rather than Ψ*Ψ. The spinor inner-product is signature-(2,2) on the 4-component module — i.e., it is **not** positive-definite. So the natural Case-R generalisation of b = |P|² is

  b^R_K = Ψ̄_K Ψ_K,                                                            (5)

which can be positive, negative, or zero. The four-band decomposition (1) then needs to be interpreted as a decomposition of the **scalar bilinear** Ψ̄_K Ψ_K, not of |Ψ|².

**Consequence:** σ_τ for Case R inherits the sign structure of Ψ̄Ψ. Massless Case-R rule-types correspond to Ψ̄Ψ = 0, which is the chiral / Weyl condition.

### 5.2 Fierz class

For Case R, the rule-type's interface couples through a specific Γ_τ from {𝟙, γ^μ, σ^{μν}, γ^μγ^5, γ^5}. The relevant scalar bilinear depends on Γ_τ:

- Γ = 𝟙 → Ψ̄Ψ (scalar mass term, "Dirac mass").
- Γ = γ^5 → Ψ̄γ^5Ψ (pseudoscalar; chiral-symmetry-breaking).
- Other Γ → tensorial; not a pure scalar mass term.

**FORCED:** σ_τ for Case R depends on Γ_τ via the structure of which bilinear realises the rest-frame "mass" content. Different Γ_τ produce different mass-term structures (Dirac vs. Majorana vs. chiral).

**Provisional Case-R refinement of (4):**

  σ_τ^{Case R} = ℏ · √( Σ_X w_τ^X · ⟨ (∂ ln |Ψ̄ Γ_τ Ψ|^X )² ⟩_τ ),               (6)

where the absolute value handles the sign-indefiniteness and the band index X applies to the Γ_τ-bilinear's four-band decomposition. This is a CANDIDATE refinement; uniqueness not established.

### 5.3 Case-P refinement

For Case P, b = |Ψ|² is positive-definite scalar (or for higher integer spin, Ψ_{μ...} Ψ^{μ...} appropriately contracted). Equation (4) applies directly:

  σ_τ^{Case P} = ℏ · √( Σ_X w_τ^X · ⟨ (∂ ln b^X)² ⟩_τ ).                         (7)

No Fierz-class subtlety; the scalar bilinear is unambiguous.

### 5.4 Spin-rep contribution

The (j_L, j_R) representation does not modify (4)/(7) directly — σ_τ is built from a Lorentz-scalar bilinear, and the Lorentz-rep content has been "consumed" in forming that scalar. Spin enters σ_τ only **indirectly**, via:
- Whether the rule-type is Case P or Case R (affecting which bilinear is used).
- Whether the rule-type permits a chiral / massless structure (affecting which Γ_τ are admissible).
- The dimensionality and sign-structure of the bilinear (affecting whether σ_τ = 0 is structurally accessible).

This is consistent with the empirical observation that spin alone does not determine mass (s = 1/2 fermions span 12 orders of magnitude in m).

---

## 6. Massless rule-types and Case P / Case R distinction

### 6.1 When can σ_τ = 0?

From (4)/(6)/(7), σ_τ = 0 iff the weighted spectral-rate sum vanishes:

  Σ_X w_τ^X · ⟨(∂ ln b^X)²⟩_τ = 0.                                              (8)

Since each ⟨(∂ ln b^X)²⟩_τ ≥ 0 (Lorentz-square of a four-vector with appropriate signature; in the rest frame it reduces to the non-negative time-derivative square plus spatial-gradient square), each term is non-negative. The sum vanishes iff **each non-zero-weighted term vanishes**:

  For all X with w_τ^X > 0: ⟨(∂ ln b^X)²⟩_τ = 0.                                (9)

(9) means the rule-type's bandwidth content in each active band has vanishing spectral rate of variation in the rest frame — i.e., b^X is structurally constant along γ_K. This is the **structurally massless condition**.

### 6.2 Hypothesis MΛ — massless = no commitment + no internal evolution

A natural reading of (9): a rule-type is massless iff its bandwidth content does not commit (w^com = 0) **and** its internal content has no rest-frame evolution rate (⟨(∂ ln b^int)²⟩ = 0).

This is the **massless candidate condition** for Arc M:

  σ_τ = 0  ⟺  (no rest-frame commitment) AND (no rest-frame internal evolution). (Mλ)

For photon-like rule-types: no rest frame exists (lightlike worldline), so the construction (4) needs a lightlike-frame analogue; in that frame, the rule-type's "rest" energy is zero by construction. This is consistent — photons satisfy Mλ trivially because (9) holds vacuously when no rest frame exists.

For massive rule-types: a rest frame exists, and at least one ⟨(∂ ln b^X)²⟩_τ > 0 in that frame, giving σ_τ > 0.

**Status:** Mλ is CANDIDATE. Stage M.1.2 will evaluate whether it is FORCED for specific rule-type classes (gauge bosons) or merely consistent.

### 6.3 Case P vs. Case R — structural difference

Both Case P and Case R can in principle have σ_τ > 0 or σ_τ = 0:

- **Case P, σ_τ > 0:** massive bosons (W, Z, Higgs analogue).
- **Case P, σ_τ = 0:** massless bosons (photon, gluon, graviton-like).
- **Case R, σ_τ > 0:** massive fermions (electron, quarks, neutrinos with non-zero mass).
- **Case R, σ_τ = 0:** massless fermions (Weyl fermions; chiral-only structure).

So neither statistics class is structurally forced to be massive or massless. The L4 lever (η = ±1) is independent of the σ_τ = 0 question.

**FORCED:** Statistics class does not determine masslessness. This is consistent with empirical data (massless gauge bosons exist; massless fermions are theoretically permitted as Weyl spinors).

### 6.4 Asymmetry between Case P and Case R re: massless structure

There is, however, one structural asymmetry. For Case R, the chiral condition Ψ̄Ψ = 0 (Weyl spinor) is a clean primitive-level statement: the participation measure lives on a (1/2, 0) or (0, 1/2) sub-module instead of the full (1/2, 0) ⊕ (0, 1/2). For Case P, masslessness corresponds to a gauge-symmetry condition (e.g., U(1) gauge invariance for photons) which has a different structural origin.

This difference flags that σ_τ = 0 has **two distinct primitive-level realisations**:

(MR-R) Case R massless: chirality-projection on the spinor module.
(MR-P) Case P massless: gauge-symmetry constraint on the integer-spin module.

Both are CANDIDATE; the construction in this memo does not pick between them.

---

## 7. Provisional formula and selection criteria

### 7.1 Provisional master formula

Combining (4), (6), (7):

  **σ_τ  =  ℏ · √( Σ_X w_τ^X · ⟨ (∂_μ ln b_τ^X)(∂^μ ln b_τ^X) ⟩_τ )**            (M)

with b_τ^X interpreted as:
- Case P: the four-band-decomposed scalar |Ψ|² (or appropriate higher-spin bilinear).
- Case R: the four-band-decomposed |Ψ̄ Γ_τ Ψ| with Fierz element Γ_τ.

This is the candidate bandwidth signature, denoted (M) for "master".

### 7.2 Why this form (selection criteria)

The functional form (M) is selected over alternatives because:

(SC1) **Lorentz scalar:** ∂_μ X · ∂^μ X is the simplest Lorentz scalar built from a scalar field's gradient.
(SC2) **Amplitude-invariant:** logarithmic derivative removes overall b-rescaling, isolating structural content.
(SC3) **Dimensionally correct:** [(∂ ln b)²] = [length]^{-2} ⇒ ℏ × √· has units [energy] (after c-factors absorbed in metric signature).
(SC4) **Band-additive:** rule-type weights are linear in w^X, respecting the four-band decomposition's additivity.
(SC5) **Massless-permitting:** σ_τ = 0 is reachable cleanly via condition (9).
(SC6) **Statistics-agnostic structurally:** identical functional form for Case P and Case R, with rule-type data distinguishing them via Γ_τ choice.

These criteria select (M) but do not uniquely fix it. Alternative candidates rejected:

(R1) σ_τ = ℏ · ⟨ □ ln b^X ⟩_τ — second-order Laplacian; dimensionally wrong (need [time]^{-1}, this gives [length]^{-2}).
(R2) σ_τ = ℏ · Σ w^X ⟨ (∂_t ln b^X) ⟩_τ — first-order time-derivative; not Lorentz-invariant (frame-dependent).
(R3) σ_τ = ℏ · Σ w^X · |Ψ|² · (rate) — explicit amplitude dependence; violates SC2.

### 7.3 What stays open

(M) leaves open:
- Specific values of w_τ^X (inherited per rule-type).
- Specific values of ⟨(∂ ln b^X)²⟩_τ (inherited from chain-specific initial conditions on b).
- Whether (M) reproduces empirical mass values for any known rule-type (Stage M.1.4 evaluation).
- Whether the logarithmic-derivative choice is the unique correct one (no derivation forces it).

These are honest gaps. (M) is a **provisional** structural object; its job is to give M.1.2 and M.1.3 a concrete formula to test.

---

## 8. FORCED / CANDIDATE / inherited / SPECULATIVE

### 8.1 FORCED

- **F1.** σ_τ exists as a Lorentz-scalar functional of the four-band content. (§3.2)
- **F2.** σ_τ has units of energy via ℏ × frequency. (§3.1)
- **F3.** σ_τ is independent of overall bandwidth amplitude (achievable via log-derivative). (§3.3, SC2)
- **F4.** Case P uses scalar bilinear; Case R uses Fierz-class-specific bilinear. (§5)
- **F5.** Spin alone does not determine σ_τ. (§5.4, §6.3)
- **F6.** σ_τ = 0 is structurally permitted for both Case P and Case R. (§6.3)

### 8.2 CANDIDATE

- **C1.** Specific functional form (M) — log-derivative of band content, weighted, Lorentz-squared. Structurally motivated by SC1–SC6 but not uniquely forced.
- **C2.** Hypothesis Mλ: σ_τ = 0 ⟺ no rest-frame commitment AND no internal evolution. (§6.2)
- **C3.** Refined Case-R formula (6) using |Ψ̄Γ_τΨ| as the relevant bilinear. Specific choice of Γ_τ per rule-type is rule-type data, not structural.
- **C4.** Two distinct massless realisations (MR-R chiral, MR-P gauge); both available; neither structurally forced to be the canonical one. (§6.4)

### 8.3 Inherited

- **I1.** Values of w_τ^X per rule-type.
- **I2.** Values of ⟨(∂ ln b^X)²⟩_τ — depend on chain-specific bandwidth initial conditions.
- **I3.** Specific Γ_τ for Case R rule-types.
- **I4.** Numerical mass scale ℏ × frequency for any specific rule-type.

### 8.4 SPECULATIVE

- **S1.** (M) is the unique correct bandwidth signature. (No proof; selection criteria are not exhaustive.)
- **S2.** Mass hierarchies emerge from systematic patterns in w_τ^X across rule-types. (No mechanism identified.)
- **S3.** Generation structure relates to a third, currently-uncharacterised structural lever beyond L1–L4. (Pure speculation.)

---

## 9. Dependency on later sub-stages

### 9.1 Hand-off to Stage M.1.2

Stage M.1.2 (`massless_rule_types.md`) will use (M) and Mλ to evaluate:
- Whether σ_τ = 0 is structurally forced for any rule-type class, or merely consistent.
- The two realisations MR-R (chiral) and MR-P (gauge) — whether ED primitives pick out one as canonical.
- Whether photon-like and graviton-like rule-types have a primitive-level structural identification.

### 9.2 Hand-off to Stage M.1.3

Stage M.1.3 (`mass_ratio_constraints.md`) will use (M) to evaluate:
- Whether systematic differences in w_τ^X across rule-types of the same taxonomy class produce structural mass-ratio constraints.
- Whether (M) reproduces any empirical mass ratios (e.g., m_μ/m_e or m_p/m_e) under any natural choice of w-pattern.
- Whether ED can support generation structure (3 copies of fermions) without ad-hoc input.

### 9.3 Hand-off to Stage M.1.4 (contingent)

Stage M.1.4 (`mass_signature_identity.md`) will evaluate, contingent on M.1.2 + M.1.3 outcomes, whether the conjectured identity m_τ = σ_τ / c² can be promoted from CANDIDATE to FORCED.

---

## 10. Cross-references

- Upstream: `chain_mass_scoping.md`, `rule_type_taxonomy_synthesis.md`, `dirac_emergence.md`, `klein_gordon_emergence.md`.
- Phase-1 mass anchoring: `u3_evolution_derivation.md` (Madelung anchor).
- Downstream placeholders: `massless_rule_types.md` (M.1.2), `mass_ratio_constraints.md` (M.1.3), `mass_signature_identity.md` (M.1.4), `chain_mass_synthesis.md` (M.2).

---

## 11. One-line summary

**Stage M.1.1 constructs the candidate bandwidth signature σ_τ = ℏ · √(Σ_X w_τ^X · ⟨(∂ ln b_τ^X)²⟩_τ) — a Lorentz-scalar, amplitude-invariant, four-band-additive functional of rule-type bandwidth content; Lorentz-scalar form is FORCED, log-derivative spectral-rate choice is CANDIDATE, per-rule-type weights and amplitudes are inherited; Case P and Case R realisations both permit σ_τ = 0 via two distinct primitive-level routes (chiral projection vs. gauge constraint), feeding Stage M.1.2 and M.1.3 with a concrete object to evaluate.**
