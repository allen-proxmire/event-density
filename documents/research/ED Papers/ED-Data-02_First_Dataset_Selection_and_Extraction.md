# ED-Data-02: First Dataset Selection and Extraction

**Allen Proxmire**
**March 2026**

---

## 0. Purpose

This note selects the single best condensed-matter dataset for the first ED-to-data confrontation designed in ED-Data-01. The objective is to choose a dataset that:

1. Reports the concentration-dependent diffusivity $D(c)$ or the normalised self-diffusion coefficient $D/D_0$ as a function of volume fraction (or concentration) over a wide range.
2. Covers concentrations from dilute to near-saturation, so that the ED mobility law $D \propto (1 - c/c_{\max})^\beta$ can be tested across the full dynamic range including the regime where $D \to 0$.
3. Has minimal confounding factors: no phase transitions in the measurement range, no chemical reactions, no strong electrostatic or hydrodynamic coupling that would dominate over the steric/geometric mechanism ED describes.
4. Uses a system where the saturation limit $c_{\max}$ is physically well-defined (e.g., a packing limit, not a vague solubility bound).
5. Is well-established, widely cited, and publicly documented enough to reconstruct the data from published figures and tables.

---

## 1. Candidate Review

### 1.1 Hard-Sphere Colloids (PMMA in organic solvents)

**Pros:**
- The defining example of density-dependent mobility vanishing at a packing limit.
- The glass transition at $\phi_g \approx 0.58$ is the physical analogue of an ED horizon ($M \to 0$).
- Extensive published data from Pusey, van Megen, Segre, and collaborators spanning three decades.
- The system is well-characterised: nearly hard-sphere interactions, minimal polydispersity ($\sim 5\%$), no long-range forces.
- Both short-time and long-time self-diffusion coefficients have been measured.
- $\phi_{\max}$ is well-defined: random close packing at $\phi_{\text{rcp}} \approx 0.64$ or the glass transition at $\phi_g \approx 0.58$.

**Cons:**
- The distinction between short-time and long-time diffusion introduces a choice: which $D(\phi)$ curve should ED match? (Long-time is more appropriate for the mobility channel, which describes large-scale transport.)
- Hydrodynamic interactions (solvent-mediated) contribute to $D(\phi)$ at all volume fractions, not just near $\phi_{\max}$. ED's geometric mechanism (mobility depending only on density) neglects this.
- Data are published in figures, not always in tables. Some digitisation is needed.

### 1.2 Lithium Diffusion in Graphite Electrodes

**Pros:**
- Directly relevant to applications (battery technology).
- $D(x)$ has been measured over the full intercalation range $x \in [0, 1]$.
- The decrease at high $x$ is qualitatively ED-like.

**Cons:**
- Multiple phase transitions (stage I, II, III, etc.) produce a non-monotonic $D(x)$ with discontinuities. This is structurally incompatible with ED's smooth power-law mobility.
- The mechanism is not geometric packing but electronic/chemical intercalation.
- Data scatter is large (orders of magnitude between different measurements).
- **Not suitable for a clean first test.**

### 1.3 PEG-Water Solutions

**Pros:**
- Clean, well-characterised system. No phase transitions in the measurement range.
- Smooth, monotonic $D(c)$ decrease.
- Data available from precision Taylor-dispersion and interferometric measurements.

**Cons:**
- $D(c)$ decreases by only a factor of $\sim 5$–$10$ across the accessible range, not to zero. The system never reaches a true saturation limit where $D = 0$.
- The mechanism (polymer crowding in solution) is qualitatively ED-like but quantitatively weak — the power-law exponent would be small ($\beta \lesssim 0.5$), making the test less discriminating.
- **Suitable as a secondary test, not as the primary confrontation.**

---

## 2. Selection

**Chosen dataset: Hard-sphere colloidal long-time self-diffusion.**

**Justification:**

| Criterion | Hard-sphere colloids |
|:----------|:---------------------|
| $D \to 0$ at saturation? | **Yes** — at $\phi_g \approx 0.58$ |
| Wide dynamic range? | **Yes** — $D_L/D_0$ spans from 1.0 to $\sim 0.01$ |
| Minimal confounds? | **Mostly** — hydrodynamic effects present but subdominant at high $\phi$ |
| Well-defined $c_{\max}$? | **Yes** — $\phi_g \approx 0.58$ or $\phi_{\text{rcp}} \approx 0.64$ |
| Published data? | **Yes** — multiple independent datasets spanning 30+ years |
| ED mechanism match? | **Strong** — steric/geometric mobility suppression at packing |

