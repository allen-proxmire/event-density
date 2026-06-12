# ShadowEmergence — Round 1 results

**The philosophically load-bearing test.** ThickRegime R1 found a clean diffusion PDE only at
ε=1 — where the certified Σ-selection is fully replaced by *injected* random scatter. But injected
noise is not the only road to a continuum. Deterministic molecular dynamics has no injected noise
either, yet it coarse-grains cleanly to the diffusion equation — through **mixing**: chaotic,
correlation-decaying determinism whose *effective* randomness emerges from the dynamics itself.
So the question ThickRegime left open, and the one that actually decides the philosophy:

> Does **pure ED (ε=0)** generate its *own* effective randomness — emergent mixing from many
> interacting commitments on rough, self-roughening landscapes — without any injected noise?

If yes, the smooth PDE layer is a **true shadow** of collective ED determinacy, and the bridge is
crossable from inside ED. If no, ED's determinism is **committal/trapping**, categorically not the
mixing kind, and confirmed-physics PDEs live in a *different* ED model, not the certified
Σ-substrate. **Script:** `shadow_emergence_test.py`. **Verdict: a clean no — ED does not mix.**

## Design

Pure certified Σ-selection (ε=0), no injected randomness, every primitive fixed (ρ monotone P11;
bandwidth conserved exactly as moved-only unit carriers; periodic steady arena; no drains/sources).
Landscapes roughen **only** from ED's own deposits. Ensemble of 300 runs across five independent
landscape families (smooth / random / gradient / ring / multi-basin), two densities (1 and 4
carriers/node). The vectorised Σ is validated bit-for-bit against the certified `compute_sigma`.

**The decisive instrument — scale-stability of D.** A diffusion equation has `γ(k) = D·k²`
*exactly*, so the coefficient `D = γ(k)/k²` must be **identical at every wavenumber**. We seed a
localized stripe (which excites many x-modes at once), watch each Fourier mode `b_n(t)` relax,
fit its rate `γ_n`, and form `D_n = γ_n/k_n²`. **Flat D_n across modes (low CV) ⇒ genuine PDE;
D_n drifting with scale ⇒ a kinetic pretender.** This is noise-robust (global projection, not the
shot-noise-limited local fit) and, ensemble-averaged over 300 landscapes, has ample signal.

We also track the mechanism the molecular-chaos route would require: **persistence p(t)** (does
ED's roughening decorrelate motion, p → 0.25?), and the **MSD exponent α** (does transport become
diffusive, α → 1?), plus its **density dependence** — the single sharpest discriminator, because
mixing systems decorrelate *faster* with density (more collisions) while trapping systems lock up.

## The instrument validates perfectly (ε=1 calibration)

| ε=1 (pure random scatter) | n=1 | n=2 | n=3 | n=4 |
|---|---|---|---|---|
| D_n = γ_n/k_n² | 0.250 | 0.251 | 0.251 | 0.251 |
| decay-R² | 1.00 | 1.00 | 1.00 | 1.00 |

CV(D_n) = **0.00**, α = **1.00**, persistence = **0.25** (memoryless). The recovered coefficient is
the analytic 2D nearest-neighbour random-walk value **D = 1/(2·dim) = 0.25**, identical across all
four modes. When a diffusion shadow exists, this test reports it with zero ambiguity. That is the
control that makes the pure-ED result below trustworthy: the failure is in ED, not the instrument.

## Pure ED (ε=0) does not cast a diffusion shadow

| signature | ε=0, frac=1 | ε=0, frac=4 (dense) | what diffusion needs |
|---|---|---|---|
| persistence p (early → late) | 0.40 → 0.47 | 0.49 → 0.49 | → 0.25 (decorrelates) |
| MSD exponent α | 0.93 | **0.57** | ≈ 1.0 |
| D_n across modes (n=1..4) | 1.91, 0.29, 0.12, 0.05 | 1.77, 0.47, 0.17, 0.08 | flat |
| **CV(D_n) — scale-stability** | **1.29** | **1.09** | **< ~0.15** |
| decay-R² (clean exponential?) | 0.75–0.39 | 0.75–0.64 | ≈ 1.0 |

Every diagnostic points the same way, and away from a PDE:

**1. No decorrelation.** Persistence stays at p ≈ 0.40–0.49 and *never* falls toward the
memoryless 0.25 — it even drifts slightly *up*. ED's own roughening does not randomize the motion;
carriers retain strong directional memory throughout. There is no molecular-chaos decorrelation.

