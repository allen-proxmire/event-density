# Key Findings and Takeaways of the Event Density Research Programme

**Allen Proxmire**
**Last updated: 29 March 2026**

---

## 1. What ED Has Demonstrated

### 1.1 A Unique Canonical PDE Derived from Seven Axioms

The Event Density (ED) programme begins with four primitives — a bounded scalar density field, a degenerate nonlinear mobility, a monostable penalty, and a global participation variable — and derives a unique canonical PDE from seven structural axioms (locality, isotropy, gradient-driven flow, dissipative structure, single scalar field, minimal coupling, dimensional consistency). No other known scalar PDE simultaneously possesses all five distinguishing features of the ED system: degenerate mobility creating free boundaries, a monostable penalty driving a unique attractor, a global participation variable producing telegraph oscillation, five simultaneous Lyapunov functionals, and the property of not being a gradient flow of any of them.

The derivation is not a postulate. The seven axioms eliminate all alternatives: axioms P1+P2 restrict the operator to functions of local values and derivatives; P3 determines the principal part; P4 constrains the reaction term; P5 excludes non-scalar fields; P6 determines the global coupling; and P7 ensures dimensional consistency. The canonical PDE is the unique second-order system satisfying all seven.

### 1.2 Three Constitutive Channels with Exact Structural Correspondences

The canonical PDE decomposes into three constitutive channels, each of which corresponds exactly to a known physical law when isolated:

| Channel | Operator | Structural correspondence | Accuracy |
|---------|----------|--------------------------|----------|
| **Penalty** | Linear restoring force toward equilibrium | RC-circuit / Debye exponential relaxation | **Exact** (0.00% error) |
| **Mobility** | Divergence-form nonlinear diffusion | Porous-medium equation (Barenblatt self-similarity) | **Exact reduction**; numerical: 1.1% error at accessible resolution |
| **Participation** | Global variable with damped feedback | Telegraph / RLC oscillation | **Exact** (0.00% error for frequency and damping) |

These are not analogies or approximations. The penalty channel *is* exponential decay: the ODE is identical to the RC-circuit discharge equation. The mobility channel *is* porous-medium diffusion: the PDE reduces exactly to the standard PME under the substitution m = beta + 1. The participation channel *is* a telegraph oscillator: the linearised coupled system is mathematically identical to the RLC-circuit equation. The correspondences hold at the level of governing equations, not merely at the level of qualitative behaviour.

### 1.3 Nine Structural Analogues Across Two and Three Dimensions

Six structural analogues were constructed in two dimensions, and three of them were extended to three dimensions. Each analogue isolates or combines constitutive channels, derives an analytical prediction, and tests it numerically against a known physical law. The results are:

**Exact matches (machine precision):**
- Analogue 1: Penalty-only relaxation reproduces RC/Debye decay with 0.00% error across all tested amplitudes, and RLC telegraph frequencies with 0.00% error across all tested values of H.

**Quantitative matches (within 5%):**
- Analogue 2: Mobility-only spreading reproduces Barenblatt self-similarity with 1.1% error for the front-radius exponent (beta = 1) and confirms compact support and self-similar profile convergence.
- Analogue 3: Mobility-plus-penalty dynamics reproduce Stefan free-boundary horizon formation with a 2.5% threshold error, monotone retreat, and lifetime monotonically increasing with amplitude.
- Analogue 5: Mobility-plus-participation coupling reproduces telegraph-modulated PME with frequency scaling omega proportional to H^0.52 (predicted: H^0.50, within 4%) and v-delta frequency matching to 0.03%.

**Scientifically informative negative result:**
- Analogue 4: All three channels active with a horizon-forming initial condition. The telegraph oscillation cannot modulate the horizon boundary because the horizon lifetime and the telegraph period are architecturally coupled through the penalty parameter. This is a structural constraint of the ED architecture, not a numerical artefact.

**Emergent discovery:**
- Analogue 6: Two-peak temporal tension reveals (a) baseline nonlinear-mobility repulsion — an effective force between density structures caused by density-dependent diffusion asymmetry — and (b) telegraph-modulated attraction/repulsion where the participation variable v(t) controls the sign of the drift.

**3D extensions (Analogues 7–9):**
- Analogue 7: 3D Barenblatt confirms the PME reduction with the predicted 3D exponent mapping (alpha_R = 0.2000 predicted, 0.1665 measured for beta = 1; pre-asymptotic at current resolution).
- Analogue 8: 3D Horizon shows a shifted critical amplitude A_c approximately equal to 0.45 (versus 0.41 in 2D), consistent with the stronger Laplacian dissipation in three dimensions. Threshold sharpness, monotone retreat, and lifetime scaling are all preserved.
- Analogue 9: 3D Temporal Tension reproduces all three phenomena observed in 2D — baseline repulsion, telegraph-modulated drift reversal at H = 2, and v-correlated oscillatory dynamics — with no new parameters or channels required.

