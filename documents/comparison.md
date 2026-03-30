# Cross-Framework Comparison

The `edsim.comparison` package compares the ED architecture to six
established theoretical frameworks along five structural axes.  All
comparisons are structural, not rhetorical.

## Comparison Axes

Each framework is described along five axes:

| Axis | Question |
|------|----------|
| **Ontology** | What exists in this framework? |
| **Primitives** | What are the irreducible building blocks? |
| **Dynamics** | How does the system evolve? |
| **Invariants** | What is conserved or monotone? |
| **Epistemology** | What is observable or measurable? |

Each axis receives an overlap score (0-3) when compared to ED:

| Score | Meaning |
|-------|---------|
| 0 | No structural overlap |
| 1 | Weak analogy or shared concept |
| 2 | Moderate structural parallel |
| 3 | Strong structural match |

## Frameworks Compared

| Framework | Key idea |
|-----------|----------|
| **Causal Sets** | Discrete partial order of events; spacetime is emergent |
| **Entropic Gravity** | Gravity as an entropic force on holographic screens |
| **Constructor Theory** | Laws constrain which transformations are possible |
| **Hydrodynamics** | Continuous fluid dynamics (Navier-Stokes) |
| **Statistical Mechanics** | Phase-space distributions evolving to equilibrium |
| **Quantum Foundations** | Hilbert space, unitary evolution, Born rule |

## How ED is Positioned

ED is a scalar, nonlinear, dissipative PDE with degenerate mobility
and global participation coupling.  It shares structural features with
several frameworks:

- **Statistical Mechanics** (closest): gradient-flow dynamics,
  entropy non-decrease, correlation functions.  Fokker-Planck
  equation is the nearest structural relative.

- **Hydrodynamics**: continuous field PDE, Laplacian smoothing,
  mass conservation.  Differs in vector vs scalar, advection vs
  diffusion.

- **Entropic Gravity**: entropy gradients drive dynamics.  Differs
  in holographic screens vs density field.

- **Quantum Foundations**: density-like primary object, Laplacian
  operator.  Differs in linearity, unitarity, complex vs real.

- **Causal Sets**: both start from events.  Fundamentally different
  in discrete vs continuous, stochastic vs deterministic.

- **Constructor Theory**: both constrain dynamics via axioms.
  No overlap in mathematical objects or evolution rules.

## Generating the Report

```python
from edsim.comparison import build_cross_framework_report

path = build_cross_framework_report(
    output_path="manuscript/ED-SIM-02-Comparison.md"
)
print(f"Report written to: {path}")
```

The report contains:
1. Framework profiles
2. Comparison matrix (score table)
3. Detailed cell-by-cell notes
4. Structural overlaps (score >= 2)
5. Structural divergences (score <= 1)
6. Features unique to ED
7. Proximity ranking

## Interpreting the Matrix

The total score for each framework measures structural proximity to ED:

| Score range | Interpretation |
|-------------|---------------|
| 10-15 | Very close structural relative |
| 6-9 | Moderate structural overlap |
| 3-5 | Weak structural analogy |
| 0-2 | Fundamentally different |

The proximity ranking (from ED-SIM-02 analysis):

1. Statistical Mechanics (12/15)
2. Hydrodynamics (10/15)
3. Entropic Gravity (7/15)
4. Quantum Foundations (5/15)
5. Causal Sets (3/15)
6. Constructor Theory (2/15)

## Adding New Frameworks

To add a new framework, create a `Framework` instance in
`edsim/comparison/frameworks.py`, add comparison entries to
`_COMPARISONS` in `edsim/comparison/matrix.py`, and rebuild
the report.

```python
from edsim.comparison.frameworks import Framework

MY_FRAMEWORK = Framework(
    name="my_framework",
    full_name="My New Framework",
    ontology=("...",),
    primitives=("...",),
    dynamics=("...",),
    invariants=("...",),
    epistemology=("...",),
)
```
