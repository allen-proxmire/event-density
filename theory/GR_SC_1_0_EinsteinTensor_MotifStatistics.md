# GR-SC 1.0 — Einstein-Tensor Motif Statistics on the ED Acoustic Metric

**Date.** 2026-04-23.
**Scope.** Working memo. Paired with `theory/GR_SC_1_6_WeylTensor_MotifStatistics.md`. Computes the motif-conditioned distribution of invariants of the Einstein tensor `G_μν = R_μν − ½ g_μν R` evaluated on the kinematic ED acoustic metric `g^{eff}[ρ_0] = diag(−N²(x), 1, 1)` with `N = √M(ρ_0)`, linearised around a uniform background `ρ̂` and treating `φ = ρ_0 − ρ̂` as the 2D isotropic GRF from the r* and GR-SC 1.1 arcs.
**Status.** Concrete calculation. Three durable structural results: **(A) `G_00 = 0` identically on any static ultrastatic acoustic metric `diag(−N²(x⃗), δ_{ij})` in any spatial dimension** — a kinematic identity independent of `ρ_0`; **(B) the spatial-block eigenvalue ratio `G_∥^{(ij)}/G_⊥^{(ij)}` is distributionally equal to r***, mobility-universal (the `μ₁` prefactor cancels); **(C) the trace `tr(G^{(ij)})` is Gaussian at GRF saddles with zero median and variance set by a single spectral moment**.

**Scope guardrails.** Kinematic only. No Einstein equations, no ADM, no source terms. What is computed is the *structure* of `G_μν[g^{eff}]` as a functional of `ρ_0`, and its *statistics* under the ED GRF ensemble.

---

## 1. Setup

### 1.1 Metric and Ricci

From `theory/ED_Effective_Acoustic_Metric.md §2B` and `theory/GR_SC_1_1_Raychaudhuri_MotifStatistics.md §1`:

$$
g^{\rm eff}_{\mu\nu} = \mathrm{diag}(-N^2(x), 1, 1),\qquad N(x) = \sqrt{M(\rho_0(x))}.
$$

Ricci tensor and scalar (2+1D, static, flat spatial section):

$$
R_{00} = N\nabla^2 N,\qquad R_{ij} = -\frac{N_{,ij}}{N},\qquad R_{0i} = 0,\qquad
R = -\frac{2\,\nabla^2 N}{N}.
$$

### 1.2 Einstein tensor — exact components

$$
G_{\mu\nu} \equiv R_{\mu\nu} - \tfrac{1}{2}\,g_{\mu\nu}\,R.
$$

**Time-time component.**
$$
G_{00} = R_{00} - \tfrac{1}{2}g_{00}R = N\nabla^2 N - \tfrac{1}{2}(-N^2)\left(-\frac{2\nabla^2 N}{N}\right) = N\nabla^2 N - N\nabla^2 N = 0.
$$

$$
\boxed{\;\; G_{00} \;=\; 0 \quad\text{identically, any } N(x⃗), \text{any spatial dimension.} \;\;}
$$

This follows directly from the Ricci identity `R_{00} = −(1/2)g_{00}R` for static ultrastatic metrics with flat spatial sections. It is independent of `ρ_0` — a purely kinematic fact about the acoustic-metric *form*.

**Mixed component.** `G_{0i} = R_{0i} − ½ g_{0i} R = 0` (both terms vanish: `R_{0i} = 0`, `g_{0i} = 0`).

**Spatial block.**
$$
G_{ij} = R_{ij} - \tfrac{1}{2}\delta_{ij}\,R = -\frac{N_{,ij}}{N} + \delta_{ij}\,\frac{\nabla^2 N}{N}.
$$

Equivalently, with `(H_N)_{ij} = N_{,ij}`:

$$
\boxed{\;\; G_{ij} = \frac{1}{N}\bigl[\delta_{ij}\,\mathrm{tr}(H_N) - (H_N)_{ij}\bigr] \;\;}
$$

In the eigenbasis of `H_N` (eigenvalues `ℓ_1, ℓ_2`):

$$
G^{(\text{eig})} = \frac{1}{N}\,\mathrm{diag}(\ell_2,\ \ell_1).
$$

**Key observation.** The spatial block of `G` has the **same eigenvalue set** as `H_N`, but the eigenvalues are **assigned to the other spatial axis**: `G_{11} = ℓ_2/N`, `G_{22} = ℓ_1/N`. The spectrum is preserved; the labelling is swapped.

