# Anomaly Cancellation in ED — Scoping via Spectral Flow

**Status:** Scoping memo, 2026-07-05. Anomaly cancellation is named "untouched" and "the deepest consistency requirement of a chiral gauge theory" in `Paper_MS-II` (preamble 3) and `ED_Program_Review` (§5, line 173). This memo does **not** derive it. It makes one conceptual connection the corpus has not drawn — that ED's chirality mechanism and the chiral anomaly are the same object — and from there tiers exactly what ED could contribute (a consistency *constraint*) versus what stays a wall (the fermion *content*). Given the discipline: nothing here is claimed as derived; the load-bearing physics identities are standard and cited to their ED source, and the one honest obstruction is named.

## The connection the corpus has not made

Two corpus results are treated as separate. They are two faces of one object.

- **Chirality (MS-II §4.2, *account*).** ED's chirality is located in the arrow's non-Hermitian retarded transport, which "carries a net **point-gap winding / spectral-flow** (a chiral signature absent in the hermitian case), located as a channel-topology class." The Program Review §5 adds that this is exactly how ED evades the **Nielsen–Ninomiya** no-go: N-N's premises (a rigid periodic lattice and a *hermitian* rule) do not bind ED, because the arrow (P11) makes the rule non-hermitian.
- **Anomaly cancellation (MS-II, Program Review §5, *untouched*).** Named as the hardest open consistency requirement, not addressed.

**These are the same physics.** In standard field theory the chiral anomaly *is* spectral flow: the axial-current divergence equals the index of the Dirac operator (Atiyah–Singer), and the domain-wall / Callan–Harvey picture realizes the anomaly as spectral flow across the mass defect. Non-Hermitian **point-gap winding** is the modern topological invariant that counts exactly this flow. So the very object MS-II §4.2 uses to *source* ED's chirality — the net point-gap winding of the retarded transport — is, in standard terms, the **anomaly**. ED has not been missing the anomaly; it has been calling it "chirality" and not connecting the two.

**Consequence for framing.** "Anomaly cancellation" in ED is not a missing add-on to be built. It is a question about an object ED already has: *does the net gauged spectral flow — the point-gap winding summed over the channels of a P05 polarity-transport group — vanish?* That is the ED translation of the anomaly-cancellation condition.

## The two faces, and what ED already realizes of each

The chiral gauge anomaly is the statement that the gauge current fails to be conserved: a non-zero anomaly means D·J ≠ 0, which breaks gauge invariance (loss of unitarity/renormalizability). Anomaly-*freedom* is therefore equivalent to **exact conservation of the gauge current** — an exact Gauss law. ED has partial structural realizations of *both* faces:

1. **The flow face (chirality):** the retarded-transport spectral flow (MS-II §4.2). Present wherever ED has chirality.
2. **The conservation face (charge):** `Paper_ChargeAsTopology_B4` establishes, **measured to machine precision**, a quantized winding `w ∈ ℤ` (π₁(U(1))=ℤ) and an **exact integral Gauss law** (circulation = 2πw, loop-independent). An exact Gauss law is exact gauge-charge conservation — the substrate-level statement of anomaly-freedom.

So the anomaly-cancellation question in ED sharpens to a single relation between two things ED already has:

> **Does the arrow's chiral spectral flow (face 1) preserve or violate B4's exact gauge-charge conservation (face 2)?**

If the exact Gauss law survives in the presence of the chiral spectral flow, then the substrate **forbids a gauge anomaly by construction** — anomaly-freedom is *forced* as a consistency requirement on whatever channel-content emerges. That would be ED's honest contribution to the anomaly question, and it is exactly ED's characteristic move: force a *constraint*, not a *value*.

## Honest tiering

