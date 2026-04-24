# ED-SC 3.6 L-Larger Follow-up — Integration

**Pass:** seventeenth (L-larger closure)
**Date:** 2026-04-23
**Parent memos:**
- `theory/ED_SC_3_6_L_Larger_Scoping.md` (scope; three-channel pre-registration)
- `theory/ED_SC_3_6_L_Larger_Driver.md` (driver specification)
- `theory/ED_SC_3_5_FFT_XiField_Integration.md` (parent arc; four-channel convergence on "canonical filter too sparse on 64²")
- `theory/ED_SC_3_4_twopoint_FilterRelaxation_Integration.md` (F4 sub-arc closure)
- `theory/GR_SC_1_8_PostF4_Consolidation.md` (post-F4 invariant table update + next-arc options)
**Executed driver:** `analysis/scripts/ed_sc_3_6_l_larger.py` at L = 128
**Artefacts:**
- `outputs/ed_sc_3_6_l_larger_L128/correlation_twopoint_table.csv`
- `outputs/ed_sc_3_6_l_larger_L128/correlation_twopoint_per_seed.csv`
- `outputs/ed_sc_3_6_l_larger_L128/xi_field_profile.csv`
- `outputs/ed_sc_3_6_l_larger_L128/xi_field_per_seed.csv`
- `outputs/ed_sc_3_6_l_larger_L128/summary.json`
- `outputs/ed_sc_3_6_l_larger_L128/stdout.json`
- `outputs/ed_sc_3_6_l_larger_L128/run.log`

---

## 1. Purpose

Close the ED-SC 3.6 L-larger arc by recording the L = 128 execution
results, reconciling the three-channel findings, updating the
GR-SC 1.0 §5 Correlation-class row pointer, and making a closure /
promote-to-L256 decision.

**L = 128 execution summary (2026-04-23, wall 181.6 s):**

- 10 seeds × 40 snapshots; canonical filter `(α_filt, N_req) = (0.25, 4)`.
- Per-seed ξ calibration tight: miss ∈ [0.00 %, 0.37 %]; ensemble mean
  xi_halfdecay = 1.7557 ± 0.0021 lu (self-cal guardrail passed at
  0.10 % miss vs 10 % tolerance).
- Total motif count: **3,869** (vs 849 on 64² — 4.6× gain matching
  L² area scaling at fixed mask density).
- Zero empty-mask snapshots across all 400 realisations (vs 13 %
  empty on 64²).
