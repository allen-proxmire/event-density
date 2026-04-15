# archive/

The archival layer of the Event Density repository. Everything here was canonical at some point in the project's history but is no longer the authoritative source for any current claim. Material is preserved for provenance, traceability, and future reference.

**Nothing in `archive/` should be cited as the authority for any present claim.** Citations should always point to the canonical locations:

- The canonical PDE: [`/theory/PDE.md`](../theory/PDE.md)
- The canonical papers: [`/papers/`](../papers/) (one folder per paper)
- The canonical empirical results overview: [`/RESULTS.md`](../RESULTS.md)
- The canonical reproduction notebooks: [`/analysis/notebooks/`](../analysis/notebooks/)

If a document in `archive/` is in conflict with a canonical document, the canonical document wins.

## Contents

```
archive/
├── README.md                       ← you are here
│
├── research_history/               ← the historical research log (formerly docs/research/)
│   ├── ED Architecture/            ← 13 architectural-analysis notes
│   ├── ED Collaboration/           ← collaboration kits and outreach drafts
│   ├── ED Cosmology/               ← early cosmology series notes
│   ├── ED Data/                    ← early data-pipeline notes
│   ├── ED Experiments/             ← experiment design notes
│   ├── ED Interpretations/         ← interpretation papers (PDFs)
│   ├── ED PAPERS/                  ← legacy paper drafts and supporting notes
│   ├── ED Physics/                 ← ED-Phys series (~112 files)
│   ├── ED Simulation/              ← simulation-architecture history (ED-Sim-01)
│   ├── ED Validation/              ← validation records
│   ├── FactorSkyline_Evaluation_EventDensity.md
│   ├── archive_index.md
│   └── research_README.md
│
└── docs_legacy/                    ← pre-v2.0 top-level docs
    ├── manuscript/                 ← analogue and physics reports
    ├── CORE_PAPERS.md              ← superseded by /papers/ tree + per-paper READMEs
    ├── RESULTS_OVERVIEW.md         ← superseded by /RESULTS.md
    ├── KEY_FINDINGS_TAKEAWAYS.md   ← superseded by /RESULTS.md
    ├── WHAT_IS_ED.md               ← superseded by /README.md
    ├── REPO_STRUCTURE.md           ← superseded by /README.md repo map
    ├── REPRODUCING_FOUNDATIONS_PAPER.md  ← superseded by /GETTING_STARTED.md
    ├── HOW_TO_RUN.md               ← superseded by /GETTING_STARTED.md
    ├── HOW_TO_RUN_ANALOGUES.md     ← superseded by /GETTING_STARTED.md + per-notebook docs
    ├── ED_ArXiv_MobilityLaw.pdf    ← duplicate of /papers/Universal_Mobility_Law/paper.pdf
    ├── index.md, comparison.md, math.md, performance.md, regimes.md,
    │   roadmap.md, units.md, usage.md  ← reference notes superseded by /theory/ and /papers/
    └── phys_*.md                   ← 10 physics regime notes superseded by /papers/Dimensional_Atlas/
```

## Why these files were not deleted

Two reasons:

1. **Provenance.** Several of these files were the source material from which the canonical documents in `/theory/`, `/papers/`, and the new top-level documents were extracted. Keeping them lets a reader trace exactly where a current claim originated.

2. **Future reference.** Some of the research-history notes contain analyses, intermediate results, or proposed experiments that are not (yet) part of the canonical record but may become so. Examples include the architectural-symmetry note (`ED Architecture/ED-Arch-09_*`), several `ED-Phys-*` series notes that explore parameter regions, and the `ED Collaboration` outreach drafts.

If you find a file in `archive/` whose content should be elevated into the canonical layer (for example, an analysis that resolves an open question), please open an issue and propose its promotion to the appropriate canonical location.

## What is *not* here

The local-only staging directory [`/Remove from Repo/`](../Remove%20from%20Repo/) (gitignored) is the throwaway-pile for genuine duplicates and superseded build artefacts. The `archive/` here is a *committed* preservation layer; the staging directory is a *transient* triage layer.
