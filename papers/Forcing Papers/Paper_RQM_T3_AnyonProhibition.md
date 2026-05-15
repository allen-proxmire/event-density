# Paper RQM-T3 — Anyon Prohibition in 3+1D

**Series:** Wave-3 Relativistic-QM Bridge — Theorem T3
**Status:** Wave-3 generative paper; **M1** verdict (pure dimension-comparison structural result; no inherited numerical content)
**Companions:** Paper_RQM_T1 (Spin–statistics), Paper_RQM_T2 (Cl(3,1)), Paper_087.

---

## Preamble: What This Paper Does NOT Claim

1. **The 13 primitives are not derived.** They are postulated per Paper_087.
2. **No claim that anyon prohibition is forced from nothing.** The result is conditional on P06 + P10 + P03 + standard configuration-space topology (Leinaas–Myrheim, Wilczek) + finite-group rep theory.
3. **No claim of numerical-content derivation.** This paper is a pure dimension-comparison structural result; no specific particle-content is inherited within the substantive claim.
4. **No claim that ED is the only consistent substrate ontology.** Other substrate ontologies are conceivable.
5. **No claim that effective 2D surface anyons are substrate-level anyons.** Anyonic statistics observed in fractional-quantum-Hall systems is consistent with the substrate framework as coarse-graining of $D = 3+1$ to effective 2D.
6. **No claim of empirical adequacy outside $D = 3+1$.** $D = 2+1$ admits anyons by braid-group structure.

---

## Abstract

Paper RQM-T3 establishes the prohibition of anyonic statistics in $D = 3+1$ as a form-IDENTIFIED structural consequence (no D rows in audit table; downgraded from FORM-FORCED per Paper_095 §2.3) of P06 (spatial dimension) + P10 (rule-type primitive) + P03 (channel + locus indexing), composed with standard algebraic topology of configuration spaces. The substrate-level mechanism: in $D = 3+1$, the configuration-space fundamental group for $n$ identical rule-type carriers is the permutation group $S_n$ (not the braid group $B_n$); the one-dimensional representations of $S_n$ are exactly the trivial (bosonic, $\eta = +1$) and sign (fermionic, $\eta = -1$) representations. Continuous-phase anyons $\eta = e^{i\theta}$ exist only in braid-group representations, which require $d = 2$ spatial dimensions. The result is form-IDENTIFIED (no D rows in audit table; downgraded from FORM-FORCED per Paper_095 §2.3) with no inherited numerical particle-content; verdict tier: **M1** per Paper_095 (structural result from primitives + standard math alone). T3 is the dimension-comparison companion to T1 spin–statistics: T1 supplies the polarity-rotation factor, T3 supplies the topological admissibility constraint; together they force the fermion/boson dichotomy exhaustively in $D = 3+1$. This paper is in the substrate-ontology research-program lineage of 't Hooft, Wolfram, and the causal-set program — not in the operational-reconstruction lineage of Hardy / CDP / Coecke-Kissinger.

---

## §1 Statement of Result

**Claim.** In $D = 3+1$ substrate dimensions (P06), the configuration-space fundamental group for $n$ identical rule-type carriers is the **permutation group** $S_n$, not the **braid group** $B_n$. Consequently, only one-dimensional representations of $S_n$ are admissible exchange-phases — namely $\eta = \pm 1$ (the trivial and sign representations) — and anyons are structurally prohibited. The dichotomy fermion/boson is exhaustive in $D = 3+1$. In $D = 2+1$, the fundamental group is $B_n$ and continuous-phase anyons exist.

form-IDENTIFIED (no D rows in audit table; downgraded from FORM-FORCED per Paper_095 §2.3) by P06 + rule-type homotopy classification + standard configuration-space topology. No new postulates.

Verdict: **M1** (pure dimension-comparison / topology-driven structural result; no inherited numerical content).

---

## §2 Primitive Inputs

### 2.1 Primitives invoked

- **P06 (Spatial dimension $D = 3+1$)** — the load-bearing primitive: forces $S_n$ rather than $B_n$.
- **P10 (Rule-type primitive)** — supplies the rule-type carriers whose exchange is considered.
- **P03 (Channel + locus indexing)** — supplies the locus indexing on which configuration space is built.

### 2.2 Upstream Dependencies

- **I-087:** 13-primitive position paper.
- **I-RQM-T1:** Spin–statistics dichotomy.
- **I-Topology:** Standard algebraic topology of configuration spaces (standard math).
- **I-Braid:** Braid-group representation theory (Leinaas–Myrheim 1977, Wilczek 1982; standard math).

---

## §3 Derivation

### 3.1 Configuration space for $n$ identical rule-types

