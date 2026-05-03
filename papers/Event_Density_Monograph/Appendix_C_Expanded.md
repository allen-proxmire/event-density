# Appendix C — Paper-to-Chapter Cross-Reference

## C.1 Appendix Overview

This appendix assigns every publication-grade Event Density paper to exactly one chapter of the monograph. The assignment is structural rather than thematic: each paper is placed at the chapter where its content is load-bearing, even when the paper's results are referenced in later chapters. Where a paper covers material spanning multiple chapters (notably the NS Synthesis Paper with its Appendices C, D, and E), the main paper is assigned to its anchoring chapter and each appendix is assigned to the chapter for which it is structurally definitive.

The cross-reference is consistent with Appendix A (theorem provenance map): every canonical-source path cited in Appendix A appears here under the chapter to which the source paper is assigned. It is consistent with Appendix B (notation glossary): every symbol defined in Appendix B has its canonical definition in a paper assigned here. It is consistent with Appendix D (substrate constants): every constant defined in Appendix D has its derivation or empirical anchor in a paper assigned here. Repository paths are stated relative to the repository root `event-density/`, exactly as in the chapter sources.

---

## C.2 Part I — Substrate Foundations

### Chapter 1 — The Substrate Ontology (P1–P13)

- **`papers/Event_Density_Ontology_and_Axioms/`** — Canonical inventory of the thirteen substrate primitives and the axiomatic structure of the program. Every later result is reachable from a subset of P1–P13 plus mathematical structure.
- **`papers/Foundations_of_Event_Density/`** — Companion foundations collection: discusses the ontological commitments behind each primitive, the substrate-locality conditions, and the boundary between substrate ontology and emergent continuum physics.
- **`papers/ED_One_Substrate_Three_Domains/`** — Program-overview / orientation context. Used in Chapter 1 only as a reading aid for situating the substrate ontology within the program's three-domain organization (substrate, continuum, gravity).

### Chapter 2 — Load-Bearing Invariants

- **ED-I-01 (Superconductivity)** — Multiplicity-as-entropy reading. Establishes the structural identification between substrate multiplicity $\mathcal{M}$ and the entropic content of substrate participation pathways, anchored against superconducting condensate behavior.
- **ED-I-23 (Josephson Junctions)** — Multiplicity at engineered low-$\mathcal{M}$ regions. Demonstrates the substrate-level mechanism by which engineered low-multiplicity regions sustain phase-coherent participation across a junction.
- **ED-I-29 (Tunneling)** — Sparse-$\sigma$ regions and global rule reconfiguration. Connects the gradient-sparsity invariant $\sigma$ to the substrate-level mechanism of tunneling as a sparse-$\sigma$ rule reconfiguration rather than barrier penetration.
- **ED-I-06 (Fields and Forces in Event Density)** — Ontological roof providing field/force vocabulary. The retroactive ontological frame that grounds the load-bearing invariants in a substrate-derived field/force taxonomy.

### Chapter 3 — The Coarse-Graining Bridge (DCGT)

- **`papers/Navier Stokes_Synthesis_Paper/` Appendix D (DCGT)** — The canonical derivation of the Diffusion Coarse-Graining Theorem. Contains the multi-scale expansion, the hydrodynamic-window scale-separation conditions, and the leading-order continuum content (scalar diffusion, directional viscosity, V1→R1, V5→Maxwell, T17 minimal coupling).
- **Arc D memos in `theory/Arc_D/`** — Six-memo arc producing DCGT. Records the substrate-to-continuum bridge construction step by step.
- **`papers/ED_QFT_Overview/`** — Program-level synthesis with DCGT central. Shows DCGT operating uniformly across the QM, QFT, NS, MHD, YM, soft-matter, and substrate-gravity sectors.

### Chapter 4 — Kernel-Level Arrow of Time (N1 + T18)

- **`papers/Time_Arrow_Theorem_18/`** — Canonical T18 derivation: V1 retardation forced at primitive level. Establishes the kernel-level arrow of time as a structural FORCED result rather than a postulated boundary condition.
- **N1 derivation paper (V1 finite-width kernel)** — Canonical N1 derivation: existence and finite width of the V1 vacuum response kernel. Upstream of T18.
- **`arcs/arc-B/`** — Arc B closure memos. Records the closure of the kernel-arrow arc; supplies the Q.8 effective-vacuum factorization that underwrites T18.

