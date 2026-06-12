# Phase Bits / Coding Kickoff — Simulator Core, Milestone 1

**Program:** Determinability-boundary bits-measurement (empirical arc)
**Document:** Coding kickoff — specification → running code
**Status:** Implementation begins; targets the first correctness gate (tie-break uniqueness)
**Date filed:** June 2026
**Author:** Allen Proxmire
**Related:** `Phase_SimulatorDesign.md`; `Phase_SimulatorImplementationPlan.md` (build order §6, module specs §3); `../../Phase_TieBreak_Specification.md`

---

## 1. Purpose

This document transitions the empirical arc **from specification to implementation**. Every prior document — architectural and empirical — has been prose; from here the deliverable is a Python package and a passing test.

The goal of this kickoff is to begin coding the **simulator core**, building only the minimal modules required for the **first correctness gate — tie-break uniqueness (gate 4)**. That gate is chosen first deliberately: per the implementation plan's build order, the tie-break is a *pure function of a candidate set and the graph*, provable in isolation **before** the update loop, strata, or boundaries exist. It is the earliest point at which real code can be proven correct against the closed specification.

**No Δ measurement will be attempted until all four correctness gates pass.** This kickoff produces the first gate's worth of code and nothing downstream of it. Measurement is gated on the full suite (monotonicity, acyclicity, factorization, tie-break uniqueness); this document delivers one of the four and the scaffolding the other three will build on. The discipline is non-negotiable: a number measured on an uncertified simulator is an artifact, and the architectural arc's integrity depends on the empirical arc never reporting one.

---

## 2. Initial Coding Scope (Build Steps 1–3)

Three modules, in dependency order. Signatures follow the implementation plan §3 exactly; this section fixes what gets *built first* and to what depth.

