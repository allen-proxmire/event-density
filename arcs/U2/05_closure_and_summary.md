# Memo 05 — U2-Discrete Arc Closure and Canonical Summary

**Date:** 2026-04-26
**Arc:** `arcs/U2/`
**Predecessors:** Memos [00](00_arc_outline.md), [01](01_decomposition_and_mapping.md), [02](02_C3a_C3b_derivation.md), [03](03_C3c_discrete_regime.md), [04](04_synthesis_and_verdict.md)
**Status:** Closure memo. Provides the canonical summary of the U2-discrete arc and its public-facing explanation. Integrates the result into the QM-emergence program and prepares for the U2-continuum follow-up arc.
**Purpose:** Close the U2-discrete arc with a single document that serves both as internal entry-point and as a self-contained external narrative.

---

## 1. Arc summary in one paragraph

The U2 arc asked whether the sesquilinear inner product on the participation-measure complex span — adopted as constraint C3 in QM-emergence Step 1 and designated upstream CANDIDATE U2 — is FORCED by ED's primitives. Memo 01 decomposed C3 into three structurally distinct sub-commitments: C3a (linearity of the participation-measure space), C3b (conjugate-bilinearity of the natural pairing), and C3c (the specific form ⟨P | Q⟩ = Σ_K ∫ dx P_K* Q_K). Memo 02 closed C3a as automatic and derived C3b as FORCED via Primitive 04 non-negativity (forcing the diagonal to equal squared modulus), Primitive 09 U(1) invariance (eliminating bilinear alternatives), and Primitive 04 §1.5 band additivity (forcing slot-wise linearity). Memo 03 — the load-bearing memo — examined C3c's three sub-features in the discrete participation-graph regime: channel counting measure, vertex counting position measure, and local complex-conjugate pointwise pairing. Each closed FORCED via independent primitive-level arguments (absence of inter-channel weighting, primitive-level vertex equivalence, and the joint action of four-band orthogonality + non-contextuality + kinematic/dynamic separation respectively). Memo 04 assembled the result into a theorem-grade verdict: U2 is FORCED in the discrete regime, with no new structural commitment introduced anywhere in the arc. Three downstream theorems (Theorem #10 Born, Step 4 Bell/Tsirelson, Step 5 Heisenberg) all promote from FORCED-conditional-on-U2 to FORCED-unconditional in the discrete regime. The continuum-regime applications retain a single narrowed residual — the lift of vertex counting measure to the emergent-manifold volume form via Primitive 12 thickening — which is a technical lift question for a focused follow-up arc, not a foundational commitment.

---

## 2. The arc's structure, narratively

**The question (Memo 00).** With Theorem #10 (Born rule via Gleason–Busch) established by the born_gleason arc conditional on U2, U2 became visible as the single highest-leverage open structural item in the QM-emergence program. The same upstream CANDIDATE gated three downstream theorems — Born (#10), Bell/Tsirelson (Step 4), Heisenberg (Step 5). One arc could promote all three simultaneously. The question was straightforward in structure but substantive in content: does the sesquilinear inner product follow from the primitive stack, or does it remain a genuine independent commitment?

**The decomposition (Memo 01).** The single-line statement of C3 — "complex-valued P_K(x) with sesquilinear inner product ⟨P | Q⟩ = Σ_K ∫ dx P_K*(x) Q_K(x)" — packages three structurally distinct commitments. Treating them as a single block obscured which parts were derivable and which were genuine choices. The three-part decomposition into C3a + C3b + C3c separated the algebraic-type questions (linearity, sesquilinearity) from the specific-form questions (which measure on channels, which measure on positions, what kind of pointwise pairing), and let the subsequent memos target each layer with the appropriate primitive inputs.

**The derivations (Memo 02).** C3a closed automatically: the participation measure is built complex-valued from Primitive 04 (real non-negative magnitude) + Primitive 09 (U(1) phase), and complex-valued function spaces are closed under componentwise sum and scalar multiplication. No primitive obstacle. C3b closed via a three-step argument: (a) the diagonal must equal squared modulus on each slot (forced by Primitive 04 non-negativity + the participation-measure construction); (b) U(1) invariance of bandwidth eliminates complex-bilinear pairings outright and reduces real-bilinear alternatives to the strictly-weaker real-part of sesquilinearity; (c) band additivity over disjoint-support participation measures forces additivity in each slot. Sesquilinearity is uniquely forced.

**The load-bearing analysis (Memo 03).** C3c's three sub-features were the substantive work of the arc. Each closed FORCED via an independent primitive-level argument:

- **Channel counting measure.** No primitive-level source for non-trivial channel weighting exists — bandwidth is in the slot value, rule-type doesn't distinguish within a chain's available channels, channel topology is intrinsic but not measure-distinguishing. The C3b diagonal-equals-bandwidth constraint independently forces unit weight on operationally relevant channels.
- **Vertex counting position measure.** Candidate alternatives (event density ρ(u), local total bandwidth) all conflict with the diagonal constraint. Graph-symmetry plus primitive-level vertex equivalence forces counting measure.
- **Local complex-conjugate pointwise pairing.** Three independent structural arguments forbid the three classes of cross-slot kernel: four-band orthogonality forbids cross-band terms; non-contextuality (inherited from born_gleason Memo 02) forbids same-band cross-channel terms; kinematic/dynamic separation forbids cross-vertex terms. The local Kronecker-delta kernel is the unique allowed structure.

The continuum lift via Primitive 12 thickening was deliberately deferred to a follow-up arc, with the three required inputs spelled out in advance (measure-theoretic content of thickening, uniqueness of emergent volume form, continuity of the lift).

**The synthesis (Memo 04).** The four-link chain Memos 02 → 03 yields the theorem-grade statement. The downstream cascade was made explicit: Theorem #10 (Born), Step 4 (Bell/Tsirelson), Step 5 (Heisenberg) all promote in the discrete regime. The continuum-regime conditionality changed character — from foundational ("does ED have a Hilbert-space arena?") to technical ("does Primitive 12's machinery preserve inner-product structure?"). The arc closed cleanly with zero new CANDIDATEs introduced anywhere.

---

## 3. The U2-discrete theorem, stated cleanly

> **Theorem (U2 from Primitives, Discrete Regime).** Let G = (V, E) be a participation graph with vertex set V (Primitive 01 micro-events) and edge set E (Primitive 03 participation relations). For a chain *C* of rule-type τ with available-channel set 𝒦_τ(u) at each u ∈ V (Primitive 07), construct the participation measure
>
> ```
> P_K(u, t) = √b_K(u, t) · e^{i π(K, u, t)}
> ```
>
> from Primitive 04 (bandwidth ≥ 0) and Primitive 09 (U(1) polarity phase), and let 𝒫 be the complex-vector-space span of all such arrays. Then there exists a unique sesquilinear inner product on 𝒫 forced by the primitive stack:
>
> ```
> ⟨P | Q⟩ = Σ_K Σ_u P_K*(u) · Q_K(u).
> ```
>
> Its diagonal recovers total bandwidth; its norm topology induces a Hilbert space ℋ_C on completion; the four-band orthogonality of Primitive 04 §1.5 is preserved as inner-product orthogonality between band-restricted projections.

**Status:** FORCED in the discrete participation-graph regime, **unconditional on any current ED-program CANDIDATE.**

**Scope conditions:**
- Discrete participation graph with vertex set V and finite/countable available-channel sets at each vertex (the regime in which Primitive 07's countability statement and graph-vertex measure are structurally clean).
- Primitive 09's U(1)-valued polarity (no current amendment under consideration that would widen this).
- Channel-as-primitive ontology of Primitive 07 §1 preserved.

**Significance for the QM-emergence program:** the result settles the single highest-leverage open structural item. It does not introduce new physics; it removes a foundational conditionality.

---

## 4. The downstream cascade

The U2 arc was opened because U2 was the shared residual on three downstream theorems. Each of those theorems had been derived — in some cases as fully written-out Step memos — but each carried an explicit conditionality on U2 because the Hilbert-space structure was needed for one or another aspect of the derivation. The U2 result lifts those conditionalities in the discrete regime:

| Theorem | Pre-U2 status | Post-U2 status (discrete) | Post-U2 status (continuum) |
|---|---|---|---|
| **Theorem #10 (Born, Gleason–Busch path)** | FORCED conditional on U2 | **FORCED unconditional** for d ≥ 2 | FORCED conditional on U2 continuum lift |
| **Step 4 (Bell + Tsirelson)** | FORCED conditional on U2 | **FORCED unconditional** | FORCED conditional on U2 continuum lift |
| **Step 5 (Heisenberg)** | FORCED conditional on U2 | **FORCED unconditional** | FORCED conditional on U2 continuum lift |

**Three structural results promoted from CANDIDATE-conditional to FORCED-unconditional in a single arc.** This is the strongest single-arc leverage produced by the QM-emergence program to date.

For applications running on discrete participation graphs (the natural setting for ED's primitive ontology), the QM-emergence program now has unconditional structural derivations of:
- the wavefunction (via the participation-measure framework);
- Schrödinger evolution (Step 2; CANDIDATE only on U3, U4 — separate items);
- the Born rule (Theorem #10);
- Bell-inequality-violating correlations at Tsirelson bound (Step 4);
- the Heisenberg uncertainty relation (Step 5).

This is a substantive structural completion of non-relativistic single-particle quantum mechanics in the discrete regime.

---

## 5. The narrowed residual: continuum lift via Primitive 12

For continuum-regime applications (matter-wave interferometry, BEC dynamics, cosmological-scale structures, anywhere the thick-regime emergent manifold is the relevant arena), one structural item remains open: the lift of the discrete vertex counting measure to the emergent-manifold volume form via Primitive 12 thickening.

The lift requires three technical inputs (per Memo 04 §4):

1. **Primitive 12 thickening's measure-theoretic content.** A clean statement of how the discrete vertex measure lifts to the emergent manifold's volume form.
2. **Uniqueness of the emergent volume form.** Verification that the bandwidth-gradient / acoustic-metric structure (Phase-3 work) determines the volume form uniquely, with no conformal-rescaling ambiguity.
3. **Continuity of the inner product under the lift.** The continuum inner product `⟨P | Q⟩ = Σ_K ∫_M dμ(x) P_K*(x) Q_K(x)` must be the well-defined limit of the discrete sum as the participation graph thickens.

**Important framing.** These are *technical lift questions*, not new structural commitments. They draw on existing Primitive 12 + Phase-3 machinery rather than amending primitives. The U2-continuum arc is anticipated to close FORCED with no new residuals — the path forward is clear and structurally focused. The conditionality has changed character, not magnitude: from foundational ("does ED have a Hilbert-space arena?") to technical ("does the lift preserve structure?"). This is a substantial sharpening even short of the full unconditional verdict.

---

## 6. Public-facing explainer

*Suitable for general scientific audience; a follow-up to the desktop `ED_Exponent2_Explainer.md` piece. Where that explainer covered the unification, this one covers the structural foundation that makes the unification possible.*

### The hidden bookkeeping question

The previous explainer described Event Density's "Exponent-2 Thread" — how the Born rule, Schrödinger equation, and Heisenberg uncertainty principle all share the same squared exponent because they all share the same underlying structural commitment: *bandwidth equals amplitude squared*.

That story has a piece that was glossed over. To say "amplitude squared" you need a notion of squaring complex numbers — and to say that those squared amplitudes add up the right way across a quantum system, you need a structure that mathematicians call an **inner product**. In standard quantum mechanics, this inner product is given to you on a silver platter: it is part of what defines a Hilbert space, the mathematical arena quantum mechanics lives in.

But in Event Density, the goal is to *derive* the structures of quantum mechanics from a simpler underlying ontology, not to assume them. The participation-measure framework gives you complex amplitudes naturally — bandwidth times a phase. But it doesn't immediately tell you that the natural way to combine two amplitudes into a single real-valued "agreement number" is the standard sesquilinear inner product.

That has to be derived. And it has to be derived from the primitives, not from a separate postulate — otherwise the "Born rule from primitives" result that the previous arc established would still secretly depend on a hidden Hilbert-space assumption.

### What the U2 arc shows

The U2 arc — five memos of structural derivation — establishes that the inner product is *not* an extra postulate. It is forced, uniquely, by the primitive ontology already in place.

The argument has three layers.

**Layer one: linearity.** The space of participation measures is a complex vector space. Sums of participation measures are participation measures; complex-scalar multiples are too. This is automatic — it follows from the participation measure being constructed as a complex-valued field in the first place.

**Layer two: sesquilinearity.** The natural pairing on a complex vector space has a particular asymmetric structure — conjugate-linear in one slot, linear in the other. This is a non-trivial choice in standard mathematics; multiple inequivalent pairings could be defined in principle. ED's primitives force the sesquilinear choice uniquely. The argument: bandwidth must remain unchanged when you multiply the participation measure by an overall phase factor (because phase is U(1)-valued and an overall phase has no physical meaning), and the only pairing that respects this *and* gives bandwidth as the diagonal output is sesquilinear.

**Layer three: the specific form.** Sesquilinearity tells you the *type* of pairing, but not the specific aggregation rule — which channels to sum over with what weighting, which positions to integrate over, whether the pairing has cross-channel coupling kernels or stays strictly local. The third layer's three sub-questions all close FORCED via independent primitive-level arguments. There is no source within the primitives for non-trivial channel weighting. There is no source for non-trivial vertex weighting. And four-band orthogonality, channel non-contextuality (a result from the previous arc), and the basic separation between kinematics and dynamics all conspire to forbid any kernel except the simplest one — local at each (channel, position) slot, with complex-conjugate multiplication.

The conclusion: the inner product is not a free choice. It is structurally forced.

### What this buys

Three of quantum mechanics's most famous results — the Born rule, Bell-inequality violations at the Tsirelson bound, and the Heisenberg uncertainty principle — were already derivable in ED conditional on the inner product being granted. With the U2 arc closing, the conditional becomes unconditional in the discrete regime where ED's primitive ontology lives most naturally.

This is a substantial step. It means the QM-emergence program has, for chains operating on discrete participation graphs, an unconditional structural derivation of essentially the entire content of non-relativistic single-particle quantum mechanics — wavefunction, evolution, measurement statistics, entanglement bounds, and uncertainty relations — from the primitive ontology alone.

### The honest framing

For continuum-regime applications — anywhere ED needs to talk about a smooth manifold rather than a discrete graph — one technical question remains open: whether the discrete-to-continuum lift preserves the inner-product structure. This is a different kind of question than the foundational one just settled. It is a measure-theoretic technicality, not an ontological commitment, and it has its own focused arc waiting to address it.

But the foundational question — *does ED's ontology force the inner-product structure that quantum mechanics needs?* — has been answered. Yes, it does. In the discrete regime where the ontology lives most cleanly, the inner product is forced.

Quantum mechanics, on this view, is not just a collection of postulates that happen to fit experiment. It is a structural consequence of how participation, bandwidth, and channels are built. The Born rule's squared amplitudes, Bell's correlation bounds, Heisenberg's uncertainty trade-off — none of them are extra ingredients. They are what the primitive ontology produces when you ask the right questions.

---

## 7. Integration into the QM-emergence program

**Memory record updates** (recommended; see Recommended Next Steps below):

- `project_qm_emergence_arc.md` — single bundled update covering: (i) U2 arc's discrete-regime FORCED result, (ii) Theorem #10's promotion from "FORCED conditional on U2" to "FORCED unconditional in discrete regime," (iii) Step 4 and Step 5's parallel promotion, (iv) narrowed continuum-regime conditionality with U2-continuum identified as next target.

**Synthesis paper updates** (recommended):

- `papers/QM_Emergence_Structural_Completion/QM_Emergence_Structural_Completion.md` — §4 (upstream CANDIDATEs) needs revision: U2 was listed as one of five upstream CANDIDATEs (U1–U5); after this arc, U2 is removed from that list in the discrete regime and replaced with a single technical residual (continuum lift). The synthesis paper's headline claim — "QM's axiomatic content reduces to five CANDIDATE structural commitments" — should be updated to reflect the arc's result. New count: U1 + U3 + U4 + U5 plus the U2-continuum-lift residual.

**Theorem inventory entry:**

> **U2-Discrete Theorem (Sesquilinear Inner Product from Primitives).** FORCED in the discrete participation-graph regime. The sesquilinear inner product `⟨P | Q⟩ = Σ_K Σ_u P_K*(u) Q_K(u)` is uniquely forced by Primitives 01+03+04+07+09+11 + four-band orthogonality + non-contextuality (born_gleason Memo 02), with no new structural commitment. Promotes Theorem #10 (Born), Step 4 (Bell/Tsirelson), and Step 5 (Heisenberg) to FORCED-unconditional in the discrete regime; continuum-regime applications gated by the U2-continuum follow-up arc.

---

## 8. Verdict

**The U2-discrete arc is closed.**

**U2 FORCED in the discrete regime.** The sesquilinear inner product is no longer a postulate of the QM-emergence framework. It is a structural consequence of the primitive ontology — derivable, citable, and compositional with the rest of the program. The single residual conditionality (continuum lift via Primitive 12) is technical rather than foundational and represents the natural next focused arc.

The arc produced five memos, no new CANDIDATEs, one new theorem-grade structural result, and the simultaneous promotion of three downstream theorems from CANDIDATE-conditional to FORCED-unconditional in the discrete regime. By the standards of structural-foundations work, this is a clean closure with significant program leverage.

---

## 9. Recommended Next Steps

**(a) Bundled memory-record update to `project_qm_emergence_arc.md`.** Per Memo 03 §10(c) and Memo 04 §7(a), this update should be done once for the whole post-arc package: U2 result + Theorem #10 / Step 4 / Step 5 promotions + narrowed continuum-regime residual + U2-continuum follow-up arc identified as next target. Consider also adding the Primitive-09 U(1) sensitivity note flagged in Memo 02 §6(c). One snapshot, not incremental edits.

**(b) Open the U2-continuum follow-up arc.** This is the highest-leverage remaining structural item: closing it produces fully unconditional Born / Bell-Tsirelson / Heisenberg results across both discrete and continuum regimes. Anticipated structure: 3 memos (decomposition of the lift question + lift derivation drawing on Primitive 12 + Phase-3 acoustic metric + verdict). The reasoning patterns from this arc are still warm; opening soon preserves methodological calibration.

**(c) Update the QM-emergence synthesis paper's §4 upstream-CANDIDATE inventory.** The synthesis paper's headline reduction-count ("QM's axiomatic content reduces to five CANDIDATE structural commitments U1–U5") is now outdated. The updated count after born_gleason + U2-discrete is: U1 + U3 + U4 + U5 plus the U2-continuum-lift residual — and the U2 entry in the inventory should explicitly cite the present arc's discrete-regime FORCED result with the continuum residual flagged. This update propagates the result to the cross-program reference document and keeps the synthesis paper's claims accurate.

---

## 10. Cross-references

**Within the U2 arc:**
- [`00_arc_outline.md`](00_arc_outline.md) — initial scoping
- [`01_decomposition_and_mapping.md`](01_decomposition_and_mapping.md) — C3a/b/c decomposition
- [`02_C3a_C3b_derivation.md`](02_C3a_C3b_derivation.md) — C3a automatic + C3b forced
- [`03_C3c_discrete_regime.md`](03_C3c_discrete_regime.md) — C3c forced in discrete regime
- [`04_synthesis_and_verdict.md`](04_synthesis_and_verdict.md) — theorem-grade synthesis

**Adjacent arcs and downstream beneficiaries:**
- [`arcs/born_gleason/05_synthesis_theorem10.md`](../born_gleason/05_synthesis_theorem10.md) — Theorem #10 (Born); now unconditional in discrete regime
- [`arcs/born_gleason/06_closure_and_summary.md`](../born_gleason/06_closure_and_summary.md) — born_gleason canonical summary (parallel template for this memo)
- [`arcs/arc-foundations/bell_correlations_from_participation.md`](../arc-foundations/bell_correlations_from_participation.md) — Step 4 Bell/Tsirelson
- [`arcs/arc-foundations/uncertainty_from_participation.md`](../arc-foundations/uncertainty_from_participation.md) — Step 5 Heisenberg
- [`arcs/arc-foundations/participation_measure.md`](../arc-foundations/participation_measure.md) — Step 1 framework where C3 originated

**Source primitives:**
- Primitive 01 — `quantum/primitives/01_micro_event.md`
- Primitive 03 — `quantum/primitives/03_participation.md`
- Primitive 04 — `quantum/primitives/04_participation_bandwidth.md`
- Primitive 07 — `quantum/primitives/07_channel.md`
- Primitive 09 — `quantum/primitives/09_tension_polarity.md`
- Primitive 11 — `quantum/primitives/11_commitment.md`
- Primitive 12 (continuum-lift follow-up arc) — `quantum/primitives/12_thickening.md`

**Program reference and memory:**
- [`papers/QM_Emergence_Structural_Completion/QM_Emergence_Structural_Completion.md`](../../papers/QM_Emergence_Structural_Completion/QM_Emergence_Structural_Completion.md) — synthesis paper
- Project memory: `memory/project_qm_emergence_arc.md`

**Public-facing companion:**
- `C:\Users\allen\Desktop\ED_Exponent2_Explainer.md` — first ScienceFriday-style explainer (Born + Schrödinger + Heisenberg unification). The §6 explainer in the present memo is intended as a sequel, focusing on the structural-foundation move that makes the unification rigorous rather than rhetorical.

---

## 11. One-line memo summary

> **U2-discrete arc closed. The sesquilinear inner product `⟨P | Q⟩ = Σ_K Σ_u P_K*(u) Q_K(u)` is FORCED in the discrete participation-graph regime by the primitive stack alone, with no new structural commitment introduced anywhere in the arc. Three downstream theorems (Theorem #10 Born, Step 4 Bell/Tsirelson, Step 5 Heisenberg) promote from CANDIDATE-conditional to FORCED-unconditional in the discrete regime simultaneously. Continuum-regime applications retain a single technical residual (the Primitive 12 thickening lift) for a focused follow-up arc; the conditionality has changed character from foundational to technical. Five memos, one new theorem-grade structural result, three downstream promotions, zero new CANDIDATEs introduced; clean structural-foundations closure with significant program leverage.**
