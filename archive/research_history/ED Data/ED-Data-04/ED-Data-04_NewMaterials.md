# ED-Data-04: New Materials and Universality Expansion

**Author:** Allen Proxmire
**Series:** ED-Data-04
**Date:** March 2026
**Status:** Material selection and pipeline specification

**Inputs:**

| Source | Content used |
|--------|-------------|
| ED-Data-01 through 03 | Hard-sphere colloids (Segre et al. 1995), β = 1.69 |
| ED-Data-05 through 07 | Sucrose-water (Price et al. 2016), β = 2.49 |
| ED-Data-08 through 10 | BSA protein solutions (Roosen-Runge et al. 2011), β = 2.12 |
| ED-Data-11 | Universality map: β = 2.10 ± 0.40 across 3 materials, α_R ≈ 0.123 |
| ED-Phys-06 | β-universality sweep: α_R = 1/(dβ+2) confirmed for β ∈ [0.5, 3.0] |
| ED-Cosmo-06 | Cosmology parked; condensed matter is the next active programme |

---

# 1. Motivation

## 1.1 Why Condensed Matter, Why Now

The ED cosmology programme (ED-Cosmo-01 through 06) has been parked with a provisional verdict: pure ED telegraph cosmology cannot reproduce the observed expansion history without a gravitational sector. The three roadmap options (ED-Poisson, alternative scale-factor, hybrid) require theoretical groundwork before further simulation.

