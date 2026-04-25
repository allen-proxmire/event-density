# Relativistic Participation-Measure Scoping

**Date:** 2026-04-24
**Location:** `quantum/foundations/relativistic_participation_measure.md`
**Status:** Phase-2 Arc-R opening scoping memo. Defines the Lorentz-covariant extension of the Phase-1 participation measure, identifies the primitives requiring covariant reformulation, and lays out the structural constraints for Klein-Gordon (scalar) and Dirac (spinor) emergence. Does not derive either wave equation in full; scoping provides the infrastructure on which dedicated Klein-Gordon and Dirac derivations will build.
**Purpose:** First Phase-2 Arc-R deliverable per `phase2_extensions_roadmap.md §2.1`. Open the relativistic-extension arc.

---

## 1. Overview and scope

### 1.1 Phase-1 non-relativistic framework

The Phase-1 QM-emergence program derived non-relativistic single-particle quantum mechanics from the participation-measure framework. The participation measure was defined on a product of channel index and spatial-coordinate position:
\begin{equation}
  P_K(x, t) = \sqrt{b_K(x, t)} \, e^{i \pi_K(x, t)}, \qquad P_K \in \mathbb{C},
\end{equation}
with space and time treated as separate variables. The coherent sum $\Psi = \sum_K P_K$ was identified with the non-relativistic wavefunction, satisfying the Schrödinger equation $i\hbar \partial_t \Psi = \hat H \Psi$ with $\hat H = \hat P^2/(2m) + V$.

### 1.2 The relativistic extension — what changes

Under Lorentz invariance, space and time must be treated on equal footing as components of a single four-vector $x^\mu = (ct, \mathbf{x})$. The participation measure, its four-band decomposition, and the evolution equation all require covariant reformulation. The non-relativistic quadratic dispersion $E = p^2/(2m)$ is replaced by the relativistic mass-shell dispersion $E^2 = p^2 c^2 + m^2 c^4$. Klein-Gordon and Dirac equations replace Schrödinger in the appropriate scalar and spinor regimes.

### 1.3 What this memo does

This memo is scoping-level: it defines the Lorentz-covariant participation measure, catalogs the primitive-level reformulations required, and identifies the structural constraints needed to derive Klein-Gordon and Dirac as thin-participation limits. Full derivations of the two equations are the successor deliverables per `phase2_extensions_roadmap.md §2.1`.

The memo distinguishes what is FORCED at the scoping level (constraints that follow from Lorentz invariance alone) from what remains open (specific evolution form, rule-type classification for fermions, Clifford-algebra derivation, interaction-term structure).

---

## 2. Lorentz-covariant participation measure

### 2.1 Definition

The **Lorentz-covariant participation measure** is a complex-valued distribution over channels and spacetime events:
\begin{equation}
  P_K(x^\mu) \in \mathbb{C}, \qquad x^\mu = (ct, \mathbf{x}),
  \label{eq:covP}
\end{equation}
defined on four-dimensional Minkowski spacetime with signature $(+, -, -, -)$ (the "mostly-minus" convention).

### 2.2 Transformation under Lorentz boosts

Under a Lorentz transformation $\Lambda$, the spacetime coordinates transform as $x^\mu \to x'^\mu = \Lambda^\mu{}_\nu x^\nu$. The participation measure has two transformation types according to the rule-type of the chain:

- **Scalar chains** (bosonic rule-type; Klein-Gordon candidates): $P_K$ transforms as a scalar at each spacetime point,
\begin{equation}
  P_K(x^\mu) \to P'_K(x'^\mu) = P_K(\Lambda^{-1} x'^\mu).
  \label{eq:scalar_transf}
\end{equation}
- **Spinor chains** (fermionic rule-type; Dirac candidates): $P_K$ carries a spinor index $\alpha$ (four-component for spin-1/2),
\begin{equation}
  P_{K,\alpha}(x^\mu) \to P'_{K,\beta}(x'^\mu) = S(\Lambda)_\beta{}^\alpha P_{K,\alpha}(\Lambda^{-1} x'^\mu),
  \label{eq:spinor_transf}
\end{equation}
with $S(\Lambda)$ the spinor representation of the Lorentz group.

**The distinction between scalar and spinor participation measures corresponds to the bosonic vs fermionic rule-type classification (Primitive 07 §7.4), which remains open.** Without the rule-type taxonomy derivation, the scalar-vs-spinor split is stipulated rather than derived.

### 2.3 Derived quantities in the covariant framework

- **Event density** $\rho(x^\mu) = \sum_K |P_K(x^\mu)|^2$ is a Lorentz scalar.
- **Coherent sum** $\Psi(x^\mu) = \sum_K P_K(x^\mu)$ is a scalar (for bosonic chains) or a spinor (for fermionic chains).
- **Four-current** $j^\mu(x^\nu)$ arises from the bilinear $P^*_K \partial^\mu P_K$ and its Hermitian-conjugate sum; it is a Lorentz four-vector.

The scalar and spinor cases will require separate treatments for each quantity.

### 2.4 Amplitude-phase decomposition

The polar-decomposition form $P_K = \sqrt{b_K} e^{i\pi_K}$ from Phase 1 extends covariantly:
\begin{equation}
  P_K(x^\mu) = \sqrt{b_K(x^\mu)} \, e^{i \pi_K(x^\mu)},
\end{equation}
with $b_K(x^\mu) \geq 0$ a Lorentz scalar and $\pi_K(x^\mu) \in [0, 2\pi)$ a Lorentz-invariant phase. For spinor chains, the decomposition applies component-wise with a spinor-valued amplitude factor.

**Status: CANDIDATE** for scalar chains (direct extension of Phase 1); more structure required for spinor chains (rule-type taxonomy must specify the spinor-index content).

---

## 3. Primitive reformulations

Four primitives require covariant reformulation for the relativistic extension. This section catalogs each.

### 3.1 Primitive 02 — Chain → worldline

**Phase-1 content.** A chain is a sequence of micro-events held together by a consistent update rule; the rule persists across the sequence and constitutes the chain's identity. Time progression is via a single parameter $t$.

**Covariant reformulation.** A chain becomes a **worldline** — a one-dimensional curve in spacetime, parameterized by proper time $\tau$:
\begin{equation}
  x^\mu(\tau) \text{ with } d\tau^2 = \frac{1}{c^2} g_{\mu\nu} dx^\mu dx^\nu.
\end{equation}
For a massive chain, $d\tau > 0$; the chain advances along a timelike worldline. The chain identity (rule persistence) is preserved under Lorentz boosts because proper time is invariant.

**Primitive-level consequence.** The Phase-1 concept of "the chain's current time" is replaced by "the chain's current proper time." The commitment-event rate (Primitive 11) is parameterized by $d\tau$, not by $dt$. Different inertial frames observe the chain's commitment rate as $d\tau / dt = \sqrt{1 - v^2/c^2}$ — the standard relativistic time dilation.

**Status: FORCED** by Lorentz invariance requirements. The covariant Primitive 02 is a strict generalization of the non-relativistic version; the latter is recovered in the limit $v/c \to 0$.

### 3.2 Primitive 04 — Four-band → covariant bands

**Phase-1 content.** Bandwidth is partitioned into four bands:
\begin{equation}
  b_K = b_K^{\mathrm{int}} + b_K^{\mathrm{adj}} + b_K^{\mathrm{env}} + b_K^{\mathrm{com}},
\end{equation}
with adjacency, environmental, internal, and commitment-reserve contributions. In Phase 1, these were defined at each $(x, t)$.

**Covariant reformulation.** Each of the four bands becomes a Lorentz scalar field on spacetime:
\begin{equation}
  b_K^{\mathrm{int}}(x^\mu), \quad b_K^{\mathrm{adj}}(x^\mu), \quad b_K^{\mathrm{env}}(x^\mu), \quad b_K^{\mathrm{com}}(x^\mu) \geq 0.
\end{equation}
The decomposition and the sum-rule $b_K = \sum_i b_K^{(i)}$ are Lorentz-invariant: the four bands carry Lorentz-scalar content at each spacetime event.

**Interpretation of the bands in the covariant framework:**
- **Internal rule-bandwidth** $b_K^{\mathrm{int}}$: participation sustaining the worldline's rule at proper time $\tau$. Invariant along the worldline.
- **Adjacency bandwidth** $b_K^{\mathrm{adj}}$: participation with spacetime neighbors on the light-cone or within the causal vicinity. In the covariant framework, "adjacency" is defined by the participation-graph's spacetime-neighborhood structure, which respects the light-cone.
- **Environmental bandwidth** $b_K^{\mathrm{env}}$: participation with broader spacetime-extended environmental structure.
- **Commitment-reserve bandwidth** $b_K^{\mathrm{com}}$: participation available for commitment events along the worldline.

**Status: FORCED** as a structural extension. The four-band decomposition is preserved; only the coordinate-time parameterization is replaced by spacetime-point parameterization.

**Light-cone structure of adjacency.** An important refinement: the Phase-1 spatial adjacency becomes, in the covariant framework, **lightlike adjacency** for massless information propagation and **spacelike adjacency** for instantaneous neighborhood. Primitive 03 (participation) requires that adjacency respects causal ordering — spacelike-separated events can participate only through their common causal past. This is the primitive-level content of the no-signaling property in the relativistic framework.

### 3.3 Primitive 06 — ED gradient → four-gradient

**Phase-1 content.** The ED gradient is the vector field $\nabla \rho(x, t)$ specifying the direction and magnitude of event-density variation. In Phase 1, the gradient and the time-derivative $\partial_t \rho$ are separate objects.

**Covariant reformulation.** The gradient becomes the **four-gradient**:
\begin{equation}
  \partial_\mu \rho(x^\nu), \qquad \mu = 0, 1, 2, 3,
\end{equation}
where $\partial_0 = (1/c) \partial_t$ and $\partial_i = \partial_{x_i}$. Under Lorentz transformation, $\partial_\mu$ transforms as a covariant four-vector.

The Phase-1 spatial and temporal derivatives are unified: no distinction between "time-component" and "spatial-components" is primitively significant; only the four-vector structure is.

**Status: FORCED** by Lorentz invariance. The covariant four-gradient is the unique Lorentz-covariant derivative operator on scalar fields.

**Four-divergence and d'Alembertian.** Two covariant differential operators are primitive-level accessible:
- **Four-divergence** of a four-vector: $\partial_\mu V^\mu$. Applied to the four-current, this gives the continuity equation $\partial_\mu j^\mu = 0$.
- **d'Alembertian** (wave operator): $\Box = \partial_\mu \partial^\mu = (1/c^2) \partial_t^2 - \nabla^2$. This appears in the Klein-Gordon equation.

Both operators are Lorentz scalars constructed from the four-gradient.

### 3.4 Primitive 13 — Relational timing → Lorentz-invariant

**Phase-1 content.** Relational timing is the phase-coupling structure between participation channels. Time is a relational rhythm, not an absolute variable; coordinate time $t$ is used as a convenient parameter.

**Covariant reformulation.** The relational timing content is preserved, but the timing-parameter is Lorentz-invariant. Each chain's intrinsic timing is its **proper time** $\tau$, which is the same in every inertial frame. Relational timing between two chains is specified by the difference in their proper-time parameterizations along their worldlines, which is Lorentz-invariant.

For coherent channel structure (multiple channels within a single chain), the relational timing is the phase advancement $\partial_\tau \pi_K$ per proper-time interval — Lorentz-invariant.

For the emergent coordinate time in the thick regime (see Primitive 13 §1), the covariant framework recognizes that coordinate time is frame-dependent; the underlying relational-timing content is frame-independent.

**Status: FORCED** by Lorentz invariance. Proper time is the natural Lorentz-invariant parameter.

### 3.5 Summary of primitive reformulations

| Primitive | Phase-1 content | Covariant reformulation | Status |
|---|---|---|---|
| 02 (Chain) | Rule-bearing sequence in time | Worldline parameterized by proper time | FORCED |
| 04 (Bandwidth four-band) | Four bands at each $(x, t)$ | Four Lorentz scalar fields at each $x^\mu$ | FORCED |
| 06 (ED gradient) | $\nabla \rho$, $\partial_t \rho$ separate | Four-gradient $\partial_\mu \rho$ | FORCED |
| 13 (Relational timing) | Phase coupling over time $t$ | Proper-time phase coupling | FORCED |

**None of these requires a new primitive.** The Phase-1 versions are non-relativistic limits of the covariant versions; the covariant versions are the primitive-level statements that reduce to Phase-1 forms in the $v/c \to 0$ limit.

---

## 4. Coherent sum in the covariant framework

### 4.1 Scalar case

For scalar participation (bosonic rule-type), the coherent sum is:
\begin{equation}
  \Psi(x^\mu) = \sum_K P_K(x^\mu), \qquad \Psi \in \mathbb{C},
\end{equation}
a complex scalar field on spacetime. Under Lorentz transformation, $\Psi(x^\mu) \to \Psi(\Lambda^{-1} x'^\mu)$ — scalar transformation.

### 4.2 Spinor case

For spinor participation (fermionic rule-type, four-component spin-1/2 for electrons, etc.), the coherent sum is:
\begin{equation}
  \psi_\alpha(x^\mu) = \sum_K P_{K,\alpha}(x^\mu), \qquad \psi \in \mathbb{C}^4,
\end{equation}
a four-component spinor field. Under Lorentz transformation, $\psi_\alpha(x^\mu) \to S(\Lambda)_\alpha{}^\beta \psi_\beta(\Lambda^{-1} x'^\mu)$.

**The spinor index content is primitive-level open.** Primitive 07 §7.4 (rule-type taxonomy) must be derived before the spinor case is primitive-derivable. A spinor participation measure is provisionally defined as CANDIDATE structure for the purposes of this scoping memo, with the understanding that the rule-type taxonomy is the load-bearing prerequisite.

### 4.3 Both cases together

In a general framework where both bosonic and fermionic chains are present, the total participation-measure content is:
\begin{equation}
  \Psi_{\text{scalar}}(x^\mu) \in \mathbb{C}, \quad \psi_{\text{spinor},\alpha}(x^\mu) \in \mathbb{C}^4,
\end{equation}
indexed by rule-type and by spacetime event. The full derivation would classify all rule-types and produce the correct tensor / spinor content for each.

---

## 5. Structural constraints for Klein-Gordon

Klein-Gordon is the relativistic scalar wave equation:
\begin{equation}
  \left(\Box + \frac{m^2 c^2}{\hbar^2}\right) \Psi(x^\mu) = 0.
  \label{eq:KG}
\end{equation}

### 5.1 Dispersion relation

The mass-shell condition $p_\mu p^\mu = m^2 c^2$, equivalently $E^2 = p^2 c^2 + m^2 c^4$, gives the relativistic dispersion relation for a scalar chain. For a plane-wave participation mode $P_k(x^\mu) = e^{-i p_\mu x^\mu / \hbar} \cdot c_k$,
\begin{equation}
  \left(\frac{\omega}{c}\right)^2 = k^2 + \left(\frac{m c}{\hbar}\right)^2,
\end{equation}
or equivalently $\omega^2 = c^2 k^2 + (mc^2/\hbar)^2$. This is the dispersion that replaces the non-relativistic $\omega = \hbar k^2/(2m)$.

### 5.2 Second-order structure

Klein-Gordon is second-order in time. This contrasts with U3's first-order Schrödinger equation. **The second-order-in-time structure is forced by the Lorentz-invariant combination $\Box = \partial_\mu \partial^\mu$:** a Lorentz-scalar wave equation for a scalar field cannot be first-order in time (which would break Lorentz invariance by privileging the time component).

**First-order alternative.** Klein-Gordon can be factored into two first-order equations by introducing auxiliary fields (Feshbach-Villars form). Under appropriate factoring, each first-order equation resembles Schrödinger structure but with relativistic dispersion. Whether the primitive-level derivation of Klein-Gordon prefers the second-order form or the factored first-order form is an open question; different routes give mathematically equivalent content but different primitive-level interpretations.

### 5.3 What must be derived

For a full Klein-Gordon derivation in the ED framework:

1. **Scalar participation measure $P_K(x^\mu) \in \mathbb{C}$** with the transformation rule (scalar_transf). FORCED by the scoping in §2.
2. **Covariant evolution equation** that reduces to $U3$ in the non-relativistic limit and to Klein-Gordon in the relativistic regime. The structural form is conjectured to be a covariant version of (U3), but the explicit form requires dedicated derivation.
3. **Mass-shell dispersion** derived from the covariant four-gradient structure (Primitive 06 covariant) + translation invariance. Specifically, a plane-wave $P_k(x^\mu) = e^{-i p_\mu x^\mu/\hbar}$ should satisfy the mass-shell condition.
4. **Non-relativistic limit** explicitly: show Klein-Gordon reduces to Schrödinger at $v/c \ll 1$.
5. **Charge conservation** (for charged scalar chains): the four-current $j^\mu = i(P^* \partial^\mu P - P \partial^\mu P^*)$ should be conserved, $\partial_\mu j^\mu = 0$.

**Status of Klein-Gordon derivation: ACCESSIBLE with dedicated session work.** All primitive-level ingredients are FORCED by the scoping. The remaining work is the explicit derivation, comparable in scope to the Phase-1 Schrödinger emergence (Step 2).

**Expected memo:** `quantum/foundations/klein_gordon_emergence.md`, multi-session derivation.

---

## 6. Structural constraints for Dirac

Dirac is the relativistic first-order spinor wave equation:
\begin{equation}
  \left(i \hbar \gamma^\mu \partial_\mu - m c\right) \psi(x^\mu) = 0,
  \label{eq:Dirac}
\end{equation}
where $\gamma^\mu$ are the Dirac gamma matrices satisfying the Clifford algebra $\{\gamma^\mu, \gamma^\nu\} = 2 g^{\mu\nu}$, and $\psi$ is a four-component spinor field.

### 6.1 The structural challenge

Dirac is substantially more demanding than Klein-Gordon because it requires:
- **Spinor structure of the participation measure.** Each channel $K$ carries a spinor index $\alpha$; $P_{K,\alpha}(x^\mu) \in \mathbb{C}^4$.
- **Clifford algebra $\gamma^\mu$.** A primitive-level origin for the anticommutation relations of the gamma matrices.
- **Fermionic rule-type classification.** Rule-type taxonomy (Primitive 07 §7.4) distinguishing fermions from bosons.
- **Spin-statistics connection.** Fermions have half-integer spin and obey the Pauli exclusion principle; bosons have integer spin and Bose-Einstein statistics. This connection must emerge from the primitive-level rule-type content.

### 6.2 What must be derived

For a full Dirac derivation in the ED framework:

1. **Spinor participation measure $P_{K,\alpha}(x^\mu)$.** Contingent on rule-type taxonomy specifying the spinor-index content for fermionic chains.
2. **Clifford algebra $\{\gamma^\mu, \gamma^\nu\} = 2 g^{\mu\nu}$ from primitive-level structure.** The gamma matrices must be derivable from the participation-graph's local Clifford-algebra content. Candidate approach: gamma matrices as representations of the spacetime-symmetry group acting on spinor-valued participation measures.
3. **First-order covariant evolution.** Unlike Klein-Gordon, Dirac is first-order in spacetime derivatives. This is compatible with the U3-like first-order structure but requires the spinor-index machinery.
4. **Non-relativistic limit** to the Pauli equation (Schrödinger equation with spin-1/2 correction).
5. **Spin-statistics theorem** as a primitive-level consequence: fermions anticommute; bosons commute.

**Status of Dirac derivation: CONTINGENT on rule-type taxonomy.** The scoping here is deferred until Primitive 07 §7.4 is addressed. Candidate approach: derive the rule-type taxonomy in an initial scoping memo (`rule_type_taxonomy.md`), then produce Dirac as a consequence.

**Expected memo (after rule-type taxonomy):** `quantum/foundations/dirac_emergence.md`.

### 6.3 Relationship to Arc M (chain-mass)

The rule-type taxonomy that unlocks Dirac also unlocks Arc M (chain-mass derivation). The two arcs share this prerequisite, and progress on the taxonomy advances both. The roadmap identifies this as a shared sub-program (`phase2_extensions_roadmap.md §3.3`).

---

## 7. FORCED versus open

### 7.1 What is FORCED at the scoping level

| Item | Status | Source |
|---|---|---|
| Lorentz-covariant participation measure on $x^\mu$ | FORCED | Lorentz invariance + Phase-1 P_K structure |
| Covariant Primitive 02 (chain → worldline) | FORCED | Proper-time invariance |
| Covariant Primitive 04 (four-band as Lorentz scalars) | FORCED | Scalar-bandwidth Lorentz invariance |
| Covariant Primitive 06 (ED four-gradient) | FORCED | Unique Lorentz-covariant derivative on scalars |
| Covariant Primitive 13 (proper-time relational timing) | FORCED | Proper-time Lorentz invariance |
| Scalar coherent sum $\Psi(x^\mu) \in \mathbb{C}$ | FORCED for bosonic chains |
| Relativistic dispersion $p_\mu p^\mu = m^2 c^2$ | FORCED | Poincaré invariance + analyticity |
| Light-cone structure of adjacency | FORCED | Causal-ordering consistency |
| No-signaling from light-cone + commitment locality | FORCED | Extension of Primitive 11 to covariant framework |

### 7.2 What remains open

| Item | Reason |
|---|---|
| Explicit covariant evolution equation | Requires dedicated derivation memo |
| Spinor participation measure content | Requires rule-type taxonomy (Primitive 07 §7.4) |
| Clifford algebra from primitives | Requires spinor-structure derivation |
| Klein-Gordon second-order vs factored first-order | Choice of derivation route |
| Non-relativistic limit to Schrödinger | Requires dedicated derivation |
| Interaction terms (gauge coupling, Coulomb, etc.) | Requires extension beyond free-particle case |
| Relationship to QFT extension (Arc Q) | Multi-particle relativistic case |

### 7.3 Inherited content

- Speed of light $c$ (Lorentz invariance scale).
- Particle mass $m$ (inherited at the species level; chain-mass derivation is Arc M).
- $\hbar$ (inherited via Phase-1 inheritance; see `hbar_origin.md`).

---

## 8. Roadmap to full derivations

The relativistic arc (Arc R) unfolds in three stages:

### 8.1 Stage R.1 — Klein-Gordon emergence (near-term)

- Opening memo (this document): scoping complete.
- Derivation memo `klein_gordon_emergence.md`: multi-session.
- Non-relativistic limit check: reduces to Schrödinger.
- Charge conservation and four-current.

Estimated scope: 3–4 memos.

### 8.2 Stage R.2 — Rule-type taxonomy sub-program (shared with Arc M)

- Scoping memo `rule_type_taxonomy.md`: open the taxonomy problem.
- Derivation memos on specific rule-types (bosonic, fermionic at minimum; possibly distinguishing spin values).
- Connection to Arc M (chain-mass) via rule-type bandwidth signatures.

Estimated scope: 3–5 memos, shared between Arc R (for Dirac) and Arc M.

### 8.3 Stage R.3 — Dirac emergence (contingent on R.2)

- Spinor participation measure: formalize the $P_{K,\alpha}(x^\mu)$ content.
- Clifford algebra derivation from participation-graph structure.
- Dirac equation derivation.
- Non-relativistic limit to Pauli.
- Spin-statistics connection.

Estimated scope: 3–5 memos after R.2 completes.

### 8.4 Downstream: interaction terms and QFT (Arc Q)

Interaction terms (gauge coupling, Coulomb, etc.) require extending the relativistic framework beyond the free-particle case. Multi-particle content (second quantization, field operators) lies in Arc Q, which builds on Arc R.

---

## 9. Honest framing

### 9.1 What this memo achieves

- Defines the Lorentz-covariant participation measure $P_K(x^\mu)$.
- Identifies the four primitive reformulations (02, 04, 06, 13) required for Lorentz invariance, all FORCED at the scoping level.
- Generalizes the coherent sum to scalar and spinor cases.
- Lays out the structural constraints for Klein-Gordon (accessible) and Dirac (contingent on rule-type taxonomy).
- Produces a clean FORCED vs open catalog.

### 9.2 What this memo does not achieve

- No derivation of the covariant evolution equation explicitly.
- No derivation of Klein-Gordon as a wave equation.
- No spinor-structure derivation.
- No Dirac equation.
- No interaction terms or QFT content.

All of these are deferred to dedicated derivation memos within Arc R.

### 9.3 Scope honesty

The Phase-2 Arc-R program is a multi-session research arc. Klein-Gordon is accessible in the near term; Dirac requires the rule-type taxonomy sub-program; full relativistic QFT requires Arc Q. The scoping memo opens the arc; successive memos close its sub-goals.

**No new primitives are required by the relativistic extension.** The four primitive reformulations (Primitives 02, 04, 06, 13) are strict generalizations of their Phase-1 versions; Phase-1 contents are recovered in the non-relativistic limit $v/c \to 0$.

---

## 10. Summary

**The Lorentz-covariant participation measure $P_K(x^\mu)$ is defined on spacetime events and transforms covariantly under Lorentz boosts.** Four primitives (Primitive 02, 04, 06, 13) receive covariant reformulations, each forced by Lorentz invariance and none requiring a new primitive. The scalar coherent sum $\Psi(x^\mu) \in \mathbb{C}$ is the Lorentz-scalar wavefunction candidate for bosonic chains; the spinor coherent sum $\psi_\alpha(x^\mu) \in \mathbb{C}^4$ is the spinor wavefunction candidate for fermionic chains, contingent on the rule-type taxonomy derivation (Primitive 07 §7.4). Klein-Gordon emergence is accessible in the near term via a dedicated derivation memo; Dirac emergence is contingent on the rule-type taxonomy and requires the Clifford-algebra derivation as a sub-task. No new primitives; all scoping-level structural content is FORCED.

---

## 11. Cross-references

### Program-level
- Phase-2 extensions roadmap: [`quantum/foundations/phase2_extensions_roadmap.md`](phase2_extensions_roadmap.md) §2.1
- QM-emergence closure (Phase-1 baseline): [`quantum/foundations/qm_emergence_closure.md`](qm_emergence_closure.md)
- Step 2 (non-relativistic Schrödinger): [`quantum/foundations/schrodinger_emergence.md`](schrodinger_emergence.md)
- Lindblad extension (non-relativistic open-system): [`quantum/foundations/lindblad_extension.md`](lindblad_extension.md)
- ℏ-origin memo (inheritance structure preserved): [`quantum/foundations/hbar_origin.md`](hbar_origin.md)

### Primitive stack
- Primitive 02 (chain; to be reformulated as worldline): [`quantum/primitives/02_chain.md`](../primitives/02_chain.md)
- Primitive 04 (bandwidth; four-band; covariant scalars): [`quantum/primitives/04_participation_bandwidth.md`](../primitives/04_participation_bandwidth.md)
- Primitive 06 (ED gradient; four-gradient): [`quantum/primitives/06_ed_gradient.md`](../primitives/06_ed_gradient.md)
- Primitive 07 (channel; rule-type taxonomy open): [`quantum/primitives/07_channel.md`](../primitives/07_channel.md)
- Primitive 13 (relational timing; proper-time reformulation): [`quantum/primitives/13_relational_timing.md`](../primitives/13_relational_timing.md)

### External references
- Klein, O. (1926). *Z. Phys.* **37**, 895.
- Gordon, W. (1926). *Z. Phys.* **40**, 117.
- Dirac, P. A. M. (1928). *Proc. Roy. Soc. A* **117**, 610.
- Weinberg, S. (1995). *The Quantum Theory of Fields*, Vol. 1. Cambridge.
- Peskin, M. E., Schroeder, D. V. (1995). *An Introduction to Quantum Field Theory*. Westview.

---

## 12. One-line summary

> **The Lorentz-covariant participation measure $P_K(x^\mu)$ is defined on spacetime events and transforms as a scalar or spinor under Lorentz boosts according to the rule-type of the chain (bosonic vs fermionic). Four primitive-level reformulations are FORCED by Lorentz invariance: Primitive 02 chain → worldline with proper-time parameterization, Primitive 04 four-band → four covariant bandwidth scalars, Primitive 06 ED gradient → four-gradient $\partial_\mu$, Primitive 13 relational timing → proper-time phase content. No new primitives required; Phase-1 contents are recovered in the $v/c \to 0$ limit. Light-cone structure of adjacency + Primitive 11 locality give primitive-level no-signaling. Scalar coherent sum $\Psi(x^\mu) \in \mathbb{C}$ and relativistic dispersion $p_\mu p^\mu = m^2 c^2$ are FORCED; these provide the infrastructure for Klein-Gordon emergence (near-term accessible, dedicated derivation memo to follow). Spinor coherent sum $\psi_\alpha(x^\mu) \in \mathbb{C}^4$ and Dirac emergence are contingent on the rule-type taxonomy derivation (Primitive 07 §7.4, shared prerequisite with Arc M chain-mass). Clifford algebra, spin-statistics, and interaction terms remain open. Arc-R opening scoping deliverable complete; three staged sub-programs (Klein-Gordon, rule-type taxonomy, Dirac) map the remaining arc with estimated 9–14 additional memos.**
