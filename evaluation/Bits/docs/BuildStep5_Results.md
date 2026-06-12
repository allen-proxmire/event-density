# Build Step 5 — Results (Reach-Stratum Detection)

**Program:** Determinability-boundary bits-measurement (empirical arc)
**Build step:** 5 — reach-stratum detection
**Status:** **PASS** (exit 0); Build Step 4 and Milestone 1 regressions **PASS**
**Date run:** June 2026
**Author:** Allen Proxmire
**Code:** `Bits/simulator/strata.py` (`compute_strata`, `assign_stratum_ids`); `update.py` `step()` stratum integration; `Bits/examples/strata_demo.py`
**Related:** `Phase_Strata_Implementation.md`; `Phase_SimulatorDesign.md` §5

---

## Verdict

**Build Step 5 PASSES.** Reach strata are computed as connected components of the reciprocal (non-decoupled) subgraph; the decoupling bridge does **not** merge the two clusters; numbering is deterministic; `step()` consumes the stratum ids. Build Step 4 (update loop) and Milestone 1 (tie-break) still pass — no regression.

## Recorded output

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

## Acceptance (Step 5 criteria)

| Criterion | Result |
|---|---|
| Strata match connected components of the reciprocal subgraph | **PASS** (map == expected) |
| Deterministic across runs | **PASS** (repeated `compute_strata` identical) |
| Same-component nodes share a stratum id | **PASS** (A:{0,1,2}=0, B:{3,4,5}=1) |
| Decoupling-separated nodes get different ids | **PASS** (bridge endpoints 2→0, 3→1) |
| Update loop accepts & uses stratum ids | **PASS** (`step(..., strata=labels)` runs) |
| No regression (Milestone 1, Step 4) | **PASS** (both exit 0) |

## The decisive check

The bridge edge `(2, 3)` is marked `decoupled=True`. It is a real edge — `neighbors(2)` includes 3 — but it is excluded from `admissible_neighbors`, so the BFS never traverses it. Result: nodes 2 and 3 land in **different strata** (0 and 1) despite being adjacent. This is the corpus semantics exactly: a decoupling surface severs reciprocal participation, and **strata are components of the reciprocal subgraph, not the full graph** (Phase E §6). One-sided adjacency does not merge strata.

## Notes

- **Deterministic numbering.** Components are labelled in ascending order of their smallest node (seeds taken in ascending id order). Cluster A (smallest node 0) → stratum 0; cluster B (smallest node 3) → stratum 1. The same graph always yields the same ids, run to run — required for reproducible Δ pairings.
- **Two write paths, one truth.** `compute_strata` returns the mapping; `assign_stratum_ids` writes it onto `NodeState.stratum_id` and returns the same mapping. The demo confirms they agree (`assign_stratum_ids writes state: True`).
- **Static for constructed surfaces.** Strata are computed once and held fixed (the MWE regime). The mapping is recomputed only if a `decoupled` flag flips (emergent mode, later robustness studies).
- **`step()` integration is non-breaking.** The optional `strata` mapping overrides `NodeState.stratum_id` for ordering when supplied; otherwise the NodeState value (populated by `assign_stratum_ids`) is used. Both Build Step 4 and Milestone 1 re-run unchanged.

## Scope boundary

Build Step 5 supplies the stratum labels that Gate 3 (factorization) will test against. It does **not** itself test factorization — that needs the boundary module (Step 6), the recorder (Step 7), and the MWE (Step 8). **No Δ until all four gates pass (Step 10).**

## Next action

**Build Step 6 — decoupling-surface detection** (`boundary.py`, constructed mode): the explicit `decoupled`-edge marking the MWE needs, plus the `boundary_nodes` helper for Δ pairing. This makes the two-cluster MWE constructible end to end.

---

*End of Build Step 5 results. Reach strata computed from the reciprocal subgraph; decoupling does not merge components; numbering deterministic; update loop stratum-aware; no regression. Next: decoupling-surface detection.*
