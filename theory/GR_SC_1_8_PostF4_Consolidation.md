# GR-SC 1.8 Post-F4 Consolidation

**Pass:** seventeenth (post-F4 checkpoint)
**Date:** 2026-04-23
**Parent arc:** GR-SC tenth-pass curvature-invariant taxonomy + fifteenth-pass quantitative prediction layer + sixteenth-pass GR-SC 2.0 Amendment + seventeenth-pass F4 Correlation-class sub-arc.
**Paired authoritative references:**
- `theory/GR_SC_2_0_Consolidation.md` (tenth-pass taxonomy)
- `theory/GR_SC_2_0_Consolidation_Amendment.md` (sixteenth-pass amendment)
- `theory/GR_SC_1_0_MotifCurvatureInvariants.md` (fifteenth-pass §5 invariant table)
- `theory/ED_SC_3_4_twopoint_FilterRelaxation_Integration.md` (F4 sub-arc closure)

---

## 1. Purpose

Consolidate the seventeenth-pass F4 Correlation-class sub-arc into a
single post-F4 checkpoint, updating the GR-SC 1.0 §5 authoritative
invariant-table pointer for the `C_redshift(r)` row, recording the
new lattice-geometry guardrail, and pre-registering the next major
arc.

**Three-line F4 closure** (from
`theory/ED_SC_3_4_twopoint_FilterRelaxation_Integration.md` §6):

1. **Canonical N_req = 4:** **Inconclusive** (pair-count sparsity).
   Canonical filter admits ~2 motifs/snapshot on the 64² torus,
   yielding 51 binned pairs across 10 r-bins at Δr = 0.5 lu.
   Every bin fails the 20-pair admissibility threshold; the
   tenth-pass GR-SC 1.7 half-rise prediction
   `r_½^filt / r_½^unfilt = 0.80 ± 0.05` is *not testable at
   the canonical operating point on 64²*. Structural finding,
   not a measurement bug.
2. **Relaxed N_req = 2:** **Refuted-by-extension structural**.
   The N_req: 4 → 2 scope amendment (scope-restricted to the
   C_redshift measurement channel only) yielded 27,210 motifs
   and 24,464 binned pairs (8 of 10 bins admissible), but
   `C_ensemble(r) ∈ [1.96, 2.05]` across every admissible bin
   from r = 1.0 lu onward — saturated at the uncorrelated
   asymptote `C(∞) = 2`. No C(r) = 1 crossing exists in the
   measured r-range; any half-rise must lie at r < 1.0 lu,
   giving a ratio < 0.57 outside the tenth-pass refutation
   envelope [0.70, 0.90].
3. **Refinement Δr = 0.25:** **Inconclusive-thin (lattice
   geometry)**. The F4-alt-refine run ({0.25, 0.50, 0.75,
   1.00, 1.25, 1.50, 1.75, 2.00} at Δr = 0.25) produced
   3 of 8 admissible bins (gate ≥ 6 of 8). Root cause is a
   **lattice-discretisation obstruction**: consecutive
   lattice-achievable radii on Z² have gap ≥ √2 − 1 ≈
   0.414 lu at small r, so Δr = 0.25 leaves five bins empty
   *by construction* regardless of motif count. The three
   admissible bins (r = 1.0, √2, 2.0) yield C ∈ [2.04, 2.08],
   reinforcing the F4-alt reading on the admissible subset.

**GR-SC 1.0 §5 Correlation-class row status:**

> The `C_redshift(r)` Correlation-class row is **closed at the
> relaxed-filter evidence level**. The tenth-pass half-rise
> compression prediction `r_½^filt / r_½^unfilt = 0.80 ± 0.05`
> is **Refuted-by-extension structural** at the F4-alt measurement
> channel (N_req = 2) on the 64² square-Z² lattice. The canonical-
> filter row (N_req = 4) remains **Inconclusive** on 64² pending
> a larger-lattice follow-up.

The structural refutation is **scope-restricted to the F4-alt
measurement channel**: it does not retract any other GR-SC
prediction, nor does it affect the canonical ED-SC operating
point `(L_ray/ξ, α_filt, N_req) = (1.08, 0.25, 4)` or the
distributional invariant `f(ρ | ξ, L_ray, α_filt, N_req)`.

---

## 2. Lattice-geometry guardrail

**Z² minimum-image distance shell structure.** On a square
integer lattice of side L with minimum-image periodic-boundary
distance, the set of achievable inter-site radii at small r is

  { 1, √2, 2, √5, √8, 3, √10, √13, 4, … }

