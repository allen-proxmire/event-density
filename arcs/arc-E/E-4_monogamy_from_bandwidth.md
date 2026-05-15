# Arc E — Memo 4: Monogamy of Entanglement from Cross-Chain Bandwidth Budgets

**Status:** First substantive-derivation memo of Arc E. Conditional on E-1 (tensor product FORM-FORCED), E-2 (generic non-factorizability FORCED), E-3 (Schmidt FORM-FORCED, values-INHERITED). Independent of E-5 (no-signaling). No new primitives. Identification-not-derivation discipline observed: CKW inequality is identification target downstream, not derivation premise.

**Date:** 2026-05-08

---

## 1. The CANDIDATE Statement

> **CANDIDATE (E4).** *Given E-1 (tensor product joint Hilbert space) plus the substrate cross-chain bandwidth structure $\Gamma_{\mathrm{cross}} \sim \exp[-\alpha\sigma]$ established in Q-COMPUTE Memo 1 / BH-2 / DCGT, plus bandwidth-additivity (P04), the entanglement that any single substrate endpoint $A$ can simultaneously share with two other endpoints $B$ and $C$ is jointly constrained by a finite local bandwidth budget $\Gamma_{\mathrm{max}}(A)$. In particular, full A–B entanglement (saturation of $\Gamma_{\mathrm{max}}(A)$ in the A→B channel) precludes any A–C entanglement. The qualitative monogamy structure is FORM-FORCED at the substrate level. The Coffman–Kundu–Wootters squared coefficient $C_{AB}^2 + C_{AC}^2 \leq C_{A(BC)}^2$ is COEFFICIENT-INHERITED via the amplitude-vs-probability squaring relationship between concurrence and substrate bandwidth.*

The CANDIDATE has four pieces, derived in order:

- **(M1) Local bandwidth-budget bound.** Each substrate endpoint $A$ has a finite, locally-determined total outgoing cross-chain bandwidth $\Gamma_{\mathrm{max}}(A)$.
- **(M2) Bandwidth-entanglement linkage.** Substrate cross-chain bandwidth $\Gamma_{XY}$ is the substrate quantity that supports entanglement between endpoints $X$ and $Y$. Maximally-entangled bipartite states saturate $\Gamma_{XY}$ at the smaller of the two endpoints' local maxima.
- **(M3) Qualitative monogamy.** $\Gamma_{AB} + \Gamma_{AC} \leq \Gamma_{\mathrm{max}}(A)$ via P04. Full A–B entanglement implies $\Gamma_{AC} = 0$, hence no A–C entanglement.
- **(M4) Quantitative CKW structure.** The squared form $C_{AB}^2 + C_{AC}^2 \leq C_{A(BC)}^2$ identifies with substrate bandwidth-additivity at the probability (squared-amplitude) level.

E-4 is a substantive-derivation memo: (M1) and (M3) are substrate-derived; (M2) is the load-bearing structural identification; (M4) is value-inherited identification with the standard QM monogamy inequality.

---

## 2. Substrate Inputs (Inheritance)

| Input | Status | Role |
|---|---|---|
| **E-1** (tensor product FORM-FORCED) | Closed (this arc) | Tripartite joint space $\mathcal{H}_A \otimes \mathcal{H}_B \otimes \mathcal{H}_C$ well-defined; partial traces over any subsystem well-defined |
| **E-2** (generic non-factorizability) | Closed (this arc) | (SP) configurations are generic; (IP) factorization is exceptional |
| **E-3** (Schmidt FORM-FORCED) | Closed (this arc) | Bipartite Schmidt rank counts substrate-shared channels; coefficients $\sqrt{\lambda_i}$ weight them |
| **U2** (single-endpoint inner-product) | FORCED-unconditional | Inner products and partial traces well-defined on each subsystem |
| **T10** (Born rule) | FORCED-unconditional | Probability assignment for joint outcomes |
| **P04** (bandwidth additivity for independent contributions) | Primitive | Independent substrate channels add bandwidth additively |
| **Q-COMPUTE Memo 1 invariants** ($\mathcal{M}$, $\mathcal{U}$, $\sigma$, $\Gamma_{\mathrm{cross}}$) | Closed-arc inheritance | Substrate-level bandwidth machinery; $\mathcal{M}(A)$ is finite per substrate region |
| **BH-2 / BH-4 decoupling-surface bandwidth** | Closed-arc inheritance | $\Gamma_{\mathrm{cross}} \sim \exp[-\alpha\sigma]$ and entanglement-straddling-at-saturation |
| **DCGT** (substrate-to-continuum) | Closed-arc inheritance | Bandwidth-budget structure survives coarse-graining; continuum entanglement measures are the coarse-grained images of substrate bandwidths |
| **ED-I-01** (multiplicity-as-entropy-analogue) | Interpretation | Finite local multiplicity bounds total outgoing bandwidth |
| **ED-I-02** (single undeveloped participation rule) | Interpretation | Substrate reading: A cannot share one rule fully with B *and* fully with C — a single rule has bounded structural capacity |
| **T18** (V1 forward-cone-only kernel) | FORCED-unconditional | V1-mediated cross-chain correlations are bandwidth-bounded; no copying without dilution |

