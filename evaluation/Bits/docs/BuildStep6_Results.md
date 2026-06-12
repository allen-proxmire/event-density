# Build Step 6 — Results (Decoupling-Surface Detection)

**Program:** Determinability-boundary bits-measurement (empirical arc)
**Build step:** 6 — decoupling-surface detection
**Status:** **PASS** (exit 0); Steps 4, 5 and Milestone 1 regressions **PASS**
**Date run:** June 2026
**Author:** Allen Proxmire
**Code:** `Bits/simulator/boundary.py` (`detect_decoupled_edges`, `detect_boundary_nodes`, `boundary_map`); `Bits/examples/boundary_demo.py`
**Related:** `Phase_Boundary_Implementation.md`; `Phase_SimulatorDesign.md` §6

---

## Verdict

**Build Step 6 PASSES.** Decoupling surfaces are detected directionally; the bridge `(2,3)` is identified as the surface; boundary nodes are exactly `{2,3}`; `boundary_map` anchors each boundary node to its across-surface partner; strata are unperturbed. No regression in Steps 4, 5, or Milestone 1.

## Recorded output

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

## Acceptance (Step 6 criteria)

| Criterion | Result |
|---|---|
| `detect_decoupled_edges` returns exactly the decoupled edges | **PASS** (`[(2,3)]`) |
| `detect_boundary_nodes` returns exactly nodes incident to decoupled edges | **PASS** (`{2,3}`) |
| `boundary_map` deterministic and stable across runs | **PASS** (`{2:[3], 3:[2]}`, repeated identical) |
| No regression (Milestone 1, Step 4, Step 5) | **PASS** (all exit 0) |

## What this establishes

The decoupling surface is now an **explicit, queryable object**, not just an implicit gap in the strata flood:

- **`detect_decoupled_edges`** — the surfaces themselves, as sorted canonical `(min,max)` pairs. Here `[(2,3)]`.
- **`detect_boundary_nodes`** — the nodes that sit on a surface (`{2,3}`). These are the anchors for Δ's near-boundary regions.
- **`boundary_map`** — for each boundary node, its across-surface partner(s): `{2:[3], 3:[2]}`. This is the Δ across-boundary pairing in raw form — node 2 (stratum 0) paired with node 3 (stratum 1) across the surface.

Strata (Step 5) and boundaries (Step 6) are now **two complementary views of the same cut**: strata say *which side* each node is on; boundaries say *where the cut is*. Together they give Gate 3 everything it needs — distinct strata to prove independence, and the explicit surface to prove nothing crosses it.

## Notes

- **Directional by design, symmetric in practice.** `detect_decoupled_edges` treats an edge as a surface if decoupled in *either* direction (`decoupled(u,v) OR decoupled(v,u)`). The current `ParticipationGraph` stores the flag on a shared edge record, so both directions agree — this models **reciprocal** ("true boundary") decoupling, which is what the MWE and Gate 3 use. The OR is written directionally so that one-sided surfaces (per-direction storage) would be detected correctly if added later. This is a forward-compatible interface, not dead code: it encodes the Phase E §6 rule that *one* severed direction is enough to make a boundary.
- **Boundaries do not perturb strata.** `boundary.py` only *reads* the graph; it never flips a flag. The strata map is byte-identical before and after boundary detection (`strata unchanged: True`). The two modules integrate by sharing the same `decoupled` flag as source of truth — `strata.py` excludes those edges from the flood, `boundary.py` enumerates them.
- **Deterministic, sorted output.** Edges are canonical `(min,max)` and sorted; `boundary_map` keys and values are sorted. Required for reproducible Δ pairings.
- **No `update.py` change.** As scoped — boundary information is consumed by Gate 3, the MWE, and Δ pairing, not by the update loop.

## Scope boundary

Build Step 6 makes the determinability boundary explicit and queryable. It does **not** test factorization — Gate 3 needs the recorder (Step 7) to capture cross-boundary histories and the MWE (Step 8) to run a two-stratum trajectory. **No Δ until all four gates pass (Step 10).**

## Next action

**Build Step 7 — `HistoryRecorder`** (`recorder.py`): append-only per-step snapshots of ρ and orientation, the committed-event log, and `.npz` + JSON export. This supplies the recorded histories that the informational half of Gate 3 (across-boundary MI ≈ 0) and Δ both consume.

---

*End of Build Step 6 results. Decoupling surfaces are explicit and queryable; boundary nodes and across-surface pairings exposed; strata unperturbed; no regression. Next: the HistoryRecorder.*
