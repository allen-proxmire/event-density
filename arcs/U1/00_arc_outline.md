# U1 Arc — Examination Outline

**Date opened:** 2026-04-26
**Location:** `arcs/U1/`
**Goal:** Determine whether U1 — the participation-measure construction $P_K(x, t) = \sqrt{b_K(x, t)} \cdot e^{i \pi(K, x, t)}$ — is FORCED, CONDITIONAL, or NOT FORCED by ED's primitives. U1 is the most upstream of all upstream commitments in the QM-emergence Phase-1 program; promoting it would make the entire participation-measure framework structurally complete except for the dynamical-equation pair (U3, U4) and the description-level continuum gauge.
**Predecessor work:** None. The participation-measure construction has been adopted as a structural commitment in the QM-emergence framework since Phase-1's Step-1 memo [`arcs/arc-foundations/participation_measure.md`]; no prior arc has attempted to derive U1 from primitives. The synthesis paper [`papers/QM_Emergence_Structural_Completion/`] §4.1 lists U1 as the first of five upstream commitments and §4.2 ranks it as the most fundamental: "U1 alone generates most of the downstream structure; U2–U5 refine specific aspects."
**High-leverage status.** U1 is upstream of U2 (sesquilinear inner product), U3 (evolution equation), U4 (momentum-basis identification), U5 (adjacency partition), and Theorem 10 (Born). It is the load-bearing primitive-level commitment from which the entire participation-measure framework derives. Promoting U1 makes the entire QM-emergence Phase-1 program structurally complete except for U3 and U4 (Schrödinger-emergence specific) and the description-level continuum-lift gauge.

---

## 1. The U1 Question

### 1.1 Precise statement

The QM-emergence Phase-1 program adopts the participation-measure construction:

$$
P_K(x, t) = \sqrt{b_K(x, t)} \cdot e^{i \pi(K, x, t)} \qquad \text{(U1)}
$$

— a complex-valued field on (channel $K$, position $x$, time $t$), fusing Primitive 04 (bandwidth $b_K$, a non-negative real edge-weight on the participation graph) with Primitive 09 (tension polarity $\pi$, a $U(1)$-valued phase). The construction places $\sqrt{b_K}$ in the magnitude slot and $e^{i \pi}$ in the phase slot, with bandwidth $b_K = |P_K|^2$ recovered as the squared magnitude.

### 1.2 In the formal style of the QM-emergence upstream-commitment list

> **U1 (Participation-Measure Construction).** The natural complex-valued representation of the joint Primitive-04 + Primitive-09 structure is the polar-form fusion $P_K = \sqrt{b_K} \cdot e^{i \pi_K}$ — magnitude is the square root of bandwidth, phase is the polarity phase, with bandwidth recovered as the squared magnitude. The participation-measure space $\mathcal{P}$ supplies the structural carrier on which all downstream QM-emergence content (Schrödinger evolution, Born rule, Bell–Tsirelson correlations, Heisenberg uncertainty) lives. Affects: all downstream steps of the QM-emergence Phase-1 program.

### 1.3 Role in the participation-measure → Hilbert-space → QM-emergence chain

U1 is the *origin* of the chain:

$$
\text{Primitives 04 + 09} \xrightarrow{\text{U1 (this arc)}} \text{participation measure } P_K
$$
$$
\xrightarrow{\text{P-04 §1.5}} \text{four-band decomposition} \xrightarrow{\text{U2 (FORCED)}} \text{inner product on } \mathcal{P}
$$
$$
\xrightarrow{\text{Theorem 10 (FORCED)}} \text{Born rule}; \quad \xrightarrow{\text{U5 (FORCED)}} \text{adjacency partition} \xrightarrow{\text{Step 5}} \text{Heisenberg}
$$
$$
\xrightarrow{\text{Step 4}} \text{Bell–Tsirelson}; \quad \xrightarrow{\text{U3 (CANDIDATE) + U4 (CANDIDATE)}} \text{Schrödinger evolution}
$$

