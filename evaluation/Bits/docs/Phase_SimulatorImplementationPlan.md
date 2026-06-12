# Phase Bits / Simulator Implementation Plan

**Program:** Determinability-boundary bits-measurement (empirical arc)
**Document:** Implementation plan — design → buildable code
**Status:** Pre-code; defines module layout, skeletons, tests, and build order
**Date filed:** June 2026
**Author:** Allen Proxmire
**Related:** `Phase_SimulatorDesign.md` (the design this operationalizes); `../../Phase_TieBreak_Specification.md` (tie-break); `../../Phase_Bits_DeterminabilityBoundaryMeasurementPlan.md` (the program & Δ)

---

## 1. Purpose

This document operationalizes `Phase_SimulatorDesign.md` into an **actionable build plan**: the concrete module layout, class/function skeletons, test definitions, and build order required to produce a minimal, correct ED-substrate simulator.

The goal is a **minimal, correct** simulator capable of generating trajectories for Δ measurement — not a performant or general one. Minimality is a feature: the smaller the faithful core, the easier it is to prove it implements the closed specification exactly.

**Correctness gates precede measurement, without exception.** The four gates — **I4 monotonicity, acyclicity, factorization, tie-break uniqueness** — must pass before any Δ is computed. They are not regression tests bolted on after; they are the acceptance criteria for the simulator's existence. A simulator that measures Δ but fails factorization is measuring an artifact. Build order (§6) is sequenced so the gates can be run as early as possible and block progression.

---

## 2. Repository Layout

Proposed structure under `evaluations/ED_Substrate/Bits/`:

```
Bits/
  Phase_SimulatorDesign.md
  Phase_SimulatorImplementationPlan.md         # this document
  simulator/
    __init__.py            # public API surface; version
    graph.py               # ParticipationGraph (design §3 — B2)
    state.py               # NodeState, StateVector (design §3 — B1/B4/B5)
    sigma.py               # Σ functional, candidate enumeration (design §4)
    update.py              # tie-break, commit, step loop (design §4)
    strata.py              # reach-stratum detection (design §5 — B6/Phase E)
    boundary.py            # decoupling-surface id & marking (design §6 — B6)
    recorder.py            # HistoryRecorder, export (design §7)
  tests/
    test_monotonicity.py   # gate 1 (I4)
    test_acyclicity.py     # gate 2
    test_factorization.py  # gate 3
    test_tiebreak.py       # gate 4
    test_mwe.py            # integration: 16-node, all four gates
  analysis/                # EXTERNAL to the simulator; consumes its output only
    delta.py               # Δ = baseline − across (M1/M2/M3 assembly)
    entropy.py             # graph-general Shannon / MI estimators (NOT spectral)
    correlation.py         # matched-separation pairing helpers
  examples/
    mwe_16node.py          # the runnable MWE (design §9)
```

**Module ↔ design-section map:**

| Module | Design §  | Corpus element |
|---|---|---|
| `graph.py` | §3 | Participation graph B2 (bandwidth-weighted channels) |
| `state.py` | §3 | Events B1, commitment density B4, orientation B5 |
| `sigma.py` | §4 | Σ = Coh − Str − Grad (orientation-blind) |
| `update.py` | §4 | Tie-break, commit, irreversibility B7, canonical-order loop |
| `strata.py` | §5 | Reach strata (reciprocal subgraph components) |
| `boundary.py` | §6 | Decoupling surfaces B6 (constructed + emergent) |
| `recorder.py` | §7 | Instrumentation → `.npz` + JSON |
| `analysis/*` | §8 | External; M1/M2/M3, Δ |

The `simulator/` package is substrate-faithful and self-contained; `analysis/` imports nothing from a running simulation — only its emitted files. This boundary is structural (design §1, §8) and is enforced by keeping `analysis/` free of any `simulator/` import.

---

## 3. Module Specifications

Signatures below are the **contract**; bodies are the build (§6). Types are indicative (this is plain Python + NumPy).

### `graph.py`

```python
class ParticipationGraph:
    """B2: bandwidth-weighted participation graph. Node ids are the B1 distinct
    identities and serve as the tie-break final key σ."""
    def __init__(self): ...
    def add_node(self, node_id: int) -> None: ...
    def add_edge(self, u: int, v: int, bw: float, decoupled: bool = False) -> None: ...
    def neighbors(self, u: int) -> list[int]:
        """All v adjacent to u (both reciprocal and one-sided)."""
    def admissible_neighbors(self, u: int) -> list[int]:
        """Candidate set 𝒩(u): v adjacent to u via a NON-decoupled edge.
        Reach-bounded; respects B6. Cached; invalidated only on decoupled-flag flip."""
    def bw(self, u: int, v: int) -> float: ...
    def is_decoupled(self, u: int, v: int) -> bool: ...
    def set_decoupled(self, u: int, v: int, flag: bool) -> None: ...
    def edges(self) -> Iterable[tuple[int, int, dict]]: ...
```

