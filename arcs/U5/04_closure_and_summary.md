# Memo 04 — U5 Arc Closure and Canonical Summary

**Date:** 2026-04-26
**Arc:** `arcs/U5/`
**Predecessors:** Memos [00](00_arc_outline.md), [01](01_decomposition_and_mapping.md), [02](02_derivations_F1_F2_F4.md), [03](03_F3_F5_and_verdict.md)
**Status:** Closure memo. Provides the canonical summary of the U5 arc and its public-facing explanation. Integrates the result into the QM-emergence program and prepares for the bundled memory-record update.
**Purpose:** Close the U5 arc with a single document that serves both as internal entry-point and as a self-contained external narrative.

---

## 1. Arc Summary in One Paragraph

The U5 arc asked whether the adjacency-band Fourier-conjugate partition $b^\mathrm{adj} = b_x + b_p$ — the structural backbone of Phase-1 Step 5's Heisenberg-uncertainty derivation — is forced by ED's primitive stack rather than postulated. Memo 01 decomposed U5 into five sub-features (F1 existence of decomposition, F2 two-component count, F3 Fourier conjugacy, F4 orthogonality under U2, F5 exhaustion) and mapped each to the relevant primitives, the participation-measure construction, the now-FORCED U2-Discrete and U2-Continuum theorems, and the now-FORCED Theorem 10 (Born). Three sub-features (F1, F2 conditional, F4) were classified forced-via-derivation with available structural inputs; two (F3, F5) were identified as load-bearing. Memo 02 closed F1, F2, and F4 via direct application of primitive-level inputs plus Parseval's identity inherited from Fourier unitarity on the U2 inner-product space, with the continuum-regime gauge-invariance verified explicitly. Memo 03 — the load-bearing memo — closed F3 by Stone's theorem applied to the translation group of the participation graph (Primitives 03 + 06 supplying translation symmetry as a kinematic input on the U2 Hilbert space), with explicit U3-independence and explicit dismissal of fractional-Fourier, wavelet, and Mellin alternatives; and closed F5 by primitive-level audit dismissing four candidate third adjacency-axes (bandwidth-gradient direction, rule-type coupling, polarity-amplitude direction, higher-derivative axes) plus a survey of the remaining nine primitives confirming no adjacency-relevant directional structure beyond Primitives 06 and 09. The arc closed FORCED with no new structural commitment introduced and with the explicit sharpening that the F3 derivation removes the U3 dependency that the earlier 2026-04-24 tightening-program memo carried. The downstream cascade is decisive: Heisenberg's uncertainty inequality $\Delta x \cdot \Delta p \geq \hbar/2$ promotes from forced-conditional-on-U5 to forced-unconditional in both discrete and continuum regimes, gauge-invariant under the U2-Continuum conformal redundancy. The active upstream-CANDIDATE inventory of the QM-emergence Phase-1 program reduces from {U1, U3, U4, U5} + gauge to **{U1, U3, U4} + gauge**.

---

## 2. The Arc's Structure, Narratively

**The question (Memo 00).** The QM-emergence Phase-1 program presented Heisenberg's uncertainty inequality conditional on a specific structural commitment: the adjacency band of Primitive 04's four-band decomposition splits into exactly two Fourier-conjugate orthogonal components — position-adjacency $b_x$ and momentum-adjacency $b_p$. This commitment, designated U5 in the QM-emergence Step-1 framework, was identified by the synthesis paper [§4.2] as "the cleanest" of the five upstream commitments. With U2 already promoted to FORCED via the prior arc cycle and Theorem 10 (Born) available as a theorem-grade input, U5 was the next-most-leveraged structural arc.

**The decomposition (Memo 01).** U5 packages five structurally distinct sub-claims — the existence of the decomposition (F1), the two-component count (F2), the Fourier conjugacy (F3), the orthogonality under U2 (F4), and the exhaustion of adjacency-axes (F5). Three of these (F1, F2 conditional, F4) had clear paths to closure via the available structural inputs; two (F3, F5) carried the substantive load of the arc. The decomposition foregrounded a sharpening opportunity: the earlier 2026-04-24 tightening-program memo for U5 derived F3 with explicit reference to U3 (the participation-measure evolution equation, itself an upstream commitment), but the present arc was positioned to derive F3 from translation symmetry as a *kinematic* property of the participation graph — without invoking U3 — by drawing on Stone's theorem applied to the U2 Hilbert space.

