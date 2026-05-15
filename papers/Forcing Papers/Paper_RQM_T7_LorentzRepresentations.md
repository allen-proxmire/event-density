# Paper RQM-T7 — Lorentz Representations from Primitives

**Series:** Wave-3 Relativistic-QM Bridge — Theorem T7
**Status:** Wave-3 generative paper; M3 verdict at write-time
**Companions:** Paper_RQM_T1 (Spin–statistics), Paper_RQM_T2 (Cl(3,1)), Paper_RQM_T4 (Dirac), Paper_RQM_T5 (KG), Paper_017 (Lorentz covariantization).

---

## Preamble: What This Paper Does NOT Claim

1. **The 13 primitives are not derived.** They are postulated per Paper_087.
2. **No claim that the Lorentz-representation taxonomy is forced from nothing.** The result is conditional on P03 + P06 + P09 + P10 + Paper_017 + standard representation theory of $\mathrm{SL}(2,\mathbb{C})$.
3. **No claim of numerical-content derivation beyond what is explicitly INHERITED.** Which specific rule-types instantiate which representations (electron → Dirac, photon → vector, etc.) is INHERITED via experimental particle taxonomy.
4. **No claim that ED is the only consistent substrate ontology.** Other substrate ontologies are conceivable.
5. **No claim of empirical adequacy for Wigner particle-state classification** — this paper covers field-component classification only; Wigner reps are downstream (Phase-1 QM emergence).
6. **No claim of higher-spin field equations beyond classification.** Rarita–Schwinger, graviton field equations are deferred.

---

## Abstract

Paper RQM-T7 establishes the finite taxonomy of Lorentz representations — scalar $(0,0)$, Weyl spinor $(1/2,0)$ and $(0,1/2)$, Dirac spinor, vector $(1/2,1/2)$, antisymmetric tensor, symmetric traceless tensor — for rule-types in $D = 3+1$, as a form-IDENTIFIED structural classification (no D rows in audit table; downgraded from FORM-FORCED per Paper_095 §2.3) derived from P06 (spatial dimension) + P03 (channel + locus indexing) + P09 ($U(1)$-valued polarity) + P10 (rule-type primitive), composed with Paper_017 substrate Lorentz covariantization and standard representation theory of $\mathrm{SL}(2,\mathbb{C})$. The taxonomy is form-IDENTIFIED with structure-forcing rule-type bundles supporting irreducible reps; specific particle-representation assignments are VALUE-INHERITED via experimental particle taxonomy. Verdict tier: **M3** per Paper_095. The result joins the Wave-3 Relativistic-QM Bridge family as the organizing principle: each representation has its field equation (KG for scalar via T5, Dirac for spinor via T4, Maxwell-class for vector, Einstein-class for tensor) and its statistics assignment via T1; the algebraic substrate for the Dirac spinor is supplied by T2 Cl(3,1). This paper is in the substrate-ontology research-program lineage of 't Hooft, Wolfram, and the causal-set program — not in the operational-reconstruction lineage of Hardy / CDP / Coecke-Kissinger.

---

## §1 Statement of Result

**Claim.** Rule-types in $D = 3+1$ admit a finite taxonomy of Lorentz representations — scalar $(0,0)$, spinor $(1/2, 0)$ and $(0, 1/2)$, vector $(1/2, 1/2)$, and higher tensor representations — derived from P06 (spatial dimension) + P03 (channel + locus indexing) + the substrate's polarity-rotation structure (P09). The classification is form-IDENTIFIED (no D rows in audit table; downgraded from FORM-FORCED per Paper_095 §2.3) by standard representation theory of $\mathrm{SL}(2,\mathbb{C})$ applied to the substrate's rule-type bundles. Which rule-types instantiate which representations is INHERITED via empirical matching.

Verdict: **M3**. No new postulates.

---

## §2 Primitive Inputs

### 2.1 Primitives invoked

