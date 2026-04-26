# Memo 02 — Derivations of F1 (Channel-Momentum Identification), F2 (Plane-Wave Eigenfunctions), and F5 (Kinetic + Potential Decomposition)

**Date:** 2026-04-26
**Arc:** `arcs/U4/`
**Predecessors:** [`00_arc_outline.md`](00_arc_outline.md), [`01_decomposition_and_mapping.md`](01_decomposition_and_mapping.md)
**Status:** Derivation memo. Closes the three non-load-bearing sub-features of U4: F1 (channel-momentum identification), F2 (plane-wave eigenfunctions), and F5 (kinetic + potential decomposition). Prepares the structural ground for Memo 03's load-bearing F3 (quadratic-in-$k$ kinetic structure) and F4 (specific coefficient $1/(2m)$). Operates under Framing 1 (U4 conditional on sibling CANDIDATE U3) with explicit U3-independence at every derivation step.
**Purpose:** Settle F1, F2, F5 so Memo 03 can focus entirely on the load-bearing F3 + F4 questions, with explicit scaffolding for the Memo 03 derivations laid here.

---

## 1. F1 — Channel-Momentum Identification

### 1.1 The claim

In the thin / continuum limit of the participation-measure framework, the channel index $K$ admits a continuous momentum-space coordinate $k$. The basis-change between channel-representation and momentum-representation on the U2 Hilbert space is the standard Fourier transform, with the translation generator $\hat{p}$ a self-adjoint operator identified by Stone's theorem.

### 1.2 The structural inputs (all primitive-level kinematic + inherited FORCED)

The derivation uses *only* the following inputs:
- **Primitives 03 (Participation) + 06 (ED Gradient):** supply translation symmetry as a kinematic property of the participation graph. The edge structure does not privilege any particular vertex (Primitive 03 homogeneity); $\nabla \rho$ supplies a spatial direction with no preferred origin (Primitive 06).
- **U2 (FORCED, prior arc):** supplies the sesquilinear inner product on the participation-measure space, hence the Hilbert space $\mathcal{H}$ on which the translation group acts.
- **Stone's theorem (mathematical):** every strongly continuous one-parameter unitary group on a Hilbert space has a unique self-adjoint generator.

**Crucially, no U3-dependent input is used.** Translation symmetry is a *kinematic* property of the participation graph — it concerns the structural homogeneity of the graph itself, not the dynamical evolution of the participation measure. The argument that translations act unitarily on the U2 Hilbert space follows from the inner-product structure (preserved by measure-preserving changes of variable) and not from any time-evolution rule.

### 1.3 The derivation, transferred from U5 Memo 03 §1

**Step 1 — Translation symmetry as a kinematic property.** Define spatial translation $T_a$ acting on the participation-measure space by $(T_a P)_K(u) := P_K(u - a)$. Primitive 03's homogeneity guarantees that the participation relation does not privilege any vertex, so $T_a$ is well-defined on $\mathcal{H}$ for every translation vector $a$ in the spatial tangent space. The set $\{T_a : a \in \mathbb{R}^d\}$ forms a $d$-parameter abelian Lie group under composition.

**Step 2 — Translation acts unitarily on the U2 Hilbert space.** For any $P, Q \in \mathcal{H}$,

