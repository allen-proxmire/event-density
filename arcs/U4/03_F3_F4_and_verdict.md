# Memo 03 — F3 (Quadratic-in-$k$ Kinetic Structure), F4 (Coefficient $1/(2m)$), and U4 Arc Verdict

**Date:** 2026-04-26
**Arc:** `arcs/U4/`
**Predecessors:** [`00_arc_outline.md`](00_arc_outline.md), [`01_decomposition_and_mapping.md`](01_decomposition_and_mapping.md), [`02_F1_F2_F5_derivations.md`](02_F1_F2_F5_derivations.md)
**Status:** Load-bearing memo of the U4 arc. Settles the two outstanding sub-features: F3 (quadratic-in-$k$ kinetic structure) via the four-constraint argument C1–C4 prepared in Memo 02, and F4 (specific coefficient $1/(2m)$) via the G1 Galilean-invariance derivation. Delivers the U4 arc verdict and characterises the downstream cascade.
**Purpose:** Close the U4 arc with a theorem-grade verdict on the specific Hamiltonian form $\hat{H} = \hbar^2 |\hat{p}|^2 / (2m) + V(\hat{x})$.

---

## 1. The State of the Arc Entering Memo 03

After Memos 01–02, three of five U4 sub-features are established:

- **F1 (channel-momentum identification):** established via Stone's theorem on the translation group, U3-independent.
- **F2 (plane-wave eigenfunctions):** automatic given F1.
- **F5 (kinetic + potential decomposition):** established via translation invariance + locality, in the gauge-coupling-free scope.

Two sub-features remain:

- **F3 (quadratic-in-$k$ kinetic structure):** load-bearing; to be derived via the four-constraint argument (C1 translation, C2 rotation, C3 analyticity, C4 non-relativistic-limit) prepared in Memo 02 §4.
- **F4 (specific coefficient $1/(2m)$):** load-bearing for form (with $m$ INHERITED per Arc M, $\hbar$ INHERITED per dimensional-atlas Madelung); to be derived via the G1 Galilean-invariance argument prepared in Memo 02 §5.

Five falsifiers remain active or partially active: **Fal-2** (linear-in-$k$, partially set up), **Fal-3** (higher-even-power), **Fal-4** (factor-of-2, the substantive load-bearing falsifier), **Fal-5** (anisotropic, partially set up), **Fal-7** (relativistic dispersion in non-rel regime). This memo dispatches all five.

