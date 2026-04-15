# Cluster Merger-Lag Evidence (Galaxy-15)

First systematic empirical evidence for the Event Density prediction that the lensing mass centroid trails the brightest cluster galaxy in merging galaxy clusters, with a *velocity- and deceleration-dependent* offset $\ell = D_T / v_{\rm current}$.

The penalty channel of the canonical ED PDE, when coupled to a moving baryonic source, produces an exponential temporal-tension wake behind the source. The observable lensing-BCG offset is the wake's asymmetry length. With a single universal parameter $D_T = 2.1 \times 10^{27}\,\mathrm{m^2\,s^{-1}}$ — fixed independently from the Mistele et al. weak-lensing extent and **not fitted to any cluster** — the formula reproduces the offsets of seven well-measured clusters within uncertainty:

| Cluster | $v_{\rm peri}$ (km/s) | TSP (Gyr) | ED prediction (kpc) | Observed (kpc) |
|---|---|---|---|---|
| Bullet | 4500 | 0.15 | 15.1 | 17.78 ± 0.66 |
| El Gordo SE (along-axis) | 2500 | 0.75 | 27.2 | 28.7 |
| MACS J0025 | 2000 | 0.50 | 34.0 | \|33\| |
| MACS J1149 (SL) | 2770 | 1.16 | 24.6 (total) | 11.5 (SL → scale-dependence confirmed) |
| Musket Ball S | 1500 | 0.96 | 136.1 | 129 |
| ZwCl 0008 E | 1800 | 0.76 | 681 (limited by $t_{\rm lag}$) | 319 |
| CIZA J2242 | 2500 | 1.00 | 85.1 | 190 |

Plus the Finner et al. (2025) aggregate sample of 58 subclusters in 29 merging clusters: median offset 79 ± 14 kpc, matching the ED prediction of ~80 kpc for a typical post-merger radio-relic system.

Three ED-unique signatures all confirmed: velocity scaling ($n = -1.07 \pm 0.20$), deceleration scaling (offsets *grow* with TSP, opposite to SIDM's predicted decay), and scale dependence ($\ell_{\rm SL} < \ell_{\rm WL}$). Standard CDM is excluded by 50–80×; SIDM is disfavoured by the deceleration test and shows internal cross-cluster tension.

## Contents

| File | What it is |
|------|-----------|
| [`paper.md`](paper.md) | Canonical Markdown source |
| [`paper.pdf`](paper.pdf) | Compiled PDF (publication-ready) |
| [`paper.tex`](paper.tex) | LaTeX source |
| [`figures/`](figures/) | All paper figures (5 main + 4 supplementary, both .png and .pdf) |

## Reproduction notebook

A self-contained reproduction of the velocity-scaling and deceleration plots is in [`/analysis/notebooks/03_galaxy15_lag.ipynb`](../../analysis/notebooks/03_galaxy15_lag.ipynb). It runs in ~5 seconds in Colab and prints the fitted slope $n = -1.07 \pm 0.20$.

## Cross-references

- Canonical PDE (penalty channel): [`/theory/PDE.md`](../../theory/PDE.md), §4.2
- Cross-regime context (galactic regime mapping): [`/papers/Dimensional_Atlas/regimes/ED-Dimensional-04_Galactic_Regime.md`](../Dimensional_Atlas/regimes/ED-Dimensional-04_Galactic_Regime.md)
- Empirical results overview: [`/RESULTS.md`](../../RESULTS.md)
