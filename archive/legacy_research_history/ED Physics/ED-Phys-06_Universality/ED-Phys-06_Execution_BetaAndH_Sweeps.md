# ED-Phys-06 Execution: Beta-Universality and H-Transition Sweeps

**Author:** Allen Proxmire
**Series:** ED-Phys-06 (Execution Phase)
**Date:** March 2026
**Status:** Complete experiment specifications with output templates
**Prerequisites:** ED-Phys-06 design document, ED-SIM-02 v0.1.0, `edsim.phys.analogues.barenblatt` module

---

## Table of Contents

1. [Beta-Universality Sweep: Full Specifications](#1-beta-universality-sweep-full-specifications)
2. [H-Transition Sweep: Full Specifications](#2-h-transition-sweep-full-specifications)
3. [Combined (beta, H) Grid Experiments](#3-combined-beta-h-grid-experiments)
4. [Data Products and Output Specification](#4-data-products-and-output-specification)
5. [Execution Roadmap](#5-execution-roadmap)
6. [Final Summary](#6-final-summary)

---

# 1. Beta-Universality Sweep: Full Specifications

## 1.1 Codebase Foundation

The existing `edsim.phys.analogues.barenblatt` module provides:
- `predict_barenblatt(beta, d, D, M0)` — analytical predictions
- `run_barenblatt_experiment(beta, N, L, T, dt)` — single-beta run
- `run_beta_sweep(beta_values, N, T, dt)` — multi-beta sweep
- `_make_pme_params(N, L, beta, D, M0, dt)` — parameter construction with $H = 0$, $P_0 = 10^{-12}$
- `_make_pme_ic(params, A, R0)` — Gaussian bump in $\delta = \rho_{\max} - \rho$ with background $\delta_{\text{bg}} = 10^{-4}$

The sweep extends the existing implementation from $\beta \in \{1, 2, 3\}$ to $\beta \in \{0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 4.0, 5.0\}$.

## 1.2 Experiment Configurations

### Master Configuration (shared across all beta values)

| Parameter | Symbol | Value | Source |
|-----------|--------|-------|--------|
| Dimension | $d$ | 2 (primary), 3 (confirmation) | Standard ED-SIM-02 |
| Domain size | $L$ | 4.0 (per axis) | `_make_pme_params` default |
| Mobility prefactor | $M_0$ | 1.0 | Canonical |
| Diffusion coefficient | $D$ | 0.3 | Canonical |
| Penalty strength | $P_0$ | $10^{-12}$ | Effectively zero (PME limit) |
| Equilibrium density | $\rho^*$ | 0.5 | Canonical (irrelevant at $P_0 \approx 0$) |
| Saturation density | $\rho_{\max}$ | 1.0 | Canonical |
| Participation coupling | $H$ | 0.0 | Mobility-only test |
| Participation timescale | $\tau$ | 1.0 | (irrelevant at $H = 0$) |
| Participation friction | $\zeta$ | 0.1 | (irrelevant at $H = 0$) |
| Boundary conditions | BC | Neumann | Standard |
| Integrator | method | `implicit_euler` | Stable for all $\beta$ |
| IC amplitude | $A$ | 0.4 | `_make_pme_ic` default |
| IC radius | $R_0$ | 0.5 | `_make_pme_ic` default |
| IC sigma | $\sigma$ | $R_0/2 = 0.25$ | Gaussian width |
| IC background | $\delta_{\text{bg}}$ | $10^{-4}$ | Prevents zero mobility |
| Output snapshots | $k_{\text{out}}$ | 30 | For power-law fitting |

### Per-Beta Configuration

The grid resolution $N$, timestep $\Delta t$, and simulation time $T$ are adapted to each $\beta$ to balance accuracy and computational cost. Higher $\beta$ produces sharper fronts requiring finer resolution, and slower spreading requiring longer simulation times.

| $\beta$ | $m = \beta + 1$ | $N$ (2D) | $N$ (3D) | $\Delta t$ | $T$ | $D_{\text{pme}} = DM_0/(\beta+1)$ | $\alpha_R^{\text{pred}}$ (2D) | Estimated wall time (2D) |
|---------|---------|----------|----------|---------|------|------|------|------|
| 0.5 | 1.5 | 96 | 32 | 0.005 | 150.0 | 0.200 | 0.3333 | ~10s |
| 1.0 | 2.0 | 96 | 32 | 0.005 | 200.0 | 0.150 | 0.2500 | ~15s |
| 1.5 | 2.5 | 96 | 32 | 0.005 | 250.0 | 0.120 | 0.2000 | ~20s |
| 2.0 | 3.0 | 96 | 32 | 0.005 | 200.0 | 0.100 | 0.1667 | ~15s |
| 2.5 | 3.5 | 128 | 40 | 0.002 | 300.0 | 0.0857 | 0.1429 | ~45s |
| 3.0 | 4.0 | 128 | 40 | 0.002 | 300.0 | 0.0750 | 0.1250 | ~45s |
| 4.0 | 5.0 | 128 | 48 | 0.001 | 400.0 | 0.0600 | 0.1000 | ~120s |
| 5.0 | 6.0 | 160 | 48 | 0.001 | 500.0 | 0.0500 | 0.0833 | ~200s |

**Rationale for parameter scaling:**
- $N$ increases with $\beta$ because the front becomes thinner (fewer grid points across the front).
- $\Delta t$ decreases with $\beta$ because the implicit Euler scheme requires smaller steps when the mobility is more degenerate (stiffer Jacobian).
- $T$ increases with $\beta$ because the front spreads more slowly ($\alpha_R$ decreases), requiring more time for the power law to establish.

### Initial Condition Construction

For all $\beta$, the IC is constructed via `_make_pme_ic`:

$$\delta(\mathbf{x}, 0) = A \exp\!\left(-\frac{|\mathbf{x} - \mathbf{x}_c|^2}{2\sigma^2}\right) + \delta_{\text{bg}}$$

$$\rho(\mathbf{x}, 0) = \rho_{\max} - \delta(\mathbf{x}, 0)$$

with $\mathbf{x}_c = (L/2, L/2)$, $A = 0.4$, $\sigma = 0.25$, $\delta_{\text{bg}} = 10^{-4}$.

This is a Gaussian (not a Barenblatt profile) — the simulation must run long enough for the Gaussian IC to relax into the Barenblatt self-similar form. The fitting window $t \in [0.2T, T]$ excludes the initial transient.

**Note:** The existing codebase uses a Gaussian IC rather than the exact Barenblatt shape. This is deliberate: the self-similar solution is an *attractor*, so any reasonable IC should converge to it. Verifying convergence from a Gaussian IC is a stronger test than starting from the exact self-similar shape.

## 1.3 Observables: Exact Extraction Procedures

### Observable 1: Front Radius $R(t)$

**Definition:** The maximum distance from the domain centre at which $\delta > \epsilon$, where $\epsilon = 0.005 \times A = 0.002$.

**Extraction procedure** (matching `barenblatt.py` lines 356–369):

```
FOR EACH output snapshot at time t_n:
    1. Compute delta = rho_max - rho
    2. Compute central delta: delta_c = delta[N//2, N//2]
    3. Compute half-maximum: half_max = delta_c / 2
    4. Construct radial grid: R(i,j) = sqrt((x_i - cx)^2 + (y_j - cy)^2)
    5. Mask: mask = (delta > half_max)
    6. Front radius: R(t_n) = max(R[mask])
```

**Power-law fitting** (matching lines 371–379):

```
1. Select fitting window: mask_t = (times > 0.2 * T)
2. Log-log linear regression: log(R) = alpha_R * log(t) + log(C_R)
3. Extract alpha_R = slope
4. Compute error: |alpha_R_meas - alpha_R_pred| / alpha_R_pred * 100%
```

### Observable 2: Central Density Decay $\delta_c(t)$

**Definition:** $\delta_c(t) = \delta(\mathbf{x}_c, t) = \rho_{\max} - \rho(\mathbf{x}_c, t)$.

**Extraction:** Direct grid sampling at the centre pixel $(N/2, N/2)$.

**Power-law fitting:** Same procedure as $R(t)$, using $\delta_c(t) = C_\rho \cdot t^{\alpha_\rho}$ on $t \in [0.2T, T]$ with the additional mask $\delta_c > 10^{-10}$ (exclude numerically zero values).

### Observable 3: Compact Support Boundary

**Definition:** At each snapshot, measure the maximum $\delta$ in the tail region $|\mathbf{x} - \mathbf{x}_c| > 2R(t)$ (matching `_measure_tail` in the codebase).

**Criterion:** Compact support is confirmed if $\delta_{\text{tail}} < 2\epsilon = 0.004$ at all output times after the transient ($t > 0.1T$).

**Extraction:**

```
FOR EACH snapshot at time t_n (t_n > 0.1 * T):
    1. Compute delta = rho_max - rho
    2. Construct radial grid R(i,j)
    3. Tail mask: mask_tail = (R > 2 * front_radius[n])
    4. tail_max[n] = max(delta[mask_tail]) if any(mask_tail) else 0
compact_support = all(tail_max[mask_t] < 0.004)
```

### Observable 4: Similarity Collapse

**Definition:** At two late times $t_1 = T/2$ and $t_2 = T$, rescale the profile by its front radius and central density, then measure the $L^2$ distance between the rescaled curves.

**Extraction:**

```
FOR t in [T/2, T]:
    1. Compute delta at time t
    2. Extract 1D radial profile: delta_radial(r) via azimuthal average
    3. Normalise: eta = r / R(t), f = delta_radial / delta_c(t)
    4. Interpolate f onto a common eta grid [0, 0.01, ..., 1.5]

collapse_error = L2_norm(f(T/2) - f(T)) / L2_norm(f(T))
```

**Threshold:** $\epsilon_{\text{collapse}} < 0.3$ for a passing similarity collapse.

## 1.4 Predicted Scaling Table

The full prediction table for both 2D and 3D:

| $\beta$ | $m$ | $\alpha_R$ (2D) | $\alpha_\rho$ (2D) | $\alpha_R$ (3D) | $\alpha_\rho$ (3D) | $D_{\text{pme}}$ |
|---------|-----|-----------------|---------------------|-----------------|---------------------|-------------------|
| 0.5 | 1.5 | 0.33333 | $-0.66667$ | 0.28571 | $-0.85714$ | 0.20000 |
| 1.0 | 2.0 | 0.25000 | $-0.50000$ | 0.20000 | $-0.60000$ | 0.15000 |
| 1.5 | 2.5 | 0.20000 | $-0.40000$ | 0.15385 | $-0.46154$ | 0.12000 |
| 2.0 | 3.0 | 0.16667 | $-0.33333$ | 0.12500 | $-0.37500$ | 0.10000 |
| 2.5 | 3.5 | 0.14286 | $-0.28571$ | 0.10526 | $-0.31579$ | 0.08571 |
| 3.0 | 4.0 | 0.12500 | $-0.25000$ | 0.09091 | $-0.27273$ | 0.07500 |
| 4.0 | 5.0 | 0.10000 | $-0.20000$ | 0.07143 | $-0.21429$ | 0.06000 |
| 5.0 | 6.0 | 0.08333 | $-0.16667$ | 0.05882 | $-0.17647$ | 0.05000 |

## 1.5 Falsification Conditions Per Beta

Each $\beta$ value has three falsification criteria. A failure at any level triggers a resolution escalation.

| $\beta$ | F1: $\alpha_R$ error threshold | F2: compact support threshold | F3: collapse error threshold | Expected difficulty |
|---------|-------------------------------|-------------------------------|------------------------------|---------------------|
| 0.5 | 15% | $\delta_{\text{tail}} < 0.004$ | $< 0.3$ | Easy (nearly linear) |
| 1.0 | 15% | $\delta_{\text{tail}} < 0.004$ | $< 0.3$ | Easy (benchmark) |
| 1.5 | 15% | $\delta_{\text{tail}} < 0.004$ | $< 0.3$ | Easy |
| 2.0 | 15% | $\delta_{\text{tail}} < 0.004$ | $< 0.3$ | Easy (existing pass at $N=64$) |
| 2.5 | 20% | $\delta_{\text{tail}} < 0.006$ | $< 0.35$ | Moderate |
| 3.0 | 20% | $\delta_{\text{tail}} < 0.006$ | $< 0.35$ | Moderate (existing pass at $N=64$) |
| 4.0 | 25% | $\delta_{\text{tail}} < 0.008$ | $< 0.40$ | Hard (thin front) |
| 5.0 | 25% | $\delta_{\text{tail}} < 0.010$ | $< 0.40$ | Hard (very thin front) |

**Escalation protocol:** If any $\beta$ fails at the specified $N$:
1. Re-run at $2N$ (double resolution).
2. Re-run at $\Delta t / 2$ (half timestep).
3. If still failing after escalation, the deviation is physical, not numerical. Record the residual as an ED-specific constitutive correction.

## 1.6 Resolution Convergence Check

For the two hardest cases ($\beta = 4.0$ and $\beta = 5.0$), run a convergence series at three resolutions:

| $\beta$ | $N_1$ | $N_2$ | $N_3$ |
|---------|-------|-------|-------|
| 4.0 | 96 | 128 | 192 |
| 5.0 | 128 | 160 | 224 |

Compute $\alpha_R$ at each resolution. If the sequence converges ($|\alpha_R(N_3) - \alpha_R(N_2)| < |\alpha_R(N_2) - \alpha_R(N_1)|$), the converged value is the physical result. If it does not converge, the front dynamics at that $\beta$ are under-resolved and the result is inconclusive.

---

# 2. H-Transition Sweep: Full Specifications

## 2.1 Two Experiment Configurations

The H-sweep uses two distinct ICs to probe different aspects of the participation channel.

### Configuration A: PME + Participation

Tests how participation modifies front spreading. Uses the Barenblatt IC with small penalty.

| Parameter | Value | Notes |
|-----------|-------|-------|
| $d$ | 2 | |
| $N$ | $(128, 128)$ | |
| $L$ | $(4.0, 4.0)$ | |
| $D$ | 0.3 | |
| $M_0$ | 1.0 | |
| $\beta$ | 2.0 | Canonical |
| $P_0$ | 0.01 | Small but nonzero (needed to drive $v$) |
| $\rho^*$ | 0.5 | |
| $\rho_{\max}$ | 1.0 | |
| $\tau$ | 1.0 | |
| $\zeta$ | 0.1 | |
| $T$ | 5.0 | |
| $\Delta t$ | 0.001 | |
| $k_{\text{out}}$ | 500 | High resolution for $v(t)$ FFT |
| IC | Gaussian bump: $A = 0.3$, $R_0 = 0.4$, $\sigma = 0.2$ | |

### Configuration B: Penalty-Relaxation + Participation

Tests how participation modifies relaxation to $\rho^*$. Uses uniform IC above equilibrium.

| Parameter | Value | Notes |
|-----------|-------|-------|
| $d$ | 2 | |
| $N$ | $(64, 64)$ | Lower resolution sufficient (no front) |
| $L$ | $(1.0, 1.0)$ | |
| $D$ | 0.3 | |
| $M_0$ | 1.0 | |
| $\beta$ | 2.0 | |
| $P_0$ | 1.0 | Strong penalty |
| $\rho^*$ | 0.5 | |
| $\rho_{\max}$ | 1.0 | |
| $\tau$ | 1.0 | |
| $\zeta$ | 0.1 | |
| $T$ | 3.0 | |
| $\Delta t$ | 0.001 | |
| $k_{\text{out}}$ | 500 | |
| IC | $\rho_0 = 0.7 + 0.01 \cdot \mathcal{N}(0, 1)$ | Uniform + small noise |

### H Values

$$H \in \{0,\; 0.1,\; 0.5,\; 1.0,\; 2.0,\; 5.0,\; 10.0,\; 20.0,\; 50.0,\; 100.0,\; 200.0\}$$

Total runs: $11 \times 2 = 22$.

## 2.2 Mapping Between $(\tau, \zeta)$ and $(\gamma, H)$

The codebase parameterises the participation channel with $(\tau, \zeta)$. The telegraph parameters used in the theoretical analysis are:

$$\gamma = \frac{DP_0 + \zeta/\tau}{2}, \qquad \omega_0^2 = \frac{DP_0\zeta + HP_0}{\tau}$$

For Configuration A ($P_0 = 0.01$, $\zeta = 0.1$, $\tau = 1.0$, $D = 0.3$):

$$\gamma = \frac{0.3 \times 0.01 + 0.1/1.0}{2} = \frac{0.003 + 0.1}{2} = 0.0515$$

$$\omega_0^2 = \frac{0.3 \times 0.01 \times 0.1 + H \times 0.01}{1.0} = 0.0003 + 0.01H$$

Underdamped condition ($\omega_0 > \gamma$): $0.0003 + 0.01H > 0.0515^2 = 0.00265$, so $H > 0.235$.

For Configuration B ($P_0 = 1.0$):

$$\gamma = \frac{0.3 + 0.1}{2} = 0.2$$

$$\omega_0^2 = \frac{0.3 \times 0.1 + H}{1.0} = 0.03 + H$$

Underdamped: $0.03 + H > 0.04$, so $H > 0.01$.

**Predicted telegraph parameters per H:**

| $H$ | Config A: $\gamma$ | Config A: $\omega_0$ | Config A: $\omega$ | Config B: $\gamma$ | Config B: $\omega_0$ | Config B: $\omega$ |
|-----|---|---|---|---|---|---|
| 0 | 0.0515 | 0.0173 | overdamped | 0.200 | 0.173 | overdamped |
| 0.1 | 0.0515 | 0.0322 | overdamped | 0.200 | 0.361 | 0.301 |
| 0.5 | 0.0515 | 0.0711 | 0.0481 | 0.200 | 0.728 | 0.700 |
| 1.0 | 0.0515 | 0.1002 | 0.0860 | 0.200 | 1.015 | 0.995 |
| 2.0 | 0.0515 | 0.1416 | 0.1319 | 0.200 | 1.428 | 1.414 |
| 5.0 | 0.0515 | 0.2238 | 0.2178 | 0.200 | 2.245 | 2.236 |
| 10.0 | 0.0515 | 0.3163 | 0.3121 | 0.200 | 3.166 | 3.160 |
| 20.0 | 0.0515 | 0.4473 | 0.4443 | 0.200 | 4.474 | 4.469 |
| 50.0 | 0.0515 | 0.7073 | 0.7054 | 0.200 | 7.072 | 7.069 |
| 100.0 | 0.0515 | 1.0001 | 0.9988 | 0.200 | 10.001 | 9.999 |
| 200.0 | 0.0515 | 1.4143 | 1.4134 | 0.200 | 14.143 | 14.142 |

**Key observation:** For Config A, oscillation onset occurs around $H \approx 0.3$ ($\omega > 0$). For Config B, onset is near $H \approx 0.05$. The critical $H_c$ depends on $P_0$.

## 2.3 Observable Extraction Procedures

### Observable 1: Oscillation Onset

**Procedure:**

```
FOR EACH H:
    1. Extract v(t) time series from simulation output
    2. Window: v_window = v(t) for t in [T/4, T]
    3. Compute FFT: V_k = FFT(v_window)
    4. Frequency axis: f_k = k / (N_window * dt_output)
    5. Power spectrum: P_k = |V_k|^2
    6. Exclude DC component (k=0)
    7. Peak frequency: omega_peak = 2*pi * f_{argmax(P_k)}
    8. Peak amplitude: A_peak = 2 * |V_{argmax}| / N_window
```

**H_c determination:**

```
A_noise = A_peak at H=0  (numerical noise floor)
H_c = min(H) where A_peak(H) > 10 * A_noise
```

### Observable 2: Frequency Scaling $\omega(H)$

**Procedure:**

```
FOR H in H_values where H > H_c:
    Record (H, omega_peak)

Fit: log(omega_peak) = a * log(H) + b
scaling_exponent = a
scaling_error = standard error of a

PREDICTION: a = 0.50 +/- 0.05
```

**Verification against analytical prediction:**

For Config A at large $H$: $\omega \approx \sqrt{HP_0/\tau} = \sqrt{0.01H} = 0.1\sqrt{H}$.

For Config B at large $H$: $\omega \approx \sqrt{H/\tau} \approx \sqrt{H}$.

### Observable 3: Diffusive-to-Ballistic Crossover (Config A only)

**Procedure:**

```
FOR EACH H:
    1. Track front radius R(t) as in beta-sweep
    2. Fit power law: R_power(t) = C1 * t^alpha
       R^2_power = coefficient of determination
    3. Fit linear: R_linear(t) = v_front * t + R_offset
       R^2_linear = coefficient of determination

    IF R^2_linear > R^2_power:
        regime = "ballistic"
        c_measured = v_front
    ELSE:
        regime = "diffusive"
        c_measured = NaN

    c_predicted = sqrt(D * H / tau) = sqrt(0.3 * H)
```

**Expected crossover:**

| $H$ | $c_{\text{pred}} = \sqrt{0.3H}$ | Expected regime |
|-----|---|---|
| 0 | 0 (diffusive) | Diffusive |
| 0.1 | 0.173 | Diffusive |
| 0.5 | 0.387 | Transitional |
| 1.0 | 0.548 | Transitional |
| 2.0 | 0.775 | Mixed |
| 5.0 | 1.225 | Mixed/ballistic |
| 10.0 | 1.732 | Ballistic |
| 20.0 | 2.449 | Ballistic |
| 50.0 | 3.873 | Ballistic |
| 100.0 | 5.477 | Ballistic |
| 200.0 | 7.746 | Ballistic |

### Observable 4: Energy Monotonicity Check

**Procedure:**

```
FOR EACH H:
    1. Compute E(t) at each output snapshot
    2. dE = E(t_{n+1}) - E(t_n) for all n
    3. E_monotone = all(dE <= epsilon) where epsilon = 1e-10
    4. IF NOT E_monotone:
        E_violation_max = max(dE)
        E_violation_time = t at first violation
        E_violation_frac = E_violation_max / |E(0)|
```

**Expected:** Energy monotonicity holds for $H \leq 50$ with these parameters. At $H = 100$ and $H = 200$, transient violations may occur during the first oscillation cycle.

## 2.4 Falsification Conditions

**F4 (frequency scaling):** The fitted exponent for $\omega(H)$ must be in $[0.40, 0.60]$. If outside this range, the linear telegraph model is inadequate.

**F5 (participation threshold):** $H_c$ must exist and be identifiable (amplitude ratio $> 10\times$ noise). If oscillation grows from zero with no threshold (purely smooth onset), this is a characterisation result, not a falsification.

**F6 (propagation speed):** At $H = 100$, the measured front speed must match $c_{\text{pred}} = \sqrt{0.3 \times 100} = 5.48$ to within 15%. Acceptable range: $[4.66, 6.30]$.

**F7 (energy monotonicity boundary):** If $E(t)$ is monotone at all $H$ tested (including $H = 200$), the Lyapunov boundary does not exist in the tested range — record this as a positive architectural result. If violations appear, record $H_{\text{Lyap}}$ and the violation amplitude.

---

# 3. Combined (beta, H) Grid Experiments

## 3.1 Grid Definition

The combined grid probes the interaction between mobility and participation:

$$\beta \in \{0.5, 1.0, 2.0, 3.0, 5.0\} \;\times\; H \in \{0, 1.0, 10.0, 100.0\}$$

Total: $5 \times 4 = 20$ grid points.

## 3.2 Per-Grid-Point Configuration

Each grid point uses a standardised configuration that enables direct comparison:

| Parameter | Value |
|-----------|-------|
| $d$ | 2 |
| $N$ | $(96, 96)$ |
| $L$ | $(4.0, 4.0)$ |
| $D$ | 0.3 |
| $M_0$ | 1.0 |
| $P_0$ | 0.1 |
| $\rho^*$ | 0.5 |
| $\rho_{\max}$ | 1.0 |
| $\tau$ | 1.0 |
| $\zeta$ | 0.1 |
| $\Delta t$ | 0.001 |
| $T$ | 3.0 |
| $k_{\text{out}}$ | 300 |
| IC | Gaussian bump: $A = 0.3$, $\sigma = 0.15$, centred |

**Why $P_0 = 0.1$:** A moderate penalty ensures all three channels are active simultaneously. At $P_0 = 0$ only mobility acts; at $P_0 = 1$ penalty dominates mobility at low $\beta$.

## 3.3 Observables at Each Grid Point

At each $(\beta, H)$ point, extract:

| Observable | Symbol | How extracted |
|-----------|--------|---------------|
| Final energy ratio | $E(T)/E(0)$ | Direct |
| Energy monotonicity | $E_{\text{mono}}$ | Check $\max(\Delta E) \leq 0$ |
| Complexity ratio | $C(T)/C(0)$ | Direct |
| $v(t)$ peak amplitude | $|v|_{\max}$ | $\max|v(t)|$ |
| $v(t)$ oscillation frequency | $\omega_v$ | FFT peak |
| $v(t)$ damping rate | $\gamma_{\text{eff}}$ | Envelope fit |
| Number of oscillation cycles | $N_{\text{osc}}$ | Zero-crossing count / 2 |
| Front radius at $T$ | $R(T)$ | Front extraction |
| Dissipation ratios at $T/2$ | $R_{\text{grad}}, R_{\text{pen}}, R_{\text{part}}$ | Dissipation module |
| Spectral entropy at $T$ | $H_{\text{spec}}(T)$ | Spectral module |
| Correlation length at $T$ | $\xi(T)$ | Correlation module |

## 3.4 Expected Morphology by Region

| $(\beta, H)$ | Region | Front | Oscillation | $R_{\text{part}}$ | $E_{\text{mono}}$ |
|---|---|---|---|---|---|
| (0.5, 0) | I: PME-weak | Broad, smooth | None | 0 | Yes |
| (1.0, 0) | I: PME | Standard | None | 0 | Yes |
| (2.0, 0) | I: PME-canonical | Barenblatt | None | 0 | Yes |
| (3.0, 0) | II: Degenerate | Sharp | None | 0 | Yes |
| (5.0, 0) | II: Strongly degen. | Very sharp | None | 0 | Yes |
| (0.5, 1) | III: Mixed-weak | Modulated | Weak | 0.05–0.15 | Yes |
| (1.0, 1) | III: Mixed | Modulated | Moderate | 0.10–0.20 | Yes |
| (2.0, 1) | III: Mixed-canonical | Modulated | Moderate | 0.10–0.25 | Yes |
| (3.0, 1) | III: Mixed-sharp | Sharp + modulated | Moderate | 0.10–0.20 | Yes |
| (5.0, 1) | III: Mixed-degen. | Very sharp + modulated | Moderate | 0.08–0.15 | Yes |
| (0.5, 10) | III–IV boundary | Oscillatory | Strong | 0.30–0.50 | Likely yes |
| (1.0, 10) | III–IV | Oscillatory | Strong | 0.30–0.50 | Likely yes |
| (2.0, 10) | III–IV | Oscillatory | Strong | 0.25–0.45 | Likely yes |
| (3.0, 10) | III | Sharp + oscillatory | Strong | 0.20–0.40 | Yes |
| (5.0, 10) | III | Very sharp + oscillatory | Strong | 0.15–0.35 | Yes |
| (0.5, 100) | IV: Telegraph | Ballistic | Very strong | 0.50–0.80 | Check |
| (1.0, 100) | IV: Telegraph | Ballistic | Very strong | 0.50–0.75 | Check |
| (2.0, 100) | IV: Telegraph | Ballistic | Very strong | 0.45–0.70 | Check |
| (3.0, 100) | IV–V: Telegraph-sharp | Ballistic + sharp | Very strong | 0.40–0.65 | Check |
| (5.0, 100) | V: Extreme | Complex | Very strong | 0.35–0.60 | Check |

## 3.5 Criteria for Identifying Critical Surfaces

### Participation Threshold $H_c(\beta)$

**Criterion:** Smallest $H$ at which $|v|_{\max} > 0.01$ (participation amplitude exceeds 1% of $\rho^*$).

From the grid, interpolate between $H = 0$ and $H = 1.0$ to estimate $H_c$.

**Prediction:** $H_c \approx 0.2$–$0.5$ for all $\beta$ (weak $\beta$-dependence), determined by $P_0$ and $\zeta/\tau$.

### Lyapunov Boundary $H_{\text{Lyap}}(\beta)$

**Criterion:** Smallest $H$ at which $\max(\Delta E) > 0$ (energy monotonicity violated).

From the grid, interpolate between $H = 10$ and $H = 100$ (or extrapolate beyond $H = 100$).

**Prediction:** $H_{\text{Lyap}}$ increases with $\beta$ because higher degeneracy dissipates more energy via the front. Estimated $H_{\text{Lyap}} \approx 30$–$80$ for $\beta = 2$ with $P_0 = 0.1$.

### Ballistic Crossover $H_{\text{bal}}(\beta)$

**Criterion:** Smallest $H$ at which the linear fit to $R(t)$ has $R^2 > 0.9$ and the power-law fit has $R^2_{\text{power}} < R^2_{\text{linear}}$.

**Prediction:** $H_{\text{bal}} \approx 5$–$10$ for $\beta = 2$ with these parameters. Weakly dependent on $\beta$.

---

# 4. Data Products and Output Specification

## 4.1 File Structure

All outputs saved under a single results directory:

```
results/ed-phys-06/
    beta_sweep/
        beta_0.50_2d.json        # Per-beta result
        beta_1.00_2d.json
        ...
        beta_5.00_2d.json
        beta_1.00_3d.json        # 3D confirmation runs
        beta_2.00_3d.json
        beta_sweep_summary.json  # Aggregated results
    h_sweep/
        config_A/
            H_0.000.json
            H_0.100.json
            ...
            H_200.000.json
        config_B/
            H_0.000.json
            ...
            H_200.000.json
        h_sweep_summary.json
    grid/
        beta_0.50_H_0.00.json
        beta_0.50_H_1.00.json
        ...
        beta_5.00_H_100.00.json
        grid_summary.json
    convergence/
        beta_4.00_N96.json
        beta_4.00_N128.json
        beta_4.00_N192.json
        beta_5.00_N128.json
        beta_5.00_N160.json
        beta_5.00_N224.json
    report/
        ED-Phys-06_Results.md
```

## 4.2 Per-Run JSON Schema

Each run produces a JSON file with the following structure:

```json
{
    "metadata": {
        "experiment": "beta_sweep | h_sweep_A | h_sweep_B | grid",
        "beta": 2.0,
        "H": 0.0,
        "d": 2,
        "N": [128, 128],
        "T": 200.0,
        "dt": 0.005,
        "timestamp": "2026-03-30T12:00:00Z",
        "edsim_version": "0.1.0"
    },
    "parameters": {
        "D": 0.3, "M0": 1.0, "P0": 0.01,
        "rho_star": 0.5, "rho_max": 1.0,
        "tau": 1.0, "zeta": 0.1
    },
    "results": {
        "alpha_R_predicted": 0.1667,
        "alpha_R_measured": 0.1650,
        "alpha_R_error_pct": 1.02,
        "alpha_rho_predicted": -0.3333,
        "alpha_rho_measured": -0.3280,
        "alpha_rho_error_pct": 1.59,
        "compact_support": true,
        "tail_max": 0.00012,
        "collapse_error": 0.045,
        "E_final_ratio": 0.132,
        "E_monotone": true,
        "v_max": 0.0,
        "omega_peak": 0.0,
        "gamma_eff": null,
        "N_oscillations": 0,
        "front_regime": "diffusive",
        "c_measured": null,
        "c_predicted": 0.0,
        "R_grad": 0.65,
        "R_pen": 0.35,
        "R_part": 0.00,
        "xi_final": 0.312,
        "H_spec_final": 1.82
    },
    "pass_fail": {
        "F1_alpha_R": "PASS",
        "F2_compact": "PASS",
        "F3_collapse": "PASS"
    }
}
```

## 4.3 Naming Conventions

| Pattern | Example | Description |
|---------|---------|-------------|
| `beta_{value}_2d.json` | `beta_2.00_2d.json` | Beta sweep, 2D |
| `beta_{value}_3d.json` | `beta_2.00_3d.json` | Beta sweep, 3D confirmation |
| `H_{value}.json` | `H_10.000.json` | H sweep, single run |
| `beta_{b}_H_{h}.json` | `beta_2.00_H_10.00.json` | Grid point |
| `beta_{b}_N{n}.json` | `beta_4.00_N128.json` | Convergence run |

All floating-point values formatted to 2 decimal places in filenames except $H$ values (3 decimal places for $H < 1$).

## 4.4 Required Plots

### Plot Set 1: Beta-Universality

| Plot | X-axis | Y-axis | Content |
|------|--------|--------|---------|
| P1 | $\beta$ | $\alpha_R$ | Predicted (curve) vs. measured (points) for 2D and 3D |
| P2 | $\beta$ | $\alpha_\rho$ | Same format as P1 |
| P3 | $\eta = r/R(t)$ | $f = \delta/\delta_c$ | Similarity collapse at $t = T/2$ and $t = T$ for each $\beta$ |
| P4 | $\log t$ | $\log R(t)$ | Front radius time series for all 8 $\beta$ values |
| P5 | $\beta$ | error (%) | Error bar chart for $\alpha_R$ and $\alpha_\rho$ |

### Plot Set 2: H-Transition

| Plot | X-axis | Y-axis | Content |
|------|--------|--------|---------|
| P6 | $t$ | $v(t)$ | Participation field time series at $H = 0, 1, 10, 100$ |
| P7 | $\log H$ | $\log \omega$ | Frequency scaling with $H^{1/2}$ reference line |
| P8 | $H$ | $N_{\text{osc}}$ | Number of oscillation cycles vs. $H$ |
| P9 | $t$ | $R(t)$ | Front radius for $H = 0, 5, 20, 100$ (Config A) |
| P10 | $H$ | $\Delta E_{\max}$ | Maximum energy increment vs. $H$ (energy monotonicity) |
| P11 | $H$ | $c_{\text{meas}}/c_{\text{pred}}$ | Speed ratio (should approach 1.0 at large $H$) |

### Plot Set 3: Phase Diagram

| Plot | X-axis | Y-axis | Content |
|------|--------|--------|---------|
| P12 | $\beta$ | $H$ | Heatmap of $R_{\text{part}}$ (participation dissipation fraction) |
| P13 | $\beta$ | $H$ | Heatmap of $N_{\text{osc}}$ with $H_c(\beta)$ contour |
| P14 | $\beta$ | $H$ | Binary map: green = $E$ monotone, red = $E$ violated |
| P15 | $\beta$ | $H$ | Front regime: blue = diffusive, orange = ballistic |

## 4.5 Summary Tables

### Table S1: Beta-Universality Results

| $\beta$ | $m$ | $\alpha_R^{\text{pred}}$ | $\alpha_R^{\text{meas}}$ | Error (%) | Compact? | Collapse error | PASS/FAIL |
|---------|-----|---|---|---|---|---|---|

(8 rows for 2D, 2–3 rows for 3D confirmation)

### Table S2: H-Transition Results (Config A)

| $H$ | $\omega_{\text{peak}}$ | $A_{\text{peak}}$ | $\gamma_{\text{eff}}$ | $N_{\text{osc}}$ | Regime | $c_{\text{meas}}$ | $c_{\text{pred}}$ | $E$ mono? |
|-----|---|---|---|---|---|---|---|---|

(11 rows)

### Table S3: Grid Summary

| $\beta$ | $H$ | $R_{\text{part}}$ | $N_{\text{osc}}$ | $E$ mono | Regime | Region |
|---------|-----|---|---|---|---|---|

(20 rows)

### Table S4: Critical Surfaces

| Quantity | Method | Value | $\beta$-dependence |
|----------|--------|-------|-----|
| $H_c$ | Oscillation onset | est. 0.2–0.5 | Weak |
| $H_{\text{Lyap}}$ | First $E$ violation | est. 30–80 | Increases with $\beta$ |
| $H_{\text{bal}}$ | Linear vs. power-law $R(t)$ | est. 5–10 | Weak |

## 4.6 Invariants to Compute

At each grid point, compute the full ED-SIM-02 invariant atlas:

| Invariant family | Quantities | Module |
|-----------------|-----------|--------|
| Energy | $E[\rho]$, $C[\rho]$, mass | `edsim.invariants.energy` |
| Spectral | $H_{\text{spec}}$, mode hierarchy, leading mode amplitude | `edsim.invariants.spectral` |
| Dissipation | $R_{\text{grad}}$, $R_{\text{pen}}$, $R_{\text{part}}$ | `edsim.invariants.dissipation` |
| Correlation | $\xi$, $S_2(r)$ | `edsim.invariants.correlation` |
| Morphology | blob/sheet/filament/pancake fractions | `edsim.invariants.morphology` |
| Topology | $\chi$ at $\theta = \rho^*/2$ | `edsim.invariants.topology` |

---

# 5. Execution Roadmap

## 5.1 Recommended Execution Order

The experiments have dependencies: later experiments use results from earlier ones to set parameters or interpret outcomes.

### Phase 1: Beta-Universality Sweep (2D)

**Runs:** 8 (one per $\beta$)
**Estimated time:** ~8 minutes total
**Dependencies:** None
**Purpose:** Establish the baseline: does $\alpha_R = 1/(d\beta + 2)$ hold?

```
ORDER: beta=2.0 (benchmark, existing result)
       beta=1.0, beta=3.0 (extend existing sweep)
       beta=0.5, beta=1.5, beta=2.5 (fill in gaps)
       beta=4.0, beta=5.0 (high-degeneracy frontier)
```

### Phase 2: Convergence Checks

**Runs:** 6 ($\beta = 4.0$ at 3 resolutions + $\beta = 5.0$ at 3 resolutions)
**Estimated time:** ~15 minutes total
**Dependencies:** Phase 1 (need to know if $\beta = 4, 5$ fail before escalating)
**Purpose:** Validate that high-$\beta$ results are converged.

### Phase 3: Beta-Universality Sweep (3D Confirmation)

**Runs:** 3 ($\beta = 1.0, 2.0, 3.0$ in 3D)
**Estimated time:** ~10 minutes total
**Dependencies:** Phase 1 (confirm 2D passes before investing in 3D)
**Purpose:** Verify dimension-independence of universality.

### Phase 4: H-Transition Sweep

**Runs:** 22 (11 H values $\times$ 2 configs)
**Estimated time:** ~15 minutes total
**Dependencies:** None (independent of beta sweep)
**Purpose:** Map the participation channel's activation and scaling.

### Phase 5: Combined Grid

**Runs:** 20 (5 $\beta$ $\times$ 4 $H$)
**Estimated time:** ~20 minutes total
**Dependencies:** Phases 1 and 4 (need $H_c$ from Phase 4 to interpret grid results)
**Purpose:** Map the full $(\beta, H)$ phase diagram.

### Phase 6: Analysis and Reporting

**Runs:** 0 (post-processing only)
**Estimated time:** ~30 minutes (manual analysis + plot generation)
**Dependencies:** All previous phases
**Purpose:** Generate plots, tables, and the results document.

### Total

| Phase | Runs | Est. time | Cumulative |
|-------|------|-----------|------------|
| 1 | 8 | 8 min | 8 min |
| 2 | 6 | 15 min | 23 min |
| 3 | 3 | 10 min | 33 min |
| 4 | 22 | 15 min | 48 min |
| 5 | 20 | 20 min | 68 min |
| 6 | 0 | 30 min | 98 min |
| **Total** | **59** | **~100 min** | |

All computation fits within a single session. No HPC resources needed.

## 5.2 Computational Cost Estimate

Each 2D run at $N = 128$, $T = 5.0$, $\Delta t = 0.001$ takes approximately:

$$\text{steps} = T / \Delta t = 5000$$

$$\text{cost per step} \approx N^2 \times (\text{operator eval} + \text{linear solve}) \approx 128^2 \times 100\text{ FLOP} \approx 1.6 \times 10^6 \text{ FLOP}$$

$$\text{total per run} \approx 5000 \times 1.6 \times 10^6 = 8 \times 10^9 \text{ FLOP} \approx 8 \text{ seconds at 1 GFLOP/s}$$

The 3D runs at $N = 48$ cost $48^3 / 128^2 \approx 6.75\times$ per step (but fewer steps due to shorter $T$), giving comparable wall time.

## 5.3 Convergence Checks

### Spatial convergence

For each beta value, the converged result is determined by Richardson extrapolation:

$$\alpha_R^{\text{conv}} = \alpha_R(N_3) + \frac{\alpha_R(N_3) - \alpha_R(N_2)}{(N_3/N_2)^p - 1}$$

where $p = 2$ (second-order accuracy of the implicit Euler scheme with central-difference Laplacian).

### Temporal convergence

For the H-sweep, verify that halving $\Delta t$ does not change $\omega_{\text{peak}}$ by more than 2%. Run one confirmation at $H = 100$ with $\Delta t = 0.0005$.

### Mass conservation

At every run, verify $|M(T) - M(0)| / M(0) < 10^{-6}$. The implicit Euler scheme with Neumann BCs conserves mass to machine precision; any violation indicates a bug.

## 5.4 Reproducibility Harness Steps

### Before running experiments

```bash
# Verify clean environment
python -m edsim certify          # 9/9 phases must pass
pytest edsim/tests/ -v           # 112/112 tests must pass
python -c "import edsim; print(edsim.__version__)"  # Must be 0.1.0
```

### After running experiments

```bash
# Verify that the standard pipeline still passes
# (experiments must not have corrupted any global state)
python -m edsim certify
```

### Archival

All result JSON files include:
- `edsim_version` (pinned to 0.1.0)
- `timestamp` (ISO 8601)
- Full parameter dict (enables exact reproduction)
- Platform info (Python version, NumPy version)

---

# 6. Final Summary

## 6.1 What Completing These Sweeps Will Establish

**The beta-universality sweep** determines whether the ED mobility channel is a genuine generalisation of the PME across the full range $\beta \in [0.5, 5.0]$. If $\alpha_R = 1/(d\beta + 2)$ holds universally:

- The condensed-matter fit ($\beta = 2.00 \pm 0.29$) is not a special case but part of a continuous family.
- The front exponent becomes a diagnostic: measuring $\alpha_R$ in any experimental system constrains $\beta$.
- The ED constitutive law $M(\rho) = M_0(\rho_{\max} - \rho)^\beta$ is validated as a PME generator for all $\beta > 0$.

**The H-transition sweep** determines the structure of the participation channel's activation:

- Whether the onset is sharp (phase transition) or smooth (crossover).
- Whether $\omega \propto H^{1/2}$ (confirming the linear telegraph model).
- Whether ballistic propagation emerges at high $H$ (confirming the telegraph speed formula).
- Where the Lyapunov boundary lies (defining the safe region for the energy functional).

**The combined grid** produces the first phase diagram of the ED PDE, identifying the boundaries between PME-dominated, mixed, and telegraph-dominated dynamics.

## 6.2 What Would Falsify ED's Universality

**Level 1 (mobility channel):** If $\alpha_R$ deviates systematically from $1/(d\beta + 2)$ — not just at resolution-limited high $\beta$ but at well-resolved moderate $\beta$ values like 1.5 or 2.5 — then the ED-to-PME mapping $m = \beta + 1$ is incorrect. The constitutive law would need a correction term.

**Level 2 (participation channel):** If $\omega(H)$ does not scale as $H^{1/2}$, the linear telegraph model is wrong. This would imply that the participation coupling is nonlinear — $v(t)$ does not enter the $\rho$-equation linearly.

**Level 3 (architecture):** If Laws L2 (energy) and L5 (dissipation sum) fail at moderate $H$ ($H < 10$) and moderate $\beta$ ($\beta \leq 3$), the ED energy functional is not a Lyapunov function for the coupled system in a physically relevant parameter range. This would be a fundamental architectural limitation.

**Level 4 (phase structure):** If no distinct regions are identifiable — if all observables change smoothly with no qualitative transitions — then the "phase diagram" is a smooth landscape rather than a phase structure. This is not a falsification of ED but would significantly reduce the framework's predictive sharpness.

## 6.3 Connection to ED-Phys-05 and ED-Cosmo-01

**ED-Phys-05 (Participation Field)** established that $v(t)$ is the mean Madelung velocity and $H = 2\omega_C$ in the quantum regime. ED-Phys-06 now asks: is the quantum regime ($\beta = 2$, $H = 2\omega_C$) inside the "safe region" where all nine laws hold? The answer depends on the nondimensional value of $H$ after rescaling by $T_0$ and $L_0$. The Lyapunov boundary $H_{\text{Lyap}}(\beta = 2)$ from the grid experiment directly determines this.

If $H_{\text{Lyap}}(\beta = 2) \gg H_{\text{nondim}}^{\text{quantum}}$: the quantum regime is deep inside the safe region, and all architectural laws apply. The Compton anchoring is fully consistent with the energy structure.

If $H_{\text{Lyap}}(\beta = 2) \lesssim H_{\text{nondim}}^{\text{quantum}}$: the quantum regime is at or beyond the Lyapunov boundary. This would mean quantum ED operates in the telegraph-dominated region where energy monotonicity may not hold — a physically significant prediction about the relationship between quantum coherence and the ED energy landscape.

**ED-Cosmo-01 (Cosmological Limit)** requires knowing whether the cosmological regime ($D = c^2/H_0$, $H_{\text{ED}} = H_0$) falls in the PME, mixed, or telegraph region of the phase diagram. The $(\beta, H)$ grid provides the map. The nondimensional cosmological $H$ (after rescaling) determines the regime. If cosmological ED is in Region IV (telegraph-dominated), the Friedmann-like dynamics predicted in ED-Phys-05 (oscillatory $q(z)$, expansion damping) are structurally supported by the phase diagram.

The execution phase of ED-Phys-06 provides the quantitative infrastructure — the phase boundaries, the critical surfaces, the universality confirmation — that makes the theoretical predictions of ED-Phys-05 and ED-Cosmo-01 precise and testable.

---

*ED-Phys-06 Execution Phase · Event Density Research Programme · March 2026*
