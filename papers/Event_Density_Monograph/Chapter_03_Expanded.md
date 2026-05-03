# Chapter 3 — The Coarse-Graining Bridge: DCGT, Hydrodynamic Window, Multi-Scale Expansion

## 3.1 Chapter Overview

The Diffusion Coarse-Graining Theorem (DCGT) is the substrate-to-continuum bridge for canonical-ED dynamical content. Its significance for the Event Density program is structural: *every* continuum theory developed in Parts II–IV — the Schrödinger equation in Phase-1 closure (Chapter 5), the gauge-field-as-rule-type structure of T17 (Chapter 6), the Navier–Stokes equation (Chapter 8), the Yang–Mills equation (Chapter 9), the Maxwell-class viscoelastic equation in soft matter (Chapter 10), the modified Poisson equation in substrate gravity (Chapter 11), the acoustic-metric scalar-tensor covariantization (Chapter 12), and the BH cross-bandwidth structure governing horizon formation (Chapter 13) — passes through DCGT or its non-Abelian generalization. Without DCGT the program would have substrate primitives on one side of a derivational gap and standard continuum physics on the other side, with no chain connecting them. With DCGT the chain is explicit and auditable.

This chapter establishes DCGT as a structural object: the hydrodynamic-window scale separation that makes the multi-scale expansion controlled, the form of the substrate-level cross-bandwidth structure $\Gamma_\mathrm{cross}(\mathbf{x}_1,\mathbf{x}_2) \sim \exp[-\alpha\int_\mathrm{path}\sigma\,d\ell]$ that recurs across multiple closed sectors, and the five leading-order coarse-grained consequences DCGT delivers: scalar diffusion, directional viscosity (the NS viscous sector), V1→R1 substrate-cutoff regularization, V5→Maxwell viscoelastic memory, and T17 minimal-coupling Lorentz force. The chapter does not derive the theorem from scratch — that derivation lives in the Arc D memos and in Appendix D of the NS Synthesis Paper. The chapter establishes what DCGT *is*, where it sits in the dependency graph, and how each subsequent chapter consumes its output.

## 3.2 The Substrate / Continuum Gap

### 3.2.1 What the gap is

Chapter 1 establishes that the substrate ontology consists of discrete events (P01) on chains (P02) with bounded bandwidth (P04), proper-time ordering (P13), commitment-irreversibility (P11), finite-width kernels (V1, V5), and substrate locality. Chapter 2 establishes the load-bearing invariants ($\mathcal{M}$, $\sigma$, $\Gamma_\mathrm{cross}$, V1, P11) that recur across the program. None of this content directly produces a continuum equation. A reader at the end of Chapter 2 has a substrate ontology and a vocabulary of substrate-state quantities, but the Schrödinger equation, Maxwell's equations, the Navier–Stokes equation, and Newton's law of gravitation are all continuum-level statements about smooth fields on smooth spacetime. They are not statements about substrate events.

The gap is therefore structural. The program needs a controlled, audited derivation that takes substrate primitives plus the load-bearing invariants of Chapter 2 and produces continuum equations as their leading-order coarse-grained consequences. DCGT is that derivation.

### 3.2.2 What standard physics does instead

Standard physics typically does not face this gap, because it does not commit to a substrate ontology in the first place. Quantum mechanics treats wavefunctions as fundamental, classical electromagnetism treats fields as fundamental, fluid dynamics treats velocity fields as fundamental, general relativity treats the spacetime metric as fundamental. Each framework starts at the continuum level and asks downward whether some deeper structure produces what is observed.

The Event Density program reverses the direction: it starts at the substrate level and asks upward whether the continuum equations of standard physics emerge as coarse-grained consequences. This requires a coarse-graining theorem that bridges the levels. DCGT is the program's answer to that requirement.

### 3.2.3 What DCGT must deliver

For DCGT to close the substrate/continuum gap, it must do four things:

1. Establish a controlled scale separation under which substrate dynamics admit a multi-scale expansion. (Section 3.3.)
2. Produce the substrate-level cross-bandwidth structure $\Gamma_\mathrm{cross}$ used throughout the program. (Section 3.4.)
3. Deliver leading-order coarse-grained continuum content covering at minimum scalar diffusion, directional viscosity, substrate-cutoff regularization, viscoelastic memory, and T17 minimal coupling. (Section 3.5.)
4. Generalize to the non-Abelian content needed for Yang–Mills (Chapter 9) and to the gradient-source content needed for substrate gravity (Chapter 11). (Section 3.7.)

DCGT delivers all four. The chapter establishes each in turn.

## 3.3 The Hydrodynamic Window

### 3.3.1 The scale separation

