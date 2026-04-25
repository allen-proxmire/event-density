# Arc N Scoping — Non-Markovian Structure

**Arc N Stage N.0 — Opening Scoping Memo**
**Status:** Scoping only. Defines the Arc N problem (whether ED admits or requires non-Markovian structure), enumerates three candidate mechanisms (N1 bandwidth-memory, N2 commitment-memory, N3 adjacency-memory), three potential sources (S1 Primitive 11 commitment, S2 Primitive 13 relational timing, S3 Q.8 vacuum response), three potential constraints (C1 Lorentz covariance, C2 spin-statistics, C3 UV-FIN), and a five-substage roadmap (N.1 cataloguing → N.2 forced-evaluation → N.3 refuted-evaluation → N.4 cross-arc implications → N.5 synthesis). Honest framing: Arc N may produce a mixed verdict like Arc Q, leaning toward "non-Markovianity ADMISSIBLE but bounded by C1/C2/C3 constraints" rather than strongly FORCED or strongly REFUTED. Arc N is independent of Arcs R/M/Q at primitive level; its closure does not require additional Phase-2 work but its results may back-flow into Arc Q.5 radiative corrections and Q.8 vacuum structure.

---

## 1. Purpose of Arc N

### 1.1 The non-Markovian question

Phase-2 (Arc R + Arc M + Arc Q) closed the structural framework for ED's quantum sector under the working assumption of *Markovian* chain evolution: at each primitive event, commitment and individuation depend only on the current state of the bandwidth fields and rule-type interface content, not on prior history. This assumption was made for tractability — it kept the Phase-2 derivations local in time and amenable to standard Lagrangian / Hamiltonian / Lindblad-style structural arguments.

The assumption was never *primitive-derived*. Nothing in Primitives 01–13 explicitly forbids history-dependence in bandwidth content $b_K$, commitment dynamics, or multi-chain adjacency relations. Conversely, nothing in Primitives 01–13 explicitly *forces* non-Markovian structure either. Arc N's purpose is to evaluate this open question structurally:

(Q-N) **Does ED admit or require non-Markovian structure in chain evolution or multi-chain interactions?**

### 1.2 Three Arc N targets

Arc N investigates three sub-questions:

- **(N-Admit):** Does the ED primitive stack *admit* non-Markovian structure as a consistent extension?
- **(N-Force):** Does any subset of primitives *force* non-Markovianity at primitive level?
- **(N-Refute):** Are there any structural constraints that *forbid* non-Markovianity in particular sectors (e.g., specific commitment dynamics, specific vacuum structure)?

The honest expected verdict — recorded up front per the methodological discipline established in M.0 and Q.0 — is *mostly admissible, partially constrained*. ED's primitive stack is unlikely to force non-Markovianity globally (no primitive carries that content explicitly), but it may admit non-Markovian structure in specific sectors (bandwidth-memory, vacuum-response memory) subject to constraints from Lorentz covariance, spin-statistics, and UV-FIN.

### 1.3 Why Arc N matters

Three reasons motivate Arc N as a substantive arc rather than a footnote:

(i) **Empirical relevance.** Non-Markovian dynamics appear in many physical contexts: open-quantum-system memory kernels, non-local response functions, vacuum-fluctuation correlations across timescales, cosmological structure formation with persistent memory. If ED admits non-Markovian structure, the framework gains additional descriptive scope without modification of primitives.

(ii) **Cross-arc implications.** Non-Markovian structure in commitment dynamics could modify Arc Q.5 radiative-correction analysis (loop integrals with memory kernels), Arc Q.8 vacuum structure (history-dependent effective vacuum), and Arc M σ_τ (spectral-rate averages with memory-weighted kernels). If non-Markovianity is admissible in these sectors, the Phase-2 closures inherit caveats; if not, the closures are robust.

(iii) **Phase-3 foundations.** ED → GR coupling at cosmological scales (Phase-3) involves long-timescale dynamics where Markovian assumptions are typically inadequate. Arc N's verdict on non-Markovian structural admissibility provides a foundational input to Phase-3 cosmological-coupling analyses.