Backing store: adjacency-list (`dict[int, dict[int, EdgeData]]`). `admissible_neighbors` cache keyed by node, invalidated by `set_decoupled`.

### `state.py`

```python
class NodeState:
    """B1/B4/B5 per-node state."""
    rho: float                 # B4 commitment density; monotone non-decreasing (B7)
    orientation: np.ndarray    # B5; [0]=longitudinal (derivable), [1:]=transverse (primitive)
    committed: bool
    active: bool               # chain front present
    stratum_id: int

class StateVector:
    """Whole-substrate state: array-of-NodeState with vectorized accessors."""
    def __init__(self, n_nodes: int, orientation_dim: int): ...
    def rho_array(self) -> np.ndarray:        # shape [|V|]
    def orientation_array(self) -> np.ndarray:# shape [|V|, k]
    def active_nodes(self) -> list[int]: ...
    def commit(self, v: int, increment: float, longitudinal: np.ndarray,
               transverse: np.ndarray) -> None:
        """ρ[v] += increment (assert non-negative increment); set committed;
        write orientation. The ONLY mutator of ρ; never decrements."""
```

`commit` is the single write path for ρ — every irreversibility guarantee funnels through it, so the monotonicity assertion lives in exactly one place.

### `sigma.py`

```python
def compute_candidates(u: int, graph: ParticipationGraph) -> list[int]:
    """𝒩(u) = graph.admissible_neighbors(u). Thin wrapper for testability."""

def compute_sigma(u: int, v: int, sv: StateVector, graph: ParticipationGraph,
                  coeffs: SigmaCoeffs) -> float:
    """Σ(e′) = κ_c·Coh − κ_s·Str − κ_g·Grad, evaluated for transition u→v.
    HARD INVARIANT: reads ρ and graph-local data ONLY. Must NOT read orientation
    (Σ is orientation-blind, Phase D §5). Enforced by code review + a guard test."""
    rho_u, rho_v = sv.rho_at(u), sv.rho_at(v)
    coh  = coeffs.kc * coherence(u, v, sv, graph)   # stabilizing (+)
    strn = coeffs.ks * rho_v                         # destabilizing (−)
    grad = coeffs.kg * abs(rho_v - rho_u)            # destabilizing (−)
    return coh - strn - grad

def coherence(u, v, sv, graph) -> float:
    """Local consistency functional on the commitment field. Orientation-free.
    Reference default: closeness of ρ(v) to the chain's running trajectory."""
```

`SigmaCoeffs` is a small frozen dataclass `(kc, ks, kg, increment)`.

### `update.py`

```python
def apply_tiebreak(u: int, sigma_max_set: list[int],
                   graph: ParticipationGraph) -> int:
    """Among the Σ-maximal candidates v, return the unique winner by lexicographic
    key κ(v) = (bw(u,v), v), descending. Total order ⇒ exactly one winner
    (Phase_TieBreak_Specification §5). Called ALWAYS, even when |set| == 1."""

def apply_update(u: int, sv: StateVector, graph, coeffs) -> Optional[int]:
    """One chain front at u: enumerate candidates → score → argmax → tie-break →
    commit at winner v → transport orientation → advance front (active u→v).
    Returns v, or None if no admissible positive step (front extinguishes)."""

def step(sv: StateVector, graph, coeffs, recorder=None) -> int:
    """One global step: process active nodes in canonical order (§4).
    Returns number of commits this step (0 ⇒ fixed point reached)."""
```

### `strata.py`

```python
def compute_strata(graph: ParticipationGraph) -> dict[int, int]:
    """Connected components of the RECIPROCAL subgraph (non-decoupled edges only).
    BFS/DFS flood. One-sided edges do NOT merge strata (Phase E §6).
    Returns node_id -> stratum_id."""

def assign_stratum_ids(sv: StateVector, graph: ParticipationGraph) -> None:
    """Write stratum_id onto every NodeState. Called once at init for constructed
    surfaces (static); re-called on decoupled-flag flips for emergent mode."""
```

### `boundary.py`