DCGT operates within a *hydrodynamic window* — a range of length scales between the substrate scale and the continuum-flow scale where substrate dynamics admit a controlled multi-scale expansion. The window is bounded below by the substrate's irreducible length scale $\ell_P$ (the Planck length, identified with the substrate length scale through T19 Newton-recovery in Chapter 11) and bounded above by the characteristic length scale $L_\mathrm{flow}$ of the continuum theory being derived. Within the window, the coarse-graining length scale $R_\mathrm{cg}$ provides a controlled intermediate scale at which substrate dynamics can be averaged without losing structural content:

```math
\ell_P \;\ll\; R_\mathrm{cg} \;\ll\; L_\mathrm{flow}.
```

The lower bound $\ell_P \ll R_\mathrm{cg}$ ensures that the coarse-graining cell at scale $R_\mathrm{cg}$ contains many substrate events, so averaging is statistically meaningful. The upper bound $R_\mathrm{cg} \ll L_\mathrm{flow}$ ensures that the coarse-grained cell is much smaller than the continuum flow scale, so the coarse-graining is local with respect to the continuum theory.

### 3.3.2 Why scale separation is required

Without the lower bound, the coarse-graining cell would be too small to average meaningfully — substrate events would dominate fluctuations, and the multi-scale expansion would have no controlled small parameter. Without the upper bound, the coarse-graining cell would be comparable to or larger than the continuum flow scale, and the resulting "continuum" content would be a global averaging rather than a local field theory.

The hydrodynamic window is therefore the structural prerequisite for DCGT to produce *local* continuum equations rather than global averages or substrate-noise-dominated content. Every continuum equation derived through DCGT in subsequent chapters relies on this window existing for the system being analyzed.

### 3.3.3 The window's substrate-level provenance

The lower bound $\ell_P$ is set by P01 event discreteness combined with the substrate length scale identified through T19. The upper bound $L_\mathrm{flow}$ is set by the system being analyzed — the continuum-flow scale of a fluid system, the qubit-system spatial extent in QC architecture, the galactic radius in substrate gravity, the black-hole horizon scale in BH architecture. The intermediate scale $R_\mathrm{cg}$ is a coarse-graining choice made within the window; results that pass through DCGT are required to be insensitive to the specific choice of $R_\mathrm{cg}$ within the window (the *coarse-graining-invariance condition*).

The hydrodynamic window therefore depends on (a) the substrate having a well-defined irreducible length (P01 + T19), and (b) the system being analyzed having a sufficiently large continuum-flow scale that scale separation actually exists. When both conditions hold, DCGT applies; when they do not, DCGT does not apply and the system is in a regime where substrate-level analysis cannot be coarse-grained to a clean continuum equation. The latter case occurs in the saturated participation zones of Chapter 13 (BH-3 interior) and at the matter-wave Q-C boundary of Chapter 7, where the substrate is precisely *outside* the hydrodynamic-window regime.

## 3.4 The Multi-Scale Expansion

### 3.4.1 Structure of the expansion

DCGT is a multi-scale expansion in the small parameter $\ell_P/R_\mathrm{cg}$ (or equivalently in the small parameter $R_\mathrm{cg}/L_\mathrm{flow}$, depending on which limit is being analyzed). Substrate quantities are expanded in powers of the small parameter, and at each order the coarse-grained content is collected to produce the leading-order continuum theory plus subleading corrections.

The leading-order content delivers the *standard* continuum equations — Newton's law of viscosity in NS, Maxwell's equations in MHD, the modified Poisson equation in substrate gravity, and so on. The first subleading correction delivers substrate-cutoff regularization terms, of which the canonical example is the R1 hyperviscous term $-\kappa\mu_\mathrm{V1}\ell_P^2 \nabla^4\mathbf{v}$ in NS (Chapter 8). The substrate-cutoff terms are small at ordinary continuum-flow scales — suppressed by powers of $\ell_P/R_\mathrm{cg}$ — but they are structurally inevitable consequences of the substrate's finite-width kernels.

### 3.4.2 What the expansion produces at each level

The multi-scale expansion's leading-order outputs are the canonical continuum equations of standard physics. The expansion's subleading outputs are substrate-cutoff corrections that are absent from standard physics but FORCED by the substrate ontology. The ordering structure:

```math
\begin{array}{l|l}
\text{Order} & \text{Content} \\
\hline
\text{Leading order } (\ell_P/R_\mathrm{cg})^0 & \text{Standard continuum equations} \\
\text{First subleading } (\ell_P/R_\mathrm{cg})^2 & \text{Substrate-cutoff regularization (R1, mass-gap, etc.)} \\
\text{Higher subleading} & \text{Increasingly small substrate-cutoff corrections} \\
\end{array}
```

