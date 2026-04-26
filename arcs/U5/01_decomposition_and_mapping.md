# Memo 01 — U5 Decomposition and Primitive / Theorem Mapping

**Date:** 2026-04-26
**Arc:** `arcs/U5/`
**Predecessor:** [`00_arc_outline.md`](00_arc_outline.md)
**Status:** Structural inventory memo. Decomposes the upstream commitment U5 (adjacency-band Fourier-conjugate partition) into five sub-features, maps each to the relevant ED primitives, the participation-measure construction, the now-FORCED U2 inner product (discrete and continuum), and the now-FORCED Born/Theorem 10 result, and classifies each by structural status (automatic / forced-via-derivation / load-bearing). Analogous in scope to U2 Memo 01 and born_gleason Memo 01.
**Purpose:** Pin down the conceptual terrain so Memo 02 can derive F1, F2, F4 directly and Memo 03 can focus on the load-bearing F3 (Fourier conjugacy) and F5 (exhaustion) questions.

---

## 1. The U5 Question, Stated Precisely

### 1.1 Formal statement, in the style of U1–U4 / U2

The Heisenberg uncertainty derivation in Phase-1 Step 5 hinges on a specific orthogonal decomposition of the adjacency band of Primitive 04's four-band structure:

$$
b^\mathrm{adj}(x, t) = b_x(x, t) + b_p(p, t) \qquad \text{(U5)}
$$

with the two components Fourier-conjugate, exhausting the adjacency band. In the formal style of the QM-emergence Step-1 framework's upstream-commitment list:

> **U5 (Adjacency-Band Fourier-Conjugate Partition).** The adjacency-band component $b^\mathrm{adj}$ of the participation-measure four-band decomposition admits a unique orthogonal decomposition $b^\mathrm{adj} = b_x + b_p$ into two Fourier-conjugate components, exhaustively partitioning the band with no residual third component. The two components are related by the Fourier transform under the U2 inner product, with $b_x \propto |\Psi(x)|^2$ and $b_p \propto |\widetilde{\psi}(p)|^2$ via the per-band Born-rule structure of Theorem 10. Affects: Step 5 (Heisenberg uncertainty $\Delta x \cdot \Delta p \geq \hbar/2$).

### 1.2 Structural commitment U5 represents

U5 is the structural commitment that the adjacency band is *exhausted* by an orthogonal Fourier-conjugate decomposition into exactly two components — position-adjacency and momentum-adjacency — with:

- **No primitive-level adjacency-axis distinct from spatial and phase-propagation.** The two components together account for all adjacency content of any chain at any locus.
- **Fourier conjugacy as the unique inter-component transformation.** The transformation between $b_x$ and $b_p$ is the standard $L^2$ Fourier transform, not some other unitary or non-unitary integral transform.
- **Orthogonality under U2.** The two components are orthogonal projections in the participation-measure inner product established by the U2 theorems.
- **Identification via Born structure.** $b_x \propto |\Psi(x)|^2$ and $b_p \propto |\widetilde{\psi}(p)|^2$ are theorem-grade identifications inherited from Theorem 10 applied per-band, not new structural commitments.

### 1.3 Role in the participation-measure → Hilbert-space → QM-emergence chain

The chain of upstream commitments leading to Heisenberg's bound is:

$$
\text{Primitives 04 + 06 + 09} \xrightarrow{\text{U1}} \text{participation measure} \xrightarrow{\text{P-04 §1.5}} \text{four-band decomposition}
$$

$$
\xrightarrow{\text{U2 (FORCED)}} \text{inner product} \xrightarrow{\text{U5 (this arc)}} \text{adjacency band split}
$$

$$
\xrightarrow{\text{Theorem 10 + Fourier-uncertainty}} \Delta x \cdot \Delta p \geq \hbar/2 \qquad \text{(Step 5 Heisenberg)}
$$

U5 is the single structural item gating Step 5's full unconditional FORCED status. The four-band orthogonality of Primitive 04 §1.5 supplies orthogonality *between* bands; U5 supplies the finer structural decomposition *within* the adjacency band that is needed for the Fourier-uncertainty theorem to apply.

---

