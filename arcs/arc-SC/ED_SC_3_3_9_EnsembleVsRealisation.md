# ED-SC 3.3.9 — Ensemble vs Realisation (S2 qualification)

**Status:** Clarification memo. Rephrases the ED-SC 3.1 rev. 3
cross-scale invariance claim at ensemble and per-realisation
resolution. No new execution; no driver changes.
**Parents:**
- `theory/ED_SC_3_3_6_PerSeedCollapse_40Snapshot.md` (40-snapshot
  per-seed collapse test; Broken-collapse verdict).
- `theory/ED_SC_3_3_7_ShellHistogram_Diagnostic.md` (shell-
  histogram diagnostic; Mixed verdict — one H-coord, two
  H-shallow).
- `theory/ED_SC_3_1_rev3_CanonicalPointCertification.md` (canonical
  operating point being qualified).
- `theory/ED_SC_3_0_rev3_ScopePatch.md` (size-dependent flatness
  threshold + refined verdict taxonomy).
**Simulator of record:** `r2_grf_falsifier_tests.py`
  + `ED_Update_Rule.ed_step_mobility`.
**Date:** 2026-04-23 (post ED-SC 3.3.7 execution).

---

## 1. Purpose

The ED-SC 3.3.6 per-seed collapse test (40-snapshot pooling per
seed, per-seed `L_ray_i = 1.08·ξ_i`) and the ED-SC 3.3.7 shell-
histogram diagnostic together resolve the cross-scale invariance
claim of ED-SC 3.1 rev. 3 at two distinct resolutions:

- **S1 (median ρ) collapses cleanly across seeds.** Max ΔS1 =
  0.115 across 10 seeds spanning 35 % natural ξ variation, below
  the ED-SC 3.0 rev. 3 threshold of 0.20. The median of
  `f(ρ | ξ, filter)` is ξ-invariant at both ensemble and
  per-realisation resolution.
- **S2 (IQR of ρ) does not collapse per realisation.** Three of
  ten seeds fail the cross-seed flatness criterion at ΔS2 ∈
  {0.241, 0.269, 0.518}. The shell-histogram diagnostic
  classified one failure (seed 456) as H-coord and two (seeds
  789, 1213) as H-shallow.

This memo **qualifies** the ED-SC 3.1 rev. 3 claim — it does not
retract it. The cross-scale invariance statement remains true for
S1 at both resolutions and for S2 at the ensemble-pool level; it
is false for S2 at per-realisation resolution within the same
seed ensemble, independent of shell-geometry artefacts.

This is an **ensemble-vs-realisation clarification**, a standard
refinement for any distributional invariance statement over
finite-N realisations. No new numerics are presented.

---

## 2. Empirical inputs

### 2.1 From ED-SC 3.3.6 (`per_seed_40snap_summary.json`)

Pooled across 10 seeds (40 snapshots each, per-seed
`L_ray_i = 1.08·ξ_i`):

- `N_pool = 830`
- `S1_pool = −1.961`, CI [−1.997, −1.919]
- `S2_pool = 1.969`, CI [1.772, 2.162]
- `S3_pool = −4.233`

Cross-seed flatness:

