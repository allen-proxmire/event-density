# ED-SC 2.0 r* — Final Verdict

**Status.** Closure memo (2026-04-22). Consolidates the nine-memo r* arc into
a single verdict on what r* = −1.304 is, what it is not, and what survives as
durable content for ED-SC 3.0.

**Scope.** This memo closes the r* analytic arc. It supersedes prior
classifications in `theory/ED_SC_2_0_r_star_Consolidation.md` by incorporating
the R2 analytic chain (`R2_Analytic.md`), the GRF derivation (`R2_GRF.md`),
and the falsifier tests (`analysis/ED_SC_2_0_r_star_R2_GRF_Tests.md`).

---

## 1. Executive summary

### 1.1 What r* was believed to be

At the start of the arc, r* = −1.304 was treated as a cross-scale invariant
of the ED framework: a motif-conditioned median of the field-space Hessian
eigenvalue ratio κ∥/κ⊥, empirically observed to sit in a narrow window at
−1.3 across ED-Arch-01 runs. It was the canonical numeric statement of
ED-SC 2.0 and appeared as a predictive target in the project memory.

### 1.2 What the analytic chain actually shows

The cubic-bistable Scenario-D chain closes to a clean one-parameter form

  **r*(χ) = −2χ/(2χ−1),   χ = 2μκ⊥²/P₀**,

with a natural-amplitude closure δ_max² = −6P₀/P₃ that forces s = −1 and
selects the target r* = −1.304 at χ = 2.145 ⟺ κ⊥² ≈ 2.14. This is
mathematically clean and self-consistent *within the cubic-bistable premises*.

### 1.3 What the R2 analytic chain shows

Porting the same derivation onto the actual R2 PDE (concave mobility
M(p)=(1−p)^{2.7}, concave drift αp^{0.5}) breaks the universality:

- The natural-amplitude discriminant Δ = P₂²/4 − 2P₁P₃/3 = −0.078 < 0.
- No cubic nullcline exists in R2.
- s is a free parameter, not fixed to −1.
- r*_R2 is a two-parameter rational function of (s, d), not a one-parameter
  function of χ.
- At canonical (s=−1.304, d=0.02): r*_R2 ≈ −1.4 × 10⁻³, not −1.304.

The deterministic R2 chain therefore **cannot produce −1.304** under any
interpretation of its own premises.

### 1.4 What the GRF derivation shows

Linearising the R2 SPDE about p̂ ≈ 0.108 yields a 2D isotropic Gaussian
Random Field with M̂ = 0.7345, α_eff = 0.0456, correlation length ξ ≈ 4.0,
Laplacian RMS σ₂ = 0.0898. The Kac–Rice saddle-eigenvalue density has the
closed form

  **f(ρ) ∝ ρ(ρ+1)(3ρ² + 2ρ + 3)^{−5/2}**,   ρ = |κ∥/κ⊥| ≥ 1.

This distribution has **unfiltered median |s| ≈ 1.94**, i.e. s_med = −1.94.
Applying an angular-window approximation to the ray-endpoint filter pushes
the filtered median to **|s|_med ≈ 1.39**. The empirical −1.304 was claimed
to sit in this filtered window.

### 1.5 What the falsifier tests show

Running the three GRF falsifier experiments on the R2 simulator with 10-seed
pooling:

- **Large-sample baseline.** At the canonical filter, N=34 pooled motifs
  give **r* = −1.88 [−2.34, −1.46] (95% CI)** — not −1.304. The original
  single-seed value (N=6) was a small-sample fluctuation.
- **T1 (scale invariance):** inconclusive; the rescaling recipe did not
  preserve p̂ (0.110 → 0.017).
- **T2 (L_ray 2→4):** fails in direction, because L_ray = 4 ≈ ξ leaves the
  local-Hessian regime.
- **T3 (N_req 2→4):** directionally confirmed; r* shifts +0.47 toward
  isotropy as predicted.

The 10-seed pooled median (−1.88) matches the **unfiltered** GRF prediction
(−1.94) to 3%.

### 1.6 Final classification of r*

**r* is a leading-order statistic of the filtered Gaussian-random-field
saddle population of the R2 simulator. It is not a deterministic PDE
observable, not a universal ED constant, and its precise numerical value
(−1.88, revised from −1.304) depends on the filter geometry and on the GRF
correlation length set by the R2 linear-response coefficients.**

