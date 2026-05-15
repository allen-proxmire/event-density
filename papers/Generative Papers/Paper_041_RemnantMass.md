# Paper 041 — Planck-Mass Remnant $M_\star = c_\star \ell_P$ (Scenario C Forced)

**Series:** Wave-2 Generative Papers (Black-Hole Arc)
**Status:** Conditional structural derivation given the 13 ED primitives (per Paper_087) + paper-specific postulates declared in §2.
**Companions:** Paper_039 (horizon as decoupling surface), Paper_047 (Hawking spectrum), Paper_048 (higher-order resummation), Paper_049 (cosmological PBH relic abundance).

---

## Preamble — What This Paper Does NOT Claim

1. This paper does **not** claim that Planck-mass remnants are a dark-matter candidate; per the ED program's substrate-gravity walkthrough, galactic dynamics are explained without DM (Papers_027–034). Remnants are a separate structural relic-matter component of the cosmic energy budget.
2. It does **not** claim a derivation of the numerical prefactor $c_\star$ in $M_\star = c_\star \ell_P$; $c_\star \sim O(1)$ is INHERITED via matching to Paper_048's higher-order resummation.
3. It does **not** claim that remnants are stable on cosmological timescales; stability is conditional on V5-cutoff persistence.
4. It does **not** introduce new substrate primitives.
5. "Scenario C" refers to the three Hawking evaporation endpoint scenarios identified in Paper_048: (A) complete evaporation, (B) eternal black hole, (C) stable Planck-mass remnant. Paper_048 shows higher-order corrections force Scenario C.
6. "Scenario C forced" means: under H-8 higher-order resummation (Paper_048), Scenarios A and B are dynamically excluded; Scenario C is the only consistent endpoint.

---

## Abstract

The Planck-mass remnant $M_\star = c_\star \ell_P$ (in Planck units) emerges as the FORCED Scenario C endpoint of Hawking evaporation under substrate-level higher-order resummation (Paper_048). Scenario A (complete evaporation) is dynamically excluded because the Hawking temperature $T_H \to c/(c_\star \ell_P)$ approaches the V5 cutoff $\omega_c = c/\ell_P$ at $M \to M_\star$ (Paper_040), causing the evaporation rate to vanish. Scenario B (eternal black hole) is excluded because evaporation does proceed for $M > M_\star$. The numerical prefactor $c_\star \sim O(1)$ is INHERITED via standard resummation-coefficient matching. Remnants are a structural relic-matter component, **not a DM candidate** (galactic dynamics are explained by substrate-gravity Papers_027–034).

---

## §1 Introduction

The endpoint of Hawking evaporation is a long-standing open question. Three scenarios:
- **A.** Complete evaporation: $M \to 0$.
- **B.** Eternal black hole: evaporation halts at finite mass.
- **C.** Planck-mass remnant: stable endpoint at $M_\star \sim \ell_P$.

Paper_048 (higher-order resummation) shows that under V5-cutoff substrate dynamics, Scenarios A and B are excluded; Scenario C is **FORCED**. This paper supplies the substrate audit of the remnant mass scale.

---

## §2 Primitive Inputs and Paper-Specific Postulates

### 2.1 Primitives invoked (per Paper_087)

- **P08 (Substrate scale $\ell_{\mathrm{ED}}$)** — supplies $\ell_P$.
- **P10 (Rule-type primitive)** — supplies V5 with cutoff $\omega_c = c/\ell_P$.
- **P11 (Commitment-irreversibility)** — directional evaporation.
- **P13 (Time homogeneity)** — substrate-frequency definition.

### 2.2 Upstream dependencies

- **I-039:** Horizon as decoupling surface (Paper_039).
- **I-040:** Trans-Planckian resolution via V5 cutoff (Paper_040).
- **I-047:** Hawking spectrum $T_H = \kappa/(2\pi)$ (Paper_047).
- **I-048:** Higher-order resummation selecting Scenario C (Paper_048).
- **I-Schwarz:** Standard Schwarzschild thermodynamics (standard math).

### 2.3 Paper-specific postulates

- **P-Cutoff-Saturation-Endpoint:** When the Hawking temperature $T_H$ approaches the V5 cutoff $\omega_c$, the evaporation rate vanishes at the substrate level: $T_H \to \omega_c \Rightarrow dM/dt \to 0$.
- **P-Remnant-Stability:** The remnant at $M_\star$ is stable against further evaporation under V5-cutoff dynamics.

---

## §2.5 Load-Bearing Step Audit Table

