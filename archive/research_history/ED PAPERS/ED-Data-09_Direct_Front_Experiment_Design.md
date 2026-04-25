# ED-Data-09: Direct Front-Propagation Experiment Design

**Allen Proxmire**
**March 2026**

---

## 0. Purpose

The ED-Data pipeline has established that the mobility law $D(c) = D_0(1 - c/c_{\max})^\beta$ fits three chemically distinct materials with $R^2 > 0.98$ and $\beta \approx 1.7$–$2.5$. The front-propagation exponent $\alpha_R = 1/(d\beta + 2)$ has been confirmed by simulation to 2.3% in 1D (colloids) and 18.8% in 3D (colloids). But no experiment has yet measured $\alpha_R$ directly in a system designed to test the ED prediction.

This note designs that experiment. The objective is to measure the collective spreading of a macroscopic concentration front in a nonlinear-diffusion medium and extract $\alpha_R$ from the data. This is not single-particle tracking (which measures tracer diffusion) — it is collective transport (which measures how a concentration profile evolves), the quantity that the ED PDE directly governs.

If the measured $\alpha_R$ matches the ED prediction using the $\beta$ fitted from $D(c)$ data — with zero additional free parameters — it is the first purpose-built experimental confirmation of the ED framework.

---

## 1. Experimental Concept

### 1.1 The Core Idea

1. Prepare a medium with known concentration-dependent diffusivity $D(c) \propto (1 - c/c_{\max})^\beta$.
2. Create a sharp, localised concentration perturbation (a "pulse" or "step") within the medium.
3. Let it spread by diffusion alone (no flow, no convection, no external forces).
4. Image the concentration profile $c(x, t)$ at regular time intervals.
5. Extract the front radius $R(t)$ from the evolving profile.
6. Fit $R(t) = A \cdot t^{\alpha_R}$ and compare $\alpha_R$ to $1/(d\beta + 2)$.

### 1.2 Why This Tests ED

Standard (Fickian) diffusion predicts $R(t) \propto t^{0.5}$ regardless of the medium. The ED-PME prediction is $R(t) \propto t^{\alpha_R}$ with $\alpha_R < 0.5$, and the front should have compact support (a sharp edge, not Gaussian tails). Both the exponent and the front shape are distinct from Fickian behaviour. A single experiment that measures both provides a double test.

### 1.3 What "Collective Transport" Means

Single-particle tracking (DLS, FCS, particle tracking) measures how one labelled particle moves through a crowd. The ED PDE describes how the crowd itself reorganises — how a macroscopic density profile evolves. The two quantities are related but not identical (collective diffusion includes cooperative effects). The experiment must measure the evolution of a *concentration field*, not the trajectory of individual particles.

---

## 2. Candidate Systems

### 2.1 Concentrated Colloidal Suspension (PMMA Hard Spheres)

| Property | Assessment |
|:---------|:----------|
| $\beta$ (from ED-Data-02) | 1.69 |
| Predicted $\alpha_R^{(1D)}$ | 0.271 |
| Front creation | Microfluidic injection of labelled vs. unlabelled colloids |
| Imaging | Confocal fluorescence microscopy |
| Front sharpness | Good — colloids are easily distinguished by fluorescent label |
| Timescale | $R \sim 100\;\mu$m over minutes to hours at $\phi \sim 0.40$ |
| Convection risk | Low if density-matched (buoyancy-neutral) |

**Verdict:** Excellent. Best-characterised system, strongest ED data basis.

### 2.2 Concentrated Protein Solution (BSA)

| Property | Assessment |
|:---------|:----------|
| $\beta$ (from ED-Data-08) | $\sim 2.1$ (constrained) |
| Predicted $\alpha_R^{(1D)}$ | 0.243 |
| Front creation | FRAP (photobleach a stripe in fluorescently labelled BSA) |
| Imaging | Fluorescence microscopy |
| Front sharpness | Moderate — bleach boundary is $\sim 1$–$5\;\mu$m wide |
| Timescale | $R \sim 10\;\mu$m over seconds to minutes at 200 g/L |
| Convection risk | Low (aqueous, small temperature gradients) |

**Verdict:** Good. FRAP geometry is well-established. Faster timescale than colloids.

