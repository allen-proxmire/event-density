# Memo 02 — Derivations of F2 (Polar Decomposition) and F4 (Phase = Polarity)

**Date:** 2026-04-26
**Arc:** `arcs/U1/`
**Predecessors:** [`00_arc_outline.md`](00_arc_outline.md), [`01_decomposition_and_mapping.md`](01_decomposition_and_mapping.md)
**Status:** Derivation memo. Closes the two non-load-bearing sub-features of U1: F2 (polar decomposition structure, automatic given F1) and F4 (phase = polarity, forced-via-derivation by primitive enumeration). Uses only primitive-level inputs and standard mathematical infrastructure, with no downstream dependencies.
**Purpose:** Settle F2 and F4 so Memo 03 can focus entirely on the load-bearing F1 (complex-valued range) and F3 (magnitude exponent) questions.

---

## 1. The Two Sub-Features

From Memo 01 §2.1, the two sub-features handled in this memo are:

- **(F2) Polar decomposition structure.** Given a complex-valued carrier (F1, anticipated forced; load-bearing argument deferred to Memo 03), the participation measure admits a polar decomposition $P_K(x, t) = r_K(x, t) \cdot e^{i \theta_K(x, t)}$ with magnitude $r_K \in \mathbb{R}_{\geq 0}$ and phase $\theta_K \in U(1)$. The decomposition is the unique natural representation of the participation-measure content as the product of magnitude and phase.

- **(F4) Phase = polarity.** The phase $\theta_K$ in F2's polar decomposition is exactly Primitive 09's polarity phase $\pi(K, x, t)$, with no additional phase variable, no rescaling, no functional transformation. Primitive 09 is the unique primitive-level $U(1)$-valued angular variable in the ED stack; no alternative source exists.

Both derivations are *conditional on F1* in the framing sense — they assume the participation-measure carrier is $\mathbb{C}$-valued, which F1 will establish in Memo 03. Conditional-on-F1 closure is sufficient for the structural inventory; the unconditional verdict follows automatically when F1 closes.

---

## 2. Derivation of F2 — Polar Decomposition

### 2.1 The claim

Given F1 (the participation measure $P_K(x, t) \in \mathbb{C}$), the polar form

$$
P_K(x, t) = r_K(x, t) \cdot e^{i \theta_K(x, t)} \qquad (1)
$$

with $r_K(x, t) \in \mathbb{R}_{\geq 0}$ and $\theta_K(x, t) \in [0, 2\pi)$ is the natural representation of the participation-measure content. The decomposition exists for every $(K, x, t)$ slot, is unique up to a global $U(1)$ ambiguity (the choice of branch for $\arg P_K$), and introduces no new structural commitment beyond F1.

### 2.2 Mathematical content

The polar decomposition for complex numbers is a standard mathematical fact:

> **Polar decomposition for $\mathbb{C}$.** Every nonzero $z \in \mathbb{C}$ admits a unique representation $z = |z| \cdot e^{i \arg z}$ with $|z| \in \mathbb{R}_{> 0}$ and $\arg z \in [0, 2\pi)$. For $z = 0$, the magnitude is $0$ and the phase is undefined (or conventionally taken as $0$).

This is universal mathematical structure for $\mathbb{C}$, not an ED-specific commitment. Any complex-valued field — whether the participation measure or any other $\mathbb{C}$-valued object — admits this decomposition pointwise.

### 2.3 Application to the participation-measure field

For $P_K(x, t) \in \mathbb{C}$ at each $(K, x, t)$ slot, define:

$$
r_K(x, t) := |P_K(x, t)|, \qquad \theta_K(x, t) := \arg P_K(x, t)
$$

with the convention $\theta_K = 0$ on the zero set $\{(K, x, t) : P_K(x, t) = 0\}$. The pair $(r_K, \theta_K)$ is well-defined as a complex-valued-function decomposition into a non-negative real magnitude field and a $U(1)$-valued phase field.

By construction, equation (1) holds pointwise.

### 2.4 Uniqueness up to global $U(1)$

The polar decomposition is unique once a branch of $\arg$ is chosen — typically $[0, 2\pi)$ or $(-\pi, \pi]$. A different branch shifts $\theta_K$ by a constant; equivalently, a global phase rotation $\theta_K \to \theta_K + \alpha$ is admissible without changing any structural content. This is the standard $U(1)$ gauge freedom inherent in any complex-valued field representation.

This global $U(1)$ ambiguity is *not* an ED-internal structural commitment — it is the same gauge freedom that appears in every complex-valued representation in physics. It does not constitute a new structural commitment of F2 beyond what F1 already established by placing $P_K$ in $\mathbb{C}$.