## 2. Decomposition into Sub-Features

U5 packages five structurally distinct sub-claims. Each must be settled independently for the U5-FORCED verdict to close.

### 2.1 The five sub-features

- **(F1) Existence of decomposition.** $b^\mathrm{adj}$ admits any orthogonal sub-band decomposition at all, i.e., it is not structurally indivisible at the primitive level.
- **(F2) Two-component count.** The decomposition has exactly two components — not one (no decomposition), not three or more (residual axes).
- **(F3) Fourier conjugacy.** The two components are Fourier-dual under the standard $L^2$ Fourier transform, not under some other unitary or non-unitary transform.
- **(F4) Orthogonality under U2.** $b_x$ and $b_p$ are orthogonal in the inner product established by the U2-Discrete and U2-Continuum theorems.
- **(F5) Exhaustion / no residual.** The partition is complete: $b^\mathrm{adj} = b_x + b_p$ exactly, with no residual third (or higher) primitive-level adjacency-axis.

### 2.2 Anticipated structural status per sub-feature

| Sub-feature | Anticipated status | Reasoning |
|---|---|---|
| **F1** Existence of decomposition | **forced-via-derivation** | Primitive 06 supplies the spatial axis, Primitive 09 supplies the phase-propagation axis; two structurally distinct nearness notions exist within "adjacency" |
| **F2** Two-component count | **forced-via-derivation** | The spatial-vs-phase-propagation distinction is the only primitive-level axis-pair within adjacency; conditional on F5 being settled, two is the count |
| **F3** Fourier conjugacy | **load-bearing** | Requires translation symmetry + Stone's theorem identifying the unique unitary intertwiner of position and momentum; uniqueness against fractional-Fourier and other generalisations needs explicit argument |
| **F4** Orthogonality under U2 | **forced-via-derivation** | Inherits directly from U2 (inner product) + the isometry of the Fourier transform on $L^2$; Parseval gives $\int |\Psi|^2 dx = \int |\widetilde\psi|^2 dp$ as the orthogonal-decomposition identity |
| **F5** Exhaustion / no residual | **load-bearing** | Negative-existence claim: requires a primitive-level audit verifying that no third adjacency-axis distinct from spatial and phase-propagation exists in the primitive stack |

The arc's verdict will hinge on F3 and F5 — the same load-bearing pattern as U2 Memo 01 (where the substantive work concentrated on the C3c sub-features).

### 2.3 Discrete vs continuum regime split

The discrete-vs-continuum split applies to U5 in a structurally narrower way than to U2:

- **Discrete regime** (participation graph $G = (V, E)$). Adjacency on the graph is encoded in edges between vertices. The spatial axis is the vertex coordinate; the phase-propagation axis is the wavenumber on the discrete reciprocal lattice. The Fourier conjugacy is the discrete Fourier transform on the vertex set, an isometry under the U2-Discrete inner product. Falsifiers Fal-1 through Fal-4 attach.

- **Continuum regime** (emergent manifold $M$ from Primitive 12 thickening). The spatial axis is the smooth coordinate on $M$; the phase-propagation axis is the dual cotangent fibre. The Fourier conjugacy is the standard continuous Fourier transform on $L^2(\mathbb{R}^d)$, an isometry under the U2-Continuum inner product. Falsifiers Fal-1 through Fal-5 attach (Fal-5 being the gauge-propagation check).

Both regimes are anticipated to admit U5-FORCED status, with the discrete regime closing first (analogously to the U2 program). The arc will treat both within the same memos rather than splitting into separate arcs, because the lift-introduced complications are smaller for U5 than for U2 (no new gauge structure expected).

### 2.4 Gauge interaction with U2-continuum

The U2-Continuum theorem established a one-parameter conformal gauge

$$
(b_K(x), d\mu(x)) \to (\Omega^{-D}(x) \cdot b_K(x), \Omega^D(x) \cdot d\mu(x))
$$

under which all inner-product values are invariant. For U5 to be gauge-compatible with U2-continuum, the partition $b^\mathrm{adj} = b_x + b_p$ must be preserved under the conformal rescaling — both components must rescale by the same $\Omega^{-D}$ factor.

