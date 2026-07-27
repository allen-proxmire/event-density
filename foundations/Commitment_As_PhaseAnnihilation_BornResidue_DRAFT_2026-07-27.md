> **SUPERSEDED / FAILED-CLOSURE (2026-07-27).** This draft mis-scoped an *interpretive reframe* as a *derivation* ("discharge row 14", "reduce P-LinRate"), which sent it to the wrong bar. Referee verdict: (1) row 14 is about *global* phase, a static gauge fact needing no P11, so it cannot be "discharged" by commitment; (2) commitment's real phase role is *relative*-phase / off-diagonal coherence removal = decoherence = einselection, which the Gleason keystone already holds as **primitive** (not new); (3) Tier-3a (P-LinRate reduction) is the circular relabel Paper_003 §3.2 already rejected; (4) Tier-3b (diagonal/off-diagonal unification) is loose analogy, different index structures. **The live version is the interpretation piece `ED_vs_ManyWorlds_ReadingTheSchrodingerEquation_2026-07-27.md`**, which keeps the two surviving factual points (global≠relative phase; ρ_KL≠Δ_KL) and drops all the discharge/reduction claims. Kept only as a failed-closure record so this is not re-run.

---

# Commitment as Phase-Annihilation: P11 and the Born Residue

**Date:** 2026-07-27
**Status:** DRAFT working note, pre-referee. Scoped as a **candidate discharge of Paper_008.5 (PhaseIndependence) audit row 14** ("Role of P11 in global-phase unobservability — OPEN, absent from body text"). Honestly tiered in §5. **Not for EDG** until refereed. Builds on, does not replace, Paper_003 (Born-as-frequency-limit).

## 0. One-sentence claim
The Born rule `|ψ|² = ψ*ψ` is the mathematical face of a commitment event: conjugation is time-reversal (Wigner), the U(1) phase is the reversible / not-yet-committed sector, and forming the product annihilates that phase and leaves the real, committed residue `b`. So **P11 (commitment) is the phase-annihilation**, and *that* is why global phase is operationally unobservable. Compactly: **time = commitment = fact**, and a fact is the phase-dead residue of participation meeting its own time-reciprocal.

## 1. What is already banked (credit, do not reinvent)
This note claims none of the following; they are the standing pieces it ties together.

