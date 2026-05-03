# Appendix B — Notation Glossary

## B.1 Appendix Overview

This appendix collects every symbol used across the monograph with a unified, self-consistent definition. Definitions are stated in the form they carry in the chapters and in the canonical source papers; nothing in this appendix introduces new notation, redefines an existing symbol, or shifts a definition relative to the source-paper canon. Where a quantity is form-FORCED (its functional shape is derived from substrate primitives) but value-INHERITED (its absolute scale or threshold inherits from substrate constants whose closed form is downstream work), the entry flags this explicitly.

The glossary is grouped by structural role: substrate quantities and primitives; length and time scales; substrate constants and coupling parameters; UR-1 thresholds and functional shapes; the multiplicity-cap function and architectural-class objects; substrate-gravity quantities; black-hole quantities; and soft-matter mobility. Symbols not in this glossary do not appear in the monograph. Symbols that appear in the monograph but whose canonical definition lives in a source paper carry a pointer to that paper.

---

## B.2 Substrate Quantities and Primitives

### $\rho$ — Local participation density

The substrate-level participation density: a scalar field on the substrate that records, at each substrate-scale region, the local rate at which participation events register. The fundamental coarse-graining target of canonical-ED dynamics. All continuum density-like quantities (mass density, charge density, fluid density) emerge as coarse-grained projections of $\rho$ through DCGT.

### $\nabla\rho$ — Participation density gradient

The substrate-scale gradient of $\rho$. The gradient sources the cross-bandwidth $\Gamma_\mathrm{cross}$ between adjacent regions and underwrites the directional viscosity and mobility-suppression structure across the program.

### $\sigma = |\nabla\rho|\,\ell_P^2/\rho_\mathrm{local}$ — Substrate-scale gradient sparsity

A dimensionless local quantity built from $|\nabla\rho|$, the substrate length scale $\ell_P^2$, and the local participation density. Sparsity $\sigma$ controls the suppression of cross-bandwidth via $\Gamma_\mathrm{cross}\sim\exp[-\alpha\sigma]$. Form-FORCED dimensionless combination.

### $\Gamma_\mathrm{cross}$ — Substrate-mediated cross-bandwidth

The cross-bandwidth between adjacent substrate regions that mediates participation-rule rule-spanning connectivity. Form-FORCED as $\Gamma_\mathrm{cross}\sim\exp[-\alpha\sigma]$ via DCGT; its absolute scale is value-INHERITED.

### $\mathcal{M}$ — Multiplicity

The count of viable distinct ED-gradient pathways through a substrate region, where "viable" is determined by the substrate participation rules. The ED analogue of entropy: high $\mathcal{M}$ corresponds to many indistinguishable substrate routes for participation, low $\mathcal{M}$ to few. Multiplicity is a load-bearing invariant of the program: it controls the unresolved-rule regime (UR-1 condition i), the QC architectural-class taxonomy (A is engineered-low-$\mathcal{M}$; B is global-geometric $\mathcal{M}$ via topological rigidity; C is high-$\mathcal{M}$ via redundancy), the entropy coefficient in BH area law, and the matter-wave Q-C boundary.

### $\mathcal{U}(\mathcal{S},t) \in [0,1]$ — Participation-rule unresolvedness

The unresolvedness functional across designated endpoints of a substrate region $\mathcal{S}$ at time $t$. Form-FORCED three-factor product:
```math
\mathcal{U}(\mathcal{S},t) = \mu(\mathcal{M}/\mathcal{M}_\mathrm{crit}) \cdot \kappa(\Gamma_\mathrm{cross}/\Gamma_\mathrm{min}) \cdot \exp\!\Big(-\!\!\int_0^t \Lambda(s)\,ds\Big).
```
Each factor corresponds to one of the three independently necessary UR-1 conditions.

### $\Lambda$ — Local commitment-injection rate