**Anticipated outcome.** The conformal rescaling acts on the bandwidth field $b_K(x)$ as a whole; the four-band decomposition (Primitive 04 §1.5) and the within-band partition (U5) are both inherited as decompositions of the rescaled field. Both $b_x$ and $b_p$ rescale by $\Omega^{-D}$ uniformly. The partition is gauge-compatible, with explicit verification deferred to Memo 03 §4 (continuum-regime gauge-propagation check).

---

## 3. Mapping Each Sub-Feature to Structural Inputs

### 3.1 F1 — Existence of decomposition

**ED primitives:**
- **Primitive 06 (ED Gradient):** the gradient $\nabla \rho$ establishes a spatial direction and scale on the participation graph (in the discrete regime) or the emergent manifold (in the continuum regime). Provides the spatial-nearness axis.
- **Primitive 09 (Tension Polarity):** polarity $\pi(K, x)$ is $U(1)$-valued; its gradient $\nabla \pi(K, x) = k_K$ is the phase-propagation rate (wavenumber). Provides the phase-propagation-nearness axis.

**Participation-measure structure:** the construction $P_K(x) = \sqrt{b_K(x)} \cdot e^{i \pi_K(x)}$ places the bandwidth magnitude in the position representation and the phase-propagation rate as the gradient of the phase factor. Both axes are simultaneously present in the participation measure.

**U2 dependency:** none direct. F1 is about the existence of two structurally distinct nearness axes; this is a primitive-level fact independent of the inner-product structure.

**Born/Theorem 10 dependency:** none.

**Continuum-lift implications:** none direct; both axes exist in both regimes.

### 3.2 F2 — Two-component count

**ED primitives:**
- **Primitive 06 + Primitive 09 jointly:** supply the two distinct nearness axes (spatial and phase-propagation). The two-component count is the count of primitive-level adjacency axes that exist.
- **Primitive 04 §1.5 (four-band orthogonality):** establishes that adjacency is one band of the four-band structure, independent of internal-rule, environmental, and commitment-reserve. This isolates the question to within the adjacency band.

**Participation-measure structure:** the construction $P_K = \sqrt{b_K} e^{i \pi_K}$ encodes magnitude (spatial-related) and phase (phase-propagation-related) — exactly two structural roles.

**Conditional dependency:** F2 is conditional on F5 (exhaustion). If F5 fails (a third axis exists), F2 fails simultaneously. If F5 closes, F2 closes by direct enumeration of the primitive-level axes.

**Continuum-lift implications:** none direct.

### 3.3 F3 — Fourier conjugacy

**ED primitives:**
- **Primitive 06 (translation symmetry):** at the primitive level, the participation graph (or emergent manifold) supports translations as a symmetry of the adjacency relation. Translation invariance is a kinematic property of the underlying graph structure, not a dynamical property requiring time-evolution.
- **Primitive 09 ($U(1)$-valued phase):** the phase factor $e^{i \pi_K(x)}$ has the form of a complex exponential; its Fourier conjugate (in $x$) is a delta function in the wavenumber $k$.

**Participation-measure structure:** the construction $P_K(x) = \sqrt{b_K(x)} e^{i \pi_K(x)}$ has explicit complex-exponential phase structure. Plane-wave-like configurations $P_K(x) = \sqrt{b_K} \cdot e^{i k x}$ are the natural primitive-level building blocks — they have well-defined wavenumber $k = \nabla \pi$.

**U2 dependency (significant):** the Fourier transform is an isometry on $L^2(\mathbb{R}^d)$ *only because* the underlying inner product is the standard $L^2$ inner product established by U2. Without U2, the term "Fourier-conjugate" would need a separate definition. With U2 (now FORCED), Fourier conjugacy means: $\Psi(x)$ and $\widetilde\psi(p)$ are related by a unitary transformation in the U2-inner-product sense.

