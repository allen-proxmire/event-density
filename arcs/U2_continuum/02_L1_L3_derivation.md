# Memo 02 — Derivation of L1 (Channel Measure) and L3 (Local Pairing) in the Continuum

**Date:** 2026-04-26
**Arc:** `arcs/U2_continuum/`
**Predecessors:** [`00_arc_outline.md`](00_arc_outline.md), [`01_decomposition_and_mapping.md`](01_decomposition_and_mapping.md)
**Status:** Derivation memo. Closes L1 (continuum channel measure) and L3 (local pointwise pairing) by transferring the corresponding U2-discrete arguments to the continuum regime, plus explicit continuum-specific checks (continuous channel spectra for L1; Primitive 12 coarse-graining smearing for L3).
**Purpose:** Settle L1 and L3 so Memo 03 can focus entirely on the load-bearing L2 (continuum position measure) question.

---

## 1. What this memo must establish

Per Memo 01, the continuum lift decomposes into:

- **L1** — channel measure: discrete `Σ_K` lifts to `Σ_K` (countable-channel case) or `∫ dν(K)` (continuous-channel case).
- **L2** — position measure: discrete `Σ_u` lifts to `∫_M dμ(x)`. **Deferred to Memo 03.**
- **L3** — local pairing: discrete `P_K*(u) Q_K(u)` lifts to `P_K*(x) Q_K(x)` without acquiring smearing kernels or non-local cross-slot terms.

This memo derives L1 and L3. Memo 01 classified both as FORCED-VIA-DERIVATION; the work here is to make those classifications rigorous.

---

## 2. L1 — Channel measure in the continuum

### 2.1 Setup

The continuum inner product (target form) at each spatial slot x ∈ M is:

```
[contribution at x] = ∫ dν_x(K) · P_K*(x) · Q_K(x)                              (1)
```

aggregated over space (L2, deferred). The question is what dν_x(K) — the channel measure on 𝒦(x) at point x — must look like.

Two regimes to handle, with the *same* primitive-level argument applying to each:

- **(L1-discrete-channels)** 𝒦(x) is finite or countable (e.g., spin states, internal atomic levels, photon polarization channels).
- **(L1-continuous-channels)** 𝒦(x) is a continuous spectrum (e.g., continuous momentum modes for matter waves, continuous position-basis channels for spatially-extended systems).

### 2.2 Transfer of the discrete-counting argument

The U2-discrete Memo 03 §2 argument for counting measure had two prongs:

- **(A1)** No primitive-level source supplies a non-trivial inter-channel weighting. Bandwidth is absorbed into the slot value `P_K`; rule-type τ does not distinguish channels within the τ-restricted set 𝒦_τ(x); channel topology is intrinsic but not measure-distinguishing.
- **(A2)** The C3b diagonal-equals-bandwidth constraint (`⟨P | P⟩ = total bandwidth`) independently forces unit weight on operationally relevant channels.

Both prongs are **regime-independent.** They invoke Primitive 04 (bandwidth), Primitive 07 (channel ontology), and the C3b sesquilinearity result — none of which acquires new content in the continuum. Primitive 12's thickening machinery does not introduce any new inter-channel weighting structure: it accumulates commitments and densifies the graph but does not assign extra weights to channels.

**Therefore both (A1) and (A2) transfer to the continuum verbatim**, with the spatial argument changed from u ∈ V to x ∈ M. For the discrete-channel case (L1-discrete-channels), the conclusion is immediate: counting measure on 𝒦(x) is FORCED in the continuum.

### 2.3 Continuous-channel case

For the continuous-channel case (L1-continuous-channels), the natural analog of "counting measure on a discrete set" is "Lebesgue measure on the continuous channel space." The structural arguments need to be checked in this setting.

**Primitive 12 input.** Primitive 12 (Memo 01 §2.2) supplies continuity of bandwidth fields b_K(x) along the spatial argument x. It does *not* by itself force the channel space to be continuous; that comes from the chain's rule-type and from the participation-graph structure (e.g., translation-invariance of the local participation graph forces continuous-momentum channels via the standard Fourier-decomposition argument).

