# Memo 01 — Continuum-Lift Decomposition and Primitive 12 / Phase-3 Mapping

**Date:** 2026-04-26
**Arc:** `arcs/U2_continuum/`
**Predecessor:** [`00_arc_outline.md`](00_arc_outline.md)
**Status:** Structural inventory memo. Decomposes the U2-continuum lift question into three sub-features (L1, L2, L3), maps each to the structural inputs supplied by Primitive 12 (thickening) and the Phase-3 acoustic-metric work, and classifies each by structural status (automatic / forced-via-derivation / load-bearing). Continuum analog of U2-discrete Memo 01.
**Purpose:** Pin down the conceptual terrain so Memo 02 can derive L1 + L3 directly and Memo 03 can focus on the load-bearing L2 (volume form) question, including the conformal-uniqueness sticking point.

---

## 1. Setup

### 1.1 The discrete starting point (inherited from U2-discrete arc)

From [`arcs/U2/04_synthesis_and_verdict.md`](../U2/04_synthesis_and_verdict.md) §2, the discrete inner product on the participation graph G = (V, E) is FORCED:

```
⟨P | Q⟩_disc = Σ_K Σ_{u ∈ V} P_K*(u) · Q_K(u)                                  (1)
```

with diagonal recovering total bandwidth and four-band orthogonality preserved.

### 1.2 The continuum target

The natural continuum analog — the inner product implicit in matter-wave, BEC, and cosmological-scale applications — is:

```
⟨P | Q⟩_cont = Σ_K ∫_M dμ(x) · P_K*(x) · Q_K(x)                                (2)
```

where:
- M is the emergent manifold supplied by Primitive 12 thickening,
- dμ(x) is its volume form,
- P_K(x), Q_K(x) are the continuum participation-measure values at point x ∈ M.

### 1.3 The lift question

Each structural feature of (1) must lift uniquely to (2) under Primitive 12 thickening + Phase-3 acoustic-metric structure. Three sub-features carry distinct structural content:

- **L1.** The channel aggregation `Σ_K` lifts to its continuum analog (still `Σ_K` for discrete channel sets, possibly `∫ dν(K)` for continuous channel spectra).
- **L2.** The vertex aggregation `Σ_u` lifts to `∫_M dμ(x)` with a uniquely determined volume form dμ.
- **L3.** The local pointwise pairing `P_K*(u) Q_K(u)` lifts to its continuum analog `P_K*(x) Q_K(x)` without acquiring smearing kernels or non-local cross-slot contributions.

This memo decomposes each, maps to upstream inputs, and classifies status.

---

## 2. L1 — Channel measure in the continuum

### 2.1 The continuum requirement

For the continuum inner product (2) to be well-defined, the channel-aggregation `Σ_K` (or its continuous analog) must:

- be a measure on the channel set 𝒦(x) at each x ∈ M;
- reduce to the discrete counting measure when 𝒦 is finite or countable;
- be uniquely determined by the primitive structure for any continuum-spectrum case (e.g., continuous momentum modes in matter-wave applications).

Two regimes to distinguish:

- **(L1-discrete-channels)** 𝒦(x) remains finite or countable in the continuum spatial regime. The aggregation is still `Σ_K` with counting measure — directly inherited from U2-discrete Memo 03 §2 with the spatial argument changed from u ∈ V to x ∈ M.
- **(L1-continuous-channels)** 𝒦(x) becomes a continuous spectrum (e.g., continuous momentum, position-basis channels for matter waves). The aggregation becomes `∫ dν(K)` with measure ν on the channel space — and the question is whether ν is uniquely forced.

### 2.2 Primitive 12 inputs

Primitive 12's thickening field τ(x, t) supports continuum descriptions where bandwidth fields are smooth and channel structures inherit continuum descriptions. Specifically:

- For a chain at thick-regime point x ∈ M with bandwidth field b_K(x), the channel set 𝒦(x) can be either discrete (e.g., internal-state channels of an atom) or continuous (e.g., momentum modes), depending on the rule-type and the chain's spatial structure.
- The thickening machinery does *not* itself force discreteness or continuity of 𝒦 — that is determined by the chain's rule-type (Primitive 07) and the surrounding participation-graph structure.

**What Primitive 12 supplies for L1:** continuity of bandwidth fields b_K(x) along the spatial argument; no direct constraint on the channel-space measure ν.

### 2.3 Phase-3 acoustic-metric inputs

Phase-3 work supplies the spatial metric structure on M but not the channel-space measure. Channels are not "directions in M"; they are pathways through participation structure (Primitive 07 §1). Channel space is a separate index set, not a fiber of the spacetime tangent bundle.

**What Phase-3 supplies for L1:** nothing direct. Channel-space measure is independent of the spatial metric.

### 2.4 Classification

The continuum lift of the channel measure is structurally analogous to the discrete case. The discrete arguments (no primitive-level inter-channel weighting + diagonal-equals-bandwidth constraint) carry over with minor rewording. For continuous channel spectra, the same arguments apply to the continuous channel space, forcing Lebesgue-on-channel-space (the natural continuous analog of counting measure).

**Status: FORCED-VIA-DERIVATION.** Memo 02 will execute the lift, using the same structural arguments that closed C3c-(i) in the discrete regime. No new structural inputs needed; expected to close cleanly.

---

## 3. L2 — Position measure in the continuum (the load-bearing item)

### 3.1 The continuum requirement

The vertex aggregation `Σ_u` must lift to a position integral `∫_M dμ(x)` with a uniquely determined volume form dμ. The lift requires:

- **(L2-i)** A clean construction of the emergent manifold M from the discrete graph G under thickening.
- **(L2-ii)** A unique metric structure g_{ab} on M, determined by primitive-level inputs.
- **(L2-iii)** A unique volume form `dμ(x) = √|g(x)| · d^D x` derived from the metric (with D = dim M).
- **(L2-iv)** Continuity of the lift: the discrete inner product (1), evaluated on a coarse-grained version of (P, Q), converges to the continuum inner product (2) as the thickening density τ → ∞.

Each of (L2-i)–(L2-iv) draws on different upstream inputs.

### 3.2 Primitive 12 inputs

From `quantum/primitives/12_thickening.md`:

- **(P12-existence) Existence of M.** When τ is large and smooth, the participation graph admits a coarse-graining yielding a smooth emergent manifold M. This is the structural content of Primitive 12 §1 ("A region that has thickened supports: A smooth emergent manifold (because participation adjacency is dense and regular)").

- **(P12-thickness-field) The thickness field τ(x, t).** A scalar density on M counting accumulated commitments. Distinguishes thin-regime (graph-only) from thick-regime (continuum) regions.

- **(P12-residuals) Open items.** Primitive 12 §2.13 explicitly lists open items: the precise weighting w(ε) for thickness accumulation, the exact threshold for continuum validity, local un-thickening rates, saturation behavior at τ_max. **These residuals could potentially gate the continuum lift if they prove load-bearing.**

**What Primitive 12 supplies for L2:** existence of M when τ is sufficiently large and smooth, with bandwidth fields and channel structures inheriting continuum descriptions. Does not by itself supply a uniquely-determined volume form.

### 3.3 Phase-3 acoustic-metric inputs

From `memory/project_qm_emergence_arc.md` (Phase-3 closure summary) + `memory/project_ed10_geometry_qft_scope.md`:

- **(Phase-3-metric) ED has a kinematic acoustic metric on M, derived from bandwidth gradients.** Specifically: from Primitive 06 (ED-gradient ∇ρ) + Primitive 04 (bandwidth field b), the acoustic metric `g_{ab}(x)` is constructed analogously to Unruh's acoustic metric in fluid mechanics. The ED-Phys-10 arc closure preserves this baseline.

- **(Phase-3-scope) ED has acoustic metric only.** No Einstein equations, no Schwarzschild, no Newtonian-gravity emergence (per ED-Phys-10 guardrails). The metric is kinematic, not dynamical.

