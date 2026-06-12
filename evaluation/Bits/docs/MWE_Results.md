# MWE — Results (Build Step 8)

**Program:** Determinability-boundary bits-measurement (empirical arc)
**Build step:** 8 — Minimal Working Example (16-node, two clusters)
**Status:** **PASS** (exit 0); Steps 4–7 and Milestone 1 regressions **PASS**; deterministic
**Date run:** June 2026
**Author:** Allen Proxmire
**Code:** `Bits/examples/mwe_demo.py`; outputs `Bits/examples/mwe_output/mwe_run.npz`, `mwe_metadata.json`
**Related:** `Phase_MWE_Implementation.md`; `Phase_SimulatorDesign.md` §9

---

## Verdict

**Build Step 8 PASSES.** The MWE constructs the 16-node two-cluster graph with a decoupled bridge, assigns independent random initial conditions per stratum, runs the full simulator with recording, terminates naturally at a fixed point, and exports valid `.npz` + JSON that reload faithfully. The two clusters evolve independently. No regression in Steps 4–7 or Milestone 1; the run is deterministic across repeats.

## Recorded output

```
================================================================
BUILD STEP 8 - Minimal Working Example (16-node, two clusters)
================================================================

  strata (A->0, B->1)      : two strata, |A|=8, |B|=8
  decoupled bridge          : [(7, 8)]
  boundary_map              : {7: [8], 8: [7]}
  steps run                 : 9  (max 200)
  total commits             : 11
  terminated naturally      : True
  final rho A [0, 1, 2, 3, 4, 5, 6, 7]: [0.26, 1.47, 1.41, 1.01, 1.16, 1.23, 2.1, 1.14]
  final rho B [8, 9, 10, 11, 12, 13, 14, 15]: [1.13, 2.05, 0.09, 0.33, 0.22, 0.32, 0.2, 0.26]
  exported                  : mwe_run.npz, mwe_metadata.json

Checks
  two strata                : True
  decoupled bridge detected : True
  independent evolution     : True
  terminated cleanly        : True
  npz round-trip            : True
  json metadata valid       : True

================================================================
BUILD STEP 8: PASS
================================================================
```

Regressions: recorder, boundary, strata, update_loop, milestone1 — all exit 0.
Determinism: a second run produced **identical** final ρ for both clusters.

## Acceptance (Step 8 criteria)

| Criterion | Result |
|---|---|
| Produces two strata | **PASS** (\|A\|=8, \|B\|=8) |
| Detects the decoupled bridge | **PASS** (`[(7,8)]`) |
| Evolves independently on each side | **PASS** (ρ_A ≠ ρ_B) |
| Terminates cleanly | **PASS** (fixed point at step 9 < 200) |
| Exports valid `.npz` + JSON | **PASS** |
| Reloads without loss | **PASS** (npz + json round-trip) |
| No regression (Steps 1–7) | **PASS** (all exit 0) |

## What the run establishes

- **Two strata, one boundary.** The decoupled bridge `(7,8)` partitions the 16 nodes into two reach strata of 8 each; `boundary_map = {7:[8], 8:[7]}` names the across-boundary pairing — node 7 (stratum 0) and node 8 (stratum 1), the Δ across-boundary anchor.
- **Natural termination.** With `extinction_threshold = -2.0`, every front stopped once it had no sufficiently-good continuation; the run reached a **fixed point at step 9**, well short of the 200-step cap. This is the acyclic, fixed-point-only dynamics of Phase D, realized: 11 commits, then quiescence.
- **Genuine independence.** The two clusters were seeded with *different* RNG seeds (A=1, B=2), so their initial ρ/orientation differ — and their final states differ markedly: ρ_A ends `[0.26, 1.47, 1.41, …]`, ρ_B ends `[1.13, 2.05, 0.09, …]`. The clusters did **not** mirror each other (contrast the Step 7 demo, where identical zero inits gave identical fills). This is the independence the Δ measurement requires: B's trajectory carries no imprint of A's, because the strata are causally factorized.
- **Determinism.** The evolution is a deterministic function of (graph, seeded init, coeffs); a second run reproduced final ρ exactly. Randomness lives only in the *initial-condition* sampling (the seeds), never in the dynamics — exactly the ensemble model the measurement plan specifies.

## Output artifacts

Written to `Bits/examples/mwe_output/`:

- **`mwe_run.npz`** — `nodes` [16], `steps` [10], `rho_history` [10, 16], `orientation_history` [10, 16, 2], `committed_edges` [11, 3]=(t,u,v). (Gitignored; regenerable by running `mwe_demo.py`.)
- **`mwe_metadata.json`** — nodes, edges (bw + decoupled), decoupled_edges `[[7,8]]`, boundary_nodes `[7,8]`, boundary_map, strata (16 entries split 8/8), params (coeffs + seeds + max_steps), counts. Committed as the canonical MWE metadata snapshot.

## Significance

This is the **first measurement-shaped run**: a complete ED substrate trajectory with two causally independent strata separated by a determinability boundary, fully recorded and exported in the schema the Δ analysis consumes. Everything Gate 3 needs is now in one artifact — distinct strata, an explicit boundary, independent histories, and a faithful export. The next step turns the visible independence into a formal assertion.

## Scope boundary

The MWE *exhibits* independence (ρ_A ≠ ρ_B; distinct trajectories) but does not yet *formally test* factorization — that is Gate 3, in the Build Step 9 test suite, which asserts (a) commits in A leave B byte-identical and (b) across-boundary MI ≈ 0. **No Δ until all four gates pass (Step 10).**

## Next action

**Build Step 9 — the full test suite** (`tests/`): five pytest files — `test_monotonicity`, `test_acyclicity`, `test_factorization`, `test_tiebreak`, `test_mwe`. **Gate 3 (factorization) becomes executable here**, run against this MWE substrate.

---

*End of MWE results. The first measurement-shaped run is live: two strata, a determinability boundary, independent evolution, natural fixed-point termination, faithful export, deterministic. Next: the formal test suite where Gate 3 fires.*
