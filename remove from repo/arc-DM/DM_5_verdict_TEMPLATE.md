# DM.5 — Verdict Memo (TEMPLATE)

**THIS IS A TEMPLATE. ALL [TBD] FIELDS REQUIRE REAL DATA FROM A COMPLETED RUN. NO NUMERIC VALUE OR VERDICT IN THIS DOCUMENT IS VALID UNTIL THE DM.4 EXECUTION PROTOCOL HAS BEEN RUN AGAINST THE SPARC SAMPLE.**

---

**Date of run:** [TBD: YYYY-MM-DD]
**Date of memo:** [TBD: YYYY-MM-DD]
**Arc:** Dark Matter (DM) — sixth memo
**Status:** [TBD: COMPLETE / FAILED-AT-GATE-N / IN-PROGRESS]
**Predecessor:** DM.4 (execution protocol committed).
**Successor:** [TBD: DM.6 — to be determined by verdict, see §7]
**Codebase:** `ed-lab/simulations/edsim/dm/` and `ed-lab/analysis/scripts/dm2_sparc/`
**Commit at run time:** [TBD: short SHA of `ed-lab` and `event-density` HEAD at execution]
**Operator:** [TBD: name of analyst who ran the protocol]

---

## 0. Refutation conditions and verdict architecture (recap)

The verdict in §6 below is determined by which, if any, of the three pre-registered refutation conditions fire. Each is binary and quantitatively defined.

**RC #1 — Systematic shape failure.**
Fires if median |⟨Δv(r)⟩| > 20 km/s in any radial bin within any stratification, across more than 30% of the sample. Or if the χ²_red distribution is multimodal at significance p < 0.01 (Hartigan dip test).

**RC #2 — Non-universal κ_act.**
Fires if σ(log κ_act,g) / mean(log κ_act,g) > 0.13 (i.e., > ±30% spread). Or if Spearman |ρ| > 0.3 against any of {log M_b, T-type, log SB_disk, log sSFR}.

**RC #3 — BTFR slope failure.**
Fires if the fitted BTFR slope from PDE-derived v_∞ is outside [3.5, 4.5] at > 3σ.

**Four-way verdict.**

- **PASS** — none of RC #1, RC #2, RC #3 fire. The activity-source PDE reproduces SPARC rotation curves with universal parameters and the right BTFR.
- **PARTIAL-universality** — RC #2 fires alone. Per-galaxy fits succeed but κ_act is not universal.
- **PARTIAL-BTFR** — RC #3 fires alone. Per-galaxy fits succeed and κ_act is universal but BTFR slope is off.
- **FAIL** — RC #1 fires (alone or in combination). Or any combination of RCs that includes RC #1.

If RC #2 and RC #3 fire jointly without RC #1: classify as **FAIL** (insufficient structural support to call the result PARTIAL).

---

## 1. Execution status by gate

The DM.4 protocol defines four sequential gates. Each must be cleared before proceeding.

### 1.1 Gate 1 — Implementation

| Module | Implemented | Unit tests | Pass |
|---|---|---|---|
| `disk_geometry.py` | [TBD: yes/no] | [TBD: N pass / N tests] | [TBD: PASS/FAIL] |
| `activity_source.py` | [TBD: yes/no] | [TBD: N pass / N tests] | [TBD: PASS/FAIL] |
| `pde_solver.py` | [TBD: yes/no] | [TBD: N pass / N tests] | [TBD: PASS/FAIL] |
| `boundary_conditions.py` | [TBD: yes/no] | [TBD: N pass / N tests] | [TBD: PASS/FAIL] |
| `validation_tests.py` | [TBD: yes/no] | [TBD: N pass / N tests] | [TBD: PASS/FAIL] |
| `run_single_galaxy.py` | [TBD: yes/no] | [TBD: N pass / N tests] | [TBD: PASS/FAIL] |
| `fit_activity_parameters.py` | [TBD: yes/no] | [TBD: N pass / N tests] | [TBD: PASS/FAIL] |
| `run_full_sample.py` | [TBD: yes/no] | [TBD: N pass / N tests] | [TBD: PASS/FAIL] |

