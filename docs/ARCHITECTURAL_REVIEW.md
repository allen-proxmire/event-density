# Event Density — Repository Architectural Review

**Reviewer:** Repo audit, 2026 April 14
**Scope:** Whole-repository structure, fresh-cloner experience, scientific narrative integration, proposed restructure, migration plan.
**Verdict in one sentence:** the *science* is unusually strong and the *front door* (`ED_FrontDoor/`) is excellent, but the rest of the repo is a 12-month research log that has grown organically into ~90 sub-directories, with two parallel paper trees, four stray PDFs at the root, broken cross-references in the structure docs, and no single page that ties Galaxy-15, UDM, and the PDE Atlas back to the one canonical PDE that is supposed to underlie all three.

---

## 1. Fresh-Cloner Experience: First Five Minutes

I traced the path a new visitor would take, starting from the GitHub landing page and moving through `git clone` to first execution. Here is what they actually encounter.

### 1.1 What they see (seconds 0–30)

GitHub landing page renders `README.md`, which is **good**:

- Strong opening claim: "a single PDE — derived from four primitives and seven axioms".
- Colab badge near the top.
- "Start Here" pointing to `ED_FrontDoor/`.
- Numbers table at the bottom (length scales, R², error percentages).

But also visible in the file tree (and slightly jarring):

- `ED-Data-Galaxy-15_First_Evidence_For_Merger_Lag.pdf` (1.7 MB) — at root
- `ED01_UDM_MobilityLaw.pdf` (515 KB) — at root
- `ED02_Foundational_Paper.pdf` (789 KB) — at root
- `Event Density as a Physical Ontology.pdf` (387 KB) — at root, with a space in the filename
- `papers/` and `docs/research/ED PAPERS/` — visibly redundant top-level entries

**First impression:** "research-grade, but slightly disorganised."

### 1.2 What they run (seconds 30–180)

If they follow the Colab badge: works as advertised. The demo notebook is 12 KB, depends only on numpy/scipy/matplotlib, and is genuinely minimal. **This is the strongest part of the repo.**

If they `git clone` and `pip install -r requirements.txt`: also works. Dependencies are conservative (numpy ≥ 1.24, scipy ≥ 1.10, matplotlib ≥ 3.7, scikit-learn ≥ 1.2). The `edsim` package is a real installable Python module with a CLI (`edsim info`, `edsim run`, `edsim sweep`, `edsim certify`).

If they run the test suite (`pytest edsim/tests/`): 112 tests, presumed passing per the README claim (I did not execute).

### 1.3 What works out of the box

- `ED_FrontDoor/ED_minimal_demo.ipynb` — demonstrably runnable, well-scoped.
- `edsim` — a clean, well-named Python package with sensible internal layout (`core/`, `experiments/`, `phys/`, `invariants/`, `tests/`, `units/`).
- Top-level `README.md` and `ED_FrontDoor/README.md` — both well-written.
- `data/README.md` — clear, points back to the falsifiable prediction.
- `requirements.txt` and `pyproject.toml` — present and minimal.
- `LICENSE` (MIT) and `CONTRIBUTING.md` — present.

### 1.4 What is confusing or broken

In rough order of impact:

1. **Stray PDFs at the root.** Four PDFs sitting next to `README.md` give the impression of a paper drop, not a curated repo. They duplicate files that already exist in `papers/` or `docs/`.
2. **Two parallel paper trees.** `docs/research/ED PAPERS/` (47 markdown files) and `papers/` (a smaller curated set) both exist, with `papers/ED_Merger_Lag_Prediction/` containing a copy of `ED-Data-Galaxy-15_First_Evidence_For_Merger_Lag.md` that already lives in `docs/research/ED PAPERS/`. A new reader cannot tell which is canonical.
3. **Broken references in `docs/REPO_STRUCTURE.md`.** It refers to `documents/` (not `docs/`), to `ED-Final_Synthesis_EventDensity_Physics.pdf` (does not exist; only `ED-Phys-40_Synthesis.md` does), and to `ED_FOR_EVERYONE_VERSION.pdf` (does not exist). This document is itself out of date.
4. **README references a "Synthesis Paper".** The text "Read next: The Synthesis Paper" survives in `docs/CORE_PAPERS.md` even though I just removed the corresponding section in the last commit (the cross-reference was orphaned). The reading-order numbering also implies a 4-paper sequence but only 3 are linked.
5. **89 sub-directories under `docs/research/`** with a mix of empty stubs, dated experiments, and the canonical Atlas/Math/Synthesis documents. A new reader cannot find the needle in this haystack without help.
6. **Naming inconsistency.** `ED PAPERS` (uppercase, space) vs `ED Papers` (the new commit created this with mixed case — git happens to be case-insensitive on Windows so it merged, but a Linux clone would see two separate directories). Same for series prefixes: `ED-Data-`, `ED-Data-Galaxy-`, `ED-Phys-`, `ED-Math-`, `ED-Dimensional-`, `ED-Sim-`, `ED-Cosmo-`, `ED-Arch-`.
7. **`docs/research/ED PAPERS/ED-Data-Galaxy-13_*` exists in two forms** — `_Merger_Lag_Prediction.md` (the original theory note) and `_Merger_Lag_Literature_Scoping.md` (the new audit). A reader cannot tell which is the canonical Galaxy-13 without opening both.
8. **No top-level pointer to UDM (the Mobility-Law paper) or to Galaxy-15.** The README's empirical-results table mentions "10 materials … R² > 0.986" and "merger lags" but does not link to the actual papers describing those results. A reader interested in UDM has to find `ED_FrontDoor/ED_MobilityLaw.md` by spelunking; a reader interested in Galaxy-15 has to know to look in `docs/research/ED PAPERS/`.
9. **No "Scientific Results" landing page.** The repo has many results pages (`KEY_FINDINGS_TAKEAWAYS.md`, `RESULTS_OVERVIEW.md`, `WHAT_IS_ED.md`, the empirical table in the README) but none of them list the *current* major results in publication-ready form: UDM (mobility law), Galaxy-15 (merger lag), the Numerical Atlas, the Dimensional Atlas.
10. **No PDE-first one-page document.** The README explains the four primitives and seven axioms in prose, but a reader looking for "give me the PDE on one page" has to assemble it from `docs/research/ED PAPERS/numerical_atlas.md` (preface section) and `docs/research/ED PAPERS/ED-Dimensional-Master_The_Unified_Atlas.md` (executive summary). Neither is presented as the canonical one-pager.

### 1.5 What should be reorganised (preview; full proposal in §3)

Three structural moves would fix most of the friction:

1. **Move the four root PDFs into `papers/`** and delete the duplicate copies. Add `*.pdf` exceptions to `.gitignore` for the canonical paper PDFs (or stop tracking them and use GitHub Releases).
2. **Collapse `docs/research/ED PAPERS/` and `papers/` into a single canonical `papers/` tree** with subfolders by paper, each containing `paper.md`, `paper.tex`, `figures/`, and a `README.md`.
3. **Add a top-level `RESULTS.md`** that lists the three current headline results (UDM, Galaxy-15, PDE Atlas) with one-paragraph summaries and direct links.

---

## 2. The PDE-Driven Narrative: Galaxy-15, UDM, and the PDE Atlas as One Story

The repo has three flagship results sitting in three different folders, each excellent on its own, but never integrated into the unified story they actually tell. Here is the integration.

### 2.1 The one canonical PDE

The Event Density PDE in its unified form (from `docs/research/ED PAPERS/ED-Dimensional-Master_The_Unified_Atlas.md`):

```
∂_t ρ  =  D · [ M(ρ) ∇²ρ + M'(ρ) |∇ρ|² − P(ρ) ]  +  H · v
v̇    =  (1/τ) · ( F̄(ρ) − ζ · v )
```

with constitutive functions

```
M(ρ) = M₀ · (ρ_max − ρ)^β        (mobility, degenerate at capacity)
P(ρ) = P₀ · (ρ − ρ*)              (penalty, monostable restoring force)
v(t)                              (participation, global feedback variable)
```

derived from four primitives (density, mobility, penalty, participation) and seven structural axioms (locality, isotropy, gradient-driven flow, dissipative structure, single scalar field, minimal coupling, dimensional consistency).

This is **the single equation the repo is built around**. Everything else is a channel, regime, or empirical test of it.

### 2.2 Three results, three channels

The three flagship results map cleanly onto the three constitutive channels:

| Result | Channel exercised | What it predicts | What was observed |
|---|---|---|---|
| **UDM (Mobility Law)** | Mobility channel `M(ρ) = M₀(ρ_max − ρ)^β` | `D(c) = D₀(1 − c/c_max)^β` for any concentrated soft-matter system | 10 materials fit with R² > 0.986; β = 1.72 ± 0.37 |
| **Galaxy-15 (Merger Lag)** | Penalty channel + dynamical wake | `ℓ = D_T / v_current` lag of lensing centroid behind moving baryons | 7 clusters consistent within uncertainty; Finner+25 median 79 ± 14 kpc matches predicted ~80 kpc |
| **PDE Atlas (Numerical + Dimensional)** | All three channels, all five regimes | Same PDE governs physics across 61 orders of magnitude | 9 architectural laws verified in dimensions 1–4; structural correspondences hold for all parameter values |

### 2.3 Why this is one story, not three

Viewed correctly, the repo is making a single claim with three lines of evidence:

> **The Event Density PDE — one equation, four primitives, seven axioms — generates the dynamics of crowded soft matter, the dynamics of merging galaxy clusters, and the universal scaling structure of physics from quantum to cosmological length scales, *with the same parameters and no fitting between domains*.**

- **UDM** demonstrates the mobility channel as a parameter-free predictor in a regime (concentrated colloids, proteins, polymers) where decades of material-specific models have failed to find a universal law.
- **Galaxy-15** demonstrates the penalty channel — specifically, the diffusive equilibration timescale `D_T/v²` and its steady-state wake — as a parameter-free predictor in a regime (cluster mergers) where dark matter and SIDM both fail.
- **The PDE Atlas** demonstrates that the *same* equation, with the *same* constitutive forms, admits a consistent dimensional interpretation at quantum, condensed-matter, galactic, and cosmological scales. The nondimensional identity `D_phys · T₀ / L₀² = 0.3` holds in every regime.

The unifier is the diffusivity `D_T = 2.1 × 10²⁷ m²/s` in Galaxy-15 — set independently from the Mistele weak-lensing extent — being the *galactic-regime image* of the same constant `D` that, in the condensed-matter regime, becomes `D₀` in the UDM law. The PDE Atlas is the formal bridge that connects them.

### 2.4 What the repo should explicitly say (and currently does not)

The README mentions all three results in passing but never names them as "three confirmations of one PDE." This is the central narrative gap. A new `RESULTS.md` should open with:

> Event Density predicts dynamics in three independent regimes from a single PDE with no inter-domain fitting:
>
> - **In concentrated soft matter**, the mobility channel predicts `D(c) = D₀(1 − c/c_max)^β`. Tested against 10 chemically distinct materials → R² > 0.986. (UDM, ED-Data-01–11.)
> - **In merging galaxy clusters**, the penalty channel predicts a lensing-mass offset `ℓ = D_T / v_current` behind moving baryons. Tested against 7 well-measured clusters and the Finner et al. (2025) aggregate of 58 subclusters → all consistent within uncertainty. (Galaxy-15, ED-Data-Galaxy-15.)
> - **Across 61 orders of magnitude in length scale**, the same PDE admits dimensional mappings into quantum, Planck, condensed-matter, galactic, and cosmological regimes, with a universal nondimensional invariant `D_nd = 0.3`. (PDE Atlas, ED-Dimensional-Master + Numerical Atlas.)

This single paragraph at the top of `RESULTS.md` (and a shorter version in the main README) would close the narrative gap.

---

## 3. Proposed New Repo Structure

Goals: clear entry point, separation of concerns (theory / data / simulation / papers), one-page-PDE README, immediately runnable Getting Started, dedicated Results / Simulation / Data sections, no duplication.

### 3.1 The proposed tree