### 1.4 Dimension-Independence of the Architecture

The three 3D analogues confirm that the structural correspondences are not artefacts of low dimensionality. The PDE reduction (mobility channel to PME) holds identically in any spatial dimension d; only the numerical value of the Barenblatt similarity exponent changes, in accordance with the formula alpha_R = 1/(d(m-1)+2). The horizon threshold shifts predictably with d due to the d-dependent Laplacian. The emergent pair interaction (temporal tension) is qualitatively identical in 2D and 3D. Axiom P7 (dimensional consistency) is validated empirically.

### 1.5 Emergent Phenomena

Two phenomena were discovered during the analogue programme that were not predicted from the analytic theory of individual channels:

1. **Nonlinear-mobility repulsion.** Two localised density peaks on a uniform background repel each other at H = 0. The mechanism is explicit: between the peaks, the tail overlap raises the local density, which lowers the local mobility, causing each peak to diffuse faster on its outer edge than its inner edge. This shifts the centres of mass apart. The effect decays with distance and has no analogue in linear diffusion.

2. **Telegraph-modulated attraction/repulsion.** At H > 0, the global participation variable oscillates via the telegraph mechanism and modulates the effective interaction between peaks. During the negative phase of v(t), the density between the peaks is reduced, increasing local mobility and weakening the repulsion — at sufficient coupling (H = 2), reversing it to net attraction. This creates an oscillatory, distance-dependent, participation-controlled effective pair interaction.

### 1.6 Architectural Limits

The ED architecture has explicitly identified limits:

- **Transient horizons.** ED horizons are free boundaries that form, persist briefly, and collapse as the monostable penalty drives the system toward the unique attractor. They cannot be sustained indefinitely. Analogue 4 demonstrates that the telegraph oscillation cannot modulate the horizon boundary at any accessible parameter combination, because the horizon lifetime and the telegraph period are architecturally coupled through the penalty slope.

- **No pattern formation.** The monostable penalty rules out Turing-type pattern formation. ED does not have the bistable or conserved structure required for stable spatial patterning.

- **No wave propagation.** The PDE is parabolic, not hyperbolic. ED does not support finite-speed wave propagation in the classical sense. It supports finite-speed *front* propagation (via the degenerate mobility), which is structurally distinct.

These limits are not weaknesses — they are testable structural predictions of the architecture.

---

## 2. Why These Findings Matter

### 2.1 ED Is a Constitutive Ontology, Not a Fitted Model

The structural correspondences between ED channels and physical laws are not the result of parameter fitting. The penalty channel produces exponential decay because the monostable penalty is the unique linear restoring force compatible with the dissipative-structure axiom. The mobility channel produces porous-medium diffusion because the capacity-bounded mobility function is the unique degenerate diffusivity compatible with the gradient-flow axiom. These correspondences are built into the constitutive architecture. They would hold for any choice of the numerical parameters D, P_0, M_0, beta.

This is a fundamentally different kind of claim from model fitting. A fitted model says: "with the right parameters, I can reproduce this data." A constitutive ontology says: "with these structural choices, this class of dynamics necessarily follows."

### 2.2 The Channels Generate Known Physical Laws from First Principles

The three constitutive channels — in isolation — reproduce exponential relaxation, nonlinear self-similar diffusion, and telegraph oscillation. These are not obscure or contrived comparisons. They are foundational physical mechanisms that appear across electrodynamics (RC circuits), fluid mechanics (porous-medium flow), and wave physics (telegraph equation). The fact that a single PDE with three constitutive channels produces all three, without any of them being explicitly designed in, is a nontrivial structural result.

### 2.3 The Architecture Is Falsifiable

Every structural analogue has an explicit falsification condition: the predicted feature must be present when the relevant channel is active, absent when the channel is silenced, and controlled by the channel's parameters. Five of the six 2D analogues pass all three conditions completely. The sixth (Analogue 4) produces a scientifically informative negative result that sharpens the boundary of what the architecture can and cannot produce. The three 3D analogues pass their falsification checks as well.

### 2.4 The Results Are Reproducible

All simulations are implemented in the open-source ED-SIM-02 platform. Each analogue has a corresponding module with a single entry-point function. The full test suite (112 tests) and the reproducibility pipeline (9 certification phases) are included in the repository. The numerical results in the foundational paper can be regenerated from the code without modification.

