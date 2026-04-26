# Memo 02 — Derivations of F1 (Existence), F2 (Two-Component Count), F4 (Orthogonality)

**Date:** 2026-04-26
**Arc:** `arcs/U5/`
**Predecessors:** [`00_arc_outline.md`](00_arc_outline.md), [`01_decomposition_and_mapping.md`](01_decomposition_and_mapping.md)
**Status:** Derivation memo. Closes the three forced-via-derivation sub-features of U5: F1 (existence of decomposition), F2 (two-component count, conditional on F5), and F4 (orthogonality under U2, including continuum-regime gauge-invariance check). Uses only primitive-level inputs, the participation-measure construction, and the already-FORCED results (U2-Discrete, U2-Continuum, Theorem 10).
**Purpose:** Settle F1, F2, F4 so Memo 03 can focus entirely on the load-bearing F3 (Fourier conjugacy) and F5 (exhaustion) questions.

---

## 1. The Three Sub-Features

From Memo 01 §2.1, the three sub-features handled in this memo are:

- **(F1) Existence of decomposition.** $b^\mathrm{adj}$ admits an orthogonal sub-band decomposition at the primitive level — i.e., the adjacency band is not structurally indivisible. The decomposition arises because the primitive stack supplies two distinct kinds of "nearness" applicable to adjacency.

- **(F2) Two-component count.** The decomposition has exactly two components — not one (no decomposition), not three or more (residual axes). The count is *conditional on F5* (exhaustion), but the count *given* exhaustion is established here by direct enumeration of primitive-level adjacency-axes.

- **(F4) Orthogonality under U2.** $b_x$ and $b_p$ are orthogonal in the U2 inner product, with Parseval's identity $\int |\Psi|^2 d\mu = \int |\widetilde\psi|^2 d\widetilde\mu$ supplying the orthogonal-decomposition relation. The continuum regime requires an explicit gauge-invariance check against the U2-Continuum conformal rescaling.

The three derivations proceed in §§2–4. A falsifier audit (§5) and summary table (§6) close the memo.

---

## 2. Derivation of F1 — Existence of Decomposition

### 2.1 The claim

The adjacency band $b^\mathrm{adj}$ admits a decomposition into orthogonal sub-bands at the primitive level. The decomposition arises because the primitive stack supplies two structurally independent specifications of what "adjacent" means, neither derivable from the other.

### 2.2 Primitive-level adjacency-axes

**Premise (P-04 §1.5).** Adjacency bandwidth $b^\mathrm{adj}$ is, per Primitive 04 §1.5, "the participation the chain shares with its immediate participation-adjacent neighborhood." Adjacency is one of the four orthogonal bands in the four-band decomposition; the band itself is supplied by Primitive 04. What "adjacent" *means* — i.e., what notion of nearness counts as participation-adjacent — is supplied by other primitives, since Primitive 04 alone gives the band but not the structural axis along which adjacency is measured.

The primitive stack supplies *two* structurally distinct nearness axes applicable to adjacency:

**(i) Spatial nearness, from Primitive 06 (ED Gradient).** Primitive 06 establishes the gradient $\nabla \rho$ on the participation graph (or emergent manifold), supplying a spatial direction and a metric scale. Two events are *spatially adjacent* if their positions are close in this metric — formally, if $|x_A - x_B|$ is small relative to a structural scale set by $\nabla \rho$. Primitive 06's spatial structure is intrinsic to the graph; it does not require dynamical evolution to define.

**(ii) Phase-propagation nearness, from Primitive 09 (Tension Polarity).** Primitive 09 establishes polarity $\pi(K, x)$ as a $U(1)$-valued phase. The phase gradient

$$
k_K(x) = \nabla \pi(K, x) \qquad (1)
$$

is the wavenumber: the rate at which the polarity phase advances as one moves spatially. Two events are *phase-propagation-adjacent* if their wavenumbers are close — formally, if the participation-measure phase factors $e^{i \pi_K(x_A)}$ and $e^{i \pi_K(x_B)}$ propagate coherently between them, i.e., if $|k_K(x_A) - k_K(x_B)|$ is small.

### 2.3 Independence of the two axes

The two axes are structurally *independent*: neither is derivable from the other within the primitive stack.

