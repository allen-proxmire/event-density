# GR-SC 2.0 — Consolidation: Curvature Invariants on the ED Acoustic Metric

**Arc:** GR-SC (General-Relativistic Structural Correspondences)
**Status:** Consolidation memo (rev. 2, five-class taxonomy)
**Date:** 2026-04-23 (tenth pass; originally drafted earlier same day as a four-class consolidation; revised in place to incorporate GR-SC 1.7 correlation-class and 1.8 EIT-Extremal error-budget integration)
**Sources:** GR-SC 1.0 (Einstein), 1.1 (Raychaudhuri), 1.4 (Analogue NEC), 1.5 (Horizon κ), 1.6 (Weyl), 1.7 (Redshift / correlation-class), 1.8 (EIT-Extremal error budget)
**Companion:** ED-SC 2.0 (r* and motif-conditioned field-space Hessian)

This document consolidates the GR-SC 1.x arc into a single structural classification of curvature invariants on the kinematic ED acoustic metric `g_eff[ρ_0]`. It is the GR analogue of ED-SC 2.0 and shares the same linearisation and motif-conditioning machinery. No new derivations; see the 1.x memos for proofs and numerics.

---

## 1. Executive summary

**What GR-SC is.** A program of computing standard general-relativistic curvature invariants (Ricci, Einstein, Weyl, Raychaudhuri focusing, surface gravity, redshift) on the ED kinematic acoustic metric `g_eff = diag(−N², 1, 1)` with `N = √M(ρ_0)`, then treating the background `ρ_0 = ρ̂ + φ` as a 2D isotropic Gaussian random field and conditioning on the motif envelope used in ED-SC 2.0. Strictly kinematic: no Einstein equations, no ADM, no Hawking physics.

**What was computed.** Seven invariants across seven memos plus one integration memo:

| Memo | Invariants | Core result |
|---|---|---|
| 1.0 | `G_{μν}`, `tr(G^ij)`, `det(G^ij)`, `ℛ_G` | `G_00 = 0` identity; spatial ratio = r*; three-class decomposition |
| 1.1 | `R_{μν} u^μ u^ν`, `F̄`, `ℛ_Ray` | Focusing trace is Gaussian; focusing ratio = r* |
| 1.4 | NEC inequality | Reduces to `(√M)''(ρ) ≥ 0`; sorts mobility families |
| 1.5 | `κ` on horizons | Rayleigh-distributed, threshold-independent |
| 1.6 | `C_{abcd}`, `C²`, `ℛ_W` | `B_{ab} ≡ 0`; bounded ratio `ℛ_W ∈ (−2, −1/2)`; quadratic scalar |
| 1.7 | `Δν/ν`, `C_redshift(r)` | First two-point invariant; rigid envelope `C(0)=0, C(∞)=2`; σ_0 entered |
| 1.8 | EIT-Extremal budget | Fieller ratio for `κ_E/κ_M`; two noise channels; clearance target `σ_1/κ_M^det < 0.036` |

**The five invariant classes.** Every curvature scalar computed on `g_eff[ρ_0]` to linear order in `φ` falls into one of five classes:

1. **Ratio-class (σ_2)** — dimensionless, mobility-universal, typically unbounded. Members: `r*`, `ℛ_Ray`, `ℛ_G` (spatial block), `ℛ_W` (bounded subclass in `(−2, −1/2)`).
2. **Trace / Gaussian-class (σ_2)** — scales linearly with `|μ₁|σ_2`, symmetric around zero, Gaussian. Members: `F̄` (angle-averaged focusing), `tr(G^{ij})`, scalar Ricci `R`.
3. **Quadratic-class (σ_2²)** — sign-definite, scales as `μ₁² σ_2²`, saddle-averaged median ≠ 0. Members: `C²` (Weyl square), `det(G^{ij})`.
4. **Rayleigh-class (σ_1)** — linear in `|N̂'| σ_1`, support on `[0, ∞)`, no support at 0. Member: `κ` (surface gravity on horizons).
5. **Correlation-class (σ_0, ξ_φ(r))** — *new in rev. 2.* Two-point invariant depending on the correlation function `ξ_φ(r)` of φ. Scales with `μ₁² σ_0²` at the plateau; rigid envelope endpoints. Member: `C_redshift(r)` (fractional-frequency-shift two-point variance).

**Spectral triad coverage.** Each class reads a different spectral moment of the GRF:

| Class | Spectral input | Observable channel |
|---|---|---|
| Ratio / Trace / Quadratic | σ_2 (Hessian) | second-derivative content |
| Rayleigh | σ_1 (gradient) | first-derivative content |
| Correlation | σ_0, ξ_φ(r) | value + correlation function |

