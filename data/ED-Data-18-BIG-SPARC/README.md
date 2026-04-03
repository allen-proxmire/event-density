# ED-Data-18: BIG-SPARC Activity Test

## Status: AWAITING DATA RELEASE

**BIG-SPARC has not been publicly released.** The Haubner, Lelli et al. (2024, arXiv:2411.13329) paper is a conference proceedings announcement. The catalog (~4000 galaxies with HI rotation curves, WISE photometry, and mass models) is not yet available for download.

When BIG-SPARC is released, run:
```bash
python data/ED-Data-18-BIG-SPARC/scripts/run_bigsparc_test.py
```

## What BIG-SPARC Will Provide

- ~4000 galaxies with Vflat, baryonic mass, and WISE W1/W2/W3 photometry
- WISE W3 (12 um) flux as a uniform SFR proxy for all galaxies
- Enough statistical power (n ~ 2000-4000) to detect rho ~ 0.1 at p < 0.001

This would be the definitive test of ED-Phys-05: at n = 3000 with rho = 0.3, the p-value would be < 10^-6.

## Current State of the Activity Test

| Module | Source | n | rho(SFR, Delta) | p | Tertile p |
|--------|--------|---|-----------------|---|-----------|
| ED-Data-12 | T-type | 122 | +0.039 | 0.667 | 0.982 |
| ED-Data-13 | Calibrated | 116 | +0.263 | **0.004** | **0.033** |
| ED-Data-14 | Literature | 51 | +0.247 | 0.081 | 0.514 |
| ED-Data-15 | GSWLC | 0 | N/A | INCOMPATIBLE | — |
| ED-Data-16 | z0MGS (20) | 20 | +0.356 | 0.124 | **0.041** |
| ED-Data-17 | z0MGS (25) | 25 | +0.324 | 0.114 | **0.030** |

**The signal is positive in every module.** The tertile test is significant in 3 of 5 modules. The Spearman correlation was significant once (ED-Data-13, p = 0.004). The limitation is sample size: n = 25 is insufficient for definitive confirmation at the observed effect size (rho ~ 0.3).

## Honest Assessment

ED-Phys-05 is **not yet confirmed, not yet falsified**. The data are consistent with a weak positive correlation between star-formation activity and BTFR residuals. BIG-SPARC, when released, will settle this decisively.

## Data Source

- Haubner, K., Lelli, F., et al. 2024, arXiv:2411.13329 (announcement only)
- Expected release: TBD (check https://arxiv.org/abs/2411.13329 for updates)
