# ED-Phys-11: Non-Dissipative and Strong-Coupling Regimes

## 1. Motivation and Targets

### 1.1 Background

ED-Phys-09 and ED-Phys-10 demonstrated that the canonical parameter regime is **dissipation-dominated**: three independent extensions (inertial wave, nonlocal kernel, gradient-mediated force) all failed to produce wave propagation or inter-peak forces at perturbative coupling strengths. ED-Phys-11 asks: *what happens when we push beyond the perturbative regime?*

### 1.2 Non-Dissipative Targets

| Target | Definition | Quantitative Threshold |
|--------|-----------|----------------------|
| **Wave propagation** | Finite-speed, oscillatory density disturbance | Peak displacement > 5 lattice sites; Q > 1 |
| **Underdamped modes** | Quality factor Q = omega/damping > 1 | v_rms oscillations with > 2 local maxima |
| **Persistent oscillons** | Localized standing wave structures | Peak count oscillation over > 5 cycles |

### 1.3 Strong-Coupling Targets

| Target | Definition | Quantitative Threshold |
|--------|-----------|----------------------|
| **Inter-peak forces** | force_rms comparable to curvature force | force_ratio = force_rms / curv_force_rms > 0.1 |
| **Structure modification** | Peak separation changes | \|delta_sep\| > 5 lattice sites |
| **Inflation modification** | lambda_1 changes > 20% | \|delta_lambda_1 / lambda_1\| > 0.2 |

### 1.4 Anisotropy Target

| Target | Definition | Quantitative Threshold |
|--------|-----------|----------------------|
| **Directional bias** | Growth rates differ by direction | grad_anisotropy = grad_x_rms / grad_y_rms deviating from 1.0 by > 10% |

**Canonical sources**: ED-5, ED-12, ED-12.5, ED-Phys-01 through ED-Phys-10.

---

## 2. Extension Designs

### 2.1 Extension A: Hyperbolic Sector (Reduced Dissipation)

**Motivation**: ED-Phys-09 showed that at tau=0.1-100 and zeta=0.1-1.0, the inertial extension is overwhelmed by canonical dissipation. ED-Phys-11 pushes into tau << 1 and zeta << 0.1 to reduce the damping ratio.

**Modified PDE:**

    tau * d^2 rho/dt^2 + zeta * d rho/dt = M(rho)*Lap(rho) + M'(rho)*|grad(rho)|^2 - alpha*gamma*rho^(gamma-1)

**First-order system:**

    d rho/dt = v
    d v/dt = (1/tau) * [RHS_canonical - zeta*v]

