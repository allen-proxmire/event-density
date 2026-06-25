# Gauge Program · Step 1 — SU(N) from Channel Multiplicity: the Non-Abelian Group from N Indistinguishable Channels

**Foundations — step 1 of the channel-topology→gauge program (the matter-sector keystone T4 bottoms out on). Goes beyond T17 (a fiber-bundle vocabulary *rewrite* that postulates U(1) and gets non-abelian structure only "by analogy"). Result: the gauge group of a rule-type family is the **structure group of its channel bundle**, and for a family of **N indistinguishable (same-rule-type) channels** that group is **U(N) = SU(N) × U(1)** — forced by bandwidth conservation (P04) acting on the N-channel amplitude. So **non-abelian SU(N) comes from channel multiplicity (P08)** — the explicit treatment P08 §7.5 flagged as needed, and a real derivation rather than T17's analogy. The abelian/non-abelian split maps exactly onto the #2b V1/V5 split: single-channel transport (V1) gives U(1) (EM); cross-channel mixing (V5) gives SU(N) (non-abelian). The Standard Model's U(1)×SU(2)×SU(3) corresponds to channel-family multiplicities 1, 2, 3. Honest hard parts: why multiplicities {1,2,3} and no others (the uniqueness question, unsolved in standard physics too); the single shared hypercharge U(1); whether P05/V5 transport genuinely realizes the mixing; spin-SU(2) (a frame-bundle object) is separate and deferred.**

---

## 1. The framework: gauge group = structure group of the channel bundle

Assemble the substrate objects into a bundle, grounding T17's named-but-postulated identifications:

- **Base:** the emergent spacetime (the loci of the participation graph, coarse-grained).
- **Fiber at a locus:** the **channel space** — the channels available there. For a given rule-type family, this is the set of that family's channels (P07), each carrying a U(1) P09 phase (P09).
- **Connection:** polarity-transport **P05** — how the channel/phase content at one locus maps to the next along edges (T17 §3.2 names this; here it does the work).
- **Gauge group = structure group = the group of fiber transformations P05-transport can induce while preserving substrate structure** — equivalently, the holonomy group of P05 around loops.

The gauge group is thus *not* postulated (T17) — it is **whatever symmetry the channel fiber has that transport must respect.** So the question "which gauge group?" becomes "what is the symmetry of the channel fiber?"

## 2. The derivation: N indistinguishable channels → U(N)

Consider a rule-type family with **multiplicity N** — N channels of the *same* rule-type available at a locus (P08; channel.md: multiplicity is "usually small," countable). A chain of that rule-type distributes its participation amplitude over the N channels:
$$\psi = (\psi_1, \dots, \psi_N) \in \mathbb{C}^N .$$
(This is the superposition-over-channels of P07 §1/§5: a chain sits across its available same-type channels until commitment.)

Two substrate facts fix the symmetry of this fiber:

1. **The N channels are indistinguishable** (same rule-type — P07's rule-type label is the only invariant; there is no substrate fact distinguishing channel *i* from channel *j* within the family). So any relabeling/mixing among them is a symmetry.
2. **Bandwidth is conserved** (P04: bandwidth is a conserved additive scalar). The total participation `Σ_i |ψ_i|²` is preserved under transport.

The transformations of `ℂ^N` that (1) mix the components and (2) preserve `Σ|ψ_i|²` are exactly the **unitary group U(N)**. Decomposing:
$$U(N) = SU(N) \times U(1) \big/ \mathbb{Z}_N ,$$
the **U(1)** factor is the *common* P09 phase (rotate all channels together — the abelian phase T17 already had), and the **SU(N)** factor is the *traceless* mixing of the N indistinguishable channels.

> **So the non-abelian gauge group SU(N) is the structure group of N indistinguishable same-rule-type channels, forced by bandwidth conservation. Multiplicity (P08) → SU(N).**

This is the explicit content P08 §7.5 flagged ("gauge-group dimension is a multiplicity-count of topology classes — needs explicit treatment") and the derivation T17 §6.1 only gestured at by analogy. The non-abelian-ness is not an analogy: it is the genuine non-commutativity of SU(N) rotations among N degenerate channels.

## 3. Abelian vs non-abelian = single-channel vs cross-channel = V1 vs V5

When is the realized holonomy U(1) (abelian) versus SU(N) (non-abelian)? It depends on whether transport *mixes* the channels or only rotates their common phase:

- **Single-channel transport** (N = 1, or transport that touches one channel's phase): holonomy in **U(1)** → an **abelian** force.
- **Cross-channel transport** (transport that mixes N indistinguishable channels): holonomy in **SU(N)** → a **non-abelian** force.

This is exactly the V1/V5 split from the #2b thread. **V1 is the single-chain kernel** → single-channel phase → **U(1)** → electromagnetism (and it is the *vector*, chirality-blind coupling, T4 step 1). **V5 is the cross-chain kernel** → correlates/mixes distinct channels → **SU(N)** → the non-abelian (weak/strong) forces (and it is the *chirality-sensitive* coupling, SQ1i). The three dichotomies coincide:
$$\text{V1 / V5} \;=\; \text{single-channel / cross-channel} \;=\; \text{U(1) / SU(N)} \;=\; \text{abelian-vector / non-abelian-chiral}.$$
The #2b kernel structure and the gauge-group structure are one thing. V5 being the cross-chain kernel is *why* the non-abelian forces are the ones that can be chiral.

## 4. The Standard-Model correspondence

The framework gives a gauge group per rule-type family, indexed by its multiplicity:

| channel multiplicity N | structure group | SM force |
|---|---|---|
| 1 | U(1) | electromagnetism / hypercharge |
| 2 | SU(2) × U(1) | weak (doublets) |
| 3 | SU(3) × U(1) | strong / color (triplets) |

So **U(1) × SU(2) × SU(3) ↔ channel-family multiplicities {1, 2, 3}.** The SM gauge group is the statement that the substrate's stable rule-type families come in singlets, doublets, and triplets — exactly the representation structure (color triplets, weak doublets, charge singlets) the SM has.

## 5. The honest hard parts

1. **Why multiplicities {1, 2, 3} and no higher?** The framework gives SU(N) for *any* N; it does not yet say why nature stops at 3. This is the deep uniqueness question — and standard physics does *not* answer it either (the SM gauge group is input). A candidate ED constraint: channel-family **stability** (channel.md: multiplicity is "usually small," and §1 stability is rule-compatibility under perturbation) + the **D=3+1** structure (P06) may bound the stable multiplicity — but that is a further sub-derivation, not done here. This is the program's hardest target.
2. **The single shared U(1) (hypercharge).** The SM has *one* U(1), not a U(1) per family. The decomposition `U(N) = SU(N)×U(1)/ℤ_N` gives a U(1) per family; reducing the several U(1)s to the single hypercharge (and the electroweak mixing that ties it to SU(2)) is unbuilt. Real detail.
3. **Does P05/V5 transport actually realize the SU(N) mixing?** §2 shows the channel fiber *has* U(N) symmetry; that it is *gauged* (local, transport-realized) requires P05/V5 transport to genuinely rotate among the N channels position-dependently. The substrate mechanism (does V5 cross-chain correlation implement SU(N) parallel transport?) needs construction — this is step 2.
4. **Spin SU(2) is a different bundle.** The spin double-cover is *also* an SU(2), but it lives on the **frame/spacetime** bundle (rotations of the Cl(3,1) local frame), not the internal channel bundle. It is a separate object (no frame-bundle treatment exists in the corpus, per the map) and is deferred to a later step.

## 6. Status

**Gauge step 1: non-abelian SU(N) is the structure group of N indistinguishable same-rule-type channels, forced by bandwidth conservation (P04) on the N-channel amplitude — a genuine derivation of the gauge-group *form* from channel multiplicity (P08), beyond T17's postulate-and-analogy.** The abelian/non-abelian split is the V1/V5 single/cross-channel split, unifying the gauge structure with the #2b kernel thread. The SM's U(1)×SU(2)×SU(3) is the statement that stable rule-type families are singlets/doublets/triplets. **Open:** why {1,2,3} (the uniqueness question — the hardest, unsolved in standard physics); the single hypercharge U(1); whether P05/V5 gauges the mixing (step 2); spin-SU(2) as a separate frame bundle (later). The framework now exists; the next step is the substrate mechanism (does transport realize the SU(N) connection?) and then the uniqueness constraint.

---

*Gauge program step 1. Framework: gauge group = structure group of the channel bundle (base = loci, fiber = channel space, connection = P05). Derivation: N indistinguishable same-rule-type channels (P08 multiplicity) + bandwidth conservation (P04) on the N-channel amplitude ψ∈ℂ^N → structure group U(N) = SU(N)×U(1)/ℤ_N. Non-abelian SU(N) from multiplicity — explicit treatment of P08 §7.5's flagged-open "gauge multiplicity," beyond T17's analogy. Abelian/non-abelian = single-channel/cross-channel = V1/U(1)/EM / V5/SU(N)/non-abelian-chiral — unifies the gauge structure with the #2b V1/V5 thread (V5 cross-chain = why non-abelian forces can be chiral). SM U(1)×SU(2)×SU(3) ↔ channel-family multiplicities {1,2,3} (singlets/doublets/triplets = SM reps). Hard parts: why {1,2,3} not higher (uniqueness — candidate: channel-family stability + D=3+1 bound; unsolved in standard physics too); single shared hypercharge U(1) (U(N) gives U(1) per family); does P05/V5 actually gauge the mixing (step 2); spin-SU(2) is a separate frame bundle (deferred). Framework built; next = substrate mechanism for the SU(N) connection + the uniqueness constraint.*
