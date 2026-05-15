# Paper 021 — Yang–Mills Mass Gap: A Substrate-Level Mechanism (YM-4) — FIXED

**Series:** Wave-2 Generative Papers (Yang–Mills Arc, YM-4)
**Status:** Conditional structural derivation given the 13 ED primitives (per Paper_087 canonical enumeration) + paper-specific postulates declared in §2.

**FIXED notes (2026-05-13):**
- Primitive enumeration aligned with Paper_087 canonical list.
- §3.3 sketch explicitly flags Perron–Frobenius and Glimm–Jaffe-style coercivity as I (standard math / standard constructive QFT); the substrate adaptation is the new content.
- §2.5 audit row added for standard-math machinery used in §3.3.
- Template "Flexibility & Correction Block" deleted; revision triggers folded into Open Questions.

---

## Preamble — What This Paper Does NOT Claim

1. This paper does **not** claim a constructive proof of the Clay Yang–Mills mass-gap problem.
2. It does **not** claim to compute the numerical value of the mass gap $\Delta$ from first principles.
3. It does **not** claim that the substrate mechanism is the unique route to a mass gap in non-Abelian gauge theory.
4. It does **not** claim that the continuum-limit gap survives in the strict $a \to 0$ limit without the conditional rescaling identified in §5.
5. It does **not** claim asymptotic freedom, confinement, or glueball spectrum results as derived.
6. It does **not** claim to bypass the OS-positivity audit of Paper_020; that audit is inherited.
7. It does **not** introduce new substrate primitives.
8. "Mass gap" here denotes a strictly positive lower bound on the spectrum of the substrate transfer operator above the vacuum, after the continuum identification of Paper_019.

---

## Abstract

We provide a substrate-level mechanism for a positive spectral gap above the vacuum in the continuum-limit YM theory of Paper_019. The mechanism composes three closed-arc ingredients: V1 finite second moment (Paper_089), V5 cross-chain bandwidth (Paper_090), non-Abelian rule-type quartic (Paper_016). The structural **form** $\Delta \propto 1/\ell_*$ is FORCED given the declared postulates. The **coefficient** is INHERITED via the standard-math machinery (Perron–Frobenius, Glimm–Jaffe coercivity) adapted to the substrate transfer operator. Survival in the continuum limit is conditional on P-Profile-Rescaling.

---

## §1 Introduction

The Clay YM problem requires (a) existence and (b) mass gap. Paper_019 supplies the construction; Paper_020 audits OS-positivity; this paper addresses (b) at the structural-mechanism level.

The mechanism is **not** a borrowed lattice argument. It is a substrate-internal claim: V1 finite width + V5 cross-chain bandwidth set an intrinsic correlation-length floor; non-Abelian quartic prevents this floor from diverging under coarse-graining.

---

## §2 Primitive Inputs and Paper-Specific Postulates

### 2.1 Primitives invoked (per Paper_087 canonical enumeration)

- **P02 (Participation)** — substrate field content.
- **P07 (Channel structure)** — gauge-rule-type bundle.
- **P08 (Substrate scale $\ell_{\mathrm{ED}}$)** — UV cutoff.
- **P09 (U(1) polarity, extended non-Abelian via P10)** — gauge group fiber.
- **P10 (Rule-type primitive)** — supplies V1, V5 as kernel rule-types (Papers_089/090) + non-Abelian composition (Paper_016).
- **P11 (Commitment-irreversibility)** — fixes V1 retarded.

### 2.2 Inherited closed-arc results

- **I-V1:** V1 kernel has finite second moment $\ell_{V1}^2$ (Paper_089).
- **I-V5:** V5 cross-chain kernel has finite bandwidth $\ell_{V5}$ (Paper_090).
- **I-T17:** Gauge fields = connections on rule-type bundles (Paper_015).
- **I-NonAb:** Non-Abelian rule-type composition produces irreducible quartic self-coupling (Paper_016 + Paper_018).
- **I-Cont:** Continuum YM action at leading order (Paper_019).
- **I-OS:** OS-positivity conditional-positive (Paper_020).
- **I-PF:** Perron–Frobenius spectral theory (standard math).
- **I-GJ:** Glimm–Jaffe-style coercivity machinery (standard constructive QFT).

### 2.3 Paper-specific postulates

