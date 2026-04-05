# ED-SIM-03 Roadmap

The `edsim.roadmap` package defines the next-generation ED simulation
platform (ED-SIM-03) and provides tools for generating, inspecting,
and updating the development roadmap.

## Purpose of ED-SIM-03

ED-SIM-02 established the foundational architecture: a working solver
for d=1-4, a complete invariant atlas, a reproducibility pipeline,
and a cross-framework comparison.  ED-SIM-03 extends this along five
axes:

1. **Multi-field coupling** -- evolve coupled density fields
2. **Stochastic forcing** -- noise-driven steady states
3. **GPU-native solvers** -- 10-100x performance
4. **Higher dimensions** -- d=5, 6, and beyond
5. **Experimental bridge** -- falsifiable physical predictions

## Architecture

ED-SIM-03 comprises 10 components:

| Component | Purpose | Prerequisites |
|-----------|---------|---------------|
| `multi_field` | Coupled (rho_1, rho_2) system | (none) |
| `stochastic` | Multiplicative/additive noise | (none) |
| `adaptive_grid` | AMR for efficiency | `gpu_solver` |
| `gpu_solver` | JAX/CuPy backend | (none) |
| `spectral_fd_hybrid` | IMEX integrator | (none) |
| `high_dim` | d=5, 6 solver + atlas | `gpu_solver` |
| `realtime_viz` | Interactive 3D viewer | (none) |
| `interactive_nb` | Jupyter widgets | `realtime_viz` |
| `formal_proofs` | Lean 4 proofs of Laws 2, 5 | (none) |
| `experimental_bridge` | Physical predictions | `multi_field` |

## Research Themes

18 open questions are organised into five themes:

| Theme | Questions | Difficulty range |
|-------|-----------|-----------------|
| Physics | 5 | medium -- very_high |
| Mathematics | 4 | medium -- very_high |
| Computation | 3 | medium -- high |
| Architecture | 2 | medium -- high |
| Interpretation | 3 | medium -- very_high |

## Dependency Graph

The dependency graph is a DAG with 28 nodes (10 components + 18
questions) and edges representing prerequisite relationships.  Root
nodes (no prerequisites) can begin immediately.

To inspect the graph:

```python
from edsim.roadmap import (
    build_edsim3_architecture,
    list_research_questions,
    build_dependency_graph,
)

arch = build_edsim3_architecture()
qs = list_research_questions()
graph = build_dependency_graph(arch, qs)

print(f"Nodes: {len(graph.nodes)}, Edges: {len(graph.edges)}")
print(f"Roots: {graph.roots()}")
print(graph.to_table())
```

## Milestone Plan

Development proceeds in five phases:

| Phase | Title | Focus |
|-------|-------|-------|
| A | Foundations | GPU, IMEX, multi-field, stochastic |
| B | Engineering | AMR, d=5/6, visualisation, notebooks |
| C | Physics | Attractor, steady states, experiments |
| D | Mathematics | Formal proofs, rigorous derivations |
| E | Documentation | Paper, docs, reproducibility, release |

Each phase has 4 tasks with explicit acceptance criteria.

## Generating the Roadmap

```python
from edsim.roadmap import generate_roadmap

path = generate_roadmap("manuscript/ED-SIM-03-Roadmap.md")
print(f"Roadmap written to: {path}")
```

The generated document contains:
1. Architecture (10 components)
2. Research questions (18, grouped by theme)
3. Dependency graph (table + Mermaid diagram)
4. Milestone plan (5 phases, 20 tasks)
5. Manuscript outline (10 sections)
6. Summary statistics

## Updating the Roadmap

As components are completed, update the `prerequisites` and
`dependencies` fields and regenerate the roadmap.  The dependency
graph and milestone plan will automatically reflect the changes.