with consecutive-radius gaps

  √2 − 1    ≈ 0.414 lu
  2 − √2    ≈ 0.586 lu
  √5 − 2    ≈ 0.236 lu
  √8 − √5   ≈ 0.592 lu
  3 − √8    ≈ 0.172 lu
  √10 − 3   ≈ 0.162 lu
  …

The smallest gap below r = 4 lu is √10 − 3 ≈ 0.162 lu; the
second-smallest is √5 − 2 ≈ 0.236 lu. Both lie below the
admissibility-relevant Δr = 0.25.

**Bin-width requirement.** Any Δr smaller than the dominant
small-r gap (√2 − 1 ≈ 0.414 lu) leaves most small-r bins empty
by construction. For r < 4 lu on 64², the practical minimum is

> **Δr ≥ 0.5 lu on 64² square-Z²**

which guarantees every bin contains at least one lattice-
achievable radius up to r ≈ 5 lu. This matches the F4-alt
canonical-grid choice (which reaches 8 of 10 admissibility).

**Δr < 0.41 lu is structurally unpopulable** on square-Z² 64²:
Case-by-case demonstration for the F4-alt-refine Δr = 0.25 grid:

| bin (r_target, lu) | bin interval | lattice radii inside | N_pairs (measured) |
|---|---|---|---|
| 0.25 | [0.125, 0.375) | none | 0 |
| 0.50 | [0.375, 0.625) | none | 0 |
| 0.75 | [0.625, 0.875) | none | 0 |
| 1.00 | [0.875, 1.125) | 1 | 1,473 |
| 1.25 | [1.125, 1.375) | none | 0 |
| 1.50 | [1.375, 1.625) | √2 ≈ 1.414 | 1,126 |
| 1.75 | [1.625, 1.875) | none | 0 |
| 2.00 | [1.875, 2.125) | 2 | 1,115 |

The pattern generalises: at Δr = 0.25, a bin is populated only
when its interval contains a member of the achievable-radius
set. This is independent of motif count, seed count, filter
strictness, or simulation length — it is a property of the
ambient geometry.

**Remedies for sub-0.5-lu r-resolution** (not executed this
pass; pre-registered under §4):

(a) **Different ambient geometry.** A hexagonal lattice has
radii {1, √3, 2, √7, 3, …} with different gaps; mixing two
lattice orientations reduces gap widths but does not eliminate
them.

(b) **Larger lattice with ξ rescaling.** On `N² = 128²` with
ξ_canonical rescaled by a factor of 2 (to 3.515 lu), the
effective r-resolution in units of ξ is preserved, but the
absolute bin-width Δr_physical = 1.0 lu on 128² ≡ 0.5·ξ_new,
which means the shell gaps in lattice units are unchanged.
**Lattice rescaling alone does not help** — only a different
geometry or a non-binned estimator does.

(c) **Direct FFT-based ξ_φ(r) estimator.** Compute the
autocorrelation of the filtered motif-indicator field via
FFT; this yields a continuous-r band-limited estimate of
ξ_φ(r) at O(N² log N) cost, bypassing the pair-binning
bottleneck entirely. Pre-registered under §4, Option B.

**Guardrail statement** (carried forward to all future GR-SC
Correlation-class work):

> Any GR-SC Correlation-class measurement that uses motif-pair
> r-binning on a square-Z² lattice must use Δr ≥ 0.5 lu. Finer
> r-resolution requires either a non-square ambient geometry
> or a non-binned estimator (direct FFT, kernel density, or
> continuous-r fit to the pair histogram).

---

## 3. GR-SC 1.0 invariant table update

The `C_redshift(r)` row of `theory/GR_SC_1_0_MotifCurvatureInvariants.md`
§5 (the 9-row authoritative invariant → input → ξ-dependence →
uncertainty → evaluated-in table) should be annotated with the
following structural notes (pointer-only; the table in GR-SC 1.0
is not reformatted, just pointed to this memo).

**Pointer entries for the `C_redshift(r)` row:**

- **`evaluated_at_canonical_filter`: `Inconclusive (pair-sparsity)`** —
  canonical `(α_filt=0.25, N_req=4)` on 64² admits ~51 binned
  pairs across 10 r-bins at Δr = 0.5 lu; no C(r) = 1 crossing
  findable. See
  `outputs/ed_sc_3_4_twopoint/correlation_twopoint_summary.json`
  and `theory/ED_SC_3_4_twopoint_Driver.md`. The tenth-pass
  prediction remains *not tested* at the canonical operating
  point on 64².

