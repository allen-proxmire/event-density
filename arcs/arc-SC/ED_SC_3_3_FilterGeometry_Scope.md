# ED-SC 3.3 — Filter-Geometry Scope

**Status:** Pre-registration. Scope-only memo. No numerics.
**Parents:**
- `theory/ED_SC_3_0_Scope.md` rev. 2 (distributional architecture,
  within-regime S-F2, resonance-mapping clause).
- `theory/ED_SC_3_1_rev3_CanonicalPointCertification.md`
  (canonical operating-point certification).
- `theory/ED_SC_3_2_5_G3_G4_Transition.md` (Regime-I plateau map).
- `theory/ED_SC_3_2_6_RayBudget_Resonance.md` rev. 2 (resonance
  mechanism confirmed; canonical 40-snapshot ξ mandate).
**Simulator of record:** `r2_grf_falsifier_tests.py`
  + `ED_Update_Rule.ed_step_mobility`.
**Date:** 2026-04-23 (post ED-SC 3.1 rev. 3).

---

## 1. Purpose

ED-SC 3.3 is hereby opened. It is **unblocked** by:

- **ED-SC 3.1 rev. 3** — certifies the canonical operating point
  `(L_ray/ξ, α_filt, N_req) = (1.08, 0.25, 4)` as interior to the
  Regime-I plateau `L_ray/ξ ∈ [1.0, 1.4]`, with canonical pool
  `N = 34, S1 = −1.881, S2 = 1.271`.
- **ED-SC 3.2.5** — maps the three-regime hinge structure at
  Δ(L_ray/ξ) = 0.1 and establishes the Regime-I plateau that
  contains the canonical point.
- **ED-SC 3.2.6 v2** — *Confirmed* verdict on the ray-budget
  resonance mechanism; two structural exclusion windows
  (Window A, Window B) mapped at Δ(L_ray) = 0.02; canonical
  40-snapshot ξ guardrail passes 9/10 seeds.

ED-SC 3.3 tests how the motif-conditioned distributional invariant
`f(ρ | ξ, L_ray, α_filt, N_req)` depends on the **filter-geometry
parameters** `(α_filt, N_req)` at the certified canonical
operating point. Specifically: does the Regime-I distributional
structure persist, deform smoothly, or exhibit new discrete
resonances as the angular tolerance and required-ray count are
varied independently of the hinge?

This memo is pre-registration only. No numerics are presented.

---

## 2. Operating point

All sweeps anchor at the certified canonical operating point:

| parameter | value | source |
|---|---|---|
| ξ (canonical) | **1.7575 lu** | ED-SC 3.1 rev. 2, `outputs/ed_sc_3_1/xi_canonical.json` |
| L_ray | **1.898 lu** (L_ray/ξ = 1.08) | ED-SC 3.1 rev. 3 §2 |
| α_filt (baseline) | 0.25 | canonical |
| N_req (baseline) | 4 | canonical |

**Constraint:** all (α_filt, N_req) scans must hold `L_ray = 1.898 lu`
fixed at the canonical value, preserving `L_ray/ξ = 1.08` interior
to Regime I `[1.0, 1.4]`. Any scan that moves L_ray must carry
a Δ ≤ 0.1 hinge sub-sampling (see §6).

---

## 3. Resonance-window exclusions

Per ED-SC 3.2.6 rev. 2, the following `L_ray` windows are
**structurally forbidden** on the 64² lattice with the canonical
4-ray `N_req = 4` geometry:

| window | L_ray range (lu) | L_ray/ξ range | shell transition |
|---|---|---|---|
| **A** | [2.50, 2.80] | [1.42, 1.59] | √4 (2.000) → √9 (3.000) |
| **B** | [3.50, 3.90] | [1.99, 2.22] | √10 (3.162) → √16 (4.000) |

ED-SC 3.3 sweeps vary `(α_filt, N_req)` at the canonical
`L_ray = 1.898 lu`, which is safely below Window A. No planned
sweep enters Window A or Window B.

