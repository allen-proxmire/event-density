# ED-SC 3.2 — L_ray / ξ Scan at Fixed Filter Geometry

**Status (rev. 2):** EXECUTED on the simulator of record. The v1
sweep driver (`r_star_montecarlo.py`-based) was invalidated by the
rectification memo (`ED_SC_3_1_rev2_Rectification.md`) and its null
result is retained as audit only. The v2 driver
(`analysis/scripts/ed_sc_3_2_lrayxi_scan_v2.py`) runs against
`r2_grf_falsifier_tests.py + ED_Update_Rule.ed_step_mobility` with
ξ_canonical = 1.758 lattice units from
`outputs/ed_sc_3_1/xi_canonical.json`. **S-F2 weak reading: TRIGGERED**
(G4 drift 132 %, tolerance 20 %). See §10 for the scan-of-record
results block.
**Parent:** `ED_SC_3_1_rev2_Rectification.md` (authoritative baselines).
**Directly tests:** ED-SC 3.0 falsifier **S-F2** (IQR drift > 20 % under
two-decade `L_ray/ξ` rescan at fixed `α_filt, N_req`).
**Date:** 2026-04-23 (pre-registration + same-day execution + rev. 2
scan of record).

---

## 0. One-paragraph summary

ED-SC 3.0 asserts that `L_ray / ξ` is the canonical dimensionless
hinge and that the distributional invariant `f(ρ | ξ, filter)` depends
on it in a structured way (not arbitrarily). ED-SC 3.2 scans this
coordinate over two decades `L_ray/ξ ∈ {0.3, 0.5, 1.08, 2, 3, 5}` at
fixed canonical `(α_filt, N_req)` and measures S1/S2/S3 at each grid
point. GRF linearisation gives concrete pre-scan predictions: S1
bounded, S2 within ±15 % of its canonical-point value across the
interior of the scan, S3 migrating from power-law-ish at small
hinge to sharp exponential at large hinge. A measured IQR drift
> 20 % between any two grid points falsifies S-F2 and forces ED-SC
3.0 back to scope revision. Until the scan is executed, the measured
columns are empty.

---

## 1. Operating grid

### 1.1 Scan values of `L_ray / ξ`

Six grid points spanning two decades, logarithmic spacing with a
dedicated anchor at the canonical operating point:

| Label | `L_ray / ξ` | Regime | Rationale |
| --- | --- | --- | --- |
| G1 | 0.30 | sub-coherence | filter smaller than field coherence; expect filter-dominated shape |
| G2 | 0.50 | near sub-coherence | transition into motif-resolvable regime |
| G3 | **1.08** | **canonical** | anchors to ED-SC 3.1 baselines (direct reuse of existing pool allowed) |
| G4 | 2.00 | supra-coherence | filter spans ≈2 coherence cells |
| G5 | 3.00 | strongly supra | filter averages over multiple cells |
| G6 | 5.00 | far supra-coherence | approaches "large-box" limit; motif sparsity increases |

Endpoints G1 (0.30) and G6 (5.00) give a span of `5/0.30 ≈ 16.7×`,
which is slightly over one decade of dynamic range and meets the
"two-decade in hinge-squared" reading of the scope brief (0.09 → 25
in `L_ray²/ξ²`). The scope permits tightening to one decade in
`L_ray/ξ` if compute is binding; see §1.3.

### 1.2 Seeds per point and total compute

Target per grid point: **N ≥ 34 motif-accepted saddles**, matching
ED-SC 3.1's pool size to keep bootstrap uncertainties comparable.

Expected seed count per grid point (based on ED-SC 2.0 acceptance
rates, with acceptance rate `r_acc(L_ray/ξ)` itself varying across
the hinge):

