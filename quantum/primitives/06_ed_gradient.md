# Primitive 06 — ED Gradient

**Role in the framework:** The first geometric object in ED. Where Primitives 01–05 establish the scalar and relational substrate, Primitive 06 introduces direction. An ED gradient is the vector field `∇ρ` (together with its bandwidth-weighted refinement) that describes how event density varies across the participation-adjacency neighborhood. It is the first primitive that carries an arrow — a local direction of increase, a slope, a polarity. Everything in ED that *moves*, *flows*, *bends*, or *curves* in the thick-regime descriptions does so because ∇ρ is non-zero. Gravity, diffusion, chain deflection, structure formation, early channel formation — all ride on this one primitive.

**Status:** First-pass canonical draft. 2026-04-24.

---

## 1. Definition

**The ED gradient** is the local vector field describing the direction and magnitude of event-density variation across participation adjacency. In the continuum: `∇ρ(x)`. In the discrete graph: the weighted difference operator on ρ across adjacent vertices.

An ED gradient is the first ED quantity that has direction. It converts the participation adjacency structure (undirected at the level of bare relation, Primitive 03) plus the scalar ρ field (Primitive 05) into a directed structure on the manifold.

### What ∇ρ *is*

- **A local vector field on the emergent manifold.** Defined where the coarse-graining threshold is crossed; smooth in thick-regime regions.
- **The first geometric ED object.** Primitives 01–05 are count-like or edge-like. ∇ρ introduces direction.
- **The driver of flow.** Chains propagate through participation structure by following gradient-directed bandwidth-preferential paths. Absent ∇ρ, there is no preferred direction; chains diffuse.
- **The local expression of participation shape.** ED-10 repeatedly talks about the "shape of participation." The explicit mathematical object of that shape, at leading order, is ∇ρ. At higher orders it is the second and higher derivatives — curvatures, which ED builds from ρ in the thick regime.

### What ∇ρ is *not*

- **Not a force.** Per Primitive 03, forces don't exist at the ED base. ∇ρ is a structural field; the apparent "force" on a chain is the thick-regime accounting of why bandwidth-preference makes the chain's trajectory curve. Gravity is the paradigm case (§5.1).
- **Not a field in the QFT sense.** Standard QFT fields are operator-valued distributions on a pre-existing manifold. ∇ρ is a classical vector field on the emergent manifold; QFT fields arise from the chain-mode decomposition of ED dynamics in the thin regime (Phase 2 Path A task).
- **Not a gauge potential.** Although gauge-like bookkeeping re-emerges downstream (Primitive 03 §7.2 on the Aharonov-Bohm interpretation), ∇ρ is the raw gradient of a scalar. It is physical and coordinate-covariant; a true gauge potential is an additional structure that will need its own treatment (in Primitive 13 or a dedicated memo on U(1)).
- **Not the same as tension.** Tension polarity (Primitive 09) is the phase relation between a chain's update rule and the local gradient direction. ∇ρ is the gradient itself; tension is how a chain's rule sits relative to it. These are related but distinct — see §3.

### Gradient magnitude and saturation

The *magnitude* |∇ρ| has a natural structural meaning: it is the local rate at which ρ changes per unit participation-adjacency distance. Small |∇ρ| = smooth region, mostly uniform ρ. Large |∇ρ| = steep ρ variation, approaching saturation-relaxation dynamics. As |∇ρ| approaches a critical structural value, the participation graph enters regimes where commitment events (Primitive 11) become selective — this is the structural origin of baryogenesis-type selection.

---

## 2. Mathematical Object

### Continuum version

`∇ρ : M → TM`

A vector field on the emergent manifold. Components in a local chart:

`(∇ρ)_i = ∂ρ/∂x^i`

where the coordinates `x^i` are themselves emergent from participation adjacency (ED-10 §3).

In the presence of bandwidth structure `b(x)`, the natural covariant gradient uses `b` as the inverse metric:

`(∇^b ρ)^i = b^{ij}(x) ∂_j ρ`

