# ED-SC 3.6 L-Larger Follow-up — Scoping

**Pass:** seventeenth (post-F4 / post-FFT closure; new ED-SC 3.6 arc)
**Date:** 2026-04-23
**Parent memos:**
- `theory/ED_SC_3_4_twopoint_FilterRelaxation_Integration.md` (F4 sub-arc closure, three-line verdict)
- `theory/ED_SC_3_5_FFT_XiField_Integration.md` (FFT arc closure, four-channel convergence on "canonical filter too sparse on 64²")
- `theory/GR_SC_1_8_PostF4_Consolidation.md` §4 Option A (L-larger pre-registration as the remaining internal path)
- `theory/GR_SC_1_0_MotifCurvatureInvariants.md` §5 (authoritative Correlation-class row; canonical-filter entry Inconclusive pending this arc)
**This memo pre-registers:** `theory/ED_SC_3_6_L_Larger_Driver.md` (driver spec, forthcoming), `analysis/scripts/ed_sc_3_6_l_larger.py` (driver script, forthcoming), `outputs/ed_sc_3_6_l_larger/` (artefacts), `theory/ED_SC_3_6_L_Larger_Integration.md` (post-execution closure).

---

## 1. Purpose

Resolve the structural finding that closed both the F4 sub-arc and
the ED-SC 3.5 FFT arc:

> **The canonical operating point `(α_filt, N_req) = (0.25, 4)`
> is too sparse on 64² for any measurement channel — motif-pair
> binning (F4), Δr-refined motif-pair binning (F4-alt-refine),
> motif-mask-weighted FFT (ED-SC 3.5 Channel B) — to resolve
> a sub-1-lu half-rise. GR-SC 1.7's half-rise compression
> prediction `r_½^filt / r_½^unfilt = 0.80 ± 0.05` is
> untestable at the canonical filter on 64².**

Per `GR_SC_1_8_PostF4_Consolidation.md` §4, the **L-larger
follow-up** is the single remaining internal path to test
GR-SC 1.7 at the canonical operating point. This memo pre-registers
that experiment in detail.

**Scope statement.** ED-SC 3.6 determines, on one or two larger
lattices (128² primary, 256² optional secondary), whether the
canonical motif-filter becomes dense enough to support:

- **(a) Motif-pair correlation** — the F4 channel, generalised
  to larger L (minimum-image distance still the estimator; r-grid
  unchanged at Δr = 0.5 lu).
- **(b) FFT motif-mask-weighted field correlation** — the ED-SC
  3.5 Channel B, generalised to larger L (full-shell radial
  average unchanged; mask density expected to stay at
  ⟨ρ_M⟩ ≈ 5 × 10⁻⁴ with absolute motif count rising ∝ L²).

A third reference channel, **(c) bulk-field FFT autocorrelation**,
is included as a self-calibration check inherited verbatim from
ED-SC 3.5 Channel A.

This is the last internal-compute option for closing the
canonical-filter row of GR-SC 1.0 §5 authoritative invariant
table. If ED-SC 3.6 produces a definitive verdict, the
Correlation-class row is fully populated at both canonical and
relaxed-filter evidence levels. If ED-SC 3.6 reports
Inconclusive on all channels even at 256², the canonical-filter
row moves to a permanent **"Inconclusive — structural scale
mismatch between canonical filter and testable lattices"**
entry, and the next recommended step shifts to an empirical or
theory-redesign arc (outside ED-SC 3.x scope).

---

## 2. Lattice size selection

Pre-register two candidate sizes, in sequence:

### 2.1 Primary: L = 128

- Lattice area: 16,384 sites (4× 64²).
- Expected motif count per snapshot: ≈ 4 × (canonical 64² count)
  = 4 × 2.1 ≈ **8.4 motifs / snap** (linear in area at fixed
  mask density).
- Ensemble motif count (10 seeds × 40 snaps × 8.4): **≈ 3,360**.
- Expected F4 pair-count in r ∈ [0.5, 5.0] lu: the fraction of
  pair candidates at r ≤ 5.0 scales as (π · 5² / L²) in the
  minimum-image limit, so 25π/16384 ≈ 4.79 × 10⁻³ of
  `C(N_motifs_seed, 2)` candidates. With N_motifs ≈ 336 per seed,
  candidates ≈ 56,280 and admissible-r pair count ≈ 270 per
  seed → **≈ 2,700 across ensemble**. At Δr = 0.5 lu over 10
  bins, **≈ 270 pairs / bin** — 13× the 20-pair admissibility
  threshold. F4 channel **adequately dense**.
