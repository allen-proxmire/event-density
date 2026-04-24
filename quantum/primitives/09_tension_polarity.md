# Primitive 09 — Tension Polarity

**Role in the framework:** The phase relation between a chain's update rule and the local ED-flow direction (∇ρ, Primitive 06). Polarity is a signed / phase-valued attribute of a chain: aligned-tension chains (matter) are phase-consistent with local ED-flow; anti-aligned-tension chains (antimatter) require participation rearrangement to update. Polarity is the structural property that distinguishes matter from antimatter, that controls survival under saturation selection, and that is the load-bearing primitive for the η derivation. It is also what "tension" in the whole ED vocabulary refers to at the rule-level.

**Status:** First-pass canonical draft. 2026-04-24.

---

## 1. Definition

**Tension polarity** is the phase relation between a chain's update rule (Primitive 02) and the local ED-flow direction at the chain's current position. Two limiting cases:

- **Aligned-tension:** the chain's rule advances in phase-compatibility with local ∇ρ and local relaxation direction. The chain's next micro-event can be instantiated without requiring participation structure to rearrange against the local flow. This is **matter**.
- **Anti-aligned-tension:** the chain's rule advances in phase-opposition to local ∇ρ / relaxation direction. Instantiating the next micro-event requires the local participation structure to rearrange *against* its natural direction. This is **antimatter**.

Polarity is not a binary in general — it is a phase in the full treatment. Between the two limits there is a continuum of phase relationships. But the two distinguished endpoints are the load-bearing cases.

### What polarity *is*

- **A phase relation between rule and flow.** Not an intrinsic property of the chain in isolation; a relational property of chain-in-environment.
- **The matter / antimatter structural distinction.** Matter = aligned; antimatter = anti-aligned. There is no other difference at the rule level. All observed particle-antiparticle pairs (electron / positron, proton / antiproton, etc.) differ exactly in polarity against the ambient ED-flow of the universe.
- **The selection variable for saturation survival.** Under saturated ED, only aligned-tension rules can instantiate without violating saturation constraints. Anti-aligned rules decohere. This is the ED account of why the universe is matter-dominated.
- **Context-dependent.** A chain is aligned relative to a specific flow-direction. Change the flow, change the polarity assignment. CPT symmetry is the structural expression of the fact that polarity is defined only relative to a flow, not intrinsically.

### What polarity is *not*

- **Not charge.** Electric charge is a separate rule-type attribute. Polarity is the alignment-phase against the ambient flow. In practice they correlate (positrons have opposite charge and opposite polarity to electrons relative to the cosmological ED-flow) but they are distinct structural quantities.
- **Not handedness or helicity.** Helicity is a spatial-orientation attribute of the chain's own internal structure. Polarity is the phase of the whole rule against the external flow.
- **Not CP violation.** CP violation is a specific type of asymmetry in how polarity-flip interacts with spatial inversion at the rule level. Polarity itself is the more basic structure; CP violation is a higher-order effect on how polarity-dependent rules compose.
- **Not a scalar.** Polarity is a phase. In certain limits it reduces to a sign (matter / antimatter binary), but the general object has phase structure.

### Why polarity has to be this

The ED account of baryogenesis (ED-I-11) needs a structural distinction between matter and antimatter that is (i) present in the rule-level structure, not added as a separate charge, (ii) relative to ambient flow rather than intrinsic, and (iii) selectable under saturation dynamics. A rule-vs-flow phase meets all three. No other primitive-level object in 01–08 does.

---

## 2. Mathematical Object

### Discrete / rule-level

For a chain `C` with rule `R` at position `v ∈ V`, polarity is:

`π(C, v) = phase(R) - phase(flow at v)`

where `flow at v` is the direction of bandwidth-weighted ∇ρ in the local neighborhood, and `phase` is the rule-update phase expressed in a coordinate compatible with that flow.

- `π ≈ 0 (mod 2π)`: aligned-tension (matter)
- `π ≈ π (mod 2π)`: anti-aligned-tension (antimatter)
- Other values: intermediate / unstable regimes that collapse to one of the two endpoints under selection

### Continuum / thick-regime

`π(x, C) : M → S¹` — a circle-valued field giving the polarity of chain C as a function of position.

Under saturated-flow conditions, the field is driven toward aligned endpoints; anti-aligned regions either relax (rule-swap to aligned) or decohere (chain terminates).

### Polarity and CPT

