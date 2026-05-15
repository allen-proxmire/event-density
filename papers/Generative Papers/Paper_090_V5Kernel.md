# Paper_090 — The V5 Cross-Chain Correlation Kernel

**Series:** Event Density (ED) Generative Papers — Wave-2 cross-domain kernel
**Author:** Allen Proxmire
**Status:** Publication draft (revision: wedge claim reframed from "40 orders of magnitude unification" to structural formalism unification; $\tau_{V5}$ regime-specificity clarified as inherited not predicted; "necessary for non-Markovian" replaced with "unified substrate mechanism"; Hawking and Maxwell sections reframed as identification rather than prediction)
**Date:** 2026-05-13
**Repository target:** `domain-arcs/wedges/Paper_090_V5_cross_chain_kernel.md` (ED-Generative)
**Working save location:** `C:\Users\allen\GitHub\event-density\papers\Forcing Papers\Paper_090_V5Kernel_FIXED.md`
**Genre:** Conditional structural derivation within the 13-Primitive Generative System. Standalone. Cold-reader accessible.

---

## Abstract

The Event Density (ED) substrate is a 13-primitive generative system whose downstream content includes a hierarchy of kernel rule-types. The first such kernel, **V1**, is the substrate's single-chain vacuum-response kernel (finite-width per Theorem N1, Paper #18; retarded-support per Theorem T18, Paper #093). This paper introduces and characterizes the second kernel rule-type: **V5**, the **cross-chain correlation kernel**. Given the postulated primitives P02, P04, P05, P07, P09, P10, P11, together with V1's finite-width retarded structure, V5 is characterized as the substrate kernel rule-type that mediates *correlation between distinct chains* with finite memory time $\tau_{V5}$, forward-causal support, and $U(1)$-gauge-compatible transport.

**Wedge claim (revised in this round).** V5 provides a **structural unification of formalism across regimes with different correlation times**: the same substrate kernel rule-type — with the same structural features (finite memory, retarded support, gauge-compatibility, Lorentz covariance) — supplies a unified substrate mechanism for non-Markovian behavior across three physical regimes: (i) Maxwell viscoelastic stress-relaxation in polymer melts and non-Newtonian fluids; (ii) the substrate-level cutoff producing the Hawking spectrum's trans-Planckian regularization at near-horizon scales; (iii) cross-chain entanglement-bandwidth modulation that controls Page-curve behavior and ER=EPR-class straddling at horizons.

**The regime-specific memory times $\tau_{V5}^{\mathrm{soft}}$, $\tau_{V5}^{\mathrm{BH}}$, $\tau_{V5}^{\mathrm{ent}}$ are inherited parameters, not predicted by the substrate.** Specifically, $\tau_{V5}^{\mathrm{soft}}$ is *identified with* the empirically-measured Maxwell relaxation time, and $\tau_{V5}^{\mathrm{BH}}$ is *chosen to match* the substrate scale $\ell_P/c$. These are operational identifications/matchings, not substrate-level predictions of the numerical values.

The Diffusion Coarse-Graining Theorem (DCGT) bridges substrate-level V5 to continuum constitutive laws in each regime. The paper is conditional: given the seven listed primitives + V1 inheritance, V5 is characterized; the primitives themselves are postulated. The cross-regime structural unification of formalism is the empirical case.

---

## 1. Introduction

### 1.1 What V5 is

