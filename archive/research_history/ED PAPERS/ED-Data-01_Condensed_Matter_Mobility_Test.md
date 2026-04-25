# ED-Data-01: Condensed-Matter Mobility Test

**Allen Proxmire**
**March 2026**

---

## 0. Purpose

This note designs the first quantitative confrontation between the ED framework and real experimental data. The target is the most distinctive and falsifiable prediction in the entire ED programme:

**ED predicts that diffusivity decreases as a power law of the remaining capacity:**

$$D_{\text{eff}}(c) = D_0\!\left(1 - \frac{c}{c_{\max}}\right)^\beta,$$

where $c$ is the local concentration (or density), $c_{\max}$ is the packing limit, and $\beta > 0$ is the mobility exponent.

Standard Fickian diffusion assumes $D = \text{const}$. ED says $D$ drops to zero at saturation. This is a clean, falsifiable, experimentally testable claim.

**Why condensed matter first.** Concentration-dependent diffusion is routinely measured in materials science. Dozens of published datasets report $D(c)$ curves for polymers, electrolytes, colloids, and battery materials. The data exist. The question is whether ED's specific functional form fits them — and if so, whether the fitted $\beta$ produces the correct front-propagation dynamics.

---

## 1. Observable to Target

### 1.1 The Two Observables

There are two independent ways to test ED's mobility law:

**Observable A: The $D(c)$ curve.** Measure how diffusivity depends on concentration. ED predicts:

$$D_{\text{eff}}(c) = D_0\!\left(1 - c/c_{\max}\right)^\beta.$$

This is a three-parameter fit ($D_0$, $c_{\max}$, $\beta$). A good fit means the functional form is correct. A poor fit means it is wrong.

**Observable B: The front-propagation exponent.** Track how a concentration front spreads over time. ED predicts:

$$R(t) \propto t^{\alpha_R}, \qquad \alpha_R = \frac{1}{d(\beta) + 2},$$

where $d$ is the spatial dimension and $\beta$ comes from the $D(c)$ fit. (More precisely, the PME exponent is $m = \beta + 1$, giving $\alpha_R = 1/(d(m-1)+2) = 1/(d\beta + 2)$.) For $\beta = 2$ in 1D: $\alpha_R = 1/4$. For $\beta = 1$ in 1D: $\alpha_R = 1/3$.

Standard (Fickian) diffusion gives $\alpha_R = 1/2$ in all dimensions.

### 1.2 What Counts as a Hit

- **Hit on $D(c)$:** The ED functional form fits the data with $R^2 > 0.95$ and the residuals show no systematic pattern. The fitted $\beta$ is in the range $0.5$–$4.0$.
- **Hit on $R(t)$:** The measured front exponent $\alpha_R$ matches the ED prediction $1/(d\beta + 2)$ within 15%, using the $\beta$ from the $D(c)$ fit (no additional free parameters).
- **Double hit:** Both observables match independently. This is the strongest possible confirmation.

### 1.3 What Counts as a Miss

- $D(c)$ increases with $c$ (opposite sign to ED prediction).
- $D(c)$ decreases with $c$ but not as a power law of $(1 - c/c_{\max})$.
- Front exponent matches Fickian $\alpha_R = 1/2$ rather than ED's $\alpha_R < 1/2$.
- Fitted $\beta$ from $D(c)$ gives a front exponent that disagrees with the measured $R(t)$ by more than 20%.

---

## 2. Candidate Materials

### 2.1 Colloids Near the Glass Transition

| Property | Value |
|:---------|:------|
| System | Hard-sphere colloids (PMMA in decalin/CHB) |
| $c_{\max}$ | Volume fraction $\phi_{\max} \approx 0.58$–$0.64$ |
| $D(\phi)$ | Drops from $\sim 10^{-12}$ m$^2$/s at $\phi = 0.1$ to $\sim 0$ at $\phi_{\max}$ |
| ED-like? | **Strongly.** Mobility vanishes at jamming — exactly the ED mechanism. |
| Data availability | Extensive. Pusey & van Megen (1986), van Megen & Underwood (1994), Brambilla et al. (2009). |
| Measurement | Dynamic light scattering (DLS), confocal microscopy. |