$$
\langle T_a P \mid T_a Q \rangle = \sum_K \int du \; P_K^*(u - a) \, Q_K(u - a) = \sum_K \int du' \; P_K^*(u') \, Q_K(u') = \langle P \mid Q \rangle
$$

(under change of variables $u' = u - a$). The translation group preserves the U2 inner product. Continuity of $T_a$ in $a$ follows from continuity of the participation-measure field on the participation graph. Therefore $\{T_a\}$ is a strongly continuous one-parameter unitary group (one parameter per translation direction; $d$-parameter in total for $d$-dimensional space).

**Step 3 — Stone's theorem identifies the translation generator.** Stone's theorem: every strongly continuous one-parameter unitary group on a Hilbert space has a unique self-adjoint generator. Applied to translation, with the ED-program convention placing $\hbar$ in the exponential:

$$
T_a = \exp\!\left(\frac{i \hat{p} \cdot a}{\hbar}\right)
$$

where $\hat{p}$ is the unique self-adjoint translation generator. **Stone's theorem identifies $\hat{p}$ uniquely** — there is no freedom to pick a different generator producing a different conjugate-pair structure.

**Step 4 — Channel-momentum identification.** The eigenstates $|k\rangle$ of $\hat{p}$ satisfy $\hat{p} \, |k\rangle = k \, |k\rangle$ and form a complete orthonormal basis on $\mathcal{H}$ (the momentum basis). In the thin / continuum limit, the channel index $K$ is identified with the momentum eigenvalue $k$:

$$
K \leftrightarrow k \qquad (\text{thin-limit identification})
$$

This is the channel-momentum identification of F1. Channels in the thin-limit continuum *are* momentum eigenstates; momentum eigenvalues *are* the natural continuum channel labels.

### 1.4 Explicit U3-independence

The four steps above invoke:
- Primitive 03 (homogeneity for $T_a$ definition)
- Primitive 06 (spatial axis for translation direction)
- U2 (inner product preserved by $T_a$)
- Stone's theorem (mathematical)

**No time-evolution operator, no Hamiltonian, no Schrödinger equation appears in the derivation.** Stone's theorem gives a self-adjoint generator of the translation group, regardless of whether that generator commutes with any time-evolution operator. The momentum operator $\hat{p}$ exists kinematically on the U2 Hilbert space; whether $\hat{p}$ commutes with a time-evolution generator $\hat{H}$ is a U3-level question, separate from F1's content.

### 1.5 Verdict for F1

**Established.** The channel-momentum identification follows from Stone's theorem applied to the translation group on the U2 Hilbert space, with all inputs primitive-level kinematic plus the now-FORCED U2. **Falsifier Fal-1 (no momentum-basis identification) is dispatched.**

---

## 2. F2 — Plane-Wave Eigenfunctions

### 2.1 The claim

The eigenfunctions of $\hat{p}$ in the position representation are plane waves:

$$
\langle x \mid k \rangle = (2\pi\hbar)^{-d/2} \cdot e^{i k \cdot x / \hbar}
$$

### 2.2 Mathematical content

Given F1's identification of $\hat{p}$ as the translation generator on the U2 Hilbert space, the position-representation form of $\hat{p}$ is determined by the relation between $T_a$ and translation in $x$:

$$
T_a \psi(x) = \psi(x - a) = \exp\!\left( -a \cdot \nabla \right) \psi(x)
$$

(Taylor expansion of the translated argument). Comparing with $T_a = \exp(i \hat{p} \cdot a / \hbar)$:

$$
\frac{i \hat{p} \cdot a}{\hbar} = -a \cdot \nabla \quad \Longrightarrow \quad \hat{p} = -i \hbar \nabla
$$

The eigenvalue equation $\hat{p} \, |k\rangle = k \, |k\rangle$ becomes, in position representation, $-i\hbar \nabla \langle x | k \rangle = k \langle x | k \rangle$, with solution $\langle x | k \rangle = C \cdot e^{i k x / \hbar}$.

### 2.3 Normalisation

The standard normalisation $C = (2\pi\hbar)^{-d/2}$ is fixed by the orthonormality requirement $\langle k | k' \rangle = \delta(k - k')$ together with the Fourier-transform convention. This is *conventional*, not structural — different normalisation conventions give different overall constants but do not affect any structural content.

### 2.4 Definitional vs structural steps

| Step | Status |
|---|---|
| $T_a = \exp(i \hat{p} \cdot a / \hbar)$ from Stone's theorem | Structural (F1) |
| $T_a \psi(x) = \psi(x - a)$ as definition of translation | Definitional |
| $T_a = \exp(-a \cdot \nabla)$ as Taylor-series representation | Mathematical (Taylor expansion) |
| $\hat{p} = -i\hbar \nabla$ in position representation | Mathematical consequence |
| Eigenfunctions are $e^{ikx/\hbar}$ | Mathematical |
| Normalisation $(2\pi\hbar)^{-d/2}$ | Conventional |

No new structural commitment beyond F1.

### 2.5 Verdict for F2

**Established.** Plane-wave eigenfunctions follow automatically from F1 by standard mathematical consequence. F2 introduces no structural commitment beyond what F1 supplies.

---

## 3. F5 — Kinetic + Potential Decomposition

### 3.1 The claim

The Hamiltonian on the participation-measure Hilbert space, in the free-particle-plus-external-potential structure, admits the additive decomposition:

$$
\hat{H} = T(\hat{p}) + V(\hat{x})
$$

with the kinetic part $T(\hat{p})$ depending only on $\hat{p}$ and the potential part $V(\hat{x})$ depending only on $\hat{x}$. Cross terms involving products of $\hat{p}$ and $\hat{x}$ are absent in this scope.

### 3.2 Translation invariance forces the kinetic part to be a function of $\hat{p}$ alone

**Claim.** In the absence of an external potential, $\hat{H}_\mathrm{free}$ commutes with translations: $[\hat{H}_\mathrm{free}, T_a] = 0$ for every translation $T_a$.

**Argument.** The free-particle setting is the participation-graph configuration in which no external structure breaks translation symmetry. The participation graph itself is translation-invariant (Primitive 03 homogeneity); without external coupling, $\hat{H}_\mathrm{free}$ inherits this invariance. Any operator commuting with the translation generator $\hat{p}$ depends on $\hat{p}$ alone via standard functional calculus on self-adjoint operators (a function of $\hat{x}$ would generically not commute with $\hat{p}$, since $[\hat{x}, \hat{p}] = i\hbar$).

Therefore $\hat{H}_\mathrm{free} = T(\hat{p})$ for some function $T : \mathbb{R}^d \to \mathbb{R}$ acting via spectral functional calculus on $\hat{p}$.

### 3.3 Locality forces external potentials to depend only on $\hat{x}$

**Claim.** External potentials, when present, act locally in position representation. The potential operator $\hat{V}$ depends only on $\hat{x}$, not on $\hat{p}$.

**Argument.** Locality is a primitive-level structural property of the participation graph: edges in $E$ connect adjacent vertices, and external influences couple to the participation measure at specific locations $x$. This locality is encoded structurally in Primitive 03's edge structure — participation relations are local, not action-at-a-distance.

In operator language: the local action of a potential on the wavefunction takes the form $(V \psi)(x) = V(x) \psi(x)$ — multiplication by a position-dependent function. This is the form $V(\hat{x})$, depending only on $\hat{x}$.

A potential depending on $\hat{p}$ would be non-local in position representation (a momentum-space multiplication corresponds to a convolution in position space). Convolution-type non-local potentials are structurally distinct from local external potentials and do not arise in the standard non-relativistic-single-particle scope of Phase-1 Step 2.

### 3.4 Cross terms forbidden

Combining §3.2 + §3.3: any cross term $\hat{p} \hat{x}$ or $\hat{x} \hat{p}$ in the Hamiltonian would violate either translation invariance (if interpreted as part of the free Hamiltonian — the $\hat{x}$ factor breaks translation symmetry) or locality (if interpreted as part of the potential — the $\hat{p}$ factor introduces non-local momentum-coupling).

In the free-particle-plus-external-potential scope, cross terms are forbidden, and the decomposition $\hat{H} = T(\hat{p}) + V(\hat{x})$ is uniquely forced.

### 3.5 Scope caveat: gauge-coupling structure

We are explicit about a scope condition. In the presence of magnetic vector potentials $A(\hat{x})$, the kinetic operator becomes $T(\hat{p} - e A(\hat{x})/c)$ — a function of *both* $\hat{p}$ and $\hat{x}$ via the gauge field $A$. This is the standard minimal coupling structure of electromagnetism and does not strictly fit the additive decomposition $T(\hat{p}) + V(\hat{x})$.

The scope condition for U4's F5 is **non-relativistic single-particle Schrödinger emergence without gauge couplings.** Gauge field theory is downstream content (Phase-2 Arc R's QFT extension and beyond), not within Phase-1 Step 2's scope. F5 holds in the scope under which U4 operates; gauge-coupled extensions are addressed by other arcs.

