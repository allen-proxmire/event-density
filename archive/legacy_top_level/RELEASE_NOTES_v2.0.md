# Event Density — Release Notes, v2.0

**Release date:** 2026-04-14
**Tag:** `v2.0`
**Codename:** *Canonical Layer*

---

## Summary

Version 2.0 is a **structural release**: no scientific results have been retracted, no theoretical claims have been weakened, and no code in the simulation engine has been changed. What has changed is the *organisation* of the repository. After a year of organic research growth, the project had accumulated 80+ sub-directories of historical research notes, two parallel paper trees, four stray PDFs at the root, and broken cross-references in the structural documentation. v2.0 collapses all of that into a single clean architecture with a self-documenting layout, one folder per scientific paper, an explicit canonical theory layer, a reproducible research layer, and a preservation archive. Every claim still in the canonical record is now traceable to a single canonical source.

The motivating architectural review is preserved in [`docs/ARCHITECTURAL_REVIEW.md`](docs/ARCHITECTURAL_REVIEW.md). The v2.0 reorganisation executed the ten-step migration plan proposed there, in six commits (Steps 1–6), with `pytest edsim/tests/` returning **112/112 passing** at every step and the canonical Colab demo URL preserved through every rename.

---

## The new top-level architecture

```
event-density/
├── README.md                  ← PDE-focused front door (one-page PDE on display)
├── RESULTS.md                 ← three-result unification narrative
├── GETTING_STARTED.md         ← install + reproduction quickstart
├── CONTRIBUTING.md
├── LICENSE                    ← MIT
├── pyproject.toml
├── requirements.txt
├── .gitignore
│
├── theory/                    ← canonical PDE statement
├── papers/                    ← 6 canonical paper folders
├── edsim/                     ← simulation engine (Python pkg, 112 tests)
├── analysis/                  ← reproduction notebooks + reference scripts
├── outreach/                  ← public-facing entry, demo notebook, slides
├── data/                      ← empirical datasets
├── outputs/                   ← solver outputs (gitignored)
├── docs/                      ← true documentation (architecture, API, changelog)
└── archive/                   ← preservation layer (research history, legacy docs)
```

Ten directories. Every name self-documents its role. No directory at the top level requires a glossary to interpret.

---

## The canonical theory layer — `theory/`

Two files. That is the entire `theory/` directory:

| File | Role |
|------|------|
| [`theory/PDE.md`](theory/PDE.md) | **The authoritative one-page statement of the canonical Event Density PDE.** Four primitives, seven structural constraints, three constitutive channels, dimensional summary. Every other document points back here. |
| [`theory/README.md`](theory/README.md) | High-level navigation; links the three constitutive channels to the three flagship empirical results. |

The long-form theoretical *papers* (the Foundational Paper, the Ontology paper, the Dimensional Atlas, the Numerical Atlas) live in `papers/` where every paper has its own canonical folder. `theory/` is the navigation layer; `papers/` is the content layer.

The canonical PDE in one expression:

```
∂_t ρ = D · [ M(ρ) ∇²ρ + M'(ρ) |∇ρ|² − P(ρ) ] + H · v
v̇   = (1/τ) · ( F̄(ρ) − ζ · v )
```

with `M(ρ) = M₀(ρ_max − ρ)^β` and `P(ρ) = P₀(ρ − ρ*)`. Four primitives (density, mobility, penalty, participation) and seven structural constraints (locality, isotropy, gradient-driven flow, dissipative structure, single scalar field, minimal coupling, dimensional consistency) uniquely select this PDE. Three channels (mobility ⇔ porous-medium, penalty ⇔ exponential decay, participation ⇔ telegraph oscillation) reduce *exactly* to known foundational equations when isolated.

---

## The canonical papers layer — `papers/`

Six folders, one per scientific paper. Every paper folder contains the same canonical layout: `paper.md` (Markdown source), `paper.pdf` (publication-ready PDF), optional `paper.tex` (LaTeX source), `figures/` (per-paper figures), and a per-folder `README.md`.