This ordering is what makes DCGT both a derivation of standard physics (at leading order) and a source of substrate-level corrections that distinguish ED from purely phenomenological coarse-grainings (at first subleading order). The substrate-cutoff corrections are FORCED — they are not optional features the framework can drop without contradicting its substrate ontology.

### 3.4.3 The coarse-graining-invariance condition

DCGT's outputs at leading order are required to be insensitive to the specific choice of $R_\mathrm{cg}$ within the hydrodynamic window. This condition is the structural counterpart of renormalization-group invariance in standard QFT: the leading-order continuum content should not depend on the artificial scale at which the substrate is coarse-grained. The condition is satisfied automatically when the substrate-level dynamics admit a clean separation of scales; it can fail when scale separation is marginal, in which case the multi-scale expansion's small parameter is no longer small.

When the coarse-graining-invariance condition fails, the system is at the boundary of DCGT's applicability. This is the substrate-level reason the matter-wave Q-C boundary at 140–250 kDa molecular mass and the BH horizon at the threshold $\sigma \gtrsim \log(R_\mathrm{cg}/\ell_P)$ are *boundaries* rather than continuous extensions of the hydrodynamic-window regime: at these boundaries, DCGT's coarse-graining-invariance condition is precisely what breaks down, and the substrate must be analyzed without relying on a continuum approximation.

## 3.5 The Cross-Bandwidth Structure $\Gamma_\mathrm{cross}$

### 3.5.1 The central output

DCGT's most heavily-used output across the program is the substrate-level cross-bandwidth structure between two regions $\mathbf{x}_1$ and $\mathbf{x}_2$:

```math
\Gamma_\mathrm{cross}(\mathbf{x}_1, \mathbf{x}_2) \;\sim\; \exp\!\left[-\alpha\!\int_\mathrm{path}\sigma(\mathbf{x})\,d\ell\right],
```

where the integral runs along the substrate-locality-permitted pathway between $\mathbf{x}_1$ and $\mathbf{x}_2$, $\sigma$ is the substrate-scale gradient sparsity defined in Chapter 2, and $\alpha$ is a substrate-determined dimensionless prefactor (INHERITED).

The structure is form-FORCED. Its derivational origin: large $\sigma$ along the path between two regions creates a steep substrate-scale barrier that suppresses cross-region participation exchange exponentially. The exponential structure follows from the multi-scale expansion's small-parameter behavior; the integration along the path follows from substrate locality, which restricts cross-region participation to substrate-locality-permitted pathways rather than global state-of-the-universe couplings.

### 3.5.2 Why the form is structural rather than coincidental

The exponential structure is not a fitting choice. It is what the multi-scale expansion produces when applied to substrate dynamics with finite-width kernels and bounded bandwidth. The integrand $\sigma(\mathbf{x})$ along the path is the substrate's only path-local invariant of the right dimensional class; the prefactor $\alpha$ is the substrate's only path-local dimensionless coefficient that can multiply it. Any other functional form would require the multi-scale expansion to produce different leading-order behavior, which would in turn require different substrate primitives or different load-bearing invariants. The exponential-in-integrated-$\sigma$ form is therefore as inevitable as the substrate ontology from which it is derived.

### 3.5.3 The cross-domain echo

The same $\Gamma_\mathrm{cross}$ structure governs phenomena across enormously different scales:

- **Black-hole horizon formation (Chapter 13).** A horizon is the surface where $\Gamma_\mathrm{cross}$ across it falls below hydrodynamic-window resolution. Substrate gradients at gravitational-collapse scales (of order $10^{38}\,\ell_P$ for stellar-mass black holes) are integrated along radial paths through the horizon region.
- **Quantum-computing condition (ii) failure (Chapter 7).** UR-1's condition (ii) requires $\gamma_{ij} \geq \Gamma_\mathrm{min}$ along every rule-spanning pathway. Failure of this condition is the substrate-level cause of qubit decoherence in Class A architectures. Substrate gradients at engineered-system scales (of order $10^{-9}\,\mathrm{m}$ for Josephson-junction barriers) are integrated along path-engineered pathways.
- **Josephson-junction macroscopic quantum tunneling (Chapter 7).** MQT rate has the WKB-form exponential structure $\tau_\mathrm{MQT}^{-1} \sim \omega_0 \exp[-\alpha\int_\mathrm{barrier}\sigma\,d\ell]$, which is precisely the DCGT $\Gamma_\mathrm{cross}$ structure evaluated at the engineered-barrier $\sigma$-profile.

The same DCGT-derived exponential structure produces all three phenomena, at scales separated by approximately 50 orders of magnitude. The substrate does not distinguish between "gravitational" and "engineered" gradient regions when computing $\Gamma_\mathrm{cross}$; it applies the same DCGT machinery, and the empirical phenomena differ only in the platform-specific values of $\sigma$ along the relevant path. Chapter 14 develops this as the program's strongest cross-platform mechanism identity.

