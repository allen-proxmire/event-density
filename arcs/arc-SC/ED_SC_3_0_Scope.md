# ED-SC 3.0 — Correlation-Length Hinge Architecture (Scope Memo)

**Status:** SCOPE — architecture and falsifier triggers only. Rev. 2
refines S-F2 per ED-SC 3.2.5 resonance finding (§5.2).
**Rev. 2 date:** 2026-04-23 (post-ED-SC 3.2.5).
**Supersedes:** ED-SC 2.0 (scalar `r*`) as the canonical cross-scale invariance
statement of the ED framework.
**Retains:** All GR-SC arc results (1.0, 1.1, 1.4–1.8, 2.0 rev. 2) as depth
inputs; mobility-law NEC diagnostic from GR-SC 1.4 as hard constraint.
**Date:** 2026-04-23 (tenth-pass closure; first ED-SC 3.0 artefact).
**Guardrails inherited:** kinematic acoustic metric only; no Einstein
equations; no Schwarzschild; no α; deterministic P4-extremal horizons
measure-zero; free-scalar QFT sector only.

---

## 0. One-paragraph summary

ED-SC 2.0 defined cross-scale invariance through a single scalar `r*`, the
motif-conditioned median of a field-space Hessian ratio on R2. The tenth-pass
closure (see `ED_SC_2_0_r_star_Final_Verdict.md`) showed that `r*` is a
**filtered GRF statistic** with pooled median `-1.88 ± 0.4` (10-seed, N=34),
not a fundamental constant. The r* program's own forensic trail, plus the
GR-SC arc's five-class taxonomy and the spectral-triad coverage
`(σ₀, σ₁, σ₂)`, together reveal that the actual invariant is not a scalar but
a **distribution** `f(ρ | ξ, filter)` hinged on the ED field correlation
length `ξ` and parameterised by the motif filter geometry
`(L_ray, α_filt, N_req)`. ED-SC 3.0 retires the scalar `r*` in favour of this
**correlation-length hinge architecture**, with `L_ray / ξ` as the canonical
dimensionless group and the spectral triad as the measurement channel.

---

## 1. Motivation

### 1.1 Why ED-SC 2.0 (scalar `r*`) is retired

Three findings from the r* program force retirement:

1. **Single-seed fluctuation.** The original `r* ≈ -1.304` was a single-seed
   N=6 artefact. Pooled 10-seed analysis (N=34) gives
   `-1.88 ± 0.4` — the "canonical value" was inside the noise band of the
   statistic itself. A scalar whose third significant figure is a 10-seed
   standard error cannot carry the weight of a cross-scale invariant.

2. **Degenerate cubic-chain identity.** The closed-form
   `r* = -2χ/(2χ − 1)` derived in `ED_SC_2_0_r_star_Derivation_Attempt.md`
   applies to cubic-bistable premises, **not** to R2. The deterministic R2
   chain gives `r* ≈ 0`, not `-1.88`. The analytic scalar and the empirical
   scalar are not the same object.

3. **GRF linearisation is the real machinery.** The observed
   `-1.88` is reproduced to 3 % by linearising R2 near the motif-conditioned
   critical density `p̂ ≈ 0.108` and applying the canonical angular filter to
   the unfiltered saddle-ratio median `-1.94` (`ED_SC_2_0_r_star_R2_GRF.md`).
   What looked like "the ED constant" is the fingerprint of the filter acting
   on the spectral triad.

### 1.2 What the r* and GR-SC arcs revealed about invariants

- **Scalar invariants are shadows of distributions.** r*, `ℛ_W`, `ℛ_Ray`,
  `ℛ_G`, `κ/|μ₁|σ₁`, `C_redshift(r)` all collapse onto a single pooled
  statistic **only** after motif conditioning and filter application. The
  underlying object is a distribution, not a number.

- **Filter geometry is part of the invariant.** Unfiltered saddle-ratio
  median is `-1.94`; canonical angular filter compresses to `-1.88`
  (η_f ≈ 1.25 in the Rayleigh class; 0.80 ± 0.05 half-rise compression in the
  correlation class). Without the filter, the "invariant" moves.

- **Spectral triad is the natural coordinate system.** GR-SC 2.0 rev. 2's
  five-class taxonomy (Ratio / Trace / Quadratic / Rayleigh / Correlation)
  covers exactly `(σ₀, σ₁, σ₂)`. Every class is a projection of the GRF's
  spectral moments through the motif filter.