- FFT Channel B mask density: ⟨ρ_M⟩ still ≈ 5 × 10⁻⁴ (selection
  rule is site-local; density does not change). But pair-
  coincidence probability at r = 1 is (⟨ρ_M⟩)² × N_neighbours
  = 4 × 2.5 × 10⁻⁷ = 10⁻⁶ per site, times 16,384 sites × 40
  snaps × 10 seeds = **≈ 6.5 motif-pair-coincidence events at
  r = 1 lu**. Still sparse but no longer zero at the ensemble
  level. Channel B **marginally adequate**; proper test requires
  the bootstrap-band width on ξ_φ_B(1) to be narrower than
  (C = 2 − ε) for any physical ε of interest. We record this
  as a stretch target, not a hard success criterion.

### 2.2 Secondary (optional): L = 256

- Lattice area: 65,536 sites (16× 64², 4× 128²).
- Expected motif count per snapshot: **≈ 33.6 motifs / snap**.
- Ensemble motif count: **≈ 13,440**.
- F4 pair-count in r ∈ [0.5, 5.0] lu: ~ 4,370 per seed →
  **≈ 43,700 across ensemble**, ≈ **4,370 / bin** at Δr = 0.5 lu.
  F4 channel **strongly dense**.
- FFT Channel B pair-coincidence at r = 1 lu: ≈ **100 events
  per ensemble**. Comfortably above Poisson-noise floor. Channel
  B **adequately dense** for half-rise resolution.

### 2.3 Scaling expectations (recorded for integration-memo cross-check)

- Motif density per area: **independent of L** (selection rule is
  local; ⟨ρ_M⟩ ≈ 5 × 10⁻⁴ on all tested L).
- Absolute motif count per snapshot: **∝ L²**.
- F4 pair density (r ≤ R_max) per ensemble: **∝ L² × mask_density
  × R_max²** — grows with L.
- F4 pair-count sparsity (the 64² bottleneck): **disappears** for
  r ≤ 5 lu on L ≥ 128.
- FFT shell spacing at small r: **unchanged** (shells are
  determined by Z² geometry, not by N). The shell sampling density
  grows with L (more sites per shell), narrowing bootstrap bands.
- `xi_halfdecay` vs full-shell FFT **estimator discrepancy**:
  the ~20 % gap documented in ED-SC 3.5 §2 is expected to persist
  on larger L (it reflects binning rule, not lattice size).
  Arc-internal consistency rule: pick one estimator and use it
  for both numerator and denominator.
- ξ_canonical rescaling: **none**. The ED-SC 3.3 canonical hinge
  `L_ray / ξ = 1.08` and canonical ξ = 1.7575 lu are lattice-
  independent *target values*; on larger L, the IC-amplitude
  calibration simply interpolates to the same ξ_target.

**Ordering rule.** Execute L = 128 first. Promote to L = 256
only if (a) L = 128's F4 channel passes its admissibility gate
but Channel B remains noise-limited, *and* (b) the L = 128
verdict is Inconclusive or marginal. If L = 128 produces a
definitive Confirmed / Refuted verdict, L = 256 is not executed
in this arc.

---

## 3. Measurement channels

### 3.1 Channel A — motif-pair correlation (F4 generalised to L)

Inherits the F4 canonical driver
(`analysis/scripts/ed_sc_3_4_twopoint_correlation.py`) verbatim,
generalised by a single `fr.SIZE` override at driver entry:

- r-grid: same 10-point Δr = 0.5 lu grid {0.5, 1.0, …, 5.0}.
- Estimators: Pearson + Spearman on the motif-ratio pair pool.
- Bootstrap: 4,000 pair-level resamples per bin.
- Admissibility gate: 20 pairs/bin ensemble, 10 pairs/bin per-seed.
- Minimum-image distance on the periodic L² torus.

Expected verdict-relevant quantities on L = 128:
`N_pairs_total` ≈ 2,700; `N_pairs_per_bin_mean` ≈ 270; admissibility
≈ 8–10 / 10 (exactly recovers the F4-alt admissibility regime but
at the **canonical filter** rather than the relaxed filter — the
key difference).

### 3.2 Channel B — FFT motif-mask-weighted field autocorrelation

Inherits the ED-SC 3.5 driver Channel B verbatim, generalised by
`fr.SIZE` override:

- Fields: `φ_B(x) = p(x) · M(x)`, mean-subtracted post-masking.
- Radial shell averaging over all achievable Z² shells up to
  r = L/2.
- Bootstrap: 4,000 seed-level resamples.
- Extraction: `r_half_B` = smallest r where
  `C_B(r) = 2 [1 − ξ_φ_B(r) / σ_0²_B] = 1`.

Expected verdict-relevant quantities on L = 128: ξ_φ_B(1)
resolved above the point-process floor with ensemble bootstrap
band narrower than 0.02 (rough target; to be verified empirically).