**Gate 1 verdict:** [TBD: PASS / FAIL]
**Anomalies:** [TBD: list any unit-test failures and how they were resolved, or note "none"]
**Mitigations applied:** [TBD: e.g., "pole regularization tightened to ΔR = 0.005 kpc to clear pde_solver pole-stability test", or "none"]

### 1.2 Gate 2 — Validation

Three analytic test cases run on the production grid (300 R × 30 z, R_max = 5 Mpc, h_disk = 0.3 kpc).

#### Test 1 — Point source → Yukawa

- **Tolerance:** max relative error < 5% over r ∈ [10 kpc, 500 kpc].
- **Measured max relative error:** [TBD: %]
- **Result:** [TBD: PASS / FAIL]

#### Test 2 — Uniform source → zero curvature

- **Tolerance:** max |∇T| / (S_0 / λ) < 1% across central 90% of grid.
- **Measured max |∇T|/(S_0/λ):** [TBD: %]
- **Result:** [TBD: PASS / FAIL]

#### Test 3 — Isothermal 1/r² source → flat curve

- **Tolerance:** |dv_T/dR| < 2 km/s/kpc over R ∈ [5 kpc, 30 kpc].
- **Measured max |dv_T/dR|:** [TBD: km/s/kpc]
- **Result:** [TBD: PASS / FAIL]

**Gate 2 verdict:** [TBD: PASS / FAIL — fails if any of Tests 1, 2, 3 fail]
**Anomalies:** [TBD: any unexpected behavior; or "none"]
**Mitigations applied:** [TBD: describe any grid refinement, solver-tolerance tightening, or BC adjustment, or "none"]

> **HARD GATE.** If Gate 2 fails, no SPARC galaxy is run. Halt and diagnose. The protocol does not advance until all three tests pass on the production grid.

### 1.3 Gate 3 — NGC 3198 proof of concept

- **Galaxy properties used:** M_b = [TBD: × 10¹⁰ M☉], R_d = [TBD: kpc], R_outer = [TBD: kpc], v_flat,obs = [TBD: km/s].
- **Tier-3 outer-loop iterations to convergence:** [TBD: N]
- **Inner SOR iterations (mean per outer):** [TBD: N]
- **Wall time:** [TBD: minutes]
- **Damping triggered:** [TBD: yes/no, at iteration N if yes]

**Pass criteria.**

- Shape: |v_pred(R) − v_obs(R)| < 30 km/s for all R ∈ [5 kpc, 25 kpc]. **Result:** [TBD: PASS/FAIL]. Max residual: [TBD: km/s] at R = [TBD: kpc].
- Convergence: outer loop converges in < 50 iterations with no oscillatory divergence. **Result:** [TBD: PASS/FAIL].
- No solver pathology: no NaN, no negative T outside active region, no unphysical features. **Result:** [TBD: PASS/FAIL].

**Gate 3 verdict:** [TBD: PASS / FAIL — all three pass criteria must hold]
**Anomalies:** [TBD: e.g., "v_pred falls below v_obs at innermost point by 8 km/s — within threshold; bulge-treatment correction may be marginally needed", or "none"]
**Diagnostic plot:** [TBD: path to v_pred vs. v_obs plot for NGC 3198]

> **HARD GATE.** If Gate 3 fails, halt and diagnose before scaling. Do not run the 30-galaxy fit.

### 1.4 Gate 4 — 30-galaxy global fit

- **Stratified subsample:** 5 mass bins × 6 galaxies. Bin contents: [TBD: comma-separated galaxy IDs per bin]
- **Optimizer:** Nelder-Mead in (log κ_act, α). Initial guess (log κ_act,0, 0.5).
- **Function evaluations to convergence:** [TBD: N]
- **Wall time:** [TBD: hours]

