# Paper_058 — Class-C Correlation-Budget Plateau

**Series:** Event Density (ED) Generative Papers — Wave-2 Q-COMPUTE arc (completes pure-class triple)
**Author:** Allen Proxmire
**Status:** Publication draft
**Date:** 2026-05-13
**Repository target:** `domain-arcs/q-compute/Paper_058_ClassC_Plateau.md` (ED-Generative)
**Genre:** Conditional structural derivation within the 13-Primitive Generative System.

---

## Preamble: What This Paper Does NOT Claim *(written first per QC discipline)*

1. **The 13 primitives are not derived** (Paper_087).
2. **UR-1 is not re-derived** (Paper_054 upstream).
3. **No claim that Class-C is the unique substrate-level account of redundancy/error-correction protection.** Standard fault-tolerant quantum computing supplies alternative descriptions; Class-C is the substrate-level account of redundancy-engagement of lever C (preventing UR-1.3 failure).
4. **No strict bijection between Class-C and UR-1.3.** Dominant-lever framing (Paper_054 §6) applies; hybrid platforms exhibit intermediate behavior.
5. **The plateau saturation value $B_{\mathrm{cross,max}}$ is not derived from primitives.** Value-layer inherited from V5 envelope structure + platform-specific redundancy budget; substrate-level *form* (plateau) is structural.
6. **No claim of derivation of specific error-correction codes** (Shor, Steane, surface code, concatenated codes). The substrate-level mechanism is redundancy-band saturation; specific code structure is value-layer / platform design.
7. **No claim of fault-tolerance theorem derivation.** Standard fault-tolerance threshold theorems remain operative in their domain; Class-C provides substrate-level mechanism for redundancy-engagement of UR-1.3, not a re-derivation of fault tolerance.
8. **No claim that Class-C operates outside dominant-lever framing.** Plateau form is conditional on pure-Class-C; hybrid Class-A/C and Class-B/C admixtures exhibit modified behaviors.

---

## Abstract

This paper develops **Class-C correlation-budget plateau** as a downstream structural consequence of the ED 13-Primitive Generative System, completing the Q-COMPUTE pure-class triple (Class-A, Paper_056; Class-B, Paper_057; Class-C, this paper). Class-C platforms — engaging engineering lever C (high-multiplicity redundancy / error correction) to prevent **UR-1.3 failure** (single-channel commitment-injection rate exceeding individuation rate) — exhibit a **substrate-level correlation-budget plateau** as the redundancy parameter $R_C$ (number of redundant substrate-channels carrying the protected state) grows. Specifically, the substrate-level **error-suppression rate** for UR-1.3 failure saturates:

$$
\Gamma_{\mathrm{UR\text{-}1.3,fail}}^{\mathrm{Class\text{-}C}}(R_C) \to \Gamma_{\mathrm{plateau}}\quad \text{as } R_C \to R_C^{\mathrm{sat}},
$$

where $R_C^{\mathrm{sat}}$ is the substrate-level redundancy-saturation parameter set by V5 cross-chain correlation budget. The plateau form (rather than monotonically-decreasing suppression) arises because **substrate-level cross-chain correlation budget is finite** (P-Corr-Budget postulate, §2): once redundancy saturates the substrate's cross-chain correlation capacity, additional redundancy cannot further suppress UR-1.3 failure. The substrate-level mechanism is **redundancy-band saturation**, distinct from Class-A multiplicity-cap (UR-1.1) and Class-B exponential gap-suppression (UR-1.2). The paper makes no claim of specific error-correction-code derivation, no claim of unique substrate mechanism, and no claim of fault-tolerance theorem replacement.

---

## 1. Introduction

### 1.1 What this paper does

This paper develops **Class-C correlation-budget plateau** — the substrate-level mechanism by which redundancy-engagement of UR-1.3 produces a plateau in error-suppression rate. The paper:

1. Defines Class-C platforms via dominant engagement of lever C (Paper_054 §6).
2. Derives the substrate-level mechanism: redundancy → multi-channel substrate-level coverage → V5 cross-chain correlation budget saturation → error-suppression plateau.
3. Distinguishes Class-C failure mode from Class-A (UR-1.1, multiplicity-cap) and Class-B (UR-1.2, cross-bandwidth gap).
4. Specifies the substrate-level scaling form and inherited coefficients.

Class-C completes the pure-class triple. Together with Papers_056 (Class-A wall) and 057 (Class-B exponential gap-suppression), this paper closes the Q-COMPUTE structural-architectural taxonomy.

