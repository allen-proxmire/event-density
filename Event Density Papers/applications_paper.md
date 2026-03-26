# Physical Applications of the Event-Density Architecture

**From Structural Ontology to Falsifiable Prediction**

Allen Proxmire
March 2026

---

## 1. Introduction

### 1.1 Purpose

The Architectural Canon of the ED cosmology PDE establishes that the Event-Density framework is defined by seven irreducible structural principles and that any dynamical system satisfying these principles belongs to a single universality class $\mathcal{U}_{\mathrm{ED}}$. The Rigour Paper (Appendices C and D) proves the mathematical well-posedness of this class: global existence, asymptotic stability, spectral structure, bifurcation geometry, and closure under constitutive and geometric perturbation.

The present paper asks the next question: *what does the ED architecture predict about the physical world?*

The purpose of this paper is to derive concrete, falsifiable physical predictions from the ED structural ontology and to organize them into a coherent program of empirical tests spanning five domains: quantum mechanics, galactic dynamics, condensed-matter physics, photonics, and phononics. Each prediction follows from the canonical principles alone — not from parameter fitting, not from ad hoc modeling, and not from analogy. The predictions are structural consequences of the architecture, and they stand or fall with the architecture itself.

### 1.2 Relationship to the Rigour Paper

This paper builds directly on the mathematical infrastructure of the Rigour Paper and its appendices:

- **Appendix C** (PDE Analysis) provides the analytic foundation: the well-posedness theory (C.1–C.2), the linearized eigenstructure and spectral gap (C.3–C.4), the nonlinear stability and dissipation channel decomposition (C.5), the bifurcation structure at the critical damping surface (C.6), and the three-stage convergence theorem (C.7). Every physical prediction in the present paper traces back to a specific theorem or proposition in Appendix C.

- **Appendix D** (Universality Class) provides the equivalence-class framework: the definition of ED-equivalence ($\sim_{\mathrm{ED}}$), the closure and invariance theorems, and the universality statement (Theorem D.19) that any system satisfying Principles 1–7 belongs to $\mathcal{U}_{\mathrm{ED}}$. This framework is what makes cross-domain prediction possible: if a physical system can be shown to satisfy the seven principles, the entire architectural ontology applies, and the predictions follow without further assumption.

The relationship between the two papers is division of labor, not dependence of content. The Rigour Paper proves that the ED mathematics is sound. The Applications Paper shows that the ED mathematics has physical content.

### 1.3 ED as a Structural Ontology

A central claim of the ED framework, established in §5 and §7 of the Architectural Canon, is that ED is not a model in the conventional sense. It is a *structural ontology*: a minimal set of irreducible principles that defines an architecture, not a specific equation. The Canonical Equivalence Class (§5) makes this precise — the mobility function $M(\rho)$, the penalty function $P(\rho)$, the domain geometry, and the parameter values may all vary freely, provided the seven principles are maintained. Different equations, same architecture.

This distinction has a direct consequence for physical applications. A model makes predictions by specifying a Lagrangian, fitting parameters to data, and computing observables. A structural ontology makes predictions differently: it identifies the *qualitative features* that any realization of the architecture must exhibit, regardless of the specific constitutive choices. These features — the motifs, laws, geometric objects, and invariants catalogued in the ED-Arch series — are the predictions.

The advantage is robustness. A model's predictions fail when the model's assumptions break down. An ontological prediction fails only when the architecture itself is wrong — when one of the seven principles is violated. This makes the predictions simultaneously broader (they apply to every system in $\mathcal{U}_{\mathrm{ED}}$) and more fragile (a single confirmed violation of any prediction would indict the entire architecture, not just a parameter choice).

### 1.4 ED-Complexity as the Bridge

The mathematical architecture of the ED PDE operates on the density field $\rho(x,t)$ and the participation variable $v(t)$. Physical systems operate on electrons, photons, galaxies, and phonons. The bridge between the abstract architecture and the physical world is **ED-complexity**: the functional

$$
C_{\mathrm{ED}}[\rho] := \int_\Omega |\nabla\rho(x)|^2\,d^d x,
$$

which measures the total gradient content of the density field. ED-complexity is not an additional assumption; it is a derived quantity, the spatial integral of $|\nabla\rho|^2$, which appears naturally in the energy functional $\mathcal{E}$ (Appendix C, eq. C.3), the dissipation identity (Appendix C, eq. C.6), and the nonlinear triad coupling (Appendix C, §C.4.5).

ED-complexity plays four roles in the physical applications:

1. **Ordering.** It provides a scalar measure that ranks physical systems by the spatial inhomogeneity of their density fields. Systems with low $C_{\mathrm{ED}}$ (spatially uniform, high symmetry) are near the equilibrium $\rho^*$; systems with high $C_{\mathrm{ED}}$ (spatially structured, low symmetry) are far from it.

2. **Dynamics.** The dissipation identity (Lemma C.6) shows that the rate of energy decrease is bounded below by $D\int P'(\rho)|\nabla\rho|^2/M(\rho)\,dx$, which is monotone in $C_{\mathrm{ED}}$. High-complexity configurations dissipate faster. This is the dynamical content of the Modal Hierarchy Law: high spatial modes decay faster than low ones (Proposition C.29).

3. **Thresholds.** The nonlinear stability theorem (Theorem C.43) identifies a threshold $\epsilon_0$ below which exponential convergence is guaranteed. When translated into physical variables, this threshold becomes a critical ED-complexity: systems below it exhibit stable, coherent behavior; systems above it undergo rapid relaxation. The existence of this threshold is a structural prediction of the architecture, not an adjustable parameter.

4. **Cross-domain comparison.** Because $C_{\mathrm{ED}}$ depends only on the gradient structure of $\rho$, it applies identically to any physical system whose dynamics can be written in the canonical ED form. A quantum wavefunction, a galactic mass distribution, a condensed-matter order parameter, and a photonic mode profile can all be compared on the same ED-complexity scale.

### 1.5 Scope of Applications

The physical applications are organized by domain:

**Quantum mechanics** (Section 2). ED predicts that decoherence rates, coherence times, Bell-correlation strengths, and the quantum-classical threshold are governed by ED-complexity rather than by mass or environmental coupling alone. The key predictions are: decoherence scaling as $\Gamma_{\mathrm{decoh}} \sim C_{\mathrm{ED}}$, a sharp complexity threshold for classicality, anomalous coherence in ultra-symmetric systems, and a fundamental limit on quantum error correction.

**Galactic dynamics** (Section 3). ED predicts that galaxy rotation curves, halo profiles, and cluster-collision lensing signatures follow from the temporal-tension structure of the ED density field rather than from dark-matter halos. The key predictions are: the Active/Quiet dwarf-galaxy mass-discrepancy separation (already confirmed in the SPARC dataset), tension-plateau scaling in low-mass systems, halo lag in cluster collisions, and deviations from NFW profiles in activity-dependent systems.

**Condensed-matter physics** (Section 4). ED predicts that pattern-forming systems near criticality — superconductors, Bose–Einstein condensates, liquid crystals — exhibit ED-architectural structure when the order-parameter dynamics satisfy Principles 1–7. The key predictions are: complexity-dependent phase coherence lengths, ED-triad signatures in nonlinear pattern spectra, and mobility-collapse analogues in systems approaching a capacity bound.

**Photonics** (Section 5). ED predicts that nonlinear optical media supporting spatial solitons and mode interactions exhibit the ED modal hierarchy and triad selection rules when the governing equations can be cast in canonical form. The key predictions are: locked harmonic ratios in cavity spectra, complexity-dependent mode lifetimes, and regime transitions (oscillatory vs. monotonic relaxation) controlled by an effective damping discriminant.

**Phononics** (Section 6). ED predicts that phonon transport in structured media — metamaterials, nanostructured solids, biological tissues — exhibits ED-complexity-dependent thermal conductivity scaling and mobility-collapse analogues near structural saturation. The key predictions are: gradient-complexity-controlled heat flow, triad-mediated phonon cascades, and horizon-like thermal barriers.

### 1.6 Falsifiability

Every prediction in this paper is stated in a form that can be tested against data. Following the standard established in the ED Experimental Open Note (ED-00, February 2026), each application section contains:

- A **prediction** stated as a quantitative or qualitative relationship.
- The **canonical principle(s)** from which the prediction follows, with references to the specific theorems in Appendix C or D.
- An **experimental path** describing how the prediction can be tested.
- A **falsification criterion**: the specific observation that would refute the prediction.

The predictions are not hedged. If the decoherence rate scales exponentially with mass rather than as a power law in ED-complexity, the prediction fails. If active dwarf galaxies do not show elevated outer-radius mass discrepancies, the prediction fails. If ultra-symmetric systems do not exhibit anomalous coherence, the prediction fails. Each failure would constitute evidence against the specific canonical principle from which the prediction derives, and a pattern of failures would indict the architecture as a whole.

This falsifiability is not incidental. It is a structural feature of the ontological approach. Because the predictions follow from the principles, and because the principles are irreducible (removing any one breaks the architecture, as shown in §4 of the Canon), each failed prediction identifies which principle is at fault. The architecture is not a flexible framework that can absorb arbitrary data; it is a rigid structure that makes sharp claims.

### 1.7 Connection to the ED Experimental Program

The ED Experimental Open Note (ED-00) collects the full set of empirical predictions and experimental paths in a living document. The present paper provides the theoretical derivation underlying those predictions — the chain of reasoning from canonical principle to mathematical theorem to physical consequence to testable claim. The Open Note provides the experimental design; this paper provides the theoretical warrant.

The first completed test — the dwarf-galaxy rotation-curve analysis using the SPARC dataset (Open Note, §8) — has already confirmed an ED prediction: dynamically active dwarf galaxies exhibit a 53% higher outer-radius mass discrepancy than quiet dwarfs, consistent with the ED prediction that increased internal activity generates increased temporal tension, which increases apparent curvature. This result is not a fit; it is a structural prediction, derived from the architecture before the data were examined.

The remaining predictions — quantum decoherence scaling, biological coherence limits, Bell-correlation degradation, interference visibility laws, galactic halo lag, condensed-matter triad signatures, photonic mode locking, and phononic complexity scaling — are open. They constitute the ED experimental program: a systematic effort to test the architectural predictions across every domain where the canonical form can be instantiated.

### 1.8 Outline

The paper is organized as follows.

- **Section 2** defines ED-complexity as the central physical quantity of the architecture and derives its properties from Principles 1–7.
- **Section 3** derives the quantum-mechanical predictions, with emphasis on decoherence scaling and the quantum-classical threshold.
- **Section 4** derives the galactic-dynamics predictions, including the dwarf-galaxy test and the halo-lag prediction.
- **Section 5** derives the condensed-matter predictions, focusing on pattern-forming systems and phase transitions.
- **Section 6** derives the photonic predictions, focusing on nonlinear cavity dynamics and mode interactions.
- **Section 7** derives the phononic predictions, focusing on structured-media thermal transport.
- **Section 8** synthesizes the cross-domain structure, demonstrating that the predictions in all five domains are instances of a single architectural logic.
- **Section 9** concludes with the status of the experimental program and the conditions under which the ED architecture would be falsified.

---

## 2. ED-Complexity

### 2.1 Definition

The central physical quantity of the ED architecture is the **ED-complexity** of a density configuration:

$$
C_{\mathrm{ED}}[\rho] := \int_\Omega |\nabla\rho(x)|^2\,d^d x.
$$

This functional assigns to every density field $\rho(x)$ on a bounded domain $\Omega \subset \mathbb{R}^d$ a non-negative scalar that measures the total spatial inhomogeneity of the configuration. The equilibrium $\rho \equiv \rho^*$ has $C_{\mathrm{ED}} = 0$; any departure from spatial uniformity has $C_{\mathrm{ED}} > 0$.

ED-complexity is not imposed from outside the theory. It is the simplest scalar invariant of the density gradient field $\nabla\rho$, and it appears — necessarily — at every level of the mathematical architecture developed in Appendices C and D. The purpose of this section is to show precisely how $C_{\mathrm{ED}}$ arises from the seven canonical principles, why it governs the physical phenomena that conventional theories attribute to mass or size, and how it serves as the unifying quantity across all physical domains.

### 2.2 How ED-Complexity Arises from the Architecture

Each of the seven canonical principles contributes a distinct structural role to $C_{\mathrm{ED}}$.

**Principle 1 (Operator Structure).** The canonical operator $F[\rho] = M(\rho)\nabla^2\rho + M'(\rho)|\nabla\rho|^2 - P(\rho)$ is a nonlinear functional of $\rho$ and its first two spatial derivatives. The gradient-squared term $M'(\rho)|\nabla\rho|^2$ is the only term in $F[\rho]$ that is quadratic in $\nabla\rho$, and its integrated strength is proportional to $C_{\mathrm{ED}}$. This term drives the nonlinear triad coupling (§2.2, Principle 7 below) and is the source of all inter-modal energy transfer (Appendix C, §C.4.5). Without spatial gradients — that is, at $C_{\mathrm{ED}} = 0$ — the operator reduces to $F[\rho] = -P(\rho)$, and the entire spatial architecture (diffusion, modal hierarchy, harmonic generation) vanishes. ED-complexity is therefore the activation threshold for the spatial content of Principle 1.

**Principle 2 (Channel Complementarity).** The density evolves through the direct channel $D\,F[\rho]$ and the mediated channel $H\,v$, with $D + H = 1$. The dissipation identity (Lemma C.6) shows that the direct-channel dissipation rate is

$$
\mathcal{D}_{\mathrm{diff}} = D\,P_*'\|\nabla\rho\|_{L^2}^2 + D^2 M_*\|\nabla^2\rho\|_{L^2}^2,
$$

which is bounded below by $D\,P_*'\,C_{\mathrm{ED}}$ (Appendix C, eq. C.53). The direct channel dissipates energy in direct proportion to the ED-complexity. The mediated channel, by contrast, dissipates through the participation damping $\mathcal{D}_{\mathrm{part}} = H\zeta\,v^2$ (eq. C.55), which is independent of $C_{\mathrm{ED}}$. The channel complementarity constraint $D + H = 1$ thus partitions the total dissipation into a complexity-dependent component (direct) and a complexity-independent component (mediated). The balance between these two components determines how quickly a given configuration relaxes: high-$C_{\mathrm{ED}}$ states are dominated by direct-channel dissipation; low-$C_{\mathrm{ED}}$ states are dominated by the participation channel.

**Principle 3 (Penalty Equilibrium).** The penalty function $P(\rho)$ with $P(\rho^*) = 0$ and $P' > 0$ provides a restoring force toward $\rho^*$. The penalty dissipation (eq. C.54) is

