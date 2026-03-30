# ED-Phys-01: The ED Update Rule

## Canonical Sources

| Source | Content Used |
|--------|-------------|
| ED-5 (Mathematical Formalization) | ED system triple (E, C, rho), five axioms, compositionality axiom |
| ED-12 (ED Compositional Rule) | General functional rule, three penalty terms, coarse-grained variables, inflation/structure/thinning dynamics |
| ED-12.5 (Cosmology from the Compositional Rule) | Nonlinear diffusion equation, mobility function, Friedmann analogue, horizon conditions |

---

## 1. The ED System (from ED-5)

An Event Density system is a triple **(E, C, rho)** where:

- **E** is a bare event domain (a set with no intrinsic structure)
- **C** is a collection of admissible finite configurations (subsets of E)
- **rho: C -> [0, infinity)** assigns a non-negative density to each configuration

### Axioms

| # | Name | Statement |
|---|------|-----------|
| A1 | Non-negativity | rho(C) >= 0 for all C in C |
| A2 | Null configuration | rho(empty) = 0 |
| A3 | Monotonicity | C subset D implies rho(C) <= rho(D) |
| A4 | Subadditivity | For disjoint C, D: rho(C union D) <= rho(C) + rho(D) |
| A5 | Compositionality | rho(C) = F(rho(C_1), ..., rho(C_k)) for a system-specific rule F |

The compositionality axiom (A5) is the gateway to the ED Compositional Rule: the function F is not fixed by the axioms — it is the physical content of any particular ED model.

---

## 2. The General ED Compositional Rule (from ED-12)

For any two finite configurations A and B:

```
rho(A ∪ B) = rho(A) + rho(B)
             − α ∫_{A∩B} f(ρ) dμ          ... (I)   Relational Penalty
             − β ∫_{A∪B} g(|∇ρ|) dμ        ... (II)  Gradient Penalty
             − γ_b ∫_{∂(A∪B)} h(|∇ρ|) dS   ... (III) Boundary Penalty
```

**Parameters:**

| Symbol | Role | Constraints |
|--------|------|-------------|
| α | Relational penalty coupling | α > 0 |
| β | Gradient penalty coupling | β > 0 |
| γ_b | Boundary penalty coupling | γ_b > 0 |

> **Notation:** We use γ_b for the boundary coupling to distinguish it from γ_exp, the concavity exponent in f(ρ). The original papers use γ for both.

---

## 3. Penalty Term Definitions (from ED-12, ED-12.5)

### 3.1 Relational Penalty: f(ρ)

```
f(ρ) = ρ^{γ_exp},    0 < γ_exp < 1
```

**Properties:**
- **Concave** (f''(ρ) < 0 for ρ > 0): ensures sublinear growth
- At low ρ: f(ρ) ≈ ρ^{γ_exp} is steep → strong competition
- At high ρ: f(ρ) grows sublinearly → penalty saturates → overdense regions stabilize

**Physical role:** Produces gravitational-instability-like behavior:
1. Small overdensities amplified (positive feedback: higher ρ → larger penalty → slower outflow → accumulation)
2. High-ρ pockets stabilize (sublinear saturation prevents runaway)

**Perturbation expansion** around mean density ρ̂:
```
ρ^{γ_exp} = ρ̂^{γ_exp} + γ_exp · ρ̂^{γ_exp − 1} · δρ + O(δρ²)
```

### 3.2 Gradient Penalty: g(|∇ρ|)

```
g(u) = u²
```

**Properties:**
- **Quadratic** in the gradient magnitude
- Penalizes spatial inhomogeneity
- Drives exponential smoothing of gradients (inflation)

**Physical role:** The dominant term in the high-ρ, small-gradient early universe. Produces the inflation-like phase.

### 3.3 Boundary Penalty: h(|∇ρ|)

```
h(u): increasing, saturating
```

**Properties:**
- h(0) = 0
- h'(u) > 0 (increasing)
- h''(u) < 0 for large u (saturating / concave)
- h(u) → h_max as u → ∞

**Concrete choice for simulation** (not specified in the canonical sources; we adopt a standard saturating form):
```
h(u) = h_max · u / (u + u_0)
```
where h_max is the saturation ceiling and u_0 is the half-saturation gradient scale.