If U1 is forced, the *entire* downstream chain (Born, Bell, Heisenberg, U2, U5) becomes forced unconditionally — except for Schrödinger evolution (which inherits U3 + U4) and the description-level continuum gauge.

This is the highest-leverage arc remaining in the QM-emergence Phase-1 program.

---

## 2. Decomposition into Sub-Features

U1 packages four structurally distinct sub-claims, each requiring independent structural status determination.

### 2.1 The four sub-features

- **(F1) Complex-valued range.** $P_K$ takes values in $\mathbb{C}$, not in $\mathbb{R}$, $\mathbb{H}$ (quaternions), or some other algebra. The participation-measure space is a *complex* vector space.

- **(F2) Polar decomposition structure.** Once $P_K$ is $\mathbb{C}$-valued, the structural form $P_K = |P_K| \cdot e^{i \arg P_K}$ is the universal polar decomposition for complex numbers. F2 asserts that this decomposition is the natural representation of the participation-measure content, with the magnitude and phase slots filled by primitive-level quantities.

- **(F3) Magnitude exponent: $|P_K|^2 = b_K$.** The magnitude is specifically $\sqrt{b_K}$, i.e., the squared magnitude equals bandwidth: $b_K = |P_K|^2$. This is the "Exponent-2" structural commitment — the foundation of the Exponent-2 Thread that runs through Born, Schrödinger, Madelung, Heisenberg.

- **(F4) Phase = polarity.** The phase factor in U1's construction is *exactly* Primitive 09's polarity phase $\pi(K, x, t)$, with no additional phase variable, no rescaling, no functional transformation. The phase slot of the polar decomposition is filled by polarity directly.

### 2.2 Anticipated structural status

| Sub-feature | Anticipated status | Reasoning |
|---|---|---|
| **F1** Complex-valued range | **load-bearing** | The choice of $\mathbb{C}$ over $\mathbb{R}$ or $\mathbb{H}$ requires a structural argument for the necessity of complex (rather than real or quaternionic) algebraic structure. Quaternionic QM is a known alternative formulation in the foundations literature; ruling it out structurally is non-trivial. |
| **F2** Polar decomposition | automatic given F1 | Polar decomposition is universal for complex numbers ($z = |z| e^{i \arg z}$); no new structural commitment beyond F1. |
| **F3** Magnitude exponent $\|P_K\|^2 = b_K$ | **load-bearing** | The famous "why squared?" question. The exponent 2 underlies the entire Exponent-2 Thread (Born, Schrödinger, Madelung, Heisenberg). Forcing α=2 versus α=1, α=3, or other exponents requires a substantive structural argument. |
| **F4** Phase = polarity | forced-via-derivation | Primitive 09 supplies a $U(1)$-valued phase directly; it is the unique primitive-level angular variable available to the construction. The "fill the phase slot with polarity" identification is the natural and only structurally-supported choice. |

The arc has two load-bearing items (F1 and F3), both structurally substantive. F2 is automatic; F4 closes via a clean uniqueness argument.

### 2.3 Discrete vs continuum regime split

The U1 construction itself is regime-independent: the participation-measure expression $P_K(x, t) = \sqrt{b_K(x, t)} \cdot e^{i \pi(K, x, t)}$ is the same in both regimes, with $x$ ranging over the discrete vertex set $V$ in the discrete regime or the continuum manifold $M$ in the continuum regime. The F1, F2, F3, F4 sub-features are likewise regime-independent at the level of their structural content.

A discrete-vs-continuum split *could* arise if the continuum-regime construction required additional structure (e.g., regularity conditions on $b_K(x)$ as a smooth field), but this is anticipated to be a technical refinement rather than a substantive structural distinction.

The U2-Continuum gauge applies to U1's downstream consequences but does not affect U1 itself: under the conformal rescaling $(b_K, d\mu) \to (\Omega^{-D} b_K, \Omega^D d\mu)$, the participation measure transforms as $P_K \to \Omega^{-D/2} P_K$, but the *form* of the U1 construction (polar decomposition with $|P|^2 = b$) is preserved. U1 is gauge-compatible by inheritance.

