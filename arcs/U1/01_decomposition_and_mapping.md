# Memo 01 — U1 Decomposition, Primitive Mapping, and Circularity Audit

**Date:** 2026-04-26
**Arc:** `arcs/U1/`
**Predecessor:** [`00_arc_outline.md`](00_arc_outline.md)
**Status:** Structural inventory memo with circularity audit. Decomposes U1 (the participation-measure construction) into four sub-features, maps each to primitive-level inputs and standard mathematical infrastructure, and explicitly identifies which prior arguments in the original Step-1 memo used downstream results that must be replaced under the present arc's primitive-only methodology. Analogous in scope to U2 Memo 01, U5 Memo 01, and born_gleason Memo 01, with the additional circularity-audit requirement specific to U1's most-upstream status.
**Purpose:** Pin down the conceptual terrain so Memo 02 can derive F2 + F4 directly and Memo 03 can focus on the load-bearing F1 (algebraic structure) and F3 (magnitude exponent) questions, with clear rules about which inputs are permitted vs forbidden.

---

## 1. The U1 Question, Stated Precisely

### 1.1 The construction

The Phase-1 QM-emergence framework adopts the participation-measure construction:

$$
P_K(x, t) = \sqrt{b_K(x, t)} \cdot e^{i \pi(K, x, t)} \qquad \text{(U1)}
$$

— a complex-valued field indexed by channel $K \in \mathcal{K}$, position $x \in V$ (or $x \in M$ in the continuum regime), and time $t \in \mathbb{R}$. The construction fuses Primitive 04's bandwidth $b_K \in \mathbb{R}_{\geq 0}$ with Primitive 09's polarity phase $\pi \in U(1)$ via the polar form, with bandwidth recovered as the squared magnitude:

$$
b_K(x, t) = |P_K(x, t)|^2.
$$

### 1.2 Role as the most upstream commitment

U1 is the *origin* of the participation-measure framework. Every downstream item — U2 (sesquilinear inner product), U3 (evolution equation), U4 (momentum-basis identification), U5 (adjacency partition), Theorem 10 (Born), Bell–Tsirelson, Heisenberg uncertainty — uses $P_K$ as a constructed object. The participation measure is the structural carrier on which the entire QM-emergence Phase-1 chain operates.

This upstream status has a methodological consequence: U1 cannot be derived using any of the downstream items as input. The structural inputs available to U1's derivation are restricted to (i) the primitive stack (Primitives 01–13, with main load on Primitives 04 and 09), (ii) standard mathematical / algebraic constructions that do not depend on the participation-measure framework, and (iii) the structural content of the participation graph itself (vertices, edges, and their primitive-level relational structure).

### 1.3 Why U1 requires primitive-only inputs

A derivation of U1 that used U2's sesquilinear inner product as an input would be circular: U2 was forced *given* U1 (the U2-Discrete and U2-Continuum theorems used $P_K$ as a constructed object throughout). Using U2 to derive U1 would close a logical loop. Similarly for Theorem 10 (used $b = |P|^2$ from U1c as a definitional input), U5 (used $b_x \propto |\Psi|^2$ from Theorem 10 + U1), U3, U4, and the Bell / Heisenberg results.

The U1 arc must therefore close from primitives + mathematics alone. This is the leanest structural environment of any arc to date, and the methodological honesty of the derivation depends on the circularity audit being explicit (Section 4).

---

## 2. Decomposition into Sub-Features

U1 packages four structurally distinct sub-claims. Each receives independent structural status determination.

### 2.1 The four sub-features

- **(F1) Complex-valued range.** $P_K$ takes values in $\mathbb{C}$, not in $\mathbb{R}$, $\mathbb{H}$ (quaternions), or some other algebra. The participation-measure space $\mathcal{P}$ is a *complex* function space.

- **(F2) Polar decomposition structure.** Once $P_K \in \mathbb{C}$, the structural form $P_K = |P_K| \cdot e^{i \arg P_K}$ is the universal polar decomposition for complex numbers. F2 asserts that this decomposition is the natural representation of the participation-measure content, with the magnitude and phase slots filled by primitive-level quantities supplied separately.

