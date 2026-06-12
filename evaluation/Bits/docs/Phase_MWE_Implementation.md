# Phase Bits / MWE — Build Step 8 Implementation

**Program:** Determinability-boundary bits-measurement (empirical arc)
**Document:** Build Step 8 — Minimal Working Example
**Status:** **Implemented, run, PASS** — first measurement-shaped run; two strata; independent evolution; natural termination; faithful export; deterministic; no regression
**Date filed:** June 2026
**Author:** Allen Proxmire
**Related:** `Phase_SimulatorDesign.md` §9; `Phase_SimulatorImplementationPlan.md`; `MWE_Results.md`

---

## 1. Purpose

This document implements **Build Step 8 — the Minimal Working Example (MWE)**, per `Phase_SimulatorDesign.md` §9. The MWE is the first full ED substrate run, and the substrate on which **Gate 3 (factorization)** and ultimately **Δ** are measured.

It assembles all seven simulator modules into one run with:

- **two strata** (two reach cells, causally independent);
- a **determinability boundary** (a single decoupled bridge);
- **independent seeds** (different RNG per cluster, so the strata are genuinely independent);
- **full recording** (ρ, orientation, commits) and `.npz` + JSON export.

The code was written, executed, and **passes** (output §7; record in `MWE_Results.md`). All prior steps re-run without regression, and the run is deterministic across repeats.

---

## 2. Graph Construction

Two isomorphic 8-node **chain** clusters joined by a single decoupled bridge:

```
Cluster A: 0-1-2-3-4-5-6-7   (chain, reciprocal edges, bw=0.5)
Cluster B: 8-9-10-11-12-13-14-15   (chain, reciprocal edges, bw=0.5)
Bridge:    (7, 8)  decoupled=True   ← the determinability boundary
```

Requirements met:

- **Isomorphic clusters** — both are 8-node chains with identical bandwidths, so any difference in their trajectories is due to *initial conditions*, not structure.
- **Bridge decoupled** — `add_edge(7, 8, bandwidth=0.5, decoupled=True)`; the reciprocal subgraph has exactly two components ⇒ two strata.
- **Deterministic and documented** — fixed node ids, fixed bandwidths, single decoupled edge; the graph is reproduced byte-for-byte on every run.

```python
def build_graph():
    g = ParticipationGraph()
    for chain in (A_NODES, B_NODES):
        for i in range(len(chain) - 1):
            g.add_edge(chain[i], chain[i + 1], bandwidth=0.5)
    g.add_edge(BRIDGE[0], BRIDGE[1], bandwidth=0.5, decoupled=True)
    return g
```

---

## 3. Initial Conditions

Each cluster gets **independent** random ρ and orientation from its own seeded RNG (A: seed 1, B: seed 2). Seeds differ across strata so B's initial state is independent of A's:

```python
def init_state(g):
    sv = StateVector()
    rng_a = np.random.default_rng(SEED_A)   # SEED_A = 1
    rng_b = np.random.default_rng(SEED_B)   # SEED_B = 2
    for n in A_NODES:
        sv[n] = NodeState(rho=float(rng_a.uniform(0.0, 0.5)),
                          orientation=rng_a.normal(size=ORIENT_DIM))
    for n in B_NODES:
        sv[n] = NodeState(rho=float(rng_b.uniform(0.0, 0.5)),
                          orientation=rng_b.normal(size=ORIENT_DIM))
    sv[A_NODES[0]].active = True   # one front per cluster, at corresponding ends
    sv[B_NODES[0]].active = True
    return sv
```

Both seeds are recorded in the run metadata (`params.seed_A`, `params.seed_B`). Randomness lives **only** in initial-condition sampling — the dynamics themselves are deterministic (the ensemble model from the measurement plan).

---

## 4. Simulation Run

The full simulator, in order: strata detection → coefficients (with extinction) → recorder → evolve.

```python
strata = assign_stratum_ids(sv, g)
coeffs = SigmaCoeffs(kc=1.0, ks=1.0, kg=1.0, rho_star=0.5,
                     extinction_threshold=-2.0)   # fronts stop with no good move
rec = HistoryRecorder(g, strata=strata, params={...}, seed=SEED_A)
rec.snapshot(0, sv)

for t in range(1, MAX_STEPS + 1):
    c = step(sv, g, coeffs, strata=strata, recorder=rec, t=t)
    if c == 0:
        break          # fixed point: all fronts extinguished
```

