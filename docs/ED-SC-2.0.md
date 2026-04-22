# ED-SC 2.0: Architectural Invariance Statement

**Revision:** 2.0 (supersedes ED-Arch-01 §5, ED-Arch-02 §3). **Date:** 2026-04-17. **Status:** canonical reference for the ED-SC cross-scale program.

**Citation form:** "ED-SC 2.0 §N."

---

## 1. Preliminaries

### 1.1 Event-density field

Let `Ω ⊂ ℝ²` be a bounded domain and let

$$E: \Omega \to \mathbb{R}$$

be a scalar field interpreted as the event-density of a physical system. In simulation, `E` is the lattice value `p(x, y)` of a discretised ED update rule. In observational or experimental systems, `E` is an explicitly specified density, potential, thickness, or order-parameter field (see §5). The mapping from a physical system to `E` must be stipulated, not inferred.

### 1.2 Hessian and stationary points

At each point `x ∈ Ω` at which `E` is twice differentiable,

$$H(x) = \nabla^2 E(x) = \begin{pmatrix} \partial_{xx} E & \partial_{xy} E \\ \partial_{xy} E & \partial_{yy} E \end{pmatrix}.$$

A point `x*` is a **Morse saddle** of `E` if `∇E(x*) = 0`, `\det H(x*) < 0`, and `|λ_{\min}(H(x*))| / |λ_{\max}(H(x*))| \geq \delta` for a pre-registered non-degeneracy tolerance `δ = 0.10`.

### 1.3 Saddle ratio

For a Morse saddle `x*` with Hessian eigenvalues `λ_1 < 0 < λ_2`, the **saddle ratio** is

$$r(x*) = \frac{\lambda_{\text{large}}}{\lambda_{\text{small}}}, \quad \lambda_{\text{large}} := \arg\max_{\lambda \in \{λ_1, λ_2\}} |\lambda|, \quad \lambda_{\text{small}} := \arg\min_{\lambda \in \{λ_1, λ_2\}} |\lambda|.$$

By construction `r(x*) < 0` and `|r(x*)| \geq 1`.

### 1.4 Motif filter

Let `\hat E = \operatorname{mean}(E)`, `\sigma_E = \operatorname{std}(E)`, and define thresholds

$$E_{\text{hi}} = \hat E + \alpha \sigma_E, \qquad E_{\text{lo}} = \hat E - \alpha \sigma_E, \qquad \alpha = 0.25.$$

For a Morse saddle `x*` with principal-axis eigenvectors `\hat e_{\text{neg}}` (`\lambda < 0`) and `\hat e_{\text{pos}}` (`\lambda > 0`), trace four rays of length `L_{\text{ray}}` in the directions `\pm \hat e_{\text{neg}}`, `\pm \hat e_{\text{pos}}`, sampled at integer lattice steps with periodic wrap on `Ω`.

`x*` is **motif-admitted** iff the endpoints satisfy:

- `E(\text{endpoint of } \pm \hat e_{\text{neg}}) < E_{\text{lo}}` (both compression rays descend into low-`E` regions), AND
- `E(\text{endpoint of } \pm \hat e_{\text{pos}}) > E_{\text{hi}}` (both expansion rays ascend into high-`E` regions).

The pre-registered ray length is `L_{\text{ray}} = 2` lattice units (scale-free: the filter operates at the smallest non-trivial scale that resolves the saddle topology; coarser `L_{\text{ray}}` is permissible provided it is declared before the test).

The **motif-conditioned saddle set** is

$$\mathcal{S}_{\text{motif}}(E) = \{\, x* \text{ Morse saddle of } E \,:\, x* \text{ is motif-admitted}\,\}.$$

### 1.5 Motif-conditioned distribution

$$\mathcal{R}_{\text{motif}}(E) = \{\, r(x*) \,:\, x* \in \mathcal{S}_{\text{motif}}(E) \,\}.$$

---

## 2. Architectural invariance claim (ED-SC 2.0)

> **Claim.** For every pair of ED-architecturally-equivalent systems `A` and `B` satisfying the domain conditions of §3, there exist event-density fields `E_A` and `E_B` on 2D domains `Ω_A, Ω_B` such that the motif-conditioned distributions satisfy
>
> $$|\operatorname{median}(\mathcal{R}_{\text{motif}}(E_A)) - \operatorname{median}(\mathcal{R}_{\text{motif}}(E_B))| \leq \varepsilon_{\text{med}}, \qquad \varepsilon_{\text{med}} = 0.2.$$
>
> Furthermore, the common value is
>
> $$r^* = \operatorname{median}(\mathcal{R}_{\text{motif}}(E)) \approx -1.30,$$
>
> with Scenario D at its architectural saddle peak `(n^* = 2.7, \sigma^* = 0.0556)` as the reference system: the motif-conditioned median of the canonical Scenario-D field satisfies `r^*_{\text{ScenD}} = -1.304`.

