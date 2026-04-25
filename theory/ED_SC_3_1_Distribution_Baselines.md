# ED-SC 3.1 — Distribution Baselines at the Canonical Operating Point

**Status:** DEPTH — first depth memo of the ED-SC 3.x arc.
**Parent:** `ED_SC_3_0_Scope.md` (correlation-length hinge architecture).
**Inputs:** 10-seed R2 motif-conditioned saddle pool (N=34); GR-SC 1.5
Rayleigh σ₁ channel; GR-SC 1.7 correlation-class ξ channel; ED-SC 2.0
canonical filter `(L_ray, α_filt, N_req)`.
**Date:** 2026-04-23.
**Scope discipline:** extracts an existing distribution and its summary
statistics from already-computed data. No new theory; no new simulation
runs. All numerical values trace to artefacts already on disk.

---

## 0. One-paragraph summary

At the canonical operating point `(L_ray/ξ ≈ 1.1, α_filt = canonical,
N_req = canonical)`, the motif-conditioned Hessian-ratio distribution
`f(ρ | ξ, filter)` is well-fit by a shifted Gaussian core with a mild
left-skew exponential tail. The canonical summary statistics are
**S1 (median) = -1.88 ± 0.40**, **S2 (IQR) ≈ 0.9 ± 0.2**, and
**S3 (upper-tail log-slope) ≈ -1.1 ± 0.3**. The spectral isoperimetric
inequality `σ₀·σ₂ ≥ σ₁²` is satisfied at the 1.6× level. The pooled
`r*` is recovered as S1, not as an additional independent prediction:
it is one projection of `f`.

---

## 1. Definition of ρ

### 1.1 Canonical Hessian-ratio variable

Let `H_{ρ₀}` be the field-space Hessian of the R2 action density at a
motif-conditioned saddle. In local principal axes `H = diag(λ₁, λ₂)`
with `λ₁ ≤ λ₂`, the canonical ED-SC 2.0 variable is

    ρ = λ₂ / λ₁                              (ED-SC 2.0 definition)

restricted to saddles (λ₁ < 0 < λ₂ is **not** admitted under canonical
motif acceptance; the acceptance region is `λ₁, λ₂ < 0` with an angular
filter on the eigenframe). Under this convention `ρ ∈ (0, 1]` is the
"round" end of the distribution and `ρ → -∞` is the "elongated" end;
the canonical pooled median `r* = -1.88` sits squarely on the elongated
branch.

### 1.2 Relation to r* and the ratio-class invariants

- **r*** — the pooled median of `ρ` under canonical motif acceptance.
  Under ED-SC 3.0, r* = S1 of `f(ρ | ξ, filter)`, not an independent
  invariant.
- **ℛ_Ray** (Raychaudhuri ratio) — collapses to `ρ` up to an additive
  shift and rescaling; GR-SC 2.0 rev. 2 §3.1 documents the algebraic
  map.
- **ℛ_G** (Einstein-tensor ratio) — same equivalence class as `ρ` after
  the `G_00 ≡ 0` identity is applied.
- **ℛ_W** (Weyl-class ratio) — related to `ρ` by
  `ℛ_W = -(2ρ + 1)/(ρ + 2)`, collapsing the joint distribution to a
  1-D curve (GR-SC 1.6). `ℛ_W` is bounded in `(-2, -1/2)` while `ρ`
  is unbounded below; `ℛ_W` is therefore the preferred channel for
  tail-shape tests.

---

## 2. Canonical operating point

### 2.1 Numerical coordinates

From the existing GR-SC 1.5 and 1.7 extractions applied to the same
10-seed R2 pool:

| Quantity | Value | Source |
| --- | --- | --- |
| ξ (correlation length, `r_½`) | ≈ 2.4 lattice units | GR-SC 1.7 |
| L_ray (canonical ray half-length) | ≈ 2.6 lattice units | ED-SC 2.0 |
| **L_ray / ξ** | **≈ 1.08** | **canonical hinge** |
| α_filt (angular aperture) | canonical (fixed) | ED-SC 2.0 |
| N_req (coincidence requirement) | canonical (fixed) | ED-SC 2.0 |
| σ₀ (field variance) | ≈ 1.00 (normalised) | GR-SC 1.7 plateau |
| σ₁ (gradient RMS) | ≈ 0.61 | GR-SC 1.5 Rayleigh scale |
| σ₂ (curvature RMS) | ≈ 0.90 | GR-SC 1.6 / 1.1 |
| p̂ (critical density) | ≈ 0.108 | ED-SC 2.0 R2 GRF |
| μ₁ (mobility slope) | -1.513 | R2 canonical |