### 2.3 PEG-Water in a Thin Channel

| Property | Assessment |
|:---------|:----------|
| $\beta$ | Not yet fitted (expected $\sim 1$–$2$) |
| Predicted $\alpha_R^{(1D)}$ | $\sim 0.25$–$0.33$ |
| Front creation | Microfluidic T-junction: inject concentrated PEG against dilute buffer |
| Imaging | Refractive-index gradient (Schlieren) or fluorescent dye |
| Front sharpness | Good if microfluidics are well-controlled |
| Timescale | $R \sim 100\;\mu$m over minutes at 30 wt% PEG |
| Convection risk | Moderate (density difference between concentrated and dilute PEG) |

**Verdict:** Feasible but requires microfluidic expertise. Convection is a concern.

### 2.4 Sucrose-Water in a Capillary

| Property | Assessment |
|:---------|:----------|
| $\beta$ (from ED-Data-05) | 2.49 |
| Predicted $\alpha_R^{(1D)}$ | 0.223 |
| Front creation | Fill one half of a capillary with concentrated sucrose, the other with dilute |
| Imaging | Optical absorption of a food dye co-dissolved with sucrose |
| Front sharpness | Depends on initial interface quality |
| Timescale | Very slow at high concentration ($D \sim 10^{-12}$ m$^2$/s at 60 wt%). For $R \sim 100\;\mu$m: $t \sim R^2/D \sim 10^4$ s ($\sim 3$ h) at moderate concentration, days at high concentration. |
| Convection risk | **High** — sucrose solutions have strong density gradients. Must orient capillary horizontally. |

**Verdict:** Simplest equipment but slowest experiment and highest convection risk.

---

## 3. Recommended Experiment

### 3.1 Primary Choice: FRAP in Concentrated BSA

**Justification:**

1. **Speed.** FRAP recovery in concentrated protein solutions takes seconds to minutes — fast enough for a complete dataset in one session.
2. **Geometry control.** The bleach stripe defines a clean 1D initial condition. The recovery is 1D (perpendicular to the stripe).
3. **No flow.** The sample is static. No convection, no microfluidics needed.
4. **Equipment.** Requires only a confocal fluorescence microscope with a bleaching laser — standard in any biophysics lab.
5. **Direct connection.** FRAP measures collective recovery of a concentration profile, not single-particle diffusion.

### 3.2 Secondary Choice: Colloidal Front in Microfluidic Channel

If FRAP is not available, a microfluidic experiment with density-matched PMMA colloids at $\phi \sim 0.40$ provides a direct 1D front measurement with confocal imaging.

---

## 4. Experimental Protocol (FRAP in Concentrated BSA)

### 4.1 Sample Preparation

1. **Protein:** BSA (bovine serum albumin), MW $\approx 66$ kDa. Use BSA-Alexa488 (fluorescently labelled) at 1–5% of total BSA. Mix with unlabelled BSA to target concentrations.

2. **Concentrations:** Prepare samples at $c = 100$, $150$, $200$, $250$, $300$ g/L (corresponding to $\phi \approx 0.07$, $0.11$, $0.15$, $0.19$, $0.23$).

3. **Buffer:** PBS at pH 7.4, $I = 0.15$ M (screens electrostatic interactions; system behaves as "effective hard spheres").

4. **Chamber:** Seal $\sim 5\;\mu$L of sample between a microscope slide and coverslip with a $\sim 20\;\mu$m spacer. This creates a thin film that suppresses convection and confines the measurement to quasi-2D.

### 4.2 Bleaching Protocol

1. **Pre-bleach image:** Acquire a uniform fluorescence image. This is the $c_0$ reference.

2. **Bleach:** Use a high-intensity laser line ($\sim 488$ nm) to bleach a rectangular stripe of width $w \sim 5$–$10\;\mu$m across the field of view. The bleach creates a "concentration step" in fluorescent molecules: $c = 0$ inside the stripe, $c = c_0$ outside.

3. **Recovery imaging:** Immediately after bleaching, acquire fluorescence images at intervals $\Delta t$ for a total time $T$:

   | $c$ (g/L) | Expected $D_{\text{eff}}$ (m$^2$/s) | $\Delta t$ | $T$ |
   |:----------|:-------------------------------------|:-----------|:----|
   | 100 | $\sim 3 \times 10^{-11}$ | 0.5 s | 60 s |
   | 200 | $\sim 7 \times 10^{-12}$ | 2 s | 300 s |
   | 300 | $\sim 1 \times 10^{-12}$ | 10 s | 1500 s |