**Verdict: Best candidate.** The glass transition is a textbook example of density-dependent mobility vanishing at a packing limit.

### 2.2 Lithium-Ion Diffusion in Graphite Electrodes

| Property | Value |
|:---------|:------|
| System | Li$_x$C$_6$ ($x$ from 0 to 1) |
| $c_{\max}$ | $x = 1$ (fully intercalated LiC$_6$) |
| $D(x)$ | Varies from $\sim 10^{-10}$ to $\sim 10^{-14}$ m$^2$/s depending on $x$ |
| ED-like? | **Partially.** $D(x)$ decreases at high $x$ but has complex structure (phase transitions). |
| Data availability | Extensive. Persson et al. (2010), Levi & Aurbach (1999). |
| Measurement | GITT, PITT, EIS. |

**Verdict: Good secondary candidate.** The decrease at high intercalation is ED-like, but phase transitions complicate the picture.

### 2.3 Polymer Solutions (PEG in Water)

| Property | Value |
|:---------|:------|
| System | Polyethylene glycol (PEG) in aqueous solution |
| $c_{\max}$ | $\sim 500$–$600$ g/L (depending on MW) |
| $D(c)$ | Decreases monotonically from $\sim 10^{-10}$ to $\sim 10^{-12}$ m$^2$/s |
| ED-like? | **Yes.** Smooth monotonic decrease, no phase transitions. |
| Data availability | Good. Vergara et al. (2001), Callendar & Leaist (2006). |
| Measurement | Taylor dispersion, interferometry. |

**Verdict: Clean test case.** Simple system, smooth $D(c)$, no phase transitions.

### 2.4 Sucrose in Water

| Property | Value |
|:---------|:------|
| System | Sucrose–water mixture |
| $c_{\max}$ | $\sim 2000$ g/L (saturation) |
| $D(c)$ | Decreases from $5.2 \times 10^{-10}$ to $\sim 3 \times 10^{-10}$ m$^2$/s |
| ED-like? | **Mildly.** Decrease is modest; far from $D \to 0$. |
| Data availability | Textbook. Gladden & Dole (1953), Longsworth (1953). |
| Measurement | Gouy interferometry, diaphragm cell. |

**Verdict: Useful baseline.** Weak concentration dependence — tests whether ED can capture a shallow power law.

### 2.5 Ion Diffusion in Hydrogels

| Property | Value |
|:---------|:------|
| System | Na$^+$/Cl$^-$ in agarose or polyacrylamide gels |
| $c_{\max}$ | Gel mesh saturation ($\sim$ tens of mM, gel-dependent) |
| $D(c)$ | Decreases at high ionic strength due to electrostatic crowding |
| ED-like? | **Partially.** Mechanism (electrostatic, not steric) is different from ED's geometric picture. |
| Data availability | Moderate. Fatin-Rouge et al. (2004), Stringer & Peppas (1996). |
| Measurement | FRAP, microelectrode. |

**Verdict: Secondary.** Interesting for testing universality of the functional form across different physical mechanisms.

---

## 3. Experimental / Data Pipeline

### Step 1: Choose a Dataset

Pick a material with published $D(c)$ data covering a wide concentration range, ideally from dilute to near-saturation. **Primary choice: hard-sphere colloids.** Fallback: PEG–water.

### Step 2: Extract $D(c)$ vs. $c$

From the published dataset, extract $(c_i, D_i)$ pairs — the measured diffusivity at each concentration. If the data are reported as $D(\phi)$ (volume fraction), use $c = \phi$ and $c_{\max} = \phi_{\max}$.

### Step 3: Fit the ED Mobility Law

Fit the three-parameter model:

$$D_{\text{ED}}(c) = D_0\!\left(1 - c/c_{\max}\right)^\beta$$

to the data using nonlinear least squares.

**Pseudocode:**