- **(Phase-3-volume-form-candidate) Candidate volume form √|g| d^D x.** Once a metric is in hand, the standard differential-geometric construction supplies a volume form. The question is whether this volume form is uniquely fixed by the primitive structure or admits rescaling freedom.

**What Phase-3 supplies for L2:** a candidate acoustic metric on M with a corresponding candidate volume form. Verification of uniqueness against conformal rescaling is the explicit Memo 03 question.

### 3.4 The conformal-uniqueness sticking point

**The likely sticking point.** Conformal rescaling `g_{ab} → e^{2σ(x)} g_{ab}` for an arbitrary smooth scalar field σ(x) preserves angles but rescales volumes: `√|g| → e^{Dσ} √|g|`, hence `dμ → e^{Dσ} dμ`. If two metrics in the same conformal class are equally consistent with ED's primitive structure, then the volume form is not uniquely fixed, and the continuum inner product admits a one-parameter family `⟨P | Q⟩_σ = Σ_K ∫_M e^{Dσ(x)} dμ(x) P_K*(x) Q_K(x)` of valid alternatives.

**Whether this is a real concern depends on whether the primitive structure conformally fixes the metric.** Two structural arguments in the existing program suggest it might:

- The bandwidth field `b(x)` itself supplies an absolute scale (it is not conformally invariant). The acoustic metric's construction from `b` and `∇ρ` involves these fields directly, plausibly fixing their absolute normalization.
- The diagonal-equals-bandwidth constraint (the same constraint that fixed the discrete vertex measure) imposes an absolute normalization on the continuum inner product: `⟨P | P⟩ = Σ_K ∫ dμ(x) b_K(x) = total bandwidth`. If `total bandwidth` is a primitive-level quantity (and Primitive 04's four-band conservation suggests it is, modulo dynamics), then dμ is fixed by the requirement that the integral reproduce that quantity.

But neither argument is fully developed in the existing program. **Memo 03 must either complete one of these arguments or identify the conformal residual as the arc's CONDITIONAL closure.**

### 3.5 Classification

**Status: LOAD-BEARING.** L2 carries the substantive work of the arc. Primitive 12 supplies M's existence; Phase-3 supplies a candidate metric and volume form; the question is whether the volume form is uniquely fixed against conformal rescaling. Two plausible structural arguments exist (bandwidth's absolute scale, diagonal-equals-bandwidth constraint) but neither is fully worked out. Memo 03 carries the load.

---

## 4. L3 — Local pairing in the continuum

### 4.1 The continuum requirement

The discrete pointwise pairing `P_K*(u) Q_K(u)` must lift to the continuum pointwise pairing `P_K*(x) Q_K(x)` at each (channel, position) slot, with no smearing kernels or non-local cross-slot contributions introduced by the thickening / coarse-graining process.

The continuum-most-general sesquilinear pairing consistent with L1 + L2 is:

```
⟨P | Q⟩ = Σ_K Σ_{K'} ∫_M ∫_M dμ(x) dμ(x') · P_K*(x) · K(K, K'; x, x') · Q_{K'}(x')   (3)
```

with kernel `K(K, K'; x, x') ∈ ℂ`. The pointwise local form has `K(K, K'; x, x') = δ_{KK'} · δ(x − x')` (Dirac delta in the continuum). The question is whether non-trivial off-diagonal kernel components are forced to vanish.

### 4.2 Primitive 12 inputs

Primitive 12's coarse-graining could in principle introduce **finite-resolution smearing**: the discrete-to-continuum lift averages over a thickening-scale neighborhood, which could leave residual short-range correlation kernels analogous to UV-cutoff effects in QFT.

Whether such smearing arises depends on whether Primitive 12's coarse-graining is structurally lossless (the continuum inner product is the strict τ → ∞ limit of the discrete sum) or introduces a residual kernel at the thickening scale.