### 4.3 The Initial Condition

The bleach stripe creates a 1D concentration dip:

$$c(x, 0) = c_0 \cdot \begin{cases} 0 & |x - x_0| < w/2 \\ 1 & |x - x_0| > w/2 \end{cases}$$

In ED terms: $\delta(x, 0) = c_0$ inside the stripe (depleted zone), $\delta(x, 0) = 0$ outside (unperturbed). The recovery is the spreading of the surrounding fluorescent molecules into the bleached region — a PME front propagating inward from both edges.

---

## 5. Measurement Pipeline

### 5.1 From Images to $R(t)$

At each time point $t_i$, the fluorescence image $I(x, y, t_i)$ encodes the local fluorescent concentration. The recovery front is extracted from the 1D profile $I(x, t)$ averaged along the stripe direction ($y$).

```python
import numpy as np

def extract_R_from_FRAP(images, x_coords, t_coords, bleach_center, threshold=0.5):
    """
    Extract front radius R(t) from FRAP image stack.

    images: 3D array (n_times, n_x, n_y)
    x_coords: 1D array of x positions
    t_coords: 1D array of time points
    bleach_center: x coordinate of bleach stripe center
    threshold: fraction of full recovery (0.5 = half-max)
    """
    # Average along y (stripe direction)
    profiles = images.mean(axis=2)  # (n_times, n_x)

    # Normalize: 0 = bleached, 1 = fully recovered
    I_pre = profiles[0]  # pre-bleach reference
    I_min = profiles[1].min()  # immediately post-bleach
    profiles_norm = (profiles - I_min) / (I_pre.mean() - I_min)

    R_list = []
    for i, t in enumerate(t_coords):
        profile = profiles_norm[i]
        # Find the recovery front: where profile crosses threshold
        # on both sides of the bleach center
        left = x_coords < bleach_center
        right = x_coords > bleach_center

        # Left front: rightmost x where profile < threshold
        below_left = np.where(profile[left] < threshold)[0]
        if len(below_left) > 0:
            x_left = x_coords[left][below_left[-1]]
        else:
            x_left = bleach_center

        # Right front: leftmost x where profile < threshold
        below_right = np.where(profile[right] < threshold)[0]
        if len(below_right) > 0:
            x_right = x_coords[right][below_right[0]]
        else:
            x_right = bleach_center

        # Front "radius" = half the unrecovered width
        R = (x_right - x_left) / 2.0
        R_list.append(R)

    return np.array(R_list)
```

### 5.2 From $R(t)$ to $\alpha_R$

The bleached stripe *shrinks* as fluorescent molecules diffuse in from the edges. The unrecovered width $W(t) = 2R(t)$ decreases over time. For Fickian diffusion, $W(t) \propto W_0 - C\sqrt{t}$. For PME, the recovery front advances as $t^{\alpha_R}$ with $\alpha_R < 0.5$.

The measurable quantity is the *advance of the recovery front* from the initial bleach edge:

$$\ell(t) = W_0/2 - R(t) \propto t^{\alpha_R}.$$

```python
def fit_alpha_R(t_data, ell_data, t_min_frac=0.1):
    """Fit front advance to power law."""
    mask = t_data > t_min_frac * t_data.max()
    log_t = np.log(t_data[mask])
    log_ell = np.log(ell_data[mask])
    alpha_R, log_A = np.polyfit(log_t, log_ell, 1)
    return alpha_R
```

### 5.3 Front Shape Analysis

At each time point, examine the profile shape:

- **Fickian (error function):** The front has smooth, exponential tails extending far into the bleached zone.
- **PME (compact support):** The front has a sharp boundary. Beyond the front, the profile is flat (no recovery yet).

```python
def front_sharpness(profile, x_coords, threshold=0.5):
    """Measure sharpness: gradient at front / gradient at peak."""
    grad = np.gradient(profile, x_coords)
    peak_grad = np.max(np.abs(grad))
    # Find front location (threshold crossing)
    front_idx = np.argmin(np.abs(profile - threshold * profile.max()))
    front_grad = np.abs(grad[front_idx])
    return front_grad / peak_grad  # > 0.3 suggests compact support
```

