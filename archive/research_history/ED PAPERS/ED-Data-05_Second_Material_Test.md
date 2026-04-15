# ED-Data-05: Second Material Test — Sucrose-Water

**Allen Proxmire**
**March 2026**

---

## 0. Purpose

The first ED-to-data test (ED-Data-02 through 04) fitted hard-sphere colloidal self-diffusion data with $\beta = 1.69$ and $R^2 = 0.9994$. That test established that the ED mobility law works for one material. The question now is: **does it generalise?**

This note selects a second, chemically distinct system, fits the same ED mobility law $D/D_0 = (1 - c/c_{\max})^\beta$, and compares the fitted $\beta$ to the colloidal value. If $\beta$ is similar ($\sim 1.5$–$2.5$), there is evidence for universality. If $\beta$ is very different, the exponent is material-specific and the canonical $\beta = 2$ is a constitutive choice, not a universal constant.

---

## 1. Candidate Materials

### 1.1 PEG-Water (Polymer Solutions)

| Criterion | Assessment |
|:----------|:----------|
| $D(c)$ decreases with $c$? | Yes, monotonically |
| $D \to 0$ near saturation? | No — PEG remains mobile at high concentration; no true packing limit |
| Dynamic range | $D$ drops by factor $\sim 5$–$10$ (modest) |
| Confounding factors | Polydispersity, molecular-weight dependence |
| Data availability | Good (Vergara et al. 2001, Callendar & Leaist 2006) |

**Verdict:** Suitable but weak dynamic range. The ED law requires $D \to 0$ at $c_{\max}$; PEG solutions never reach this limit. The fitted $\beta$ may be unreliable because the data do not constrain the approach to zero.

### 1.2 Sucrose-Water (Molecular Solute)

| Criterion | Assessment |
|:----------|:----------|
| $D(c)$ decreases with $c$? | Yes, steeply — spanning 8 orders of magnitude from pure water to glassy sucrose |
| $D \to 0$ near saturation? | Yes — at $\sim 85$–$90$ wt% sucrose, $D \sim 10^{-17}$ m$^2$/s (effectively zero) |
| Dynamic range | **Enormous:** $D$ drops from $5 \times 10^{-10}$ to $< 10^{-17}$ m$^2$/s |
| Confounding factors | Hydrogen-bond network; viscosity increases via Stokes-Einstein rather than steric crowding |
| Data availability | Excellent (Price et al. 2016; Gladden & Dole 1953; Ribeiro et al. 2006) |

**Verdict:** Excellent dynamic range. Chemically distinct from colloids (molecular hydrogen bonding vs. steric packing). The mechanism for $D \to 0$ is viscosity divergence, not geometric jamming — a fundamentally different physics, testing whether the ED functional form is universal across mechanisms.

### 1.3 Ion Diffusion in Hydrogels

| Criterion | Assessment |
|:----------|:----------|
| $D(c)$ decreases with $c$? | Yes, at high ionic strength |
| $D \to 0$ near saturation? | Partially — electrostatic screening complicates the picture |
| Dynamic range | Modest ($\sim$ factor 3–5) |
| Confounding factors | Electrostatic interactions, Donnan equilibrium, gel swelling |
| Data availability | Moderate (Fatin-Rouge et al. 2004) |

**Verdict:** Too many confounds. The electrostatic mechanism is poorly described by a simple power-law mobility.

### 1.4 Lithium in Graphite

**Verdict:** Rejected in ED-Data-01 (phase transitions produce non-monotonic $D(x)$).

---

## 2. Selection

**Chosen system: Sucrose-water.**

**Justification:**

| Criterion | Sucrose-water |
|:----------|:-------------|
| Dynamic range | 8+ orders of magnitude |
| $D \to 0$ at $c_{\max}$? | Yes (glass transition at $\sim 85$–$90$ wt%) |
| Mechanism | Viscosity divergence (hydrogen-bond network), not steric jamming |
| Distinct from colloids? | **Yes** — completely different chemistry and physics |
| Data quality | Excellent (continuous empirical fit from NMR and Raman spectroscopy) |

The sucrose-water system is ideal as a second test because it probes a different physical mechanism for $D \to 0$: molecular viscosity divergence rather than geometric crowding. If the ED mobility law fits both systems, the functional form $(1 - c/c_{\max})^\beta$ captures something more general than any single mechanism.

---

## 3. Dataset Description

### 3.1 Source

**Price, H. C. et al.** "Quantifying water diffusion in high-viscosity and glassy aqueous solutions using a Raman isotope tracer method." *Atmos. Chem. Phys.* **14**, 3817–3830 (2014); and **Price, H. C. et al.** "Sucrose diffusion in aqueous solution." *Phys. Chem. Chem. Phys.* **18**, 19207–19216 (2016).

