# ED-SC 3.1 — rev. 2 Rectification Memo

**Status:** RECTIFICATION — corrects the simulator-of-record attribution,
restores the canonical baselines from the real pool artefact, and blocks
ED-SC 3.2 pending a rebuilt sweep driver.
**Supersedes:** `ED_SC_3_1_Distribution_Baselines.md` §2.1–§5 numerical
attributions. The memo's S1 median value (−1.88) survives as a number;
its attribution (to `r_star_montecarlo.py`) does not.
**Date:** 2026-04-23.

---

## 1. Summary of the regression

- The ED-SC 3.1 canonical baselines (`N = 34`, `r* ≈ −1.88`) did **not**
  come from `analysis/scripts/r_star_montecarlo.py`.
- `r_star_montecarlo.py` is **untracked** in the repository (confirmed
  by `git status`) and is **documented to return `N = 0`** at its
  shipped constants — see `analysis/ED_SC_2_0_r_star_MonteCarlo_Results.md`
  §2 (*"Because field std ≈ 0.024 ≪ δ_thr = 0.10, no stationary point
  ever clears the amplitude gate."*). It is a null-result diagnostic
  harness, not the canonical simulator.
- The 2026-04-23 reproduction run of the stock `r_star_montecarlo.py`
  (this session, `outputs/ed_sc_3_2/stock_mc_output.json`) independently
  confirmed `N = 0` across all 10 canonical seeds — the documented
  behaviour is current and reproducible.
- The true canonical pool comes from:

      analysis/scripts/ed_arch_r2/r2_grf_falsifier_tests.py

  using `ED_Update_Rule.ed_step_mobility` from the ED-SIM engine at
  `C:\Users\allen\GitHub\Emergence Universe\ED-SIM-Code`. Its output
  JSON (`r2_grf_falsifier_results.json`) records `n_total: 34,
  median: −1.8807…` for the `T1a_baseline` configuration — exactly
  the ED-SC 2.0 / 3.1 canonical statistic.
- The ED-SC 3.2 sweep driver and ED-SC 3.1 §2.1's `ξ ≈ 2.4` quote
  inherited the wrong simulator by my mistake. ED-SC 3.1 rev. 2 and
  this memo are the corrective action.

---

## 2. Simulator of record (declared)

| Item | Value |
| --- | --- |
| **Simulator of record** | `analysis/scripts/ed_arch_r2/r2_grf_falsifier_tests.py` |
| **Engine** | `ED_Update_Rule.ed_step_mobility` |
| **Engine path** | `C:\Users\allen\GitHub\Emergence Universe\ED-SIM-Code` |
| **Mobility law** | `M(p) = (1 − p)^{2.7}` |
| **α (saturation)** | `0.03` |
| **γ (coupling)** | `0.5` |
| **Noise σ** | `0.0556` |
| **α_filt** | `0.25` |
| **L_ray** | `2` |
| **N_req** | `4` (of 4 principal-axis rays) |
| **Steps** | `500` |
| **Grid** | `64 × 64` periodic |
| **Seeds** | `{77, 101, 123, 234, 456, 789, 1011, 1213, 1415, 2021}` |

The seed list differs from `r_star_montecarlo.py`'s (which contains
`234 → 789` swap and no `101`), which is itself a forensic marker: any
future memo that quotes the canonical pool must reference the
simulator-of-record seed list above.

---

## 3. Canonical baselines (re-extracted from the pool JSON)

Source: `analysis/scripts/ed_arch_r2/r2_grf_falsifier_results.json`,
entry `"T1a_baseline"`. Values taken verbatim; not recomputed.

### 3.1 Pool-level statistics

