# ED-Data-16: z0MGS Cross-Match — Definitive Nearby Galaxy SFR Test

## The Result

**20 SPARC galaxies** with real, uniform, dust-corrected SFR from z0MGS (Leroy+ 2019).

| Test | Spearman rho | p-value | Direction |
|------|---|---|---|
| Delta vs log(SFR) | **+0.356** | **0.124** | **Positive** |
| Delta vs log(sSFR) | +0.092 | 0.700 | Positive |
| Tertile (high > low) | — | **0.041** | **Positive, significant** |

**Verdict: SUGGESTIVE** — The correlation is positive (rho = +0.36), the high-SFR tertile lies above the BTFR while the low-SFR tertile lies below (p = 0.04, significant), but the overall Spearman test is not significant at p < 0.05 with n = 20.

## Why This Matters

This is the **first test using real, uniform, dust-corrected SFR** for SPARC galaxies. All 20 SFR values come from the z0MGS catalog (Leroy et al. 2019, ApJS 244, 24), which provides combined GALEX+WISE photometric SFR from SED fitting — the gold standard for nearby-galaxy SFR estimation.

The **tertile test is significant** (p = 0.041): galaxies in the top third by SFR have a mean BTFR residual of +0.015, while galaxies in the bottom third have -0.099. This 0.11 dex separation in the ED-predicted direction passes at the 5% level.

## Progression Across Five Modules

| Module | SFR Source | n | rho(SFR, Delta) | p |
|--------|-----------|---|-----------------|---|
| ED-Data-12 | Morphological type | 122 | +0.039 | 0.667 |
| ED-Data-13 | Calibrated sSFR | 116 | +0.263 | **0.004** |
| ED-Data-14 | Literature compilation | 51 | +0.247 | 0.081 |
| ED-Data-15 | GSWLC | 0 | N/A | INCOMPATIBLE |
| **ED-Data-16** | **z0MGS (uniform)** | **20** | **+0.356** | **0.124** |

The signal has been **positive in every module** (rho = +0.04 to +0.36). The tertile test has been significant in ED-Data-13 (p = 0.033) and now ED-Data-16 (p = 0.041). The Spearman correlation was significant in ED-Data-13 (p = 0.004 at n = 116) and approaches significance in ED-Data-16 (p = 0.124 at n = 20). The limitation is sample size.

## Data Source

- z0MGS: Leroy, A. K., et al. 2019, ApJS, 244, 24
- VizieR catalog: J/ApJS/244/24/table4
- Each galaxy queried individually via VizieR cone search (60 arcsec)
- SFR type: Uniform GALEX+WISE dust-corrected SED fitting

## How to Reproduce

```bash
python data/ED-Data-16-z0MGS/scripts/run_z0mgs_test.py
```

## Files

```
data/ED-Data-16-z0MGS/
    scripts/run_z0mgs_test.py
    figures/P1-P5
    results/btfr_fit.json
    results/correlation_stats.json
    results/crossmatched_z0mgs.csv
    results/final_summary.json
    results/final_summary.md
```