When the channel space is continuous, the bandwidth-fraction interpretation of the inner product (per the C3b derivation) requires:

```
∫ dν_x(K) · b_K(x) = b_total(x)                                                 (2)
```

— integrated over channels, this must equal the total bandwidth at x. For (2) to hold uniformly across continuum-channel chains, the channel measure ν_x(K) must be the natural Lebesgue measure on 𝒦(x).

**Could ν_x(K) admit non-Lebesgue alternatives?** The same arguments as the discrete case apply:

- **(A1-cont)** No primitive-level source for a non-trivial channel weighting on the continuous channel space. The bandwidth field b_K(x) supplies all the channel-distinguishing structure; no further weighting is licensed by the primitives.
- **(A2-cont)** The diagonal-equals-bandwidth constraint (2) forces ν_x to be the unique measure consistent with `∫ dν b = b_total` for arbitrary b. Up to overall normalization, this is Lebesgue measure on 𝒦(x). Any non-Lebesgue alternative would conflict with (2) for some bandwidth profile, eliminating it.

**Falsifier F2-cont (alternative continuum channel measure):** dispatched. The diagonal-equals-bandwidth constraint forces Lebesgue-on-channel-space (the natural continuous analog of counting measure) for continuous-channel cases, just as it forced counting measure for discrete-channel cases.

### 2.4 Verdict for L1

**FORCED in the continuum regime.** The discrete-counting argument transfers verbatim to discrete-channel cases. For continuous-channel cases, the natural Lebesgue-on-channel-space measure is forced by the same structural arguments (no primitive-level inter-channel weighting + diagonal-equals-bandwidth constraint). Falsifier F2-cont is dispatched.

---

## 3. L3 — Local pointwise pairing in the continuum

### 3.1 Setup

The continuum-most-general sesquilinear pairing consistent with L1 + L2 is:

```
⟨P | Q⟩ = Σ_K ∫_M ∫_M dμ(x) dμ(x') · P_K*(x) · K_loc(K; x, x') · Q_K(x')        (3)
```

(restricting to within-channel terms; cross-channel and cross-band terms are addressed below). The pointwise local form has `K_loc(K; x, x') = δ(x − x')`. The question is whether non-trivial off-diagonal kernel components are forced to vanish — and whether Primitive 12's coarse-graining introduces any non-pointwise structure.

The full general kernel `K(K, K'; x, x')` admits three classes of non-trivial off-diagonal contributions:

- **Cross-band** (K, K' belong to different bands of the four-band decomposition).
- **Cross-channel within a band** (K ≠ K' within the same band).
- **Cross-position** (K = K', x ≠ x').

The U2-discrete Memo 03 §4 argument forbade each via independent structural arguments. This memo verifies each transfers to the continuum.

### 3.2 Transfer of the four-band orthogonality argument (cross-band terms)

**Source.** Primitive 04 §1.5 establishes four orthogonal bands (b_int, b_adj, b_env, b_com). Bands are partitioned bandwidth pools that do not mix at the primitive level.

**Transfer.** Four-band orthogonality is a primitive-level structural statement, regime-independent. It applies to bandwidth fields whether discrete (per-vertex bandwidths) or continuum (bandwidth densities b(x)). The continuum bandwidth field b(x) inherits the four-band partition: at each x, b(x) decomposes into b_int(x) + b_adj(x) + b_env(x) + b_com(x) with the same orthogonality structure.

For the continuum inner product to respect this orthogonality, cross-band kernel components must vanish: `K(K, K'; x, x') = 0` whenever K and K' belong to different bands. **The argument transfers verbatim to the continuum.**

**Falsifier F1′-cont (cross-band class):** dispatched.

### 3.3 Transfer of the non-contextuality argument (cross-channel-within-band terms)

**Source.** Born_gleason Memo 02 established that per-channel bandwidth `b_K(u)` is partition-independent (a function of (K, u) alone), forced by the channel-as-primitive ontology of Primitive 07. The argument forbade cross-channel kernel terms within a band: such terms would make the inner-product diagonal contextual on the channel decomposition, contradicting the partition-independence result.

**Transfer.** The channel-as-primitive ontology is regime-independent. Primitive 07 §1's statement that "channels are primitive ontological objects … sub-structure of the participation graph" applies whether the participation graph is the discrete G = (V, E) or the thickened continuum analog. In the continuum, channels at point x ∈ M are continuum sub-structures of the thickened participation manifold — but they remain primitive ontological objects whose identity is intrinsic to the structure, not basis-dependent.

The non-contextuality argument therefore transfers: per-channel bandwidth `b_K(x)` in the continuum is a function of (K, x) alone, partition-independent. Cross-channel kernel terms `K(K, K'; x, x)` for K ≠ K' would reintroduce contextuality, which the primitive structure forbids. **The argument transfers verbatim to the continuum.**

**Falsifier F1′-cont (cross-channel-within-band class):** dispatched.

### 3.4 Transfer of the kinematic/dynamic separation argument (cross-position terms)

**Source.** The discrete argument forbade cross-vertex (x ≠ x') kernel terms by appealing to the structural separation between kinematics (inner product = norm) and dynamics (time evolution = propagator). Cross-vertex terms have the form of propagators and belong in the dynamics (Step 2's H_K, V_{KK'}), not in the kinematic norm.

**Transfer.** The kinematic/dynamic separation is a structural feature of the QM-emergence framework, regime-independent. In the continuum, the dynamics is encoded in the participation-measure evolution equation and its Schrödinger / Klein-Gordon / Dirac thick-regime limits — all of which carry their own propagators and kernel structures. The inner product remains kinematic.

A non-zero `K(K, K; x, x')` for x ≠ x' in the continuum would introduce a position-space coherence kernel into the inner product, conflating it with the propagation operator. **The argument transfers verbatim to the continuum.**

**Falsifier F1′-cont (cross-position class):** dispatched.

### 3.5 The continuum-specific check: Primitive 12 coarse-graining smearing

This is the new continuum-specific concern not addressed by the discrete-argument transfer. Primitive 12's thickening machinery coarse-grains the discrete participation graph into the emergent manifold M. In principle, coarse-graining over a finite thickening-scale neighborhood ℓ_thick could leave residual short-range correlation kernels in the inner product — analogous to UV-cutoff effects in QFT, where a finite-resolution regularization scheme introduces regulator-dependent kernels that must be removed in the renormalization limit.

**The structural question.** Does Primitive 12's coarse-graining inherently introduce a smearing kernel into the continuum inner product, or does the strict τ → ∞ thickening limit recover pointwise locality?

**The structural answer.** Primitive 12 is *accumulation* (`T(R, t) = Σ_{ε ∈ commitments in R up to t} w(ε)`). Each commitment adds a vertex to the participation graph; thickening counts how many commitments persist. In the τ → ∞ limit, the graph becomes infinitely dense, and the discrete vertex measure refines into a continuum measure (this is L2's question). At each refinement step, the discrete inner product remains strictly pointwise (`P_K*(u) Q_K(u)` only at matching vertices, never at distinct vertices) — see L3's discrete arguments §3.2–§3.4 above.

**The continuum inner product is the τ → ∞ limit of the discrete inner product, not a finite-resolution coarse-graining.** Smearing kernels would arise *only if* one stopped the thickening at a finite τ and used the resulting finite-resolution structure. The strict continuum limit removes the smearing scale entirely and recovers pointwise locality.

This is the structural analog of "the continuum limit of a lattice quantum field theory recovers a local QFT, not a smeared one" — but here the underlying ontology already supplies the discrete structure (no regularization choice is involved), and the continuum is genuinely a limit rather than a regularization scheme.

**Two corner cases to address:**

- **(C1) Could finite-thickness corrections matter physically?** In ED, finite thickness τ < ∞ corresponds to incompletely-thickened regions (e.g., very early universe, deep vacuum, near-Q-C-boundary regimes). In such regimes, the continuum inner product (2) is not the appropriate description anyway — the discrete inner product (1) is. The continuum lift question concerns the strict thick-regime inner product, not finite-τ approximations.

- **(C2) Could coarse-graining preserve pointwise locality only in a measure-zero sense?** The concern: even in the τ → ∞ limit, the inner product might be pointwise "almost everywhere" but acquire singular contributions on measure-zero sets. The four-band orthogonality + non-contextuality arguments above forbid such singular contributions: any cross-position or cross-channel term, even on a measure-zero set, would violate the structural arguments. **Pointwise locality is exact, not just almost-everywhere.**

**Falsifier F1′-cont (smearing class):** dispatched. Primitive 12's thickening, taken to its strict τ → ∞ limit, recovers pointwise locality at the inner-product level. Smearing kernels are artifacts of finite-resolution coarse-graining, not primitive-level structural features.

### 3.6 U(1) consistency check

Under global phase rotation P → e^{iα} P, Q → e^{iα} Q, the local pointwise pairing transforms as `e^{-iα} e^{iα} P_K*(x) Q_K(x) = P_K*(x) Q_K(x)`. U(1)-invariant.

A non-local cross-slot kernel `K(K, K; x, x') P_K*(x) Q_K(x')` for x ≠ x' would also be U(1)-invariant under global rotation (the same argument applies). U(1) does not by itself forbid cross-slot terms. The structural arguments (four-band orthogonality, non-contextuality, kinematic/dynamic separation) are the operative ones.

This is consistent with the discrete-regime status: U(1) invariance is a *necessary* property of any admissible inner-product structure but not by itself *sufficient* to force pointwise locality. The full forcing requires the band/channel/dynamics structural arguments.

### 3.7 Verdict for L3

**FORCED in the continuum regime.** The local pointwise complex-conjugate pairing `P_K*(x) Q_K(x)` is the unique inner-product kernel consistent with (i) C3b sesquilinearity, (ii) Primitive 04 §1.5 four-band orthogonality (cross-band terms forbidden), (iii) non-contextuality from channel primitivity (cross-channel-within-band terms forbidden), (iv) kinematic/dynamic separation (cross-position terms forbidden), and (v) Primitive 12's strict thickening limit (no smearing kernels survive). All four classes of off-diagonal kernel contributions are dispatched by independent structural arguments. Falsifier F1′-cont is dispatched in all sub-classes.

---

## 4. Joint status after Memos 01–02 of U2-continuum

| Sub-feature | Status |
|---|---|
| **L1** Channel measure (continuum) | **FORCED** (this memo §2) |
| **L2** Position measure (continuum) | LOAD-BEARING; deferred to Memo 03 |
| **L3** Local pointwise pairing (continuum) | **FORCED** (this memo §3) |

**The arc's verdict now reduces entirely to Memo 03's treatment of L2.** Both anticipated-clean items closed cleanly, as projected. The substantive work is the position-measure question — specifically the conformal-uniqueness of the acoustic-metric volume form, with the diagonal-equals-bandwidth argument as the anticipated lead closure path (Memo 01 §7).

---

## 5. Comparative observation

L1 and L3 in the continuum closed with arguments structurally identical to U2-discrete Memo 03 §2 and §4 respectively, plus one continuum-specific check each (continuous-channel-space Lebesgue measure for L1; Primitive 12 strict-limit smearing dispatch for L3). Neither continuum-specific check required new structural inputs; both were resolved by transferring the existing discrete-regime arguments to the continuum context with appropriate scope adjustment.

This is consistent with the working hypothesis that L1 and L3 are FORCED-VIA-DERIVATION (Memo 01 §2.4 and §4.5). The structural-derivation methodology established in U2-discrete and born_gleason continues to compose well: arguments developed for one regime transfer to adjacent regimes when the relevant primitives are regime-independent.

L2 remains the qualitatively distinct case because it depends on Primitive 12 + Phase-3 acoustic-metric inputs that are themselves continuum-specific. The discrete-regime argument that closed C3c-(ii) — vertex-counting forced by graph-symmetry + diagonal constraint — does not directly transfer because the continuum analog of "vertex-counting" is `∫ dμ`, and the question is precisely whether dμ is uniquely fixed.

---

## 6. Recommended Next Steps

**(a) Begin Memo 03 (L2 derivation + arc verdict).** This is the load-bearing memo of the arc. It should examine three sub-questions: (a) is M uniquely constructed from G under thickening, (b) is the metric on M uniquely determined, (c) is the volume form uniquely determined by the metric. The diagonal-equals-bandwidth argument (Memo 01 §7 candidate 2) is the anticipated lead closure path. Memo 03 also delivers the arc's overall verdict.

**(b) Conduct the Phase-3 acoustic-metric audit before drafting Memo 03.** This was flagged in Memo 01 §9(b) and remains the most important pre-Memo-03 preparation. If existing GR-arc / acoustic-arc work has explicit conformal-uniqueness statements, Memo 03 quotes them and the arc closes quickly. If not, Memo 03 develops the diagonal-equals-bandwidth argument in full. Knowing which path before drafting will significantly shape Memo 03's length and emphasis.

**(c) Pre-decide Memo 03's verdict-handling for Primitive 12 internal residuals (P12 §2.13).** Per Memo 01 §9(c), P12's open items (weighting w(ε), continuum-validity threshold, un-thickening rates) could in principle gate the continuum lift. Memo 03 should explicitly verify each is independent of the inner-product structure (anticipated path) or identify which propagates (would yield CONDITIONAL). Deciding the framing in advance — "verify independence and dispatch" vs. "scope-restrict around the residual" — keeps Memo 03 focused.

---

## 7. Cross-references

- Arc outline: [`arcs/U2_continuum/00_arc_outline.md`](00_arc_outline.md)
- Memo 01 (decomposition + Primitive 12 / Phase-3 mapping): [`arcs/U2_continuum/01_decomposition_and_mapping.md`](01_decomposition_and_mapping.md)
- U2-discrete Memo 03 (parallel template; L1 transfers from §2, L3 transfers from §4): [`arcs/U2/03_C3c_discrete_regime.md`](../U2/03_C3c_discrete_regime.md)
- U2-discrete synthesis (theorem statement inherited): [`arcs/U2/04_synthesis_and_verdict.md`](../U2/04_synthesis_and_verdict.md)
- Born_gleason Memo 02 (non-contextuality, source for §3.3 transfer): [`arcs/born_gleason/02_noncontextuality_argument.md`](../born_gleason/02_noncontextuality_argument.md)
- Primitive 04 (bandwidth, four-band orthogonality): `quantum/primitives/04_participation_bandwidth.md`
- Primitive 07 (channel ontology, regime-independent): `quantum/primitives/07_channel.md`
- Primitive 09 (polarity, U(1) phase): `quantum/primitives/09_tension_polarity.md`
- Primitive 12 (thickening, strict τ → ∞ limit): `quantum/primitives/12_thickening.md`

---

## 8. One-line memo summary

> **L1 (continuum channel measure) and L3 (continuum local pointwise pairing) are both FORCED in the continuum regime. L1 follows from direct transfer of the U2-discrete counting-measure argument (no primitive-level inter-channel weighting + diagonal-equals-bandwidth constraint), with continuous-channel cases forced to Lebesgue-on-channel-space by the same arguments. L3 follows from regime-independent transfer of three discrete-regime arguments (four-band orthogonality forbidding cross-band kernels, non-contextuality forbidding cross-channel-within-band kernels, kinematic/dynamic separation forbidding cross-position kernels), plus a Primitive-12 smearing check showing that smearing kernels are artifacts of finite-resolution coarse-graining and do not survive the strict τ → ∞ thickening limit. Falsifiers F2-cont and F1′-cont (all sub-classes) dispatched. The arc's verdict now reduces entirely to Memo 03's load-bearing analysis of L2 (continuum position measure), with the diagonal-equals-bandwidth argument as the anticipated lead closure path against the conformal-rescaling concern.**