---

## 3. Structural Inputs

The U1 arc operates with the leanest structural inputs of any arc to date. U1 is upstream of every downstream item in the QM-emergence program; it cannot use any of those items as inputs without circularity.

### 3.1 Primitives drawn upon

- **Primitive 04 (Bandwidth):** supplies the non-negative real scalar $b_K(x, t) \geq 0$, with bandwidth additivity over disjoint channel-subsets (four-band orthogonality of §1.5). Provides the magnitude content.
- **Primitive 09 (Tension Polarity):** supplies the $U(1)$-valued phase $\pi(K, x, t) \in [0, 2\pi)$. Primitive 09 §1.16 establishes polarity as phase-valued ("not a binary in general — it is a phase in the full treatment"), and §1.30 confirms its $U(1)$ character ("not a scalar"). Provides the phase content.
- **Primitive 03 (Participation):** supplies the relational structure on which $P_K$ is defined; the participation graph supplies the index set $V$ for positions and the adjacency relations.
- **Primitive 07 (Channel):** supplies the channel index set $\mathcal{K}$. Channels are primitive ontological sub-structures of the participation graph.

### 3.2 Inputs *not* available (would be circular)

The following items depend on U1 (use the participation measure as a constructed object) and therefore cannot be used as inputs to U1's derivation without circularity:

- U2 (sesquilinear inner product on $\mathcal{P}$) — uses $P_K$ as input.
- Theorem 10 (Born rule via Gleason–Busch) — uses $b = |P|^2$ identification, which is U1c.
- U3 (participation-measure evolution equation) — uses $P_K$ as input.
- U4 (momentum-basis identification) — uses $P_K$ as input.
- U5 (adjacency-band partition) — uses $b_x \propto |\Psi|^2$ from Born, ultimately depending on U1.
- Bell–Tsirelson, Heisenberg uncertainty — derived from $P_K$.

This is the leanest structural environment of any arc to date. **The U1 derivation must close from primitives + mathematical / algebraic constructions alone.**

### 3.3 Mathematical / algebraic constructions

The arc may draw on standard mathematical results that do not depend on the participation-measure construction:

- **Frobenius theorem (Frobenius 1878).** The only finite-dimensional associative real division algebras are $\mathbb{R}$, $\mathbb{C}$, $\mathbb{H}$. Used in F1 to enumerate algebraic-structure alternatives.
- **Polar decomposition for complex numbers.** $z = |z| \cdot e^{i \arg z}$. Used in F2.
- **Quadratic-form theory.** Classification of quadratic forms on complex vector spaces; relevant for F3.
- **$U(1)$ representation theory.** Phase factors $e^{i\theta}$ as elements of the unit circle; used in F4.

These are mathematical facts independent of ED's structural commitments. They function as enabling infrastructure rather than load-bearing inputs.

---

## 4. Falsifiers

The arc is **closed FORCED** if all four sub-features (F1–F4) close uniquely.

The arc is **closed CONDITIONAL** if F2, F4 close uniquely but F1 or F3 admits a non-pathological alternative consistent with the primitive structure.

The arc is **closed NOT FORCED** if any sub-feature admits a *physically distinct* alternative producing a different downstream phenomenology than standard QM (specifically, a different Hilbert-space structure, a different Born exponent, or a different uncertainty pattern).

### 4.1 Specific falsifiers

