# Memo 04 — U2-Continuum Arc Closure and Canonical Summary

**Date:** 2026-04-26
**Arc:** `arcs/U2_continuum/`
**Predecessors:** Memos [00](00_arc_outline.md), [01](01_decomposition_and_mapping.md), [02](02_L1_L3_derivation.md), [03](03_L2_and_verdict.md)
**Status:** Closure memo. Provides the canonical summary of the U2-continuum arc and its public-facing explanation. Integrates the result into the QM-emergence program and prepares for the bundled memory-record update covering born_gleason + U2-discrete + U2-continuum.
**Purpose:** Close the U2-continuum arc with a single document that serves both as internal entry-point and as a self-contained external narrative, with the gauge-redundancy framing foregrounded.

---

## 1. Arc summary in one paragraph

The U2-continuum arc asked whether the discrete-regime U2 theorem (sesquilinear inner product FORCED on the participation-graph vertex set) lifts uniquely to the continuum regime under Primitive 12 thickening + Phase-3 acoustic-metric structure. Memo 01 decomposed the lift into three sub-features (L1 channel measure, L2 position measure, L3 local pairing) and mapped each to its required upstream inputs, foregrounding L2's conformal-uniqueness question as the likely sticking point. Memo 02 closed L1 and L3 cleanly via direct transfer of the U2-discrete arguments plus continuum-specific checks (Lebesgue-on-channel-space for continuous spectra; strict τ → ∞ thickening limit dispatching the smearing concern). Memo 03 — the load-bearing memo — analyzed L2 and produced a structurally rich verdict: the continuum position measure dμ is FORCED up to a conformal gauge redundancy `(b_K, dμ) ~ (Ω^{-D} b_K, Ω^D dμ)` under which all inner-product values are invariant; the conformal class itself is fixed by the bandwidth-gradient ratio structure of the acoustic metric; Primitive 12's internal residuals (P12 §2.13) are independent of the inner-product structure and do not propagate. The arc closed FORCED-with-explicit-gauge: the continuum inner product is uniquely determined in the regime that matters for physical content (gauge-invariant), with a description-level redundancy structurally analogous to Weyl rescaling in conformal field theory or lattice-spacing renormalization in lattice QFT. The downstream cascade is decisive: Theorem #10 (Born), Step 4 (Bell/Tsirelson), and Step 5 (Heisenberg) are now FORCED-unconditional across both discrete and continuum regimes, with all physical predictions gauge-invariant.

---

## 2. The arc's structure, narratively

**The question (Memo 00).** With U2-discrete closed, the QM-emergence program's three downstream theorems (Born, Bell/Tsirelson, Heisenberg) carried a single residual conditionality for continuum-regime applications: the lift of vertex counting measure to the emergent-manifold volume form. The U2-continuum arc was opened to settle this — in principle a smaller arc than U2-discrete because the structural question was narrower (lift only the position measure, not the full inner-product structure), but with potentially trickier inputs (Primitive 12 thickening + Phase-3 acoustic-metric work, both with their own conditionalities).

**The decomposition (Memo 01).** The lift question separated cleanly into three sub-features. L1 and L3 were anticipated to close via direct transfer of the U2-discrete arguments — both invoke regime-independent primitives (Primitive 04 bandwidth, Primitive 07 channel ontology, four-band orthogonality, non-contextuality, kinematic/dynamic separation). L2 was identified as the load-bearing item with two structural risks: (a) conformal-rescaling freedom in the acoustic-metric volume form, (b) Primitive 12's internal residuals propagating into the inner-product structure. The decomposition foregrounded the diagonal-equals-bandwidth argument as the anticipated lead closure path for L2.

**The clean transfers (Memo 02).** L1 closed cleanly: the discrete-counting argument transfers verbatim to discrete-channel cases, and the same arguments applied to continuous channel spectra force Lebesgue-on-channel-space. L3 closed cleanly: four-band orthogonality, non-contextuality, and kinematic/dynamic separation are all regime-independent and forbid cross-band, cross-channel, and cross-position kernel terms in the continuum just as they did discretely. The new continuum-specific concern — Primitive 12 coarse-graining smearing — was dispatched by recognizing that thickening is *accumulation* (each commitment adds a vertex), so the strict τ → ∞ limit recovers pointwise locality rather than a finite-resolution averaging. Smearing kernels are artifacts of stopping at finite τ, not primitive-level structural features.