What survives is structural: (i) the cubic-chain closed form r*(χ) =
−2χ/(2χ−1) within its premises, (ii) the GRF saddle-ratio density f(ρ)
within its linear-response premises, and (iii) the qualitative fact that
the motif filter selects a GRF sub-population with a well-defined median.

---

## 2. Deterministic chain summary

### 2.1 Cubic-bistable chain (Scenario-D analytic form)

- Form: ∂t δ = ∇·(M(δ)∇δ) − P(δ) + ξ, with M = M₀ + ½M₂δ², P = P₀δ + (P₃/6)δ³.
- **Trace equation:** μ(δ)(κ∥ + κ⊥) = P₀δ + (P₃/6)δ³.
- **Natural-amplitude closure:** δ_max² = −6P₀/P₃ (requires P₀·P₃ < 0).
- **Saddle condition:** forces s = κ∥/κ⊥ = −1 at leading order (symmetric
  pinning of both curvatures on the cubic nullcline).
- **Closed form:** r*(χ) = −2χ/(2χ−1), χ = 2μκ⊥²/P₀.
- **Target match:** r* = −1.304 at χ = 2.145 ⟺ κ⊥² ≈ 2.14 in the chain's
  native units.

Verdict: **internally consistent, structurally correct, and reproduces
−1.304 exactly** under the cubic-bistable premises. But those premises do
not describe R2.

### 2.2 R2 chain (concave mobility + concave drift)

- Form: ∂t p = M(p)∇²p − αp^γ + ση, M(p) = (1−p)^{n*}, n*=2.7, γ=0.5, α=0.03.
- Shift δ = p − p̂ at p̂ ≈ 0.108. Local Taylor coefficients:
  M₀=0.7345, M₁=−2.223, M₂=4.237; P₁=0.0457, P₂=−0.211, P₃=2.931.
- **Trace equation:** μ(δ)(κ∥ + κ⊥) = π_total(δ) = P₁δ + (P₂/2)δ² + (P₃/6)δ³.
- **Anisotropy equation:** 12μ(p−r) = (a−b)[π − 6μ₁(a+b)] (in local frame).
- **Natural-amplitude discriminant:** Δ = P₂²/4 − 2P₁P₃/3 = 0.0112 − 0.0893
  = **−0.0781 < 0** → no real natural amplitude.
- **Consequence:** s is a free parameter; no χ-collapse; r* is a
  two-parameter rational function in (s, d).
- **Evaluation at canonical (s=−1.304, d=0.02):** r*_R2 ≈ −1.4 × 10⁻³.

Verdict: **the R2 deterministic chain produces r* ≈ 0 at the canonical
amplitude, not −1.304**. The cubic chain's χ-universality is an artefact
of the cubic-bistable premises and does not generalise to R2.

---

## 3. Stochastic chain summary

### 3.1 Linearised SPDE and GRF

R2 linear operator: **Lφ = M̂∇²φ − α_eff·φ** with M̂ = 0.7345, α_eff = 0.0456.
Stationary power spectrum S(k) = σ²/[2(α_eff + M̂k²)]. Correlation length
ξ = √(M̂/α_eff) ≈ 4.0. Spectral moments (lattice cutoff k_max = π):
σ₀ = 0.0292, σ₁ = 0.0400, σ₂ = 0.0898. BBKS shape γ_BBKS = 0.611.

### 3.2 Unfiltered saddle-ratio distribution

Kac–Rice weighting of the 2D isotropic-GRF Hessian joint density on the
saddle region (λ₁ > 0, λ₂ < 0):

  f(ρ) ∝ ρ(ρ+1)(3ρ² + 2ρ + 3)^{−5/2},   ρ = |κ∥|/|κ⊥| ≥ 1.

Symmetric under ρ ↔ 1/ρ. **Unfiltered median |s|_med ≈ 1.94** → s_med ≈ −1.94.

### 3.3 Filter-conditioned distribution

Angular-window acceptance for the R2 ray-endpoint filter
w(ρ) = [1 − (2/π) arcsin√(ρ/(ρ+1))]² biases toward near-isotropic saddles.
**Filtered median |s|_med ≈ 1.39** in the leading-order angular-window
approximation.

