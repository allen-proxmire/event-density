# Milestone 1 — Results

**Program:** Determinability-boundary bits-measurement (empirical arc)
**Milestone:** 1 — Gate 4 (tie-break uniqueness) + orientation-blindness + irreversibility chokepoint
**Status:** **PASS** (exit code 0)
**Date run:** June 2026
**Author:** Allen Proxmire
**Code:** `Bits/simulator/{graph,state,sigma,update,__init__}.py`; `Bits/examples/milestone1_tiebreak.py`
**Related:** `Phase_CodingKickoff.md` (acceptance criteria §4); `Phase_Milestone1_Codegen.md` (the generated code)

---

## Verdict

**MILESTONE 1 PASSES.** All three acceptance checks from `Phase_CodingKickoff.md` §4 hold; the script exits 0. Gate 4 (tie-break uniqueness) is **green ahead of the update loop**, exactly as the build order intends.

## Recorded output

Verbatim from `python examples/milestone1_tiebreak.py`:

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

## Acceptance checks (Kickoff §4)

| Check | Criterion | Result |
|---|---|---|
| **A — tie-break uniqueness** | forced Σ-tie ⇒ exactly one winner; lexicographic (bw, node_id) | **PASS** |
| | Case A (distinct bw): winner by bandwidth | winner = **2** (bw 0.5, the max) ✓ |
| | Case B (equal bw): winner by node id (B1 final key) | winner = **3** (max node id) ✓ |
| | determinism: re-run ⇒ identical selection | identical (True, True) ✓ |
| **B — orientation-blindness** | flip all orientations ⇒ Σ unchanged | Σ identical before/after (unchanged: True) ✓ |
| **C — irreversibility chokepoint** | `commit(+)` raises ρ; `commit(−)` rejected; `commit` sole ρ-writer | 1.0→1.5 ✓; negative rejected ✓ |

## Notes

- **Forced tie is genuine, not assumed.** All three leaves carry identical ρ = 0.5, so Σ = −1.0 for every candidate (Σ tied = True printed for both cases). The tie-break therefore decides on a real tie, not a degenerate single-candidate set.
- **Both tie-break keys exercised.** Case A is decided by the *primary* key (bandwidth: 0.5 > 0.4 > 0.3 ⇒ node 2). Case B collapses the primary key (all bw = 0.5) and is decided by the *final* key (node id: 3 > 2 > 1 ⇒ node 3). This is exactly the B1-distinctness fallback from `Phase_TieBreak_Specification.md` §5, and it is confirmed to fire.
- **Orientation-blindness is behaviorally verified, not asserted.** Orientations were overwritten with arbitrary nonzero values (random on leaves, `[7, −3]` on the center); Σ did not move by even 1e-15. This is the live tripwire for the Phase D §5 invariant — had `compute_sigma` or `coherence` read orientation, Σ would have changed and the milestone would have failed.
- **Irreversibility is a single chokepoint.** `NodeState.commit` is the only method that writes ρ; it raises `ValueError` on a negative delta. The monotonicity gate (gate 1, Build Step 4) will rest on this single-writer guarantee.
- **Environment:** Python 3 with NumPy; no other dependencies. The package imports cleanly via `sys.path` insertion of `Bits/`.

## Scope boundary (what Milestone 1 does *not* yet establish)

Gates 1–3 are **not** addressed here and cannot be, by design — they require machinery not built at Milestone 1:

- **Gate 1 (monotonicity)** and **Gate 2 (acyclicity)** need the update loop (Build Step 4).
- **Gate 3 (factorization)** needs strata (Step 5), boundaries (Step 6), and the recorder (Step 7).

**No Δ will be measured until all four gates pass** (Build Step 10). Milestone 1 certifies the selection mechanics only — score, forced tie, deterministic resolution — which everything downstream is built on.

## Next action

Proceed to **Build Step 4 — the update loop** (`apply_update`, `step`): asynchronous, canonical `(stratum_id, node_id)` order, commits immediately visible. That unlocks gates 1 and 2 once a run completes.

---

*End of Milestone 1 results. Gate 4 green; selection mechanics certified faithful to the specification ahead of the update loop. The next deliverable is the update loop and gates 1–2.*