**Stone's theorem (mathematical, not primitive):** the one-parameter unitary group of translations $T_a : x \to x + a$ has a self-adjoint generator $\hat{p}$ such that $T_a = e^{i \hat{p} a / \hbar}$. The eigenfunctions of $\hat{p}$ are plane waves $\langle x | p \rangle = (2\pi\hbar)^{-1/2} e^{ipx/\hbar}$, and the basis-change $\Psi(x) \to \widetilde\psi(p)$ is the standard Fourier transform. Stone's theorem requires (i) a Hilbert space (supplied by U2) and (ii) a one-parameter unitary group of translations (supplied by Primitive 06 translation symmetry).

**Note on U3 dependency.** An earlier tightening-program derivation [`arcs/arc-foundations/u5_adjacency_partition_derivation.md`] invoked U3 (the participation-measure evolution equation) as a premise for the Fourier conjugacy argument. The present arc replaces this dependency: translation invariance is a *kinematic* property of the participation graph (Primitive 06 + Primitive 03 supply graph homogeneity), not a *dynamical* property requiring U3. F3 is derivable from U2 + translation symmetry + Stone's theorem without invoking U3. This is a sharper structural argument than the earlier tightening-memo version.

**Born/Theorem 10 dependency:** Theorem 10 is needed to identify $b_x \propto |\Psi(x)|^2$ and $b_p \propto |\widetilde\psi(p)|^2$ — the per-band Born-rule structure. Without Theorem 10, the bandwidth-distribution interpretation of $|\Psi|^2$ and $|\widetilde\psi|^2$ would itself be conditional. With Theorem 10 (FORCED-unconditional), the identifications are theorem-grade inputs to the Fourier-conjugacy argument.

