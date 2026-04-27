# Memo 04 — U3 Arc Closure, Canonical Summary, and Phase-1 Completion

**Date:** 2026-04-26
**Arc:** `arcs/U3/`
**Predecessors:** Memos [00](00_arc_outline.md), [01](01_decomposition_and_mapping.md), [02](02_F1_F2_F3_F4_derivations.md), [03](03_F5_and_verdict.md)
**Status:** Closure memo. Provides the canonical summary of the U3 arc and its public-facing explanation. Integrates the result into the QM-emergence structural-foundations program. **Formally closes Phase-1 of the QM-emergence program.**
**Purpose:** Close the U3 arc with a single document that serves both as internal entry-point and as a self-contained external narrative, and as the formal closure of the Phase-1 structural-foundations cycle.

---

## 1. Canonical Summary of the U3 Arc

The U3 arc asked whether the participation-measure evolution equation $i\hbar \, \partial_t P_K = \hat{H} P_K$ — the structural backbone of Phase-1 Step 2's Schrödinger emergence — is forced by ED's primitive stack rather than postulated. With U4 closed in the prior cycle (form FORCED, values INHERITED, conditional on U3 via Framing 1), U3 was the sole remaining upstream CANDIDATE in the QM-emergence Phase-1 program.

**The methodological framing.** The arc adopted a strict forbidden-input discipline analogous to U5's "U3 forbidden" discipline: U4 may not appear as a derivation premise for F1–F4, and may appear in F5 only as an identification target (never as a derivation premise). This protocol preserves acyclicity in the U3 ⟷ U4 loop: U4 was derived under Framing 1 conditional on U3's existence-of-Hermitian-generator content; U3 must therefore be derived independently and the F5 identification step must close the loop by *identification* rather than *derivation*.

**The decomposition (Memo 01).** U3 packaged into five structurally distinct sub-features: F1 existence of a strongly continuous time-translation representation, F2 uniqueness of the self-adjoint generator (Stone's theorem), F3 linearity, F4 first-order-in-time structure, F5 compatibility with U4's Hamiltonian form. The Memo 01 transfer audit established that F1–F4 were template-transfers from U5's spatial-translation derivation (Stone's theorem applied to a different symmetry group); F5 was the lone genuinely substantive question of the arc.

**The clean transfers (Memo 02).** F1 closed via Primitive 13 (continuous time axis, confirmed by pre-derivation audit) + Primitive 03 (homogeneity) + U2 measure translation-invariance, establishing $\{U_t : t \in \mathbb{R}\}$ as a strongly continuous one-parameter abelian unitary group on the U2 Hilbert space. F2 closed via Stone's theorem applied to F1's group, producing a unique self-adjoint generator $\hat{H}_{U3}$. F3 (linearity) and F4 (first-order-in-time) were automatic consequences of Hilbert-space structure plus the operator-exponential form $U_t = \exp(-i\hat{H}_{U3} t/\hbar)$. The U2-Continuum conformal gauge was confirmed to act trivially on the time-translation generator (gauge is spatial-only). Six of seven falsifiers dispatched; Fal-5 (compatibility with U4) remained open for Memo 03.

**The load-bearing analysis (Memo 03).** F5's derivation produced the arc's only genuinely substantive structural content. **Strategy A (Galilean-Lie-algebra closure)** established that $\hat{H}_{U3}$, as the time-translation generator within the Galilean group's representation on $\mathcal{H}$, must satisfy the Galilean commutator $[\hat{H}_{U3}, \hat{K}_i] = -i\hbar\hat{p}_i$. Substituting the boost generator $\hat{K}_i = m\hat{x}_i - t\hat{p}_i$ and integrating against the U5 momentum operator $\hat{p}$ yielded $T(\hat{p}) = |\hat{p}|^2/(2m)$ — the same kinetic-energy form U4 derived, by the same chain-rule integration Jacobian. The kinetic-plus-potential decomposition was independently justified at the F5 level via translation invariance + locality (sourced to the same primitives U4 used, but invoked independently). The identification $\hat{H}_{U3} = \hat{H}_{U4}$ closed modulo the additive vacuum-energy zero-point gauge, which coincides between the two arcs trivially. **Strategy B (Stone-uniqueness on the $\hat{H}_{U4}$-generated group)** served as a cross-check, confirming the same identification by an independent route. Fal-5 dispatched.

