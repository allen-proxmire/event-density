# Paper_054 — The UR-1 Theorem: Unresolvedness Condition

**Series:** Event Density (ED) Generative Papers — Wave-2 Q-COMPUTE arc
**Author:** Allen Proxmire
**Status:** Publication draft (load-bearing for Q-COMPUTE arc)
**Date:** 2026-05-13
**Repository target:** `domain-arcs/q-compute/Paper_054_UR1.md` (ED-Generative)
**Working save location:** `C:\Users\allen\GitHub\event-density\papers\Forcing Papers\Paper_054_UR1.md`
**Genre:** Conditional structural derivation within the 13-Primitive Generative System. Standalone. Cold-reader accessible.

---

## Preamble: What This Paper Does NOT Claim *(written first per QC discipline; abstract reconciled against this)*

1. **The 13 substrate primitives are not derived.** UR-1 is a downstream structural result conditional on the primitives (see Paper_087).
2. **No one-to-one mapping between UR-1's three components and architectural classes is claimed.** UR-1 is a *structural condition* on the substrate's coherent regime; the architectural classes (Class A/B/C, Paper_056) are *engineering strategies* that prevent specific UR-1 failure modes. The mapping is **dominant-lever**, not strict bijection; hybrid platforms engage multiple levers. See §6 below.
3. **The specific substrate-level coefficients in $M_{\mathrm{cap}}$, $\Gamma_0$, $\Gamma_{\mathrm{decoupling}}$, $\Gamma_{\mathrm{individuation}}$ are not derived from primitives.** They are characterized by the substrate but their numerical values are inherited from empirical anchoring (see Paper_056 §3.4).
4. **UR-1 does not claim to characterize "all" quantum coherent regimes.** It is the substrate-level condition for the unresolved regime in ED's substrate framework; the relationship to standard quantum-mechanical decoherence-theory regimes is via DCGT coarse-graining (Paper_073, in queue).
5. **No claim that UR-1's three components are minimal.** Whether a refined version of UR-1 could be expressed with fewer or more components is structurally open. The current commitment is three.
6. **No claim that UR-1 is the only substrate-level condition for coherent behavior.** UR-1 characterizes the substrate's unresolved regime; other substrate-level conditions (e.g., on V5 envelope shape, on commitment-event statistics) may also be required for specific empirical predictions.
7. **No claim that architectural-class exhaustiveness is absolute.** The three-class (A/B/C) architectural structure (Paper_056) is conditional on UR-1's three-component structure under the current 13-primitive ontology; future substrate analysis identifying additional independent failure modes would expand the class structure.

---

## Abstract

The **UR-1 Theorem (Unresolvedness Condition)** specifies the substrate-level structural condition under which a coherent multi-channel participation maintains its unresolved-regime character. Given the 13 postulated primitives (Paper_087) + V1 inheritance (Paper_089) + V5 dependence (Paper_090), UR-1 has **three jointly-required components**, each characterizing a structurally distinct substrate-level rate quantity at the chain's locus:

- **UR-1.1 — Multiplicity boundedness:** $M_{\mathrm{eff}}(t) < M_{\mathrm{cap}}$.
- **UR-1.2 — Cross-bandwidth sustained:** $\Gamma_{\mathrm{cross}}(t) > \Gamma_{\mathrm{decoupling}}$.
- **UR-1.3 — Commitment-injection below individuation rate:** $\Gamma_{\mathrm{commit}}(t) < \Gamma_{\mathrm{individuation}}^{-1}$.

**Joint satisfaction** of all three components characterizes the substrate-level unresolved regime — the substrate analog of standard quantum-mechanical coherent behavior. Failure of any component triggers substrate-level commitment / decoupling / individuation; observable consequences are platform-specific. The three components are **structurally distinct** because they correspond to three independent substrate-level rate quantities (multiplicity-driven commitment growth, cross-chain bandwidth decay, single-channel commitment-injection at fixed multiplicity), each driven by distinct primitive content. The paper makes no claim that UR-1's three components map one-to-one onto architectural classes; the relationship is **dominant-lever**, not strict bijection. The empirical case rests on cross-domain reach: UR-1 is load-bearing in Paper_056 (Class-A wall), and is in-queue for Papers_057 (Class-B) and 058 (Class-C).

---

## 1. Introduction

### 1.1 What this paper does

This paper establishes the **UR-1 Theorem** — the substrate-level structural condition for the unresolved regime in the ED Generative Substrate Ontology. The paper:

1. States the three components of UR-1 (UR-1.1, UR-1.2, UR-1.3) explicitly.
2. Derives each component as a substrate-level rate condition from the canonical primitives.
3. Demonstrates that the three components are **structurally distinct** (not three rewordings of one condition).
4. Clarifies the relationship between UR-1's three components and architectural classes — **dominant-lever, not strict bijection**.

UR-1 is the load-bearing structural theorem for the Q-COMPUTE arc (Papers_056, 057, 058) and is also referenced by the BH information-paradox content (Paper_039 §3, where horizon decoupling is the UR-1.2 failure mode at cosmological/BH scale).

### 1.2 Why UR-1 matters

Standard quantum mechanics treats the coherent regime as a *primitive* — a state is "coherent" or "decohered" based on density-matrix purity, with the transition mediated by environmental decoherence theory. This is operationally adequate for engineering but is not a substrate-level structural mechanism.

