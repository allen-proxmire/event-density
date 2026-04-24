# ED-SC 2.0 r*: Consolidation Memo

**Role.** Single point of reference for the state of the ED-SC 2.0 r*
program. Supersedes no prior memo — all nine remain authoritative for
their scope — but *consolidates* their findings into one status document.
Replace the arc-memory pointer here first when asking "what is r* right
now?"

**Sister memos** (in dependency order):

1. [`theory/ED_SC_2_0_r_star_Derivation_Attempt.md`](ED_SC_2_0_r_star_Derivation_Attempt.md) — 3-mode predecessor.
2. [`theory/ED_SC_2_0_r_star_Derivation_Extended.md`](ED_SC_2_0_r_star_Derivation_Extended.md) — 4-mode Hermite–Gauss, spatial-vs-field-space verdict.
3. [`theory/ED_SC_2_0_r_star_Local_Geometry.md`](ED_SC_2_0_r_star_Local_Geometry.md) — full 2D nonlinear saddle PDE + quasi-potential.
4. [`theory/ED_SC_2_0_r_star_Anisotropy.md`](ED_SC_2_0_r_star_Anisotropy.md) — Taylor-expansion closure r*(χ).
5. [`theory/ED_SC_2_0_r_star_SaddleSolve.md`](ED_SC_2_0_r_star_SaddleSolve.md) — deterministic 2D radial bounce.
6. [`analysis/ED_SC_2_0_r_star_MonteCarlo_Workflow.md`](../analysis/ED_SC_2_0_r_star_MonteCarlo_Workflow.md) — pre-registered MC spec.
7. [`analysis/ED_SC_2_0_r_star_MonteCarlo_Results.md`](../analysis/ED_SC_2_0_r_star_MonteCarlo_Results.md) — isotropic-MC null.
8. [`analysis/ED_SC_2_0_r_star_Normalization_Audit.md`](../analysis/ED_SC_2_0_r_star_Normalization_Audit.md) — R2-vs-analytic-chain PDE mismatch.
9. [`analysis/ED_SC_2_0_r_star_RayForcing_Design.md`](../analysis/ED_SC_2_0_r_star_RayForcing_Design.md) — symmetry-broken experiment design.
10. [`analysis/ED_SC_2_0_r_star_RayForcing_Results.md`](../analysis/ED_SC_2_0_r_star_RayForcing_Results.md) — symmetry-broken-MC null.

---

## 1. Executive summary

**What r* is.** The canonical ED-SC 2.0 invariant r* is the motif-
conditioned median of the spatial Hessian-eigenvalue ratio `κ∥/κ⊥` of
δ(x,y) at stationary points selected by the ray/D₂ motif filter. Target
value `r* = −1.304` from the ED-Arch-01 Scenario-D simulation.

**What was derived.** The analytic chain (Attempt → Extended → Local
Geometry → Anisotropy → SaddleSolve) is *closed at leading order*. It
produces a single-parameter closed form

    r* = − 2χ / (2χ − 1),    χ = 2 μ κ⊥² / P₀

with a theorem that the natural amplitude `δ_max² = −6P₀/P₃` forces the
shape parameter `s = κ∥/κ⊥ = −1` exactly at leading order. The target
r* = −1.304 matches at `χ = 2.145 ⟺ κ⊥ ≈ 1.04`. A variational
obstruction `G[δ] = ½ M₂ δ |∇δ|²` is made explicit for the M₂ correction;
at M₂ = 0 the chain is fully analytic. The derivation rests on a cubic-
bistable penalty (P₃δ³/6) and a quadratic mobility (M₀ + ½M₂δ²).

**What was tested.** Three Monte-Carlo pipelines run the analytic-chain
SPDE numerically: (i) isotropic noise with the pre-registered α-contour
D₂ motif filter; (ii) isotropic noise, no filter (raw saddle population);
(iii) quadrupolar forced-then-relaxed with the same filter plus a no-
filter variant. A reconstruction of the ED-Arch-01 ("R2") simulator was
also audited from `analysis/scripts/ed_arch_r2/`.

**What held.** The analytic mapping `r*(χ)` is valid under its premises;
the deterministic 2D bounce gives r* → −1 in the stiff-curvature limit,
as predicted; the s = −1 theorem at the cubic nullcline is reproduced
on-grid; the variational obstruction is locally explicit.

