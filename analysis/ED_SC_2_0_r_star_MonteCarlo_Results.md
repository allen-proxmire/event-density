# ED-SC 2.0 r*: Monte-Carlo Results (First Pass)

**Status.** First empirical pass on the workflow specified in
[`ED_SC_2_0_r_star_MonteCarlo_Workflow.md`](ED_SC_2_0_r_star_MonteCarlo_Workflow.md).
Result is a clean, honestly-null finding: at the normalized Scenario-D
couplings of the analytic chain (M₀ = P₀ = 1, P₃ = −1), the pre-registered
ED-SC 2.0 motif filter selects **zero** saddles out of populations of 10⁴ per
realisation, across the canonical noise level σ = 0.0556 *and* its
normalization-stretched variants up to σ = 1.0, across three strictness
levels of the filter. The underlying noisy-field saddle population itself
sits in a regime where κ⊥ ≈ 0.01–0.20 and χ < ½ — so the *entire
unfiltered* saddle distribution gives r* ≈ 0 to +0.1, not −1.304. The
target κ⊥ ≈ 1.04 is not a generic saddle property of the Scenario-D SPDE
at these couplings.

**Companion script.**
[`analysis/scripts/r_star_montecarlo.py`](scripts/r_star_montecarlo.py).
Diagnostic drivers: [`r_star_mc_sweep.py`](scripts/r_star_mc_sweep.py),
[`r_star_mc_nofilter.py`](scripts/r_star_mc_nofilter.py).

---

## 1. Numerical configuration

Grid 64 × 64, dx = 1, periodic; IMEX Euler with dt = 0.05; N_steps = 1200;
burn-in 300; snapshot every 25 steps; 5 realisations per config. Initial
condition δ ~ 0.3 + 0.4·U(0,1). Couplings M₀ = 1, M₂ = 0, P₀ = 1, P₃ = −1.

Stationary-point detection: 2×2 plaquette sign changes on central-difference
discrete gradient + bilinear Newton refinement (8 iterations, convergence
tol 1e−8). Spatial Hessian K from centred differences with periodic BCs.
Ordering: κ∥ = eigenvalue of larger |·|, κ⊥ = smaller |·|. Saddle
condition κ∥·κ⊥ < 0. Per-point r*_pt = −2χ/(2χ−1), χ = 2μκ⊥²/P₀, μ = M₀
(since M₂ = 0).

Pre-registered ED-SC 2.0 motif filter: δ_thr = 0.10, α = 0.25, L_ray = 2,
aspect ≥ 1.5, D₂ reflection-symmetry residual ≤ 0.20, orientation
tolerance ≤ 15° (major axis of α-contour connected component vs κ∥
eigenvector).

---

## 2. Pre-registered filter: zero motifs at all tested σ

Initial run at canonical σ = 0.0556 (10 realisations, N_steps = 2000):

| σ     | realisations | motifs (filter) | field std (final) |
|-------|--------------|------------------|-------------------|
| 0.0556 | 10          | 0                | 0.024             |

Because field std ≈ 0.024 ≪ δ_thr = 0.10, no stationary point ever clears
the amplitude gate. Extending σ:

Sweep `r_star_mc_sweep.py` — pre-registered filter (strict), σ ∈ {0.7, 1.0}:

| σ     | filter      | motifs | field std |
|-------|-------------|--------|-----------|
| 0.7   | strict      | 0      | 0.30      |
| 1.0   | strict      | 0      | 0.44      |

Relaxed filter sweep (from earlier diagnostic job): at σ = 1.0, rejection
breakdown of 444 saddle candidates (out of 1167 stationary points) was
dominated by the symmetry and aspect gates:

    amplitude: 109   (d_pt < δ_thr)
    alpha_mask_centre: 79
    cc_too_small: 8
    L_maj: 8
    aspect: 85
    sym: 155
    (orientation: 0  — never reached, all rejected upstream)

