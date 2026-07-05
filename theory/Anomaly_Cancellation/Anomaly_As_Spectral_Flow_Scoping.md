# Anomaly Cancellation in ED — Scoping via Spectral Flow

**Status:** Scoping memo, 2026-07-05. **PARTIALLY CORRECTED same day (see banner) after a second-session check.** Anomaly cancellation is named "untouched" and "the deepest consistency requirement of a chiral gauge theory" in `Paper_MS-II` (preamble 3) and `ED_Program_Review` (§5, line 173).

> **⚠️ Correction (2026-07-05).** This memo's central bridge — "ED's chirality *is* the anomaly, via the point-gap winding of the retarded transport" — **rests on a conflation in `Paper_MS-II` §4.2 that I did not verify and should have.** §4.2 asserts the retarded transport carries a "point-gap winding / spectral-flow," treating **"retarded" (one-sided-in-time support, a standard causal boundary condition) as synonymous with "non-Hermitian" in the operator sense** the winding machinery requires. They are not the same: the retarded Green's function of a *Hermitian* Hamiltonian ($G_R = 1/(\omega - H + i0^+)$) is one-sided in time and perfectly standard. **Point-gap winding requires (a) a genuinely non-Hermitian operator (complex spectrum) and (b) a periodic parameter to wind around** (crystal momentum over a Brillouin zone, Hatano–Nelson / Gong-et-al.-type). `Paper_089`'s canonical V1 — $K_{V1} = \theta(t-t')\,G(\sigma/\ell_{ED}^2)$, a real bounded scalar of the invariant separation — has **neither**. So the "V1 point-gap winding" computation this memo proposed asks for an object that does not exist in the source: the full stand-in trap. **What changes:** §"the connection" and the "flow face" below are DEMOTED from *reframing* to *conjectural, and resting on an unconstructed §4.2 claim*. The **B4 conservation face survives** (it is a real measured result and does not depend on the winding). The corrected next step is a definitions/literature check, not a V1 build (see §"Candidate next steps"). Credit: the catch is the second session's.

This memo does **not** derive anomaly cancellation. It tiers what ED could contribute (a consistency *constraint*) versus what stays a wall (the fermion *content*), and — post-correction — flags the load-bearing gap in the chirality mechanism it leaned on.

## The connection the corpus has not made

Two corpus results are treated as separate. They are two faces of one object.

- **Chirality (MS-II §4.2, *account*).** ED's chirality is located in the arrow's non-Hermitian retarded transport, which "carries a net **point-gap winding / spectral-flow** (a chiral signature absent in the hermitian case), located as a channel-topology class." The Program Review §5 adds that this is exactly how ED evades the **Nielsen–Ninomiya** no-go: N-N's premises (a rigid periodic lattice and a *hermitian* rule) do not bind ED, because the arrow (P11) makes the rule non-hermitian.
- **Anomaly cancellation (MS-II, Program Review §5, *untouched*).** Named as the hardest open consistency requirement, not addressed.

**The general identity is standard; ED's realization of it is NOT established (corrected).** In standard field theory the chiral anomaly *is* spectral flow: the axial-current divergence equals the index of the Dirac operator (Atiyah–Singer), and the domain-wall / Callan–Harvey picture realizes the anomaly as spectral flow across the mass defect. That much is textbook. **But note even here two distinct objects get run together:** *spectral flow* is an Atiyah–Patodi–Singer invariant of a **Hermitian** operator family; *point-gap winding* is a **non-Hermitian** invariant. They are related but not identical, and MS-II §4.2 (and this memo's first draft) treated "point-gap winding / spectral-flow" as one thing. **The ED-specific bridge — "the retarded transport's point-gap winding is the anomaly" — is therefore conjectural, not a reframing:** it rests on §4.2's assertion that the retarded transport is a non-Hermitian operator with a computable winding, which §4.2 does not construct and which V1's canonical definition cannot support (see the ⚠️ banner). *What remains genuinely plausible:* ED's irreversibility (P11) is a real time-reversal-breaking ingredient, and irreversible/dissipative dynamics **can** carry an effective non-Hermitian operator (Lindblad / decay-term effective Hamiltonians). So a real non-Hermitian ED operator may well exist — but it is **not V1**, and no source exhibits it or its periodic parameter. The honest state: chirality-as-spectral-flow is a plausible *conjecture* awaiting the actual operator, not an established identification.

**Consequence for framing.** "Anomaly cancellation" in ED is not a missing add-on to be built. It is a question about an object ED already has: *does the net gauged spectral flow — the point-gap winding summed over the channels of a P05 polarity-transport group — vanish?* That is the ED translation of the anomaly-cancellation condition.

## The two faces, and what ED already realizes of each

The chiral gauge anomaly is the statement that the gauge current fails to be conserved: a non-zero anomaly means D·J ≠ 0, which breaks gauge invariance (loss of unitarity/renormalizability). Anomaly-*freedom* is therefore equivalent to **exact conservation of the gauge current** — an exact Gauss law. ED has partial structural realizations of *both* faces:

1. **The flow face (chirality):** the retarded-transport spectral flow (MS-II §4.2). Present wherever ED has chirality.
2. **The conservation face (charge):** `Paper_ChargeAsTopology_B4` establishes, **measured to machine precision**, a quantized winding `w ∈ ℤ` (π₁(U(1))=ℤ) and an **exact integral Gauss law** (circulation = 2πw, loop-independent). An exact Gauss law is exact gauge-charge conservation — the substrate-level statement of anomaly-freedom.

So the anomaly-cancellation question in ED sharpens to a single relation between two things ED already has:

> **Does the arrow's chiral spectral flow (face 1) preserve or violate B4's exact gauge-charge conservation (face 2)?**

If the exact Gauss law survives in the presence of the chiral spectral flow, then the substrate **forbids a gauge anomaly by construction** — anomaly-freedom is *forced* as a consistency requirement on whatever channel-content emerges. That would be ED's honest contribution to the anomaly question, and it is exactly ED's characteristic move: force a *constraint*, not a *value*.

## Honest tiering

- **Reframing — SPLIT after correction.** The *anomaly-free = exact Gauss law* half is solid (standard identity + B4's measured result). The *anomaly = §4.2 spectral flow* half is **conjectural, not solid**: it rests on §4.2's unconstructed "point-gap winding" and its retarded/non-Hermitian conflation (⚠️ banner). Do not cite the chirality-is-the-anomaly bridge as established.
- **"ED forces anomaly-freedom" (CANDIDATE, conditional, blocked):** the argument above *would* make anomaly-freedom a substrate-forced constraint, but it is **not closed**, for a concrete reason (next section). Do not state it as established.
- **The fermion content (WALL, untouched):** even a fully closed constraint says only "the emergent content must be anomaly-free." It does **not** give the specific representation spectrum / hypercharges that realize cancellation — that is downstream of the open channel-topology → representation-spectrum classification (MS-II §4.4, §92), which is untouched. ED would force *that* the content is anomaly-free, never *which* content. Same wall as the representation spectrum. (In the SM, anomaly cancellation ties quark×3-color to lepton hypercharges and forces charge quantization; ED already has the exact-charge-quantization side via B4, but not the content that the SM cancellation relates.)

## The obstruction (why this is analytic, not a certified-simulator build)

B4 states plainly that the winding is **inert under the certified rule**: because the Σ-selection is orientation/phase-blind, the winding "has no dynamical effect at the Σ level; it couples only weakly, through the P04 bandwidth channel. It is a conserved topological invariant, not a dynamically active charge." That is the **same gauge-sector Σ-blindness** that blocked the H1 gauge-mass probe (`theory/Higgs_Emergence/H1_Leg_Scoping.md`): the phase/polarity/gauge sector (P05, P09) is invisible to the certified Σ dynamics.

So the interaction between the chiral spectral flow (face 1) and the gauge-charge conservation (face 2) is **not dynamically realized in the certified simulator** — the anomaly lives in the Σ-blind sector. This means:

- The anomaly-cancellation question is **not runnable on the certified commit-simulator**; it is an analytic question about the **V1 retarded kernel** (`Paper_089`) and the **P05 polarity-transport** structure, not the Σ-commit dynamics.
- The recurring theme (Higgs mass, now the anomaly): ED's gauge/phase sector is the part the certified substrate does not dynamically resolve. Grounding either would require the gauge sector to be dynamically active, which the reference rule makes it not.

## Candidate next steps (corrected — definitions first, NOT a V1 build)

1. **Do NOT build the "V1 point-gap winding."** The object does not exist in the source (⚠️ banner): V1 is a real scalar kernel with no non-Hermitian operator and no periodic parameter. Building one would be inventing the operator and the loop — the stand-in trap.
2. **Resolve the prior definitional question first (literature + sources, not a sim).** (a) Confirm from the non-Hermitian-topology literature what point-gap winding actually requires (a non-reciprocal/asymmetric-coupling operator à la Hatano–Nelson, plus a periodic parameter) — and that plain retardation does not supply it. (b) Ask whether ED's irreversibility (P11) yields a *genuine* effective non-Hermitian operator anywhere, and if so **where** — candidates to check are the **V5 cross-chain** structure (`Paper_090`, which is bilocal and could be non-reciprocal) and the **Cl(3,1)/Dirac construction in Arc R**, not V1. Only if a real operator + periodic parameter are exhibited does any "winding = anomaly" computation become well-posed.
3. **Flag the MS-II §4.2 gap upstream.** The chirality mechanism there asserts a "point-gap winding / spectral-flow" without constructing the non-Hermitian operator it needs and conflates "retarded" with "non-Hermitian." MS-II already tiers chirality as an *account*, so this is not a tiering violation — but the mechanism is shakier than "account" suggests, and it should carry the definitional caveat.
4. **The fermion content stays out of reach regardless** — downstream of the open representation spectrum. Anomaly cancellation cannot be closed at the content level before that is.

## Bottom line (corrected)

Two things survive the correction and are worth keeping:
- **The conservation side is solid.** B4's exact integral Gauss law (measured) is exact gauge-charge conservation — the substrate-level statement of anomaly-freedom. This does not depend on any winding claim.
- **The framing question is still the right one:** does whatever chiral structure ED has coexist with that exact conservation? If yes, the substrate forbids a gauge anomaly and anomaly-freedom is a forced *constraint* (never the *content* — that stays a wall downstream of the open representation spectrum).

What does **not** survive: the claim that ED's chirality *is* the anomaly via "the retarded transport's point-gap winding." That leaned on `Paper_MS-II` §4.2, which asserts a non-Hermitian point-gap winding it does not construct, conflating retardation with operator non-Hermiticity; and V1's canonical kernel has neither the operator nor the periodic parameter such a winding needs. The idea is a *plausible conjecture* (irreversibility is a real T-breaking ingredient that could give an effective non-Hermitian operator) awaiting the actual operator — which, if it exists, is not V1. The honest next move is the definitions/sources check in the section above, not a simulator build. Same lesson as the rest of the session: verify that an asserted object is *constructed* before building on it.