The substrate-level rate at which commitments (irreversible participation recordings) are injected into a region. Decomposes as $\Lambda = \Lambda_\mathrm{env} + \Lambda_\mathrm{int}$ — environmental and intrinsic contributions. Governs the commitment-survival exponential factor in $\mathcal{U}$.

### V1, V5 — Finite-width vacuum kernel and cross-chain memory kernel

V1 is the finite-width vacuum response kernel of Theorem N1, the substrate-level temporal-smearing kernel mediating effective-vacuum participation. V5 is the cross-chain memory kernel mediating substrate-level memory between chains; its first temporal moment yields the Maxwell viscoelastic relaxation time $\tau_R$ via DCGT.

### P1–P13 — The thirteen substrate primitives

The irreducible substrate commitments. Notably P01 (event discreteness), P02 (chain worldline), P04 (bandwidth update), P11 (commitment-irreversibility), P13 (proper-time ordering); seven additional primitives covering participation, multiplicity, finite kernels, and substrate-locality conditions. Canonical inventory in `papers/Event_Density_Ontology_and_Axioms/`.

### R1 — Substrate-cutoff hyperviscous regularization

The continuum hyperviscous term
```math
-\kappa\,\mu_\mathrm{V1}\,\ell_P^2\,\nabla^4\mathbf{v},
```
inherited from V1's finite width through DCGT. R1 underwrites the substrate-cutoff regularization of Navier–Stokes-class equations and the form-level mass-gap mechanism for Yang–Mills.

---

## B.3 Length and Time Scales

### $\ell_P$ — Planck length

The substrate length scale, derived to coincide with the Planck length via T19's identification. Sets the units in which $\sigma$, $A/\ell_P^2$, $\beta_\mathrm{crit}$, and the R1 prefactor are expressed.

### $R_\mathrm{cg}$ — Coarse-graining length scale

The coarse-graining radius of DCGT. Lies in the hydrodynamic window $\ell_P \ll R_\mathrm{cg} \ll L_\mathrm{flow}$. The DCGT multi-scale expansion proceeds at $R_\mathrm{cg}$.

### $L_\mathrm{flow}$ — Continuum-flow length scale

The length scale of the emergent continuum dynamics. The upper bound of the hydrodynamic window. Relative ordering $\ell_P \ll R_\mathrm{cg} \ll L_\mathrm{flow}$ is a substantive scale-separation condition that DCGT requires.

### $\tau_\mathrm{QC}$ — QC operating window

The minimum of the three UR-1 condition-failure timescales. Defines the maximum coherent-computation duration available in any architectural class:
```math
\tau_\mathrm{QC} = \min(\tau_{(\mathrm{i})}, \tau_{(\mathrm{ii})}, \tau_{(\mathrm{iii})}).
```

### $\tau_{(\mathrm{i})}, \tau_{(\mathrm{ii})}, \tau_{(\mathrm{iii})}$ — UR-1 condition-failure timescales

The three independent timescales on which UR-1 conditions (i)/(ii)/(iii) fail respectively. Each timescale is class-dependent: Class A is dominated by $\tau_{(\mathrm{iii})}$; Class B by $\tau_{(\mathrm{i})}$; Class C by $\tau_{(\mathrm{ii})}$.

---

## B.4 Substrate Constants and Coupling Parameters

### $\hbar$ — Planck's constant

Substrate input. Sets the absolute scale of canonical-conjugate uncertainty bounds and enters T19's identification of $G$.

### $c$ — Speed of light

Substrate input. The substrate-propagation speed for participation-rule connectivity and the asymptotic causal-cone speed for V1 retardation.

### $H_0$ — Hubble rate

Substrate input. Sets the cosmic-horizon participation density scale in T20.

### $G$ — Gravitational constant (DERIVED)

Form-FORCED + value-DERIVED:
```math
G = \frac{c^3\,\ell_P^2}{\hbar}.
```
Source: T19. Not a substrate input.

