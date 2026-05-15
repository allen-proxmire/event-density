# Paper 040 — Trans-Planckian Resolution via V5 Cutoff $\omega_c = c/\ell_P$

**Series:** Wave-2 Generative Papers (Black-Hole Arc)
**Status:** Conditional structural derivation given the 13 ED primitives (per Paper_087) + paper-specific postulates declared in §2.
**Companions:** Paper_039 (horizon as decoupling surface), Paper_047 (Hawking spectrum), Paper_073 (DCGT), Paper_089 (V1), Paper_090 (V5).

---

## Preamble — What This Paper Does NOT Claim

1. This paper does **not** claim that the trans-Planckian problem is universally resolved across all approaches to Hawking radiation; the resolution here is specific to the substrate-level V5-cutoff approach.
2. It does **not** claim numerical predictions for the Hawking spectrum corrections at trans-Planckian frequencies; the cutoff structural resolution is at the form level.
3. It does **not** introduce new substrate primitives.
4. "Trans-Planckian problem" means: in standard semiclassical Hawking calculations, the outgoing Hawking modes trace back to ingoing modes with frequencies exceeding the Planck scale near the horizon, signaling a breakdown of the semiclassical framework at trans-Planckian scales.
5. "V5 cutoff resolution" means: substrate-level dynamics are characterized by V5's cross-chain correlation kernel with bandwidth $\omega_c = c/\ell_P$; modes above this cutoff do not exist as substrate-level excitations, so the semiclassical mode-tracing argument terminates at the cutoff.

---

## Abstract

The trans-Planckian problem is structurally resolved at the substrate level in ED by V5's intrinsic UV cutoff $\omega_c = c/\ell_P$ (Paper_090). Substrate-level modes do not exist above $\omega_c$; the semiclassical mode-tracing argument that produces the trans-Planckian frequencies terminates at the cutoff. The resolution is **inherent to the substrate** (no fine-tuning required) and is therefore consistent with the regulated-completion verdict of Arc Hawking (Paper_047). The Hawking spectrum corrections at frequencies approaching $\omega_c$ are characterized at form level; their leading-order substrate effect is suppressed at $(\ell_P / M)^2$ for black holes of mass $M$.

---

## §1 Introduction

The trans-Planckian problem in Hawking radiation: in the standard derivation, outgoing Hawking quanta of frequency $\omega \sim T_H$ at infinity correspond to ingoing modes with frequencies blueshifted near the horizon to $\omega_{\mathrm{near-horizon}} \sim \omega \exp(\kappa t)$, exceeding $\omega_P = c/\ell_P$ within finite time. Standard semiclassical QFT is not valid above $\omega_P$, yet the derivation requires propagating modes through this regime.

This paper supplies the substrate-level resolution: V5's bandwidth cutoff $\omega_c = c/\ell_P$ truncates the substrate mode content. Modes above $\omega_c$ do not exist substantively at substrate level; the mode-tracing argument terminates at the cutoff.

---

## §2 Primitive Inputs and Paper-Specific Postulates

### 2.1 Primitives invoked (per Paper_087)

- **P08 (Substrate scale $\ell_{\mathrm{ED}}$)** — supplies the Planck length $\ell_P$.
- **P10 (Rule-type primitive)** — supplies V5 kernel rule-type (Paper_090).
- **P11 (Commitment-irreversibility)** — supplies the directional structure for retarded propagation.
- **P13 (Time homogeneity)** — supplies time-translation symmetry on which frequencies are defined.

### 2.2 Upstream dependencies

- **I-039:** Horizon as decoupling surface (Paper_039).
- **I-047:** Hawking spectrum via substrate-Unruh (Paper_047).
- **I-073:** DCGT (Paper_073).
- **I-090:** V5 cross-chain correlation kernel (Paper_090).
- **I-014:** V1 in curved acoustic background (Paper_014).

### 2.3 Paper-specific postulates

- **P-V5-UV-Cutoff:** The V5 kernel rule-type has intrinsic UV cutoff $\omega_c = c/\ell_P$: substrate modes above $\omega_c$ are not supported by V5 cross-chain correlation structure.
- **P-Cutoff-Saturation:** The trans-Planckian mode content predicted by semiclassical mode-tracing saturates the V5 cutoff at the horizon-crossing scale; substrate-level mode content terminates rather than continuing trans-Planckian.