**No new primitives.** **No use of E-5 (no-signaling) or E-6 (entropy form).**

---

## 3. Derivation of (M1): Local Bandwidth-Budget Bound

### 3.1 Finite local multiplicity at any substrate region

Q-COMPUTE Memo 1 §2.2 (D1) defines $\mathcal{M}(\mathcal{S})$ as the count of substrate-resolvable participation channels at region $\mathcal{S}$. For a substrate region of finite participation density $\rho_{\mathrm{local}}$ and finite spatial extent, $\mathcal{M}(A) < \infty$.

This finiteness is itself FORCED by ED-I-01 §2.3 (multiplicity-as-entropy-analogue with finite-density substrate) + BH-2's gradient-sparsity definition $\sigma = |\nabla\rho|\ell_P^2/\rho_{\mathrm{local}}$ which produces well-defined finite values at any non-degenerate substrate region.

### 3.2 Outgoing-bandwidth bound from local multiplicity

The cross-chain bandwidth from $A$ to any other region $X$ is mediated by V1-kernel cross-chain correlations originating at $A$. The total outgoing bandwidth from $A$ — summed over all regions $X$ that $A$ couples to — is bounded by $A$'s capacity to source cross-chain correlations, which is in turn bounded by $\mathcal{M}(A)$.

Concretely: each substrate-resolvable channel at $A$ can be engaged in cross-chain correlations with at most one external region's channel at full strength (or distributed across multiple external regions at partial strength). Q-COMPUTE Memo 1 §2.2 (D2) supplies the dynamical-state quantifier $\mathcal{U}$, but the *capacity* — the substrate quantity that bounds the total — is set by $\mathcal{M}(A)$ per substrate timescale.

Define:

$$\Gamma_{\mathrm{max}}(A) := \sup_{\{X_k\}} \sum_k \Gamma_{A \to X_k},$$

the supremum of total outgoing cross-chain bandwidth across any partitioning of A's external couplings. By the substrate-finiteness of $\mathcal{M}(A)$ and the bounded V1-kernel coupling per channel,

$$\Gamma_{\mathrm{max}}(A) < \infty \qquad \text{and} \qquad \Gamma_{\mathrm{max}}(A) \propto \mathcal{M}(A).$$

The proportionality constant is INHERITED from the V1-kernel functional form (specifically: the per-channel saturation bandwidth, which is set by ℓ_P, $\hbar$, and substrate density at $A$). The form $\Gamma_{\mathrm{max}}(A) \propto \mathcal{M}(A)$ is FORCED.

### 3.3 Bandwidth-additivity from P04

P04 (bandwidth additivity for independent contributions) establishes that independent substrate channels contribute additively to total bandwidth. For non-overlapping cross-chain couplings $A \to B$ and $A \to C$ (i.e., couplings via distinct A-side channels), the bandwidths add:

$$\Gamma_{A \to B} + \Gamma_{A \to C} \leq \Gamma_{\mathrm{max}}(A).$$

The inequality (rather than equality) accounts for the possibility that some of A's channels are unused — A's outgoing bandwidth need not be saturated.

Independence of A-side channels is the substrate condition for additivity. If A's coupling to B and A's coupling to C share *the same* A-side channels, they are not P04-independent, and the additive bound does not apply directly — but the *capacity* bound $\Gamma_{\mathrm{max}}(A)$ still does, since shared channels cannot exceed their own per-channel maximum.

**(M1) is FORCED** by Q-COMPUTE Memo 1 + BH-2 + ED-I-01 + P04.

---

## 4. Derivation of (M2): Bandwidth-Entanglement Linkage

This is the load-bearing structural identification of the memo.

