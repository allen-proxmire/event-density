# U4 Arc — Examination Outline

**Date opened:** 2026-04-26
**Location:** `arcs/U4/`
**Goal:** Determine whether U4 — the specific Hamiltonian form $H_k = \hbar^2 |k|^2/(2m)$ for the free-kinetic-energy operator on the participation-measure Hilbert space, plus the kinetic + potential decomposition $H = T(p) + V(x)$ — is FORCED, CONDITIONAL, or NOT FORCED by ED's primitives plus the now-FORCED upstream items (U1, U2, U5, Theorem 10).
**Predecessor work:** `arcs/arc-foundations/u4_hamiltonian_form_derivation.md` (2026-04-24 tightening-program memo). The earlier memo claimed structural FORCED status for the $k^2$ form via translation + rotation + analyticity + non-relativistic-limit arguments, but it was written before the structural-derivation methodology of the 2026-04-26 cycle (born_gleason → U2 → U5 → U1) was established. The present arc supersedes the earlier memo by applying the sharper primitive-only methodology and explicitly auditing the U3-dependency questions left open there. The synthesis paper [`papers/QM_Emergence_Structural_Completion/`] §4.2 ranks U4 (with U3) as "specific to Schrödinger" and "the most analog to standard QM assumptions" — i.e., the most delicate of the structural-foundations-cycle items.
**High-leverage status:** U4 is one of the two remaining active upstream CANDIDATEs of the QM-emergence Phase-1 program (the other being U3, the participation-measure evolution equation itself). Promoting U4 closes the kinetic-energy-form question of Schrödinger emergence; combined with U3, layer 3 (dynamical) of the Phase-1 program would be structurally complete, completing the entire Phase-1 framework except for the description-level continuum gauge.

---

## 1. The U4 Question

### 1.1 Precise statement

The QM-emergence Phase-1 framework identifies, in the thin (continuum) limit of the participation-measure evolution, a specific Hamiltonian operator acting on the participation-measure Hilbert space:

$$
\hat{H} = -\frac{\hbar^2 \nabla^2}{2m} + V(\hat{x})
$$

equivalently in momentum representation,

$$
H_k = \frac{\hbar^2 |k|^2}{2m} + V(\hat{x}) \qquad \text{(U4)}
$$

with the kinetic term quadratic in momentum (with coefficient $1/(2m)$) and an additive position-dependent potential $V(\hat{x})$. This is the standard non-relativistic Hamiltonian form, and it is what makes the evolution equation (U3) reduce to the Schrödinger equation in its standard textbook form.

### 1.2 In the formal style of the QM-emergence upstream-commitment list

> **U4 (Specific Hamiltonian Form / Momentum-Basis Identification).** In the thin-participation continuum limit, the channel index $K$ admits a continuous momentum-space coordinate $k$ via Stone's theorem applied to translation symmetry on the U2 Hilbert space. The Hamiltonian operator on the participation-measure Hilbert space takes the specific form $\hat{H} = T(\hat{p}) + V(\hat{x})$ with $T(\hat{p}) = \hbar^2 |\hat{p}|^2 / (2m)$ — quadratic-in-momentum free kinetic energy plus position-only potential. The coefficient $\hbar^2/(2m)$ has $\hbar$ inherited from the dimensional-atlas Madelung anchoring and $m$ inherited per Arc M's "form FORCED, values INHERITED" framing. **Affects: Step 2 (Schrödinger emergence).**

### 1.3 Role in the participation-measure → Hilbert-space → QM-emergence chain

U4 is the structural backbone of Phase-1 Step 2's Schrödinger emergence. Without U4, U3's linear evolution equation $i\hbar \partial_t P_K = \hat{H}_K P_K + \sum V_{KK'} P_{K'}$ has no specific functional form for the generator $\hat{H}$. U4 supplies the form; U3 supplies the existence + Hermiticity + linear-first-order structure.

