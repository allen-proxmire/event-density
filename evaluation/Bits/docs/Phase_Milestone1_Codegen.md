# Phase Bits / Milestone 1 — Code Generation

**Program:** Determinability-boundary bits-measurement (empirical arc)
**Document:** Milestone 1 code generation (the first running code)
**Status:** **Generated, run, PASS** — Gate 4 green ahead of the update loop
**Date filed:** June 2026
**Author:** Allen Proxmire
**Related:** `Phase_CodingKickoff.md` (scope & acceptance §4); `Phase_SimulatorImplementationPlan.md` (module specs §3); `Milestone1_Results.md` (recorded run)

---

## 1. Purpose

This document generates the **code for Milestone 1** of the ED-substrate simulator, per `Phase_CodingKickoff.md`. It produces the initial package under `Bits/simulator/`, the example under `Bits/examples/`, and the results note `Bits/Milestone1_Results.md`.

Milestone 1 tests **only Gate 4 (tie-break uniqueness)**, plus the **orientation-blindness** invariant and the **irreversibility chokepoint**. By design it contains:

- **no update loop** (`apply_update`/`step` deferred to Build Step 4),
- **no strata** (Build Step 5),
- **no boundaries** (Build Step 6),
- **no recorder** (Build Step 7).

The tie-break is built first because it is a *pure function of a candidate set and the graph* — provable in isolation before any dynamics exist. The code below was written, executed, and **passes** (full output in §7 and `Milestone1_Results.md`).

**One signature reconciliation, recorded for honesty.** The kickoff sketched `compute_sigma(node_id, state, graph)`. Σ is intrinsically a property of a *transition* `u → v` (its gradient term `|ρ(v) − ρ(u)|` needs both endpoints), so the implemented signature is `compute_sigma(u, v, state, graph, coeffs)` — the implementation-plan form. This is a correctness-driven adaptation, not a drift; it is noted in the module docstring.

---

## 2. Code — `Bits/simulator/graph.py`

`ParticipationGraph` (B2): sparse adjacency-list, reciprocal edges, bandwidth weights, decoupling flag. Node ids are the B1 distinct identities and double as the tie-break final key.

```python
"""ParticipationGraph — B2 bandwidth-weighted participation graph.

Node ids are the B1 distinct identities; they also serve as the tie-break
final key (sigma) when bandwidths tie. Edges are reciprocal (undirected) by
default; a `decoupled` flag marks a decoupling surface (B6).
"""
from __future__ import annotations

from typing import Iterable


class ParticipationGraph:
    """Sparse adjacency-list participation graph (B2).

    Internal store: node -> {neighbor -> {"bw": float, "decoupled": bool}}.
    The same edge-data dict is shared by both directions so a flag flip is
    seen reciprocally.
    """

    def __init__(self) -> None:
        self._adj: dict[int, dict[int, dict]] = {}

    def add_node(self, node_id: int) -> None:
        """Register a node (no-op if it already exists)."""
        self._adj.setdefault(node_id, {})

    def add_edge(self, u: int, v: int, bandwidth: float,
                 decoupled: bool = False) -> None:
        """Add a reciprocal channel u<->v with the given bandwidth (B2 weight)."""
        self.add_node(u)
        self.add_node(v)
        data = {"bw": float(bandwidth), "decoupled": bool(decoupled)}
        self._adj[u][v] = data
        self._adj[v][u] = data  # shared dict ⇒ reciprocal

    def neighbors(self, u: int) -> list[int]:
        """All nodes adjacent to u (reciprocal and decoupled alike)."""
        return list(self._adj.get(u, {}).keys())

    def admissible_neighbors(self, u: int) -> list[int]:
        """Candidate set N(u): neighbors reachable via a NON-decoupled edge.
        Reach-bounded; respects decoupling surfaces (B6)."""
        return [v for v, d in self._adj.get(u, {}).items() if not d["decoupled"]]

    def bw(self, u: int, v: int) -> float:
        """Channel bandwidth on edge (u, v)."""
        return self._adj[u][v]["bw"]

    def is_decoupled(self, u: int, v: int) -> bool:
        """Whether edge (u, v) is a decoupling surface."""
        return self._adj[u][v]["decoupled"]

    def set_decoupled(self, u: int, v: int, flag: bool) -> None:
        """Set/clear the decoupling flag on edge (u, v) (reciprocal)."""
        self._adj[u][v]["decoupled"] = bool(flag)

    def nodes(self) -> Iterable[int]:
        """All registered node ids."""
        return self._adj.keys()
```