**What Primitive 12 supplies for L3:** the coarse-graining machinery itself; structural verification of losslessness is part of Memo 03's L2-(iv) continuity check, but the L3 pointwise-locality question can be addressed in parallel using the discrete-regime L3 arguments transferred to the continuum.

### 4.3 Phase-3 acoustic-metric inputs

The acoustic metric structure does not directly bear on the L3 question. The metric supplies the volume form (L2) and the geometric structure for ∫_M; it does not introduce smearing kernels.

**What Phase-3 supplies for L3:** nothing direct.

### 4.4 Discrete-regime arguments transferring to the continuum

The U2-discrete Memo 03 §4 argument forbidding cross-slot kernel terms had three independent components:

- **(D-ortho)** Four-band orthogonality forbids cross-band kernel terms. **Transfers verbatim to the continuum** — four-band orthogonality is a Primitive 04 §1.5 statement, regime-independent.
- **(D-context)** Non-contextuality from channel primitivity (born_gleason Memo 02) forbids cross-channel kernel terms within a band. **Transfers verbatim to the continuum** — channel ontology is regime-independent (Primitive 07 §1).
- **(D-kin)** Kinematic/dynamic separation forbids cross-vertex (cross-position in continuum) kernel terms — these belong in the dynamics (Step 2's H_K, V_{KK'}), not in the kinematic norm. **Transfers verbatim to the continuum** — the kinematic/dynamic separation is regime-independent.

All three discrete-regime arguments transfer cleanly. The single new continuum-specific concern is potential smearing from Primitive 12 coarse-graining (F1′-cont), which Memo 02 should address explicitly.

### 4.5 Classification

**Status: FORCED-VIA-DERIVATION.** The discrete arguments transfer with minor modifications; Memo 02 will execute the transfer plus the Primitive-12-smearing check. Expected to close cleanly.

---

## 5. Joint structural status

| Sub-feature | Description | Primitive 12 input | Phase-3 input | Status |
|---|---|---|---|---|
| **L1** | Channel measure (Σ_K → Σ_K or ∫ dν(K)) | Continuity of b_K(x) along x | None direct | **FORCED-VIA-DERIVATION** (Memo 02) |
| **L2** | Position measure (Σ_u → ∫_M dμ(x)) | Existence of M; thickness field τ; **internal residuals (P12 §2.13) potentially gating** | Acoustic metric g_{ab}; candidate volume form √|g| d^D x; **conformal-uniqueness explicitly open** | **LOAD-BEARING** (Memo 03) |
| **L3** | Local pointwise pairing (P_K*(u) Q_K(u) → P_K*(x) Q_K(x)) | Coarse-graining machinery; smearing-or-not question | None direct | **FORCED-VIA-DERIVATION** (Memo 02; includes smearing check) |

**The arc's verdict reduces almost entirely to Memo 03's treatment of L2.** L1 and L3 are anticipated to close cleanly via discrete-argument transfer + minor continuum-specific checks. The substantive question is whether the continuum volume form is uniquely fixed by the primitive structure or admits conformal-rescaling alternatives.

---

## 6. Falsifier table for the continuum regime

The arc outline §4 identified four sub-falsifiers. With the L1/L2/L3 decomposition and Primitive 12 / Phase-3 mapping in hand, each falsifier attaches to a specific sub-feature:

| Falsifier | Description | Attaches to | Resolution path |
|---|---|---|---|
| **F2-cont** | Alternative continuum channel measure (non-Lebesgue-on-channel-space ν) | L1 | Memo 02 (transfer of discrete-counting argument to continuum channel spaces) |
| **F3-cont** | Alternative continuum position measure (most likely conformal rescaling of dμ) | L2 | Memo 03 (conformal-uniqueness of acoustic-metric volume form) |
| **F1′-cont** | Non-local cross-slot terms in continuum (smearing kernels from Primitive 12 coarse-graining or cross-channel/cross-position contributions) | L3 | Memo 02 (discrete-argument transfer + Primitive-12-smearing check) |
| **F-thickening** | Primitive 12 internal residuals (weighting w(ε), threshold τ for continuum validity, un-thickening rates, saturation) gate the lift | L2 (and potentially L1, L3) | Memo 03 (assess whether any P12 §2.13 residual is load-bearing for the lift; if so, declare the lift CONDITIONAL on that residual) |

