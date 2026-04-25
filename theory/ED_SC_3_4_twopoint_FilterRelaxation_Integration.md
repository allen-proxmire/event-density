# ED-SC 3.4 F4 Sub-Arc Integration Memo

**Pass:** seventeenth (GR-SC F4 Correlation-class sub-arc, closure)
**Date:** 2026-04-23
**Parent memos:**
- `theory/ED_SC_3_4_twopoint_Scoping.md` (F4 canonical pre-registration)
- `theory/ED_SC_3_4_twopoint_Driver.md` (F4 canonical driver)
- `theory/ED_SC_3_4_twopoint_FilterRelaxation.md` (F4-alt scope amendment)
- `theory/ED_SC_3_4_twopoint_FilterRelaxation_Driver.md` (F4-alt driver)
- `theory/ED_SC_3_4_twopoint_FilterRelaxation_Refine.md` (F4-alt-refine scope)

**Parent artefacts:**
- `outputs/ed_sc_3_4_twopoint/correlation_twopoint_summary.json` (F4 canonical)
- `outputs/ed_sc_3_4_twopoint_relaxed/correlation_twopoint_summary.json` (F4-alt)
- `outputs/ed_sc_3_4_twopoint_relaxed_refine/correlation_twopoint_summary.json` (F4-alt-refine)

---

## 1. Purpose

Close the seventeenth-pass GR-SC F4 Correlation-class sub-arc by synthesising
the canonical (N_req = 4, Δr = 0.5), filter-relaxed (N_req = 2, Δr = 0.5),
and Δr-refined (N_req = 2, Δr = 0.25) drivers into a single coherent
verdict on the tenth-pass GR-SC 1.7 falsifier
`r_½^filt / r_½^unfilt = 0.80 ± 0.05`.

---

## 2. Three-tier execution summary

| Tier | Driver | N_req | Δr | N_motifs | N_pairs_binned | Admissible bins | Formal verdict |
|------|--------|-------|----|----------|-----------------|------------------|------|
| F4 canonical | `ed_sc_3_4_twopoint_correlation.py` | 4 | 0.5 lu | 849 | 51 | 0/10 | Inconclusive (pair sparsity) |
| F4-alt | `ed_sc_3_4_twopoint_correlation_relaxed.py` | 2 | 0.5 lu | 27,210 | 24,464 | 8/10 | Inconclusive (no crossing; C saturated at ≈ 2) |
| F4-alt-refine | `ed_sc_3_4_twopoint_correlation_relaxed_refine.py` | 2 | 0.25 lu | 27,210 | 3,714 | 3/8 | Inconclusive-thin (lattice obstruction) |

All three runs used the same 10-seed ensemble {11, 22, 33, 44, 55, 66, 77,
88, 99, 111}, the same canonical operating point (L_ray/ξ, α_filt) = (1.08,
0.25) on the 40-snapshot evolution with per-seed IC-amplitude calibration
to ξ_target = 1.7575 lu (miss < 1% each seed), and the same
minimum-image distance on the 64² periodic torus.

---

## 3. Structural reading of the admissible subset

Concatenating the admissible bins across F4-alt (8 bins at r ∈
{1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5}) and F4-alt-refine (3 bins at
r ∈ {1.0, 1.5, 2.0}):

- **F4-alt** — C_ensemble ∈ [1.96, 2.05] across all 8 admissible bins;
  C_rank ∈ [1.97, 2.12]. No C(r) = 1 crossing within r ∈ [0.25, 5.25] lu.
  Rigid endpoint C(r_max = 4.5) = 2.042 (within 2.1% of the uncorrelated
  asymptote C(∞) = 2).
- **F4-alt-refine** — C_ensemble ∈ [2.04, 2.08] at r = {1.0, √2 ≈ 1.414,
  2.0}; C_rank ∈ [2.01, 2.12]. Re-measures the small-r points available
  on a 64² lattice.

Convergent reading: **C_redshift(r) is at or slightly above its
uncorrelated asymptote C(∞) = 2 for all lattice-resolvable distances
r ≥ 1 lu at (α_filt, N_req) = (0.25, 2).** The motif-ratio field
exhibits no spatial correlation above r = 1 lu; the half-rise from
C(0) ≈ 0 (perfectly correlated coincident motifs) to C = 1 must lie
entirely within r < 1 lu if it exists.

---

## 4. Why Δr < 0.41 cannot populate the small-r bins (new guardrail)

**Lattice-discretisation obstruction** (discovered by F4-alt-refine):
on a square integer lattice Z² with minimum-image distance, the set of
achievable inter-site distances at small r is {1, √2, 2, √5, √8, 3, …}.
The two smallest gaps are

  √2 − 1 ≈ 0.414 lu
  2 − √2 ≈ 0.586 lu

Any bin-width Δr < 0.414 will therefore leave every small-r bin whose
interior does not contain one of these lattice-achievable radii
*empty by construction*, regardless of motif count, seed count, or
filter relaxation. F4-alt-refine's 3-of-8 admissibility (bins at
r = 1.0, 1.5, 2.0 — each containing exactly one lattice-achievable
distance) is a direct consequence.

**Guardrail for future GR-SC Correlation-class measurements on the
64² square lattice:** use Δr ≥ 0.5 lu (F4-alt grid), which guarantees
every bin contains at least one lattice-achievable radius up to
r ≈ 5 lu. Any finer r-resolution requires either (a) a different
ambient geometry (hexagonal, off-lattice), (b) a structure function that
does not bin raw distances (e.g. direct correlation of motif ratios
against analytic expected ξ_φ(r)), or (c) a larger lattice with
rescaling such that Δr measured in units of ξ stays ≥ √2 − 1 times ξ.