**Step 1 — `simulator/graph.py` : `ParticipationGraph` (B2).**
- Adjacency representation: `dict[int, dict[int, EdgeData]]` (sparse, adjacency-list).
- `add_node(node_id)`, `add_edge(u, v, bw, decoupled=False)`, `neighbors(u)`.
- `admissible_neighbors(u)` — non-decoupled neighbors (the reach-bounded candidate set 𝒩(u)); cached.
- `bw(u, v)`, `is_decoupled(u, v)`, `set_decoupled(u, v, flag)`.
- The **decoupled-edge flag** is the single source of truth for boundaries; node ids are the B1 distinct identities (and the tie-break's final key σ).
- *Depth for Milestone 1:* full, except the cache may be naive (correctness over speed). Strata/boundary helpers are NOT built here.

**Step 2 — `simulator/state.py` : `NodeState`, `StateVector` (B1/B4/B5).**
- `NodeState`: `rho`, `orientation` (`[0]` longitudinal, `[1:]` transverse), `committed`, `active`, `stratum_id`.
- `StateVector`: array-of-states with `rho_array()`, `orientation_array()`, `active_nodes()`, accessors `rho_at(v)`, `is_active(v)`, `stratum_id(v)`.
- **`commit(v, increment, longitudinal, transverse)` is the sole writer of ρ** — the irreversibility chokepoint. It asserts `increment >= 0`, does `rho[v] += increment`, sets `committed`, writes orientation. No other function in the package may assign to ρ. This single-writer rule is what makes the monotonicity gate enforceable in one place.
- *Depth for Milestone 1:* full for `commit`/accessors; `stratum_id` defaults to 0 (strata module not yet built).

**Step 3 — `simulator/sigma.py` + `simulator/update.py` (Σ + tie-break).**
- `sigma.py`:
  - `compute_candidates(u, graph)` → `graph.admissible_neighbors(u)`.
  - `compute_sigma(u, v, sv, graph, coeffs)` → `κ_c·Coh − κ_s·Str − κ_g·Grad`.
  - **Orientation-blindness invariant:** `compute_sigma` and `coherence` read `rho` and graph-local data **only**; they must not reference `orientation`. Enforced by review and by an explicit guard test (§4).
- `update.py` (tie-break only at this step):
  - `apply_tiebreak(u, sigma_max_set, graph)` → unique winner by lexicographic key `κ(v) = (bw(u,v), v)`, descending; total order ⇒ exactly one winner; called even when the set has one element.
  - `apply_update` / `step` are **stubbed or omitted** at Milestone 1 (Build Step 4).

`SigmaCoeffs` (frozen dataclass `kc, ks, kg, increment`) lands in `sigma.py`.

---

## 3. First Runnable Milestone

The smallest script that exercises gate 4 **without** the update loop, strata, or boundaries:

```
examples/milestone1_tiebreak.py

1. Build a tiny ParticipationGraph: one center node u with 3 admissible
   neighbors v1, v2, v3 (distinct bandwidths in case A; two equal bandwidths
   in case B, to exercise the σ = node_id final key).
2. Build a StateVector; assign ρ on v1,v2,v3 so that compute_sigma(u, vi)
   is IDENTICAL across the three (a forced Σ-tie by construction).
3. Compute Σ for each candidate; confirm the Σ-maximal set = {v1, v2, v3}.
4. Call apply_tiebreak(u, [v1,v2,v3], graph); print the winner.
5. Assert exactly one winner; assert it is the lexicographic max of (bw, node_id).
6. Re-run the whole script; assert identical winner (determinism).
```

This milestone runs with only `graph.py`, `state.py`, `sigma.py`, and the tie-break in `update.py`. It needs no `step()`, no `strata.py`, no `boundary.py`, no `recorder.py`. It is the minimal proof that the **selection mechanics** — score, argmax, deterministic tie-break — are faithful to the specification.

---

## 4. Acceptance Criteria for Milestone 1

Three checks, each a blocking assertion (these become `tests/test_tiebreak.py` and a guard test under the full suite at Build Step 9):

**A — Tie-break uniqueness.**
- A forced Σ-tie over ≥2 candidates ⇒ `apply_tiebreak` returns **exactly one** node.
- The returned node is the lexicographic maximum of `(bw(u,v), node_id)`.
- Case A (distinct bandwidths): winner decided by `bw`. Case B (equal bandwidths): winner decided by `node_id` (the B1-distinctness final key).
- Repeated runs ⇒ **identical** selection (determinism).

**B — Orientation-blindness.**
- Compute Σ for the candidate set; record the values.
- Mutate every node's `orientation` to arbitrary different values; recompute Σ.
- Assert Σ is **unchanged** for every candidate. (If Σ moves, `compute_sigma` or `coherence` is reading orientation — a specification violation, hard fail.)

**C — Irreversibility chokepoint.**
- `commit` with a positive increment raises ρ; `commit` with a negative increment **raises/asserts** (rejected).
- A static check (or a small reflection test) confirms **no function other than `commit` assigns to `rho`** — grep-level discipline backed by the single-writer design.

Milestone 1 is accepted when A, B, and C all pass. Gate 4 is then green ahead of the update loop, exactly as the build order intends.

---

## 5. Next Coding Steps (Preview)

After Milestone 1 passes, implementation proceeds down the build order:

- **Build Step 4 — update loop** (`apply_update`, `step`): asynchronous, canonical `(stratum_id, node_id)` order, commits immediately visible. Unlocks gate 1 (monotonicity, full) and gate 2 (acyclicity) once a run completes.
- **Build Step 5 — reach-stratum detection** (`strata.py`): connected components of the reciprocal subgraph. Supplies the canonical-order key and is a precondition for gate 3.
- **Build Step 6 — decoupling-surface detection** (`boundary.py`, constructed mode): the decoupled bridge the MWE needs.
- **Build Step 7 — `HistoryRecorder`** (`recorder.py`): append-only snapshots, `.npz` + JSON export; supplies the informational half of gate 3.
- **Build Step 8 — MWE** (`examples/mwe_16node.py`): the 16-node two-cluster trajectory, end to end.
- **Build Step 9 — full test suite**: all five test files; gate 3 (factorization) becomes executable here.

Acceptance for the whole simulator remains **Build Step 10**: all four gates green on the MWE, with bit-identical histories across identical-input runs.

---

## 6. Deliverables

This kickoff is complete when it has produced:

1. **A minimal codebase under `Bits/simulator/`** containing:
   - `graph.py` — `ParticipationGraph` (full, per §2 Step 1);
   - `state.py` — `NodeState`, `StateVector`, with `commit` as the sole ρ-writer;
   - `sigma.py` — `compute_candidates`, `compute_sigma`, `coherence`, `SigmaCoeffs` (orientation-blind);
   - `update.py` — `apply_tiebreak` (the update loop deferred to Build Step 4);
   - `__init__.py` exposing the public surface.
2. **A runnable example script** (`examples/milestone1_tiebreak.py`) demonstrating tie-break uniqueness, orientation-blindness, and the irreversibility chokepoint.
3. **A short results note** recording Milestone 1's outcome — the printed winner for cases A and B, confirmation of the three acceptance checks, and confirmation of determinism across re-runs. (Filed as `Bits/Milestone1_Results.md` when the code runs.)

On these deliverables the empirical arc has its first certified component: the selection mechanics, proven before anything is built on top of them.

---

## 7. Next Actions

The next step is **writing the four modules and the milestone script**, in the §2 order (`graph.py` → `state.py` → `sigma.py` → `update.py` tie-break), then running `examples/milestone1_tiebreak.py` against the §4 acceptance criteria and recording the result.

This is the first line of code in the empirical arc. Gate 4 is the target; the update loop, strata, boundaries, recorder, and MWE follow in build order, with the full four-gate suite as the acceptance bar before any determinability-boundary number is measured.

---

*End of Coding Kickoff. This document opens implementation and scopes Milestone 1 (tie-break uniqueness). The deliverable is running code: four minimal modules and a script that proves the selection mechanics faithful to the closed specification, ahead of the update loop.*
