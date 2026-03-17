# ED-Phys-19: The Unified Cosmological Equation of Event Density

## 1. Introduction

This module derives the unified partial differential equation governing cosmological dynamics in the Event Density (ED) framework. The derivation synthesizes results from eight prior modules:

- ED-Phys-07: linear stability analysis
- ED-Phys-13: parabolic vs hyperbolic time evolution
- ED-Phys-15: P_SY2 symmetric-denominator restoring penalty
- ED-Phys-16: coupled oscillators and nonlinear mode interactions
- ED-Phys-17: oscillator cosmology (universal relaxation)
- ED-Phys-18: hybrid cosmology (parabolic + oscillatory mixing)

The result is the first complete theoretical formulation of ED cosmology: a single PDE with tunable dynamical character, a unique equilibrium, a computable ground state energy, a smooth phase diagram, and a natural partition between bulk and horizon dynamics.

**Canonical sources:** ED-5, ED-12, ED-12.5.

---

## 2. The Unified ED Cosmology PDE

### 2.1 Derivation

The ED framework admits two participation channels through which density responds to thermodynamic forces:

1. **Parabolic (diffusive) channel:** Density responds instantaneously to the right-hand side (RHS) of the mobility equation. This is first-order in time, irreversible, and dissipative.

2. **Oscillatory (inertial) channel:** Density responds through a velocity field v that carries memory (inertia). This is second-order in time, supports wave propagation, and produces damped oscillations.

Both channels operate on the same density field rho and the same RHS. The unified PDE couples them through mixing weights D (parabolic) and H (oscillatory):

```
    ┌─────────────────────────────────────────────────────────┐
    │  ∂ρ/∂t = D · F[ρ]  +  H · v                           │
    │  ∂v/∂t = (1/τ) · (F[ρ] − ζ · v)                       │
    │                                                         │
    │  D + H = 1,   D ∈ [0,1],   H ∈ [0,1]                  │
    │                                                         │
    │  F[ρ] = M(ρ)·∇²ρ + M'(ρ)·|∇ρ|² − P_SY2(ρ)            │
    └─────────────────────────────────────────────────────────┘
```

where:

```
    M(ρ)     = M₀ · (1 − ρ/ρ_max)^n_mob          (mobility)
    M'(ρ)    = −M₀ · (n_mob/ρ_max) · (1 − ρ/ρ_max)^(n_mob−1)
    P_SY2(ρ) = αγ · (ρ − ρ*) / √((ρ − ρ*)² + ρ₀²)  (restoring penalty)
```

### 2.2 Sector Emergence

**Parabolic sector (D = 1, H = 0):**
```
    ∂ρ/∂t = F[ρ]
```
The velocity equation decouples. Density responds directly to forces. First-order in time. No oscillations. Monotonic relaxation. This is the classical diffusion equation with nonlinear mobility and restoring force.

**Oscillatory sector (D = 0, H = 1):**
```
    ∂ρ/∂t = v
    ∂v/∂t = (1/τ)(F[ρ] − ζv)
```
Combining: τ·∂²ρ/∂t² + ζ·∂ρ/∂t = F[ρ]. This is a damped wave equation. Second-order in time. Supports oscillations. The participation field v carries inertia.

**Hybrid sector (0 < D < 1):**
```
    ∂ρ/∂t = D·F[ρ] + H·v
```
Both channels contribute. The direct response D·F[ρ] provides immediate dissipation. The inertial response H·v provides memory-driven oscillations. The mixing ratio D/H controls the character of the transient dynamics without affecting the equilibrium.

### 2.3 The Unified PDE as a Single Equation

Eliminating v from the system (by differentiating the first equation and substituting the second), the unified PDE can be written as a single equation for rho:

```
    τ · ∂²ρ/∂t² + (ζ + τD/H · ∂/∂t) · ∂ρ/∂t = (1 + D/H) · F[ρ] + ...
```

This mixed-order PDE is more naturally analyzed as the coupled first-order system. The key insight is that D and H do not change the equilibrium (F[rho] = 0 at rho = rho_star regardless of D, H), only the transient dynamics.

---

## 3. Fundamental Terms: Decomposition of F[rho]

### 3.1 Term-by-Term Analysis

The forcing function F[rho] contains three terms:

**Term 1: Diffusive flux divergence — M(rho) * nabla^2(rho)**

Physical meaning: Density flows from high to low concentration, modulated by mobility. At canonical parameters (M_0 = 1, n_mob = 2, rho_max = 100):

```
    M(rho) = (1 − ρ/100)²
```