V5 is a **substrate-level kernel rule-type** distinct from V1 (single-chain vacuum kernel, Papers #18 / #093) and distinct from matter rule-types (chain-carrying participation measures of Papers #1, #5). Where V1 mediates a single chain's vacuum response, V5 mediates **correlations between distinct chains** through the substrate. Operationally, V5 is the substrate-level mechanism by which one chain's participation content can influence another chain's participation content across substrate-graph distance, subject to finite memory time, forward-causal direction, and the gauge structure of P05–P09.

V5 is *not* a free-standing postulate of ED. It is a rule-type the substrate carries given the 13 postulated primitives + V1 inheritance: P10 (multiple structurally distinct rule-types) opens room for kernel rule-types beyond V1; P02 + P04 + P05 + P07 + P09 supply the structural mechanism for inter-chain correlation transport; P11 + V1's retardation supply the causal-direction constraint.

### 1.2 Why cross-chain kernels matter

Standard physics treats correlations between distinct subsystems via field-theoretic propagators. In ED's substrate ontology, there are no fundamental fields (ED-I-06); chains and channels are the primitive ontological objects, and correlations between distinct chains are mediated by *substrate-level kernel rule-types* rather than by continuum fields. V5 is the substrate-level analog of the cross-chain "field propagator" operating on the discrete participation graph rather than on a smooth continuum.

The interest of V5 — and the reason this paper exists as the first Wave-2 Generative Paper — is its **structural unification of formalism across regimes with different correlation times**: the same substrate rule-type (with the same structural features) provides a unified substrate mechanism for non-Markovian behavior across three physical regimes:

- **Soft-matter physics:** Maxwell viscoelastic stress relaxation in polymer melts, complex fluids, non-Newtonian rheology.
- **Black-hole physics:** the substrate-level cutoff at near-horizon scales that regularizes the Hawking spectrum's trans-Planckian extrapolation.
- **Quantum entanglement:** cross-chain bandwidth that controls entanglement-entropy growth, Page-curve behavior, ER=EPR-class straddling at horizons.

The three regimes have **different correlation times** ($\tau_{V5}^{\mathrm{soft}}$, $\tau_{V5}^{\mathrm{BH}}$, $\tau_{V5}^{\mathrm{ent}}$, all regime-specific inherited parameters), but the **substrate-level kernel structure is the same** in all three: finite memory, retarded support, gauge-compatibility, cross-chain operational form. This structural unification of formalism is the wedge claim of V5.

### 1.3 V5 in the kernel hierarchy

- **V1** (Papers #18 / Paper_093): single-chain vacuum response. Finite-width, retarded, Lorentz-covariant.
- **V5** (this paper): cross-chain correlation. Finite-memory $\tau_{V5}$, retarded, gauge-compatible.
- **N1-E, N2-E, N3-D** (future Wave-2 papers): memory-kernel cascade.
- **Lindblad limit** (future Wave-2 paper): Markovian coarse-grained limit of V1 + V5.

V1 and V5 are the two foundational kernels; the cascade and Lindblad limit are downstream of their joint action.

### 1.4 What this paper does

§2 lists primitive inputs. §3 defines V5. §4 establishes structural properties. §5 develops three regimes (soft-matter, Hawking, entanglement). §6 develops DCGT. §7 names what the paper does *not* claim. §8 lists falsification criteria. §9 is the position statement.

**Series context.** First Wave-2 Generative Paper after the 2026-05-13 pivot to the Generative Primitives System framing.

---

## 2. Primitive Inputs (postulated, not derived in this paper)

- **P02 (Participation as primitive relation).**
- **P04 (Bandwidth as non-negative additive scalar).**
- **P05 (Polarity-transport along edges).**
- **P07 (Channel structure as ontological primitive).**
- **P09 ($U(1)$-valued polarity).**
- **P10 (Rule-type primitive).**
- **P11 (Commitment irreversibility).**

**V1 inheritance:**

- V1 finite-width (Theorem N1, Paper #18).
- V1 retarded support (Theorem T18, Paper_093).

**Upstream paper dependencies:** Papers #1, #3, #5, #18, #093.

**No primitive forcing is invoked.**

---

## 3. Definition of the V5 Kernel

### 3.1 Participation-based definition

For two chains $C_A$, $C_B$ at distinct loci, V5 is:

$$
K_{V5}(u_A, t_A; u_B, t_B) = \theta(t_A - t_B)\, F_{V5}\!\left(\frac{\sigma(u_A, u_B; t_A, t_B)}{\ell_{V5}^2},\, \frac{t_A - t_B}{\tau_{V5}}\right)
$$

where:

- $\theta(t_A - t_B)$: Heaviside step enforcing retarded support (forward-causal from V1 via P11).
- $\sigma(u_A, u_B; t_A, t_B)$: substrate-level Synge function analog.
- $\ell_{V5}$: V5-characteristic spatial scale (regime-dependent; inherited from $\ell_{\mathrm{ED}}$ at substrate scale, renormalized in coarse-grained regimes via DCGT).
- $\tau_{V5}$: V5-characteristic memory time. **Regime-specific; inherited, not predicted (§3.3 below).**
- $F_{V5}$: V5 envelope function — bounded, decaying. The *form* (bounded, finite-width, retarded) is fixed by V5's substrate-rule-type identity; the *specific functional shape* (exponential, power-law, multi-scale) is value-layer content.

The cross-chain correlation acts:

$$
\langle X^A(u_A, t_A) \cdot Y^B(u_B, t_B)\rangle_{V5} = \int K_{V5}(u_A, t_A; u_B, t_B)\,\mathcal{Q}_{X,Y}^{AB}\,d\mu(\mathrm{intermediate}).
$$

### 3.2 Cross-chain correlation structure

V5 acts on **pairs of chains**, distinguishing it from V1 (single-chain operator). The two-chain character is essential; without V5, the substrate would have only V1 + matter rule-types, and cross-chain correlations would require either repeated V1 cascade (Markovian only) or substrate-level fundamental fields (forbidden by ED-I-06).

V5 provides a unified substrate mechanism for non-Markovian cross-chain correlation transport without invoking continuum fields. **The substrate mechanism is unified across regimes**; the specific $\tau_{V5}$ in each regime is inherited from value-layer empirical content.

### 3.3 Memory time $\tau_{V5}$ — regime-specific, inherited, not predicted

This section is revised in this round to clarify the postulational/empirical status of $\tau_{V5}$.

The memory-time parameter $\tau_{V5}$ controls cross-chain correlation decay:

$$
F_{V5}\!\left(\sigma/\ell_{V5}^2, t/\tau_{V5}\right) \xrightarrow{t/\tau_{V5} \to \infty} 0.
$$

**Structural content (substrate-derived):**

- The *existence* of a finite memory time is structural (forced by V1's finite-width inheritance + UV-finiteness of substrate primitives).
- The *form* of the V5 kernel (finite-memory, retarded, gauge-compatible, Lorentz-covariant) is structural.

**Value-layer content (inherited, not substrate-derived):**

- The *specific numerical value* of $\tau_{V5}$ in any given physical system is **inherited from value-layer empirical content**, not predicted by the substrate.
- The *specific decay profile* (exponential, power-law, multi-scale) within the structural class is inherited.

In the regime-specific evaluations of §5, three regime-specific values appear: $\tau_{V5}^{\mathrm{soft}}$, $\tau_{V5}^{\mathrm{BH}}$, $\tau_{V5}^{\mathrm{ent}}$. **All three are inherited parameters, not substrate predictions.** Specifically:

- **Soft-matter regime:** $\tau_{V5}^{\mathrm{soft}}$ is **identified with** the empirically-measured Maxwell relaxation time of polymer melts and non-Newtonian fluids ($\sim 10^{-3}$ s for typical samples). The substrate framework provides the operational mechanism (V5 cross-chain correlation); the numerical value is inherited from rheometry.

- **Black-hole / Hawking regime:** $\tau_{V5}^{\mathrm{BH}}$ is **chosen to match the substrate scale** $\ell_P/c \sim 10^{-44}$ s. This is a substrate-scale matching, not a substrate-level derivation: $\ell_P$ itself is empirically identified with $\ell_{\mathrm{ED}}$ via Newton-recovery (Paper_027), so $\tau_{V5}^{\mathrm{BH}} = \ell_P/c$ matches the substrate scale by construction. The Hawking-cutoff result of §5.2 is conditional on this matching.

- **Entanglement regime:** $\tau_{V5}^{\mathrm{ent}}$ is system-specific, inherited from the specific quantum-information context.

The substrate's structural prediction is that V5's memory time has a **consistent operational definition across regimes** (same substrate kernel rule-type, same structural features), but the **numerical value in any specific system is inherited from value-layer empirical content**.

### 3.4 Relation to V1

V5 inherits from V1:

1. **Finite-width support (V1 Theorem N1):** $F_{V5}$ bounded, decaying outside V5-characteristic scale. V5 has no $\delta$-function limit and no infinite-width limit.
2. **Retarded support (V1 Theorem T18 / Paper_093):** $K_{V5}$ has $\theta(t_A - t_B)$ support. Forced by the same P11 commitment-irreversibility argument that fixes V1's retardation. Advanced / symmetric V5 are excluded by the same substrate-operational compositional-closure arguments (Paper_093 §5.3, §6.4).

### 3.5 V5 is a substrate rule-type

By P10, V5 occupies the cross-chain-correlation slot in the kernel-rule-type category. V5 is not a matter rule-type, not a gauge rule-type — it is its own structural category alongside V1 and the future cascade kernels.

---

## 4. Structural Properties

### 4.1 Linearity

V5 acts linearly on cross-chain participation content.

### 4.2 Boundedness

V5 produces bounded cross-chain correlations.

### 4.3 Gauge-compatibility via P05 + P09

Under $U(1)$ gauge transformations, $K_{V5}$ transforms covariantly:

$$
K_{V5} \to e^{i(\alpha(u_A) - \alpha(u_B))}\,K_{V5}.
$$

### 4.4 Lorentz covariance

V5 transforms as a Lorentz scalar; envelope $F_{V5}$ depends on Lorentz-invariant separation. In curved spacetime, generalizes via Synge world-function on $g_{\mu\nu}$.

### 4.5 Rule-type identity via P10

V5 is a kernel rule-type alongside V1 in the rule-type category.

### 4.6 Retarded support and the kernel-level arrow

V5's retarded support inherits from V1 via P11 (Paper_093 §6.4 substrate-operational argument).

---

## 5. Cross-Domain Manifestations of V5

V5 provides a **unified substrate mechanism for non-Markovian behavior across regimes** with different correlation times. The three regimes have **different inherited $\tau_{V5}$ values** but share the **same substrate-level kernel formalism**.

### 5.1 Soft-matter Maxwell viscoelastic relaxation

**The phenomenon.** In polymer melts, complex fluids, and non-Newtonian rheology, stress relaxation follows the Maxwell law:

$$
\sigma(t) = \sigma_0\,e^{-t/\tau_{\mathrm{Maxwell}}}.
$$

In typical polymer-melt systems, $\tau_{\mathrm{Maxwell}}$ is in the $10^{-3}$ s range, varying with molecular weight, temperature, chemistry.

**The V5 identification (revised in this round to be explicit about identification vs. prediction).** Polymer-melt molecules are extended chain structures in the substrate sense (P02 + P07). Cross-chain correlations between distinct polymer molecules are mediated at the substrate level by V5. The substrate-level V5 envelope produces an exponential-decay form in the soft-matter regime:

$$
F_{V5}(\sigma/\ell_{V5}^2, t/\tau_{V5}^{\mathrm{soft}}) \sim e^{-t/\tau_{V5}^{\mathrm{soft}}}
$$

at large temporal separations. Through DCGT (§6), this becomes the continuum Maxwell stress-relaxation law.

**Identification of $\tau_{V5}^{\mathrm{soft}}$.** **$\tau_{V5}^{\mathrm{soft}}$ is identified with the empirically-measured Maxwell relaxation time $\tau_{\mathrm{Maxwell}}$, not predicted by the substrate.** Specifically:

- The substrate framework supplies the *operational mechanism* (V5 cross-chain correlation with exponential-envelope structural form) that produces the Maxwell stress-relaxation law via DCGT.
- The *numerical value* of $\tau_{V5}^{\mathrm{soft}}$ in any specific polymer system is inherited from rheometry — it is the empirically-measured Maxwell relaxation time for that system.
- ED does *not* predict the specific value of $\tau_{\mathrm{Maxwell}}$ from molecular structure (molecular weight, temperature, chemistry). That prediction would require additional substrate-level content connecting molecular structure to substrate-graph cross-chain correlation parameters, which is in-queue work.

**The substrate framework's structural prediction is therefore:** the **form** of stress-relaxation (exponential, Maxwell-type) in the soft-matter regime is a substrate-level structural consequence of V5's finite-memory envelope; the **value** of the relaxation time is inherited from value-layer empirical content.

**Arc-D context.** Substrate-level V5-Maxwell identification developed in Arc-D / DCGT memos (closed 2026-04-30).

### 5.2 Hawking-spectrum cutoff via imaginary-time periodicity

**The phenomenon.** Hawking radiation is thermal flux at $T_H = \kappa/(2\pi)$. Standard derivation requires extrapolation of matter-field modes to $\omega \to \infty$ — the trans-Planckian problem.

**The V5 identification (revised in this round to be explicit about the substrate-scale matching).** Near the horizon, V5 acts as the substrate-level cross-chain correlation kernel between chains carrying Hawking-radiation excitations and substrate near-horizon vacuum structure. V5 contributes the substrate-level KMS condition:

$$
\langle\phi(u_A, t_A)\phi(u_B, t_B)\rangle_{V5}^{\mathrm{Eucl}} = \langle\phi(u_A, t_A + i\beta_H)\phi(u_B, t_B)\rangle_{V5}^{\mathrm{Eucl}}, \quad \beta_H = 2\pi/\kappa,
$$

producing thermal Planck distribution at $T_H = 1/\beta_H = \kappa/(2\pi)$.

The cutoff frequency that regularizes the trans-Planckian extrapolation is set by V5's substrate-level memory time:

$$
\omega_c = \frac{1}{\tau_{V5}^{\mathrm{BH}}} \sim \frac{c}{\ell_P}.
$$

**The identification $\tau_{V5}^{\mathrm{BH}} = \ell_P/c$ is chosen to match the substrate scale, not derived from substrate-level analysis.** Specifically:

- The substrate framework requires V5's near-horizon memory time to be at the substrate scale (consistent with V5's substrate-level kernel-rule-type identity).
- $\ell_P$ is empirically identified with $\ell_{\mathrm{ED}}$ via Newton-recovery (Paper_027 §5.3); this is a value-layer empirical identification, not a substrate-level derivation.
- The matching $\tau_{V5}^{\mathrm{BH}} = \ell_P/c$ is therefore an **operational substrate-scale matching**, conditional on $\ell_{\mathrm{ED}} = \ell_P$.

If $\ell_{\mathrm{ED}}$ were identified with a different empirical scale, $\tau_{V5}^{\mathrm{BH}}$ would shift correspondingly. The Hawking-cutoff result is conditional on this matching.

**The substrate framework's structural content (independent of the specific numerical value):**

- V5 provides a substrate-level kernel mechanism that *structurally produces* a UV cutoff in the Hawking spectrum (from V5's finite-memory envelope).
- The cutoff frequency is the inverse of V5's near-horizon memory time, scaled to the substrate scale.
- The trans-Planckian extrapolation is not generated because V5-mediated cross-chain correlations cannot extrapolate to frequencies $\omega > 1/\tau_{V5}^{\mathrm{BH}}$.

The numerical value $\omega_c \sim c/\ell_P$ matches the physical Planck scale **because** the substrate framework identifies $\ell_{\mathrm{ED}}$ with $\ell_P$ — this is empirical matching, not substrate derivation.

**Arc-Hawking context.** Substrate-level V5-Hawking-cutoff developed in Arc-Hawking memos (H-4 closure 2026-05-09).

### 5.3 Entanglement-bandwidth modulation

**The phenomenon.** Entanglement entropy growth between subsystems is bounded by cross-chain correlation capacity. In black-hole physics, the Page curve describes entanglement-entropy growth and saturation. In condensed-matter physics, entanglement-entropy growth follows analogous patterns bounded by the Lieb-Robinson velocity.

**The V5 derivation.** Entanglement between chains $C_A$, $C_B$ is carried by V5-mediated cross-chain correlation content. Maximum entanglement-bandwidth growth rate:

$$
\frac{dS_E}{dt}\bigg|_{\max} = c_{V5} \cdot \frac{\sigma_{AB}}{\tau_{V5}^{\mathrm{ent}}}.
$$

V5's finite-memory structure produces entanglement-entropy saturation at a characteristic timescale related to $\tau_{V5}^{\mathrm{ent}}$.

In black-hole physics, Page-curve transition occurs at $t_{\mathrm{Page}} \sim \tau_{V5}^{\mathrm{ent}}(M)$; substrate-level mechanism for ER=EPR-class straddling. In condensed-matter, the Lieb-Robinson bound emerges as the DCGT continuum limit of V5.

**Empirical identification:** $\tau_{V5}^{\mathrm{ent}}$ is system-specific, **inherited from value-layer empirical content**, not predicted by the substrate.

**Arc-E context.** Arc-E memos (E-5 closure 2026-05-08).

### 5.4 The structural unification (summary)

V5 provides a unified substrate kernel rule-type with consistent structural features (finite memory, retarded, gauge-compatible, Lorentz-covariant) across three regimes with different inherited correlation times:

| Regime | $\tau_{V5}$ status | Substrate role |
|---|---|---|
| Soft-matter polymer melts | Identified with empirical $\tau_{\mathrm{Maxwell}}$ | V5 mechanism for Maxwell viscoelastic relaxation |
| Near-horizon black hole | Chosen to match substrate scale $\ell_P/c$ | V5 mechanism for Hawking spectrum cutoff |
| Entanglement (system-dependent) | Inherited from system | V5 mechanism for entanglement-bandwidth modulation |

**The structural unification of formalism is the wedge claim.** What V5 supplies across these regimes is the **same substrate kernel structure** (the same primitive content, the same kernel-rule-type identity, the same set of structural properties — finite memory, retarded support, gauge-compatibility, cross-chain operational form), with **regime-specific inherited correlation times**.

V5 is **not** claimed to *necessarily* underlie all non-Markovian behavior. Standard frameworks (polymer-chain reptation, mode-coupling theory, Lieb-Robinson bounds derived from microscopic Hamiltonians) provide alternative descriptions in their respective regimes. V5 provides a **unified substrate mechanism** for these phenomena — a single substrate-level kernel structure that produces these effects via DCGT. Whether V5 is the *only* possible substrate-level mechanism, or whether alternative substrate ontologies could supply equally consistent mechanisms, is open.

The empirical case for V5 (and for the 13-primitive ED ontology) is the structural unification of formalism: one substrate kernel rule-type doing structurally identical jobs in three regimes that differ in correlation time. This is the wedge content.

---

## 6. Diffusion Coarse-Graining (DCGT) and Continuum Constitutive Laws

DCGT (Arc-D closure 2026-04-30) bridges substrate-level V5 + V1 + matter-rule-type content to continuum constitutive laws in the hydrodynamic-window scale separation $\ell_{\mathrm{ED}} \ll R_{\mathrm{cg}} \ll L_{\mathrm{flow}}$.

### 6.1 V5 → Maxwell relaxation in soft matter

DCGT coarse-graining of V5 cross-chain correlations in soft-matter produces:

$$
G(t) = G_0\,e^{-t/\tau_{\mathrm{Maxwell}}}
$$

with $\tau_{\mathrm{Maxwell}}$ identified with the substrate-level $\tau_{V5}^{\mathrm{soft}}$ rescaled by the DCGT coarse-graining kernel. Krieger-Dougherty viscosity and Cross / Carreau / Bird-Carreau constitutive laws emerge as DCGT continuum limits.

### 6.2 V5 → propagator structure in QFT

DCGT coarse-graining of V5 in the QFT regime produces retarded / Feynman / advanced propagator hierarchy. V5's substrate-level UV cutoff at $\omega \sim 1/\tau_{V5}$ becomes standard QFT regulators (Pauli-Villars, dimensional, lattice) in the continuum limit. In near-horizon regime, V5's $\omega_c \sim c/\ell_P$ (matched to substrate scale, §5.2) provides the trans-Planckian cutoff.

### 6.3 V5 → Lieb-Robinson bound in condensed matter

DCGT coarse-graining in condensed-matter:

$$
v_{LR} = c_{V5}\cdot\frac{\ell_{V5}}{\tau_{V5}^{\mathrm{ent}}}.
$$

### 6.4 V5 → curved-spacetime entanglement at horizons

V5's curved-spacetime extension produces entanglement structure across horizons that ER=EPR-class arguments require: cross-chain correlations straddle the horizon, with committed structure (P11) interior-confined and uncommitted-entanglement amplitude straddling.

### 6.5 DCGT structural summary

DCGT applies to V5 wherever hydrodynamic-window scale separation holds. In each regime, the same substrate primitive produces a regime-specific continuum constitutive law via DCGT. The structural unification of formalism is preserved across these continuum limits.

---

## 7. What This Paper Does NOT Claim

### 7.1 The V5 memory time $\tau_{V5}$ is not predicted by the substrate

**Specific numerical values of $\tau_{V5}^{\mathrm{soft}}$, $\tau_{V5}^{\mathrm{BH}}$, $\tau_{V5}^{\mathrm{ent}}$ are inherited from value-layer empirical content, not predicted by the substrate**:

- $\tau_{V5}^{\mathrm{soft}}$ is identified with empirically-measured Maxwell relaxation time.
- $\tau_{V5}^{\mathrm{BH}} = \ell_P/c$ is chosen to match the substrate scale; $\ell_P$ itself is empirically identified with $\ell_{\mathrm{ED}}$ via Newton-recovery.
- $\tau_{V5}^{\mathrm{ent}}$ is system-specific, inherited.

The substrate's structural content is the **kernel form + structural features** (finite memory, retarded support, gauge-compatibility), not the numerical values.

### 7.2 The V5 envelope shape is not derived

The specific functional shape of $F_{V5}$ within the admissible class is value-layer content.

### 7.3 No coupling constants or masses are derived

V5 does not derive specific material constants, BH parameters, or entanglement-coupling coefficients. V5 produces the *structural form*; numerical content is value-layer inherited.

### 7.4 No uniqueness claim beyond the 13 primitives

V5's characterization is conditional on the postulated primitives + V1 inheritance. Other substrate ontologies could allow different cross-chain kernel structures.

### 7.5 No forcing of primitives

The seven primitives are postulated; not derived from a deeper layer.

### 7.6 No claim of derivation from nothing

Conditional on postulated primitives + V1 inheritance + upstream papers + DCGT.

### 7.7 No claim of superiority over standard cross-correlation physics

Standard QFT propagators, soft-matter Maxwell viscoelasticity, Lieb-Robinson bound are empirically successful. V5 does not "replace" them — V5 produces them via DCGT and provides a **unified substrate mechanism for non-Markovian behavior across regimes**. The regime-specific continuum laws are inherited and DCGT-derived from V5.

### 7.8 V5 is not claimed as the only possible substrate-level mechanism

V5 provides a unified substrate mechanism for non-Markovian behavior across regimes — within the 13-primitive ED ontology. **V5 is not claimed as necessary for non-Markovian dynamics in some absolute sense.** Standard frameworks (polymer reptation, mode-coupling theory, microscopic Lieb-Robinson derivations) supply alternative descriptions in their respective regimes; V5's distinctive content is the *substrate-level unification of formalism* across these regimes within ED's ontology.

---

## 8. Falsification Criteria

### 8.1 Failure of structural unification of formalism

**Discovery that soft-matter Maxwell relaxation, Hawking spectrum cutoff, and entanglement-bandwidth modulation cannot be described by a single substrate-level kernel formalism with consistent structural features (finite memory, retarded support, gauge-compatibility, cross-chain operational form) — even after accounting for regime-specific $\tau_{V5}$ — would falsify V5's structural unification claim.**

The falsification would take the form of demonstrating that the substrate-level structural features differ across the three regimes in a way that cannot be reconciled with a single kernel rule-type. For example:

- Soft-matter Maxwell exhibits non-finite-memory behavior at substrate scale that contradicts V5's finite-memory structure.
- Hawking-cutoff structure exhibits non-gauge-compatible behavior contradicting V5's $U(1)$-covariance.
- Entanglement-bandwidth modulation exhibits non-retarded behavior contradicting V5's forward-causal support.

The current state of empirical content is **consistent with single-substrate-kernel structural-formalism unification** across the three regimes. Tighter cross-regime empirical comparison could either confirm or falsify.

### 8.2 Observation of independent structural-formalism mechanisms for the three regimes

Specific empirical observations that would falsify V5's structural unification:

- Substrate-level structural features (memory, support, gauge, Lorentz) differing between soft-matter and entanglement contexts.
- Hawking spectrum cutoff exhibiting non-V5-compatible structural features.
- Entanglement-bandwidth modulation exhibiting non-V5-compatible structural features.

### 8.3 Observation of advanced V5 support

Discovery of cross-chain correlations carrying advanced (backward-causal) support at the substrate level would falsify V5's retarded character (§4.6 + Paper_093).

### 8.4 Breakdown of structural identifications

- **Soft-matter:** discovery that Maxwell-type stress relaxation has structurally non-V5 substrate origin would falsify the V5 identification of §5.1.
- **Hawking:** discovery that the trans-Planckian cutoff is at a frequency inconsistent with $\omega_c = 1/\tau_{V5}^{\mathrm{BH}}$ (at the substrate-scale matching) would falsify the V5 mechanism of §5.2.

### 8.5 Breakdown of gauge-compatibility

Cross-chain correlations between gauge-coupled chains failing to transform covariantly under $U(1)$ gauge transformations would falsify §4.3.

### 8.6 Substrate-level kernel without V5

**Discovery that the substrate-level kernel hierarchy can be exhausted by V1 alone (without V5) — i.e., that all observed cross-chain correlation phenomena can be derived from V1 composed across intermediate chains via Markovian cascade — would falsify V5's structural role within the substrate framework**, although it would not directly falsify the empirical phenomena V5 describes (which would be reattributed to V1-only cascade in such a counterfactual).

Current state: empirical non-Markovian cross-chain correlation structure is structurally inconsistent with single-V1 cascade composition (V5 supplies a unified substrate mechanism for non-Markovian behavior that V1-only cascade cannot supply within ED's ontology). Falsification would require demonstrating that empirical non-Markovian correlations *can* be reduced to V1-only cascades.

---

## 9. Position Statement

V5 is a **substrate kernel rule-type** in the 13-Primitive Generative Substrate Ontology. V5's identity is *conditional* on the postulated primitives P02 + P04 + P05 + P07 + P09 + P10 + P11 + V1 inheritance + upstream Wave-1 papers + DCGT.

**V5's wedge content** — and the reason this paper exists as the first Wave-2 Generative Paper — is the **structural unification of formalism across regimes with different correlation times**. V5 provides a unified substrate kernel rule-type — with consistent structural features (finite memory, retarded support, gauge-compatibility, Lorentz-covariance, cross-chain operational form) — that serves as a unified substrate mechanism for non-Markovian behavior across three physical regimes:

- Soft-matter Maxwell viscoelastic relaxation ($\tau_{V5}^{\mathrm{soft}}$ identified with empirically-measured Maxwell relaxation time).
- Hawking-spectrum cutoff ($\tau_{V5}^{\mathrm{BH}} = \ell_P/c$ chosen to match the substrate scale).
- Entanglement-bandwidth modulation ($\tau_{V5}^{\mathrm{ent}}$ system-specific, inherited).

The three regimes have different correlation times — **all inherited parameters, not substrate predictions**. The substrate-level structural features (kernel form, memory, support, gauge-covariance) are the same in all three. This structural unification of formalism — a single substrate kernel rule-type underlying all three — is the wedge claim.

What the paper does *not* claim:

- The primitives are not derived; they are postulated.
- $\tau_{V5}$ values are inherited from value-layer empirical content, not substrate predictions.
- V5 is not claimed as necessary for non-Markovian dynamics in some absolute sense; standard regime-specific frameworks supply alternative descriptions. V5's distinctive content is the *substrate-level unification of formalism* across regimes.
- V5 does not replace standard continuum cross-correlation physics — it provides a unified substrate mechanism that, through DCGT, recovers standard continuum laws in each regime.
- The Hawking cutoff scale $\omega_c \sim c/\ell_P$ matches the physical Planck scale **because** the substrate framework identifies $\ell_{\mathrm{ED}}$ with $\ell_P$ (Paper_027 §5.3); this is empirical matching, not substrate derivation.

V5 is offered for empirical engagement on these terms: a substrate primitive whose cross-regime structural-formalism unification is the empirical case, and whose specific numerical values are inherited from value-layer empirical content.

**Series context.** First Wave-2 Generative Paper. Wave-2 continues with Paper #21 (Memory-Kernel Cascade), Paper #22 (Lindblad Limit), Paper #23 (Kernel Hierarchy Structural Unification).

---

## Appendix: Cross-References and Glossary

### Cross-references

- **Position paper:** `paper_ED_Framework_13_Primitive_Generative_System.md`.
- **Primitive load-bearing audit:** `PRIMITIVE_LOAD_BEARING_AUDIT.md`.
- **Paper #1 (Participation Measure), #3 (Inner Product), #5 (Gauge T17).**
- **Paper #18 (V1 N1), Paper_093 (T18):** kernel inheritance.
- **Paper_027 (Newton's $G$):** empirical identification $\ell_{\mathrm{ED}} = \ell_P$ that the §5.2 Hawking matching uses.
- **Arc-D (DCGT closure 2026-04-30):** substrate-to-continuum bridge.
- **Arc-Hawking (H-4 closure 2026-05-09):** Hawking-cutoff via V5 KMS.
- **Arc-E (E-5 closure 2026-05-08):** entanglement-bandwidth via V5.

### Glossary

- **V5 (cross-chain correlation kernel rule-type).** Substrate kernel rule-type mediating correlations between distinct chains.
- **Kernel rule-type.** Category of substrate rule-types whose participation content is correlation amplitude between chains or substrate-graph regions. Includes V1, V5, future cascade kernels.
- **Memory time $\tau_{V5}$.** V5-characteristic temporal scale. **Regime-specific; inherited from value-layer empirical content, not substrate-predicted.**
- **V5 envelope $F_{V5}$.** Bounded, decaying function defining V5's specific functional form. Structural form fixed; specific shape inherited.
- **Structural unification of formalism across regimes.** V5's cross-regime substrate-level structural-feature consistency: same substrate kernel rule-type, same structural features, different inherited correlation times. The empirical case for V5.
- **Unified substrate mechanism for non-Markovian behavior.** What V5 provides across regimes — one substrate-level kernel structure that supplies non-Markovian effects across diverse physical contexts.
- **DCGT (Diffusion Coarse-Graining Theorem).** Substrate-to-continuum bridge. Arc-D closure 2026-04-30.
- **Imaginary-time periodicity.** Substrate-level KMS condition V5 imposes in Euclidean near-horizon BH geometry; produces Hawking spectrum at $T_H = \kappa/(2\pi)$.
- **Lieb-Robinson velocity.** DCGT continuum-limit bound on entanglement-content propagation from V5's finite-memory cross-chain correlation.
- **ER=EPR-class straddling.** V5-mediated cross-chain correlations spanning event horizons; substrate-level mechanism for BH information-paradox structural avoidance.
- **Substrate-scale matching.** Operational identification of a V5 regime-specific memory time with a substrate scale, conditional on prior substrate-scale empirical identifications (e.g., $\ell_{\mathrm{ED}} = \ell_P$).
- **Empirical identification.** Operational identification of a V5 regime-specific memory time with an empirically-measured timescale (e.g., $\tau_{V5}^{\mathrm{soft}} = \tau_{\mathrm{Maxwell}}$).

---

**End of Paper_090.**

*Wave-2 Generative Paper — Wedges / Kernel Arc, Foundation. Round-2 revision: wedge claim reframed from "structural unification across ~40 orders of magnitude" to "structural unification of formalism across regimes with different correlation times"; §3.3 clarifies $\tau_{V5}^{\mathrm{soft}}/\tau_{V5}^{\mathrm{BH}}/\tau_{V5}^{\mathrm{ent}}$ are inherited parameters, not substrate predictions; §5.1 reframes Maxwell identification as $\tau_{V5}^{\mathrm{soft}}$ identified with empirical Maxwell relaxation time (not predicted); §5.2 reframes Hawking cutoff as $\tau_{V5}^{\mathrm{BH}} = \ell_P/c$ chosen to match the substrate scale (conditional on the $\ell_{\mathrm{ED}} = \ell_P$ empirical identification), not derived; §7.8 + §9 + glossary remove "necessary for non-Markovian dynamics" claims and replace with "V5 provides a unified substrate mechanism for non-Markovian behavior across regimes."*