- **(Fal-1) Real-valued participation measure.** Attaches to **F1**. If the primitive structure admits a real-valued representation $P_K^\mathrm{real}$ with phase content separately encoded (e.g., via a separate $\mathbb{Z}_2$ or $\mathrm{SO}(2)$ structure), F1 fails. Real QM is a known formal alternative (real-valued wavefunctions exist mathematically but lose the standard interference structure); ruling it out requires showing that primitive-level interference and superposition structure require complex amplitudes.
- **(Fal-2) Quaternionic-valued participation measure.** Attaches to **F1**. Quaternionic QM is a known alternative formulation in the foundations literature (Adler 1995, Stueckelberg 1960). If the primitive structure admits a quaternionic representation $P_K^\mathbb{H}$ — perhaps motivated by a richer polarity structure than $U(1)$ — F1 fails. Ruling it out requires showing that Primitive 09's $U(1)$-valued polarity uniquely supports complex (not quaternionic) phase content.
- **(Fal-3) Different magnitude exponent.** Attaches to **F3**. If the primitive structure admits a representation with $|P_K|^\alpha = b_K$ for $\alpha \neq 2$ — e.g., $\alpha = 1$ giving linear-amplitude bandwidth, $\alpha = 4$ giving quartic bandwidth — F3 fails. The resulting downstream Born expression would have a different exponent, violating the empirically-observed $|\psi|^2$ rule. Ruling out alternative exponents requires a structural argument *not* downstream of Born or of any participation-measure-dependent result.
- **(Fal-4) Phase distinct from polarity.** Attaches to **F4**. If the primitive stack supplies a phase variable distinct from polarity that could fill the $e^{i \cdot}$ slot — e.g., a $U(1)$ subgroup of a wider symmetry group, or an additional primitive-level angular variable — F4 fails. The phase slot would carry an additional structural commitment beyond polarity.
- **(Fal-5) Non-multiplicative fusion.** Attaches to the joint structure F1 + F2. If the natural fusion of bandwidth and polarity is not the multiplicative product $\sqrt{b} \cdot e^{i \pi}$ but some other operation — e.g., additive $\sqrt{b} + e^{i \pi}$ (dimensionally incoherent but structurally conceivable), or a tensor-product fusion in a higher-dimensional algebra — F1+F2 fail jointly. Ruling this out requires showing that the polar-decomposition multiplicative form is the unique structurally-coherent fusion.

### 4.2 Falsifier-to-sub-feature attachment

| Falsifier | Sub-feature | Anticipated status |
|---|---|---|
| Fal-1 (real-valued) | F1 | Dispatched via interference / superposition argument requiring complex algebra |
| Fal-2 (quaternionic) | F1 | Dispatched via Primitive 09 $U(1)$-only structure |
| Fal-3 (different exponent) | F3 | **Load-bearing**; requires substantive structural argument |
| Fal-4 (phase ≠ polarity) | F4 | Dispatched via uniqueness of primitive-level phase variable |
| Fal-5 (non-multiplicative fusion) | F1 + F2 | Dispatched via polar-decomposition universality |

### 4.3 Discrete-regime versus continuum-regime falsifier attachment

Both regimes attach the same falsifiers. U1's construction is regime-independent at the level of its structural content; the falsifiers apply uniformly.

---

## 5. Memo Plan

### Memo 01: `01_decomposition_and_mapping.md`

Decompose U1 into sub-features F1–F4. For each, identify which primitive(s) and which mathematical / algebraic constructions supply the structural inputs. Classify each as automatic / forced-via-derivation / load-bearing. Inventory parallels U2 Memo 01 and U5 Memo 01 templates, with the difference that U1 has *no* prior FORCED items available as inputs (only primitives + mathematical infrastructure).

**Anticipated structure:**
- §1: U1 statement and role
- §2: Four sub-features with primitive mapping
- §3: Inputs *not* available (circularity check)
- §4: Mathematical infrastructure (Frobenius, polar decomposition, etc.)
- §5: Falsifier attachment
- §6: Comparison to U2 / U5 / born_gleason structural shape
- §7: Recommended Next Steps

### Memo 02: `02_F2_F4_derivations.md`

Derive the cleaner sub-features: F2 (polar decomposition, automatic given F1) and F4 (phase = polarity, forced-via-derivation via uniqueness of primitive-level phase variable). Establish that no additional structural commitment is required for these sub-features beyond what the primitive stack already supplies.

**Anticipated structure:**
- §1: F2 derivation (polar decomposition universality)
- §2: F4 derivation (phase = polarity uniqueness)
- §3: Joint status
- §4: Load-bearing items deferred to Memo 03

### Memo 03: `03_F1_F3_and_verdict.md`

