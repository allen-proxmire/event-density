# NS-Q3 — P7 Amplitude-Ratio Interpretation of Q ≈ 3.5

**Date:** 2026-04-30
**Status:** NS-Q3 of the Q-Factor arc. **Headline: H3(P7) fails. P7's 3–6% amplitude ratio and Q-factor's $1/(2Q) \approx 14\%$ damping ratio differ numerically by 2.4–4.8× and correspond to physically different mechanisms (nonlinear harmonic generation vs. linear viscous damping). No architectural channel links them. Brief negative result as expected.**
**Companions:** [`NS_Q1_Opening.md`](NS_Q1_Opening.md), [`NS_Q2_V5_Memory.md`](NS_Q2_V5_Memory.md), [`../../Architectural_Canon.md`](../../Architectural_Canon.md) §2 (P7).

---

## 1. Purpose

This memo evaluates H3(P7): whether ED's P7 canonical amplitude ratio (3–6%) has any structural or quantitative connection to the viscous-oscillator Q-factor (Q ≈ 3.5). Per NS-Q1 §5.3 weak-prior assessment, this is expected to be a brief negative-result memo.

---

## 2. Inputs

| Input | Source |
|---|---|
| P7 canonical amplitude ratio: $A_3/A_1$ ≈ 3–6%, weak coupling ~0.03 | [`../../Architectural_Canon.md`](../../Architectural_Canon.md) §2 (P7), [`../../Universal_Invariants.md`](../../Universal_Invariants.md) §3 |
| Oscillator Q-factor: $Q = 1/(2\zeta)$ for underdamped $\zeta < 1$ | Classical mechanics |
| ED canonical Q ≈ 3.5 | [`../../Architectural_Canon.md`](../../Architectural_Canon.md) §3 |
| NS-Q1 hypotheses | [`NS_Q1_Opening.md`](NS_Q1_Opening.md) §6 |
| NS-Q2 V5 result: H2 weak-coincidental | [`NS_Q2_V5_Memory.md`](NS_Q2_V5_Memory.md) §7 |

---

## 3. Step 1 — Observable Class Comparison

**P7 amplitude ratio** $A_3/A_1$ is a **forced harmonic-generation coefficient**: under multiplicative perturbations on a fundamental at $k_1$, the steady-state amplitude at $k_3 = 3k_1$ relative to the fundamental is 3–6%. Mechanism: nonlinear gradient self-coupling $M'(\rho)|\nabla\rho|^2$ generating higher-Fourier harmonics under driving.

**Oscillator Q-factor** $Q = 1/(2\zeta)$ where $\zeta = c/(2m\omega_0)$ is the **linear damping ratio**: ratio of damping coefficient to critical damping. Mechanism: viscous dissipation linearly removing energy from the oscillation per cycle.

**Different observable classes:**

| | P7 amplitude ratio | Q damping ratio |
|---|---|---|
| Mechanism | Nonlinear harmonic generation (cubic in field) | Linear viscous dissipation |
| Observable | Spatial / Fourier-mode amplitude ratio | Energy-decay rate per cycle |
| Dimensional structure | Dimensionless field-amplitude ratio | Dimensionless damping (ratio to critical) |
| Physical setting | Driven nonlinear PDE in steady state | Linear damped harmonic oscillator |
| Generated from | $M'(\rho)|\nabla\rho|^2$ nonlinearity | Linear $-c\dot x$ damping term |

**No direct mapping exists between $A_3/A_1$ and $1/(2Q)$.** They are different quantities measuring different physics, even though both are dimensionless ratios in the few-percent-to-tens-of-percent range.

---

## 4. Step 2 — Numerical Coincidence Check

Compute $1/(2Q)$ for $Q = 3.5$:

$$\zeta = \frac{1}{2Q} = \frac{1}{7} \approx 0.143 = 14.3\%.$$

Compare to P7 amplitude ratio: 3–6%.

**Ratio: $14.3/3 \approx 4.8$ to $14.3/6 \approx 2.4$** — i.e., the damping ratio is **2.4–4.8× larger** than P7's amplitude ratio.

If the comparison were instead between Q and $1/A_3/A_1$:
- $1/A_3 \approx 1/0.04$ (mid-range) ≈ 25
- Q = 3.5

Also no match (factor 7×).

Or comparing $A_3/A_1$ to $1/Q$ directly:
- $1/Q = 1/3.5 \approx 0.286$
- $A_3/A_1 \approx 0.04$ (mid-range)

Factor of ~7× off. No clean numerical coincidence.

**No simple algebraic relation between $A_3/A_1$ and Q gives a quantitative match.** The numerical magnitudes differ by factors of 2–7× depending on which combination is compared.

---

## 5. Step 3 — Architectural Assessment

### 5.1 No mechanism-level link