---

## 3. Code — `Bits/simulator/state.py`

`NodeState`/`StateVector` (B1/B4/B5). `commit()` is the **sole writer of ρ** and the irreversibility chokepoint (B7).

```python
"""NodeState / StateVector — B1 events, B4 commitment density, B5 orientation.

commit() is the SOLE writer of rho: the irreversibility chokepoint (B7).
No other code path in the package may assign to NodeState.rho.
"""
from __future__ import annotations

from typing import Optional

import numpy as np


class NodeState:
    """Per-node substrate state.

    rho         : commitment density (B4); monotone non-decreasing (B7).
    orientation : B5; index 0 = longitudinal (derivable), 1.. = transverse
                  (primitive). Carried by chain-continuity, never read by Sigma.
    """

    def __init__(self, rho: float = 0.0,
                 orientation: Optional[np.ndarray] = None,
                 orientation_dim: int = 2) -> None:
        self.rho: float = float(rho)
        if orientation is None:
            orientation = np.zeros(orientation_dim, dtype=float)
        self.orientation: np.ndarray = np.asarray(orientation, dtype=float)
        self.committed: bool = False
        self.active: bool = False
        self.stratum_id: int = 0

    def commit(self, delta: float,
               longitudinal: Optional[float] = None,
               transverse: Optional[np.ndarray] = None) -> None:
        """The ONLY method that writes rho. Enforces irreversibility (B7):
        delta must be >= 0; rho is incremented, never decremented.

        Optionally writes orientation: longitudinal (index 0) is the derivable
        commitment-flow direction; transverse (1..) is the primitive component
        transported from the source node.
        """
        if delta < 0:
            raise ValueError(
                f"Irreversibility violation (B7): commit delta={delta} < 0"
            )
        self.rho += float(delta)
        self.committed = True
        if longitudinal is not None:
            self.orientation[0] = float(longitudinal)
        if transverse is not None:
            self.orientation[1:] = np.asarray(transverse, dtype=float)


class StateVector(dict):
    """node_id -> NodeState, with convenience accessors.

    A thin dict subclass: the whole-substrate state is the mapping itself.
    """

    def rho_at(self, v: int) -> float:
        return self[v].rho

    def orientation_at(self, v: int) -> np.ndarray:
        return self[v].orientation

    def is_active(self, v: int) -> bool:
        return self[v].active

    def stratum_id(self, v: int) -> int:
        return self[v].stratum_id

    def active_nodes(self) -> list[int]:
        return [v for v, s in self.items() if s.active]
```

---

## 4. Code — `Bits/simulator/sigma.py`

Σ = Coh − Str − Grad. **Orientation-blind** (Phase D §5): reads ρ and graph-local data only.