## 3.6 The Five Leading-Order Consequences

DCGT's leading-order multi-scale expansion delivers five canonical consequences that recur across the closed-arc inventory. Each is the substrate-to-continuum bridge for a specific continuum-physical content.

### 3.6.1 Scalar diffusion

The substrate's participation density $\rho$, coarse-grained over the hydrodynamic window, satisfies a diffusion equation at leading order. The diffusion coefficient is set by the participation-channel statistics of the underlying substrate, with a packing-class saturation as the participation density approaches the substrate's maximum sustainable value. The form is FORCED at leading order; the specific diffusion coefficient is INHERITED from substrate-channel statistics.

This diffusion content is the substrate-to-continuum bridge for soft-matter mobility (Chapter 10). The Universal Mobility Law $M(\rho) = M_0(1-\rho/\rho_\mathrm{max})^\beta$ is the form-FORCED packing-saturation behavior of substrate diffusion's leading-order coefficient.

### 3.6.2 Directional viscosity (the NS viscous sector)

When the scalar-diffusion content is extended from a scalar density to a vector velocity field, the DCGT multi-scale expansion produces Newton's law of viscosity at leading order. The viscous-diffusion term $\mu\nabla^2\mathbf{v}$ in the Navier–Stokes equation is FORCED at leading order by DCGT applied to vector-valued participation transport.

This is the substrate-to-continuum bridge for the viscous sector of Navier–Stokes (Chapter 8). The advective sector $(\mathbf{v}\cdot\nabla)\mathbf{v}$ is *not* DCGT-derived; it is a frame-kinematic artifact of writing fluid dynamics in laboratory-frame coordinates. The pressure and incompressibility terms are continuum-imposed constraints. Of the four kinds of structure in NS, two (viscous diffusion and the substrate-cutoff R1 below) are DCGT-derived; the other two are not.

### 3.6.3 V1 → R1 substrate-cutoff regularization

The V1 finite-width vacuum kernel produces, at first subleading order in the DCGT expansion, the hyperviscous correction term $-\kappa\mu_\mathrm{V1}\ell_P^2 \nabla^4\mathbf{v}$. This is the R1 substrate-cutoff term that supplies the Clay-NS-relevant regularizing mechanism in Chapter 8. The term is small at ordinary flow scales (suppressed by $\ell_P^2$) but it is structurally inevitable — V1's finite width is a primitive-level commitment, and DCGT's first subleading order produces R1 as a direct consequence.

R1 is the canonical example of a substrate-cutoff correction. Its mass-gap analogue in Yang–Mills (Chapter 9) and its cross-patch correlation analogue in BH area-law entropy (Chapter 13) are produced by the same V1-to-subleading-correction mechanism applied to different content channels.

### 3.6.4 V5 → Maxwell viscoelastic memory

The V5 cross-chain memory kernel, coarse-grained under DCGT, produces Maxwell-class viscoelastic dynamics:

```math
\tau_R\,\dot\sigma + \sigma = 2\mu S,
```

where $\tau_R$ is the relaxation time identified as the V5 kernel's first temporal moment, $\sigma$ is the stress tensor (here distinct from the substrate sparsity), $S$ is the strain-rate tensor, and $\mu$ is the viscosity. The form is FORCED by DCGT applied to V5's finite-width memory structure; the relaxation time $\tau_R$ is INHERITED from molecular physics in a soft-matter context (Chapter 10).

This is the substrate-to-continuum bridge for soft-matter viscoelasticity. Maxwell's spring-dashpot model, used phenomenologically in soft-matter rheology since the late nineteenth century, is reproduced from the substrate without phenomenological postulation.

### 3.6.5 T17 minimal coupling (Lorentz force)

T17 (Chapter 6) establishes gauge fields as participation measures of structural rule-types. The substrate-to-continuum bridge for the Lorentz force on charged particles is DCGT applied to charged-chain populations using T17's minimal-coupling structure. The Lorentz force $\mathbf{F} = q(\mathbf{E} + \mathbf{v}\times\mathbf{B})$ emerges as the leading-order DCGT output for charged participation transport.

This is the substrate-to-continuum bridge for the electromagnetic content of MHD (Chapter 9) and for Maxwell's equations more generally. The same machinery generalizes to non-Abelian gauge theory in Section 3.7.

### 3.6.6 The five together

The five leading-order consequences cover the structural content of every classical continuum field theory in the program's closed-arc inventory. Scalar diffusion produces soft-matter mobility (Chapter 10) and the substrate-level analogue of heat conduction. Directional viscosity produces the viscous sector of NS (Chapter 8). V1→R1 produces substrate-cutoff regularization in NS (Chapter 8) and the YM mass-gap mechanism (Chapter 9) and the BH area-law motif alphabet (Chapter 13). V5→Maxwell produces soft-matter viscoelasticity (Chapter 10). T17 minimal coupling produces electromagnetism and (with non-Abelian generalization) Yang–Mills.