- **C (charge conjugation):** rule-swap that reverses polarity — aligned ↔ anti-aligned
- **P (parity):** spatial inversion of the chain's internal structure; leaves polarity invariant if the flow is itself parity-symmetric
- **T (time reversal):** reverses the flow direction; therefore swaps which rules count as aligned vs. anti-aligned — effectively a polarity flip
- **CPT:** the triple composition returns polarity to its original value — this is the ED structural content of CPT invariance

CPT is, in ED, the fact that polarity is defined *relatively* to the flow: any global transformation that preserves the rule-flow relationship preserves polarity, and CPT is the minimal such transformation.

### What is *not yet* settled

- **Precise phase-coordinate for a given rule-type.** "Phase of R" in the discrete definition requires a choice of coordinate on the rule's internal update cycle. Whether this coordinate is universal or rule-type-specific is open.
- **Continuous vs. discrete spectrum of polarity.** Matter / antimatter suggests binary. Intermediate unstable values might exist transiently.
- **Relation to intrinsic spin.** Spin has polarity-like structure at the single-chain level. Whether intrinsic spin is a polarity-adjacent primitive or a separate structure (likely: separate — spin is internal chain-geometry, polarity is external rule-vs-flow) needs explicit treatment.

---

## 3. Relations to Earlier Primitives

### Upstream

| Primitive | Role |
|---|---|
| 02 Chain | Polarity is a property of the chain's rule |
| 03 Participation | The flow polarity is measured against is a participation-structure object |
| 04 Bandwidth | Phase-comparison requires a bandwidth-coherent frame for comparing rule-phase and flow-phase |
| 06 ED gradient | ∇ρ defines the flow direction |
| 07 Channel | Polarity is naturally defined along a channel's tangent direction |

### Downstream

| Primitive | Role |
|---|---|
| 10 Individuation | Individuation may require polarity-consistency across the chain boundary |
| 11 Commitment | Commitment events can include polarity-flip (rule-swap) events under specific conditions |
| 12 Thickening | Thickened structures have stabilized polarity; polarity-inconsistent structures don't thicken |
| 13 Relational timing | Polarity is a phase relation; relational timing is the rhythm at which phases update |

### Circular-definition flags

1. **"Phase of R"** requires a coordinate on the rule's update cycle — operational until rule-type taxonomy is formalized (Primitive 07 §7).
2. **"Flow direction"** uses ∇ρ from Primitive 06; not circular but dependency.
3. **"Anti-aligned chains decohere"** forward-references Primitive 11 (Commitment) for the decoherence mechanism.

---

## 4. Measurable Signature

- **Matter / antimatter asymmetry.** The macroscopic cosmological signature. η ≈ 6 × 10⁻¹⁰.
- **CP violation.** In kaon, B-meson, and (by implication) neutrino sectors. Small asymmetries in how polarity-flip interacts with spatial inversion.
- **Annihilation rates.** Matter + antimatter → radiation at bandwidth-equivalent rest-mass. An aligned + anti-aligned chain pair is structurally unstable — the pair annihilates back to polarity-neutral photon chains.
- **ALPHA-g and related antimatter-gravity tests.** ED predicts antimatter gravitates identically to matter because the gravitational coupling is to ρ contribution, which is polarity-independent (ED-I-11, ED-10). ALPHA-g has confirmed this at ~1σ; stronger tests in progress.
- **Neutrino mass hierarchy and mixing.** Polarity structure at the neutrino rule-type is tied to the flavor-channel mixing and possibly to the mass-hierarchy question.
- **Pair production thresholds.** A photon at sufficient bandwidth can fission into aligned + anti-aligned chain pair. The threshold is 2mc²-equivalent because two polarity-endpoints of equal magnitude must emerge simultaneously (polarity conservation).

### Operational handle

- Not directly operationalized in current ED-Arch (which is single-rule-type); cosmological simulator (Phase 4 infrastructure) would implement polarity explicitly.
- The tension-polarity concept has been present in ED-I-11 and in the simulator's implicit treatment of chain stability; it has not been explicitly parameterized.

---

## 5. Example Applications

### 5.1 Baryogenesis (the central case)

In the saturated post-inflationary ED, all commitment events that instantiate new chain-rule-continuations are filtered by polarity compatibility. Aligned-tension rules can commit because their update is phase-consistent with the local flow. Anti-aligned-tension rules cannot commit without rearranging participation structure that saturation has locked; those rules decohere. Survivors: aligned-tension chains (matter). Non-survivors: anti-aligned chains (antimatter). The ratio of survivors to total committed events is η.