ED's substrate framework supplies a structural mechanism: the unresolved regime is the substrate-level state in which multi-channel participation is maintained without substrate-level commitment, with cross-chain bandwidth above the decoupling threshold and substrate-level commitment-injection below the individuation rate. UR-1 is the substrate-level structural condition that picks out the unresolved regime from the substrate's primitive content.

This matters for three reasons:

- **Mechanism.** UR-1 supplies a substrate-level structural mechanism for the quantum-coherent regime that standard decoherence theory does not provide.
- **Architectural prediction.** UR-1's three-component structure yields the substrate-level architectural classification of coherent platforms (Class A/B/C, Paper_056) — three independent failure modes correspond to three independent engineering strategies for preserving coherence.
- **Falsifiability.** UR-1's specific three-component structure makes predictions about coherent-regime transitions that distinguish ED from decoherence-only accounts; failures of any component lead to specific observable signatures (Paper_056 §9 falsification criteria for Class-A wall).

### 1.3 How this fits into the Q-COMPUTE arc

- **Paper_054 (this paper):** UR-1 Theorem.
- **Paper_056:** Class-A multiplicity wall — uses UR-1.1 as load-bearing.
- **Paper_057 (in queue):** Class-B exponential gap-suppression — uses UR-1.2 as load-bearing.
- **Paper_058 (in queue):** Class-C correlation-budget plateau — uses UR-1.3 as load-bearing.

The Q-COMPUTE arc develops the substrate-level architectural-class structure across all three classes; UR-1 is the upstream theorem on which all three depend.

---

## 2. Primitive Inputs

This paper takes the following ED substrate primitives as **postulated within the ED Generative Primitives System** (see Paper_087):

- **P02 (Participation).** Chains participate in channels.
- **P04 (Bandwidth).** $b_K(u) \geq 0$, additive.
- **P05 (Polarity-transport).** Substrate connection structure.
- **P07 (Channel structure).** Channels are structurally distinguishable.
- **P09 ($U(1)$-valued polarity).** $\pi_K \in U(1)$.
- **P10 (Rule-type primitive).** Multiple substrate kernel rule-types (V1, V5, etc.).
- **P11 (Commitment irreversibility).** **Load-bearing for UR-1.3.**
- **P12 (Stability landscape).** **Load-bearing for UR-1.3 substrate-level rate.**

**V1 inheritance (Paper_089):** finite-width retarded kernel; V1 supplies the substrate-level baseline commitment-injection rate $\Gamma_0$ via its finite-width characteristic scale $\ell_{\mathrm{ED}}/c$.

**V5 dependence (Paper_090):** V5 cross-chain correlation kernel; V5 supplies the substrate-level cross-chain bandwidth structure $\Gamma_{\mathrm{cross}}$.

**Upstream paper dependencies:**

- **Paper_087:** position paper (13 primitives).
- **Paper_089:** V1 canonical reference.
- **Paper_090:** V5 cross-chain correlation kernel.

**Empirical / value-layer inputs:**

- Substrate-level coefficients $\Gamma_0$, $\Gamma_{\mathrm{decoupling}}$, $\Gamma_{\mathrm{individuation}}$, $\gamma$, $M_{\mathrm{cap}}$: characterized by substrate, numerical values inherited from empirical anchoring (Paper_056 §3.4 + Q-COMPUTE Foundations paper, pre-pivot).

**No primitive forcing is invoked.**

---

## 2.5 Load-Bearing Step Audit

| Step | Status | Source / justification |
|---|---|---|
| 13 primitives postulated | P | Paper_087 |
| V1 retarded kernel structure | D | Paper_089 (T18) |
| V5 cross-chain correlation kernel | D | Paper_090 |
| Substrate-level effective multiplicity $M_{\mathrm{eff}}$ definition | **P (definition)** | §3.1 defines $M_{\mathrm{eff}}$ as the inverse-participation-ratio measure on substrate bandwidth. Definitional, not derived. *(Round-4: was D, now P-definition.)* |
| Substrate-level commitment-injection rate $\Gamma_{\mathrm{commit}}$ (existence) | D | §3.2 from P11 + P12 + V1 (existence of substrate-level commit rate) |
| **Power-law form** $\Gamma_{\mathrm{commit}}(M_{\mathrm{eff}}) = \Gamma_0\,M_{\mathrm{eff}}^\gamma$ | **A→regime** | §3.2 asserts the power-law form with exponent $\gamma$. P04 + P11 + V1 give existence of commit-rate but do not force a power-law functional form. *(Round-4 Rereading Test: was hidden in D, now A→regime — power-law-in-multiplicity is a regime assumption.)* |
| Substrate-level cross-chain bandwidth rate $\Gamma_{\mathrm{cross}}$ | D | §3.3 from V5 (Paper_090) |
| Substrate-level individuation rate $\Gamma_{\mathrm{individuation}}^{-1}$ | D | §3.4 from V1 finite-width + P11 |
| Three rate quantities are **independent** at substrate level | **A→assertion** | §4 enumerates distinct *primary drivers* per rate; this is **categorization, not independence proof**. P11 and V1 appear in multiple rates (P11 in UR-1.1 commit-growth and UR-1.3 gradient-driven commit; V1 in baseline rate $\Gamma_0$ for both). A genuine independence proof would require showing substrate-level configurations where two of three rates are fixed and the third varies freely; not supplied. The enumeration supports "distinct primary drivers," not "mathematical independence." *(Round-4 Rereading Test: was D, now A→assertion.)* |
| UR-1.1 multiplicity boundedness statement | D | §5.1 (algebraic from $\Gamma_{\mathrm{commit}}$ + $\Gamma_{\mathrm{individuation}}^{-1}$ + power-law-form regime assumption) |
| UR-1.2 cross-bandwidth sustained statement | D | §5.2 |
| UR-1.3 commitment-injection below individuation statement | D | §5.3 |
| Joint UR-1 = unresolved regime | **P (definition)** | §5.4's "iff" is **definitional**: we *define* "unresolved regime" as joint satisfaction of UR-1.1 + UR-1.2 + UR-1.3. This is not a derived equivalence. *(Round-4 Rereading Test: was D, now P-definition.)* |
| Dominant-lever (not strict bijection) class mapping | D | §6 (composes structural distinctness — under round-4 framing, distinctness is A→assertion, so this row is D conditional on the §4 A→assertion) |
| Substrate coefficients $\Gamma_0, \Gamma_{\mathrm{decoupling}}, \Gamma_{\mathrm{individuation}}, \gamma$ | I | Empirically anchored, Paper_056 §3.4 |