The load-bearing memo. Examines F1 (complex-valued range, against real and quaternionic alternatives) and F3 (magnitude exponent $|P|^2 = b$, against alternative exponents). Anticipated leading arguments:

- **F1.** Complex-valued range is forced by (i) Primitive 09's $U(1)$-valued polarity (uniquely supports a complex phase factor; quaternionic phase would require an $S^3$-valued polarity, not supplied by Primitive 09); (ii) primitive-level interference structure requiring superposition with phase content (real-valued amplitudes lose the imaginary-part content needed for interference); (iii) Frobenius theorem restricting algebraic alternatives to $\mathbb{R}$, $\mathbb{C}$, $\mathbb{H}$, with $\mathbb{R}$ ruled out by interference and $\mathbb{H}$ ruled out by Primitive 09's $U(1)$ structure.

- **F3.** Magnitude exponent $|P|^2 = b$ is forced by (i) the requirement that bandwidth be a *quadratic form* on the participation-measure space (forced by bandwidth additivity over disjoint channel-subsets, which makes bandwidth a positive-definite quadratic form on $\mathcal{P}$ once $\mathcal{P}$ is C-valued); (ii) the fact that on $\mathbb{C}$, the unique $U(1)$-invariant positive-definite quadratic form (up to scale) is $|z|^2$; (iii) consistency with the sublinear bandwidth-composition rule (forced by Primitive 04's structural composition).

**Anticipated structure:**
- §1: F1 derivation (complex-valued range; real and quaternionic alternatives dismissed)
- §2: F3 derivation (magnitude exponent $|P|^2 = b$; alternative exponents dismissed)
- §3: Falsifier audit
- §4: Verdict
- §5: Downstream cascade (multiple downstream items promoted to *fully unconditional*)

### Memo 04: `04_closure_and_summary.md` *(optional but recommended)*

Closure memo with canonical narrative, integration into the QM-emergence program, and public-facing explainer. Parallels U2-Discrete Memo 05, U2-Continuum Memo 04, born_gleason Memo 06, U5 Memo 04.

---

## 6. Comparison to Prior Arcs

### 6.1 Methodological similarities

| Methodological element | born_gleason | U2 (Discrete + Continuum) | U5 | U1 (anticipated) |
|---|---|---|---|---|
| Decomposition into sub-features | 8 Gleason assumptions | 3 (C3a, C3b, C3c) | 5 (F1–F5) | 4 (F1–F4) |
| Automatic items | 5 of 8 | 1 (C3a) | 0 | 1 (F2) |
| Forced-via-derivation items | 1 inherited (A1 ↔ U2) | 1 (C3b) + 3 (C3c sub-features) | 3 (F1, F2 conditional, F4) | 1 (F4) |
| Load-bearing items | 2 (A4 + A8 = same question) | 1 cluster (C3c) | 2 (F3, F5) | 2 (F1, F3) |
| Methodological pattern | decompose → load-bearing → primitive arguments | same | same | same |
| New CANDIDATEs introduced | 0 | 0 | 0 | anticipated 0 |
| Inherited prior FORCED items | none (started the cycle) | none initially; both U2 results closed in arc | U2 + Theorem 10 + four-band ortho | **none — primitives only** |

### 6.2 Structural differences

**U1 has the leanest structural inputs of any arc.** Born_gleason inherited Gleason's mathematical theorem; U2 inherited U2-discrete results within its own arc; U5 inherited U2 + Theorem 10. U1 has only the primitives directly, plus standard mathematical constructions. This leanness is structurally honest — U1 is *the most upstream* commitment, so it must derive from the primitive stack alone.

**U1 has two genuinely substantive load-bearing items.** Compare:
- U2's load was C3c with three sub-features, but the sub-features were structurally homogeneous (each closed by the same diagonal-equals-bandwidth + non-negative-weighting argument structure).
- U5's two load-bearing items were F3 (positive structural construction via Stone's theorem) and F5 (negative-existence audit). One positive, one negative.
- U1's two load-bearing items are F1 (algebraic-structure question: real vs complex vs quaternion) and F3 (exponent question: $|P|^2 = b$). Both are genuinely structural, both connect to deep questions in the foundations of quantum mechanics, and both have known literature alternatives (real QM, quaternionic QM, alternative-exponent generalizations) that must be explicitly dismissed.

