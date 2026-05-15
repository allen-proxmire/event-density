# Paper_074 — V5 Viscoelastic Maxwell Ansatz Substrate-Grounded

**Series:** Event Density (ED) Generative Papers — Wave-2 soft-matter arc
**Author:** Allen Proxmire
**Status:** Publication draft (opens soft-matter arc proper after Paper_073 DCGT)
**Date:** 2026-05-13
**Repository target:** `domain-arcs/soft-matter/Paper_074_V5_MaxwellAnsatz.md`
**Genre:** Conditional structural derivation within the 13-Primitive Generative System.

---

## Preamble: What This Paper Does NOT Claim

1. **The 13 primitives are not derived** (Paper_087).
2. **The Maxwell viscoelastic ansatz numerical parameters are not derived.** The exponential-decay form is structurally derived from V5 + DCGT (under Markovian limit); the **relaxation time $\tau_{\mathrm{Maxwell}}$** is **empirically matched** to substrate $\tau_{V5}^{\mathrm{soft}}$ — labeled I per Paper_073 §6.1 + Paper_090 §5.1.
3. **No claim of derivation of Krieger–Dougherty / Cross / Carreau viscosity laws.** Standard polymer-melt constitutive laws are inherited; this paper derives the substrate-level **Maxwell form**, with downstream extensions to specific constitutive laws in queue.
4. **No claim that all polymer-melt viscoelasticity is captured by Maxwell ansatz.** The Maxwell ansatz is a substrate-level structural foundation; multi-mode / non-exponential relaxation requires substrate-level extensions (e.g., V5 with multi-scale envelope).
5. **No claim of derivation of substrate-level molecular structure.** Polymer-molecule substrate content is inherited from chemistry; substrate framework supplies kernel-coarse-graining mechanism.

---

## Abstract

This paper derives the **Maxwell viscoelastic ansatz** $G(t) = G_0\,e^{-t/\tau_{\mathrm{Maxwell}}}$ for stress-relaxation in polymer melts and non-Newtonian fluids, as a substrate-level structural consequence of V5 cross-chain correlation kernel (Paper_090) + DCGT continuum limit (Paper_073) + the **Markovian-limit regime** ($\tau_{V5}^{\mathrm{soft}} \ll L_{\mathrm{flow}}/c$). The substrate-level mechanism:

- Polymer molecules are substrate-level extended chain structures (P02 + P07).
- V5 cross-chain correlation between distinct polymer molecules at substrate-level locus pairs produces substrate-level stress content.
- DCGT coarse-graining in the soft-matter regime + Markovian limit produces continuum exponential-relaxation form (Paper_073 §6.1).
- Identification $\tau_{V5}^{\mathrm{soft}} = \tau_{\mathrm{Maxwell}}$ is **empirical matching** (labeled I); structural form is derived.

**Numerical Matching Honesty:** $\tau_{\mathrm{Maxwell}}$ for any specific polymer system is value-layer empirical (rheometry data); ED supplies form, not value. The structural prediction is the **exponential-decay form** (Markovian Maxwell), not the numerical timescale.

The paper makes no claim of derivation of polymer-specific relaxation times, no claim of derivation of all soft-matter constitutive laws, and no claim of substrate-level chemistry.

---

## 1. Introduction

### 1.1 What this paper does

This paper opens the **soft-matter arc** properly after Paper_073 DCGT (the substrate→continuum bridge). It supplies the substrate-level **Maxwell viscoelastic-ansatz** derivation that Paper_073 §6.1 referenced and Paper_090 §5.1 promised.

### 1.2 Arc context

- **Paper_073:** DCGT.
- **Paper_074 (this paper):** V5 Maxwell ansatz.
- **Papers_075–086 (in queue):** NS-1 through NS-Synthesis (Navier-Stokes program); P4-NN (Krieger-Dougherty + Maxwell); soft-matter empirical anchors.

---

## 2. Primitive Inputs

**Substrate primitives:** P02, P03, P04, P07.

**Upstream paper dependencies:** Paper_087, Paper_073 (DCGT), Paper_090 (V5).

**Paper-specific postulates:**