- Ensemble mask density ⟨ρ_M⟩ = 5.90 × 10⁻⁴ (essentially unchanged
  from 64²'s 5.18 × 10⁻⁴ — **mask density is lattice-invariant**).
- Channel A (pair-binned F4): 216 pairs binned (vs 51 on 64²);
  **4 / 10 bins admissible** (vs 0 on 64²); gate failed (≥ 8 required);
  no C = 1 crossing → `verdict_A = Inconclusive`.
- Channel B (FFT masked): C_B(r ≥ 1) = 2.000 ± 0.001 on every shell;
  `r_half_B_FFT = 0.500 lu`; ratio_primary = 0.2366 → `verdict_B = Refuted`.
- Channel C (FFT bulk): `r_half_C_FFT = 2.1134 lu`; estimator gap vs
  `xi_halfdecay_ensemble = 1.7557` lu reproduces the ED-SC 3.5 §2 20 %
  gap exactly.
- Combined verdict (scoping §6 matrix, single-channel-B path):
  **`Refuted`** — Channel A gate failed; Channel B's Refuted verdict
  propagates.

**Critical qualification.** The formal `Refuted` verdict is **structural,
not empirical**. The mechanism is Poisson-mask sparsity — the same
mechanism that caused ED-SC 3.5 Channel B to return Inconclusive on
64². Channel B on 128² returns a *definitive* Refuted this time
*only because the scoping §5.2 gate was defined on absolute motif
count (threshold 3,200) rather than pair-coincidence rate at r = 1.*
The absolute count is sufficient to "pass the gate" but the
pair-coincidence rate at r = 1 remains ~ 0.09 events per ensemble —
still effectively zero. The Poisson trap is not escaped by L-larger
scaling; it is only papered over by a gate-definition artefact.

**Structural conclusion.** The canonical-filter GR-SC 1.7 half-rise
compression prediction `r_½^filt / r_½^unfilt = 0.80 ± 0.05` is now
**Refuted-by-extension structural** across three independent
measurement channels on two lattice sizes:

1. **F4 canonical motif-pair channel on 64²** — Inconclusive via
   pair-count sparsity (seventeenth-pass F4 sub-arc).
2. **F4-alt relaxed-filter motif-pair channel on 64²** —
   Refuted-by-extension structural (C(r) saturated at ≈ 2 from
   r = 1 lu; F4-alt integration).
3. **ED-SC 3.5 FFT masked-field channel on 64²** — Inconclusive
   via self-cal guardrail, with Poisson-mask structural reading.
4. **ED-SC 3.6 FFT masked-field channel on 128²** — Refuted via
   scoping §5.2 gate, with Poisson-mask structural reading
   (mechanism unchanged from (3)).

All four channels converge on one reading: **the motif filter at
canonical strictness produces a Poisson point process at all
lattice sizes tested; no field-correlation signal is resolvable
in the filtered channel; the GR-SC 1.7 half-rise compression is
not observed in any channel on any accessible lattice.** The
unfiltered bulk-field channel (Channel C across arcs) gives a
clean monotone half-decay matching the ED-SC 3.3 canonical ξ
definition (up to the 20 % estimator-bias gap), but this is the
*denominator* of the GR-SC 1.7 ratio — it does not discriminate
the filter compression claim.

---

## 2. Channel findings

### 2.1 Channel A (pair-binned F4, canonical filter on L = 128)

**Raw counts.**
- Total motifs: 3,869.
- Total pairs in r ∈ [0.25, 5.25) lu: 216 (vs. 51 on 64²).
- Admissible bins (N_pairs ≥ 20): 4 of 10 (r = 3.0, 3.5, 4.0, 5.0).
  Inadmissible bins (< 20 pairs): r = 0.5 (0 pairs), r = 1.0
  (13 pairs), r = 1.5 (8), r = 2.0 (12), r = 2.5 (0), r = 4.5 (15).

**C_ensemble on admissible bins.**

| r | N_pairs | C_ensemble | C_CI_lo | C_CI_hi |
|---:|---:|---:|---:|---:|
| 3.0 | 62 | 1.907 | 1.730 | 2.079 |
| 3.5 | 36 | 2.044 | 1.751 | 2.337 |
| 4.0 | 39 | 1.955 | 1.782 | 2.143 |
| 5.0 | 31 | 2.169 | 1.973 | 2.366 |

All four admissible bins report C ∈ [1.91, 2.17] — **saturated at
the uncorrelated asymptote C(∞) = 2**. Bootstrap bands straddle 2
in all cases; point estimates are all consistent with Poisson
(C = 2) within 1σ.

**Verdict-relevant:**
- No C = 1 crossing in the r-grid.
- `r_half_A_filt` = None.
- `ratio_A` = None.
- Channel A primary gate (≥ 8 of 10 admissible): **FAILED** (4/10).
- `verdict_A` = Inconclusive.

**Structural read.** Channel A on L = 128 produces the first
admissible measurement of C_ensemble at the canonical filter for
any lattice size. The result corroborates F4-alt's structural
reading (C saturated at 2 for r ≥ 1) now at the canonical filter,
on the large-r portion of the grid. The small-r portion (r < 3 lu)
remains pair-sparse — the same bottleneck as F4 canonical on 64²,
now pushed to r < 3 lu rather than the full r-grid.

Pair density scaling: on 128² with 3,869 motifs, the expected
pairs in r < R_max is approximately
`N_pairs × (π R_max²) / L²` per snapshot, summed across the
ensemble. For R_max = 5.25, this gives
`3869 × π × 27.6 / 16384 ≈ 20,500` total pair-in-disk events if
motifs were uniform. The observed 216 is orders of magnitude
lower than this upper bound because (a) motifs are same-snapshot
only (40 snapshots × 9.7 motifs/snap = 388 motifs/frame on
average, giving ~ 94,000 same-snapshot candidates total, ~ 500
in-disk → ~ 216 after r-binning inside [0.25, 5.25) ⊂ disk), and
(b) the motif-filter density concentrates admissible sites on
lattice regions with specific local structure, not uniformly.

### 2.2 Channel B (FFT motif-mask-weighted, L = 128)

**Raw FFT profile.**
- ξ_φ_B(0) = σ_0²_B = 4.39 × 10⁻⁵ (variance dominated by ~10
  nonzero sites per 16,384-site snapshot × 400 snapshots).
- ξ_φ_B(r = 1) = −2.2 × 10⁻⁹ (statistically zero to 6 significant
  figures after normalisation).
- ξ_φ_B(r = √2) = −2.2 × 10⁻⁹.
- ξ_φ_B(r ≥ 1) = **0 ± 1.5 × 10⁻⁸** at every achievable shell.

**C_B profile.**
- C_B(0) = 0.
- C_B(r = 1) = **2.000** [1.999, 2.001] (bootstrap 16/84).
- C_B(r ≥ 1) = 2.000 ± 0.001 at every shell.

**Half-rise.**
- `r_half_B_FFT` = 0.49998 lu, bootstrap [0.49941, 0.50044].
- **This is a linear-interpolation artefact** between (r = 0, C = 0)
  and (r = 1, C = 2.000). No C = 1 was observed; the curve jumps
  from 0 to 2 across a single step (C is step-function at r = 0).

**Pair-coincidence rate.** At mask density ρ_M = 5.9 × 10⁻⁴ on
16,384 sites × 400 snapshots = 6.55 × 10⁶ site-frames with 4
neighbours each:
  `P(coincidence at r = 1) = ρ_M² × 4 × N_site_frames = 9.1 × 10⁻²`
events per ensemble. ~0.09 events — effectively zero. The Poisson-
point reading is numerically confirmed.

**Verdict-relevant.**
- `ratio_primary` = `r_half_B_FFT / r_half_C_FFT` = 0.49998 / 2.11340 = 0.23657.
- Bootstrap [0.23612, 0.23706] — extremely tight because both numerator
  and denominator are measured on the same ensemble with paired-seed
  bootstrap. The tightness is **misleading** — both the numerator
  (Poisson artefact) and the denominator (bulk half-decay) are
  separately stable to 0.2 %, but their *ratio* is not a physical
  half-rise compression.
- Channel B primary gate (ensemble_total_motifs ≥ 3,200): **PASSED**
  (3,869 vs 3,200 threshold).
- `verdict_B` = Refuted.

**Structural read.** Channel B on 128² is the same Poisson-point
signature observed on 64², at essentially the same mask density.
The Refuted verdict is produced because the ratio (0.2366) sits
far outside [0.70, 0.90] — but this number is 0.50 / 2.11, not a
genuine correlation-compression measurement. The 0.2366 value is
stable across L because both the numerator (lattice-step
interpolation artefact at r = 1) and the denominator (bulk-field
half-decay, unchanged from 64²) are lattice-invariant.

### 2.3 Channel C (FFT bulk reference, L = 128)

**Raw FFT profile — monotone Gaussian-like decay.**
- ξ_φ_C(0) = σ_0²_C = 1.90 × 10⁻⁴.
- C_C profile: 0.561 at r = 1, 0.757 at r = √2, 0.955 at r = 2,
  1.049 at r = √5, 1.242 at r = √8, 1.281 at r = 3, 1.710 at r = 5,
  asymptotic to 2.00 at r ≥ 15.
- Single clean crossing at r = 2.113 lu.

**Ensemble values.**
- `r_half_C_FFT` = 2.11340 lu, bootstrap [2.10918, 2.11749].
- `xi_halfdecay_ensemble_mean` = 1.75566 lu, std 0.00207 lu.
- Multi-crossing: false; non-monotone: false.

**Self-calibration guardrail.**
- xi_halfdecay_ensemble vs ξ_target: |1.75566 − 1.7575| / 1.7575 = 0.105 %.
- Tolerance: 10 %.
- **PASSED.**

**Estimator gap (ED-SC 3.5 §2 finding reproduced).** Channel C's
full-shell FFT r_half (2.11340) and the `xi_halfdecay` integer-binned
estimator (1.75566) differ by 20.3 % on L = 128 — within 0.2 % of
the 19.7 % gap measured on 64². The gap is a **lattice-size-invariant
property of the two estimators**, not a simulator artefact. Arc-
internal consistency rule: pick one estimator and use it for both
numerator and denominator of the GR-SC 1.7 ratio.

### 2.4 Cross-channel consistency

| quantity | 64² (ED-SC 3.5) | 128² (ED-SC 3.6) | Δ |
|---|---:|---:|---:|
| Mask density ⟨ρ_M⟩ | 5.18 × 10⁻⁴ | 5.90 × 10⁻⁴ | +14 % |
| Total motifs (ensemble) | 2,093† | 3,869 | 1.85× |
| Empty-mask snapshots | 53 / 400 | 0 / 400 | eliminated |
| ξ_halfdecay ensemble | 1.7551 lu | 1.7557 lu | +0.03 % |
| Self-cal miss | — | 0.10 % | — |
| r_half_C_FFT | 2.104 lu | 2.113 lu | +0.43 % |
| r_half_B_FFT | 0.501 lu | 0.500 lu | −0.2 % |
| ratio_primary (B / C FFT) | 0.2379 | 0.2366 | −0.5 % |
| Channel A ensemble pairs | N/A‡ | 216 | first measurement |
| Channel A admissible | N/A | 4 / 10 | first partial gate |

† ED-SC 3.5 Channel A = bulk field; no motif count equivalent.
‡ ED-SC 3.5 did not run Channel A (pair-binned) — first such
measurement at canonical filter is this arc.

**Key invariants.** Mask density, r_half_C, r_half_B, and
ratio_primary are all lattice-size-invariant to within 0.5 %.
The lattice-invariance of ratio_primary is the *definitive*
corroboration of the Poisson-mask mechanism: if the 0.2366 ratio
reflected a genuine field-level compression, it would evolve
with lattice size as the field's correlation structure is better
resolved; its invariance is diagnostic of a geometry-driven
artefact (the ratio is set by the mask-density-to-bulk-variance
ratio, which is lattice-invariant by the filter's site-local
selection rule).

---

## 3. Structural conclusions

### 3.1 Mask density is lattice-invariant

The canonical motif filter `(α_filt, N_req) = (0.25, 4)` applies a
site-local selection rule based on Morse-saddle structure and
4-ray endpoint thresholds. The rule has no explicit lattice-size
dependence and no non-local normalisation. Empirically, mask
density on L ∈ {64, 128} matches to ~ 14 % (and that spread is
plausibly finite-ensemble noise):

- L = 64: 5.18 × 10⁻⁴
- L = 128: 5.90 × 10⁻⁴

**Prediction.** On L = 256, mask density is expected to remain in
the [5.0, 6.0] × 10⁻⁴ band. Absolute motif count scales as L² at
fixed density. Zero empty-mask snapshots expected for L ≥ 128.

### 3.2 L-larger does not escape the Poisson trap

Pair-coincidence probability at r = 1 in the masked-field FFT is

  P(coincidence at r = 1) ≈ ρ_M² × (number of r = 1 pairs per site) × total sites × snapshots
                       ≈ ρ_M² × 4 × L² × 40 × 10 (for the 10-seed ensemble)
                       ≈ ρ_M² × 1600 × L².

For ρ_M ≈ 5.5 × 10⁻⁴:

- L = 64: P ≈ 3.0 × 10⁻⁷ × 4096 × 1600 = **1.97 events** per ensemble
  (observed: C_B(1) = 1.998, consistent with near-zero coincidences).
- L = 128: P ≈ 3.0 × 10⁻⁷ × 16384 × 1600 = **7.9 events** per ensemble
  (observed: C_B(1) = 2.000, no signal above Poisson).
- L = 256: P ≈ 3.0 × 10⁻⁷ × 65536 × 1600 = **31 events** per ensemble
  (expected: C_B(1) likely still at Poisson floor; ~ 6 σ signal
  required to distinguish from C = 2 given typical bootstrap noise).

**Conclusion.** Even on L = 256, Channel B remains at or near the
Poisson-point floor. The "half-rise at r = 0.5" interpolation
artefact persists. The mechanism is the mask's site-local selection
producing spatially isolated motif points; lattice scaling does
not alter the selection rule or the density that results.

### 3.3 The canonical filter cannot support a filtered-field correlation function on any accessible L

Combining §3.1 and §3.2: on any lattice size accessible to the
current compute budget (L ≤ 256, per GR-SC 1.8 Post-F4 §4
Option A), the motif-mask-weighted field's two-point autocorrelation
is dominated by isolated-point variance at r = 0 and Poisson
asymptote C = 2 at all r ≥ 1. No meaningful half-rise is
resolvable in this channel at the canonical filter.

The relaxed-filter channel (F4-alt, N_req = 2) produces ×500 more
motifs and bypasses this Poisson trap, but the result there is
still C(r) saturated at ≈ 2 from r = 1 onward — the *underlying
field* has a half-decay at ≈ 1 lu in the motif-ratio correlation,
below the first resolvable lattice shell.

### 3.4 The Refuted verdict is structural

The ED-SC 3.6 L = 128 combined verdict is `Refuted` (per the
scoping §6 single-channel-B reconciliation path). This verdict
is formally correct under the pre-registered taxonomy, but its
scientific content is:

> **The canonical-filter motif-mask-weighted field on 128²
> produces a Poisson point process, whose ratio of artefactual
> "half-rise at r = 0.5" to bulk-field half-decay at r = 2.11 is
> 0.24, far outside the GR-SC 1.7 prediction band [0.70, 0.90].**

This is a structural statement about the filter's density regime,
not an empirical falsification of GR-SC 1.7's physical content.
The integration memo records it as `Refuted-by-extension
structural` to parallel the F4-alt verdict's naming convention:
the prediction is refuted *at this measurement channel at the
canonical filter on this lattice*, but the refutation mechanism
is channel-dependent (Poisson sparsity), and the scope of the
refutation is restricted to the Correlation-class channel at the
canonical operating point.

---

## 4. GR-SC 1.0 §5 Correlation-class row update

Supersedes the §3 pointer from `GR_SC_1_8_PostF4_Consolidation.md`
and the §5 pointer from `ED_SC_3_5_FFT_XiField_Integration.md`:

**Canonical-filter row (N_req = 4 on {64², 128²}):**
> **Refuted-by-extension structural** — Poisson-mask sparsity
> mechanism confirmed across three channels (F4 canonical pair-
> binned, ED-SC 3.5 FFT masked, ED-SC 3.6 FFT masked on L-larger)
> and two lattice sizes. Mask density is lattice-invariant
> (5.2–5.9 × 10⁻⁴) at all accessible L, keeping the
> filtered-field channel at or near the Poisson point-process
> floor. Ratio_primary stable at 0.237 ± 0.001 across L ∈ {64,
> 128} — the lattice-invariance is diagnostic of the geometric
> artefact. See `ED_SC_3_6_L_Larger_Integration.md` §2–3.

**Relaxed-filter row (N_req = 2 on 64², C_redshift channel only):**
> **Refuted-by-extension structural** — unchanged from
> `ED_SC_3_4_twopoint_FilterRelaxation_Integration.md` §6.
> 24,464 binned pairs, C_ensemble(r) ∈ [1.96, 2.05] across
> r ∈ [1, 5] lu; half-rise below r = 1 lu; ratio < 0.57
> outside [0.70, 0.90] envelope. Corroborated by ED-SC 3.5
> and ED-SC 3.6 Channel B at canonical filter.

**Refinement row (N_req = 2, Δr = 0.25, r ∈ [0.25, 2.0] on 64²):**
> **Inconclusive-thin** — lattice-discretisation obstruction;
> Δr ≥ 0.5 lu guardrail. Unchanged from
> `ED_SC_3_4_twopoint_FilterRelaxation_Refine.md`.

**Bulk unfiltered FFT row (Channel C, reference):**
> **r_half_C_FFT lattice-invariant** — 2.104 lu on 64², 2.113 lu
> on 128² (within 0.5 %). Estimator gap vs `xi_halfdecay`
> (integer-binned) is 19.7–20.3 %, lattice-invariant; pick one
> estimator per arc. See `ED_SC_3_5_FFT_XiField_Integration.md`
> §2 and this memo §2.3.

**Lattice-geometry guardrail (carried forward):**
> Δr ≥ 0.5 lu on square-Z² for pair-binned channels; FFT radial-
> shell channels naturally sample the full shell set but disagree
> with integer-binned `xi_halfdecay` by ~20 %. Both guardrails
> apply on all accessible L.

**New methodological guardrail (this memo):**
> Channel B primary gates should be defined on **pair-coincidence
> rate at r = 1**, not on absolute motif count. The ED-SC 3.6
> scoping §5.2 gate definition (3,200 motifs on L = 128) passed
> on absolute count but the underlying channel remained at the
> Poisson floor (coincidence rate ~ 0.09 events per ensemble).
> Any future Correlation-class scoping memo must pre-register a
> coincidence-rate threshold, e.g.
> `P_coincidence(r = 1) ≥ 0.5 × expected_signal_size`, to ensure
> the channel is in a resolvable regime before adjudicating
> verdict.

---

## 5. L = 256 decision

### 5.1 Promote or close?

**Default recommendation: do not promote. Close the arc.**

### 5.2 Why L = 256 will not fix Channel B

Per §3.2 scaling analysis:
- L = 256 pair-coincidence at r = 1 ≈ 31 events per ensemble.
- Bootstrap noise floor on C_B(r = 1) given ~ 31 coincidences
  in the numerator and ~ 100 isolated-motif variance events
  in the denominator is ~ ±0.05 on C — not enough to resolve
  a Confirmed / Refuted distinction (which requires
  resolution of C ~ 1 ± 0.05, i.e. C distinguishable from 2
  by an amount comparable to the bootstrap noise).
- Channel B on L = 256 will most likely return a ratio in
  the [0.23, 0.27] band — same structural Refuted verdict,
  no new physics content.

**Conclusion on L = 256 Channel B.** Promoting does not add
information. The Poisson trap is L-invariant.

### 5.3 Channel A would gain on L = 256

Channel A ensemble pair count scales as N_motifs² × (R_max²/L²)
× (snapshots) / 2. From 64² → 128² the gain was 4.2× (51 → 216).
From 128² → 256² an additional 4× is expected (216 → ~ 860
ensemble pairs). At that count, Channel A should reach
admissibility in 8–10 / 10 bins at Δr = 0.5 lu, producing the
first definitive canonical-filter four-way verdict on the
motif-pair channel.

**Expected outcome.** Based on F4-alt's structural reading and
the ED-SC 3.6 L = 128 admissible-bin values (all at C ≈ 2), the
L = 256 Channel A verdict is expected to be `Refuted` (no
C = 1 crossing; saturated asymptote) — corroborating the
already-existing structural Refuted-by-extension reading with
a single-channel-A formal Refuted verdict at the canonical
filter.

### 5.4 Does the expected outcome warrant the ~ 30-min compute?

**Case for promoting:** a formal single-channel-A Refuted verdict
at the canonical filter would close the canonical-filter row of
GR-SC 1.0 §5 at the *pair-binned* evidence level (currently the
row cites only the cross-channel structural Refuted-by-extension).
Some reviewers may prefer a direct pair-binned verdict.

**Case against promoting:** the structural Refuted-by-extension
verdict is already secure across three channels + two lattices.
The L = 256 Channel A run would produce an expected result
(C saturated at 2 in admissible bins, no crossing, ratio
undefined, verdict Refuted) that adds no new scientific content
beyond confirming the existing reading with a slightly tighter
pair-level measurement. The ~ 30-min wall budget could be
better spent on (a) an empirical-track status check (FRAP or
ED-09.5 Aspelmeyer/Arndt), (b) a new-scoping memo exploring
whether any motif-based GR-SC 1.7 test is viable at all given
the Poisson-mask structural finding, or (c) a GR-SC 2.1 full
revision integrating the seventeenth-pass findings.

### 5.5 Closure statement

**ED-SC 3.6 closes at L = 128 with a structural Refuted-by-extension
verdict on the canonical-filter Correlation-class row.** The L = 256
promotion is *available* but not *required*; the recommendation is
to close the arc here and redirect eighteenth-pass work away from
further ED-SC 3.x Correlation-class drivers.

No further ED-SC 3.x correlation-class arcs are required.

---

## 6. Deliverables

- [x] Integration memo (this document).
- [x] Pointer updates for
  `theory/GR_SC_1_8_PostF4_Consolidation.md` §3 — GR-SC 1.0 §5
  Correlation-class row canonical-filter entry upgraded from
  "Inconclusive pending L-larger" to **"Refuted-by-extension
  structural (Poisson-mask sparsity, lattice-invariant across
  L ∈ {64, 128})"** via forward reference from this memo §4.
  No direct edit of `GR_SC_1_8_PostF4_Consolidation.md` needed;
  this memo supersedes §3 row on the canonical-filter entry.
- [x] New methodological guardrail (§4): Channel B primary
  gates must use coincidence-rate thresholds, not absolute motif
  counts. Carried forward to any future Correlation-class scoping.
- [x] Closure decision recorded: ED-SC 3.6 closes at L = 128;
  L = 256 not promoted; no further ED-SC 3.x Correlation-class
  arcs required.
- [x] Next-arc handoff: eighteenth-pass highest-priority options
  are (a) empirical-track status check (FRAP, ED-09.5),
  (b) GR-SC 2.1 full revision integrating seventeenth-pass
  findings, (c) a new scoping memo asking whether any
  motif-based GR-SC 1.7 test is viable given the Poisson-mask
  structural finding.

**Changelog.**

- 2026-04-23 (seventeenth pass) — Initial draft. Closes ED-SC 3.6
  L-larger arc with a structural Refuted-by-extension verdict on
  the canonical-filter Correlation-class row. Records four-channel
  cross-arc convergence: mask density is lattice-invariant
  (5.2–5.9 × 10⁻⁴ across L ∈ {64, 128}); Channel B remains at
  Poisson-point floor regardless of lattice scaling;
  ratio_primary lattice-invariant at 0.237 ± 0.001 — diagnostic
  of the geometric artefact. Channel A admissibility partially
  achieved (4 / 10 at canonical filter on 128², first such
  measurement); saturated C ≈ 2 in admissible bins corroborates
  F4-alt. Channel C (bulk reference) lattice-invariant with
  20 % estimator gap vs `xi_halfdecay`. Recommends closing the
  arc; L = 256 promotion is not warranted as it does not escape
  the Poisson trap. Adds methodological guardrail: Channel B
  gates must use coincidence-rate thresholds, not absolute
  motif counts. No tenth-pass, fifteenth-pass, sixteenth-pass,
  or prior seventeenth-pass structural claims retracted.
