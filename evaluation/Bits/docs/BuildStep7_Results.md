# Build Step 7 — Results (HistoryRecorder)

**Program:** Determinability-boundary bits-measurement (empirical arc)
**Build step:** 7 — HistoryRecorder
**Status:** **PASS** (exit 0); Steps 4–6 and Milestone 1 regressions **PASS**
**Date run:** June 2026
**Author:** Allen Proxmire
**Code:** `Bits/simulator/recorder.py` (`HistoryRecorder`); `update.py` `step()` recording hook; `Bits/examples/recorder_demo.py`
**Related:** `Phase_Recorder_Implementation.md`; `Phase_SimulatorDesign.md` §7

---

## Verdict

**Build Step 7 PASSES.** The `HistoryRecorder` captures per-step ρ/orientation snapshots and the commit log append-only, attaches topology/strata/boundary metadata, and exports `.npz` + JSON that reload faithfully. Recording does not perturb the run. With `recorder.py` filed, **all 7 simulator modules are complete.** No regression in Steps 4–6 or Milestone 1.

## Recorded output

```
================================================================
BUILD STEP 7 - HistoryRecorder
================================================================

  rho_history shape         : (6, 6)   (T x |V|)
  orientation_history shape : (6, 6, 2)   (T x |V| x k)
  committed_edges shape     : (10, 3)   (C x 3: t,u,v)
  final rho                 : [0.0, 3.0, 2.0, 0.0, 3.0, 2.0]
  metadata.strata           : {'0': 0, '1': 0, '2': 0, '3': 1, '4': 1, '5': 1}
  metadata.decoupled_edges  : [[2, 3]]
  metadata.boundary_nodes   : [2, 3]
  exported npz              : run.npz
  exported json             : run.json

Checks
  npz round-trip (rho)         : True
  json round-trip (metadata)   : True
  recording does not perturb   : True
  recorded rho monotone        : True
  metadata correct             : True

================================================================
BUILD STEP 7: PASS
================================================================
```

Regressions: boundary, strata, update_loop, milestone1 — all exit 0.

## Acceptance (Step 7 criteria)

| Criterion | Result |
|---|---|
| No mutation of simulation state (recording is read-only) | **PASS** (run identical with/without recorder) |
| Correct metadata (topology / strata / boundary) | **PASS** (strata, decoupled_edges, boundary_nodes all correct) |
| Clean export + faithful reload | **PASS** (`.npz` ρ and JSON metadata round-trip) |
| Append-only / monotone snapshots | **PASS** (Δρ ≥ 0 across all recorded steps) |
| No regression (Milestone 1, Steps 4–6) | **PASS** (all exit 0) |

## Two findings worth recording

**1. A clean factorization preview.** Final ρ = `[0.0, 3.0, 2.0, 0.0, 3.0, 2.0]` — the two strata are **mirror-identical**: cluster A (nodes 0,1,2) = `[0,3,2]`, cluster B (nodes 3,4,5) = `[0,3,2]`. Two independent fronts, seeded at the isomorphic "ends" (nodes 0 and 3) of two decoupled, structurally identical clusters, produced **byte-identical fills**. This is exactly what factorization predicts: the strata are causally independent (no channel crosses the decoupled bridge), so each evolves on its own — and being isomorphic, they evolve identically. This is a *preview*, not the Gate 3 test (which formally asserts a commit in A leaves B unchanged and across-boundary MI ≈ 0, Build Step 9); but the symmetry is the behavior Gate 3 will confirm, visible already.

**2. A demo-only bug, caught and fixed (recorder was correct).** The first run reported `metadata correct: False`. The cause was in the *demo's assertion*, not the recorder: `metadata()` stores strata with **string** keys (`{'0':0, …}`) so the JSON sidecar is valid (JSON object keys must be strings), but the demo compared against **int** keys. The recorder's output was correct; the test's expectation was wrong. Fixed the comparison to use string keys; re-ran → PASS. Recorded here because it is a real (if small) instance of the test, not the code, being at fault — and the JSON-string-key convention is a deliberate, correct choice.

## Notes

- **Append-only, read-only.** `snapshot` and `log_commit` only append; `export` only reads. The recorder never touches `NodeState` — confirmed by the no-perturbation check (final ρ identical with and without a recorder). History is itself irreversible, consistent with the substrate it records.
- **Export schema.** `.npz` holds `nodes`, `steps`, `rho_history` [T,|V|], `orientation_history` [T,|V|,k], `committed_edges` [C,3]=(t,u,v). JSON sidecar holds nodes, edges (with bw + decoupled), decoupled_edges, boundary_nodes, boundary_map, strata, params, seed, counts. This is the exact contract the analysis layer (`analysis/`) consumes for entropy/MI/Δ.
- **`step()` recording hook is non-breaking.** `step(..., recorder=rec, t=t)` logs commits and snapshots; omit the args and behavior is identical to Build Steps 4–6. All four prior demos re-run unchanged.
- **`.npz` outputs are gitignored** (`Bits/.gitignore`) — trajectory artifacts are regenerable and not committed.

## Milestone: simulator package complete

With Build Step 7, all seven simulator modules exist and are green:

```
simulator/  graph  state  sigma  update  strata  boundary  recorder   (7/7)
```

The selection mechanics, dynamics, reach partition, boundary detection, and instrumentation are all built and individually verified. What remains is **assembly and certification**, not new components.

## Scope boundary

Build Step 7 supplies the recorded trajectories Gate 3 and Δ consume. It does **not** run the MWE or test factorization — those are Steps 8 and 9. **No Δ until all four gates pass (Step 10).**

## Next action

**Build Step 8 — the MWE** (`examples/mwe_16node.py`): two 8-node clusters, a decoupled bridge, independent seeds, evolved to the fixed point with full recording. The first measurement-shaped run — and the substrate for the Gate 3 factorization test (Step 9).

---

*End of Build Step 7 results. The HistoryRecorder is live, append-only, read-only, with faithful export; the simulator package is complete (7/7 modules); a factorization preview is already visible. Next: the 16-node MWE.*
