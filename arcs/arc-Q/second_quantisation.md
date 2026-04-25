# Second Quantisation

**Stage Q.7 — Arc Q Sub-Memo**
**Status:** Foundational evaluation memo. Headline closures: **R-1 (lightlike worldlines) CLOSED via dispersion-relation argument from σ_τ = 0 + Stage R.1 Casimir.** **R-5 (vacuum/particle status) PARTIALLY CLOSED** — dual vacuum-field-plus-particle-excitation structure for τ_g is structurally admissible at primitive level; full primitive-level vacuum structure deferred to Q.8. **UV-FIN CANDIDATE PROMOTED to STRONG** but not yet FORCED — Primitive 01 event-discreteness provides a genuine natural cutoff at primitive level; rigorous demonstration that all multi-chain participation integrals are finite requires Q.8 vacuum closure. **G4 (vacuum-anchored generation labelling) remains DEFERRED** — Q.7 framework alone insufficient. **Schwinger sign of g − 2 remains CANDIDATE** with vertex-topology argument plausible but not derived. **GRH refinements: 4 of 5 CLOSED; only R-5 remains PARTIAL pending Q.8.**

---

## 1. Goal

Stage Q.7 is, alongside Q.1, the most foundational substage of Arc Q. It closes:

- **R-1 (lightlike worldline reformulation):** how propagation along null worldlines is structurally realised for σ = 0 rule-types.
- **R-5 (vacuum/particle status):** whether τ_g is a vacuum field with particle excitations, a particle-class rule-type, or both.

It also evaluates:

- **UV-FIN (C-Q5.1):** primitive event-discreteness as natural UV cutoff.
- **G4 (vacuum-anchored generation labelling):** whether vacuum structure differentiates same-quantum-number rule-types.
- **Schwinger-sign CANDIDATE (C-Q5.2):** whether one-loop g − 2 sign is structurally derivable.

The driving question:

(Q-2Q) What is the ED analogue of second quantisation — and does it admit, force, or refute the conventional QFT structure (Fock space, creation/annihilation operators, vacuum state)?

The expected pattern (from Q.0 §5.1): Q.7 is moderate-high feasibility; spin-statistics from R.2.5 already FORCES the (anti-)commutation structure, so assembly into the QFT framework is largely structural. This is potentially Arc Q's strongest positive-content substage.

---

## 2. Inputs

### 2.1 From Q.1–Q.6

- GRH CANDIDATE-STRONG; R-2, R-3, R-4 closed; R-1, R-5 to be closed here.
- U(1) FORCED; SU(N) admissible.
- Vertex catalogue (Q.3); vertex-anchored commitment (R-3 closed).
- Higgs SSB admissible structurally (Q.4).
- Radiative corrections admissible; UV-FIN CANDIDATE (Q.5).
- Multi-generation structure admissible via L1/L3 (Q.6); G4 DEFERRED here.

### 2.2 From Stage R.2

- Spin-statistics theorem η = (−1)^{2s} FORCED.
- Cl(3,1) frame, Fierz basis.
- π_1 = ℤ_2 in 3+1D; anyons forbidden.

### 2.3 From Stages R.1, R.3

- Lorentz-covariant participation measure, Klein-Gordon, Dirac equations.
- Mass-shell condition P_μ P^μ = m²c² (Stage R.1 Casimir).

### 2.4 From Arc M

- σ_τ = 0 admissible structurally for both Case P (MR-P) and Case R (MR-R).
- m_τ inherited per rule-type.

### 2.5 From Phase-1

- Participation measure P_K(x, t) = √b_K · e^{iπ_K} primitive-level.
- Multi-chain participation already implicit at single-chain Phase-1 level (Bell correlations).

---

## 3. Structural framework

### 3.1 What is a "field" in ED's rule-type ontology?

A **field** in ED is the participation measure of a rule-type τ evaluated as a function of the event-manifold coordinate x^μ:

  Φ_τ(x) = participation-measure value at x for rule-type τ,                  (1)

with the structural realisation:

- For Case-P scalar: Φ_τ(x) = √(b_τ(x)) · e^{iπ_τ(x)} (Stage R.1).
- For Case-R Dirac: Φ_τ(x) = Ψ_τ(x) ∈ Cl(3,1) spinor module (Stage R.3).
- For Case-P vector (gauge): Φ_τ(x) = A^a_μ(x) (GRH).

