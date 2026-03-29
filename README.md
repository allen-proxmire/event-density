# Event Density

**A structural ontology for physics.**

---

## What Event Density Is

Event Density (ED) is an ontological framework built on four primitives — a bounded scalar density field, a degenerate nonlinear mobility, a monostable penalty, and a global participation variable — from which a unique canonical PDE is derived via seven structural axioms. The PDE decomposes into three constitutive channels whose structural consequences are compared to known physical laws.

ED is not a model fitted to data. It is a constitutive architecture: a specific choice of mathematical objects and their interaction rules. The question is not whether ED can be tuned to match observations, but whether its intrinsic channels correspond to recognisable physical laws.

## What Event Density Is Not

ED does not postulate a spacetime metric, a gravitational potential, a Hilbert space, a gauge field, a partition function, or any multi-component microphysics. It has no Lorentz invariance, no gauge symmetry, no action principle. It is parabolic, dissipative, and scalar. It does not claim to derive general relativity, quantum mechanics, or statistical mechanics.

## The Three Constitutive Channels

| Channel | Operator | Physical function |
|---------|----------|-------------------|
| **Mobility** | Nonlinear degenerate diffusion | Geometry: how density redistributes |
| **Penalty** | Linear restoring force | Calculus: how density relaxes |
| **Participation** | Global scalar feedback | Dynamics: how the system oscillates |

## The Six Structural Analogues

Each analogue isolates one or more channels, derives an analytical prediction, runs a numerical experiment, and checks whether the result matches a known physical law.

| # | Channels | Analogue | Key result |
|---|----------|----------|------------|
| 1 | Penalty | RC / Debye relaxation | 0.00% error |
| 2 | Mobility | Barenblatt PME self-similarity | 1.1% accuracy |
| 3 | Mobility + Penalty | Stefan horizon dynamics | 2.5% threshold error |
| 4 | All three | Telegraph-modulated horizons | Negative result (architectural limit) |
| 5 | Mobility + Participation | Telegraph-modulated PME | 0.03% frequency match |
| 6 | All three | Temporal tension interaction | Emergent nonlinear repulsion discovered |

---

## Repository Structure

```
Event Density/
    edsim/                      ED-SIM-02: simulation platform (Python package)
        core/                   Parameters, operators, integrators, boundary, spectral
        invariants/             Energy, spectral, morphology, dissipation, correlation, topology
        experiments/            Scenarios, sweeps, atlas runner
        phys/                   ED-PHYS-01..10 experiments + six structural analogues
            analogues/          RC/Debye, Barenblatt, horizon, telegraph, temporal tension
        units/                  Physical units, scales, mapping
        regimes/                Regime manifold, classifier, observables
        math/                   Modal hierarchy, transients, architectural laws
        comparison/             Cross-framework comparison matrix
        reproducibility/        9-phase validation pipeline
        visualization/          Field, invariant, morphology, animation plots
        tests/                  112 pytest tests

    manuscript/                 Generated reports and papers
        foundational_paper/     ED Foundational Paper (.md and .tex)
        ED-Analogue-01..06_*.md Individual analogue reports
        ED-PHYS-01..10_*.md     Physics experiment reports
        monograph/              Full ED monograph

    research/                   Complete ED research archive (read-only)
        ED Architecture/        12 layered structural documents
        ED PAPERS/              Core papers, appendices, monograph
        ED Physics/             ED-Phys 01-40
        ED Interpretations/     31 domain interpretations + 12 essays
        ED Experiments/         Experiment programme, SPARC test
        ED Simulation/          ED-SIM v1 + v2 architecture
        ED Validation/          P1-P7 reproducibility outputs

    docs/                       Usage guide, architecture, API, performance
    examples/                   Lab tour + visual gallery notebooks
```

---

## Quick Start

### Install

```bash
pip install -e .
```

### Run Tests

```bash
pytest edsim/tests/ -v
```

All 112 tests should pass in under 5 seconds.

### Run the Reproducibility Pipeline

```bash
python -m edsim certify
```

All 9 phases should pass.

### Run a Scenario

```python
from edsim.experiments.scenarios import get_scenario
from edsim.experiments.atlas import run_atlas, summarize_time_series

params, ts = run_atlas(get_scenario("A_2d_cosine"))
print(summarize_time_series(ts))
```

### Run the Six Structural Analogues

See [HOW_TO_RUN_ANALOGUES.md](HOW_TO_RUN_ANALOGUES.md) for detailed instructions.

```python
from edsim.phys.analogues.rc_debye import run_rc_debye_experiment
report = run_rc_debye_experiment()
print(report)
```

---

## Key Documents

| Document | Location | Content |
|----------|----------|---------|
| Foundational Paper | [`manuscript/foundational_paper/`](manuscript/foundational_paper/) | Six analogues, falsification, synthesis |
| BAO Paper | [`manuscript/ED_BAO_Paper.md`](manuscript/ED_BAO_Paper.md) | BAO-like correlation feature |
| Monograph | [`manuscript/monograph/`](manuscript/monograph/) | Full ED monograph |
| What Is ED | [`WHAT_IS_ED.md`](WHAT_IS_ED.md) | Conceptual overview |
| Reproducing Results | [`REPRODUCING_FOUNDATIONS_PAPER.md`](REPRODUCING_FOUNDATIONS_PAPER.md) | How to regenerate every result |

---

## Citation

If you use ED-SIM-02 or the structural analogues in your work, please cite:

```bibtex
@article{proxmire2026ed,
  author  = {Allen Proxmire},
  title   = {Event Density as an Ontological Framework:
             Constitutive Channels, Structural Laws,
             and Six Empirical Analogues},
  year    = {2026},
  note    = {Available at https://github.com/allen/event-density}
}
```

---

## License

This project is released under the [MIT License](LICENSE).