**The clean transfers (Memo 02).** F1 closed by direct identification of two structurally independent primitive-level adjacency-axes: Primitive 06's spatial axis $\nabla \rho$ and Primitive 09's phase-propagation axis $\nabla \pi$. Neither is reducible to the other; both are kinematic structural features of the participation graph that do not require dynamical evolution to define. F2 closed by direct enumeration: exactly two adjacency-axes are present in the current primitive stack. F4 closed via Parseval's identity on the U2 inner-product space, with the per-band Theorem-10 identifications $b_x \propto |\Psi(x)|^2$, $b_p \propto |\widetilde\psi(p)|^2$ supplying the bandwidth-density interpretations and the U2-Continuum gauge-invariance verified explicitly: under the conformal rescaling, both Parseval sides are inner-product values that the U2-Continuum theorem already guarantees gauge-invariant; both partition components $b_x \cdot d\mu$ and $b_p \cdot d\widetilde\mu$ are gauge-covariant in the same way.

**The load-bearing analysis (Memo 03).** F3's derivation produced the arc's most distinctive structural content. Translation symmetry on the participation graph is supplied by Primitives 03 (homogeneity of the participation relation) and 06 (admissibility of translations along the spatial axis) jointly — kinematic inputs not requiring dynamical evolution. Stone's theorem applies: the translation group has a unique self-adjoint generator $\hat{p}$ on the U2 Hilbert space. Plane waves are $\hat{p}$'s eigenfunctions; the standard Fourier transform is the unique unitary basis-change between position eigenstates and momentum eigenstates. Three classes of alternative conjugacies — fractional-Fourier transforms (which diagonalise *different* operator pairs), wavelet transforms (multi-scale resolutions, not Stone's-theorem intertwiners), and the Mellin transform (which intertwines dilations, not translations) — were each dismissed by structural inconsistency with the translation-symmetry-driven construction. F5's derivation closed via a primitive-level audit dismissing four candidate third adjacency-axes — bandwidth-gradient direction (refines within Primitive 06's spatial axis), rule-type coupling (lives in the environmental band of the four-band structure, not adjacency), polarity-amplitude direction (not supplied by any primitive; Primitive 09's polarity is purely $U(1)$-valued phase), higher-derivative axes (derivative quantities, not independent primitive-level commitments) — plus a survey of the remaining nine primitives confirming none supplies adjacency-relevant directional structure beyond Primitives 06 and 09.

**The verdict (Memo 03 §4).** FORCED. All five sub-features close with the available structural inputs; all five falsifiers dispatch; no new structural commitment is introduced; the derivation is independent of U3, sharpening the earlier tightening-program argument. The U2-Continuum gauge acts uniformly on both partition components, preserving the partition under conformal rescaling. Heisenberg's uncertainty inequality promotes to forced-unconditional in both regimes.

---

## 3. The U5 Theorem, Stated Cleanly

> **Theorem (U5; Adjacency-Band Fourier-Conjugate Partition).** Let $G = (V, E)$ be a participation graph with vertex set $V$ (Primitive 01) and edge set $E$ (Primitive 03), supplying translation symmetry as a kinematic feature. Let $b^\mathrm{adj}$ denote the adjacency-band component of the four-band bandwidth decomposition (Primitive 04 §1.5). Then $b^\mathrm{adj}$ admits a unique orthogonal decomposition
>
> $$
> b^\mathrm{adj}(x, t) = b_x(x, t) + b_p(p, t)
> $$
>
> with the following structural properties:
>
> 1. **Existence.** The decomposition exists because Primitive 06 supplies a spatial axis ($\nabla \rho$) and Primitive 09 supplies a phase-propagation axis ($\nabla \pi$), with the two axes structurally independent.
> 2. **Two-component count.** No third primitive-level adjacency-axis exists in the current primitive stack: bandwidth-gradient direction refines within the spatial axis, rule-type coupling lives in the environmental band, polarity-amplitude is not supplied by any primitive (polarity is $U(1)$-valued), higher-derivative axes are derivative quantities. The remaining nine primitives supply no adjacency-relevant directional structure.
> 3. **Fourier conjugacy.** The two components are connected by the standard $L^2$ Fourier transform, uniquely identified by Stone's theorem applied to the translation group of the participation graph on the U2 inner-product Hilbert space. No fractional-Fourier, wavelet, or Mellin alternative is admissible.
> 4. **Orthogonality under U2.** $b_x$ and $b_p$ are orthogonal projections of the participation-measure state, with Parseval's identity $\int |\Psi|^2 d\mu = \int |\widetilde\psi|^2 d\widetilde\mu = N_\mathrm{adj}$ supplying the orthogonal-decomposition relation. Bandwidth-density identifications $b_x \propto |\Psi|^2$, $b_p \propto |\widetilde\psi|^2$ inherited from Theorem 10 (Born).
> 5. **Continuum-regime gauge-invariance.** Under the U2-Continuum conformal gauge $(b_K, d\mu) \to (\Omega^{-D} b_K, \Omega^D d\mu)$, both partition components rescale uniformly and Parseval's identity is gauge-invariant. The partition is preserved.

**Status:** **FORCED.** No new structural commitment introduced. All inputs are already established or supplied by the primitive stack:
- Primitives 03, 04, 06, 09 (kinematic structure of the participation graph and its adjacency band).
- U2-Discrete and U2-Continuum theorems (sesquilinear inner product on the participation-measure space, in both regimes).
- Theorem 10 (Born rule via Gleason–Busch path; supplies bandwidth-density identifications).
- Stone's theorem (mathematical, applied to the translation group on the U2 Hilbert space).

**Scope:**
- *Discrete regime.* Forced unconditionally on the participation graph. Translation symmetry is global; Stone's theorem applies globally; standard Fourier transform supplies the conjugacy globally.
- *Continuum regime, flat-spacetime baseline.* Forced unconditionally. Translation symmetry is global; the gauge-invariance of the U2-Continuum theorem extends to the partition.
- *Continuum regime, curved-spacetime baseline.* Forced pointwise. Translation symmetry is local (in tangent-space approximations at each point); the local Fourier transform supplies the conjugacy at each point. Heisenberg's uncertainty is itself a local statement, so the local-Fourier construction is sufficient.

**Sharpening over earlier tightening-program work.** The 2026-04-24 tightening-program memo for U5 derived F3 (Fourier conjugacy) via U3 (the participation-measure evolution equation). The present derivation replaces this dependency: translation symmetry is a kinematic property of the participation graph (Primitives 03 + 06), not a dynamical property requiring U3. The U5 verdict is therefore independent of whatever conditionality U3 carries.

**Sensitivity flag.** The verdict is conditional on the current primitive stack. A future amendment supplying an additional adjacency-relevant directional structure would re-open F5. The verdict is as strong as the current adjacency-axis content of the primitives. (Structurally analogous to the U2 program's Primitive-09 $U(1)$ sensitivity flag.)

---

## 4. Integration of the Derivations

### 4.1 F1, F2, F4 from Memo 02

**F1 (existence of decomposition).** Primitive 06's spatial axis $\nabla \rho$ and Primitive 09's phase-propagation axis $\nabla \pi$ are two structurally independent primitive-level nearness specifications applicable to adjacency. Independence verified by limiting cases: a chain with uniform polarity phase still has spatial nearness, and a chain with uniform spatial bandwidth still has phase-propagation nearness. The adjacency band must therefore split into at least two orthogonal components.

**F2 (two-component count).** Direct enumeration of the primitive-level adjacency-axes yields exactly two. The count is conditional on F5 (exhaustion); given F5, the count is two unconditionally.

**F4 (orthogonality under U2).** Parseval's identity on the U2 inner-product space: $\int |\Psi(x)|^2 d\mu(x) = \int |\widetilde\psi(p)|^2 d\widetilde\mu(p) = N_\mathrm{adj}$. Both sides are U2 inner-product values supplying the orthogonal-decomposition relation. Bandwidth-density identifications $b_x \propto |\Psi|^2$, $b_p \propto |\widetilde\psi|^2$ inherited from Theorem 10. Continuum-regime gauge-invariance verified directly: both Parseval sides are gauge-invariant per the U2-Continuum theorem; the partition components transform as $b_x \cdot d\mu \to b_x \cdot d\mu$ and $b_p \cdot d\widetilde\mu \to b_p \cdot d\widetilde\mu$ (gauge-invariant local content), uniformly.

### 4.2 F3 and F5 from Memo 03

**F3 (Fourier conjugacy specificity).** The derivation has three parts:

- *Translation symmetry is kinematic, not dynamical.* Primitive 03 supplies homogeneity of the participation relation (no vertex privileged). Primitive 06 supplies admissibility of translations along the spatial axis. Together they establish translation symmetry as a primitive-level kinematic feature, with no U3 (dynamical) input required.
- *Stone's theorem identifies the translation generator uniquely.* The translation group $\{T_a : a \in \mathbb{R}^d\}$ is a strongly-continuous unitary group on the U2 Hilbert space (unitarity inherited from U2's gauge-covariant inner-product structure). Stone's theorem identifies the unique self-adjoint generator $\hat{p}$ such that $T_a = e^{i \hat{p} \cdot a / \hbar}$. Plane waves $\langle x \mid p \rangle = (2\pi\hbar)^{-d/2} e^{ipx/\hbar}$ are the eigenfunctions; the standard Fourier transform is the unique unitary basis-change.
- *Alternatives dismissed structurally.* Fractional-Fourier transforms diagonalise rotated phase-space operators, not the translation generator $\hat{p}$. Wavelet transforms are multi-scale resolutions, not Stone's-theorem intertwiners. Mellin transforms intertwine the dilation group, which is not a primitive-level kinematic symmetry of the participation graph.

The continuum-regime extension: translation symmetry is global on flat-spacetime baselines and local on curved-spacetime baselines; the local-Fourier construction at each point of the emergent manifold supplies the pointwise conjugacy, sufficient for Heisenberg's local statement.

**F5 (exhaustion / no third adjacency-axis).** Audit of four candidate third axes:

| Candidate | Dismissal reason |
|---|---|
| Bandwidth-gradient direction $\nabla b$ | Derived quantity (not primitive-level); refines within spatial axis already supplied by Primitive 06 |
| Rule-type coupling | Lives in environmental band, not adjacency band (four-band orthogonality of Primitive 04 §1.5) |
| Polarity-amplitude (distinct from polarity-phase) | Not supplied by Primitive 09 ($U(1)$-valued, purely phase); no separate amplitude variable |
| Higher-derivative axes ($\nabla^2 \rho$, $\nabla^2 \pi$, etc.) | Derivative quantities of existing primitives; refine within existing axes |

Plus a survey of the remaining nine primitives (01, 02, 05, 07, 08, 10, 11, 12, 13) confirming none supplies adjacency-relevant directional structure. **Adjacency-relevant content is concentrated in Primitives 06 and 09 only.**

### 4.3 The sharpening over the earlier tightening-program

The 2026-04-24 tightening-program memo `u5_adjacency_partition_derivation.md` derived F3 with explicit reference to U3 (the participation-measure evolution equation). The present arc replaces this dependency: translation symmetry is a kinematic property (Primitives 03 + 06), not a dynamical property (U3). The methodological consequence is that U5's verdict is now independent of U3's conditionality — promoting U3 in a future arc would not change the U5 result, and U5's promotion does not feed back into U3's derivation chain. This is structural decoupling, not just a cleaner argument: U5 stands on its own kinematic foundation.

---

## 5. Downstream Implications

### 5.1 Heisenberg uncertainty (Phase-1 Step 5)

**Pre-U5 status.** The Heisenberg uncertainty inequality $\Delta x \cdot \Delta p \geq \hbar/2$ was derived in Phase-1 Step 5 conditional on U2 and U5. With U2 forced (in both regimes per the U2 program) and U5 now forced (this arc), both conditionalities are resolved.

**Post-U5 status.** **Heisenberg promotes to FORCED-unconditional in both discrete and continuum regimes**, with all variances gauge-invariant under the U2-Continuum conformal redundancy. The bandwidth-allocation inequality $(\Delta b_x)(\Delta b_p) \geq K_{xp}$ derives from the partition (forced by F1–F5); the structural constant $K_{xp} = \hbar/2$ is fixed by the standard Fourier-uncertainty theorem applied to the U2 Hilbert space. Both pieces are now forced.

### 5.2 Updated upstream-CANDIDATE inventory

| Upstream commitment | Pre-U5 status | Post-U5 status |
|---|---|---|
| U1 (participation-measure construction) | Active CANDIDATE | (unchanged) Active CANDIDATE |
| U2 (sesquilinear inner product) | FORCED (via U2 program) | (unchanged) FORCED |
| U3 (participation-measure evolution equation) | Active CANDIDATE | (unchanged) Active CANDIDATE |
| U4 (momentum-basis identification) | Active CANDIDATE | (unchanged) Active CANDIDATE |
| U5 (adjacency-band Fourier-conjugate partition) | Active CANDIDATE | **FORCED (this arc)** |
| Continuum-lift conformal gauge | Description-level convention (via U2-Continuum) | (unchanged) Description-level convention |

The active upstream-CANDIDATE inventory reduces from **{U1, U3, U4, U5} + gauge** to **{U1, U3, U4} + gauge**. One additional foundational theorem (Heisenberg) joins Born and Bell–Tsirelson at fully-FORCED-unconditional status.

### 5.3 Downstream theorem-status table

| Theorem | Pre-U5 | Post-U5 |
|---|---|---|
| Born rule (Theorem 10) | FORCED-unconditional | (unchanged) |
| Bell–Tsirelson | FORCED-unconditional | (unchanged) |
| **Heisenberg uncertainty** | FORCED conditional on U5 | **FORCED-unconditional** in discrete + continuum (gauge-invariant) |

### 5.4 Position in the participation-measure → Hilbert-space → QM-emergence chain

The chain leading to Heisenberg's bound is now closed at theorem grade:

$$
\text{Primitives 03 + 04 + 06 + 09} \xrightarrow{\text{U1 (CANDIDATE)}} \text{participation measure}
$$
$$
\xrightarrow{\text{P-04 §1.5}} \text{four-band decomposition} \xrightarrow{\text{U2 (FORCED)}} \text{inner product}
$$
$$
\xrightarrow{\text{U5 (FORCED, this arc)}} \text{adjacency band split}
$$
$$
\xrightarrow{\text{Theorem 10 + Fourier-uncertainty}} \Delta x \cdot \Delta p \geq \hbar/2
$$

The structural backbone of Step 5 is complete. Heisenberg's bound is now a theorem-grade structural consequence of the primitive stack, conditional only on U1 (which is upstream of all participation-measure-based results) and the description-level continuum gauge.

### 5.5 No new gauge structure

U5 introduces no new gauge structure beyond what U2-Continuum already established. The partition $b^\mathrm{adj} = b_x + b_p$ is preserved under the conformal rescaling: both components transform uniformly. The Fourier conjugacy of F3 is preserved (translation symmetry is gauge-equivariant). The orthogonality of F4 is preserved (Parseval inherits gauge-invariance from U2-Continuum). The continuum gauge identified in U2-Continuum remains the only description-level redundancy.

---

## 6. Public-Facing Explainer

*This section is intended for a general scientific audience and is not part of the formal derivation.*

### 6.1 What Heisenberg's uncertainty principle is asking for

Heisenberg's uncertainty principle is one of the famous statements of quantum mechanics. It says: you cannot simultaneously know a particle's position and its momentum to arbitrary precision. The product of the two uncertainties has a floor — roughly Planck's constant divided by two.

The mathematical statement looks like this:

$$\Delta x \cdot \Delta p \geq \frac{\hbar}{2}$$

For a hundred years, this has been derived in standard quantum mechanics from a piece of mathematical machinery called the *Fourier-uncertainty theorem* — a statement about how localised a function in position-space can be while its Fourier transform stays equally localised in momentum-space. The deeper question — why position and momentum are *Fourier-conjugate* in the first place, and why there is exactly one pair of conjugate variables (rather than three, or seven, or some continuous family) — usually gets bundled into the Hilbert-space postulate of quantum mechanics. It is just *what quantum mechanics looks like*.

The Event Density framework wants to derive that piece too. If quantum mechanics is supposed to emerge from a deeper ontology — a participation graph with bandwidth on its edges and channels as primitive sub-structures — then the position-momentum conjugacy underlying Heisenberg's principle had better come out of the derivation, not be assumed alongside it.

### 6.2 Two kinds of "nearness"

Here is the picture the U5 result paints.

In the participation graph, every event has a *spatial position*. Two events are "nearby" if their positions are close. This is a familiar kind of nearness — it is what you would measure with a ruler.

But there is a second kind of nearness, less familiar but just as real. The participation measure has a *phase* — a number that lives on the unit circle, called the polarity phase in ED's vocabulary. As you move from one location to another, the phase advances. The rate at which it advances is called the *wavenumber*. Two events are nearby in the *phase-propagation* sense if they share the same wavenumber — if their polarity phases advance at the same rate as you move through them.

These two kinds of nearness are independent. A chain can have a sharp spatial position and a wide spread of wavenumbers (a localised lump of bandwidth, varying phase). Or it can have a uniform phase-propagation but a wide spatial extent (a plane wave). Or any mixture. The two axes — spatial nearness and phase-propagation nearness — neither contains the other.

That gives the adjacency band of the bandwidth structure exactly two structural axes. Not one. Not three. Two.

### 6.3 Why Fourier conjugacy is inevitable

Now the second piece. The two axes are not independent in their relationship to one another — they are linked by a specific mathematical operation. That operation is the standard Fourier transform.

Why? Consider what it would take to translate a quantum state by a small distance — to shift it spatially. There is a mathematical theorem, due to Marshall Stone in the 1930s, that says: any continuous family of unitary translations has a unique generator, and the eigenfunctions of that generator are plane waves. The basis-change between position eigenstates and the eigenstates of the translation generator is the Fourier transform.

There is no second choice here. The Fourier transform is the *unique* unitary intertwiner between position and momentum once the translation symmetry of the participation graph is in place. Other transforms — fractional-Fourier, wavelet, Mellin — solve different mathematical problems (rotated phase-space bases, multi-scale resolutions, dilation symmetry); they do not compete with the standard Fourier in this structural setting.

In ED's language: translation symmetry is a *kinematic* property of the participation graph. It does not require any dynamical assumption. The Fourier conjugacy of position and momentum is therefore a structural consequence of the graph itself plus Stone's theorem — not an extra postulate of quantum mechanics.

(A subtlety worth flagging: an earlier draft of this argument in the project's internal materials derived the Fourier conjugacy by way of the participation-measure *evolution* equation — invoking dynamics. The present derivation removes that dependency. Translation symmetry holds at a single time, on a static participation graph, without needing to know anything about how the graph evolves.)

### 6.4 Why no third axis exists

The third structural piece: there are exactly two axes, no more.

This is a *negative-existence* claim — there is no third primitive-level nearness axis applicable to adjacency. Establishing it requires an audit of the primitive stack to verify that no candidate third axis survives.

Four candidates were examined in the technical derivation. The gradient of the bandwidth itself does not supply a new nearness — it just refines within the spatial axis already given by the event-density gradient. Rule-type coupling (the structural difference between, say, an electron-channel and a photon-channel) lives in a different band of the four-band bandwidth structure (the environmental band, not the adjacency band). Polarity-amplitude does not exist at the primitive level — polarity is purely phase-valued, with no separate amplitude content. Higher derivatives of the existing fields are computed quantities, not separately-supplied primitive features.

Plus a survey of the remaining nine primitives in the ED stack confirmed that none supplies adjacency-relevant directional structure. The two axes — spatial and phase-propagation — exhaust the primitive-level content of "adjacency."

### 6.5 What this gives us

With the two axes forced (F1, F2, F5), the Fourier conjugacy forced (F3), and the orthogonality forced (F4), Heisenberg's uncertainty inequality follows from the standard Fourier-uncertainty theorem applied to the participation-measure wavefunction. The bound $\Delta x \cdot \Delta p \geq \hbar/2$ is now a structural consequence of the participation-graph ontology rather than a postulate of quantum mechanics.

The position-momentum conjugacy that Heisenberg used in 1927, that has appeared in every quantum-mechanics textbook ever published, that nobody really tried to derive because it was just *part of the framework* — has now been derived. Two structural axes, one Fourier transform connecting them, one bound that drops out of the Fourier-uncertainty mathematics. Quantum mechanics's most famous piece of "you can't know both at once" is what the participation graph looks like when you ask it about adjacency.

### 6.6 The honest framing

This result does not predict a new experiment. Heisenberg's bound is the same number it has always been. ED reproduces standard quantum mechanics exactly.

What changes is the answer to the question "why?" — specifically, why position and momentum, why Fourier-conjugate, why this particular bound. In standard quantum mechanics the answer is: "because we postulate it as part of the Hilbert-space formalism." In Event Density the answer is: "because the participation graph supplies two structurally independent adjacency-axes — spatial and phase-propagation — connected by the standard Fourier transform via Stone's theorem on the graph's translation symmetry, with no third axis surviving the primitive-level audit."

The framework still rests on its primitives. Whether they are right remains the load-bearing question. But the position-momentum conjugacy and the Heisenberg bound that depends on it are no longer separate postulates floating above the framework. They emerge from the kinematic structure of the participation graph plus the inner product established in the prior arcs.

---

## 7. Memo-to-Theorem Mapping

The U5 arc consisted of four memos (Memos 00–03) plus this closure memo. The mapping between memos, structural results, and theorem components is:

| Memo | Structural result | Theorem component |
|---|---|---|
| **Memo 00** (arc outline) | Decomposition into five sub-features (F1–F5); falsifier inventory; structural-input survey; comparison-to-U2 framing | Sets up the question and the analytical framework |
| **Memo 01** (decomposition + mapping) | Refined decomposition with primitive-level mapping; sub-feature classification (automatic / forced-via-derivation / load-bearing); falsifier-to-sub-feature attachment; sharpening opportunity over earlier tightening-program work flagged | Establishes the structural terrain for Memos 02 and 03 |
| **Memo 02** (F1, F2, F4 derivations) | F1 (existence, via P-06 + P-09 supplying two independent axes); F2 (two-component count, via direct enumeration, conditional on F5); F4 (orthogonality, via Parseval on U2 + Theorem-10 identifications); continuum-regime gauge-invariance check | Theorem properties 1, 2 (conditional), 4, 5 |
| **Memo 03** (F3, F5, verdict) | F3 (Fourier conjugacy, via translation symmetry + Stone's theorem + dismissal of fractional-Fourier / wavelet / Mellin alternatives, U3-independent); F5 (exhaustion, via primitive-level audit dismissing four candidate third axes + survey of remaining nine primitives); falsifier dispatch (Fal-2 unconditional, Fal-3); arc verdict | Theorem properties 2 (unconditional), 3, 6; verdict statement |
| **Memo 04** (this memo) | Canonical narrative summary; theorem statement; downstream cascade integration; public explainer; memo-to-theorem mapping | Final synthesis and outreach interface |

The structural content of each theorem property is supplied by the specific sub-feature derivation; the verdict aggregates them into the unified theorem statement.

---

## 8. Recommended Next Steps

**(a) Bundled memory-record update covering the U5 arc.** Following the discipline established in the U2 program, a single comprehensive update to `project_qm_emergence_arc.md` should capture the post-U5 state: (i) U5 theorem now FORCED, (ii) Heisenberg uncertainty promoted to forced-unconditional in both discrete and continuum regimes, (iii) updated active upstream-CANDIDATE inventory from {U1, U3, U4, U5} + gauge to {U1, U3, U4} + gauge, (iv) sensitivity flag for future primitive amendments supplying adjacency-relevant directional structure (analogous to the U2 program's Primitive-09 $U(1)$ sensitivity), (v) the methodological sharpening of removing U3 dependency from F3 — a structural-decoupling result that may inform future arcs targeting U3 itself. Update the `MEMORY.md` index line accordingly, with the arc-cycle theorem count moving from 12 to 13.

**(b) Decide priority for the next foundational arc: U1 vs. U3 + U4.** Three active CANDIDATEs remain. Two reasonable framings:
- *U1 first (highest leverage).* U1 — the participation-measure construction $P_K = \sqrt{b_K} \cdot e^{i\pi_K}$ — is the load-bearing primitive-level commitment from which all participation-measure-based results derive. Promoting U1 would make the entire QM-emergence Phase-1 program structurally complete in the participation-measure framework. The structural-derivation methodology established across four arcs (born_gleason, U2-Discrete, U2-Continuum, U5) is well-suited to U1's likely shape (decomposition into the magnitude-from-bandwidth and phase-from-polarity structural commitments, plus the complex-valued fusion).
- *U3 + U4 (Schrödinger-emergence specific).* U3 (the participation-measure evolution equation) and U4 (the momentum-basis identification $H_k = \hbar^2 k^2 / 2m$) are jointly responsible for Schrödinger emergence. They are structurally tighter than U1 but require additional Step-2 (Schrödinger-emergence) context. With U5 closed and the U3-independence of F3 established, U3 may be approachable with a sharpened structural-derivation argument that the earlier tightening-program memo could not access.

Recommended: **U1 first**. The leverage argument is decisive: U1 is upstream of every participation-measure-based result, and its derivation would make the Phase-1 structural-foundations program complete except for the dynamical-equation pair (U3 + U4) and the description-level continuum gauge.

**(c) Consider drafting the U5 publication paper.** The U5 result is publication-grade, parallel to the prior arc papers (Born_Gleason, U2_Inner_Product). A standalone paper would document the Fourier-conjugate partition derivation and the Heisenberg promotion in the format established by the prior papers (Markdown source → faithful LaTeX conversion → PDF). The paper would join the publishable papers folder as the third in the structural-foundations sequence. This is convention work, not derivation work, and can be deferred or scheduled per project-priority decisions.

---

## 9. Cross-references

**Within the U5 arc:**
- [`00_arc_outline.md`](00_arc_outline.md) — arc scoping and decomposition
- [`01_decomposition_and_mapping.md`](01_decomposition_and_mapping.md) — sub-feature classification + primitive mapping
- [`02_derivations_F1_F2_F4.md`](02_derivations_F1_F2_F4.md) — derivations of forced-via-derivation sub-features
- [`03_F3_F5_and_verdict.md`](03_F3_F5_and_verdict.md) — load-bearing derivations + arc verdict

**Predecessor arcs:**
- [`arcs/born_gleason/06_closure_and_summary.md`](../born_gleason/06_closure_and_summary.md) — Born rule arc closure (Theorem 10)
- [`arcs/U2/05_closure_and_summary.md`](../U2/05_closure_and_summary.md) — U2-Discrete arc closure
- [`arcs/U2_continuum/04_closure_and_summary.md`](../U2_continuum/04_closure_and_summary.md) — U2-Continuum arc closure

**Predecessor publication papers (templates for the U5 paper):**
- [`papers/Born_Gleason/born_gleason_paper.md`](../../papers/Born_Gleason/born_gleason_paper.md)
- [`papers/U2_Inner_Product/paper_u2_inner_product.md`](../../papers/U2_Inner_Product/paper_u2_inner_product.md)

**Earlier tightening-program work (superseded by the present arc; U3-independence sharpening):**
- [`arcs/arc-foundations/u5_adjacency_partition_derivation.md`](../arc-foundations/u5_adjacency_partition_derivation.md)

**Downstream beneficiary:**
- [`arcs/arc-foundations/uncertainty_from_participation.md`](../arc-foundations/uncertainty_from_participation.md) — Phase-1 Step 5 Heisenberg derivation, now FORCED-unconditional

**Source primitives:**
- Primitive 03 (Participation, supplies graph homogeneity for translation symmetry): `quantum/primitives/03_participation.md`
- Primitive 04 (bandwidth + four-band decomposition + adjacency band): `quantum/primitives/04_participation_bandwidth.md`
- Primitive 06 (ED gradient, supplies spatial axis + translation direction): `quantum/primitives/06_ed_gradient.md`
- Primitive 09 (tension polarity, $U(1)$ phase, supplies phase-propagation axis): `quantum/primitives/09_tension_polarity.md`

**Mathematical reference:**
- Stone's theorem: M. H. Stone, "On one-parameter unitary groups in Hilbert space," *Annals of Mathematics* **33**, 643–648 (1932).

**Project memory:**
- `memory/project_qm_emergence_arc.md`
- `memory/MEMORY.md`

**Public-facing companions (in same series; potential fourth public-explainer to draft):**
- `C:\Users\allen\Desktop\ED_Exponent2_Explainer.md` (overview)
- `C:\Users\allen\Desktop\ED_Born_Gleason_Explainer.md` (Born rule)
- `C:\Users\allen\Desktop\ED_U2_Inner_Product_Explainer.md` (inner product)
- *(Potential)* `ED_U5_Heisenberg_Explainer.md` (adjacency-partition / Heisenberg) — natural fourth in the sequence

---

## 10. One-line Memo Summary

> **U5 arc closed. The adjacency-band Fourier-conjugate partition $b^\mathrm{adj} = b_x + b_p$ is FORCED by the joint action of Primitives 03, 04, 06, 09, the now-FORCED U2 inner product (discrete + continuum), and Theorem 10 (Born), via Stone's theorem applied to the translation group of the participation graph on the U2 Hilbert space. Five sub-features established: F1 (existence) via two independent primitive-level adjacency-axes, F2 (two-component count) by direct enumeration conditional on F5, F3 (Fourier conjugacy) via Stone's theorem with explicit dismissal of fractional-Fourier / wavelet / Mellin alternatives — and explicit U3-independence sharpening the earlier tightening-program argument, F4 (orthogonality under U2) via Parseval inherited from Fourier unitarity on the U2 Hilbert space with continuum gauge-invariance verified, F5 (exhaustion) via primitive-level audit dismissing four candidate third axes plus survey of remaining nine primitives. All five falsifiers dispatched. No new structural commitment introduced. Heisenberg uncertainty promotes to FORCED-unconditional in both discrete and continuum regimes (gauge-invariant under the U2-Continuum conformal redundancy). Active upstream-CANDIDATE inventory reduces from {U1, U3, U4, U5} + gauge to {U1, U3, U4} + gauge. Four memos, one new theorem-grade structural result, one downstream theorem promoted to fully unconditional, methodological sharpening (U3 dependency removed); clean structural-foundations closure consistent with the methodology established in born_gleason + U2 program.**
