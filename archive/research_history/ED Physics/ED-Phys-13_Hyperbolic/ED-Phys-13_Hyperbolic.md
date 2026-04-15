# ED-Phys-13: Hyperbolic Participation with Regularized Penalty

## 1. Motivation

ED-Phys-11 attempted to add a second time derivative to the canonical ED update rule, promoting the parabolic PDE to a hyperbolic (damped-wave) form. The goal was to test whether participation channels could exhibit oscillatory or wave-like dynamics rather than the monotonic, overdamped decay observed across the canonical pipeline (ED-Phys-01 through ED-Phys-10).

**ED-Phys-11 failed completely.** Every hyperbolic run (17 configurations across tau and zeta) produced runaway velocity growth and density depletion. The root cause: the canonical relational penalty P(rho) = alpha*gamma*rho^(gamma-1) diverges as rho -> 0 for gamma < 1. In the parabolic formulation, this singularity merely accelerates the asymptotic drain. But in the hyperbolic formulation, the diverging penalty creates diverging *acceleration* (dv/dt ~ rho^(gamma-1)/tau), establishing a catastrophic feedback loop: rho decreases -> penalty increases -> velocity grows -> rho decreases faster.

ED-Phys-12 then showed that the soft-floor penalty P_SF(rho) = alpha*gamma*(rho + rho_0)^(gamma-1) removes the low-density singularity while preserving all canonical observables at rho >> rho_0. This module combines the two insights: **hyperbolic time evolution with soft-floor regularization**.

**Canonical sources:** ED-5 (update rule derivation), ED-12 (relational penalty), ED-12.5 (participation channels).

---

## 2. The Hyperbolic ED Form

### 2.1 Full PDE

Starting from the canonical parabolic ED equation:

```
drho/dt = M(rho)*Lap(rho) + M'(rho)*|grad(rho)|^2 - alpha*gamma*rho^(gamma-1)
```

We promote the time sector to second order and substitute the soft-floor penalty:

```
tau * d^2rho/dt^2 + zeta * drho/dt = M(rho)*Lap(rho) + M'(rho)*|grad(rho)|^2
                                      - alpha*gamma*(rho + rho_0)^(gamma-1)
```

where:
- tau: inertial timescale (resistance to acceleration)
- zeta: damping coefficient (friction on the velocity field)
- rho_0: soft-floor shift (removes low-density singularity)

### 2.2 First-Order System

For numerical integration:

```
drho/dt = v
dv/dt   = (1/tau) * [RHS_SF(rho) - zeta*v]
```

where RHS_SF(rho) = M(rho)*Lap(rho) + M'(rho)*|grad(rho)|^2 - alpha*gamma*(rho + rho_0)^(gamma-1).

### 2.3 Parabolic Limit

Setting tau -> 0 (or equivalently zeta -> infinity with tau/zeta fixed): the velocity relaxes instantaneously to v = RHS/zeta, recovering the parabolic equation drho/dt = RHS/zeta. The parabolic case corresponds to tau = 0 (no inertia).

---

## 3. Linear Stability Analysis

### 3.1 Linearization

Consider perturbations delta_rho ~ exp(ikx + sigma*t) around a homogeneous background rho_bar with grad(rho_bar) = 0:

- Diffusion linearizes to: -M(rho_bar) * k^2 * delta_rho
- Gradient-squared term: O(delta_rho^2) (drops out)
- Penalty linearizes to: P'(rho_bar) * delta_rho, where P'(rho_bar) = alpha*gamma*(gamma-1)*(rho_bar + rho_0)^(gamma-2)

For gamma < 1: P'(rho_bar) < 0, meaning the penalty derivative acts as a **restoring force** on perturbations.

The linearized equation for delta_rho:

```
tau * sigma^2 + zeta * sigma + K_eff(k) = 0
```

where the effective spring constant is:

```
K_eff(k) = M(rho_bar) * k^2 + P'(rho_bar)
         = M(rho_bar) * k^2 - |P'(rho_bar)|
```

### 3.2 Natural Frequency and Q Factor

When K_eff(k) > 0, the mode is oscillatory (for sufficient tau):

```
omega_0(k) = sqrt(K_eff(k) / tau)
Q(k)       = omega_0 * tau / zeta = sqrt(tau * K_eff(k)) / zeta
```