The arc covers the full `(σ_0, σ_1, σ_2)` spectral triad. A cross-check relation, `σ_0 · σ_2 ≥ σ_1²` (isoperimetric inequality on GRF spectral moments), must hold in any measurement on an isotropic Gaussian motif field.

**Mobility-universality results.** Ratio-class invariants are **mobility-universal**: they depend on `M(ρ)` only through the axis-swap sign. Trace- and quadratic-class invariants carry `μ₁ = M'(ρ̂)/(2M(ρ̂))` as an overall scale. Rayleigh-class carries `|N̂'| = |μ₁| N̂`. Correlation-class carries `μ₁²` at the plateau but yields a mobility-universal filter signature in the half-rise ratio (§3.5).

**Structural predictions.** The arc produces ten durable pooled-R2 predictions (§5 table), two structural identities (`G_00 = 0`, `B_{ab} = 0`), one mobility-law-level constraint (NEC diagnostic `Q ≥ 0`), one algebraic curve `ℛ_W(r*) = −(2r*+1)/(r*+2)` tying Weyl and r*, one rigid two-point envelope `C_redshift(0) = 0` / `C_redshift(∞) = 2`, and one engineering clearance target `σ_1/κ_M^det < 0.036` for the EIT-Extremal experiment.

---

## 2. Acoustic metric geometry

**Metric.** `g_eff = diag(−N²(x), 1, 1)`, `N = √M(ρ_0)`, static ultrastatic with flat spatial block. In 2+1D for ED-SC convention; trivial z-uplift to 3+1D only for Weyl (Weyl vanishes in d ≤ 3).

**Non-zero curvature components** (all derivable from `N(x)`):

```
R_{00}     = N ∇²N
R_{ij}     = −N_{,ij} / N
R          = −2 ∇²N / N         (scalar Ricci in 2+1D)
G_{00}     = 0                  (identity, §3)
G_{ij}     = (1/N)·[ δ_{ij} tr(H_N) − (H_N)_{ij} ]
E_{ij}     = (1/(2N))·traceless(H_N^{(3D)})      (Weyl electric, after z-uplift)
B_{ij}     = 0                  (identity, §3)
κ          = (1/2) |∇N|         on level sets
F          = −R_{μν} u^μ u^ν    Raychaudhuri focusing for u = N^{-1} ∂_t
Δν/ν       = N(x_1)/N(x_2) − 1  redshift between two static observers
```

**Linearisation.** `ρ_0 = ρ̂ + φ` with `φ` a 2D isotropic GRF having spectral moments `σ_0², σ_1², σ_2²`. Then

```
N = N̂ + N̂' φ,        N̂ = √M(ρ̂),   N̂' = M'(ρ̂)/(2√M(ρ̂)),
μ₁ = N̂'/N̂ = M'(ρ̂)/(2 M(ρ̂)),
∇N = N̂' ∇φ,    H_N = N̂' H_φ + O(φ).
```

All GR-SC invariants reduce to linear combinations of `φ`, `∇φ`, and `H_φ` (pointwise) or `φ(x_1) − φ(x_2)` (two-point) weighted by powers of `μ₁` and `N̂`. The motif-conditioning filter is identical to ED-SC 2.0 (canonical ray-endpoint filter).

---

## 3. The five invariant classes

### 3.1 Ratio-class (σ_2)

Invariants built from ratios of eigenvalues of `H_φ`. The spatial-Hessian eigenvalue ratio `t = λ_1/λ_2` is the fundamental motif-saddle parameter; every ratio-class invariant is an algebraic function of `t`.

| Invariant | Closed form in `t` | Range | Pooled R2 median |
|---|---|---|---|
| `r*` (ED-SC 2.0) | `t` | `ℝ` | `−1.88 ± 0.40` |
| `ℛ_Ray` (1.1) | `t` | `ℝ` | `−1.88 ± 0.40` |
| `ℛ_G` spatial (1.0) | `t` | `ℝ` | `−1.88 ± 0.40` |
| `ℛ_W` (1.6) | `−(2t+1)/(t+2)` | `(−2, −1/2)` | `−1.23 ± 0.05` |

**Mobility-universality.** All four are independent of `μ₁`, `N̂`, and mobility normalisation. They depend on `M(ρ)` only through whether `M'` is positive or negative (axis orientation).

**Motif-conditioning.** Canonical ray-endpoint filter applied to GRF saddles of `φ`. Pooled 10-seed statistics match ED-SC 2.0 r* protocol.

**Structural identity.** `ℛ_Ray = ℛ_G^{spatial} = r*` exactly in distribution. `ℛ_W = −(2r*+1)/(r*+2)` is an algebraic map that collapses the joint `(r*, ℛ_W)` to a 1D curve in the clean-saddle limit.