| Folder | What it is |
|--------|-----------|
| [`papers/Foundations_of_Event_Density/`](papers/Foundations_of_Event_Density/) | The axiomatic Foundational Paper: derivation of the canonical PDE, the six original 2D structural analogues, 3D extensions in Appendix G, and ten formal supporting appendices (independence proofs, sufficiency proofs, PDE analysis, universality class, numerical methods, glossary, references) |
| [`papers/Event_Density_Ontology_and_Axioms/`](papers/Event_Density_Ontology_and_Axioms/) | The ontological framing: "becoming" as primitive, the ontological status of the four primitives, and the interpretive layer underlying the Foundational Paper |
| [`papers/Universal_Mobility_Law/`](papers/Universal_Mobility_Law/) | UDM — universal mobility law `D(c) = D₀(1 − c/c_max)^β` tested against 10 chemically distinct soft-matter systems, all R² > 0.986 |
| [`papers/Cluster_Merger_Lag_Evidence/`](papers/Cluster_Merger_Lag_Evidence/) | Galaxy-15 — the first systematic empirical test of the cluster-merger lensing-BCG offset prediction `ℓ = D_T / v_current` against 7 well-measured clusters and the Finner et al. (2025) aggregate of 58 subclusters |
| [`papers/Dimensional_Atlas/`](papers/Dimensional_Atlas/) | The five-regime mapping (quantum, Planck, condensed-matter, galactic, cosmological) spanning 61 orders of magnitude with the universal nondimensional invariant `D · T₀ / L₀² = 0.3` |
| [`papers/Numerical_Atlas/`](papers/Numerical_Atlas/) | The computational atlas: well-posedness, spectral decay, modal hierarchy, Lyapunov dissipation, bifurcation surface, three-stage convergence — all numerically realised across the (D, ζ, τ) parameter space |

---

## The reproducible research layer — `analysis/`

Self-contained scientific code that produces or reproduces canonical results.

```
analysis/
├── README.md
├── notebooks/                            (Colab-runnable in seconds each)
│   ├── 02_three_channels.ipynb           three PDE channels in isolation
│   ├── 03_galaxy15_lag.ipynb             velocity-scaling + deceleration plots
│   └── 04_udm_mobility.ipynb             universal-mobility-law fits
└── scripts/
    ├── build_reproduction_notebooks.py   regenerates the notebooks above
    ├── generate_galaxy15_figures.py      Galaxy-15 main figures
    ├── generate_galaxy15_supp_figures.py Galaxy-15 supplementary figures
    ├── wake_derivation.py                analytic + numerical wake reference
    ├── generate_analogue_summary.py
    ├── generate_barenblatt_figure.py
    ├── generate_channels_schematic.py
    ├── generate_frap_figure.py
    ├── generate_mobility_figure.py
    └── generate_pme_similarity_figure.py
```