### 3.6 Verdict for F5

**Established (within scope).** The kinetic + potential decomposition $\hat{H} = T(\hat{p}) + V(\hat{x})$ is forced by translation invariance for the free part + locality for the potential part, in the gauge-coupling-free scope of Phase-1 Step 2. **Falsifier Fal-6 (position-momentum cross terms) is dispatched.**

The form of $V$ is structural (scalar function of $\hat{x}$); the *specific* $V$ for a given physical system is inherited from external context, not derived within U4.

---

## 4. Pre-Derivation Setup for F3 — Quadratic-in-$k$ Kinetic Structure

This section lays scaffolding for Memo 03's derivation of $T(\hat{p}) \propto |\hat{p}|^2$. We do not attempt the full F3 derivation here; we identify the structural constraints Memo 03 will use.

### 4.1 What F1 + F5 have already established

After §§1–3 of this memo:
- $\hat{H}$ has the form $T(\hat{p}) + V(\hat{x})$ (F5).
- $T(\hat{p})$ is a function of $\hat{p}$ alone (F5 + F3 setup).
- $\hat{p}$ is the unique self-adjoint translation generator on the U2 Hilbert space (F1).
- Plane-wave eigenfunctions of $\hat{p}$ are $e^{i k x / \hbar}$ (F2).

The remaining question for F3 is: what specific function $T(\hat{p})$? The candidate forms are $|\hat{p}|^\alpha$ for various $\alpha$, plus polynomial combinations $a_0 + a_1 |\hat{p}|^2 + a_2 (|\hat{p}|^2)^2 + \ldots$, plus non-polynomial alternatives ($|\hat{p}| c$ massless, $\sqrt{|\hat{p}|^2 c^2 + m^2 c^4}$ relativistic, etc.).

