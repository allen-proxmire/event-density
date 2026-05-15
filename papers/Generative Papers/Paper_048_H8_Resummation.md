# Paper 048 — Higher-Order Resummation (H-8) Selecting Scenario C

**Series:** Wave-2 Generative Papers (Black-Hole Arc)
**Status:** Conditional structural derivation given the 13 ED primitives (per Paper_087) + paper-specific postulates declared in §2.
**Companions:** Paper_040 (trans-Planckian resolution), Paper_041 (Planck-mass remnant), Paper_047 (Hawking spectrum), Paper_049 (cosmological PBH relic abundance).

---

## Preamble — What This Paper Does NOT Claim

1. This paper does **not** claim a complete derivation of the Hawking-evaporation series-resummation from substrate primitives; the resummation strategy is FORM-FORCED, the specific coefficients are INHERITED.
2. It does **not** claim that the H-8 designation refers to an 8-loop calculation in standard QFT; "H-8" is the Arc-Hawking memo identifier per the corpus.
3. It does **not** introduce new substrate primitives.
4. "H-8 higher-order resummation" = the substrate-level resummation of all-order corrections to the Hawking emission spectrum as $T_H \to \omega_c = c/\ell_P$ (Paper_040 cutoff).
5. "Scenario C forced" = the resummation result that Scenarios A (complete evaporation) and B (eternal black hole) are dynamically excluded, leaving Scenario C (Planck-mass remnant, Paper_041) as the only consistent endpoint.

---

## Abstract

The higher-order resummation (H-8) of substrate-corrected Hawking emission demonstrates that the leading $(\ell_P/M)^2$ corrections (Paper_040) compound at higher orders in a series whose **resummation produces a finite, non-zero emission rate** truncating at $M \to M_\star \sim \ell_P$ (Paper_041). The resummation series has the structure of a geometric / exponential factor multiplying the standard Stefan-Boltzmann-like rate. The substrate origin of the series: each higher order corresponds to V5-cutoff corrections to the Hawking-mode spectrum, accumulating coherently under DCGT coarse-graining. The structural form of the resummation is FORCED; specific coefficients INHERITED via standard QFT-loop matching. The result selects **Scenario C** by exclusion (A and B dynamically incompatible).

---

## §1 Introduction

The Hawking-evaporation endpoint problem requires understanding the emission rate as $M \to \ell_P$ (Paper_041). Standard semiclassical Hawking calculation (Paper_047) gives $T_H \sim 1/M$ and emission rate $\sim 1/M^2$, predicting complete evaporation (Scenario A). Substrate corrections at $(\ell_P/M)^2$ (Paper_040) are negligible at $M \gg \ell_P$ but compound at $M \to \ell_P$.

This paper supplies the higher-order substrate resummation showing that the corrections force Scenario C (remnant) by dynamically excluding A and B.

---

## §2 Primitive Inputs and Paper-Specific Postulates

### 2.1 Primitives invoked (per Paper_087)

- **P08 (Substrate scale $\ell_{\mathrm{ED}}$)** — Planck length.
- **P10 (Rule-type primitive)** — V5 with cutoff $\omega_c = c/\ell_P$.
- **P11 (Commitment-irreversibility)** — directional evaporation.
- **P13 (Time homogeneity)** — frequency content.

### 2.2 Upstream dependencies

- **I-040:** Trans-Planckian resolution / V5 UV cutoff (Paper_040).
- **I-041:** Planck-mass remnant Scenario C (Paper_041).
- **I-047:** Hawking spectrum $T_H = \kappa/(2\pi)$ (Paper_047).
- **I-073:** DCGT (Paper_073).
- **I-Loop:** Standard QFT-loop resummation machinery (standard math).

### 2.3 Paper-specific postulates

- **P-Resummation-Convergence:** The series of substrate corrections to Hawking emission $(\ell_P/M)^{2n}$ for $n \geq 1$ resumms to a convergent factor at all $M \geq M_\star$.
- **P-Endpoint-Truncation:** The resummed emission rate vanishes at $M \to M_\star$, truncating evaporation at the remnant scale.

---

## §2.5 Load-Bearing Step Audit Table