### 1.2 Why a plateau, not exponential decay

Standard fault-tolerant quantum computing predicts **exponential** error-suppression with increasing redundancy (concatenated codes give doubly-exponential suppression). The substrate-level Class-C mechanism differs structurally: it predicts a **plateau** rather than continued exponential decay.

**Reason:** substrate-level cross-chain correlation budget is finite (P-Corr-Budget postulate). Adding redundant substrate-channels increases coverage up to the substrate's correlation budget; beyond saturation, additional channels cannot further suppress UR-1.3 failure because no new substrate-level correlation slots are available.

**Empirical signature:** Class-C platforms should exhibit error-suppression that initially decreases with redundancy parameter (similar to standard fault-tolerant scaling) and then plateaus at high redundancy. The plateau onset is the substrate-level wedge claim.

### 1.3 Arc context

- **Paper_054 (UR-1):** Three jointly-required components.
- **Paper_056 (Class-A):** Multiplicity wall (UR-1.1 lever).
- **Paper_057 (Class-B):** Exponential gap-suppression (UR-1.2 lever).
- **Paper_058 (this paper, Class-C):** Correlation-budget plateau (UR-1.3 lever).

The Q-COMPUTE pure-class triple is closed with this paper.

---

## 2. Primitive Inputs

**Substrate primitives (postulated, Paper_087):** P02, P04, P05, P07, P09, P10, P11, P12 — same load-bearing set as Paper_054 + Paper_056 + Paper_057.

**V1 inheritance (Paper_089):** finite-width retarded kernel.

**V5 dependence (Paper_090):** cross-chain correlation kernel; supplies substrate-level correlation budget.

**Upstream paper dependencies:**

- **Paper_087:** position paper.
- **Paper_054:** UR-1; three jointly-required components; dominant-lever framing.
- **Paper_056 + 057:** sibling architectural classes; complete pure-class triple with this paper.
- **Paper_089, 090:** V1, V5.

**Paper-specific postulates (added per QC discipline):**

- **P-Corr-Budget (Substrate-level cross-chain correlation budget is finite):** *V5 cross-chain correlation content at a substrate-graph locus carries a substrate-level **correlation budget** $B_{\mathrm{cross}}(u, t)$ bounded above by $B_{\mathrm{cross,max}}$ — a substrate-level scale inherited from V5 envelope structure.* This postulate makes redundancy saturation possible: once redundant substrate-channels exhaust the correlation budget, no additional cross-chain content can be maintained. P-Corr-Budget is not derivable from P04 alone (P04 fixes bandwidth as non-negative additive scalar but does not bound cross-chain correlation budget); it is a substrate-level commitment specific to V5 cross-chain content.
- **P-Redundancy-Mapping (Substrate-level redundancy parameter maps to channel coverage):** *The Class-C redundancy parameter $R_C$ (number of redundant substrate-channels carrying the protected state) maps linearly to substrate-level cross-chain coverage in the unsaturated regime.* Substrate-level commitment; the **mapping form (linear)** is a regime assumption — alternative substrate-consistent forms (logarithmic, square-root) would give modified scaling.

**Empirical / value-layer inputs:**

- Substrate-level scales $B_{\mathrm{cross,max}}$, $R_C^{\mathrm{sat}}$, $\Gamma_{\mathrm{plateau}}$: inherited from V5 envelope shape + platform-specific redundancy design.

---

## 2.5 Load-Bearing Step Audit