### 4.2 Structural constraints to be used in Memo 03

Memo 03 will dispatch the candidate alternatives via four constraints:

**(C1) Translation invariance** — already established (F5). Forces $T = T(\hat{p})$ alone.

**(C2) Spatial rotation invariance.** The participation graph supports rotations as a kinematic symmetry (Primitive 03's isotropy + Primitive 06's spatial-axis structure with no preferred direction). $T(\hat{p})$ must commute with rotations. Rotation-invariant functions of $\hat{p}$ depend only on $|\hat{p}|^2$ (the squared magnitude), not on individual components or direction. Therefore:

$$T(\hat{p}) = f(|\hat{p}|^2)$$

for some function $f : \mathbb{R}_{\geq 0} \to \mathbb{R}$.

**(C3) Analyticity at low momentum.** $f$ is analytic in $|\hat{p}|^2$ at $|\hat{p}|^2 = 0$. This is a regularity assumption — physically motivated (no singularities at zero momentum) — and admits a Taylor expansion:

$$f(|\hat{p}|^2) = a_0 + a_1 |\hat{p}|^2 + a_2 (|\hat{p}|^2)^2 + \ldots$$

The constant term $a_0$ is an additive zero-point energy; convention sets $a_0 = 0$.

**(C4) Non-relativistic-limit scope condition.** In the strict non-relativistic limit $|\hat{p}|^2 / (mc)^2 \ll 1$, higher-order terms $a_2 (|\hat{p}|^2)^2$ etc. are suppressed by $(v/c)^2$ and vanish in the strict limit $c \to \infty$ (with $v$ fixed). Only the leading $a_1 |\hat{p}|^2$ term survives.

### 4.3 What remains for Memo 03

Combining C1 + C2 + C3 + C4 within Memo 03 will give:

$$T(\hat{p}) = a_1 |\hat{p}|^2$$

with the higher-order Taylor coefficients suppressed in the non-relativistic limit. This is the quadratic-in-$\hat{p}$ kinetic structure of F3.

The exclusion of *linear-in-$|\hat{p}|$* terms (a candidate $a_{1/2} |\hat{p}|$) is not directly handled by C3 (analyticity in $|\hat{p}|^2$ already excludes odd-power terms in the Taylor expansion) but warrants explicit treatment as a candidate non-relativistic alternative. The $|\hat{p}|c$ form is the photon-like dispersion — relativistic massless behaviour, incompatible with the non-relativistic-massive-particle scope condition.

Memo 03 §1 will execute the full F3 derivation using C1–C4, with explicit treatment of the linear-in-$|\hat{p}|$ candidate via the analyticity argument + non-relativistic-limit scope.

### 4.4 Falsifiers prepared for Memo 03 dispatch

- **Fal-2 (linear-in-$k$):** partially set up via C2 (rotation invariance forbids vector $\alpha \cdot \hat{p}$) plus C3 + C4 (analyticity at low momentum + non-relativistic limit forbid scalar $|\hat{p}|c$ term). Full dispatch in Memo 03.
- **Fal-3 (higher-even-power):** prepared via C4 (strict non-relativistic limit suppresses all $a_n |\hat{p}|^{2n}$ for $n \geq 2$). Full dispatch in Memo 03.
- **Fal-5 (anisotropic):** prepared via C2 (rotation invariance forces dependence on $|\hat{p}|^2$ alone). Full dispatch in Memo 03.
- **Fal-7 (relativistic dispersion in non-rel regime):** scope-conditional; the non-relativistic-limit (C4) is the regime input. Full dispatch in Memo 03 via the scope statement.

---

## 5. Pre-Derivation Setup for F4 — Specific Coefficient $1/(2m)$

### 5.1 The exact gap

After Memo 03 §1 establishes F3 ($T(\hat{p}) = a_1 |\hat{p}|^2$), the load-bearing question for F4 is: **what is the value of $a_1$?**

Dimensional analysis fixes $a_1$ up to a dimensionless constant: $T$ has dimensions of energy, $|\hat{p}|^2$ has dimensions of (momentum)$^2$, so $a_1$ has dimensions of (momentum)$^2$/energy = 1/(mass) (in units where $\hbar$ and $c$ are dimensionful). With the $\hbar$ factor inherited from $\hat{p} = -i\hbar \nabla$, the dimensional form is

$$a_1 = \frac{c_1 \cdot \hbar^2}{m}$$

with $c_1$ a dimensionless constant. The standard non-relativistic kinetic-energy form is

