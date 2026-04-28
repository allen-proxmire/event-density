# DM.2 — SPARC Per-Galaxy Confrontation Design

**Date:** 2026-04-25
**Arc:** Dark Matter (DM) — third memo
**Status:** Simulation design complete. This memo specifies the pipeline; it does **not** execute it. Implementation is DM.3 (or its variants).
**Predecessor:** DM.1 (structural pass on shape/magnitude under activity sourcing).
**Successor:** see *Recommended Next Step*.
**Target codebase:** `ed-lab/simulations/edsim/dm/` and `ed-lab/analysis/scripts/dm2_sparc/` and notebook `ed-lab/analysis/notebooks/05_dm2_sparc_fits.ipynb`.

---

## 1. The pipeline

The structural argument is in DM.1. DM.2 turns it into a numerical comparison against SPARC. The pipeline has six stages, each with a well-defined input and output.

### Stage 1 — Load SPARC inputs

For each galaxy in the SPARC sample:

- **Table 1:** structural parameters (R_d, M_b, distance, morphological T-type, quality flag Q).
- **Table 2:** per-radius rotation-curve data — observed v_obs(r), uncertainty σ_v(r), and Newtonian-baryonic decompositions v_gas(r), v_disk(r), v_bulge(r).

Construct the Newtonian baryonic curve:

> v²_bar(r) = v²_gas(r) + v²_disk(r) + v²_bulge(r).

Apply the standard quality cut Q ≤ 2 to drop the most uncertain ~15% of the sample. Final working sample: ~150 galaxies.

### Stage 2 — Construct the activity index A(r)

Compute the activity scalar from the Newtonian baryonic kinematics:

> A(r) = α · |dv_bar/dr|² + β · (v_bar / r)².

The first term is radial shear (the strain-rate-like contribution); the second is differential-rotation vorticity. For axisymmetric thin disks, these are the dominant gradient invariants.

**Bootstrap vs. self-consistency.** This stage uses v_bar — the Newtonian curve — to build A(r). The self-consistent definition would use the full predicted v_pred(r), which depends on T, which depends on A. Three-tier protocol:

- **Tier 1 (first pass):** A from v_bar. Cheapest, no iteration.
- **Tier 2 (one iteration):** A from v_pred(Tier 1).
- **Tier 3 (fixed point):** iterate A → T → v_pred → A until ‖v_pred,n+1 − v_pred,n‖ < 1 km s⁻¹ across the sample.

DM.2 commits to Tier 3 as the structurally correct definition. Tier 1 is run first as a sanity check; if Tier 3 fails to converge (rare for diffusive PDEs but possible), we fall back to Tier 2 and document the gap.

### Stage 3 — Source term

> S_activity(R, z) = κ_act · A(R) · ρ_geom(R, z),

where ρ_geom is a geometric factor encoding where the activity lives in the disk:

> ρ_geom(R, z) = (1 / 2 h_disk) · sech²(z / h_disk),

with h_disk a fixed disk thickness scale. For SPARC dwarfs and spirals, h_disk ≈ 0.3 kpc is a reasonable default; the result is insensitive to this choice for r ≫ h_disk.

### Stage 4 — Solve the equilibrium PDE

The PDE in axisymmetric cylindrical coordinates:

> (1/R) ∂/∂R (R ∂T/∂R) + ∂²T/∂z² − T/L² = − S_activity(R, z) / D_T,

with L = √(D_T/λ) ≈ 1 Mpc. Boundary conditions:

- **R = 0:** ∂T/∂R = 0 (regularity on axis).
- **R → ∞:** T → 0 (Yukawa decay; in practice imposed at R = R_max with R_max ≥ 5L = 5 Mpc).
- **z = ±z_max:** T → 0 (z_max = 5 h_disk ≈ 1.5 kpc).
- **z = 0:** ∂T/∂z = 0 (mid-plane symmetry; permits half-space computation).

Stage 4 outputs T(R, z) on the grid.