**Cross-validation (5-fold stratified by log M_b):**
- Mean χ² training: [TBD: value]
- Mean χ² test: [TBD: value]
- R_cv = ⟨χ²_test⟩ / ⟨χ²_train⟩: [TBD: value]
- R_cv ∈ [0.9, 1.5]? [TBD: yes/no]

**Catastrophic per-galaxy failures (χ²_red > 100 or non-convergence):**
- Count: [TBD: N out of 30]
- Galaxies: [TBD: list IDs]
- Acceptable threshold: ≤ 5/30. Met? [TBD: yes/no]

**Gate 4 verdict:** [TBD: PASS / FAIL — passes if R_cv in range AND catastrophic failures ≤ 5/30]
**Anomalies:** [TBD: describe any]

> **HARD GATE.** If Gate 4 fails, the 30-galaxy fit is unstable. Do not run full sample with same conditions. Diagnose what the 30-galaxy fit is telling us.

---

## 2. Global fit report

[Fill in only if Gates 1–4 cleared. Otherwise mark §§2–6 as "NOT REACHED" and proceed to §7 with the gate-failure path.]

### 2.1 Best-fit parameters

- κ_act = [TBD: value ± 1σ, mks units, kg s/m³]
- α = [TBD: value ± 1σ, dimensionless, ∈ [0, 1]]
- γ = D_T / κ_act = [TBD: value, derived, m⁵/(kg·s³)]

### 2.2 Convergence behavior

- Optimizer trajectory: [TBD: brief description of the trajectory in (log κ_act, α) space]
- Convergence type: [TBD: monotone / oscillatory / multimodal]
- Multiple local minima? [TBD: yes/no, with description if yes]

### 2.3 Cross-validation

- 5-fold R_cv: [TBD: value] (already reported in §1.4 Gate 4)
- Per-fold variation: [TBD: range across folds]
- Indication of overfitting: [TBD: none / mild / strong, with rationale]

### 2.4 Sample-wide χ² distribution

- Sample size (post-cuts): [TBD: N galaxies]
- Mean χ²_red: [TBD: value]
- Median χ²_red: [TBD: value]
- σ(χ²_red): [TBD: value]
- 90th percentile χ²_red: [TBD: value]
- Distribution shape: [TBD: unimodal / bimodal / heavy-tailed]
- Hartigan dip test p-value: [TBD: value] (multimodal if p < 0.01)

### 2.5 Catastrophic per-galaxy failures (full sample)

- Count: [TBD: N out of full sample]
- Fraction: [TBD: %]
- Acceptable threshold: ≤ 5%. Met? [TBD: yes/no]
- Identified failure modes: [TBD: list — e.g., bulge-dominated, non-axisymmetric, very low inclination, etc.]

---

## 3. Universality report

### 3.1 Per-galaxy κ_act distribution

After global α held fixed, per-galaxy fit of κ_act for each of the [TBD: N] galaxies in the full sample.

- Mean(log κ_act,g): [TBD: value]
- σ(log κ_act,g): [TBD: value]
- σ/mean ratio: [TBD: value]
- **Universality threshold: σ/mean < 0.13.** Met? [TBD: yes/no]

Histogram available at: [TBD: path to dm2_kappa_act_distribution.png]

### 3.2 Spearman correlations against galaxy properties

| Property | ρ | p-value | |ρ| < 0.3? |
|---|---|---|---|
| log M_b | [TBD: value] | [TBD: value] | [TBD: yes/no] |
| T-type (morphology) | [TBD: value] | [TBD: value] | [TBD: yes/no] |
| log SB_disk | [TBD: value] | [TBD: value] | [TBD: yes/no] |
| log sSFR | [TBD: value] | [TBD: value] | [TBD: yes/no] |

### 3.3 RC #2 verdict

**RC #2 fires if either:**
- σ(log κ_act,g) / mean > 0.13, OR
- Spearman |ρ| > 0.3 against any of {log M_b, T-type, log SB_disk, log sSFR}.

**Did RC #2 fire?** [TBD: yes/no]