$$T(\hat{p}) = \frac{\hbar^2 |\hat{p}|^2}{2m}$$

corresponding to $c_1 = 1/2$. **The factor of $1/2$ — equivalently, the factor of 2 in the denominator $1/(2m)$ — is the load-bearing question.**

### 5.2 What the existing tightening memo did vs what Memo 03 must do

The 2026-04-24 tightening-program memo (`arcs/arc-foundations/u4_hamiltonian_form_derivation.md` §2.5) silently adopted the factor of 2 by *convention* (matching classical Hamiltonian mechanics: $T_\mathrm{classical} = p^2/(2m)$). Under the 2026-04-26 structural-derivation methodology, this is insufficient: the factor must be derived from primitive-level inputs, not borrowed by convention from classical mechanics (which is itself downstream content not available as input under Framing 1).

Memo 03 §2 must close this gap.

### 5.3 The role of Galilean invariance

The candidate argument: **Galilean invariance forces the factor of 2.**

Under a Galilean boost with velocity $v$, the wavefunction transforms as

$$
\psi(x, t) \to e^{i (m v x - m v^2 t / 2) / \hbar} \, \psi(x - v t, t)
$$

and the momentum operator transforms as $\hat{p} \to \hat{p} + m v$. For the Hamiltonian to transform consistently — specifically, for $\hat{H}'$ to be the boosted-frame Hamiltonian when acting on the boosted wavefunction — the kinetic-energy form $T(\hat{p})$ must satisfy:

$$
T(\hat{p} + m v) - T(\hat{p}) = v \cdot \hat{p} + \frac{1}{2} m v^2 + (\text{other terms cancelling against the boost phase})
$$

The unique $T = T(|\hat{p}|^2)$ satisfying this transformation rule is $T(\hat{p}) = |\hat{p}|^2 / (2m)$. Specifically, the *factor of 2 in the denominator* comes from the $\frac{1}{2} m v^2$ term in the boost phase factor. Any other coefficient breaks Galilean covariance.

### 5.4 The where-does-Galilean-invariance-come-from question

The Galilean argument is structurally valid — it forces the factor of 2 — but it requires Galilean invariance as an *input*. The load-bearing question for Memo 03 is: **where does Galilean invariance come from in the U4 derivation?**

Three framings, restated from Memo 01 §2.4:

- **G1 — Derive Galilean invariance from primitives.** The participation graph in the non-relativistic regime supports observer-shift transformations as a consistent symmetry. Given Primitive 03 (homogeneity), Primitive 06 (spatial-axis structure), and the non-relativistic-limit scope condition, the natural boost structure is Galilean rather than Lorentzian. Under this framing, F4's factor of 2 is forced from primitives + non-rel scope.

- **G2 — Inherit Galilean invariance from the non-relativistic-limit scope.** The non-relativistic scope condition itself implies Galilean invariance, because Galilean is what "non-relativistic" *means* at the boost-symmetry level. Under this framing, F4 is FORCED *given* the non-rel scope, with the scope as a regime choice.

- **G3 — Replace Galilean with an alternative argument.** For example, dimensional analysis combined with a primitive-level energy scale identification. Under this framing, F4 closes without invoking Galilean directly. Memo 03's analysis suggests this framing has limited reach (dimensional analysis alone cannot fix the factor of 2).

### 5.5 Commitment to G1 as the target

**This memo commits to G1 (derive Galilean invariance from primitives) as the target for Memo 03.** The reasoning:

- G1 is the most ambitious framing, most aligned with the structural-derivation methodology of the 2026-04-26 cycle.
- If G1 closes, the U4 verdict is FORCED with one inherited conditionality (U3 sibling CANDIDATE).
- If G1 fails to close cleanly within Memo 03's scope, Memo 03 will fall back to G2 with a scope-conditional verdict.
- G3 is reserved as a last resort if both G1 and G2 fail; the methodology suggests G1 should be tried first.

The G1 sketch (to be elaborated in Memo 03 §2):