### 4.1 Schmidt rank requires substrate-shared channels (E-3 substrate reading)

E-3 §5.1 established the substrate reading: bipartite Schmidt rank $r$ between $A$ and $B$ counts the substrate-shared participation channels between $A$ and $B$. Each shared channel corresponds to one nonzero Schmidt coefficient $\sqrt{\lambda_i}$.

A *shared* channel between A and B is precisely a substrate cross-chain correlation channel — i.e., a contribution to $\Gamma_{AB}$. Therefore:

$$\text{Schmidt rank } r_{AB} > 0 \iff \Gamma_{AB} > 0.$$

(Schmidt rank 1 with $\lambda_1 = 1$ corresponds to a (IP) configuration — A and B independently prepared, no shared channels — and matches $\Gamma_{AB} = 0$.)

### 4.2 Strength of entanglement is bandwidth-monotone

The total *strength* of entanglement between A and B — measured by any standard bipartite entanglement measure (concurrence, entanglement of formation, von Neumann entropy of reduced state, negativity) — is monotonically related to the substrate-coupling-strength of the shared channels.

Operational reading at the substrate level:

- If only one shared channel is active with weight $\sqrt{\lambda_1} \approx 1$ and Schmidt rank $r = 1$: A and B are weakly entangled or unentangled. Substrate cross-bandwidth $\Gamma_{AB}$ is small.
- If multiple shared channels are active with comparable weights: Schmidt rank is higher; entanglement strength is higher. Substrate cross-bandwidth $\Gamma_{AB}$ is larger.
- If the shared-channel structure is maximal — Schmidt rank $r = \min(d_A, d_B)$ with all $\lambda_i = 1/r$ equal — A and B are *maximally entangled*. Substrate cross-bandwidth $\Gamma_{AB}$ is at its A-side maximum (or B-side maximum, whichever is smaller).

Formally:

$$E(\rho_{AB}) = F(\Gamma_{AB}) \quad \text{with $F$ monotone increasing}, \qquad E_{\max}(d_A, d_B) = F(\min(\Gamma_{\mathrm{max}}(A), \Gamma_{\mathrm{max}}(B))).$$

The *exact functional form* of $F$ depends on which entanglement measure is used and on the V1-kernel's amplitude-vs-probability calibration. The monotonicity itself is FORCED. The specific $F$ is INHERITED from continuum-mathematical structure.

### 4.3 Maximal entanglement saturates the smaller endpoint's bandwidth

For a maximally-entangled bipartite state on $\mathcal{H}_A \otimes \mathcal{H}_B$ with $d_A \leq d_B$ (without loss of generality), the Schmidt rank is $d_A$ and all coefficients are $\sqrt{1/d_A}$. The substrate has every A-side channel coupled to one B-side channel with full available bandwidth. This is

$$\Gamma_{AB}^{\mathrm{max}} = \Gamma_{\mathrm{max}}(A).$$

A's entire outgoing bandwidth is engaged with B in this configuration. By the (M1) bound, no A-side bandwidth remains for any third region.

### 4.4 The linkage is FORCED at qualitative level, INHERITED at quantitative level

(M2) qualitative form — entanglement requires shared channels, and shared channels are bandwidth — is FORCED by E-3 substrate reading + Q-COMPUTE Memo 1 + BH-2.

(M2) quantitative form — the specific monotone $F$ mapping $\Gamma$ to a particular entanglement measure — is INHERITED from continuum-mathematical structure. We will not derive $F$ here; we identify that *some* monotone exists (FORCED) and that *which* monotone applies depends on which measure (concurrence, EoF, negativity, etc.) is invoked (INHERITED).

This is the canonical form-FORCED-coefficient-INHERITED pattern.

---

## 5. Derivation of (M3): Qualitative Monogamy

### 5.1 The constraint

Combine (M1) and (M2):

- (M1): $\Gamma_{A \to B} + \Gamma_{A \to C} \leq \Gamma_{\mathrm{max}}(A)$.
- (M2): entanglement strength between $A$ and $X$ is monotone in $\Gamma_{A \to X}$, with maximum entanglement saturating $\Gamma_{\mathrm{max}}(A)$.

If A and B are maximally entangled — $\Gamma_{A \to B} = \Gamma_{\mathrm{max}}(A)$ — then $\Gamma_{A \to C} = 0$ by (M1). By (M2)'s monotone link, $\Gamma_{A \to C} = 0$ implies zero entanglement strength between A and C.

