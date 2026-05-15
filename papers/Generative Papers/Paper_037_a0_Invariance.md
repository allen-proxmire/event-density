# Paper 037 — $a_0$ Continuum-Limit Invariance

**Series:** Wave-2 Generative Papers (Gravity Arc)
**Status:** Conditional structural derivation given the 13 ED primitives (per Paper_087) + paper-specific postulates declared in §2.
**Companions:** Paper_029 ($a_0 = c H_0/(2\pi)$), Paper_032 (six ED-10 prerequisites), Paper_073 (DCGT), Paper_087 (13 primitives), Paper_088 (primitive load-bearing audit).

---

## Preamble — What This Paper Does NOT Claim

1. This paper does **not** claim derivation of $H_0$ from substrate primitives; $H_0$ is INHERITED as the substrate-level cosmological-rate parameter.
2. It does **not** claim that $a_0$'s invariance is empirically distinguishable from a coincidence; the invariance is at the structural level.
3. It does **not** claim that all coarse-graining limits preserve $a_0$; only the **substrate-consistent** continuum limit under DCGT preserves it.
4. It does **not** introduce new substrate primitives.
5. "Continuum-limit invariance" means: $a_0$ as defined by $c H_0 / (2\pi)$ (Paper_029) is **not** rescaled by substrate→continuum coarse-graining; substrate-level $c$ and cosmological-level $H_0$ are individually preserved, and their product is the same in substrate and coarse-grained descriptions.

---

## Abstract

The transition acceleration $a_0 = c H_0/(2\pi)$ (Paper_029) is **continuum-limit invariant**: substrate-level $c$ is invariant under DCGT coarse-graining (P-Substrate-c-Constancy, Paper_012), and $H_0$ is a cosmological-rate parameter not subject to local coarse-graining rescaling (P-H0-Cosmological-Invariant). Therefore $a_0$ is unchanged under continuum limit. This is structurally important because it distinguishes $a_0$ from quantities that **do** rescale under coarse-graining (e.g., the mass-gap scale in Paper_021 under P-Profile-Rescaling), supplying the substrate-consistency anchor for the deep-MOND regime (Paper_034).

---

## §1 Introduction

In the substrate-gravity arc, several quantities are derived at substrate level: Newton's $G$ (Paper_027), transition acceleration $a_0$ (Paper_029), ED Combination Rule (Paper_030), BTFR slope-4 (Paper_031). For the continuum predictions to match the substrate-level forms without rescaling, the constituent quantities must be invariant under continuum limit.

This paper supplies the substrate audit of $a_0$'s continuum-limit invariance. The result contrasts with Paper_021's mass-gap scale, which requires explicit P-Profile-Rescaling for continuum-limit survival.

---

## §2 Primitive Inputs and Paper-Specific Postulates

### 2.1 Primitives invoked (per Paper_087)

- **P08 (Substrate scale $\ell_{\mathrm{ED}}$)** — supplies $\ell_P$ entering $G$ and indirectly $a_0$.
- **P10 (Rule-type primitive)** — supplies V1 kernel (substrate-$c$).
- **P11 (Commitment-irreversibility)** — supplies the directional structure.
- **P13 (Time homogeneity)** — supplies $H_0$ as cosmological-rate parameter.

### 2.2 Upstream dependencies

- **I-029:** $a_0 = c H_0/(2\pi)$ (Paper_029).
- **I-032:** Six ED-10 prerequisites for substrate-gravity continuum limit (Paper_032).
- **I-073:** DCGT (Paper_073).
- **I-012:** P-RB-1 / P-Substrate-c-Constancy (Paper_012).
- **I-RG:** Standard renormalization-group machinery (standard math).

### 2.3 Paper-specific postulates

- **P-H0-Cosmological-Invariant:** $H_0$ is a cosmological-rate parameter that is **not** subject to local coarse-graining rescaling; it is a global substrate-level quantity inherited from cosmological boundary conditions.
- **P-$a_0$-Invariance:** $a_0 = c H_0/(2\pi)$ is invariant under DCGT continuum coarse-graining, by virtue of P-Substrate-c-Constancy (Paper_012) and P-H0-Cosmological-Invariant.

---

## §2.5 Load-Bearing Step Audit Table

