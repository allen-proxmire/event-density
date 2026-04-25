# Arc-R Stage R.1 Synthesis — Scalar Relativistic Quantum Mechanics

**Date:** 2026-04-24
**Location:** `quantum/foundations/arc_r_stage1_synthesis.md`
**Status:** Closure memo for Arc-R Stage R.1 (scalar relativistic quantum mechanics). Consolidates the three Stage-R.1 derivation memos — Lorentz-covariant participation-measure scoping, free-particle Klein-Gordon emergence, and minimal coupling with conserved four-current — into a single archival document. Marks Stage R.1 as structurally complete for bosonic (scalar) chains in external electromagnetic fields. Identifies Stage R.2 (rule-type taxonomy) as the critical next sub-program.
**Purpose:** Close Arc-R Stage R.1 cleanly and hand off to Stage R.2. Archival-quality integration of the Stage-R.1 results.

---

## 1. Stage R.1 overview

### 1.1 What Stage R.1 set out to do

Stage R.1 of the relativistic arc (Phase-2 Arc R per `phase2_extensions_roadmap.md §2.1`) targeted the derivation of relativistic quantum mechanics for scalar (bosonic) chains in the ED framework. The specific content to be established:

- A Lorentz-covariant participation measure $P_K(x^\mu) \in \mathbb{C}$ on spacetime events.
- The Klein-Gordon wave equation $(\Box + m^2 c^2/\hbar^2) \Psi = 0$ as the thin-participation limit for free scalar chains.
- The interacting Klein-Gordon equation $(D_\mu D^\mu + m^2 c^2/\hbar^2) \Psi = 0$ under minimal electromagnetic coupling.
- The conserved four-current $j^\mu$ and its continuity equation.
- An explicit non-relativistic limit reducing to the Phase-1 Schrödinger equation.

### 1.2 What Stage R.1 did not include

Stage R.1 was restricted to the scalar case. The spinor (Dirac) case requires the rule-type taxonomy to specify fermionic participation-measure structure and is deferred to Stages R.2 (taxonomy) and R.3 (Dirac).

### 1.3 The three Stage-R.1 memos

Stage R.1 was executed across three derivation memos:

1. **`relativistic_participation_measure.md`** — scoping memo defining the Lorentz-covariant participation measure and the covariant reformulations of Primitives 02, 04, 06, 13.
2. **`klein_gordon_emergence.md`** — derivation of the free-particle Klein-Gordon equation from Lorentz invariance + plane-wave mode ansatz + mass-shell condition, plus the non-relativistic limit to free Schrödinger.
3. **`kg_minimal_coupling_and_current.md`** — extension to interacting Klein-Gordon via gauge-covariant derivative $D_\mu$, derivation of the conserved four-current $j^\mu$, and non-relativistic limit to Schrödinger with electromagnetic coupling.

---

## 2. The integrated Stage-R.1 framework

### 2.1 Starting point — covariant participation measure

The Lorentz-covariant participation measure for a scalar (bosonic) chain is
\begin{equation}
  P_K(x^\mu) = \sqrt{b_K(x^\mu)} \, e^{i \pi_K(x^\mu)} \in \mathbb{C},
  \tag{1}
