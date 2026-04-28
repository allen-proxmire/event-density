# MCD.0 — Many-Chain Dynamics and the Path-of-Easiest-Updating: Scoping

**Date:** 2026-04-27
**Arc:** Many-Chain Dynamics (MCD) — first memo (scoping)
**Status:** New arc launched. Following the closure of the DM-arc and its three sub-arc refutations (DM.0, DM.1, DM.G), the MCD arc opens a structurally distinct question: what is ED's substrate-level analogue of the principle of least action, and how does it produce emergent collective dynamics for many interacting chains? The DM-arc treated ED as a continuum field theory (linear PDE with smeared source) and hit a structural wall (linearity-plus-disc-integration trap). MCD reframes the problem: chains are the primitive dynamical objects, paths are the trajectories of chains through ED gradients, the path-of-easiest-updating is the extremization principle that selects among possible paths, and many-chain dynamics is the collective behavior that emerges when multiple chains shape and are shaped by the substrate they occupy. **The principle of least disruption is already in the ED canon (ED-07 §5.1)**; the arc's contribution is to give it precise mathematical formulation, extend it from single-chain to many-chain regimes, and check whether the collective limit produces a structurally distinct emergent gravity (potentially nonlinear, potentially escaping the DM-arc linearity wall).
**Predecessor:** DM.G.4 (DM-arc closure with linearity-plus-disc-integration diagnosis); ED-07 (Event Density and Relativistic Phenomena); GR-3A (free-chain geodesic worldlines via eikonal limit, in the project memory).
**Empirical anchor:** Inertial motion, gravitational acceleration, and (eventually) galactic-scale dynamics. Same observational base as DM-arc but approached structurally rather than by source-function postulation.
**Successor:** MCD.1 (candidate action functionals from ED primitives).

---

## 1. The core question of the arc

### 1.1 What does "path of easiest updating" mean in ED?

ED-07 §5.1 articulates the principle: "A system tends to follow the path that minimizes disruption to its internal pattern of becoming." This is the ED analogue of the principle of least action, but with a different extremized quantity: not a Lagrangian built from kinetic and potential energy, but the *compatibility* of a system's internal ED with the surrounding ED field.

Three concrete criteria for a path to be inertial (ED-07 §5.1):

- The ED gradient along the path is minimal.
- The system's internal micro-event structure remains maximally coherent.
- Participation with the surrounding field is least strained.

These three criteria are stated qualitatively. **The arc's first task is to give them mathematical content.** What functional does an inertial path extremize? What does "compatibility" measure quantitatively? Is there a single ED-substrate scalar whose path-integral is extremized along inertial trajectories?

### 1.2 Is it an extremization principle?

The qualitative language of ED-07 §5.1 is consistent with extremization. "A system tends to follow the path that minimizes..." reads as δS = 0 for some action functional S[γ] over chain paths γ. But the principle could also be interpreted as:

- A *gradient descent* on some cost function (chains move to reduce strain monotonically).
- A *causal* rule (each chain step locally minimizes an instantaneous cost, not a global path integral).
- A *thermodynamic* principle (chains follow paths consistent with maximum entropy of the surrounding ED field).

These are not equivalent. An action principle is global (the entire path matters); a gradient descent is local (only the next step matters). They give different dynamics for non-trivial fields. **MCD.1 must distinguish among these readings.**

### 1.3 Does ED have a substrate-level action functional?

Open question. ED's primitives (event density, micro-events, participation, ED gradients) do not include a manifestly Lagrangian-style structure. But the existence of GR-3A (free-chain geodesic worldlines via eikonal limit, FORCED-conditional in the project memory) implies that *something* extremization-like is operating at the level of the eikonal approximation. The arc's task is to identify what it is and whether it extends beyond eikonal regime.

### 1.4 How do many chains interact?

The single-chain principle is stated for "a system" moving through a *given* ED field. But in the many-chain regime, the ED field at any point depends on the chains present at that point — chains both shape and are shaped by the substrate they occupy.

This produces a self-consistent dynamical system: each chain's path is determined by the ED field it experiences, and the ED field is determined by the chains that occupy it. **Many-chain dynamics is the closure of this loop.** What form does the closure take? Is it a mean-field continuum limit (recovering a PDE)? Is it a discrete many-body system? Is it something intermediate (BBGKY-like hierarchy)?

---

## 2. Substrate ingredients