- **(F3) Magnitude exponent: $|P_K|^2 = b_K$.** The squared magnitude equals bandwidth: $b_K = |P_K|^2$, equivalently $|P_K| = \sqrt{b_K}$. This is the "Exponent-2" structural commitment underlying the entire Exponent-2 Thread (Born, Schrödinger kinetic term, Madelung form, Heisenberg).

- **(F4) Phase = polarity.** The phase factor in U1's construction is *exactly* Primitive 09's polarity phase $\pi(K, x, t)$, with no additional phase variable, no rescaling, no functional transformation. The phase slot of the polar decomposition is filled by polarity directly.

### 2.2 Anticipated structural status

| Sub-feature | Status | Reasoning |
|---|---|---|
| **F1** Complex-valued range | **load-bearing** | Choice of $\mathbb{C}$ over $\mathbb{R}$ or $\mathbb{H}$ requires a structural argument. Real QM (Stueckelberg 1960) and quaternionic QM (Adler 1995) are known formal alternatives; ruling them out structurally is non-trivial. |
| **F2** Polar decomposition | **automatic given F1** | Polar decomposition $z = |z| e^{i \arg z}$ is universal for $\mathbb{C}$; no new structural commitment beyond F1. |
| **F3** Magnitude exponent $\|P_K\|^2 = b_K$ | **load-bearing** | The "why squared?" question. Forcing $\alpha = 2$ versus $\alpha = 1, 3,$ or other exponents requires a substantive structural argument. The exponent connects to Primitive 04's bandwidth-additivity structure plus the requirement that bandwidth be a quadratic form on the participation-measure space. |
| **F4** Phase = polarity | **forced-via-derivation** | Primitive 09 is the unique primitive supplying a $U(1)$-valued phase variable. The phase slot of the polar decomposition has no other structurally-supported source. |

### 2.3 Discrete vs continuum regime split

U1's construction is regime-independent: $P_K(x, t) = \sqrt{b_K(x, t)} \cdot e^{i \pi(K, x, t)}$ is the same expression in both regimes, with $x \in V$ in the discrete case and $x \in M$ in the continuum case. The four sub-features F1–F4 carry the same structural content in both regimes.

The U2-Continuum gauge applies *downstream* of U1 — under $(b_K, d\mu) \to (\Omega^{-D} b_K, \Omega^D d\mu)$, the participation measure transforms as $P_K \to \Omega^{-D/2} P_K$, but the *form* of the U1 construction (polar decomposition with $|P|^2 = b$) is preserved. U1's derivation does not need the gauge as input; U1 is gauge-compatible with U2-Continuum by inheritance once U1 is established.

### 2.4 The "fusion" question

A fifth sub-claim is implicit in the construction: the *multiplicative* form $\sqrt{b_K} \cdot e^{i \pi_K}$ rather than additive $\sqrt{b_K} + e^{i \pi_K}$ or other operations. We treat this as a consequence of F1 + F2: once $P_K \in \mathbb{C}$ and the polar decomposition is the natural representation, the multiplicative form is the only structurally-coherent fusion of magnitude and phase. Fal-5 (non-multiplicative fusion) is therefore dispatched jointly by F1's complex-algebra structure and F2's polar-decomposition universality.

---

## 3. Mapping Each Sub-Feature to Structural Inputs

### 3.1 F1 — Complex-valued range

**Primitive inputs:**
- **Primitive 09 (Tension Polarity):** establishes polarity as $U(1)$-valued. Primitive 09 §1.16 commits explicitly to phase-valued polarity ("not a binary in general — it is a phase in the full treatment"), and §1.30 confirms this is *not* an $S^3$-valued or other higher-dimensional phase ("not a scalar"). The $U(1)$ structure of polarity supports a $\mathbb{C}$-valued phase factor $e^{i \pi}$ but does *not* support a quaternionic $S^3$-valued phase factor. F1 derives from Primitive 09's $U(1)$-only structure plus the algebraic requirement that the participation measure carry phase content.

- **Primitive 04 (Bandwidth):** supplies the magnitude content as a non-negative real scalar.

- **Primitive 03 + Primitive 07:** supply the indexing structure (channel index $K$, position $x$, edge structure of the participation graph) on which $P_K$ is defined as a function. These are not algebraic-structure inputs; they are domain-structure inputs.

