# NS-Q4 — P4 Mobility-Saturation Interpretation of Q ≈ 3.5

**Date:** 2026-04-30
**Status:** NS-Q4 of the Q-Factor arc. **Headline: P4 channel fails to explain Q ≈ 3.5. P4 governs steady-state mobility saturation; Q governs time-dependent oscillation decay. Different dynamical axes; no canonical algebraic relation links β to ζ or Q. Brief negative result as expected. Combined with NS-Q2 (V5 weak-coincidental) and NS-Q3 (P7 fail), the three correspondence channels close — arc verdict at H1 null is now well-supported.**
**Companions:** [`NS_Q1_Opening.md`](NS_Q1_Opening.md), [`NS_Q2_V5_Memory.md`](NS_Q2_V5_Memory.md), [`NS_Q3_P7_Amplitude.md`](NS_Q3_P7_Amplitude.md), [`../P4_NN_Synthesis.md`](../P4_NN_Synthesis.md), [`../../Architectural_Canon.md`](../../Architectural_Canon.md) §2 (P4).

---

## 1. Purpose

This memo evaluates the P4 mobility-saturation channel as a possible explanation for the viscous-oscillator Q ≈ 3.5, with a-priori expectation of a negative result per NS-Q1 §5.1.

P4 governs **equilibrium / instantaneous mobility saturation** — the canonical form $M(\rho) = M_0(1 - \rho/\rho_\mathrm{max})^\beta$ with empirical mean β ≈ 1.72 ± 0.37 across 10 soft-matter systems and canonical β = 2.0 (per [`../P4_NN_Synthesis.md`](../P4_NN_Synthesis.md) and [`../P4_NN_D4_Empirical_Comparison.md`](../P4_NN_D4_Empirical_Comparison.md)). Q-factor governs **time-dependent oscillation decay** — the linear damping ratio $\zeta = c/(2m\omega_0)$ with $Q = 1/(2\zeta)$.

These two architectural objects sit on different dynamical axes — one steady-state structural, one time-dependent linear-decay. The arc's a-priori expectation is that no architectural channel links them.

---

## 2. Inputs

| Input | Source |
|---|---|
| P4 canonical form $M(\rho) = M_0(1 - \rho/\rho_\mathrm{max})^\beta$, canonical β = 2.0 | [`../../Architectural_Canon.md`](../../Architectural_Canon.md) §2 (P4); [`../../PDE.md`](../../PDE.md) §4.1 |
| P4 empirical mean β = 1.72 ± 0.37 across 10 systems (R² > 0.986) | [`../P4_NN_D4_Empirical_Comparison.md`](../P4_NN_D4_Empirical_Comparison.md) §6.1 |
| P4 fluid-mechanical extension: Krieger-Dougherty + DST + Cross | [`../P4_NN_Synthesis.md`](../P4_NN_Synthesis.md) |
| Oscillator Q: $Q = 1/(2\zeta)$ | Classical mechanics |
| NS-Q1 hypotheses + a-priori H1 null | [`NS_Q1_Opening.md`](NS_Q1_Opening.md) |
| NS-Q2 V5 result: H2 weak-coincidental | [`NS_Q2_V5_Memory.md`](NS_Q2_V5_Memory.md) §7 |
| NS-Q3 P7 result: H3(P7) fails | [`NS_Q3_P7_Amplitude.md`](NS_Q3_P7_Amplitude.md) §6 |

---

## 3. Step 1 — Physical Role Comparison

### 3.1 What P4 governs

P4 is a **steady-state structural axiom** of the canonical PDE: it specifies that mobility $M(\rho)$ saturates to zero at a packing-class upper bound $\rho_\mathrm{max}$. This determines:
- *What viscosity is at given density* (Krieger-Dougherty divergence near jamming).
- *How transport coefficients depend on state variables* (concentration, strain rate via P4-NN extensions).
- *Threshold behavior at packing limits* (jamming, DST, shear-thickening).

