# docs/

True documentation for the Event Density repository: architecture, API reference, changelog, and the architectural-review record of the v2.0 reorganisation.

## Contents

| File | Purpose |
|------|---------|
| [`architecture.md`](architecture.md) | The five-layer architecture of the `edsim` simulation engine |
| [`api.md`](api.md) | High-level API reference for the key classes and functions in `edsim` |
| [`CHANGELOG.md`](CHANGELOG.md) | Versioned changelog for the project |
| [`ARCHITECTURAL_REVIEW.md`](ARCHITECTURAL_REVIEW.md) | The repository-level architectural review that motivated the v2.0 reorganisation |

## Where everything else went

The historical research log, manuscript drafts, and pre-v2.0 summary documents have been relocated into [`/archive/`](../archive/) as part of the v2.0 reorganisation. Specifically:

| Old location | New location |
|--------------|--------------|
| `docs/research/` (10 sub-directories, ~250 files) | [`/archive/research_history/`](../archive/research_history/) |
| `docs/manuscript/` (27 analogue and physics reports) | [`/archive/docs_legacy/manuscript/`](../archive/docs_legacy/manuscript/) |
| `docs/CORE_PAPERS.md`, `docs/RESULTS_OVERVIEW.md`, `docs/KEY_FINDINGS_TAKEAWAYS.md`, `docs/WHAT_IS_ED.md`, `docs/REPO_STRUCTURE.md`, `docs/REPRODUCING_FOUNDATIONS_PAPER.md`, `docs/HOW_TO_RUN*.md`, `docs/index.md`, `docs/comparison.md`, `docs/math.md`, `docs/performance.md`, `docs/regimes.md`, `docs/roadmap.md`, `docs/units.md`, `docs/usage.md`, `docs/phys_*.md` (10 files) | [`/archive/docs_legacy/`](../archive/docs_legacy/) |
| `docs/ED_ArXiv_MobilityLaw.pdf` | [`/archive/docs_legacy/ED_ArXiv_MobilityLaw.pdf`](../archive/docs_legacy/ED_ArXiv_MobilityLaw.pdf) (canonical: [`/papers/Universal_Mobility_Law/paper.pdf`](../papers/Universal_Mobility_Law/paper.pdf)) |

The functional content of those documents has either been:

- **Replaced by the new top-level documents** ([`/README.md`](../README.md), [`/RESULTS.md`](../RESULTS.md), [`/GETTING_STARTED.md`](../GETTING_STARTED.md)),
- **Promoted into the canonical theory** ([`/theory/PDE.md`](../theory/PDE.md)) and **canonical papers** ([`/papers/`](../papers/)),
- Or **preserved as historical research** in the archive without being canonical for current claims.

## Where to start, by audience

- **New visitor:** start with [`/README.md`](../README.md), then click through to [`/RESULTS.md`](../RESULTS.md) and [`/GETTING_STARTED.md`](../GETTING_STARTED.md).
- **Want to read the canonical theory:** [`/theory/PDE.md`](../theory/PDE.md), then [`/papers/Foundations_of_Event_Density/`](../papers/Foundations_of_Event_Density/).
- **Want to reproduce a result:** [`/analysis/notebooks/`](../analysis/notebooks/) or [`/analysis/scripts/`](../analysis/scripts/).
- **Want to use the simulation engine:** [`architecture.md`](architecture.md) for layout, [`api.md`](api.md) for the API reference.
- **Want the historical research log:** [`/archive/research_history/`](../archive/research_history/).