**Physical role:** Dominates in the late-time universe when bulk gradients vanish. Produces area-law scaling at extreme gradients (horizons). Ensures finite cost for arbitrarily steep boundaries.

---

## 4. The Nonlinear Diffusion Equation (from ED-12.5)

When the compositional rule is applied to a continuum field ρ(x, t) on a lattice, its dynamics take the form of a nonlinear diffusion equation:

```
∂ρ/∂t = ∇ · [M(ρ) ∇ρ] − α · ∂f/∂ρ + boundary corrections
```

### 4.1 Mobility Function M(ρ)

```
M(ρ) → 0   as   ρ → ρ_max     (saturation / horizon formation)
M(ρ) > 0   for  ρ < ρ_max      (finite diffusivity)
```

**Concrete choice for simulation:**
```
M(ρ) = M_0 · (1 − ρ/ρ_max)^n,    n ≥ 1
```
where M_0 is the bare mobility and n controls the sharpness of saturation.

**Physical role:** Encodes the key ED insight that high-density regions resist reorganization. Horizons form where M(ρ) → 0.

### 4.2 Relaxation Function Γ(ρ)

In the homogeneous limit (∇ρ = 0), the dynamics reduce to:
```
dρ̂/dt = −Γ(ρ̂)
```

This is the ED analogue of the Friedmann equation. The "dark energy" residual is the stiffness preventing full relaxation: Γ(ρ) → 0 as ρ → ρ_min > 0.

---

## 5. Symbolic Derivatives of Each Penalty Term

### 5.1 Relational Penalty Variation

```
δΦ_rel/δρ(x) = α · γ_exp · ρ(x)^{γ_exp − 1}
```

Since 0 < γ_exp < 1, the exponent (γ_exp − 1) is negative, so:
- This derivative diverges as ρ → 0 (strong coupling at low density)
- Decreases as ρ increases (saturation)

### 5.2 Gradient Penalty Variation

The gradient penalty functional is:
```
Φ_grad[ρ] = β ∫ |∇ρ|² dμ
```

Its functional derivative is:
```
δΦ_grad/δρ(x) = −2β · ∇²ρ(x)
```

This is a standard diffusion operator: it smooths gradients.

### 5.3 Boundary Penalty Variation

For the saturating form h(u) = h_max · u / (u + u_0):
```
h'(u) = h_max · u_0 / (u + u_0)²
```

The boundary penalty contributes at domain boundaries and internal sharp interfaces. In the bulk interior of a lattice simulation, this term acts only at cells adjacent to the boundary or at internal gradient discontinuities.

### 5.4 Mobility-Weighted Diffusion

From the nonlinear diffusion form ∂ρ/∂t = ∇·[M(ρ)∇ρ]:
```
∇·[M(ρ)∇ρ] = M(ρ)·∇²ρ + M'(ρ)·|∇ρ|²
```

For M(ρ) = M_0·(1 − ρ/ρ_max)^n:
```
M'(ρ) = −M_0 · n/ρ_max · (1 − ρ/ρ_max)^{n−1}
```

---

## 6. The Complete Continuous Update Equation

Combining all terms, the full PDE governing ρ(x, t) is:

```
∂ρ/∂t = ∇·[M(ρ)∇ρ] − α · γ_exp · ρ^{γ_exp − 1} + (boundary terms at ∂Ω)
```

Expanding the mobility-weighted diffusion:

```
∂ρ/∂t = M(ρ)·∇²ρ + M'(ρ)·|∇ρ|² − α·γ_exp·ρ^{γ_exp − 1} + (boundary terms)
```

### Term-by-term physics:

| Term | Expression | Role |
|------|-----------|------|
| Mobility diffusion | M(ρ)·∇²ρ | Smoothing (inflation); halts at saturation |
| Gradient self-interaction | M'(ρ)·\|∇ρ\|² | Nonlinear correction; negative (brakes diffusion at high ρ) |
| Relational penalty | −α·γ_exp·ρ^{γ_exp−1} | Structure formation (concave competition) |
| Boundary penalty | at ∂Ω only | Horizon/boundary stabilization |

---

## 7. Discretized Update Rule

### 7.1 Lattice Setup