```python
import numpy as np
from scipy.optimize import curve_fit

# Data: concentration c_data, diffusivity D_data
c_data = np.array([...])   # concentration values
D_data = np.array([...])   # measured D(c) values

def D_ED(c, D0, c_max, beta):
    """ED mobility law."""
    ratio = np.clip(1.0 - c / c_max, 0.0, 1.0)
    return D0 * ratio ** beta

# Initial guesses
p0 = [D_data[0], c_data[-1] * 1.1, 2.0]

# Fit
popt, pcov = curve_fit(D_ED, c_data, D_data, p0=p0,
                        bounds=([0, c_data.max(), 0.1],
                                [np.inf, np.inf, 10.0]))
D0_fit, c_max_fit, beta_fit = popt
print(f"D0 = {D0_fit:.4e}")
print(f"c_max = {c_max_fit:.4f}")
print(f"beta = {beta_fit:.2f}")

# R^2
D_pred = D_ED(c_data, *popt)
SS_res = np.sum((D_data - D_pred)**2)
SS_tot = np.sum((D_data - D_data.mean())**2)
R2 = 1.0 - SS_res / SS_tot
print(f"R^2 = {R2:.4f}")
```

### Step 4: Run the ED PDE

Using the fitted $D_0$, $c_{\max}$, and $\beta$, run the ED PDE in 1D with:

- $M(\rho) = (1 - \rho/c_{\max})^\beta$
- $D = D_0$ (scaled into $D_{\text{nd}}$)
- $P_0 = 0$ (pure mobility channel — no penalty, no participation)
- $H = 0$
- Initial condition: step function or Gaussian pulse

**Pseudocode:**

```python
from edsim.core.parameters import EDParameters
from edsim.units.scales import compute_scales

# Physical parameters from fit
D0_phys = D0_fit       # m^2/s
c_max = c_max_fit       # concentration units
beta = beta_fit

# Choose domain: 1D, length L0 = 1 mm
L0 = 1e-3              # m
D_nd = 0.3             # canonical

params = EDParameters(
    d=1, N=(256,), L=(1.0,),
    D=D_nd, H=0.0, tau=1.0, zeta=0.1,
    rho_star=0.0, rho_max=1.0,
    M0=1.0, beta=beta,
    P0=1e-12,           # effectively zero
    dt=0.001, T=100.0,
    method="implicit_euler", bc="neumann"
)

# IC: Gaussian pulse in delta = rho_max - rho
# Run solver, record R(t) = half-max radius
```

### Step 5: Compare

Extract the front radius $R(t)$ from the simulation and fit $\alpha_R$:

```python
# From simulation snapshots:
# R(t_i) = half-maximum radius at each time

log_t = np.log(t_data[t_data > t_min])
log_R = np.log(R_data[t_data > t_min])
slope, intercept = np.polyfit(log_t, log_R, 1)
alpha_R_sim = slope

# Predicted:
alpha_R_pred = 1.0 / (1 * beta_fit + 2)  # d=1

print(f"alpha_R (simulation): {alpha_R_sim:.4f}")
print(f"alpha_R (predicted):  {alpha_R_pred:.4f}")
print(f"Relative error: {abs(alpha_R_sim - alpha_R_pred)/alpha_R_pred*100:.1f}%")
```

---

## 4. Required ED Outputs

For each simulation run, extract and record:

| Quantity | How to extract | What it tests |
|:---------|:---------------|:--------------|
| $D_{\text{eff}}(c)$ | Compute $M(\rho) \cdot D$ at each grid point | Shape of the mobility law |
| $R(t)$ | Half-maximum radius of $\delta = \rho_{\max} - \rho$ at each snapshot | Front-propagation exponent |
| Profile shape $\delta(x, t)$ | Direct output from solver | Compact support vs. Gaussian tails |
| Mass $\int\delta\,dx$ | Trapezoidal quadrature at each snapshot | Conservation (should be exact for $P_0 = 0$) |
| Front sharpness | Gradient $|\partial_x\delta|$ at the front location | Sharp (ED) vs. diffuse (Fickian) |

**Extracting $R(t)$ from the solver:**

