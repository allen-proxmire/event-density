# Gleason Keystone, Reframed: Orthogonality is Operational (P11+P07), the Form is Forced by Complementarity (Solèr)

**Opened 2026-07-08** at AP's direction. The QM-kinematics keystone (#8b / Paper_004): derive the substrate inner product instead of inheriting it. Crank-rail ON. Read: `Paper_004_GleasonUniqueness.md`, `foundations/Gleason_Rehabilitation_Attempt.md`.

## The state (from the sources)

- The inner product needs two postulates: **P-Channel-Orthogonality** (`⟨K|L⟩=δ_KL`) and **P-Gleason-Compatibility** (non-contextuality).
- **P-Gleason-Compatibility:** bookkeeping half DERIVED (P02+P04: no decomposition-slot in the primitives); physical/Kochen-Specker half OPEN.
- **P-Channel-Orthogonality:** BLOCKING. Three routes fail (P04-additivity, P07-distinctness, P11-phase-randomization); a regime-conditional rescue was withdrawn (visibility `c_12` ≠ `⟨K|L⟩` — a which-path-vs-position conflation).
- **Even with both postulates**, Paper_004 §3.2 is explicit: the sesquilinear form is **constructed to match standard QM, not derived by uniqueness** ("under different postulates a different form would be constructed").

## The hidden mistake in all three routes

They seek orthogonality as a **kinematic/metric** fact inside a *pre-existing* inner product. ED has no pre-existing inner product; it is the object being built. So "prove `⟨K|L⟩=0`" is near-circular (build the free vector space over the channel index set and it is orthonormal *by construction*, as the rehabilitation note observed). The three routes are all attempts to derive-within-an-assumed-metric, which is the wrong frame.

## The reframe — two moves

### Move 1: the inner product is OPERATIONAL, from P11; then P07 gives orthogonality

ED's actual projective measurement is the **P11 commitment**: at a commitment, participation collapses to a single channel (a which-channel selection). Define the substrate inner product *operationally* via the commitment-measurement statistics (the Born frequencies, Paper_003), not as a pre-given metric. Under this operational definition:

- **P07 structural distinguishability** = distinct channels `K≠L` are distinct substrate objects that no substrate process conflates (Paper_087 §P07: "structurally distinguishable carriers with intrinsic identities... distinct even if bandwidth/polarity coincide").
- Operationally, states a single measurement **perfectly distinguishes** are **orthogonal** (this is the *definition* of orthogonality in an operational/quantum-logic inner product, not a theorem needing a prior metric).
- So `⟨K|L⟩ = δ_KL` **follows** from {operational inner product via P11-commitment} + {P07 perfect-distinguishability}. This realizes Paper_004's own **Conjecture 1** ("P-Channel-Orthogonality may follow from P07's structural-distinguishability applied at the inner-product level") with an explicit mechanism.

**Why the three routes failed, explained:** orthogonality is not kinematic; it is the operational content of the P11 commitment-measurement together with P07. Route 3 (P11) was aimed at the right primitive but the wrong target (it tried to force the metric directly, rather than *define* the metric operationally from the commitment).

### Move 2: the FORM is forced by P04–P09 COMPLEMENTARITY, via Piron–Solèr

The which-channel measurement (bandwidth `b_K`, P04, realized by the commitment) and the phase/interference measurement (polarity `π_K`, P09) are **genuinely complementary**:
- Committing to a channel (a sharp `b`/which-channel measurement) **destroys phase coherence** — P11 randomizes the phases of unselected channels at commitment (sourced: rehabilitation §3 route 3 / U2). This is exactly ED's **which-path-destroys-interference**: a which-channel measurement and a phase-coherence (interference) measurement cannot both be sharp.
- Complementarity ⟹ the lattice of substrate measurements is **non-Boolean / non-distributive (orthomodular)**: the which-channel and phase measurements do not commute, so their propositions do not form a Boolean algebra.
- The **Piron–Solèr theorem** (quantum logic): a complete, irreducible, orthomodular, atomic lattice satisfying the covering law and Solèr's angle condition (an infinite orthonormal sequence) is the lattice of closed subspaces of a Hilbert space over ℝ, ℂ, or ℍ, with the inner product **forced**.

So the inner-product FORM is not "constructed to match QM" — it is **forced** by a complementarity ED demonstrably has (P04-vs-P09, enforced by P11). This directly answers Paper_004 §3.2's honest limit (non-uniqueness) and reaches the field question (ℝ/ℂ/ℍ), connecting to the downgraded **T14** (complex-Hilbert): the ℂ selection is Solèr's remaining discriminator, not a separate postulate.

## What the reframe buys

The blocking postulate P-Channel-Orthogonality stops being a bare axiom: it becomes a **consequence** of {operational inner product from P11} + {P07 distinguishability}. And the inner-product form stops being a non-unique construction: it becomes **forced** by the P04–P09 complementarity via Solèr. Both moves use only ED structure (P04, P07, P09, P11) already in hand.

## Grounding checks (done, source-based)

1. **P11 commitment is a which-channel projective selection** — yes (P11 = commitment/collapse to one channel).
2. **Commitment destroys phase coherence (complementarity)** — yes (P11 randomizes unselected phases; = which-path destroys interference; ED's double-slit, F1 super-threshold interference is the corpus's own killable double-slit bet).
3. **P07 structural-distinguishability = perfect operational distinguishability** — yes (Paper_087 §P07: distinct channels are never-conflated substrate objects).

## Honest gaps / crank rail (the hard open core)

