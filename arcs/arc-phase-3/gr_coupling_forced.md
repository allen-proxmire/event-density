# Structurally FORCED Curvature-Coupling Structures

**Phase-3 Stage GR.2 — FORCED Evaluation Memo**
**Status:** Evaluation memo. Headline verdict: **GR-2A (V1 with Synge world function $\sigma(x, x')$) is FORCED at primitive level by Theorem N1 + general covariance + the Hadamard-parametrix argument — Theorem GR1, ED's first FORCED gravitational-sector structural theorem.** Three secondary items are FORCED-conditional via cascading: GR-3A (free-chain geodesic worldlines), GR-2D (curvature-dependent cross-chain correlations via V5 inheritance from GR-2A), GR-4D (curvature-induced vacuum backreaction in existence sense). Sixteen remaining items are NOT FORCED at Stage GR.2 — they are ADMISSIBLE-NOT-FORCED, with REFUTED determinations deferred to Stage GR.3. Total Stage GR.2 outcome: **1 unconditionally FORCED + 3 FORCED-conditional + 16 NOT-FORCED.** ED-Phys-10 acoustic-metric guardrails preserved; GR-4A Einstein-like emergence remains SPECULATIVE; GR-4C acoustic-metric-only baseline retained.

---

## 1. Evaluation Frame

### 1.1 Definition of FORCED in Phase-3

A curvature-coupling structure is FORCED at primitive level iff *all three* hold:

(a) **Consistency:** the structure is consistent with ED Primitives 01–13, Phase-2 structural theorems (spin-statistics R.2.5, GRH unconditional Q.1+Q.8, canonical (anti-)commutation Q.7, UV-FIN Q.8), Arc N's Theorem N1 (V1 forced), and ED-Phys-10's kinematic acoustic-metric content.

(b) **Necessity:** at least one of:
  - A primitive constraint *requires* the structure to be present in curved spacetime.
  - Removing the structure leads to inconsistency with a Phase-2 / Arc N theorem under curved-spacetime extension.
  - The structure is the unique generally-covariant generalisation of a flat-space FORCED result (e.g., V1 in flat space → V1 with Synge world function in curved space).

(c) **Constraint compliance:** the structure satisfies C1 (Lorentz / general covariance), C2 (spin-statistics preservation), C3 (UV-FIN preservation), and locality (Primitive 11).

A structure that satisfies (a) and (c) but not (b) is **ADMISSIBLE-NOT-FORCED**: consistent and constraint-compliant but not structurally required. A structure that fails (c) is REFUTED at Stage GR.3.

### 1.2 The "natural generalisation" criterion

A flat-space FORCED result extends to a curved-spacetime FORCED result iff its forcing argument depends only on **metric-independent primitives** (event-discreteness, finite proper-time intervals, bandwidth boundedness) plus **Lorentz / general covariance**. The flat-space forcing argument generalises by replacing flat-space invariants (e.g., $(x - x')^2$) with their curved-spacetime analogues (e.g., Synge's world function $\sigma(x, x')$).

This is the **Hadamard-parametrix criterion**: structures whose flat-space forcing argument depends only on metric-independent primitives + invariants extend to curved spacetime via the standard QFT-on-curved-spacetime construction. V1 satisfies this criterion (Theorem N1's forcing depends on Primitive 01 + Primitive 13 + Lorentz scalars, all metric-independent or generally-covariant).

### 1.3 Expected outcome distribution

Per Phase-3 opening §7.1 (45% partial GR-induce):

- 1–3 unconditionally FORCED items.
- 1–3 FORCED-conditional items.
- 14–18 NOT-FORCED items.

This memo confirms the prior with **1 unconditionally FORCED + 3 FORCED-conditional + 16 NOT-FORCED**, lying in the partial-GR-induce quadrant of the prior.

---

## 2. Special Analysis: GR-2A (V1 with Synge World Function)

GR-2A is the cleanest Phase-3 FORCED candidate. Detailed analysis follows.

### 2.1 The flat-space forcing argument (recap)

Theorem N1 (Stage N.5 §2) establishes V1 FORCED in flat Minkowski space via three legs:

- **(Leg 1) UV-FIN:** δ-function vacuum response amplifies high-frequency contributions; Primitive 01 event-discreteness imposes a primitive-level resolution scale $\ell_\mathrm{ED}$; Primitive 13 supplies finite proper-time intervals. Joint conclusion: kernel must have finite, non-zero width.
- **(Leg 2) Lorentz-covariance + locality:** kernel must decay at large separations (constant kernel implies infinite correlation length, breaks locality).
- **(Leg 3) UV-FIN refinement:** kernel must have sub-power-law-2 short-distance behaviour ($\alpha < 2$ in 3+1D).

The flat-space kernel is $K_\mathrm{vac}(x - x') = K_\mathrm{vac}^\mathrm{prim}((x - x')^2 / \ell_\mathrm{ED}^2)$, depending only on the Lorentz invariant $(x - x')^2$.

### 2.2 Extension to curved spacetime via Synge's world function

In curved spacetime, the natural generalisation of $(x - x')^2$ is **Synge's world function**:
$$
\sigma(x, x') = \tfrac{1}{2} \cdot (\text{squared geodesic distance from } x \text{ to } x'),
$$
defined wherever a unique geodesic connects $x$ and $x'$. In flat space, $\sigma(x, x') = \tfrac{1}{2}(x - x')^2$, recovering the flat-space invariant. In curved spacetime, $\sigma$ is the unique generally-covariant scalar two-point function that reduces to the flat-space invariant in the flat limit.

The natural curved-spacetime generalisation of V1 is therefore:
$$
\boxed{K_\mathrm{vac}^\mathrm{curved}(x, x') = K_\mathrm{vac}^\mathrm{prim}\bigl(\sigma(x, x') / \ell_\mathrm{ED}^2\bigr).}
$$
This is the **GR-2A** structure.

### 2.3 The forcing argument extends

We evaluate whether each of Theorem N1's three legs extends to curved spacetime under the GR-2A construction.

**(Leg 1, extended) UV-FIN in curved spacetime.** Arc Q's UV-FIN argument (Stage Q.8 §5.2) operates by primitive-level finiteness of multi-chain participation integrals via Primitive 01 event-discreteness + Primitive 13 finite proper-time intervals + Primitive 04 bounded bandwidth. Each of these primitives is **metric-independent**: they operate on the underlying event manifold regardless of whether curvature is present. UV-FIN therefore extends to curved spacetime unchanged.

In curved spacetime, a δ-function vacuum response $K_\mathrm{vac}^\mathrm{curved}(x, x') \propto \delta_g^{(4)}(x, x')$ (where $\delta_g$ is the covariant Dirac distribution) carries the same UV-amplification pathology as its flat-space counterpart — the Fourier transform with respect to a local inertial frame at $x$ produces a constant frequency-weighting, threatening UV-FIN at any spacetime point. The δ-curved limit is REFUTED for the same reason V1-δ is REFUTED in flat space.

Therefore Leg 1 forces finite-width kernel in curved spacetime.

**(Leg 2, extended) General covariance + locality.** Constant kernels $K_\mathrm{vac}^\mathrm{curved}(x, x') = c_\infty$ for all $x, x'$ have the same pathology in curved spacetime as in flat: infinite correlation length breaks Primitive 11 locality. The curved-spacetime extension of locality is generally-covariant locality — commitment events remain point-events on the event manifold regardless of curvature.

Therefore Leg 2 forces decaying kernel support in curved spacetime.

**(Leg 3, extended) UV-FIN refinement in curved spacetime.** The 3+1D power-counting argument from Leg 3 ($\alpha < 2$ for $|z|^{-2\alpha}$ kernel in 3+1D) operates locally — it depends on the dimensionality of spacetime at the event-resolution scale, not on global curvature. In any 3+1-dimensional spacetime, near each event the local dimensionality is 3+1D, and the power-counting argument applies pointwise to $\sigma(x, x') / \ell_\mathrm{ED}^2$ in place of $(x - x')^2 / \ell_\mathrm{ED}^2$.

Therefore Leg 3 forces sub-power-law-2 short-distance behaviour for $K_\mathrm{vac}^\mathrm{curved}$.

**(Conclusion).** All three legs of Theorem N1's forcing argument extend to curved spacetime under GR-2A. The kernel $K_\mathrm{vac}^\mathrm{curved}(x, x') = K_\mathrm{vac}^\mathrm{prim}(\sigma(x, x') / \ell_\mathrm{ED}^2)$ is structurally FORCED.

### 2.4 Theorem GR1 — V1 with Synge World Function FORCED

> **Theorem GR1 (V1 in Curved Spacetime FORCED).** *In curved spacetime where unique geodesics connect any two events $x, x'$, the vacuum-response kernel is structurally FORCED at primitive level to take the form*
> $$K_\mathrm{vac}^\mathrm{curved}(x, x') = K_\mathrm{vac}^\mathrm{prim}\bigl(\sigma(x, x') / \ell_\mathrm{ED}^2\bigr),$$
> *with $\sigma(x, x')$ Synge's world function (one-half squared geodesic distance), $K_\mathrm{vac}^\mathrm{prim}$ a function of admissibility class identical to the V1 flat-space class (finite, non-zero, decaying, sub-power-law-2 in argument), and $\ell_\mathrm{ED}$ the primitive event-discreteness scale. The flat-space V1 forcing argument (Theorem N1) extends to curved spacetime via Hadamard-parametrix-style construction.*

**Sketch of proof.** Per §2.3, all three legs of Theorem N1's flat-space forcing argument extend to curved spacetime under the natural Synge-world-function generalisation. Specifically:
1. UV-FIN (Theorem Q3) is metric-independent.
2. Primitive 01 event-discreteness is metric-independent.
3. Primitive 13 finite proper-time intervals generalise to affine-parameter intervals on geodesics.
4. Lorentz covariance generalises to general covariance.
5. The 3+1D power-counting argument for sub-power-law-2 kernels applies pointwise.

The Hadamard parametrix construction in QFT-on-curved-spacetime [4, 5] supplies the standard mathematical infrastructure: $\sigma(x, x')$ is the unique generally-covariant scalar two-point function reducing to $\tfrac{1}{2}(x - x')^2$ in the flat limit. Under GR-2A, V1's curved-spacetime form is unique up to specific functional realisation (which remains INHERITED). $\square$

**Dependencies on primitives + theorems.** Primitive 01; Primitive 04; Primitive 13; Primitive 11 (locality); Primitive 06 generalised to general covariance; Theorem N1 (V1 flat-space forced); Theorem Q3 (UV-FIN); ED-Phys-10 acoustic metric (or any proposed dynamical metric admitting unique geodesics).

### 2.5 Status

**Theorem GR1 is ED's first FORCED gravitational-sector structural theorem.** It takes its place in the ED structural inventory alongside the eight Phase-2 + Arc N FORCED theorems (Stage N.5 §8.1), now extended to nine.

The **class** of admissible $K_\mathrm{vac}^\mathrm{curved}$ kernels is FORCED; the **specific functional form** within the class (curved-space analogues of V2 exponential, V3 with $\alpha < 2$ power-law, V4 multi-scale) is INHERITED. This preserves the form-FORCED / value-INHERITED methodology established in Phase-2 + Arc N.

### 2.6 Cascading FORCED-conditional items

Theorem GR1 propagates FORCED-conditional status to several Phase-3 catalogue items via the curved-spacetime V1 cascade:

- **GR-2D (curvature-dependent cross-chain correlations):** V5 in flat space is FORCED-conditional-on-V1 in existence sense (Arc N). In curved spacetime, V5 inherits Synge-world-function structure via GR-2A, making cross-chain correlations naturally curvature-dependent. **FORCED-conditional via cascade.**
- **GR-2B (curvature-dependent kernel width):** if event-discreteness scale $\ell_\mathrm{ED}$ is itself curvature-dependent, V1's width inherits this dependence. The forcing argument does NOT require $\ell_\mathrm{ED}$ to depend on curvature — a constant $\ell_\mathrm{ED}$ is admissible — so GR-2B is **NOT FORCED** but admissible as a refinement.

---

## 3. GR-3A — Free-Chain Geodesic Worldlines (Detailed)

GR-3A is the second-most-likely FORCED candidate per Phase-3 opening expected verdict.

### 3.1 The free-chain condition

A "free chain" in Phase-2 satisfies:
- No commitment events along $\gamma_K$ (Primitive 11).
- No individuation pairing with other chains (Primitive 10).
- No gauge coupling to gauge rule-types (Phase-2 R.1 minimal coupling switched off).
- Pure Klein-Gordon (Case P) or Dirac (Case R) free-particle equations apply.

In flat Minkowski space, free chains follow straight lines (geodesics of $\eta_{\mu\nu}$). In curved spacetime, the question is whether free chains follow geodesics of the emergent acoustic metric $g^\mathrm{ac}_{\mu\nu}$.

### 3.2 The structural argument

Stage R.1's Klein-Gordon equation $(\Box + m^2 c^2/\hbar^2) \Psi = 0$ generalises to curved spacetime as
$$
(\Box_g + \xi R + m^2 c^2/\hbar^2) \Psi = 0,
$$
with $\Box_g = g^{\mu\nu} \nabla_\mu \nabla_\nu$ the curved-spacetime d'Alembertian and $\xi$ a non-minimal curvature coupling. In the **eikonal approximation** (high-frequency limit), the WKB-style solution $\Psi(x) \propto \exp(iS(x)/\hbar)$ with $S$ the action, the eikonal equation
$$
g^{\mu\nu} \partial_\mu S \, \partial_\nu S = m^2 c^2,
$$
yields equations of motion for $S$-characteristic worldlines that are **geodesics** of $g_{\mu\nu}$ — the standard derivation of geodesic motion from KG / Dirac in curved spacetime.

Stage R.3's Dirac equation similarly yields geodesic motion in the eikonal limit (Foldy-Wouthuysen + WKB analysis on curved background).

### 3.3 The forcing claim

Combining §3.1 and §3.2: free-chain worldlines satisfy KG / Dirac equations in curved spacetime; in the eikonal approximation, these equations force geodesic motion on the metric $g_{\mu\nu}$. If $g_{\mu\nu}$ is identified with the ED-Phys-10 emergent acoustic metric $g^\mathrm{ac}_{\mu\nu}$, then free-chain worldlines are geodesics of $g^\mathrm{ac}_{\mu\nu}$.

The conditional structure: GR-3A is FORCED *conditional on* the identification $g_{\mu\nu} = g^\mathrm{ac}_{\mu\nu}$, i.e., conditional on free chains "feeling" the acoustic metric rather than some other geometric structure. This identification is itself the natural ED-Phys-10 hypothesis but not unconditionally FORCED at primitive level.

### 3.4 Verdict

**GR-3A: FORCED-CONDITIONAL on the acoustic-metric identification.** The geodesic motion of free chains follows from KG / Dirac equations on curved spacetime in the eikonal limit; the metric appearing in those equations is the natural curved-spacetime extension of the flat-space Minkowski metric, which in ED-Phys-10's framework is the acoustic effective metric. Specific identification details (whether the rule-type-dependent curvature coupling $\xi$ varies with rule-type, whether the equivalence-principle analogue holds across all rule-types) are sub-questions deferred to Stage GR.3 / GR.4.

**Dependencies:** ED-Phys-10 acoustic metric; Stage R.1 Klein-Gordon; Stage R.3 Dirac; Primitive 02 worldline structure; Primitive 13 proper time / affine parameter; eikonal-limit / WKB approximation framework.

---

## 4. Bandwidth-Curvature Sector (GR-1) Evaluation

### 4.1 GR-1A — Curvature-dependent bandwidth evolution

**Evaluation.** A direct $\xi_X R \cdot b_K^X$ coupling term in the bandwidth equation of motion is structurally admissible — non-minimal scalar-curvature coupling is a standard QFT-on-curved-spacetime construction. However, no primitive-level argument *requires* such a coupling: the minimal coupling $\Box \to \Box_g$ is sufficient for general covariance. The non-minimal coupling $\xi_X$ is rule-type / band-coupling data (INHERITED), not primitive-derived.

**Verdict:** **NOT FORCED.** Minimal-coupling alternative admissible.

### 4.2 GR-1B — Curvature-modified σ_τ structure

**Evaluation.** Arc M's σ_τ master formula in curved spacetime acquires generally-covariant form: $\sigma_\tau = \hbar \sqrt{\Sigma_X w_\tau^X \langle (\nabla_\mu \ln b_\tau^X)(\nabla^\mu \ln b_\tau^X) \rangle_\tau}$. The Lorentz-scalar product becomes the metric-contracted scalar product. This is the natural generally-covariant generalisation. However, *additional* curvature corrections (e.g., explicit $\zeta_\tau R \cdot \sigma_\tau$ shift) are NOT FORCED — they are admissible refinements with $\zeta_\tau$ INHERITED.

**Verdict:** **NOT FORCED for the explicit-curvature-shift form.** The generally-covariant σ_τ form is itself a natural extension and not a new FORCED claim — it is the curved-spacetime version of Theorem M1.

### 4.3 GR-1C — Curvature-dependent bandweights

**Evaluation.** Spacetime-dependent bandweights $w_\tau^X(x)$ are admissible if generally covariant. However, no primitive-level argument forces $w_\tau^X$ to vary with curvature: rule-type bandweights are Lever L1 data that can equally well be globally constant. Phase-2 + Arc N derivations consistently use constant $w_\tau^X$ without inconsistency.

**Verdict:** **NOT FORCED.**

### 4.4 GR-1D — Curvature-dependent Fierz-class effects

**Evaluation.** Curvature-induced Fierz-class shifts are admissible structurally but not forced. The Cl(3,1) frame algebra is metric-independent; in curved spacetime it generalises to a tetrad-frame Clifford algebra without changing the algebraic structure. Curvature-induced Fierz-class admixtures could in principle occur but are not primitive-required.

**Verdict:** **NOT FORCED.** Sub-cases violating C2 Fierz TYPE preservation potentially REFUTED at GR.3.

### 4.5 GR-1E — Curvature-dependent Case-P/R distinctions

**Evaluation.** Stage R.2.5's spin-statistics theorem $\eta = (-1)^{2s}$ is unconditional FORCED at primitive level; Stage R.2.3's π_1(Q_2) = ℤ_2 topological theorem holds in any 3+1D spacetime with locally Minkowski tangent structure. Curvature-induced modifications of Case-P/R distinctions would violate both theorems.

**Verdict:** **NOT FORCED.** Likely REFUTED at GR.3 by C2.

---

## 5. Vacuum-Curvature Sector (GR-2) Evaluation

### 5.1 GR-2A — V1 with Synge world function

Per §2: **GR-2A is unconditionally FORCED** at primitive level. **Theorem GR1.**

### 5.2 GR-2B — Curvature-dependent kernel width

**Evaluation.** A curvature-dependent V1 kernel width $\tau_\mathrm{vac}(x) = \tau_\mathrm{vac}|_\mathrm{flat} \cdot f(R)$ is admissible structurally but not unconditionally forced. Theorem GR1 forces V1 in curved spacetime via Synge-world-function generalisation; this fixes the *kernel form* but does not require its *width* to depend explicitly on curvature beyond what enters through $\sigma(x, x')$. The event-discreteness scale $\ell_\mathrm{ED}$ may or may not be itself curvature-dependent — this is a separate primitive-level question not yet settled.

**Verdict:** **NOT FORCED unconditionally.** Curvature-dependence of $\ell_\mathrm{ED}$ is admissible but not forced.

### 5.3 GR-2C — Curvature-dependent kernel amplitude

**Evaluation.** Curvature-dependent kernel amplitude $A_\mathrm{vac}(R)$ multiplying the Theorem-GR1 form is admissible but not forced. Constant amplitude (relative to the metric-induced volume element) is the structurally simpler choice and is admissible. No primitive forces curvature-dependent amplitude.

**Verdict:** **NOT FORCED.**

### 5.4 GR-2D — Curvature-dependent cross-chain correlations

**Evaluation.** V5 (cross-chain correlations) is FORCED-conditional-on-V1 in flat space (Stage N.2 + N.5). Under Theorem GR1, V5's curved-spacetime extension inherits Synge-world-function structure: cross-chain correlations between events $x_1, x_2$ depend on $\sigma(x_1, x_2)$. This is the natural extension and is FORCED-conditional on Theorem GR1 + flat-space V5 existence claim.

Specifically: if V5 cross-chain correlations exist in flat space (FORCED-conditional-on-V1 in existence sense), and Theorem GR1 forces V1's curved-spacetime form, then V5's curved-spacetime form follows as the natural generalisation.

**Verdict:** **FORCED-CONDITIONAL via cascade from Theorem GR1.** Cross-chain correlation amplitudes still INHERITED.

### 5.5 GR-2E — Curvature-dependent vacuum-polarisation structure

**Evaluation.** Arc Q.5 vacuum-polarisation structure in curved spacetime acquires generally-covariant form via Theorem GR1's V1 in curved spacetime (form-factor structure inherited from $K_\mathrm{vac}^\mathrm{curved}$). Transversality $q_\mu \Pi^{\mu\nu}(q) = 0$ is preserved (Arc Q.5 + GRH-3 carryover; generally-covariant Lorentz-scalar form preserves transversality). However, *explicit additional* curvature couplings beyond what enters through Theorem GR1 are NOT FORCED.

**Verdict:** **NOT FORCED unconditionally.** The natural generally-covariant extension is FORCED via Theorem GR1; additional explicit-curvature corrections INHERITED.

---

## 6. Worldline-Curvature Sector (GR-3) Evaluation

### 6.1 GR-3A — Free chains follow geodesics of emergent metric

Per §3: **GR-3A is FORCED-CONDITIONAL** on the acoustic-metric identification.

### 6.2 GR-3B — Curvature-dependent commitment thresholds

**Evaluation.** Curvature-dependent individuation thresholds are admissible structurally but not forced. A constant threshold (independent of curvature) is the simpler and structurally consistent choice — Phase-2 + Arc N derivations all use constant thresholds. Sub-cases with curvature-dependent thresholds in Case-R sectors potentially violate C2 (Pauli exclusion), paralleling the Stage N.3 §2.2 N2-B Case-R refutation.

**Verdict:** **NOT FORCED.** Case-R sub-cases potentially REFUTED at GR.3.

### 6.3 GR-3C — Curvature-dependent adjacency graphs

**Evaluation.** Curvature-dependent multi-chain adjacency relations are admissible but not forced. Constant adjacency relations (independent of curvature) are admissible.

**Verdict:** **NOT FORCED.**

### 6.4 GR-3D — Curvature-dependent memory kernels

**Evaluation.** Curvature-dependent Arc N memory kernels (N1-A, N2-A/C, N3-A/B in curved spacetime) acquire generally-covariant form naturally via Theorem GR1's Synge-world-function structure for V1-related kernels. *Additional explicit* curvature coupling for non-V1 memory kernels (those not directly tied to vacuum response) is NOT FORCED — these kernels are themselves ADMISSIBLE-NOT-FORCED at Arc N closure (Stage N.5).

**Verdict:** **NOT FORCED.** Generally-covariant extension is FORCED via Theorem GR1 for V1-coupled kernels only.

### 6.5 GR-3E — Curvature-dependent null-cone deformation

**Evaluation.** ED-Phys-10's acoustic-metric construction already produces curvature-dependent null-cone structure: bandwidth-mode propagation speeds $c_s(x)$ depend on local bandwidth-flow content, which in turn depends on curvature. This is a kinematic feature of ED-Phys-10, not a new Phase-3 result.

**Verdict:** **NOT FORCED at Phase-3 level** — this is the established ED-Phys-10 baseline kinematic content. Phase-3 inherits it without adding structural commitment.

---

## 7. Curvature-Dynamics Sector (GR-4) Evaluation

### 7.1 GR-4A — Einstein-like equations with kernel-weighted source

**Evaluation.** ED-Phys-10's prior closure established that ED produces kinematic acoustic-metric content but **no Einstein equations**. Phase-3's Theorem GR1 provides primitive-level kernel structure for vacuum-response in curved spacetime but does not by itself force a dynamical equation for the metric. The bandwidth-field equations remain the underlying dynamics; the acoustic metric is a kinematic construct on top of bandwidth dynamics.

For GR-4A to be FORCED, some primitive-level argument would need to derive Einstein-like dynamics for $g^\mathrm{ac}_{\mu\nu}$ from the bandwidth-field equations. ED-Phys-10's exhaustive analysis did not produce such a derivation; Arc N's Theorem N1 supplies vacuum-kernel structure but not metric dynamics.

**Verdict:** **NOT FORCED.** SPECULATIVE — ED-Phys-10 baseline preserved.

### 7.2 GR-4B — Nonlocal curvature equations from V1

**Evaluation.** A non-local curvature equation $R_{\mu\nu}(x) = \int K_\mathrm{vac}(\sigma(x, x')) \cdot S_{\mu\nu}(x') d^4 x'$ is structurally admissible (Theorem GR1 supplies the kernel; bandwidth-source $S_{\mu\nu}$ is constructible from primitive bandwidth content). However, no primitive-level argument forces such an equation: alternative dynamical relations between curvature and bandwidth source are equally admissible, including the trivial relation (no curvature dynamics, GR-4C baseline).

**Verdict:** **NOT FORCED.**

### 7.3 GR-4C — Acoustic-metric-only dynamics (baseline)

**Evaluation.** ED-Phys-10's established result. The acoustic metric is a kinematic construct; no primitive-level argument forces dynamical equations for it beyond the underlying bandwidth-field dynamics. This is the established baseline against which GR-4A and GR-4B are evaluated.

**Verdict:** **Baseline preserved** (not a new FORCED claim, but the structural ceiling Phase-3 cannot exceed without explicit forcing argument).

### 7.4 GR-4D — Curvature-induced vacuum backreaction

**Evaluation.** Arc N §6.1's hand-off identified "Λ as V1-kernel integral" — under Theorem GR1, this becomes
$$
\Lambda_\mathrm{primitive}(x) \sim \int K_\mathrm{vac}(\sigma(x, x')) \cdot \rho_\mathrm{vac}(x') d^4 x',
$$
with $\rho_\mathrm{vac}$ the local vacuum-energy density. The *existence* of a finite $\Lambda$-integral structure is FORCED-conditional via Arc Q.8 + Theorem GR1; the *back-reaction* of $\Lambda$ on curvature requires an additional dynamical mechanism (analogous to Einstein's $R_{\mu\nu} - \tfrac{1}{2} R g_{\mu\nu} + \Lambda g_{\mu\nu} = 8\pi G T_{\mu\nu}$).

If the dynamical mechanism is admissible (GR-4A or GR-4B), then GR-4D's back-reaction is structurally non-trivial. Without forced GR-4A or GR-4B, the back-reaction is a kinematic feature without dynamical consequence.

**Verdict:** **FORCED-CONDITIONAL in existence sense (Λ-integral structure exists from Theorem GR1 + Arc Q.8).** Dynamical back-reaction NOT FORCED — depends on GR-4A or GR-4B status. Specific coupling $\kappa$ INHERITED.

### 7.5 GR-4E — Curvature-dependent UV-FIN constraints

**Evaluation.** UV-FIN (Theorem Q3) operates at the primitive event-discreteness scale $\ell_\mathrm{ED}$. Whether $\ell_\mathrm{ED}$ itself depends on curvature is a separate primitive-level question. Phase-3's Theorem GR1 forces V1's curved-spacetime form via metric-independent primitives; the curved-spacetime UV-FIN argument operates with the same $\ell_\mathrm{ED}$ as flat space. No primitive-level argument forces $\ell_\mathrm{ED}$ to be curvature-dependent.

**Verdict:** **NOT FORCED.**

---

## 8. Summary Table

| ID | Description | FORCED? | Justification | Primitive dependencies | Constraint drivers |
|---|---|---|---|---|---|
| **GR-1A** | Curvature-dependent bandwidth evolution | NO | Minimal coupling alternative admissible | 04, 06, ED-Phys-10 | C1 |
| **GR-1B** | Curvature-modified σ_τ shift | NO | Generally-covariant Theorem M1 form is natural extension; explicit shift not forced | 06, M.1, ED-Phys-10 | C1 |
| **GR-1C** | Curvature-dependent bandweights | NO | Constant bandweights admissible | 04, 07-L1, ED-Phys-10 | C1 |
| **GR-1D** | Curvature-dependent Fierz-class | NO | Constant Fierz class admissible; sub-cases potentially REFUTED at GR.3 | R.2.4, 07-L3, ED-Phys-10 | **C2** |
| **GR-1E** | Curvature-dependent Case-P/R distinctions | NO | Stage R.2.5 forces unconditional spin-statistics; likely REFUTED at GR.3 | R.2.5, R.2.3, ED-Phys-10 | **C2 (heavy)** |
| **GR-2A** | **V1 with Synge world function** | **YES (Theorem GR1)** | All three Theorem N1 legs extend to curved spacetime via $\sigma(x,x')$ | N1, 01, 04, 06, 11, 13, ED-Phys-10 | UV-FIN + general covariance + locality |
| **GR-2B** | Curvature-dependent kernel width | NO | $\ell_\mathrm{ED}$ may be constant; curvature-dependence not forced | N1, 01, ED-Phys-10 | C3 (V1-δ, V1-∞ bounds) |
| **GR-2C** | Curvature-dependent kernel amplitude | NO | Constant amplitude admissible | N1, ED-Phys-10 | C1 |
| **GR-2D** | Curvature-dependent cross-chain correlations | **FORCED-CONDITIONAL via GR-2A cascade** | V5 inherits Synge structure under Theorem GR1 | N1 (V5), 10, ED-Phys-10 | C1, C3 |
| **GR-2E** | Curvature-dependent vacuum polarisation | NO | Generally-covariant extension via GR-2A; additional corrections not forced | Q.5, N1, ED-Phys-10 | C1, transversality |
| **GR-3A** | **Free chains follow geodesics of $g^\mathrm{ac}_{\mu\nu}$** | **FORCED-CONDITIONAL** | KG/Dirac eikonal yields geodesic motion conditional on acoustic-metric identification | 02, 13, R.1, R.3, ED-Phys-10 | None obvious; conditional |
| **GR-3B** | Curvature-dependent commitment thresholds | NO | Constant threshold admissible; Case-R sub-cases potentially REFUTED at GR.3 | 10, 11, ED-Phys-10 | C2 (Case-R) |
| **GR-3C** | Curvature-dependent adjacency graphs | NO | Constant adjacency admissible | 10, ED-Phys-10 | C1, C2 |
| **GR-3D** | Curvature-dependent memory kernels | NO | Generally-covariant extension via GR-2A for V1-coupled kernels only | Arc N, ED-Phys-10 | C1, C3 |
| **GR-3E** | Curvature-dependent null-cone deformation | NO | ED-Phys-10 baseline; not new at Phase-3 | ED-Phys-10, 06 | Causal structure |
| **GR-4A** | Einstein-like equations with kernel-weighted source | NO | ED-Phys-10 baseline preserved; no derivation of Einstein dynamics | Phase-2, ED-Phys-10, N1 | All four |
| **GR-4B** | Non-local curvature equations from V1 | NO | Alternatives admissible | N1, ED-Phys-10, 11 | Locality at V1 width |
| **GR-4C** | Acoustic-metric-only dynamics (baseline) | Baseline preserved | Established result; not a new FORCED claim | ED-Phys-10, Phase-2 | None |
| **GR-4D** | Curvature-induced vacuum backreaction | **FORCED-CONDITIONAL in existence (Λ-integral)** | Λ as V1-kernel integral from Theorem GR1 + Arc Q.8 | N1, Q.8, ED-Phys-10 | C1, C3 |
| **GR-4E** | Curvature-dependent UV-FIN constraints | NO | $\ell_\mathrm{ED}$-curvature-dependence not forced | Q.3, 01, ED-Phys-10 | C3 |

### 8.1 Final tally

- **1 unconditionally FORCED:** GR-2A (Theorem GR1).
- **3 FORCED-conditional:** GR-3A (free-chain geodesics conditional on acoustic-metric identification); GR-2D (cross-chain correlations via cascade from GR-2A); GR-4D (Λ-integral existence; back-reaction conditional on GR-4A or GR-4B status).
- **16 NOT FORCED:** GR-1A/B/C/D/E, GR-2B/C/E, GR-3B/C/D/E, GR-4A/B/C/E.
- **GR-4C baseline preserved** (not a new FORCED claim).

Total: 4 FORCED (1 unconditional + 3 conditional), 16 NOT-FORCED, GR-4C established baseline.

---

## 9. Stage GR.2 Verdict

### 9.1 Headline result: Theorem GR1

**GR-2A (V1 with Synge world function) is unconditionally FORCED** at primitive level by Theorem GR1. The flat-space Theorem N1 (V1 forced) extends to curved spacetime via Hadamard-parametrix construction with Synge's world function $\sigma(x, x')$ replacing $(x - x')^2$. All three legs of the flat-space forcing argument extend cleanly:

(i) **UV-FIN** is metric-independent (Primitives 01 + 04 + 13 are metric-independent).
(ii) **General covariance + locality** are the curved-spacetime extensions of Lorentz-covariance + locality.
(iii) **3+1D power-counting** applies pointwise.

**Theorem GR1 is ED's first FORCED gravitational-sector structural theorem.**

### 9.2 ED's structural inventory now contains 9 FORCED theorems

| # | Theorem | Source | Type |
|---|---|---|---|
| 1 | Spin-statistics $\eta = (-1)^{2s}$ | R.2.5 | Theorem-level structural |
| 2 | Cl(3,1) frame uniqueness | R.2.4 | Algebra-level structural |
| 3 | Anyon prohibition in 3+1D | R.2.3 | Topology-level structural |
| 4 | Dirac equation emergence | R.3 | Dynamical-equation-level structural |
| 5 | GRH unconditional FORCED | Q.1 + Q.2/3/7/8 | Existence-level structural |
| 6 | Canonical (anti-)commutation FORCED | Q.7 | Operator-level structural |
| 7 | UV-FIN FORCED | Q.8 | Bound-level structural |
| 8 | V1 finite-width vacuum kernel FORCED | N.2 + N.5 | Memory-kernel-level structural |
| **9** | **V1 with Synge world function FORCED** | **GR.2 (this memo)** | **Curved-spacetime-kernel-level structural** |

Theorem GR1 is the **first curved-spacetime-kernel-level structural theorem** in ED, distinct in character from the Phase-2 + Arc N theorems but consistent with them. It supplies primitive-level kernel structure for vacuum response in curved spacetime via the natural Synge-world-function generalisation.

### 9.3 Cascading FORCED-conditional items

Theorem GR1 propagates FORCED-conditional status to three secondary items:

- **GR-3A (free-chain geodesic worldlines):** FORCED-conditional on acoustic-metric identification. The Stage R.1 / R.3 KG/Dirac equations in curved spacetime yield geodesic motion in the eikonal limit; identification of the metric with $g^\mathrm{ac}_{\mu\nu}$ from ED-Phys-10 makes the geodesic claim concrete.
- **GR-2D (curvature-dependent cross-chain correlations):** FORCED-conditional via cascade. V5 inherits Synge-world-function structure under Theorem GR1.
- **GR-4D (curvature-induced vacuum backreaction):** FORCED-conditional in existence (Λ as V1-kernel integral); dynamical back-reaction conditional on GR-4A or GR-4B status (neither FORCED).

### 9.4 NOT FORCED items

The 16 remaining catalogue items are NOT FORCED at Stage GR.2. Most are ADMISSIBLE-NOT-FORCED structurally; some sub-cases will be REFUTED at Stage GR.3 (notably GR-1E by C2, and GR-1D / GR-3B in restricted sub-cases).

### 9.5 ED-Phys-10 guardrails preserved

Phase-3 Stage GR.2 closure preserves ED-Phys-10's structural ceiling:

- **No Einstein equations.** GR-4A NOT FORCED.
- **No Schwarzschild solution.** Not derivable from Stage GR.2 content.
- **No Newtonian gravity emergence.** Out of Stage GR.2 scope; depends on GR-4A / GR-4B status.
- **Acoustic-metric-only dynamics baseline (GR-4C) preserved.**

These guardrails are consistent with the Phase-3 opening §2.1 commitment.

### 9.6 Form-FORCED, value-INHERITED preserved

Theorem GR1 forces the **class** of curved-spacetime V1 kernels with Synge-world-function structure. Specific functional realisations within the class (curved-space analogues of V2 exponential, V3 with $\alpha < 2$ power-law, V4 multi-scale) remain INHERITED. This continues the Phase-2 + Arc N methodological framing.

The cascading FORCED-conditional items inherit the same structure: existence FORCED, specific values INHERITED.

---

## 10. Hand-Off

### 10.1 To Stage GR.3 (REFUTED evaluation)

`gr_coupling_refuted.md`. Will evaluate the 16 NOT-FORCED items + sub-cases of FORCED items against C1/C2/C3/locality. Expected REFUTED targets:

- **GR-1E (curvature-dependent Case-P/R)** — heavily REFUTED by C2 (spin-statistics theorem).
- **GR-1D in sub-cases violating Fierz TYPE preservation** — REFUTED by C2.
- **GR-3B in Case-R sub-cases** — REFUTED by C2 (Pauli exclusion).
- **GR-4A** — NOT REFUTED but SPECULATIVE; ED-Phys-10 baseline preserved.

Theorem GR1 limit sub-cases (analogue of V1-δ and V1-∞ in curved spacetime) bound the FORCED class — these are expected REFUTED parallel to Stage N.3 §3 structure.

### 10.2 To Stage GR.4 (cosmological implications)

`gr_cosmological_implications.md`. Will evaluate cosmological consequences of Theorem GR1 + cascading items + ADMISSIBLE structures:

- Explicit V1-kernel integral for cosmological-Λ in closed cosmological spacetime.
- Large-scale structure via V5 cosmological correlations.
- Dispersion-relation modifications.
- Empirical-signature framework.

### 10.3 To Stage GR.5 (synthesis)

`phase3_synthesis.md`. Will integrate GR.0 through GR.4 into the final Phase-3 verdict.

### 10.4 Back-flow to Phase-2 + Arc N

Theorem GR1 does not require modification of any Phase-2 + Arc N closure. It is a *curved-spacetime extension* of Theorem N1, preserving all flat-space structure as the flat limit. Form-FORCED / value-INHERITED methodology preserved.

---

## 11. Cross-References

- Phase-3 opening: `phase3_scoping.md` (GR.0).
- Catalogue: `gr_coupling_catalogue.md` (GR.1).
- Phase-2 closures: `phase2_synthesis.md`, `arc_q_synthesis.md`, `chain_mass_synthesis.md`, `dirac_emergence.md`, `rule_type_taxonomy_synthesis.md`.
- Arc N closure: `arc_n_synthesis.md`, `non_markov_forced.md`, `non_markov_refuted.md`.
- ED-Phys-10 prior: `archive/research_history/ED Physics/ED-Phys-10/`, `memory/project_ed10_geometry_qft_scope.md`.
- Downstream: `gr_coupling_refuted.md` (GR.3), `gr_cosmological_implications.md` (GR.4), `phase3_synthesis.md` (GR.5).

---

## 12. References

[1] A. Proxmire, *Phase-3 Scoping*, `phase3_scoping.md`, 2026.

[2] A. Proxmire, *GR Coupling Catalogue*, `gr_coupling_catalogue.md`, 2026.

[3] A. Proxmire, *Arc N Synthesis*, `arc_n_synthesis.md`, 2026.

[4] B. S. DeWitt, *The Global Approach to Quantum Field Theory*. Oxford University Press, 2003 — Synge's world function and Hadamard parametrix.

[5] R. M. Wald, *Quantum Field Theory in Curved Spacetime and Black Hole Thermodynamics*. University of Chicago Press, 1994 — Hadamard parametrix construction.

[6] ED-Phys-10 kinematic-curvature arc, closed 2026-04-22. See `memory/project_ed10_geometry_qft_scope.md`.

---

## 13. One-Line Summary

**Stage GR.2 evaluates the 20 Phase-3 catalogue items and FORCES one unconditionally — GR-2A (V1 with Synge world function), establishing Theorem GR1 (V1 in Curved Spacetime FORCED) as ED's first FORCED gravitational-sector structural theorem and the ninth FORCED theorem in ED's structural inventory — by extending Theorem N1's three-leg flat-space forcing argument to curved spacetime via the Hadamard-parametrix construction with $\sigma(x, x')$ replacing $(x - x')^2$ (UV-FIN metric-independent, general covariance + locality preserved, 3+1D power-counting applies pointwise); three cascading FORCED-conditional items emerge (GR-3A free-chain geodesic worldlines via KG/Dirac eikonal limit conditional on acoustic-metric identification, GR-2D cross-chain correlations via Theorem GR1 cascade, GR-4D Λ-integral existence with dynamical back-reaction conditional on unforced GR-4A/GR-4B); 16 catalogue items remain NOT FORCED at Stage GR.2 with REFUTED determinations deferred to Stage GR.3 (notably GR-1E heavily REFUTED candidate by C2, GR-1D and GR-3B partially REFUTED in sub-cases); ED-Phys-10 acoustic-metric guardrails preserved (no Einstein equations FORCED, GR-4A SPECULATIVE, GR-4C baseline retained); form-FORCED / value-INHERITED methodology consistent with Phase-2 + Arc N closures; ED's structural inventory now spans nine FORCED theorems across non-relativistic, relativistic-kinematic, mass-structure, QFT, kernel, and curved-spacetime-kernel layers.**