1. The participation graph in the non-relativistic regime supports continuous translation symmetry (already established in F1 via Stone's theorem).
2. Time translations are similarly continuous in the participation-graph structure (Primitive 13 relational timing supplies the time-axis; the graph is homogeneous in time as well as space at the primitive level).
3. Combining spatial and temporal translation symmetry, the symmetry group of the participation graph in the non-relativistic regime is the *Galilean group* $\mathrm{Gal}(d) = \mathrm{ISO}(d) \ltimes \mathbb{R}^{d+1}$ (rotations, spatial translations, time translations, and Galilean boosts).
4. The non-relativistic scope condition rules out Lorentzian boost structure (which would mix space and time at $v \sim c$, contradicting the $v \ll c$ regime).
5. Therefore Galilean boosts are admissible kinematic symmetries in the non-relativistic-regime participation graph.
6. Galilean-invariance of the Hamiltonian forces $T(\hat{p}) = |\hat{p}|^2/(2m)$ via the boost-transformation-algebra argument of §5.3 above.

The substantive content of Memo 03 §2 will be making each of these steps rigorous, particularly step 4 (where the regime condition enters) and step 5 (where the structural commitment to Galilean rather than Lorentzian is locked in).

### 5.6 Form-FORCED vs value-INHERITED distinction

Memo 03's verdict for F4 will explicitly separate:
- **Form FORCED.** The dimensional structure $T(\hat{p}) = \hbar^2 |\hat{p}|^2 / (2m)$ — including the factor of 2 — is derived from Galilean invariance (per G1 or G2).
- **Value INHERITED.** The mass $m$ is a per-rule-type empirical parameter inherited per Arc M's "form FORCED, values INHERITED" methodology. The value of $\hbar$ is inherited via the dimensional-atlas Madelung anchoring.

The verdict is FORCED at the form level; specific numerical content is inherited.

---

## 6. Updated Falsifier Status

After Memo 02's derivations of F1, F2, F5:

| Falsifier | Sub-feature | Memo-02 status | Notes |
|---|---|---|---|
| **Fal-1** No momentum-basis identification | F1 | **DISPATCHED** (§1) | Stone's theorem on U2 Hilbert space gives unique $\hat{p}$; channel-momentum identification follows |
| **Fal-2** Linear-in-$k$ kinetic term | F3 | **PARTIALLY DISPATCHED** (§4.4 setup) | Translation invariance + rotation invariance forbid vector $\alpha \cdot \hat{p}$ terms; analyticity + non-rel limit will exclude scalar $|\hat{p}| c$ term in Memo 03 |
| **Fal-3** Higher-even-power terms | F3 | Active for Memo 03 | Setup via §4.2 C4 (non-rel-limit scope); full dispatch in Memo 03 |
| **Fal-4** Coefficient $\neq 1/(2m)$ — wrong factor | F4 | **Active for Memo 03 (THE LOAD-BEARING FALSIFIER)** | Setup via §5; G1 Galilean-invariance argument committed as target |
| **Fal-5** Anisotropic kinetic energy | F3 | **PARTIALLY DISPATCHED** (§4.2 C2 setup) | Rotation invariance forces $T(\hat{p}) = f(|\hat{p}|^2)$; full dispatch with the $f$ form in Memo 03 |
| **Fal-6** Position-momentum cross terms | F5 | **DISPATCHED** (§3.4) | Translation invariance + locality forbid cross terms in the gauge-coupling-free scope |
| **Fal-7** Relativistic dispersion in non-rel regime | F3 | Active for Memo 03 | Scope-conditional; the non-rel-limit (C4) is the regime input |

**Memo-02 dispatch summary:**
- **Fully dispatched:** Fal-1, Fal-6 (two falsifiers).
- **Partially dispatched:** Fal-2, Fal-5 (two falsifiers; setup via F3's C-constraints).
- **Active for Memo 03:** Fal-3, Fal-4, Fal-7 (three falsifiers; F3 + F4 derivations).

The substantive load-bearing falsifier remaining is **Fal-4** (the factor of 2 in $1/(2m)$), to be dispatched in Memo 03 §2 via the Galilean-invariance argument under G1.

---

## 7. Recommended Structure for Memo 03

Based on the audits and pre-derivation setup of Memos 01 and 02, Memo 03 should derive F3 + F4 cleanly with explicit Galilean-invariance commitment.

### Recommended Memo 03 structure

**Title:** `03_F3_F4_and_verdict.md`

**§1. F3 — Quadratic-in-$k$ kinetic structure.**

- **§1.1** Restate the constraints from §4.2 of this memo: C1 (translation invariance), C2 (rotation invariance), C3 (analyticity at low momentum), C4 (non-relativistic-limit scope).
- **§1.2** Apply C1 + C2: $T(\hat{p}) = f(|\hat{p}|^2)$ for some $f : \mathbb{R}_{\geq 0} \to \mathbb{R}$.
- **§1.3** Apply C3: Taylor expansion $f(|\hat{p}|^2) = a_0 + a_1 |\hat{p}|^2 + a_2 (|\hat{p}|^2)^2 + \ldots$ with $a_0 = 0$ by convention.
- **§1.4** Apply C4: in the strict non-relativistic limit, all $a_n$ for $n \geq 2$ are suppressed by $(v/c)^{2(n-1)}$ and vanish. Only $a_1 |\hat{p}|^2$ survives.
- **§1.5** Linear-in-$|\hat{p}|$ alternative ($T = b |\hat{p}|c$) excluded: analyticity in $|\hat{p}|^2$ at $\hat{p} = 0$ forbids non-analytic $|\hat{p}|$ terms; the $|\hat{p}|c$ photon-like dispersion is outside the non-rel-massive-particle scope.
- **§1.6** Verdict for F3: $T(\hat{p}) = a_1 |\hat{p}|^2$ with $a_1$ to be determined in §2.
- **§1.7** Falsifier dispatch for Fal-2, Fal-3, Fal-5, Fal-7.

**§2. F4 — Coefficient $1/(2m)$ via Galilean invariance.**

- **§2.1** The dimensional bridge: $a_1 = c_1 \hbar^2 / m$ for some dimensionless $c_1$. Dimensional analysis alone fixes the form up to $c_1$.
- **§2.2** The factor of 2 question: $c_1 = 1/2$ is the standard non-relativistic value, but dimensional analysis does not fix it. We commit to **G1 (derive Galilean invariance from primitives)** as the load-bearing argument.
- **§2.3** G1 derivation: the participation graph in the non-relativistic regime supports the Galilean group (rotations, spatial translations, time translations, Galilean boosts) as a kinematic symmetry. Spatial translation already established (F1); time translation supplied by Primitive 13; Galilean boost is the load-bearing addition. The non-relativistic-limit scope condition rules out Lorentzian boost structure. Derivation: structural-input audit confirming that the participation-graph structure in the $v \ll c$ regime admits Galilean boost as a consistent observer-shift transformation.
- **§2.4** Galilean-invariance argument: $\hat{H}_\mathrm{kin}$ must transform consistently under the Galilean boost. The unique $T(\hat{p}) = c_1 \hbar^2 |\hat{p}|^2 / m$ satisfying Galilean covariance has $c_1 = 1/2$.
- **§2.5** If G1 fails to close (e.g., if the primitive-level argument for Galilean does not produce the boost symmetry uniquely), fall back to **G2 (inherit Galilean from non-rel scope)** with explicit scope-conditional framing.
- **§2.6** Verdict for F4: form FORCED ($T(\hat{p}) = \hbar^2 |\hat{p}|^2 / (2m)$); value INHERITED ($m$ per Arc M, $\hbar$ per dimensional atlas).
- **§2.7** Falsifier dispatch for Fal-4 (the load-bearing falsifier).

**§3. Final falsifier audit.**

- Consolidate Memo 03's dispatches with Memo 02's prior dispatches.
- All seven falsifiers either DISPATCHED or DISPATCHED-WITHIN-SCOPE.
- Note any outstanding scope conditions (gauge-coupling-free for F5, non-relativistic for F3 + F4) explicitly.

**§4. U4 verdict.**

- Aggregate the five sub-feature derivations (F1, F2, F5 from Memo 02; F3, F4 from this memo).
- State the U4 theorem in formal style (parallel to U5 Memo 03 §4 and U1 Memo 03 §5).
- Conditionalities: U3 (Framing 1), Galilean-invariance source (G1 or G2 per §2.5).
- Sensitivity flags: Primitive 04 bandwidth-additivity (inherited from prior arcs); Arc M chain-mass status (inherited).

**§5. Downstream cascade.**

- With U4 closed, what changes? Schrödinger emergence (Step 2) becomes FORCED conditional on U3 alone.
- Updated active CANDIDATE inventory: {U3} + continuum gauge.
- Note that promoting U3 in a subsequent arc would close the entire QM-emergence Phase-1 structural-foundations program.

**Anticipated length:** moderate to long. The F3 derivation is largely a clean transfer from the existing tightening memo. The F4 derivation under G1 is the substantively novel content and warrants careful treatment. Comparable to U1 Memo 03 or U5 Memo 03.

---

## 8. Recommended Next Steps

**(a) Begin Memo 03 (F3 + F4 derivations + arc verdict).** Natural next session step. The F3 derivation transfers cleanly from existing tightening-program content with the regime caveat noted; the substantive new content is the F4 derivation under G1 (Galilean invariance from primitives). Expected outcome: U4 FORCED with form-FORCED-value-INHERITED framing, conditional on U3 (Framing 1) and possibly also on Galilean-from-non-rel-scope (if G1 falls back to G2).

**(b) Pre-Memo-03 sketch of the G1 Galilean-from-primitives argument.** Before drafting Memo 03, sketch the structural argument that the participation graph in the non-relativistic regime supports Galilean boosts. The argument has three components: (i) spatial translation symmetry already established; (ii) time translation symmetry from Primitive 13; (iii) Galilean boost symmetry as the unique non-relativistic combination. The substantive question is (iii) — whether Galilean boost is *forced* or *one consistent option*. Test the argument before drafting to identify whether G1 closes or whether fallback to G2 is needed.

**(c) Document the form-FORCED-value-INHERITED methodology for F4 explicitly.** Memo 03's verdict for F4 should state, in structured form, exactly what is FORCED (the coefficient form $1/(2m)$) and what is INHERITED ($m$ value, $\hbar$ value), with explicit cross-references to Arc M (for $m$) and the dimensional-atlas Madelung anchoring (for $\hbar$). This methodological transparency is consistent with the discipline established across the prior structural-foundations arcs and prepares the U4 closure memo's positioning.

---

## 9. Cross-references

- Arc outline: [`arcs/U4/00_arc_outline.md`](00_arc_outline.md)
- Memo 01 (decomposition + audits): [`arcs/U4/01_decomposition_and_mapping.md`](01_decomposition_and_mapping.md)
- U5 Memo 03 §1 (Stone's-theorem template for F1 transfer): [`arcs/U5/03_F3_F5_and_verdict.md`](../U5/03_F3_F5_and_verdict.md)
- Existing tightening-program memo (audit target; F3 content transfers from §§2.1–2.4 + 3 + 4): [`arcs/arc-foundations/u4_hamiltonian_form_derivation.md`](../arc-foundations/u4_hamiltonian_form_derivation.md)
- U2-Inner-Product paper (U2 Hilbert space inherited as input for F1): [`papers/U2_Inner_Product/paper_u2_inner_product.md`](../../papers/U2_Inner_Product/paper_u2_inner_product.md)

**Source primitives:**
- Primitive 03 (Participation, supplies homogeneity for translation symmetry): `quantum/primitives/03_participation.md`
- Primitive 04 (Bandwidth, supplies $|P|^2 = b$ via U1): `quantum/primitives/04_participation_bandwidth.md`
- Primitive 06 (ED Gradient, supplies spatial axis): `quantum/primitives/06_ed_gradient.md`
- Primitive 13 (Relational Timing, supplies time axis for §5.5 G1 argument): `quantum/primitives/13_relational_timing.md`

**Arc M (chain-mass framework):**
- `papers/Arc_M/paper_arc_m.md` — "form FORCED, values INHERITED" framing for $m$ inheritance.

---

## 10. One-line memo summary

> **F1 (channel-momentum identification) is established by transfer of the U5 Memo 03 §1 Stone's-theorem argument: the participation graph's translation symmetry (Primitives 03 + 06, kinematic) acts unitarily on the U2 Hilbert space, Stone's theorem identifies the unique self-adjoint translation generator $\hat{p}$, and channels in the thin/continuum limit are identified with momentum eigenvalues. Explicitly U3-INDEPENDENT: no time-evolution operator enters the derivation. F2 (plane-wave eigenfunctions $\langle x|k\rangle = (2\pi\hbar)^{-d/2} e^{ikx/\hbar}$) follows automatically from F1 via $\hat{p} = -i\hbar\nabla$ in position representation; mathematical consequence with no new structural commitment. F5 (kinetic + potential decomposition $\hat{H} = T(\hat{p}) + V(\hat{x})$) is established by translation invariance forcing the free-particle Hamiltonian to depend on $\hat{p}$ alone + locality of external potentials forcing $V$ to depend on $\hat{x}$ alone + cross terms forbidden; scope condition: gauge-coupling-free (gauge-coupled extensions are downstream Arc R / QFT content). F3 (quadratic-in-$k$ kinetic structure) pre-derivation setup: four constraints C1 translation + C2 rotation + C3 analyticity + C4 non-relativistic-limit will give $T(\hat{p}) = a_1 |\hat{p}|^2$ in Memo 03 §1. F4 (coefficient $1/(2m)$) pre-derivation setup: dimensional analysis fixes $a_1 = c_1 \hbar^2/m$ with $c_1$ dimensionless; the factor-of-2 ($c_1 = 1/2$) is the load-bearing question requiring Galilean invariance. Three framings: G1 derive Galilean from primitives (target), G2 inherit Galilean from non-rel scope (fallback), G3 alternative (last resort). Updated falsifier status: Fal-1 + Fal-6 fully dispatched; Fal-2 + Fal-5 partially dispatched (setup via F3 C-constraints); Fal-3 + Fal-7 active for Memo 03; Fal-4 (factor of 2) is the substantive load-bearing falsifier active for Memo 03 §2.**
