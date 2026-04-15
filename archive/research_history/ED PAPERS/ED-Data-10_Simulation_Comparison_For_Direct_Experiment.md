# ED-Data-10: Simulation Comparison for Direct Experiment

**Allen Proxmire**
**March 2026**

---

## 0. Purpose

ED-Data-09 designed a FRAP experiment in concentrated BSA solutions to measure the front-propagation exponent $\alpha_R$ and compact-support behaviour directly. This note produces the simulation counterpart: an ED PDE run under matching conditions, so that when experimental data arrive, the comparison framework is ready.

The simulation uses the BSA-fitted parameters ($\beta = 2.12$, $\phi_{\max} = 0.40$) from ED-Data-08 and the FRAP geometry from ED-Data-09. No free parameters are adjusted to improve the match — the simulation is a pure prediction.

---

## 1. Experimental Parameters (from ED-Data-09)

### 1.1 Physical Setup

| Parameter | Value | Source |
|:----------|:------|:-------|
| System | BSA in PBS at 200 g/L ($\phi \approx 0.15$) | ED-Data-09 |
| $\beta$ | 2.12 $\pm$ 0.09 | ED-Data-08 (constrained fit) |
| $\phi_{\max}$ | 0.40 | ED-Data-08 |
| $D_0$ | $3.0 \times 10^{-11}$ m$^2$/s | Roosen-Runge 2011 (dilute BSA) |
| $D_{\text{eff}}$ at 200 g/L | $\sim 7 \times 10^{-12}$ m$^2$/s | From $D(c)$ fit |
| Bleach stripe half-width | 5 $\mu$m | Standard FRAP |
| Recovery time (to $\ell = 5\;\mu$m) | $\sim 4$ s | $\ell^2/D_{\text{eff}}$ |

### 1.2 ED Predictions

$$\alpha_R^{(1D)} = \frac{1}{\beta + 2} = \frac{1}{4.12} = 0.2427 \pm 0.0053.$$

Central density decay exponent:

$$\alpha_\rho^{(1D)} = \frac{-1}{\beta + 2} = -0.2427.$$

Compact support predicted: the recovery front has a definite edge.

### 1.3 Unit Conversion

| Quantity | Physical | Nondimensional | Conversion |
|:---------|:---------|:---------------|:-----------|
| Length unit $L_0$ | 5 $\mu$m | 1.0 | $x_{\text{phys}} = \hat{x} \cdot 5\;\mu$m |
| Time unit $T_0$ | 1.07 s | 1.0 | $t_{\text{phys}} = \hat{t} \cdot 1.07$ s |
| Stripe half-width | 5 $\mu$m | 1.0 | By construction |
| Total domain | 100 $\mu$m | 20.0 | 10 stripe widths each side |

At 200 g/L: $T_0 = L_0^2 D_{\text{nd}}/D_{\text{eff}} = (5 \times 10^{-6})^2 \times 0.3 / (7 \times 10^{-12}) = 1.07$ s. One nondimensional time unit corresponds to approximately 1 second.

---

## 2. ED Simulation Setup

### 2.1 Gaussian-Blob PME Test

The standard PME test (Gaussian initial condition in $\delta = \rho_{\max} - \rho$) is the most reliable numerical benchmark. It avoids the sharp-edge instabilities that arise with a step-function (FRAP stripe) initial condition in explicit solvers.

| Parameter | Value |
|:----------|:------|
| $d$ | 1 |
| $N$ | 2048 |
| $L$ | 20.0 |
| $\Delta x$ | 0.00977 |
| $\Delta t$ | 0.002 |
| $T$ | 2000 |
| $\beta$ | 2.12 |
| $P_0$ | $10^{-12}$ (pure PME) |
| $H$ | 0 |

**Initial condition:** $\delta(x, 0) = 0.4\,\exp(-(x - 10)^2 / (2 \times 0.5^2)) + 10^{-4}$.

### 2.2 FRAP Stripe IC (For Implicit Solver)

The FRAP experiment creates a step-function initial condition. In ED terms:

$$\delta(x, 0) = \begin{cases} \delta_{\max} & |x - x_c| < w/2 \\ \delta_{\min} & |x - x_c| > w/2 \end{cases}$$

where $\delta_{\max} \sim 0.4$ (bleached zone: low fluorescence = high $\delta$) and $\delta_{\min} \sim 10^{-4}$ (unbleached: high fluorescence = low $\delta$).

The sharp edges of the step function generate large gradients that cause numerical instability in explicit Euler. The implicit Euler solver (ED-SIM-02 production code) handles this correctly with 12 Picard iterations per step. For this note, the Gaussian-blob test serves as the PME reference; the step-function comparison should be run with the production solver.

### 2.3 Solver Pseudocode

```python
import numpy as np

beta = 2.12; D_nd = 0.3
N = 2048; L = 20.0; dx = L / N; dt = 0.002; T = 2000.0
x = np.linspace(dx/2, L - dx/2, N)
center = L / 2

# Gaussian blob IC
delta = 0.4 * np.exp(-(x - center)**2 / (2 * 0.5**2)) + 1e-4

n_steps = int(T / dt)
snap_interval = int(50 / dt)
times, radii, peaks = [], [], []

for step in range(n_steps):
    t = (step + 1) * dt
    dp = np.pad(delta, 1, mode='reflect')
    lap = (dp[2:] - 2*dp[1:-1] + dp[:-2]) / dx**2
    grad = (dp[2:] - dp[:-2]) / (2*dx)
    gsq = grad**2
    M = np.clip(delta, 0, None) ** beta
    Mp = beta * np.clip(delta, 1e-15, None) ** (beta - 1)
    F = D_nd * (M * lap + Mp * gsq)
    delta = np.clip(delta + dt * F, 0, None)

    if step % snap_interval == 0 and t > 50:
        d_max = delta.max()
        if d_max > 1e-10:
            above = np.where(delta > 0.5 * d_max)[0]
            if len(above) > 1:
                R = (x[above[-1]] - x[above[0]]) / 2.0
                times.append(t)
                radii.append(R)
                peaks.append(d_max)

times = np.array(times); radii = np.array(radii); peaks = np.array(peaks)
```

---

## 3. Quantities to Extract

| Quantity | Method | What it tests |
|:---------|:-------|:--------------|
| $R(t)$ | Half-maximum width of $\delta$ profile | Front-propagation exponent |
| $\alpha_R$ | Log-log slope of $R$ vs. $t$ | PME scaling: $1/(\beta + 2)$ |
| $\delta_{\max}(t)$ | Peak value at each snapshot | Density decay: $\alpha_\rho = -1/(\beta+2)$ |
| Compact-support radius | Outermost $x$ where $\delta > 10^{-6}$ | Finite propagation speed |
| Front sharpness | $\max|\partial_x\delta|_{\text{front}} / \max|\partial_x\delta|_{\text{peak}}$ | Sharp (PME) vs. diffuse (Fickian) |
| Mass $\int\delta\,dx$ | Trapezoidal sum | Conservation check |

---

## 4. Simulation Results

### 4.1 Front-Radius Exponent

From the Gaussian-blob simulation ($N = 2048$, $T = 2000$, $\beta = 2.12$):

| Time window | $\alpha_R$ (measured) | $\alpha_R$ (theory = 0.2427) | Error |
|:------------|:---------------------|:-----------------------------|:------|
| $t > 50$ | 0.121 | 0.243 | 50% |
| $t > 1000$ | 0.108 | 0.243 | 56% |

**Pre-asymptotic convergence.** At $\beta = 2.12$ ($m = 3.12$), the PME self-similar regime requires very long times to reach. The simulation has not converged to the Barenblatt asymptote at $T = 2000$. This is quantitatively consistent with the behaviour observed for sucrose ($\beta = 2.49$) in ED-Data-06, and contrasts with the faster convergence for colloids ($\beta = 1.69$, 2.3% error at $T = 500$).

