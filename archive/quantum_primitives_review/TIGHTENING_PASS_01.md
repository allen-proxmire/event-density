# Tightening Pass 01 — Primitive-Stack Audit

**Date:** 2026-04-24
**Scope:** Primitives 01–13, as drafted in the single-session Phase 1 pass on 2026-04-24.
**Status:** Audit document, not a rewrite. Findings are organized as a diff against the current state of the stack. Structural-fix prioritization in §7.
**Purpose:** Identify every inconsistency, circular dependency that can now be resolved, PDE-parameter drift, overclaim, missing mathematical commitment, and PDE-layer gap that stands between the primitive stack and execution of either Path B (QM as thin-regime effective theory) or Path C (Arndt-style retrodiction).

---

## 1. Definition drift across primitives

Actual places where a term's meaning or load shifts between where it is introduced and where it is used downstream. This is the single most important class of finding; it is also the most correctable.

### 1.1 Participation bandwidth — framing shift between 03 and 04

- In **Primitive 03 §1**, participation bandwidth is introduced as "the *measure* of participation — how rich the relation is."
- In **Primitive 04 §1**, bandwidth becomes "inherently comparative," and §1 introduces a **four-band decomposition** (internal rule-bandwidth, adjacency, environmental, commitment-reserve) as a structural claim.
- The four-band structure is not retroactively visible in 03. 03 §5.6 describes superposition persistence as "low participation bandwidth with environment," but "bandwidth with environment" is actually `b_env` in 04's vocabulary, not a single scalar.
- **Drift:** 03 treats bandwidth as a single relational scalar; 04 treats it as a partition across four bands. Both are consistent — but the reader who processes 03 before 04 builds a thinner mental model.
- **Fix:** Add one sentence to 03 §1 pointing forward to the four-band refinement in 04. Do not backport the full four-band structure into 03 — keep 03 at the relational level.

### 1.2 Channel — "stable pattern" (03) vs. "rule-type-selective infrastructure" (07)

- **Primitive 03 §1** calls channel "a stable pattern in participation."
- **Primitive 07 §1** makes channel "rule-type-selective" — admitting chains with rule-types compatible with its structure and excluding incompatible ones.
- The rule-type-selective property is load-bearing for 07's entire account (neutrino oscillation, photonic band structure, Josephson channels). It is not even hinted at in 03's gloss.
- **Drift:** 03's gloss is strictly weaker than 07's definition. A reader using 03's gloss to interpret 05 or 06 will miss the rule-type-discrimination structure that later primitives rely on.
- **Fix:** 03 §1's mention of channel should read "a stable rule-type-selective pattern in participation (formalized in 07)."

### 1.3 Commitment order — asserted in 01/03, not instantiated in 11

