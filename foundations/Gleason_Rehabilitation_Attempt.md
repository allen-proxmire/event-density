# Rehabilitating P-Gleason-Compatibility and P-Channel-Orthogonality Against the Current Primitives

**Foundations — QM-kinematics / #8b arc. Direct attempt, not a scoping pass — this note works the actual derivation, having found (via the 2026-07-02 reconciliation audit, see `docs/ED_Research_Targets.md` item 8b and the corrected `theorems/T10.md`/`T11.md`) that the two prior corpus attempts (`arcs/born_gleason/`, `arcs/U2/`) used a retired primitive set and, in U2's case, a circular step. This note starts fresh from `Paper_004_GleasonUniqueness.md`'s two named postulates and today's canonical P02/P04/P07/P09/P11 (`Paper_087_13Primitives.md`).**

---

## 1. The two targets, restated precisely

From `Paper_004_GleasonUniqueness.md` §2:

- **P-Gleason-Compatibility:** the probability assigned to outcome $K$ in any substrate-channel-decomposition containing $K$ depends only on $K$'s own substrate amplitude content, not on the rest of the decomposition.
- **P-Channel-Orthogonality:** distinct substrate channels $K \neq L$ satisfy $\langle K|L\rangle = \delta_{KL}$ in the substrate-level inner-product structure.

Paper_004 could not derive either from P07+P08 alone and left both as open conjectures.

---

## 2. P-Gleason-Compatibility — a real, narrower argument found

**Claim.** Under the current primitives, P-Gleason-Compatibility holds in a specific, honestly-bounded sense: **"decomposition" carries no primitive-level slot to act as a hidden input to $b_K(u)$.**

**Argument.** P04 (bandwidth) states its content directly: *"Each channel-locus participation carries a bandwidth $b_K(u) \geq 0$."* This is a two-argument function of $(K, u)$ — full stop. Nothing in P02 (participation as a four-tuple $(C,K,u,t)$), P03 (channel/locus indexing), or P04 itself introduces a third argument for "which larger set of channels $K$ is currently being grouped with." A **decomposition** $\mathcal{D}$ of the available-channel set $\mathcal{K}(u)$ is not a substrate-level object at all in the current 13-primitive vocabulary — it is a bookkeeping act performed by whoever is describing the state (an external analyst choosing how to partition an already-fixed set of $(K,u)$-bandwidth facts). Since $b_K(u)$'s definition has no decomposition-argument to begin with, and the Born-type probability ratio $P(K) = b_K(u) / \sum_{K' \in \mathcal{D}} b_{K'}(u)$ (Paper_003) is built entirely from $(K,u)$-indexed bandwidth values, the only place a decomposition choice could enter is the normalization sum — and for any *complete* decomposition of the same $\mathcal{K}(u)$, that sum is the same intrinsic total (the full available bandwidth at $u$ for chain $C$'s rule-type, itself a $(u, \text{rule-type})$-indexed quantity, not decomposition-indexed). So the ratio cannot vary with $\mathcal{D}$.

**This is real, and it's cleaner than born_gleason Memo 02's version** — it doesn't need Memo 02's old-P11 (Born-weighting pre-loaded into the primitive, now recognized as circular) and it doesn't need Memo 02's "apparatus loophole" argument (which resolved contextuality by definitional fiat, per the 2026-07-02 audit). This version doesn't need to argue that an apparatus can't change $b_K(u)$ — the claim is purely that the mathematical object "decomposition" has nowhere to enter the current primitives' definitions at all.

**The honest limit, stated plainly.** This closes only the *bookkeeping* reading of non-contextuality — that relabeling or regrouping a fixed set of channels can't change the math. It does **not** address the physically loaded, Kochen-Specker-flavored reading Gleason's theorem actually needs: whether the probability assigned to $K$ can depend on which *other, physically distinct, mutually incompatible measurement context* $K$ is embedded in — i.e., whether coupling the system to a genuinely different apparatus (a different physical resolution of channels, not just a different way of listing the same ones) could change $b_K(u)$. That question is about physical coupling, not bookkeeping, and nothing above touches it. This is the same gap Memo 02's "Loophole 2" tried and failed to close (per the 2026-07-02 audit) — this note does not claim to have closed it either. It closes a real, non-trivial, narrower piece cleanly, and names the remaining physical piece precisely instead of papering over it.

**Verdict: P-Gleason-Compatibility, bookkeeping sense — DERIVED, from P02+P04 alone, no old-primitive dependency, no definitional apparatus-loophole. Physical (measurement-context) sense — still OPEN, honestly unaddressed.**

---

## 3. P-Channel-Orthogonality — tried three routes, all fail; found a sharper reframe

Three candidate derivation routes were tried directly, using only the current primitives:

**Route 1 — P04 additivity.** P04's stated content: $b_{K_1 \cup K_2} = b_{K_1} + b_{K_2}$ for *disjoint* sub-channels. Does this force zero cross-channel interference (orthogonality)? No — additivity of the *bandwidth scalar* under channel-union is a different claim from additivity of *squared amplitude under vector superposition*. The two coincide only if the cross-coherence term vanishes ($b_{\text{combined}}^2 = b_1^2 + b_2^2 + 2c_{12}b_1b_2$ with $c_{12}=0$) — which is itself the orthogonality condition being sought, not a consequence of P04's bare wording. This is the same gap born_gleason Memo 02 flagged as its own "Loophole 1" and did not fully close.

