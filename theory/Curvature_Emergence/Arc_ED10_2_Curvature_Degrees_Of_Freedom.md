# Arc_ED10_2 — Curvature-Emergent Degrees of Freedom

**Date:** 2026-04-30
**Status:** First technical memo of the Curvature Emergence Arc. Identifies the substrate quantities that can serve as curvature-bearing degrees of freedom and maps them to continuum geometric objects (metric, Christoffel symbols, Riemann / Ricci / Einstein tensors). **Result: structural-suggestive mapping identified — substrate cumulative-strain four-index structure → Riemann-class object; substrate connection coefficients → Christoffel-class object; substrate participation metric → acoustic-metric-class object. Structural plausibility established; full curvature dynamics remain speculative pending ED10-3 / ED10-4.**
**Companions:** [`Arc_ED10_1_Opening.md`](Arc_ED10_1_Opening.md), [`../../arcs/quantum/foundations/phase3_synthesis.md`](../../arcs/quantum/foundations/phase3_synthesis.md) (Theorem GR1), [`../Substrate_Gravity/Arc_SG_6_Substrate_Gravity_Synthesis.md`](../Substrate_Gravity/Arc_SG_6_Substrate_Gravity_Synthesis.md), [`../Arc_D/Arc_D_6_Synthesis_And_Theorem.md`](../Arc_D/Arc_D_6_Synthesis_And_Theorem.md), [`../ED_Geometry_Emergence_Scoping.md`](../ED_Geometry_Emergence_Scoping.md) (earlier ED-10 scoping with acoustic-metric guardrails).

---

## 1. Purpose

This memo performs the first technical-derivation step of the Curvature Emergence Arc. Specifically:

- **Identifies which substrate quantities can act as curvature-bearing degrees of freedom.** Curvature is a four-index tensor structure (Riemann); its substrate analogue must be a four-index participation-channel object. The memo identifies candidate substrate objects with the correct index structure and audits them for curvature-emergence suitability.
- **Determines whether ED's curvature-like participation structure (GR1) can support a genuine geometric interpretation.** Theorem GR1 (Phase-3 closure) supplied curvature-like content at the V1-kernel level via Hadamard parametrix. The question is whether this kernel-level content extends to a *geometric* interpretation at the field-equation level — i.e., whether substrate participation structures can play the role of metric, connection, and curvature tensors at continuum scale.
- **Sets the stage for ED10-3 (weak-field limit).** The structural mapping identified here is the input for ED10-3's weak-field-limit analysis, where the curvature-emergent objects must reduce to Arc_SG_4's modified Poisson equation in the $g_{\mu\nu}\to\eta_{\mu\nu}$ limit.

The memo is structurally a *mapping memo* — identifying correspondences between substrate quantities and continuum geometric objects — rather than a fundamental-derivation memo. The mappings are structural-suggestive at this stage; their structural-positive content depends on the downstream ED10-3 / ED10-4 verifications.

**Critical framing.** The memo identifies *what could play the role* of curvature degrees of freedom in the ED substrate. It does not yet *derive* the curvature-emergent field equation. The mapping work here is structurally analogous to Arc_YM_2's identification of substrate gauge-field correlators as the substrate basis for the YM equation — necessary but not yet sufficient. ED-Phys-10 acoustic-metric guardrails remain operative throughout; deviations would be flagged explicitly.

---

## 2. Inputs

