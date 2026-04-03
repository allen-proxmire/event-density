# ED-Data-12: Galactic Activity-Dependence Test

## Purpose

Test the ED-Phys-05 prediction that galaxies with higher star-formation activity lie systematically *above* the baryonic Tully-Fisher relation (BTFR) at fixed baryonic mass. This is an independent test of the ED participation field at galactic scales, completely decoupled from the condensed-matter programme.

## The ED Prediction

The participation field v(t) equilibrates on a finite timescale. Galaxies with recent activity (star formation, accretion) have v(t) out of equilibrium, which shifts their effective rotation velocity. ED predicts that active galaxies scatter above the BTFR, while quiescent galaxies lie on or below it. Neither LCDM nor MOND predicts this correlation.

## Data

- **Source:** SPARC (Lelli, McGaugh & Schombert 2016) — 122 galaxies with Vflat, baryonic mass, and morphological type
- **SFR proxy:** Morphological type T (late-type = high SFR, early-type = low SFR)
- **BTFR fit:** Theil-Sen robust regression, slope = 3.72

## Result

- Spearman rho = +0.039, p = 0.67
- Direction: **positive** (consistent with ED prediction)
- Significance: **not significant** (p > 0.05)
- Verdict: **SUGGESTIVE** — the sign is correct but the signal is not statistically significant with morphological type as the SFR proxy

## Interpretation

The correlation has the predicted sign but is too weak to be statistically significant with the current proxy (morphological type). This is expected — morphological type is a crude SFR indicator. A stronger test requires direct SFR measurements (GALEX FUV, WISE W4, or Halpha) cross-matched with the SPARC sample.

## How to Reproduce

```bash
python data/ED-Data-12-Galactic-Activity/scripts/run_galactic_activity_test.py
```

## Next Steps

1. Cross-match SPARC with GALEX All-Sky Survey (FUV-based SFR)
2. Cross-match with WISE (W3/W4 mid-IR SFR)
3. Use MaNGA IFU data for spatially-resolved Halpha SFR
4. Test with BIG-SPARC (4000 galaxies) when available

## Files

```
data/ED-Data-12-Galactic-Activity/
    scripts/run_galactic_activity_test.py
    figures/P1-P4 (BTFR, residuals, mass, histogram)
    results/btfr_fit.json
    results/correlation_stats.json
    results/crossmatched_table.csv
    results/final_summary.json
    results/final_summary.md
```
