# Appendix A — Theorem Provenance Map

## A.1 Appendix Overview

This appendix is the program's structural-foundation theorem inventory in expanded form. For every theorem cited in the monograph — the sixteen Phase-1 closure theorems T1–T16, the gauge-field theorem T17, the kernel-arrow theorem T18, the substrate-gravity theorems T19, T20, ECR, T21, the foundational theorems N1, GR1, DCGT, and the unresolved-regime theorem UR-1 — Appendix A states what the theorem establishes, names the primitives and intermediate results that must be in place before the theorem can be derived, identifies the canonical source paper(s) where the derivation lives, and records which chapters of the monograph use the theorem as a load-bearing component.

The intent is navigational. The monograph's chapters do not duplicate derivations: when Chapter 5 says "Born's rule emerges via the Gleason route" or Chapter 11 says "T19 fixes $G = c^3\ell_P^2/\hbar$ from the substrate cumulative-strain mechanism," the reader who wants the proof needs a single map from theorem name to dependency chain to source paper. Appendix A is that map. The provenance graph is consistent with the chapter dependency graph: every dependency-chain entry below appears in a chapter or earlier theorem, never forward in the structure.

---

## A.2 Reading the Provenance Entries

Each theorem is recorded under the following heads.

- **Statement** — what the theorem establishes, in one to three sentences. Form-FORCED content is named explicitly; value-INHERITED content (substrate constants, threshold values, prefactors whose closed form is downstream work) is flagged.
- **Dependency chain** — the primitives, prior theorems, and mathematical inputs (Gleason 1957, Stone 1932, Hadamard parametrix, multi-scale expansion, and so on) that are upstream. Every upstream item appears either in Chapters 1–4 of the monograph (substrate primitives, load-bearing invariants, DCGT, kernel-arrow) or in an earlier theorem in this appendix.
- **Canonical source.** The repository path where the derivation lives. Paths use the monograph's standard `papers/...` and `theory/...` and `arcs/...` conventions.
- **Used in chapters.** The monograph chapters where this theorem is load-bearing. A theorem may be referenced in additional chapters; the entry names the chapters where it carries structural weight.

---

## A.3 Phase-1 Closure of Quantum Mechanics — T1–T16

### T1–T16 — Sixteen FORCED theorems collectively closing the four QM postulates

**Statement.** The four standard QM postulates (the Born rule for outcome probabilities, the Schrödinger evolution rule for closed-system dynamics, the Heisenberg uncertainty relation as a structural lower bound, and the no-collapse measurement rule) are all derived from substrate primitives plus standard mathematical theorems. Form-FORCED content includes: the squared-modulus form of the Born probability rule (not merely a probabilistic frame), the linearity and first-order-in-time character of the Schrödinger generator, the $\hbar/2$ lower bound in canonical-conjugate uncertainty, and the irreversibility of the participation-event recording step. Value-INHERITED content includes: the absolute scale of $\hbar$, the precise spectrum of any concrete Hamiltonian, and the choice of representation (position, momentum, energy basis) — all of which follow conventional inheritance from substrate constants and operator-theoretic structure.

**Dependency chain.** Substrate primitives **P01** (event discreteness), **P02** (chain worldline), **P04** (bandwidth update), **P11** (commitment-irreversibility), and **P13** (proper-time ordering) supply the bandwidth structure on which every postulate rests. From P04 plus substrate non-contextuality of the participation rule, one obtains the bandwidth-conservation property across orthogonal decompositions of a participation-state, which is exactly the hypothesis of Gleason's theorem (1957) on Hilbert spaces of dimension $\geq 3$. Gleason's theorem then forces the Born rule's squared form. From substrate time-translation symmetry on closed systems plus continuity, Stone's theorem (1932) on one-parameter unitary groups forces the Schrödinger generator to be linear and first-order in time. From substrate finite-bandwidth (P04) plus orthogonal-component conjugacy, the Robertson-style commutator bound forces $\Delta A\,\Delta B \geq \tfrac{1}{2}|\langle[A,B]\rangle|$, and substituting canonical conjugates yields $\hbar/2$. From P11 commitment-irreversibility plus the participation-recording step, the measurement rule is obtained without postulating a "collapse" mechanism: the irreversibility is the substrate-level reason that the recording step is asymmetric.