**Continuum-lift implications:** the Fourier transform on $L^2(\mathbb{R}^d)$ generalises directly from the discrete Fourier transform on the vertex set in the strict $\tau \to \infty$ limit (per U2-Continuum's lift mechanism). The conjugacy is preserved.

### 3.4 F4 — Orthogonality under U2

**ED primitives:**
- **Primitive 04 §1.5 (four-band orthogonality):** ensures the adjacency band is independently normalised from the other three bands. F4's orthogonality claim is *within* the adjacency band; the band-level orthogonality is a separate (inherited) structural input.

**U2 dependency (load-bearing):** orthogonality requires an inner product. U2 supplies it. The orthogonality of $b_x$ and $b_p$ as components of $b^\mathrm{adj}$ is the statement that

$$
\int |\Psi(x)|^2 \, dx = \int |\widetilde\psi(p)|^2 \, dp = N_\mathrm{adj}
$$

— Parseval's theorem, a direct consequence of Fourier transform's unitarity on the U2 inner-product space. With U2 FORCED and Fourier conjugacy F3 in hand, F4 is automatic.

**Born/Theorem 10 dependency:** as for F3, Theorem 10 supplies the bandwidth-density identifications $b_x \propto |\Psi|^2$, $b_p \propto |\widetilde\psi|^2$ that make the Parseval integrals interpretable as bandwidth integrals.

**Continuum-lift implications:** Parseval's theorem holds in both the discrete and continuum regimes. The U2-Continuum gauge rescales $|\Psi|^2$ and $|\widetilde\psi|^2$ by the same $\Omega^{-D}$ factor (since the participation measure $P$ rescales by $\Omega^{-D/2}$, and $|\Psi|^2 = \sum_K |P_K|^2$ rescales as $\Omega^{-D} |\Psi|^2$; the Fourier transform is unitary, so $|\widetilde\psi|^2$ rescales identically). Parseval's identity is gauge-invariant.

### 3.5 F5 — Exhaustion / no residual

**ED primitives:**
- **Primitive 04 §1.5 (four-band orthogonality):** isolates the adjacency band from the other three bands. F5's exhaustion claim is *within* the adjacency band, taking the four-band structure as a given.
- **Primitive 06 (ED gradient) + Primitive 09 ($U(1)$ polarity):** supply the two adjacency axes. F5 asserts these are the *only* primitive-level adjacency axes.

**Participation-measure structure:** the construction $P_K(x) = \sqrt{b_K(x)} e^{i \pi_K(x)}$ has exactly two structural constituents — magnitude $\sqrt{b_K}$ (carries the spatial information via Primitive 06) and phase $e^{i \pi_K}$ (carries the phase-propagation information via Primitive 09). No third constituent exists in the construction; any additional structural feature would have to be an additional primitive.

**U2 dependency:** F5's exhaustion claim within the adjacency band is independent of the inner-product structure. Once F5 is established, U2 supplies the orthogonality (F4) and Fourier conjugacy (F3) of the resulting two-component partition.

**Primitive-stack audit:** F5 is the sub-feature most exposed to a primitive-level audit. Specifically, F5 fails if the primitive stack supplies a *third* adjacency-axis distinct from Primitive 06 (spatial) and Primitive 09 (phase-propagation). Candidate third axes that warrant explicit dismissal:
- **Bandwidth gradient direction.** Distinct from spatial gradient $\nabla \rho$? Within the participation graph, "spatial direction" is defined via $\nabla \rho$; bandwidth gradient is structurally subordinate. Not a distinct axis.
- **Rule-type coupling direction.** Different rule-types live in different primitive sectors (Primitive 07's rule-type-selectivity); within a single rule-type's adjacency band, no rule-type axis exists. Not a distinct axis.
- **Polarity-amplitude direction (different from polarity-phase).** Primitive 09 supplies polarity *phase*; polarity does not have an independent amplitude beyond the bandwidth magnitude. Not a distinct axis.
- **Higher-derivative axes.** Could $\nabla^2 \rho$ or $\nabla^2 \pi$ supply a distinct nearness axis? Higher derivatives are structurally derivative from the first-derivative axes; they do not constitute independent primitive-level adjacency-axes.

The audit anticipates closure: no third axis exists at the current primitive stack. Memo 03 §2 will execute this audit explicitly.

**Continuum-lift implications:** F5's exhaustion claim is regime-independent — the primitive-level audit applies in both discrete and continuum regimes. No new continuum-specific axes emerge under Primitive 12 thickening; thickening accumulates commitments but does not introduce new structural axes.

### 3.6 Summary: structural inputs by sub-feature

| Sub-feature | Primitives | Participation-measure | U2 | Theorem 10 | Continuum-lift |
|---|---|---|---|---|---|
| **F1** existence | 06, 09 | construction | — | — | regime-independent |
| **F2** two-component | 06, 09, 04 §1.5 | construction | — | — | regime-independent |
| **F3** Fourier conjugacy | 06 (translation), 09 (phase) | construction (complex exponential) | required (Hilbert-space + isometry) | required (band-density identification) | preserved under continuum lift |
| **F4** orthogonality | 04 §1.5 | construction | required (inner product) | required (band-density identification) | gauge-invariant under U2-continuum |
| **F5** exhaustion | 04 §1.5, 06, 09; primitive-stack audit | construction | — | — | regime-independent |

---

## 4. Falsifiers Attached to Each Sub-Feature

The arc is **closed FORCED** if all five sub-features close under the available structural inputs.

The arc is **closed CONDITIONAL** if F1, F2, F4 close uniquely but F3 or F5 admit a non-pathological alternative.

The arc is **closed NOT FORCED** if any sub-feature admits a *physically distinct* alternative producing a different downstream phenomenology than standard QM (specifically, a Heisenberg-like inequality with a different prefactor or different conjugate-pair structure).

### 4.1 Specific falsifiers

- **(Fal-1) No decomposition exists.** Attaches to **F1**. If neither Primitive 06 nor Primitive 09 supplies an adjacency-axis applicable at the primitive level — e.g., if "adjacency" is structurally indivisible — F1 fails and U5 collapses.
- **(Fal-2) More than two components.** Attaches to **F5**. If the primitive stack supplies a third adjacency-axis distinct from Primitive 06 and Primitive 09, F5's exhaustion claim fails. The corresponding uncertainty inequality would be a multi-variable Heisenberg-like statement with a third spread variable.
- **(Fal-3) Non-Fourier conjugacy.** Attaches to **F3**. If the natural transformation between $b_x$ and $b_p$ admits non-standard generalisations on the participation-measure space (fractional Fourier, wavelet, Mellin, etc.), F3 fails. The resulting uncertainty inequality would have a different prefactor than $\hbar/2$.
- **(Fal-4) Non-orthogonal partition.** Attaches to **F4**. If $b_x$ and $b_p$ are not orthogonal under the U2 inner product — i.e., if Parseval's identity fails or acquires correction terms — F4 fails. The uncertainty inequality would acquire cross-overlap correction terms.
- **(Fal-5) Gauge propagation.** Attaches to **F4** and **F3** in the continuum regime. If the U2-continuum conformal rescaling $b_K \to \Omega^{-D} b_K$ acts asymmetrically on $b_x$ and $b_p$ — i.e., if the two components rescale by different powers of $\Omega$ — Heisenberg's bound would acquire gauge dependence. This is anticipated *not* to obtain (both rescale by $\Omega^{-D}$ uniformly under the U2-continuum gauge) but warrants explicit verification.

### 4.2 Discrete-regime versus continuum-regime falsifier attachments

| Falsifier | Discrete regime | Continuum regime |
|---|---|---|
| Fal-1 (no decomposition) | attaches | attaches |
| Fal-2 (third axis) | attaches | attaches |
| Fal-3 (non-Fourier conjugacy) | attaches (discrete Fourier transform) | attaches (continuous Fourier transform) |
| Fal-4 (non-orthogonal partition) | attaches | attaches |
| Fal-5 (gauge propagation) | not applicable | attaches |

Both regimes are addressed in the memo plan; Fal-5 receives explicit treatment in Memo 03 §4 (continuum-regime gauge-propagation check).

---

## 5. Memo-Level Status Summary

| Sub-feature | Status | Source of difficulty | Falsifier(s) |
|---|---|---|---|
| **F1** Existence of decomposition | forced-via-derivation | Two distinct primitive-level adjacency-axes (P-06 spatial, P-09 phase-propagation) supply the decomposition; no primitive obstacle | Fal-1 |
| **F2** Two-component count | forced-via-derivation, conditional on F5 | Direct enumeration of primitive-level adjacency-axes once F5 establishes exhaustion | Fal-2 (jointly with F5) |
| **F3** Fourier conjugacy | **load-bearing** | Translation symmetry + Stone's theorem + uniqueness against fractional-Fourier and wavelet generalisations; requires U2 inner product as input | Fal-3 |
| **F4** Orthogonality under U2 | forced-via-derivation | Parseval's theorem (consequence of Fourier unitarity) + the U2 inner product (now FORCED); plus a continuum-regime gauge-invariance check | Fal-4, Fal-5 (continuum) |
| **F5** Exhaustion / no residual | **load-bearing** | Negative-existence claim against a third adjacency-axis; primitive-level audit required | Fal-2 |

**Net.** Three of five sub-features (F1, F2, F4) are anticipated to close cleanly via direct application of primitive-level inputs + U2 + Theorem 10. Two sub-features (F3, F5) are load-bearing and concentrate the substantive work of the arc in Memo 03.

---

## 6. Comparison to U2's Shape

### 6.1 Methodological similarities

| Methodological element | U2 arc | U5 arc (anticipated) |
|---|---|---|
| Decomposition into sub-features | 3 (C3a, C3b, C3c with 3 sub-features) | 5 (F1–F5) |
| Automatic items | 1 (C3a linearity) | 0 |
| Forced-via-derivation items | 1 (C3b sesquilinearity) + 3 (C3c sub-features in discrete) | 3 (F1, F2 conditional, F4) |
| Load-bearing items | 1 (C3c specific form, with 3 sub-features) | 2 (F3 Fourier conjugacy, F5 exhaustion) |
| Methodological pattern | Decompose → identify load-bearing → close via primitive-level arguments | Same |
| New CANDIDATEs introduced | 0 | Anticipated: 0 |
| Inherits prior FORCED items | None at start; both U2-Discrete and U2-Continuum closed in the arc | U2-Discrete + U2-Continuum + Theorem 10 (Born) all available as inputs |

### 6.2 Structural differences

**U5 is narrower in scope.** U2 derived an entire algebraic structure (linearity + sesquilinearity + specific aggregation form) on the participation-measure space. U5 derives a specific orthogonal decomposition of one band of the four-band structure. The scope is one-band-finer than U2.

**U5 has more structural inputs available.** U2 derived its result using only Primitives 04 + 09 + four-band orthogonality. U5 has access to all of U2's inputs plus the now-FORCED U2 inner product itself plus the now-FORCED Born rule (via Theorem 10). The available structural infrastructure is substantially richer.

**U5 has a different class of load-bearing argument.** U2's load was concentrated on positive structural derivations (channel measure, vertex measure, local pairing each derived from independent primitive arguments). U5's load on F5 is a *negative-existence* argument (no third adjacency-axis exists). Negative-existence arguments require exhaustive primitive-level audits rather than positive constructions, and are methodologically distinct.

**U5's continuum lift is structurally simpler.** U2's continuum lift introduced an explicit conformal gauge structure that required dedicated treatment (an entire follow-up arc). U5's continuum lift is anticipated to be gauge-compatible with U2-continuum (both partition components rescale uniformly), introducing no new gauge structure. Memo 03 §4 will execute the explicit verification, but no new gauge dependency is anticipated.

**U5 has a sharper inheritance opportunity.** The earlier tightening-program memo for U5 invoked U3 (the participation-measure evolution equation, itself an upstream commitment) as a premise for the Fourier-conjugacy argument. The present arc is positioned to replace this dependency: translation invariance is a *kinematic* property of the participation graph (Primitive 06 + Primitive 03 supply graph homogeneity), not a *dynamical* property requiring U3. Memo 03 §1 will execute this re-derivation, producing a U3-independent path to F3 and tightening the U5 result correspondingly.

### 6.3 Whether U5 is cleaner or more delicate

**Anticipated: cleaner.** Synthesis paper §4.2 explicitly classifies U5 as "the cleanest" among the four remaining upstream items. The structural-symmetry argument for the Fourier-conjugate partition is plausibly derivable from the available inputs without introducing new structural commitments.

**Specific risk locations:**

1. **F5's negative-existence argument** (Memo 03 §2). The primitive-stack audit must be exhaustive. The memo will enumerate candidate third axes (bandwidth-gradient direction, rule-type coupling, polarity-amplitude, higher-derivative axes) and dismiss each. The audit is anticipated to close, but the methodology is structurally different from U2's positive constructions.

2. **F3's Fourier specificity** (Memo 03 §1). If the natural transform between $b_x$ and $b_p$ admits non-standard generalisations on the participation-measure space — e.g., fractional-Fourier on certain manifolds, or non-translation-invariant baselines — the standard Heisenberg bound might be replaced by a generalised version with a different prefactor. This is anticipated *not* to obtain on the flat-space baseline (where Stone's theorem uniquely identifies $\hat{p}$ as the translation generator and Fourier transform as its diagonalising basis-change), but the verification needs to be explicit.

3. **U3 independence** (Memo 03 §1). The earlier tightening-program memo invoked U3 freely. The present arc must execute the re-derivation under translation symmetry as a primitive-level (kinematic) input rather than a dynamical (U3) input. This is a methodological tightening, not a structural risk per se, but warrants explicit execution.

### 6.4 Overall assessment

U5 is anticipated to close FORCED with a structurally cleaner derivation than U2. The arc is expected to be 3 memos plus an optional closure memo (4 total), shorter than U2's 5+5 = 10-memo program (U2-Discrete + U2-Continuum). The downstream cascade is narrower — Heisenberg promotes to fully unconditional, but Born and Bell/Tsirelson are unaffected (already promoted by U2). The methodological pattern from born_gleason + U2 + U2-Continuum applies directly, with the additional opportunity to sharpen the existing tightening-program U5 derivation by removing its U3 dependency.

---

## 7. Recommended Next Steps

**(a) Begin Memo 02 (F1, F2, F4 derivations).** Natural next session step. The three forced-via-derivation sub-features have all their primitive-level inputs in hand; Memo 02 is verification work, not discovery work. Expected outcome: clean closure with explicit derivations of (i) F1's two-axis existence from Primitives 06 + 09, (ii) F2's two-component count via primitive-level enumeration (provisionally; pending F5's exhaustion confirmation), and (iii) F4's orthogonality from U2 + Parseval. Should be a moderate-length memo, similar in size to U2 Memo 02.

**(b) Pre-Memo-03 audit of the existing tightening-program memo `u5_adjacency_partition_derivation.md`.** Specifically: identify which arguments in §3 (Fourier conjugacy) genuinely depend on U3 versus on translation symmetry alone, and identify which arguments in §5 (exhaustion) constitute a complete primitive-level audit versus a partial one. This audit will let Memo 03 build on the existing arguments where they transfer to the sharper methodology, and replace them where they don't.

**(c) Pre-decide Memo 03's framing of the F3 / F5 verdict structure.** Two reasonable framings:
- *Tight verdict.* If F3 admits the standard-Fourier-uniqueness argument cleanly and F5's audit is exhaustive, Memo 03 produces a single FORCED verdict for U5.
- *Scoped verdict.* If F3 is restricted to flat-spacetime (standard $L^2$ Fourier; Stone's theorem applies cleanly) but its extension to curved settings (non-translation-invariant manifolds) introduces complications, Memo 03 may scope U5-FORCED to flat-spacetime baseline with a curved-spacetime extension flagged as a future arc. The U2-Continuum result was scoped similarly (gauge-fixed for downstream applications); a parallel scoping for U5 is structurally consistent. Recommended: pre-decide before drafting Memo 03 to keep the verdict framing focused.

---

## 8. Cross-references

- Arc outline: [`arcs/U5/00_arc_outline.md`](00_arc_outline.md)
- Existing tightening-program attempt at U5: [`arcs/arc-foundations/u5_adjacency_partition_derivation.md`](../arc-foundations/u5_adjacency_partition_derivation.md) (2026-04-24; supersession candidate)
- U2-Inner-Product paper (inner-product structure inherited as input for F3, F4): [`papers/U2_Inner_Product/paper_u2_inner_product.md`](../../papers/U2_Inner_Product/paper_u2_inner_product.md)
- Born_Gleason paper (Theorem 10 inherited as input for $b_x \propto |\Psi|^2$, $b_p \propto |\widetilde\psi|^2$ identifications): [`papers/Born_Gleason/born_gleason_paper.md`](../../papers/Born_Gleason/born_gleason_paper.md)
- U2 Memo 01 (parallel decomposition template): [`arcs/U2/01_decomposition_and_mapping.md`](../U2/01_decomposition_and_mapping.md)
- Born_Gleason Memo 01 (parallel decomposition template): [`arcs/born_gleason/01_gleason_inventory.md`](../born_gleason/01_gleason_inventory.md)
- Step 5 derivation (Heisenberg, downstream beneficiary of U5 closure): [`arcs/arc-foundations/uncertainty_from_participation.md`](../arc-foundations/uncertainty_from_participation.md)
- Primitive 04 (bandwidth + four-band decomposition + adjacency band): `quantum/primitives/04_participation_bandwidth.md`
- Primitive 06 (ED gradient, supplies spatial axis): `quantum/primitives/06_ed_gradient.md`
- Primitive 09 (tension polarity, $U(1)$ phase, supplies phase-propagation axis): `quantum/primitives/09_tension_polarity.md`

---

## 9. One-line memo summary

> **U5 decomposes into five sub-features: F1 (existence, forced-via-derivation from Primitives 06 + 09 supplying two distinct adjacency axes), F2 (two-component count, forced-via-derivation conditional on F5), F3 (Fourier conjugacy, LOAD-BEARING — derived from translation symmetry + Stone's theorem + U2 inner product, with an opportunity to sharpen the existing tightening-program argument by removing its U3 dependency), F4 (orthogonality under U2, forced-via-derivation via Parseval + U2-continuum gauge-invariance verification), F5 (exhaustion, LOAD-BEARING — primitive-level audit dismissing candidate third axes). Three sub-features close cleanly; two carry the substantive load. U5 is anticipated cleaner than U2 due to richer available structural inputs (U2-Discrete, U2-Continuum, Theorem 10 all FORCED as inputs); principal risk locations are F3's Fourier specificity and F5's negative-existence audit. The U2-Continuum gauge is anticipated to act uniformly on both partition components, preserving the partition under conformal rescaling.**