### 3.2 Trace / Gaussian-class (σ_2)

Invariants linear in `H_φ` via its trace. Gaussian-distributed around zero with RMS scaling linearly with `|μ₁|σ_2`.

| Invariant | Closed form | Distribution | RMS at R2 canonical |
|---|---|---|---|
| `F̄` (angle-averaged focusing, 1.1) | `−(μ₁/2) tr(H_φ)` | `N(0, μ₁² σ_2² / 4)` | ≈ 0.068 |
| `tr(G^{ij})` (1.0) | `(μ₁/N̂)·tr(H_φ)` at linear order | `N(0, μ₁² σ_2² / N̂²)` | ≈ 0.078 |
| `R` (scalar Ricci) | `−2 μ₁ ∇²φ / N̂` | `N(0, 4 μ₁² σ_2² / N̂²)` | ≈ 0.156 |

**Mobility-dependence.** Overall scale `|μ₁| σ_2`; sign symmetric. All three vanish in median under any motif filter that is reflection-symmetric in the GRF.

**Structural identity.** `median = 0` is a **rigid** prediction: the three trace-class invariants are odd under `φ → −φ`, and any symmetric filter preserves this. A measured non-zero median of any trace-class invariant falsifies either the GRF isotropy or the filter symmetry.

### 3.3 Quadratic-class (σ_2²)

Invariants quadratic in `H_φ`. Sign-definite, scales as `μ₁² σ_2²`, saddle-averaged median `O(1) × μ₁² σ_2²`.

| Invariant | Closed form | Sign | Median coeff (×μ₁²σ_2²) |
|---|---|---|---|
| `C²` Weyl square (1.6) | `(4μ₁²/3)(3s² + u²)` | ≥ 0 | ≈ 2.13 |
| `det(G^{ij})` (1.0) | `(μ₁²/N̂²)·det(H_φ)` | ≤ 0 (at saddles) | ≈ −0.42 |

(Here `s = (λ_1+λ_2)/2`, `u = (λ_1−λ_2)/2` from the saddle decomposition, with GRF moments `⟨s²⟩ = 7σ_2²/12`, `⟨u²⟩ = σ_2²/12`.)

**Mobility-dependence.** Scales as `μ₁² σ_2²`. Halving `σ_2` by smoothing divides the median curvature scalar by 4. Changing the mobility magnitude at `ρ̂` rescales the median as `|M'|²/|M|`.

### 3.4 Rayleigh-class (σ_1)

Single member: surface gravity on acoustic horizons.

| Invariant | Closed form | Distribution | Pooled R2 dimensionless |
|---|---|---|---|
| `κ` (1.5) | `(1/2)|N̂'|·|∇φ|` on Σ_h | `Rayleigh(|N̂'|σ_1/(2√2))` | `κ/(|μ₁|σ_1) = 0.52 ± 0.05` |

**Key features.**
- Support `[0, ∞)`, `P(κ = 0) = 0` — deterministic extremal horizons are measure-zero.
- Threshold-independent — identical Rayleigh law on every level set of `N(x)`.
- Motif filter preserves Rayleigh shape; rescales by `η_f ≈ 1.25`.
- Scales linearly with `|N̂'| σ_1` (not `σ_2`, since it reads first-derivative spectral content).

### 3.5 Correlation-class (σ_0, ξ_φ(r)) — new in rev. 2 (GR-SC 1.7)

First two-point GR-SC invariant. Content carried by the correlation function `ξ_φ(r) = ⟨φ(x) φ(x+r)⟩` rather than by a local spectral moment.

**Linearised redshift.**

```
Δν/ν  =  μ₁ · ( φ(x_1) − φ(x_2) )     (two static observers at x_1, x_2).
```

**Variance profile.**

```
Var(Δν/ν)(r)  =  2 μ₁² [ σ_0² − ξ_φ(r) ],      r = |x_1 − x_2|.
```

**Dimensionless correlation-class invariant.**

```
C_redshift(r)  ≡  Var(Δν/ν)(r) / (μ₁² σ_0²)
                =  2 · [ 1 − ξ_φ(r) / σ_0² ].
```

| r-limit | `ξ_φ(r)` | `C_redshift(r)` | Status |
|---|---|---|---|
| `r → 0` | `σ_0²` | `0` | rigid |
| `r → ∞` | `0` | `2` | rigid |

**Rigid envelope.** `C_redshift(0) = 0` and `C_redshift(∞) = 2` hold under any mobility law, any motif filter, and any isotropic GRF. The **shape** of the rise between 0 and 2 is the observable content; `ξ_φ(r)` is directly recoverable via `ξ_φ(r) = σ_0² [1 − C_redshift(r)/2]`.