**Therefore: full A–B entanglement implies zero A–C entanglement.**

### 5.2 Beyond maximal: continuous monogamy

For non-maximal A–B entanglement ($\Gamma_{A \to B} < \Gamma_{\mathrm{max}}(A)$), some bandwidth budget remains for A–C, but the residual is bounded:

$$\Gamma_{A \to C} \leq \Gamma_{\mathrm{max}}(A) - \Gamma_{A \to B}.$$

Through (M2)'s monotone $F$, this maps to a bound on A–C entanglement strength as a function of A–B entanglement strength. The bound is *strict* monotone-decreasing: stronger A–B entanglement leaves strictly less budget for A–C, hence strictly weaker A–C entanglement.

### 5.3 Substrate channels confirming the constraint

Each substrate channel that could conceivably bypass the bandwidth budget is checked:

- **V1 kernel duplication?** The V1 kernel cannot freely duplicate a substrate-coupling channel from A to two distinct external regions at full strength. Forward-cone-only propagation (T18) plus finite per-channel bandwidth at A constrain the V1-kernel-mediated coupling to bandwidth-budget-respecting configurations. No duplication channel exists.
- **ED-I-02 shared-rule splitting?** The "single undeveloped participation rule" framework explicitly says A and B share *one* rule — not two copies of one rule. If A simultaneously shared "one rule" fully with B and "one rule" fully with C, this would require A to support two distinct full-strength shared-rule structures simultaneously, which contradicts the finite-channel-capacity reading of ED-I-02 + ED-I-01. ED-I-02 is consistent with monogamy and indeed predicts it ontologically.
- **BH-4 entanglement-straddling at decoupling surfaces?** At a saturated decoupling surface (BH-2 horizon mechanism), the cross-bandwidth $\Gamma_{\mathrm{cross}}$ is exactly saturated. Adding a second straddling channel from the same A-side region requires additional A-side capacity, which (M1) bounds. The BH-4 mechanism is bandwidth-budget-respecting.
- **GHZ-class three-body correlations?** GHZ states $\frac{1}{\sqrt{2}}(|000\rangle + |111\rangle)$ have Schmidt rank 2 across any bipartition $A | BC$, but bipartite reduced states $\rho_{AB} = \frac{1}{2}(|00\rangle\langle 00| + |11\rangle\langle 11|)$ are *separable*. So GHZ does not violate monogamy — A is entangled with the joint $BC$ system, but not bipartitely with $B$ alone or $C$ alone. The bandwidth reading: A's outgoing bandwidth in GHZ goes to a *joint* three-body channel rather than splitting between independent A-B and A-C channels. Bandwidth budget respected.
- **Multipartite W-class states?** $|W\rangle = \frac{1}{\sqrt{3}}(|001\rangle + |010\rangle + |100\rangle)$ has nonzero bipartite entanglement A-B and A-C, but neither saturates $\Gamma_{\mathrm{max}}(A)$. The bipartite entanglements are *partial* and their squared sum is bounded by $C_{A(BC)}^2$ — exactly the CKW inequality. Bandwidth budget respected with strict inequality.

All substrate channels and standard multipartite-state classes confirm the constraint.

**(M3) qualitative monogamy is FORCED.**

---

## 6. Derivation of (M4): CKW Squared Structure (Coefficient-INHERITED)

### 6.1 The CKW inequality

For a tripartite pure state $|\Psi\rangle_{ABC}$ on three qubits, the Coffman–Kundu–Wootters inequality (Coffman, Kundu, Wootters 2000) reads:

$$C_{AB}^2 + C_{AC}^2 \leq C_{A(BC)}^2,$$

where $C_{XY}$ is the Wootters concurrence between $X$ and $Y$. For higher-dimensional subsystems, analogous monogamy inequalities hold for various entanglement measures (squashed entanglement, entanglement of formation in some cases).

### 6.2 Substrate reading of the squared structure

Concurrence $C_{XY}$ is amplitude-like: for a maximally-entangled two-qubit state, $C = 1$; for a separable state, $C = 0$; for a pure state $|\Psi\rangle = \sum_i \sqrt{\lambda_i} |i i\rangle$, $C = 2\sqrt{\lambda_1 \lambda_2}$ (for two qubits) — proportional to a product of Schmidt-coefficient amplitudes.

Concurrence-squared is therefore probability-like: $C^2 \propto \lambda_i \lambda_j$ — products of probabilities, which add additively under independent contributions.