With the filter relaxed to (sym ≤ 0.40, aspect ≥ 1.3, orient ≤ 30°) and
(sym ≤ 0.60, aspect ≥ 1.2, orient ≤ 45°) at σ ∈ {1.0, 0.7}: still **0
motifs across all 5-realisation runs**. The D₂-symmetric ray constraint
on an α-contour connected component is simply incompatible with the
geometry of typical stationary points of a noisy ∇²δ = δ − δ³/6 field at
these couplings.

---

## 3. Underlying saddle population (amplitude-only + no filter)

To isolate what the filter *would* be selecting from, we drop the
anisotropy gates entirely and characterise the raw saddle population
(script `r_star_mc_nofilter.py`, 5 realisations per config):

| config                    | σ      | amp_thr | saddles total | field std |
|---------------------------|--------|---------|---------------|-----------|
| σ=0.0556, no amp          | 0.0556 | —       | 80,089         | 0.024     |
| σ=0.0556, amp≥0.01         | 0.0556 | 0.01    | 51,421         | 0.024     |
| σ=1.0, no amp              | 1.0    | —       | 79,438         | 0.43      |
| σ=1.0, amp≥0.10            | 1.0    | 0.10    | 63,554         | 0.43      |

**Pooled medians + IQR** (16k–16k saddles per realisation; per-realisation
medians tight to 1% so bootstrap CI collapses to point):

| config           | median \|κ⊥\| | IQR \|κ⊥\|        | median s | s IQR            | median r*_pt | r*_pt IQR           | median \|d_pt\| |
|------------------|----------------|-------------------|----------|------------------|---------------|----------------------|-----------------|
| σ=0.056, no amp  | 0.0110         | [0.0053, 0.0187]  | −2.77    | [−6.22, −1.61]   | +5.0e−4       | [1.1e−4, 1.4e−3]    | 0.0146          |
| σ=0.056, amp>.01 | 0.0109         | [0.0052, 0.0185]  | −2.79    | [−6.31, −1.62]   | +4.8e−4       | [1.1e−4, 1.4e−3]    | 0.0217          |
| σ=1.0, no amp    | 0.199          | [0.095, 0.338]    | −2.77    | [−6.23, −1.61]   | +0.111        | [0.014, 0.448]      | 0.267           |
| σ=1.0, amp>.10   | 0.198          | [0.095, 0.337]    | −2.78    | [−6.29, −1.61]   | +0.109        | [0.014, 0.445]      | 0.335           |

Bootstrap-95 CI over realisations for `κ⊥` and `r*` point-median:

- σ = 0.0556, no amp: κ⊥ ∈ [0.0109, 0.0111], r* ∈ [4.7e−4, 4.9e−4]
- σ = 1.0, no amp:    κ⊥ ∈ [0.196, 0.201],   r* ∈ [0.107, 0.112]

Per-realisation variance is tiny because each realisation contains ~16k
saddles — the population has very low per-realisation noise.

---

## 4. Comparison to analytic targets

| quantity    | target (ED-SC 2.0) | MC σ=0.0556      | MC σ=1.0         | gap            |
|-------------|---------------------|-------------------|-------------------|----------------|
| κ⊥          | ≈ 1.04              | 0.011             | 0.199             | ×100 / ×5.2    |
| s = κ∥/κ⊥   | −1.304 (or −1 lead) | −2.77             | −2.77             | off by ~2×     |
| χ = 2κ⊥²    | 2.145               | 2.4e−4            | 0.079             | ×10⁴ / ×27     |
| r*          | −1.304              | +5e−4             | +0.11             | wrong sign     |

The entire noisy-field saddle population lives in the **χ < ½ branch** of
the asymptotic `r* = −2χ/(2χ−1)`, where `r*` is small and positive. The
ED-SC 2.0 target −1.304 sits on the **χ > ½ branch** (χ = 2.145), which
requires κ⊥ ≳ 0.7 in these units — an order of magnitude larger than the
typical saddle. No noise level tested (from 0.0556 up to 1.0) produced
saddles with κ⊥ anywhere near the target band.