---

## 6. Expected ED Predictions

### 6.1 Front Advance Exponent

Using $\beta = 2.0$ (canonical ED value, consistent with all three material fits):

| $d$ | $\alpha_R$ | Fickian $\alpha_R$ | Ratio |
|:----|:-----------|:-------------------|:------|
| 1 | 0.250 | 0.500 | 0.50 |
| 2 | 0.167 | 0.500 | 0.33 |
| 3 | 0.125 | 0.500 | 0.25 |

The FRAP experiment in a thin film is quasi-1D (the bleach stripe is much longer than wide), so the relevant prediction is $\alpha_R^{(1D)} = 0.250$.

### 6.2 Compact Support

The recovery front should have a definite edge. At time $t$, the profile should show:

- A flat, fully recovered region far from the bleach centre.
- A steep front advancing at rate $\propto t^{\alpha_R - 1}$.
- A flat, unrecovered region inside the front (within the bleached zone).

The Fickian prediction is an error-function profile with gradual tails on both sides. The PME prediction is a parabolic-cap profile with a sharp boundary.

### 6.3 Concentration Dependence

At higher BSA concentration ($\phi$ closer to $\phi_{\max}$), the ED prediction becomes more distinct from Fickian:

- Lower effective $\alpha_R$ (slower recovery).
- Sharper front (stronger nonlinear mobility suppression).
- Longer time to full recovery.

Running the experiment at multiple concentrations (100, 200, 300 g/L) provides a built-in consistency check: the $\alpha_R$ at each concentration should be consistent with the $\beta$ fitted from the $D(\phi)$ curve.

---

## 7. Practical Considerations

### 7.1 Noise and Drift

- **Shot noise:** Fluorescence microscopy has Poisson noise. At typical photon counts ($\sim 100$–$1000$ per pixel), the SNR is $\sim 10$–$30$. Averaging along the stripe ($y$-direction) improves this by $\sqrt{N_y}$.
- **Stage drift:** Thermal drift can shift the field of view by $\sim 0.1\;\mu$m/min. Correct by tracking fiducial markers (fluorescent beads attached to the coverslip).
- **Photobleaching during imaging:** Repeated imaging bleaches the sample further. Keep the imaging laser power low ($\sim 1$–$5\%$ of bleach power) and minimise the number of frames.

### 7.2 Ensuring Collective Transport

FRAP measures collective recovery: the fluorescent concentration profile is a macroscopic field, not a single-particle trajectory. The recovery rate reflects how the *concentration front* propagates, which is the quantity the ED PDE describes. No correction for single-particle vs. collective diffusion is needed.

However, ensure that:
- The bleach is uniform along the stripe (no 3D gradients through the film thickness).
- The labelling fraction is low enough ($< 5\%$) that labelled and unlabelled BSA have the same diffusivity.
- The sample is at thermal equilibrium (no temperature gradients from the bleach laser).

### 7.3 Timescales

| Concentration (g/L) | $D_{\text{eff}}$ (m$^2$/s) | Time for $\ell = 5\;\mu$m | Regime |
|:---------------------|:---------------------------|:--------------------------|:-------|
| 100 | $\sim 3 \times 10^{-11}$ | $\sim 1$ s | Fast; pre-asymptotic |
| 200 | $\sim 7 \times 10^{-12}$ | $\sim 4$ s | Moderate |
| 300 | $\sim 1 \times 10^{-12}$ | $\sim 25$ s | Slow; closer to asymptotic |

The higher concentrations provide better access to the sub-Fickian regime because the nonlinear mobility effect is stronger. The trade-off is longer experiment time and lower signal (more bleaching).

**Recommendation.** Run at 200 g/L as the primary concentration: fast enough for a clean dataset ($\sim 5$ min total), slow enough for the nonlinear effect to be measurable.

---

## 8. Success / Failure Criteria

