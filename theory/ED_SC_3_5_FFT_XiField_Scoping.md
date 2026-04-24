# ED-SC 3.5 FFT-Based Field Autocorrelation — Scoping

**Pass:** seventeenth (post-F4 checkpoint; new ED-SC 3.5 arc)
**Date:** 2026-04-23
**Parent memos:**
- `theory/GR_SC_1_8_PostF4_Consolidation.md` §4 Option B
- `theory/GR_SC_2_0_Consolidation.md` §7 (GR-SC 1.7 tenth-pass derivation)
- `theory/GR_SC_1_0_MotifCurvatureInvariants.md` §5 (authoritative invariant table, C_redshift row)

---

## 1. Purpose

Pre-register a **field-level autocorrelation measurement** of the
half-rise compression prediction that the seventeenth-pass F4 sub-arc
tested in the motif-ratio pair channel. This is an **independent
falsifier** of the tenth-pass GR-SC 1.7 prediction
`r_½^filt / r_½^unfilt = 0.80 ± 0.05`, using a measurement channel
that bypasses motif-pair binning and the square-Z² lattice-shell
gap floor.

**Primary object.** The bulk scalar two-point autocorrelation

  ξ_φ(r) = ⟨ φ(x) φ(x+r) ⟩ − ⟨φ⟩²

sampled via FFT on 64² periodic realisations at canonical ξ =
1.7575 lu, with r radially averaged on the lattice. The derived
quantity

  C_redshift(r) = 2 · [ 1 − ξ_φ(r) / σ_0² ]

(where σ_0² = ξ_φ(0) = Var φ) is the tenth-pass GR-SC 1.7
observable. The half-rise is the smallest r ≥ 0 at which
C_redshift(r) = 1, equivalently `ξ_φ(r) / σ_0² = 0.5`
(half-decay of the normalised autocorrelation).

**Why this is an independent test.** GR-SC 1.7's derivation
operates on a continuous field — the two-point correlator of
a bulk scalar. The F4 sub-arc projected this onto a
motif-ratio pair channel (Pearson/Spearman correlation of
`ρ` between motif points separated by r). These are
*different* mathematical objects:

- ξ_φ(r) is a bulk-field observable, measured everywhere.
- motif-pair correlation is a spatially filtered statistic,
  sampled only at the (sparse) points where the motif filter
  admits a ratio.

**Pinned interpretation.** In the absence of a derivation step
that commutes "half-decay of ξ_φ(r)" with "half-decay of the
motif-ratio correlator", the GR-SC 1.7 prediction is *primarily*
a statement about ξ_φ(r). The F4 channel is a secondary
diagnostic; the FFT channel is the primary test. This memo
adopts that ordering and flags any eighteenth-pass work that
would need to reconcile the two channels.

---

## 2. Field selection

Two candidate fields; both may be computed in a single driver run,
but only (A) produces the primary verdict.

**(A) Bulk p-field — primary.**

  φ(x) ≡ p(x, t_snap)

Scalar density field at each snapshot, with its own mean
subtracted. This is the field whose half-decay length is ξ by
the ED-SC 3.3 definition (canonical ξ = 1.7575 lu comes from
`xi_halfdecay` applied to this field). The FFT
autocorrelation of p is therefore measuring *exactly* the
half-decay that defines ξ — with an important qualification:
ξ was derived from the density channel of the *unfiltered*
field, so

  r_½^unfilt ≡ ξ_canonical = 1.7575 lu (by definition).

The primary prediction is that the **filtered** version of
the same field (next paragraph) has a compressed half-decay
by a factor `0.80 ± 0.05`.

**"Filtered" for the primary test.** The GR-SC 1.7 half-rise
compression prediction compares the unfiltered two-point
correlator against its motif-filter-conditioned counterpart.
At the field level, the natural "filter" is not a different
field but a different *window*: ξ_φ(r) measured on the field
*restricted to motif-hosting sites* vs ξ_φ(r) measured on
the bulk field. Two implementations of the restriction:

1. **Motif-indicator masking.** Compute ξ_φ(r) on `p(x) · M(x)`
   where `M(x)` is the indicator of motif sites passing the
   canonical `(α_filt, N_req) = (0.25, 4)` filter. This
   changes the normalisation (σ_0² ≠ Var p) but preserves the
   FFT machinery. Filtered half-decay
   `r_½^filt ≡ C_filtered(r) = 1 crossing`.