The arc operates on ED's existing primitives. No new fundamental constants or fields are introduced; the goal is to extract dynamics from what's already there.

### 2.1 Event density ρ

The local rate of micro-event production. ED-07 §2.1: "Event Density is the local rate of becoming: the number of micro-events produced per unit of internal evolution." Smoothly varying field; non-negative; defines the "pace" of physical processes at each region.

### 2.2 Update rule (local becoming rate)

The substrate-level dynamics that extends a chain by one micro-event step. Not explicitly given as a single formula in ED-07, but governs how chains propagate from one event to the next. Should be local (depends on chain's current state plus immediate neighborhood) and consistent with the ED field's variation.

### 2.3 Gradients, compression, boundaries, horizons

ED gradients ∇ρ produce differential becoming across a system's extent (ED-07 §2.3). Compression (regions where ρ rises sharply) and rarefaction (regions where ρ falls) shape participation. Horizons (where participation across regions becomes impossible) act as causal boundaries. These structural features set the geometry that chain paths navigate.

### 2.4 Slow-time T and temporal tension

The slow-time field from BTFR.08: T as dimensionless fractional time-rate, with `dτ_local/dt_global = 1 − T`. Temporal tension is `T` and its gradients produce effective accelerations via the geodesic-like relation `a = c²·∇T` (in the slow-time interpretation). T is related to ρ but not identical: ED-07 distinguishes "becoming rate" (ρ) from "stretched participation across gradients" (T).

The relation between ρ and T is a structural question for MCD: are they the same field with different normalizations, or genuinely distinct? ED-07 §3 treats time dilation as a "difference in rate of becoming between regions" which sounds like ρ-mismatch; but §2.3's "ED gradients are the fundamental driver" suggests the *gradient*, not the absolute value, is what produces effective dynamics — i.e., T may be the integrated/normalized form of ρ-gradient effects.

**MCD must clarify the ρ-T relation.** If they are the same up to a reference value (T = const · log(ρ/ρ_ref) or similar), one set of substrate primitives suffices. If they are independent, MCD must say why.

### 2.5 Chain geometry

A *1-chain* is a single sequence of micro-events, the propagation track of an individual quantum (photon, electron, atom, etc.). *Many-chains* are collections of 1-chains coexisting in the same ED region. *Chain bundles* are coherent collections of chains moving together (e.g., a star, a galaxy, a planet — bound systems whose constituent chains maintain mutual coherence).

The arc's central new construct is the chain-bundle: it is many-chain (composed of many 1-chains) but coherent (the chains move together, maintaining a definite collective shape). Galactic dynamics is many-bundle dynamics.

---

## 3. Candidate meanings of "easiest updating"

Five structurally distinct readings:

### 3.1 Minimization of total update cost along a chain

> S[γ] = ∫_γ U(ρ, ∇ρ, ...) dτ,    inertial path = arg min S.

A path-integral of some scalar update-cost density `U` evaluated along the chain. This is the closest analogue to a classical action functional. The functional form of `U` is to be determined. Candidates:

- `U = ρ` (high-ρ regions are "expensive" to traverse; chains drift toward low-ρ).
- `U = 1/ρ` (low-ρ regions are "expensive"; chains drift toward high-ρ — matches the slow-time intuition where chains drift toward slower-time regions).
- `U = |∇ρ|²` (gradient regions are expensive; chains avoid steep gradients — matches ED-07 §5.1 "the ED gradient along the path is minimal").
- `U = (ρ − ρ_internal)²` (mismatch with the chain's internal ED is expensive; chains drift toward compatible regions).

### 3.2 Minimization of curvature or tension

> S[γ] = ∫_γ κ²(γ) dτ,    inertial path = arg min S.

Where κ is the path's curvature in some appropriate sense. In flat ED (uniform ρ), straight lines have κ=0 and are extremal. In non-uniform ED, paths curve to minimize a tension-like quantity. This is a more geometric reading, closer to GR's geodesic equation as κ = 0 in the metric of curved spacetime.

### 3.3 Maximization of entropy-like updating freedom

> S[γ] = ∫_γ H(ρ, ∇ρ, ...) dτ,    inertial path = arg max S.

Where H is an entropy-like functional measuring "how many ways the chain can update at each step." Paths are inertial when they preserve maximum updating-flexibility. This is a thermodynamic/information-theoretic reading.

### 3.4 Minimization of action built from ED primitives

A specific Lagrangian-like construction that combines ρ, T, and chain internal-state quantities into a single functional. For example:

> L = (1/2) · (dχ/dτ)² − V(ρ, T)

where χ is the chain's internal-state coordinate and V is an effective potential. This recovers classical mechanics in the appropriate limit and may extend to relativistic and quantum regimes.

### 3.5 Geodesic-like updating in slow-time geometry

> Inertial path = geodesic of the metric g(T, ∇T, ...).

A direct analogue of GR's geodesic principle, but with the metric derived from ED's slow-time field rather than postulated. This connects naturally to GR-3A's eikonal-limit result. The arc would derive the metric construction explicitly from ED primitives.

### 3.6 Discrimination criteria

These readings make different predictions:

- **Static vs dynamic:** §3.1 and §3.4 are global (whole-path); §3.2 is local (curvature); §3.3 is hybrid; §3.5 reduces to local in the geodesic equation.
- **Single chain vs many chain:** §3.1 and §3.2 generalize to many-chain by adding interaction terms; §3.3 and §3.4 require explicit coupling specifications; §3.5 generalizes through the field equations that determine the metric from many chains.
- **Limits:** §3.5 most directly recovers GR; §3.1 and §3.4 most directly recover classical mechanics; §3.2 is intermediate.

**MCD.1 must select among these (or identify a unifying reading) before MCD.2 can derive update equations.**

---

## 4. What a many-chain action principle must explain

If MCD succeeds, it should account for the following phenomenology that DM.G could not:

### 4.1 Why chains choose particular paths

The fundamental dynamical question. In QM, paths are summed over with phases; in CM, the path of stationary action is selected; in GR, geodesics are followed. ED's substrate-level account must say which paths chains "actually take" and how that selection depends on the surrounding ED field.

### 4.2 How chain bundles produce effective fields

A chain bundle (e.g., a planet, a star) is a coherent collection of many chains. To other chains passing through, the bundle appears as a source of ED gradient. The arc must explain how this "effective field" emerges from the constituent chains, and how it differs (if at all) from the field a smooth-density continuum source would produce.

This is the structural escape route from the DM-arc linearity wall: if many-chain bundles produce effective fields that are *not* simple superpositions of single-chain contributions (due to coherence, internal coupling, etc.), the resulting emergent gravity may be intrinsically nonlinear.

### 4.3 How nonlinearities emerge from many-chain coupling

The DM-arc treated the source as a continuum integrated over the disc — a linear superposition. If many-chain dynamics produces interactions that are not superposable (e.g., chain A's path depends on chain B's path which depends on chain A's...), the effective field equations will contain nonlinear terms that the continuum-source treatment missed.

The arc must determine *whether* such nonlinearities arise and *what form* they take in the appropriate continuum limit.

### 4.4 Whether this naturally produces MOND-like or GR-like limits

In appropriate regimes:

- **High-acceleration / dense bundles:** should reduce to Newtonian limit (the easy case).
- **Low-acceleration / extended sources:** could reduce to MOND-like deep-regime if the many-chain dynamics produces the right √M_b scaling automatically. Or could give something else.
- **Strong-field / relativistic:** should reduce to GR (GR-3A's geodesic limit) with appropriate metric construction.
- **Cosmological:** should connect to ED-08's anticipated cosmic-scale temporal-tension structure.

### 4.5 Whether this bypasses the DM-arc linearity wall

The diagnostic question. The DM.G.4 closure identified the obstacle: linear-PDE-plus-disc-integration locks BTFR slope at 2. A many-chain action principle bypasses this *if and only if* the effective field equation in the many-chain continuum limit is genuinely nonlinear.

**The arc's success criterion is not "MCD derives slope-4 BTFR" but "MCD's many-chain limit is nonlinear in a way that allows slope-4 BTFR to emerge."** The first criterion is too narrow (it could fail if the prefactor is wrong while the slope is right); the second is the structural test that matters.

---

## 5. Structural questions for the arc

The arc must answer, in roughly this order:

### 5.1 What is the substrate-level definition of "update cost"?

Per MCD.1: select among the §3 candidates based on consistency with ED's existing primitives, ED-07's qualitative criteria, and dimensional cleanliness (the cost density should be expressible in ρ, ∇ρ, T, ∇T, c, λ, κ_act without new fundamental constants).

### 5.2 What is the correct functional to extremize?

Per MCD.1, after selecting an update-cost density: write the functional `S[γ] = ∫_γ U dτ` (or its appropriate variational form) and verify it produces ED-07's qualitative criteria as Euler-Lagrange equations.

### 5.3 How do many chains couple?

Per MCD.3: examine whether chain-chain coupling is direct (one chain's path explicitly enters another's update cost), indirect (through shared modification of the substrate), or mean-field (each chain sees an effective averaged field generated by all others). The structural commitment will determine whether the continuum limit is linear or nonlinear.

### 5.4 Does the many-chain limit produce a nonlinear PDE?

Per MCD.3 + MCD.4: derive the continuum field equation. If linear, the arc is essentially the DM-arc with different vocabulary and the linearity wall reappears. If nonlinear, examine whether the nonlinearity is of the form needed to produce slope-4 BTFR (MOND-like deep-regime asymptotic) or some other form.

### 5.5 Does the resulting emergent gravity match observation?

Per MCD.4: confront the derived field equation with empirical galactic and cluster phenomenology. Compare to MOND's μ(|∇φ|/a₀) form for structural similarity. Check whether the cluster anchor (D_T, λ from merger-lag) is preserved.

### 5.6 If success, can the substrate derivation be tightened?

Per MCD.5: if MCD.4 produces a positive structural verdict, check whether the substrate-level definition of "update cost" is forced by ED's primitives or whether multiple substrate options would have produced the same emergent dynamics. This is an AD-style minimality check.

If failure, identify cleanly which structural commitment failed and whether it admits revision.

---

## 6. Roadmap for MCD.1–MCD.5

### 6.1 MCD.1 — Candidate action functionals from ED primitives

Survey the §3 candidate readings of "easiest updating." For each, write the action functional explicitly in terms of ED primitives. Apply three selection criteria:

- **Dimensional cleanliness.** Functional uses only existing ED primitives.
- **ED-07 §5.1 consistency.** Reduces to ED-07's three qualitative criteria as variational consequences.
- **Single-chain consistency.** Recovers GR-3A's eikonal-limit geodesic result for free chains.

Output: ranked list of candidate functionals; preferred candidate(s) for further analysis.

### 6.2 MCD.2 — Derive Euler-Lagrange-like update equations

For the preferred candidate(s), derive the equations of motion for a single chain. Check:

- **Newtonian limit:** chain path in uniform ρ should be straight; chain path in non-uniform ρ should curve toward higher-T regions consistent with ED-07 §5.3.
- **Geodesic limit:** in eikonal regime, recover GR-3A's geodesic equation with ED-derived metric.
- **Spaghettification consistency:** for an extended chain bundle in non-uniform T, the front and back of the bundle should experience differential acceleration in the direction predicted by ED-07 §5.3.

### 6.3 MCD.3 — Many-chain coupling and emergent nonlinearity

Extend the action functional from single chain to many chains. Determine the coupling structure and derive the continuum-limit field equation. Identify whether the continuum equation is linear or nonlinear, and characterize the form of any nonlinearity.

This is the **structural pivot point** of the arc. If linear, the DM-arc linearity wall reappears and MCD likely fails for the same C2 reasons. If nonlinear, the structural escape route is open and MCD.4 can proceed.

### 6.4 MCD.4 — Gravitational limit (compare to MOND/GR)

Take the continuum field equation from MCD.3 and examine its limits:

- **High-acceleration limit:** does it reduce to Newtonian gravity?
- **Low-acceleration / extended-source limit:** does it produce MOND-like deep-regime behavior, with a derived (not postulated) acceleration scale a₀ and interpolation function?
- **Strong-field / relativistic limit:** does it reduce to GR's Einstein equation, or to a structural extension of GR?

Compare structurally to MOND's μ(|∇φ|/a₀) form. Identify which features are common and which are MCD-distinctive.

### 6.5 MCD.5 — Decision memo

Based on MCD.1–MCD.4:

- **Adopt:** if the many-chain action principle produces a nonlinear emergent gravity that recovers Newtonian + GR limits and naturally yields MOND-like deep-regime behavior. The arc concludes with a structurally-distinct ED gravitational sector that bypasses the DM-arc linearity wall.
- **Revise:** if some structural commitment failed but a small modification might rescue it. Identify the modification and either continue the arc or fork to a sub-arc.
- **Reject:** if the many-chain limit is fundamentally linear (DM-arc wall reappears) or if the resulting nonlinearity has the wrong structural form. Close MCD with a clean refutation.

---

## 7. Scope discipline

### 7.1 What this arc is

A foundational structural arc — comparable in flavor to BTFR.01–09 or DM.G but addressing a deeper question. It works at ED's substrate level (chains, micro-events, ED field) rather than at the macroscopic-PDE level. The arc is **structural-derivation only**; no numerical implementation work is contemplated until-and-unless MCD.5 reaches "adopt."

### 7.2 What this arc is not

- Not a revival of the DM-arc. The DM-arc is closed; MCD is independent.
- Not an empirical-fitting exercise. MCD does not test against SPARC or other observations except as structural-consistency checks.
- Not a re-derivation of GR or MOND from scratch. MCD assumes those frameworks as comparison targets, not as inputs.
- Not a complete reformulation of ED. The arc preserves ED's existing primitives and forced theorems; it adds an action-principle layer that should be consistent with what's already established.

### 7.3 AD methodology considerations

The MCD arc's outputs would be a natural target for Architectural Distillation (AD) evaluation. The six AD criteria (minimality, locality, determinism, generative sufficiency, envelope tightness, structural optimality) provide a sharper assessment than free-form prose. If MCD.5 reaches "adopt," an AD evaluation should follow as a separate downstream task to verify the architecture's structural integrity.

The existing AD evaluation of Event Density (`ad_examples/AD_Evaluation_EventDensity.md`) should be consulted before MCD.1 begins, both to understand what's already been distilled about ED's architecture and to ensure MCD's new constructs are consistent with existing AD findings about ED.

### 7.4 Termination conditions

The arc terminates at MCD.5 with adopt, revise, or reject. Adoption may trigger a downstream implementation arc (MCD.6+) or feed into a renewed DM-arc revival with the new action-principle framework. Rejection closes the arc with a clean structural-derivation record.

---

## 8. Lessons from prior arcs that bear on MCD

Three methodological commitments inherited from BTFR.01–09 and DM.G:

### 8.1 Linearization-artifact testing

BTFR.08 discovered that the linearized treatment of T (with v_baryon as fixed input) hid structurally important effects. DM.G.1 hit the same issue by analyzing only outer-disc activity. **MCD must default to fully self-consistent treatment** of any field that interacts with the chains it's sourced by. Linearized analysis can be used as a sanity check but not as a primary tool.

### 8.2 Full-integration verification

DM.G.1b's "G4 survives" verdict was based on partial integration (outer disc only); the full calculation in DM.G.2 showed the inner disc dominates. **MCD must always carry calculations to completion** before drawing structural conclusions. Partial results are fine for intuition but cannot anchor verdicts.

### 8.3 Honest acknowledgment of conditional results

BTFR.08's Einstein-like relation `D_T = c²·κ_act` was a *conditional* structural result that BTFR.09 had to elevate to "foundational open question." **MCD should label conditional results explicitly** so future memos don't inherit them as established facts. An arc-internal-result is not a forced theorem until it has been audited at the foundational level.

---

## 9. Recommended Next Steps

Three concrete next steps:

1. **MCD.1: Candidate action functionals.** Survey the §3 candidate readings of "easiest updating." For each, write the action functional explicitly using only existing ED primitives. Apply the three selection criteria (dimensional cleanliness, ED-07 §5.1 consistency, single-chain GR-3A consistency). Output: ranked list, preferred candidate(s) for MCD.2 derivation. **This is the immediate next step.**

2. **Read the existing AD evaluation of Event Density** (`ad_examples/AD_Evaluation_EventDensity.md`) before MCD.1. This will surface what's already been structurally distilled about ED's architecture, what constraints are already known, and what slack the existing constraint census has revealed. New action-principle constructs in MCD must be consistent with the existing AD findings — checking this up front prevents wasted work in later MCD memos.

3. **Hold the empirical arcs (merger-lag retrodiction, weak-lensing tests) in parallel.** MCD is structural-derivation work; empirical tests proceed independently. The merger-lag retrodiction recommendation from DM.6 §6.1 remains active. MCD's outcome may eventually inform what to do empirically, but the empirical work does not wait on MCD.

The MCD arc opens a structurally distinct question from the DM-arc and offers a potential escape route from the DM-arc's linearity wall. Whether the escape route is real depends on whether the many-chain continuum limit produces genuine nonlinearity. **MCD.3 is the pivot point**; everything before (MCD.1, MCD.2) is preparation, and everything after (MCD.4, MCD.5) is consequence-checking. The arc's prospects rest on what happens at MCD.3.

Status: complete.