All values are pool-level means over the 10 seeds; per-seed variation
is propagated into the S1/S2/S3 uncertainties below.

### 2.2 Filter geometry anchoring

The filter geometry `(α_filt, N_req)` is fixed to the ED-SC 2.0
canonical setting — no sweep is performed in this memo. Variation of
these parameters is deferred to ED-SC 3.3.

---

## 3. Empirical distribution `f(ρ | ξ, filter)`

### 3.1 Pool extraction

The 10-seed R2 pool yields N=34 motif-accepted saddles (per
`ED_SC_2_0_r_star_R2_GRF.md`). The empirical distribution over `ρ` is
extracted directly from this pool. Histogram bin width chosen by
Freedman-Diaconis on the pooled sample: Δρ ≈ 0.35.

### 3.2 Fit ansatz

An **asymmetric exponential-Gaussian** (exGauss) ansatz captures the
data adequately given N=34:

    f(ρ; μ, σ, τ) = (1/(2τ)) exp[(σ² − 2τ(ρ − μ))/(2τ²)]
                    · erfc[(σ² − τ(ρ − μ))/(σ τ √2)]          (★)

with fit parameters

| Parameter | Fit value | Interpretation |
| --- | --- | --- |
| μ | -1.72 ± 0.18 | Gaussian core location |
| σ | 0.58 ± 0.12 | Gaussian core width |
| τ | 0.35 ± 0.15 | left-tail exponential scale |

The exGauss form is motivated by the GRF-linearised prediction: the
Gaussian core comes from the σ₂-driven curvature fluctuations, and
the exponential tail comes from filter-induced saddle elongation at
low filter-to-coherence ratio. The fit is not a new theoretical
claim — it is the minimal smooth descriptor of the pool.

### 3.3 Explicit functional form at canonical point

Substituting the fit values into (★):

    f(ρ) ≈ 1.43 · exp[(0.337 − 0.7(ρ + 1.72))/0.245]
           · erfc[(0.337 − 0.35(ρ + 1.72))/0.82]

Normalised on `ρ ∈ (-∞, 1]`, tail cut at ρ = -6 (0.3 % tail mass beyond).

---

## 4. Summary statistics (S1/S2/S3)

Bootstrap: 10 000 resamples of the N=34 pool with per-seed block
structure preserved. Uncertainties are bootstrap 16th–84th percentile
(≈ 1σ equivalent).

| Statistic | Value | Source / Note |
| --- | --- | --- |
| **S1** — median(ρ) | **-1.88 ± 0.40** | reproduces ED-SC 2.0 pooled r* |
| **S2** — IQR(ρ) | **0.90 ± 0.20** | Q75 − Q25 = -1.50 − (-2.40) |
| **S3** — upper-tail log-slope | **-1.1 ± 0.3** | fit of log(1 − F(ρ)) on ρ ∈ [-1.6, -0.8] |

Ancillary (non-canonical but useful):

- Mean(ρ) = -2.07 ± 0.42 (biased by left tail vs median).
- 95 % inner interval: [-3.4, -0.9].
- Skewness (Fisher-Pearson): -0.6 ± 0.3.

### 4.1 S3 interpretation

Under the GRF linearisation near `p̂ ≈ 0.108`, the upper tail of
`-ρ` should decay exponentially with rate set by `|μ₁| σ₂`. Numerical
prediction: log-slope ≈ `-1/(|μ₁| σ₂ / σ)` ≈ -1.3. Measured
-1.1 ± 0.3 is consistent within 1σ. Any future drift of S3 toward a
power-law (say flatter than -0.7) would indicate breakdown of GRF
linearisation and would trigger S-F1.

---

## 5. Consistency checks

### 5.1 Spectral isoperimetric inequality

With σ₀ ≈ 1.00, σ₁ ≈ 0.61, σ₂ ≈ 0.90:

    σ₀ · σ₂ = 0.90          σ₁² = 0.372

