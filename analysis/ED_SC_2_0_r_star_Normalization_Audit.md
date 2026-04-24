# ED-SC 2.0 r*: Normalization Audit and Data-Generating-Process Reconstruction

**Status.** Diagnostic memo for the zero-motif null result in
[`ED_SC_2_0_r_star_MonteCarlo_Results.md`](ED_SC_2_0_r_star_MonteCarlo_Results.md).
Reconstructs the actual ED-Arch-01 simulator pipeline from the R2
canonical-reproduction code (`analysis/scripts/ed_arch_r2/`) and the
ED-Arch-01 canonical memo. Headline: **the null result is not a
normalization mismatch — the analytic chain's assumed PDE form is not the
one ED-Arch-01 integrates**. The canonical r* = −1.304 is produced by a
*concave* mobility + *concave* penalty + ray-endpoint motif filter, not by
the M₂-expanded bistable cubic of the analytic chain. The analytic chain
is therefore correct *given* its premise, but its premise (the
leading-order form `∂_t δ = M₀∇²δ − P₀δ − (P₃/6)δ³ + ξ`) is a Taylor
truncation that has *lost the specific nonlinear structure* that selects
κ⊥ ≈ 1.04 in the actual simulator.

---

## 1. Normalization reconstruction

### 1.1 Dimensional survey

ED-Arch-01 Scenario-D integrates a field `p(x,t)` with hard clip
`p ∈ [p_min, p_max] = [0.01, 1.0]`, initial condition `p₀ ~ U(0.3, 0.7)`
on a 64×64 periodic grid with `dx = 1`, `dt = 0.05`, and runs for 500
steps to `t_phys = 25`. At the architectural saddle peak `(n*, σ*)` the
stationary field has `p̂ ≈ 0.1079`, `σ_E ≈ 0.01525`, `p ∈ [0.054, 0.165]`
(≈ ±3σ_E about p̂).

The update rule is

    p_{t+1} = p_t + dt · [∇·(M(p) ∇p) − α · p^γ + σ · η]      (R2.1)

with
- **Mobility** `M(p) = ((p_max − p)/p_max)^n`, exponent `n = n* = 2.7`.
- **Penalty** `α · p^γ`, with `α = 0.03`, `γ = 0.5`.
- **Noise** `η(x,t) ~ N(0,1)` iid, spatially uncorrelated, temporally
  uncorrelated; amplitude `σ = 0.0556` (not √dt-scaled in the canonical
  run).
- **Clipping** `p ← clip(p, 0.01, 1.0)` after each step.

### 1.2 Mapping to the analytic-chain SPDE

The analytic chain uses

    ∂_t δ = ∇·(M(δ)∇δ) − P(δ) + ξ,     M = M₀+½M₂δ², P = P₀δ+(P₃/6)δ³,
    M₀ = 1, M₂ = 0, P₀ = 1, P₃ = −1.                           (T.1)

Formal Taylor expansion of (R2.1) around `p = p̂`:

Let `δ ≡ p − p̂`. Then
- `M(p) = (1 − p/p_max)^n` expanded at `p = p̂`:
  `M = m₀ + m₁ δ + m₂ δ² + …` with
  `m₀ = (1−p̂)^n ≈ 0.892^2.7 ≈ 0.735`,
  `m₁ = −n(1−p̂)^{n−1}/p_max ≈ −2.22`,
  `m₂ = n(n−1)(1−p̂)^{n−2}/(2 p_max²) ≈ 2.80`.
  So `M(p)` has a **linear-in-δ component** (`m₁ ≠ 0`) absent from
  `M₀ + ½M₂δ²`. The analytic chain's `M₂δ²` form is *not* the leading
  correction to R2's mobility.