---

## 2. Background

### 2.1 ED primitives are Markov-compatible but not Markov-forcing

A review of Primitives 01–13 against the Markovian / non-Markovian distinction:

- **Primitive 01 (micro-event):** discrete events; no inherent temporal structure beyond "events happen at points." Markov-compatible.
- **Primitive 02 (chain):** worldlines $\gamma_K$ are continuous structures with persistent identity. The chain *itself* is a memory-bearing object — its existence is a temporal continuity claim — but the *dynamical update rule* along $\gamma_K$ is not constrained to be Markovian by Primitive 02 alone.
- **Primitive 03 (participation):** instantaneous; no memory content.
- **Primitive 04 (bandwidth):** four-band decomposition specifies amplitudes at each event but does not specify whether the amplitudes evolve Markovianly. **Candidate site for non-Markovian structure.**
- **Primitive 06 (four-gradient):** Lorentz covariance constrains the *form* of dynamical equations but does not pick Markov over non-Markov.
- **Primitive 07 (rule-type):** Lever L1 specifies bandwidth partition pattern $w_\tau^X$; whether $w_\tau^X$ is constant in time or dynamically history-dependent is not specified by Primitive 07.
- **Primitive 09 (polarity phase):** instantaneous; no inherent memory.
- **Primitive 10 (individuation):** threshold-crossing event-class; instantaneous in formulation, but the *threshold value* could in principle depend on prior chain history. **Candidate site for non-Markovian structure.**
- **Primitive 11 (commitment):** discrete events along $\gamma_K$. Each commitment is a point-event, but the *rate* and *content* of commitment events can in principle depend on prior commitment history. **Candidate site for non-Markovian structure.**
- **Primitive 13 (relational timing):** proper time $\tau_K$ along $\gamma_K$. Proper time is a continuous parameter; it does not enforce locality in proper time at the dynamical level. **Candidate site for non-local temporal structure.**

In summary: no primitive forbids non-Markovian structure; several primitives (04, 10, 11, 13) admit it as a structurally consistent extension.

### 2.2 Phase-2 Markovian assumptions

Phase-2 derivations made implicit Markovian assumptions at three points:

- **Stage R.1 minimal coupling:** the gauge-covariant derivative $D_\mu = \partial_\mu + (iq/\hbar) A_\mu$ is a *local* operator in spacetime; non-local memory kernels could in principle replace $\partial_\mu$ with a history-weighted derivative.
- **Arc M σ_τ master formula:** the proper-time average $\langle (\partial \ln b)^2 \rangle_\tau$ is implicitly a *local* average; non-Markovian extension would weight prior history of $b$ in the average.
- **Arc Q.7 second quantisation:** canonical (anti-)commutation relations are *equal-time* relations; non-Markovian extensions admit unequal-time commutation structure with memory content.

In each case, the Markovian form was selected for tractability and matches standard QFT machinery. Whether the non-Markovian extension is *primitive-admissible* or *primitive-required* is Arc N's question.

### 2.3 Existing memory-kernel work

A precursor memo `memory_kernel_derivation.md` [1] sketched a Nakajima-Zwanzig-style non-Markovian memory kernel for ED chain evolution with environmental coupling. That memo predates the full Phase-2 closure and treated non-Markovianity as a *platform-specific* phenomenon (e.g., specific dissipative-environment couplings) rather than as a structural primitive-level feature. Arc N revisits the question at the primitive level, building on the Phase-2 closures.

### 2.4 Non-Markovianity in standard physics

For context (informational only):

- **Open quantum systems:** non-Markovian master equations (Nakajima-Zwanzig, time-convolutionless) describe systems with memory of bath state.
- **Linear response theory:** generalised susceptibilities $\chi(\omega)$ with frequency dependence encode memory-kernel structure.
- **Cosmological structure formation:** persistent gravitational memory effects (Christodoulou memory, ordinary memory) involve non-Markovian dynamics.
- **Electroweak / QCD vacuum dynamics:** vacuum-condensate evolution in cosmology involves history-dependent effective fields.

