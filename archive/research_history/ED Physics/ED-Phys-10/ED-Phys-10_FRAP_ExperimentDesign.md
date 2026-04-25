# ED-Phys-10: Design of the BSA-FRAP Void-Spreading Experiment

**Author:** Allen Proxmire
**Series:** ED-Phys-10
**Date:** March 2026
**Status:** Experiment design — ready for synthetic validation (ED-Phys-11) and lab execution

**Inputs:**

| Source | Content used |
|--------|-------------|
| ED-Phys-09 | Negative result: standard D(c) spreading does not produce PME exponent |
| ED-Phys-08 | Positive result: ED PME simulation confirms alpha_R |
| ED-Phys-07 | Predicted alpha_R values for all 10 materials |
| ED-Data-08 (original series) | BSA protein: beta = 2.12, R^2 = 0.986 |
| ED-Data-09 (original series) | Initial FRAP experiment concept (unexecuted) |
| ED-Phys-06 | Beta-universality confirmed numerically |

---

# 1. Motivation

## 1.1 The ED-Phys-09 Lesson

ED-Phys-09 demonstrated that the front-propagation exponent $\alpha_R = 1/(d\beta + 2)$ **cannot** be measured from standard concentration-spreading experiments. When a bump of solute spreads into a dilute background, the front propagates into the region where $D(c)$ is *large* (fast diffusion), not where $D(c) \to 0$ (degenerate diffusion). The resulting exponent is near-Fickian ($\alpha_R \approx 0.5$), not PME-like ($\alpha_R \approx 0.12$).

The ED prediction is specific: it applies to the **complementary variable** $\delta = \rho_{\max} - \rho$, which satisfies the porous-medium equation. The front in the $\delta$ variable propagates into the region where $\delta \to 0$ (i.e., $\rho \to \rho_{\max}$), where the mobility $M(\rho) = M_0(\rho_{\max} - \rho)^\beta$ vanishes. This produces compact support, finite-speed propagation, and the Barenblatt exponent.

## 1.2 The Correct Geometry: Void Spreading

The ED exponent is observable when:
- The background is at high concentration ($\rho \approx \rho_{\max}$, $\delta \approx 0$, mobility $\approx 0$).
- A localised region has lower concentration ($\rho < \rho_{\max}$, $\delta > 0$, mobility $> 0$).
- The "void" (low-density region) spreads into the dense background.

This is the inverse of standard spreading: instead of solute diffusing into solvent, a *gap* in the solute field diffuses into a concentrated matrix.

## 1.3 FRAP Provides Exactly This Geometry

In a FRAP experiment:
1. A dense fluorescent solution fills the sample chamber.
2. A focused laser photobleaches a small region, destroying the fluorescence locally.
3. Unbleached fluorescent molecules diffuse *into* the bleached region, recovering the fluorescence.

The **bleached region** is the void ($\delta > 0$). The **unbleached background** is the dense matrix ($\delta \approx 0$). The recovery front — the boundary between bleached and unbleached — propagates *into* the dense background as the void fills in.

In the $\delta$ variable (where $\delta$ represents the fluorescence deficit), this is a compact bump spreading according to the degenerate mobility law. The spreading exponent of the recovery front is $\alpha_R = 1/(d\beta + 2)$.

**FRAP is the natural experimental realisation of the ED PME analogue.**

---

# 2. Experimental Setup

## 2.1 Sample Preparation

| Parameter | Specification | Rationale |
|-----------|---------------|-----------|
| Protein | BSA (bovine serum albumin) | Best-characterised material in the ED-Data series ($\beta = 2.12$) |
| Fluorescent label | BSA-FITC or BSA-Alexa488 | Standard fluorescent conjugates, widely available |
| Concentration | 200--350 mg/mL ($\phi = 0.15$--$0.25$) | High enough for degenerate mobility to be significant; below gelation |
| Buffer | 50 mM phosphate, pH 7.0, 150 mM NaCl | Standard physiological buffer; minimises electrostatic artifacts |
| Temperature | $25.0 \pm 0.1$ °C | Matches the published $D(c)$ data from Roosen-Runge et al. |
| Sample geometry | Thin chamber (10--50 $\mu$m depth) between coverslips | Quasi-2D to match $d = 2$ prediction; minimises convection |
| Chamber material | Glass coverslip + spacer + glass slide | Low autofluorescence |

## 2.2 Photobleaching