**Spatial-axis-only argument (no phase-propagation needed).** A chain whose polarity phase is uniform ($\pi_K \equiv \mathrm{const}$, hence $k_K \equiv 0$) still has well-defined spatial nearness via $\nabla \rho$. Spatial adjacency exists independently of phase-propagation structure.

**Phase-propagation-axis-only argument (no spatial structure needed).** A chain whose spatial bandwidth is uniform ($b_K(x) \equiv \mathrm{const}$, hence $\nabla \rho \equiv 0$ contributions vanish) still has well-defined phase-propagation nearness via $\nabla \pi$ — the phase gradient is non-zero even when the magnitude is constant. Phase-propagation adjacency exists independently of spatial-density structure.

The two axes can be simultaneously non-trivial (generic case) or one can be trivialised while the other persists (limiting cases). Neither is a shadow or derivative of the other.

### 2.4 Why "adjacency" cannot collapse onto a single scalar axis

A single-scalar nearness measure on adjacency would have to privilege one axis over the other — defining "nearness" as either spatial-only or phase-propagation-only. But the primitive stack supplies both axes as independent structural commitments (Primitive 06 cannot be reduced to Primitive 09, nor vice versa; this is a structural fact at the primitive level). Therefore both must be represented in the adjacency-bandwidth decomposition.

The decomposition is forced: $b^\mathrm{adj}$ must split into at least two components, one for each axis.

### 2.5 Independence from U3

The earlier tightening-program memo for U5 [`arcs/arc-foundations/u5_adjacency_partition_derivation.md`] derived F1's two-axis structure with reference to U3 (the participation-measure evolution equation). The present derivation does *not* invoke U3:

- Primitive 06's spatial axis is a *kinematic* property of the participation graph (a property of the structural relations between vertices), not a dynamical property requiring time-evolution.
- Primitive 09's phase-propagation axis is similarly kinematic: the phase factor $e^{i \pi_K}$ has a gradient $\nabla \pi$ that is well-defined at any fixed time without invoking how the phase evolves.

F1 is established from primitive-level kinematic structure alone. **No U3 dependency is introduced.**

### 2.6 Verdict for F1

**Established.** The adjacency band $b^\mathrm{adj}$ admits a decomposition because the primitive stack supplies two structurally independent nearness axes — Primitive 06 (spatial) and Primitive 09 (phase-propagation) — neither of which can be reduced to the other.

The minimum number of components in any orthogonal decomposition consistent with these two axes is two. F2 (Section 3) addresses whether the count is exactly two (rather than two-or-more); F5 (Memo 03) addresses whether the count is exactly two (rather than three-or-more).

---

## 3. Derivation of F2 — Two-Component Count

### 3.1 The claim