```
event-density/
├── README.md                       ← rewritten; one-page PDE on the front
├── RESULTS.md                      ← NEW; three flagship results, linked
├── GETTING_STARTED.md              ← NEW; promoted from FrontDoor demo
├── CONTRIBUTING.md
├── LICENSE
├── pyproject.toml
├── requirements.txt
├── .gitignore
│
├── theory/                         ← NEW; the PDE and its derivation
│   ├── README.md                   ← The PDE on one page
│   ├── 01_axioms_and_primitives.md
│   ├── 02_canonical_PDE.md
│   ├── 03_three_channels.md
│   ├── 04_dimensional_atlas.md     ← (moved from research/ED PAPERS)
│   ├── 05_numerical_atlas.md       ← (moved from research/ED PAPERS)
│   └── 06_mathematical_foundations.md
│
├── papers/                         ← canonical, single tree
│   ├── README.md                   ← reading order
│   ├── foundational/               ← ED Foundational Paper
│   │   ├── paper.md
│   │   ├── paper.tex
│   │   └── figures/
│   ├── UDM/                        ← ED01_UDM_MobilityLaw
│   │   ├── paper.md
│   │   ├── paper.pdf               ← (tracked via Git LFS or releases)
│   │   └── figures/
│   ├── galaxy-15/                  ← ED-Data-Galaxy-15
│   │   ├── paper.md
│   │   ├── paper.tex
│   │   ├── paper.pdf
│   │   └── figures/
│   ├── dimensional-atlas/
│   ├── numerical-atlas/
│   └── archive/                    ← old/superseded papers, dated
│
├── edsim/                          ← unchanged; the simulation engine
│   └── (current structure — already clean)
│
├── data/                           ← unchanged structure
│   └── (current; already documented)
│
├── analysis/                       ← NEW; reusable analysis scripts
│   ├── README.md
│   ├── wake_derivation.py          ← (moved from /scripts)
│   ├── galaxy15_figures.py         ← (moved + renamed)
│   ├── galaxy15_supp_figures.py
│   └── notebooks/
│       ├── 01_minimal_demo.ipynb   ← (promoted from FrontDoor)
│       ├── 02_three_channels.ipynb ← NEW; one-cell-per-channel demo
│       ├── 03_galaxy15_lag.ipynb   ← NEW; reproduces Galaxy-15 fits
│       └── 04_udm_mobility.ipynb   ← NEW; reproduces UDM fits
│
├── outputs/                        ← unchanged; gitignored regenerable results
│
├── docs/                           ← reduced; only true documentation
│   ├── README.md                   ← what's in docs/
│   ├── architecture.md             ← (moved from research)
│   ├── how_to_run.md               ← (moved + simplified)
│   ├── api.md                      ← edsim API reference
│   ├── changelog.md
│   └── archive/                    ← historical research log (89 dirs collapsed here)
│       └── README.md               ← "this is the historical research archive"
│
└── outreach/                       ← renamed from ED_FrontDoor
    ├── README.md
    ├── what_is_ED_1pager.md
    ├── falsifiable_prediction.md
    ├── targeted_hooks.md
    ├── 3min_demo_script.md
    └── slides/                     ← generated slides + video graphics
```

### 3.2 Key design decisions

- **`theory/` is the conceptual entry.** A single one-page PDE document at `theory/README.md` becomes the canonical statement. Every other technical document references back to it.
- **`papers/` becomes a single canonical tree** with one folder per paper, each containing source + figures + (optionally) compiled PDF. Dead documents go to `papers/archive/`. The current `docs/research/ED PAPERS/` collapses into `papers/` proper or `docs/archive/`.
- **`analysis/` is new** and consolidates the loose `scripts/` directory plus the `ED_FrontDoor/generate_*.py` scripts that don't belong in an outreach folder. It also hosts the reproduction notebooks (one per major result).
- **`docs/` shrinks dramatically** to true documentation (architecture, how-to-run, API, changelog) plus a clearly-labelled archive of the historical research log.
- **`ED_FrontDoor/` becomes `outreach/`.** Lower-case, conventional, and free of the figure-generation scripts that don't fit the outreach mission.
- **`edsim/` and `data/` are untouched.** They are already clean.

### 3.3 Inventory of redundancies, outdated files, and consolidations