where `b^{ij}` is the bandwidth-kernel inverse — the metric-like object that participation bandwidth produces in the thick regime (ED-10 §3.2 establishes that bandwidth adjacency *is* the metric tensor in the large-scale limit).

So the physically relevant gradient is not the bare ∂ρ but the bandwidth-weighted gradient `b^{ij} ∂_j ρ`. This is the quantity that drives physical flows.

### Discrete version

For a participation graph `G = (V, E, w = b)` and scalar `ρ : V → ℕ`:

The gradient is an edge-valued quantity:

`(∇ρ)_{uv} = b_{uv} · (ρ(v) - ρ(u))`

Each edge carries a signed bandwidth-weighted ρ difference. The edge-level gradient field is the full discrete object; the continuum vector field is its coarse-graining.

### Higher-order geometry

Once ∇ρ is on the table, the full hierarchy of geometric objects follows:

- **First derivative:** `∇ρ` — direction of ρ increase
- **Second derivative (Hessian):** `∇∇ρ` — ED-curvature tensor; in the thick regime this couples to the Ricci-like tensor in the ED account of GR
- **Laplacian:** `∇²ρ = ∇·∇ρ` — source-sink structure; diffusion of ρ
- **Higher-order:** Cotton-like tensors, Weyl-like structure — for ED's treatment of gravitational radiation, tidal effects, and the full non-linear geometry

These higher-order objects are already partly developed in the GR-SC work (GR-SC 1.0+ arc). GR-SC 1.0a-1.3 treat the ED analog of curvature-invariant taxonomy, with κ ≈ 0.001766 as the post-F3-verify central value for the coupling between ED-curvature and matter-chain ρ.

### What is *not yet* settled

- **Proper formalization of the emergent-metric ↔ bandwidth-kernel relation.** ED-10 asserts the metric is built from bandwidth; the explicit formula `g_{ij} ~ b_{ij}^{-1}` is the right leading-order relation but the subleading corrections have not been rigorously derived. Phase 2 Path B task.
- **Relationship to the Riemann-like curvature.** `∇∇ρ` is a tensor, but the ED analog of the full Riemann tensor likely involves mixed derivatives of both ρ and b. The GR-SC 1.0+ arc is the empirical investigation of this; the formal synthesis is Phase 2.
- **Regimes where ∇ρ is ill-defined.** At commitment events, ρ changes discontinuously; ∇ρ is not well-defined at the event itself. The right treatment is a jump-condition formalism that matches onto a smooth ∇ρ outside the event. Needs explicit treatment.

---

## 3. Relations to Earlier Primitives

### Upstream dependencies

| Primitive # | Role |
|---|---|
| 01 Micro-event | The vertices whose count-field is differentiated |
| 03 Participation | Adjacency defines what "neighboring region" means, hence what a gradient is taken across |
| 04 Participation bandwidth | The kernel b(x) provides the metric for the physically relevant gradient `b^{ij} ∂_j ρ` |
| 05 Event density | The scalar field whose gradient is taken |

∇ρ is the first primitive that genuinely composes the earlier ones: it requires 01 (vertices), 03 (adjacency), 04 (kernel/metric), and 05 (scalar) all at once. This is why it is the first geometric object.

### Downstream

| Primitive # | How it uses ∇ρ |
|---|---|
| 07 Channel | Channels form preferentially along ∇ρ-aligned paths in the early stages; ∇ρ is the scaffolding for channel nucleation |
| 08 Multiplicity | Multiplicity depends on local |∇ρ|; smooth regions admit more channels, steep regions admit fewer |
| 09 Tension polarity | Polarity is the phase of a chain's rule against the local ∇ρ direction |
| 10 Individuation | The boundary of a distinct system is where ∇ρ between the system and its exterior exceeds the individuation threshold |
| 11 Commitment | Commitment events preferentially occur at local ρ maxima or along specific ∇ρ configurations; the PDE saturation condition is a ∇ρ-magnitude condition |
| 12 Thickening | Thickening accumulates along regions where ∇ρ stabilizes a configuration |
| 13 Relational timing | The rhythm of ρ updates respects ∇ρ structure; phase propagation follows gradient-defined directions |