**U1's downstream leverage is the largest.** Born_gleason promoted the Born rule. U2 promoted Born + Bell + Heisenberg conditional on U2 itself, and U2-Continuum extended this. U5 promoted Heisenberg (the third foundational theorem). **U1 promotes everything at once.** If U1 is forced, the entire participation-measure framework — and every downstream theorem — becomes structurally complete except for U3, U4, and the description-level continuum gauge.

### 6.3 Whether U1 is cleaner or more delicate

**Anticipated: more delicate.** Synthesis paper §4.2 ranks U1 as the most fundamental commitment but does *not* rank it as cleanest. The cleanest is U5 (already done). U1's load-bearing items (F1 and F3) connect to genuinely deep foundational questions:

- **F1 risk.** Quaternionic QM is a real research program with substantial mathematical infrastructure; ruling out a quaternionic-valued participation measure structurally requires a rigorous argument from Primitive 09's $U(1)$-only polarity structure plus the Frobenius classification of real division algebras. The argument is anticipated to close, but it is *non-trivial*.

- **F3 risk.** The magnitude-exponent question is the deepest structural question in the QM-emergence program. The exponent-2 commitment underlies the Born rule, the Madelung form, the Schrödinger kinetic term, and Heisenberg's bound. Forcing α=2 versus alternative α requires showing that bandwidth is a quadratic form on $\mathcal{P}$ — which in turn requires bandwidth additivity on the participation-measure-space-as-vector-space. The argument is anticipated to close via Primitive 04's bandwidth additivity structure (four-band orthogonality + within-band additivity), but the argument's correctness depends on bandwidth additivity being genuinely a primitive-level fact and not a downstream consequence.

**Methodology robust, content delicate.** The structural-derivation methodology established across four prior arcs (born_gleason, U2-Discrete, U2-Continuum, U5) applies directly. The substantive content of F1 and F3 is more delicate than prior arcs' content. The arc may need 4 memos (rather than 3) plus the optional closure memo, with F1 and F3 each receiving its own dedicated memo.

### 6.4 Overall assessment

U1 is anticipated to close FORCED, with the methodological pattern established in prior arcs applying directly. The substantive content is more delicate than prior arcs because U1's load-bearing items connect to deep foundational questions (real-vs-complex-vs-quaternion algebra; $|P|^2 = b$ exponent) with known literature alternatives. The arc is expected to be 4 memos plus an optional closure memo (5 total), longer than U5's 4 memos but shorter than U2's combined 9 memos.

The downstream cascade is the largest of any arc: if U1 is forced, the entire participation-measure framework becomes structurally complete except for U3 + U4 (Schrödinger evolution) and the continuum gauge.

---

## 7. Recommended Next Steps

**(a) Begin Memo 01 (decomposition + primitive mapping).** Natural next session step. Following the templates of U2 Memo 01 and U5 Memo 01, Memo 01 should produce a tight inventory of the four sub-features with explicit primitive correspondents, status classifications, and circularity-check (which inputs are *not* available because they depend on U1). Expected outcome: a structural map ready for Memos 02 and 03 (and possibly Memo 04 if F1 and F3 each warrant their own memo).

**(b) Pre-Memo-01 audit of the Step-1 participation-measure memo.** The existing `arcs/arc-foundations/participation_measure.md` memo from the QM-emergence Phase-1 program supplies the original construction of U1 with nine structural constraints (C1–C9) and the surrounding context. A focused read of this memo before drafting Memo 01 will identify (i) which structural arguments for U1's sub-features already exist and can be sharpened, (ii) which constraints (C1–C9) correspond to F1–F4 directly, and (iii) any prior arguments worth replacing under the present arc's tighter primitive-only methodology.