These contexts confirm that non-Markovian structure is empirically relevant; Arc N evaluates whether ED admits or forces it structurally.

---

## 3. Central Question

The Arc N central question:

> **(Q-N) Does ED admit or require non-Markovian structure in chain evolution or multi-chain interactions?**

Three sub-questions structure the investigation:

- **(Q-N.A)** *Admissibility.* Is non-Markovian structure consistent with Primitives 01–13 + Phase-2 closures?
- **(Q-N.F)** *Forcing.* Do any primitive-level constraints *force* non-Markovianity in specific sectors?
- **(Q-N.R)** *Refutation.* Do any primitive-level constraints (Lorentz, spin-statistics, UV-FIN) *forbid* non-Markovianity in specific sectors?

The honest expected outcome (recorded for calibration, not derivation): Q-N.A likely YES (admissibility broad); Q-N.F likely NO (no primitive forces non-Markovianity globally); Q-N.R likely YES in restricted sectors (Lorentz covariance + UV-FIN may forbid certain memory-kernel forms).

---

## 4. Three Candidate Mechanisms for Non-Markovianity

Arc N enumerates three candidate primitive-level mechanisms by which non-Markovian structure could enter ED's framework. Each is independently evaluable; they may coexist or operate in disjoint sectors.

### 4.1 N1 — Bandwidth-memory

**Statement.** The bandwidth fields $b_K^X(x^\mu)$ at event $x^\mu$ depend not only on the participation amplitude at $x^\mu$ but on a history-weighted integral over prior events on the worldline:
$$
b_K^X(x^\mu) = \int_{-\infty}^{\tau_K(x^\mu)} K_X(\tau_K(x^\mu) - \tau') \cdot \mathrm{(participation\ at\ \tau')} \, d\tau'
$$
with memory kernel $K_X(\Delta\tau)$ that decays on some characteristic timescale $\tau_\mathrm{mem}^X$.

**Primitive-level basis.** Primitive 04 specifies the four-band decomposition but does not specify whether each band's amplitude evolves Markovianly. The Markovian limit corresponds to $K_X(\Delta\tau) \to \delta(\Delta\tau)$; finite-width $K_X$ is the non-Markovian extension.

**Candidate sectors.** Most plausibly active in $b^\mathrm{env}$ (environment-coupled band): environmental influences propagate with finite response times, naturally producing memory kernels. Less plausibly in $b^\mathrm{int}$ (rule-type-internal): internal structure is typically conservative.

**Constraints.** C1 (Lorentz covariance) requires $K_X$ to be Lorentz-scalar-form-compatible — memory kernels along $\gamma_K$ must respect proper-time covariance. C3 (UV-FIN) requires $K_X$ to be bounded at short timescales (no $\delta$-function divergences amplified by finite kernels).

### 4.2 N2 — Commitment-memory

**Statement.** The Primitive 10 individuation threshold and Primitive 11 commitment rate at event $x^\mu$ depend on the rule-type's commitment-event history $\{x^\mu_1, x^\mu_2, \dots, x^\mu_n\}$ along $\gamma_K$, not only on the current bandwidth state.

**Primitive-level basis.** Primitive 11 produces discrete commitment events along $\gamma_K$; the commitment dynamics could in principle depend on the full event history rather than only the current state. Primitive 10's individuation threshold could similarly be history-dependent — e.g., a chain that has recently undergone many commitment events might have a temporarily-elevated threshold (refractory-period-like behaviour).

**Candidate sectors.** Most plausibly active in dense-commitment regimes where the commitment rate per dτ is high enough that finite recovery times affect subsequent dynamics. Less plausibly in sparse-commitment regimes where each event is well-separated.

