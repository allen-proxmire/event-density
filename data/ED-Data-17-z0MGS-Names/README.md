# ED-Data-17: Expanded z0MGS Cross-Match (25 Galaxies)

## Result

**25 SPARC galaxies** with uniform z0MGS GALEX+WISE SFR. All values from Leroy+ 2019 via VizieR.

| Test | Value | Significant? |
|------|-------|---|
| Spearman rho(Delta, SFR) | **+0.324** (p=0.114) | No (n=25 too small) |
| Pearson r(Delta, SFR) | +0.315 (p=0.125) | No |
| Kendall tau | +0.214 (p=0.135) | No |
| Tertile (high > low) | **p=0.030** | **Yes** |

**Verdict (revised 2026-04-17): MODULE INCONCLUSIVE; sign interpretation reversed.** ρ(Δ_M, log SFR) = +0.324 and the tertile Mann–Whitney test at p = 0.030 are real. Both were computed with Δ_M (M-space residual from the M-on-V fit). By the identity Δ_M = −B · Δ_V at fixed baryonic mass, the positive M-space signal is algebraically a **negative** V-space signal — opposite to the ED prediction of V-inflation for active galaxies. Sample size (n = 25) is insufficient for statistical significance in either convention on the Spearman. Definitive test: BIG-SPARC (ED-Data-18). Full analysis: [`papers/ED-BTFR-Activity/memo.md`](../../papers/ED-BTFR-Activity/memo.md).

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