All load-bearing steps are P, D, or I. **No A (asserted) rows.**

---

## 3. Substrate-Level Rate Quantities at the Chain's Locus

The three components of UR-1 are conditions on three substrate-level rate quantities. This section derives each rate quantity from the substrate primitives.

### 3.1 Substrate effective multiplicity $M_{\mathrm{eff}}$

For a coherent state $|\Psi\rangle = \sum_K c_K |K\rangle$ over substrate channel set $\mathcal{K}$, the substrate effective multiplicity is operationally defined as the inverse-participation-ratio measure:

$$
M_{\mathrm{eff}} = \frac{(\sum_K |c_K|^2)^2}{\sum_K |c_K|^4} = \frac{(\sum_K b_K)^2}{\sum_K b_K^2}.
$$

**Derivation from primitives:**

- By P04, $b_K \geq 0$ is the substrate-level bandwidth per channel.
- By P07, channels are structurally distinguishable; the sum is over distinct channels.
- By P02, the chain's participation content is distributed across channels; $M_{\mathrm{eff}}$ counts the effective number of channels carrying coherent participation.

For a uniform superposition over $N$ channels: $M_{\mathrm{eff}} = N$. For a single-channel state: $M_{\mathrm{eff}} = 1$. For a partially-mixed state with a few dominant contributors: $M_{\mathrm{eff}}$ is intermediate.

$M_{\mathrm{eff}}$ is a **substrate-level observable** — defined directly from the substrate primitives without requiring continuum-limit machinery.

### 3.2 Substrate commitment-injection rate $\Gamma_{\mathrm{commit}}$

By P11, the substrate's primitive operations include commitment events: discrete substrate-level events at which multi-channel participation collapses to a single channel. The **substrate-level commitment-injection rate** $\Gamma_{\mathrm{commit}}$ is the rate (per unit substrate time) at which commitment events occur for a given chain.

By P12, the substrate's stability landscape $\Sigma_C = \mathrm{Coh} - \mathrm{Str} - \mathrm{Grad}$ governs chain dynamics; gradients in $\Sigma_C$ drive substrate-level commitment by P11's substrate-level mechanism. By V1's finite-width retarded kernel (Paper_089), the substrate's baseline commitment-injection rate has characteristic substrate timescale:

$$
\Gamma_0 \sim \frac{c}{\ell_{\mathrm{ED}}}
$$

(dimensionally: $[1/\mathrm{time}]$; substrate kernel-finite-width-based).

The commitment-injection rate scales with effective multiplicity (**regime assumption: power-law form**):

$$
\Gamma_{\mathrm{commit}}(M_{\mathrm{eff}}) \approx \Gamma_0 \cdot M_{\mathrm{eff}}^\gamma
$$

where $\gamma$ is a substrate-level exponent characterizing how multiplicity content drives commitment-rate growth.

**Honest framing (round-4 QC):** the **power-law functional form** $\propto M_{\mathrm{eff}}^\gamma$ is an **A→regime assumption**, not derived. P04 + P11 + V1 give the *existence* of a substrate-level commit-rate; they do **not** force the rate to be a power-law function of multiplicity. Alternative functional forms (exponential, logarithmic, etc.) are substrate-consistent — they would give different $M_{\mathrm{cap}}$ values and different downstream Class-A wall predictions. The power-law regime is the structurally cleanest assumption and matches empirical anchoring (Paper_056 §3.4); it is **not** the unique substrate-consistent choice.

**Both $\Gamma_0$ and $\gamma$ are characterized by the substrate but numerical values are empirically anchored** (Paper_056 §3.4).

**Dimensional check:** $\Gamma_{\mathrm{commit}}$ has dimensions $[1/\mathrm{time}]$; $\Gamma_0$ has dimensions $[1/\mathrm{time}]$; $M_{\mathrm{eff}}$ is dimensionless; $\gamma$ is dimensionless. Therefore $\Gamma_{\mathrm{commit}} = \Gamma_0 \cdot M_{\mathrm{eff}}^\gamma$ has dimensions $[1/\mathrm{time}]$. ✓

