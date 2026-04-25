# ED-Phys-05: Parameter Sweeps and Phase Diagrams

## Canonical Lineage

| Source | Role |
|--------|------|
| ED-Phys-01 | Update rule and PDE defining the parameter space |
| ED-Phys-02 | Simulator executing all 135 runs |
| ED-Phys-03 | Baseline measurements (lambda_1, lambda_2) for reference |
| ED-Phys-04 | Physical-analogue mappings used to interpret regimes |
| ED-12 | Epoch predictions: inflation, structure formation, thinning, heat death |

---

## 1. Parameter Space Definition

### 1.1 Sweep Dimensions

| # | Parameter | Symbol | Range | Resolution | ED-Phys-04 Analogue |
|---|-----------|--------|-------|-----------|-------------------|
| 1 | Concavity exponent | gamma_exp | 0.1 - 0.9 | 9 values | Controls structure formation instability |
| 2 | Relational coupling | alpha | 0.1 - 2.0 | 10 values | Gravitational instability strength |
| 3 | Mobility exponent | n_mob | 1 - 6 | 6 values | Horizon sharpness (saturation steepness) |
| 4 | Bare mobility | M_0 | 0.1 - 1.0 | 5 values | Inflation rate (diffusion speed) |
| 5 | IC mode | — | 3 classes | 3 values | Initial universe topology |

### 1.2 Justification for Each Dimension

**gamma_exp (0.1 - 0.9):** ED-Phys-04 identifies the concave exponent as the control parameter for structure formation. At gamma_exp -> 0, f(rho) = rho^gamma_exp -> 1 (constant penalty, no instability). At gamma_exp -> 1, f(rho) -> rho (linear, no concavity). The interesting physics lives in (0, 1).

**alpha (0.1 - 2.0):** The ratio alpha/M_0 determines whether structure formation (relational penalty) or smoothing (diffusion) dominates. At alpha >> M_0, structures form immediately. At alpha << M_0, everything diffuses away.

**n_mob (1 - 6):** Controls how sharply mobility drops near rho_max. n_mob = 1 gives a linear cutoff; n_mob = 6 gives a very sharp horizon transition. This affects whether horizons are "soft" or "hard."

**M_0 (0.1 - 1.0):** Sets the absolute scale of diffusion (inflation rate). Higher M_0 = faster inflation.

**IC mode:** Three qualitatively different initial conditions test robustness of the cosmological timeline.

### 1.3 Fixed Parameters

| Parameter | Value | Justification |
|-----------|-------|--------------|
| rho_max | 100.0 | Horizon scale (fixed reference) |
| gamma_b | 0.0 | Boundary penalty off (periodic BCs) |
| dx | 1.0 | Normalized grid spacing |
| N | 256 | 1D lattice, sufficient for gradient resolution |
| n_steps | 20,000 | ~1 e-folding time for default parameters |
| cfl_safety | 0.4 | Aggressive but stable |
| rho_mean | 50.0 | Mid-range (rho_max/2) |
| noise_amplitude | 0.5 | ~1% of rho_mean |
| seed | 42 | Reproducibility |

---

## 2. Sweep Methodology

**Total runs:** 90 (sweep 1) + 30 (sweep 2) + 15 (sweep 3) = **135 simulations**

**Per-run extraction:**
- Inflation rate lambda_1 (exponential fit to log(grad_mean) vs t)
- Fit quality R^2
- Thinning coefficient lambda_2
- Basin count trajectory (initial, final, max, grew?)
- Equation of state w_eff (ED-Phys-04 Section 13.2)
- Horizon candidate fraction
- Curvature statistics (Laplacian mean, std, positive fraction)
- Phase sequence identification

**Runtime:** ~310 seconds total (2.3 seconds per run average).

---

## 3. Sweep 1: gamma_exp x alpha — The Primary Phase Diagram

### 3.1 Inflation Rate lambda_1

