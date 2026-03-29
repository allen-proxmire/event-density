# ED-Phys-35: Scientific Findings from the 2D Event Density System

**Date:** 2026-03-28
**Data:** 30-point parameter sweep (5 D-values x 3 amplitudes x 2 mode counts), N=48, T=1.0
**Figures:** 8 scientific figures in `edsim2d/output/phase7/figures/`

---

## 1. Transient Structure Taxonomy

The 2D ED system supports five distinct structural motifs, classified by invariant signatures:

### 1.1 Structure Definitions

| Structure | Detection Criterion | Physical Meaning |
|-----------|-------------------|------------------|
| **FILAMENT** | Filamentarity F > 0.7 | Curvature concentrated in one direction; ridge-like density features |
| **SADDLE** | Saddle fraction > 0.3 | Hessian eigenvalues of opposite sign; pass-like topology between peaks |
| **SHEET** | Sheetness > 0.7 | Both Hessian eigenvalues same sign; uniform concavity/convexity |
| **TWIST** | Twist RMS > 0.1 | Large mixed partial d^2 rho/dxdy; off-diagonal curvature |
| **HORIZON** | Max proximity > 0.5 | Mobility M(rho) approaching zero; density near rho_max |

### 1.2 Observed Motif Sequences

**Single-mode IC (Nm=1):** The field is dominated by the cos(pi x)cos(pi y) mode. No saddles, no horizons. Structure remains SMOOTH throughout relaxation. Filamentarity stays near 0.44-0.48 (the baseline value for a single 2D cosine, which has inherent anisotropy between its ridge and valley directions).

**Multi-mode IC (Nm=4):** With 16 modes superposed (4x4), the field immediately develops:
- **SADDLE** structure (saddle fraction 0.43-0.75) from the interference pattern
- **TWIST** structure (twist RMS 3-29) from the cross-coupling of modes
- **HORIZON** proximity (> 0.96) when total amplitude exceeds ~0.03

The temporal sequence is: SADDLE + TWIST + HORIZON at t=0 -> SADDLE + TWIST + HORIZON through relaxation -> slow convergence toward SMOOTH. The horizon-forming runs never fully relax within T=1.0.

### 1.3 Key Finding: Horizon Formation is Amplitude-Dependent, Not D-Dependent

In 1D, horizon formation requires large D (strong diffusion compresses density against the capacity bound). In 2D, horizons form at **much smaller D** because multi-mode superposition creates constructive interference maxima. The table below shows which (D, A, Nm) combinations form horizons:

| D | A=0.01 | A=0.03 | A=0.05 |
|---|--------|--------|--------|
| **Nm=1** | | | |
| 0.1-0.9 | No horizon | No horizon | No horizon |
| **Nm=4** | | | |
| 0.1 | No horizon | **HORIZON** | **HORIZON** |
| 0.3 | No horizon | **HORIZON** | **HORIZON** |
| 0.5 | No horizon | **HORIZON** | **HORIZON** |
| 0.7 | No horizon | **HORIZON** | **HORIZON** |
| 0.9 | No horizon | **HORIZON** | **HORIZON** |

A 2D multi-mode perturbation with total amplitude A=0.03 and 16 modes creates interference maxima of order A * sqrt(Nm) ~ 0.12, pushing rho to ~0.62. The mobility function M(rho) = (1 - rho)^2 drops to 0.14 at this density, and the nonlinear feedback loop (high rho -> low mobility -> slow redistribution -> even higher rho) triggers horizon formation.

This is a **genuinely 2D phenomenon**: the 1D equivalent with 4 modes has smaller interference maxima and does not trigger horizons at the same amplitude.

---

## 2. Universality Analysis

### 2.1 Universality Score

The universality score across all 30 runs is **U = 0.45** (moderate). This is lower than the 1D universality score because:
1. The multi-mode horizon-forming runs diverge sharply from the single-mode runs
2. The sweep time T=1.0 is insufficient for full convergence

When restricted to single-mode runs only (Nm=1, 15 runs), the invariant landscape is much tighter.

### 2.2 Invariant Stability Classification

| Invariant | Cross-Run CV | Classification |
|-----------|-------------|----------------|
| Filamentarity F | 0.20 | **STABLE** |
| Gradient dissipation R_grad | 0.17 | **STABLE** |
| Penalty dissipation R_pen | 0.63 | VARIABLE |
| Spectral entropy H | 1.43 | VARIABLE |
| Saddle fraction | 0.34 | VARIABLE |
| Curvature RMS | 2.15 | VARIABLE |