P4 is a **state-function constraint** — it specifies how the constitutive function $M$ relates to the field $\rho$ at any given time. It is *not* a temporal-dynamics constraint.

### 3.2 What Q governs

Q-factor is a **temporal-decay characterization** of a linear damped oscillator: it specifies how fast oscillation amplitude decays per cycle. It is determined by:
- *Linear viscous damping coefficient $c$* in the equation of motion $m\ddot x + c\dot x + kx = 0$.
- *Mass and spring constants* via $\omega_0 = \sqrt{k/m}$.

Q is a **dynamics-domain quantity** — it characterizes the time-evolution of a linear oscillator.

### 3.3 Different axes of dynamics

| Aspect | P4 | Q |
|---|---|---|
| Domain | State-space / equilibrium constitutive | Time-evolution / linear damping |
| Type | Function form (mobility saturation) | Scalar ratio (energy decay per cycle) |
| Determined by | $\rho_\mathrm{max}$, β | $c, m, \omega_0$ |
| Time-dependence | None at canonical level (steady-state) | Central role |

P4 and Q live on **different axes of the dynamics framework**. The canonical PDE has *both* mobility-saturation structure (P4) *and* damping/oscillation structure (P5–P6 participation channel, where Q ≈ 3.5 emerges); these are independent canon principles.

---

## 4. Step 2 — Structural Link Check

Three concrete questions to test for a P4↔Q architectural link:

### 4.1 Does P4 fix any ratio of storage vs. loss per oscillation cycle?

**No.** P4 specifies $M(\rho_\mathrm{max}) = 0$ — the mobility-saturation structural fact. It does not specify any time-evolution ratio. Storage (elastic) vs. loss (dissipative) ratios are determined by the linear-damping coefficient, not by P4.

In the P4-NN arc's Maxwell-viscoelastic extension via V5 (D5 of P4-NN; see also NS-Q2), the storage/loss ratio is set by $\omega_0\tau_R$, with $\tau_R$ being a V5 quantity (INHERITED). P4 itself does not enter this ratio.

### 4.2 Does β = 2.0 or any P4 exponent enter a Q-like expression?

**No canonical relation exists.** β appears in:
- Mobility law: $M(\rho) = M_0(1 - \rho/\rho_\mathrm{max})^\beta$.
- Krieger-Dougherty viscosity: $\mu(\rho) = \mu_0(1 - \rho/\rho_\mathrm{max})^{-\beta}$ (D1 of P4-NN).
- DST divergence: $\mu(\dot\gamma) \propto (1 - \dot\gamma/\dot\gamma_\mathrm{max})^{-\beta}$ (D2 of P4-NN §4.1).

None of these involve Q-factor or damping ratio. β is a state-function exponent; Q is a time-domain dynamic ratio.

### 4.3 Does any known P4 result constrain ζ or Q?

**Indirectly via effective viscosity.** P4 affects $\mu(\rho)$ at given density; for a damped oscillator embedded in a P4-class fluid, the damping coefficient $c$ depends on $\mu$, and hence ζ depends on $\mu(\rho)$. So ζ varies with density via P4.

**But:** this is *embedding-specific*, not architectural. The relation between Q and β depends on the specific oscillator setup — what density of fluid the oscillator is in, what frequency $\omega_0$ it operates at, what geometry. **P4 does not fix any universal Q value;** it just changes the local viscosity that goes into the standard ζ formula.

For Q to be 3.5 specifically, we'd need ζ = 0.143, which corresponds to a specific damping coefficient $c$, which depends on the specific fluid's $\mu$ at the specific density / shear rate. P4's β value does not force this.

---

## 5. Step 3 — Numerical Check

Canonical numerical values:
- P4 canonical β = 2.0 (or empirical mean β = 1.72 ± 0.37 from UDM).
- Q ≈ 3.5 → ζ = 1/(2 · 3.5) = 1/7 ≈ 0.143 (14.3%).