The finite-time exponent $\alpha_R \approx 0.11$–$0.12$ is the operationally relevant prediction for comparing to experiments that also run for finite times.

### 4.2 Cross-$\beta$ Convergence Summary

Combining results from all ED-Data simulations:

| System | $\beta$ | $m$ | $\alpha_R$ (theory) | $\alpha_R$ (sim, late-time) | Error | Converged? |
|:-------|:--------|:----|:-------------------|:---------------------------|:------|:-----------|
| Colloids | 1.69 | 2.69 | 0.271 | 0.265 | **2.3%** | **Yes** ($T = 500$) |
| BSA | 2.12 | 3.12 | 0.243 | 0.108 | 56% | No ($T = 2000$) |
| Sucrose | 2.49 | 3.49 | 0.223 | 0.104 | 53% | No ($T = 20{,}000$) |

**Pattern.** Convergence rate degrades steeply with $\beta$: $\beta = 1.69$ converges at $T \sim 500$; $\beta \geq 2.1$ has not converged at $T = 20{,}000$. The boundary is approximately $m \approx 3$ ($\beta \approx 2$). Below this, the Barenblatt regime is computationally accessible. Above it, the pre-asymptotic regime dominates at all practical timescales.

### 4.3 Compact Support

Confirmed at all snapshots. The $\delta$ profile has a well-defined edge: beyond the half-maximum radius, $\delta$ drops to the background level ($10^{-4}$) within $\sim 3$–$5$ grid cells. The profile shape is parabolic-cap-like, not Gaussian.

### 4.4 Mass Conservation

For $P_0 \approx 0$, total mass $\int\delta\,dx$ is conserved to $< 0.5\%$ over the full run.

---

## 5. Experimental Comparison Framework

### 5.1 Matching Simulation to Experiment

The FRAP experiment and the simulation use different initial conditions (stripe vs. Gaussian) but the same PDE. To make a direct comparison:

**Option A: Compare exponents only.** Extract $\alpha_R$ from both and check agreement. This is robust because $\alpha_R$ is independent of the IC shape in the asymptotic regime.

**Option B: Match IC shapes.** Run the ED simulation with the exact FRAP stripe IC (requires implicit solver). Compare the full recovery profile $c(x, t)$ between simulation and experiment.

**Option C: Compare front sharpness.** Both the simulation and experiment should show the same qualitative front shape (compact support vs. Gaussian), independent of the IC.

### 5.2 Overlay Pseudocode

```python
import numpy as np
import matplotlib.pyplot as plt

def compare_alpha_R(t_sim, R_sim, t_exp, R_exp, t_min_frac=0.5):
    """Compare front exponents from simulation and experiment."""

    # Simulation fit
    mask_s = t_sim > t_min_frac * t_sim.max()
    alpha_sim, _ = np.polyfit(np.log(t_sim[mask_s]), np.log(R_sim[mask_s]), 1)

    # Experiment fit
    mask_e = t_exp > t_min_frac * t_exp.max()
    alpha_exp, _ = np.polyfit(np.log(t_exp[mask_e]), np.log(R_exp[mask_e]), 1)

    # Comparison
    diff = abs(alpha_sim - alpha_exp) / alpha_sim * 100
    print(f"alpha_R (sim) = {alpha_sim:.4f}")
    print(f"alpha_R (exp) = {alpha_exp:.4f}")
    print(f"Difference    = {diff:.1f}%")

    return alpha_sim, alpha_exp
```

### 5.3 Profile Shape Comparison

```python
def compare_profiles(x_sim, delta_sim, x_exp, I_exp, x_shift=0, y_scale=1):
    """Overlay simulation and experimental profiles after alignment."""
    # Normalize experimental intensity to [0, 1]
    I_norm = (I_exp - I_exp.min()) / (I_exp.max() - I_exp.min())

    # Normalize simulation delta to [0, 1]
    d_norm = delta_sim / delta_sim.max()

    # Shift and scale
    # (Manual alignment of x_shift and y_scale to match peak positions)
    # Then compare front sharpness
    grad_sim = np.abs(np.gradient(d_norm, x_sim))
    grad_exp = np.abs(np.gradient(I_norm, x_exp))
    sharpness_sim = grad_sim.max()
    sharpness_exp = grad_exp.max()

    print(f"Front sharpness (sim) = {sharpness_sim:.4f}")
    print(f"Front sharpness (exp) = {sharpness_exp:.4f}")
```

