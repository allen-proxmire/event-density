# ED PAPERS

The publication-grade deliverables of the Event Density research program.

This folder collects the core papers, technical appendices, and extended
specifications that constitute the formal scientific output of the ED
program. Each document is either a self-contained paper (PDF) or a
complete technical specification (Markdown) written in journal-ready
or monograph-ready style.

---

## Role in the ED Program

Every other folder in the repository supports the work collected here.
The Architecture defines the principles. The Physics pipeline explores
the dynamics. The Validation tests confirm the signatures. The Simulation
engine computes the invariants. The Experiments folder designs the
empirical tests. This folder is where those results become papers.

The documents form a logical arc:

1. **Canon** — defines the seven principles.
2. **UCE** — derives the cosmological equation.
3. **Foundations** — proves the mathematics (Appendices C and D).
4. **Applications** — derives nineteen falsifiable predictions.
5. **Scale Correspondence** — establishes the scaling framework.
6. **Numerical Atlas** — documents the computational demonstrations.
7. **Simulation Suite** — specifies the full ED-SIM pipeline.
8. **Monograph** — unifies everything into a single self-contained book.

---

## Papers

### The Architectural Canon of the Unified ED Cosmology PDE
**`The Architectural Canon of the Unified ED Cosmology PDE.pdf`**

The foundational paper. Defines the seven irreducible structural
principles (P1–P7) that uniquely characterize the ED architecture.
Establishes that the canonical PDE is the unique equation satisfying all
seven principles simultaneously and that any dynamical system satisfying
them belongs to the universality class U_ED.

### The Unified Cosmological Equation of Event Density
**`The Unified Cosmological Equation of Event Density.pdf`**

Derives the ED cosmological dynamics from the canonical operator. Shows
how the architecture reproduces inflation-like smoothing, structure
formation, expansion, and late-time flattening without geometry, fields,
or curvature. The UCE is the physical instantiation of the seven
principles.

### Event Density Canon Foundations (Rigour Paper)
**`Event Density Canon Foundations.pdf`**

Places the Architectural Canon on rigorous mathematical footing. The
central results are in the appendices (see below): global existence and
uniqueness of solutions, linearized spectral analysis, nonlinear stability,
bifurcation structure, long-time convergence, and the universality class
closure theorems.

### Physical Applications of the Event Density Architecture
**`applications_paper.md`** — 1,395 lines

Derives nineteen concrete, falsifiable physical predictions from the
canonical principles across five domains: quantum mechanics (7 predictions),
galactic dynamics (10), condensed matter (8), photonics, and phononics (2).
Each prediction is traced to specific theorems in Appendix C, contrasted
with standard-theory expectations, and equipped with a falsification
condition. One prediction (dwarf galaxy rotation curves) has been tested
and confirmed.

### Scale Correspondence in Event Density
**`Scale‑Correspondence in Event Density.pdf`**

Develops the scaling framework that connects the canonical PDE across
physical scales. Establishes how the architectural invariants transform
under rescaling and how systems at different scales can be compared
within U_ED.

### Numerical Atlas
**`numerical_atlas.md`** — 3,767 lines

The complete computational companion to the Rigour Paper. Documents
forty-five figures demonstrating every theorem and proposition of
Appendices C and D through direct numerical simulation: regime geometry,
modal hierarchy, triad coupling, complexity dynamics, horizon behavior,
three-stage convergence, regime transitions, and cross-domain analogues.
Includes full pseudocode, parameter tables, and reproducibility
specifications.

### Simulation Suite Specification
**`simulation_suite.md`** — 13,133 lines

The definitive technical specification for ED-SIM v1. Covers the
canonical PDE restatement, data structures, spatial and temporal
discretization, boundary conditions, mobility collapse handling,
positivity enforcement, stability constraints, initialization, time
loop structure, output formats, checkpointing, error handling,
convergence testing, experiment templates, parameter sweeps,
parallelization, observables (energy, dissipation channels, modal
amplitudes, triad coefficients, complexity, convergence rates, horizon
proximity), output formats (time series, spectral data, figure data,
metadata), versioning, reproducibility (seed control, environment capture,
manifests), validation tests (linear, nonlinear, triad, horizon,
three-stage), implementation notes (Python, Julia, MATLAB), performance
tuning, memory management, and planned extensions (GPU, AMR, higher-order
schemes, multi-domain, stochastic perturbations).