| rho | M(rho) | Diffusion strength |
|-----|--------|-------------------|
| 0 | 1.000 | Full |
| 25 | 0.5625 | 56% |
| 50 (rho_star) | 0.250 | 25% |
| 75 | 0.0625 | 6.3% |
| 90 | 0.010 | 1% |
| 95 | 0.0025 | 0.25% |
| 99 | 0.0001 | 0.01% |

Near the ceiling: M -> 0. The diffusive term vanishes. This is the origin of the mobility horizon.

**Term 2: Gradient nonlinearity — M'(rho) * |grad rho|^2**

Physical meaning: Density gradients create a correction to the flux. M'(rho) < 0, so this term pushes density away from gradients (anti-diffusive correction). At canonical parameters:

```
    M'(ρ) = −(2/100) · (1 − ρ/100)
```

This term is quadratic in perturbation amplitude (|grad rho|^2), making it the leading nonlinearity in the system. ED-Phys-16 measured the nonlinear coupling coefficient as ~0.030 — weak but measurable.

Near the ceiling: M' -> 0. The gradient nonlinearity also vanishes.

**Term 3: Restoring penalty — P_SY2(rho)**

Physical meaning: A density-dependent force pushing rho toward rho_star. The algebraic-smooth form:

```
    P_SY2(ρ) = αγ · (ρ − ρ*) / √((ρ − ρ*)² + ρ₀²)
```

Key properties:
- Exactly antisymmetric: P_SY2(rho_star + delta) = -P_SY2(rho_star - delta)
- C-infinity smooth (no discontinuities)
- Bounded: |P_SY2| < alpha*gamma for all rho
- Linear near rho_star: P_SY2 ~ (alpha*gamma/rho_0) * (rho - rho_star)
- Saturating far from rho_star: P_SY2 -> +/- alpha*gamma

**Near the ceiling: P_SY2 does NOT vanish.** At rho = 95: P_SY2(95) = 0.05 * 45/sqrt(45^2 + 0.25) ~ 0.05. The penalty acts even when mobility is negligible.

### 3.2 Ceiling Survival Analysis

