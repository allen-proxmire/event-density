# DM.14-EXEC — Production Run Checklist

**Date:** 2026-04-25
**Arc:** Dark Matter (DM) — operational checklist
**Status:** Procedure committed. This memo is read by the analyst at the start of the production compute run and followed verbatim.
**Predecessor:** DM.14 (notebook construction plan).
**Successor:** DM.5 (real, not TEMPLATE) — written from the run log after the production run completes.
**Target:** `ed-lab/analysis/notebooks/05_dm2_sparc_fits.ipynb`

This memo is operational, not architectural. No design decisions. No code. No fabricated numbers. The procedure for starting, running, and verifying the production compute run.

---

## 1. Preconditions

The production run does not begin until **all** of the following are satisfied. Verify each before opening the notebook.

### 1.1 Engineering completeness

- [ ] DM.7 (`disk_geometry.py`) landed; tests pass.
- [ ] DM.8 (`activity_source.py`) landed; tests pass.
- [ ] DM.9 (`pde_solver.py`) landed; tests pass.
- [ ] DM.10 (`boundary_conditions.py`) landed; tests pass; DM.9 tests still pass after refactor.
- [ ] DM.11 (`run_single_galaxy.py`) landed; tests pass.
- [ ] DM.12 (`run_full_sample.py`) landed; non-slow tests pass; slow tests run at least once.
- [ ] DM.13 (`validation_tests.py`) landed; **production-grid validation suite passes**; DM.4 Validation Gate marked unblocked in run log.
- [ ] DM.14 (notebook `05_dm2_sparc_fits.ipynb`) landed; notebook runs top-to-bottom on the smoke-test configuration without raising.

### 1.2 Repository state

- [ ] `git status` is clean in `ed-lab` (no uncommitted edits).
- [ ] `git status` is clean in `event-density` (no uncommitted edits to arc memos).
- [ ] `ed-lab` HEAD SHA recorded: __________________ (write here at run start).
- [ ] `event-density` HEAD SHA recorded: __________________ (write here at run start).

### 1.3 Data availability

- [ ] SPARC tables present at `ed-lab/data/SPARC/` (Table 1 and Table 2).
- [ ] Sufficient disk space at `ed-lab/analysis/outputs/` (at least 2 GB free for HDF5 outputs).

### 1.4 Compute environment

- [ ] Machine has at least 4 physical CPU cores (8 preferred for parallelism).
- [ ] Machine will not be put to sleep or interrupted during the run.
- [ ] Power supply stable (laptops on charger).
- [ ] Network connectivity not required during the run, but `git push` must work afterwards.

If any precondition is unsatisfied, do not begin the production run. Address the gap first.

---

## 2. Production-run configuration

### 2.1 Threading and RNG environment

These are set in the notebook's Section 2 (environment-setup cell) and must take effect *before* numpy is imported. The values are fixed by the notebook design:

- `OMP_NUM_THREADS = 1`
- `MKL_NUM_THREADS = 1`
- `OPENBLAS_NUM_THREADS = 1`
- `numpy.random.seed(42)`
- `random.seed(42)`
- `joblib.parallel_config(backend="loky")`

After running Section 2, verify by inspecting the printout: `OMP_NUM_THREADS=1` and `numpy.show_config()` should report a single-thread BLAS.

### 2.2 Tier level per section

The production-mode tier settings (uncomment the "FOR REAL RUN" lines in the notebook before starting):

| Section | Tier | Notes |
|---|---|---|
| Validation suite (Section 6) | Full production grid | Not "tier" applicable; runs all three analytic tests |
| NGC 3198 (Section 7) | Tier-3 | Self-consistency loop active |
| 30-galaxy subset (Section 8) | Tier-3 | Inside Nelder-Mead optimizer |
| Cross-validation (Section 8) | Tier-1 | Documented compromise: full Tier-3 CV is ~30 hours; Tier-1 CV is ~2 hours and gives a useful R_cv estimate |
| Full sample (Section 9) | Tier-3 | Final production verdict input |