| Parameter | Specification | Rationale |
|-----------|---------------|-----------|
| Bleach laser | 488 nm (argon) or 473 nm (solid-state), 10--50 mW at sample | Standard FRAP wavelength for FITC/Alexa488 |
| Bleach geometry | Circular spot, radius $r_0 = 2$--$5$ $\mu$m | Small enough for the front to propagate measurably; large enough for confocal resolution |
| Bleach duration | 0.5--2.0 s | Complete bleaching in the spot centre ($> 80\%$ fluorescence loss) |
| Bleach depth | $> 80\%$ fluorescence reduction at spot centre | Ensures $\delta / \delta_{\max} > 0.8$, well into the nonlinear regime |
| Bleach profile | Approximately Gaussian (inherent to focused laser) | Matches the Gaussian IC used in ED simulations |

## 2.3 Imaging

| Parameter | Specification | Rationale |
|-----------|---------------|-----------|
| Microscope | Confocal (LSM) or widefield epifluorescence | Confocal gives better z-sectioning; widefield is faster |
| Imaging laser | 488 nm, low power (0.1--1 mW) | Avoid additional bleaching during imaging |
| Frame rate | 1--10 fps (depending on $D_0$ and $r_0$) | Must resolve the recovery timescale $\tau_{\text{rec}} = r_0^2 / D_0$ |
| Total imaging time | $5\tau_{\text{rec}}$ to $20\tau_{\text{rec}}$ | Sufficient to observe the power-law regime and approach full recovery |
| Pixel size | $< r_0 / 10$ ($< 0.2$--$0.5$ $\mu$m) | Resolve the front width |
| Field of view | $> 5 r_0$ ($> 10$--$25$ $\mu$m) | Capture the full spreading profile without boundary effects |
| Number of frames | 50--200 | Sufficient for log-log fitting with 10+ points in the power-law regime |

## 2.4 Resolution Requirements

For BSA at $c = 250$ mg/mL:
- $D_0 \approx 6.1 \times 10^{-11}$ m$^2$/s (dilute self-diffusion)
- $D(\phi = 0.18) \approx 3 \times 10^{-11}$ m$^2$/s (at working concentration)
- Recovery timescale for $r_0 = 3$ $\mu$m: $\tau_{\text{rec}} = r_0^2 / D \approx (3 \times 10^{-6})^2 / (3 \times 10^{-11}) = 0.3$ s
- Total experiment duration: $\sim 5$ s
- Required time resolution: $\Delta t \leq \tau_{\text{rec}} / 10 = 30$ ms (achievable with standard confocal at 30 fps)
- Required spatial resolution: $\Delta x \leq r_0 / 10 = 0.3$ $\mu$m (standard confocal)

---

# 3. Theoretical Prediction

## 3.1 The ED Prediction for BSA

BSA protein: $\beta = 2.12 \pm 0.18$, $\phi_{\max} = 0.40$.

In the FRAP geometry ($d = 2$, radial spreading from a circular bleach spot):

$$\alpha_R = \frac{1}{d\beta + 2} = \frac{1}{2 \times 2.12 + 2} = \frac{1}{6.24} = 0.1603 \tag{1}$$

Uncertainty:

$$\sigma_{\alpha_R} = \frac{d}{(d\beta + 2)^2}\sigma_\beta = \frac{2}{6.24^2} \times 0.18 = 0.0092 \tag{2}$$

$$\boxed{\alpha_R^{\text{BSA, 2D}} = 0.160 \pm 0.009}$$

## 3.2 Comparison Values

| Material | $\beta$ | $d$ (experiment) | $\alpha_R$ predicted | $\pm$ |
|----------|---------|---|---|---|
| BSA (FRAP, 2D) | 2.12 | 2 | **0.160** | 0.009 |
| BSA (3D radial) | 2.12 | 3 | 0.118 | 0.007 |
| Lysozyme (FRAP, 2D) | 1.36 | 2 | 0.213 | 0.004 |
| PMMA (confocal, 3D) | 1.81 | 3 | 0.134 | 0.005 |
| Fickian reference | — | 2 | 0.500 | 0 |

The ED prediction ($\alpha_R = 0.16$) is dramatically different from Fickian diffusion ($\alpha_R = 0.50$). A standard FRAP recovery curve follows $R(t) \propto t^{0.5}$; the ED prediction is that at high BSA concentration, the recovery is much slower: $R(t) \propto t^{0.16}$.

## 3.3 Expected Front Shape

The Barenblatt self-similar profile in 2D is:

$$\delta(r, t) = t^{\alpha_\rho}\,\left[C - k\,\frac{r^2}{t^{2\alpha_R}}\right]_+^{1/\beta} \tag{3}$$

where $[x]_+ = \max(x, 0)$ enforces compact support. The front is at $R(t) = \sqrt{C/k}\,t^{\alpha_R}$.

In terms of the fluorescence intensity $I(r, t) = I_0 - I_0\,\delta(r,t)/\delta_{\max}$:

- Inside the bleach spot ($r < R(t)$): $I < I_0$ (partially recovered).
- Outside the front ($r > R(t)$): $I = I_0$ (unbleached, full intensity).
- The front is **sharp** (compact support), not a smooth Gaussian tail.

This sharp front is the **observable signature** of the ED mobility law. Fickian diffusion produces a smooth Gaussian recovery; ED produces a sharp-edged recovery front that expands as $t^{0.16}$.

## 3.4 Time Regimes

| Time regime | $t$ relative to $\tau_{\text{rec}}$ | Expected behaviour |
|------------|---|---|
| Early ($t < 0.1\tau$) | Initial transient | IC adjusts to self-similar form; $\alpha_R$ not yet established |
| Intermediate ($0.1\tau < t < 5\tau$) | **Power-law regime** | $R(t) \propto t^{0.16}$; this is where $\alpha_R$ is measured |
| Late ($t > 5\tau$) | Near-complete recovery | Front reaches the edge of the initially bleached region; finite-size effects |

The measurement window is $0.1\tau_{\text{rec}} < t < 5\tau_{\text{rec}}$, corresponding to $\sim 0.03$ s to $\sim 1.5$ s for BSA at 250 mg/mL with $r_0 = 3$ $\mu$m.

---

# 4. Measurement Pipeline

## 4.1 Image Preprocessing

1. **Background subtraction:** Subtract the pre-bleach baseline from all frames to remove autofluorescence and optical aberrations.
2. **Normalisation:** Divide each frame by the pre-bleach frame to obtain the fractional fluorescence deficit $\delta(x,y,t) = 1 - I(x,y,t)/I_{\text{pre}}(x,y)$.
3. **Radial averaging:** Average $\delta$ in annular bins centred on the bleach spot to obtain $\delta(r, t)$.
4. **Noise filtering:** Apply a mild Gaussian smoothing ($\sigma_{\text{smooth}} = 1$ pixel) only if single-pixel noise is dominant.

## 4.2 Front Detection

For each time frame $t_n$:

1. Compute the radial profile $\delta(r, t_n)$.
2. Define the front position using **two methods**:
   - **Half-maximum:** $R(t_n) = r$ where $\delta(r) = \delta_{\text{centre}} / 2$.
   - **Threshold:** $R(t_n) = r$ where $\delta(r) = 0.1 \times \delta_{\text{centre}}(t_0)$ (10% of initial bleach depth).
3. Record both $R_{\text{half}}(t_n)$ and $R_{\text{thresh}}(t_n)$.

## 4.3 Power-Law Fitting

1. Select the fitting window: $t \in [0.1\tau_{\text{rec}}, 5\tau_{\text{rec}}]$.
2. Log-log linear regression: $\ln R = \alpha_R \ln t + \ln C$.
3. Compute $R^2$ and residuals.
4. Repeat for both front definitions (half-max and threshold).

## 4.4 Uncertainty Estimation

1. **Bootstrap:** Resample the $(t_n, R_n)$ pairs with replacement (1000 iterations).
2. **Threshold sensitivity:** Compare $\alpha_R$ from the half-max and threshold definitions.
3. **Frame-rate sensitivity:** Sub-sample the data at half the frame rate and refit.
4. **Combined:** $\sigma_{\alpha} = \sqrt{\sigma_{\text{boot}}^2 + (\Delta\alpha_{\text{thresh}}/2)^2 + (\Delta\alpha_{\text{subsample}}/2)^2}$.

## 4.5 Comparison to Prediction

Compute the normalised discrepancy:

$$\epsilon = \frac{|\alpha_R^{\text{meas}} - \alpha_R^{\text{pred}}|}{\sqrt{\sigma_{\text{meas}}^2 + \sigma_{\text{pred}}^2}} \tag{4}$$

---

# 5. Practical Considerations

## 5.1 Photobleaching Depth

The bleach must be deep enough ($> 80\%$) to place the system in the nonlinear regime where $M(\rho)$ is significantly different from $M_0$. At shallow bleach ($< 30\%$), the fluorescence deficit $\delta$ is small relative to $\rho_{\max}$, and the mobility is approximately constant — the recovery is Fickian regardless of $\beta$.

**Criterion:** Bleach depth $> 80\%$ at the spot centre. Verify by comparing the centre intensity immediately post-bleach to the pre-bleach level.

## 5.2 Avoiding Convection

At high protein concentration ($> 200$ mg/mL), the sample is viscous enough that convection is negligible. Additional precautions:
- Use a sealed chamber (no evaporation).
- Allow thermal equilibration ($> 10$ min) after mounting.
- Verify by checking that the bleach spot remains centred (no drift $> 0.5$ $\mu$m over the measurement window).

## 5.3 Temperature Control

