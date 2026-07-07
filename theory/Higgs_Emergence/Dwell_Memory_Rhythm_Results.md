# Memory rhythm probe ("waves have memory") — results

**Date:** 2026-07-06 (AP route #2, and the "to persist is to pulse" framing, #2a)
**Status:** RUN, positive, noise-robust. Finite memory produces a genuine, quantized, tunable, noise-robust temporal rhythm on the certified substrate. Honest ceiling stated: this is a temporal stride/frequency, not full phase-wave behavior.

## The question, honestly bounded first

"Memory turns diffusion into waves" is real general physics. But in ED a front cannot reverse (P11 irreversibility — rho only increases, fronts advance or dwell, never go backward), so a single particle's *position* cannot oscillate spatially: genuine spatial waves are structurally off the table. The testable core is a **temporal rhythm** — do memory-driven hops come at regular, clockwork intervals (an emergent frequency, the seed of wave behavior) or at random intervals (stable average, no rhythm)? Full QM phase-waves (de Broglie) are NOT testable here: phase/polarity is not read by the certified Sigma (the same wall the mass work hit). This probe tests temporal rhythm only, and says so.

## Result 1 — the hops are a sharp, quantized, tunable stride

Discriminant: coefficient of variation (CV = std/mean) of inter-hop intervals at steady state (long chain = 20,000 nodes so the front never hits a boundary; 15,000 steps; first 3,000 discarded as transient; 6 seeds; ~24,000–48,000 hops per regime).

| k_mem | decay | mean interval | CV | reading |
|---|---|---|---|---|
| 0.05 | 0.95 | 1.50 | 0.33 | period-2 pattern (alternating 1,2) |
| 0.1 | 0.9 | 1.50 | 0.33 | period-2 pattern |
| 0.2 | 0.9 | 2.00 | **0.00** | exact clockwork: hop every 2 steps |
| 0.3 | 0.9 | 2.00 | **0.00** | exact clockwork: hop every 2 steps |
| 0.5 | 0.9 | 3.00 | **0.00** | exact clockwork: hop every 3 steps |

The interval distribution is not merely low-variance — at the clean regimes it is a **single value**: 100% of steady-state hops occur at exactly interval 2 (or exactly 3 at stronger memory). The stride is **quantized** (an integer number of steps) and **tunable**: stronger memory lengthens the stride (2 → 3), i.e. lowers the frequency. That is a genuine emergent frequency/wavelength born from finite memory — and its dependence on memory strength is a dispersion-relation-like structure (memory sets the frequency).

## Result 2 — the rhythm is NOISE-ROBUST, not a deterministic-toy artifact

The obvious worry: CV = 0.000 is almost too clean — is it a genuine rhythm, or just an artifact of the near-deterministic toy (default tie-break jitter = 1e-3)? The real P11 is primitively stochastic (phase-randomization), so the honest test is whether the rhythm survives real noise. Swept the jitter up by three orders of magnitude at a clean-clockwork regime (k_mem=0.3, decay=0.9; recall rho_star=0.5 is the signal scale):

| jitter | mean interval | CV | reading |
|---|---|---|---|
| 0.001 | 2.00 | 0.000 | rhythm survives |
| 0.01 | 2.00 | 0.000 | rhythm survives |
| 0.05 | 2.00 | 0.000 | rhythm survives |
| 0.1 | 2.00 | 0.033 | rhythm survives |
| 0.3 | 2.20 | 0.188 | rhythm survives (clear peak, some spread) |
| 1.0 | 2.16 | 4.96 | rhythm gone (Poisson/disordered) |

The rhythm survives noise all the way up to jitter ≈ 0.3 — which is **60% of the entire signal scale** (rho_star = 0.5). It only washes out at jitter = 1.0, i.e. when the noise **exceeds the whole density scale** (2× rho_star) — an unphysical regime where the background jitter is larger than the signal itself. There is a fairly sharp order→disorder transition between those two (CV jumps 0.19 → 4.96), like a melting point of the rhythm. **So the emergent stride is robust physics across the entire physically-sensible noise range, not a fragile artifact of the deterministic toy.**

## What this confirms, and the honest ceiling

**Confirmed:** finite chain-memory produces a real, quantized, tunable, noise-robust temporal rhythm — a stable stride/frequency that emerges purely from the memory dynamics. This is the honest, testable core of AP's "waves have memory," and it directly instantiates the "to persist is to pulse" framing at the single-chain scale: a persisting, re-committing front does not drift smoothly — it *ticks*, at a sharp, memory-set period.

**Ceiling, stated plainly (not buried):**
1. This is a *temporal* rhythm (a frequency/stride), not spatial oscillation (forbidden by P11) and not full phase-wave/de Broglie behavior (phase is Sigma-blind — unchanged wall). "Wave-adjacent," not "wave."
2. The rhythm requires the same added memory channel the mass work needed (`k_mem`, honestly-named new state) — it is not a property of the bare certified substrate, which is ballistic (hops every step, trivially).
3. The connection to actual stellar pulsation (helioseismology, Cepheids) is a *structural* rhyme — rhythm is what finite-memory handoff produces at every scale — not a demonstrated identity of mechanism or period. The scales differ enormously; don't conflate.

## Natural next step (for the "to persist is to pulse" thread)

The single-chain stride is established. The collective question — do many independent chain-rhythms **phase-lock** into a shared pulsation (the actual "a star pulses" claim) — is the natural follow-up: run multiple memory-carrying fronts with weak mutual coupling and check whether their strides synchronize (a Kuramoto-style phase-locking) or stay independent. Not yet built; banked in `Parked_Routes_And_Open_Threads.md` route 2a.