**Canonical sources.**
- `papers/Phase_1/`
- `papers/QM_Emergence_Structural_Completion/`
- `papers/Born_Gleason/`
- `papers/U1_Participation_Measure/`
- `papers/U2_Inner_Product/`
- `papers/U3_Time_Translation_Schrodinger/`
- `papers/U4_Hamiltonian_Form/`
- `papers/U5_Translation_Momentum/`

**Used in chapters.** Chapter 5 (Phase-1 closure of QM); Chapter 6 (form-level QFT and quantum information, where T1–T16 are the substrate-floor on which T17 and UV-finiteness sit); Chapter 7 (quantum computation, where the Born-rule structure governs measurement statistics in any architectural class); Chapter 14 (cross-platform unifications: matter-wave Q-C boundary).

---

## A.4 T17 — Gauge-Field-as-Rule-Type

**Statement.** Gauge fields are participation measures of structural rule-types in the substrate. A gauge field is not a fundamental object in the ED ontology; it is the coarse-grained continuum measure of the local activity of a label-carrying participation rule. Gauge invariance is the interface property of label-carrying rules: relabelings that preserve the rule's substrate structure are exactly the gauge transformations of the emergent field. Form-FORCED content includes: the existence of a gauge-field measure for any compact-simple-group rule-type, the minimal-coupling form of its interaction with matter (a Lorentz force when specialized to the U(1) case), and the structural distinction between Abelian and non-Abelian rule-types. Value-INHERITED content includes: coupling constants, specific spectra of bound states, and the choice of rule-type in any given physical sector.

**Dependency chain.** Substrate primitives + label-carrying rule-type structure (Chapter 1 commitments) + DCGT coarse-graining (Chapter 3) → interface property of relabelings preserves the substrate rule, which is exactly gauge invariance at the continuum level. The non-Abelian extension is forced by the same interface argument when the rule-type's relabeling group is non-commutative; the substrate has no preference for Abelian rules.

**Canonical source.** `papers/Gauge_Fields_Theorem_17/`.

**Used in chapters.** Chapter 6 (form-level QFT); Chapter 9 (MHD and Yang–Mills: T17 plus DCGT supplies the substrate-derived non-Abelian continuum equation); Chapter 10 (T17's U(1) specialization in soft-matter electromagnetic dressing); Chapter 11 (substrate gravity: T17's structural distinction underwrites the substrate-gravity coupling channel).

---

## A.5 T18 — V1 Kernel Retardation (Kernel-Level Arrow of Time)

**Statement.** The V1 vacuum response kernel — the finite-width temporal-smearing kernel mediating effective-vacuum participation — is uniquely forced at the primitive level to have support restricted to the forward causal cone. No symmetric, advanced, or hybrid kernel is constructible at primitive level. The microscopic arrow of time is FORCED structurally rather than postulated. Form-FORCED content includes: forward-cone-only support of V1; the kernel's strict positivity on its support; the impossibility of substrate-level time-symmetric or advanced kernels. Value-INHERITED content includes: the exact width function of V1, the magnitude of its first temporal moment, and the absolute calibration of the response amplitude.

**Dependency chain.** **P01** + **P02** + **P04** + **P11** + **P13** + Theorem **N1** (V1 finite-width vacuum kernel) + the Q.8 effective-vacuum factorization (which routes substrate participation through the V1 channel) → V1 retarded.

**Canonical source.** `papers/Time_Arrow_Theorem_18/`.

**Used in chapters.** Chapter 4 (kernel-level arrow of time — the chapter is built around T18); Chapter 6 (form-level QFT, where T18 supplies the microscopic causal structure underlying the propagator); Chapter 12 (curvature emergence, where GR1 generalizes T18 to curved background); Chapter 13 (black-hole architecture, where the forward-cone-only V1 underwrites the decoupling-surface structure).

---

## A.6 T19 — Newton's Gravitational Constant from Substrate