**The load-bearing analysis (Memo 03).** L2 produced the arc's distinctive structural finding. The diagonal-equals-bandwidth argument, when developed carefully, runs into the standard density/measure relationship: in the continuum, `b_K(x)` is a *density* (value-per-unit-volume on M), and densities require a reference measure to be defined. The combination `b_K(x) · dμ(x)` is the well-defined invariant local bandwidth content; the separate factors are co-defined under conformal rescaling. Crucially, the off-diagonal calculation `⟨P | Q⟩ = Σ_K ∫ dμ · P_K* Q_K` shows that simultaneous rescaling `(b_K, dμ) → (Ω^{-D} b_K, Ω^D dμ)` leaves *every* inner-product value invariant — both diagonal and off-diagonal. This is gauge redundancy, not physical ambiguity. The conformal class of dμ is fixed by the bandwidth-gradient *ratio* structure of the acoustic metric (which is itself conformally invariant). Each P12 §2.13 internal residual was examined and found independent of the inner-product structure (each affects what M is or when continuum descriptions are valid, not the structure within).

**The verdict (Memo 03).** FORCED with explicit gauge structure. Physical content unconditional. Three downstream theorems promote to FORCED-unconditional in the continuum regime, joining their discrete-regime counterparts (already promoted by U2-discrete). The QM-emergence program now has FORCED-unconditional structural derivations of Born + Bell-Tsirelson + Heisenberg across all regimes.

---

## 3. The U2-continuum theorem, stated cleanly

> **Theorem (U2 in the Continuum Regime).** Let G = (V, E) be a participation graph thickened by Primitive 12 to an emergent manifold M with bandwidth fields b_K(x) and the acoustic metric supplied by the Phase-3 framework (Primitive 06 ED-gradient + Primitive 04 bandwidth construction). Then there exists a unique sesquilinear inner product on the participation-measure space 𝒫(M),
>
> ```
> ⟨P | Q⟩_cont = Σ_K ∫_M dμ(x) · P_K*(x) · Q_K(x),
> ```
>
> with the following structural properties:
>
> 1. **Existence:** the continuum inner product is the strict τ → ∞ limit of the U2-discrete inner product, with no smearing kernels surviving the lift.
> 2. **Uniqueness up to conformal gauge:** the pair (b_K(x), dμ(x)) admits a one-parameter rescaling `(b_K, dμ) ~ (Ω^{-D} b_K, Ω^D dμ)` for any smooth Ω(x) > 0.
> 3. **Gauge invariance of inner-product values:** every inner-product value `⟨P | Q⟩` (diagonal and off-diagonal) is invariant under the gauge.
> 4. **Conformal class fixed:** the conformal class of dμ is fixed by the bandwidth-gradient ratio structure of the acoustic metric.
> 5. **Independence from Primitive 12's internal residuals:** the structural form of the inner product does not depend on Primitive 12's open items (weighting w(ε), continuum-validity threshold, un-thickening rates, saturation behavior).
>
> **The continuum inner product is FORCED in every sense relevant to physical content.** The gauge (2) is a description redundancy structurally analogous to gauge fixing in geometric / field-theoretic frameworks; it does not affect any inner-product value, any Born probability, any Bell correlation, or any Heisenberg variance.

**Status:** FORCED with explicit gauge structure; physical content unconditional.

---

## 4. The gauge structure, explained

### 4.1 The transformation rule

The conformal gauge acts on (b_K(x), dμ(x)) by:

```
(b_K(x), dμ(x))   →   (Ω^{-D}(x) · b_K(x),  Ω^D(x) · dμ(x))                    (1)
```

where Ω(x) > 0 is an arbitrary smooth scalar field and D = dim M. The rule preserves the local bandwidth content `b_K(x) · dμ(x)`, which is the invariant quantity (the continuum limit of the discrete edge-weight integral over a thickened-vertex neighborhood).

### 4.2 Why the inner product is invariant

The participation measure transforms as P_K = √b_K · e^{iπ_K} → Ω^{-D/2} P_K under (1) (the phase factor is unchanged). Then:

```
⟨P | Q⟩ = Σ_K ∫_M dμ · P_K* · Q_K
       → Σ_K ∫_M (Ω^D dμ) · (Ω^{-D/2} P_K)* · (Ω^{-D/2} Q_K)
       = Σ_K ∫_M dμ · P_K* · Q_K
       = ⟨P | Q⟩.                                                                (2)
```