The substrate identification:

- **Concurrence $C_{XY}$** ↔ amplitude of substrate cross-chain coupling between $X$ and $Y$ (specifically: $\sqrt{\Gamma_{XY}/\Gamma_{\mathrm{ref}}}$ for some reference scale).
- **Concurrence-squared $C_{XY}^2$** ↔ substrate bandwidth fraction $\Gamma_{XY} / \Gamma_{\mathrm{ref}}$ (probability-like quantity).

Bandwidth additivity (P04) at the *probability* level gives:

$$\frac{\Gamma_{AB}}{\Gamma_{\mathrm{max}}(A)} + \frac{\Gamma_{AC}}{\Gamma_{\mathrm{max}}(A)} \leq 1,$$

which under the identification becomes:

$$C_{AB}^2 + C_{AC}^2 \leq C_{A(BC)}^2,$$

with $C_{A(BC)}^2 \leq 1$ identifying with $\Gamma_{A \to (BC)} / \Gamma_{\mathrm{max}}(A) \leq 1$.

### 6.3 Why the structure is COEFFICIENT-INHERITED rather than FORM-FORCED

The *form* — squared-amplitudes-add-additively — *is* FORCED by (M3) plus the amplitude-vs-probability squaring relationship that holds whenever a quantum amplitude is mapped to a probability through Born's rule. So in a sense the squared structure is form-FORCED.

The *coefficient* — the specific "1" on the right-hand side, the specific concurrence definition, the specific 2-qubit reduction — is INHERITED from:
- (a) Wootters' choice of concurrence as the amplitude variable;
- (b) the specific dimensional structure of two-qubit Hilbert space;
- (c) the calibration of $\Gamma_{\mathrm{ref}}$ to the maximally-entangled-state bandwidth.

For higher-dimensional subsystems or other entanglement measures (squashed entanglement, conditional mutual information), analogous but quantitatively different monogamy bounds hold. Each is COEFFICIENT-INHERITED from the specific measure's calibration; the structural FORCED content is the same: bandwidth-budget bound with amplitude-squared additivity.

**(M4) is FORM-FORCED-via-(M3)-plus-Born-squaring + COEFFICIENT-INHERITED via the choice of entanglement measure.**

---

## 7. Multipartite Generalization Audit

### 7.1 A–(BC) joint partition

For a tripartite pure state, A's entanglement with the joint BC system is bounded by

$$\Gamma_{A \to (BC)} \leq \Gamma_{\mathrm{max}}(A),$$

since A's total outgoing bandwidth is bounded irrespective of how it is distributed.

For partial sub-allocations:

$$\Gamma_{A \to B} + \Gamma_{A \to C} + \Gamma_{A \to (BC)\,\mathrm{joint}} \leq \Gamma_{\mathrm{max}}(A),$$

where $\Gamma_{A \to (BC)\,\mathrm{joint}}$ accounts for three-body correlations (GHZ-class) that engage A with the joint BC system in a way irreducible to bipartite A-B and A-C channels.

### 7.2 N-party generalization

For an N-party pure state with A and $N - 1$ other endpoints $\{B_1, \ldots, B_{N-1}\}$,

$$\sum_{k} \Gamma_{A \to B_k} + \sum_{S \subset \{B_1, \ldots, B_{N-1}\}, |S| \geq 2} \Gamma_{A \to S\,\mathrm{joint}} \leq \Gamma_{\mathrm{max}}(A).$$

This produces an N-party monogamy hierarchy: A's bipartite entanglement with each individual $B_k$ is bounded by the unused part of $\Gamma_{\mathrm{max}}(A)$ after accounting for all bipartite and multipartite correlations.

The structural feature — *finite outgoing bandwidth budget at A* — is preserved. The form FORCED at three-party generalizes to N-party.

### 7.3 Continuum extension via DCGT

DCGT (Diffusion Coarse-Graining Theorem) bridges substrate bandwidth budgets to continuum entanglement measures. The continuum mapping:

- Substrate $\Gamma_{XY}$ → continuum entanglement-measure (concurrence, EoF, negativity)
- Substrate $\Gamma_{\mathrm{max}}(A)$ → continuum maximum entanglement strength A can support
- Substrate bandwidth-additivity (P04) → continuum monogamy inequality

DCGT preserves linear-algebraic structure (E-1), and bandwidth-budget structure is a feature of the substrate's local participation density rather than a substrate-specific microscopic detail. The continuum monogamy inequality therefore inherits FORCED status from the substrate result via DCGT.