- **`evaluated_at_relaxed_filter`: `Refuted-by-extension structural`** —
  N_req = 2 scope amendment (C_redshift channel only) yields
  `C_ensemble(r) ∈ [1.96, 2.05]` across r ∈ [1.0, 5.0] lu,
  with no crossing of C = 1; half-rise must lie at r < 1 lu,
  giving ratio < 0.57 outside the [0.70, 0.90] envelope.
  See `outputs/ed_sc_3_4_twopoint_relaxed/correlation_twopoint_summary.json`
  and `theory/ED_SC_3_4_twopoint_FilterRelaxation.md`.

- **`evaluated_at_refinement_grid`: `Inconclusive-thin (lattice
  geometry)`** — Δr = 0.25 in r ∈ [0.25, 2.0] on 64² square-Z²
  produces 3 of 8 admissible bins (gate 6 required). Three
  admissible bins (r = 1.0, √2, 2.0) all yield C ∈ [2.04, 2.08].
  Root cause: Z² radius-shell gaps exceed Δr. See
  `outputs/ed_sc_3_4_twopoint_relaxed_refine/correlation_twopoint_summary.json`
  and `theory/ED_SC_3_4_twopoint_FilterRelaxation_Refine.md`.

- **`scope_restriction`** — the F4-alt and F4-alt-refine
  Refuted-by-extension and Inconclusive-thin verdicts apply to
  the C_redshift(r) measurement channel *only*. The canonical
  ED-SC operating point and the distributional invariant
  `f(ρ | ξ, L_ray, α_filt, N_req)` are untouched.

- **`net_uncertainty_structure`** — the Correlation-class row
  now carries four evidence levels: canonical (Inconclusive
  pending L-larger), relaxed (Refuted-by-extension structural),
  refinement (Inconclusive-thin lattice obstruction), and
  post-L-larger (pending §4 Option A). The canonical-filter
  verdict is the primary citation; the relaxed-filter verdict
  is a secondary diagnostic reading scope-restricted to the
  measurement channel.

**GR-SC 2.0 Consolidation Amendment** gains a new note
(sixteenth-pass amendment is already paired with tenth-pass
Consolidation; this post-F4 consolidation extends the taxonomy-
stabilisation record):

> **Correlation-class closure note (seventeenth pass, post-F4).**
> The `C_redshift(r)` Correlation-class row is closed at the
> relaxed-filter evidence level with a structural Refuted-by-
> extension verdict. The canonical-filter row awaits an L-larger
> follow-up. The lattice-geometry guardrail Δr ≥ 0.5 lu on 64²
> is a new methodological constraint applying to any future
> Correlation-class measurement on square-Z².

---

## 4. Next major arc

Three options are pre-registered; the choice should be taken
in the eighteenth pass based on the relative priorities of
internal theoretical closure vs external empirical work.

### Option A — L-larger follow-up (internal; compute)

**Scope.** Re-run F4 canonical at N_req = 4 on a 128² or 256²
lattice with paired ξ rescaling to keep `(L_ray/ξ, α_filt, N_req)`
= (1.08, 0.25, 4) fixed. Expected pair-density gain is ≈ 4× per
lattice doubling (motif count scales with lattice area at fixed
filter strictness; bin-contained pairs scale with pair count).

**Deliverables.**
- Driver memo
  `theory/ED_SC_3_4_twopoint_LLarger_Driver.md`.
- Driver script
  `analysis/scripts/ed_sc_3_4_twopoint_correlation_Llarger.py`
  (F4 canonical driver verbatim with two changes:
  `fr.SIZE` override path and ξ_target rescaling).
- Outputs in
  `outputs/ed_sc_3_4_twopoint_Llarger/`.
- Integration memo
  `theory/ED_SC_3_4_twopoint_LLarger_Integration.md`.

**Expected verdict structure** (four-way ratio band plus the
lattice-geometry guardrail; no six-way extension needed if
Δr ≥ 0.5 lu is honoured on the larger lattice).

**Wall estimate.** Single session (≈ 150–400 s on 128²;
≈ 600–1500 s on 256²).

**Closes.** The canonical-filter C_redshift row of GR-SC 1.0
§5; removes the "awaiting L-larger" footnote; upgrades the
GR-SC 1.7 half-rise compression prediction from "Inconclusive"
to a definitive four-way verdict at the canonical operating
point.

### Option B — Direct FFT ξ_φ(r) estimator (internal; compute)

