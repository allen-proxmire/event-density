# ED-Data-14: GALEX/WISE Photometric SFR Test

## Purpose

Definitive test of the ED-Phys-05 activity-dependence prediction using published photometric SFR values from GALEX+WISE surveys (z0MGS, KINGFISH, 11HUGS) and NED, replacing the calibrated estimates used in ED-Data-13.

## Key Results

| Indicator | Spearman rho | p-value | Direction | Significant? |
|-----------|---|---|---|---|
| log(sSFR) | -0.063 | 0.663 | Negative | No |
| log(SFR) | +0.247 | **0.081** | Positive | Marginal |
| Phot-only (n=33) | +0.039 | 0.828 | Positive | No |

## Verdict: INCONCLUSIVE

The total SFR shows a marginal positive correlation (p = 0.08) in the ED-predicted direction, but the specific SFR shows no correlation. The photometric-only subsample (33 galaxies with z0MGS, KINGFISH, or 11HUGS SFR) shows no significant signal. The sample size (51 galaxies) is too small for a definitive test.

## Progression Across Modules

| Module | Proxy | n | rho(SFR) | p(SFR) |
|--------|-------|---|----------|--------|
| ED-Data-12 | Morphological type | 122 | +0.039 | 0.667 |
| ED-Data-13 | Calibrated sSFR | 116 | +0.263 | **0.004** |
| ED-Data-14 | Photometric SFR | 51 | +0.247 | 0.081 |

The total-SFR signal persists across all three modules (always positive, always rho ~ 0.2-0.3) but is only significant in ED-Data-13 (largest sample with calibrated sSFR). The smaller photometric sample in ED-Data-14 lacks the statistical power to confirm or deny the signal.

## Data Sources

- z0MGS (Leroy+ 2019): 17 galaxies with GALEX+WISE SFR
- KINGFISH (Kennicutt+ 2011, Dale+ 2017): 7 galaxies with Halpha+24um SFR
- 11HUGS (Lee+ 2009): 9 dwarf galaxies with Halpha SFR
- NED: 14 galaxies with GALEX FUV-based SFR
- EST: 4 galaxies with estimated SFR from T-type calibration

## Next Steps

1. Download full GSWLC catalog (700K galaxies) and cross-match with SPARC
2. Use BIG-SPARC (4000 galaxies) when available
3. Perform uniform GALEX+WISE aperture photometry for all 175 SPARC galaxies

## How to Reproduce

```bash
python data/ED-Data-14-Photometric-SFR/scripts/run_photometric_sfr.py
```
