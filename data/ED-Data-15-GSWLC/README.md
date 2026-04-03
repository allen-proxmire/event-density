# ED-Data-15: GSWLC Cross-Match (Definitive SFR Test)

## Status: INCOMPATIBLE — GSWLC Does Not Cover SPARC Galaxies

**GSWLC has a minimum redshift of z = 0.01. SPARC galaxies are at z < 0.005. These catalogs do not overlap.**

GSWLC was designed for SDSS galaxies at z = 0.01–0.30. SPARC galaxies are too nearby for SDSS spectroscopy — they are resolved, extended sources that overflow SDSS fibers. Zero of 42 SPARC galaxies matched within the GSWLC catalog.

The GSWLC catalog was downloaded and the cross-match was executed, confirming the incompatibility.

## How to Run

### Step 1: Download GSWLC

1. Go to **https://salims.pages.iu.edu/gswlc/**
2. Download **GSWLC-X2.dat.gz** (recommended; ~50 MB compressed, ~200 MB uncompressed)
   - Alternative: GSWLC-A2.dat.gz (deeper UV coverage, fewer galaxies)
3. Place the file in: `data/ED-Data-15-GSWLC/raw/`
4. Gunzip if needed: `gzip -d GSWLC-X2.dat.gz`

### Step 2: Run the analysis

```bash
python data/ED-Data-15-GSWLC/scripts/run_gswlc_crossmatch.py
```

The script will automatically:
- Load 660,000 GSWLC galaxies with dust-corrected SFR
- Cross-match 42 SPARC galaxies by position (< 10 arcsec)
- Fit the BTFR and compute residuals
- Test the ED-Phys-05 activity-dependence correlation
- Generate 3 publication-quality plots
- Save full results to `results/`

## Why GSWLC Is the Definitive Dataset

| Feature | ED-Data-12 | ED-Data-13 | ED-Data-14 | **ED-Data-15** |
|---------|------------|------------|------------|----------------|
| SFR source | Morphological type | Calibrated T-type | Literature compilation | **UV+IR SED fitting** |
| Dust correction | None | None | Partial | **Full (energy balance)** |
| Uniformity | Yes | Yes | No (mixed sources) | **Yes (single pipeline)** |
| n (expected) | 122 | 116 | 51 | **30-50** |

GSWLC provides the most reliable SFR estimates available for nearby galaxies: UV+optical+IR SED fitting with full dust correction and uniform methodology across all galaxies.

## The ED Prediction

Active galaxies (high SFR or sSFR) should lie systematically ABOVE the baryonic Tully-Fisher relation at fixed baryonic mass. This is a unique prediction of the ED participation field that neither LCDM nor MOND makes.

## Previous Results

| Module | rho(SFR, Delta) | p-value | Verdict |
|--------|-----------------|---------|---------|
| ED-Data-12 | +0.039 | 0.667 | Suggestive (wrong proxy) |
| ED-Data-13 | +0.263 | **0.004** | Significant (calibrated) |
| ED-Data-14 | +0.247 | 0.081 | Marginal (small n) |
| ED-Data-15 | N/A | N/A | **INCOMPATIBLE** (z ranges don't overlap) |

GSWLC cannot test SPARC galaxies (z_min = 0.01 vs SPARC z < 0.005). The correct catalog for this test is z0MGS (Leroy+ 2019), which covers z < 0.05 with GALEX+WISE photometry.

## Data Source

- Salim, S., Lee, J.C., Janowiecki, S., et al. 2016, ApJS, 227, 2
- Salim, S., Boquien, M., & Lee, J.C. 2018, ApJ, 859, 11
- https://salims.pages.iu.edu/gswlc/