### $a_0$ — MOND transition acceleration (DERIVED)

Form-FORCED + value-DERIVED:
```math
a_0 = \frac{c\,H_0}{2\pi}.
```
Source: T20. The factor $2\pi$ is the azimuthal period of the leading anisotropic projection mode.

### $\alpha$ — DCGT prefactor

The form-FORCED, value-INHERITED prefactor in the cross-bandwidth structure $\Gamma_\mathrm{cross}\sim\exp[-\alpha\sigma]$. Its closed form is downstream work in the substrate-constants program.

### $\beta$ — Universal Mobility Law mobility exponent

The exponent in the Universal Mobility Law $M(\rho) \propto (1 - \rho/\rho_\mathrm{max})^\beta$. Canonical form-FORCED value 2 (substrate prediction); empirical anchor $\beta \approx 1.72 \pm 0.37$ across ten systems (PASSED). Discrepancy from canonical 2 is the program's anchored prediction of the closed-form correction route.

---

## B.5 UR-1 Thresholds (INHERITED)

The following thresholds are form-FORCED to exist (UR-1 establishes their existence and structural role) but value-INHERITED (their closed-form expressions in substrate constants are downstream work).

### $\mathcal{M}_\mathrm{crit}$ — Critical multiplicity threshold

Above this multiplicity, the unresolved-rule regime fails: the substrate region cannot sustain coherent rule-spanning. Underwrites both the matter-wave Q-C boundary (140–250 kDa, projected) and the qubit-system multiplicity wall — the same substrate object via two-point Q-C mass extrapolation. O-QC-1 in the closed-form-substrate-constants program.

### $\Gamma_\mathrm{min}$ — Minimum cross-bandwidth

The minimum $\Gamma_\mathrm{cross}$ below which cross-endpoint connectivity fails. Class C correlation-budget plateau is set by $\Gamma_\mathrm{min}$.

### $\Lambda_\mathrm{V1}$ — V1 vacuum residual injection rate

The irreducible commitment-injection rate from the V1 vacuum kernel itself, present even in perfect environmental isolation. Class A's perfect-isolation ceiling: a Class A device cannot lower $\Lambda$ below $\Lambda_\mathrm{V1}$ regardless of engineering effort.

### $\beta_\mathrm{crit} \sim \log(R_\mathrm{cg}/\ell_P)$ — Critical gradient threshold

The critical sparsity threshold for decoupling-surface formation in the BH program. Form-FORCED logarithmic dependence on the scale ratio.

### $N_\mathrm{corr}$ — Correlation budget

The maximum number of correlated substrate channels available before Class C redundancy saturates. Class C correlation-budget plateau is governed by $N_\mathrm{corr}$.

### $\Delta_\mathrm{top}$ — Topological gap

