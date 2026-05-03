# Arc QC — Memo 6: Predictive Content and Falsifiable Substrate-Level Claims

**Status:** Memo 6 of Arc Q-COMPUTE. Last technical memo before synthesis. Architect-mode active. Form-FORCED / value-INHERITED methodology applied to predictive content.

**Date:** 2026-05-02

---

## 1. Structural Summary

This memo extracts the predictive content of $M$ and states it as falsifiable substrate-level claims. For each architectural class, the asymptotic scaling of $\tau_\mathrm{QC}$ with system size, geometry, and environment is derived; substrate-determined ceilings are located; and falsification conditions are specified.

The arc's predictive deliverables fall into three categories:

- **Sharp claims** — substrate-level form is FORCED with quantitative scaling, even though the numerical thresholds are INHERITED. These are falsifiable by structure: a measurement that violates the *form* of the scaling refutes the model, regardless of where the threshold sits numerically.
- **Structural claims** — qualitative architectural-class properties FORCED by the substrate machinery (existence of ceilings, sub-linear redundancy scaling, exponential gap-suppression structure, etc.). Falsifiable by demonstrating an architecture that does not exhibit the predicted structural property.
- **Inherited claims** — specific numerical predictions whose values depend on closed-form derivations of substrate constants ($\mathcal{M}_\mathrm{crit}$, $\Gamma_\mathrm{min}$, $\Lambda$ thresholds, redundancy correlation budget $N_\mathrm{corr}$, etc.) that the program has not currently extracted. These are provisional and can be sharpened by future structural work without invalidating the form-level results.

The cross-platform unification claim — that matter-wave Q-C boundary at 140–250 kDa, SC qubit T₁/T₂, JJ MQT, topological-gap suppression, and Hafezi multi-timescale all live on one substrate function — is the **central falsifier** of the arc. Any platform exhibiting behavior outside the substrate-allowed structure of $M$ refutes the framework.

---

## 2. Derivation / Argument

### 2.1 Class A predictions: engineered-low-multiplicity scaling

#### 2.1.1 Asymptotic scaling

For a Class A platform with system input $\mathcal{S}$ and environment $\mathcal{E}$:

$$
\tau_\mathrm{QC}^A(\mathcal{S}, \mathcal{E}) = \min\bigl[\tau_{(\mathrm{i})}^{(A)}(\mathcal{S}, \mathcal{E}),\,\tau_{(\mathrm{ii})}^{(A)}(\mathcal{S}, \mathcal{E}),\,\tau_{(\mathrm{iii})}^{(A)}(\mathcal{S}, \mathcal{E})\bigr].
$$

The system-size dependence enters through $\mathcal{M}_\mathrm{floor}(\mathcal{S})$. Define the **system-multiplicity scaling function**:

$$
\mathcal{M}_\mathrm{floor}^{(A)}(\mathcal{S}) = f_\mathrm{sys}^{(A)}(\text{architecture-specific scaling parameters})
$$

For matter waves: $\mathcal{S} = $ molecule of mass $M_\mathrm{mol}$; $f_\mathrm{sys}^{(A)} = f_\mathrm{int}(M_\mathrm{mol})$ (molecular internal-DOF activation). Monotone increasing.

For SC-qubit systems: $\mathcal{S} = $ multi-qubit register; $f_\mathrm{sys}^{(A)}$ scales with cross-qubit pathway count, which is roughly polynomial in $N_\mathrm{qubits}$ for standard architectures (more qubits open more cross-individuation pathways through gate operations, ancilla resets, and stray-coupling channels). Form FORCED to be monotone increasing; specific scaling INHERITED from architectural details.

**Sharp Class A prediction (form-level):**

> $\tau_\mathrm{QC}^A$ exhibits a **system-multiplicity wall**: as $f_\mathrm{sys}^{(A)}(\mathcal{S}) \to \mathcal{M}_\mathrm{crit}$, $\tau_{(\mathrm{i})}^{(A)} \to 0$ regardless of environmental engineering. Improving isolation, dynamical decoupling, or any environmental-side technique cannot push past this wall. Beyond the wall, Class A operation is structurally impossible.

The wall's location is INHERITED. The wall's *existence* and its character as a static-failure of (i) are FORCED.

#### 2.1.2 Class A ceiling

The ceiling is the supremum of $\tau_\mathrm{QC}^A$ over all environments and meta-architectural overlays:

$$
\tau_\mathrm{QC}^{A,\mathrm{ceil}}(\mathcal{S}) = \sup_{\mathcal{E}, \mathcal{O}} M(\mathcal{S}, A, \mathcal{E}, \mathcal{O}) = \min\bigl[\tau_{(\mathrm{i})}^{(A,\sup)},\,\tau_{(\mathrm{ii})}^{(A,\sup)},\,\tau_{(\mathrm{iii})}^{(A,\sup)}\bigr].
$$

In the limit of perfect isolation ($\Lambda_\mathrm{env} \to \Lambda_\mathrm{V1}$, the V1-vacuum-kernel residual rate) and perfect environmental engineering, the ceiling becomes:

$$
\tau_\mathrm{QC}^{A,\mathrm{ceil}}(\mathcal{S}) \approx \min\!\left[\frac{\mathcal{M}_\mathrm{crit} - \mathcal{M}_\mathrm{floor}(\mathcal{S})}{A_\mathcal{S}\,\langle\delta\mathcal{M}\rangle_\mathrm{V1}},\,\tau_{(\mathrm{ii})}^{(A,\sup)},\,\frac{\ln(1/\mathcal{U}_\mathrm{min})}{\Lambda_\mathrm{V1}}\right]
$$

The first term goes to zero at the system-multiplicity wall. The third term sets the ultimate Class A ceiling at perfect isolation, INHERITED from the V1 kernel residual.

#### 2.1.3 Falsifiers

A Class A platform that:

- Exhibits coherence times *increasing* monotonically with system size beyond some characteristic scale, with no plateau or decrease, would refute the system-multiplicity wall structure.
- Exhibits a Q-C-boundary-like static failure in matter-wave coherence at a mass *not* monotonically related to internal-DOF count would refute the $f_\mathrm{int}(M_\mathrm{mol})$ form.
- Exhibits SC qubit T₁ scaling with $N_\mathrm{qubits}$ in a non-monotone way (oscillatory, periodic, or anomalous) would refute the substrate-level $\Lambda_\mathrm{env}^{(A,\mathrm{SC})}$ accumulation structure.

### 2.2 Class B predictions: global-geometric-rigidity scaling

#### 2.2.1 Asymptotic scaling

For a Class B platform with topological gap $\Delta_\mathrm{top}$ at substrate-equivalent temperature $T_\mathrm{eff}$:

$$
\tau_\mathrm{QC}^B(\mathcal{T}, T_\mathrm{eff}) \approx \tau_\mathrm{gap-stab}(\mathcal{T}) \cdot \exp(\Delta_\mathrm{top}/T_\mathrm{eff}).
$$

The exponential factor dominates the scaling. The binding constraint is $\tau_\mathrm{gap-stab}$, the inverse rate of gap-closing or edge-hybridization events. This is set by macroscopic substrate quality (sample homogeneity, edge purity, defect density, anyonic fusion-error rates), not by environmental coupling rate.

**Sharp Class B prediction (form-level):**

