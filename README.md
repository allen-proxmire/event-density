# Event Density — Reproducible Simulation Repository

**Event Density (ED)** is an architectural framework for studying collective dynamics
in N-particle systems. Particles move ballistically on a periodic 2-D domain. Velocities
are assigned once at initialisation according to a *gamma gate* and never updated
thereafter — there are no forces, no potentials, and no runtime interactions. Despite
this minimal rule set, collapse timing is governed by exact closed-form *law surfaces*,
and seven architectural invariants hold to four decimal places across all tested
configurations.

This repository contains the complete, self-contained simulation infrastructure for
the ED-Arch experimental series (ED-Arch-01 through ED-Arch-21), a reproducibility
harness, four analysis notebooks, and full documentation.

---

## Quick start

```bash
# 1. Create and activate the environment
conda env create -f environment.yml
conda activate ed-arch

# 2. Run the golden experiment (N=6, d=60, gamma=+1)
python run_all.py --scenario H
# Expected: chi_ref=0.4000  chi_emp=0.4000  dev=0.0000  mechanism=inward-collapse

# 3. Run all canonical scenarios and generate all figures
python run_all.py --all
```

Results are written to `results/summary.json`; figures are saved under
`figures/boundaries/`, `figures/manifolds/`, and `figures/invariants/`.

---

## Repository layout

```
ED/
|
|-- run_all.py               # CLI harness  (--scenario H|triads|compositionality|scaling | --all)
|
|-- ed_core/                 # Core simulation library
|   |-- fields.py            #   SimParams, EDField, EDRing
|   |-- update_rules.py      #   step(), run_ring()
|   |-- micro_events.py      #   MicroEvent, detect_micro_events(), classify_mechanism_from_geometry()
|   |-- invariants.py        #   chi_ref_in(), chi_ref_out(), d_sw_tangent(), chi_prog_pause_resume()
|   |-- utils.py             #   dmin_pbc(), cross_dmin(), K_for_N(), set_seed()
|   `-- harness.py           #   run_scenario_*(), save_*_figure()
|
|-- scenarios/               # Standalone scenario scripts
|   |-- scenario_H.py        #   Golden experiment (N=6, d=60, gamma=+1)
|   |-- triads.py            #   Three-cluster equilateral-triangle configuration
|   |-- compositionality.py  #   3x3 gamma-pairing matrix (INV-21-1)
|   `-- scaling_tests.py     #   K = 2 sin(pi/N) scaling for N = 3 .. 12
|
|-- experiments/             # Jupyter notebooks (ED-Arch-12, 17, 20, 21)
|   |-- ED-Arch-12-boundaries.ipynb
|   |-- ED-Arch-17-manifold.ipynb
|   |-- ED-Arch-20-sheets.ipynb
|   `-- ED-Arch-21-laws.ipynb
|
|-- docs/                    # Documentation and technical reports
|   |-- index.md             #   Entry point with links to all docs
|   |-- overview.md          #   What ED is and why it exists
|   |-- architecture.md      #   Ontology, geometry, update rule, law surfaces
|   |-- micro_events.md      #   MicroEvent operator and mechanism taxonomy
|   |-- invariants.md        #   INV-21-1 through INV-21-7
|   |-- ed_arch_series.md    #   Phase-by-phase series summary
|   |-- how_to_run.md        #   Full installation and usage guide
|   `-- glossary.md          #   Definitions of all ED terms
|
|-- figures/                 # Generated figures (not tracked in git)
|   |-- boundaries/          #   dmin_trace plots per scenario
|   |-- manifolds/           #   chi scatter plots
|   `-- invariants/          #   heatmaps and bar charts
|
|-- results/                 # Generated results (not tracked in git)
|   `-- summary.json         #   Full output of run_all.py --all
|
|-- data/                    # Raw simulation data (not tracked in git)
|-- environment.yml          # Conda environment specification
`-- LICENSE
```

---

## Running the reproducibility harness

`run_all.py` is the single entry point for all canonical scenarios.

```bash
# Run a single scenario by name
python run_all.py --scenario H
python run_all.py --scenario triads
python run_all.py --scenario compositionality
python run_all.py --scenario scaling