- **Cross-scale hinges are dimensional.** The one combination that survives
  rescaling, filtering, and pooling is the dimensionless ratio of
  filter support to field correlation length — `L_ray / ξ`. Scale
  invariance of `r*` (falsifier T1) was **inconclusive** precisely because
  rescaling breaks `p̂` and therefore breaks the scalar; the ratio
  `L_ray / ξ` does not break.

### 1.3 Why ED-SC 3.0 must be structural, not numerical

A numerical invariant (pick a number, test it) is falsifiable but brittle:
one seed pool revision and the number moves. A **structural** invariant
specifies the architecture that generates the number — the spectral triad,
the filter, the correlation length, the conditioning — and makes predictions
about the whole distribution: medians, IQR, tails, endpoint behaviour, and
cross-class identities. The GR-SC arc already supplies the structural
pieces. ED-SC 3.0 is the explicit statement that cross-scale invariance
in ED lives in `f(ρ | ξ, filter)`, not in any scalar reduction of it.

---

## 2. Core invariant structure

### 2.1 `ξ` as the cross-scale hinge

The ED field correlation length `ξ` is the scale at which the two-point
function `ξ_φ(r)` decays to a fixed fraction of its zero-lag value `σ₀²`.
It is the only length scale intrinsic to the GRF (independent of the motif
filter) and it sets the dimensional hinge for every cross-scale statement.

**Operational definition (ED-SC 3.0 canonical):**
`ξ = r_½`, the lag at which `C_redshift(r) = 1`, equivalently
`ξ_φ(ξ)/σ₀² = 1/2`. (GR-SC 1.7 correlation-class invariant.)

### 2.2 Filter geometry as part of the invariant

The motif filter enters through three parameters:

- `L_ray` — canonical ray half-length (filter support).
- `α_filt` — angular aperture / weighting shape.
- `N_req` — required number of coincident rays for motif acceptance.

These are not "experimental knobs to tune away"; they are part of the
invariant's definition. Two observers with different filter geometries
see different distributions, but the **architecture** of the distribution
(its dependence on `L_ray / ξ`, `α_filt`, `N_req`) is invariant.

### 2.3 Dimensionless groups

The invariant architecture is built from three dimensionless groups:

| Group | Meaning | Role |
| --- | --- | --- |
| `L_ray / ξ` | filter support vs field coherence | **canonical hinge** |
| `α_filt` | angular aperture | filter shape |
| `N_req` | coincidence requirement | filter stringency |

Scalar invariants correspond to specific slices of this three-parameter
space. The pooled `r* = -1.88 ± 0.4` lives at one particular
`(L_ray/ξ, α_filt, N_req)` point.

### 2.4 Spectral triad as inputs

GR-SC 2.0 rev. 2's five-class taxonomy covers `(σ₀, σ₁, σ₂)`:

- **σ₀** (variance): correlation class (redshift variance plateau).
- **σ₁** (gradient RMS): Rayleigh class (surface-gravity scale).
- **σ₂** (curvature RMS): quadratic / trace / ratio classes.

Cross-class consistency is enforced by the spectral isoperimetric
inequality `σ₀ · σ₂ ≥ σ₁²`. ED-SC 3.0 treats this inequality as a
structural constraint, not an empirical prediction.

### 2.5 Distributional invariants vs scalar invariants

| | Scalar (ED-SC 2.0) | Distributional (ED-SC 3.0) |
| --- | --- | --- |
| Object | `r* ∈ ℝ` | `f(ρ | ξ, L_ray, α_filt, N_req) ∈ 𝒫(ℝ)` |
| Test | point estimate vs prediction | full summary statistic set |
| Brittle to | seed pool, filter choice | only filter mis-specification |
| Falsifier | `r̂* ≠ r*` | shape / endpoint / scaling mismatch |

---

## 3. Replacement for `r*`

### 3.1 `r*` as one projection

Under ED-SC 3.0, the pooled `r* = -1.88 ± 0.4` is preserved as
**one projection** of the higher-dimensional invariant at the canonical
`(L_ray/ξ, α_filt, N_req)` operating point. It remains a legitimate
check — failure of the pooled median to reproduce at that operating point
still falsifies the framework — but it is no longer *the* invariant.