### 1.3 Invariants of the Einstein tensor

In 2+1D, a symmetric tensor with vanishing 0-row has four independent components (three spatial). Natural scalar invariants:

| Invariant | Formula |
| --- | --- |
| `tr(G^{ij})` | `δ^{ij} G_{ij} = \mathrm{tr}(H_N)/N = \nabla^2 N / N` |
| `\det(G^{ij})` | `\ell_1 \ell_2 / N^2 = \det(H_N)/N^2` |
| Signed eigenvalue ratio `\mathcal{R}_G = G_\|^{(ij)}/G_\perp^{(ij)}` | (defined via ED-SC 2.0 ordering) |
| Full trace `G^μ_μ` | `g^{μν}G_{μν} = g^{ij}G_{ij} = \mathrm{tr}(H_N)/N = -R/2` |

`G^μ_μ = −R/2` in 2+1D (standard identity `G^μ_μ = (1 − D/2)R`). The full and spatial traces coincide because `G_{00} = 0`.

---

## 2. Linearisation around `ρ̂`

Let `ρ_0(x) = ρ̂ + φ(x)` with `φ` a zero-mean 2D isotropic GRF. From GR-SC 1.1 §3:

$$
N = \hat N + \hat N'\varphi + O(\varphi^2),\qquad \hat N'/\hat N = \mu_1 = \tfrac{1}{2}\,M'(\hat\rho)/M(\hat\rho).
$$

At a critical point of `φ` (so `∇φ = 0`):

$$
(H_N)_{ij} = \hat N'\,(H_\varphi)_{ij} + O(\varphi^2),\qquad \nabla^2 N = \hat N'\,\nabla^2\varphi + O(\varphi^2).
$$

### 2.1 Linearised Einstein-tensor spatial block