### The ED Monograph
**`The ED Monograph.pdf`**

The unified mathematical treatment. Integrates the Canon, Rigour Paper,
Applications Paper, Invariant Atlas, and Simulation Suite into a single
self-contained book in six parts: Foundations, Invariants, Computation,
Synthesis, Reproducibility, and Outlook. The Markdown and LaTeX source
files (`ed_monograph.md`, `ed_monograph.tex`, `ed_references.bib`) are
located in `ED Simulation/` because they document the simulation results
and are maintained alongside the code that generates the figures.

---

## Appendices

The `ED_Canon Foundation Appendices/` subdirectory contains the extended
appendices for the Canon Foundations paper, written as self-contained
Markdown documents.

| Appendix | Title | Content |
|----------|-------|---------|
| A | Proofs of Independence Results | Demonstrates that each of the seven principles is independent: removing any one permits a system that satisfies the remaining six but not the full architecture. |
| B | Proofs of Sufficiency Results | Demonstrates that the seven principles together are sufficient to determine the canonical PDE uniquely. |
| C | PDE Analysis | The mathematical core: local existence (C.1), global existence (C.2), linearization and eigenstructure (C.3), spectral analysis (C.4), stability (C.5), bifurcation structure (C.6), and long-time behavior (C.7). 2,409 lines. |
| D | Universality Class | Formal definition of ED-equivalence, the universality class U_ED, closure theorems (rescaling, constitutive perturbation, domain changes), invariance theorems (discriminant, regime geometry, modal hierarchy), robustness theorems, and the universality statement. 312 lines. |
| E | Numerical Methods | Specification of the numerical schemes used for computational validation. |
| F | Extended Figures and Data | Additional figures and data tables supporting the main text. |
| G | Glossary of Symbols | Complete symbol table for the Canon Foundations paper. |
| H | Reproducibility Statement | Statement of computational reproducibility standards and procedures. |

### Supporting Files

| File | Purpose |
|------|---------|
| `ED_Canon Foundation Appendices/glossary.md` | Canonical lexicon of ED architectural and dynamical terms: attractor, capacity, discriminant, horizon, manifold, modal hierarchy, spiral, triad, and all related quantities. |
| `ED_Canon Foundation Appendices/references.md` | Curated reference list: foundational PDE theory (Amann, Evans, Ladyzhenskaya), dynamical systems (Hirsch-Smale, Khalil, Strogatz), spectral methods (Boyd, Trefethen), universality and normal forms (Arnold, Guckenheimer-Holmes, Goldenfeld), numerical methods (LeVeque, Press), and functional analysis (Rudin, Zeidler). |

---

## Reading Order

**For the mathematical reader:** Canon → Foundations (Appendix C) → Appendix D → Applications Paper.

**For the computational reader:** Simulation Suite → Numerical Atlas → Applications Paper.

**For the complete picture:** The Monograph integrates all of the above.

**Quick reference:** Glossary → References → Appendix G (symbols).

---

## Connection to Other Folders

| Folder | Relationship |
|--------|-------------|
| **ED Architecture** | ED-Arch-12 (Architectural Canon) is the source document for the Canon paper. The twelve architecture documents develop the structural layers that the papers formalize. |
| **ED Physics** | The UCE paper formalizes the cosmological results of ED-Phys modules 03, 17–19. The Rigour Paper (Appendix C) provides the analytic theory that ED-Phys module 07 validates. |
| **ED Experiments** | The Applications Paper derives predictions tested in the Open Note. The SPARC test data is the empirical basis for the confirmed dwarf-galaxy prediction. |
| **ED Simulation** | ED-SIM v1 implements the Simulation Suite specification. The Numerical Atlas documents the figures that ED-SIM produces. The Monograph source files (`.md`, `.tex`, `.bib`) are in `ED Simulation/`. |
| **ED Validation** | The six principle tests validate the architectural signatures that the Canon paper defines and the Rigour Paper proves. |
| **ED Interpretations** | The domain interpretations explore the physical reach of the predictions formalized in the Applications Paper. |

---

## Citation

Proxmire, Allen T., *Event Density Ontology*, 2026