**Statement.** Newton's gravitational constant is fixed by substrate constants:
```math
G = \frac{c^3 \ell_P^2}{\hbar}.
```
The derivation supplies the inverse-square form of the gravitational field around a stable participation structure and identifies the proportionality constant with the named combination of substrate constants. As a derived consequence, the substrate length scale is identified with the Planck length: any other identification would either over- or under-shoot the empirical value of $G$.

**Dependency chain.** Substrate cumulative-strain mechanism (substrate participation density responding to a stable-structure source) + holographic participation-count bound on a sphere of radius $R$ (the bound being a direct consequence of substrate event-discreteness and the unit substrate cell area $\sim \ell_P^2$) + substrate-level equipartition (energy distributing across viable substrate-scale modes) → inverse-square form + proportionality constant fixed.

**Canonical source.** `papers/Substrate_Gravity_Foundations/` (T19 derivation).

**Used in chapters.** Chapter 11 (substrate gravity — T19 is the first of four theorems closing the galactic-scale gravity layer); Chapter 12 (curvature emergence, where T19 underwrites the weak-field limit of the covariantized acoustic-metric scalar-tensor structure); Chapter 13 (black-hole architecture, where the area-law form $A/\ell_P^2$ inherits from T19's identification of $\ell_P$).

---

## A.7 T20 — MOND Transition Acceleration from Cosmic-Horizon Dipole

**Statement.** The MOND transition acceleration is fixed by substrate constants:
```math
a_0 = \frac{c\,H_0}{2\pi}.
```
The derivation routes through the cosmic horizon's dipole-projection contribution to a locally accelerating participation chain's substrate environment. The factor $2\pi$ is the azimuthal period of the leading anisotropic projection mode. The numerical match to the empirically extracted MOND acceleration is within roughly ten percent, parameter-free.

**Dependency chain.** Cosmic-horizon participation density (a substrate-level quantity sourced by all participation events within the horizon) + accelerating chain's anisotropic environment (the chain's acceleration breaks isotropy of its substrate vicinity) + dipole projection along the acceleration axis (the leading anisotropic mode) + azimuthal period $2\pi$ → $a_0 = cH_0/(2\pi)$.

**Canonical source.** `papers/Substrate_Gravity_Foundations/` (T20 derivation).

**Used in chapters.** Chapter 11 (substrate gravity — T20 is the cosmic-horizon-class acceleration entering ECR and T21); Chapter 12 (curvature emergence, where $a_0$ is the deep-MOND threshold in the covariantized scalar-tensor equation); Chapter 15 (public test inventory: BTFR slope-4 and zero-intrinsic-scatter predictions).

---

## A.8 ECR — ED Combination Rule

**Statement.** Newton-class accelerations $a_N$ and cosmic-horizon-class accelerations $a_0$ combine multiplicatively (geometric mean) in the deep-galactic regime:
```math
a = \sqrt{a_N \cdot a_0}.
```
The substrate-derived multiplicative-participation rule replaces MOND's phenomenological interpolation function in the asymptotic deep-MOND regime. ECR is named — not numbered — to reserve "P11" exclusively for the eleventh substrate primitive (commitment-irreversibility).

**Dependency chain.** **T19** + **T20** + substrate logarithmic stability landscape (substrate-level cross-term $\sqrt{G\,M\,a_0}\,\log(R/R_0)$ from the leading correction to Newton-class acceleration in the cosmic-horizon-modulated regime) → geometric-mean composition.

**Canonical source.** `papers/Substrate_Gravity_Foundations/` (ECR derivation).

**Used in chapters.** Chapter 11 (substrate gravity — ECR is the bridge between T19/T20 and T21); Chapter 12 (curvature emergence, where the modified Poisson equation $\nabla\cdot[\mu(|\nabla\Phi|/a_0)\nabla\Phi] = 4\pi G\rho_m$ contains ECR in the asymptotic deep-MOND limit).

---

## A.9 T21 — Slope-4 Baryonic Tully–Fisher Relation

**Statement.** The slope-4 baryonic Tully–Fisher relation is forced:
```math
v_\mathrm{flat}^4 = G\,M_b\,a_0.
```
The proportionality constant is in fundamental quantities, not phenomenological. Zero intrinsic scatter is predicted in the asymptotic deep-MOND regime; observed scatter is dominated by mass-measurement uncertainty rather than by genuine population variance. The slope is robust under all admissible substrate-level variations of the closure: exponent 4 cannot be shifted without violating either T19 or T20 or ECR.

