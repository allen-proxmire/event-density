# Collective phase-locking / pulsation test — results

**Date:** 2026-07-06 (route 2a, "to persist is to pulse" → "does a star pulse")
**Status:** RUN, clean NEGATIVE with a precise boundary. Independent memory-fronts do NOT phase-lock into a collective pulsation under the substrate's native coupling; the coupling is dispersive (traffic-like), not synchronizing. The single-chain rhythm (route 2) stands; the collective leap does not come for free.

## The question

Route 2 established a single chain has a real, robust temporal rhythm (a quantized, noise-robust hop-stride). The "a star pulses" claim is the collective version: do many memory-carrying chains, coupled, phase-lock into a shared pulsation (Kuramoto-style synchronization)?

## Honest design + a caught measurement error

Fronts get a **spread** of natural tempos (different memory strengths — identical oscillators would "sync" trivially by being copies; real synchronization is *different* frequencies pulled together). Coupling is the substrate's **native** channel, not invented: a committing front raises rho (certified `commit`), which others read in their Sigma (certified `compute_sigma`), plus excluded volume (two chains can't occupy one locus). Geometry: a ring, so fronts keep re-encountering each other. Per-decision physics is the certified rule verbatim.

**First run was invalid — a red flag caught it before any interpretation.** The single-front sanity check hopped every step (rate 0.998) instead of the expected period-2 rhythm, and the collective null came out nonsensical. Root cause (diagnosed, real, not a code bug): on a *closed* ring, rho is irreversible (monotone-increasing), so the ground **saturates** — and once saturated, dwelling stops paying off and the rhythm dies. The measurement window (post step 1500) was entirely in the dead, saturated regime. Fixed: a big ring (3000 nodes) and a **fresh window** [200,1000] verified pre-saturation by an explicit rho tracker (mean rho rises only 0.51 → 0.84 across the window; single-front rate = exactly 0.500 = period-2 dwelling alive). *(The saturation itself is a real, honest finding: the same irreversibility that creates the single-chain rhythm kills the collective one on a closed system — see "what this means" below.)*

## Result — two measures, both negative

**1. Frequency-locking: NEGATIVE.** The spread of per-front hop-rates was *larger* coupled than isolated (ratio 1.51), not smaller. Coupling does not pull tempos toward a common value — it disperses them. Physically sensible: shared-rho + exclusion is a *traffic-like* interaction (a front hitting another's high-rho trail or getting blocked slows; one with fresh ground ahead speeds up), which increases heterogeneity (jams and gaps), the opposite of Kuramoto attraction.

**2. Collective phase-synchronization: NEGATIVE, established rigorously.** The raw population activity did show a period-3 peak 22× above a naive null — but that null was too aggressive (it destroyed individual periodicity too, so "coupled >> null" only proves the fronts are individually rhythmic, which we already knew). The correct test is a **phase-randomized surrogate**: keep each front's exact rhythm, randomize only its phase offset, 100 surrogates per seed. Result across all 5 seeds: the real collective oscillation amplitude (0.87–1.12) is if anything *slightly below* the random-phase surrogate (1.18–1.29), z = −1.0 to −1.8. So the period-3 aggregate peak is **fully explained by individual periodicity, not collective alignment** — and the coupling mildly *de*-synchronizes rather than syncs, consistent with the traffic-like frequency result.

## What this means

**The single-chain pulse is real and robust (route 2). The collective pulse does NOT emerge for free.** Under the minimal certified substrate's own native coupling (shared rho + exclusion), independent chain-rhythms stay independent — indeed the coupling is dispersive, mildly anti-aligning. And separately, irreversible rho-saturation kills even the individual rhythm on a *closed* system over time.

Both point the same way, and it's an honest, meaningful result about "a star pulses": collective sustained pulsation needs ingredients the minimal substrate lacks —
- a genuinely **synchronizing** (attractive phase) coupling, which shared-rho + exclusion is not; and/or
- an **open / throughput** system, so irreversible accumulation doesn't saturate the medium and freeze the rhythm.

Real stars have both (genuine pressure↔gravity restoring forces; open energy throughput). So the honest read is not "ED can't produce a pulsing star," but "**the bare substrate's native coupling is dispersive, not synchronizing, and a closed system saturates — collective pulsation requires more structure than the minimal substrate provides, exactly the structure real stars have.**"

## Honest scope

Tested **one** coupling geometry (ring; shared-rho + exclusion). A negative here does not prove collective synchronization is impossible in ED — it shows the *minimal native* coupling doesn't produce it. A genuine cross-chain phase-coupling (e.g. an actual V5 kernel, which is exactly the finite-memory cross-chain object still uncharacterized — target A2) could in principle be attractive/synchronizing; untested. That is the natural next question if this thread resumes: does a V5-style cross-chain coupling synchronize where shared-rho does not?

## Relationship to prior results

Does not touch route 2's single-chain rhythm result (that stands). Sharpens the "to persist is to pulse" framing: persistence gives each chain its *own* beat (confirmed), but a *shared* beat across chains is not automatic — it needs a synchronizing coupling this substrate doesn't natively have. The pulse is individual, not (yet) collective.
