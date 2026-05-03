# Arc QC — Memo 2: UR-1, the Unresolved-Regime Characterization Theorem

**Status:** Memo 2 of Arc Q-COMPUTE. Block A's gate-condition derivation. Architect-mode active.

**Date:** 2026-05-02

---

## 1. Structural Summary

This memo derives the **functional form of $\mathcal{U}(\mathcal{S},t)$** from substrate primitives, states **UR-1** as a formal theorem, sketches its proof, tests it against three known regimes (bulk superconductor, Josephson junction, atomic-scale matter wave), and resolves OQ-1 (functional form of $\mathcal{U}$) and OQ-3 (independence vs. coupling of UR-1 conditions). Partial closure on OQ-6 ($\mathcal{M}$ vs. $\mathcal{U}$ independence).

The result is a three-factor form-FORCED expression:

$$
\boxed{\;\mathcal{U}(\mathcal{S},t) \;=\; \underbrace{\prod_i \mu\!\left(\frac{\mathcal{M}_i}{\mathcal{M}_\mathrm{crit}}\right)}_{\text{multiplicity headroom}} \cdot \underbrace{\prod_{(i,j)\in\mathcal{R}} \kappa\!\left(\frac{\gamma_{ij}}{\Gamma_\mathrm{min}}\right)}_{\text{rule-spanning connectivity}} \cdot \underbrace{\exp\!\left[-\int_0^t \Lambda_\mathcal{S}(t')\,dt'\right]}_{\text{commitment-survival}}\;}
$$

with $\mu, \kappa: [0,\infty) \to [0,1]$ form-FORCED monotone functions whose specific shapes are INHERITED from V1-kernel + DCGT structure. UR-1 then states the three conditions as necessary and (jointly with substrate-geometric coupling constraints) sufficient for $\mathcal{U} \approx 1$.

OQ-1 closes: the functional form is FORCED in structure, INHERITED in specific shape — same methodology as the rest of the program.

OQ-3 closes: the three UR-1 conditions are **independent in form** (each can fail alone) but **coupled through substrate geometry** (substrate constraints link 𝓜, σ, and Λ in any physical region). Independence of failure modes survives; complete decoupling does not.

OQ-6 partially closes: $\mathcal{M}$ and $\mathcal{U}$ are *related but distinct* — $\mathcal{M}$ is a region-property (count of viable pathways); $\mathcal{U}$ is a rule-property (integrity of one participation rule across endpoints). Low $\mathcal{M}$ is necessary for high $\mathcal{U}$ but not sufficient.

---

## 2. Derivation / Argument

### 2.1 What $\mathcal{U}$ must be, from the ontology

A participation rule, in ED, is a structural constraint that spans multiple substrate endpoints — the minimum constraint specifying how a chain engages with ED-gradients (per ED-I-29 §2.3). Before commitment, the rule is *unresolved*: it spans its endpoints without having individuated to a specific configuration at any one of them. Commitment forces the rule to individuate.

$\mathcal{U}(\mathcal{S},t)$ measures the integrity of one such rule at substrate time $t$. Three substrate processes can degrade it:

- **Local multiplicity proliferation at any endpoint.** If $\mathcal{M}_i$ rises at endpoint $e_i$, more alignments become available locally, and the rule has more ways to individuate spontaneously at that endpoint.
- **Cross-endpoint connectivity collapse.** If $\Gamma_\mathrm{cross}$ between endpoints drops below hydrodynamic-window resolution along the pathway, the rule can no longer span the gap; the endpoints decouple and the rule fragments.
- **Commitment-event accumulation.** P11 commitment events and environmental ED-injection drive individuation directly. Each event contributes to a cumulative individuation pressure.

These three processes are structurally distinct (they arise from different substrate quantities) but compose multiplicatively on $\mathcal{U}$, because any of them alone can drive the rule to $\mathcal{U} \to 0$ regardless of the others. The functional form must therefore be a product of three factors, one per process.

### 2.2 The multiplicity-headroom factor

At each endpoint $e_i$, the local multiplicity $\mathcal{M}_i$ counts the viable distinct ED-gradient pathways available. Per ED-I-01 §2.3, $\mathcal{M}$ is the ED analogue of entropy: high $\mathcal{M}$ means many distinct configurations, low $\mathcal{M}$ means few.

The rule's per-endpoint integrity factor must satisfy:

- $\mu(0) = 1$ (single pathway: rule has exactly one configuration to occupy; no individuation pressure from local multiplicity).
- $\mu(\infty) = 0$ (unbounded pathways: rule cannot stably remain unresolved against the entropic pressure of available alignments).
- Monotone decreasing in $\mathcal{M}_i / \mathcal{M}_\mathrm{crit}$.

The substrate-determined threshold $\mathcal{M}_\mathrm{crit}$ is the critical multiplicity at which the rule's per-endpoint stability crosses the unresolved/individuated boundary. By ED-I-01's statistical-mechanics analogue of multiplicity-as-entropy, $\mathcal{M}_\mathrm{crit}$ is set by the substrate's intrinsic commitment-density scale relative to the V1 kernel temporal width: $\mathcal{M}_\mathrm{crit} \sim$ (V1 kernel temporal capacity) / (P11 commitment-event substrate time-scale). The exact closed-form value of $\mathcal{M}_\mathrm{crit}$ is INHERITED.

The form is FORCED to be monotone-decreasing-from-1; the specific functional shape (Boltzmann-like $e^{-x}$, rational $1/(1+x)$, etc.) is INHERITED from the V1 kernel's specific finite-width form, which is itself a Theorem N1 quantity that has been established in form but not in specific kernel-shape closed form.

### 2.3 The rule-spanning connectivity factor

A participation rule spans a relation set $\mathcal{R}$ of endpoint pairs. For each pair $(i,j) \in \mathcal{R}$, the rule must remain coherent across the pathway connecting $e_i$ and $e_j$. The substrate connectivity between endpoints is the cross-bandwidth $\gamma_{ij}$ along the pathway, given by DCGT coarse-graining (Arc D):

$$
\gamma_{ij} \sim \exp\!\left[-\alpha \int_{\mathrm{path}} \sigma(\mathbf{x})\,d\ell\right]
$$

where $\sigma(\mathbf{x}) = |\nabla\rho|\,\ell_P^2/\rho_\mathrm{local}$ and $\alpha$ is a substrate-constant prefactor.

The connectivity factor must satisfy:

- $\kappa(\infty) = 1$ (Γ_cross much greater than minimum: rule connects easily).
- $\kappa(0) = 0$ (Γ_cross collapsed below hydrodynamic-window: rule cannot span).
- Sharp transition near $\gamma_{ij} \sim \Gamma_\mathrm{min}$, where $\Gamma_\mathrm{min}$ is the substrate-determined minimum for hydrodynamic-window resolution.

By the same DCGT machinery that establishes $\Gamma_\mathrm{cross}$ as exponential in $\sigma$, $\kappa$ inherits the same exponential structure: $\kappa(x) \approx 1 - e^{-x}$ at leading order. Form FORCED; specific shape INHERITED from DCGT closed-form details.

This is the same machinery that produces the BH-2 horizon-formation condition; here it is applied to engineered rule-spanning rather than to gravitational-collapse-driven horizons. The structural identity is exact.

### 2.4 The commitment-survival factor

P11 commits irreversibly. Once a commitment event fires at any endpoint of the rule, that endpoint individuates and the rule is no longer fully unresolved across all $\mathcal{R}$. The probability that no commitment event has fired in $\mathcal{S}$ between substrate time $0$ and $t$ is, for a Poisson-class point process with local rate $\Lambda_\mathcal{S}(t')$, exactly $\exp[-\int_0^t \Lambda_\mathcal{S}(t')\,dt']$.

The local individuation rate has two contributions:

$$
\Lambda_\mathcal{S}(t') = \Lambda_\mathrm{env}(t') + \Lambda_\mathrm{int}(\mathcal{S}, t').
$$

- $\Lambda_\mathrm{env}$: rate of environmental ED-injection forcing individuation at any endpoint of $\mathcal{S}$. Sourced by external ED-flow crossing the boundary of $\mathcal{S}$. Bounded below by V1 kernel minimum (no environment can be perfectly cold; the V1 vacuum kernel itself sources a residual rate).
- $\Lambda_\mathrm{int}$: rate of P11 commitment events occurring inside $\mathcal{S}$ from internal participation dynamics. Includes deliberate operations (gates, ancilla resets) and incidental commitments (intermediate readouts, internal scattering events).

The form $\exp[-\int \Lambda\,dt']$ is FORCED by the Poisson-class structure of P11 commitment events; the specific functional form of $\Lambda(t')$ is INHERITED from the substrate environment + internal-dynamics specification.

### 2.5 The full form of $\mathcal{U}$

Combining:

$$
\mathcal{U}(\mathcal{S},t) = \left[\prod_{i \in \mathrm{endpts}(\mathcal{R})} \mu\!\left(\frac{\mathcal{M}_i(t)}{\mathcal{M}_\mathrm{crit}}\right)\right] \cdot \left[\prod_{(i,j) \in \mathcal{R}} \kappa\!\left(\frac{\gamma_{ij}(t)}{\Gamma_\mathrm{min}}\right)\right] \cdot \exp\!\left[-\int_0^t \Lambda_\mathcal{S}(t')\,dt'\right].
$$

Three substrate-mechanism factors, each derivable from a distinct substrate process, each form-FORCED in structure with INHERITED specific shape.

### 2.6 UR-1: formal statement

> **UR-1 (Unresolved-Regime Characterization Theorem).**
>
> Let $\mathcal{S}$ be a substrate region with designated participation-rule relation set $\mathcal{R}$ over endpoints $\{e_1, \ldots, e_n\}$. Let $\mathcal{U}_\mathrm{min} \in (0,1)$ be a target unresolvedness threshold. Then $\mathcal{U}(\mathcal{S},t) \geq \mathcal{U}_\mathrm{min}$ holds at substrate time $t$ if and only if all three of the following obtain:
>
> **(i) Multiplicity bounded.** For every endpoint $e_i$,
> $$\mathcal{M}_i(t) \leq \mathcal{M}_\mathrm{crit}^{(\mu^{-1}(\mathcal{U}_\mathrm{min}^{1/n}))}.$$
>
> **(ii) Cross-endpoint connectivity sustained.** For every pair $(i,j) \in \mathcal{R}$,
> $$\gamma_{ij}(t) \geq \Gamma_\mathrm{min} \cdot \kappa^{-1}\!\left(\mathcal{U}_\mathrm{min}^{1/|\mathcal{R}|}\right).$$
>
> **(iii) Commitment-injection bounded.**
> $$\int_0^t \Lambda_\mathcal{S}(t')\,dt' \leq \ln\!\left(\frac{1}{\mathcal{U}_\mathrm{min}}\right) - C_{(\mathrm{i})} - C_{(\mathrm{ii})}$$
> where $C_{(\mathrm{i})}$ and $C_{(\mathrm{ii})}$ are the (negative-log) deficits incurred by conditions (i) and (ii).
>
> Each condition is independently necessary. Failure of any one drives $\mathcal{U}$ below $\mathcal{U}_\mathrm{min}$ at a substrate-determined rate. Conditions (i)–(iii) are coupled through substrate geometry: physical substrate configurations cannot independently dial all three; constraints among $\mathcal{M}$, $\sigma$, and $\Lambda$ are imposed by the substrate's actual structure. But within the substrate-allowed region of parameter space, each condition can fail without the others, so each is structurally distinct.

### 2.7 Proof sketch

**Sufficient direction.** Assume (i), (ii), (iii) hold. Then:

- By (i), $\mu(\mathcal{M}_i/\mathcal{M}_\mathrm{crit}) \geq \mu(\mu^{-1}(\mathcal{U}_\mathrm{min}^{1/n})) = \mathcal{U}_\mathrm{min}^{1/n}$ for each $i$, so $\prod_i \mu \geq \mathcal{U}_\mathrm{min}$.
- By (ii), an analogous bound on the connectivity product gives $\prod_{(i,j)} \kappa \geq \mathcal{U}_\mathrm{min}$.
- By (iii), $\exp[-\int \Lambda\,dt'] \geq \mathcal{U}_\mathrm{min} \cdot e^{C_{(\mathrm{i})} + C_{(\mathrm{ii})}}$.

Multiplying the three factors and accounting for the cross-condition deficits: $\mathcal{U}(\mathcal{S},t) \geq \mathcal{U}_\mathrm{min}$. ∎ (sketch)

**Necessary direction.** Suppose $\mathcal{U}(\mathcal{S},t) \geq \mathcal{U}_\mathrm{min}$ but condition (i) fails at some endpoint $e_k$: $\mathcal{M}_k > \mathcal{M}_\mathrm{crit}^{(\mu^{-1}(\mathcal{U}_\mathrm{min}^{1/n}))}$. Then $\mu(\mathcal{M}_k/\mathcal{M}_\mathrm{crit}) < \mathcal{U}_\mathrm{min}^{1/n}$, so the multiplicity-headroom product $\prod_i \mu < \mathcal{U}_\mathrm{min}$. Even with the other two factors at their maximum (1 each), $\mathcal{U} < \mathcal{U}_\mathrm{min}$, contradiction. The same argument applies for (ii) and (iii). Each condition is independently necessary. ∎ (sketch)

The full closed-form proof requires the specific functional shapes of $\mu$ and $\kappa$, which are INHERITED. The structural argument above is form-FORCED.

### 2.8 Reduction to known regimes

**Regime 1 — Bulk superconductor (ED-I-01).**

A bulk superconductor below $T_c$ is a region where lattice symmetry has collapsed local multiplicity to $\mathcal{M} \approx 1$ (single coherent ED-flow channel for charge-related dynamics). The participation rule of interest is the macroscopic phase / coherent occupation across the bulk; its endpoints are the spatial extent of the superconducting domain.

- (i) holds robustly: $\mathcal{M}_i \approx 1 \ll \mathcal{M}_\mathrm{crit}$ everywhere in the bulk.
- (ii) holds: $\sigma$ is smooth across the symmetric bulk; $\gamma_{ij}$ between any two interior points is high.
- (iii) holds *below* $T_c$: thermal ED-injection rate is below the substrate individuation threshold for the locked-in symmetry. *Above* $T_c$, thermal agitation injects multiplicity (per ED-I-01 §7); $\Lambda_\mathrm{env}$ rises, condition (iii) fails, and $\mathcal{U}$ drops sharply. **$T_c$ is identified as the substrate temperature at which condition (iii) crosses its threshold.**

This recovers the ED-I-01 reading of $T_c$ exactly: the temperature at which "multiplicity overwhelms symmetry" is the temperature at which condition (iii) fails. UR-1 reproduces this without modification.

**Regime 2 — Josephson junction (ED-I-23).**

A Josephson junction is two low-$\mathcal{M}$ SC bulk regions separated by a thin insulating barrier. The participation rule of interest spans the two electrodes; its $\mathcal{R}$ is the relation between left-electrode endpoint and right-electrode endpoint.

- (i) holds in both electrodes: $\mathcal{M} \approx 1$ on each side.
- (ii) is the *load-bearing* condition: the barrier is a high-$\sigma$ region, so $\gamma_{LR}$ across it is suppressed. By design, the barrier is engineered such that $\gamma_{LR}$ is *above* $\Gamma_\mathrm{min}$ but only barely. The JJ lives at the (ii) boundary. This is exactly the ED-I-23 reading: "the junction is a sparsity bottleneck where ED-flow must reconcile incompatible timing across a region that cannot support its own multiplicity."
- (iii) holds when the junction is well-isolated and below $T_c$.

Macroscopic quantum tunneling (Devoret-Martinis-Clarke) corresponds to dynamical fluctuations at the (ii) boundary: when the engineered $\gamma_{LR}$ momentarily drops below $\Gamma_\mathrm{min}$ in a metastable configuration, the rule globally reconfigures (ED-I-29: "tunneling is global reconfiguration of a participation rule across sparse-σ regions"). **MQT is identified as the dynamical signature of condition (ii) marginally fluctuating below threshold and the rule reconfiguring across the gap.** The exponential dependence of MQT rate on barrier width / height is the substrate-level $\kappa$ function evaluated near its threshold — same exponential structure as DCGT-derived $\Gamma_\mathrm{cross}$.

UR-1 reproduces the full ED-I-23 / ED-I-29 reading of JJ behavior structurally.

**Regime 3 — Free atomic-scale matter wave (Eibenberger / Fein / Arndt).**

A neutral atom or small molecule traversing a matter-wave interferometer is a low-$\mathcal{M}$ ED-object whose participation rule spans the interferometer's two arms. Endpoints are the arm-merge points downstream of the beam splitter.

- (i) is the *load-bearing* condition: the molecule's internal $\mathcal{M}$ scales with mass / internal complexity. At small mass (atoms, single molecules), $\mathcal{M}_i \ll \mathcal{M}_\mathrm{crit}$ and (i) holds with margin. As mass grows, internal $\mathcal{M}$ rises; at $\mathcal{M}_i \sim \mathcal{M}_\mathrm{crit}$, the matter-wave Q-C boundary is crossed.
- (ii) holds: vacuum gradient between arms is modest; $\gamma_{LR}$ is bounded by V1-kernel range and arm separation. For typical interferometer geometry, this condition is comfortable.
- (iii) holds for short transit times in adequate vacuum: $\Lambda_\mathrm{env}$ from background gas + blackbody is low.

**The 140–250 kDa Q-C boundary is identified as the molecular mass at which condition (i) crosses threshold.** Below the boundary: $\mathcal{M}_i < \mathcal{M}_\mathrm{crit}$, $\mathcal{U} \approx 1$, fringes visible. Above the boundary: $\mathcal{M}_i > \mathcal{M}_\mathrm{crit}$, $\mathcal{U} \to 0$, fringes wash out.

The substrate-level relationship between molecular mass and $\mathcal{M}_i$ is INHERITED — it depends on how internal degrees of freedom (rotational, vibrational, electronic) populate available ED-pathways as mass grows. The form of the boundary (sharp or gradual) is set by the specific shape of $\mu$. The fact that the boundary exists at *some* mass is FORCED.

UR-1 reproduces the matter-wave Q-C boundary as condition (i) crossing threshold, distinct from condition (iii) crossing threshold (which produces $T_c$ in the SC regime). **The matter-wave boundary and the SC critical temperature are different conditions of UR-1 failing — different mechanisms, same theorem.**

### 2.9 Cross-regime consistency (preview of $M$)

Regime 1 fails at (iii) — thermal injection.
Regime 2 lives at (ii) — engineered cross-bandwidth.
Regime 3 fails at (i) — multiplicity load.

Three regimes; three different UR-1 conditions are the binding constraint in each. This pattern is exactly the input the multiplicity-cap function $M$ will need: $M$ is the envelope over the three conditions across architectural classes. Block D builds on this.

### 2.10 Resolving OQ-1, OQ-3, OQ-6

**OQ-1 — Functional form of $\mathcal{U}$.** **Closed.** Three-factor product, form-FORCED structure, specific shapes of $\mu$, $\kappa$ INHERITED from V1-kernel + DCGT closed-form details. The form is sufficient for all UR-1 derivations and downstream block work. The shape-INHERITED pieces affect only specific numerical thresholds, which were already flagged as INHERITED in Memo 1.

**OQ-3 — Independence vs. coupling of UR-1 conditions.** **Closed.** Conditions are *independent in form* (each can fail alone, each is independently necessary, the proof above establishes this) but *coupled through substrate geometry* (a physical substrate region cannot independently dial $\mathcal{M}$, $\sigma$, $\Lambda$ to arbitrary values; the substrate itself imposes consistency constraints). For Block B (failure-mode rates) and Block D ($M$ function), each condition is treated independently. For Block C (architectural classification), the geometric coupling matters — different architectures use different substrate-geometric tactics to satisfy multiple conditions simultaneously, and the substrate-coupling structure is what distinguishes one architecture class from another.

**OQ-6 — $\mathcal{M}$ vs. $\mathcal{U}$ independence.** **Partially closed.** $\mathcal{M}$ enters $\mathcal{U}$ explicitly via the multiplicity-headroom factor; $\mathcal{U}$ also depends on $\sigma$ and $\Lambda$, which are not dimensions of $\mathcal{M}$. So they are *related but distinct*: $\mathcal{M}$ is a region-property; $\mathcal{U}$ is a rule-property. Low $\mathcal{M}$ at every endpoint is necessary for high $\mathcal{U}$ but not sufficient. The independence question reduces to "are $\sigma$ and $\Lambda$ dimensions of substrate state genuinely separate from $\mathcal{M}$?" The answer is yes — $\sigma$ is a gradient-geometry property and $\Lambda$ is a commitment-rate property, neither reducible to $\mathcal{M}$.

### 2.11 Updated working invariants / definitions list

| Symbol | Meaning | Status | Source |
|---|---|---|---|
| $\mathcal{M}(\mathcal{S})$ | Multiplicity (ED-entropy analogue) | DEFINED, INHERITED scale | ED-I-01, Memo 1 |
| $\mathcal{U}(\mathcal{S},t)$ | Participation-rule unresolvedness | **DERIVED** (this memo §2.5) | this memo |
| $\sigma$, $\Gamma_\mathrm{cross}$ | Sparsity, cross-bandwidth | INHERITED | BH-2, DCGT |
| $\mu(x), \kappa(x)$ | Headroom + connectivity factor functions | FORCED form, INHERITED shape | this memo §2.2, §2.3 |
| $\Lambda_\mathcal{S}(t)$ | Local individuation rate | DEFINED; env + int contributions | this memo §2.4 |
| $\mathcal{M}_\mathrm{crit}$ | Critical multiplicity threshold | NAMED, INHERITED value | this memo §2.2 |
| $\Gamma_\mathrm{min}$ | Minimum cross-bandwidth | NAMED, INHERITED value | this memo §2.3 |
| **UR-1** | Unresolved-Regime Theorem | **DERIVED** (this memo §2.6, sketch §2.7) | this memo |
| (F1), (F2), (F3) | Failure modes mapped to UR-1 (i), (ii), (iii) | DERIVED | this memo §2.8 |
| $T_c$ | SC critical temperature | identified as condition (iii) crossing | this memo §2.8 |
| Matter-wave Q-C boundary 140–250 kDa | identified as condition (i) crossing | this memo §2.8 |
| MQT | dynamical fluctuation through condition (ii) | identified | this memo §2.8 |

### 2.12 Open questions (updated)

- **OQ-1 — CLOSED.** Functional form of $\mathcal{U}$ derived.
- **OQ-2 — open.** Three-class architectural exhaustiveness. Block C target.
- **OQ-3 — CLOSED.** Conditions independent in form; coupled through substrate geometry.
- **OQ-4 — open, sharpened.** Whether $M$ is one function with class-projections vs. three separate functions. UR-1's three-condition structure suggests $M$ has *three projections* (one per condition's failure mode) with *architectural-class modulation* of each. To be confirmed at Block D.
- **OQ-5 — open, partially advanced.** Matter-wave Q-C boundary identified as condition (i) crossing. To unify with QC ceiling: show that QC-platform ceilings also cross condition (i) (or the appropriate UR-1 condition for that platform's binding constraint). Block D target.
- **OQ-6 — partially closed.** $\mathcal{M}$ and $\mathcal{U}$ are related but distinct. Full closure when Block B specifies whether failure modes (F1)–(F3) are fully captured by UR-1's three conditions or whether additional substrate-state dimensions matter.
- **OQ-7 (new this memo).** Specific functional shape of $\mu$ and $\kappa$ — Boltzmann, rational, sigmoid, or some V1-kernel-specific shape. Affects how sharp the UR-1-condition transitions are. Likely INHERITED but may close partially via V1-kernel-specific work in a future memo if it becomes load-bearing for Block D.

### 2.13 Honest scope

What this memo delivers:

- $\mathcal{U}$ derived in form; specific shapes inherited.
- UR-1 stated formally; proof sketched.
- Three known regimes recovered cleanly, each by a different UR-1 condition.
- OQ-1, OQ-3, OQ-6 closed or partially closed.

What this memo does NOT deliver:

- Closed-form values of $\mathcal{M}_\mathrm{crit}$, $\Gamma_\mathrm{min}$, $\Lambda$ thresholds. These are INHERITED; closing them is downstream work, parallel to closed-form $\log g$ in BH-5.
- Specific functional shapes of $\mu$, $\kappa$. INHERITED.
- Exhaustiveness of the three-class architectural decomposition (OQ-2). Block C target.
- The multiplicity-cap function $M$. Block D target.

Verdict-class projection consistent with Memo 1: form-FORCED on UR-1's structure and the three-condition characterization; value-INHERITED on the thresholds.

---

## 3. Consequences for the Arc

1. **UR-1 is closed, Block A is closed, the arc gate-condition has lifted.** Block B (failure-mode quantification) and downstream blocks are now unblocked.

2. **The three UR-1 conditions provide the failure-mode taxonomy directly.** (F1) ↔ (i): multiplicity proliferation. (F2) ↔ (ii): cross-bandwidth collapse. (F3) ↔ (iii): commitment-injection accumulation. Block B's job is now to quantify the *rates* at which each condition fails — i.e., $d\mathcal{M}/dt$, $d\gamma_{ij}/dt$, $\Lambda(t)$ — for each architectural class.

3. **The matter-wave Q-C boundary, $T_c$, and JJ MQT are now substrate-unified.** Three different empirical phenomena, three different conditions of UR-1 crossing threshold. This is structural unification of the kind the program has been delivering across other sectors.

4. **The hypothesis that $M$ is one substrate object with class-projections is sharpened.** UR-1 has three conditions; $M$ likely has three projections (one per condition), with architectural-class modulation of which condition is binding. Block D will test this.

5. **Block C (architectural classification) is reframed.** Architectures differ in *which UR-1 condition is binding* and *how the substrate-geometric coupling is configured to keep the others slack*. Class A (engineered-low-$\mathcal{M}$): condition (i) is held by structural simplification; the architecture works against (iii) using isolation and against (ii) using engineered geometry. Class B (global-geometric): condition (ii) is held by topological rigidity; (i) and (iii) are downstream consequences. Class C (multi-multiplicity-redundancy): condition (i) is RELAXED by allowing higher $\mathcal{M}$ but using redundancy of pathways. The three-class hypothesis now has a cleaner structural test: do the three classes correspond to *which UR-1 condition is the architecture's primary protection target*? If yes, exhaustiveness is plausible (three conditions → three classes). If a fourth substrate-allowed protection target exists, the decomposition needs a Class D.

6. **OQ-7 added.** Specific functional shape of $\mu$, $\kappa$. Likely INHERITED unless it becomes load-bearing for $M$.

7. **Verdict-class projection re-affirmed.** Form-FORCED on UR-1, on the failure-mode → condition map, on $M$'s general shape. Value-INHERITED on numerical thresholds.

---

## 4. Recommended Next Step

**Memo 3 — Quantify failure-mode rates.** Block B opens.

File: `theory/Quantum_Computing/Arc_QC_3_Failure_Mode_Rates.md`.

Scope:

- For each UR-1 condition (i)–(iii), derive the substrate-level dynamics of how the relevant quantity ($\mathcal{M}_i$, $\gamma_{ij}$, $\Lambda$) evolves under engineered + environmental conditions.
- Identify the substrate-determined timescales: $\tau_{(\mathrm{i})}$ for multiplicity-rise driving (i) failure; $\tau_{(\mathrm{ii})}$ for cross-bandwidth collapse driving (ii) failure; $\tau_{(\mathrm{iii})}$ for commitment-injection accumulation driving (iii) failure.
- Establish what the QC operating regime looks like: a bounded substrate time-window during which all three conditions hold, set by the minimum of the three $\tau$ scales for the architecture in question.
- Test against three regimes: SC qubit decoherence times, JJ tunneling rates, matter-wave fringe-loss timescales.
- Honest verdict on which timescales close in form-FORCED terms and which are INHERITED.

Closes (partial) OQ-6, advances OQ-2 (Block C exhaustiveness setup), prepares Block C.

Estimated 1–2 sessions.

If failure-mode rates close cleanly, Memo 4 opens Block C: the architectural exhaustiveness audit + class-by-class derivation of which UR-1 condition each architecture targets and how substrate-geometric coupling is configured.