**What failed.** The identification of `r* = −1.304` with a leading-order
property of the bare Scenario-D SPDE is **empirically falsified**. The
pre-registered filter admits zero motifs across all tested σ and seeding
protocols; the raw saddle population and primary-region (ray-forced)
saddle population both sit in the χ < ½ branch with s ≈ −2.77, far from
the −1.304 target. The R2 reconstruction does reproduce −1.304 (N = 6,
median match) — but uses a *different PDE* (concave mobility + concave
penalty, not the cubic-bistable form the analytic chain Taylor-expands)
and a *different filter* (ray-endpoint threshold about p̂ ≈ 0.108, not
α-contour D₂ symmetry). Additionally the Workflow-memo filter has an
internal inconsistency (δ_thr=0.10 at a saddle whose generic d_pt ≈ 0),
traced to a mistranslation from the R2 baseline-subtracted form.

**Current status of r* = −1.304.** Reclassified from "leading-order
universal ED-SC 2.0 invariant" to **"regime- and simulator-dependent
invariant of the R2 concave-PDE + ray-endpoint-filter data-generating
process, under the specific Scenario-D parameter choice n* = 2.7,
σ* = 0.0556."** The analytic chain provides the *structural form* of r*
as a single-parameter function of motif curvature, but the *quantitative
value* −1.304 is not recovered from the chain's cubic-bistable truncation
under any tested sampling regime. Empirical closure of the chain requires
either (a) re-doing the analytic derivation on the R2 PDE, or (b)
accepting r*(χ) as a descriptive family rather than a predictive number.

---

## 2. Analytic chain (fixed; see memos 1–5 for derivations)

### 2.1 Derivation path

1. **PDE → saddle PDE** (Local Geometry §2). The full nonlinear 2D
   Scenario-D saddle equation
   `(M₀ + ½M₂δ²) ∇²δ + M₂ δ |∇δ|² − P₀ δ − (1/6) P₃ δ³ = 0`
   is the Euler–Lagrange condition for the instanton.
2. **Quasi-potential + variational obstruction** (Local Geometry §3).
   Drift differs from `−δΦ/δδ` by `G[δ] = ½ M₂ δ |∇δ|²`, so
   `Ψ = 2Φ + M₂ Ψ₁ + O(M₂²)` — the non-gradient correction is local.
3. **Local Hessian structure** (Local Geometry §4). Spatial Hessian
   `K_ij = ∂²δ/∂x_i∂x_j` at the saddle has eigenvalues κ∥, κ⊥; trace
   equation `μ(κ∥ + κ⊥) = P₀ δ + (1/6) P₃ δ³` where μ = M(δ_max).
4. **Anisotropy equation + s-closure** (Anisotropy §3).
   `12 μ (p − r) = (a − b) · [π − 6 M₂ d (a + b)]` reduces at the
   natural-amplitude closure `δ_max² = −6P₀/P₃` to `s = κ∥/κ⊥ = −1`
   exactly at leading order.
5. **Closed form** (Anisotropy §4). Inserting s = −1 into the symbolic
   r* formula (Local Geometry §5) gives

    ┌──────────────────────────────────────────────────────────────────┐
    │                                                                  │
    │    r* = − 2 χ / (2 χ − 1)                                       │
    │                                                                  │
    │       χ  = 2 μ κ⊥² / P₀                                         │
    │       μ  = M₀ + ½ M₂ δ_max²      (mobility at saddle)           │
    │       π  = P₀ + ½ P₃ δ_max²       (penalty slope)               │
    │       s  = κ∥ / κ⊥ = −1          (nullcline-closure leading)    │
    │       κ⊥ = spatial Hessian evalue of smaller |·|                │
    │       κ∥ = spatial Hessian evalue of larger |·|                 │
    │                                                                  │
    │    Target:  r* = −1.304 ⟺ χ = 2.145 ⟺ κ⊥ ≈ 1.04 (at M₂=0).    │
    │                                                                  │
    └──────────────────────────────────────────────────────────────────┘

### 2.2 Status of the chain

- Leading order (M₂ = 0): **analytically closed**. Single remaining
  empirical scalar is κ⊥.
- Full order (M₂ ≠ 0): reduces to a single 4D integral `𝒦_NL`
  (Local Geometry eq. 4.8). Not evaluated; not required for the
  leading-order result.

---

## 3. Deterministic diagnostics (SaddleSolve, memo 5)

### 3.1 2D radial bounce

The radial reduction `δ″ + δ′/r = δ − δ³/6` with `δ′(0)=0, δ(∞)=0` has
a critical shooting amplitude

    δ*_max = 5.40406639   (2D Coleman-like bounce)