**If yes, identify which subcondition fired:** [TBD: spread / mass / morphology / SB / sSFR / multiple]

**Structural interpretation if RC #2 fired:** [TBD: brief — e.g., "κ_act correlates with sSFR at ρ = 0.45, suggesting an additional SFR-coupling channel beyond the shear sourcing", or "n/a — RC #2 cleared"]

---

## 4. BTFR report

### 4.1 v_∞ extraction

- Definition used: median(v_pred(R)) over R ∈ [R_outer/2, R_outer].
- Sample-wide v_∞ range: [TBD: km/s] to [TBD: km/s]
- Distribution: [TBD: brief description]

### 4.2 M_b values

- M_star: from L_3.6 with Υ_3.6 = 0.5.
- M_gas: 1.4 × M_HI.
- Sample-wide M_b range: [TBD: log M☉] to [TBD: log M☉]
- Distance method weighting applied: [TBD: yes/no, with description]

### 4.3 Slope and scatter

Linear regression of log v_∞ vs. log M_b across the analysis sample, errors-in-both-variables (`scipy.odr`).

- **Slope:** [TBD: value ± 1σ]
- **Scatter (RMS in log v_∞ at fixed log M_b):** [TBD: value dex]
- **Intercept (log v_∞ at log M_b = 10):** [TBD: value]

### 4.4 Δ_offset diagnostic

- Predicted log v_∞ at log M_b = 10: [TBD: value]
- Empirical log v_∞ at log M_b = 10 (SPARC): ≈ 2.15
- Δ_offset = [TBD: value]
- |Δ_offset| > 0.1? [TBD: yes/no — warning, not refutation]

### 4.5 RC #3 verdict

**RC #3 fires if slope ∉ [3.5, 4.5] at > 3σ.**

- Slope: [TBD: value]
- Slope error: [TBD: σ]
- Distance from nearest acceptable boundary in σ: [TBD: σ]
- **Did RC #3 fire?** [TBD: yes/no]

### 4.6 Comparison to empirical BTFR

Empirical SPARC/MOND slope ≈ 4.0 ± 0.1. Comparison to this fit: [TBD: agree / weakly tension / strongly tension, with σ deviation].

---

## 5. Residual structure report

### 5.1 Aggregate residuals by radial bin

Radial binning: [TBD: e.g., "5 logarithmic bins from 1 to 30 kpc"]

| Radial bin (kpc) | Median Δv | σ Δv | N galaxies in bin | |Median| > 20 km/s? |
|---|---|---|---|---|
| [TBD: bin 1 range] | [TBD: km/s] | [TBD: km/s] | [TBD: N] | [TBD: yes/no] |
| [TBD: bin 2 range] | [TBD: km/s] | [TBD: km/s] | [TBD: N] | [TBD: yes/no] |
| [TBD: bin 3 range] | [TBD: km/s] | [TBD: km/s] | [TBD: N] | [TBD: yes/no] |
| [TBD: bin 4 range] | [TBD: km/s] | [TBD: km/s] | [TBD: N] | [TBD: yes/no] |
| [TBD: bin 5 range] | [TBD: km/s] | [TBD: km/s] | [TBD: N] | [TBD: yes/no] |

### 5.2 Stratified residuals

Stratification by mass (4 bins), morphology (early/late/irregular), SB_disk (3 bins), activity index ⟨A⟩ (3 bins).

For each stratification, report whether any radial bin has |median Δv| > 20 km/s for > 30% of the galaxies in that stratum.

| Stratification | Failure detected? | Details |
|---|---|---|
| Mass bins | [TBD: yes/no] | [TBD: which bins, which radii] |
| Morphology | [TBD: yes/no] | [TBD: which types] |
| SB_disk | [TBD: yes/no] | [TBD: HSB / LSB asymmetry?] |
| Activity index | [TBD: yes/no] | [TBD: low / mid / high activity systems] |

### 5.3 Systematic patterns identified

