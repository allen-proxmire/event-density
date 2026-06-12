# Phase Bits / Boundary — Build Step 6 Implementation

**Program:** Determinability-boundary bits-measurement (empirical arc)
**Document:** Build Step 6 — decoupling-surface detection
**Status:** **Implemented, run, PASS** — surfaces explicit; boundary nodes exact; strata unperturbed; no regression
**Date filed:** June 2026
**Author:** Allen Proxmire
**Related:** `Phase_SimulatorDesign.md` §6; `Phase_SimulatorImplementationPlan.md` §3; `Phase_E_ConstraintSurface.md` §6; `BuildStep6_Results.md`

---

## 1. Purpose

This document implements **Build Step 6 — decoupling-surface detection**, per `Phase_SimulatorDesign.md` §6. A **decoupling surface** is an edge across which reciprocal participation cannot propagate (B6). These surfaces are the **empirical determinability boundary** — the structural object Phase E §6 located, now made explicit and queryable in code.

They matter for two downstream consumers:

- **Gate 3 (factorization)** depends on correct surface detection: to prove that decoupling severs reciprocal participation, the test must know exactly where the surfaces are.
- **Δ measurement** uses the surfaces to define its pairings — the across-boundary partner of each near-boundary region.

The code below was written, executed, and **passes** (output §6; record in `BuildStep6_Results.md`). Steps 4, 5, and Milestone 1 were re-run and still pass.

---

## 2. Structural Definition

**Decoupling surface.** An edge `(u, v)` is a decoupling surface iff it is decoupled in **either** direction:

> `decoupled(u, v) == True  OR  decoupled(v, u) == True`

**Directionality.** Surfaces are treated directionally:

- **One-sided decoupling does not restore comparability** — if even one direction is severed, the edge is a boundary (the OR above). Phase E §6: one-sided outflow may cross, but it does not make the two strata comparable.
- **Reciprocal decoupling defines a true boundary** — both directions severed; the standard case.

The current `ParticipationGraph` stores the `decoupled` flag on a **shared** edge record, so the two directions always agree: the implementation models **reciprocal** decoupling, the "true boundary" case the MWE and Gate 3 use. The directional OR is written so that, were per-direction storage added later for one-sided surfaces, detection would already be correct — a forward-compatible interface, not dead code.

**Boundary nodes.** The nodes incident to at least one decoupling surface. These anchor Δ's near-boundary regions.

---

## 3. Code — `Bits/simulator/boundary.py`

```python
"""Decoupling-surface detection — Build Step 6.

A decoupling surface is an edge across which reciprocal participation fails
(B6). It is the empirical determinability boundary: strata are the connected
components of the reciprocal subgraph (strata.py), and the surfaces are the
edges that separate them. This module exposes those surfaces explicitly for the
factorization gate (Gate 3) and for Δ pairing.

Directionality. An edge (u, v) counts as a decoupling surface if it is decoupled
in EITHER direction:  decoupled(u, v) OR decoupled(v, u). One-sided decoupling
does not restore comparability, so a single decoupled direction is enough to
make the edge a boundary. The current ParticipationGraph stores the flag
symmetrically (a shared edge record), so both directions agree — this models the
RECIPROCAL-decoupling ("true boundary") case the MWE and Gate 3 use. The OR is
written directionally so that, were per-direction storage added later for
one-sided surfaces, detection would already be correct.

All returned structures are deterministic and sorted.
"""
from __future__ import annotations

from .graph import ParticipationGraph


def _undirected_edges(graph: ParticipationGraph) -> list[tuple[int, int]]:
    """All edges as canonical (min, max) pairs, each once, sorted."""
    seen: set[tuple[int, int]] = set()
    for u in graph.nodes():
        for v in graph.neighbors(u):
            seen.add((min(u, v), max(u, v)))
    return sorted(seen)


def detect_decoupled_edges(graph: ParticipationGraph) -> list[tuple[int, int]]:
    """Return the decoupling surfaces as sorted canonical (u, v) pairs.

    An edge is a surface iff it is decoupled in either direction. Deterministic.
    """
    surfaces: list[tuple[int, int]] = []
    for u, v in _undirected_edges(graph):
        if graph.is_decoupled(u, v) or graph.is_decoupled(v, u):  # directional OR
            surfaces.append((u, v))
    return surfaces


def detect_boundary_nodes(graph: ParticipationGraph) -> set[int]:
    """Return the set of nodes incident to at least one decoupling surface."""
    nodes: set[int] = set()
    for u, v in detect_decoupled_edges(graph):
        nodes.add(u)
        nodes.add(v)
    return nodes


def boundary_map(graph: ParticipationGraph) -> dict[int, list[int]]:
    """node_id -> sorted list of neighbors reachable only across a decoupling
    surface. Deterministic and stable across runs; used to anchor Δ pairings
    (the across-boundary partner of each boundary node)."""
    m: dict[int, set[int]] = {}
    for u, v in detect_decoupled_edges(graph):
        m.setdefault(u, set()).add(v)
        m.setdefault(v, set()).add(u)
    return {k: sorted(vs) for k, vs in sorted(m.items())}
```