| # | Step | Label | Notes |
|---|---|---|---|
| 1 | $a_0 = c H_0/(2\pi)$ | I | Paper_029. |
| 2 | Substrate-$c$ constancy under coarse-graining | I | P-Substrate-c-Constancy (Paper_012). |
| 3 | $H_0$ cosmological-invariant | P-H0-Cosmological-Invariant | Postulate. |
| 4 | DCGT coarse-graining does not rescale $c$ | I | Paper_073 + Paper_012. |
| 5 | DCGT coarse-graining does not rescale $H_0$ | D-via-I | Application of P-H0-Cosmological-Invariant + Paper_073 (local coarse-graining does not act on global cosmological scale). |
| 6 | $a_0$ continuum-limit invariance | D | Composition of steps 4 + 5. |
| 7 | Distinguishes $a_0$ from mass-gap-scale rescaling | A→position | Comparative observation re Paper_021. |
| 8 | Empirical-test admissibility (RG-running of $a_0$) | I | Standard math; $a_0$ does not run with energy under substrate-consistent RG. |

---

## §3 The Invariance Argument

### 3.1 Substrate $c$ is invariant under coarse-graining

By Paper_012 P-Substrate-c-Constancy, the substrate $c$ is invariant under all admissible coarse-graining variations. DCGT (Paper_073) is admissible; therefore $c$ does not rescale under continuum limit.

### 3.2 $H_0$ is cosmological-invariant

P-H0-Cosmological-Invariant: $H_0$ is a global cosmological-rate parameter inherited from substrate-cosmological boundary conditions. Local DCGT coarse-graining (operating on the hydrodynamic-window scale $R_{\mathrm{cg}}$) does not act on the global cosmological scale; therefore $H_0$ is unchanged.

The substrate-consistency justification: the cosmological decoupling surface (Paper_028) is at $R_H = c/H_0$, far larger than any local coarse-graining scale; $H_0$ is a boundary condition, not a substrate field subject to local renormalization.

### 3.3 Composing: $a_0$ invariance

$a_0 = c H_0/(2\pi)$. By §3.1, $c$ unchanged. By §3.2, $H_0$ unchanged. Therefore $a_0$ unchanged.

### 3.4 Contrast with mass-gap rescaling

Paper_021's mass-gap scale requires explicit P-Profile-Rescaling for continuum-limit survival because the relevant V1/V5 widths are **local** substrate scales subject to coarse-graining rescaling. $a_0$ is structurally different: it composes a substrate-$c$ (invariant under P-Substrate-c-Constancy) and a cosmological $H_0$ (invariant under P-H0-Cosmological-Invariant). Neither factor requires rescaling.

This is the load-bearing structural distinction (A→position).

---

## §4 Distinguishing Structural vs Empirical Content

- **Structural (P + D):** $a_0$ invariance composition argument; substrate-$c$ + cosmological-$H_0$ separability.
- **Inherited (I):** Numerical values $c \approx 3 \times 10^{10}$ cm/s, $H_0 \approx 70$ km/s/Mpc, $a_0 \approx 1.2 \times 10^{-8}$ cm/s².
- **Postulated (P):** P-H0-Cosmological-Invariant.

The substrate program **does not derive** $H_0$; the invariance argument is conditional on $H_0$ being a cosmological boundary condition.

---

## §5 Falsification Criteria

- **F1:** Empirical detection of $a_0$ running with energy scale (RG-running) — would refute the substrate-consistency anchor.
- **F2:** Empirical evidence that $H_0$ varies on local coarse-graining scales — refutes P-H0-Cosmological-Invariant.
- **F3:** Empirical detection of substrate-$c$ variation (would propagate from Paper_012 falsification).
- **F4:** Substrate evidence that $a_0$ is rescaled under continuum-limit despite invariant factors — would refute the composition argument.

---

## §6 Position Statement

$a_0$ is **continuum-limit invariant** by composition of substrate-$c$ constancy (Paper_012) and cosmological $H_0$ invariance (P-H0-Cosmological-Invariant). This distinguishes $a_0$ from the mass-gap scale of Paper_021, which requires explicit profile rescaling. The invariance is the substrate-consistency anchor for the deep-MOND regime (Paper_034) and the flat-background field equation (Paper_036).

---

**End Paper 037 (FIXED).**