**Constraints.** C2 (spin-statistics) constrains how commitment-memory interacts with the (anti-)commutation structure of Arc Q.7: history-dependent threshold modifications must preserve $\eta = (-1)^{2s}$ at the structural level. C1 (Lorentz covariance) requires history-dependence to respect proper-time invariance.

### 4.3 N3 — Adjacency-memory

**Statement.** Multi-chain adjacency graphs (Primitive 10 individuation) at event $x^\mu$ encode not only current chain-pair distinguishability but also temporal correlations across adjacency-graph evolution. Two chains that have been adjacent for a long time may carry persistent correlation structure beyond their instantaneous state.

**Primitive-level basis.** Primitive 10's adjacency relation is in principle a snapshot at each event; Arc Q.2 §6 closed R-2 (gauge-quotient individuation) via *adjacency-equivalence-class* construction, which respects gauge equivalence at each event but does not address temporal correlation across events. Adjacency-memory would extend the equivalence-class structure to *adjacency-equivalence-trajectories* — equivalence classes of adjacency-graph time-evolutions.

**Candidate sectors.** Most plausibly active in entangled multi-chain systems where joint participation has temporal correlations beyond instantaneous coincidence (Arc R Bell-correlation analogue at multi-event scale). Less plausibly in isolated single-chain systems.

**Constraints.** C2 (spin-statistics) constrains adjacency-memory's interaction with Pauli exclusion: adjacency-memory in Case-R sectors must preserve antisymmetry. C3 (UV-FIN) constrains the temporal range of admissible correlations.

---

## 5. Three Potential Sources of Non-Markovianity

The candidate mechanisms N1–N3 require primitive-level *sources* — specific aspects of Primitives 01–13 that could supply the history-dependence content.

### 5.1 S1 — Primitive 11 (commitment) as a discrete history-bearing process

Each commitment event along $\gamma_K$ is a discrete fact about the chain's history. The accumulation of commitment events constitutes a *commitment record* — a discrete sequence of events that the chain has experienced. If subsequent dynamics depend on this record (rather than only on the current bandwidth state), Primitive 11 supplies the substrate for N2 (commitment-memory).

**Strength as source.** Strong. Primitive 11 is intrinsically a history-bearing process: commitment events are discrete and accumulate. The Markovian assumption that subsequent dynamics depend only on current state is a *choice*, not a primitive-level commitment.

**Constraints.** Primitive 11's locality (each commitment is a point-event) does not directly constrain history-dependence; locality is about where commitments occur, not about what their effects depend on.

### 5.2 S2 — Primitive 13 (relational timing) allowing non-local temporal structure

Primitive 13 supplies proper time $\tau_K$ along $\gamma_K$ as the invariant relational clock. The clock structure does not enforce *locality in proper time*: dynamical equations could in principle involve proper-time derivatives at multiple points along $\gamma_K$, producing non-local-in-time evolution.

**Strength as source.** Moderate. Primitive 13 supplies the temporal-parameter substrate, but does not by itself enforce or forbid non-locality in time. Non-local temporal structure would require additional primitive-level commitment beyond what Primitive 13 supplies.

**Constraints.** Lorentz covariance (Primitive 06): non-local temporal structure must respect Lorentz invariance, which restricts admissible memory kernels to those built from Lorentz-scalar combinations along $\gamma_K$.

### 5.3 S3 — Vacuum response (from Arc Q.8) as a history-dependent environment

Arc Q.8's effective vacuum $|0\rangle_\tau^\mathrm{eff}$ carries transient $\tau$-participation in $b^\mathrm{env}$ of charged-matter rule-types. The vacuum response to perturbations could be *history-dependent*: a rule-type interacting with the vacuum at event $x^\mu$ might experience an effective coupling that depends on the vacuum's response to perturbations at earlier events.

**Strength as source.** Moderate-strong. Vacuum response is a natural site for memory kernels in standard QFT (e.g., dispersion relations, dielectric response). ED's effective-vacuum framework admits the same structure conditional on the underlying multi-chain dynamics being non-Markovian.

