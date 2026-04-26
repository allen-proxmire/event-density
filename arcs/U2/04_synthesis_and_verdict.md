# Memo 04 — U2 Arc Synthesis and Verdict

**Date:** 2026-04-26
**Arc:** `arcs/U2/`
**Predecessors:** [`00_arc_outline.md`](00_arc_outline.md), [`01_decomposition_and_mapping.md`](01_decomposition_and_mapping.md), [`02_C3a_C3b_derivation.md`](02_C3a_C3b_derivation.md), [`03_C3c_discrete_regime.md`](03_C3c_discrete_regime.md)
**Status:** Synthesis memo. Consolidates Memos 01–03 into a theorem-grade verdict for U2 in the discrete participation-graph regime, updates downstream theorem-status entries, and prepares the continuum-lift follow-up arc.
**Purpose:** Close the U2 arc for the discrete regime and integrate the result into the QM-emergence program.

---

## 1. Where we are

After Memos 01–03, the three sub-commitments of U2 (the sesquilinear inner product on the participation-measure complex span, constraint C3 of QM-emergence Step 1) are fully resolved in the discrete regime:

| Sub-commitment | Description | Status | Source |
|---|---|---|---|
| **C3a** | Linearity of 𝒫 (complex-vector-space structure) | **AUTOMATIC** | Memo 02 §2 |
| **C3b** | Conjugate-bilinearity (sesquilinearity) | **FORCED** | Memo 02 §3 |
| **C3c-(i)** | Channel counting measure | **FORCED** (discrete regime) | Memo 03 §2 |
| **C3c-(ii)** | Vertex counting position measure | **FORCED** (discrete regime); continuum lift deferred | Memo 03 §3 |
| **C3c-(iii)** | Local complex-conjugate pointwise pairing | **FORCED** | Memo 03 §4 |