Together, these five consequences span the entire continuum-classical-physics content the program derives. There is no continuum theory in the program's closed-arc inventory that does not pass through at least one of them.

## 3.7 The Non-Abelian Generalization

### 3.7.1 What changes for non-Abelian content

T17 minimal coupling (Section 3.6.5) covers Abelian gauge structure (U(1) electromagnetism). The Yang–Mills content of Chapter 9 requires the same DCGT machinery applied to non-Abelian compact-simple-group gauge structures. The generalization is structural: the multi-scale expansion remains the same; the cross-bandwidth structure remains the same; the difference is that the participation rule-types being coarse-grained carry non-Abelian internal labels rather than Abelian (charge-only) labels.

The output of the non-Abelian DCGT generalization is the continuum Yang–Mills equation $D_\mu F^{\mu\nu} = J^\nu$ at leading order, plus a substrate-level mass-gap mechanism at first subleading order from V1's second-moment expansion. Chapter 9 develops both. The machinery is exactly DCGT — the same hydrodynamic-window scale separation, the same multi-scale expansion, the same five-consequence structure — applied to a different content channel.

### 3.7.2 Why the generalization works

The structural reason DCGT generalizes cleanly to non-Abelian content is that the substrate ontology does not commit to which gauge group nature realizes. T17 establishes gauge fields as participation measures of structural rule-types; the *form* of gauge field content is FORCED by the substrate, but the specific gauge group (Abelian U(1) vs non-Abelian SU(2), SU(3), etc.) is empirical input. DCGT's machinery is therefore agnostic about gauge-group choice: it produces the appropriate continuum Yang–Mills equation for whichever compact-simple-group structure the rule-type carries.

The form-FORCED status of DCGT's non-Abelian generalization means: the framework predicts the *form* of the Yang–Mills equation (the $D_\mu F^{\mu\nu} = J^\nu$ structure) and the *form* of the mass-gap mechanism, without committing to specific values for gauge couplings or to specific gauge groups. The Standard Model gauge group remains empirical input; the form of Yang–Mills equations is FORCED.

## 3.8 DCGT's Role Across the Closed-Arc Inventory

The closed-arc inventory's dependence on DCGT is comprehensive. The summary below identifies which DCGT output each closed sector consumes.

```math
\begin{array}{l|l}
\text{Closed sector} & \text{DCGT output consumed} \\
\hline
\text{Phase-1 closure of QM (Ch. 5)} & \text{V1 mediation; bandwidth-conservation structure} \\
\text{Form-level QFT (Ch. 6)} & \text{T17 minimal coupling; vacuum-response structure} \\
\text{Quantum computation (Ch. 7)} & \text{Cross-bandwidth } \Gamma_\mathrm{cross} \\
\text{Navier–Stokes (Ch. 8)} & \text{Directional viscosity; V1→R1 cutoff} \\
\text{MHD and Yang–Mills (Ch. 9)} & \text{T17 minimal coupling; non-Abelian generalization; V1 mass-gap} \\
\text{Soft-matter mobility (Ch. 10)} & \text{Scalar diffusion; V5→Maxwell memory} \\
\text{Substrate gravity (Ch. 11)} & \text{Cumulative-strain coarse-graining} \\
\text{Curvature emergence (Ch. 12)} & \text{Acoustic-metric kinematic-summary} \\
\text{Black-hole architecture (Ch. 13)} & \text{Cross-bandwidth } \Gamma_\mathrm{cross}; V1\text{ motif alphabet} \\
\end{array}
```

Every row uses DCGT or one of its generalizations. The two rows that use the largest DCGT footprint are quantum computation (which uses cross-bandwidth in UR-1, V1 in commitment-injection, and the multi-scale expansion structure in deriving the multiplicity-cap function) and black-hole architecture (which uses cross-bandwidth in horizon formation, V1 in motif counting, and the substrate-condition $\sigma$-threshold in five distinct architectural results). Both sectors use DCGT through the same $\Gamma_\mathrm{cross}$ structure at scales separated by ~50 orders of magnitude.

## 3.9 The Substrate-to-Continuum Mapping

### 3.9.1 What DCGT delivers in plain structural terms

DCGT takes substrate-level inputs:
- The substrate primitives of Chapter 1.
- The load-bearing invariants of Chapter 2.
- A system characterized by a continuum-flow scale $L_\mathrm{flow}$ that admits a hydrodynamic window $\ell_P \ll R_\mathrm{cg} \ll L_\mathrm{flow}$.