```
                    alpha
gamma   0.1   0.2   0.4   0.6   0.8   1.0   1.2   1.4   1.7   2.0
 0.1   0.44  0.44  0.44  0.44  0.44  0.44  0.44  0.44  0.44  0.44
 0.2   0.44  0.44  0.44  0.44  0.44  0.44  0.44  0.44  0.44  0.44
 0.3   0.44  0.44  0.44  0.44  0.44  0.44  0.44  0.44  0.44  0.44
 0.4   0.43  0.43  0.44  0.44  0.44  0.44  0.44  0.44  0.44  0.44
 0.5   0.37  0.40  0.42  0.42  0.43  0.43  0.43  0.43  0.43  0.43
 0.6   0.13  0.22  0.30  0.34  0.37  0.38  0.39  0.40  0.40  0.41
 0.7   0.02  0.04  0.08  0.10  0.13  0.15  0.17  0.19  0.22  0.24
 0.8   0.00  0.01  0.01  0.02  0.02  0.03  0.03  0.04  0.05  0.06
 0.9   0.01  0.02  0.03  0.04  0.05  0.06  0.06  0.07  0.08  0.09
```

**Key finding:** There is a sharp **inflation cliff** between gamma_exp = 0.5 and gamma_exp = 0.7. Below gamma_exp ~ 0.5, inflation is fast and nearly independent of alpha (lambda_1 ~ 0.44). Above gamma_exp ~ 0.7, inflation is strongly suppressed (lambda_1 < 0.1). The relational penalty term alpha * gamma_exp * rho^(gamma_exp-1) becomes strong enough at high gamma_exp to compete with diffusion, disrupting the clean exponential decay.

### 3.2 Equation of State w_eff

```
                    alpha
gamma   0.1    0.2    0.4    0.6    0.8    1.0    1.2    1.4    1.7    2.0
 0.1   -1.00  -1.00  -1.00  -1.00  -1.00  -1.00  -1.00  -1.00  -1.00  -1.00
 0.2   -1.00  -1.00  -1.00  -1.00  -1.00  -1.00  -1.00  -1.00  -1.00  -1.00
 0.3   -1.00  -1.00  -1.00  -1.00  -1.00  -1.00  -1.00  -1.00  -1.00  -1.00
 0.4   -1.00  -1.00  -1.00  -1.00  -1.00  -1.00  -1.00  -1.00  -1.00  -1.00
 0.5   -1.00  -1.00  -1.00  -1.00  -1.00  -1.00  -1.00  -1.00  -1.00  -1.00
 0.6   -0.99  -0.99  -1.00  -1.00  -1.00  -1.00  -1.00  -1.00  -1.00  -0.99
 0.7   +4.2   +0.6   -0.5   -0.7   -0.8   -0.8   -0.9   -0.9   -0.9   -0.9
 0.8   >100   >100   >100   >100   >100   >100   >100   >100   >100   >100
 0.9   >100   >100   >100   >100   >100   >100   >100   >100   >100   >100
```

**Key finding:** The equation of state exhibits three distinct regimes:

1. **De Sitter regime (w ~ -1):** gamma_exp <= 0.6, all alpha. Pure inflationary behavior. This is the "physical" cosmological regime.

2. **Transition regime (w between -1 and +1):** gamma_exp ~ 0.7, moderate-to-high alpha. The relational penalty is strong enough to partially break de Sitter behavior. At gamma_exp = 0.7, alpha = 0.4, w = -0.45 — resembling a quintessence-like equation of state.

3. **Stiff regime (w >> 1):** gamma_exp >= 0.8. The relational penalty dominates, driving rapid density drain that far exceeds the expansion rate. This is an unphysical regime where the concave penalty overwhelms diffusion.

### 3.3 Basin Loss (Structure Activity)