### Circular-definition flags

1. **"Thick regime"** in §1 leans on Primitive 12 (Thickening) for its formal definition. Used here operationally as "where ρ is smooth enough for ∇ρ to be well-defined."
2. **"Emergent manifold"** — the manifold itself is an ED-10-level emergent structure from participation adjacency. The gradient lives on it, which means ∇ρ is well-defined only in regimes where a manifold exists. In pre-manifold regimes (deep UV, near-saturation), one must use the discrete edge-gradient form.
3. **"Critical structural value"** in §1 — the exact saturation threshold. Phase 4 target to pin down.

---

## 4. Measurable Signature

### Direct observable consequences

- **Gravitational acceleration.** `g = -∇Φ`, where Φ is the Newtonian potential. In ED, Φ ∝ ρ (at leading order) and `g = -∇Φ ∝ -∇ρ`. Gravitational acceleration is directly the ED gradient in the thick weak-field regime (ED-10 §7.2).
- **Gravitational redshift, lensing, time dilation.** All derived from the emergent metric, which is built from the bandwidth kernel which is built from the participation structure which is tightly coupled to ρ. Every GR observable has an ED-gradient origin.
- **Chain deflection / geodesic motion.** A test chain (non-self-gravitating) follows bandwidth-preferential paths in the (ρ, b) landscape; in the thick regime this is geodesic motion in the emergent metric.
- **Cosmological large-scale structure.** Galaxies, clusters, voids — all are ρ-density peaks and troughs. Structure formation is the nonlinear evolution of ∇ρ starting from a near-uniform initial condition with small fluctuations.
- **Refractive bending of light in an inhomogeneous medium.** Null chains propagate through ρ structure; the effective bending is a ∇ρ-dependent null-geodesic.
- **Diffusion-like transport.** In regimes where ρ is not yet organized into chains, ρ-transport follows a Laplacian-plus-drift equation whose drift term is ∇ρ itself — a classical diffusion pattern emerging from the structural gradient.
- **GR-SC curvature observables.** The entire GR-SC arc is empirical testing of ∇ρ-derived curvature structure in the simulator. κ, pooled-R2, GR-SC 1.7/1.8 clearances are all ∇ρ (and higher-order) measurements.

### Indirect consequences

- **Structure of the CMB power spectrum** — imprinted at recombination by the ∇ρ field at that epoch
- **Galaxy-cluster mass profiles** — inferred through lensing, which reads ∇ρ
- **Rotation curves** — set by ∇ρ at galactic scales (the dark-matter question is whether there is additional ρ that needs accounting for, and in ED it is naturally present in the diffuse chain-structure around galaxies)
- **Baryogenesis selectivity** — selection operates where |∇ρ| crosses the saturation threshold

### Operational handle

- **ED-Arch simulator.** `∇ρ(x, t)` is directly computable from the lattice field at each time step. Core stability is a local-∇ρ-structure property. Core-core interactions are ∇ρ-interaction events.
- **GR-SC 1.0+ simulator.** Built specifically to test ∇ρ-derived curvature observables. κ, pooled-R2, F2–F4 investigations are all ∇ρ-related measurements.
- **Q-C Boundary PDE.** The D(x) functional includes ∇ρ sensitivity; large |∇ρ| regions are where D crosses into committed regime.

---

## 5. Example Applications

### 5.1 Gravity as ∇ρ

A massive chain contributes to ρ around it. At distance, the ρ-contribution falls off with a specific distance kernel that in the thick regime reproduces the Newtonian 1/r potential at leading order. The gradient ∇ρ points toward the chain; any test chain moving through this region experiences bandwidth-preferential paths that curve toward the source.

Gravitational acceleration = -∇Φ in standard physics. In ED: `g ~ -∇ρ / ρ_scale` (at leading order, with ρ_scale a structural normalization tying ρ-gradients to standard acceleration units). The equivalence principle is automatic because both inertial response and gravitational coupling come from the same chain contribution to ρ.

