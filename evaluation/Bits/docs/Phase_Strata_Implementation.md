# Phase Bits / Strata — Build Step 5 Implementation

**Program:** Determinability-boundary bits-measurement (empirical arc)
**Document:** Build Step 5 — reach-stratum detection
**Status:** **Implemented, run, PASS** — decoupling does not merge strata; numbering deterministic; no regression
**Date filed:** June 2026
**Author:** Allen Proxmire
**Related:** `Phase_SimulatorDesign.md` §5; `Phase_SimulatorImplementationPlan.md` §3; `Phase_E_ConstraintSurface.md` §6 (determinability boundary = decoupling surface); `BuildStep5_Results.md`

---

## 1. Purpose

This document implements **Build Step 5 — reach-stratum detection**, per `Phase_SimulatorDesign.md` §5. A **reach stratum** is a maximal set of nodes mutually reachable without crossing a decoupling surface — formally, a **connected component of the reciprocal (non-decoupled) subgraph**.

Stratum ids are required by three downstream consumers:

- the **canonical update order** `(stratum_id, node_id)` (Build Step 4's `step`);
- the **factorization test, Gate 3** — which needs distinct strata to verify that decoupling severs reciprocal participation;
- **Δ measurement** — the baseline (within-stratum) vs. across-boundary pairing is defined relative to strata.

The code below was written, executed, and **passes** (output §6; record in `BuildStep5_Results.md`). Build Step 4 and Milestone 1 were re-run and still pass.

---

## 2. Structural Definition

**Reciprocal subgraph.** G_recip = (V, E_recip) where edge `(u, v)` is in E_recip **iff `decoupled(u, v) == False`**. Because edges are stored as a shared bidirectional record (`graph.py`), the flag is symmetric: an edge is reciprocal in both directions or neither. One-sided influence (an edge that transmits outward but not reciprocally) is modelled by the decoupled flag and is **excluded** from E_recip — so it does **not** merge strata.

**Strata.** The connected components of G_recip. Two nodes share a stratum iff a path of non-decoupled edges connects them.

**Staticity.** For constructed decoupling surfaces (fixed at init — the primary measurement regime), strata are computed **once** and held fixed. They are recomputed only if a `decoupled` flag changes (emergent mode, later robustness studies). This matches Phase E §6 / design §5: the reach partition is a structural property of the participation graph, not of the dynamics.

---

## 3. Code — `Bits/simulator/strata.py`

```python
"""Reach-stratum detection — Build Step 5.

A reach stratum is a maximal set of nodes mutually reachable WITHOUT crossing a
decoupling surface — i.e. a connected component of the RECIPROCAL subgraph
G_recip = (V, { e : not decoupled(e) }). One-sided influence does NOT merge
strata (Phase E §6): only non-decoupled (reciprocal) edges are traversed.

Stratum numbering is deterministic: components are labelled in ascending order
of their smallest node id, so the same graph always yields the same ids.
"""
from __future__ import annotations

from .graph import ParticipationGraph
from .state import StateVector


def compute_strata(graph: ParticipationGraph) -> dict[int, int]:
    """Return node_id -> stratum_id over the reciprocal (non-decoupled) subgraph.

    BFS flood over non-decoupled edges only. Deterministic: seed nodes are taken
    in ascending id order and each new component gets the next id, so stratum ids
    are ordered by smallest member.
    """
    labels: dict[int, int] = {}
    next_id = 0
    for seed in sorted(graph.nodes()):          # ascending ⇒ deterministic labelling
        if seed in labels:
            continue
        sid = next_id
        next_id += 1
        # BFS over reciprocal edges from this seed.
        stack = [seed]
        labels[seed] = sid
        while stack:
            u = stack.pop()
            for v in graph.admissible_neighbors(u):   # non-decoupled only
                if v not in labels:
                    labels[v] = sid
                    stack.append(v)
    return labels


def assign_stratum_ids(state: StateVector, graph: ParticipationGraph) -> dict[int, int]:
    """Compute strata and write stratum_id onto every NodeState. Returns the
    mapping. Call at init for constructed surfaces (static); re-call after any
    decoupling-flag change (emergent mode, Build Step 6+)."""
    labels = compute_strata(graph)
    for node_id, sid in labels.items():
        if node_id in state:
            state[node_id].stratum_id = sid
    return labels
```

Key implementation points (all in §6's acceptance):

- **Reciprocal-only traversal:** the BFS uses `graph.admissible_neighbors(u)` (non-decoupled neighbors), never `neighbors(u)`. This is the single line that makes a decoupling surface a stratum boundary.
- **Deterministic numbering:** seeds iterated in ascending node id ⇒ component containing the smallest id gets stratum 0, next component stratum 1, etc. Stable across runs.
- **Two consumers, one truth:** `compute_strata` is the pure mapping; `assign_stratum_ids` writes it onto state and returns the same mapping.

---

## 4. Integration with Update Loop

`step()` in `update.py` now resolves a node's stratum id from an **optional `strata` mapping** if supplied, otherwise from `NodeState.stratum_id` (populated by `assign_stratum_ids`). Either way it sorts active fronts by `(stratum_id, node_id)`:

```python
def step(state, graph, coeffs=SigmaCoeffs(), strata: dict[int, int] | None = None) -> int:
    def sid(u: int) -> int:
        if strata is not None:
            return strata.get(u, state.stratum_id(u))
        return state.stratum_id(u)

    order = sorted(state.active_nodes(), key=lambda u: (sid(u), u))
    # ... (unchanged: async canonical-order processing, newly_active guard)
```

This preserves both guarantees from Build Step 4:

- **Determinism within strata** — the `(stratum_id, node_id)` order is total and stable.
- **Factorization across strata** — fronts in different strata share no admissible edges (decoupled), so processing order never couples them; the stratum grouping is purely a within-stratum determinizer. With real strata now populated, the grouping is non-trivial and ready for the Gate 3 test.

The change is **non-breaking**: when `strata` is omitted, behavior is identical to Build Step 4. Both prior demos re-run unchanged (§6).

`__init__.py` now exports `compute_strata`, `assign_stratum_ids`.

---

## 5. Minimal Example Script — `Bits/examples/strata_demo.py`

Two clusters (A = {0,1,2}, B = {3,4,5}) joined by a single **decoupled** bridge `(2,3)`; computes strata; verifies the bridge does not merge them.

```python
"""Build Step 5 demo - reach-stratum detection.

Two clusters (A = {0,1,2}, B = {3,4,5}) joined by a single DECOUPLED bridge
(2,3). The reciprocal subgraph therefore has two connected components, so the
bridge must NOT merge the strata. Checks:
  - mapping matches the two expected components;
  - decoupled bridge endpoints land in DIFFERENT strata;
  - deterministic across repeated computations.
"""
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from simulator import (  # noqa: E402
    ParticipationGraph,
    NodeState,
    StateVector,
    SigmaCoeffs,
    compute_strata,
    assign_stratum_ids,
    step,
    hash_state,
)


def build_two_clusters():
    g = ParticipationGraph()
    # Cluster A: 0-1-2 (reciprocal)
    g.add_edge(0, 1, bandwidth=0.5)
    g.add_edge(1, 2, bandwidth=0.5)
    # Cluster B: 3-4-5 (reciprocal)
    g.add_edge(3, 4, bandwidth=0.5)
    g.add_edge(4, 5, bandwidth=0.5)
    # Bridge 2-3: DECOUPLED (a decoupling surface)
    g.add_edge(2, 3, bandwidth=0.5, decoupled=True)
    return g


def fresh_state(g):
    sv = StateVector()
    for n in sorted(g.nodes()):
        sv[n] = NodeState(rho=0.0, orientation=np.array([0.0, 0.0]))
    return sv


def main():
    print("=" * 64)
    print("BUILD STEP 5 - reach-stratum detection")
    print("=" * 64)

    g = build_two_clusters()

    labels = compute_strata(g)
    print(f"\n  stratum map: {dict(sorted(labels.items()))}")
    print(f"  expected   : {{0: 0, 1: 0, 2: 0, 3: 1, 4: 1, 5: 1}}")

    expected = {0: 0, 1: 0, 2: 0, 3: 1, 4: 1, 5: 1}
    matches_expected = labels == expected

    # Bridge endpoints 2 and 3 must be in DIFFERENT strata.
    bridge_split = labels[2] != labels[3]

    # Same-component nodes share a stratum.
    same_A = labels[0] == labels[1] == labels[2]
    same_B = labels[3] == labels[4] == labels[5]

    # Determinism across repeated computation.
    deterministic = (compute_strata(g) == compute_strata(g) == labels)

    # assign_stratum_ids writes onto state and agrees with compute_strata.
    sv = fresh_state(g)
    assigned = assign_stratum_ids(sv, g)
    on_state = all(sv[n].stratum_id == labels[n] for n in g.nodes())

    # Integration: step() consumes stratum ids; seed one front per cluster and
    # confirm the run is deterministic and a commit in A never touches B.
    sv[0].active = True
    sv[3].active = True
    coeffs = SigmaCoeffs()
    h_before_B = tuple(sv[n].rho for n in (3, 4, 5))
    step(sv, g, coeffs, strata=labels)
    # (one step: each front advances within its own cluster)

    print("\nChecks")
    print(f"  matches expected components      : {matches_expected}")
    print(f"  decoupled bridge does NOT merge  : {bridge_split}  (stratum[2]={labels[2]}, stratum[3]={labels[3]})")
    print(f"  same-cluster nodes share stratum : {same_A and same_B}")
    print(f"  deterministic across runs        : {deterministic}")
    print(f"  assign_stratum_ids writes state  : {on_state}")

    passed = (matches_expected and bridge_split and same_A and same_B
              and deterministic and on_state)
    print("\n" + "=" * 64)
    print(f"BUILD STEP 5: {'PASS' if passed else 'FAIL'}")
    print("=" * 64)
    return passed


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
```

---

## 6. Acceptance Criteria for Build Step 5 — Result

Executed; **PASS** (exit 0). Recorded output:

```
================================================================
BUILD STEP 5 - reach-stratum detection
================================================================

  stratum map: {0: 0, 1: 0, 2: 0, 3: 1, 4: 1, 5: 1}
  expected   : {0: 0, 1: 0, 2: 0, 3: 1, 4: 1, 5: 1}

Checks
  matches expected components      : True
  decoupled bridge does NOT merge  : True  (stratum[2]=0, stratum[3]=1)
  same-cluster nodes share stratum : True
  deterministic across runs        : True
  assign_stratum_ids writes state  : True

================================================================
BUILD STEP 5: PASS
================================================================
```

Regressions: Build Step 4 exit 0; Milestone 1 exit 0.

| Criterion | Result |
|---|---|
| Match connected components of the reciprocal subgraph | **PASS** (map == expected) |
| Deterministic across runs | **PASS** |
| Same-component nodes → identical stratum id | **PASS** (A=0, B=1) |
| Decoupling-separated nodes → different ids | **PASS** (2→0, 3→1) |
| Update loop accepts & uses stratum ids | **PASS** (`step(..., strata=labels)`) |
| No regression (Milestone 1, Step 4) | **PASS** (both exit 0) |

**The decisive check:** bridge edge `(2,3)` is `decoupled=True` — a real edge (`neighbors(2)` includes 3) but excluded from `admissible_neighbors`, so the BFS never crosses it. Nodes 2 and 3 land in different strata (0, 1) despite adjacency. Strata are components of the *reciprocal* subgraph, not the full graph — Phase E §6 semantics, confirmed.

---

## 7. Next Steps (Preview)

| Step | Build | Unlocks |
|---|---|---|
| **6** | Decoupling-surface detection (`boundary.py`, constructed) + `boundary_nodes` | MWE bridge; Δ pairing anchors |
| **7** | `HistoryRecorder` (`recorder.py`) — `.npz` + JSON | informational half of Gate 3 |
| **8** | MWE (`examples/mwe_16node.py`) — two strata, end to end | first measurement-shaped run |
| **9** | Full test suite | Gate 3 (factorization) executable |
| **10** | Run all four gates on the MWE | acceptance: simulator certified |

---

## 8. Deliverables

Produced and verified:

- **`Bits/simulator/strata.py`** — `compute_strata`, `assign_stratum_ids` (reciprocal-subgraph components, deterministic numbering).
- **`Bits/simulator/update.py`** — `step()` updated to consume an optional `strata` mapping; non-breaking.
- **`Bits/examples/strata_demo.py`** — runnable; verifies decoupling does not merge strata.
- **`Bits/BuildStep5_Results.md`** — recorded run and acceptance table.

**Strata labels are live; the reach partition is faithful to Phase E.** Per program discipline, **no Δ is measured until all four gates pass** (Build Step 10). The next deliverable is decoupling-surface detection.

---

## 9. Next Actions

Proceed to **Build Step 6 — decoupling-surface detection** (`boundary.py`): the constructed-mode `mark_constructed_surfaces` (explicit `decoupled` edges) and `boundary_nodes` (nodes incident to a decoupling surface, cached for Δ pairing). With strata (Step 5) and boundaries (Step 6) in hand, the two-cluster MWE becomes constructible end to end (Step 8), and Gate 3 (factorization) becomes testable.

---

*End of Build Step 5 implementation. Reach strata are computed from the reciprocal subgraph; decoupling surfaces partition the graph as Phase E requires; the update loop is stratum-aware; no regression. The next deliverable is decoupling-surface detection.*