- **P-Gap-Coercivity:** The substrate effective action $S_{\mathrm{eff}}[A]$ satisfies a coercivity bound $S_{\mathrm{eff}}[A] \geq c_1 \|A\|_{H^1}^2 - c_2 \|A\|_{L^2}^2$ on the gauge-fixed slice.
- **P-Profile-Rescaling:** Under continuum limit $a \to 0$, V1 and V5 profiles rescale so $\ell_{V1}/a$ and $\ell_{V5}/a$ remain bounded above and below by positive constants.
- **P-Quartic-Sign:** Induced quartic coefficient $\lambda_4$ in $S_{\mathrm{eff}}$ is strictly positive at the matching scale.

---

## §2.5 Load-Bearing Step Audit Table

| # | Step | Label | Notes |
|---|---|---|---|
| 1 | V1 finite second moment $\ell_{V1}^2$ | I | Paper_089. |
| 2 | V5 finite bandwidth $\ell_{V5}$ | I | Paper_090. |
| 3 | Non-Abelian quartic $g^2[A,A]^2$ present | I | Paper_016 + Paper_018. |
| 4 | Continuum YM action at leading order | I | Paper_019. |
| 5 | OS positivity (conditional) | I | Paper_020. |
| 6 | Coercivity of $S_{\mathrm{eff}}$ on gauge-fixed slice | P-Gap-Coercivity | Postulate. |
| 7 | Kernel-profile rescaling | P-Profile-Rescaling | Postulate. |
| 8 | Sign of induced quartic | P-Quartic-Sign | Postulate. |
| 9 | Perron–Frobenius applied to $\mathcal{T}$ on $\mathcal{H}_{\mathrm{OS}}$ | I | Standard math (I-PF). |
| 10 | Glimm–Jaffe-style coercivity argument | I | Standard constructive QFT (I-GJ). |
| 11 | Substrate adaptation of standard machinery to V1/V5 + rule-type bundle | D | The new content of this paper. |
| 12 | Correlation-length floor $\ell_* \leq C \max(\ell_{V1}, \ell_{V5}, \lambda_4^{-1/2} g^{-1})$ | D | From substrate adaptation of I-GJ given P-Gap-Coercivity. |
| 13 | Spectral gap $\Delta \geq c/\ell_*$ | D (form) / I (coefficient) | Form from substrate adaptation of I-PF; coefficient inherited from matching. |
| 14 | Survival of $\Delta > 0$ as $a \to 0$ | D — conditional on P-Profile-Rescaling | Conditional. |
| 15 | Numerical value of $\Delta$ for specific $G$ | OPEN | Not claimed. |

The strengthened D-row rereading: Perron–Frobenius and Glimm–Jaffe-style coercivity are explicit I-rows (standard math/QFT). The new content is **the substrate adaptation** of these machineries to the V1/V5 + rule-type-bundle context (step 11).

---

## §3 The Mechanism

### 3.1 The substrate transfer operator

From Paper_018 §4, the coarse-grained substrate dynamics admit a transfer operator $\mathcal{T}$ on the rule-type bundle. By I-OS, $\mathcal{T}$ is self-adjoint and positive on $\mathcal{H}_{\mathrm{OS}}$.

### 3.2 The three substrate ingredients

**(A) V1 finite width as UV regulator.** Kinetic term inherits momentum-space form factor $\hat{K}_{V1}(p)$ decaying for $|p|\ell_{V1} \gtrsim 1$.

**(B) V5 cross-chain bandwidth as coherence cutoff.** Cross-channel damping in the propagator beyond $\ell_{V5}$.

**(C) Non-Abelian quartic as mass-generating.** With P-Quartic-Sign, $\lambda_4 (A^a A_a)^2$ lifts would-be massless modes via the standard coercive-quartic mechanism.

### 3.3 The correlation-length floor (with explicit standard-math acknowledgment)

**Claim (D for substrate adaptation; I for underlying standard math):**

Given (A)+(B)+(C) and P-Gap-Coercivity, there exists a finite correlation length
$$\ell_* \leq C \cdot \max(\ell_{V1}, \ell_{V5}, \lambda_4^{-1/2} g^{-1}) .$$

**Sketch.** The argument applies **Glimm–Jaffe-style coercivity (I-GJ, standard constructive QFT)** combined with **Perron–Frobenius (I-PF, standard math)** structure of $\mathcal{T}$ on $\mathcal{H}_{\mathrm{OS}}$, yielding exponential clustering of gauge-invariant two-point functions.

The **standard machinery** is I. The **substrate adaptation** — applying I-GJ and I-PF to the V1/V5 + rule-type-bundle transfer operator — is the new content (D).

### 3.4 The spectral gap