---

## C.3 Part II — Quantum Sector

### Chapter 5 — Phase-1 Closure of QM (T1–T16)

- **`papers/Phase_1/`** — Canonical Phase-1 closure paper: the sixteen forced theorems collectively deriving the four QM postulates from substrate primitives plus mathematical theorems (Gleason 1957, Stone 1932).
- **`papers/QM_Emergence_Structural_Completion/`** — Companion paper on the structural-completion methodology and the boundary between FORCED-form and INHERITED-value content in the QM emergence program.
- **`papers/Born_Gleason/`** — Detailed treatment of the Born-rule derivation via Gleason's theorem. The substrate-level argument for bandwidth-conservation across orthogonal decompositions, supplying Gleason's hypothesis.
- **`papers/U1_Participation_Measure/`** — U1: the substrate-derived participation-measure structure underlying state-vector formalism.
- **`papers/U2_Inner_Product/`** — U2: derivation of the inner-product structure on the participation-state space.
- **`papers/U3_Time_Translation_Schrodinger/`** — U3: time-translation symmetry plus Stone's theorem yielding the Schrödinger generator's linearity and first-order character.
- **`papers/U4_Hamiltonian_Form/`** — U4: derivation of the Hamiltonian's substrate-level form.
- **`papers/U5_Translation_Momentum/`** — U5: derivation of the canonical translation/momentum structure and the canonical commutator.

### Chapter 6 — Form-Level QFT and Quantum Information (T17, UV-FIN, ED-I-13)

- **`papers/Gauge_Fields_Theorem_17/`** — Canonical T17 derivation: gauge fields as participation measures of structural rule-types. Covers Abelian U(1) and non-Abelian compact-simple-group cases.
- **ED-I-13 (Quantum Information: Channel Geometry)** — Quantum-information channel-geometry interpretation grounded in T17's interface-property reading.
- **`papers/Arc_Q/`** — Arc Q closure memos: gauge-field-as-rule-type arc.
- **`papers/Arc_R/`** — Arc R closure memos: substrate-level UV finiteness via V1 finite width.

### Chapter 7 — Quantum Computation (UR-1, $M$, A/B/C)

- **`papers/Quantum_Computing_Foundations/`** — Canonical Q-COMPUTE Foundations Paper. Contains the UR-1 derivation, the multiplicity-cap function $M(\mathcal{S}, K, \mathcal{E}, \mathcal{O})$, the three-class architectural taxonomy A/B/C, and the closed-form-substrate-constants targets O-QC-1 through O-QC-6.
- **Arc Q-COMPUTE memos in `theory/Quantum_Computing/`** — Seven-memo arc producing the Q-COMPUTE Foundations Paper. Records the architectural-class derivation, the meta-architectural overlay structure, and the cross-domain echo with BH-2 ($\Gamma_\mathrm{cross}$ collapse).
- **ED-I-14 (Topological Effects)** — Topological-effects interpretation underwriting the Class B (global-geometric-rigidity) projection of $M$.
- **ED-I-18 (Multi-Timescale Photonics)** — Multi-timescale photonics interpretation; the Hafezi 2025 multi-timescale photonics anchor lives here as a PASSED prediction.
- **ED-I-12 (Photonics)** — Photonics interpretation supplying the substrate-level reading of photonic platforms relevant to Class A and Class C realizations.

---

## C.4 Part III — Continuum and Dynamics

### Chapter 8 — Navier–Stokes Architectural Foundations

- **`papers/Navier Stokes_Synthesis_Paper/` (main + Appendix C)** — The NS Synthesis Paper consolidates the full NS program: Path B-strong, the Intermediate Path C closure, the R1 substrate-cutoff regularization, the form-FORCED viscosity, and the vortex-stretching obstruction analysis. Appendix C covers the MHD extension (assigned to Chapter 9).
- **Arc NS memos in `theory/Navier Stokes/`** — Records the NS-1, NS-2, NS-3, NS-Smoothness, NS-Turb, P4-NN, NS-Q, and NS-MHD arc closures.
- **ED-I-06 (Fields and Forces)** — Ontological roof for the NS classification: identifies advection-non-ED and induction-kinematic-non-ED as transport-kinematic frame artifacts rather than substrate primitives.