Derived invariants:

| quantity      | value       |
|---------------|-------------|
| δ*_max        | 5.404       |
| κ_rad = κ∥=κ⊥ | −10.4496    |
| χ             | 218.39      |
| r* (radial)   | −1.00229    |

Pure-PDE bounce sits in the stiff-curvature asymptote `r* → −1` (χ → ∞).
**Not −1.304.** The ED-SC 2.0 target corresponds to κ⊥ an order of
magnitude shallower than the deterministic soliton.

### 3.2 Consequence

The ED-SC 2.0 reference is *not* the deterministic 2D instanton of the
analytic-chain PDE. Any quantitative match requires either the noisy-
field stationary distribution to select a shallower sub-population, or
the underlying PDE to differ from the cubic-bistable form. §4 resolves
which.

---

## 4. Stochastic diagnostics (MonteCarlo + RayForcing; memos 6–10)

### 4.1 Isotropic MC + pre-registered filter (memo 7)

64×64 periodic, IMEX Euler, dt = 0.05, 10 realisations at σ = 0.0556
(canonical) and a σ-sweep to 1.0; filter as specified in Workflow §3.

**Result:** 0 motifs at all σ and all filter-strictness levels tested.
Rejection breakdown (σ=1.0 diagnostic): sym_err 155 / aspect 85 /
amplitude 109 of 444 saddle candidates; orientation gate never reached.

### 4.2 Isotropic MC, no filter (memo 7, §3 supplementary)

Raw saddle population, ~16k saddles per realisation, pooled medians
tight to 1%:

| σ      | \|κ⊥\|_med | s_med  | r*_med  |
|--------|-----------|--------|---------|
| 0.0556 | 0.011     | −2.77  | +5e−4   |
| 1.0    | 0.199     | −2.77  | +0.11   |

All χ < ½; r* small and positive; s far from −1.3 and from −1.

### 4.3 Normalization audit (memo 8)

Reconstructed the ED-Arch-01 simulator pipeline from
`analysis/scripts/ed_arch_r2/`. Key finding: ED-Arch-01 integrates

    p_{t+1} = p + dt·[ ∇·(M(p) ∇p) − α p^γ + σ η ],
              M(p) = ((1 − p) / 1.0)^{2.7},
              α = 0.03, γ = 0.5, σ = 0.0556.

This is **not** the cubic-bistable SPDE of the analytic chain. The
mobility is concave-saturating; the penalty is concave square-root.
Analytic-chain Taylor expansion about the stationary mean `p̂ ≈ 0.108`
gives a linear + *quadratic* penalty series, not linear + cubic. The
chain's cubic truncation is structurally incorrect for R2, and the
target κ⊥ ≈ 1.04 is a dimensional artefact of the cubic closure that
has no direct R2 analogue.

Additionally, the R2 motif filter (ray-endpoint thresholds relative to
`p̂ ± α_filt·std(p)`) is **not** the Workflow memo's α-contour D₂ filter.
R2 filter admits N = 6 saddles at canonical σ* with median `λ₁/λ₂ = −1.304`
(exact target match). Workflow filter admits 0 on the same pre-processed
field conceptually.

χ and r* are normalization-invariant; dimensional rescaling cannot close
the gap (Audit §1.5).

### 4.4 Ray-forced MC (memo 10)

**Design amendment:** Gaussian-ridge forcing creates a peak (positive-
definite Hessian), not a saddle — filter rejects by construction.
Implementation uses quadrupolar forcing `F = A(x̃²/σ_x² − ỹ²/σ_y²)
exp(−r̃²/2σ²)` instead, which seeds an exact Morse saddle at origin.

**Pre-registered filter (3 seeds tested):** 0 motifs. Filter rejects at
the δ_thr gate because the quadrupole-seeded saddle has d_pt ≈ 0 at the
centre; this flags an **internal inconsistency in the Workflow filter**
— the R2 source uses ray-endpoint thresholds relative to the field mean,
which the Workflow memo translated to saddle-amplitude thresholds that
drop the baseline subtraction.

**No-filter supplementary (5 seeds × 3 σ):**

| σ    | primary \|κ⊥\|_med | s_med  | r*_med  | χ_med  |
|------|---------------------|--------|---------|--------|
| 0.05 | 0.011              | −2.69  | +4e−4   | 0.0002 |
| 0.20 | 0.042              | −2.69  | +7e−3   | 0.0035 |
| 0.40 | 0.083              | −2.75  | +3e−2   | 0.014  |