**(c) Pre-decide whether F1 and F3 receive separate memos or share Memo 03.** Two reasonable framings:
- *Single load-bearing memo.* Memo 03 covers both F1 and F3, with §1 on F1 and §2 on F3. Suitable if the arguments are similar in length to U5 Memo 03's F3 + F5 treatment.
- *Two load-bearing memos.* Memo 03 covers F1 (algebraic-structure question), Memo 04 covers F3 (magnitude-exponent question), with the closure-and-summary memo becoming Memo 05. Suitable if either F1 or F3 requires substantial dedicated treatment.

The single-memo framing is recommended unless Memo 02 reveals that one of F1 or F3 has more structural content than anticipated. Decide before drafting Memo 03.

---

## 8. Cross-references

**Companion arcs (predecessors, sets the methodological pattern):**
- [`arcs/born_gleason/`](../born_gleason/) — Born rule via Gleason–Busch (Theorem 10)
- [`arcs/U2/`](../U2/) — U2-Discrete (sesquilinear inner product on participation graph)
- [`arcs/U2_continuum/`](../U2_continuum/) — U2-Continuum (continuum lift with conformal gauge)
- [`arcs/U5/`](../U5/) — U5 (adjacency-band Fourier-conjugate partition)

**Step-1 participation-measure memo** (pre-arc context to audit):
- [`arcs/arc-foundations/participation_measure.md`](../arc-foundations/participation_measure.md)

**Synthesis paper (upstream-commitment inventory; U1 listed in §4.1):**
- [`papers/QM_Emergence_Structural_Completion/QM_Emergence_Structural_Completion.md`](../../papers/QM_Emergence_Structural_Completion/QM_Emergence_Structural_Completion.md)

**Source primitives:**
- Primitive 03 (Participation, supplies relational structure on which $P_K$ is defined): `quantum/primitives/03_participation.md`
- Primitive 04 (Bandwidth, supplies non-negative real magnitude content): `quantum/primitives/04_participation_bandwidth.md`
- Primitive 07 (Channel, supplies channel index set $\mathcal{K}$): `quantum/primitives/07_channel.md`
- Primitive 09 (Tension Polarity, supplies $U(1)$-valued phase): `quantum/primitives/09_tension_polarity.md`

**Foundations-of-QM literature relevant to F1 and F3:**
- S. L. Adler, *Quaternionic Quantum Mechanics and Quantum Fields* (Oxford, 1995). Quaternionic-QM literature relevant for Fal-2 dispatch in Memo 03.
- E. C. G. Stueckelberg, *Quantum theory in real Hilbert space* (Helv. Phys. Acta 33, 727, 1960). Real-QM literature relevant for Fal-1 dispatch.
- F. G. Frobenius, *Über lineare Substitutionen und bilineare Formen*, J. Reine Angew. Math. 84, 1–63 (1878). Frobenius theorem on real division algebras.

**Project memory:** `memory/project_qm_emergence_arc.md`

---

## 9. One-line arc summary

> **Test whether U1 — the participation-measure construction $P_K = \sqrt{b_K} \cdot e^{i \pi_K}$ — is FORCED by Primitives 04 + 09 + supporting primitive structure + standard mathematical / algebraic constructions, with no inherited FORCED items available (U1 is the most upstream commitment). Four sub-features: F1 complex-valued range (load-bearing — real and quaternionic alternatives must be ruled out), F2 polar decomposition (automatic given F1), F3 magnitude exponent $|P|^2 = b$ (load-bearing — the foundational "why squared?" question; alternative exponents must be ruled out), F4 phase = polarity (forced-via-derivation via uniqueness of primitive-level phase). If FORCED, the entire participation-measure framework becomes structurally complete except for U3, U4, and the continuum gauge — every other downstream theorem promoted to fully unconditional. Anticipated more delicate than prior arcs (real / quaternionic / alternative-exponent literature alternatives have known mathematical infrastructure) but methodologically tractable via the structural-derivation pattern established in four prior arcs. Four-memo plan plus optional closure; possible expansion to five memos if F1 or F3 warrants dedicated treatment.**