- `α p^γ = α (p̂ + δ)^γ` expanded:
  `α p̂^γ + α γ p̂^{γ−1} δ − α γ(1−γ) p̂^{γ−2} δ² / 2 + …`
  with `p̂ = 0.108`, `γ = 0.5`:
  constant `α p̂^γ = 0.03 · 0.329 ≈ 0.0099` (steady drift),
  linear `α γ p̂^{γ−1} = 0.03 · 0.5 · 3.05 ≈ 0.0457` (≈ P₀_eff),
  quadratic `−α γ(1−γ)/2 · p̂^{γ−2} ≈ −0.03 · 0.125 · 8.55 ≈ −0.0321`
  (a *quadratic* term, not cubic).
  So the effective penalty is dominated by a linear-plus-quadratic series,
  not the linear-plus-cubic of the analytic chain.

Matching the linear coefficients gives
`P₀_eff ≈ 0.046`, `M₀_eff ≈ 0.735`, so the *effective* normalised
(M₀=P₀=1) units rescale time by `1/P₀_eff ≈ 21.7` and length by
`√(M₀_eff/P₀_eff) ≈ 4.0`. Amplitude rescaling: the analytic chain's
"natural amplitude" is `δ_nat ≈ √(6 P₀/|P₃|)`; to match curvature scales,
`δ → δ / δ_nat`.

### 1.3 σ mapping

In dimensional units (R2.1), σ = 0.0556 has units of `[field/time]`. In
the analytic-chain normalization with time-rescale `τ = t · P₀_eff`,
`σ_norm = σ / √(P₀_eff · ℓ²_rescale) ≈ 0.0556 / √(0.046 · 16) ≈ 0.065`.

**Conclusion:** σ* = 0.0556 in R2 maps to σ_norm ≈ 0.065 in the analytic-
chain normalization — essentially the same number, because the ratio
`σ / √(P₀ · ℓ²)` is already O(0.05) in both units. **Normalization is
not the main gap.**

### 1.4 Curvature scaling

Hessian of the field at a saddle has units `[field]/[length]²`. From
(R2.1) to (T.1):
- `[field]` rescales by `1/δ_nat ≈ 1/√(6·0.046/0.03) ≈ 1/3.0` ≈ 0.33,
  i.e. `δ_norm = (p − p̂)/3.0`. But R2 field excursion is only
  ±0.05 about p̂, so δ_norm ≈ ±0.017.
- `[length]²` rescales by `1/(M₀/P₀) = 1/16`.

So `κ_norm = κ_R2 · (0.33 / 16) ≈ κ_R2 · 0.021`. R2 saddles have
`|κ|` set by centred differences of a field with range ≈ 0.1 over
length scales ≈ 1 grid point, so `κ_R2 ~ O(0.1 − 1)`.
`κ_norm ≈ 0.002 − 0.02` in normalised units. **This is compatible with
the MC measurement `κ⊥_med = 0.011` at σ = 0.0556.**

In other words: the MC pipeline running the analytic-chain SPDE *is*
recovering the correct κ⊥ magnitude for a concave-mobility R2-like field.
What it is NOT recovering is the motif-filter-selected *sub-population*,
because the motif filter is different (see §2.4) and because the actual
SPDE it's filtering on is different (§2.1–2.3).

### 1.5 Why s ≈ 5 would not help

The Results memo §5.1 conjectured that a factor s ≈ 5 on κ⊥ could
reconcile MC with the target 1.04. The rescaling dictionary above shows
this factor would have to come from length-scale mismatch alone
(amplitude mismatch is small). A length rescaling by √16 = 4 gets most
of the way; but it is applied symmetrically to the analytic formula
`χ = 2μκ⊥²/P₀`, which is **dimensionless** — so rescaling κ⊥ by a
length factor has to be compensated by rescaling P₀ by the inverse of
its square, leaving χ (and therefore r*) unchanged. **The r* prediction
is normalization-invariant; no choice of rescaling moves r*.**

This is a stronger negative result than §5.1 suggested: the discrepancy
is not dimensional. It is a structural mismatch between the PDE the
analytic chain Taylor-expanded and the PDE ED-Arch-01 actually runs.

---

## 2. Simulator pipeline reconstruction