> Class B coherence time exhibits **exponential dependence on the substrate-level gap-to-perturbation ratio** $\Delta_\mathrm{top}/T_\mathrm{eff}$, with binding shifted from environmental rate (Class A's regime) to topology-perturbation rate. Engineering effort that improves $\Delta_\mathrm{top}$ or reduces topological perturbation produces exponential improvements; engineering effort that improves isolation in the standard Class A sense produces diminishing returns past a substrate-determined point.

#### 2.2.2 Class B ceiling

$$
\tau_\mathrm{QC}^{B,\mathrm{ceil}} = \sup_\mathcal{T} \tau_\mathrm{gap-stab}(\mathcal{T}) \cdot \exp(\Delta_\mathrm{top}^{\max}/T_\mathrm{eff,\min}).
$$

The ceiling is set by:
- The maximum stable topological gap achievable in any substrate ($\Delta_\mathrm{top}^{\max}$ INHERITED).
- The minimum substrate-equivalent temperature ($T_\mathrm{eff,\min}$ INHERITED).
- The maximum stability of the topological structure ($\tau_\mathrm{gap-stab}^{\max}$ INHERITED from material-quality limits).

For Majorana qubits with $\Delta_\mathrm{top} \sim 0.1$ meV at $T_\mathrm{eff} \sim 20$ mK: the exponential factor $\exp(\Delta/T_\mathrm{eff}) \sim e^{58} \sim 10^{25}$. This means $\tau_\mathrm{gap-stab}$ can be very short (microseconds) and Class B still beats Class A coherence (milliseconds) because the multiplier is enormous. This is the load-bearing structural prediction: Class B's ceiling is *not bounded by environmental rates at all* in the gap-suppressed regime.

#### 2.2.3 Falsifiers

A Class B platform that:

- Exhibits coherence times scaling polynomially (rather than exponentially) with $\Delta_\mathrm{top}$ at fixed temperature would refute the gap-suppression structure.
- Exhibits binding by environmental rate (e.g., Purcell-like coupling) rather than gap-stability would refute Class B's structurally-distinct binding mode.
- Exhibits no exponential temperature dependence in the gap-suppressed regime would refute $\Lambda_\mathrm{env}^{(B)} \sim \Lambda_\mathrm{env}^\mathrm{baseline}\exp(-\Delta/T_\mathrm{eff})$.

### 2.3 Class C predictions: high-multiplicity-redundancy scaling

#### 2.3.1 Asymptotic scaling

For a Class C platform with redundancy $N$:

$$
\tau_\mathrm{QC}^C(N) \sim \tau_\mathrm{QC}^\mathrm{single} \cdot \exp(N/N_\mathrm{corr})\quad\text{for } N \ll N_\mathrm{corr}
$$

where $N_\mathrm{corr}$ is the correlation budget. Beyond saturation:

$$
\tau_\mathrm{QC}^C(N) \to \tau_\mathrm{QC}^\mathrm{single} \cdot \exp(1) \quad\text{for } N \gtrsim N_\mathrm{corr}.
$$

Saturation occurs because correlated noise channels (common-mode environmental fluctuations, shared substrate defects, optical-mode crosstalk) become dominant once redundancy exceeds the budget; adding more pathways doesn't help against correlated failures.

**Sharp Class C prediction (form-level):**

> Class C coherence-time scaling with redundancy $N$ exhibits a **correlation-budget plateau**: exponential improvement for $N \ll N_\mathrm{corr}$, saturation at $\sim e \cdot \tau^\mathrm{single}$ for $N \gtrsim N_\mathrm{corr}$. The plateau is structurally FORCED by the correlation-budget mechanism; the value of $N_\mathrm{corr}$ is INHERITED from the substrate-coupling pattern across redundant pathways.

#### 2.3.2 Class C ceiling

$$
\tau_\mathrm{QC}^{C,\mathrm{ceil}} = \tau_\mathrm{QC}^\mathrm{single} \cdot \exp(1) \quad\text{(asymptotic in } N\text{)}.
$$

The ceiling is bounded by the single-pathway $\tau_\mathrm{QC}^\mathrm{single}$ multiplied by an O(1) factor. Class C cannot exceed the single-pathway ceiling by more than a constant factor *when correlation saturates* — the redundancy advantage is bounded.

This is structurally important: **Class C is not a strategy to exceed Class A or Class B ceilings without bound**. It is a strategy to extend the *useful operating window* before saturation, and to mitigate disorder/fabrication variations that would otherwise destroy a single-pathway implementation. Hafezi's 100% device yield is the canonical signature.

#### 2.3.3 Falsifiers

A Class C platform that:

- Exhibits unbounded scaling of $\tau_\mathrm{QC}$ with $N$ (no saturation) would refute the correlation-budget structure.
- Exhibits linear or super-linear early-regime scaling rather than exponential would refute the $c(N) \sim \exp(-N/N_\mathrm{corr})$ form.
- Exhibits $\tau_\mathrm{QC}^C / \tau_\mathrm{QC}^\mathrm{single}$ asymptotically much larger than $e$ would refute the bounded-redundancy-advantage structure.

### 2.4 Cross-platform unification: the matter-wave / qubit-system identity

The matter-wave Q-C boundary at 140–250 kDa and the qubit-system multiplicity wall are **the same boundary projected onto two platforms**. Both arise from $\mathcal{M}_\mathrm{floor}^{(A)}(\mathcal{S}) = \mathcal{M}_\mathrm{crit}$ — the static-failure branch of the Class A $\tau_{(\mathrm{i})}$ projection.

The identity is structural:

| Platform | $\mathcal{S}$ | $f_\mathrm{sys}^{(A)}(\mathcal{S})$ scaling parameter | Q-C boundary location |
|---|---|---|---|
| Matter-wave | molecule of mass $M_\mathrm{mol}$ | molecular internal-DOF activation $f_\mathrm{int}(M_\mathrm{mol})$ | 140–250 kDa (empirical) |
| SC qubit array | $N$-qubit register | cross-qubit pathway count $f_\mathrm{xy}(N_\mathrm{qubits}, \mathrm{architecture})$ | $N_\star$ qubits (INHERITED, predicted to exist) |
| Trapped-ion array | $N$-ion crystal | inter-ion pathway count + motional-mode coupling | analogous $N_\star$ (INHERITED) |
| Photonic gate-model | photonic-mode register | mode-coupling pathway count | analogous $N_\star$ (INHERITED) |

**Sharp cross-platform claim:** The matter-wave Q-C boundary value of 140–250 kDa, calibrated against $\mathcal{M}_\mathrm{crit}$, fixes the substrate-determined cap on Class A platforms across all instantiations. Any platform's $N_\star$ is determined by its *architecture-specific scaling* of $f_\mathrm{sys}^{(A)}(\mathcal{S})$ relative to molecular $f_\mathrm{int}$, with the substrate constant $\mathcal{M}_\mathrm{crit}$ shared across platforms.

This means: a more accurate measurement of the matter-wave boundary (currently 140–250 kDa, narrowable with new experiments) directly constrains the system-multiplicity wall location for all Class A qubit platforms via the substrate-level identity. The qubit-platform $N_\star$ values are not independent free parameters — they are determined (up to architecture-specific calibration) by the matter-wave anchor.

This is a **non-trivial predictive claim** of the framework, of the form-FORCED + value-INHERITED variety: the form (cross-platform identity) is FORCED; the calibration constants and the architecture-specific $f_\mathrm{sys}$ functions are INHERITED.

### 2.5 Position of current SOTA platforms on $M$

A snapshot of current platforms on $M$, with class assignment + binding condition + approximate $\tau_\mathrm{QC}$:

| Platform | Class | Binding | $\tau_\mathrm{QC}$ scale | Distance to ceiling |
|---|---|---|---|---|
| Transmon SC qubit | A | (iii): T₁ from Purcell+dielectric+QP | 100 μs–1 ms | Bounded by environmental engineering; system-multiplicity wall not yet binding at single-qubit |
| Multi-qubit SC array (1000+ physical) | A | mix of (ii)/(iii) at qubit level + system-multiplicity load | sub-ms effective coherence at system level | Approaching system-multiplicity wall in $f_\mathrm{xy}$ scaling; the engineering frontier |
| JJ as coherent element | A (boundary) | (ii) at engineered $\gamma_\mathrm{floor} \approx \Gamma_\mathrm{min}$ | designed at the boundary | Living on (ii) edge by design |
| Trapped ion qubit | A | (iii) | seconds (long T₁) | Far from system-multiplicity wall at single-ion; $f_\mathrm{xy}$ scaling slower than SC |
| Topological qubit (Majorana) | B | gap-stab (QP poisoning, edge-hybridization) | μs scale at present, exponential improvement potential | Bound by topology engineering, not by isolation |
| Photonic Chern channel | B | edge-state stability vs disorder | varies | Bound by fabrication quality |
| Hafezi multi-timescale | C | correlation budget at $N \sim 2$ | empirical robustness | Below saturation (only 2 axes used) |
| Bosonic cat code | C | photon-number correlation budget | extends single-mode lifetimes by $\sim 10$× | Approaching saturation at high cat sizes |
| GKP code | C | photon-number redundancy | depends on encoding distance | Below saturation in current implementations |
| Surface-code logical qubit | Meta: A+C | logical-level binding via composition | approaching threshold-suppression regime | Engineering frontier; $\tau_\mathrm{QC}^\mathrm{logical}$ scaling-with-distance under active development |

**Engineering-frontier observation:** The SC platform improvement curve (T₁ rising over the past decade, $N_\mathrm{qubits}$ rising more recently) is approaching the regime where the system-multiplicity wall in $f_\mathrm{xy}(N_\mathrm{qubits})$ becomes the dominant binding. When that happens, Class A scaling stops paying — the platform must transition to Class C (encoded redundancy via codes) or to Class B (topological), or it stalls.

### 2.6 Cross-class architectural transitions

Three structural transitions emerge from $M$'s class projections.

#### 2.6.1 Class A → Class C transition

Mandatory when: $f_\mathrm{sys}^{(A)}(\mathcal{S}) \to \mathcal{M}_\mathrm{crit}$ — i.e., the system-multiplicity wall becomes binding regardless of environmental engineering.

Mechanism: the only way to push past the wall is to *accept* high $\mathcal{M}$ at the physical level and use redundancy (Class C) to maintain $\mathcal{U}$ at a logical level despite high physical multiplicity.

Empirical signature: SC platforms at $\sim 10^4$–$10^6$ physical qubits will encounter the wall and must move to logical-qubit operation (which is already a Class A + Class C composition). The composition becomes mandatory; running pure-Class-A at scale becomes structurally impossible.

**Sharp prediction:** A SC-qubit-only architecture that does not encode logical qubits will plateau in effective $\tau_\mathrm{QC}^\mathrm{logical}$ before reaching the engineering frontier of physical-qubit count, even with continued T₁/T₂ improvements.

#### 2.6.2 Class B overtakes Class A

Occurs when: Class A's environmental ceiling $\tau_{(\mathrm{iii})}^{(A,\sup)}$ is exceeded by Class B's gap-suppressed $\tau_{(\mathrm{iii})}^{(B)}$ AND when Class B's $\tau_\mathrm{gap-stab}(\mathcal{T})$ is engineered to match.

The crossover scales as: $\tau_\mathrm{QC}^B/\tau_\mathrm{QC}^A \sim [\tau_\mathrm{gap-stab}(\mathcal{T})/\tau^{(A)}_\mathrm{ref}]\cdot\exp(\Delta_\mathrm{top}/T_\mathrm{eff})$.

Empirical signature: when topological gaps can be reliably engineered above some threshold scale, and topology can be made stable on long timescales, Class B's exponential factor wins.

**Sharp prediction:** Topological-qubit advantage will become structurally dominant when $\Delta_\mathrm{top}/T_\mathrm{eff} \gtrsim \ln[\tau_\mathrm{QC}^A / \tau_\mathrm{gap-stab}(\mathcal{T})] \sim 10$–$20$. For $T_\mathrm{eff} \sim 20$ mK, this means $\Delta_\mathrm{top} \gtrsim 0.5$–$1$ meV gaps with stable topology on millisecond timescales would push Class B past current Class A coherence times by orders of magnitude.

#### 2.6.3 Class C saturation

Occurs at $N \sim N_\mathrm{corr}$. Beyond this, redundancy stops paying.

Empirical signature: The multi-timescale photonic platform's improvement curve will plateau as additional axes are added, when correlated optical-mode coupling becomes the binding noise channel.

**Sharp prediction:** Hafezi-class platforms scaling beyond ~3–5 timescale axes will show diminishing returns, with the saturation point set by shared-substrate noise correlations. Bosonic codes scaling beyond a code-distance threshold will exhibit similar saturation due to photon-number correlated losses.

### 2.7 Near-term experimental tests

Four classes of test, each targeting a specific structural prediction.

#### Test 1 — Coherence-scaling experiments (Class A wall)

Measure $\tau_\mathrm{QC}^\mathrm{logical}$ in scaled SC qubit systems as a function of $N_\mathrm{qubits}$, holding error correction code distance constant and pushing T₁/T₂ via engineering. Prediction: a plateau emerges as $f_\mathrm{xy}(N_\mathrm{qubits})$ approaches $\mathcal{M}_\mathrm{crit}$. The plateau location is INHERITED. The plateau's *existence* is FORCED.

Falsifier: continued monotonic improvement of $\tau_\mathrm{QC}^\mathrm{logical}$ with $N_\mathrm{qubits}$ under fixed error-correction code distance, with no plateau in the projected platform-roadmap range.

#### Test 2 — Multiplicity-growth probes (matter-wave and qubit)

For matter waves: directly measure how internal-DOF activation correlates with fringe contrast loss using mass-matched but DOF-different molecules (e.g., highly symmetric vs floppy isomers). Prediction: contrast loss correlates with internal-DOF count, not directly with mass, when mass is held fixed.

For qubit systems: directly measure cross-qubit pathway count (via leakage tomography, cross-talk characterization) and correlate with effective system-level coherence. Prediction: $\tau_\mathrm{QC}^\mathrm{eff}$ scales with the substrate-level $\mathcal{M}^\mathrm{system}$, not directly with $N_\mathrm{qubits}$.

Falsifier: matter-wave contrast loss correlates only with mass, not with internal-DOF structure; or qubit-system coherence scales linearly with $N_\mathrm{qubits}$ regardless of architecture-specific cross-coupling.

#### Test 3 — Topology-perturbation thresholds (Class B)

For topological qubits: measure $\tau_\mathrm{QC}$ as a function of $\Delta_\mathrm{top}$ (varied via material engineering or via temperature). Prediction: exponential dependence $\tau_\mathrm{QC}^B \sim \exp(\Delta/T_\mathrm{eff})$ with the predicted exponent at fixed temperature, transitioning to $\tau_\mathrm{gap-stab}$ binding at large $\Delta/T$.

Falsifier: polynomial rather than exponential dependence on $\Delta_\mathrm{top}/T_\mathrm{eff}$; or gap-stability behavior that does not match the predicted functional form for the topology in question.

#### Test 4 — Redundancy-saturation signatures (Class C)

For multi-timescale photonic platforms: extend Hafezi-class architectures to higher axis counts (3, 4, 5+) and measure FPM relaxation, harmonic-generation bandwidth, yield. Prediction: saturation emerges past ~3–5 axes due to correlated optical-mode coupling.

For bosonic codes: scale code distance and measure logical-qubit lifetime. Prediction: plateau emerges past distance $\sim N_\mathrm{corr}^\mathrm{photon}$ due to correlated photon-loss.

Falsifier: continued monotonic improvement with axis-count or code-distance, with no plateau in the explored range.

### 2.8 Sharp-vs-structural verdict, claim by claim

| Claim | Sharp / Structural | Falsifiability |
|---|---|---|
| Three architectural classes are exhaustive over substrate-level base strategies | Sharp (closed Memo 4) | A genuine Class D would refute |
| Each class has a substrate-determined ceiling | Sharp (form-FORCED) | No-ceiling behavior in any class would refute |
| System-multiplicity wall exists in Class A | Sharp (form-FORCED) | Continued unbounded improvement past projected wall would refute |
| Wall location 140–250 kDa for matter waves | Inherited (empirical anchor) | Sharper measurement may shift the value; substrate-level form unchanged |
| $N_\star$ for SC qubit systems | Inherited | Determined up to architecture-specific calibration |
| Exponential gap-suppression in Class B | Sharp (form-FORCED) | Polynomial or other form would refute |
| Specific value of $\Delta_\mathrm{top}^{\max}$, $T_\mathrm{eff}^{\min}$ | Inherited | Dependent on substrate / material / engineering frontier |
| Correlation-budget saturation in Class C | Sharp (form-FORCED) | Unbounded redundancy scaling would refute |
| Specific $N_\mathrm{corr}$ for any Class C platform | Inherited | Determined by substrate-coupling pattern |
| Cross-platform unification of matter-wave and qubit-system walls | Sharp (form-FORCED + cross-anchor) | A platform whose Class A wall is inconsistent with the matter-wave anchor (under appropriate calibration) would refute |
| Specific mass-wall to qubit-wall calibration | Inherited | Architecture-specific |
| Class A → Class C transition is mandatory at the wall | Sharp (form-FORCED) | A Class A architecture surpassing the wall without composition with Class C would refute |
| Class B overtakes Class A at $\Delta/T \gtrsim 10$–20 | Sharp form, inherited threshold | Inversion of class-ordering at substrate-allowed parameters would refute |
| Class C saturation past $\sim N_\mathrm{corr}$ | Sharp (form-FORCED) | Continued exponential scaling past saturation would refute |

The arc's predictive content is therefore: **mostly sharp at the structural level, mostly inherited at the numerical level**. Same form-FORCED + value-INHERITED demarcation as the rest of the program.

### 2.9 The arc's central falsifier

The cross-platform unification claim is the central falsifier of the arc. If a future platform is identified that:

- exhibits coherence properties consistent with no class assignment (A, B, or C), AND
- the platform's behavior cannot be explained as a meta-architectural composition of A/B/C, AND
- the platform's $\tau_\mathrm{QC}$ does not match $M$ under any substrate-allowed parameter calibration,

then $M$ is refuted at the structural level. The framework would need to be either extended (Class D introduced) or replaced.

Conversely, if the four primary anchors (matter-wave, SC, topological, multi-timescale) plus all secondary anchors continue to be consistent with one $M$ function across the next decade of platform development — and the cross-platform calibration constraints ($\mathcal{M}_\mathrm{crit}$ from matter-wave fixing $N_\star$ for qubit systems, etc.) hold quantitatively — that is significant cross-platform evidence for the substrate framework.

### 2.10 Honest scope

What this memo delivers:

- Class-by-class scaling laws and ceilings, with form-FORCED structure and INHERITED specific values.
- Cross-platform unification: matter-wave Q-C boundary and qubit-system walls are the same substrate phenomenon.
- Position of current SOTA platforms on $M$.
- Three sharp cross-class transition predictions (A → C mandatory, B overtakes A, C saturation).
- Four classes of near-term experimental tests, each with clear falsification conditions.
- Honest sharp-vs-structural verdict for every prediction.

What this memo does NOT deliver:

- Closed-form numerical predictions for any specific platform's ceiling.
- Closed-form $\mathcal{M}_\mathrm{crit}$, $\Gamma_\mathrm{min}$, $N_\mathrm{corr}$, $\Delta_\mathrm{top}^{\max}$, etc. INHERITED throughout.
- Specific architecture-to-platform calibration constants for the matter-wave-to-qubit-system cross-platform identity.

The arc is now ready for synthesis (Memo 7) and publication-grade paper.

---

## 3. Consequences for the Arc

1. **Block D's predictive content is delivered.** Sharp form-level claims with falsification conditions; inherited specific values with provisional ranges where empirical anchors permit.

2. **The arc has produced what it was opened to deliver.** Memo 1 asked: what is QC in ED, and what are its limits? Memos 2–6 answer: QC is the engineered occupation of an unresolved substrate regime, characterized by UR-1; its limits are set by the multiplicity-cap function $M$ with three architectural-class projections; ceilings are exponentially-scale-different across classes; cross-platform unification is achieved.

3. **The matter-wave / qubit-system identity is the program's most cross-domain-unifying prediction yet.** It connects an existing empirical anchor (the 140–250 kDa Q-C boundary) directly to a future experimental frontier (SC qubit scaling) via substrate-level structural identity. This is the kind of cross-platform consistency claim that distinguishes substrate-level frameworks from phenomenological ones.

4. **The four near-term experimental tests are concrete enough to be pursued today.** Test 1 (coherence-scaling plateau) is essentially being run by the qubit industry already; the framework predicts a structurally-specific plateau character. Test 2 (multiplicity-growth probes) requires modest extensions to existing matter-wave and qubit-tomography techniques. Test 3 (topology-perturbation thresholds) maps onto the active topological-qubit research program. Test 4 (redundancy-saturation signatures) is testable in current Hafezi-class and bosonic-code platforms.

5. **The cross-domain echo with BH-2 holds at the predictive level.** Both decoupling-surface formation in BH-2 and condition (ii) failure in QC scale via $\Gamma_\mathrm{cross}$ collapse. The substrate-level mechanism is the same; the falsifiers in different platforms test different aspects of one underlying structure.

6. **Predictive content is honest about what's sharp and what's inherited.** Same methodology as Phase-1, Arc D, Arc SG, Arc BH. No overclaim; clear demarcation of form-FORCED structure from value-INHERITED specifics.

---

## 4. Recommended Next Step

**Memo 7 — Arc synthesis and Clay-relevance-style verdict.**

File: `theory/Quantum_Computing/Arc_QC_7_Synthesis.md`.

Scope:

- Synthesize Memos 1–6 into a coherent architectural picture of QC in ED.
- Deliver the FORCED / INHERITED / OPEN classification across the arc.
- State the Clay-relevance-style structural verdict: arc-level structural completeness; honest demarcation; explicit open extensions.
- Update program-state: Arc Q-COMPUTE closed at architectural level; new active-priority-list status; integration with broader program.
- Identify natural follow-on arcs: closed-form $\mathcal{M}_\mathrm{crit}$ derivation (parallel to E4 / closed-form-$\log g$), specific architecture-to-platform calibration work, and any open cross-domain consistency tests that emerge from the arc's predictions.
- Prepare arc for publication-grade paper.

Estimated 1 session.

After Memo 7, the arc is closed at the architectural level and ready for the publication-grade paper analogous to *Black Holes in Event Density* and *Foundations of Substrate Gravity*. The natural follow-on is the Q-COMPUTE foundations paper: substrate-level architecture for the QC sector, parallel in form and methodology to BH-Foundations and SG-Foundations.