| Step | Status | Justification |
|---|---|---|
| 13 primitives postulated | P | Paper_087 |
| UR-1 with three components | D | Paper_054 |
| Class-C = dominant-lever-C engagement | D | Paper_054 §6 |
| V5 supplies cross-chain correlation content | D | Paper_090 |
| Substrate-level cross-chain correlation budget exists, bounded above | **P (P-Corr-Budget)** | §2 postulate; not derivable from P04 (which bounds bandwidth, not correlation budget). Substrate-level commitment specific to V5 structure. |
| Redundancy parameter $R_C$ maps linearly to coverage in unsaturated regime | **P (P-Redundancy-Mapping) / A→regime** | §2 substrate-level mapping; linear form is a regime assumption. |
| Error-suppression rate decreases initially with $R_C$ in unsaturated regime | D | §3.2 algebra from coverage increasing in unsaturated regime |
| Plateau onset at $R_C \to R_C^{\mathrm{sat}}$ | **D conditional on P-Corr-Budget** | §3.3 explicit algebra: $B_{\mathrm{cross}} \to B_{\mathrm{cross,max}}$ saturates per P-Corr-Budget; substrate-level error-suppression rate inherits the saturation form |
| Plateau form ($\Gamma \to \Gamma_{\mathrm{plateau}}$, not $\to 0$) | **D conditional on P-Corr-Budget** | §3.4 — finite correlation budget (P-Corr-Budget bounded above) forces non-zero plateau; conditional on P-Corr-Budget's "bounded-above-but-not-zero" content |
| Class-C distinct from Class-A failure mode (UR-1.1) | **D conditional on Paper_054 UR-1 independence (A→inheritance)** | §4.1 from UR-1.1 vs UR-1.3 distinctness — this distinctness depends on Paper_054 §3.5's A→assertion that the three rate quantities have distinct primary drivers (not formal independence). *(Round-5 QC: the Class-A/B/C three-way distinctness inherits Paper_054's UR-1 independence assumption.)* |
| Class-C distinct from Class-B failure mode (UR-1.2) | **D conditional on Paper_054 UR-1 independence (A→inheritance)** | §4.2 from UR-1.2 vs UR-1.3 distinctness — same inheritance as above |
| Substrate-level coefficients $B_{\mathrm{cross,max}}, R_C^{\mathrm{sat}}, \Gamma_{\mathrm{plateau}}$ | I | V5 envelope shape + platform-specific redundancy budget; empirical inheritance |
| Specific error-correction codes (Shor, surface, etc.) | I | Empirical / platform design |

All rows P, D, I, or labeled. **No A (asserted) rows. No banned-phrase patterns ("plays the role of," "Boltzmann-like" etc.).**

---

## 3. Substrate-Level Mechanism

### 3.1 The redundancy engagement of UR-1.3

By Paper_054 §5.3, UR-1.3 requires substrate-level commitment-injection rate $\Gamma_{\mathrm{commit}}$ to remain below the inverse individuation timescale: $\Gamma_{\mathrm{commit}}(t) < \Gamma_{\mathrm{individuation}}^{-1}$.

Class-C engineering lever C (Paper_054 §6.1): suppress single-channel $\Gamma_{\mathrm{commit}}$ via **redundancy** — the protected quantum state is encoded across multiple substrate-channels (the substrate-level analog of a logical qubit encoded across multiple physical qubits in standard fault-tolerant QC).

**Substrate-level mechanism:** redundant substrate-channels carrying the protected state effectively distribute the substrate-level commitment-injection content across more channels. The substrate-level **rate of single-channel commitment-injection on any specific channel** decreases as redundancy grows — provided substrate-level cross-chain correlation can be maintained across the redundant channels (V5 budget).

### 3.2 Error-suppression in the unsaturated regime

In the **unsaturated regime** ($R_C \ll R_C^{\mathrm{sat}}$), substrate-level correlation budget $B_{\mathrm{cross}}$ is well below saturation. By P-Redundancy-Mapping, the redundancy parameter $R_C$ maps linearly to substrate-level cross-chain coverage:

$$
B_{\mathrm{cross}}(R_C) \approx \alpha\,R_C \quad \text{(unsaturated regime)}
$$

with $\alpha$ a substrate-level mapping coefficient inherited from V5 envelope structure.

The substrate-level error-suppression rate for UR-1.3 failure scales inversely with cross-chain coverage:

$$
\Gamma_{\mathrm{UR\text{-}1.3,fail}}^{\mathrm{Class\text{-}C}}(R_C) \approx \frac{\Gamma_0^{\mathrm{Class\text{-}C}}}{R_C}\quad \text{(unsaturated regime)}.
$$

**Dimensional check:** $\Gamma$ has $[1/\mathrm{time}]$; $\Gamma_0^{\mathrm{Class\text{-}C}}$ has $[1/\mathrm{time}]$; $R_C$ is dimensionless (count of redundant channels). ✓

In this regime, error suppression decreases monotonically with redundancy — similar to early stages of standard fault-tolerant scaling.

### 3.3 Plateau onset at correlation-budget saturation

As $R_C$ increases toward $R_C^{\mathrm{sat}}$, substrate-level cross-chain correlation budget approaches saturation:

$$
B_{\mathrm{cross}}(R_C) \to B_{\mathrm{cross,max}}\quad \text{as } R_C \to R_C^{\mathrm{sat}}.
$$