**2. Sub-diffusive transport.** The MSD exponent is α ≈ 0.93 (sparse) and **0.57** (dense) — below
the diffusive α = 1, i.e. trapping, not spreading. The carriers funnel into coherence basins
(ρ ≈ ρ\*) and the monotone P11 footprint freezes them there, exactly as ThickRegime diagnosed.

**3. The coefficient is not scale-stable.** D_n falls by ~40× from the longest mode to the
shortest (CV ≈ 1.1–1.3, versus the calibration's 0.00). The relaxation rates `γ_n` are roughly
*flat* in k rather than `∝ k²` — the fingerprint of an overall cloud spreading, not of diffusion.
There is no single coefficient; there is no PDE.

**4. The density trend is the dagger.** Going from 1 to 4 carriers/node makes ED transport **more**
trapped (α 0.93 → 0.57), not less. This is the exact opposite of mixing: in any chaotic/collisional
system, higher density means more interactions, faster decorrelation, and *cleaner* diffusion. ED's
interactions are not collisions — they are competitions for commitment that **lock** the
configuration. More of them = more locking. This single contrast separates ED's determinism from
the mixing determinism of molecular dynamics more cleanly than any other measurement in the arc.

This also **refutes a hopeful hint** from ThickRegime R1: there, ε=0 at moderate density showed
α ≈ 0.93 and I flagged possible "density-induced effective scattering" — maybe enough density would
tip ED into mixing. The density sweep here falsifies that directly: denser pure ED is *more*
trapped (α → 0.57), not more diffusive. The hint was noise; the trend is trapping.

## Verdict

**Pure ED (ε=0) does not generate its own effective randomness.** Across 300 independent
landscapes, high density, and full self-roughening — with no injected noise — the certified
Σ-substrate stays persistent (p ≈ 0.45, never 0.25), sub-diffusive (α ≈ 0.57–0.93, *worsening*
with density), and scale-unstable (CV ≈ 1.1–1.3 versus a clean PDE's ≈0). The same instrument
returns a flawless diffusion signature at ε=1 (CV = 0.00, D = 0.25, R² = 1.00), so the negative is
ED's, not the method's.

So the molecular-chaos route is closed for this substrate. ED's determinism is **committal /
trapping**, not **mixing / chaotic** — the two kinds of determinism diverge exactly where it
matters: molecular dynamics decorrelates and casts the diffusion shadow; ED commits and freezes.
**The smooth PDE layer is therefore not a shadow the certified Σ-substrate casts from within.** It
belongs either to a *different* ED instantiation (the Q-C / UDM diffusion model, which is posited at
the continuum, not generated by Σ-dynamics) or to the externally-imposed randomness (ε=1) that
*erases* the substrate. Both bridge routes — inject noise (ThickRegime) and emerge noise
(ShadowEmergence) — now return the same structural verdict: **you reach the PDE only by leaving ED.**

Stated as the structural reason the brief asked for: **trapping, not mixing.** ED's selection rule
drives carriers to the coherence optimum and the monotone footprint pins them; interactions
increase the pinning rather than decorrelating it, so no amount of pure-ED collective dynamics
produces the local equilibrium a diffusion PDE requires.

## What this settles (and what it doesn't)

- **Settles:** the two-layer worry is now empirically grounded, not just argued. The certified
  Σ-substrate sits *below* the PDE layer and does **not** itself cast the diffusion shadow — neither
  by injected noise (ThickRegime) nor by emergent mixing (here). The determinism is the wrong *kind*.
- **Does not settle (honest limits):** (i) one substrate instantiation (the certified Σ-rule grid)
  at modest sizes/times; (ii) a *different* ED model (the Q-C/UDM PDE itself) is posited at the
  continuum and was not tested here — it may well be diffusive by construction; (iii) absolute D
  values are not the result, the *contrasts* are (CV ≈ 1.2 vs 0.00; α worsening vs improving with
  density; p stuck at 0.45 vs 0.25). The verdict is about the certified Σ-substrate, not all of ED.

## Crank-safety / honesty notes

- ε=0 throughout the test; the ε=1 column is labelled instrument calibration only.
- No primitive changed; ρ monotone (P11); bandwidth conserved exactly; no drains/sources; the only
  landscape roughening is ED's own deposits.
- The local Fickian fit is reported but explicitly flagged shot-noise-limited; the verdict rests on
  the scale-stability (CV) and density-trend diagnostics, which are validated by the ε=1 control.
- A clean negative for ED-as-PDE-generator; a clean, now-empirical confirmation of the
  trapping-not-mixing reading. Reported as the data fell, including the refuted ThickRegime hint.
