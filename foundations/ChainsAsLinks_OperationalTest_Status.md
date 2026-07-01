# The Operational Test: Three Real Fixes, Still No Verified Geometric Witness — Honest Status

**Foundations — matter-sector / #2b arc, continues `ChainsAsLinks_MultichainV5_Reachable.md` and `ChainsAsLinks_LocalVsRandom_Correction.md`. Those notes established, on solid ground, that a graph built from ED's own combinatorial rules (single-chain composition + V5 cross-links) can contain a genuine K6 minor at modest coupling density, a real, abstract, graph-theoretic result. This note documents a good-faith attempt to go one step further, actually verifying that guaranteed linking geometrically, and running the real operational test (does undoing an order force a collision) on it — and where that attempt currently stands: not yet successful, after three separate, real methodology fixes, each catching a genuine flaw.**

## 1. What was attempted, and what kept going wrong

**Attempt 1.** Close each K6-minor branch set into a loop via a greedy nearest-neighbor tour through its embedded points, compute linking numbers, attempt separation.
**Flaw found:** a branch set is only guaranteed to be a *connected subgraph*, not a cycle — there was no real loop there to close in the first place. Confirmed by testing the same closure method on a known-linked control under realistic scatter: it reported erratic, non-integer values (-1.02, +0.24, +1.89, +0.32) that didn't track the true answer at all past mild jitter.

**Attempt 2.** Replace the greedy tour with a geometric fix (project onto best-fit plane, sort by angle).
**Improvement:** fixed the negative control completely — a genuinely unlinked pair now reads exactly zero at every jitter level.
**Flaw remaining:** the positive (known-linked) control still broke down under realistic scatter (-0.73, +2.42, +0.32) — a better closure heuristic, but still an arbitrary geometric imposition rather than something grounded in the graph's real structure.

**Attempt 3.** Stop imposing loops on branch sets at all. Use the actual mathematical content of "K6 is intrinsically linked": split the six branch sets into two genuine triangles, using real graph edges (the verified K6-witness connections) plus real internal BFS paths within each branch set, and compute linking numbers between these two authentic, graph-grounded cycles, for all ten possible 3-3 splits.
**Real improvement:** this produced, on the first pass, several near-integer readings (+0.98, +0.94, +0.92) against a clean-zero control — a much more promising, well-grounded result.
**Flaw found on closer inspection:** these readings did not survive a resolution-convergence check. Densifying the *same* real paths (more sample points along the same existing edges, no new topology) drove every one of the ten splits' linking numbers toward small, non-integer, or zero values — none converged to a clean integer. The earlier near-integer readings were themselves coarse-sampling artifacts, caught the same way the -0.355 reading in a side-check was caught converging to ~0.

## 2. Where this leaves things, honestly

**What still stands, solidly:** the abstract graph-theoretic result. A K6 minor genuinely exists in this graph at this coupling density (verified directly: six disjoint connected branch sets, all fifteen pairwise cross-connections confirmed). By Robertson–Seymour–Thomas, *some* embedding of this graph into 3D space must contain two linked cycles. That mathematical guarantee does not depend on anything in this note and is untouched by any of the three failed attempts above.

**What has not been achieved:** a trustworthy, verified, geometric example of that guaranteed linking, in a specific embedding, clean enough to run the actual operational test (does trying to undo an order force a collision) on with any confidence. Three real methodological problems were found and, in sequence, only partially fixed: (i) branch sets aren't loops, (ii) even correctly-identified real cycles need resolution-convergence checking before a linking number can be trusted, and (iii) the individual cycles themselves were never verified to be simple, non-self-crossing curves in their own right, which is also required for the linking number to be well-defined. That third issue was surfaced but not addressed.

## 3. Why this is a hard problem, not a quick one

Testing whether a graph's *guaranteed* intrinsic linking is realized in one specific, honestly-constructed embedding turns out to be a genuine computational-geometry problem, not a short script. The published literature on intrinsic linking and linkless embeddings (the same Robertson–Seymour–Thomas result this arc has leaned on throughout) has real, established algorithms for this kind of verification; an ad hoc force-directed layout plus a Gauss-integral convergence check, built fresh this session, is a reasonable first attempt but has now failed three times in three different ways. That pattern — each fix catching a real, distinct flaw rather than converging toward a working method — is itself informative: it suggests the next attempt should reach for established methods rather than a fourth home-built patch.

## 4. Status of #2b's fourth item

Unchanged from the graph-theoretic result: structurally reachable, concretely demonstrated at the abstract level, robust to coupling shape (local vs. random). The operational question — does undoing a committed order actually require passing through this structure — remains genuinely untested, and this note documents a real, honest attempt that did not get there, rather than pretending either a positive or negative result was achieved. The next attempt at this specific piece should use an established linkless-embedding-detection method rather than another ad hoc geometric construction.