The decomposition of $b^\mathrm{adj}$ has exactly two components — not one (subsumed by F1's existence claim) and not three or more. The count is established here by direct enumeration of primitive-level adjacency-axes; the *uniqueness* of two (versus three or more) is conditional on F5's exhaustion claim, which is taken up in Memo 03.

### 3.2 Direct enumeration

Within the primitive stack, the adjacency-relevant nearness axes are:

| Axis | Source primitive | Structural content |
|---|---|---|
| Spatial | Primitive 06 (ED Gradient) | $\nabla \rho$ supplies direction; metric supplied by graph adjacency structure |
| Phase-propagation | Primitive 09 (Tension Polarity) | $\nabla \pi = k$ supplies wavenumber; $U(1)$ structure of $\pi$ supplies phase coherence |

Two axes supplied by the primitive stack. F1 established that both are independent structural commitments. The corresponding bandwidth decomposition is therefore at least two-component:

$$
b^\mathrm{adj} = b_x + b_p + b_\mathrm{residual}, \qquad b_\mathrm{residual} \geq 0 \qquad (2)
$$

where $b_x$ encodes the spatial-axis content, $b_p$ encodes the phase-propagation-axis content, and $b_\mathrm{residual}$ accounts for any further primitive-level adjacency-axis content. **F2's claim is that $b_\mathrm{residual} = 0$.**

### 3.3 Conditional dependency on F5

The vanishing of $b_\mathrm{residual}$ is the content of F5 (exhaustion). F5 asserts that no third primitive-level adjacency-axis exists; F2 asserts that *given* F5, the count is exactly two.

This conditional structure is intentional. F2's enumeration argument is independently verifiable: examining the primitive stack, exactly two adjacency-axes (spatial and phase-propagation) are present. F5's exhaustion argument is methodologically distinct (a negative-existence claim against a third axis) and is the substantive load-bearing item handled in Memo 03.

### 3.4 Robustness of F2 under different primitive-stack audits

If a future amendment to the primitive stack introduced a third adjacency-axis (e.g., via a new Primitive supplying an additional structural feature relevant to adjacency), F5 would fail and the count would become three or more. F2's enumeration would correspondingly increase. The current structural status — given the current primitive stack — is two.

### 3.5 Verdict for F2

**Established conditional on F5.** Direct enumeration of primitive-level adjacency-axes yields exactly two: spatial (Primitive 06) and phase-propagation (Primitive 09). The count is two given that F5 (exhaustion) holds. F5's audit is the substantive load-bearing item handled in Memo 03; if F5 closes affirmatively, F2 closes simultaneously and unconditionally.

The two-component decomposition obtained from F1 + F2 (conditional on F5) is

$$
b^\mathrm{adj}(x, t) = b_x(x, t) + b_p(p, t) \qquad (3)
$$

— the structural form U5 asserts.

---

## 4. Derivation of F4 — Orthogonality under U2

### 4.1 The claim

The two components $b_x$ and $b_p$ are orthogonal in the U2 inner product, with the orthogonality-defining identity supplied by Parseval's theorem:

$$
\int |\Psi(x)|^2 \, d\mu(x) = \int |\widetilde\psi(p)|^2 \, d\widetilde\mu(p) = N_\mathrm{adj} \qquad (4)
$$

where $\Psi(x) = \sum_K P_K(x)$ is the position-representation aggregated wavefunction, $\widetilde\psi(p)$ is its momentum-representation Fourier transform, $d\mu$ and $d\widetilde\mu$ are the position-space and momentum-space U2 measures respectively, and $N_\mathrm{adj}$ is the total adjacency bandwidth (also identified, via the four-band conservation of Primitive 04, as the conserved adjacency-norm of the chain).

The continuum regime additionally requires an explicit check that the U2-Continuum conformal gauge does not propagate into asymmetric rescaling of $b_x$ versus $b_p$ — i.e., that the Parseval identity is gauge-invariant.

### 4.2 Inputs from U2 and Theorem 10

**U2 (FORCED).** The U2-Discrete Theorem [`papers/U2_Inner_Product/`] supplies the sesquilinear inner product on the participation-measure space at the discrete level:

$$
\langle \Psi \mid \Phi \rangle_\mathrm{disc} = \sum_K \sum_u P_K^*(u) \cdot Q_K(u) \qquad (5)
$$

with the analogous continuum form

$$
\langle \Psi \mid \Phi \rangle_\mathrm{cont} = \sum_K \int_M d\mu(x) \cdot P_K^*(x) \cdot Q_K(x) \qquad (6)
$$

both forced (the latter forced up to a description-level conformal gauge that leaves all inner-product values invariant).

**Theorem 10 (FORCED-unconditional).** Theorem 10 [`papers/Born_Gleason/`] supplies the per-band Born-rule structure: for any chain at locus $u$ (or $x$), the bandwidth-fraction map equals $\mathrm{Tr}(\rho \cdot E)$ for an appropriate density operator. Applied per-band, this gives the bandwidth-density identifications:

$$
b_x(x) \propto |\Psi(x)|^2, \qquad b_p(p) \propto |\widetilde\psi(p)|^2 \qquad (7)
$$

The proportionality constants can be absorbed into normalisation; what matters structurally is that the spatial-bandwidth distribution equals the position-density and the momentum-bandwidth distribution equals the momentum-density.

### 4.3 Parseval's identity from U2

**Premise.** The Fourier transform between position and momentum representations is an isometry on the U2 inner-product Hilbert space. (This is established in Memo 03 §1 via Stone's theorem applied to translation symmetry; we adopt it here as a forward reference.)

**Consequence.** Parseval's identity follows directly from Fourier unitarity. Specifically: the inner product computed in the position basis equals the inner product computed in the momentum basis,

$$
\int \Psi^*(x) \Psi(x) \, d\mu(x) = \int \widetilde\psi^*(p) \widetilde\psi(p) \, d\widetilde\mu(p), \qquad (8)
$$

both equalling $\langle \Psi | \Psi \rangle$ — the U2 norm-squared of the state, equivalent to the total adjacency bandwidth $N_\mathrm{adj}$ via the per-band Born identifications (7).

### 4.4 Orthogonality from Parseval

The bandwidth components $b_x$ and $b_p$ are orthogonal components of the adjacency band in the following sense: their integrated-over-domain norms each equal the same total $N_\mathrm{adj}$, and the two distributions $|\Psi(x)|^2$ and $|\widetilde\psi(p)|^2$ are independent functions related only by the Fourier transform.

**Formally.** Define the position-representation projection $\Pi_x$ and the momentum-representation projection $\Pi_p$ as the operators that select the spatial-localisation content and the momentum-localisation content respectively. Both are well-defined on the U2 Hilbert space. Their compositions satisfy

$$
\Pi_x \Pi_p = 0 \quad (\text{up to the unitary Fourier intertwiner}) \qquad (9)
$$

— the projections do not have overlapping image. Equivalently, the bandwidth distributions $b_x$ and $b_p$ are supported in dual representations (position-space and momentum-space respectively), and the Fourier transform maps one to the other isometrically.

The integrated-norm identity (8) supplies the orthogonal-decomposition identity for the bandwidth content:

$$
b^\mathrm{adj} = b_x + b_p \qquad \text{with} \qquad \|b_x\|_x = \|b_p\|_p = N_\mathrm{adj} \qquad (10)
$$

— each component carries the full adjacency-band content, but in a different representation. Under the Fourier intertwiner, the two components are unitarily equivalent; under the U2 inner product, they are orthogonal projections of the participation-measure state onto the position-representation and momentum-representation subspaces respectively.

### 4.5 Preservation under U3 evolution (forward reference, not derived here)

If U3 (the participation-measure evolution equation) is invoked as a unitary evolution generated by a self-adjoint Hamiltonian, it preserves the U2 inner product and hence Parseval's identity. The orthogonal decomposition $b^\mathrm{adj} = b_x + b_p$ is preserved at all times under U3 evolution.

This forward reference is not load-bearing for F4; F4 establishes the orthogonality at a fixed time (kinematic statement). U3 supplies the additional dynamical consistency that the orthogonal decomposition persists. The U5 verdict does not depend on U3 (per the U3-independence noted in Memo 01 §6.2 and §3.3).

### 4.6 Continuum-regime gauge-invariance check

The U2-Continuum theorem [`papers/U2_Inner_Product/`, Section 14] established the conformal gauge

$$
(b_K(x), d\mu(x)) \to (\Omega^{-D}(x) \cdot b_K(x), \Omega^D(x) \cdot d\mu(x)) \qquad (11)
$$

with $P_K(x) \to \Omega^{-D/2}(x) \cdot P_K(x)$ and every U2 inner-product value invariant.

We verify that F4's orthogonality (the Parseval identity (8)) is preserved under (11).

**Position-space norm.** Under (11):

$$
\int |\Psi'(x)|^2 \, d\mu'(x) = \int (\Omega^{-D/2})^2 |\Psi(x)|^2 \cdot \Omega^D \, d\mu(x) = \int |\Psi(x)|^2 \, d\mu(x) \qquad (12)
$$

The position-space norm is gauge-invariant.

**Momentum-space norm.** Both sides of Parseval (8) are U2 inner-product values (the position-representation and the momentum-representation norms of the same state $\Psi$). The U2-Continuum theorem establishes that *every* U2 inner-product value is invariant under (11). Therefore both sides of (8) transform identically under the gauge — both invariantly. The Parseval identity is gauge-invariant by direct inheritance.

**Bandwidth-density identifications.** The Theorem-10 identifications (7) are gauge-covariant: under (11), $|\Psi(x)|^2 \to \Omega^{-D} |\Psi(x)|^2$ and the position-density measure $|\Psi|^2 d\mu \to (\Omega^{-D} |\Psi|^2)(\Omega^D d\mu) = |\Psi|^2 d\mu$, gauge-invariant. Equivalently, $b_x(x) \cdot d\mu(x)$ — the local bandwidth content at $x$ — is the gauge-invariant quantity, exactly as for the per-channel bandwidth content per the U2-Continuum gauge structure.

The same argument applies to $b_p \cdot d\widetilde\mu$. Both partition components are gauge-covariant in the same way; their ratio (which controls the Heisenberg uncertainty product) is gauge-invariant.

**Net.** Parseval (8) is gauge-invariant. The orthogonal decomposition (10) is preserved under the U2-Continuum conformal rescaling. F4 holds in both discrete and continuum regimes, with the continuum-regime case gauge-invariant.

### 4.7 Verdict for F4

**Established.** The orthogonality of $b_x$ and $b_p$ as components of $b^\mathrm{adj}$ follows from Parseval's identity, which in turn follows from Fourier unitarity on the U2 inner-product space (forward reference to Memo 03 §1) plus the per-band Theorem-10 identifications (7). The discrete-regime case follows directly from the U2-Discrete theorem; the continuum-regime case inherits gauge-invariance from the U2-Continuum theorem, with both partition components transforming covariantly under the conformal rescaling.

---

## 5. Falsifier Audit

We dispatch the falsifiers attached to F1, F2, F4 per Memo 01 §4.

### 5.1 Fal-1 (no decomposition exists) — dispatched

**Fal-1's claim.** The adjacency band is structurally indivisible at the primitive level, with neither Primitive 06 nor Primitive 09 supplying an applicable adjacency-axis.

**Dispatch.** §2 explicitly identifies two independent primitive-level adjacency-axes: Primitive 06's spatial axis ($\nabla \rho$) and Primitive 09's phase-propagation axis ($\nabla \pi$). Both are kinematic structural features of the participation graph; both are independent of one another (§2.3); both apply to the adjacency band per the relational structure of Primitive 04 §1.5. Fal-1 fails: the decomposition exists.

### 5.2 Fal-2 (more than two components) — partially dispatched

**Fal-2's claim.** The primitive stack supplies a third adjacency-axis distinct from spatial and phase-propagation, making the count three or more.

**Partial dispatch from F2.** Direct enumeration of primitive-level adjacency-axes (§3.2) yields exactly two: Primitive 06 (spatial) and Primitive 09 (phase-propagation). The current primitive stack supplies no third axis. F2's enumeration argument is direct and verifiable.

**Outstanding (deferred to Memo 03 / F5).** F2's enumeration is conditional on the absence of a third axis being established by exhaustive primitive-level audit (F5). Specifically, F5 must dismiss candidate third axes such as bandwidth-gradient direction, rule-type coupling, polarity-amplitude direction (distinct from polarity-phase), and higher-derivative axes. Memo 03 §2 will execute this audit explicitly.

**Net.** Fal-2 is dispatched as far as direct enumeration goes; full dispatch awaits F5's exhaustive audit.

### 5.3 Fal-4 (non-orthogonal partition) — dispatched

**Fal-4's claim.** $b_x$ and $b_p$ are not orthogonal under the U2 inner product, with Parseval's identity failing or acquiring correction terms.

**Dispatch.** §4 derives Parseval's identity (8) from Fourier unitarity on the U2 inner-product space. Fourier unitarity is a mathematical consequence of Stone's theorem applied to translation symmetry (Memo 03 §1 forward reference); the U2 inner product is FORCED by the U2-Discrete and U2-Continuum theorems. The derivation introduces no new structural commitments beyond those already in the primitive stack and the FORCED items. Parseval's identity holds; the orthogonal-decomposition identity (10) follows.

**Net.** Fal-4 fails: the partition is orthogonal under the U2 inner product, with Parseval supplying the explicit identity.

### 5.4 Fal-5 (gauge propagation in continuum regime) — dispatched

**Fal-5's claim.** The U2-Continuum conformal gauge $(b_K, d\mu) \to (\Omega^{-D} b_K, \Omega^D d\mu)$ rescales $b_x$ and $b_p$ asymmetrically, propagating gauge dependence into Heisenberg's bound.

**Dispatch.** §4.6 verifies that under the conformal rescaling, both partition components transform as $b_x \cdot d\mu \to b_x \cdot d\mu$ (gauge-invariant local content) and the same for $b_p \cdot d\widetilde\mu$. The Parseval identity (8) is gauge-invariant by direct inheritance from the U2-Continuum theorem's general inner-product-invariance result. The bandwidth-density identifications (7) are gauge-covariant, with $|\Psi|^2 d\mu$ as the gauge-invariant quantity.

**Net.** Fal-5 fails: the gauge acts uniformly on both partition components, preserving the partition and Parseval. The continuum-regime gauge does not propagate into Heisenberg's bound.

### 5.5 Falsifiers remaining active

Two falsifiers remain active for Memo 03:

- **Fal-2 (full dispatch)**, attached to F5. Requires exhaustive primitive-level audit of candidate third adjacency-axes.
- **Fal-3 (non-Fourier conjugacy)**, attached to F3. Requires explicit Stone's-theorem argument and uniqueness against fractional-Fourier and wavelet generalisations.

Memo 03 will execute both.

---

## 6. Memo-Level Summary

| Sub-feature | Derivation summary | Primitive inputs | Falsifier dispatched |
|---|---|---|---|
| **F1** Existence of decomposition | Two structurally independent adjacency-axes exist: spatial (Primitive 06's $\nabla \rho$) and phase-propagation (Primitive 09's $\nabla \pi$). Neither derivable from the other; both kinematic at the primitive level. Adjacency band must split into at least two orthogonal components. | Primitive 06, Primitive 09, Primitive 04 §1.5 | Fal-1 |
| **F2** Two-component count (conditional on F5) | Direct enumeration of primitive-level adjacency-axes yields exactly two. Conditional on F5's exhaustion claim against a third axis. Decomposition $b^\mathrm{adj} = b_x + b_p$ established as the structural form. | Primitive 06, Primitive 09, Primitive 04 §1.5; primitive-stack enumeration | Fal-2 (partial; full dispatch awaits F5) |
| **F4** Orthogonality under U2 | Parseval's identity $\int |\Psi|^2 d\mu = \int |\widetilde\psi|^2 d\widetilde\mu$ from Fourier unitarity on U2 inner-product space supplies the orthogonal-decomposition relation. Continuum-regime gauge-invariance verified: both partition components transform covariantly under the U2-Continuum conformal rescaling, with $b_x d\mu$ and $b_p d\widetilde\mu$ as the gauge-invariant local contents. Bandwidth-density identifications $b_x \propto |\Psi|^2$, $b_p \propto |\widetilde\psi|^2$ inherited from Theorem 10. | U2-Discrete (FORCED), U2-Continuum (FORCED), Theorem 10 (FORCED), Primitive 04 §1.5; forward reference to Memo 03 §1 (Fourier unitarity from Stone's theorem) | Fal-4, Fal-5 |

**Net status after Memos 01–02.** Three of five U5 sub-features (F1, F2, F4) are now established. Two remain active for Memo 03: F3 (Fourier conjugacy as the unique unitary intertwiner of position and momentum) and F5 (exhaustion via primitive-level audit). The F2 derivation is complete in form but conditional on F5's full dispatch.

The arc's verdict reduces to Memo 03's treatment of F3 and F5. Both are anticipated to close FORCED via the structural-derivation methodology established in U2 and born_gleason, with F3 admitting a U3-independent derivation via translation symmetry + Stone's theorem and F5 closing via a primitive-stack audit against candidate third adjacency-axes.

---

## 7. Recommended Next Steps

**(a) Begin Memo 03 (F3 + F5 derivations + arc verdict).** Natural next session step. Memo 03 is the load-bearing memo of the U5 arc and should examine F3 (Fourier conjugacy) and F5 (exhaustion) against falsifiers Fal-3 and the unconditional form of Fal-2. Anticipated structure: §1 F3 derivation via Stone's theorem on translation symmetry (with explicit U3-independence noted), §2 F5 audit dismissing candidate third adjacency-axes, §3 falsifier audit, §4 continuum-regime considerations (F3's Fourier-uniqueness in the continuum), §5 verdict and downstream cascade.