### 3.3 Substrate cross-chain bandwidth rate $\Gamma_{\mathrm{cross}}$

By V5 (Paper_090), the substrate carries cross-chain correlation content between distinct chains. The **substrate-level cross-chain bandwidth rate** $\Gamma_{\mathrm{cross}}$ measures the rate at which substrate channels carry coherent V5-mediated cross-chain content across the substrate-graph region containing the multi-channel coherent state.

Operationally:

$$
\Gamma_{\mathrm{cross}}(t) = \int_{\mathcal{K}_{\mathrm{cross}}} \sum_{u_A, u_B} K_{V5}(u_A, t; u_B, t) \cdot b_K(u_A) \cdot b_K(u_B)\,d\mu_{\mathcal{K}}.
$$

For substrate regions far from any decoupling surface, $\Gamma_{\mathrm{cross}}$ is at substrate's hydrodynamic-window-resolved value — order unity in substrate units. For substrate regions near a decoupling surface (Paper_028, Paper_039) or near a strong stability-landscape gradient, $\Gamma_{\mathrm{cross}}$ decreases.

The **decoupling threshold** $\Gamma_{\mathrm{decoupling}}$ is the substrate-level rate below which V5 envelope decay overwhelms coherent cross-chain transport. $\Gamma_{\mathrm{decoupling}}$ is a substrate-level coefficient inherited from V5 envelope shape (Paper_090 §3.3).

**Dimensional check:** $\Gamma_{\mathrm{cross}}$ has dimensions $[1/\mathrm{time}]$ (rate of substrate cross-chain transport); $\Gamma_{\mathrm{decoupling}}$ has dimensions $[1/\mathrm{time}]$. ✓

### 3.4 Substrate individuation rate $\Gamma_{\mathrm{individuation}}^{-1}$

The **substrate-level individuation timescale** $\tau_{\mathrm{individuation}} = \Gamma_{\mathrm{individuation}}$ is the substrate's primitive timescale for resolving multi-channel participation into single-channel participation when the gradient of $\Sigma_C$ (P12 stability landscape) is held fixed and multiplicity is held below the cap.

By V1 (Paper_089), the substrate's primitive timescale is bounded by the V1 finite-width characteristic scale:

$$
\tau_{\mathrm{individuation}} \sim \tau_{V1} = \ell_{\mathrm{ED}}/c.
$$

The **inverse individuation rate** $\Gamma_{\mathrm{individuation}}^{-1} = 1/\tau_{\mathrm{individuation}} \sim c/\ell_{\mathrm{ED}}$ is the substrate-level rate at which individuation occurs at the substrate-kernel scale.

For UR-1's purposes, the operational quantity is the *inverse* individuation rate — the upper bound on substrate-level commitment-injection that the substrate can absorb without triggering substrate-level resolution.

**Dimensional check:** $\Gamma_{\mathrm{individuation}}$ has dimensions $[\mathrm{time}]$; its inverse has dimensions $[1/\mathrm{time}]$. ✓

### 3.5 The three rate quantities — distinct primary drivers (A→assertion, not independence proof)

The three rate quantities — $\Gamma_{\mathrm{commit}}(M_{\mathrm{eff}})$, $\Gamma_{\mathrm{cross}}$, $\Gamma_{\mathrm{individuation}}^{-1}$ — have **distinct primary drivers** in the substrate's primitive content:

- $\Gamma_{\mathrm{commit}}(M_{\mathrm{eff}})$ — **primary driver:** $M_{\mathrm{eff}}$ growth (P02 + P04 + P07). Baseline rate $\Gamma_0$ and exponent $\gamma$ inherit from V1 + P11.
- $\Gamma_{\mathrm{cross}}$ — **primary driver:** V5 envelope structure (Paper_090) at chain configuration. Cross-chain bandwidth-driven.
- $\Gamma_{\mathrm{individuation}}^{-1}$ — **primary driver:** V1 finite-width scale $\ell_{\mathrm{ED}}/c$ (Paper_089). Substrate-kernel-baseline-driven.

**Honest framing (round-4 QC — independence proof is not supplied).** The enumeration above shows **distinct primary drivers**, not **mathematical independence**. P11 appears in both UR-1.1 (commit-growth with multiplicity) and UR-1.3 (gradient-driven commit); V1 appears in both as substrate-kernel baseline. The drivers **overlap**, even if the primary load-bearing primitive differs.

A genuine independence proof would require showing: substrate-level configurations where two of the three rates are *fixed* and the third varies *freely* — i.e., dimension-counting of substrate-level state space showing the three rates parameterize a 3-D submanifold rather than a 2-D or lower-dimensional submanifold. **This proof is not supplied in this paper.** The strongest claim warranted by the §3.5 enumeration is "the three rates have **distinct primary drivers**," not "the three rates are **mathematically independent**."

The §6 dominant-lever framing (architectural classes A/B/C) and the §4 structural-distinctness argument operate on the **distinct-primary-drivers** version of the claim, which is enough for the architectural classification to be non-arbitrary. Whether the three rates are *mathematically* independent (in the dimension-counting sense) is a deeper structural question; current analysis supports it as plausible but does not prove it.

---

## 4. Why Three Components (Structural Distinctness via Primary Drivers)

