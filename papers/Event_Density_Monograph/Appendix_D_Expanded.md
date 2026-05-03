# Appendix D — Substrate Constants and Inherited Values

## D.1 Appendix Overview

This appendix collects every substrate constant referenced across the monograph, with each entry recording four heads: the constant's structural role in the program, its substrate-input vs. derived-vs.-inherited status, its current numerical value (closed-form where derived, empirical anchor where inherited, dimensionless ratio where structurally fixed), and the chapter or chapters where it is load-bearing. The appendix is the program's accounting of what is fixed and what remains open at the level of dimensional and dimensionless constants.

The classification follows the form-FORCED / value-INHERITED methodology: substrate-input constants ($\hbar$, $c$, $H_0$, $\ell_P$) are taken as given; derived constants ($G$, $a_0$) are FORCED both in form and in value once the substrate inputs are fixed; inherited constants ($\mathcal{M}_\mathrm{crit}$, $\log g$, $\Lambda_\mathrm{V1}$, the UR-1 functional shapes, the architecture-specific scaling functions) are FORCED in their structural role but value-INHERITED until closed-form derivation is supplied by the substrate-constants program. Three INHERITED constants — $\mathcal{M}_\mathrm{crit}$ (O-QC-1), $\log g$ (O2 from Arc BH), and $\kappa/|\hat{N}'|$ (E4 from the ED-SC arc) — form a structurally-similar cluster that is the program's closed-form-substrate-constants program.

---

## D.2 Substrate Inputs (Taken as Given)

The four substrate-input constants are not derived within the monograph's nine sectors. They are the program's empirical anchors at the substrate level; every other constant in the monograph's nine sectors is either form-FORCED + value-DERIVED from these inputs, or form-FORCED + value-INHERITED.

### $\hbar$ — Planck's constant