**Motif-conditioning.** The canonical ray-endpoint filter enhances short-range `ξ_φ` (both endpoints sit on the same motif slope) and reduces long-range `ξ_φ` (faster independence onset). **Both endpoint rigidities are preserved.** The half-rise separation `r_½` (where `C_redshift(r_½) = 1`) compresses under filtering:

```
r_½^{filt} / r_½^{unfilt}  =  0.80 ± 0.05       (10-seed pooled R2).
```

This ratio is both **mobility-universal** and **σ_0-universal** — it probes only the motif-filter geometry applied to the R2 kernel. Cleanest correlation-class falsifier.

**Key structural features.**
- First two-point GR-SC invariant; introduces correlation-function content `ξ_φ(r)` as a new observable axis.
- Reads σ_0 (value variance), completing the `(σ_0, σ_1, σ_2)` spectral triad alongside κ (σ_1) and the Hessian classes (σ_2).
- Native observable of EIT / cold-atom analogue-gravity apparatuses (frequency-shift autocorrelation between two spatial regions).

---

## 4. Mobility-law constraints (GR-SC 1.4)

The analogue NEC `R_{μν} k^μ k^ν ≥ 0` on all `g_eff`-null vectors reduces to pointwise convexity of `N(x) = √M(ρ_0(x))`, which further reduces to the scalar diagnostic

```
Q(ρ) ≡ M''(ρ) − M'(ρ)² / (2 M(ρ))     (=  2√M · (√M)''(ρ) )
```

and the sign of `M'` at motif extrema. The sign of `Q` sorts ED mobility laws:

| Mobility `M(ρ)` | `Q(ρ)` sign | NEC verdict |
|---|---|---|
| `(1−ρ)^β`, β ≥ 2 | ≥ 0 | **NEC-safe** |
| `(1−ρ)^2` | 0 | marginal |
| `(1−ρ)^β`, 0 < β < 2 | < 0 | NEC-violating on slopes |
| `1−ρ` (canonical linear β=1) | < 0 | **NEC-violating** |
| `M_0/(1+αρ)` | > 0 | NEC-safe |
| `M_0 e^{−αρ}` | > 0 | NEC-safe |

**Implications.**
- ED's default linear mobility does **not** enforce focusing: null congruences can defocus on steep-gradient regions.
- Focusing is locally restored at motif extrema (∇ρ = 0), which is the regime where GR-SC 1.1 `ℛ_Ray` is defined. The saddle-restricted ratio-class statistics are therefore consistent regardless of NEC sign.
- If ED wishes to import standard focusing theorems (horizon-area monotonicity, topological censorship analogues), the mobility must be promoted to a `Q ≥ 0` family.

**Curvature-sign implications.** `Q < 0` allows negative-eigenvalue `H_N`, hence negative `R_{μν} k^μ k^ν` on specific directions — equivalently, the acoustic analogue admits negative effective null energy.

---

## 5. Falsifiable predictions (unified table)

Pooled-R2 canonical values: `μ₁ = −1.513`, `σ_2 = 0.0898` (R2 kernel), `η_f ≈ 1.25` (canonical filter factor), 10-seed pooled band. `σ_0`, `σ_1`, `ℓ_R2`, `κ_M^det` are apparatus-specific.

| Class | Invariant | Prediction | Universality | Threshold-indep? |
|---|---|---|---|---|
| Ratio | `r*` | `−1.88 ± 0.40` | mobility-universal | n/a |
| Ratio | `ℛ_Ray` | `−1.88 ± 0.40` | mobility-universal | n/a |
| Ratio | `ℛ_G^{spatial}` | `−1.88 ± 0.40` | mobility-universal | n/a |
| Ratio | `ℛ_W` | `−1.23 ± 0.05` (bounded) | mobility-universal | n/a |
| Trace | `median(R)` | `0` (rigid) | — | yes |
| Trace | `median(tr G^{ij})` | `0` (rigid) | — | yes |
| Trace | `median(F̄)` | `0` (rigid) | — | yes |
| Quadratic | `⟨C²⟩ / (μ₁² σ_2²)` | `≈ 2.44` (mean), `≈ 2.13` (median) | mobility-dependent | yes |
| Quadratic | `⟨det G^{ij}⟩ / (μ₁² σ_2² / N̂²)` | `≈ −0.42` (median at saddles) | mobility-dependent | yes |
| Rayleigh | `κ / (|μ₁| σ_1)` | `0.52 ± 0.05` | mobility-dependent | **yes** (threshold-invariant) |
| Correlation | `C_redshift(0)` | `0` (rigid) | all mobility | n/a |
| Correlation | `C_redshift(∞)` | `2` (rigid) | all mobility | n/a |
| Correlation | `r_½^{filt} / r_½^{unfilt}` | `0.80 ± 0.05` | mobility- and σ_0-universal | — |
| EIT ratio | `median(κ_E/κ_M)` | `≈ 0.83 · σ_κ^tot/κ_M^det` | apparatus-specific | within-apparatus |
| EIT ratio | `width(κ_E/κ_M)` | `≈ σ_1/κ_M^det` (leading) | apparatus-specific | within-apparatus |
| EIT clearance | `σ_1/κ_M^det` | `< 0.036` (2σ target) | engineering design target | — |
| Identity | `G_{00}` | `≡ 0` (rigid) | all mobility | all thresholds |
| Identity | `B_{ab}` | `≡ 0` (rigid) | all mobility | all thresholds |
| NEC | `sign(Q(ρ))` | `< 0` for canonical ED | mobility selector | — |
| Algebraic | `ℛ_W = −(2r*+1)/(r*+2)` | 1D curve in joint | mobility-universal | — |
| Spectral | `σ_0 · σ_2 ≥ σ_1²` | isoperimetric (rigid) | GRF consistency | — |

