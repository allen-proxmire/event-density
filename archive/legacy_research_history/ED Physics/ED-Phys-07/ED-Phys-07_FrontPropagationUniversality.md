# ED-Phys-07: Front-Propagation Universality Across Materials

**Author:** Allen Proxmire
**Series:** ED-Phys-07
**Date:** March 2026
**Status:** Specification — ready for execution

**Inputs:**

| Source | Content used |
|--------|-------------|
| ED-Phys-06 | $\beta$-universality sweep, $\alpha_R = 1/(d\beta + 2)$ confirmed numerically for $\beta \in [0.5, 3.0]$ |
| ED-Data-06/07 | 10-material $\beta$ dataset, $\beta = 1.72 \pm 0.37$ |
| ED-Data-08 | Universality paper draft (weak universality, sub-class structure) |
| ED-Data-09 (original series) | BSA-FRAP experiment design (unexecuted) |
| Foundational Paper | Barenblatt/PME analogue (Analogue 2), $\alpha_R$ definition |

---

# 1. Motivation

## 1.1 The Completed Test: $\beta$

The ED mobility law $D(\phi) = D_0 M_0(1 - \phi/\phi_{\max})^\beta$ has been tested against 10 materials (ED-Data-06/07). The functional form is universal ($R^2 > 0.986$ for all 10). The exponent clusters near $\beta \approx 1.7$ with a range of $[1.3, 2.5]$. This establishes weak universality: the form holds everywhere, the exponent varies by material.

But $\beta$ is extracted from a *static* measurement — $D(\phi)$ at different concentrations. It tests the constitutive law but not the *dynamical* prediction.

## 1.2 The Open Test: $\alpha_R$

The ED PDE, via its reduction to the porous-medium equation, predicts that concentration fronts propagate as:

$$R(t) \propto t^{\alpha_R}, \qquad \alpha_R = \frac{1}{d\beta + 2} \tag{1}$$

This is a **zero-free-parameter prediction**: given $\beta$ (measured from $D(\phi)$) and $d$ (the spatial dimension of the experiment), $\alpha_R$ is fully determined. No fitting. No adjustable constants.

ED-Phys-06 confirmed equation (1) numerically for $\beta \in [0.5, 3.0]$ in $d = 2$ (simulation). The original ED-Data-11 noted that the 3-material 3D prediction ($\alpha_R \approx 0.123$ at $\beta \approx 2$) was consistent across materials. But **no direct experimental measurement of $\alpha_R$ has been performed in any material.**

This is the single most important open test in the ED programme. A measured $\alpha_R$ that matches the prediction from an independently measured $\beta$ would close the loop between the constitutive law (statics) and the PDE dynamics (front propagation), providing the first direct confirmation of the Barenblatt/PME reduction in a real physical system.

## 1.3 Why This Is High-Leverage

| Test type | What it tests | Status |
|-----------|---------------|--------|
| $D(\phi)$ fitting | Constitutive law (mobility form) | **Done** (10 materials) |
| $\alpha_R$ measurement | PDE dynamics (front propagation) | **Open** (0 materials) |
| $\beta$--$\alpha_R$ joint test | Constitutive + dynamics simultaneously | **Open** |

A single $\alpha_R$ measurement in one material would be more scientifically valuable than $\beta$ measurements in ten more materials, because it tests a *different prediction* of the same theory.

---

# 2. Predicted $\alpha_R$ Values

## 2.1 Predictions from the 10-Material Dataset

For each material, the predicted front exponent in $d = 3$ (the physical dimension) and $d = 1$ (the simplest experimental geometry) is:

| # | Material | $\beta$ | $\alpha_R^{(1D)} = \frac{1}{\beta + 2}$ | $\alpha_R^{(3D)} = \frac{1}{3\beta + 2}$ | $\alpha_R^{(3D)}$ uncertainty |
|---|----------|---------|---|---|---|
| 1 | Hard-sphere colloids | 1.690 | 0.271 | 0.132 | $\pm 0.008$ |
| 2 | Sucrose-water | 2.490 | 0.223 | 0.097 | $\pm 0.006$ |
| 3 | BSA protein | 2.120 | 0.243 | 0.118 | $\pm 0.008$ |
| 4 | Lysozyme | 1.360 | 0.298 | 0.165 | $\pm 0.004$ |
| 5 | PMMA colloids | 1.813 | 0.262 | 0.134 | $\pm 0.005$ |
| 6 | Ludox silica | 1.407 | 0.294 | 0.161 | $\pm 0.003$ |
| 7 | PEG-water | 1.297 | 0.303 | 0.172 | $\pm 0.005$ |
| 8 | Dextran | 1.464 | 0.289 | 0.155 | $\pm 0.007$ |
| 9 | Casein micelles | 1.794 | 0.264 | 0.135 | $\pm 0.004$ |
| 10 | Glycerol-water | 1.741 | 0.267 | 0.139 | $\pm 0.003$ |

**Uncertainty propagation:** From $\alpha_R = 1/(d\beta + 2)$:

$$\sigma_{\alpha_R} = \frac{d}{(d\beta + 2)^2}\,\sigma_\beta$$

## 2.2 Range of Predicted $\alpha_R^{(3D)}$

The 10-material predictions span $\alpha_R^{(3D)} \in [0.097, 0.172]$, a factor of 1.77. The mean is $\bar{\alpha}_R = 0.141$. At the canonical $\beta = 2$: $\alpha_R = 0.125$.

In 1D, the range is $[0.223, 0.303]$ — wider and easier to distinguish experimentally because the exponents are larger and more separated.

## 2.3 The Discriminating Power of $\alpha_R$

Consider two materials with $\beta$ values that differ by $\Delta\beta = 0.5$ (e.g., Lysozyme at 1.36 vs. PMMA at 1.81):

- In $d = 3$: $\Delta\alpha_R = 0.165 - 0.134 = 0.031$ (a 19% relative difference)
- In $d = 1$: $\Delta\alpha_R = 0.298 - 0.262 = 0.036$ (a 12% relative difference)

An $\alpha_R$ measurement with 10% precision would be sufficient to distinguish these materials on the universality curve. An $\alpha_R$ measurement with 5% precision would provide a stringent consistency check between independently measured $\beta$ and $\alpha_R$.

---

# 3. Experimental Data Requirements

## 3.1 What Is Needed

To extract $\alpha_R$ from experiment, the minimum data requirement is:

| Requirement | Specification | Why |
|-------------|---------------|-----|
| Spatial concentration profiles | $c(x, t)$ or $c(r, t)$ at $\geq 5$ time points | To track the front position $R(t)$ |
| Time stamps | Absolute times $t_1, \ldots, t_n$ | Power-law fit requires $\log t$ |
| Imaging resolution | $\Delta x < R_{\text{final}} / 20$ | Resolve the front width |
| Concentration calibration | Known relationship between signal and $c$ | Map intensity to physical units |
| Geometry | 1D (planar) or 3D (radial) — must be specified | Determines $d$ in $\alpha_R = 1/(d\beta + 2)$ |
| Time span | $t_{\max} / t_{\min} > 10$ | Sufficient dynamic range for power-law fitting |

## 3.2 Candidate Experimental Techniques

| Technique | Geometry | Resolution | Time range | Materials suited |
|-----------|----------|------------|------------|------------------|
| FRAP (fluorescence recovery) | 2D/3D radial | $\sim 1$ $\mu$m | ms to min | Proteins (BSA, lysozyme), polymers (PEG, dextran) |
| Gradient diffusion cell + optical tracking | 1D planar | $\sim 10$ $\mu$m | min to hours | Colloids (PMMA, Ludox), sucrose |
| Confocal microscopy | 3D | $\sim 0.5$ $\mu$m | s to min | Fluorescent colloids (PMMA), casein |
| Mach-Zehnder interferometry | 1D planar | $\sim 1$ $\mu$m | min to hours | Small molecules (glycerol, sucrose) |
| NMR profiling | 1D | $\sim 100$ $\mu$m | min to hours | Any hydrogen-containing system |

## 3.3 Published Front-Propagation Data: Assessment

