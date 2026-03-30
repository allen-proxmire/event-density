# Results Overview

A summary of the ED programme's empirical results, from laboratory diffusion to galactic weak lensing.

---

## Condensed Matter

The ED mobility law D(c)/D₀ = (1 − c/c_max)^β was fitted to published diffusion data from three physically distinct materials.

| Material | Mechanism | β | R² |
|:---------|:----------|:--|:---|
| Hard-sphere colloids | Steric jamming | 1.60 | 0.9996 |
| Sucrose-water | H-bond viscosity | 2.19 | 0.994 |
| BSA protein solutions | Hydrodynamic crowding | 2.22 | 0.988 |
| **Mean** | — | **2.00 ± 0.29** | — |

The front-propagation exponent α_R = 1/(dβ + 2) was confirmed by simulation:

| Dimension | Quantity | Theory | Simulation | Error |
|:----------|:---------|:-------|:-----------|:------|
| 1D | α_R (colloids) | 0.271 | 0.265 | **2.3%** |
| 3D | α_ρ (colloids) | −0.4240 | −0.4241 | **0.02%** |

Compact support (sharp fronts, not Gaussian tails) was confirmed in every simulation.

**Details:** [ED-Data-01 through 11](research/ED%20PAPERS/)

---

## Dwarf Galaxy Halos

The ED PDE coupled to the Poisson equation (generalised mobility: α = 0.5, β = 2) produces density profiles matching Burkert to 99.6% for dwarf galaxies.

| Galaxy | ED core (kpc) | Burkert core (kpc) | Match |
|:-------|:-------------|:-------------------|:------|
| DDO 154 | 2.34 | 2.3 | 2% |
| IC 2574 | ~4–5 | 4.1 | ~10% |
| DDO 168 | ~2.0 | 1.9 | 5% |
| WLM | ~1.2 | 1.0 | 20% |

The core-widening mechanism — degenerate mobility suppressing transport at high density — is unique to ED.

**Details:** [ED-Data-Galaxy-03 through 06](research/ED%20PAPERS/)

---

## NGC 3198 (Spiral Galaxy)

The gravity-only ED model overshoots the flat rotation curve by ~30 km/s. Adding the temporal-tension channel (V_temp = 12.5 km/s) resolves this:

| Model | RMS (km/s) | Parameters |
|:------|:-----------|:-----------|
| Burkert (pure) | 1.9 | 2 |
| ED + temporal tension | 1.9 | 3 |
| ED gravity only | 23.8 | 3 |

**Details:** [ED-Data-Galaxy-07, 08](research/ED%20PAPERS/)

---

## Weak Lensing (Mistele et al. 2024)

At 100–1000 kpc projected radius:

| R (kpc) | Burkert (km/s) | NFW (km/s) | ED (km/s) | Observed |
|:--------|:---------------|:-----------|:----------|:---------|
| 100 | 73 | 179 | 134 | ~135 |
| 500 | 42 | 127 | 134 | ~137 |
| 1000 | 32 | 102 | 134 | ~136 |

ED predicts flat V; Burkert predicts V → 0; NFW predicts slow decline. The data are flat.

**Details:** [ED-Data-Galaxy-09, 10](research/ED%20PAPERS/)

---

## Baryonic Tully-Fisher Relation

| Model | Exponent n | RMS (km/s) |
|:------|:-----------|:-----------|
| ED / MOND (1/4) | 0.250 (fixed) | 5.9 |
| ΛCDM virial (1/3) | 0.333 (fixed) | 17.9 |
| Free fit | **0.246 ± 0.025** | 5.6 |

The free exponent matches 1/4 (< 0.2σ) and rejects 1/3 (> 3σ). The ED acceleration scale a_ED = 2.1 × 10⁻¹⁰ m/s² ≈ 1.8 a₀.

**Details:** [ED-Data-Galaxy-11](research/ED%20PAPERS/)

---

## ED-Unique Predictions

Two tests distinguish ED from both MOND and ΛCDM:

| Test | ED prediction | MOND | ΛCDM |
|:-----|:-------------|:-----|:-----|
| Activity-dependent V at fixed mass | ΔV ~ 30–70 km/s | 0 | 0 |
| Merger lensing lag | 15–45 kpc behind baryons | 0 | Opposite direction |

Both are feasible with current surveys (KiDS, HSC, Euclid).

**Details:** [ED-Data-Galaxy-12, 13](research/ED%20PAPERS/)