[TBD: free-form description of any systematic residual pattern. Examples to consider:
- LSB galaxies systematically over-/under-predicted at large R
- Dwarf systems with wrong shape (rising-instead-of-flat)
- Bulge-dominated galaxies with poor inner-disk fit
- Convergence failures concentrated in one morphology
- BTFR offset correlated with morphology
None of the above? Then write "no systematic patterns identified at the |Δv| > 20 km/s level beyond statistical scatter."]

### 5.4 RC #1 verdict

**RC #1 fires if:**
- median |⟨Δv(r)⟩| > 20 km/s in any radial bin within any stratification, across > 30% of the sample. OR
- χ²_red distribution multimodal at p < 0.01.

**Did RC #1 fire?** [TBD: yes/no]

**If yes, which subcondition:** [TBD: radial-bin failure in stratum X / multimodal χ² / both]

---

## 6. Verdict

### 6.1 RC fire matrix

| RC | Description | Fired? |
|---|---|---|
| RC #1 | Systematic shape failure | [TBD: yes/no] |
| RC #2 | Non-universal κ_act | [TBD: yes/no] |
| RC #3 | BTFR slope failure | [TBD: yes/no] |

### 6.2 Verdict assignment rule

Apply this rule mechanically:

- If RC #1 fires (alone or in combination): **FAIL**.
- Else if RC #2 fires alone: **PARTIAL-universality**.
- Else if RC #3 fires alone: **PARTIAL-BTFR**.
- Else if RC #2 and RC #3 fire jointly (with RC #1 not firing): **FAIL** (insufficient structural support to call PARTIAL).
- Else (no RC fires): **PASS**.

### 6.3 Final verdict

**[TBD: one of: PASS / PARTIAL-universality / PARTIAL-BTFR / FAIL]**

### 6.4 Verdict explanation (3–5 sentences)

[TBD: write 3–5 sentences explaining what the verdict means in concrete terms. Include: which RCs fired and which did not; the most diagnostic single quantitative fact behind the verdict; what this implies for the activity-source PDE as a galactic-scale dark-matter mechanism; and what is preserved (cluster merger-lag, forced theorems, etc.) regardless of the verdict.]

### 6.5 What is preserved regardless of verdict

These are not contingent on DM.5's outcome:

- The cluster-merger lag result (seven well-measured clusters + Finner aggregate, confirmed in the merger-lag paper).
- The activity-dependence signature in ED-04.5 (53% separation between Active and Quiet dwarfs).
- The nine forced theorems in the quantum and gravitational sectors.
- The universal mobility law (10-material confirmation in `Universal_Mobility_Law_Evidence`).

DM.5 tests one specific claim — that the equilibrium activity-sourced PDE reproduces galactic rotation curves at the per-galaxy level with universal parameters. A FAIL or PARTIAL verdict constrains this claim, not the framework as a whole.

### 6.6 What is constrained by this verdict

[TBD: depending on outcome:

- **PASS:** the framework's claim that activity sourcing reproduces galactic rotation curves is empirically supported. The DM mechanism is now established at galactic scales as well as cluster scales.
- **PARTIAL-universality:** activity sourcing reproduces the shape and BTFR but κ_act varies systematically. The framework needs additional structure (a second coupling channel, environmental factor, or morphology dependence). DM.6 targets this.
- **PARTIAL-BTFR:** the activity-source mechanism produces the right shape with universal κ_act but the BTFR slope is off. The conditional disk-scaling argument (DM.1 §5) is the suspect link.
- **FAIL:** the activity-source equilibrium PDE is structurally insufficient for galactic rotation curves. The framework retreats to the cluster-merger result and explores alternative galactic mechanisms in DM.6.]

---

## 7. Recommended next step

Branching is determined by §6 verdict.

### 7.1 If verdict = PASS

**DM.6 — Verification, robustness, and extensions.**

- Run a parameter-sensitivity sweep: how does the verdict change with ±20% perturbations of D_T and λ?
- Test the model against galaxy clusters in equilibrium (not just merger-lag non-equilibrium).
- Apply to galaxies outside SPARC (e.g., LITTLE THINGS dwarfs, MaNGA early-types) to test generalizability.
- Begin DM-arc paper drafting.

