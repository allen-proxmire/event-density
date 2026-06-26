# The Three Walls Are One: ED Goes One Way, the Standard Continuum Goes Both Ways

**Foundations framing note (organizing, not new physics). Consolidates three separately-measured results into one structural fact, and names the single open bridge they share.**

> **MAJOR CORRECTION (same day, AP's reframe, `maxwell_coherent_decomp.py`).** The "wall" framing below is **likely wrong as stated** — at least for #2, and plausibly all three. AP's point: coarse-graining *is* losing the arrow, and the arrow should **relocate to entropy**, not block the field. Tested on #2: separating the coarse field into **coherent** (⟨e^{iφ}⟩) and **incoherent** parts, the **coherent part converges toward Coulomb** (deficit·r² → ~0.17, trending to the 0.126 Maxwell value, vs ~6.7 for the un-separated total) and the **incoherence is concentrated near the source and falls off far away = the entropy**. So **CGing ED gives Maxwell (coherent) + entropy (incoherent)** — the inverted stack working *correctly*, not a wall. The earlier #2 "no" was a **measurement error**: summing the field and the entropy and calling the sum non-Maxwell. The walls should be re-read with a **discriminator**: *is the "failure" a measurement error (a real signal masked by entropy → flips to a window), or a genuine feature (no signal there → stays a wall)?* The re-checks:

- **#2 (Maxwell): FLIPS to a window.** There IS a signal — the Coulomb field — under the entropy; the coherent/incoherent split reveals it (`maxwell_coherent_decomp.py`, confirmed at L=121). CG ED → Maxwell (coherent) + entropy (incoherent). The earlier "no" was a measurement error.
- **#5c (Gaussianity): does NOT flip — stays a real wall.** Tested at sparse seeding (`grf_gaussian_decomp.py`): removing the filament cells drives skew→0 but kurtosis→−1 — you never reach Gaussian; under the filaments is a **flat/sub-Gaussian background, not a Gaussian**. The field is *flat background + super-Gaussian filaments*, **neither Gaussian** — there is no Gaussian signal to recover. The GRF "no" is a real internal finding (the coarse field is non-Gaussian), **not promoted to an external/official prediction** (notebook documentation only, pending understanding).
- **#3 (diffusion): a third outcome — a clean continuum law, but the "wrong" object.** Re-checked (`diffusion_coherent_decomp.py`): the ensemble-mean density *does* obey a clean continuum law (step IC: regression R² 0.10 single → 0.60 mean — averaging out the ballistic-worldline disorder reveals a coherent law), **but it is eikonal/transport (|∇ρ|, R²=0.60), not diffusion (∇²ρ, R²=0.26).** ED coarse-grains to *ballistic transport*, not the diffusion PDE — diffusion was the wrong target (the "many CGs" point: Newton vs GR; ED gives the transport law). Confirms the CoarseGrain trilogy at the ensemble-mean level. See `CoarseGrain_Arc/Diffusion_CoherentMean_Finding.md`.

So the corrected framing is **not "three walls are windows"** but the sharper, more useful **three-outcome** result: **#2 Maxwell** = the coherent part *is* the textbook object (window); **#3 diffusion** = the coherent part is a clean continuum law but a *different* object (transport, not diffusion); **#5c Gaussianity** = *no* coherent object at all (genuinely non-Gaussian, a wall). The discriminator: **is there a coherent signal under the disorder, and is it the object you asked for?** That distinction is the result. The "ED goes one way" content below still holds as the *reason the entropy is there*; what's corrected is that the entropy doesn't always *block* a signal — sometimes (e.g. #2) the signal is intact underneath, sometimes (e.g. #5c) there is no signal. Read the rest of this note as the original (over-strong) framing, kept for the record.

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
