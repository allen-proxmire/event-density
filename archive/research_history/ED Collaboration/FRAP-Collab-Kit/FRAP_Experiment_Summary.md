# FRAP Experiment Summary

## What We Measure

The rate at which a photobleached spot recovers in concentrated BSA-FITC protein solutions. Specifically, we measure the exponent alpha_R in the power law R(t) ~ t^alpha_R, where R(t) is the radius of the bleached region.

## Prediction

| Quantity | Our prediction | Standard theory |
|----------|---------------|-----------------|
| Recovery exponent | 0.16 | 0.50 |
| Front shape | Sharp-edged (compact) | Smooth Gaussian tail |
| Concentration dependence of exponent | None (constant) | None (constant) |

## Sample Preparation

| Item | Specification |
|------|---------------|
| Protein | BSA-FITC conjugate (Sigma A9771 or equivalent) |
| Concentrations | 200, 250, 300, 350 mg/mL |
| Buffer | 50 mM sodium phosphate, pH 7.0, 150 mM NaCl |
| Chamber | Coverslip sandwich, 10-50 um spacer, sealed with vacuum grease |
| Temperature | 25.0 +/- 0.5 C |

## Imaging

| Parameter | Value |
|-----------|-------|
| Microscope | Any confocal with FRAP (Zeiss, Leica, Nikon, Olympus) |
| Objective | 40x or 63x, NA >= 1.2 |
| Excitation | 488 nm |
| Frame rate | 10-60 fps |
| Pixel size | <= 0.4 um |
| Field of view | >= 25 um x 25 um |

## Photobleaching

| Parameter | Value |
|-----------|-------|
| Bleach ROI | Circle, radius 2-5 um |
| Bleach power | Maximum 488 nm |
| Bleach duration | 0.5-2 s |
| Target depth | > 80% fluorescence loss at centre |

## Protocol (Per Concentration)

1. Load sample, equilibrate 10 min
2. Record 5-10 pre-bleach frames
3. Bleach the ROI
4. Record recovery for 2 s (or until full recovery)
5. Repeat in a different field of view (5 replicates)
6. Save raw TIFF stacks

## Total Time

- 4 concentrations x 5 replicates x 3 min setup = ~60 min imaging
- Plus sample prep: ~2-3 hours
- **Total: 4-6 hours**

## What to Send Us

- Raw TIFF stacks (16-bit)
- Metadata: fps, pixel size (um), bleach ROI coordinates, bleach duration, concentration, temperature

## Full Technical Details

See: `documents/research/ED Physics/ED-Phys-12/ED-Phys-12_FRAP_CollaborationPlan.md`