### 2.3 Expected wall-clock budget

| Section | Expected wall time |
|---|---|
| Section 6 (validation) | 5–10 minutes |
| Section 7 (NGC 3198 Tier-3) | 3–8 minutes |
| Section 8 (30-galaxy global fit, Nelder-Mead, Tier-3, 8-core parallel) | 5–7 hours |
| Section 8 (Tier-1 cross-validation) | 1–2 hours |
| Section 9 (full sample, Tier-3, 8-core parallel) | 1–2 hours |
| Sections 10–12 (analysis layer) | 5–15 minutes |
| Section 13 (fill cheat sheet) | seconds |

**Total: approximately 8–12 hours.** Plan for an overnight run.

### 2.4 Outputs

Outputs are written to:

> `ed-lab/analysis/outputs/dm2_<DATE>_<SHA7>/`

where `<DATE>` is the run date (YYYY-MM-DD) and `<SHA7>` is the first 7 characters of the `ed-lab` HEAD SHA. Expected files:

- `dm2_run_log.json` — comprehensive run log; the source of truth for DM.5.
- `validation_report.json` — Section 6 output.
- `dm2_per_galaxy.csv` — Section 9 output.
- `dm2_residuals.csv` — Section 9 output.
- `dm2_global_fit_results.json` — Section 8 output.
- `dm2_btfr.json` — Section 11 output.
- `dm2_T_fields.h5` — full T-fields per galaxy, compressed.
- Plot PNGs from Sections 7, 8, 10, 11, 12.

---

## 3. Execution checklist

Follow these steps in order. Do not skip ahead.

### 3.1 Pre-run

1. [ ] Open a fresh terminal at the `ed-lab/` repository root.
2. [ ] Confirm preconditions §1 are all checked.
3. [ ] Record start timestamp: __________________ (write here).
4. [ ] Open the notebook: `jupyter lab analysis/notebooks/05_dm2_sparc_fits.ipynb`.
5. [ ] In the notebook, **Restart Kernel and Clear All Outputs** (Kernel menu → Restart & Clear Output).
6. [ ] Edit Sections 8 and 9: locate every "FOR REAL RUN" comment, uncomment the production line, and re-comment the smoke-test line. Save the notebook.
7. [ ] Verify the notebook is the only large process the machine will be running.

### 3.2 Sections 1–6 (validation)

8. [ ] Run Sections 1–5 sequentially. Verify each completes without error.
9. [ ] Run Section 6 (validation suite). **Watch the output.**
10. [ ] If any validation test fails: **HALT**. Do not proceed. Diagnose the failure and re-run from the start. The validation gate is the precondition for everything downstream.
11. [ ] If all three validation tests pass: confirm in the cell output and in `validation_report.json`. Proceed.

### 3.3 Section 7 (NGC 3198)

12. [ ] Run Section 7. Expected runtime: 3–8 minutes.
13. [ ] Observe the cell output. Record:
    - Outer iterations to convergence: ________
    - Wall time: ________
    - Max |Δv|: ________
14. [ ] If NGC 3198 fails the pass criteria (DM.4 §3.5: max |Δv| > 30 km/s, oscillatory divergence, or solver pathology): **HALT**. Do not scale to 30 galaxies. Diagnose.
15. [ ] If NGC 3198 passes: confirm the three plots saved correctly. Proceed.

### 3.4 Section 8 (30-galaxy global fit)

16. [ ] Note 30-galaxy section start time: __________________ (write here).
17. [ ] Start Section 8. **This is the longest single computation in the run.** Do not interrupt.
18. [ ] Periodic monitoring is permitted but not required. The cell output should print Nelder-Mead progress lines.
19. [ ] When the cell completes, note end time: __________________ (write here).
20. [ ] Inspect:
    - Optimizer evaluations to convergence: ________
    - R_cv: ________
    - Fold count with successful evaluation: ________ / 5