Let ρ_i^t denote the event density at lattice site i at timestep t, on a lattice with spacing Δx in D dimensions.

### 7.2 Finite-Difference Operators

**Discrete Laplacian (D = 1):**
```
∇²ρ_i ≈ (ρ_{i+1} − 2ρ_i + ρ_{i−1}) / Δx²
```

**Discrete Laplacian (D = 2):**
```
∇²ρ_{i,j} ≈ (ρ_{i+1,j} + ρ_{i−1,j} + ρ_{i,j+1} + ρ_{i,j−1} − 4ρ_{i,j}) / Δx²
```

**Discrete gradient magnitude squared (D = 1):**
```
|∇ρ|²_i ≈ ((ρ_{i+1} − ρ_{i−1}) / (2Δx))²
```

**Discrete gradient magnitude squared (D = 2):**
```
|∇ρ|²_{i,j} ≈ ((ρ_{i+1,j} − ρ_{i−1,j}) / (2Δx))² + ((ρ_{i,j+1} − ρ_{i,j−1}) / (2Δx))²
```

### 7.3 Discrete Mobility

```
M_i = M_0 · max(0, 1 − ρ_i/ρ_max)^n
```

The `max(0, ...)` clamp prevents negative mobility if ρ overshoots ρ_max.

### 7.4 Discrete Mobility Derivative

```
M'_i = −M_0 · (n/ρ_max) · max(0, 1 − ρ_i/ρ_max)^{n−1}
```

### 7.5 The Explicit Update Rule

```
ρ_i^{t+1} = ρ_i^t + η · [
    M_i · (∇²ρ)_i                          ... mobility-weighted diffusion
  + M'_i · |∇ρ|²_i                         ... nonlinear gradient correction
  − α · γ_exp · max(ρ_i, ε)^{γ_exp − 1}   ... relational penalty
]
```

where:
- **η** is the timestep (learning rate)
- **ε** is a small floor (e.g., 1e-10) to prevent divergence of ρ^{γ_exp−1} at ρ = 0

### 7.6 Boundary Conditions

| Type | Implementation |
|------|---------------|
| **Periodic** | ρ_{0} = ρ_{N}, ρ_{N+1} = ρ_{1} |
| **Absorbing** | ρ_{boundary} = ρ_min (fixed low density) |
| **Reflecting** | ∇ρ · n̂ = 0 at boundary (ghost cells mirror interior) |

For cosmological simulations, **periodic** boundary conditions are the default (homogeneity assumption). For horizon studies, **absorbing** boundaries may be appropriate.

### 7.7 Boundary Penalty Implementation

At boundary-adjacent cells (within 1 cell of ∂Ω), add:

```
boundary_correction_i = −γ_b · h'(|∇ρ|_i) · (∇²ρ)_i / |∇ρ|_i
```

This term is only active at cells where ρ has significant gradient toward the domain boundary. For periodic boundaries in cosmological runs, this term is zero everywhere.

---

## 8. Stability Constraints

### 8.1 CFL-Type Condition (Diffusion Stability)

For an explicit Euler scheme with diffusion coefficient D_eff = max_i M_i, stability requires:

**1D:**
```
η < Δx² / (2 · D_eff)
```

**2D:**
```
η < Δx² / (4 · D_eff)
```

**General D dimensions:**
```
η < Δx² / (2D · D_eff)
```

where D_eff = M_0 (the maximum mobility, occurring at ρ = 0).

### 8.2 Relational Penalty Stability

The relational term −α·γ_exp·ρ^{γ_exp−1} has magnitude that diverges as ρ → 0. To prevent numerical blowup:

1. **Floor clamping:** Use max(ρ, ε) with ε ≈ 1e-10
2. **Adaptive timestep:** Reduce η when min(ρ) approaches zero

### 8.3 Combined Stability Criterion

```
η < min(
    Δx² / (2D · M_0),                           ... diffusion CFL
    ε^{1−γ_exp} / (α · γ_exp)                   ... relational term bound
)
```

### 8.4 Positivity Preservation

The update rule does not automatically preserve ρ ≥ 0. Enforce after each step:
```
ρ_i^{t+1} = max(ρ_i^{t+1}, 0)
```

---