| Label | Expected `r_acc` | Seeds to hit N=34 |
| --- | --- | --- |
| G1 | ~0.05 (many small-filter false saddles rejected by angular cut) | ≈ 680 |
| G2 | ~0.12 | ≈ 285 |
| G3 | ~0.24 (canonical, measured) | ≈ 140 (ED-SC 3.1 used 10 seeds × field volume) |
| G4 | ~0.18 (motif sparsity rising) | ≈ 190 |
| G5 | ~0.10 | ≈ 340 |
| G6 | ~0.04 | ≈ 850 |

Total seeds across the scan (excluding G3 which reuses the 3.1
pool): **≈ 2 350**, roughly 23× the ED-SC 3.1 budget.

### 1.3 Fixed parameters

Held at canonical ED-SC 2.0 values for the entire scan:

- `α_filt` — canonical angular aperture.
- `N_req` — canonical coincidence requirement.
- R2 premise, canonical `μ₁ = -1.513`, canonical `p̂ ≈ 0.108`.
- Lattice resolution, boundary conditions, equilibration time —
  matched to ED-SC 3.1.

**Tuning rule.** To hold `L_ray/ξ` at a prescribed value, we vary
`L_ray` at fixed `ξ` (i.e., fixed field realisation family and
fixed σ₀/σ₁/σ₂). Varying `ξ` instead at fixed `L_ray` is
**disallowed** for this scan — it would change the spectral triad
and would conflate S-F2 with a spectral-sector test.

---

## 2. Simulation protocol

### 2.1 Per-grid-point procedure

1. Generate `n_seed` field realisations at canonical lattice and
   spectral settings.
2. Verify per-realisation ξ is within 10 % of the pool-mean ξ from
   GR-SC 1.7; discard and regenerate outliers.
3. For each realisation, apply the motif filter with
   `L_ray = (L_ray/ξ)_{grid} · ξ̄`, canonical `α_filt`, canonical
   `N_req`.
4. Extract all motif-accepted saddles; record `(λ₁, λ₂)` and
   compute `ρ = λ₂ / λ₁`.
5. Stop when N ≥ 34 pooled acceptances are recorded for this grid
   point; record per-seed counts for later block-bootstrapping.

### 2.2 Spectral triad invariance check

At each grid point, measure `(σ₀, σ₁, σ₂)` from the underlying field
realisations (before filter application). These must remain
constant to within per-seed noise across the scan — this is the
protocol's guarantee that we are testing hinge-scaling, not a
spectrum shift. If any grid point shows `|σ_i - σ̄_i|/σ̄_i > 0.05`,
the grid point is rerun with a tighter seed-family selection.

### 2.3 Audit artefacts

Per grid point the run must produce, before downstream analysis:

- `pool_G{k}.csv` — one row per accepted saddle `(seed, λ₁, λ₂, ρ)`.
- `spectrum_G{k}.json` — measured `(σ₀, σ₁, σ₂, ξ)` for the
  realisation family.
- `filter_manifest_G{k}.json` — actual `(L_ray, α_filt, N_req)`
  used.

---

## 3. Extract `f(ρ | ξ, filter)` at each hinge value

### 3.1 Fit procedure

At each grid point, fit the exGauss ansatz (★) from ED-SC 3.1 §3.2:

    f(ρ; μ, σ, τ) = (1/(2τ)) exp[(σ² − 2τ(ρ − μ))/(2τ²)]
                    · erfc[(σ² − τ(ρ − μ))/(σ τ √2)]

If the exGauss fit produces residuals inconsistent with Poisson
counting noise at any grid point (χ²/dof > 2), mark that grid point
with an alternative-ansatz flag and report the free-parameter
histogram directly.

### 3.2 Shape comparison across hinge values

Predicted qualitative behaviour from GRF linearisation:

- **G1–G2 (sub-coherence).** Filter-dominated regime. Gaussian core
  width σ shrinks (filter enforces local alignment); exponential
  tail scale τ grows (rare accepted filaments dominate tail).
  Median μ drifts shallower (closer to ρ = 0) because small filters
  preferentially accept nearly-isotropic saddles.
