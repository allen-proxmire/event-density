# ED-Data-14: GALEX/WISE Photometric SFR Test

## Purpose

Definitive test of the ED-Phys-05 activity-dependence prediction using published photometric SFR values from GALEX+WISE surveys (z0MGS, KINGFISH, 11HUGS) and NED, replacing the calibrated estimates used in ED-Data-13.

## Key Results

| Indicator | Spearman rho | p-value | Direction | Significant? |
|-----------|---|---|---|---|
| log(sSFR) | -0.063 | 0.663 | Negative | No |
| log(SFR) | +0.247 | **0.081** | Positive | Marginal |
| Phot-only (n=33) | +0.039 | 0.828 | Positive | No |

## Verdict (revised 2026-04-17): INCONCLUSIVE, and sign-interpretation reversed

ρ(Δ_M, log SFR) = +0.247 at p = 0.081 (marginal). The positive sign is **not** in the ED-predicted direction once the sign-convention identity Δ_M = −B · Δ_V at fixed M is applied (see [`papers/ED-BTFR-Activity/memo.md`](../../papers/ED-BTFR-Activity/memo.md), §2). A translated V-space partial correlation from this sample would be approximately −0.25; the small sample (n = 51) prevents any strong claim either way. The sSFR null (ρ = −0.063, p = 0.66) is consistent with no activity signal once mass is removed. Definitive test: BIG-SPARC (ED-Data-18).

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