### 3.3 Channel C — FFT bulk-field autocorrelation (self-calibration)

Inherits ED-SC 3.5 Channel A verbatim:

- Fields: `φ_A(x) = p(x)`, mean-subtracted.
- Same radial-shell averaging as Channel B.
- Purpose: self-calibration guardrail. `r_half_A` measured via
  the full-shell FFT must match `xi_halfdecay` on the same
  ensemble within the 20 % estimator-bias band documented in
  ED-SC 3.5 §2; if `xi_halfdecay(r_½) / xi_canonical − 1` exceeds
  ±10 % on the L-larger ensemble, raise a guardrail flag (the
  test is whether *both* estimators reproduce their lattice-
  independent targets, not whether they agree with each other).

---

## 4. Calibration strategy

### 4.1 IC-amplitude calibration

Inherit the 9-point calibration pre-pass (`CALIBRATION_W_GRID`)
from the F4-alt / ED-SC 3.5 drivers verbatim. Per-seed procedure
unchanged:

1. Run the 9-point w-grid with `fr.SIZE` set to the new L.
2. For each w, evolve 40 snapshots with the canonical simulator
   parameters (`fr.ALPHA0, fr.GAMMA, fr.NOISE0, fr.MOBILITY_EXP,
   fr.DT`) — **none of these are size-scaled**; the ED framework
   is lattice-unit-normalised.
3. Measure `xi_halfdecay` per snapshot; mean across snapshots.
4. Interpolate to ξ_target = 1.7575.
5. One refinement step if |miss| > 1 %.

**Expected outcome on L ∈ {128, 256}:** per-seed miss fractions
similar to 64² (≤ 1 % achievable via the 9-point grid
without refinement for most seeds). No re-tuning of the
calibration grid expected.

### 4.2 Expected estimator differences

Two estimators measured per run:

- **`xi_halfdecay`** (integer-binned, ED-SC 3.3 canonical):
  expected per-seed value ≈ 1.7575 ± 0.01 lu (target).
- **FFT full-shell r_half** (Channel C of this driver):
  expected per-seed value ≈ 2.10 ± 0.05 lu (same 20 %
  estimator-bias documented in ED-SC 3.5 §2).

The 20 % gap is a **within-arc constant**; it should not drift
with L (it reflects the binning rule, not the lattice size).
Arc-internal consistency rule (inherited from ED-SC 3.5 §2.4):
within ED-SC 3.6, pick the Channel-C FFT estimator as
denominator for any ratio involving Channel B, and use
`xi_halfdecay` as the ξ reference only for the L = L calibration
gate (per-seed miss vs ξ_target). Both numerator and denominator
of `r_½^filt / r_½^unfilt` must come from the same estimator.

**Primary ratio definition for this arc:**

```
ratio = r_half_Channel_B_FFT / r_half_Channel_C_FFT
```

where both half-rises are extracted from the full-shell FFT
radial average. Channel A (pair-binned F4) produces an
independent ratio using its own half-rise extractor; the two
ratios are reported separately and compared in the integration
memo.

---

## 5. Success criteria

Three per-channel primary gates; the arc produces a combined
verdict only when all three pass.

### 5.1 Channel A (pair-binned F4) primary gate

- **≥ 8 of 10 r-bins admissible** at Δr = 0.5 lu (ensemble
  pair-count ≥ 20 per bin).

### 5.2 Channel B (FFT mask-weighted) primary gate

- **Ensemble mean mask density ⟨ρ_M⟩ × L² ≥ 8** motifs per
  4,096-site area-equivalent block. Restated: absolute
  ensemble-total motif count ≥ 3,200 (ensemble = 10 seeds ×
  40 snaps) for L = 128, or ≥ 12,800 for L = 256. This is a
  density target, not a mask-density target — the mask density
  stays at 5 × 10⁻⁴ regardless of L; we need absolute count
  for pair-coincidence statistics.

### 5.3 Channel C (FFT bulk reference) primary gate

- **Self-calibration guardrail passed** — `xi_halfdecay`
  ensemble mean within ±10 % of ξ_target = 1.7575 lu. This
  is the ED-SC 3.5 §4 guardrail, carried forward unchanged.

### 5.4 Combined success: definitive verdict

- Half-rise ratio extracted on both Channel A (pair-binned)
  and Channel B (FFT) with bootstrap bands of width < 0.15
  each (a 15 % bootstrap band corresponds to the Confirmed /
  Confirmed-marginal discriminating width).
- Ratios reported alongside a cross-estimator comparison.

### 5.5 Partial success: at least one channel definitive

- If Channel A passes its gate but Channel B does not (or
  vice versa), the channel that passes provides the
  canonical-filter verdict; the other is reported as
  diagnostic-only.

