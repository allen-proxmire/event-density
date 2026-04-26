# U2-Continuum Arc — Examination Outline

**Date opened:** 2026-04-26
**Location:** `arcs/U2_continuum/`
**Goal:** Determine whether the U2-discrete theorem (sesquilinear inner product FORCED on the participation graph's vertex-level structure) lifts uniquely to the continuum regime under Primitive 12 thickening + Phase-3 acoustic-metric structure.
**Predecessor work:** `arcs/U2/` (full discrete-regime arc; see [`05_closure_and_summary.md`](../U2/05_closure_and_summary.md) for the canonical entry-point).
**High-leverage status:** This arc closes the single remaining residual on Theorem #10 (Born), Step 4 (Bell/Tsirelson), and Step 5 (Heisenberg) for continuum-regime applications (matter-wave, BEC, cosmological-scale work). Closing it produces fully unconditional Born + Bell + Heisenberg across all regimes the QM-emergence program addresses.

---

## 1. The precise question

The U2-discrete theorem (`arcs/U2/04_synthesis_and_verdict.md` §2) established:

```
⟨P | Q⟩_discrete = Σ_K Σ_{u ∈ V} P_K*(u) · Q_K(u)                              (discrete)
```

is FORCED by the primitive stack on the discrete participation graph G = (V, E). The natural continuum analog — used implicitly in matter-wave, BEC, and cosmological-scale applications — is:

```
⟨P | Q⟩_continuum = Σ_K ∫_M dμ(x) · P_K*(x) · Q_K(x)                          (continuum)
```

where M is the emergent manifold supplied by Primitive 12 thickening and dμ(x) is its volume form.

**Question.** Does the discrete inner product lift uniquely to the continuum inner product under Primitive 12, or does the lift admit non-trivial alternatives (e.g., conformally-rescaled volume forms, smeared cross-vertex pairings, alternative continuum channel measures)?

If the lift is unique, U2-continuum FORCED, and the U2 program completes. If the lift admits non-trivial alternatives, the residual is identified precisely and the QM-emergence program retains a continuum-regime conditionality of clarified character.

---

## 2. The three sub-features to lift

The discrete inner product has three structural sub-features (per U2 Memo 03), each requiring a continuum analog:

- **(L1) Channel measure.** The discrete `Σ_K` (counting measure on 𝒦_τ(u), forced by Memo 03 §2). Continuum analog: still `Σ_K` for discrete channel sets, or `∫ dν(K)` for continuous channel spectra. The question is whether Primitive 07's countability statement (which underwrote counting measure in the discrete regime) carries over to the thick regime — and what happens if a chain's effective channel set becomes continuous (e.g., continuous momentum modes in matter-wave systems).

- **(L2) Position measure.** The discrete `Σ_u` (counting measure on V, forced by Memo 03 §3 in the discrete regime). Continuum analog: `∫_M dμ(x)` with dμ(x) the volume form on the emergent manifold M. **This is the load-bearing item for the arc.** The lift requires (a) a clean construction of M from G via Primitive 12, (b) uniqueness of the volume form dμ given the thickening structure, and (c) verification that the lift preserves the diagonal-equals-bandwidth constraint that fixed the discrete vertex measure.

- **(L3) Local pairing.** The discrete pointwise `P_K*(u) · Q_K(u)` (forced by Memo 03 §4 via four-band orthogonality + non-contextuality + kinematic/dynamic separation). Continuum analog: still pointwise `P_K*(x) · Q_K(x)` at each (channel, position) slot. The question is whether the continuum-limit of the discrete pointwise pairing remains pointwise, or whether the thickening machinery introduces smearing kernels (e.g., short-range correlation kernels from coarse-graining over many discrete events into a continuum patch).

**Anticipated structural difficulty:** L1 and L3 should lift cleanly (the structural arguments forbidding alternatives in the discrete regime carry over with minor modifications). L2 is the substantive item — the continuum measure construction has more moving parts (Primitive 12 thickening + Phase-3 acoustic metric + emergent volume form), and any non-uniqueness in those upstream pieces propagates into the lift.

---

## 3. Structural inputs from Primitive 12 and Phase-3

### 3.1 Primitive 12 — Thickening

From `quantum/primitives/12_thickening.md` §1–§2:

- **Thickening is the accumulation of committed micro-events into stable persistent structure.**
- **Discrete version:** `T(R, t) = Σ_{ε ∈ commitments in R up to t} w(ε)` — region-summed commitment weights.
- **Thick-regime field:** `τ(x, t) : M × ℝ → ℝ_{≥0}` — a density of accumulated thickness on the emergent manifold M.
- **Regime boundary:** `τ` large + smooth → continuum-field description valid; `τ ≈ 0` → graph-only description.
- **Open items** (per Primitive 12 §2.13): exact weighting w(ε), precise thickness threshold for continuum validity, local un-thickening rates, saturation behavior.

**What Primitive 12 supplies for the U2 lift:** the existence of an emergent manifold M when τ is sufficiently large and smooth, with bandwidth fields and channel structures inheriting continuum descriptions.

**What Primitive 12 does not yet supply:** an explicit, uniquely determined volume form dμ on M. The existence of M is established; the metric structure that determines dμ is the province of the Phase-3 acoustic-metric arc.

### 3.2 Phase-3 acoustic-metric work

From `memory/project_qm_emergence_arc.md` (Phase-3 closure summary):

- **Phase-3 closed (six memos GR.0–GR.5)** with Theorem GR1 (V1 with Synge world function FORCED) and four cascading FORCED-conditional results.
- **ED-Phys-10 acoustic-metric-only baseline preserved:** ED has a kinematic acoustic metric on M, derived from bandwidth gradients (Primitive 06 ED-gradient + Primitive 04). No Einstein equations, no Schwarzschild, no Newtonian gravity emergence.
- **Implication for U2 lift:** the acoustic metric on M supplies a unique metric structure (modulo conformal-rescaling questions, which are part of what Memo 03 of this arc must check), which in turn supplies a unique volume form dμ via the standard differential-geometric construction (g_{μν} → √|g| dx^d).

**What Phase-3 supplies for the U2 lift:** a candidate metric on M (the acoustic metric from bandwidth gradients), with a corresponding candidate volume form.

**What Phase-3 does not yet supply (potential sticking point):** verification that this metric / volume form is *uniquely* determined by the primitive structure, with no conformal-rescaling or other freedom that would admit alternative measures. The ED-SC arcs and GR-SC arcs have done substantial work on the acoustic-metric structure, but the explicit "is the volume form unique?" question may need to be addressed within the present arc.

---

## 4. Falsification conditions

The arc is **closed FORCED** if all three lift sub-features (L1, L2, L3) close uniquely under Primitive 12 + Phase-3 inputs.

The arc is **closed CONDITIONAL** if L1 and L3 close uniquely but L2 admits a non-trivial alternative (e.g., conformal-rescaling of the volume form) consistent with the primitive structure. The residual would be identified precisely (e.g., "U2-continuum FORCED up to a single scalar conformal factor in the volume form, which is itself conditional on a separate metric-uniqueness derivation").

The arc is **closed NOT FORCED** if any of L1, L2, L3 admits a *physically distinct* alternative — meaning a different inner-product structure that satisfies the primitives and produces a different downstream phenomenology than standard QM in the continuum regime.

**Specific sub-falsifiers to watch for:**

- **(F2-cont — alternative continuum channel measure).** If Primitive 07 admits continuum channel spectra (e.g., continuous momentum modes) but the natural lift of the counting measure is *not* uniquely Lebesgue-on-channel-space, the channel-aggregation in the continuum could admit non-trivial alternatives.

- **(F3-cont — alternative continuum position measure).** If the emergent manifold M's volume form is not uniquely determined by the acoustic metric — e.g., if conformal rescalings g → e^{2σ} g are consistent with all primitives — then dμ could be replaced by e^{dσ} dμ for arbitrary scalar σ, giving a one-parameter family of valid continuum inner products. This is the most likely source of a CONDITIONAL verdict.

- **(F1′-cont — non-local cross-slot terms in continuum).** If the discrete-to-continuum coarse-graining introduces correlation kernels at the thickening scale (analogous to UV-cutoff effects in QFT), the continuum pairing could include short-range smearing rather than strict pointwise locality.

- **(F-thickening — Primitive 12 internal residuals).** Primitive 12 §2.13 lists open items (weighting w(ε), threshold τ for continuum validity, un-thickening rates). If any of these proves to gate the continuum lift in an unresolved way, the arc must either (a) close those upstream items en route, or (b) declare the lift CONDITIONAL on Primitive 12's internal residuals being settled separately.

---

## 5. Memo structure (3 memos)

### Memo 1: `01_decomposition_and_p12_mapping.md`
Decompose the lift question into L1 + L2 + L3. For each, identify which Primitive 12 + Phase-3 inputs are needed and what discrete-regime arguments must transfer. Survey what existing Primitive 12 and Phase-3 work supplies (and what it does not). Status: pure structural inventory; no derivation yet. Inventory analogous to U2 Memo 01 and born_gleason Memo 01.

### Memo 2: `02_L1_and_L3_continuum_derivation.md`
Derive L1 (continuum channel measure) and L3 (local pointwise pairing) directly from the discrete-regime results + Primitive 12 lift. Anticipated outcome: both close cleanly with minor modifications to the discrete arguments. Specifically:
- **L1:** the discrete counting-measure argument (no primitive source for non-trivial channel weighting + diagonal-equals-bandwidth constraint) lifts directly to the continuum case for discrete channel sets; for continuous channel spectra (e.g., continuous momentum), the natural Lebesgue-on-channel-space measure is forced by the same arguments applied to the continuum channel space.
- **L3:** four-band orthogonality + non-contextuality + kinematic/dynamic separation all carry over to the continuum verbatim. Smearing alternatives (F1′-cont) are blocked by the same arguments at the continuum scale.

### Memo 3: `03_L2_position_measure_and_verdict.md`
The load-bearing memo. Examines whether the continuum position measure dμ on M is uniquely determined by Primitive 12 thickening + Phase-3 acoustic-metric structure, or whether genuine alternatives (most likely conformal rescalings) survive. Three sub-questions:
- (a) Is the emergent manifold M uniquely constructed from G under thickening?
- (b) Is the metric on M uniquely determined by the bandwidth-gradient / acoustic-metric structure?
- (c) Is the volume form dμ uniquely determined by the metric (modulo standard differential-geometric conventions)?

If all three close affirmatively, U2-continuum FORCED. If (b) admits conformal rescaling, U2-continuum CONDITIONAL on conformal-fixing. If (a) admits multiple inequivalent thickening lifts, U2-continuum CONDITIONAL on choice of lift. If all three fail in informative ways, U2-continuum is genuinely NOT FORCED with consequences for the QM-emergence program's continuum-regime claims.

This memo also delivers the arc's verdict and updates the downstream-theorem table accordingly.

---

## 6. First-session scope

Memos 01 and 02. Memo 01 is the structural inventory; Memo 02 is the cleaner of the two derivation memos and should close cleanly. The substantive load lands in Memo 03, which is a distinct session-length effort.

**Predicted outcome for Memos 01–02 (to be tested, not assumed):** L1 and L3 lift cleanly. The discrete-regime arguments transfer with minor modifications. The contested question is L2 (the volume form), addressed in Memo 03.

**Anticipated risk for Memo 03:** the conformal-rescaling question. ED's acoustic metric is derived from bandwidth gradients; whether that determination is conformal-invariant or conformal-fixing is a structural question the present arc may need to settle, drawing on existing GR-SC and Phase-3 work but possibly requiring its own focused argument.

---

## 7. Comparative observation

The U2-continuum arc's structural shape mirrors but is smaller than U2-discrete:

| Parameter | U2-discrete | U2-continuum |
|---|---|---|
| Memo count | 5 (00 + 4 work memos) | 4 (00 + 3 work memos) |
| Sub-commitment count | 3 (C3a, C3b, C3c) | 3 (L1, L2, L3) |
| Automatic items | 1 (C3a) | 0 (all three are lift questions) |
| Forced-via-derivation items | 1 (C3b) | 2 (L1, L3 anticipated) |
| Load-bearing items | 1 (C3c, with 3 sub-features) | 1 (L2) |
| Inherited structural inputs | Primitives 04, 07, 09, 11 + four-band orthogonality + non-contextuality | U2-discrete result + Primitive 12 + Phase-3 acoustic-metric work |
| Anticipated verdict | FORCED (working hypothesis) | FORCED with non-trivial conformal-rescaling concern |

The arc inherits more structural infrastructure than U2-discrete did (Primitive 12 + Phase-3 inputs), which both helps (more is in hand) and adds risk (more upstream items have their own conditionalities that could propagate).

---

## 8. Recommended Next Steps

**(a) Begin Memo 01 (decomposition + Primitive 12 mapping).** Natural next session step. Should be a tight inventory parallel to U2 Memo 01: decompose the lift into L1/L2/L3, map each to Primitive 12 and Phase-3 inputs, classify status and load-bearing items. Setting up this inventory cleanly will let Memos 02 and 03 target specific items rather than re-deriving the lift from scratch.

**(b) Pre-Memo-01 audit of Phase-3 acoustic-metric work, particularly conformal-uniqueness statements.** The most likely sticking point in Memo 03 is whether the acoustic metric on M is conformally fixed or admits rescaling freedom. A short scan of `arcs/arc-foundations/` (especially Phase-3 GR.0–GR.5 memos), `arcs/arc-acoustic/`, and the relevant ED-SC arcs for explicit conformal-uniqueness statements before drafting Memo 01 will identify whether this question has already been settled elsewhere (in which case Memo 03's scope shrinks) or whether it remains open (in which case Memo 03 must address it directly).

**(c) Don't update memory or downstream tables until Memo 03 verdict.** Same discipline as the U2-discrete arc: avoid memory churn by waiting until the arc's verdict is known. The bundled memory update recommended in U2 Memo 04 §7(a) and Memo 05 §9(a) should still be done before this arc opens, so the post-U2-discrete state is captured cleanly. After Memo 03 of the present arc closes, a second bundled update can record the final post-arc state across both arcs.

---

## 9. Cross-references

- U2-discrete arc (canonical entry-point): [`arcs/U2/05_closure_and_summary.md`](../U2/05_closure_and_summary.md)
- U2-discrete theorem statement: [`arcs/U2/04_synthesis_and_verdict.md`](../U2/04_synthesis_and_verdict.md)
- Born_gleason arc (Theorem #10, downstream beneficiary of continuum-lift completion): [`arcs/born_gleason/06_closure_and_summary.md`](../born_gleason/06_closure_and_summary.md)
- Step 4 Bell/Tsirelson (downstream beneficiary): [`arcs/arc-foundations/bell_correlations_from_participation.md`](../arc-foundations/bell_correlations_from_participation.md)
- Step 5 Heisenberg (downstream beneficiary): [`arcs/arc-foundations/uncertainty_from_participation.md`](../arc-foundations/uncertainty_from_participation.md)
- Phase-3 GR-arc (Theorem GR1, acoustic-metric inputs): `arcs/arc-phase-3/`
- ED-Phys-10 acoustic-metric closure (per memory): cross-referenced in `memory/project_ed10_geometry_qft_scope.md`
- Primitive 04 (bandwidth, four-band orthogonality): `quantum/primitives/04_participation_bandwidth.md`
- Primitive 06 (ED-gradient, supplies bandwidth-gradient input to acoustic metric): `quantum/primitives/06_ed_gradient.md`
- Primitive 07 (channel ontology + countability statement): `quantum/primitives/07_channel.md`
- Primitive 09 (polarity, U(1) phase): `quantum/primitives/09_tension_polarity.md`
- Primitive 11 (commitment, accumulating into thickening): `quantum/primitives/11_commitment.md`
- Primitive 12 (thickening, central to this arc): `quantum/primitives/12_thickening.md`
- Project memory: `memory/project_qm_emergence_arc.md`, `memory/project_ed10_geometry_qft_scope.md`, `memory/project_ed_gr_sc_arc.md`

---

## 10. One-line arc summary

> **Test whether the discrete-regime U2 inner product `⟨P | Q⟩ = Σ_K Σ_u P_K*(u) Q_K(u)` lifts uniquely to the continuum form `⟨P | Q⟩ = Σ_K ∫ dμ(x) P_K*(x) Q_K(x)` under Primitive 12 thickening + Phase-3 acoustic-metric structure. Three sub-features to check: (L1) channel measure, (L2) position measure (load-bearing — most likely sticking point is conformal-rescaling of the emergent volume form), (L3) local pointwise pairing. If FORCED, three downstream theorems (Born #10, Bell/Tsirelson, Heisenberg) become unconditional in continuum regime simultaneously, completing the QM-emergence program's structural foundation across all regimes. If CONDITIONAL or NOT FORCED, the residual is identified precisely as a property of the emergent-manifold structure rather than of the inner-product structure itself.**