21. [ ] If Gate 4 criteria fail (DM.4 §4.5): **HALT**. Do not run full sample. The 30-galaxy fit is unstable; diagnose what it is telling us.
22. [ ] If Gate 4 passes: proceed.

### 3.5 Section 9 (full sample)

23. [ ] Note full-sample start time: __________________ (write here).
24. [ ] Run Section 9. Expected runtime: 1–2 hours at 8-core parallelism.
25. [ ] When complete, note end time: __________________ (write here).
26. [ ] Inspect:
    - Galaxies attempted: ________
    - Galaxies failed (catastrophic): ________
    - Mean χ²_red: ________
27. [ ] If catastrophic failure rate > 5% of sample: review failures; consider Tier-2 fallback (see DM.4 risk #2 mitigation). If failure rate is acceptable, proceed.

### 3.6 Sections 10–13 (analysis and verdict)

28. [ ] Run Section 10 (universality test).
29. [ ] Run Section 11 (BTFR).
30. [ ] Run Section 12 (RC #1 + verdict).
31. [ ] Observe the verdict printout. Record: ________ (one of PASS / PARTIAL_universality / PARTIAL_BTFR / FAIL).
32. [ ] Run Section 13 (fill cheat sheet). The cheat sheet prints the run-log keys mapped to DM.5-TEMPLATE placeholders.
33. [ ] Record run end timestamp: __________________ (write here).

### 3.7 Post-run verification

34. [ ] Open `ed-lab/analysis/outputs/dm2_<DATE>_<SHA7>/`. Verify:
    - [ ] `dm2_run_log.json` exists and is well-formed JSON.
    - [ ] `validation_report.json` exists.
    - [ ] `dm2_per_galaxy.csv` exists with rows for the full sample.
    - [ ] `dm2_residuals.csv` exists.
    - [ ] `dm2_global_fit_results.json` exists.
    - [ ] `dm2_btfr.json` exists.
    - [ ] `dm2_T_fields.h5` exists.
    - [ ] All expected plot PNGs exist.
35. [ ] Verify `dm2_run_log.json` contains all keys mapped in DM.14 §1.2 Section 13: `validation_gate`, `ngc3198_result`, `subset_30_fit`, `full_sample_run`, `universality_test`, `btfr_analysis`, `verdict`.
36. [ ] Confirm `verdict.final` matches the verdict observed in step 31.
37. [ ] Commit the output directory and any notebook output cells:

    ```
    git add ed-lab/analysis/outputs/dm2_<DATE>_<SHA7>/
    git add ed-lab/analysis/notebooks/05_dm2_sparc_fits.ipynb
    git add ed-lab/arcs/arc-DM/run_log.md
    git commit -m "DM production run complete — verdict: <VERDICT>"
    git push
    ```

38. [ ] Append to `ed-lab/arcs/arc-DM/run_log.md`: `<DATE>: Production run complete. Verdict: <VERDICT>. Run log at outputs/dm2_<DATE>_<SHA7>/dm2_run_log.json.`

---

## 4. DO NOT

The following are forbidden during the production run. Each is a discipline commitment, not a suggestion.

- **DO NOT edit any code** in `ed-lab/simulations/edsim/dm/` during the run. If a bug surfaces, halt the run and fix in a separate commit; restart the run from the top.
- **DO NOT modify κ_act or α manually** between sections. The 30-galaxy fit produces these; the full sample uses them unchanged. Any manual adjustment invalidates the verdict.
- **DO NOT compute any DM.5 quantity by hand.** Every number in DM.5 traces to `dm2_run_log.json`. If a value is needed but not in the log, that is a DM.14 implementation gap; halt and fix the notebook, do not derive the value manually.
- **DO NOT re-run individual cells out of order** once Section 7 has started. The notebook's reproducibility guarantee depends on top-to-bottom execution. Out-of-order execution corrupts the run log.
- **DO NOT skip the validation gate** even if "I'm sure it'll pass." The gate is the precondition; skipping it forfeits the verdict's credibility.
- **DO NOT reduce the tier mid-run** to save time. If Tier-3 is too slow, halt and re-plan; do not silently downgrade to Tier-2 mid-run.
- **DO NOT continue if NGC 3198 fails** Gate 3. Scaling to 30 or 150 galaxies with a known bad NGC 3198 produces invalid results faster.
- **DO NOT push the notebook with cleared outputs.** The output cells are part of the run record; clearing them after a successful run defeats reproducibility.

---

## 5. Failure handling

If the run fails at any gate:

1. Capture the failure: copy the error message and the relevant cell output into a new file at `ed-lab/arcs/arc-DM/failures/<DATE>_<gate>.md`.
2. Commit the failure record: `git add` and `git commit` with message `DM production run failed at <gate>: <one-line summary>`.
3. Diagnose. The failure mode determines next steps:
   - **Validation failure:** the validation suite from DM.13 has a runtime issue. Halt; fix in a coding session, not during the production run.
   - **NGC 3198 failure:** the pipeline has a problem at the single-galaxy level. Diagnose via the NGC 3198 section's diagnostic plots; fix in a coding session.
   - **30-galaxy convergence failure:** the optimizer is unstable. May indicate κ_act non-universality (a real finding rather than a bug). Examine the per-galaxy χ² distribution before deciding.
   - **Full-sample catastrophic failures > 5%:** investigate the failure modes; may be data-quality issues with specific galaxies. Tier-2 fallback for those galaxies is documented in DM.4 risk #2.
4. After diagnosis and fix, restart the run from precondition §1.

A failure is not a setback. It is a pre-registered finding. The run log records the failure mode, and DM.5 (when written) reports it as the verdict.

---

## 6. After the run

When the production run completes successfully (any of the four verdicts: PASS, PARTIAL_universality, PARTIAL_BTFR, FAIL), the next step is writing DM.5 — the real verdict memo.

DM.5 is **not** written during the production run. It is written by:

1. Opening `arcs/arc-DM/DM_5_verdict_TEMPLATE.md`.
2. Saving a copy as `arcs/arc-DM/DM_5_verdict.md` (drop the "_TEMPLATE" suffix).
3. Filling each `[TBD: ...]` placeholder by reading the corresponding value from `dm2_run_log.json`. The Section 13 cheat sheet (printed during the production run) maps placeholders to keys.
4. Removing the "THIS IS A TEMPLATE" header line at the top.
5. Updating the date and run metadata.
6. Reading the §6 verdict explanation and writing the 3–5 sentence narrative.
7. Reading the §7 recommended-next-step section, choosing the matching subsection (7.1, 7.2, 7.3, or 7.4) based on the verdict, and copying its content as the explicit recommendation.
8. Committing: `git commit -m "DM.5 verdict: <VERDICT>"`.

The DM.5 memo is short. It contains real numbers, a real verdict, and a concrete recommendation for DM.6 (which is determined by the verdict per the four-way branch architecture).

---

## Recommended Next Step

After the production run completes per §3 and the post-run verification in §3.7 is satisfied, open `arcs/arc-DM/DM_5_verdict_TEMPLATE.md` and save a copy at `arcs/arc-DM/DM_5_verdict.md`; then fill every `[TBD: ...]` placeholder by reading the corresponding value from `ed-lab/analysis/outputs/dm2_<DATE>_<SHA7>/dm2_run_log.json` using the Section 13 cheat sheet that the notebook printed at the end of the run; remove the "THIS IS A TEMPLATE" header; write the §6.4 verdict narrative (3–5 sentences) using only values from the run log; copy the matching §7 sub-recommendation into §7.5; commit the file with message `DM.5 verdict: <VERDICT>` and push. Do not compute any value manually; do not deviate from the template structure; do not write DM.5 before the production run completes.