**New-resonance clause (inherited from ED-SC 3.0 rev. 2 §5.2):**
if any `(α_filt, N_req)` sub-grid reveals a new non-monotonicity
in S1 or S2 that is not attributable to sampling noise, that
region must be sub-sampled at Δ ≤ 0.05 in the relevant parameter
before any falsifier reading is reported. Discovery of new
resonances is **permitted and expected**; silent passage through
a resonance is forbidden.

---

## 4. Parameter grid

Cartesian product over:

- **α_filt** ∈ {0.10, 0.15, 0.20, 0.25, 0.30}   (5 values)
- **N_req**  ∈ {2, 3, 4, 5}                     (4 values)

Full grid: **20 cells**. The canonical point `(0.25, 4)` is one
cell; it is re-run as an internal consistency check against
ED-SC 3.1 rev. 3's canonical pool.

**L_ray held fixed** at `1.898 lu` (canonical) across all 20
cells, so every cell sits at `L_ray/ξ = 1.08` interior to
Regime I. This is the design choice that isolates filter-geometry
dependence from hinge dependence.

**Secondary hinge sweep (per-cell).** For each `(α_filt, N_req)`
cell, a short hinge scan `L_ray/ξ ∈ {1.00, 1.10, 1.20, 1.30, 1.40}`
(Δ = 0.10, 5 points) is run to confirm that the cell still lies
on a Regime-I plateau under the varied filter. If the plateau
shifts or breaks in a given cell, that cell is flagged and
sub-sampled at Δ ≤ 0.05.

Total raw runs: 20 filter cells × 5 hinge points = **100
evaluation points** (plus per-cell ξ guardrail snapshots).

---

## 5. Protocol

For each `(α_filt, N_req)` cell:

1. **Evolve fields** with the simulator of record
   (`r2_grf_falsifier_tests.py` driver +
   `ED_Update_Rule.ed_step_mobility` update).
   - Canonical seed list (10 seeds; inherited from ED-SC 3.1
     rev. 2).
   - Burn-in 100 steps, then 40 snapshots spaced 10 steps apart
     (total 500 steps per seed).
   - Lattice 64², canonical ED initial conditions.
2. **Collect motifs** under the filter `(α_filt, N_req, L_ray)`
   at every snapshot. Pool across seeds and snapshots.
3. **Compute summary statistics** on the pooled motif
   distribution:
   - **S1** — median ρ.
   - **S2** — IQR of ρ.
   - **S3** — upper-tail log-slope (shape reading only,
     operational).
   - Bootstrap 16–84 % CIs (2000 resamples) for S1 and S2.
4. **ξ guardrail.** Per seed, compute ξ via the canonical
   40-snapshot half-decay method (GR-SC 1.7, density channel).
   Per-seed ξ must lie within 20 % of the canonical
   `ξ = 1.7575 lu`. A cell passes the guardrail iff ≥ 8/10
   seeds pass.
5. **Hinge sub-sampling.** Per cell, run the 5-point hinge
   scan `L_ray/ξ ∈ {1.00, 1.10, 1.20, 1.30, 1.40}` and verify
   flat S1, S2 to within 10 % of the cell's canonical reading.
   Any cell failing flatness triggers a Δ ≤ 0.05 refinement
   before a falsifier verdict is rendered.
6. **Verdict.** Each cell is assigned one of
   `{Confirmed, Refuted, GuardrailFailure}` per the taxonomy
   inherited from ED-SC 3.2.6.

No module globals or canonical parameters are mutated. The
driver passes `(α_filt, N_req, L_ray)` explicitly to the
motif filter; everything else (mobility law, lattice size,
seed list, step count, burn-in, snapshot cadence) is the
canonical configuration.

---

## 6. Falsifier definitions

ED-SC 3.3 inherits, by reference, the falsifier set already in
force:

- **S-F1** (unchanged, from ED-SC 3.0 rev. 2 §5.1):
  the canonical point (α_filt, N_req, L_ray/ξ) = (0.25, 4, 1.08)
  must reproduce `S1 = −1.881 ± 0.4` and `S2 = 1.271 ± 20 %`
  under the simulator of record. Violation ⇒ `Refuted`.
