# NS-Turb-4 — Failure-Mode Audit

**Date:** 2026-04-30
**Status:** NS-Turb-4 of the P7 ↔ Turbulence arc. **Headline: four failure modes catalogued. Failure A (cascade-regime magnitude mismatch) is decisive — P7's 3–6% does not match dominant inertial-range cascade triads (0.1–0.3, 2–10× larger). Failure B (mechanism mismatch: forced vs free-cascade), C (polynomial-order: cubic vs bilinear), and D (index-structure asymmetry: symmetric-gradient vs transport) are structural and persist at all amplitudes. The forced-response regime gives a restricted partial success for H2; H3 (architectural template for cascade) fails. Final architectural classification in NS-Turb-5.**
**Companions:** [`P7_Triads_NS_Turb_1_Opening.md`](P7_Triads_NS_Turb_1_Opening.md), [`P7_Triads_NS_Turb_2_Energy_Transfer.md`](P7_Triads_NS_Turb_2_Energy_Transfer.md), [`P7_Triads_NS_Turb_3_Inheritance.md`](P7_Triads_NS_Turb_3_Inheritance.md), [`../NS-2.08_ED-PDE_Direct_Mapping.md`](../NS-2.08_ED-PDE_Direct_Mapping.md), [`../NS-3.02b_Multi_Lyapunov_Audit.md`](../NS-3.02b_Multi_Lyapunov_Audit.md).

---

## 1. Purpose

This memo aggregates the findings from NS-Turb-2 (energy-transfer derivation + dimensional-observable analysis) and NS-Turb-3 (inertial-range magnitude check + forced-response analysis) into a complete failure-mode audit of the P7 ↔ turbulence mapping.

The audit catalogues:
- **Where H2 fails** (cascade regime — order-of-magnitude mismatch).
- **Where H2 partially succeeds** (forced-response regime — substantive restricted match).
- **Why H3 cannot be realized** (structural mismatches at the mechanism, polynomial-order, and index-structure levels).

This is the decisive audit before the final architectural-classification synthesis (NS-Turb-5).

---

## 2. Inputs

| Input | Source |
|---|---|
| H1/H2/H3 hypotheses | [`P7_Triads_NS_Turb_1_Opening.md`](P7_Triads_NS_Turb_1_Opening.md) §6.3 |
| Cascade-triad magnitude $\tilde f \sim 0.1$–$0.3$ | [`P7_Triads_NS_Turb_2_Energy_Transfer.md`](P7_Triads_NS_Turb_2_Energy_Transfer.md) §6.2; [`P7_Triads_NS_Turb_3_Inheritance.md`](P7_Triads_NS_Turb_3_Inheritance.md) §3.1 |
| Forced-response match $R_\mathrm{forced} \sim \epsilon^2 \sim 0.02$–$0.09$ for $\epsilon \sim 0.15$–$0.3$ | [`P7_Triads_NS_Turb_3_Inheritance.md`](P7_Triads_NS_Turb_3_Inheritance.md) §4.3, §5 |
| P7 amplitude 3–6%, weak coupling ~0.03 | [`../../Architectural_Canon.md`](../../Architectural_Canon.md) §2 (P7), [`../../Universal_Invariants.md`](../../Universal_Invariants.md) §3 |
| NS-2.08 advection-is-non-ED finding | [`../NS-2.08_ED-PDE_Direct_Mapping.md`](../NS-2.08_ED-PDE_Direct_Mapping.md) §5 |
| NS-3.02b multi-Lyapunov advection-breaks-gradient-norm finding | [`../NS-3.02b_Multi_Lyapunov_Audit.md`](../NS-3.02b_Multi_Lyapunov_Audit.md) §3.4 |

---

## 3. Failure Mode A — Cascade-Regime Magnitude Mismatch

### 3.1 Statement

| Quantity | Value |
|---|---|
| Dominant inertial-range cascade-triad magnitude (normalized $\tilde f$ or $\tilde\eta$) | **O(0.1–0.3)** |
| Weak-triad tail magnitude | O(0.01–0.05) |
| P7 architectural amplitude prediction | 3–6% (= 0.03–0.06) |
| **Mismatch factor (cascade vs P7)** | **2–10×** |

P7's 3–6% lies *below* dominant-cascade values by a factor of 2–10×. P7 overlaps only the weak-triad tail of the cascade distribution — *not* the cascade-defining triads that carry the bulk of the energy flux.

### 3.2 Verdict

**H2 fails in the developed-cascade regime.** The amplitude that defines turbulence's inertial-range cascade does not correspond to P7's predicted amplitude. The match would require P7 to predict O(0.2), not O(0.05); empirically and architecturally it predicts the latter.