```python
"""Sigma functional — Σ = Coh − Str − Grad. ORIENTATION-BLIND (Phase D §5).

HARD INVARIANT: compute_sigma and coherence read rho (B4) and graph-local
structure ONLY. They MUST NOT read NodeState.orientation (B5). Sigma being
orientation-blind is the basis of the stratified-orientation result; violating
it would corrupt the whole evaluation. Verified by the orientation-blindness
acceptance check (Milestone 1).

Note on signature: Sigma is intrinsically a property of a *transition* u -> v
(the Grad term needs both endpoints), so compute_sigma takes (u, v). This is
the implementation-plan signature; it supersedes the shorthand in the kickoff.
"""
from __future__ import annotations

from dataclasses import dataclass

from .graph import ParticipationGraph
from .state import StateVector


@dataclass(frozen=True)
class SigmaCoeffs:
    """Channel weights and parameters for Sigma. Qualitative roles are fixed
    (Coh stabilizing +, Str/Grad destabilizing -); magnitudes are tunable."""
    kc: float = 1.0          # coherence weight
    ks: float = 1.0          # strain weight
    kg: float = 1.0          # gradient-strain weight
    rho_star: float = 0.5    # coherence target density
    increment: float = 1.0   # commitment increment per step


def coherence(u: int, v: int, state: StateVector, coeffs: SigmaCoeffs) -> float:
    """Local consistency functional on the commitment field. ORIENTATION-FREE.

    Reference default: negative squared distance of rho(v) from the target
    rho_star, so maximizing Sigma favors candidates whose density is consistent
    with the chain's target. Reads rho only.
    """
    return -(state.rho_at(v) - coeffs.rho_star) ** 2


def compute_sigma(u: int, v: int, state: StateVector, graph: ParticipationGraph,
                  coeffs: SigmaCoeffs = SigmaCoeffs()) -> float:
    """Sigma for the transition u -> v:  Σ = kc*Coh - ks*Str - kg*Grad.

    Reads rho (B4) and graph-local structure ONLY; never orientation (B5).
    """
    rho_u = state.rho_at(u)
    rho_v = state.rho_at(v)
    coh = coherence(u, v, state, coeffs)   # stabilizing channel  (+)
    strain = rho_v                          # destabilizing: penalize dense targets (-)
    grad = abs(rho_v - rho_u)               # destabilizing: penalize fighting gradient (-)
    return coeffs.kc * coh - coeffs.ks * strain - coeffs.kg * grad


def compute_candidates(u: int, state: StateVector,
                       graph: ParticipationGraph) -> list[int]:
    """Admissible next-states from u: non-decoupled neighbors (reach-bounded)."""
    return graph.admissible_neighbors(u)
```

---

## 5. Code — `Bits/simulator/update.py`

Tie-break only (no loop yet). Lexicographic key `(bw, node_id)`, descending — deterministic, total.

```python
"""Update mechanics. Milestone 1: tie-break only (no update loop yet).

apply_tiebreak resolves a Sigma-maximal set to a unique winner via the
lexicographic key (bandwidth, node_id), descending — Phase_TieBreak_Specification.
The full step()/apply_update() loop is Build Step 4.
"""
from __future__ import annotations

from .graph import ParticipationGraph


def apply_tiebreak(u: int, candidates: list[int],
                   graph: ParticipationGraph) -> int:
    """Among Sigma-tied candidates v, return the unique winner whose key
    kappa(v) = (bw(u, v), v) is lexicographically maximal (descending).

    Bandwidth (B2) is the primary key; node id (B1 distinctness) is the final
    key. The order is total over distinct node ids, so exactly one winner exists.
    Deterministic; called even when |candidates| == 1.
    """
    if not candidates:
        raise ValueError("apply_tiebreak called with empty candidate set")
    return max(candidates, key=lambda v: (graph.bw(u, v), v))
```

Package surface — `Bits/simulator/__init__.py`:

```python
"""ED substrate simulator (empirical arc) — Milestone 1 core."""
from .graph import ParticipationGraph
from .state import NodeState, StateVector
from .sigma import compute_sigma, compute_candidates, coherence, SigmaCoeffs
from .update import apply_tiebreak

__all__ = [
    "ParticipationGraph", "NodeState", "StateVector",
    "compute_sigma", "compute_candidates", "coherence", "SigmaCoeffs",
    "apply_tiebreak",
]
```

---

## 6. Code — `Bits/examples/milestone1_tiebreak.py`

Tiny center+3-leaf graph; leaf ρ set equal to **force a Σ-tie**; tie-break then decided by bandwidth (Case A) or node id (Case B); plus orientation-flip and commit checks. (Console em-dashes are ASCII hyphens for cross-platform output.)