$$
G_{ij}^{\rm lin} = \frac{\hat N'}{\hat N}\,\bigl[\delta_{ij}\,\mathrm{tr}(H_\varphi) - (H_\varphi)_{ij}\bigr]
= \mu_1\,\bigl[\delta_{ij}\,\mathrm{tr}(H_\varphi) - (H_\varphi)_{ij}\bigr].
$$

In the eigenbasis of `H_φ` with eigenvalues `(λ_1, λ_2)`:

$$
G^{\rm lin,\,(\text{eig})}_{ij} = \mu_1\,\mathrm{diag}(\lambda_2,\ \lambda_1).
$$

$$
\boxed{\;\;
G_{\rm spatial}^{\rm lin}\text{ eigenvalues} = \mu_1\cdot(\lambda_2,\ \lambda_1),\qquad
\mathrm{tr}(G^{\rm lin,\,ij}) = \mu_1\cdot(\lambda_1+\lambda_2),\qquad
\det(G^{\rm lin,\,ij}) = \mu_1^2\,\lambda_1\lambda_2.
\;\;}
$$

### 2.2 R2 canonical values

`M(p) = (1-p)^{2.7}, p̂ = 0.108`:

$$
\hat N = 0.857,\qquad \mu_1 = -1.513,\qquad \mu_1^2 = 2.289.
$$

---

## 3. GRF statistics at φ-saddles

Import from `theory/ED_SC_2_0_r_star_R2_GRF.md §2` and `GR_SC_1_1_Raychaudhuri_MotifStatistics.md §4`:

Saddle joint density (with `a = λ_1 > 0, b = −λ_2 > 0`):

$$
f_{\rm sad}(a, b) \propto ab(a+b)\exp\!\left[-\frac{3a^2+2ab+3b^2}{2\sigma_2^2}\right].
$$

In `(s, u) = ((a+b)/2, (a-b)/2)`:

$$
f_{\rm sad}(s, u) \propto s(s^2-u^2)\exp\!\left[-\frac{4s^2+2u^2}{\sigma_2^2}\right],\qquad s > 0,\ |u| < s.
$$

**Closed-form spectral moments at saddles** (derived via analytic integration of the marginals, cross-checked by MC at 5·10⁵ samples, §A below):

| Moment | Value | Check |
| --- | --- | --- |
| `⟨u²⟩_{sad}` | `σ_2² / 12` | analytic (f(u) Gaussian after s-integration) |
| `⟨s²⟩_{sad}` | `7\sigma_2² / 12` | numerical (confirmed `0.5833 σ_2²` to 4 sig fig) |
| `⟨ab⟩_{sad} = ⟨s²-u²⟩` | `σ_2² / 2` | `(7-1)/12` |
| `⟨a²+b²⟩_{sad} = 2⟨s²+u²⟩` | `4σ_2²/3` | `(7+1)/12 · 2` |
| `⟨tr(H_φ)²⟩_{sad} = 4⟨u²⟩` | `σ_2² / 3` | |
| `⟨(\lambda_1-\lambda_2)²⟩_{sad} = 4⟨s²⟩` | `7σ_2² / 3` | |

The key identity `⟨ab⟩_{sad} = σ_2²/2` (equivalently `⟨|det H_φ|⟩_{sad} = σ_2²/2`) is the Rice/Adler formula for the determinant density at 2D GRF saddles.

---

## 4. Distributions of Einstein-tensor invariants

### 4.1 `G_00`: degenerate distribution

`G_00 = 0` exactly. Distribution is a delta at 0, independent of motif filter, independent of `ρ_0`.

**Structural statement.** Any observation of `G_00 ≠ 0` on the acoustic metric would mean one of: (i) the metric is not static (background flow `v_0 ≠ 0`); (ii) the spatial section is not flat (ED does not provide this); (iii) the kinematic-acoustic-metric construction itself is being abandoned.

### 4.2 `tr(G^{ij})`: Gaussian zero-median

Linearised: `tr(G^{ij}) = μ₁·tr(H_φ) = μ₁·(λ_1 + λ_2) = 2μ₁·u`.

At GRF saddles, `u` is Gaussian with variance `σ_2²/12` (§3). Therefore:

$$
\mathrm{tr}(G^{ij})_{\rm sad} \sim \mathcal{N}\!\left(0,\ \frac{\mu_1^2\,\sigma_2^2}{3}\right).
$$

$$
\boxed{\;\;
\mathrm{med}\bigl(\mathrm{tr}(G^{ij})\bigr) = 0,\qquad
\mathrm{std}\bigl(\mathrm{tr}(G^{ij})\bigr) = \frac{|\mu_1|\sigma_2}{\sqrt{3}}.
\;\;}
$$

**R2 canonical.** `std = 1.513·0.0898/√3 ≈ 0.0784`.  `med(|tr(G^{ij})|) = 0.6745·std ≈ 0.0529`.

The zero-median is exact under `a ↔ b` (hence `u ↔ −u`) symmetry of `f_{sad}`. The canonical motif filter also respects this symmetry (it depends only on `ρ = max(a/b, b/a)`), so the filtered median is also exactly zero:

$$
\mathrm{med}\bigl(\mathrm{tr}(G^{ij})\mid\text{filter}\bigr) = 0\quad\text{exactly}.
$$

Equivalent statement: `tr(G^{ij}) = −R/2` in 2+1D, so the Ricci scalar `R` also has zero motif-conditioned median.

### 4.3 Spatial-eigenvalue ratio `ℛ_G` — r*-copy, mobility-universal

By §2.1, the spatial block of `G^{lin}` has eigenvalues `(μ_1 λ_2, μ_1 λ_1)`. These are the eigenvalues of `μ_1·H_φ` with the *labelling* (to spatial axes) swapped. For scalar invariants, the labelling is irrelevant — only the *set* of eigenvalues matters.

Under the ED-SC 2.0 convention (`|κ_∥| ≥ |κ_⊥|`, signs preserved):

$$
\mathcal{R}_G \equiv \frac{G_\|^{\rm eig}}{G_\perp^{\rm eig}}
= \frac{\mu_1\cdot(\text{larger-}|\cdot|\text{ eigenvalue of }H_\varphi)}{\mu_1\cdot(\text{smaller-}|\cdot|\text{ eigenvalue of }H_\varphi)}
= \frac{\kappa_\|}{\kappa_\perp} = r^*.
$$

The `μ_1` prefactor cancels — `ℛ_G` is **mobility-universal** (independent of `M(ρ)` as long as `μ_1 ≠ 0`).

$$
\boxed{\;\;
\mathcal{R}_G\;\stackrel{\rm d}{=}\;r^*.
\;\;}
$$

**Motif-conditioned prediction** (pooled 10-seed R2, canonical filter, from `ED_SC_2_0_r_star_Final_Verdict.md`):

$$
\mathrm{med}(\mathcal{R}_G\mid\text{filter}) = -1.88 \pm 0.40\quad\text{(95% CI)},\qquad
\mathrm{med}(\mathcal{R}_G)_{\rm unfiltered} = -1.94.
$$

Note the structural identity: `ℛ_Ray` (GR-SC 1.1) `= ℛ_G` (GR-SC 1.0) `= r*` (ED-SC 2.0) all coincide in distribution under motif conditioning. This is not three independent invariants — it is one invariant viewed through three tensor contractions.

### 4.4 `\det(G^{ij})` — definite-sign scalar

`det(G^{lin,ij}) = μ_1² \lambda_1 \lambda_2 = −μ_1²·ab` (at saddle, `λ_1 λ_2 = −ab < 0`).

So `det(G^{ij})` is **always negative at φ-saddles**, sign-definite.

$$
\mathrm{mean}(\det G^{ij})_{\rm sad} = -\mu_1^2\,\langle ab\rangle_{\rm sad} = -\frac{\mu_1^2\,\sigma_2^2}{2}.
$$

$$
\mathrm{med}(\det G^{ij})_{\rm sad} = -\mu_1^2 \cdot \mathrm{med}(ab)_{\rm sad} \approx -0.420\,\mu_1^2\,\sigma_2^2\quad(\text{MC, N=5e5, §A}).
$$

**R2 canonical numerical.** `mean ≈ −0.00924`, `median ≈ −0.00776` (in dimensionless `σ_2`-scaled units).

The filter (ray-endpoint) preferentially admits near-isotropic saddles, which have small `|s-u|·|s+u| = ab` when `|s|` is small and `|u| ≈ 0`... actually the filter biases `a/b → 1`, which for fixed geometric scale `s` maximises `ab = s² − u²`. So the filter **increases** typical `|det G^{ij}|` — by a factor of order the filter-induced compression of `|u|/s` (numerical `~30%` increase at canonical filter parameters).

### 4.5 Summary table

| Invariant | Sad. distribution | Median | Filter-effect on median | Mobility-dependence |
| --- | --- | --- | --- | --- |
| `G_{00}` | δ(0) | 0 | none | none |
| `G_{0i}` | δ(0) | 0 | none | none |
| `tr(G^{ij})` | Gaussian(0, μ₁²σ_2²/3) | 0 | 0 exactly | via `\|\mu_1\|` scale |
| `\det(G^{ij})` | sign-definite negative | `≈ −0.42 μ₁²σ_2²` | `↑\|·\|` | via `\mu_1^2` scale |
| `\mathcal{R}_G` ratio | `= r^*` | `−1.88 ± 0.4` | same as r* filter-shift | **mobility-universal** |

---

## 5. Falsifiable predictions (R2 pipeline)

1. **`G_{00}` vanishes identically at every R2 grid point.** Computing `G_{00}[g^{eff}[ρ_0]]` from numerically-finite-differenced `N = √M(ρ_0)` and its derivatives should yield values consistent with finite-difference round-off, not a statistically distinguishable distribution. A non-zero systematic would indicate the acoustic-metric construction is being applied to a configuration where the staticity assumption is broken (e.g., `v_0 ≠ 0` states).

2. **`tr(G^{ij})` has zero median at motif-conditioned saddles.** Equivalently, the Ricci scalar `R = −2·tr(G^{ij})` has zero motif-conditioned median. Testable on the canonical R2 motif population; a systematic non-zero would indicate GRF isotropy-breaking.

3. **`ℛ_G` reproduces the r* distribution exactly.** Computing the signed spatial-eigenvalue ratio of `G_{ij}[g^{eff}]` at motif-conditioned saddles should return `−1.88 ± 0.4` (10-seed pooled). A discrepancy would indicate linearisation breakdown (quadratic `φ²` corrections in `H_N` becoming non-negligible).

4. **`det(G^{ij})` is always negative at motif-conditioned saddles.** A positive sample would be either a non-saddle admitted by the filter (e.g., a degenerate flat direction) or a genuine failure of the linearisation. Direction sensitive.

5. **Mobility-universality of `ℛ_G`.** Rerunning with alternative mobility laws (`M(p) = (1-p)^β` for different `β`, or saturating forms) while keeping `p̂` fixed in the canonical regime should leave `ℛ_G` motif-conditioned distribution invariant. The prefactor `μ_1 = M'/(2M)` changes; the ratio statistic does not. This is the cleanest direct test of the mobility-universality result.

---

## 6. Durable structural content

1. **`G_{00} = 0` is a rigid kinematic identity of the acoustic metric.** It is not a small parameter, not a linearisation artifact, and not dependent on `ρ_0`. Any ED-framework statement that relies on `G_{00} ≠ 0` (e.g., to source an "effective energy density") is inconsistent with the acoustic-metric construction.

2. **The spatial eigenvalue ratio `ℛ_G = r^*` is the third observed instance of r*-in-distribution** — after the original `κ_∥/κ_⊥` (ED-SC 2.0) and the Raychaudhuri ratio `ℛ_{Ray}` (GR-SC 1.1). Three distinct geometric contractions of `g^{eff}` — Hessian eigenvalue ratio, Ricci focusing ratio, Einstein spatial eigenvalue ratio — collapse to the same filtered GRF statistic at motif-conditioned φ-saddles.

3. **Trace-type invariants are Gaussian zero-median.** `tr(G^{ij}) = μ_1 tr(H_φ)`. This is the fourth observed instance (the Ricci scalar `R`, the Raychaudhuri `F̄`, the trace of Einstein, and `tr(H_φ)` itself) of the same Gaussian-zero-median pattern. The underlying mechanism is `a ↔ b` symmetry of `f_{sad}` preserved by the motif filter.

4. **Sign-definite quadratic invariants scale as `μ_1² σ_2²`.** `det(G^{ij})`, `(∇²N)²/N²`, and `C²` (Weyl, GR-SC 1.6) all scale this way. Their medians are fixed fractions of `μ_1² σ_2²`:

  | Invariant | Median / (μ₁²σ_2²) |
  | --- | --- |
  | `|\det(G^{ij})|` | ≈ 0.42 |
  | `C²` (Weyl, see GR-SC 1.6) | ≈ 2.13 |

5. **The r*-template has now produced three distinct scalar classes:**

  - **r*-type (ratio):** Mobility-universal signed eigenvalue ratio. Median ≈ −1.88 (filtered).
  - **Gaussian-type (trace):** Zero median by GRF symmetry. Scale `|μ_1|σ_2`.
  - **Quadratic-type (det, norm):** Sign-definite positive or negative. Median scales as `μ_1²σ_2²`.

  Every further GR-adjacent invariant should be classifiable into one of these three classes by inspecting its index structure on `H_φ` at linearisation.

---

## Appendix A — Numerical verification of saddle moments

From the joint saddle density `f_{sad}(s, u) ∝ s(s²-u²) exp[−(4s²+2u²)/σ_2²]`, Monte Carlo samples (N = 5·10⁵, σ_2 = 1):

| Quantity | Analytic | MC | Agreement |
| --- | --- | --- | --- |
| `⟨u²⟩` | `0.08333` | `0.08333` | exact |
| `⟨tr²⟩ = 4⟨u²⟩` | `0.33333` | `0.33333` | exact |
| `\mathrm{std}(tr)` | `1/\sqrt{3} = 0.5774` | `0.5773` | 4 sig fig |
| `⟨s²⟩` | `7/12 = 0.5833` | `0.5833` | 4 sig fig |
| `⟨ab⟩ = ⟨s²-u²⟩` | `1/2` | `0.4998` | 4 sig fig |
| `\mathrm{med}(\|tr\|)` | `0.6745 \cdot 1/\sqrt 3 = 0.3894` | `0.3893` | 4 sig fig |
| `\mathrm{med}(ab)` | (no closed form) | `0.4199` | MC |

All analytic values recovered by MC to 4 sig fig. Integration code: the identity `⟨s²⟩ = 7σ_2²/12` is a consequence of

$$
\int_{|u|}^{\infty} 2s(s^2 - u^2) e^{-(4s^2+2u^2)/\sigma^2}\,ds = \frac{\sigma^4}{8}\,e^{-6u^2/\sigma^2}
$$

followed by Gaussian integration of `s²` against `(σ²/8) e^{-6u²/σ²}` — the full 2D joint, normalised.

---

## Cross-references

- Metric and Ricci: `theory/ED_Effective_Acoustic_Metric.md`, `theory/ED_Acoustic_Metric_Curvature.md`.
- GRF machinery: `theory/ED_SC_2_0_r_star_R2_GRF.md`.
- Raychaudhuri (paired): `theory/GR_SC_1_1_Raychaudhuri_MotifStatistics.md`.
- Weyl (paired): `theory/GR_SC_1_6_WeylTensor_MotifStatistics.md`.
- Scope guardrails: `memory/project_ed10_geometry_qft_scope.md`.