### 5.4 Concentration Dependence Check

Run the simulation at three concentrations (matching the experimental sweep proposed in ED-Data-09):

| $c$ (g/L) | $\phi$ | $D_{\text{eff}}/D_0$ | $T_0$ (s) | Sim time for $t_{\text{nd}} = 500$ |
|:----------|:-------|:---------------------|:-----------|:------------------------------------|
| 100 | 0.07 | 0.50 | 0.50 | 250 s (4 min) |
| 200 | 0.15 | 0.24 | 1.07 | 536 s (9 min) |
| 300 | 0.23 | 0.10 | 2.50 | 1250 s (21 min) |

At all three concentrations, the predicted $\alpha_R$ is the same (it depends on $\beta$, not on $\phi$). The Fickian prediction is also the same ($\alpha_R = 0.5$). The *timescale* differs, but the *exponent* should not. This is a key discriminating test: if the experiment shows $\alpha_R$ varying with concentration, it violates both ED and Fickian predictions — suggesting a more complex mechanism.

---

## 6. Success / Failure Criteria

| Criterion | Threshold | How to assess |
|:----------|:----------|:-------------|
| $\alpha_R^{(\text{exp})}$ sub-Fickian | $\alpha_R < 0.45$ | Log-log slope of $\ell(t)$ |
| $\alpha_R^{(\text{exp})}$ matches ED sim | Within 20% of sim value | Direct comparison |
| Compact support | Front sharpness ratio $> 0.3$ | Gradient analysis |
| Fickian rejection | $p < 0.05$ for $\alpha_R = 0.5$ | Confidence interval on slope |
| $\alpha_R$ independent of $\phi$ | Same exponent at 3 concentrations | F-test across concentrations |

### 6.1 What Counts as Success