---

## 8. Verdict

> **VERDICT (E4): FORM-FORCED, COEFFICIENT-INHERITED.**
>
> Qualitative monogamy of entanglement — specifically, that no substrate endpoint $A$ can be simultaneously maximally entangled with two distinct other endpoints $B$ and $C$ — is FORCED at the substrate level by Q-COMPUTE Memo 1's $\mathcal{M}(A)$ finiteness + BH-2 / DCGT cross-chain bandwidth structure + P04 bandwidth additivity, combined with E-1's tensor product and E-3's substrate reading of Schmidt rank as substrate-shared-channel count. Quantitative monogamy in the form of the CKW inequality $C_{AB}^2 + C_{AC}^2 \leq C_{A(BC)}^2$ is identified with substrate bandwidth-budget additivity at the probability (squared-amplitude) level. The form-FORCED content is the bandwidth-budget bound + bandwidth-monotone entanglement linkage. The COEFFICIENT-INHERITED content is the specific entanglement measure's calibration (concurrence, EoF, etc.).

**Verdict-class details:**

- **Form-FORCED:** existence of a finite local bandwidth budget at any substrate endpoint; bandwidth-additivity of independent contributions; monotone link between bandwidth and entanglement strength; impossibility of simultaneous maximal A-B and A-C entanglement.
- **Coefficient-INHERITED:** the specific functional form $F$ mapping bandwidth $\Gamma$ to a chosen entanglement measure; the specific CKW-type inequality coefficients; the dimensional reductions (2-qubit, qudit, continuous-variable) that produce specific coefficient values.
- **No CONDITIONAL caveat survived the audit.** Each conceivable substrate-channel that could bypass the budget was checked and confirmed bandwidth-respecting.
- **No NOT-FORCED option survived.** The substrate has finite local participation density (Q-COMPUTE Memo 1 + ED-I-01), and that finiteness propagates to finite outgoing bandwidth (ED-I-01 + P04).
- **No new active CANDIDATEs.** Active CANDIDATE inventory remains {}.

---

## 9. Circularity Audit

| Potential circularity | Audit verdict |
|---|---|
| E-5 (no-signaling) used as derivation premise? | **No.** Not invoked. (Note: §5.3's V1 kernel discussion uses T18 as input, not E-5's derived no-signaling result.) |
| E-6 (entropy form) used as derivation premise? | **No.** Bandwidth-vs-entanglement linkage in §4 uses Schmidt rank from E-3, not entropy from E-6. |
| E-7 (synthesis) used as derivation premise? | **No.** Not invoked. |
| Self-reference of E-4 within itself? | **No.** §3 → §4 → §5 → §6 → §7 derivation chain is acyclic. |
| E-1, E-2, E-3 used only as inputs? | **Confirmed.** E-1 supplies tensor product; E-2 supplies (IP)/(SP) reading; E-3 supplies Schmidt-rank-as-shared-channel-count substrate reading. None re-derived. |
| CKW inequality used as derivation premise? | **No.** CKW appears in §6 as identification target downstream, not derivation input. The substrate derivation in §3–§5 is independent of CKW; §6 then identifies the substrate result with the CKW form. |
| Q-COMPUTE Memo 1 used as input not as conclusion? | **Confirmed.** Q-COMPUTE Memo 1's invariants ($\mathcal{M}$, $\mathcal{U}$, $\sigma$, $\Gamma_{\mathrm{cross}}$) are taken as substrate-derived from Q-COMPUTE arc closure; not re-derived. |
| BH-2 / BH-4 used as inputs not conclusions? | **Confirmed.** Decoupling-surface bandwidth structure inherited from Arc BH closure; not re-derived. |

**Acyclicity confirmed.**

---

## 10. Falsification

### 10.1 Falsifier for FORM-FORCED, COEFFICIENT-INHERITED verdict (current verdict)

A substrate construction satisfying all of E-1, P04, Q-COMPUTE Memo 1, BH-2, DCGT, and ED-I-02, in which a single substrate endpoint $A$ is simultaneously maximally entangled with two distinct other endpoints $B$ and $C$. Concretely: $\Gamma_{AB} = \Gamma_{\mathrm{max}}(A)$ AND $\Gamma_{AC} = \Gamma_{\mathrm{max}}(A)$ simultaneously, with $\Gamma_{\mathrm{max}}(A) > 0$.

