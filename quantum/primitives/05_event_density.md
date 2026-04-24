# Primitive 05 — Event Density

**Role in the framework:** The scalar count-measure that pairs with bandwidth (Primitive 04) to form the continuum substrate for the PDE layer. Where 04 weights the edges of the participation graph, 05 measures the vertices — how many micro-events have accumulated in a region. Together they are the two components that coarse-grain into the continuum field descriptions used throughout the ED PDE work (ED-Phys-16/17, P6, 00.3) and the ED-Arch simulator. Event density is the primitive the framework is named after; it is where the theory makes contact with quantities that can be written down as fields on space.

**Status:** First-pass canonical draft. 2026-04-24.

---

## 1. Definition

**Event density** is the local scalar count-measure of accumulated micro-events per region of the emergent manifold (or per neighborhood of the discrete participation graph, in the pre-manifold regime). It is the most basic scalar you can write down in ED: *how many becomings have taken place around here*.

In the discrete formulation: `ED(R) = |V ∩ R|` for some region `R`, where `V` is the set of micro-events (Primitive 01) and `R` is a neighborhood defined by participation adjacency (Primitive 03).

In the thick regime: `ρ(x) = dED/dV` — a continuous field on the emergent manifold whose integral over any region recovers the event count in that region.

### What ED *is*

- **A scalar count.** Non-negative, additive across disjoint regions, zero in causally disconnected / not-yet-participated regions.
- **The vertex measure of the participation graph.** Primitive 04 weights edges; Primitive 05 counts vertices. Together, `(ρ, b)` is the full graph state.
- **The substrate for gradient dynamics.** An ED gradient (Primitive 06) is `∇ρ`; it exists only because ρ is a field. Without ρ there is nothing to take a gradient of.
- **The quantity the framework is named after.** ED = Event Density. The whole ontology is built around the claim that this scalar, plus its gradients and its coupling to bandwidth, is sufficient (in the thick regime) to produce the phenomenology classical physics describes with metrics, fields, and matter content.

### What ED is *not*

- **Not energy density.** Energy density in classical / relativistic physics is a thick-regime accounting quantity. ED is prior: it is the count of becomings, and energy-like quantities emerge from the rate-of-change of ED along chain trajectories (per the PDE layer). ρ is not T₀₀.
- **Not probability density.** In QM, |ψ(x)|² is a probability density — a pre-commitment weighting of channel outcomes. ED is the count of already-committed micro-events. Born-rule weights are channel-bandwidth quantities (Primitive 04), not ED.
- **Not mass density.** Mass in the thick regime is a very specific derived quantity tied to the stable-core density of chains with particle-like update rules (ED-Arch, ED-I-23). ρ counts all micro-events, not only those in persistent chains.
- **Not observer-dependent.** Different observers in the thick regime may coordinatize ρ differently, but the count of micro-events in a given region of the participation graph is structural. Coordinate dependence enters only when we project onto emergent spacetime charts.

### Why a count-measure is enough

The choice to make the core scalar a *count* rather than an *intensity* or *magnitude* is load-bearing. Counts are additive, non-negative, discrete at the base, and match the atomic-event ontology of Primitive 01 without introducing new quantities. All other scalars in ED (energy, mass, charge, temperature) are derived combinations of ρ, b, and their gradients. ED does not postulate them; it predicts them as coarse-grainings.

---

## 2. Mathematical Object

### Discrete version

For the participation graph `G = (V, E, w)` with vertex set `V`, edge set `E`, and edge weights `w = b` (bandwidth):

`ED : 2^V → ℕ` defined by `ED(S) = |S|` for any subset `S ⊆ V`.

Restricted to a "region" — a participation-connected neighborhood defined via adjacency thresholds — ED gives a count that matches the intuitive "how many events here."

### Continuum version

In regimes where the participation graph is dense enough to coarse-grain, the count measure converges to a smooth density field:

`ρ : M → ℝ≥0`

where `M` is the emergent manifold (or a pre-manifold region equipped with participation-adjacency structure that locally resembles a manifold).

Properties:

- **Non-negative:** `ρ(x) ≥ 0` everywhere.
- **Additive:** for disjoint `R₁, R₂`, `ED(R₁ ∪ R₂) = ED(R₁) + ED(R₂)`.
- **Countably additive** at scales above the coarse-graining threshold.
- **Bounded above locally** — there is a maximum ρ a region can sustain before saturation dynamics change the update behavior (the saturation regime is what drives baryogenesis selection and inflationary-end phenomenology).

### The paired state (ρ, b)

Together with bandwidth, the pair `(ρ, b)` is the full coarse-grained state of the participation graph. This pair is the input to the continuum dynamics:

- `ρ(x)` — scalar event-density field
- `b(x, y)` — bandwidth kernel between regions (usually reducing to local `b(x)` + short-range structure in the thick regime)

