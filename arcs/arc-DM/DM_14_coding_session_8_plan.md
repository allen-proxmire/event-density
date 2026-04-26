# DM.14 — Coding Session 8 Plan: Reproducibility Notebook

**Date:** 2026-04-25
**Arc:** Dark Matter (DM) — fifteenth memo
**Status:** Notebook-construction plan committed. This memo is read by the analyst at the start of Session 8 and followed without further design decisions.
**Predecessor:** DM.13 (Session 7 plan — `validation_tests.py`).
**Target file:** `ed-lab/analysis/notebooks/05_dm2_sparc_fits.ipynb`
**Session goal:** End-to-end reproducibility notebook that orchestrates validation → NGC 3198 → 30-galaxy fit → full-sample run, with deterministic settings and complete output logging. After this session, every number that goes into DM.5 comes from a logged computation in a notebook that can be re-run by an independent operator.

This memo contains no Python code. It specifies the notebook structure, the cells, the outputs, and the reproducibility guarantees. Implementation is the analyst's task.

**Note on session character.** This is the last engineering session in the DM arc. Sessions 1–7 wrote modules; Session 8 wires them into the reproducibility artifact that turns "the code exists" into "the analysis is reproducible." After Session 8 lands, the remaining work is **compute**, not code: actually running the notebook, filling in DM.5-TEMPLATE with the resulting numbers, producing the real DM.5 verdict.

**Prerequisite:** DM.7–DM.13 must be fully landed. The notebook depends on every prior module being functional and tested.

---

## 1. Notebook specification

### 1.1 File location and naming

- Path: `ed-lab/analysis/notebooks/05_dm2_sparc_fits.ipynb`.
- Numbering convention: matches existing `03_galaxy15_lag.ipynb` and `04_udm_mobility.ipynb`. The number `05` reflects its position in the broader analysis-notebook sequence.
- Output directory: `ed-lab/analysis/outputs/dm2_<DATE>_<SHA>/` where `<DATE>` is the run date (YYYY-MM-DD) and `<SHA>` is the first 7 characters of the `ed-lab` HEAD SHA at run time.

### 1.2 Notebook sections

The notebook has 13 sections, each one a markdown cell followed by one or more code cells. Section structure is fixed; analyst implements the bodies.

#### Section 1 — Header and metadata

A markdown cell with:
- Title: "DM Arc — SPARC Confrontation Reproducibility Notebook"
- Subtitle: "DM.5 Source — every number in the verdict memo originates here"
- One-paragraph description: this notebook executes the full DM.4 protocol against the SPARC sample and produces the artifacts needed to fill DM.5-TEMPLATE.
- Date of last edit: filled at run time.
- Reference list: DM.0–DM.13 memos.

#### Section 2 — Environment and reproducibility setup

A code cell that performs deterministic configuration **before any other imports**:

- `os.environ["OMP_NUM_THREADS"] = "1"` — prevents BLAS multi-threading non-determinism.
- `os.environ["MKL_NUM_THREADS"] = "1"` — same for Intel MKL.
- `os.environ["OPENBLAS_NUM_THREADS"] = "1"` — same for OpenBLAS.
- `numpy.random.seed(42)` — deterministic numpy RNG.
- `random.seed(42)` — deterministic Python RNG.
- `joblib.parallel_config(backend="loky")` — deterministic joblib backend.
- A second cell logs versions: Python, numpy, scipy, joblib, pandas, h5py.

**Critical.** The thread-environment variables must be set *before* importing numpy or scipy. If they are set after, the configuration is silently ignored. The first code cell does only this; the import cell comes second.

#### Section 3 — Imports

A single code cell with all imports needed for the notebook:
- Standard library: `os`, `json`, `subprocess`, `pathlib`, `datetime`.
- Third-party: `numpy`, `pandas`, `matplotlib.pyplot`, `seaborn`.
- DM modules: `from edsim.dm.run_single_galaxy import run_single_galaxy, SparcGalaxy`, `from edsim.dm.run_full_sample import (everything needed)`, `from edsim.dm.validation_tests import run_validation_suite, assert_validation_passed`.
- IPython display utilities for tables and plots.

#### Section 4 — SHA logging and run log initialization

