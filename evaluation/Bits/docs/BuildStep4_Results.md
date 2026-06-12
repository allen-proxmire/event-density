# Build Step 4 — Results (Update Loop)

**Program:** Determinability-boundary bits-measurement (empirical arc)
**Build step:** 4 — the ED substrate update loop
**Status:** **PASS** (exit code 0); Milestone 1 regression **PASS**
**Date run:** June 2026
**Author:** Allen Proxmire
**Code:** `Bits/simulator/update.py` (`apply_update`, `step`, `hash_state`); `Bits/examples/update_loop_demo.py`
**Related:** `Phase_UpdateLoop_Implementation.md`; `Phase_SimulatorDesign.md` §4

---

## Verdict

**Build Step 4 PASSES.** The update loop runs, produces deterministic trajectories, and satisfies the two properties Gates 1 and 2 will formally assert:

- **Gate 1 (monotonicity):** ρ never decreases — **True**.
- **Gate 2 (acyclicity):** the global state hash is distinct every step — **True**.
- **Determinism:** two runs with identical inputs produce bit-identical hash sequences — **True**.

Milestone 1 (Gate 4) **still passes** after the `update.py` rewrite — no regression.

## Recorded output

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

--- run 2 (determinism check) ---
  step 0  rho=[0.0, 0.0, 0.0, 0.0, 0.0]  hash=e896452f
  step 1  rho=[0.0, 1.0, 0.0, 0.0, 0.0]  commits=1  hash=3710b634
  step 2  rho=[0.0, 1.0, 1.0, 0.0, 0.0]  commits=1  hash=11b9c0f1
  step 3  rho=[0.0, 1.0, 1.0, 1.0, 0.0]  commits=1  hash=8fb2dc02
  step 4  rho=[0.0, 1.0, 1.0, 1.0, 1.0]  commits=1  hash=48862cf4
  step 5  rho=[0.0, 1.0, 1.0, 2.0, 1.0]  commits=1  hash=da16616d
  step 6  rho=[0.0, 1.0, 1.0, 2.0, 2.0]  commits=1  hash=63efd168

Checks
  Gate 1  monotonicity (rho never decreases) : True
  Gate 2  acyclicity   (distinct hash/step)  : True
  determinism (run1 hashes == run2 hashes)   : True

================================================================
BUILD STEP 4: PASS
================================================================
```

## Acceptance (Implementation Plan / Step 4)

| Criterion | Result |
|---|---|
| Runs without errors | **PASS** (exit 0) |
| ρ strictly non-decreasing across steps | **PASS** (Gate 1 True) |
| Distinct global state hash per step (no cycles) | **PASS** (Gate 2 True) |
| Tie-break determinism preserved (Milestone 1) | **PASS** (re-run identical; M1 exit 0) |

## Reading the trajectory (a teaching point for acyclicity)

The front starts at node 0 and fills the path forward: steps 1–4 commit at nodes 1, 2, 3, 4 (`rho` rises 0→1 at each). At step 5 the front, now at the path end (node 4), has only neighbor 3 and **moves back into 3** (`rho[3]` 1→2). At step 6 it advances to 4 again (`rho[4]` 1→2).

This is the key acyclicity insight made visible: **the front spatially revisits nodes 3 and 4, yet the global state never repeats.** Acyclicity (Gate 2) is a property of the *global state vector*, guaranteed by ρ-monotonicity (I4) — not a claim that a front never re-enters a node. Every commit strictly raises total ρ, so each step's hash is new even when the front retraces its path. The demo exhibits exactly the Phase D structure: the dynamics are acyclic in state despite bounded, revisiting motion in space.

(Note: ρ accrues at the *entered* node, not the source — so `rho[0]` stays 0; the seed node is never committed into in this topology.)

## Notes

- **Determinism is exact.** Run 1 and run 2 produce identical 32-bit hash prefixes at every step (`e896452f … 63efd168`). The evolution is a deterministic function of (graph, initial state, coeffs); no randomness in `step`.
- **Single chokepoint upheld.** Every ρ change went through `NodeState.commit`; monotonicity held with no special-casing.
- **Extinction not exercised here.** The demo uses `extinction_threshold=None` (bounded-step propagation) so the front keeps moving for the fixed 6 steps. Threshold-based extinction (Phase D fixed-point termination) is available for realistic runs and will be exercised in the MWE (Build Step 8).
- **Environment:** Python 3 + NumPy; package imports via `sys.path` insertion of `Bits/`.

## Scope boundary

Build Step 4 demonstrates Gates 1 & 2 on a single-stratum path. The **formal** gates run in the test suite (Build Step 9) over multiple configurations including the MWE. Gate 3 (factorization) still requires strata (Step 5), boundaries (Step 6), and the recorder (Step 7). **No Δ until all four gates pass (Step 10).**

## Next action

**Build Step 5 — reach-stratum detection** (`strata.py`): connected components of the reciprocal (non-decoupled) subgraph; populate `NodeState.stratum_id`. This makes the canonical order genuinely stratum-aware and is the precondition for Gate 3.

---

*End of Build Step 4 results. The update loop is live; Gates 1 & 2 demonstrated; determinism exact; Milestone 1 intact. Next: reach-stratum detection.*
