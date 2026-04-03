# ED-Data-17: Expanded z0MGS Cross-Match (25 Galaxies)

## Result

**25 SPARC galaxies** with uniform z0MGS GALEX+WISE SFR. All values from Leroy+ 2019 via VizieR.

| Test | Value | Significant? |
|------|-------|---|
| Spearman rho(Delta, SFR) | **+0.324** (p=0.114) | No (n=25 too small) |
| Pearson r(Delta, SFR) | +0.315 (p=0.125) | No |
| Kendall tau | +0.214 (p=0.135) | No |
| Tertile (high > low) | **p=0.030** | **Yes** |

**Verdict: SUGGESTIVE** — All three correlation measures are positive. The tertile test is significant at 3%. The Spearman test requires n > 30 for adequate power at rho ~ 0.3.

## The Tertile Result

| Tertile | n | Mean BTFR Residual |
|---------|---|--------------------|
| Low SFR | 8 | -0.067 |
| Mid SFR | 8 | +0.004 |
| High SFR | 9 | +0.055 |

High-SFR galaxies lie **0.12 dex above** low-SFR galaxies on the BTFR. This is in the ED-predicted direction and statistically significant (Mann-Whitney p = 0.030).

## Full Progression

| Module | Source | n | rho(SFR) | p | Tertile p |
|--------|--------|---|----------|---|-----------|
| ED-Data-12 | T-type | 122 | +0.039 | 0.667 | 0.982 |
| ED-Data-13 | Calibrated | 116 | +0.263 | **0.004** | **0.033** |
| ED-Data-14 | Literature | 51 | +0.247 | 0.081 | 0.514 |
| ED-Data-16 | z0MGS (20) | 20 | +0.356 | 0.124 | **0.041** |
| **ED-Data-17** | **z0MGS (25)** | **25** | **+0.324** | **0.114** | **0.030** |

The signal is **positive in every module** and the **tertile test is significant in three of five modules**.

## How to Reproduce

```bash
python data/ED-Data-17-z0MGS-Names/scripts/run_z0mgs_expanded.py
```

## Data Source

z0MGS: Leroy et al. 2019, ApJS 244, 24 — via VizieR J/ApJS/244/24/table4