2. **Kernel reweighting.** Compute the autocorrelation of
   `p(x)` weighted by a slowly varying envelope that peaks at
   motif sites. Smoother but introduces an envelope-width
   parameter. Not adopted; would need its own scoping memo.

Implementation (1) is adopted as the primary filtered-field
definition for this memo.

**(B) Filtered motif-indicator field — secondary diagnostic.**

  φ_M(x) = M(x) (0-1 indicator)

Autocorrelation of the motif-indicator itself, independent
of the continuous p-values. This is a *density-of-motifs*
correlation function and reflects the spatial Poisson (or
non-Poisson) structure of where motifs live, not the
correlation of the ratios they carry. Useful as a
cross-check on whether the motif-indicator field is
consistent with a Poisson point process (giving
ξ_φ_M(r) ≈ 0 for r > 0 by construction, i.e.
C_redshift(r) ≈ 2 everywhere — matching F4-alt's
structural reading).

Secondary channel; **not part of the primary verdict**. Its
output is reported in diagnostics only.

---

## 3. Measurement architecture

**Ensemble.** 10 seeds × 40 snapshots, identical to the F2 /
F4 / F4-alt configuration:

  SEEDS = {11, 22, 33, 44, 55, 66, 77, 88, 99, 111}
  burn-in = 100, snap-every = 10
  canonical hinge: L_ray = 1.08 · ξ_measured per seed
  canonical filter (for field (A)-filtered): α_filt = 0.25, N_req = 4

IC-amplitude calibration to ξ_target = 1.7575 lu per seed
(miss tolerance ≤ 1 %; inherited verbatim from F4-alt driver).

**Estimator.** For each snapshot:

1. Compute `φ̂ = FFT(φ − ⟨φ⟩)`.
2. Power spectrum `P = |φ̂|²`.
3. Real-space autocorrelation `C_real = Re(IFFT(P)) / N²`.
4. `fftshift` to centre `r = 0` at the midpoint.
5. Radial average over integer-r lattice shells to obtain
   `ξ_φ(r)` for `r ∈ {0, 1, √2, 2, √5, √8, 3, √10, √13, 4, …}`
   (the continuous-r profile, which the FFT samples on the
   full shell structure, not just the Δr = 0.5 lu bins).

Snapshot-level `ξ_φ(r)` is ensemble-averaged across the 400
(10 × 40) snapshot realisations to form the central curve.

**Continuous-r vs shell-r.** The FFT radial average samples
every achievable Z² shell radius (no gap-induced empty bins);
this is the key advantage over the F4 pair-binning channel. The
output curve is *still* discrete in r (one value per shell
radius), but the shell spacing is as fine as the lattice
allows — {1, √2, 2, √5, √8, 3, √10, √13, 4, √17, √18, √20, …}
— giving effective sub-0.25-lu resolution at small r without
the binning obstruction.

**Bootstrap.** 4000 resamples across the 10-seed ensemble
(snapshot-level is treated as within-seed; bootstrap is
over *seeds*, consistent with the sixteenth-pass
ensemble-vs-single-seed guardrail). Per-resample ξ_φ(r)
curve → per-resample r_½; 16 / 84 quantiles give the
uncertainty band on r_½.

---

## 4. Half-rise extraction

**Definition.** For each channel (unfiltered bulk and
filtered-masked), define

  C_redshift(r) = 2 · [ 1 − ξ_φ(r) / σ_0² ]

with σ_0² = ξ_φ(0). C is 0 at r = 0 and saturates at 2 at
large r. The **half-rise** is the smallest r ≥ 0 such that
`C_redshift(r) = 1`, equivalently `ξ_φ(r) / σ_0² = 0.5`.

**Extraction method.** Linear interpolation between the two
consecutive shell radii bracketing the `ξ_φ(r)/σ_0² = 0.5`
crossing. Because the FFT shell structure produces a
monotone-decreasing curve for a generic random field, a
single crossing is expected; multi-crossing cases are
flagged as diagnostic (non-monotone ξ_φ, unusual but
reportable).

**Ratio definition.**

  ratio ≡ r_½^filt / r_½^unfilt

where r_½^unfilt is measured on the same ensemble from the
bulk p field (independent re-measurement of ξ; expected to
agree with ξ_canonical = 1.7575 lu to within ensemble
spread — acts as a self-calibration check). r_½^filt is
measured from the motif-indicator-masked p-field
autocorrelation.