The protective gap separating topologically distinct ground states in Class B. Closes at gap-suppression rate $\sim e^{-\#}$ in the topology-perturbation regime.

### $T_\mathrm{eff}$ — Substrate-equivalent perturbation temperature

The substrate-level effective temperature corresponding to environmental perturbations. Enters Class A and Class B failure routes through thermal commitment-injection.

---

## B.6 UR-1 Functional Shapes (Form-FORCED, Shape INHERITED)

The unresolvedness three-factor product contains two named factor functions whose form is FORCED (monotonicity, range) and whose specific shape is INHERITED.

### $\mu(x)$ — Multiplicity-headroom factor

Monotone-decreasing from $\mu(0)=1$ to $\mu(\infty)=0$. Form-FORCED. Its closed form is downstream work.

### $\kappa(x)$ — Rule-spanning connectivity factor

Monotone-increasing from $\kappa(0)=0$ to $\kappa(\infty)=1$. Form-FORCED. Its closed form is downstream work.

### $g(N), h(N), c(N)$ — Class C redundancy modifier functions

The Class C scaling functions for redundancy, hybridization, and correlation respectively. Form-FORCED in the Class-C projection of $M$; specific shapes are downstream work.

---

## B.7 Multiplicity-Cap Function and Architectural Classes

### $M(\mathcal{S}, K, \mathcal{E}, \mathcal{O})$ — Multiplicity-cap function

The single substrate object capping multiplicity in any QC architecture. Three architectural-class projections (A/B/C) plus meta-architectural overlays $\mathcal{O}$. The unification of multiplicity-cap behavior across all engineered QC platforms into one substrate function is the load-bearing structural result of Arc Q-COMPUTE.

### $K \in \{A, B, C\}$ — Architectural class

A: engineered-low-multiplicity (e.g. SC qubits, trapped ions). B: global-geometric-rigidity (e.g. topological qubits). C: high-multiplicity-redundancy (e.g. error-correcting codes, ensemble averaging). Form-FORCED three-class exhaustiveness via UR-1.

### $\mathcal{O}$ — Meta-architectural overlay

Compositions of the three architectural classes: error correction, dynamical decoupling, reservoir engineering, hybrids. Not new classes; compositions.

### $\mathcal{S}$ — Substrate-region system input

The substrate-region characterization of the QC system itself.

### $\mathcal{E}$ — Environment input

The substrate-region characterization of the QC system's environment.

### $\mathcal{M}_\mathrm{floor}, \gamma_\mathrm{floor}$ — Architectural floors

The architecturally-imposed lower bounds on multiplicity and connectivity respectively that a given architectural class can achieve.

### $A_S$ — Architectural restoring rate

The class-dependent rate at which the architecture restores conditions (i)/(ii)/(iii) after perturbation.

### $f_\mathrm{int}, f_\mathrm{xy}, f_\mathrm{sys}^{(A)}$ — Architecture-specific scaling functions

Dimensionless scaling functions in the multiplicity-cap projection for each architectural class.

---

## B.8 Substrate-Gravity Quantities

### $\Phi$ — Gravitational potential

The substrate-derived gravitational potential in flat-background substrate gravity. Satisfies the modified Poisson equation
```math
\nabla\cdot\big[\mu(|\nabla\Phi|/a_0)\,\nabla\Phi\big] = 4\pi G\,\rho_m.
```

### $\mu(|\nabla\Phi|/a_0)$ — Interpolation function

The interpolation function in the substrate-gravity modified Poisson equation. Form-FORCED to match Newtonian asymptote at $|\nabla\Phi|\gg a_0$ and deep-MOND asymptote at $|\nabla\Phi|\ll a_0$. Note: this $\mu$ is a different object from the UR-1 multiplicity-headroom factor $\mu(x)$; the symbol is shared by convention with the source papers.

### $g_{\mu\nu}^\mathrm{ac}$ — Acoustic metric

The kinematic-summary metric of substrate participation density in Arc ED-10. Not the Einstein metric; an acoustic-metric construction underwriting the covariantized scalar-tensor structure.

### $T$ — Trace of matter stress-energy

The trace appearing in the covariantized substrate-gravity equation
```math
\nabla_\mu\big[\mu(\sqrt{g^{\alpha\beta}\nabla_\alpha\Phi\nabla_\beta\Phi}/a_0)\,\nabla^\mu\Phi\big] = 4\pi G\,T.
```

### $v_\mathrm{flat}$ — Asymptotic flat-rotation-curve speed

The rotational speed in the asymptotic deep-MOND regime, related to baryonic mass by T21's $v^4 = G\,M_b\,a_0$.

### $M_b$ — Baryonic mass

The total baryonic mass of a galactic system, the variable on the right side of the BTFR slope-4 relation.

---

## B.9 Black-Hole Quantities

### $\Sigma_H$ — Decoupling surface

The substrate-level horizon: the surface across which substrate participation rule-connectivity is severed. The substrate-level analogue of an event horizon, but defined kinematically without invoking an Einstein metric.

### $A$ — Coarse-grained acoustic-metric area of $\Sigma_H$

The area of the decoupling surface in the coarse-grained acoustic-metric units. Enters the area law with prefactor $\ell_P^{-2}\log g$.

### $S$ — Black-hole entropy

Form-FORCED area law:
```math
S = \frac{A}{\ell_P^2}\,\log g.
```
The form is FORCED; the coefficient $\log g$ is value-INHERITED, with $\log g \approx 1/4$ corresponding to the Bekenstein–Hawking match.

### $\log g$ — Entropy coefficient

The INHERITED coefficient in the area law. O-2 in the closed-form-substrate-constants program.

### $\delta_{\ell m}$ — BHPT phase shift

The black-hole perturbation-theory phase shift, a global path-integrated invariant in the BH scattering structure.

### $\Delta\mathcal{A}$ — Channel action density excess

The action-density excess along a perturbation channel's substrate trajectory near $\Sigma_H$.

### $\Delta\phi_\mathrm{twist}$ — Kerr-twist accumulated frame-dragging vorticity

The accumulated frame-dragging vorticity along a path in the Kerr extension of the BH architecture.

### $\omega_\mathrm{FD}$ — Local frame-dragging angular velocity

The local angular velocity of frame-dragging at a substrate point in the rotating BH.

### $\mathcal{T}$ — Topological structure label

The label distinguishing topological structures in the Class B QC and the BH motif alphabet.

### $T_H$ — Hawking temperature

```math
T_H = \frac{\kappa}{2\pi},
```
where $\kappa$ is surface gravity. The structural form FORCED; closed-form spectrum is the B4 open-extension target.

### $\tau_\mathrm{gap-stab}(\mathcal{T})$ — Class B topology-perturbation rate

The rate at which the topological gap $\Delta_\mathrm{top}$ closes for topology label $\mathcal{T}$ under perturbation. Class B exponential gap-suppression prediction is governed by $\tau_\mathrm{gap-stab}$.

---

## B.10 Soft-Matter Mobility

### $M(\rho)$ — Mobility (Universal Mobility Law)

Form-FORCED power law:
```math
M(\rho) = M_0\,\big(1 - \rho/\rho_\mathrm{max}\big)^\beta,
```
with canonical $\beta = 2$ (substrate prediction) and empirical $\beta \approx 1.72 \pm 0.37$ across ten systems (PASSED). Note: this $M$ is a different object from the multiplicity-cap function $M(\mathcal{S}, K, \mathcal{E}, \mathcal{O})$; the symbol is shared by convention with the source papers.

### $\rho_\mathrm{max}$ — Packing limit

The maximum participation density at which mobility vanishes in UDM.

### $\tau_R$ — Maxwell viscoelastic relaxation time

The first temporal moment of the V5 cross-chain memory kernel under DCGT, identified with the Maxwell viscoelastic relaxation time of the emergent continuum.

---

## B.11 Convention Notes

### Symbol re-use across sectors

Three symbols are re-used by convention in different sectors:

- **$\mu$**: appears as (i) the UR-1 multiplicity-headroom factor $\mu(x)$, (ii) the substrate-gravity interpolation function $\mu(|\nabla\Phi|/a_0)$, and (iii) the V1-amplitude prefactor $\mu_\mathrm{V1}$ in R1. Context disambiguates; sectorial reuse follows the source-paper canon.
- **$M$**: appears as (i) the multiplicity-cap function $M(\mathcal{S}, K, \mathcal{E}, \mathcal{O})$, (ii) the soft-matter mobility $M(\rho)$, and (iii) the baryonic mass $M_b$. Context disambiguates.
- **$\kappa$**: appears as (i) the UR-1 connectivity factor $\kappa(x)$, (ii) the BH surface gravity $\kappa$ in $T_H = \kappa/(2\pi)$, and (iii) the R1 prefactor $\kappa$ in $-\kappa\mu_\mathrm{V1}\ell_P^2\nabla^4\mathbf{v}$. Context disambiguates.

### Form-FORCED / Value-INHERITED Tagging

The glossary tags every entry whose value is INHERITED rather than DERIVED. Form-FORCED structural quantities ($\mathcal{M}_\mathrm{crit}$, $\Gamma_\mathrm{min}$, $\log g$, $\beta$ canonical 2) are flagged as INHERITED when their closed-form expressions are downstream work; FORCED-and-DERIVED quantities ($G$, $a_0$, $T_H$ functional form) are flagged accordingly.

### Repository Path Convention

Source paths use `papers/...`, `theory/...`, and `arcs/...` exactly as in the chapter sources, with no prefix path component beyond the repository root `event-density/`.

---

## B.12 Dependency Section

Appendix B is consistent with Appendix A (theorem provenance map): every symbol used in a theorem statement in Appendix A is defined in Appendix B. It is consistent with Appendix C (paper-to-chapter cross-reference): every symbol in this glossary is used in at least one chapter, and the canonical definition of every symbol lives in a paper assigned to a chapter in Appendix C. It is consistent with Appendix D (substrate constants): every substrate constant defined in Appendix D ($c$, $\hbar$, $H_0$, $\ell_P$, $G$, $a_0$, $\alpha$, $\beta$, the UR-1 thresholds, $\log g$) appears here with the same definition.

The glossary inherits the substrate-primitive layer (Chapter 1), the load-bearing-invariants layer (Chapter 2), the DCGT layer (Chapter 3), and the kernel-arrow layer (Chapter 4). Symbols whose canonical definitions live in source papers point to those papers via the entries in Appendix C.

---

## B.13 Canonical Sources

- `papers/Event_Density_Ontology_and_Axioms/`
- `papers/Foundations_of_Event_Density/`
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
- `papers/Navier Stokes_Synthesis_Paper/` (main + Appendices C/D/E)
- `papers/Quantum_Computing_Foundations/`
- `papers/Black_Hole_Foundations/`
- `papers/Universal_Mobility_Law/`
- `papers/P4_NonNewtonian_Paper_Draft/`
- `papers/ED_QFT_Overview/`
- `theory/Arc_D/` (DCGT memos)
- `theory/Quantum_Computing/` (Arc Q-COMPUTE memos)
- `theory/Substrate_Gravity/` (substrate-gravity arc memos)
- `theory/Black_Holes/` (Arc BH memos)
- `theory/Yang_Mills/` (Yang–Mills arc memos)
- `arcs/arc-B/` (Arc B closure memos)

---

## B.14 Optional Figures

The following tables and diagrams are described for inclusion in the final monograph:

- **Table B.1 — Symbol-by-section incidence.** Rows: symbols. Columns: chapters 1–15. Filled cells indicate "used as load-bearing." Used to verify glossary completeness and chapter-by-chapter consistency.
- **Table B.2 — Form-FORCED / Value-INHERITED tagging.** Two columns separating FORCED-structure entries from INHERITED-value entries. Highlights the closed-form-substrate-constants program targets ($\mathcal{M}_\mathrm{crit}$, $\log g$, $\alpha$, the UR-1 $\mu(x)$ and $\kappa(x)$ shapes).
- **Figure B.1 — Symbol-reuse map.** Diagram showing the three convention-reused symbols ($\mu$, $M$, $\kappa$) and which sector each instance belongs to. Used to disambiguate notation under sectorial context.
- **Table B.3 — Substrate-input vs derived-quantity inventory.** Two columns: substrate inputs ($\hbar$, $c$, $H_0$, $\ell_P$ at the program-level — note $\ell_P$ becomes derived under T19) versus derived quantities ($G$, $a_0$, $\Gamma_\mathrm{cross}$ form, $\mathcal{U}$ form, BTFR slope-4, area law form). Maps the FORCED/INHERITED tagging onto a clean substrate-input vs. derivation chart.