### 3.2 The invariant as `f(ρ | ξ, filter)`

ED-SC 3.0 defines the cross-scale invariant as the motif-conditioned
distribution

    f(ρ | ξ, L_ray, α_filt, N_req)                    (★)

of the field-space Hessian-ratio variable `ρ` under canonical motif
acceptance. The arguments after the bar are the **invariant's
coordinates**, not nuisance parameters. Two theories with the same `(★)`
at matched coordinates are cross-scale equivalent.

### 3.3 Canonical summary statistics

A distributional invariant is verifiable only through a finite set of
summary statistics. ED-SC 3.0 fixes three canonical summaries:

- **S1 — Median.** `med(ρ | ξ, filter)`. Preserves the `r*` program's
  pooled `-1.88 ± 0.4` at the canonical operating point.
- **S2 — IQR.** `IQR(ρ | ξ, filter)`. Tests the filter's dispersion
  prediction; currently ≈ `0.9` at canonical point (from 10-seed pool).
- **S3 — Tail shape.** Upper-tail exponent / log-slope on
  `1 - F(ρ)`. Detects failure of GRF linearisation; an exponential tail
  is the GRF prediction.

Tests that pass S1 but fail S2 or S3 indicate that the filter is
reproducing the median by construction while the underlying field
statistics disagree — a mode of failure invisible to ED-SC 2.0.

---

## 4. Integration with GR-SC 2.0

### 4.1 Five-class taxonomy → ED-SC 3.0 inputs

| GR-SC class | Spectral moment | ED-SC 3.0 role |
| --- | --- | --- |
| Ratio (GR-SC 1.0, 1.1, 1.6) | σ₂ | canonical ρ definition; r* projection |
| Trace-Gaussian (GR-SC 1.0) | σ₂ | alternative summary channel |
| Quadratic (GR-SC 1.6) | σ₂ | bounded-invariant cross-check (`ℛ_W`) |
| **Rayleigh (GR-SC 1.5)** | **σ₁** | **`ξ`-independent gradient-RMS probe** |
| **Correlation (GR-SC 1.7)** | **σ₀ + ξ_φ(r)** | **`ξ` measurement channel** |

The Rayleigh and Correlation classes — new in the tenth pass — are the
two classes that make ED-SC 3.0 possible. Before GR-SC 1.5/1.7 there
was no ED-native way to measure `ξ` and σ₁ independently of the
Hessian-ratio distribution itself.

### 4.2 Depth inputs

The following GR-SC memos become depth inputs, not independent arcs:

- **GR-SC 1.5** — horizon κ Rayleigh statistics → σ₁ channel.
- **GR-SC 1.6** — Weyl-class bounded ratio `ℛ_W ∈ (-2, -1/2)` →
  distributional cross-check independent of `r*`.
- **GR-SC 1.7** — redshift correlation-class → `ξ` measurement.
- **GR-SC 1.8** — EIT-Extremal error budget → falsifier clearance
  condition (σ₁/κ_M^det < 0.036) and two-channel Fieller decomposition.

### 4.3 Spectral triad entry

- σ₀ enters via GR-SC 1.7 (redshift variance plateau).
- σ₁ enters via GR-SC 1.5 (horizon κ Rayleigh scale).
- σ₂ enters via GR-SC 1.0/1.1/1.6 (curvature-invariant variances).

All three are measured from the same underlying GRF realisation; the
spectral isoperimetric inequality `σ₀ · σ₂ ≥ σ₁²` is the consistency
constraint across channels.

---

## 5. Falsifier triggers

ED-SC 3.0 is falsified if **any** of the following occur at matched
operating points `(L_ray/ξ, α_filt, N_req)`:

### 5.1 Experimental falsifiers

- **E-F1** — EIT-Extremal surface-gravity ratio disagrees with the
  GR-SC 1.8 Fieller prediction `median(κ_E/κ_M) ≈ 0.83 · ε_tot` at
  2σ after clearance `σ₁/κ_M^det < 0.036` is met.
- **E-F2** — Measured `ξ` from redshift correlation disagrees with
  `ξ` inferred from σ₀/σ₁ via spectral isoperimetry at 2σ.
- **E-F3** — Pooled `r̂*` at the canonical operating point falls
  outside `-1.88 ± 0.4` across ≥10 independent seed pools.