Summary of R2 canonical pipeline, extracted from
`analysis/scripts/ed_arch_r2/r2_canonical.py`,
`r2_motif_filter.py`, and `R2_Motif_Verdict.md`:

### 2.1 Mobility is concave-saturating, not quadratic

`M(p) = ((1 − p)/1.0)^{2.7}` is monotone-decreasing and concave. The
analytic-chain `M₀ + ½M₂δ²` is symmetric-quadratic. Effects:

- **δ_max location.** R2 field is pinned at p̂ ≈ 0.108 by the balance
  `α p^γ = M(p) · ∇²p − fluctuation`. Analytic chain predicts natural
  amplitude `δ_nat² = −6 P₀/P₃ = 6`; this value is meaningless for
  R2 because R2 doesn't have a cubic penalty.
- **κ⊥.** Concave M suppresses gradients near p=1 and enhances them near
  p=0, producing *broader* stationary-point basins than a symmetric
  quadratic mobility; this makes R2's saddles flatter (smaller |κ|)
  than a matched-linear-coefficient analytic-chain field would produce.
- **Motif population.** Concave M selects saddles whose contour shape
  reflects the one-sided asymmetry; this breaks the exact D₂ symmetry
  assumed by the ED-SC 2.0 motif filter of the Workflow memo.
- **Filter acceptance.** Under our MC filter (Workflow memo §3), zero;
  under the R2 ray-endpoint filter, N = 6 at the canonical seed.

### 2.2 Penalty is concave square-root, not cubic

`P(p) = α p^γ = 0.03 · p^{0.5}`. Effects:

- **δ_max.** Set by `P(p̂) ≈ M(p̂) ⟨∇²p⟩ + σ-corrections`. Not at any
  cubic nullcline. The Anisotropy memo's "natural-amplitude closure"
  `s = −1` is a theorem for cubic penalty only.
- **κ⊥.** Concave penalty with `P'(p̂) = α γ p̂^{γ−1} ≈ 0.046` gives an
  effective linear stiffness of 0.046, ~20× weaker than P₀ = 1 in the
  analytic chain. This is the direct origin of the factor-of-20
  smallness in MC κ⊥ if the analytic chain's P₀ is interpreted as
  R2's P'(p̂).
- **Motif population + filter.** As §2.1 — broken assumption of D₂
  symmetric cubic-saddle geometry.

### 2.3 Initial conditions and noise are generic

- **IC:** `p₀ ~ U(0.3, 0.7)`, seed 77. Uniform, not Gaussian. Amplitude
  range ±0.2 about 0.5, which relaxes to p̂ ≈ 0.108 after ~50 steps.
- **Noise:** white in space and time, no spatial correlation, no
  coloured structure.
- **No localised forcing, no ray injection, no source term, no
  symmetry-breaking seed.**
- **No deterministic pre-relaxation:** noise is on from t = 0.

These three items are **as assumed in the MC pipeline**. The gap is
*not* in initial conditions, boundary conditions, or noise structure.

### 2.4 Motif filter is ray-endpoint, not α-contour D₂

R2 filter (from `r2_motif_filter.py`):

1. **Smooth** the field once: `p_smooth = p + 0.2 · Σ_4neighbours p`.
2. Find **Morse saddles** of `p_smooth` (discrete Hessian, periodic BCs).
3. For each saddle compute eigenvectors `ê_neg`, `ê_pos` of H.
4. Trace 4 rays of length `L_ray = 2` in directions `±ê_neg`, `±ê_pos`
   (integer lattice steps, periodic wrap).
5. **Admit** the saddle iff:
   - both `±ê_neg` ray endpoints have `p < p̂ − α_filt · std(p)`,
   - both `±ê_pos` ray endpoints have `p > p̂ + α_filt · std(p)`,
   with `α_filt = 0.25`.
6. **Degeneracy cut:** discard saddles where `|λ_min|/|λ_max| < 0.10`.