**Constraints.** Q.8's vacuum-structure analysis does not by itself force or forbid non-Markovian vacuum response; it leaves the question open. UV-FIN (C3) constrains the high-frequency behaviour of vacuum response kernels.

---

## 6. Three Potential Constraints

Three primitive-level structural features could constrain admissible non-Markovian forms.

### 6.1 C1 — Lorentz covariance

**Constraint.** Memory kernels must be Lorentz-scalar combinations. For chain-local memory kernels along $\gamma_K$, this restricts admissible forms to those built from proper-time invariants (e.g., $K(\Delta\tau)$ as a function of proper-time difference, with $\Delta\tau$ a Lorentz scalar). For multi-chain memory kernels, Lorentz scalar combinations of multi-event coordinates are required.

**Strength as constraint.** Strong. Lorentz covariance is a Phase-2 FORCED structural feature (Arc R [2] R.1, R.2.5); any non-Markovian extension must preserve it.

**Forbidden forms.** Memory kernels that distinguish a preferred frame (e.g., $K(\Delta t)$ in a fixed Lorentz frame) are REFUTED by Lorentz covariance.

### 6.2 C2 — Spin-statistics structure

**Constraint.** Non-Markovian structure must preserve $\eta = (-1)^{2s}$ at the structural level. For Case-R rule-types, history-dependent extensions must maintain the antisymmetry that yields Pauli exclusion. For Case-P rule-types, symmetry must be maintained.

**Strength as constraint.** Strong. Spin-statistics is an Arc R FORCED theorem; any non-Markovian extension that violates it would refute the theorem's structural completeness.

**Forbidden forms.** Memory kernels that mix Case-R and Case-P statistics across temporal correlations (e.g., a kernel that produces apparent $\eta$ violations at finite memory range) are REFUTED by spin-statistics.

### 6.3 C3 — UV-FIN

**Constraint.** Non-Markovian structure must preserve primitive-level UV finiteness from Arc Q [3] Theorem Q3. Memory kernels with sufficiently slow decay at short timescales could amplify high-frequency contributions and threaten UV-FIN; bounded kernels are admissible, divergent kernels are not.

**Strength as constraint.** Moderate-strong. UV-FIN is FORCED by Primitives 01 + 13 + 04; any non-Markovian extension that violates UV finiteness would refute UV-FIN's structural status.

**Forbidden forms.** Memory kernels with $K(\Delta\tau) \sim \Delta\tau^{-\alpha}$ for $\alpha \geq$ some critical value (depending on integrand structure) are REFUTED by UV-FIN. Bounded kernels and exponentially-decaying kernels remain admissible.

---

## 7. Arc N Roadmap

Arc N proceeds through five substages.

### 7.1 N.0 — This memo (scoping). **Complete.**

Defines the Arc N problem, three candidate mechanisms (N1–N3), three potential sources (S1–S3), three potential constraints (C1–C3), and the roadmap.

### 7.2 N.1 — Catalogue admissible non-Markovian structures

`non_markov_catalogue.md`. Systematically enumerate admissible non-Markovian extensions in each candidate sector:

- **N1-admissible:** classes of bandwidth-memory kernels compatible with C1/C2/C3.
- **N2-admissible:** classes of commitment-memory mechanisms compatible with C1/C2.
- **N3-admissible:** classes of adjacency-memory structures compatible with C2/C3.

Each class characterised by its primitive-level realisation, its constraint-compliance, and its potential cross-arc effects (Arc M σ_τ, Arc Q.5 radiative, Arc Q.8 vacuum).

### 7.3 N.2 — Evaluate FORCED candidates

`non_markov_forced.md`. For each admissible class from N.1, evaluate whether any primitive-level argument *forces* it to be active. Honest expected verdict: most admissible non-Markovian structures will be ADMISSIBLE-BUT-NOT-FORCED, paralleling the pattern of Arc M (most masslessness mechanisms admissible, few forced) and Arc Q.4 (multiple Higgs mechanisms admissible, none forced).