| # | Step | Label | Notes |
|---|---|---|---|
| 1 | Hawking temperature $T_H = c^3/(8\pi G M)$ (Planck units: $T_H \sim 1/M$) | I | Paper_047. |
| 2 | V5 UV cutoff $\omega_c = c/\ell_P$ | I | Paper_040. |
| 3 | Standard Schwarzschild evaporation rate $dM/dt \sim -1/M^2$ | I | Standard math (I-Schwarz). |
| 4 | $T_H \to \omega_c$ as $M \to \ell_P$ | D-via-I | Composition of steps 1, 2. |
| 5 | Evaporation rate vanishes when $T_H \to \omega_c$ | P-Cutoff-Saturation-Endpoint | Postulate. |
| 6 | Scenario A excluded: $M$ cannot reach 0 because $dM/dt \to 0$ at $M_\star$ | D-via-I | Application of step 5. |
| 7 | Scenario B excluded: $dM/dt \ne 0$ for $M \gg M_\star$ | I | Standard Hawking evaporation. |
| 8 | Scenario C forced | I | Paper_048 H-8 resummation. |
| 9 | Remnant mass $M_\star = c_\star \ell_P$ | D-via-I | Composition + matching. |
| 10 | Numerical prefactor $c_\star \sim O(1)$ | I | Empirical / resummation matching. |
| 11 | Remnant stability | P-Remnant-Stability | Postulate. |
| 12 | Galactic-dynamics role (DM candidate?) | A→position (**NOT a DM candidate**) | Per ED's substrate-gravity walkthrough. |

---

## §3 The Remnant Mass Scale

### 3.1 Hawking temperature reaching V5 cutoff

For a Schwarzschild black hole, $T_H \sim 1/M$ in Planck units. At $M \sim \ell_P$, $T_H \sim 1/\ell_P \sim \omega_c$.

### 3.2 Evaporation rate vanishing at the cutoff

By P-Cutoff-Saturation-Endpoint: when $T_H \to \omega_c$, the Hawking-mode content reaches the V5 substrate-bandwidth limit. Substrate modes above $\omega_c$ are not supported (Paper_040); the emission spectrum truncates. Standard Stefan-Boltzmann-like $dM/dt \sim -T^4$ structure (I) is multiplied by a V5-cutoff suppression factor that vanishes as $T_H \to \omega_c$.

Therefore $dM/dt \to 0$ at $M \to M_\star \sim \ell_P$.

### 3.3 Scenarios A and B excluded

- **Scenario A** (complete evaporation $M \to 0$): excluded because $dM/dt \to 0$ at $M_\star$, the trajectory cannot continue to $M = 0$.
- **Scenario B** (eternal black hole, evaporation halts at $M \gg M_\star$): excluded because standard Hawking evaporation $dM/dt \ne 0$ for $M \gg \ell_P$ (substrate UV cutoff irrelevant at low temperature).

By exclusion: **Scenario C is FORCED**.

### 3.4 Numerical prefactor $c_\star$

The exact value of $c_\star$ in $M_\star = c_\star \ell_P$ requires Paper_048's higher-order resummation. The substrate program does not derive $c_\star$ at first principles; **$c_\star \sim O(1)$ is INHERITED**.

---

## §4 The Critical Framing: Remnants Are Not Dark Matter

This is a **load-bearing framing statement** for the ED program: Planck-mass remnants are **NOT** the ED dark-matter candidate. Reasons:

- **ED's substrate-gravity walkthrough** (Papers_027–034 + galactic-dynamics walkthrough) explains galactic dynamics **without DM**.
- Remnants are a **structural relic-matter component** of the cosmic energy budget (Paper_049), distinct from any DM-class object.
- Confusion between "remnants" and "DM-via-remnants" is a common interpretive error; this paper marks the distinction.

This is **A→position** (framing claim).

---

## §5 Falsification Criteria

- **F1:** Empirical detection of complete black-hole evaporation ($M \to 0$ endpoint) — refutes Scenario C and P-Cutoff-Saturation-Endpoint.
- **F2:** Empirical detection of eternal black-hole endpoint without remnant — refutes Scenario C in favor of B; refutes substrate program.
- **F3:** Detection of remnant mass scale $\ne O(\ell_P)$ — refutes $M_\star = c_\star \ell_P$.
- **F4:** Empirical evidence that galactic dynamics require Planck-mass remnants as DM — refutes the substrate-gravity walkthrough (Papers_027–034) and would force a reframing.

---

## §6 Position Statement

Planck-mass remnant $M_\star = c_\star \ell_P$ with $c_\star \sim O(1)$ is the **FORCED Scenario C endpoint** of Hawking evaporation under substrate dynamics. P-Cutoff-Saturation-Endpoint + P-Remnant-Stability + higher-order resummation (Paper_048) jointly force the result. Numerical prefactor INHERITED.

**Remnants are NOT a DM candidate**; they are a structural relic-matter component of the cosmic energy budget. Galactic dynamics are explained by substrate-gravity (Papers_027–034) without DM.

---

**End Paper 041 (FIXED).**