And produces continuum-level outputs:
- Leading-order continuum equations governing the system's coarse-grained dynamics.
- First-subleading-order substrate-cutoff corrections that distinguish ED from purely phenomenological continuum theories.
- The cross-bandwidth structure $\Gamma_\mathrm{cross}$ governing two-region exchange.
- Coarse-graining-invariant content that does not depend on the choice of $R_\mathrm{cg}$ within the window.

### 3.9.2 The form-FORCED / value-INHERITED content of DCGT

The form of DCGT's output is FORCED:
- The hydrodynamic-window scale separation requirement.
- The multi-scale expansion structure.
- The exponential form of $\Gamma_\mathrm{cross}$ in integrated $\sigma$.
- The five leading-order consequences (scalar diffusion, directional viscosity, V1→R1, V5→Maxwell, T17 minimal coupling).
- The non-Abelian generalization structure for Yang–Mills.

The value of DCGT's output is INHERITED:
- The specific dimensionless prefactor $\alpha$ in the cross-bandwidth exponential.
- The specific diffusion coefficient in scalar diffusion.
- The specific viscosity coefficient in directional viscosity.
- The specific R1 cutoff coefficient $\kappa\mu_\mathrm{V1}\ell_P^2$.
- The specific Maxwell relaxation time $\tau_R$ (V5 first temporal moment).
- The specific gauge-coupling values in Yang–Mills (gauge-group-specific empirical input).

### 3.9.3 What DCGT does *not* deliver

DCGT does not deliver:
- The advective sector of Navier–Stokes (a frame-kinematic artifact, not a substrate consequence).
- The pressure and incompressibility constraints in NS (continuum-imposed constraints, not DCGT outputs).
- Einstein's general relativity (Chapter 12 is honest that the acoustic-metric covariantization is kinematic-class, not full GR).
- A constructive proof of the Clay Yang–Mills problem (Chapter 9 gives a structural-positive verdict at the substrate-suggestive level, which is a form-level claim, not a constructive theorem at Streater–Wightman / OS-axiom rigor).
- Specific numerical values for any of the substrate constants.

What DCGT delivers and does not deliver is precisely demarcated. Chapters 8–13 each respect the demarcation and identify which content within the chapter is DCGT-derived (form-FORCED) versus continuum-imposed (frame-kinematic, constraint-class, or empirical-input).

## 3.10 The Coarse-Graining Bridge as Audit Trail

### 3.10.1 Auditability is a methodological commitment

Every continuum equation in the program's closed-arc inventory should be reachable from substrate primitives through an audited derivation chain. DCGT is the program's central auditing instrument: it takes substrate-level content as input and produces continuum-level content as output, with each step in the chain identified and form-FORCED versus value-INHERITED status of the output explicitly demarcated.

The audit trail's structure is the same in every closed sector:
1. Identify the substrate primitives consumed.
2. Identify the load-bearing invariants used.
3. Specify the hydrodynamic window for the system being analyzed.
4. Apply the DCGT multi-scale expansion.
5. Read off the leading-order continuum equation as form-FORCED output.
6. Read off the first-subleading substrate-cutoff correction as a separate form-FORCED output.
7. Identify which numerical values in the output are INHERITED.
8. Identify which content in the original continuum theory (if any) is frame-kinematic or continuum-imposed and therefore not DCGT-derived.

This audit structure is implicit in every chapter from Chapter 5 onward. The program's methodological commitment is that any reader can, in principle, perform this audit on any continuum equation derived in the program.

### 3.10.2 The audit at the boundaries of DCGT applicability

When the hydrodynamic window does not exist (when scale separation is marginal or fails), DCGT is not applicable, and the substrate must be analyzed without coarse-graining to a clean continuum equation. The framework is honest about these regimes:

- The matter-wave Q-C boundary at 140–250 kDa molecular mass (Chapter 7): the molecule's effective system multiplicity has crossed the substrate threshold, and the DCGT-derived unresolved-rule regime ceases to be sustainable.
- The BH-3 saturated participation zone (Chapter 13): substrate gradients have steepened to the saturation regime where the acoustic-metric reading breaks down, and the coarse-grained continuum content is replaced by a substrate-level finite-thickness saturated zone.
- The deep-MOND superluminal scalar propagation in Arc ED-10 (Chapter 12): the acoustic-metric scalar-tensor covariantization produces a kinematic-class reading whose superluminality is a structurally-FORCED consequence of producing the substrate-derived MOND behavior without introducing additional dynamical fields.

In each of these cases, the framework identifies the boundary of DCGT applicability explicitly and resorts to substrate-level analysis without requiring a clean continuum equation. The audit trail is preserved; the audit's content changes from "DCGT applied" to "DCGT not applicable here, substrate-level analysis used directly."