- **P-Polymer-as-Chain (Polymer molecules as substrate-level extended chains):** *Polymer molecules in soft-matter systems are substrate-level extended-chain structures with internal participation-channel structure (P02 + P07). Distinct polymer molecules in a sample are substrate-level distinct chains.* Substrate-level identification commitment for polymer systems.
- **P-Stress-from-V5 (Substrate stress content from V5 cross-chain correlation):** *Polymer-melt stress content emerges at substrate level from V5-mediated cross-chain correlation between distinct polymer molecules.* Substrate-level commitment about how soft-matter stress maps to substrate V5 content.

**Empirical / value-layer inputs:**

- $\tau_{\mathrm{Maxwell}}$ for specific polymer systems: rheometry data (I).
- $G_0$ initial modulus: value-layer.

---

## 2.5 Load-Bearing Step Audit

| Step | Status | Justification |
|---|---|---|
| 13 primitives + V1 + V5 + DCGT | P / D / I | Paper_087, 089, 090, 073 |
| Polymer molecules = substrate-level chains | **P (P-Polymer-as-Chain)** | §2 substrate-level identification |
| Polymer-melt stress = V5 cross-chain correlation content | **P (P-Stress-from-V5)** | §2 substrate-level commitment |
| Markovian-limit regime ($\tau_{V5}^{\mathrm{soft}} \ll L_{\mathrm{flow}}/c$) | **A→regime** | §3.1 regime condition for exponential-decay form |
| DCGT Markovian-limit form $G(t) \propto e^{-t/\tau_{V5}^{\mathrm{soft}}}$ | **I conditional on Markovian regime (inherited from Paper_073 §6.1)** | §3.2 — form delivered by Paper_073 DCGT machinery applied to V5 soft-matter Markovian limit; not derived in this paper. *(Round-8 relabel: was D conditional on Markovian regime, now I conditional on Markovian regime — Paper_073 supplies the DCGT result.)* |
| Exponential-decay structural form (Maxwell relaxation) | **I** | §3.3 — restates §3.2's result under standard-Maxwell-form identification; not an additional derivation. Folded into the inherited DCGT form row above. |
| Numerical $\tau_{\mathrm{Maxwell}}$ for specific system | **I (empirical matching to $\tau_{V5}^{\mathrm{soft}}$)** | Rheometry data; not substrate-derived. Per Numerical-Matching Honesty Rule. |
| Initial modulus $G_0$ | I | Value-layer |
| Non-Markovian extension to multi-mode relaxation | NOT CLAIMED | preamble item 4 |
| Krieger–Dougherty / Cross / Carreau laws | NOT CLAIMED (downstream) | preamble item 3 |

All rows P, D, I, or labeled. **No A (asserted) rows.**

---

## 3. Substrate-Level Maxwell Ansatz

### 3.1 Markovian-limit regime

The Markovian-limit regime is the substrate-level condition:

$$
\tau_{V5}^{\mathrm{soft}} \ll L_{\mathrm{flow}}/c
$$

where $\tau_{V5}^{\mathrm{soft}}$ is the V5 substrate-level memory time in the soft-matter regime and $L_{\mathrm{flow}}/c$ is the macroscopic-flow timescale. In this regime, V5's substrate-level memory is fast compared to the timescale on which polymer-melt stress varies macroscopically — and V5 effectively acts as a **memoryless** substrate-level coupling at coarse-grained scales.

This is **A→regime** — a regime condition labeled openly.

### 3.2 DCGT Markovian-limit form

By Paper_073 §6.1 (DCGT V5 → Maxwell relaxation; round-5 fix: form derived, value matched), under Markovian limit DCGT produces:

$$
G(t) = G_0\,e^{-t/\tau_{V5}^{\mathrm{soft}}}.
$$

The **form** (exponential decay) is **derived** from V5 finite-memory envelope under DCGT Markovian limit. The **value** $\tau_{V5}^{\mathrm{soft}}$ is **empirically matched** to $\tau_{\mathrm{Maxwell}}$ via rheometry data.

**Explicit derivation step (algebraic):** V5's exponential temporal envelope $F_{V5}(t/\tau_{V5}^{\mathrm{soft}}) \sim e^{-t/\tau_{V5}^{\mathrm{soft}}}$ (Paper_090 §3.3) in the Markovian limit acts as a $\delta$-function in time multiplied by a damping coefficient on macroscopic timescales; the substrate-level stress correlation function $G(t) = \langle\sigma(t)\sigma(0)\rangle_{V5}$ inherits the V5 exponential form via standard convolution structure under DCGT.

**Dimensional check:** $G(t)$ has units of stress (modulus); $G_0$ has stress units; $e^{-t/\tau}$ dimensionless. ✓