A code cell that:
- Captures `ed-lab` HEAD SHA via `subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ED_LAB_PATH)`.
- Captures `event-density` HEAD SHA the same way.
- Constructs `output_dir = Path(f"ed-lab/analysis/outputs/dm2_{date}_{sha[:7]}/")` and creates it if needed.
- Constructs `run_log_path = output_dir / "dm2_run_log.json"`.
- Initializes the run log dict with: notebook execution timestamp, SHAs, environment versions, configuration parameters.
- Saves the initial run log JSON.

The run log is appended to throughout the notebook; the final state captures every number used in DM.5.

#### Section 5 — Configuration parameters

A markdown cell explaining the parameters, followed by a code cell defining a single `SampleConfig` instance with:
- Paths to SPARC tables.
- D_T, λ at production values from `pde_solver.py` constants.
- Quality cuts: Q ≤ 2, inclination ≥ 30°.
- Optimizer settings.
- Output directory (from Section 4).
- Seed = 42.

The parameters are logged to the run log immediately.

#### Section 6 — Validation gate

A markdown cell explaining: "Before any SPARC galaxy is run, the analytic-validation suite must pass. This is DM.4 Gate 2."

A code cell that:
- Calls `run_validation_suite()` on the production grid.
- Asserts `all_passed == True`. If False, the cell raises and halts the notebook.
- Logs each test's result (test name, metric value, tolerance, passed) to the run log.
- Saves `validation_report.json` to `output_dir`.

A markdown cell explaining: "Validation gate **PASSED**. SPARC pipeline cleared to run." (Or: an error halts execution before this cell.)

#### Section 7 — NGC 3198 proof-of-concept (DM.4 Gate 3)

A markdown cell explaining: "Before scaling to 30 or 150 galaxies, NGC 3198 is run as the canonical proof-of-concept per DM.4 §3."

Code cells:
1. Load NGC 3198 from SPARC tables.
2. Construct kappa_act and α at the dimensional anchor (from DM.4 §3.2).
3. Call `run_single_galaxy(galaxy=ngc3198, kappa_act=kappa_act_anchor, alpha=0.5, D_T=D_T, lam=lam, tier=3, verbose=True)`.
4. Print results: χ²_red, outer iterations, wall-time, max |Δv|.
5. Apply DM.4 §3.5 pass criteria:
   - |v_pred(R) − v_obs(R)| < 30 km/s for R ∈ [5, 25] kpc.
   - Outer loop converged in < 50 iterations.
   - No NaN, no negative T outside active region.
6. **Plot:** v_pred vs. v_obs vs. v_baryon as a function of R, with shaded uncertainty band on v_obs. Save PNG to output_dir.
7. **Plot:** T(R, z=0) on a log-y axis, showing the temporal-tension halo profile. Save PNG.
8. **Plot:** outer-loop convergence trace (max residual per iteration). Save PNG.
9. Log the result to the run log under key `ngc3198_result`.

A final markdown cell stating: "NGC 3198 gate **PASSED** / FAILED" based on the criteria. If FAILED, the analyst halts and diagnoses before scaling up.

#### Section 8 — 30-galaxy global fit (DM.4 Gate 4)

A markdown cell explaining: "30-galaxy stratified subset; global Nelder-Mead fit of (κ_act, α); cross-validation."

Code cells:
1. Load full SPARC catalog; apply quality cuts.
2. Construct stratified 30-galaxy subset (5 mass bins × 6 each).
3. Run global fit via `global_fit(subset, config)` — this is the expensive step (~6 hours at Tier-3 + 8-core parallel; ~30 hours at Tier-3 + serial; ~30 minutes at Tier-1 + 8-core).
4. Print fitted (κ_act, α) with optimizer convergence message.
5. Run cross-validation via `cross_validate(subset, config, n_folds=5)`.
6. Print R_cv and per-fold ratios.
7. Apply DM.4 §4.5 gate criteria:
   - Optimizer converged in < 50 evaluations.
   - R_cv ∈ [0.9, 1.5].
   - Catastrophic failures ≤ 5/30.
8. **Plot:** χ²_red distribution across the subset. Save PNG.
9. **Plot:** v_pred vs. v_obs grid (5 × 6 mini-panels per stratification bin). Save PNG.
10. Log fitted parameters and CV statistics to the run log under `subset_30_fit`.