- P7's amplitude ratio comes from the *nonlinear harmonic-generation channel* of the canonical PDE — a *cubic-in-field* self-coupling driving energy into higher Fourier modes under steady-state forcing.
- Q-damping comes from the *linear viscous channel* — a first-derivative-in-time term removing energy from the oscillation linearly.

These are different channels of the canonical PDE / general dynamics framework. No ED architectural channel links them at primitive level.

### 5.2 No canon-level ratio yields Q ≈ 3.5 from P7 amplitude

The canonical PDE has *both* P7's nonlinear coupling and a linear damping (via the participation channel coefficient $\zeta$). They are separately parameterized. Their canonical values are:
- P7 amplitude ratio: 3–6% (canon §3 universal invariant from canonical-PDE simulation traces).
- Q ≈ 3.5: derived from the participation-channel ODE's underdamped regime at canon-default $\zeta = 1/4$.

These are independent invariants of the canonical PDE — neither derives from the other. The canon does not contain a structural relation $Q = f(A_3/A_1)$ or vice versa. Both are computed properties of the canonical-PDE simulation; their numerical values are independent inputs.

### 5.3 Architectural verdict

| Question | Answer |
|---|---|
| Does P7 architecturally explain Q ≈ 3.5? | **No.** Different channels; different mechanisms. |
| Is there a quantitative correspondence between P7's 3–6% and Q ≈ 3.5? | **No.** Numerical mismatches by factor 2–7× under any direct comparison. |
| Does ED canon link the two ratios structurally? | **No.** Both are independent invariants of the canonical PDE. |

**No architectural correspondence; no quantitative correspondence; no mechanism-level correspondence.**

---

## 6. Provisional Verdict for H3(P7)

**H3(P7) fails.** P7's amplitude ratio does not explain the oscillator Q-factor. The two observables are independent properties of the canonical PDE measuring different physical channels (nonlinear harmonic generation vs. linear viscous damping), and their numerical values do not match in any clean ratio.

This is the expected brief negative result per NS-Q1 §5.3 weak-prior. **Confirms H1 null** as the leading interpretation: ED's canonical Q ≈ 3.5 is an internal canon property without specific empirical fluid-mechanical universal correspondence; the P7 amplitude ratio is a separate canon property that cannot architecturally explain it.

### 6.1 What this rules out

- **P7 → Q derivation chain.** No structural argument exists deriving Q-factor from P7's amplitude-ratio invariant. Both are independent canonical-PDE invariants.
- **A_3/A_1 = 1/(2Q) hypothesis.** Numerical magnitudes differ by factor 2.4–4.8× (canon-level data); not a clean match.
- **P7 forced-response → Q damping mapping.** Mechanism mismatch (nonlinear cubic vs. linear viscous); no architectural channel links them.

### 6.2 What remains for the arc

NS-Q4 (P4 mobility-saturation channel) is the last correspondence channel to evaluate. Per NS-Q1 §5.1 weak-prior, also expected brief negative result. After NS-Q4, NS-Q5 synthesis closes the arc — likely at H1 null with H2 weak-coincidental from NS-Q2.

---

## 7. Recommended Next Steps

1. **NS-Q4 — P4 mobility-saturation interpretation.** File: `theory/Navier Stokes/Q_Factor/NS_Q4_P4_Mobility.md`. Per NS-Q1 §5.1 weak-prior assessment, expected brief negative result. Estimated 0.5 sessions.

2. **NS-Q5 — Final verdict + arc closure.** File: `theory/Navier Stokes/Q_Factor/NS_Q5_Synthesis.md`. Aggregate the three correspondence-channel investigations. Expected outcome: **H1 null verdict** with H2 weak-coincidental (NS-Q2: V5 moderate-damping overlap, not architectural) and H3(P7) and H3(P4) both failing (NS-Q3 + NS-Q4 brief negative results). Arc closes quickly. Estimated 0.5 sessions.

### Decisions for you

- **Confirm H3(P7) negative verdict.** P7's amplitude ratio and Q damping ratio are different observables; no architectural / quantitative / mechanism-level correspondence.
- **Confirm proceeding to NS-Q4 (P4) as final brief-note channel investigation.**
- **Confirm arc-closure expectation at H1 null** (with H2 weak-coincidental from NS-Q2; H3 fails per NS-Q3 + NS-Q4).

---

*NS-Q3 P7 channel evaluated. P7's 3–6% amplitude ratio and Q-factor's $1/(2Q) \approx 14\%$ damping ratio differ numerically by factor 2.4–4.8× and correspond to physically different mechanisms (nonlinear cubic harmonic generation vs. linear viscous damping). Both are independent invariants of the canonical PDE; no canon-level ratio links them. **H3(P7) fails as expected.** Confirms H1 null as leading interpretation. NS-Q4 + NS-Q5 close the arc next.*
