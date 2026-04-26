# U5 Arc — Examination Outline

**Date opened:** 2026-04-26
**Location:** `arcs/U5/`
**Goal:** Determine whether U5 — the adjacency-band Fourier-conjugate partition `b^{adj} = b_x + b_p` — is FORCED, CONDITIONAL, or NOT FORCED by ED's primitives, the participation-measure framework, and the now-FORCED U2 inner-product structure.
**Predecessor work:** `arcs/arc-foundations/u5_adjacency_partition_derivation.md` (2026-04-24 tightening-program attempt; claimed FORCED status but predates the structural-derivation methodology established in born_gleason + U2 + U2-continuum). Synthesis paper [`papers/QM_Emergence_Structural_Completion/`] §4.1 lists U5 as one of five upstream CANDIDATE structural commitments and §4.2 flags U5 as "the cleanest" among the four remaining items.
**High-leverage status:** U5 is the structural backbone of QM-emergence Step 5 (Heisenberg uncertainty). A theorem-grade U5 derivation would close the substantive primitive-level account of Heisenberg's bound, removing one of the four remaining upstream commitments from the QM-emergence inventory.

---

## 1. The U5 Question

### 1.1 Precise statement

The Heisenberg uncertainty derivation in Phase-1 Step 5 hinges on a specific orthogonal decomposition of Primitive 04's adjacency band:

$$
b^\mathrm{adj}(x, t) = b_x(x, t) + b_p(p, t) \qquad (\text{U5})
$$

where:
- $b^\mathrm{adj}$ is the adjacency-band component of the four-band decomposition (Primitive 04 §1.5);
- $b_x$ is the position-adjacency bandwidth (encoded in the spatial density distribution $|\Psi(x)|^2$);
- $b_p$ is the momentum-adjacency bandwidth (encoded in the momentum density distribution $|\widetilde{\psi}(p)|^2$);
- the two components are **Fourier-conjugate**: concentrating bandwidth in $b_x$ (sharp position) is dual to spreading it in $b_p$ (broad momentum), and vice versa.

Combined with U2's inner-product structure (now FORCED) and the standard Fourier-uncertainty theorem on $L^2$ functions, this partition produces

$$
\Delta x \cdot \Delta p \geq \frac{\hbar}{2}
$$

— the Heisenberg uncertainty inequality.

### 1.2 What U5 commits to, in the same formal style as U1–U4 / U2

U5 is the structural commitment that the adjacency-band bandwidth is *exhausted* by an orthogonal Fourier-conjugate decomposition into exactly two components — position-adjacency and momentum-adjacency — with no residual independent component, with the two components Fourier-dual under the participation-measure inner product, and with the orthogonality of the partition inherited from the U2 sesquilinear inner product applied to the band-restricted projections.

In the formal style of the QM-emergence Step-1 framework's upstream-commitment list:

> **U5 (Adjacency-Band Fourier-Conjugate Partition).** The adjacency-band component of the participation-measure four-band decomposition admits a unique orthogonal decomposition $b^\mathrm{adj} = b_x + b_p$ into two Fourier-conjugate components, exhaustively partitioning the band with no residual third component. Affects: Step 5 (Heisenberg uncertainty).

### 1.3 Role in the participation-measure → Hilbert-space → QM-emergence chain

The participation measure $P_K(x, t) = \sqrt{b_K(x, t)} \cdot e^{i \pi(K, x, t)}$ supplies, via Primitive 04's four-band decomposition, four orthogonal sub-objects: $P_K^\mathrm{int}, P_K^\mathrm{adj}, P_K^\mathrm{env}, P_K^\mathrm{com}$. The four-band orthogonality (Primitive 04 §1.5) is at the band level; what U5 asserts is a finer-grained structural decomposition *within* the adjacency band.

Step 5's derivation of Heisenberg requires this finer decomposition because the Fourier-uncertainty theorem ($\Delta x \cdot \Delta p \geq \hbar/2$) is a statement about Fourier pairs in $L^2$ — it cannot apply to "the adjacency band as a whole." The band must split into a Fourier-conjugate pair for the theorem to bite.

The chain in which U5 sits:

```
Primitives 04 + 06 + 09  →  participation measure (U1)
                         →  four-band decomposition  (Primitive 04 §1.5)
                         →  inner product on participation manifold  (U2, FORCED)
                         →  adjacency-band split  (U5, this arc)
                         →  Fourier-uncertainty applied to L² Ψ  (Step 5, with U5 + U2)
                         →  Heisenberg Δx · Δp ≥ ℏ/2
```

