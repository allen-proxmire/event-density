# Phase Bits / Update Loop — Build Step 4 Implementation

**Program:** Determinability-boundary bits-measurement (empirical arc)
**Document:** Build Step 4 — the ED substrate update loop
**Status:** **Implemented, run, PASS** — Gates 1 & 2 demonstrated; determinism exact; Milestone 1 intact
**Date filed:** June 2026
**Author:** Allen Proxmire
**Related:** `Phase_SimulatorDesign.md` §4; `Phase_SimulatorImplementationPlan.md` §4; `BuildStep4_Results.md` (recorded run)

---

## 1. Purpose

This document implements **Build Step 4** — the update loop — per `Phase_SimulatorDesign.md` §4 and `Phase_SimulatorImplementationPlan.md` §4. The loop is the machinery that turns the certified selection mechanics (Milestone 1) into actual ED trajectories.

The update loop is required for **correctness Gates 1 and 2**:

- **Gate 1 — I4 monotonicity:** ρ never decreases.
- **Gate 2 — acyclicity:** no global state vector recurs.

This step produces the **first real ED trajectories** — sequences of Σ-maximizing commitments under the deterministic tie-break, with irreversibility enforced through the single `commit` chokepoint. The code below was written, executed, and **passes** (output in §6; full record in `BuildStep4_Results.md`). Milestone 1 (Gate 4) was re-run and still passes — no regression from the `update.py` rewrite.

---

## 2. Update Loop Specification

The canonical step (design §4), as built:

1. **Order.** Sort active fronts by **(stratum_id, node_id)** ascending. Deterministic.
2. **Per front `u`:**
   - compute Σ for all admissible transitions `u → v` (reach-bounded candidates);
   - take the Σ-maximal set; apply the **deterministic tie-break** `(bw, node_id)`;
   - **commit** the chosen transition at the winner — the irreversibility chokepoint (ρ increment-only).
3. **Advance** the front `u → winner`; a front that advances into a node this step does **not** take a second hop the same step.

**Asynchronous, immediately visible.** A commit by an earlier-ordered front is seen by later fronts in the *same* step (no double-buffering). 

**Determinism within strata, factorization across strata.** Ordering by (stratum_id, node_id) plus the total tie-break makes the whole evolution a deterministic function of (graph, initial state, coeffs) — verified exactly in §6 (two runs, identical hashes). Fronts in different strata share no admissible edges (decoupled), so update order never couples strata: the canonical order is purely a within-stratum determinizer, and factorization holds regardless of scheduling. (At Build Step 4 all nodes carry `stratum_id = 0`; strata detection is Build Step 5. The order machinery is already stratum-aware and will become non-trivial once strata are populated.)

---

## 3. Code — `Bits/simulator/update.py`

Full update loop. `apply_tiebreak` (Milestone 1) retained; `apply_update`, `step`, `hash_state` added.