### Chapter 9 — Magnetohydrodynamics and Yang–Mills

- **`papers/Navier Stokes_Synthesis_Paper/` Appendix C (MHD)** — Full MHD treatment: the H1/H2/H3 hold conditions, the 6:2:3 classification of eleven MHD items into canonical-ED, transport-kinematic, and ED-coupled.
- **`papers/Navier Stokes_Synthesis_Paper/` Appendix E (Yang–Mills)** — Full Yang–Mills treatment integrated into the NS Synthesis Paper. Contains the substrate-derived continuum YM equation $D_\mu F^{\mu\nu} = J^\nu$ via DCGT generalized to non-Abelian + T17, plus the mass-gap mechanism via V1 second-moment plus non-Abelian quartic stabilization.
- **Arc YM memos in `theory/Yang_Mills/`** — Six-memo arc YM-1 through YM-6 producing the YM closure. Records the structurally-positive Clay-relevance verdict and the OS-positivity audit.

### Chapter 10 — Soft-Matter Mobility and Non-Newtonian Rheology

- **`papers/Universal_Mobility_Law/`** — Canonical Universal Mobility Law paper. Form-FORCED $M(\rho) \propto (1 - \rho/\rho_\mathrm{max})^\beta$ with canonical $\beta = 2$; empirical $\beta \approx 1.72 \pm 0.37$ across ten systems (PASSED).
- **`papers/P4_NonNewtonian_Paper_Draft/`** — P4-NN paper: substrate-derived Krieger-Dougherty form plus Maxwell viscoelastic memory via V5-DCGT.

---

## C.5 Part IV — Gravity and Cosmology

### Chapter 11 — Substrate Gravity at Galactic Scale (T19, T20, ECR, T21)

- **`papers/Substrate_Gravity_Foundations/Substrate_Gravity_Foundations_Paper.{md,tex,pdf}`** — Canonical Substrate Gravity Foundations Paper. Contains T19 ($G = c^3\ell_P^2/\hbar$), T20 ($a_0 = c\,H_0/(2\pi)$), the ED Combination Rule ($a = \sqrt{a_N\,a_0}$), and T21 (BTFR slope-4).
- **`papers/Substrate_Gravity_Foundations/ED_substrate_gravity_foundations_2026-04-28.{md,tex,pdf}`** — Detailed-derivation companion paper. Records the dipole-projection derivation of $a_0$, the substrate-cumulative-strain mechanism for T19, and the substrate logarithmic stability landscape that produces ECR.

### Chapter 12 — Curvature Emergence (Arc ED-10)

- **`papers/Substrate_Gravity_Foundations/`** — Curvature-emergence section in the extended-scope Substrate Gravity Foundations paper. Contains the substrate-FORCED scalar-tensor acoustic-metric covariantization $\nabla_\mu[\mu(\sqrt{g^{\alpha\beta}\nabla_\alpha\Phi\nabla_\beta\Phi}/a_0)\nabla^\mu\Phi] = 4\pi GT$, OS-positivity, ghost-freedom, and gradient-stability under (C1)-(C3).
- **Arc ED-10 memos in `theory/Substrate_Gravity/`** — Six-memo arc records the curvature-emergence closure; deep-MOND superluminality structurally FORCED as the only structural cost.

### Chapter 13 — Black-Hole Architecture (Arc BH)

- **`papers/Black_Hole_Foundations/`** — Canonical Black Hole Foundations Paper. Contains the decoupling-surface construction, the area-law form $S = (A/\ell_P^2)\log g$, the BHPT phase-shift structure, the helicity behavior, and the Kerr-twist accumulated frame-dragging vorticity.
- **Arc BH memos in `theory/Black_Holes/` (BH-1 through BH-7)** — Seven-memo arc producing the BH Foundations Paper. Records the structural-positive verdicts on no-singularities, information blocking and entanglement straddling, evaporation as participation re-routing, and the open follow-ons (B4 Hawking spectrum, superradiance amplitude, closed-form $\log g$, full Kerr interior audit).

---

## C.6 Part V — Empirical Synthesis

### Chapter 14 — Cross-Platform Unifications and Methodology