A final markdown cell: "30-galaxy fit gate **PASSED** / FAILED."

#### Section 9 — Full-sample run

A markdown cell explaining: "Full SPARC sample (~150 galaxies) run at the globally-fitted (κ_act, α). No further fitting; this is the production verdict input."

Code cells:
1. Run `run_sample(full_galaxies, kappa_act=fitted, alpha=fitted, ...)` with parallelism enabled.
2. Print sample-wide χ²_red distribution stats: mean, median, σ, 90th percentile.
3. Print catastrophic-failure count and IDs.
4. Save per-galaxy results to `dm2_per_galaxy.csv`.
5. Save residuals to `dm2_residuals.csv`.
6. Save T(R, z) fields to `dm2_T_fields.h5` (HDF5 with one group per galaxy).
7. Log to the run log under `full_sample_run`.

#### Section 10 — Universality test

A markdown cell explaining: "Per-galaxy κ_act distribution and Spearman correlations against galaxy properties — RC #2 detection."

Code cells:
1. Call `compute_kappa_per_galaxy(full_galaxies, alpha_global, ...)`.
2. Call `test_universality(kappa_per_galaxy, galaxy_properties)`.
3. Print σ(log κ_act) / mean and the four Spearman correlations.
4. Apply RC #2 criteria.
5. **Plot:** histogram of log κ_act with the universality threshold annotated. Save PNG.
6. **Plot:** scatter of κ_act vs. each of {log M_b, T-type, log SB, log sSFR}. 4-panel figure. Save PNG.
7. Log to run log under `universality_test`.

#### Section 11 — BTFR analysis

A markdown cell explaining: "Predicted v_∞ extracted from each galaxy's v_pred; slope fit against M_b — RC #3 detection."

Code cells:
1. Call `compute_btfr(full_galaxies, results)`.
2. Print slope, scatter, intercept, Δ_offset.
3. Apply RC #3 criteria.
4. **Plot:** log v_∞ vs. log M_b across the sample, with fitted line, error bars on both axes, and the empirical SPARC BTFR for comparison. Save PNG.
5. Log to run log under `btfr_analysis`.

#### Section 12 — RC #1 detection and verdict

A markdown cell explaining: "Stratified residual analysis for shape failure — RC #1 detection. Final verdict assignment."

Code cells:
1. Call `detect_rc1(results, radial_bins=...)`.
2. Print median |⟨Δv⟩| in each radial bin.
3. Apply RC #1 criteria.
4. Call `assign_verdict(rc_1_fired, rc_2_fired, rc_3_fired)`.
5. Print final verdict: PASS / PARTIAL_universality / PARTIAL_BTFR / FAIL.
6. **Plot:** stratified residuals by radial bin, mass bin, morphology, SB. Multi-panel figure. Save PNG.
7. Log RC results and final verdict to run log under `verdict`.

#### Section 13 — DM.5-TEMPLATE fill instructions

A markdown cell with explicit instructions for filling DM.5 from the notebook outputs:

> The verdict in §6 of DM.5-TEMPLATE is determined by `verdict.final` in `dm2_run_log.json`. Each `[TBD: ...]` placeholder in DM.5-TEMPLATE corresponds to a specific key in the run log:
>
> - `[TBD: best-fit κ_act ± 1σ]` ← `subset_30_fit.kappa_act_fit` and `subset_30_fit.kappa_act_uncertainty`.
> - `[TBD: BTFR slope ± 1σ]` ← `btfr_analysis.slope` and `btfr_analysis.slope_sigma`.
> - `[TBD: RC #1/2/3 fired?]` ← `verdict.rc_1_fired`, `verdict.rc_2_fired`, `verdict.rc_3_fired`.
> - `[TBD: final verdict]` ← `verdict.final`.
> - (etc.)
>
> The DM.5 verdict memo is written by reading values from `dm2_run_log.json` and pasting them into the corresponding template fields. No manual numerical work; no recomputation.

A code cell that prints a "DM.5 fill-in cheat sheet" — a JSON-formatted dump of the run log's verdict-relevant subset, formatted for direct copy-paste into the template.

---

## 2. Reproducibility guarantees

### 2.1 Deterministic execution

The notebook commits to:

- **Single-threaded BLAS** (Section 2). Multi-threaded BLAS produces order-of-summation non-determinism in vector operations.
- **Fixed RNG seeds** (Section 2). Numpy and Python RNGs both seeded to 42.
- **Joblib loky backend** (Section 2). Other backends (e.g., threading) introduce additional non-determinism.
- **No hidden state from previous notebook executions.** The run-log dict is reset at the top of every run; output files are written to a SHA-tagged subdirectory.
- **Deterministic SPARC catalog filtering.** Stratified sampling within mass bins uses the seed; ties broken in a fixed order (alphabetical by galaxy ID after primary sort).

A re-run of the notebook on the same code SHA produces an identical `dm2_run_log.json` modulo timestamps and wall-time fields.

### 2.2 Logging completeness

Every value that goes into DM.5 must appear in `dm2_run_log.json`. The run-log keys mapped to DM.5 sections:

| DM.5 section | Run-log key |
|---|---|
| §1 Validation gate | `validation_gate` |
| §2 NGC 3198 | `ngc3198_result` |
| §3 30-galaxy fit | `subset_30_fit` |
| §4 Full-sample run | `full_sample_run` |
| §5 Universality | `universality_test` |
| §6 BTFR | `btfr_analysis` |
| §7 RC #1 / verdict | `verdict` |

Each key holds a sub-dict with all the numerical values, status flags, and diagnostic info needed.

### 2.3 SHA tagging

- The output directory name includes the `ed-lab` SHA prefix.
- The run log stores SHAs of both `ed-lab` and `event-density` at run time.
- A re-run on a different SHA produces a different output directory; a re-run on the same SHA overwrites the same directory.

### 2.4 Number provenance discipline

The DM.5 verdict memo is filled by reading values from `dm2_run_log.json`. Manual numerical work is forbidden. If a value is needed for DM.5 but not in the run log, the notebook is incomplete — add a logging step rather than computing it manually.

This discipline mirrors the program's broader commitment to reproducibility: every number on the public verdict ledger must be traceable to a logged computation.

---

## 3. Two-hour notebook-construction plan

The notebook is large in section count but each section is short. The two-hour plan covers Sections 1–6 (header through validation gate); Sections 7–13 extend into hours 2–4.

### 3.1 Hour 0:00 — 0:15 — Setup and Section 1

- Verify DM.7–DM.13 are landed: `pytest ed-lab/simulations/edsim/dm/tests/` passes.
- Create `ed-lab/analysis/notebooks/05_dm2_sparc_fits.ipynb`.
- Add Section 1 (header markdown cell).
- Add Section 2 (environment setup: OMP_NUM_THREADS, RNG seeds, joblib backend).
- Add Section 3 (imports).

**Checkpoint.** Notebook opens in Jupyter; Section 2 runs without error; imports succeed.

### 3.2 Hour 0:15 — 0:35 — Section 4 (SHA logging) and Section 5 (config)

- Add Section 4: SHA capture, output_dir construction, run-log initialization.
- Add Section 5: SampleConfig instantiation; log to run log.

**Checkpoint.** SHA prints correctly; output directory is created; run log JSON exists with initial fields.

### 3.3 Hour 0:35 — 0:55 — Section 6 (validation gate)

- Add Section 6: call `run_validation_suite`; assert pass; log results.
- Run the section. If validation fails, halt and diagnose (this means the validation suite from DM.13 has a runtime issue).

**Checkpoint.** Validation gate passes; `validation_report.json` written.

### 3.4 Hour 0:55 — 1:35 — Section 7 (NGC 3198)

- Add Section 7: load NGC 3198, run pipeline, apply pass criteria, generate plots, log result.
- Run the section.

**Checkpoint.** NGC 3198 runs end-to-end (this takes ~3–8 minutes); plots saved; result logged.

### 3.5 Hour 1:35 — 2:00 — Section 8 (30-galaxy fit) — stub only

- Add Section 8 markdown and code cells.
- **Do not run the actual 30-galaxy fit during Session 8.** That is a 6-hour compute task and belongs to a separate compute session.
- Replace the actual `global_fit(...)` call with a smoke test on a 5-galaxy subset at Tier-1 (~5 minutes) to verify the cells work.
- Document in a markdown cell: "**FOR REAL RUN:** uncomment the 30-galaxy production-Tier-3 line and re-execute. Estimated runtime: 6 hours."