**Mathematical infrastructure:**
- **Frobenius theorem (1878).** The only finite-dimensional associative real division algebras are $\mathbb{R}$, $\mathbb{C}$, $\mathbb{H}$. This restricts the algebraic-structure alternatives to a finite enumerable list, simplifying F1's negative-existence audit.

**Original Step-1 memo correspondent:** **C1 (Complex-valuedness).** The original memo states: "Amplitude + phase structure. Without phase, interference and Schrödinger fail." This argument *uses Schrödinger* — a downstream U3-dependent result — as a justification for complex-valuedness. **The argument is circular under the present arc's methodology.** The replacement argument must derive complex-valuedness from primitive-level interference / superposition structure or from Primitive 09's $U(1)$ phase content directly, *without* invoking Schrödinger.

**Forbidden inputs (circularity):** U2 (assumes $\mathcal{P}$ is a complex Hilbert space, which assumes F1); U3 / Schrödinger (downstream of U1); Theorem 10 (downstream of U1); Bell–Tsirelson (downstream).

### 3.2 F2 — Polar decomposition

**Primitive inputs:** none specifically; F2 is a mathematical consequence of F1.

**Mathematical infrastructure:**
- **Polar decomposition for $\mathbb{C}$.** Every complex number $z \neq 0$ has a unique representation $z = |z| \cdot e^{i \arg z}$ with $|z| \in \mathbb{R}_{> 0}$ and $\arg z \in [0, 2\pi)$ (with $0$ admitting either argument-zero or magnitude-zero conventions). This is universal mathematical structure for $\mathbb{C}$.

**Original Step-1 memo correspondent:** implicit in C1 (the construction $\sqrt{b_K} \cdot e^{i \pi_K}$ is itself the polar form). No separate constraint dedicated to F2.

**Forbidden inputs:** none relevant; F2 is mathematical.

### 3.3 F3 — Magnitude exponent $|P_K|^2 = b_K$

**Primitive inputs:**
- **Primitive 04 (Bandwidth).** Supplies bandwidth as the *quantity* on the magnitude side of the relation. Critically, Primitive 04 also supplies **bandwidth additivity** at the primitive-graph level: bandwidths along edges sum disjointly when channel-subsets are disjoint, and the four-band orthogonality of §1.5 ensures bandwidth doesn't mix between bands. This additivity is a *kinematic* structural property of the participation graph, independent of any participation-measure construction.

- **Primitive 09 (Tension Polarity).** $U(1)$-invariance of bandwidth is a direct consequence: under global phase rotation $\pi \to \pi + \alpha$, bandwidth is unchanged. This places a $U(1)$-invariance constraint on whatever functional relation connects $|P|$ to $b$.

**Mathematical infrastructure:**
- **Quadratic-form theory.** Classification of positive-definite quadratic forms on complex vector spaces. Combined with $U(1)$-invariance, the unique quadratic form on $\mathbb{C}$ up to overall positive scaling is $z \mapsto |z|^2 = z^* z$. This is the structural fact that anchors F3's exponent-2 commitment.