By P-Corr-Budget (§2), the substrate-level correlation budget is bounded above. Once $B_{\mathrm{cross}}$ saturates, the substrate cannot maintain additional cross-chain correlation across further redundant channels. The substrate-level mechanism: at saturation, additional redundant substrate-channels carry the protected state nominally but **cannot be coherently correlated** with the existing substrate-channel set.

The substrate-level error-suppression rate plateaus:

$$
\boxed{\Gamma_{\mathrm{UR\text{-}1.3,fail}}^{\mathrm{Class\text{-}C}}(R_C) \to \Gamma_{\mathrm{plateau}}\quad \text{as } R_C \to R_C^{\mathrm{sat}}.}
$$

The plateau value $\Gamma_{\mathrm{plateau}}$ is inherited from substrate-level cross-chain correlation budget: $\Gamma_{\mathrm{plateau}} \sim \Gamma_0^{\mathrm{Class\text{-}C}}/R_C^{\mathrm{sat}}$ — the suppression at which the substrate first saturates.

### 3.4 Why the plateau is not zero — finite correlation budget

**The plateau is at a non-zero rate** $\Gamma_{\mathrm{plateau}} > 0$, not at $\Gamma \to 0$ asymptote. The substrate-level reason: P-Corr-Budget bounds correlation **above**; it does not bound suppression to zero. At saturation, the substrate has exhausted its capacity to add cross-chain coverage; any residual UR-1.3 failure rate at saturation persists.

**Comparison to standard fault-tolerance scaling.** Standard fault-tolerant QC predicts exponential error suppression with redundancy (concatenated codes) or polynomial suppression (surface codes) — both monotonically approaching zero asymptotically. **Class-C plateau differs structurally**: error suppression saturates at finite $\Gamma_{\mathrm{plateau}}$, not at zero.

This is the substrate-level wedge claim distinguishing Class-C from standard fault-tolerant scaling. **Empirical test:** plot error rate vs. redundancy parameter for fault-tolerant quantum-computing platforms; check whether suppression continues to decrease (standard fault-tolerance) or plateaus at high redundancy (Class-C).

---

## 4. Distinction from Class-A and Class-B Failure Modes

**Inheritance note (round-5 QC):** the Class-A/B/C three-way structural distinctness inherits **Paper_054's UR-1 independence assumption** (Paper_054 §3.5, labeled A→assertion: the three rate quantities $\Gamma_{\mathrm{commit}}(M_{\mathrm{eff}})$, $\Gamma_{\mathrm{cross}}$, $\Gamma_{\mathrm{individuation}}^{-1}$ have **distinct primary drivers** in substrate primitives, but formal mathematical independence is not proven). The Class-A/B/C distinctness developed below is therefore **conditional on Paper_054's distinct-primary-drivers framing**, not on a stronger mathematical-independence claim. If Paper_054's independence assumption is weakened or refuted, the Class-A/B/C distinctness becomes correspondingly weaker.

### 4.1 Class-C distinct from Class-A (UR-1.1)

- **Class-A (UR-1.1):** $M_{\mathrm{eff}}$ exceeds $M_{\mathrm{cap}}$; substrate-level commitment-injection rate grows with multiplicity. **Mass-limited** wall.
- **Class-C (UR-1.3):** $\Gamma_{\mathrm{commit}}$ exceeds $\Gamma_{\mathrm{individuation}}^{-1}$ at fixed multiplicity due to single-channel commitment-injection acceleration. **Correlation-budget-limited** plateau.

The two are structurally distinct failure modes (Paper_054 §4): Class-A is driven by **multiplicity growth**; Class-C is driven by **single-channel commitment-injection** that redundancy attempts to suppress.

### 4.2 Class-C distinct from Class-B (UR-1.2)

- **Class-B (UR-1.2):** $\Gamma_{\mathrm{cross}}$ drops below $\Gamma_{\mathrm{decoupling}}$; V5 envelope decays at chain configuration. **Rigidity-limited** exponential suppression.
- **Class-C (UR-1.3):** redundancy distributes commitment-injection across multiple channels; correlation budget saturates. **Correlation-budget-limited** plateau.

The two are structurally distinct (Paper_054 §4): Class-B engages V5 envelope structural integrity (gapped regime); Class-C engages V5 correlation budget capacity (saturation regime). Both involve V5, but at different aspects of V5 structure.