```
                    alpha
gamma   0.1   0.2   0.4   0.6   0.8   1.0   1.2   1.4   1.7   2.0
 0.1      0     0     0     0     0     0     0     0     0     0
 0.2      0     0     0     0     0     0     0     0     0     0
 0.3      0     0     0     0     0     0     0     0     0     0
 0.4      1     1     0     0     0     0     0     0     0     0
 0.5     22    11     3     2     1     1     1     1     1     0
 0.6     62    53    42    35    22    20    16    13    10     7
 0.7     76    71    68    64    64    62    59    57    54    51
 0.8     80    80    79    79    78    78    78    77    76    76
 0.9     80    80    81    82    82    82    82    82    82    82
```

**Key finding:** Basin loss shows a **structure-activity gradient** running from top-left (no activity) to bottom-left (total basin annihilation):

- **gamma_exp <= 0.4:** No basin loss. Diffusion dominates; the landscape is too smooth for structural dynamics.
- **gamma_exp = 0.5, low alpha:** Moderate basin loss (22/82). The sweet spot for cosmological structure dynamics.
- **gamma_exp = 0.6-0.7:** Heavy basin loss (50-76/82). The relational penalty is strong enough to rapidly merge structures.
- **gamma_exp >= 0.8:** Near-total basin annihilation (76-82/82). The concave penalty is so strong it destroys all spatial structure, leaving a nearly uniform field.

**The alpha effect is inverse:** Higher alpha *reduces* basin loss at fixed gamma_exp >= 0.5. This is counterintuitive — stronger relational penalty preserves structures rather than destroying them. The mechanism: at high alpha, the concave saturation stabilizes existing structures before they can merge, because the penalty cost of disrupting a stable peak is too high.

### 3.4 Identified Regimes

From the combined data, five distinct regimes emerge in the (gamma_exp, alpha) plane:

| Regime | gamma_exp | alpha | lambda_1 | w_eff | Basin loss | Character |
|--------|-----------|-------|----------|-------|-----------|-----------|
| **I. Fast Inflation** | 0.1 - 0.4 | any | > 0.43 | -1.000 | 0 | Clean de Sitter; no structure activity |
| **II. Cosmological** | 0.5 - 0.6 | 0.1 - 0.4 | 0.13 - 0.42 | -0.99 to -1.00 | 3 - 62 | Inflation + structure merging; the "physical" zone |
| **III. Stiff Inflation** | 0.5 - 0.6 | 0.6 - 2.0 | 0.34 - 0.44 | -0.99 to -1.00 | 1 - 35 | Inflation with structure stabilization |
| **IV. Marginal** | 0.7 | any | 0.02 - 0.24 | -0.9 to +4.2 | 51 - 76 | Slow inflation; heavy basin loss; w crosses 0 |
| **V. Penalty-Dominated** | 0.8 - 0.9 | any | < 0.06 | >> 1 | 76 - 82 | No meaningful inflation; total structure destruction |

---

## 4. Sweep 2: n_mob x M_0 — Mobility Structure

### 4.1 lambda_1 Grid

```
              M_0
n_mob   0.10   0.25   0.50   0.75   1.00
  1    0.084  0.202  0.369  0.503  0.611
  2    0.043  0.105  0.202  0.290  0.368
  3    0.022  0.053  0.105  0.154  0.202
  4    0.011  0.027  0.053  0.079  0.104
  5    0.005  0.014  0.027  0.040  0.053
  6    0.003  0.007  0.014  0.020  0.027
```

### 4.2 Scaling Law Discovery

**lambda_1 scales linearly with effective mobility M_eff = M_0 * (1 - rho/rho_max)^n_mob:**

At rho = 50, rho_max = 100: M_eff = M_0 * (0.5)^n_mob

The ratio lambda_1 / M_eff is remarkably constant:

| n_mob | lambda_1/M_eff (avg across M_0) |
|-------|-------------------------------|
| 1 | 1.47 |
| 2 | 1.60 |
| 3 | 1.67 |
| 4 | 1.68 |
| 5 | 1.72 |
| 6 | 1.72 |