**Self-calibration check.** Before the primary verdict is
taken, the unfiltered r_½ must reproduce ξ_canonical =
1.7575 lu to within ±10 % (ensemble band). If it does not,
the driver flags a `GuardrailFailure` and the verdict is
declared Inconclusive until the calibration discrepancy is
resolved. This is the FFT analogue of the F4-alt "pair-count
sparsity" gate.

---

## 5. Verdict taxonomy

Four-way, inheriting the F4-alt / F4 tenth-pass bands:

- **Confirmed** — `ratio ∈ [0.75, 0.85]` (tenth-pass 0.80 ± 0.05
  band; two-channel corroboration with GR-SC 1.7).
- **Confirmed-marginal** — `ratio ∈ [0.70, 0.75) ∪ (0.85, 0.90]`
  (outside the Confirmed band but inside the double envelope).
- **Refuted** — `ratio < 0.70 or > 0.90` (outside the double
  envelope; GR-SC 1.7 prediction contradicted at the primary
  channel).
- **Inconclusive** — no crossing of `ξ_φ(r)/σ_0² = 0.5` in the
  measured r-range; **or** bootstrap 16–84 band straddles a
  verdict-threshold boundary (Confirmed-marginal or
  Refuted → reported as Confirmed-marginal if the central is
  in Confirmed but the band leaks, Inconclusive if the central
  is in Confirmed-marginal but the band leaks to Refuted);
  **or** self-calibration check fails (ratio_unfilt / ξ_canonical
  outside ±10 %).

**Cross-channel verdict reconciliation.** The FFT result is
reported alongside the F4 sub-arc verdict. Four combined cases:

| FFT verdict | F4 verdict | Combined interpretation |
|---|---|---|
| Confirmed | Refuted-by-extension (F4-alt) | Channel-dependent: field-level half-rise matches prediction; motif-pair channel does not. New scientific finding. |
| Refuted | Refuted-by-extension (F4-alt) | Two-channel corroboration of F4 sub-arc's structural reading; GR-SC 1.7 prediction refuted at primary channel. |
| Confirmed | Refuted-by-extension (F4-alt) *via lattice obstruction* | FFT primary verdict stands; F4-alt reading downgraded to "measurement-channel artefact at relaxed filter on 64²". |
| Inconclusive (any reason) | Refuted-by-extension (F4-alt) | F4-alt sub-arc's verdict unchallenged; FFT channel pending driver refinement or larger lattice. |

The integration memo (pre-registered as
`theory/ED_SC_3_5_FFT_XiField_Integration.md`, forthcoming)
applies this reconciliation and updates the GR-SC 1.0 §5
Correlation-class row pointer accordingly.

---

## 6. Deliverables

- [x] Scoping memo (this document).
- [ ] Driver memo
  `theory/ED_SC_3_5_FFT_XiField_Driver.md`.
- [ ] Driver script
  `analysis/scripts/ed_sc_3_5_fft_xi_field.py`.
- [ ] Execution artefacts under
  `outputs/ed_sc_3_5_fft_xi_field/`
  (`xi_field_profile.csv`, `xi_field_per_seed.csv`,
  `xi_field_summary.json`).
- [ ] Integration memo
  `theory/ED_SC_3_5_FFT_XiField_Integration.md`
  (post-execution synthesis; cross-channel reconciliation per §5).

**Pre-registered closure scope.** ED-SC 3.5 closes when:
(a) the primary unfiltered-bulk-field ξ_φ(r) self-calibrates to
ξ_canonical within ±10 % (guardrail); (b) the filtered-field
half-rise ratio is extracted with bootstrap band; (c) the
four-way verdict is rendered; (d) the cross-channel
reconciliation with F4 is performed and the GR-SC 1.0 §5
Correlation-class row pointer is updated via an addendum to
`theory/GR_SC_1_8_PostF4_Consolidation.md`.

**Changelog.**

- 2026-04-23 (seventeenth pass) — Initial draft. Pre-registers
  the FFT field-autocorrelation channel as the primary test of
  GR-SC 1.7's half-rise compression prediction. Adopts the bulk
  p-field as primary, the motif-indicator-masked p-field as the
  filtered counterpart, and the motif-indicator field itself as
  a secondary diagnostic. Four-way verdict taxonomy inherited
  from F4. Cross-channel reconciliation matrix specified.
  Driver + execution + integration deferred as subsequent
  seventeenth-pass follow-up (or eighteenth-pass work).