Each notebook is **self-contained** — depends only on numpy/scipy/matplotlib so it runs in Colab without cloning the package. Each notebook prints quantitative checks (e.g., the velocity-scaling power-law fit returns `n = -1.07 ± 0.20`, consistent with ED's prediction `n = -1`).

---

## The public-facing layer — `outreach/`

Renamed from `ED_FrontDoor/` and trimmed to its actual outreach mission.

| File | Audience |
|------|----------|
| [`outreach/ED_minimal_demo.ipynb`](outreach/ED_minimal_demo.ipynb) | Everyone — the canonical 3-minute demo |
| [`outreach/ED_What_It_Does_1pager.md`](outreach/ED_What_It_Does_1pager.md) | Researchers — one-page overview |
| [`outreach/ED_Falsifiable_Prediction.md`](outreach/ED_Falsifiable_Prediction.md) | Observers/experimentalists — the strongest currently-untested prediction with observational protocol |
| [`outreach/ED_Targeted_Hooks.md`](outreach/ED_Targeted_Hooks.md) | 2-3 sentence hooks for 8 different audiences |
| [`outreach/ED_3min_demo_script.md`](outreach/ED_3min_demo_script.md) | Video production |
| [`outreach/ED_MobilityLaw.md`](outreach/ED_MobilityLaw.md) and [`ED_ArXiv_MobilityLaw.md`](outreach/ED_ArXiv_MobilityLaw.md) | UDM Markdown sources (will move to `papers/Universal_Mobility_Law/paper.md` in v2.x) |
| [`outreach/slides/`](outreach/slides/) | Slide and video-graphics generators |

The Colab badge URL — preserved through every rename in the v2.0 reorg — points at [`outreach/ED_minimal_demo.ipynb`](https://colab.research.google.com/github/Allen-Proxmire/Event-Density/blob/main/outreach/ED_minimal_demo.ipynb).

---

## The archival layer — `archive/`

Material that was canonical at some point in the project's history but is no longer the authoritative source for any current claim. **Nothing in `archive/` should be cited as the authority for any present claim.** Material is preserved for provenance, traceability, and future reference.

```
archive/
├── README.md
├── research_history/                ← formerly docs/research/ (~250 files)
│   ├── ED Architecture/             (13 architectural-analysis notes)
│   ├── ED Collaboration/            (collaboration kits, outreach drafts)
│   ├── ED Cosmology/                (early cosmology series)
│   ├── ED Data/                     (early data-pipeline notes)
│   ├── ED Experiments/              (experiment design notes)
│   ├── ED Interpretations/          (interpretation papers)
│   ├── ED PAPERS/                   (legacy paper drafts and supporting notes)
│   ├── ED Physics/                  (~112 ED-Phys series files)
│   ├── ED Simulation/               (~73 simulation-history files)
│   └── ED Validation/               (validation records)
└── docs_legacy/                     ← pre-v2.0 top-level docs
    ├── manuscript/                  (27 analogue and physics reports)
    ├── CORE_PAPERS.md               (superseded by /papers/)
    ├── RESULTS_OVERVIEW.md          (superseded by /RESULTS.md)
    ├── KEY_FINDINGS_TAKEAWAYS.md    (superseded by /RESULTS.md)
    ├── WHAT_IS_ED.md                (superseded by /README.md)
    ├── REPO_STRUCTURE.md            (superseded by /README.md repo map)
    ├── REPRODUCING_FOUNDATIONS_PAPER.md, HOW_TO_RUN.md, HOW_TO_RUN_ANALOGUES.md
    │                                (superseded by /GETTING_STARTED.md)
    ├── index.md, comparison.md, math.md, performance.md, regimes.md,
    │   roadmap.md, units.md, usage.md (reference notes)
    ├── phys_*.md                    (10 physics regime notes superseded by
    │                                 /papers/Dimensional_Atlas/)
    └── ED_ArXiv_MobilityLaw.pdf     (duplicate of /papers/Universal_
                                      Mobility_Law/paper.pdf)
```

If a document in `archive/` is in conflict with a canonical document, the canonical document wins.

---

## The three flagship results

v2.0 introduces a unification narrative that ties three independent empirical regimes to the *same* canonical PDE with *no* fitting between domains. The full statement is in [`/RESULTS.md`](RESULTS.md). In summary:

| Result | Channel exercised | Prediction | Evidence |
|--------|-------------------|------------|----------|
| **UDM** ([`/papers/Universal_Mobility_Law/`](papers/Universal_Mobility_Law/)) | Mobility | `D(c) = D₀(1 − c/c_max)^β` | 10 chemically distinct materials, R² > 0.986, β = 1.72 ± 0.37 |
| **Galaxy-15** ([`/papers/Cluster_Merger_Lag_Evidence/`](papers/Cluster_Merger_Lag_Evidence/)) | Penalty / dynamical wake | `ℓ = D_T / v_current` | 7 clusters consistent within uncertainty; Finner et al. (2025) median 79 ± 14 kpc matches predicted ~80 kpc |
| **PDE Atlas** ([`/papers/Dimensional_Atlas/`](papers/Dimensional_Atlas/) + [`/papers/Numerical_Atlas/`](papers/Numerical_Atlas/)) | All channels, all five regimes | One PDE, `D · T₀ / L₀² = 0.3` invariant | 9 architectural laws verified in dimensions 1–4; 61 orders of magnitude in length |

The unifier is the diffusivity `D`. Set independently from the Mistele weak-lensing observation at galactic scales (giving `D_T = 2.1 × 10²⁷ m²/s`), the *same* constant — through the dimensional bridges of the Atlas — becomes the `D₀` of the soft-matter mobility law in the condensed-matter regime. The PDE Atlas is the formal mapping that connects them.

---

## What's new in v2.0

### Structural

- **One canonical PDE statement** at [`theory/PDE.md`](theory/PDE.md) with the four primitives, seven structural constraints, three channels, and dimensional summary on a single page.
- **Six descriptive paper folders** in `papers/`, replacing the old `ED01`/`ED02`/`Galaxy-15`/`UDM` legacy naming. Each contains `paper.md`, `paper.pdf`, optional `paper.tex`, `figures/`, and a per-folder `README.md`.
- **Three new top-level documents** ([`README.md`](README.md), [`RESULTS.md`](RESULTS.md), [`GETTING_STARTED.md`](GETTING_STARTED.md)) replace ~10 fragmented summary documents.
- **Three new reproduction notebooks** ([`02_three_channels`](analysis/notebooks/02_three_channels.ipynb), [`03_galaxy15_lag`](analysis/notebooks/03_galaxy15_lag.ipynb), [`04_udm_mobility`](analysis/notebooks/04_udm_mobility.ipynb)) turn each flagship result into a runnable demo.
- **Five new figures** + **four supplementary figures** for Galaxy-15, with all source files committed alongside the paper.
- **Public-facing `outreach/`** (renamed from `ED_FrontDoor/`) cleanly distinguished from the `analysis/` reproducible research layer.
- **80+ directory historical research log** preserved in `archive/research_history/` rather than dominating the top-level documentation.

### Scientific

- **The Galaxy-15 paper is brand new in v2.0.** It is the first systematic empirical test of the cluster-merger lensing-BCG offset prediction. Three ED-unique signatures (velocity scaling `n = -1.07 ± 0.20`, deceleration scaling, scale dependence) are confirmed in the data; LCDM is excluded by 50–80×; SIDM is disfavoured by the deceleration test.
- **The corrected merger-lag formula** `ℓ = D_T / v_current` (replacing the Galaxy-13 `ℓ = D_T / v_peri` formula) resolves the largest discrepancy in the original predictions: the Musket Ball south offset goes from a 2.8× overshoot to within 5% of the prediction.
- **The Finner et al. (2025) aggregate sample** of 58 subclusters in 29 merging clusters has been independently digitised and cross-matched with published merger velocities; the median DM-BCG offset of 79 ± 14 kpc matches the ED prediction of ~80 kpc for typical post-merger systems.

### Documentation

- Every cross-reference in the canonical layer (README, RESULTS, GETTING_STARTED, theory/, papers/) is verified to resolve to a real file.
- `docs/ARCHITECTURAL_REVIEW.md` records the reasoning behind every structural decision.
- `archive/README.md` documents the canonical-vs-archival policy.
- Each canonical paper folder has its own `README.md` linking the paper to its channel, its reproduction notebook, and its empirical companion result.

---

## Migration notes for existing users

If you have an older clone of the repository:

```bash
git pull origin main
```

Old paths and where they went:

| Old path | New path |
|----------|----------|
| `papers/UDM/` | `papers/Universal_Mobility_Law/` |
| `papers/galaxy-15/` | `papers/Cluster_Merger_Lag_Evidence/` |
| `papers/foundational/` | `papers/Foundations_of_Event_Density/` |
| `papers/ED_Merger_Lag_Prediction/` | (duplicate; removed) |
| `ED-Data-Galaxy-15_*.pdf` (root) | `papers/Cluster_Merger_Lag_Evidence/paper.pdf` |
| `ED01_UDM_MobilityLaw.pdf` (root) | `papers/Universal_Mobility_Law/paper.pdf` |
| `ED02_Foundational_Paper.pdf` (root) | `papers/Foundations_of_Event_Density/paper.pdf` |
| `ED_FrontDoor/` | `outreach/` |
| `ED_FrontDoor/ED_minimal_demo.ipynb` | `outreach/ED_minimal_demo.ipynb` |
| `ED_FrontDoor/generate_*_figure.py` | `analysis/scripts/generate_*_figure.py` |
| `ED_FrontDoor/generate_slides.py` | `outreach/slides/generate_slides.py` |
| `scripts/` (top level) | `analysis/scripts/` |
| `docs/research/` | `archive/research_history/` |
| `docs/manuscript/` | `archive/docs_legacy/manuscript/` |
| `docs/CORE_PAPERS.md`, `docs/RESULTS_OVERVIEW.md`, `docs/KEY_FINDINGS_TAKEAWAYS.md`, `docs/WHAT_IS_ED.md`, `docs/REPO_STRUCTURE.md`, `docs/HOW_TO_RUN*.md`, `docs/REPRODUCING_FOUNDATIONS_PAPER.md`, `docs/phys_*.md`, … | `archive/docs_legacy/<filename>` |
| Direct reference to the canonical PDE | now [`theory/PDE.md`](theory/PDE.md) |
| Reading-order summary | now [`RESULTS.md`](RESULTS.md) |
| Run instructions | now [`GETTING_STARTED.md`](GETTING_STARTED.md) |

The Colab badge URL in the README has been updated to the new demo location and is the canonical way to launch the demo.

---

## Verification

Every commit in the v2.0 reorganisation series (Steps 1–6) was verified against:

| Check | Outcome |
|-------|---------|
| `pytest edsim/tests/` | **112/112 passing** at every step |
| Three reproduction notebooks (`02`, `03`, `04`) | All executed end-to-end via `jupyter nbconvert` |
| Canonical Colab demo (`outreach/ED_minimal_demo.ipynb`) | Working URL preserved through every rename |
| Cross-reference validity | `grep -r` across `*.md`, `*.py`, `*.ipynb` for stale paths returns zero matches outside `archive/` |
| Empty / orphaned directories | None remaining in canonical layout |
| Build artifacts | Local `outputs/` is gitignored; LaTeX `.aux/.log/.out` artifacts in `Remove from Repo/` for review |

The simulation engine (`edsim/`) and the canonical demo are functionally identical to v1.x. No code changes accompanied the v2.0 reorganisation.

---

## Acknowledgements

The v2.0 reorganisation followed a ten-step migration plan derived from a full architectural review. Steps 1–6 were executed in sequence over a single working session, each as one or more test-passing commits. The architectural review and the migration plan are preserved in [`docs/ARCHITECTURAL_REVIEW.md`](docs/ARCHITECTURAL_REVIEW.md).

The Galaxy-15 result builds on the empirical work of Cha et al. (2025), Finner et al. (2025), Dawson et al. (2012, 2013), Golovich et al. (2017, 2019), Jee et al. (2014, 2015, 2021), Bradac et al. (2008), Wittman et al. (2018), and the Merging Cluster Collaboration. The Mistele et al. (2024) weak-lensing observation provides the independent constraint on `D_T` used throughout.

---

## Looking ahead

A short follow-up release (v2.x) will:

- Relocate the UDM Markdown source from `outreach/ED_MobilityLaw.md` into `papers/Universal_Mobility_Law/paper.md` (the PDF is already canonical there).
- Decide on a tracking policy for canonical paper PDFs (Git LFS or GitHub Releases).
- Add reproduction notebooks `01_minimal_demo.ipynb` (a copy of the canonical demo, in `analysis/notebooks/` for reading-order continuity) and additional cluster-by-cluster Galaxy-15 notebooks if the Finner per-cluster catalog becomes available.

Larger forward work (Euclid and LSST follow-up of Galaxy-15, MCMAC reanalysis of El Gordo / MACS J0025 / CIZA J2242, FRAP front-exponent test of the UDM falsifiable prediction) is documented in [`outreach/ED_Falsifiable_Prediction.md`](outreach/ED_Falsifiable_Prediction.md) and in §8 of [`papers/Cluster_Merger_Lag_Evidence/paper.md`](papers/Cluster_Merger_Lag_Evidence/paper.md).

---

**License:** MIT
**Contact:** Allen Proxmire — open an issue on [github.com/Allen-Proxmire/Event-Density](https://github.com/Allen-Proxmire/Event-Density)