The median shape parameter `s ≈ −2.77` is also notable: it is neither the
nullcline closure value `s = −1` (Anisotropy memo leading order) nor the
ED-SC 2.0 reference `s = −1.304`. It is the characteristic shape of saddle
points of a linear-Ornstein-Uhlenbeck-like 2D Gaussian field — consistent
with the SPDE's linearised-around-zero regime at small σ.

---

## 5. Structural diagnosis

Three compatible readings of the null result, in order of how invasive
each is to the analytic chain:

### 5.1 Normalization mismatch (most benign)

The "canonical σ = 0.0556" in the ED-SC 2.0 reference comes from
ED-Arch-01's specific dimensional choice, not from the normalised
(M₀ = P₀ = |P₃| = 1) form used throughout the analytic chain. Converting
σ between the two normalizations requires knowing how ED-Arch-01 rescales
field amplitude, time, and length. If the "true" normalised σ is O(1)×
larger to produce δ_max near the natural amplitude √6, the κ⊥ target
would also correspond to a larger raw curvature.

**Evidence for:** the pure-PDE 2D radial bounce (SaddleSolve memo)
requires δ_max = 5.40 in these normalized units to get the deterministic
soliton. If the canonical target state sits near δ_max = √6 ≈ 2.45, that
is a ratio of ≈ 2.2 from the bounce amplitude and ~100 from the MC noisy-
field median |d_pt| = 0.27 at σ = 1.0.

**Implication:** a σ large enough to populate amplitudes near √6 would
almost certainly push the system into the stiff-curvature bounce regime
(the SaddleSolve r* → −1 limit) rather than the shallow κ⊥ = 1.04 band.
So normalization mismatch alone is not obviously enough to close the gap.

### 5.2 Filter incompatibility with isotropic fluctuations (structural)

The pre-registered filter requires a D₂-reflection-symmetric, aspect ≥
1.5, ray-like α-contour with major axis aligned to κ∥ within 15°. In a
homogeneous isotropic Gaussian random field, stationary points are
statistically isotropic; their α-contour shape distributions are not
peaked at aspect 1.5 with short axis along κ∥, so the intersection of all
the gates has near-zero probability. This is internally consistent with
the sweep data: rejection is dominated by the symmetry and aspect gates,
never by orientation (the orientation gate never fires because no
candidate survives to that point).

**Implication:** the ED-SC 2.0 motif is not a typical saddle of the
SPDE's stationary distribution. It is a rare, anisotropy-selected
sub-population whose existence requires some symmetry-breaking seed —
ray-injecting boundary data, localised forcing, or a non-stationary
relaxation from specific initial conditions. The pre-registered filter
assumes such a sub-population exists; at canonical couplings under pure
Gaussian bulk noise, it does not.

### 5.3 The ED-SC 2.0 reference is a simulator artefact (most invasive)

If the −1.304 figure originates from a specific ED-Arch-01 simulation
that includes (a) non-Gaussian initial conditions, (b) non-periodic
boundaries, (c) localised source injection, or (d) a deterministic
relaxation phase before measurement, then the value reflects those
specific off-SPDE ingredients rather than the SPDE's stationary
distribution. In that case the analytic chain correctly captures the
formal r*(κ⊥) mapping, but the κ⊥ ≈ 1.04 empirical scalar is set by
simulator details outside the Scenario-D PDE proper.

---

## 6. What this changes in the arc

- **Analytic chain** (Derivation → Extended → Local Geometry →
  Anisotropy → SaddleSolve): untouched. Closed-form
  `r* = −2χ/(2χ−1)`, `χ = 2μκ⊥²/P₀`, natural-amplitude `s = −1`, and
  deterministic bounce `r* → −1` remain correct.

- **Empirical closure** of κ⊥ at target ≈ 1.04 **does not come from the
  pure Scenario-D SPDE at these normalized couplings under the
  pre-registered motif filter**. The arc's "one remaining number" is not
  extractable from this setup; it requires a different data-generating
  process than the one specified.