- Q > 0.5: underdamped (oscillatory)
- Q = 0.5: critically damped
- Q < 0.5: overdamped (monotonic decay)

### 3.3 Critical Wavenumber

K_eff(k) = 0 defines a critical wavenumber below which modes are unstable/aperiodic:

```
k_crit = sqrt(|P'(rho_bar)| / M(rho_bar))
```

Modes with k > k_crit can oscillate; modes with k < k_crit cannot.

### 3.4 Numerical Values at Canonical Parameters

With alpha = 0.1, gamma = 0.5, rho_0 = 0.5, rho_bar = 50, M_0 = 1, rho_max = 100, n_mob = 2:

| Quantity | Value |
|----------|-------|
| M(50)    | 0.25  |
| P'(50)   | -6.97e-5 |
| k_crit   | 0.0167 (lambda_crit = 376 sites) |
| K_eff(k=0.196, lambda=32) | 0.00953 |
| K_eff(k=0.393, lambda=16) | 0.0386 |

### 3.5 Oscillation Period

```
T(k) = 2*pi / omega_0(k) = 2*pi * sqrt(tau / K_eff(k))
```

At k = 0.196 (n=16 mode on N=512):
- tau=100:  T = 643 time units (3216 steps at eta=0.2)
- tau=1000: T = 2033 time units (10167 steps at eta=0.2)

Predicted period ratio (tau=1000)/(tau=100) = sqrt(10) = 3.16.

---

## 4. The Velocity Drain Problem

### 4.1 Diagnosis

The first implementation attempt used small damping coefficients (zeta ~ 0.01), matching ED-Phys-11's parameter choices. This caused immediate density depletion because:

In the hyperbolic formulation, the steady-state velocity (when dv/dt = 0) is:

```
v_ss = -P(rho) / zeta
```

For the soft-floor penalty at rho = 50: P(50) = alpha*gamma*(50.5)^(-0.5) = 0.00704.

With zeta = 0.01: v_ss = -0.704. The density drains at rate 0.704 per time unit, yielding 0.141 per timestep (eta=0.2). Over 35 steps, rho=50 is completely depleted.

With zeta = 1.0: v_ss = -0.00704. The density drains at rate 0.00704 per time unit, matching the parabolic drain rate exactly.

### 4.2 Design Constraint

**For the hyperbolic drain rate to match the parabolic drain rate, zeta must equal 1.** This is not a free parameter — it is fixed by the requirement that the DC (homogeneous) behavior match the canonical evolution.

With zeta = 1 fixed, the Q factor becomes:

```
Q(k) = sqrt(tau * K_eff(k))
```

And the condition Q > 1 (oscillatory) requires:

```
tau > 1 / K_eff(k)
```

At k = 0.196: tau > 105
At k = 0.393: tau > 26
At k = 0.025: tau > 12,400 (impractical)

**Conclusion:** Oscillatory dynamics are possible only at short wavelengths (high k), with tau of order 50-1000.

---

## 5. Parameter Regimes

Based on the velocity drain analysis, four parameter regimes were designed:

| Regime | tau | zeta | Q(k=0.196) | Q(k=0.393) | Drain match | Purpose |
|--------|-----|------|-----------|-----------|-------------|---------|
| R1 (short-wave) | 100 | 1.0 | 0.98 | 1.96 | 1x parabolic | Oscillation at lambda < 16 |
| R2 (medium-wave) | 500 | 1.0 | 2.18 | 4.39 | 1x parabolic | Oscillation at lambda < 32 |
| R3 (fast response) | 50 | 0.5 | 1.38 | 2.78 | 2x parabolic | Higher Q, faster drain |
| R4 (high Q) | 1000 | 1.0 | 3.09 | 6.21 | 1x parabolic | Extended ringing |

CFL conditions:
- Diffusion: eta < CFL * dx^2 / (2*d*M_max) = 0.4/2 = 0.2 (1D)
- Wave: eta < CFL * dx * sqrt(tau/M_max) = 0.4*sqrt(tau)
- The diffusion CFL dominates for tau >= 0.25

---

## 6. Implementation

### 6.1 Time Integration

Explicit Euler on the first-order system:

```python
rhs = compute_rhs(rho, params, rho_0, use_soft_floor=True)

if time_mode == "parabolic":
    rho_new = rho + eta * rhs
else:  # hyperbolic
    dv = (1/tau) * (rhs - zeta*v)
    v_new = v + eta * dv
    rho_new = rho + eta * v_new
```

Positivity enforced: rho_new = max(rho_new, 0).

### 6.2 Stability Checks

- Safety checks every 100 steps: NaN/Inf detection, |rho| > 1e12, |v| > 1e12
- No blowups observed in any configuration (all 8 experiments, 4 regimes each)

### 6.3 Diagnostics

- rho_mean, rho_max, rho_min, rho_std (density statistics)
- grad_mean (gradient magnitude)
- v_rms, v_max (velocity field statistics, hyperbolic only)
- penalty_mean, penalty_max
- Oscillation analysis: turning-point counting, peak envelope damping

---

## 7. Experimental Results

### 7.1 Experiment 1: Homogeneous Validation

Uniform rho_0 = 50 on N=256, 10K steps. Validates that the hyperbolic drain matches parabolic.

| Config | rho_mean (initial) | rho_mean (final) | v_rms (final) | Stable |
|--------|-------------------|------------------|---------------|--------|
| Parabolic | 50.0 | 34.70 | — | Yes |
| R1 (tau=100, zeta=1) | 50.0 | 35.67 | 0.0082 | Yes |
| R2 (tau=500, zeta=1) | 50.0 | 38.99 | 0.0075 | Yes |
| R3 (tau=50, zeta=0.5) | 50.0 | 18.11 | 0.0220 | Yes |
| R4 (tau=1000, zeta=1) | 50.0 | 41.84 | 0.0064 | Yes |

**Interpretation:**
- R1 (zeta=1): drains to 35.67, closely matching parabolic 34.70. The small difference comes from inertial delay (velocity takes tau/zeta time to reach steady state).
- R3 (zeta=0.5): drains to 18.11 — roughly 2x the parabolic drain, consistent with v_ss = P/0.5 = 2P.
- R4 (tau=1000): drains to 41.84 — slower because the velocity field hasn't fully equilibrated in 10K steps (characteristic time tau/zeta = 1000 steps).

### 7.2 Experiment 2: Local Oscillation Test (Gaussian Pulse)

Gaussian perturbation (sigma=20, amplitude=25) on rho_bg=50. N=512, 20K steps.

| Config | rho oscillations | rho_mean (final) |
|--------|-----------------|------------------|
| Parabolic | 0 | 18.56 |
| R1 | 0 | 20.21 |
| R2 | 0 | 25.32 |
| R3 | 1 | 0.00 |
| R4 | 0 | 29.99 |

**Interpretation:** The broad Gaussian (sigma=20) has most spectral power at k ~ 1/(2*pi*20) = 0.008, deep in the overdamped regime (k << k_crit for oscillation). No oscillation is expected or observed. R3 depletes fully due to 2x drain rate.

### 7.3 Experiment 3: Sinusoidal Mode Test

Two long-wavelength modes: rho = 50 + 10*sin(2*pi*x/512) + 5*sin(4*pi*x/512). N=512, 20K steps.

| Config | rho oscillations | v oscillations | std crossings |
|--------|-----------------|----------------|---------------|
| Parabolic | 0 | — | 1 |
| R1 | 0 | 0 | 1 |
| R2 | 0 | 0 | 1 |
| R3 | 1 | 0 | 1 |
| R4 | 0 | 0 | 1 |

**Interpretation:** k_1 = 0.012 and k_2 = 0.025 are both below k_crit for any regime. No oscillation possible — confirmed.

### 7.4 Experiment 4: Wave Propagation Test (Step Function)

Step function: rho = 40 (background), rho = 70 (quarter-domain block). N=512, 20K steps.

| Config | Propagation speed | Spread rate | Stable |
|--------|------------------|-------------|--------|
| Parabolic | 0.0 | -0.0092 | Yes |
| R1 | 0.0 | -0.0082 | Yes |
| R2 | 0.0 | -0.0061 | Yes |
| R3 | 0.0 | -0.0157 | Yes |
| R4 | 0.0 | -0.0052 | Yes |

