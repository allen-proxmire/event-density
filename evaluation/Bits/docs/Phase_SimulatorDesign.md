# Phase Bits / Simulator Design — ED Substrate Simulator

**Program:** Determinability-boundary bits-measurement (empirical arc)
**Document:** Simulator architecture & design specification
**Status:** Pre-implementation; defines the build that §7 of the measurement plan calls for
**Date filed:** June 2026
**Author:** Allen Proxmire
**Related:** `../../Phase_Bits_DeterminabilityBoundaryMeasurementPlan.md` (the program); `../../Phase_B_ArchitecturalSpecification.md` (axioms/rule); `../../Phase_TieBreak_Specification.md` (tie-break); `../../Phase_E_ConstraintSurface.md` §6 (reach strata / determinability boundary); `../../Phase_OrientationPrimitivity_Resolution.md` (orientation = longitudinal-derivable + transverse-primitive)

---

## 1. Purpose

This document defines the **architecture of the ED-substrate simulator** for the empirical arc. The measurement plan's §7 step 1 requires a simulator; this is its engineering specification — data structures, update loop, Σ-maximization logic, tie-break integration, reach-stratum detection, decoupling-surface identification, and instrumentation hooks.

Two hard requirements govern every design choice:

1. **Fidelity to the architectural corpus.** The simulator must implement the ED substrate *exactly* as the twelve architectural documents specify it: the Σ = Coh − Str − Grad maximization rule, the deterministic tie-break, axioms B1–B7, and reach stratification. It is an executable transcription of a closed specification — not a new model, not an approximation, and explicitly **not a PDE or any averaging dynamics** (those produce the diffusive *shadow*, the wrong object — Phase D §3).

2. **Sufficiency for Δ.** The simulator's purpose is to generate the data from which

   > **Δ = predictability_within_stratum − predictability_across_boundary**

   can be computed (measurement plan §3). Every instrumentation choice exists to serve this difference: paired near-boundary / far-boundary / across-boundary region histories at matched graph separation.

The simulator produces **raw histories only**. All information-theoretic analysis (M1/M2/M3, Δ) is external (§8). This keeps the substrate-faithful core decoupled from the measure choice, so the measure can be fixed (plan §7 step 2) without touching the simulator.

---

## 2. Architectural Inputs

The simulator must implement, one-to-one, the following substrate components:

| Corpus element | Simulator obligation |
|---|---|
| **Participation graph (B2)** | A graph G = (V, E) with bandwidth-weighted channels (edge weights `bw`) |
| **Event states (B1)** | Atomic, distinct events; per-node commitment accumulation; distinct node identities (the tie-break's final key depends on this distinctness) |
| **Channels (5-channel table)** | Coherence, Strain, Gradient-strain as the three score-bearing inputs to Σ; Orientation and Decoupling as structural channels (non-score-bearing) |
| **Σ = Coh − Str − Grad** | A local, orientation-blind scalar computed per candidate transition |
| **Deterministic tie-break** | Lexicographic key κ = (bw, σ) over the Σ-maximal set (`Phase_TieBreak_Specification.md`) |
| **Irreversibility (B7)** | Commitment density ρ monotone non-decreasing; committed flags set-only, never cleared |
| **Reach boundaries (B6)** | Decoupling surfaces severing reciprocal participation; bound every node's candidate neighborhood |
| **Orientation (B5, primitive)** | Per-node orientation with a derivable longitudinal component and a **primitive transverse** component carried by chain-continuity |

**Prohibited.** No PDE discretization, no diffusion/Laplacian smoothing, no field averaging, no gradient-flow energy descent. The update is **discrete local selection (argmax)**, not continuous relaxation. Any averaging step would simulate the shadow, not the substrate, and invalidate the measurement. This prohibition is a correctness gate, not a stylistic preference.

---

## 3. Data Structures

**Graph representation.** Adjacency-list for sparse participation graphs (the expected regime), with an optional CSR/matrix backend for dense small graphs. Node IDs are integers `0..|V|-1` — these *are* the B1 distinct identities and supply the tie-break's canonical final key `σ` (§4).

```
Node v:
  rho        : float    # commitment density (B4); monotone non-decreasing (B7)
  orientation: float[k] # B5; component 0 = longitudinal (derivable), 1..k-1 = transverse (primitive)
  committed  : bool     # whether any chain has committed at v
  stratum_id : int      # reach-stratum label (§5)
  active     : bool     # whether a chain front currently sits at v

Edge e = (u, v):
  bw         : float    # channel bandwidth (B2); also primary tie-break key
  decoupled  : bool     # True ⇒ this edge is a decoupling surface (B6); reciprocal participation severed
  committed  : bool     # whether a chain has propagated along e
```

**Local neighborhood cache.** For each active node `u`, cache its admissible candidate set 𝒩(u) = { v : (u,v) ∈ E, ¬decoupled(u,v) } so Σ is computed only over the bounded, reach-respecting neighborhood. Invalidate the cache for `u` only when an incident edge's `decoupled` flag changes (never, for constructed-surface runs — §6).

**Stratum labels.** `stratum_id` per node, computed by §5. For constructed (fixed) surfaces these are static after init.

**Boundary markers.** The `decoupled` edge flag is the single source of truth for decoupling surfaces. A derived `boundary_node` set (nodes incident to ≥1 decoupled edge) is cached for the instrumentation pairing (§7).

**History recording.** Per-step append-only arrays sized `[T, |V|]` (ρ), `[T, |V|, k]` (orientation), plus committed-edge event log. Pre-allocate when `T` is known; arrays are write-once per step (consistent with irreversibility — history is itself append-only). See §7.

---

## 4. Update Rule Implementation

**Per-candidate score.** For an active chain at node `u` with current chain state `s`, and a candidate next-event `e′` at node `v` along admissible edge `e = (u,v)`:

```
Σ(e′) = Coh(e′, s) − Str(e′, ρ_local) − Grad(e′, ∇ρ)
```

Reference instantiation (local, orientation-blind — coefficients are parameters, qualitative channel roles are fixed):

```
Coh(e′, s)   = κ_c · coherence(s, v)         # stabilizing (+); rewards consistent continuation; NOT a function of orientation
Str(e′, ρ)   = κ_s · ρ(v)                      # destabilizing (−); penalizes committing into dense regions
Grad(e′, ∇ρ) = κ_g · | ρ(v) − ρ(u) |           # destabilizing (−); penalizes fighting the local density gradient
```

`coherence(s, v)` is a local consistency functional on the commitment field (e.g. closeness of ρ(v) to the chain's running trajectory) — a modeling choice to be fixed at implementation, **constrained** to be: (a) computable from `u`'s bounded neighborhood, (b) **independent of orientation** (Σ is orientation-blind, Phase D §5 — this is a hard invariant the implementation must not violate). The coefficients (κ_c, κ_s, κ_g) are run parameters.

**Per-step update (one active chain):**

1. **Enumerate** 𝒮_cand = 𝒩(u) (cached; reach-bounded, decoupling-respecting).
2. **Score** Σ(e′) for each candidate.
3. **Σ-maximal set** 𝒮 = argmax_{e′} Σ(e′).
4. **Tie-break** (always, even when |𝒮| = 1): select the unique `e′* ∈ 𝒮` with lexicographically maximal κ(e′) = ( bw(u,v), σ(v) ), where `σ(v) = v` (the B1 node id). Lexicographic, descending. Totality is guaranteed because node ids are distinct and 𝒮 is finite (`Phase_TieBreak_Specification.md` §5).
5. **Commit** `e′*` at node `v`:
   - `ρ(v) += 1` (or the configured commitment increment) — **monotone, irreversible**;
   - `committed(v) = True`, `committed(u,v) = True`;
   - advance the chain front: `active(u) = False`, `active(v) = True`;
   - **orientation transport:** set `orientation[v][0]` (longitudinal) = direction of the committed step `u→v`; copy `orientation[v][1:]` (transverse) from `u` (chain-continuity carries the primitive component, Phase E §7 / orientation-primitivity resolution).
6. **Enforce irreversibility:** ρ is increment-only; `committed` and history are set-only. No code path decrements ρ or clears a committed flag. (Asserted in the test suite, §10.)

**Synchronous vs. asynchronous.** Use **asynchronous updates in canonical node-id order** as the default:

- Within a step, process active chains in ascending `stratum_id`, then ascending node id; each commit is visible to chains processed later in the same step.
- This makes the entire evolution **deterministic given (graph, initial condition, parameters)** — no randomness in the dynamics (randomness enters only via initial-condition sampling across an ensemble, §9 / plan §7). Per-trajectory determinism is required for clean Δ attribution (Phase D: trajectories are deterministic within a stratum, so across-boundary uncertainty is attributable to the boundary, not to dynamical noise).
- **Cross-stratum independence is preserved regardless of order:** chains in different strata share no admissible edges (decoupled), so update order never couples strata (factorization holds by construction). The canonical order is purely a within-stratum determinizer.
- A fully **synchronous** mode (all chains score against the start-of-step snapshot, then commit together, with the lexicographic key resolving any two-chains-want-one-node conflict) is provided as an alternative for robustness checks; results must agree with async on factorization and monotonicity.

---

## 5. Reach-Stratum Detection

A **reach stratum** is a maximal set of nodes mutually reachable without crossing a decoupling surface — i.e. a connected component of the **reciprocal-participation subgraph** G_recip = (V, { e ∈ E : ¬decoupled(e) }).

**Algorithm:**

```
function assign_strata(G):
    for each unvisited node v in V:                 # BFS/DFS flood
        sid = next_stratum_id()
        queue = [v]
        while queue:
            u = queue.pop()
            stratum_id[u] = sid
            for (u,w) in incident_edges(u):
                if not decoupled(u,w) and w unvisited:
                    queue.push(w)
```

One-sided influence (an edge that transmits outward but not reciprocally) does **not** merge strata: only `¬decoupled` (reciprocal) edges are traversed. This matches the corpus exactly — strata are causally independent under *reciprocal* participation; one-sided outflow may cross a surface but does not restore comparability (Phase E §6).

**When recomputed.**

- **Constructed-surface runs (primary):** decoupling edges are fixed at init, so strata are computed **once at initialization** and are static. This is the primary measurement regime (plan R1 mitigation: clean, crisp boundaries).
- **Emergent-surface runs (robustness, optional):** if `decoupled` flags can change during evolution (§6 emergent mode), strata are **recomputed when any edge's `decoupled` flag flips**, incrementally where possible. Used only in the graded-decoupling robustness study, not the primary measurement.

---

## 6. Decoupling-Surface Identification

Two modes, sharing the same `decoupled` edge flag as output:

**Constructed (primary).** Decoupling surfaces are specified at init by explicitly setting `decoupled(e) = True` on chosen edges (a hard severing of reciprocal participation). This gives a crisp, unambiguous boundary by construction — the design's primary regime, and the basis for the MWE (§9). The surface is a known input, not an inference.

**Emergent (robustness, optional).** Decoupling is *detected* during evolution where reciprocal participation effectively fails. Candidate criteria (one to be fixed for the study, not mixed):
- *bandwidth threshold:* `bw_eff(e) < τ_reach` (channel too weak to transmit reciprocally), or
- *gradient threshold:* `|ρ(v) − ρ(u)|` exceeds a severing threshold (a commitment cliff one-sides participation).
Scanned per step; flipping a flag triggers stratum recomputation (§5). Reported separately and flagged as inference-dependent (plan R1: graded boundaries are a later robustness study, never the primary number).

**Use in Δ.** The decoupling surface defines the measurement pairings consumed by the analysis (§7, §8):
- **Across-boundary pair:** region states straddling a decoupled edge — side-1 boundary nodes vs. side-2 boundary nodes (different strata). The factorization predicts low shared information; Δ's second term measures it.
- **Baseline (within-stratum) pair:** boundary-region nodes vs. nodes at **matched graph distance within the same stratum** (reciprocal reach intact). Δ's first term.
Matching graph distance between the two pairs is what makes Δ difference out estimator/representation artifacts (plan §3, R2).

---

## 7. Instrumentation Hooks

The simulator records, per step `t`:

- **State snapshots:** `rho_history[t, :]` (shape `[T, |V|]`), `orientation_history[t, :, :]` (shape `[T, |V|, k]`), and the **committed-event log** (list of `(t, u, v)` for each commit).
- **Per-stratum histories:** views of the above grouped by `stratum_id` (no copy; index sets cached at init for static strata).
- **Cross-boundary state pairs:** for each decoupling surface, the time series of (side-1 boundary region, side-2 boundary region) state vectors — the **across-boundary samples** for Δ.
- **Baseline pairs:** for each boundary region, the time series of (near-boundary region, matched-distance far region within stratum) — the **within-stratum samples** for Δ.
- **Channel states & orientation:** per-edge `bw`, `committed`; per-node orientation (both components) — recorded so the analysis can include or exclude orientation and can separate the longitudinal (derivable) from transverse (primitive) content.

**Region definition.** A "region" is a fixed node set (e.g. a k-hop ball around a chosen anchor node), defined at init and held constant across the run so that pairs are comparable over time.

**Export format.**
- **Arrays → NumPy `.npz`:** `rho_history`, `orientation_history`, `committed_edges`, plus the cached region index sets.
- **Metadata → JSON sidecar:** graph topology (edge list + `bw`), `decoupled` edge set, `stratum_id` map, region definitions, the (baseline-pair, across-pair) matching with graph distances, run parameters (κ_c, κ_s, κ_g, commitment increment, update mode), and the **initial-condition seed** (for ensemble reproducibility). One `.npz` + one `.json` per run; ensembles are directories of these.

The simulator writes raw histories and the pairing metadata; it computes **no** entropy, MI, or Δ itself.

---

## 8. Integration with Analysis Stack

The handoff is one-directional: **simulator → (`.npz` + `.json`) → analysis module → Δ.** The simulator never imports the analysis code; the analysis never re-runs the simulator.

- **ed-lab entropy functions.** `ed-lab/.../invariants/spectral.py` provides a Shannon-entropy core `H = −Σ pₖ ln pₖ`. *Caveat:* ed-lab's entropy is **spectral (FFT/DCT on Cartesian grids)** and is **not** directly applicable to arbitrary participation graphs. What transfers is the **Shannon-entropy kernel and the ε-regularization idiom**, applied to region-state *distributions* we construct from the recorded histories — not the spectral transform. Use ed-lab's kernel where the region state is binnable; use a general estimator (next bullet) otherwise.
- **ed-lab correlation-length estimators.** `ed-lab/.../invariants/correlation.py` computes matched-separation autocorrelation/structure functions. The **matched-separation discipline** is directly reusable as the template for pairing baseline vs. across-boundary at equal graph distance (§6). The estimator math is grid-specific; the *separation-matching pattern* is what we borrow.
- **Δ computation (M1/M2/M3).** New code, operating on the recorded region-state samples:
  - **M1 (mutual information)** and **M2 (conditional entropy):** a finite-sample-bias-corrected estimator (KSG or binned-with-correction) over (near-region history, far/across-region state) — graph-general, not grid-based.
  - **M3 (within-stratum-restricted predictive gap):** fit a predictor (scikit-learn) on within-stratum information, score it on across-boundary vs. baseline targets; the accuracy gap is the operational measure, mapped to bits by the fixed calibration (plan §5, §7 step 2).
  - **Δ** assembled as the baseline-minus-across difference, per matched pair, aggregated across the ensemble.

The analysis layer is the subject of a later document; this section fixes only the interface contract (what the simulator must emit so the analysis can run).

---

## 9. Minimal Working Example (MWE)

The smallest configuration that (a) contains at least one decoupling surface and (b) permits Δ to be computed.

**Graph.** Two clusters joined by a single decoupled bridge:

```
Cluster A: path/clique of 8 nodes  [a0 a1 a2 a3 a4 a5 a6 a7]
Cluster B: path/clique of 8 nodes  [b0 b1 b2 b3 b4 b5 b6 b7]
Bridge edge: (a7, b0) with decoupled = True   ← the decoupling surface
All intra-cluster edges: decoupled = False, bw assigned (varied, to exercise the tie-break)
```

This yields exactly **two reach strata** (A and B) under §5, separated by the constructed surface.

**Initial condition.** Seed **independent** active chains in *both* clusters — e.g. `active(a0) = True`, `active(b0) = True` — with **independently sampled** initial ρ / orientation in A and B. Independence is essential: it gives B genuine dynamics to (fail to) predict from A.

**Regions & pairs.**
- *Across-boundary pair:* region near `a7` (boundary, side A) vs. region near `b0` (boundary, side B) — straddles the decoupled bridge.
- *Baseline pair:* region near `a7` vs. region near `a3` (matched graph distance within A, reach intact).

**Expected result (a sanity prediction, not an assumption).** Across-boundary predictability ≈ 0 — A's history carries no information about B's state, because the strata are causally independent (factorization). Baseline predictability high — within A, near and matched-far regions are reach-connected. Hence **Δ large and positive.** If the MWE does *not* show this, the simulator has a factorization bug, not a measurement subtlety — making the MWE simultaneously the first measurement and a correctness test (§10).

**Scale.** 16 nodes, `T` on the order of a few hundred steps to reach the fixed point in both strata. Trivially fast; suitable for tight iteration and for the test suite.

---

## 10. Next Actions

The next step after this document is **implementation of the simulator** to this specification.

The **first deliverable is a correctness test suite** — the simulator must pass these before any Δ is measured (they are the correctness gates from measurement plan §7 step 1):

1. **I4 monotonicity** — assert `ρ(v, t₂) ≥ ρ(v, t₁)` for all `v`, all `t₂ > t₁`, across every run. A single decrement is a hard failure.
2. **Acyclicity** — assert no chain revisits a state configuration; equivalently, every commit strictly increases total committed ρ, and no node configuration recurs along a chain. (Follows from monotonicity + irreversibility; tested directly as a guard against implementation error.)
3. **Factorization at decoupling surfaces** — assert that committing anywhere in stratum A leaves all of stratum B's states unchanged (and vice versa), and that measured across-boundary MI is ≈ 0 in the independent-init MWE. This is the empirical check that decoupling truly severs reciprocal participation.
4. **Tie-break uniqueness** — construct a forced Σ-tie (equal-Σ candidates by design) and assert the lexicographic key (bw, σ) selects **exactly one** candidate, deterministically, on every such occurrence; assert reproducibility across repeated runs with the same seed.

Determinism is itself under test: the same (graph, initial condition, parameters) must produce a bit-identical history on every run. Only after all four gates pass does the program proceed to fixing the primary measure (plan §7 step 2) and running ensembles.

---

*End of Simulator Design. This document specifies the build; it does not implement it. The simulator is a faithful executable transcription of the closed ED-substrate specification — discrete Σ-maximization, never averaging — instrumented to emit the paired histories Δ requires. Implementation and the correctness test suite are the next deliverable.*