The PDE layer (ED-Phys-16/17, P6, 00.3, 06a-c) is a family of evolution equations for `(ρ, b)` under specific regime assumptions. The effective channel weight `D(x)` used in the Q-C Boundary PDE is a functional of `(ρ, b)`.

### What is *not yet* settled

- **Coarse-graining threshold.** At what participation-graph density does the discrete count converge robustly to a continuum density? This is the ED analog of the statistical mechanics thermodynamic limit. Likely depends on the local channel multiplicity (Primitive 08) and the bandwidth distribution (Primitive 04), not just vertex count.
- **Saturation bound.** There is a local maximum ρ_max beyond which new micro-event accumulation changes the participation topology (saturation). Is ρ_max a universal constant, or is it region-dependent? ED-I-11 treats it as universal for baryogenesis; inflation-end phenomenology may require regional variation.
- **Relationship to bandwidth.** Dense ED usually implies dense bandwidth — you can't have many micro-events clustered without many participation edges forming between them. But you can have the converse: a region with modest ρ but very high bandwidth internally (a well-connected chain). The functional relationship between ρ and the bandwidth-kernel distribution `b` is not a pointwise identity. Needs explicit treatment.
- **Signed density.** ED is non-negative by construction (you can't have fewer than zero events). But the *time rate of change* of ρ can be negative (outflow regions). Whether to carry signed ρ-flux as a separate object (essentially a current) or to keep it implicit in ∇ρ dynamics is a formulation choice; the PDE layer does the latter.

---

## 3. Relations to Earlier Primitives

### Upstream dependencies

| Primitive # | Role |
|---|---|
| 01 Micro-event | ED counts these — no micro-events, no density |
| 03 Participation | "Region" is defined via participation adjacency; without participation structure, the count has no neighborhood to be indexed by |
| 04 Participation bandwidth | Coarse-graining from discrete count to continuum field requires sufficient participation-bandwidth density to support the limit |

Primitive 05 is downstream of 01, 03, and 04. It does *not* depend on Primitive 02 (Chain) directly — ED counts all micro-events regardless of whether they belong to a stable chain. Chain structure is a refinement that identifies *which* micro-events in a region have coherent rule-identities, but the density is the raw count.

### Downstream

| Primitive # | How it uses ED |
|---|---|
| 06 ED gradient | `∇ρ` is the first geometric quantity — gradients presuppose a scalar field to differentiate |
| 07 Channel | Channel stability is bandwidth-preservation *along a trajectory*, and the trajectory is parameterized through ED structure |
| 08 Multiplicity | Regions with ρ well above saturation threshold support fewer channels; regions well below support many. Multiplicity is a function of ρ (and bandwidth) |
| 09 Tension polarity | Polarity is a phase relation against the *local relaxation direction*, which is the direction of ∇ρ (Primitive 06) — so it traces back to 05 |
| 10 Individuation | Individuation requires internal ρ exceeding a boundary-sharing threshold |
| 11 Commitment | Commitment events add to ρ at a specific location; every commitment is an increment of ED |
| 12 Thickening | Thickened regions are high-ρ regions with committed structure |
| 13 Relational timing | The rhythm of ρ updates across coupled channels |

### Circular-definition flags

1. **"Saturation regime"** in §1 leans on Primitive 06 (ED gradient) and Primitive 11 (Commitment) for the dynamical definition — saturation is when ∇ρ reaches a critical magnitude beyond which commitment events no longer accumulate normally.
2. **"Region"** in §1 leans on Primitive 03 (Participation) via adjacency, which is already drafted — this is not circular but dependency.
3. **"Coarse-graining"** in §2 leans on Primitive 12 (Thickening) for the full formal condition under which a continuum limit is well-defined.

---

## 4. Measurable Signature

ED itself is not directly observable as a raw scalar (there's no detector that reads "event density = X micro-events per cubic meter"). But its consequences are pervasive.

### Direct observable consequences (in ED's mapping)

- **Mass density in the thick regime.** The mass density of ordinary matter is a specific combination of ρ and chain-multiplicity (Primitive 08) restricted to particle-like chain rules. High-ρ + particle-chain-rule-density = high mass density.
- **Casimir-like pressures.** Vacuum regions have non-zero baseline ρ (vacuum is not empty in ED; it is low-ρ but non-zero; ED-I-12, ED-09). Geometric constraints on vacuum ρ produce pressure differences — the Casimir effect.
- **Cosmological density of baryons / photons.** Large-scale ρ distributions in early-universe dynamics (ED-I-11) set the observed cosmological densities and the baryon-to-photon ratio η.
- **Gravitational-potential magnitude.** In the thick regime, ∇ρ produces the effective gravitational potential (ED-10 §7.2). Regions of high ρ produce deep potential wells.
- **Refractive index in photonics.** In photonic materials, local ρ variations modify the propagation bandwidth of null chains — the classical refractive index (ED-I-12).
- **Superconducting order parameter magnitude.** The amplitude of the superconducting gap is proportional to the local ρ of Cooper-pair-chain micro-events (ED-I-23).
- **ED-Arch simulator field ρ(x, t).** In the simulator, the field is explicit — every site carries a numerical ρ value. The simulator is the direct operational handle on ED as a field.

### Indirect consequences

Essentially every field-theoretic quantity in classical physics is a functional of ρ, b, and their gradients. Charge density is (conceptually) a refinement of ρ by a chain-type filter. Current density is ρ-flux along a chain-type-filtered participation network. Stress-energy is the combined local accounting of all of these.

### Operational handle

- **ED-Arch.** Scenario E update rule defines ρ(x, t) explicitly. Gamma-sweep, radius-spectra, orbit-distance studies all track ρ as the primary field.
- **Q-C Boundary PDE.** The PDE evolves ρ together with ancillary chain-specific variables. `D(x)` is a functional of `ρ` along the chain's trajectory.
- **Cosmological simulations (future).** A large-scale ED simulator for early-universe regimes would track ρ at cosmological scale; ED-I-11 and the η-derivation Phase 4 target both require this infrastructure.

---

## 5. Example Applications

### 5.1 Gravity as ∇ρ in the thick regime

Classical gravitational attraction is, in ED, an expression of ρ gradients. Dense regions have high ρ; low-ρ regions are "above" denser regions in the participation-manifold sense. Chains propagating through an ∇ρ structure follow paths of least bandwidth-cost, which in the thick regime reduces to geodesic motion in the effective metric (ED-10 §7.2). There is no gravitational force as such; there are bandwidth-preference paths through a ρ-gradient landscape.

This is the simplest application: gravity is ED-gradient dynamics. The Newtonian potential is a thick-regime linearized summary of ∇ρ; the relativistic version (ED's account of GR) is the full nonlinear ρ / b geometry.

### 5.2 Vacuum ρ and the Casimir effect

Vacuum in ED is not empty — it has a baseline ρ supported by low-bandwidth participation structure (ED-09, ED-I-12). Two parallel conducting plates impose geometric boundary conditions that suppress the bandwidth spectrum supportable between them, lowering the local vacuum ρ relative to the unbounded vacuum outside.

The ρ differential produces an effective pressure — the Casimir force. The standard QED calculation gives the correct numerical result; ED's interpretation is that the QED vacuum-mode sum is a specific accounting of participation-bandwidth modes consistent with the boundary conditions, and the force is the ρ-gradient across the plates.

### 5.3 Cosmological ρ and η

In the saturated early universe, participation selection rules (Primitive 03 §7.4, Primitive 04 §7.7) admit only aligned-tension chains into long-term stability. The surviving-chain ρ (baryons) vs. total committed-event ρ (photons + baryons) gives the observed ratio η ≈ 6 × 10⁻¹⁰.

This is the Phase 4 priority derivation. It requires an explicit dynamical model of ρ evolution through the saturation-relaxation transition, with the participation-selection filter applied. Current status: motivated, not yet derived.

### 5.4 Refractive index and photonics

In an optical medium, null chains (photon-chains) propagate through a local ρ structure that differs from vacuum. The local bandwidth available to null-chain rules is modified: higher ρ configurations typically slow the null-chain update rate, giving refractive index `n > 1`. The full ED account reproduces classical and quantum optics (ED-I-12) with n as a functional of ρ and the chain-rule-compatibility structure of the medium.

Photonic-crystal and metamaterial effects arise when periodic or engineered ρ structures produce null-chain dispersion relations with band gaps, negative group velocities, or topological chirality — all ED-level features of the ρ-structured medium.

### 5.5 Mass and gravitational coupling

Mass density in ED is the ρ-component restricted to chains whose update rules yield localized, persistent cores (particles). Mass as a coupling constant to gravity in the thick regime is the ρ-magnitude those cores contribute to the ambient ρ field, hence to ∇ρ, hence to the effective geodesic structure other chains follow.

The equivalence principle — inertial and gravitational mass are the same — is automatic in ED: both are ρ-contributions of the same chain-structure, measured once as "how much ρ does the chain contribute" and once as "how much ρ gradient does the chain follow." Same quantity, two roles.

### 5.6 Saturation-end phenomenology (inflation end, baryogenesis)

At the end of inflation, ρ reaches saturation over large regions. Beyond saturation, the participation-graph topology changes: new micro-events cannot be added without disrupting existing adjacency. The resulting relaxation — ρ flowing from over-saturated to under-saturated regions — is the preheating / reheating transition in cosmological terms.

The chain-survivability filter during this relaxation is what selects the observed matter content (Primitive 03 §7.4). This is the structural origin of baryogenesis in ED, and it plugs directly into the η-derivation program.

---

## 6. Simulator / PDE Instantiation

### ED in the ED-Arch simulator

- `ρ(x, t)` is the primary evolving field. Each lattice site has a numerical value updated each step via the Scenario E rule.
- The γ-sweep (ED-Arch-08) modulates how ρ concentrates into cores vs. spreads across the lattice. Higher γ = stiffer ρ concentration, sharper architectural quantization.
- Radius spectra, orbit-distance studies, scattering-grid: all are ρ-field measurements of emergent chain dynamics.
- 64² and 128² lattices: ρ is stored and updated at each of 4096 or 16384 sites. This is the concrete operational instantiation of Primitive 05 at simulation scale.

### ED in the Q-C Boundary PDE

The PDE evolves ρ along a chain's trajectory. The effective channel weight:

`D(x) = F(ρ(x), ∇ρ(x), b(x), ...)`

with `F` being the specific functional derived from the PDE structure. `D = 0.5` is the critical value; `D < 0.1` and `D > 0.5` define the thin and thick regimes respectively.

Concrete numerical predictions — N_osc ≈ 9 at D < 0.1, Q ≈ 3.5 at critical, 3–6% third-harmonic — are features of ρ-field evolution across the transition. The PDE layer is directly the evolution of Primitive 05 (with Primitive 04 as the coupling) along the chain parameterization.

### What's missing

- **Explicit derivation of D(x) from (ρ, b).** The PDE effectively uses D as the primary variable, but the underlying functional connecting D to ρ and b hasn't been written out in full. Phase 2 task.
- **ρ conservation laws.** In what regimes is ρ strictly conserved, and in what regimes is it sourced (from new participation structure forming) or sinked (via decoherence to non-trackable environmental modes)? Needs explicit flux / continuity structure.
- **Cosmological ρ dynamics.** The ED-Arch simulator is microscale; a cosmological-scale ρ evolution engine (for inflation-end, baryogenesis, structure formation) does not yet exist. Phase 4 infrastructure.

---

## 7. Open Questions

1. **Coarse-graining threshold.** At what participation-graph density does discrete count robustly support the continuum ρ(x) description? Important for knowing where ED's PDE predictions are trustworthy vs. needing the discrete underlying description.

2. **Saturation constant ρ_max.** Universal structural constant or regime-dependent? If universal, it's a fundamental ED parameter on par with the bandwidth normalization to ℏ. If regime-dependent, it's an effective quantity that varies with participation topology.

3. **ρ vs. bandwidth functional.** Given a participation graph with edge weights, `ρ` (vertex count) and `b` (edge-weight distribution) are tightly coupled but not identical. What's the full functional relationship? Needed to complete the (ρ, b) coarse-graining.

4. **The η thread — ρ form.** η = ρ_baryon / ρ_photon after the saturation-relaxation transition. Deriving it from first principles requires a dynamical ρ-evolution model of the saturation transition with chain-survivability filtering. **Phase 4 priority.**

5. **ρ-flux as current.** Standard PDE formulations of ρ-dynamics carry a current `j = ρ v` that is not explicit in the current ED memos. Making this explicit aligns the ED PDE with standard field-theory tools and clarifies conservation structure.

6. **Connection to QFT vacuum ρ.** QED's zero-point energy density is formally infinite without regularization; ED's vacuum ρ is finite and small but non-zero. How the two descriptions reconcile — what ED regularization looks like, and whether it predicts a specific vacuum ρ value — connects to the cosmological constant problem. Phase 4 target.

7. **ρ and holography.** Area-law entropy suggests that the maximum ρ a region can contain scales with boundary area, not volume. In ED terms, this is a constraint that ρ saturation is area-bounded (via participation-bandwidth bottleneck structure at horizons). Making this explicit is a route to the ED account of holographic bounds.

---

## 8. Citation format

> *Per `quantum/primitives/05_event_density.md` §1* — for ED as scalar count-measure.
> *Per `quantum/primitives/05_event_density.md` §2* — for the paired state (ρ, b) as coarse-grained substrate.
> *Per `quantum/primitives/05_event_density.md` §5.3* — for the η-derivation framing in ρ terms.
> *Per `quantum/primitives/05_event_density.md` §5.6* — for saturation-end phenomenology.

---

## 9. One-line summary

> **Event density ρ is the scalar count-measure of accumulated micro-events per region. Paired with participation bandwidth b, (ρ, b) is the full coarse-grained state of the participation graph and the substrate on which every continuum ED description — including the Q-C Boundary PDE, the gravitational-potential account, and the η-derivation path — is built.**