This is **not** a physical refutation — it is a statement that the F4
measurement channel, as pre-registered, does not resolve r < 1 lu on
64². The tenth-pass GR-SC 1.7 prediction r_½^filt / ξ ≈ 0.80 (which
would place r_½^filt ≈ 1.4 lu — in the admissible range) is testable
on this lattice; the prediction "r_½^filt < 1 lu" implied by the
F4-alt/F4-alt-refine data is not directly measurable on 64² at Δr < 0.5.

---

## 5. Implied ratio and structural verdict

If a true half-rise exists somewhere below the first admissible bin
r = 1 lu, the ratio is bounded above by

  r_½^filt / r_½^unfilt = r_½^filt / 1.7575 ≤ 1.0 / 1.7575 ≈ 0.569

This falls **outside** the tenth-pass refutation envelope
[0.70, 0.90] — the pre-registered F4 Refuted band. Under this
structural reading, the F4 sub-arc **Refutes** the tenth-pass GR-SC 1.7
half-rise prediction *at the F4-alt filter (N_req = 2) on the 64²
lattice*.

However, per the F4-alt §2 / F4-alt-refine §3 scope restriction,
the F4-alt filter is not the canonical ED-SC operating point — it was
adopted purely to acquire pair statistics at N_req = 4's sparsity. The
structural refutation therefore applies narrowly to the *relaxed-filter
measurement channel*, not to the ED-SC canonical prediction set.

---

## 6. Three-line verdict for the seventeenth pass

1. **At the canonical operating point (N_req = 4)**: Inconclusive —
   the filter is too sparse on 64² for the F4 correlation measurement
   (51 binned pairs). The tenth-pass GR-SC 1.7 half-rise prediction
   remains *untested on this lattice at the canonical filter*, pending
   either a larger lattice or a direct ξ_φ(r) estimator that does not
   require motif-pair binning.
2. **At the relaxed filter (N_req = 2)**: Refuted-by-extension (structural) —
   C_redshift(r) is at the uncorrelated asymptote for all lattice-resolvable
   r ≥ 1 lu; any half-rise must lie at r_½^filt < 1 lu, giving ratio
   < 0.57 outside the [0.70, 0.90] envelope.
3. **Scope restriction**: the structural refutation applies to the
   F4-alt measurement channel only; the canonical operating point
   (N_req = 4, L_ray/ξ = 1.08, α_filt = 0.25) remains authoritative
   for every other ED-SC / GR-SC claim. The ED-SC 3.x distributional
   invariant `f(ρ | ξ, L_ray, α_filt, N_req)` is not affected.

---

## 7. Durable seventeenth-pass findings (to carry into pass eighteen)

1. **Pair-count sparsity is the dominant obstacle to Correlation-class
   tests at N_req = 4 on 64².** Canonical F4 produced only 51 binned
   pairs across 10 bins; relaxing to N_req = 2 recovers 24,464 pairs (×480).
2. **Lattice-discretisation obstruction at Δr < 0.41 lu on square Z².**
   Small-r bins at Δr = 0.25 are empty by construction; Δr ≥ 0.5 lu is
   the practical minimum for 64².
3. **C_redshift(r) saturates at the uncorrelated asymptote C = 2 for all
   lattice-resolvable r ≥ 1 lu at (α_filt, N_req) = (0.25, 2)** — a
   robust result now confirmed at two different Δr resolutions.
4. **Six-way verdict taxonomy** (Confirmed / Confirmed-marginal /
   Inconclusive / Refuted / Inconclusive-nonmonotone / Inconclusive-thin)
   performed as pre-registered: the Inconclusive-thin branch correctly
   flagged the lattice-geometry obstruction without conflating it with
   statistical thinness.
5. **Scope-restriction pattern** (F4-alt / F4-alt-refine relaxed filter
   applies to the C_redshift channel only) survives intact: no other
   ED-SC / GR-SC prediction was contaminated by the N_req = 2 excursion.

---

## 8. Open threads for pass eighteen

- **L-larger follow-up**: re-run F4 canonical at N_req = 4 on a 128²
  or 256² lattice (paired ξ rescaling to keep canonical operating
  point fixed) to obtain ≥ 400 binned pairs and retest the tenth-pass
  prediction at the canonical filter. Wall scaling ≈ 4× per lattice
  doubling; feasible in one session.
- **Direct ξ_φ(r) estimator**: bypass the motif-pair binning by
  FFT-correlating the filtered motif-indicator field directly, yielding
  continuous r-resolution. Would require a new driver script; the
  measurement channel is distinct from the F4 pair-based Pearson/Spearman
  channel and constitutes a **parallel** test, not a replacement.
- **GR-SC 1.0 §5 invariant table closure status**: F4 row is now closed
  at the relaxed-filter channel with a structural Refuted-by-extension;
  the canonical-filter row remains Inconclusive pending the L-larger
  follow-up.

---

## 9. Status

**F4 sub-arc CLOSED at the seventeenth pass** with the three-line
verdict in §6. All deliverables accounted for:

- 3 scoping memos (F4 / F4-alt / F4-alt-refine)
- 2 driver memos (F4 / F4-alt)
- 3 driver scripts (executed, artefacts persisted)
- 1 integration memo (this document)

Total: **nine memos**, **three executed drivers**, **three output directories**.
