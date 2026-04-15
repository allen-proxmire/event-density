# analysis/

**The reproducible research layer of the Event Density repository.** Everything in this directory is code that produces or reproduces a scientific result: per-paper reproduction notebooks, figure-generation scripts, and reference implementations.

If you want to *use* the framework, start here. If you want to *show* it to someone, start at [`/outreach/`](../outreach/) instead.

## Contents

```
analysis/
├── README.md                         ← you are here
├── notebooks/                        ← per-paper reproduction notebooks
│   ├── 02_three_channels.ipynb       ← three constitutive channels in isolation
│   ├── 03_galaxy15_lag.ipynb         ← Galaxy-15 velocity-scaling + deceleration plots
│   └── 04_udm_mobility.ipynb         ← UDM universal-mobility-law fits
└── scripts/                          ← reproducible figure generators + reference impls
    ├── build_reproduction_notebooks.py        (regenerates the 02/03/04 notebooks)
    ├── generate_galaxy15_figures.py           (Galaxy-15 main figures: 1, 5, 6, 7, 9)
    ├── generate_galaxy15_supp_figures.py      (Galaxy-15 supplementary: S1–S4)
    ├── wake_derivation.py                     (analytic + numerical wake reference)
    ├── generate_analogue_summary.py           (foundational analogues summary)
    ├── generate_barenblatt_figure.py          (Barenblatt PME figure)
    ├── generate_channels_schematic.py         (three-channel schematic)
    ├── generate_frap_figure.py                (FRAP front-propagation figure)
    ├── generate_mobility_figure.py            (UDM mobility-law figure)
    └── generate_pme_similarity_figure.py      (PME self-similarity figure)
```

## Running the notebooks

The minimal-dependency setup (numpy, scipy, matplotlib) is in [`/requirements.txt`](../requirements.txt). Each notebook is self-contained and runs in under 10 seconds:

```bash
pip install -r requirements.txt
jupyter notebook analysis/notebooks/02_three_channels.ipynb
```

For a guided tour of all three notebooks see [`/GETTING_STARTED.md`](../GETTING_STARTED.md).

## Running the scripts

The scripts in `analysis/scripts/` are standalone Python files. They produce figures and reference outputs that are committed into the appropriate [`/papers/<paper>/figures/`](../papers/) directories. For example:

```bash
python analysis/scripts/generate_galaxy15_figures.py
```

writes the five main Galaxy-15 figures into the local `papers/Cluster_Merger_Lag_Evidence/figures/` directory. (Figures are typically regenerated only when the paper's data or model changes; the committed figures are the canonical artifacts.)

## Where to go next

- [`/papers/`](../papers/) — canonical papers, each with its own folder
- [`/theory/`](../theory/) — the canonical PDE statement
- [`/edsim/`](../edsim/) — the simulation engine (Python package + 112-test suite)
- [`/outreach/`](../outreach/) — public-facing materials and the minimal demo