**Scope.** Compute `ξ_φ(r) = ⟨φ(x)φ(x+r)⟩` directly on the
filtered motif-indicator field or the bulk scalar field, using
FFT autocorrelation at O(N² log N). Produces a continuous-r
band-limited estimate of `C_redshift(r) = 2[1 − ξ_φ(r)/σ_0²]`
independent of the motif-pair-binning channel.

**Deliverables.**
- Scope memo
  `theory/ED_SC_3_5_FFT_XiField_Scoping.md`
  (pre-registers the estimator definition, the field-selection
  rule — filtered motif indicator vs bulk `p` — and the
  half-rise extraction protocol).
- Driver memo
  `theory/ED_SC_3_5_FFT_XiField_Driver.md`.
- Driver script
  `analysis/scripts/ed_sc_3_5_fft_xi_field.py`.
- Outputs in
  `outputs/ed_sc_3_5_fft_xi_field/`.

**Expected outcomes.** (i) continuous-r resolution below the
lattice-shell gap floor; (ii) a parallel-channel
cross-check on the F4-alt Refuted-by-extension structural
reading; (iii) a new measurement modality independent of the
motif-filter pair-density bottleneck.

**Wall estimate.** Single session (≈ 30–90 s on 64²; FFT is
cheap compared to motif extraction).

**Closes.** Does not replace Option A (which tests a different
channel — motif-ratio pair correlations rather than bulk field
autocorrelation), but provides independent evidence on the
underlying half-rise scale; if the FFT channel agrees with
F4-alt that half-rise is below r = 1 lu, the Refuted verdict
is corroborated across channels.

### Option C — Pause GR-SC; resume empirical tracks

**Scope.** Suspend GR-SC 1.0+ theoretical arc and return
attention to the two external-blocked empirical tracks:

1. **FRAP at Creative Proteomics** — under technician review.
   Status check warranted (a) if the technician review has
   returned feedback, and (b) if new data would inform the
   ED-09.5 follow-up.
2. **ED-09.5 Aspelmeyer / Arndt outreach** — pending external
   response. Follow-up correspondence or a revised experimental-
   strategy memo may be warranted.

**Deliverables.** Status-check memos only; no new drivers.

**Rationale.** GR-SC 1.0 §5 is now closed at every row
(Ratio, Quadratic, Rayleigh, Trace-Gaussian rigid-zero,
Correlation) at either quantitative prediction or
structural-verdict resolution. No high-ROI theoretical
intervention remains without new driver work (Option A / B);
external empirical progress may have higher marginal value.

### Recommended ordering

**Option B first** (single short session; provides independent
cross-check on F4-alt structural reading with minimal
investment), **then Option A** (longer session; closes the
canonical-filter row), **with Option C in parallel** (empirical
status checks are not compute-bound and can run alongside
either theoretical option).

---

## 5. Deliverables

- [x] Post-F4 consolidation memo (this document).
- [x] Pointer updates for:
  - `memory/project_ed_gr_sc_arc.md` — seventeenth-pass
    F4 sub-arc section (applied).
  - `memory/MEMORY.md` — GR-SC arc one-liner (applied).
  - `docs/ED-Orientation.md` — status line and seventeenth-pass
    bullet (applied).
  - `docs/ED_Accomplishments.md` — F4 accomplishment entry
    and generation-history line (applied).
  - `theory/GR_SC_1_0_MotifCurvatureInvariants.md` §5 — via
    pointer to this memo §3 (no direct edit required;
    `C_redshift(r)` row annotated by reference).
  - `theory/GR_SC_2_0_Consolidation_Amendment.md` — via
    the "Correlation-class closure note" above (pointer-only;
    amendment remains paired with tenth-pass Consolidation).
- [x] Lattice-geometry guardrail §2 stated as a first-class
  methodological constraint for any future GR-SC Correlation-
  class work on square-Z².
- [x] Pre-registered next major arc (Options A / B / C) §4
  with deliverables, wall estimates, and closure scope.

**Changelog.**

- 2026-04-23 (seventeenth pass) — Initial draft. Consolidates
  the F4 sub-arc (canonical, F4-alt, F4-alt-refine, integration)
  into a single post-F4 checkpoint. Adds the Δr ≥ 0.5 lu
  lattice-geometry guardrail. Pre-registers Option A (L-larger),
  Option B (direct FFT ξ_φ(r)), and Option C (empirical
  tracks) as the next major arc choices. No tenth-pass,
  fifteenth-pass, or sixteenth-pass structural claims retracted;
  this memo is a closure-and-handoff document, not a revision.