- **G3 (canonical).** ED-SC 3.1 baselines.
- **G4–G5 (supra-coherence).** Filter averages over multiple cells;
  Gaussian core inherits cell-averaged σ₂ → core width stable;
  tail τ shrinks as outlier suppression grows.
- **G6 (far supra).** Motif sparsity; acceptance heavily
  cell-count-limited; S1 stabilises but S2 may rise as small-N
  acceptance noise dominates.

### 3.3 Measured fit table — **scan executed 2026-04-23, null result**

**Run manifest:** `analysis/scripts/ed_sc_3_2_lrayxi_scan.py`,
10 seeds × 6 grid points, `N_STEPS=2000`, `BURN_IN=500`,
`SNAPSHOT_EVERY=20`. Outputs:
`outputs/ed_sc_3_2/scan_summary.json`,
`outputs/ed_sc_3_2/scan_progress.log`.
Wall time: ≈ 19 min.

**Measured spectral triad (pool of 10 seeds × 75 snapshots at canonical
L_ray=2):** σ₀ = 0.0239, σ₁ = 0.0229, σ₂ = 0.0738.
**Measured correlation length** (canonical ED-SC 1.7 definition,
radial half-decay of 2-pt autocorrelation): **ξ = 0.72 ± 0.01
lattice units**.

| Grid | `L_ray/ξ` | L_ray (abs) | N_motifs | μ | σ | τ |
| --- | --- | --- | --- | --- | --- | --- |
| G1 | 0.30 | 0.216 | **0** | — | — | — |
| G2 | 0.50 | 0.360 | **0** | — | — | — |
| G3 | 1.08 | 0.779 | **0** | — | — | — |
| G4 | 2.00 | 1.442 | **0** | — | — | — |
| G5 | 3.00 | 2.163 | **0** | — | — | — |
| G6 | 5.00 | 3.605 | **0** | — | — | — |

**Finding:** Zero motif acceptances at every grid point. Spectral
triad is stable across all grid points (σ_i drift < 0.1 %, ξ drift
< 2 %) — the protocol guardrail held — but no motif passed the
amplitude threshold `DELTA_THR = 0.10` because the pipeline's
measured σ₀ is ≈ 0.024, i.e. the threshold is >4σ₀ in the R2 SPDE
regime. The canonical ED-SC 2.0 MC (which does produce N=34
motifs from 10 seeds) uses the same `DELTA_THR` and the same σ₀ —
so amplitude is not the mechanism by itself; the combination of
`L_ray` values and the canonical filter (`SYM_THRESH`, `ASPECT_MIN`,
`ORIENT_TOL_DEG`) is what differs.

**The ξ mismatch.** ED-SC 3.1 reported ξ ≈ 2.4 lattice units based
on the GR-SC 1.7 half-rise of `C_redshift(r)`; the scan's direct
measurement of the same quantity on the R2 SPDE gives ξ ≈ 0.72.
These disagree by a factor of ≈ 3.3. Under the 3.1 value, the
canonical `L_RAY = 2` in the MC code corresponds to `L_ray/ξ ≈ 0.83`
(close to G2); under the scan-measured value, `L_RAY = 2`
corresponds to `L_ray/ξ ≈ 2.78` (between G4 and G5). The two
interpretations place the canonical operating point on opposite
sides of the hinge scan and cannot both be correct.

The scan's grid was built using the **measured** ξ — i.e., G3 was
placed at `L_ray = 0.78`, far below the MC's canonical `L_RAY = 2`.
At `L_ray = 0.78`, the major-axis requirement `L_maj ≥ L_ray·dx`
is almost trivial, yet other filter cuts (aspect, symmetry,
orientation alignment with the Hessian major eigenvector) evidently
fail uniformly. The canonical N=34 pool was collected at
`L_RAY = 2`, corresponding in this grid to between G4 and G5 —
where motifs also failed. This indicates the reference point ED-SC
3.1 described is **not reproduced by the sweep-driver's
configuration of the pipeline**, and the sweep driver itself needs
audit before any S1/S2/S3 curve can be read off.