| # | Step | Label | Notes |
|---|---|---|---|
| 1 | Leading $(\ell_P/M)^2$ correction | I | Paper_040. |
| 2 | Higher-order corrections $(\ell_P/M)^{2n}$, $n \geq 2$ | I | Standard QFT loop expansion (I-Loop). |
| 3 | Series convergence | P-Resummation-Convergence | Postulate. |
| 4 | Resummed factor multiplies standard Hawking rate | D-via-I | Application of I-Loop resummation. |
| 5 | Resummed emission rate vanishes at $M_\star$ | P-Endpoint-Truncation | Postulate. |
| 6 | Scenario A excluded (cannot reach $M=0$) | D-via-I | Application of step 5. |
| 7 | Scenario B excluded (evaporation does proceed for $M > M_\star$) | I | Paper_047. |
| 8 | Scenario C forced | D | By exclusion of A + B. |
| 9 | Numerical resummation coefficients | I | Empirical / loop-matching. |
| 10 | Connection to Paper_041 remnant mass | I | Paper_041. |

---

## §3 The Resummation Structure

### 3.1 The series of substrate corrections

By I-040, the leading substrate correction to the Hawking spectrum at scale $M$ is $(\ell_P/M)^2$. Higher-order corrections at $(\ell_P/M)^{2n}$ for $n \geq 2$ arise from successive loop-level V5-cutoff corrections, analyzable via standard QFT machinery (I-Loop).

The corrected emission rate has the form:
$$\frac{dM}{dt} = -\frac{1}{M^2} \cdot R\!\left(\frac{\ell_P^2}{M^2}\right) ,$$
where $R(x)$ is the resummation factor, $R(0) = 1$ (standard Hawking) and $R(x) \to 0$ as $x \to 1$ (substrate truncation at $M = \ell_P$).

### 3.2 Series convergence

P-Resummation-Convergence asserts that the series for $R(x)$ converges for $x \leq c_\star^{-2}$ (the remnant scale parameter, Paper_041). The convergence is plausible by standard QFT-loop convergence arguments (I-Loop) but is **postulated** at substrate level.

### 3.3 Endpoint truncation

P-Endpoint-Truncation asserts $R(c_\star^{-2}) = 0$: the resummed rate vanishes at the remnant scale. This is the substrate-level expression of the V5 cutoff terminating emission.

### 3.4 Scenarios A and B excluded

- **Scenario A** (complete evaporation): excluded because $dM/dt \to 0$ at $M_\star$. The trajectory cannot continue past $M = M_\star$.
- **Scenario B** (eternal black hole halting at $M \gg M_\star$): excluded because $R \to 1$ for $M \gg \ell_P$, recovering standard Hawking evaporation.

Therefore **Scenario C is FORCED** (D, by exclusion).

---

## §4 What This Paper Supplies and Does Not Supply

**Supplies:** Substrate-level resummation structure. Selection of Scenario C by exclusion of A + B. Form of resummed emission rate $dM/dt \sim -R(\ell_P^2/M^2)/M^2$.

**Does not supply:** Specific functional form of $R(x)$ from first principles (INHERITED via loop-matching). Quantitative time-evolution profile $M(t)$.

---

## §5 Falsification Criteria

- **F1:** Empirical detection of complete black-hole evaporation — refutes Scenario C and falsifies the resummation.
- **F2:** Substrate evidence that the correction series $(\ell_P/M)^{2n}$ does NOT converge — refutes P-Resummation-Convergence.
- **F3:** Substrate evidence that $R(c_\star^{-2}) \ne 0$ — refutes P-Endpoint-Truncation.
- **F4:** Empirical evidence of black-hole evaporation halting at $M \gg \ell_P$ — would force Scenario B and refute the substrate cutoff structure.

---

## §6 Position Statement

Higher-order substrate-correction resummation of Hawking emission rate **forces Scenario C** (Planck-mass remnant, Paper_041) by exclusion of A and B. Resummation structure FORCED via Paper_040 leading correction + P-Resummation-Convergence + P-Endpoint-Truncation. Numerical coefficients INHERITED.

---

**End Paper 048 (FIXED).**