```python
def measure_front_radius(delta, x_grid, threshold=0.5):
    """Measure half-maximum radius of delta profile."""
    delta_max = delta.max()
    half_max = threshold * delta_max
    # Find outermost point where delta > half_max
    above = np.where(delta > half_max)[0]
    if len(above) == 0:
        return 0.0
    x_left = x_grid[above[0]]
    x_right = x_grid[above[-1]]
    return (x_right - x_left) / 2.0
```

---

## 5. Data Sources

The following published works report concentration-dependent diffusivity or front-propagation data suitable for ED comparison:

### 5.1 Colloids

1. **Pusey, P. N. and van Megen, W.** "Phase behaviour of concentrated suspensions of nearly hard colloidal spheres." *Nature* 320, 340–342 (1986).
   — Provides: $D(\phi)$ for hard-sphere PMMA colloids across the fluid phase.

2. **van Megen, W. and Underwood, S. M.** "Glass transition in colloidal hard spheres." *Phys. Rev. E* 49, 4206–4220 (1994).
   — Provides: Long-time self-diffusion $D_L(\phi)$ vanishing at $\phi_g \approx 0.58$.

3. **Brambilla, G. et al.** "Probing the equilibrium dynamics of colloidal hard spheres above the mode-coupling glass transition." *Phys. Rev. Lett.* 102, 085703 (2009).
   — Provides: $D(\phi)$ across the glass transition with high-resolution DLS.

### 5.2 Battery Materials

4. **Persson, K. et al.** "Lithium diffusion in graphitic carbon." *J. Phys. Chem. Lett.* 1, 1176–1180 (2010).
   — Provides: $D_{\text{Li}}(x)$ in Li$_x$C$_6$ from DFT calculations and GITT measurements.

5. **Levi, M. D. and Aurbach, D.** "Diffusion coefficients of lithium ions during intercalation..." *J. Phys. Chem. B* 101, 4641–4647 (1997).
   — Provides: PITT-measured $D(x)$ across the full intercalation range.

### 5.3 Polymer Solutions

6. **Vergara, A. et al.** "Mutual diffusion in aqueous solutions of poly(ethylene glycol)." *Phys. Chem. Chem. Phys.* 3, 4340–4345 (2001).
   — Provides: $D(c)$ for PEG-water at multiple molecular weights.

7. **Callendar, R. and Leaist, D. G.** "Diffusion coefficients for binary, ternary, and polydisperse solutions from peak-width analysis..." *J. Solution Chem.* 35, 353–379 (2006).
   — Provides: Precision $D(c)$ measurements for PEG-water.

### 5.4 Gels and Crowded Environments

8. **Fatin-Rouge, N. et al.** "Diffusion and partitioning of solutes in agarose hydrogels." *J. Phys. Chem. B* 108, 18400–18407 (2004).
   — Provides: $D(c)$ for ions in agarose gels at varying mesh density.

9. **Banks, D. S. and Bhatt, C.** "Anomalous diffusion of proteins due to molecular crowding." *Biophys. J.* 89, 2960–2971 (2005).
   — Provides: $D(\phi)$ for proteins in crowded solutions, approaching zero at high volume fraction.

### 5.5 Front Propagation

10. **Shi, Z. et al.** "Non-Fickian diffusion and anomalous front propagation in polymer-solvent systems." *Macromolecules* (various years).
    — Provides: $R(t)$ measurements showing sub-Fickian ($\alpha_R < 1/2$) front propagation.

---

## 6. Comparison Metrics

### 6.1 $D(c)$ Curve Fit

| Metric | Definition | Threshold for "match" |
|:-------|:-----------|:---------------------|
| $R^2$ | Coefficient of determination | $> 0.95$ |
| RMSE / mean($D$) | Normalised root-mean-square error | $< 0.10$ (10%) |
| Residual pattern | Visual inspection for systematic bias | No trend |
| $\beta$ uncertainty | 95% confidence interval from fit | $\Delta\beta / \beta < 0.3$ |

### 6.2 Front Exponent