| Criterion | Threshold | How to measure |
|:----------|:----------|:---------------|
| $\alpha_R$ within 20% of $0.250$ | $\alpha_R \in [0.20, 0.30]$ | Log-log slope of $\ell(t)$ |
| Sub-Fickian? | $\alpha_R < 0.45$ (rejecting $0.5$ at $2\sigma$) | Statistical test on slope |
| Compact support? | Front sharpness ratio $> 0.3$ | Profile gradient analysis |
| Fickian rejection | $p < 0.05$ for $\alpha_R = 0.5$ | $t$-test or confidence interval |
| Concentration dependence | $\alpha_R$ decreases with $\phi$ | Trend across 3+ concentrations |

**A successful experiment** produces:
1. $\alpha_R$ in $[0.20, 0.30]$ at $c = 200$ g/L.
2. Measurably sharper front than the Fickian error function.
3. Consistent trend: higher $c$ gives lower $\alpha_R$ (stronger nonlinear effect).

**A null result** would be:
1. $\alpha_R = 0.50 \pm 0.05$ at all concentrations (Fickian).
2. Error-function profile shapes.
3. No concentration dependence beyond what Fickian diffusion with constant $D$ predicts.

---

## 9. Next Steps

### 9.1 If the Experiment Is Feasible

1. **ED-Data-10: Simulation comparison.** Run the ED PDE with the FRAP initial condition (stripe bleach) and the fitted $\beta$, $\phi_{\max}$ from ED-Data-08. Compare the simulated recovery profile $c(x, t)$ directly to the experimental images — not just $\alpha_R$ but the full profile shape.

2. **Multi-concentration sweep.** Run the FRAP at $c = 100$, $150$, $200$, $250$, $300$ g/L. Extract $\alpha_R(c)$ at each concentration. The ED prediction: $\alpha_R$ is the same at all concentrations (because $\beta$ is a material constant, not a function of $c$). The Fickian prediction: $\alpha_R = 0.5$ at all concentrations. This is a discriminating test.

3. **Colloidal version.** If BSA-FRAP succeeds, repeat with PMMA colloids in a microfluidic channel at $\phi = 0.35$–$0.45$. The colloidal system has the strongest ED data basis ($\beta = 1.69$, confirmed to 2.3%) and provides an independent check.

### 9.2 If the Experiment Is Not Feasible

4. **Alternative: capillary diffusion.** Fill a glass capillary with a sharp interface between concentrated and dilute sucrose solution (horizontal orientation to suppress convection). Image the front position by absorption of a co-dissolved food dye. Slower ($\sim$ hours to days) but requires no specialised equipment.

5. **Alternative: colloidal sedimentation-diffusion.** Create a sharp density profile in a colloidal suspension by centrifugation, then stop the centrifuge and track the relaxation of the front by optical extinction.

### 9.3 What This Experiment Would Establish

If $\alpha_R \approx 0.25$ and compact support are observed in a purpose-built FRAP experiment at controlled protein concentration, it is the first direct, quantitative, purpose-designed experimental confirmation of an ED prediction. Combined with the three-material $D(c)$ fits ($R^2 > 0.98$ in all cases), this would establish the ED mobility law as a quantitatively accurate constitutive relationship for density-dependent transport in condensed matter.

---

## Appendix: Equipment Requirements

| Item | Specification | Availability |
|:-----|:-------------|:-------------|
| Confocal microscope | Laser scanning, 488 nm excitation, $20\times$–$40\times$ objective | Standard in biophysics labs |
| FRAP module | Bleaching laser ($\sim 10$ mW at sample), stripe geometry | Standard on most confocal systems |
| BSA-Alexa488 | Commercially available (ThermoFisher A13100) | Off-the-shelf |
| BSA (unlabelled) | $\geq 98\%$ purity, fatty-acid-free | Sigma-Aldrich A7030 |
| Sample chamber | Slide + coverslip + $20\;\mu$m spacer | Standard |
| Image analysis | Python + NumPy + SciPy | Free |
| ED simulation | ED-SIM-02 + parameters from ED-Data-08 | Available in repo |

**Estimated cost:** $< \$500$ in consumables (BSA, dye, slides). All major equipment is standard in a confocal microscopy facility.

**Estimated time:** One day of sample preparation, one day of FRAP measurements, one day of analysis. Total: 3 days for a complete dataset at one concentration; 1 week for a multi-concentration sweep.