Multi-chain content arises from **summing over chain insertions** at each event:

  Φ_τ(x) = Σ_{K ∈ τ} P_{K,τ}(x).                                              (2)

Each chain K of rule-type τ contributes a participation amplitude at every event in its support. The sum (2) is the field-as-multi-chain-superposition.

This is **not** a postulate — it is the natural primitive-level extension of Phase-1's coherent-sum Ψ = Σ_K P_K (which produced the Schrödinger emergence) to relativistic / multi-rule-type content.

### 3.2 What is a "vacuum" in ED?

The vacuum state |0⟩_τ for rule-type τ is the configuration with **no chains of rule-type τ committed** in any region of the event manifold:

  |0⟩_τ ⟺ no τ-chain has crossed individuation threshold (Primitive 10) in the region.

Equivalently: b_τ = 0 throughout the region, meaning no participation amplitude has been allocated to τ.

**This is structurally well-defined at primitive level** — the absence of τ-chains is a definite state of the bandwidth-field manifold. It is not a "fluctuating sea" in the Dirac-sea sense; it is the absence-of-commitment configuration.

### 3.3 Creation and annihilation events

**Chain-creation event:** a participation amplitude P_τ crosses the Primitive 10 individuation threshold from b_τ < threshold to b_τ ≥ threshold at some event x. This is the structural realisation of a "creation operator" acting on |0⟩_τ.

**Chain-annihilation event:** the inverse — participation amplitude drops below threshold; an existing chain "decommits" out of identifiable existence at event x. This is the "annihilation operator."

**Primitive evaluation.**

- **Primitive 01 (micro-event):** chain-creation and chain-annihilation are point-events on the event manifold. **Compatible.**
- **Primitive 10 (individuation):** threshold-crossing structure is exactly the create/annihilate event-class. **Compatible.**
- **Primitive 11 (commitment):** commitment events along the new/old chain anchor the create/annihilate transitions. **Compatible.**
- **Conservation:** total bandwidth content is locally conserved (Primitive 04 + flux-continuity); creation-annihilation in pairs respects this.

**Status:** Creation/annihilation structure is **structurally clean** at primitive level. No external operator-formalism required — the structure emerges from primitives 01 + 10 + 11.

### 3.4 (Anti-)commutation from spin-statistics