### Stage 5 — Map T to the gravitational potential (Reading B)

Per DM.1, Reading B identifies T as a contribution to the gravitational potential:

> Φ_T(R, z) = γ · T(R, z),
> Φ_total(R, z) = Φ_bar(R, z) + Φ_T(R, z),

with γ fixed by the self-consistency relation γ · κ_act = D_T (DM.1 §4.2).

### Stage 6 — Predicted rotation curve and residuals

Evaluate at z = 0:

> v²_pred(R) = R · ∂Φ_total / ∂R |_{z=0}.

Compute residuals against observation:

> Δv(R_i) = v_pred(R_i) − v_obs(R_i),
> χ²_galaxy = Σ_i (Δv(R_i) / σ_v(R_i))²,
> χ²_red = χ²_galaxy / N_points.

Aggregate across the sample for global statistics (next section).

---

## 2. Free and inherited parameters

| Parameter | Status | Value | Source |
|---|---|---|---|
| D_T | Inherited | 2.1 × 10²⁷ m² s⁻¹ | Cluster-merger paper (Mistele weak-lensing extent) |
| λ | Inherited | 1/t_H ≈ 2.3 × 10⁻¹⁸ s⁻¹ | Cluster-merger paper (Hubble time) |
| L | Derived | √(D_T/λ) ≈ 1 Mpc | From above |
| γ | Tied | D_T / κ_act | DM.1 self-consistency |
| **κ_act** | **Free, universal** | TBD | Fit globally across SPARC |
| **α** | **Free, universal** | TBD | Fit or fix by symmetry |
| **β** | **Free, universal** | TBD | Fit or fix by symmetry |
| h_disk | Nuisance | 0.3 kpc | Sensitivity-tested in §5 |
| ρ_geom form | Nuisance | sech² | Robust to alternatives |

**Effective free parameter count: 2 — κ_act and the ratio α/β.** With α and β separately fittable but only their relative weight mattering structurally, we set α + β = 1 (normalization) and let α ∈ [0, 1] be the single shear-vs-vorticity mixing parameter, with β = 1 − α.

**The hard rule of DM.2: κ_act and α are universal.** They are fit *once*, globally, against the entire SPARC sample. They are not allowed to vary per galaxy. If the sample requires per-galaxy variation to fit, the framework has failed refutation condition #2.

---

## 3. Empirical tests

### 3.1 Per-galaxy fits

For each galaxy g in the working sample:

- Run the pipeline with the global (κ_act, α).
- Output v_pred(r) and Δv(r) on the SPARC grid.
- Record χ²_red,g.

### 3.2 Sample statistics

- Distribution of χ²_red across the sample. A healthy fit gives a unimodal distribution centered near 1, with limited tail.
- Mean residual ⟨Δv(r)⟩ binned by radius — should be consistent with zero across the sample.
- RMS residual ⟨Δv²(r)⟩^(1/2) binned by radius — should be small relative to v_obs.

### 3.3 Stratification

Compute χ²_red conditional on:

- **Mass:** M_b in bins (10⁷–10⁸, 10⁸–10⁹, 10⁹–10¹⁰, 10¹⁰–10¹¹ M☉).
- **Morphology:** T-type (early-type, late-type, irregular).
- **Surface brightness:** SB_disk.
- **Activity index:** ⟨A⟩ over the disk.