```python
def mark_constructed_surfaces(graph, decoupled_edges: list[tuple[int,int]]) -> None:
    """Primary mode: set decoupled=True on the given edges (hard cut)."""

def detect_decoupling_surfaces(graph, sv, criterion: BoundaryCriterion) -> list[tuple]:
    """Emergent/robustness mode: return edges newly failing reciprocity under a
    SINGLE fixed criterion (bw_eff < τ_reach) OR (|Δρ| > τ_grad). Not mixed.
    Flipping a flag must trigger strata recomputation by the caller."""

def boundary_nodes(graph) -> set[int]:
    """Nodes incident to ≥1 decoupled edge — cached for Δ pairing (design §6/§7)."""
```

### `recorder.py`

```python
class HistoryRecorder:
    """Append-only instrumentation (design §7). History is itself irreversible."""
    def __init__(self, n_nodes, orientation_dim, T_hint=None,
                 region_defs=None, pair_defs=None): ...
    def snapshot(self, t: int, sv: StateVector) -> None:
        """Append ρ[t,:], orientation[t,:,:]; log committed events."""
    def log_commit(self, t: int, u: int, v: int) -> None: ...
    def export(self, path_prefix: str) -> None:
        """Write <prefix>.npz (rho_history, orientation_history, committed_edges,
        region index sets) + <prefix>.json (topology, decoupled set, stratum map,
        region/pair defs, params, seed). One pair of files per run."""
```

---

## 4. Update Loop Specification

The canonical step (design §4), stated as the build target for `update.step`:

```
def step(sv, graph, coeffs, recorder):
    commits = 0
    # Canonical order: ascending (stratum_id, node_id). Deterministic.
    order = sorted(sv.active_nodes(), key=lambda u: (sv.stratum_id(u), u))
    for u in order:
        if not sv.is_active(u):        # may have been advanced earlier this step
            continue
        v = apply_update(u, sv, graph, coeffs)   # async: commit visible immediately
        if v is not None:
            commits += 1
            if recorder: recorder.log_commit(t, u, v)
    if recorder: recorder.snapshot(t, sv)
    return commits
```

Key properties this loop must guarantee (and the tests verify):

- **Asynchronous, immediately visible.** A commit by an earlier-ordered chain is seen by later chains in the *same* step. No double-buffering. This matches design §4.
- **Determinism within strata.** Ordering by `(stratum_id, node_id)` plus the total tie-break makes the entire evolution a deterministic function of `(graph, initial state, coeffs)`. Same inputs ⇒ bit-identical history (tested in §5).
- **Factorization preserved regardless of order.** Chains in different strata share no admissible edges (decoupled), so processing order never couples strata. The canonical order is purely a within-stratum determinizer; it cannot manufacture or destroy cross-stratum dependence. (This is *why* gate 3 can pass independently of loop scheduling.)

Randomness enters **only** through initial-condition sampling across an ensemble — never inside `step`.

---

## 5. Test Suite Definition

Each gate is an explicit, blocking test.

### `test_monotonicity.py` — gate 1 (I4)
```
Run several configurations (incl. MWE) to the fixed point.
ASSERT for all v, all t2 > t1: rho_history[t2, v] >= rho_history[t1, v].
A single decrement anywhere ⇒ FAIL. (Also unit-test StateVector.commit rejects
negative increments.)
```

### `test_acyclicity.py` — gate 2
```
Evolve; record the per-step global state vector (rho + committed).
ASSERT no state vector recurs (hash set of state signatures, no collisions);
equivalently, total committed ρ strictly increases on every step with commits>0.
```

### `test_factorization.py` — gate 3
```
MWE with INDEPENDENT init in clusters A and B, decoupled bridge (a7,b0).
(a) Structural: commit events in A leave every NodeState in B byte-identical
    across the whole run (and vice versa). Direct, exact check.
(b) Informational: estimated across-boundary MI(A-history ; B-state) ≈ 0
    within estimator tolerance. (Uses analysis/entropy.py; tolerance documented.)
Either failing ⇒ decoupling does not truly sever reciprocal participation.
```

### `test_tiebreak.py` — gate 4
```
Construct a forced Σ-tie: ≥2 candidates with identical Σ by design, with
DISTINCT bandwidths AND, in a second case, EQUAL bandwidths (exercising the
σ=node_id final key).
ASSERT apply_tiebreak returns exactly one v, the lexicographic-max (bw, node_id),
on every occurrence; ASSERT determinism: repeated runs identical.
```

### `test_mwe.py` — integration
```
Build the 16-node two-cluster MWE (examples/mwe_16node.py).
Run to fixed point; then assert ALL FOUR gates on this single run:
monotonicity, acyclicity, factorization (A⊥B), tie-break uniqueness (where ties
occur). Additionally assert determinism: two runs ⇒ identical .npz histories.
This is the acceptance test for "the simulator exists and is correct."
```

A shared `conftest.py` provides builders (`make_cluster`, `make_mwe`, `force_tie_config`) so tests construct graphs declaratively.