Possible exceptions where primitives may force non-Markovianity:

- **Vacuum response (S3 + N1 in $b^\mathrm{env}$):** the effective vacuum's response to perturbations may *require* a finite-width memory kernel for consistency with UV-FIN (a $\delta$-function response would amplify high-frequency contributions). If true, this would be a structurally FORCED non-Markovian element.
- **Commitment refractory periods (S1 + N2):** if Primitive 11's discrete event structure imposes a primitive-level minimum interval between commitment events at the same chain location, this would be a structurally FORCED non-Markovian element. Currently SPECULATIVE.

### 7.4 N.3 — Evaluate REFUTED candidates

`non_markov_refuted.md`. For admissible classes from N.1 that violate any of C1/C2/C3, classify as REFUTED. Likely targets:

- **Frame-dependent memory kernels** (violate C1).
- **Memory kernels mixing Case-R and Case-P statistics** (violate C2).
- **Power-law memory kernels with insufficient decay** (violate C3).
- **Memory kernels producing instantaneous-coincidence violations** at finite memory range (violate C2 in Case-R sectors).

The REFUTED catalogue identifies which non-Markovian extensions are forbidden by Phase-2 structural commitments.

### 7.5 N.4 — Cross-arc implications

`non_markov_implications.md`. Evaluate the implications of admissible / forced / refuted non-Markovian classes for:

- **Vacuum structure (Arc Q.8):** does admissible non-Markovian vacuum response modify the Q.8 vacuum factorisation $\bigotimes_\tau |0\rangle_\tau$? Likely *no* at the structural level (factorisation is a kinematic statement); *yes* at the dynamical-response level (effective-vacuum coupling kernels gain memory content).
- **Radiative corrections (Arc Q.5):** non-Markovian loop-integrand structure modifies effective propagators. Numerical content remains INHERITED; form-level effects on transversality (vacuum-pol) and tree-level $g = 2$ need to be checked for preservation.
- **Mixing and CP structure (Arc Q.6):** non-Markovian Yukawa interactions could in principle generate effective phase content beyond the standard CKM/PMNS framework. Likely admissible structurally; specific values remain INHERITED.
- **Cosmological boundary conditions (Phase-3):** long-timescale non-Markovian dynamics in vacuum response or cosmological-Λ contributions are natural targets. This is a Phase-3 deliverable rather than an Arc N closure, but Arc N supplies the structural admissibility framework.

### 7.6 N.5 — Synthesis

`arc_n_synthesis.md`. Integrate N.0–N.4 into a final Arc N verdict. Expected closure: **non-Markovian structure ADMISSIBLE in restricted sectors (specifically environment-coupled bandwidth and effective-vacuum response), bounded by C1/C2/C3 constraints, with neither global FORCED nor global REFUTED status.**

The synthesis records:

- FORCED non-Markovian elements (if any — possibly in vacuum response under S3 + N1 + UV-FIN).
- ADMISSIBLE-NOT-FORCED non-Markovian extensions.
- REFUTED non-Markovian forms.
- Cross-arc implications back-flowing into Arc Q closures.
- Phase-3 hand-off content.

### 7.7 Estimated scope

- N.0 (this memo): 1 substage.
- N.1: 1–2 sessions.
- N.2 + N.3: 2–3 sessions.
- N.4: 1–2 sessions.
- N.5: 1 session.
- **Arc N total: 5–9 sessions.**

Comparable to Arc M's 4–7-session estimate. Smaller than Arc Q's 10–18-session estimate. Arc N is independent of other arcs at primitive level; its closure does not block Phase-3 but provides additional structural input.

---

## 8. Honest Framing

### 8.1 What Arc N realistically can achieve

- **Catalogue admissible non-Markovian structures** (high feasibility).
- **Identify constraint violations** from C1/C2/C3 (high feasibility).
- **Evaluate cross-arc implications** for Q.5, Q.6, Q.8 (moderate feasibility).
- **Identify potential FORCED elements** in restricted sectors (moderate feasibility — vacuum response under UV-FIN is the most plausible candidate).