### 4.3 Hybrid architectures

A platform engaging both lever B (rigidity) and lever C (redundancy) — e.g., a surface code with topological protection — is **hybrid Class-B + Class-C**. The substrate-level error-suppression curve exhibits exponential suppression in the gap-protected regime (Class-B) overlaid with plateau onset at correlation-budget saturation (Class-C). The dominant-lever framing (Paper_054 §6) classifies such platforms by primary engagement; hybrid platforms have intermediate behavior with composite scaling.

---

## 5. Empirical Wedge

### 5.1 Plateau-vs-exponential test

The substrate-level Class-C prediction differs structurally from standard fault-tolerant scaling at high redundancy:

- **Standard fault-tolerance:** monotonic exponential or polynomial suppression as $R_C$ grows; asymptotic $\Gamma \to 0$.
- **Class-C (this paper):** plateau onset at $R_C \to R_C^{\mathrm{sat}}$; asymptotic $\Gamma \to \Gamma_{\mathrm{plateau}} > 0$.

**Empirical test:** for surface-code or concatenated-code quantum-computing platforms, measure logical error rate as function of code distance / concatenation level. Standard prediction: continued exponential decrease. Class-C prediction: plateau at sufficiently high redundancy. The plateau onset is empirically distinguishable.

### 5.2 Cross-platform consistency

Different Class-C platforms (surface codes, concatenated codes, color codes, novel error-correction schemes) should exhibit plateau onset at consistent substrate-level $B_{\mathrm{cross,max}}$ — after platform-specific scaling. This is the substrate-level cross-platform unification claim, analogous to Paper_056 §6.4 (Class-A) and Paper_057 §6.2 (Class-B).

**Honesty caveat:** cross-platform unification carries retroactive-fit risk; substrate-derived $B_{\mathrm{cross,max}}$ matching independently across platforms requires Strategy-1 commitments (in-queue work). The current operational stance is **structural-form prediction** (plateau exists, not exponential-to-zero) + acknowledged retroactive-fit risk on numerical $B_{\mathrm{cross,max}}$ matching.

### 5.3 Plateau-onset detection

The plateau onset is observationally detectable as a **curvature change** in error-rate-vs-redundancy plots:

- Unsaturated regime: log-error vs. $R_C$ approximately linear (exponential scaling).
- Plateau regime: log-error vs. $R_C$ flattens.

Current fault-tolerant QC platforms are still in the unsaturated regime (code distances up to ~$d = 30$ in surface codes, well below substrate-level saturation as currently estimated). **Plateau detection is a near-term experimental signature** as code distances grow.

---

## 6. Falsification Criteria

### 6.1 Continued exponential suppression at very high redundancy

**Falsifier sentence:** *Empirical observation that pure-Class-C platforms (no Class-A or Class-B admixture) exhibit continued exponential or polynomial error-suppression at arbitrarily high redundancy — with no plateau onset — would falsify §3's correlation-budget saturation mechanism.*

This is the sharp substrate-level test. Current quantum-computing platforms have not yet reached saturation regimes; future high-distance experiments are the falsifier.

### 6.2 Plateau at zero asymptote

**Falsifier sentence:** *Empirical observation of plateau onset but at $\Gamma_{\mathrm{plateau}} = 0$ (rather than $> 0$) would falsify P-Corr-Budget's "bounded above, not zero" structure.*

### 6.3 Cross-platform $B_{\mathrm{cross,max}}$ inconsistency

**Falsifier sentence:** *Empirical demonstration that different Class-C platforms have substantially different effective $B_{\mathrm{cross,max}}$ (after appropriate platform-specific scaling) would falsify the §5.2 cross-platform unification claim.*

### 6.4 Non-linear $R_C$ → coverage mapping observed

**Falsifier sentence:** *Empirical observation that the redundancy-to-coverage mapping is significantly non-linear in the unsaturated regime (e.g., logarithmic, square-root) would falsify P-Redundancy-Mapping's linear-form regime assumption.*

### 6.5 No distinction from standard fault-tolerance at any redundancy

**Falsifier sentence:** *Empirical demonstration that Class-C platforms exactly match standard fault-tolerant scaling at all redundancy levels would render the Class-C plateau prediction empirically indistinguishable from standard fault-tolerance, weakening (but not falsifying) the substrate-level wedge.*

### 6.6 Class-C platforms hit Class-A or Class-B walls