All three σ values: primary-region saddle statistics are
**indistinguishable from the isotropic-MC population** at matched σ. The
seeded deterministic motif decays within the T_burn = 100 post-forcing
window (decay time τ ≈ 1/P₀ = 1 ≪ sampling window duration 35 in
physical units), so the sampled saddles are pure noise-induced.

**All three r* branches are in χ < ½**; none crosses into the χ > ½
branch where r* becomes negative, let alone near −1.304.

### 4.5 Triple-null summary

| population                              | \|κ⊥\|_med | s_med  | r*_med  | χ_med  | branch     |
|-----------------------------------------|-----------|--------|---------|--------|------------|
| ED-SC 2.0 target                        | 1.04      | −1.30  | −1.304  | 2.145  | χ > ½       |
| Deterministic 2D bounce                  | 10.45     | +1.00  | −1.00   | 218    | χ ≫ ½      |
| Isotropic MC, σ=0.0556                   | 0.011     | −2.77  | +5e−4   | 2e−4   | χ ≪ ½      |
| Isotropic MC, σ=1.0                      | 0.199     | −2.77  | +0.11   | 0.08   | χ < ½       |
| Ray-forced primary, σ=0.05               | 0.011     | −2.69  | +4e−4   | 2e−4   | χ ≪ ½      |
| Ray-forced primary, σ=0.40               | 0.083     | −2.75  | +3e−2   | 0.014  | χ ≪ ½      |
| R2 canonical reproduction                | n/a       | −1.304 | −1.304  | n/a    | target     |

---

## 5. Interpretation

### 5.1 Structurally solid

- **Analytic mapping `r*(χ)` at leading order.** `r* = −2χ/(2χ−1)` with
  `χ = 2μκ⊥²/P₀` is correctly derived from the Scenario-D saddle PDE
  under cubic-bistable penalty; it is a theorem of that PDE. No MC
  result invalidates the formula; they invalidate only its application
  to the bare-SPDE stationary distribution.
- **Natural-amplitude closure `s = −1` at leading order.** A theorem
  at the cubic nullcline `δ_max² = −6P₀/P₃`; independent of M₀, M₂;
  independent of noise.
- **Variational obstruction `G[δ] = ½M₂δ|∇δ|²`.** Exact and local.
  ED is non-gradient; the obstruction is a single scalar per instanton
  trajectory (`𝒦_NL`).
- **Deterministic 2D bounce is in the stiff-curvature asymptote.** The
  pure-PDE bounce gives r* → −1 and is not the ED-SC 2.0 motif; this
  is a clean quantitative result and a useful anchor.
- **Spatial-not-field-space Hessian reading (F1 in arc memory).** The
  Extended memo's verdict stands: ED-SC 2.0 r* is `K(x)` spatial, not
  `H(Ψ)` field-space. This is unchanged.

### 5.2 Empirically falsified as stated

- **"κ⊥ ≈ 1.04 is a typical saddle curvature of the bare analytic-chain
  Scenario-D SPDE."** False at every σ from 0.05 to 1.0 and under both
  isotropic and ray-forced sampling. Observed values are 0.01 to 0.20 —
  an order of magnitude or more below target.
- **"The pre-registered D₂ motif filter admits the ED-SC 2.0 motif
  population in the bare SPDE."** False: 0 motifs, traced to both
  filter mis-specification (§5.2 of RayForcing_Results: δ_thr=0.10
  applied at saddle point in a zero-mean field) and PDE mismatch.
- **"Symmetry-broken seeding recovers the target by nonlinear self-
  sustainment."** False: the cubic penalty has decay time τ ≈ 1 ≪
  sampling window, so the seeded motif fully decays before sampling.
- **SaddleSolve §8 falsification call:** `κ⊥ expected ∈ [0.97, 1.10]`;
  observed 0.011–0.20. Band missed by a factor of 5–100. The call
  is formally falsified; honest reading is in §5.3 below.

### 5.3 Simulator- and protocol-dependent

The Normalization Audit (§2.4) and RayForcing Results (§5.1) converge
on a single structural diagnosis:

**r* = −1.304 is a property of the R2 (ED-Arch-01) data-generating
process**, which consists of:

1. A concave-saturating mobility `M(p) = ((1−p)/1)^{2.7}`.
2. A concave square-root penalty `α p^{0.5}`, α = 0.03.
3. White noise at σ = 0.0556 applied from `t = 0` without pre-
   relaxation.