| Quantity | Value | Field in JSON |
| --- | --- | --- |
| N_total | **34** | `n_total` |
| p̂_mean | **0.1097** | `p_hat_mean` |
| p_std_mean | 0.00826 | `p_std_mean` |
| S1 — median ρ | **−1.8807** | `median` |
| S2a — Q25 | −2.6039 | `q25` |
| S2b — Q75 | −1.3333 | `q75` |
| **S2 — IQR (Q75 − Q25)** | **1.271** | (derived) |
| 95 % CI low | −2.3405 | `ci95_lo` |
| 95 % CI high | −1.4640 | `ci95_hi` |
| Pool mean | −2.199 | `mean` |
| Pool std | 1.136 | `std` |
| S3 — upper-tail log-slope | **not stored** | — |

### 3.2 S3 (tail slope) status

The `T1a_baseline` JSON stores pool-level summaries but not per-motif
records, so S3 cannot be extracted from the artefact alone. S3 is
**pending** a targeted re-run of `r2_grf_falsifier_tests.py` that emits
per-motif ρ values, or a one-off side-script that reproduces the pool
and emits the histogram. Until then, ED-SC 3.1 rev. 2 carries only
S1 and S2 as canonical.

### 3.3 Per-seed medians (for audit)

| Seed | n_motif | median ρ | p̂ |
| --- | --- | --- | --- |
| 77 | 3 | −1.305 | 0.1084 |
| 101 | 4 | −1.597 | 0.1098 |
| 123 | 4 | −2.740 | 0.1107 |
| 234 | 4 | −1.542 | 0.1086 |
| 456 | 1 | −1.158 | 0.1107 |
| 789 | 4 | −1.735 | 0.1091 |
| 1011 | 4 | −2.332 | 0.1104 |
| 1213 | 2 | −2.639 | 0.1099 |
| 1415 | 4 | −3.379 | 0.1089 |
| 2021 | 4 | −1.736 | 0.1109 |

Per-seed medians span `[−3.38, −1.16]`; the single-seed instability
that misled the original `r* = −1.304` estimate is visible directly in
seed 77's value of −1.305 (matched to three digits) versus the pool
median −1.881.

### 3.4 ED-SC 3.1 replacements

The ED-SC 3.1 §2.1 "canonical operating point" table is superseded by:

- `N = 34` (from simulator of record)
- `p̂ ≈ 0.1097` (from simulator of record)
- S1 = −1.881 (from simulator of record)
- S2 = 1.271 (from simulator of record)
- S3 — pending
- The `σ₀`, `σ₁`, `σ₂`, `ξ` entries in ED-SC 3.1 §2.1 are
  **invalidated** until re-measured on the ED-SIM engine (§4).

The exGauss fit parameters in ED-SC 3.1 §3.2 `(μ, σ, τ)` are
**withdrawn** — they were back-solved against the wrong simulator's
non-existent pool and should not be cited.

---

## 4. ξ status

- ED-SC 3.1's quoted `ξ ≈ 2.4 lattice units` was never measured on the
  simulator of record. It was inferred from a GRF dictionary argument
  applied to the plain R2 SPDE integrator, which is not the canonical
  simulator.
- `ξ` must be **re-measured on the ED-SIM mobility engine** using the
  GR-SC 1.7 half-decay definition: the smallest lag at which
  `ξ_φ(r)/σ₀² ≤ 1/2`, evaluated on the snapshot population produced
  by `ed_step_mobility` with the canonical parameters in §2.
- Until `ξ` is re-measured, **all hinge coordinates in ED-SC 3.2 are
  non-canonical**, including G3. The "G3 = 1.08" anchor was derived
  from the wrong-simulator `ξ`.

---

## 5. Consequences for ED-SC 3.2

- The L_ray/ξ scan in `ED_SC_3_2_LrayXi_Scan.md` is **invalidated
  except for the spectral-triad stability check**. The protocol
  demonstrated that the sweep driver holds `(σ₀, σ₁, σ₂)` stable
  across hinge points to < 0.1 %; that methodological result
  transfers to the rebuilt driver unchanged.
- The grid definition, the exGauss ansatz choice, the S-F2 weak-reading
  registration, the S1/S2/S3 summary-statistic framework, and the
  pre-registered predicted curves all carry over structurally — they
  just must be re-anchored to the correct simulator.