- **Falsification call (from SaddleSolve memo):** "Expected value ≈ 1.04;
  falsification if it lands outside [0.97, 1.10]." At normalized σ = 1.0
  the actual value is κ⊥ = 0.20 ± 0.01 (over realisations), well outside
  the falsification band. **Formally this falsifies the prediction as
  stated**, but the honest reading is that the test does not discriminate
  between (a) the analytic prediction being wrong and (b) the sampling
  setup being wrong — see §5.

---

## 7. Next-step targets

1. **Normalization audit.** Reconstruct how ED-Arch-01's σ* = 0.0556 maps
   to the normalized (M₀ = P₀ = |P₃| = 1) form. If the ED-Arch-01 field
   amplitude is rescaled by a factor s, then κ⊥(normalized) = s · κ⊥(raw)
   and the 1.04 target refers to the ED-Arch-01-rescaled curvature. A
   factor s ≈ 5 would bring this MC data's σ = 1.0 result (κ⊥ = 0.20)
   into the target band.

2. **Source-injection MC.** Repeat the workflow with a localised Gaussian
   "ray" forcing term of width L_ray = 2 and amplitude tuned so that the
   induced saddle has δ_max ≈ √6 at long times. Measure κ⊥ of the
   induced saddle. This tests reading §5.2 (filter requires symmetry-
   broken seed).

3. **ED-Arch-01 re-analysis.** Pull κ⊥ directly from the canonical
   ED-Arch-01 motif-filtered snapshot distribution and compare to 1.04.
   If the number reproduces from that simulator's actual fields under
   the same filter, then the gap isolates specifically to the choice of
   bulk SPDE setup (our MC pipeline) vs. simulator setup (ED-Arch-01).

4. **Update ED-SC 2.0 canonical doc** to specify, if applicable, that
   the motif population is built under a specific seeding protocol —
   not as stationary-distribution saddles of the bare Scenario-D SPDE.

---

## 8. Closed result (update)

    ┌──────────────────────────────────────────────────────────────────┐
    │                                                                  │
    │  Analytic chain (unchanged):                                     │
    │                                                                  │
    │    r* = −2 χ / (2 χ − 1),   χ = 2 μ κ⊥² / P₀                     │
    │    target:  r* = −1.304 ⟺ χ = 2.145 ⟺ κ⊥ ≈ 1.04                 │
    │                                                                  │
    │  Monte-Carlo test (new):                                         │
    │                                                                  │
    │    pre-registered filter  →  0 motifs at σ ∈ {0.0556, 0.7, 1.0}  │
    │    raw saddle population  →  κ⊥_med = 0.011 (σ=0.0556)           │
    │                               κ⊥_med = 0.199 (σ=1.0)             │
    │                               s_med   ≈ −2.77                    │
    │                               r*_med  ≈ +0.0005 / +0.11          │
    │                                                                  │
    │  Falsification call in SaddleSolve §8:                           │
    │    κ⊥ expected ∈ [0.97, 1.10];  observed 0.011–0.20.             │
    │    → Prediction falsified for bare Scenario-D SPDE +             │
    │      pre-registered ED-SC 2.0 motif filter.                      │
    │                                                                  │
    │  Interpretation: the empirical scalar κ⊥ ≈ 1.04 does not arise   │
    │  as a typical saddle curvature under the canonical SPDE; it      │
    │  requires either (i) a different normalization dictionary, or    │
    │  (ii) a symmetry-broken seeding protocol, or (iii) reflects      │
    │  ED-Arch-01 simulator structure beyond the bare SPDE.            │
    │                                                                  │
    └──────────────────────────────────────────────────────────────────┘

---

## 9. Related memos

- `analysis/ED_SC_2_0_r_star_MonteCarlo_Workflow.md` — pre-registered workflow.
- `theory/ED_SC_2_0_r_star_SaddleSolve.md` — deterministic-bounce diagnostic
  + falsification band definition.
- `theory/ED_SC_2_0_r_star_Anisotropy.md` — closed-form asymptotic.
- `theory/ED_SC_2_0_r_star_Local_Geometry.md` — symbolic r* formula.
- `memory/project_ed_r_star_analytic_arc.md` — durable arc memory
  (to be updated with §5 structural diagnosis + §7 next-steps).