**Checkpoint.** Section 8 cells execute on the smoke-test subset.

End of two-hour notebook-construction block. Sections 9–13 extend into hours 2–4.

---

## 4. Hours 2–4 — Sections 9–13 + smoke test

### 4.1 Hour 2:00 — 2:30 — Sections 9–10

- Add Section 9 (full-sample run) — stub similarly to Section 8. **Do not run the actual full sample.**
- Add Section 10 (universality test) — runs on whatever results Section 9 produces (smoke-test results during construction).

### 4.2 Hour 2:30 — 3:00 — Sections 11–12

- Add Section 11 (BTFR analysis).
- Add Section 12 (RC #1 detection and verdict assignment).
- Smoke-test on the small-sample stub from Sections 8–9.

### 4.3 Hour 3:00 — 3:30 — Section 13 and final wiring

- Add Section 13 (DM.5-TEMPLATE fill instructions and cheat-sheet print).
- Verify all `[TBD]` placeholders in DM.5-TEMPLATE have a corresponding run-log key.
- Verify the run log JSON saves correctly at the end of execution.

### 4.4 Hour 3:30 — 4:00 — Top-to-bottom smoke test, debug, commit

- Restart the notebook kernel.
- Run all cells top to bottom on the smoke-test configuration (small sample, Tier-1).
- Verify no cell raises; final run-log JSON is well-formed; verdict cell prints PASS or one of the alternatives.
- Fix any cell-ordering or import issues.
- Update `ed-lab/arcs/arc-DM/run_log.md`: append `2026-MM-DD: Step 8 complete. 05_dm2_sparc_fits.ipynb implemented; smoke-test run succeeds end-to-end; production run deferred to compute session.`
- Commit:

  ```
  git add ed-lab/analysis/notebooks/05_dm2_sparc_fits.ipynb
  git add ed-lab/arcs/arc-DM/run_log.md
  git commit -m "Add 05_dm2_sparc_fits.ipynb — DM Step 8 complete, ready for production run"
  git push
  ```

---

## 5. Session-complete checklist

- [ ] `ed-lab/analysis/notebooks/05_dm2_sparc_fits.ipynb` exists with 13 sections per §1.2.
- [ ] Notebook runs top-to-bottom on a smoke-test configuration without raising any exception.
- [ ] Validation suite passes when invoked from the notebook.
- [ ] NGC 3198 run completes end-to-end with sensible output.
- [ ] Sections 8 and 9 (30-galaxy fit and full-sample run) are stubbed with smoke-test data; production-mode lines are commented with explicit "FOR REAL RUN" markers.
- [ ] All output paths are correctly constructed under `ed-lab/analysis/outputs/dm2_<DATE>_<SHA>/`.
- [ ] All sections log their results to `dm2_run_log.json`.
- [ ] Plots save as PNG to the output directory.
- [ ] Section 13 prints a fill-in cheat sheet that maps run-log keys to DM.5-TEMPLATE placeholders.
- [ ] Reproducibility guarantees per §2 are implemented (OMP_NUM_THREADS, RNG seeds, joblib backend, SHA tagging).
- [ ] No `print` debug statements remain (except intentional logging output).
- [ ] All DM.7–DM.13 module tests still pass.
- [ ] One-line entry added to run log.
- [ ] Commit landed.
- [ ] Push to origin successful.

If any item is unchecked, the session is incomplete. Do not begin the production compute run until the §5 checklist is fully satisfied.

---

## 6. Anti-scope-creep guardrails

The following are **explicitly out of scope** for Session 8:

- **The actual 30-galaxy production fit.** That is a 6-hour compute task; running it during a coding session is wasteful. Section 8 has a smoke-test stub for now.
- **The actual full-sample SPARC run.** Same reasoning. Section 9 stubs to smoke-test.
- **Cross-validation execution.** ~30-hour task; deferred to compute session.
- **Filling DM.5-TEMPLATE with real numbers.** That happens after the production compute run.
- **Optimization of the notebook for performance.** The notebook orchestrates; it does not optimize underlying computation.
- **Adding new analysis sections beyond the 13 specified.** The structure is fixed; expansions are post-DM.5 work.
- **Refactoring DM.7–DM.13 modules.** Any bug found in those modules is fixed in place, not refactored from the notebook.

If during the session a tempting deviation surfaces, record it in a TODO and move on.

---

## 7. Risk inventory for Session 8

Three things most likely to consume more time than expected:

1. **OMP_NUM_THREADS not taking effect.** Setting after import has no effect. Mitigation: explicit verification in Section 2 — print `os.environ["OMP_NUM_THREADS"]` and `numpy.show_config()` to confirm. Expected resolution: 10 minutes.

2. **Import path to DM modules.** The DM modules live in `ed-lab/simulations/edsim/dm/`. Whether they are importable from the notebook depends on the project's package layout. If the notebook can't import, either install `ed-lab` as a package via `pip install -e .` or adjust `sys.path` in Section 3. Expected resolution: 15–30 minutes.

3. **NGC 3198 runtime exceeds 10-minute budget.** If Tier-3 takes longer than expected, the notebook stalls during construction. Mitigation: temporarily reduce to Tier-1 for Section 7's smoke test; document the change with a "FOR REAL RUN" comment. Expected resolution: 15 minutes.

If the session runs over budget, do not skip writing later sections or commit. The completion checklist is the gate.

---

## 8. Cross-checks against earlier memos

The implementation must respect five structural constraints:

1. **Validation gate before any galaxy** (DM.4 §1.2 / DM.13 §1.12): Section 6 calls `run_validation_suite` and halts on failure. No subsequent section runs if validation fails.

2. **Four hard gates in order** (DM.4 §7): Sections 6, 7, 8 enforce Gates 2, 3, 4 explicitly with pass-criteria checks. Section 9 (full sample) runs only after Gate 4 clears.

3. **Reproducibility discipline** (program-wide): every number in DM.5 traces to `dm2_run_log.json`. No manual computation in the verdict memo.

4. **DM.5-TEMPLATE structure** (DM.5-TEMPLATE §0–§7): the run-log keys map one-to-one to the template's `[TBD]` placeholders. Section 13 enforces this explicitly.

5. **SHA tagging for reproducibility** (program-wide): the output directory name and the run log both record `ed-lab` and `event-density` SHAs.

---

## End-of-turn summary

**What got done this turn:** the Session 8 notebook plan is fully scoped. 13 sections cover end-to-end orchestration from environment setup through verdict assignment. Reproducibility guarantees (single-threaded BLAS, fixed RNG seeds, joblib loky backend, SHA tagging, complete logging) are explicit. The two-hour construction plan covers Sections 1–7 (through NGC 3198 smoke test); Sections 8–13 extend into hours 2–4. Anti-scope-creep guardrails forbid running production compute during the coding session.

**What did not get done:** no notebook code has been written. The DM.14 memo is a notebook-construction plan, not the notebook itself.

**What this means for the program:** **after Session 8 lands, all engineering work in the DM arc is complete.** The remaining work is compute: running the notebook in production mode (uncommenting the "FOR REAL RUN" lines), waiting ~12 hours for the global fit + cross-validation + full-sample run to complete, then filling DM.5-TEMPLATE with the resulting numbers.

**Next phase (post-DM.14):** **DM.5 (real)** — the verdict memo, written by filling DM.5-TEMPLATE from `dm2_run_log.json`. This is the first DM-arc memo that contains real numbers. It is also the document that the program has been driving toward for fourteen memos.

---

## Recommended Next Step

After confirming DM.7 through DM.13 are all fully landed (their §5 checklists satisfied), begin DM.14 Session 8: in `ed-lab/analysis/notebooks/`, create `05_dm2_sparc_fits.ipynb` and implement the 13 sections in the order specified in DM.14 §3.2–§3.5 then §4.1–§4.3 (header → environment + RNG/threading setup → imports → SHA logging → config → validation gate → NGC 3198 → 30-galaxy stub → full-sample stub → universality → BTFR → RC #1 + verdict → DM.5 fill instructions), enforcing the reproducibility guarantees in §2 and the anti-scope-creep guardrails in §6 (no production compute during this session). Run the notebook end-to-end on the smoke-test configuration; verify all sections execute without error, the run log JSON is well-formed, and the Section 13 cheat sheet correctly enumerates DM.5-TEMPLATE fill values. Do not begin the production compute run until the §5 session-complete checklist is fully satisfied.