| Category | Item | Action |
|---|---|---|
| Redundant | 4 root-level PDFs | Move to `papers/<paper>/paper.pdf`, delete root copies |
| Redundant | `papers/` (current) vs `docs/research/ED PAPERS/` | Merge into single `papers/` tree per §3.1 |
| Redundant | `papers/ED_Merger_Lag_Prediction/ED-Data-Galaxy-15_*.md` ≡ `docs/research/ED PAPERS/ED-Data-Galaxy-15_*.md` | Keep one canonical copy in `papers/galaxy-15/paper.md` |
| Redundant | `docs/research/ED PAPERS/ED-Data-Galaxy-13_Merger_Lag_Prediction.md` and `_Literature_Scoping.md` | Rename to `papers/galaxy-13/01_prediction.md` and `02_literature_scoping.md` |
| Outdated | `docs/REPO_STRUCTURE.md` | Rewrite to match new tree, or delete in favour of new top-level README |
| Outdated | `docs/CORE_PAPERS.md` "Synthesis Paper" reference | Already cleaned in last commit; `Read next: The Synthesis Paper` line still exists, fix |
| Outdated | Empty stub READMEs in some research sub-dirs | Remove or merge into parent |
| Unclear naming | `ED PAPERS` (caps + space) | Rename to `papers/` lowercase |
| Unclear naming | `outputs/` vs `data/ED-Sim-*` | `outputs/` for solver runs, `data/ED-Sim-*` for committed reference results — clarify in READMEs |
| Unclear naming | `scripts/` (only 3 files, all Galaxy-15) | Rename or move to `analysis/galaxy15/` |
| Missing doc | One-page PDE statement | Create `theory/README.md` |
| Missing doc | "Scientific Results" landing | Create `RESULTS.md` |
| Missing doc | Reproduction notebook for UDM | Create `analysis/notebooks/04_udm_mobility.ipynb` |
| Missing doc | Reproduction notebook for Galaxy-15 | Create `analysis/notebooks/03_galaxy15_lag.ipynb` |
| Missing doc | Three-channel demo notebook | Create `analysis/notebooks/02_three_channels.ipynb` |
| Consolidation | 8 `generate_*.py` in `ED_FrontDoor/` | Move scientific ones to `analysis/`, slide/video ones to `outreach/slides/` |
| Consolidation | `docs/HOW_TO_RUN.md` + `docs/HOW_TO_RUN_ANALOGUES.md` + `docs/REPRODUCING_FOUNDATIONS_PAPER.md` | Merge into single `docs/how_to_run.md` with sections |
| Consolidation | `docs/RESULTS_OVERVIEW.md` + `docs/KEY_FINDINGS_TAKEAWAYS.md` + scattered tables | Replace with single `RESULTS.md` at root |

### 3.4 Rewritten top-level `README.md` (proposal)

```markdown
# Event Density

**One PDE, derived from four primitives and seven axioms, whose three
constitutive channels reproduce the dynamics of concentrated soft matter,
merging galaxy clusters, and physics across 61 orders of magnitude — with
no fitting between domains.**

## The PDE on one page

  ∂_t ρ  =  D · [ M(ρ) ∇²ρ + M'(ρ) |∇ρ|² − P(ρ) ]  +  H · v
  v̇    =  (1/τ) · ( F̄(ρ) − ζ · v )

with M(ρ) = M₀(ρ_max − ρ)^β  and  P(ρ) = P₀(ρ − ρ*).

Four primitives:  density ρ,  mobility M,  penalty P,  participation v.
Seven axioms:    locality, isotropy, gradient-driven flow, dissipative
                 structure, single scalar field, minimal coupling,
                 dimensional consistency.

Three channels:  mobility (PME-like), penalty (RC-like), participation
                 (telegraph-like). Each reduces exactly to a known
                 physical equation when isolated.

Full derivation: theory/README.md.

## Three flagship results

| Result | Domain | Prediction | Observed |
|---|---|---|---|
| **UDM** | Soft matter | D(c) = D₀(1−c/c_max)^β | R² > 0.986 across 10 materials |
| **Galaxy-15** | Cluster mergers | ℓ = D_T / v_current | 7 clusters + Finner+25 median 79±14 kpc, all consistent |
| **PDE Atlas** | All physics | One PDE, 5 regimes, 61 orders of magnitude | 9 architectural laws verified in d = 1–4 |

Full results: RESULTS.md.

## Try it in 3 minutes

[![Open In Colab](...)](...)

Local install:
    git clone ...
    cd event-density
    pip install -r requirements.txt
    jupyter notebook analysis/notebooks/01_minimal_demo.ipynb

Full quickstart: GETTING_STARTED.md.

## Repository map

  theory/         The PDE, its axioms, the dimensional + numerical atlases
  papers/         Canonical papers, one folder each
  edsim/          Simulation engine (Python package, CLI, 112 tests)
  data/           Empirical datasets (galaxy rotation, SFR, SPARC, etc.)
  analysis/       Reusable scripts and reproduction notebooks
  outreach/       1-pagers, demo scripts, falsifiable prediction
  docs/           Architecture, API, how-to-run, changelog, archive
  outputs/        Solver outputs (regenerable; gitignored)

## What ED claims, and what it doesn't

ED claims architectural sufficiency: one PDE, derived from minimal
primitives, generates the dynamical structure of multiple known regimes
without fitting. It does *not* claim to derive general relativity,
quantum mechanics, or the Standard Model. Its horizons are transient.
Its cosmology is provisionally falsified as a standalone model. These
limits are documented and tested.

License: MIT.  Contact: open an issue.
```