- **P03 (Channel + locus indexing)** — supplies the indexing on which Lorentz reps act.
- **P06 (Spatial dimension $D = 3+1$)** — supplies the Lorentz group $\mathrm{SO}(3,1)$ structure.
- **P09 ($U(1)$-valued polarity)** — supplies the angular-rotation generator content.
- **P10 (Rule-type primitive)** — rule-types as carriers of Lorentz reps.

### 2.2 Upstream Dependencies

- **I-087:** 13-primitive position paper.
- **I-017:** Substrate→continuum Lorentz covariantization (Paper_017).
- **I-RQM-T1:** Spin–statistics dichotomy.
- **I-RQM-T2:** Cl(3,1) frame uniqueness.
- **I-Lorentz:** Standard representation theory of $\mathrm{SL}(2,\mathbb{C})$ (standard math).
- **I-Group:** Standard Lie-group / Lie-algebra machinery.

---

## §3 Derivation

### 3.1 The Lorentz group at substrate level

By Paper_017 substrate→continuum Lorentz covariantization, the substrate's coarse-grained kinematics support an acoustic metric with Lorentzian signature (P06: $D = 3+1$). The local Lorentz group $\mathrm{SO}(3,1)$ acts on the substrate's coarse-grained vector / spinor / tensor content.

For substrate-level rule-types, the natural classification is by **representation of the local Lorentz group**. The universal cover of $\mathrm{SO}(3,1)$ is $\mathrm{SL}(2,\mathbb{C})$, and the finite-dimensional irreducible representations of $\mathrm{SL}(2,\mathbb{C})$ are labeled by pairs $(j_1, j_2)$ with $j_1, j_2 \in \{0, 1/2, 1, 3/2, ...\}$.

### 3.2 Standard $\mathrm{SL}(2,\mathbb{C})$ representations

The full classification (I-Lorentz):

| Rep label $(j_1, j_2)$ | Dimension | Name |
|---|---|---|
| $(0, 0)$ | 1 | Scalar |
| $(1/2, 0)$ | 2 | Left-handed Weyl spinor |
| $(0, 1/2)$ | 2 | Right-handed Weyl spinor |
| $(1/2, 0) \oplus (0, 1/2)$ | 4 | Dirac spinor |
| $(1/2, 1/2)$ | 4 | Vector (4-vector) |
| $(1, 0)$ | 3 | Self-dual antisymmetric tensor |
| $(0, 1)$ | 3 | Anti-self-dual antisymmetric tensor |
| $(1, 0) \oplus (0, 1)$ | 6 | Antisymmetric tensor $F_{\mu\nu}$ |
| $(1, 1/2)$, $(1/2, 1)$ | 6 each | Rarita–Schwinger fields |
| $(1, 1)$ | 9 | Symmetric traceless tensor (graviton-class) |
| Higher | ... | ... |

Each rule-type in the substrate maps to one of these representations (or a direct sum thereof).

### 3.3 Substrate origin of the classification

P06 ($D = 3+1$) fixes the Lorentz group as $\mathrm{SO}(3,1)$ with universal cover $\mathrm{SL}(2,\mathbb{C})$. P03 (channel + locus indexing) supplies the indexing under which rule-types are assigned to specific representations. P09 ($U(1)$-valued polarity) supplies the angular-rotation content; combined with the boost generators (which P03 + P06 imply), the full Lorentz algebra emerges.

The substrate-level rule-type bundle structure (T17 / Paper_015) provides the carrier-space on which $\mathrm{SL}(2,\mathbb{C})$ representations act. Each rule-type's carrier-space dimension matches the dimension of its representation.

**Schur's lemma + irreducibility:** rule-types are indexed by **irreducible** $\mathrm{SL}(2,\mathbb{C})$ representations. Reducible representations decompose into direct sums of irreducibles, each of which corresponds to a substrate-level rule-type.

### 3.4 Spin-$s$ assignment from $(j_1, j_2)$