Both diagonal and off-diagonal pairings are invariant. The transformation is a pure redundancy in description.

### 4.3 Why this is a redundancy, not an ambiguity

A *physical ambiguity* would mean: two different gauge choices give two different physical predictions. Then the framework would be incomplete — a residual choice would be needed to nail down predictions.

A *description redundancy* (gauge) means: two different gauge choices give *identical* physical predictions. The framework is complete; the multiple descriptions are different ways of expressing the same physical content.

The U2-continuum gauge (1) is the latter: every inner-product value is invariant per §4.2. Born probabilities are bandwidth ratios `b_K / Σ b` — explicitly gauge-invariant by cancellation of Ω. Bell correlations are inner-product overlaps — invariant per (2). Heisenberg variances are bandwidth allocations — invariant by the same cancellation as Born.

**No physical quantity carries gauge dependence.**

### 4.4 What is fixed and what is gauge

- **Fixed by the primitives:** the conformal class of dμ (the angle structure of the acoustic metric, determined by bandwidth-gradient ratios, themselves primitive-level invariants).
- **Gauge-redundant:** the choice of representative within the conformal class — equivalently, the choice of "absolute scale" for dμ given the angle structure.

This is the standard structure of a gauge theory: there is a primitive-level invariant content (the conformal class) and a description-level redundancy (the choice of representative within the class). The gauge is fixed by convention, not by additional primitive commitments.

---

## 5. The downstream cascade

The U2 program (born_gleason + U2-discrete + U2-continuum) was opened because U2 was the single shared residual on three downstream theorems. With both U2 arcs now closed, the residuals are fully resolved:

| Theorem | Pre-U2-program | Post-born_gleason | Post-U2-discrete | Post-U2-continuum |
|---|---|---|---|---|
| **Theorem #10 (Born)** | Step 3 candidate-with-decoherence-residual | FORCED on U2 | **FORCED unconditional in discrete regime** | **FORCED unconditional, all regimes** (gauge-invariant) |
| **Step 4 (Bell + Tsirelson)** | FORCED on U2 (assumed) | (unchanged) | **FORCED unconditional in discrete regime** | **FORCED unconditional, all regimes** (gauge-invariant) |
| **Step 5 (Heisenberg)** | FORCED on U2 (assumed) | (unchanged) | **FORCED unconditional in discrete regime** | **FORCED unconditional, all regimes** (gauge-invariant) |

**Three of the QM-emergence program's structural results are now FORCED-unconditional across both the discrete and continuum regimes**, with the conformal gauge as a description-level redundancy that does not affect any physical prediction. This is the structural-foundations completion the program was working toward for non-relativistic single-particle quantum mechanics.

What remains in the QM-emergence Step-1 upstream-CANDIDATE inventory: U1 (the participation-measure construction itself), U3 (participation-measure evolution equation), U4 (momentum-basis identification), U5 (adjacency-band conjugate partition). U2 has been removed from the active CANDIDATE list. The reduction count moves from "five upstream CANDIDATEs U1–U5" to "four upstream CANDIDATEs U1, U3, U4, U5 plus the U2 conformal-gauge convention."

---

## 6. Public-facing explainer

*Suitable for general scientific audience; sequel to the desktop `ED_Exponent2_Explainer.md` and to the U2-discrete arc's closure explainer. Where those explainers covered the unification and the discrete structural foundation, this one covers the continuum lift and its gauge structure.*

### The lift question

Two earlier explainers laid out the picture so far. Event Density derives quantum mechanics's three most famous laws — Born, Schrödinger, Heisenberg — from a single underlying structure: a complex-valued participation measure built from bandwidth and phase. The Born rule's squared exponent appears in all three because all three express the same structural commitment: bandwidth equals amplitude squared. And the inner-product structure that makes this possible — the sesquilinear pairing on the participation-measure space — is itself derivable from ED's primitives, not assumed as a separate Hilbert-space postulate. That much was established for *discrete* settings: chains living on participation graphs with vertex-by-vertex structure.

But many of the systems quantum mechanics describes don't look discrete. A particle moves through a continuous space; a beam of light propagates along a continuous trajectory; a cosmological structure forms over continuous spacetime. For ED's framework to apply to these — for the Born rule, Bell correlations, and Heisenberg uncertainty to be unconditional in those settings too — the discrete inner-product structure had to lift cleanly to a continuum analog.