4. Uniform initial condition `p₀ ~ U(0.3, 0.7)`, periodic BCs, 64×64
   grid, dt = 0.05, 500 steps.
5. A ray-endpoint motif filter with thresholds relative to the
   stationary mean `p̂ ≈ 0.108` and spread `std(p) ≈ 0.015`; α_filt = 0.25;
   L_ray = 2; degeneracy cut at |λ_min|/|λ_max| < 0.10.

Under this pipeline (reproduction in `analysis/scripts/ed_arch_r2/`,
canonical memo `R2_Motif_Verdict.md`): N = 6 admitted motifs, median
eigenvalue ratio = −1.304, IQR [−1.94, −1.21].

**None** of the five ingredients above coincides with the cubic-
bistable + α-contour-D₂ setup of the analytic chain + Workflow memo.

### 5.4 Classification of r* = −1.304

**Recommended reading (this memo):**

- *Not* a universal ED-SC 2.0 invariant independent of simulator
  details.
- *A regime-dependent invariant* of the R2 simulator at the architectural
  saddle peak `(n* = 2.7, σ* = 0.0556)` under the ray-endpoint filter.
- *Provisional* until one of:
  - (a) the analytic chain is re-derived on the R2 PDE (concave M,
    concave penalty) and shown to yield −1.304 at its natural
    closure, or
  - (b) the R2 value is shown to be stable under parameter variation
    — tested in `R2_Motif_Verdict.md` at the (n*, σ*) peak but not
    across a wider parameter map.

The analytic chain's r*(χ) formula remains valid as a **structural
form**: under its premises, the ratio is a single-scalar function of a
single motif curvature. That is the genuine analytic content.

---

## 6. Status + next steps

### 6.1 Status box

    ┌──────────────────────────────────────────────────────────────────┐
    │                                                                  │
    │   ED-SC 2.0 r* Program — Status (this memo, 2026-04-22)          │
    │                                                                  │
    │   Analytic chain (cubic-bistable SPDE):           CLOSED         │
    │     r*(χ) = −2χ/(2χ−1),  χ = 2μκ⊥²/P₀                           │
    │     s = −1 leading order, natural-amplitude closure              │
    │     variational obstruction G[δ] = ½M₂δ|∇δ|² explicit            │
    │                                                                  │
    │   Deterministic 2D bounce diagnostic:             CONSISTENT     │
    │     δ*_max = 5.40, κ_rad = −10.45, r* = −1.00                   │
    │     (stiff-curvature asymptote, as predicted)                    │
    │                                                                  │
    │   Bare-SPDE stationary-distribution test:         FAILED         │
    │     pre-registered filter admits 0 motifs at all σ               │
    │     raw saddle pop: κ⊥ ~ 0.01–0.20, s ≈ −2.77, r* > 0             │
    │                                                                  │
    │   Ray-forced / symmetry-broken seeding test:      FAILED         │
    │     quadrupole seed decays before sampling;                      │
    │     primary-region saddles match isotropic baseline              │
    │                                                                  │
    │   R2 reconstruction (concave-PDE + ray-endpoint):  MATCHES       │
    │     N = 6 motifs, median eigenvalue ratio = −1.304               │
    │     (canonical ED-Arch-01 reproduction)                          │
    │                                                                  │
    │   r* = −1.304 classification:                                    │
    │     REGIME-DEPENDENT invariant of the R2 simulator               │
    │     (not universal across SPDE choices or filter forms)           │
    │                                                                  │
    │   Motif-filter specification (Workflow memo §3):   BUG FLAGGED   │
    │     δ_thr = 0.10 applied at saddle-point amplitude               │
    │     mistranslates R2's ray-endpoint-relative-to-p̂ test;          │
    │     needs baseline-subtracted re-specification                   │
    │                                                                  │
    └──────────────────────────────────────────────────────────────────┘

### 6.2 Next steps (3–5, in priority order)

**S1. R2-form MC port + reproduction (highest priority).**
Port the ED-Arch-01 SPDE (concave mobility + concave penalty) and the
R2 ray-endpoint filter into the MC pipeline. Run at canonical `(n*, σ*)`
and reproduce N = 6 motifs with median `λ₁/λ₂ = −1.304` on an
independent implementation. This locks in the target as reproducible
outside `analysis/scripts/ed_arch_r2/`. Budget: ~1 day.