- **Move 1's link (perfect-distinguishability ⟹ orthogonal) must be made rigorous WITHOUT sneaking in Hilbert space.** The operational inner product must be *defined* (from commitment/Born statistics) so that the distinguishability→orthogonality step is by-definition, not by importing the QM theorem. This is the Gleason/quantum-logic construction; stating it cleanly for ED's commitment statistics is unbuilt.
- **Move 2 needs ED's commitment-lattice to satisfy ALL of Solèr's hypotheses** (orthomodularity, atomicity, covering law, the angle/infinite-orthonormal-sequence condition). Complementarity gives *non-Boolean*; establishing the *full* Solèr package is a large, deep program (Solèr's theorem is celebrated precisely because its hypotheses are strong). Do NOT claim the Hilbert space is derived; claim the *route* is grounded and named, with the lattice-verification the open core.
- The reframe **relocates** the keystone (from "postulate orthogonality" to "verify ED's logic is orthomodular-Solèr"); it does not *close* it. The payoff of the relocation: success would deliver orthogonality + the inner-product form + the ℝ/ℂ/ℍ field **all at once**, from complementarity ED already has, rather than three separate postulates.

## Tier + next steps

**Tier: a reframe with grounded ingredients, NOT a closed derivation.** The blocking postulate is relocated to an operational/complementarity footing (grounded), not eliminated; the Solèr lattice-verification is the remaining hard core.

**Next:** (a) construct the operational inner product from P11 commitment statistics explicitly and check the distinguishability→orthogonality step is non-circular; (b) exhibit two genuinely incompatible ED commitments forming a non-distributive (orthomodular) sub-lattice — the concrete first test of the quantum-logic claim (the b/π complementarity predicts they exist); (c) map ED's commitment-lattice against Solèr's hypotheses one by one, flagging which hold and which are open; (d) fold the ℂ-field discriminator into the T14 cross-check. Step (b) is the sharp, decidable entry: **does ED have a genuinely non-Boolean pair of measurements?** If yes, the quantum-logic route is on; if all ED measurements are compatible (Boolean), the logic is classical and the Hilbert space does NOT follow (a real potential negative).

---

## Step (b) DONE (2026-07-08) — the non-Boolean gate PASSES: ED's which-channel vs relative-phase logic is genuinely complementary

`evaluation/ChiralGauge/gleason_nonboolean_probe.py`. Tested whether ED's which-channel measurement (`b`, P04, via P11-commitment) and its relative-phase measurement (`π`, P09, via interference) are genuinely incompatible, using ED's own amplitude structure.

**Results (all from ED's primitives):**
1. **Interference is real:** the combined participation `|P_1+P_2|² = b_1+b_2+2√(b_1b_2)cos Δπ` swings from 2.0 (Δπ=0) to 0.0 (Δπ=π). The relative phase is an observable.
2. **Commitment destroys it:** averaging over the P11-randomized phase gives `|P_1+P_2|² → 1.0 = b_1+b_2`, interference gone. Which-channel measurement kills the interference.
3. **Uncertainty relation (the ED-native core):** a definite relative phase *forces* `b_1=b_2` (maximal which-channel uncertainty); a definite channel (`b_2=0`) leaves the relative phase *undefined* (no second channel to phase against). The two cannot be jointly sharp. **This follows directly from `P_K = √b_K e^{iπ_K}`: a relative phase requires shared participation across channels — an ED-native fact, no Hilbert space assumed.**
4. **Distributivity FAILS:** for A=channel-1, B/C=phase-eigenstates, `rank[A∧(B∨C)] = 1 ≠ 0 = rank[(A∧B)∨(A∧C)]` — the textbook non-Boolean fingerprint. MUB overlaps all 0.50.

**Verdict: the gate passes — ED's measurement logic is non-Boolean (complementary), grounded in the primitive fact that a relative phase requires shared participation.** The Piron–Solèr route is *on*: the inner-product form is a candidate *consequence* of this native complementarity, not a bare postulate.

**Honest tier + the circularity caveat (crank rail, post-homochirality-lesson).**
- **Parts 1–3 are genuinely ED-native and non-circular.** The complementarity (interference destroyed by commitment; the uncertainty relation) follows from `P_K=√b e^{iπ}` + P11, with no Hilbert-space assumption. This is real: ED *has* the complementarity the whole route needs.
- **Part 4 (the distributivity computation) is a FORMALIZATION, not independent evidence.** It represented channels as an orthonormal basis (`|1⟩=[1,0], |2⟩=[0,1]`) — i.e., it *assumed* P-Channel-Orthogonality to display the non-Boolean lattice. So Part 4 formalizes the complementarity of Parts 1–3 in a representation that already has orthogonality; it does not independently derive orthogonality. Read it as "the complementarity, once represented, is non-distributive," not "orthogonality proven."
- **This does NOT close the keystone.** It establishes the *premise* of Move 2 (ED is non-Boolean → Solèr applies). It does not (i) derive orthogonality non-circularly (Move 1's operational construction is still needed), nor (ii) verify the *full* Solèr package (atomicity, covering law, angle condition), which is the deep open core. The gate passing means the route is viable, not that the Hilbert space is derived.

**Net:** the sharp first gate passes — ED has genuine, primitive-grounded complementarity, so the quantum-logic route to the inner product is live (not a dead classical/Boolean structure). The remaining work is the honest hard part: the non-circular operational orthogonality (Move 1) and the Solèr lattice-verification (Move 2's completion). A real first advance on a keystone that was fully stuck, with the over-read boundary (Part 4) flagged rather than hidden.