## 9. Coarse-Grained Observables

These quantities track the macroscopic state of the simulation (from ED-12):

| Observable | Definition | Physical Analogue |
|-----------|-----------|-------------------|
| Mean density ρ̂(t) | (1/N) Σ_i ρ_i^t | Global "thickness" of becoming |
| Mean gradient G(t) | (1/N) Σ_i \|∇ρ\|_i^t | Degree of inhomogeneity |
| Scale factor proxy a(t) | 1 / G(t) | Cosmological scale factor |
| Structure count S(t) | Number of connected regions with ρ > ρ_threshold | Galaxy/structure count |
| Max density ρ_max(t) | max_i ρ_i^t | Peak becoming intensity |
| Gradient energy E_grad(t) | Σ_i \|∇ρ\|²_i | Total gradient penalty cost |

---

## 10. Cosmological Phases (from ED-12)

The update rule naturally produces four epochs:

### Phase 1: Inflation (Gradient Smoothing)
- **Regime:** High ρ, nonzero G
- **Dominant term:** M(ρ)·∇²ρ (diffusion)
- **Dynamics:** G(t) = G(0)·exp(−λ₁·t); a(t) ∝ exp(λ₁·t)
- **Duration:** Ends when G falls below a threshold where diffusion weakens

### Phase 2: Structure Formation
- **Regime:** Moderate ρ, small perturbations δρ
- **Dominant term:** −α·γ_exp·ρ^{γ_exp−1} (relational penalty)
- **Dynamics:** Overdensities amplified by concave competition; stabilized by sublinear saturation
- **Signatures:** Localized high-ρ pockets form; structure count increases then saturates

### Phase 3: Global Thinning (Expansion)
- **Regime:** Decreasing ρ̂, small G
- **Dominant term:** Diffusive outflow from structures
- **Dynamics:** dρ̂/dt ≈ −λ₂·G²; a(t) grows (first exponentially, then slowly)

### Phase 4: Heat Death (Asymptotic Flatness)
- **Regime:** ρ̂ → ρ_min, G → 0
- **Dominant term:** Boundary penalty (area-law scaling)
- **Dynamics:** Near-uniform low-ρ state; negligible further evolution

---

## 11. Pseudocode

```
FUNCTION ed_simulate(params, initial_rho, n_steps):
    # Unpack parameters
    alpha, gamma_exp, beta, gamma_b = params.alpha, params.gamma_exp, params.beta, params.gamma_b
    M_0, rho_max_param, n_mob = params.M_0, params.rho_max, params.n_mob
    eta, dx, eps = params.eta, params.dx, params.eps
    D = params.dimensions  # 1 or 2

    # Initialize
    rho = copy(initial_rho)
    history = []

    FOR t = 0 TO n_steps - 1:

        # 1. Compute discrete Laplacian
        lap = discrete_laplacian(rho, dx, boundary_type)

        # 2. Compute discrete gradient magnitude squared
        grad_sq = discrete_grad_squared(rho, dx, boundary_type)

        # 3. Compute mobility at each site
        M = M_0 * max(0, 1 - rho / rho_max_param)^n_mob

        # 4. Compute mobility derivative at each site
        M_prime = -M_0 * (n_mob / rho_max_param) * max(0, 1 - rho / rho_max_param)^(n_mob - 1)

        # 5. Compute relational penalty derivative
        rel_penalty = alpha * gamma_exp * max(rho, eps)^(gamma_exp - 1)

        # 6. Assemble the RHS
        drho = M * lap + M_prime * grad_sq - rel_penalty

        # 7. Update
        rho = rho + eta * drho

        # 8. Enforce positivity
        rho = max(rho, 0)

        # 9. Record observables
        IF t % record_interval == 0:
            history.append({
                't': t,
                'rho_mean': mean(rho),
                'G_mean': mean(sqrt(grad_sq)),
                'rho_max': max(rho),
                'structure_count': count_structures(rho, threshold),
                'grad_energy': sum(grad_sq)
            })

    RETURN rho, history
```

---

## 12. Parameter Summary

