# ED-SC 3.5 FFT-Based Field Autocorrelation — Integration

**Pass:** seventeenth (post-F4 checkpoint; ED-SC 3.5 closure)
**Date:** 2026-04-23
**Parent memos:**
- `theory/ED_SC_3_5_FFT_XiField_Scoping.md` (scope + primary-channel pinning)
- `theory/ED_SC_3_5_FFT_XiField_Driver.md` (driver specification)
- `theory/ED_SC_3_4_twopoint_FilterRelaxation_Integration.md` (F4 sub-arc closure)
- `theory/GR_SC_1_8_PostF4_Consolidation.md` (post-F4 invariant-table update + next-arc options)
**Executed driver:** `analysis/scripts/ed_sc_3_5_fft_xi_field.py`
**Artefact:** `outputs/ed_sc_3_5_fft_xi_field/xi_field_summary.json`
           `outputs/ed_sc_3_5_fft_xi_field/xi_field_profile.csv`
           `outputs/ed_sc_3_5_fft_xi_field/xi_field_per_seed.csv`
           `outputs/ed_sc_3_5_fft_xi_field/xi_field.stdout.json`
           `outputs/ed_sc_3_5_fft_xi_field/xi_field.log`

---

## 1. Purpose

Close the ED-SC 3.5 FFT-based bulk-field autocorrelation arc by
integrating its executed results with the seventeenth-pass F4 sub-arc
closure, recording the two structural findings that emerged, and
updating the GR-SC 1.0 §5 authoritative invariant-table pointer for
the `C_redshift(r)` Correlation-class row.

**Execution summary (2026-04-23):** 10 seeds × 40 snapshots, canonical
ξ_target = 1.7575 lu (per-seed miss ≤ 0.57 %), canonical motif filter
(α_filt = 0.25, N_req = 4). Wall = 54.3 s. 338 Z² shell radii measured.
Bulk-field half-rise r_½^A = 2.104 ± 0.012 lu (bootstrap 16/84).
Masked-field half-rise r_½^B = 0.501 ± 0.001 lu. Ratio
r_½^B / r_½^A = 0.238 ± 0.002. **Formal four-way verdict:
`Inconclusive`** (self-calibration guardrail triggered at 19.7 %
miss vs 10 % tolerance).

**Two structural findings** emerged beneath the guardrail and are
the substantive content of this arc:

(a) **~20 % estimator-dependence** between the integer-binned
`xi_halfdecay` function (which defines the canonical ξ = 1.7575 lu)
and the full-shell FFT radial-average r_½^A = 2.104 lu. Same field;
two coarse-grainings. Not a simulator bug; a methodological
multiplicity that future arcs must pick a side on.

(b) **Motif-mask Poisson sparsity.** The canonical filter admits
≈ 2.1 motifs / snapshot on a 4,096-site 64² lattice (mean mask
density ⟨ρ_M⟩ = 5.18 × 10⁻⁴). The masked field's autocorrelation
jumps from C = 0 at r = 0 to C ≈ 2 at r = 1 lu, with no resolvable
correlation length — a Poisson point-process signature, not a
field correlation.

**Consequence.** The FFT channel, at the canonical filter on 64²,
*does not meaningfully test* the GR-SC 1.7 half-rise compression
prediction `r_½^filt / r_½^unfilt = 0.80 ± 0.05`. Its verdict
converges structurally on the F4 sub-arc verdict: the canonical
filter is too sparse on 64² to support a Correlation-class
measurement in any channel yet tried. GR-SC 1.7 remains untestable
at the canonical operating point on this lattice.

---

## 2. Bulk-field channel (A) findings

### 2.1 Measurement

- `r_half_central` = 2.10406 lu
- `r_half_bootstrap_16_84` = [2.09230, 2.11564] lu (4000 seed-bootstrap
  resamples; 100 % valid)
