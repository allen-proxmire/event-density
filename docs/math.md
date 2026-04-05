# Mathematical Development Layer

The `edsim.math` package provides the formal mathematical infrastructure
for the ED-SIM-02 platform: modal decomposition, transient classification,
axiom scaffolding, law formalization, and appendix generation.

## Modal Decomposition

The `modal` module extracts the full time-resolved spectral structure
$A_k(t)$ from a simulation.

```python
from edsim.math import compute_modal_spectrum, extract_modal_hierarchy

ms = compute_modal_spectrum(ts, params)
mh = extract_modal_hierarchy(ms)

print(f"Primary mode: k={mh.primary_k}, A={mh.primary_amplitude:.4e}")
print(f"Hierarchy ratio A_1/A_2: {mh.hierarchy_ratio:.2f}")
print(f"Energy concentration (top 10%): {mh.energy_concentration:.2%}")
print(f"Inertial exponent: {mh.inertial_exponent:.3f}")
```

The `ModalSpectrum` stores amplitudes as a $(n_t \times n_k)$ array with
the DC mode excluded.  The `ModalHierarchy` identifies the primary mode,
secondary cascade, inertial subrange, and dissipative cutoff.

Modal decay rates $\sigma_k$ are estimated by fitting $\log A_k(t)$
linearly in time:

```python
from edsim.math import modal_decay_rates
rates = modal_decay_rates(ms)  # positive = decaying
```

## Transient Families

The `transients` module classifies the transient behaviour into one of
four canonical types:

| Type | Name | Criterion |
|------|------|-----------|
| I | Monotone relaxation | Concave energy decay, no mode switches |
| II | Modal cascade | Mode switches, low hierarchy ratio |
| III | Metastable plateau | Extended near-constant energy phase |
| IV | Multi-scale burst | Multiple mode switches with convex phases |

```python
from edsim.math import classify_transient, compute_transient_invariants

inv = compute_transient_invariants(ts)
tc = classify_transient(ts, modal_hierarchy=mh, modal_spectrum=ms)

print(f"Type: {tc.transient_type.value}")
print(f"Confidence: {tc.confidence:.2f}")
print(f"Relaxation time: {tc.invariants.relaxation_time:.4f}")
```

The classification uses six scalar invariants: relaxation time, modal
turnover rate, entropy drop, energy curvature, plateau fraction, and
mode-switch count.

## Architectural Axioms

The `architecture` module encodes the seven axioms P1-P7 and the
derivation tree that produces the canonical ED PDE.

```python
from edsim.math import ArchitecturalAxioms, derive_canonical_pde

for a in ArchitecturalAxioms.all_axioms():
    print(f"{a.name} ({a.title}): {a.statement}")

steps = derive_canonical_pde()
for s in steps:
    print(f"Step {s.step} (uses {s.uses_axioms}): {s.description}")
```

The seven axioms are:

| Axiom | Title | Content |
|-------|-------|---------|
| P1 | Locality | F depends only on local derivatives |
| P2 | Isotropy | No preferred direction |
| P3 | Gradient-driven flow | Flux = $-M(\rho)\nabla\rho$ |
| P4 | Dissipative structure | Lyapunov functional exists |
| P5 | Single scalar field | One real-valued $\rho(x,t)$ |
| P6 | Minimal coupling | Global mode $v(t)$ couples additively |
| P7 | Dimensional consistency | Same constitutive functions for all $d$ |

The derivation tree shows how P1-P7 uniquely determine the canonical PDE.

## The Nine Laws

The `laws` module expresses each architectural law as a `Law` dataclass
with mathematical statement, LaTeX form, derivation status, dimensional
dependence, and universality scope.

```python
from edsim.math import ALL_LAWS, verify_all_laws

for law in ALL_LAWS:
    print(f"Law {law.number}: {law.name} [{law.derivation_status}]")

results = verify_all_laws(ts, params)
for r in results:
    status = "PASS" if r["passed"] else "FAIL"
    print(f"  Law {r['law']}: {status}")
```

| Law | Name | Status |
|-----|------|--------|
| 1 | Unique attractor | partial |
| 2 | Monotone energy decay | derived |
| 3 | Spectral concentration | empirical |
| 4 | Factorial complexity dilution | partial |
| 5 | Gradient-dissipation dominance | derived |
| 6 | Topological conservation | partial |
| 7 | Horizon formation | empirical |
| 8 | Morphological hierarchy | empirical |
| 9 | Sheet-filament oscillation | empirical |

Each law has a verification function that tests it against a `TimeSeries`.

## Generating the Appendix

The `appendix` module assembles all mathematical content into a single
Markdown document:

```python
from edsim.math import build_math_appendix

path = build_math_appendix(
    output_path="manuscript/ED-SIM-02-Appendix-Math.md",
    scenario_name="A_2d_cosine",
)
print(f"Appendix written to: {path}")
```

The generated appendix contains:
- A.1: Modal hierarchy summary
- A.2: Transient classification
- A.3: Architectural derivation (P1-P7)
- A.4: The nine laws (formal statements)
- A.5: Law verification table

All content is auto-generated from a live simulation run, ensuring
consistency between the code and the manuscript.
