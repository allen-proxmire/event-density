# Reading the Same Equation the Other Way: Event Density vs Many-Worlds on the Born Rule and the Arrow

**Date:** 2026-07-27
**Genre:** Interpretation / positioning argument, not a derivation. It is "as provable" as Many-Worlds, pilot-wave, or a dark-matter particle: it earns its keep by coherence, parsimony, and explanatory reach, not by theorem. The only thing proved here is comparative: that Many-Worlds carries specific costs, and that reading the same formalism with commitment as primitive does not carry them. Factual throughout; it must not misstate the mathematics or overstate what ED derives (see the honest-tier section, §7). Supersedes the discharge-framed draft `Commitment_As_PhaseAnnihilation_BornResidue_DRAFT`, which asked the wrong question (it tried to "discharge" a mis-posed audit row); its two surviving factual constraints are carried into §3 and §7 here.

## 1. What this is, and what it is not
Hugh Everett did not prove anything. He took the equations everyone already had and said: read them literally, all the way down, and drop the collapse postulate. Many-Worlds is a *reading*. Its appeal is that it is the most austere reading, the one that adds nothing to the Schrödinger equation. This note offers a different reading of the very same equation, one in which the primitive is not reversible unitary evolution but irreversible commitment. Neither reading is a theorem. The question between them is which reading pays less and explains more.

We grant Many-Worlds its genuine strength up front, because a critique that does not steelman its target is worthless. As Sean Carroll puts it, the theory "is not about the worlds, it is about obeying the Schrödinger equation all the time." At the level of postulates it is the simplest quantum mechanics anyone has written down. That is real, and it is the thing to beat.

## 2. The disagreement is one bit
Both readings agree on the radical part: spacetime is not fundamental, it is emergent. Carroll builds it out of a vector in Hilbert space; ED builds it out of a relational substrate of participating chains. They agree there. They disagree about the floor:

- **Many-Worlds:** the ground floor is *reversible*. A universal wavefunction evolving unitarily is the whole of reality; irreversibility, definiteness, and the arrow are emergent appearances.
- **Event Density:** the ground floor is *irreversible*. Commitment (the arrow) is primitive; unitary Schrödinger evolution is the coarse-grained, reversible description of the not-yet-committed substrate.

Everything else follows from that one bit. The rest of this note is what the bit buys and what it costs on each side.

## 3. Three things Many-Worlds owes, and why they are one thing
Take unitary evolution as the complete fundamental law and three bills come due.

**The probability problem.** If every outcome happens on some branch, each with a real copy of you, then "how likely is spin-up" is a counting question, and naive counting gives even odds, not the Born weights. To recover `|ψ|²` you must make a low-amplitude branch "count less" while insisting it fully exists. Carroll's route is self-locating uncertainty plus a claim that there is an obvious right way to assign credences. It is contested precisely because assigning unequal weight to equally-real worlds is the thing the ontology cannot cleanly define. The one empirical fact that made anyone believe quantum mechanics, the Born rule, is the shakiest plank in the most austere theory.

**The preferred-basis problem.** The formalism does not say which basis the worlds branch along. Why definite positions and pointer readings, rather than some superposed basis? The standard answer is decoherence: the environment monitors certain observables and einselects a pointer basis. That is a patch applied on top of unitarity, not something unitarity hands you.

**The arrow.** Unitary evolution is time-symmetric, so the arrow of time must be imported as a special low-entropy boundary condition on the whole universe, the past hypothesis.

These are not three separate debts. They are one debt seen three ways. Each is a hole you inherit the moment you take the *reversible* description as the fundamental thing. You then spend the theory buying back what reversibility scrubbed out: definiteness, weight, direction.

A factual guardrail, since this is where loose interpretation dies. What decoherence removes is not the *global* phase of the state. Global phase is unobservable for a trivial static reason (it cancels in `ρ = ψψ*` by construction, with or without any measurement). What is at stake is the *off-diagonal, relative-phase* content of the density matrix, the coherences between distinct outcomes. Those are physical (they are interference), and their fate is the crux below.

## 4. The other reading: commitment first
Make commitment primitive. Then the objects of the formalism read differently.

The amplitude `ψ` is one-sided: complex, phase-carrying, reversible. It is the not-yet-committed sector, and unitary Schrödinger evolution `e^{-iHt}` is exactly its reversible internal turning. Superposition is not "many coexisting worlds," it is "not yet closed."

A fact is what you get when that one-sided thing closes with its own reciprocal. Complex conjugation is time reversal (Wigner; exactly so for the spinless scalar phase carrier, with the usual `σ_y` and momentum-flip dressing once spin is included). So `ψ*` is `ψ`'s backward leg, and the density matrix `ρ = ψψ*` pairs the forward leg with the backward one. Its diagonal entries `ψ_K* ψ_K = |ψ_K|²` are real, phase-free, and committed: the Born weights. Its off-diagonal entries `ψ_K* ψ_L` carry the relative phase: interference between outcomes of one system, and, when the two indices sit on different subsystems, entanglement (a distinct object from the single-system coherence, a close cousin, not the same matrix entry).