U5 is the single remaining structural item gating Step 5's full unconditional FORCED status. With U5 promoted, Heisenberg becomes structurally complete in both the discrete and continuum regimes (the latter inheriting U2-continuum's gauge-invariant promotion).

---

## 2. Decomposition into Sub-Features

U5 packages five structurally distinct sub-claims, each requiring its own structural status determination.

### 2.1 The five sub-features

- **(F1) Existence of decomposition.** $b^\mathrm{adj}$ splits into orthogonal sub-bands at all (i.e., the adjacency band is not structurally indivisible).
- **(F2) Two-component count.** The decomposition has exactly two components — not one, not three or more.
- **(F3) Fourier conjugacy.** The two components are Fourier-dual (in the sense that the natural transform between $b_x$ and $b_p$ is the Fourier transform on $L^2(\mathbb{R}^d)$).
- **(F4) Orthogonality under U2.** $b_x$ and $b_p$ are orthogonal in the inner product established by the U2-Discrete and U2-Continuum theorems.
- **(F5) Exhaustion / no residual.** The partition is complete: $b^\mathrm{adj} = b_x + b_p$ exactly, with no residual third (or higher) component.

### 2.2 Anticipated structural status

Based on the structural inputs available (§3 below) and the existing tightening-program attempt at U5 [`u5_adjacency_partition_derivation.md`]:

| Sub-feature | Anticipated status | Source of structure |
|---|---|---|
| **F1** Existence of decomposition | FORCED-VIA-DERIVATION | Primitive 06 (ED gradient supplies spatial axis) + Primitive 09 (polarity phase supplies phase-propagation axis); two structurally distinct nearness notions exist within "adjacency" |
| **F2** Two-component count | FORCED-VIA-DERIVATION | Spatial-vs-phase-propagation is the only primitive-level distinction within adjacency; no third primitive-level adjacency-axis exists |
| **F3** Fourier conjugacy | LOAD-BEARING | The transformation between position-density and momentum-density is the Fourier transform if and only if $b_x \propto |\Psi|^2$ and $b_p \propto |\widetilde{\psi}|^2$ for the same $\Psi$; this requires structural identification of the spatial component with $|\Psi|^2$ and the phase-propagation component with $|\widetilde{\psi}|^2$ |
| **F4** Orthogonality under U2 | FORCED-VIA-DERIVATION | Inherits from U2's sesquilinear inner-product structure (now FORCED); Fourier transform is an isometry on $L^2$, preserving orthogonality |
| **F5** Exhaustion / no residual | LOAD-BEARING | Requires showing that no primitive-level structural axis other than spatial-vs-phase-propagation exists within the adjacency band |

The arc's verdict will hinge on F3 and F5: whether Fourier conjugacy is uniquely forced (rather than one possible partition among many), and whether the two-component partition exhausts the adjacency band's primitive-level structure.

### 2.3 Regime split

The discrete-vs-continuum split applies to U5 in a structurally narrower way than it did to U2:

- **Discrete regime.** Adjacency on the participation graph is encoded in edges between vertices. The "spatial-vs-phase-propagation" distinction can be defined at the discrete graph level (vertex-coordinate vs. wavenumber-on-discrete-lattice), with the discrete Fourier transform supplying the conjugacy.
- **Continuum regime.** Spatial coordinates are smooth points on $M$; momenta are smooth covectors. The standard continuous Fourier transform on $L^2(\mathbb{R}^d)$ supplies the conjugacy.

Both regimes are anticipated to admit U5-FORCED status, with the discrete regime closing first (analogously to the U2 program). The continuum-lift gauge from U2-continuum does *not* affect U5 directly because the adjacency-band partition is defined at a fixed locus in the inner-product structure; the conformal gauge rescales bandwidth densities but preserves the two-component decomposition (both $b_x$ and $b_p$ rescale by the same $\Omega^{-D}$ factor, so the ratio and orthogonality are preserved).

---

## 3. Structural Inputs

### 3.1 Primitives drawn upon