For a Case-R rule-type, two chain-creation events at the same event point would require two chains to coincide, which Primitive 10 individuation excludes (M.1.2 §4.1, vanishing-on-coincidence). This forces the chain-creation operators to **anticommute**:

  {a^†_τ(x), a^†_τ(x')} ∝ δ⁴(x − x') × 0 = 0     for Case R, x = x'.            (3)

For Case P, coincidence is admissible; chain-creation operators **commute**:

  [a^†_τ(x), a^†_τ(x')] = 0     for Case P.                                   (4)

These are the **canonical (anti-)commutation relations** of QFT, derived here directly from R.2.5 spin-statistics + Primitive 10. **FORCED.**

---

## 4. Closure of refinement R-1 (lightlike worldlines)

### 4.1 The problem

Stage Q.1 §3.1 flagged that GRH-4 (σ_{τ_g} = 0) implies τ_g's worldline is lightlike, but Primitive 13's proper-time relational timing degenerates on lightlike worldlines (dτ = 0). The Stage R.1 commitment-rate construction along γ_K assumed a timelike worldline; the lightlike case requires reformulation.

### 4.2 Dispersion-relation argument

Stage R.1 derived the Klein-Gordon Casimir P_μ P^μ = m²c². For σ_τ = 0 (and identifying mc² with σ_τ via the inherited m = σ/c²):

  P_μ P^μ = 0                                                                  (5)

— the **massless dispersion relation**. On the event manifold, a particle satisfying (5) propagates along a **lightlike (null) worldline**: the four-momentum is light-like, and the worldline tangent u^μ ∝ P^μ is light-like.

This is **structurally forced** for any σ = 0 rule-type. No additional postulate required — (5) is the σ = 0 specialisation of Stage R.1's Casimir.

### 4.3 Lightlike-affine-parameter reformulation

For commitment events along a lightlike worldline, replace proper-time τ with a **lightlike affine parameter** λ defined by:

  dx^μ / dλ = P^μ,     P^μ light-like.                                        (6)

λ is well-defined and increasing along the worldline (parametrising distance in a Lorentz-invariant manner up to affine reparametrisation).

**Commitment events for lightlike rule-types:** anchored by λ-positions along γ_{τ_g}, but per Q.3 §3.2 R-3 closure, all such commitment events are **vertex-anchored** (occurring only at interaction vertices with charged matter). So the lightlike-affine-parameter primarily indexes propagation between vertices, not intrinsic commitment.

### 4.4 R-1 closure

| Sub-claim | Status |
|-----------|--------|
| σ = 0 ⇒ null dispersion P²= 0 | **FORCED** (Stage R.1 Casimir) |
| Null dispersion ⇒ lightlike worldline | **FORCED** (Lorentz geometry) |
| Lightlike-affine-parameter reformulation admissible | **FORCED** (standard differential geometry) |
| Vertex-anchored commitment for τ_g consistent with λ-parametrisation | **FORCED** (R-3 carryover) |

**R-1: CLOSED.** Lightlike propagation is FORCED for σ = 0 rule-types via the structural chain GRH-4 → R.1 Casimir → null dispersion → lightlike worldline → λ-affine reformulation.

---

## 5. Closure of refinement R-5 (vacuum/particle status)

### 5.1 The problem

Stage Q.1 §6.4 flagged R-5: is τ_g a "vacuum-occupying" rule-type whose participation field A_μ is a global background structure, or a "particle-like" rule-type whose participation is concentrated near interactions, or both?

### 5.2 Dual structure at primitive level

Apply the §3 framework to τ_g:

- **Vacuum sector |0⟩_{τ_g}:** no τ_g-chains committed anywhere. b_{τ_g} = 0, A_μ = 0 (or pure-gauge equivalent under R-2 closure).
- **Single-particle sector:** one τ_g-chain committed, propagating lightlike between vertices. Identified phenomenologically with a single photon.
- **Multi-particle sector:** multiple τ_g-chains, each lightlike, possibly interacting via quartic gauge self-coupling (for non-Abelian) or via charged-matter loops.

**Both vacuum and particle states are structurally admissible** in the primitive-level Fock-space-like framework. τ_g supports a vacuum (no-commitment configuration) and excitations (committed chains), exactly as conventional QFT does.

### 5.3 Is the vacuum structurally trivial?

A subtlety: even with no τ_g-chains committed, **virtual transient participations** of τ_g in the bandwidth-environment band b^env of charged matter rule-types are present whenever charged matter is committed. These produce the Q.5 vacuum-polarisation effects and the QFT zero-point fluctuations.

So the τ_g vacuum is:

- **Strict vacuum** (no committed chains): the absence-of-commitment state.
- **Effective vacuum in physical situations** (charged matter present): includes transient τ_g-participation in b^env of charged rule-types.

The QFT vacuum |0⟩_QFT corresponds to the **effective** vacuum: the lowest-energy state of the multi-rule-type system, which is not the strict zero-participation state because charged matter contributes zero-point fluctuations of the gauge field via b^env.

### 5.4 R-5 closure status

| Sub-claim | Status |
|-----------|--------|
| τ_g admits a vacuum sector | **FORCED** (§3.2) |
| τ_g admits particle excitations | **FORCED** (§3.3) |
| Dual vacuum-and-particle nature is structural | **FORCED** |
| Effective vacuum carries zero-point contributions from charged-matter b^env | **CANDIDATE** (depends on Q.8 vacuum-structure detail) |
| Vacuum-anchored SSB (H5) becomes viable | **CANDIDATE** (depends on Q.8) |

**R-5: PARTIALLY CLOSED.** Vacuum + particle structure structurally admissible at Q.7 level; full vacuum-structure characterisation (including effective-vacuum content, H5 evaluability, zero-point regularisation detail) deferred to Q.8.

---

## 6. UV-FIN evaluation

### 6.1 The CANDIDATE statement

From Q.5 §7.3: ED's primitive event-manifold discreteness (Primitive 01) provides a natural UV cutoff. Multi-chain participation integrals at primitive level are finite. UV divergences in QFT are continuum-approximation artefacts.

### 6.2 Structural argument for UV-FIN

Three primitive-level supports:

**(SUP-1) Primitive 01 discreteness.** Micro-events are discrete on the event manifold. The "continuum" of event-manifold points is an emergent / approximate description; primitive-level integrals over event-manifold variables are sums over discrete micro-events.

**(SUP-2) Primitive 13 finite proper-time intervals.** Proper-time intervals between commitment events are non-zero and finite. There is no zero-time-interval limit at primitive level.

**(SUP-3) Bandwidth finiteness per rule-type.** The total bandwidth Σ_τ b_τ is finite per event (Primitive 04 implies bounded-above bandwidth content). Multi-chain participation integrals weighted by bandwidth are bounded.

These three together mean: any primitive-level multi-chain participation integral is over a discrete, finite-step, bounded-amplitude domain. Such integrals are **automatically finite**.

### 6.3 Continuum approximation produces apparent divergences

In the continuum limit (where Primitive 01 discreteness is approximated as smooth manifold structure), the discrete sum becomes a continuous integral. If the integrand is not bounded by a cutoff, the integral can diverge — these are the UV divergences of conventional QFT.

**Resolution under UV-FIN:** the divergences arise because the continuum integral over-extends beyond the actual primitive-level domain. The cutoff is **physical** (Primitive 01 event-discreteness scale), not an artificial regularisation parameter.

### 6.4 Promotion status

UV-FIN was CANDIDATE at Q.5. Q.7's structural framework provides three independent supports (SUP-1 through SUP-3). This is **strong evidence** for primitive-level UV finiteness, but not yet a rigorous derivation.

**Promotion:** UV-FIN promoted to **CANDIDATE-STRONG** at Q.7. Full FORCED promotion requires:

- Q.8 vacuum-structure closure to demonstrate finite zero-point contributions explicitly.
- A rigorous derivation that any specific multi-chain participation integral is finite at primitive level.

### 6.5 Schwinger-sign CANDIDATE (C-Q5.2)

Q.5 §5.4 flagged the one-loop QED g − 2 sign as CANDIDATE for derivation. The sign comes from:

(i) Vertex-topology of photon-electron-photon insertion.
(ii) Propagator iε prescription giving specific sign of imaginary part.
(iii) Trace over Dirac matrices.

In ED's primitive-level framework:

- Vertex topology is the primitive-level multi-chain insertion pattern (R-3 closed).
- Propagator iε corresponds to forward-in-time commitment-event ordering (Primitive 11 + Primitive 13 timing).
- Dirac trace is Cl(3,1) algebra (R.2.4).

All three components are admissible at primitive level. The **sign** of g − 2 emerges from these combined; in principle derivable, in practice the QFT calculation is complex and ED's derivation tracks it step-for-step.

**Status:** Schwinger sign is **structurally derivable in principle** at Q.7 level. Concrete derivation would require executing the multi-chain integral explicitly. Not done here; flagged for possible Q.synthesis or future work. **Promoted from CANDIDATE to CANDIDATE-PLAUSIBLE.**

### 6.6 Asymptotic-freedom sign

Similar argument applies to the SU(3) β-function sign. The 11N/3 − 2N_f/3 calculation has primitive-level analogues (gauge self-coupling vs matter loops are both admissible per Q.3 + Q.5). The **sign of N**et contribution depends on the relative magnitudes, which is QFT-loop-integral content.

**Status:** Asymptotic-freedom sign remains CANDIDATE at Q.7. Likely INHERITED at Arc Q closure unless explicit derivation executed.

---

## 7. G4 evaluation (vacuum-anchored generation labelling)

### 7.1 The question

Q.6 deferred G4 to Q.7 / Q.8. Question: can vacuum structure structurally differentiate same-(s, statistics, gauge-rep) rule-types?

### 7.2 Q.7-level evaluation

The vacuum-as-no-commitment-configuration framework of §3.2 admits multiple **vacuum sectors** if there are distinct stable absence-of-commitment configurations. Examples:

- θ-vacua: continuous family of CP-violating vacua labelled by an angle (analogue exists in QCD).
- SSB vacua: multiple equivalent symmetry-broken ground states (continuous family for U(1) SSB; discrete for ℤ_n).

Could **different vacuum sectors** correspond to different generations of the same rule-type?

**Difficulty:** generations have different *masses* — i.e., different σ_τ values — but in ED the σ_τ master formula depends on rule-type data (w_τ^X) and chain-initial-condition data, not on vacuum sector. Vacuum sector affects the *expectation values* of fields in a sector, not the rule-type-level σ_τ formula itself.

For G4 to work, vacuum-sector dependence would need to feed back into σ_τ — e.g., via H2-style spatially-patterned bandwidth condensate that differs per sector. This is structurally non-trivial.

**Status:** **G4 remains DEFERRED at Q.7.** Structural framework for vacuum sectors admissible, but the connection to σ_τ differentiation per sector is not derivable at Q.7 level. Q.8 may close partially, but the dominant verdict expected: G4 is structurally admissible-as-labelling but does not produce mass-differentiation. Generation count remains EMPIRICAL.

---

## 8. FORCED / CANDIDATE / REFUTED table

### 8.1 Per-claim

| Claim | Status |
|-------|--------|
| Multi-chain field structure exists at primitive level | **FORCED** (§3.1) |
| Vacuum state defined as no-commitment configuration | **FORCED** (§3.2) |
| Creation/annihilation events from individuation-threshold crossings | **FORCED** (§3.3) |
| (Anti-)commutation relations from spin-statistics + individuation | **FORCED** (§3.4) |
| Lightlike worldlines for σ = 0 rule-types | **FORCED** (R-1 closure §4) |
| τ_g admits dual vacuum + particle structure | **FORCED** (§5) |
| Effective vacuum = strict vacuum + zero-point b^env contributions | **CANDIDATE** (Q.8 detail) |
| H5 (vacuum-anchored Higgs) viable | **CANDIDATE** (Q.8 detail) |
| UV-FIN (primitive-level UV cutoff) | **CANDIDATE-STRONG** (§6) |
| Schwinger sign structurally derivable in principle | **CANDIDATE-PLAUSIBLE** (§6.5) |
| Asymptotic-freedom sign structurally derivable | **CANDIDATE** |
| G4 (vacuum-anchored generation labelling) | **DEFERRED** (Q.8) |
| Anyonic statistics in 3+1D | **REFUTED** (R.2.3 carry-forward) |

### 8.2 Per-mechanism

| Mechanism | Status |
|-----------|--------|
| Fock-space construction at primitive level | **FORCED** (§3) |
| Discrete creation/annihilation event structure | **FORCED** (§3.3) |
| Vacuum state structurally well-defined | **FORCED** (§3.2) |
| Vacuum sectors admissible | **CANDIDATE** (§7) |
| UV-FIN regularisation | **CANDIDATE-STRONG** (§6) |
| Renormalisation as effective machinery | **ADMISSIBLE-as-effective** (Q.5 carryover) |
| Effective-theory loop integrals | **ADMISSIBLE-as-effective** (Q.5 carryover) |

---

## 9. Verdict

### 9.1 What is structurally FORCED at the second-quantisation layer?

- Multi-chain field structure as primitive sum-over-chain-insertions.
- Vacuum state as no-commitment configuration.
- Creation/annihilation operator structure from Primitive 10 threshold crossings.
- Canonical (anti-)commutation relations from R.2.5 spin-statistics + Primitive 10.
- Lightlike worldlines for σ = 0 rule-types (R-1 CLOSED).
- Vacuum + particle dual structure for τ_g (R-5 PARTIALLY CLOSED).
- Anyon prohibition in 3+1D (R.2.3 carry-forward).

### 9.2 What is admissible but not forced?

- Specific vacuum-sector structure (multiple sectors, θ-vacua, etc.).
- UV-FIN as rigorous (not just plausible) primitive-level finiteness.
- H5 (vacuum-anchored SSB) — viable structurally if Q.8 admits non-trivial vacuum.
- Schwinger sign of g − 2 derivable from primitive-level vertex topology (in principle, not executed).
- Asymptotic-freedom sign derivable structurally.
- G4 (vacuum-anchored generation labelling) — admissible-as-labelling but not as mass-differentiation.

### 9.3 What is forbidden?

- Anyonic statistics (R.2.3 carry-forward).
- Loop corrections that violate gauge / Lorentz / locality (Q.5 carry-forward).
- Vacuum states violating Lorentz invariance globally (Lorentz-symmetry-breaking is admissible only as SSB at L3 level, not as global vacuum-structural violation).

### 9.4 What remains empirical?

- All numerical loop-correction coefficients.
- Specific sign / magnitude of g − 2 at one loop (derivable in principle; not executed).
- Specific β-function coefficients.
- Generation count (G4 cannot reduce empirical to structural).
- Higgs-sector specific structure.

### 9.5 Bottom line

Stage Q.7 is Arc Q's strongest positive-content substage. Three major structural achievements:

(a) **R-1 closed:** lightlike worldlines for σ = 0 rule-types FORCED via dispersion-relation argument from Stage R.1 Casimir.

(b) **R-5 partially closed:** vacuum-and-particle dual structure for τ_g structurally admissible at Q.7 level; full vacuum-structure detail deferred to Q.8.

(c) **UV-FIN promoted to CANDIDATE-STRONG:** three independent primitive-level supports (Primitive 01 discreteness, Primitive 13 finite intervals, Primitive 04 bounded bandwidth) for primitive-level UV finiteness.

Plus the canonical (anti-)commutation relations of QFT FORCED from R.2.5 + Primitive 10 — closing the structural assembly of the second-quantisation framework.

### 9.6 What becomes the target for Q.8?

- **Final R-5 closure:** primitive-level vacuum-structure characterisation including zero-point b^env contributions.
- **UV-FIN final verdict:** rigorous demonstration (or refutation) of primitive-level multi-chain participation integral finiteness.
- **H5 final evaluation:** vacuum-anchored Higgs viability.
- **G4 final evaluation:** vacuum-anchored generation labelling.
- **Arc Q synthesis preparation:** Q.8 closes the final substage; synthesis assembles Q.0–Q.8.

---

## 10. GRH refinement status post-Q.7

| Refinement | Pre-Q.7 | Post-Q.7 |
|-----------|---------|----------|
| R-1 (lightlike-worldline) | open | **CLOSED** (§4) |
| R-2 (gauge-quotient individuation) | closed (Q.2) | closed |
| R-3 (vertex-anchored commitment) | closed (Q.3) | closed |
| R-4 (non-Abelian extension) | closed (Q.3) | closed |
| R-5 (vacuum/particle status) | open | **PARTIAL** (§5) |

**Four of five GRH refinements closed; only R-5 remains partial pending Q.8.** Once R-5 closes fully at Q.8, GRH should promote from CANDIDATE-STRONG to **unconditional FORCED**, retroactively promoting M.1.2's F-M8 (massless Case-P rule-type existence) from conditional FORCED to unconditional FORCED.

---

## 11. FORCED / CANDIDATE / REFUTED summary

### 11.1 FORCED

- **F-Q7.1.** Multi-chain field structure Φ_τ(x) = Σ_K P_{K,τ}(x) at primitive level.
- **F-Q7.2.** Vacuum state |0⟩_τ as no-commitment configuration.
- **F-Q7.3.** Creation/annihilation operator structure from Primitive 10 individuation-threshold crossings.
- **F-Q7.4.** Canonical (anti-)commutation relations from R.2.5 + Primitive 10:
  - {a^†_τ, a^†_τ} = 0 (Case R, coincident points).
  - [a^†_τ, a^†_τ] = 0 (Case P).
- **F-Q7.5.** Lightlike worldlines FORCED for σ = 0 rule-types via Stage R.1 Casimir + Lorentz geometry. **R-1 CLOSED.**
- **F-Q7.6.** Lightlike-affine-parameter reformulation admissible.
- **F-Q7.7.** τ_g admits both vacuum and particle states.
- **F-Q7.8.** Vertex-anchored commitment for τ_g consistent with λ-parametrisation (R-3 carryover).
- **F-Q7.9.** Anyon prohibition (R.2.3 carryover).

### 11.2 CANDIDATE

- **C-Q7.1 (UV-FIN, promoted to CANDIDATE-STRONG).** Primitive 01 discreteness + Primitive 13 finite intervals + Primitive 04 bounded bandwidth ⇒ primitive-level UV finiteness. Final FORCED promotion pending Q.8.
- **C-Q7.2 (Schwinger sign, promoted to CANDIDATE-PLAUSIBLE).** One-loop g − 2 sign derivable from vertex topology + commitment-ordering + Cl(3,1) trace structure in principle.
- **C-Q7.3.** Asymptotic-freedom sign for SU(3) derivable structurally (analogous argument).
- **C-Q7.4 (effective vacuum content).** Effective vacuum = strict vacuum + zero-point b^env contributions; specific content Q.8 deliverable.
- **C-Q7.5 (H5 viability).** Vacuum-anchored Higgs admissible if Q.8 admits non-trivial vacuum sectors.
- **C-Q7.6 (vacuum sectors).** Multiple stable no-commitment configurations admissible at Q.7 framework.

### 11.3 REFUTED

- **R-Q7.1.** Anyonic statistics in 3+1D (R.2.3 carryover).
- **R-Q7.2.** Vacuum states violating Lorentz invariance globally.
- **R-Q7.3.** Loop corrections violating gauge / Lorentz / locality (Q.5 carryover).
- **R-Q7.4.** G4 producing primitive-level mass differentiation across generations. (Vacuum-as-labelling is admissible; vacuum-as-mass-source via G4 requires an additional H2-style mechanism.)

### 11.4 INHERITED

- **I-Q7.1.** Specific magnitudes of loop corrections (α-expansion etc.).
- **I-Q7.2.** Specific value of Schwinger correction (numerical magnitude).
- **I-Q7.3.** Specific β-function coefficients.
- **I-Q7.4.** Generation count (Q.6 carryover).
- **I-Q7.5.** Specific Higgs-sector structure (Q.4 carryover).

### 11.5 DEFERRED to Q.8

- **D-Q7.1.** Final R-5 closure — full vacuum-structure characterisation.
- **D-Q7.2.** UV-FIN rigorous derivation / final FORCED promotion.
- **D-Q7.3.** H5 viability final verdict.
- **D-Q7.4.** G4 final evaluation as labelling structure.

---

## 12. Implications for Q.8 and Arc Q synthesis

### 12.1 Q.8 deliverables

Q.8 must close:
- R-5 fully.
- UV-FIN final verdict.
- H5 viability.
- G4 final evaluation.

These are interrelated — all hinge on the primitive-level structure of the no-commitment / effective vacuum.

### 12.2 Arc Q synthesis projection

Post-Q.7, Arc Q's positive structural content is concentrated in:
- Q.1 GRH structure.
- Q.3 vertex catalogue + R-3, R-4 closures.
- Q.6 mixing/CP linear-algebra structure (FORCED admissibility).
- **Q.7 second-quantisation framework (this memo) + R-1 closure + UV-FIN promotion.**

These constitute Arc Q's structurally-positive contributions. Negative content concentrated in Q.2 (SM gauge group), Q.4 (specific Higgs mechanism), Q.5 (numerical loop content), Q.6 (generation count + mixing values).

The **Arc Q synthesis** will integrate both, paralleling Arc M's structure-vs-value separation at QFT scope.

### 12.3 Back-flow to Arc M

R-1 closure does not yet promote F-M8 to unconditional FORCED — R-5 still partial. After Q.8, the chain closes and Arc M back-flow completes.

---

## 13. Cross-references

- Upstream: `generations_and_mixing.md` (Q.6), `radiative_corrections.md` (Q.5 — UV-FIN, Schwinger sign), `higgs_mechanism_scoping.md` (Q.4 — H5), `interaction_vertex_classification.md` (Q.3 — R-3 closure carryover), `gauge_group_scoping.md` (Q.2), `grh_evaluation.md` (Q.1), `dirac_emergence.md` (R.3), `klein_gordon_emergence.md` (R.1 — Casimir for §4), `rule_type_taxonomy_synthesis.md` (R.2.5 — spin-statistics for §3.4).
- Downstream: `vacuum_and_zero_point.md` (Q.8 — closes R-5 fully, finalises UV-FIN, H5, G4), `arc_q_synthesis.md`.
- Refinement tracking: R-1 **CLOSED** (this memo); R-2 closed (Q.2); R-3 closed (Q.3); R-4 closed (Q.3); R-5 **PARTIAL** (this memo, Q.8 to finalise).

---

## 14. One-line summary

**Stage Q.7 closes refinement R-1 (lightlike worldlines FORCED via σ = 0 + Stage R.1 Casimir → null dispersion → null worldline) and partially closes R-5 (τ_g admits both vacuum and particle states structurally), establishes the primitive-level Fock-space framework with creation/annihilation events as Primitive 10 threshold crossings and FORCED canonical (anti-)commutation from R.2.5 spin-statistics + Primitive 10, promotes UV-FIN from CANDIDATE to CANDIDATE-STRONG with three independent primitive-level supports (event-discreteness + finite proper-time intervals + bounded bandwidth), promotes Schwinger sign of g − 2 to CANDIDATE-PLAUSIBLE for in-principle derivation from primitive-level vertex topology, leaves G4 (vacuum-anchored generation labelling) DEFERRED to Q.8 with admissible-as-labelling but not as mass-differentiation, and reduces the open GRH refinement set to a single partial item (R-5) — Q.7 is Arc Q's strongest positive-content substage with form-FORCED structural content concentrated here and the final pieces (Q.8 vacuum closure + Arc Q synthesis) remaining to complete Arc Q.**
