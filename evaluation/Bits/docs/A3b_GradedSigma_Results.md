# A3b — Wiring Bandwidth Into Σ: Severance Stays Sharp, for a Deeper Reason

**Follow-on to `A3_TopologySigmaSweep_Results.md`, run 2026-07-01. That sweep found the certified rule's bandwidth field is dynamically inert — only a tie-break key, never a graded weight — so "reach" was necessarily a hard on/off switch. This note builds an experimental (not certified) variant where bandwidth genuinely scales Σ, Σ_graded = bandwidth × Σ_certified, and re-runs the same reach test. Result: severance still snaps in sharply, not smoothly — but for a real, structural reason this run surfaced, not because the graded mechanism failed to do anything.**

## 1. What changed

`Σ_graded(u,v) = bandwidth(u,v) × Σ_certified(u,v)` — the most natural, minimal way to make a channel's bandwidth a genuine multiplicative gain on how attractive it is to commit across, rather than a tie-break-only field. Everything else (candidate enumeration, extinction, commit mechanics) is an unmodified copy of the certified update loop. This is an experimental, uncertified variant — it does not touch or replace `graph.py`/`sigma.py`/`update.py`, which remain the source of truth for every other result in this project.

## 2. Result

| Bridge bandwidth | M1 (within-stratum) | M2 (across-boundary) |
|---|---|---|
| 0.5000 (= internal edge strength) | +0.006 (no signal) | -0.005 |
| 0.2500 | +0.642 | +0.002 |
| 0.1000 | +0.593 | -0.002 |
| 0.0500 | +0.642 | -0.005 |
| 0.0100 | +0.642 | -0.004 |
| 0.0050 | +0.593 | +0.002 |
| 0.0010 | +0.593 | +0.002 |
| 0.0001 | +0.593 | -0.005 |

Across four orders of magnitude of bridge bandwidth (0.25 down to 0.0001), M1 stays strong and M2 stays at the shuffle floor. There is no gradual fade from coupled to severed — the transition happens somewhere between 0.5 and 0.25 and then the system is flat.

## 3. Why, honestly — a deeper structural reason, not a failed experiment

This isn't a null result from a mechanism that didn't work. It's a real finding about *why* the boundary is sharp. The update rule is winner-take-all: at each step, a front commits to whichever admissible candidate has the single highest Σ. Once the bridge's bandwidth drops even slightly below the internal edges' bandwidth (0.5), any competing internal candidate — which shares the same underlying Σ_certified scale but isn't discounted — becomes more attractive by comparison, and the bridge is essentially never chosen as long as an internal alternative exists. It doesn't need to be *much* weaker; it just needs to lose the comparison, and once it does, the front effectively never crosses it — which looks, from the outside, exactly like decoupling, even though the edge was never marked as such.

**So the honest generalization is sharper than the original certified-rule finding, not softer:** severance in this substrate isn't just a property of a binary flag someone chose to include. It looks like a generic consequence of maximal-Σ, winner-take-all selection — any consistent relative disadvantage for a channel, however small, tends to produce near-total avoidance of it once alternatives exist, rather than a proportionally-reduced-but-still-real crossing rate. That's a stronger, more structural version of "the boundary is sharp" than "the rule happens to use an on/off switch."

## 4. The bw=0.5 anomaly, chased and mostly resolved

At bridge bandwidth exactly equal to the internal edge bandwidth (no discount at all), the original N=150 run read M1 ≈ 0.006 — apparently no signal at all, unlike every other bandwidth tested.

**Chased with a direct diagnostic** (larger batch, N=40, measuring the raw Pearson correlation between the two within-stratum halves directly rather than through the histogram MI estimator): the correlation is real and positive at bw=0.5, just markedly weaker than elsewhere — **+0.42**, versus **+0.87** at bw=0.25. The two halves land on the same side of their own median only 60% of the time at bw=0.5, versus 90% at bw=0.25. So this was never a dead zone with no relationship at all; it's a real but genuinely weaker correlation.

**The likely proximate cause:** the M1/M2 pipeline's histogram MI estimator uses only 2 bins (per the original size-sweep design) and is known to be a coarse instrument — strong correlations (like 0.87) come through cleanly, but a real, weaker correlation (0.42) sitting closer to the estimator's noise floor is plausibly what read as "near zero" at N=150.

**The honest remaining question — why the tie specifically weakens the correlation — is not fully nailed.** The working account: when the bridge exactly ties the internal edges in Σ-weight, the winner-take-all tie-break has more room to send the front across the bridge early, or to take a less predictable path generally, than when the bridge is even slightly weaker and reliably loses every comparison. That would decorrelate the two halves more often. This is plausible and consistent with the data, but wasn't directly verified by tracing individual step-by-step paths, so it's held at that tier — a working explanation, not a demonstrated mechanism.

## 5. Status

The follow-on question A3 raised — does severance become continuous once bandwidth is wired into the dynamics — has a real, honest, if unexpected, answer: **no, it becomes sharp even faster than the binary case might have suggested**, and the reason points at something more general about winner-take-all selection rules than about this substrate's particular decoupling flag. The bw=0.5 anomaly is resolved to "a real but weaker correlation, likely undercounted by a coarse estimator" — the headline finding stands, and the one open loose thread left is the precise mechanism (early bridge-crossing under exact ties) rather than the existence of the effect itself.