---

## 6. Build Order

Strict sequence; each step is independently testable, and the gates come online as early as their dependencies allow.

| Step | Build | Unlocks / testable when done |
|---|---|---|
| **1** | `ParticipationGraph` + `NodeState`/`StateVector` | graph construction, `commit` monotonicity unit test (partial gate 1) |
| **2** | Σ functional (`sigma.py`), orientation-blind | the orientation-blindness guard test |
| **3** | Deterministic tie-break (`apply_tiebreak`) | **gate 4** (`test_tiebreak`) — needs no full loop |
| **4** | Update loop (`apply_update`, `step`) | gate 1 (full), gate 2 once a run completes |
| **5** | Reach-stratum detection (`strata.py`) | canonical-order key; precondition for gate 3 |
| **6** | Decoupling-surface detection (`boundary.py`, constructed mode) | the decoupled bridge for the MWE |
| **7** | `HistoryRecorder` + export | `.npz`/`.json` output; informational half of gate 3 |
| **8** | MWE example (`examples/mwe_16node.py`) | a runnable trajectory end-to-end |
| **9** | Test suite (all five files) | all gates executable |
| **10** | **Run tests until all four gates pass** | acceptance: simulator is correct |

Gate 4 (tie-break) is deliberately buildable at step 3, before the loop exists — it is a pure function of a candidate set and the graph, so it can be proven correct in isolation early. Gate 3 (factorization) is last among the gates because it needs strata (5), boundaries (6), and the recorder (7).

---

## 7. Integration with Analysis Stack

The simulator emits `.npz` + `.json`; `analysis/` consumes them. One-directional, no shared imports (design §8).

- **Entropy estimators (`analysis/entropy.py`) — graph-general, NOT spectral.** ed-lab's `spectral.py` entropy is FFT/DCT on Cartesian grids and does not apply to participation graphs. We reuse only the **Shannon kernel + ε-regularization idiom**, applied to region-state distributions built from `rho_history`/`orientation_history`. A finite-sample-bias-corrected MI estimator (KSG or binned-with-correction) lives here for M1/M2.
- **Correlation-length estimators (`analysis/correlation.py`) — matched-separation.** We borrow ed-lab `correlation.py`'s **separation-matching discipline** (pairing at equal distance), not its grid-specific autocorrelation math. This module builds the (baseline-pair, across-pair) matching at equal **graph** distance.
- **Δ computation (`analysis/delta.py`) — M1/M2/M3.** Assembles `Δ = predictability_within_stratum − predictability_across_boundary`: M1/M2 from `entropy.py`, M3 (within-stratum-restricted predictor) via scikit-learn, calibrated to bits per plan §5/§7. Aggregated across the ensemble.

The simulator computes **no** entropy/MI/Δ. The analysis modules are specified by their interface here and built in a later document; this section fixes only the data contract (the `.npz`/`.json` schema of §3 `recorder.py`).

---

## 8. Deliverables

This plan is complete when it has produced:

1. **A minimal working ED-substrate simulator** that:
   - evolves under **Σ-maximization + deterministic tie-break** (discrete selection, never averaging);
   - computes **reach strata** (reciprocal-subgraph components) and supports **constructed decoupling surfaces**;
   - **passes all four correctness gates** (monotonicity, acyclicity, factorization, tie-break uniqueness) and is **deterministic** (bit-identical histories for identical inputs);
   - **emits paired histories** (`.npz` + `.json`) in the schema Δ requires.
2. **A reproducible MWE demonstration** — `examples/mwe_16node.py` runnable end-to-end, producing the two-stratum trajectory, exporting its histories, and serving as the integration test (`test_mwe.py`).

On these deliverables the empirical arc proceeds to: fix the primary Δ measure (plan §7 step 2), build `analysis/`, and run ensembles. **No Δ is reported until the four gates pass** — the architectural arc's integrity depends on the empirical arc never measuring an artifact.

---

## 9. Next Actions

The next step after this document is **writing the code**, in the build order of §6, beginning with `simulator/graph.py` and `simulator/state.py`. The first runnable milestone is **gate 4 at build step 3** (tie-break uniqueness, provable before the loop exists); the acceptance milestone is **step 10** (all four gates green on the MWE).

This is the boundary between specification and implementation: every document in the corpus to this point — architectural and empirical — has been prose. The next deliverable is a Python package and a passing pytest suite.

---

*End of Implementation Plan. This document defines the build; the next deliverable is the code itself. The simulator is a faithful, minimal transcription of the closed ED-substrate specification, gated by four correctness tests that must pass before any determinability-boundary number is measured.*
