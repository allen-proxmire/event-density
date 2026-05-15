# From Primitives to Yang-Mills Existence and Mass Gap

## A Walkthrough of the Event Density Arc YM Closure

**Allen Proxmire** · May 2026

---

## 1. The Question

The Yang-Mills existence and mass gap problem is one of the seven Clay Millennium Prize Problems, posed in 2000 with a million-dollar prize for resolution. The question is mathematically precise but mathematically deep: prove that for any compact simple gauge group, quantum Yang-Mills theory exists on four-dimensional Minkowski spacetime as a relativistic quantum field theory satisfying the Wightman or Osterwalder-Schrader axioms, and that it has a mass gap — a strictly positive lowest excitation energy above the vacuum.

The problem matters because Yang-Mills theory is the mathematical structure underlying the Standard Model's strong and electroweak interactions. Asymptotic freedom, color confinement, the quark-gluon plasma, the spectrum of hadrons — all of these phenomenological features rest on Yang-Mills foundations that have been validated empirically across decades but remain mathematically unproven at the level of the Wightman or Osterwalder-Schrader axioms. The Clay problem asks for the foundation, not the phenomenology.

Despite seventy years of work since Yang and Mills's 1954 paper, the question remains open. Constructive quantum field theory has produced Yang-Mills theory in two and three spacetime dimensions, but four dimensions has resisted. Lattice gauge theory provides a non-perturbative regularization that produces a mass gap on the lattice, but the continuum limit at fixed physical mass scale has not been rigorously established. Functional integration approaches encounter Gribov copies — multiple gauge-equivalent representatives of the same physical configuration that ordinary gauge-fixing prescriptions cannot uniquely select among, breaking Osterwalder-Schrader reflection positivity in the gauge-fixing sector. The historical stall point of constructive Yang-Mills existence is OS-positivity preservation in the gauge-fixing sector, not the kinetic or self-interaction structure.

The Event Density framework's contribution to the Clay-YM problem is methodologically distinct, paralleling the framework's contribution to the Clay-NS smoothness problem. The framework neither solves Clay-YM nor is irrelevant to it. It supplies a partial structural framework that produces a substrate-derived continuum Yang-Mills equation D_μF^μν = J^ν, identifies a substrate-induced mass-gap mechanism via the V1 finite-width vacuum kernel's second-moment expansion, classifies all Yang-Mills content under the framework's canonical-versus-non-canonical ontology, and audits Osterwalder-Schrader positivity channel-by-channel. The result is a structural-suggestive positive verdict conditional on a four-element preservation locus — compact gauge group, V1 positive Fourier transform, kernel-profile rescaling condition, and matter-sector OS positivity. The verdict is structural, not constructively rigorous.

This is parallel framing to NS-Smoothness Intermediate Path C. ED supplies a real Clay-relevant structural mechanism (R1 substrate-cutoff stabilization for NS smoothness; substrate-induced mass scale plus non-Abelian quartic stabilization for YM gap and existence). The Clay-relevance verdict in each case is conditional on a value-inherited condition that ED catalogues but does not predict numerically — R1 versus super-Burnett quantitative competition for NS, kernel-profile rescaling exponent for YM. The framework's discipline at Clay-prize-relevance territory is structural decomposition with explicit identification of load-bearing inherited conditions.

What the framework does forcefully establish:

The continuum Yang-Mills equation D_μF^μν = J^ν follows from substrate primitives via DCGT-style multi-scale expansion of non-Abelian gauge-field correlators, with the non-Abelian commutator structure forced by T17's substrate-level rule-type bracket structure on the gauge generators.

A substrate-induced mass scale m_eff² ~ c_V1 ℓ_P^(−2) arises automatically from V1's finite-width vacuum kernel via second-moment expansion, gauge-invariant kinetic-class not Proca-class, with non-Abelian quartic self-interaction structurally distinguishing the gap-bearing case from the Abelian gapless case.

The Yang-Mills equation contains four canonical-ED content channels (kinetic, self-interaction, matter source, higher-derivative correction) with zero transport-kinematic obstruction class — structurally cleaner than NS or MHD.

OS positivity is preserved channel-by-channel for the canonical-ED sector at the structural-suggestive level under the four-element preservation locus.

The classical constructive-QFT obstruction at OS-positivity preservation in the gauge-fixing sector is reframed by T17's substrate-level gauge-quotient identification, which bypasses the continuum gauge-fixing problem at the substrate scale rather than solving it.

The walkthrough has eight structural moves. Three forcing arguments (substrate-to-continuum derivation, mass-gap mechanism, architectural classification), one positivity audit (channel-by-channel OS-positivity preservation), one verdict (Clay-relevance Intermediate Path C analogue), and a closing discussion of what the argument establishes. The structural payoff: the framework reaches Clay-prize-relevance territory on a second Clay problem with a parallel Intermediate Path C-style honest verdict, demonstrating the framework's methodological discipline at the highest-stakes mathematical-physics open questions.

---

## 2. The Substrate Ontology

The framework rests on substrate-level ontological commitments — the same primitives that gave the Born rule, the Schrödinger equation, the Klein-Gordon equation, the Dirac equation, the structural mass content, the spin-statistics theorem, and the Navier-Stokes smoothness decomposition. The Yang-Mills walkthrough adds four prerequisite structural results that jointly enable the substrate-to-continuum mapping.

**Micro-events, chains as worldlines, channels, bandwidth.** Reality consists of discrete acts of becoming. Chains hold these together via persistent rules. Channels are the substrate's adjacency-mediated communication structure. Bandwidth measures local participation density. (Same as in previous walkthroughs.)

**Theorem 17 (Gauge Fields as Rule-Type Structure).** From the framework's Arc Q closure. Establishes that the gauge connection A_μ that appears in minimal coupling is the participation measure of a structural rule-type $\tau_g$ whose group content is non-Abelian-capable with Killing-form positivity and Jacobi closure. The relevant T17 clauses for this walkthrough:

C2 — substrate gauge group is non-Abelian-capable with Lie bracket [T^a, T^b] = i f^abc T^c on the generators, Killing form K^ab = f^acd f^bcd positive-definite for compact simple groups.

C3 — generalized minimal coupling at the substrate-level commitment vertex: ∂_μ → D_μ = ∂_μ − ig A_μ^a T^a with g the gauge coupling.

C8 — unified four-channel gauge-quotient identification at substrate level. This is the load-bearing clause for the OS-positivity reframing later in the walkthrough.

T17 establishes the substrate-level non-Abelian gauge structure forced. The specific compact simple gauge group is inherited at value layer.

**Theorem 18 (V1 Kernel Forward-Cone Retardation).** From the framework's Arc B closure. Establishes that the V1 vacuum response kernel has forward-cone-only support at the substrate level — micro-events at one location influence subsequent micro-events at causally-connected locations only. The substrate-level analytic-structure ancestor of upper-half-plane analyticity in standard QFT. Required for OS-positivity preservation analysis: forward-cone support at substrate level translates to the analytic-structure properties needed for reflection-positive correlators.

**ED-I-06 (Fields and Forces in Event Density).** The framework's directional-field/scalar-field/curvature-like-field ontology. Forces are biases in participation flow sourced by stable participation structures. Non-forces (transport-kinematic frame artifacts and continuum-imposed constraints) appear in continuum equations but are not sourced by participation structure. This ontology is the canonical-versus-non-canonical classification axis used in the architectural classification step.