No claim is made about higher moments of `\mathcal{R}_{\text{motif}}` (mean, variance, IQR, skewness, tail behaviour). The invariant is **the median, and only the median**.

---

## 3. Domain of applicability

ED-SC 2.0 applies exclusively to systems in which a scalar field `E : Ω \to \mathbb{R}` can be defined on a 2D **real-space physical domain** `Ω ⊂ \mathbb{R}^2`, and on which:

1. `E` is measurable or computable at resolution `\Delta x \leq L_{\text{coh}}(E) / 8`, where `L_{\text{coh}}` is the coherence length of `E` (i.e., the first-zero crossing of the autocorrelation, or equivalently `1 / \operatorname{mean}(|\nabla E|)`).
2. `\nabla E` and `\nabla^2 E` are computable via central-difference stencils on the sampling grid.
3. The sampling domain `Ω` contains at least 10 Morse saddles of `E`, post-degeneracy filter.

Systems that do **not** qualify under ED-SC 2.0, even if they exhibit saddle topology:

| Excluded system class | Reason |
|:---|:---|
| k-space band dispersions (graphene, twisted bilayer graphene, kagome) | `E(k_x, k_y)` is a reciprocal-space object, not a real-space density |
| Effective-potential saddles in dynamical systems (Lagrange L1/L3) | `Ω` is a phase-space potential, not an event-density |
| Parameter-space observable surfaces (e.g., `f(n, \sigma)` in ED-Arch-01) | Input variables are sweep parameters, not physical coordinates |
| Strain-rate / velocity-gradient tensors (OSCER cross-slot) | Rank-2 tensor object, not the Hessian of a scalar density |
| Minimal-surface curvature (catenoid, gyroid) | Geometric mean-curvature identity `H_1 + H_2 = 0`, unrelated to `∇²E` |
| Stress-intensity-factor fields at crack tips | Singular, not a Morse saddle |

A system becomes admissible under ED-SC 2.0 only if a native 2D real-space physical field `E(x, y)` is stipulated alongside it.

---

## 4. Falsification criterion

ED-SC 2.0 is falsified by any single comparison system `E_X` satisfying §3 for which

$$|\operatorname{median}(\mathcal{R}_{\text{motif}}(E_X)) - (-1.30)| > 0.20.$$

Falsifying measurements must be pre-registered with respect to:

- the chosen field `E_X(x, y)` and its data source,
- the motif-filter parameters `(\alpha, L_{\text{ray}}, \delta)`,
- the sampling domain `Ω_X`.

Post-hoc parameter adjustment to recover a match is disallowed. The filter parameters of §1.4 are to be used unchanged across all comparison systems. The only quantity that may be tuned per-system is the IC-/measurement-specific sampling grid, provided the resolution condition of §3 is met.

Partial falsification (e.g., the median sits at `−1.6` in System `X` but at `−1.3` in System `Y`) falsifies the claim of universal invariance but not the existence of two architectural sub-classes. In such cases the invariance claim must be restated with an explicit class partition.

---

## 5. Cross-scale test protocol

Each comparison system is specified by: (i) the 2D real-space field `E`, (ii) the data source, (iii) the extraction procedure for the motif-conditioned distribution, (iv) the pass criterion.

### 5.1 Local Group projected density

- **Field:** projected surface mass density `\Sigma(x, y)` of the Local Group on the galactic mass-sheet plane, in the plane-of-sky projection centred on the Milky Way–Andromeda midpoint.
- **Data source:** mass-sheet reconstruction, e.g. Wempe et al. or comparable inversion of observed galaxy positions and velocities.
- **Procedure:** apply the motif filter of §1.4 to `\Sigma(x, y)` with `\alpha = 0.25`, `L_{\text{ray}} = 2` in units of the reconstruction grid. Compute `\operatorname{median}(\mathcal{R}_{\text{motif}}(\Sigma))`.
- **Pass criterion:** median ∈ `[−1.50, −1.10]`.
- **Notes:** the reconstructed `\Sigma` must have a coherence length at least 8× the sampling resolution (per §3). Sparse-sampling artefacts in existing reconstructions may require smoothing to a coarser grid before motif-filter application.