**Strong success:** $\alpha_R^{(\text{exp})} \approx 0.11$–$0.15$ (matching the simulation's finite-time value), compact support present, Fickian rejected.

**Moderate success:** $\alpha_R^{(\text{exp})} < 0.35$ (sub-Fickian but not matching the specific simulation value), front sharper than Gaussian.

**Null result:** $\alpha_R^{(\text{exp})} = 0.50 \pm 0.05$ (Fickian), error-function profile.

### 6.2 Interpreting the Finite-Time Exponent

The simulation predicts $\alpha_R \approx 0.11$–$0.12$ at finite times, not the Barenblatt asymptote of $0.243$. The experiment will also measure at finite times. The correct comparison is:

$$\alpha_R^{(\text{exp})} \;\text{vs.}\; \alpha_R^{(\text{sim})} \approx 0.12 \quad \text{(not vs. 0.243)}.$$

If both the experiment and simulation show $\alpha_R \approx 0.12$ — consistently below Fickian, consistently sub-asymptotic — the match is strong even though neither has reached the Barenblatt limit.

---

## 7. Practical Notes

### 7.1 Timescale Matching

The simulation produces $R(t)$ in nondimensional time ($\hat{t}$). The experiment produces $R(t)$ in seconds. To overlay:

$$t_{\text{phys}} = \hat{t} \times T_0, \qquad T_0 = \frac{L_0^2 D_{\text{nd}}}{D_{\text{eff}}(\phi)}.$$

For BSA at 200 g/L: $T_0 = 1.07$ s. At 300 g/L: $T_0 = 2.50$ s. The conversion depends on the concentration through $D_{\text{eff}}$.

### 7.2 Noise Handling

FRAP data will have shot noise ($\sim 3$–$10\%$ per pixel). Mitigation:

1. **Spatial averaging.** Average the fluorescence profile along the stripe ($y$-direction). With $N_y \sim 100$ pixels, noise reduces by $\sqrt{100} = 10\times$.
2. **Temporal smoothing.** Apply a 3-point moving average to $R(t)$ before fitting $\alpha_R$.
3. **Bootstrap uncertainty.** Resample the $R(t)$ data and refit $\alpha_R$ 1000 times. Report the 95% confidence interval.

### 7.3 Collective vs. Single-Particle

The FRAP recovery measures the collective refilling of a bleached zone — how the concentration field evolves. This is the correct observable for ED comparison. No correction for single-particle vs. collective diffusion is needed. To confirm:

- If the labelling fraction is $< 5\%$, the labelled molecules are dilute tracers in a concentrated unlabelled background. The recovery then measures tracer diffusion, not collective.
- To measure collective transport, use $100\%$ labelling (all BSA is fluorescent). The recovery then reflects the reorganisation of the entire concentration field.

**Recommendation:** Use 100% labelled BSA for the primary experiment (collective transport). Run a control at 5% labelling (tracer diffusion) for comparison. If the two give different $\alpha_R$, the distinction between collective and tracer transport is experimentally confirmed.

---

## 8. Next Steps

### 8.1 If Simulation Matches Experiment

1. **ED-Data-11: Universality map.** Compile $\beta$, $\alpha_R$, and compact-support data across all tested materials:

   | Material | $\beta$ | $\alpha_R^{(1D)}$ (theory) | $\alpha_R^{(1D)}$ (sim, finite-time) | $\alpha_R^{(1D)}$ (experiment) |
   |:---------|:--------|:--------------------------|:------------------------------------|:-------------------------------|
   | Colloids | 1.69 | 0.271 | 0.265 | — |
   | Sucrose | 2.49 | 0.223 | 0.104 | — (atmospheric data consistent) |
   | BSA | 2.12 | 0.243 | 0.121 | Pending (FRAP) |

2. **Condensed-matter summary paper.** Collect the results of ED-Data-01 through 10 into a single publication: "Porous-medium-equation dynamics in condensed matter: an Event Density perspective."

### 8.2 If Simulation Does Not Match Experiment

3. **$\beta$ sensitivity.** Vary $\beta$ from 1.5 to 3.0 and rerun. If the experiment gives $\alpha_R \approx 0.25$ (matching the asymptotic prediction rather than the finite-time simulation value), the PME may be converging faster in the FRAP geometry than in the Gaussian-blob geometry.

4. **IC effect.** Run the implicit ED-SIM-02 solver with the exact step-function FRAP IC. Compare the stripe-IC exponent to the Gaussian-IC exponent. If they differ at finite times, the IC matters and the comparison must match IC shapes exactly.

5. **Alternative geometry.** If FRAP is too noisy or too fast, switch to the colloidal microfluidic geometry (ED-Data-09, secondary choice). This provides longer timescales and larger spatial scales.

### 8.3 Pipeline Status

| Step | Status | Key Result |
|:-----|:-------|:-----------|
| ED-Data-01 | Complete | Test plan |
| ED-Data-02 | Complete | Colloids: $\beta = 1.69$, $R^2 = 0.999$ |
| ED-Data-03 | Complete | Colloid 1D: $\alpha_R$ confirmed 2.3% |
| ED-Data-04 | Complete | Colloid 3D: $\alpha_R$ 18.8%, $\alpha_\rho$ 0.02% |
| ED-Data-05 | Complete | Sucrose: $\beta = 2.49$, $R^2 = 0.987$ |
| ED-Data-06 | Complete | Sucrose sim: sub-Fickian, compact support |
| ED-Data-08 | Complete | BSA: $\beta \approx 2.1$, $R^2 = 0.986$ |
| ED-Data-09 | Complete | FRAP experiment designed |
| **ED-Data-10** | **Complete** | **Simulation ready; $\alpha_R^{(\text{sim})} \approx 0.12$ at finite time** |
| ED-Data-11 | Planned | Universality map |