**Universal vs mobility-dependent.** Four ratio-class predictions, three correlation-class rigidities (endpoints + filter ratio), two rigid metric identities, and the spectral isoperimetric inequality are mobility-universal. Three trace-class medians are rigid at zero. Quadratic-, Rayleigh-, and EIT-Extremal predictions scale with explicit `(μ₁, σ_0, σ_1, σ_2, κ_M^det)` parameters and must be reported with that context.

**Threshold-indep invariants.** All level-set / saddle-restricted statistics (ratio, quadratic, Rayleigh, correlation) are independent of the horizon threshold or motif-peak threshold. Only trace-class statistics are point-statistics and therefore trivially threshold-free.

---

## 6. Structural implications for ED

**What ED geometry can reproduce from GR.**
- All Ricci / Einstein / Weyl / Raychaudhuri invariants to linear order in a GRF motif background.
- A mobility-law-level NEC diagnostic that correctly sorts focusing vs defocusing.
- A bounded ratio invariant (`ℛ_W`) that is qualitatively sharper than r* (±0.05 vs ±0.40).
- A horizon surface-gravity distribution (`κ`, Rayleigh) consistent with both the deterministic P4 extremal limit and the GRF-roughened generic regime.
- A two-point frequency-shift invariant (`C_redshift(r)`) native to EIT / cold-atom apparatuses.
- A quantitative error budget for the live EIT-Extremal protocol with an explicit engineering clearance target.

**What ED geometry cannot reproduce (and why).**
- **No Einstein equations.** `G_{μν} = 8πG T_{μν}` is never imposed; the ED stress-energy sector is kinematic only (free scalar). `G_00 = 0` is a *metric* identity here, not a *dynamical* vacuum statement.
- **No Schwarzschild, no 1/r gravity, no α.** Confirmed in the closed arc `project_ed10_geometry_qft_scope`. GR-SC respects that guardrail: every invariant here is evaluated on `g_eff[ρ_0]`, not solved for.
- **No magnetic Weyl, no frame-dragging.** `B_{ab} ≡ 0` on any static ultrastatic acoustic metric (rigid). ED cannot import gravitomagnetic phenomenology from this geometry.
- **No Hawking temperature.** `κ` here is a geometric quantity only; quantising the acoustic phonon field would be a separate dynamical step.

**Why these invariants are kinematic, not dynamical.** Every result above follows from (a) the metric ansatz `g_eff`, (b) linearisation in `φ`, and (c) GRF statistics of `φ` plus motif filtering. No field equation, no action principle, no variational derivation. The GR-SC arc is best read as a *dictionary of geometric identities* that the ED kinematic metric must satisfy, plus their motif-conditioned statistical consequences.

**How GR-SC integrates with ED-SC.**
- ED-SC 2.0 provides the GRF machinery (saddle density, ray-endpoint filter, pooled-R2 canonical `(μ₁, σ_2)`).
- GR-SC 1.x imports that machinery wholesale and applies it to geometric curvature contractions.
- Three ratio-class invariants collapse onto `r*` identically — GR-SC is *predicted* by ED-SC on the ratio axis.
- One ratio-class invariant (`ℛ_W`) is new and bounded, providing a sharper test.
- Rayleigh-class `κ` adds a first-derivative-spectrum prediction that ED-SC 2.0 did not reach (σ_1 enters instead of σ_2).
- Correlation-class `C_redshift(r)` adds value-variance + correlation-function content (σ_0, ξ_φ), the final axis of the spectral triad.