### 7.2 If verdict = PARTIAL-universality

**DM.6 — Universality structural analysis.**

- Identify the property κ_act correlates with most strongly (Spearman ρ from §3.2).
- Hypothesize the missing structural coupling: SFR-dependent activity, environmental tension, morphology-dependent κ_act.
- Refine the activity-source model to incorporate the missing piece.
- Re-run the SPARC fit with the refined model.

### 7.3 If verdict = PARTIAL-BTFR

**DM.6 — BTFR structural analysis.**

- Test whether R_d ∝ √M_b holds for the SPARC subsample used.
- If yes: the BTFR derivation gap is in the activity-source mechanism itself, not in disk scaling. Re-examine the conditional argument in DM.1 §5.
- If no: the disk-scaling assumption fails for this sample, and the BTFR test was invalid. Re-run against a sample that does obey the disk relation, or accept that BTFR is sample-dependent.

### 7.4 If verdict = FAIL

**DM.6 — Return to V₁ + acoustic-metric channel.**

- The activity-source equilibrium PDE is structurally insufficient at galactic scales.
- The framework retains the cluster merger-lag result (non-equilibrium, different physics) but loses the implicit ED-04 claim of equilibrium-PDE-based galactic rotation curves.
- DM.6 explores an alternative mechanism: the V₁ vacuum kernel (Theorem N1 / T8) coupled through the acoustic metric (Theorem GR1 / T9) at galactic scales.
- This is a structurally cleaner channel because V₁ is a forced theorem with structurally fixed bounds, but it has not yet been applied to galactic dynamics in the ED program.
- DM.6 would scope the V₁ channel; DM.7 onward would derive and test.

### 7.5 Recommended next step (final)

[TBD: select the appropriate sub-section (7.1, 7.2, 7.3, or 7.4) based on the verdict in §6.3, and copy its content here as the explicit recommendation.]

---

## 8. Run artifacts and reproducibility

### 8.1 Artifacts produced

- Code: [TBD: SHA of `ed-lab` HEAD at run time]
- Solver validation report: [TBD: path to validation_report.json]
- Per-galaxy fit results: [TBD: path to dm2_per_galaxy.csv]
- Residuals: [TBD: path to dm2_residuals.csv]
- Global fit results: [TBD: path to dm2_global_fit_results.json]
- BTFR analysis: [TBD: path to dm2_btfr.json]
- T-fields per galaxy: [TBD: path to dm2_T_fields.h5]
- Run log: [TBD: path to dm2_run_log.json]
- Diagnostic plots: [TBD: path to plots directory]

### 8.2 Reproducibility check

- Notebook `05_dm2_sparc_fits.ipynb` runtime on Colab subset (10 galaxies): [TBD: minutes]
- Notebook reproduces this memo's headline verdict: [TBD: yes/no]
- Independent re-run by [TBD: name] on [TBD: date]: [TBD: result match yes/no]

### 8.3 Outstanding caveats

[TBD: list any caveats that should accompany the verdict — e.g., distance-uncertainty propagation not yet rigorous, Tier-3 fallback to Tier-2 for N galaxies due to convergence failure, etc.]

---

## End-of-memo summary

**What the actual run accomplished:** [TBD: 2-3 sentences summarizing the run]

**What the actual run did not do:** [TBD: 2-3 sentences honestly stating the limitations of this DM.5 — what was not tested, what was deferred, what residual gaps remain]

**What this means for the program:** [TBD: 2-3 sentences locating the verdict in the broader DM arc and the framework]

**Decision point:** [TBD: which DM.6 branch is now active — see §7.5]

---

**Reminder: this is a TEMPLATE. The fields above are explicit placeholders. None of them is filled. A DM.5 memo with these placeholders unfilled is not a verdict; it is an unwritten document. The verdict the program needs is real numbers from a real run.**
