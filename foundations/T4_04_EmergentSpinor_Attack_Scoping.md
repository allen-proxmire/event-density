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

---

## Build 1 (DONE 2026-07-08) — the discriminator is computed and reduces to a single geometric quantity: the SCREW PITCH. Verdict: default VECTOR.

`evaluation/ChiralGauge/t4_spinor_discriminator.py`. Built the minimal emergent Weyl 2-spinor with helicity eigenstates along the arrow (`|L⟩` = spin+arrow, `|R⟩` = spin−arrow), P05 transport as a U(2) link `U = e^{iφ}·V` (φ = P09 U(1) advance, `V ∈ SU(2)` = spin-frame re-routing by angle θ about axis n̂), and computed the SQ1g discriminator `advance(h) = arg⟨h|U|h⟩`. Nothing chiral put in by hand; the frame-rotation axis is scanned, not assumed.

**Result (exact, verified against closed form to machine precision):**
$$\text{advance}(L) - \text{advance}(R) = -2\,\mathrm{atan2}\!\big(\sin(\theta/2)\,n_z,\ \cos(\theta/2)\big),$$
which depends **only on `n_z`**, the component of the frame-rotation *about the arrow* (the screw pitch). Cases:
- **pure translation** (θ=0) or **transverse rotation** (`n_z=0`): discriminator = 0 → **VECTOR**. (Transverse rotation also fails to conserve helicity, `[U,σ_z]≠0` — spin flips, not a clean chiral split.)
- **rotation about the arrow** (`n_z≠0`, a SCREW): discriminator ≠ 0 → **CHIRAL**, and helicity IS conserved (`[U,σ_z]=0`): `|L⟩,|R⟩` are transport eigenstates with different P09 eigen-charges. **The screw pitch is γ⁵.**

**So the entire phase-screw → γ⁵ question reduces to one geometric fact: does P05 transport SCREW the spin-frame about the arrow it advances along?** advance(L)−advance(R) = the frame-rotation-about-the-arrow per step.

**Verdict: default VECTOR (derived-conditional).** The canonical U(N) transport (Gauge_02: an isometry forced by P04+P07+P11) does **not** force a screw — `n_z` is unfixed, and Gauge_02 §6.4 explicitly defers the spin-frame bundle. Geometrically, in 3+1D the arrow is a *time* direction and picks out no *spatial* rotation axis, so there is no forced rotation-about-the-momentum. A screw requires the channel/tether arrangement (T4_03) to be **helical along the arrow**, a handed channel-topology feature the minimal primitives leave as a free degree of freedom (the T4_02/03 "could-say-no"). P09 cannot supply it (P09→spin was killed, T4_01 §2). So the minimal emergent fermion is **vector-like**; chirality is *possible* (`n_z≠0` is not forbidden) but *not forced*.

**Consistency check (important).** This confirms and sharpens SQ1e §2-3's flag that the 3+1D survivor "may default vector-like" and that the 1+1D winding=anomaly (SQ1c) is "dimension-special": in 1+1D the single spatial direction *is* the arrow direction, collapsing the screw distinction, so the arrow gives chirality there; in 3+1D the screw distinction reappears and the arrow alone does not. The pictures cohere.

**Net for T4 / the matter sector.** The chirality gate is now a *single, computed* discriminator = the screw pitch, with a **derived default-VECTOR verdict**: ED's emergent fermion does **not** structurally force the weak force's chirality from the minimal primitives. Parity violation, if ED has it, needs one of: (a) a **helical channel-topology screw** (`n_z≠0`) — an unforced structural input (the remaining could-say-no; determine whether P07's actual graph geometry is handed), or (b) **spontaneous / IC symmetry breaking** (the SQ1g fallback, which connects to baryogenesis's first-arrival handedness). This is consistent with the corpus's already-refuted "commitment-coupled weak-chirality" mechanism: the arrow does not hand chirality to the 3+1D fermion for free.

**Honest scope.** This is the SQ1g discriminator computed on the minimal emergent spinor, reducing chirality to the screw pitch and delivering a derived default-vector verdict, NOT a proof that ED is vector-like (the channel-topology could still be handed). It does not construct the full 4-spinor from P07 channels (the Weyl 2-spinor + its transport suffices for the helicity discriminator); the double-cover/4-component and the rep-spectrum (which topology → which spin) remain as in T4_02/03. Tier: **the reduction (discriminator = screw pitch) is a clean result; the verdict is derived-conditional VECTOR, conditional on the minimal-primitive transport (no forced screw).**

**Next (two forks).** (a) **Determine whether P07's channel-topology is helical** (is there a forced screw?) — the remaining could-say-no; if yes, chiral is earned and maximality (V−A, SQ1d) becomes the check; if no, ED is vector-like and parity violation is fork (b). (b) **Pursue spontaneous/IC parity breaking** via the baryogenesis first-arrival handedness (R4 bridge, `ChiralGauge_SQ1h`), the ED-native route if the topology is not handed.

---

## Fork (a) RESOLVED (2026-07-08) — canonical P07 supplies NO channel-topology, hence no helix; default VECTOR confirmed at the primitive level

Checked canonical **Paper_087 §P07** verbatim (not an elaboration, per the sourcing discipline): *"Channels are structurally distinguishable carriers with intrinsic identities in the participation graph. Two distinct channels at the same locus are substrate-level distinct objects, even if their bandwidth and polarity content happen to coincide. The channel structure is an ontological primitive."* Load-bearing in 025 (channel-counting), 054 (multi-channel), 089/090 (kernels).

