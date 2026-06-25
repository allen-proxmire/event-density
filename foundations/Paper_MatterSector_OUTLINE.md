# OUTLINE — Matter-Sector Paper (Gauge Structure from Channel Topology)

**Planning doc, not the paper. Maps the session's results onto the Paper GR-II house style (Preamble-NOT-claims → dense abstract → §1 Intro → §2 Primitive Inputs → §2.5 Load-Bearing Audit → derivation sections → Residual → Wedge → Falsifiers → two-part Position Statement → Appendix/Glossary/Reader-map). Eventual target: `ED Generative/physics-papers/` (RQM/QFT line). Tier of the paper: M2 — structural results derived + one unifying account, with the frontier honestly open (same shape as GR-II).**

---

## Proposed title (GR-II "evocative : descriptive list" pattern)

**Primary:** *The Arrow's Other Fingerprint: Event-Density's Matter Sector is a Lattice Gauge Theory — Gauge Groups from Channel Multiplicity, Parity Violation from the Non-Abelian Sector, Chirality from the First Commitment*

**Alternates:**
- *Forces from Channels: Event-Density's Gauge Sector as a Lattice Gauge Theory on the Participation Graph*
- *Where Parity Lives: Channel Multiplicity, the V1/V5 Kernel Split, and the Arrow as the Origin of Chirality*