**No simple algebraic relation $f(\beta) = \zeta$ is canonically defined.** Try simple combinations:
- $1/\beta = 0.5$ ≠ 0.143.
- $1/(2\beta) = 0.25$ ≠ 0.143.
- $1/\beta^2 = 0.25$ ≠ 0.143.
- $\beta/Q = 2/3.5 \approx 0.57$ — no obvious physical meaning.

No clean numerical coincidence between β and ζ.

If we generalize to any P4-class number (β values across 10 UDM systems range from 1.30 to 2.49; mean 1.72), there's no specific point in the distribution where the algebraic combination matches Q-factor = 3.5 cleanly.

**Any apparent numerical match would be embedding-dependent and non-architectural.** It would correspond to a specific oscillator-in-specific-P4-fluid-at-specific-density configuration — not to a universal canon-level prediction.

---

## 6. Architectural Verdict for P4

**P4 channel: H3(P4) fails.** Three sub-verdicts:

1. **No mechanism-level link.** P4 (state-space constitutive) and Q (time-domain damping) live on different axes of the canonical-PDE structure. They are independent principles in the architectural canon.

2. **No structural-relation link.** No canonical algebraic relation exists between β and ζ or Q. Any influence of P4 on Q is indirect via effective viscosity, which is embedding-specific (depends on density, frequency, geometry), not universal.

3. **No clean numerical link.** β values (1.30–2.49) and ζ values (0.143 for Q = 3.5) don't match cleanly under any simple algebraic combination.

**P4 does not architecturally explain Q ≈ 3.5.** Any influence on Q is indirect (P4 sets effective viscosity → viscosity sets damping coefficient → damping coefficient sets ζ → ζ sets Q), and the resulting Q value depends on specific embedding details, not on canon-level architecture.

**Confirms H1 null** as the leading interpretation. With NS-Q2 (V5 weak-coincidental), NS-Q3 (P7 fail), and NS-Q4 (P4 fail), the three correspondence-channel investigations all support H1 null.

---

## 7. Recommended Next Steps

1. **NS-Q5 — Final synthesis + arc closure.** File: `theory/Navier Stokes/Q_Factor/NS_Q5_Synthesis.md`. Aggregate the four memos. Verdict: **H1 null is the arc verdict.** ED's canonical Q ≈ 3.5 is an internal-canon invariant of the underdamped-regime canonical PDE; no specific fluid-mechanical universal corresponds to it. H2 weak-coincidental support from NS-Q2 (V5 moderate-damping overlap, not architectural); H3 fails from NS-Q3 (P7) + NS-Q4 (P4). Estimated 0.5 sessions.

2. **Optional brief note for any future external-facing material:** ED's canonical Q ≈ 3.5 should be framed as an *internal canon invariant* — a property of the canonical-PDE simulation traces — not as a fluid-mechanical universal prediction. This avoids overclaiming.

### Decisions for you

- **Confirm P4 negative verdict.** P4 and Q live on different dynamical axes; no architectural / structural / numerical link.
- **Confirm proceeding to NS-Q5 synthesis as the arc-closure deliverable.** Total arc effort came in at the planned brief-note scale (4 short memos + opening + synthesis = ~2–3 effective sessions).
- **Confirm arc-closure expectation: H1 null** as primary verdict, H2 weak-coincidental from V5 only, H3 fails for both P7 and P4 channels.

---

*NS-Q4 P4 channel evaluated. P4 governs steady-state mobility saturation; Q governs time-dependent oscillation decay. Different dynamical axes; no canonical algebraic relation between β and ζ/Q. Any P4-influence on Q is indirect via effective viscosity, embedding-specific, non-universal. Three correspondence channels (V5 weak-coincidental in NS-Q2, P7 fail in NS-Q3, P4 fail in NS-Q4) all support H1 null. NS-Q5 closes the arc next.*