The chain leading to standard Schrödinger:

```
Primitives 03, 04, 06, 07, 09  →  U1 (FORCED) → P_K = √b · e^{iπ}
                                  → U2 (FORCED) → ⟨P|Q⟩ inner product
                                  → translation symmetry via Primitives 03 + 06
                                  → U4 (this arc) → momentum basis + H_k = ℏ²k²/(2m)
                                  → U3 (still CANDIDATE) → iℏ ∂_t P_K = H̃ P_K
                                  → Step 2 Schrödinger evolution (FORCED on U3 + U4)
```

U4 sits *parallel* to U3 in the dynamical layer (layer 3 of the Phase-1 program). The two are intertwined in the original Step-1 formulation but can be derived separately if the structural inputs are partitioned carefully.

---

## 2. Decomposition into Sub-Features

U4 packages five structurally distinct sub-claims, each requiring independent structural status determination.

### 2.1 The five sub-features

- **(F1) Channel-momentum identification.** In the thin/continuum limit, the channel index $K$ is labeled by a continuous momentum-space coordinate $k$ via Stone's theorem applied to translation symmetry. The basis-change between channel-representation and momentum-representation is the standard Fourier transform.

- **(F2) Plane-wave eigenfunctions.** The eigenfunctions of the translation generator $\hat{p} = -i\hbar \nabla$ in the position representation are plane waves $\langle x | k \rangle = (2\pi\hbar)^{-d/2} \cdot e^{i k \cdot x / \hbar}$. Mathematical consequence of F1.

- **(F3) Quadratic-in-momentum kinetic energy.** The free-kinetic-energy operator depends only on $|k|^2$ — i.e., $T(\hat{p}) \propto |\hat{p}|^2$ rather than $|\hat{p}|$, $|\hat{p}|^3$, $|\hat{p}|^4$, or some non-polynomial form. Linear-in-$k$ and higher-even-power-in-$k$ terms are absent in the non-relativistic limit.

- **(F4) Specific coefficient $1/(2m)$ structure.** The proportionality constant in $T(\hat{p}) = c |\hat{p}|^2$ takes the specific form $c = 1/(2m)$ where $m$ is a mass parameter. The *form* of the coefficient (inverse twice mass) is structural; the *value* of $m$ is inherited per Arc M's form-FORCED-value-INHERITED methodology, and the $\hbar^2$ factor is inherited from the dimensional-atlas Madelung anchoring.

- **(F5) Kinetic + potential decomposition.** The Hamiltonian admits the additive decomposition $\hat{H} = T(\hat{p}) + V(\hat{x})$, with the kinetic part depending only on momentum and the potential part depending only on position. There are no cross terms involving products of $\hat{p}$ and $\hat{x}$ in the free-particle-plus-external-potential structure.

### 2.2 Anticipated structural status

| Sub-feature | Anticipated status | Reasoning |
|---|---|---|
| **F1** Channel-momentum identification | **forced-via-derivation** | Stone's theorem on translation symmetry (Primitives 03 + 06) on the U2 Hilbert space (now FORCED). Direct transfer of the U5 Memo 03 §1 argument to the channel-basis question. |
| **F2** Plane-wave eigenfunctions | **automatic given F1** | Mathematical: eigenfunctions of $-i\hbar \nabla$ are plane waves. |
| **F3** Quadratic-in-momentum kinetic energy | **load-bearing** | The classical "why $|k|^2$?" question. Requires translation invariance + spatial rotation invariance + parity (or time-reversal) + non-relativistic-limit scope condition + analyticity-in-$k$ to force quadratic-leading behavior with linear-in-$k$ and higher-even-power terms forbidden. |
| **F4** Specific coefficient $1/(2m)$ | **load-bearing for form; coefficient values INHERITED** | The coefficient *form* (inverse-twice-mass) is structural via Galilean correspondence or equivalent argument. The mass $m$ is inherited per Arc M's framing. Whether this is "FORCED form" or "FORCED with mass-as-input" is the load-bearing structural question. |
| **F5** Kinetic + potential decomposition | **forced-via-derivation** | Translation invariance forbids cross terms in the free-particle Hamiltonian; locality of potential interactions forces $V(\hat{x})$ to depend only on $\hat{x}$, not $\hat{p}$. Direct argument from the free-vs-interacting structural separation. |

