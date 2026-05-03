# Arc QC — Memo 3: Failure-Mode Rates

**Status:** Memo 3 of Arc Q-COMPUTE. Block B (failure-mode quantification). Architect-mode active. Form-FORCED / value-INHERITED methodology.

**Date:** 2026-05-02

---

## 1. Structural Summary

Each UR-1 condition (i), (ii), (iii) admits a substrate-level dynamical equation governing the rate at which the relevant invariant ($\mathcal{M}$, $\gamma_{ij}$, $\Lambda$-integrated) crosses its threshold. This memo derives those dynamics, identifies the substrate-determined timescales $\tau_{(\mathrm{i})}, \tau_{(\mathrm{ii})}, \tau_{(\mathrm{iii})}$ at which each condition fails, and combines them into the QC operating window:

$$
\boxed{\;\tau_\mathrm{QC} = \min\bigl(\tau_{(\mathrm{i})},\,\tau_{(\mathrm{ii})},\,\tau_{(\mathrm{iii})}\bigr)\;}
$$

Each timescale is **architecture-class-dependent**: which condition binds, and how long, depends on the substrate-geometric configuration the architecture maintains. The class-dependence pattern is the input Block C will audit for exhaustiveness.

OQ-6 closes fully: $\mathcal{M}$ and $\mathcal{U}$ are *genuinely independent dimensions* of substrate state. $\mathcal{U}$ can fall while $\mathcal{M}$ is held fixed (via (ii) or (iii) failure); $\mathcal{M}$ can drift while $\mathcal{U}$ is held fixed (within UR-1 tolerance). Three substrate-state axes — $\mathcal{M}$ (region-property), the gradient-geometry of $\sigma$ underwriting $\gamma_{ij}$ (substrate-geometry property), and $\Lambda$ (commitment-rate property) — are jointly required.

---

## 2. Derivation / Argument

### 2.1 Condition (i) — multiplicity dynamics and $\tau_{(\mathrm{i})}$

#### 2.1.1 Substrate-level dynamics of $\mathcal{M}$

Per ED-I-01 §2.3, multiplicity is the ED analogue of entropy: it grows under environmental forcing and is held bounded by structural mechanisms. The substrate-level dynamical equation is, at leading order:

$$
\frac{d\mathcal{M}}{dt}\bigg|_\mathcal{S} = \underbrace{\alpha_\mathrm{env}\,\Lambda_\mathrm{env}(t)}_{\text{environmental ED-injection}} + \underbrace{\alpha_\mathrm{act}\,S_\mathrm{int}(t)}_{\text{internal pathway-activation}} - \underbrace{A_\mathcal{S}\,(\mathcal{M} - \mathcal{M}_\mathrm{floor})}_{\text{architectural restoring}}.
$$

- $\alpha_\mathrm{env}$: substrate coupling between environmental injection and pathway-count growth. ED-I-01 §2.5 establishes the mechanism: each ED-injection event opens a fraction of new participation pathways, scaling roughly with the V1 kernel temporal width.
- $\alpha_\mathrm{act}\,S_\mathrm{int}$: rate at which the system's internal degrees of freedom activate new pathways from thermal or operational stimulation. For matter waves this is mass-dependent; for SC qubits it is gate-operation-dependent.
- $A_\mathcal{S}\,(\mathcal{M} - \mathcal{M}_\mathrm{floor})$: architectural restoring rate. The structural mechanism (lattice symmetry, topological gap, engineered redundancy-stabilization) drives $\mathcal{M}$ toward the architecturally-imposed floor $\mathcal{M}_\mathrm{floor}$.

In steady state with active architectural restoring: $\mathcal{M} \approx \mathcal{M}_\mathrm{floor} + (\alpha_\mathrm{env}\,\Lambda_\mathrm{env} + \alpha_\mathrm{act}\,S_\mathrm{int})/A_\mathcal{S}$.

#### 2.1.2 Failure timescale $\tau_{(\mathrm{i})}$

Condition (i) fails when $\mathcal{M}$ crosses $\mathcal{M}_\mathrm{crit}$. From the dynamics:

- **Static failure mode (mass-cap class):** if $\mathcal{M}_\mathrm{floor}$ itself exceeds $\mathcal{M}_\mathrm{crit}$, the system *cannot* be operated in the unresolved regime regardless of timescale. This is the matter-wave Q-C boundary at 140–250 kDa: as molecular mass grows, $\mathcal{M}_\mathrm{floor}(M)$ — the molecule's intrinsic-internal-DOF participation count — rises, and at $M \sim 140$–$250$ kDa, $\mathcal{M}_\mathrm{floor}(M)$ crosses $\mathcal{M}_\mathrm{crit}$. No experimental window. This is condition (i) failing at $\tau_{(\mathrm{i})} = 0$.

- **Dynamic failure mode:** if $\mathcal{M}_\mathrm{floor} < \mathcal{M}_\mathrm{crit}$ but environmental injection drives the steady-state above threshold, the system has a finite operating window:
  $$
  \tau_{(\mathrm{i})} \sim \frac{\mathcal{M}_\mathrm{crit} - \mathcal{M}_\mathrm{floor}}{\alpha_\mathrm{env}\,\Lambda_\mathrm{env} + \alpha_\mathrm{act}\,S_\mathrm{int} - A_\mathcal{S}\,(\mathcal{M}_\mathrm{ss} - \mathcal{M}_\mathrm{floor})}
  $$
  with the denominator the *net* multiplicity-growth rate after architectural restoring.

#### 2.1.3 Empirical anchors

- **Matter-wave Q-C boundary 140–250 kDa.** $\mathcal{M}_\mathrm{floor}(M)$ scales with molecular internal DOFs (rotational + vibrational + electronic populating thermally accessible modes). The mass-scaling is INHERITED from molecular physics; the fact that $\mathcal{M}_\mathrm{floor}$ *exists and grows monotonically* is FORCED. The boundary location at 140–250 kDa is a value-INHERITED prediction with form-FORCED structure.
- **Internal-DOF activation thresholds.** Below the Q-C boundary, dropping into colder vacuum or longer flight time can extend coherence — direct test of the dynamic failure mode.
- **Decoherence-by-thermal-radiation (Hornberger et al.).** A probe of $\alpha_\mathrm{env}$: blackbody photons from internal molecular emission carry away sufficient ED-injection to push $\mathcal{M}_\mathrm{eff}$ above threshold. Standard physics describes this as "which-path information leaving the molecule"; ED reads it as environmental ED-injection lifting $\mathcal{M}$.

### 2.2 Condition (ii) — cross-bandwidth dynamics and $\tau_{(\mathrm{ii})}$

#### 2.2.1 Substrate-level dynamics of $\gamma_{ij}$

From DCGT (Arc D): $\gamma_{ij}(t) \sim \exp[-\alpha\int_\mathrm{path}\sigma(\mathbf{x},t)\,d\ell]$. The cross-bandwidth evolves because $\sigma(\mathbf{x},t)$ evolves under substrate dynamics + architectural maintenance + environmental perturbation.

At leading order:

$$
\frac{d\gamma_{ij}}{dt} = -\frac{1}{\tau_\mathrm{dec}^{(\mathrm{ii})}}\bigl(\gamma_{ij} - \gamma_\mathrm{floor}\bigr) + \xi(t)
$$

with:

- $\tau_\mathrm{dec}^{(\mathrm{ii})}$: characteristic decay timescale set by substrate gradient-erosion + architectural-pumping balance.
- $\gamma_\mathrm{floor}$: substrate-supported steady-state cross-bandwidth, set by the architecture.
- $\xi(t)$: stochastic forcing from environmental perturbation of the gradient profile.

#### 2.2.2 Failure timescale $\tau_{(\mathrm{ii})}$

Condition (ii) fails when $\gamma_{ij}$ falls below $\Gamma_\mathrm{min}$ along any rule-spanning pathway. Two regimes:

- **Sustained-above-threshold regime:** $\gamma_\mathrm{floor} > \Gamma_\mathrm{min}$ with margin. Stochastic excursions below threshold are rare (Poisson-class). Mean first-passage time:
  $$
  \tau_{(\mathrm{ii})} \sim \tau_\mathrm{dec}^{(\mathrm{ii})}\,\exp\!\left[\frac{(\gamma_\mathrm{floor} - \Gamma_\mathrm{min})^2}{2\,\sigma_\xi^2}\right]
  $$
  exponentially long — Kramers-class escape from the protected configuration. This is the substrate-level analog of phase-coherence preservation in well-isolated SC qubits.

