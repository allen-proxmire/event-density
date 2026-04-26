# Memo 03 — C3c Sub-Features in the Discrete Regime

**Date:** 2026-04-26
**Arc:** `arcs/U2/`
**Predecessors:** [`00_arc_outline.md`](00_arc_outline.md), [`01_decomposition_and_mapping.md`](01_decomposition_and_mapping.md), [`02_C3a_C3b_derivation.md`](02_C3a_C3b_derivation.md)
**Status:** Load-bearing memo of the U2 arc. Examines whether C3c — the specific form ⟨P | Q⟩ = Σ_K ∫ dx P_K*(x) Q_K(x) — is FORCED in the discrete participation-graph regime via three sub-features: (c1) channel counting measure, (c2) vertex counting position measure, (c3) local complex-conjugate pointwise pairing. Continuum lift via Primitive 12 thickening is explicitly deferred to a follow-up arc; this memo is restricted to the discrete vertex-level regime.
**Purpose:** Settle the U2 arc's verdict in its primary regime. Per the recommendation in Memo 02 §6(b), the discrete-regime result is the load-bearing piece; the continuum lift is technical scaffolding for a separate arc.

---

## 1. Setup

In the discrete regime, the participation graph is G = (V, E) with vertex set V (micro-events, Primitive 01) and edge set E (participation relations, Primitive 03). For a chain *C* of rule-type τ with available-channel set 𝒦_τ(u) at each u ∈ V, the participation measure is the array `{P_K(u) : K ∈ 𝒦_τ(u), u ∈ V}` with each slot value in ℂ (Memo 02 §2).

Memo 02 closed C3a (linearity) and C3b (sesquilinearity). Together they fix the *algebraic type* of the inner product: a sesquilinear pairing whose diagonal equals the aggregated bandwidth. What remains is to fix the *aggregation form* — specifically, the channel measure, the position measure, and whether the basic pairing has any cross-slot structure.

Three candidate alternative structures exist for each:

- **(c1 alternatives — F2):** non-counting channel measures `Σ_K w(K)` with w(K) ≠ 1 for some K.
- **(c2 alternatives — F3 discrete subset):** non-counting position measures `Σ_u w(u)` with w(u) ≠ 1 for some u.
- **(c3 alternatives — F1′):** non-local pairing kernels `K_{KK'}(u, u')` allowing cross-channel or cross-vertex contributions.

This memo addresses each.

---

## 2. (c1) — Channel counting measure

### 2.1 The question

Could the channel-aggregation be `⟨P | Q⟩ = Σ_K w(K) Σ_u P_K*(u) Q_K(u)` for some non-trivial weight function w : 𝒦_τ(u) → ℝ_{>0} other than w ≡ 1?

### 2.2 Primitive-level analysis

**Where could w(K) come from?** A non-trivial channel weight would have to be a structural feature of the participation graph that distinguishes one channel from another in a measure-theoretic sense — independent of bandwidth (which is already captured in the diagonal P_K* P_K = b_K).

The candidates within the primitive stack:

- **Bandwidth itself.** Already absorbed into the P-slot value; cannot be reused as an independent weight without double-counting.
- **Rule-type τ.** All channels in 𝒦_τ(u) are τ-compatible by definition (Primitive 07 §1: "rule-type-selective"). Within the restricted set 𝒦_τ(u), rule-type does not distinguish among channels.
- **Channel topology / connectivity.** Could a channel's sub-graph structure (number of edges, branching factor) supply a weight? Primitive 07 §1 establishes channels as primitive ontological objects — their identity is intrinsic to the graph, but the *measure-theoretic equivalence* of channels follows from their primitive status. No primitive-level structural feature beyond bandwidth distinguishes channels in the measure sense.
- **Environmental coupling.** A channel's coupling to environmental modes is captured by the four-band decomposition (b_env contribution) — already absorbed into bandwidth. Cannot supply an independent weight.

**There is no primitive-level source for a non-trivial w(K).**

### 2.3 The diagonal-equals-bandwidth constraint

Even setting aside the primitive-source question, the C3b Step A result (Memo 02 §3.2) requires the diagonal pairing on each slot to equal bandwidth: `⟨P_K(u) | P_K(u)⟩ = b_K(u) = |P_K(u)|²`.

Inserting a non-trivial channel weight would give:

```
⟨P | P⟩ = Σ_K w(K) Σ_u |P_K(u)|² = Σ_K w(K) Σ_u b_K(u)                       (1)
```

For this to equal the total bandwidth `Σ_K Σ_u b_K(u)` of the chain at the locus, we'd need `w(K) = 1` for every K with non-zero bandwidth. Since the relevant channels are exactly those in the support of the bandwidth distribution, this forces w ≡ 1 on the operationally relevant channel set.

A non-trivial w(K) on bandwidth-zero channels is operationally vacuous (they contribute nothing to the inner product anyway); restricting attention to operationally relevant channels gives w ≡ 1.

### 2.4 Falsifier F2 dispatch

**F2 (alternative channel measure):** dispatched. No primitive-level source supplies a non-trivial channel weight; the C3b diagonal-equals-bandwidth constraint forces w ≡ 1 on operationally relevant channels.

### 2.5 Verdict for (c1)

**FORCED.** Counting measure on 𝒦_τ(u) is the unique channel-aggregation consistent with (i) the absence of primitive-level inter-channel weighting and (ii) the C3b requirement that the diagonal pairing equal bandwidth.

---

## 3. (c2) — Vertex counting position measure (discrete regime)

### 3.1 The question

Could the position-aggregation be `⟨P | Q⟩ = Σ_K Σ_u w(u) P_K*(u) Q_K(u)` for some non-trivial vertex weight w : V → ℝ_{>0} other than w ≡ 1?

### 3.2 Primitive-level analysis

The candidates for a vertex weight:

- **Local event density ρ(u) (Primitive 05).** ρ is the count of micro-events at vertex u (or a smoothed version in the thick regime). A position measure `dμ(u) = ρ(u)` would weight vertices by their event density. This would give `⟨P | P⟩ = Σ_K Σ_u ρ(u) b_K(u)` — bandwidth weighted by local density.
- **Local total bandwidth `b(u) = Σ_K b_K(u)`.** Vertex weight = total bandwidth at u. Yields `⟨P | P⟩ = Σ_K Σ_u b(u) b_K(u) = Σ_u b(u)²` on the diagonal. Not equal to total bandwidth.
- **Vertex multiplicity / connectivity in the graph.** Number of edges incident to u, or the number of channels passing through u. Could in principle supply a weight, but no primitive-level requirement forces this.

### 3.3 The diagonal-equals-bandwidth constraint (again)

By the same argument as §2.3: the diagonal must satisfy `⟨P | P⟩ = total bandwidth across all channels and vertices`. With vertex weight w(u):

```
⟨P | P⟩ = Σ_K Σ_u w(u) |P_K(u)|² = Σ_K Σ_u w(u) b_K(u)                       (2)
```

For this to equal `Σ_K Σ_u b_K(u)`, w(u) ≡ 1 is forced on every vertex with non-zero bandwidth presence. Vertices with zero bandwidth presence contribute nothing regardless of w.

The candidate alternatives (ρ(u), b(u), etc.) all conflict with the diagonal constraint:

- ρ(u) gives event-density-weighted bandwidth, not bandwidth itself. Different physical quantity; would correspond to a different participation-measure framework.
- b(u) gives bandwidth-squared on the diagonal, which is dimensionally and structurally inconsistent with the C3b derivation.

### 3.4 Graph-symmetry argument

Independent of the diagonal constraint: the participation graph G = (V, E) is built from primitive vertices (Primitive 01 micro-events, individuated by their identity but otherwise primitively equivalent). For two vertices u, u' that are graph-isomorphic in their local neighborhood structure, no primitive feature distinguishes them. A non-counting measure w(u) ≠ w(u') for graph-isomorphic vertices would violate this primitive-level equivalence.

For two vertices that are *not* graph-isomorphic (different bandwidth, different local channel structure), the differences are already captured in the participation measure's slot values P_K(u). The vertex measure w(u) would be encoding the same information twice, which the diagonal-equals-bandwidth constraint forbids.

### 3.5 Falsifier F3 (discrete subset) dispatch

**F3 (alternative position measure), discrete subset:** dispatched. Vertex counting measure is forced by (i) the diagonal-equals-bandwidth constraint and (ii) primitive-level equivalence of graph vertices in the absence of bandwidth distinction.

### 3.6 Continuum lift deferred

The continuum lift — replacing `Σ_u` with `∫_M dx · μ(x)` where M is the emergent manifold (Primitive 12 thickening) and μ(x) is its volume form — requires:

- Primitive 12's thickening machinery to construct M from G.
- The emergent metric structure (acoustic-metric work, Phase-3 arc) to determine the volume form.
- Verification that the volume form is uniquely forced by the discrete-to-continuum lift, with no residual ambiguity (e.g., conformal rescaling).

**This is genuinely outside Memo 03's scope.** The discrete result above is structurally complete for the discrete regime; the continuum extension is a separate arc.

**What additional input the continuum-lift arc would need:**
- A clean statement of how Primitive 12 thickening constructs the emergent manifold M from the discrete graph G.
- A derivation that the emergent volume form is uniquely determined by the bandwidth-gradient / metric structure, with no conformal or other rescaling freedom that would admit alternative continuum measures.
- A verification that the continuum limit of the discrete vertex-counting measure is the emergent Lebesgue (or volume-form) measure — i.e., that no measure-theoretic obstruction arises in the lift.

These are technical extensions, not new structural commitments. They require the Phase-3 acoustic-metric work as input but should not require new primitives.

### 3.7 Verdict for (c2) in discrete regime

**FORCED.** Vertex counting measure is the unique position aggregation consistent with the diagonal-equals-bandwidth constraint and primitive-level vertex equivalence. Continuum lift deferred to a follow-up arc.

---

## 4. (c3) — Local complex-conjugate pointwise pairing

### 4.1 The question

C3b forces the inner product to be sesquilinear with diagonal equal to aggregated bandwidth. The remaining question: must the pairing be *strictly local on (K, u)-slots* — i.e., contributing only when the two slots match — or could it include cross-slot kernels `K(K, K'; u, u')` mixing different channels or different vertices?

The most general sesquilinear pairing consistent with §2 + §3 (counting measures fixed) is:

```
⟨P | Q⟩ = Σ_{K, K'} Σ_{u, u'} P_K*(u) · K(K, K'; u, u') · Q_{K'}(u')           (3)
```

with kernel `K(K, K'; u, u') ∈ ℂ`.

The local form `K(K, K'; u, u') = δ_{KK'} δ_{uu'}` (Kronecker deltas in the discrete setting) gives the standard `Σ_K Σ_u P_K* Q_K`. The question is whether non-trivial off-diagonal kernel components are allowed.

### 4.2 Diagonal-equals-bandwidth fixes the diagonal of K

Inserting (3) into the diagonal:

```
⟨P | P⟩ = Σ_{K, K'} Σ_{u, u'} P_K*(u) K(K, K'; u, u') P_{K'}(u').              (4)
```

For this to equal `Σ_K Σ_u b_K(u) = Σ_K Σ_u |P_K(u)|²` for *every* P, the diagonal contribution (terms with K = K', u = u') must give `Σ_K Σ_u |P_K(u)|²`. Comparing with (4):

```
K(K, K; u, u) = 1   for every (K, u).                                         (5)
```

Off-diagonal components (K ≠ K' or u ≠ u') are not constrained by the diagonal alone — they contribute zero when P = Q only if their cross-terms cancel, which is a non-generic condition. So the diagonal constraint fixes the diagonal of K but leaves the off-diagonal of K formally free.

The argument forbidding non-trivial off-diagonal must come from elsewhere. Three structural arguments combine to force `K(K, K'; u, u') = δ_{KK'} δ_{uu'}`.

### 4.3 Argument from four-band orthogonality

**Premise (P4-band-orth).** Primitive 04 §1.5 establishes four orthogonal bands (b_int, b_adj, b_env, b_com) with the chain's bandwidth partitioned across them. Orthogonality at the primitive level means the bands do not mix bandwidth: a chain's internal-rule band is structurally disjoint from its environmental band.

For the inner product to respect this orthogonality, the kernel K must be **block-diagonal across the four bands**: components mixing different bands must vanish. Otherwise the inner product would generate cross-band coherences in `⟨P | P⟩` that violate the primitive-level orthogonality.

This already eliminates a large class of cross-channel kernel components — any K(K, K'; u, u') with K and K' belonging to different bands must equal zero.

### 4.4 Argument from non-contextuality (channel primitivity)

**Premise (P7-prim).** Born_gleason Memo 02 established that per-channel bandwidth `b_K(u)` is partition-independent — a function of (K, u) alone, with no contribution from other channels at u. The channel-as-primitive ontology of Primitive 07 forces this.