For $n$ identical rule-type carriers in $d$ spatial dimensions, the configuration space is
$$M_n = (\mathbb{R}^d)^n \setminus \Delta \;/\; S_n ,$$
where $\Delta$ is the diagonal (coincidence set) removed because identical carriers cannot occupy the same locus, and division by $S_n$ identifies configurations related by permutation.

### 3.2 The fundamental group $\pi_1(M_n)$

Standard configuration-space topology (Leinaas–Myrheim, Wilczek; I-Topology + I-Braid):

- **$d = 3$ spatial (i.e., $D = 3+1$):** $\pi_1(M_n) = S_n$ (permutation group).
- **$d = 2$ spatial (i.e., $D = 2+1$):** $\pi_1(M_n) = B_n$ (braid group).
- **$d = 1$ spatial:** statistics degenerates (no exchange-path topology).

The dimensional crossover at $d = 3$: in three or more spatial dimensions, any loop in configuration space that effects an exchange can be deformed (without crossing the coincidence diagonal) into a loop that effects the same permutation by a different route. All such loops are homotopically equivalent → only the permutation matters → $\pi_1 = S_n$.

In two spatial dimensions, this freedom is lost: two carriers in the plane cannot pass through each other, and the order of exchange (clockwise vs counterclockwise) becomes topologically distinct → braid structure → $\pi_1 = B_n$.

### 3.3 Representations of $S_n$ vs $B_n$

**$S_n$ representations** include:
- Trivial (all permutations → $+1$): bosonic.
- Sign / alternating (even permutations → $+1$, odd → $-1$): fermionic.
- Higher-dimensional representations (Young-diagram irreducibles).

For exchange-phase purposes, only the **one-dimensional** representations of $S_n$ produce a single-valued multiplicative phase factor. There are exactly two: trivial ($\eta = +1$, bosonic) and sign ($\eta = -1$, fermionic).

**$B_n$ representations** include:
- Trivial (all braids → $+1$): bosonic.
- Sign (all generators → $-1$): fermionic.
- **Continuous-phase one-dim representations** $\eta = e^{i\theta}$ for $\theta \in [0, 2\pi)$: **anyonic**.
- Higher-dimensional non-abelian representations: non-abelian anyons.

The continuous-phase $\eta = e^{i\theta}$ exists in $B_n$ but not in $S_n$, because $B_n$ has infinite-order generators (each elementary braid generator has infinite order), while $S_n$'s transpositions have order 2 (squaring gives identity).

### 3.4 Substrate-level anyon prohibition in $D = 3+1$

In $D = 3+1$ (P06), the rule-type carriers' configuration space has $\pi_1 = S_n$. By §3.3, the only admissible one-dimensional exchange-phase representations are $\eta = \pm 1$. **Anyons (continuous-phase $\eta = e^{i\theta}$ with $\theta \notin \{0, \pi\}$) are structurally prohibited.**

This is the substrate-level basis for the empirical fact that in three-dimensional spatial settings, all known particles are either fermions or bosons. The exhaustive dichotomy in $D = 3+1$ is FORM-FORCED.

### 3.5 What is admissible in $D = 2+1$

Two-dimensional spatial substrate (hypothetical or effective; e.g., quantum-Hall surface states confined to a plane) has $\pi_1 = B_n$. Anyons are admissible.

Empirically: anyonic statistics has been observed in 2D fractional-quantum-Hall systems (Bartolomei et al. 2020; Nakamura et al. 2020). These are **effective 2D systems realized within 3D substrate**; the anyonic statistics applies to the surface degrees of freedom whose effective configuration space is two-dimensional.

The substrate framework is consistent with this: the underlying substrate is $D = 3+1$ (no anyons at substrate level), but **effective 2D surface theories** can exhibit anyonic statistics within the surface configuration space. This is a coarse-graining phenomenon, not a substrate-level anyon.

### 3.6 Connection to spin–statistics (T1)

T1 derived the exchange-phase $\eta = (-1)^{2s}$ for spin-$s$ rule-types in $D = 3+1$. Combined with this paper's result that only $\eta = \pm 1$ are admissible:

- $\eta = +1 \Rightarrow 2s$ even $\Rightarrow s \in \{0, 1, 2, ...\}$: bosonic.
- $\eta = -1 \Rightarrow 2s$ odd $\Rightarrow s \in \{1/2, 3/2, ...\}$: fermionic.

No values of $s$ produce admissible anyonic phase. The spin–statistics dichotomy is exactly the two-class limit forced by configuration-space topology.

### 3.7 Connection to Cl(3,1) (T2)

T2 derived the four-component spinor structure in $D = 3+1$. The four-component Dirac spinor is the algebraic substrate of the half-integer-spin fermionic class. T1 + T2 + T3 together establish: $D = 3+1$ supports exactly two statistics classes, with the spinor class algebraically realized by Cl(3,1).