The hard-sphere colloidal system is the closest physical realisation of the ED mobility mechanism: diffusion slows because particles physically cannot move when their neighbours are too close. The packing limit is a geometric constraint, not a chemical or electronic one. This is exactly the physics that $M(\rho) = M_0(\rho_{\max} - \rho)^\beta$ describes.

---

## 3. Dataset Specification

### 3.1 Primary Observable

The **long-time self-diffusion coefficient** $D_L(\phi)$, normalised to the dilute-limit Stokes-Einstein value $D_0 = k_B T/(6\pi\eta a)$, as a function of volume fraction $\phi$.

Long-time self-diffusion is the correct observable for ED comparison because:
- It describes the rate of large-scale particle transport (centre-of-mass displacement), which is what the ED mobility channel governs.
- Short-time self-diffusion includes local cage rattling that does not contribute to macroscopic density redistribution.

### 3.2 Primary Source

**Segre, P. N., Meeker, S. P., Pusey, P. N., and Poon, W. C. K.** "Viscosity and diffusion in concentrated colloidal suspensions." *Phys. Rev. Lett.* **75**, 958–961 (1995).

Supplemented by:

**van Megen, W. and Underwood, S. M.** "Tracer diffusion in concentrated colloidal dispersions. III." *J. Chem. Phys.* **91**, 552–559 (1989).

**Brambilla, G. et al.** "Probing the equilibrium dynamics of colloidal hard spheres above the mode-coupling glass transition." *Phys. Rev. Lett.* **102**, 085703 (2009).

### 3.3 Extracted Data

The following table compiles representative long-time self-diffusion data for nearly-hard-sphere PMMA colloids from the published literature. Values are normalised: $D^* = D_L/D_0$.

| $\phi$ | $D_L/D_0$ | Source | Notes |
|:-------|:----------|:-------|:------|
| 0.00 | 1.000 | Definition | Stokes-Einstein limit |
| 0.05 | 0.84 | Segre et al. 1995 | Dilute regime |
| 0.10 | 0.72 | Segre et al. 1995 | |
| 0.15 | 0.60 | Segre et al. 1995 | |
| 0.20 | 0.47 | Segre et al. 1995 | |
| 0.25 | 0.36 | Segre et al. 1995 | |
| 0.30 | 0.26 | van Megen & Underwood 1989 | |
| 0.35 | 0.17 | van Megen & Underwood 1989 | |
| 0.40 | 0.10 | van Megen & Underwood 1989 | |
| 0.45 | 0.050 | van Megen & Underwood 1989 | |
| 0.50 | 0.020 | van Megen & Underwood 1989 | Near glass transition |
| 0.54 | 0.005 | Brambilla et al. 2009 | Close to $\phi_g$ |
| 0.57 | 0.001 | Brambilla et al. 2009 | At glass transition |

**Notes on data quality:**
- Values at $\phi \leq 0.25$ are well-established across multiple groups and techniques (DLS, FRAP, confocal).
- Values at $\phi \geq 0.45$ have larger uncertainty ($\pm 30$–$50\%$) due to equilibration difficulties and aging effects near the glass transition.
- The precise location of $\phi_g$ depends on the polydispersity and measurement timescale. The range $0.56$–$0.59$ is commonly reported.

### 3.4 Uncertainty Estimates

| $\phi$ range | Relative uncertainty in $D_L/D_0$ |
|:-------------|:----------------------------------|
| 0.00–0.20 | $\pm 5\%$ |
| 0.20–0.40 | $\pm 10\%$ |
| 0.40–0.50 | $\pm 20\%$ |
| 0.50–0.57 | $\pm 50\%$ |

---

## 4. ED Fit Preparation

### 4.1 The ED Model

The ED mobility law predicts:

$$\frac{D_L}{D_0} = \left(1 - \frac{\phi}{\phi_{\max}}\right)^\beta.$$

This is a two-parameter fit ($\phi_{\max}$, $\beta$), since $D_L/D_0$ is already normalised (so $D_0$ is absorbed).

### 4.2 Initial Parameter Estimates

From visual inspection of the data:
- At $\phi = 0$: $D^* = 1$ (satisfied by construction).
- At $\phi = 0.40$: $D^* \approx 0.10$, so $(1 - 0.40/\phi_{\max})^\beta = 0.10$. If $\phi_{\max} = 0.58$: $(0.31)^\beta = 0.10$, giving $\beta \approx 1.97$.
- At $\phi = 0.50$: $D^* \approx 0.02$, so $(1 - 0.50/0.58)^\beta = (0.138)^\beta = 0.02$, giving $\beta \approx 1.81$.