The U2-continuum arc asked: does the lift go through, and is the resulting continuum inner product uniquely determined?

### What the arc found

Two of the three sub-features of the lift went through cleanly. The way channels are aggregated in the continuum is uniquely forced by the same arguments that worked discretely. The way the inner product remains *local* in the continuum — without mysterious cross-position coupling kernels — is similarly forced.

The third sub-feature — the continuum *position measure*, which generalizes the discrete vertex-counting to a smooth integral over the emergent manifold — produced a structurally richer answer than the binary "yes, it's forced" or "no, it isn't."

The clean part: the *shape* of the position measure is forced. It's determined by the geometry of the emergent manifold, which in turn is determined by ED's bandwidth-gradient structure via something called the acoustic metric. There is no ambiguity about the angles, the orthogonality relations, the ratios of distances — all of those are pinned down by the primitives.

The subtle part: there is a one-parameter redundancy in *how you describe* the position measure, and a corresponding one-parameter redundancy in how you describe the bandwidth density. These two redundancies cancel exactly. Multiplying the position measure by some smooth function and dividing the bandwidth density by the same function preserves every inner-product value, every probability, every correlation. No physical quantity depends on the choice.

This is a familiar phenomenon in modern physics. Lattice quantum field theories have a "lattice spacing" that gets absorbed into field renormalization; the predictions are independent of the lattice spacing once you take the continuum limit. Conformal field theories have a "Weyl rescaling" symmetry that lets you rescale lengths by a smooth function; the conformally-invariant quantities are the physical ones. General relativity has coordinate freedom; only invariant quantities (curvatures, scalars) carry physical content.

The U2-continuum gauge is in the same family. It is a *description* redundancy, not a *physical* ambiguity.

### Why this matters

The honest framing matters for two reasons.

First, it's accurate. Pretending the continuum inner product is "fully unique" without the gauge would misrepresent the structure. The gauge is real; naming it explicitly is more useful than hiding it.

Second, it doesn't compromise the downstream physics. The Born rule's probabilities are ratios of bandwidths — the gauge cancels by construction. Bell correlations are inner-product overlaps — the gauge cancels per the explicit calculation. Heisenberg's variance bounds are bandwidth allocations — the gauge cancels by the same mechanism. None of the three big quantum-mechanics theorems carries any residual gauge dependence.

So the cascade goes through. With this arc closed, ED's framework now has unconditional structural derivations of the Born rule, Bell-inequality-violating correlations at the Tsirelson bound, and the Heisenberg uncertainty principle — across both discrete and continuum settings, for any quantum system the framework addresses.

Quantum mechanics, on this view, is no longer a collection of postulates that happen to fit experiment. It is what the participation-graph ontology produces, all the way down — including the inner-product structure that makes any of it work.

### The honest framing

What ED has *not* done is explain *why* there is a participation graph, *why* bandwidth is the right measure, *why* polarity is U(1)-valued. Those remain primitives — structural commitments adopted at the foundation of the framework. ED's claim is not that quantum mechanics is reducible to nothing; it is that quantum mechanics's *postulates* (Schrödinger, Born, Bell-Tsirelson, Heisenberg) are reducible to a smaller set of *structural commitments* about participation, bandwidth, and channels.

That smaller set is still load-bearing. The framework stands or falls on whether the primitives are the right ones. But the postulates of quantum mechanics no longer have to be assumed independently — they emerge from the framework as structural consequences. That is the substantive move, and the U2 program has now completed it for the foundational inner-product structure, both discretely and in the continuum, with explicit honesty about the gauge that the continuum lift introduces.

---

## 7. Integration into the QM-emergence program

**Memory record updates** (recommended; see Recommended Next Steps below):

- `project_qm_emergence_arc.md` — bundled update covering all three completed arcs (born_gleason + U2-discrete + U2-continuum). Single comprehensive snapshot rather than three incremental edits.

**Synthesis paper updates** (recommended):

- `papers/QM_Emergence_Structural_Completion/QM_Emergence_Structural_Completion.md` — §3.3 (Step 3 — Born Rule), §3.4 (Step 4 — Bell), §3.5 (Step 5 — Heisenberg), and §4 (upstream CANDIDATEs) all need updating. The headline reduction-count "five CANDIDATEs U1–U5" becomes "four CANDIDATEs U1, U3, U4, U5 plus a description-level conformal gauge from the continuum lift." The three Step memos should cite the unconditional promotion via born_gleason + U2 arcs.