- **`papers/ED_QFT_Overview/`** — Program-level synthesis. Twelve sections integrating Phase-1 QM emergence + foundational theorems + DCGT + NS/MHD + Yang–Mills + substrate-gravity preview. The cross-platform unifications (matter-wave Q-C boundary ↔ qubit-system multiplicity wall via shared $\mathcal{M}_\mathrm{crit}$; $\Gamma_\mathrm{cross}$ collapse across BH-2 and QC condition (ii); P04 mobility-capacity bound across UDM and Class A QC; V1 across kernel-arrow, R1, YM mass-gap, and BH motif alphabet) are surveyed here.
- **`papers/ED_One_Substrate_Three_Domains/`** — Program-overview / cross-domain context paper. Used in Chapter 14 to situate the cross-platform unifications within the program's three-domain organization.

### Chapter 15 — Public Test Inventory and Open Extensions

- **`Desktop/ED_Public_Test_Inventory.md`** — Living test catalog. Records the status taxonomy (PASSED / ANCHORED / IN PROGRESS / ACTIVE / OPEN) uniformly across sectors, with three PASSED predictions, thirteen ANCHORED predictions, three IN PROGRESS predictions, seventeen ACTIVE predictions, and four OPEN predictions.
- **`docs/Investigation_Priority_List.md`** — Active priority list with open extensions. Records the current "what to work on next" priority list (twenty-three numbered items, easiest-to-hardest, with closed items archived).
- **Various ED-I interpretation papers** — Sector-specific prediction sources. Each ED-I paper supplies the substrate-level reading for one sector and contributes the sector-specific predictions in the public test inventory.

---

## C.7 Cross-Reference: ED-I Interpretation Papers

The ED-I (Event Density Interpretation) paper series supplies sector-specific substrate-level readings used across the monograph. Each ED-I paper is assigned to its primary chapter; many are referenced in additional chapters. The list below records the assignments named in Sections C.2–C.6 plus the additional ED-I papers appearing in the program's interpretation-paper inventory and used as supporting references.

- **ED-I-01 (Superconductivity)** → Chapter 2.
- **ED-I-06 (Fields and Forces in Event Density)** → Chapter 2 (also load-bearing in Chapter 8).
- **ED-I-12 (Photonics)** → Chapter 7.
- **ED-I-13 (Quantum Information: Channel Geometry)** → Chapter 6.
- **ED-I-14 (Topological Effects)** → Chapter 7.
- **ED-I-18 (Multi-Timescale Photonics)** → Chapter 7.
- **ED-I-23 (Josephson Junctions)** → Chapter 2.
- **ED-I-29 (Tunneling)** → Chapter 2.

Additional ED-I papers in the program interpret sectors not load-bearing in any monograph chapter; they appear in Chapter 15's prediction inventory through specific predictions but are not assigned as load-bearing to any chapter here.

---

## C.8 Cross-Reference: Arc Memos and Closure Documents

The program's structural derivations are organized into named arcs, each consisting of multiple sequential memos. Each arc is assigned here to its primary chapter alongside the publication-grade paper(s) that consolidate its content.

- **Arc B (Kernel-Arrow / V1 closure)** → Chapter 4. Memos in `arcs/arc-B/`.
- **Arc D (DCGT)** → Chapter 3. Memos in `theory/Arc_D/`. Six-memo arc producing the Diffusion Coarse-Graining Theorem.
- **Arc Q (Gauge-Field-as-Rule-Type)** → Chapter 6. Memos in `papers/Arc_Q/`.
- **Arc R (Substrate UV Finiteness)** → Chapter 6. Memos in `papers/Arc_R/`.
- **Arc Q-COMPUTE** → Chapter 7. Seven-memo arc in `theory/Quantum_Computing/`. Closed 2026-05-02.
- **Arc NS (Navier–Stokes)** → Chapter 8. Multiple sub-arcs: NS-1, NS-2, NS-3 / NS-Smoothness, NS-Turb, P4-NN, NS-Q. Memos in `theory/Navier Stokes/`.
- **Arc YM (Yang–Mills)** → Chapter 9. Six-memo arc in `theory/Yang_Mills/`. Closed 2026-04-30.
- **Arc SG (Substrate Gravity Extension)** → Chapter 11. Six-memo arc in `theory/Substrate_Gravity/`. Closed 2026-04-30.
- **Arc ED-10 (Curvature Emergence)** → Chapter 12. Six-memo arc in `theory/Substrate_Gravity/`. Closed 2026-04-30.
- **Arc BH (Black Holes)** → Chapter 13. Seven-memo arc (BH-1 through BH-7) in `theory/Black_Holes/`. Closed 2026-05-01.