(Mirrors GR-II's "The Arrow's Fingerprint: … Khronometric, GW-Clean, and Lorentz-Safe." The matter-sector "fingerprint of the arrow" is chirality, paralleling gravity's khronon — same through-line: ED's signature commitment, the arrow, shows up as the one departure/feature.)

**Series/Status line:** Event Density Generative Papers — Relativistic-QM / QFT line, matter-sector. *Publication draft. Conditional structural derivation within the 13-Primitive Generative System. Standalone; cold-reader accessible.* Companions: T17 (gauge rewrite — superseded in part), T2/T4 (Cl(3,1)/Dirac), Paper_090 (V5), the baryogenesis arc (R4).

---

## Preamble: What This Paper Does NOT Claim (write first)

1. The 13 primitives are not derived (Paper_087).
2. **The Standard-Model gauge group U(1)×SU(2)×SU(3) is not derived.** The paper derives that gauge groups are SU(N) from channel multiplicity, and that the SM groups correspond to multiplicities {1,2,3}; it does **not** derive *why* the multiplicities stop at 3 (the uniqueness question — §Residual; the spatial-dimension candidate was a category error and is retracted).
3. **The weak force's specific chirality is not derived.** The paper shows parity violation is confined to the non-abelian sector and that all chirality originates in the arrow's first commitment; it does **not** derive why the *weak* SU(2) in particular couples to one handedness (the matter-assignment — tangled with the SM's own open problems, strong-CP and the CKM phase; the candidate "commitment-coupled" mechanism was tested and refuted).
4. **The chirality-origin result is an account, not a closed proof.** "All chirality traces to the arrow's first commitment" is built on established pieces (the R4 lock, the topological quantization, the screw) plus one new synthesis; the selection *direction* is a contingent initial condition (spontaneous symmetry breaking).
5. **No Yang–Mills action, no electroweak/Higgs sector, no anomaly cancellation** are derived (all deferred — §Residual). The paper builds the gauge *connection and curvature* (the kinematics), not the dynamics.
6. **"P05 re-routes channels unitarily" is a structural reading** of P05 (P07 composition + P04 bandwidth + between-commitment invertibility), defensible but not a closed substrate proof.
7. Masses, mixing angles, coupling constants — inherited, not derived.
8. No claim ED is the only consistent substrate ontology.

---

## Abstract (drafted — the core, tiered)

> Event Density's substrate is a participation graph on which chains propagate along **channels** (P07) carrying U(1) **polarity** (P09), transported by **P05**. This paper asks what *gauge structure* that substrate carries. Four structural results. **(1) The gauge group is the channel count.** A rule-type family of N indistinguishable channels, under bandwidth conservation (P04), has structure group **U(N) = SU(N)×U(1)** — so non-abelian SU(N) is forced by channel **multiplicity** (P08), grounding what the prior gauge rewrite (T17) obtained only by analogy. The Standard-Model groups correspond to multiplicities {1,2,3}. **(2) The substrate is a lattice gauge theory.** P05-transport of N channels — bandwidth-conserving and invertible between commitments — is a **U(N) link variable**; the gauge field is the per-edge generator and the field strength is the plaquette holonomy. ED's matter sector is a non-abelian lattice gauge theory on the **relational** graph (no Brillouin torus) with the **retarded** arrow — exactly the structure that escapes the Nielsen–Ninomiya doubling no-go. **(3) Parity violation is a non-abelian phenomenon.** The abelian (single-channel, V1) coupling is chirality-blind — vector, parity-conserving (electromagnetism); only the non-abelian (cross-channel, V5) coupling is chirality-sensitive and can violate parity. ED therefore *forbids* a parity-violating abelian force (a falsifiable prediction; chiral abelian U(1)s are allowed in general gauge theory). The vector/chiral split of the forces is the V1/V5 = single/cross-channel split. **(4) All chirality originates in the arrow.** A commitment is a handed event — it carries a P09 phase *and* a channel-topology screw orientation; the universe's **first commitment** imprints both a matter/antimatter reference (the phase) and a parity reference (the screw), locked globally and made maximal by their topological (quantized) character. Parity violation and the matter/antimatter asymmetry are two attributes of one first-arrival imprint — correlated but distinct, reproducing C and P violated separately with CP only partial — unifying the chiral-gauge structure with baryogenesis under the substrate's signature commitment, the arrow. The paper does **not** derive the SM gauge group (why multiplicities stop at 3 is open), the weak force's specific chirality (the matter-assignment is open), or the Yang–Mills dynamics; result (4) is an account, not a closed proof. What ED's *structure* forces — gauge group from multiplicity, lattice-gauge-theory form, parity-violation-is-non-abelian, chirality-from-the-arrow — is independent of those open quantities.

---

## §1 Introduction
- **1.1 What this paper does** — the four results above, in order; positions against T17 (a vocabulary *rewrite* that postulated U(1) and analogized the non-abelian sector; this paper derives both).
- **1.2 Why this matters** — the deepest question for a discrete substrate is whether it can carry chiral gauge fields without Nielsen–Ninomiya; the honest answer is the interesting one (it can — lattice gauge theory on a relational graph with the arrow — and chirality turns out to be the matter-sector fingerprint of the same arrow that gives gravity its khronon). Parallel to GR-II's framing.
- **1.3 How this fits the arc** — T2 (Cl(3,1)), T4 (Dirac form) inherited; T17 superseded in part; Paper_090 (V5) and the baryogenesis R4 mechanism load-bearing; the open matter-sector targets downstream.
- **1.4 Conventions and regime of validity** — continuum (DCGT) limit for the gauge fields; the results are *multiplicity-independent in form* (they don't depend on the value {1,2,3}); no strong-coupling, no Higgs, no cosmology claim.

## §2 Primitive Inputs
- Substrate: P02, P04 (bandwidth conservation — load-bearing), P05 (transport/connection), P07 (channels), P08 (multiplicity), P09 (U(1) polarity), P11 (commitment/arrow).
- Inherited: T2 (Cl(3,1) 4-spinor), T4 (Dirac form), Paper_090 (V5 kernel; gauge-compatibility, chirality-sensitivity via R4), the R4 first-arrival lock (baryogenesis).
- Mathematical input (inherited, standard): U(N) as the isometry group of ℂ^N; lattice-gauge-theory holonomy/plaquette; the Nielsen–Ninomiya premises (Brillouin torus + hermiticity).
- Value-layer (inherited): masses, mixings, the multiplicities {1,2,3} themselves.

## §2.5 Load-Bearing Step Audit (the table — tiers)

| Step | Status | Source |
|---|---|---|
| Channel fiber carries U(1) polarity; P05 = connection (named) | I | T17 (named); grounded below |
| N indistinguishable channels + P04 → structure group U(N)=SU(N)×U(1) | **D** | Gauge_01 §2 |
| Non-abelian SU(N) from multiplicity (P08) | **D** | Gauge_01 — beyond T17's A→analogy |
| SM groups ↔ multiplicities {1,2,3} | I (correspondence) | Gauge_01 §4 |
| P05-transport of N channels = U(N) link variable (bandwidth-conserving, invertible between commitments) | **D-structural** | Gauge_02 §2 — "P05 re-routes unitarily" is a structural reading (preamble 6) |
| Gauge field = per-edge generator; field strength = plaquette holonomy | D | Gauge_02 §3 |
| Substrate = lattice gauge theory on relational graph + retarded arrow → escapes N–N | **D-structural** | Gauge_02 §4 + SQ1 |
| V1 chirality-blind (vector); V5 chirality-sensitive | I | R4 (∂_χ𝒦_V1=0; 𝒦_V5∝alignment) |
| Parity violation ⟺ non-abelian (abelian/EM = vector, forbidden chiral) | **D-structural** | Gauge_05 |
| Spin/chirality = channel topology; P09 = vector U(1) | **D-structural** | T4_01/02 |
| Commitment is a handed event (P09 phase + screw); first commitment imprints C and P references | **account** | FirstArrival §3–4 — new synthesis, not closed proof (preamble 4) |
| Both references topological → maximal; C/P correlated-but-distinct | D-via-account | FirstArrival §5 + SQ1d |
| Parity violation + matter/antimatter = one first-arrival imprint (unification) | **account** | FirstArrival §5 |
| Uniqueness {1,2,3} (why stop at 3) | **OPEN** | Gauge_03/04 — spatial bound a category error, retracted |
| Weak-specific chirality (why L-doublets) | **OPEN** | WeakChirality_Tested — commitment hook refuted |
| Yang–Mills action; electroweak/Higgs; anomalies | **deferred** | §Residual |

## §3 The Gauge Group is the Channel Count (Gauge_01)
- §3.1 The channel bundle (base = loci, fiber = channel space, connection = P05).
- §3.2 N indistinguishable channels + bandwidth conservation → U(N) = SU(N)×U(1). Non-abelian from multiplicity.
- §3.3 The SM correspondence {1,2,3} (stated as correspondence, not derivation).

## §4 The Substrate is a Lattice Gauge Theory (Gauge_02)
- §4.1 P05-transport of N channels = U(N) link variable (bandwidth conservation + invertibility-between-commitments).
- §4.2 Gauge field, field strength (plaquette holonomy), holonomy (grounds Aharonov-Bohm/Berry's inherited use).
- §4.3 Relational graph + retarded arrow = the Nielsen–Ninomiya escape (tie to the discreteness objection — the §1.2 hook).
- §4.4 Unitary between commitments; commitments = projections (sparse-commitment).

## §5 Parity Violation is Non-Abelian (Gauge_05 + T4_01/02)
- §5.1 V1 chirality-blind (vector/EM); V5 chirality-sensitive (R4).
- §5.2 So parity violation can only live in the non-abelian (V5) sector; abelian forces are necessarily vector. The V1/V5 = vector/chiral = EM/weak split.
- §5.3 Spin/chirality = channel topology; P09 = the vector U(1). (The "why the transport route looked vector-like" resolution.)

## §6 The Arrow is the Origin of Chirality (FirstArrival) — the centerpiece
- §6.1 A commitment is a handed event (phase + screw; the screw = time-arrow correlated with spatial twist).
- §6.2 The first commitment imprints both references (C: phase → matter/antimatter; P: screw → parity); R4 locks them globally; topology makes them maximal.
- §6.3 C and P correlated (same event) but distinct (different attributes) → C, P separate, CP partial.
- §6.4 The unification: parity violation + matter/antimatter asymmetry = two faces of one first-arrival imprint. The arrow is the source of all chirality (with the khronon, α₁, time dilation — cross-reference GR-II). *Tiered as account throughout.*

## §7 The Residual and the Open Frontier (the GR-II §8 analog)
- Uniqueness {1,2,3} — open; the spatial-dimension candidate was a category error (complex-internal count ≠ real-spatial dimension); redirect to internal channel-family stability.
- Weak-specific chirality — open; the commitment-coupled hook refuted (the chiral, flavor-conserving Z); tangled with strong-CP and the CKM phase.
- Yang–Mills action (lattice→continuum via DCGT); electroweak/Higgs (the V1/V5 split does not capture chiral hypercharge); anomaly cancellation.
- Which handedness — contingent IC (standard SSB).

## §8 The Wedge — Where ED Diverges / Predicts (GR-II §10 analog)
- **Falsifiable prediction 1:** no parity-violating *abelian* fundamental force (EM-type forces are vector). [The sharpest clean prediction.]
- **Prediction 2:** gauge group rank = channel multiplicity (forces come in SU(N) families).
- **Structural claim:** the matter sector is one lattice gauge theory unifying gauge fields (multiplicity) and matter (channel topology) on the relational graph.
- **Unification claim:** parity violation and the matter/antimatter asymmetry share one origin (the first-arrival imprint).

## §9 Falsification Criteria (GR-II style — falsifier sentences)
- *A parity-violating fundamental abelian gauge force would falsify §5 (abelian = vector).*
- *A fundamental gauge force whose group is not SU(N)×U(1)-type (not a channel-multiplicity structure group) would falsify §3.*
- *A demonstration that ED's relational-graph lattice gauge structure does carry the N–N doubling (vector-like-forced) would falsify §4.3 / the discreteness reply.*
- *Demonstration that the matter/antimatter asymmetry and parity-violation handedness are uncorrelated (not a shared first-arrival imprint) would falsify §6's unification.*

## §10 Position Statement (two-part, GR-II style)
- **What this paper claims:** gauge group = SU(N) from channel multiplicity; the substrate is a lattice gauge theory (relational graph, escapes N–N); parity violation is confined to the non-abelian sector (abelian forbidden chiral); all chirality originates in the arrow's first commitment (account), unifying parity violation with baryogenesis — all independent of the open quantities.
- **What this paper does not claim:** the SM gauge group (uniqueness open); the weak force's specific chirality (open); the Yang–Mills dynamics, electroweak/Higgs, anomalies (deferred); §6 is an account, not a proof; the selection direction is contingent IC.
- **Series context:** matter-sector companion to the gravity line (GR-II) — the arrow's fingerprint in matter (chirality) as the khronon is its fingerprint in gravity.

## Appendix — Cross-references, Glossary, Reader-map/Open-work
- Glossary: channel, multiplicity, V1/V5 kernels, structure group, lattice gauge connection, plaquette holonomy, screw, first-arrival imprint, C-type/P-type chirality.
- Reader map: where to look for spin/Dirac (T2/T4), V5 (Paper_090), baryogenesis lock (R4), the gravity-line arrow (GR-II).
- Open work (declared): uniqueness via stability; the weak matter-assignment; YM action; electroweak; anomalies.

---

## Notes for the full draft
- **Voice:** GR-II's — honest, results-forward, crank-railed; "to avoid overclaiming" asides; italic forward-notes where downstream work would resolve.
- **Tier discipline:** the four headline results are D / D-structural; the centerpiece (§6) is explicitly *account*; the frontier is *open/deferred*. Keep the abstract's NOT-claims loud.
- **The N–N hook** (§1.2 + §4.3) is the paper's strongest framing device — it answers the standard "the universe can't be discrete" objection head-on, which is the natural cold-reader entry point.
- **Length:** GR-II is ~325 lines / ~12 sections. Target similar.
- **One paper, not several** (per the "2 will do" instinct): this single paper carries the whole matter-sector arc; baryogenesis/gravity are cross-referenced, not folded in.