- **Phase = reversible/gauge sector; `b` = real physical content.** Paper_008.5 §3.2–3.3: the polarity `π_K` is the gauge-charged sector; bandwidth `b_K` is the gauge-invariant real content; Born depends only on `b_K`.
- **Conjugation = time reversal, acting on phase but not bandwidth.** Paper_008.5 §3.6, verbatim in substance: `T: Ψ → Ψ*` sends `e^{iπ_K} → e^{−iπ_K}` and "leaves `b_K` unchanged." Both Wick rotation and `T` "act on the phase sector while preserving the bandwidth sector."
- **Born = `|P_K|² = b_K`**, the phase-invariant piece. Paper_002 (Born-Gleason), Paper_003 (frequency-limit route), Paper_U1 polar carrier `P_K = √b_K · e^{iπ_K}`.
- **Schrödinger evolution is pure phase / unitary / reversible.** `e^{−iHt}` acts in the `π` sector; the reversible sector is the phase sector. (Standard; consistent with ED's "unitary = the not-yet-committed, reversible limit.")

## 2. The gap this note targets (verbatim)
Paper_008.5 audit table, **row 14**:

> "Role of P11 (global-phase unobservability) — OPEN. Currently absent from body text; substrate role of P11 in fixing global-phase unobservability OPEN."

The corpus records, in its own hand, that it treats the phase-independence of `b` as a *static* fact of the polar decomposition (`b` simply does not depend on `π`) and has **no account of why commitment makes the phase unobservable.** That is the hole.

## 3. The move: from static invariance to active annihilation
Existing framing (static): `b_K = |P_K|` is, by polar decomposition, independent of `π_K`; hence global phase drops out of Born. True but inert. It says the phase is *ignorable*, not *why*.

Proposed framing (active): a commitment is the event in which the forward participation `P` closes with its time-reciprocal `P*` (P02 reciprocity read through Wigner `T = ` conjugation). Writing that closure out,

```
P*_K · P_K = ( √b_K e^{−iπ_K} )( √b_K e^{iπ_K} ) = b_K .
```

The phase does not "drop out"; it is **cancelled by meeting its own time-mirror.** The residue `b_K` is real precisely because it is what survives the annihilation of the reversible phase. Commitment (P11) *is* this operation. The global phase is unobservable **because a fact is definitionally the phase-dead residue of `P` meeting `P*`** — there is nothing left for a global `e^{iα}` to act on once the reversible sector has been annihilated into a fact.

This reads P11, the Born residue, and time-reversal as one structure:
- **P11 (commitment)** = the annihilation operation `P* · P`.
- **Born `|ψ|²`** = the residue of that operation (a real, committable weight).
- **`T` = conjugation** = the reason `P*` is the *backward* leg: the reciprocal is the time-reverse.
- **Unobservability of global phase** = there is no phase left in a fact; the phase lived only in the un-committed (reversible, Schrödinger) sector.

## 3.5 Sharpening: commitment = diagonalization of ρ (this is the load-bearing form)
The §3 statement "commitment annihilates the phase" is too coarse as written; its correct, stronger form is **commitment diagonalizes the density matrix.** Write `ρ = ψψ*`, entries `ρ_KL = ψ_K* ψ_L`.

- **Diagonal (`K = L`):** `ψ_K* ψ_K = b_K`. The Born residue. Phase-dead, real, committed. §3.
- **Off-diagonal (`K ≠ L`):** `ψ_K* ψ_L`. Carries the *relative* phase. Same-chain, this is **interference** (Paper_008.5 §3.4: relative phases ARE observable). Cross-chain via V5, this is exactly Paper_063's bilocal `Δ_KL` = **entanglement**.

So P11 does **not** annihilate all phase. It annihilates the **off-diagonal** phase content and leaves the diagonal. That operation is decoherence, and it is einselection (which the Gleason reconstruction already takes as *primitive*), and it lands on Born. One operation, three standing names. `|ψ|²` is the diagonal of `ρ`; the commitment event is the diagonalization.

**This pre-answers referee kill-test #3** (does "annihilate the phase" wrongly kill the observable relative phase?). No: pre-commitment the off-diagonals are alive, and that aliveness *is* the interference; commitment is precisely their removal. The reframe does not kill observable phase; it defines the moment observable coherence becomes a fact. Only the committed channel's off-diagonal coherences die; inter-channel interference is intact right up to the commitment event.

## 4. Why the amplitude is complex and the fact is real (a corollary, same structure)
A lone `P_K` is one-sided: complex, phase-carrying, reversible, not-yet-committed. It is only the *relation* `P* · P` (two-sided, participation meeting reciprocal) that is real. This is the corpus's "two is more fundamental than one" surfacing in the formalism: probability is real because it is a relation; the amplitude is complex because it is half of one. The "square" everyone reads as a brute exponent is the signature of two one-sided things closing, not a magic squaring.

Standing analogues in physics (for the referee, to place the reading, not to claim priority over): Cramer transactional (offer × confirmation handshake), Aharonov two-state-vector (forward preparation + backward post-selection), Schwinger-Keldysh / density-matrix `ρ = ψψ*` closed-time-path (ket forward, bra backward). In all three the `|·|²` is a forward leg meeting a backward leg. This note's only addition is the ED reading: the backward leg is P02 reciprocity, and the closure is the P11 commitment event.

## 5. Tiers (hold these; do not inflate)
- **Tier 1 (already banked, not claimed here):** phase = reversible/gauge sector; `T` = conjugation acting on phase not `b`; Born = `b`, the phase-invariant residue. §1.
- **Tier 2 (the actual proposal):** the *active* reading that P11 = **diagonalization of `ρ = ψψ*`** (§3.5), that `|ψ|²` (the diagonal) is the shadow of the commitment event, and that this is *why* global phase is unobservable. Scoped strictly as a **candidate discharge of Paper_008.5 row 14** and the cleanest formal home for "time = commitment = fact." **Not** a new derivation of Born (that stays Paper_003's frequency-limit route), and **not** a new derivation of decoherence/einselection (which the corpus already treats as primitive) — a synthesis naming them one operation. Closes a marked-open row.
- **Tier 3a (a LEAD, explicitly NOT banked):** that this reduces Paper_003's open **P-LinRate** postulate (why commit-rate is linear in `b`, not `b²` or `√b`). If `b` *is* the committed, phase-dead content by construction, then rate-of-fact-production tracking `b` is natural rather than arbitrary. It grounds "the rate tracks `b`"; it does **not** give the linearity, which stays a residual (≈ P04 additivity-of-opportunities). Partial reduction at most. Plausible, unproven.
- **Tier 3b (a LEAD, explicitly NOT banked, contingent on re-reading `Paper_QuadraticStrain`):** the diagonal/off-diagonal split of `ρ` may be the *same* `|ΣP|²` motif as the gravity line (per memory: `Str = |ΣP|²`, diagonal = Newton, off-diagonal = MOND). If so, one structure runs across three domains — diagonal = committed/classical (Born, product state, Newton), off-diagonal = coherent/uncommitted (interference, entanglement `Δ_KL`, MOND) — with **the arrow selecting the diagonal in every row.** Genuinely unifying, and precisely the too-clean claim to distrust until verified. Do not bank; verify `Paper_QuadraticStrain` first.

## 6. Referee brief (the breaker)
Check this against these specific corpus papers and answer: is it redundant with, or contradicting, established work? Is it re-deriving something the corpus already has?
- **Paper_008.5 (PhaseIndependence)** — does §3.6 + row 14 really leave P11's role undischarged, or does the body already imply it? (Read confirms row 14 is flagged OPEN as of its date; verify no later paper discharged it.)
- **Paper_004 (GleasonUniqueness — the real Born-Gleason; NOT the file named Paper_002, which is tensor-product)** — does the Gleason keystone already contain "commitment = phase-annihilation / ρ-diagonalization" under other words? (Read suggests NOT: Paper_004 derives the inner-product *form* via P-Channel-Orthogonality + P-Gleason-Compatibility, and explicitly rejected P11-phase-randomization as "wrong layer." Confirm.)
- **Paper_003 (Born frequency-limit)** — does this note contradict the frequency-limit route, or sit beside it as a different (interpretive) grounding? It must not silently replace P-LinRate.
- **Paper_063 (TensorProduct / entanglement)** — is the §3.5 identification of the off-diagonal `ρ_KL` with the V5 bilocal `Δ_KL` faithful, or does it conflate the single-chain relative-phase off-diagonal with the cross-chain bilocal term? (These must be the *same slot* of one structure for §3.5 to hold; if they are structurally different objects, downgrade §3.5.)
- **Paper_QuadraticStrain** — does it actually carry `Str = |ΣP|²` with diagonal = Newton / off-diagonal = MOND? Tier-3b stands or falls here. (Not re-read this session; memory-sourced.)
- **Paper_U1 (Participation Measure)** — is `P* · P = b` as "the committed residue" consistent with how U1 grounds `|P|² = b`, or does it smuggle a new assumption?
- **State-reduction / collapse-models paper** — does the objective-collapse comparison already say this?

Specific kill-tests to try:
1. **Is §3 circular?** Does "commitment = `P*·P`" secretly assume the Born form it purports to illuminate? (It should be read as *interpreting* an operation the formalism already performs, not deriving `|·|²` from nothing. If it reads as a derivation, downgrade to Tier-1-restatement.)
2. **Wigner scope.** `T = ` complex conjugation is exact for spinless nonrelativistic `ψ`; with spin there is the extra `σ_y`/antiunitary structure and momentum flip. Does the reading survive, or is it a spinless-corner artifact?
3. **Relative vs global phase.** Paper_008.5 §3.4: relative phases ARE observable (interference). §3.5 claims to answer this (commitment diagonalizes ρ; off-diagonals live pre-commitment = interference; only the committed channel's coherences die). **Verify §3.5 actually resolves it and is not itself circular** (does "diagonalization" presuppose a chosen basis = the pointer basis = the thing to be explained? If einselection-primitive is doing the basis-choosing, say so and confirm that is consistent with the Gleason reconstruction, not a new smuggle).
4. **Does it actually discharge row 14, or just rename it?** The failure mode is relabeling "b is phase-independent" as "commitment annihilates phase" with no added content. State plainly what, if anything, is *added* beyond §1. The candidate added content is §3.5 (P11 = ρ-diagonalization = einselection, giving the *mechanism* of global-phase unobservability, not just the *fact*). Judge whether that is genuine added content or a restatement.
5. **Tier-3b over-reach.** The diagonal/off-diagonal unification table (§5 Tier-3b) is the highest over-bank risk. Attack it: are "Born diagonal," "product-vs-entangled," and "Newton-vs-MOND" really the *same* diagonal/off-diagonal decomposition of one `|ΣP|²`, or three loosely-analogous splits being forced into one table? Default to the latter unless `Paper_QuadraticStrain` makes the identification exact.

## 7. If it survives
Write back to: Paper_008.5 (discharge or downgrade row 14), Paper_003 §6.3 (note the P-LinRate lead, tiered), the QM-kinematics README, and the relevant memory pointer ([[project_gleason_complementarity_reframe]] / Born notes). If it does not survive, record it as a failed-closure note (like the exactly-3 attempt) so a future session does not re-run it.