- The scan itself must be re-executed on the ED-SIM engine; the
  2026-04-23 null result does not evaluate S-F2.
- `analysis/scripts/ed_sc_3_2_lrayxi_scan.py` must be **rewritten** to
  drive `ED_Update_Rule.ed_step_mobility`, not `r_star_montecarlo.py`.
  All current-memo scan outputs (`outputs/ed_sc_3_2/scan_summary.json`,
  `scan_progress.log`) are retained as audit artefacts of the
  regression but are not canonical ED-SC 3.2 results.

---

## 6. Guardrail for all future ED-SC 3.x work

**New standing rule, effective 2026-04-23:**

> **Every ED-SC 3.x numerical claim must cite the simulator of record
> by filename.** Any claim without such a citation is invalid.

The simulator of record is defined in §2. Changes to the simulator of
record require a rectification memo of this form; silent substitution
is forbidden.

Applies to ED-SC 3.0 §5 falsifier triggers, ED-SC 3.1 baselines,
ED-SC 3.2 scan outputs, and all ED-SC 3.3+ depth memos.

---

## 7. Next required actions (ordered)

1. **Re-measure ξ** on the ED-SIM engine using the GR-SC 1.7
   half-decay definition. Deliverable: a short note + JSON in
   `outputs/ed_sc_3_1/xi_canonical.json` recording ξ and its seed-pool
   variance at the canonical parameters in §2.
2. **Rebuild the ED-SC 3.2 sweep driver** against the simulator of
   record. Replace `ed_sc_3_2_lrayxi_scan.py` with a driver that
   imports `ED_Update_Rule.ed_step_mobility` and varies `L_ray` at
   fixed `(α_filt, N_req, α, γ, σ)`.
3. **Re-anchor the hinge grid** using the corrected ξ from step 1.
   The canonical G3 becomes `L_ray / ξ_canonical` for `L_ray = 2`;
   other grid points scale accordingly. Grid regions that were
   labelled "sub-coherence" or "supra-coherence" may shift relative
   to G3; that is expected.
4. **Re-run ED-SC 3.2** on the rebuilt driver. Populate the pending
   rows in §3.3 and §4.3 of `ED_SC_3_2_LrayXi_Scan.md` with genuine
   simulator-of-record output, or issue a rev. 2 of that memo if
   structural changes are required.
5. **Only then reopen ED-SC 3.3.** ED-SC 3.3's filter-geometry sweep
   depends on the corrected hinge map and cannot be designed ahead of
   step 4.

Also required at step 1 or step 2:
- Extend the simulator of record to emit per-motif `ρ` records so S3
  (tail log-slope) can be computed without a full re-derivation.

---

## 8. Artefacts referenced by this memo

- `analysis/scripts/r_star_montecarlo.py` — untracked, null-diagnostic;
  **not** simulator of record.
- `analysis/scripts/ed_arch_r2/r2_grf_falsifier_tests.py` — simulator
  of record.
- `analysis/scripts/ed_arch_r2/r2_grf_falsifier_results.json` —
  canonical pool artefact.
- `analysis/ED_SC_2_0_r_star_MonteCarlo_Results.md` §2 — prior
  documentation that `r_star_montecarlo.py` returns N=0.
- `outputs/ed_sc_3_2/stock_mc_output.json`,
  `outputs/ed_sc_3_2/stock_spectra.json`,
  `outputs/ed_sc_3_2/scan_summary.json` — this session's regression
  audit artefacts; retained for traceability only.
- `theory/ED_SC_3_1_Distribution_Baselines.md` — to be superseded by
  a rev. 2 that carries the corrected simulator attribution; until
  rev. 2 is written, this memo is the authoritative correction.
- `theory/ED_SC_3_2_LrayXi_Scan.md` — scan invalidated per §5;
  guardrail §6 applies to all future rev.

---

*End of rectification memo. No ED-SC 3.x numerical claim may be made
against `r_star_montecarlo.py`. The simulator of record is the only
accepted source.*