---

## §2.5 Load-Bearing Step Audit Table

| # | Step | Label | Notes |
|---|---|---|---|
| 1 | V5 cross-chain kernel with finite bandwidth | I | Paper_090. |
| 2 | V5 UV cutoff $\omega_c = c/\ell_P$ | P-V5-UV-Cutoff | Postulate. |
| 3 | Horizon as decoupling surface | I | Paper_039. |
| 4 | Hawking spectrum via substrate-Unruh | I | Paper_047. |
| 5 | Semiclassical mode-tracing produces trans-Planckian frequencies | I | Standard semiclassical analysis. |
| 6 | Substrate modes do not exist above $\omega_c$ | P-V5-UV-Cutoff | Postulate (re-statement at mode level). |
| 7 | Mode-tracing argument terminates at $\omega_c$ | P-Cutoff-Saturation | Postulate. |
| 8 | Trans-Planckian problem structurally resolved | D-via-I | Composition of P-V5-UV-Cutoff + P-Cutoff-Saturation. |
| 9 | Leading-order corrections at $(\ell_P/M)^2$ | I | Standard QFT perturbation. |
| 10 | Numerical values of corrections | I | Empirical / standard math. |

---

## §3 The Resolution

### 3.1 The trans-Planckian problem at substrate level

In the standard derivation (I), Hawking outgoing modes correspond to ingoing modes with frequencies $\omega_{\mathrm{near-horizon}} \sim \omega \exp(\kappa t)$, growing without bound. Substrate-level modes are supported by V5 cross-chain correlation; by P-V5-UV-Cutoff, V5 has bandwidth $\omega_c = c/\ell_P$.

### 3.2 Substrate modes terminate at $\omega_c$

By P-Cutoff-Saturation, substrate modes do not exist above $\omega_c$; the semiclassical mode-tracing argument runs out of substrate modes at the cutoff. The trans-Planckian extrapolation is not substrate-supported.

### 3.3 Why the resolution is intrinsic (not fine-tuned)

The cutoff $\omega_c$ is set by **substrate scale $\ell_P$ via P08** — it is not a free parameter. Standard dispersion-modification approaches to the trans-Planckian problem introduce a UV cutoff by hand; the substrate program inherits the cutoff from primitive content.

### 3.4 Corrections at $(\ell_P/M)^2$

For a black hole of mass $M$, the Hawking temperature $T_H \sim 1/M$ is far below $\omega_c \sim 1/\ell_P$. Substrate corrections are suppressed at $O(T_H/\omega_c)^2 \sim (\ell_P/M)^2$. For solar-mass black holes, this is $\sim 10^{-76}$ — negligible. For Planck-mass remnants (Paper_041), corrections become $O(1)$ — see Paper_041.

---

## §4 Falsification Criteria

- **F1:** Empirical detection of Hawking-spectrum trans-Planckian-frequency contributions inconsistent with substrate cutoff — refutes P-V5-UV-Cutoff or P-Cutoff-Saturation.
- **F2:** Substrate evidence that V5 admits modes above $\omega_c$ — refutes P-V5-UV-Cutoff.
- **F3:** Substrate evidence that the semiclassical mode-tracing argument can continue past the cutoff under substrate-consistent dynamics — refutes P-Cutoff-Saturation.
- **F4:** Empirical detection of corrections of order $(\ell_P/M)^k$ for $k < 2$ — would require revised perturbation expansion.

---

## §5 Position Statement

The trans-Planckian problem is **structurally resolved** at the substrate level by the V5 UV cutoff $\omega_c = c/\ell_P$ inherited from P08 + P10. Substrate modes do not exist above $\omega_c$; the semiclassical mode-tracing argument terminates at the cutoff. Leading-order corrections to the Hawking spectrum are at $(\ell_P/M)^2$, suppressed for macroscopic black holes. The resolution is **intrinsic** (not fine-tuned).

This feeds Paper_047 (Hawking spectrum) and Paper_041 (Planck-mass remnants).

---

**End Paper 040 (FIXED).**
