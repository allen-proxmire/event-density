# Paper RQM-T8 — Canonical (Anti-)Commutation Relations

**Series:** Wave-3 Relativistic-QM Bridge — Theorem T8
**Status:** Wave-3 generative paper; M3 verdict at write-time. **FORM-INHERITED + VALUE-INHERITED** (canonical commutation relations are standard-form construction per Paper_095 §2.3; $\hbar$ is INHERITED).
**Companions:** Paper_RQM_T1 (Spin–statistics), Paper_RQM_T7 (Lorentz reps), Paper_002 (Born-Gleason), Paper_063 (E-1 tensor product).

---

## Preamble: What This Paper Does NOT Claim

1. **The 13 primitives are not derived.** They are postulated per Paper_087.
2. **No claim that canonical (anti-)commutation relations are derived in this paper.** Per Paper_095 §2.3, writing down $[\hat{x},\hat{p}] = i\hbar$ and field-operator (anti-)commutation relations is P (definitional standard-form construction). The forms are INHERITED.
3. **No claim that $\hbar$ has a substrate-derived origin.** $\hbar$ enters as the inherited Planck constant — a chain-step participation quantum (inheritance from Paper_087 P10 + P09), not derived here. The "structural origin of $\hbar$" framing in earlier drafts was oversold.
4. **No claim of numerical-content derivation beyond what is explicitly INHERITED.** $\hbar$ value is empirically matched.
5. **No claim that ED is the only consistent substrate ontology.** Other substrate ontologies are conceivable.
6. **No claim of empirical adequacy outside the regime stated in §2.2.** Equal-time vs spacelike (anti-)commutation for relativistic fields (microcausality) is deferred.

---

## Abstract

Paper RQM-T8 identifies the canonical commutation relation $[\hat{x},\hat{p}] = i\hbar$ and the field-operator (anti-)commutation relations as the standard-form QM/QFT operator algebra inherited by substrate-level scalar and spinor rule-types. **The (anti-)commutation forms are P-definitional per Paper_095 §2.3** (standard-form construction); $\hbar$ appears as the inherited Planck constant (chain-step participation quantum inheritance from Paper_087 P10 + P09 + P04 bandwidth-additive structure). The substrate-level content is the identification that the **commutator-vs-anticommutator dichotomy** is forced by T1 spin–statistics: bosonic rule-types satisfy commutators; fermionic rule-types satisfy anticommutators. Heisenberg uncertainty follows downstream from canonical commutation + Cauchy–Schwarz, not as an independent postulate. Verdict tier: **M3** with FORM-INHERITED + VALUE-INHERITED framing. The result joins the Wave-3 Relativistic-QM Bridge family alongside T1 (supplies the dichotomy decision) and T7 (classifies bosonic/fermionic reps). This paper is in the substrate-ontology research-program lineage of 't Hooft, Wolfram, and the causal-set program — not in the operational-reconstruction lineage of Hardy / CDP / Coecke-Kissinger.

---

## §1 Statement of Result

**Claim.** The canonical commutation relation $[\hat{x}, \hat{p}] = i\hbar$ for position-momentum and the canonical anti-commutation relation $\{\hat{\psi}, \hat{\psi}^\dagger\} = \delta$ for fermionic field operators are form-IDENTIFIED (no D rows in audit table; downgraded from FORM-FORCED per Paper_095 §2.3) by the substrate's participation-measure structure (P02) + bandwidth-additive primitive (P04) + adjacency-bandwidth content. The commutator/anticommutator dichotomy is determined by T1's spin–statistics (Paper_RQM_T1) class assignment. The Planck-constant $\hbar$ is INHERITED via empirical matching.

Verdict: **M3**. No new postulates.

---

## §2 Primitive Inputs

### 2.1 Primitives invoked

- **P02 (Participation)** — supplies the participation-amplitude content on which operators act.
- **P03 (Channel + locus indexing)** — supplies the adjacency structure entering canonical relations.
- **P04 (Bandwidth)** — supplies the bandwidth-additive content underlying $\hbar$-normalization.
- **P10 (Rule-type primitive)** — rule-type carriers (scalar / spinor) on which operators act.