In this reading, commitment is the diagonalization of `ρ`. It removes the off-diagonal coherences and leaves the diagonal facts. That operation already has two standard names, decoherence and einselection, and ED takes it as primitive rather than as a patch: committing *is* selecting a definite outcome in the channel basis. The Born rule is not a magic squaring bolted onto the theory. It is the phase-dead residue that a commitment leaves behind.

## 5. The crux: the fate of the off-diagonal coherences
Here is the whole ED-vs-Many-Worlds disagreement in one concrete, checkable statement. Write `ρ = ψψ*` and ask what happens to its off-diagonal coherences when a measurement occurs.

- **Many-Worlds:** they never vanish. Unitarity preserves them exactly, forever. They only delocalize into the wider environment and become practically inaccessible. Every outcome remains real on its branch; the road not taken is another world.
- **Event Density:** commitment genuinely diagonalizes `ρ`. The off-diagonals are removed, not hidden. One outcome becomes a fact and the alternatives are gone. One world.

Same matrix. Opposite fate for its off-diagonals. That single divergence is the entire disagreement, stated without metaphysical hand-waving. It also says where, in principle, the two could be told apart: any physical process that genuinely removes coherence (rather than merely dispersing it) is an ED event and a Many-Worlds impossibility. That is the same frontier as objective-collapse tests and matter-wave interferometry, and it is the honest reason ED sits nearer the objective-collapse family than nearer Everett, but with the collapse grounded in a primitive rather than added as a stochastic term with free parameters.

## 6. How the one bit pays off the three debts
- **Probability.** There is one world; the alternatives do not happen. "How likely" is not "how many copies of me," it is "which commitment occurs." Born weights are propensities of a single committal event on the actual outcome space, not shares assigned to equally-real branches. The counting paradox does not arise because there is nothing to count.
- **Preferred basis.** It is not derived from the environment watching you. Committing *is* basis selection. Einselection is the primitive, the same primitive Many-Worlds has to reconstruct via decoherence. ED pays for the basis once, at the foundation; Many-Worlds pays for it repeatedly, downstream.
- **Arrow.** It is the floor, not a boundary condition. No past hypothesis surcharge is needed, because time-asymmetry was never scrubbed out to begin with. Carroll buys the arrow back at the end; ED never sells it.

## 7. What ED does not claim here (the honest tiers)
This is an interpretation, and it must wear its tiers even in argument.

- ED does **not** derive quantum mechanics from nothing. Its substrate reproduction of the Born rule is postulate-conditional (it rests on a substrate rate-vs-bandwidth commitment and a participation-measure identification), and pieces of the Hilbert-space scaffolding (channel orthogonality, the inner product) are conditional or inherited. This note does not lean on any of those being closed. It leans only on the *reading*: that `|ψ|²` is the committed diagonal residue and the off-diagonals are the reversible sector.
- "Commitment = the fact-making diagonalization" is ED's *primitive*, not a result proved here. That is the point: Many-Worlds has to manufacture einselection from unitarity and never quite finishes; ED posits it and reads everything else off it. Whether posit-one-arrow beats reconstruct-it-from-a-timeless-vector is exactly the interpretive judgment on the table.
- The claim is not "Many-Worlds is refuted." It is "Many-Worlds carries three costs traceable to one choice, and the opposite choice does not carry them." That is a comparison, not a proof, and it is the same kind of case Everett himself made.

Many-Worlds' best reply, honestly stated, is the historical one: the usual failure mode in physics is losing the courage of your theories, not-taking-your-equations-literally-enough (Carroll's Kelvin's-paradox point). The ED answer is that "take your theory literally" only points at Many-Worlds once you have assumed *which* theory is fundamental. Both sides agree you should take the fundamental theory dead seriously. They disagree about whether the fundamental theory is the reversible Schrödinger equation or the committing substrate beneath it. If it is the latter, then crowning unitarity as the literal whole of reality is not courage, it is mistaking the continuum for the molecules. Which theory is fundamental is the entire question, and the "courage" argument quietly assumes its answer.

## 8. Bottom line
Many-Worlds is the most honest reading of the Schrödinger equation *if that equation is the bottom.* Event Density is the reading you get if it is not, if unitary evolution is the reversible shadow of a substrate that commits. The two agree the formalism is right and that spacetime is emergent, and they disagree on one bit: the reversibility of the floor. From that one bit, Many-Worlds inherits the probability, basis, and arrow debts, and ED does not, at the price of a single primitive: the arrow. Same equation, read the other way.

---
*Positioning piece for the outreach/critique line. Companion targets, same mode: GR two ways from ED; Newton's G and 3+1 dimensions each several ways; the QM-kinematics reproduction. All to be written with tiers intact.*