This rules out interpretation of P7 as the architectural template for *turbulent cascade* triadic transfer.

---

## 4. Failure Mode B — Mechanism Mismatch (Forced vs. Free)

### 4.1 The structural distinction

P7's predicted amplitude (3–6%) is the **steady-state response of a driven nonlinear oscillator** — the canonical PDE forced by multiplicative perturbations on a fundamental, with the nonlinear $M'(\rho)|\nabla\rho|^2$ term coupling the fundamental to harmonics. This is a forced-driven phenomenon: the fundamental exists because of external driving; the harmonics are generated *because* of that driving.

Turbulence cascade is **free conservative redistribution** — energy is injected at large scales, redistributed across the inertial range by triadic interactions that conserve energy within each triad ($S(\mathbf{k}|\mathbf{p},\mathbf{q}) + S(\mathbf{p}|\mathbf{q},\mathbf{k}) + S(\mathbf{q}|\mathbf{k},\mathbf{p}) = 0$ per NS-Turb-2 §4.3), and dissipated at small scales. There is no specific "fundamental" mode that drives "harmonic" generation — the cascade is multi-scale and statistical.

### 4.2 Why these are different physical phenomena

| Aspect | P7 (forced) | Cascade (free) |
|---|---|---|
| Energy source | External driving on fundamental | Initial conditions / large-scale forcing → cascade |
| Mode population | One driven mode + driven harmonics | Many modes simultaneously active |
| Triad role | Couples fundamental → harmonics under forcing | Redistributes existing energy across modes conservatively |
| Steady-state structure | Fixed-amplitude harmonic ratio response | Statistical distribution; Kolmogorov 5/3 spectrum |
| Time character | Steady-state under continuous forcing | Statistically stationary in inertial range |

These are different physical setups even though both are described by NS-class equations and both produce triadic Fourier interactions.

### 4.3 Verdict

**H2 cannot be extended to H3 (architectural template for cascade).** The forced-response match (NS-Turb-3 §5) is a magnitude correspondence in a *non-cascade* regime; extending it to claim that P7 architecturally underlies the cascade requires reconciling the forced-vs-free mechanism distinction, which is not delivered. The cascade is a structurally different physical phenomenon from P7's driven harmonic generation.

This failure mode is decisive for H3 and is not resolvable by amplitude-match work alone — it is a structural physics distinction.

---

## 5. Failure Mode C — Polynomial-Order Mismatch

### 5.1 Polynomial structure

| Source | Nonlinearity | Polynomial order in field | Third harmonic at order |
|---|---|---|---|
| P7 (canonical PDE) | $M'(\rho)|\nabla\rho|^2$ | **Cubic in ρ** (since $M'$ depends on ρ at leading order) | First nonlinear order: $k_0 \times k_0 \times k_0 \to 3k_0$ direct |
| NS advection | $u_j \partial_j u_i$ | **Bilinear in u** | Second nonlinear order: $k_0 \times k_0 \to 2k_0$, then $k_0 \times 2k_0 \to 3k_0$ |

### 5.2 Implication for amplitude scaling

Same numerical magnitude $R \sim 0.05$ (5%) corresponds to different $\epsilon$ values:
- **P7 cubic structure:** $R \sim \epsilon$ → $\epsilon \sim 0.05$ matches.
- **NS bilinear structure:** $R \sim \epsilon^2$ → $\epsilon \sim 0.22$ matches.

### 5.3 Verdict

The polynomial-order mismatch is a real structural distinction. The forced-response match in NS-Turb-3 §5 (achieved at $\epsilon \sim 0.15$–$0.3$ for NS bilinear) corresponds to a *different perturbative regime* than P7's prediction (which would correspond to $\epsilon \sim 0.05$ for cubic). The numerical-magnitude match is at *different effective forcing intensities* in the two systems.

This indicates **non-equivalence of the underlying nonlinear operators** at the polynomial-structure level. P7's cubic and NS's bilinear are different *types* of nonlinearity; one gives k=3 directly, the other gives it via cascade. Even when amplitudes match numerically, the operator structures differ.

---

## 6. Failure Mode D — Index-Structure Asymmetry

### 6.1 Index structure of the two nonlinearities

**P7:** $M'(\rho)|\nabla\rho|^2 = M'(\rho)(\partial_i \rho)(\partial_i \rho)$. Symmetric quadratic-in-gradients of a scalar field. Index structure: $\delta_{ij} \cdot \partial_i \rho \partial_j \rho$ — *full symmetric* in (i, j).

