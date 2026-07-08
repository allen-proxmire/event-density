# T4_04 — Attack on the emergent-spinor gate: the discriminator hinges on spin-gauge coupling in P05

**Opened 2026-07-08** at AP's direction ("let's do T4"). Crank-rail ON. This is the matter-sector keystone: chirality's relativistic descent AND anomaly cancellation both reduce to T4. Builds on T4_01/02/03, the ChiralGauge SQ1 series (esp. SQ1g), and Gauge_01/02. Default prior stated up front: **vector; a chiral result must be earned.**

## Where T4 stands (state map, 2026-07-08)

Tier ladder (from a full read of T4_01/02/03, Paper_RQM_T2/T4, SQ1e/g/j):
- **Cl(3,1) algebra + 4-spinor irrep:** IMPORTED. D=3+1 (P06) + acoustic-metric signature (Paper_017) selects Cl(3,1) "by definition"; the 4-dim irrep is standard Clifford math (Pauli/Schur, `I` rows). Paper_RQM_T2 self-downgraded FORM-FORCED → form-IDENTIFIED. Not constructed from substrate d.o.f.
- **Dirac operator:** FORM-IDENTIFIED (unique first-order factorization of Klein-Gordon). The substrate-V1 → Dirac reduction is OPEN (Paper_RQM_T4 §3.7 / audit row 15).
- **P09 → spin: KILLED.** T4_01 §2: a U(1) winds by integers; spin-½ needs the SL(2,ℂ) double cover (Clifford), so P09 is NOT the source of spin/chirality. P09 argued to be a **vector** U(1) (structural, §3).
- **Spin = channel topology:** STRUCTURAL (T4_02); relocates the gap to channel-topology → gauge/spin (P07 §7.4).
- **Double cover (spin-½ from tethering):** ACCOUNT (T4_03; belt-trick/π₁(SO(3))=ℤ₂; the could-say-no is whether P07's graph geometry realizes the SO(3) action with the right π₁).

**The single load-bearing gate (three equivalent faces):** construct the emergent 4-spinor from substrate d.o.f. (P07 channels + P03 loci + directions) and **locate γ⁵** in it (candidate: channel screw-orientation vs the local Cl(3,1) frame, NOT P09). Sharp entry = the SQ1g discriminator.

## The discriminator (SQ1g) and the crux, sharpened against Gauge_02

**Discriminator:** the emergent fermion couples to the P09 U(1) field either the same for both handednesses (vector, parity-conserving) or differently (chiral, γ⁵, parity-violating). The single deciding number is `advance(L) − advance(R)` = the P09 phase-advance of a left- vs right-helicity mode under P05 transport one commitment-step along the arrow. Zero ⇒ vector; nonzero ⇒ chiral. Helicity = sign of `spin·(arrow-direction)`, so this hinges on **one property of P05: is its phase-transport spin-arrow-coupled or spin-blind?**

**Sharpened against the actual P05 definition (Gauge_02, read 2026-07-08).** Gauge_02 derives P05 transport as a U(N) link variable `ψ(u') = U_{uu'} ψ(u)`, `U ∈ U(N)`, from three facts: P04 (bandwidth conservation → isometry), P07 (channel re-routing → mixing), P11 (invertible between commitments → unitary). **None of the three references spin or helicity.** So the gauge-fiber transport, as derived, is **spin-blind → the default is VECTOR** (consistent with SQ1g's stated prior and standard minimal coupling).

**But the chiral channel is structurally open, not closed off.** Gauge_02 §4 states the load-bearing structural fact: the gauge sector (U(N) from channel *multiplicity*) and the fermion sector (spinor = channel *topology*, T4_02) are the **same lattice gauge theory** — both carried by the **same channels**, transported by the **same P05**. Therefore:

> **The discriminator reduces to: does the single P05 transport map `U_{uu'}` act REDUCIBLY as (spin-frame transport) ⊗ (independent U(1) phase advance) [⇒ vector], or IRREDUCIBLY, so that the U(1) phase-advance depends on the spin-frame's orientation relative to the arrow [⇒ chiral]?**

Because spin and the U(1) phase ride the same P05-transported channels, the coupling is *possible* (nothing in the U(N) construction forbids a spin-dependent generator). Its *presence* is decided by the emergent-spinor construction: specifically, **is the P07 channel re-routing that defines `U_{uu'}` helicity-handed** — does it depend on the traversal direction relative to the channel-topology screw (T4_02 §3's γ⁵ candidate)? If the re-routing is fixed by the channel graph alone (traversal-direction-independent) → reducible → vector. If it depends on the screw sense vs the arrow → irreducible → chiral, and the screw IS γ⁵.

**Net:** the crux is real, well-posed, and bottoms out on the SAME unbuilt object as the whole gate: the discrete emergent spinor. It cannot be answered by reading; it requires building the spinor carefully enough that the P05 map's action on it can be read off as reducible or not. Honest default remains **vector** until a specific helicity-handed feature of the P07 re-routing is exhibited.

## Concrete next step (SQ1g step 1 — the gate, research-grade analytic construction)

Build the minimal **discrete emergent Weyl mode on the directed participation graph**: the two-component object that HAS a helicity (spin·arrow), from the channel-topology construction (T4_02 spin-as-topology + T4_03 tether double cover). Carry the spin-frame and the P09 U(1) phase on the SAME channels (per Gauge_02 §4). Then:
1. Apply P05's transport `U_{uu'}` (the Gauge_02 U(N) link map) to an aligned (L) and an anti-aligned (R) mode, one commitment-step along the arrow.
2. Read off each mode's P09 phase-advance; compute `advance(L) − advance(R)`.
3. Zero ⇒ vector (screw route fails; fall back: is parity violation then spontaneous / IC-selected?). Nonzero ⇒ chiral (γ⁵ real; the screw is the mechanism). If chiral, check maximality (SQ1d predicts pure V−A).

**Substrate note:** this is NOT runnable on the certified Σ-commit simulator (the gauge/phase sector is Σ-blind, the same obstruction as the H1 Higgs and the anomaly). It is an analytic construction on the directed participation graph (channels + loci + directions), possibly with a small hand-built directed-graph model of the channel-topology screw to make the reducible-vs-irreducible question concrete. The existing `evaluation/ChiralGauge/chiral_3p1d.py` (undoubling 16→1) is prior art but SQ1e §5 is explicit it cannot settle chiral-vs-vector; the spinor construction is the real work.

**Crank rail.** Default vector. Do not assert chiral. The construction either exhibits a helicity-handed re-routing (earning chiral) or it does not (vector, and parity violation must then be sought as spontaneous/IC — a real fallback, not a failure). Either outcome is a genuine result: a *derived* vector-vs-chiral verdict for ED's emergent fermion, which is the matter-sector's sharpest open question.