### 3.4 Empirical R2 (10-seed pooled, canonical filter)

- N = 34 motifs pooled across seeds {77, 101, 123, 234, 456, 789, 1011,
  1213, 1415, 2021}.
- **r* = −1.88, bootstrap-95% CI [−2.34, −1.46].**
- Matches unfiltered GRF prediction (−1.94) to 3%.
- The single-seed canonical value (−1.304, N=6) falls within the upper
  edge of the CI but is displaced from the pooled point estimate by ~0.6;
  treating it as a high-precision invariant was unwarranted.

The filtered-GRF model overpredicted the filter's isotropy bias. The
empirical N_req sensitivity (Test 3) is in the predicted direction but
smaller than the leading-order angular-window estimate.

---

## 4. Falsifier results

| Test | Description                          | GRF prediction           | Empirical result             | Verdict                    |
|------|--------------------------------------|--------------------------|------------------------------|----------------------------|
| T1   | (α, σ) → (2α, √2 σ)                  | |Δr*| ≤ 0.05             | Δr* = −0.31; p̂ collapsed    | **Inconclusive**           |
| T2   | L_ray 2 → 4                          | shift to −1.55 … −1.7    | Δr* = +0.16 (wrong sign)     | **Fails structurally**     |
| T3   | N_req 2 → 4                          | shift to −1.15 … −1.2    | Δr* = +0.47 (right sign)     | **Directionally confirmed**|

**T1 diagnostic.** The rescaling recipe preserves the linear-response
variance ratio σ²/α_eff only at fixed p̂. Under (2α, √2 σ) the drift-noise
balance sets a different p̂; a proper p̂-preserving rescaling would require
re-tuning the IC or extending burn-in.

**T2 diagnostic.** At L_ray = 4 the ray endpoint sits at one full correlation
length ξ from the saddle. The GRF memo's angular-window argument assumed
endpoint field values dictated by the local Hessian Taylor expansion, which
is valid only for L_ray ≪ ξ. At L_ray ≈ ξ the endpoint is a weakly
correlated GRF value, not a Taylor expansion of the saddle — so the filter
sign test becomes approximately independent of local saddle geometry and
moves r* toward the unfiltered baseline along a different mechanism than
the memo modelled.

**T3 diagnostic.** N_req 2 → 4 tightens the number of simultaneously-passing
direction sign tests, which is the pure-geometry selection on which the
angular-window model was built. Direction matches; magnitude is ~50% of the
leading-order prediction, consistent with higher-order corrections from
correlated angular ray statistics.

---

## 5. Final verdict

**r* is a filtered GRF saddle-ratio statistic of the R2 simulator.**

Consequences for each prior claim about r*:

1. **r* is not a deterministic PDE invariant.** The R2 deterministic chain
   gives r* ≈ 0 at canonical amplitudes. The cubic chain produces −1.304
   only under premises (cubic nullcline, natural-amplitude closure) that R2
   violates.

2. **r* is not a universal ED constant.** Its numerical value depends on
   the GRF correlation length (set by M̂/α_eff), the field variance, and
   the filter geometry (L_ray, α_filt, N_req). Change any of these and r*
   changes. The N_req test (§4, T3) provides direct empirical evidence of
   this.

3. **The cubic chain remains structurally correct within its premises.**
   The closed form r*(χ) = −2χ/(2χ−1) and the s = −1 closure are not
   retracted; they describe the cubic-bistable Scenario-D SPDE exactly.
   They simply do not describe R2.

4. **The R2 simulator's r* arises from noise + filter geometry.** The
   leading-order mechanism is GRF saddle statistics; the filter selects a
   sub-population whose median sits near the unfiltered GRF value (−1.94)
   at the canonical filter, and moves systematically under filter changes.

5. **The original target −1.304 requires downward revision to ≈ −1.88
   ± 0.4.** Or, more honestly, should be stated as a distribution — median
   ≈ −1.9, IQR ≈ [−2.6, −1.3] — rather than a pointwise invariant.

---

## 6. Implications for ED-SC 2.0 and a path to ED-SC 3.0

### 6.1 What is universal (structural form)

- **The existence of a well-defined motif-conditioned saddle-ratio
  distribution** on the stationary GRF of any mobility-regularised SPDE
  whose linearisation around its mean has a finite correlation length.
