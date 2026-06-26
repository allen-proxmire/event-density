# The Three Walls Are One: ED Goes One Way, the Standard Continuum Goes Both Ways

**Foundations framing note (organizing, not new physics). Consolidates three separately-measured results into one structural fact, and names the single open bridge they share. Logged per the standing observation (across the CoarseGrain/PDE arc and this session) that ED's own coarse-graining does not reproduce the standard reversible continuum objects.**

---

## The three measured walls

Three independent questions, all of the form *"does ED's coarse-graining give the standard continuum object?"* — all answered **no**, all for the same reason:

1. **#3 Diffusion.** The certified ED substrate coarse-grains to a **kinetic lattice-gas (ballistic worldlines), not a diffusion PDE** (CoarseGrain trilogy). "You reach the PDE only by leaving ED."
2. **#5c Gaussianity.** ED's coarse field is **non-Gaussian** — strongly so, and coarse-graining makes the heavy tails *worse* (anti-CLT). The CLT route is blocked because the dynamics are committal/trapping ("locks configs, doesn't decorrelate").
3. **#2 Maxwell.** Ensemble-averaging the holonomies around a charge gives an isotropic but **non-Coulomb** field (trapped incoherence, deficit·r² grows). ED's coarse-graining does not select the Maxwell action.

## The one fact behind them

**ED goes one way; the standard continuum object goes both ways.**

- ED's rule is **commit-and-advance** (`Bits/simulator/update.py`): a front commits at a node (the irreversibility chokepoint) and *advances*. Net forward flow — the arrow, in the law. (Re-commitment of a node *can* happen, via passing fronts; what does **not** happen is free *relaxation* back toward neighbour-coherence. The precise blocker is **advance-vs-relax**, not commit-once.)
- The diffusion PDE, the Gaussian field, and the Maxwell/Coulomb field are all the **two-way** object: time-symmetric, reversible, the thermal/equilibrium limit. They are what you get by letting the system *relax to balance* — which has no arrow.
- **Standard coarse-graining secretly assumes the two-way symmetry** (ergodicity / a scramble-able time order / a Gibbs weight). That assumption is precisely the one thing the arrow forbids. So ED's *own* (one-way) coarse-graining cannot land on the two-way object — you only reach it by *removing the arrow*, which is "a level up," no longer ED.

This is the same content as `[[philosophy_pde_is_coarsegrain_artifact]]`: continuum equations carry *more* symmetry than the substrate (reversibility is the coarse-graining artifact); the arrow is **primitive** in ED and **emergent** in standard physics (the stack is inverted). Lossy ≠ wrong: ED is freed from owing the *equations* (reversible artifacts) — but it still owes the *observations*.

## The one open bridge (the real frontier)

The three walls share one unresolved question, and it is the honest open problem:

> **ED owes the observed world — and the observed world looks two-way (Coulomb fields, diffusion, Gaussian fluctuations). Does the one-way committal substrate, coarse-grained the way an observer actually measures, recover the two-way thermal limit?**

Nobody has crossed this bridge (for ED or, arguably, for the arrow-of-time problem generally). The walls say ED's *naive self-coarse-graining* does not give the continuum object; the open question is whether a *faithful observational* coarse-graining does. Until then, the honest statement is: **ED reproduces the topological / structural skeleton of these phenomena (winding=charge, the lattice-gauge form, the kinetic substrate) and locates the reversible continuum flesh one layer up, in a thermal limit its one-way dynamics do not themselves sample.**

## Status

An organizing consolidation: #2, #3, #5c are one wall — *ED goes one way, the standard continuum goes both ways, and standard coarse-graining assumes the both-ways symmetry the arrow forbids.* The shared open bridge (does observational coarse-graining recover the thermal limit?) is the real frontier. Not new physics; a framing that keeps three measured results from reading as three separate disappointments — they are three confirmations of one structural truth about the arrow.

---

*Three walls, one fact. #3 (ED→lattice-gas not diffusion-PDE), #5c (coarse field non-Gaussian, anti-CLT), #2 (coarse holonomies→non-Coulomb trapped field) all answer "does ED's coarse-graining give the standard continuum object?" with NO, for one reason: ED is one-way (commit-and-advance, the arrow), the continuum objects (diffusion/Gaussian/Maxwell) are two-way (reversible/thermal/equilibrium), and standard coarse-graining assumes the two-way symmetry the arrow forbids — so you reach them only by removing the arrow ("a level up", not ED). Precise blocker = advance-vs-relax (not commit-once; re-commitment is fine, free relaxation is what gives the continuum). Same content as philosophy_pde_is_coarsegrain_artifact (reversibility = CG artifact; arrow primitive not emergent; lossy≠wrong, owes observations not equations). Shared OPEN BRIDGE: does observational coarse-graining (not naive self-CG) recover the two-way thermal limit? — the real frontier, uncrossed. ED reproduces the skeleton, locates the reversible flesh a layer up. Organizing framing, not new physics.*