**No new structural commitments were introduced anywhere in the arc.** Every sub-commitment closes via existing primitive-stack content + structural arguments inherited from prior arcs (specifically, born_gleason Memo 02's non-contextuality result).

---

## 2. The U2 theorem (discrete regime)

> **Theorem (U2 from Primitives, discrete regime).** Let G = (V, E) be a participation graph with vertex set V (Primitive 01 micro-events) and edge set E (Primitive 03 participation relations). Let *C* be a chain of rule-type τ with available-channel set 𝒦_τ(u) at each u ∈ V (Primitive 07). Construct the participation measure
>
> ```
> P_K(u, t) = √b_K(u, t) · e^{i π(K, u, t)}                                     (1)
> ```
>
> from Primitive 04 (bandwidth `b_K ∈ ℝ_{≥0}`) and Primitive 09 (polarity `π ∈ U(1)`), and let 𝒫 be the complex-vector-space span of all such arrays.
>
> **Then there exists a unique sesquilinear inner product on 𝒫 forced by the primitive stack:**
>
> ```
> ⟨P | Q⟩ = Σ_K Σ_u P_K*(u) · Q_K(u).                                           (2)
> ```
>
> This inner product satisfies all four sesquilinear-form properties (S1)–(S4) of Memo 02 §3.1. Its diagonal recovers the chain's total bandwidth: `⟨P | P⟩ = Σ_K Σ_u b_K(u)`. The induced norm topology yields a Hilbert space ℋ_C on completion.
>
> **The four-band orthogonality of Primitive 04 §1.5 is preserved** as inner-product orthogonality between band-restricted projections of P. The non-contextuality of per-channel bandwidth (born_gleason Memo 02) is preserved as basis-independence of the channel-resolved diagonal.
>
> **Proof sketch.** C3a follows automatically from the complex-valued construction (1) and closure of complex-valued function spaces under componentwise sum and complex-scalar multiplication (Memo 02 §2). C3b follows from the joint action of Primitive 04 non-negativity (forces diagonal = squared modulus), Primitive 09 U(1) invariance (eliminates complex-bilinear, reduces real-bilinear to strictly weaker real-part of sesquilinearity), and Primitive 04 §1.5 band additivity (forces slot-wise additivity), giving sesquilinearity uniquely (Memo 02 §3). C3c-(i)–(iii) follow in the discrete regime from independent primitive-level arguments: counting measure on channels is forced by the absence of primitive-level inter-channel weighting plus the diagonal-equals-bandwidth constraint; counting measure on vertices is forced by primitive-level vertex equivalence plus the same diagonal constraint; local pointwise pairing is forced by the joint action of four-band orthogonality (no cross-band kernel terms), non-contextuality (no cross-channel kernel terms within a band), and the kinematic/dynamic separation of QM-emergence (no cross-vertex kernel terms) (Memo 03 §2–§4). ∎

**Status:** FORCED in the discrete participation-graph regime, unconditional on any current ED-program CANDIDATE.

---

## 3. Downstream theorem-status updates

The U2 arc was opened because U2 was the single shared residual conditionality on three downstream theorems. With U2 FORCED in the discrete regime, those conditionalities are now resolved:

### 3.1 Born rule (Theorem #10, born_gleason arc)

**Previous status:** FORCED for d ≥ 2 in the thin-participation regime, conditional on U2.

**New status:**
- **Discrete-graph chains:** **FORCED unconditional** for d ≥ 2 in the thin-participation regime.
- **Continuum-regime chains** (matter-wave, BEC, cosmological-scale): FORCED for d ≥ 2 in the thin-participation regime, conditional on the continuum lift of U2 (Primitive 12 thickening; separate U2-continuum arc).

### 3.2 Bell / Tsirelson (QM-emergence Step 4)

**Previous status:** FORCED conditional on U2 (sesquilinear inner product needed for Cauchy-Schwarz / operator-norm bounds underlying Tsirelson 2√2).

**New status:**
- **Discrete-graph chains:** **FORCED unconditional.** Tsirelson bound 2√2 holds for entangled bipartite participation measures on discrete graphs.
- **Continuum-regime chains:** FORCED conditional on U2 continuum lift.

### 3.3 Heisenberg uncertainty (QM-emergence Step 5)

**Previous status:** FORCED conditional on U2 (sesquilinear inner product needed for L² norm structure underlying Fourier-uncertainty `Δx · Δp ≥ ℏ/2`).

**New status:**
- **Discrete-graph chains:** **FORCED unconditional.** Bandwidth-allocation inequalities + the discrete-Fourier analog of Δx · Δp ≥ ℏ/2 hold.
- **Continuum-regime chains:** FORCED conditional on U2 continuum lift.

### 3.4 Consolidated downstream table

| Theorem | Pre-U2 status | Post-U2 status (discrete) | Post-U2 status (continuum) |
|---|---|---|---|
| Theorem #10 (Born, Gleason–Busch) | FORCED on U2 | **FORCED unconditional** | FORCED on continuum lift |
| Step 4 (Bell + Tsirelson) | FORCED on U2 | **FORCED unconditional** | FORCED on continuum lift |
| Step 5 (Heisenberg) | FORCED on U2 | **FORCED unconditional** | FORCED on continuum lift |

**Three theorems promoted from CANDIDATE-conditional to FORCED-unconditional in the discrete regime, by a single arc.**

---

## 4. The narrowed residual: continuum lift via Primitive 12

The discrete-regime FORCED verdict leaves one structural item open for continuum-regime applications: the lift of vertex counting measure to the emergent-manifold volume form via Primitive 12 thickening.

**What the continuum lift requires** (per Memo 03 §3.6):

1. **Primitive 12 thickening's measure-theoretic content.** A precise statement of how the discrete participation graph's vertex measure lifts to the emergent manifold M's volume form.
2. **Uniqueness of the emergent volume form.** Verification that the bandwidth-gradient / acoustic-metric structure (Phase-3 work) determines the volume form on M uniquely, with no conformal-rescaling or other freedom that would admit alternative continuum measures.
3. **Continuity of the inner product under the lift.** Verification that the continuum inner product `⟨P | Q⟩ = Σ_K ∫_M dμ(x) P_K*(x) Q_K(x)` is the well-defined limit of the discrete sum as the participation graph thickens — i.e., no measure-theoretic obstruction in the lift.

**Important framing:** these are *technical lift questions*, not new structural commitments. They draw on existing Primitive 12 and Phase-3 acoustic-metric work rather than amending primitives. The continuum-lift arc is anticipated to close FORCED with no new residuals — but the verification is its own session-length effort.

The conditionality has therefore *changed in character*. It moved:

- **From foundational** ("does ED have a Hilbert-space arena at all?") — settled by this arc,
- **To technical** ("does the discrete-to-continuum machinery preserve the inner-product structure?") — open for the U2-continuum follow-up arc.

This is a substantial sharpening even short of the full unconditional verdict.

---

## 5. The U2 arc's net contribution

**What the arc delivered:**

- One new theorem-grade structural result (U2 in the discrete regime).
- Promotion of three downstream theorems (Born, Bell/Tsirelson, Heisenberg) to FORCED-unconditional in the discrete regime.
- Narrowing of continuum-regime conditionality from foundational to technical.
- Zero new CANDIDATEs introduced.
- Identification of a clean follow-up arc (U2-continuum) with a focused, technical scope.

**What the arc did not deliver:**

- Continuum-regime unconditional U2. Deferred to the U2-continuum arc.
- A primitive-level account of the channel-K to QM-ray correspondence, or any extension beyond the structural question of inner-product form. (Out of scope for U2.)
- Any new physical predictions. The arc is a structural-derivation result; downstream phenomenology is unchanged from prior QM-emergence work.

**Comparative observation.** The U2 arc parallels the born_gleason arc in shape: both decomposed a single CANDIDATE into 3–8 sub-claims, found most automatic or interpretive, and located the load on a small number of substantive items that closed via primitive-level arguments. Both produced theorem-grade results without introducing new CANDIDATEs. The structural-derivation methodology is now established and replicable.

---

## 6. Verdict

**THEOREM ESTABLISHED — U2 is FORCED in the discrete participation-graph regime.**

The sesquilinear inner product `⟨P | Q⟩ = Σ_K Σ_u P_K*(u) Q_K(u)` is uniquely forced by ED's primitive stack — Primitives 01, 03, 04, 07, 09, 11 + the four-band orthogonality + the non-contextuality result inherited from born_gleason Memo 02 — without any new structural commitment.

**The three downstream theorems gating on U2 (Born / Bell+Tsirelson / Heisenberg) are now FORCED unconditional for chains operating on discrete participation graphs.**

For continuum-regime applications, a single technical conditionality remains: the lift of vertex counting measure to the emergent-manifold volume form via Primitive 12 thickening. This is the natural scope for a focused follow-up arc (U2-continuum), structurally analogous to but smaller than the present arc.

**The U2 arc is closed.**

---

## 7. Recommended Next Steps

**(a) Update memory record `project_qm_emergence_arc.md` with a single bundled package.** Per Memo 03 §10(c)'s recommendation, the post-arc state should be captured in one update covering: (i) the U2 arc's discrete-regime FORCED result, (ii) Theorem #10's promotion to FORCED-unconditional in the discrete regime, (iii) Step 4 and Step 5's parallel promotion, and (iv) the narrowed continuum-regime conditionality with the U2-continuum arc identified as the next high-leverage target. This bundled update is preferable to incremental edits across multiple memos; it gives a clean snapshot of the post-arc program state and makes the leverage of the U2 arc legible at a glance.

**(b) Decide whether to open the U2-continuum follow-up arc immediately or defer.** Two reasonable paths:
- **Open immediately.** The technical lift is the single remaining gate on three unconditional continuum-regime theorems; closing it completes the structural-foundations program for QM-emergence. Reasoning patterns from the present arc are still warm. Anticipated scope: 3 memos, structurally analogous to but smaller than U2.
- **Defer.** The discrete-regime result already buys substantial promotion. Continuum-regime applications can proceed with a single narrowed conditionality (the U2-continuum lift) as a flagged but acceptable residual, while attention shifts to other open program items (e.g., U3/U4 sibling derivations, empirical-track work).

The recommendation depends on the broader program priority. *Default suggestion:* open the U2-continuum arc immediately while the structural-derivation methodology and Primitive 12 / Phase-3 context are warm; deferring risks losing the methodological calibration developed across born_gleason + U2.

**(c) Write a short closure-and-summary memo (Memo 05) for the U2 arc.** Parallel to born_gleason Memo 06: canonical narrative summary of the arc, integration into the QM-emergence program, and a public-facing explainer section (potentially a follow-up to the existing `ED_Exponent2_Explainer.md` desktop piece, this time focused on "the structural foundation that makes the Born-Schrödinger-Heisenberg unification possible"). The closure memo serves both as the canonical entry-point for future cross-references and as the prep for any external write-up of the result.

---

## 8. Cross-references

**Within the U2 arc:**
- [`00_arc_outline.md`](00_arc_outline.md) — initial scoping
- [`01_decomposition_and_mapping.md`](01_decomposition_and_mapping.md) — C3a/b/c decomposition + primitive mapping
- [`02_C3a_C3b_derivation.md`](02_C3a_C3b_derivation.md) — C3a automatic + C3b forced
- [`03_C3c_discrete_regime.md`](03_C3c_discrete_regime.md) — C3c forced in discrete regime

**Downstream beneficiaries:**
- [`arcs/born_gleason/05_synthesis_theorem10.md`](../born_gleason/05_synthesis_theorem10.md) — Theorem #10 (Born); now unconditional in discrete regime
- [`arcs/born_gleason/06_closure_and_summary.md`](../born_gleason/06_closure_and_summary.md) — born_gleason canonical summary
- [`arcs/arc-foundations/bell_correlations_from_participation.md`](../arc-foundations/bell_correlations_from_participation.md) — Step 4 Bell/Tsirelson; now unconditional in discrete regime
- [`arcs/arc-foundations/uncertainty_from_participation.md`](../arc-foundations/uncertainty_from_participation.md) — Step 5 Heisenberg; now unconditional in discrete regime

**Source primitives:**
- Primitive 01 (micro-event, vertex primitivity): `quantum/primitives/01_micro_event.md`
- Primitive 03 (participation, edge structure): `quantum/primitives/03_participation.md`
- Primitive 04 (bandwidth, four-band orthogonality): `quantum/primitives/04_participation_bandwidth.md`
- Primitive 07 (channel ontology): `quantum/primitives/07_channel.md`
- Primitive 09 (polarity, U(1) phase): `quantum/primitives/09_tension_polarity.md`
- Primitive 11 (commitment): `quantum/primitives/11_commitment.md`
- Primitive 12 (thickening, relevant for U2-continuum follow-up arc): `quantum/primitives/12_thickening.md`

**Program reference:**
- [`papers/QM_Emergence_Structural_Completion/QM_Emergence_Structural_Completion.md`](../../papers/QM_Emergence_Structural_Completion/QM_Emergence_Structural_Completion.md) — synthesis paper; §4 upstream-CANDIDATE inventory should be updated to reflect U2 promotion
- Project memory: `memory/project_qm_emergence_arc.md`

---

## 9. One-line memo summary

> **U2 is FORCED in the discrete participation-graph regime: the sesquilinear inner product ⟨P | Q⟩ = Σ_K Σ_u P_K*(u) Q_K(u) is uniquely forced by Primitives 01+03+04+07+09+11 + four-band orthogonality + non-contextuality (born_gleason Memo 02), with no new structural commitment. Three downstream theorems (Theorem #10 Born / Step 4 Bell+Tsirelson / Step 5 Heisenberg) promote from FORCED-conditional-on-U2 to FORCED-unconditional in the discrete regime. Continuum-regime applications retain a single narrowed residual: the lift of vertex counting measure to the emergent-manifold volume form via Primitive 12 thickening — a technical lift question for the focused follow-up U2-continuum arc, not a foundational structural commitment. U2 arc closed.**