- `multi_crossing_flag` = false; `non_monotone_flag` = false
- `all_crossings` = [2.104056] (single clean crossing)
- C_A is monotone-increasing from 0 at r = 0 through 0.567 at r = 1,
  0.764 at r = √2, 0.959 at r = 2, 1.053 at r = √5, rising
  asymptotically to C_A(r ≥ 15) ≈ 2.01. Textbook Gaussian-like
  autocorrelation profile.

### 2.2 Self-calibration guardrail failure

- ξ_canonical = 1.75753 lu (`xi_halfdecay` 10-seed ensemble mean;
  ED-SC 3.1 rev. 3 certification artefact
  `outputs/ed_sc_3_1/xi_canonical.json`).
- r_half_A = 2.104 lu.
- Miss fraction = |2.104 − 1.7575| / 1.7575 = 0.1972 (19.7 %).
- Guardrail tolerance (ED-SC 3.5 scoping §4) = 10 %.
- **Verdict: guardrail failed.** Formal four-way verdict declared
  Inconclusive per §3.6 of the driver.

### 2.3 Interpretation: estimator mismatch, not simulator error

The discrepancy is real and structural, but reflects the two
functions binning lattice-shell radii differently:

- **`xi_halfdecay`** (the ED-SC 3.3 definition of ξ, used to
  certify ξ_canonical): integer-bins radial distances,
  `r = int(√(Δy² + Δx²))`. The r = 1 bin contains *all* sites with
  integer-floor distance 1, i.e. shells {1.0, √2 ≈ 1.414,
  √3 ≈ 1.732}. These are averaged *before* the half-decay interp.
- **FFT radial-shell**: keeps every achievable squared-radius
  distinct. Shells {1.0, √2, 2, √5, √8, 3, √10, …} each carry
  their own ξ_φ value.

Because ξ_φ is monotone-decreasing in r, the integer-binned
average of shells {1.0, √2, √3} at the r = 1 bin is *lower*
than ξ_φ(1) alone. This compresses the effective small-r profile,
pulling `xi_halfdecay`'s half-decay estimate inward. The FFT
full-shell r_½ is systematically larger, by the ~20 % seen here,
for any field with monotone-decreasing ξ_φ and sufficient small-r
sampling.

**Neither is "correct"**; they are two estimators of the same
underlying half-decay length that disagree by a multiplicative
bias determined by the shell-binning rule. The F4 sub-arc's
pair-binning channel (Δr = 0.5 lu) sits at an intermediate
coarse-graining and will carry its own bias.

### 2.4 Methodological implication

> **Guardrail (forward-carried to eighteenth-pass work).** Within
> any single arc, pick one half-decay estimator (integer-bin
> `xi_halfdecay`, full-shell FFT, or pair-binned F4) and *do
> not* compare r_½ values across estimators numerically. The
> ratio `r_½^filt / r_½^unfilt` is meaningful only when both
> numerator and denominator are measured by the *same*
> estimator on the *same* channel.

The ED-SC 3.5 self-calibration check is the first test that
forced this guardrail to surface explicitly. Its value is
preserving the 19.7 % finding as a durable methodological
constraint, not as a simulator failure.

---

## 3. Masked-field channel (B) findings

### 3.1 Measurement

- `r_half_central` = 0.50059 lu
- `r_half_bootstrap_16_84` = [0.49989, 0.50129] lu
- `multi_crossing_flag` = false; `non_monotone_flag` = false
- `all_crossings` = [0.500589] (single crossing — but see §3.3)
- `mean_mask_density_ensemble` = 5.18 × 10⁻⁴
- 53 of 400 snapshots had zero motifs admitted (13 % empty frames)

### 3.2 C_B shape

- C_B(0) = 0 (by construction, σ_0² normalisation).
- C_B(r = 1) = 1.998 [1.995, 2.000] (bootstrap band).
- C_B(r ≥ 1) = 2.000 ± 0.002 at every admissible shell.

Linear interpolation between (0, 0) and (1, 1.998) returns r = 0.501
as the "C = 1 crossing". No meaningful intermediate shells exist
between r = 0 and r = 1 on Z² (the next achievable radius is
exactly r = 1).