- **Near-threshold regime:** $\gamma_\mathrm{floor} \approx \Gamma_\mathrm{min}$, by architectural design (Josephson junctions). Fluctuations frequently push below threshold, and each crossing produces a global rule reconfiguration (ED-I-29: tunneling). MQT rate is the *Poisson rate of below-threshold excursions*:
  $$
  \tau_{(\mathrm{ii})}^{-1} = \tau_\mathrm{MQT}^{-1} \sim \omega_0\,\exp\!\left[-\alpha\!\int_\mathrm{barrier}\sigma\,d\ell\right]
  $$
  with $\omega_0$ a substrate-attempt frequency. **This recovers the WKB exponential structure of MQT directly from DCGT** — same exponential as $\Gamma_\mathrm{cross}$, evaluated at the engineered barrier.

#### 2.2.3 Empirical anchors

- **JJ MQT rates (Devoret-Martinis-Clarke 1985).** Exponential dependence on barrier height/width. Reproduced as the substrate $\kappa$ function evaluated at the engineered $\sigma$-profile of the barrier. Architecturally: the JJ is designed to live at the (ii) boundary; its functional behavior is set by $\tau_{(\mathrm{ii})}$.
- **SC qubit T₂.** Coherence between qubit endpoints (encoded in JJ phase) decays as the engineered low-$\sigma$ pathway erodes under quasiparticle generation, dielectric noise, and stray flux. T₂ is the substrate-level mean first-passage time below $\Gamma_\mathrm{min}$ for the qubit's cross-endpoint pathway.
- **Photonic-channel loss.** $\gamma_{ij}$ between input and output endpoints of a photonic channel decays as the gradient-architecture (waveguide structure, scattering centers) erodes the protected pathway. ED-I-12: photonics is the engineering of ED-gradients; loss is the gradient-architecture's failure to sustain $\gamma_{ij}$.

### 2.3 Condition (iii) — commitment-injection dynamics and $\tau_{(\mathrm{iii})}$

#### 2.3.1 Substrate-level dynamics of $\Lambda_\mathcal{S}$