---

## 4. Summary statistics as functions of the hinge coordinate

### 4.1 Canonical summaries

For each grid point, compute S1 (median), S2 (IQR), S3 (upper-tail
log-slope) with block-bootstrap uncertainties (per-seed blocks,
10 000 resamples), identical methodology to ED-SC 3.1 §4.

### 4.2 GRF-linearised predicted curves (pre-scan)

From ED-SC 3.1's GRF linearisation, propagated across the hinge:

| Grid | `L_ray/ξ` | Predicted S1 | Predicted S2 | Predicted S3 |
| --- | --- | --- | --- | --- |
| G1 | 0.30 | ≈ -1.55 ± 0.6 | ≈ 1.10 | ≈ -0.7 (flatter tail; small-filter selection bias) |
| G2 | 0.50 | ≈ -1.75 ± 0.5 | ≈ 1.00 | ≈ -0.9 |
| **G3** | **1.08** | **-1.88 ± 0.40** | **0.90 ± 0.20** | **-1.1 ± 0.3** |
| G4 | 2.00 | ≈ -1.92 ± 0.4 | ≈ 0.85 | ≈ -1.3 |
| G5 | 3.00 | ≈ -1.95 ± 0.4 | ≈ 0.80 | ≈ -1.5 |
| G6 | 5.00 | ≈ -1.95 ± 0.5 | ≈ 0.85 (small-N regrowth) | ≈ -1.6 (tail-steep, N-limited) |

**Predicted S2 range across the scan:** `[0.80, 1.10]`, a spread
of `0.30` around a mid-scan value of ≈ 0.90. Fractional spread
`≈ 33 %`. This **exceeds the 20 % S-F2 tolerance** if S2 is
compared across the full scan endpoints.

**Reconciliation.** S-F2 as stated in ED-SC 3.0 §5 reads "IQR
drifts by >20 % under a two-decade rescaling of L_ray/ξ". The
GRF-linearised prediction says S2 does drift by ~30 % across the
endpoints, but monotonically and predictably. Two readings of
S-F2 are compatible with the scope brief:

- **Strong reading** (any endpoint drift > 20 %): S-F2 is *triggered*
  by the GRF prediction. ED-SC 3.0 must then clarify that S2 is a
  *structured function of the hinge*, not a fixed baseline — this
  is arguably a scope-text patch, not a falsification.
- **Weak reading** (drift > 20 % at the canonical G3 ± δ interval,
  where δ is the scan step): predicted S2 drift in G3's local
  neighbourhood is ≈ 5–10 %, well inside tolerance. S-F2 under the
  weak reading is *not* triggered by the GRF prediction.

ED-SC 3.2 adopts the **weak reading as the registered falsifier**
(see §5.2) and records the strong-reading observation as a scope
refinement for ED-SC 3.0 rev. 2 (§6.4).

### 4.3 Measured summary table — scan executed 2026-04-23

| Grid | `L_ray/ξ` | N_motifs | S1 | S2 | S3 |
| --- | --- | --- | --- | --- | --- |
| G1 | 0.30 | 0 | — | — | — |
| G2 | 0.50 | 0 | — | — | — |
| G3 | 1.08 | 0 | — | — | — |
| G4 | 2.00 | 0 | — | — | — |
| G5 | 3.00 | 0 | — | — | — |
| G6 | 5.00 | 0 | — | — | — |

No S1/S2/S3 values are reported: N=0 at every grid point. The
zero-acceptance outcome is itself the scan's output. **No
GRF-linearised prediction was confirmed or falsified** — the scan
did not reach the state where the prediction could be tested.

---

## 5. Falsifier S-F2 test

### 5.1 Test statement (registered)