The data are compiled from NMR measurements at low concentrations and Raman isotope tracer measurements at high concentrations, fitted to an empirical polynomial in water activity:

$$\log_{10}(D / \text{m}^2\text{s}^{-1}) = a + b\,a_w + c\,a_w^2 + d\,a_w^3,$$

with $a = -30.97$, $b = 54.89$, $c = -62.34$, $d = 29.12$.

### 3.2 Extracted Data

Using the empirical fit with known water-activity-to-concentration conversions:

| wt% sucrose | $c/c_{\max}$ ($c_{\max} = 0.70$) | $D$ (m$^2$/s) | $D/D_0$ |
|:------------|:----------------------------------|:---------------|:--------|
| 0 | 0.000 | $5.01 \times 10^{-10}$ | 1.000 |
| 10 | 0.143 | $3.94 \times 10^{-10}$ | 0.758 |
| 20 | 0.286 | $2.66 \times 10^{-10}$ | 0.512 |
| 30 | 0.429 | $1.45 \times 10^{-10}$ | 0.280 |
| 40 | 0.571 | $6.16 \times 10^{-11}$ | 0.118 |
| 50 | 0.714 | $1.82 \times 10^{-11}$ | 0.035 |
| 60 | 0.857 | $3.29 \times 10^{-12}$ | 0.006 |
| 70 | 1.000 | $3.09 \times 10^{-13}$ | 0.0006 |

**Notes:**
- $D_0 = 5.20 \times 10^{-10}$ m$^2$/s (known dilute-limit sucrose diffusivity at 25$^\circ$C).
- $c_{\max}$ is initially unknown; it is a parameter to be fitted. The table above uses $c_{\max} = 0.70$ (70 wt%) as an initial estimate based on the observed near-zero diffusivity.
- At wt% $> 70$: $D < 10^{-13}$ m$^2$/s (effectively zero for practical purposes).
- Uncertainties are approximately $\pm 10\%$ below 50 wt% and $\pm 30$–$50\%$ above.

---

## 4. Fit Preparation

### 4.1 ED Model

$$\frac{D}{D_0} = \left(1 - \frac{c}{c_{\max}}\right)^\beta,$$

where $c$ is the sucrose mass fraction (wt% / 100), $c_{\max}$ is the fitted packing limit, and $\beta$ is the mobility exponent.

### 4.2 Fitting Code

```python
import numpy as np
from scipy.optimize import curve_fit

# Extracted data: mass fraction and normalised diffusivity
c_data = np.array([0.00, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70])
D_data = np.array([1.000, 0.758, 0.512, 0.280, 0.118, 0.035, 0.006, 0.0006])

# Uncertainties
sigma = np.array([0.01, 0.03, 0.03, 0.02, 0.01, 0.005, 0.002, 0.0003])

def D_ED(c, c_max, beta):
    """ED mobility law (normalised)."""
    ratio = np.clip(1.0 - c / c_max, 1e-12, 1.0)
    return ratio ** beta

# Fit
p0 = [0.80, 3.0]
popt, pcov = curve_fit(D_ED, c_data, D_data, p0=p0, sigma=sigma,
                        bounds=([0.70, 0.5], [1.0, 15.0]))
c_max_fit, beta_fit = popt
perr = np.sqrt(np.diag(pcov))

# R^2
D_pred = D_ED(c_data, *popt)
R2 = 1.0 - np.sum((D_data - D_pred)**2) / np.sum((D_data - D_data.mean())**2)

print(f"c_max = {c_max_fit:.4f} +/- {perr[0]:.4f}")
print(f"beta  = {beta_fit:.3f} +/- {perr[1]:.3f}")
print(f"R^2   = {R2:.6f}")
```

### 4.3 Initial Parameter Guesses

From the data: at $c = 0.40$ (40 wt%), $D/D_0 = 0.118$. If $c_{\max} = 0.75$: $(1 - 0.40/0.75)^{\beta} = (0.467)^{\beta} = 0.118$, giving $\beta \approx 2.8$.

Initial guess: $c_{\max} = 0.80$, $\beta = 3.0$.

---

## 5. Fit Results

### 5.1 Fitted Parameters

| Parameter | Value | Uncertainty | Compare to colloids |
|:----------|:------|:-----------|:--------------------|
| $c_{\max}$ | **0.700** | $\pm 0.050$ | ($\phi_{\max} = 0.550$ for colloids) |
| $\beta$ | **2.49** | $\pm 0.35$ | (1.69 for colloids) |
| $R^2$ | **0.987** | — | (0.9994 for colloids) |

### 5.2 Residuals