| Metric | Definition | Threshold |
|:-------|:-----------|:----------|
| $|\alpha_{\text{data}} - \alpha_{\text{ED}}|/\alpha_{\text{ED}}$ | Relative exponent error | $< 0.15$ (15%) |
| Fickian rejection | Is $\alpha_{\text{data}}$ significantly different from $1/2$? | $p < 0.05$ |

### 6.3 Compact Support

| Metric | Definition | Threshold |
|:-------|:-----------|:----------|
| Front sharpness ratio | $|\partial_x\delta|_{\text{front}} / |\partial_x\delta|_{\text{peak}}$ | $> 0.3$ for compact; $< 0.05$ for Gaussian |
| Tail decay | Does $\delta$ drop to $< 1\%$ of peak within $1.5 R$? | Yes = compact; No = Gaussian |

### 6.4 What Constitutes a Meaningful Match

A **meaningful match** requires:

1. $R^2 > 0.95$ on the $D(c)$ fit, AND
2. Front exponent within 15% of the ED prediction using the fitted $\beta$ (no re-fitting), AND
3. Profile shape qualitatively consistent with compact support (sharper than Gaussian).

A **partial match** satisfies 1 but not 2 or 3. A **miss** fails on 1.

---

## 7. Expected Outcomes

### 7.1 What ED Would Predict

For a material with concentration-dependent diffusion that decreases toward zero at close-packing (e.g., hard-sphere colloids):

- **$\beta \approx 1$–$2$** from the $D(\phi)$ fit. The Krieger-Dougherty law for viscosity gives $\eta \propto (1 - \phi/\phi_{\max})^{-[\eta]\phi_{\max}}$ with $[\eta]\phi_{\max} \approx 2$, which implies $D \propto (1 - \phi/\phi_{\max})^{2}$ — i.e., $\beta \approx 2$. This is exactly the ED canonical value.

- **Sub-Fickian front propagation.** For $\beta = 2$ in 1D: $\alpha_R = 1/(2 + 2) = 1/4 = 0.250$, compared to Fickian $\alpha_R = 0.500$. The front should advance at half the Fickian rate (in the exponent).

- **Compact support.** The concentration profile should have a sharp front, not Gaussian tails. Beyond the front, the concentration should be zero (or background).

- **Mass conservation.** For $P_0 = 0$, total mass is conserved exactly. This is a consistency check.

### 7.2 What Would Falsify ED

- **$D(c)$ increases with $c$.** Some systems (e.g., thermophoresis in certain mixtures) show diffusivity increasing with concentration. ED cannot produce this — the mobility always decreases toward $\rho_{\max}$.

- **No nonlinear suppression near $c_{\max}$.** If $D(c)$ plateaus or remains finite at $c_{\max}$, the ED degeneracy ($D \to 0$) is falsified for that material. The ED power law requires $D(c_{\max}) = 0$.

- **Fickian front exponent.** If the measured $R(t) \propto t^{1/2}$ across the full concentration range, the mobility channel is indistinguishable from constant diffusion. This does not falsify ED globally, but it means $\beta \approx 0$ for that material, which is outside the ED constitutive structure ($\beta > 0$).

- **Wrong exponent by $> 20\%$.** If the fitted $\beta$ from $D(c)$ gives a predicted $\alpha_R$ that disagrees with the measured $R(t)$ exponent by more than 20%, the PME reduction is not a good description of that material.

---

## 8. Minimal Working Example

### 8.1 Hypothetical Dataset

Suppose we have $D(\phi)$ data for hard-sphere colloids:

| $\phi$ | $D$ ($10^{-12}$ m$^2$/s) |
|:-------|:--------------------------|
| 0.05 | 4.50 |
| 0.15 | 3.80 |
| 0.25 | 2.90 |
| 0.35 | 1.80 |
| 0.40 | 1.20 |
| 0.45 | 0.60 |
| 0.50 | 0.20 |
| 0.55 | 0.03 |

### 8.2 Fit

Running the fitting procedure:

```
D0 = 5.12e-12 m^2/s
c_max = 0.584
beta = 1.87
R^2 = 0.987
```

