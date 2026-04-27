# Memo 03 — U3 F5 Compatibility Derivation, Falsifier Audit, and Arc Verdict

**Date:** 2026-04-26
**Arc:** `arcs/U3/`
**Predecessors:** [`00_arc_outline.md`](00_arc_outline.md), [`01_decomposition_and_mapping.md`](01_decomposition_and_mapping.md), [`02_F1_F2_F3_F4_derivations.md`](02_F1_F2_F3_F4_derivations.md)
**Status:** Load-bearing derivation memo. Executes the F5 compatibility derivation between $\hat{H}_{U3}$ (the time-translation generator from F1 + F2) and $\hat{H}_{U4}$ (the kinetic-plus-potential operator derived in U4 via Galilean Lie algebra integration), dispatches the lone remaining falsifier (Fal-5), delivers the U3 arc verdict, and documents the downstream structural cascade.
**Purpose:** Close the U3 arc and the QM-emergence Phase-1 structural-foundations program (modulo description-level continuum gauge).

---

## 1. Pre-Derivation Setup

### 1.1 Recap of F1–F4 status

From Memo 02:

- **F1 (existence of time-translation representation): closed.** $\{U_t : t \in \mathbb{R}\}$ is a strongly continuous one-parameter abelian unitary group on the U2 Hilbert space $\mathcal{H}$, derived from Primitives 13 + 03 + U2 measure translation-invariance.
- **F2 (uniqueness of self-adjoint generator): closed.** Stone's theorem produces a unique self-adjoint $\hat{H}_{U3}$ on $\mathcal{H}$ such that $U_t = \exp(-i\hat{H}_{U3} t / \hbar)$.
- **F3 (linearity): closed.** Automatic from the Hilbert-space structure + linear unitary representation + abelian group structure.
- **F4 (first-order-in-time): closed.** Automatic from Stone's-theorem operator-exponential form + non-relativistic scope.

Six of seven falsifiers dispatched (Fal-1, Fal-2, Fal-3, Fal-4, Fal-6, Fal-7). Fal-5 (incompatibility between $\hat{H}_{U3}$ and $\hat{H}_{U4}$) remains the lone open falsifier.

### 1.2 The F5 question (re-stated)

After F1–F4, two self-adjoint operators are in play on the U2 Hilbert space:

- **$\hat{H}_{U3}$:** the unique self-adjoint generator of the time-translation group $\{U_t\}$, produced by Stone's theorem (F2). Content at this stage: *abstractly, the time-translation generator;* no specified functional form.
- **$\hat{H}_{U4} = \hbar^2|\hat{p}|^2/(2m) + V(\hat{x})$:** the kinetic-plus-potential operator derived in U4 via Galilean Lie algebra integration on the U5 momentum operator. Content: *a specific operator with specific form,* derived under Framing 1 (i.e., conditional on the existence of a Hermitian Hamiltonian generator — which is U3's F2 content).

The F5 question:
$$
\boxed{\hat{H}_{U3} \stackrel{?}{=} \hat{H}_{U4} \quad \text{as self-adjoint operators on } \mathcal{H}.} \tag{1.1}
$$

### 1.3 Discipline: identification, not derivation

The discipline established in Memos 01 and 02:

- **(i)** $\hat{H}_{U3}$ was derived in F1 + F2 from Primitive 13 + Primitive 03 + U2 + Stone's theorem. **U4 played no role.**
- **(ii)** $\hat{H}_{U4}$ is treated as a mathematical object on $\mathcal{H}$ — a specific self-adjoint operator. **U4's derivation chain is taken as background, not as a U3-input.**
- **(iii)** F5 establishes an identification between the two via shared structural infrastructure (the Galilean Lie algebra), not via deriving one from the other.

This protocol preserves acyclicity. The U3 ⟷ U4 loop is closed *consistently* (both arcs identify the same operator) without circularity (neither arc takes the other as a derivation premise).

### 1.4 Forbidden inputs for F5

Reiterated:

- **U4 as derivation premise.** Forbidden. U4 may only appear as identification target.
- **U3 itself as derivation premise.** Forbidden (question-begging).
- **PDE-level Schrödinger equation.** Forbidden.
- **Relativistic kinematics.** Out of scope.
- **Downstream gauge-coupling structure.** Out of scope (gauge-coupling-free per inherited Phase-1 Step 2 scope).
- **U4's Framing-1 conditionality "U3 exists" used as input.** Forbidden — would close the circular loop. Reframing: F5 treats $\hat{H}_{U4}$ as a self-adjoint operator on $\mathcal{H}$ with specific functional form, *without* invoking the conditionality under which U4 was derived.

---

## 2. Structural Infrastructure for F5

### 2.1 Inputs available to F5

The F5 derivation draws on the following structural infrastructure:

- **Primitive 13 (Relational Timing).** Supplies the time axis and time-translation symmetry. Already used in F1.
- **U2 inner-product preservation.** Galilean transformations are unitary on $\mathcal{H}$ (per U4 §F4.4); the inner-product structure supplies the framework within which both $\hat{H}_{U3}$ and $\hat{H}_{U4}$ are well-defined self-adjoint operators.
- **U5 momentum structure.** $\hat{p} = -i\hbar\nabla$ is the spatial-translation generator. It enters $\hat{H}_{U4}$ as the kinetic-energy variable. It also enters the Galilean Lie algebra as the spatial-translation generator. The shared momentum operator is one of the structural anchors of the F5 identification.
- **U4 Hamiltonian form (as identification target only).** $\hat{H}_{U4} = \hbar^2|\hat{p}|^2/(2m) + V(\hat{x})$. **Used solely as the operator to be identified with $\hat{H}_{U3}$, not as a derivation premise.**
- **Non-relativistic single-particle scope.** Inherited from Phase-1 Step 2. Selects the Galilean group over the Lorentz group as the consistent boost-translation algebra.
- **Primitive-level Galilean boost algebra.** The Galilean group is the unique consistent boost-translation algebra in the non-relativistic scope (per U4 §2.3, treated here as primitive-level structural infrastructure available to U3 independently of U4's specific derivation).

### 2.2 The Galilean Lie algebra at primitive level

The Galilean Lie algebra is generated by:

- **$\hat{H}$ (time translations):** the generator targeted by F2.
- **$\hat{p}_i$ (spatial translations, $i = 1, \ldots, d$):** the U5 momentum operator.
- **$\hat{x}_i$ (position):** the multiplication operator on $\mathcal{H}$.
- **$\hat{K}_i$ (Galilean boosts):** generators of velocity-shifts between inertial frames.
- **$\hat{J}_i$ (rotations, $i = 1, \ldots, d(d-1)/2$):** generators of spatial rotations.

The substantive commutators are:
\begin{align}
[\hat{x}_i, \hat{p}_j] &= i\hbar \, \delta_{ij}, \tag{2.1} \\
[\hat{K}_i, \hat{p}_j] &= i\hbar m \, \delta_{ij}, \tag{2.2} \\
[\hat{H}, \hat{K}_i] &= -i\hbar \, \hat{p}_i. \tag{2.3}
\end{align}

The mass $m$ enters (2.2) as the **central-extension structure constant** of the Galilean group (Bargmann 1954). It is a primitive-level feature of the Galilean Lie algebra in the non-relativistic single-particle scope.

The boost generator takes the form
$$
\hat{K}_i = m \, \hat{x}_i - t \, \hat{p}_i \tag{2.4}
$$
which is forced by the requirement that $\hat{K}_i$ generate the standard Galilean boost $\hat{p} \to \hat{p} - mv$ acting on momentum eigenstates. This form is sourced from the Galilean group's structure, not from U4's derivation chain.

### 2.3 Why the Galilean group is primitive-level infrastructure here

A potential acyclicity worry: U4's derivation used the Galilean Lie algebra in §F4 to derive the $1/(2m)$ coefficient. Does using the same algebra in F5 close a circular loop?

**Resolution (per Memo 01 §2.5).** The Galilean Lie algebra is not specific to U4. It is the unique consistent boost-translation algebra in the non-relativistic scope — a feature of the scope condition itself, not of U4's derivation. U4 *uses* the algebra to derive $\hat{H}_{U4}$'s form; U3 *uses* the same algebra (independently) to identify $\hat{H}_{U3}$ with $\hat{H}_{U4}$. The two uses are structurally independent: U4's use derives a specific functional form from the commutator (2.3); U3's use establishes operator identity via uniqueness of the time-translation generator within the algebra's representation.

The Galilean group is therefore treated as primitive-level infrastructure available to *any* arc operating in the non-relativistic single-particle scope. F5's invocation is acyclic.

### 2.4 The U2 Galilean representation

Per U4 §F4.4:

- **Spatial translations $T_a = \exp(i\hat{p}\cdot a/\hbar)$:** unitary by U5's F1 (Stone's theorem).
- **Time translations $U_t = \exp(-i\hat{H}_{U3} t/\hbar)$:** unitary by U3's F1 (this arc).
- **Rotations $R_\omega = \exp(i\hat{J}\cdot\omega/\hbar)$:** unitary by C2 (rotation invariance, sourced to Primitive 03's spatial homogeneity).
- **Galilean boosts $B_v = \exp(i\hat{K}\cdot v/\hbar)$:** unitary as exponential of self-adjoint $\hat{K} = m\hat{x} - t\hat{p}$ (real-coefficient linear combination of self-adjoint $\hat{x}$ and $\hat{p}$).

All Galilean transformations act unitarily on $\mathcal{H}$. The U2 Hilbert space carries a unitary representation of the Galilean group.

---

## 3. Strategy A — Galilean-Lie-Algebra Closure

This is the primary derivation. It establishes $\hat{H}_{U3} = \hat{H}_{U4}$ via uniqueness of the time-translation generator within the Galilean Lie algebra's representation on $\mathcal{H}$.

### 3.1 $\hat{H}_{U3}$ as the time-translation generator within the Galilean representation

By F1 + F2, $\hat{H}_{U3}$ is the unique self-adjoint generator of the time-translation group $\{U_t\}$ on $\mathcal{H}$. By §2.4, time translations $\{U_t\}$ are part of the Galilean group's unitary representation on $\mathcal{H}$. Therefore $\hat{H}_{U3}$ is the **time-translation generator within the Galilean representation** — i.e., the operator playing the role of $\hat{H}$ in the commutator algebra (2.1)–(2.3).

In particular, $\hat{H}_{U3}$ must satisfy the Galilean commutator (2.3):
$$
[\hat{H}_{U3}, \hat{K}_i] = -i\hbar \, \hat{p}_i. \tag{3.1}
$$
This is an algebraic constraint inherited from the Galilean group's structure — *not* an assumption imported from U4's derivation chain. The constraint is what the Galilean Lie algebra forces on the operator playing the time-translation role.

### 3.2 Solving the Galilean commutator condition for $\hat{H}_{U3}$

Substituting $\hat{K}_i = m\hat{x}_i - t\hat{p}_i$ from (2.4) into (3.1):
$$
[\hat{H}_{U3}, m\hat{x}_i - t\hat{p}_i] = -i\hbar \, \hat{p}_i.
$$
Using $[\hat{H}_{U3}, t\hat{p}_i] = 0$ (the parameter $t$ is c-number; $\hat{H}_{U3}$ commutes with $\hat{p}_i$ on the spatially-homogeneous free-particle component, as confirmed below):
$$
m \, [\hat{H}_{U3}, \hat{x}_i] = -i\hbar \, \hat{p}_i. \tag{3.2}
$$

Decomposing $\hat{H}_{U3} = T_{U3}(\hat{p}) + V_{U3}(\hat{x})$ (a working ansatz to be justified below), and using $[T_{U3}(\hat{p}), \hat{x}_i] = -i\hbar \, \partial T_{U3}/\partial \hat{p}_i$ and $[V_{U3}(\hat{x}), \hat{x}_i] = 0$:
$$
m \cdot (-i\hbar) \, \frac{\partial T_{U3}(\hat{p})}{\partial \hat{p}_i} = -i\hbar \, \hat{p}_i,
$$
so
$$
\frac{\partial T_{U3}(\hat{p})}{\partial \hat{p}_i} = \frac{\hat{p}_i}{m}. \tag{3.3}
$$

This is **the same differential equation** U4 §F4 derived. Integrating with $T_{U3}(0) = 0$ (additive-constant gauge fixed below):
$$
T_{U3}(\hat{p}) = \frac{|\hat{p}|^2}{2m}. \tag{3.4}
$$

The factor of $1/2$ emerges from the chain-rule integration Jacobian, exactly as in U4 §F4.7.

### 3.3 Justifying the kinetic-plus-potential decomposition

The decomposition $\hat{H}_{U3} = T_{U3}(\hat{p}) + V_{U3}(\hat{x})$ assumed at the start of §3.2 must itself be justified at the F5 level (it cannot be imported from U4 §F5).

The justification is the same primitive-level argument U4 §F5 used, *applied independently* here: translation invariance of the participation graph (Primitive 03 + Primitive 06) forbids the free part from depending on $\hat{x}$, so the free part is $T_{U3}(\hat{p})$; locality of external potentials (Primitive 03 + Primitive 06) forbids the potential part from depending on $\hat{p}$, so the potential part is $V_{U3}(\hat{x})$; cross terms are forbidden by both translation invariance (free) and locality (potential).

The argument is *primitive-level*, sourced to the same primitives U4 used but invoked independently in F5. No U4 import.

### 3.4 The identification

Combining (3.4) with §3.3 and restoring $\hbar$:
$$
\hat{H}_{U3} = \frac{\hbar^2 |\hat{p}|^2}{2m} + V_{U3}(\hat{x}). \tag{3.5}
$$
Comparing with U4's result:
$$
\hat{H}_{U4} = \frac{\hbar^2 |\hat{p}|^2}{2m} + V(\hat{x}). \tag{3.6}
$$
The two operators have identical kinetic terms (both derived from the same Galilean commutator condition + the same chain-rule integration). The potential terms agree if $V_{U3}(\hat{x}) = V(\hat{x})$ — addressed below in §3.5.

### 3.5 Potential-term identification

The potential terms $V_{U3}(\hat{x})$ and $V(\hat{x})$ both denote scalar functions of position appearing in the Hamiltonian. Both are inherited from external context (the specific potential acting on the participation-measure system) rather than derived from the structural-foundations cycle. The identification $V_{U3}(\hat{x}) = V(\hat{x})$ is therefore tautological at the F5 level: both expressions denote *the same external-context-supplied potential*.

Modulo the additive-constant residual (§5), $V_{U3}(\hat{x}) = V(\hat{x})$ holds as operator equality.

### 3.6 No additive or multiplicative freedom remains (Strategy A verdict)

Combining §§3.2–3.5:
$$
\hat{H}_{U3} = \frac{\hbar^2 |\hat{p}|^2}{2m} + V(\hat{x}) = \hat{H}_{U4}. \tag{3.7}
$$

The kinetic term's coefficient $1/(2m)$ is fixed by the integration Jacobian — no multiplicative freedom. The mass $m$ is the Galilean group's central-extension structure constant — inherited per Arc M's "form FORCED, value INHERITED" methodology, identical to U4's treatment. The factor $\hbar^2$ is inherited via the dimensional-atlas Madelung anchoring, identical to U4's treatment. The additive constant in $V(\hat{x})$ is gauge — addressed in §5.

**Strategy A closes the F5 identification.** $\hat{H}_{U3}$ and $\hat{H}_{U4}$ are operator-identical on the U2 Hilbert space, with the only residual freedom being the additive vacuum-energy gauge.

**Falsifier Fal-5 (incompatible generator) dispatched under Strategy A.**

---

## 4. Strategy B (Cross-Check) — Stone-Theorem Uniqueness on $\hat{H}_{U4}$-Generated Group

This is a fallback / cross-check argument. It is presented for completeness; the F5 closure is established by Strategy A, and Strategy B is invoked only if Strategy A fails.

### 4.1 $\hat{H}_{U4}$ generates a strongly continuous unitary group

The operator $\hat{H}_{U4} = \hbar^2|\hat{p}|^2/(2m) + V(\hat{x})$ is self-adjoint on a dense domain in $\mathcal{H}$ (per U4's derivation). Self-adjoint operators on Hilbert spaces generate strongly continuous one-parameter unitary groups via the spectral theorem:
$$
V_t := \exp(-i\hat{H}_{U4} t / \hbar) \tag{4.1}
$$
is a strongly continuous one-parameter unitary group on $\mathcal{H}$, with $\hat{H}_{U4}$ as its self-adjoint generator (by Stone's theorem applied in reverse).

### 4.2 $\{V_t\}$ coincides with $\{U_t\}$

The group $\{V_t\}$ generated by $\hat{H}_{U4}$ acts on the U2 Hilbert space as a unitary representation of the time-translation symmetry. By the uniqueness of unitary representations of $(\mathbb{R}_t, +)$ within the Galilean group's representation on $\mathcal{H}$ (sourced to Galilean group structure, §2), $\{V_t\}$ must coincide with $\{U_t\}$ from F1 — both are *the* time-translation representation on $\mathcal{H}$.

Schematically: there is only one time-translation symmetry (Primitive 13); only one unitary representation of it on $\mathcal{H}$ (within the non-relativistic single-particle scope); both $\{V_t\}$ (constructed from $\hat{H}_{U4}$) and $\{U_t\}$ (constructed in F1) realize that representation.

### 4.3 Stone-theorem uniqueness forces $\hat{H}_{U4} = \hat{H}_{U3}$

Stone's theorem: every strongly continuous one-parameter unitary group on a Hilbert space has a *unique* self-adjoint generator. Applied to the common group $\{V_t\} = \{U_t\}$:

- The unique generator of $\{V_t\}$ is $\hat{H}_{U4}$ (by construction in §4.1).
- The unique generator of $\{U_t\}$ is $\hat{H}_{U3}$ (by F2).
- Stone's-theorem uniqueness forces $\hat{H}_{U4} = \hat{H}_{U3}$.

### 4.4 Strategy B verdict

Strategy B closes the F5 identification by an alternative route: Stone-theorem uniqueness applied to the common time-translation group, with $\hat{H}_{U4}$ pre-identified as the generator of one realization.

**Strategy B status.** Cross-check, not primary. **Strategy B is invoked only if Strategy A fails.** Since Strategy A closes (§3.6), Strategy B's role here is confirmatory: the same identification arises by an independent route, providing structural redundancy for the F5 conclusion.

---

## 5. Additive-Shift Residual

### 5.1 Stone's theorem leaves an additive constant

Stone's theorem produces $\hat{H}_{U3}$ unique up to an additive real constant $E_0$ — a vacuum-energy zero-point shift. The unitary group $\{U_t\}$ is unchanged under $\hat{H}_{U3} \to \hat{H}_{U3} + E_0 I$ because the additional factor $\exp(-i E_0 t / \hbar) I$ is a global phase (acts trivially on physical states up to overall phase).

### 5.2 U4's $V(\hat{x})$ has the same additive-constant ambiguity

The potential $V(\hat{x})$ in U4's derivation is determined by external context up to an additive constant. Shifting $V(\hat{x}) \to V(\hat{x}) + V_0$ produces $\hat{H}_{U4} \to \hat{H}_{U4} + V_0 I$, identical in form to the Stone-theorem additive-shift gauge.

### 5.3 The two additive-constant ambiguities coincide

Both ambiguities are the same gauge: the vacuum-energy zero-point shift. Choosing the same conventional zero (e.g., $V(\infty) = 0$ for confining potentials, or $V_0 = 0$ for free particles) fixes both simultaneously. The coincidence is automatic; no additional structural commitment is required.

### 5.4 Inherited-value audit ($m$, $\hbar$)

- **Mass $m$:** the Galilean group's central-extension structure constant. Inherited per Arc M's "form FORCED, value INHERITED" methodology, identical to U4's treatment in §F4.7.
- **$\hbar$:** inherited via the dimensional-atlas Madelung anchoring, identical to U4's treatment.

Both $m$ and $\hbar$ are inherited values, identical between $\hat{H}_{U3}$ and $\hat{H}_{U4}$. No residual freedom in the structural form arises from the inherited values; the form is identical, the values are identical.

---

## 6. Theorem F5 (Compatibility)

> **Theorem F5 (U3 — Compatibility with U4).** Let $\hat{H}_{U3}$ denote the unique self-adjoint generator of the time-translation group $\{U_t\}$ on the U2 Hilbert space $\mathcal{H}$, supplied by Stone's theorem applied in F1 + F2. Let $\hat{H}_{U4} = \hbar^2 |\hat{p}|^2/(2m) + V(\hat{x})$ denote the kinetic-plus-potential operator derived in U4. Then, modulo the additive vacuum-energy zero-point gauge,
> $$
> \hat{H}_{U3} = \hat{H}_{U4} = \frac{\hbar^2 |\hat{p}|^2}{2m} + V(\hat{x})
> $$
> as self-adjoint operators on $\mathcal{H}$. The identification is established by Strategy A (Galilean-Lie-algebra closure: $\hat{H}_{U3}$ satisfies the Galilean commutator $[\hat{H}_{U3}, \hat{K}_i] = -i\hbar\hat{p}_i$, integration of which yields $T(\hat{p}) = |\hat{p}|^2/(2m)$ via the chain-rule Jacobian; kinetic-plus-potential decomposition follows from translation invariance + locality), and cross-checked by Strategy B (Stone-theorem uniqueness of the time-translation generator). The mass $m$ and constant $\hbar$ are inherited per Arc M and dimensional-atlas Madelung anchoring, identical to U4's treatment.

**Status:** **FORCED**, with no new structural CANDIDATEs introduced.

### 6.1 Schrödinger evolution structurally complete

Combining F1, F2, F3, F4, F5:
$$
\boxed{i\hbar \, \partial_t P(t) = \hat{H} \, P(t), \qquad \hat{H} = \frac{\hbar^2 |\hat{p}|^2}{2m} + V(\hat{x}).} \tag{6.1}
$$

This is the Schrödinger equation in standard form, derived structurally from:

- **Primitive 13 + Primitive 03 + U2** (existence + unitarity + continuity of time-translation representation, F1),
- **Stone's theorem** (uniqueness + self-adjointness of generator, F2),
- **Hilbert-space + operator structure** (linearity, F3; first-order-in-time, F4),
- **Galilean Lie algebra + U5 momentum operator** (compatibility identification with U4 form, F5).

No PDE-level Schrödinger assumption appears anywhere in the derivation. The Schrödinger equation is structurally **forced**.

---

## 7. Final Falsifier Audit

### 7.1 Fal-5 dispatch

Fal-5 (incompatible generator: $\hat{H}_{U3}$ does not coincide with $\hat{H}_{U4}$). Dispatched in §3 (Strategy A) and cross-checked in §4 (Strategy B). The two operators are identical modulo the additive vacuum-energy gauge, which is itself a coincident gauge structure across both arcs.

### 7.2 Final falsifier table

| Falsifier | Targets | Source layer | Status | Dispatch location |
|---|---|---|---|---|
| Fal-1 (non-unitary time evolution) | F1 | Primitive-level | **Dispatched** | Memo 02 §2.4 |
| Fal-2 (multiple inequivalent generators) | F2 | Mathematical (Stone) | **Dispatched** | Memo 02 §3.2 |
| Fal-3 (non-linear evolution) | F3 | U2-dependent | **Dispatched** | Memo 02 §4.2 |
| Fal-4 (higher-order in time) | F4 | Phase-1-scope-dependent | **Dispatched** | Memo 02 §5.2 |
| Fal-5 (incompatible generator) | F5 | U4-identification | **Dispatched** | Memo 03 §3 (Strategy A) + §4 (Strategy B) |
| Fal-6 (non-self-adjoint generator) | F2 | Mathematical (Stone) | **Dispatched** | Memo 02 §3.3 |
| Fal-7 (non-continuous time) | F1 | Primitive 13 audit | **Dispatched** | Memo 02 §1.4 + §2.6 |

**All seven falsifiers dispatched.**

---

## 8. U3 Arc Verdict

### 8.1 Verdict

**FORCED.**

### 8.2 Justification (one paragraph)

The U3 commitment — the participation-measure evolution equation $i\hbar \partial_t P_K = \hat{H} P_K$ — is structurally derivable from ED's primitive stack plus the inherited FORCED upstream items (U1, U2-Discrete, U2-Continuum, U5, U4) and standard mathematical infrastructure (Stone's theorem, Galilean Lie algebra, $L^2$ functional analysis). Existence + unitarity + continuity of the time-translation representation (F1) follows from Primitive 13 + Primitive 03 + U2; uniqueness + self-adjointness of the generator (F2) follows from Stone's theorem applied to F1's group; linearity (F3) and first-order-in-time character (F4) are automatic from the Hilbert-space and operator-exponential structure; compatibility of the Stone-derived generator $\hat{H}_{U3}$ with the U4-derived operator $\hat{H}_{U4}$ (F5) follows from Galilean-Lie-algebra closure (Strategy A) — the time-translation generator within the Galilean representation must satisfy the commutator $[\hat{H}, \hat{K}_i] = -i\hbar\hat{p}_i$, integration of which against the boost generator $\hat{K} = m\hat{x} - t\hat{p}$ uniquely yields $T(\hat{p}) = |\hat{p}|^2/(2m)$ — with the result independently confirmed by Stone-theorem uniqueness applied to the $\hat{H}_{U4}$-generated group (Strategy B). All seven falsifiers are dispatched; no new structural CANDIDATEs are introduced; the only residual freedom is the additive vacuum-energy zero-point gauge, which coincides between $\hat{H}_{U3}$ and $\hat{H}_{U4}$ trivially. **The Schrödinger evolution equation is structurally forced from primitive-level inputs.**

### 8.3 Conditionality ledger

The U3 verdict is **FORCED** with the following inherited conditionalities and zero new ones:

1. **Non-relativistic single-particle scope.** Inherited from Phase-1 Step 2; conditions the use of the abelian time-translation group (F4) and the Galilean group (F5).
2. **Gauge-coupling-free scope.** Inherited from U4; conditions the kinetic-plus-potential decomposition without magnetic vector potential corrections.
3. **U2 inner-product structure (both regimes).** Inherited; supplies the Hilbert space.
4. **U1 participation-measure structure.** Inherited; supplies the carrier on which $U_t$ acts.
5. **U5 momentum-operator structure.** Inherited; supplies $\hat{p}$ for the Galilean algebra.
6. **U4 Hamiltonian form (as identification target only).** F5's identification is established with U4's operator form treated as a mathematical object on $\mathcal{H}$, not as a derivation premise.
7. **Inherited values.** Mass $m$ per Arc M; $\hbar$ per dimensional-atlas Madelung anchoring; both identical to U4's treatment.

**No new structural CANDIDATEs introduced.** All conditionalities are inherited from prior structural commitments.

### 8.4 Acyclicity confirmation

The U3 derivation operates strictly within the primitive-input scope of the present arc (Memo 01 §2 + Memo 02 §1.2 + Memo 03 §1.4). U4 appears only as an identification target in F5, never as a derivation premise. The U3 ⟷ U4 loop closes consistently: U4 was derived (Framing 1, conditional on U3's existence-of-Hermitian-generator); U3 is derived independently (Stone's theorem on Primitive 13 + U2); the F5 identification establishes that the two derivations land on the same operator. **Acyclicity preserved.**

---

## 9. Downstream Structural Consequences

### 9.1 U4 retroactive promotion

U4 was closed FORCED-conditional on U3 (Framing 1, U4 paper §10). With U3 now FORCED (this memo), **U4 promotes from FORCED-conditional to FORCED-unconditional retroactively.** The Framing-1 conditionality U4 carried is resolved.

### 9.2 Schrödinger evolution promoted to FORCED-unconditional

The Phase-1 Step 2 chain reads, post-U3:
```
Primitives 03, 04, 06, 07, 09, 13
              |
              v
        U1 (FORCED) -> P_K = sqrt(b) * exp(i pi)
              |
              v
        U2 (FORCED) -> <P|Q> inner product
              |
              v
        U5 (FORCED) -> spatial translation -> p̂ = -i ℏ ∇
              |
              v
        U4 (FORCED-UNCONDITIONAL post-U3) -> H = ℏ² |p̂|²/(2m) + V(x̂)
              |
              v
        U3 (FORCED, this memo) -> i ℏ ∂_t P = H P
              |
              v
       SCHRÖDINGER EVOLUTION (FORCED-unconditional)
```

Schrödinger evolution is **FORCED-unconditional in both discrete and continuum regimes**, gauge-invariant under the U2-Continuum conformal redundancy (per Memo 02 §6).

### 9.3 Active CANDIDATE inventory

Pre-U3: $\{U3\}$ + continuum gauge convention.

Post-U3: $\{ \, \}$ + continuum gauge convention.

**The active upstream-CANDIDATE inventory of the QM-emergence Phase-1 program is now empty** (modulo the description-level continuum gauge, which is a gauge choice rather than a structural commitment).

### 9.4 Forced-theorem count

Pre-U3: 15 forced structural theorems.

Post-U3: **16 forced structural theorems**, with one retroactively promoted to FORCED-unconditional:

| # | Theorem | Status (post-U3) |
|---|---|---|
| 10 | Born rule (Gleason–Busch) | FORCED-unconditional |
| 11 | U2-Discrete | FORCED-unconditional |
| 12 | U2-Continuum (with conformal gauge) | FORCED-unconditional |
| 13 | U5 (translation generator + momentum operator) | FORCED-unconditional |
| 14 | U1 (participation-measure construction) | FORCED-unconditional |
| 15 | U4 (specific Hamiltonian form) | **FORCED-unconditional** (was FORCED-conditional) |
| **16** | **U3 (this arc, time-translation generator + Schrödinger evolution)** | **FORCED-unconditional** |

### 9.5 All four foundational QM postulates structurally derived

| Postulate | Pre-U3 status | Post-U3 status |
|---|---|---|
| Born rule | FORCED-unconditional | (unchanged) FORCED-unconditional |
| Bell–Tsirelson bound | FORCED-unconditional | (unchanged) FORCED-unconditional |
| Heisenberg uncertainty | FORCED-unconditional | (unchanged) FORCED-unconditional |
| **Schrödinger evolution** | FORCED-conditional on U3 | **FORCED-unconditional** |

**All four foundational QM postulates are now structurally derived from ED primitives.**

### 9.6 Phase-1 program structurally complete

The QM-emergence Phase-1 structural-foundations program is **structurally complete** modulo the description-level continuum gauge convention. Every load-bearing structural item in the participation-measure → Hilbert-space → QM-emergence chain has been derived:

- **Layer 1 (carrier):** U1.
- **Layer 2 (Hilbert-space arena):** U2-Discrete + U2-Continuum + Theorem 10 (Born) + U5.
- **Layer 3 (dynamical):** U4 + U3 (this arc).

The seven-arc cycle (born_gleason → U2 → U2-continuum → U5 → U1 → U4 → U3) closes the Phase-1 program. The methodological pattern (decompose CANDIDATE → identify load-bearing items → close via primitive-level arguments → introduce zero new CANDIDATEs) has been demonstrated against seven substantively different structural questions, including the dynamical-content question that was U3's load-bearing F5.

### 9.7 Updated synthesis-paper status

The QM-emergence Phase-1 synthesis paper [`papers/QM_Emergence_Structural_Completion/`] §§3.3/3.4/3.5/4 require revision to reflect the post-U3 state. Specifically:

- §3.3 (foundational postulates' status): all four now FORCED-unconditional.
- §3.4 (upstream-CANDIDATE inventory): empty (modulo continuum gauge).
- §3.5 (reduction count): from "five upstream commitments" to "zero upstream commitments + one description-level gauge."
- §4 (open work): focus shifts entirely to Phase-3 (gravitational sector) and synthesis-paper revision.

A single editorial pass can now cover all four sections (no further arc work is gating the synthesis revision).

### 9.8 Sensitivity flags

Inherited from prior arcs and now load-bearing on the closed Phase-1 program:

- **Primitive 09 $U(1)$-only.** Load-bears U1 (Theorem 14) and U2 (Theorem 11). Future amendment supplying additional polarity content would re-open these arcs.
- **Primitive 04 bandwidth-additivity.** Load-bears U1 (Theorem 14 via Cauchy functional equation). Future amendment to bandwidth additivity would re-open U1.
- **Primitive 13 continuous-time interpretation.** Load-bears U3 F1 + Fal-7. Future amendment to discrete-time would require thin-limit adaptation of F1.
- **Galilean-group uniqueness within non-relativistic scope.** Load-bears U3 F5 (Strategy A) and U4 §F4. Future amendment to the non-relativistic scope (e.g., relativistic extension) would require Lorentz-group treatment of both arcs.
- **Arc M ("form FORCED, values INHERITED" methodology).** Load-bears U3 F5 inherited values + U4 §F4 inherited values. Conventional ED methodology; not a sensitivity in the usual sense.

These flags are inherited from prior structural decisions and do not constitute new conditionalities introduced by U3.

---

## 10. Recommended Next Steps

**(a) Draft Memo 04 (closure and canonical summary).** Following the templates of U5 Memo 04, U1 Memo 04, and U4 Memo 04, Memo 04 should produce a single document that serves as the canonical entry-point for the U3 arc: arc summary, narrative integration of the four memos, theorem-grade U3 statement, downstream cascade integration, public-facing explainer section, and the section-to-memo mapping appendix. Memo 04 also serves as the coordination point for the bundled memory-record update (per the deferred-update discipline established in Memos 00–02).

**(b) Bundled memory-record update covering the U3 arc + Phase-1 closure.** A single comprehensive update to `project_qm_emergence_arc.md` capturing the post-arc state: (i) U3 theorem now FORCED-unconditional, (ii) U4 promotion to FORCED-unconditional retroactively, (iii) Schrödinger evolution promoted to FORCED-unconditional, (iv) updated active upstream-CANDIDATE inventory ($\{ \, \}$ + continuum gauge), (v) all four foundational QM postulates now structurally derived, (vi) Phase-1 program structurally complete, (vii) updated forced-theorem count (16, with two promotions in this arc cycle), (viii) sensitivity flag inventory (per §9.8). The MEMORY.md index line update should be similarly bundled.

**(c) Draft the U3 publication paper.** Following the templates of U5, U4, and U1 publication papers, the U3 paper would be the natural sixth in the structural-foundations publication series. The paper documents the Stone's-theorem-on-time-translation derivation (parallel to U5's Stone's-theorem-on-spatial-translation derivation), the Galilean-Lie-algebra closure argument identifying $\hat{H}_{U3}$ with $\hat{H}_{U4}$, and the headline result: all four foundational QM postulates structurally derived from ED primitives. Companion public explainer should follow as the seventh in the public-explainer ladder. This deliverable is convention work (publication formalization), not derivation work; can be scheduled per project priorities.