\end{equation}
transforming as a scalar at each spacetime event under Lorentz boosts: $P_K(x^\mu) \to P_K(\Lambda^{-1} x'^\mu)$. The coherent sum
\begin{equation}
  \Psi(x^\mu) = \sum_K P_K(x^\mu)
  \tag{2}
\end{equation}
is the Lorentz-scalar wavefunction candidate.

The four primitives receive covariant reformulations (per `relativistic_participation_measure.md` §3):

| Primitive | Covariant form |
|---|---|
| 02 (Chain) | Worldline $x^\mu(\tau)$ parameterized by proper time |
| 04 (Four-band) | Four Lorentz-scalar bandwidth fields $b_K^{\mathrm{int/adj/env/com}}(x^\mu)$ |
| 06 (ED gradient) | Four-gradient $\partial_\mu$ |
| 13 (Relational timing) | Proper-time phase content |

All four reformulations are FORCED by Lorentz invariance; no new primitives are introduced.

### 2.2 Free-particle wave equation

The free-particle Klein-Gordon equation (derived in `klein_gordon_emergence.md`):
\begin{equation}
  \left(\Box + \frac{m^2 c^2}{\hbar^2}\right) \Psi(x^\mu) = 0,
  \tag{3}
\end{equation}
arises as the unique minimum-order linear Lorentz-scalar wave equation on a scalar field, with:

- **d'Alembertian** $\Box = \partial_\mu \partial^\mu$ as the unique Lorentz-scalar second-order differential operator.
- **Mass-shell condition** $p_\mu p^\mu = m^2 c^2$ forced by applying (3) to plane-wave modes $P_K(x^\mu) = c_K e^{-i p_\mu x^\mu / \hbar}$.
- **Relativistic dispersion** $E^2 = |\mathbf{p}|^2 c^2 + m^2 c^4$ as the component form of the mass-shell.

### 2.3 Minimal electromagnetic coupling

The interacting wave equation (from `kg_minimal_coupling_and_current.md`):
\begin{equation}
  \left(D_\mu D^\mu + \frac{m^2 c^2}{\hbar^2}\right) \Psi(x^\mu) = 0,
  \tag{4}
\end{equation}
where the gauge-covariant derivative is
\begin{equation}
  D_\mu = \partial_\mu + \frac{i q}{\hbar} A_\mu,
  \tag{5}
\end{equation}
with $q$ the chain's electromagnetic charge (inherited) and $A_\mu$ the external electromagnetic four-potential.

Equation (4) is FORCED as the unique first-order gauge-covariant extension of (3) under local U(1) gauge invariance. Under the gauge transformation
\begin{equation}
  \Psi \to e^{i q \alpha(x)/\hbar} \Psi, \qquad A_\mu \to A_\mu + \partial_\mu \alpha,
\end{equation}
the covariant derivative transforms as $D_\mu \Psi \to e^{i q \alpha/\hbar} D_\mu \Psi$, and the equation is gauge-invariant.

### 2.4 Conserved four-current

The four-current (from `kg_minimal_coupling_and_current.md` §5):
\begin{equation}
  j^\mu = \frac{i \hbar}{2 m}\left[\Psi^* D^\mu \Psi - \Psi (D^\mu \Psi)^*\right]
  \tag{6}
\end{equation}
has three properties, each FORCED:

- **Real:** $j^\mu$ is a real four-vector (direct from (6) structure).
- **Gauge-invariant:** the bilinear $\Psi^* D^\mu \Psi$ is gauge-invariant because net charge is zero.
- **Conserved:** $\partial_\mu j^\mu = 0$ follows algebraically from (4) and (6).

The components $j^\mu = (c \rho_{\mathrm{em}}, \mathbf{j}_{\mathrm{em}})$ give the charge-current density. The continuity equation expresses local charge conservation:
\begin{equation}
  \partial_t \rho_{\mathrm{em}} + \nabla \cdot \mathbf{j}_{\mathrm{em}} = 0.
\end{equation}

**Caveat on j⁰:** for Klein-Gordon at the single-particle level, the time component $j^0$ is not positive-definite. This is a known interpretive obstacle, motivating the QFT extension (Arc Q). Under the charge-current interpretation adopted here, non-positive-definiteness is acceptable (charge density can have either sign); under a probability-density interpretation it is not. The resolution requires second quantization, deferred to Arc Q.

### 2.5 Non-relativistic limit

Rest-energy factorization $\Psi = e^{-i m c^2 t / \hbar} \psi(\mathbf{x}, t)$, substituted into (4) and dropping the relativistic-correction term $(1/c^2) \partial_t^2 \psi$, yields
\begin{equation}
  i \hbar \partial_t \psi = \left[\frac{1}{2m}(-i \hbar \nabla - q \mathbf{A})^2 + q \varphi\right] \psi.
  \tag{7}
\end{equation}

This is the Phase-1 Schrödinger equation with electromagnetic coupling. The non-relativistic limit is mathematically exact and reproduces the Phase-1 Step-2 derivation result of `schrodinger_emergence.md` §4, augmented by the minimal-coupling $(-i \hbar \nabla - q \mathbf{A})^2$ kinetic term and the scalar potential $q \varphi$.

**Consistency with Phase 1:** the Phase-1 Schrödinger equation is a strict sub-theory of Stage-R.1 relativistic scalar quantum mechanics. Every Phase-1 result for a scalar particle in an external potential is recovered as the $v/c \to 0$ limit of the Stage-R.1 framework.

---

## 3. Stage R.1 consolidated status

### 3.1 What is FORCED

| Feature | Source |
|---|---|
| Lorentz-covariant $P_K(x^\mu)$ | Scoping memo §2 |
| Covariant Primitives 02, 04, 06, 13 | Scoping memo §3 |
| Scalar coherent sum $\Psi(x^\mu)$ | Scalar rule-type |
| D'Alembertian as Lorentz-scalar operator | `klein_gordon_emergence.md` §2 |
| Free Klein-Gordon (eq. 3) | `klein_gordon_emergence.md` §4 |
| Mass-shell condition $p_\mu p^\mu = m^2 c^2$ | `klein_gordon_emergence.md` §3 |
| Relativistic dispersion $E^2 = \|\mathbf{p}\|^2 c^2 + m^2 c^4$ | `klein_gordon_emergence.md` §3 |
| Non-relativistic limit to free Schrödinger | `klein_gordon_emergence.md` §5 |
| Local U(1) gauge invariance (structural commitment) | `kg_minimal_coupling_and_current.md` §2 |
| Minimal-coupling prescription $p_\mu \to p_\mu - q A_\mu$ | `kg_minimal_coupling_and_current.md` §2 |
| Gauge-covariant derivative $D_\mu = \partial_\mu + (i q/\hbar) A_\mu$ | `kg_minimal_coupling_and_current.md` §2 |
| Interacting Klein-Gordon (eq. 4) | `kg_minimal_coupling_and_current.md` §3 |
| Gauge invariance of the interacting equation | `kg_minimal_coupling_and_current.md` §4 |
| Four-current $j^\mu$ (eq. 6) | `kg_minimal_coupling_and_current.md` §5 |
| Reality, gauge invariance, conservation of $j^\mu$ | `kg_minimal_coupling_and_current.md` §5 |
| Non-relativistic limit to Schrödinger-EM (eq. 7) | `kg_minimal_coupling_and_current.md` §6 |

**All sixteen structural features of Stage R.1 are FORCED** from primitives + promoted identifications + Lorentz-invariance constraints + gauge-invariance constraints. No new primitives; no additional postulates beyond Phase-1 content plus the local-U(1)-gauge-invariance structural commitment.

### 3.2 What is inherited

| Constant | Source of inheritance |
|---|---|
| Speed of light $c$ | Dimensional Atlas relativistic regime |
| Reduced Planck constant $\hbar$ | Dimensional Atlas Madelung anchoring (via U3) |
| Scalar-particle mass $m$ | Species-level anchoring (chain-mass derivation open, Arc M) |
| Electromagnetic charge $q$ | Species-level anchoring (coupled with chain-mass) |
| Electromagnetic four-potential $A_\mu(x^\nu)$ | External-field specification; apparatus-level |

The inheritance list is exactly the set of empirical constants that enter relativistic scalar quantum mechanics in the standard formulation; Stage R.1 does not introduce additional inherited content.

### 3.3 Not addressed in Stage R.1

| Item | Deferred to |
|---|---|
| Spinor / Dirac content for fermionic chains | Arc R Stage R.3 (requires rule-type taxonomy from Stage R.2) |
| Rule-type taxonomy | Arc R Stage R.2 |
| Dynamical origin of $A_\mu$ (Maxwell's equations) | Separate sub-program within Arc R or Arc Q |
| Quantization of the electromagnetic field (photons) | Arc Q (QFT extension) |
| Multi-particle scalar-field content | Arc Q |
| Interaction terms beyond minimal coupling (strong force, etc.) | Arc Q with appropriate gauge-group extensions |
| Chain-mass primitive-level derivation | Arc M |
| Primitive-level derivation of $\hbar$ | `hbar_origin.md` catalogued inheritance; no derivation |
| Interpretive resolution of non-positive-definite $j^0$ | Arc Q |

---

## 4. Stage R.1 closure

**Arc R Stage R.1 is structurally complete.** The scalar relativistic quantum mechanics of bosonic chains in external electromagnetic fields is derived end-to-end from the ED primitive framework plus local U(1) gauge invariance, with only the standard empirical constants inherited.

### 4.1 Sub-stage completion checklist

- [x] Stage R.1.1 — Lorentz-covariant participation-measure scoping (`relativistic_participation_measure.md`).
- [x] Stage R.1.2 — Free-particle Klein-Gordon emergence + non-relativistic limit to free Schrödinger (`klein_gordon_emergence.md`).
- [x] Stage R.1.3 — Minimal coupling, gauge-covariant derivative, interacting Klein-Gordon equation (`kg_minimal_coupling_and_current.md` §3–§4).
- [x] Stage R.1.4 — Conserved four-current, continuity equation (`kg_minimal_coupling_and_current.md` §5).
- [x] Stage R.1.5 — Non-relativistic limit to Schrödinger-EM (`kg_minimal_coupling_and_current.md` §6).
- [x] Stage R.1.6 — Synthesis memo (this document).

### 4.2 Legitimate Stage R.1 claims

With Stage R.1 closed, the following claims are derivable within the ED framework:

- **Scalar relativistic quantum mechanics emerges from ED primitives.** The Klein-Gordon equation, its minimal-coupling extension, the conserved charge current, and the non-relativistic limit to Schrödinger with electromagnetic coupling are all structural consequences of the Lorentz-covariant participation measure.

- **Phase-1 Schrödinger is a sub-theory of Stage-R.1 scalar relativistic QM.** The non-relativistic limit $v/c \to 0$ recovers Phase 1 exactly. No Phase-1 result is invalidated; all are embedded as the low-velocity limit of Stage R.1.

- **Gauge invariance is structurally forced, not postulated.** Local U(1) gauge symmetry appears in Stage R.1 as a structural commitment at the participation-phase level, with the minimal-coupling prescription as its unique first-order consequence.

- **Charge conservation is structurally forced.** The continuity equation $\partial_\mu j^\mu = 0$ is a direct algebraic consequence of the interacting Klein-Gordon equation and the gauge-invariant current.

### 4.3 Explicit non-claims

Stage R.1 does **not** claim:

- A derivation of the numerical value of the elementary charge $q$ or the fine-structure constant $\alpha$.
- A derivation of particle masses (chain-mass derivation is Arc M).
- A spinor or Dirac content (requires rule-type taxonomy, Stage R.2).
- A multi-particle or quantum-field-theoretic content (requires Arc Q).
- A dynamical origin of the electromagnetic field (separate sub-program).
- A resolution of the single-particle Klein-Gordon interpretive pathologies (requires Arc Q).

---

## 5. Transition to Stage R.2

### 5.1 Why Stage R.2 is next

With Stage R.1 complete, the natural next sub-stage of Arc R is Stage R.2 — the **rule-type taxonomy derivation**. This sub-stage is the critical bottleneck for the remaining relativistic content (Dirac, spin-statistics, spinor interactions) and is also the prerequisite for Arc M (chain-mass derivation). Both arcs share this sub-program, making Stage R.2 the highest-leverage next target in the Phase-2 program.

### 5.2 What Stage R.2 must deliver

Stage R.2 derivation scope (per `phase2_extensions_roadmap.md §2.1 and §3.3`):

- **Rule-type classification** from ED primitives: what structurally distinguishes one rule-type from another at the Primitive 07 level (§7.4 is currently open).
- **Bosonic vs fermionic distinction**: the specific structural feature that produces the difference between Bose-Einstein and Fermi-Dirac statistics.
- **Spinor index content**: the internal index structure of $P_{K, \alpha}$ for fermionic rule-types; derivation of the four-component spinor dimensionality for spin-1/2 chains.
- **Clifford algebra** $\{\gamma^\mu, \gamma^\nu\} = 2 g^{\mu\nu}$ from primitive-level structure.
- **Spin-statistics connection**: derivation that fermions have half-integer spin and anticommute under exchange; bosons have integer spin and commute.

### 5.3 Stage R.2 opening memo

The Stage-R.2 opening memo would be `rule_type_taxonomy.md`, scoping the classification problem and identifying the structural commitments needed to produce fermionic-vs-bosonic distinction from ED primitives.

### 5.4 After Stage R.2

Stage R.3 (Dirac emergence) follows, providing the spinor relativistic wave equation for fermionic chains. After Stage R.3, Arc R is structurally complete at the single-particle level, and Arc Q (QFT extension) and Arc M (chain-mass derivation) can proceed with the rule-type taxonomy in hand.

---

## 6. Phase-2 program status after Stage R.1 closure

### 6.1 Arc-by-arc status

| Arc | Status after this memo |
|---|---|
| Arc N (Non-Markovian) | Memory-kernel derivation complete (`memory_kernel_derivation.md`); platform-specific applications remaining |
| Arc R (Relativistic) | **Stage R.1 closed** (this memo); Stages R.2, R.3 remaining |
| Arc M (Chain-mass) | Blocked on rule-type taxonomy (shared with R.2) |
| Arc Q (QFT) | Blocked on R.3 and M |
| Subsidiary: ℏ-origin | Documented (`hbar_origin.md`); inheritance structure clarified |

### 6.2 Milestone progress

Per the Phase-2 roadmap's milestone scheme:

- **Short-term milestones:** ℏ-origin memo, non-Markovian memory kernel, relativistic scoping — all complete.
- **Medium-term milestones:** Klein-Gordon emergence — complete (as part of Stage R.1); non-Markovian platform corrections and rule-type taxonomy scoping — open.
- **Long-term milestones:** Dirac, chain-mass, full QFT, Standard-Model emergence scoping — all contingent on rule-type taxonomy or further Phase-2 derivations.

### 6.3 Program-level observation

**The Phase-2 program has advanced from the short-term to the medium-term regime.** Stage R.1's closure is the first medium-term milestone achieved. The next medium-term milestone (rule-type taxonomy scoping, shared with Arcs R and M) is the natural next deliverable and is the highest-leverage single target: it unlocks Dirac (R.3), chain-mass (M), and eventually QFT (Q).

---

## 7. One-line summary

> **Arc R Stage R.1 — scalar relativistic quantum mechanics for bosonic chains — is structurally complete. The Lorentz-covariant participation measure $P_K(x^\mu) = \sqrt{b_K} e^{i\pi_K}$ produces, in the thin-participation limit, the free Klein-Gordon equation $(\Box + m^2c^2/\hbar^2)\Psi = 0$ and, under minimal electromagnetic coupling, the interacting Klein-Gordon equation $(D_\mu D^\mu + m^2c^2/\hbar^2)\Psi = 0$ with gauge-covariant derivative $D_\mu = \partial_\mu + (iq/\hbar)A_\mu$. The conserved gauge-invariant four-current $j^\mu = (i\hbar/2m)(\Psi^* D^\mu \Psi - \Psi (D^\mu \Psi)^*)$ satisfies $\partial_\mu j^\mu = 0$ directly from the interacting wave equation. The non-relativistic limit reduces exactly to the Phase-1 Schrödinger equation with electromagnetic coupling $i\hbar \partial_t \psi = [(1/2m)(-i\hbar\nabla - q\mathbf{A})^2 + q\varphi]\psi$. All sixteen structural features are FORCED from ED primitives plus Lorentz invariance plus local U(1) gauge invariance; dimensional constants $c, \hbar, m, q$ and the external field $A_\mu$ are inherited. No new primitives. Stage R.1 closed; Stage R.2 (rule-type taxonomy) is the critical next sub-program, shared with Arc M (chain-mass) and prerequisite for Stage R.3 (Dirac) and eventually Arc Q (QFT). The Phase-2 program has advanced to the medium-term regime.**

---

## 8. Cross-references

### Stage-R.1 source memos
- Scoping: [`quantum/foundations/relativistic_participation_measure.md`](relativistic_participation_measure.md)
- Free Klein-Gordon: [`quantum/foundations/klein_gordon_emergence.md`](klein_gordon_emergence.md)
- Minimal coupling + current: [`quantum/foundations/kg_minimal_coupling_and_current.md`](kg_minimal_coupling_and_current.md)

### Phase-1 anchoring (embedded as non-relativistic sub-theory)
- Phase-1 Schrödinger (non-relativistic limit recovery target): [`quantum/foundations/schrodinger_emergence.md`](schrodinger_emergence.md)
- Phase-1 QM-emergence synthesis: [`quantum/foundations/qm_emergence_synthesis.md`](qm_emergence_synthesis.md)
- Phase-1 QM-emergence closure: [`quantum/foundations/qm_emergence_closure.md`](qm_emergence_closure.md)
- ℏ-origin memo (inheritance structure preserved in Stage R.1): [`quantum/foundations/hbar_origin.md`](hbar_origin.md)

### Phase-2 program context
- Phase-2 extensions roadmap: [`quantum/foundations/phase2_extensions_roadmap.md`](phase2_extensions_roadmap.md) §2.1
- Arc-N non-Markovian extension (parallel arc): [`quantum/foundations/memory_kernel_derivation.md`](memory_kernel_derivation.md)
- Lindblad extension (Phase-1 → Phase-2 bridge): [`quantum/foundations/lindblad_extension.md`](lindblad_extension.md)

### Primitive stack (covariant reformulations in Stage R.1)
- Primitive 02 (chain → worldline): [`quantum/primitives/02_chain.md`](../primitives/02_chain.md)
- Primitive 04 (four-band → covariant scalars): [`quantum/primitives/04_participation_bandwidth.md`](../primitives/04_participation_bandwidth.md)
- Primitive 06 (ED gradient → four-gradient): [`quantum/primitives/06_ed_gradient.md`](../primitives/06_ed_gradient.md)
- Primitive 13 (relational timing → proper-time): [`quantum/primitives/13_relational_timing.md`](../primitives/13_relational_timing.md)
- Primitive 07 (channel + rule-type; §7.4 is the Stage R.2 opening target): [`quantum/primitives/07_channel.md`](../primitives/07_channel.md)

### Classical references
- Klein, O. (1926). *Zeitschrift für Physik* **37**, 895.
- Gordon, W. (1926). *Zeitschrift für Physik* **40**, 117.
- Weyl, H. (1929). Elektron und Gravitation I. *Zeitschrift für Physik* **56**, 330–352.
- Pauli, W. (1940). The Connection Between Spin and Statistics. *Physical Review* **58**, 716–722.
- Weinberg, S. (1995). *The Quantum Theory of Fields*, Vol. 1. Cambridge University Press.
- Peskin, M. E., Schroeder, D. V. (1995). *An Introduction to Quantum Field Theory*. Westview Press.

---

## 9. Closure statement

**Arc R Stage R.1 is hereby closed.**

Scalar relativistic quantum mechanics for bosonic chains in external electromagnetic fields is structurally complete within the ED framework, with the free and interacting Klein-Gordon equations, the conserved four-current, the non-relativistic limit to Schrödinger with electromagnetic coupling, and the gauge-invariance content all derived from primitives + Lorentz invariance + local U(1) gauge invariance. Three derivation memos (scoping, free Klein-Gordon, minimal coupling + current) together with this synthesis close the sub-arc.

Remaining Arc R work (Stages R.2 rule-type taxonomy and R.3 Dirac) is open and documented. Stage R.2 is the critical next sub-program; it is shared with Arc M and is prerequisite for Arc R Stage R.3 and Arc Q. Arc N has a parallel open item (platform-specific non-Markovian corrections) and is independent of Stage R.2.

Stage R.1 closure date: **2026-04-24**.