**NS advective:** $u_j \partial_j u_i$. Bilinear field-times-gradient with directional transport. Index structure (with incompressibility projection): $k_j P_{im}(\mathbf{k}) \cdot u_j(\mathbf{p}) u_m(\mathbf{q})$ from NS-Turb-2 §3.3 — *asymmetric in (j, m)*, with explicit transport-direction dependence (via $k_j$) and projection onto solenoidal subspace (via $P_{im}$).

### 6.2 Persistence at all amplitudes

The index-structure asymmetry is not a small-amplitude perturbative artifact. NS's $k_j P_{im}$ structure is fundamentally non-symmetric and transport-directional; P7's $\delta_{ij}$ structure is fundamentally symmetric and gradient-self-coupling. These differ at *all* amplitudes and in *all* regimes.

### 6.3 Connection to NS-2.08 and NS-3.02b findings

This is exactly the "advection-is-non-ED" obstruction documented in:
- **NS-2.08 §5:** "advection as fluid-mechanical-addition not native to ED architecture" — the kinematic coupling between velocity components is structurally distinct from any P-level ED-architectural content.
- **NS-3.02b §3.4 + §5:** "the advective convective derivative's vortex-stretching term" specifically breaks the gradient-norm Lyapunov in 3D NS via this index-structure-asymmetric content.

Both prior findings independently identified the index-structure asymmetry as the locus of the advection-vs-ED structural mismatch. NS-Turb-4 confirms the same finding from the third angle (P7-vs-cascade mapping), giving three mutually-reinforcing identifications:
- **Architectural** (NS-2.08): advection is non-ED canonical.
- **Dynamical** (NS-3.02b): advection breaks gradient-Lyapunov via vortex-stretching.
- **Spectral** (NS-Turb-4 here): advection's index-structure asymmetry prevents P7-class Fourier-triadic mapping.

Three independent program-level analyses converge on the same structural feature.

### 6.4 Verdict

**The index-structure asymmetry is a fundamental structural mismatch persisting at all amplitudes.** It is not resolvable by amplitude-matching, polynomial-order analysis, or regime-restriction. It is the *single most consistent finding across multiple program analyses*: advection is structurally non-ED, in three independent senses.

---

## 7. Partial Success — Forced-Response Regime

### 7.1 The substantive positive finding

Per NS-Turb-3 §5: in viscous-laminar forced-response regime, with single-wavenumber forcing at $k_0$ and $\epsilon = u(k_0)/(\nu k_0) \sim 0.15$–$0.3$ (moderate weakly-nonlinear):

$$R_\mathrm{forced} = \frac{|u(3k_0)|}{|u(k_0)|} \sim \epsilon^2 \sim 0.02\text{–}0.09.$$

This window overlaps P7's predicted 3–6% cleanly. **Order-of-magnitude / window-overlap match in restricted regime.**

### 7.2 Significance

- This is a substantive positive finding. The forced-response match is *not* trivially generic; it requires the moderate-weakly-nonlinear regime specifically. Outside this regime (deep linear: too small; transitional/strongly nonlinear: too large; cascade: too large), the match fails.
- Experimentally accessible: oscillating-cylinder boundary layers, weakly-forced channel flows, viscous-acoustic-driven flows. A dedicated DNS experiment in this regime would directly test the magnitude prediction.

### 7.3 Limits of the partial success

- **Restricted regime.** Match holds only in the moderate weakly-nonlinear forced-response regime — not in turbulent cascade.
- **Coincidental rather than structural.** The match reflects shared Fourier-triadic structure (generic to quadratic-in-field nonlinearities) + similar weak-coupling magnitude — not an architectural identity. The structural mismatches (B, C, D) persist within the matched-amplitude regime.
- **Order-of-magnitude only.** Precise prefactors depend on geometry, forcing structure, dimensionality; the match is at the window-overlap level rather than precision-prediction level.

This partial success supports H2 in a restricted, conditional, qualified sense. It does *not* support H3.

---

## 8. Provisional Verdicts

Summary across the three hypotheses identified in NS-Turb-1 §6.3:

| Hypothesis | Claim | Verdict | Reason |
|---|---|---|---|
| **H1** | Generic triadic similarity | **Succeeds (trivially)** | Both NS and P7 produce triadic Fourier interactions $\mathbf{k}_1 + \mathbf{k}_2 + \mathbf{k}_3 = 0$. Generic to any quadratic-in-field nonlinearity. Not specifically informative about ED. |
| **H2** | Weak-coupling amplitude correspondence (3–6% match) | **Partial success in restricted forced-response regime; fails in cascade regime** | Forced-response: $R \sim \epsilon^2 \sim 0.02$–$0.09$ for $\epsilon \sim 0.15$–$0.3$ overlaps P7's 3–6%. Cascade: $\tilde f \sim 0.1$–$0.3$, 2–10× larger than P7. |
| **H3** | Architectural template for NS turbulence cascade | **Fails** | Three structural mismatches persist: mechanism (forced vs. free-cascade); polynomial order (cubic vs. bilinear); index structure (symmetric-gradient vs. transport). NS-2.08 + NS-3.02b independently identified the index-structure mismatch as the "advection-is-non-ED" obstruction. NS-Turb-4 confirms from spectral angle. |