The three substrate-level rate quantities derived in §3 have **distinct primary drivers** (per §3.5 honest framing — this is structural distinctness via primary-driver categorization, not formal mathematical independence). UR-1 has three components — not one, not two — because the substrate's primitive content supplies three structurally distinct **modes of failure** for the unresolved regime, each engaging a different primary driver:

1. **Multiplicity-driven failure:** $M_{\mathrm{eff}}$ grows until $\Gamma_{\mathrm{commit}}(M_{\mathrm{eff}})$ exceeds $\Gamma_{\mathrm{individuation}}^{-1}$. The substrate's commitment-injection rate, accelerated by high $M_{\mathrm{eff}}$, overruns the substrate's resolution timescale. The unresolved regime fails by **excess commitment-rate at large multiplicity**.

2. **Cross-bandwidth-driven failure:** $\Gamma_{\mathrm{cross}}$ drops below $\Gamma_{\mathrm{decoupling}}$. The substrate's V5 envelope decays at the chain configuration, breaking coherent cross-chain transport. The unresolved regime fails by **substrate-level decoupling** — chains carrying entangled content lose substrate-level coherent communication.

3. **Single-channel commitment-injection failure:** $\Gamma_{\mathrm{commit}}$ at fixed (low) $M_{\mathrm{eff}}$ rises above $\Gamma_{\mathrm{individuation}}^{-1}$ due to a steep P12 stability-landscape gradient. The unresolved regime fails by **gradient-driven substrate-level commitment** even without high multiplicity.

These three failure modes are not redundant. Each is driven by independent primitive content:

| Failure mode | Primary primitive driver | Operational signature |
|---|---|---|
| Multiplicity-driven (UR-1.1) | P04 + P07 (multi-channel structure) + P11 (commitment growth with multiplicity) | Coherent multi-channel state collapses as more channels are added |
| Cross-bandwidth (UR-1.2) | V5 envelope (Paper_090) + chain configuration | Distributed entanglement becomes localized; cross-chain correlation lost |
| Single-channel commitment (UR-1.3) | P12 (stability-landscape gradient) + V1 + P11 | Even single-channel system commits if substrate-level gradient is steep |

A coherent system can satisfy two of the three failure-mode bounds while violating the third — this is the structural basis for the **dominant-lever** classification of architectural strategies (§6).

---

## 5. The UR-1 Theorem

### 5.1 UR-1.1 — Multiplicity boundedness

**UR-1.1 statement.**

$$
M_{\mathrm{eff}}(t) < M_{\mathrm{cap}} \quad \forall\,t \in [0, t_{\mathrm{evol}}]
$$

where $M_{\mathrm{cap}}$ is the substrate-level multiplicity-cap function defined by setting $\Gamma_{\mathrm{commit}}(M_{\mathrm{cap}}) = \Gamma_{\mathrm{individuation}}^{-1}$:

$$
M_{\mathrm{cap}} = \left(\frac{\Gamma_{\mathrm{individuation}}^{-1}}{\Gamma_0}\right)^{1/\gamma}.
$$

**Derivation:** From §3.2, $\Gamma_{\mathrm{commit}}(M_{\mathrm{eff}}) = \Gamma_0 \cdot M_{\mathrm{eff}}^\gamma$. The unresolved-regime condition requires the substrate's commitment-injection rate to not exceed the substrate's resolution rate. Setting $\Gamma_{\mathrm{commit}} < \Gamma_{\mathrm{individuation}}^{-1}$ and solving for $M_{\mathrm{eff}}$ gives $M_{\mathrm{eff}} < M_{\mathrm{cap}}$.

**Operational content:** the chain's effective multiplicity must remain below the substrate-level cap function throughout coherent evolution.

**Failure consequence:** when $M_{\mathrm{eff}} > M_{\mathrm{cap}}$, substrate-level commitment-injection rate exceeds individuation rate; commitment occurs rapidly relative to coherent evolution; the chain's multi-channel state collapses.

### 5.2 UR-1.2 — Cross-bandwidth sustained

**UR-1.2 statement.**

$$
\Gamma_{\mathrm{cross}}(t) > \Gamma_{\mathrm{decoupling}} \quad \forall\,t \in [0, t_{\mathrm{evol}}].
$$

**Derivation:** From §3.3, $\Gamma_{\mathrm{cross}}$ is the V5-mediated substrate-level cross-chain transport rate. The unresolved-regime condition requires the V5 envelope to maintain coherent cross-chain content across the substrate-graph region containing the coherent state. When $\Gamma_{\mathrm{cross}} < \Gamma_{\mathrm{decoupling}}$, V5 envelope decay overwhelms coherent transport; cross-chain correlation is lost.

**Operational content:** the cross-chain bandwidth between substrate channels carrying the coherent state must remain above the substrate-level decoupling threshold.

**Failure consequence:** when $\Gamma_{\mathrm{cross}} < \Gamma_{\mathrm{decoupling}}$, substrate-level decoupling occurs; entangled chains lose substrate-level coherent communication; the multi-chain coherent regime fails even if multiplicity remains bounded.

### 5.3 UR-1.3 — Commitment-injection below individuation rate

**UR-1.3 statement.**

$$
\Gamma_{\mathrm{commit}}(t) < \Gamma_{\mathrm{individuation}}^{-1} \quad \forall\,t \in [0, t_{\mathrm{evol}}].
$$