**Anticipated argument:** if the participation-measure space $\mathcal{P}$ is to be a vector space (so that linear combinations of participation measures are participation measures — a structural feature inherited automatically once F1 establishes complex-valued range, per U2 Memo 02 §2's argument applied here as a *consequence* of F1, not as inherited from U2), and if bandwidth is additive over disjoint channel-subsets (Primitive 04), then bandwidth must be a *quadratic form* on $\mathcal{P}$. Among quadratic forms on $\mathbb{C}$ that are $U(1)$-invariant on the diagonal (since bandwidth is $U(1)$-invariant per Primitive 09), the unique form (up to overall scale) is $|P|^2$. The exponent $\alpha = 2$ is structurally forced.

**Original Step-1 memo correspondent:** **C4 (Sublinear composition with exponent 2).** The original memo cites this as a constraint: "$|P_1 + P_2|^2 = |P_1|^2 + |P_2|^2 + 2 \mathrm{Re}(P_1^* P_2)$ is the squared-amplitude composition. Committed in `visibility_to_bandwidth.md §1.2`." This is a *constraint*, not a derivation. The original memo assumes the exponent-2 composition structure as an input to U1 rather than deriving it. **The present arc must derive $\alpha = 2$ from primitive-level inputs**, with C4 as a *consequence* of F3 rather than an assumption.

**Forbidden inputs (circularity):**
- **C3 (sesquilinear inner product).** This is U2 — already FORCED *given* U1 in the prior arc. Using C3 as input to F3 would be circular.
- **C8 (environmental-decohering → Born weights).** This is Theorem 10 (Born). Downstream of U1 via $b = |P|^2$.
- **C7 (thin-regime → Schrödinger).** Downstream of U1 + U3.
- **C9 (Fourier-conjugate → Heisenberg).** Downstream of U1 + U2 + U5.

**Permitted inputs:**
- **Primitive 04's bandwidth additivity** at the participation-graph level (kinematic, primitive-level).
- **Primitive 09's $U(1)$-invariance of polarity phase** (kinematic, primitive-level).
- **Mathematical quadratic-form classification.**
- **The vector-space structure of $\mathcal{P}$**, which follows automatically from F1 (complex-valued function spaces are closed under componentwise sum and scalar multiplication; this is a *consequence* of F1, not an inheritance from U2's C3a).

### 3.4 F4 — Phase = polarity

**Primitive inputs:**
- **Primitive 09 (Tension Polarity).** The primitive directly supplies a $U(1)$-valued phase $\pi(K, x, t)$. This is the *only* primitive-level $U(1)$-valued angular variable available for the construction. Other primitives (03, 04, 07, 08, 10, 11, 12, 13) supply scalar or relational structures, not angular variables.

**Mathematical infrastructure:** none specifically; F4 is a uniqueness argument from primitive enumeration.

**Anticipated argument:** the phase slot of the polar decomposition $P_K = |P_K| \cdot e^{i \arg P_K}$ requires a $U(1)$-valued angular variable. Primitive 09 supplies exactly such a variable; no other primitive does. Therefore $\arg P_K = \pi(K, x, t)$ (Primitive 09's polarity phase) is the unique structurally-supported phase. Any alternative phase variable would have to come from a primitive *not currently in the stack*, which is outside the scope of the present arc.

**Original Step-1 memo correspondent:** implicit in C1 ("Amplitude + phase structure"). The "phase" referenced in C1 is identified with polarity throughout the original memo without a separate constraint dedicated to F4.

**Forbidden inputs:** none relevant; F4 is a primitive-enumeration argument.

---

## 4. Circularity Audit

### 4.1 The audit procedure

The U1 arc's methodological honesty depends on excluding any input that depends on the participation-measure construction itself or on any downstream item that uses $P_K$ as a constructed object. We audit the original Step-1 memo `arcs/arc-foundations/participation_measure.md` for arguments that violate this exclusion, and identify replacements that close the gap.

### 4.2 The C1–C9 inventory revisited

The original memo presented nine constraints (C1–C9) on the participation-measure construction:

| Constraint | Content | Source / Status | Permitted as input to U1? |
|---|---|---|---|
| **C1** Complex-valuedness | "Amplitude + phase structure. Without phase, interference and Schrödinger fail." | Downstream-justified (cites Schrödinger, an U3-dependent result) | **No (circular).** Replacement: derive complex-valuedness from primitive-level $U(1)$-polarity + interference structure directly. |
| **C2** Channel-indexed | Indexed by channel set $\mathcal{K}$ | Primitive 07 | **Yes.** Primitive-level domain structure. |
| **C3** Sesquilinear inner product | "Enables Hilbert-space structure, orthogonal partitions, uncertainty inequalities." | This is U2 (now FORCED) | **No (circular).** U2 is downstream of U1. |
| **C4** Sublinear composition (exponent 2) | $|P_1 + P_2|^2 = |P_1|^2 + |P_2|^2 + 2 \mathrm{Re}(P_1^* P_2)$ | Visibility-to-bandwidth memo; downstream commitment | **No (circular for F3).** This is the *target* of F3's derivation, not an input. |
| **C5** Four-band decomposability | $P = P^{int} + P^{adj} + P^{env} + P^{com}$ with conservation | Primitive 04 §1.5 | **Partially.** The four-band orthogonality at the *bandwidth* level is primitive (P-04 §1.5); the decomposability at the *participation-measure* level inherits from F1 + F2 + the band-structured magnitude. We use the bandwidth-level statement as input. |
| **C6** Joint-measure non-factorizability | Bell-violating correlations | Downstream (Bell, Step 4) | **No (circular).** Downstream of U1. |
| **C7** Thin-regime → Schrödinger | Schrödinger emergence in thin limit | Downstream (Step 2 + U3 + U4) | **No (circular).** Downstream of U1. |
| **C8** Environmental-decohering → Born weights | Born rule on incoherent mixture | Downstream (Theorem 10) | **No (circular).** Downstream of U1. |
| **C9** Fourier-conjugate partition → Heisenberg | $\Delta x \Delta p \geq \hbar/2$ | Downstream (Step 5 + U5) | **No (circular).** Downstream of U1. |

**Net:** of the nine constraints in the original memo, **only C2 is fully permitted as primitive-level input**. C5 is partially permitted (the bandwidth-level four-band orthogonality, not the participation-measure-level decomposition). C1, C3, C4, C6, C7, C8, C9 are all circular and must be replaced by primitive-only arguments.

### 4.3 Permitted inputs for the U1 arc

**Primitives (in their kinematic content, not their downstream consequences):**
- Primitive 01 — micro-events (vertex set $V$).
- Primitive 03 — participation relation (edge set $E$ + relational structure of the graph).
- Primitive 04 — bandwidth as edge-weight $w : E \to \mathbb{R}_{\geq 0}$ + bandwidth additivity over disjoint channel-subsets + four-band orthogonality of §1.5 (at the bandwidth level).
- Primitive 06 — ED gradient $\nabla \rho$ (supplies spatial-structure axis if needed for arguments involving spatial coherence).
- Primitive 07 — channel index set $\mathcal{K}$ + channel-as-primitive ontology.
- Primitive 09 — tension polarity as $U(1)$-valued phase $\pi$.
- Primitives 02, 05, 08, 10, 11, 12, 13 — available as background structural context where relevant; not anticipated to be load-bearing for U1's derivation.

**Mathematical infrastructure:**
- Frobenius theorem on real division algebras.
- Polar decomposition for $\mathbb{C}$.
- Quadratic-form theory on complex vector spaces.
- $U(1)$ representation theory.
- Standard linear-algebra constructions (sum, scalar multiplication, vector-space axioms) on function spaces valued in fields.

**Implicit primitive-level structural facts:**
- *Bandwidth $U(1)$-invariance.* Bandwidth $b_K = |P_K|^2$ is invariant under global polarity rotation $\pi \to \pi + \alpha$. This invariance is *primitive-level* in the sense that bandwidth and polarity are independent primitives whose interaction is constrained: rotating polarity does not change bandwidth.
- *Bandwidth additivity over disjoint channel-subsets.* From Primitive 04 directly (not via U2's inner product).

### 4.4 Forbidden inputs

**Downstream FORCED items:**
- **U2-Discrete and U2-Continuum** (sesquilinear inner product). Used $P_K$ as input throughout; circular.
- **Theorem 10 (Born rule via Gleason–Busch).** Used $b = |P|^2$ identification (i.e., F3) as a definitional input; circular for F3, and circular for F1 because Theorem 10 inherits Hilbert-space structure from U2.
- **U5 (adjacency-band Fourier-conjugate partition).** Inherited Theorem 10 + U2; transitively circular.

**Downstream CANDIDATE items:**
- **U3 (participation-measure evolution equation).** Uses $P_K$ as input; would be circular.
- **U4 (momentum-basis identification).** Uses $P_K$ as input; circular.

**Downstream non-theorem statements:**
- **Schrödinger evolution (Step 2 of QM-emergence).** Inherits U3 + U4.
- **Bell–Tsirelson bound (Step 4).** Inherits U2 + U1.
- **Heisenberg uncertainty (Step 5).** Inherits U2 + U5 + Theorem 10.

The forbidden-inputs list is *every downstream theorem and CANDIDATE in the QM-emergence Phase-1 program*. U1 must close from the primitives + mathematics alone.

### 4.5 Specific replacements for the original Step-1 arguments

The original Step-1 memo's arguments that violate the circularity exclusion are:

- **C1's justification ("Without phase, interference and Schrödinger fail").** The Schrödinger reference is downstream of U1 + U3. **Replacement:** complex-valuedness is forced by Primitive 09's $U(1)$-valued polarity directly — the phase factor $e^{i \pi}$ is well-defined only on a complex-algebra carrier (or a higher-dimensional algebra with a $U(1)$ subgroup). Primitive 09's phase content cannot be carried by a real-valued participation measure; therefore $\mathcal{P}$ must be at least $\mathbb{C}$-valued. Quaternionic alternatives are dismissed by Primitive 09's commitment to $U(1)$-only (not $S^3$-valued) polarity. Memo 03 §1 will execute this replacement explicitly.

- **C4's exponent-2 commitment.** The original memo treats this as adopted from `visibility_to_bandwidth.md`. **Replacement:** $\alpha = 2$ is forced by (i) bandwidth additivity over disjoint channel-subsets (Primitive 04, kinematic), (ii) the requirement that bandwidth be a quadratic form on the complex-valued participation-measure space (forced by additivity + linearity-from-F1), and (iii) the unique $U(1)$-invariant positive-definite quadratic form on $\mathbb{C}$ being $|z|^2$. Memo 03 §2 will execute this replacement explicitly.

- **C3's inner product.** Used as a constraint in the original memo without derivation. **Note for the present arc:** U2 has now been derived, but it depends on U1, so we cannot use U2 as input to U1. We *can* use the structural fact that $\mathcal{P}$ is a complex vector space (which follows from F1 alone), and the structural fact that bandwidth is additive (Primitive 04). These are sufficient for F3's quadratic-form argument without invoking U2's full inner-product structure.

---

## 5. Falsifier-to-Sub-Feature Mapping

Per Memo 00 §4.1, five falsifiers attach to U1's sub-features. The mapping:

| Falsifier | Attaches to | Description | Anticipated dispatch |
|---|---|---|---|
| **Fal-1** Real-valued | F1 | $P_K$ takes values in $\mathbb{R}$, not $\mathbb{C}$, with phase content separately encoded | Dispatched in Memo 03 via Primitive 09's $U(1)$ phase requirement (real-algebra cannot carry a $U(1)$ phase factor structurally; phase content cannot be cleanly separated without losing primitive-level coherence) |
| **Fal-2** Quaternionic | F1 | $P_K$ takes values in $\mathbb{H}$, requiring $S^3$-valued or higher-dimensional phase content | Dispatched in Memo 03 via Primitive 09's commitment to $U(1)$-only polarity (Primitive 09 §1.30 "not a scalar"; phase-valued; specifically circular not spherical) |
| **Fal-3** Different exponent | F3 | $|P|^\alpha = b$ for $\alpha \neq 2$ | Dispatched in Memo 03 via bandwidth additivity (Primitive 04) + $U(1)$-invariance (Primitive 09) forcing bandwidth to be a $U(1)$-invariant quadratic form on $\mathbb{C}$, uniquely $|z|^2$ |
| **Fal-4** Phase ≠ polarity | F4 | Phase factor uses some angular variable distinct from polarity | Dispatched in Memo 02 via primitive-enumeration: only Primitive 09 supplies a $U(1)$-valued angular variable; no alternative exists |
| **Fal-5** Non-multiplicative fusion | F1 + F2 jointly | Bandwidth and polarity combined by an operation other than multiplication | Dispatched in Memo 02 via polar-decomposition universality: once F1 establishes $\mathbb{C}$-valued range, the multiplicative form $|P| \cdot e^{i \arg}$ is the unique structurally-coherent representation of magnitude + phase |

### 5.1 Discrete-regime versus continuum-regime falsifier attachment

All five falsifiers attach uniformly in both regimes. U1's construction is regime-independent at the level of structural content; the falsifiers operate at the algebraic / structural level rather than the regime level.

---

## 6. Memo-Level Summary Table

| Sub-feature | Status | Primitive inputs | Falsifier(s) | Circularity risk notes |
|---|---|---|---|---|
| **F1** Complex-valued range | **load-bearing** | Primitive 09 ($U(1)$ polarity); Primitive 04 (real-valued bandwidth as magnitude); Frobenius theorem (math) | Fal-1, Fal-2 | Original memo's C1 cited Schrödinger (downstream); replacement argument must use Primitive 09's $U(1)$-only structure directly. **Circularity risk: high if Schrödinger or interference-from-quantum-state is invoked.** Replacement: argue from $U(1)$-phase-cannot-live-in-$\mathbb{R}$ + $U(1) \subset \mathbb{C}$ requires $\mathbb{C}$. |
| **F2** Polar decomposition | **automatic given F1** | Polar decomposition for $\mathbb{C}$ (math) | Fal-5 (jointly with F1) | No primitive input directly; mathematical consequence of F1. Circularity risk: none. |
| **F3** Magnitude exponent $\|P\|^2 = b$ | **load-bearing** | Primitive 04 (bandwidth additivity); Primitive 09 ($U(1)$-invariance of bandwidth); quadratic-form theory (math) | Fal-3, Fal-5 | Original memo adopted exponent-2 from visibility_to_bandwidth.md (downstream commitment); the present arc must derive $\alpha = 2$ structurally. **Circularity risk: high if Born, Schrödinger kinetic, or any downstream exponent-2 manifestation is invoked.** Replacement: bandwidth additivity (kinematic, P-04) + $U(1)$-invariance (kinematic, P-09) + linearity (consequence of F1) → bandwidth is $U(1)$-invariant quadratic form → $\alpha = 2$ uniquely. |
| **F4** Phase = polarity | **forced-via-derivation** | Primitive 09 ($U(1)$-valued phase); primitive-enumeration (no alternative phase variable) | Fal-4 | Original memo identifies phase with polarity throughout without separate constraint. Circularity risk: low. Argument: Primitive 09 is the unique primitive-level $U(1)$-valued angular variable. |

**Net.** Two sub-features are load-bearing (F1, F3); one is automatic (F2); one is forced-via-derivation (F4). Both load-bearing items have meaningful circularity risk, primarily because the original Step-1 memo's arguments for C1 (mapped to F1) and C4 (mapped to F3) used downstream-justified content. The replacement arguments must be derived from primitive-level kinematic structure plus mathematical infrastructure, with explicit care to avoid invoking U2, Theorem 10, U5, U3, U4, or any downstream consequence.

---

## 7. Recommended Next Steps

**(a) Begin Memo 02 (F2 + F4 derivations).** Natural next session step. F2 (polar decomposition) and F4 (phase = polarity) are the cleaner sub-features; both close via mathematical / enumeration arguments without significant circularity risk. F2 uses standard polar-decomposition universality; F4 uses primitive-enumeration to identify Primitive 09 as the unique source of a $U(1)$-valued angular variable. Expected outcome: clean closure of both. Memo 02 should be moderately short.

**(b) Pre-Memo-03 audit of bandwidth-additivity content in Primitive 04 and the visibility-to-bandwidth memo.** F3's load-bearing argument hinges on bandwidth additivity at the *primitive-graph* level (kinematic, P-04 directly) being independent of the *participation-measure-level* additivity (which uses F1's complex-vector-space structure). A focused read of Primitive 04 §2 (the bandwidth definition) and `arcs/arc-foundations/visibility_to_bandwidth.md §1.2` (cited by the original memo as the source of the exponent-2 commitment) before drafting Memo 03 will clarify which content is genuinely primitive-level kinematic and which content depends on downstream constructions. The goal is to identify the precise primitive-level statement of bandwidth additivity that F3 can use as input *without* circularity.

**(c) Pre-decide Memo 03 single-vs-double framing for F1 and F3.** Memo 00 §7(c) flagged this decision. Two reasonable options:
- *Single Memo 03* covering both F1 and F3 (with §1 on F1 and §2 on F3).
- *Two memos*: Memo 03 for F1 (algebraic-structure question; quaternionic-QM literature engagement); Memo 04 for F3 (magnitude-exponent question; quadratic-form argument); closure-and-summary becomes Memo 05.

Recommended: *single Memo 03* unless Memo 02 reveals one of F1 or F3 has more substantive content than anticipated. The substantive content of F1 (real / quaternionic dismissal) and F3 (quadratic-form argument) are anticipated to fit comfortably in a single load-bearing memo, as they did for U5's F3 + F5 in U5 Memo 03.

---

## 8. Cross-references

- Arc outline: [`arcs/U1/00_arc_outline.md`](00_arc_outline.md)
- Step-1 participation-measure memo (audit target; contains C1–C9 constraints): [`arcs/arc-foundations/participation_measure.md`](../arc-foundations/participation_measure.md)
- Visibility-to-bandwidth memo (cited by original memo as source of exponent-2 commitment; audit for F3): [`arcs/arc-foundations/visibility_to_bandwidth.md`](../arc-foundations/visibility_to_bandwidth.md) *(if not present, equivalent content in `theory/visibility_to_bandwidth.md` per memory record)*
- U2 Memo 01 (parallel decomposition template): [`arcs/U2/01_decomposition_and_mapping.md`](../U2/01_decomposition_and_mapping.md)
- U5 Memo 01 (parallel decomposition template, particularly for the negative-existence audit pattern relevant to F1 and Fal-2): [`arcs/U5/01_decomposition_and_mapping.md`](../U5/01_decomposition_and_mapping.md)
- Born_Gleason Memo 01 (parallel template for inventory pattern): [`arcs/born_gleason/01_gleason_inventory.md`](../born_gleason/01_gleason_inventory.md)

**Source primitives:**
- Primitive 03 (Participation): `quantum/primitives/03_participation.md`
- Primitive 04 (Bandwidth, with bandwidth-additivity content load-bearing for F3): `quantum/primitives/04_participation_bandwidth.md`
- Primitive 07 (Channel): `quantum/primitives/07_channel.md`
- Primitive 09 (Tension Polarity, $U(1)$-valued phase, load-bearing for F1, F4): `quantum/primitives/09_tension_polarity.md`

**Foundations-of-QM literature:**
- S. L. Adler, *Quaternionic Quantum Mechanics and Quantum Fields* (Oxford, 1995). Quaternionic-QM literature relevant for Fal-2 in Memo 03.
- E. C. G. Stueckelberg, *Quantum theory in real Hilbert space* (Helv. Phys. Acta 33, 727, 1960). Real-QM literature relevant for Fal-1 in Memo 03.
- F. G. Frobenius, *Über lineare Substitutionen und bilineare Formen*, J. Reine Angew. Math. 84, 1–63 (1878). Frobenius theorem on real division algebras.

**Project memory:** `memory/project_qm_emergence_arc.md`

---

## 9. One-line memo summary

> **U1 decomposes into four sub-features: F1 complex-valued range (load-bearing; original memo's C1 cited Schrödinger downstream and must be replaced by argument from Primitive 09's $U(1)$-only polarity + Frobenius classification), F2 polar decomposition (automatic given F1, mathematical), F3 magnitude exponent $|P|^2 = b$ (load-bearing; original memo's C4 was downstream-imported and must be replaced by argument from Primitive 04's bandwidth additivity + Primitive 09's $U(1)$-invariance + quadratic-form classification on $\mathbb{C}$), F4 phase = polarity (forced-via-derivation by primitive-enumeration: Primitive 09 is the unique $U(1)$-valued angular variable in the stack). Circularity audit: of the original Step-1 memo's nine constraints C1–C9, only C2 is fully permitted as primitive-level input; C5 partially permitted (bandwidth-level four-band orthogonality only); C1, C3, C4, C6, C7, C8, C9 are all circular under U1's most-upstream methodology. Permitted inputs: Primitives 01–13 in their kinematic content, plus Frobenius theorem, polar decomposition, quadratic-form theory, $U(1)$ rep theory, standard linear algebra. Forbidden inputs: U2 (downstream), Theorem 10 (downstream), U5 (downstream), U3 / U4 / Schrödinger / Bell / Heisenberg (all downstream of U1). Five falsifiers attach: Fal-1 (real-valued) → F1, Fal-2 (quaternionic) → F1, Fal-3 (different exponent) → F3, Fal-4 (phase ≠ polarity) → F4, Fal-5 (non-multiplicative fusion) → F1 + F2 jointly. Both regimes attach uniformly. Recommended Memo 03 framing: single load-bearing memo covering F1 + F3, parallel to U5 Memo 03's F3 + F5 treatment.**