| Parameter | Symbol | Typical Range | Role |
|-----------|--------|---------------|------|
| Relational coupling | α | 0.01 − 1.0 | Strength of concave competition |
| Concavity exponent | γ_exp | 0.3 − 0.7 | Controls saturation sharpness (must be in (0,1)) |
| Gradient coupling | β | absorbed into M_0 | Strength of smoothing (inflation) |
| Boundary coupling | γ_b | 0.0 − 1.0 | Strength of boundary/horizon term |
| Bare mobility | M_0 | 0.1 − 10.0 | Maximum diffusion rate |
| Saturation density | ρ_max | 10.0 − 1000.0 | Density ceiling (horizon threshold) |
| Mobility exponent | n_mob | 1 − 3 | Sharpness of saturation cutoff |
| Timestep | η | set by CFL | Evolution rate |
| Grid spacing | Δx | 1.0 (normalized) | Lattice resolution |
| Density floor | ε | 1e-10 | Prevents divergence in relational term |

---

## 13. Notes on Stiffness, Stability, and Parameter Sensitivity

### 13.1 Stiffness

The system is **mildly stiff** due to:

1. **Relational term divergence:** The term ρ^{γ_exp−1} diverges as ρ → 0. The floor ε mitigates this, but cells near ε may require small timesteps.

2. **Mobility contrast:** When some cells are near ρ_max (M → 0) and others are at low ρ (M → M_0), the system has widely varying effective diffusion rates. An implicit or semi-implicit scheme may be needed for large grids.

3. **Scale separation:** During inflation, G decays exponentially while ρ̂ changes slowly — this timescale separation can cause numerical drift if η is tuned only for the fast mode.

### 13.2 Sensitivity

**Most sensitive parameters:**
- **γ_exp** (concavity exponent): Controls whether structures form at all. Below ~0.2, the relational penalty is too weak; above ~0.8, it is nearly linear and loses its concave amplification property.
- **α / M_0 ratio:** Determines the balance between structure formation and smoothing. If α >> M_0, structures dominate immediately; if M_0 >> α, the system smooths completely before structures can form.
- **ρ_max**: Sets the horizon scale. Too low and the system saturates everywhere; too high and mobility effects are negligible.

**Least sensitive parameters:**
- **n_mob** (mobility exponent): Changes the sharpness of the saturation transition but not its qualitative character.
- **Δx**: The system is scale-free in the continuum limit; results should converge with grid refinement.

### 13.3 Recommended Starting Parameters

For a first cosmological run (exploring all four phases):

```
α       = 0.1
γ_exp   = 0.5
M_0     = 1.0
ρ_max   = 100.0
n_mob   = 2
η       = 0.1 * Δx² / (2D · M_0)   # 10% of CFL limit
Δx      = 1.0
ε       = 1e-10
```

Initial condition: uniform ρ = 50.0 with small Gaussian noise (amplitude ~ 0.1).

---

## 14. Relationship to Canonical Cosmological Dynamics

| ED-12 Prediction | Update Rule Realization |
|-----------------|------------------------|
| G(t) = G(0)·exp(−λ₁·t) | Emerges from M(ρ)·∇²ρ dominance at early times |
| dρ̂/dt = −λ₂·G² | Emerges from net outward diffusion from structures |
| ρ^{γ_exp} amplifies overdensities | Directly encoded in −α·γ_exp·ρ^{γ_exp−1} |
| h(u) saturates at horizons | Boundary term with saturating h(u) |
| M(ρ) → 0 at ρ_max | Mobility function halts diffusion at saturation |
| dM/dt ∝ −1/M² (black holes) | Emerges in the ρ → ρ_max limit of the diffusion equation |

---

## 15. Open Decisions for ED-Phys-02

The following choices are deferred to the simulator implementation phase:

1. **Explicit vs. semi-implicit integration:** Explicit Euler is simplest but may require very small η. A semi-implicit scheme (implicit diffusion, explicit relational) would allow larger timesteps.

2. **Boundary penalty implementation:** The exact form of h(u) is not specified canonically. The choice h(u) = h_max·u/(u+u_0) is a reasonable default but alternatives (e.g., tanh, erf) should be tested.

3. **Adaptive timestepping:** Whether to implement adaptive η based on local stiffness indicators.

4. **Dimensionality:** 1D runs first (fast, captures homogeneous cosmology), then 2D (captures structure formation).