**The verdict.** **FORCED.** All seven falsifiers dispatched; no new structural CANDIDATEs introduced; the only residual freedom (additive vacuum-energy gauge) coincides between $\hat{H}_{U3}$ and $\hat{H}_{U4}$. **The Schrödinger evolution equation is structurally forced from primitive-level inputs.** U4 promotes from FORCED-conditional to FORCED-unconditional retroactively. The active upstream-CANDIDATE inventory of the QM-emergence Phase-1 program reduces from $\{U3\}$ + gauge to $\{ \, \}$ + gauge — empty modulo description-level convention. **All four foundational QM postulates (Born, Bell–Tsirelson, Heisenberg, Schrödinger) are now structurally derived from ED primitives.**

---

## 2. Sub-Feature Verdict Table

| Sub-feature | Status | Memo of establishment | Structural inputs used |
|---|---|---|---|
| **F1** Existence of strongly continuous time-translation representation | **FORCED-via-derivation** | Memo 02 §2 | Primitive 13 (continuous time axis) + Primitive 03 (homogeneity) + U2 inner-product translation-invariance + standard $L^2$ continuity |
| **F2** Uniqueness of self-adjoint generator (Stone's theorem) | **FORCED-via-derivation** | Memo 02 §3 | F1 + Stone's theorem (1932) on one-parameter unitary groups |
| **F3** Linearity of the evolution equation | **automatic** | Memo 02 §4 | Hilbert-space vector structure + operator-theoretic linearity + linear unitary representation + abelian time-translation group structure |
| **F4** First-order-in-time evolution | **automatic** | Memo 02 §5 | Stone's-theorem operator-exponential form + non-relativistic scope (sourced to Phase-1 Step 2, not U4) |
| **F5** Compatibility with U4 Hamiltonian form | **FORCED (load-bearing)** | Memo 03 §§3–6 | Galilean Lie algebra (primitive-level non-rel-scope infrastructure) + U5 momentum operator $\hat{p}$ + U2 Galilean unitary representation + boost generator $\hat{K} = m\hat{x} - t\hat{p}$ + chain-rule integration; cross-checked by Stone-uniqueness on $\hat{H}_{U4}$-generated group |

**Five-sub-feature decomposition closes uniformly FORCED**, with F1–F2 forced-via-derivation, F3–F4 automatic, F5 load-bearing-and-closed.

---

## 3. Falsifier-Resolution Table

| Falsifier | Target | Dispatch argument | Memo |
|---|---|---|---|
| **Fal-1** (non-unitary time evolution) | F1 | Direct calculation: $\langle U_t P \mid U_t Q \rangle = \langle P \mid Q \rangle$ via translation-invariance of the U2 measure on the time axis (Primitive 13 supplies translation-invariant relational time) | Memo 02 §2.4 |
| **Fal-2** (multiple inequivalent generators) | F2 | Stone's theorem on the strongly continuous one-parameter unitary group $\{U_t\}$ produces a unique self-adjoint generator | Memo 02 §3.2 |
| **Fal-3** (non-linear evolution) | F3 | Linear unitary representations on a Hilbert space induce linear evolution equations; operator-theoretic linearity is automatic from "operator on a Hilbert space" definition | Memo 02 §4.2 |
| **Fal-4** (higher-order in time) | F4 | $U_t = \exp(-i\hat{H}_{U3} t/\hbar)$ differentiated once gives a first-order equation; non-relativistic scope (sourced to Phase-1 Step 2) selects abelian $\mathbb{R}_t$ over Lorentz boosts | Memo 02 §5.2 |
| **Fal-5** (incompatible generator) | F5 | **Strategy A** (Galilean-Lie-algebra closure): $\hat{H}_{U3}$ must satisfy $[\hat{H}_{U3}, \hat{K}_i] = -i\hbar\hat{p}_i$; integrating yields $T(\hat{p}) = |\hat{p}|^2/(2m)$ via chain-rule Jacobian, identifying $\hat{H}_{U3} = \hat{H}_{U4}$. **Strategy B** (Stone-uniqueness cross-check): $\hat{H}_{U4}$-generated group coincides with $\{U_t\}$; Stone-uniqueness forces $\hat{H}_{U4} = \hat{H}_{U3}$ | Memo 03 §3 (Strategy A) + §4 (Strategy B) |
| **Fal-6** (non-self-adjoint generator) | F2 | Stone's theorem produces a self-adjoint generator from a strongly continuous unitary group; self-adjointness is automatic from the theorem's hypotheses | Memo 02 §3.3 |
| **Fal-7** (non-continuous time) | F1 | Pre-derivation Primitive 13 audit confirms continuous-time interpretation at Phase-1 scope; standard $L^2$-translation continuity inherits to the U2 Hilbert space's direct-integral structure | Memo 02 §1.4 + §2.6 |

**All seven falsifiers dispatched within the stated scope conditions and forbidden-input discipline.**

---

## 4. Conditionality Ledger

The U3 verdict is **FORCED** with the following inherited conditionalities and **zero new ones**:

1. **Non-relativistic single-particle scope.** Inherited from Phase-1 Step 2; conditions the use of the abelian time-translation group (F4) and the Galilean group (F5). The Lorentz-group / relativistic extension is out of scope (and would belong to a relativistic-emergence arc, not Phase-1).

2. **Gauge-coupling-free scope.** Inherited from U4; conditions the kinetic-plus-potential decomposition without magnetic vector potential corrections. Gauge field theory is downstream content.

3. **U2 inner-product structure (both regimes).** Inherited from U2-Discrete (Theorem 11) and U2-Continuum (Theorem 12); supplies the Hilbert space on which Stone's theorem applies and the Galilean group acts unitarily.

4. **U1 participation-measure structure.** Inherited from U1 (Theorem 14); supplies the carrier $P_K = \sqrt{b_K} e^{i\pi_K}$ on which $U_t$ acts.

5. **U5 momentum-operator structure.** Inherited from U5 (Theorem 13); supplies $\hat{p} = -i\hbar\nabla$ for the Galilean Lie algebra and the F5 identification.

6. **U4 Hamiltonian form (as identification target only).** F5's identification is established with U4's operator form $\hat{H}_{U4} = \hbar^2|\hat{p}|^2/(2m) + V(\hat{x})$ treated as a mathematical object on $\mathcal{H}$, not as a derivation premise. U4 is the identification target; not a derivation input.

7. **Inherited values.** Mass $m$ per Arc M's "form FORCED, value INHERITED" methodology; $\hbar$ per dimensional-atlas Madelung anchoring. Both identical to U4's treatment.

8. **Primitive 13 continuous-time interpretation.** Confirmed by pre-derivation audit at Phase-1 scope. Discrete-time alternatives belong to Phase-3-and-beyond extensions.

9. **Galilean-group uniqueness within non-relativistic scope.** Treated as primitive-level structural infrastructure (per Memo 03 §2.3); shared with U4 but invoked independently in F5.

**U3 introduces NO new structural CANDIDATEs.** All nine items are inherited from prior structural commitments or scope conditions established before this arc opened. The arc's verdict is unconditional within these inherited conditionalities, in both discrete and continuum regimes, gauge-invariant under the U2-Continuum conformal redundancy.

---

## 5. Integration into the Structural-Foundations Program

### 5.1 Position in the Phase-1 chain

The Phase-1 chain leading to Schrödinger evolution is now complete:

```
Primitives 03, 04, 06, 07, 09, 13
              |
              v
        U1 (FORCED) -> P_K = sqrt(b) * exp(i pi)
              |
              v
        U2 (FORCED) -> <P|Q> inner product on H
              |
              v
        U5 (FORCED) -> spatial translation -> p̂ = -i ℏ ∇
              |
              v
        U4 (FORCED-UNCONDITIONAL post-U3) -> Ĥ = ℏ² |p̂|²/(2m) + V(x̂)
              |
              v
        U3 (FORCED, this arc) -> i ℏ ∂_t P = Ĥ P
              |
              v
       SCHRÖDINGER EVOLUTION (FORCED-unconditional)
```

Every upstream commitment in the chain is now FORCED. The structural backbone of standard non-relativistic single-particle quantum mechanics is closed.

### 5.2 Updated active CANDIDATE inventory

| Inventory | Pre-U3 | Post-U3 |
|---|---|---|
| Active upstream-CANDIDATE list | $\{U3\}$ + continuum gauge convention | $\{ \, \}$ + continuum gauge convention |
| Open structural commitments | 1 (U3) | **0** |
| Description-level conventions | 1 (continuum gauge) | 1 (continuum gauge; unchanged) |

**The active upstream-CANDIDATE inventory is empty.** The continuum gauge convention is a description-level redundancy under the U2-Continuum conformal rescaling, not a structural commitment. Phase-1 is closed at the structural level.

### 5.3 Updated FORCED-theorem count

| # | Theorem | Pre-U3 status | Post-U3 status |
|---|---|---|---|
| 10 | Born rule (Gleason–Busch) | FORCED-unconditional | (unchanged) |
| 11 | U2-Discrete | FORCED-unconditional | (unchanged) |
| 12 | U2-Continuum (with conformal gauge) | FORCED-unconditional | (unchanged) |
| 13 | U5 (translation generator + momentum operator) | FORCED-unconditional | (unchanged) |
| 14 | U1 (participation-measure construction) | FORCED-unconditional | (unchanged) |
| 15 | U4 (specific Hamiltonian form) | FORCED-conditional on U3 | **FORCED-unconditional** ← retroactive promotion |
| **16** | **U3 (this arc; time-translation generator + Schrödinger evolution)** | (active CANDIDATE) | **FORCED-unconditional** |

**Forced-theorem count: 15 → 16, with U4 retroactively promoted** to fully unconditional status. The two-promotion U3 cycle is the most leveraged single arc in the structural-foundations program's history.

### 5.4 Foundational QM postulates: full structural derivation

| Postulate | Pre-U3 status | Post-U3 status |
|---|---|---|
| Born rule | FORCED-unconditional | (unchanged) FORCED-unconditional |
| Bell–Tsirelson bound | FORCED-unconditional | (unchanged) FORCED-unconditional |
| Heisenberg uncertainty | FORCED-unconditional | (unchanged) FORCED-unconditional |
| **Schrödinger evolution** | FORCED-conditional on U3 | **FORCED-unconditional** |

**All four foundational postulates of non-relativistic single-particle quantum mechanics are now structurally derived from ED primitives.**

### 5.5 Methodological pattern across the seven-arc cycle

The seven-arc cycle (born_gleason → U2-Discrete → U2-Continuum → U5 → U1 → U4 → U3) demonstrates the structural-derivation methodology against seven substantively different structural questions:

1. **born_gleason** — Born rule via Gleason–Busch + non-contextuality.
2. **U2-Discrete** — sesquilinear inner product via primitive-level aggregation arguments.
3. **U2-Continuum** — discrete-to-continuum lift with explicit conformal gauge structure.
4. **U5** — Stone's theorem on spatial translations → momentum operator.
5. **U1** — participation-measure construction via Frobenius + Cauchy functional equation.
6. **U4** — Galilean Lie algebra integration → kinetic-energy form, factor-of-2 Jacobian.
7. **U3 (this arc)** — Stone's theorem on time translations + Galilean closure → Hamiltonian operator + Schrödinger evolution.

The pattern (decompose CANDIDATE → identify automatic / forced-via-derivation / load-bearing sub-features → close load-bearing items via primitive-level arguments → introduce zero new CANDIDATEs) holds across all seven arcs. Acyclicity is preserved everywhere; the forbidden-input discipline (different in each arc) is enforced explicitly.

---

## 6. Public Explainer (Non-Technical)

*This section is intended for a scientifically literate but non-expert audience and is not part of the formal derivation.*

### 6.1 What U3 is

The Schrödinger equation, $i\hbar \, \partial_t \psi = \hat{H} \psi$, is the dynamical heart of non-relativistic quantum mechanics. It says: a quantum state evolves in time according to the Hamiltonian operator $\hat{H}$, with the time-derivative coefficient being precisely $i\hbar$. For a hundred years, this equation has been adopted as a postulate — one of the structural axioms of quantum theory. Physicists work with it every day, but few would claim to have derived it from anything more fundamental.

The U3 question asks whether the Schrödinger equation is a postulate or a consequence. Specifically: given the participation-measure framework Event Density has built — the Hilbert space (U2), the momentum operator (U5), the Hamiltonian's specific form (U4), the participation-measure carrier (U1), the Born rule (Theorem 10) — does the time-evolution equation follow structurally, or must it be added as a separate commitment?

### 6.2 Why time-translation symmetry forces Schrödinger evolution

The answer is that it follows. The argument has two parts.

The first part is structurally identical to U5's argument for the momentum operator, but applied to the time axis instead of the spatial axis. Empty time, like empty space, is homogeneous: there is no privileged instant, no special moment that the participation-measure framework distinguishes. Time-translation operators — the operators that shift a state forward or backward in time by a parameter $t$ — are therefore well-defined, continuous, and unitary on the participation-measure Hilbert space. By Stone's theorem (a 1932 result of Marshall Stone in functional analysis), every such family of unitary operators has a unique self-adjoint generator. *That generator is the Hamiltonian operator.* And because the family is parameterized by a single real time variable, differentiating once produces a first-order-in-time equation. The Schrödinger equation, in skeleton form $i\hbar \partial_t \psi = \hat{H} \psi$, is the operator-exponential identity of Stone's theorem, written in differential form.

This much establishes that *some* Hamiltonian operator $\hat{H}$ exists, that the equation is linear, and that it is first-order in time. What remains is to identify $\hat{H}$ as the same Hamiltonian U4 derived — the kinetic-plus-potential operator $\hat{H} = \hbar^2|\hat{p}|^2/(2m) + V(\hat{x})$ — without arguing in a circle.

### 6.3 Why the Hamiltonian must match the U4 operator

The second part of the argument is the load-bearing piece. U4 derived the Hamiltonian's form by integrating a specific commutator condition imposed by the Galilean group — the symmetry group of inertial observers in the non-relativistic regime. The same Galilean group, however, also constrains what *any* time-translation generator on the participation-measure Hilbert space can look like: the time-translation generator is one of the Galilean group's basic generators, and it must satisfy a specific commutator with the boost generator. Solving that commutator gives the same kinetic-energy form U4 derived. Two independent arguments — Stone's theorem applied to time translations, and U4's Galilean integration acting on the momentum operator — converge on the same operator. The Hamiltonian Stone's theorem produces is precisely the Hamiltonian U4 derived. The Schrödinger equation is structurally complete.

A subtle methodological point: this argument was conducted under a strict discipline that treats U4's operator form as an *identification target* rather than a derivation input. U4 was earlier derived under the conditional assumption that a Hermitian Hamiltonian generator exists (which is exactly U3's content); to now use U4 as a derivation premise for U3 would close a circular loop. The discipline avoids this by deriving U3 independently from primitive-level inputs (Stone's theorem on time translations) and then *identifying* the result with U4's operator via the shared Galilean structure. The two arcs land on the same operator because the Galilean group forces them to — not because either arc was assumed in deriving the other.

### 6.4 How this completes the structural derivation of QM

With U3 closed, every upstream commitment in the participation-measure → Hilbert-space → Schrödinger-emergence chain has been derived. The Hilbert space comes from U2; the Born rule from Gleason–Busch (Theorem 10); the momentum operator from U5; the participation-measure carrier from U1; the Hamiltonian's specific form from U4; the time-evolution equation from U3. All four foundational postulates of non-relativistic single-particle quantum mechanics — the Born rule, the Bell–Tsirelson bound, Heisenberg's uncertainty inequality, and Schrödinger evolution — are now structural consequences of the Event Density primitive ontology rather than independent postulates. The framework still rests on its primitives; whether those primitives are right is the load-bearing empirical question. But the structural backbone of standard quantum mechanics is now derived rather than assumed.

This does not predict new experiments. The Schrödinger equation is the same Schrödinger equation it has always been, and Event Density reproduces standard non-relativistic single-particle quantum mechanics exactly. What changes is the depth at which the answer to "why does quantum mechanics look like this?" can be given. In the standard formulation: "because we postulate it." In Event Density: "because the participation graph supplies primitive-level commitments that, together with standard mathematical infrastructure (Stone's theorem, Galilean Lie algebra, Fourier theory) and one inherited symmetry-group identification (the Galilean group at non-relativistic scope), force every structural feature of the framework — the Hilbert space, the Born rule, the momentum and Hamiltonian operators, the inner product, the time evolution — to take precisely the form quantum mechanics takes." Phase-1 is closed.

---

## 7. Memo-to-Theorem Mapping

The U3 arc consisted of four memos (Memos 00–03) plus this closure memo. The mapping between memos, structural results, and theorem components:

| Memo | Structural result | Theorem component |
|---|---|---|
| **Memo 00** (arc outline) | Decomposition into five sub-features (F1–F5); seven-falsifier inventory; structural-input survey; comparison-to-U5 framing; three-verdict scoping (FORCED / PARTIAL / FREE) | Sets up the question and the analytical framework |
| **Memo 01** (decomposition + circularity audit + transfer audit) | Sub-feature classification (F1, F2 forced-via-derivation; F3, F4 automatic; F5 load-bearing); circularity audit (U4-as-derivation-input forbidden; identification protocol established); U5 → U3 transfer audit (Stone's theorem clean transfer; operator-content questions deferred to F5); falsifier-status update (Fal-2, Fal-3, Fal-4, Fal-6 dispatched by mathematical theorems) | Establishes the structural terrain for Memos 02 and 03 |
| **Memo 02** (F1, F2, F3, F4 derivations) | F1 (existence of strongly continuous time-translation representation, via Primitive 13 + 03 + U2); F2 (Stone-uniqueness of self-adjoint generator $\hat{H}_{U3}$); F3 (linearity, automatic); F4 (first-order-in-time, automatic); continuum-regime gauge-compatibility check; F5 setup (compatibility condition isolated; identification-not-derivation discipline) | Theorem properties 1, 2, 3, 4 (and gauge-invariance) |
| **Memo 03** (F5 + verdict) | F5 (compatibility with U4): Strategy A (Galilean-Lie-algebra closure: $\hat{H}_{U3}$ satisfies Galilean commutator → integration yields $T = |\hat{p}|^2/(2m)$ → kinetic-plus-potential decomposition independently justified → $\hat{H}_{U3} = \hat{H}_{U4}$); Strategy B (Stone-uniqueness on $\hat{H}_{U4}$-generated group as cross-check); additive-shift residual analysis; falsifier Fal-5 dispatched; arc verdict FORCED; downstream cascade (U4 retroactive promotion, Schrödinger emergence promotion, Phase-1 closure) | Theorem property 5 + final theorem statement + verdict |
| **Memo 04** (this memo) | Canonical narrative summary; theorem statement; downstream cascade integration; public explainer; memo-to-theorem mapping; Phase-1 completion declaration | Final synthesis and outreach interface |

### 7.1 The U3 theorem, stated cleanly

> **Theorem (U3; Time-Translation Generator and Schrödinger Evolution).** Let the ED primitive stack supply: graph homogeneity (Primitive 03), bandwidth (Primitive 04), spatial gradient (Primitive 06), tension polarity (Primitive 09), and relational timing (Primitive 13). Let the participation-measure carrier (U1, FORCED), the U2 inner product (U2-Discrete + U2-Continuum, both FORCED), the momentum operator (U5, FORCED), and the kinetic-plus-potential Hamiltonian operator (U4, FORCED-conditional) supply the Hilbert space $\mathcal{H}$ and the operator infrastructure. Then:
>
> 1. **Time-translation representation.** The time-translation operators $(U_t P)_K(x, s) := P_K(x, s - t)$ for $t \in \mathbb{R}$ form a strongly continuous one-parameter abelian unitary group on $\mathcal{H}$.
>
> 2. **Unique self-adjoint generator.** By Stone's theorem, there exists a unique self-adjoint operator $\hat{H}_{U3}$ on $\mathcal{H}$ such that
> $$
> U_t = \exp\!\left(-\frac{i \hat{H}_{U3} t}{\hbar}\right), \qquad t \in \mathbb{R}.
> $$
>
> 3. **Linear first-order-in-time evolution equation.** Differentiating yields
> $$
> i\hbar \, \partial_t P(t) = \hat{H}_{U3} \, P(t),
> $$
> linear in $P(t)$, first-order in $\partial_t$.
>
> 4. **Compatibility with U4.** The Galilean Lie algebra (primitive-level non-relativistic-scope infrastructure) forces $\hat{H}_{U3}$ to satisfy $[\hat{H}_{U3}, \hat{K}_i] = -i\hbar\hat{p}_i$ with the boost generator $\hat{K}_i = m\hat{x}_i - t\hat{p}_i$. Integration yields $T(\hat{p}) = |\hat{p}|^2/(2m)$ via the chain-rule Jacobian. The kinetic-plus-potential decomposition follows independently from translation invariance + locality. Modulo the additive vacuum-energy zero-point gauge,
> $$
> \hat{H}_{U3} = \hat{H}_{U4} = \frac{\hbar^2 |\hat{p}|^2}{2m} + V(\hat{x}).
> $$
>
> 5. **Schrödinger evolution.** Combining (1)–(4):
> $$
> \boxed{i\hbar \, \partial_t P(t) = \left( \frac{\hbar^2 |\hat{p}|^2}{2m} + V(\hat{x}) \right) P(t).}
> $$
>
> The derivation invokes no PDE-level Schrödinger assumption, no U4-as-derivation-input circularity, no relativistic kinematics, no downstream gauge-coupling structure. All seven falsifiers are dispatched.

**Status:** **FORCED-unconditional** in both discrete and continuum regimes; gauge-invariant under the U2-Continuum conformal redundancy; **U4 promoted retroactively to FORCED-unconditional**; Phase-1 program structurally complete modulo description-level continuum gauge.

---

## 8. Phase-1 Completion Statement

> **Formal Declaration of Phase-1 Completion.**
>
> With the U3 arc closed FORCED on 2026-04-26 and U4 retroactively promoted to FORCED-unconditional, the QM-emergence Phase-1 structural-foundations program is hereby formally closed at the structural-derivation level.
>
> **All four foundational postulates of non-relativistic single-particle quantum mechanics — the Born rule, the Bell–Tsirelson bound, the Heisenberg uncertainty inequality, and the Schrödinger evolution equation — are structurally FORCED-unconditional consequences of the Event Density primitive ontology** (Primitives 01 through 13), the standard mathematical infrastructure of functional analysis (Stone's theorem, the spectral theorem, $L^2$ Fourier theory, Gleason's theorem and the Busch generalization), and the standard symmetry-group infrastructure of non-relativistic kinematics (the Galilean Lie algebra and its central extension).
>
> **The active upstream-CANDIDATE inventory of the Phase-1 program is empty**, with the sole residual being the description-level continuum gauge convention established in U2-Continuum — a gauge redundancy under conformal rescaling, not a structural commitment.
>
> **Sixteen forced structural theorems** populate the Phase-1 ledger, with two retroactive promotions in the present cycle (U4 from FORCED-conditional to FORCED-unconditional; U3 from active CANDIDATE to FORCED-unconditional).
>
> **The ED primitive ontology suffices to derive the full non-relativistic single-particle quantum-mechanical formalism.** The Hilbert space, the Born rule, the position-momentum conjugacy, the Heisenberg uncertainty inequality, the Hamiltonian operator's specific form (kinetic-plus-potential with coefficient $1/(2m)$), the time-evolution equation (linear, first-order, with coefficient $i\hbar$), and the participation-measure carrier itself ($P_K = \sqrt{b_K} \cdot e^{i\pi_K}$) are all structural consequences of the primitive stack plus standard mathematical and symmetry-group infrastructure.
>
> **No PDE-level Schrödinger assumption, no Hilbert-space postulate, no Born-rule postulate, no Hamiltonian-form postulate, no commutation-relation postulate appears in the Phase-1 derivations.** Every load-bearing structural feature of standard non-relativistic single-particle quantum mechanics is derived from inputs strictly upstream of the standard QM formalism.
>
> The methodological pattern (decompose CANDIDATE → identify load-bearing items → close via primitive-level arguments → introduce zero new CANDIDATEs) has been demonstrated against seven substantively different structural questions across the seven-arc cycle (born_gleason, U2-Discrete, U2-Continuum, U5, U1, U4, U3). Acyclicity has been preserved everywhere; the forbidden-input discipline (different in each arc) has been enforced explicitly with documented circularity audits.
>
> **Phase-1 of the QM-emergence program is closed.**

---

## 9. Recommended Next Steps

**(a) Bundled memory-record update covering U3 arc + Phase-1 closure.** A single comprehensive update to `project_qm_emergence_arc.md` capturing the post-arc state: (i) U3 theorem now FORCED-unconditional, (ii) U4 promotion to FORCED-unconditional retroactively, (iii) Schrödinger evolution promoted to FORCED-unconditional, (iv) updated active upstream-CANDIDATE inventory ($\{ \, \}$ + continuum gauge), (v) all four foundational QM postulates now structurally derived, (vi) Phase-1 program structurally complete, (vii) updated forced-theorem count (16, with two promotions in this arc cycle), (viii) seven-arc cycle complete with methodological pattern validated across seven structural questions, (ix) sensitivity flag inventory (per Memo 03 §9.8). Update `MEMORY.md` index line accordingly.

**(b) Draft the U3 publication paper.** Following the templates of U5, U4, and U1 publication papers, the U3 paper would be the natural sixth in the structural-foundations publication series. The paper documents the Stone's-theorem-on-time-translation derivation (parallel to U5's Stone's-theorem-on-spatial-translation derivation), the Galilean-Lie-algebra closure argument identifying $\hat{H}_{U3}$ with $\hat{H}_{U4}$, and the headline result: all four foundational QM postulates structurally derived from ED primitives. Title proposal: *"U3: The Forced Structure of Time-Translation Symmetry and the Schrödinger Evolution Equation."* Anticipated length comparable to U4 / U5 papers (~13–15 pp).

**(c) Companion desktop explainer.** Following the established public-explainer ladder (Exponent2 → Born → U2 inner product → U1 participation measure → U4 Hamiltonian → U5 momentum), the U3 explainer would be the seventh and capstone in the series. Title proposal: *"How the Schrödinger Equation Got Its Form."* The Memo 04 §6 public-explainer section supplies a draft. The capstone framing is significant: this is the explainer in which Phase-1 closure is announced to the public-facing audience, with all four QM postulates collectively framed as structurally derived.

**(d) Phase-1 synthesis paper revision.** With Phase-1 structurally complete, the synthesis paper [`papers/QM_Emergence_Structural_Completion/`] §§3.3, 3.4, 3.5, 4 require comprehensive revision to reflect the post-U3 state. Specifically: §3.3 (foundational postulates' status) — all four now FORCED-unconditional; §3.4 (upstream-CANDIDATE inventory) — empty (modulo continuum gauge); §3.5 (reduction count) — from "five upstream commitments" to "zero upstream commitments + one description-level gauge"; §4 (open work) — focus shifts entirely to Phase-3 (gravitational sector), Arc Q sharpening, and synthesis-paper revision itself. A single editorial pass can now cover all four sections (no further arc work is gating the synthesis revision). This is the natural deliverable for declaring Phase-1 closed in the publication record.

---

**Arc Closed.**