- **Primitive 01 §2** asserts: "Directed edges (a subset) = commitment order."
- **Primitive 03 §2** repeats: "Commitment ordering (part of Primitive 11) gives us the direction on the subset of edges that are ordered."
- **Primitive 11 §2** defines commitment as *"the discrete selection of a single channel... together with the addition of a new micro-event"* — i.e., a vertex-addition event. It does not formalize "commitment order" as an edge-direction field.
- **Drift:** 01 and 03 promise that 11 will supply an edge-directionality structure. 11 delivers an event-sequence structure instead. These are related (event order induces edge order between successive vertices along a chain) but not identical. A chain's internal edge order is well-defined; cross-chain commitment ordering across the whole graph is not formalized anywhere.
- **Fix:** Either (a) 11 adds an explicit sub-section defining global commitment ordering on the participation graph, or (b) 01/03 narrow the claim to "per-chain commitment ordering." Option (b) is safer because global commitment ordering gets entangled with relativistic simultaneity (ED-10's scope).

### 1.4 Saturation — three different framings across 05, 06, and 09

- **Primitive 05 §1** frames saturation as ρ-magnitude: "there is a maximum ρ a region can sustain before saturation dynamics change the update behavior."
- **Primitive 06 §1** frames saturation as |∇ρ|-magnitude: "as |∇ρ| approaches a critical structural value, the participation graph enters regimes where commitment events become selective."
- **Primitive 09 §1** invokes "saturated ED-flow" as the regime for polarity selection, combining both framings without explicit commitment.
- **Drift:** ρ-saturation and |∇ρ|-saturation are not equivalent. A uniformly high-ρ region has small |∇ρ|; a steep-∇ρ region may have moderate ρ at both endpoints. Whether the baryogenesis-selection mechanism operates on ρ, |∇ρ|, or a joint condition is a substantive Phase 4 question that the primitive stack currently obscures.
- **Fix:** 05 §1, 06 §1, 09 §1 need a shared reference to a definition of "saturation" that commits to the joint condition (most likely: *region entering the ρ-band where `ρ → ρ_max` AND the `|∇ρ|`-band where the commitment-selection rate becomes polarity-sensitive*). Until Phase 4 resolves the quantitative form, the primitive stack should label this as **the saturation condition** with an explicit cross-reference rather than using three unaligned framings.

### 1.5 Rule vs. rule-type — term introduced in 07, used retroactively in 02 and 09

- **Primitive 02** uses "update rule" without committing to rule-types as a discrete classification. Rules can be "compatible" with channels (§3 circular flag) but the taxonomy is not established.
- **Primitive 07 §1** introduces "rule-type `τ`" as "a label drawn from a finite (structurally determined) set of compatible rule-classes" — a discrete-classification claim.
- **Primitive 09** treats polarity as operating at the rule level but slides between "rule" and "rule-type" in §1–§5.
- **Drift:** The rule-type classification is structurally large — it is the ED analog of the particle-species inventory. Introducing it at 07 without backporting to 02 leaves it unclear whether every chain has a rule-type label (is rule-type an intrinsic chain attribute?) or whether rule-type is a channel-level attribute that chains of compatible rule inherit.
- **Fix:** 02 should be tightened to commit explicitly: **a chain has a rule; the rule has a rule-type label drawn from the structurally permitted set (formalized in 07)**. Polarity (09) is then a phase attribute on the rule, not on the rule-type.

### 1.6 Thick regime / thickened — vocabulary-circular between 06 and 12

- **Primitive 06** uses "thick regime" operationally as "where ρ is smooth enough for ∇ρ to be well-defined."
- **Primitive 12** defines "thickening" as the *process* producing thick-regime conditions.
- **Drift:** "Thick regime" is used before 12 formalizes "thickening," with the implicit meaning "the regime that thickening produces." This is structurally unavoidable given the ordering, but it should be flagged explicitly in 06 (and 05 §1, and 01 §7) to acknowledge the forward-reference.
- **Fix:** Small. Every primitive that uses "thick regime" before 12 should carry a one-line footnote: "thick regime here is operational; the process producing it is formalized in Primitive 12."

### 1.7 Emergent manifold — diffuse across 03, 05, 06, 13 with no single owner

- **Primitive 03 §1** says participation has "geometric potential" producing manifolds in the thick regime.
- **Primitive 05 §2** uses "the emergent manifold" as an established object.
- **Primitive 06 §1** acknowledges pre-manifold regimes and mentions the continuum description requires participation to be dense enough for manifold structure.
- **Primitive 13 §1** derives time as a coordinate on the manifold.
- **Drift:** No single primitive is responsible for "emergent manifold." It is referenced as if it were settled by 03 but is actually jointly produced by 03 (adjacency) + 04 (metric via bandwidth kernel) + 12 (thickening threshold). No explicit construction exists.
- **Fix:** This gap is larger than a tightening-pass fix can solve. It is a candidate for its own Phase 2 memo: `quantum/effective_theory/emergent_manifold_construction.md`. For the tightening pass, flag it in every affected primitive (§8 of each) as a joint-primitive dependency pending Phase 2.

---

## 2. Circular-dependency flags that can now be resolved

Each primitive flagged forward-references in §3 or §7. With the full stack visible, most are now resolvable — the referenced primitive exists and defines the referenced term. Remaining flags are the genuinely-open ones, not flagged-for-sequencing.

### 2.1 Resolved

| Primitive | Flag | Resolved by | Notes |
|---|---|---|---|
| 02 | "Consistent update rule" → 09 | 09 §1 ✓ | Polarity is the phase of the rule; consistency is phase-alignment with flow |
| 02 | "Coherence condition" → 07 | 07 §1–§2 ✓ | Channel stability + bandwidth coherence condition |
| 02 | "Chain's identity distinct from other chains" → 10 | 10 §1 ✓ | Bandwidth-ratio threshold |
| 02 | "Chain termination" → 11 + 12 | 11 §5.4, 12 §1 ✓ | Commitment event types + thickening-state endpoint |
| 03 | "Integration" → 04 | 04 §1 ✓ | Bandwidth measures integration richness |
| 03 | "Participation structure has shape" → 06 + 07 | 06 §1 + 07 §1 ✓ | Gradient direction + channel structure |
| 04 | "Coherence" → 07 | 07 §1 ✓ | Bandwidth-preservation along channel |
| 04 | "Commitment-reserve" → 11 | 11 §3 circular-flag #1 ✓ | Mutual resolution now explicit |
| 04 | "Environment" → 10 | 10 §1 ✓ | Boundary bandwidth below individuation threshold |
| 05 | "Region" → 03 | 03 §1 ✓ | Participation-adjacency neighborhood |
| 05 | "Coarse-graining" → 12 | 12 §1 ✓ | Thickening threshold sets continuum validity |
| 07 | "Superposition" → 08 + 10 + 11 | 08 §1 + 11 §1 ✓ | M > 1 pre-commitment state |
| 08 | "Commitment" → 11 | 11 §1 ✓ | Event that reduces M |
| 09 | "Flow direction" → 06 | 06 §1 ✓ | ∇ρ direction |
| 09 | "Anti-aligned decoherence" → 11 | 11 §5.2 ✓ | Environmental-forced commitment sequence |

### 2.2 Still open after tightening — these are genuine unresolved questions

| Primitive | Flag | Nature of remaining gap |
|---|---|---|
| 01 §7 | Graph vs. hypergraph vs. simplicial complex | Mathematical-structure choice (see §5.1 below) |
| 01 §7 | Countability connection to η | Phase 4 derivation target |
| 06 §7 | Critical |∇ρ|-threshold value | Phase 4 quantitative |
| 07 §7 | Rule-type taxonomy | Phase 2 derivation target |
| 07 §7 | Channel-space metric | Phase 2 Path A target |
| 07 §7 | Stability-condition formalism | Open; needs spectral-gap or Lyapunov-type criterion |
| 08 §7 | D–M_eff functional relationship | **Cross-primitive inconsistency — see §3 below** |
| 09 §7 | Rule-phase coordinate | Tied to rule-type taxonomy (07) |
| 11 §7 | Born rule derivation | Phase 2 target; depends on bandwidth-composition rule (04 open) |
| 04 §7 | Additive vs. sublinear bandwidth composition | **Load-bearing for Born rule and interference — see §5.2 below** |
| 05 §7 | ρ-saturation value ρ_max | Universal vs. regime-dependent; ties to η |
| 13 §7 | Emergent-time derivation | Phase 2 target |

### 2.3 Meta-observation on circular-flag resolution

The sequential drafting produced **fifteen forward-reference flags that are now cleanly closed** and **twelve that remain open on substantive grounds**. The ratio is good — it means the sequencing was largely correct. The twelve remaining opens cluster into three buckets: mathematical-structure commitments (§5), PDE-layer gaps (§6), and genuinely-Phase-4 quantitative targets. That cluster pattern is the tightening pass's clearest positive signal that the stack is coherent.

---

## 3. PDE-parameter drift

This is the class of findings most directly relevant to Arndt-retrodiction blockers. The canonical PDE parameters are `D, H, ζ, τ, P_0, M_0` (per the D_crit resolution memo and the Dimensional Atlas). The primitives gesture at `D` in three inconsistent ways and ignore the rest.

### 3.1 `D` has three different functional definitions across primitives

- **Primitive 04 §6:** `D(x) = b_dominant_channel(x) / b_total(x)` — a simple ratio of leading-channel bandwidth to summed bandwidth.
- **Primitive 07 §6:** `D(x)` is "the channel-dominance variable along a propagating chain" — conceptually similar to 04 but no explicit formula.
- **Primitive 08 §2:** `D ≈ 1/M_eff` where `M_eff = (Σ b_K)² / Σ b_K²` is the participation-ratio functional.

These definitions are **not equivalent.** Worked example: bandwidth distributed across three channels as (0.90, 0.05, 0.05) of total:
- 04's formula gives `D = 0.90`
- 08's formula gives `M_eff = (1.0)² / (0.8125 + 0.0025 + 0.0025) = 1.227`; `D ≈ 1/1.227 ≈ 0.815`

The two agree at the limits (D = 1 at full concentration, D → 0 at maximal spread) but differ by ~10% in generic cases. At the Q-C boundary itself (D ≈ D_crit), the difference could be large enough to shift `x_c` predictions meaningfully.

**Fix (§7 priority 2):** Commit to a single functional form. The participation-ratio form (08) is standard in statistical physics, dimensionally clean, and matches how "effective number of channels" is normally computed. 04 §6 and 07 §6 should be amended to match.

### 3.2 `H`, `ζ`, `τ`, `P_0`, `M_0` — never mapped to primitive-level quantities

The canonical PDE is `∂_t ρ = D · F[ρ] + H · v` with `F[ρ] = M(ρ) ∇²ρ + M'(ρ) |∇ρ|² − P(ρ)`. The six parameters:

- `D` — channel weight (gestured at; inconsistently, see §3.1)
- `H` — participation weight (`H = 1 − D`; not discussed as a primitive-level quantity)
- `ζ` — participation damping (entirely absent from the primitive stack)
- `τ` — participation relaxation timescale (entirely absent)
- `P_0` — penalty slope at ρ* (entirely absent)
- `M_0` — mobility prefactor (entirely absent)

And the participation field `v(x, t)` in the PDE has **no primitive-level identification at all.** It is mentioned in the dimensional-atlas memo as a "Candidate" interpretation (mean-field decoherence mode, measurement back-action, or environmental coupling — all unresolved). The primitive stack does not commit to an interpretation, and different primitives would suggest different ones:

- 04's "commitment-reserve bandwidth" band is a plausible `v` candidate
- 11's commitment-rate field is another plausible candidate
- 13's relational-timing phase coupling is a third

**Fix (§7 priority 1):** Produce an explicit mapping memo linking each of the six PDE parameters and the field `v` to primitive-level objects. This is the single most load-bearing piece of Phase 2 work and is the prerequisite for the Arndt retrodiction (Blocker 1 in `quantum/retrodictions/arndt_interferometry.md`).

### 3.3 `D_crit` — stale reference across multiple primitives

- The primitives reference `D = 0.5` as the Q-C transition implicitly (via citations to the Q-C Boundary paper).
- The D_crit resolution memo (2026-04-22) retires 0.5 as a heuristic and supplies `D_crit(ζ = 1/4) ≈ 0.896`.
- No primitive explicitly cites the retirement. This means a reader of the primitive stack may carry the old value forward.

**Fix:** Every primitive that mentions the Q-C boundary or D = 0.5 should footnote the retirement. Affected: Primitives 04 §5.3, 04 §6, 05 §5, 05 §6, 07 §5.3, 07 §6, 08 §1, 08 §5.3, 08 §6, 11 §4, 11 §6.

### 3.4 ρ in the PDE vs. ρ in the primitives

- **Primitive 05 §1** defines ED as a **count-measure**: `ED(R) = |V ∩ R|`, non-negative integer at the discrete level, non-negative real in the continuum.
- **Dimensional Atlas, quantum regime** identifies ρ with **Born probability density `|ψ|²`**, which is a probability density, not a count.

These are not incompatible — count per unit volume can be interpreted as a density — but the specific identification ρ ↔ |ψ|² that the atlas relies on is a stronger commitment than Primitive 05 makes. 05 treats ρ as a count of committed micro-events; the atlas treats ρ as an amplitude-squared distribution.

**Fix:** 05 §2 should add an explicit dual-identity statement: *at the discrete graph level, ρ counts micro-events; under the quantum-regime anchoring of the Dimensional Atlas, ρ is identified with the probability density |ψ|² via Madelung.* The two are consistent once the count is normalized per unit L_0^d.

---

## 4. Overclaims — assertions exceeding what the core triad supports

Places where a primitive asserts a substantive result as if established, where the underlying derivation is actually Phase 2/3/4 work. Keeping these is fine as motivating text; the fix is to label them explicitly as aspirational rather than delivered.

### 4.1 Primitive 03 §7.2 — gauge theory from participation topology

> "what classical physics calls 'gauge potentials' are bookkeeping devices for participation-geometry topology. Making this formal — showing that U(1), SU(2), SU(3) gauge structures arise as specific participation-topology classes — would be one of the most consequential derivations in the program."

Correctly flagged as Phase 2/3 target. The concern is that §1 and §5.5 speak about topological phases as if the mechanism were in place. Tighten the §1/§5.5 language to "conjectured structural origin" rather than "structural origin."

### 4.2 Primitive 04 §5.4 — uncertainty relations derive from bandwidth allocation

> "All uncertainty relations are allocation inequalities on bandwidth partitions of a common budget, normalized to ℏ by the structural constants of the participation graph in the thick-regime limit."

This is the single strongest claim in the primitive stack. It asserts that (a) the four-band structure is mathematically forced, (b) each conjugate-variable pair corresponds to a specific partition, (c) the structural constants happen to equal ℏ/2 in the thick regime. None of these is derived. All three are open questions in 04 §7.

**Fix:** §5.4 should be re-framed as "the bandwidth-allocation hypothesis for uncertainty relations" with the three (a/b/c) claims listed as sub-conjectures. This is a high-value claim if derivable; labeling it as a hypothesis until it is derived protects the rest of the stack from a single-point failure.

### 4.3 Primitive 06 §5.1 — gravity as ∇ρ in the thick regime

> "`g ~ -∇ρ / ρ_scale` (at leading order, with ρ_scale a structural normalization tying ρ-gradients to standard acceleration units). The equivalence principle is automatic because both inertial response and gravitational coupling come from the same chain contribution to ρ."

The leading-order equivalence-principle claim is plausible but not derived. The explicit form `g ~ -∇ρ / ρ_scale` has a normalization constant `ρ_scale` that has not been anchored to `G` or to thick-regime observables. GR-SC 1.0+ measures κ ≈ 0.001766, which is an ED-level coupling — but its identification as the ρ_scale in 06 is assumed, not shown.

**Fix:** §5.1 should reference GR-SC 1.0+ explicitly and mark the ρ_scale ↔ G relationship as Path B Phase 2 work.

### 4.4 Primitive 06 §4 — gravitational observables as direct consequences

Listing gravitational redshift, lensing, and time dilation as "direct observable consequences" of ∇ρ reads stronger than is supported. These follow *if* the bandwidth-kernel-to-metric story works. Since that story is Path B work, these should be labeled "consequences conditional on Path B."

### 4.5 Primitive 11 §2 — Born rule from sublinear bandwidth composition

> "The squared-amplitude structure emerges because bandwidth composes sublinearly under channel merging... in a way that, after normalization, gives `|ψ|²` weighting. The Born rule is therefore a thick-regime emergent statement about discrete commitment selection."

The sublinear-composition claim (Primitive 04 §7 item 2) is itself open. The Born-rule derivation depends on it. Labeling the Born rule as "derived" here is premature; the honest framing is "the Born rule is expected to emerge as a thick-regime statement, via bandwidth-composition rules whose precise form is open."

### 4.6 Primitive 09 §5.1 — baryogenesis selection "a structural consequence"

> "the structural baryogenesis mechanism. It does not require new particles, enhanced CP violation, or sterile neutrinos. It requires the polarity-selection rule under saturated flow — which is a structural consequence of primitives 03, 04, 06, 09 acting together."

The mechanism is described at the level of direction (aligned rules commit, anti-aligned decohere), not executed. "Structural consequence" overstates. Honest label: "the baryogenesis-selection hypothesis is that this is a structural consequence of 03, 04, 06, 09; deriving it explicitly is the Phase 4 priority target."

### 4.7 Primitive 13 §5.3 — gravitational time dilation from bandwidth compression

Same pattern. The structural *direction* is plausible; the derivation is not in hand. Relabel as conditional on Path B.

---

## 5. Missing mathematical-object commitments

Places where a primitive gestures at a mathematical object but does not commit to a specific structure. Each of these is load-bearing for Phase 2.

### 5.1 Graph vs. hypergraph vs. simplicial complex (Primitive 01 §7, Primitive 03 §2)

Not committed. Downstream primitives operate with graph-level language but hypergraph/simplicial structure has been repeatedly gestured at (multi-particle entanglement, topological phases, gauge from topology).

**Commitment needed for Phase 2:** Pick one. The cleanest default is *simplicial complex with weighted simplices*, which natively supports the topology-from-homology story (03 §7.2, 07 §7.4). Hypergraph is a cheaper compromise. Plain graph is the weakest and likely insufficient for gauge structure.

### 5.2 Bandwidth composition — additive or sublinear (Primitive 04 §7)

Open. If additive, interference fringes cannot have bandwidth-coherence loss from just composition and require a separate mechanism. If sublinear, the Born rule's `|ψ|²` structure emerges (per 11 §2). If superlinear, something is structurally wrong.

**Commitment needed for Phase 2:** Sublinear-composition is the only form consistent with both standard QM interference visibility and the Born rule. Commit to it, specify the functional form, and derive the sublinear exponent (likely tied to the 2-in-`|ψ|²`).

### 5.3 D-functional — pick one form (primitives 04, 07, 08)

Per §3.1 above. The participation-ratio form from 08 is the recommended commitment.

### 5.4 Emergent metric from bandwidth kernel (Primitive 06 §2)

Gestured: `g_ij ~ b_ij^{-1}` at leading order. Not committed. This is Path B Phase 2's opening step.

### 5.5 Participation field `v(x, t)` in the PDE

Not identified. The three candidates listed in §3.2 above need to be adjudicated. The most defensible near-term candidate, given the polarity-selection thread running through the primitives, is probably **`v` = commitment-rate density at rule-aligned polarity** — i.e., a field measuring local commitment activity along the polarity-aligned direction. But this is speculative; needs explicit Phase 2 derivation.

### 5.6 Rule-phase coordinate (Primitive 09 §7.1)

Open. What is the coordinate on a rule's update cycle against which polarity phase is measured? Structurally, likely a connection one-form on the rule-type fiber of the participation complex — but that language presupposes the simplicial/fiber-bundle commitment in §5.1.

### 5.7 "Saturation condition" (per §1.4 drift finding)

No single primitive owns the formal saturation condition. Candidate joint form:

`saturated(x) := ρ(x) > ρ_sat AND |∇ρ(x)| > κ_sat`

with `ρ_sat` and `κ_sat` structural constants tied to η-derivation. Needs explicit commitment.

---

## 6. PDE-layer gestures without clean mapping

Places where the primitives cite PDE-level results as if derived from primitives, but where the actual bridge is missing.

### 6.1 `D(x)` as a function of experimental control parameter

Appears in 04 §6, 07 §6, 08 §1. In each case `D(x)` is treated as if the `x → D` map is well-defined. It is not — this is precisely the Arndt Blocker 1.

**Mapping required for Phase 2 execution (Path B or Path C Step 2):** Given an experimental control parameter `x` (mass, velocity, temperature, coupling rate), derive `D(x)` from (a) the bandwidth kernel `b(x)`, (b) the environmental decoherence rate `Λ(x)`, and (c) the participation-ratio functional form committed in §5.3. This derivation has not been done for any experimental system.

### 6.2 `D_crit(ζ)` — the primitive stack does not connect to it

The D_crit resolution memo gives `D_crit(ζ) = √(2-ζ)(2-√(2-ζ))`. No primitive discusses `ζ`. `ζ` is "participation damping" in the PDE; the primitive-level object most analogous would be the dissipation rate of commitment-reserve bandwidth into environmental bandwidth (Primitive 04 / Primitive 11), but this identification is not committed.

**Mapping required:** `ζ` (PDE) ↔ commitment-reserve dissipation rate (primitives 04+11).

### 6.3 `τ` (participation relaxation time) ↔ ???

No primitive-level correspondent. Plausible candidates: the chain's internal rule-period (Primitive 02 / 13), the commitment-rate inverse (Primitive 11), the relational-timing reference rhythm (Primitive 13). All three differ; none is committed.

**Mapping required:** `τ` (PDE) ↔ specific primitive-level timescale.

### 6.4 `M_0`, `P_0` — mobility and penalty prefactors

These are constitutive parameters of the PDE. The Dimensional Atlas handles them via `T_0` normalization; the primitives do not discuss them. In the quantum regime their physical units are anchored but their interpretation in terms of primitives (Is mobility a bandwidth-flow property? Is penalty a tension-polarity restoring tendency?) is not committed.

**Mapping required:** `M_0, P_0` (PDE constitutive) ↔ primitive-level interpretation.

### 6.5 Q-C Boundary distinguishing predictions — origin in primitives

`N_osc ≈ 9`, `Q ≈ 3.5`, triad ≈ 0.03, 3–6% third-harmonic. These are PDE-linearization predictions from ED-Phys-16/17/00.3. The primitive stack does not explain why these numbers take these values from a primitive-level structural argument. They are correctly attributed to the PDE as a derived consequence. What is missing is any primitive-level *structural* reason — e.g., "N_osc ≈ 9 because the commitment-rate spectrum around D < 0.1 supports 9 oscillatory modes before participation-damping absorbs them." Without that link, the distinguishing predictions are PDE-specific and not genuinely primitive-backed.

**Mapping required (Phase 2 priority):** derive at least one of the four distinguishing predictions (probably `N_osc ≈ 9` as the most tractable) from primitive-level argument.

---

## 7. Prioritized structural fixes

In order of leverage on downstream work (Path B, Path C, Phase 4).

### Fix 1 — the PDE-parameter mapping memo (**highest priority, Phase 2 critical path**)

Produce `quantum/effective_theory/pde_parameter_mapping.md` establishing the six-parameter correspondence:

- `D` ↔ (primitive-level object, using the participation-ratio form per §5.3)
- `H = 1 − D` ↔ (participation-weight at primitive level)
- `ζ` ↔ (commitment-reserve dissipation rate, per §6.2)
- `τ` ↔ (specific timescale, per §6.3)
- `M_0, P_0` ↔ (primitive-level interpretations, per §6.4)
- `v(x, t)` ↔ (specific primitive-level field, per §5.5)

This single memo unblocks Arndt Step 2, Path B opening, and Phase 4 η-derivation prerequisites. Until it exists, the primitive stack is **philosophically complete and operationally disconnected from the PDE layer.** It is the #1 source of drift in this audit.

### Fix 2 — D-functional unification across 04, 07, 08

Commit to `D = 1 / M_eff` with `M_eff = (Σ b_K)² / Σ b_K²`. Amend 04 §6 and 07 §6 formulas. Worth ~one paragraph per primitive. Low cost, high clarity gain.

### Fix 3 — saturation-condition commitment

Shared definition of saturated regime (§5.7). Amend 05 §1, 06 §1, 09 §1, 11 §5.6, 12 §1 to cross-reference. Phase 4's η-derivation requires this.

### Fix 4 — overclaim relabeling

Section 4.1–4.7. Mechanical relabeling of seven assertions as "hypothesis" / "conjecture" / "conditional on Path X." Protects the stack against single-point failure in any one derivation. Low-cost.

### Fix 5 — graph-structure commitment

Per §5.1. Pick one of {graph, hypergraph, simplicial complex}. Recommendation: simplicial complex with weighted simplices, because it is the only structure that natively carries the homology/cohomology needed for gauge topology (03 §7.2) and topological phases (07 §7.4). Costs: one cross-cutting memo plus amendments to Primitive 01 §2 and Primitive 03 §2. Blocks: 03 §7.2, 07 §7.4, polarity coordinate (09 §7.1).

### Fix 6 — bandwidth-composition commitment

Per §5.2. Commit to sublinear composition with specified functional form. Amend Primitive 04 §7 item 2. Blocks: Primitive 11 §2 Born rule framing.

### Fix 7 — D_crit retirement footnote

Per §3.3. Mechanical, but necessary to keep the stack synchronized with the 2026-04-22 resolution memo. Cheapest fix; highest defensive value against reader confusion.

---

## 8. What this audit does NOT claim to have found

- It does not claim to have found every inconsistency. Thirteen interrelated primitives drafted in one session against a 30+ paper interpretation corpus almost certainly contain issues beyond what this single pass surfaced. A second-pass audit after Fixes 1–7 are applied is likely to be productive.
- It does not claim that any of these findings are fatal. The stack is internally consistent *as philosophy* even where it is operationally incomplete. The fixes listed are about tightening the philosophy into something Phase 2 can build on, not about rescuing a broken framework.
- It does not resolve the Arndt Blocker 1 problem. Fix 1 above is the path to resolving Arndt Blocker 1; this audit specifies the fix but does not execute it.
- It does not alter the status of the primitive stack as "careful prose definitions with gestures at mathematical objects" rather than formal axiomatization. That honest framing from the last turn stands.

---

## 9. Cross-reference

- Arndt retrodiction blockers: [quantum/retrodictions/arndt_interferometry.md](../retrodictions/arndt_interferometry.md) §3 (Blocker 1 ↔ Fix 1 here).
- Retired `D_crit = 0.5`: [theory/D_crit_Resolution_Memo.md](../../theory/D_crit_Resolution_Memo.md) (2026-04-22).
- Dimensional anchoring: [papers/Dimensional_Atlas/regimes/ED-Dimensional-01_Quantum_Regime.md](../../papers/Dimensional_Atlas/regimes/ED-Dimensional-01_Quantum_Regime.md).
- Primitive files: [quantum/primitives/01_micro_event.md](01_micro_event.md) through [13_relational_timing.md](13_relational_timing.md).

---

## 10. One-line summary

> **The thirteen-primitive stack is internally coherent as philosophy but operationally disconnected from the PDE layer. Seven structural fixes — led by a PDE-parameter mapping memo — would make it Phase-2-ready. Fifteen circular-dependency flags are now closed by the full stack being visible; twelve remain open on substantive grounds and cluster into three buckets (mathematical-structure commitments, PDE-layer gaps, Phase-4 quantitative targets) — which is the clearest positive signal of the audit: the sequencing was largely correct.**