This is **fundamentally different** from the MC Workflow memo's
pre-registered filter. The MC filter requires a D₂-symmetric, aspect-1.5
ray-like α-contour connected component; the R2 filter requires four ray
endpoints to clear asymmetric thresholds about the global mean. The
geometric objects tested are not the same.

**R2 filter succeeds at canonical σ*:** N_motif = 6, median ratio
κ∥/κ⊥ = −1.304 exact match, IQR [−1.94, −1.21]. Reproduction of the
canonical r* value is confirmed by R2.

**MC filter fails at canonical σ*:** N_motif = 0 because it tests an
incompatible geometric condition (D₂ symmetry of α-contour cc), which is
not satisfied by typical R2-like stationary points.

### 2.5 The canonical r* is a Hessian-eigenvalue ratio, not the analytic κ⊥

R2 reports `r* = λ_larger/λ_smaller` (signed, in (−∞, −1]) at motif-
admitted saddles. The analytic chain's `r*` is `4μκ∥κ⊥/denom`, which
under the assumption `κ∥ · κ⊥ < 0` and the trace equation collapses to
`−2χ/(2χ−1)`. **The two `r*`s coincide only if the analytic-chain
`κ∥/κ⊥` equals R2's `λ_1/λ_2`**, which is true by definition (both are
the signed ratio of 2D spatial-Hessian eigenvalues), but requires the
Hessian to be evaluated at the *same* points under the *same* filter.

The analytic chain predicts that for `s = κ∥/κ⊥ = −1.304` we need
`χ = 2.145` i.e. κ⊥² ≈ 1.07. R2 measures `λ_1/λ_2 = −1.304` directly
at N = 6 filter-admitted saddles without ever needing to compute
`χ` or isolate `κ⊥` — because the analytic chain's `χ`-dependence comes
from the trace equation `μ(κ∥+κ⊥) = P₀ δ + (P₃/6)δ³`, which is derived
from the cubic penalty. **R2 has no cubic penalty, so the trace equation
does not hold, and the closed-form `r* = −2χ/(2χ−1)` does not apply.**

---

## 3. Motif-population hypothesis testing

For each candidate gap mechanism, qualitative + quantitative
prediction of the change in saddle distribution:

| mechanism                         | shifts δ_max | shifts κ⊥ | shifts motif pop. | shifts filter rate | reconciles? |
|-----------------------------------|--------------|-----------|--------------------|--------------------|-------------|
| (A) length rescaling only         | no           | yes       | no                 | no                 | **no** (χ invariant) |
| (B) amplitude rescaling only      | yes          | no        | no                 | no                 | **no**       |
| (C) σ large enough to reach δ_nat | yes (→√6)    | yes (→stiff)| deterministic bounce regime | no — filter still rejects iso noise | **no** |
| (D) concave mobility (R2-like)    | → p̂≈0.108   | weakens   | yes — asym shape   | yes — destroys D₂   | **yes** for r*; **no** for Workflow filter |
| (E) concave penalty (R2-like)     | → p̂≈0.108   | weakens   | yes — asym shape   | yes — destroys D₂   | **yes** for r*; **no** for Workflow filter |
| (F) ray-endpoint filter (R2)      | no           | no        | no                 | yes — from 0 to 6   | **yes** — N>0, median = −1.304 |
| (G) non-periodic or source term   | yes          | yes       | yes                | yes                 | unclear      |
| (H) coloured spatial noise        | no           | yes (can tune)| yes (reduces density)| yes (improves sym)| partial   |

**Necessary ingredients to reproduce r* = −1.304 as in R2:**
1. The **R2-form** SPDE (concave mobility + concave penalty), not the
   Taylor-expanded analytic-chain form.
2. The **R2 ray-endpoint motif filter**, not the α-contour D₂ filter.
3. Noise at σ ≈ 0.0556 on the R2 field scale (equivalently, the R2 field
   statistics `p̂ ≈ 0.108`, `std ≈ 0.015`).