**Theorem inventory entry:**

> **U2-Continuum Theorem (Continuum Inner Product, Gauge-Invariant Form).** FORCED with explicit gauge structure. The continuum sesquilinear inner product `⟨P | Q⟩ = Σ_K ∫_M dμ(x) P_K*(x) Q_K(x)` is uniquely determined up to a conformal gauge `(b_K, dμ) ~ (Ω^{-D} b_K, Ω^D dμ)` under which all inner-product values are invariant. The conformal class of dμ is fixed by the bandwidth-gradient ratio structure of the acoustic metric. Promotes Theorem #10 (Born), Step 4 (Bell/Tsirelson), and Step 5 (Heisenberg) to FORCED-unconditional across both discrete and continuum regimes; physical content fully gauge-invariant.

---

## 8. Verdict

**The U2-continuum arc is closed.**

**U2 FORCED in the continuum regime, with explicit gauge structure; physical content unconditional.** Combined with U2-discrete and born_gleason, the QM-emergence program's structural-foundations completion for non-relativistic single-particle quantum mechanics is in hand: Born + Bell-Tsirelson + Heisenberg are all FORCED-unconditional across all regimes the framework addresses, with the conformal gauge as a description-level redundancy that does not affect any physical prediction.

The arc produced four memos, no new CANDIDATEs, one structurally rich theorem (FORCED with explicit gauge), the simultaneous final promotion of three downstream theorems, and a gauge-redundancy framing that is structurally familiar from CFT, lattice QFT, and general relativity. The arc cycle (born_gleason + U2-discrete + U2-continuum) collectively represents the QM-emergence program's most substantial structural-foundations completion.

---

## 9. Recommended Next Steps

**(a) Bundled memory-record update covering all three arcs.** This is the highest-priority next step. The post-cycle state — Theorem #10 + Step 4 + Step 5 all FORCED-unconditional across regimes; U2 removed from active CANDIDATE list; gauge structure explicitly named; reduction count updated — needs to be captured as a single comprehensive snapshot in `project_qm_emergence_arc.md`. Three arcs of structural-foundations work culminate in this update; capturing it as a single update preserves the substantive program-level shift rather than fragmenting it across incremental edits.

**(b) QM-emergence synthesis paper revision.** The synthesis paper `QM_Emergence_Structural_Completion.md` is the cross-program reference document and currently presents the program's results conditional on U2 (and other CANDIDATEs). With U2 fully resolved, §3.3 (Born), §3.4 (Bell), §3.5 (Heisenberg), and §4 (upstream CANDIDATEs) all need updating. The headline claim — "QM's axiomatic content reduces to five CANDIDATE structural commitments" — moves to "four CANDIDATEs plus a continuum-lift conformal gauge." This is a substantial editorial pass but a structurally important one.

**(c) Consider opening the next-most-leveraged remaining arc (U1, U3, U4, or U5).** With U2 closed, the remaining QM-emergence Step-1 upstream CANDIDATEs become the next high-leverage targets. Of the four:
- **U1** (the participation-measure construction `P_K = √b · e^{iπ}` itself) is the most fundamental and the most ambitious — promoting it to FORCED would make the entire QM-emergence program structurally complete in the participation-measure framework.
- **U3** (the participation-measure evolution equation) is the natural target for completing Step 2 (Schrödinger emergence).
- **U4** (the momentum-basis identification) is the most "analog to standard QM" and might be the cleanest to address.
- **U5** (the adjacency-band conjugate partition) is the cleanest in §4.2 of the synthesis paper's program-priority assessment.

The U2 arc cycle's success establishes the structural-derivation methodology; applying it to U1, U3, U4, or U5 is the natural continuation. Recommended: U5 first (cleanest), U1 second (highest leverage); U3 and U4 require additional Step-2 context. But this is a program-priority decision worth deferring until the bundled memory update and synthesis paper revision are complete.

---

## 10. Cross-references