This would require $\Gamma_{\mathrm{max}}(A)$ to be doubled (or infinite) — contradicting Q-COMPUTE Memo 1's $\mathcal{M}(A)$-finiteness or P04's additivity.

### 10.2 Falsifier for CONDITIONAL verdict (rejected)

An auxiliary assumption beyond Q-COMPUTE Memo 1 + BH-2 + P04 + E-1 + E-3 that is required for the §3–§5 derivation. The audit identifies none. The bandwidth-vs-entanglement monotone link in (M2) is FORCED qualitatively; quantitatively it is INHERITED, not auxiliary-conditional.

### 10.3 Falsifier for NOT-FORCED verdict (rejected)

A substrate-level construction with infinite or unbounded local bandwidth at $A$, permitting unbounded simultaneous entanglement with multiple endpoints. Refuted by Q-COMPUTE Memo 1's finite-multiplicity result + ED-I-01.

### 10.4 Empirical-side falsifier

Any experimental observation of a quantum system in which a single qubit (or higher-dim subsystem) is *simultaneously* maximally entangled with two distinct other systems. By the standard CKW theorem in QM, this is mathematically impossible for pure tripartite states. Experimental verification of CKW (e.g., quantum-state-tomography of various tripartite states) consistently confirms the inequality. ED-derived monogamy is empirically equivalent to standard QM monogamy; experimental falsification of one is falsification of the other.

### 10.5 Subtle empirical edge case

For *mixed* states, monogamy inequalities are weaker (e.g., for entanglement of formation) and counterexamples to naive squared-monogamy exist for some mixed states. The bandwidth-budget framework predicts monogamy for *pure* tripartite states (analogous to standard CKW); mixed-state monogamy is downstream of mixed-state Schmidt structure (which E-3 explicitly deferred). A future arc memo treating mixed states would need to extend §4's bandwidth-vs-entanglement link to operator-valued cross-chain coupling — a structurally analogous but quantitatively distinct extension.

---

## 11. Consequences for the Arc

1. **E-4 closes as substantive-derivation memo.** Monogamy is FORM-FORCED. The substrate-level mechanism (finite local bandwidth budget) is structurally simpler than the standard QM derivation route (which goes through specific concurrence properties and trace inequalities); ED's framework reframes monogamy as a bandwidth-conservation phenomenon.

2. **Cross-domain coupling: Q-COMPUTE bandwidth ceiling.** Q-COMPUTE Memo 5's multiplicity-cap function $M$ has a Class C (high-multiplicity-redundancy) prediction of a *correlation-budget plateau*: redundancy-based architectures saturate at $N_{\mathrm{corr}}$ correlated qubits because cross-bandwidth budget is finite. E-4's monogamy is the *bipartite-projection* of the same bandwidth-budget structure that produces Q-COMPUTE's Class C plateau. This is a structural unification: the substrate bandwidth budget controls both monogamy (E-4) and Class-C entanglement-bandwidth-ceiling (Q-COMPUTE).

3. **Cross-domain coupling: BH-4 entanglement-straddling.** BH-4 establishes that entanglement-straddling at saturated decoupling surfaces engages the full local cross-bandwidth budget. This is BH's version of monogamy: a BH horizon endpoint cannot be simultaneously fully entangled with the BH interior *and* fully entangled with infalling matter — the bandwidth budget at the horizon is finite and shared. E-4 + BH-4 are the same bandwidth-budget mechanism at different scales.

4. **Cross-domain echo: B1 over-determination.** The substrate over-determination of monogamy (Q-COMPUTE finite-$\mathcal{M}$ + ED-I-01 finite-multiplicity + P04 additivity + ED-I-02 single-rule structural-capacity-bound) parallels E-5's three-lock structure for no-signaling and B1's cascade-from-V1 + R1-bypass redundancy for time's arrow. **Over-determination is emerging as a recurrent structural feature of ED's substrate-level results.**

5. **E-6 (entropy form) is now structurally enabled for cross-checks.** Entanglement entropy as the natural quantitative measure of bandwidth saturation: $S(\rho_A) = -\sum_i \lambda_i \log \lambda_i$ tracks how much of A's bandwidth is engaged with B. Maximal $S$ corresponds to maximal saturation; zero $S$ corresponds to unused bandwidth. E-6 will derive the entropy form; with E-4 in hand, the substrate reading of entropy as "bandwidth-saturation measure" is available.