- `S2_rel_SEM_across_seeds = 0.0697` (4× tighter than the
  single-snapshot ED-SC 3.3.5 precursor's 0.2840)
- `flat_thresh = max(0.20, 2 · 0.0697) = 0.200` (floor binds)
- `max ΔS1 = 0.115` on seed 123 — **below threshold**
- `max ΔS2 = 0.518` on seed 456 — **above threshold**

Per-seed failures (|Δ| ≥ flat_thresh = 0.200):

| seed | ξ_i | L_ray_i | N_i | S1_i | S2_i | ΔS1 | ΔS2 |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 456 | 2.191 | 2.366 | 67 | −2.186 | 2.988 | 0.115 | **0.518** |
| 789 | 1.663 | 1.796 | 88 | −1.935 | 1.440 | 0.013 | **0.269** |
| 1213 | 1.772 | 1.913 | 86 | −1.880 | 1.494 | 0.041 | **0.241** |

The seven passing seeds occupy S2 ∈ [1.678, 2.149] around the
pool median 1.969, spanning a ±12 % band. All passing-seed ΔS1
values also sit below 0.20.

### 2.2 From ED-SC 3.3.7 (`shell_summary.json`)

Shell-histogram diagnostic (endpoint shells
`r = √(dᵢ² + dⱼ²)` for the 4 ray endpoints of each admitted
motif, 4 × N_motifs entries per seed):

- **Pooled shell distribution:** dominant shell 2.000 (1800
  counts, 54.2 %), next 2.236 (1428, 43.0 %), 2.828 (48, 1.4 %),
  1.414 (44, 1.3 %).
- **Passing-seed JS-vs-pass-pool spread:** max 0.0187 on seed
  101. H-coord threshold set at 1.5× = 0.0280.
- **Seed 456:** JS-vs-pass-pool = **0.0716** (3.8× threshold).
  Unique √8 = 2.828 shell carries 48 endpoints (18 % of its
  endpoints); **this shell is absent from all nine other seeds'
  histograms** (total 0 counts across 9 seeds). Shell entropy
  1.489 bits (pool 1.173) — highest in the ensemble.
- **Seeds 789, 1213:** JS-vs-pass-pool = 0.0060 and 0.0066
  respectively. Both **within** the passing-seed spread of
  [0.0002, 0.0187]. Dominant shells (2.000, 2.236) with
  within-normal fractions. Shell entropies 0.991 and 1.075
  bits — within passing range.

Verdicts from the diagnostic:

- Seed 456 → **H-coord** (shell-geometry crossing).
- Seeds 789, 1213 → **H-shallow** (shell-normal, S2-deviant).
- Master verdict: **Mixed**.

---

## 3. Decomposition of failures

The Mixed verdict distinguishes two structurally independent
mechanisms:

**Seed 456 (H-coord) — coordinate/geometry issue.** The
dimensionless hinge `L_ray/ξ = 1.08` does not absorb lattice-
integer shell crossings. Seed 456 has the largest canonical ξ
(2.191 lu, 24.6 % above ξ_canonical), which pushes its per-seed
`L_ray_i = 2.366 lu` across the threshold at which the diagonal
ray endpoint `(round(0.707·L), round(0.707·L))` rounds to `(2, 2)`
on shell √8, rather than `(1, 1)` on shell √2 as in the other
nine seeds. The filter's 4-ray `N_req = 4` geometry is therefore
sampling a **different shell set** on seed 456 than on the others
— a coordinate-level effect, not a realisation-level effect.
Remediation: redefine the dimensionless hinge to absorb shell
geometry, restrict the invariance claim to seeds below the
shell-crossing ξ threshold, or adopt shell-binned aggregation.
Scoped for `theory/ED_SC_3_3_8_CoordinateReconsideration.md`
(not in this memo).

**Seeds 789 and 1213 (H-shallow) — per-realisation variability.**
Their shell histograms are within the passing-seed spread
(JS-vs-pass-pool both < 0.007), yet S2 on their per-seed 80+ motif
pools is ~25 % below the ensemble mean. The ρ-distribution on the
same integer-lattice shells is genuinely narrower for these two
realisations; no shell-geometry explanation rescues them. This is
**structural per-realisation variability** that survives 40-
snapshot pooling and is not a noise artefact under the ED-SC 3.0
rev. 3 size-corrected threshold (both seeds have N_i ∈ [86, 88],
above any low-N floor). It is what a distributional-invariance
claim over finite realisations looks like when the claim holds at
the pool level but not at the single-draw level.

H-coord is remediable by coordinate redefinition; H-shallow is
**not** — it is an irreducible property of `f(ρ | ξ, filter)`
viewed as an object indexed over realisations, and must be
acknowledged explicitly in the invariance statement.

---

## 4. Revised invariance statement

The ED-SC 3.1 rev. 3 cross-scale invariance claim is refined into
two resolution-dependent sub-statements:

- **S1 (median ρ) — invariant at ensemble AND per-realisation
  resolution.** Across the 10-seed canonical ensemble spanning 35
  % natural ξ variation, per-seed S1 agrees with the ensemble
  median S1_pool to within the ED-SC 3.0 rev. 3 size-corrected
  threshold (max ΔS1 = 0.115, threshold 0.20). The cross-scale
  claim for S1 holds at both resolutions.
- **S2 (IQR of ρ) — invariant at ensemble resolution only.**
  Across the same ensemble, pool-level `S2_pool = 1.969` (CI
  [1.772, 2.162]) is stable under the pooling operation. At
  per-realisation resolution, S2 exhibits O(25 %) spread across
  seeds even at N_i ≳ 70 per seed. The flat-threshold failures on
  seeds 789 and 1213 (H-shallow) are not eliminable by higher
  statistics, not explained by shell geometry, and must be
  treated as part of the invariance statement.
- **S3 (upper-tail log-slope) — provisional.** S3 is defined at
  N_i ≥ 8 per seed and varies widely in the 3.3.6 output
  (S3_i ∈ [−5.95, −3.00]). No ED-SC 3.x memo has proposed a
  cross-scale claim for S3; this memo does not promote one.

**Operational rephrasing** (to be cited in downstream memos in
place of "ED-SC 3.1 rev. 3 invariance"):

> The distributional invariant `f(ρ | ξ, L_ray, α_filt, N_req)`
> of ED-SC 3.1 rev. 3 is cross-scale invariant in the
> dimensionless coordinates `(L_ray/ξ, α_filt, N_req)` at the
> canonical operating point `(1.08, 0.25, 4)` in the following
> sense:
>
> **(a) its median S1 is invariant at per-realisation resolution
> across 35 % natural ξ variation (max ΔS1 = 0.115 <
> flat_thresh); and**
>
> **(b) its IQR S2 is invariant at ensemble-pool resolution only
> — per-realisation S2 exhibits irreducible ~25 % spread across
> seeds within the canonical 10-seed set, not attributable to
> shell-geometry artefacts.**
>
> **(c) Coordinate-level shell crossings can break the
> invariance for individual realisations with ξ > 2.0 lu (cf.
> ED-SC 3.3.7 seed 456); these are mapped separately by
> `ED_SC_3_3_8_CoordinateReconsideration.md`.**

Any ratio-class, quadratic-class, or correlation-class invariant
(GR-SC 1.0+ taxonomy) that is derived from S2, its moments, or
quantiles above the median must treat the ~25 % per-realisation
spread as part of the prediction uncertainty, not as
measurement noise. S1-derived invariants inherit the stronger
per-realisation guarantee.

---

## 5. Downstream implications

**ED-SC 3.4 (multi-parameter coupling).** The pre-registration
must be re-scoped: the test is no longer "is `f(ρ | ξ, filter)`
invariant under varied ξ" but rather "does the ensemble-pool S2
remain stable under deliberate 1D ξ variation over an order of
magnitude, and how does the per-realisation S2 spread evolve with
ξ?" The latter is a **calibration** of the per-realisation spread
along the ξ axis, not an invariance test. Two explicit outputs:
- Ensemble-pool S1, S2 vs ξ.
- Per-seed ΔS2 distribution vs ξ (characterising the H-shallow
  spread as a function of the scan parameter).

**GR-SC 1.0+ (curvature-invariant taxonomy).** Ratio-class
invariants constructed directly from the motif-ratio median
(`r* ≈ −1.88`) inherit the strong S1 per-realisation invariance
and may be cited as point predictions. Invariants depending on
S2 (width of the distribution, IQR-based ratios, upper-percentile
quantiles) must carry an **explicit ~25 % realisation-wise
uncertainty** in their predicted value. In particular:
- `ℛ_Ray`, `ℛ_G`, `r*` (ratio-class, S1-derived): realisation-
  wise predictions stand.
- `ℛ_W = −(2r* + 1)/(r* + 2)` (Weyl ratio, bounded): depends on
  r* alone; inherits S1-level certainty.
- `C²` (Weyl square, quadratic-class, S1²·σ₂² scaling): the
  `σ₂` term inherits S2-level uncertainty; mean-C² is ensemble-
  level, realisation-C² carries ±25 %.
- `det G` (quadratic-class): same as `C²`.
- `κ` (Rayleigh-class, σ₁-derived): untouched by this memo; σ₁
  is a separate distribution statistic not examined in ED-SC
  3.3.6.
- `C_redshift(r)` (correlation-class, two-point): untouched.

GR-SC 1.8 (EIT-Extremal error budget) should adopt the ~25 %
per-realisation S2 spread as an additional contribution to the
`σ₁/κ_M` clearance budget where relevant; the memo currently
treats Channel A and B noise only.

**ED-SC 3.0 rev. 2 / rev. 3.** A pointer line is recommended in
`theory/ED_SC_3_0_Scope.md` rev. 2 §5.1 and `rev3_ScopePatch`
§5, citing this memo for the ensemble-vs-realisation
qualification. No structural change to either scope memo; the
pointer exists so that any future reader of the S-F2 falsifier
encounters the qualification before drawing a per-realisation
falsifier claim from an ensemble-pool quantity.

**ED-SC 3.1 rev. 3.** The canonical-point certification itself is
unchanged. It holds `N = 34, S1 = −1.881, S2 = 1.271` as the
canonical pool values; these are **ensemble-pool** quantities and
were never claimed at per-realisation resolution. A single-line
forward pointer in rev. 3 §4 to this memo is recommended but not
applied here.

---

## 6. Changelog

- **Rev. 1 (2026-04-23, this memo):** opens ED-SC 3.3.9 as an
  ensemble-vs-realisation clarification of the ED-SC 3.1 rev. 3
  cross-scale invariance claim.
  - Integrates ED-SC 3.3.6's verdict (S1 collapses, S2 does not
    per realisation) and ED-SC 3.3.7's Mixed verdict (one
    H-coord, two H-shallow).
  - Decomposes the three failing seeds: 456 (H-coord, deferred to
    `ED_SC_3_3_8_CoordinateReconsideration.md`), 789 and 1213
    (H-shallow, addressed here).
  - Formally rephrases the ED-SC 3.1 rev. 3 invariance statement:
    S1 invariant at per-realisation, S2 invariant at
    ensemble-pool only (~25 % per-realisation spread
    irreducible, not shell-geometry).
  - Declares downstream consequences for ED-SC 3.4 (re-scoped as
    calibration not invariance test), GR-SC 1.0+ (S2-derived
    invariants inherit ±25 % per-realisation uncertainty; S1-
    derived invariants do not), and ED-SC 3.0 / 3.1 (pointer
    references).
  - No execution. No drivers modified. No memos modified —
    pointer lines to this memo in ED-SC 3.0 rev. 3, ED-SC 3.1
    rev. 3, and ED-SC 3.4 (forthcoming) are flagged as
    recommended but deferred to their own dedicated revisions.