Curved-spacetime GR arises at higher order: the full emergent metric is built from the bandwidth kernel, the Riemann-like curvature from second-order ρ / b structure, and the nonlinear Einstein-like equations from the self-consistent relation between ρ source and bandwidth kernel. GR-SC 1.0+ is the empirical investigation of this correspondence at simulator scale.

### 5.2 Structure formation and the cosmic web

The early universe has small-amplitude ρ fluctuations on a nearly uniform background. ∇ρ is tiny; dynamics are nearly linear. Over time, gradients amplify: regions slightly above average pull chains inward, slightly below push them outward. Nonlinear structure develops — galaxies at ρ peaks, filaments along ridges of ∇ρ, sheets and voids at lower-ρ regions.

The cosmic web is the large-scale organized ∇ρ structure of the universe. ED-I Chronicle scores the cosmic-web entry at 5.0/5 — this is why: the entire thing is a ∇ρ pattern.

### 5.3 Channel nucleation along gradient

At the earliest stages of channel formation (the precursor to Primitive 07), a proto-channel emerges as a locally coherent bandwidth-preferred path aligned with the local ∇ρ. Gradient direction provides the initial axis; bandwidth structure fills in the channel around it.

This is why many channels, especially in condensed-matter contexts, have a natural orientation aligned with the local ρ-gradient: the gradient seeded the channel. In isotropic regions without ∇ρ, channel formation is isotropic. In strongly-gradient regions (interfaces, boundaries, strong external fields), channels orient along the gradient direction. ED-I-12 (photonics) and ED-I-23 (Josephson) both use this principle implicitly.

### 5.4 Saturation and baryogenesis selection

When local ρ approaches ρ_max, ∇ρ near the saturation boundary becomes large. Commitment events at this boundary are selectively filtered: only chains whose update rule is phase-aligned with the local ∇ρ direction can commit without bandwidth overflow. Anti-aligned rules require bandwidth arrangements inconsistent with the saturated ρ.

The matter-antimatter asymmetry follows: in the post-inflationary saturation phase, aligned-tension chains (matter) could instantiate; anti-aligned chains (antimatter) mostly could not. The surviving-chain ρ at the end of the transition is baryon ρ; the committed non-surviving micro-events remain as photon ρ. The ratio is η.

Phase 4 priority: derive η quantitatively from this ∇ρ-threshold selection. Structurally the story is clear; the number is the open target.

### 5.5 Gravitational-wave-like propagation

A propagating perturbation in ρ and b, supported by specific second-order ∇ρ structure, propagates at the bandwidth-limit speed c (Primitive 03 §5.4). These perturbations — the ED analog of gravitational waves — carry transverse-traceless information about ρ-distribution changes at the source.

LIGO observes them. ED reproduces the same phenomenology because the thick-regime equations for small ρ / b perturbations are the same as linearized GR in the relevant limit. The GR-SC arc investigates how well the full nonlinear correspondence holds in the simulator.

### 5.6 Tension, polarity, and the link to Primitive 09

Primitive 09 (Tension polarity) will define the phase of a chain's update rule against the local gradient. The hook is right here: ∇ρ is the *direction* that matters. A chain whose rule is phase-aligned with ∇ρ has positive tension polarity; a chain whose rule is phase-opposed has negative polarity. This is the structural property that differentiates matter from antimatter, and is the reason Primitive 06 needs to be in place before 09 can be cleanly stated.

---

## 6. Simulator / PDE Instantiation

### ∇ρ in ED-Arch

- Computed directly from lattice ρ via finite differences at every time step
- Drives core motion: a core's center-of-ρ drifts in response to ambient ∇ρ
- Determines core-core interaction direction: two cores "pull" or "push" according to the shape of ∇ρ between them
- The γ-sweep modulates how sharply ∇ρ concentrates near cores; high γ = sharply localized ∇ρ ridges around each core

### ∇ρ in the GR-SC simulator