**Structural role.** Sets the absolute scale of canonical-conjugate uncertainty bounds (Heisenberg's $\hbar/2$ in T1–T16); enters T19's identification of $G$.

**Status.** Substrate input.

**Value.** $\hbar = 1.054 \times 10^{-34}$ J·s (CODATA).

**Used in.** Chapter 5 (Phase-1 closure of QM); Chapter 11 (substrate gravity, via T19).

### $c$ — Speed of light

**Structural role.** The substrate-propagation speed for participation-rule connectivity; the asymptotic causal-cone speed for V1 retardation; enters T19 and T20 identifications.

**Status.** Substrate input.

**Value.** $c = 2.998 \times 10^8$ m/s (exact by SI definition).

**Used in.** Chapter 4 (kernel-arrow); Chapter 11 (substrate gravity, via T19 and T20); Chapter 12 (curvature emergence).

### $H_0$ — Hubble rate

**Structural role.** Sets the cosmic-horizon participation density scale in T20.

**Status.** Substrate input.

**Value.** $H_0 \in [67, 73]$ km/s/Mpc (Hubble tension band). The Hubble-tension band translates to roughly a 15% prediction band on $a_0$ via T20.

**Used in.** Chapter 11 (substrate gravity, via T20).

### $\ell_P$ — Planck length / substrate length scale

**Structural role.** The substrate length scale: governs the dimensionless gradient sparsity $\sigma = |\nabla\rho|\,\ell_P^2/\rho_\mathrm{local}$, the BH area law $S = (A/\ell_P^2)\log g$, the substrate-cutoff hyperviscous prefactor in R1 ($-\kappa\mu_\mathrm{V1}\ell_P^2\nabla^4\mathbf{v}$), and the critical gradient threshold $\beta_\mathrm{crit}\sim\log(R_\mathrm{cg}/\ell_P)$.

**Status.** Identified with the Planck length via T19 Newton-recovery (derived, not postulated). Listed as a substrate input in this section because no still-more-fundamental substrate input fixes it; T19 fixes it by requiring the derived form $G = c^3\ell_P^2/\hbar$ to recover the empirically observed $G$.

**Value.** $\ell_P = (G\hbar/c^3)^{1/2} \approx 1.616 \times 10^{-35}$ m.

**Used in.** Chapters 2, 3, 7, 8, 9, 11, 12, 13.

---

## D.3 Derived Substrate Constants (Form-FORCED, Value-DERIVED)

Two substrate constants are FORCED both in form and in value once the substrate inputs are fixed. The derivations live in the substrate-gravity foundations papers.

### $G$ — Newton's gravitational constant

**Structural role.** The proportionality constant in the inverse-square gravitational field. Enters every Newtonian-asymptote calculation in the substrate-gravity sector and the BTFR slope-4 relation.

**Status.** FORCED both in form (inverse-square) and in value (named combination of substrate inputs).

**Closed-form value.**
```math
G = \frac{c^3\,\ell_P^2}{\hbar} \approx 6.674 \times 10^{-11}\ \mathrm{m^3\,kg^{-1}\,s^{-2}}.
```

**Source.** T19, in `papers/Substrate_Gravity_Foundations/`.

**Used in.** Chapter 11; Chapter 12; Chapter 13.

### $a_0$ — MOND transition acceleration

**Structural role.** The deep-MOND-asymptote acceleration scale; the threshold below which the substrate-gravity interpolation function $\mu(|\nabla\Phi|/a_0)$ enters its deep-MOND limit; the proportionality constant in BTFR slope-4.

**Status.** FORCED both in form (cosmic-horizon dipole projection) and in value (named combination of substrate inputs).

**Closed-form value.**
```math
a_0 = \frac{c\,H_0}{2\pi} \approx 1.08 \times 10^{-10}\ \mathrm{m/s^2}.
```
Matches the empirical MOND acceleration $\approx 1.2 \times 10^{-10}$ m/s² to within roughly 10%, parameter-free. The Hubble-tension band $H_0 \in [67, 73]$ km/s/Mpc translates to a roughly 15% prediction band on $a_0$.

**Source.** T20, in `papers/Substrate_Gravity_Foundations/`.

**Used in.** Chapter 11; Chapter 12; Chapter 15.

---

## D.4 INHERITED Substrate Constants (Form-FORCED in Role; Specific Value Calibrated Empirically or Downstream)

The following constants are FORCED in their structural role by the substrate-level derivations of the program — they exist, they have specific dimensional or dimensionless types, and their qualitative behavior is fixed — but their specific numerical values are either calibrated against empirical anchors or remain downstream targets of the closed-form-substrate-constants program.

### $\mathcal{M}_\mathrm{crit}$ — Critical multiplicity threshold

**Structural role.** The critical multiplicity above which the unresolved-rule regime fails; underwrites both the matter-wave Q-C boundary and the qubit-system multiplicity wall via the same substrate object. Form-FORCED by UR-1 condition (i).

**Status.** INHERITED. Value-anchored empirically by the matter-wave Q-C boundary at 140–250 kDa molecular mass (two-point Q-C mass extrapolation).

**Closed-form derivation status.** OPEN. Designated **O-QC-1** in the closed-form-substrate-constants program.

**Used in.** Chapter 7 (QC architectural taxonomy); Chapter 14 (cross-platform unifications: matter-wave ↔ qubit identity).

### $\Gamma_\mathrm{min}$ — Minimum cross-bandwidth

**Structural role.** The minimum cross-bandwidth below which UR-1 condition (ii) fails; the threshold governing the Class C correlation-budget plateau and the BH decoupling-surface formation condition.

**Status.** INHERITED from V1-kernel + DCGT closed-form details.

**Used in.** Chapter 3 (DCGT); Chapter 7 (Class C correlation-budget plateau); Chapter 13 (decoupling-surface threshold).

### $\Lambda_\mathrm{V1}$ — V1 vacuum residual injection rate

**Structural role.** The irreducible commitment-injection rate from the V1 vacuum kernel itself, present even in perfect environmental isolation. Bounds Class A's perfect-isolation ceiling: a Class A device cannot lower $\Lambda$ below $\Lambda_\mathrm{V1}$ regardless of engineering effort.

**Status.** INHERITED.

**Used in.** Chapter 7 (Class A perfect-isolation ceiling).

### $\beta_\mathrm{crit} \sim \log(R_\mathrm{cg}/\ell_P)$ — Critical gradient threshold

**Structural role.** The critical sparsity threshold above which decoupling-surface formation becomes structurally favorable. Form-FORCED logarithmic dependence on the scale ratio $R_\mathrm{cg}/\ell_P$.

**Status.** INHERITED. Substrate-determined dimensionless number; precise prefactor depends on coarse-graining choices.

**Used in.** Chapter 7; Chapter 13.

### $N_\mathrm{corr}$ — Correlation budget for Class C platforms

**Structural role.** The maximum number of correlated substrate channels available before Class C redundancy saturates. Sets the Class C correlation-budget plateau.

**Status.** INHERITED from substrate-coupling pattern across redundant pathways; platform-specific.

**Used in.** Chapter 7.

### $\Delta_\mathrm{top}^{\max}$ — Maximum stable topological gap (Class B)

**Structural role.** The maximum topological gap that can be stably maintained against substrate-level perturbations in a Class B platform. Sets the upper bound on Class B coherent-computation duration.

**Status.** INHERITED from material/topology engineering. The Class B exponential gap-suppression prediction is governed by the rate at which $\Delta_\mathrm{top}$ closes under perturbation.

**Used in.** Chapter 7.

### $T_\mathrm{eff}^{\min}$ — Minimum substrate-equivalent perturbation temperature

**Structural role.** The minimum effective substrate-equivalent temperature that environmental engineering can achieve in a given platform. Enters Class A and Class B failure routes through thermal commitment-injection.

**Status.** INHERITED from environmental engineering.

**Used in.** Chapter 7.

### $\log g$ — Black-hole area-law entropy coefficient

**Structural role.** The coefficient in the form-FORCED BH area law $S = (A/\ell_P^2)\log g$. Determines the substrate-level analogue of the Bekenstein–Hawking $1/4$ coefficient.

**Status.** INHERITED from substrate motif counting. The empirical match $\log g \approx 1/4$ corresponds to $g \approx 1.28$, a non-integer substrate motif-count base.

**Closed-form derivation status.** OPEN. Designated **O2** in the Arc BH closed-form-substrate-constants targets.

**Used in.** Chapter 13.

### $\beta$ — Universal Mobility Law mobility exponent

**Structural role.** The exponent in $M(\rho) = M_0(1 - \rho/\rho_\mathrm{max})^\beta$. The form-FORCED canonical substrate prediction is $\beta = 2$.

**Status.** Empirical anchor: $\beta = 1.72 \pm 0.37$ across ten systems with mechanism-clustered scatter (PASSED). The discrepancy from canonical 2 anchors a closed-form correction route as downstream work.

**Used in.** Chapter 10; Chapter 15.

### $\kappa/|\hat{N}'| \approx 0.001766$ — ED-SC anchor (cross-scale invariance)

**Structural role.** The cross-scale invariance anchor of the ED-SC arc; central value 0.001766 with model band ±10.78%. Records the empirically-measured cross-scale invariance ratio.

**Status.** INHERITED from cross-scale invariance.

**Closed-form derivation status.** OPEN. Designated **E4** in the ED-SC arc.

**Used in.** Cross-reference: ED-SC arc work, not within this monograph's nine sectors but flagged here for completeness because it is one of three structurally-similar INHERITED constants in the closed-form-substrate-constants program.

---

## D.5 Class-Specific INHERITED Quantities

The following quantities are FORCED in their structural role by UR-1 and the multiplicity-cap function $M(\mathcal{S}, K, \mathcal{E}, \mathcal{O})$ projections, but their specific shapes or values are INHERITED from V1-kernel + DCGT details, from architecture-to-platform calibration, or from a topology-stability theorem still to be derived.

### $\mu(x), \kappa(x)$ — UR-1 functional shapes

**Structural role.** The multiplicity-headroom factor (monotone-decreasing from 1 to 0) and rule-spanning connectivity factor (monotone-increasing from 0 to 1) in the unresolvedness three-factor product. Form-FORCED to be monotone with specific limits.

**Status.** Specific shape (Boltzmann, rational, sigmoid, etc.) is INHERITED from V1-kernel + DCGT closed-form details.

**Used in.** Chapter 7.

### $g(N), h(N), c(N)$ — Class C redundancy modifier functions

**Structural role.** The Class C scaling functions for redundancy, hybridization, and correlation. Form-FORCED in the Class-C projection of $M$.

**Status.** Specific shapes INHERITED.

**Used in.** Chapter 7.

### $f_\mathrm{int}(M_\mathrm{mol}), f_\mathrm{xy}(N_\mathrm{qubits}), f_\mathrm{sys}^{(A)}(\mathcal{S})$ — Architecture-specific scaling functions

**Structural role.** Map system-size variables (molecular mass, qubit count, system-size descriptor) to effective multiplicity for each architectural class.

**Status.** INHERITED from architecture-to-platform calibration. Designated **O-QC-2** in the Q-COMPUTE open-extension list.

**Used in.** Chapter 7; Chapter 14.

### $\tau_\mathrm{gap-stab}(\mathcal{T})$ — Class B topology-perturbation rate

**Structural role.** The rate at which the topological gap $\Delta_\mathrm{top}$ closes for topology label $\mathcal{T}$ under perturbation. Underwrites the Class B exponential gap-suppression prediction.

**Status.** Form named; topology-stability theorem (designated **O-QC-4**) is the natural follow-on for substrate-level derivation.

**Used in.** Chapter 7.

---

## D.6 The Closed-Form-Substrate-Constants Program

Three INHERITED constants in the inventory above are structurally similar in character: each is dimensionless or has a specific dimensional form, each is empirically anchored, and each is the target of a closed-form derivation that the substrate-constants program treats as a priority.

| Constant | Sector | Open-extension label | Empirical anchor |
|---|---|---|---|
| $\mathcal{M}_\mathrm{crit}$ | QC (Chapter 7) | O-QC-1 | Matter-wave Q-C boundary at 140–250 kDa |
| $\log g$ | BH (Chapter 13) | O2 (Arc BH) | $\log g \approx 1/4$ Bekenstein–Hawking match |
| $\kappa/|\hat{N}'|$ | ED-SC (cross-reference) | E4 | $\approx 0.001766$ central; model band $\pm 10.78\%$ |

Closed-form derivation in any one of these constants constrains the others by the form-FORCED / value-INHERITED methodology's cross-domain consistency requirement: the program's three-domain organization (substrate / continuum / gravity) demands that any substrate-level closed-form derivation route must be expressible in substrate primitives that are themselves cross-domain. A closed-form derivation of $\mathcal{M}_\mathrm{crit}$ will use substrate-level multiplicity counting; the same multiplicity counting must be the substrate-level mechanism counting BH motifs that fixes $\log g$; and the same multiplicity counting must underwrite the cross-scale invariance ratio that fixes $\kappa/|\hat{N}'|$. The three constants are not mutually independent; they are three projections of the same closed-form-substrate-constants problem.

---

## D.7 Structural Roles Cross-Referenced by Sector

The substrate constants in this appendix support the following sectorial structures:

- **Quantum sector (Chapters 5–7).** $\hbar$ in T1–T16 uncertainty bounds; $\mathcal{M}_\mathrm{crit}$ in QC architectural taxonomy and matter-wave Q-C boundary; $\Gamma_\mathrm{min}$, $\Lambda_\mathrm{V1}$, $\beta_\mathrm{crit}$, $N_\mathrm{corr}$, $\Delta_\mathrm{top}^{\max}$, $T_\mathrm{eff}^{\min}$ in UR-1 condition-failure timescales and class-specific projections of $M$.
- **Continuum and dynamics (Chapters 8–10).** $\ell_P$ in the R1 substrate-cutoff hyperviscous prefactor; $\beta$ in the Universal Mobility Law; the V5-derived Maxwell relaxation time $\tau_R$ inheriting through DCGT.
- **Gravity sector (Chapters 11–13).** $c$, $\hbar$, $H_0$, $\ell_P$ as substrate inputs; $G$ and $a_0$ as derived; $\log g$ in the BH area-law coefficient.
- **Cross-platform and empirical synthesis (Chapters 14–15).** $\mathcal{M}_\mathrm{crit}$ unifying matter-wave Q-C and qubit-system multiplicity wall; $\Gamma_\mathrm{cross}$ collapse across BH-2 and QC condition (ii); $\beta$ as a PASSED empirical anchor; $a_0$ as the BTFR slope-4 anchor (PASSED).

---

## D.8 Form-FORCED / Value-INHERITED Tagging Summary

| Constant | Form-FORCED? | Value-DERIVED or INHERITED? |
|---|---|---|
| $\hbar$ | — | Substrate input |
| $c$ | — | Substrate input |
| $H_0$ | — | Substrate input |
| $\ell_P$ | — | Substrate input (also identified via T19 Newton-recovery) |
| $G$ | FORCED | DERIVED ($G = c^3\ell_P^2/\hbar$) |
| $a_0$ | FORCED | DERIVED ($a_0 = c\,H_0/(2\pi)$) |
| $\mathcal{M}_\mathrm{crit}$ | FORCED | INHERITED (O-QC-1 open) |
| $\Gamma_\mathrm{min}$ | FORCED | INHERITED |
| $\Lambda_\mathrm{V1}$ | FORCED | INHERITED |
| $\beta_\mathrm{crit}$ | FORCED (logarithmic shape) | INHERITED (prefactor) |
| $N_\mathrm{corr}$ | FORCED | INHERITED |
| $\Delta_\mathrm{top}^{\max}$ | FORCED | INHERITED |
| $T_\mathrm{eff}^{\min}$ | FORCED | INHERITED |
| $\log g$ | FORCED | INHERITED (O2 open) |
| $\beta$ | FORCED (canonical 2) | EMPIRICAL ANCHOR ($1.72\pm 0.37$, PASSED) |
| $\kappa/|\hat{N}'|$ | FORCED | INHERITED (E4 open) |
| $\mu(x), \kappa(x)$ | FORCED (monotone, limits) | INHERITED (specific shape) |
| $g(N), h(N), c(N)$ | FORCED | INHERITED |
| $f_\mathrm{int}, f_\mathrm{xy}, f_\mathrm{sys}^{(A)}$ | FORCED | INHERITED (O-QC-2) |
| $\tau_\mathrm{gap-stab}(\mathcal{T})$ | Form named | INHERITED (O-QC-4) |

---

## D.9 Dependency Section

Appendix D is consistent with Appendix A (theorem provenance map): the derivations of $G$ via T19 and $a_0$ via T20 appear in Appendix A under their respective theorems. It is consistent with Appendix B (notation glossary): every constant defined here has its symbol entry in Appendix B. It is consistent with Appendix C (paper-to-chapter cross-reference): every derivation or empirical anchor cited here lives in a paper assigned in Appendix C.

The substrate-input layer ($\hbar$, $c$, $H_0$, $\ell_P$) is upstream of every derivation in the monograph. The derived constants ($G$, $a_0$) are upstream of the substrate-gravity sector (Chapters 11–13) and of the BTFR-slope-4 prediction. The INHERITED constants are downstream of the sectorial derivations that establish their structural role, and upstream of empirical anchors and predictions in Chapter 15. The closed-form-substrate-constants program (O-QC-1, O2, E4) is the program's strategy for closing the INHERITED-value gap from below.

---

## D.10 Canonical Sources

- **Substrate inputs and T19 / T20 derivations:**
  - `papers/Substrate_Gravity_Foundations/Substrate_Gravity_Foundations_Paper.{md,tex,pdf}`
  - `papers/Substrate_Gravity_Foundations/ED_substrate_gravity_foundations_2026-04-28.{md,tex,pdf}`
- **UR-1 thresholds and Q-COMPUTE open-extension labels:**
  - `papers/Quantum_Computing_Foundations/`
  - Arc Q-COMPUTE memos in `theory/Quantum_Computing/`
- **BH area-law coefficient and O2:**
  - `papers/Black_Hole_Foundations/`
  - Arc BH memos in `theory/Black_Holes/`
- **Universal Mobility Law $\beta$ empirical anchor:**
  - `papers/Universal_Mobility_Law/`
  - `papers/P4_NonNewtonian_Paper_Draft/`
- **DCGT and V1/V5 closed-form details (governing $\Gamma_\mathrm{min}$, $\Lambda_\mathrm{V1}$, UR-1 functional shapes):**
  - `papers/Navier Stokes_Synthesis_Paper/` Appendix D (DCGT)
  - Arc D memos in `theory/Arc_D/`
  - Theorem N1 paper (V1 finite-width kernel)
- **ED-SC anchor and E4:**
  - ED-SC arc work (cross-reference; not within this monograph's nine sectors)

---

## D.11 Optional Figures

The following tables and diagrams are described for inclusion in the final monograph:

- **Table D.1 — Master substrate-constants inventory.** Rows: every constant in this appendix. Columns: structural role; status (substrate input / FORCED-DERIVED / FORCED-INHERITED / EMPIRICAL ANCHOR); current value; chapter(s) where load-bearing; closed-form derivation status / open-extension label. The complete tabular form of Sections D.2–D.5.
- **Table D.2 — Form-FORCED vs Value-INHERITED tagging summary.** The summary table reproduced from Section D.8.
- **Figure D.1 — Closed-form-substrate-constants program diagram.** Three nodes for $\mathcal{M}_\mathrm{crit}$, $\log g$, and $\kappa/|\hat{N}'|$, with their open-extension labels (O-QC-1, O2, E4) and empirical anchors. Edges indicate the cross-domain consistency requirement: closed-form derivation in any one constrains the others by substrate-level multiplicity counting.
- **Figure D.2 — Substrate-input-to-derived-constants dependency tree.** Root nodes: $\hbar$, $c$, $H_0$, $\ell_P$. First-level derived: $G$ (via T19), $a_0$ (via T20). Second-level relationships: BTFR slope-4 (via $G$ and $a_0$), area law (via $\ell_P$ and $\log g$ INHERITED), Heisenberg bound (via $\hbar$), R1 prefactor (via $\ell_P$). Visualizes the program's value-derivation structure end-to-end.
- **Table D.3 — Sectorial-incidence matrix.** Rows: constants. Columns: sectors (substrate ontology, load-bearing invariants, DCGT, kernel-arrow, QM, QFT, QC, NS, MHD, YM, soft-matter, substrate gravity, curvature, BH, cross-platform, public tests). Filled cells indicate "load-bearing." Used to verify that every constant has a sectorial home and every sector is grounded in the constants inventory.