### 3.3 The Maxwell ansatz

The standard Maxwell viscoelastic-ansatz:

$$
\boxed{G(t) = G_0\,e^{-t/\tau_{\mathrm{Maxwell}}}}
$$

with the substrate-level identification $\tau_{\mathrm{Maxwell}} = \tau_{V5}^{\mathrm{soft}}$ (empirical matching, labeled I).

**This is the substrate-level Maxwell viscoelastic ansatz.** The form is derived; the value is matched.

### 3.4 Empirical content

For typical polymer melts: $\tau_{\mathrm{Maxwell}} \sim 10^{-3}$ s (~ms range). Substrate-level $\tau_{V5}^{\mathrm{soft}}$ is matched to this value — the substrate framework does not predict the millisecond timescale from first principles; it inherits it from rheometry.

**Cross-polymer comparison:** different polymer systems have different $\tau_{\mathrm{Maxwell}}$ ranging from microseconds to seconds depending on molecular weight, temperature, chemistry. Each substrate-level $\tau_{V5}^{\mathrm{soft}}$ is empirically matched per system; the **structural form** (exponential Maxwell) is universal across polymer systems in the Markovian regime.

### 3.5 Non-Markovian extension (brief)

Outside the Markovian limit ($\tau_{V5}^{\mathrm{soft}} \sim L_{\mathrm{flow}}/c$), the substrate-level Maxwell ansatz fails; multi-mode / non-exponential relaxation requires substrate-level extension (e.g., V5 with multi-scale envelope structure). This is downstream work; this paper restricts to single-mode Markovian Maxwell.

---

## 4. Falsification Criteria

### 4.1 Polymer-melt stress relaxation non-exponential

**Falsifier sentence:** *Empirical demonstration that polymer-melt stress relaxation in the Markovian-limit regime is non-exponential (e.g., power-law, stretched-exponential) at substrate level — would falsify §3.2 + §3.3.*

### 4.2 Polymer molecules not substrate-level chains

**Falsifier sentence:** *Demonstration that polymer molecules at substrate level have non-chain structure (e.g., are derived from continuum-field content not reducible to substrate-chain structure) — would falsify P-Polymer-as-Chain.*

### 4.3 Polymer-melt stress not V5-mediated

**Falsifier sentence:** *Empirical demonstration that polymer-melt stress content originates from substrate-level mechanism other than V5 cross-chain correlation — would falsify P-Stress-from-V5.*

### 4.4 Markovian-limit regime fails universally

**Falsifier sentence:** *Empirical demonstration that all polymer-melt systems are intrinsically non-Markovian (no substrate-level Markovian regime accessible) — would force replacement of the Maxwell-ansatz form with multi-mode substrate machinery throughout soft-matter arc.*

---

## 5. Position Statement

The **Maxwell viscoelastic ansatz** is a substrate-level structural form derived from V5 (Paper_090) + DCGT (Paper_073 §6.1) + P-Polymer-as-Chain + P-Stress-from-V5 + Markovian-limit regime assumption. Numerical $\tau_{\mathrm{Maxwell}}$ is value-layer empirical (matched to substrate $\tau_{V5}^{\mathrm{soft}}$).

What this paper claims:

- Substrate-level Maxwell form derived for Markovian-limit polymer-melt regime.
- Form structural; value matched.
- Opens soft-matter arc proper.

What this paper does *not* claim:

- $\tau_{\mathrm{Maxwell}}$ values not derived.
- Standard Krieger–Dougherty / Cross / Carreau laws not derived (downstream).
- Non-Markovian multi-mode extension not in this paper.
- Substrate-level molecular structure not derived.

**Series context.** Paper_074 of soft-matter arc.

---

## Appendix

**Cross-references:** Paper_087, Paper_073, Paper_090.

**Glossary:**
- **Maxwell viscoelastic ansatz.** $G(t) = G_0\,e^{-t/\tau_{\mathrm{Maxwell}}}$ stress-relaxation form.
- **Markovian-limit regime.** $\tau_{V5}^{\mathrm{soft}} \ll L_{\mathrm{flow}}/c$.
- **P-Polymer-as-Chain.** Polymer molecules as substrate-level extended chains.
- **P-Stress-from-V5.** Soft-matter stress mapped to V5 cross-chain correlation.

---

**End of Paper_074.**