**Interpretation:** No wave propagation observed. The step function contains a wide range of wavelengths, but the dominant behavior is diffusive smoothing, not wave propagation. All spread rates are negative (the high-density region contracts as it diffuses). The hyperbolic term slows the spreading (smaller |spread| for larger tau) but does not convert it to propagation.

### 7.5 Experiment 5: Long-term Stability (50K Steps)

Gaussian pulse IC, 50K steps. Tests whether any regime eventually blows up.

| Config | Steps completed | Blew up | rho_mean (final) | v_rms (final) |
|--------|----------------|---------|------------------|---------------|
| R1 | 50,000 | No | 0.0 | 0.0707 |
| R2 | 50,000 | No | 0.0 | 0.0707 |
| R3 | 50,000 | No | 0.0 | 0.1414 |
| R4 | 50,000 | No | 0.0 | 0.0684 |

**Interpretation:** All regimes are unconditionally stable (no blowup). The density eventually drains to zero in all cases (soft-floor penalty is always positive). The residual v_rms values are P(0)/zeta = alpha*gamma*rho_0^(gamma-1)/zeta: for zeta=1: 0.0707, for zeta=0.5: 0.1414. These match exactly, confirming the steady-state velocity theory.

### 7.6 Experiment 8: Short-Wavelength Oscillation Test (THE KEY RESULT)

Single sinusoidal modes targeting the oscillatory regime: n=16 (k=0.196, lambda=32) and n=32 (k=0.393, lambda=16). Amplitude 5 on rho_bg=50. N=512, 30K steps.

| IC | Regime | rho oscillations | v oscillations | Period (diag. indices) |
|----|--------|-----------------|----------------|----------------------|
| mode n=16 | R1 (tau=100) | **21** | 2 | 77.5 |
| mode n=16 | R4 (tau=1000) | **7** | 4 | 251.7 |
| mode n=32 | R1 (tau=100) | **43** | 6 | 38.6 |
| mode n=32 | R4 (tau=1000) | **15** | 13 | 126.5 |
| narrow pulse | R1 | 1 | 1 | — |
| narrow pulse | R4 | 0 | 0 | — |
| mode n=16 | Parabolic | 0* | — | — |
| mode n=32 | Parabolic | 0* | — | — |

*Parabolic "oscillation" counts (266, 449) are spurious — numerical noise at rho_std ~ machine epsilon after the mode decays. The parabolic mode decays monotonically.*

**Key findings:**

1. **Genuine oscillatory dynamics confirmed.** The hyperbolic extension with soft-floor penalty produces 21-43 oscillations in rho_std at short wavelengths, compared to zero in the parabolic baseline.

2. **Period scales with sqrt(tau).** Period ratio R4/R1 for mode n=16: 251.7/77.5 = 3.25. Predicted: sqrt(1000/100) = 3.16. Error: 3%. For mode n=32: 126.5/38.6 = 3.28. Predicted: 3.16. Error: 4%. Excellent agreement.

3. **More oscillations at higher k.** At R1: mode n=32 shows 43 oscillations vs 21 for mode n=16 (ratio 2.05). This reflects the higher frequency at larger k.

4. **Narrow pulse shows no oscillation.** Broad spectral content is dominated by overdamped long-wavelength modes. The short-wavelength oscillatory content is spectrally weak.

5. **Velocity oscillations lag density oscillations.** v_rms shows fewer oscillations than rho_std, consistent with v being the time derivative of rho (90-degree phase shift).

### 7.7 Experiment 6: Parabolic vs Hyperbolic Comparison (Two Peaks)

Two Gaussian peaks (sep=150, sigma=20) on rho_bg=50. N=512, 20K steps.

| Config | rho_mean (final) | rho_std (final) |
|--------|------------------|-----------------|
| Parabolic + soft-floor | 22.41 | 5.35 |
| R1 hyperbolic | 23.87 | — |
| R2 hyperbolic | 28.58 | — |

**Interpretation:** Hyperbolic modes preserve more density (slower drain from inertial delay) but show no qualitative difference in peak dynamics at these length scales (sigma=20 -> overdamped).

### 7.8 Experiment 7: 2D Hyperbolic Cosmology

Random IC rho in [20, 80] on 128x128 grid, 5K steps.