The total angular momentum of a $(j_1, j_2)$ rule-type ranges over $j = |j_1 - j_2|, |j_1 - j_2| + 1, ..., j_1 + j_2$. For "spin-$s$" assignment in the sense of spin–statistics (T1):
- Scalar $(0,0)$: $s = 0$.
- Weyl $(1/2, 0)$ or $(0, 1/2)$: $s = 1/2$.
- Dirac $(1/2,0) \oplus (0,1/2)$: $s = 1/2$.
- Vector $(1/2, 1/2)$: $s = 0$ or $s = 1$ (the four components decompose into a scalar + a 3-vector).
- Antisymmetric tensor: $s$ derived from decomposition.
- Symmetric traceless 2-tensor (graviton): $s = 2$.

The spin–statistics dichotomy (T1) then assigns each representation either bosonic ($s$ integer) or fermionic ($s$ half-integer).

### 3.5 Why $\mathrm{SL}(2,\mathbb{C})$ and not $\mathrm{SO}(3,1)$ directly

$\mathrm{SO}(3,1)$ does not have finite-dimensional unitary representations (the boosts are non-compact). Its **universal cover** $\mathrm{SL}(2,\mathbb{C})$ has finite-dimensional non-unitary representations (the $(j_1, j_2)$ representations) used for **finite-component fields**.