### 8.2 What Arc N realistically cannot achieve

- **Predict specific memory-kernel values.** All numerical magnitudes remain INHERITED from empirical / platform-specific data.
- **Solve the cosmological-Λ value problem.** Non-Markovian vacuum response is structurally admissible but does not by itself fix the Λ magnitude.
- **Force a specific non-Markovian mechanism for the universe.** ED's primitive structure is unlikely to force a unique non-Markovian form globally.

### 8.3 Verdict-distribution prior (calibration)

Honest expected outcome distribution:

- **40% admissible-bounded:** non-Markovian structure ADMISSIBLE in restricted sectors; bounded by C1/C2/C3; no global FORCED status.
- **30% mixed-with-one-FORCED-element:** non-Markovian vacuum response under S3 + N1 + UV-FIN may be FORCED; other sectors admissible-not-forced.
- **20% mostly-Markovian:** Phase-2 Markovian assumptions found to be tightly constrained by Phase-2 closures; non-Markovian extensions mostly REFUTED.
- **10% surprise:** unexpected primitive-level structural mechanism produces non-trivial Forced non-Markovian content.

Arc N's job is to produce a verdict grounded in primitive-level analysis, not to confirm this prior. The prior is recorded for calibration only.

### 8.4 Methodological discipline

Arc N follows the M.0 / Q.0 methodological pattern:

- *Clear separation* of FORCED / CANDIDATE / REFUTED / INHERITED.
- *Honest expected-verdict prior* up front; updated against findings.
- *Cross-arc implications* explicitly evaluated; back-flow effects on Phase-2 closures recorded.
- *Form-FORCED, value-INHERITED* framing preserved: ED's primitives may force structural memory-content classifications without predicting specific kernel values.

---

## 9. Cross-References

### 9.1 Upstream

- Phase-1 closure: `qm_emergence_closure.md`.
- Arc R closure: `arc_r_stage1_synthesis.md`, `rule_type_taxonomy_synthesis.md`, `dirac_emergence.md`.
- Arc M closure: `chain_mass_synthesis.md`.
- Arc Q closure: `arc_q_synthesis.md`.
- Phase-2 synthesis: `phase2_synthesis.md`.
- Memory-kernel precursor: `memory_kernel_derivation.md`.

### 9.2 Downstream (Arc N substages, forthcoming)

- `non_markov_catalogue.md` (N.1).
- `non_markov_forced.md` (N.2).
- `non_markov_refuted.md` (N.3).
- `non_markov_implications.md` (N.4).
- `arc_n_synthesis.md` (N.5).

### 9.3 Phase-3 hand-off

Arc N's verdict supplies structural input for Phase-3 cosmological / GR-coupling work, particularly:

- Long-timescale vacuum dynamics (cosmological-Λ analysis).
- Cosmological-boundary-condition admissibility for non-Markovian vacuum response.
- Empirical signatures of non-Markovian structure at high-energy / cosmological scales (paralleling UV-FIN's empirical-signatures route).

---

## 10. One-Line Summary

**Arc N opens an independent thread investigating whether ED admits, forces, or refutes non-Markovian structure: three candidate mechanisms (N1 bandwidth-memory, N2 commitment-memory, N3 adjacency-memory) drawing on three potential sources (S1 Primitive 11 commitment as history-bearing, S2 Primitive 13 relational timing admitting non-local temporal structure, S3 vacuum response as history-dependent environment) bounded by three potential constraints (C1 Lorentz covariance, C2 spin-statistics, C3 UV-FIN), with a five-substage roadmap (N.1 catalogue → N.2 forced-evaluation → N.3 refuted-evaluation → N.4 cross-arc implications → N.5 synthesis) producing an expected mixed verdict of admissible-bounded non-Markovian structure with possible FORCED elements in vacuum response — paralleling Arc M's H1-dominant pattern and Arc Q's mostly-positive pattern at the temporal-locality layer.**
