# outreach/

**This folder is the public-facing entry point of the Event Density repository.** It contains the materials a new visitor should encounter first: the minimal demo notebook, a one-page overview, the strongest falsifiable prediction, audience-specific hooks, and the slide / video generators that drive talks and demos.

If you have 3 minutes, open the notebook. If you have 30 seconds, read the 1-pager.

## Contents

| File | Purpose | Audience |
|------|---------|----------|
| **[`ED_minimal_demo.ipynb`](ED_minimal_demo.ipynb)** | Run the full ED pipeline and see results | Everyone |
| [`ED_What_It_Does_1pager.md`](ED_What_It_Does_1pager.md) | One-page overview of the framework | Researchers |
| [`ED_Falsifiable_Prediction.md`](ED_Falsifiable_Prediction.md) | The strongest currently-untested prediction, with observational protocol | Observers, experimentalists |
| [`ED_Targeted_Hooks.md`](ED_Targeted_Hooks.md) | 2–3 sentence hooks for 8 different audiences | Outreach, talks |
| [`ED_3min_demo_script.md`](ED_3min_demo_script.md) | Timestamped script for a 3-minute video walkthrough | Video production |
| [`ED_MobilityLaw.md`](ED_MobilityLaw.md) | The Universal Mobility Law (UDM) paper, full Markdown source | Soft-matter readers |
| [`ED_ArXiv_MobilityLaw.md`](ED_ArXiv_MobilityLaw.md) | UDM paper, arXiv-formatted variant | Soft-matter readers |
| [`slides/`](slides/) | Slide and video-graphics generators (matplotlib) | Outreach prep |

The two UDM Markdown files (`ED_MobilityLaw.md` and `ED_ArXiv_MobilityLaw.md`) live here because they were authored as outreach-friendly readings of the published UDM paper. They will eventually be relocated to [`/papers/Universal_Mobility_Law/paper.md`](../papers/Universal_Mobility_Law/) as the canonical Markdown source; the publication-ready PDF is already at [`/papers/Universal_Mobility_Law/paper.pdf`](../papers/Universal_Mobility_Law/paper.pdf).

## Run the demo

**In Google Colab (zero setup):**

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Allen-Proxmire/Event-Density/blob/main/outreach/ED_minimal_demo.ipynb)

**Locally:**

```bash
git clone https://github.com/Allen-Proxmire/Event-Density.git
cd Event-Density
pip install -r requirements.txt
jupyter notebook outreach/ED_minimal_demo.ipynb
```

## What you will see in the demo

1. A 2D ED simulation running with canonical parameters
2. The density field evolving from a cosine perturbation toward equilibrium
3. All nine architectural laws verified against the simulation
4. The penalty channel reproducing RC-circuit decay at 0.00% error
5. The participation channel reproducing telegraph oscillation at 0.00% error
6. Monotone energy decay with dissipation channels summing exactly to 1

None of these behaviours were programmed in. They are structural consequences of the constitutive architecture.

## What is *not* here

The `analysis/` directory contains the reproducible research layer: per-paper reproduction notebooks ([`02_three_channels`](../analysis/notebooks/02_three_channels.ipynb), [`03_galaxy15_lag`](../analysis/notebooks/03_galaxy15_lag.ipynb), [`04_udm_mobility`](../analysis/notebooks/04_udm_mobility.ipynb)) and the figure-generation scripts that produce the figures in [`/papers/`](../papers/). If you want to reproduce a published result, start there. If you want to run the canonical demo or share ED with a non-specialist audience, start here.

## Where to go next

- [`/README.md`](../README.md) — the repository front page
- [`/RESULTS.md`](../RESULTS.md) — the unification narrative across the three flagship results
- [`/GETTING_STARTED.md`](../GETTING_STARTED.md) — install and reproduction quickstart
- [`/theory/PDE.md`](../theory/PDE.md) — the canonical PDE on one page
- [`/papers/`](../papers/) — canonical papers (one folder per paper)