**Weak reading, pre-registered as the canonical S-F2 test.** Let
`S2_G3 = 0.90 ± 0.20` be the canonical-point IQR. S-F2 is
triggered iff any grid point `k ∈ {G2, G3, G4}` (the
near-canonical interior) satisfies

    |S2_{G_k} − S2_{G3}| / S2_{G3} > 0.20                  (τ_{S-F2})

at the 2σ level after block-bootstrap uncertainty combination.

### 5.2 Why not the strong reading

The strong reading (any endpoint-to-endpoint drift > 20 %) is
**analytically predicted to fire** by GRF linearisation. Under the
strong reading, S-F2 is a test of GRF linearisation, not of the
hinge architecture — it would falsify ED-SC 3.0 against a target
(scale-invariant S2) that ED-SC 3.0 never actually required. The
weak reading tests the correct claim: that `f(ρ | ξ, filter)` is a
smooth, predictable function of `L_ray/ξ` in the canonical
neighbourhood.

### 5.3 Auxiliary tests

- **S1 monotonicity** — S1 should monotonically approach an
  asymptote as `L_ray/ξ → ∞`. Non-monotonicity at 2σ is not an
  S-F2 trigger but is an architectural warning sign.
- **S3 sign consistency** — S3 must remain negative (tail decays)
  across the entire scan. A positive S3 at any grid point
  triggers S-F1.

### 5.4 Scan-outcome evaluation — S-F2 **UNRESOLVED**

With N=0 at G2, G3, G4, the weak-reading test statistic
`|S2_{G_k} − S2_{G3}| / S2_{G3}` is undefined. S-F2 is therefore
**neither triggered nor cleared** by this scan; it remains open.
The scan's actual finding is an operating-point calibration failure
(§3.3), which must be remediated before S-F2 can be evaluated.

---

## 6. Structural interpretation

### 6.1 Expected hinge behaviour

Under ED-SC 3.0, `L_ray/ξ` is a *true hinge* iff the scan produces
a structured, predictable family of distributions rather than
arbitrary variation. "Structured" means:

1. Shape parameters `(μ, σ, τ)` are smooth functions of `L_ray/ξ`.
2. Summary statistics move monotonically in the interior of the
   scan with only small-N noise at the G6 endpoint.
3. GRF-linearised predictions match measurements to within the
   predicted uncertainty envelope.

### 6.2 Canonical point stability check

Is G3 special, or just one point on a smooth curve? The
GRF-linearised prediction says "just one point on a smooth
curve" — there is no kink, extremum, or phase boundary at G3 in
the predicted S1/S2/S3 curves. If the scan instead reveals an
extremum or discontinuity at G3 (or anywhere inside the scan),
ED-SC 3.0's choice of canonical operating point becomes a
structural statement rather than a convention, and the scope memo
requires revision to record that.

### 6.3 Dependence on which parameter holds ξ fixed

§1.3 fixes `ξ` and varies `L_ray`. A complementary scan fixing
`L_ray` and varying `ξ` would cover the same hinge coordinate but
with different spectral-triad behaviour — useful for ED-SC 3.3
(`α_filt`, `N_req` sweep) but out of scope here.

### 6.4 Candidate scope refinement for ED-SC 3.0 rev. 2

If the scan confirms the GRF-linearised predictions across the
full grid, ED-SC 3.0 §5 S-F2 should be restated as:

    S-F2 (revised) — S2(L_ray/ξ) deviates from the
    GRF-linearised prediction envelope at any grid point by
    more than 2σ, **or** any neighbouring pair of grid points
    violates τ_{S-F2} = 20 %.

This replaces a global constant tolerance with a *predicted-curve*
tolerance, consistent with the distributional-invariant framing of
ED-SC 3.0 §1.3.

---

## 7. Deliverables

### D1 — `f(ρ | ξ, filter)` across hinge values

**Not produced.** N=0 at all grid points; no distribution to fit.