## 3.11 Form-FORCED vs Value-INHERITED at the Coarse-Graining Bridge

### 3.11.1 What is form-FORCED at this layer

- The hydrodynamic-window scale separation requirement $\ell_P \ll R_\mathrm{cg} \ll L_\mathrm{flow}$.
- The multi-scale expansion structure with the small parameter $\ell_P/R_\mathrm{cg}$.
- The exponential structure $\Gamma_\mathrm{cross} \sim \exp[-\alpha\int_\mathrm{path}\sigma\,d\ell]$ for substrate-mediated cross-region exchange.
- The five leading-order coarse-grained consequences (scalar diffusion, directional viscosity, V1→R1, V5→Maxwell, T17 minimal coupling).
- The non-Abelian generalization to Yang–Mills.
- The coarse-graining-invariance condition for leading-order outputs.
- The substrate-cutoff structure of first-subleading corrections.
- The boundaries of DCGT applicability (matter-wave Q-C boundary, BH saturated zone, deep-MOND superluminality regime).

### 3.11.2 What is value-INHERITED at this layer

- The specific functional shape of the V1 finite-width vacuum kernel (the existence and finite-width are FORCED; the closed-form shape is INHERITED).
- The specific dimensionless prefactor $\alpha$ in the cross-bandwidth exponential structure.
- The specific diffusion coefficient in scalar diffusion (set by substrate-channel statistics; INHERITED).
- The specific viscosity coefficient in directional viscosity (INHERITED).
- The specific R1 cutoff coefficient combination $\kappa\mu_\mathrm{V1}\ell_P^2$ (INHERITED; appears as the small substrate-cutoff prefactor).
- The specific Maxwell relaxation time $\tau_R$ (INHERITED from molecular or substrate physics).
- The specific T17 minimal-coupling charge values (INHERITED from gauge-group empirical input).
- The specific numerical thresholds at the boundaries of DCGT applicability (the matter-wave boundary value of 140–250 kDa, the BH-3 saturation threshold $\beta_\mathrm{crit}$, the deep-MOND transition acceleration $a_0$).

### 3.11.3 Methodological consistency at the coarse-graining bridge

The form-FORCED / value-INHERITED pattern at the coarse-graining bridge is consistent with the pattern at the primitive layer (Chapter 1) and the load-bearing invariants layer (Chapter 2). Form is structurally fixed; values are calibrated empirically against anchors. DCGT inherits the methodology; every subsequent chapter inherits it from DCGT.

## 3.12 Dependencies

### 3.12.1 Upstream