**Canonical P07 is a combinatorial distinguishability statement: channels are distinct labeled objects with intrinsic identities. It has NO geometry, NO arrangement, NO topology.** A set of distinguishable labels has no handedness. So the helical screw the discriminator needs (Build 1) is not merely un-forced by P07, it is undefined at the canonical level.

**The "channel topology" that carries spin/chirality (T4_02) is an ELABORATION, not canonical P07.** T4_02 cites "P07 §7.4 (U(1)/SU(2)/SU(3) as channel-topology classes)" and "§7.7 (η thread)" — but canonical Paper_087 P07 has no subsections; these §7.x are a channel-concept elaboration. And T4_02's own verdict is that §7.4 is an **explicitly UNBUILT Phase-2/3 target**: the topology that would carry spin/chirality has never been derived from the participation graph. So there is no constructed channel-topology whose handedness could even be checked.

**Verdict on fork (a): NO — P07's channel-topology is not helical, because at the canonical level it has no topology to be helical.**
- The screw is not supplied by the primitives, so Build 1's **default-VECTOR verdict is confirmed at the primitive level** (not just for the minimal transport). Nothing in P07 (identities), P05 (spin-blind transport, Gauge_02), or P11 (a *time* arrow, no spatial axis) forces a spatial rotation-about-the-momentum.
- A helical/chiral channel-topology is **neither forced nor forbidden — it is undefined-and-unbuilt.** Supplying it = building the entire channel-topology→gauge program (deriving U(1)/SU(2)/SU(3) + the double cover from the graph), a major program with no guarantee the result is handed.
- Tellingly, even within that elaboration, chirality-selection is routed through a **selection** (the η thread: baryogenesis filters channels by polarity vs ∇ρ, §7.7), NOT an intrinsic helix. The corpus's own channel-level picture points chirality at a selection/breaking mechanism, not a handed topology.

**Net: fork (a) is a NO.** ED's emergent fermion is vector-like by default, confirmed at the primitive level; the chiral topology that would change that is undefined-and-unbuilt, not something the primitives quietly supply. The honest redirect is **fork (b): parity violation, if ED has it, is spontaneous / IC breaking via the baryogenesis first-arrival handedness (the η thread / R4 bridge), not an intrinsic topological screw.** This also confirms, from the primitive side, why the "commitment-coupled weak-chirality" mechanism was refutable: there is no handed topology for the arrow to couple to. **T4's chirality gate now reads: default vector (primitive-confirmed); chiral requires either the unbuilt channel-topology→gauge program to be built AND come out handed, or spontaneous/IC selection (fork b) — the ED-native route.**

---

## Fork (b) RESOLVED (2026-07-08) — first-arrival gives C (matter/antimatter), NOT P (parity); the keystone's C/P unification over-reads the P-side

Read `FirstArrival_HandednessImprint.md` (the first-arrival keystone) + `ChiralGauge_SQ1h`. The account claims the first commitment imprints **two** global references at once: (i) a P09-phase reference → matter/antimatter (C-type), and (ii) a **channel-topology / screw orientation** → parity/helicity (P-type). Its own §2 states R4 covers *only* C; the P-type is the "new content" of §3-4, built entirely on the commitment carrying "a channel-topology orientation (the screw's spatial-twist sense)."

**That ingredient is exactly what Build 1 + fork (a) removed.** Build 1: no forced screw in 3+1D. Fork (a): canonical P07 has no channel-topology. So the P-type imprint borrows the same absent handed structure. The honest split:

- **C-type (matter/antimatter): real, ED-native.** R4's first-arrival selects χ* on the P09 phase circle `S¹`, a genuine U(1) order-parameter (parity-**even**) selection → baryogenesis. Solid; untouched by this correction.
- **P-type (parity/helicity): no carrier.** Breaking parity by selection requires a parity-**odd** (pseudoscalar) order parameter — three spatial axes with a fixed handedness. The first commitment has the arrow (a *time* axis) + the P09 phase (an internal U(1)); no handed spatial 3-frame, no pseudoscalar. `S¹` is parity-even, so selecting on it gives C, not P. B5 orientation is a *director* (headless, no orientation sense), and director + arrow = 2 axes, insufficient for a pseudoscalar. There is nothing parity-odd for the first commitment to imprint.

**Verdict on fork (b): first-arrival delivers C, not P.** The keystone's "one event imprints both C and P" **over-reads the P-side**: it assumed a channel-topology screw (its §3-4) that fork (a) + Build 1 show is absent. Same root cause as fork (a): **ED has no handed spatial structure**, so the arrow breaks *time*-symmetry (→ the arrow itself, and → matter/antimatter via the P09 phase) but cannot break *spatial parity*.

**Matter-sector chirality verdict (Build 1 + fork a + fork b, triple-confirmed).**
- **Matter/antimatter asymmetry (C): ED-native** — the arrow's first-arrival P09-phase selection (R4). Real.
- **Parity violation / weak chirality (P): a genuine WALL** — no native mechanism. Confirmed absent from all three angles: wiring/topology (fork a, no channel-topology), transport/screw (Build 1, no 3+1D screw), and selection/first-arrival (fork b, no pseudoscalar order parameter). Weak chirality is **inherited, not derived**.

This is the honest culmination of the T4 chirality attack: ED reproduces the matter/antimatter asymmetry but does **not** natively produce the weak force's parity violation. The over-read to retire is the first-arrival C/P unification's P-half; the C-half (baryogenesis) stands. Tier: derived-conditional VECTOR fermion + C-native / P-inherited, a clean, falsifiable matter-sector tiering, and a correction (not a fabrication) of the keystone's P-claim.