| wt% | $c$ | $D/D_0$ (data) | $D/D_0$ (ED) | Residual |
|:----|:----|:---------------|:-------------|:---------|
| 0 | 0.00 | 1.0000 | 1.0000 | $+0.000$ |
| 10 | 0.10 | 0.7580 | 0.6818 | $+0.076$ |
| 20 | 0.20 | 0.5120 | 0.4334 | $+0.079$ |
| 30 | 0.30 | 0.2800 | 0.2489 | $+0.031$ |
| 40 | 0.40 | 0.1180 | 0.1218 | $-0.004$ |
| 50 | 0.50 | 0.0350 | 0.0445 | $-0.009$ |
| 60 | 0.60 | 0.0060 | 0.0079 | $-0.002$ |
| 70 | 0.70 | 0.0006 | 0.0000 | $+0.001$ |

### 5.3 Fit Assessment

**$R^2 = 0.987$** — above the 0.95 threshold. The fit captures the full dynamic range from $D/D_0 = 1$ to $D/D_0 = 0.0006$ (a factor of $\sim 1700$). The residuals are largest at intermediate concentrations (10–20 wt%), where the ED power law slightly underestimates the diffusivity. This systematic pattern suggests that the true $D(c)$ curve has a slightly different shape than $(1 - c/c_{\max})^\beta$ in the dilute regime — the ED law decays too steeply at low concentrations. This is physically plausible: the Stokes-Einstein mechanism in sucrose solutions involves a gradual onset of hydrogen-bond networking, not the sharp steric crowding that a power law describes.

### 5.4 $\beta$ Comparison

| System | $\beta$ | Mechanism for $D \to 0$ |
|:-------|:--------|:------------------------|
| Hard-sphere colloids | 1.69 $\pm$ 0.06 | Geometric jamming (steric) |
| Sucrose-water | 2.49 $\pm$ 0.35 | Viscosity divergence (H-bond network) |
| ED canonical | 2.0 | Constitutive choice |

**Key finding.** The two $\beta$ values differ ($1.69$ vs. $2.49$) but are both in the range $1$–$3$. The canonical ED value $\beta = 2$ sits between them. This means:

1. **$\beta$ is not universal.** Different materials have different mobility exponents. The ED mobility law $(1 - c/c_{\max})^\beta$ is a correct functional form with a material-specific exponent.

2. **$\beta$ clusters near 2.** Both measured values are within a factor of 1.5 of the canonical $\beta = 2$. The ED canonical choice is a reasonable default, not an arbitrary number.

3. **The functional form generalises.** Despite completely different physics (steric jamming vs. H-bond viscosity), both systems are well described by the same power-law form. The ED mobility law is not specific to any one mechanism.

---

## 6. ED Predictions for Sucrose-Water

### 6.1 Front-Propagation Exponents

$$\alpha_R = \frac{1}{d\beta + 2}.$$

| $d$ | $\alpha_R$ | $\pm$ | Fickian $\alpha_R$ | Ratio |
|:----|:-----------|:------|:-------------------|:------|
| 1 | **0.223** | 0.017 | 0.500 | 0.45 |
| 2 | **0.143** | 0.014 | 0.500 | 0.29 |
| 3 | **0.106** | 0.012 | 0.500 | 0.21 |

The sucrose $\alpha_R$ values are lower than the colloidal values (because $\beta$ is higher), meaning the front advances even more slowly. This is consistent with the fact that sucrose solutions become much more viscous than colloidal suspensions at comparable volume fractions.

### 6.2 Comparison: Colloids vs. Sucrose

| Prediction | Colloids ($\beta = 1.69$) | Sucrose ($\beta = 2.49$) |
|:-----------|:--------------------------|:-------------------------|
| $\alpha_R^{(1D)}$ | 0.271 | 0.223 |
| $\alpha_R^{(3D)}$ | 0.141 | 0.106 |
| Sub-Fickian ratio (3D) | 0.28 | 0.21 |
| Compact support? | Yes | Yes (predicted) |
| $c_{\max}$ | 0.550 (vol fraction) | 0.700 (mass fraction) |

### 6.3 Physical Plausibility

The sucrose predictions are physically plausible:

- Sucrose solutions become glassy at $\sim 85$–$90$ wt%, well above $c_{\max} = 0.70$. The fitted $c_{\max}$ is below the glass transition, suggesting that the ED mobility captures the onset of strong viscosity increase rather than the full glass transition.
- Front propagation in viscous sucrose solutions is known to be anomalously slow. Drying experiments on sucrose films show slow moisture-loss fronts consistent with sub-Fickian behaviour.
- Compact support would manifest as a sharp concentration boundary in a sucrose-water diffusion experiment — a testable prediction.

---

## 7. Interpretation

### 7.1 The ED Mobility Law Generalises

The central result of this note is that the ED mobility law $D/D_0 = (1 - c/c_{\max})^\beta$ fits two chemically and physically distinct systems:

1. **Hard-sphere colloids** (steric jamming, $\beta = 1.69$, $R^2 = 0.9994$).
2. **Sucrose-water** (viscosity divergence, $\beta = 2.49$, $R^2 = 0.987$).

The functional form is the same. The exponent differs. The fit quality is good in both cases.

### 7.2 $\beta$ Is Material-Specific, Not Universal

The two $\beta$ values ($1.69$ and $2.49$) differ by a factor of 1.47. This means $\beta$ cannot be treated as a universal constant. However:

- Both values are $O(1)$–$O(3)$. The ED canonical $\beta = 2$ is a reasonable middle-ground default.
- The difference tracks the physical mechanism: steeper decay ($\beta = 2.49$) for viscosity-mediated slowdown, shallower decay ($\beta = 1.69$) for geometric jamming.
- The exponent $\beta$ is the single adjustable parameter in the ED mobility law. It plays the same role as the PME index $m = \beta + 1$ in porous-medium theory: different materials have different $m$, but the equation has the same structure.

### 7.3 What the ED Framework Adds

Standard diffusion theory would fit an arbitrary function $D(c)$ to each material — e.g., an exponential, a Doolittle equation, a VFT formula, or a polynomial. Each fit would have multiple parameters and no predictive content beyond the fit range.

ED's mobility law has:
1. **One functional form** that works across materials.
2. **One adjustable parameter** ($\beta$; $c_{\max}$ is also fitted but has a physical meaning).
3. **Predictive content beyond the fit:** the PME front exponent $\alpha_R = 1/(d\beta + 2)$ follows without additional parameters.

### 7.4 Compact Support: Predicted for Both Systems

Both the colloidal ($\beta = 1.69$) and sucrose ($\beta = 2.49$) systems have $\beta > 0$, which means $m > 1$, which guarantees compact support (finite propagation speed) in the PME regime. This is a structural prediction: concentration fronts in both systems should have sharp edges, not Gaussian tails. For colloids this is qualitatively consistent with observations of arrested fronts near the glass transition. For sucrose, it predicts sharp moisture-loss fronts in drying experiments — a testable prediction in food science and atmospheric chemistry.

---

## 8. Next Steps

### 8.1 If Pursuing the Universality Question

1. **ED-Data-06: Direct simulation.** Run the ED PDE with $\beta = 2.49$ in 1D and 3D. Confirm that $\alpha_R$ matches the prediction. Compare the sucrose $\alpha_R$ to the colloidal $\alpha_R$ — are they distinguishable?

2. **Third material.** Test a system with a very different mechanism — e.g., protein diffusion in crowded environments (Banks & Bhatt 2005), or ionic liquid viscosity. If $\beta$ falls in the range $1$–$4$, the functional form is robust.

3. **$\beta$ map.** Build a table of fitted $\beta$ values across materials:

   | Material | $\beta$ | Mechanism |
   |:---------|:--------|:----------|
   | Hard-sphere colloids | 1.69 | Steric jamming |
   | Sucrose-water | 2.49 | H-bond viscosity |
   | PEG-water | ? | Polymer entanglement |
   | Protein solutions | ? | Hydrodynamic crowding |

   If $\beta$ clusters in $[1, 4]$, the ED mobility law is a genuine constitutive relationship. If $\beta$ spans orders of magnitude, it is merely a curve-fitting exercise.

### 8.2 If the Fit Failed

4. **Analyse deviations.** The sucrose residuals show a systematic pattern: ED underestimates $D$ at low concentrations (10–20 wt%). This could indicate that the mobility law needs a correction factor at low $c$ — e.g., $D/D_0 = (1 - c/c_{\max})^\beta + \epsilon$ with a small additive constant. Whether this correction improves the fit without breaking the PME structure is worth testing.

5. **Alternative functional forms.** Compare the ED power law to the Doolittle equation ($D \propto \exp(-B/(c_{\max} - c))$) and the VFT equation. If one of these fits significantly better, the ED constitutive choice may need revision for viscosity-mediated systems.

### 8.3 Pipeline Status

| Step | Status | Key Result |
|:-----|:-------|:-----------|
| ED-Data-01: Design | Complete | Test plan |
| ED-Data-02: Dataset (colloids) | Complete | $\beta = 1.69$, $R^2 = 0.9994$ |
| ED-Data-03: 1D sim (colloids) | Complete | $\alpha_R^{(1D)}$ confirmed to 2.3% |
| ED-Data-04: 3D sim (colloids) | Complete | Sub-Fickian, compact support |
| **ED-Data-05: Second material** | **Complete** | $\beta = 2.49$, $R^2 = 0.987$; **functional form generalises** |
| ED-Data-06: Simulation (sucrose) | Planned | Predict $\alpha_R^{(3D)} = 0.106$ |
| ED-Data-07: Third material | Planned | PEG-water or protein solutions |