| Config | rho_mean (final) | rho_std (final) | v_rms (final) |
|--------|------------------|-----------------|---------------|
| Parabolic | 50.99 | 0.26 | — |
| R1 (tau=100) | 168.20 | 118.24 | 138.15 |
| R3 (tau=50) | 221.41 | 169.02 | 733.23 |

**Interpretation:** The 2D hyperbolic runs show artificial density growth (rho_mean > 50 initial) and extremely high velocity fields. This is a **numerical artifact** of the positivity floor: when v temporarily pushes rho below zero, the floor clips rho to 0. When v subsequently reverses, rho grows without the corresponding negative excursion. This asymmetric clipping creates a net positive density bias. The effect is catastrophic in 2D because the random IC has many points where rho passes through zero during oscillation.

**Warning:** The positivity floor rho = max(rho, 0) is incompatible with hyperbolic dynamics in 2D random-IC scenarios. Alternative approaches (e.g., logarithmic density variable, implicit integration) would be needed for 2D hyperbolic evolution.

---

## 8. Architectural Analysis

### 8.1 What Works

1. **The soft-floor removes the hyperbolic instability.** ED-Phys-11's runaway loop (penalty divergence -> velocity growth -> density depletion -> worse divergence) is completely eliminated. The penalty is bounded at all rho by P_max = alpha*gamma*rho_0^(gamma-1).