- **Theorem GR1 (Phase-3 closure 2026-04-24).** V1 vacuum response kernel lifted to curved spacetime via Hadamard parametrix construction: $K_\mathrm{vac}^\mathrm{curved}(x, x') = K_\mathrm{vac}^\mathrm{prim}(\sigma(x, x')/\ell_\mathrm{ED}^2)$ with Synge's world function $\sigma(x, x')$. Establishes that V1 carries *curvature-like* structural content at the kernel level — i.e., V1's behavior on curved spacetime depends on the geometric structure of the spacetime in a structurally well-defined way.
- **Arc SG (Substrate Gravity Extension closure 2026-04-30).** Six checkable weak-field-limit prerequisites identified per Arc_SG_6 §5; these prerequisites constrain what curvature-emergent content ED-10 can structurally support.
- **DCGT (Arc D closure 2026-04-30).** Substrate-to-continuum coarse-graining methodology in flat-Minkowski-acoustic-metric regime. ED10-2 asks how this generalizes for curvature-like-field-class substrate content.
- **ED-I-06 (Fields and Forces, Feb 2026).** Three field classes: directional, scalar, curvature-like. §5 explicitly designates curvature-like-fields as the conceptual bridge to spacetime emergence. The substrate quantities identified here must fit the curvature-like-field-class ontology.
- **ED-QFT Unified Overview Paper.** §10 substrate-gravity preview + §11 program-state-and-open-directions.
- **Earlier ED-10 scoping** (`theory/ED_Geometry_Emergence_Scoping.md`, 2026-04-22). Established that ED has kinematic acoustic metric + free-scalar QFT only; no Einstein, no Schwarzschild. Updated 2026-04-27 to note substrate-gravity arc consistency. The acoustic-metric guardrail is operative; ED10-2's mapping work must respect it or explicitly flag where it would be challenged.

---

## 3. Step 1 — Substrate Objects with Curvature-Like Structure

Curvature is a four-index tensor (Riemann $R^\rho_{\sigma\mu\nu}$). Its substrate analogue must be a four-index participation-channel object. Four candidate substrate quantities have the correct index structure:

### 3.1 Cumulative-strain four-index object

The substrate-level cumulative-strain mechanism (introduced in T19's substrate derivation of Newton's $G$) tracks how participation-channel commitments propagate across spacetime. For four nearby chain commitments at substrate positions $(x_1, x_2, x_3, x_4)$, the cumulative-strain tensor $S(x_1, x_2, x_3, x_4)$ measures the deviation of parallel-transport across the four-point loop from triviality. Specifically:

$$S^{ab}_{cd}(x_1, x_2, x_3, x_4) \;\sim\; \langle\, \tau_a(x_1) \tau_b(x_2) \tau_c^{-1}(x_3) \tau_d^{-1}(x_4) - \mathrm{triv} \,\rangle,$$

with $\tau_a(x_i)$ the substrate-level participation-channel transport from a reference point to $x_i$, the four-point combination evaluated under V1-mediated chain-step propagation. The substrate-level cumulative-strain is non-zero when the four-point loop encloses curvature-like participation-density variation.

**Candidate suitability:** Cumulative-strain four-index structure is structurally analogous to the holonomy of a connection around a four-point loop — exactly the algebraic structure that produces Riemann curvature in differential geometry. The substrate quantity is well-defined under V1-mediated chain dynamics + T19's substrate-gravity mechanism. **Strong candidate** for the substrate origin of Riemann curvature.

### 3.2 Participation-curvature tensor from GR1

