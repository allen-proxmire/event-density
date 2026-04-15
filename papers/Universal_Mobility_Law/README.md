# The Universal Mobility Law (UDM)

Empirical demonstration that concentration-dependent diffusivity in concentrated soft-matter systems follows a single universal functional form,

$$
D(c) \;=\; D_0 \,\bigl(1 - c/c_{\max}\bigr)^{\beta},
$$

predicted by the *mobility channel* of the canonical Event Density PDE. Tested against ten chemically distinct systems (hard-sphere colloids, BSA protein, sucrose, glycerol, PMMA colloids, casein micelles, polysaccharides, polymer melts, and small-molecule mixtures); every system fits with $R^2 > 0.986$. Population-mean exponent $\beta = 1.72 \pm 0.37$.

The paper additionally derives a zero-free-parameter falsifiable prediction: the FRAP front-recovery exponent for concentrated BSA at 200–350 mg/mL is $R(t) \sim t^{1/(3\beta+2)} \sim t^{0.12}$, distinct from the Fickian $t^{0.50}$. This is testable in an afternoon on any standard confocal microscope.

## Contents

| File | What it is |
|------|-----------|
| [`paper.pdf`](paper.pdf) | Compiled PDF (publication-ready) |

## Status of the Markdown source

The canonical Markdown source of this paper currently lives in [`/ED_FrontDoor/ED_MobilityLaw.md`](../../ED_FrontDoor/ED_MobilityLaw.md) (with an alternate arXiv-formatted version at [`/ED_FrontDoor/ED_ArXiv_MobilityLaw.md`](../../ED_FrontDoor/ED_ArXiv_MobilityLaw.md)). It will be relocated to `paper.md` here in a subsequent reorganization step; the PDF is canonical in the meantime.

## Reproduction notebook

A self-contained reproduction of the universal mobility-law fit on representative materials is in [`/analysis/notebooks/04_udm_mobility.ipynb`](../../analysis/notebooks/04_udm_mobility.ipynb). It runs in ~3 seconds in Colab.

## Cross-references

- Canonical PDE (mobility channel): [`/theory/PDE.md`](../../theory/PDE.md), §4.1
- Falsifiable prediction (FRAP front exponent): [`/ED_FrontDoor/ED_Falsifiable_Prediction.md`](../../ED_FrontDoor/ED_Falsifiable_Prediction.md)
- Empirical results overview: [`/RESULTS.md`](../../RESULTS.md)
