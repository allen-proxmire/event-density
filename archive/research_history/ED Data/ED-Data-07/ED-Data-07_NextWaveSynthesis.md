# ED-Data-07: Next Wave Synthesis — 10 Materials

**Author:** Allen Proxmire
**Series:** ED-Data-07
**Date:** March 2026
**Status:** Complete — four new materials processed, universality analysis updated

---

## 1. New Materials

Four additional materials were processed through the ED-Data pipeline:

| # | Material | Mechanism | $\beta$ | $\pm$ | $R^2$ | Verdict |
|---|----------|-----------|---------|-------|-------|---------|
| 7 | PEG-water (6 kDa) | Polymer excluded volume | 1.297 | 0.054 | 0.996 | Consistent |
| 8 | Dextran (70 kDa) | Polysaccharide crowding | 1.464 | 0.081 | 0.993 | Consistent |
| 9 | Casein micelles | Biological colloid | 1.794 | 0.055 | 0.998 | **Confirmed** |
| 10 | Glycerol-water | Small molecule H-bonding | 1.741 | 0.034 | 0.999 | **Confirmed** |

All four materials show excellent fits ($R^2 > 0.99$). Two are Confirmed (casein, glycerol) with $\beta \in [1.5, 2.5]$; two are Consistent (PEG, dextran) with $\beta$ just below 1.5. Zero are Excluded.

---

## 2. Updated 10-Material Dataset

| # | Material | Type | $\beta$ | $R^2$ | Verdict |
|---|----------|------|---------|-------|---------|
| 1 | Hard-sphere colloids | Colloid | 1.690 | 0.995 | Confirmed |
| 2 | Sucrose-water | Molecular | 2.490 | 0.987 | Confirmed |
| 3 | BSA protein | Protein | 2.120 | 0.986 | Confirmed |
| 4 | Lysozyme | Protein | 1.360 | 0.998 | Consistent |
| 5 | PMMA colloids | Colloid | 1.813 | 0.994 | Confirmed |
| 6 | Ludox silica | Charged colloid | 1.407 | 0.999 | Consistent |
| 7 | PEG-water | Polymer | 1.297 | 0.996 | Consistent |
| 8 | Dextran | Polysaccharide | 1.464 | 0.993 | Consistent |
| 9 | Casein micelles | Bio-colloid | 1.794 | 0.998 | Confirmed |
| 10 | Glycerol-water | Small molecule | 1.741 | 0.999 | Confirmed |

The dataset now spans 8 distinct physical mechanisms across colloids, proteins, polymers, polysaccharides, and small molecules.

---

## 3. Combined Statistics

| Statistic | 6 materials (ED-Data-06) | 10 materials (ED-Data-07) |
|-----------|-------------------------|--------------------------|
| Mean $\beta$ | 1.813 | **1.718** |
| Std $\beta$ | 0.433 | **0.371** |
| 95% CI | [1.359, 2.268] | **[1.452, 1.983]** |
| $\beta = 2.0$ in CI? | Yes | **No** |
| Range | [1.36, 2.49] | [1.30, 2.49] |
| Confirmed | 4/6 | 6/10 |
| Consistent | 2/6 | 4/10 |
| Excluded | 0/6 | 0/10 |

---

## 4. The Verdict on $\beta = 2$

**The canonical value $\beta = 2.0$ falls *outside* the 95% CI at $n = 10$.**

This is the most important result of ED-Data-07. At 6 materials, the CI was wide enough to include 2.0. At 10 materials, the standard error has narrowed sufficiently ($\text{SE} = 0.117$) that the CI upper bound (1.983) sits just below 2.0.

**What this means:**

- The ED mobility law $D \propto (1 - \phi/\phi_{\max})^\beta$ is confirmed as a universal functional form — all 10 materials fit it with $R^2 > 0.98$.
- The exponent $\beta$ is **not** exactly 2.0. The best estimate from 10 materials is $\beta \approx 1.7 \pm 0.4$.
- The original ED-Data-11 estimate ($\beta = 2.10 \pm 0.40$, from 3 materials) was biased upward by the sucrose outlier ($\beta = 2.49$). More data has corrected this.
- The canonical ED value $\beta = 2$ is within the 99% CI ($[1.10, 2.53]$) but not the 95% CI. It is a reasonable approximation but not exact.

**For the ED architecture, this changes nothing operationally.** ED-Phys-06 confirmed that the PDE's behaviour is qualitatively identical across $\beta \in [0.5, 5.0]$. Whether the true universal exponent is 1.7 or 2.0 affects quantitative predictions (front speed, relaxation timescale) but not the structural laws (compact support, similarity collapse, attractor convergence).

---

## 5. Patterns in the Data

### 5.1 Mechanism Dependence

| Mechanism cluster | Materials | Mean $\beta$ |
|-------------------|-----------|--------------|
| Hard-sphere / steric | Hard-sphere, PMMA, Casein | 1.76 |
| Electrostatic / charged | Ludox, Lysozyme | 1.38 |
| Molecular / H-bonding | Sucrose, Glycerol | 2.12 |
| Polymer / crowding | BSA, PEG, Dextran | 1.63 |

There is a tentative pattern: **molecular (H-bonding) systems have higher $\beta$ (~2.1), while charged and polymer systems have lower $\beta$ (~1.4).** Hard-sphere systems sit in between (~1.8). If this pattern holds with more data, the universality class may split into sub-classes by interaction type, each with a characteristic $\beta$ range.

### 5.2 Fit Quality Is Universal

All 10 materials have $R^2 > 0.986$. The power-law mobility form is not just a good fit — it is an excellent fit across every system tested. This is the strongest empirical result: the *form* is universal even if the *exponent* varies.

---

## 6. What Should Be Tested Next

1. **More H-bonding systems** (e.g., trehalose, ethanol-water) to confirm whether $\beta \approx 2$ is specific to this mechanism.
2. **A charged polymer** (e.g., polyelectrolyte, DNA) to test whether the electrostatic sub-class ($\beta \approx 1.4$) extends to flexible chains.
3. **A granular system** (e.g., glass beads in viscous fluid) to test whether the mobility law applies beyond Brownian dynamics.
4. **Direct $\alpha_R$ measurement** in any one of the 10 materials — the most informative single experiment, still unexecuted.

---

## Data Products

```
outputs/ED-Data-07/
  peg_water/       (raw_data.json, beta_fit.json, P1-P3)
  dextran/         (raw_data.json, beta_fit.json, P1-P3)
  casein_micelles/ (raw_data.json, beta_fit.json, P1-P3)
  glycerol_water/  (raw_data.json, beta_fit.json, P1-P3)
  plots/           (universality_map_10.png, beta_all_10.png, beta_distribution_10.png)
  tables/          (S1, S2, S3)
  summary/         (final_summary.json)
```

---

*ED-Data-07 · Event Density Research Programme · March 2026*