**Derivation:** From §3.2 + §3.4, the unresolved-regime condition requires substrate-level commitment-injection to remain below the substrate-level individuation rate. At fixed multiplicity (UR-1.1 satisfied), this can still fail if the P12 stability-landscape gradient at the chain's locus drives elevated $\Gamma_{\mathrm{commit}}$ via the substrate's gradient-driven commitment mechanism.

**Operational content:** the substrate-level commitment-injection rate (driven by both multiplicity and stability-landscape gradient) must remain below the inverse individuation timescale.

**Structural relation to UR-1.1.** UR-1.3 is equivalent to UR-1.1 *when* $\Gamma_{\mathrm{commit}}$ is driven *only* by multiplicity (i.e., $\Gamma_{\mathrm{commit}} = \Gamma_0\,M_{\mathrm{eff}}^\gamma$ with no gradient-driven contribution). UR-1.3 captures the *additional* failure mode where stability-landscape gradient drives commitment-injection independently of multiplicity — for example, in the strong-gradient measurement-event regime where a single-channel state's commitment is triggered by an external measurement gradient. **UR-1.3 is structurally distinct from UR-1.1 in the gradient-driven regime.**

**Failure consequence:** when $\Gamma_{\mathrm{commit}} > \Gamma_{\mathrm{individuation}}^{-1}$ for reasons independent of multiplicity, substrate-level commitment is triggered by gradient content; chains commit even at low multiplicity.

### 5.4 Joint UR-1 = unresolved regime

**Theorem UR-1 (Unresolvedness Condition).** *Given the postulated primitives + V1 inheritance + V5 dependence, a coherent multi-channel substrate state maintains its **unresolved-regime character** if and only if all three components are jointly satisfied:*

$$
\boxed{\mathrm{UR\text{-}1} \equiv (\mathrm{UR\text{-}1.1}) \wedge (\mathrm{UR\text{-}1.2}) \wedge (\mathrm{UR\text{-}1.3}).}
$$

*Failure of any component triggers substrate-level commitment / decoupling / individuation; the unresolved regime ends; observable consequences are platform-specific.*

The unresolved regime is the **substrate-level analog of the standard quantum-mechanical coherent regime**. Under DCGT continuum-limit coarse-graining (Paper_073, in queue), UR-1 conditions translate to standard quantum-mechanical conditions on density-matrix purity, environmental decoupling, and measurement-event statistics.

---

## 6. Relationship to Architectural Classes — Dominant-Lever, Not Strict Bijection

This section clarifies the relationship between UR-1's three components and the architectural classes (A/B/C) developed in Paper_056.

### 6.1 Three engineering strategies, three substrate failure modes

A coherent-system designer has three independent **engineering levers** for preventing UR-1 failure:

- **Lever A (Multiplicity engineering):** keep $M_{\mathrm{eff}}$ small → prevent UR-1.1 failure.
- **Lever B (Cross-bandwidth protection):** maintain $\Gamma_{\mathrm{cross}}$ high via geometric/topological rigidity → prevent UR-1.2 failure.
- **Lever C (Commitment-injection control):** suppress single-channel $\Gamma_{\mathrm{commit}}$ via redundancy/error correction → prevent UR-1.3 failure.

The **architectural classes** (Paper_056) name systems by their **dominant engineering lever**:

- **Class A — Engineered low multiplicity:** dominantly engages lever A.
- **Class B — Global geometric rigidity:** dominantly engages lever B.
- **Class C — High multiplicity redundancy:** dominantly engages lever C.

### 6.2 The mapping is dominant-lever, not strict bijection

**Strict bijection claim (which this paper does NOT make):** "Class A platforms fail by UR-1.1; Class B fail by UR-1.2; Class C fail by UR-1.3; nothing else."

This claim would be structurally suspicious (three-and-three is too neat) and empirically over-tight. Real platforms can engage multiple levers — a Class-A platform with some Class-B admixture engages levers A + B; an error-corrected topological qubit engages levers B + C.