**Route 2 — P07 channel distinctness.** P07 gives channels *intrinsic identity* — $K \neq L$ as substrate objects, even with matching bandwidth/polarity. But object-identity-distinctness is a weaker claim than metric-orthogonality. Two genuinely distinct, individuated objects can still be "close" (non-orthogonal) in whatever pairing structure is built on top of them; distinct labels do not by themselves force a zero inner product. This is exactly Paper_004's own diagnosis (§3.4: "P07 distinguishes channels but does not force orthogonality"), confirmed here independently rather than just repeated.

**Route 3 — P11 phase randomization.** P11 randomizes the phases of *unselected* channels at a *commitment* event — a post-selection, dynamical fact. The inner product is supposed to be a kinematic object (describing states *before* commitment, per U2 Memo 03's own kinematic/dynamic separation argument, which is one of the few pieces of that arc that survives scrutiny on its own terms). A dynamical, post-commitment fact doesn't naturally constrain a pre-commitment kinematic structure. This route doesn't obviously fail so much as apply to the wrong layer.

**All three routes fail or fall short. This matches Paper_004's own honest verdict — independently re-derived here, not just cited.**

**The reframe.** Pushing further: is "prove $\langle K|L \rangle = 0$" even the right question? If the "motif algebra" (Paper_007's pre-completion vector space) is *constructed* as the free vector space over the channel index set — formal linear combinations $\sum_K P_K |K\rangle$ with $\{|K\rangle\}$ declared a formal basis — then $\langle K|L\rangle = \delta_{KL}$ is true **by construction**, the way the standard basis of $\mathbb{R}^n$ is orthonormal by definition, not by theorem. Paper_004's own §3.4 phrasing ("distinct channels *could have* non-trivial overlap, breaking the basis structure") already points at this: the real open question isn't an internal derivation within an already-free vector space, it's **whether the free/orthogonal representation is the physically correct one at all**, versus a representation admitting genuine cross-channel amplitude coupling.

**And the corpus's own other work suggests the answer is regime-dependent, not universal.** The sublinear composition rule born_gleason Memo 02 cites in its own Loophole 1 discussion (`quantum/effective_theory/visibility_to_bandwidth.md`, Fix 6) — $b_{\text{combined}}^2 = b_1^2 + b_2^2 + 2c_{12}b_1b_2$ — carries a **non-zero cross-coherence term $c_{12}$ in general**, vanishing only "under environmental phase-randomization" (i.e., in the same thin-participation regime both born_gleason and U2 already had to restrict to). That is direct evidence, from elsewhere in ED's own corpus, that genuine cross-channel coupling is a real physical possibility in general, and orthogonality is the special case where it happens to vanish — not a primitive-forced universal fact.

**Verdict: P-Channel-Orthogonality — NOT derivable from current primitives by any of the three routes tried. Reframed and sharpened: it is best understood as a regime-conditional approximation (valid where cross-coherence vanishes — the same thin-participation regime the whole Born/Gleason chain already requires), not a universal primitive-level postulate. This is a stronger, more precise negative than "open" — it's an account of *why* it's open and *when* it should be expected to hold anyway.**

---

## 4. Consolidated verdict

| Postulate | Status (this note) | Compare to Paper_004 |
|---|---|---|
| P-Gleason-Compatibility | **Partially DERIVED** (bookkeeping sense, from P02+P04 alone) — physical/measurement-context sense still open | Paper_004: fully open conjecture. This note closes half of it, cleanly, without old-primitive or definitional-fiat dependencies. |
| P-Channel-Orthogonality | **Not derived; reframed as regime-conditional**, expected to hold only where cross-coherence vanishes (thin-participation regime) | Paper_004: fully open conjecture, flags P07 insufficiency correctly. This note confirms that diagnosis independently and adds the regime-conditional account plus the corpus-internal evidence (sublinear composition rule) for why it's the right way to think about the gap. |

**What this note does NOT claim:** a closed proof of either postulate; a fix to Paper_004 itself (not edited here); resolution of the physical/Kochen-Specker-flavored non-contextuality question; a demonstration that the thin-participation regime is where real physical systems actually sit (that's an separate empirical/regime question, addressed elsewhere in the corpus's Q-Compute and decoherence arcs, not here).

**What would come next, if pursued:** (a) attempt the physical (measurement-context) half of P-Gleason-Compatibility directly — likely needs P11's environmental/commitment machinery, engaged honestly rather than by definitional fiat; (b) formalize the regime-conditional account of P-Channel-Orthogonality as an actual bound (how does $c_{12}$ scale with departure from thin-participation, and does it vanish fast enough to protect the downstream QM-kinematics chain in the regimes ED already claims recovers standard QM); (c) decide whether Paper_004 and Paper_007's status rows should be updated to reflect the partial P-Gleason-Compatibility closure found here.

---

*Foundations note. Direct derivation attempt, not a scoping pass. One real, if narrow, positive result (P-Gleason-Compatibility, bookkeeping sense); one sharpened, better-understood negative (P-Channel-Orthogonality, reframed as regime-conditional). Neither Paper_004 nor Paper_007 edited; this is working material for whoever picks up the corpus-facing writeup.*