- **Primitive 04 (Bandwidth):** supplies the adjacency band $b^\mathrm{adj}$ as one of the four orthogonal bands. The four-band orthogonality at the band level is a primitive-level commitment; what U5 derives is a finer decomposition *within* the adjacency band.
- **Primitive 06 (ED Gradient):** supplies the spatial-structure axis. The gradient $\nabla \rho$ establishes a spatial direction and scale, making "nearness in $x$" well-defined.
- **Primitive 09 (Tension Polarity):** supplies the phase-structure axis. The polarity phase $\pi(K, x)$ is $U(1)$-valued, and its gradient $\nabla \pi$ establishes a phase-propagation direction, making "nearness in phase-propagation" (equivalently, in wavenumber $k = \nabla \pi$) well-defined.
- **Primitive 04 §1.5 four-band orthogonality** (used as a structural input rather than derived here): the four bands do not mix, supplying the kinematic context for U5's finer partition.

### 3.2 Participation-measure structure (U1)

The participation measure $P_K(x, t) = \sqrt{b_K(x, t)} \cdot e^{i \pi_K(x, t)}$ supplies the complex-valued field on which the partition operates. The aggregated wavefunction $\Psi(x, t) = \sum_K P_K(x, t)$ has both a position representation and (via Fourier transform) a momentum representation. U5's identification of $b_x \propto |\Psi(x)|^2$ and $b_p \propto |\widetilde{\psi}(p)|^2$ is the structural bridge between adjacency bandwidth and the wavefunction's position/momentum content.

### 3.3 U2 dependency (now FORCED)

The U2-Discrete Theorem [`papers/U2_Inner_Product/`] establishes the sesquilinear inner product on the participation-measure space. U5 inherits two structural features from U2:

- **Orthogonality has a well-defined meaning.** $b_x \perp b_p$ requires an inner product to be checked; U2 supplies it.
- **The Fourier transform is an isometry.** The discrete Fourier transform on the participation graph (and its continuum analog) preserves the U2 inner product, which is the structural basis for $b_x$ and $b_p$ being Fourier-conjugate orthogonal components.

The U2-Continuum Theorem's gauge structure does *not* propagate into U5 directly: the conformal rescaling $b_K \to \Omega^{-D} b_K$ rescales all bandwidth densities uniformly, including both $b_x$ and $b_p$. The decomposition $b^\mathrm{adj} = b_x + b_p$ is preserved, with both terms rescaling by the same factor.

### 3.4 Born / Bell / Heisenberg dependency

Born (Theorem 10) is now FORCED-unconditional and is therefore *available as a structural input* rather than something U5 must derive. Specifically:

- **Born is needed for the bandwidth-density identification.** The identification $b_x(x) \propto |\Psi(x)|^2$ uses the Born-rule structure applied to position measurements; the analogous $b_p(p) \propto |\widetilde{\psi}(p)|^2$ uses Born for momentum measurements. With Born now forced, these identifications are not new structural commitments — they are consequences of Theorem 10 applied per band.

Bell/Tsirelson and Heisenberg are *downstream* of U5 (Heisenberg directly; Bell indirectly via the shared inner-product structure). U5's derivation does not depend on them.

### 3.5 Continuum-lift / gauge implications

As noted in §2.3 and §3.3, the U2-continuum conformal gauge $(b_K, d\mu) \to (\Omega^{-D} b_K, \Omega^D d\mu)$ does not affect U5's partition structure. Both $b_x$ and $b_p$ rescale by the same factor; their ratio (which determines the partition) and their orthogonality (which is gauge-invariant under U2-continuum) are preserved. U5 is therefore *gauge-compatible* with the U2-continuum result.

---

## 4. Falsifiers

The arc is **closed FORCED** if all five sub-features (F1–F5 of §2.1) close uniquely under the available structural inputs.

The arc is **closed CONDITIONAL** if F1, F2, F4 close uniquely but F3 (Fourier conjugacy) or F5 (exhaustion) admits a non-pathological alternative consistent with the primitive structure.

The arc is **closed NOT FORCED** if any sub-feature admits a *physically distinct* alternative — meaning a different adjacency-band partition that satisfies the primitives and produces a different downstream phenomenology than standard QM (specifically, a different uncertainty inequality than $\Delta x \cdot \Delta p \geq \hbar/2$).

### 4.1 Specific sub-falsifiers to watch for