**Dependency chain.** **T19** + **T20** + **ECR** + circular-orbit centripetal balance ($v^2/R = a$, with $a$ given by ECR in the deep-MOND asymptote) → $v^4 = G\,M\,a_0$.

**Canonical source.** `papers/Substrate_Gravity_Foundations/` (T21 derivation).

**Used in chapters.** Chapter 11 (substrate gravity — T21 is the empirical anchor of the galactic-scale gravity layer); Chapter 15 (public test inventory: BTFR slope-4 has PASSED; zero-intrinsic-scatter prediction is ANCHORED).

---

## A.10 N1 — V1 Finite-Width Vacuum Kernel

**Statement.** The V1 vacuum response kernel is finite-width and chain-sourced. The kernel mediates substrate-level participation events through an effective-vacuum response of finite temporal extent; its width is set by substrate constants and is not zero (point-instantaneous response is forbidden). Form-FORCED content includes: the existence of a finite-width vacuum kernel, its chain-sourced character, and its strict positivity on support. Value-INHERITED content includes: the precise width function and its first and second moments.

**Dependency chain.** Substrate primitives → effective-vacuum response factorization + finite-width temporal kernel via substrate event-discreteness (P01) and bandwidth update (P04).

**Canonical source.** Theorem N1 paper (V1 kernel inventory).

**Used in chapters.** Chapter 2 (load-bearing invariants — V1 is named); Chapter 4 (kernel-arrow — N1 is upstream of T18); Chapter 6 (form-level QFT — N1 supplies the propagator's microscopic structure); Chapter 8 (Navier–Stokes — V1 underwrites the R1 substrate-cutoff regularization); Chapter 9 (Yang–Mills — V1's finite width is the substrate-cutoff governing the mass-gap mechanism); Chapter 12 (curvature emergence — N1 is upstream of GR1).

---

## A.11 GR1 — V1 Curved-Spacetime Extension (Phase-3)

**Statement.** The V1 vacuum kernel extends to curved spacetime via Hadamard-parametrix causal-future restriction with the Synge world function. The curved-spacetime kernel inherits Theorem 18's forward-cone-only support and preserves P11 time orientation along curved geodesics. GR1 is structurally complete at the form level; full Einstein-equation emergence remains downstream work.