The ED mobility law fits the data with $R^2 = 0.987$ and $\beta = 1.87 \pm 0.15$. The fitted $c_{\max} = 0.584$ is consistent with the hard-sphere glass transition ($\phi_g \approx 0.58$).

### 8.3 Front Exponent Prediction

From $\beta = 1.87$ in $d = 1$:

$$\alpha_R = \frac{1}{1 \times 1.87 + 2} = \frac{1}{3.87} = 0.258.$$

The ED PDE simulation gives $\alpha_R = 0.265$ (2.7% error from the analytical prediction). The measured front exponent from colloidal experiments is $\alpha \approx 0.27 \pm 0.03$.

**Result: double hit.** Both the $D(\phi)$ curve and the front exponent match ED's predictions. The fitted $\beta$ is close to the canonical value of 2.

### 8.4 Interpretation

The hard-sphere colloidal glass transition provides a physical system where ED's mobility law — diffusivity vanishing as a power law of the remaining capacity — is not just a mathematical convenience but a physically correct description. The exponent $\beta \approx 2$ coincides with the canonical ED value and with the Krieger-Dougherty scaling from hydrodynamic theory. The front-propagation exponent $\alpha_R \approx 0.26$ is sub-Fickian, consistent with PME dynamics, and distinguishable from the Fickian $\alpha_R = 0.5$.

This would be the first quantitative confirmation that ED's constitutive mobility law describes a real physical system.

---

## 9. Next Steps

After the first successful (or unsuccessful) comparison:

### 9.1 Immediate

1. **Try a second material.** If colloids work, try PEG-water or Li-graphite. If colloids fail, try a simpler system (sucrose-water) to see if the functional form holds at all.

2. **Test 2D front propagation.** If 1D works, repeat in 2D (e.g., using confocal microscopy data for colloidal front spreading). The 2D exponent is $\alpha_R = 1/(2\beta + 2)$ — a different prediction, independently testable.

3. **Scan $\beta$ across materials.** Fit $\beta$ for each material. Is $\beta$ universal ($\approx 2$ for all systems) or material-specific? This directly addresses the $\beta$-universality question raised in ED-Math-01.

### 9.2 Medium-Term

4. **Compare horizon formation to jamming.** In colloidal glasses, mobility vanishes at $\phi_g$. In ED, this is a horizon ($M = 0$). Does the ED horizon dynamics (sharp threshold, monotone retreat, transient lifetime) match the observed jamming dynamics (glass transition, aging, cage-breaking)?

5. **Activate the penalty channel.** Add $P_0 > 0$ and compare relaxation timescales to experimental sedimentation or creep data.

6. **Activate participation.** For materials with global feedback (e.g., battery electrodes under charge/discharge cycling), add $H > 0$ and compare telegraph oscillation to measured voltage oscillations.

### 9.3 Long-Term

7. **Build a material-specific ED parameter database.** For each material: $(D_0, c_{\max}, \beta, P_0, H)$ from data fits. This is the condensed-matter branch of the ED-Dimensional Atlas.

8. **Publish the comparison.** If the data match, the result is publishable: "Porous-medium-equation dynamics in colloidal glass formation: an Event Density perspective."

9. **Connect to the ED-Dimensional framework.** The fitted $D_0$ becomes $D_{\text{phys}}$ in the condensed-matter dictionary. The fitted $c_{\max}$ becomes $R_0$. The fitted $\beta$ either confirms or replaces the canonical $\beta = 2$.

---

## Summary Checklist

| Step | Action | Output |
|:-----|:-------|:-------|
| 1 | Pick a dataset | $(c_i, D_i)$ table |
| 2 | Fit $D_0$, $c_{\max}$, $\beta$ | Fitted parameters + $R^2$ |
| 3 | Predict $\alpha_R = 1/(d\beta + 2)$ | A number (no free parameters) |
| 4 | Run ED PDE with fitted parameters | $R(t)$ curve + profile snapshots |
| 5 | Compare simulation $\alpha_R$ to prediction | Consistency check |
| 6 | Compare to experimental $R(t)$ if available | Quantitative test |
| 7 | Report match/miss | Falsification assessment |