- **(Fal-1) No decomposition exists.** If the adjacency band is structurally indivisible at the primitive level — i.e., if neither Primitive 06 nor Primitive 09 supplies a nearness-axis applicable to adjacency — then F1 fails and U5 collapses entirely.
- **(Fal-2) More than two components.** If the primitive stack supplies a *third* adjacency-axis distinct from spatial and phase-propagation (e.g., from an as-yet-unidentified primitive-level structural feature), then F5's exhaustion claim fails and the partition is incomplete. The corresponding uncertainty inequality would be a multi-variable Heisenberg-like statement involving the third axis.
- **(Fal-3) Non-Fourier conjugacy.** If the natural transformation between $b_x$ and $b_p$ is not the Fourier transform but some other unitary or non-unitary transform, then F3 fails. The transformation could in principle be a non-Fourier integral transform (Wavelet, Mellin, fractional-Fourier) admissible on $L^2$ but not standard Fourier; the resulting uncertainty inequality would have a different prefactor than $\hbar/2$.
- **(Fal-4) Non-orthogonal partition.** If $b_x$ and $b_p$ are not orthogonal under the U2 inner product, then F4 fails and the partition is not a clean spectral decomposition. The uncertainty inequality would acquire correction terms proportional to the cross-overlap.
- **(Fal-5) Gauge propagation.** If the U2-continuum conformal gauge $(b_K, d\mu) \to (\Omega^{-D} b_K, \Omega^D d\mu)$ rescales $b_x$ and $b_p$ asymmetrically (different powers of $\Omega$ for each), then U5's partition would acquire gauge dependence, propagating the U2-continuum gauge into Heisenberg's bound. This is anticipated *not* to obtain (both components rescale uniformly) but warrants explicit verification.

### 4.2 Discrete-regime versus continuum-regime falsifiers

- **Discrete regime.** Falsifiers Fal-1 through Fal-4 attach. Fal-5 is irrelevant (no continuum gauge in the discrete regime).
- **Continuum regime.** All five falsifiers attach. Fal-5 specifically requires the explicit verification that the conformal rescaling acts uniformly on both components.

Both regimes are addressed in the arc's memo plan (§5).

---

## 5. Memo Plan

### Memo 01: `01_decomposition_and_mapping.md`

Decompose U5 into sub-features F1–F5. For each, identify which primitive(s) and which prior FORCED items (U2-Discrete, U2-Continuum, Born/Theorem 10) supply the structural inputs. Classify each as automatic / forced-via-derivation / load-bearing. Inventory parallels the U2 Memo 01 and born_gleason Memo 01 templates.

**Anticipated structure:**
- §1: U5 statement and role
- §2: Five sub-features (F1–F5) with primitive mapping
- §3: Status classification table
- §4: Comparison to U2 Memo 01 structural shape
- §5: Pre-Memo-02 audit recommendations

### Memo 02: `02_F1_F2_F4_derivation.md`

Derive the three sub-features anticipated to close cleanly: F1 (existence of decomposition) via Primitives 06 + 09 supplying two distinct adjacency-axes; F2 (two-component count) via the absence of a primitive-level third axis; F4 (orthogonality under U2) via direct application of the U2 inner-product structure plus the isometry property of the Fourier transform.

**Anticipated structure:**
- §1: F1 derivation (existence of decomposition)
- §2: F2 derivation (two-component count)
- §3: F4 derivation (orthogonality)
- §4: Joint status; load-bearing items deferred to Memo 03

### Memo 03: `03_F3_F5_and_verdict.md`

The load-bearing memo. Examines F3 (Fourier conjugacy) and F5 (exhaustion / no residual) against falsifiers Fal-3, Fal-2, Fal-5. Anticipated leading argument: the spatial axis (Primitive 06) and the phase-propagation axis (Primitive 09) are conjugate via the standard $L^2$ Fourier transform because the participation-measure construction $P_K(x) = \sqrt{b_K} e^{i\pi_K}$ places the bandwidth magnitude in the $x$-representation and the phase-propagation rate $\nabla \pi = k$ in the Fourier-dual $p$-representation; the two are Fourier pairs by construction. Exhaustion follows from the absence of any primitive-level adjacency-axis distinct from these two.

**Anticipated structure:**
- §1: F3 derivation (Fourier conjugacy)
- §2: F5 derivation (exhaustion / no residual)
- §3: Falsifier audit (Fal-2, Fal-3, Fal-4, Fal-5)
- §4: Continuum-regime gauge-propagation check
- §5: Verdict
- §6: Downstream cascade (Heisenberg promotion)