### 2.5 Structural Identities Reveal Architectural Coupling

The analogue programme discovered a structural identity not present in standard PDEs: the participation channel requires the penalty channel to activate. With Neumann boundary conditions and P_0 = 0, the divergence theorem forces the domain-averaged diffusion operator to vanish identically. This means the participation variable v(t) receives no forcing and decays to zero. A nonzero penalty — however small — breaks this degeneracy. The three channels are not fully independent; they are architecturally coupled. This is not a design choice but a mathematical consequence of the PDE structure.

---

## 3. What ED Does Not Claim

### 3.1 ED Does Not Derive General Relativity

ED does not contain a spacetime metric, curvature, geodesics, or an Einstein equation. The transient horizons produced by the mobility degeneracy are structurally analogous to free boundaries in the Stefan problem, not to event horizons in general relativity. The analogy is mathematical, not physical.

### 3.2 ED Does Not Derive Quantum Mechanics

ED does not contain a Hilbert space, superposition, entanglement, a Born rule, or a measurement postulate. The oscillatory dynamics produced by the participation channel are telegraph oscillations, not quantum interference. No claim of quantum derivation is made or implied.

### 3.3 ED Does Not Derive the Standard Model

ED does not contain gauge fields, fermions, bosons, symmetry breaking, or renormalisable interactions. It is a single scalar PDE. The structural correspondences described in this programme are with foundational mechanisms (decay, diffusion, oscillation, free boundaries), not with specific particle-physics phenomena.

### 3.4 ED Does Not Claim to Be a Cosmology

ED does not derive the Friedmann equations, the CMB power spectrum, or the matter power spectrum. A companion paper demonstrates that the ED PDE produces a BAO-like preferred correlation scale, but this scale is set by the telegraph frequency, not by the sound horizon. The comparison is structural, not observational.

### 3.5 ED Does Not Claim to Match Observational Data

The structural analogues are comparisons of mathematical form: the ED channel produces the same equation, scaling law, or dynamical pattern as the physical law. No comparison to measured physical constants, experimental data sets, or astronomical observations is made. ED is tested against the mathematical structure of known laws, not against their empirical content.

### 3.6 ED Does Not Claim to Be a Microscopic Theory

The four primitives (density, mobility, penalty, participation) are not derived from a microscopic theory, a variational principle, or a symmetry group. They are postulated as constitutive choices and tested by their structural consequences. The gap between structural sufficiency and microscopic derivation is the central open problem of the ED programme.

### 3.7 ED Does Not Claim to Replace Existing Physics

ED is a framework for investigating the structural foundations of physical law. It does not claim that its PDE governs actual physical processes. It claims that its constitutive architecture is sufficient to generate a broad family of physics-shaped dynamics, and that this sufficiency is worth understanding.

---

## 4. The Path Toward Describing Physical Reality

### 4.1 Structural Sufficiency as a Scientific Milestone

The foundational paper and its appendices establish structural sufficiency: the four ED primitives are sufficient to generate exponential relaxation, self-similar spreading with compact support, free-boundary formation and retreat, telegraph oscillation, oscillation-modulated nonlinear diffusion, effective pair interactions, and dimension-independent architectural laws. No parameter tuning is involved in these correspondences — they are consequences of the constitutive choices.

Structural sufficiency is not the same as physical derivation, but it is a meaningful scientific milestone. It means that a single, minimal, axiomatically derived PDE can reproduce the mathematical backbone of mechanisms that underlie much of classical and continuum physics. This is a statement about the architecture of physical law, not about any specific physical system.

### 4.2 Physics-Shaped Behaviour Without Tuning

The most striking feature of the ED results is that the structural correspondences hold without tuning. The penalty channel does not need to be calibrated to produce exponential decay — it produces it for all values of the parameters. The mobility channel does not need special initial conditions to produce PME scaling — it does so for any compactly supported perturbation. The correspondences are structural, not parametric.

This is important because it suggests that the ED constitutive choices — degenerate mobility, monostable penalty, global participation — capture something about the logical structure of dissipative, bounded, density-driven systems that is independent of specific physical content.

### 4.3 Dimension-Independence

The 3D analogues confirm that the structural correspondences survive the transition from two to three spatial dimensions. The exponent mapping, horizon threshold, and emergent interaction law are all dimension-independent in their structural content; only numerical parameters shift in accordance with the d-dependent geometry of the Laplacian. This is a necessary condition for any framework that aspires to describe physics in three-dimensional space.

### 4.4 The Gap Between Sufficiency and Derivation

The central open problem is: can the ED primitives be derived from — or connected to — established physical principles? Several paths are under investigation:

- **Geometric connection.** The ED density field induces a Hessian structure at each point. The eigenvalue morphology (filaments, sheets, blobs) documented in the ED-SIM-02 invariant atlas may connect to notions of Riemannian curvature or information geometry.

- **Variational structure.** ED possesses five simultaneous Lyapunov functionals but is not a gradient flow of any of them. Characterising the non-gradient structure may connect ED to Wasserstein gradient flows or GENERIC formalism.

- **Cosmological extension.** The BAO-like preferred correlation scale produced by the ED PDE is a structural feature. Refining it into a quantitative prediction — and comparing it to the observed BAO scale — would require embedding the ED PDE in an expanding-domain framework.

None of these paths has been completed. They are identified here as directions, not claims.

### 4.5 Next Steps

The ED research programme has completed the following milestones:

- Axiomatic derivation of the canonical PDE (ED-Phys series)
- Nine architectural laws validated across dimensions 1–4 (ED-Phys-36 through 40)
- Twelve-family invariant atlas (ED-SIM-02)
- Six 2D structural analogues (foundational paper, Sections 4–9)
- Three 3D structural analogues (foundational paper, Appendix G)
- BAO-like preferred correlation scale (companion paper)
- 112-test reproducibility suite

The immediate next steps are:

1. **Spectral cross-validation.** Reproduce the six analogues using the ETD-RK4 spectral solver to confirm solver-independence.
2. **ED geometry papers.** Connect the Hessian eigenvalue morphology to curvature and develop the geometric interpretation of the density field.
3. **ED cosmology papers.** Embed the PDE in an expanding domain and refine the BAO-like correlation prediction.
4. **Variational analysis.** Characterise the non-gradient-flow structure and its relationship to established variational frameworks.

---

## 5. Summary Table of All Analogues

| # | Name | Channels | Physical law reproduced | Key result | Accuracy | Dim. |
|---|------|----------|------------------------|------------|----------|------|
| 1 | RC / Debye | Penalty | Exponential relaxation | Decay rate matches exactly | **0.00%** | 2D |
| 1b | RLC | Penalty + Participation | Telegraph oscillation | Frequency and damping match exactly | **0.00%** | 2D |
| 2 | Barenblatt | Mobility | Porous-medium self-similarity | Exponent mapping m = beta + 1 confirmed | **1.1%** | 2D |
| 3 | Horizon | Mobility + Penalty | Stefan free boundary | Sharp threshold A_c, monotone retreat | **2.5%** | 2D |
| 4 | Telegraph Horizon | All three | Oscillatory free boundary | Horizons too transient for modulation | Negative result | 2D |
| 5 | Telegraph PME | Mobility + Participation | Oscillation-modulated diffusion | Frequency scaling H^0.52; v-delta match 0.03% | **0.03–4%** | 2D |
| 6 | Temporal Tension | All three | Emergent pair interaction | Nonlinear repulsion + telegraph attraction | Qualitative | 2D |
| 7 | 3D Barenblatt | Mobility | 3D porous-medium self-similarity | PME reduction confirmed; pre-asymptotic convergence | **16.7%** | 3D |
| 8 | 3D Horizon | Mobility + Penalty | 3D Stefan free boundary | A_c shifted to 0.45; all structural patterns preserved | Quantitative | 3D |
| 9 | 3D Temporal Tension | All three | 3D emergent pair interaction | Repulsion + reversal + oscillation confirmed | Qualitative | 3D |

---

## 6. Closing Statement

Event Density is a coherent, reproducible, and falsifiable ontological framework. From four primitives and seven axioms, it derives a unique canonical PDE whose three constitutive channels correspond exactly to known physical laws — exponential decay, porous-medium diffusion, and telegraph oscillation. Nine structural analogues, spanning two and three spatial dimensions, demonstrate that these channels and their combinations are sufficient to generate a broad family of physics-shaped dynamics: self-similar spreading, free-boundary formation, oscillatory modulation, and emergent pair interactions.

The framework has clear limits. It does not derive general relativity, quantum mechanics, or the Standard Model. It does not claim to match observational data. Its horizons are transient, its dynamics are dissipative, and its field is scalar. These limits are not concealed — they are tested, documented, and scientifically informative.

ED is at an early stage. It has established structural sufficiency but not physical derivation. The gap between the two is the central challenge of the programme. What is established is that a minimal constitutive architecture — without fitting, without tuning, and without importing the laws it reproduces — can generate the mathematical structures that underlie much of classical and continuum physics. Whether this architectural sufficiency reflects something deep about the logical structure of physical law, or is instead a coincidence of mathematical form, is a question that further work must answer. The evidence assembled so far suggests the question is worth asking.