**Diffusion Coarse-Graining Theorem (DCGT).** From Arc D. Establishes the substrate-to-continuum coarse-graining methodology used to derive the continuum Yang-Mills equation. DCGT supplies hydrodynamic-window scale separation conditions, multi-scale expansion methodology, form-FORCED / value-INHERITED structural split, sign-FORCED kernel-positivity arguments, and error-bound scaling. The same DCGT machinery used for NS viscosity, R1 hyperviscosity, V5 viscoelastic memory, and the Abelian Lorentz force generalizes here to non-Abelian gauge fields.

**The participation measure for gauge-charged chains.** From the Klein-Gordon walkthrough plus T17, the participation measure for a chain charged under the gauge group is:

$$
P_K(x^\mu) = \sqrt{b_K}(x^\mu) \cdot e^{i\pi_K(x^\mu})
$$

with the local U(1) phase replaced by the local gauge transformation under T17. For non-Abelian gauge groups, the phase factor is replaced by a path-ordered exponential of the gauge connection along the worldline. The minimal coupling D_μ = ∂_μ − ig A_μ^a T^a acts on the rule-type's internal index space via the representation R(T^a) of the generators on the matter representation.

**Form-FORCED versus value-INHERITED methodology.** The same discipline preserved throughout the framework. Form-FORCED content is derivable from architectural principles. Value-INHERITED content is specific numerical parameters that the canon does not determine. For Yang-Mills, the equation form is forced; gauge coupling g, specific compact simple gauge group choice, kernel widths, and kernel-profile rescaling exponents are inherited.

That's the working set. From here, the walkthrough runs through three forcing arguments to derive the continuum YM equation, identify the mass-gap mechanism, and classify the architectural content, then through one positivity audit and a verdict.

---

## 3. The Substrate-to-Continuum Yang-Mills Derivation

The first structural move derives the continuum Yang-Mills equation from substrate primitives via DCGT-style multi-scale expansion of non-Abelian gauge-field correlators. The derivation generalizes the NS-MHD-2 Abelian Lorentz-force derivation to non-Abelian gauge content using the same DCGT machinery plus T17's non-Abelian commutator structure.

### 3.1 The substrate non-Abelian gauge structure

T17 establishes the substrate gauge field as the participation measure of a structural rule-type $\tau_g$ with non-Abelian-capable group content. For a compact simple gauge group G with Lie algebra g of dimension dim(G), write:

$$
A_\mu(x) = A_\mu^a(x) T^a, a = 1, ..., dim(G)
$$

with T^a Hermitian generators of g satisfying:

$$
[T^a, T^b] = i f^{\mathrm{abc}} T^c
$$

where f^abc are the totally-antisymmetric structure constants of G. The Killing form K^ab = f^acd f^bcd is positive-definite for compact simple groups (T17 clause C2). The Jacobi identity closes the algebra. The compactness of G is the structural condition required later for OS positivity.

T17 clause C3 establishes generalized minimal coupling at the substrate-level commitment vertex. The non-Abelian extension of the U(1) minimal coupling is:

$$
\partial_\mu \to D_\mu= \partial_\mu − ig A_\mu^a T^a
$$