**Scaling law:**
```
lambda_1 = C * M_eff = C * M_0 * (1 - rho_mean/rho_max)^n_mob
```
where C ~ 1.5-1.7 is a geometric factor depending on the lattice coordination number and gradient field structure.

This confirms ED-12's prediction that the inflation rate is set by the effective mobility at the mean density. The constant C encodes the efficiency of gradient smoothing on a 1D lattice with periodic BCs and random initial gradients.

### 4.3 Implications

- **n_mob controls inflation speed:** Doubling n_mob roughly halves lambda_1 (since M_eff halves at rho = rho_max/2).
- **M_0 is a direct scaling factor:** lambda_1 is proportional to M_0.
- **The mobility exponent does not change the qualitative dynamics** — only the rate. All (n_mob, M_0) combinations produce the same phase sequence; they simply run at different speeds.
- **Horizon sharpness (high n_mob) comes at the cost of slower dynamics** in the bulk.

---

## 5. Sweep 3: Initial Condition Sensitivity

### 5.1 Results Table

| IC Mode | alpha | lambda_1 | basins (i->f) | w_eff | Phases |
|---------|-------|----------|--------------|-------|--------|
| uniform_noise | 0.1 | 0.368 | 82->60 | -1.000 | transition -> inflation |
| uniform_noise | 0.3 | 0.414 | 82->77 | -1.000 | transition -> inflation |
| uniform_noise | 1.0 | 0.427 | 82->81 | -0.999 | transition -> thinning |
| uniform_noise | 2.0 | 0.431 | 82->82 | -0.998 | transition -> thinning |
| localized_gradient | 0.1 | 0.000 | 0->0 | -0.870 | transition -> thinning |
| localized_gradient | 0.5 | 0.000 | 0->0 | +0.747 | transition -> thinning |
| localized_gradient | 2.0 | -0.001 | 0->0 | nan | transition -> thinning |
| random | 0.1 | 0.301 | 82->60 | -1.031 | transition -> inflation |
| random | 1.0 | 0.423 | 82->81 | -1.033 | transition |
| random | 2.0 | 0.439 | 82->81 | -1.032 | transition |

### 5.2 Key Findings

**uniform_noise vs random:** Nearly identical behavior. Both produce inflation with lambda_1 ~ 0.37-0.43 and w_eff ~ -1.00. The random IC mode (larger perturbations) has slightly lower lambda_1 at low alpha because larger gradients take longer to smooth. This confirms the cosmological timeline is **robust to IC details** when the initial state is approximately homogeneous.

**localized_gradient:** Fundamentally different behavior — no inflation detected (lambda_1 ~ 0). The single Gaussian bump creates a stable structure that persists indefinitely. The system goes directly to thinning without passing through inflation. This is because:
1. The bump is a single coherent structure, not a random gradient field
2. The concave penalty stabilizes it against diffusion
3. There is no "inflation" because the gradient field doesn't decay exponentially — it's maintained by the structure

**Physical interpretation:** The localized gradient IC corresponds to a pre-existing bound structure (like a galaxy or star). It skips inflation and goes directly to the structure persistence + thinning phase. This is consistent with the ED picture: inflation smooths random gradients, but coherent structures resist smoothing.

---

## 6. Phase Diagrams

### 6.1 Primary Phase Diagram: gamma_exp vs alpha

```
     alpha ->  0.1  0.2  0.4  0.6  0.8  1.0  1.2  1.4  1.7  2.0
gamma_exp
   0.1-0.4    [=================== FAST INFLATION ====================]
              w = -1.000, lambda_1 > 0.43, no basin loss

   0.5        [COSMO][ C ][ STIFF INFLATION                           ]
              w~-1, L1=0.37-0.43, basin loss 22->0

   0.6        [COSMO][ COSMOLOGICAL     ][   STIFF INFLATION          ]
              w~-1, L1=0.13-0.41, basin loss 62->7

   0.7        [MARGINAL .... w crosses 0 .... approaching w<-1        ]
              L1=0.02-0.24, basin loss 76->51

   0.8-0.9    [========== PENALTY-DOMINATED (UNPHYSICAL) =============]
              w >> 1, L1 < 0.1, near-total basin destruction
```