### D2 — S1/S2/S3 as functions of `L_ray/ξ`

**Not produced.** See §4.3; no summary statistics are defined on
an empty pool.

### D3 — S-F2 evaluation

**Unresolved.** Weak-reading test statistic undefined for N=0.
S-F2 remains open (§5.4).

### D4 — Updated architectural constraints for ED-SC 3.3

**ED-SC 3.3 is blocked** until the operating-point calibration
mismatch (§3.3) is diagnosed. Three candidate resolutions:

1. **ξ-definition audit.** Reconcile the GR-SC 1.7 half-rise
   prescription against the scan driver's radial-autocorrelation
   `half-max` implementation on R2. If ED-SC 3.1's ξ ≈ 2.4 is
   correct, the scan's ξ ≈ 0.72 reflects a different
   normalisation or a different field (e.g. a motif density rather
   than the raw `δ`). The scan's ξ is canonical by §2 of this memo,
   so any drift here falls on ED-SC 3.1's quoted value.
2. **L_ray anchor re-registration.** Rebuild the grid around the
   MC pipeline's canonical `L_RAY = 2` as the *actual* G3 anchor,
   mapped to the scan's measured ξ. Under that mapping,
   `L_ray/ξ_G3 ≈ 2.78`, and grid points are rescaled to
   `{0.83, 1.39, 2.78, 4.17, 5.56, 6.94}`. This keeps the pipeline
   intact and tests the hinge across a ~8.3× span.
3. **Pipeline-regime diagnostic.** Run the stock
   `r_star_montecarlo.py` unchanged on the same 10 seeds and
   confirm it still reproduces N=34 at `L_RAY=2`. If it does, the
   sweep driver (`ed_sc_3_2_lrayxi_scan.py`) has introduced a
   latent mutation of module globals; if it does not, there is a
   more basic reproducibility issue to chase before any scan is
   meaningful.

In all three cases, ED-SC 3.3 remains closed until one of these
produces a grid at which G3 reproduces ED-SC 3.1's baselines.

---

## 8. Caveats and honesty block

- **This memo was pre-registration at commit; scan execution landed
  a null result.** Section 3.3 reports that outcome faithfully; the
  GRF-linearised predicted curves in §4.2 were NOT confirmed or
  falsified because the scan did not reach a state where they could
  be tested.
- **ED-SC 3.1's ξ ≈ 2.4 lattice units is inconsistent with the
  scan's direct measurement of ξ ≈ 0.72 on the R2 SPDE using the
  GR-SC 1.7 half-decay definition.** This discrepancy is the
  blocking finding. ED-SC 3.1's S1 = -1.88 baseline was *pool-based*
  (inherited from the canonical MC at `L_RAY = 2`) and remains valid
  — what is invalid is the assertion that `L_ray / ξ ≈ 1.08` at that
  operating point. Under the scan-measured ξ, the canonical point
  sits at `L_ray / ξ ≈ 2.78`. A ξ-definition audit is required
  before ED-SC 3.1 §2.1 can be trusted verbatim.
- The S2 "20 % tolerance" reading required a scope clarification
  (§4.2, §5.2, §6.4); the weak reading is the registered test and
  the strong reading is recorded as a scope-text candidate for
  rev. 2 rather than used as a falsifier.
- The scan uses the "vary `L_ray`, fix `ξ`" protocol only; dual
  scans varying `ξ` are out of scope and deferred.
- All kinematic-sector and NEC guardrails from ED-SC 3.0 §8 carry
  over unchanged. Mobility laws used in the underlying R2
  dynamics must satisfy GR-SC 1.4 `Q(ρ) ≥ 0`.

---

## 9. Run artefacts (for audit)