Within a single band, can the inner product include cross-channel kernel terms K(K, K'; u, u) for K ≠ K'? Such terms would contribute `P_K*(u) · K(K, K'; u, u) · Q_{K'}(u)` to ⟨P | Q⟩ — a coupling between distinct primitive channels at the same locus.

If such a term were present, its contribution to `⟨P | P⟩` would be `P_K*(u) K(K, K'; u, u) P_{K'}(u)`, which depends on the *cross-channel coherence* P_K* P_{K'}. This would mean the inner-product norm of P depends on inter-channel phase relationships — *the inner product would be contextual on the channel decomposition*. But born_gleason Memo 02 forced non-contextuality: `b_K(u)` is partition-independent, hence the inner-product diagonal cannot depend on inter-channel coherences.

**Cross-channel kernel terms within a band are forbidden by non-contextuality.**

### 4.5 Argument from kinematic/dynamic separation

**Premise (P11-kinematic).** Inner products encode *kinematic* content (norms, orthogonalities, probabilities at a single time). Time-evolution and channel-mixing dynamics are encoded separately, in the participation-measure evolution equation (Step 2's `iℏ ∂_t P_K = H_K P_K + Σ V_{KK'} P_{K'}`).

A non-local kernel `K(K, K'; u, u')` with u ≠ u' would couple participation values at distinct vertices in the inner product — i.e., the inner product would carry propagation/dynamical information. This conflates kinematics with dynamics, contrary to the standard structural separation in QM (and in ED's QM-emergence framework, which inherits this separation explicitly).

Specifically: if `K(K, K; u, u') ≠ 0` for u ≠ u', then `⟨P | P⟩ = ... + Σ K(K, K; u, u') P_K*(u) P_K(u')` would include a non-local coherence term. This term has the structure of a propagator (a position-space kernel coupling distinct vertices) rather than a norm. It belongs in the *dynamics* (Step 2's V_{KK'} or H_K), not in the *kinematic norm*.

**Cross-vertex kernel terms within a channel are forbidden by the kinematic/dynamic separation.**

### 4.6 Joint conclusion

The three arguments combine to force `K(K, K'; u, u') = δ_{KK'} δ_{uu'}`:

| Kernel component | Forbidden by |
|---|---|
| Cross-band (K, K' in different bands) | Four-band orthogonality (§4.3) |
| Same-band cross-channel (K ≠ K' within a band) | Non-contextuality / channel primitivity (§4.4) |
| Same-channel cross-vertex (K = K', u ≠ u') | Kinematic/dynamic separation (§4.5) |

The only allowed kernel is the local Kronecker-delta structure. The basic inner product is therefore:

```
⟨P | Q⟩ = Σ_K Σ_u P_K*(u) · Q_K(u).                                            (6)
```

### 4.7 U(1)-invariance check

A consistency check on (6): under global phase rotation P → e^{iα} P, Q → e^{iα} Q, the pairing transforms as `e^{-iα} e^{iα} ⟨P | Q⟩ = ⟨P | Q⟩`. U(1)-invariant on both diagonal and off-diagonal, consistent with §3.3 of Memo 02.

The non-local cross-vertex kernel `K(K, K; u, u')` would also be U(1)-invariant if we apply the same rotation to both slots — so U(1) does not by itself forbid cross-vertex terms. The structural argument (kinematic/dynamic separation) is the operative one.

### 4.8 Falsifier F1′ dispatch

**F1′ (non-local cross-slot terms):** dispatched by the joint action of four-band orthogonality (cross-band), non-contextuality (cross-channel within a band), and kinematic/dynamic separation (cross-vertex). All three structural arguments are independent and individually sufficient for their respective sub-classes.

### 4.9 Verdict for (c3)

**FORCED.** Local complex-conjugate pointwise pairing P_K*(u) Q_K(u) is the unique inner-product kernel consistent with C3b sesquilinearity + Primitive 04's four-band orthogonality + non-contextuality (Memo 02 of born_gleason) + the kinematic/dynamic separation of QM-emergence.

---

## 5. Joint verdict for C3c in the discrete regime

| Sub-feature | Falsifier | Verdict |
|---|---|---|
| **(c1)** Channel counting measure | F2 | **FORCED** (§2) |
| **(c2)** Vertex counting position measure | F3 (discrete subset) | **FORCED** (§3); continuum lift deferred |
| **(c3)** Local complex-conjugate pointwise pairing | F1′ | **FORCED** (§4) |

**C3c is FORCED in the discrete participation-graph regime.**

Combined with Memo 02's results (C3a AUTOMATIC, C3b FORCED), the full sesquilinear inner product `⟨P | Q⟩ = Σ_K Σ_u P_K*(u) Q_K(u)` is **FORCED in the discrete regime by the primitive stack** — Primitives 01, 03, 04, 07, 09, 11, the participation-measure construction (1), and the structural results inherited from born_gleason Memo 02 (non-contextuality from channel primitivity).

**No new structural commitment is required.**

---

## 6. What the discrete-regime FORCED verdict buys

If the discrete-regime result stands as the canonical statement of U2 (with continuum lift handled separately):

- **Theorem #10 (Born rule, born_gleason arc) promotes from "FORCED conditional on U2" to "FORCED unconditional in the discrete regime."**
- **QM-emergence Step 4 (Bell / Tsirelson) similarly promotes** for chains operating on discrete participation graphs.
- **QM-emergence Step 5 (Heisenberg) similarly promotes** for the same discrete chains.

For continuum-regime applications (matter-wave interferometry, BEC dynamics, cosmological-scale structures), the unconditional promotion awaits the continuum-lift arc. In the meantime, all three downstream theorems retain a single conditionality — but it is now narrowed from "U2 (full statement)" to "the continuum lift of vertex counting measure to emergent-manifold volume form."

This is a substantial sharpening even short of the full unconditional verdict. The conditionality moves from a structural-foundations question ("does ED have a Hilbert space?") to a technical lift question ("does the discrete-to-continuum machinery preserve the inner-product structure?"). The latter is a Primitive 12 / Phase-3 question with its own techniques.

---

## 7. What remains for the continuum-lift follow-up arc

A separate arc — call it U2-continuum — would address:

1. **Primitive 12 thickening's measure-theoretic content.** How the discrete participation graph's vertex measure lifts to the emergent manifold's volume form.
2. **Uniqueness of the emergent volume form.** Whether the bandwidth-gradient / metric structure (acoustic metric, Phase-3 work) determines the volume form uniquely or admits conformal-rescaling alternatives.
3. **Continuity of the inner product under the lift.** Verification that the continuum inner product `⟨P | Q⟩ = Σ_K ∫_M dμ(x) P_K*(x) Q_K(x)` is the well-defined limit of the discrete sum as the participation graph thickens.

These are technical questions, not new structural commitments. They draw on existing Primitive 12 and Phase-3 work rather than amending primitives. The continuum-lift arc is anticipated to close FORCED with no new residuals — but the verification is its own session-length effort.

---

## 8. Consolidated U2-arc status (after Memos 01–03)

| Sub-commitment | Status |
|---|---|
| **C3a** (linearity) | AUTOMATIC (Memo 02) |
| **C3b** (sesquilinearity) | FORCED (Memo 02) |
| **C3c-(i)** (channel measure) | FORCED in discrete regime (this memo §2) |
| **C3c-(ii)** (position measure) | FORCED in discrete regime (this memo §3); continuum lift deferred |
| **C3c-(iii)** (local pointwise pairing) | FORCED (this memo §4) |

**U2 (discrete regime): FORCED.**

**U2 (continuum regime): FORCED conditional on a clean Primitive 12 lift (separate arc).**

---

## 9. Verdict

**U2 is FORCED in the discrete participation-graph regime.**

All three sub-features of C3c (channel counting measure, vertex counting position measure, local complex-conjugate pointwise pairing) follow from the primitive stack — Primitives 01, 03, 04, 07, 09, 11 + the four-band orthogonality + non-contextuality from born_gleason Memo 02 — without introducing new structural commitments. Falsifiers F2, F3 (discrete subset), and F1′ are each dispatched by independent primitive-level arguments.

The continuum lift via Primitive 12 thickening is the only structural item remaining for a fully unconditional U2-FORCED verdict. It is a technical lift question, not a foundational structural question; it has been deferred to a follow-up arc.

The discrete-regime FORCED verdict is sufficient to **promote Theorem #10 (Born), Step 4 (Bell/Tsirelson), and Step 5 (Heisenberg) to fully FORCED status for chains operating on discrete participation graphs.** Continuum-regime applications retain a single conditionality (continuum lift) until the U2-continuum arc completes.

---

## 10. Recommended Next Steps

**(a) Begin Memo 04 (synthesis + verdict + downstream-status update).** With C3a, C3b, and C3c (discrete regime) all closed, Memo 04 is consolidation work: state the U2 arc's overall verdict, update the downstream theorem table (Theorem #10, Step 4, Step 5 → FORCED in discrete regime / conditional on continuum lift in continuum regime), and recommend whether to open the U2-continuum follow-up arc immediately or defer it. Should be a shorter memo, structurally analogous to born_gleason Memo 05.

**(b) Open the U2-continuum follow-up arc once Memo 04 closes.** The continuum lift is the single remaining structural item gating the unconditional promotion of three downstream theorems. It is high-leverage in the same way the U2 arc itself was, and the path forward is clear (Primitive 12 + Phase-3 acoustic-metric inputs). Recommended structure for the U2-continuum arc: 3 memos (decomposition + lift derivation + verdict), shorter overall than U2 because the structural questions are more focused.

**(c) After Memo 04, update memory record `project_qm_emergence_arc.md`.** The U2 arc's discrete-regime FORCED result + Theorem #10's promotion + the residual continuum-lift conditionality together constitute a substantial program update. The memory record should be updated once for the whole package (after Memo 04) rather than incrementally — this avoids churn and gives a clean snapshot of the post-arc program state.

---

## 11. Cross-references

- Arc outline: [`arcs/U2/00_arc_outline.md`](00_arc_outline.md)
- Memo 01 (decomposition + mapping): [`arcs/U2/01_decomposition_and_mapping.md`](01_decomposition_and_mapping.md)
- Memo 02 (C3a + C3b derivation): [`arcs/U2/02_C3a_C3b_derivation.md`](02_C3a_C3b_derivation.md)
- Born_gleason Memo 02 (non-contextuality from channel primitivity, source for §4.4): [`arcs/born_gleason/02_noncontextuality_argument.md`](../born_gleason/02_noncontextuality_argument.md)
- Born_gleason synthesis (Theorem #10, downstream beneficiary): [`arcs/born_gleason/05_synthesis_theorem10.md`](../born_gleason/05_synthesis_theorem10.md)
- Step 4 (Bell / Tsirelson, downstream beneficiary): [`arcs/arc-foundations/bell_correlations_from_participation.md`](../arc-foundations/bell_correlations_from_participation.md)
- Step 5 (Heisenberg, downstream beneficiary): [`arcs/arc-foundations/uncertainty_from_participation.md`](../arc-foundations/uncertainty_from_participation.md)
- Primitive 01 (micro-event, vertex primitivity): `quantum/primitives/01_micro_event.md`
- Primitive 03 (participation, edge structure): `quantum/primitives/03_participation.md`
- Primitive 04 (bandwidth, four-band orthogonality): `quantum/primitives/04_participation_bandwidth.md`
- Primitive 07 (channel ontology, primitivity): `quantum/primitives/07_channel.md`
- Primitive 09 (polarity, U(1) phase): `quantum/primitives/09_tension_polarity.md`
- Primitive 11 (commitment, kinematic/dynamic separation): `quantum/primitives/11_commitment.md`
- Primitive 12 (thickening, relevant for continuum-lift follow-up arc): `quantum/primitives/12_thickening.md`

---

## 12. One-line memo summary

> **C3c (the specific Σ_K ∫ form of the inner product) is FORCED in the discrete participation-graph regime. Channel counting measure (c1) is forced by the absence of primitive-level inter-channel weighting plus the diagonal-equals-bandwidth constraint; vertex counting position measure (c2) is forced by the same diagonal constraint plus primitive-level vertex equivalence; local complex-conjugate pointwise pairing (c3) is forced by the joint action of four-band orthogonality (no cross-band kernel terms), non-contextuality from channel primitivity (no cross-channel kernel terms within a band), and kinematic/dynamic separation (no cross-vertex kernel terms). Falsifiers F2, F3 (discrete), F1′ all dispatched by independent primitive-level arguments. U2 is FORCED in the discrete regime; continuum lift via Primitive 12 thickening is deferred to a follow-up arc whose path is clear and structurally focused. This promotes Theorem #10 (Born), Step 4 (Bell/Tsirelson), and Step 5 (Heisenberg) to fully FORCED for chains on discrete participation graphs; continuum-regime applications retain one residual conditionality.**
