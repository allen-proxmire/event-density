# Paper_006 — Unitary Evolution from V1 Kernel Propagation

**Series:** Event Density (ED) Generative Papers — Wave-2 QM-kinematics arc
**Author:** Allen Proxmire
**Status:** Publication draft
**Date:** 2026-05-13
**Repository target:** `domain-arcs/qm-kinematics/Paper_006_UnitaryEvolution.md`
**Genre:** Conditional structural derivation within the 13-Primitive Generative System.

---

## Preamble: What This Paper Does NOT Claim

1. **The 13 primitives are not derived** (Paper_087).
2. **No claim that unitary evolution is derived from V1 alone.** Derivation uses V1 (Paper_089) + DCGT (Paper_073) + Paper_004 P-Channel-Orthogonality + Paper-specific P-Norm-Preservation that bridges substrate V1 propagation to standard Hilbert-space norm conservation.
3. **No claim of derivation of specific Hamiltonian operators.** Standard QM Schrödinger evolution $i\hbar\partial_t\Psi = H\Psi$ with specific $H$ is downstream of this paper's structural unitary-evolution form.
4. **No claim that V1 retardation produces literal unitary evolution at substrate level.** V1 is retarded (forward-causal); standard unitary evolution is time-symmetric in operator form (though boundary conditions select retarded propagation in practice). The substrate-level V1 + DCGT produces continuum retarded evolution that, under inner-product norm preservation, has the unitary-evolution form on motif-algebra/Hilbert-space states.
5. **No claim that unitary evolution covers measurement events.** P11 commitment (Paper_005) is irreversible; unitary evolution covers pre-measurement substrate-level dynamics between commitment events.

---

## Abstract