**Form** $\Delta \propto 1/\ell_*$ via Perron–Frobenius spectral-radius/Perron–Frobenius relation on $\mathcal{H}_{\mathrm{OS}}$ — substrate adaptation of I-PF.

**Coefficient** $c$ and group-dependent prefactor INHERITED from the matching condition of Paper_019.

---

## §4 Why This Is Not a Borrowed Argument

Three features distinguish the substrate mechanism from a rebadged lattice argument:

1. **Intrinsic length scales.** $\ell_{V1}$, $\ell_{V5}$ are kernel moments fixed by P10/P11 at substrate level (Papers_089–090), not lattice spacings.
2. **Quartic origin.** $\lambda_4 > 0$ traces to non-Abelian rule-type composition (Paper_016), not chosen lattice action.
3. **Continuum-limit conditional.** The continuum-limit problem is exposed as P-Profile-Rescaling rather than hidden.

The standard mathematical machinery (Perron–Frobenius, Glimm–Jaffe coercivity) is the **inherited tool**; the **substrate adaptation** is the new content.

---

## §5 The Continuum-Limit Conditional (Stall-Risk Locus)

Three failure modes:

- **Mode 1:** $\ell_{V1}/a \to 0$ — UV regulator collapses.
- **Mode 2:** $\ell_{V5}/a \to \infty$ — cross-chain coherence dominates.
- **Mode 3:** $\lambda_4 \to 0$ under matching — quartic stabilization fails.

P-Profile-Rescaling asserts none triggers. **Declared**, not derived.

---

## §6 Open Structural Questions

- **O-MG-1:** Constructive proof of P-Gap-Coercivity from substrate kernel data.
- **O-MG-2:** Derivation of $\lambda_4 > 0$ from compact-simple-$G$ group-theoretic structure.
- **O-MG-3:** Asymptotic freedom — substrate matching reproduces running $g(\mu)$?
- **O-MG-4:** Confinement — Wilson-loop area law from V1/V5 cross-correlation?
- **O-MG-5:** Glueball spectrum $\Delta_n / \Delta_1$.
- **O-MG-6:** Whether P-Profile-Rescaling can be replaced by a derived rescaling.

**Revision triggers (folded in from former §9):**
- If P-Gap-Coercivity is derived, §3.3 strengthens to D-only.
- If P-Profile-Rescaling is derived, §5 strengthens and continuum-limit conditional becomes unconditional.
- If P-Quartic-Sign is derived from group theory (O-MG-2), §3.2(C) strengthens.

---

## §7 Falsification Criteria

- **F1:** V1 with divergent second moment under any admissible substrate variation — invalidates I-V1.
- **F2:** V5 cross-chain bandwidth unbounded — invalidates I-V5.
- **F3:** Non-Abelian rule-type composition does **not** produce coercive quartic — invalidates I-NonAb / P-Quartic-Sign.
- **F4:** P-Gap-Coercivity fails for explicit $S_{\mathrm{eff}}$ from Paper_019 matching — invalidates mechanism's central step.
- **F5:** No choice of kernel-profile rescaling avoids all three failure modes — refutes P-Profile-Rescaling.

---

## §8 Position Statement

Substrate-level structural mechanism for YM mass gap at **conditional-positive level**. Form $\Delta \propto 1/\ell_*$ FORCED given declared postulates. Numerical value INHERITED via matching. Survival in continuum limit conditional on P-Profile-Rescaling.

**Not a constructive proof** of the Clay problem. Positive structural verdict parallel to Paper_020's OS-positivity audit. Papers 019/020/021 close the YM-arc's Clay-relevance program at the structural-positive level.

---

## Appendix — Relation to Standard YM Mass-Gap Approaches

| Standard approach ingredient | Substrate origin |
|---|---|
| Lattice spacing $a$ as UV regulator | $\ell_{V1}$ from V1 finite width (Paper_089) |
| Site decoupling at long distance | $\ell_{V5}$ V5 cross-chain bandwidth (Paper_090) |
| Plaquette action quartic | Non-Abelian rule-type quartic (Paper_016) |
| Reflection positivity | OS-positivity audit (Paper_020) |
| Continuum limit | Profile rescaling (P-Profile-Rescaling, declared) |
| Perron–Frobenius spectral theory | I-PF (same standard math) |
| Glimm–Jaffe coercivity | I-GJ (same standard constructive QFT machinery) |

**Structural correspondence**, not derivation of one from the other. Substrate program's predictive content matches standard mechanism at leading order; honest framing that the continuum-limit step is a declared postulate.

---

**End Paper 021 (FIXED).**