Two falsifiers attach to L2 (F3-cont and F-thickening, both potentially), confirming L2's load-bearing status. F2-cont and F1′-cont attach to L1 and L3 respectively and are anticipated to be dispatched cleanly in Memo 02.

---

## 7. The likely sticking point, foregrounded

**Conformal-uniqueness of the volume form is the explicit Memo 03 question.** Based on the mapping above, three structural arguments could in principle settle it affirmatively (each explored in Memo 03):

1. **Bandwidth's absolute scale.** The bandwidth field b(x) carries an absolute physical scale (set by the chain's persistence-regime budget per Primitive 04). Constructions that build the metric from b should inherit this absolute scale and conformally fix it.

2. **Diagonal-equals-bandwidth constraint.** The continuum inner product's diagonal must equal total bandwidth: `⟨P | P⟩ = Σ_K ∫ dμ(x) b_K(x) = b_total`. If b_total is primitive-level fixed (modulo dynamics), the constraint `Σ_K ∫ dμ(x) b_K(x) = b_total` for all P fixes dμ given the b_K profile, eliminating conformal freedom.

3. **Acoustic-metric construction.** The acoustic-metric construction from bandwidth gradients (Phase-3 work) involves dimensional inputs (b has units, ∇ρ has units) that may by themselves conformally fix the metric. Verification requires examining the explicit Phase-3 construction.

Each of these is a candidate route to closure. Memo 03 must develop at least one rigorously, or — if all three fail — identify the conformal residual as the arc's CONDITIONAL closure with a precisely stated residual.

**Anticipated outcome.** Argument 2 (diagonal-equals-bandwidth) is the cleanest and most directly inherited from the discrete-regime work. Memo 03 should likely lead with this argument; if it closes, F3-cont is dispatched and L2 is FORCED.

---

## 8. Comparative observation

The U2-continuum decomposition mirrors but is structurally tighter than U2-discrete:

| Parameter | U2-discrete | U2-continuum |
|---|---|---|
| Sub-commitment / sub-feature count | 3 (C3a, C3b, C3c with 3 sub-features) | 3 (L1, L2, L3) |
| Automatic items | 1 (C3a) | 0 (all three are lift questions) |
| Forced-via-derivation items | 1 (C3b) | 2 (L1, L3) |
| Load-bearing items | 1 (C3c, with 3 sub-features and 3 falsifiers) | 1 (L2, with 4 sub-requirements and 2 falsifiers) |
| Inherited inputs | Primitives 04, 07, 09, 11 + four-band orthogonality | U2-discrete result + Primitive 12 + Phase-3 acoustic metric |
| Anticipated headline risk | Channel non-contextuality | Conformal-uniqueness of volume form |