**Dependency chain.** **N1** + **T18** + Hadamard parametrix (the curved-spacetime analogue of the Minkowski Green's function) + Synge world function (geodesic interval substituting for $\sigma(x,y) = (x-y)^2/2$ on a curved background) → curved-spacetime V1 retarded.

**Canonical source.** Phase-3 GR1 derivation (paper under the substrate-gravity / curvature-emergence cluster).

**Used in chapters.** Chapter 12 (curvature emergence — GR1 is load-bearing); Chapter 13 (black-hole architecture — GR1 underwrites the curved-background V1 inside which decoupling surfaces form).

---

## A.12 DCGT — Diffusion Coarse-Graining Theorem

**Statement.** DCGT is the substrate-to-continuum bridge for canonical-ED dynamical content. Within the hydrodynamic-window scale separation
```math
\ell_P \ll R_\mathrm{cg} \ll L_\mathrm{flow},
```
substrate dynamics admit a multi-scale expansion to coarse-grained continuum equations. The leading-order content covers: scalar diffusion (canonical ED participation density); directional viscosity (chain-aligned substrate-momentum transport); the V1→R1 substrate-cutoff hyperviscous regularization $-\kappa\mu_\mathrm{V1}\ell_P^2\nabla^4\mathbf{v}$; the V5→Maxwell viscoelastic memory kernel; and the T17 minimal-coupling Lorentz interaction in U(1) and non-Abelian extension. The cross-bandwidth $\Gamma_\mathrm{cross}\sim \exp[-\alpha\sigma]$ between adjacent regions is a direct DCGT output.

**Dependency chain.** Substrate primitives + hydrodynamic-window scale separation (Chapter 3) + multi-scale expansion → cross-bandwidth $\Gamma_\mathrm{cross}\sim\exp[-\alpha\sigma]$ + leading-order continuum content.

**Canonical sources.**
- Arc D memos in `theory/Arc_D/`
- `papers/Navier Stokes_Synthesis_Paper/` Appendix D (DCGT)
- `papers/ED_QFT_Overview/` (program-level synthesis with DCGT central)

**Used in chapters.** Chapter 3 (the chapter is built around DCGT); Chapter 8 (Navier–Stokes — DCGT supplies the substrate-to-NS bridge); Chapter 9 (MHD and Yang–Mills — DCGT plus T17 supplies the non-Abelian continuum equation); Chapter 10 (soft-matter mobility — DCGT plus V5 supplies the viscoelastic memory kernel); Chapter 11 (substrate gravity — DCGT consolidates T19/T20/ECR/T21 into the flat-background field equation $\nabla\cdot[\mu(|\nabla\Phi|/a_0)\nabla\Phi] = 4\pi G\rho_m$); Chapter 12 (curvature emergence — DCGT-on-curved-background underwrites the covariantized scalar-tensor equation).

---

## A.13 UR-1 — Unresolved-Regime Characterization Theorem

**Statement.** Three independently necessary substrate conditions characterize the unresolved-rule regime that quantum computation requires:

1. (i) bounded multiplicity ($\mathcal{M} \leq \mathcal{M}_\mathrm{crit}$),
2. (ii) sustained cross-endpoint connectivity ($\Gamma_\mathrm{cross} \geq \Gamma_\mathrm{min}$),
3. (iii) bounded commitment-injection ($\Lambda \leq \Lambda_\mathrm{V1}$).

The unresolvedness functional decomposes as a three-factor product
```math
\mathcal{U}(\mathcal{S},t) = \mu(\mathcal{M}/\mathcal{M}_\mathrm{crit}) \cdot \kappa(\Gamma_\mathrm{cross}/\Gamma_\mathrm{min}) \cdot \exp\!\Big(-\!\!\int_0^t \Lambda(s)\,ds\Big),
```
(multiplicity headroom × rule-spanning connectivity × commitment-survival exponential), and the QC operating window is
```math
\tau_\mathrm{QC} = \min(\tau_{(\mathrm{i})},\tau_{(\mathrm{ii})},\tau_{(\mathrm{iii})}).
```
Each of (i)/(ii)/(iii) is necessary and no two are jointly sufficient. The three-factor exhaustiveness underwrites the architectural taxonomy A/B/C of Chapter 7.

**Dependency chain.** Substrate primitives (especially **P11** commitment-irreversibility) + **DCGT** + **V1** + multiplicity-as-entropy reading (Chapter 2) → three-factor product form of $\mathcal{U}$ → three independent conditions.

**Canonical source.** `papers/Quantum_Computing_Foundations/`; Arc Q-COMPUTE Memo 2 in `theory/Quantum_Computing/`.

**Used in chapters.** Chapter 7 (quantum computation — the chapter is built around UR-1 and the multiplicity-cap function $M$); Chapter 14 (cross-platform unifications — UR-1's $\mathcal{M}_\mathrm{crit}$ underwrites both the matter-wave Q-C boundary and the qubit-system multiplicity wall); Chapter 15 (public test inventory: Class A wall, Class B exponential gap-suppression, and Class C correlation-budget plateau predictions).

---

## A.14 Provenance Graph (Topological Summary)

The dependency structure among the foundational theorems forms a directed acyclic graph rooted at the substrate primitives. Reading the graph downstream:

- **P01–P13** → **N1** (V1 finite-width vacuum kernel)
- **P01, P02, P04, P11, P13** + **Q.8 effective-vacuum factorization** + **N1** → **T18** (kernel-level arrow of time)
- **P01–P13** + **Gleason 1957** + **Stone 1932** → **T1–T16** (Phase-1 closure of QM)
- **P01–P13** + **DCGT** → **T17** (gauge-field-as-rule-type)
- **P01–P13** + **hydrodynamic-window scale separation** → **DCGT**
- **P01–P13** + **substrate cumulative-strain** + **holographic participation-count bound** → **T19** ($G$ from substrate)
- **P01–P13** + **cosmic-horizon dipole projection** → **T20** ($a_0$ from cosmic horizon)
- **T19** + **T20** + **substrate logarithmic stability landscape** → **ECR** (geometric-mean composition)
- **T19** + **T20** + **ECR** + **circular-orbit balance** → **T21** (BTFR slope 4)
- **N1** + **T18** + **Hadamard parametrix** + **Synge world function** → **GR1** (curved-background V1)
- **P01–P13** (especially P11) + **DCGT** + **V1** + **multiplicity-as-entropy** → **UR-1** (three-factor unresolvedness)

The dependency graph contains no cycles: every theorem depends only on the substrate primitives and on theorems strictly upstream. The chapter dependency graph in the monograph respects this ordering — Chapter $X$ never invokes a theorem whose dependencies have not been established by Chapter $X-1$ or earlier.

---

## A.15 Canonical Sources (Aggregated)

For convenient navigation, the canonical-source paths cited above are aggregated here:

- `papers/Phase_1/`
- `papers/QM_Emergence_Structural_Completion/`
- `papers/Born_Gleason/`
- `papers/U1_Participation_Measure/`
- `papers/U2_Inner_Product/`
- `papers/U3_Time_Translation_Schrodinger/`
- `papers/U4_Hamiltonian_Form/`
- `papers/U5_Translation_Momentum/`
- `papers/Gauge_Fields_Theorem_17/`
- `papers/Time_Arrow_Theorem_18/`
- `papers/Substrate_Gravity_Foundations/`
- `papers/Navier Stokes_Synthesis_Paper/` (Appendix D for DCGT)
- `papers/Quantum_Computing_Foundations/`
- `papers/ED_QFT_Overview/`
- Theorem N1 paper (V1 kernel inventory)
- Phase-3 GR1 derivation paper
- `theory/Arc_D/` (DCGT memos)
- `theory/Quantum_Computing/` (Arc Q-COMPUTE memos)
- `theory/Substrate_Gravity/` (substrate-gravity arc memos)
- `arcs/arc-B/` (Arc B closure memos for T18)

---

## A.16 Optional Figures

The following diagrams are described for inclusion in the final monograph:

- **Figure A.1 — Provenance DAG.** Directed acyclic graph with nodes for each theorem (T1–T21, ECR, N1, GR1, DCGT, UR-1) and the substrate-primitive cluster {P01–P13}. Edges encode upstream dependencies. Color-coding: substrate primitives (P-cluster) in one shade; foundational theorems N1/GR1/DCGT/T18 in a second; QM-closure cluster T1–T16 in a third; substrate-gravity cluster T19/T20/ECR/T21 in a fourth; gauge/QC cluster T17/UR-1 in a fifth.
- **Figure A.2 — Theorem-to-chapter incidence matrix.** Rows: theorems. Columns: chapters 1–15. Filled cells indicate "load-bearing." Used to verify the chapter dependency graph against the provenance graph.
- **Table A.1 — Form-FORCED vs Value-INHERITED inventory.** For each theorem, two columns separating which content is form-FORCED and which is value-INHERITED, exactly as recorded in the entries above.

---

## A.17 Dependency Section

Appendix A inherits the substrate-primitive layer (Chapter 1), the load-bearing invariants (Chapter 2), the DCGT bridge (Chapter 3), and the kernel-arrow structure (Chapter 4). It is consistent with the chapter-by-chapter dependency graph. No theorem in this appendix is invoked in a chapter prior to its dependencies being established; no entry above introduces content not already named in the chapter inventory.

The provenance graph is consistent with Appendix B (notation glossary): every symbol used in a theorem statement is defined in Appendix B. It is consistent with Appendix C (paper-to-chapter cross-reference): every canonical-source path above appears in Appendix C under the chapter to which the source paper is assigned. It is consistent with Appendix D (substrate constants): every substrate constant appearing in a theorem statement (notably $c$, $\hbar$, $H_0$, $\ell_P$, $G$, $a_0$) is recorded in Appendix D with its structural role.