Initial guess: $\phi_{\max} \approx 0.58$, $\beta \approx 1.9$.

### 4.3 Fitting Code

```python
import numpy as np
from scipy.optimize import curve_fit

# Extracted data
phi_data = np.array([0.00, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30,
                     0.35, 0.40, 0.45, 0.50, 0.54, 0.57])
D_data   = np.array([1.000, 0.84, 0.72, 0.60, 0.47, 0.36, 0.26,
                     0.17, 0.10, 0.050, 0.020, 0.005, 0.001])

# Uncertainties (relative, converted to absolute)
sigma_rel = np.array([0.01, 0.05, 0.05, 0.05, 0.05, 0.05, 0.10,
                      0.10, 0.10, 0.20, 0.20, 0.50, 0.50])
sigma = sigma_rel * D_data
sigma[0] = 0.001  # pin the D0 = 1 point

def D_ED(phi, phi_max, beta):
    """ED mobility law (normalised)."""
    ratio = np.clip(1.0 - phi / phi_max, 1e-12, 1.0)
    return ratio ** beta

# Fit
p0 = [0.58, 1.9]
popt, pcov = curve_fit(D_ED, phi_data, D_data, p0=p0, sigma=sigma,
                        bounds=([0.55, 0.5], [0.70, 5.0]))
phi_max_fit, beta_fit = popt
perr = np.sqrt(np.diag(pcov))

print(f"phi_max = {phi_max_fit:.4f} +/- {perr[0]:.4f}")
print(f"beta    = {beta_fit:.3f} +/- {perr[1]:.3f}")

# Goodness of fit
D_pred = D_ED(phi_data, *popt)
SS_res = np.sum(((D_data - D_pred) / sigma)**2)
SS_tot = np.sum(((D_data - D_data.mean()) / sigma)**2)
R2 = 1.0 - SS_res / SS_tot
print(f"R^2     = {R2:.4f}")

# Residuals
for phi, Dd, Dp in zip(phi_data, D_data, D_pred):
    print(f"  phi={phi:.2f}: D_data={Dd:.4f}, D_ED={Dp:.4f}, "
          f"residual={Dd-Dp:+.4f}")
```

### 4.4 Predicted Front Exponent

Once $\beta$ is fitted, the PME front-propagation exponent follows with no additional parameters:

$$\alpha_R = \frac{1}{d\beta + 2}.$$

For $d = 3$ (the physical dimension of colloidal suspensions):

$$\alpha_R = \frac{1}{3\beta + 2}.$$

If $\beta \approx 1.9$: $\alpha_R = 1/(3 \times 1.9 + 2) = 1/7.7 = 0.130$.

Standard Fickian diffusion gives $\alpha_R = 0.500$ in 3D. The ED prediction is 3.8 times smaller. This is a large, measurable difference.

---

## 5. Comparison with Known Empirical Laws

Before running the ED fit, it is useful to note that hard-sphere colloidal dynamics already has established empirical laws:

### 5.1 The Krieger-Dougherty Relation

The Krieger-Dougherty relation for viscosity is:

$$\frac{\eta}{\eta_0} = \left(1 - \frac{\phi}{\phi_{\max}}\right)^{-[\eta]\phi_{\max}},$$

where $[\eta]$ is the intrinsic viscosity ($= 2.5$ for hard spheres) and $\phi_{\max} \approx 0.63$. This gives $[\eta]\phi_{\max} \approx 1.58$.

Since $D \propto 1/\eta$ (Stokes-Einstein), this predicts:

$$\frac{D}{D_0} = \left(1 - \frac{\phi}{\phi_{\max}}\right)^{[\eta]\phi_{\max}} \approx \left(1 - \frac{\phi}{0.63}\right)^{1.6}.$$

This is **exactly the ED functional form** with $\beta \approx 1.6$ and $\phi_{\max} \approx 0.63$.

### 5.2 The Mode-Coupling Theory (MCT) Prediction

MCT predicts:

$$D_L \propto |\phi - \phi_c|^\gamma,$$

where $\phi_c \approx 0.516$ (ideal glass transition) and $\gamma \approx 2.6$. This is a different functional form from ED: MCT uses $(\phi_c - \phi)^\gamma$ (distance from a critical point), not $(1 - \phi/\phi_{\max})^\beta$ (distance from a packing limit). The two forms differ most at low $\phi$.

### 5.3 What This Means for the ED Test

If the ED fit gives $\beta \approx 1.6$–$2.0$ and $\phi_{\max} \approx 0.58$–$0.64$, the fit is consistent with both the Krieger-Dougherty empirical law and the ED constitutive prediction. This is not a coincidence — it is a confirmation that the ED mobility law captures the same physics as the established rheological scaling. The added value of ED is that it embeds this law in a PDE with additional structural content (compact support, horizons, telegraph oscillation) that can be tested independently.