**What this enables for future arcs.**
- **EIT-Extremal execution (delivered in 1.8).** The error budget is now quantitatively specified with a two-channel noise model and a clearance target.
- **Analogue focusing experiments.** The NEC sorting table (§4) tells any experimentalist which mobility profile to engineer for null focusing vs defocusing. A mobility promotion to `(1−ρ)^β≥2` or `M_0/(1+αρ)` makes ED's acoustic geometry focusing-safe.
- **Higher-moment curvature invariants.** `R²`, `R_{μν}R^{μν}`, `R_{μνρσ}R^{μνρσ}`, Kretschmann, etc. — all decompose into the five classes above with coefficients set by the μ₁-weighted moment algebra already developed.
- **ED-SC 3.0 (queued).** The correlation-length hinge `L_ray / ξ_{R2}` plus the spectral-triad `(σ_0, σ_1, σ_2)` plus filter geometry is the natural structural successor to ED-SC 2.0. Materials from 1.7 and 1.8 are prerequisites.
- **Cosmological-regime transport.** The mobility-law selector from 1.4 may place constraints on the galactic-scale mobility used in the merger-lag and weak-lensing-activity cosmological tests.

---

## 7. EIT-Extremal error-budget integration (GR-SC 1.8)

GR-SC 1.8 applies the Rayleigh-class `κ` from 1.5 and the correlation-class `Δν/ν` from 1.7 to the live EIT-Extremal protocol (`experiements/ED-Acoustic-EIT-Extremal_InProcess/`), producing a quantitative error budget for the deterministic `κ_E / κ_M < 0.1` prediction.

### 7.1 Two GRF-induced noise channels

**Channel A — intrinsic Rayleigh** (from 1.5). Horizon-point `|∇φ|` is Rayleigh-distributed; motif-filtered scale:

```
σ_{κ,A}  =  η_f · |N̂'| · σ_1 / (2√2)   ≈  0.53 · σ_1       (R2 canonical, η_f ≈ 1.25, |N̂'| = 1.513).
```

**Channel B — redshift reconstruction noise** (from 1.7). EIT reconstructs `N(x)` from probe-field detunings; near-field noise is bounded by the R2 correlation length:

```
σ_{κ,B}  ≈  (1/2) · |N̂'| · σ_0 / ℓ_R2   ≈  0.76 · σ_1       (using σ_0/ℓ_R2 ≈ σ_1 by spectral scaling).
```

**Combined in quadrature:**

```
σ_{κ,tot}  =  √( σ_{κ,A}² + σ_{κ,B}² )  ≈  0.93 · σ_1.
```

Channel B dominates by ×1.4 in R2 canonical conditions — reconstruction noise is **of the same order as** intrinsic physical fluctuation, neither dominating.

### 7.2 Fieller-type ratio distribution for κ_E / κ_M

With `κ_E ~ Rayleigh(σ_{κ,tot})` (E-configuration designed to be near-extremal) and `κ_M ~ N(κ_M^det, σ_{κ,tot}^2)` (M-configuration at finite deterministic baseline), the within-apparatus ratio has:

```
median(κ_E / κ_M)  ≈  0.83 · ε_tot,       ε_tot ≡ σ_{κ,tot} / κ_M^det,
IQR              ≈  0.55 · ε_tot,
95% upper tail   ≈  1.80 · ε_tot.
```

For spatially close E- and M-horizons sharing motifs, correlation coefficient `ρ_EM ≈ 0.2–0.4` tightens the ratio width by 10–20%.

### 7.3 Engineering clearance condition

Falsification of the deterministic `κ_E / κ_M < 0.1` prediction at 2σ requires:

```
median(κ_E/κ_M) + 2σ  <  0.1
⇒  0.83 ε_tot + 2 ε_tot  <  0.1
⇒  ε_tot  <  0.035
⇒  σ_1 / κ_M^det  <  0.036       (2σ falsification-clearance target).
```

Apparatuses meeting `σ_1/κ_M^det < 0.036` can cleanly falsify the prediction. Apparatuses with `σ_1/κ_M^det > 0.1` cannot discriminate even under perfect kinematic-acoustic-metric assumptions.

### 7.4 Seven falsifiable EIT-Extremal predictions

- **E-P1 (zero-lag rigidity):** `C_exp(0) = 0` to measurement resolution. Non-zero → falsifies the linearised acoustic-metric kinematic assumption.
- **E-P2 (plateau):** `Var(Δν/ν)(∞) / (μ₁² σ_0²) = 2`, rigid.
- **E-P3 (κ pooled):** `κ_pooled / (|μ₁| σ_1) = 0.52 ± 0.05`, from 1.5.
- **E-P4 (spectral inequality):** `σ_0 · σ_2 ≥ σ_1²`. Violation → non-Gaussian motif field.
- **E-P5 (ratio width):** `width(κ_E/κ_M) ≈ 0.98 · σ_1 / κ_M^det`. Empirical width inconsistent with this falsifies 1.5 or 1.7.
- **E-P6 (ratio median):** `median(κ_E/κ_M) ≈ 0.83 · σ_{κ,tot} / κ_M^det`, not zero. Any claim of zero-ratio within GRF noise regime contradicts the Rayleigh-class model.
- **E-P7 (falsification clearance):** `σ_1/κ_M^det < 0.036` is the 2σ clearance target.