```python
"""Update mechanics — Build Step 4: the ED substrate update loop.

Implements the asynchronous, canonical-order Sigma-maximizing update:
  - apply_tiebreak : resolve a Sigma-maximal set to a unique winner (Milestone 1).
  - apply_update   : one chain front — score candidates, tie-break, commit, advance.
  - step           : one global step — process active fronts in (stratum_id, node_id)
                     order, commits immediately visible.
  - hash_state     : deterministic hash of the whole StateVector (acyclicity support).

Determinism within a stratum and factorization across strata are properties of
this loop (see module notes and Phase_SimulatorDesign §4).
"""
from __future__ import annotations

from .graph import ParticipationGraph
from .sigma import SigmaCoeffs, compute_candidates, compute_sigma
from .state import StateVector


def apply_tiebreak(u: int, candidates: list[int],
                   graph: ParticipationGraph) -> int:
    """Among Sigma-tied candidates v, return the unique winner whose key
    kappa(v) = (bw(u, v), v) is lexicographically maximal (descending).

    Bandwidth (B2) is the primary key; node id (B1 distinctness) is the final
    key. Total order over distinct node ids ⇒ exactly one winner. Deterministic;
    called even when |candidates| == 1.
    """
    if not candidates:
        raise ValueError("apply_tiebreak called with empty candidate set")
    return max(candidates, key=lambda v: (graph.bw(u, v), v))


def apply_update(u: int, state: StateVector, graph: ParticipationGraph,
                 coeffs: SigmaCoeffs = SigmaCoeffs()):
    """One chain front at u. Returns the committed target v, or None if the
    front extinguishes.

    Steps: enumerate admissible candidates → score Sigma → take the maximal set
    → deterministic tie-break → commit at the winner (irreversibility chokepoint)
    → advance the front (active u -> v). Orientation transport: longitudinal set
    from the committed direction, transverse carried from the source (Phase E §7).

    Extinction: if there are no admissible candidates, or (when
    coeffs.extinction_threshold is not None) the maximal Sigma <= threshold, the
    front extinguishes — it stops, it never reverses (P11/B7).
    """
    cands = compute_candidates(u, state, graph)
    if not cands:
        state[u].active = False
        return None

    sig = {v: compute_sigma(u, v, state, graph, coeffs) for v in cands}
    smax = max(sig.values())

    if coeffs.extinction_threshold is not None and smax <= coeffs.extinction_threshold:
        state[u].active = False
        return None

    maximal = [v for v, s in sig.items() if s == smax]
    winner = apply_tiebreak(u, maximal, graph)

    # Commit at the winner — the SOLE rho writer (B7 chokepoint).
    transverse = state[u].orientation[1:].copy()
    state[winner].commit(
        coeffs.increment,
        longitudinal=float(winner),   # minimal: encode committed direction by target id
        transverse=transverse,
    )

    # Advance the front: u -> winner.
    state[u].active = False
    state[winner].active = True
    return winner


def step(state: StateVector, graph: ParticipationGraph,
         coeffs: SigmaCoeffs = SigmaCoeffs()) -> int:
    """One global step. Process active fronts in canonical (stratum_id, node_id)
    order; each commit is visible to later fronts in the same step (asynchronous).

    Returns the number of commits this step (0 ⇒ fixed point: all fronts
    extinguished). A front that advances into a node this step does NOT take a
    second hop the same step (newly-active fronts wait until the next step).
    """
    order = sorted(state.active_nodes(), key=lambda u: (state.stratum_id(u), u))
    newly_active: set[int] = set()
    commits = 0
    for u in order:
        if u in newly_active:        # advanced into this step ⇒ wait for next step
            continue
        if not state.is_active(u):   # extinguished earlier this step
            continue
        v = apply_update(u, state, graph, coeffs)
        if v is not None:
            commits += 1
            newly_active.add(v)
    return commits


def hash_state(state: StateVector) -> int:
    """Deterministic hash of the entire StateVector — used by the acyclicity
    gate. Signature = sorted tuple of (node_id, rho, orientation...), rounded to
    suppress float noise. Two states with identical (rho, orientation) on every
    node hash identically; any difference changes the hash.
    """
    sig = tuple(
        (
            node_id,
            round(st.rho, 12),
            tuple(round(float(o), 12) for o in st.orientation),
        )
        for node_id, st in sorted(state.items())
    )
    return hash(sig)
```

Supporting change — `SigmaCoeffs` gains an extinction control (`sigma.py`):

```python
    # Extinction: when not None, a front stops once its maximal Sigma <= this
    # threshold (Phase D: "no positive-Sigma continuation"). When None, fronts
    # propagate as long as admissible candidates exist (used by bounded-step demos).
    extinction_threshold: float | None = None
```

`__init__.py` now also exports `apply_update`, `step`, `hash_state`.

---

## 4. Global State Hashing (Acyclicity Support)

`hash_state` (above) produces a deterministic hash of the **entire** StateVector: a sorted tuple of `(node_id, ρ, orientation…)` per node, rounded to 12 decimals to suppress float noise, then hashed. Properties:

- **Deterministic:** identical states ⇒ identical hash, run to run (confirmed in §6 — two runs share every hash).
- **Total:** any difference in any node's ρ or orientation changes the hash.
- **Acyclicity tool:** the Build Step 9 acyclicity gate collects `hash_state` per step and asserts all are distinct. Because ρ is monotone (I4) and every step commits, total ρ strictly rises, so a repeat is structurally impossible — the hash check is the executable guard against an implementation that violates this.

---

## 5. Minimal Example Script — `Bits/examples/update_loop_demo.py`

A 5-node path, one seeded front, six steps; prints per-step ρ and hash; checks monotonicity, distinct hashes, and determinism (two runs).

```python
"""Build Step 4 demo - the ED substrate update loop.

Constructs a small path graph, seeds one active front, runs several steps, and
checks the two properties the update loop must guarantee:
  Gate 1 (monotonicity): rho never decreases, anywhere, between steps.
  Gate 2 (acyclicity):   the global state hash is distinct every step.

Plus a determinism re-run (identical trajectory for identical inputs).
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
    step,
    hash_state,
)

N = 5          # path nodes 0-1-2-3-4
STEPS = 6


def build_path(n):
    g = ParticipationGraph()
    g.add_node(0)
    for i in range(1, n):
        g.add_edge(i - 1, i, bandwidth=0.5)   # uniform bw ⇒ ties resolved by node id
    return g


def fresh_state(n, seed_node=0):
    sv = StateVector()
    for i in range(n):
        sv[i] = NodeState(rho=0.0, orientation=np.array([0.0, 0.0]))
    sv[seed_node].active = True
    return sv


def rho_vector(sv, n):
    return [sv[i].rho for i in range(n)]


def run(coeffs, label):
    g = build_path(N)
    sv = fresh_state(N)
    print(f"\n--- {label} ---")
    hashes = []
    rho_prev = rho_vector(sv, N)
    print(f"  step 0  rho={rho_prev}  hash={hash_state(sv) & 0xffffffff:08x}")
    hashes.append(hash_state(sv))
    monotone = True
    for t in range(1, STEPS + 1):
        commits = step(sv, g, coeffs)
        rho_now = rho_vector(sv, N)
        h = hash_state(sv)
        # monotonicity: elementwise non-decreasing vs previous step
        if any(b < a for a, b in zip(rho_prev, rho_now)):
            monotone = False
        print(f"  step {t}  rho={rho_now}  commits={commits}  "
              f"hash={h & 0xffffffff:08x}")
        hashes.append(h)
        rho_prev = rho_now
    distinct = len(set(hashes)) == len(hashes)
    return hashes, monotone, distinct


def main():
    print("=" * 64)
    print("BUILD STEP 4 - update loop (Gates 1 & 2 preview)")
    print("=" * 64)

    coeffs = SigmaCoeffs(kc=1.0, ks=1.0, kg=1.0, rho_star=0.5)  # no extinction: bounded-step demo

    h1, monotone, distinct = run(coeffs, "run 1")
    h2, _, _ = run(coeffs, "run 2 (determinism check)")
    deterministic = (h1 == h2)

    print("\nChecks")
    print(f"  Gate 1  monotonicity (rho never decreases) : {monotone}")
    print(f"  Gate 2  acyclicity   (distinct hash/step)  : {distinct}")
    print(f"  determinism (run1 hashes == run2 hashes)   : {deterministic}")

    passed = monotone and distinct and deterministic
    print("\n" + "=" * 64)
    print(f"BUILD STEP 4: {'PASS' if passed else 'FAIL'}")
    print("=" * 64)
    return passed


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
```

---

## 6. Acceptance Criteria for Build Step 4 — Result

Executed; **PASS** (exit 0). Recorded output:

```
================================================================
BUILD STEP 4 - update loop (Gates 1 & 2 preview)
================================================================

--- run 1 ---
  step 0  rho=[0.0, 0.0, 0.0, 0.0, 0.0]  hash=e896452f
  step 1  rho=[0.0, 1.0, 0.0, 0.0, 0.0]  commits=1  hash=3710b634
  step 2  rho=[0.0, 1.0, 1.0, 0.0, 0.0]  commits=1  hash=11b9c0f1
  step 3  rho=[0.0, 1.0, 1.0, 1.0, 0.0]  commits=1  hash=8fb2dc02
  step 4  rho=[0.0, 1.0, 1.0, 1.0, 1.0]  commits=1  hash=48862cf4
  step 5  rho=[0.0, 1.0, 1.0, 2.0, 1.0]  commits=1  hash=da16616d
  step 6  rho=[0.0, 1.0, 1.0, 2.0, 2.0]  commits=1  hash=63efd168

--- run 2 (determinism check) ---   [identical hashes e896452f … 63efd168]

Checks
  Gate 1  monotonicity (rho never decreases) : True
  Gate 2  acyclicity   (distinct hash/step)  : True
  determinism (run1 hashes == run2 hashes)   : True

================================================================
BUILD STEP 4: PASS
================================================================
```

| Criterion | Result |
|---|---|
| Runs without errors | **PASS** (exit 0) |
| ρ strictly non-decreasing | **PASS** (Gate 1 True) |
| Distinct global state hash per step | **PASS** (Gate 2 True) |
| Tie-break determinism preserved (Milestone 1) | **PASS** (M1 re-run exit 0; demo runs identical) |

**Trajectory note (acyclicity made visible).** The front fills 0→1→2→3→4 (steps 1–4), then at the path end **retraces into node 3** (step 5, `rho[3]` 1→2) and back to 4 (step 6). The front *spatially revisits* nodes, yet **no global state recurs** — every commit raises total ρ, so each hash is new. This is precisely Gate 2's content: acyclicity is a property of the global state (guaranteed by ρ-monotonicity), not spatial non-revisiting. (ρ accrues at the entered node, so `rho[0]` stays 0.) Detail in `BuildStep4_Results.md`.

---

## 7. Next Steps (Preview)

| Step | Build | Unlocks |
|---|---|---|
| **5** | Reach-stratum detection (`strata.py`) — reciprocal-subgraph components; populate `stratum_id` | stratum-aware order; precondition for Gate 3 |
| **6** | Decoupling-surface detection (`boundary.py`, constructed) | the MWE's decoupled bridge |
| **7** | `HistoryRecorder` (`recorder.py`) — `.npz` + JSON | informational half of Gate 3 |
| **8** | MWE (`examples/mwe_16node.py`) — two strata, end to end | the first measurement-shaped run |
| **9** | Full test suite — five files | Gate 3 (factorization) executable |
| **10** | Run all four gates on the MWE | acceptance: simulator certified |

---

## 8. Deliverables

Produced and verified:

- **`Bits/simulator/update.py`** — full update loop (`apply_update`, `step`, `hash_state`) plus retained `apply_tiebreak`; `SigmaCoeffs.extinction_threshold` added; `__init__.py` exports updated.
- **`Bits/examples/update_loop_demo.py`** — runnable; demonstrates Gates 1 & 2 and determinism.
- **`Bits/BuildStep4_Results.md`** — recorded run, acceptance table, trajectory reading.

**Gates 1 & 2 demonstrated; Gate 4 intact.** Per program discipline, **no Δ is measured until all four gates pass** in the formal suite (Build Step 10). Build Step 4 produces the first real ED trajectories; the next deliverable is reach-stratum detection.

---

## 9. Next Actions

Proceed to **Build Step 5 — reach-stratum detection** (`strata.py`): connected components of the reciprocal (non-decoupled) subgraph, writing `NodeState.stratum_id`. This makes the canonical order genuinely stratum-aware and is the precondition for Gate 3 (factorization), which needs distinct strata to test that decoupling severs reciprocal participation.

---

*End of Build Step 4 implementation. The update loop is live and deterministic; Gates 1 & 2 are demonstrated on real trajectories; Milestone 1 is intact. The next deliverable is reach-stratum detection.*