**Stable invariants** (CV < 0.30): Filamentarity and the gradient dissipation fraction are structural properties of the ED architecture that persist across parameter regimes. These are candidates for 2D architectural laws.

**Variable invariants** (CV > 0.30): Spectral entropy, saddle fraction, and curvature are regime-dependent — they encode the specific dynamics rather than the architecture. In 1D, spectral entropy is an invariant (CV < 5% at convergence); the higher 2D variability reflects the richer space of possible spectral distributions in 2D.

### 2.3 Convergence to Attractor

Only 5 of 30 runs converged to a stable spectral entropy (CV < 5% in the last 20% of the time series). All 5 are single-mode runs at high D (D >= 0.7). The remaining runs either:
- Have not reached the attractor by T=1.0 (need longer integration), or
- Are in the horizon regime (permanent near-capacity state with ongoing dynamics)

This suggests that the 2D attractor exists and is reachable, but the convergence timescale is longer than in 1D due to the larger modal space.

---

## 3. Dimensional Effects: 2D vs 1D

### 3.1 Quantitative Comparison

Running the same physics (D=0.3, A=0.05) with a y-invariant IC (effectively 1D) and an isotropic 2D IC:

| Invariant | 1D-embedded | 2D-isotropic | Ratio | Interpretation |
|-----------|-------------|-------------|-------|----------------|
| Spectral entropy | 0.081 | 0.085 | 1.06 | Nearly identical — entropy is architecture-determined |
| ED complexity | 0.00306 | 0.00069 | 0.23 | **4x lower in 2D** — energy spreads over 2 dimensions |
| Filamentarity | 1.000 | 0.476 | 0.48 | 1D is maximally filamentary by construction |
| A_spec | 1.000 | 0.000 | 0 | 2D isotropic has no preferred axis |
| Saddle fraction | 0.000 | 0.547 | inf | **Saddles are a 2D-only phenomenon** |
| Curvature RMS | 0.000 | 2.252 | inf | **Level-set curvature is 2D-only** |
| R_grad | 0.721 | 0.834 | 1.16 | 2D has 16% more gradient dissipation |
| R_pen | 0.279 | 0.166 | 0.60 | 2D has 40% less penalty dissipation |

### 3.2 Key Dimensional Findings

**Finding D1: ED complexity is dimension-diluted.** A perturbation of the same L^2 norm produces 4x less gradient energy in 2D than in 1D, because the energy distributes over 2 spatial axes. This suggests that the complexity scale C_ED must be normalised by dimension when comparing 1D and 2D systems.

**Finding D2: Saddle-point topology is genuinely 2D.** In 1D, the Hessian has one eigenvalue and no saddle points. In 2D, saddle points occupy ~55% of the domain even for a simple isotropic cosine mode. These saddle regions are where the gradient field reverses direction — they are the 2D analogue of zero-crossing points in 1D, but with richer topology.

**Finding D3: The dissipation partition shifts toward gradients in 2D.** The gradient channel carries 83% of dissipation in 2D vs 72% in 1D (for the same D value). The penalty channel drops from 28% to 17%. This is because the 2D Laplacian has twice the eigenvalue magnitude (sum of x and y eigenvalues) at the same wavenumber, making diffusive smoothing more efficient relative to the penalty relaxation.

**Finding D4: The unique attractor appears to persist in 2D.** For single-mode runs at D=0.3, the spectral entropy shows a clear trajectory toward a shared asymptotic value, regardless of amplitude (H_late increases with A but converges toward a common curve at long times). The attractor structure is: rho -> rho* + small residual in the (1,1) mode, with all higher modes decayed.

### 3.3 New 2D-Only Phenomena

1. **Anisotropy trajectories** (Fig 6): Multi-mode runs trace a characteristic path in the (A_spec, A_geom) plane, starting from the IC's anisotropy and relaxing toward (0, 0) (isotropy). The trajectory is not straight — geometric anisotropy decays faster than spectral anisotropy, because the gradient field isotropises faster than the modal energy redistribution.

2. **Curvature dynamics**: Level-set curvature starts moderate, peaks during the transient as modes reorganise, then decays. The curvature peak marks the transition from the multi-modal initial state to the dominant-mode attractor.

3. **Twist decay**: The mixed partial d^2 rho/dxdy decays exponentially during relaxation, with a rate that scales with D. Twist is a direct measure of inter-modal coupling (it vanishes for separable fields cos(kx)*cos(ky) only when kx or ky is zero).

---

## 4. Energy and Dissipation

### 4.1 Energy Decay Rates

The energy ratio E(T)/E(0) depends strongly on D:

| D | E_ratio (Nm=1) | E_ratio (Nm=4, A=0.01) |
|---|----------------|------------------------|
| 0.1 | 0.387 | 0.039 |
| 0.3 | 0.055 | 0.003 |
| 0.5 | 0.008 | 0.001 |
| 0.7 | 0.001 | 0.0001 |
| 0.9 | 0.0001 | 0.00002 |

The single-mode energy decay is approximately exponential: E(t) ~ exp(-2 D alpha_11 t) where alpha_11 = M* mu_11 + P*'. The multi-mode decay is faster because higher modes have larger eigenvalues and decay more quickly — the energy concentrates in the lowest mode before that mode itself decays.

### 4.2 Dissipation Partition

The gradient fraction R_grad is the dominant dissipation channel across all regimes (Fig 5). Its value increases with D:

| D | R_grad | R_pen | R_part |
|---|--------|-------|--------|
| 0.1 | 0.58 | 0.42 | < 1e-8 |
| 0.3 | 0.83 | 0.17 | < 1e-8 |
| 0.5 | 0.94 | 0.06 | < 1e-8 |
| 0.7 | 0.98 | 0.02 | < 1e-8 |
| 0.9 | 0.99 | 0.01 | < 1e-8 |

The participation channel is negligible in all runs (R_part < 1e-8) because the participation variable v remains near zero for these small-amplitude ICs with v(0)=0. The R_grad/R_pen partition is determined by the ratio D*M*mu_11 / P*' which increases with D.

---

## 5. Scientific Figures

| Figure | Content | Key Observation |
|--------|---------|-----------------|
| **fig1** | Transient evolution (Nm=4 multi-mode) | Interference pattern -> saddle-dominated field -> slow relaxation |
| **fig2** | Spectral entropy vs D | Entropy increases with A but saturates; higher D -> faster convergence |
| **fig3** | Filamentarity vs D (multi-mode) | F ~ 0.5-0.7 regardless of D; a structural invariant |
| **fig4** | Energy decay vs D | Exponential decay; rate linear in D |
| **fig5** | Dissipation ratios | R_grad dominates; increases monotonically with D |
| **fig6** | Anisotropy trajectory (A_spec vs A_geom) | Non-diagonal relaxation path; geometric anisotropy decays first |
| **fig7** | Geometry quad (D=0.3, Nm=4) | Shows Hessian eigenvalues, saddle/ridge structure |
| **fig8** | Universality scatter (H* vs D, R_grad* vs D) | Curves collapse for single-mode; multi-mode diverges at horizons |

---

## 6. Open Questions for 3D Extension

1. **Does the 3D Laplacian further dilute complexity?** The 2D complexity is 4x lower than 1D for the same perturbation. In 3D, we expect another factor of ~2-3x reduction. Does this change the attractor structure?

2. **Do 3D saddle geometries (monkey saddles, umbilic points) introduce new invariant families?** The 2D Hessian has 2 eigenvalues; the 3D Hessian has 3, enabling richer topology (e.g., lambda_1 > 0 > lambda_2 > lambda_3 gives "pancake" collapse).

3. **Does the horizon formation threshold decrease further in 3D?** The 2D multi-mode interference maxima scale as A * sqrt(Nm). In 3D with Nm modes per axis, the interference scales as A * Nm^{3/4}, potentially triggering horizons at even smaller amplitudes.

4. **Is the R_grad dominance preserved in 3D?** The 3D Laplacian eigenvalue is the sum of 3 components, further boosting gradient dissipation relative to penalty. We predict R_grad -> 1 even faster with D.

5. **What is the 3D analogue of filamentarity?** In 3D, the Hessian has 3 eigenvalues, giving a richer morphology: sheets (2 similar eigenvalues, 1 different), filaments (1 dominant eigenvalue), and blobs (3 similar eigenvalues). The Minkowski functionals (volume, area, mean curvature, Euler characteristic) provide the natural classification.

---

## 7. Summary

The 2D ED system preserves the core architectural properties of the 1D system — energy monotone decrease, unique attractor, exponential modal decay — while introducing genuinely new phenomena:

- **Saddle-point topology** (55% of domain for isotropic ICs)
- **Constructive interference horizons** (multi-mode 2D ICs hit rho_max at lower amplitude than 1D)
- **Dissipation partition shift** (83% gradient vs 72% in 1D at D=0.3)
- **Anisotropy relaxation trajectories** (geometric anisotropy decays faster than spectral)
- **Dimension-diluted complexity** (4x reduction in gradient energy vs 1D)

The two most stable 2D invariants are **filamentarity** (CV=0.20) and **gradient dissipation fraction** (CV=0.17), making them candidates for 2D architectural laws analogous to the 1D invariant families.