# Run all four scenarios in sequence
python run_all.py --all
```

Each scenario run:

1. Calls the corresponding `run_scenario_*()` function in `ed_core/harness.py`.
2. Saves figures to `figures/{boundaries,manifolds,invariants}/` with ISO-8601 timestamps.
3. Appends its results to an in-memory summary dict.

After `--all`, the full summary is written to `results/summary.json` as UTF-8 JSON.
Every scenario verifies `dev = chi_emp - chi_ref = 0.0000`; a non-zero deviation
indicates a broken invariant.

### Expected output (--all)

| Scenario | Key result |
|---|---|
| H | chi_ref = chi_emp = 0.4000, dev = 0.0000, mechanism = inward-collapse |
| triads | All 3 clusters: dev = 0.0000 |
| compositionality | 6/9 gamma-pairs collapsing: dev_A = 0.0000 for all |
| scaling | 10/10 N-values (N=3..12): dev = 0.0000 |

---

## Regenerating figures and summary.json

Figures and `results/summary.json` are not tracked in git. To regenerate them from
scratch:

```bash
# Remove any existing outputs (optional)
rm -rf figures/boundaries/* figures/manifolds/* figures/invariants/* results/summary.json

# Regenerate everything
python run_all.py --all
```

Figures are deterministic when `set_seed(42)` is called (the default). Passing a
different seed will produce statistically equivalent but numerically distinct outputs.

To regenerate outputs for a single scenario:

```bash
python run_all.py --scenario scaling
```

The corresponding figure files are written immediately after each scenario completes.

To reproduce the Jupyter notebook outputs, open any notebook in `experiments/` and
select **Kernel > Restart & Run All**. Notebooks call `set_seed(42)` in their first
code cell.

---

## Core mechanics

### Gamma gates and the ballistic rule

Each ring is initialised by choosing:

- **N** — number of particles
- **d** — nearest-neighbour separation (px)
- **gamma** — velocity gate: `+1` inward radial, `0` tangential CCW, `-1` outward radial

At each simulation step `t`, every particle moves as:

```
pos[t+1] = (pos[t] + vel * DT) % L
```

where `DT = 0.1`, `L = 400`, and velocities are fixed at initialisation. Collapse is
detected every `SAMPLE = 50` steps: when `dmin_pbc(pos) <= MERGE_THR = 23.5 px`, the
simulation terminates and records `collapse_step`.

The dimensionless collapse time is `chi = collapse_step / T_DECAY` where `T_DECAY = 1000`.

### Law surfaces

Because the motion is purely ballistic, collapse timing is determined by closed-form
geometry. Two law surfaces govern the two collapsing regimes:

**Inward sheet (gamma = +1).** Particles move radially inward at speed `K * DT` per
step, where `K = 2 sin(pi/N)` is the chord-to-radius ratio. The quantised collapse
time is:

```
chi_ref_in(d) = ceil((d - MERGE_THR) / (K * DT) / SAMPLE) * SAMPLE / T_DECAY
```

**Outward sheet (gamma = -1).** Particles move radially outward, wrap through periodic
boundary conditions, and converge from the opposite side. The quantised collapse time is:

```
chi_ref_out(d) = ceil((L - 2*d - MERGE_THR) / (2*K*DT) / SAMPLE) * SAMPLE / T_DECAY
```

**Pythagorean tangential drift (INV-21-3).** Under `gamma = 0`, adjacent particles
diverge as:

```
d_sw = sqrt(d_init^2 + (t_sw * DT)^2)
```

If the gate is later switched to `+1`, this `d_sw` feeds directly into `chi_ref_in`.

Both surfaces are implemented in `ed_core/invariants.py` and verified to four decimal
places (`dev = 0.0000`) for all N in {3, ..., 12} and a wide range of d values.

### Micro-event operator

A *micro-event* is the atomic record produced at collapse time. The operator in
`ed_core/micro_events.py` records:

| Field | Description |
|---|---|
| `collapse_step` | Step index at which dmin <= MERGE_THR |
| `chi_emp` | Empirical collapse time: collapse_step / T_DECAY |
| `dmin_at_event` | Measured nearest-neighbour distance at event step |
| `mechanism` | Classified label (see below) |
| `gamma` | Active gate at event time |
| `R` | Mean circumradius at event time |
| `K` | Ring chord-to-radius constant |
| `pos_snapshot` | (N, 2) particle positions at event step |
| `vel_snapshot` | (N, 2) particle velocities at event step |

Mechanism classification applies five geometry-based priority rules to the dmin and R
histories maintained throughout the simulation:

| Priority | Label | Condition |
|---|---|---|
| 1 | `PBC-corner` | Particle within 1 px of domain boundary, velocity pointing outward |
| 2 | `inward-collapse` | gamma=+1 and dmin strictly decreasing over last 3 sample steps |
| 3 | `outward-PBC` | gamma=-1 and circumradius R strictly increasing over last 2 sample steps |
| 4 | `other-late` | chi > 3.0 and no earlier rule matched |
| 5 | `DECAY` | No collapse within STEPS=5000; sentinel appended |

Usage:

```python
from ed_core import EDRing, set_seed
from ed_core.micro_events import detect_micro_events

set_seed(42)
ring = EDRing(N=6, d=60.0, cx=200.0, cy=200.0, gamma=1)
events = detect_micro_events(ring)
print(events[0].chi_emp, events[0].mechanism)
# 0.4  inward-collapse
```

---

## ED-Arch-21 invariants

Seven invariants form the closure of the ED-Arch program. All are verified by
`run_all.py --all` to four decimal places.

| ID | Statement |
|---|---|
| INV-21-1 | **3x3 gamma-sheet compositionality.** Collapse time of ring A is unaffected by the gamma assignment of any co-present ring B. |
| INV-21-2 | **Memoryless law-surface jumps.** A gamma switch causes immediate transition to the new law surface with no residual from prior trajectory. |
| INV-21-3 | **Pythagorean tangential drift.** After t_sw tangential steps from d_init: d_sw = sqrt(d_init^2 + (t_sw * DT)^2). |
| INV-21-4 | **Geometry-aware programmed collapse.** Three-phase programmes are fully predictable: chi_adj = t2/T_DECAY + chi_ref_in(d_sw, K). |
| INV-21-5 | **Perturbation hardness hierarchy.** Robustness to geometric jitter: outward-PBC >= inward-collapse > DECAY. |
| INV-21-6 | **DECAY angular sub-regime.** Certain angular configurations within gamma=0 admit late collapses; DECAY is not uniformly stable. |
| INV-21-7 | **Ghost compositionality.** Physical particle interpenetration carries no timing consequence; compositionality holds even when clusters overlap. |

Full formal statements and significance notes: [docs/invariants.md](docs/invariants.md)

---

## Documentation

| File | Contents |
|---|---|
| [docs/index.md](docs/index.md) | Entry point with links to all documentation |
| [docs/overview.md](docs/overview.md) | What ED is and why it exists |
| [docs/architecture.md](docs/architecture.md) | Ontology, geometry, update rule, law surface formulas |
| [docs/micro_events.md](docs/micro_events.md) | MicroEvent operator and mechanism taxonomy |
| [docs/invariants.md](docs/invariants.md) | INV-21-1 through INV-21-7 with significance notes |
| [docs/ed_arch_series.md](docs/ed_arch_series.md) | Phase-by-phase summary of ED-Arch-01 to ED-Arch-21 |
| [docs/how_to_run.md](docs/how_to_run.md) | Full installation and usage guide |
| [docs/glossary.md](docs/glossary.md) | Definitions of all ED terms |

### Technical reports

The three primary technical reports from the ED-Arch series are provided as PDFs in
`docs/`:

| Report | PDF |
|---|---|
| Architectural Framework for Predictive Micro-Dynamics | [PDF](docs/ED-Arch-00_Architectural%20Framework%20for%20Predictive%20Micro%E2%80%91Dynamics.pdf) |
| ED Micro-Event Operator | [PDF](docs/ED-Arch-00_ED%20Micro%E2%80%91Event%20Operator.pdf) |
| ED-Arch-21: Compositionality | [PDF](docs/ED-Arch-21_NOFIGS_Compositionality.pdf) |

---

## Notebooks

Four Jupyter notebooks in `experiments/` reproduce the key figures from the
ED-Arch series:

| Notebook | Content |
|---|---|
| [ED-Arch-12-boundaries.ipynb](experiments/ED-Arch-12-boundaries.ipynb) | dmin_trace boundary plots for scenario H and triads |
| [ED-Arch-17-manifold.ipynb](experiments/ED-Arch-17-manifold.ipynb) | chi_ref vs chi_emp scatter across N=3..12 |
| [ED-Arch-20-sheets.ipynb](experiments/ED-Arch-20-sheets.ipynb) | Three law surfaces (inward, outward, tangential) on a single figure |
| [ED-Arch-21-laws.ipynb](experiments/ED-Arch-21-laws.ipynb) | 3x3 compositionality matrix and K-scaling bar charts |

Launch:

```bash
jupyter notebook experiments/
```

---

## ED-Arch series summary

The ED-Arch series spans 21 experimental reports across five phases:

- **Phase 1 (ED-Arch-01..05) — Ontology.** Establishes the minimal vocabulary: particle, field, ring, gamma gate, event. No simulation infrastructure; the framework is purely mathematical.
- **Phase 2 (ED-Arch-06..12) — Laws.** Derives the inward and outward law surfaces analytically. Verifies the golden experiment (chi_ref = chi_emp = 0.4000) for the first time.
- **Phase 3 (ED-Arch-13..16) — Compositionality and micro-events.** Introduces the triadic geometry, the MicroEvent operator, and the five-rule mechanism taxonomy.
- **Phase 4 (ED-Arch-17..20) — Manifold and sheets.** Characterises the full (d, N) chi manifold and synthesises all three gamma sheets into a unified geometric structure.
- **Phase 5 (ED-Arch-21) — Invariants and closure.** Establishes INV-21-1 through INV-21-7. Simulation confirms rather than discovers: every collapse time is predicted analytically before any run.

---

## Requirements

- Python >= 3.11
- NumPy >= 1.24
- Matplotlib >= 3.7
- Jupyter >= 1.0 (for notebooks only)

All dependencies are pinned in `environment.yml`. Install with:

```bash
conda env create -f environment.yml
conda activate ed-arch
```

---

## License

MIT — see [LICENSE](LICENSE).