The commitment-survival factor is $\exp[-\int_0^t \Lambda_\mathcal{S}(t')\,dt']$. This factor crosses any threshold $\mathcal{U}_\mathrm{min}^{(\mathrm{iii})}$ at:

$$
\int_0^t \Lambda_\mathcal{S}(t')\,dt' = \ln\!\left(\frac{1}{\mathcal{U}_\mathrm{min}^{(\mathrm{iii})}}\right).
$$

For roughly time-stationary $\Lambda_\mathcal{S}$:

$$
\tau_{(\mathrm{iii})} = \frac{\ln(1/\mathcal{U}_\mathrm{min}^{(\mathrm{iii})})}{\Lambda_\mathcal{S}} = \frac{\ln(1/\mathcal{U}_\mathrm{min}^{(\mathrm{iii})})}{\Lambda_\mathrm{env} + \Lambda_\mathrm{int}}.
$$

#### 2.3.2 Sources of $\Lambda_\mathrm{env}$ and $\Lambda_\mathrm{int}$

- $\Lambda_\mathrm{env}$ — environmental ED-injection. Sourced by external coupling channels: thermal radiation, residual-gas collisions, Purcell decay into electromagnetic modes, dielectric noise, magnetic-flux fluctuations, cosmic-ray strikes, quasiparticle injection from above-gap excitations. Each channel contributes additively at leading order. Bounded below by the V1 vacuum kernel itself (no environment is perfectly cold; the substrate's V1 floor sources a residual rate).
- $\Lambda_\mathrm{int}$ — internal P11 commitment-event rate. Includes intentional commitments (gates, ancilla resets, intermediate measurements as part of error-correcting protocols) and incidental commitments (internal scattering events, leakage-out-of-computational-subspace events).

#### 2.3.3 Empirical anchors

- **SC qubit T₁ (energy relaxation).** Identified as $\tau_{(\mathrm{iii})}$ for a single-qubit unresolved rule, with $\Lambda_\mathrm{env}$ dominated by Purcell decay + quasiparticle poisoning + dielectric loss in the engineered geometry.
- **Quasiparticle poisoning** (anomalous T₁ events). Direct ED-injection channel: a quasiparticle entering the SC island lifts $\mathcal{M}$ locally and forces individuation. Both $\Lambda_\mathrm{env}$ and (through induced multiplicity) $\tau_{(\mathrm{i})}$ are affected.
- **Matter-wave coherent flight time.** Set by background-gas collision rate + blackbody emission rate. $\tau_{(\mathrm{iii})}^\mathrm{MW}$ is the maximum interferometer transit time before environmental ED-injection drives $\mathcal{U}$ below threshold.
- **Topological-qubit error suppression.** In Class B architectures, $\Lambda_\mathrm{env}$ for the *protected subspace* is exponentially suppressed by the topological gap — most environmental modes do not couple to the rule. $\tau_{(\mathrm{iii})}^\mathrm{top} \gg \tau_{(\mathrm{iii})}^\mathrm{trivial}$.

### 2.4 The QC operating window

Combining:

$$
\tau_\mathrm{QC} = \min\bigl(\tau_{(\mathrm{i})}, \tau_{(\mathrm{ii})}, \tau_{(\mathrm{iii})}\bigr).
$$

Three structural observations:

1. **Different architectures bind on different conditions.** Each architectural class is characterized not by which timescale is *longest* but by which is *shortest* — i.e., which UR-1 condition is the architecture's binding constraint. Block C's exhaustiveness audit pivots on this.

2. **The operating window is a substrate observable.** $\tau_\mathrm{QC}$ is what experimentalists call "coherence time," "circuit-execution-window," or "fault-tolerance-headroom-time." Its empirical behavior across platforms is the program's empirical anchor for Block D.

3. **Architectural design is the optimization of $\min$.** Improving the longest of three timescales is irrelevant; a QC architect must improve the *shortest*. This is why platform improvements often plateau when the binding constraint changes from (e.g.) (iii) to (i) and the engineering effort no longer addresses the new binding constraint.

#### 2.4.1 Matter-wave check

Matter-wave Q-C: $\tau_{(\mathrm{ii})} \to \infty$ (vacuum gradient is smooth; $\gamma$ between arms is well above threshold). Below the mass cap: $\tau_{(\mathrm{i})}$ from environmental injection-driven $\mathcal{M}$ growth, comparable to $\tau_{(\mathrm{iii})}$ from the same environmental injection through the commitment channel. Above the mass cap: $\tau_{(\mathrm{i})} = 0$ (static failure of (i)). The Q-C boundary is where $\tau_{(\mathrm{i})}$ collapses from finite-and-environmentally-set to zero.

#### 2.4.2 SC qubit check

SC qubit: $\tau_{(\mathrm{iii})}$ (≈ T₁) and $\tau_{(\mathrm{ii})}$ (≈ T₂) are typically the binding constraints, with $\tau_{(\mathrm{i})}$ usually held longer by the engineered low-$\mathcal{M}$ structure (until a quasiparticle event lifts $\mathcal{M}$, which simultaneously shortens both $\tau_{(\mathrm{i})}$ and $\tau_{(\mathrm{iii})}$). Modern SC platforms with T₁ ≈ T₂ ≈ 100 μs–1 ms have $\tau_\mathrm{QC} \sim$ minimum of those, set by the binding environmental-injection channel.

#### 2.4.3 JJ-as-element check

JJ used as a coherent element (not a qubit): designed to live at $\tau_{(\mathrm{ii})}$ binding boundary. DC Josephson behavior persists because the engineered $\gamma_\mathrm{floor}$ is just above $\Gamma_\mathrm{min}$; coherence is *enforced* by the substrate-geometric design. MQT happens at the rate $\tau_{(\mathrm{ii})}^{-1}$ characteristic of the engineered barrier.

### 2.5 Closing OQ-6 fully

OQ-6 asked: are $\mathcal{M}$ and $\mathcal{U}$ independent dimensions of substrate state?

Memo 2 partially closed: $\mathcal{U}$ depends on $\mathcal{M}$ but also on $\sigma$ and $\Lambda$. Memo 3 closes fully: the dynamics are *triply distinct*. $\mathcal{U}$ degrades from three different substrate processes — multiplicity growth, gradient-bandwidth collapse, commitment accumulation — only one of which is $\mathcal{M}$. A system can be in any of the following states:

- High $\mathcal{U}$, low $\mathcal{M}$ — operating QC.
- High $\mathcal{U}$, briefly elevated $\mathcal{M}$ but well below $\mathcal{M}_\mathrm{crit}$ — perturbed but recoverable.
- Low $\mathcal{U}$, low $\mathcal{M}$ — connectivity collapse (ii) or commitment (iii) drove $\mathcal{U}$ down without changing $\mathcal{M}$.
- Low $\mathcal{U}$, high $\mathcal{M}$ — full classical regime, all three conditions failed.

The first three states are accessible without any change in $\mathcal{M}$, demonstrating $\mathcal{U}$ has dynamics independent of $\mathcal{M}$. **OQ-6 closes: $\mathcal{M}$ and $\mathcal{U}$ are genuinely separate substrate-state axes**, with $\sigma$-geometry and $\Lambda$-rate as the additional independent dimensions $\mathcal{U}$ depends on.

### 2.6 Architectural-class rate-pattern (input to Block C)

For each provisional architectural class, the rate pattern looks structurally distinct:

| Class | Hypothesized binding constraint | Mechanism for slacking the other two |
|---|---|---|
| **A** — engineered-low-multiplicity (SC qubits, ions, gate-model photonic) | $\tau_{(\mathrm{iii})}$: environmental ED-injection through engineered isolation. | Lattice/structural restoring on (i); engineered low-$\sigma$ pathways on (ii). |
| **B** — global-geometric-rigidity (topological qubits, Chern channels, geometric-phase) | $\tau_{(\mathrm{ii})}$: rigidity of the *topologically protected* cross-bandwidth pathway is the load-bearing protection. | Gap-suppressed environmental coupling on (iii); $\mathcal{M}$ at floor by topological protection on (i). |
| **C** — high-multiplicity-redundancy (Hafezi multi-timescale, multi-axis) | Condition (i) is *relaxed by architectural design*. The architecture allows $\mathcal{M}$ above what Class A would tolerate, and uses redundancy to keep effective $\mathcal{U}$ high despite multiple individuated pathways. | Effective $\Gamma_\mathrm{cross}$ enhanced by multiple parallel pathways; $\Lambda$ for the protected information distinct from $\Lambda$ for any single mode. |

This pattern is the **input** Block C will audit. The provisional three-class structure now has a sharp test: do the three classes correspond to *three different binding-condition strategies*? If yes, exhaustiveness over UR-1's three conditions is plausible. If a fourth substrate-allowed strategy exists that doesn't bind on any of the three (e.g., dynamically-rotating which condition binds, or a combined-protection scheme that doesn't reduce to one binding choice), Class D is needed.

### 2.7 Updated invariants / definitions list

| Symbol | Meaning | Status | Source |
|---|---|---|---|
| $\tau_{(\mathrm{i})}, \tau_{(\mathrm{ii})}, \tau_{(\mathrm{iii})}$ | Failure timescales for UR-1 conditions (i), (ii), (iii) | DERIVED (this memo) | this memo |
| $\tau_\mathrm{QC} = \min(\tau_{(\mathrm{i})}, \tau_{(\mathrm{ii})}, \tau_{(\mathrm{iii})})$ | QC operating window | DEFINED | this memo §2.4 |
| $\alpha_\mathrm{env}, \alpha_\mathrm{act}, A_\mathcal{S}$ | Multiplicity dynamics rate constants | NAMED, INHERITED | this memo §2.1 |
| $\mathcal{M}_\mathrm{floor}$ | Architecturally-imposed multiplicity floor | DEFINED | this memo §2.1 |
| $\tau_\mathrm{dec}^{(\mathrm{ii})}, \gamma_\mathrm{floor}$ | $\gamma_{ij}$ dynamics constants | NAMED, INHERITED | this memo §2.2 |
| $\Lambda_\mathrm{env}, \Lambda_\mathrm{int}$ | Environmental and internal commitment rates | DEFINED | Memo 2 §2.4, this memo §2.3 |
| Class-A/B/C binding-condition pattern | Hypothesized | this memo §2.6 |

### 2.8 Honest scope

What this memo delivers:

- Substrate-level dynamics for $\mathcal{M}$, $\gamma_{ij}$, and $\Lambda_\mathcal{S}$.
- Failure timescales $\tau_{(\mathrm{i})}, \tau_{(\mathrm{ii})}, \tau_{(\mathrm{iii})}$ in form-FORCED structure with INHERITED values.
- $\tau_\mathrm{QC} = \min(\cdot)$ as the substrate-level coherence-window observable.
- Empirical-anchor reductions: matter-wave Q-C boundary, JJ MQT, SC T₁/T₂, photonic-channel loss, topological-qubit error suppression — all reduce to specific UR-1 condition failures with substrate-level rate predictions.
- OQ-6 fully closed.
- Class-rate-pattern table (input to Block C).

What this memo does NOT deliver:

- Closed-form values of $\alpha_\mathrm{env}$, $A_\mathcal{S}$, $\tau_\mathrm{dec}^{(\mathrm{ii})}$, etc. INHERITED.
- The specific value of the matter-wave Q-C boundary mass. INHERITED from molecular physics + $\mathcal{M}_\mathrm{crit}$ calibration.
- The exhaustiveness of Class A/B/C. Block C target.
- The multiplicity-cap function $M$. Block D target.

Verdict-class projection consistent with Memos 1–2: form-FORCED on rate-equation structure and on the $\tau_\mathrm{QC} = \min(\cdot)$ relationship; value-INHERITED on the specific timescales.

---

## 3. Consequences for the Arc

1. **Block B closes.** All three failure-mode rates derived; $\tau_\mathrm{QC}$ defined; OQ-6 closed.

2. **Block C is now sharply specified.** The architectural-class exhaustiveness audit becomes: do classes correspond to *which UR-1 condition is each architecture's binding constraint*? If the three-class hypothesis maps cleanly onto the three conditions (Class A → (iii)-binding via isolation; Class B → (ii)-binding via global rigidity; Class C → (i)-relaxation via redundancy), exhaustiveness is plausible. The audit must confirm or refute this mapping.

3. **The $\tau_\mathrm{QC} = \min(\cdot)$ structure is the empirical observable.** Coherence-time data across SC qubit platforms, ion traps, photonic gate-model devices, topological-qubit progress, multi-timescale photonics, and matter-wave interferometers are all measurements of $\tau_\mathrm{QC}$ for different binding conditions. Block D's $M$ function will need to reproduce all of these as different projections of the same substrate machinery.

4. **Architectural design = optimizing $\min(\cdot)$.** This recovers what platform-development teams empirically know: improving the dominant timescale is what matters; improving non-binding timescales is wasted effort. The substrate provides the structural reason.

5. **The matter-wave Q-C boundary is a $\tau_{(\mathrm{i})} \to 0$ static failure.** It is structurally distinct from SC T₁ (a $\tau_{(\mathrm{iii})}$ phenomenon) and JJ MQT (a $\tau_{(\mathrm{ii})}$ phenomenon). Three different empirical signatures, three different UR-1 conditions, one substrate framework.

6. **Quasiparticle poisoning is a multi-condition event.** A quasiparticle entering an SC qubit raises both $\mathcal{M}$ (failing (i)) and $\Lambda$ (failing (iii)). This kind of multi-condition perturbation will matter for Block D — the multiplicity-cap function must handle correlated-failure events, not only single-condition crossings.

---

## 4. Recommended Next Step

**Memo 4 — Architectural-class exhaustiveness audit (Block C opens).**

File: `theory/Quantum_Computing/Arc_QC_4_Architectural_Class_Audit.md`.

Scope:

- Test the hypothesis that the three architectural classes (A, B, C) correspond exhaustively to three binding-condition strategies in UR-1: A binds on (iii), B binds on (ii), C relaxes (i) by redundancy.
- For each class, derive *how the substrate-geometric configuration* enforces the binding pattern, using closed-arc results: ED-I-01 (Class A bulk SC), ED-I-23 (Class A JJ qubits), ED-I-14 + ED-I-18 (Class B topological + global-geometric), ED-I-18 (Class C multi-timescale redundancy), ED-I-12 (Class B photonic).
- Audit for substrate-allowed Class D candidates: any substrate-geometric protection strategy not reducible to one of (A)/(B)/(C). Candidates to consider: dynamically-rotating-binding architectures (e.g., topological + dynamical decoupling); coherence-by-engineered-environment (reservoir engineering); error-correction-as-architecture (does logical-qubit protection constitute its own substrate-class or is it a reapplication of one of A/B/C at a higher level?); hybrid approaches.
- Honest verdict: three-class exhaustive, four-or-more needed, or some classes collapse on closer inspection.
- Closes OQ-2; partially closes OQ-4 and OQ-5.

Estimated 2–3 sessions (the audit is more substantive than the rate-derivation memo because it must test multiple candidate architectures against the substrate constraints).

If exhaustiveness closes cleanly (three classes confirmed), Memo 5 opens Block D with the multiplicity-cap function $M$. If a Class D is identified, the arc accommodates it before proceeding to $M$.