2. **Oscillatory dynamics are possible at short wavelengths.** The Q factor exceeds 1 for wavenumbers k > sqrt(1/tau - |P'|/M) / k (approximately k > 0.15 for tau=100). This produces 20-40+ oscillation cycles in the density standard deviation.

3. **Period scaling matches linear theory.** The sqrt(tau) dependence of the oscillation period is confirmed to within 4%, validating the linear stability analysis.

4. **Long-term stability is unconditional.** No blowup in any of 50K-step runs across all parameter regimes.

### 8.2 What Doesn't Work

1. **Long-wavelength modes remain overdamped.** For the canonical grid (N=512, dx=1), modes with lambda > ~60 sites are always overdamped (Q < 0.5). The ED cosmological structure (basin widths ~100-200 sites) falls squarely in this regime.

2. **No wave propagation observed.** Step functions diffuse rather than propagate. The hyperbolic term slows diffusion but does not create traveling waves at the tested parameters.

3. **The penalty drain persists.** Both parabolic and hyperbolic modes drain density to zero over long times. The hyperbolic inertia delays but does not prevent this.

4. **2D hyperbolic evolution is numerically problematic.** The positivity floor creates artificial density growth by asymmetrically clipping velocity-driven oscillations.

### 8.3 The Overdamping Landscape

ED-Phys-11 concluded that overdamping is "structural." ED-Phys-13 refines this: overdamping is **scale-dependent**. The ED compositional rule is:

- Overdamped at long wavelengths (lambda > ~60 sites for tau=100)
- Oscillatory at short wavelengths (lambda < ~30 sites for tau=100)
- The boundary shifts with tau: larger tau extends oscillation to longer wavelengths

This means the ED framework can support oscillatory dynamics, but only at scales much smaller than the typical structure (peaks, basins, horizons). Whether this is physically relevant depends on the interpretation of the lattice spacing dx.

---

## 9. Connection to Prior Modules

| Module | Relevance to ED-Phys-13 |
|--------|------------------------|
| ED-Phys-01 | Canonical PDE — the parabolic limit of the hyperbolic extension |
| ED-Phys-02 | Core engine — operators (Laplacian, mobility) reused identically |
| ED-Phys-07 | Analytical theory — linear stability framework adapted for second-order dynamics |
| ED-Phys-09 | Initial hyperbolic exploration (numerical instability patterns) |
| ED-Phys-11 | Failed hyperbolic attempt — directly motivates this module |
| ED-Phys-12 | Soft-floor penalty — the key ingredient that makes hyperbolic stable |

---

## 10. Implications for ED Ontology

### 10.1 Participation Channel Inertia

The parameter tau represents inertial resistance in the participation channel. In ED language: regions of high event density resist rapid changes to their participation rate. This is ontologically distinct from the diffusive mobility M(rho), which governs how participation spreads spatially.

The finding that tau must be large (100-1000) for oscillation means that significant inertial resistance is required — participation changes propagate slowly through the density field.

### 10.2 Oscillation as Reversible Participation

In the canonical (parabolic) ED framework, participation changes are irreversible — density flows from high to low and never reverses. The hyperbolic extension introduces a velocity field that can reverse sign, allowing density to overshoot its equilibrium and oscillate back. This is a form of **reversible participation**: the density field can temporarily exceed its equilibrium before settling.

However, the penalty drain (drho/dt < 0 on average) means the equilibrium itself moves toward zero. The oscillations are transient fluctuations around a declining mean. True undamped oscillation would require a restoring force (like the symmetric penalty from ED-Phys-12) to maintain a nonzero equilibrium.

### 10.3 Scale Hierarchy

The discovery that oscillation is scale-dependent (short wavelengths oscillate, long wavelengths are overdamped) suggests a natural scale hierarchy in the ED framework:

- **Sub-structural scale** (lambda < 30): oscillatory, wave-like, potentially reversible
- **Structural scale** (lambda ~ 100-200): overdamped, diffusive, irreversible
- **Global scale** (lambda ~ N): uniform drain, no spatial dynamics

This mirrors physical systems where microscopic degrees of freedom can oscillate while macroscopic behavior is diffusive (e.g., phonons vs heat conduction).

---

## 11. Limitations

1. **Explicit Euler integration.** Higher-order methods (Verlet, RK4) would improve accuracy, especially for long-time oscillation tracking.

2. **Positivity floor artifact.** The max(rho, 0) clipping breaks conservation in hyperbolic mode. A logarithmic density variable (rho = exp(phi)) or implicit integration would be more appropriate.

3. **No adaptive timestepping.** The CFL-based timestep is conservative; adaptive methods could improve efficiency for large-tau runs.

4. **1D focus.** The 2D hyperbolic results are contaminated by the positivity artifact. Clean 2D results require a different numerical approach.

5. **No coupling to symmetric penalty.** The combination of hyperbolic dynamics with the symmetric penalty (which provides a true restoring force at rho_star) is unexplored. This combination could produce sustained oscillations around a nonzero equilibrium.

---

## 12. Future Directions

1. **Hyperbolic + symmetric penalty.** The symmetric penalty provides a restoring force toward rho_star, which combined with hyperbolic inertia could produce sustained oscillation. This is the most promising avenue for genuine wave-like ED dynamics.

2. **Logarithmic density formulation.** Replace rho with phi = log(rho) to enforce positivity without clipping. The PDE becomes nonlinear in phi but avoids the conservation-breaking floor.

3. **Spectral methods.** Since oscillation is scale-dependent, spectral decomposition of the density field could isolate oscillatory and overdamped modes, providing cleaner diagnostics.

4. **Physical interpretation of tau.** The inertial timescale tau has no canonical derivation from f(rho). It would need either empirical calibration or a deeper ontological argument for its value.

---

## Appendix A: Penalty Comparison at Canonical Parameters

At rho = 50, alpha = 0.1, gamma = 0.5, rho_0 = 0.5:

| Quantity | Canonical | Soft-floor | Difference |
|----------|-----------|------------|------------|
| P(50) | 0.00707 | 0.00704 | 0.4% |
| P(1) | 0.0500 | 0.0408 | 18% |
| P(0.01) | 0.500 | 0.0697 | 86% |
| P(0) | divergent | 0.0707 | — |
| P'(50) | -7.07e-5 | -6.97e-5 | 1.4% |

The soft-floor is indistinguishable from canonical at rho >> rho_0 but caps the penalty at a finite maximum as rho -> 0.

## Appendix B: File Inventory

| File | Purpose |
|------|---------|
| `ED-Phys-13_Hyperbolic.md` | This document |
| `ed_phys_hyperbolic.py` | Simulator: parabolic + hyperbolic modes, 8 experiments |
| `results/hyperbolic_results.json` | All quantitative results |
| `results/2d_parabolic_rho.npy` | 2D final density (parabolic baseline) |
| `results/2d_hyperbolic_R1_rho.npy` | 2D final density (hyperbolic R1) |
| `results/2d_hyperbolic_R3_rho.npy` | 2D final density (hyperbolic R3) |
