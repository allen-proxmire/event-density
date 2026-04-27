# Memo 02 — U3 F1, F2, F3, F4 Derivations and Falsifier Dispatches

**Date:** 2026-04-26
**Arc:** `arcs/U3/`
**Predecessors:** [`00_arc_outline.md`](00_arc_outline.md), [`01_decomposition_and_mapping.md`](01_decomposition_and_mapping.md)
**Status:** Derivation memo. Closes the four template-transfer sub-features (F1, F2, F3, F4) by direct adaptation of the U5 Stone's-theorem methodology to the time axis, dispatches six of the seven falsifiers (Fal-1, Fal-2, Fal-3, Fal-4, Fal-6, Fal-7), establishes the gauge-compatibility check, and prepares the load-bearing F5 (compatibility with U4) for Memo 03 by isolating the exact compatibility condition that must be closed.
**Purpose:** Reduce the U3 verdict's open content to a single substantive question (F5) for Memo 03 to address.

---

## 1. Pre-Derivation Setup

### 1.1 Recap of sub-feature classification

From Memo 01 §1.2:

| Sub-feature | Classification |
|---|---|
| F1 (existence of time-translation representation) | forced-via-derivation |
| F2 (uniqueness of self-adjoint generator) | forced-via-derivation |
| F3 (linearity) | automatic given F1 + F2 |
| F4 (first-order-in-time) | automatic given F2 |
| F5 (compatibility with U4) | load-bearing (Memo 03) |

### 1.2 Forbidden inputs (re-stated for this memo)

The following are forbidden as derivation inputs to F1, F2, F3, F4:

- **U4** in any role (form of $\hat{H}$, kinetic-plus-potential decomposition, Galilean integration, or operator content).
- **U3 itself** (question-begging).
- **PDE-level Schrödinger equation** in textbook form.
- **Relativistic kinematics** (Lorentz boosts, Klein–Gordon, Dirac).
- **Downstream gauge-coupling structure** (magnetic vector potentials).
- **QFT-level inputs** (creation/annihilation operators, Fock space).

These restrictions are enforced explicitly in §§2–5 below.

### 1.3 Permitted inputs