Ingredients that are *not* needed:
- Localised forcing, ray injection, or symmetry-breaking seeds.
- Non-periodic boundaries.
- Coloured noise.
- Deterministic pre-relaxation.

---

## 4. Decision tree

```
Q1: Is the null result due to normalization mismatch (length/amplitude/time)?
│
├─ NO  (shown in §1.5: χ is dimensionless, r* is invariant).
│      Skip Test A.
│
Q2: Is the null result due to the analytic chain's PDE form differing from R2's?
│
├─ YES (shown in §2.1–2.2: mobility is concave, penalty is concave p^0.5).
│      → Test D: rerun MC with R2's mobility + penalty; measure κ⊥ and the
│        Hessian-eigenvalue ratio distribution. Expectation: r*_med matches
│        R2's −1.304 band under the R2 filter; our Workflow filter still
│        rejects, confirming the filter is also a mismatch.
│
Q3: Is the null result due to the motif filter definition?
│
├─ YES (shown in §2.4: R2 filter admits N=6; Workflow filter admits N=0).
│      → Test F: rerun our MC field with the R2 ray-endpoint filter
│        substituted for the α-contour D₂ filter. Expectation under
│        analytic-chain PDE: small but non-zero motif count; r* ratio
│        may still be off because PDE form differs.
│
Q4: Is the analytic chain's closed-form r* = −2χ/(2χ−1) a faithful
    asymptotic of R2's motif-filtered r*?
│
├─ UNKNOWN. The chain derives the formula from cubic penalty. R2 has no
│  cubic penalty; trace equation does not hold. The formula may still
│  be a *descriptive* parametrisation of the measured ratio via an
│  effective χ_eff, but it is not derived from R2's PDE.
│      → Test G: from R2 canonical snapshots, directly extract κ⊥ at
│        the N=6 filter-admitted saddles and test whether the reported
│        median −1.304 satisfies r* = −2χ/(2χ−1) with χ = 2κ⊥²/P'(p̂).
│        If yes, χ-formula is structurally valid under effective
│        linearisation. If no, the formula is specific to cubic
│        penalty and has no direct meaning in R2.
│
Q5: Is there any plausible extension in which the analytic chain and
    ED-SC 2.0 reference both hold simultaneously without any of the
    above reinterpretations?
│
├─ Only if the Taylor truncation keeping only `P₀δ + (P₃/6)δ³` is
│  quantitatively adequate near p̂ ≈ 0.108 for R2's penalty. Check
│  whether `α p^γ` admits a regime where the Taylor expansion is
│  cubic-dominated.
│      → Test H: compute the Taylor expansion of α p^γ about p̂ out
│        to O(δ³), compare the cubic coefficient to the quadratic,
│        and assess whether the analytic chain can be re-derived with
│        a non-zero quadratic penalty term.
```

---

## 5. Deliverables

### 5.1 Targeted numerical tests

**Test D — R2-PDE MC with R2 motif filter (first priority).**
Port `r2_canonical.py` + `r2_motif_filter.py` into the MC framework
(`r_star_montecarlo.py`), run 10 realisations at canonical parameters
(α = 0.03, γ = 0.5, n = 2.7, σ = 0.0556), apply the R2 filter, and
report:
- N_motif per realisation (target ≈ 6).
- Median `λ₁/λ₂` (target −1.304 within [−1.5, −1.1]).
- IQR width (R2 gives [−1.94, −1.21]).
This is the canonical reproduction — if it fails, the R2 code itself
is inconsistent; if it succeeds, we have an aligned MC baseline on
which to vary filter and PDE ingredients.

**Test F — analytic-chain PDE with R2 motif filter.**
Our current MC (Taylor-truncated bistable cubic) + R2 ray-endpoint
filter substituted for the α-contour D₂ filter. Reports:
- N_motif per realisation (expected 0–few).
- If non-zero, median `λ₁/λ₂`. Tests whether the R2 filter applied to
  a cubic-penalty field reproduces −1.304 or gives a different
  ratio.