### 7.5 Honesty caveat preserved

The `κ_E / κ_M < 0.1` **central prediction** is shared with standard analogue gravity, not ED-unique. GR-SC 1.8's contribution is the **calibrated noise model** and **engineering clearance criterion** that convert a deterministic yes/no test into a statistically well-posed experimental design. Cross-regime consistency with the rest of the GR-SC arc (ratio-class / trace-class / quadratic-class pooled-R2 predictions, NEC mobility diagnostic) is the real ED-specific content.

---

## 8. Experimental integration — mapping classes to EIT observables

This section summarises how each GR-SC class appears in an EIT / cold-atom analogue-gravity apparatus. The apparatus reconstructs `N(x)` (group-index profile) via probe-field detuning on a spatial grid, then derives spatial derivatives and horizon level sets from the reconstructed profile.

| Class | Observable in EIT | Extraction channel | Spectral moment probed |
|---|---|---|---|
| Ratio (`r*`, `ℛ_Ray`, `ℛ_G`, `ℛ_W`) | Saddle-point eigenvalue ratios of `H_N` | Motif identification + `H_N` diagonalisation + canonical ray-endpoint filter | σ_2 via `|H_N|²` averaging |
| Trace (`R`, `tr G^{ij}`, `F̄`) | Point-averages of `∇²N` / traces | Laplacian finite-difference on `N(x)` grid | σ_2 (same) |
| Quadratic (`C²`, `det G^{ij}`) | Point-averages of `|H_N|²` / `det H_N` | Second-difference tensor; eigenvalue product | σ_2² |
| Rayleigh (`κ`) | Surface gravity on horizon level sets | Locate `{x : N(x) = N_h}`; compute `|∇N|/2` along level set | σ_1 via `⟨|∇N|²⟩` |
| Correlation (`C_redshift(r)`) | Two-region detuning autocorrelation | `C_exp(r) = ⟨(Δν/ν)(x)·(Δν/ν)(x+r)⟩_x` | σ_0 via plateau; ξ_φ via rise shape |

**Independent spectral-moment measurement.** Three distinct channels for `σ_0, σ_1, σ_2` are available within one EIT run:

- **σ_0** from `Var(Δν/ν)` plateau: `σ_0² = Var(Δν/ν)(∞) / (2 μ₁²)`.
- **σ_1** from gradient variance: `σ_1² = ⟨|∇N|²⟩ / (2 N̂² μ₁²)`.
- **σ_2** from Hessian variance: `σ_2² ∝ ⟨|H_N|²⟩ / (N̂² μ₁²)` with the proportionality constant fixed by GRF isotropy.

Consistency check: the three independent measurements must satisfy the isoperimetric inequality `σ_0 · σ_2 ≥ σ_1²`. Violation → non-Gaussian motif field or apparatus-noise contamination.

**Cross-arc cross-check.** Channel A of 1.8 (Rayleigh κ) reads σ_1; Channel B of 1.8 (redshift reconstruction) reads σ_0. Both must be reported for the same motif-field realisation, and the predicted ratio `σ_{κ,B}/σ_{κ,A} ≈ 1.4` can be verified independently of κ_M^det.

**EIT-Extremal workflow.**

1. Shape the EIT control field to produce the E- and M-configurations; toggle within the same atomic cell.
2. Measure probe-field detuning on a dense spatial grid in each configuration.
3. Reconstruct `N(x)`; extract `σ_0, σ_1, σ_2`; verify the isoperimetric inequality.
4. Locate horizon level sets; compute `κ_E` and `κ_M` per realisation.
5. Pool ≥ 10 independent control-field roughness seeds.
6. Check E-P1 through E-P7 (§7.4).
7. Report pooled `median(κ_E/κ_M)` vs the deterministic `0.1` threshold with explicit `σ_1/κ_M^det` reported.

The measurements in steps 3–4 are sufficient to reconstruct every GR-SC class-level prediction (§5 table) from one EIT run.

---

## 9. Deliverables

**D1 — Five-class taxonomy.** Every curvature scalar on `g_eff[ρ_0]` to linear order in `φ` belongs to one of: Ratio (σ_2, mobility-universal), Trace/Gaussian (σ_2, median 0), Quadratic (σ_2², sign-definite), Rayleigh (σ_1, support `[0,∞)`), or Correlation (σ_0 + ξ_φ(r), two-point).

