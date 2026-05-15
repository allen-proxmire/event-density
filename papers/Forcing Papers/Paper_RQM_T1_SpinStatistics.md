# Paper RQM-T1 — Spin–Statistics $\eta = (-1)^{2s}$ in 3+1D

**Series:** Wave-3 Relativistic-QM Bridge — Theorem T1
**Status:** Wave-3 generative paper; M3 verdict at write-time (FORM-FORCED + VALUE-INHERITED)
**Companions:** Paper_087 (13 primitives), Paper_063 (E-1 tensor product), Paper_RQM_T2 (Cl(3,1)), Paper_RQM_T3 (anyon prohibition), Paper_RQM_T4 (Dirac), Arc-R Stage R.2 (relativistic rule-type taxonomy).

---

## Preamble: What This Paper Does NOT Claim

1. **The 13 primitives are not derived.** They are postulated per Paper_087.
2. **No claim that the spin–statistics dichotomy is forced from nothing.** The $\eta = (-1)^{2s}$ result is conditional on P06 + P09 + P10 + the topology of $SO(3)$ + standard QFT exchange machinery.
3. **No claim of numerical-content derivation beyond what is explicitly INHERITED.** Specific particle spin assignments (electron $s = 1/2$, photon $s = 1$, etc.) are INHERITED via standard QM matching, not substrate-derived.
4. **No claim that ED is the only consistent substrate ontology.** Other substrate ontologies are conceivable; ED commits to the 13-primitive set.
5. **No claim that this paper closes CPT, parity, or time-reversal sectors.** The exchange-phase dichotomy only is covered here; discrete-symmetry audits are deferred.
6. **No claim of empirical adequacy outside $D = 3+1$.** In $D = 2+1$, anyonic statistics is admissible (covered separately in Paper_RQM_T3).

---

## Abstract

Paper RQM-T1 establishes the spin–statistics dichotomy $\eta = (-1)^{2s}$ in 3+1 substrate dimensions as a FORM-FORCED structural consequence of P06 (spatial dimension $D = 3+1$), P09 ($U(1)$-valued polarity), and P10 (rule-type primitive), composed with the standard topology $\pi_1(SO(3)) = \mathbb{Z}_2$ and standard QFT exchange-statistics machinery. The substrate-level mechanism: exchange of two identical rule-type carriers corresponds topologically to a $\pi$-rotation of the carrier-pair frame; polarity (P09) transforms under such rotations according to the intrinsic-rotation quantum number $s$, yielding $\eta = (-1)^{2s}$. The structural form of the dichotomy (only $\eta = \pm 1$ admissible, fermion/boson exhaustive) is FORM-FORCED; specific particle spin assignments are VALUE-INHERITED. Verdict tier: **M3** per Paper_095. The result is structurally prior to Dirac (T4) and anyon prohibition (T3), and is the load-bearing entry point for the Wave-3 Relativistic-QM Bridge family. This paper is in the substrate-ontology research-program lineage of 't Hooft's cellular-automaton interpretation, Wolfram's Ruliad, and the causal-set program — not in the operational-reconstruction lineage of Hardy / CDP / Coecke-Kissinger.

---

## §1 Statement of Result

**Claim.** In 3+1 substrate dimensions (P06), the exchange of two identical rule-type carriers under participation measure produces a phase factor $\eta = (-1)^{2s}$, where $s$ is the rule-type's intrinsic-rotation quantum number. Fermionic ($\eta = -1$, half-integer $s$) and bosonic ($\eta = +1$, integer $s$) are the only admissible statistics classes. The dichotomy is FORM-FORCED by composition of P06 (spatial-dimension primitive), P09 ($U(1)$-valued polarity), and rule-type exchange topology. Specific spectroscopic spin values are INHERITED via standard QM matching.

The result anchors the relativistic-QM bridge: spin–statistics is the substrate-level reason why electrons obey Pauli exclusion and photons obey Bose–Einstein statistics. It is structurally prior to Dirac (T4) and anyon prohibition (T3), and is the load-bearing entry point for the bridge family.

Verdict tier: **M3**. No new postulates introduced.

---

## §2 Primitive Inputs

### 2.1 Primitives invoked (per Paper_087)

- **P03 (Channel + locus indexing; spatial homogeneity)** — supplies the indexing under which rule-type carriers are distinguished.
- **P05 (Polarity-transport along edges)** — supplies the substrate-level transport carrying the $U(1)$ polarity that rotates under exchange.
- **P06 (Spatial dimension $D = 3+1$)** — the load-bearing primitive: only in $D = 3+1$ does the exchange-rotation topology produce the $2\pi$-vs-$4\pi$ dichotomy.
- **P09 ($U(1)$-valued polarity)** — supplies the phase target group on which exchange acts.
- **P10 (Rule-type primitive)** — supplies the rule-type carriers themselves.

### 2.2 Upstream Dependencies