```python
"""Milestone 1 - Gate 4 (tie-break uniqueness) + orientation-blindness +
irreversibility chokepoint.

Runs with only graph.py, state.py, sigma.py, update.py. No update loop, no
strata, no boundaries, no recorder.

Topology: one center node (0) with three admissible leaves (1, 2, 3). Leaf rho
is set equal so Sigma is identical across leaves -> a forced Sigma-tie. The
tie-break then decides:
  Case A (distinct bandwidths): winner by bandwidth.
  Case B (equal bandwidths):    winner by node id (the B1-distinctness key).
"""
import os
import sys

import numpy as np

# Make Bits/ importable so `simulator` resolves regardless of CWD.
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from simulator import (  # noqa: E402
    ParticipationGraph,
    NodeState,
    StateVector,
    compute_sigma,
    compute_candidates,
    SigmaCoeffs,
    apply_tiebreak,
)

CENTER = 0
LEAVES = [1, 2, 3]


def build(bandwidths):
    g = ParticipationGraph()
    g.add_node(CENTER)
    for v, bw in zip(LEAVES, bandwidths):
        g.add_edge(CENTER, v, bandwidth=bw)
    return g


def forced_tie_state(rho_leaf=0.5, rho_center=0.0):
    sv = StateVector()
    sv[CENTER] = NodeState(rho=rho_center, orientation=np.array([0.0, 0.0]))
    for v in LEAVES:
        # identical rho on every leaf -> identical Sigma -> forced tie
        sv[v] = NodeState(rho=rho_leaf, orientation=np.array([0.0, 0.0]))
    return sv


def sigmas(sv, g, coeffs):
    return {v: compute_sigma(CENTER, v, sv, g, coeffs) for v in LEAVES}


def main():
    coeffs = SigmaCoeffs(kc=1.0, ks=1.0, kg=1.0, rho_star=0.5)

    print("=" * 64)
    print("MILESTONE 1 - Gate 4 (tie-break) + orientation-blindness + B7")
    print("=" * 64)

    # ---- Case A: distinct bandwidths -> winner by bandwidth ----
    gA = build(bandwidths=[0.3, 0.5, 0.4])
    svA = forced_tie_state()
    sigA = sigmas(svA, gA, coeffs)
    candsA = compute_candidates(CENTER, svA, gA)
    tiedA = len({round(s, 12) for s in sigA.values()}) == 1
    winnerA = apply_tiebreak(CENTER, candsA, gA)
    print("\nCase A - distinct bandwidths")
    print(f"  Sigma per candidate : {sigA}")
    print(f"  Sigma tied          : {tiedA}")
    print("  bandwidths          : " +
          ", ".join(f"{v}:{gA.bw(CENTER, v)}" for v in LEAVES))
    print(f"  winner              : {winnerA}   (expected 2, bw=0.5)")

    # ---- Case B: equal bandwidths -> winner by node id ----
    gB = build(bandwidths=[0.5, 0.5, 0.5])
    svB = forced_tie_state()
    sigB = sigmas(svB, gB, coeffs)
    candsB = compute_candidates(CENTER, svB, gB)
    tiedB = len({round(s, 12) for s in sigB.values()}) == 1
    winnerB = apply_tiebreak(CENTER, candsB, gB)
    print("\nCase B - equal bandwidths (sigma=node_id final key)")
    print(f"  Sigma per candidate : {sigB}")
    print(f"  Sigma tied          : {tiedB}")
    print("  bandwidths          : all 0.5")
    print(f"  winner              : {winnerB}   (expected 3, max node id)")

    # ---- determinism: re-run -> identical ----
    winnerA2 = apply_tiebreak(CENTER, compute_candidates(CENTER, svA, gA), gA)
    winnerB2 = apply_tiebreak(CENTER, compute_candidates(CENTER, svB, gB), gB)
    det = (winnerA2 == winnerA) and (winnerB2 == winnerB)
    print("\nDeterminism (re-run)")
    print(f"  Case A winner again : {winnerA2}  (identical: {winnerA2 == winnerA})")
    print(f"  Case B winner again : {winnerB2}  (identical: {winnerB2 == winnerB})")

    # ---- orientation-blindness ----
    before = sigmas(svA, gA, coeffs)
    rng = np.random.default_rng(0)
    for v in LEAVES:
        svA[v].orientation[:] = rng.normal(size=2)
    svA[CENTER].orientation[:] = np.array([7.0, -3.0])
    after = sigmas(svA, gA, coeffs)
    blind = all(abs(before[v] - after[v]) < 1e-15 for v in LEAVES)
    print("\nOrientation-blindness")
    print(f"  Sigma before flip   : {before}")
    print(f"  Sigma after  flip   : {after}")
    print(f"  unchanged           : {blind}")

    # ---- irreversibility chokepoint ----
    n = NodeState(rho=1.0)
    n.commit(0.5)
    rose = (n.rho == 1.5)
    rejected = False
    try:
        n.commit(-0.1)
    except ValueError:
        rejected = True
    print("\nIrreversibility chokepoint (commit)")
    print(f"  commit(+0.5)        : rho 1.0 -> {n.rho}  (increment ok: {rose})")
    print(f"  commit(-0.1)        : rejected = {rejected}")

    # ---- verdict ----
    passed = (
        tiedA and tiedB
        and winnerA == 2 and winnerB == 3
        and det and blind and rose and rejected
    )
    print("\n" + "=" * 64)
    print(f"MILESTONE 1: {'PASS' if passed else 'FAIL'}")
    print("=" * 64)
    return passed


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
```