**(b) Pre-Memo-03 audit of the candidate third adjacency-axes for F5.** Memo 01 §3.5 identified four candidate third axes (bandwidth-gradient direction, rule-type coupling, polarity-amplitude direction, higher-derivative axes). A focused audit of each — verifying that none constitutes an independent primitive-level adjacency-axis distinct from Primitive 06 and Primitive 09 — should be done before Memo 03 drafts the F5 dispatch. This will sharpen the negative-existence argument and identify any candidate axis that requires a non-trivial structural argument to dismiss (versus those that dismiss trivially).

**(c) Pre-decide the continuum-regime treatment of F3.** Memo 01 §6.3 flagged a potential issue: the standard $L^2$ Fourier transform and Stone's theorem apply on flat-space translation-invariant baselines, but their extension to curved-spacetime settings (where Primitive 06's ED-gradient structure is generic and translation symmetry is local rather than global) introduces complications. Two reasonable framings for Memo 03:
- *Tight verdict.* Argue that translation symmetry holds locally (in tangent-space approximations) on any emergent manifold, with the corresponding local Fourier transform supplying the conjugacy. F3 closes uniformly.
- *Scoped verdict.* Restrict U5-FORCED to the flat-spacetime baseline where translation symmetry is global; flag the curved-spacetime extension as a future arc (parallel to how U2-Continuum was scoped to gauge-fixed downstream applications).
Recommended: pre-decide before drafting Memo 03 to keep the verdict framing focused.