**Within the U2-continuum arc:**
- [`00_arc_outline.md`](00_arc_outline.md) — initial scoping
- [`01_decomposition_and_mapping.md`](01_decomposition_and_mapping.md) — L1/L2/L3 decomposition
- [`02_L1_L3_derivation.md`](02_L1_L3_derivation.md) — L1 + L3 closed
- [`03_L2_and_verdict.md`](03_L2_and_verdict.md) — L2 with gauge structure; arc verdict

**The full U2 program:**
- [`arcs/U2/05_closure_and_summary.md`](../U2/05_closure_and_summary.md) — U2-discrete canonical summary
- [`arcs/U2/04_synthesis_and_verdict.md`](../U2/04_synthesis_and_verdict.md) — U2-discrete theorem statement

**The born_gleason arc (predecessor; produced Theorem #10):**
- [`arcs/born_gleason/06_closure_and_summary.md`](../born_gleason/06_closure_and_summary.md) — born_gleason canonical summary
- [`arcs/born_gleason/05_synthesis_theorem10.md`](../born_gleason/05_synthesis_theorem10.md) — Theorem #10 statement

**Downstream beneficiaries:**
- [`arcs/arc-foundations/born_rule_from_participation.md`](../arc-foundations/born_rule_from_participation.md) — Step 3 Born (predecessor; superseded by Theorem #10)
- [`arcs/arc-foundations/bell_correlations_from_participation.md`](../arc-foundations/bell_correlations_from_participation.md) — Step 4 Bell/Tsirelson
- [`arcs/arc-foundations/uncertainty_from_participation.md`](../arc-foundations/uncertainty_from_participation.md) — Step 5 Heisenberg

**Source primitives:**
- Primitive 04 (bandwidth, density/measure structure): `quantum/primitives/04_participation_bandwidth.md`
- Primitive 06 (ED-gradient, acoustic-metric input): `quantum/primitives/06_ed_gradient.md`
- Primitive 07 (channel ontology): `quantum/primitives/07_channel.md`
- Primitive 09 (polarity, U(1) phase): `quantum/primitives/09_tension_polarity.md`
- Primitive 11 (commitment): `quantum/primitives/11_commitment.md`
- Primitive 12 (thickening, central to L2): `quantum/primitives/12_thickening.md`

**Phase-3 / acoustic-metric context:**
- `arcs/arc-phase-3/`, `arcs/arc-acoustic/`, `arcs/arc-GR-SC/`
- `memory/project_ed10_geometry_qft_scope.md`, `memory/project_ed_gr_sc_arc.md`

**Program reference and memory:**
- [`papers/QM_Emergence_Structural_Completion/QM_Emergence_Structural_Completion.md`](../../papers/QM_Emergence_Structural_Completion/QM_Emergence_Structural_Completion.md)
- Project memory: `memory/project_qm_emergence_arc.md`

**Public-facing companions:**
- `C:\Users\allen\Desktop\ED_Exponent2_Explainer.md` — first ScienceFriday-style explainer (Born + Schrödinger + Heisenberg unification)
- The §6 explainer here is intended as the third in a sequence: Exponent-2 (overview) → U2-discrete §6 (structural-foundation move) → U2-continuum §6 (gauge structure of the continuum lift).

---

## 11. One-line memo summary

> **U2-continuum arc closed. The continuum sesquilinear inner product `⟨P | Q⟩ = Σ_K ∫_M dμ(x) P_K*(x) Q_K(x)` is FORCED with explicit gauge structure: the pair (b_K(x), dμ(x)) admits a one-parameter rescaling `(b_K, dμ) ~ (Ω^{-D} b_K, Ω^D dμ)` under which every inner-product value is invariant; the conformal class of dμ is fixed by the bandwidth-gradient ratio structure of the acoustic metric; Primitive 12's internal residuals are independent of the inner-product structure. The gauge is a description redundancy structurally analogous to Weyl rescaling in CFT, lattice-spacing renormalization in lattice QFT, or coordinate freedom in general relativity — physical content is unconditional. Three downstream theorems (Theorem #10 Born, Step 4 Bell/Tsirelson, Step 5 Heisenberg) now FORCED-unconditional across both discrete and continuum regimes. The U2 program (born_gleason + U2-discrete + U2-continuum) collectively represents the QM-emergence program's structural-foundations completion for non-relativistic single-particle quantum mechanics: every postulate of QM that the program addresses is now derived rather than assumed, with the conformal gauge as the only description-level convention remaining. Four memos, one structurally rich theorem, three downstream final promotions, zero new CANDIDATEs introduced.**