**S2. R2-form analytic closure.**
Redo the Anisotropy memo's Taylor expansion with concave mobility +
concave penalty about `p̂ ≈ 0.108` instead of cubic-bistable about δ = 0.
Derive the analogue of `r* = −2χ/(2χ−1)` with its own natural-amplitude
closure. Targeted outcome: a closed form `r* = f(χ_R2)` where χ_R2
collapses to a quantitative target consistent with R2's −1.304. If the
closure succeeds, the arc is analytically closed end-to-end on the
actual ED-Arch-01 PDE. Budget: 2–3 days.

**S3. Parameter-map stability of R2 r*.**
Sweep (n, σ) around the canonical peak and measure how the motif-
median ratio varies. Tests whether −1.304 is locally stable, a knife-
edge, or part of a continuous family. A ~1% plateau over a finite (n, σ)
region would support "regime-dependent invariant"; steep variation
would demote the target to a point estimate. Budget: 0.5 day.

**S4. Motif-filter re-specification.**
Rewrite the Workflow memo's §3 filter to match the R2 ray-endpoint form
(ray-endpoint amplitudes relative to `p̂ ± α_filt·std(p)`, not saddle-
point amplitude relative to δ_thr). Re-run MC tests under the corrected
filter to check whether the filter-specification bug, independent of
the PDE mismatch, was contributing to the zero-motif null. Budget:
0.5 day.

**S5. ED-SC 2.0 canonical-doc clarification.**
Amend `docs/ED-SC-2.0.md` §1.4 to specify (a) spatial Hessian K(x) not
field-space H(Ψ) (already flagged in arc-memory F1), and (b) that r* is
an invariant of the specific ED-Arch-01 data-generating process and
ray-endpoint-filter baseline, not a universal constant of Scenario-D
PDE solutions at any parameter choice. Prevents definitional drift in
future sessions. Budget: 1 hour.

### 6.3 Optional follow-ups

- **Reversible / QM-sector r\*.** Extend the Local Geometry quasi-
  potential construction to the reversible (M₂ = 0, with gradient-flow
  limit) sector and check whether a non-trivial r* exists there or
  whether the invariant is specific to the irreversible, non-gradient
  ED flow. Would clarify whether r* is a non-equilibrium phenomenon
  fundamentally.
- **𝒦_NL closure.** Evaluate the 4D integral for the M₂ correction
  (Local Geometry eq. 4.8) along the deterministic instanton. Shifts
  the leading-order r* by a computable second-decimal amount; currently
  unevaluated, not required for the structural form.

---

## 7. Arc-memory update (recommended)

The durable memory `memory/project_ed_r_star_analytic_arc.md` should be
updated to:

- Add **F5: the analytic-chain cubic-bistable SPDE is not the ED-Arch-01
  PDE.** ED-Arch-01 integrates concave mobility `((1−p)/1)^{2.7}` and
  concave penalty `0.03 p^{0.5}`. The cubic truncation is a structural
  mismatch, not just a Taylor-series error.
- Add **G6: Do not treat κ⊥ ≈ 1.04 as a universal empirical target.**
  It is a dimensional artefact of the cubic-nullcline closure; under
  R2's concave penalty there is no cubic nullcline and κ⊥ ≈ 1.04 has
  no direct meaning.
- Add **G7: Do not interpret "r* = −1.304" as a leading-order analytic
  output.** It is the R2 simulator's motif-filtered median
  eigenvalue ratio at `(n*, σ*) = (2.7, 0.0556)`; the analytic chain
  supplies its *structural form* (single-scalar χ-dependence), not
  its numerical value.
- Point to this memo as the single arc summary.

---

## 8. Bottom line

The ED-SC 2.0 r* program delivered more than it was sold to deliver and
less than it was hoped to. It produced:

- A genuine leading-order analytic closure `r* = −2χ/(2χ−1)` derived
  from first principles on a cubic-bistable SPDE.
- A clean theorem (`s = −1` at natural amplitude) that generalises to
  any cubic-nullcline closure.
- A deterministic 2D bounce diagnostic locating the stiff-curvature
  asymptote at r* → −1.
- Three null Monte-Carlo tests, all honestly reported, that rule out
  reading −1.304 as a typical saddle of the analytic chain's SPDE.
- A clean reconstruction of the R2 simulator showing where −1.304
  actually lives: a different PDE, a different filter, a specific
  parameter point.

The arc's closure is structural, not numerical. Treating that honestly
is the deliverable. Future work either ports the chain onto the R2
PDE (S2 above) or accepts r* as a descriptive scalar of the
Scenario-D family rather than a predicted constant.