### 6.2 Mobility Phase Diagram: n_mob vs M_0

```
     M_0 ->   0.10   0.25   0.50   0.75   1.00
n_mob
   1          [  +  ][  ++  ][ +++ ][ +++ ][ +++ ]
   2          [  .  ][  +   ][  ++ ][ ++  ][ +++ ]
   3          [  .  ][  .   ][  +  ][  +  ][  ++ ]
   4          [  .  ][  .   ][  .  ][  .  ][  +  ]
   5          [  -  ][  .   ][  .  ][  .  ][  .  ]
   6          [  -  ][  -   ][  .  ][  .  ][  .  ]

Key: +++ = fast inflation (L1 > 0.3)
      ++ = moderate inflation (0.1 < L1 < 0.3)
       + = slow inflation (0.05 < L1 < 0.1)
       . = marginal (0.01 < L1 < 0.05)
       - = negligible (L1 < 0.01)

All points: w ~ -1.00, R^2 > 0.99
Scaling: lambda_1 ~ 1.6 * M_0 * (0.5)^n_mob
```

### 6.3 Regime Boundary Summary

| Boundary | Location | Physical Meaning |
|----------|----------|-----------------|
| Inflation cliff | gamma_exp ~ 0.6-0.7 | Relational penalty overcomes diffusion |
| De Sitter boundary | gamma_exp ~ 0.65 (w = -1 to w = 0) | Transition from inflation-dominated to penalty-dominated |
| Structure activity onset | gamma_exp ~ 0.45 | Basin dynamics become significant |
| Total basin destruction | gamma_exp ~ 0.85 | Concave penalty destroys all spatial structure |
| Mobility scaling | lambda_1 proportional to M_eff | Universal across all (n_mob, M_0) |

---

## 7. Interpretation Using ED-Phys-04 Analogues

### 7.1 The "Physical" Region

The cosmologically realistic region of parameter space is:

```
gamma_exp = 0.5 - 0.6
alpha = 0.1 - 0.4
```

In this region:
- **w_eff = -1.00** (de Sitter inflation, matching standard cosmology)
- **lambda_1 = 0.13 - 0.42** (meaningful but not overwhelming inflation)
- **Basin loss = 3 - 62** (active structure dynamics without total destruction)
- **Exponential fit R^2 > 0.92** (clean inflationary behavior)

This is where ED produces physics most resembling our universe.

### 7.2 The gamma_exp = 0.7 Transition

At gamma_exp = 0.7, the equation of state passes through zero:
- alpha = 0.1: w = +4.2 (stiff, radiation-like)
- alpha = 0.4: w = -0.45 (quintessence-like)
- alpha = 2.0: w = -0.92 (approaching de Sitter)

This suggests that **gamma_exp ~ 0.7 is where matter-radiation-like behavior emerges**. The relational penalty is strong enough to create a positive-pressure component competing with the negative-pressure inflation. If our universe's equation of state evolved from w = -1 (inflation) through w = 0 (matter/radiation era) to w ~ -1 again (dark energy), then the ED framework may need a time-varying effective gamma_exp — or the transition may emerge naturally from rho decreasing over time (which changes the relative strength of the penalty terms).

### 7.3 The Scaling Law and Emergent Constants

The discovery that lambda_1 = C * M_eff with C ~ 1.6 is significant:
- C is a **geometric constant** of the lattice (coordination number, gradient field statistics)
- M_eff = M_0 * (1 - rho/rho_max)^n_mob is the **physical mobility** at the current density
- The inflation rate is therefore fully determined by the local physics — no free parameters