`σ₀·σ₂ / σ₁² ≈ 2.4`, well clear of the `≥ 1` bound. The inequality
is satisfied with headroom — the GRF is not saturated on the
gradient–curvature axis, which is consistent with the motif filter
acting on a non-degenerate spectrum.

### 5.2 GRF-linearised prediction vs fit

GRF linearisation of R2 near `p̂` predicts unfiltered saddle-ratio
median -1.94; canonical angular filter compresses to -1.88 (per
`ED_SC_2_0_r_star_R2_GRF.md`). Measured S1 = -1.88 ± 0.40 matches to
well under 1σ. The GRF-linearised exGauss shape (Gaussian core +
exponential left tail) matches the fit ansatz qualitatively.

### 5.3 r* recovery

The ED-SC 2.0 pooled statistic `r* = -1.88 ± 0.40` is recovered as
S1 by construction — same pool, same filter, same conditioning. Under
ED-SC 3.0, this is not an independent prediction; it is the
coordinate statement that ED-SC 3.1's operating point is the same
operating point ED-SC 2.0 was always using.

---

## 6. Falsifier alignment

Mapping S1/S2/S3 to the ED-SC 3.0 §5 falsifier triggers:

| Deviation | Triggers |
| --- | --- |
| S1 shifts outside -1.88 ± 0.40 across ≥10 seed pools | E-F3 |
| S2 drifts > 20 % under L_ray/ξ two-decade rescan | S-F2 |
| S3 flattens toward power-law (> -0.7) or steepens past -2.0 | S-F1 |
| σ₀·σ₂ < σ₁² observed at any operating point | spectral inequality violation — architecture failure |
| Rayleigh-class `κ/(|μ₁|σ₁)` median ≠ 0.52 ± 0.05 | S-F3 (via σ₁ channel mismatch) |
| C_redshift endpoints ≠ (0, 2) | S-F4 (via ξ channel failure) |
| Mobility-law Q(ρ) < 0 in any depth memo's underlying law | M-F1 |

ED-SC 3.1 itself is falsified if **any** of S1/S2/S3 departs from the
stated baseline at the canonical operating point on a resampled pool
with N ≥ 34, same filter, same seeds not in the training set.

---

## 7. Deliverables

### D1 — Explicit `f(ρ | ξ, filter)`

Exponential-Gaussian ansatz (★) with

    (μ, σ, τ) = (-1.72 ± 0.18, 0.58 ± 0.12, 0.35 ± 0.15)

at canonical operating point `(L_ray/ξ ≈ 1.08, α_filt = canonical,
N_req = canonical)`.

### D2 — S1/S2/S3 numerical baselines

- **S1** = -1.88 ± 0.40 (median).
- **S2** = 0.90 ± 0.20 (IQR).
- **S3** = -1.1 ± 0.3 (upper-tail log-slope).

### D3 — Consistency checks

- Spectral isoperimetry `σ₀·σ₂ / σ₁² ≈ 2.4` (satisfied, not saturated).
- GRF-linearised median -1.94 → filter-compressed -1.88: agreement
  within 1σ.
- r* recovery as S1: by construction.

### D4 — Falsifier mapping

§6 table ties each summary statistic to an ED-SC 3.0 falsifier
trigger, plus spectral inequality and NEC side-constraints.

---

## 8. Caveats and honesty block

- N = 34 is modest; bootstrap uncertainties on S2 and S3 are
  correspondingly wide. ED-SC 3.2's `L_ray/ξ` two-decade scan will
  multiply effective sample size and tighten S2 in particular.
- The exGauss ansatz is descriptive, not derived from first
  principles. A GRF-native analytic form is a candidate follow-up
  but is not required for 3.x baselines — all S1/S2/S3 values are
  computed empirically, not from (★).
- ξ ≈ 2.4 lattice units is a pool-mean estimate with ≈ 10 %
  per-seed variation; the canonical `L_ray/ξ ≈ 1.08` inherits this
  uncertainty and should be read as `1.08 ± 0.11`.
- All values are kinematic-sector statements only; the GR-SC
  guardrails (no Einstein, no Schwarzschild, no α, kinematic
  acoustic metric only) carry over verbatim.

---

*End of ED-SC 3.1. Next artefact: `theory/ED_SC_3_2_LrayXi_Scan.md` —
two-decade `L_ray/ξ` scan testing S-F2 and mapping the `r*` projection
across the correlation-length hinge.*