### 2.5 No new structural commitment

F2's content is exhausted by the polar decomposition's mathematical universality plus F1's commitment to $\mathbb{C}$-valued range. No primitive is invoked beyond what F1 invokes; no mathematical machinery is invoked beyond the polar decomposition theorem; no downstream item is invoked.

In particular:
- F2 does *not* commit to any specific functional form for $r_K$ (that is F3's content: $r_K = \sqrt{b_K}$).
- F2 does *not* commit to any specific functional form for $\theta_K$ (that is F4's content: $\theta_K = \pi_K$).
- F2 only commits to *the existence of the decomposition* — that any complex-valued $P_K$ can be written as magnitude × phase.

### 2.6 Verdict for F2

**Established (conditional on F1).** Given F1's commitment to $\mathbb{C}$-valued participation measure, the polar decomposition $P_K = r_K \cdot e^{i \theta_K}$ exists, is unique up to global $U(1)$ ambiguity, and introduces no new structural content. F3 will fix $r_K = \sqrt{b_K}$; F4 will fix $\theta_K = \pi_K$. F2's role is to establish the *form* of the decomposition; F3 and F4 fill its slots.

**Falsifier risk:** zero beyond Fal-5 (non-multiplicative fusion), addressed in §4.

---

## 3. Derivation of F4 — Phase = Polarity

### 3.1 The claim

The phase $\theta_K$ in F2's polar decomposition is exactly Primitive 09's polarity phase $\pi(K, x, t)$:

$$
\theta_K(x, t) = \pi(K, x, t) \qquad (2)
$$

with no additional phase variable, no functional transformation, no rescaling. This identification is forced by primitive-enumeration: Primitive 09 is the unique primitive-level $U(1)$-valued angular variable in the ED stack, and the phase slot of F2's polar decomposition has no other structurally-supported source.

### 3.2 Primitive enumeration: which primitives supply angular variables?

We audit the entire ED primitive stack (Primitives 01–13) for any primitive-level $U(1)$-valued (or higher-dimensional angular) variable that could fill the phase slot of F2:

| Primitive | Supplies | Angular character |
|---|---|---|
| **Primitive 01 (Micro-Event)** | Discrete events; vertex set $V$ | None (set-valued, not angular) |
| **Primitive 02 (Chain)** | Chain identity-rule | None (rule-typed, not angular) |
| **Primitive 03 (Participation)** | Edge structure; relational adjacency | None (relational-typed, not angular) |
| **Primitive 04 (Bandwidth)** | Edge weighting $w : E \to \mathbb{R}_{\geq 0}$ | None ($\mathbb{R}_{\geq 0}$-valued, not angular) |
| **Primitive 05 (Event Density)** | Density field $\rho : V \to \mathbb{R}_{\geq 0}$ | None (real scalar, not angular) |
| **Primitive 06 (ED Gradient)** | $\nabla \rho$ on the participation graph | Vector-valued in tangent bundle, not angular per se (orientations exist on rotation-equivariant scaffolding but are not $U(1)$-valued primitive variables) |
| **Primitive 07 (Channel)** | Channel sub-structure labels | None (set/sub-graph-typed, not angular) |
| **Primitive 08 (Multiplicity)** | Effective channel count $M_\mathrm{eff}$ | None (real-positive scalar, not angular) |
| **Primitive 09 (Tension Polarity)** | Polarity phase $\pi(K, x, t) \in U(1)$ | **$U(1)$-valued — the unique angular primitive** |
| **Primitive 10 (Individuation)** | Threshold for distinguishing chains | None (threshold-valued, not angular) |
| **Primitive 11 (Commitment)** | Discrete commitment events | None (event-valued, not angular) |
| **Primitive 12 (Thickening)** | Thickening density $\tau : M \to \mathbb{R}_{\geq 0}$ | None (real scalar density, not angular) |
| **Primitive 13 (Relational Timing)** | Proper-time intervals | None (real-valued temporal, not angular) |

**Result of audit.** Primitive 09 is the *unique* primitive-level source of a $U(1)$-valued angular variable in the ED stack. No other primitive supplies an angular variable that could fill F2's phase slot.

### 3.3 Could the phase be a *function* of polarity?

A more refined challenge: could $\theta_K = f(\pi_K)$ for some non-trivial function $f$, rather than $\theta_K = \pi_K$ directly?

For $\theta_K$ to be a $U(1)$-valued field that respects the structural content of polarity, $f$ must be a $U(1) \to U(1)$ map. The continuous group homomorphisms $U(1) \to U(1)$ are characters — multiplications by integer winding number $n \in \mathbb{Z}$:

$$
f_n : U(1) \to U(1), \qquad f_n(\pi) = n \pi \pmod{2\pi}
$$

A non-trivial choice $n \neq 1$ would mean the participation-measure phase $\theta_K$ winds $n$ times faster than the polarity phase $\pi_K$. For such an $n$ to be primitive-level supported, there would have to be a primitive supplying an integer winding number distinct from polarity itself. **The audit of §3.2 shows no such primitive exists.** Integer winding-numbers are not primitive-level structural commitments in the ED stack; they are derived quantities at most.

The case $n = 1$ — direct identification $\theta_K = \pi_K$ — is the only structurally-supported choice. Higher-character maps $f_n$ for $|n| > 1$ require structural input not present in the primitive stack.

The case $n = 0$ — phase identically zero, $\theta_K \equiv 0$ — would mean the participation measure has no phase content at all, reducing $P_K$ to a real-valued field. This contradicts F1's commitment to $\mathbb{C}$-valued range with non-trivial phase content. Dismissed.

The case $n = -1$ — $\theta_K = -\pi_K$ — corresponds to the standard complex-conjugation freedom $z \leftrightarrow z^*$, which is a global gauge convention rather than a structurally distinct alternative. The two conventions describe the same physical content (related by the $\mathrm{CPT}$-style structural symmetry); no primitive selects one over the other. We adopt the standard convention $n = +1$.

### 3.4 Could the phase be a *combination* of polarity with other quantities?

Another refinement: could $\theta_K = \pi_K + g(b_K, \rho, \ldots)$ for some real-valued function $g$ of other primitive quantities (bandwidth, density, gradient magnitudes, etc.)?

For $\theta_K$ to be a $U(1)$-valued field, $g$ must take real values modulo $2\pi$. A non-trivial $g$ would shift the phase by a primitive-level scalar quantity.

Two cases:
- *Constant $g$.* A constant phase shift $\theta_K = \pi_K + \alpha$ is the standard global $U(1)$ gauge freedom of F2's polar decomposition (§2.4). It is not a structurally distinct alternative; conventionally $\alpha = 0$.
- *Non-constant $g(b_K, \rho, \ldots)$.* For $g$ to depend on real-valued primitive quantities like bandwidth, $g$ would have to be a primitive-level supported map $\mathbb{R} \to \mathbb{R} \pmod{2\pi}$. Such a map requires its own structural content — a primitive-level identification of "the right phase shift as a function of bandwidth." No primitive supplies this. Real-valued primitives ($b$, $\rho$, $\tau$, etc.) are dimensionful magnitudes; their identification with phase shifts would require a dimensional conversion factor that is not primitive-level supported.

**Conclusion.** No non-trivial $g$ is structurally supported. The phase is exactly $\pi_K$ up to the standard global $U(1)$ convention.

### 3.5 The identification is independent of downstream items

F4's argument uses only:
- Primitive 09 (supplies the $U(1)$-valued polarity field directly).
- Primitive enumeration (audits the entire stack for alternative angular variables; finds none).
- Standard $U(1)$ representation theory (continuous homomorphisms $U(1) \to U(1)$ are integer characters).

It does *not* use:
- U2 (sesquilinear inner product) — downstream of U1.
- Theorem 10 (Born) — downstream.
- U5 (adjacency partition) — downstream.
- U3, U4, Schrödinger, Bell, Heisenberg — all downstream.

The argument is fully primitive-level + mathematical, with no circularity risk.

### 3.6 Verdict for F4

**Established.** The phase $\theta_K$ in F2's polar decomposition is exactly Primitive 09's polarity phase $\pi(K, x, t)$, up to standard global $U(1)$ gauge convention. Primitive enumeration confirms Primitive 09 is the unique primitive-level $U(1)$-valued angular variable; non-trivial functional alternatives (integer-character winding $n \neq 1$, non-constant phase shifts $g(b_K, \rho, \ldots)$) require primitive-level inputs not present in the stack.

**Falsifier Fal-4 (phase ≠ polarity) is dispatched.**

---

## 4. Falsifier Audit

### 4.1 Fal-4 (phase ≠ polarity) — dispatched by F4

**Fal-4's claim.** The phase factor in U1's construction uses some $U(1)$-valued angular variable distinct from Primitive 09's polarity phase.

**Dispatch.** §3.2's primitive enumeration confirms Primitive 09 is the unique source of a $U(1)$-valued angular variable in the ED stack; no other primitive supplies one. §3.3 confirms non-trivial functional alternatives ($n \neq 1$ winding-number maps) require primitive-level integer-winding inputs not present in the stack. §3.4 confirms phase-shift alternatives via real-valued primitives require dimensional-conversion structure not supplied. The phase factor is exactly $e^{i \pi_K}$ up to global gauge convention.

### 4.2 Fal-5 (non-multiplicative fusion) — dispatched jointly by F1 + F2

**Fal-5's claim.** Bandwidth and polarity are combined by an operation other than multiplication — e.g., additive fusion $\sqrt{b} + e^{i \pi}$, or some tensor-product fusion in a higher-dimensional algebra.

**Dispatch.** Once F1 establishes $P_K \in \mathbb{C}$ (Memo 03) and F2 establishes the polar decomposition $P_K = r_K \cdot e^{i \theta_K}$, the *multiplicative* form is automatic by the polar decomposition theorem. There is no "additive" or "tensor-product" alternative that simultaneously: (i) places $P_K$ in $\mathbb{C}$, (ii) extracts a non-negative real magnitude $r_K$, (iii) extracts a $U(1)$-valued phase $\theta_K$, and (iv) is structurally distinct from $r_K \cdot e^{i \theta_K}$.

Specifically:
- *Additive fusion $r_K + e^{i \theta_K}$.* Produces a complex number, but its magnitude is $\sqrt{r_K^2 + 2 r_K \cos\theta_K + 1}$ — not equal to $r_K$. The natural magnitude/phase decomposition of this object is *not* $r_K, \theta_K$. So additive fusion does not produce the structurally-claimed decomposition.
- *Tensor-product fusion $r_K \otimes e^{i \theta_K}$ in a higher-dimensional algebra.* Requires a higher-dimensional algebra not in the primitive stack. F1's Frobenius classification (Memo 03) restricts to $\mathbb{R}, \mathbb{C}, \mathbb{H}$; tensor-product fusions live in $\mathbb{R} \otimes \mathbb{C} = \mathbb{C}$ trivially, $\mathbb{R} \otimes \mathbb{H} = \mathbb{H}$ (dismissed by F1), or higher-dimensional structures not admissible.

**Fal-5 is dispatched** as soon as F1 + F2 are jointly in place. F2 contributes no new risk: its content is purely the polar-decomposition theorem applied to F1's commitment.

### 4.3 Falsifiers remaining active for Memo 03

Three falsifiers remain active for Memo 03:

- **Fal-1 (real-valued)**, attached to F1.
- **Fal-2 (quaternionic)**, attached to F1.
- **Fal-3 (different exponent)**, attached to F3.

Fal-5's full dispatch awaits F1's closure in Memo 03; the F2 contribution (multiplicative form is the polar decomposition, not an alternative fusion) is in place here.

---

## 5. Memo-Level Summary Table

| Sub-feature | Derivation summary | Primitive inputs | Falsifier dispatched | Circularity notes |
|---|---|---|---|---|
| **F2** Polar decomposition | Standard polar-decomposition theorem on $\mathbb{C}$ applied pointwise to the participation-measure field. Conditional on F1's commitment to $\mathbb{C}$-valued range. Decomposition exists pointwise, is unique up to global $U(1)$ gauge convention, and introduces no new structural commitment. | F1 (anticipated forced; conditional input); polar-decomposition theorem (mathematical) | Fal-5 (jointly with F1) | None. F2 uses only F1's anticipated content + standard mathematics. No downstream item invoked. |
| **F4** Phase = polarity | Primitive enumeration (§3.2) confirms Primitive 09 is the unique primitive-level $U(1)$-valued angular variable in the ED stack. Functional alternatives ($n \neq 1$ winding-number characters; non-constant phase shifts) require primitive-level inputs not present. Phase is identified as $\theta_K = \pi_K$ up to global $U(1)$ gauge convention. | Primitive 09 ($U(1)$-valued polarity); primitive enumeration; $U(1)$ representation theory (continuous homomorphisms are integer characters) | Fal-4 | None. F4 uses Primitive 09 + primitive enumeration + standard mathematics. No downstream item invoked. The argument is structurally independent of F1's specific algebraic content; if F1 closes (anticipated), F4's identification automatically slots into F2's phase variable. |

**Net status after Memos 01–02.** Two of four U1 sub-features (F2 conditional on F1, F4) are now established. Two remain active for Memo 03: F1 (complex-valued range) and F3 (magnitude exponent $|P|^2 = b$). F2's establishment is conditional on F1; once F1 closes, F2's establishment becomes unconditional. F4 is unconditionally established, contingent only on the existence of a phase slot in U1's construction (which F2 supplies).

The arc's verdict reduces to Memo 03's treatment of F1 and F3.

---

## 6. Recommended Next Steps

**(a) Begin Memo 03 (F1 + F3 derivations + arc verdict).** The natural next session step. Memo 03 is the load-bearing memo of the U1 arc and should derive F1 (complex-valued range, with explicit dismissal of real-valued and quaternionic alternatives) and F3 (magnitude exponent $|P|^2 = b$, with explicit derivation from primitive-level bandwidth additivity + $U(1)$-invariance + quadratic-form theory). Anticipated structure: §1 F1 derivation (Frobenius theorem + Primitive 09 $U(1)$-only structure + interference / superposition argument from primitive level), §2 F3 derivation (bandwidth additivity + quadratic-form classification), §3 falsifier audit (Fal-1, Fal-2, Fal-3), §4 verdict, §5 downstream cascade.

**(b) Pre-Memo-03 audit of Primitive 09's commitment to $U(1)$-only polarity.** F1's dismissal of quaternionic alternatives (Fal-2) hinges on Primitive 09 supplying *only* a $U(1)$-valued phase, not an $S^3$-valued or higher-dimensional polarity. A focused read of Primitive 09 §1.16 ("polarity is a phase in the full treatment") and §1.30 ("not a scalar") before drafting Memo 03 will sharpen the argument. The structural commitment of Primitive 09 to $U(1)$-only is the load-bearing dismissal of quaternionic QM — the audit should confirm this commitment is explicit in the primitive's text rather than implicit.

**(c) Pre-Memo-03 audit of bandwidth-additivity content in Primitive 04.** F3's load-bearing argument depends on bandwidth being additive over disjoint channel-subsets at the *kinematic* level (the participation graph itself), not at the participation-measure level (which would invoke F1 transitively). The relevant content is in Primitive 04 §2 (bandwidth as edge-weight $w : E \to \mathbb{R}_{\geq 0}$ with disjoint-sum decomposition over edge-subsets). A focused read confirming this is genuinely primitive-level (not a downstream consequence of U2's inner product or any other downstream item) will sharpen Memo 03's quadratic-form argument.

---

## 7. Cross-references

- Arc outline: [`arcs/U1/00_arc_outline.md`](00_arc_outline.md)
- Memo 01 (decomposition + circularity audit): [`arcs/U1/01_decomposition_and_mapping.md`](01_decomposition_and_mapping.md)
- Step-1 participation-measure memo: [`arcs/arc-foundations/participation_measure.md`](../arc-foundations/participation_measure.md)
- U5 Memo 02 (parallel template for the cleaner-sub-features derivation): [`arcs/U5/02_derivations_F1_F2_F4.md`](../U5/02_derivations_F1_F2_F4.md)
- U2 Memo 02 (parallel derivation template): [`arcs/U2/02_C3a_C3b_derivation.md`](../U2/02_C3a_C3b_derivation.md)

**Source primitives (used in this memo):**
- Primitive 01–13 (audited in §3.2 for $U(1)$-valued angular variables): `quantum/primitives/`
- Primitive 09 (load-bearing for F4): `quantum/primitives/09_tension_polarity.md`

**Mathematical reference:**
- Polar decomposition for complex numbers: any standard complex-analysis textbook.
- $U(1)$ continuous homomorphisms as integer characters: any standard representation-theory textbook.

---

## 8. One-line memo summary

> **F2 (polar decomposition) is established conditional on F1: given that the participation measure takes values in $\mathbb{C}$ (F1 anticipated), the polar form $P_K = r_K \cdot e^{i \theta_K}$ exists pointwise and is unique up to global $U(1)$ gauge convention, by the standard polar-decomposition theorem on $\mathbb{C}$. F2 introduces no new structural commitment. F4 (phase = polarity) is established unconditionally: primitive enumeration of the entire ED stack (Primitives 01–13) confirms Primitive 09 is the unique primitive-level source of a $U(1)$-valued angular variable; non-trivial functional alternatives — integer-character winding maps $f_n(\pi) = n\pi$ for $n \neq 1$, or phase-shift maps $g(b, \rho, \ldots)$ via real-valued primitives — require primitive-level inputs not present in the stack. The phase is identified as $\theta_K = \pi_K$ up to global gauge convention. Falsifiers Fal-4 (dispatched fully) and Fal-5 (dispatched jointly by F1 + F2 once F1 closes); F2 contributes no new risk. Two of four U1 sub-features now established; arc verdict reduces to Memo 03's load-bearing treatment of F1 (complex-valued range) and F3 (magnitude exponent $|P|^2 = b$). Active falsifiers remaining: Fal-1 (real-valued, F1), Fal-2 (quaternionic, F1), Fal-3 (different exponent, F3).**