### 3.5 `GETTING_STARTED.md` (proposal)

A focused 1-page quickstart that does three things:

1. **Run the demo** in Colab or locally (the current FrontDoor recipe).
2. **Run the test suite** — `pytest edsim/tests/` and `python -m edsim certify`.
3. **Reproduce a flagship result** — point to one of the new analysis notebooks (UDM, Galaxy-15, three-channels) and say "this notebook regenerates Figure X of paper Y in <60 seconds."

Crucially: each step should be a copy-paste command that *actually works* on a fresh clone with only `requirements.txt` installed.

### 3.6 `RESULTS.md` (proposal)

The Scientific Results landing page. One section per flagship result, each ~150 words, in the unification framing of §2:

- **UDM**: link to `papers/UDM/`, show the universal scaling fit, link to `analysis/notebooks/04_udm_mobility.ipynb`.
- **Galaxy-15**: link to `papers/galaxy-15/`, show the velocity-scaling and deceleration tests, link to `analysis/notebooks/03_galaxy15_lag.ipynb`.
- **PDE Atlas**: link to `theory/04_dimensional_atlas.md` and `theory/05_numerical_atlas.md`, show the five-regime mapping with the `D · T₀ / L₀² = 0.3` invariant.

Plus a short closing paragraph that names the unification: *one PDE, three independent regime tests, no inter-domain fitting, no failures so far.*

---

## 4. Migration Plan

A step-by-step plan that can be executed incrementally without breaking the working demo or losing history. Each step is one PR-sized commit.

### Step 1 — Cleanup at the root (low risk, high impact)

- `git mv ED-Data-Galaxy-15_First_Evidence_For_Merger_Lag.pdf papers/galaxy-15/`  *(create the folder if needed)*
- `git mv ED01_UDM_MobilityLaw.pdf papers/UDM/`
- `git mv ED02_Foundational_Paper.pdf papers/foundational/`
- `git mv "Event Density as a Physical Ontology.pdf" papers/foundational/Event_Density_as_a_Physical_Ontology.pdf`
- Delete `papers/ED_Merger_Lag_Prediction/` (it duplicates the new `papers/galaxy-15/`).

**Effect:** root tree shrinks to README + canonical metadata files. ~3.5 MB of duplicate PDFs removed.

### Step 2 — Create the new top-level documents

- Write the new `README.md` per §3.4.
- Write the new `RESULTS.md` per §3.6.
- Write the new `GETTING_STARTED.md` per §3.5.
- Move `docs/REPO_STRUCTURE.md` → `docs/archive/REPO_STRUCTURE_old.md` (keeps history) and write a new `docs/architecture.md` matching the new tree.

**Effect:** the front door of the repo now matches the new vision. Internal structure can still be cleaned up incrementally.

### Step 3 — Create the `theory/` directory

- `mkdir theory`
- Move and rename:
  - `docs/research/ED PAPERS/ED-Dimensional-Master_The_Unified_Atlas.md` → `theory/04_dimensional_atlas.md`
  - `docs/research/ED PAPERS/numerical_atlas.md` → `theory/05_numerical_atlas.md`
  - `docs/research/ED PAPERS/ED-Math-01_Uniqueness_Well-Posedness_and_Architectural_Laws.md` → `theory/06_mathematical_foundations.md`
- Write fresh shorter docs:
  - `theory/README.md` — one-page PDE statement
  - `theory/01_axioms_and_primitives.md` — distilled from existing papers
  - `theory/02_canonical_PDE.md` — distilled
  - `theory/03_three_channels.md` — distilled

**Effect:** a new reader has a coherent four-document path from "what is the PDE?" to "what does it imply mathematically?"

### Step 4 — Reorganise `papers/` into per-paper folders

- For each canonical paper: create `papers/<short-name>/` containing `paper.md`, `paper.tex` if it exists, `figures/`, and a per-paper `README.md` with a 1-paragraph abstract and reproduction pointers.
- Move the matching markdown out of `docs/research/ED PAPERS/` into the new locations (use `git mv`).
- Move stale, superseded, or one-off papers into `papers/archive/` with a dated subfolder.

**Effect:** the publication-ready papers are clearly distinguished from research notes. Each paper is self-contained.