The diffusion coefficient is strongly temperature-dependent ($D \propto T/\eta(T)$). A $\pm 1$ °C uncertainty at $25$ °C changes $D$ by $\sim 3\%$, which propagates to $\alpha_R$ as a $\sim 1\%$ effect. This is smaller than the statistical uncertainty.

**Criterion:** Temperature stable to $\pm 0.5$ °C during measurement.

## 5.4 Imaging Noise

Photon shot noise in confocal imaging produces fluctuations in the radial profile $\delta(r, t)$. The front position $R(t)$ is estimated from a threshold crossing, which can be noisy if the profile is not smooth.

**Mitigations:**
- Average over 3--5 repeated experiments at the same concentration.
- Use radial averaging (many pixels contribute to each annular bin).
- Apply mild smoothing if the signal-to-noise ratio at the front is $< 3$.

## 5.5 Concentration Range

The experiment should be repeated at 3--5 concentrations spanning $\phi = 0.10$ to $\phi = 0.25$. The ED prediction is that $\alpha_R$ is independent of concentration (it depends only on $\beta$, which is a material constant). Observing the same $\alpha_R$ at multiple concentrations would be an independent confirmation.

If $\alpha_R$ varies systematically with concentration, this would indicate that $\beta$ is concentration-dependent — a deviation from the ED constitutive law that would narrow the universality claim.

---

# 6. Success Criteria

## 6.1 Classification

| Discrepancy $\epsilon$ | Verdict | Interpretation |
|------------------------|---------|----------------|
| $\epsilon < 1$ | **Strong confirmation** | $\alpha_R$ matches ED prediction within combined uncertainties |
| $1 \leq \epsilon < 2$ | **Consistent** | Agreement within $2\sigma$; consistent but not definitive |
| $2 \leq \epsilon < 3$ | **Tension** | Marginal disagreement; may indicate finite-time or resolution effects |
| $\epsilon \geq 3$ | **Falsified** | Clear disagreement; the Barenblatt reduction fails for BSA |

## 6.2 Minimum Success

- At least one concentration with $\epsilon < 2$ (Consistent or better).
- $R^2 > 0.95$ for the log-log fit.
- No systematic residual pattern.

## 6.3 Full Success

- Three or more concentrations with $\epsilon < 1$ (Strong confirmation).
- $\alpha_R$ independent of concentration within uncertainties.
- Sharp front observed (qualitative: compact support, not Gaussian tail).
- $R^2 > 0.99$ for the log-log fit.

## 6.4 What Falsification Would Mean

If $\alpha_R$ is Fickian ($\approx 0.5$) at all concentrations, the degenerate mobility is not producing the expected PME-like dynamics in real BSA solutions. Possible causes:
- The true $D(c)$ functional form is not a power law near $c_{\max}$.
- The photobleaching creates a chemical modification, not just a fluorescence deficit.
- Hydrodynamic interactions or viscoelasticity dominate over the mobility mechanism.

Any of these would narrow the scope of the ED mobility law from "quantitative constitutive law" to "phenomenological fit for D(c) only."

---

# 7. Roadmap

## 7.1 ED-Phys-11: Synthetic FRAP Simulation

Before running the real experiment, simulate it computationally:
- Solve the 2D ED PDE with a Gaussian bleach IC at BSA parameters.
- Extract $\alpha_R$ from the simulated fluorescence recovery.
- Verify that the pipeline recovers $\alpha_R = 0.160$ from synthetic data.
- Test sensitivity to bleach depth, noise level, and frame rate.

This validates the measurement pipeline and identifies the optimal experimental parameters.

## 7.2 ED-Phys-12: Experimental Collaboration Plan

Identify a collaborator or facility with:
- Confocal microscope with FRAP capability.
- Temperature-controlled sample stage.
- BSA-FITC at $> 200$ mg/mL (or capacity to prepare it).

Produce a 1-page experimental protocol document suitable for sharing with a collaborator who does not need to understand the ED framework — only the measurement procedure and the predicted exponent.

## 7.3 ED-Data-12: Joint Beta-Alpha_R Universality Map

Once $\alpha_R$ is measured for BSA:
- Plot BSA at $(\beta, \alpha_R)$ on the universality map alongside the 10 $\beta$-only materials.
- This is the first point with *both* $\beta$ (from $D(c)$) and $\alpha_R$ (from FRAP) independently measured.
- If additional materials are measured (lysozyme-FRAP, PMMA-confocal), add them.

The target figure: the universality curve $\alpha_R = 1/(d\beta + 2)$ with materials plotted as points with error bars in both coordinates. This is the definitive test of the ED Barenblatt/PME reduction.

---

*ED-Phys-10 · Event Density Research Programme · March 2026*