| Term | Near rho_star | Near ceiling (rho -> rho_max) |
|------|--------------|------------------------------|
| M * nabla^2(rho) | Active (M = 0.25) | Vanishes (M -> 0) |
| M' * |grad rho|^2 | Active (M' = -0.01) | Vanishes (M' -> 0) |
| P_SY2(rho) | Active (~ alpha*gamma/rho_0 * delta) | Active (~ alpha*gamma) |

**Critical insight:** At the mobility ceiling, only P_SY2 survives. This means:

- In the **parabolic sector**, the only force at the ceiling is -P_SY2, giving drho/dt = -P_SY2. The density is pulled back from the ceiling by the penalty alone.

- In the **oscillatory sector**, the velocity v carries inertia independent of mobility. At the ceiling, dv/dt = (1/tau)(-P_SY2 - zeta*v), which is a damped oscillator driven by the penalty. The density oscillates near the ceiling.

This creates a natural partition:
```
    Bulk (rho << rho_max):  diffusion + penalty + inertia
    Ceiling (rho ~ rho_max): penalty + inertia only
```

---

## 4. Equilibrium and Ground State Energy

### 4.1 Uniqueness of Equilibrium

At equilibrium, drho/dt = 0 and v = 0. From the unified PDE:

```
    0 = D · F[ρ_eq] + H · 0  =>  F[ρ_eq] = 0  (for D > 0)
    0 = (1/τ)(F[ρ_eq] − 0)   =>  F[ρ_eq] = 0  (from v equation)
```

Both equations require F[rho_eq] = 0. For a spatially uniform equilibrium rho_eq = const:
- nabla^2(rho_eq) = 0
- |grad rho_eq|^2 = 0
- F[rho_eq] = -P_SY2(rho_eq)

Setting P_SY2(rho_eq) = 0:
```
    αγ · (ρ_eq − ρ*) / √((ρ_eq − ρ*)² + ρ₀²) = 0
```

The numerator vanishes if and only if rho_eq = rho_star. The denominator is always positive (>= rho_0 > 0).

**Therefore rho = rho_star is the unique uniform equilibrium, independent of D, H, tau, zeta, M_0, and all other parameters.**

### 4.2 Stability

Linearizing around rho_star. Let rho = rho_star + epsilon * delta(x) * exp(sigma*t). The linearized forcing is:

```
    F_lin = M(ρ*) · ∇²δ − P_SY2'(ρ*) · δ
```

For a Fourier mode delta ~ exp(ikx):
```
    F_lin = −K_eff(k) · δ
    K_eff(k) = M(ρ*) · k² + αγ/ρ₀
```

Since M(rho_star) > 0 and alpha*gamma/rho_0 > 0, K_eff(k) > 0 for all k. In the parabolic sector, sigma = -K_eff(k) < 0 (stable). In the oscillatory sector, the eigenvalues are:

```
    σ = −ζ/(2τ) ± √(ζ²/(4τ²) − K_eff(k)/τ)
```

Both roots have Re(sigma) < 0 when zeta > 0. The equilibrium is **linearly stable for all wavenumbers, in all sectors, for all D, H.**

### 4.3 Ground State Energy

The effective potential associated with P_SY2 is:

```
    V(ρ) = αγ · √((ρ − ρ*)² + ρ₀²)
```

This is the integral of P_SY2: dV/drho = P_SY2(rho).

The minimum of V occurs at rho = rho_star:
```
    V(ρ*) = αγ · √(0 + ρ₀²) = αγρ₀
```

The total energy per site in a uniform field at rho_star with v = 0 is:
```
    E_ground = (1/2)·τ·v² + (1/2)·M(ρ*)·|∇ρ|² + V(ρ*)
             = 0 + 0 + αγρ₀
             = αγρ₀
```

At canonical parameters: E_ground = 0.1 * 0.5 * 0.5 = **0.0250**.

### 4.4 Universality of E_ground

The ground state energy depends only on alpha, gamma, and rho_0. It is independent of:
- D and H (dynamical channel mixing)
- tau and zeta (oscillator parameters)
- M_0 and n_mob (mobility parameters)
- rho_max (ceiling)
- grid size, dimensionality, initial conditions

This was confirmed numerically: E_final = 0.0250 across all experiments in ED-Phys-15, 17, and 18 — every regime, every IC, every dimension.

**E_ground = alpha*gamma*rho_0 is a universal invariant of ED cosmology.**

---

## 5. Phase Structure

### 5.1 The D-H Phase Diagram

ED-Phys-18 swept D from 0 to 1 in steps of 0.1 using a 5-peak IC on a 512-site grid (50K steps). The results reveal three regimes:

```
    D ∈ [0.0, 0.1)   OSCILLATORY REGIME
                       15-7 oscillations, 20-64 merges
                       Rich transient structure, ringing relaxation

    D ∈ [0.1, 0.5)   TRANSITIONAL REGIME
                       1-2 oscillations, 5-16 merges
                       Damped oscillatory character

    D ∈ [0.5, 1.0]   PARABOLIC REGIME
                       0 oscillations, 4 merges (= initial peaks)
                       Monotonic relaxation, no ringing
```

### 5.2 Oscillation Death at D_crit = 0.5

The oscillation count drops to zero at D = 0.5. To understand why, consider the linearized hybrid dynamics for a single mode:

```
    dδ/dt = −D · K_eff · δ + H · v
    dv/dt = (1/τ)(−K_eff · δ − ζ · v)
```

The characteristic equation is:

```
    λ² + (ζ/τ + D·K_eff)·λ + (K_eff/τ)(1 + D·τ·K_eff/ζ·...) = 0
```

More precisely, substituting delta ~ exp(lambda*t), v ~ exp(lambda*t):

```
    λ² + (ζ/τ + D·K_eff)·λ + (K_eff/τ + D·ζ·K_eff/τ) = 0
```

The discriminant determines oscillatory vs overdamped:

```
    Δ = (ζ/τ + D·K_eff)² − 4·(K_eff/τ + D·ζ·K_eff/τ)
```

Oscillations occur when Delta < 0. As D increases, the first term (effective damping) grows while the second term (effective spring constant) grows more slowly. At D = D_crit, the system transitions from underdamped to overdamped.

At canonical parameters (tau = 100, zeta = 0.5, K_eff ~ 0.1 for low-k modes):
- D = 0: Delta = (0.005)^2 - 4*(0.001) = -0.004 < 0 (oscillatory)
- D = 0.5: Delta = (0.005 + 0.05)^2 - 4*(0.001 + 0.00025) = 0.003 - 0.005 ~ 0 (critical)
- D = 1.0: Delta > 0 (overdamped)

The D = 0.5 critical point is mode-dependent: low-k modes (small K_eff) are last to lose oscillations, high-k modes (large K_eff) are overdamped first. The observed D_crit = 0.5 reflects the longest-lived (lowest-k) modes.

### 5.3 Absence of Chaos and Bifurcations

The unified PDE has three key properties that prevent chaos:

1. **Energy dissipation:** For the oscillatory sector, dE/dt = -zeta * integral(v^2) dx <= 0. The parabolic sector also dissipates (drho/dt = F[rho] drives rho toward the minimum of V). Neither channel can inject energy.

2. **Unique attractor:** The potential V(rho) has a single minimum at rho_star. There are no secondary minima, saddle points, or limit cycles.

3. **No energy injection:** The system is autonomous (no external driving). Without energy input, the system must relax to the ground state.

These three properties guarantee that the phase diagram is smooth and monotone: increasing D monotonically increases damping, decreases oscillations, and accelerates equilibration. No bifurcations, hysteresis, or chaotic regimes are possible.

---

## 6. Horizon Dynamics

### 6.1 The Mobility Horizon

At rho = rho_max, M(rho_max) = 0. This defines the **mobility horizon**: a boundary beyond which density cannot spread diffusively. The horizon threshold is conventionally set at rho >= 0.9 * rho_max (= 90 at canonical parameters).

### 6.2 Parabolic Horizon Dynamics

In the parabolic sector (D = 1):
```
    ∂ρ/∂t = M(ρ)·∇²ρ + M'(ρ)·|∇ρ|² − P_SY2(ρ)
```

Near the ceiling, M -> 0 and M' -> 0, so:
```
    ∂ρ/∂t ≈ −P_SY2(ρ)
```

The density decays exponentially from the ceiling:
```
    ρ(t) ≈ ρ* + (ρ_max − ρ*)·exp(−P_SY2'(ρ_max)·t)
```

Since P_SY2'(rho) = alpha*gamma*rho_0^2 / ((rho - rho_star)^2 + rho_0^2)^(3/2), at rho = rho_max:
```
    P_SY2'(ρ_max) = αγρ₀² / ((ρ_max − ρ*)² + ρ₀²)^(3/2)
                   = 0.05 · 0.25 / (2500.25)^1.5
                   ≈ 1.0 × 10⁻⁷
```

This is extremely slow. At the ceiling, the parabolic horizon dissolves slowly because P_SY2 saturates (bounded by alpha*gamma = 0.05).

### 6.3 Oscillatory Horizon Dynamics

In the oscillatory sector (D = 0):
```
    ∂ρ/∂t = v
    ∂v/∂t = (1/τ)(−P_SY2(ρ) − ζ·v)     [near ceiling, M ≈ 0]
```

This is a nonlinear oscillator with saturating restoring force. The velocity v has inertia (tau = 100) independent of mobility. Even when diffusion is frozen, the velocity field continues to evolve, pulling density away from the ceiling through oscillatory dynamics.

The oscillatory horizon dynamics has two phases:
1. **Initial overshoot:** v carries density past rho_star (undershoot phase)
2. **Damped return:** Successive oscillations bring density back toward rho_star

ED-Phys-18 measured horizon lifetime = 8 tracking samples for pure oscillatory vs 5 for pure parabolic — a 60% increase. The oscillatory channel sustains horizons longer because:
- The inertial delay (tau = 100) slows the initial retreat from the ceiling
- The density oscillates near the ceiling instead of monotonically retreating

### 6.4 Hybrid Horizon Dynamics

In the hybrid sector, horizon lifetime interpolates linearly between the pure cases:

| D | Horizon Lifetime |
|---|-----------------|
| 0.0 | 8 samples |
| 0.3 | 8 samples |
| 0.4 | 7 samples |
| 0.7 | 6 samples |
| 1.0 | 5 samples |

The transition is gradual, not sharp. At D = 0.4, the parabolic channel is strong enough to reduce horizon persistence by one sample, but the oscillatory channel (H = 0.6) still extends it above the pure parabolic value.

### 6.5 Horizon Size Is IC-Determined

All regimes produce the same maximum horizon extent: 15 sites (for a peak reaching rho = 95 on a 512-site grid). The initial condition determines how much density exceeds the threshold; the dynamics determines how long it persists. This decoupling of extent (IC-dependent) and lifetime (dynamics-dependent) is a clean prediction.

---

## 7. Relaxation Laws

### 7.1 Universal Relaxation to rho_star

Every experiment across ED-Phys-15, 17, and 18 confirmed: all density fields relax to uniform rho = rho_star. The conditions for this are:

1. **V(rho) has a unique minimum at rho_star** (guaranteed by P_SY2 construction)
2. **Dissipation: zeta > 0** (ensures dE/dt <= 0 in oscillatory sector)
3. **D > 0 or zeta > 0** (ensures at least one dissipative channel)

When all three hold, the Lyapunov functional:
```
    E[ρ, v] = ∫ [(τ/2)·v² + (1/2)·M(ρ*)·|∇ρ|² + V(ρ)] dx
```
decreases monotonically, and rho -> rho_star, v -> 0 as t -> infinity.

### 7.2 Relaxation Timescale

The half-life (time for rho_std to halve) varies only 13% across the full D range:

| D | Half-life (steps) | Ratio to D=0 |
|---|-------------------|-------------|
| 0.0 | 1416 | 1.000 |
| 0.5 | 1332 | 0.941 |
| 1.0 | 1236 | 0.873 |

The relaxation rate is dominated by the P_SY2 restoring force, not the dynamical channel. At the linearized level:

**Parabolic rate:** sigma_par = -K_eff(k) where K_eff = M(rho_star)*k^2 + alpha*gamma/rho_0

**Oscillatory rate:** sigma_osc = -zeta/(2*tau) (damping envelope decay)

At canonical parameters:
- sigma_par (k=0) = -alpha*gamma/rho_0 = -0.1
- sigma_osc = -0.5/(2*100) = -0.0025

The parabolic rate for k=0 modes is 40x faster than the oscillatory damping rate. But the observed half-life difference is only 13% because:
1. The overall relaxation involves all k modes, not just k=0
2. Higher-k modes have K_eff >> alpha*gamma/rho_0, making the channel distinction irrelevant
3. The P_SY2 restoring force (alpha*gamma/rho_0 = 0.1 at canonical parameters) sets the effective cosmological clock for the longest-lived k=0 mode

### 7.3 P_SY2 as the Cosmological Clock

The relaxation timescale is set by:
```
    t_relax ~ 1 / (αγ/ρ₀) = ρ₀ / (αγ)
```

At canonical parameters: t_relax ~ 0.5 / 0.05 = 10 time units. In simulation steps (eta ~ 0.12): ~80 steps for one e-folding. The observed half-life (~1300 steps) corresponds to ~16 e-foldings, consistent with the slowest modes requiring multiple relaxation times.

**P_SY2 is the cosmological clock of ED:** it sets the fundamental timescale for universal relaxation, independent of the dynamical channel.

### 7.4 Oscillatory Transient Structure

In the oscillatory sector, the transient contains 8-19 damped oscillations (ED-Phys-17):

| Configuration | Oscillations |
|--------------|-------------|
| Single peak, flat background | 8 |
| Single peak, global oscillation | 10 |
| Single peak, standing wave background | 19 |
| Two peaks, flat | 9 |
| Two peaks, wave background | 13 |

The oscillation count is controlled by:
1. **Q factor:** Q = omega_0 / (2*gamma) = sqrt(K_eff*tau) / zeta. At canonical parameters, Q ranges from 6.3 (low k) to 10.1 (high k). Higher Q = more oscillations before damping.
2. **Background complexity:** Multi-mode backgrounds extend oscillation counts because different modes damp at different rates, sustaining detectable structure longer.
3. **Perturbation amplitude:** Large perturbations produce similar oscillation counts but with larger amplitude swings.

The Q factor is the fundamental predictor. For Q = 6.3 (lowest mode), the number of oscillations before amplitude drops to 1% is:
```
    N_osc ~ Q · ln(A_0/A_min) / π ≈ 6.3 · ln(100) / π ≈ 9
```

This matches the observed 8 oscillations for a single peak on flat background.

---

## 8. Nonlinear Interaction Structure

### 8.1 Mode Coupling

ED-Phys-16 established that nonlinear interactions between modes are weak:
- Coupling coefficient: A_gen / A_parent^2 ~ 0.030
- Triad resonance generates combination modes at k1 +/- k2
- No mode locking (phase drift sigma ~ 2.0 rad)
- Standing waves are stable motifs with 3-6% harmonic generation

### 8.2 Implications for Cosmology

The weak nonlinear coupling means that in ED cosmology:
1. **Modes evolve quasi-independently.** Each Fourier mode of the density field relaxes at its own rate without significant energy exchange with other modes.
2. **No turbulent cascade.** The coupling is too weak to sustain energy transfer across scales. There is no analog of the Kolmogorov cascade.
3. **Structure formation is linear.** The nonlinear corrections (gradient term, mobility modulation, penalty saturation) modify amplitudes by a few percent but do not create qualitatively new physics.

### 8.3 What Would Be Needed for Nonlinear Structure

For persistent nonlinear structure, the ED framework would require:
- Coupling coefficients >> 0.030 (currently ~30x too weak)
- Or multiple competing equilibria (rho_star is unique)
- Or external driving (currently autonomous)
- Or topological constraints (currently smooth periodic boundary)

---

## 9. Cosmological Motifs by Regime

### 9.1 Oscillatory Regime (D < 0.1)

**Character:** Ringing universe. Density oscillates around rho_star with 7-15 height oscillations. Peaks appear and disappear repeatedly. Merging events are frequent (20-64) as peaks oscillate through detection thresholds.

**Motifs:**
- Damped standing participation waves
- Transient peak-basin pairs
- Oscillatory horizon formation and dissolution
- Quasi-periodic structure at omega_0 ~ sqrt(K_eff/tau)

**Timescale:** Relaxation half-life ~ 1416 steps. Oscillation period ~ 200-1000 steps (mode-dependent).

### 9.2 Transitional Regime (0.1 <= D < 0.5)

**Character:** Weakly ringing universe. 1-2 oscillations survive, but the parabolic channel rapidly damps the transients. Merging events are reduced (5-16).

**Motifs:**
- Single overshoot followed by monotonic approach
- Weak oscillatory modulation of diffusive spreading
- Extended horizon lifetimes (oscillatory inertia partially active)

**Timescale:** Half-life ~ 1344-1404 steps (5-10% faster than pure oscillatory).

### 9.3 Parabolic Regime (D >= 0.5)

**Character:** Smooth, monotonic universe. Zero oscillations. Each peak disappears exactly once (merges = initial peak count). No ringing, no transient structure.

**Motifs:**
- Diffusive spreading and absorption into rho_star
- Monotonic horizon retreat
- Smooth, featureless relaxation

**Timescale:** Half-life ~ 1236-1332 steps (~13% faster than pure oscillatory).

---

## 10. The Role of P_SY2 as Architectural Anchor

### 10.1 What P_SY2 Determines

P_SY2 is the single most important term in the unified PDE. It determines:

1. **Equilibrium:** rho_star (unique zero of P_SY2)
2. **Ground state energy:** E_ground = alpha*gamma*rho_0
3. **Relaxation timescale:** t_relax ~ rho_0 / (alpha*gamma)
4. **Oscillation frequency:** omega_0 = sqrt(K_eff/tau), where K_eff includes alpha*gamma/rho_0
5. **Quality factor:** Q = sqrt(K_eff*tau) / zeta, which controls oscillation count
6. **Horizon retreat:** P_SY2 is the only force at the mobility ceiling
7. **Antisymmetry:** Equal treatment of peaks and basins

### 10.2 What P_SY2 Does Not Determine

P_SY2 does not control:
- The dynamical character (oscillatory vs parabolic) — set by D/H
- Nonlinear coupling strength — set by mobility nonlinearity
- Spatial structure formation — set by initial conditions (all structure is transient)
- The horizon extent — set by initial density relative to rho_max

### 10.3 P_SY2 as Universal Attractor

The potential V(rho) = alpha*gamma*sqrt((rho - rho_star)^2 + rho_0^2) has the properties:
- Global minimum at rho_star
- No secondary minima
- Bounded gradient (|P_SY2| < alpha*gamma)
- C-infinity smooth

These properties guarantee universal relaxation. No initial condition, no dynamical channel, no parameter choice (with zeta > 0 or D > 0) can prevent the system from reaching rho = rho_star. The attractor is **global, unique, and inescapable.**

---

## 11. Unified Cosmological Theory: Complete Formulation

### 11.1 The Equations

```
    ∂ρ/∂t = D · [M(ρ)·∇²ρ + M'(ρ)·|∇ρ|² − P_SY2(ρ)] + H · v

    ∂v/∂t = (1/τ) · [M(ρ)·∇²ρ + M'(ρ)·|∇ρ|² − P_SY2(ρ) − ζ·v]

    D + H = 1

    M(ρ) = M₀(1 − ρ/ρ_max)^n_mob

    P_SY2(ρ) = αγ(ρ − ρ*) / √((ρ − ρ*)² + ρ₀²)
```

### 11.2 The Invariants

1. **Equilibrium:** rho = rho_star (unique, global, stable)
2. **Ground state energy:** E_ground = alpha*gamma*rho_0 (universal)
3. **Energy monotonicity:** dE/dt <= 0 (for zeta > 0 or D > 0)
4. **Mass conservation:** d/dt integral(rho) dx = 0 (periodic boundaries, no sources)
5. **Positivity:** rho >= 0 (maintained by clipping; zero clips at canonical parameters)

### 11.3 The Phase Diagram

```
    H = 1.0 ┤ OSCILLATORY: 15 osc, 64 merges, hor_life=8
            │
    H = 0.9 ┤ TRANSITIONAL: 7 osc, 20 merges
            │
    H = 0.8 ┤                2 osc, 16 merges
            │
    H = 0.6 ┤                1 osc,  5 merges, hor_life=7
            │
    H = 0.5 ┤── OSCILLATION DEATH ──────────────────────
            │
    H = 0.4 ┤ PARABOLIC: 0 osc, 4 merges
            │
    H = 0.2 ┤              0 osc, 4 merges, hor_life=6
            │
    H = 0.0 ┤ PURE PARABOLIC: 0 osc, 4 merges, hor_life=5
            └─────────────────────────────────────────
              D = 0        D = 0.5        D = 1.0
```

Three regimes, one transition (D_crit = 0.5), no bifurcations, no chaos.

### 11.4 The Horizon Law

```
    Horizon lifetime ∝ 5 + 3H    (tracking samples)
    Horizon extent   = f(IC)      (independent of dynamics)
```

The oscillatory channel extends horizon persistence through inertial delay, while the parabolic channel accelerates horizon dissolution through direct response.

### 11.5 The Relaxation Law

```
    t_half ≈ 1236 + 180·H    (simulation steps)
    t_relax ~ ρ₀/(αγ)        (fundamental timescale)
    N_osc ~ Q·ln(A₀/A_thresh)/π    (oscillation count)
```

The relaxation timescale is set by P_SY2 (varying only 13% with D/H). The oscillation count is set by Q = sqrt(K_eff*tau)/zeta (ranging from 6.3 to 10.1 across scales).

---

## 12. Implications for Event Density Ontology

### 12.1 ED Has Two Cosmological Sectors

The unified PDE reveals that ED naturally supports two modes of density evolution:

1. **Diffusive sector:** Density responds directly to thermodynamic forces. Irreversible, dissipative, monotonic. Governed by mobility M(rho).

2. **Inertial sector:** Density responds through a velocity field carrying memory. Reversible at short times, oscillatory, eventually dissipative through damping zeta.

Both sectors emerge from the same forcing function F[rho] and the same penalty P_SY2. They are not separate physics but different channels of the same participation architecture.

### 12.2 Hybrid Cosmology Interpolates Cleanly

The mixing parameter D continuously interpolates between sectors without discontinuities, bifurcations, or instabilities. This means the ED framework does not require choosing between parabolic and oscillatory cosmology — both can coexist in the same universe with a tunable mixing ratio.

### 12.3 P_SY2 Defines the Universal Attractor

Regardless of the cosmological sector:
- The equilibrium is rho_star
- The ground state energy is alpha*gamma*rho_0
- All structure is transient

P_SY2 is not merely a restoring force — it is the **ontological anchor** of ED cosmology. It determines what the universe relaxes to, how fast it relaxes, and what energy remains in the ground state.

### 12.4 ED Cosmology Is a Unified Dynamical Architecture

The unified PDE provides a single mathematical framework that:
- Contains parabolic diffusion as a limiting case
- Contains damped wave propagation as a limiting case
- Interpolates smoothly between them
- Preserves stability, positivity, and energy bounds throughout
- Partitions naturally into bulk (diffusion-dominated) and horizon (inertia-dominated) dynamics
- Has a unique, universally attractive equilibrium

This is a complete cosmological architecture: any ED universe, regardless of its D/H ratio, initial conditions, or dimensionality, evolves toward the same ground state through dynamics that are fully determined by the canonical parameters (alpha, gamma, rho_0, M_0, rho_max, tau, zeta).

### 12.5 The Open Question

The unified cosmological theory shows that the P_SY2 oscillator, in all its variants, produces universal relaxation. No persistent structures form. This raises the central question for the next phase of ED physics:

**What additional mechanism — beyond P_SY2 — could sustain persistent density concentrations (proto-particles) against the universal attractor?**

Candidates from the derivation:
1. External driving (energy injection to counterbalance dissipation)
2. Spatial heterogeneity in rho_star (multiple local equilibria)
3. Topological constraints (boundary conditions that trap structure)
4. Stronger nonlinear coupling (beyond the current ~3%)
5. Additional density-dependent terms in the PDE

The unified cosmological equation provides the foundation on which such extensions can be systematically explored.

---

## 13. Quantitative Summary

| Quantity | Value | Source |
|----------|-------|--------|
| Unified PDE | drho/dt = D*F[rho] + H*v | This work |
| Equilibrium | rho = rho_star (unique) | Section 4.1 |
| Ground state energy | E = alpha*gamma*rho_0 = 0.0250 | Section 4.3 |
| Oscillation death | D_crit = 0.5 | Section 5.2 |
| Phase regimes | 3 (oscillatory, transitional, parabolic) | Section 5.1 |
| Bifurcations | 0 | Section 5.3 |
| Horizon lifetime range | 5-8 samples (60% variation) | Section 6.4 |
| Relaxation half-life | 1236-1416 steps (13% variation) | Section 7.2 |
| Cosmological clock | t_relax ~ rho_0/(alpha*gamma) | Section 7.3 |
| Nonlinear coupling | ~0.030 (weak) | Section 8.1 |
| Q factor range | 6.3-10.1 | ED-Phys-15 |
| Oscillation count | 8-19 (config-dependent) | Section 7.4 |
| Positivity clips | 0 (all experiments) | ED-Phys-15/17/18 |

---

## 14. Conclusions

1. The **unified ED cosmology PDE** combines parabolic and oscillatory dynamics through mixing weights D and H (D + H = 1), with both sectors driven by the same forcing function F[rho].

2. **P_SY2 is the architectural anchor:** it determines the unique equilibrium (rho_star), the universal ground state energy (alpha*gamma*rho_0), and the cosmological relaxation timescale (rho_0/(alpha*gamma)).

3. **Three phase regimes** exist: oscillatory (D < 0.1), transitional (0.1 <= D < 0.5), and parabolic (D >= 0.5). The transition at D_crit = 0.5 is smooth with no bifurcations.

4. **Horizons partition naturally:** the bulk is diffusion-dominated (M > 0), while near-ceiling regions are inertia-dominated (M -> 0, but velocity field persists). Horizon lifetime increases 60% with the oscillatory channel.

5. **Relaxation is universal:** all configurations reach rho_star with zero positivity clips. The relaxation rate varies only 13% across the full D range because P_SY2 — not the dynamical channel — sets the cosmological clock.

6. **No persistent structure forms** under any variant of the unified PDE. Universal relaxation is guaranteed by the unique minimum of V(rho), energy dissipation, and absence of external driving.

7. **ED cosmology is a unified dynamical architecture** with a single PDE that continuously interpolates between reversible and irreversible dynamics while preserving stability, positivity, and the universal attractor.

---

## Appendix A: Notation

| Symbol | Meaning |
|--------|---------|
| rho | Event density field |
| rho_star | Equilibrium density (= 50) |
| rho_max | Mobility ceiling / horizon (= 100) |
| rho_0 | Penalty smoothing parameter (= 0.5) |
| v | Participation velocity field |
| tau | Oscillator inertia (= 100) |
| zeta | Damping coefficient (= 0.5) |
| alpha | Penalty amplitude (= 0.1) |
| gamma | Penalty exponent (= 0.5) |
| M_0 | Base mobility (= 1.0) |
| n_mob | Mobility exponent (= 2) |
| D | Parabolic mixing weight |
| H | Oscillatory mixing weight |
| F[rho] | Forcing function: M*Lap + M'*|grad|^2 - P_SY2 |
| V(rho) | Effective potential: alpha*gamma*sqrt((rho-rho_star)^2 + rho_0^2) |
| K_eff(k) | Effective spring constant: M(rho_star)*k^2 + alpha*gamma/rho_0 |
| Q | Quality factor: sqrt(K_eff*tau) / zeta |
| E_ground | Ground state energy: alpha*gamma*rho_0 = 0.0250 |

---

## Appendix B: Derivation of Characteristic Equation

For the linearized hybrid system with a single Fourier mode delta_k ~ exp(lambda*t):

```
    lambda * delta_k = -D * K_eff * delta_k + H * v_k
    lambda * v_k     = (1/tau) * (-K_eff * delta_k - zeta * v_k)
```

From the second equation: v_k = -K_eff * delta_k / (tau * lambda + zeta)

Substituting into the first:
```
    lambda = -D * K_eff - H * K_eff / (tau * lambda + zeta)
    lambda * (tau * lambda + zeta) = -D * K_eff * (tau * lambda + zeta) - H * K_eff
    tau * lambda^2 + zeta * lambda = -D * K_eff * tau * lambda - D * K_eff * zeta - H * K_eff
    tau * lambda^2 + (zeta + D * K_eff * tau) * lambda + K_eff * (D * zeta + H) = 0
```

Since D + H = 1:
```
    tau * lambda^2 + (zeta + D * K_eff * tau) * lambda + K_eff * (D * zeta + 1 - D) = 0
```

Discriminant:
```
    Delta = (zeta + D * K_eff * tau)^2 - 4 * tau * K_eff * (1 - D + D * zeta)
```

Oscillations occur when Delta < 0. At D = 0 (pure oscillatory):
```
    Delta = zeta^2 - 4 * tau * K_eff
```
Which is negative when K_eff > zeta^2 / (4*tau) = 0.25 / 400 = 6.25e-4. Since K_eff >= alpha*gamma/rho_0 = 0.1, this is always satisfied: the pure oscillatory regime is always underdamped.

At D = 1 (pure parabolic):
```
    Delta = (zeta + K_eff * tau)^2 - 4 * tau * K_eff * zeta
          = zeta^2 + 2 * zeta * K_eff * tau + K_eff^2 * tau^2 - 4 * tau * K_eff * zeta
          = (K_eff * tau - zeta)^2
          >= 0
```
Always non-negative: the pure parabolic regime is always overdamped or critically damped.

The critical D where oscillations die is found by setting Delta = 0 and solving for D. This yields a mode-dependent D_crit(k). The global D_crit is the minimum over all k, occurring at the lowest wavenumber.
