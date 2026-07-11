# §4 — Quantum Mechanics from the Substrate: the arrow selects the pointer basis

*Draft v1, 2026-07-10. Register: peer-facing (sympathetic physicist). Tier: **reconstruction** (Gate 1 substantially grounded; not a closed theorem). Point-toward, not re-derive. Primary source: `Paper_QuantumLogicKeystone_GleasonReconstruction` (the per-axiom Piron–Solèr map); postulate reconstructed: `Paper_004`; amplitude: `Paper_001`. Ledger/target: #8b (`project_pchannel_orthogonality_target`, `ED_Research_Targets.md`). This is the arrow's first job worked in depth; §6 will identify it with gravity's.*

---

**The arrow's job here.** Of the roles set out in §3, this section cashes two: the arrow as the quantum **pointer basis** (einselection) and as the source of measurement **repeatability** (the covering law). The claim is not that ED is *compatible* with quantum mechanics. It is that quantum mechanics' most under-explained structural facts, why outcomes are definite in one basis and not another, and why measurement is repeatable at all, are what a one-way commitment *is*.

## The postulate that would not ground

ED's quantum kinematics (Paper_004) rests on an inner product over the substrate states. In a substrate ontology that cannot simply be assumed; it must trace to the primitives or be flagged as postulated. Two assumptions had blocked three prior attempts: that distinct channels are orthogonal, and that the probability assignment is the Gleason/Born one. The obstruction was always the same shape. Orthogonality was sought as a *metric* fact about vectors, and no ED primitive delivers a metric.

The reconstruction breaks the stall by changing the question, from "are the channel vectors orthogonal?" to "what does the substrate operationally do, and what representation must carry that?" The target is the standard quantum-logic chain: **Piron** (an irreducible, complete, atomistic, orthomodular lattice with the covering law, rank ≥ 4, is the lattice of closed subspaces of a Hermitian space over a division ring with involution), then **Solèr** (an infinite orthonormal sequence of equal norm forces the field into `{ℝ, ℂ, ℍ}` and the space to be a genuine Hilbert space), then a physics input to select the field. ED's lattice is the set of propositions "the commitment resolves in channel-set `S`" — the P11 outcomes. The reconstruction maps each axiom to a primitive, with an explicit tier.

## Three results

**1. Orthogonality reduces to distinguishability.** Take candidate channel-states with a *tunable* overlap `c = ⟨K|L⟩` (do not set `c = 0`). The best confusion-free detection of `K`, maximizing `⟨K|E|K⟩` over POVM elements subject to `⟨L|E|L⟩ = 0`, is the projector onto the complement of `|L⟩`:
$$\max \langle K|E|K\rangle = 1 - c^2,$$
which equals 1 iff `c = 0`. Perfect distinguishability ⟺ orthogonality. And ED's channels *are* perfectly distinguishable from commitment frequencies alone (a pure channel-`L` state has `b_K = 0`, so it commits to `K` with frequency zero, P07). So `⟨K|L⟩ = 0` is not an independent postulate; it is what "perfectly distinguishable by commitment" means. The honest boundary: step (B) is proven *inside* the inner-product representation, so this reduces orthogonality to distinguishability *given* that the representation exists — it does not build the metric from primitives.

**2. The complex field is selected.** Solèr allows `{ℝ, ℂ, ℍ}`; ED picks ℂ by two standard discriminators, each grounded in a primitive. ℝ is excluded not because a real space cannot carry a phase (it can, via a Stueckelberg `J`), but because a real division ring supplies no *central scalar* square root of `−1`; ED's phase `e^{iπ}` is a scalar amplitude factor (Paper_001), not an operator constrained to commute with all observables, so the field must contain `i`. ℍ is excluded by the standard tensor-product obstruction: composite systems (the V5 cross-chain joint amplitudes, Paper_063) need a commutative field for `⊗` to be well-defined. This is a *selection* from Solèr's menu, account-tier, not a from-scratch derivation, but it means ℂ is no longer a bare assumption.

**3. The covering law: irreversibility enforces it.** The covering law's operational content is the ideal first-kind measurement, measure an atom, get "yes," project, and get "yes" again on repetition. The natural worry is that P11's irreversibility *breaks* the repeatability this needs. It is exactly backwards. Commitment projects the state onto the resolved channel-atom (orthogonally, by P11 exclusivity), and then *locks* it: an irreversible outcome cannot drift, so re-measurement returns the same channel with certainty. **A committed channel is the most repeatable outcome there is.** Irreversibility is not an obstruction to the covering law; it is what supplies it. (Honest scope: this grounds the first-kind core on the *channel* basis; the full lattice-geometric exchange condition and the phase basis remain residual.)

## The two arrow-tied resolutions