This is the ED analogue of determining the Hubble parameter from the energy content of the universe.

### 7.4 Physical vs Non-Physical Regions

| Region | Physical Status | Reasoning |
|--------|----------------|-----------|
| gamma_exp < 0.4 | Non-physical (too smooth) | No structure activity; universe remains featureless |
| gamma_exp = 0.5-0.6, alpha = 0.1-0.4 | **Physical** | Inflation + structure + thinning; w = -1 |
| gamma_exp = 0.5-0.6, alpha > 0.6 | Semi-physical | Inflation but structure frozen by strong penalty |
| gamma_exp = 0.7 | Transitional | w crosses 0; may encode matter/radiation era |
| gamma_exp > 0.8 | Non-physical (penalty-dominated) | Structures destroyed; w >> 1; no inflation |

---

## 8. The alpha Paradox: More Penalty Preserves More Structure

One of the most surprising findings: increasing alpha (the relational penalty coupling) *reduces* basin loss at gamma_exp >= 0.5. At gamma_exp = 0.6:
- alpha = 0.1: 62 basins lost (76% destruction)
- alpha = 2.0: 7 basins lost (9% destruction)

**Mechanism:** The concave penalty f(rho) = rho^gamma_exp has two effects:
1. **Destabilizing:** Amplifies perturbations (positive feedback for small overdensities)
2. **Stabilizing:** Saturates at high density (sublinear growth prevents runaway)

At low alpha, effect (1) dominates: perturbations grow and basins merge destructively. At high alpha, effect (2) dominates: existing structures are locked in place by the strong saturation, preventing merging. The transition occurs at alpha ~ 0.5 for gamma_exp = 0.6.

This is the ED analogue of **gravitational binding energy**: stronger gravity creates deeper potential wells that are harder to disrupt.

---

## 9. Data Files

| File | Contents |
|------|----------|
| `results/sweep1_gamma_alpha.csv` | 90 runs: gamma_exp x alpha grid |
| `results/sweep2_nmob_M0.csv` | 30 runs: n_mob x M_0 grid |
| `results/sweep3_ic_modes.csv` | 15 runs: IC mode x alpha grid |
| `phase_diagrams/pd1_gamma_alpha.json` | Phase diagram data: lambda_1, w_eff, basins grids |
| `phase_diagrams/pd2_nmob_M0.json` | Phase diagram data: lambda_1 grid |

---

## 10. Open Questions for ED-Phys-06

1. **Time-varying effective gamma_exp:** As rho decreases during thinning, the relative strength of the relational penalty changes. Does the effective gamma_exp shift dynamically, producing a w(t) that evolves from -1 to 0 to -1 (inflation -> matter -> dark energy)?

2. **Structure seeding at gamma_exp = 0.6, alpha = 0.1:** This is the most structurally active parameter point with realistic w. Can longer runs (200K+ steps) show new basin creation (not just merging)?

3. **The w = 0 crossing at gamma_exp = 0.7:** Does this transition have observable signatures in the gradient field topology? Are there emergent particle-like excitations at this crossing?

4. **IC dependence of the localized gradient:** The single bump is perfectly stable. What happens with two bumps at varying separations? Do they interact (gravitational-like attraction)?

5. **2D phase diagrams:** Do the regime boundaries shift in 2D? The lambda_1(2D)/lambda_1(1D) = 2.68 ratio from ED-Phys-03 suggests the scaling law C may be dimension-dependent.

6. **The scaling constant C ~ 1.6:** Can this be derived analytically from the Laplacian eigenspectrum of the periodic lattice and the initial gradient power spectrum?

7. **Horizon formation:** None of the 135 runs produced horizon candidates (rho near rho_max). Need dedicated runs with rho_mean = 80-95 to explore the saturation/horizon regime.
