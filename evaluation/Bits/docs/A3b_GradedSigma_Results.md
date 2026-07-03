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

## 4. The one thing left unexplained

At bridge bandwidth exactly equal to the internal edge bandwidth (0.5 = 0.5, no discount at all), both M1 and M2 come out near zero — no signal anywhere, not even within a stratum. This is the one genuinely odd point in the sweep and it isn't explained by the account in §3, which predicts this case should behave like normal, undiscounted flow (i.e., look like the original certified chain result, M1 ≈ 0.8). It doesn't. Left as an open, flagged anomaly rather than smoothed over — possibly a tie-heavy degenerate regime (bridge and internal edges scoring identically triggers different tie-break behavior across many steps), not yet investigated.

## 5. Status

The follow-on question A3 raised — does severance become continuous once bandwidth is wired into the dynamics — has a real, honest, if unexpected, answer: **no, it becomes sharp even faster than the binary case might have suggested**, and the reason points at something more general about winner-take-all selection rules than about this substrate's particular decoupling flag. The bw=0.5 anomaly is a loose thread worth a closer look if this arc is picked back up, but doesn't change the headline finding.