This is the structural baryogenesis mechanism. It does not require new particles, enhanced CP violation, or sterile neutrinos. It requires the polarity-selection rule under saturated flow — which is a structural consequence of primitives 03, 04, 06, 09 acting together.

### 5.2 Pair creation and annihilation

Energy-equivalent photon → e⁺ + e⁻: an aligned + anti-aligned chain pair produced from a polarity-neutral photon chain, conserving total polarity (zero). The reverse: the pair meets, polarities cancel, photon emerges.

### 5.3 ALPHA-g and antimatter gravitation

Antimatter has anti-aligned polarity. But polarity is a rule-vs-flow phase; gravitational coupling is to ρ contribution. Anti-aligned chains contribute ρ in the same way aligned chains do. Therefore antimatter gravitates identically to matter. ALPHA-g data (2023) confirms this.

This is one of the few currently-checkable ED predictions that has landed. Polarity does not couple to gravity at the ρ level.

### 5.4 CPT in ED

CPT invariance is the structural consequence of polarity being a relative phase against the flow. Any transformation preserving the chain-to-flow relationship preserves polarity; CPT does. This is not a postulate in ED but a derived symmetry.

### 5.5 Neutrino polarity and mass hierarchy

The fact that all observed neutrinos are left-handed and all antineutrinos right-handed, in the absence of evidence for the other two helicities, is a polarity-constraint at the neutrino rule-type. Whether neutrinos are Majorana (their own antiparticle — polarity-trivial) or Dirac (distinct anti-neutrino — polarity-doubled) is a live experimental question with direct ED interpretation at the polarity level.

### 5.6 Non-observation of macroscopic antimatter domains

The universe does not contain galaxy-scale antimatter regions. In ED: saturated-flow selection was global, not patchy. The polarity-selection rule applied everywhere in the post-inflationary phase. No region escaped the selection; no anti-matter island survives. This is why searches for antimatter domains (via annihilation-boundary gamma signatures) have been null.

---

## 6. Simulator / PDE Instantiation

- Current ED-Arch is single-rule-type; no explicit polarity. A polarity-extended simulator would instantiate two rule-types distinguished by phase, watching survivability under saturated-flow conditions.
- Q-C Boundary PDE handles single-chain dynamics; polarity is a global attribute of which rule is running and doesn't appear explicitly.
- GR-SC work does not invoke polarity.

### What's missing

- Polarity-extended simulator for cosmological / baryogenesis studies — Phase 4 infrastructure priority.
- Formal polarity-selection rule in terms of the bandwidth / saturation condition — Phase 4 formalization.
- Quantitative η derivation from the selection rule — Phase 4 target.

---

## 7. Open Questions

1. **Rule-phase coordinate.** How is "phase of R" made precise for a given rule-type? Structural or conventional?

2. **Continuous vs. binary polarity spectrum.** Do intermediate polarities exist transiently? Do they correspond to unstable particle states?

3. **Polarity and spin.** Spin is rule-internal geometry; polarity is rule-vs-flow phase. Their interaction — why polarity-flip correlates with spin-statistics properties — needs explicit treatment.

4. **Majorana vs. Dirac in polarity language.** Is the Majorana case "polarity-self-inverse" and the Dirac case "polarity-doubled"? If yes, neutrino experiments directly probe polarity structure.

5. **η derivation (the priority).** The saturation-selection rule in precise bandwidth / gradient terms gives a ratio of aligned-survivors to total commitments. Computing this ratio requires: ρ evolution through saturation, bandwidth budget in the selection filter, explicit phase-comparison between rule update and local flow. All Phase 4 work. **Priority target.**

6. **CP violation magnitude.** Standard-Model CP violation is too small for observed baryogenesis. In ED, η comes from the selection rule directly, not from CP violation. The observed CP violation is a separate, smaller effect on polarity-sensitive rule composition. Quantitative relation is open.

---

## 8. One-line summary

> **Tension polarity is the phase relation between a chain's update rule and the local ED-flow direction. Aligned = matter, anti-aligned = antimatter. It is the structural origin of the matter/antimatter distinction, the load-bearing primitive for baryogenesis selection under saturated ED, the reason CPT holds, and the priority hook for the η derivation.**
