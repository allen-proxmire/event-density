# V5 characterization via the relational synchronization test — results

**Date:** 2026-07-06 (AP-directed, following the collective-pulse reframe)
**Status:** RUN, clean positive at the phase-model level. Characterizes V5's *relational role* — a finite-reach binder that creates local shared proper time (composite rest frames) without a universal tick — and derives a NEW constraint on V5's structure (its phase coupling must be attractive). Honest scope: a model of V5's known features, not the certified V5.

## The reframe that set the target (AP, 2026-07-06)

ED rejects a universal tick — that is *why* it has time dilation (each chain's proper time is its own commitment sequence; dilation is the *relative* rate between chains). So the earlier "no global collective pulse" negative was the physically REQUIRED answer, not a failure: global synchronization would BE a universal clock and would destroy time dilation. The right question is relational and distance-dependent:

**Does V5's finite cross-chain reach synchronize NEARBY (bound) chains into a shared rate — a local proper time / rest frame — while leaving DISTANT chains free (no universal tick, time dilation preserved)?**

V5's defining feature is finite reach (finite cross-chain memory ℓ_V5). Finite reach is exactly the ingredient that could give local-binding-without-a-universal-clock. This probe tests it.

## The test

Two spatially-separated clusters of 5 chains each (a NEAR cluster around x=0, a FAR cluster around x=50). Each chain is a commitment-phase oscillator with its own natural rate; the two clusters run at *different* mean rates (1.0 vs 1.4 — a stand-in for two frames in relative motion / different gravitational potential, i.e. a time-dilation setup). Coupling: finite-reach phase coupling, `dφ_i/dt = ω_i + K·Σ_j exp(−|x_i−x_j|/ℓ_V5)·sin(φ_j−φ_i)` — the minimal faithful skeleton of V5's known structure (finite reach + the gauge-covariant relative phase). Sweep the reach ℓ_V5; measure within-cluster sync (local binding), cross-cluster rate-gap (time-dilation proxy), and cross-cluster lock.

## Result — finiteness is load-bearing for relativity

| ℓ_V5 | within-sync | cross-cluster rate-gap | reading |
|---|---|---|---|
| (no coupling) | 0.33 | 0.41 | drift; natural rate gap |
| 2 – 15 (**< separation**) | **1.00** | **0.41 → 0.30 (preserved)** | **LOCAL proper time, time dilation intact, clusters NOT locked** |
| 50 – 200 (**≥ separation**) | 1.00 | **0.00 (collapsed)** | global lock = universal clock (time dilation destroyed) |

The decisive number is the cross-cluster **rate-gap** (the two bound composites' relative tick rate = the time-dilation observable):
- **While V5's reach is finite and smaller than the inter-cluster distance**, nearby chains fully synchronize into a shared rate (within-sync = 1.00 — a local proper time, the basis of a composite object with its own rest frame), the two clusters keep their *different* rates (gap preserved at 0.41 = time dilation intact), and they are not locked to each other. This is exactly the physically-required regime: **local binding, no universal tick.**
- **When the reach reaches or exceeds the inter-cluster distance**, the clusters lock globally and the rate-gap collapses to exactly zero — time dilation destroyed. This is the universal-clock regime, which would contradict relativity.

*(Note on the "between-sync" column in the raw output: with only two clusters its baseline for genuinely-unsynced clusters is ~0.64, not 0, so the ~0.62 values in the local regime correctly mean "not locked" — the rate-gap is the clean, unambiguous discriminator and it separates sharply at ℓ_V5 = separation.)*

## What this characterizes about V5 (two real results)

1. **V5's finite reach ⟺ local proper time without a universal tick ⟺ time dilation.** The finiteness of V5's cross-chain reach is not incidental — it is exactly what lets the substrate bind nearby chains into composites with a shared rest-frame clock while refusing to impose a universal clock. If V5's reach were infinite, ED would have a universal tick and no time dilation. So V5's defining feature is directly tied to relativity. This is a new, physically-motivated *role* for V5: **the finite-reach binder of local proper time.** It also ties V5 straight to the mass/composite work — a bound cluster sharing a proper time is precisely a composite object with its own rest frame.

2. **A new derived CONSTRAINT on V5's structure: its phase coupling must be attractive (synchronizing).** For V5 to bind chains into composites with a shared proper time at all, its phase coupling must pull phases together (the synchronizing sign). A repulsive coupling would give no local binding — no composites, no rest frames. This is a genuine forward constraint on V5's still-undetermined structure, obtained by working backward from the required physics — something the failed forward "what does V5 force" attempts (Tsirelson route) never produced. It sharpens the V5-characterization keystone: V5 must be (a) finite-reach (corpus already says this) and (b) attractive-phase-coupling (new, from this test).

## Honest scope (stated plainly, not buried)

- This is a **phase-oscillator model of V5's known structural features** (finite reach + gauge-covariant phase coupling, both real in Paper_090), NOT the certified V5 — which has never been implemented in code (that's the open keystone, target A2). It abstracts each chain to a commitment-phase oscillator, one level above raw commitment dynamics.
- The synchronizing **sign** of the coupling is *assumed* here (motivated by the gauge phase, not derived). But note: this test *reclassifies* that sign from "free assumption" to "required constraint" — V5 *must* be attractive to do its job, which is a result, not an input.
- V5 is **retarded**; this minimal model uses instantaneous coupling (retardation adds a delay, secondary to the reach question). Flagged.
- This is **reverse-characterization**: it establishes what V5 must look like (finite-reach + attractive phase coupling) to reproduce the required physics (local proper time + time dilation), rather than deriving from primitives that V5 does so. Complementary to the failed forward attempts, and arguably more useful — it gives V5 a concrete functional target and two structural constraints.

## Real-substrate confirmation (same session, 2026-07-06) — the forward step

The above is a phase-oscillator model. Built the genuine cross-chain V5 coupling into the **actual certified substrate simulator** (`v5_substrate_coupling_probe.py`) to check whether the same signature falls out of real substrate dynamics, not just the abstraction. Design: chains on parallel lanes (each a real certified 1D chain, real `compute_sigma`, real memory-driven advance rates — higher memory = slower rate, the route-2 mechanism); two clusters at different mean rates (time-dilation setup) with a **genuine within-cluster rate spread** (chains at genuinely different tempos, ~0.67 / 0.5 / 0.33, that would drift apart uncoupled); V5 as a real cross-chain term with finite transverse reach ℓ_V5 + finite longitudinal window + retarded (uses last step's positions), pulling each front toward the reach-weighted group mean.

**Result: the full signature reproduces from real substrate dynamics.** Uncoupled within-cluster rate spread = 0.084 (real), cross-cluster gap = 0.243 (time dilation).

| ℓ_V5 (transverse reach) | within-cluster spread | cross-cluster gap | reading |
|---|---|---|---|
| uncoupled | 0.084 | 0.243 | natural |
| 0.5 – 2 (**« separation 20**) | **0.0005 (−99%)** | **0.25 (preserved)** | **LOCAL lock + time dilation intact** |
| 5 | 0.0006 | 0.118 (half-collapsed) | transition |
| 10 – 100 (**≥ ~separation**) | 0.0006 | **0.002 (collapsed)** | universal tick (wrong) |

So with a genuine cross-chain V5 term in the real substrate: when the reach is finite and smaller than the inter-cluster distance, the genuinely-different-tempo chains within a cluster **lock to a shared rate** (within-spread collapses 99% — real local proper time, not an accident of identical inputs this time) **while the two clusters keep their different rates** (time dilation preserved). When the reach reaches the separation, everything locks and the rate-gap collapses to zero — universal clock, time dilation destroyed. **The phase-model characterization is confirmed by the real substrate dynamics.**

**What this forward step does and does NOT establish (honest):**
- DOES: shows V5's *known structure* (finite-reach, retarded, attractive cross-chain coupling), implemented as a real term in the certified substrate, produces the local-proper-time-without-universal-tick signature — the physically-required behavior — from genuine substrate dynamics, not a toy abstraction. Confirms finiteness is load-bearing for time dilation in the real sim.
- Does NOT: derive from the 13 primitives that the substrate *must* have this V5 term. The V5 coupling is an honestly-named structural addition (the certified base has no cross-chain coupling), faithful to V5's corpus-stated form but not forced by the primitives. The forward primitive derivation — why the substrate carries V5 at all — remains the hard open core of target A2. This narrows that target from "uncharacterized" to "here is exactly the coupling structure it must have (finite-reach + attractive + retarded) and exactly the physics it must produce (local proper time + time dilation); derive *that specific structure* from the primitives."
- The attractive sign and the position-as-phase-proxy are inputs here (consistent with the phase model's derived constraint that V5 must be attractive), not derived. Fronts restricted to forward advance. All flagged.

## Relationship to prior results

- Resolves the collective-pulse negative (`Collective_Pulse_Results.md`): global sync *should* fail (it would be a universal tick); the real behavior is local sync, which the crude shared-rho coupling couldn't produce but a finite-reach phase coupling does — now confirmed in the real substrate sim, not just the phase model.
- Advances target A2 (V5 characterization) from a different angle than the failed Tsirelson route: a relational/dynamical characterization tying V5 to time dilation and composite rest frames, with two concrete structural constraints (finite reach + attractive coupling).
- Ties the mass/memory thread to relativity: local proper time (a bound composite's shared rate) is the rest-frame clock of a massive composite object.

## Update 2026-07-08 — the attractive sign is now DERIVED (forced-conditional), no longer assumed

This doc treated V5's synchronizing/attractive sign as a NECESSITY condition (required to bind composites, but taken as an input; see "Honest scope": "the synchronizing sign is assumed here, motivated by the gauge phase, not derived"). That is now upgraded to derived. See `V5_ForwardDerivation_Scoping.md` (Build 1 + G1), enabled by P12-Coh being operationalized (`P12_Coherence_PhaseAlignment_Scoping.md` Step 4):

- **Build 1** (`v5_coherence_coupling_probe.py`): coupling two clusters of real certified chains by P12's coherence GRADIENT with P12's own `+` sign, with NO hand-put attractive term, reproduces this doc's exact signature (nearby chains lock to a shared rate, the cross-cluster gap is preserved, and the gap collapses to a universal tick only when the reach reaches the separation). A sign-flip control (`−Coh`) destroys binding at every reach, so the attraction is specifically P12's `+` coherence sign, not the coupling machinery.
- **G1**: Paper_090 §4.3's difference-phase gauge law `e^{i(α_A − α_B)}` forces V5's coupling to be the conjugated amplitude-pair moment `⟨P^A (P^B)^*⟩`, whose gauge-invariant real part is the coherence content `√(b_A b_B) cos Δπ`. So V5's coupling IS P12-Coh, forced-conditional on P-Bipartite-Mapping (bilinear content) plus the like-chain correlation reading.

Net: V5's attractive sign is derived from P12's reward-coherence structure (tier: MEASURED, with the identification gauge-law-forced). This doc's point-2 "assumed here" becomes "derived, forced-conditional." Existence (P10 posit) and ℓ_V5 (inherited) are unchanged.