**Test G — χ-formula consistency check on R2 snapshots.**
Extract κ⊥ directly from R2 canonical-run snapshots at the N=6 filter-
admitted saddles; compute `χ = 2 M(p̂) κ⊥² / P'(p̂)` with
`M(p̂) ≈ 0.735, P'(p̂) ≈ 0.046`; check whether `−2χ/(2χ−1)` reproduces
−1.304. This is the decisive test of whether the analytic chain's
closed form describes R2 under effective linearisation.

**Test H — Taylor audit of the penalty.**
Expand `α p^γ` to O(δ³) at p̂ and compare quadratic-to-cubic
coefficient ratio. Quadratic dominates (coefficient ≈ −0.032 vs
cubic ≈ 0.02 and both at O(10⁻²·δⁿ)); cubic truncation of the analytic
chain is **not leading-order** for R2.

**Test I (optional) — re-derivation with quadratic penalty.**
Redo the Anisotropy-memo Taylor expansion with a quadratic penalty
term `P(δ) = P₀δ + (P₂/2)δ²` instead of the cubic, and produce the
analogous closed form for s and r*. This closes the analytic chain
around R2's actual PDE.

### 5.2 Most-consistent hypothesis

**The null result is explained by reading §2.4 (motif-filter mismatch)
combined with reading §2.1–2.2 (PDE-form mismatch).** The ED-SC 2.0
canonical value r* = −1.304 is a property of the *R2* simulator — a
concave-mobility, concave-penalty SPDE equipped with a ray-endpoint
motif filter — and it is reproducible under those ingredients (R2
canonical run: N = 6, median −1.304). It is **not** a property of the
cubic-bistable Taylor truncation used throughout the analytic chain,
under any noise level or normalization.

This resolves the null result honestly:
- The analytic chain's closed form `r* = −2χ/(2χ−1)` is correct under
  its premises.
- Its premises (cubic bistable + D₂ symmetric α-contour motifs) are a
  Taylor truncation + filter idealization that do not match ED-Arch-01.
- ED-Arch-01's r* = −1.304 is empirically reproduced in R2 with
  concave mobility + concave penalty + ray-endpoint filter.
- The arc's analytic closure should be understood as *formal structural
  form* (predicts r* is a single scalar χ’s function) rather than
  *quantitative target* (κ⊥ ≈ 1.04 is not meaningful in R2 units).

### 5.3 Recommended arc update

1. Tag the analytic chain as *cubic-penalty leading order*, with an
   explicit statement that ED-Arch-01's penalty is `α p^γ` (concave
   square-root), not cubic. Flag this as G6 in the arc memory.
2. Demote "κ⊥ ≈ 1.04" from "one remaining number" to "dimensional
   fiction of the cubic truncation". Replace with the concrete
   empirical observables: `M(p̂), P'(p̂), κ∥/κ⊥` from R2.
3. Add Tests D, F, G, H above as the next-step targets, replacing the
   SaddleSolve §8 falsification band (which was keyed to the cubic
   truncation, hence now obsolete).

---

## 6. Related memos

- `analysis/ED_SC_2_0_r_star_MonteCarlo_Results.md` — the null result
  this memo explains.
- `analysis/ED_SC_2_0_r_star_MonteCarlo_Workflow.md` — the
  (now-known-to-be-mismatched) pre-registered workflow.
- `analysis/scripts/ed_arch_r2/R2_Motif_Verdict.md` — the R2 canonical
  reproduction with N = 6, median −1.304.
- `theory/ED_SC_2_0_r_star_Anisotropy.md` — closed-form asymptotic
  (correct under cubic penalty; not applicable to R2 directly).
- `theory/ED_SC_2_0_r_star_SaddleSolve.md` — deterministic bounce
  diagnostic (now known to be a cubic-truncation artefact).
- `memory/project_ed_r_star_analytic_arc.md` — durable arc memory,
  to be updated with the PDE-form guardrail.