- **Primitive 13 (Relational Timing).** Supplies the continuous time axis $\mathbb{R}_t$ and time-translation symmetry as a kinematic feature of the participation graph. Per §1.4 audit below, the continuous-time interpretation is the canonical reading.
- **Primitive 03 (Participation).** Supplies graph homogeneity, including time-axis homogeneity (no privileged instant of time).
- **Primitive 04 (Bandwidth).** Supplies the participation-measure components $P_K$ on which $U_t$ acts.
- **Primitive 09 (Tension Polarity).** $U(1)$-valued polarity phase. Supplies the complex structure on which Hermitian operators act (via U1).
- **U1 (Theorem 14).** Participation-measure construction $P_K = \sqrt{b_K} \cdot e^{i\pi_K}$.
- **U2-Discrete (Theorem 11) + U2-Continuum (Theorem 12).** Sesquilinear inner product on the participation-measure Hilbert space, in both regimes.
- **U5 (Theorem 13).** Methodological template (Stone's theorem applied to spatial translations); structural inheritance only — F1–F4 do not invoke the U5 *content* (the spatial momentum operator $\hat{p}$).
- **Stone's theorem** on one-parameter unitary groups.
- **Standard $L^2$ functional analysis** (translation continuity, spectral theorem).
- **Phase-1 Step 2 scope conditions:** non-relativistic single-particle, flat-spacetime baseline, gauge-coupling-free.

### 1.4 Pre-derivation Primitive 13 audit

Per Memo 00 §7(b) and Memo 01 §7(b), a brief Primitive 13 audit is required before F1 to confirm the continuous-time interpretation.

**Audit summary.** Primitive 13 (Relational Timing) supplies the time axis as a continuous parameter $t \in \mathbb{R}$ at the structural level, with the time-translation symmetry an automatic feature of the relational structure (no privileged instant). The discrete-vs-continuous reading question that arose for the spatial axis (where U5 handled both regimes via a thin-limit argument) does not arise on the time axis at Phase-1 scope: Primitive 13 commits to continuous relational time, with discrete-time structures (e.g., causal-set-like discreteness) belonging to Phase-3-and-beyond extensions outside the present scope.

**Audit verdict.** Continuous time axis confirmed. Stone's theorem applies directly without a thin-limit step. **Falsifier Fal-7 (non-continuous time-translation representation) is conditionally dispatched** by the audit; the explicit dispatch in §2.6 will state this for the record.

---

## 2. Derivation of F1 (Existence of Time-Translation Representation)

### 2.1 The claim

The time-translation operators $\{U_t : t \in \mathbb{R}\}$ acting on the U2 Hilbert space $\mathcal{H}$ by
$$
(U_t P)_K(x, s) := P_K(x, s - t)
$$
form a strongly continuous one-parameter abelian unitary group. Specifically: $U_t$ is well-defined componentwise on participation-measure components, acts linearly, preserves the U2 inner product (unitarity), satisfies the abelian group structure $U_t U_s = U_{t+s}$, and is strongly continuous in $t$.

### 2.2 Time-translation symmetry as a kinematic feature

Three primitive-level observations:

- **(i)** Primitive 13's relational timing supplies a continuous time axis $\mathbb{R}_t$ (per §1.4 audit). No privileged instant of time exists at the primitive level.
- **(ii)** Primitive 03's homogeneity extends to the time axis: the participation relation does not privilege any time slice. The participation graph's structure at time $s$ is structurally identical to its structure at time $s - t$ for any $t$, up to relabeling of time coordinates.
- **(iii)** No primitive-level structure singles out a privileged time origin or a privileged time-translation magnitude. The time-translation group is the abelian group $(\mathbb{R}_t, +)$.

These three observations establish time-translation symmetry as a *kinematic* property of the participation graph — a symmetry of the static structure indexed across time slices, not a property requiring dynamical evolution. **No reference to U4, no Hamiltonian, and no Schrödinger equation appears in this argument.** The time-translation symmetry is structurally upstream of the dynamical equation that U3 will identify.

### 2.3 Linearity

Time translation acts linearly on participation-measure components:
$$
U_t (\alpha P + \beta Q)_K(x, s) = \alpha P_K(x, s - t) + \beta Q_K(x, s - t) = \alpha (U_t P)_K(x, s) + \beta (U_t Q)_K(x, s)
$$
for all $\alpha, \beta \in \mathbb{C}$ and all $P, Q \in \mathcal{H}$. The linearity of $U_t$ inherits from the linearity of the shift operation on functions; no linearity import from U1 is required.

### 2.4 Unitarity

For $P, Q \in \mathcal{H}$ and $t \in \mathbb{R}$:
$$
\langle U_t P \mid U_t Q \rangle_{\mathcal{H}} = \sum_K \int_{\mathbb{R}^d} \int_{\mathbb{R}_t} P_K^*(x, s - t) \, Q_K(x, s - t) \, ds \, d\mu(x).
$$
Substituting $s' = s - t$, with $ds' = ds$ (the time-translation Jacobian is unity since the U2 measure is translation-invariant on the time axis: Primitive 13 supplies a translation-invariant relational time, with no $t$-dependent weighting in the U2 measure construction):
$$
\langle U_t P \mid U_t Q \rangle_{\mathcal{H}} = \sum_K \int_{\mathbb{R}^d} \int_{\mathbb{R}_t} P_K^*(x, s') \, Q_K(x, s') \, ds' \, d\mu(x) = \langle P \mid Q \rangle_{\mathcal{H}}.
$$
The time-translation operators preserve the U2 inner product. **Falsifier Fal-1 (non-unitary time evolution) dispatched.**

### 2.5 Group structure

Direct calculation:
$$
(U_t U_s P)_K(x, r) = (U_s P)_K(x, r - t) = P_K(x, r - t - s) = (U_{t+s} P)_K(x, r),
$$
so $U_t U_s = U_{t+s}$. Also $U_0 = I$ and $U_{-t} = U_t^{-1}$. The time-translation group is abelian and isomorphic to $(\mathbb{R}_t, +)$.

### 2.6 Strong continuity

For any $P \in \mathcal{H}$ with components $P_K(x, \cdot)$ in $L^2(\mathbb{R}_t, ds)$ (per the U2-measure construction's time-axis component), the map $t \mapsto U_t P$ is strongly continuous because $L^2$-translation is strongly continuous in the translation parameter. This is a standard result of $L^2$ analysis (cf. Reed and Simon, *Methods of Modern Mathematical Physics, Volume I*, §VIII.4) and inherits to the U2 Hilbert space's direct-sum / direct-integral structure across the channel index $K$ and the spatial argument $x$.

The continuous-time interpretation of Primitive 13 (per §1.4 audit) is the precondition for strong continuity. Were Primitive 13 to supply only discrete time, the strong-continuity argument would require a thin-limit step parallel to U5's continuum-regime treatment. The audit rules this out at Phase-1 scope. **Falsifier Fal-7 (non-continuous time-translation representation) dispatched** by Primitive 13's continuous-time content.

### 2.7 Theorem F1 statement

> **Theorem F1 (U3 — Time-Translation Representation).** Let $\mathcal{H}$ denote the U2 Hilbert space of participation measures established by the U2-Discrete and U2-Continuum theorems. Then the time-translation operators
> $$
> (U_t P)_K(x, s) := P_K(x, s - t), \qquad t \in \mathbb{R},
> $$
> form a strongly continuous one-parameter abelian unitary group on $\mathcal{H}$. The derivation invokes Primitives 13 (time axis) and 03 (homogeneity) plus the U2 inner-product structure, with no input from U4, no Hamiltonian, and no PDE-level Schrödinger assumption.

### 2.8 Falsifier dispatches in F1

- **Fal-1 (non-unitary time evolution).** Dispatched by §2.4 (translation-invariance of U2 measure on time axis).
- **Fal-7 (non-continuous time-translation representation).** Dispatched by §2.6 (Primitive 13's continuous-time content + standard $L^2$-translation continuity).

---

## 3. Derivation of F2 (Stone-Uniqueness of the Generator)

### 3.1 Stone's theorem (re-stated)

> **Theorem (Stone 1932).** Every strongly continuous one-parameter unitary group $\{V(t) : t \in \mathbb{R}\}$ on a Hilbert space has a unique self-adjoint generator $A$ such that $V(t) = \exp(itA)$.

### 3.2 Application to F1's group

By Theorem F1, $\{U_t : t \in \mathbb{R}\}$ is a strongly continuous one-parameter abelian unitary group on the U2 Hilbert space $\mathcal{H}$. Apply Stone's theorem: there exists a unique self-adjoint operator on $\mathcal{H}$, denoted $\hat{H}_{U3}$ (the subscript marks this as the U3-derived operator, in anticipation of the F5 identification with $\hat{H}_{U4}$), such that
$$
U_t = \exp\!\left( -\frac{i \hat{H}_{U3} t}{\hbar} \right). \tag{3.1}
$$
The sign convention ($-i$ rather than $+i$) and the $\hbar$ factor are standard quantum-mechanical conventions, choosable freely; the substantive content of Stone's theorem is **existence and uniqueness of $\hat{H}_{U3}$ as a self-adjoint operator on $\mathcal{H}$**, with the operator-exponential parametrizing the entire group $\{U_t\}$.

The generator is unique. **Falsifier Fal-2 (multiple inequivalent generators) dispatched.**

### 3.3 Self-adjointness

Stone's theorem produces a self-adjoint generator, not merely a Hermitian one. Self-adjointness — in the strict sense of equality of the operator with its adjoint on the same dense domain — is automatic from the theorem's hypotheses (strong continuity of the unitary group). No separate verification is required. **Falsifier Fal-6 (non-self-adjoint generator) dispatched.**

### 3.4 No U4-dependent assumptions enter

The derivation invokes only: (i) F1 (a strongly continuous unitary group on $\mathcal{H}$), and (ii) Stone's theorem (mathematical infrastructure). At no point does U4's specific operator form $\hbar^2|\hat{p}|^2/(2m) + V(\hat{x})$, the Galilean Lie algebra, or any U4-derived content enter. The operator $\hat{H}_{U3}$ produced by Stone's theorem is *abstract*: it is the unique self-adjoint generator of $U_t$, with no specified content beyond that. Identification of $\hat{H}_{U3}$ with U4's operator is the F5 question, deferred to Memo 03.

### 3.5 Theorem F2 statement

> **Theorem F2 (U3 — Uniqueness of the Time-Translation Generator).** Under the hypotheses of Theorem F1, there exists a unique self-adjoint operator $\hat{H}_{U3}$ on the U2 Hilbert space $\mathcal{H}$ such that $U_t = \exp(-i\hat{H}_{U3} t / \hbar)$ for all $t \in \mathbb{R}$. The identification is via Stone's theorem applied to the strongly continuous unitary group $\{U_t\}$, and is U4-independent.

### 3.6 Falsifier dispatches in F2

- **Fal-2 (multiple inequivalent generators).** Dispatched by §3.2 (Stone's-theorem uniqueness).
- **Fal-6 (non-self-adjoint generator).** Dispatched by §3.3 (Stone's-theorem self-adjointness).

---

## 4. Derivation of F3 (Linearity of the Evolution Equation)

### 4.1 The argument

The evolution equation induced by $U_t$ on a state $P \in \mathcal{H}$ is obtained by differentiating the operator-exponential at $t = 0$:
$$
\frac{d}{dt}\bigg|_{t=0} U_t P = -\frac{i}{\hbar} \hat{H}_{U3} P.
$$
Substituting $P(t) := U_t P_0$ for the time-evolved state with initial datum $P_0$:
$$
\frac{d}{dt} P(t) = -\frac{i}{\hbar} \hat{H}_{U3} P(t),
$$
or equivalently,
$$
\boxed{i\hbar \, \partial_t P(t) = \hat{H}_{U3} P(t).} \tag{4.1}
$$

### 4.2 Linearity is automatic

The evolution equation (4.1) is linear in $P(t)$ because:

- **(i)** The Hilbert space $\mathcal{H}$ is a complex vector space (linear by definition).
- **(ii)** The operator $\hat{H}_{U3}$ is a self-adjoint operator on $\mathcal{H}$, hence linear (operators on Hilbert spaces are linear by definition of "operator").
- **(iii)** The unitary group $\{U_t\}$ acts linearly on $\mathcal{H}$ (per F1 §2.3).
- **(iv)** Time translations form an additive abelian group on $\mathbb{R}_t$, with $U_{t+s} = U_t U_s$ inheriting linearity from each factor.

No additional structural assumption is required. Non-linearity could arise only if (a) the Hilbert space were not a vector space, (b) operators on it were not linear, (c) the unitary representation was not linear, or (d) the time-translation group did not have additive group structure. None of these obtains under the established structural inputs.

In particular, **Gross-Pitaevskii-like nonlinearities do not arise structurally** in the present framework: such nonlinearities are introduced phenomenologically to model interactions in many-body systems, not derived from primitive-level structural commitments. The Phase-1 single-particle scope precludes such phenomenological additions; under the established inputs, $\hat{H}_{U3}$ acts linearly. **Falsifier Fal-3 (non-linear evolution) dispatched.**

### 4.3 Theorem F3 statement

> **Theorem F3 (U3 — Linearity of the Evolution Equation).** The induced evolution equation $i\hbar \, \partial_t P(t) = \hat{H}_{U3} P(t)$ on the U2 Hilbert space is linear in $P(t)$. Linearity is automatic from the Hilbert-space structure, the operator-theoretic definition of $\hat{H}_{U3}$, the linearity of the unitary representation $\{U_t\}$, and the additive structure of the time-translation group. No additional structural assumption is required.

### 4.4 Falsifier dispatch in F3

- **Fal-3 (non-linear evolution).** Dispatched by §4.2.

---

## 5. Derivation of F4 (First-Order-in-Time Evolution)

### 5.1 The argument

Differentiating the operator-exponential $U_t = \exp(-i\hat{H}_{U3} t/\hbar)$ once in $t$:
$$
\frac{d}{dt} U_t = -\frac{i}{\hbar} \hat{H}_{U3} \, U_t.
$$
Applied to a state $P(t) = U_t P_0$:
$$
i\hbar \, \partial_t P(t) = \hat{H}_{U3} P(t),
$$
which is **first-order** in $\partial_t$. The equation contains the first time-derivative and no higher-order time-derivatives.

### 5.2 Why higher-order does not arise

The operator-exponential $U_t = \exp(-i\hat{H}_{U3} t/\hbar)$ is a one-parameter group, parameterized by a single real $t$. Its first derivative in $t$ produces a first-order equation. Higher derivatives produce powers of $\hat{H}_{U3}$:
$$
i\hbar \, \partial_t^n P(t) = (\hat{H}_{U3})^n P(t),
$$
which are downstream consequences of (4.1), not independent equations.

A second-order-in-time equation (Klein–Gordon-like, $\partial_t^2 \psi = -\hat{H}^2 \psi / \hbar^2$ or $\partial_t^2 \psi = -c^2(-\nabla^2 + m^2) \psi$) arises in *relativistic* quantum mechanics where time and space are mixed by Lorentz boosts. The non-relativistic scope condition (inherited from Phase-1 Step 2) selects the abelian time-translation group $\mathbb{R}_t$ rather than the Lorentz boost group; under this scope, Stone's theorem produces a single self-adjoint generator and the operator-exponential structure gives a first-order equation.

The non-relativistic scope condition is sourced from Phase-1 Step 2's framing, not from U4 (per Memo 01 §2.1's reframable-by-sourcing audit). The first-order character is therefore not U4-dependent; it follows from Stone's theorem + non-relativistic scope.

**Falsifier Fal-4 (higher-order-in-time evolution) dispatched.**

### 5.3 Theorem F4 statement

> **Theorem F4 (U3 — First-Order-in-Time Structure).** The evolution equation $i\hbar \, \partial_t P(t) = \hat{H}_{U3} P(t)$ is first-order in $\partial_t$. The first-order character is automatic from Stone's theorem (operator-exponential parameterization), the abelian group structure of time translations, and the non-relativistic scope condition (which selects the abelian $\mathbb{R}_t$ time-translation group over relativistic Lorentz boosts). No higher-order-in-time terms arise structurally.

### 5.4 Falsifier dispatch in F4

- **Fal-4 (higher-order-in-time evolution).** Dispatched by §5.2.

---

## 6. Continuum-Regime Gauge-Compatibility Check

### 6.1 The U2-Continuum conformal gauge is spatial-only

The U2-Continuum theorem's gauge structure is the conformal rescaling $(b_K, d\mu) \to (\Omega^{-D} b_K, \Omega^D d\mu)$ where $\Omega = \Omega(x)$ is a smooth positive function on the spatial manifold. The conformal factor $\Omega$ depends on the spatial coordinate $x$, **not on the time coordinate $t$**. The gauge therefore acts on the spatial measure and the spatial bandwidth content, leaving the time-axis structure untouched.

### 6.2 Consequence for the time-translation generator

The time-translation operator $U_t$ shifts the time argument: $(U_t P)_K(x, s) = P_K(x, s - t)$. Under the U2-Continuum conformal gauge:
$$
(U_t P)_K(x, s) \to \Omega^{-D/2}(x) \, P_K(x, s - t)
$$
(with the $\Omega^{-D/2}$ factor inherited from the field-redefinition $P_K \to \Omega^{-D/2} P_K$ that compensates the measure redefinition). The conformal factor $\Omega^{-D/2}(x)$ is *time-independent*; it commutes with the time-translation operator $U_t$. Consequently:
$$
\hat{H}_{U3} \to \hat{H}_{U3}
$$
under the conformal gauge — the time-translation generator is **gauge-invariant**.

This is simpler than U5's gauge-compatibility check, which required showing that the spatial-translation generator preserved its identification under spatial conformal rescalings. Here the gauge does not even act on the relevant axis, so invariance is immediate.

### 6.3 Statement and verification

> The U2-Continuum conformal gauge acts trivially on the time-translation generator $\hat{H}_{U3}$. The U3 verdict is gauge-invariant in the continuum regime.

This completes the gauge-compatibility check and confirms that F1, F2, F3, F4 all hold in both discrete and continuum regimes without additional regime-specific structural commitments.

---

## 7. Pre-Derivation Setup for F5 (Compatibility with U4)

### 7.1 The exact compatibility condition

After F1–F4, we have:

- A unique self-adjoint operator $\hat{H}_{U3}$ on the U2 Hilbert space, produced by Stone's theorem applied to time-translation symmetry. Content: **"the time-translation generator."** No further specification of $\hat{H}_{U3}$'s functional form has been derived.
- A self-adjoint operator $\hat{H}_{U4} = \hbar^2|\hat{p}|^2/(2m) + V(\hat{x})$ on the U2 Hilbert space, produced by U4 via Galilean Lie algebra integration on the U5 momentum operator. Content: **a specific kinetic-plus-potential operator on the U2 Hilbert space.**

The F5 question is whether these two operators coincide:
$$
\boxed{\hat{H}_{U3} \stackrel{?}{=} \hat{H}_{U4} \quad \text{as operators on } \mathcal{H}.} \tag{7.1}
$$

If equality holds, the U3 verdict is **FORCED**, the Schrödinger evolution equation becomes structurally complete, and U4's Framing-1 conditionality is retroactively resolved (U4 promotes from FORCED-conditional to FORCED-unconditional). If equality fails, the U3 verdict is **PARTIAL** (with the disagreement defining the residual content) or **FREE** (if no identification is possible at all).

### 7.2 Discipline: identification, not derivation

The F5 question is *not* "derive $\hat{H}_{U3}$ from $\hat{H}_{U4}$" (which would invert U4's Framing-1 conditionality and close the U3 ↔ U4 circular loop). The question is: are these two operators, *each constructed independently from primitive-level inputs and standard mathematical infrastructure*, the same operator on the U2 Hilbert space?

The discipline (per Memo 01 §2.5):

- **(i)** $\hat{H}_{U3}$ is derived from F1 + F2 (Stone's theorem on time translations). U4 plays no role.
- **(ii)** $\hat{H}_{U4}$ is treated as a mathematical object on $\mathcal{H}$ — a specific self-adjoint operator with specific functional form. U4's derivation is taken as background (not as a U3-input).
- **(iii)** F5 establishes an identification between the two via shared structural infrastructure (the Galilean Lie algebra), not via deriving one from the other.

This protocol preserves acyclicity. U3 is derived from primitives + Stone's theorem; U4 was derived from primitives + Galilean integration on U5; the identification step closes the U3 ↔ U4 loop *consistently* without circularity.

### 7.3 Structural constraints available for the F5 derivation

Memo 03's F5 derivation will draw on the following structural constraints:

1. **Galilean invariance.** The Galilean Lie algebra is the unique consistent boost-translation algebra in the non-relativistic scope (per U4 §2.3). It contains $\hat{H}$, $\hat{p}$, $\hat{x}$, $\hat{K}$, $\hat{J}$ as generators with the standard commutator structure:
   - $[\hat{x}_i, \hat{p}_j] = i\hbar \delta_{ij}$,
   - $[\hat{K}_i, \hat{p}_j] = i\hbar m \delta_{ij}$ (mass as central-extension structure constant),
   - $[\hat{H}, \hat{K}_i] = -i\hbar \hat{p}_i$ (the load-bearing commutator U4 integrated).

   The Galilean group is *primitive-level* infrastructure, available to U3 independently of U4 (per Memo 01 §2.5's reframable classification). U4 uses this algebra to derive $\hat{H}_{U4}$'s form; U3 uses the same algebra to identify $\hat{H}_{U3}$ as the time-translation generator within the algebra's representation.

2. **U2 inner-product preservation.** All Galilean transformations are unitary on the U2 Hilbert space (per U4 §F4.4). Both $\hat{H}_{U3}$ (by Stone's theorem applied to time translations) and $\hat{H}_{U4}$ (by U4's derivation) are self-adjoint. The inner-product preservation supplies the framework within which both operators are well-defined.

3. **U5 momentum structure.** The U5 momentum operator $\hat{p} = -i\hbar\nabla$ is the spatial-translation generator. It enters $\hat{H}_{U4}$ as the kinetic-energy variable. It also enters the Galilean Lie algebra as the spatial-translation generator. The shared momentum operator is one of the structural anchors of the F5 identification.

4. **Non-relativistic scope.** Selects the Galilean group over the Lorentz group. Both U3 and U4 operate within this scope; the identification is performed within it.

5. **Primitive-level boost algebra.** The boost generator $\hat{K}_i = m\hat{x}_i - t\hat{p}_i$ (per U4 §F4.2) is a Galilean-group generator. Its commutator with $\hat{H}$ is the load-bearing equation (U4's derivation integrated this commutator to derive the kinetic-energy form). The same commutator, evaluated against $\hat{H}_{U3}$, will supply the F5 identification: the time-translation generator must satisfy the same Galilean commutator condition as the kinetic-plus-potential operator, and the Galilean group's representation theory then forces them to coincide.

### 7.4 The F5 derivation strategy (preview for Memo 03)

Two candidate arguments are anticipated, in order of preference:

**Strategy A: Galilean-Lie-algebra closure.** Show that $\hat{H}_{U3}$ and $\hat{H}_{U4}$ are both representations of the same Lie algebra element — the time-translation generator of the Galilean group. The Galilean group's representation on the U2 Hilbert space is unique (up to unitary equivalence) within the non-relativistic single-particle scope. The two operators must therefore coincide.

**Strategy B: Stone-theorem uniqueness on the Galilean group.** Show that $\hat{H}_{U4}$ generates a strongly continuous one-parameter unitary group on the U2 Hilbert space (the time-evolution group induced by $\hat{H}_{U4}$). Show that this group coincides with $\{U_t\}$ from F1 (i.e., it is the time-translation group of the Galilean representation). Stone's-theorem uniqueness then forces $\hat{H}_{U4} = \hat{H}_{U3}$.

Strategy A is anticipated to be cleaner (purely algebraic); Strategy B may serve as a backup or cross-check.

### 7.5 Anticipated outcome

The natural prior is **F5 closes via Strategy A**: the Galilean Lie algebra has a unique time-translation generator on the U2 Hilbert space's Galilean representation, and that generator is necessarily $\hat{H}_{U4} = \hbar^2|\hat{p}|^2/(2m) + V(\hat{x})$. The Stone-theorem-derived $\hat{H}_{U3}$ coincides with it.

Two potential complications, each anticipated to be manageable:

- **(i) Additive-shift residual.** Stone's theorem produces $\hat{H}_{U3}$ unique up to an additive constant; U4's $V(\hat{x})$ likewise has an additive constant ambiguity. Both are gauge (vacuum-energy zero-point shifts) and coincide trivially.
- **(ii) Domain-of-self-adjointness subtleties.** The U2 Hilbert space's domain structure may require a domain-matching argument for the operator equality to hold strictly. This is technical functional-analytic content, not new structural commitment.

If the natural prior holds, Memo 03's verdict is FORCED with no new structural CANDIDATEs introduced.

---

## 8. Updated Falsifier Status

| Falsifier | Targets | Source layer | Memo-02 status | Dispatch location |
|---|---|---|---|---|
| **Fal-1** (non-unitary time evolution) | F1 | Primitive-level | **Dispatched** | §2.4 |
| **Fal-2** (multiple inequivalent generators) | F2 | Mathematical (Stone) | **Dispatched** | §3.2 |
| **Fal-3** (non-linear evolution) | F3 | U2-dependent | **Dispatched** | §4.2 |
| **Fal-4** (higher-order in time) | F4 | Phase-1-scope-dependent | **Dispatched** | §5.2 |
| **Fal-5** (incompatible generator) | F5 | U4-dependent (compatibility) | **Open** | Memo 03 |
| **Fal-6** (non-self-adjoint generator) | F2 | Mathematical (Stone) | **Dispatched** | §3.3 |
| **Fal-7** (non-continuous time) | F1 | Primitive 13 audit | **Dispatched** | §1.4 + §2.6 |

**Six of seven falsifiers dispatched.** Fal-5 (compatibility failure) is the lone active falsifier for Memo 03.

The arc's open content reduces to a single substantive question (F5) and a single falsifier (Fal-5) — exactly the pattern Memos 00 and 01 anticipated.

---

## 9. Recommended Structure for Memo 03

### 9.1 Proposed memo title

**Memo 03 — U3 F5 Compatibility Derivation, Falsifier Audit, and Verdict**

### 9.2 Proposed section outline

- **§1. Pre-derivation setup.**
  - §1.1 Recap of F1–F4 status (closed in Memo 02).
  - §1.2 The exact compatibility condition (re-stated from Memo 02 §7.1).
  - §1.3 Discipline: identification, not derivation (re-stated from Memo 02 §7.2).
  - §1.4 Forbidden inputs for F5 (specifically: U4 may not appear as a *premise*; only as identification target).

- **§2. The Galilean Lie algebra as primitive-level infrastructure.**
  - §2.1 Galilean group and its generators ($\hat{H}, \hat{p}, \hat{x}, \hat{K}, \hat{J}$).
  - §2.2 Standard commutator structure.
  - §2.3 Non-relativistic scope selection of Galilean over Lorentz (sourced to Phase-1 Step 2, not U4).
  - §2.4 Galilean group's unitary representation on the U2 Hilbert space.

- **§3. Strategy A: Galilean-Lie-algebra closure.**
  - §3.1 $\hat{H}_{U3}$ as the time-translation generator within the Galilean representation.
  - §3.2 $\hat{H}_{U4}$ as the unique solution of the Galilean commutator condition $[\hat{H}, \hat{K}_i] = -i\hbar \hat{p}_i$ on the U2 Hilbert space (per U4 §F4).
  - §3.3 Uniqueness of the Galilean representation's time-translation generator on the U2 Hilbert space (within non-relativistic single-particle scope).
  - §3.4 Identification: $\hat{H}_{U3} = \hat{H}_{U4}$.
  - §3.5 Domain-of-self-adjointness check.

- **§4. Strategy B (cross-check): Stone-theorem uniqueness on $\hat{H}_{U4}$-generated group.**
  - §4.1 $\hat{H}_{U4}$ generates a strongly continuous one-parameter unitary group on $\mathcal{H}$.
  - §4.2 This group coincides with $\{U_t\}$ from F1.
  - §4.3 Stone-theorem uniqueness forces $\hat{H}_{U4} = \hat{H}_{U3}$.

- **§5. Additive-shift residual analysis.**
  - §5.1 Stone's theorem produces $\hat{H}_{U3}$ unique up to additive constant.
  - §5.2 U4's $V(\hat{x})$ has additive constant ambiguity.
  - §5.3 Both are vacuum-energy zero-point gauge; coincide trivially.

- **§6. Theorem F5 statement.**
  - $\hat{H}_{U3} = \hat{H}_{U4}$ on the U2 Hilbert space, via Galilean-Lie-algebra closure.

- **§7. Falsifier Fal-5 dispatched.**
  - Statement and dispatch argument.
  - Final falsifier table: 7/7 dispatched.

- **§8. U3 arc verdict.**
  - **FORCED** (anticipated).
  - Conditionality ledger: zero new CANDIDATEs introduced.
  - Inherited conditionalities: non-relativistic single-particle scope, gauge-coupling-free scope, U2 inner-product structure, U1 participation-measure structure, U5 momentum-operator structure.

- **§9. Downstream cascade.**
  - §9.1 U4 promotes from FORCED-conditional to FORCED-unconditional retroactively (Framing 1 resolved).
  - §9.2 Schrödinger evolution becomes FORCED-unconditional in both regimes.
  - §9.3 Active upstream-CANDIDATE inventory reduces from $\{U3\}$ + gauge to $\{$ $\}$ + gauge.
  - §9.4 Forced-theorem count rises from 15 to 16 (and U4's status retroactively unconditional).
  - §9.5 All four foundational QM postulates (Born, Bell-Tsirelson, Heisenberg, Schrödinger) structurally derived from ED primitives.
  - §9.6 Phase-1 program structurally complete (modulo description-level continuum gauge convention).

- **§10. Sensitivity flags.**
  - Primitive 13 continuous-time interpretation (load-bears F1 / Fal-7).
  - Galilean-group uniqueness within non-relativistic scope (load-bears F5 / Strategy A).
  - U4 derivation chain (load-bears F5 / identification target).

---

## 10. Recommended Next Steps

**(a) Begin Memo 03 (F5 compatibility derivation + arc verdict).** The natural next step. Following the section outline in §9.2 above, Memo 03 should execute the Galilean-Lie-algebra closure argument (Strategy A) as the primary derivation, with the Stone-theorem uniqueness argument (Strategy B) as cross-check, dispatch the lone remaining falsifier (Fal-5), state the arc verdict (anticipated FORCED), document the downstream cascade (U4 retroactive promotion, Schrödinger emergence promotion, Phase-1 closure), and flag the sensitivity items. The substantive content is the Galilean-algebra argument; the rest is bookkeeping. Anticipated length: comparable to U5 Memo 03 or U4 Memo 03 (one substantive derivation + verdict + cascade).

**(b) Pre-Memo-03 cross-check of U4 §F4 derivation as it appears to F5.** A short cross-check (15–30 minutes) of U4's Galilean-integration derivation, viewed from the F5 identification perspective, to confirm that $\hat{H}_{U4}$'s structural content is exactly what F5 needs to identify with $\hat{H}_{U3}$. Specifically: confirm that U4's derivation produces $\hat{H}_{U4}$ as a self-adjoint operator on the U2 Hilbert space (yes, per U4 paper Theorem F4) and that the operator's form is uniquely determined (yes, modulo $V(\hat{x})$'s additive constant and the inherited mass $m$ + $\hbar$). If U4's derivation has any subtleties bearing on F5 (e.g., domain-of-self-adjointness questions, additive-shift gauge), they should be flagged for explicit treatment in Memo 03 §3.5 / §5.

**(c) Defer memory-record update until Memo 03 closure.** Per Memo 00 §7(c) and Memo 01 §7(c), no memory churn during the arc. The bundled update to `project_qm_emergence_arc.md` will be made after Memo 03 (with optional Memo 04 closure). This memo (Memo 02) does not warrant a separate memory update; its content is recorded in the arc directory and will be summarized in the eventual closure memo.