### 3.3 Interpretation: Poisson point process, no correlation length

Mask density ⟨ρ_M⟩ = 5.18 × 10⁻⁴ means ~ 2.1 motifs per snapshot
on 4,096 sites. The probability that *two neighbouring sites*
(4 neighbours at r = 1) both carry motifs is approximately
(ρ_M)² = 2.7 × 10⁻⁷, which on 40 × 10 = 400 snapshots averages
to ~4 × 10⁻⁴ expected pair-coincidences — statistically zero.

Consequently ξ_φ_B(r = 1) is driven entirely by isolated-motif
variance contributions that vanish in the cross-site product,
giving ξ_φ_B(1) / σ_0²_B ≈ 0 and thus C_B(1) ≈ 2. The same
holds at every r > 0.

**The r_½^B = 0.5 lu "half-rise" is a linear-interpolation
artefact between two shells with no intermediate data.** It does
not represent a physical correlation length; it represents the
mid-point of an unresolved step discontinuity.

A field that contains isolated point-like excitations (a Poisson
point process in the limit of vanishing density) has, by
construction, C(r) = 2 for all r > 0 — it is "uncorrelated
beyond r = 0". The motif-mask filter on the canonical operating
point produces this limit, not because the underlying p-field is
uncorrelated (it is not — see Channel A's clean monotone decay)
but because the filter admits so few sites that the pair-
coincidence probability is negligible.

### 3.4 Convergence with F4-alt

The F4-alt (N_req = 2) relaxed-filter motif-pair channel found
C(r) ∈ [1.96, 2.05] for every admissible bin r ∈ [1, 5] lu. The
ED-SC 3.5 FFT Channel B (N_req = 4) finds C(r) = 2.00 ± 0.002
at every admissible shell r ≥ 1 lu. Both channels, at their
respective filter strictnesses, converge on **"motif-conditioned
correlations are at the uncorrelated asymptote from r = 1 lu
onward on 64²"**. This is the substantive corroboration between
channels; see §4.

---

## 4. Cross-channel reconciliation with F4

### 4.1 The reconciliation matrix (scoping §5)

| FFT verdict | F4 verdict | Combined interpretation |
|---|---|---|
| Inconclusive (self-cal failed + mask Poisson) | Refuted-by-extension structural (F4-alt, relaxed filter) | **This pass.** Two independent channels both find motif-conditioned correlation at C ≈ 2 across all r ≥ 1 lu; the half-rise (if any) lies below the first achievable lattice shell. The FFT self-cal miss reveals the estimator-dependence, not a disagreement. |

The scoping-memo reconciliation matrix had pre-registered four
cases; this pass falls into a fifth case not explicitly tabulated
("FFT Inconclusive via self-cal / Poisson; F4-alt Refuted-by-extension"),
which is best read as a *soft corroboration*: the FFT channel does
not contradict F4-alt, and the mechanism (mask sparsity preventing
any channel from resolving a sub-1 lu half-rise) is the same in
both.

### 4.2 Unified conclusion

> **The canonical operating point `(α_filt, N_req) = (0.25, 4)`
> is too sparse on 64² for any channel — motif-pair binning
> (F4), motif-pair refinement (F4-alt-refine), bulk-field FFT
> (ED-SC 3.5 Channel A masked), or relaxed-filter motif-pair
> binning (F4-alt, N_req = 2) — to resolve a sub-1-lu
> half-rise. The GR-SC 1.7 half-rise compression prediction
> `r_½^filt / r_½^unfilt = 0.80 ± 0.05` is untestable at the
> canonical filter on the 64² square-Z² lattice.**

### 4.3 What each channel *does* tell us

- **Channel A (bulk unfiltered FFT)**: the bulk p-field has a
  clean monotone Gaussian-like ξ_φ(r) with full-shell half-decay
  2.10 lu (equivalent to `xi_halfdecay` 1.76 lu after the 20 %
  estimator shift). This is the denominator of the GR-SC 1.7
  ratio if we ever obtain a meaningful numerator.
- **F4 canonical (N_req = 4, motif-pair)**: pair-density sparsity
  at 51 binned pairs across 10 r-bins at Δr = 0.5 lu; Inconclusive.
- **F4-alt (N_req = 2, motif-pair)**: 24,464 pairs, 8/10
  admissible, C(r) saturated at ≈ 2 from r = 1 lu; strictly
  Inconclusive, structurally Refuted-by-extension in the relaxed-
  filter channel.
- **F4-alt-refine (N_req = 2, Δr = 0.25)**: 3/8 admissible, lattice-
  discretisation obstruction; Inconclusive-thin; admissible bins
  corroborate F4-alt.
- **Channel B (masked FFT, N_req = 4)**: mask too sparse for
  field-correlation signal; C_B(r) = 2 for all r ≥ 1 lu
  (Poisson-point-process signature).

Four channels, one convergent structural reading.

---

## 5. GR-SC 1.0 §5 Correlation-class row — pointer update

The `C_redshift(r)` row of the GR-SC 1.0 §5 authoritative invariant
table is updated by pointer (no direct table reformat), superseding
the pointer written in `GR_SC_1_8_PostF4_Consolidation.md` §3 with
the FFT corroboration folded in:

**Canonical-filter row (N_req = 4 on 64²):**
> **Inconclusive** — untestable on 64² due to motif-mask sparsity.
> Pair-density channel (F4, 51 binned pairs / 10 bins) and
> bulk-FFT masked channel (Channel B, mask density 5.18 × 10⁻⁴,
> C_B(r ≥ 1) = 2.00 ± 0.002) both fail to resolve a sub-1-lu
> half-rise. See `ED_SC_3_5_FFT_XiField_Integration.md` §4.

**Relaxed-filter row (N_req = 2 on 64², C_redshift channel only):**
> **Refuted-by-extension structural** — 24,464 binned pairs,
> C_ensemble(r) ∈ [1.96, 2.05] across r ∈ [1, 5] lu; any half-rise
> must lie at r < 1 lu, giving ratio < 0.57 outside the
> [0.70, 0.90] envelope. Corroborated by FFT Channel B at the
> canonical filter (same asymptote). See
> `ED_SC_3_4_twopoint_FilterRelaxation_Integration.md` §6.

**Refinement row (N_req = 2, Δr = 0.25, r ∈ [0.25, 2.0]):**
> **Inconclusive-thin** — lattice-discretisation obstruction:
> Δr = 0.25 leaves 5/8 bins empty by construction on square-Z².
> Guardrail Δr ≥ 0.5 lu on 64² documented.
> See `ED_SC_3_4_twopoint_FilterRelaxation_Refine.md` and
> `GR_SC_1_8_PostF4_Consolidation.md` §2.

**Bulk unfiltered FFT row (Channel A, new):**
> **Reference denominator** for any future ratio measurement —
> r_½^A = 2.104 ± 0.012 lu (full-shell FFT) or 1.758 lu
> (integer-binned `xi_halfdecay`). Self-cal guardrail triggered
> at 19.7 % estimator mismatch; the two estimators are not
> numerically interchangeable. Within-arc rule: pick one
> estimator and use it for both numerator and denominator.
> See `ED_SC_3_5_FFT_XiField_Integration.md` §2.

**Lattice-geometry guardrail** (carried forward from F4-alt-refine
and corroborated by ED-SC 3.5 shell structure):
> Δr ≥ 0.5 lu is the minimum admissible bin-width for any
> pair-binned Correlation-class measurement on 64² square-Z²;
> any FFT radial-shell measurement on the same lattice naturally
> samples the full achievable shell set {1, √2, 2, √5, √8, 3, …}
> without this constraint but will *differ in half-decay numerical
> value* from the integer-binned estimator by a systematic
> ~20 % shift.

---

## 6. Next arc recommendation

**Option A (L-larger, 128² or 256²) is now promoted to the single
remaining path** to test GR-SC 1.7 at the canonical filter. Option B
(direct FFT ξ_φ(r)) was the cheap cross-check and is now executed;
its outcome — "canonical filter too sparse for meaningful Channel B"
— is the structural corroboration of F4, not an independent
refutation. Option C (empirical tracks) remains valid as a parallel,
non-compute activity.

**Why L-larger is now the only internal path:**

On 128², the mask density at fixed filter strictness is expected to
scale linearly in lattice area (same selection rule, more sites):
⟨ρ_M⟩ ≈ 5 × 10⁻⁴ still, but absolute motif count per snapshot
rises from ~ 2.1 on 64² to ~ 8.5 on 128² (4× area). Pair-coincidence
probability at r = 1 scales as (motif_count/N_sites)² × N_sites =
motif_count²/N_sites, which on 128² gives ≈ 8.5²/16384 ≈ 0.004 pair-
coincidences per snapshot — still sparse but measurable at the
ensemble level across 400 snapshots (~ 2 pair events). On 256²,
motif count ≈ 34 per snapshot, pair-coincidence ≈ 0.018 per
snapshot, ≈ 7 events per 400-snapshot ensemble.

At 256², Channel B of an analogous FFT driver would resolve
small-r correlation structure *if it exists*, with enough
coincidences to distinguish C(r) = 2 (Poisson) from C(r) = 2 − ε
(weakly correlated). The F4 pair-binning channel on 256² would
also see ~ 7 × 28,000 ≈ 200,000 pair candidates / 10 r-bins at
Δr = 0.5 lu, ~ 4,000 pairs/bin — well above the 20-pair admissibility
gate by two orders of magnitude.

**Recommended closure:**

ED-SC 3.5 closes this pass with a **structural verdict**:

> **Canonical filter too sparse on 64² for any Correlation-class
> channel; FFT corroborates F4.** GR-SC 1.7 half-rise compression
> prediction is untestable at the canonical operating point on
> this lattice. The L-larger follow-up (128² or 256², paired
> with ξ rescaling) is the single remaining internal path to
> definitive verdict; executing it is the eighteenth-pass
> highest-priority theoretical task.

---

## 7. Deliverables

- [x] Integration memo (this document).
- [x] Pointer update for `GR_SC_1_8_PostF4_Consolidation.md` §3
  (GR-SC 1.0 §5 Correlation-class row now carries four pointer
  rows: canonical, relaxed, refinement, and bulk-unfiltered FFT
  reference; see §5 above). No direct edit required — this memo
  supersedes §3 of the Post-F4 Consolidation for the Correlation-
  class row via forward reference.
- [x] Durable seventeenth-pass finding carried forward to memory:
  **20 % estimator-dependence between `xi_halfdecay` and full-shell
  FFT r_½** is a new methodological guardrail (§2.4 above). Within-
  arc consistency rule: one estimator per arc.
- [x] No driver changes required. The ED-SC 3.5 driver executed
  cleanly, reported its structural findings, and is closed.
- [x] Next-arc pointer: Option A (L-larger) promoted as single
  remaining internal closure path for the canonical-filter
  Correlation-class row.

**Changelog.**

- 2026-04-23 (seventeenth pass) — Initial draft. Closes ED-SC 3.5
  as a "structural corroboration of F4" rather than an independent
  falsifier. Records the two durable findings: (a) 20 % estimator-
  dependence (`xi_halfdecay` vs full-shell FFT); (b) canonical
  motif-mask Poisson sparsity (⟨ρ_M⟩ = 5.18e-04 on 64² gives
  C_B(r ≥ 1) = 2.00 ± 0.002 by point-process statistics, not by
  field decorrelation). Cross-channel reconciliation with F4
  sub-arc: four channels converge on "canonical filter too sparse
  on 64²". Promotes L-larger as the only remaining path to test
  GR-SC 1.7 at the canonical filter. No structural claims from
  the tenth-pass, fifteenth-pass, sixteenth-pass, or seventeenth-
  pass F4 arc are retracted.