---

## §4 Audit Table

| # | Step | Label | Notes |
|---|---|---|---|
| 1 | P06 $D = 3+1$ | P | Primitive. |
| 2 | P10 rule-type carriers | P | Primitive. |
| 3 | Configuration space $M_n = (\mathbb{R}^d)^n \setminus \Delta / S_n$ | I | Standard construction. |
| 4 | $\pi_1(M_n) = S_n$ for $d = 3$ | I | Standard topology (I-Topology, I-Braid). |
| 5 | $\pi_1(M_n) = B_n$ for $d = 2$ | I | Standard topology. |
| 6 | One-dim $S_n$ reps are exactly trivial + sign | I | Standard rep theory. |
| 7 | Continuous-phase $B_n$ reps exist | I | Standard math. |
| 8 | Anyons prohibited in $D = 3+1$ | D-via-I | Application of step 6 to step 4. |
| 9 | Anyons admissible in $D = 2+1$ | D-via-I | Application of step 7 to step 5. |
| 10 | Effective 2D surface theories may host anyonic excitations | D-via-I | Coarse-graining of $D = 3+1$ substrate to effective 2D. |
| 11 | Composition with T1 yields fermion/boson exhaustive dichotomy | D-via-I | Step 8 + T1 (inherited spin–statistics). |

---

## §5 Falsification Criteria

- **F1: Empirical detection of genuinely 3D anyonic statistics.** A particle exhibiting continuous-phase exchange in a bulk three-dimensional system (not effective 2D surface) refutes the prohibition.

- **F2: Substrate evidence that P06 permits $d = 2$ realization for substrate physics.** Would propagate from F2 of Paper_RQM_T1.

- **F3: Standard topology result $\pi_1(M_n) = S_n$ in $d = 3$ shown to be wrong.** Would refute I-Topology.

- **F4: Empirical detection of anyonic statistics in genuine 3+1D condensed-matter systems (not 2+1D surface states).** Empirical refutation target: observation of continuous-phase $\eta = e^{i\theta}$ exchange in bulk 3D — would refute the dimension-comparison argument.

---

## §6 Position Statement

Paper RQM-T3 establishes anyon prohibition in 3+1D as **M1** (form-IDENTIFIED structural dimension-comparison result; no D rows in audit table; downgraded from FORM-FORCED per Paper_095 §2.3) under P06 + P10 + P03 with no new postulates. The structural form is form-IDENTIFIED by composition of substrate primitives with standard algebraic topology of configuration spaces and standard finite-group rep theory; no numerical particle-content is inherited because the result is purely about admissible exchange-phase classes. The result joins the Wave-3 Relativistic-QM Bridge family as the dimension-comparison companion to T1 spin–statistics, complementary to T2 (Cl(3,1) algebraic substrate) and T4 (Dirac equation), serving as the load-bearing topological constraint for the fermion/boson exhaustive dichotomy in $D = 3+1$.

This paper does NOT claim that effective 2D anyonic systems are substrate-level anyons — those are coarse-graining phenomena. It does NOT claim numerical content beyond the structural dichotomy.

This paper is in the Wave-3 Relativistic-QM Bridge series of the Event Density program — a substrate-ontology research program in the lineage of 't Hooft's cellular-automaton interpretation, Wolfram's Ruliad, and the causal-set program (Sorkin et al.); NOT in the operational-reconstruction lineage of Hardy / CDP / Coecke-Kissinger.

---

## §7 Rewrite Note

This paper supplies the topological complement to Paper_RQM_T1's spin–statistics derivation. T1 derives $\eta = (-1)^{2s}$; T3 establishes that only $\eta = \pm 1$ are configuration-space-admissible in $D = 3+1$. Together they force the fermion/boson dichotomy exhaustively.

**Relationship to other RQM-bridge papers:**
- **T1 spin–statistics:** complementary; T1 supplies the polarity-rotation factor, T3 supplies the topological admissibility constraint.
- **T2 Cl(3,1):** algebraically realizes the fermionic class derived here.
- **T4 Dirac:** uses the four-component spinor structure for the fermionic sector identified here.

**Coarse-graining note:** Effective 2D surface theories (e.g., quantum Hall edge states) can host anyonic excitations; this is consistent with the substrate framework since the **effective configuration space** of confined-to-2D excitations is two-dimensional, with corresponding $\pi_1 = B_n$. The substrate itself remains $D = 3+1$.

**Form IDENTIFIED.** The anyon-prohibition result is structurally identified by P06 + standard topology (no D rows in audit table; downgraded from FORM-FORCED per Paper_095 §2.3). **Values inherited:** specific anyonic phases observed in 2D systems are INHERITED from condensed-matter experimental matching.

Verdict: **M1**.

---

**End Paper RQM-T3.**