- **Chapter 1.** P01 event discreteness (sets the substrate length scale floor); P04 bandwidth update (controls the substrate's bounded-bandwidth content); finite-kernel commitments (V1, V5 finite-width); substrate-locality commitments (controls the path-integration structure of $\Gamma_\mathrm{cross}$).
- **Chapter 2.** Load-bearing invariants — particularly $\sigma$ (entering the cross-bandwidth exponent), V1 (entering the substrate-cutoff structure), and the $\Gamma_\mathrm{cross}$ definition that DCGT formalizes.

### 3.12.2 Downstream

- **Chapter 4 (Theorem N1 + Theorem 18).** Theorem N1 establishes V1 as a finite-width chain-sourced response kernel, formally completing the V1 commitment that DCGT consumes. Theorem 18 propagates P11 + chain structure through V1 to forward-cone-only support, formally completing the kernel-arrow content that DCGT inherits.
- **Chapter 5 (Phase-1 closure).** DCGT's V1 mediation enters the Born-rule and Schrödinger-equation derivations indirectly through bandwidth-conservation structure.
- **Chapter 6 (Form-level QFT).** DCGT's T17 minimal-coupling content is the substrate-to-continuum bridge for gauge fields; vacuum-response structure passes through DCGT's V1 content.
- **Chapter 7 (Quantum computing).** The cross-bandwidth structure $\Gamma_\mathrm{cross}$ enters UR-1's condition (ii). The multi-scale expansion underlies the unresolvedness $\mathcal{U}$'s three-factor product structure.
- **Chapter 8 (Navier–Stokes).** DCGT directly produces the viscous sector and the V1→R1 substrate-cutoff regularization.
- **Chapter 9 (MHD and Yang–Mills).** DCGT's T17 minimal coupling produces the Lorentz force; the non-Abelian DCGT generalization produces Yang–Mills; V1's second-moment produces the YM mass-gap.
- **Chapter 10 (Soft-matter mobility).** DCGT's scalar-diffusion content produces the Universal Mobility Law; V5→Maxwell produces viscoelasticity.
- **Chapter 11 (Substrate gravity).** DCGT's cumulative-strain coarse-graining is the substrate-to-continuum bridge for the modified Poisson equation.
- **Chapter 12 (Curvature emergence).** DCGT's acoustic-metric kinematic-summary content underlies the scalar-tensor covariantization.
- **Chapter 13 (Black-hole architecture).** DCGT's cross-bandwidth structure governs horizon formation; V1's per-patch motif content governs the area-law entropy form.
- **Chapter 14 (Cross-platform unifications).** The cross-domain identity between BH horizon formation and QC condition (ii) failure rests on the same DCGT-derived $\Gamma_\mathrm{cross}$ structure.
- **Chapter 15 (Public test inventory).** Empirical anchors calibrate the value-INHERITED coefficients in DCGT's leading-order and substrate-cutoff outputs.

The graph is comprehensive. Every chapter from Chapter 4 onward depends on DCGT directly or through a chapter that does.

## 3.13 Canonical Sources

- Arc D memos in `theory/Arc_D/`
- NS Synthesis Paper Appendix D — `papers/Navier Stokes_Synthesis_Paper/`
- ED-QFT Unified Overview Paper — `papers/ED_QFT_Overview/`

The Arc D memos contain the formal derivation of DCGT's multi-scale expansion structure and the explicit production of the five leading-order consequences. NS Synthesis Paper Appendix D presents the DCGT material in publication-grade form integrated with the Navier–Stokes program. The ED-QFT Unified Overview Paper presents DCGT in its program-level role across the closed-arc inventory.

The Monograph Shell's Appendix A theorem provenance map and Appendix B notation glossary are the cross-reference documents that connect DCGT's outputs to the downstream theorems and notation used throughout the monograph.

## 3.14 Optional Figures

**Figure 3.1 — The substrate / continuum gap and DCGT as bridge.** A horizontal arrangement: substrate primitives (Chapter 1) on the left, continuum equations (Chapters 5–13) on the right, and DCGT in the middle as the labeled bridge. The figure makes visible that DCGT is the *only* substrate-to-continuum bridge in the program; every continuum equation reaches its substrate origin through it.

**Figure 3.2 — The hydrodynamic-window scale separation.** A logarithmic length-scale axis from $\ell_P$ at the bottom to $L_\mathrm{flow}$ at the top, with $R_\mathrm{cg}$ marked at an intermediate scale. The window between $\ell_P$ and $L_\mathrm{flow}$ is shaded; outside the window, DCGT does not apply. Annotations identify the window boundaries for representative systems: matter-wave interferometry (small molecule scale to interferometer scale), SC qubit array (substrate scale to system scale), galactic dynamics (substrate scale to galactic radius), black-hole architecture (substrate scale to horizon scale).

**Figure 3.3 — The multi-scale expansion ordering.** A vertical arrangement showing leading order producing standard continuum equations, first subleading order producing substrate-cutoff corrections (R1 in NS, mass-gap in YM, motif-correlation in BH), and higher subleading orders producing increasingly small substrate-cutoff content. Each row is annotated with the small-parameter power $(\ell_P/R_\mathrm{cg})^n$ that produces it.

**Figure 3.4 — The five leading-order DCGT consequences.** A radial diagram with DCGT at the center and five spokes radiating outward to: (i) scalar diffusion (used in Chapter 10); (ii) directional viscosity (used in Chapter 8); (iii) V1→R1 substrate-cutoff (used in Chapters 8, 9, 13); (iv) V5→Maxwell viscoelastic memory (used in Chapter 10); (v) T17 minimal-coupling Lorentz force (used in Chapters 6, 9). The figure makes visible the breadth of DCGT's downstream consumption.

**Figure 3.5 — The cross-domain $\Gamma_\mathrm{cross}$ echo.** A length-scale diagram showing the same DCGT-derived exponential structure $\Gamma_\mathrm{cross} \sim \exp[-\alpha\int_\mathrm{path}\sigma\,d\ell]$ producing phenomena at scales separated by ~50 orders of magnitude: Josephson-junction MQT at $\sim 10^{-9}\,\mathrm{m}$ (Chapter 7), QC condition (ii) failure at $\sim 10^{-3}\,\mathrm{m}$ (Chapter 7), BH horizon formation at $\sim 10^{4}\,\mathrm{m}$ for stellar-mass black holes (Chapter 13), Rindler horizons at acceleration-dependent scales, cosmological horizons at $\sim H_0^{-1}$. The figure is the visual form of the cross-domain identity developed in Chapter 14.

**Figure 3.6 — DCGT's footprint across the closed-arc inventory.** A grid: rows are the five DCGT leading-order consequences plus the cross-bandwidth structure plus the non-Abelian generalization; columns are the nine closed sectors. Cells are filled where the DCGT output is consumed in the sector. The figure makes visible that no closed sector escapes DCGT's reach.