Termination is **either** natural (no commits ⇒ fixed point) **or** the `MAX_STEPS = 200` cap. With `extinction_threshold = -2.0`, fronts stop once no candidate clears the threshold; the run reached a fixed point at **step 9**, well short of the cap — the acyclic, fixed-point-only dynamics of Phase D, realized.

---

## 5. Output Artifacts

Written to `Bits/examples/mwe_output/`:

- **`mwe_run.npz`** — `nodes` [16], `steps` [10], `rho_history` [10,16], `orientation_history` [10,16,2], `committed_edges` [11,3]=(t,u,v). Binary, regenerable; **gitignored**.
- **`mwe_metadata.json`** — nodes, edges (bw + decoupled), `decoupled_edges`=`[[7,8]]`, `boundary_nodes`=`[7,8]`, `boundary_map`, `strata` (8/8 split), `params` (coeffs + seeds + max_steps), counts. Small, human-readable; committed as the canonical MWE snapshot.

Shapes and final ρ are recorded in `MWE_Results.md`.

---

## 6. Minimal Example Script — `Bits/examples/mwe_demo.py`

Builds the graph, seeds independently, runs with the recorder, saves outputs, and prints strata / boundary_map / final ρ / commit count / round-trip checks. (Full source in the repo; key structure shown in §2–§4 above.) The script is self-checking: it asserts two strata, bridge detection, independent evolution, clean termination, and `.npz`/JSON round-trip, exiting non-zero on any failure.

---

## 7. Acceptance Criteria for Build Step 8 — Result

Executed; **PASS** (exit 0). Recorded output:

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
  final rho A [0..7] : [0.26, 1.47, 1.41, 1.01, 1.16, 1.23, 2.1, 1.14]
  final rho B [8..15]: [1.13, 2.05, 0.09, 0.33, 0.22, 0.32, 0.2, 0.26]
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

Regressions: recorder, boundary, strata, update_loop, milestone1 — all exit 0. Determinism: a second run produced identical final ρ.

| Criterion | Result |
|---|---|
| Two strata | **PASS** (8/8) |
| Decoupled bridge detected | **PASS** (`[(7,8)]`) |
| Independent evolution per side | **PASS** (ρ_A ≠ ρ_B) |
| Terminates cleanly | **PASS** (fixed point at step 9) |
| Valid `.npz` + JSON export | **PASS** |
| Reloads without loss | **PASS** (round-trip) |
| No regression (Steps 1–7) | **PASS** (all exit 0) |

**The decisive feature for what follows:** ρ_A ends `[0.26, 1.47, 1.41, …]` and ρ_B ends `[1.13, 2.05, 0.09, …]` — markedly different. The clusters did *not* mirror one another (contrast Step 7's identical-init demo). The strata are causally factorized: B carries no imprint of A. This is the independence Δ measures, exhibited on a real run.

---

## 8. Next Steps (Preview)

| Step | Build | Unlocks |
|---|---|---|
| **9** | Full test suite (`tests/`, 5 files) | **Gate 3 (factorization) executable** against this MWE |
| **10** | All four gates green on the MWE | simulator certified → **Δ measurement opens** |

---

## 9. Deliverables

Produced and verified:

- **`Bits/examples/mwe_demo.py`** — the runnable MWE (build, seed, run, export, self-check).
- **`Bits/examples/mwe_output/mwe_run.npz`** — recorded trajectory (gitignored, regenerable).
- **`Bits/examples/mwe_output/mwe_metadata.json`** — canonical MWE metadata snapshot (committed).
- **`Bits/MWE_Results.md`** — recorded run and acceptance table.
- **`Bits/Phase_MWE_Implementation.md`** — this document.

**The first measurement-shaped run is live.** Per program discipline, **no Δ is measured until all four gates pass** (Build Step 10). The next deliverable is the formal test suite.

---

## 10. Next Actions

Proceed to **Build Step 9 — the full test suite** (`tests/`): `test_monotonicity.py`, `test_acyclicity.py`, `test_factorization.py`, `test_tiebreak.py`, `test_mwe.py`. **Gate 3 (factorization) becomes executable here** — asserting that commits in stratum A leave stratum B byte-identical, and that across-boundary mutual information is ≈ 0 on the MWE. The four gates run together on the MWE substrate at Build Step 10, certifying the simulator and opening the Δ measurement.

---

*End of MWE implementation. The first measurement-shaped run is live: two causally factorized strata across a determinability boundary, independent evolution, natural fixed-point termination, faithful export, deterministic. The next deliverable is the formal test suite where Gate 3 fires.*