| Material | Published spatial profiles? | Suitable for $\alpha_R$ extraction? | Source |
|----------|----|---|---|
| Hard-sphere colloids | Yes (DLS studies with spatial resolution) | **Potentially** — requires reprocessing | Segre et al. 1995 |
| Sucrose-water | Yes (interferometric profiles) | **Yes** — Vergara et al. report $c(x,t)$ | Vergara et al. 2001 |
| BSA protein | No (DLS only, no spatial profiles) | **No** — FRAP experiment designed (ED-Data-09) but unexecuted | — |
| Lysozyme | No (DLS/NMR bulk measurements) | **No** | — |
| PMMA colloids | Yes (confocal microscopy + light scattering) | **Potentially** — Poon et al. 2012 have spatial data | Poon et al. 2012 |
| Ludox silica | No (bulk DLS/SANS) | **No** | — |
| PEG-water | Yes (interferometric profiles) | **Yes** — Vergara et al. report $c(x,t)$ | Vergara et al. 2001 |
| Dextran | Partial (some FRAP studies) | **Potentially** — Luby-Phelps et al. have FRAP data | Luby-Phelps 1986 |
| Casein micelles | No (bulk DLS) | **No** | — |
| Glycerol-water | Yes (Taylor dispersion profiles) | **Potentially** — D'Errico et al. report spreading profiles | D'Errico et al. 2004 |

**Summary:** Three materials (sucrose, PEG, glycerol) have published 1D spatial profiles suitable for direct $\alpha_R$ extraction. Two more (PMMA, hard-sphere colloids) have spatial data that may be reprocessable. Five materials lack spatial profiles and would require new experiments.

---

# 4. Extraction Pipeline

## 4.1 Front Detection

Given spatial profiles $c(x, t_n)$ at times $t_1 < t_2 < \cdots < t_N$:

1. Define the front threshold: $c_{\text{front}} = (c_{\max} + c_{\min}) / 2$ (midpoint between reservoir and background concentrations).

2. For each profile, locate the front position $R(t_n)$:
   - **Threshold crossing:** $R(t_n) = x$ such that $c(x, t_n) = c_{\text{front}}$ (linear interpolation between grid points).
   - **Half-maximum radius:** $R(t_n) = \max\{x : c(x, t_n) > c_{\text{front}}\}$.
   - **Inflection point:** $R(t_n) = x$ where $|\partial_x c|$ is maximum (steepest gradient).

3. Record $\{(t_n, R(t_n))\}_{n=1}^N$.

## 4.2 Power-Law Fitting

Fit $R(t) = C \cdot t^{\alpha_R}$ via log-log linear regression:

$$\log R(t_n) = \alpha_R \cdot \log t_n + \log C \tag{2}$$

Exclude the first 1--2 time points (transient from initial condition to self-similar regime) and any points where $R$ has reached the domain boundary.

**Quality metrics:**
- $R^2$ of the log-log fit (require $> 0.95$).
- Residual pattern (must be random, not systematic).
- Sensitivity to threshold choice (vary $c_{\text{front}}$ by $\pm 20\%$ and check $\alpha_R$ stability).

## 4.3 Uncertainty Estimation

1. **Bootstrap on time points:** Resample the $(t_n, R_n)$ pairs with replacement (1000 iterations) and refit.
2. **Threshold sensitivity:** Repeat extraction at $c_{\text{front}} \pm 10\%$ and $c_{\text{front}} \pm 20\%$.
3. **Combined uncertainty:** $\sigma_{\alpha_R} = \sqrt{\sigma_{\text{bootstrap}}^2 + \sigma_{\text{threshold}}^2}$.

## 4.4 Comparison to Prediction

For each material:

1. Compute $\alpha_R^{\text{pred}} = 1/(d\beta + 2)$ from the independently measured $\beta$ and the experimental geometry $d$.
2. Compute the discrepancy: $\epsilon = |\alpha_R^{\text{meas}} - \alpha_R^{\text{pred}}| / \alpha_R^{\text{pred}}$.
3. Classify:

| $\epsilon$ | Verdict |
|-----------|---------|
| $< 10\%$ | **Strong confirmation** |
| $10$--$20\%$ | **Consistent** |
| $20$--$50\%$ | **Tension** (may indicate finite-time or resolution effects) |
| $> 50\%$ | **Falsified** (the Barenblatt reduction fails for this material) |

---

# 5. Universality Test Plan

## 5.1 Phase 1: Published Spatial Data (3 Materials)

Extract $\alpha_R$ from existing published spatial profiles for:

| Material | Geometry | Source | Expected $\alpha_R$ | $d$ |
|----------|----------|--------|---------------------|-----|
| Sucrose-water | 1D planar | Vergara et al. 2001 | 0.223 | 1 |
| PEG-water | 1D planar | Vergara et al. 2001 | 0.303 | 1 |
| Glycerol-water | 1D planar | D'Errico et al. 2004 | 0.267 | 1 |

All three use interferometric data in 1D planar geometry. The $d = 1$ predictions are well separated (0.22 to 0.30), so even moderate precision would test the relationship.

## 5.2 Phase 2: Reprocessed Data (2 Materials)

Extract $\alpha_R$ from reprocessed confocal/scattering data for:

| Material | Geometry | Source | Expected $\alpha_R$ | $d$ |
|----------|----------|--------|---------------------|-----|
| PMMA colloids | 3D radial | Poon et al. 2012 | 0.134 | 3 |
| Hard-sphere colloids | 3D radial | Segre et al. 1995 | 0.132 | 3 |

These require digitising published figures or obtaining raw data from authors.

## 5.3 Phase 3: New Experiments (2--3 Materials)

Design and execute FRAP or gradient-cell experiments for:

| Material | Technique | Expected $\alpha_R$ | $d$ |
|----------|-----------|---------------------|-----|
| BSA protein | FRAP (2D radial) | 0.155 ($d = 2$) | 2 |
| Lysozyme | FRAP (2D radial) | 0.209 ($d = 2$) | 2 |
| Casein micelles | Confocal (3D radial) | 0.135 | 3 |

The BSA-FRAP experiment was designed in ED-Data-09 but never executed. It remains the highest-priority new experiment.

## 5.4 Success Criteria

| Level | Criterion | What it proves |
|-------|-----------|----------------|
| Minimum | 1 material with $\epsilon < 20\%$ | The Barenblatt reduction works in at least one real system |
| Target | 3 materials with $\epsilon < 20\%$ | The $\beta$--$\alpha_R$ relationship is empirically confirmed |
| Full | 5+ materials spanning $\beta \in [1.3, 2.5]$ with $\epsilon < 15\%$ | Front-propagation universality established |

---

# 6. Roadmap

## 6.1 ED-Phys-08: Front Extraction Execution

Execute the Phase 1 extraction for sucrose-water, PEG-water, and glycerol-water using published interferometric profiles. Deliverables:
- Extracted $\alpha_R$ values with uncertainties.
- Comparison to predictions.
- Three ED-Data packages with front data.

## 6.2 ED-Phys-09: Full $\alpha_R$ Universality Synthesis

Combine Phase 1 and Phase 2 results (5 materials with $\alpha_R$ measurements) into a synthesis:
- Joint $\beta$--$\alpha_R$ universality plot.
- Test of the theoretical curve $\alpha_R = 1/(d\beta + 2)$.
- Updated classification of all materials.

## 6.3 ED-Data-11 (Revised): Joint Universality Map

Produce the definitive figure: 10 materials plotted on the $(\beta, \alpha_R)$ plane against the theoretical curve, with independently measured $\beta$ (from $D(\phi)$) and $\alpha_R$ (from front propagation) for each material that has both measurements. This figure is the strongest possible empirical test of the ED mobility law and the Barenblatt/PME reduction.

## 6.4 Timeline

| Module | Materials | Data source | Est. sessions |
|--------|-----------|-------------|---------------|
| ED-Phys-08 | Sucrose, PEG, Glycerol | Published profiles | 1--2 |
| ED-Phys-09 | + PMMA, Hard-sphere | Reprocessed data | 1--2 |
| ED-Data-11 rev | All with $\alpha_R$ | Combined | 1 |

---

*ED-Phys-07 · Event Density Research Programme · March 2026*
