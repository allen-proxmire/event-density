# Repository Structure

```
Event Density/
│
├── README.md                          Top-level overview (start here)
├── WHAT_IS_ED.md                      Conceptual overview of the ontology
├── KEY_FINDINGS_TAKEAWAYS.md          Summary of all findings
├── REPRODUCING_FOUNDATIONS_PAPER.md    Step-by-step reproduction guide
│
├── documents/                         All written output (unified)
│   ├── README.md                      Deep-dive: what ED is and does
│   ├── CORE_PAPERS.md                 Canonical papers in reading order
│   ├── RESULTS_OVERVIEW.md            Empirical results summary
│   ├── HOW_TO_RUN.md                  Reproduction instructions
│   ├── REPO_STRUCTURE.md              This file
│   ├── units.md                       Nondimensionalization scheme
│   │
│   ├── manuscript/                    Published papers and reports
│   │   ├── foundational_paper/        The Foundational Paper (.md + .tex)
│   │   ├── ED-SIM-02.md              Solver architecture document
│   │   ├── ED-SIM-3D_...md           2D/3D extension and invariant mini-atlas
│   │   └── ED-Analogue-*.md          Individual analogue reports (01–09)
│   │
│   └── research/                      Research archive
│       ├── ED PAPERS/                 Core research notes (49 files)
│       │   ├── ED-Final_Synthesis_*   Capstone synthesis paper (.md + .pdf + .tex)
│       │   ├── ED-Math-01_*           Mathematical foundations
│       │   ├── ED-Dimensional-*       Five regime mappings + master atlas
│       │   ├── ED-Data-01 – 11        Condensed-matter data pipeline
│       │   └── ED-Data-Galaxy-01 – 13 Galaxy-scale data pipeline
│       ├── ED Interpretations/        31 interpretation papers (PDFs)
│       ├── ED Architecture/           Architectural analysis (12 notes)
│       ├── ED Experiments/            Experiment notes + SPARC data
│       ├── ED Physics/                ED-Phys series
│       ├── ED Simulation/             Simulation architecture
│       └── ED Validation/             Validation records
│
├── edsim/                             ED-SIM-02 simulation platform
│   ├── core/                          Core PDE solver
│   │   ├── parameters.py             Parameter dataclass
│   │   ├── operators.py              Spatial operators (2D/3D/4D)
│   │   ├── boundary.py               Boundary conditions
│   │   ├── constitutive.py           Mobility and penalty functions
│   │   ├── participation.py          Participation ODE
│   │   └── integrators/              Time integration (implicit Euler, ETD-RK4)
│   ├── phys/                          Physics experiments
│   │   └── analogues/                The six foundational analogues + 3D extensions
│   ├── units/                         Dimensional mapping
│   │   ├── constants.py              Physical constants (CODATA 2018)
│   │   ├── scales.py                 Scale factories (quantum, Planck, galactic, ...)
│   │   └── mapping.py                ED ↔ SI conversion functions
│   ├── invariants/                    Invariant atlas engine
│   ├── tests/                         112 pytest tests
│   └── reproducibility/               Certification pipeline (9 phases)
│
└── examples/                          Example notebooks and scripts
```

## Where to Start

| If you want to... | Start here |
|:-------------------|:----------|
| Understand what ED is | [`documents/README.md`](README.md) |
| Read the papers in order | [`documents/CORE_PAPERS.md`](CORE_PAPERS.md) |
| See the empirical results | [`documents/RESULTS_OVERVIEW.md`](RESULTS_OVERVIEW.md) |
| Run experiments | [`documents/HOW_TO_RUN.md`](HOW_TO_RUN.md) |
| Understand the code | [`edsim/README.md`](../edsim/README.md) |
| Read the synthesis paper | [`documents/research/ED PAPERS/ED-Final_Synthesis_EventDensity_Physics.pdf`](research/ED%20PAPERS/ED-Final_Synthesis_EventDensity_Physics.pdf) |
| Understand ED without math | [`documents/research/ED PAPERS/ED_FOR_EVERYONE_VERSION.pdf`](research/ED%20PAPERS/ED_FOR_EVERYONE_VERSION.pdf) |

## Key Research Series

| Series | Notes | Focus |
|:-------|:------|:------|
| **ED-Data** (01–11) | 11 notes | Condensed-matter mobility law, three-material test, front exponents |
| **ED-Data-Galaxy** (01–13) | 13 notes | Halo edges, dwarf fits, NGC 3198, weak lensing, BTFR, merger lags |
| **ED-Dimensional** (01–05 + Master) | 6 notes | Quantum, Planck, condensed matter, galactic, cosmological regime mappings |
| **ED-Math** (01) | 1 note | Uniqueness theorem, well-posedness, architectural laws |
| **ED-SIM-3D** | 1 note | 2D/3D solver extension, five invariant tests |