**D2 — Mobility-law NEC constraint.** Analogue NEC `R_{μν}k^μ k^ν ≥ 0` is equivalent to `(√M)''(ρ) ≥ 0`. Canonical ED `M = 1−ρ` violates NEC on slopes; `β ≥ 2` power-law, saturating, and exponential mobilities are NEC-safe.

**D3 — Pooled-R2 predictions.**

```
r*         =  −1.88 ± 0.40                      ratio, mobility-universal
ℛ_Ray      =  −1.88 ± 0.40                      ratio, mobility-universal
ℛ_G^sp     =  −1.88 ± 0.40                      ratio, mobility-universal
ℛ_W        =  −1.23 ± 0.05  (bounded (−2,−1/2)) ratio, mobility-universal
R, tr G, F̄    median = 0 (rigid)                trace
⟨C²⟩          ≈ 2.44 μ₁²σ_2²                    quadratic
med(C²)       ≈ 2.13 μ₁²σ_2²                    quadratic
med(det G)    ≈ −0.42 μ₁²σ_2²/N̂²                 quadratic
κ/(|μ₁|σ_1)   =  0.52 ± 0.05                    Rayleigh, threshold-indep
C_redshift(0) =  0 (rigid)                       correlation, endpoint
C_redshift(∞) =  2 (rigid)                       correlation, endpoint
r_½^f/r_½^u   =  0.80 ± 0.05                     correlation, mobility/σ_0-univ
σ_1/κ_M^det   <  0.036 (2σ target)               EIT engineering clearance
σ_0·σ_2 ≥ σ_1²   (rigid)                         spectral-moment consistency
```

**D4 — Rigid identities.** `G_{00} ≡ 0`, `B_{ab} ≡ 0`, `median(trace-class) ≡ 0` under reflection-symmetric filtering, `C_redshift(0) ≡ 0` and `C_redshift(∞) ≡ 2`, spectral isoperimetric `σ_0σ_2 ≥ σ_1²`.

**D5 — Unified structural picture.** Curvature in ED is a layered object: (i) a deterministic acoustic geometry set by `M(ρ_0)`, (ii) GRF linearisation in `φ` that promotes every deterministic identity into a distributional law, (iii) motif-conditioning that reshapes those distributions through the ray-endpoint filter, and (iv) a five-class algebraic taxonomy that organises the results across the full `(σ_0, σ_1, σ_2)` spectral triad. The mobility law `M(ρ)` controls both the overall scales (via μ₁, N̂) and the qualitative focusing character (via `Q`). The GRF spectral moments control the spread of each class differently — σ_2 for ratio/trace/quadratic, σ_1 for Rayleigh, σ_0 and ξ_φ(r) for correlation. The motif filter provides a single dimensionless correction `η_f ≈ 1.25` (Rayleigh), a saddle-density shift (ratio, from −1.94 unfiltered to −1.88 filtered), and a half-rise compression `0.80 ± 0.05` (correlation).

**D6 — EIT-Extremal integration.** Error budget combining σ_1 intrinsic and σ_0/ℓ_R2 reconstruction channels; Fieller-type ratio distribution; engineering clearance target `σ_1/κ_M^det < 0.036` for 2σ falsification of `κ_E/κ_M < 0.1`. Seven falsifiable predictions E-P1 through E-P7.

---

## Closure

GR-SC 2.0 (rev. 2) consolidates seven kinematic-curvature memos plus one integration memo into a five-class taxonomy with one mobility-law diagnostic, two metric identities, one algebraic joint-distribution curve, one rigid two-point envelope, one spectral isoperimetric inequality, one engineering clearance target, and fourteen quantitative pooled-R2 predictions spanning the full `(σ_0, σ_1, σ_2)` spectral triad. The arc respects the `project_ed10_geometry_qft_scope` guardrails throughout: kinematic acoustic metric only, no Einstein equations, no Schwarzschild, no α. It extends ED-SC 2.0 from scalar field-space Hessian statistics to the full GR curvature dictionary, demonstrates that three distinct geometric ratios collapse onto r*, adds one bounded-ratio and one Rayleigh-class prediction as new independent falsifiers, adds a first two-point correlation-class invariant native to EIT apparatuses, and delivers a calibrated error budget for the live EIT-Extremal experiment. The mobility-law NEC constraint is the first structural selector at the level of `M(ρ)` itself, separating ED's default linear mobility (NEC-violating) from a class of NEC-safe alternatives. ED-SC 3.0 (correlation-length hinge architecture `L_ray / ξ_{R2}` plus spectral-triad plus filter geometry) is queued as the natural structural successor to ED-SC 2.0; GR-SC 1.7 and 1.8 are its prerequisites.