### 5.2 Ray-budget resonance mapping (rev. 2 clause)

ED-SC 3.2.5 (`theory/ED_SC_3_2_5_G3_G4_Transition.md`) established
that the motif filter exhibits **discrete ray-budget resonances**:
as `L_ray` crosses integer-multiple thresholds of the lattice
saddle-neighbourhood scale, the admitted-motif set changes in
integer-valued jumps, producing sharp transitions in S1/S2/S3
between plateaus of locally stable invariant statistics. Two such
transitions were resolved empirically at `L_ray/ξ ≈ 1.5` and
`≈ 2.1` (absolute `L_ray ≈ 2.64`, `≈ 3.69` lu on the 64² lattice
at `ξ = 1.758`), consistent with the `N_req = 4` filter geometry
encountering first and second lattice shells.

**Mandatory pre-work for any hinge scan:** before a depth memo
claims a falsifier reading in `L_ray/ξ`, it must

1. Sub-sample the hinge at Δ(L_ray/ξ) ≤ 0.1 across the reported
   window to resolve regime boundaries, and
2. Report regime membership for its operating point(s) explicitly.

This is a scope-level requirement, not a suggestion. Failure to
map resonance structure before reporting a falsifier reading is
itself grounds for memo rejection.

### 5.3 Simulator falsifiers

- **S-F1** — `f(ρ | ξ, filter)` upper-tail deviates from GRF-linearised
  exponential at the canonical operating point (fails S3).
- **S-F2 (rev. 2)** — *Within-regime* IQR(ρ) drift exceeds 20 %
  under rescaling of `L_ray / ξ` at fixed `(α_filt, N_req)`.
  "Regime" means a contiguous sub-interval of the hinge on which
  no **ray-budget resonance** transition occurs (see §5.2).
  Cross-regime drifts are **diagnostic, not falsifying**: they
  indicate the hinge scan has crossed a discrete lattice-shell
  threshold of the motif filter, which must be mapped, not
  interpreted as a failure of `(★)`. A candidate resonance
  transition is identified by (i) a step-wise S2 jump > 3× the
  median neighbouring derivative, or (ii) a repeated-value
  fingerprint in S1/S2 across adjacent grid points (a signature
  of integer ray-endpoint coincidences on the lattice).
  **Canonical-window constraint:** the ED-SC 3.1 canonical
  operating point `L_ray/ξ = 1.08` must sit interior to a
  Regime I plateau of width ≥ 0.3 in `L_ray/ξ` on which S-F2
  holds; ED-SC 3.2.5 confirms this (plateau [1.0, 1.4]).
- **S-F3** — Rayleigh-class `κ/(|μ₁|σ₁)` median departs from pooled
  `0.52 ± 0.05` (GR-SC 1.5 prediction).
- **S-F4** — Correlation-class `C_redshift(r)` endpoints depart from
  `C(0)=0, C(∞)=2` (these are **rigid**; any departure falsifies the
  architecture itself, not just a parameter).

### 5.4 Mobility-law constraints (NEC)

- **M-F1** — Any mobility law used in depth memos must satisfy the
  GR-SC 1.4 analogue NEC:
      `Q(ρ) = M''(ρ) - [M'(ρ)]² / (2M(ρ)) ≥ 0`.
- **M-F2** — The canonical linear mobility `M = 1 - ρ` is
  NEC-violating on slopes and is **excluded** from ED-SC 3.0 depth
  work. Saturating (`(1-ρ)^β`, β ≥ 1) or exponential
  (`M_0 e^{-αρ}`) forms are admissible.
- **M-F3** — Any depth memo claiming a new invariant must include an
  explicit NEC check for its mobility profile.

---

## 6. Deliverables

### D1 — Correlation-length hinge invariant

The cross-scale invariant of ED is the motif-conditioned distribution
`f(ρ | ξ, L_ray, α_filt, N_req)`. The scalar `r*` is one projection
(median at canonical operating point). Cross-scale equivalence is
agreement of `f` at matched coordinates, tested through S1/S2/S3
summary statistics.

### D2 — Dimensionless groups and filter geometry

Three dimensionless groups: `L_ray / ξ` (canonical hinge),
`α_filt` (aperture), `N_req` (coincidence). Filter geometry is
**part of the invariant**, not a nuisance. Rescaling that preserves
all three leaves `f` invariant; rescaling that breaks `L_ray / ξ`
re-parameterises it.