### 8.1 Aggregate

**ED's P7 supplies a limited, restricted-regime structural prediction about NS forced-response harmonic generation in moderate weakly-nonlinear flow. ED's P7 does *not* architecturally template developed-cascade turbulence.** The arc's investigation reveals that the apparent triadic-structure similarity is generic (H1 trivial), the weak-coupling amplitude correspondence is regime-restricted (H2 partial), and the structural-template ambition fails for cascade (H3 fail).

The substantive positive content of the arc:
- A clean, testable order-of-magnitude prediction in a specific regime (forced-response, $\epsilon \sim 0.15$–$0.3$).
- A reconfirmation across three program-level analyses (NS-2.08 architectural, NS-3.02b dynamical, NS-Turb-4 spectral) that advection is structurally non-ED, with the index-structure asymmetry as the locus.

The substantive negative content:
- ED does not architecturally explain turbulence cascade. The Clay-NS-relevance question (NS-3 closed at Intermediate per NS-3.04) is not resolved or strengthened by this arc.

---

## 9. Recommended Next Steps

1. **NS-Turb-5 — Final architectural classification synthesis.** File: `theory/Navier Stokes/Turbulence/P7_Triads_NS_Turb_5_Synthesis.md`. Aggregate the four prior memos into the arc closure. Headline: H1 trivial / H2 partial-restricted-regime / H3 fail. ED's P7 supplies a limited forced-response prediction; does not architecturally template turbulence cascade. Three-way convergence (NS-2.08 + NS-3.02b + NS-Turb-4) on advection-is-non-ED structural finding. Estimated 1 session.

2. **Optional: forced-response DNS experiment design.** With H2 partial-success identified in restricted regime, a dedicated DNS at $\epsilon \sim 0.15$–$0.3$ measuring $u(3k_0)/u(k_0)$ would directly test the order-of-magnitude prediction. Setup: simple-geometry viscous-laminar flow with single-wavenumber forcing, measure third-harmonic amplitude as function of $\epsilon$. Compare to ED P7 prediction R ≈ 3–6% in the moderate-weakly-nonlinear window. Estimated +2–3 sessions for setup + analysis. Defer to standalone-paper decision; appendix-class for any future "ED forced-response" paper.

3. **Optional: Note for future "ED forced-response" paper.** With H2 partial-success establishing a restricted-regime correspondence, there's potential for a follow-up paper: *"ED P7 Predicts Third-Harmonic Amplitude Ratio in Viscous-Laminar Forced Flow"* or similar narrower-scope title. This would not claim turbulence-cascade architectural status but would document the forced-response match as a substantive ED-NS structural prediction. Defer to NS-Turb-5 synthesis decision.

### Decisions for you

- **Confirm four-failure-mode catalogue.** A: cascade magnitude mismatch decisive for H2-as-cascade; B: mechanism mismatch (forced vs free) decisive for H3; C: polynomial-order mismatch decisive at operator structure; D: index-structure asymmetry the persistent structural feature documented across NS-2.08 + NS-3.02b + NS-Turb-4.
- **Confirm H2 partial-success framing.** Restricted to forced-response regime, $\epsilon \sim 0.15$–$0.3$, $R \sim 0.02$–$0.09$ overlap with P7's 3–6%. Substantive but limited.
- **Confirm H3 fail.** Cascade architectural template not delivered; structural mismatches at three independent levels.
- **Confirm proceeding to NS-Turb-5 synthesis as the final arc deliverable.**

---

*NS-Turb-4 failure-mode audit complete. Four failure modes catalogued: A (cascade-regime magnitude mismatch — P7's 3–6% vs cascade's 0.1–0.3, decisive for H2-as-cascade); B (mechanism: forced harmonic-generation vs free conservative-cascade — decisive for H3); C (polynomial-order: cubic P7 vs bilinear NS — operator non-equivalence); D (index-structure asymmetry: symmetric-gradient vs transport-directional — persistent at all amplitudes; three-way confirmation via NS-2.08 + NS-3.02b + NS-Turb-4). H1 trivially succeeds; H2 partial-success in forced-response regime $\epsilon \sim 0.15$–$0.3$; H3 fails. ED P7 supplies a restricted, regime-conditional prediction about NS forced-response harmonic generation; does not architecturally template turbulence cascade. NS-Turb-5 synthesis next.*