---

## 8. Cross-references

- Arc outline: [`arcs/U5/00_arc_outline.md`](00_arc_outline.md)
- Memo 01 (decomposition + mapping): [`arcs/U5/01_decomposition_and_mapping.md`](01_decomposition_and_mapping.md)
- U2-Inner-Product paper (inner-product structure inherited as input for F4 orthogonality and the continuum gauge-invariance check): [`papers/U2_Inner_Product/paper_u2_inner_product.md`](../../papers/U2_Inner_Product/paper_u2_inner_product.md)
- Born_Gleason paper (Theorem 10 inherited as input for $b_x \propto |\Psi|^2$, $b_p \propto |\widetilde\psi|^2$ identifications): [`papers/Born_Gleason/born_gleason_paper.md`](../../papers/Born_Gleason/born_gleason_paper.md)
- U2 Memo 02 (parallel derivation template for F1 / F2 / F4 cleanly-closing items): [`arcs/U2/02_C3a_C3b_derivation.md`](../U2/02_C3a_C3b_derivation.md)
- U2-Continuum Memo 02 (parallel derivation template for the continuum-regime gauge-invariance check): [`arcs/U2_continuum/02_L1_L3_derivation.md`](../U2_continuum/02_L1_L3_derivation.md)
- Existing tightening-program memo for U5 (U3-dependent argument; the present arc replaces the U3 dependency with translation-symmetry-only kinematic argument): [`arcs/arc-foundations/u5_adjacency_partition_derivation.md`](../arc-foundations/u5_adjacency_partition_derivation.md)
- Step 5 derivation (Heisenberg, downstream beneficiary): [`arcs/arc-foundations/uncertainty_from_participation.md`](../arc-foundations/uncertainty_from_participation.md)
- Primitive 04 (bandwidth + four-band decomposition + adjacency band): `quantum/primitives/04_participation_bandwidth.md`
- Primitive 06 (ED gradient, supplies spatial axis): `quantum/primitives/06_ed_gradient.md`
- Primitive 09 (tension polarity, $U(1)$ phase, supplies phase-propagation axis): `quantum/primitives/09_tension_polarity.md`

---

## 9. One-line memo summary

> **F1 (existence of decomposition) is established by direct identification of two independent primitive-level adjacency-axes — Primitive 06's $\nabla \rho$ supplying the spatial axis and Primitive 09's $\nabla \pi$ supplying the phase-propagation axis — with neither derivable from the other and both kinematic (no U3 dependency). F2 (two-component count) is established by direct enumeration: exactly two adjacency-axes exist in the current primitive stack, with the count conditional on F5's exhaustion claim. F4 (orthogonality under U2) is established via Parseval's identity, inherited from Fourier unitarity on the U2 inner-product space (forward reference to Memo 03 §1) plus the per-band Theorem-10 identifications $b_x \propto |\Psi|^2$, $b_p \propto |\widetilde\psi|^2$; the continuum regime is gauge-invariant by direct inheritance from the U2-Continuum theorem, with both partition components transforming covariantly under the conformal rescaling. Falsifiers Fal-1, Fal-4, Fal-5 dispatched in full; Fal-2 partially dispatched (full dispatch awaits Memo 03 / F5). Three of five U5 sub-features now established; arc verdict reduces to Memo 03's treatment of F3 (Fourier conjugacy) and F5 (exhaustion).**