Two structural questions that other accounts install by hand resolve here directly from the arrow, and they are ED's distinctive quantum picture.

**Einselection is primitive.** P11 is the only collapse primitive, and it is a *which-channel* selection. A superposition `|+⟩ = (|1⟩ + |2⟩)/√2` is not an intrinsic channel; no primitive collapses to it; committing a `|+⟩` state resolves it to `|1⟩` or `|2⟩`, never to `|+⟩`. So the channel basis is the unique pointer basis, selected by the arrow, not emergent from environmental decoherence. Phase stays a genuine coherence observable (interference is real; a definite phase and a definite channel are complementary), but it is never a commitment basis. **ED is a preferred-basis quantum theory because it is a committing theory.** Ordinary basis-democracy is recovered at the apparatus level (an apparatus is a system whose channels couple to the target observable), so standard QM emerges; the distinctive claim is that einselection is fundamental rather than derived.

**Born probabilities are non-contextual.** The bandwidth `b_K` is intrinsic (P04, a bare state property with no apparatus argument), so `P(K) = b_K / Σb` is fixed. Because ED commits only in the channel basis, there is exactly *one* substrate commitment context, and Kochen–Specker contextuality (which needs one projector sitting in multiple incompatible contexts) has nowhere to arise. ED assigns non-contextual *probabilities* (Gleason-permitted, the Born rule), never non-contextual definite *values* (Kochen–Specker-forbidden), because outcomes are stochastically committed, not pre-valued. It is consistent with both theorems at once.

## Honest status

This is a **coherent reconstruction, not a closed theorem** — and stating that plainly is what keeps it credible. Precisely:
- Orthogonality is *reduced* (to distinguishability, given the representation), not produced from primitives; ℂ is *selected*, not derived; the covering law is *candidate-grounded* on the channel basis only.
- The residual is **Solèr lattice rigor**, and it is a *different kind of thing* from ED's structural opens (§13). The postulate that actually stalled three prior attempts — channel-orthogonality — is **discharged and circularity-audited** (2026-07-08, 2026-07-10), not open. What remains is a rigor-completion: mostly the standard Piron–Solèr machinery (which ED *invokes*, not owes — it sits on the "inherited by design" list alongside Clifford algebra and the lattice-gauge dictionary), plus one genuinely ED-side soft spot named precisely — whether the primitives establish the *full orthomodular identity metric-free* (they give non-distributivity outright; the full identity is the tightest open screw). This is why the box is checked at the tier the word carries: **reconstructed** — substantially grounded by mapping onto a standard theorem, not proven from scratch, and not a missing physics result of the #1/#3 class.
- ED's quantum *logic* (the orthomodular lattice, the covering law) is substrate-exact; its quantum *geometry* (the inner-product metric) is Born-statistical and therefore emergent. The Hilbert space is exact-as-logic, emergent-as-metric.
- The equal-norm (angle) condition, flagged as a circularity in earlier drafts, was discharged operationally in 2026-07-10: in the amplitude representation `⟨K|K⟩ = b_K`, so equal-norm ⟺ equal-bandwidth, forced by P03 homogeneity.

What is new and solid, independent of the residual rigor, is the **reframe**: orthogonality is operational rather than metric, the complex field is selected by ED's actual phase and composites, and the arrow selects the pointer basis.

## What this buys §6

Note what did the work in every result above: the *irreversibility* of commitment. It locked the channel to give repeatability; it made the channel basis the unique pointer basis; it made outcomes stochastic commitments rather than pre-valued facts. That irreversibility is the arrow of §3. Hold onto the specific identification, **the arrow selects the quantum pointer basis** — because §5 will show the same arrow fixes gravity's preferred time, and §6 will argue those are not two facts.

---

*Draft notes for finalization:*
- *Tier discipline: every result stated at the keystone paper's tier (reduced / selected / candidate-grounded / rigor-residual). Do not upgrade "reconstruction" to "derivation" anywhere. But do NOT over-flag either: this box is a ✅ (reconstructed), NOT a ⚠️ structural open — the Solèr residual is a rigor-completion of an inherited theorem + one lattice-identity soft spot, different in kind from #1/#3. The blocking orthogonality postulate is discharged/audited (target doc #8b), not open. The honesty lives in the tier word "reconstructed," not in demoting the box.*
- *Length ~1150 words (shorter than §3, per the budget). Trim the three-results block first if the report wants it tighter; the arrow-tie and honest-status blocks are load-bearing, keep them.*
- *Cross-check the einselection framing against §7 (chirality) and §3's role table so "the arrow selects the pointer basis" reads identically in all three.*
- *Register OK: Piron/Solèr/POVM/Gleason/Kochen–Specker/einselection named flat-out, no popular-science scaffolding.*