### 2.2 Upstream Dependencies

- **I-002:** Born-Gleason rule (Paper_002).
- **I-007:** Hilbert-space emergence as completion of motif algebra.
- **I-063:** Tensor-product structure on bipartite carriers (Paper_063).
- **I-RQM-T1:** Spin–statistics dichotomy.
- **I-RQM-T7:** Lorentz representations (which rep is fermionic vs bosonic).
- **I-Stone:** Standard Stone's theorem.
- **I-CCR:** Standard canonical commutation relations.

---

## §3 Derivation

### 3.1 $[\hat{x}, \hat{p}] = i\hbar$ from participation-measure structure

In standard QM, the canonical commutation relation $[\hat{x}, \hat{p}] = i\hbar$ is the defining feature of the Heisenberg algebra. Substrate-level derivation:

**Step 1: Position operator from P03.** P03 (channel + locus indexing) supplies the locus content. The position operator $\hat{x}$ is the multiplicative operator $\hat{x}\Psi(x) = x\,\Psi(x)$ on the participation amplitude $\Psi(x)$.

**Step 2: Momentum operator from P03 translation-invariance.** P03's spatial-homogeneity content supplies translation invariance of the substrate. By Stone's theorem applied to the one-parameter group of substrate translations (I-Stone), the infinitesimal generator is $\hat{p} = -i\hbar \partial_x$ — the momentum operator. The factor $\hbar$ is INHERITED via empirical matching.

**Step 3: The commutator.** Direct computation:
$$[\hat{x}, \hat{p}]\Psi = \hat{x}(-i\hbar\partial_x\Psi) - (-i\hbar\partial_x)(\hat{x}\Psi) = -i\hbar x\partial_x\Psi + i\hbar\partial_x(x\Psi) = i\hbar\Psi .$$

Therefore $[\hat{x}, \hat{p}] = i\hbar$.

**Step 4: Substrate origin of $\hbar$.** $\hbar$ enters in step 2 as the rate constant connecting infinitesimal translation generators to substrate-level momentum content. By P04 (bandwidth-additive structure), the substrate-level participation budget per unit translation has dimensions of action; the empirical value of $\hbar$ matches this rate.

The substrate framework does not derive $\hbar$'s numerical value from first principles. It supplies the **structural form** $[\hat{x}, \hat{p}] = i\hbar$; the constant is empirically matched.

### 3.2 Canonical (anti-)commutation for field operators

For quantum field operators $\hat{\psi}(x)$, the dichotomy fermionic / bosonic determines whether the canonical relation is commutator or anticommutator:

**Bosonic fields** (scalar, vector, ...) satisfy
$$[\hat{\psi}(x), \hat{\psi}^\dagger(x')] = \delta^3(x - x') ,$$
$$[\hat{\psi}(x), \hat{\psi}(x')] = 0 .$$

**Fermionic fields** (spinor, ...) satisfy
$$\{\hat{\psi}(x), \hat{\psi}^\dagger(x')\} = \delta^3(x - x') ,$$
$$\{\hat{\psi}(x), \hat{\psi}(x')\} = 0 .$$

The substrate origin of the commutator-vs-anticommutator distinction:

**Step 1: Spin–statistics from T1.** Paper_RQM_T1 establishes $\eta = (-1)^{2s}$ as the exchange phase. Bosonic fields ($\eta = +1$): exchange preserves sign. Fermionic fields ($\eta = -1$): exchange flips sign.

**Step 2: Multi-quantum participation structure.** Multiple identical-rule-type quanta carry tensor-product participation amplitudes (Paper_063 E-1). Under exchange of two quanta:
- Bosonic case: amplitude symmetrized → field operators must commute.
- Fermionic case: amplitude antisymmetrized → field operators must anticommute.

**Step 3: Delta-function from substrate-cell adjacency.** The delta-function $\delta^3(x - x')$ on the right-hand side arises from substrate-cell adjacency content (P03): operators at distinct loci $x \neq x'$ are decoupled at substrate level; only same-locus operators have non-trivial commutator/anticommutator.

The substrate framework supplies the **form** of the canonical relations. The specific delta-function structure inherits from P03 locus indexing; the choice between commutator and anticommutator inherits from T1 spin–statistics.

### 3.3 Connection to adjacency-bandwidth structure

P04 (bandwidth-additive) supplies the substrate-level structure under which canonical relations are normalized. Specifically: the bandwidth content per substrate cell sets the **scale** of the canonical relation.

In the position-momentum sector ($[\hat{x},\hat{p}]$), the bandwidth scale appears as the Planck constant $\hbar$. In the field-operator sector, the bandwidth scale appears in the delta-function normalization.

This is the substrate-level identification (not derivation) of $\hbar$: $\hbar$ appears as a chain-step participation quantum (inheritance from Paper_087 P10 + P09 + P04), not as a substrate-derived quantity. The "structural origin of $\hbar$" framing should be read narrowly as substrate-level **identification**, not as derivation of the numerical value, which is INHERITED.

### 3.4 Why anticommutator for fermions (alternative argument)

An alternative substrate-level argument for fermionic anticommutation:

By T1 spin–statistics, exchange of two identical fermions multiplies the amplitude by $-1$. The creation/annihilation operators $\hat{\psi}^\dagger(x), \hat{\psi}(x)$ are the substrate-level operators that add/remove single fermionic quanta at locus $x$. Two-quantum creation:
$$\hat{\psi}^\dagger(x_1)\hat{\psi}^\dagger(x_2)|0\rangle .$$

By exchange-antisymmetry,
$$\hat{\psi}^\dagger(x_1)\hat{\psi}^\dagger(x_2)|0\rangle = -\hat{\psi}^\dagger(x_2)\hat{\psi}^\dagger(x_1)|0\rangle .$$

This forces $\{\hat{\psi}^\dagger(x_1), \hat{\psi}^\dagger(x_2)\} = 0$, i.e., anticommutation. Hermitian conjugation gives the $\hat{\psi}\hat{\psi}$ anticommutator, and the inhomogeneous $\hat{\psi}\hat{\psi}^\dagger$ anticommutator follows from delta-function normalization.

### 3.5 Heisenberg uncertainty from canonical commutation

The canonical commutation $[\hat{x},\hat{p}] = i\hbar$ implies (Robertson–Schrödinger inequality; standard QM)
$$\Delta x \, \Delta p \geq \frac{|\langle [\hat{x},\hat{p}]\rangle|}{2} = \frac{\hbar}{2} .$$

The Heisenberg uncertainty principle is a direct consequence — not an independent postulate. It is downstream of T8 and follows from canonical commutation + Cauchy-Schwarz.

This is the substrate-level account of why Heisenberg uncertainty holds: it is structurally forced by the participation-measure / translation-generator structure giving $[\hat{x},\hat{p}] = i\hbar$.

---

## §4 Audit Table

| # | Step | Label | Notes |
|---|---|---|---|
| 1 | P02 participation | P | Primitive. |
| 2 | P03 channel + locus indexing | P | Primitive. |
| 3 | P04 bandwidth | P | Primitive. |
| 4 | P10 rule-type | P | Primitive. |
| 5 | Position operator from P03 multiplicative | P | Standard-form construction per Paper_095 §2.3 (definitional). |
| 6 | Momentum operator from translation generator via Stone | I | Standard math (I-Stone). |
| 7 | $\hbar$ as rate constant inherited | I | Empirical matching. |
| 8 | $[\hat{x},\hat{p}] = i\hbar$ | D-via-I | Direct computation from steps 5-7. |
| 9 | Multi-quantum tensor product structure | I | Paper_063. |
| 10 | Spin–statistics dichotomy T1 | I | Paper_RQM_T1. |
| 11 | Bosonic commutator + fermionic anticommutator | I | Inherited from T1 spin–statistics dichotomy + standard QFT. |
| 12 | Delta-function from P03 locus indexing | P | Standard-form construction per Paper_095 §2.3 (definitional). |
| 13 | Heisenberg uncertainty from canonical commutation | I | Standard math + I-CCR. |
| 14 | Specific commutator/anticommutator normalizations | I | Standard QFT matching. |

---

## §5 Falsification Criteria

- **F1: Empirical-detection target.** High-precision interferometric / matter-wave experiments showing position-momentum commutator deviating from $i\hbar$ at accessible scales (e.g., trapped-ion or Bose–Einstein-condensate precision measurements of $\Delta x \Delta p$ that violate Heisenberg's inequality $\hbar/2$) in regimes where standard QM predicts canonical commutation would refute the substrate-CCR identification.

- **F2: Empirical detection of bosonic field exhibiting anticommutation, or fermionic field exhibiting commutation.** Would refute T1 + T8 spin–statistics-to-canonical-relations link.

- **F3: Substrate evidence that Stone's theorem fails for substrate translation group.** Would refute step 6.

- **F4: Substrate-level evidence that the translation generator does NOT have units of action × inverse length.** Would refute the $\hbar$-form.

---

## §6 Position Statement

Paper RQM-T8 establishes canonical (anti-)commutation relations as **M3** with **FORM-INHERITED + VALUE-INHERITED** framing. Per Paper_095 §2.3, the canonical relations $[\hat{x},\hat{p}] = i\hbar$ and field-operator (anti-)commutators are P-definitional standard-form construction; $\hbar$ is INHERITED as a chain-step participation quantum (Paper_087 P10 + P09 + P04 inheritance). The substrate-level contribution is identification of the **commutator-vs-anticommutator dichotomy** as forced by T1 spin–statistics: bosonic ↔ commutator; fermionic ↔ anticommutator. Heisenberg uncertainty follows downstream from canonical commutation + Cauchy–Schwarz. No new postulates.

This paper does NOT derive the canonical-relation forms from substrate primitives — they are INHERITED. It does NOT derive $\hbar$'s numerical value (also INHERITED). It does NOT extend to spacelike (anti-)commutation / microcausality (deferred).

The result joins the Wave-3 Relativistic-QM Bridge family alongside T1 (supplies the dichotomy decision) and T7 (classifies bosonic/fermionic reps).

This paper is in the Wave-3 Relativistic-QM Bridge series of the Event Density program — a substrate-ontology research program in the lineage of 't Hooft's cellular-automaton interpretation, Wolfram's Ruliad, and the causal-set program (Sorkin et al.); NOT in the operational-reconstruction lineage of Hardy / CDP / Coecke-Kissinger.

---

## §7 Rewrite Note

This paper completes the canonical-relations sector of the relativistic-QM bridge. The commutation/anticommutation dichotomy is form-IDENTIFIED (no D rows in audit table; downgraded from FORM-FORCED per Paper_095 §2.3) by participation-measure + spin–statistics; the constant $\hbar$ is INHERITED.

**Relationship to other RQM-bridge papers:**
- **T1 spin–statistics:** supplies the commutator-vs-anticommutator decision.
- **T7 Lorentz reps:** classifies which rule-types are bosonic vs fermionic, hence which canonical relations apply.
- **Phase-1 QM emergence (slot 6):** establishes Schrödinger-evolution via Stone's theorem; this paper extends to canonical relations.

**Numerical content INHERITED.** $\hbar$ value. **Form IDENTIFIED.** Canonical (anti-)commutation form.

**Heisenberg uncertainty** is downstream of this paper, not independent. The substrate origin of Heisenberg is the canonical commutation derived here.

**Future work.** Substrate derivation of $\hbar$ value (currently inherited) — likely tied to Arc M H1-dominant mass-structural-form analysis. Substrate audit of equal-time vs spacelike (anti-)commutation for relativistic fields (microcausality).

Verdict: **M3**.

---

**End Paper RQM-T8.**