This paper derives **unitary evolution** at substrate level from V1 (Paper_089) + DCGT (Paper_073) + Paper_004 P-Channel-Orthogonality + **P-Norm-Preservation** (this paper's substrate-level commitment that V1-propagation preserves substrate-amplitude norm in the inner-product structure). The substrate-level mechanism:

- V1 substrate-graph propagation acts on Paper_001 amplitude content $\Psi^C(t) = \sum_K P_K^C(t)|K\rangle$ via the V1 retarded kernel.
- DCGT coarse-grains V1 to continuum propagator (Paper_073 §4).
- Under P-Norm-Preservation, the continuum-level propagator preserves the inner-product norm $\|\Psi\|^2 = \sum_K |P_K|^2 = \sum_K b_K$.
- A norm-preserving complex-linear operator on the (Cauchy-completed) Hilbert space is **unitary** (standard linear algebra).
- The substrate-level evolution operator $U(t_2, t_1) = e^{-iH(t_2 - t_1)/\hbar}$ for some Hermitian $H$ (Stone's theorem applied to the substrate-level evolution semigroup).

The substrate-level $H$ (Hamiltonian) is inherited at value-layer (specific system-dependent content); the substrate-level structural form of unitary evolution is derived.

The paper makes no claim of Hamiltonian-derivation, no claim that V1 retardation literally equals unitary-form (it equals it under P-Norm-Preservation), and no claim that measurement events are covered (Paper_005 territory).

---

## 1. Introduction

### 1.1 What this paper does

Paper_007's forward-pointer named Paper_006 as the unitary-evolution derivation. This paper supplies it: V1 substrate-graph propagation + DCGT + Paper_004 + P-Norm-Preservation → standard unitary evolution form.

### 1.2 Arc context

Closes QM-kin trio with Papers_003 (Born) + 005 (measurement) + this paper (dynamics). Paper_007 Hilbert-space completion provides arena.

---

## 2. Primitive Inputs

**Substrate primitives:** P02, P04, P07, P11, P13.

**Upstream paper dependencies:** Paper_087, Paper_001, Paper_004 (P-Channel-Orthogonality), Paper_073 (DCGT), Paper_089 (V1).

**Paper-specific postulate:**

- **P-Norm-Preservation (Substrate V1-propagation preserves inner-product norm):** *Under DCGT continuum-limit coarse-graining of V1 substrate-graph propagation (Paper_073 §4), the substrate-amplitude norm $\|\Psi\|^2 = \sum_K |P_K|^2 = \sum_K b_K$ is preserved along the propagation. Specifically: $\|U(t_2, t_1)\Psi(t_1)\|^2 = \|\Psi(t_1)\|^2$ for any pre-measurement substrate-level interval.* Substrate-level commitment that V1-propagation is **norm-preserving** in the inner-product structure. Not derivable from V1 + DCGT alone (the substrate-level conservation of $\sum b_K$ requires an additional commitment about how V1 acts on bandwidth content).

---

## 2.5 Load-Bearing Step Audit

| Step | Status | Justification |
|---|---|---|
| 13 primitives postulated | P | Paper_087 |
| V1 finite-width retarded kernel | D | Paper_089 |
| DCGT continuum limit (V1 → diffusion-type operator) | I | Paper_073 |
| Paper_004 P-Channel-Orthogonality | P | Paper_004 |
| V1 propagation preserves substrate-amplitude norm | **P (P-Norm-Preservation)** | §2 substrate-level commitment; not derivable from V1 + DCGT alone |
| Continuum propagator $U(t_2, t_1)$ — continuum-limit step | **I (inherited via DCGT, Paper_073)** | §3.1 DCGT coarse-graining of substrate-level V1 evolution → continuum propagator on Hilbert-space states |
| Continuum propagator $U(t_2, t_1)$ — substrate-level identification | **D** | §3.1 substrate-side identification: substrate-level evolution operator constructed from V1 + P-Norm-Preservation, identified with continuum propagator post-DCGT |
| Norm-preservation + complex-linearity → unitary | **I (standard linear algebra)** | §3.2 — polarization identity argument from standard linear algebra; norm-preserving complex-linear operator is unitary. Not substrate-derived. *(Round-7 relabel.)* |
| Stone's theorem: $U(t_2 - t_1) = e^{-iH(t_2 - t_1)/\hbar}$ for some Hermitian $H$ | I | Standard mathematical theorem |
| Hamiltonian $H$ specific value | I | Value-layer; system-specific |
| Time-translation invariance via P13 | D | §3.4 from P13 |

All rows P, D, I, or labeled. **No A (asserted) rows.**

---

## 3. Substrate-Level Unitary Evolution

### 3.1 V1 propagation in continuum limit

By Paper_089, V1 substrate-graph propagation has retarded support. By Paper_073 §4, DCGT coarse-grains V1 to a continuum differential operator $\hat{D}_{\mathrm{cont}}$ with diffusion-type form. In the QM-kin context (pre-measurement, no V5 cross-chain content), V1 acts as a **propagator** on pre-individuation amplitude content:

$$
\Psi(t_2) = U(t_2, t_1)\,\Psi(t_1)
$$

where $U(t_2, t_1)$ is the V1-DCGT-coarse-grained substrate-level evolution operator.

### 3.2 Norm preservation → unitarity

By **P-Norm-Preservation (§2)**, V1 propagation preserves substrate-amplitude norm:

$$
\|U(t_2, t_1)\Psi(t_1)\|^2 = \|\Psi(t_1)\|^2.
$$

A **complex-linear, norm-preserving operator** on a Hilbert space is **unitary** (standard linear algebra). Proof sketch: for $U$ complex-linear with $\|U\Psi\| = \|\Psi\|$ for all $\Psi$, the polarization identity gives $\langle U\Psi|U\Phi\rangle = \langle\Psi|\Phi\rangle$, hence $U^\dagger U = I$, hence $U$ is unitary (on finite-dim; extension to infinite-dim standard).

**Therefore $U(t_2, t_1)$ is unitary** on the Cauchy-completed Hilbert space (Paper_007).

**Dimensional check:** $\Psi$ has substrate-amplitude units; $U$ is dimensionless; $\|U\Psi\| = \|\Psi\|$ has substrate-amplitude units. ✓

### 3.3 Stone's theorem → Hamiltonian form (via standard math inheritance)

The set of substrate-level unitary evolutions $\{U(t_2, t_1): t_2 > t_1\}$ forms a one-parameter strongly-continuous unitary semigroup (under P13 time-homogeneity). **Under standard application of Stone's theorem to the substrate-derived one-parameter unitary semigroup**, the standard Schrödinger evolution form emerges:

$$
U(t_2, t_1) = e^{-iH(t_2 - t_1)/\hbar}
$$

for some Hermitian operator $H$ on the Hilbert space.

**Honest framing (round-7):** Stone's theorem is **inherited standard math** (I). The substrate-derivation supplies the one-parameter unitary-semigroup structure (via P-Norm-Preservation + polarization identity / Stone setup); the **Hamiltonian-exponential form** then follows from Stone's theorem as an inherited mathematical consequence. The substrate-level content is the unitary-semigroup structure; the Hamiltonian form is the standard-math image of that structure.

The specific $H$ for a given physical system is **value-layer inherited** — particle-in-potential, multi-particle interactions, etc., come from specific system content not derivable from substrate primitives alone.

### 3.4 P13 time-homogeneity

By P13 (substrate time-homogeneity), $U(t_2, t_1) = U(t_2 - t_1)$ — depends only on the time interval, not on absolute time. Consistent with time-translation-invariant Hamiltonian dynamics.

### 3.5 Schrödinger equation

From $\Psi(t) = U(t)\Psi(0) = e^{-iHt/\hbar}\Psi(0)$, differentiating:

$$
i\hbar\frac{\partial\Psi}{\partial t} = H\Psi.
$$

**This is the Schrödinger equation** — substrate-level structural form derived under V1 + DCGT + P-Norm-Preservation + Stone's theorem.

---

## 4. Connection to Measurement (Paper_005)

Unitary evolution covers **pre-measurement substrate-level dynamics**. At commitment events (Paper_005), unitary evolution is **interrupted** by the P11 commitment:

- Between commit events: $\Psi(t) = U(t - t_{\mathrm{last commit}})\Psi(t_{\mathrm{last commit}})$ — unitary.
- At commit event: $\Psi \to |K^*\rangle$ — projective measurement (Paper_005); **non-unitary**, irreversible.

The substrate-level dynamics is **unitary + commitment**, alternating. Standard QM measurement-process picture.

---

## 5. Falsification Criteria

### 5.1 Norm violation in pre-measurement dynamics

**Falsifier sentence:** *Empirical observation that the substrate-amplitude norm is not preserved during pre-measurement substrate-level dynamics — i.e., $\sum_K |P_K|^2$ changes in the absence of commitment events — would falsify P-Norm-Preservation.*

### 5.2 Non-Hermitian Hamiltonian

**Falsifier sentence:** *Empirical demonstration that a system's pre-measurement evolution is non-unitary in a way not attributable to commitment events — and not derivable from a Hermitian $H$ — would falsify §3.2 + §3.3.*

### 5.3 Time-translation symmetry breaking

**Falsifier sentence:** *Empirical observation that pre-measurement evolution depends on absolute time (not just time interval) in a regime where P13 is expected to hold — would falsify §3.4.*

### 5.4 V1 → non-diffusion continuum operator

**Falsifier sentence:** *Empirical demonstration that V1 substrate-graph propagation does not coarse-grain to a continuum operator of unitary-evolution form — would falsify §3.1 + Paper_073 V1-DCGT bridge.*

---

## 6. Position Statement

**Unitary evolution** is a downstream structural identification under V1 (Paper_089) + DCGT (Paper_073) + Paper_004 P-Channel-Orthogonality + P-Norm-Preservation. The Schrödinger equation $i\hbar\partial_t\Psi = H\Psi$ emerges with Hermitian $H$ via Stone's theorem on the Cauchy-completed Hilbert space.

**Closes the QM-kin trio:** 003 (Born) + 005 (measurement) + 006 (unitary evolution). Standard QM kinematics fully derived structurally under the paper-specific postulates added across the trio.

What this paper claims:

- Pre-measurement substrate-level dynamics is unitary under P-Norm-Preservation + V1 + DCGT.
- Schrödinger equation form follows via Stone's theorem.
- Specific $H$ is value-layer inherited.

What this paper does *not* claim:

- Specific Hamiltonians not derived.
- Unitary evolution does not cover commitment events (Paper_005).
- P-Norm-Preservation not derivable from canonical 13 alone.

**Series context.** Paper_006 of QM-kin arc.

---

## Appendix

**Cross-references:** Paper_087, Paper_001, Paper_003, Paper_004, Paper_005, Paper_007, Paper_073, Paper_089.

**Glossary:**
- **Unitary evolution.** Norm-preserving complex-linear substrate-level dynamics; $U(t_2 - t_1) = e^{-iHt/\hbar}$.
- **P-Norm-Preservation.** Substrate-level commitment that V1-propagation preserves inner-product norm.
- **Schrödinger equation.** $i\hbar\partial_t\Psi = H\Psi$ — derived form under §3.5.

---

**End of Paper_006.**