Theorem GR1 establishes V1's curved-spacetime kernel structure $K_\mathrm{vac}^\mathrm{curved}(x, x') = K_\mathrm{vac}^\mathrm{prim}(\sigma(x, x')/\ell_\mathrm{ED}^2)$. The kernel's *deviation* from the flat-spacetime form $K_\mathrm{vac}^\mathrm{flat}((x-x')^2/\ell_P^2)$ encodes the spacetime curvature via Synge's world function $\sigma(x, x')$. Specifically, the difference $K_\mathrm{vac}^\mathrm{curved}(x, x') - K_\mathrm{vac}^\mathrm{flat}(x, x')$ at small geodesic separation has an expansion in terms of the local Riemann tensor + higher-curvature-invariants, by the standard Hadamard-parametrix expansion.

**Candidate suitability:** The participation-curvature tensor from GR1 is a *derived* substrate quantity — it inherits its curvature content from the metric structure of the underlying spacetime rather than producing the metric structure itself. It is therefore *not* an independent substrate degree of freedom but rather a consequence of one. **Useful for verification** (downstream sub-arcs can check that the substrate-derived curvature is consistent with GR1) but not the load-bearing curvature degree of freedom itself.

### 3.3 Directional-bias gradients from ED-I-06

ED-I-06 §3 identifies directional fields as orientation-bearing participation structures; §5 identifies curvature-like fields as the structurally distinct class. *Gradients* of directional-bias fields supply two-index substrate objects ($\partial_\mu(\text{directional bias})_\nu$) that under second derivative or commutator structure could produce four-index objects. Specifically:

$$[\,\partial_\mu, \partial_\nu\,]\,(\text{directional bias})_\rho \;\sim\; (\text{four-index participation-curvature object})^{\sigma}_{\rho\mu\nu}.$$

**Candidate suitability:** Directional-bias-gradient commutators produce four-index objects with the right index structure but typically do not vanish in flat space (the commutator of partial derivatives vanishes, but the commutator of *directional-bias-modulated* derivatives does not in general). They are a candidate substrate quantity but their structural relationship to genuine spacetime curvature (which vanishes in flat space) is not automatically guaranteed. **Secondary candidate** — useful for cross-checking but not the primary substrate origin.

### 3.4 Kernel-shape second-derivative structure

The V1 kernel's shape — its second-derivative structure $\partial_\alpha\partial_\beta K_{V1}(x, x')$ — supplies a two-index substrate object at small geodesic separation. Under the Hadamard-parametrix expansion of GR1, this second-derivative structure couples to the local Riemann tensor:

$$\partial_\alpha\partial_\beta K_{V1}^\mathrm{curved}(x, x')\bigl|_{x' \to x} \;\sim\; \partial_\alpha\partial_\beta K_{V1}^\mathrm{flat}\bigl|_\mathrm{flat} \;+\; (\text{curvature corrections involving } R_{\alpha\beta} \text{ and } R).$$

**Candidate suitability:** Kernel-shape second-derivative structure is the substrate-level diagnostic for local curvature — it *responds to* curvature rather than *producing* it. Like the GR1 participation-curvature tensor (3.2), it is a *derived* substrate quantity rather than an independent degree of freedom. **Diagnostic candidate**, not load-bearing.

### 3.5 Why these are the only candidates

The substrate-level participation-channel network has only three structurally distinct ways to produce four-index tensor content:

- **(a) Four-point cumulative-strain structure** (3.1) — the genuine multi-point participation-channel correlation that captures the loop-holonomy-class content of curvature.
- **(b) Two-derivative structures** (3.4) — second-derivative substrate operators acting on participation-density or kernel quantities.
- **(c) Two-index-tensor commutators** (3.3) — commutators of directional-bias-modulated derivatives.

Other potential substrate constructions reduce to combinations of these three. For example, four-point V1-kernel correlations $K_{V1}(x_1, x_2)\cdot K_{V1}(x_3, x_4)$ at coincident points reduce via the Hadamard expansion to (a) plus (b); higher-derivative-modulated bilinears reduce to (b) plus (c). The three classes are exhaustive at the structural level.

The load-bearing candidate for the curvature-emergent degree of freedom is **3.1 (cumulative-strain four-index object)**: it is the only candidate that produces a *genuine independent substrate degree of freedom* rather than a derived consequence of an underlying metric structure. The other candidates (3.2, 3.3, 3.4) are diagnostic / cross-checking / secondary.

---

## 4. Step 2 — Mapping to Continuum Geometric Objects

Propose the structural correspondences between substrate quantities and continuum geometric objects:

### 4.1 Substrate participation metric → acoustic metric candidate

The substrate participation-channel network supplies a notion of *substrate distance* between chain commitments, set by the V1-mediated propagation kernel. At continuum scale, this substrate distance becomes a *metric-like* quantity:

$$g_{\mu\nu}^\mathrm{acoustic}(x) \;\propto\; \bigl(\text{participation-density-modulated effective metric}\bigr).$$

The acoustic-metric candidate is the standard ED interpretation per ED-Phys-10 acoustic-metric-only baseline: the metric is *kinematic* (a continuum-level summary of substrate participation-density variation) rather than *dynamical* (an independent field with its own equation of motion). The acoustic-metric form was already established in the earlier ED-10 scoping (`theory/ED_Geometry_Emergence_Scoping.md`, 2026-04-22).

**Status:** **Structural-suggestive** — the acoustic-metric candidate is consistent with closed-arc work but does not by itself produce dynamical curvature content. ED10-3's weak-field-limit analysis will test whether the acoustic-metric reading is sufficient for SG-4 recovery or whether dynamical-metric content is required.

### 4.2 Substrate connection coefficients → Christoffel-like objects

If the substrate supplies a metric-like quantity (4.1), then *covariant derivatives* + *parallel transport* require connection coefficients. The substrate connection coefficients arise from gradients of the participation-channel transport structure:

$$\Gamma^\rho_{\mu\nu}(x) \;\sim\; \frac{1}{2}\,g^{\rho\sigma}\bigl(\partial_\mu g_{\sigma\nu} + \partial_\nu g_{\sigma\mu} - \partial_\sigma g_{\mu\nu}\bigr),$$

with $g_{\mu\nu}$ the substrate participation metric of (4.1). The substrate analogue is the gradient of the participation-channel transport structure, which under DCGT-style multi-scale expansion yields the Christoffel-class quantity.

**Status:** **Structural-suggestive** — connection coefficients are derived from the metric (4.1); their substrate-derivation chain follows from (4.1) by standard differential-geometry constructions. Consistent with ED-Phys-10 acoustic-metric baseline.

### 4.3 Substrate curvature tensor → Riemann-like object

The substrate cumulative-strain four-index object (3.1) maps to the Riemann curvature tensor at continuum scale:

$$R^\rho_{\sigma\mu\nu}(x) \;\sim\; (\text{continuum limit of}) \;S^{ab}_{cd}(x, x+\delta_1, x+\delta_2, x+\delta_3),$$

with $\delta_1, \delta_2, \delta_3$ infinitesimal substrate displacement vectors and the index identifications fixed by the multi-scale expansion of the cumulative-strain object. Under DCGT-style coarse-graining (with appropriate generalization to curved background per Step 3), the Riemann curvature emerges as the leading-order four-index continuum object from the substrate cumulative-strain.

**Status:** **Structural-suggestive** — the cumulative-strain four-index object exists at substrate level and produces a four-index continuum quantity under coarse-graining; the identification of this quantity with the Riemann curvature is consistent with the index structure but requires explicit verification in ED10-3 / ED10-4. Under the acoustic-metric reading, the Riemann-like object is *derived* from the metric (4.1) rather than independent; under a stronger curvature-emergent reading, it could be an independent substrate degree of freedom.

### 4.4 These are structural mappings, not claims of GR derivation

The mappings (4.1) – (4.3) supply the *correspondence framework* within which curvature emergence can be analyzed. They are **not claims** that ED derives general relativity. Specifically:

- The acoustic-metric reading is a kinematic-summary of substrate participation density, not a fundamental dynamical metric field. ED-Phys-10 baseline preserved.
- The Christoffel-class connection follows from the metric kinematically; not derived as an independent dynamical quantity.
- The Riemann-like object inherits its curvature content from the metric (4.1) under the acoustic-metric reading; an independent-curvature reading would require establishing a substrate dynamical mechanism for curvature that ED-10 has not yet identified.

The structural mappings are necessary scaffolding but not sufficient for a curvature-emergent field equation. The downstream ED10-3 / ED10-4 work must verify that the mappings produce the SG-4 weak-field limit + identify the field equation.

---

## 5. Step 3 — DCGT on Curvature-Like Fields

DCGT (Arc D) was derived in flat-Minkowski-acoustic-metric regime. Curvature-like-field-class application requires structural generalization. Three classes:

### 5.1 Scalar diffusion → Laplacian (recap)

Arc_D_2 derived $\partial_t\rho = \nabla\cdot(M(\rho)\nabla\rho)$ from substrate event-flux statistics in flat background. The Laplacian operator $\nabla\cdot\nabla$ is the canonical scalar-diffusion operator under DCGT scalar-coarse-graining.

### 5.2 Vector diffusion → covariant divergence (recap)

Arc_D_3 derived $\rho\,\partial_t\mathbf{v} = \mu(\rho)\nabla^2\mathbf{v} + \cdots$ from substrate chain-momentum-flux statistics in flat background. The Laplacian-acting-on-vector-field $\nabla^2\mathbf{v}$ is the canonical directional-field-diffusion operator.

### 5.3 Curvature-like diffusion → Laplace-Beltrami + curvature-coupling terms (new)

In curved background, the flat-background Laplacian $\nabla^2$ becomes the Laplace-Beltrami operator

$$\Box_g \;=\; \frac{1}{\sqrt{|g|}}\partial_\mu\!\Bigl(\sqrt{|g|}\,g^{\mu\nu}\partial_\nu\Bigr) \;=\; g^{\mu\nu}\nabla_\mu\nabla_\nu,$$

with $\nabla_\mu$ the metric-covariant derivative. Additionally, multi-scale expansion of the V1-mediated chain-step propagation in curved background introduces *curvature-coupling terms* via the GR1 Hadamard-parametrix structure:

$$\Box_g^\mathrm{DCGT-curved} \;=\; \Box_g \;+\; \alpha_R\,R \;+\; \beta_{R_{\mu\nu}}\,R^{\mu\nu}\nabla_\mu\nabla_\nu \;+\; \mathcal{O}(\ell_P^2\,R^2),$$

with $\alpha_R$, $\beta_{R_{\mu\nu}}$ dimensionless V1-profile coefficients (substrate-derived; INHERITED at value layer). The curvature-coupling terms arise from the V1 second-moment expansion under the Hadamard parametrix, parallel to Arc_D_4's flat-background V1 second-moment expansion + R1 emergence.

**FORCED at substrate level:**
- Operator structure $\Box_g$ + curvature-coupling-term presence (from V1 second-moment expansion under GR1's curved-spacetime kernel structure).
- Sign of leading curvature-coupling contributions (from V1 positive Fourier transform).

**INHERITED at value layer:**
- Specific coefficients $\alpha_R$, $\beta_{R_{\mu\nu}}$ (set by V1 kernel profile + substrate normalization).
- Higher-order corrections in $\ell_P^2 R^2$ and beyond.

This is the curvature-like-field-class generalization of DCGT. It is structurally analogous to Arc_D_4's V1 → R1 emergence but with the substrate-cutoff correction now coupling to background curvature.

---

## 6. Step 4 — Constraints from SG-6 Weak-Field Targets

The six SG-6 prerequisites (Arc_SG_6 §5) constrain the curvature-emergent degrees of freedom:

### 6.1 Newtonian Poisson recovery

In the weak-field high-acceleration regime, ED-10 must reduce to $\nabla^2\Phi = 4\pi G\rho_m$. **Constraint:** the curvature-emergent field equation must contain a Newtonian-Poisson sector that emerges in the appropriate limit. The acoustic-metric reading (4.1) supplies this via the standard weak-field expansion $g_{\mu\nu} = \eta_{\mu\nu} + h_{\mu\nu}$ with $h_{00} = -2\Phi/c^2$.

### 6.2 Modified Poisson recovery with $\mu(x)$ asymptotics

In the weak-field general-acceleration regime, ED-10 must reduce to $\nabla\cdot[\mu(|\nabla\Phi|/a_0)\nabla\Phi] = 4\pi G\rho_m$. **Constraint:** the curvature-emergent field equation must produce a substrate-derivation of the $\mu(x)$ interpolation function in the weak-field limit, with the correct asymptotic limits ($\mu \to 1$ at high acceleration; $\mu \to x$ at low acceleration).

### 6.3 BTFR slope-4

In the deep-MOND regime, ED-10 must reproduce $v^4 = G\,M\,a_0$. **Constraint:** the curvature-emergent equation's deep-MOND limit must preserve the dimensional combination $G\,M\,a_0$ producing slope-4. Since slope-4 is dimensionally locked by $G + M + a_0$ structure, this constraint is satisfied automatically once (6.1) and (6.2) are satisfied.

### 6.4 $a_0$ horizon-scale invariance

The transition acceleration $a_0 = c\,H_0/(2\pi)$ must remain horizon-scale-invariant in the curvature-emergent regime. **Constraint:** ED-10's curvature-emergent treatment must preserve the cosmological-horizon-anchored structural origin of $a_0$ identified in Arc_SG_3. Specifically, the cosmological-horizon participation-density mechanism (Arc_SG_3 §3) must extend cleanly to curved-spacetime regime.

### 6.5 SG-4 recovery in $g_{\mu\nu}\to\eta_{\mu\nu}$ limit

The curvature-emergent equation must reduce exactly to Arc_SG_4's modified Poisson equation when the metric is taken to be flat Minkowski. **Constraint:** the substrate-derivation chain must be structurally consistent across flat / curved background; no structural ingredients can appear in the curved regime that have no flat-regime counterpart.

### 6.6 GR1 generalization to consolidated field equation

The curvature-emergent equation must reduce to GR1 at the kernel level + reduce to SG-4 at the field-equation level. **Constraint:** GR1's Hadamard-parametrix curvature-coupling structure must be consistent with whatever curvature-coupling terms appear in the curvature-emergent field equation.

### 6.7 Constraint summary on curvature-emergent degrees of freedom

The six constraints jointly restrict the curvature-emergent degrees of freedom to a specific structural class:

- **Metric must be acoustic-class** (4.1): kinematic-summary of substrate participation density rather than fundamental dynamical field. Violating this constraint would break ED-Phys-10 acoustic-metric baseline.
- **Connection must be metric-derived** (4.2): standard Levi-Civita connection from the metric, not an independent dynamical structure.
- **Curvature must reduce to derived-from-metric structure in weak-field limit** (4.3): the cumulative-strain four-index substrate object must produce the standard Riemann curvature in continuum limit, with the curvature dynamics inherited from the metric dynamics rather than being independent.

These constraints place ED-10 squarely in the **acoustic-metric-class curvature-emergence regime**: the substrate produces a metric-like quantity that responds to participation-density variation (and hence to mass-energy content), the connection follows kinematically, the curvature follows kinematically, and the *dynamics* of the metric come from a substrate-derived effective field equation rather than from Einstein's $G_{\mu\nu} = 8\pi G\,T_{\mu\nu}$ at field-equation level.

This is structurally consistent with ED-Phys-10 acoustic-metric guardrails. The arc does not produce GR; it produces an acoustic-metric-class curvature-emergent framework that recovers SG-4 in the weak-field limit + extends consistently with GR1's curved-spacetime kernel structure.

---

## 7. Step 5 — Preliminary Verdict

**Curvature-like degrees of freedom exist at substrate level (GR1).** The substrate cumulative-strain four-index structure (3.1) supplies a genuine substrate-level curvature-emergent degree of freedom. The participation-curvature tensor from GR1 (3.2), kernel-shape second-derivative structure (3.4), and directional-bias-gradient commutators (3.3) supply diagnostic / cross-checking quantities. The exhaustive structural enumeration confirms that these are the only candidates.

**Mapping to continuum geometric objects is structurally plausible.** The acoustic-metric candidate (4.1), Christoffel-class connection (4.2), and Riemann-like curvature object (4.3) form a structurally-consistent correspondence framework. The framework is ED-Phys-10-compatible (acoustic-metric-class) and consistent with the closed substrate-gravity arc work.

**DCGT generalizes structurally to curvature-like-field-class** (Step 3) via Laplace-Beltrami operator + curvature-coupling terms from V1 second-moment expansion under the Hadamard parametrix. The generalization is consistent with the closed-arc Arc_D_4 V1 → R1 emergence in flat background.

**SG-6 prerequisites constrain the curvature-emergent regime to acoustic-metric class** (Step 4 §6.7). The constraints are jointly satisfiable under acoustic-metric-class curvature emergence; they would be jointly violated by any attempt to derive Einstein-class field equations at substrate level (which would require dynamical-metric content beyond the substrate participation-density-modulated reading).

**But full curvature dynamics remain speculative until ED10-3 and ED10-4.** The mapping work here is structural-suggestive scaffolding. The structural-positive verdict requires:

- ED10-3 verifying that the weak-field limit of the curvature-emergent framework reduces to Arc_SG_4's modified Poisson equation.
- ED10-4 producing a specific covariant-form candidate field equation with explicit substrate-derivation chain.
- ED10-5 auditing OS-positivity / stability constraints for whatever covariant form emerges.

The preliminary verdict at this stage is **structural plausibility established; structural-positive content depends on downstream sub-arc deliverables**.

**Honest framing.** The mapping work is not original per se — acoustic-metric-class curvature-emergent frameworks have been extensively studied in standard relativistic-acoustic-metric / analog-gravity literature. The ED-program-specific contribution at this stage is the *substrate-derivation chain* identifying which substrate quantities supply the acoustic-metric content + how DCGT generalizes to curvature-like fields. Whether this scaffolding produces a substrate-derivation that satisfies all six SG-6 prerequisites simultaneously is the load-bearing question for downstream sub-arcs.

---

## 8. Recommended Next Step

Proceed to **Arc_ED10_3 (Weak-Field Limit and SG-4 Matching)**. File: `theory/Curvature_Emergence/Arc_ED10_3_Weak_Field_Limit.md`. Scope: derive the weak-field limit of the curvature-emergent framework identified here; verify that the limit reproduces Arc_SG_4's modified Poisson equation; identify which structural assumptions are load-bearing for the matching to work; flag any inconsistencies between the curvature-emergent scaffolding and the SG-6 prerequisites.

Estimated 1–2 sessions for Arc_ED10_3 given the consistency-check nature.

### Decisions for you

- **Confirm curvature-degree-of-freedom mapping.** Substrate cumulative-strain four-index → Riemann-class object as the load-bearing candidate; acoustic-metric reading per ED-Phys-10 baseline; structural plausibility established.
- **Confirm DCGT generalization to curvature-like fields** via Laplace-Beltrami + V1-second-moment curvature-coupling terms.
- **Confirm acoustic-metric-class regime** as the structural framework forced by SG-6 constraints.
- **Confirm proceeding to Arc_ED10_3 (weak-field limit and SG-4 matching) as the next deliverable.**

---

*Arc_ED10_2 closes the curvature-degree-of-freedom mapping work. Substrate cumulative-strain four-index object identified as the load-bearing curvature-emergent degree of freedom; participation-curvature tensor from GR1, kernel-shape second-derivative structure, and directional-bias-gradient commutators identified as diagnostic / cross-checking / secondary candidates. Structural correspondences proposed: substrate participation metric → acoustic-metric candidate (4.1), substrate connection coefficients → Christoffel-class object (4.2), substrate cumulative-strain → Riemann-like curvature object (4.3). DCGT generalizes structurally to curvature-like-field-class via Laplace-Beltrami operator + V1 second-moment curvature-coupling terms ($\alpha_R\,R$, $\beta_{R_{\mu\nu}}\,R^{\mu\nu}\nabla_\mu\nabla_\nu$, etc.) FORCED at substrate level. Six SG-6 prerequisites jointly constrain the curvature-emergent regime to acoustic-metric class, structurally consistent with ED-Phys-10 baseline. Preliminary verdict: structural plausibility established; structural-positive content depends on ED10-3 weak-field-limit verification + ED10-4 covariant-form derivation + ED10-5 OS-positivity audit. Mapping work is not original (acoustic-metric-class curvature-emergence is well-studied in standard relativistic-acoustic-metric literature); ED-program-specific contribution is the substrate-derivation chain. Arc_ED10_3 (weak-field limit + SG-4 matching) is the next deliverable.*