For unitary representations on Hilbert space (carrying particle states), one uses infinite-dimensional representations of the Poincaré group (Wigner's classification). The two are distinct: $(j_1, j_2)$ classifies **field-component structure**; Wigner reps classify **one-particle states**.

This paper covers the field-component classification (relevant for substrate rule-type taxonomy). Particle-state classification is downstream (covered in Phase-1 QM emergence).

### 3.6 Connection to T1 + T2 + T4 + T5

- **T1 spin–statistics:** Each $(j_1, j_2)$ rep has total spin $s$; T1's $\eta = (-1)^{2s}$ classifies bosonic vs fermionic.
- **T2 Cl(3,1):** Dirac spinor $(1/2,0) \oplus (0,1/2)$ is the four-component spinor whose algebraic structure is Cl(3,1).
- **T4 Dirac equation:** Governs the Dirac-spinor $(1/2,0) \oplus (0,1/2)$ representation.
- **T5 Klein–Gordon equation:** Governs the scalar $(0,0)$ representation.

The Lorentz-representation taxonomy is the **organizing principle** for the relativistic-QM bridge: each representation has its own field equation (KG for scalar, Dirac for spinor, Maxwell-class for vector, Einstein-class for tensor), and each has its statistics assignment via T1.

### 3.7 Numerical content inherited

- Which **specific** rule-types instantiate which representations is inherited from experimental particle taxonomy.
- Examples:
  - Higgs scalar → $(0,0)$.
  - Electron → Dirac $(1/2,0) \oplus (0,1/2)$.
  - Neutrino → Weyl $(1/2, 0)$ or $(0,1/2)$ (chirality empirically inherited).
  - Photon → vector $(1/2, 1/2)$ (specifically, the $s=1$ part; gauge-fixed).
  - Graviton (hypothetical) → symmetric traceless 2-tensor $(1,1)$.

The substrate framework provides the **classification**; specific particle assignments are inherited.

---

## §4 Audit Table

| # | Step | Label | Notes |
|---|---|---|---|
| 1 | P03 channel + locus indexing | P | Primitive. |
| 2 | P06 $D = 3+1$ | P | Primitive. |
| 3 | P09 $U(1)$ polarity | P | Primitive. |
| 4 | P10 rule-type primitive | P | Primitive. |
| 5 | Substrate Lorentz covariantization → $\mathrm{SO}(3,1)$ on acoustic metric | I | Paper_017. |
| 6 | Universal cover $\mathrm{SL}(2,\mathbb{C})$ | I | Standard math (I-Lorentz). |
| 7 | Finite-dim $\mathrm{SL}(2,\mathbb{C})$ irreps labeled by $(j_1, j_2)$ | I | Standard rep theory. |
| 8 | Standard rep table (scalar, Weyl, Dirac, vector, tensor, ...) | I | Standard rep theory. |
| 9 | Rule-type bundles support irreducible reps | D-via-I | Application of standard rep theory of Lorentz group (inherited Schur's lemma). |
| 10 | Total spin $s$ from $(j_1, j_2)$ decomposition | I | Standard angular-momentum theory. |
| 11 | Spin–statistics assignment via T1 | I | Paper_RQM_T1. |
| 12 | Dirac spinor algebra is Cl(3,1) | I | Paper_RQM_T2. |
| 13 | Field equations per representation (KG for scalar, Dirac for spinor, ...) | I | Paper_RQM_T4, T5; standard physics. |
| 14 | Specific particle-rep assignments | I | Empirical. |
| 15 | Wigner particle-state classification (separate) | I (out of scope) | Phase-1 QM emergence. |

---

## §5 Falsification Criteria

- **F1: Empirical detection of a rule-type that does not transform under any $\mathrm{SL}(2,\mathbb{C})$ irreducible representation** in $D = 3+1$. Would refute the substrate-rep classification.

- **F2: Substrate Lorentz covariantization (Paper_017) shown to support a group different from $\mathrm{SO}(3,1)$.** Propagates from upstream.

- **F3: Schur's lemma application to rule-type bundles shown to fail.** Would refute step 9.

- **F4: Discovery of a rule-type whose carrier dimension exceeds the maximum allowed by standard $\mathrm{SL}(2,\mathbb{C})$ representations.** Would refute completeness of the classification.

---

## §6 Position Statement

Paper RQM-T7 establishes the Lorentz representation taxonomy as **M3** (form-IDENTIFIED structural classification + VALUE-INHERITED specific particle-representation assignments; no D rows in audit table; downgraded from FORM-FORCED per Paper_095 §2.3) under P03 + P06 + P09 + P10 + Paper_017 with no new postulates. The classification is form-IDENTIFIED by substrate Lorentz covariantization + standard rep theory of $\mathrm{SL}(2,\mathbb{C})$; specific particle assignments (which rule-type ↔ which rep) are INHERITED. The result joins the Wave-3 Relativistic-QM Bridge family as the organizing principle for the entire bridge: T1 (spin–statistics) gives statistics class per rep, T2 (Cl(3,1)) supplies algebraic substrate for Dirac spinor, T4 + T5 supply field equations per rep, T6 supplies gauge interactions, T8 supplies canonical relations, T9 supplies UV-finiteness per rep class.

This paper does NOT cover Wigner particle-state classification (deferred to Phase-1 QM emergence), does NOT supply higher-spin field equations beyond classification (Rarita–Schwinger, graviton — deferred), and does NOT derive specific particle-rep assignments.

This paper is in the Wave-3 Relativistic-QM Bridge series of the Event Density program — a substrate-ontology research program in the lineage of 't Hooft's cellular-automaton interpretation, Wolfram's Ruliad, and the causal-set program (Sorkin et al.); NOT in the operational-reconstruction lineage of Hardy / CDP / Coecke-Kissinger.

---

## §7 Rewrite Note

This paper supplies the Lorentz-representation taxonomy that organizes the substrate's relativistic rule-type structure. Form IDENTIFIED (no D rows in audit table; downgraded from FORM-FORCED per Paper_095 §2.3); specific particle assignments INHERITED.

**Relationship to other RQM-bridge papers:**
- **T1 spin–statistics + T2 Cl(3,1):** specific representations.
- **T4 Dirac + T5 KG:** field equations per representation.
- **T6 minimal coupling:** interaction structure across representations.
- **T8 commutation relations + T9 UV finiteness:** further structural features inherited per representation class.

**Numerical content INHERITED.** Specific particle-representation assignments. **Form IDENTIFIED.** The $\mathrm{SL}(2,\mathbb{C})$ representation taxonomy as substrate-level rule-type classification scheme.

**Future work.** Wigner particle-state classification at substrate level (interplay of Lorentz reps with Phase-1 Hilbert-space emergence); higher-spin field equations (Rarita–Schwinger, graviton); supersymmetric extensions (if any substrate-level support).

Verdict: **M3**.

---

**End Paper RQM-T7.**
