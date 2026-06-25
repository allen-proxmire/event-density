# T4 · Step 1 — Spin Is Clifford, P09 Is (a) Vector U(1): Pinning the Open Chain and a First Result

**Foundations — first step of the T4 substrate→Dirac derivation (Paper_106 §3.7, OPEN; the gate #2b reduced to). Reads Paper_103 (T2, Cl(3,1)) + Paper_106 (T4, Dirac form) and identifies the precise unbuilt piece: how the U(1) P09 polarity relates to the Cl(3,1) spinor's spin/chirality. First result: the spin-½ / double-cover / chirality structure is a *Cl(3,1)* feature (T2), not a P09 feature — a U(1) winds by integers, spin-½ needs the SL(2,ℂ) double cover the Clifford algebra supplies. So the #2b "P09↔spin" question sharpens to: *does P09 act as a vector U(1) (e^{iθ}, chirality-blind) or an axial U(1) (e^{iθγ⁵}, chirality-distinguishing)?* A structural argument gives **vector**: P09's transport-advance is tied to the arrow (the γ⁰/time direction) → a temporal vector coupling → P09 is electromagnetism-like, blind to chirality (consistent with SQ1i's V1=vector=EM). Consequence for #2b: chirality is Clifford-based and P09 (vector) is independent of it at the transport level, so the C-lock (P09/χ_C) and P-lock (Clifford helicity) are *distinct by default* — leaning toward two separate locks, with V5 the only candidate tie.**

---

## 1. What's established (T2 + T4) and what's not

- **T2 (Paper_103, M1):** the substrate's local frame is Cl(3,1) (signature from P06 + Paper_017 acoustic metric); Cl(3,1) has a unique 4-component irreducible representation = the Dirac spinor, up to similarity. So spinor rule-types carry 4-component amplitudes Ψ.
- **T4 (Paper_106, M2):** given that 4-component spinor, the Dirac operator `iγ^μ∂_μ − mc/ℏ` is the unique first-order factorization of Klein–Gordon. Form established.
- **Not built (the open chain, §3.7):** how the substrate *graph* (loci P02/P03, channels P07, U(1) polarities P09, V1 transport, P05 connection) actually realizes the 4-component spinor — and, the part both papers only *gesture* at, **how P09 sits inside that spinor.** T2 §2.1 says P09 "supplies the angular structure that polarity rotation propagates onto gamma-matrices"; T4 §2.1 says P09 is "the phase target." Neither develops it. That gesture is the #2b gate.

## 2. First result: the spin is Clifford, not P09

A clean, decisive observation cuts the problem:

> **P09 is a U(1). A U(1) phase winds by integer amounts (2π → e^{2πi} = 1). Spin-½ requires the double cover — a 2π rotation must give −1 — which is the Spin(3,1) = SL(2,ℂ) structure, i.e. the *Clifford* algebra of T2.**

So the spinor's half-integer / double-cover nature — and therefore its chirality (γ⁵ = iγ⁰γ¹γ²γ³ is a *Clifford* element) — **comes from Cl(3,1) (T2), not from P09.** P09 cannot be the source of the spin or the handedness; those are Clifford-structural. This is why T2's gesture ("P09 propagates onto the gamma-matrices") was never built: P09 doesn't *generate* the spin structure, it *sits on top of* it.

This re-poses the #2b gate crisply. There are exactly two U(1)s that can act on a Dirac spinor:

- **vector** `Ψ → e^{iθ}Ψ` — same phase on left and right components, chirality-blind (this is electromagnetism / the conserved vector current);
- **axial** `Ψ → e^{iθγ⁵}Ψ` — opposite phase on left and right, chirality-distinguishing (the chiral rotation).

**The #2b question is exactly: which one is P09?** Vector ⇒ P09 is blind to handedness; axial ⇒ P09 distinguishes handedness and is tied to parity.

## 3. A structural argument: P09 is a vector U(1)

How does P09 act? Its phase advances under transport — P05 carries the polarity phase along edges, and V1 propagates the chain along the arrow (the kernel-arrow / time direction). So P09's advance is **tied to the propagation/arrow direction** — the timelike `γ⁰` direction.

A phase coupling carried by the timelike direction is the *temporal component of a vector coupling* (`ψ̄γ⁰ψ A₀`, the charge-density coupling) — it is **vector, not axial.** (This is the same point SQ1g flagged: "timelike phase alone = temporal vector coupling; γ⁰ is necessary but not sufficient for γ⁵.") For P09 to act *axially*, its advance would have to couple through `γ⁵` itself — i.e., depend on the chirality, which is the full `γ⁰γ¹γ²γ³` Clifford orientation, not just the arrow.

So, structurally: **P09's basic (V1/P05-transport) action is a vector U(1) — electromagnetism-like, chirality-blind.** This dovetails exactly with the kernel picture from SQ1i: **V1 transport couples P09 vectorially (chirality-blind = EM); V5 couples to P09 phase *differences* chirality-sensitively (weak).** P09 is one U(1); its vector face is what V1/EM sees, and the chirality-sensitivity is V5's doing, not an axial character of P09 itself.

## 4. Consequence for #2b (and a partial walk-back of the optimistic lean)

If the spinor's chirality is **Clifford-based** (T2) and P09 is a **vector** U(1) independent of it at the transport level, then:

- The **C-lock** (baryogenesis χ_C — a P09 phase structure, R4) and the **P-lock** (parity / helicity — a Cl(3,1) spin structure) are **distinct objects by default.** Selecting a P09 phase (first-arrival χ*) does not, by itself, select a Clifford handedness.
- So the SQ1j "one event, two projections" hope leans toward **no** — C and P look like *two separate locks*, not one — *unless* something ties the vector-P09 phase to the Clifford chirality.
- The only candidate tie is **V5**: it is the kernel that correlates chains in a *chirality-sensitive* way (SQ1i, from R4), so it is the one structure that "sees" both the P09 phase relationship and the Clifford chirality of the chains it couples. Whether V5 *links* them (making the C-lock and P-lock correlated) or merely responds to each separately is the residual.

This is a more conservative reading than SQ1i/SQ1j leaned toward, and it is where the actual T2/T4 structure points: handedness is Clifford; P09 is (vector) electromagnetism; the parity violation rides V5's Clifford-chirality-sensitivity, not an axial P09.

## 5. What this leaves as the next concrete step

The open chain now has a sharp, ordered to-do:

1. **Build the 4 components from substrate d.o.f.** T2 gives the *algebra* (Cl(3,1)) abstractly; it does not construct the 4 spinor components from the graph's actual content (channels P07 + loci + directions). This is the still-inherited part of §3.7 — the genuine substrate→spinor construction.
2. **Locate the Clifford chirality in that construction** — what substrate feature is γ⁵ (the L/R split)? Candidate: the orientation of the chain's participation relative to the local Cl(3,1) frame (the channel/direction structure, P07 + P03), *not* P09.
3. **Determine whether V5 ties P09-phase to Clifford-chirality** (the C/P link, §4) — the residual that decides the unification.

Step 1 is the gate behind all of it: until the 4 components are built from substrate content, "where γ⁵ lives" and "does V5 tie it to P09" can't be closed. That is the real next move.

## 6. Status

**T4 step 1: the spin/chirality structure is Cl(3,1)-based (T2), not P09-based — P09 is, by a structural argument, a vector U(1) (electromagnetism-like, chirality-blind), consistent with the V1=vector=EM picture.** This pins the open §3.7 chain: the unbuilt piece is the substrate construction of the 4 spinor components and the location of the Clifford chirality (γ⁵) in it — *not* a P09↔spin identity, which the integer-vs-half-integer winding rules out. For #2b: chirality is Clifford, P09 is vector, so the C-lock and P-lock are distinct by default, leaning toward two separate locks with V5 as the only candidate tie. Next: build the 4 components from substrate d.o.f. (channels/loci/directions) and find γ⁵ in them. Honest limits: §3's "P09 is vector" is a structural argument, not a closed derivation; the 4-component construction (step 5.1) is still inherited from T2's abstract algebra and is the real unbuilt core.

---

*T4 step 1. T2 (Cl(3,1) 4-spinor, M1) + T4 (Dirac form, M2) leave §3.7 OPEN: the substrate→spinor construction + P09's role. Result: spin-½/double-cover/chirality is Clifford (T2) not P09 — a U(1) winds integer, spin-½ needs the SL(2,ℂ) double cover. So #2b's "P09↔spin" sharpens to: is P09 a vector U(1) (e^{iθ}, chirality-blind) or axial (e^{iθγ⁵}, chirality-distinguishing)? Structural argument ⇒ VECTOR: P09's transport-advance is tied to the arrow/γ⁰ (timelike) → temporal vector coupling (γ⁰ necessary not sufficient for γ⁵). P09 = electromagnetism-like, blind to chirality; matches SQ1i (V1=vector=EM couples P09; V5 chirality-sensitive via phase differences + Clifford structure of chains, not an axial P09). Consequence: chirality is Clifford, P09 is vector ⇒ C-lock (P09/χ_C) and P-lock (Clifford helicity) DISTINCT by default ⇒ leans toward TWO separate locks (walks back SQ1j's one-event hope); V5 the only candidate tie. Next: (1) build the 4 spinor components from substrate d.o.f. (P07 channels + P03 loci + directions) — the real unbuilt core, still inherited from T2's abstract algebra; (2) locate γ⁵ in that construction (candidate: chain orientation vs local Cl(3,1) frame, not P09); (3) does V5 tie P09 to Clifford chirality (the C/P link). Honest: P09-is-vector is a structural argument not closed; the 4-component substrate construction is the unbuilt gate behind everything else.*