- The GR-SC 1.0+ arc is specifically built to measure ∇ρ-derived curvature observables in the simulator
- κ ≈ 0.001766 (post-F3-verify) is the central value of the ED-curvature coupling
- GR-SC 1.7, 1.8 clearances bound the matter-chain contribution `|N̂'|` via ∇ρ-derived quantities
- F2, F3, F4 investigations are all probing the same underlying ∇ρ and its higher-order structure

### ∇ρ in the Q-C Boundary PDE

- D(x) has a ∇ρ-sensitivity in its defining functional: large |∇ρ| regions are where commitment selection becomes efficient
- The critical transition D = 0.5 corresponds to a specific ∇ρ-magnitude threshold in the chain's local environment
- N_osc ≈ 9 at low D is a ∇ρ-rigid regime; the chain explores many channel options because ∇ρ hasn't forced a selection

### What's missing

- **Explicit ∇ρ → emergent metric formula.** ED-10 asserts the metric comes from bandwidth; precise derivation including ∇ρ corrections beyond leading order is Phase 2 Path B work.
- **Jump-condition formalism at commitment events.** ∇ρ is ill-defined at discrete events; need matching conditions to keep the continuum description consistent across events.
- **∇ρ-induced channel-nucleation formalism.** Mentioned in §5.3; no explicit rule yet for how ∇ρ seeds a channel.

---

## 7. Open Questions

1. **Bandwidth-weighted vs. bare gradient.** The physically relevant object is `b^{ij} ∂_j ρ`, not plain `∂_j ρ`. What is the precise functional `b^{ij}` for given participation-graph structure? This pins down the emergent-metric formula. Phase 2 Path B target.

2. **Saturation threshold |∇ρ|_crit.** The critical gradient magnitude at which commitment selection engages. Universal structural constant or regime-dependent? Ties to the η derivation at Phase 4.

3. **Riemann-like ED tensor.** The full second-derivative structure of (ρ, b) gives an ED analog of Riemann curvature. The GR-SC 1.0+ program is the empirical probe; the formal synthesis — showing the ED second-order tensor reduces to Riemann in the thick regime — is Phase 2.

4. **Tension polarity formalism.** Primitive 09 will formalize polarity as the phase of a chain's rule against ∇ρ. The detailed phase structure — discrete or continuous, stabilized by what mechanism — is the key open question for 09.

5. **∇ρ in cosmological simulators.** Existing ED-Arch and GR-SC simulators are microscale. A cosmological ∇ρ-evolution simulator for structure formation and baryogenesis is Phase 4 infrastructure. Required to produce the η number.

6. **Gauge-like structure from ∇ρ.** The ED-I-14 account of Aharonov-Bohm suggests non-trivial global participation topology produces gauge-like phases. Whether this is a ∇ρ-level phenomenon or requires explicit higher-primitive structure (Primitive 13 + dedicated U(1) memo) is open.

7. **Non-geometric regimes.** Near saturation, in black-hole-interior-like regions, the emergent manifold picture breaks down. ∇ρ still exists as a discrete edge quantity but the continuum interpretation fails. Treatment of these regimes needs explicit non-geometric language — a direction the ED-10 scope-closure work already guardrails.

---

## 8. Citation format

> *Per `quantum/primitives/06_ed_gradient.md` §1* — for ∇ρ as the first geometric ED object.
> *Per `quantum/primitives/06_ed_gradient.md` §2* — for the bandwidth-weighted gradient `b^{ij} ∂_j ρ`.
> *Per `quantum/primitives/06_ed_gradient.md` §5.1* — for gravity as thick-regime ∇ρ.
> *Per `quantum/primitives/06_ed_gradient.md` §5.3* — for ∇ρ-driven channel nucleation.
> *Per `quantum/primitives/06_ed_gradient.md` §5.4* — for ∇ρ-threshold baryogenesis selection.

---

## 9. One-line summary

> **The ED gradient ∇ρ is the first geometric object in the framework — the direction and magnitude of ρ variation across participation adjacency. Weighted by bandwidth, it supplies the emergent metric; as a structural quantity it drives gravity, structure formation, channel nucleation, and the saturation-threshold selection rule behind baryogenesis.**