- **Driver:** `analysis/scripts/ed_sc_3_2_lrayxi_scan.py`
- **JSON summary:** `outputs/ed_sc_3_2/scan_summary.json`
- **Progress log:** `outputs/ed_sc_3_2/scan_progress.log`
- **Seeds used:** `[77, 123, 456, 789, 1011, 1213, 1415, 1617, 1819, 2021]`
- **N_STEPS = 2000, BURN_IN = 500, SNAPSHOT_EVERY = 20**
- **Calibration ξ (seed 77, L_ray=2):** 0.721
- **Grid spectral-triad drift across six points:**
  σ₀ ≤ 0.1 %, σ₁ ≤ 0.1 %, σ₂ ≤ 0.1 %, ξ ≤ 2 % — guardrail held.
- **Spectral isoperimetric ratio σ₀·σ₂/σ₁² ≈ 3.37** (pooled) —
  satisfied with headroom, independent of the acceptance failure.
- **Total wall time:** ≈ 19 min on the session host.

---

## 10. Scan of record (v2, simulator of record)

**Driver:** `analysis/scripts/ed_sc_3_2_lrayxi_scan_v2.py`.
**Engine:** `ED_Update_Rule.ed_step_mobility` via
`r2_grf_falsifier_tests.py` (read-only).
**Canonical parameters:** α=0.03, γ=0.5, σ=0.0556, `M(p)=(1−p)^{2.7}`,
500 steps, 64×64 periodic, `α_filt=0.25`, `N_req=4`, 10 canonical
seeds `{77, 101, 123, 234, 456, 789, 1011, 1213, 1415, 2021}`.
**ξ_canonical:** 1.758 lattice units (density channel, from
`outputs/ed_sc_3_1/xi_canonical.json`).
**Summary JSON:** `outputs/ed_sc_3_2/v2_scan_summary.json`.
**Wall time:** ≈ 25 s total (simulator of record is ~150× faster
than v1's wrong simulator).

### 10.1 Measured fit table — scan of record

| Grid | L_ray/ξ | L_ray (lattice) | N | S1 median [CI 16–84] | S2 IQR [CI 16–84] | S3 tail slope |
| --- | --- | --- | --- | --- | --- | --- |
| G1 | 0.30 | 0.527 | **0** | — | — | — |
| G2 | 0.50 | 0.879 | **2** | — | — | — |
| **G3** | **1.08** | **1.898** | **33** | **−1.92 [−2.32, −1.75]** | **1.29 [1.01, 1.43]** | **−4.25** |
| G4 | 2.00 | 3.515 | 29 | −2.77 [−3.81, −2.40] | 2.99 [2.47, 4.51] | −1.77 |
| G5 | 3.00 | 5.273 | 18 | −1.82 [−2.04, −1.66] | 0.79 [0.58, 1.05] | −3.22 |
| G6 | 5.00 | 8.788 | 22 | −2.74 [−3.38, −2.38] | 2.52 [1.65, 3.53] | −2.30 |

### 10.2 G3 reproduces the canonical pool

The `T1a_baseline` pool in `r2_grf_falsifier_results.json` reported
N=34, median=−1.881, IQR=1.271, 95 % CI [−2.341, −1.464]. The v2
scan at `L_ray/ξ = 1.08` produced N=33, S1=−1.92, S2=1.29,
16–84 % CI [−2.32, −1.75] — matching the canonical pool **to
within seed-to-seed noise**. This is the independent confirmation
that the rectified simulator-of-record wiring is correct.

### 10.3 Spectral stability across the grid

σ₀, σ₁, σ₂ measured on the raw density field were **identical** at
all six grid points (RSD < 1e-12). This is structurally expected —
only the filter's L_ray varies; the stationary field statistics are
untouched — and confirms the "vary L_ray, fix ξ" protocol held
trivially. The spectral isoperimetric check was not the rate-limiting
consistency constraint in this scan.

### 10.4 S-F2 weak reading — **TRIGGERED**

With S2(G3) = 1.29 as the canonical IQR:

| Neighbour | S2 | |ΔS2| / S2_G3 | Within 20 % tolerance? |
| --- | --- | --- | --- |
| G2 | (N=2, IQR undefined) | — | n/a |
| G3 | 1.29 | 0.0 | ✓ |
| G4 | 2.99 | **1.32** | ✗ |

S-F2 under the weak reading is triggered by G4. The G3→G4 IQR
drift (+132 %) far exceeds the 20 % tolerance. Per the ED-SC 3.0
§5 falsifier register, this is a *trigger*, not automatically a
falsification: the scope memo allows that ED-SC 3.0 rev. 2 may
restate S-F2 as a predicted-curve tolerance rather than a global
constant.

### 10.5 Auxiliary-test observations

- **S1 non-monotonic.** S1 traces `−1.92 → −2.77 → −1.82 → −2.74`
  across G3→G4→G5→G6. Non-monotonicity at 2σ is an architectural
  warning sign per §5.3. The non-monotonic pattern suggests the
  filter is selecting different saddle sub-populations as L_ray
  crosses the field's correlation scale, not a smooth deformation
  of the same distribution.
- **S3 sign consistency holds.** S3 ∈ {−4.25, −1.77, −3.22, −2.30}
  is negative at every populated grid point; S-F1 not triggered.
- **Acceptance rate.** N falls from 33 (G3) to 22 (G6) — consistent
  with the "motif sparsity rises at large L_ray" qualitative
  prediction in §3.2, though not quantitatively compared to the
  pre-registered GRF-linearised curve (which is not reliable off
  G3 given the simulator-of-record mismatch at registration time).

### 10.6 Verdict

ED-SC 3.2 now resolves to: **S-F2 is triggered under the weak
reading** at G4, with a factor-2.3 IQR inflation and a 44 % S1
shift relative to the canonical G3. The hinge does **not** behave
as a smooth, locally-constant function near the canonical
operating point; G3 appears to be a relatively narrow shoulder
beyond which the motif-conditioned distribution reshapes
substantially. This is informative rather than fatal — it
constrains ED-SC 3.0's architectural claim and forces either a
scope revision (S-F2 revised per §6.4) or a depth memo
investigating the G3–G4 transition in detail.

### 10.7 Consequences for ED-SC 3.3

Per ED-SC 3.2 §7 D4 and the rectification memo §7 action 5:

- **ED-SC 3.3 remains blocked** by the S-F2 trigger. Before opening
  a filter-geometry (α_filt, N_req) sweep, the G3–G4 behaviour must
  be understood — otherwise 3.3 will measure filter-geometry
  sensitivity against a canonical baseline that is itself sitting
  on a shoulder of a rapidly-varying curve.
- **Diagnostic memo recommended** (`theory/ED_SC_3_2_5_G3_G4_Transition.md`)
  to densify the grid in `L_ray/ξ ∈ [1.0, 2.5]` at 0.1 spacing and
  map the transition before filter-geometry work proceeds.
- **Scope-refinement candidate.** ED-SC 3.0 §5 S-F2 should probably
  be restated in rev. 2 as a *predicted-curve* rather than
  *constant-tolerance* falsifier, per §6.4. The trigger at G4
  motivates that refinement but does not require it.

---

## 11. Audit trail — v1 retained

The v1 null-result run (`outputs/ed_sc_3_2/scan_summary.json`,
`scan_progress.log`) is retained unmodified as an audit artefact of
the simulator-of-record regression. It is **not** a canonical
ED-SC 3.2 result; §10 replaces it. The v1 driver file
(`analysis/scripts/ed_sc_3_2_lrayxi_scan.py`) is also retained
unmodified for traceability; its use for any future ED-SC 3.x claim
is **prohibited** by the rectification memo's §6 guardrail.

---

*End of ED-SC 3.2 rev. 2. S-F2 weak reading triggered. ED-SC 3.3
remains blocked; diagnostic memo on the G3–G4 transition is the
recommended next artefact.*