The arc operates under **Framing 1**: U4 is derived *given* the existence of a Hermitian Hamiltonian generator (which is U3's content). U3 is a sibling CANDIDATE and is not invoked as a derivation input.

---

## 2. Derivation of F3 — Quadratic-in-$k$ Kinetic Structure

### 2.1 The claim

The free-kinetic-energy operator $T(\hat{p})$ on the participation-measure Hilbert space takes the form

$$T(\hat{p}) = a_1 |\hat{p}|^2$$

with $a_1$ a positive real constant (its specific value to be determined in §3 by F4). Linear-in-$|\hat{p}|$ terms are absent. Higher-even-power terms ($|\hat{p}|^4, |\hat{p}|^6, \ldots$) are absent in the strict non-relativistic limit. Anisotropic and direction-dependent terms are absent.

### 2.2 The four constraints (recap from Memo 02 §4)

The derivation uses four structural constraints, all primitive-level + scope-conditional + inherited from prior FORCED items:

- **(C1) Translation invariance.** $T = T(\hat{p})$ depends on $\hat{p}$ alone; established in Memo 02 §3.2 via Primitive 03 homogeneity of the participation graph.
- **(C2) Spatial rotation invariance.** The participation graph supports rotations as a kinematic symmetry (graph isotropy from Primitive 03 + Primitive 06's spatial-axis structure with no preferred direction).
- **(C3) Analyticity at low momentum.** $T(\hat{p}) = f(|\hat{p}|^2)$ is analytic in $|\hat{p}|^2$ at $\hat{p} = 0$. Regularity assumption — physically motivated and standard in non-relativistic QM.
- **(C4) Non-relativistic-limit scope condition.** $|\hat{p}|^2 / (mc)^2 \ll 1$. Inherited from Phase-1 Step 2's scope.

### 2.3 Step 1 — From C1 + C2 to $f(|\hat{p}|^2)$

By C1, $T = T(\hat{p})$. By C2, $T$ is invariant under rotations of $\hat{p}$. The most general rotation-invariant function of a vector operator $\hat{p}$ depends only on the rotational invariants formed from $\hat{p}$. The unique such invariant (up to powers) is the squared magnitude $|\hat{p}|^2 = \hat{p} \cdot \hat{p}$. Therefore:

$$T(\hat{p}) = f(|\hat{p}|^2) \qquad (1)$$

for some function $f : \mathbb{R}_{\geq 0} \to \mathbb{R}$.

**Anisotropic alternatives dismissed.** Any anisotropic candidate — e.g., $T = c_x \hat{p}_x^2 + c_y \hat{p}_y^2 + c_z \hat{p}_z^2$ with $c_x \neq c_y \neq c_z$, or $T = (\hat{p} \cdot \hat{n})^2$ for a fixed direction $\hat{n}$ — fails C2 by selecting a preferred direction in space. **Falsifier Fal-5 (anisotropic kinetic energy) is dispatched.**

### 2.4 Step 2 — Taylor expansion under C3

By C3, $f$ is analytic at $|\hat{p}|^2 = 0$, admitting a Taylor expansion:

$$f(|\hat{p}|^2) = a_0 + a_1 |\hat{p}|^2 + a_2 (|\hat{p}|^2)^2 + a_3 (|\hat{p}|^2)^3 + \ldots \qquad (2)$$

The constant term $a_0$ is an additive zero-point energy. Convention sets $a_0 = 0$ (no zero-point shift); equivalently, the kinetic-energy operator vanishes at zero momentum.

**Half-integer powers excluded by C3.** A candidate term of the form $a_{1/2} |\hat{p}|$ — i.e., proportional to $\sqrt{|\hat{p}|^2}$ — is *not analytic* in $|\hat{p}|^2$ at the origin (the square-root function has a branch point). Such a term is excluded by the analyticity assumption C3. Physically, the $|\hat{p}| c$ form is the photon-like dispersion of a massless particle — relativistic massless behaviour, incompatible with the non-relativistic massive-particle scope condition C4.

The $|\hat{p}| c$ form is also excluded by C2 in vector form: a candidate $\alpha \cdot \hat{p}$ (linear in components of $\hat{p}$) is not rotation-invariant unless $\alpha = 0$. **Falsifier Fal-2 (linear-in-$k$ kinetic term) is dispatched.**

### 2.5 Step 3 — C4 suppresses higher-even-power terms

In the non-relativistic regime $|\hat{p}|^2 / (mc)^2 \ll 1$, the relative size of the $a_n (|\hat{p}|^2)^n$ term to the $a_1 |\hat{p}|^2$ term is

$$\frac{a_n (|\hat{p}|^2)^n}{a_1 |\hat{p}|^2} = \frac{a_n}{a_1} (|\hat{p}|^2)^{n-1}$$

For dimensional consistency, $a_n$ has the natural scaling

$$a_n \sim \frac{a_1}{(m c)^{2(n-1)}}$$

(the only natural dimensional combination involving the relativistic-scale $mc$). Substituting:

$$\frac{a_n (|\hat{p}|^2)^n}{a_1 |\hat{p}|^2} \sim \left( \frac{|\hat{p}|^2}{(mc)^2} \right)^{n-1} = \left( \frac{v}{c} \right)^{2(n-1)}$$

where $v$ is the characteristic velocity ($v \ll c$ in the non-relativistic regime). Higher-order terms are suppressed by powers of $(v/c)^2$.

**In the strict non-relativistic limit $c \to \infty$ (with $v$ fixed),** all $a_n$ for $n \geq 2$ vanish. Only the leading $a_1 |\hat{p}|^2$ term survives.

**Falsifier Fal-3 (higher-even-power terms) is dispatched** — these terms exist in the relativistic regime (as $1/c^2$ corrections to $|\hat{p}|^2/(2m)$) but are explicitly suppressed in the non-relativistic scope.

### 2.6 Step 4 — Relativistic dispersion in non-relativistic regime

A candidate alternative to the polynomial Taylor expansion: the full relativistic dispersion

$$T_\mathrm{rel}(\hat{p}) = \sqrt{|\hat{p}|^2 c^2 + m^2 c^4} - m c^2$$

is the relativistic kinetic energy (subtracting rest energy). Expanding in $|\hat{p}|^2 / (mc)^2 \ll 1$:

$$T_\mathrm{rel}(\hat{p}) = \frac{|\hat{p}|^2}{2m} - \frac{|\hat{p}|^4}{8 m^3 c^2} + O\!\left( \frac{|\hat{p}|^6}{m^5 c^4} \right)$$

In the strict non-relativistic limit $c \to \infty$, only the leading $|\hat{p}|^2/(2m)$ term survives; higher-order relativistic corrections vanish.

**Falsifier Fal-7 (relativistic dispersion in non-relativistic regime) is dispatched** — the relativistic dispersion *reduces* to the U4 form in the non-relativistic limit, consistent with U4's scope condition. Phase-2 Arc R handles the relativistic regime; U4 is the Phase-1 non-relativistic content.

### 2.7 Net F3 form

Combining §§2.3–2.6:

$$T(\hat{p}) = a_1 |\hat{p}|^2 \qquad (3)$$

with $a_1$ a positive real constant whose specific value is determined in §3.

### 2.8 Verdict for F3

**Established.** The free-kinetic-energy operator is uniquely quadratic in $|\hat{p}|^2$ in the non-relativistic regime, with all alternative forms (anisotropic, linear-in-$|\hat{p}|$, higher-even-power, relativistic) excluded by the four constraints C1–C4.

**Falsifiers dispatched:** Fal-2, Fal-3, Fal-5, Fal-7.

The argument is U3-independent (it operates on the kinematic structure of the U2 Hilbert space + scope condition, with no time-evolution operator invoked).

---

## 3. Derivation of F4 — Coefficient $1/(2m)$ via G1 Galilean Invariance

### 3.1 The claim

The constant $a_1$ in $T(\hat{p}) = a_1 |\hat{p}|^2$ takes the specific form

$$a_1 = \frac{1}{2m}$$

(in units where $\hbar$ is implicit in the momentum operator $\hat{p} = -i\hbar\nabla$; equivalently $a_1 = \hbar^2/(2m)$ in standard units), with $m$ a per-rule-type mass parameter inherited per Arc M's "form FORCED, values INHERITED" methodology.

The substantive derivation question: **the factor of 2 in $1/(2m)$**. Dimensional analysis fixes $a_1 \propto 1/m$ but does not fix the numerical prefactor. The G1 argument under Galilean invariance derives the factor of 2 from the Galilean Lie algebra structure.

### 3.2 G1 Step 1 — Primitive-level definition of boosts

A Galilean boost with velocity $v$ is the observer-shift transformation

$$x \to x + v t, \qquad t \to t \qquad (4)$$

— space and time transform together, with absolute time preserved. An observer moving with velocity $v$ relative to the original frame sees coordinates shifted by $vt$ at time $t$.

For (4) to be a kinematic symmetry of the participation graph, the structural relations (edges, bandwidth, channel structure) must be invariant under the transformation. Three structural inputs combine to support this:

- **Primitive 03 (Participation):** supplies translation symmetry of the graph — no spatial position is privileged.
- **Primitive 13 (Relational Timing):** supplies time-translation symmetry — no time is privileged.
- **Non-relativistic-limit scope condition (C4):** preserves absolute time $t \to t$ under observer shifts (in the relativistic regime, time would mix with space under boosts via Lorentz transformation; the non-relativistic scope rules out Lorentzian boost structure).

Combining these three: in the non-relativistic regime, observer-shift transformations $x \to x + vt$ are admissible kinematic symmetries of the participation graph.

### 3.3 G1 Step 2 — Commutation structure of translations + boosts

The Galilean Lie algebra is generated by:
- **Spatial translation generators** $\hat{P}_i$, with $[\hat{P}_i, \hat{P}_j] = 0$ (translations commute).
- **Time translation generator** $\hat{H}$ (time-evolution Hamiltonian).
- **Spatial rotation generators** $\hat{J}_i$, with the standard $\mathfrak{so}(d)$ algebra.
- **Galilean boost generators** $\hat{K}_i$.

The substantive structural fact is the commutation relation between boosts and translations:

$$[\hat{K}_i, \hat{P}_j] = i \hbar m \, \delta_{ij} \qquad (5)$$

— a *non-zero* commutator with the mass $m$ as the structure constant. This is the **central extension** of the classical Galilean algebra: in classical kinematics $\{K_i, P_j\}_\mathrm{Poisson} = m \delta_{ij}$, and the quantum version has $[\hat{K}_i, \hat{P}_j] = i \hbar m \delta_{ij}$.

The boost generator takes the form

$$\hat{K}_i = m \hat{x}_i - t \hat{p}_i \qquad (6)$$

(in the convention where $\hat{K}_i$ generates the boost via $|\psi\rangle \to e^{i \hat{K} \cdot v / \hbar} |\psi\rangle$). The factor of $m$ is built into the boost generator.

The other Galilean commutators include

$$[\hat{H}, \hat{K}_i] = -i\hbar \hat{p}_i \qquad (7)$$

(time-derivative of the boost generator equals the momentum). This is the load-bearing commutation relation for F4.

### 3.4 G1 Step 3 — Uniqueness of the non-relativistic boost algebra

**Claim.** In the non-relativistic regime (C4 + absolute time), the Galilean Lie algebra is the unique consistent boost-translation algebra.

**Argument.** The candidate boost-translation algebras compatible with absolute time fall into two categories:

- **Galilean group $\mathrm{Gal}(d)$.** Boosts and translations generate the Galilean Lie algebra with commutator (5). Time is absolute. Mass is the central charge.
- **Lorentzian group $\mathrm{ISO}(d, 1)$.** Boosts mix space and time. Time is *not* absolute; observers in different inertial frames see different time intervals.

In the non-relativistic regime, time is absolute by scope condition (C4). Lorentzian boost structure is therefore ruled out. The Galilean group is the unique remaining alternative.

Within the Galilean group, the central extension is unique up to the choice of central charge. The central charge is identified with mass $m$, which is a per-rule-type parameter inherited per Arc M.

**Galilean is uniquely forced within the non-relativistic scope condition that U4 already inherits.**

### 3.5 G1 Step 4 — Compatibility with the U2 inner product

The Galilean transformations must act unitarily on the U2 Hilbert space for the Galilean algebra to be a symmetry of the participation-measure framework.

- **Translations $\hat{p}$:** unitary by F1 (Stone's theorem on translation symmetry).
- **Time translations $\hat{H}$:** assumed self-adjoint under Framing 1 (U3 supplies the existence of a Hermitian Hamiltonian generator).
- **Spatial rotations $\hat{J}$:** unitary by C2 (rotation symmetry of the participation graph).
- **Galilean boosts $\hat{K} = m \hat{x} - t \hat{p}$:** the position operator $\hat{x}$ is self-adjoint (multiplication by a real coordinate); $\hat{p}$ is self-adjoint (Stone's theorem); $\hat{K}$ is self-adjoint as a real-coefficient linear combination. Therefore boosts act unitarily on $\mathcal{H}$.

All Galilean transformations are unitary on the U2 Hilbert space. The Galilean group is a symmetry group of the participation-measure framework in the non-relativistic regime.

### 3.6 G1 Step 5 — Transformation of momentum under boosts

Under an infinitesimal Galilean boost with velocity $v$, the momentum operator transforms as

$$\hat{p}_j \to \hat{p}_j' = e^{i \hat{K} \cdot v / \hbar} \hat{p}_j e^{-i \hat{K} \cdot v / \hbar}$$

Expanding to first order in $v$:

$$\hat{p}_j' = \hat{p}_j + \frac{i v_i}{\hbar} [\hat{K}_i, \hat{p}_j] + O(v^2) = \hat{p}_j + \frac{i v_i}{\hbar} \cdot i \hbar m \, \delta_{ij} + O(v^2) = \hat{p}_j - m v_j + O(v^2)$$

For a finite boost (using BCH or direct integration of the infinitesimal transformation):

$$\hat{p} \to \hat{p}' = \hat{p} - m v \qquad (8)$$

(active transformation; the passive transformation has the opposite sign). The *mass* enters as the proportionality factor between boost velocity and momentum shift — exactly as in classical kinematics.

### 3.7 G1 Step 6 — Forced identification of the kinetic term as $|\hat{p}|^2 / (2m)$

The Hamiltonian $\hat{H} = T(\hat{p})$ must satisfy the Galilean commutation relation (7):

$$[\hat{H}, \hat{K}_i] = -i\hbar \hat{p}_i$$

Substituting $\hat{K}_i = m \hat{x}_i - t \hat{p}_i$ and using $[\hat{H}, \hat{p}_i] = 0$ (since $\hat{H}$ is a function of $\hat{p}$ alone, by F3):

$$[\hat{H}, \hat{K}_i] = m [T(\hat{p}), \hat{x}_i] - t [T(\hat{p}), \hat{p}_i] = m [T(\hat{p}), \hat{x}_i]$$

Using the canonical commutation $[\hat{x}_i, \hat{p}_j] = i \hbar \delta_{ij}$ and the identity $[T(\hat{p}), \hat{x}_i] = -i\hbar (\partial T/\partial \hat{p}_i)$:

$$[\hat{H}, \hat{K}_i] = m \cdot (-i\hbar) \frac{\partial T(\hat{p})}{\partial \hat{p}_i}$$

Setting equal to $-i\hbar \hat{p}_i$:

$$-i\hbar m \frac{\partial T(\hat{p})}{\partial \hat{p}_i} = -i\hbar \hat{p}_i \quad \Longrightarrow \quad \frac{\partial T(\hat{p})}{\partial \hat{p}_i} = \frac{\hat{p}_i}{m} \qquad (9)$$

Equation (9) is a system of differential equations for $T(\hat{p})$. Integrating component by component (using the F3 result $T = f(|\hat{p}|^2)$, so $\partial T / \partial \hat{p}_i = 2 \hat{p}_i f'(|\hat{p}|^2)$):

$$2 \hat{p}_i f'(|\hat{p}|^2) = \frac{\hat{p}_i}{m} \quad \Longrightarrow \quad f'(|\hat{p}|^2) = \frac{1}{2m}$$

Integrating with the convention $f(0) = 0$ (zero kinetic energy at zero momentum):

$$f(|\hat{p}|^2) = \frac{|\hat{p}|^2}{2m} \qquad (10)$$

**The factor of 2 emerges from the integration.** Specifically: the coefficient $1/(2m)$ in $T = |\hat{p}|^2/(2m)$ comes from integrating $f'(|\hat{p}|^2) = 1/(2m)$ — the factor of 2 is the *Jacobian* relating the chain-rule derivative $\partial T/\partial \hat{p}_i = 2 \hat{p}_i f'(|\hat{p}|^2)$ to the form of the Galilean commutator. **It is not a convention; it is the result of integrating the differential equation that Galilean invariance demands.**

### 3.8 Combining F3 + F4

Combining (3) and (10), and restoring $\hbar$ explicitly (since $\hat{p} = -i\hbar\nabla$ has explicit $\hbar$):

$$T(\hat{p}) = \frac{\hbar^2 |\hat{p}|^2}{2m} \qquad (11)$$

with $m$ inherited per Arc M and $\hbar$ inherited per the dimensional-atlas Madelung anchoring.

**Falsifier Fal-4 (coefficient $\neq 1/(2m)$, wrong factor) is dispatched.** The factor of 2 is forced by the Galilean Lie algebra structure (specifically, by integrating the Galilean commutator condition (9) on $T$).

### 3.9 G1 successfully closes within the non-relativistic scope

The G1 Galilean-from-primitives argument closes under the following structural inputs:
- Primitive 03 (translation symmetry).
- Primitive 13 (time-translation symmetry).
- Non-relativistic-limit scope condition (preserves absolute time, rules out Lorentzian boost structure).
- C2 (rotation invariance) and the U2 inner product (for unitarity).
- F1 (Stone's theorem identifying $\hat{p}$).
- Standard Lie algebra calculations (no new structural commitment).

**No new structural commitment is introduced beyond what U4 already inherits.** The non-relativistic scope condition is the same scope that conditions all of U4's content; it is not a new conditional introduced by F4 specifically.

### 3.10 Verdict for F4

**Established (form FORCED; values INHERITED).** The kinetic-energy form is

$$T(\hat{p}) = \frac{\hbar^2 |\hat{p}|^2}{2m}$$

with the factor of 2 forced by the Galilean Lie algebra structure within the non-relativistic scope. The mass $m$ is inherited per Arc M's "form FORCED, values INHERITED" methodology; $\hbar$ is inherited via the dimensional-atlas Madelung anchoring.

The argument is U3-independent at the derivation level (the Galilean commutator algebra is a kinematic structure on the U2 Hilbert space; U3 supplies the existence of the time-evolution generator $\hat{H}$, which is taken as inherited under Framing 1).

**Falsifier Fal-4 is dispatched.**

---

## 4. Fallback Analysis under G2

The G1 argument closes successfully in §3 above. We document the fallback analysis under G2 for completeness, in case future structural revisions identify a gap in the G1 argument.

### 4.1 G2 framing

G2 inherits Galilean invariance from the non-relativistic-limit scope condition, treating Galilean as a *property of the regime* rather than a *derived consequence of primitives + regime*.

Under G2, the non-relativistic scope condition is itself defined to include Galilean invariance: "non-relativistic" means "absolute time + Galilean boost symmetry." The factor of 2 in $1/(2m)$ then follows from the same boost-algebra integration argument as in §3.7.

### 4.2 Verdict differential between G1 and G2

The two framings produce structurally identical derivations of the factor of 2; the difference is in the structural conditionality:

- **G1 verdict:** F4 FORCED, with the non-relativistic scope condition as the only inherited conditional (which U4 already inherits).
- **G2 verdict:** F4 FORCED conditional on Galilean invariance being *part of the regime definition*, which is a slightly weaker structural claim — Galilean is treated as a regime input rather than a derived property.

Practically, the difference is small: under G1, the regime condition + primitives produces Galilean invariance; under G2, the regime condition includes Galilean invariance directly. Either way, the factor of 2 is forced by the boost algebra; the verdict is FORCED.

### 4.3 Why G1 is preferable

G1 is more aligned with the structural-derivation methodology of the 2026-04-26 cycle: Galilean invariance is *derived* from the joint action of three primitives (03, 13) plus the regime condition, rather than being treated as an independent regime input.

The G1 argument's substantive content — that the regime condition + Primitive 03 (spatial translations) + Primitive 13 (time translations) + the structural homogeneity of the participation graph in $v \ll c$ regime forces Galilean rather than Lorentzian boost structure — is genuinely a derivation, not a definition.

Under G1, U4's verdict is FORCED with no novel conditionality (only the inherited non-relativistic scope). Under G2, U4's verdict is FORCED conditional on Galilean-as-regime-component, which is essentially the same conditionality re-described.

**The U4 arc adopts G1 as the canonical framing.**

---

## 5. Final Falsifier Audit

We consolidate all seven falsifiers from Memo 00 §4.1 with their dispatch status across Memos 02–03:

| Falsifier | Sub-feature | Dispatch location | Status |
|---|---|---|---|
| **Fal-1** No momentum-basis identification | F1 | Memo 02 §1 | **DISPATCHED** |
| **Fal-2** Linear-in-$k$ kinetic term | F3 | Memo 03 §2.4 (analyticity + rotation) | **DISPATCHED** |
| **Fal-3** Higher-even-power terms | F3 | Memo 03 §2.5 (non-rel-limit scope) | **DISPATCHED** (within scope) |
| **Fal-4** Coefficient $\neq 1/(2m)$ — wrong factor | F4 | Memo 03 §3.7 (Galilean boost algebra) | **DISPATCHED** |
| **Fal-5** Anisotropic kinetic energy | F3 | Memo 03 §2.3 (rotation invariance) | **DISPATCHED** |
| **Fal-6** Position-momentum cross terms | F5 | Memo 02 §3 | **DISPATCHED** (within gauge-coupling-free scope) |
| **Fal-7** Relativistic dispersion in non-rel regime | F3 | Memo 03 §2.6 (scope condition) | **DISPATCHED** (within scope; relativistic dispersion reduces to U4 form in non-rel limit) |

**All seven falsifiers are dispatched.** No physical-distinction alternative survives under U4's stated scope conditions (non-relativistic single-particle, gauge-coupling-free).

### 5.1 Outstanding scope conditions

Two scope conditions remain explicit:
- **Non-relativistic regime** (C4). Conditions F3 (suppresses higher-even-power terms; rules out $|\hat{p}| c$ dispersion; rules out full relativistic dispersion) and F4 (selects Galilean boost structure over Lorentzian).
- **Gauge-coupling-free regime** (F5 §3.5). Conditions the kinetic + potential decomposition; magnetic vector potentials produce $T(\hat{p} - eA(\hat{x})/c)$ which couples position and momentum.

Both scope conditions are inherited from Phase-1 Step 2's framing. Neither is a new conditional introduced by U4.

---

## 6. The U4 Verdict

### 6.1 Statement

> **Theorem (U4; Specific Hamiltonian Form / Momentum-Basis Identification).** Let the ED primitive stack supply: bandwidth (Primitive 04), spatial structure (Primitive 06), participation relations (Primitive 03), channel index (Primitive 07), tension polarity (Primitive 09), and relational timing (Primitive 13), together with the now-FORCED upstream items U1, U2-Discrete, U2-Continuum, U5, and Theorem 10. Within the non-relativistic single-particle scope of Phase-1 Step 2 (gauge-coupling-free), and *conditional on the existence of a Hermitian Hamiltonian generator* (sibling CANDIDATE U3, Framing 1), the Hamiltonian operator on the participation-measure Hilbert space takes the unique form
>
> $$\hat{H} = \frac{\hbar^2 |\hat{p}|^2}{2m} + V(\hat{x})$$
>
> with the following structural properties:
>
> 1. **Channel-momentum identification.** In the thin/continuum limit, the channel index $K$ is identified with the momentum eigenvalue $k$ via Stone's theorem on the translation group. Plane-wave eigenfunctions $\langle x | k \rangle = (2\pi\hbar)^{-d/2} e^{i k x / \hbar}$ supply the position-momentum basis change.
>
> 2. **Kinetic + potential decomposition.** $\hat{H} = T(\hat{p}) + V(\hat{x})$ — kinetic depending only on momentum, potential depending only on position. Translation invariance forces the free part; locality forces the potential part.
>
> 3. **Quadratic-in-$k$ kinetic structure.** $T(\hat{p}) = a_1 |\hat{p}|^2$ uniquely, by the four constraints C1 (translation) + C2 (rotation) + C3 (analyticity) + C4 (non-relativistic-limit). Linear-in-$|\hat{p}|$, higher-even-power, anisotropic, and relativistic-dispersion alternatives all dismissed.
>
> 4. **Specific coefficient $\hbar^2/(2m)$.** $a_1 = \hbar^2/(2m)$, with the factor of 2 forced by the Galilean Lie algebra commutation relation $[\hat{H}, \hat{K}_i] = -i\hbar \hat{p}_i$ integrated against $\hat{K} = m\hat{x} - t\hat{p}$. The mass $m$ is inherited per Arc M's "form FORCED, values INHERITED" methodology; $\hbar$ is inherited via the dimensional-atlas Madelung anchoring.
>
> 5. **Form $V(\hat{x})$.** The potential takes the form of a scalar function of position; the *specific* $V$ for a given physical system is inherited from external context.

**Status: FORCED with form-FORCED-value-INHERITED framing.**

### 6.2 Conditionalities

The U4 verdict is conditional on:

1. **U3 (sibling CANDIDATE; Framing 1).** The existence of a Hermitian Hamiltonian generator. U4 specifies the form of $\hat{H}$ given that $\hat{H}$ exists; U3 supplies the existence. Promoting U3 in a subsequent arc would make U4 fully unconditional.

2. **Non-relativistic single-particle scope** (Phase-1 Step 2). Higher-even-power terms vanish in this scope; Galilean boost structure is the unique consistent boost algebra.

3. **Gauge-coupling-free scope.** The kinetic + potential decomposition holds in the absence of magnetic vector potentials; gauge-coupled extensions are downstream content.

4. **Inherited values** (per Arc M for $m$; per dimensional-atlas Madelung for $\hbar$). The U4 verdict is at the *form* level; specific numerical content is inherited from prior structural commitments.

The first conditional is the natural sibling-CANDIDATE conditional; the second and third are scope conditions inherited from Phase-1 Step 2's framing; the fourth is the form-FORCED-value-INHERITED methodology established by Arc M and applied uniformly across the structural-foundations cycle.

### 6.3 One-paragraph justification

The U4 verdict is **FORCED**: the specific Hamiltonian form $\hat{H} = \hbar^2 |\hat{p}|^2/(2m) + V(\hat{x})$ is uniquely determined by the participation-measure framework's primitive structure plus the inherited FORCED items (U1, U2, U5, Theorem 10), within the non-relativistic single-particle gauge-coupling-free scope of Phase-1 Step 2 and conditional on U3 (Framing 1). The substantive load was concentrated on F3 (quadratic-in-$|\hat{p}|^2$ structure, derived via translation + rotation + analyticity + non-relativistic-limit) and F4 (factor of 2 in $1/(2m)$, derived via the G1 Galilean-from-primitives argument; the factor emerges from integrating the Galilean commutation relation $[\hat{H}, \hat{K}] = -i\hbar \hat{p}$ against $\hat{K} = m\hat{x} - t\hat{p}$, not from convention). All seven falsifiers are dispatched. The U4 verdict introduces no new CANDIDATEs, only inherited conditionalities (U3, non-rel scope, gauge-coupling-free scope, mass-value via Arc M, $\hbar$-value via dimensional atlas) — all of which were already present in the program structure before U4 closed. The arc adds the fifth of the structural-foundations-cycle theorems and brings the QM-emergence Phase-1 program to within one arc (U3) of complete structural foundations across all four foundational postulates plus the description-level continuum gauge.

---

## 7. Downstream Structural Consequences

### 7.1 Phase-1 structural ledger

| Cycle position | New theorem | Status |
|---|---|---|
| born_gleason | Theorem 10 (Born) | FORCED |
| U2-Discrete | Theorem #11 | FORCED |
| U2-Continuum | Theorem #12 | FORCED (with conformal gauge) |
| U5 | Theorem #13 | FORCED |
| U1 | Theorem #14 | FORCED |
| **U4 (this arc)** | **Theorem #15** | **FORCED (form; values inherited)** |

The structural-foundations cycle now contains **15 forced theorems** (was 14 before U4; was 9 at start of session).

### 7.2 Updated active CANDIDATE inventory

| Pre-U4 | Post-U4 |
|---|---|
| {U3, U4} + continuum gauge | **{U3} + continuum gauge** |

**One upstream CANDIDATE remains.** U3 (the participation-measure evolution equation $i\hbar \partial_t P_K = \hat{H}_K P_K + \sum V_{KK'} P_{K'}$) supplies the existence of a Hermitian Hamiltonian generator and the linear-first-order-in-time form of the evolution. Promoting U3 would close the entire QM-emergence Phase-1 structural-foundations program (except for the description-level continuum gauge convention).

### 7.3 Schrödinger-emergence chain

With U4 closed, the Schrödinger-emergence chain (Phase-1 Step 2) now reads:

```
Primitives 03, 04, 06, 07, 09, 13
                          |
                          v
                    U1 (FORCED) → P_K = √b · e^{iπ}
                          |
                          v
                    U2 (FORCED) → ⟨P|Q⟩ inner product
                          |
                          v
                    U4 (FORCED, this arc) → H = ℏ²|p|²/(2m) + V(x)
                          |
                          v
                    U3 (CANDIDATE, sole remaining) → iℏ ∂_t P = H P
                          |
                          v
                  Schrödinger emergence (Step 2)
```

Schrödinger emergence is **FORCED conditional on U3 alone**. All other structural inputs are now in place (U1 + U2 + U4 + the kinematic primitives + the inherited values).

### 7.4 Preparation for the U3 arc

The natural next foundational arc is **U3** — the participation-measure evolution equation. With U4 closed, U3 is the sole remaining active CANDIDATE in the QM-emergence Phase-1 program.

U3's structural content: there exists a self-adjoint Hamiltonian $\hat{H}$ on the U2 Hilbert space such that the participation measure evolves as $i\hbar \partial_t P = \hat{H} P + \sum V_{KK'} P_{K'}$ — i.e., linear, first-order in time, with Hermitian generator. U3 supplies *existence + structure*; U4 (now FORCED) supplied *specific form*.

The U3 arc would address:
- *Existence of a self-adjoint $\hat{H}$ generating time evolution.* Likely via Stone's theorem on time-translation symmetry (Primitive 13) on the U2 Hilbert space, paralleling F1's argument for spatial translations.
- *Linearity of the evolution equation.* Likely via the participation-measure framework's structural commitments (no nonlinear self-coupling at the kinematic level).
- *First-order-in-time character.* Possibly forced by the structure of the participation graph's time-axis content (Primitive 13).

The U3 arc inherits all five FORCED upstream items (U1, U2, U5, U4, Theorem 10). The methodological calibration from the five-arc cycle should transfer cleanly. Anticipated to be a clean closure, parallel in structure to U4 but operating on the time-translation symmetry rather than spatial translation.

Promoting U3 would close the entire QM-emergence Phase-1 program except for the description-level continuum gauge — the structural-foundations cycle would be complete across all four foundational postulates of non-relativistic single-particle quantum mechanics.

### 7.5 No new gauge structure introduced

U4 introduces no new gauge structure beyond what U2-Continuum already established. The Hamiltonian $\hat{H} = T(\hat{p}) + V(\hat{x})$ is gauge-compatible with the U2-Continuum conformal gauge by inheritance: under $(b_K, d\mu) \to (\Omega^{-D} b_K, \Omega^D d\mu)$, the participation measure rescales as $P_K \to \Omega^{-D/2} P_K$ but the operator structure of $\hat{H}$ on the abstract Hilbert space is unchanged. Inner-product values remain gauge-invariant per the U2-Continuum theorem.

The gauge-coupling-free scope of F5 (§3.5 of Memo 02) is a separate scope condition from the U2-Continuum gauge; it concerns electromagnetic gauge couplings ($A(\hat{x})$ vector potentials), not the U2-Continuum description-level conformal redundancy.

### 7.6 Methodological observation

U4 is the fifth and most delicate of the structural-foundations cycle (born_gleason, U2-Discrete, U2-Continuum, U5, U1, U4). The methodological pattern — **decompose CANDIDATE → identify automatic / forced-via-derivation / load-bearing sub-features → close load-bearing items via primitive-level + symmetry + scope arguments → introduce zero new CANDIDATEs → produce theorem-grade results** — has now been validated against:
- Non-contextuality + Gleason–Busch admissibility (born_gleason).
- Linearity + sesquilinearity + specific aggregation (U2).
- Discrete-to-continuum lift with explicit gauge (U2-Continuum).
- Adjacency-band partition with negative-existence audit (U5).
- Algebraic-structure question + magnitude-exponent question (U1).
- **Specific Hamiltonian form via Galilean-Lie-algebra integration (this arc)**.

Six substantively different structural questions, all closed via the same methodology. The pattern is now demonstrated across the full diversity of the QM-emergence Phase-1 structural questions.

---

## 8. Recommended Next Steps

**(a) Begin the U4 closure-and-summary memo (Memo 04).** The U4 arc is now ready for its canonical closure memo, parallel to U5 Memo 04 and U1 Memo 04. Memo 04 should provide the canonical narrative summary, the integration into the QM-emergence program (with the updated active-CANDIDATE inventory {U3} + gauge), the integrated F1–F5 derivation overview, and a public-facing explainer section. Anticipated to be a moderate-length memo with no new substantive arguments.

**(b) Open the U3 arc as the natural next foundational target.** With U4 closed, U3 is the sole remaining active CANDIDATE in the QM-emergence Phase-1 program. U3's anticipated structure: 4-memo arc (00 outline + 01 decomposition + 02 derivations + 03 verdict), inheriting all five prior FORCED items, with the substantive content concentrated on (i) existence of a self-adjoint $\hat{H}$ via Stone's theorem on time-translation symmetry (Primitive 13), (ii) linearity of the evolution equation, (iii) first-order-in-time character. Promoting U3 would close the entire Phase-1 structural-foundations program except for the description-level continuum gauge.

**(c) Write the U4 publication paper as the fifth in the structural-foundations publication series.** With U4 closed, the structural-foundations cycle now has six theorem-grade results (Theorem 10 + Theorems #11–15) but only three publication papers (Born_Gleason, U2_Inner_Product, U1_Participation_Measure). U5 and U4 papers are publishable but not yet drafted. A coordinated drafting of both — or sequential drafting starting with U4 (the most recent, methodologically richest arc) — would complete the structural-foundations publication series. Convention work, not derivation work; can be scheduled per project priorities.

---

## 9. Cross-references

**Within the U4 arc:**
- [`00_arc_outline.md`](00_arc_outline.md) — arc scoping
- [`01_decomposition_and_mapping.md`](01_decomposition_and_mapping.md) — sub-feature classification + circularity audit + transfer audit
- [`02_F1_F2_F5_derivations.md`](02_F1_F2_F5_derivations.md) — three forced-via-derivation sub-features

**Predecessor arcs (FORCED inputs):**
- [`arcs/born_gleason/`](../born_gleason/) — Theorem 10 (Born)
- [`arcs/U2/`](../U2/) — U2-Discrete
- [`arcs/U2_continuum/`](../U2_continuum/) — U2-Continuum
- [`arcs/U5/`](../U5/) — U5; particularly Memo 03 §1's Stone's-theorem template
- [`arcs/U1/`](../U1/) — U1

**Sibling CANDIDATE (forbidden as derivation input under Framing 1):**
- U3 (participation-measure evolution equation) — sole remaining active CANDIDATE; natural next foundational arc.

**Predecessor tightening-program memo (audit target; superseded by present arc):**
- [`arcs/arc-foundations/u4_hamiltonian_form_derivation.md`](../arc-foundations/u4_hamiltonian_form_derivation.md) (2026-04-24) — §§2.1–2.4 + §3 + §4 transfer cleanly per Memo 01 §3; §2.5's silent factor-of-2 adoption is the precise gap closed in §3 of this memo via the G1 Galilean argument.

**Source primitives:**
- Primitive 03 (Participation, supplies homogeneity for translation symmetry): `quantum/primitives/03_participation.md`
- Primitive 04 (Bandwidth, supplies $|P|^2 = b$ via U1): `quantum/primitives/04_participation_bandwidth.md`
- Primitive 06 (ED Gradient, supplies spatial axis): `quantum/primitives/06_ed_gradient.md`
- Primitive 09 (Tension Polarity): `quantum/primitives/09_tension_polarity.md`
- Primitive 13 (Relational Timing, supplies time-axis for Galilean argument): `quantum/primitives/13_relational_timing.md`

**Arc M (mass-parameter inheritance):**
- `papers/Arc_M/paper_arc_m.md` — "form FORCED, values INHERITED" framing.

**Mathematical reference:**
- Stone's theorem: M. H. Stone, "On one-parameter unitary groups in Hilbert space," *Annals of Mathematics* **33**, 643–648 (1932). Used in F1 (Memo 02) and §3.4 (Galilean unitarity).
- Galilean Lie algebra and central extension: standard mathematical-physics reference; e.g., V. Bargmann, "On unitary ray representations of continuous groups," *Annals of Mathematics* **59**, 1–46 (1954).

---

## 10. One-line memo summary

> **F3 (quadratic-in-$|\hat{p}|^2$ kinetic structure) is established by the four-constraint argument: C1 translation invariance (Memo 02) gives $T = T(\hat{p})$; C2 rotation invariance gives $T = f(|\hat{p}|^2)$ (dispatching Fal-5 anisotropic); C3 analyticity at low momentum gives Taylor expansion with no $|\hat{p}|$ branch-point terms (dispatching Fal-2 linear-in-$k$); C4 non-relativistic-limit suppresses higher-even-power terms (dispatching Fal-3 and Fal-7), leaving $T(\hat{p}) = a_1 |\hat{p}|^2$ uniquely. F4 (specific coefficient $1/(2m)$) is established under G1 Galilean-from-primitives via six-step argument: (1) primitive-level boost definition $x \to x + vt$ supported by Primitives 03 + 13 + non-rel scope; (2) Galilean Lie algebra commutators $[\hat{K}_i, \hat{P}_j] = i\hbar m \delta_{ij}$ and $[\hat{H}, \hat{K}_i] = -i\hbar \hat{p}_i$ as the structural anchor; (3) Galilean uniqueness within non-rel scope (Lorentzian boosts ruled out by absolute-time scope condition); (4) U2 inner-product unitarity of all Galilean transformations; (5) momentum transformation $\hat{p} \to \hat{p} - mv$ from boost commutator (5); (6) integration of $T'(|\hat{p}|^2) = 1/(2m)$ from the Galilean commutator condition $[\hat{H}, \hat{K}_i] = -i\hbar \hat{p}_i$ — **the factor of 2 is the integration Jacobian, not a convention** (dispatching Fal-4). All seven falsifiers dispatched. **U4 verdict: FORCED with form-FORCED-value-INHERITED framing**, conditional on (i) U3 sibling CANDIDATE under Framing 1, (ii) non-relativistic-single-particle scope (inherited from Phase-1 Step 2), (iii) gauge-coupling-free scope (F5), (iv) inherited mass values per Arc M and $\hbar$ via dimensional-atlas Madelung. Active CANDIDATE inventory reduces from {U3, U4} + gauge to **{U3} + gauge**. The QM-emergence Phase-1 program is now within one arc of complete structural foundations across all four foundational postulates.**