- **I-063:** Tensor-product structure for bipartite chain pairs (Paper_063, E-1).
- **I-008:** Phase structure on rule-types from P09 + P10 (Paper_008).
- **I-087:** 13-primitive position paper (Paper_087).
- **I-Topology:** Standard $SO(3)$ / $SU(2)$ topology — $\pi_1(SO(3)) = \mathbb{Z}_2$ (standard math).
- **I-Exchange:** Standard QFT exchange-statistics machinery (standard physics).

---

## §3 Derivation

### 3.1 Rule-type exchange under participation measure

Consider two identical rule-type carriers at substrate locations $x_A$ and $x_B$, each carrying $U(1)$-valued polarity (P09) and assigned to channels via P03. The participation measure on the bipartite configuration is constructed under E-1 tensor-product structure (Paper_063):
$$\Psi(x_A, x_B) = \Psi_A(x_A) \otimes \Psi_B(x_B) \;\;\text{or sum of permutations.}$$

Exchange of the two carriers $(x_A \leftrightarrow x_B)$ is a substrate-level operation. The question: what is the phase factor $\eta$ multiplying the post-exchange amplitude relative to pre-exchange?

### 3.2 Exchange as $\pi$-rotation in 3+1D

In $D = 3+1$ substrate dimensions, the exchange of two identical carriers along a continuous path corresponds topologically to a $\pi$-rotation of the carrier-pair frame (Berry's argument; standard QM). In $D \geq 3$ spatial dimensions, this $\pi$-rotation is **homotopically connected** to the identity via paths that avoid carrier coincidence.

Crucially: the **double exchange** (two consecutive exchanges, returning to original configuration) corresponds to a $2\pi$-rotation, which in $D = 3+1$ is a topologically distinct element from the identity for half-integer-spin carriers (because $\pi_1(SO(3)) = \mathbb{Z}_2$ — the famous "Dirac belt trick").

### 3.3 The $\eta = (-1)^{2s}$ factor

The carrier's $U(1)$ polarity (P09) transforms under spatial rotations according to its intrinsic-rotation quantum number $s$. Under a $2\pi$-rotation of the carrier frame:
$$\Psi \to e^{2\pi i \cdot 2s / 2} \Psi = e^{2\pi i s} \Psi = (-1)^{2s} \Psi .$$

For integer $s$: $(-1)^{2s} = +1$ (bosonic; $\Psi$ returns to itself after double exchange).
For half-integer $s$: $(-1)^{2s} = -1$ (fermionic; $\Psi$ acquires a sign after double exchange).

By the topological argument of §3.2 + the polarity-rotation argument here, single exchange yields $\eta = (-1)^{2s}$ — half the double-exchange phase, since a single exchange is $\pi$-rotation, not $2\pi$.

This is the standard spin–statistics relation. The substrate origin: P09 supplies the $U(1)$ rotation structure on polarity; P06 supplies the $D = 3+1$ topology that distinguishes integer-spin from half-integer-spin under exchange.

### 3.4 Why only 3+1D works

In $D = 2+1$ (Paper_RQM_T3 covers this in detail), the exchange topology is different: the configuration-space fundamental group is the **braid group** $B_n$, not the permutation group $S_n$. Braid-group representations admit arbitrary phase factors $e^{i\theta}$, giving rise to *anyons*.

In $D = 1+1$, no exchange-rotation argument applies; statistics degenerates.

In $D \geq 4$ (spatial), the exchange topology gives only the permutation group (no braid structure), but the rotation group $SO(D)$ for $D \geq 4$ does not have the $\mathbb{Z}_2$ topology of $SO(3)$, so the half-integer-spin sector behaves differently.

**Only $D = 3+1$ produces exactly two statistics classes via the $(-1)^{2s}$ rule.** P06 is therefore load-bearing.

### 3.5 Composition with Arc-R Stage R.2

Arc-R Stage R.2 (relativistic rule-type taxonomy) classifies rule-types by their Lorentz representations (Paper_RQM_T7). The classification includes:
- Scalar (spin-0) rule-types — bosonic.
- Vector (spin-1) rule-types — bosonic.
- Spinor (spin-1/2) rule-types — fermionic.
- Tensor (spin-2) rule-types — bosonic.

The spin–statistics dichotomy is the substrate-level constraint on which combinations are admissible. Half-integer spin forces fermionic statistics; integer spin forces bosonic.

### 3.6 Numerical content

Specific spin values for specific rule-types (electron $s = 1/2$, photon $s = 1$, etc.) are INHERITED via standard QM matching. The substrate program does not derive the spin assignment of specific particles from first principles; it derives the **dichotomy** that any rule-type's spin assignment must obey.

---

## §4 Audit Table

| # | Step | Label | Notes |
|---|---|---|---|
| 1 | P06 spatial dimension $D = 3+1$ | P | Primitive (Paper_087). |
| 2 | P09 $U(1)$-valued polarity | P | Primitive. |
| 3 | P10 rule-type primitive | P | Primitive. |
| 4 | Tensor-product structure on bipartite carriers | I | Paper_063 (E-1). |
| 5 | Phase structure $S^1$ on rule-types | I | Paper_008. |
| 6 | Standard $SO(3)$ / $SU(2)$ topology, $\pi_1(SO(3)) = \mathbb{Z}_2$ | I | Standard math. |
| 7 | Exchange = $\pi$-rotation of carrier-pair frame in $D = 3+1$ | D-via-I | Application of standard topology to substrate exchange. |
| 8 | Double exchange = $2\pi$-rotation; topologically non-trivial for half-integer $s$ | D-via-I | Composition of step 7 + Berry's argument. |
| 9 | Polarity transforms as $\Psi \to e^{2\pi i s}\Psi$ under $2\pi$-rotation | I | Standard rep theory of $SO(3)$. |
| 10 | $\eta = (-1)^{2s}$ exchange phase | D-via-I | Composition of steps 7–9 (topology + polarity-rotation, both inherited). |
| 11 | Integer $s$ → bosonic; half-integer $s$ → fermionic | D-via-I | Direct from step 10 + standard rep theory. |
| 12 | Only $D = 3+1$ produces exactly two statistics classes | D | Composition of step 7 + dimension-specific topology. |
| 13 | Specific particle spin assignments | I | Empirical QM matching. |

No structural-analogy mislabel.

---

## §5 Falsification Criteria

- **F1: Empirical detection of statistics violating $\eta = (-1)^{2s}$ in 3+1D.** Direct observation of fermionic behavior for an integer-spin particle, or bosonic behavior for a half-integer-spin particle (without intervening interactions), refutes the spin–statistics relation and propagates to refutation of the substrate derivation.

- **F2: Detection of a third statistics class in $D = 3+1$.** Anyonic / parastatistical behavior beyond fermion/boson dichotomy in genuine 3+1D systems (not 2+1D surface states) refutes the topological argument of §3.2.

- **F3: Substrate evidence that P06 admits multiple statistics dichotomies in $D = 3+1$.** If substrate-level rule-type taxonomy admits exchange-phase classes beyond $\pm 1$ in $D = 3+1$, the derivation fails.

- **F4: Empirical refutation of $\pi_1(SO(3)) = \mathbb{Z}_2$ in physical rotations.** Would refute the topological input I-Topology and propagate.

---

## §6 Position Statement

Paper RQM-T1 establishes the spin–statistics dichotomy $\eta = (-1)^{2s}$ as **M3** (FORM-FORCED structural dichotomy + VALUE-INHERITED particle-specific assignments) under the load-bearing primitives P06 + P09 + P10 with no new postulates introduced. The structural form is FORM-FORCED by composition of substrate primitives with standard $SO(3)$ topology and standard QFT exchange machinery; specific spin values for electron, photon, etc. are INHERITED via standard QM matching. The result joins the Wave-3 Relativistic-QM Bridge family alongside T2 (Cl(3,1) algebraic substrate), T3 (anyon prohibition — dimension-comparison companion), T4 (Dirac equation for spinor rule-types), and T7 (Lorentz representation taxonomy), serving as the foundational dichotomy on which downstream spinor-sector results rest.

This paper does NOT derive specific particle spin assignments from first principles, does NOT extend to CPT / parity / time-reversal sectors (deferred), and does NOT claim that the spin–statistics relation alone forces the full standard model. The empirical adequacy claim is regime-conditional on $D = 3+1$ substrate dimensions.

This paper is in the Wave-3 Relativistic-QM Bridge series of the Event Density program — a substrate-ontology research program in the lineage of 't Hooft's cellular-automaton interpretation, Wolfram's Ruliad, and the causal-set program (Sorkin et al.); NOT in the operational-reconstruction lineage of Hardy / CDP / Coecke-Kissinger.

---

## §7 Rewrite Note

This paper rewrites the standard spin–statistics theorem within the ED substrate framework. The novelty is not the spin–statistics relation itself (well-established) but its **substrate-level derivation** from P06 + P09 + rule-type exchange topology rather than from Lorentz-covariance plus positivity-of-energy (the standard Pauli proof).

**Relationship to other RQM-bridge papers:**
- T2 (Cl(3,1) frame uniqueness) supplies the gamma-matrix structure on which spinor rule-types are realized.
- T3 (Anyon prohibition) is the dimension-comparison companion to T1: T1 says 3+1D admits exactly two statistics; T3 says 2+1D admits a continuum.
- T4 (Dirac equation) supplies the relativistic first-order equation for spinor rule-types.
- T7 (Lorentz representations) supplies the full taxonomy of rule-type spin assignments.

**Numerical content INHERITED.** Specific particle spin assignments come from standard QM. **Form FORCED.** The $\eta = (-1)^{2s}$ structural relation is substrate-derived.

**Future work.** Substrate-level audit of CPT, parity, and time-reversal sectors of the spin–statistics machinery is OPEN; this paper covers the exchange-phase dichotomy only.

Verdict: **M3** (FORM-FORCED structural dichotomy + VALUE-INHERITED particle-specific assignments).

---

**End Paper RQM-T1.**