The arc inherits more upstream infrastructure than U2-discrete did. This both helps (more is in hand) and adds risk (Primitive 12's own internal residuals could propagate; the Phase-3 work has its own conditionalities).

---

## 9. Recommended Next Steps

**(a) Begin Memo 02 (L1 + L3 derivation).** Natural next session step. Both L1 and L3 are anticipated to close via discrete-argument transfer + minor continuum-specific checks (continuous channel spectra for L1; Primitive-12-smearing for L3). Should be a moderately tight memo, similar in size to U2-discrete Memo 02 but with additional continuum-specific content. Expected outcome: clean closure with both L1 and L3 forced.

**(b) Pre-Memo-03 audit of Phase-3 acoustic-metric work for explicit conformal-uniqueness statements.** This was flagged in arc outline §8(b) and remains the most important pre-Memo-03 preparation. Specifically: scan the Phase-3 GR-arc memos (`arcs/arc-phase-3/` if available, otherwise the GR.0–GR.5 references in `memory/project_qm_emergence_arc.md`), `arcs/arc-acoustic/`, and the `arcs/arc-GR-SC/` work for any explicit derivation that fixes the acoustic-metric conformal class. If found, Memo 03 can quote it directly and the conformal-rescaling falsifier is dispatched cheaply. If not found, Memo 03 must develop the diagonal-equals-bandwidth argument (§7 candidate 2) from scratch.

**(c) Address Primitive 12 internal residuals (P12 §2.13) as a scoping question for Memo 03.** Primitive 12's open items (weighting w(ε), continuum-validity threshold, un-thickening rates) could in principle gate the continuum lift. Memo 03 should explicitly address whether any of these is load-bearing for L2's continuity check (L2-iv). Two paths: (a) demonstrate that L2 closure is robust against P12's internal residuals (each open item is independent of the inner-product structure), in which case the lift is unconditionally FORCED; (b) identify a P12 residual that does propagate, in which case the lift is CONDITIONAL on that residual and the U2-continuum verdict inherits that conditionality. Path (a) is anticipated and preferred — the structural separation between Primitive 12's accumulation dynamics and the inner-product structure suggests independence — but the verification is its own line of work in Memo 03.

---

## 10. Cross-references

- Arc outline: [`arcs/U2_continuum/00_arc_outline.md`](00_arc_outline.md)
- U2-discrete arc (canonical entry-point + theorem statement): [`arcs/U2/05_closure_and_summary.md`](../U2/05_closure_and_summary.md), [`arcs/U2/04_synthesis_and_verdict.md`](../U2/04_synthesis_and_verdict.md)
- U2-discrete Memo 03 (load-bearing memo, parallel template for this arc's Memo 03): [`arcs/U2/03_C3c_discrete_regime.md`](../U2/03_C3c_discrete_regime.md)
- Born_gleason Memo 02 (non-contextuality, source for L3 §4.4 transfer argument): [`arcs/born_gleason/02_noncontextuality_argument.md`](../born_gleason/02_noncontextuality_argument.md)
- Phase-3 GR-arc and acoustic-metric work (sources for L2 §3.3 inputs): `arcs/arc-phase-3/`, `arcs/arc-acoustic/`, `arcs/arc-GR-SC/`
- Project memory (Phase-3 closure summary, ED-Phys-10 acoustic-metric baseline): `memory/project_qm_emergence_arc.md`, `memory/project_ed10_geometry_qft_scope.md`, `memory/project_ed_gr_sc_arc.md`
- Primitive 04 (bandwidth, four-band orthogonality, absolute scale): `quantum/primitives/04_participation_bandwidth.md`
- Primitive 06 (ED-gradient, supplies bandwidth-gradient input to acoustic metric): `quantum/primitives/06_ed_gradient.md`
- Primitive 07 (channel ontology, regime-independent): `quantum/primitives/07_channel.md`
- Primitive 12 (thickening, central to L2 + smearing question for L3): `quantum/primitives/12_thickening.md`

---

## 11. One-line memo summary

> **U2-continuum decomposes into L1 (channel measure, FORCED-VIA-DERIVATION via discrete-argument transfer), L2 (position measure, LOAD-BEARING — hinges on conformal-uniqueness of the acoustic-metric volume form), and L3 (local pairing, FORCED-VIA-DERIVATION via four-band orthogonality + non-contextuality + kinematic/dynamic separation transferring verbatim, plus a Primitive-12-smearing check). Primitive 12 supplies M's existence and thickness field τ but not by itself a uniquely fixed volume form; Phase-3 acoustic-metric work supplies a candidate metric and volume form with conformal-uniqueness explicitly open. The likely Memo 03 closure path is the diagonal-equals-bandwidth argument: requiring `⟨P | P⟩ = Σ_K ∫ dμ(x) b_K(x) = b_total` for all P fixes dμ given the b_K profile, eliminating conformal freedom. Falsifier table maps F2-cont → L1, F3-cont + F-thickening → L2, F1′-cont → L3.**
