# Paper RQM-Q7Q8 — Vacuum + Particle Dual Structure (Q.7 + Q.8)

**Series:** Wave-3 Relativistic-QM Bridge — Arc-Q Stage 7+8
**Status:** Wave-3 generative paper; M3 verdict at write-time
**Companions:** Paper_RQM_T5 (KG), Paper_RQM_T10 (Lightlike worldlines), Paper_RQM_GRH_D1 (massless Case-P gauge), Paper_089 (V1), Arc-R / Arc-Q.

---

## Preamble — What This Paper Does NOT Claim

1. This paper does **not** claim derivation of the vacuum + particle dual Fock structure for $\sigma=0$ rule-types from nothing. Result is conditional on the 13 ED primitives (Paper_087) + declared paper-specific postulates.
2. It does **not** claim closed-proof reconstruction in the Hardy 2001 / CDP 2011 / Coecke-Kissinger operational-reconstruction sense. ED sits in the substrate-ontology lineage ('t Hooft cellular-automaton, Wolfram Ruliad, causal-set), not the operational-reconstruction lineage.
3. It does **not** override Paper_095's three-tier verdict grammar. Verdict for this paper is stated in §1.
4. It does **not** rigorously derive "no-rest-frame $\Rightarrow$ minimal vacuum+particle dual structure" from substrate primitives alone — the §3.4 argument is currently heuristic and flagged OPEN in audit row 14a. It also does **not** derive specific particle-state content per rule-type (mode-density normalization, etc.) — these are INHERITED via standard QFT.
5. The **vacuum + one-particle Fock structure** for $\sigma=0$ rule-types (mutual orthogonality, Wightman-unique vacuum, lightlike one-particle sector) is FORM-FORCED by T10 (lightlike) + T8 (canonical relations) + P11 + P13; the **rigorous proof of dual-structure necessity** from §3.4 is OPEN.

## Abstract

This paper supplies the substrate-level vacuum + particle dual Fock-space structure for $\sigma = 0$ rule-types in $D = 3+1$, closing Arc-Q stages 7 (one-particle) and 8 (vacuum). The vacuum $|0\rangle_{\mathrm{sub}}$ is characterized (per Wightman uniqueness, applied to the substrate Hilbert space of Paper_007) by Lorentz invariance, time-translation invariance (P13), and annihilation by all $\sigma=0$ mode-annihilation operators; one-particle states are constructed as $|p\rangle = \hat a^\dagger_p|0\rangle$ with $p^2 = 0$ (Paper_RQM_T10 lightlike). The two sectors are mutually orthogonal, and the Fock-space decomposition $\mathcal{H}_{\mathrm{sub}} = \mathcal{H}_{\mathrm{vac}} \oplus \mathcal{H}_{1-\mathrm{ptcl}} \oplus \cdots$ follows from T8 canonical (anti-)commutation relations. The §3.4 "no rest-frame forces minimal dual" argument is OPEN. Verdict per Paper_095: **M3** at write-time. Key falsifier line: **F1** (discovery of a Lorentz-covariant single-mode non-dual representation of $\sigma=0$ excitations).

---

## §1 Statement of Result

**Claim.** For $\sigma = 0$ rule-types in $D = 3+1$, the substrate-level structure forces a **dual vacuum + particle architecture**: (i) a **vacuum sector** consisting of substrate states with no $\sigma = 0$ rule-type excitations (Q.8 vacuum content), and (ii) a **one-particle sector** consisting of substrate states with one lightlike-propagating $\sigma = 0$ rule-type excitation (Q.7 particle content). The two sectors are mutually orthogonal in the rule-type participation Hilbert space (Paper_007) and are connected by creation/annihilation operators with canonical (anti-)commutation structure (Paper_RQM_T8).

The duality is FORM-FORCED by the lightlike-propagation structure of $\sigma = 0$ rule-types (Paper_RQM_T10) + the substrate-level vacuum-state characterization under P11 commitment-irreversibility. Specific particle-state content per rule-type is INHERITED via standard QFT matching.

Verdict: **M3**. No new postulates.

---

## §2 Primitive Inputs

### 2.1 Primitives invoked

- **P02 (Participation)** — supplies vacuum-state and particle-state content as participation configurations.
- **P10 (Rule-type primitive)** — supplies $\sigma = 0$ rule-type carriers.
- **P11 (Commitment-irreversibility)** — supplies directional vacuum / particle distinction.
- **P13 (Time homogeneity)** — supplies temporal-translation symmetry on which the vacuum is defined as time-translation-invariant.

### 2.2 Upstream Dependencies

- **I-007:** Hilbert-space emergence as completion of motif algebra.
- **I-063:** Tensor-product structure (E-1).
- **I-089:** V1 finite-width retarded kernel.
- **I-RQM-T5:** Klein–Gordon equation.
- **I-RQM-T8:** Canonical (anti-)commutation relations.
- **I-RQM-T10:** Lightlike worldlines for $\sigma = 0$ rule-types.
- **I-Wightman:** Standard Wightman QFT machinery.

---

## §3 Derivation

### 3.1 Substrate vacuum state (Q.8)

The substrate vacuum $|0\rangle_{\mathrm{sub}}$ is defined as the participation configuration containing **no rule-type excitations** above the substrate ground state. By P11, the vacuum is a "no-commitment" state — substrate participation content is at its minimal level.

For $\sigma = 0$ rule-types specifically, the vacuum-state characterization Q.8 requires:
1. **Lorentz invariance:** $|0\rangle_{\mathrm{sub}}$ is invariant under the acoustic-metric Lorentz group (Paper_017).
2. **Time-translation invariance** (P13): $|0\rangle_{\mathrm{sub}}$ is unchanged under substrate temporal translation.
3. **Annihilation by all annihilation operators:** $\hat{a}_p |0\rangle_{\mathrm{sub}} = 0$ for all $\sigma = 0$ rule-type modes $p$.

The vacuum is the unique substrate state satisfying all three (Wightman uniqueness, I-Wightman, applied to substrate Hilbert space I-007).

### 3.2 One-particle states (Q.7)

A **one-particle state** of a $\sigma = 0$ rule-type is constructed by acting on the vacuum with a creation operator:
$$|p\rangle = \hat{a}^\dagger_p |0\rangle_{\mathrm{sub}} ,$$
where $p$ is a four-momentum satisfying the massless dispersion $p^2 = 0$ (Paper_RQM_T10 lightlike condition).

The one-particle state is:
1. Eigenstate of the substrate four-momentum operator $\hat{P}^\mu$ with eigenvalue $p^\mu$.
2. Lightlike: $\hat{P}^2 |p\rangle = 0$ (per Paper_RQM_T10).
3. Lorentz-transforming according to the rule-type's Lorentz representation (Paper_RQM_T7).

The substrate origin of Q.7 one-particle structure: V1 kernel propagation (Paper_089) supports lightlike-frequency modes for $\sigma = 0$ rule-types; the corresponding creation operators populate the one-particle sector.

### 3.3 Orthogonality of vacuum and particle sectors

$|0\rangle_{\mathrm{sub}}$ and $|p\rangle$ are orthogonal:
$$\langle 0 | p \rangle = \langle 0 | \hat{a}^\dagger_p | 0 \rangle .$$

Using $[\hat{a}_p, \hat{a}^\dagger_{p'}] = \delta^3(p - p')$ (bosonic case; T8) or analogous anticommutator (fermionic case), the substrate-level matrix element vanishes by the vacuum's annihilation property.

The two sectors are **mutually orthogonal** subspaces of the substrate Hilbert space. The substrate Hilbert space decomposes as
$$\mathcal{H}_{\mathrm{sub}} = \mathcal{H}_{\mathrm{vac}} \oplus \mathcal{H}_{1-\mathrm{particle}} \oplus \mathcal{H}_{2-\mathrm{particle}} \oplus \cdots ,$$
the **Fock-space decomposition**. For $\sigma = 0$ rule-types, this is the substrate-level Fock-space structure.

### 3.4 Why $\sigma = 0$ forces the dual structure

For $\sigma > 0$ rule-types (massive), the vacuum + particle architecture exists but is **enriched** by rest-frame states: a massive particle has a rest frame, and the one-particle sector includes states of arbitrary spatial momentum continuously connecting to the rest-frame state.

For $\sigma = 0$ rule-types (massless), no rest frame exists (Paper_RQM_T10 lightlike); the one-particle sector consists entirely of lightlike-momentum states. This is the **structurally minimal** one-particle sector — there is no intermediate rest-frame structure to bridge to.

The dual structure (vacuum + particle, with nothing between) is therefore **forced** for $\sigma = 0$ rule-types: no rest-frame sector exists to interpolate. Massive rule-types have a richer single-particle structure that "deforms" the dual into a more continuous form.

This is the substrate origin of why the photon's quantum description is particularly simple (just vacuum + photons; no rest-frame photon to consider).

### 3.5 Connection to GRH and gauge structure

By Paper_RQM_GRH_D1 (next paper), GRH guarantees the existence of at least one massless Case-P gauge rule-type. The vacuum + particle dual structure derived here applies to this gauge rule-type as its substrate-level quantum description.

For gauge rule-types, the one-particle sector includes only **transverse** polarizations (per gauge-invariance / T17). Longitudinal modes are removed by the substrate gauge-quotient (Paper_022 T17 C8). The dual structure is preserved; the one-particle sector is restricted to physical degrees of freedom.

### 3.6 Multi-particle and Fock structure

Extending to $n$-particle sectors:
$$|p_1, p_2, \ldots, p_n\rangle = \hat{a}^\dagger_{p_1} \hat{a}^\dagger_{p_2} \cdots \hat{a}^\dagger_{p_n} |0\rangle_{\mathrm{sub}} ,$$
with appropriate (anti-)symmetrization per T1 statistics. The full Fock-space structure follows from the vacuum + particle dual + the canonical (anti-)commutation relations (T8).

This is the substrate-level reconstruction of QFT Fock-space content for $\sigma = 0$ rule-types.

---

## §4 Audit Table

| # | Step | Label | Notes |
|---|---|---|---|
| 1 | P02 participation | P | Primitive. |
| 2 | P10 $\sigma = 0$ rule-type | P | Primitive. |
| 3 | P11 commitment-irreversibility (vacuum / particle distinction) | P | Primitive. |
| 4 | P13 time homogeneity (vacuum invariance) | P | Primitive. |
| 5 | Substrate Hilbert space | I | Paper_007. |
| 6 | Substrate Lorentz covariantization | I | Paper_017. |
| 7 | V1 kernel for $\sigma = 0$ rule-types | I | Paper_089. |
| 8 | Lightlike worldlines for $\sigma = 0$ | I | Paper_RQM_T10. |
| 9 | Canonical (anti-)commutation relations | I | Paper_RQM_T8. |
| 10 | Vacuum-state characterization (Lorentz-inv + time-inv + annihilated) | D-via-I | Wightman uniqueness applied to substrate. |
| 11 | One-particle states $|p\rangle = \hat{a}^\dagger_p |0\rangle$ | D-via-I | Standard QFT construction on substrate. |
| 12 | Vacuum ⊥ particle (Q.7 + Q.8 dual) | D | Direct from step 10 + step 11. |
| 13 | Fock-space decomposition | D-via-I | Composition + standard QFT. |
| 14 | Gauge-rule-type restriction to transverse modes | I | Paper_022 (T17 C8). |
| 14a | §3.4 substrate argument "σ=0 ⇒ no rest frame ⇒ minimal dual structure" | OPEN | Substrate-level argument currently heuristic; rigorous derivation of "no-rest-frame forces dual structure" from substrate primitives alone is OPEN. |
| 15 | Verdict M3 | A→position | Per Paper_095. |

---

## §5 Falsification Criteria

- **F1:** Discovery of a Lorentz-covariant **single-mode (non-dual)** representation of $\sigma = 0$ substrate excitations — i.e., a Lorentz-covariant representation of massless rule-types that does not factor through the vacuum + one-particle dual + Fock-space structure — would falsify the dual-structure necessity claim of §3.4.

- **F2: Substrate evidence that the vacuum state is not annihilated by all $\sigma = 0$ annihilation operators.** Would refute Q.8 vacuum characterization.

- **F3: Substrate evidence that one-particle $\sigma = 0$ states are not lightlike.** Propagates from Paper_RQM_T10 falsifier.

- **F4: Wightman uniqueness of the vacuum shown to fail at substrate level.** Would refute step 10.

---

## §6 Position Statement

This paper sits within the **substrate-ontology research-program lineage** ('t Hooft cellular-automaton interpretation of QM; Wolfram Ruliad / hypergraph-rewriting; causal-set program, Sorkin et al.), **not** within the operational-reconstruction lineage (Hardy 2001, CDP 2011, Coecke-Kissinger). Methodology per Paper_095 (form-FORCED / value-INHERITED).

This paper supplies the substrate-level vacuum + particle dual structure for $\sigma = 0$ rule-types, closing Arc-Q stages 7 and 8.

**Relationship to other RQM papers:**
- **T5 KG, T10 lightlike worldlines:** supply the dispersion + propagation structure.
- **T8 canonical relations:** supply the creation/annihilation operator algebra.
- **GRH D1 (next paper):** guarantees at least one $\sigma = 0$ rule-type exists, making the dual structure non-vacuous.

**Numerical content INHERITED.** Specific particle masses, mode-density normalization. **Form FORCED.** Vacuum + one-particle Fock structure for $\sigma = 0$ rule-types.

**Future work.** Substrate audit of multi-particle interaction sectors; substrate origin of $S$-matrix structure; substrate audit of vacuum stability under curved acoustic metric.

Verdict: **M3**.

---

**End Paper RQM-Q7Q8.**