### 5.6 Guardrail failure: one or more gates fail

- Combined verdict: **Inconclusive (L-larger-insufficient)**.
- Promotes L = 256 if L = 128 was the primary execution;
  otherwise closes the arc at "Inconclusive — structural
  scale mismatch" per §1.

---

## 6. Verdict taxonomy

Four-way, inherited from F4 / ED-SC 3.5, applied per channel:

- **Confirmed** — ratio ∈ [0.75, 0.85] (tenth-pass 0.80 ± 0.05
  band, bootstrap band entirely inside Confirmed window).
- **Confirmed-marginal** — ratio ∈ [0.75, 0.85] with bootstrap
  band leaking outside, *or* ratio ∈ [0.70, 0.75) ∪ (0.85, 0.90].
- **Refuted** — ratio < 0.70 or > 0.90 (outside the double
  envelope).
- **Inconclusive** — no C = 1 crossing in the r-range *or* primary
  gate (§5) failed.

**Combined verdict reconciliation across channels A and B:**

| Channel A verdict | Channel B verdict | Combined |
|---|---|---|
| Confirmed | Confirmed | **Two-channel Confirmed** (strongest outcome; GR-SC 1.7 survives at canonical filter) |
| Confirmed | Refuted | **Channel-dependent** — new finding; pair-binned and mask-weighted field correlators disagree at the canonical filter. Escalates to a new scoping memo in the eighteenth pass. |
| Confirmed | Inconclusive | **Single-channel Confirmed (pair-binned)**; Channel B deferred. |
| Refuted | Refuted | **Two-channel Refuted** — GR-SC 1.7 half-rise compression prediction refuted at canonical filter on the L-larger lattice. Would be the arc's strongest negative outcome; scope-restricted to the Correlation-class channel per the F4-alt convention. |
| Refuted | Inconclusive | **Single-channel Refuted (pair-binned)**; Channel B deferred. |
| Inconclusive | Inconclusive | **Promote to L = 256** (if primary was L = 128) or **close arc at "Inconclusive — structural scale mismatch"** (if secondary). |
| Any | guardrail failure (§5.6) | **Inconclusive (L-larger-insufficient)**; promote or close per §5.6. |

---

## 7. Deliverables

- [x] Scoping memo (this document).
- [ ] Driver memo `theory/ED_SC_3_6_L_Larger_Driver.md`
  (forthcoming; will inherit F4-canonical and ED-SC 3.5
  driver specs with `fr.SIZE` override and three-channel
  output schema).
- [ ] Driver script `analysis/scripts/ed_sc_3_6_l_larger.py`
  (forthcoming).
- [ ] Execution artefacts under `outputs/ed_sc_3_6_l_larger/`
  (primary L = 128 run: `xi_field_profile.csv`,
  `xi_field_per_seed.csv`, `correlation_twopoint_table.csv`,
  `correlation_twopoint_per_seed.csv`, `summary.json`,
  `stdout.json`, `log`).
- [ ] Integration memo
  `theory/ED_SC_3_6_L_Larger_Integration.md`
  (post-execution synthesis; combined-verdict reconciliation
  per §6; updates GR-SC 1.0 §5 canonical-filter row pointer
  via forward reference from `GR_SC_1_8_PostF4_Consolidation.md`).

**Pre-registered closure scope.** ED-SC 3.6 closes when:
(a) the L = 128 execution produces a combined verdict per §6,
and (b) if Inconclusive on L = 128, either the L = 256 execution
produces a combined verdict *or* the arc closes at "Inconclusive —
structural scale mismatch" per §1.

**Wall estimate.** Single session on L = 128 (expected
≈ 400–900 s based on 64² wall × 4× area scaling for the
rate-limiting motif extraction). L = 256 secondary run would
add ≈ 2,000–4,000 s if promoted. Total arc wall budget:
≤ 6,000 s across both lattice sizes if both are executed.

**Changelog.**

- 2026-04-23 (seventeenth pass) — Initial draft. Pre-registers
  the L-larger follow-up as the single remaining internal path
  to test GR-SC 1.7 at the canonical operating point, with
  L = 128 primary and L = 256 optional secondary. Three-channel
  measurement (pair-binned F4, FFT mask-weighted, FFT bulk
  reference). Four-way per-channel verdict taxonomy with cross-
  channel reconciliation matrix (§6). Pre-registered success
  criteria explicitly distinguish absolute motif count (for
  pair-coincidence statistics) from mask density (lattice-
  independent). Arc closes with either a definitive canonical-
  filter verdict for GR-SC 1.7 or a permanent "Inconclusive —
  structural scale mismatch" entry that forces the next-pass
  arc to shift away from ED-SC 3.x Correlation-class tests
  on compute-accessible lattices.