---

## 7. Results Note — `Bits/Milestone1_Results.md`

The script was executed; it **passes** (exit code 0). Recorded output:

```
================================================================
MILESTONE 1 - Gate 4 (tie-break) + orientation-blindness + B7
================================================================

Case A - distinct bandwidths
  Sigma per candidate : {1: -1.0, 2: -1.0, 3: -1.0}
  Sigma tied          : True
  bandwidths          : 1:0.3, 2:0.5, 3:0.4
  winner              : 2   (expected 2, bw=0.5)

Case B - equal bandwidths (sigma=node_id final key)
  Sigma per candidate : {1: -1.0, 2: -1.0, 3: -1.0}
  Sigma tied          : True
  bandwidths          : all 0.5
  winner              : 3   (expected 3, max node id)

Determinism (re-run)
  Case A winner again : 2  (identical: True)
  Case B winner again : 3  (identical: True)

Orientation-blindness
  Sigma before flip   : {1: -1.0, 2: -1.0, 3: -1.0}
  Sigma after  flip   : {1: -1.0, 2: -1.0, 3: -1.0}
  unchanged           : True

Irreversibility chokepoint (commit)
  commit(+0.5)        : rho 1.0 -> 1.5  (increment ok: True)
  commit(-0.1)        : rejected = True

================================================================
MILESTONE 1: PASS
================================================================
```

**Acceptance (Kickoff §4):**

| Check | Result |
|---|---|
| A — tie-break uniqueness (forced tie ⇒ one winner; both keys exercised; deterministic) | **PASS** — Case A→2 (bw), Case B→3 (node id), re-runs identical |
| B — orientation-blindness (flip orientations ⇒ Σ unchanged) | **PASS** — Σ identical to <1e-15 |
| C — irreversibility chokepoint (commit + raises ρ; − rejected; sole writer) | **PASS** — 1.0→1.5; negative rejected |

Detail and notes: `Milestone1_Results.md`.

---

## 8. Deliverables

Produced and verified:

- **`Bits/simulator/`** — `graph.py`, `state.py`, `sigma.py`, `update.py` (tie-break only), `__init__.py`. Runs as-is on Python 3 + NumPy.
- **`Bits/examples/milestone1_tiebreak.py`** — runnable; demonstrates tie-break uniqueness (both keys), orientation-blindness, and the irreversibility chokepoint.
- **`Bits/Milestone1_Results.md`** — the recorded run and acceptance table.

**Gate 4 is green.** The selection mechanics — score, forced tie, deterministic resolution — are certified faithful to the closed specification, ahead of the update loop. Per the program discipline, **no Δ is measured until all four gates pass** (Build Step 10); Milestone 1 is one of the four.

---

## 9. Next Actions

Proceed to **Build Step 4 — the update loop** (`apply_update`, `step`): asynchronous, canonical `(stratum_id, node_id)` order, commits immediately visible, built on the certified `commit` chokepoint. That unlocks **Gate 1 (monotonicity)** and **Gate 2 (acyclicity)** once a run completes. Strata (Step 5), boundaries (Step 6), the recorder (Step 7), and the MWE (Step 8) follow, with Gate 3 (factorization) executable at the full suite (Step 9).

---

*End of Milestone 1 code generation. The empirical arc now has running, tested code: the selection core, certified ahead of the dynamics. The next deliverable is the update loop and gates 1–2.*
