# A Narrow, Honest Negative — and a Trap to Not Fall Into (the N-N Parallel)

**Foundations — matter-sector / #2b arc, continues `ChainsAsLinks_Scoping.md`. This note delivers the graph-theory check the scoping note called for, and is careful about its scope in a way modeled directly on how the program already handled Nielsen–Ninomiya: a no-go result only binds the structure it actually assumes, and it's easy to mistake "closed for a narrow toy model" for "closed for ED." This note keeps the two apart on purpose.**

## 1. The check the scoping note asked for

`ChainsAsLinks_Scoping.md` reframed "does ED hold order by linking" into an embedding-independent, graph-theoretic question: does ED's channel-composition structure force linking under *any* 3D embedding — a property called **intrinsic linking**, characterized by containing one of seven specific graphs, the **Petersen family** (Robertson–Seymour–Thomas). This needs no simulation and no assumed continuum; it's a fact about the graph alone.

ED's own primitive documentation (`archive/quantum_primitives_review/07_channel.md`, "Channel composition") states the composition rules for a single chain's channels plainly: **sequential composition** (two channels sharing an endpoint, chained together) and **branching / merging** (a fork, then a rejoin — literally the Mach-Zehnder interferometer example given in that same document). Those two operations are, close to verbatim, the textbook definition of a **series-parallel graph**.

## 2. The clean, correct, narrow result

Series-parallel graphs have a well-established property: they are always **planar** — they can be drawn flat, in a single plane, with no edges crossing. And a graph that can be drawn flat can never be intrinsically linked, because a flat drawing is itself a witness that *some* embedding has zero linking (two curves confined to one plane can never wind around each other), and intrinsic linking requires *every* embedding to link. One counterexample embedding is enough to rule it out.

**So: the single-chain channel-composition graph, as ED's own documentation currently describes it, cannot force linking. This is a genuine, checkable, correct negative — no simulation, no proxy, no fidelity gap.**

## 3. The trap — and why this negative does not belong on the ED house

This is exactly the shape of mistake the program already learned to avoid with Nielsen–Ninomiya. N-N's proof needs two specific things — a rigid, periodic lattice, and a hermitian (time-reversible) rule — and it was verified, carefully, that ED has neither, before anyone was allowed to treat the no-go as binding. The lesson generalizes: **a no-go result only rules out the structure its proof actually assumes.** Mistaking "this narrow model fails" for "ED fails" is the trap.

The planarity argument above needs its own specific structure: a graph built *only* from one chain's own sequential/branch/merge composition. That is a real thing ED describes, but it is a small, local picture, one chain's private interferometer diagram. It is **not** ED's full participation graph. The full graph includes many chains simultaneously, cross-chain correlations (the V5 kernel), and whatever structure actually links different chains' commitment orders to each other — none of which the single-chain composition rules touch at all. Cross-chain edges are exactly the kind of addition that can push a graph out of the simple, planar, series-parallel class and into a much richer one; nobody has characterized what that larger graph looks like.

**So the honest position is: closed for the single-chain toy diagram. Open for the ED house.** The full participation graph's connectivity, once someone actually characterizes it (most likely via the existing V5 cross-chain structure, or downstream of the curvature-emergence arc), is a separate, larger, currently unanswered question — and it may well be answered by other, already-running work before this specific thread gets back to it.

## 4. What this note does and does not claim

**Claims:** the single-chain channel-composition algebra, exactly as ED's own P07 documentation states it, is series-parallel, hence planar, hence cannot be intrinsically linked. This is solid, standard graph theory, not a simulation result and not subject to the fidelity problems of the retracted probe.

**Does not claim:** that ED's substrate as a whole cannot hold order by linking. That would require characterizing the full, multi-chain, cross-correlated participation graph, which this note does not attempt and which remains genuinely open.

## 5. Status of #2b's fourth item

Narrowed, not closed. "Does ED hold commitment-order by spatial linking" now reads precisely as: **ruled out for the single-chain composition picture; open, and dependent on future characterization of the full cross-chain participation graph, for ED as a whole.** No further action needed on this thread until that characterization exists elsewhere in the program (most naturally as an extension of the V5 cross-chain work, not a new dedicated push).