### Memo 04: `04_closure_and_summary.md` *(optional but recommended)*

Closure memo with canonical narrative summary, integration into the QM-emergence program, and a public-facing explainer section. Parallels the U2-discrete Memo 05 and U2-continuum Memo 04 templates.

**Anticipated structure:**
- §1: Arc summary
- §2: U5 theorem statement and proof sketch
- §3: Heisenberg promotion (downstream cascade)
- §4: Position in the QM-emergence program
- §5: Public-facing explainer
- §6: Section-to-memo mapping appendix

---

## 6. Comparison to U2's Shape

### 6.1 Methodological similarities

| Methodological element | U2 arc | U5 arc (anticipated) |
|---|---|---|
| Decomposition into sub-features | 3 sub-commitments (C3a, C3b, C3c) | 5 sub-features (F1–F5) |
| Automatic items | 1 (C3a linearity) | 0 |
| Forced-via-derivation items | 1 (C3b sesquilinearity) | 3 (F1 existence, F2 two-component, F4 orthogonality) |
| Load-bearing items | 1 (C3c specific form, with 3 sub-features) | 2 (F3 Fourier conjugacy, F5 exhaustion) |
| Methodological pattern | Decompose → identify load-bearing → close via primitive-level arguments | Same |
| New CANDIDATEs introduced | 0 | Anticipated: 0 |

The U5 arc inherits the same structural-derivation methodology as U2 and is expected to produce a theorem-grade result by the same pattern.

### 6.2 Structural differences

**U5 is narrower in scope.** U2 derived an entire algebraic structure (linearity + sesquilinearity + specific aggregation form) on the participation-measure space. U5 derives a specific orthogonal decomposition of one band of the four-band structure. The scope is one-band-finer than U2.

**U5 has more structural inputs available.** U2 derived its result using only Primitives 04 + 09 + four-band orthogonality. U5 has access to all of U2's inputs plus the now-FORCED U2 inner product itself plus the now-FORCED Born rule (via Theorem 10). The available structural infrastructure is richer.

**U5 has fewer load-bearing items.** U2's load was concentrated on three sub-features of C3c (channel measure, position measure, local pairing). U5's load is concentrated on F3 (Fourier conjugacy) and F5 (exhaustion). Two load-bearing items vs. three; smaller substantive surface.

**U5's continuum lift is structurally simpler.** U2's continuum lift introduced an explicit conformal gauge structure that required dedicated treatment. U5's continuum lift is anticipated to be gauge-compatible with U2-continuum (both partition components rescale uniformly), introducing no new gauge structure.

### 6.3 Whether U5 is cleaner or more delicate

**Anticipated: cleaner.** Synthesis paper §4.2 explicitly classifies U5 as "the cleanest" among the four remaining upstream items. The structural-symmetry argument for the Fourier-conjugate partition is plausibly derivable from Primitives 06 + 09 supplying the two distinct adjacency-axes plus U2 supplying the inner product on which the Fourier transform is an isometry.

**Risk locations.** The principal structural risk is F5 (exhaustion). Showing that no third adjacency-axis exists at the primitive level requires an exhaustive primitive-level survey rather than a positive construction; this is a different kind of argument than the constructive arguments closing F1, F2, F3, F4. The argument shape here is "no primitive-level source for X" — analogous to U2 Memo 03's arguments forbidding non-trivial channel weighting and non-trivial vertex weighting. The methodological pattern is established but the argument's correctness depends on the primitive-level audit being genuinely exhaustive.

A secondary risk is F3 (Fourier conjugacy specificity). If the natural transform between $b_x$ and $b_p$ admits non-standard generalisations (e.g., fractional-Fourier on certain manifolds), the standard Heisenberg bound might be replaced by a generalised version with a different prefactor. This is anticipated *not* to obtain on flat-spacetime baseline (where standard Fourier is the unique unitary intertwiner of position and momentum), but warrants explicit verification.

### 6.4 Overall assessment

U5 is anticipated to close FORCED with a structurally cleaner derivation than U2. The arc is expected to be 3 memos plus an optional closure memo (4 total), shorter than U2's 5+5 = 10-memo program (U2-discrete + U2-continuum). The downstream cascade is narrower — Heisenberg promotes to fully unconditional, but Born and Bell/Tsirelson are unaffected (already promoted by U2).