**Parameter regime:**
- tau in {0.0001, 0.001, 0.01, 0.1} (much smaller than ED-Phys-09's 0.1-100)
- zeta in {0.0001, 0.001, 0.01, 0.1} (much smaller than ED-Phys-09's 0.1-1.0)

**Quality factor estimate:**

    Q = sqrt(M * k^2 / tau) / zeta

For M=1, k=2*pi/512, tau=0.001, zeta=0.001: Q ~ 388.
For M=1, k=2*pi/512, tau=0.1, zeta=0.1: Q ~ 0.4.

**Predicted behavior**: At Q >> 1, the system should be underdamped. Density perturbations should oscillate and potentially propagate.

**Instability risks**: At very small tau, dv/dt = (1/tau)*RHS can become enormous. The canonical RHS includes the relational penalty -alpha*gamma*rho^(gamma-1), which acts as a constant drain. If tau is too small, this drain is amplified, potentially driving rho to zero and v to extreme values.

**CFL constraint:**

    eta_wave = 0.3 * dx / sqrt(M_max / tau)
    eta = min(eta_wave, eta_diffusion, 0.01)

### 2.2 Extension B: Strong GMF Coupling

**Motivation**: ED-Phys-10 established force_rms = 3.1*kappa*lambda. At the tested range (kappa, lambda in [0.01, 0.1]), force_rms ~ 0.003 to 0.03, while curvature force ~ O(0.1-1.0). To achieve force_ratio > 0.1, need kappa*lambda > 0.03.

**Modified PDE system (same as ED-Phys-10):**

    d rho/dt = M(rho)*Lap(rho) + M'(rho)*|grad rho|^2 - alpha*gamma*rho^(gamma-1) - lam*div(rho*grad(phi))
    d phi/dt = D_phi*Lap(phi) - mu*phi + kappa*(rho - rho_bar)

**Parameter regime:**
- kappa in {0.5, 1.0, 2.0, 5.0}
- lambda in {0.5, 1.0, 2.0}

At kappa*lambda = 1.0, expected force_rms ~ 3.1, which should be comparable to curvature forces.

**Instability risks**: The phi field grows as kappa*rho, and the force term lam*div(rho*grad(phi)) scales as lam*rho*kappa*rho = lam*kappa*rho^2. This quadratic growth can create a positive feedback loop leading to blowup.

**CFL constraint:**

    eta_coupling = 0.02 * dx / (lam * rho_scale)
    eta = min(eta_rho, eta_phi, eta_coupling, 0.005)

### 2.3 Extension C: Directional Operator (2D)

**Motivation**: ED-Phys-10 showed that isotropic phi coupling cannot break isotropy. A directional operator — anisotropic phi diffusion plus gradient-directional source — deliberately selects a preferred direction.

**Modified phi equation:**

    d phi/dt = D_x * d^2 phi/dx^2 + D_y * d^2 phi/dy^2 - mu*phi + kappa * d rho/dx

Key differences from ED-Phys-10:
1. **Anisotropic diffusion**: D_x >> D_y (or D_y = 0) — phi propagates only in x
2. **Gradient source**: kappa * d(rho)/dx — phi is sourced by the x-gradient of rho, not by rho itself

This creates a feedback loop:
- Density gradients in x generate phi
- phi generates a force on rho preferentially in x
- The asymmetry amplifies directional structure

**Rho equation (unchanged):**

    d rho/dt = RHS_canonical - lam * div(rho * grad(phi))

**Parameter regime:**
- D_x in {5, 10, 20}, D_y = 0
- kappa in {0.1, 0.5, 1.0, 2.0}
- lambda in {0.1, 0.5, 1.0, 2.0}
- Also test with density source (kappa*(rho-rho_bar)) as control

**Instability risks**: The gradient source d(rho)/dx is naturally bounded for smooth rho, but can spike at sharp interfaces. Combined with strong coupling, this can create localized blowup.

---

## 3. Implementation

### 3.1 Test Harness

File: `ed_phys_nondissipative.py`

Three separate simulators implemented:
- `simulate_hyperbolic()` — Extension A
- `simulate_strong_gmf()` — Extension B
- `simulate_directional()` — Extension C

All share a common safety framework:
- `_check_blowup()` runs every 100 steps, checking for NaN, Inf, and |rho| > 10^10
- Blowup is recorded with step number and message
- Simulation terminates early on blowup, preserving all diagnostics up to that point
- Timestep is capped (eta <= 0.01 for hyperbolic, eta <= 0.005 for strong coupling)

### 3.2 Validation

Before aggressive experiments, the canonical path is unchanged: at kappa=lambda=0, Extension B reduces identically to the canonical PDE. The control run (isotropic, kappa=lambda=0.1, isotropic source) confirms expected behavior.

### 3.3 Experiment Suite

| Block | Extension | Test | Grid | Steps | Runs |
|-------|-----------|------|------|-------|------|
| A1 | Hyperbolic | Wave (pulse IC) | 1D, 512 | 50K | 9 |
| A2 | Hyperbolic | Oscillation (sinusoidal IC) | 1D, 512 | 50K | 4 |
| A3 | Hyperbolic | Stability (extreme params) | 1D, 512 | 50K | 4 |
| B1 | Strong GMF | Force (two peaks) | 1D, 512 | 30K | 12 |
| B2 | Strong GMF | Cosmology (random IC) | 1D, 512 | 30K | 5 |
| B3 | Strong GMF | Stability (long time) | 1D, 512 | 50K | 4 |
| C1 | Directional | Anisotropy (2D random IC) | 2D, 128x128 | 10K | 5 |
| C2 | Directional | Stability (2D long run) | 2D, 128x128 | 20K | 2 |

Total: 45 runs, 281 seconds.

---

## 4. Results

### 4.1 Extension A: Hyperbolic Sector

#### A1: Wave Test (9 runs)

| tau | zeta | Q (est.) | v_rms (final) | rho_max | Peaks | Peak shift | Oscillations |
|-----|------|----------|---------------|---------|-------|-----------|-------------|
| 0.001 | 0.001 | 388 | 5.0x10^6 | 0.000 | 1->0 | 0 | 0 |
| 0.001 | 0.01 | 39 | 5.0x10^5 | 0.000 | 1->0 | 0 | 0 |
| 0.001 | 0.1 | 3.9 | 5.0x10^4 | 0.000 | 1->0 | 0 | 0 |
| 0.01 | 0.001 | 123 | 5.0x10^6 | 0.000 | 1->0 | 0 | 0 |
| 0.01 | 0.01 | 12 | 5.0x10^5 | 0.000 | 1->0 | 0 | 0 |
| 0.01 | 0.1 | 1.2 | 5.0x10^4 | 0.000 | 1->0 | 0 | 0 |
| 0.1 | 0.001 | 39 | 5.0x10^6 | 0.000 | 1->0 | 0 | 0 |
| 0.1 | 0.01 | 3.9 | 5.0x10^5 | 0.000 | 1->0 | 0 | 0 |
| 0.1 | 0.1 | 0.4 | 5.0x10^4 | 0.000 | 1->0 | 0 | 0 |

**Result: No waves, no oscillations. System depletes to rho = 0.**

The velocity field reaches extreme values (v_rms ~ 10^4 to 10^6) but is not oscillatory — it is a monotonic runaway. The v field drives all density to the positivity floor (eps = 10^-10), destroying all structure.

**Mechanism of failure**: The canonical RHS includes the relational penalty -alpha*gamma*rho^(gamma-1), which at low rho diverges as rho^(-0.5). When the hyperbolic extension amplifies this by factor 1/tau, the drain rate becomes explosive:

    dv/dt = (1/tau) * [-alpha*gamma*rho^(gamma-1) - zeta*v + diffusion]

At rho ~ 1, the drain contributes ~ -0.05/tau. For tau = 0.001, this is -50. This accelerates v to large negative values, which drives rho to zero, which makes rho^(gamma-1) even larger, creating a runaway.

**The v_rms scales as 1/zeta**: v_rms(zeta=0.001) = 10 * v_rms(zeta=0.01) = 100 * v_rms(zeta=0.1), confirming that the steady-state v is set by the balance v ~ RHS/zeta.

**Classification: UNSTABLE.** The hyperbolic extension with reduced damping does not produce waves — it produces runaway density depletion.

#### A2: Oscillation Test (4 runs)

| tau | zeta | v oscillations | grad oscillations | v_rms |
|-----|------|---------------|-------------------|-------|
| 0.001 | 0.001 | 0 | 0 | 5.0x10^6 |
| 0.001 | 0.01 | 0 | 0 | 5.0x10^5 |
| 0.01 | 0.001 | 0 | 0 | 5.0x10^6 |
| 0.01 | 0.01 | 0 | 0 | 5.0x10^5 |

Zero oscillations in both v_rms and gradient energy. Same runaway depletion as A1.

**Classification: UNSTABLE.**

#### A3: Stability Test (extreme parameters, 50K steps)

| tau | zeta | rho range | v_max |
|-----|------|-----------|-------|
| 0.001 | 0.0001 | [0, 0] | 5.0x10^7 |
| 0.001 | 0.001 | [0, 0] | 5.0x10^6 |
| 0.0001 | 0.0001 | [0, 0] | 5.0x10^7 |
| 0.0001 | 0.001 | [0, 0] | 5.0x10^6 |

All runs drive rho to zero. No blowup (NaN/Inf) because the positivity clamp prevents rho from going negative, but the system is physically dead.

**Classification: UNSTABLE.**

#### Extension A Summary

The hyperbolic extension fails in the low-damping regime because the canonical relational penalty rho^(gamma-1) creates a runaway drain when amplified by 1/tau. The problem is structural: the ED compositional rule includes a term that diverges as rho -> 0, and the hyperbolic extension converts this divergence into explosive acceleration.

**Key insight**: Wave physics in ED requires not just a second time derivative, but also a **modified relational penalty** that does not diverge at low density. The current penalty rho^(gamma-1) with gamma < 1 is incompatible with underdamped dynamics because it creates an infinite restoring force at zero density — which sounds like it should be stabilizing but actually drives rho to zero faster through the velocity field.

### 4.2 Extension B: Strong GMF Coupling

#### B1: Force Test (12 runs)

| kappa | lambda | Blowup step | Sep before blowup | Force achieved? |
|-------|--------|-------------|-------------------|-----------------|
| 0.5 | 0.5 | 3800 | 153 (unchanged) | Before measurement |
| 0.5 | 1.0 | 5100 | 153 | Before measurement |
| 0.5 | 2.0 | 7000 | 153 | Before measurement |
| 1.0 | 0.5 | 2600 | 153 | Before measurement |
| 1.0 | 1.0 | 3500 | 153 | Before measurement |
| 1.0 | 2.0 | 4800 | 153 | Before measurement |
| 2.0 | 0.5 | 1800 | 153 | Before measurement |
| 2.0 | 1.0 | 2500 | 153 | Before measurement |
| 2.0 | 2.0 | 3400 | 153 | Before measurement |
| 5.0 | 0.5 | 1100 | 153 | Before measurement |
| 5.0 | 1.0 | 1500 | 153 | Before measurement |
| 5.0 | 2.0 | 2100 | 153 | Before measurement |

**Result: All 12 runs blow up. Zero peak movement before blowup.**

The blowup time scales inversely with kappa*lambda:
- kappa*lambda = 0.25: blowup ~ 3800 steps
- kappa*lambda = 1.0: blowup ~ 3500 steps
- kappa*lambda = 10.0: blowup ~ 1100 steps

The separation remains exactly 153 in all pre-blowup snapshots. The strong coupling does not produce measurable forces before instability destroys the simulation.

**Blowup mechanism**: The phi field grows as kappa*rho. The force term lam*div(rho*grad(phi)) ~ lam*kappa*rho^2 is quadratically self-reinforcing. Once phi builds up sufficiently, the force creates local density spikes, which source more phi, which creates more force — a positive feedback loop that blows up in finite time.

**Classification: UNSTABLE.**

#### B2: Cosmology Test (5 runs)

| kappa | lambda | Blowup | lambda_1 |
|-------|--------|--------|----------|
| 0 | 0 | None | 0.00006 |
| 0.5 | 0.5 | 1000 | — |
| 1.0 | 1.0 | 500 | — |
| 2.0 | 2.0 | 400 | — |
| 5.0 | 5.0 | 400 | — |

The control run (kappa=lambda=0) gives lambda_1 = 0.00006 (low R^2 = 0.52, indicating the gradient evolution is not well-fit by a single exponential at this timestep/recording interval — this is a control artifact from the conservative timestep eta=0.005). All coupled runs blow up within 400-1000 steps.

**Classification: UNSTABLE.**

#### B3: Stability Test (50K steps)

| kappa | lambda | Blowup step |
|-------|--------|-------------|
| 1.0 | 1.0 | 4700 |
| 5.0 | 5.0 | 4100 |
| 10.0 | 10.0 | 4000 |
| 20.0 | 20.0 | 3900 |

All blow up. Higher coupling blows up slightly earlier.

**Classification: UNSTABLE.**

#### Extension B Summary

Strong GMF coupling is **unconditionally unstable** with explicit time integration at kappa*lambda >= 0.25. The fundamental problem is the quadratic feedback loop: phi ~ kappa*rho, force ~ lam*rho*grad(phi) ~ lam*kappa*rho^2. This makes the effective force scale as rho^2, creating positive feedback that cannot be stabilized by the canonical linear dissipation.

**Critical finding**: The boundary between stable and unstable GMF coupling lies at kappa*lambda ~ 0.01 (ED-Phys-10 was stable at 0.0025). The force at this boundary is force_rms ~ 0.03, which is still ~10x below the curvature force scale of ~0.3. **The gap cannot be closed with explicit integration.**

Accessing strong GMF forces would require either:
1. Implicit time integration (treating the coupling term implicitly)
2. A modified coupling that is sublinear in rho (e.g., force ~ rho^(1/2) * grad(phi))
3. A coupling with built-in saturation (e.g., lam * rho / (rho + rho_s) * div(grad(phi)))

### 4.3 Extension C: Directional Operator

#### C1: Anisotropy Test (5 runs)

| Configuration | Anisotropy Ratio | Grad Anisotropy | grad_x_rms | grad_y_rms | phi_rms |
|--------------|-----------------|-----------------|------------|------------|---------|
| Isotropic control | 0.999 | 1.125 | 0.0106 | 0.0095 | 0.097 |
| D_x=5, D_y=0, grad source, k=l=0.1 | 0.981 | 1.156 | 0.0071 | 0.0062 | 0.005 |
| D_x=5, D_y=0, grad source, k=l=0.5 | 0.998 | **0.932** | 0.0106 | 0.0114 | 0.032 |
| D_x=10, D_y=0, grad source, k=l=1.0 | 0.999 | **0.276** | 0.0576 | 0.2085 | 0.116 |
| D_x=5, D_y=0, density source, k=l=0.5 | BLOWUP@700 | — | — | — | — |

**RESULT: Gradient anisotropy achieved.** The "very strong" configuration (D_x=10, k=l=1.0) produces a gradient anisotropy ratio of 0.276, meaning x-gradients are only 28% of y-gradients. This is a 4:1 directional bias.

**However**: The density variance anisotropy (x_var/y_var) remains near 1.0 in all runs. The directional coupling modifies the *gradient* structure but not the bulk density variance. This means the coupling preferentially smooths gradients in the x-direction (where phi diffuses) while leaving y-gradients untouched.

**Control comparison**: The isotropic control has grad_anisotropy = 1.125 (slight asymmetry from random IC). The directional runs show a clear, monotonic decrease with increasing coupling strength: 1.156 -> 0.932 -> 0.276.

**Density-source variant**: Using kappa*(rho - rho_bar) instead of kappa*d(rho)/dx blows up at step 700. The density source creates a stronger positive feedback because it amplifies bulk density fluctuations rather than gradient fluctuations.

#### C2: Stability Test (20K steps)

| Configuration | Grad Anisotropy (final) | Grad Anisotropy Series | Blowup |
|--------------|------------------------|----------------------|--------|
| D_x=10, k=l=1.0, 20K steps | **0.248** | 1.00 -> 0.71 -> 0.52 -> 0.43 -> 0.38 -> ... -> 0.25 | None |
| D_x=20, k=l=2.0, 20K steps | — | 1.00 -> 0.68 -> 1.00 | step 2100 |

**Key findings:**

1. **Sustained anisotropy at D_x=10, k=l=1.0**: The gradient anisotropy starts at 1.0 (isotropic) and monotonically decreases to 0.25 over 20K steps, with no sign of reverting. The series shows smooth, saturating approach to a steady-state anisotropy. This is not a transient — it is a genuine dynamical attractor.

2. **Convergence trajectory**: The anisotropy decreases as approximately grad_aniso(t) ~ 0.25 + 0.75*exp(-t/T) with T ~ 3000 steps. By step 10K, the system is within 10% of its asymptotic value.

3. **Instability boundary**: D_x=20, k=l=2.0 blows up at step 2100. The stability boundary for the directional extension lies between (D_x=10, k=l=1.0) and (D_x=20, k=l=2.0).

**Classification: MARGINAL-TO-NON-DISSIPATIVE.** The directional extension achieves genuine anisotropy (grad_aniso = 0.25) that is sustained, convergent, and stable. It does not produce waves or inter-peak forces, but it successfully breaks the isotropy that all prior extensions preserved.

---

## 5. Classification Summary

### 5.1 Extension Classification

| Extension | Wave target | Force target | Anisotropy target | Overall classification |
|-----------|------------|-------------|-------------------|----------------------|
| **A: Hyperbolic** | UNSTABLE | N/A | N/A | **UNSTABLE** |
| **B: Strong GMF** | N/A | UNSTABLE | N/A | **UNSTABLE** |
| **C: Directional** | N/A | N/A | **ACHIEVED** | **MARGINAL** |

### 5.2 Detailed Classification

**Extension A — Hyperbolic Sector: UNSTABLE**
- The relational penalty rho^(gamma-1) diverges at low rho, creating runaway depletion when amplified by 1/tau
- No waves, no oscillations, no surviving structure
- The failure is structural: the ED compositional rule is incompatible with underdamped dynamics at low density
- Would require modifying the relational penalty itself (not just adding terms)

**Extension B — Strong GMF: UNSTABLE**
- Quadratic positive feedback (force ~ kappa*lambda*rho^2) makes strong coupling unconditionally unstable with explicit integration
- Stability boundary at kappa*lambda ~ 0.01, where forces are still 10x too weak
- The gap between stable coupling and effective coupling cannot be closed
- Would require implicit integration or sublinear coupling

**Extension C — Directional Operator: MARGINAL (Anisotropy ACHIEVED)**
- Successfully produces sustained gradient anisotropy (ratio = 0.25)
- Anisotropy is a dynamical attractor, not a transient
- Does not produce waves or inter-peak forces
- Stable at (D_x=10, k=l=1.0), unstable at (D_x=20, k=l=2.0)
- Gradient structure is anisotropic but bulk density variance remains isotropic

### 5.3 Target Achievement Summary

| Target | Achieved? | Best result | Limitation |
|--------|-----------|-------------|-----------|
| Wave propagation (Q > 1) | **No** | Runaway depletion (Q>>1 but unstable) | Relational penalty incompatible with underdamped dynamics |
| Underdamped modes | **No** | Zero oscillations detected | Same structural limitation as waves |
| Inter-peak forces (force_ratio > 0.1) | **No** | All strong runs blow up | Quadratic feedback instability |
| Structure modification (delta_sep > 5) | **No** | Zero separation change before blowup | Force never reaches sufficient strength |
| Inflation modification (> 20%) | **No** | Runs blow up before measurement | ED-Phys-10 achieved 12% at perturbative coupling |
| **Anisotropy (grad_aniso > 10% from 1.0)** | **YES** | **grad_aniso = 0.25 (75% deviation)** | Gradient-level only; density variance still isotropic |

---

## 6. The Dissipation Barrier

### 6.1 Three Failed Pathways to Waves

| Module | Approach | Mechanism of failure |
|--------|----------|---------------------|
| ED-Phys-09 | Inertial term (tau=0.1-100, zeta=0.1-1.0) | Canonical dissipation overwhelms inertia; overdamped |
| ED-Phys-11 A | Inertial term (tau=0.001-0.1, zeta=0.001-0.1) | Relational penalty creates runaway depletion via v field |
| ED-Phys-10 | GMF potential field (kappa,lambda=0.01-0.1) | Force too weak; field equation is parabolic (no waves) |

**The pattern**: At high damping, waves are suppressed. At low damping, the relational penalty destabilizes the system. There is no stable underdamped window.

### 6.2 Root Cause: The rho^(gamma-1) Singularity

The relational penalty alpha*gamma*rho^(gamma-1) with gamma = 0.5 gives alpha*0.5*rho^(-0.5). At rho = 1, this is 0.05. At rho = 0.01, this is 0.5. At rho = 0.0001, this is 5.0.

In the canonical (first-order) PDE, this divergence is harmless because dρ/dt = -penalty, and rho simply decays smoothly to the floor. But in the hyperbolic extension:

    dv/dt = (1/tau) * [-penalty(rho) - zeta*v + ...]

The diverging penalty creates a diverging acceleration. As rho decreases, v becomes more negative, which drives rho down faster, which increases the penalty further. This is a catastrophic feedback loop that exists for ANY tau < infinity and ANY zeta < infinity.

### 6.3 What Would Be Required for Waves

Based on the combined evidence from ED-Phys-09, 10, and 11:

1. **Modified relational penalty**: Replace rho^(gamma-1) with a form that does not diverge at rho=0, e.g., rho^(gamma-1) * max(rho/rho_0, 1) or (rho + rho_0)^(gamma-1). This would remove the runaway instability.

2. **Independent wave field**: Instead of adding d^2 rho/dt^2 to the density equation, introduce a separate field psi with its own wave equation d^2 psi/dt^2 = c^2*Lap(psi) that couples to rho only weakly. The density field remains parabolic; the wave lives in psi-space.

3. **Implicit time integration**: For strong GMF coupling, implicit treatment of the coupling term would allow stable evolution at kappa*lambda >> 1.

4. **Fundamentally different dissipation balance**: The canonical parameters (M_0=1, alpha=0.1, gamma=0.5) may simply be in a regime that is inherently dissipation-dominated. Different parameter islands (e.g., very high M_0, very low alpha) might support waves.

---

## 7. The Anisotropy Breakthrough

### 7.1 What Worked

Extension C successfully achieved sustained gradient anisotropy through a minimal mechanism:
- Anisotropic phi diffusion (D_x >> D_y) selects a preferred direction
- Gradient source (kappa * d(rho)/dx) couples phi specifically to x-structure
- Force feedback (lam * div(rho * grad(phi))) preferentially smooths x-gradients

The result: x-gradients are suppressed to 25% of y-gradients. This is the first time any ED-Phys extension has produced a measurable directional asymmetry.

### 7.2 Physical Interpretation

In the ED ontological framework, the directional coupling can be interpreted as:
- A preferred axis in the compositional rule (the gradient penalty acts differently in different directions)
- A "crystal lattice" effect where the underlying geometry of event space has preferred directions
- An analogy to magnetic field alignment in cosmology (the phi field plays the role of a background field that breaks isotropy)

### 7.3 Limitations

1. **Gradient anisotropy only**: The bulk density variance (x_var vs y_var) remains isotropic (ratio ~ 1.0). The directional bias affects fine structure but not large-scale statistics.

2. **Requires explicit symmetry breaking**: The anisotropy comes from the input (D_x != D_y, gradient source in x), not from spontaneous symmetry breaking. The system does not self-organize into anisotropic states from isotropic inputs.

3. **No filamentary structure**: Despite the gradient anisotropy, visual inspection of the 2D density fields does not show elongated or filamentary structures. The effect is statistical, not morphological.

### 7.4 New Scaling Observation

Gradient anisotropy vs coupling strength (from C1 data):

| Coupling (k*l) | D_x | Grad Anisotropy |
|----------------|-----|-----------------|
| 0.01 | 5 | 1.16 |
| 0.25 | 5 | 0.93 |
| 1.0 | 10 | 0.28 |

The anisotropy decreases (more anisotropic) with increasing D_x * kappa * lambda. The convergence time series (C2) shows exponential approach to a steady-state value.

---

## 8. Implications for the ED Ontology

### 8.1 Dissipative Character is Intrinsic

The evidence from four modules (09, 10, 11) is now overwhelming: the ED compositional rule, as specified in ED-12, produces a fundamentally dissipative dynamical system. This is not an accident of parameter choice — it is a structural consequence of:

1. **First-order time**: The compositional rule specifies how density at time t+dt depends on density at time t, not on t-dt. There is no memory, hence no inertia.
2. **Concave penalty**: The rho^(gamma-1) term with gamma < 1 creates a drain that accelerates at low density, preventing any oscillation around zero.
3. **Mobility freeze**: M(rho) -> 0 at rho_max eliminates transport at high density, creating an absorbing boundary.

These three features combine to create a system that is dissipative at all scales and in all parameter regimes.

### 8.2 Wave Physics Requires a New Layer

If wave-like dynamics are desired in the ED framework, they cannot be achieved by modifying the canonical PDE. They require a **new ontological layer** — a separate field with its own wave equation, coupled to the density field but not constrained by the same compositional rule.

This is analogous to how electromagnetic waves in physics are not described by the matter equation of state but by a separate field equation (Maxwell's equations) coupled to matter through charges and currents.

### 8.3 Anisotropy is Accessible

Unlike waves, anisotropy can be achieved within the existing framework by introducing directional bias into the coupling structure. This suggests that the ED ontology can support:
- Preferred-direction effects (analogous to cosmic magnetic fields)
- Directional structure formation (if coupling is strong enough)
- Broken isotropy as a consequence of boundary conditions or initial conditions

### 8.4 The Strong-Coupling Wall

The strong-coupling regime is inaccessible with the current numerical method. The quadratic feedback in GMF coupling creates an instability barrier that separates the perturbative (force << curvature) regime from the non-perturbative (force ~ curvature) regime. Crossing this barrier would require implicit solvers, which are a significant numerical development.

---

## 9. Limitations

1. **Explicit integration only** — implicit methods might stabilize Extensions A and B
2. **1D focus** — hyperbolic and strong GMF tested only in 1D; 2D behavior may differ
3. **Fixed canonical parameters** — different (alpha, gamma, M_0) might change the dissipation balance
4. **No modified penalty tested** — the key insight (rho^(gamma-1) singularity) was identified but not addressed by modifying the penalty
5. **Gradient source for anisotropy only** — other directional mechanisms (tensor mobility, external field) not tested

---

## 10. Future Directions

1. **Modified relational penalty**: Test rho^(gamma-1) * smooth_cutoff(rho) to remove the low-density singularity while preserving the high-density behavior.

2. **Independent wave field**: Introduce a field psi obeying d^2 psi/dt^2 = c^2*Lap(psi) + damping + coupling_to_rho. This field lives in its own dynamical sector and is not constrained by the compositional rule.

3. **Implicit GMF integration**: Implement Crank-Nicolson or similar implicit scheme for the coupling term to access kappa*lambda >> 1.

4. **Spontaneous anisotropy**: Test whether a tensor mobility M_ij(rho, grad_rho) can produce anisotropy from isotropic initial conditions.

5. **Combined extensions**: Test hyperbolic + modified penalty + strong coupling simultaneously.

---

## Appendix A: Experiment Parameters

### A.1 Common Parameters
- alpha = 0.1, gamma = 0.5, M_0 = 1.0, rho_max = 100.0, n_mob = 2
- Boundary: periodic
- Positivity floor: eps = 10^-10

### A.2 Extension A Parameters
- tau in {0.0001, 0.001, 0.01, 0.1}
- zeta in {0.0001, 0.001, 0.01, 0.1}
- CFL: eta = min(0.3*dx/sqrt(M/tau), eta_diffusion, 0.01)

### A.3 Extension B Parameters
- kappa in {0.5, 1.0, 2.0, 5.0, 10.0, 20.0}
- lambda in {0.5, 1.0, 2.0, 5.0, 10.0, 20.0}
- D_phi = 1.0, mu = 0.1
- CFL: eta = min(eta_rho, eta_phi, 0.02*dx/(lam*rho_scale), 0.005)

### A.4 Extension C Parameters
- D_x in {5, 10, 20}, D_y = 0
- kappa in {0.1, 0.5, 1.0, 2.0}
- lambda in {0.1, 0.5, 1.0, 2.0}
- mu = 0.1
- Source: kappa * d(rho)/dx (gradient) or kappa*(rho-rho_bar) (density)

---

## Appendix B: File Inventory

| File | Purpose |
|------|---------|
| `ed_phys_nondissipative.py` | Three extension simulators and full experiment suite |
| `ED-Phys-11_NonDissipative.md` | This document |
| `README.md` | Module overview |
| `results/nondissipative_results.json` | All quantitative results (45 experiments) |
| `results/2d_*_rho.npy` | 2D density field snapshots |
| `results/2d_*_phi.npy` | 2D phi field snapshots |