The arc has two load-bearing items (F3 and F4), with F4 split into form-FORCED + value-INHERITED. F1 and F5 close cleanly via established techniques (Stone's theorem + structural separation arguments). F2 is automatic.

### 2.3 Discrete vs continuum regime split

U4 is fundamentally a *continuum-regime* claim — the momentum-basis identification F1 requires a continuous translation group, which exists naturally on the emergent manifold $M$ (Primitive 12 thickening) but is replaced by discrete-translation structure on the participation graph. The discrete-regime analog would be the discrete Fourier transform on the participation-graph vertex set, with the discrete-momentum eigenvalues replacing the continuous $k$.

For this arc, we treat U4 as a continuum-regime claim by default, with the discrete-regime analog noted but not derived in detail. The continuum regime is the regime in which standard Schrödinger evolution applies; this is the regime Phase-1 Step 2 targets.

The U2-Continuum gauge $(b_K, d\mu) \to (\Omega^{-D} b_K, \Omega^D d\mu)$ acts on the participation measure but does not affect the form of the Hamiltonian operator (which depends on $\hat{p}$ and $\hat{x}$, not on bandwidth densities directly). U4 is gauge-compatible by inheritance.

### 2.4 Scope condition: the non-relativistic limit

A crucial scope condition: U4 is the *non-relativistic* Hamiltonian form. In the relativistic regime, the free-particle dispersion relation is $E = \sqrt{p^2 c^2 + m^2 c^4}$, not $E = p^2/(2m) + mc^2$. The non-relativistic limit is recovered by expanding around $p \ll mc$ and dropping the rest energy.

Phase-2 Arc R already established the relativistic case (Klein-Gordon, Dirac). U4 lives in Phase-1 Step 2's *non-relativistic single-particle* scope. The relationship between U4's quadratic form and Arc R's relativistic dispersion is consistency at the Hamiltonian level: U4 is the leading-order non-relativistic expansion of Arc R's relativistic kinetic energy.

This scope choice means U4 inherits the non-relativistic-limit assumption, which is a structural commitment of Phase-1 Step 2 itself, not a U4-specific commitment.

---

## 3. Structural Inputs and Circularity Audit

### 3.1 Primitives drawn upon

- **Primitive 03 (Participation):** supplies graph homogeneity → translation symmetry as a kinematic input (same as in U5).
- **Primitive 04 (Bandwidth):** supplies the magnitude content of the participation measure (via U1's $|P|^2 = b$).
- **Primitive 06 (ED Gradient):** supplies the spatial axis along which translation acts.
- **Primitive 09 (Tension Polarity):** supplies the $U(1)$ phase content (via U1).

### 3.2 Inherited FORCED items (permitted as inputs)

The U4 arc has access to substantially more structural infrastructure than the prior arcs because the structural-foundations cycle has now closed five upstream items:

- **U1 (FORCED, this session):** participation-measure construction $P_K = \sqrt{b_K} \cdot e^{i \pi_K}$.
- **U2-Discrete (FORCED, this session):** sesquilinear inner product on the participation-measure Hilbert space.
- **U2-Continuum (FORCED, this session):** continuum inner product up to the conformal gauge.
- **U5 (FORCED, this session):** adjacency-band Fourier-conjugate partition + Stone's theorem on translation symmetry establishing the position-momentum unitary intertwiner.
- **Theorem 10 (FORCED, this session):** Born rule via Gleason–Busch path.

In particular, U5's Memo 03 §1 derivation of Stone's theorem on the participation graph's translation group is *directly applicable* to F1 of the present arc. The U4 arc inherits U5's machinery and applies it to identify the momentum basis.

### 3.3 Inputs *not* available (sibling CANDIDATE)

**U3 (the participation-measure evolution equation $i\hbar \partial_t P_K = \hat{H} P_K + \sum V_{KK'} P_{K'}$) is a sibling upstream CANDIDATE** and cannot be invoked as input to U4 without circularity (or without explicitly framing U4 as conditional on U3).

The methodological choice for this arc:

- **Framing 1: U4 conditional on U3.** Derive U4's specific Hamiltonian form *given* that an evolution equation with Hermitian generator $\hat{H}$ exists. The verdict is "U4 FORCED conditional on U3"; promoting U3 in a separate arc would make U4 fully unconditional.

- **Framing 2: U4 jointly with U3.** Derive both together, since they are entangled.

We adopt **Framing 1** (conditional on U3) for this arc because it preserves the structural-derivation methodology's discipline — each arc operates within its own scope. The U3 arc, taken up subsequently, would address the existence-of-evolution-operator question independently. This framing parallels how the U5 arc was conditional on U2 before U2 closed.

### 3.4 Mathematical infrastructure

- **Stone's theorem on one-parameter unitary groups** (Stone 1932). Already used in U5 Memo 03 §1.
- **Fourier-transform unitarity on $L^2(\mathbb{R}^d)$.** Standard.
- **Functional calculus on self-adjoint operators.** Standard.
- **Asymptotic / analyticity arguments for the kinetic-energy form.** The non-relativistic limit assumes analyticity in $p$ around $p = 0$ for the kinetic-energy operator.
- **Galilean (or equivalent) invariance arguments.** For F4's coefficient form. We treat the load-bearing question of which structural input supplies Galilean invariance as a Memo 03 question.

### 3.5 Circularity audit

Following the discipline established in the U1 arc (Memo 01 §4), we explicitly identify which inputs are permitted vs forbidden:

**Permitted inputs:**
- Primitives 03, 04, 06, 07, 09 in their kinematic content.
- U1 (FORCED).
- U2-Discrete and U2-Continuum (FORCED).
- U5 (FORCED) — particularly the Stone's-theorem machinery.
- Theorem 10 (FORCED) — particularly the Born identifications $b_x \propto |\Psi|^2$ for momentum-density interpretations.
- Standard mathematical infrastructure (Stone's theorem, functional calculus, Fourier transform).
- Non-relativistic-limit scope condition (Phase-1 Step 2 scope).

**Forbidden inputs (would be circular or require sibling-CANDIDATE invocation):**
- U3 — sibling CANDIDATE; treated as conditional input (Framing 1 above).
- The standard Schrödinger equation in its textbook form — would assume U3 + U4 jointly.
- The classical Hamiltonian $H = p^2/(2m) + V(x)$ as a postulate — would be assuming the answer.

**Specifically deferred (related but separate):**
- The mass parameter $m$'s primitive-level origin — Arc M established "form FORCED, values INHERITED"; the present arc inherits this framing for F4's coefficient.

---

## 4. Falsifiers

The arc is **closed FORCED** if all five sub-features close uniquely under the available structural inputs (with F4 split into form-FORCED + value-INHERITED).

The arc is **closed CONDITIONAL** if F1, F2, F5 close uniquely but F3 or F4 admits a non-pathological alternative consistent with the primitive structure plus inherited items.

The arc is **closed NOT FORCED** if any sub-feature admits a *physically distinct* alternative producing a different downstream phenomenology than standard non-relativistic quantum mechanics.

### 4.1 Specific falsifiers

- **(Fal-1) No momentum-basis identification.** Attaches to **F1**. If translation symmetry on the participation graph fails to support Stone's theorem (e.g., if the graph admits no continuous translation group in the thin limit), F1 fails and U4 collapses entirely. *Anticipated dispatch:* U5's Stone's-theorem argument applies directly.

- **(Fal-2) Linear-in-$k$ kinetic term.** Attaches to **F3**. If the kinetic-energy operator includes a $|k|$ term (with no quadratic suppression), the dispersion relation would be linear at low momentum. This is forbidden in non-relativistic kinematics by parity / time-reversal arguments combined with the non-relativistic-limit scope condition.

- **(Fal-3) Higher-even-power terms.** Attaches to **F3**. If the kinetic-energy operator includes $|k|^4, |k|^6, \ldots$ terms (with non-zero coefficients in the non-relativistic limit), the dispersion would deviate from quadratic at higher momenta. *Anticipated dispatch:* analyticity in $k$ + non-relativistic-limit expansion forces leading-order quadratic with higher-even-power terms suppressed by $O(p^4/m^3 c^2)$ relativistic corrections.

- **(Fal-4) Coefficient $\neq 1/(2m)$.** Attaches to **F4**. If the proportionality constant in $T \propto |k|^2$ is something other than $\hbar^2/(2m)$ — e.g., $\hbar/m$, $1/(m c)$, etc. — the dispersion relation would have wrong dimensional scaling. *Anticipated dispatch:* dimensional analysis + Galilean-invariance argument (or equivalent) forces $\hbar^2/(2m)$.

- **(Fal-5) Anisotropic kinetic energy.** Attaches to **F3**. If the kinetic-energy operator depends on the direction of $k$, not just $|k|^2$, the dispersion would be anisotropic. *Anticipated dispatch:* spatial rotation invariance of the participation graph (homogeneity from Primitive 03) forces isotropy.

- **(Fal-6) Position-momentum cross terms.** Attaches to **F5**. If the Hamiltonian includes terms like $p \cdot x + x \cdot p$, the kinetic + potential decomposition fails. *Anticipated dispatch:* translation invariance forbids position-dependent kinetic terms in the free-particle Hamiltonian; locality of external potentials forces $V$ to depend only on $\hat{x}$.

- **(Fal-7) Relativistic dispersion in non-relativistic regime.** Attaches to **F3**. If the kinetic-energy operator is the full relativistic $E = \sqrt{p^2 c^2 + m^2 c^4} - mc^2$ rather than its non-relativistic expansion, U4 is not the non-relativistic Hamiltonian form. *Resolution:* the non-relativistic-limit scope condition fixes the regime; full relativistic dispersion is Arc R's domain, not U4's.

### 4.2 Discrete vs continuum regime falsifier attachment

All falsifiers attach in the continuum regime. The discrete regime requires its own treatment for F1 (discrete Fourier transform vs continuous) but the substantive dynamical content of F3, F4 is fundamentally a continuum-regime claim.

---

## 5. Memo Plan

### Memo 01: `01_decomposition_and_mapping.md`

Decompose U4 into sub-features F1–F5. For each, identify which primitives + inherited FORCED items + mathematical infrastructure supply the structural inputs. Classify each as automatic / forced-via-derivation / load-bearing. **Crucially: perform a circularity audit identifying that U3 is a sibling CANDIDATE and explicitly framing U4 as conditional on U3.** Also audit the existing 2026-04-24 tightening-program memo to identify which arguments transfer cleanly and which need sharpening under the 2026-04-26 methodology.

**Anticipated structure:**
- §1: U4 statement and role
- §2: Five sub-features with primitive + inherited-item mapping
- §3: Circularity audit (U3 sibling CANDIDATE, Framing 1 adopted)
- §4: Audit of the existing tightening-program memo
- §5: Falsifier-to-sub-feature attachment
- §6: Comparison to U5 / U1 structural shape
- §7: Recommended next steps

### Memo 02: `02_F1_F2_F5_derivations.md`

Derive the three forced-via-derivation / automatic sub-features: F1 (channel-momentum identification via Stone's theorem on translation symmetry), F2 (plane-wave eigenfunctions, automatic), F5 (kinetic + potential decomposition via translation invariance of free part + position-locality of potential).

**Anticipated structure:**
- §1: F1 derivation (Stone's theorem, paralleling U5 Memo 03 §1 with channel-basis target)
- §2: F2 derivation (plane-wave eigenfunctions of $\hat{p}$)
- §3: F5 derivation (kinetic + potential decomposition)
- §4: Joint status; load-bearing items deferred to Memo 03

### Memo 03: `03_F3_F4_and_verdict.md`

The load-bearing memo. Derives F3 (quadratic-in-$k$ kinetic-energy structure) and F4 (specific coefficient $1/(2m)$ form). Anticipated leading arguments:

- **F3.** Translation invariance + spatial rotation invariance + non-relativistic-limit scope condition + analyticity-in-$k$ → free-particle Hamiltonian is a function of $|k|^2$ alone, with leading-order quadratic and higher-order terms suppressed in the non-relativistic limit. Linear-in-$|k|$ terms forbidden by parity / time-reversal symmetry.

- **F4.** Galilean invariance (or equivalent argument from the non-relativistic regime's transformation properties) forces the proportionality constant to take the form $1/(2m)$ with $m$ a mass parameter. The mass $m$ is inherited per Arc M.

The substantive load-bearing question for Memo 03: **what primitive-level input supplies Galilean invariance?** The candidate answers:
- (a) Galilean invariance is a *consequence* of more basic primitive structure (graph homogeneity in space + observer-shifting consistency).
- (b) Galilean invariance is *inherited* from the non-relativistic-limit scope condition itself.
- (c) An alternative argument (e.g., dimensional analysis + a primitive-level energy scale) suffices without invoking Galilean invariance directly.

Memo 03 must commit to an answer and either derive the Galilean argument from primitives or flag the structural conditionality explicitly.

**Anticipated structure:**
- §1: F3 derivation (quadratic structure)
- §2: F4 derivation (coefficient form)
- §3: Falsifier audit
- §4: Verdict + downstream cascade
- §5: Schrödinger emergence (Step 2) status update

### Memo 04: `04_closure_and_summary.md` *(optional but recommended)*

Closure memo with canonical narrative, integration into the QM-emergence program, and public-facing explainer. Parallels the U5 Memo 04 and U1 Memo 04 templates.

---

## 6. Comparison to Prior Arcs

### 6.1 Methodological similarities

| Methodological element | U5 | U1 | U4 (anticipated) |
|---|---|---|---|
| Decomposition into sub-features | 5 (F1–F5) | 4 (F1–F4) | 5 (F1–F5) |
| Automatic items | 0 | 1 (F2 polar decomposition) | 1 (F2 plane-wave eigenfunctions) |
| Forced-via-derivation items | 3 | 1 | 2 (F1, F5) |
| Load-bearing items | 2 (F3 Fourier conjugacy, F5 exhaustion) | 2 (F1 algebra, F3 exponent) | 2 (F3 quadratic, F4 coefficient) |
| Methodological pattern | Same | Same | Same |
| Inherited prior FORCED items | U2, Theorem 10 | None | U1, U2, U5, Theorem 10 |
| Sibling CANDIDATE conditionality | None at time of arc | None | **U3 (Framing 1)** |
| New CANDIDATEs introduced | 0 | 0 | Anticipated 0 |

### 6.2 Structural differences

**U4 has the richest available inputs of any arc.** Five FORCED items inherited (U1, U2-Discrete, U2-Continuum, U5, Theorem 10). The Stone's-theorem machinery from U5 transfers directly to F1.

**U4 introduces a sibling-CANDIDATE conditionality (U3).** This is methodologically novel: prior arcs either had no sibling CANDIDATEs (U2-Discrete, U2-Continuum, U5) or were the most upstream item (U1). U4 is the first arc whose verdict is naturally framed as conditional on a sibling CANDIDATE rather than being unconditional.

**U4's load-bearing items are dynamical, not kinematic.** U5's load-bearing items were kinematic (Fourier conjugacy as basis-change; exhaustion as primitive-stack audit). U1's load-bearing items were structural-algebraic (carrier choice; magnitude exponent). U4's load-bearing items concern the *dynamical content* of the participation-measure evolution — specifically, what Hamiltonian acts on the Hilbert space. This is qualitatively different.

**U4 needs a structural input not present in prior arcs: Galilean invariance.** The previous arcs derived their results from translation + rotation + parity + analyticity + non-relativistic-limit. U4's F4 (coefficient form) plausibly requires Galilean invariance specifically. Whether this is primitive-derivable, inherited, or replaceable by an alternative argument is the load-bearing structural question.

### 6.3 Whether U4 is cleaner or more delicate

**Anticipated: more delicate than U5 and U1.** The synthesis paper [§4.2] explicitly classified U3 + U4 as "the most analog to standard QM assumptions" — i.e., the arc where the structural-derivation methodology may need its most careful application.

The principal risk locations:

1. **F4's Galilean-invariance argument.** If Galilean invariance must be inherited (Framing (b) above) rather than derived from primitives, U4's F4 verdict becomes "form FORCED conditional on Galilean invariance," and the arc's verdict is FORCED with two conditionalities (U3 sibling + Galilean inherited).

2. **Mass parameter $m$.** The form-FORCED-value-INHERITED framing inherits Arc M's methodology. This is established in the program but specifically for U4 it means the coefficient $1/(2m)$ is "FORCED form, INHERITED $m$" rather than "FORCED form + value." The verdict should be honest about this.

3. **The non-relativistic-limit scope condition.** U4 lives in a specific regime. The arc must be honest that the regime itself is a scope choice, not derived from primitives within U4's arc.

### 6.4 Overall assessment

U4 is anticipated to close FORCED with explicit form-FORCED-value-INHERITED framing, and conditional on (i) U3 (sibling CANDIDATE, addressed in subsequent arc) and (ii) potentially Galilean invariance (addressed in Memo 03 §1 of this arc). The arc is expected to be 4 memos (00 outline + 01 decomposition + 02 F1/F2/F5 + 03 F3/F4/verdict) plus an optional closure memo. The downstream effect, when combined with U3 closure later, is to fully derive Schrödinger evolution as a structural consequence of the ED primitive stack — completing the entire QM-emergence Phase-1 program except for the description-level continuum gauge.

---

## 7. Recommended Next Steps

**(a) Begin Memo 01 (decomposition + circularity audit).** Natural next session step. The decomposition is laid out above; Memo 01 should refine it with explicit primitive-level mapping for each sub-feature, perform the circularity audit (with U3-sibling-CANDIDATE handling explicit), and audit the existing tightening-program memo to identify which arguments transfer cleanly.

**(b) Pre-Memo-01 audit of the existing tightening-program memo `arcs/arc-foundations/u4_hamiltonian_form_derivation.md`.** A focused 15-minute read of that 2026-04-24 memo before drafting Memo 01 will identify (i) which structural arguments (translation, rotation, parity, analyticity, non-relativistic-limit) transfer cleanly to the 2026-04-26 methodology, (ii) which arguments invoked U3 (and need to be reframed under Framing 1), and (iii) which arguments invoked the SPECULATIVE chain-mass content (which is Arc M's domain, not U4's).

**(c) Pre-decide Memo 03's framing of the Galilean-invariance question.** Three options:
- *Derive Galilean invariance from primitives* (graph homogeneity + observer-shifting consistency). High intellectual value if it works.
- *Inherit Galilean invariance from non-relativistic-limit scope* (Framing (b) above). Cleanest verdict but adds a conditional.
- *Replace Galilean argument with dimensional-analysis-only argument*. Tightest but may leave the coefficient form less than fully forced.

Decide before drafting Memo 03 to keep the verdict framing focused. *Recommended:* commit to the first option as the target and fall back to the second if it does not close.

---

## 8. Cross-references

**Companion arcs (predecessors, FORCED inputs):**
- [`arcs/born_gleason/`](../born_gleason/) — Theorem 10 (Born) inherited
- [`arcs/U2/`](../U2/) — U2-Discrete inherited
- [`arcs/U2_continuum/`](../U2_continuum/) — U2-Continuum inherited
- [`arcs/U5/`](../U5/) — U5 inherited; Stone's-theorem machinery in U5 Memo 03 §1 directly applicable to F1
- [`arcs/U1/`](../U1/) — U1 inherited

**Sibling CANDIDATE (forbidden as input under Framing 1):**
- U3 (participation-measure evolution equation) — to be addressed in a subsequent arc.

**Predecessor tightening-program memo (audit target; supersession candidate):**
- [`arcs/arc-foundations/u4_hamiltonian_form_derivation.md`](../arc-foundations/u4_hamiltonian_form_derivation.md) (2026-04-24)

**Synthesis paper (upstream-commitment inventory; U4 listed in §4.1):**
- [`papers/QM_Emergence_Structural_Completion/`](../../papers/QM_Emergence_Structural_Completion/)

**Source primitives (load-bearing for U4):**
- Primitive 03 (Participation, supplies graph homogeneity for translation symmetry): `quantum/primitives/03_participation.md`
- Primitive 04 (Bandwidth, supplies magnitude content via U1): `quantum/primitives/04_participation_bandwidth.md`
- Primitive 06 (ED Gradient, supplies spatial axis): `quantum/primitives/06_ed_gradient.md`
- Primitive 07 (Channel, supplies channel index): `quantum/primitives/07_channel.md`
- Primitive 09 (Tension Polarity, supplies $U(1)$ phase content via U1): `quantum/primitives/09_tension_polarity.md`

**Mathematical infrastructure:**
- Stone's theorem on one-parameter unitary groups (Stone 1932). Already used in U5.
- Functional calculus on self-adjoint operators.
- Galilean-invariance arguments (load-bearing for F4).

**Project memory:** `memory/project_qm_emergence_arc.md`

---

## 9. One-line arc summary

> **Test whether U4 — the specific Hamiltonian form $H_k = \hbar^2 |k|^2/(2m) + V(\hat{x})$ on the participation-measure Hilbert space — is FORCED by Primitives 03/04/06/07/09 + the now-FORCED upstream items (U1, U2-Discrete, U2-Continuum, U5, Theorem 10) + standard mathematical infrastructure, framed as conditional on the sibling CANDIDATE U3 (the existence of a Hermitian generator). Five sub-features: F1 channel-momentum identification (forced-via-derivation, Stone's theorem applied to translation symmetry, paralleling U5 Memo 03 §1), F2 plane-wave eigenfunctions (automatic given F1), F3 quadratic-in-$k$ kinetic-energy structure (load-bearing, requires translation + rotation + parity + non-relativistic-limit + analyticity), F4 specific coefficient $1/(2m)$ (load-bearing for form, with $m$ inherited per Arc M's "form FORCED, values INHERITED" framing; load-bearing question is which structural input supplies Galilean invariance), F5 kinetic + potential decomposition (forced-via-derivation, translation invariance + locality of potential). Anticipated more delicate than U5 and U1 due to (a) Galilean-invariance question for F4, (b) sibling CANDIDATE conditionality on U3, (c) form-FORCED-value-INHERITED framing inheriting from Arc M. If FORCED, Schrödinger evolution becomes structurally derivable conditional on U3 alone; promoting U3 in a subsequent arc would close the entire QM-emergence Phase-1 structural-foundations program except for the description-level continuum gauge. Four-memo plan plus optional closure.**