6. **No new active CANDIDATEs.** Active CANDIDATE inventory remains {}.

7. **No new sensitivity flags beyond inherited ones.** E-4 inherits Q-COMPUTE Memo 1's $\mathcal{M}$-finiteness load-bearing + ED-I-01's multiplicity-as-entropy-analogue. No new load-bearings introduced.

---

## 12. Summary

**What this memo accomplished.**

- Stated the E-4 CANDIDATE (§1), decomposed it into (M1)–(M4): local bandwidth-budget bound, bandwidth-entanglement linkage, qualitative monogamy, CKW squared structure.
- Derived (M1) via Q-COMPUTE Memo 1's $\mathcal{M}(A)$-finiteness + BH-2 cross-bandwidth + P04 additivity (§3).
- Identified (M2) as the load-bearing structural identification: Schmidt-rank counts substrate-shared channels (E-3 reading); bandwidth-monotone link to entanglement strength is FORCED qualitatively, INHERITED quantitatively (§4).
- Derived (M3) qualitative monogamy: $\Gamma_{AB} + \Gamma_{AC} \leq \Gamma_{\mathrm{max}}(A)$ ⟹ full A-B precludes A-C. Audited V1 / ED-I-02 / BH-4 / GHZ / W substrate channels (§5).
- Identified (M4) CKW squared structure with substrate bandwidth-additivity at probability level via amplitude-squared mapping; coefficient-INHERITED from chosen entanglement measure (§6).
- Audited multipartite generalization (§7): N-party hierarchy preserves the bandwidth-budget structure; DCGT bridges to continuum.
- Issued the verdict: **FORM-FORCED, COEFFICIENT-INHERITED** (§8).
- Confirmed acyclicity (§9) and provided substrate-level falsifiers (§10).
- Identified cross-domain unifications (§11): bandwidth-budget mechanism shared with Q-COMPUTE Class C plateau, BH-4 straddling, and B1 over-determination pattern.

**What this memo did not do.**

- Did not derive the *specific* functional form $F$ mapping substrate bandwidth $\Gamma$ to standard entanglement measures. This is INHERITED from continuum-mathematical structure and would require a dedicated mapping memo (potentially flagged as O-E-Bandwidth-Map for downstream work).
- Did not derive mixed-state monogamy. Mixed-state Schmidt structure is downstream of E-3's pure-state focus; mixed-state bandwidth-vs-entanglement link is not addressed.
- Did not derive the CKW *inequality* directly — only identified its structural form with substrate bandwidth-additivity at the probability level.
- Did not derive Q-COMPUTE's Class C plateau specifically (Q-COMPUTE Memo 6's job). Cross-domain unification noted; explicit identification deferred to E-7 synthesis.
- Did not address dynamical monogamy (how bandwidth budgets evolve under unitary evolution and measurement). This is a downstream topic if Arc E develops a dynamical-monogamy memo.

**Recommended next steps.**

1. **E-6 (next memo): Entanglement-entropy form $S = -\sum_i \lambda_i \log \lambda_i$.** Second substantive-derivation memo. Substrate inputs: E-3 Schmidt eigenvalues + ED-I-01 multiplicity-as-entropy + Shannon-Khinchin axioms applied at substrate level + bandwidth-saturation reading enabled by E-4. Expected verdict: form-FORCED, coefficient-INHERITED, parallel to BH-5 area-law. Estimated 1–2 sessions.

2. **(After E-6) E-7 synthesis.** Cross-domain echoes with BH-4 (entanglement-straddling), Q-COMPUTE (bandwidth ceiling, Class C plateau), Phase-1 (Bell–Tsirelson with no-signaling jointly characterizing quantum correlations). ER=EPR-class structural reading via the bandwidth-budget unification identified in §11. Honest "no echo found" is a valid outcome.

3. **(Optional, low priority) O-E-Bandwidth-Map open item.** The specific functional form $F: \Gamma \to E(\rho_{AB})$ for various entanglement measures would map substrate bandwidth quantitatively to continuum quantum-information measures. Would close the value-INHERITED gap in (M2). Estimated 2–3 sessions if pursued. Defer to post-arc-E follow-up.

4. **(Documentation) Phase-1 / Q-COMPUTE inheritance ledger update.** With E-4 closed, monogamy is now substrate-derived rather than QM-imported. Phase-1 and Q-COMPUTE's external inheritance footprints can be tightened. Documentation, not new derivation.

---

**Pause for further instruction.**