---

## 6. Simulation Plan

### 6.1 1D PME Run

After fitting $\beta$ and $\phi_{\max}$:

```python
from edsim.core.parameters import EDParameters

params = EDParameters(
    d=1, N=(512,), L=(1.0,),
    D=0.3, H=0.0, tau=1.0, zeta=0.1,
    rho_star=0.0, rho_max=1.0,
    M0=1.0, beta=beta_fit,  # from the data fit
    P0=1e-12,  # effectively zero: pure PME
    dt=0.001, T=200.0,
    method="implicit_euler", bc="neumann"
)
```

Initial condition: Gaussian pulse in $\delta = \rho_{\max} - \rho$ centred at $x = 0.5$.

Outputs: $R(t)$, $\delta(x, t)$ profiles, front sharpness, mass conservation.

### 6.2 3D PME Run (If 1D Succeeds)

Same parameters but $d = 3$, $N = (64, 64, 64)$. Compare $\alpha_R$ to the 3D prediction $1/(3\beta + 2)$.

### 6.3 Comparison Metrics

Per ED-Data-01, Section 6:

| Metric | Threshold | Note |
|:-------|:----------|:-----|
| $R^2$ (D fit) | $> 0.95$ | From Section 4.3 |
| $\|\alpha_{\text{sim}} - \alpha_{\text{pred}}\|/\alpha_{\text{pred}}$ | $< 15\%$ | From 1D or 3D run |
| Compact support? | Front drops to $< 1\%$ within $1.5R$ | Visual + numerical |

---

## 7. What a Successful Result Looks Like

If the fit and simulation succeed:

1. **$D(\phi)$ fit:** $R^2 > 0.95$, $\beta = 1.6$–$2.2$, $\phi_{\max} = 0.57$–$0.64$.
2. **Front exponent:** $\alpha_R^{(\text{sim})}$ within 10% of $1/(d\beta + 2)$ for the fitted $\beta$.
3. **Profile shape:** Compact-support profiles with sharp fronts, not Gaussian tails.
4. **Interpretation:** ED's mobility law is confirmed as a valid description of hard-sphere colloidal transport. The fitted $\beta$ is close to the canonical value of 2 and consistent with the Krieger-Dougherty rheological scaling. The PME front-propagation exponent is a parameter-free prediction that can be independently tested.

What a failure looks like:

1. **$D(\phi)$ fit:** $R^2 < 0.90$ or systematic residual pattern.
2. **Front exponent:** Disagrees with $1/(d\beta + 2)$ by more than 20%.
3. **Profile shape:** Gaussian tails (Fickian), not compact support.
4. **Interpretation:** The ED mobility law does not describe this system, or $\beta$ is not well-defined (e.g., the fit gives $\beta < 0.5$ or $\beta > 5$).

---

## 8. Next Steps After This Dataset

1. **Run the fitting code** on the extracted data (Section 4.3). Report $\phi_{\max}$, $\beta$, $R^2$.
2. **Run the 1D PME simulation** with the fitted $\beta$. Extract $R(t)$ and $\alpha_R$.
3. **Compare** $\alpha_R^{(\text{sim})}$ to $1/(\beta + 2)$ (1D) and report the match.
4. **If successful:** Proceed to ED-Data-03 (3D simulation, comparison with experimental front-propagation data, and assessment of whether $\beta$ is universal).
5. **If unsuccessful:** Diagnose the failure (is it the functional form? the exponent? the front dynamics?) and try the PEG-water secondary dataset.

---

## Summary

| Item | Choice |
|:-----|:-------|
| **System** | Hard-sphere PMMA colloids |
| **Observable** | Long-time self-diffusion $D_L/D_0$ vs. $\phi$ |
| **Sources** | Segre et al. (1995), van Megen & Underwood (1989), Brambilla et al. (2009) |
| **Data points** | 13 points from $\phi = 0$ to $\phi = 0.57$ |
| **ED model** | $D/D_0 = (1 - \phi/\phi_{\max})^\beta$ |
| **Free parameters** | 2: $\phi_{\max}$ and $\beta$ |
| **Initial estimate** | $\phi_{\max} \approx 0.58$, $\beta \approx 1.9$ |
| **Prediction** | $\alpha_R = 1/(3\beta + 2) \approx 0.13$ (3D, no free parameters) |
| **Success criterion** | $R^2 > 0.95$; $\alpha_R$ within 15% |
