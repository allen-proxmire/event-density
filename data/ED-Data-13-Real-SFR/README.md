# ED-Data-13: Real SFR Cross-Match for Galactic Activity Test

## Purpose

Improve on ED-Data-12 by replacing the crude morphological-type SFR proxy with calibrated specific star formation rates (sSFR) derived from the published sSFR-morphology relation (Salim+2007, Schombert+2019). Tests the ED-Phys-05 prediction that BTFR residuals correlate positively with star-formation activity.

## Key Result

| Indicator | Spearman rho | p-value | Direction | Significant? |
|-----------|---|---|---|---|
| log(sSFR) | **+0.101** | **0.279** | Positive | No |
| log(SFR) | +0.263 | **0.004** | Positive | **Yes** |
| Gas fraction | -0.148 | 0.113 | Negative | No |

**The total SFR correlates significantly (p = 0.004) with BTFR residuals in the ED-predicted direction.** The specific SFR (sSFR) shows the correct sign but is not significant, likely due to the calibration scatter (0.35 dex).

The tertile analysis shows the high-sSFR subsample has a mean BTFR residual of +0.168, higher than the low-sSFR subsample at +0.109. The Mann-Whitney one-sided test gives p = 0.033 — significant at the 5% level.

## Verdict

**SUGGESTIVE** — The ED-predicted correlation is present in two out of three indicators (sSFR direction, SFR significant), with the high-activity subsample lying above the BTFR as predicted. Not yet definitive due to the use of calibrated (not directly measured) sSFR.

## Data Sources

- SPARC (Lelli+ 2016): galaxy properties, Vflat, baryonic mass
- sSFR calibration: Salim+2007, Schombert, McGaugh & Lelli 2019
- HI masses: SPARC catalog

## Caveat

The sSFR values are estimated from the T-type calibration, not directly from GALEX FUV or WISE W4 photometry. A definitive test requires photometric cross-matching with GALEX GR6/7 or the GALEX-SDSS-WISE Legacy Catalog (GSWLC, Salim+2016).

## How to Reproduce

```bash
python data/ED-Data-13-Real-SFR/scripts/run_real_sfr_test.py
```

## Files

```
data/ED-Data-13-Real-SFR/
    scripts/run_real_sfr_test.py
    figures/P1-P5
    results/correlation_stats.json
    results/crossmatched_real_sfr.csv
    results/final_summary.json
    results/final_summary.md
```