### 5.2 Casimir cavity potential field

- **Field:** lateral interaction potential `U(x, y)` of a gold flake above a textured gold substrate in aqueous-salt solution, evaluated at the equilibrium vertical separation. `U` is the 2D lateral energy landscape experienced by the flake after Casimir + electrostatic balance in the vertical direction.
- **Data source:** direct measurement via flake position tracking, or Lifshitz-framework computation from the substrate topography.
- **Procedure:** apply the motif filter to `U(x, y)` with `\alpha = 0.25`, `L_{\text{ray}} = 2` in units of the measurement grid. Compute `\operatorname{median}(\mathcal{R}_{\text{motif}}(U))`.
- **Pass criterion:** median ∈ `[−1.50, −1.10]`.
- **Notes:** ED-Arch-01 §5 reports a prior Casimir match at `κ∥/κ⊥ ≈ −1.3`. Under ED-SC 2.0 this prior claim is specifically re-targeted at the motif-conditioned median of the lateral potential field, not the vertical-equilibrium Hessian.

### 5.3 Thin-film dewetting thickness field

- **Field:** film thickness `h(x, y)` of a thin polymer or liquid film on a flat substrate during spinodal dewetting, measured in the pre-rupture regime where `h` is continuous.
- **Data source:** atomic force microscopy (AFM) or optical profilometry. Standard resolutions (50 nm lateral, 0.1 nm vertical) satisfy §3.
- **Procedure:** apply the motif filter to `h(x, y)` with `\alpha = 0.25`, `L_{\text{ray}} = 2` in units of the measurement grid.
- **Pass criterion:** median ∈ `[−1.50, −1.10]`.
- **Notes:** valid comparison only in the spinodal pre-rupture regime where `h` has stationary points but has not yet developed ruptured (disconnected) regions.

### 5.4 Stripe-domain order parameter fields

- **Field:** scalar order parameter `\phi(x, y)` of a 2D stripe-domain system (ferroelectric, ferromagnetic, or block-copolymer film) in the stripe-forming regime with occasional defect-driven saddle points at domain junctions.
- **Data source:** piezoelectric force microscopy (PFM), magnetic force microscopy (MFM), or TEM for block copolymers.
- **Procedure:** apply the motif filter to `\phi(x, y)` with `\alpha = 0.25`, `L_{\text{ray}} = 2`.
- **Pass criterion:** median ∈ `[−1.50, −1.10]`.
- **Notes:** restrict the sampling domain to regions containing at least 10 Morse saddles. Pure single-stripe regions (no defects) are not testable; regions with defect dislocations / disclinations are.

### 5.5 Reaction-diffusion activator fields

- **Field:** activator concentration `u(x, y)` of a 2D gradient-form reaction-diffusion system (e.g. Gierer–Meinhardt with fast inhibitor adiabatically eliminated, or Allen–Cahn) at a steady or quasi-steady state.
- **Data source:** simulation or fluorescence imaging of chemical RD experiments (e.g. BZ reaction on a 2D substrate).
- **Procedure:** apply the motif filter to `u(x, y)` with `\alpha = 0.25`, `L_{\text{ray}} = 2`.
- **Pass criterion:** median ∈ `[−1.50, −1.10]`.
- **Notes:** non-gradient reaction-diffusion systems (those without a Lyapunov functional) are excluded — their stationary-point structure is dynamical, not topographic, and `\nabla^2 u` at those points does not correspond to the ED-SC invariant.

---

## 6. Reinterpretation of ED-Arch-01's published value

ED-Arch-01 §5 reports `κ∥ ≈ −1.3, κ⊥ ≈ +1.0` at Scenario D's saddle peak `(n^* = 2.7, \sigma^* = 0.0556)`. The original presentation is ambiguous with respect to the object under measurement: the text adjoins the reported value to a claim of architectural invariance (a field-space property under ED-Arch-02), but the number itself is extracted from the parameter-space Hessian of the phase-exit-step surface `f(n, \sigma)` at its 4×4-sweep ridge maximum.

Under ED-SC 2.0 the ambiguity is resolved as follows:

1. **The `−1.3` value is retained**, but reassigned from the parameter-space Hessian of `f(n, \sigma)` to the motif-conditioned median of the field-space Hessian of the Scenario-D event-density field `p(x, y)` at the same sweep-parameter point `(n^*, \sigma^*)`.