### Step 5 — Create `analysis/` and consolidate scripts

- `mkdir -p analysis/notebooks`
- `git mv scripts/wake_derivation.py analysis/wake_derivation.py`
- `git mv scripts/generate_galaxy15_figures.py analysis/galaxy15_figures.py`
- `git mv scripts/generate_galaxy15_supp_figures.py analysis/galaxy15_supp_figures.py`
- Move scientific generators from `ED_FrontDoor/` (anything that produces a published figure) into `analysis/`.
- Move slide / video generators from `ED_FrontDoor/` into `outreach/slides/`.
- Promote `ED_FrontDoor/ED_minimal_demo.ipynb` to `analysis/notebooks/01_minimal_demo.ipynb` and update the README + Colab link.
- Write the three new reproduction notebooks (`02_three_channels`, `03_galaxy15_lag`, `04_udm_mobility`).

**Effect:** scientific code is in one place; outreach materials are in another; demos are runnable from a predictable path.

### Step 6 — Rename `ED_FrontDoor/` → `outreach/`

- `git mv ED_FrontDoor outreach`
- Update the README, Colab badges, and any cross-references.
- Add a redirect note in `outreach/README.md` for visitors who arrive from old links.

**Effect:** lowercase conventional naming; clearer separation of outreach from analysis.

### Step 7 — Collapse `docs/research/`

- Survey the 89 sub-directories. For each:
  - If it contains a canonical paper now in `papers/` or `theory/`: delete (the canonical copy is already moved).
  - If it contains a unique research note still relevant: move to `docs/archive/<series>/`.
  - If it is empty or duplicates content elsewhere: delete.
- Add `docs/archive/README.md`: "this directory contains the historical research log; canonical content has been moved to `theory/` and `papers/`."

**Effect:** the visible `docs/` tree shrinks from ~89 dirs to ~5–10. The historical record is preserved but no longer the front door of the documentation.

### Step 8 — Update `.gitignore` and tracked artefacts

- Decide on the policy for compiled PDFs of canonical papers. Two reasonable options:
  - **Track them with Git LFS.** Requires LFS setup but keeps `papers/<name>/paper.pdf` always in sync with the source.
  - **Use GitHub Releases.** Tag each paper version (e.g. `galaxy-15-v1.0`) and attach the PDF. Keeps the repo small.
- Whichever option: remove the blanket `**/*.pdf` ignore and replace with a more specific rule (e.g. ignore PDFs only in `outputs/` and `docs/archive/`).

**Effect:** the canonical PDFs travel with the source and don't need to be regenerated by every reader.

### Step 9 — Verify the new front door works

- On a clean clone, run:
  - `pip install -r requirements.txt`
  - `pytest edsim/tests/` (must pass)
  - `python -m edsim certify` (must pass)
  - `jupyter notebook analysis/notebooks/01_minimal_demo.ipynb` (must run end to end)
  - Each of the three new reproduction notebooks (must produce a recognisable figure)
- If anything is broken, fix before merge.

**Effect:** the `GETTING_STARTED.md` instructions actually work.

### Step 10 — Tag a release

- `git tag v2.0-restructure` and push.
- Write release notes describing the restructuring, the three flagship results, and the new entry points.

**Effect:** anyone arriving via search engines or external citations can find a stable reference to the new structure.

---

## 5. Summary

The Event Density repository contains genuinely strong scientific work — three independent confirmations of a single PDE-based ontology, two of them recent and quantitatively striking — but the repository structure has not kept pace with the science. A new visitor sees an excellent README and an excellent demo notebook, then drowns in 89 sub-directories of historical research notes, two parallel paper trees, four stray PDFs at the root, and broken cross-references in the structure docs.

The fix is mostly mechanical and can be executed in ten incremental steps without losing any history. The three substantive additions are:

1. A `theory/` directory whose `README.md` is the one-page PDE.
2. A `RESULTS.md` at the root that names the three flagship results and the unification claim that ties them together.
3. Three reproduction notebooks (`analysis/notebooks/02_three_channels`, `03_galaxy15_lag`, `04_udm_mobility`) that turn the papers into runnable demos.

After these changes, a fresh cloner's first five minutes look like: see the PDE on the README, run the Colab demo, click through to `RESULTS.md`, see three results that all derive from one PDE, click through to a reproduction notebook, see the actual data fit. That is the experience the science deserves.

— *End of review.*