- **S-F2 rev. 2** (regime-based, from ED-SC 3.0 rev. 2 §5.1):
  within a contiguous regime of any hinge scan, S1 and S2 must
  be flat to within 20 %. Cross-regime drifts are **diagnostic,
  not falsifying**. Applied per-cell to the 5-point hinge
  sub-sweep of §4.
- **Resonance-mapping clause** (from ED-SC 3.0 rev. 2 §5.2):
  any new hinge introduced by a depth memo (here: `α_filt` or
  `N_req`) must be sub-sampled at Δ ≤ 0.1 across its reported
  window, with regime membership declared before falsifier
  readings are reported.
- **Canonical ξ method** (from ED-SC 3.2.6 rev. 2 §5.2):
  per-seed ξ for the guardrail uses the 40-snapshot half-decay
  method. Single-snapshot ξ is not permitted.
- **Simulator-of-record guardrail** (from ED-SC 3.1 rev. 2 §6):
  every cell must cite `r2_grf_falsifier_tests.py`
  + `ED_Update_Rule.ed_step_mobility` by filename in its output
  artefact.

No new falsifiers are introduced. The point of ED-SC 3.3 is
to **map** the filter-geometry dependence of
`f(ρ | ξ, filter)`, not to declare a new invariant.

---

## 7. Deliverables

Per cell `(α_filt, N_req)`:

- `outputs/ed_sc_3_3/pool_alpha{α}_Nreq{N}.csv` — pooled ρ
  values (one row per motif), with columns
  `(seed, snap, ρ, α_filt, N_req, L_ray, ξ_seed)`.
- `outputs/ed_sc_3_3/summary_alpha{α}_Nreq{N}.json` — cell
  summary:
  - `(α_filt, N_req, L_ray, L_ray/ξ_canonical)`
  - `N_pool, S1, S2, S3, S1_CI, S2_CI`
  - `xi_per_seed[]`, `xi_guardrail_pass_rate`
  - `hinge_subsweep[]` (5-point L_ray/ξ ∈ {1.0,…,1.4})
  - `verdict ∈ {Confirmed, Refuted, GuardrailFailure}`
  - `simulator_of_record = "r2_grf_falsifier_tests.py +
    ED_Update_Rule.ed_step_mobility"`.

Master summary:

- `outputs/ed_sc_3_3/filter_geometry_summary.json` — aggregates
  all 20 cell summaries, includes a 5 × 4 grid of
  `(S1, S2, verdict)` indexed by `(α_filt, N_req)`, and a
  `resonance_flags[]` list naming any cell whose hinge
  sub-sweep failed the S-F2 rev. 2 flatness check.

Artefact hashes must be reported alongside the summary, matching
the convention set by ED-SC 3.2.6 rev. 2.

---

## 8. Next steps

After ED-SC 3.3 closes, proceed to **ED-SC 3.4 — Multi-Parameter
Coupling**. ED-SC 3.4's pre-registration (forthcoming
`theory/ED_SC_3_4_*.md`) will:

- Sweep `(α_filt, N_req)` jointly with `ξ` (via initial-condition
  amplitude or mobility prefactor) to test whether the
  filter-geometry invariants collapse under a dimensionless
  rescaling involving ξ.
- Introduce mobility-law variants (`M(ρ)` family) per GR-SC
  1.4's NEC taxonomy, with the filter anchored at the ED-SC 3.3
  optimum identified here.
- Carry all guardrails inherited here plus any new resonance
  windows discovered by ED-SC 3.3.

ED-SC 3.5 (projected) will attempt to close the distributional
invariance statement by demonstrating that `f(ρ | ξ, filter)`
collapses to a universal form under the dimensionless coordinates
`(L_ray/ξ, α_filt, N_req)` across the Regime-I interior of the
entire `(α_filt, N_req)` grid.

---

## 9. Changelog

- **Rev. 1 (2026-04-23, this memo):** opens ED-SC 3.3.
  Pre-registers the 5 × 4 filter-geometry grid at the certified
  canonical operating point, inherits all guardrails from
  ED-SC 3.0 rev. 2, 3.1 rev. 2–3, 3.2.5, and 3.2.6 rev. 2, and
  commits to the three-way verdict taxonomy per cell.
  No numerics.