**Falsifier sentence:** *Empirical observation that pure-Class-C platforms hit a UR-1.1 multiplicity-cap wall or a UR-1.2 rigidity-breaking transition (rather than UR-1.3 plateau) would falsify §4's failure-mode distinctness claim and re-map Class-C to a different architectural lever.*

---

## 7. Position Statement

**Class-C correlation-budget plateau** is a downstream structural identification in the ED Generative Primitives System. Given the postulated primitives + UR-1 (Paper_054) + V1/V5 + dominant-lever framing + P-Corr-Budget + P-Redundancy-Mapping, Class-C platforms (engaging engineering lever C — redundancy to prevent UR-1.3 failure) exhibit:

$$
\Gamma_{\mathrm{UR\text{-}1.3,fail}}^{\mathrm{Class\text{-}C}}(R_C) \approx \frac{\Gamma_0^{\mathrm{Class\text{-}C}}}{R_C}\;(R_C \ll R_C^{\mathrm{sat}}), \qquad \to \Gamma_{\mathrm{plateau}}\;(R_C \to R_C^{\mathrm{sat}}).
$$

The plateau form arises from substrate-level cross-chain correlation budget saturation (P-Corr-Budget). Class-C failure mode is structurally distinct from Class-A (multiplicity-cap, UR-1.1) and Class-B (rigidity-gap, UR-1.2).

What this paper claims:

- Class-C platforms exhibit a substrate-level error-suppression plateau (not continued exponential decay) at sufficiently high redundancy.
- The plateau form is conditional on P-Corr-Budget + P-Redundancy-Mapping postulates.
- Class-C failure mode is structurally distinct from Class-A and Class-B.
- The substrate-level wedge: plateau-vs-exponential is empirically distinguishable at high code distances.

What this paper does *not* claim:

- The 13 primitives are not derived (Paper_087).
- UR-1 is not re-derived (Paper_054).
- Plateau coefficients ($B_{\mathrm{cross,max}}$, $R_C^{\mathrm{sat}}$, $\Gamma_{\mathrm{plateau}}$) are value-layer inherited.
- Specific error-correction codes are not derived; platform design inherited.
- Class-C does not replace standard fault-tolerance theorems; it supplies substrate-level mechanism for UR-1.3 redundancy engagement.
- Dominant-lever framing is not strict bijection; hybrid platforms exhibit composite scaling.

**Series context.** Paper_058 of the Q-COMPUTE arc. **Completes the pure-class triple** with Paper_056 (Class-A) + Paper_057 (Class-B). Q-COMPUTE arc now has its four foundational papers (054 UR-1, 056/057/058 architectural triple).

---

## Appendix: Cross-References and Glossary

### Cross-references

- **Paper_087:** position paper.
- **Paper_054 (UR-1):** three components; dominant-lever framing.
- **Paper_056 (Class-A wall):** sibling.
- **Paper_057 (Class-B exponential gap-suppression):** sibling.
- **Paper_089, 090:** V1, V5.

### Glossary

- **Class-C platform.** Coherent platform dominantly engaging engineering lever C (high-multiplicity redundancy / error correction).
- **Engineering lever C.** Suppress single-channel $\Gamma_{\mathrm{commit}}$ via redundancy → prevent UR-1.3 failure.
- **Redundancy parameter $R_C$.** Platform-specific: number of redundant substrate-channels carrying protected state.
- **Substrate-level cross-chain correlation budget $B_{\mathrm{cross}}$.** V5-mediated substrate correlation content carried at chain locus; bounded above by $B_{\mathrm{cross,max}}$ (P-Corr-Budget).
- **Correlation-budget saturation $R_C^{\mathrm{sat}}$.** Redundancy parameter at which $B_{\mathrm{cross}} \to B_{\mathrm{cross,max}}$.
- **Plateau rate $\Gamma_{\mathrm{plateau}}$.** Asymptotic error-suppression rate at $R_C \to R_C^{\mathrm{sat}}$; $> 0$, not zero.
- **P-Corr-Budget.** Substrate-level cross-chain correlation budget is finite (bounded above).
- **P-Redundancy-Mapping.** Linear mapping $R_C$ → coverage in unsaturated regime (regime assumption).

---

**End of Paper_058.**

*Wave-2 Generative Paper — Q-COMPUTE Arc. Completes pure-class triple. Plateau form distinguishes Class-C from Class-A (mass-limited wall) and Class-B (rigidity-limited exponential suppression).*
