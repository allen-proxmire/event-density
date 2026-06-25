# #2b · The Point-Gap Route — the Arrow Carries a Net Chirality (and a correction to SQ1b)

**Foundations computation — pursues the point-gap-winding route flagged in SQ1b, and revises SQ1b's verdict. Sims: `evaluation/ChiralGauge/chiral_winding.py` + `chiral_skin.py`. Result: SQ1b's "the arrow lifts doublers Wilson-style → vector-like" reading was *too hasty* — it imported the hermitian-Wilson outcome into a non-hermitian setting where it does not hold. The retarded (arrow) transport carries a **nonzero net spectral flow (±1) — a chiral-anomaly signature — and a non-Hermitian skin effect (all modes pick one direction)**: the signatures of a single net chirality, exactly what hermitian lattices (Nielsen–Ninomiya) forbid. So the arrow is a genuine candidate *mechanism* for chirality, not merely an escape from the no-go. This matches AP's standing intuition — "only one pattern is allowed." The relativistic / unitarity / anomaly bridges remain genuinely open; the toy result is 1+1D, not the Standard Model.**

**Crank rail — and it cut both ways this time.** In SQ1b the rail caught optimism (I had hoped the arrow gives chirality; the Wilson reading said vector-like, and I reported that). Here the rail cuts the *other* way: that pessimistic reading was itself unjustified — the correct non-hermitian computation shows net chirality. I report the correction, and I hold the line on what is still *not* shown (the relativistic chiral gauge coupling and its anomaly).

---

## 1. What was pursued, and the correction

SQ1b lifted the Nielsen–Ninomiya doublers via the observation that ED's retarded difference contains a free "Wilson term," and concluded — too quickly — that Wilson-style lifting gives a *vector-like* (non-chiral) fermion. That conclusion borrowed the outcome of the *hermitian* Wilson construction. ED's retarded transport is **non-hermitian** (the arrow), and in the non-hermitian setting the relevant question is not "is there a leftover Wilson mass" but "what is the **point-gap / spectral-flow topology** of the operator." This note computes that, and it is nonzero.

## 2. Three signatures of chirality from the arrow (computed)

| signature | hermitian (tR=tL) | retarded / arrow (tR≠tL) | meaning |
|---|---|---|---|
| **point-gap winding** (around E=0) | **0** | **±1** | non-hermitian topology; the class hermiticity forbids |
| **non-Hermitian skin effect** (open chain, mean eigenstate COM, N=80, mid=39.5) | **39.5** (extended, L/R symmetric) | **77–79** (all modes pile at one edge) | the arrow makes every mode pick **one direction** |
| **net spectral flow** under U(1) flux twist 0→2π | **0** (states up = states down: anomaly-free, vector-like) | **±1** (net flow) | a **chiral-anomaly** signature = **one net chirality** |

All three agree and all three are *zero in the hermitian case and nonzero with the arrow.* The decisive one is the **net spectral flow**: in 1+1D the net spectral flow under flux insertion *is* the net chirality (the chiral anomaly coefficient, by the index theorem). Hermitian lattices are pinned to zero (the N–N doublers make up-flow = down-flow — vector-like, anomaly-free). The arrow's non-hermiticity gives **±1 — a single net chirality.** That is the opposite of "vector-like."

So the corrected reading of the doubler-lifting: the arrow does not lift the doubler into a *vector-like* theory; it lifts it into a **chiral** one. The surviving mode is a single uni-directional (chiral) mode, with no opposite-chirality partner — and the skin effect is the position-space face of the same fact.

## 3. AP's intuition, vindicated

AP's standing intuition for the substrate has been that it must obey **"only one pattern allowed."** That is precisely what these signatures express. The arrow (P11; the strictly-retarded V1, T18) admits propagation **one way only** — and the consequences computed here are: every mode localizes one direction (skin effect), the spectrum winds one way (point-gap winding ±1), and the net chirality is ±1 (one handedness, no mirror partner). The mirror twin that hermiticity *forces* to exist (the N–N doubler — the "second pattern") is exactly what the arrow forbids. **"Only one pattern allowed" is the single net chirality.** The intuition predicted the physics.

This also re-unifies the thread: the same one-wayness of commitment that gives ED the khronon, α₁-safety, and the position-dependent clock is, on this reading, what gives it a *handed* fermion sector. Chirality as the arrow's fourth job is back on the table — and now with a computed signature behind it, not just a hope.