with g the gauge coupling (dimensionless in 4D, inherited at value layer per T17's form-FORCED / value-INHERITED split). For charged structural rule-types in representation R of G, the generators T^a act on the rule-type's internal index space via R(T^a).

### 3.2 The substrate field strength

The substrate-level gauge-field strength is the directional-field curvature of A_μ under the non-Abelian commutator structure forced by T17. Define:

$$
F_\mu \nu \equiv \partial_\mu A_\nu − \partial_\nu A_\mu − ig[A_\mu, A_\nu]
$$

componentwise:

$$
F_\mu \nu^a = \partial_\mu A_\nu^a − \partial_\nu A_\mu^a + g f^{\mathrm{abc}} A_\mu^b A_\nu^c
$$

The non-Abelian commutator term is forced by the rule-type bracket structure. The forcing argument runs through substrate-level participation-channel parallel-transport on closed loops:

T17 clause C2 establishes the substrate gauge group as non-Abelian-capable with Lie bracket structure on the generators.

The substrate-level participation-channel parallel-transport on a closed loop of side δ accrues a phase ~ g [A_μ, A_ν] δ^μ δ^ν at second order, generated by the rule-type bracket.

Closing the loop and antisymmetrizing in (μ, ν) extracts the substrate curvature, identical in form to the standard Yang-Mills field strength.

For the Abelian case (U(1), f^abc = 0), the commutator vanishes and F_μν → ∂_μ A_ν − ∂_ν A_μ, the standard Maxwell field strength. The non-Abelian case adds the commutator structure as the load-bearing new element relative to NS-MHD-2's Abelian derivation.

### 3.3 Coarse-graining the non-Abelian flux

Apply DCGT-style multi-scale expansion to the substrate gauge-field flux. Define the substrate gauge-flux tensor:

$$
\Phi_\mu \nu^a(x) = (V1-kernel-weighted chain transport of A_\nu^a along \partial_\mu direction)
$$

That is, the substrate-level transport of the gauge potential along the μ̂ chain-step direction, V1-weighted by the substrate finite-width kernel at scale ℓ_P, evaluated on chains carrying gauge content under T17 minimal coupling.

Apply hydrodynamic-window coarse-graining $\langle \cdot \rangle$_R_cg under the scale separation:

$$
\ell_P ≪ R_{\mathrm{cg}} ≪ L_{\mathrm{flow}}
$$

Multi-scale expansion of the V1-weighted transport integral parallels the velocity-sector analysis in Arc D: zeroth moment yields the field itself; odd moments vanish by V1 isotropy; even moments yield successive Laplacian-class corrections.

Antisymmetrizing Φ_[μν]^a on the spacetime indices and adding the rule-type commutator contribution from substrate parallel-transport yields:

$$
\langle \Phi_{[\mu\nu]}^a\rangle_{R_{\mathrm{cg}}} = F_{\mu\nu}^a + O(\ell_P^{2} \nabla^{2}A^a)
$$

Term-by-term:

Zeroth moment → ∂_μ A_ν^a − ∂_ν A_μ^a + g f^abc A_μ^b A_ν^c = F_μν^a, the continuum non-Abelian field strength.

First moment vanishes by V1 isotropy.

Second moment → O(ℓ_P² ∇²A) corrections to the field strength. This is the YM analogue of R1 in the velocity sector — a substrate-cutoff stabilization at next-to-leading order. Negligible at hydrodynamic scales but load-bearing for the mass-gap analysis at ~ ℓ_P scales.

The leading-order coarse-grained antisymmetrized gauge-flux tensor is the canonical Yang-Mills field strength.

### 3.4 The covariant divergence

Derive D_μ F^μν = J^ν via the same momentum-flux machinery used for the Abelian Lorentz force, generalized to non-Abelian content.

Under T17 generalized minimal coupling on charged chains, the chain canonical momentum is shifted by −g A_μ^a T^a. The corresponding charged-chain momentum-flux contribution at fluid scale is:

$$
\delta \Pi_\mu \nu^(g) = J_\mu^a A_\nu^a
$$

with J_μ^a the gauge-current density at fluid scale (the non-Abelian analogue of j = ρqv from the Abelian Lorentz-force derivation; here J_μ^a carries gauge-component index a in addition to the spacetime index μ).

Take the substrate momentum-flux divergence:

$$
\partial_\mu \delta \Pi_\mu \nu^(g) = J_\mu^a \partial_\mu A_\nu^a + (\partial_\mu J_\mu^a) A_\nu^a
$$

The second piece involves the gauge-current divergence. For Abelian gauge theory, this vanishes by ordinary current conservation ∂_μ J^μ = 0. For non-Abelian gauge theory, the analogous conservation law is the gauge-covariant version:

$$
D_\mu J^\mu= \partial_\mu J^\mu,a + g f^{\mathrm{abc}} A_\mu^b J^\mu,c = 0
$$

This follows from gauge invariance of the matter sector under T17 (clause C8 unified four-channel quotient; clause C3 vertex-quotient pulled back through coupling). The covariant-conservation law is forced at substrate level.

Substituting ∂_μ J^μ,a = −g f^abc A_μ^b J^μ,c into the divergence and using the Yang-Mills field-strength identity, the right-hand side rearranges into the covariant divergence:

$$
(D_\mu F^\mu \nu)^a = \partial_\mu F^\mu \nu,a + g f^{\mathrm{abc}} A_\mu^b F^\mu \nu,c
$$

Combining the substrate-level momentum-flux divergence with the time-component minimal-coupling contribution and collecting all gauge-current source terms:

$$
(D_\mu F^\mu \nu)^a = J^\nu,a
$$

This is the canonical Yang-Mills equation, derived from substrate primitives via DCGT-style multi-scale expansion of non-Abelian gauge-field correlators plus momentum-flux divergence plus non-Abelian charge conservation.

### 3.5 Status

**Result.** Under hydrodynamic-window coarse-graining ℓ_P ≪ R_cg ≪ L_flow over ED substrate primitives (chains, V1/V5 kernels, charged structural rule-types under T17 generalized minimal coupling on a compact simple gauge group G), the cell-averaged non-Abelian gauge-field strength F_μν^a and gauge-current density J^ν,a satisfy:

$$
D_\mu F^\mu \nu= J^\nu, F_\mu \nu^a = \partial_\mu A_\nu^a − \partial_\nu A_\mu^a + g f^{\mathrm{abc}} A_\mu^b A_\nu^c
$$

with covariant derivative D_μ = ∂_μ − ig A_μ^a T^a acting in the appropriate matter-representation, and gauge-current covariantly conserved D_μ J^μ = 0 via T17 gauge-quotient identification.

The structural form is FORCED by T17 generalized minimal coupling plus DCGT multi-scale expansion plus non-Abelian rule-type bracket structure. Sign-FORCED stabilizing by V1 positive Fourier transform. Values INHERITED at gauge coupling g, kernel widths, specific compact simple gauge group choice. Bianchi identity D_[μ F_νρ] = 0 preserved as algebraic structural consequence (follows from the field-strength definition plus the Jacobi identity).

The Abelian limit (f^abc = 0) recovers ∂_μ F^μν = J^ν, the inhomogeneous Maxwell equation. The non-Abelian case adds the structure-constant gauge-current self-coupling g f^abc A_μ^b F^μν,c via the covariant derivative D_μ.

---

## 4. The Substrate Mass-Gap Mechanism

The second structural move identifies a substrate-induced mass scale arising from V1's finite-width vacuum kernel and analyzes its survival under the continuum limit. The mechanism has four elements.

### 4.1 The V1 second-moment correction

The V1 kernel has finite spatial width at scale ℓ_P (forced by Theorem N1 admissibility class plus T18 forward-cone support). Under the multi-scale expansion of the V1-weighted gauge-field correlator (the same expansion used in the field-strength derivation), the substrate-level field strength acquires a next-to-leading-order correction at second moment:

$$
F_\mu \nu^a \to F_\mu \nu^a + c_V1 \ell_P^{2} \nabla^{2}A_\nu^a + ...
$$

with c_V1 a dimensionless V1-profile coefficient (proportional to the second-moment integral $\langle \delta^{2}\rangle$_V1 / ℓ_P² of the kernel, inherited at value layer per the standard form-FORCED / value-INHERITED split).

This is the YM analogue of R1 in the NS velocity sector. The structural parallel is:

| Velocity sector (NS) | Gauge sector (YM) |
|----------------------|-------------------|
| V1 fourth-moment expansion | V1 second-moment expansion |
| R1: −κ$\mu_V$1 ℓ_P² ∇⁴v | YM mass term: c_V1 ℓ_P² ∇²A |
| Hyperviscous stabilization at high-k | Mass term suppressing low-k massless modes |
| Lyapunov-decay-stabilizing in 3D NS | Mass-gap-stabilizing in YM |
| Form FORCED by V1 finite width | Form FORCED by V1 finite width |
| Sign FORCED by V1 positive Fourier transform | Sign FORCED by V1 positive Fourier transform |

The structural similarity is exact at the level of the kernel-moment expansion. The difference is the order at which the correction enters the equation of motion. In the velocity sector, the leading non-trivial term is the second-moment Laplacian (viscosity) and R1 enters at fourth moment (∇⁴). In the gauge sector, the leading kinetic term −(1/4)F² already contains derivatives of A_μ, so the second-moment expansion of A_ν produces a ∇²A correction one derivative-order lower than the kinetic term, giving an effective mass term.

### 4.2 The effective mass scale

Take the Fourier transform of the substrate-corrected gauge-field equation. With A_μ^a(x) = ∫ d⁴k Ã_μ^a(k) e^(ikx):

$$
\nabla^{2}A_\mu^a(x) \to −k^{2} Ã_\mu^a(k)
$$

The second-moment correction becomes:

$$
c_V1 \ell_P^{2} \nabla^{2}A_\mu^a \to −c_V1 \ell_P^{2} k^{2} Ã_\mu^a
$$

For modes near the substrate cutoff k ~ 1/ℓ_P, this is an order-unity correction to the gauge-field amplitude — non-perturbative at the substrate scale. The standard relation between an inverse-Laplacian shift and a mass term is:

$$
(−k^{2} + m^{2}) Ã ↔ (−\nabla^{2} − m^{2}) A
$$

The substrate-induced shift contributes additively to the kinetic operator at second order in ℓ_P. At momentum scale k ~ 1/ℓ_P, the substrate correction to the dispersion relation is:

$$
k^{2} \to k^{2} + m_{\mathrm{eff}}^{2}(k), m_{\mathrm{eff}}^{2}(k) ~ c_V1 \ell_P^(−2)
$$

This is the substrate-induced mass scale. Three structural points characterize it:

It is **substrate-induced**, not phenomenological. It arises from the V1 kernel's finite width, forced at primitive level. No symmetry-breaking mechanism is invoked.

It is **gauge-invariant kinetic-class**, not Proca-class. A Proca mass term −(1/2) m² A_μ A^μ would explicitly break gauge invariance. The substrate-induced mass term arises in the kinetic operator (as a k-dependent suppression at high k) rather than as a quadratic mass term in A_μ directly. The substrate-corrected gauge-field action remains gauge-invariant; the mass is a spectral property of the gauge-field propagator, not a mass insertion in the Lagrangian.

It is a **kinetic suppression scale**. The mass-term-like structure suppresses modes at high k and produces a finite spectral gap below which no gauge-field modes propagate freely. Structurally similar to lattice-gauge-theory's gap mechanism, with ℓ_P playing the role of the lattice spacing.

### 4.3 Non-Abelian quartic stabilization

The non-Abelian commutator structure −ig[A_μ, A_ν] in F_μν produces self-interactions among gauge-field components. Expanding the YM kinetic term −(1/4) F_μν^a F^μν,a:

$$
−(1/4) F_\mu \nu^a F^\mu \nu,a = −(1/4)(\partial_\mu A_\nu^a − \partial_\nu A_\mu^a)^{2}
− (1/2) g f^{\mathrm{abc}} (\partial_\mu A_\nu^a − \partial_\nu A_\mu^a) A^\mu,b A^\nu,c
− (1/4) g^{2} (f^{\mathrm{abc}} A_\mu^b A_\nu^c)^{2}
$$

The cubic (AAA) and quartic (AAAA) self-interaction vertices arise from the non-Abelian commutator structure. Combining with the substrate-induced mass term, the effective potential for gauge-field fluctuations near a homogeneous background takes the form:

$$
V_{\mathrm{eff}}(A) ~ m_{\mathrm{eff}}^{2} A^{2} + g A^{3} + g^{2} A^{4} + ...
$$

The quartic term g² A⁴ is **non-perturbative-stabilizing**. It bounds the gauge-field amplitude from below at large A and gives the effective potential a stable minimum at A = 0 even in the presence of higher-loop fluctuations.

Two structural consequences:

**The quartic term stabilizes the mass term.** Without the non-Abelian self-interaction, the substrate-induced mass term might be unstable under loop corrections (massless gauge fields tend to remix at low energies via radiative corrections). The quartic term supplies a structural stabilization mechanism: any low-energy fluctuation that would attempt to remove the mass term encounters the quartic potential's confinement to small A, which preserves the gap.

**The cutoff-induced mass is non-perturbatively enhanced.** In the Abelian case (f^abc = 0), the cubic and quartic terms vanish and the substrate-induced mass term is purely perturbative. In the non-Abelian case, the self-interaction terms produce a non-perturbative dressing of the mass term. By analogy to non-perturbative gluon-condensate-class arguments in standard YM, this enhancement is structurally toward increasing the gap rather than closing it.

The non-Abelian enhancement is therefore a structural argument in favor of gap survival: where the Abelian gap might close in the continuum limit (it does — U(1) electromagnetism is gapless), the non-Abelian gap is structurally stabilized by self-interaction. This parallels the standard YM-existence intuition that pure non-Abelian gauge theory should have a mass gap precisely because of self-interaction; the Abelian theory should be gapless.

### 4.4 Continuum-limit survival condition

The substrate-level gap is automatic and forced. The structurally non-trivial question is whether it survives the continuum limit:

$$
\ell_P \to 0, R_{\mathrm{cg}} \to \infty, \ell_P / R_{\mathrm{cg}} \to 0
$$

with the macroscopic flow scale L_flow held fixed.

Naively, the bare substrate-level gap m_eff,bare² ~ c_V1 ℓ_P^(−2) diverges as ℓ_P → 0. This is the same UV divergence pattern that appears in standard QFT under momentum-cutoff regularization. The renormalized gap depends on how the V1 kernel profile rescales as ℓ_P → 0.

Three regimes:

If c_V1(ℓ_P) → 0 as ℓ_P²: the renormalized gap c_V1(ℓ_P) ℓ_P^(−2) is finite; gap survives at finite m_phys² > 0.

If c_V1(ℓ_P) → 0 slower than ℓ_P²: the renormalized gap diverges; substrate gap diverges and the continuum theory is gap-divergent (likely non-physical).

If c_V1(ℓ_P) → 0 faster than ℓ_P²: the renormalized gap closes; substrate gap closes in the continuum limit (gap closure).

**Mass-gap survival condition.** The continuum-limit-survival of the gap is conditional on:

$$
c_V1(\ell_P) \ell_P^(−2) \to m_{\mathrm{phys}}^{2} > 0 as \ell_P \to 0
$$

This is structurally analogous to the renormalization-flow conditions that determine the existence of a continuum limit in lattice gauge theory: the lattice spacing must be taken to zero with the bare coupling tuned to a fixed point such that the physical mass remains finite. The framework's substrate derivation reframes this from a renormalization-flow technicality to a kernel-profile-rescaling condition.

The kernel-profile-rescaling condition is value-INHERITED. ED's structural derivation does not pin the rescaling exponent. The existence of the gap is forced at substrate level (V1 finite width unconditional). The survival of the gap at finite physical value is inherited at kernel-rescaling layer.

---

## 5. The Architectural Classification

The third structural move classifies all Yang-Mills content channels under the framework's ED-I-06 ontology.

### 5.1 Six content channels

Write the substrate-derived YM equation in expanded form:

$$
\partial_\mu F^\mu \nu,a + g f^{\mathrm{abc}} A_\mu^b F^\mu \nu,c = J^\nu,a
$$

Three primary content channels at the level of the equation itself:

(A) Kinetic term ∂_μ F^μν,a — ordinary divergence acting on the gauge-field strength.

(B) Non-Abelian self-interaction g f^abc A_μ^b F^μν,c — structure-constant coupling between the gauge potential and the field strength, present only for non-Abelian G.

(C) Matter-source term J^ν,a — gauge-current density at fluid scale produced by charged-chain populations under T17 generalized minimal coupling.

Three additional content channels enter the YM problem at the level of the full continuum theory:

(D) Gauge-fixing condition (Lorenz, Coulomb, axial) — imposed at continuum level to remove gauge-redundancy from the path integral.

(E) Coordinate artifacts — Christoffel-symbol contributions when ∂_μ → ∇_μ in curved coordinates.

(F) Higher-derivative corrections — c_V1 ℓ_P² ∇²A from V1 second-moment expansion, the YM analogue of R1.

### 5.2 Classification under ED-I-06

**(A) Kinetic term ∂_μ F^μν: Canonical ED.** Originates from substrate-level directional-field curvature of A_μ^a under V1-kernel-mediated multi-scale expansion. Field strength emerges as the leading-order coarse-grained antisymmetrized gauge-flux. Under ED-I-06, A_μ^a is a directional-field-class participation structure (gauge field as participation measure of $\tau_g$ per T17 clause C1); the kinetic term is the dynamical equation of that directional field, sourcing biases on participation flow under canonical mobility-channel logic. Parallel to Maxwell kinetic term in NS-MHD.

**(B) Non-Abelian self-interaction g f^abc A_μ^b F^μν,c: Canonical ED.** Forced by T17 rule-type commutator structure. The substrate-level participation-channel parallel-transport on a closed loop produces the commutator term in F_μν via T17 clause C2. The covariant-derivative structure D_μ acting on the adjoint-representation field strength produces the structure-constant coupling.

The structural distinction matters here. The non-Abelian self-interaction term has the same algebraic shape as a transport-kinematic bilinear (it is bilinear in A_μ with index-structure couplings). But it arises from substrate-level rule-type commutator structure forced by T17, not from coordinate-frame bookkeeping. **Same algebraic shape as advection-class terms; different structural origin; canonical-ED rather than frame-kinematic.**

This structural distinction is important. In NS, advection's bilinear-with-projection structure (k_j P_im(k) u_j u_m) is non-ED — it is an Eulerian-frame coordinate artifact of convective fluxes. In YM, the non-Abelian self-interaction's structure-constant coupling (g f^abc A^b A^c) is canonical-ED — it is forced by the substrate-level Lie-algebra structure of the gauge rule-type $\tau_g$. The algebraic shape similarity is misleading; the structural origins differ.

**(C) Matter source J^ν,a: Canonical ED.** Non-Abelian generalization of the Abelian matter current j = ρqv that appeared in NS-MHD. Substrate origin: charged-chain flux under T17 generalized minimal coupling, with gauge-component index a added to the spacetime current. Charge conservation D_μ J^μ = 0 forced by T17 clause C8 plus C3.

**(D) Gauge condition: Non-ED (continuum-imposed constraint).** Gauge-fixing conditions are continuum-level structural commitments imposed to remove gauge-redundancy from the path-integral or canonical-quantization formulation. They have no substrate analogue. T17 supplies gauge-quotient identification at substrate level (clause C8); the continuum gauge-fixing condition is a continuum bookkeeping device that picks a single representative from each gauge-equivalence class. The gauge condition does not appear in the substrate-to-continuum derivation of D_μ F^μν = J^ν.

Parallel to incompressibility ∇·v = 0 in NS — both are continuum-imposed structural commitments imposed at fluid or gauge-mechanical scale rather than sourced by substrate participation structure.

**(E) Coordinate artifacts: Non-ED (frame-kinematic).** When the YM equation is written in curved coordinates, Christoffel-symbol contributions appear as bookkeeping of the chosen coordinate system, not as dynamics. Vanish in flat Minkowski coordinates. Parallel structurally to advection in NS or induction-kinematic in MHD: those arose as Eulerian-coordinate bookkeeping; Christoffel-symbol contributions arise as curvilinear-coordinate bookkeeping. Both are coordinate-frame artifacts.

**(F) Higher-derivative correction c_V1 ℓ_P² ∇²A: Canonical ED.** YM analogue of R1. Same V1-second-moment substrate origin; same form-FORCED status; same sign-FORCED stabilizing property by V1 positive Fourier transform. Feeds directly into the mass-gap mechanism. Substrate-cutoff bias on gauge-field participation flow sourced by V1 finite-width vacuum-kernel structure.

### 5.3 The architectural picture

| Term | Expression | ED-I-06 Class | Origin |
|------|-----------|---------------|--------|
| Kinetic | ∂_μ F^μν,a | Canonical ED | Participation curvature via V1 |
| Non-Abelian self-interaction | g f^abc A_μ^b F^μν,c | Canonical ED | T17 rule-type commutator |
| Matter source | J^ν,a | Canonical ED | T17 generalized minimal coupling |
| Gauge condition | ∂_μ A^μ,a = 0 | Non-ED | Continuum-imposed constraint |
| Coordinate artifacts | Christoffel terms | Non-ED | Frame-kinematic bookkeeping |
| Higher-derivative | c_V1 ℓ_P² ∇²A | Canonical ED | V1 second-moment (R1 analogue) |

**Aggregate: 4 canonical-ED / 2 non-ED.** The dynamical content of the YM equation is fully canonical ED, with no transport-kinematic obstruction class.

This is structurally significant. NS has a 1-canonical / 1-transport-kinematic ratio in its momentum equation (viscous diffusion canonical, advection non-ED). Full MHD has 4-canonical / 3-transport-kinematic (advection plus induction-kinematic plus Ohm-kinematic all non-ED). YM has 4-canonical / 0-transport-kinematic. **YM is structurally cleaner than NS or MHD** — the non-Abelian gauge sector is more ED-architectural than fluid mechanics.

Three direct consequences:

YM dynamics are fully canonical ED. Every term in D_μ F^μν = J^ν has a substrate origin.

Gauge fixing is non-ED bookkeeping, not a structural feature. Its non-ED status parallels incompressibility in NS — both are continuum-imposed constraints.

OS-positivity analysis applies only to the four canonical-ED channels. Gauge-fixing and Christoffel-class are excluded from the positivity audit by classification.

---

## 6. The OS-Positivity Audit

The fourth structural move audits Osterwalder-Schrader reflection positivity channel-by-channel for the four canonical-ED content channels under Euclidean continuation t → −iτ, A_0 → iA_4.

### 6.1 What OS positivity requires

Reflection positivity in the Osterwalder-Schrader formulation requires that, for any local observable O(x_0, x) with x_0 > 0:

$$
\langle \Theta O, O\rangle \geq 0
$$

where Θ is Euclidean-time reflection (x_0 → −x_0) combined with appropriate field-component conjugation. OS positivity is the structural condition that allows reconstruction of the Hilbert-space quantum theory from the Euclidean correlator — the load-bearing axiom of the OS reconstruction theorem and the historical stall point of constructive YM existence.

### 6.2 Channel-by-channel audit

**Kinetic term (channel A).** In Euclidean signature:

$$
S_E^{\mathrm{kin}} = (1/4) \int d^{4}x F_\mu \nu^a F^\mu \nu,a = (1/2) \int d^{4}x Tr(F_\mu \nu F^\mu \nu)
$$

For compact gauge groups, the Killing form is positive-definite (T17 clause C2), and the trace inner product Tr(T^a T^b) = (1/2)δ^ab in canonical normalization yields:

$$
(1/2) Tr(F_\mu \nu F^\mu \nu) = (1/4) F_\mu \nu^a F^\mu \nu,a \geq 0
$$

The integrand is the squared norm of the field strength under the Killing-form inner product, positive-definite for compact G. The kinetic term is positive-definite for compact gauge groups. This is the same positivity that underlies lattice YM's plaquette action.

**Non-Abelian self-interaction (channel B).** Expanding the YM kinetic term yields cubic and quartic self-interaction terms. The cubic term g f^abc ∂A · A A is reflection-odd under Euclidean reflection (one explicit derivative plus three field factors, producing an odd parity under sign-flip of x_0). Its contribution to the reflection-positive correlator vanishes by reflection antisymmetry.

The quartic term −(1/4) g² (f^abc A_μ^b A_ν^c)² in Lorentzian signature becomes +(1/4) g² (f^abc A_μ^b A_ν^c)² in Euclidean signature after sign-flip. The structure-constant contraction f^abc f^ade produces a positive-semidefinite tensor on A² for compact G via Killing-form positivity. The Euclidean quartic term is positive: ≥ 0 for compact gauge groups.

The self-interaction contributes no negative-norm modes. Its quartic component is positive in Euclidean signature; its cubic component is odd-parity under reflection and sign-cancels at the correlator level.

**Matter source (channel C).** The source term enters as:

$$
S_E^{\mathrm{source}} = \int d^{4}x J_\mu(x) A_\mu(x)
$$

Under Euclidean reflection τ → −τ, the gauge potential transforms as A_4 → −A_4 (time-component) and A_i → A_i (spatial components). The current J_μ, constructed from charged-matter bilinears under minimal coupling, transforms with the same reflection structure. The bilinear J_μ A_μ is reflection-invariant: Θ(J_4 A_4) = (−J_4)(−A_4) = J_4 A_4; Θ(J_i A_i) = J_i A_i.

The reflection-positive correlator:

$$
\langle \Theta(J_\mu A_\mu), (J_\mu A_\mu)\rangle= \langle(J_\mu A_\mu)*, (J_\mu A_\mu)\rangle \geq 0
$$

is non-negative provided the matter sector itself satisfies OS positivity. Matter-sector OS positivity is structurally backed by the framework's closed work — fermionic matter via R.2.5 spin-statistics plus Cl(3,1) framework, bosonic matter via standard scalar-field OS positivity. Under that assumption, the source-term contribution is non-negative.

**Higher-derivative term (channel F).** The action contribution:

$$
S_E^R1 = (1/2) c_V1 \ell_P^{2} \int d^{4}x A_\mu^a (−\nabla^{2}) A^\mu,a
$$

In Euclidean signature, ∇² = ∂_τ² + δ^ij ∂_i ∂_j. Integrating by parts:

$$
\int d^{4}x A_\mu^a (−\nabla^{2}) A^\mu,a = \int d^{4}x |\nabla A_\mu^a|^{2} \geq 0
$$

Combined with c_V1 > 0 from V1 positive Fourier transform (forced by Theorem N1 plus T18):

$$
S_E^R1 = (1/2) c_V1 \ell_P^{2} \int d^{4}x |\nabla A|^{2} \geq 0
$$

The V1-induced higher-derivative term preserves OS positivity. The action contribution is the squared L² norm of ∇A, reflection-symmetric and non-negative. This is the YM analogue of R1 positivity in NS-Smoothness — same V1 substrate origin, same sign-forced stabilizing property, same structural positivity outcome.

### 6.3 The four-element preservation locus

Combining the four channel-by-channel audits, the Euclidean action is bounded below and reflection-positive in each canonical-ED channel separately, conditional on four structural conditions:

**(L1) Compact gauge group.** Required for kinetic-term Killing-form positivity and quartic-term positivity. T17 clause C2 establishes substrate gauge group as non-Abelian-capable with Killing-form closure; compactness is the additional structural condition for OS positivity. Compactness is INHERITED at value layer (specific compact simple group choice is empirical).

**(L2) Kernel positive Fourier transform.** Required for higher-derivative term positivity. Forced at substrate level by Theorem N1 admissibility class plus T18 forward-cone support. Structurally automatic given the closed Arc B / Arc N work.

**(L3) Kernel-profile rescaling condition.** Required for continuum-limit stability of the substrate-induced mass scale: c_V1(ℓ_P) ℓ_P^(−2) → m_phys² ≥ 0 as ℓ_P → 0. INHERITED at value layer per the mass-gap analysis. Mass-gap survival requires m_phys² > 0 strictly; OS-positivity preservation requires only m_phys² ≥ 0 (massless case is OS-positive but gapless, parallel to QED).

**(L4) Matter-sector OS positivity.** Required for source-term positivity. Structurally backed by closed T1–T18 foundation work; assumed in the present audit.

**Necessity and sufficiency.** Under any of (L1)–(L4) failing, OS positivity fails. Under all four holding, each canonical-ED content channel is OS-positive separately, and the combined Euclidean action is bounded below and reflection-positive at the structural-suggestive level.

### 6.4 The gauge-fixing reframing

Standard constructive YM has historically hit obstructions at OS-positivity preservation in the gauge-fixing sector — particularly via Gribov copies in non-perturbative gauge-fixing regimes. Multiple gauge-equivalent representatives of the same physical configuration produce ambiguities in continuum gauge-fixing that break OS positivity at the operator-distribution level on ℝ⁴.

The framework's substrate-derivation reframes this. T17 clause C8 supplies unified four-channel gauge-quotient identification at substrate level — physical equivalence under gauge transformations is identified at the substrate scale rather than at continuum level. The continuum gauge-fixing problem is bypassed at the substrate scale rather than solved at the continuum scale.

This is structurally significant: the historical stall point of constructive YM existence is reframed from a continuum technical problem to a substrate-quotient-commutes-with-DCGT-coarse-graining structural question. The reframing does not resolve the rigorous continuum gauge-fixing issue, but it relocates the structural question to substrate scale where T17 clause C8 supplies a clean structural commitment.

### 6.5 Honest framing

The audit is structural-suggestive, not constructively rigorous. Each canonical-ED content channel has the correct sign and reflection structure to be compatible with OS positivity, and the four conditions (L1)–(L4) are individually satisfiable under the program's existing closed work. A constructive proof at the Streater-Wightman / OS-axiom level would require:

Rigorous control of the gauge-fixing sector at the operator-distribution level, including Gribov-copy obstructions in the non-perturbative regime. Per the architectural classification, gauge-fixing is non-ED bookkeeping; ED's substrate gauge-quotient identification (T17 C8) bypasses the continuum gauge-fixing problem at the substrate scale, but the continuum limit of the gauge-quotient structure is not analyzed here.

Full operator-valued-distribution-on-ℝ⁴ verification, with all n-point Schwinger functions audited for cluster decomposition and reflection positivity.

Continuum-limit convergence of the substrate-level OS-positivity property to the continuum theory under DCGT, including verification that DCGT's hydrodynamic-window error bounds do not destroy OS positivity at the level of the operator structure.

These constructive verifications are out of scope. The structural-positive verdict is that the canonical-ED sector is compatible with OS positivity; the constructive verification is a Clay-problem-class technical question.

---

## 7. The Intermediate Path C Verdict

The fifth structural move integrates the substrate-to-continuum derivation, the mass-gap mechanism, the architectural classification, and the OS-positivity audit into a single Clay-relevance verdict parallel in form and honesty to NS-Smoothness's Intermediate Path C.

### 7.1 The structural decomposition

Six structural consequences combine into the final picture:

**Substrate-to-continuum YM mapping is structurally stable.** DCGT plus T17 plus T18 jointly produce a continuum YM equation with no transport-kinematic obstructions and no analytic-structure pathology at the substrate-derivation level.

**YM dynamics are fully canonical ED.** All dynamical terms arise from substrate participation structure: kinetic from V1 directional-field curvature, self-interaction from T17 rule-type commutator, matter source from T17 generalized minimal coupling, higher-derivative from V1 second-moment expansion. Architecturally cleaner than NS or MHD.

**Substrate mass-gap mechanism exists.** V1 finite width forces a stabilizing ℓ_P² ∇²A correction at substrate level. At Fourier momentum near the cutoff, this produces effective mass scale m_eff² ~ c_V1 ℓ_P^(−2). Non-Abelian self-interaction stabilizes the mass term against loop-correction remixing.

**Mass-gap survival is conditional.** The physical mass gap exists in the continuum limit if and only if c_V1(ℓ_P) ℓ_P^(−2) → m_phys² > 0. This is the kernel-profile-rescaling condition; INHERITED at value layer.

**OS positivity is structurally compatible.** Each canonical-ED channel preserves reflection positivity under Euclidean continuation. The Euclidean action is bounded below for compact gauge groups; the higher-derivative term's positivity follows from V1 positive Fourier transform; the matter-source contribution inherits OS positivity from the matter sector.

**Gauge-fixing obstruction is reframed.** ED's substrate-derivation places gauge-quotient identification at substrate level via T17 clause C8, bypassing the continuum gauge-fixing problem at the substrate scale. The reframing is structurally significant; the resolution of continuum gauge-fixing remains a separate technical question.

### 7.2 The hypothesis-style closure

Parallel in form to NS-MHD-5's H1/H2/H3 resolution and NS-Smoothness's Intermediate Path C:

**YM-existence at structural level: holds.** Substrate-to-continuum mapping produces a well-defined continuum equation D_μ F^μν = J^ν.

**OS-positivity preservation at structural-suggestive level: holds conditional on locus (L1)–(L4).** Each canonical-ED channel preserves reflection positivity separately.

**Mass-gap-from-substrate-cutoff: holds at substrate level; survival conditional on (L3).** Substrate mechanism FORCED; physical-value survival INHERITED.

Verdict: structural-positive, conditional, parallel in form to NS-Smoothness Intermediate Path C.

### 7.3 The Clay-relevance statement

The ED substrate provides a structurally suggestive path toward a constructively stable Yang-Mills continuum limit. Substrate-to-continuum mapping is well-defined; canonical-ED dynamics are FORCED at substrate level; OS positivity is structurally compatible at the canonical-ED-channel level under the four-condition preservation locus.

The mass-gap mechanism is FORCED at substrate level via the V1 finite-width second-moment expansion plus non-Abelian self-interaction stabilization. The mechanism exists unconditionally at substrate level; the physical mass-gap value is INHERITED via the kernel-profile-rescaling condition.

Mass-gap survival in the continuum limit is conditional on c_V1(ℓ_P) ℓ_P^(−2) → m_phys² > 0. ED supplies the structural mechanism; the rescaling exponent that determines whether the gap survives at finite positive value is value-INHERITED.

OS positivity is preserved channel-by-channel under the ED canonical content — kinetic (positive-definite for compact G), self-interaction (positive in Euclidean signature for compact G), matter source (non-negative bilinear), higher-derivative (non-negative via V1 positivity). Combined Euclidean action bounded below plus reflection-positive at the structural-suggestive level.

The gauge-fixing obstruction is reframed via substrate gauge-quotient identification (T17 clause C8). Standard constructive YM has historically hit obstructions at OS-positivity preservation in the gauge-fixing sector — particularly via Gribov copies in non-perturbative gauge-fixing regimes. ED's substrate-level gauge-quotient identification reframes this from a continuum-gauge-fixing technical problem to a substrate-quotient-commutes-with-DCGT-coarse-graining structural question. The reframing is structurally significant; the rigorous resolution remains a separate technical question.

No constructive proof of YM existence or mass gap is claimed. The Clay Yang-Mills Existence and Mass Gap problem requires constructive proof of YM existence with mass gap on ℝ⁴ at the level of Streater-Wightman / Osterwalder-Schrader axioms. The present analysis is structural — the ED account of YM existence and mass gap under substrate-discrete-and-finite assumptions, with OS-positivity preservation analyzed but not proven in full constructive rigor.

The arc identifies the load-bearing structural conditions for a positive Clay-relevance verdict — the OS-positivity preservation locus from the audit:

(L1) Compact gauge group (INHERITED, value-layer).

(L2) V1 positive Fourier transform (FORCED, substrate-level).

(L3) Kernel-profile rescaling condition (INHERITED, value-layer).

(L4) Matter-sector OS positivity (structurally backed by closed work).

If all four hold, the canonical-ED sector of the ED-derived YM theory is structurally compatible with OS positivity and mass-gap survival. ED supplies (L2) FORCED at substrate level and structural backing for (L4); (L1) and (L3) are INHERITED at value layer.

Explicitly: this is not a solution to the Clay Millennium Problem. It is a structural analysis identifying the conditions under which the ED substrate → continuum mapping is compatible with the Clay axioms. The contribution is the substrate framing of the YM equation, the substrate origin of the mass-gap mechanism, the channel-by-channel OS-positivity audit, and the precise specification of the kernel-profile-rescaling condition as the load-bearing INHERITED condition.

---

## 8. What This Argument Establishes

The chain runs:

Substrate primitives (micro-events, participation, chains, channels, four-band bandwidth, individuation, commitment irreversibility, polarity) plus four prerequisite theorems (T17 gauge-as-rule-type, T18 V1 forward-cone retardation, ED-I-06 fields-and-forces ontology, DCGT substrate-to-continuum theorem) → DCGT-style multi-scale expansion of non-Abelian gauge-field correlators with V1 weighting → substrate-level participation-channel parallel-transport on closed loops generating the rule-type bracket commutator term −ig[A_μ, A_ν] → substrate field strength F_μν^a = ∂_μ A_ν^a − ∂_ν A_μ^a + g f^abc A_μ^b A_ν^c → substrate momentum-flux divergence under T17 generalized minimal coupling on charged chains → continuum Yang-Mills equation D_μ F^μν = J^ν with covariant gauge-current conservation → V1 finite-width second-moment expansion producing ℓ_P² ∇²A correction → effective mass scale m_eff² ~ c_V1 ℓ_P^(−2) gauge-invariant kinetic-class → non-Abelian quartic self-interaction g²(f^abc A^b A^c)² stabilizing the mass term against loop-correction remixing → architectural classification with four canonical-ED channels and zero transport-kinematic obstruction → channel-by-channel OS-positivity audit (Killing-form positivity for kinetic, Euclidean quartic positivity for self-interaction, bilinear positivity for source, V1 positive Fourier transform for higher-derivative) → four-element preservation locus → Intermediate Path C-style Clay-relevance verdict.

Each move has its load-bearing argument worked out. The substrate-to-continuum derivation runs through DCGT machinery generalized to non-Abelian fields plus T17 minimal coupling plus the rule-type bracket structure forced by T17 clause C2. The mass-gap mechanism runs through V1 finite width plus second-moment expansion plus Fourier transform plus non-Abelian quartic stabilization. The architectural classification distinguishes canonical-ED dynamical content from non-ED bookkeeping (gauge-fixing, Christoffel artifacts) under ED-I-06 ontology. The OS-positivity audit channel-by-channel produces the four-element preservation locus.

The framework reaches Clay-prize-relevance territory on a second Clay problem with a parallel Intermediate Path C-style verdict. NS-Smoothness: ED-canonical regularizing infrastructure (R1 substrate-cutoff stabilization) plus advection-as-non-ED obstruction with quantitative competition value-inherited. YM existence and mass gap: ED-canonical content fully covering dynamics with no transport-kinematic obstruction, mass gap and OS positivity conditional on the four-element preservation locus with kernel-profile rescaling value-inherited. Two structurally honest Clay-relevance verdicts that document the framework's discipline at the highest-stakes mathematical-physics open questions.

What's gained methodologically: the framework engages Clay-YM structurally rather than auxiliary-positivity-theoretically. Most contributions to constructive YM either claim broader applicability without confronting the gauge-fixing-sector obstruction, or focus on specific lattice-to-continuum techniques without engaging the substrate question of why the equation has the form it has. The framework's contribution is upstream — derives the equation form from substrate primitives via DCGT generalized to non-Abelian gauge fields, identifies the substrate origin of a mass-gap mechanism via V1 second-moment expansion, classifies all content under canonical-versus-non-canonical ontology, and audits OS positivity channel-by-channel with the four-element preservation locus identified explicitly.

The structural beauty of the result is the clean architectural decomposition. The framework produces four canonical-ED content channels with zero transport-kinematic obstruction class. NS has the advection obstruction (the unique transport-kinematic non-ED feature breaking gradient-norm Lyapunov monotonicity). YM has nothing analogous. Every term in the YM equation of motion has a substrate origin. Gauge-fixing and Christoffel-class are bookkeeping rather than dynamical content. The non-Abelian self-interaction term, despite having the same algebraic shape as a transport-kinematic bilinear, is canonical-ED forced by T17's substrate-level rule-type commutator structure rather than coordinate-frame bookkeeping. The framework's structural treatment of YM is architecturally cleaner than its treatment of NS — the gauge sector is more ED-architectural than the fluid-mechanical sector.

This is methodologically interesting. The Clay-NS smoothness problem has the framework reaching partial structural reach (Intermediate Path C with advection-obstruction localized at three independent levels). The Clay-YM existence and mass gap problem has the framework reaching cleaner structural reach (full canonical-ED dynamics with zero transport-kinematic obstruction; mass-gap mechanism forced at substrate level; OS-positivity preservation conditional on four explicit conditions). The framework's reach into mathematical fluid mechanics is partial; its reach into mathematical gauge theory is structurally cleaner. The two Clay problems expose different aspects of the framework's architectural discipline.

This is also rare in the constructive QFT literature. Most theoretical frameworks that touch Clay-YM either claim broad applicability without confronting OS positivity in the gauge-fixing sector, or contribute auxiliary positivity machinery without engaging the substrate question of why the equation form is what it is. The framework's contribution is to engage substrate-level structural questions and to be honest about where its reach ends. The structural-suggestive verdict refuses to claim a Clay-problem solution while documenting precisely what the framework delivers.

Compare with the NS smoothness walkthrough. There, the framework reaches Intermediate Path C with the advection obstruction localized at three independent levels (architectural, dynamical, spectral). Here, the framework reaches Intermediate Path C with the four-element OS-positivity preservation locus identified explicitly. Both verdicts are structurally honest partial closures. The framework's discipline is its methodological signature — derive what the substrate primitives can deliver, identify the load-bearing inherited conditions, refuse to overclaim, and name the inheritance layer where empirical content lives.

The empirical exposure of the YM work is partial. The framework's contribution to Clay-YM is structural-decompositional, not constructively rigorous, so it doesn't make a sharp prediction that experiment can confirm or falsify on the Clay-YM question itself. But the framework's broader gauge-theoretic content does have empirical exposure: the gauge-as-rule-type identification (T17) plus minimal coupling plus the U(1) Lorentz force are reproduced from substrate primitives via DCGT; the non-Abelian generalization here extends the same machinery to compact simple gauge groups; the mass-gap mechanism's substrate origin via V1 second-moment expansion is the same kind of substrate-cutoff structure that produces R1 in NS. The methodological discipline is: derive what the substrate primitives can deliver, refuse to overclaim on what they can't.

Whether the substrate commitments are right is the load-bearing question, as in every walkthrough. The framework stands or falls on whether discreteness, finite participation bandwidth, commitment irreversibility, the four-band bandwidth decomposition, the rule-type taxonomy, the V1 vacuum response kernel, T17's gauge-as-rule-type identification, T18's forward-cone retardation, and DCGT's substrate-to-continuum bridge are the correct foundational concepts. The empirical exposure of this particular walkthrough's content lives in any future test of substrate-level gauge physics that distinguishes the framework from standard treatments. The most empirically substantive open territories include: lattice-versus-continuum YM mass-gap measurements that constrain the kernel-profile rescaling exponent in the framework's terms; precision tests of the non-Abelian gauge structure that constrain T17's substrate-level forcing of the commutator term; gravitational-wave or extreme-energy phenomena that activate the V1 substrate-cutoff scale where the higher-derivative correction becomes load-bearing.

The next steps, structurally, are the broader QFT extension (Arc Q completion with Standard Model gauge group specification and Higgs mechanism evaluation), Phase-3 cosmological work (ED-10 spacetime emergence picking up the curvature-like-field thread from ED-I-06), and the unified ED-QFT overview paper that consolidates the closed structural work across Arc R (relativistic), Arc M (chain mass), Arc Q (gauge / GRH / UV-FIN), Arc N (V1 kernel), Arc B (kernel arrow), DCGT (substrate-to-continuum), and YM (this arc). The framework's primitive stack delivers structural decompositions for foundational questions across multiple domains; the YM walkthrough closes the framework's structural treatment of the second Clay Millennium Prize problem with an honest H1/H2/H3-style verdict that respects the question's open status while documenting precisely what the framework delivers.

The walkthrough collection now stands as a comprehensive presentation of the framework's foundational territory: Born rule, Schrödinger equation, Bell-Tsirelson bound, Heisenberg uncertainty, kernel-level arrow of time, galactic dynamics, black-hole architecture, Klein-Gordon equation, Dirac equation with g = 2, mass form forced with values inherited, spin-statistics theorem at substrate level, Navier-Stokes smoothness via Intermediate Path C, and Yang-Mills existence and mass gap via parallel Intermediate Path C. **Thirteen walkthroughs covering the framework's foundational quantum, gravitational, statistical, mass, fluid-mechanical, and gauge-theoretic content.** Each derivation is structurally honest about what it forces and what remains open. The framework's discipline is its methodological signature — derive what the substrate primitives can deliver, refuse to overclaim, and name the inheritance layer where empirical content lives.

---

## 9. References

- Yang, C. N., Mills, R. L. "Conservation of Isotopic Spin and Isotopic Gauge Invariance." *Physical Review* 96, 191-195 (1954).
- Wightman, A. S. "Quantum field theory in terms of vacuum expectation values." *Physical Review* 101, 860-866 (1956).
- Osterwalder, K., Schrader, R. "Axioms for Euclidean Green's functions." *Communications in Mathematical Physics* 31, 83-112 (1973); 42, 281-305 (1975).
- Wilson, K. G. "Confinement of quarks." *Physical Review D* 10, 2445-2459 (1974).
- Gross, D. J., Wilczek, F. "Ultraviolet Behavior of Non-Abelian Gauge Theories." *Physical Review Letters* 30, 1343-1346 (1973).
- Politzer, H. D. "Reliable Perturbative Results for Strong Interactions?" *Physical Review Letters* 30, 1346-1349 (1973).
- Gribov, V. N. "Quantization of non-Abelian gauge theories." *Nuclear Physics B* 139, 1-19 (1978).
- Jaffe, A., Witten, E. "Quantum Yang-Mills Theory." Clay Millennium Prize Problems description (2000).
- Faddeev, L., Slavnov, A. *Gauge Fields: Introduction to Quantum Theory.* Benjamin/Cummings, 1980.
- Glimm, J., Jaffe, A. *Quantum Physics: A Functional Integral Point of View.* Springer-Verlag, 1987.
- Proxmire, A. *Arc YM-1 Opening (Yang-Mills program scoping).* April 2026.
- Proxmire, A. *Arc YM-2 Substrate to Continuum Limit (DCGT extension to non-Abelian gauge fields).* April 2026.
- Proxmire, A. *Arc YM-3 Mass Gap from Substrate Cutoff.* April 2026.
- Proxmire, A. *Arc YM-4 Architectural Classification.* April 2026.
- Proxmire, A. *Arc YM-5 OS-Positivity and Continuum Stability.* April 2026.
- Proxmire, A. *Arc YM-6 Synthesis and Clay-Relevance Statement.* April 2026.
- Proxmire, A. *NS Synthesis Paper Appendix E — Yang-Mills Synthesis.* April 2026.
- Proxmire, A. *Theorem 17 — Gauge Fields as Rule-Type Structure (Arc Q closure).* April 2026.
- Proxmire, A. *Theorem 18 — V1 Kernel Forward-Cone Retardation (Arc B closure).* April 2026.
- Proxmire, A. *Arc D — Diffusion Coarse-Graining Theorem.* April 2026.
- Proxmire, A. *Event Density Foundations: A Unified Substrate Architecture for Quantum, Fluid, Gauge, and Gravitational Dynamics.* April 2026.
- The full Event Density corpus, including all forced theorems and supporting memos, is available at https://github.com/allen-proxmire/event-density.