$$
\mathcal{D}_{\mathrm{pen}} = \frac{D\,P_*'^{\,2}}{M_*}\|\rho - \rho^*\|_{L^2}^2,
$$

which penalizes deviation from the equilibrium density. The Poincare–Wirtinger inequality connects this to $C_{\mathrm{ED}}$: for any function $\rho$ with spatial mean $\bar{\rho}$,

$$
\|\rho - \bar{\rho}\|_{L^2}^2 \leq C_\Omega\,\|\nabla\rho\|_{L^2}^2 = C_\Omega\,C_{\mathrm{ED}}.
$$

Thus the penalty dissipation is controlled from above by ED-complexity: configurations with large gradients necessarily have large $L^2$-deviations from their mean, and the penalty acts to suppress them. The unique equilibrium $\rho^*$ is the unique minimizer of $C_{\mathrm{ED}}$ subject to the stationarity condition $F[\rho^*] = 0$.

**Principle 4 (Mobility Capacity Bound).** The mobility collapse $M(\rho_{\max}) = 0$ introduces a density-dependent modulation of the effective diffusivity. Near the capacity bound, the diffusion coefficient $D\,M(\rho)$ vanishes, and the dissipation integrand $P'(\rho)|\nabla\rho|^2/M(\rho)$ diverges (Proposition C.10). This means that gradients near $\rho_{\max}$ carry *amplified* ED-complexity: a small $|\nabla\rho|^2$ near the horizon generates a disproportionately large dissipation cost. The energy barrier $\Phi(\rho) \to +\infty$ as $\rho \to \rho_{\max}$ (Proposition C.11) ensures that infinite ED-complexity is required to reach the capacity bound. In physical terms, the mobility collapse creates a *complexity horizon*: a region of state space where the cost of maintaining spatial structure becomes infinite, and the system is forced into homogeneity.

**Principle 5 (Participation Feedback Loop).** The participation variable $v$ integrates the operator output $F[\rho]$ and feeds it back into the density equation. For spatially homogeneous perturbations ($C_{\mathrm{ED}} = 0$), the feedback loop sustains oscillations (spirals) or monotonic decay, depending on the damping discriminant. For spatially inhomogeneous perturbations ($C_{\mathrm{ED}} > 0$), the feedback loop couples the spatial complexity to the temporal dynamics: the operator output $F[\rho]$ depends on $\nabla^2\rho$ and $|\nabla\rho|^2$, so higher $C_{\mathrm{ED}}$ produces larger $|F[\rho]|$, which drives stronger participation, which feeds back into the density more vigorously. This creates a complexity-dependent amplification loop that is ultimately stabilized by the diffusive and penalty dissipation.

**Principle 6 (Damping Discriminant).** The canonical damping parameter $\Delta = D + 2\zeta$ classifies the qualitative behavior of the homogeneous mode (Appendix C, §C.3.5). For the spatial modes ($n \geq 1$), the classification is unconditional: they are always overdamped (Theorem C.22(i)), with decay rates $D\alpha_n = D(M_*\mu_n + P_*')$ that increase monotonically with the eigenvalue $\mu_n$. The quantity $C_{\mathrm{ED}}$ determines the *weight* of each mode in the total configuration: in the Fourier–Neumann decomposition $\rho = \rho^* + \sum a_n\varphi_n$,

$$
C_{\mathrm{ED}} = \sum_{n=1}^\infty \mu_n\,a_n^2,
$$

so ED-complexity is the $\mu$-weighted energy across spatial modes. High $C_{\mathrm{ED}}$ means the configuration has significant amplitude in high-frequency modes, which are precisely the modes that the damping discriminant classifies as rapidly decaying.

**Principle 7 (Nonlinear Triad Coupling).** The gradient-squared nonlinearity $M'(\rho)|\nabla\rho|^2$ generates inter-modal energy transfer through the trilinear coupling coefficients $\Gamma_{mnk}$ (Appendix C, §C.4.5). The total rate of nonlinear energy injection into mode $k$ is

$$
\sum_{m,n \geq 1} M_*'\,a_m\,a_n\,\Gamma_{mnk},
$$

which is quadratic in the Fourier amplitudes and therefore quadratic in $\sqrt{C_{\mathrm{ED}}}$. The strength of the triad coupling — and hence the rate of harmonic generation, the amplitude of the locked $k_3/k_1$ ratio, and the spectral fingerprint of the nonlinear interaction — scales with $C_{\mathrm{ED}}$. At $C_{\mathrm{ED}} = 0$, the triad is inactive; at finite $C_{\mathrm{ED}}$, it produces the characteristic spectral structure that is the hallmark of Principle 7.

### 2.3 Why Complexity, Not Mass or Size

In standard physics, decoherence is governed by mass (the particle becomes "too heavy" for quantum effects), entanglement is limited by distance (the particles are "too far apart"), transport is controlled by material properties (conductivity, viscosity), and gravitational halos are attributed to dark matter (whose mass generates the observed curvature). In each case, the governing quantity is extensive: it scales with the amount of matter or the size of the system.

The ED architecture makes a fundamentally different claim. The governing quantity is *not* mass, size, or environmental coupling. It is ED-complexity — the total gradient content of the density field. This claim is not an additional postulate; it is a theorem-level consequence of the canonical structure.

The argument has three steps.

**Step 1: The energy functional depends on gradients, not on mass.** The total energy $\mathcal{E}[\rho, v]$ (eq. C.3) is a functional of $\rho$ and $v$, not of the total mass $\int\rho\,dx$. The density potential $\Phi(\rho) = \int_{\rho^*}^\rho P(r)/M(r)\,dr$ penalizes *deviation from $\rho^*$*, not deviation from zero. Two configurations with the same total mass but different gradient structures have different energies — and therefore different dissipation rates, different stability properties, and different long-time behavior. The architecture is blind to total mass; it sees only the density field and its spatial structure.

**Step 2: The dissipation rate is controlled by gradients, not by size.** The dissipation identity (Lemma C.6) shows that the rate of energy decrease is bounded below by

$$
D\int_\Omega \frac{P'(\rho)}{M(\rho)}\,|\nabla\rho|^2\,dx \geq D\,c_\delta\,C_{\mathrm{ED}},
$$

where $c_\delta = \inf_{\rho \in [\delta, \rho_{\max}-\delta]} P'(\rho)/M(\rho) > 0$. This lower bound is proportional to $C_{\mathrm{ED}}$ and independent of $|\Omega|$ (the domain volume). A small system with large gradients dissipates faster than a large system with small gradients. Domain size enters only through the Neumann eigenvalues $\mu_n$, which affect the modal structure but not the fundamental relationship between dissipation and gradient content.

**Step 3: The stability threshold depends on gradients, not on particle number.** The nonlinear stability theorem (Theorem C.43) guarantees exponential convergence for initial data satisfying $\|\rho_0 - \rho^*\|_{H^s} + |v_0| < \epsilon_0$. The Sobolev norm $\|\rho_0 - \rho^*\|_{H^s}$ controls both the $L^2$-deviation and the first $s$ derivatives. For $s = 1$, this norm is comparable to $\|\rho_0 - \rho^*\|_{L^2} + \sqrt{C_{\mathrm{ED}}[\rho_0]}$. The threshold $\epsilon_0$ is determined by the canonical parameters ($D$, $\zeta$, $\tau$, $P_*'$, $M_*$, $\mu_1$) — not by the number of particles, the system mass, or the domain volume. A system with $10^{23}$ particles and low gradients is more stable than a system with $10$ particles and high gradients.

The physical consequence is stark: **in the ED architecture, a symmetric buckyball ($C_{60}$) is simpler than an asymmetric peptide of smaller mass, and the buckyball's quantum coherence should persist longer — not because it is lighter, but because its ED-complexity is lower.**

### 2.4 The Four Regimes of ED-Complexity

The canonical structure of the ED system organizes the physical behavior into four regimes, each defined by the magnitude of $C_{\mathrm{ED}}$ relative to the architectural parameters.

**Regime I: Equilibrium** ($C_{\mathrm{ED}} = 0$). The density is spatially uniform: $\rho(x) \equiv \bar{\rho}$. The dynamics are governed entirely by the homogeneous mode $(a_0, v)$, which evolves by the $2 \times 2$ matrix $\mathbf{A}_0$ (eq. C.13). The damping discriminant $\Delta = D + 2\zeta$ determines whether the approach to $(\rho^*, 0)$ is oscillatory or monotonic (Theorem C.22). The nonlinear triad is inactive. All dissipation flows through the penalty and participation channels; the diffusive channel is silent.

*Physical examples:* Bose–Einstein condensates in the ground state; perfectly symmetric optical lattices; uniform-density galactic cores; superconducting loops in the Meissner state.

**Regime II: Low complexity** ($0 < C_{\mathrm{ED}} \ll \epsilon_0^2$). The density has small spatial perturbations about $\rho^*$. The linearized dynamics (eq. C.9) provide an accurate description. Each spatial mode $n \geq 1$ decays exponentially at rate $D\alpha_n$ (Theorem C.17(i)). The spectral gap $\gamma$ (Corollary C.18) governs the overall relaxation time. The nonlinear triad operates at leading order, generating harmonics at amplitudes locked by the selection rules (Theorem C.34). The Lyapunov functional $\mathcal{V}$ (Definition C.39) decays exponentially (Theorem C.43).

*Physical examples:* Symmetric nanoparticles with weak surface perturbations; small molecules in interferometric superposition; nearly homogeneous galactic disks; weakly modulated optical fields.

**Regime III: Moderate complexity** ($C_{\mathrm{ED}} \sim \epsilon_0^2$). The density perturbation is of order the stability threshold. The linearized approximation breaks down. The full nonlinear dynamics (system C.1) are required, and the three-stage convergence theorem (Theorem C.76) governs the approach to equilibrium: global bounds (Stage I), algebraic convergence (Stage II), eventual exponential decay (Stage III). The transition from Stage II to Stage III occurs at a time $t_*$ that increases with $C_{\mathrm{ED}}$. The nonlinear triad is fully active, and the spectral fingerprint (the locked $k_3/k_1$ ratio) is at its strongest.

*Physical examples:* Asymmetric biomolecules in quantum experiments; rotationally supported galaxies with structure; strongly modulated optical cavities; phonon-carrying nanostructures.

**Regime IV: High complexity** ($C_{\mathrm{ED}} \gg \epsilon_0^2$). The density field has large spatial gradients. The diffusive dissipation channel dominates: $\mathcal{D}_{\mathrm{diff}} \gg \mathcal{D}_{\mathrm{pen}} + \mathcal{D}_{\mathrm{part}}$ (Proposition C.48(i)). Spatial inhomogeneities are smoothed rapidly, and the system relaxes toward equilibrium on a diffusive time scale. Near the capacity bound $\rho_{\max}$, the mobility collapse amplifies the effective complexity cost (Proposition C.10), creating the horizon-like behavior described in §C.7.6. The relaxation from Regime IV to Regime II passes through Regime III, where the nonlinear triad is transiently activated before being quenched by the decay.

*Physical examples:* Complex biological structures (proteins, viruses, microtubules) in decoherence experiments; dynamically active dwarf galaxies; turbulent photonic cavities; highly structured phononic metamaterials.

### 2.5 Gradient Structure, Mobility Collapse, Penalty Curvature, and Triad Interaction

The four principal architectural mechanisms — gradients, mobility collapse, penalty curvature, and the triad — each contribute a distinct qualitative feature to the complexity-dependent physics.

**Gradient structure** determines the *rate* of dissipation. The leading term in the energy decay (Lemma C.6) is $D\,P_*'\,C_{\mathrm{ED}}$. Systems with larger gradients lose energy faster and relax toward equilibrium sooner. This is the origin of the ED prediction that decoherence rate scales with $C_{\mathrm{ED}}$, not with mass.

**Mobility collapse** determines the *ceiling* of complexity. The energy barrier $\Phi(\rho) \to +\infty$ at $\rho_{\max}$ (Proposition C.11) ensures that no finite-energy configuration can sustain density near the capacity bound. This creates an effective cutoff: the maximum achievable $C_{\mathrm{ED}}$ for a given energy is bounded, and the bound tightens as $\rho$ approaches $\rho_{\max}$. In galactic applications, this cutoff manifests as the Horizon Surface — the density at which gravitational self-reinforcement saturates.

**Penalty curvature** determines the *shape* of the potential well near equilibrium. The second derivative $P_*'' = P''(\rho^*)$ controls the leading nonlinear correction to the restoring force (Theorem C.58, eq. C.76). When $P_*'' > 0$ (convex penalty), the restoring force strengthens superlinearly with displacement, and the approach to equilibrium is faster than the linear prediction. When $P_*'' < 0$ (concave penalty), the restoring force weakens, and the approach is slower. The sign of $P_*''$ does not affect the stability (Theorem C.43 is unconditional in $P_*''$) but it affects the *transient complexity profile*: how $C_{\mathrm{ED}}(t)$ decays from its initial value to zero.

**Triad interaction** determines the *spectral signature* of the decay. As a high-$C_{\mathrm{ED}}$ configuration relaxes, the nonlinear term $M'(\rho)|\nabla\rho|^2$ transfers energy between spatial modes according to the selection rule $k \in \{|m-n|, m+n\}$ (Theorem C.34). This transfer produces a characteristic spectral pattern — the triad fingerprint — that is observable in the Fourier transform of the relaxing density field. The locked $k_3/k_1$ amplitude ratio (Proposition C.35) is independent of the initial amplitude, depending only on the constitutive ratio $M_*'/M_*$ and the eigenvalue structure. This ratio is a *structural invariant* of the ED architecture (Theorem D.14), preserved across all physical domains.

### 2.6 Low vs. High ED-Complexity: A Comparative Table

| Property | Low $C_{\mathrm{ED}}$ | High $C_{\mathrm{ED}}$ |
|----------|------------------------|-------------------------|
| Density profile | Nearly uniform | Strongly structured |
| Active dissipation channel | Penalty + participation | Diffusion-dominated |
| Dominant time scale | $1/\gamma_{\mathrm{hom}}$ (homogeneous relaxation) | $1/(D\alpha_1)$ or faster (modal hierarchy) |
| Regime (Appendix C.5) | Penalty-dominated | Diffusion-dominated |
| Triad activity | Weak (quadratic in $\sqrt{C_{\mathrm{ED}}}$) | Strong (saturates before decay quenches) |
| Approach to $\rho^*$ | Exponential from $t = 0$ | Three-stage: global $\to$ algebraic $\to$ exponential |
| Quantum prediction | Long coherence, strong entanglement | Rapid decoherence, weak correlations |
| Galactic prediction | Small halo, NFW-like profile | Large tension halo, activity-dependent profile |
| Condensed-matter prediction | Long-range phase coherence | Short-range order, rapid pattern dissipation |
| Photonic prediction | Stable mode structure, weak harmonics | Mode instability, strong triad signatures |
| Phononic prediction | Ballistic transport, low scattering | Diffusive transport, complexity-dependent conductivity |

### 2.7 $C_{\mathrm{ED}}$ as the Unifying Quantity

The table in §2.6 reveals the central structural fact of the ED applications program: **the same complexity functional $C_{\mathrm{ED}}$ governs qualitatively different physical phenomena across all five domains.** This is not a coincidence or an analogy. It is a mathematical consequence of the universality theorem (Theorem D.19): any system satisfying Principles 1–7 belongs to $\mathcal{U}_{\mathrm{ED}}$, and within $\mathcal{U}_{\mathrm{ED}}$, the dissipation rate, stability threshold, spectral structure, and long-time behavior are all controlled by $C_{\mathrm{ED}}$.

The unification works as follows.

1. **Different physics, same operator structure.** A quantum system, a galaxy, a condensed-matter pattern, an optical cavity, and a phononic medium may all be governed by different microscopic equations. But if each system's effective dynamics can be cast in the canonical form (D.1) — a density field evolving under a mobility-weighted diffusion plus a gradient-squared nonlinearity minus a restoring force, coupled to a participation variable through two complementary channels — then the architectural consequences follow.

2. **Different $M$ and $P$, same $C_{\mathrm{ED}}$ dependence.** The specific mobility and penalty functions differ between domains: $M$ might encode quantum tunneling amplitudes, gravitational self-interaction, elastic moduli, optical nonlinearities, or phonon scattering rates. But the *structural role* of $M$ and $P$ is the same in every case: $M$ controls the diffusivity, $P$ provides the restoring force, $M(\rho_{\max}) = 0$ creates the capacity bound, $P(\rho^*) = 0$ identifies the equilibrium, and $C_{\mathrm{ED}} = \|\nabla\rho\|_{L^2}^2$ measures the departure from that equilibrium. The theorems of Appendix C — the dissipation identity, the spectral gap, the stability estimates, the convergence rates — hold for every constitutive choice satisfying Principles 3 and 4.

3. **Different $\Omega$, same architectural layers.** The domain $\Omega$ might be the configuration space of a molecule, the disk of a galaxy, the surface of a thin film, the cross-section of a fiber, or the unit cell of a metamaterial. The Neumann eigenvalues $\mu_n$ change with the domain, but the architectural layers — the modal hierarchy, the triad selection rules, the regime geometry, the three-stage convergence — persist (Theorem D.10).

4. **One number, many predictions.** In each domain, the ED prediction takes the form: *the relevant physical observable scales with $C_{\mathrm{ED}}$, not with the conventionally assumed variable.* Decoherence scales with $C_{\mathrm{ED}}$, not with mass. Halo formation scales with $C_{\mathrm{ED}}$, not with dark-matter density. Phase coherence length scales with $C_{\mathrm{ED}}$, not with temperature alone. Mode lifetime scales with $C_{\mathrm{ED}}$, not with cavity finesse alone. Thermal conductivity scales with $C_{\mathrm{ED}}$, not with material density alone. In every case, the conventional variable is a proxy for $C_{\mathrm{ED}}$ — correlated with it in typical regimes, but decoupled from it in the specific configurations where ED makes distinctive predictions.

The remainder of this paper derives these predictions domain by domain, traces each one to the specific canonical principle and Appendix C theorem from which it follows, and identifies the experimental signatures that would confirm or refute the ED-complexity hypothesis.

---

## 3. Quantum Mechanical Applications

The ED architecture makes its sharpest and most distinctive predictions in quantum mechanics, where the standard theory attributes decoherence to mass, environmental coupling, and system size, while ED attributes it to the gradient complexity of the density field. This section derives seven predictions, each traceable to specific canonical principles and Appendix C theorems, and each falsifiable by targeted experiment.

In the quantum context, the density field $\rho(x)$ is identified with the spatial probability density $|\psi(x)|^2$ of the quantum state, and the ED-complexity $C_{\mathrm{ED}} = \int|\nabla\rho|^2\,d^dx$ measures the total gradient content of this density. For a multi-particle system, $x \in \mathbb{R}^{3N}$ and $\Omega$ is the accessible configuration space.

---

### 3.1 ED Decoherence Rule

**Prediction.** The decoherence rate of a quantum system scales with its ED-complexity, not with its mass:

$$
\Gamma_{\mathrm{decoh}} \sim k\,C_{\mathrm{ED}}[\rho] = k\!\int |\nabla\rho(x)|^2\,d^d x,
$$

where $k > 0$ is a domain-dependent proportionality constant. Systems with high spatial symmetry (low $C_{\mathrm{ED}}$) maintain coherence; systems with low spatial symmetry (high $C_{\mathrm{ED}}$) decohere rapidly.

**Derivation from the architecture.** The decoherence rate corresponds, in the ED framework, to the rate at which the density field relaxes toward the equilibrium $\rho^*$. The dissipation identity (Lemma C.6) provides the bound

$$
-\frac{d\mathcal{E}}{dt} \geq D\int_\Omega \frac{P'(\rho)}{M(\rho)}\,|\nabla\rho|^2\,dx \geq D\,c_\delta\,C_{\mathrm{ED}},
$$

where $c_\delta = \inf P'(\rho)/M(\rho) > 0$ on the admissible interval (Theorem C.66(i)). The energy dissipation rate — and hence the rate at which the system loses its non-equilibrium structure — is bounded below by a quantity proportional to $C_{\mathrm{ED}}$. This is the content of the penalty dissipation channel (Principle 3) acting through the diffusive channel (Principle 1): spatial gradients are ironed out by the operator $M(\rho)\nabla^2\rho$, and the rate of ironing is proportional to $\|\nabla\rho\|_{L^2}^2$.

The structural principles involved are:

- **P1** (Operator Structure): provides the diffusion $M(\rho)\nabla^2\rho$ that smooths spatial gradients.
- **P3** (Penalty Equilibrium): provides $P' > 0$, ensuring the dissipation integrand is sign-definite.
- **P4** (Mobility Capacity Bound): ensures $M(\rho) > 0$ on the admissible interval, so the dissipation lower bound $c_\delta$ is positive.

**Contrast with standard QM.** Standard decoherence theory (Joos–Zeh, Zurek, Caldeira–Leggett) predicts that decoherence rate scales with mass, temperature, and the strength of environmental coupling. ED does not deny the role of environment; rather, it predicts that the *intrinsic* decoherence rate — the rate at which a system's own density-field structure drives relaxation, independent of external environment — scales with $C_{\mathrm{ED}}$. The two theories agree for typical systems (where mass and complexity are correlated) but diverge for systems where the correlation breaks: a heavy but highly symmetric system (low $C_{\mathrm{ED}}$) should cohere longer than a light but asymmetric one (high $C_{\mathrm{ED}}$), contrary to mass-based predictions.

**Experimental path.** Construct a structural-complexity ladder of molecules with controlled variation in $C_{\mathrm{ED}}$:

1. Compute $C_{\mathrm{ED}}$ from the ground-state electron density of each molecule (obtainable from DFT calculations or crystallographic data).
2. Perform matter-wave interferometry (Talbot–Lau or KDTLI) to measure coherence time.
3. Plot coherence time against $C_{\mathrm{ED}}$ and against mass separately.
4. Compare the quality of the two fits.

A suitable ladder: $C_{60}$ (buckyball, high symmetry, low $C_{\mathrm{ED}}$) $\to$ $C_{70}$ (slightly lower symmetry) $\to$ rigid asymmetric organic molecule $\to$ floppy biomolecule (peptide) $\to$ virus capsid.

**Falsification condition.** If coherence time correlates with mass but not with $C_{\mathrm{ED}}$ across the complexity ladder — specifically, if a high-mass, low-$C_{\mathrm{ED}}$ molecule (e.g., a symmetric metallofullerene) decoheres faster than a low-mass, high-$C_{\mathrm{ED}}$ molecule (e.g., an asymmetric peptide of lower mass) — then the ED decoherence rule is falsified.

---

### 3.2 Biological Coherence Limit

**Prediction.** There exists a critical ED-complexity $C_{\mathrm{crit}}$ above which quantum coherence is structurally impossible. All biological macromolecules exceed this threshold, and therefore biological structures cannot maintain quantum superposition.

Specifically:

- Microtubules decohere essentially instantaneously ($C_{\mathrm{ED}} \gg C_{\mathrm{crit}}$).
- Proteins decohere too rapidly for quantum-biological effects ($C_{\mathrm{ED}} \gg C_{\mathrm{crit}}$).
- Virus capsids are borderline but should fail to show interference ($C_{\mathrm{ED}} \gtrsim C_{\mathrm{crit}}$).

**Derivation from the architecture.** The nonlinear stability theorem (Theorem C.43) establishes a threshold $\epsilon_0$ in the $H^s$-norm below which exponential convergence to equilibrium is guaranteed. The three-stage convergence theorem (Theorem C.76) shows that above $\epsilon_0$, relaxation proceeds through an algebraic (Stage II) phase before entering the exponential regime.

In the quantum identification, the stability threshold translates to a critical ED-complexity:

$$
C_{\mathrm{crit}} \sim \epsilon_0^2 \cdot \mu_1^{-1},
$$

where $\mu_1$ is the first nonzero Neumann eigenvalue of the configuration domain. Below $C_{\mathrm{crit}}$, the quantum state's density profile is within the exponential-convergence basin (Regime II of §2.4): coherent evolution is stable against small perturbations. Above $C_{\mathrm{crit}}$, the system is in Regime III or IV: the density field dissipates rapidly through the diffusion-dominated channel, and the quantum superposition collapses on a time scale set by $D\alpha_1 = D(M_*\mu_1 + P_*')$.

Biological molecules have extremely high $C_{\mathrm{ED}}$ because their ground-state electron densities are highly structured: irregular atomic arrangements, numerous bond gradients, complex three-dimensional folding. This places them deep in Regime IV, where decoherence is effectively instantaneous.

The principles involved are **P1** (diffusive smoothing of gradients), **P3** (penalty driving toward $\rho^*$), and the stability threshold from **Theorem C.43**.

**Contrast with standard QM.** Standard quantum mechanics does not predict an intrinsic complexity-dependent coherence limit. Decoherence is attributed entirely to environmental coupling, and in principle, any system — however complex — could be made to cohere by sufficiently isolating it. ED disagrees: even in perfect isolation, biological structures would decohere because their intrinsic $C_{\mathrm{ED}}$ exceeds the architectural threshold.

**Experimental path.**

1. Perform interferometry on peptides, small proteins, and virus capsids.
2. Compute $C_{\mathrm{ED}}$ for each from structural data.
3. Identify the predicted threshold: the complexity value below which interference is observed and above which it is not.

**Falsification condition.** A positive interference result for a high-complexity biomolecule (e.g., a protein with $C_{\mathrm{ED}} > 10\,C_{\mathrm{crit}}$) would falsify this prediction. A single clean observation of matter-wave interference for a structurally complex biological molecule in a well-controlled environment would constitute strong evidence against the ED biological coherence limit.

---

### 3.3 Interference Visibility Scaling

**Prediction.** The interference visibility $\mathcal{V}$ of a matter-wave experiment decays as a power law in ED-complexity:

$$
\mathcal{V} \sim \frac{1}{1 + \alpha\,C_{\mathrm{ED}}},
$$

not exponentially in mass.

**Derivation from the architecture.** The visibility of an interference pattern is determined by the degree to which the density field maintains spatial coherence across the interferometric path. In the ED framework, the coherence of the density profile decays at a rate proportional to the dissipation rate $-d\mathcal{E}/dt$, which is bounded below by $D\,c_\delta\,C_{\mathrm{ED}}$ (Lemma C.6). For an interferometric measurement of duration $T$, the accumulated decoherence is

$$
\int_0^T \Gamma_{\mathrm{decoh}}(t)\,dt \sim k\,C_{\mathrm{ED}}\,T.
$$

The visibility is the exponential of the negative accumulated decoherence:

$$
\mathcal{V} = e^{-k\,C_{\mathrm{ED}}\,T}.
$$

For fixed flight time $T$ (as in Talbot–Lau interferometry), the visibility depends on $C_{\mathrm{ED}}$ alone. When the decoherence channel is not purely exponential — as occurs in the nonlinear regime (Regime III, where the three-stage convergence of Theorem C.76 applies) — the effective decay transitions from exponential to algebraic, yielding the power-law form $\mathcal{V} \sim (1 + \alpha C_{\mathrm{ED}})^{-1}$ as the leading-order rational approximation.

The key principles are **P1** (gradient-driven dissipation), **P3** (penalty restoring force determining the rate constant), and the three-stage structure of **Theorem C.76**.

**Contrast with standard QM.** Standard decoherence models (e.g., collisional decoherence, thermal photon scattering) predict that visibility decays exponentially with mass $m$ or with a decoherence function $\exp(-\Lambda m^2 / \hbar^2)$, where $\Lambda$ encodes environmental parameters. The mass-dependence is the conventional expectation. ED predicts a different functional form (power law in $C_{\mathrm{ED}}$) and a different governing variable ($C_{\mathrm{ED}}$ rather than $m$).

**Experimental path.**

1. Prepare a set of molecules spanning a range of $C_{\mathrm{ED}}$ values but with controlled mass variation.
2. Measure interference visibility for each molecule under identical interferometric conditions.
3. Fit the data to both models: (a) the ED power law $\mathcal{V} \sim (1 + \alpha C_{\mathrm{ED}})^{-1}$; (b) the standard exponential $\mathcal{V} \sim \exp(-\beta m^\gamma)$.
4. Compare goodness of fit.

**Falsification condition.** If the exponential-in-mass model provides a systematically better fit than the power-law-in-$C_{\mathrm{ED}}$ model across a broad range of molecules, the ED visibility scaling is falsified.

---

### 3.4 Hyper-Coherence in Ultra-Symmetric Systems

**Prediction.** Systems with extremely low ED-complexity — specifically, systems whose density fields are nearly spatially uniform — exhibit coherence times anomalously longer than standard decoherence theory predicts.

Candidates:

- Superconducting loops (macroscopic, high mass, but spatially uniform Cooper-pair condensate: low $C_{\mathrm{ED}}$).
- Bose–Einstein condensates (large particle number, but ground-state density is near-uniform in a harmonic trap: low $C_{\mathrm{ED}}$).
- Symmetric nanoparticles (high mass, but icosahedral or octahedral symmetry reduces $C_{\mathrm{ED}}$).
- Perfectly symmetric optical lattices (many sites, but translational symmetry keeps $C_{\mathrm{ED}}$ low).

**Derivation from the architecture.** At $C_{\mathrm{ED}} \approx 0$, the density field is in Regime I (§2.4): the dynamics are governed entirely by the homogeneous mode $(a_0, v)$, and all spatial dissipation channels are silent ($\mathcal{D}_{\mathrm{diff}} = 0$, eq. C.53). The only remaining dissipation is through the penalty channel ($\mathcal{D}_{\mathrm{pen}}$) and the participation channel ($\mathcal{D}_{\mathrm{part}}$), which act on the mean deviation $\bar{\rho} - \rho^*$ and the participation variable $v$. If the system is prepared near $\rho^*$ with $v \approx 0$, the dissipation rate is $\sim \max(D P_*'^2/M_*,\, H\zeta) \cdot |\bar{\rho} - \rho^*|^2$, which can be extremely small for near-equilibrium states.

The key insight is the spectral gap structure (Lemma C.31): the homogeneous decay rate $\gamma_{\mathrm{hom}} = \frac{1}{2}(DP_*' + \zeta/\tau)$ can be much smaller than the spatial decay rate $\gamma_{\mathrm{sp}} = D\alpha_1 = D(M_*\mu_1 + P_*')$. In the regime $M_*\mu_1 \gg P_*'$ (diffusion-dominated), the spatial modes decay orders of magnitude faster than the homogeneous mode. An ultra-symmetric system, having negligible amplitude in spatial modes, bypasses the fast diffusive channel entirely and relaxes only through the slow homogeneous channel.

Standard decoherence theory does not distinguish between the homogeneous and spatial decay channels. It predicts a decoherence rate that depends on the total system mass and environmental coupling, not on the modal decomposition of the density field. ED predicts that the effective decoherence rate for ultra-symmetric systems is $\gamma_{\mathrm{hom}}$, which can be parametrically smaller than the rate $\gamma_{\mathrm{sp}}$ that would apply to an asymmetric system of the same mass.

The principles involved are **P1** (the modal hierarchy that separates spatial and homogeneous time scales), **P5** (participation damping as the slow channel), and **P6** (discriminant structure determining whether the slow approach is oscillatory or monotonic).

**Experimental path.**

1. Measure coherence times in ultra-symmetric engineered systems: superconducting qubits in symmetric geometries, BECs in isotropic traps, symmetric nanoparticle interferometry.
2. Compare to standard decoherence models calibrated on asymmetric systems of similar mass.
3. Look for positive anomalies: coherence times that exceed the mass-based prediction.

**Falsification condition.** If ultra-symmetric systems show coherence times consistent with mass-based scaling (no anomaly), or if an asymmetric system of the same mass and environmental coupling shows the same coherence time as the symmetric one, then the hyper-coherence prediction is falsified.

---

### 3.5 Quantum-Classical Threshold

**Prediction.** There exists a critical ED-complexity $C_{\mathrm{crit}}$ that defines a sharp threshold between quantum and classical behavior:

- Below $C_{\mathrm{crit}}$: stable quantum behavior (exponential convergence in Regime II).
- Above $C_{\mathrm{crit}}$: immediate classicality (rapid dissipation in Regime IV).

The transition is sharp, not a smooth crossover.

**Derivation from the architecture.** The nonlinear stability theorem (Theorem C.43) identifies a threshold $\epsilon_0$ in the $H^s$-norm that separates exponential convergence (inside the basin) from the three-stage process (outside). The transition at $\epsilon_0$ is not a smooth parameter variation; it is a qualitative change in the convergence mechanism — from single-stage exponential to three-stage global-algebraic-exponential (Theorem C.76).

Translated to the quantum setting: systems with $C_{\mathrm{ED}} < C_{\mathrm{crit}}$ have density profiles within the exponential-convergence basin. Small perturbations (measurements, environmental fluctuations) are absorbed and corrected exponentially fast — this is quantum stability. Systems with $C_{\mathrm{ED}} > C_{\mathrm{crit}}$ are outside the basin. Any perturbation triggers a cascade through the diffusion-dominated Regime IV, rapidly destroying spatial coherence — this is classicality.

The sharpness of the threshold is a consequence of the Lyapunov structure (Theorem C.43): the exponential estimate (C.50) holds if and only if $\|u\|_{H^s} + |w| < \gamma_*/C_{\mathrm{nl}}$. There is no intermediate regime where the estimate "partially" holds. The system is either inside the basin (quantum) or outside it (classical).

The principles involved are **P1** (providing the spatial dissipation that drives classical relaxation), **P3** (providing the restoring force that defines the basin), and the full nonlinear stability structure of **Appendix C.5**.

**Contrast with standard QM.** Standard quantum mechanics treats the quantum-classical transition as a smooth crossover governed by the ratio $\hbar / S$, where $S$ is the classical action. There is no sharp threshold; decoherence increases continuously with system size. ED predicts a structurally sharp transition at a specific $C_{\mathrm{ED}}$ value, which is determined by the architectural parameters, not by $\hbar$.

**Experimental path.**

1. Incrementally increase the structural complexity of molecules in an interferometric setup.
2. Track the coherence time as a function of $C_{\mathrm{ED}}$.
3. Identify the predicted sharp transition: a rapid drop in coherence over a narrow range of $C_{\mathrm{ED}}$, rather than a smooth exponential decline.

**Falsification condition.** If the coherence time decreases smoothly and monotonically with complexity (or mass), with no identifiable threshold, then the sharp quantum-classical transition predicted by ED is falsified.

---

### 3.6 Bell Correlation Degradation with Complexity

**Prediction.** Bell-type correlations (CHSH inequality violations) degrade with the ED-complexity of the entangled subsystems, even when environmental coupling is held constant.

Specifically: if two subsystems $A$ and $B$ are prepared in a maximally entangled state, and the internal structure of each subsystem is varied (changing $C_{\mathrm{ED}}$ without changing the environmental coupling), the measured CHSH parameter $S$ should decrease as $C_{\mathrm{ED}}$ increases:

$$
S(C_{\mathrm{ED}}) < S(0) = 2\sqrt{2},
$$

with the degradation rate governed by the dissipation identity.

**Derivation from the architecture.** Entanglement, in the ED framework, corresponds to correlated spatial structure in the joint density field $\rho(x_A, x_B)$. The ED-complexity of the entangled state includes cross-gradient terms $|\nabla_{x_A}\rho|^2 + |\nabla_{x_B}\rho|^2$ that contribute to $C_{\mathrm{ED}}$. The dissipation identity (Lemma C.6) drives these gradients toward zero, smoothing the joint density toward the product state $\rho(x_A)\rho(x_B)$ — the separable (unentangled) equilibrium.

The rate of entanglement degradation is bounded below by $D\,c_\delta$ times the contribution to $C_{\mathrm{ED}}$ from the cross-correlations. If the internal structure of each subsystem contributes additional gradient content (high internal $C_{\mathrm{ED}}$), the total dissipation rate increases, and the entanglement degrades faster — even though the *environmental* coupling has not changed.

The principles involved are **P1** (gradient-driven dissipation of spatial correlations), **P3** (penalty force driving toward the separable equilibrium), and **P2** (channel complementarity partitioning the dissipation into direct and mediated components).

**Contrast with standard QM.** Standard quantum mechanics predicts that Bell-correlation degradation depends on environmental decoherence and measurement imperfections, not on the internal structure of the entangled subsystems. Two photons entangled in polarization should violate the CHSH inequality identically regardless of whether they pass through a simple medium or a complex one, provided the *coupling* to the medium is the same. ED predicts that the medium's structural complexity (its $C_{\mathrm{ED}}$) independently degrades the correlations.

**Experimental path.**

1. Prepare entangled photon pairs or entangled ions.
2. Transmit through or couple to media of varying internal complexity (e.g., structured vs. unstructured optical fibers, simple vs. complex ionic traps).
3. Hold environmental coupling constant (same temperature, same loss rate).
4. Measure CHSH parameter $S$ as a function of the medium's $C_{\mathrm{ED}}$.

**Falsification condition.** If the CHSH parameter is constant across media of different $C_{\mathrm{ED}}$ at fixed environmental coupling, the complexity-dependent Bell-degradation prediction is falsified.

---

### 3.7 Quantum Error Correction Limit

**Prediction.** There exists a fundamental limit to scalable quantum error correction based on the ED-complexity of the encoded state. Above a critical complexity, error-correction codes cannot maintain coherent participation, and the logical error rate exceeds the correction rate regardless of code distance.

Specifically: the logical qubit's effective $C_{\mathrm{ED}}$ increases with the number of physical qubits in the code block (because the encoding introduces additional spatial/configurational structure). When the total $C_{\mathrm{ED}}$ of the encoded state crosses $C_{\mathrm{crit}}$, the system enters Regime III or IV, and the error rate overwhelms the correction capacity.

**Derivation from the architecture.** Quantum error correction operates by distributing logical information across many physical qubits, creating a highly entangled, spatially structured state. In the ED framework, this encoding increases the gradient content of the density field: each additional physical qubit contributes to $|\nabla\rho|^2$ through the cross-correlations in the joint configuration space.

The dissipation rate of the encoded state is (Lemma C.6):

$$
-\frac{d\mathcal{E}}{dt} \geq D\,c_\delta\,C_{\mathrm{ED}}[\rho_{\mathrm{encoded}}],
$$

which grows with the code size. The error-correction procedure must apply corrective operations faster than this dissipation rate to maintain coherence. But the correction rate is limited by the code structure (syndrome measurement, classical processing, gate times), which does not scale with $C_{\mathrm{ED}}$. There is therefore a maximum code size — equivalently, a maximum $C_{\mathrm{ED}}$ — beyond which correction cannot keep pace with dissipation.

The architectural principles involved are **P1** (gradient dissipation increasing with code complexity), **P3** (penalty force driving the encoded state toward the unencoded equilibrium), and **P4** (mobility collapse providing a hard ceiling on the achievable density structure — the encoded state cannot exceed the capacity bound $\rho_{\max}$, limiting the information density).

**Contrast with standard QM.** The threshold theorem of standard quantum error correction states that arbitrarily reliable quantum computation is possible provided the physical error rate is below a constant threshold, with no fundamental limit on code size. ED predicts that this theorem breaks down at high $C_{\mathrm{ED}}$: the *intrinsic* error rate (from ED dissipation) grows with code size, eventually exceeding any fixed threshold.

**Experimental path.**

1. Perform multi-qubit scaling tests on current quantum hardware (superconducting, trapped-ion, or topological).
2. Track the logical error rate as a function of code distance (equivalently, the number of physical qubits).
3. Compute $C_{\mathrm{ED}}$ for the encoded state at each code distance.
4. Identify the predicted breakdown point: the code distance at which the logical error rate begins to *increase* rather than decrease.

**Falsification condition.** If quantum error correction scales to arbitrarily large code distances with monotonically decreasing logical error rates — with no complexity-dependent floor — the ED error-correction limit is falsified. This is a long-term test, requiring hardware capabilities beyond current levels, but it is a clean and decisive target.

---

## 4. Galactic and Cosmological Applications

The ED architecture replaces dark-matter halos with *temporal halos*: diffuse structures generated by the activity-dependent gradients of the event-density field. In the galactic context, the density field $\rho(x,t)$ is the event-density distribution across the spatial extent of a galaxy or cluster, and $C_{\mathrm{ED}} = \int|\nabla\rho|^2\,d^3x$ measures the total gradient content generated by baryonic activity — rotation, star formation, turbulence, feedback, and mergers. The participation variable $v(t)$ encodes the integrated temporal memory of this activity.

This section derives ten predictions, one of which has already been tested and confirmed. Each prediction distinguishes ED from the cold dark matter (CDM) paradigm by identifying observable signatures that depend on *activity* rather than *mass alone*.

---

### 4.1 Temporal Halos

**Prediction.** The apparent "dark matter" halo surrounding a galaxy is not a distribution of massive particles but a *temporal halo*: a spatial structure in the event-density field generated by the galaxy's internal dynamical activity and sustained by the participation feedback loop.

The temporal halo has the following properties:

- It is generated by baryonic activity (gradients in $\rho$), not by a separate matter species.
- It is sustained by the participation variable $v$, which integrates past activity (Principle 5).
- It diffuses outward via $M(\rho)\nabla^2\rho$ (Principle 1), producing smooth, extended profiles.
- It relaxes toward $\rho^*$ on a time scale set by $\tau$ and $\zeta$ (Principle 5), not instantaneously.

**Derivation from the architecture.** In the canonical ED system (D.1), the density equation $\partial_t\rho = D\,F[\rho] + Hv$ shows that the density field is driven by two sources: the direct operator $F[\rho]$, which smooths and restores; and the participation feedback $Hv$, which injects the integrated operator history. A galaxy with sustained internal activity (rotation, star formation) continuously generates gradients in $\rho$ through the operator's diffusion and penalty terms. These gradients diffuse outward and accumulate, producing an extended density structure — the temporal halo — that persists as long as the participation variable $v$ retains memory of the activity.

The key principles are:

- **P1**: Provides the spatial diffusion $M(\rho)\nabla^2\rho$ that spreads the halo.
- **P3**: Provides the penalty restoring force that determines the halo's asymptotic profile (convergence to $\rho^*$ at large radii, Theorem C.76).
- **P5**: Provides the participation memory that sustains the halo after activity subsides.

**Contrast with CDM.** CDM halos are gravitationally bound structures composed of weakly interacting massive particles. They are determined by the galaxy's total mass and merger history, not by its current dynamical state. ED temporal halos are determined by the galaxy's activity history — specifically, by the time integral of the gradient generation rate. Two galaxies with identical mass but different activity levels should have different halo strengths under ED but identical halos under CDM.

**Observational path.** Compare halo properties (rotation-curve amplitude, lensing signal) across galaxies matched in baryonic mass but differing in dynamical activity (star-formation rate, rotation speed, turbulence). If halo strength correlates with activity at fixed mass, the temporal-halo model is supported.

**Falsification condition.** If halo strength depends only on total mass and is insensitive to dynamical state — specifically, if galaxies with identical mass but very different star-formation rates have identical rotation curves — then the temporal-halo prediction is falsified.

---

### 4.2 Dwarf Galaxy Rotation Curves (Completed Test — Passed)

**Prediction.** Dynamically active dwarf galaxies exhibit larger outer-radius mass discrepancies than quiet dwarfs, even at fixed baryonic mass.

The causal chain is: increased internal activity $\to$ increased temporal tension (higher $C_{\mathrm{ED}}$) $\to$ stronger temporal halo $\to$ increased apparent curvature $\to$ larger mass discrepancy.

**Derivation from the architecture.** Active dwarf galaxies have higher $C_{\mathrm{ED}}$ because their internal dynamics (star formation, gas turbulence, rotational shear) generate steeper density gradients. By the dissipation identity (Lemma C.6), the energy stored in these gradients is $\sim C_{\mathrm{ED}}$, and the participation variable $v$ integrates this energy through the feedback loop (Principle 5). The accumulated participation produces a stronger mediated-channel contribution $Hv$ to the density equation, which manifests as additional effective mass at large radii.

The mass discrepancy $D(r) = V_{\mathrm{obs}}^2(r)/V_{\mathrm{bar}}^2(r)$ at the outermost radius measures the ratio of the total dynamical mass (inferred from the rotation curve) to the baryonic mass. In ED, the numerator includes the temporal-halo contribution; in CDM, it includes the dark-matter halo contribution. The ED prediction is that $D_{\mathrm{outer}}$ correlates with activity level, not just with baryonic mass.

**Test outcome.** This prediction was tested using the SPARC dataset (Lelli et al. 2016), filtering to 46 dwarf galaxies and classifying each as Active or Quiet based on dynamical indicators:

- Quiet dwarfs: $\langle D_{\mathrm{outer}}\rangle \approx 3.94$.
- Active dwarfs: $\langle D_{\mathrm{outer}}\rangle \approx 6.01$.
- Ratio: $D_{\mathrm{Active}}/D_{\mathrm{Quiet}} \approx 1.53$.

The active dwarfs exhibit a 53% higher outer-radius mass discrepancy. The separation is visually clean and statistically reproducible (Open Note, §8).

**Contrast with CDM.** CDM predicts that the mass discrepancy is determined by the dark-matter halo mass, which is set by the galaxy's assembly history (concentration, virial mass) and should not correlate with current star-formation rate or dynamical state at fixed baryonic mass. The observed activity dependence is not a standard CDM prediction.

**Falsification condition.** This prediction has been confirmed. It would be falsified by a larger dataset showing that the Active/Quiet separation disappears when controlling for halo concentration or assembly history — that is, if the activity correlation is entirely explained by CDM halo parameters.

---

### 4.3 Halo Lag in Collisions

**Prediction.** In high-speed cluster collisions (Bullet Cluster analogues), the temporal halo lags behind the baryonic mass, producing:

- Offset between the lensing peak and the X-ray gas peak.
- Shear and stretching of the halo along the collision axis.
- Smeared or displaced lensing contours.
- Extended low-density lensing regions (temporal wakes) trailing the collision.

**Derivation from the architecture.** Temporal tension is tied to the activity of the baryonic matter and diffuses with finite speed (set by $M(\rho)$ and $\tau$). During a violent collision, the baryonic components (gas, stars) are displaced rapidly, but the temporal halo — sustained by the participation variable $v$, which evolves on the time scale $\tau$ — cannot follow instantaneously. The participation equation $\dot{v} = \tau^{-1}(F[\rho] - \zeta v)$ shows that $v$ responds to changes in $F[\rho]$ with a lag of order $\tau$. During this lag, the halo remains at its pre-collision position, producing the predicted offset.

The shearing arises because different parts of the halo experience different collision-induced perturbations, and the diffusive character of the density equation ($M(\rho)\nabla^2\rho$, Principle 1) smooths these perturbations on a finite spatial scale. The temporal wake is the residual halo structure left behind as the baryonic mass moves ahead.

The principles involved are **P1** (finite-speed diffusion), **P5** (participation lag with time constant $\tau$), and **P3** (penalty restoring force that eventually dissipates the wake).

**Contrast with CDM.** CDM predicts collisionless passage: the dark-matter halos of two colliding clusters pass through each other without significant interaction, producing lensing peaks aligned with the dark matter and offset from the gas (which is collisional). The CDM prediction is sharp lensing peaks with minimal distortion. ED predicts distorted, lagging, sheared halo contours — a qualitatively different morphology.

**Observational path.** Compare lensing maps to X-ray gas distributions in cluster collisions (Bullet Cluster, El Gordo, Musket Ball Cluster). Look for:

1. Elongated, asymmetric, or dragged halo contours.
2. Extended low-density lensing regions trailing the collision axis (temporal wakes).
3. Lensing-peak offsets that correlate with collision velocity and time since pericenter.

**Falsification condition.** A clean, collisionless passage — with sharp, undistorted lensing peaks perfectly aligned with the inferred particle dark-matter distribution and no trailing wake — falsifies the halo-lag prediction.

---

### 4.4 Activity-Dependent Halos

**Prediction.** Galaxies with identical baryonic mass but different dynamical states exhibit different halo strengths. The halo strength correlates with:

- Rotation speed.
- Star-formation rate.
- Turbulence level.
- Feedback intensity.
- Bar dynamics.
- Merger history.

**Derivation from the architecture.** Each of these activity indicators contributes to $C_{\mathrm{ED}}$: rotation generates velocity gradients in $\rho$; star formation creates localized density enhancements and depletions; turbulence injects broadband gradient content across multiple spatial scales; feedback (supernovae, AGN jets) drives large-amplitude density perturbations; bars create non-axisymmetric gradients; mergers produce the most extreme gradient configurations. By the dissipation identity and the participation feedback, the temporal halo amplitude is monotone in the time-averaged $C_{\mathrm{ED}}$ (§2.4, Regime III–IV dynamics).

**Contrast with CDM.** CDM halos depend on mass and assembly history. At fixed baryonic mass, CDM allows halo variation through scatter in the mass–concentration relation, but does not predict a systematic correlation with *current* dynamical activity. An activity-dependent correlation supports ED.

**Observational path.** Compare rotation curves of galaxies matched in baryonic mass but differing in star-formation rate, rotation speed, or turbulence. Examine whether halo strength (measured by $D_{\mathrm{outer}}$ or the total lensing signal) correlates with current or recent activity.

**Falsification condition.** A mass-only correlation — with no residual dependence on activity indicators at fixed mass — supports CDM and falsifies this ED prediction.

---

### 4.5 Reduced Substructure

**Prediction.** Temporal halos have less small-scale substructure than CDM halos. Specifically, ED predicts:

- Suppressed subhalo populations (fewer dwarf satellites than CDM expects).
- Smoother halo profiles (fewer clumps and flux anomalies).
- Smoother rotation curves in low-mass systems.

**Derivation from the architecture.** Temporal tension is diffusive: the operator $M(\rho)\nabla^2\rho$ (Principle 1) smooths spatial structure on all scales. The modal hierarchy (Proposition C.29) ensures that high-frequency spatial modes decay faster than low-frequency ones, with decay rates growing as $D\,M_*\,\mu_n \sim n^{2/d}$ (Weyl asymptotics). Small-scale clumps (high-$n$ modes) are therefore suppressed exponentially faster than the large-scale halo envelope (low-$n$ modes). The penalty restoring force (Principle 3) drives all structure toward the smooth equilibrium $\rho^*$. The result is a temporal halo that is structurally smoother than a CDM halo at every radius.

**Contrast with CDM.** CDM predicts abundant subhalos and clumpy substructure at all scales, arising from hierarchical structure formation. The "missing satellites" and "too-big-to-fail" problems are well-known tensions between CDM predictions and observations. ED resolves these tensions structurally: the diffusive nature of temporal tension suppresses substructure by construction.

**Observational path.**

1. Count dwarf satellite galaxies around Milky-Way analogues and compare to CDM substructure predictions.
2. Analyze strong-lensing flux anomalies for evidence of subhalo populations.
3. Compare high-resolution rotation curves in low-mass galaxies to CDM and ED halo models.

**Falsification condition.** A highly clumpy halo — with abundant substructure matching CDM N-body predictions — supports CDM and falsifies the ED reduced-substructure prediction.

---

### 4.6 Hysteresis

**Prediction.** The temporal halo retains memory of past activity. A galaxy that recently experienced a starburst, merger, AGN feedback episode, or bar-driven inflow should retain an enhanced halo even after the activity subsides. The halo relaxes on the participation time scale $\tau$, producing a measurable lag between the cessation of activity and the weakening of the halo.

**Derivation from the architecture.** The participation variable $v$ evolves as $\dot{v} = \tau^{-1}(F[\rho] - \zeta v)$ (Principle 5). When the driving term $F[\rho]$ is large (during active periods), $v$ accumulates. When the driving subsides ($F[\rho] \to 0$), $v$ decays as $v(t) \sim v_0\,e^{-\zeta t/\tau}$, with relaxation time $\tau/\zeta$. During this decay, the mediated-channel term $Hv$ continues to contribute to the density equation, sustaining the halo beyond the period of active driving. This is the Memory Loop motif of the ED architecture (ED-Arch-02).

The three-stage convergence theorem (Theorem C.76) ensures that the halo eventually dissipates (Stage III: exponential convergence), but the algebraic Stage II may persist for an extended period if the initial participation amplitude is large.

**Contrast with CDM.** CDM halos do not have temporal memory. The dark-matter distribution responds to the gravitational potential, which adjusts on a dynamical time scale. There is no mechanism for a CDM halo to "remember" a past starburst or retain an enhanced profile after the activity ceases. CDM predicts instantaneous response; ED predicts memory.

**Observational path.**

1. Identify post-starburst galaxies and measure their halo strengths (via rotation curves or weak lensing).
2. Compare to galaxies with similar current activity but different recent histories.
3. Look for temporal overshoot: halos stronger than the current activity level predicts.

**Falsification condition.** If halos respond instantaneously to changes in activity — with no memory effect and no temporal overshoot — then the hysteresis prediction is falsified.

---

### 4.7 Vortex-Like Distortions

**Prediction.** Rotation and shear in a galaxy stir the temporal field, producing vortex-like distortions in the halo:

- Swirl-like features in the isopotential contours.
- Twisted halo shapes aligned with the galaxy's rotation axis.
- Asymmetries between the approaching and receding sides of rotation curves.

**Derivation from the architecture.** The operator $F[\rho]$ includes the gradient-squared nonlinearity $M'(\rho)|\nabla\rho|^2$ (Principle 7), which couples the density gradients generated by rotation to the halo structure. In a rotating galaxy, the gradients are not isotropic: they have a preferred helical geometry imposed by the rotation. The nonlinear term transfers this helical structure into the halo through the triad coupling (Appendix C, §C.4.5), producing non-axisymmetric features that inherit the galaxy's rotational geometry.

The participation feedback (Principle 5) sustains these features by integrating the rotationally driven $F[\rho]$ over time, producing a time-averaged helical pattern in $v$ that feeds back into the density.

**Contrast with CDM.** CDM halos are approximately triaxial, with shapes determined by the assembly history (mergers, accretion), not by the current rotation of the baryonic disk. CDM does not predict systematic correlations between halo shape and disk rotation, nor spiral or swirl-like halo features. A spherical or triaxial halo supports CDM; a swirl-patterned halo supports ED.

**Observational path.**

1. Map lensing shear around fast-rotating galaxies.
2. Compare rotation curves on opposite sides of the disk (approaching vs. receding).
3. Look for spiral-shaped or vortex-like features in the weak-lensing reconstruction.

**Falsification condition.** If halos are systematically spherical or triaxial with no correlation to disk rotation, the vortex-distortion prediction is falsified.

---

### 4.8 Asymmetry Reflecting Baryonic Structure

**Prediction.** The temporal halo inherits the morphological asymmetries of the baryonic distribution. Specifically, the halo should reflect:

- Bars (elongated along the bar axis).
- Warps (bent in the same direction as the disk warp).
- Lopsided star formation (asymmetric halo enhancement on the active side).
- Asymmetric gas inflows (distorted halo contours tracing the inflow geometry).

**Derivation from the architecture.** The temporal halo is generated by the baryonic density gradients via $F[\rho] = M(\rho)\nabla^2\rho + M'(\rho)|\nabla\rho|^2 - P(\rho)$. Since $F[\rho]$ depends directly on $\rho$ and its derivatives, any spatial asymmetry in the baryonic distribution produces a corresponding asymmetry in $F[\rho]$, which propagates through the diffusion operator and the participation feedback into the halo. The halo is a smoothed, diffused image of the baryonic structure — not an independent component.

**Contrast with CDM.** CDM halos are gravitationally self-consistent structures whose shapes are determined by the dark-matter distribution, which is only weakly coupled to the baryonic disk. CDM predicts that halos should remain approximately spherical and insensitive to baryonic asymmetries (bars, warps, lopsidedness). A halo that mirrors baryonic structure supports ED; a halo that ignores it supports CDM.

**Observational path.**

1. Compare halo shape (from lensing or rotation-curve decomposition) to bar orientation.
2. Examine warped disks for corresponding halo distortions.
3. Test whether asymmetric star-forming regions correlate with halo asymmetry.

**Falsification condition.** If halos are systematically symmetric and uncorrelated with baryonic morphological features, this prediction is falsified.

---

### 4.9 Rotation-Dependence

**Prediction.** Fast-rotating galaxies host stronger temporal halos than slow-rotating galaxies of the same baryonic mass. Rotation injects activity into the density field, deepening the effective potential.

**Derivation from the architecture.** Rotation generates persistent velocity gradients in the density field, contributing a steady-state term to $C_{\mathrm{ED}}$. The rotational contribution to $C_{\mathrm{ED}}$ scales as $v_{\mathrm{rot}}^2/r^2$ integrated over the disk, which increases with rotation speed at fixed mass. By the dissipation identity (Lemma C.6) and the participation feedback (Principle 5), the time-averaged halo strength is monotone in the time-averaged $C_{\mathrm{ED}}$. Therefore, halo strength should correlate with angular momentum, not just with mass.

This prediction is particularly testable in ultra-diffuse galaxies (UDGs), which have large spatial extents and correspondingly low surface densities. UDGs with high spin parameters should have stronger halos than compact galaxies of the same mass.

**Contrast with CDM.** CDM halos are determined by the virial mass and concentration parameter, which depend on assembly history, not on the current rotation speed. CDM predicts a mass-only correlation. A rotation-dependent correlation, at fixed mass, supports ED.

**Observational path.**

1. Compare halo strength (from rotation curves or lensing) versus rotation speed for galaxies matched in baryonic mass.
2. Examine UDGs with high spin parameters.
3. Test whether halo strength correlates with angular momentum rather than mass.

**Falsification condition.** A mass-only correlation — with no residual rotation dependence — supports CDM and falsifies this prediction.

---

### 4.10 Temporal Lensing Deviations

**Prediction.** Temporal halos produce gravitational lensing profiles that are systematically:

- Smoother than CDM (NFW) predictions.
- More extended (shallower decline at large radii).
- Less cuspy (shallower central density slope).
- Less centrally concentrated.

**Derivation from the architecture.** The diffusive character of the ED operator ($M(\rho)\nabla^2\rho$, Principle 1) smooths the temporal halo on all spatial scales. The modal hierarchy (Proposition C.29) ensures that high-frequency components are damped first, producing a smooth, extended profile. The penalty equilibrium (Principle 3) drives the central density toward $\rho^*$, preventing the formation of a steep cusp. The mobility collapse (Principle 4) creates an energy barrier that prevents density concentration beyond $\rho_{\max}$, capping the central density.

The resulting lensing profile is a smoothed version of the baryonic profile, extended by the diffusion scale $\ell_{\mathrm{diff}} \sim \sqrt{M_*\,\tau}$ and flattened at the center by the penalty force. This contrasts with the NFW profile, which has a characteristic $r^{-1}$ cusp at small radii and a sharp cutoff at the virial radius.

The principles involved are **P1** (diffusion smoothing the profile), **P3** (penalty preventing central cusps), **P4** (mobility collapse capping central density), and the spectral analysis of **Appendix C.4** (modal hierarchy ensuring smooth profiles).

**Contrast with CDM.** The NFW profile, the standard CDM prediction, has a central cusp ($\rho \propto r^{-1}$) and abundant substructure. The "core-cusp problem" — observed cores where NFW predicts cusps, particularly in dwarf galaxies — is a well-known tension. ED resolves this tension: temporal halos are cored by construction, because the penalty force and diffusive smoothing prevent cusp formation.

**Observational path.**

1. Fit lensing shear profiles with CDM (NFW) and ED-inspired models (smooth, extended, cored).
2. Look for extended low-curvature wings in the lensing signal beyond the NFW prediction.
3. Compare central density slopes to the NFW cusp prediction.

**Falsification condition.** A cuspy, NFW-like profile — confirmed across a large sample with no core-cusp tension — supports CDM and falsifies the ED lensing-deviation prediction. Conversely, a smooth, extended, cored profile that cannot be accommodated by CDM baryonic feedback models supports ED.

---

## 5. Condensed Matter and Photonic Applications

The ED architecture predicts that systems governed by density-gradient dynamics — mesoscopic conductors, superconducting films, Casimir cavities, nonlinear microresonators, and photonic crystals — exhibit structural thresholds, saturation plateaus, and asymmetries that standard models attribute to smooth crossovers or do not predict at all. In each case, the ED prediction is that a measurable quantity transitions sharply at a critical ED-complexity, rather than varying smoothly with the conventionally assumed control parameter.

In this section, the density field $\rho(x)$ is identified with the relevant order parameter or field intensity of the physical system: the electron density in a mesoscopic conductor, the superfluid phase stiffness in a superconductor, the vacuum-fluctuation field between Casimir plates, or the optical mode profile in a resonator. The ED-complexity $C_{\mathrm{ED}} = \int|\nabla\rho|^2\,d^dx$ measures the gradient content of this field within the device geometry.

---

### 5.1 Mesoscopic Transport Threshold

**Prediction.** The conductance $G(L)$ of a mesoscopic channel exhibits a non-analytic kink at a critical length $L_{\mathrm{crit}}$ where the event-density gradient saturates:

- Below $L_{\mathrm{crit}}$: ballistic-like scaling.
- Above $L_{\mathrm{crit}}$: diffusive-like scaling.
- At $L_{\mathrm{crit}}$: a sharp, reproducible kink in $G(L)$.

The critical length $L_{\mathrm{crit}}$ depends on the ED-complexity of the channel geometry (cross-section, surface roughness, lattice structure), not on the impurity concentration.

**Architectural origin.** The kink arises from the nonlinear stability threshold of Theorem C.43. As the channel length increases, the density gradient across the channel grows, and $C_{\mathrm{ED}}$ increases. Below $L_{\mathrm{crit}}$, the system is in Regime II (§2.4): the perturbation is within the exponential-convergence basin, and transport is governed by the fast, coherent (ballistic) dynamics. Above $L_{\mathrm{crit}}$, the system crosses into Regime III: the density gradient exceeds the stability threshold $\epsilon_0$, the three-stage convergence (Theorem C.76) activates, and transport transitions to the slow, dissipation-dominated (diffusive) regime.

The sharpness of the kink is a consequence of the Lyapunov structure: the exponential estimate (eq. C.50) holds if and only if $C_{\mathrm{ED}} < C_{\mathrm{crit}}$. There is no intermediate regime. The relevant principles are **P1** (diffusion providing the spatial dynamics), **P3** (penalty equilibrium defining the stability basin), and the full stability theory of **Appendix C.5**.

Standard transport theory (Landauer–Buttiker, Boltzmann) predicts a smooth crossover from ballistic to diffusive transport governed by the ratio $L/\ell_{\mathrm{mfp}}$, where $\ell_{\mathrm{mfp}}$ is the mean free path. The crossover is analytic and has no kink. ED predicts a structural transition at a length determined by geometry, not by scattering.

**Experimental path.** Fabricate quasi-1D channels with tunable length (graphene nanoribbons, carbon nanotubes, GaAs/AlGaAs heterostructures, metallic nanowires). For each device: measure $G(L)$ across a sweep of channel lengths, compute $C_{\mathrm{ED}}$ from the structural geometry, and identify the predicted kink at $L_{\mathrm{crit}}$.

**Falsification condition.** A smooth crossover with no structural transition — specifically, a $G(L)$ curve that is everywhere analytic and well-fit by standard scattering models — falsifies this prediction.

---

### 5.2 Superconducting Phase-Stiffness Saturation

**Prediction.** The superfluid phase stiffness $J(T)$ of a thin-film superconductor exhibits a characteristic flattening before the superconducting transition:

- At low temperature: standard stiffness behavior.
- Approaching $T_c$: premature saturation of $J(T)$ (a plateau).
- Near $T_c$: rapid collapse once the ED-locking regime fails.

The saturation temperature $T_{\mathrm{sat}}$ depends on the ED-complexity of the film (geometry, disorder symmetry, thickness), not on the microscopic pairing strength.

**Architectural origin.** In the ED framework, superconductivity corresponds to a high-density event-locking regime: the density field is maintained near a local maximum of participation by the feedback loop (Principle 5), with the phase stiffness measuring the resistance of this locked state to spatial perturbations. As temperature increases, the density gradients grow (thermal fluctuations inject gradient content), and $C_{\mathrm{ED}}$ rises. The mobility collapse (Principle 4) creates a structural ceiling: the energy barrier $\Phi(\rho) \to +\infty$ at $\rho_{\max}$ (Proposition C.11) caps the achievable gradient content. When $C_{\mathrm{ED}}$ approaches this ceiling, the stiffness saturates — further temperature increase cannot steepen the gradients beyond the mobility-collapse limit.

The plateau is the physical manifestation of the energy barrier at $\rho_{\max}$ (Appendix C, §C.2.5). The collapse at $T_c$ occurs when the penalty restoring force (Principle 3) can no longer maintain the locked state against thermal perturbations — the system exits the stability basin (Theorem C.43).

Standard BCS, Kosterlitz–Thouless, and phase-fluctuation models predict a smooth, monotonic softening of $J(T)$ without a plateau. The ED plateau is a structural prediction with no counterpart in conventional theory.

**Experimental path.** Use thin-film superconductors with tunable geometry (NbN, MoGe, YBCO, amorphous InOx). Measure $J(T)$ via THz spectroscopy or two-coil mutual inductance. Compute $C_{\mathrm{ED}}$ from the film's structural symmetry and thickness. Identify the predicted saturation plateau and compare to BCS/KT predictions.

**Falsification condition.** A smooth, monotonic softening of $J(T)$ with no plateau — across multiple film geometries — falsifies this prediction.

---

### 5.3 Casimir-Gradient Saturation

**Prediction.** The Casimir force between two closely spaced surfaces exhibits three regimes:

- At large separations: standard Casimir–Lifshitz behavior ($F \propto d^{-4}$).
- At intermediate separations: steepening as the ED gradient builds.
- At sub-100 nm separations: a force-saturation plateau where the ED gradient cannot increase further.

The saturation distance $d_{\mathrm{sat}}$ depends on the ED-complexity of the cavity (surface roughness, ionic strength, dielectric structure), not on the vacuum-mode density.

**Architectural origin.** In the ED framework, near-field forces arise from event-density gradients between surfaces, not from vacuum-mode summation. As two surfaces approach, the density field between them steepens, and $C_{\mathrm{ED}}$ increases. The mobility collapse (Principle 4) imposes a maximum sustainable gradient: $M(\rho_{\max}) = 0$ ensures that the density cannot exceed the capacity bound, and the energy barrier $\Phi(\rho) \to +\infty$ caps the gradient energy (Proposition C.11). When the inter-surface gradient reaches this structural limit, further reduction in separation does not increase the force — the gradient has saturated.

The saturation is the Casimir-scale manifestation of the Horizon Surface (§C.7.6, Remark C.75): the same mobility-collapse mechanism that prevents the density from reaching $\rho_{\max}$ in the PDE analysis creates a maximum achievable force between surfaces in the physical application.

Standard Casimir theory (Lifshitz formula with material corrections) predicts a smooth $d^{-4}$ divergence at small separations, with corrections from finite conductivity, surface roughness, and temperature, but no structural saturation. ED predicts a plateau.

**Experimental path.** Use MEMS/NEMS or microcantilever platforms with tunable plate separation (gold–gold in salt water, gold–silica in dielectric fluids, graphene–substrate cavities, microfabricated Casimir platforms). Measure $F(d)$ down to $\sim$10 nm separation. Compute $C_{\mathrm{ED}}$ from cavity geometry and dielectric environment. Identify the predicted saturation plateau at $d_{\mathrm{sat}}$.

**Falsification condition.** A smooth divergence with no plateau — consistent with the Lifshitz formula including full material corrections — falsifies this prediction.

---

### 5.4 Microresonator Frequency-Phase Threshold

**Prediction.** The frequency-conversion efficiency $\eta(P)$ in a nonlinear microresonator exhibits a structural transition at a critical pump power $P_{\mathrm{crit}}$:

- Below $P_{\mathrm{crit}}$: weak, noisy, dispersion-limited conversion.
- At $P_{\mathrm{crit}}$: a nonlinear jump in efficiency as ED locking activates.
- Above $P_{\mathrm{crit}}$: stable, high-yield conversion insensitive to small detuning.

The critical power $P_{\mathrm{crit}}$ depends on the ED-complexity of the cavity (geometry, mode multiplicity, material symmetry), not on standard dispersion parameters.

**Architectural origin.** Nonlinear frequency conversion, in the ED framework, corresponds to a multi-mode density-locking transition. Below the threshold, the density field in the cavity has insufficient gradient content to activate the nonlinear triad coupling (Principle 7): the modes are weakly interacting and conversion is inefficient. At $P_{\mathrm{crit}}$, the intracavity $C_{\mathrm{ED}}$ crosses the threshold where the triad selection rules (Theorem C.34) become active, and the modes lock into a coherent energy-transfer pattern.

The jump in efficiency is the photonic analogue of the transition from Regime II to Regime III (§2.4): below the threshold, the modes are in the linear basin; above it, the nonlinear triad drives efficient, locked conversion. The robustness to detuning above $P_{\mathrm{crit}}$ reflects the structural stability of the locked state (Theorem D.16).

Standard nonlinear-optical models ($\chi^{(2)}$, $\chi^{(3)}$) predict smooth efficiency curves governed by phase matching and dispersion, with no structural threshold. ED predicts a sharp jump.

**Experimental path.** Use high-Q microresonators with tunable pump power (chalcogenide micro-racetrack resonators, SiN microrings, AlN or LiNbO$_3$ integrated resonators). Sweep pump power and measure $\eta(P)$. Compute $C_{\mathrm{ED}}$ from cavity geometry and mode structure. Identify the predicted threshold jump.

**Falsification condition.** A smooth, dispersion-limited efficiency curve with no threshold — across multiple cavity geometries — falsifies this prediction.

---

### 5.5 Linewidth Asymmetry

**Prediction.** The optical linewidth $\kappa(\Delta)$ of a high-Q microresonator, measured as a function of detuning $\Delta$, exhibits:

- Symmetric Lorentzian behavior at low ED-gradient.
- Increasing skew as ED gradients build.
- A distinct asymmetric splitting when the ED field crosses a structural threshold.

The onset of asymmetry depends on the ED-complexity of the cavity (mode density, geometry, pump configuration), not on standard loss mechanisms.

**Architectural origin.** In the ED framework, the optical mode profile is a density field whose gradient content determines its dissipation rate. The dissipation channel decomposition (Appendix C, §C.5.6) shows that the diffusive channel $\mathcal{D}_{\mathrm{diff}}$ and the penalty channel $\mathcal{D}_{\mathrm{pen}}$ contribute asymmetrically to the total linewidth when the density field is spatially non-uniform: the gradient-dependent term $D\,P_*'\|\nabla\rho\|_{L^2}^2$ (eq. C.53) weights the high-gradient side of the mode profile more heavily than the low-gradient side.

When the intracavity ED field is symmetric (low $C_{\mathrm{ED}}$), both sides contribute equally, and the linewidth is symmetric (Lorentzian). When the field becomes asymmetric — due to geometry, pump detuning, or multi-mode participation — the gradient imbalance produces a skewed linewidth. The splitting occurs when $C_{\mathrm{ED}}$ crosses the stability threshold and the mode profile bifurcates into two distinct branches with different gradient structures (the center manifold bifurcation of Appendix C.6).

Standard cavity theory (linear and nonlinear) predicts symmetric Lorentzian broadening from material loss and coupling, with no structural mechanism for asymmetry. ED predicts a gradient-driven asymmetry.

**Experimental path.** Use high-Q microresonators with tunable detuning and pump power (SiN microrings, AlN or LiNbO$_3$ resonators, silica microtoroids, chalcogenide micro-racetracks). Sweep detuning while measuring the cavity transmission spectrum. Compute $C_{\mathrm{ED}}$ from mode structure and cavity geometry. Identify the predicted asymmetric splitting.

**Falsification condition.** A symmetric Lorentzian linewidth at all pump powers and detunings — with no structural splitting — falsifies this prediction.

---

### 5.6 Photonic Crystal Gradient Limit

**Prediction.** Nanophotonic cavities do not achieve arbitrarily high field confinement. As the spatial mode is squeezed, the event-density gradient inside the cavity approaches a structural limit, beyond which further geometric confinement does not increase the local field intensity.

The cavity field intensity $I(V_{\mathrm{eff}})$ exhibits:

- Standard scaling for large mode volumes.
- Steep enhancement as the cavity approaches the band edge.
- A saturation plateau when the ED gradient reaches its structural maximum.

The saturation volume $V_{\mathrm{sat}}$ depends on the ED-complexity of the lattice (symmetry, defect geometry, dielectric contrast), not on band-edge dispersion.

**Architectural origin.** The saturation is the photonic manifestation of the mobility-collapse barrier (Principle 4). In the ED framework, the optical field intensity is proportional to the density $\rho$ of the photonic mode. As the mode volume shrinks, $|\nabla\rho|^2$ increases (the field is concentrated into a smaller region), and $C_{\mathrm{ED}}$ grows. The energy barrier $\Phi(\rho) \to +\infty$ at $\rho_{\max}$ (Proposition C.11) caps the achievable density, and hence the achievable field intensity. The gradient suppression near $\rho_{\max}$ (Proposition C.10) ensures that the approach to saturation is smooth.

Standard photonic-crystal theory and Purcell-factor models predict continuous enhancement as $V_{\mathrm{eff}} \to 0$, limited only by material absorption and fabrication imperfections. ED predicts a structural ceiling independent of fabrication quality.

**Experimental path.** Use nanophotonic cavities with tunable defect geometry (Si or SiN photonic-crystal nanobeams, L3 or H0 defect cavities, high-contrast 2D photonic-crystal slabs, inverse-designed nanocavities). Vary defect geometry to sweep the effective mode volume. Measure local field intensity via nonlinear emission, SHG, or photoluminescence enhancement. Compute $C_{\mathrm{ED}}$ from lattice symmetry and defect structure. Identify the predicted saturation plateau.

**Falsification condition.** Smooth, unbounded enhancement with no plateau — continuing to scale as predicted by Purcell-factor theory to arbitrarily small mode volumes — falsifies this prediction.

---

### 5.7 Multi-Timescale Comb Formation Threshold

**Prediction.** Optical frequency-comb formation in microresonators is governed by a sharp, thresholded onset rather than a smooth transition from modulation instability to soliton formation. The comb formation curve $\eta_{\mathrm{comb}}(P, \Delta)$ exhibits:

- Weak, noisy sidebands at low ED-gradient.
- Increasing modulation instability as pump power rises.
- A sudden transition to stable, broadband combs when multi-timescale ED locking activates.
- Robustness to small detuning changes once the locked regime is active.

The critical pump power $P_{\mathrm{crit}}$ and detuning $\Delta_{\mathrm{crit}}$ depend on the ED-complexity of the cavity (mode density, geometry, thermal pathways), not on standard Lugiato–Lefever (LLE) parameters alone.

**Architectural origin.** The comb-formation threshold corresponds to the synchronization of three time scales within the ED framework: the fast round-trip time (spatial mode dynamics, governed by $D\alpha_n$ from Appendix C.3), the intermediate thermal time scale (governed by the participation variable $v$ with time constant $\tau$, Principle 5), and the slow carrier or lattice time scale. When the pump power crosses $P_{\mathrm{crit}}$, the intracavity $C_{\mathrm{ED}}$ is sufficient to activate the triad coupling (Principle 7) across all three scales simultaneously, locking the modes into a stable comb pattern.

The threshold corresponds to the entry into the nonlinear triad-active regime (Regime III of §2.4), where the selection rules of Theorem C.34 produce the broadband spectral structure characteristic of a frequency comb. The robustness above threshold reflects the structural stability of the ED-equivalent state (Theorem D.16).

Standard LLE theory predicts a continuous transition from modulation instability to soliton formation, governed by the interplay of dispersion and Kerr nonlinearity. The transition is smooth in the LLE bifurcation diagram. ED predicts a sharp structural threshold.

**Experimental path.** Use microcomb-capable resonators with tunable pump power and detuning (SiN microrings, AlN or LiNbO$_3$ resonators, silica microtoroids, chalcogenide micro-racetracks). Sweep pump power and detuning while monitoring comb spectra. Compute $C_{\mathrm{ED}}$ from cavity geometry, thermal pathways, and mode structure. Identify the predicted sharp onset.

**Falsification condition.** A smooth, continuous transition from noisy sidebands to stable combs — with no identifiable structural threshold — falsifies this prediction.

---

### 5.8 ED-Limited Soliton Step Height

**Prediction.** The discrete "soliton steps" observed in pumped microresonators have a maximum height that is capped by the ED gradient limit. The soliton step height $H(P, \Delta)$ exhibits:

- Standard growth at low ED-gradient.
- Steepening as the system approaches soliton formation.
- A saturation plateau where further pump power does not increase step height.
- Robustness of the plateau across small detuning changes.

The saturation height $H_{\mathrm{sat}}$ depends on the ED-complexity of the cavity (mode density, geometry, thermal pathways), not on nonlinear dispersion parameters alone.

**Architectural origin.** The soliton step height measures the amplitude of the intracavity density modulation. In the ED framework, this amplitude is bounded by the mobility-collapse barrier (Principle 4): the energy cost $\Phi(\rho) \to +\infty$ as $\rho \to \rho_{\max}$ ensures that the density modulation cannot exceed the capacity bound. The gradient suppression near $\rho_{\max}$ (Proposition C.10) further limits the achievable spatial contrast.

The saturation is the soliton-scale manifestation of the same Horizon Surface that prevents the galactic density from exceeding $\rho_{\max}$ (§C.7.6) and that caps the Casimir gradient (§5.3). In each case, the mobility collapse creates a structural ceiling on the achievable density gradient.

Standard LLE soliton theory predicts that step height scales smoothly with pump power and detuning, limited only by material nonlinearity and dispersion. No structural upper bound is predicted. ED predicts a hard ceiling.

**Experimental path.** Use microcomb-capable resonators with tunable pump power and detuning. Sweep pump power while monitoring the soliton step in the transmission curve. Compute $C_{\mathrm{ED}}$ from cavity geometry, thermal pathways, and mode structure. Identify the predicted saturation plateau in step height.

**Falsification condition.** Smooth, unbounded increase in soliton step height with pump power — with no saturation plateau — falsifies this prediction.

---

## 6. ED-Phononics and Orbital Flow

The ED architecture predicts that lattice dynamics — phonons, thermal transport, and angular-momentum transfer — are governed by the gradient and vorticity structure of the event-density field, not by quasiparticle scattering amplitudes alone. This section derives two predictions that probe the deepest structural layer of the ED ontology: the claim that rotating density structures in any medium generate curvature in the ED field, and that this curvature produces measurable orbital currents independent of magnetic order.

In the phononic context, the density field $\rho(x,t)$ is identified with the local event density of the lattice — a coarse-grained measure of the rate of atomic-scale dynamical events (vibrations, bond distortions, thermal excitations) at position $x$. A thermal gradient creates a spatial gradient in $\rho$; a chiral phonon mode creates a rotating density pattern. The ED-complexity $C_{\mathrm{ED}} = \int|\nabla\rho|^2\,d^3x$ measures the total gradient content, while the *ED-vorticity* measures the curl of the density-flow field.

---

### 6.1 Chiral-Phonon ED-Vorticity Test

**Prediction.** A chiral phonon mode — a lattice vibration in which atoms execute circular motion — generates a localized vortex in the ED-flow field (an ED-vortex). This vortex produces curvature in the event-density field that acts as emergent magnetism, entraining nearby electron ED-flow loops and generating a measurable orbital angular-momentum current.

The magnitude of the orbital current scales with:

- The ED-vorticity of the phonon mode (determined by the circularity and amplitude of the atomic motion).
- The local ED-tension (the magnitude of $|\nabla\rho|$, set by the thermal gradient).
- The participation bandwidth between lattice and electrons (the coupling efficiency of the mediated channel).

The orbital current does *not* scale with:

- Phonon population alone.
- Magnetic susceptibility.
- Band-structure symmetry.

**Architectural origin.** The ED-vortex is a consequence of the operator structure (Principle 1) acting on a rotating density pattern. When $\rho(x,t)$ has a time-dependent helical structure (as produced by a chiral phonon), the gradient-squared nonlinearity $M'(\rho)|\nabla\rho|^2$ (Principle 7) generates a non-zero curl in the effective force field. This curl is the ED-vorticity: a localized rotational structure in the density dynamics.

The participation feedback loop (Principle 5) sustains the vortex: the participation variable $v$ integrates the operator output $F[\rho]$, which includes the vortical contribution, and feeds it back into the density equation through the mediated channel $Hv$. The result is a self-sustaining rotational density structure that persists as long as the chiral phonon drives it.

The entrainment of electron ED-flow is a consequence of channel complementarity (Principle 2): the electron density and the lattice density share the same ED field (they are coupled components of the total event density), so a vortex in the lattice density entrains a corresponding vortex in the electron density. The orbital current is the physical manifestation of this entrainment.

The key distinction from standard theory is the *mechanism* of angular-momentum transfer. Standard theory (phonon–electron coupling, spin-orbit interaction) attributes the orbital current to a coupling between the phonon angular momentum and the electron orbital degrees of freedom, mediated by the crystal potential. ED attributes it to a structural feature of the density field itself: the ED-vortex is a geometric object (analogous to the Spiral motif of ED-Arch-02) that entrains any overlapping density component by the architecture of the coupled system.

**Contrast with standard theory.** Standard phonon transport theory predicts that chiral phonons transfer angular momentum to electrons through spin-orbit coupling and crystal-field effects. The current depends on the phonon population, the coupling matrix elements, and the band-structure symmetry. ED predicts a different scaling: the current depends on ED-vorticity and ED-tension (gradient content), not on phonon number or band symmetry. The two theories agree qualitatively (both predict orbital currents from chiral phonons) but disagree quantitatively on what the current scales with.

**Experimental path.** Use crystals with known chiral phonon modes:

- $\alpha$-quartz.
- Transition-metal dichalcogenides (e.g., WSe$_2$, MoS$_2$).
- Polar or piezoelectric lattices.

For each material:

1. Apply a controlled thermal gradient to bias phonon chirality (preferentially exciting one handedness).
2. Measure the orbital angular-momentum current via XMCD, Kerr rotation, or orbital Hall probes.
3. Extract the ED-vorticity from the phonon circularity and lattice symmetry.
4. Compare the current magnitude to ED-tension ($|\nabla T|$ as a proxy for $|\nabla\rho|$) rather than to phonon population.

**Falsification condition.** If the orbital current scales with phonon population and band-structure coupling constants but shows no independent dependence on the thermal gradient (ED-tension) — specifically, if the current vanishes when phonon population is held fixed and the thermal gradient is varied, or if it persists identically when the thermal gradient is removed but phonon population is maintained by other means — then the ED-vorticity prediction is falsified. A clean absence of entrainment in a system with confirmed chiral phonons and a strong thermal gradient would constitute decisive evidence against this ED prediction.

---

### 6.2 Orbital Seebeck ED-Tension Test

**Prediction.** A thermal gradient in a nonmagnetic crystal with chiral phonon modes generates an orbital angular-momentum current (the orbital Seebeck effect). ED predicts that this current is driven by the ED-tension gradient — the spatial gradient in event-production rate — rather than by the phonon population gradient.

The orbital Seebeck coefficient depends on:

- The ED-tension gradient ($\nabla\rho$, proxied by the temperature gradient $\nabla T$).
- The chirality of available phonon modes (the lattice's capacity to support rotational density patterns).
- The participation bandwidth between phonons and electrons (the coupling efficiency of the mediated channel, Principle 5).

The coefficient is independent of:

- Charge carrier density.
- Magnetic ordering.
- Phonon coherence time.

ED makes three specific sub-predictions:

1. **Persistence without coherence.** The orbital current persists even when phonon coherence is degraded (e.g., by disorder or elevated temperature), because the ED-vorticity is a structural feature of the rotating density field, not a coherent quantum state.
2. **Tension scaling.** The current magnitude increases with ED-tension (thermal gradient) even at fixed phonon population, because the driving force is the gradient in $\rho$, not the number of phonons.
3. **Lattice universality.** The effect appears in any lattice supporting circular ED-flow — not only in materials with strong spin-orbit coupling, but in any polar, chiral, or piezoelectric crystal.

**Architectural origin.** The orbital Seebeck effect, in the ED framework, is a direct consequence of the dissipation channel structure (Appendix C, §C.5.6). A thermal gradient creates a spatial gradient in the event-density field: $\nabla\rho \neq 0$. This gradient drives a net ED-flow from the hot side (high event rate, high $\rho$) to the cold side (low event rate, low $\rho$), through the diffusive channel $M(\rho)\nabla^2\rho$ (Principle 1). In a chiral lattice, the ED-flow acquires a rotational component (the phonon chirality imposes a helical geometry on $\nabla\rho$), producing a net angular-momentum flux.

The persistence without coherence follows from the robustness of the ED-vorticity: it depends on the *gradient structure* of $\rho$, not on the phase coherence of individual phonon modes. As long as the thermal gradient maintains $\nabla\rho \neq 0$, the vortical flow persists, even if the individual phonon states are thermally mixed. This is the phononic manifestation of the structural stability theorem (Theorem D.16): the architectural features of the ED system — including the vortex structure — persist under perturbation of the constitutive details (here, the phonon coherence properties).

The tension scaling follows from the dissipation identity (Lemma C.6): the ED-flow rate is bounded below by $D\,c_\delta\,C_{\mathrm{ED}}$, which is proportional to $\|\nabla\rho\|_{L^2}^2$. Since the thermal gradient is the physical proxy for $\nabla\rho$, the orbital current scales with the gradient magnitude.

The lattice universality follows from the universality theorem (Theorem D.19): any system satisfying Principles 1–7 belongs to $\mathcal{U}_{\mathrm{ED}}$. The chiral-phonon orbital current is a consequence of the operator structure (P1), the nonlinear coupling (P7), and the participation feedback (P5) — none of which require spin-orbit coupling or magnetic order. Any lattice with the structural capacity for rotational ED-flow (chirality) will exhibit the effect.

**Contrast with standard theory.** Standard thermoelectric theory (Boltzmann transport, Kubo formalism) predicts that the orbital Seebeck effect requires spin-orbit coupling to convert phonon angular momentum into electronic orbital angular momentum. The coefficient depends on the phonon population, the spin-orbit coupling strength, and the electronic band structure. ED predicts a different mechanism: the driving force is the ED-tension gradient, and the coefficient depends on $\nabla\rho$ and the lattice chirality, not on spin-orbit coupling. The two theories make distinct predictions for materials with weak spin-orbit coupling but strong lattice chirality.

**Experimental path.** Use nonmagnetic crystals with chiral phonon modes:

- Quartz.
- h-BN.
- Strained graphene.
- Polar oxides.

For each sample:

1. Hold phonon population constant using controlled illumination or fixed heating power (maintaining the total phonon number while varying the spatial distribution).
2. Vary the thermal gradient independently (by changing the temperature difference across the sample while keeping the mean temperature fixed).
3. Measure the orbital current as a function of ED-tension ($\nabla T$) at fixed phonon population.
4. Compare the scaling to predictions from phonon-population models (standard theory) versus ED-tension models (ED prediction).

**Falsification condition.** If the orbital current scales with phonon population and collapses when phonon coherence is lost — showing no independent dependence on the thermal gradient at fixed phonon number — then the ED-tension interpretation is falsified. A current that tracks phonon number rather than gradient magnitude, across multiple materials and gradient conditions, would constitute decisive evidence against this prediction.

---

## 7. Cross-Domain Universality

The preceding four sections derived predictions in five physical domains: quantum mechanics (Section 3), galactic dynamics (Section 4), condensed matter and photonics (Section 5), and phononics (Section 6). Each prediction was traced to specific canonical principles and specific theorems in Appendix C. This section demonstrates that the predictions are not independent — they are structural consequences of a single architectural logic, unified by the universality class $\mathcal{U}_{\mathrm{ED}}$ established in Appendix D.

---

### 7.1 Five Domains, One Architecture

The five physical domains differ in every conventional respect: the microscopic degrees of freedom, the governing equations of motion, the energy scales, the spatial scales, and the experimental techniques. The following table summarizes these differences.

| Domain | Density field $\rho$ | Spatial scale | Energy scale | Governing physics |
|--------|---------------------|---------------|--------------|-------------------|
| Quantum mechanics | $|\psi(x)|^2$ (probability density) | $10^{-10}$–$10^{-7}$ m | eV | Schrodinger equation, decoherence |
| Galactic dynamics | Event-density of baryonic activity | $10^{19}$–$10^{22}$ m | $10^{40}$–$10^{50}$ J | Gravity, gas dynamics, star formation |
| Condensed matter | Order parameter, electron density | $10^{-9}$–$10^{-3}$ m | meV–eV | BCS, Boltzmann, Ginzburg–Landau |
| Photonics | Optical mode intensity | $10^{-7}$–$10^{-3}$ m | eV | Maxwell, Kerr nonlinearity |
| Phononics | Lattice event density | $10^{-10}$–$10^{-6}$ m | meV | Lattice dynamics, thermal transport |

Despite these differences, ED claims that every system in the table — when its effective dynamics can be written in the canonical form (D.1) — belongs to the same universality class $\mathcal{U}_{\mathrm{ED}}$ and exhibits the same architectural layers: the same eight motifs, the same nine laws, the same eight geometric objects, and the same nine invariants.

This is not an analogy. It is a theorem (Theorem D.19): any system satisfying Principles 1–7 belongs to $\mathcal{U}_{\mathrm{ED}}$, regardless of its microscopic origin. The universality is *architectural*, not quantitative — the systems share structural features, not numerical values.

---

### 7.2 Why the Physical Interpretation of $\rho$ Does Not Matter

The canonical ED system (D.1) operates on an abstract density field $\rho(x,t)$ and a participation variable $v(t)$. The seven principles constrain the *structural properties* of these variables — the form of the operator, the channel decomposition, the penalty uniqueness, the mobility collapse, the feedback loop, the damping discriminant, and the nonlinear coupling — but they do not specify *what $\rho$ physically represents*.

This abstraction is the source of the cross-domain universality. The physical interpretation of $\rho$ varies by domain:

- In quantum mechanics, $\rho = |\psi|^2$ is the Born probability density. Its gradients encode the spatial complexity of the quantum state.
- In galactic dynamics, $\rho$ is the event density generated by baryonic activity. Its gradients encode the spatial distribution of dynamical processes (rotation, star formation, turbulence).
- In condensed matter, $\rho$ is the relevant order parameter or electron density. Its gradients encode the spatial structure of the phase (superconducting gap, transport channels, Casimir fields).
- In photonics, $\rho$ is the intracavity mode intensity. Its gradients encode the spatial profile of the optical field.
- In phononics, $\rho$ is the lattice event density. Its gradients encode the spatial distribution of thermal and vibrational activity.

In every case, the *mathematical* role of $\rho$ is identical: it is a non-negative scalar field on a bounded domain, evolving under a quasilinear parabolic operator coupled to a participation variable through two complementary channels. The theorems of Appendix C — local and global existence (C.1–C.2), spectral structure (C.3–C.4), stability (C.5), bifurcation (C.6), and long-time behavior (C.7) — hold for any $\rho$ satisfying these structural conditions. The specific physical content of $\rho$ enters only through the constitutive functions $M(\rho)$ and $P(\rho)$, which Theorem D.8 shows can vary freely within $\mathcal{U}_{\mathrm{ED}}$ as long as Principles 3, 4, and 7 are satisfied.

The consequence is stark: the ED architecture does not need to know whether it is describing a molecule, a galaxy, a superconductor, a laser cavity, or a crystal. It needs to know only the structural form of the dynamics. If the form satisfies Principles 1–7, the predictions follow.

---

### 7.3 ED-Complexity as the Unifying Quantity

The central physical quantity across all five domains is $C_{\mathrm{ED}} = \int|\nabla\rho|^2\,d^dx$ (Section 2). In each domain, $C_{\mathrm{ED}}$ measures the same mathematical quantity — the total gradient content of $\rho$ — but its physical meaning differs:

| Domain | $C_{\mathrm{ED}}$ measures | Low $C_{\mathrm{ED}}$ | High $C_{\mathrm{ED}}$ |
|--------|---------------------------|------------------------|-------------------------|
| Quantum | Wavefunction spatial complexity | Symmetric, coherent states | Asymmetric, decohering states |
| Galactic | Gradient content of baryonic activity | Quiescent, weak halos | Active, strong temporal halos |
| Condensed matter | Order-parameter inhomogeneity | Phase-coherent, ballistic | Phase-disordered, diffusive |
| Photonics | Intracavity field gradient | Stable modes, weak harmonics | Mode instability, strong triads |
| Phononics | Lattice event-density gradient | Low vorticity, weak currents | High vorticity, strong entrainment |

The predictions of Sections 3–6 all take the same structural form: a physical observable transitions sharply at a critical $C_{\mathrm{ED}}$, scales with $C_{\mathrm{ED}}$ rather than with the conventionally assumed variable, and is governed by the dissipation identity (Lemma C.6) and the stability threshold (Theorem C.43). The specific observable differs — decoherence rate, halo strength, conductance, conversion efficiency, orbital current — but the mathematical mechanism is identical in every case.

This unification is not imposed; it is derived. The dissipation identity $-d\mathcal{E}/dt \geq D\,c_\delta\,C_{\mathrm{ED}}$ holds for every system in $\mathcal{U}_{\mathrm{ED}}$ (Lemma C.6, Theorem D.19). The stability threshold $\epsilon_0$ exists for every system in $\mathcal{U}_{\mathrm{ED}}$ (Theorem C.43, Theorem D.17). The spectral gap $\gamma > 0$ exists for every system in $\mathcal{U}_{\mathrm{ED}}$ (Corollary C.18). The triad selection rule $k \in \{|m-n|, m+n\}$ holds for every system in $\mathcal{U}_{\mathrm{ED}}$ (Theorem D.14). These are not domain-specific results; they are universal properties of the class.

---

### 7.4 The Universality Class as the Foundation

The universality class $\mathcal{U}_{\mathrm{ED}}$ (Appendix D) underpins the entire applications program through four structural theorems:

**Theorem D.8 (Constitutive closure)** guarantees that the predictions are robust to the choice of $M$ and $P$. Two systems with different mobility functions (e.g., quantum tunneling amplitudes vs. gravitational self-interaction) and different penalty functions (e.g., Born-rule normalization vs. virial equilibrium) belong to the same universality class and exhibit the same architecture, provided both satisfy Principles 3 and 4. This is why the quantum decoherence prediction (§3.1) and the galactic halo prediction (§4.1) — despite having completely different microphysics — share the same structural form: both are governed by $C_{\mathrm{ED}}$, both exhibit a stability threshold, and both converge to a unique equilibrium through the three-stage process of Theorem C.76.

**Theorem D.10 (Domain closure)** guarantees that the predictions are robust to the choice of $\Omega$. The domain may be the configuration space of a molecule, the disk of a galaxy, a thin-film superconductor, a microresonator cross-section, or a crystal unit cell. The architectural layers — modal hierarchy, spectral gap, triad coupling, regime geometry — persist across all domain geometries. This is why the mesoscopic transport threshold (§5.1) and the photonic crystal gradient limit (§5.6) share the same mechanism: both are stability thresholds in a bounded domain with Neumann-type boundary conditions, and the threshold location depends on $C_{\mathrm{ED}}$, not on the specific eigenvalue spectrum of the domain.

**Theorem D.11 (Discriminant invariance)** guarantees that the regime classification is universal. The damping discriminant $\Delta = D + 2\zeta$ is invariant under every ED-equivalence transformation. This means that the qualitative character of the approach to equilibrium — oscillatory (Spiral Sheet) or monotonic (Monotonic Cone) — is a structural property of the system, not an accident of the parameterization. The regime geometry observed in one domain (e.g., oscillatory relaxation of a quantum state in the underdamped regime) is the same regime geometry that appears in another domain (e.g., spiral approach to equilibrium in a galactic temporal halo) whenever $\Delta < 1$.

**Theorem D.19 (Universality)** is the master theorem. It states that *any* system satisfying Principles 1–7 belongs to $\mathcal{U}_{\mathrm{ED}}$. This converts the question of physical applicability into a checkable mathematical condition: to determine whether the ED predictions apply to a given physical system, one must verify that the system's effective dynamics can be cast in the canonical form (D.1) satisfying the seven principles. If so, the full architectural ontology — 8 motifs, 9 laws, 8 geometric objects, 9 invariants — applies, and every prediction derived in this paper follows.

---

### 7.5 The Structural Logic of Cross-Domain Prediction

The cross-domain predictions of this paper follow a single logical chain:

$$
\text{Physical system} \;\xrightarrow{\text{canonical form}}\; \mathcal{S} \in \mathcal{U}_{\mathrm{ED}} \;\xrightarrow{\text{Appendix C}}\; \text{theorems} \;\xrightarrow{C_{\mathrm{ED}}}\; \text{predictions}
$$

The first arrow requires identifying the density field $\rho$, the constitutive functions $M$ and $P$, the channel parameters $D$ and $\zeta$, and the participation time constant $\tau$ for the physical system, and verifying that Principles 1–7 are satisfied. This is the domain-specific step — it requires physical knowledge of the system.

The second arrow is purely mathematical. Once the system is in $\mathcal{U}_{\mathrm{ED}}$, the theorems of Appendix C apply: the dissipation identity, the spectral gap, the stability threshold, the three-stage convergence, the triad selection rules, the bifurcation structure. These are universal — they do not depend on the physical domain.

The third arrow translates the mathematical theorems into physical predictions via $C_{\mathrm{ED}}$. The dissipation bound $-d\mathcal{E}/dt \geq D\,c_\delta\,C_{\mathrm{ED}}$ becomes "decoherence rate scales with gradient complexity" in quantum mechanics, "halo strength scales with dynamical activity" in galactic dynamics, "transport transitions at a critical length" in condensed matter, "conversion efficiency jumps at a critical power" in photonics, and "orbital current scales with ED-tension" in phononics. The mathematical content is the same; only the physical vocabulary changes.

This logical structure has a crucial consequence for falsification. A failed prediction in one domain does not merely weaken the case for ED in that domain — it challenges the universality theorem itself. If the decoherence rate does not scale with $C_{\mathrm{ED}}$, then either the quantum system was incorrectly identified as a member of $\mathcal{U}_{\mathrm{ED}}$ (the canonical-form step failed), or the dissipation identity (Lemma C.6) is wrong, or Principles 1–7 are not the correct structural axioms. The first possibility is a technical error, correctable by refining the identification. The second and third are fundamental — they would require revising the mathematical architecture or the canonical principles.

Conversely, a confirmed prediction in one domain strengthens the case for ED in every domain, because the prediction follows from the same universal theorems. The SPARC dwarf-galaxy test (§4.2, confirmed) is evidence for the dissipation identity and the participation feedback mechanism — which are the same mathematical structures that underlie the quantum decoherence prediction (§3.1) and the mesoscopic transport threshold (§5.1). A success in one domain provides structural support for the architecture as a whole.

---

### 7.6 Summary: One Architecture, Many Worlds

The ED universality class $\mathcal{U}_{\mathrm{ED}}$ contains every dynamical system whose effective density-field dynamics satisfy Principles 1–7. The physical interpretation of the density field — probability, mass, order parameter, mode intensity, lattice activity — is architecturally irrelevant. What matters is the structural form: a quasilinear parabolic operator with mobility collapse and gradient-squared nonlinearity, coupled to a participation variable through complementary channels with a damping discriminant.

Within $\mathcal{U}_{\mathrm{ED}}$, every system exhibits:

- The same dissipation identity, with rate controlled by $C_{\mathrm{ED}}$.
- The same spectral gap, with modal hierarchy determined by the Neumann eigenvalues.
- The same stability threshold, with exponential convergence below $\epsilon_0$.
- The same three-stage convergence: global bounds, algebraic decay, exponential tail.
- The same triad selection rules, with locked harmonic ratios.
- The same regime geometry, with the Spiral Sheet and Monotonic Cone separated by the Boundary Surface at $\mathscr{D}_0 = 0$.
- The same unique, globally attracting equilibrium $(\rho^*, 0)$.

These are not analogies between domains. They are theorems about a class. The domains are different windows onto the same mathematical structure. The predictions of Sections 3–6 are the physical shadows cast by this structure onto the walls of five different experimental caves.

The ED architecture makes the same claim in every domain: *it is not the size of the system, or the mass, or the temperature, or the coupling strength that governs the behavior. It is the gradient complexity of the density field.* This claim is testable in each domain independently, and each test probes the same underlying architecture.

---

## 8. Falsification Suite

The ED architecture is a rigid structure. It makes sharp claims that can be tested, and it can be broken. This section identifies the six cleanest, most decisive experimental tests of the ED ontology — drawn from the predictions of Sections 3–6 — and states, for each, the precise observation that would confirm ED and the precise observation that would falsify it. One test has already been completed. The remaining five are open.

The tests are selected for three properties: (i) they probe core architectural principles (not peripheral consequences), (ii) they produce binary outcomes (the predicted feature is present or absent, with no continuum of partial confirmation), and (iii) they are experimentally accessible with current or near-term technology.

---

### 8.1 Decoherence Scaling

**Core principle tested:** P1 (Operator Structure), P3 (Penalty Equilibrium).

**Architectural claim.** The decoherence rate scales with $C_{\mathrm{ED}}$ (gradient complexity of the density field), not with mass (§3.1, Lemma C.6).

**Confirms ED.** Across a structural-complexity ladder ($C_{60}$ $\to$ $C_{70}$ $\to$ rigid asymmetric molecule $\to$ floppy peptide $\to$ virus capsid), the coherence time correlates more strongly with $C_{\mathrm{ED}}$ than with mass. The decisive signature: a high-mass, high-symmetry molecule (low $C_{\mathrm{ED}}$) coheres longer than a low-mass, low-symmetry molecule (high $C_{\mathrm{ED}}$).

**Falsifies ED.** Coherence time correlates with mass and is uncorrelated with $C_{\mathrm{ED}}$ after controlling for mass. No complexity-based ordering is observed. Mass-based decoherence models (Joos–Zeh, Caldeira–Leggett) provide uniformly better fits than $C_{\mathrm{ED}}$-based models across the ladder.

**Why this test is decisive.** The decoherence rule is a direct consequence of the dissipation identity (Lemma C.6), which is the most fundamental energy estimate in the ED architecture. If the dissipation rate does not scale with $C_{\mathrm{ED}}$, the energy functional $\mathcal{E}$ (eq. C.3) is not the correct Lyapunov functional, and the entire stability and convergence theory of Appendices C.2–C.7 is undermined. This test probes the deepest structural layer of the mathematics.

---

### 8.2 Biological Coherence Limit

**Core principle tested:** P3 (Penalty Equilibrium), P1 (Operator Structure), and the stability threshold (Theorem C.43).

**Architectural claim.** There exists a critical $C_{\mathrm{crit}}$ above which quantum coherence is structurally impossible. All biological macromolecules exceed this threshold (§3.2).

**Confirms ED.** Interferometry on a progression of increasingly complex biomolecules reveals a sharp coherence cutoff: molecules below $C_{\mathrm{crit}}$ show interference, molecules above it do not, and the boundary depends on structural complexity rather than mass. No biomolecule above $C_{\mathrm{crit}}$ shows interference regardless of isolation quality.

**Falsifies ED.** A structurally complex biomolecule (protein, virus capsid) produces clean matter-wave interference in a well-controlled experiment. The coherence persists despite high $C_{\mathrm{ED}}$, demonstrating that structural complexity does not impose an intrinsic decoherence limit.

**Why this test is decisive.** The biological coherence limit is a direct consequence of the nonlinear stability threshold $\epsilon_0$ (Theorem C.43). If the threshold does not exist — if arbitrarily complex systems can be made to cohere by sufficient isolation — then the Lyapunov basin structure of Appendix C.5 does not correctly describe the physical dynamics, and the distinction between Regime II (coherent) and Regime IV (rapidly decohering) is not physical.

---

### 8.3 Dwarf Galaxy Activity Separation (Completed)

**Core principle tested:** P5 (Participation Feedback Loop), P1 (Operator Structure), P3 (Penalty Equilibrium).

**Architectural claim.** Dynamically active dwarf galaxies exhibit larger outer-radius mass discrepancies than quiet dwarfs at fixed baryonic mass, because activity generates temporal tension ($C_{\mathrm{ED}}$) that produces a stronger temporal halo (§4.2).

**Status: Confirmed.** Analysis of 46 dwarf galaxies from the SPARC dataset shows:

- Quiet dwarfs: $\langle D_{\mathrm{outer}}\rangle \approx 3.94$.
- Active dwarfs: $\langle D_{\mathrm{outer}}\rangle \approx 6.01$.
- Ratio: $D_{\mathrm{Active}}/D_{\mathrm{Quiet}} \approx 1.53$.

The separation is clean, reproducible, and visually unambiguous. This is the first completed astrophysical test of the ED architecture.

**Would have falsified ED.** No activity-dependent separation. Quiet and active dwarfs showing identical $D_{\mathrm{outer}}$ distributions, with halo strength depending on mass alone.

**Why this test is decisive.** The activity separation probes the participation feedback loop (Principle 5): the temporal halo is sustained by the participation variable $v$, which integrates the operator output $F[\rho]$ over time. If halo strength were independent of dynamical activity, the participation mechanism would have no physical effect, and the two-channel structure (Principle 2) would be superfluous.

---

### 8.4 Mesoscopic Transport Kink

**Core principle tested:** P1 (Operator Structure), P3 (Penalty Equilibrium), and the stability threshold (Theorem C.43).

**Architectural claim.** The conductance $G(L)$ of a mesoscopic channel exhibits a non-analytic kink at a critical length $L_{\mathrm{crit}}$ where the ED gradient saturates, marking a structural transition from ballistic to diffusive transport (§5.1).

**Confirms ED.** A sharp, reproducible kink in $G(L)$ at a length $L_{\mathrm{crit}}$ that depends on the ED-complexity of the channel geometry (not on impurity concentration). The kink persists across different materials and channel cross-sections, and $L_{\mathrm{crit}}$ can be predicted from the structural geometry.

**Falsifies ED.** A smooth, everywhere-analytic $G(L)$ curve well-described by standard Landauer–Buttiker or Boltzmann transport theory. No kink at any length. The transition from ballistic to diffusive scaling is a continuous crossover governed by the mean free path, with no geometry-dependent structural threshold.

**Why this test is decisive.** The transport kink is a direct physical manifestation of the stability threshold $\epsilon_0$ (Theorem C.43). Below $L_{\mathrm{crit}}$, the density gradient is within the exponential-convergence basin (ballistic); above it, the gradient exceeds the threshold and the system enters the three-stage regime (diffusive). This test probes the existence of the Lyapunov basin boundary in a condensed-matter setting, complementing the quantum test (§8.2) and the galactic test (§8.3). Confirmation in a mesoscopic device would establish the stability threshold as a physical reality across three energy scales separated by twenty orders of magnitude.

---

### 8.5 Casimir-Gradient Saturation

**Core principle tested:** P4 (Mobility Capacity Bound).

**Architectural claim.** The Casimir force $F(d)$ between closely spaced surfaces saturates at sub-100 nm separations because the ED gradient between the surfaces reaches the mobility-collapse limit (§5.3, Proposition C.11).

**Confirms ED.** A clear force plateau at small separations, reproducible across different surface materials and dielectric environments, with the saturation distance $d_{\mathrm{sat}}$ depending on the ED-complexity of the cavity (surface roughness, ionic strength, dielectric structure) rather than on vacuum-mode density. The plateau cannot be explained by material corrections to the Lifshitz formula.

**Falsifies ED.** A smooth $d^{-4}$-type divergence at all accessible separations, consistent with Casimir–Lifshitz theory including full material corrections. No saturation plateau at any separation. The force continues to increase as $d \to 0$ without structural limit.

**Why this test is decisive.** The Casimir saturation probes Principle 4 directly: the mobility collapse $M(\rho_{\max}) = 0$ is the architectural mechanism that prevents the density from exceeding the capacity bound. The energy barrier $\Phi(\rho) \to +\infty$ at $\rho_{\max}$ (Proposition C.11) is the mathematical statement that infinite gradient cost prevents the system from reaching the boundary of the admissible region. If this barrier is not physical — if forces diverge smoothly rather than saturating — then the capacity bound is not a real constraint, and Principle 4 has no physical content. This is the cleanest laboratory test of the Horizon Surface.

---

### 8.6 Microresonator Threshold

**Core principle tested:** P7 (Nonlinear Triad Coupling), P1 (Operator Structure).

**Architectural claim.** The frequency-conversion efficiency $\eta(P)$ in a nonlinear microresonator exhibits a sharp threshold jump at a critical pump power $P_{\mathrm{crit}}$, where multi-timescale ED locking activates (§5.4, §5.7).

**Confirms ED.** A sharp, reproducible efficiency jump at $P_{\mathrm{crit}}$, followed by stable, high-yield conversion robust to small detuning changes. The critical power depends on the ED-complexity of the cavity (geometry, mode multiplicity, material symmetry) rather than on standard dispersion parameters. The same thresholded behavior is observed in both single-frequency conversion (§5.4) and comb formation (§5.7).

**Falsifies ED.** A smooth, continuous efficiency curve with no threshold — governed by phase matching and dispersion, as predicted by standard $\chi^{(2)}$/$\chi^{(3)}$ models and the Lugiato–Lefever equation. Conversion efficiency increases smoothly with pump power, with no jump and no robustness transition.

**Why this test is decisive.** The microresonator threshold probes the nonlinear triad coupling (Principle 7) and its activation at a critical $C_{\mathrm{ED}}$. The triad selection rules (Theorem C.34) predict that inter-modal energy transfer is governed by $\Gamma_{mnk}$ and activates when the intracavity gradient content is sufficient. If frequency conversion is smooth rather than thresholded, the triad coupling does not produce the predicted locking transition, and Principle 7 has no distinctive physical consequence beyond standard nonlinear optics.

---

### 8.7 The Falsification Logic

The six tests are not independent. They probe different principles through different physical systems, but the mathematical infrastructure is shared. The following table maps each test to the principles and theorems it probes.

| Test | Domain | Principles | Key theorem | Status |
|------|--------|------------|-------------|--------|
| Decoherence scaling | Quantum | P1, P3 | Lemma C.6 | Open |
| Biological coherence limit | Quantum | P1, P3, C.43 | Theorem C.43 | Open |
| Dwarf galaxy separation | Galactic | P1, P3, P5 | Theorem C.76 | **Passed** |
| Mesoscopic transport kink | Condensed matter | P1, P3, C.43 | Theorem C.43 | Open |
| Casimir saturation | Condensed matter | P4 | Proposition C.11 | Open |
| Microresonator threshold | Photonics | P1, P7 | Theorem C.34 | Open |

The overlap structure means that a confirmed test in one domain provides indirect evidence for predictions in other domains that share the same mathematical basis:

- Confirming the **decoherence scaling** (Lemma C.6) supports the **dwarf galaxy separation** (same dissipation identity) and the **mesoscopic kink** (same stability threshold).
- Confirming the **Casimir saturation** (Proposition C.11) supports the **soliton step-height limit** (§5.8) and the **photonic crystal gradient limit** (§5.6), since all three probe the same mobility-collapse barrier.
- Confirming the **microresonator threshold** (Theorem C.34) supports the **comb formation threshold** (§5.7) and the **linewidth asymmetry** (§5.5), since all three probe the triad coupling mechanism.

Conversely, a failure in one domain challenges every prediction that shares its mathematical basis. If the decoherence rate does not scale with $C_{\mathrm{ED}}$, the dissipation identity (Lemma C.6) is suspect, and the dwarf-galaxy prediction — which depends on the same identity — must be re-examined.

This interconnection is the strength of the architectural approach. The tests form a web, not a list. Each successful test tightens the web; each failure loosens it. The architecture is either right as a whole or wrong as a whole. There is no middle ground where some principles hold and others fail, because the principles are irreducible (§4 of the Canon): removing any one breaks the architecture completely.

---

### 8.8 Current Status

| Test | Status | Outcome |
|------|--------|---------|
| Decoherence scaling | Open | — |
| Biological coherence limit | Open | — |
| Dwarf galaxy activity separation | **Completed** | **Passed** ($D_{\mathrm{Active}}/D_{\mathrm{Quiet}} \approx 1.53$) |
| Mesoscopic transport kink | Open | — |
| Casimir-gradient saturation | Open | — |
| Microresonator threshold | Open | — |

One test passed. Five remain. The architecture stands until a test breaks it.

---

## 9. Discussion and Outlook

### 9.1 What ED Explains

The Event-Density architecture, as developed in the Architectural Canon and placed on rigorous footing in Appendices C and D, provides structural explanations for phenomena that standard theories treat as unrelated:

**The quantum-classical boundary.** Standard quantum mechanics offers no intrinsic mechanism for classicality — decoherence is attributed entirely to environmental coupling, and the boundary between quantum and classical is a matter of degree. ED provides a structural mechanism: the nonlinear stability threshold $\epsilon_0$ (Theorem C.43) creates a sharp boundary between coherent (Regime II) and decohering (Regime IV) configurations, determined by the gradient complexity $C_{\mathrm{ED}}$ of the density field, not by system size or mass.

**The missing-mass problem.** The discrepancy between observed rotation curves and baryonic mass predictions is conventionally resolved by postulating dark matter — a new species of particle with no non-gravitational interactions. ED resolves the same discrepancy structurally: the temporal halo generated by baryonic activity through the participation feedback loop (Principle 5) produces the additional gravitational effect. The halo depends on activity, not on an invisible mass component. The confirmed SPARC dwarf-galaxy test (§4.2, §8.3) provides the first empirical evidence for this mechanism.

**Transport thresholds in mesoscopic systems.** The ballistic-to-diffusive transition in mesoscopic conductors is conventionally attributed to scattering from impurities and phonons, producing a smooth crossover. ED predicts a structural kink at a critical length determined by the channel's ED-complexity (§5.1), arising from the same stability threshold that governs quantum decoherence. The mechanism is architectural, not material-specific.

**Saturation phenomena in nonlinear optics.** Conventional nonlinear-optical theory predicts smooth scaling of conversion efficiency, soliton height, and field confinement with pump power and mode volume. ED predicts structural ceilings (§5.4, §5.6, §5.8) arising from the mobility-collapse barrier (Principle 4) and the triad-coupling activation (Principle 7). These ceilings are geometry-dependent, not material-dependent.

**Phonon-driven orbital currents.** The observation that chiral phonons generate orbital angular-momentum currents in nonmagnetic crystals is conventionally attributed to spin-orbit coupling. ED provides an alternative mechanism: ED-vorticity generated by rotating density patterns entrains electron flow through the shared density field (§6.1). The current scales with ED-tension rather than phonon population.

In each case, the ED explanation has a distinctive feature: it attributes the phenomenon to the *gradient structure* of a density field, not to a particle, a coupling constant, or an environmental parameter. The explanatory power comes from the architecture, not from the equation.

### 9.2 What ED Predicts

Beyond explaining known phenomena, ED makes predictions that have no counterpart in standard theories:

1. **Complexity-ordered decoherence** (§3.1): coherence time ranks by $C_{\mathrm{ED}}$, not by mass.
2. **A biological coherence limit** (§3.2): a structural threshold above which biomolecules cannot cohere.
3. **Power-law visibility scaling** (§3.3): interference visibility decays as $(1 + \alpha C_{\mathrm{ED}})^{-1}$, not exponentially in mass.
4. **Hyper-coherence in symmetric systems** (§3.4): anomalously long coherence in ultra-symmetric configurations.
5. **A sharp quantum-classical threshold** (§3.5): a structural transition, not a smooth crossover.
6. **Complexity-dependent Bell degradation** (§3.6): entanglement degrades with subsystem complexity at fixed coupling.
7. **Activity-dependent halos** (§4.4): halo strength correlates with dynamical state, not mass alone.
8. **Halo lag in collisions** (§4.3): temporal halos lag behind baryonic mass in cluster collisions.
9. **Halo hysteresis** (§4.6): post-starburst galaxies retain enhanced halos.
10. **A mesoscopic transport kink** (§5.1): a non-analytic transition at a geometry-dependent critical length.
11. **Phase-stiffness saturation** (§5.2): $J(T)$ plateaus before $T_c$ in thin-film superconductors.
12. **Casimir-force saturation** (§5.3): the force plateaus at sub-100 nm separations.
13. **Microresonator efficiency jumps** (§5.4): sharp threshold in frequency conversion.
14. **Linewidth asymmetry** (§5.5): gradient-driven splitting in high-Q cavities.
15. **Photonic confinement saturation** (§5.6): field intensity plateaus at a minimum mode volume.
16. **Comb-formation threshold** (§5.7): sharp onset of stable frequency combs.
17. **Soliton step-height saturation** (§5.8): a structural ceiling on soliton amplitude.
18. **ED-vorticity from chiral phonons** (§6.1): orbital currents scaling with ED-tension.
19. **Orbital Seebeck tension scaling** (§6.2): orbital current driven by $\nabla\rho$, not phonon number.

Each prediction is falsifiable, each is traceable to specific canonical principles and Appendix C theorems, and each distinguishes ED from the standard theory in its domain.

### 9.3 What ED Cannot Yet Explain

The ED architecture, in its current form, has clear limitations:

**Quantitative parameter determination.** The canonical principles determine the *qualitative* structure of the dynamics but do not fix the constitutive functions $M(\rho)$ and $P(\rho)$ or the parameter values $D$, $\zeta$, $\tau$, $\rho_{\max}$ for any specific physical system. These must be determined either by fitting to data or by deriving them from the underlying microphysics. The architecture tells us *what form* the dynamics must take; it does not tell us *which specific equation* governs a given system.

**The canonical-form identification.** For each physical domain, the density field $\rho$, the constitutive functions, and the canonical parameters must be identified from the microscopic theory. This identification has been carried out schematically (§7.2) but not rigorously for any specific physical system other than the ED cosmology PDE itself. The gap between "the architecture applies in principle" and "here is the specific $M(\rho)$ for this superconductor" remains open.

**Multi-field extensions.** The canonical ED system has a single density field $\rho$ and a single participation variable $v$. Physical systems with multiple coupled order parameters (e.g., multi-band superconductors, coupled optical modes, multi-species galactic dynamics) may require extensions of the canonical form. The universality class $\mathcal{U}_{\mathrm{ED}}$ is defined for the single-field case; its generalization to multi-field systems is an open mathematical problem.

**Relativistic regime.** The ED PDE is a parabolic equation on a fixed spatial domain. It does not incorporate relativistic effects, curved spacetime, or dynamical geometry. The galactic predictions (Section 4) are derived in the non-relativistic limit, where the temporal halo produces an effective Newtonian potential. Extension to the relativistic regime — necessary for cosmological applications (expansion, structure formation, horizon physics) — requires a covariant formulation of the ED architecture that has not yet been developed.

**Derivation from first principles.** The seven canonical principles are stated axiomatically. They are not derived from a more fundamental theory (a Lagrangian, an action principle, or a quantum-gravity framework). Whether the principles are fundamental or emergent — and if emergent, from what — is an open question. The Architectural Canon establishes their sufficiency and minimality but not their origin.

### 9.4 What the Numerical Atlas Will Provide

The ED-SIM simulation engine, which implements the canonical ED system with 14 laws and over 56,000 data records, provides a computational laboratory for exploring the architecture beyond the analytic results of Appendix C. The planned Numerical Atlas will supply:

**Quantitative constitutive maps.** Systematic numerical surveys of the $(D, \zeta, \tau)$-parameter space, mapping the dependence of decay rates, oscillation frequencies, triad amplitude ratios, and convergence times on the canonical parameters. These maps will convert the qualitative predictions of this paper into quantitative targets for experiment.

**Nonlinear regime exploration.** The analytic results of Appendix C are sharpest near equilibrium (linearized spectral theory, local stability). The Numerical Atlas will explore the far-from-equilibrium regime (Regime IV of §2.4), where the nonlinear triad is fully active and the three-stage convergence proceeds through its algebraic phase. This is the regime most relevant to high-$C_{\mathrm{ED}}$ physical systems (biomolecules, active galaxies, turbulent cavities).

**Domain-specific parameter fitting.** For each physical domain, the Atlas will provide reference solutions that can be compared to experimental data, enabling the extraction of the constitutive functions $M(\rho)$ and $P(\rho)$ and the canonical parameters from measured observables.

**Bifurcation diagrams.** The center manifold analysis of Appendix C.6 characterizes the regime transition near the critical surface $\mathscr{D}_0 = 0$. The Numerical Atlas will map the full nonlinear bifurcation structure, including hysteresis loops, multi-stability (if present in extended systems), and the basin geometry in parameter space.

### 9.5 Experimental Priorities

The falsification suite of Section 8 identifies six decisive tests. Given current experimental capabilities, the recommended priority ordering is:

**Tier 1 — Immediate (existing platforms, minimal new infrastructure):**

1. **Mesoscopic transport kink** (§5.1, §8.4). Graphene nanoribbons and GaAs heterostructures with tunable channel length are mature platforms. The measurement ($G$ vs. $L$) is standard. The predicted kink is a binary observable. This is the lowest-cost, fastest-turnaround test.

2. **Microresonator threshold** (§5.4, §8.6). High-Q SiN microrings and AlN resonators with tunable pump power are commercially available. Sweeping pump power and measuring conversion efficiency is a standard photonics experiment. The predicted threshold jump is a binary observable.

**Tier 2 — Near-term (requires targeted sample preparation):**

3. **Decoherence scaling** (§3.1, §8.1). Matter-wave interferometry on a complexity ladder from $C_{60}$ to biomolecules requires specialized molecular beams and interferometric setups (Talbot–Lau, KDTLI), which exist at several laboratories worldwide. The main challenge is preparing and launching the higher-complexity molecules.

4. **Casimir saturation** (§5.3, §8.5). MEMS-based Casimir-force measurements at sub-100 nm separations are technically challenging but within reach of current nanofabrication capabilities. The predicted plateau is a binary observable.

**Tier 3 — Longer-term (requires new capabilities or larger datasets):**

5. **Biological coherence limit** (§3.2, §8.2). Interferometry on proteins and virus capsids pushes the frontier of matter-wave experiments. This test requires advances in molecular-beam preparation for large biomolecules.

6. **Dwarf galaxy activity separation** (§4.2, §8.3). Already completed and passed. Extension to a larger sample (beyond the 46 SPARC dwarfs) and independent replication with other datasets would strengthen the result.

### 9.6 The Next Papers

The present paper is the second in the ED-Arch foundational arc, following the Architectural Canon (which established the seven principles) and the Rigour Paper (which proved the mathematical well-posedness). The planned continuation is:

**ED-Arch-X: Architectural Diagnostics.** A systematic method for determining whether a given dynamical system belongs to $\mathcal{U}_{\mathrm{ED}}$. This paper will develop the canonical-form identification procedure (§9.3) into a practical diagnostic toolkit, providing algorithms for extracting $M(\rho)$, $P(\rho)$, and the canonical parameters from experimental data.

**ED-Cosmo: Physical Cosmology Through ED.** Application of the temporal-halo mechanism to cosmological observables: the Hubble tension, large-scale structure, the CMB power spectrum, and the accelerating expansion. This paper will require the relativistic extension of the ED architecture (§9.3) and will draw on the galactic predictions of Section 4 as its empirical foundation.

**ED Numerical Atlas.** The computational companion to the present paper, providing quantitative parameter maps, nonlinear regime surveys, and domain-specific reference solutions for comparison with experimental data.

**ED Experimental Reports.** Individual papers reporting the outcomes of the falsification-suite tests (§8.1–§8.6), each structured as a self-contained experimental test of a specific ED prediction. The first such report — the dwarf-galaxy rotation-curve analysis — has been completed and is documented in the Open Note (ED-00, §8).

### 9.7 Closing Statement

The Event-Density architecture is a structural claim about the mathematical organization of physical dynamics. It asserts that seven irreducible principles — operator structure, channel complementarity, penalty equilibrium, mobility capacity bound, participation feedback, damping discriminant, and nonlinear triad coupling — generate a complete architectural ontology that is universal across physical domains.

This paper has derived the physical consequences of that claim. Nineteen predictions, spanning quantum mechanics, galactic dynamics, condensed matter, photonics, and phononics, follow from the architecture through the rigorous mathematical infrastructure of Appendices C and D. One prediction has been tested and confirmed. The remaining eighteen are open.

The predictions are sharp: each has a stated falsification condition. The architecture is rigid: each principle is irreducible, and the failure of any prediction challenges the architecture as a whole. The universality is mathematical: every system satisfying Principles 1–7 belongs to $\mathcal{U}_{\mathrm{ED}}$ and inherits the full nine-layer ontology.

The program is clear: test the predictions. The architecture will stand or fall on the outcomes. No parameter can be adjusted to accommodate a failure; no auxiliary hypothesis can be invoked to explain away a discrepancy. The seven principles either describe the structural logic of physical dynamics, or they do not.

The experiments will decide.