## 4. What is still NOT shown (the honest bridges)

The result is a 1+1D toy chirality, not the Standard Model's chiral gauge theory. Three genuine bridges remain, and they are where the difficulty now lives:

1. **The relativistic γ⁵ bridge.** Net spectral flow / point-gap winding is the *condensed-matter / discrete* chirality. The Standard Model's chirality is the Lorentz-covariant γ⁵ Weyl structure coupling to SU(2). Showing the discrete net chirality descends, under DCGT + Lorentz-covariantization, to a relativistic chiral *gauge* coupling is the open computation (and it needs the open substrate-V1 → Dirac chain, T4 §3.7). The toy gives the *structure*; the relativistic realization is unbuilt.
2. **Unitarity.** The non-hermiticity that *produces* the chirality is the arrow — i.e. non-unitarity. A chiral fermion from a non-unitary operator is not yet a sensible unitary QFT. ED's candidate resolution is already in hand in principle: **sparse commitment** — unitary evolution between rare irreversible commitments (the same structure behind α₁-safety). The claim to establish: the emergent, between-commitments limit recovers a *unitary* chiral fermion while the commitments carry the handedness. Open, but the mechanism is named.
3. **Anomaly cancellation (SQ3).** A single Weyl fermion is gauge-anomalous; the SM cancels anomalies across quarks and leptons per generation. Whether ED reproduces that cancellation is the hardest piece and the most plausible site of a genuine obstruction. Untouched.

## 5. Verdict

**Pursuing the point-gap route flips SQ1b's lean from "partial no (vector-like)" to "genuinely promising": the arrow carries a net chirality (spectral flow ±1, skin effect, point-gap winding ±1) — the very structure hermitian lattices forbid — so it is a real candidate *mechanism* for the Standard Model's parity violation, not just an escape from Nielsen–Ninomiya.** AP's "only one pattern allowed" intuition is the correct reading: the arrow permits one handedness and forbids its mirror. **But this is a 1+1D toy chirality, not a derivation of chiral gauge theory.** The honest status of #2b is upgraded from "hard, default vector-like" to **"open and promising, with three well-posed bridges": the relativistic γ⁵ descent (needs the open T4 coarse-graining), unitarity (via sparse commitment), and anomaly cancellation (SQ3, the hardest).** No relativistic chiral coupling is constructed here; no anomaly is computed; the claim is the *mechanism and its signature*, not the Standard Model.

**Honest trajectory across the four steps:** SQ1 — N–N does not bind ED (no torus, non-hermitian). SQ1b — the arrow lifts the doublers, *misread* as vector-like. SQ1c (here) — corrected: the arrow lifts them *chirally* (net spectral flow ±1), vindicating "one pattern allowed." The remaining work is the relativistic bridge + unitarity + anomalies — real, but now the arrow is a computed candidate mechanism for chirality rather than a wall or a vector-like dead end.

---

*Point-gap route for #2b (`chiral_winding.py` + `chiral_skin.py`). Corrects SQ1b: the "Wilson → vector-like" reading imported the hermitian outcome wrongly. Non-hermitian computation: the retarded (arrow) transport carries (i) point-gap winding ±1, (ii) the non-Hermitian skin effect (all modes localize one edge: COM 77–79 vs hermitian 39.5), (iii) net spectral flow ±1 under flux = a chiral-anomaly signature = ONE net chirality (hermitian is pinned to 0 = vector-like/anomaly-free). All three vanish hermitially and are nonzero with the arrow — exactly the chirality N–N forbids on hermitian lattices. So the arrow is a candidate MECHANISM for parity violation, not just an escape; AP's "only one pattern allowed" = the single net chirality, vindicated. Honest open bridges: (1) relativistic γ⁵ descent (the discrete chirality → Lorentz-covariant Weyl gauge coupling; needs open T4 substrate→Dirac chain); (2) unitarity (non-hermitian arrow → unitary emergent QFT via sparse commitment — mechanism named, not shown); (3) anomaly cancellation (SQ3, hardest). 1+1D toy chirality, NOT the Standard Model. Verdict: #2b upgraded from "default vector-like, hard" to "open and promising, three well-posed bridges." Crank-rail cut both ways: corrected my own over-pessimism, held the line on the relativistic claim. No coupling constructed, no anomaly computed, no number faked.*