Systematic χ²_red dependence on any of these — particularly mass or morphology — is a refutation indicator (RC #1).

### 3.4 BTFR test

For each galaxy:

- Determine v_∞ from the predicted curve. The cleanest definition is the asymptotic value at the outermost SPARC radius, or the median of v_pred over the outer half of the disk.
- Plot log v_∞ vs. log M_b across the sample.
- Fit slope.

Predicted slope under DM.1 conditional argument: 4.0 (BTFR), conditional on R_d ∝ √M_b. Acceptable range: 3.5–4.5. Deviation outside this range triggers RC #3.

### 3.5 Universality test

Re-fit κ_act per galaxy (relaxing the universality constraint). Plot the per-galaxy κ_act distribution.

- A narrow distribution (1σ within ±20% of mean): universality is consistent.
- A broad distribution, or systematic dependence of fitted κ_act on galaxy properties: universality fails (RC #2).

---

## 4. Refutation conditions — quantitative

The activity-sourced PDE is refuted at the level DM.2 can test if any of the following holds:

**RC #1 — Systematic shape failure.**
- Definition: median |⟨Δv(r)⟩| > 20 km s⁻¹ in any radial bin across more than 30% of the sample, OR χ²_red has a clear bimodal/multimodal distribution suggesting multiple unaccounted populations.
- Implication: the activity-source PDE does not capture the rotation-curve shape across SPARC despite passing the asymptotic argument in DM.1.

**RC #2 — Non-universal κ_act.**
- Definition: 1σ spread of per-galaxy fitted κ_act exceeds ±30% of the global mean, OR fitted κ_act shows systematic correlation (Spearman |ρ| > 0.3) with M_b, morphology, or environment.
- Implication: there is no single coupling that fits the sample. The framework's parsimony claim collapses.

**RC #3 — BTFR slope failure.**
- Definition: fitted BTFR slope from the predicted v_∞ falls outside [3.5, 4.5] at > 3σ.
- Implication: the conditional BTFR argument in DM.1 fails. Either the disk-scaling assumption R_d ∝ √M_b does not hold for this sample, or the activity-source mechanism does not deliver BTFR even with that assumption.

A pass on all three is a real DM result. A fail on any one is a real constraint. Either outcome is decisive.

---

## 5. Computational requirements

### 5.1 Grid

Two-dimensional axisymmetric grid in (R, z):

- R range: 0 to R_max = 5 Mpc (5L). Logarithmic spacing inside 50 kpc, linear outside.
- R resolution: 0.1 kpc near the disk center, 100 kpc at the screening edge. Total ~ 500 cells.
- z range: −z_max to +z_max with z_max = 1.5 kpc. By mid-plane symmetry, compute on [0, z_max]. ~ 50 cells.
- Total: ~ 25,000 cells per galaxy.

### 5.2 Numerical method

The screened-Poisson (Helmholtz) operator on an axisymmetric grid is well-conditioned for several methods:

- **Finite-difference relaxation (Gauss-Seidel with SOR).** Simplest, robust, ~10³–10⁴ iterations to converge. Per galaxy: ~10–60 seconds on a single CPU core.
- **FFT-based Hankel transform in R + finite-difference in z.** Faster (~10× speedup), but requires more careful implementation of the screening term.
- **Multigrid V-cycle on the Helmholtz operator.** Fastest (~100× speedup), implementation overhead is moderate.

**Default choice for DM.3 implementation: finite-difference SOR.** Robust, well-understood, easy to validate against analytic limits. Migrate to multigrid if total runtime becomes a bottleneck.

### 5.3 Validation

Before running the SPARC sample, validate the solver on three analytic test cases:

- **Point source.** S = δ³(x). Check that T → exp(−r/L) / (4π D_T r). Pass if relative error < 1% at r = 100 kpc.
- **Uniform infinite source.** S = const. Check that T → S/(λ) everywhere (zero-curvature solution). Pass if T uniform to 0.1%.
- **Isothermal source profile S(r) = S₀ / r².** Check that T(r) → −(S₀/D_T) ln(r) + const in the unscreened limit r ≪ L. This is the DM.1 self-consistent solution; the predicted v_T should be exactly flat.

The third test is critical: it confirms that the solver reproduces DM.1's analytic flat-curve emergence numerically, so any failure in the SPARC fits is a *physics* failure (the activity profile), not a *solver* failure.

### 5.4 Runtime budget

Per-galaxy: ~30 seconds for Tier 1 (no iteration), ~3 minutes for Tier 3 (with iteration).
Sample (150 galaxies): ~1 hour for Tier 1, ~7 hours for Tier 3.
Sensitivity studies (varying κ_act, α): 5–10 multiplicative factor.

**Total compute envelope: O(50 hours) on a single CPU**, fully tractable on a laptop. No HPC required.

### 5.5 Repository placement

The simulation belongs in **`ed-lab/simulations/edsim/dm/`** as a new submodule:

- `dm/screened_poisson_solver.py` — the core 2D Helmholtz solver
- `dm/activity_index.py` — the A(r) constructor
- `dm/sparc_pipeline.py` — Stages 1–6 wired together
- `dm/validation.py` — the three analytic test cases

The analysis layer lives in **`ed-lab/analysis/scripts/dm2_sparc/`**:

- `dm2_run_sample.py` — runs the pipeline across SPARC, outputs per-galaxy fits and aggregate statistics
- `dm2_global_fit.py` — global fit of (κ_act, α) against the sample
- `dm2_btfr.py` — BTFR slope test
- `dm2_universality.py` — per-galaxy κ_act distribution

The reproducibility notebook is **`ed-lab/analysis/notebooks/05_dm2_sparc_fits.ipynb`**.

---

## 6. Engineering considerations

### 6.1 Two pre-existing notebooks set the precedent

`03_galaxy15_lag.ipynb` (cluster merger-lag) and `04_udm_mobility.ipynb` (universal mobility) are short, runnable, and fast. The DM.2 notebook should match that pattern: load data, run pipeline, print verdict, plot results, fit in under 5 minutes of Colab runtime for a representative subset (e.g., 10 galaxies). Full-sample runs go into the scripts.

### 6.2 SPARC data access

SPARC tables are public. The processed CSV format used in `04_udm_mobility.ipynb` will likely be reusable. If not, a one-time ingestion step from the SPARC text files is straightforward (~50 lines of Python).

### 6.3 Baryonic potential Φ_bar

SPARC provides v_gas, v_disk, v_bulge per radius; the corresponding potentials are obtained by integration. Standard. The disk potential for an exponential profile is analytically known (modified Bessel functions) — use the analytic form rather than numerical integration to avoid noise.

### 6.4 Failure-mode triage

If RC #1 fires (systematic shape failure):
- Inspect residuals at the per-galaxy level to identify which radii fail.
- Check whether failures correlate with disk thickness, bulge presence, or bar features (which the axisymmetric model doesn't capture).
- This informs whether the failure is fundamental or a model-detail issue.

If RC #2 fires (non-universal κ_act):
- Examine whether κ_act correlates with a single galaxy property (morphology, environment, sSFR).
- A clean correlation would indicate a missing structural ingredient (a second activity channel, environmental coupling) rather than a refutation.
- A scattered, uncorrelated κ_act would be a hard refutation of the universality claim.

If RC #3 fires (BTFR failure):
- Test whether the disk relation R_d ∝ √M_b holds for the SPARC subsample.
- If it does, BTFR is genuinely missing — refutation.
- If it doesn't (selection effect), the BTFR test was invalid and rerun against a sample that does obey the disk relation.

---

## 7. What DM.2 will and will not do

### 7.1 Will
- Test whether the activity-source PDE reproduces SPARC rotation curves with universal (κ_act, α).
- Provide quantitative residuals per galaxy.
- Provide global statistics (χ² distribution, BTFR slope, κ_act universality).
- Apply the three quantitative refutation conditions.

### 7.2 Will not
- Test the framework against galaxy clusters (already done by the merger-lag paper).
- Test the framework against weak-lensing data (Mistele-derived D_T is the input, not the output).
- Distinguish Reading B from Reading C (both produce the same v_pred for thin disks).
- Derive κ_act from primitives. That remains a structural open question after DM.2 regardless of outcome.
- Address non-axisymmetric features (bars, warps, lopsidedness). These are second-order corrections in the axisymmetric design.

---

## 8. Verdict structure for DM.2

DM.2 will produce one of four verdicts on completion:

- **PASS:** all three RCs cleared. Per-galaxy fits succeed, κ_act is universal within ±30%, BTFR slope matches. Activity-source PDE confirmed at galactic scales.
- **PARTIAL — universality failure:** RCs 1 and 3 cleared, RC 2 fails. The fits work but κ_act varies systematically. Indicates missing structure (DM.3 explores).
- **PARTIAL — BTFR failure:** RCs 1 and 2 cleared, RC 3 fails. The fits work and κ_act is universal, but the predicted BTFR slope is off. Indicates the disk-scaling assumption is the load-bearing piece. (DM.3 examines.)
- **FAIL:** RC 1 fails. The PDE does not reproduce rotation-curve shapes regardless of parameter choice. The activity-source mechanism is structurally insufficient. (DM.3 returns to alternative channels.)

---

## 9. Refutation resilience — what survives a FAIL

If DM.2 returns FAIL, the framework loses the equilibrium-galactic-rotation-curve claim. What survives:

- Cluster merger-lag (non-equilibrium, different test).
- ED-04.5 dwarf activity-dependence (signature, not mechanism).
- All forced theorems (independent of the DM arc).
- The universal mobility law (different physics).

What does not survive:
- The implicit ED-04 claim that activity-driven temporal-tension halos reproduce galactic rotation curves at the equilibrium-PDE level.
- The DM.1 partial pass.

A FAIL is therefore an honest constraint, not a destruction. It tells us where the framework's reach actually ends.

---

## Recommended Next Step

**DM.3 — implementation of the solver and execution against SPARC.**

The design is now committed. The next step is engineering: build the four-file solver in `ed-lab/simulations/edsim/dm/`, validate against the three analytic test cases, run the global fit pipeline against SPARC, and apply the three refutation conditions. This is bounded computational work — O(50 hours of compute, several days of implementation effort).

The alternative branches the user named are not appropriate at this stage:

- **Reduced-order analytic approximation:** would not provide quantitative per-galaxy residuals against real data. Adds nothing beyond DM.1's structural argument.
- **Parameter-sensitivity study:** is a part of DM.3 (sensitivity to h_disk, ρ_geom form, Tier 1 vs. Tier 3) but does not stand alone — it makes sense only after the global fit exists.
- **Return to V₁ + acoustic-metric channel:** is the right move *if and only if* DM.3 returns FAIL. Pursuing it speculatively before the empirical test is premature, because DM.1's structural argument is too clean to abandon without confrontation.

DM.3 is the smallest executable next step that delivers a verdict. It is also the step that most cheaply tells us where the framework actually stands — pass, partial, or fail — at galactic scales.

If DM.3 returns FAIL, **DM.4 should be the V₁ + acoustic-metric channel exploration.** If DM.3 returns PARTIAL (either kind), DM.4 should target the specific structural gap exposed by the partial.

---

## End-of-turn summary

**What got done:** the simulation pipeline is fully specified — six-stage data flow, two-parameter universal fit, three quantitative refutation conditions, validation protocol, repository placement, and runtime budget. The pipeline is engineerable from this memo without further design decisions.

**What did not get done:** the implementation itself. No code has been written.

**What this means for the program:** the DM arc has gone from "structurally plausible" (DM.1) to "ready to confront real data" (DM.2). The next move is execution.

**Computational ask:** O(50 hours) on a single CPU, runnable on a laptop. No HPC, no specialized hardware.

**Code ask:** ~500–1000 lines of Python across four solver files and four analysis scripts, plus one notebook for reproducibility. Standard scientific stack (numpy, scipy, matplotlib, pandas) — no novel dependencies.

**Verdict architecture:** DM.3 returns one of four verdicts (PASS, PARTIAL-universality, PARTIAL-BTFR, FAIL). DM.4's direction is determined by which.
