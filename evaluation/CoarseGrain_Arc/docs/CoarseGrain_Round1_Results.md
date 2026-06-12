# ED-CoarseGrain — Round 1 Results: what continuum law does the certified substrate generate?

**Question:** run the certified Σ-rule substrate, coarse-grain, and identify the continuum PDE it actually generates — no assumption of diffusion or the Q-C PDE.
**Code:** `CoarseGrain_Arc/coarsegrain_test.py` (certified `Bits/simulator`; 121×121 grid). **Date:** June 2026.
**Crank rail:** let the data pick the PDE class; report negatives honestly.

---

## 0. The structural fact that reshaped the experiment

A single active front in the certified substrate **does not branch** — verified directly: one seed → **one** active front after 15 steps, depositing ρ along a **1-D chain** (a worldline). So the certified Σ-rule is a **chain/worldline propagator, not a field-update rule.** That means a "ρ-field PDE" is the wrong object for a single chain, and the experiment must work at two levels: (A) the single-chain worldline law, and (B) the chain-ensemble density.

A second structural fact: **ρ only changes where a front commits.** ρ is monotone and grows by a fixed increment at each commit, so `∂_t ρ` is, literally, the *commit-deposition indicator* — ρ is a **deposited field slaved to where the fronts are**, not an independently-evolving field. This is the key to reading the results below.

## 1. Single chain — a drift-diffusion worldline (not a random walk, not a straight line)

Tracking one chain's trajectory on different ρ-landscapes (straightness = net displacement / path length):

| landscape | steps | straightness | character |
|---|---|---|---|
| **uniform** (flat ρ) | 60 | **0.13** | diffusive wander (`≈ 1/√60` = random-walk scaling) |
| **gradient** (ρ ∝ x) | 60 | **0.98** | **ballistic / eikonal** (directed worldline) |
| **gaussian** (symmetric well) | 60 | 0.05 | trapped wander |

The chain is a **drift-diffusion worldline**: on a ρ-gradient it moves **ballistically** (straightness → 1 — a directed, extremal/eikonal path, *not* diffusion); on a flat landscape it **wanders diffusively** (straightness ≈ `1/√T`, the random-walk signature). The drift comes from the Σ-landscape (the front seeks ρ≈ρ\* and avoids its own high-ρ committed trail via the strain term); the diffusion is the flat-landscape exploration. So the single-chain continuum is a **biased/drift-diffusion (Fokker-Planck-generating) trajectory**, landscape-dependent — emphatically *not* a simple heat-equation diffusion.

## 2. Chain ensemble — ρ-only PDEs fail, and diffusion fails decisively

Seeding a sparse ensemble of simultaneous chains and coarse-graining ρ(x,t) (30×30), then SINDy-regressing `∂_t ρ` on candidate term-libraries (R² in the active cells):

| IC | diffusion `∇²ρ` | eikonal `|∇ρ|` | diff+eik | PME/UDM |
|---|---|---|---|---|
| uniform | 0.004 | 0.001 | 0.005 | 0.009 |
| gaussian | 0.001 | 0.065 | 0.065 | 0.062 |
| step | 0.001 | 0.094 | 0.095 | 0.095 |
| ring | 0.001 | 0.057 | 0.059 | 0.045 |

Two clean reads:

- **Diffusion is decisively rejected** — `∇²ρ` carries essentially zero explanatory power (R² ≈ 0.001–0.004) across every initial condition. The certified substrate is **not** a heat-equation / naive-diffusion generator.
- **No clean *closed ρ-only* PDE fits** — the best model (a weak eikonal/transport term `+|∇ρ|`, front-growth-like) reaches only R² ≈ 0.06–0.10. A low-order local PDE *in ρ alone* does not capture the dynamics.

## 3. Why ρ-only fails — and what the native continuum actually is

This is not a noise artifact; it is structural, and §0 explains it. **ρ is a slaved, deposited field:** `∂_t ρ ∝ (local front density)`. The genuine dynamical variable is the **front-density φ** (the transported worldlines), not ρ. So the substrate's continuum is a **coupled transport–deposition (kinetic) system**, schematically:

> `∂_t ρ = (increment) · φ`  (deposition: ρ grows where fronts pass)
> `∂_t φ = transport[φ]`  (the drift-diffusion worldlines of §1)

ρ alone is **not a closed variable** — which is exactly why every closed ρ-only PDE regresses near zero. The dynamical content lives in the front-density/current, and ρ is its accumulated deposit. The weak `|∇ρ|` signal is the shadow of the front transporting through the ρ-gradient it has itself laid down.

## 4. Verdict — the substrate's native continuum is transport/worldline, not diffusion

**The certified ED substrate's native continuum limit is a kinetic transport law — drift-diffusion worldlines depositing ρ — not a closed scalar diffusion PDE.** Specifically:
- single chain → a **drift-diffusion / eikonal worldline** (ballistic in a ρ-gradient, diffusive on flat ground);
- ensemble → a **coupled transport–deposition system** in which **ρ is slaved to the transported front-density**; no closed ρ-only PDE describes it, and **diffusion is decisively excluded**.

**Consequence for the Q-C PDE.** The Q-C Boundary PDE (a *closed*, diffusion-like equation in ρ with the `D(x)` order parameter) is therefore **not the certified Σ-substrate's direct continuum limit** — the two are different ED models, as suspected. If the Q-C PDE relates to this substrate at all, it would be as a *further, over-damped / many-collision effective limit* of the transport system, not its leading continuum.

**Honest lean (worth flagging, not overclaiming).** The native object being **worldlines / transport** — directed extremal trajectories with a current — sits on the **geodesic/kinetic side**, not the scalar-diffusion side. That is consistent with the session's finding that *geometry* (geodesic motion, the emergent metric) was the natural emergence from this substrate, while *diffusion* (Q-C PDE, UDM) is a separate, coarser regime. The substrate generates trajectories first; fields are what their density makes.

## 5. Honest caveats

- The ensemble is **sparse and deterministic**; coarse-grained `∂_t ρ` is granular, so the *absolute* R² values are not the point — the **decisive contrast** (diffusion ≈ 0 vs the structural slaving of ρ) is.
- I regressed **ρ-only** libraries. The proper closure needs the **front-current `J`** as a variable (Round 2). The Round-1 claim is precisely: *ρ alone is not closed, and it is not diffusion* — not "no continuum exists."
- This is one substrate instantiation (the Σ-rule Bits sim) at one scale; a true continuum limit should be checked across block sizes and substrate sizes (Round 2).

## 6. Round-2 questions

1. **Close it with the current.** Track the front-current `J` (the commit-flow field) and test the transport/continuity closure `∂_t ρ = increment·φ`, `∂_t φ + ∇·(φ v) = ∇·(D∇φ)`. Does `(ρ, φ, J)` give a clean continuum law where ρ-alone failed?
2. **Drift vs diffusion tensor.** Measure the worldline drift `v(∇ρ)` and diffusion `D` from single-chain statistics — is the drift a clean function of the Σ-gradient (Hamilton-Jacobi)?
3. **Scaling / continuum existence.** Does the law stabilize across block sizes and S (a genuine continuum limit), or drift with scale?
4. **The Q-C PDE relationship.** Is the closed Q-C/UDM diffusion PDE recoverable as the over-damped limit of the transport system (high commit-rate, short mean free path)? That would *connect* the two ED models rather than leave them separate.
5. **Anisotropy.** The grid + tie-break may give faceted/anisotropic transport — measure and report (a real continuum-limit concern).

---

*Round-1 result: the certified substrate is a chain/worldline propagator whose native continuum is a kinetic transport–deposition law (drift-diffusion worldlines depositing a slaved ρ), NOT a closed scalar diffusion PDE — diffusion is decisively excluded. The Q-C PDE is a different ED model, at most an over-damped limit. ρ alone is not a closed continuum variable; the dynamical field is the front-current. No new rules; certified simulator only.*