Meanwhile, ED's condensed-matter contact point is the framework's strongest empirical asset — and it is built on only three materials. The universality claim β = 2.00 ± 0.29 (from the Foundational Paper) or β = 2.10 ± 0.40 (from ED-Data-11's expanded analysis) rests on:

1. **Hard-sphere colloids** (Segre et al. 1995): β = 1.69, R² = 0.995
2. **Sucrose-water solutions** (Price et al. 2016): β = 2.49, R² = 0.987
3. **BSA protein solutions** (Roosen-Runge et al. 2011): β = 2.12, R² = 0.986

Three points on the universality curve. Each additional material that fits the mobility law $M(\rho) = M_0(\rho_{\max} - \rho)^\beta$ with β ≈ 2 is an independent confirmation. Each material that *doesn't* fit identifies a boundary of the universality class. Either outcome advances the science.

## 1.2 The Scientific Return

| Number of materials | Statistical power | Status |
|---------------------|-------------------|--------|
| 3 (current) | Suggestive (σ = 0.40, wide) | Done |
| 5 | Moderate (σ narrows if consistent) | Target for ED-Data-05 |
| 8–10 | Strong (can distinguish β = 2.0 from β = 1.5 or 2.5) | Target for ED-Data-06 |

The β-universality sweep from ED-Phys-06 confirmed that the simulation engine correctly reproduces $\alpha_R = 1/(d\beta + 2)$ for β ∈ [0.5, 3.0]. The simulation side is ready. The limiting factor is experimental data.

---

# 2. Material Selection Criteria

## 2.1 Required Properties

A material is suitable for ED universality testing if it satisfies all of the following:

| # | Criterion | Rationale |
|---|-----------|-----------|
| C1 | **Concentration-dependent diffusion**: $D(c)$ decreases with increasing concentration | The ED mobility law predicts $M(\rho) \propto (\rho_{\max} - \rho)^\beta$, which requires $D$ to vanish at a finite concentration $\rho_{\max}$ |
| C2 | **Published $D(c)$ data**: at least 5 data points spanning $c/c_{\max} \in [0.1, 0.8]$ | Sufficient for a power-law fit with meaningful $R^2$ |
| C3 | **Identifiable $c_{\max}$ or $\phi_{\max}$**: a maximum packing, solubility limit, or glass transition | Needed to define $(\rho_{\max} - \rho)$ in the mobility law |
| C4 | **No confounding physics**: no phase transitions, crystallisation, gelation, or chemical reactions in the measurement range | These would introduce non-ED dynamics that contaminate the $D(c)$ relationship |
| C5 | **Reproducible measurements**: $D(c)$ from DLS, NMR, FRAP, or interferometry with stated uncertainties | Quality control |

## 2.2 Desirable Properties

| # | Criterion | Rationale |
|---|-----------|-----------|
| D1 | **Front-propagation data available**: spatial profiles $c(x,t)$ from gradient diffusion cells or FRAP | Enables direct $\alpha_R$ measurement, not just $D(c)$ fitting |
| D2 | **Different physical mechanism** from the existing three | Expands the universality claim across mechanisms |
| D3 | **Well-characterised thermodynamics**: equation of state, virial coefficients, or osmotic pressure known | Enables connection to theoretical models |
| D4 | **Available at standard lab conditions**: room temperature, aqueous | Practical reproducibility |

## 2.3 Candidate Materials

| # | Material | Type | Mechanism | $c_{\max}$ proxy | Published $D(c)$ source | Priority |
|---|----------|------|-----------|-------------------|------------------------|----------|
| 1 | **Lysozyme solutions** | Protein | Short-range attraction + crowding | Crystal solubility / gel | Muschol & Rosenberger 1997; Roosen-Runge et al. 2011 | **High** |
| 2 | **PMMA colloids in cis-decalin** | Synthetic colloid | Hard-sphere + depletion | Random close packing (φ ≈ 0.64) | van Megen & Underwood 1994; Poon et al. 2012 | **High** |
| 3 | **Silica nanoparticles (Ludox)** | Charged colloid | Electrostatic + steric | Gel/glass transition | Dozier et al. 1987; Phalakornkul et al. 1996 | **High** |
| 4 | **PEG-water solutions** | Polymer | Excluded volume + entanglement | Vitrification ~60 wt% | Vergara et al. 2001; Price et al. 2003 | Medium |
| 5 | **Dextran solutions** | Polysaccharide | Hydrodynamic drag + crowding | ~50 wt% (viscosity divergence) | Weast (CRC tables); Ribeiro et al. 2006 | Medium |
| 6 | **Ionic liquid mixtures** (e.g., [BMIM][BF4] in water) | IL + solvent | Electrostatic + solvation | Phase separation boundary | Noda et al. 2001; Tokuda et al. 2005 | Medium |
| 7 | **Casein micelles in milk** | Biological colloid | Depletion + steric | Random packing of micelles ~0.78 | Alexander et al. 2002; Dahbi et al. 2010 | Medium |
| 8 | **Polystyrene latex in water** | Charged colloid | DLVO + Brownian | Glass transition φ ≈ 0.58 | Pusey & van Megen 1987; Banchio et al. 2008 | Lower |
| 9 | **Glycerol-water mixtures** | Small molecule | Hydrogen bonding | Pure glycerol (100 wt%) | D'Errico et al. 2004; He et al. 2006 | Lower |
| 10 | **Haemoglobin solutions** | Protein | Crowding + oxygen binding | ~35 g/dL (intracellular) | Riveros-Moreno & Wittenberg 1972; Lavalette et al. 1999 | Lower |

**Rationale for top 3:**
- **Lysozyme** is the best-studied globular protein after BSA; extensive $D(c)$ data exists from multiple labs; the gelation boundary is well-characterised.
- **PMMA colloids** are the gold standard for hard-sphere physics; $D(c)$ is measured to very high precision; direct comparison with the existing hard-sphere colloidal dataset (Material 1) tests inter-lab reproducibility.
- **Silica Ludox** is a charged colloidal system, testing whether electrostatic interactions change β or leave it near 2.

---

# 3. Data Requirements

For each new material, the following data must be acquired or extracted from published sources:

## 3.1 Minimum Required Data

| Data item | Format | Units | Notes |
|-----------|--------|-------|-------|
| Concentration series | $c_1, c_2, \ldots, c_n$ ($n \geq 5$) | mol/L, g/dL, wt%, or volume fraction $\phi$ | Must span at least $c/c_{\max} \in [0.1, 0.8]$ |
| Diffusion coefficients | $D(c_1), D(c_2), \ldots, D(c_n)$ | m²/s or cm²/s | From DLS, NMR, FRAP, or interferometry |
| Uncertainties | $\sigma_D(c_i)$ | Same as $D$ | From published error bars or repeated measurements |
| Maximum concentration | $c_{\max}$ or $\phi_{\max}$ | Same as $c$ | From glass transition, gelation, crystallisation, or viscosity divergence |
| Temperature | $T$ | K or °C | Must be constant across the $c$-series |
| Solvent | Identity | — | Water, organic, ionic liquid, etc. |
| Measurement technique | DLS / NMR / FRAP / interferometry | — | Affects systematic uncertainty |

## 3.2 Optional (for Front-Propagation Analysis)

| Data item | Format | Notes |
|-----------|--------|-------|
| Spatial profiles $c(x,t)$ | 1D or radial, at multiple times | From gradient diffusion cells, FRAP recovery curves, or microfluidic channels |
| Time stamps | $t_1, t_2, \ldots$ | Uniform spacing preferred |
| Imaging resolution | $\Delta x$ in µm | Determines minimum resolvable front width |
| Geometry | Planar / cylindrical / spherical | Determines the effective $d$ for $\alpha_R$ |

## 3.3 Preprocessing Requirements

| Step | Description | When needed |
|------|-------------|-------------|
| Unit conversion | Convert all concentrations to a common scale (volume fraction $\phi$ or mass fraction $w$) | Always |
| $c_{\max}$ identification | Determine from phase diagram, rheology, or literature | Always |
| Baseline subtraction | Remove solvent self-diffusion $D_0$ if measuring mutual diffusion | If $D(c)$ includes solvent contribution |
| Outlier removal | Remove points with $R^2 < 0.9$ or $\sigma_D / D > 0.3$ | If data quality is uneven |
| Interpolation | Fill gaps in the $c$-series using spline or linear interpolation | Only if gaps > 20% of the range |

---

# 4. ED-Data Series Format

Each new material produces an **ED-Data package** — a self-contained directory with standardised structure.

```
ED-Data-{NN}_{MaterialName}/
├── data/
│   ├── raw_Dc.csv              # Columns: c, D, sigma_D, units
│   ├── profiles/               # (optional) c(x,t) spatial profiles
│   └── metadata.json           # Temperature, solvent, technique, source
├── processed/
│   ├── Dc_normalised.csv       # phi, D/D0, (1 - phi/phi_max)^beta
│   ├── beta_fit.json           # {beta, R2, M0, phi_max, method, ...}
│   └── front_positions.json    # (optional) {times, R(t), alpha_R_fit}
├── plots/
│   ├── Dc_vs_phi.png           # D(c) data with ED fit
│   ├── loglog_mobility.png     # log(D/D0) vs log(1 - phi/phi_max)
│   ├── front_propagation.png   # (optional) R(t) vs t
│   └── residuals.png           # Fit residuals
├── README.md                   # Material description, data source, results
└── result_summary.json         # {material, beta, R2, alpha_R, universality_class}
```

### Naming Convention

- `ED-Data-12_Lysozyme/` (continuing from ED-Data-11)
- `ED-Data-13_PMMA_Colloids/`
- `ED-Data-14_Silica_Ludox/`
- etc.

### The `beta_fit.json` Schema

```json
{
    "material": "Lysozyme",
    "beta": 2.05,
    "beta_uncertainty": 0.15,
    "R_squared": 0.992,
    "M0": 1.23e-11,
    "phi_max": 0.52,
    "phi_range": [0.05, 0.45],
    "n_points": 8,
    "method": "least_squares_loglog",
    "temperature_K": 298,
    "solvent": "25 mM NaCl buffer",
    "data_source": "Muschol & Rosenberger 1997, Table 2",
    "notes": "phi_max from crystal solubility at T=298K"
}
```

---

# 5. Pipeline for Each Material

## 5.1 Step 1: Data Import

1. Locate published $D(c)$ data (table or figure extraction).
2. Enter into `data/raw_Dc.csv` with columns: `c, D, sigma_D, c_unit, D_unit`.
3. Enter metadata into `data/metadata.json`.

## 5.2 Step 2: Normalisation

1. Convert concentration to volume fraction: $\phi = c \cdot v_{\text{mol}}$ (or use published $\phi$ directly).
2. Identify $\phi_{\max}$ from the phase diagram or published value.
3. Compute the ED variable: $\delta = 1 - \phi/\phi_{\max}$.
4. Normalise diffusion: $D_{\text{norm}} = D / D_0$ where $D_0 = D(\phi \to 0)$.
5. Save to `processed/Dc_normalised.csv`.

## 5.3 Step 3: β Fitting

The ED mobility law predicts:

$$D(\phi) = D_0 \cdot M_0 \left(1 - \frac{\phi}{\phi_{\max}}\right)^\beta$$

In log-log form:

$$\log(D/D_0) = \log(M_0) + \beta \cdot \log(1 - \phi/\phi_{\max})$$

1. Perform linear regression of $\log(D/D_0)$ vs. $\log(1 - \phi/\phi_{\max})$.
2. Extract slope = β, intercept = log(M₀), $R^2$.
3. Estimate uncertainty via bootstrap (resample with replacement, 1000 iterations).
4. Save to `processed/beta_fit.json`.

**Quality thresholds:**
- $R^2 > 0.95$: strong fit (β is reliable)
- $0.90 < R^2 < 0.95$: moderate fit (β is indicative)
- $R^2 < 0.90$: weak fit (material may not belong to ED universality class)

## 5.4 Step 4: Universality Check

1. Compare fitted β to the universality band: $\beta = 2.0 \pm 1.0$ (wide) or $\beta = 2.0 \pm 0.5$ (narrow).
2. Compute the predicted front exponent: $\alpha_R = 1/(d\beta + 2)$ for $d = 3$.
3. If front-propagation data is available, extract measured $\alpha_R$ and compare.
4. Plot the material on the universality map (β vs. α_R) alongside the existing three materials.

## 5.5 Step 5: Reporting

1. Generate plots: $D(\phi)$ with fit, log-log mobility, residuals, (optional) front propagation.
2. Write `README.md` with material description, data source, key results, and assessment.
3. Produce `result_summary.json` with the final β, R², and universality verdict.

---

# 6. Success Criteria

## 6.1 Per-Material Criteria

A material **passes** the ED universality test if:

| Criterion | Threshold | Rationale |
|-----------|-----------|-----------|
| U1: $R^2 > 0.95$ | Strong power-law fit | The mobility law must actually describe the data |
| U2: $\beta \in [1.0, 3.5]$ | Within the broad universality band | The exponent must be in the PME range |
| U3: $\beta \in [1.5, 2.5]$ | Within the narrow universality band | Consistent with $\beta \approx 2$ |
| U4: $\alpha_R$ matches $1/(d\beta + 2)$ within 20% | Front exponent consistent with theory | Only if front data available |
| U5: No systematic residual pattern | Random residuals in log-log fit | Rules out more complex functional forms |

**Classification:**

| Outcome | Criteria met | Interpretation |
|---------|-------------|----------------|
| **Confirmed** | U1 + U2 + U3 + U5 | Material belongs to ED universality class |
| **Consistent** | U1 + U2 + U5 (but U3 fails) | Material has ED-like mobility but β ≠ 2 |
| **Excluded** | U1 fails or U2 fails | Material does not follow the ED mobility law |
| **Boundary** | U1 marginal (0.90–0.95) | Inconclusive; needs higher-quality data |

## 6.2 Programme-Level Criteria

| Criterion | Target | Current (3 materials) |
|-----------|--------|----------------------|
| Number of "Confirmed" materials | ≥ 5 | 3 |
| Mean β | 2.0 ± 0.3 | 2.10 ± 0.40 |
| β standard deviation | < 0.3 | 0.40 |
| Number of distinct physical mechanisms | ≥ 4 | 3 (excluded volume, hydrogen bonding, crowding) |
| At least one measured $\alpha_R$ | Yes | No (designed but not executed) |

---

# 7. Roadmap for ED-Data-05 and ED-Data-06

## 7.1 ED-Data-05: First Expansion (3 New Materials)

**Target materials:** Lysozyme, PMMA colloids, silica Ludox (the top-3 priority candidates).

**Tasks:**
1. Extract $D(\phi)$ data from published sources for all three materials.
2. Run the β-fitting pipeline for each.
3. Plot all six materials on the universality map.
4. Produce three ED-Data packages (ED-Data-12, 13, 14).

**Success criterion:** At least 2 of 3 new materials classified as "Confirmed" (U1+U2+U3+U5).

**Estimated effort:** 1–2 sessions (data extraction + fitting + reporting).

## 7.2 ED-Data-06: Universality Synthesis

**Target:** Comprehensive synthesis across all 6–10 materials.

**Tasks:**
1. If ED-Data-05 succeeds with ≥ 2 materials: expand to 3–4 more candidates from the list (PEG, dextran, casein, glycerol).
2. Recompute the universality statistics: mean β, standard deviation, confidence interval.
3. Test whether β = 2.0 is within the 95% confidence interval of the cross-material mean.
4. Produce a publication-quality universality plot with error bars.
5. Write ED-Data-15: updated universality map note (superseding ED-Data-11).

**Success criterion:** β = 2.0 within the 95% CI of the cross-material mean with $n \geq 6$ materials.

**The deliverable:** A single figure — the universality map with 6–10 materials plotted on the theoretical curve $\alpha_R = 1/(3\beta + 2)$ — that either confirms or falsifies the ED mobility law as a universal description of concentration-dependent diffusion.

## 7.3 Timeline

| Module | Materials | Depends on | Est. sessions |
|--------|-----------|------------|---------------|
| ED-Data-05 | Lysozyme, PMMA, silica | Published data availability | 1–2 |
| ED-Data-06 | +3–4 from candidate list | ED-Data-05 results | 2–3 |
| ED-Data-15 | Universality synthesis note | ED-Data-06 complete | 1 |

---

*ED-Data-04 · Event Density Research Programme · March 2026*