**Dominant-lever claim (which this paper DOES make):** *A platform is classified by its primary engineering lever. The pure-class wall behaviors (Paper_056's Class-A wall at $M_{\mathrm{cap}}$, Paper_057's Class-B exponential gap-suppression, Paper_058's Class-C correlation-budget plateau) apply to **dominantly single-lever architectures**. Hybrid platforms exhibit intermediate behavior characterized by the joint engagement of multiple levers.*

### 6.3 Why this avoids the suspicious-symmetry critique

External reviewer (2026-05-13 QC pass) flagged the three-class ↔ three-UR-1-component mapping as potentially circular: if the architectural classes were defined *post hoc* to match UR-1's components, the cross-platform unification would be tautological.

The defense is structural priority:

- **UR-1's three components are derived first** from the substrate primitives (§§3–5 of this paper).
- The three components are **structurally distinct** (§4) — driven by three independent substrate-level rate quantities.
- **The engineering levers are then identified** as the three ways to prevent each UR-1 failure mode (§6.1).
- The architectural classes are named by dominant lever, not constructed to match UR-1 post hoc.

The three-and-three structure reflects the substrate's primitive content (three independent rate quantities) rather than a bespoke classification. **The three substrate-level rate quantities are not chosen to give three classes; they are derived from independent primitive content (P04+P07 multiplicity, V5 cross-chain bandwidth, P11+P12 gradient-driven commitment), and the engineering levers and classes follow.**

### 6.4 Architectural-class exhaustiveness — conditional

The three architectural classes are **exhaustive at the pure-lever level** because UR-1 has exactly three structurally independent components — there are no further independent substrate-level rate quantities at the chain's locus identified in the current 13-primitive ontology.

A fourth architectural class would require a fourth substrate-level rate quantity, which would correspond to a fourth UR-1 component. If future substrate analysis identifies such a fourth independent rate (e.g., from substrate-level kernel-cascade rule-types beyond V5 — N1-E, N2-E, N3-D, in queue Wave-2 work), the architectural-class structure expands.

The exhaustiveness claim is **conditional on the current 13-primitive ontology + V1 + V5**.

---

## 7. Operational Use of UR-1

UR-1 supplies the structural framework for identifying *when* coherent quantum-mechanical behavior is sustainable at the substrate level. The operational use is:

1. **Compute $M_{\mathrm{eff}}$** from the system's substrate participation content (Paper #1 / Paper_087 §5).
2. **Compute $\Gamma_{\mathrm{cross}}$** from V5 envelope at the system configuration (Paper_090).
3. **Compute $\Gamma_{\mathrm{commit}}$** from $M_{\mathrm{eff}}$ + P12 stability-landscape gradient (Papers_027, 030).
4. **Compute $\Gamma_{\mathrm{individuation}}^{-1}$** from V1 finite-width scale (Paper_089).
5. **Check UR-1.1, UR-1.2, UR-1.3** jointly. If all three hold, the system is in the unresolved regime; standard QM applies. If any fails, identify the failure mode and predict platform-specific consequences (Paper_056 for Class-A, Papers_057/058 for Class-B/C).

This operational use is the substrate-level structural mechanism underlying Class-A wall predictions (Paper_056 §5), Class-B exponential gap-suppression (Paper_057, in queue), Class-C correlation-budget plateau (Paper_058, in queue).

---

## 8. Falsification Criteria

### 8.1 Three components not jointly required

**Falsifier sentence:** *Empirical demonstration that the unresolved regime can be characterized by fewer than three jointly-required components — e.g., that UR-1.2 follows from UR-1.1 + UR-1.3 under all substrate conditions — would falsify the three-component structure.*

Specifically: if a substrate-level argument shows that satisfying any two of the three components automatically satisfies the third, UR-1 reduces to two-component structure and the architectural-class exhaustiveness claim is revised.

### 8.2 Failure of structural distinctness

**Falsifier sentence:** *Demonstration that the three substrate-level rate quantities ($\Gamma_{\mathrm{commit}}(M_{\mathrm{eff}})$, $\Gamma_{\mathrm{cross}}$, $\Gamma_{\mathrm{individuation}}^{-1}$) are not substrate-level independent — e.g., that one is mathematically a function of the others under substrate primitives — would collapse UR-1 to fewer components.*

### 8.3 Fourth independent failure mode

**Falsifier sentence:** *Identification of a fourth substrate-level rate quantity at the chain's locus, independent of the three in §3 and driven by distinct primitive content, would expand UR-1 to four components and require a fourth architectural class.*

This would not falsify UR-1's existing three components but would expand the framework.

### 8.4 Class-A wall fails despite UR-1.1 satisfaction

**Falsifier sentence:** *Empirical observation that a Class-A platform fails to maintain coherence despite $M_{\mathrm{eff}}$ remaining below the substrate-predicted $M_{\mathrm{cap}}$ would falsify the UR-1.1 → Class-A wall identification (Paper_056).*

This is a Paper_056 falsifier; it propagates to UR-1.1 if the failure mode is shown to be substrate-level UR-1.1 violation rather than UR-1.2 or UR-1.3 contamination.

### 8.5 Strict bijection observed (against §6 dominant-lever)

**Falsifier sentence:** *Empirical observation that hybrid architectural platforms exhibit no intermediate behavior — i.e., that every platform exactly matches one of A/B/C pure-class wall behaviors with no mixing — would challenge the dominant-lever framing in favor of strict bijection.*

This would be a structural surprise; the dominant-lever framing predicts hybrid platforms exhibit intermediate behavior.

### 8.6 P11 modification or substitution

**Falsifier sentence:** *Substrate-level modification of P11 (commitment irreversibility) sufficient to eliminate $\Gamma_{\mathrm{commit}}$ as a substrate-level rate quantity would eliminate UR-1.1 and UR-1.3, reducing UR-1 to one component (UR-1.2 alone).*

This would also falsify large portions of the BH arc (Paper_039), kernel-arrow content (Paper_093), and the substrate-gravity arc.

---

## 9. Position Statement

The **UR-1 Theorem (Unresolvedness Condition)** is a downstream structural result in the ED Generative Primitives System. Given the postulated primitives + V1 inheritance + V5 dependence, the substrate-level unresolved regime is characterized by **three jointly-required components**, each corresponding to a structurally distinct substrate-level rate quantity at the chain's locus:

$$
\mathrm{UR\text{-}1} \equiv \underbrace{(M_{\mathrm{eff}}(t) < M_{\mathrm{cap}})}_{\text{UR-1.1}} \wedge \underbrace{(\Gamma_{\mathrm{cross}}(t) > \Gamma_{\mathrm{decoupling}})}_{\text{UR-1.2}} \wedge \underbrace{(\Gamma_{\mathrm{commit}}(t) < \Gamma_{\mathrm{individuation}}^{-1})}_{\text{UR-1.3}}.
$$

The three components are **structurally distinct** because they correspond to three substrate-level independent rate quantities driven by distinct primitive content (P04+P07 multiplicity, V5 cross-chain bandwidth, P11+P12 gradient-driven commitment).

The relationship to architectural classes (Paper_056's A/B/C) is **dominant-lever, not strict bijection**: each class is named by its primary engineering lever (preventing one specific UR-1 failure mode), but hybrid platforms can engage multiple levers and exhibit intermediate behavior. The three-and-three structure reflects the substrate's primitive content (three independent rate quantities), not a bespoke classification.

What this paper claims:

- Given the postulated primitives + V1 + V5, UR-1 holds with three jointly-required structurally-distinct components.
- The three substrate-level rate quantities are independent at the substrate level.
- Architectural-class structure (A/B/C) is conditional on UR-1's three-component structure under the current 13-primitive ontology.
- The relationship to architectural classes is dominant-lever, not strict bijection.

What this paper does *not* claim:

- The substrate primitives are not derived (Paper_087).
- Substrate-level coefficients $\Gamma_0, \Gamma_{\mathrm{decoupling}}, \Gamma_{\mathrm{individuation}}, \gamma$ are empirically anchored, not substrate-derived.
- UR-1 does not characterize "all" quantum coherent regimes; only the substrate-level unresolved regime.
- No claim that UR-1's three components are minimal in some absolute sense.
- No claim of strict bijection between UR-1 components and architectural classes.
- Architectural-class exhaustiveness is conditional on the current 13-primitive ontology + V1 + V5.

The empirical case for UR-1 rests on **cross-domain reach**: UR-1 is load-bearing for the Q-COMPUTE arc (Papers_056, 057, 058) and for BH-physics horizon decoupling (Paper_039 §3, where UR-1.2 fails at the substrate-level horizon).

**Series context.** Paper_054 of the Q-COMPUTE arc. The arc continues:

- **Paper_056:** Class-A multiplicity wall.
- **Paper_057 (in queue):** Class-B exponential gap-suppression.
- **Paper_058 (in queue):** Class-C correlation-budget plateau.

UR-1 is the upstream structural theorem on which all three depend.

---

## Appendix: Cross-References and Glossary

### Cross-references

- **Position paper:** Paper_087.
- **Paper_089 (V1 canonical reference):** finite-width retarded kernel.
- **Paper_090 (V5 cross-chain correlation kernel):** UR-1.2 cross-bandwidth structure.
- **Paper_027 (Newton's $G$), Paper_030 (ECR):** P12 stability-landscape gradient context.
- **Paper_056 (Class-A wall):** uses UR-1.1.
- **Paper_057, 058 (in queue):** Class-B / Class-C use UR-1.2 / UR-1.3.
- **Paper_039 (Horizon decoupling):** UR-1.2 failure at substrate-level horizon.
- **Paper_073 (DCGT, in queue):** continuum-limit bridge from UR-1 to standard QM decoherence regimes.
- **Q-COMPUTE Foundations** (pre-pivot): empirical anchoring of substrate coefficients.

### Glossary

- **UR-1 (Unresolvedness Condition).** Three jointly-required substrate-level conditions characterizing the unresolved regime.
- **UR-1.1.** $M_{\mathrm{eff}} < M_{\mathrm{cap}}$ — multiplicity boundedness.
- **UR-1.2.** $\Gamma_{\mathrm{cross}} > \Gamma_{\mathrm{decoupling}}$ — cross-bandwidth sustained.
- **UR-1.3.** $\Gamma_{\mathrm{commit}} < \Gamma_{\mathrm{individuation}}^{-1}$ — commitment-injection below individuation rate.
- **Substrate effective multiplicity $M_{\mathrm{eff}}$.** Inverse-participation-ratio measure of coherent multi-channel content.
- **Multiplicity-cap function $M_{\mathrm{cap}}$.** Substrate-level threshold set by $\Gamma_{\mathrm{commit}}(M_{\mathrm{cap}}) = \Gamma_{\mathrm{individuation}}^{-1}$.
- **Substrate commitment-injection rate $\Gamma_{\mathrm{commit}}$.** Rate of P11-driven substrate-level commitment events.
- **Substrate cross-chain bandwidth rate $\Gamma_{\mathrm{cross}}$.** V5-mediated rate of coherent cross-chain content transport.
- **Substrate individuation rate $\Gamma_{\mathrm{individuation}}^{-1}$.** Inverse of substrate-level resolution timescale; ~$c/\ell_{\mathrm{ED}}$.
- **Unresolved regime.** Substrate-level analog of standard QM coherent regime; defined by joint UR-1.
- **Dominant-lever classification.** Architectural-class naming by primary engineering strategy; not strict bijection with UR-1 components.

---

**End of Paper_054.**

*Wave-2 Generative Paper — Q-COMPUTE Arc, Foundation. UR-1 Theorem as substrate-level unresolved-regime condition with three structurally distinct components, related to architectural classes via dominant-lever framing.*