### D3 — Integration with spectral triad

- σ₀ via GR-SC 1.7 redshift variance.
- σ₁ via GR-SC 1.5 Rayleigh κ scale.
- σ₂ via GR-SC 1.0/1.1/1.6 curvature variances.
- Consistency: `σ₀ · σ₂ ≥ σ₁²` (spectral isoperimetric bound).

### D4 — Falsifier list

Three experimental (E-F1–3), four simulator (S-F1–4), three mobility
(M-F1–3) — see §5.

### D5 — Roadmap for ED-SC 3.1+

Depth memos, each under its own falsifier triggers:

- **ED-SC 3.1** — `f(ρ | ξ, filter)` explicit form and S1/S2/S3
  baselines at canonical operating point. Consumes GR-SC 1.5/1.7
  as σ₁/ξ measurement channels.
- **ED-SC 3.2** — Two-decade scan in `L_ray / ξ` at fixed
  `(α_filt, N_req)`. Tests S-F2 directly; maps the `r*` projection
  across the hinge.
- **ED-SC 3.3** — Filter-geometry sweep: independent variation of
  `α_filt` and `N_req` at fixed `L_ray / ξ`. Tests whether any
  projection is insensitive to filter shape (candidate
  "geometry-free" scalar).
- **ED-SC 3.4** — Mobility-law scan under NEC (GR-SC 1.4) —
  does `f(ρ | ...)` depend on mobility profile in the
  NEC-admissible family?
- **ED-SC 3.5** — Integration with EIT-Extremal protocol (GR-SC
  1.8): lifts the clearance condition from a scalar (κ_E/κ_M) to
  a distributional test using S1/S2/S3 of `f(ρ | ξ, filter)`
  reconstructed from EIT observables.

---

## 7. Acceptance criteria for this scope memo

This memo is accepted if:

1. The retirement of scalar `r*` as *the* cross-scale invariant is
   explicit and justified (§1.1–1.3).
2. The new invariant `f(ρ | ξ, filter)` is stated as a distribution
   with canonical coordinates (§2–3).
3. Integration with GR-SC 2.0's five-class taxonomy is table-level
   explicit (§4).
4. Falsifier triggers are enumerated before any depth memo is written
   (§5), with the NEC constraint tying back to GR-SC 1.4.
5. The ED-SC 3.1–3.5 roadmap is in place (§6 D5) as a contract; no
   depth memo is committed before this scope memo is signed off.

No numerical predictions are made in this memo beyond those already
carried by GR-SC 2.0 rev. 2. ED-SC 3.0 is architecture; ED-SC 3.1 is
where the first new numerical baseline appears.

---

## 8. Guardrails (inherited, reiterated)

- Kinematic acoustic metric only (`g_eff = diag(-N², 1, 1)`,
  `N = √M(ρ₀)`). No Einstein equations.
- Free-scalar QFT sector only. No gauge, no α, no Schwarzschild.
- Deterministic P4-extremal horizons are measure-zero; generic
  horizons are GRF-statistical.
- Mobility laws must satisfy the GR-SC 1.4 analogue NEC.
- Filter geometry is part of the invariant — no "deconvolving" it
  away.
- Pooled `r* = -1.88 ± 0.4` is a projection check, not *the*
  invariant.

---

*End of ED-SC 3.0 scope memo. Next artefact: `theory/ED_SC_3_1_*.md`
depth memo, contingent on sign-off of this scope document.*

---

## Changelog

- **Rev. 1 (2026-04-23):** initial scope memo.
- **Rev. 2 (2026-04-23, post-ED-SC 3.2.5):**
  - §5.1 **S-F2 restated** as within-regime tolerance (not flat
    20 % across the full hinge). Cross-regime drifts are
    diagnostic, not falsifying.
  - §5.2 **new clause** — ray-budget resonance mapping is now a
    mandatory scope-level pre-work requirement for any
    `L_ray/ξ` scan.
  - §5.3 renumbered from §5.2 (simulator falsifiers).
  - §5.4 renumbered from §5.3 (mobility-law / NEC).
  - Canonical-window constraint added to S-F2: canonical point
    must sit interior to a ≥ 0.3-wide Regime I plateau
    (ED-SC 3.2.5 confirms: plateau [1.0, 1.4]).