- **Reframing (solid, not a new ED result):** anomaly = the §4.2 spectral flow, gauged; anomaly-freedom = B4's exact Gauss law. Both are standard-physics identities applied to existing ED results. This is the contribution — a connection, not a derivation.
- **"ED forces anomaly-freedom" (CANDIDATE, conditional, blocked):** the argument above *would* make anomaly-freedom a substrate-forced constraint, but it is **not closed**, for a concrete reason (next section). Do not state it as established.
- **The fermion content (WALL, untouched):** even a fully closed constraint says only "the emergent content must be anomaly-free." It does **not** give the specific representation spectrum / hypercharges that realize cancellation — that is downstream of the open channel-topology → representation-spectrum classification (MS-II §4.4, §92), which is untouched. ED would force *that* the content is anomaly-free, never *which* content. Same wall as the representation spectrum. (In the SM, anomaly cancellation ties quark×3-color to lepton hypercharges and forces charge quantization; ED already has the exact-charge-quantization side via B4, but not the content that the SM cancellation relates.)

## The obstruction (why this is analytic, not a certified-simulator build)

B4 states plainly that the winding is **inert under the certified rule**: because the Σ-selection is orientation/phase-blind, the winding "has no dynamical effect at the Σ level; it couples only weakly, through the P04 bandwidth channel. It is a conserved topological invariant, not a dynamically active charge." That is the **same gauge-sector Σ-blindness** that blocked the H1 gauge-mass probe (`theory/Higgs_Emergence/H1_Leg_Scoping.md`): the phase/polarity/gauge sector (P05, P09) is invisible to the certified Σ dynamics.

So the interaction between the chiral spectral flow (face 1) and the gauge-charge conservation (face 2) is **not dynamically realized in the certified simulator** — the anomaly lives in the Σ-blind sector. This means:

- The anomaly-cancellation question is **not runnable on the certified commit-simulator**; it is an analytic question about the **V1 retarded kernel** (`Paper_089`) and the **P05 polarity-transport** structure, not the Σ-commit dynamics.
- The recurring theme (Higgs mass, now the anomaly): ED's gauge/phase sector is the part the certified substrate does not dynamically resolve. Grounding either would require the gauge sector to be dynamically active, which the reference rule makes it not.

## Candidate next steps (analytic, correctly scoped)

1. **Compute the point-gap spectral winding of the V1 retarded kernel** (`Paper_089`) for a single channel, and confirm it is a genuine spectral-flow invariant (the anomaly), non-zero for the chiral (non-hermitian) case and zero for the hermitian case — grounding MS-II §4.2's "point-gap winding" claim as an actual computed invariant rather than an asserted one. This is the one concrete, bounded, analytic probe; it does not need the fermion content.
2. **Test whether B4's exact Gauss law is stable under the retarded (non-hermitian) transport.** If the exact integral Gauss law survives when the winding sector is made dynamically active (a modified rule where P05/P09 are not Σ-blind), that is direct evidence the substrate forbids a gauge anomaly. This needs a gauge-sector-active substrate variant — the same missing ingredient as the Higgs work, so it should be scoped jointly, not bolted on.
3. **Do not attempt the fermion content.** It is downstream of the open representation spectrum; anomaly cancellation cannot be closed at the content level before that is.

## Bottom line

ED's chirality *is* the anomaly — the arrow's non-Hermitian spectral flow — and ED already realizes the exact-gauge-charge-conservation (anomaly-free) side via B4's exact Gauss law. The honest open question is whether these two survive together (chiral flow + exact conservation), which would make anomaly-freedom a substrate-forced *constraint*. It is blocked by the same gauge-sector Σ-blindness that blocked the Higgs mass, so it is an analytic question about the V1 kernel and P05 transport, not a certified-simulator build. And it forces at most a constraint: the fermion *content* that realizes cancellation stays a wall, downstream of the untouched representation spectrum. This reframes "anomaly cancellation, untouched" into "anomaly = a spectral-flow object ED already has, whose consistency with exact charge conservation is the real, bounded, analytic open question."