---

## C.9 Dependency Section

Appendix C respects the chapter dependency graph. Each chapter assignment cites only papers whose content does not invoke results from later chapters: a paper assigned to Chapter $X$ may use any earlier chapter's content, but does not depend structurally on a chapter $Y > X$. In the few cases where a paper's derivation references a downstream result (e.g. the NS Synthesis Paper main text references DCGT, which is canonically derived in Appendix D of the same paper), the dependency is internal to the paper and respects the chapter ordering: NS Synthesis Paper Appendix D is assigned to Chapter 3 (DCGT), which precedes Chapter 8 (NS main).

The cross-reference is consistent with Appendix A: every theorem-source path in Appendix A appears here under its chapter. It is consistent with Appendix B: the canonical definition of every glossary symbol lives in a paper assigned to a chapter here. It is consistent with Appendix D: every substrate constant in Appendix D has its derivation or empirical anchor in a paper assigned here.

---

## C.10 Canonical Sources (Aggregated)

The following repository paths appear in this appendix; their full inventory is consolidated here for ease of navigation.

**`papers/` cluster:**
- `papers/Event_Density_Ontology_and_Axioms/`
- `papers/Foundations_of_Event_Density/`
- `papers/ED_One_Substrate_Three_Domains/`
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
- `papers/Arc_Q/`
- `papers/Arc_R/`
- `papers/Quantum_Computing_Foundations/`
- `papers/Navier Stokes_Synthesis_Paper/` (main + Appendices C, D, E)
- `papers/Universal_Mobility_Law/`
- `papers/P4_NonNewtonian_Paper_Draft/`
- `papers/Substrate_Gravity_Foundations/Substrate_Gravity_Foundations_Paper.{md,tex,pdf}`
- `papers/Substrate_Gravity_Foundations/ED_substrate_gravity_foundations_2026-04-28.{md,tex,pdf}`
- `papers/Black_Hole_Foundations/`
- `papers/ED_QFT_Overview/`

**`theory/` cluster:**
- `theory/Arc_D/`
- `theory/Quantum_Computing/`
- `theory/Navier Stokes/`
- `theory/Yang_Mills/`
- `theory/Substrate_Gravity/`
- `theory/Black_Holes/`

**`arcs/` cluster:**
- `arcs/arc-B/`

**`docs/` and orientation:**
- `Desktop/ED_Public_Test_Inventory.md`
- `docs/Investigation_Priority_List.md`

---

## C.11 Optional Figures

The following tables and diagrams are described for inclusion in the final monograph:

- **Table C.1 — Paper-to-chapter assignment matrix.** Rows: every publication-grade paper in the program. Columns: chapters 1–15. Each row has exactly one filled cell (the chapter the paper is assigned to). Used to verify completeness of the cross-reference and prevent paper-orphaning.
- **Table C.2 — ED-I interpretation paper inventory.** Rows: ED-I papers (numbered 01 through 29). Columns: primary chapter + secondary chapters + sectorial role. Records the full ED-I inventory and the interpretation-layer mapping into the chapter structure.
- **Figure C.1 — Arc dependency graph.** Directed acyclic graph of arc closures: Arc B → T18 + N1; Arc D → DCGT; Arc Q → T17; Arc Q-COMPUTE → UR-1 + $M$; Arc NS → NS Synthesis; Arc YM → YM Synthesis; Arc SG → Substrate Gravity Foundations; Arc ED-10 → Curvature Emergence; Arc BH → BH Foundations. Edges encode "feeds into." Used to visualize how the arc-closure pipeline produces the publication-grade papers assigned in this appendix.
- **Table C.3 — Repository-cluster summary.** Three rows (papers/, theory/, arcs/) with column counts of items per chapter. Used to verify that every chapter has at least one publication-grade source and at least one supporting arc/theory reference where applicable.