2. **The numerical match between the two Hessians is documented but not assumed structural.** Direct computation (this work) gives `\operatorname{median}(\mathcal{R}_{\text{motif}}(p_{\text{ScenD}})) = -1.304`, within 0.004 of the published parameter-space value. Whether this agreement reflects an underlying `H_{\text{param}} \leftrightarrow H_{\text{field}}` correspondence or is a numerical coincidence is an open theoretical question. ED-SC 2.0 does not depend on its resolution.

3. **The field-space form is canonical; the parameter-space form is deprecated as a citation for architectural invariance.** The phase-exit-step surface `f(n, \sigma)` remains a useful diagnostic for locating Scenario-D's architectural-saddle regime, but its Hessian eigenvalues are not the ED-SC invariant. Papers citing ED-Arch-01's `−1.3` as evidence of cross-scale invariance should be updated to cite ED-SC 2.0 §2 instead, with the motif-conditioned median as the object of the claim.

4. **The IQR of the field-space distribution is not an invariant.** ED-SC 2.0 makes no claim about the spread of `\mathcal{R}_{\text{motif}}`. This is a weakening relative to any implicit reading of ED-Arch-01 that took `±0.2` as a tight tolerance on individual saddle ratios. In ED-SC 2.0, the `±0.2` is the falsification tolerance on the median only.

---

## 7. Reference measurement — Scenario D at `(n^*, \sigma^*)`

For reproducibility and future recalibration, the reference measurement from which `r^* = -1.30` is anchored is as follows.

| Parameter | Value |
|:---|:---|
| Update rule | mobility-weighted (`ed_step_mobility`, ED-05.5 / ED-12.5 cubic compositional form) |
| Grid | 64 × 64, periodic |
| `\alpha` | 0.03 |
| `\gamma` | 0.5 |
| `dt` | 0.05 |
| `p_{\min}, p_{\max}` | 0.01, 1.0 |
| IC | uniform `[0.3, 0.7]` |
| Seed | 77 |
| Mobility exponent `n^*` | 2.7 |
| Noise amplitude `\sigma^*` | 0.0556 |
| Total steps | 500 (`t_{\text{phys}} = 25`) |
| Post-run statistics | `\hat p = 0.10788`, `\sigma_E = 0.01525`, range `[0.054, 0.165]` |
| Motif filter | `\alpha_{\text{filt}} = 0.25`, `L_{\text{ray}} = 2`, `\delta = 0.10` |
| Post-motif sample size | `|\mathcal{S}_{\text{motif}}| = 6` |
| **Reference invariant** | `\operatorname{median}(\mathcal{R}_{\text{motif}}(p_{\text{ScenD}})) = -1.304` |

Re-derivation requires `ED_Update_Rule.py` and `Run_Simulation.py` from `Emergence Universe/ED-SIM-Code/`. The motif-filter implementation is provided in `analysis/scripts/ed_arch_r2/r2_motif_filter.py`.

---

## 8. Open items

1. **Ensemble statistics.** The reference measurement is from a single seed. An ensemble `(N ≥ 20)` over independent seeds would yield an uncertainty estimate on `r^* = −1.30` and a better-characterised filter sensitivity. Not blocking for publication; recommended before first cross-scale test.
2. **Structural vs coincidental `H_{\text{param}} \leftrightarrow H_{\text{field}}` correspondence.** Whether the exact agreement between the parameter-space and field-space medians at `(n^*, \sigma^*)` reflects a derivable mapping is an open theoretical problem. Deferred to a separate ED-SC theory note.
3. **Motif-filter robustness.** Alternative motif detectors (persistence-based Morse–Smale complex, topological-data-analysis thresholding, channel-network graph-theoretic filters) should be cross-checked against the `(α = 0.25, L_{\text{ray}} = 2)` detector to confirm that the `r^* = −1.30` result is detector-robust.
4. **First cross-scale test target.** Among the five comparison systems of §5, **thin-film dewetting (§5.3)** is the lowest-cost: AFM profilometry data at the required resolution is widely published, and the motif filter applies directly. Recommended as the first ED-SC 2.0 cross-scale test.

---

*End of ED-SC 2.0 statement. Supersedes the cross-scale invariance language of ED-Arch-01 §5 and ED-Arch-02 §3. Compatible with the architectural-object taxonomy of ED-Arch-02 §§1–2 (saddles, channels, boundaries, horizons) and the scale-correspondence program of ED-SC-00.*