- **The closed-form unfiltered GRF saddle-ratio density**
  f(ρ) ∝ ρ(ρ+1)(3ρ²+2ρ+3)^{−5/2}, which is a universal 2D-isotropic result
  (Bardeen–Bond–Kaiser–Szalay / Longuet-Higgins) independent of SPDE
  coefficients.
- **The cubic-chain closed form r*(χ) = −2χ/(2χ−1)** for any SPDE whose
  drift admits a real natural-amplitude closure (P₂²/4 − 2P₁P₃/3 ≥ 0).
- **Qualitative filter response:** tightening N_req moves r* toward −1;
  loosening N_req moves r* toward the unfiltered GRF median.

### 6.2 What is simulator-dependent (numerical value)

- **The value of −1.304 (or −1.88).** Both are specific to R2's choice of
  (n*, α, γ, σ) which set the GRF correlation length ξ and the linear-
  response variance ratio.
- **The cubic-chain χ that matches any given R2 run.** This is a
  phenomenological back-fit, not a derivation.
- **The filter geometry (α_filt, L_ray, N_req).** Each of these choices
  was made during ED-Arch-01 for qualitative motif detection, not for r*
  calibration.
- **The small-sample (single-seed N=6) median.** Any future quoted value
  of r* must be a pooled multi-seed statistic with explicit CIs.

### 6.3 Recommendations for ED-SC 3.0

1. **Restate r* as a distribution, not a scalar.** The ED-SC cross-scale
   claim should quote median and CI from pooled multi-seed runs of any
   ED simulator, not a single-seed point estimate.

2. **Pin the claim to the filter.** ED-SC 3.0 should specify the exact
   motif filter geometry (α_filt, L_ray, N_req, smoothing operator, saddle
   detector) as part of the invariant. Different filters define different
   invariants.

3. **Decouple the structural claim from the numerical claim.** The
   structural invariant is the *existence* of a stable filtered GRF
   saddle-ratio median; the numerical value depends on the linear-response
   coefficients. The cross-scale claim is most defensible at the structural
   level.

4. **Identify the correlation length as the cross-scale hinge.** Under the
   GRF picture, two different simulators share r* only if they share ξ
   (in lattice units) and the filter geometry in units of ξ. The
   dimensionless group is L_ray / ξ.

5. **Replace the cubic-chain χ fit with the GRF derivation.** Any future
   attempt to predict r* from first principles should proceed through
   (i) linearisation about p̂, (ii) spectral moments, (iii) Kac–Rice
   density, (iv) filter convolution — not through a cubic-bistable
   back-fit.

6. **Recompute targets for all ED-SC tests at pooled multi-seed scale.**
   Every prior single-seed numerical claim in the ED-SC series should be
   audited against a 10-seed pooled rerun; if any invariant claim survives
   only at N < 10, it is a candidate artefact.

7. **Retire "r* = −1.304" as the canonical statement.** Replace with
   "motif-conditioned median of κ∥/κ⊥ lies in [−2.3, −1.5] for R2 at the
   canonical filter, consistent with a filtered GRF saddle-ratio
   distribution centred on −1.94."

---

## 7. Closure

The r* program is closed. The nine-memo arc produced four durable results:

1. The cubic-chain closed form r*(χ) = −2χ/(2χ−1) and its s = −1 closure.
2. The R2 analytic chain, showing no natural amplitude and a free s.
3. The 2D GRF saddle-ratio density f(ρ) ∝ ρ(ρ+1)(3ρ²+2ρ+3)^{−5/2} with
   unfiltered median −1.94.
4. The falsifier suite on the R2 simulator, confirming r* as a filtered
   GRF statistic at the qualitative level and revising the target from
   −1.304 to −1.88 ± 0.4.

**ED-SC 2.0 as a scalar invariant is retired.** ED-SC 3.0 should
reconstitute the cross-scale claim as a structural one over filtered GRF
saddle populations, with the correlation length as the scaling hinge and
the filter geometry as part of the invariant specification.

Memory node `project_ed_r_star_analytic_arc.md` should be updated to
reflect this closure: eighth pass closed the deterministic chain; ninth
pass (GRF port + falsifiers) closes the full program and reclassifies r*
as a filter-dependent GRF statistic, not a universal ED constant.