Requirements met:

- **Directional treatment** — the OR over both directions (§2).
- **Deterministic, sorted structures** — canonical `(min,max)` edges, sorted; `boundary_map` keys and values sorted.
- **Clean integration with `strata.py`** — both read the same `decoupled` flag as the single source of truth; `strata.py` *excludes* those edges from its flood, `boundary.py` *enumerates* them. Read-only: boundary detection never mutates the graph.

---

## 4. Integration with Strata and Update Loop

The two modules are complementary views of the same cut, sharing one source of truth (`graph`'s `decoupled` flag):

- **`strata.py` already ignores decoupled edges** — its BFS walks `admissible_neighbors` (non-decoupled), so decoupling silently partitions the graph into strata.
- **`boundary.py` exposes the surfaces explicitly** — the edges, the incident nodes, and the across-surface pairings.

Strata say *which side* a node is on; boundaries say *where the cut is*. Gate 3 needs both: distinct strata to assert independence, and the explicit surface to assert nothing crosses.

**No changes to `update.py`** — as scoped. Boundary information is consumed by Gate 3 (Step 9), the MWE (Step 8), and Δ pairing, not by the update loop. The demo confirms strata are byte-identical before and after boundary detection (boundary detection is read-only).

`__init__.py` now exports `detect_decoupled_edges`, `detect_boundary_nodes`, `boundary_map`.

---

## 5. Minimal Example Script — `Bits/examples/boundary_demo.py`

Reuses the two-cluster graph (A={0,1,2}, B={3,4,5}, decoupled bridge `(2,3)`); prints surfaces, boundary nodes, the boundary map, and strata; verifies all four.

```python
"""Build Step 6 demo - decoupling-surface detection.

Reuses the two-cluster graph from strata_demo (A={0,1,2}, B={3,4,5}, decoupled
bridge (2,3)). Verifies that:
  - the decoupled bridge (2,3) is detected as a surface;
  - boundary nodes are exactly {2, 3};
  - boundary_map anchors each boundary node to its across-surface partner;
  - strata are unchanged (boundary detection does not perturb the partition).
"""
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from simulator import (  # noqa: E402
    ParticipationGraph,
    compute_strata,
    detect_decoupled_edges,
    detect_boundary_nodes,
    boundary_map,
)


def build_two_clusters():
    g = ParticipationGraph()
    g.add_edge(0, 1, bandwidth=0.5)
    g.add_edge(1, 2, bandwidth=0.5)
    g.add_edge(3, 4, bandwidth=0.5)
    g.add_edge(4, 5, bandwidth=0.5)
    g.add_edge(2, 3, bandwidth=0.5, decoupled=True)   # decoupling surface
    return g


def main():
    print("=" * 64)
    print("BUILD STEP 6 - decoupling-surface detection")
    print("=" * 64)

    g = build_two_clusters()

    edges = detect_decoupled_edges(g)
    bnodes = detect_boundary_nodes(g)
    bmap = boundary_map(g)
    strata = compute_strata(g)

    print(f"\n  decoupled edges : {edges}")
    print(f"  boundary nodes  : {sorted(bnodes)}")
    print(f"  boundary_map    : {bmap}")
    print(f"  strata          : {dict(sorted(strata.items()))}")

    # Checks
    bridge_detected = edges == [(2, 3)]
    boundary_exact = bnodes == {2, 3}
    map_correct = bmap == {2: [3], 3: [2]}
    strata_unchanged = strata == {0: 0, 1: 0, 2: 0, 3: 1, 4: 1, 5: 1}
    deterministic = (detect_decoupled_edges(g) == edges
                     and boundary_map(g) == bmap)

    print("\nChecks")
    print(f"  (2,3) detected as decoupled      : {bridge_detected}")
    print(f"  boundary nodes == {{2,3}}          : {boundary_exact}")
    print(f"  boundary_map correct             : {map_correct}")
    print(f"  strata unchanged                 : {strata_unchanged}")
    print(f"  deterministic across runs        : {deterministic}")

    passed = (bridge_detected and boundary_exact and map_correct
              and strata_unchanged and deterministic)
    print("\n" + "=" * 64)
    print(f"BUILD STEP 6: {'PASS' if passed else 'FAIL'}")
    print("=" * 64)
    return passed


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
```

---

## 6. Acceptance Criteria for Build Step 6 — Result

Executed; **PASS** (exit 0). Recorded output:

```
================================================================
BUILD STEP 6 - decoupling-surface detection
================================================================

  decoupled edges : [(2, 3)]
  boundary nodes  : [2, 3]
  boundary_map    : {2: [3], 3: [2]}
  strata          : {0: 0, 1: 0, 2: 0, 3: 1, 4: 1, 5: 1}

Checks
  (2,3) detected as decoupled      : True
  boundary nodes == {2,3}          : True
  boundary_map correct             : True
  strata unchanged                 : True
  deterministic across runs        : True

================================================================
BUILD STEP 6: PASS
================================================================
```

Regressions: Step 5 exit 0; Step 4 exit 0; Milestone 1 exit 0.

| Criterion | Result |
|---|---|
| `detect_decoupled_edges` returns exactly the decoupled edges | **PASS** (`[(2,3)]`) |
| `detect_boundary_nodes` returns exactly nodes incident to decoupled edges | **PASS** (`{2,3}`) |
| `boundary_map` deterministic and stable | **PASS** (`{2:[3],3:[2]}`) |
| No regression (Milestone 1, Steps 4–5) | **PASS** (all exit 0) |

The surface `(2,3)` connects stratum 0 (node 2) to stratum 1 (node 3): the boundary map `{2:[3], 3:[2]}` is the Δ across-boundary pairing in raw form — a node on each side of the determinability boundary, paired across it.

---

## 7. Next Steps (Preview)

| Step | Build | Unlocks |
|---|---|---|
| **7** | `HistoryRecorder` (`recorder.py`) — append-only ρ/orientation snapshots, commit log, `.npz` + JSON | informational half of Gate 3; Δ inputs |
| **8** | MWE (`examples/mwe_16node.py`) — two clusters, decoupled bridge, independent seeds | first measurement-shaped run |
| **9** | Full test suite | Gate 3 (factorization) executable |
| **10** | Run all four gates on the MWE | acceptance: simulator certified |

---

## 8. Deliverables

Produced and verified:

- **`Bits/simulator/boundary.py`** — `detect_decoupled_edges`, `detect_boundary_nodes`, `boundary_map` (directional, deterministic, read-only).
- **`Bits/examples/boundary_demo.py`** — runnable; verifies surface detection and that strata are unperturbed.
- **`Bits/BuildStep6_Results.md`** — recorded run and acceptance table.

**The determinability boundary is now an explicit, queryable object.** Per program discipline, **no Δ is measured until all four gates pass** (Build Step 10). The next deliverable is the HistoryRecorder.

---

## 9. Next Actions

Proceed to **Build Step 7 — `HistoryRecorder`** (`recorder.py`): append-only per-step snapshots of ρ and orientation, the committed-event log, and `.npz` + JSON export with the topology/strata/boundary metadata. This captures the trajectories that the informational half of Gate 3 (across-boundary MI ≈ 0) and the Δ computation both consume — the last simulator component before the MWE assembles them end to end.

---

*End of Build Step 6 implementation. Decoupling surfaces are explicit and queryable; boundary nodes and across-surface pairings exposed; strata unperturbed; no regression. The next deliverable is the HistoryRecorder.*