---

## 7. Recommended Next Steps

**(a) Begin Memo 01 (decomposition + primitive mapping).** Natural next session step. Following the template of U2 Memo 01 and born_gleason Memo 01, Memo 01 should produce a tight inventory of the five sub-features with explicit primitive correspondents and status classifications. Expected outcome: a structural map ready for Memos 02 and 03 to target specific load-bearing items.

**(b) Pre-Memo-01 audit of the existing tightening-program memo.** The 2026-04-24 `u5_adjacency_partition_derivation.md` memo claimed FORCED status under the earlier tightening-program methodology but predates the structural-derivation methodology established in born_gleason + U2. A 15-minute audit before drafting Memo 01 will identify which structural arguments transfer cleanly to the new methodology and which need to be re-derived under the sharper standard. Specifically: the existing memo's derivations of the spatial-vs-phase-propagation distinction (F1) and the orthogonality argument (F4) likely transfer; the exhaustion argument (F5) and the Fourier-conjugacy specificity (F3) may need to be redone under the more rigorous standard.

**(c) Single memory-record update only after Memo 03 closure.** Following the discipline established in the U2 program, avoid memory churn during the arc. The bundled update to `project_qm_emergence_arc.md` should capture the post-arc state covering: (i) U5 theorem, (ii) Heisenberg's full unconditional promotion, (iii) updated upstream-commitment count from {U1, U3, U4, U5} + gauge to {U1, U3, U4} + gauge, (iv) Primitive-09 sensitivity (already flagged in U2 program — same dependency applies here). The MEMORY.md index line update should be similarly bundled.

---

## 8. Cross-references

- Companion arcs (predecessors): [`arcs/born_gleason/`](../born_gleason/), [`arcs/U2/`](../U2/), [`arcs/U2_continuum/`](../U2_continuum/)
- Existing tightening-program attempt at U5: [`arcs/arc-foundations/u5_adjacency_partition_derivation.md`](../arc-foundations/u5_adjacency_partition_derivation.md) (2026-04-24)
- QM-emergence synthesis (upstream-commitment inventory; U5 listed in §4.1): [`papers/QM_Emergence_Structural_Completion/QM_Emergence_Structural_Completion.md`](../../papers/QM_Emergence_Structural_Completion/QM_Emergence_Structural_Completion.md)
- Step 5 derivation (Heisenberg, downstream beneficiary): [`arcs/arc-foundations/uncertainty_from_participation.md`](../arc-foundations/uncertainty_from_participation.md)
- U2-Inner-Product paper (inner-product structure inherited as input): [`papers/U2_Inner_Product/paper_u2_inner_product.md`](../../papers/U2_Inner_Product/paper_u2_inner_product.md)
- Born_Gleason paper (Born structure inherited as input for $b_x \propto |\Psi|^2$, $b_p \propto |\widetilde{\psi}|^2$ identifications): [`papers/Born_Gleason/born_gleason_paper.md`](../../papers/Born_Gleason/born_gleason_paper.md)
- Primitive 04 (bandwidth + four-band decomposition + adjacency band): `quantum/primitives/04_participation_bandwidth.md`
- Primitive 06 (ED gradient, supplies spatial axis): `quantum/primitives/06_ed_gradient.md`
- Primitive 09 (tension polarity, $U(1)$ phase, supplies phase-propagation axis): `quantum/primitives/09_tension_polarity.md`
- Project memory: `memory/project_qm_emergence_arc.md`

---

## 9. One-line arc summary

> **Test whether U5 — the adjacency-band Fourier-conjugate partition $b^\mathrm{adj} = b_x + b_p$ — is FORCED by Primitives 04 + 06 + 09 + the now-FORCED U2 inner product + the now-FORCED Born structure. Five sub-features: F1 existence of decomposition, F2 two-component count, F3 Fourier conjugacy (load-bearing), F4 orthogonality under U2, F5 exhaustion / no residual (load-bearing). Anticipated cleaner than U2 due to richer available structural inputs; principal risk locations are F3 (Fourier conjugacy specificity) and F5 (exhaustion via primitive-level audit). If FORCED, Heisenberg promotes to fully unconditional, removing the structural backbone of Step 5's conditionality. Three-memo plan plus optional closure memo. The U2-continuum gauge is anticipated to act uniformly on both partition components, preserving the partition under conformal rescaling.**
