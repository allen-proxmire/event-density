# Event Density: One Substrate, Three Domains
## A Structural Account of Quantum Mechanics, Galactic Gravity, and Universal Soft-Matter Mobility

**Allen Proxmire**
**April 2026**

---

## Abstract

We present Event Density (ED), a single substrate ontology of discrete events and relational adjacency from which the foundational structures of three nominally separate domains of physics are derived rather than postulated. From substrate primitives alone we obtain: (i) the four foundational postulates of non-relativistic quantum mechanics — Born's rule, the Schrödinger equation, the Heisenberg uncertainty bound, and the Bell–Tsirelson bound — as forced structural theorems, together with gauge fields, canonical (anti-)commutation, UV-finiteness, and the kernel-level arrow of time; (ii) Newton's gravitational law with `G = c³ ℓ_P² / ℏ`, the MOND transition acceleration `a₀ = c·H₀/(2π)`, the deep-regime combination law `a = √(a_N · a₀)`, and the slope-4 baryonic Tully–Fisher relation `v⁴ = G·M·a₀`, all parameter-free; and (iii) a universal degenerate-mobility law `D(c) = D₀ (1 − c/c_max)^β` that fits diffusion data from ten chemically unrelated soft-matter systems with `R² > 0.986` at a common exponent `β = 1.72 ± 0.37`. The framework predicts no laboratory result that differs from standard physics in the regimes where standard physics has been tested. What it does is replace a long list of independent postulates with a smaller list of substrate commitments, from which those postulates follow as theorems. We tabulate twenty-one forced structural theorems plus one foundational substrate rule, derive the load-bearing results, and close with the framework's pre-registered empirical falsifiers.

---

## 1. Introduction

Modern physics is organized around three nominally separate problems: the very small, the very large, and the messy middle. Quantum mechanics describes particles and fields. General relativity (with a dark-matter patch) describes galaxies and cosmology. A sprawl of phenomenological models describes soft matter, glasses, and biological transport. Each domain has its own postulates, its own constants, and its own characteristic puzzles. Walk into any one of them and ask why the rules are the rules, and the answer is the same: *because we postulate them, and the postulates work.*

This paper argues that a single substrate underlies all three domains, and that the postulates of each can be derived rather than assumed.

The substrate is **Event Density** (ED): a relational ontology in which discrete micro-events are the fundamental constituents, and physics is what their participation structure makes possible. There are no fundamental fields, no fundamental spacetime, no fundamental wavefunction. Particles are stable chains of micro-events; spacetime is an emergent geometry of the relational structure; the wavefunction is a participation measure on a graph. From this minimal toolkit and a small set of structural commitments, the foundational structures of the three domains follow as theorems.

The paper is organized as follows. Section 2 lays out the substrate primitives, the participation measure, the chain stability landscape, and the canonical ED partial differential equation. Section 3 catalogs the twenty-one forced structural theorems plus the one foundational substrate rule that constitute the program's current results. Sections 4, 5, and 6 derive the load-bearing results in quantum mechanics, gravity, and soft matter respectively. Section 7 states the framework's pre-registered empirical falsifiers. Section 8 concludes.

The framework predicts no current laboratory result that differs from standard physics. It replaces a long list of independent postulates with a smaller list of substrate commitments from which those postulates follow. That is the only claim being made. Whether the substrate commitments are right is the empirical question, addressed by the falsifiers in Section 7.

---

## 2. The ED Substrate

### 2.1 Primitives

The ED ontology rests on a small set of primitives. We list those load-bearing for the present paper.

- **Micro-events.** Reality consists of discrete acts of becoming. The local rate of micro-event production at x is the event density `ρ(x,t)`.
- **Participation and adjacency.** Micro-events do not exist in isolation; they participate in one another's becoming. Two micro-events are *adjacent* when they integrate each other's becoming, share participation bandwidth, and maintain coherent relational timing.
- **Channels.** A channel K is a stable subgraph along which micro-events propagate. Channels carry edge weights `b_K` called *bandwidth*.
- **Chains.** A chain is a sequence of micro-events maintaining coherent participation across its extent. Chains are the substrate-level objects we call particles.
- **Decoupling surfaces.** Participation thresholds where reciprocal participation between two regions becomes one-sided. The cosmic decoupling surface lies at radius `R_H = c/H₀`. An accelerating chain induces a decoupling surface at distance `d_a = c²/a` behind it.
- **Commitment irreversibility (P11).** Every commitment event is irreversible. Once made, never unmade.

### 2.2 The participation measure

A channel's participation in becoming is described by the **participation measure**:

$$P_K(x,t) = \sqrt{b_K(x,t)} \cdot e^{i \pi_K(x,t)},$$

where `b_K` is the channel's bandwidth and `π_K` a U(1)-valued phase. The form of this measure is forced (Theorem T14): the magnitude exponent is fixed by the Cauchy functional equation on bandwidth additivity, and the phase structure by Frobenius. The participation measure is the substrate object whose continuum limit standard quantum mechanics names ψ.

### 2.3 The chain stability landscape

A chain at substrate position x with current micro-event state s evaluates its next propagation step against the available local participation environment by maximizing the **stability score**:

$$\Sigma(e') = \mathrm{Coh}(e', s) - \mathrm{Str}(e', \rho_{\mathrm{local}}) - \mathrm{Grad}(e', \nabla\rho),$$

where Coh measures coherence with the current state, Str the participation strain against the surrounding environment, and Grad the strain accumulated against the surrounding ED-gradient. The chain extends to the next state with maximum Σ. The gradient of Σ experienced by the chain manifests as force.

### 2.4 The canonical ED PDE

Coarse-grained over many chain steps, the substrate dynamics for a participation density `ρ(x,t)` on a bounded domain reduces to a single quasilinear parabolic PDE with three constitutive channels:

$$\partial_t \rho = D \bigl[\, M(\rho) \, \nabla^2 \rho + M'(\rho) |\nabla\rho|^2 - P(\rho) \,\bigr] + H \, v,$$

$$\dot{v} = \tau^{-1}\bigl(\bar F - \zeta\, v\bigr).$$

The three channels are:

- **Mobility (M).** A degenerate nonlinear mobility producing porous-medium-equation behavior. Closes Section 6.
- **Penalty (P).** A monostable penalty producing exponential (Debye) relaxation toward equilibrium.
- **Participation (v).** A global participation variable obeying a damped first-order law and producing telegraph oscillation when coupled to the density channel.

The canonical degenerate mobility is `M(ρ) = (1 − ρ/ρ_max)^β`, which produces the universal soft-matter law of Section 6. The PDE's existence, well-posedness, three-channel decomposition, and exponential stability of equilibrium are established in the foundational ED corpus and not re-derived here.

---

## 3. Forced Theorem Inventory

The substrate-level program has produced twenty-one forced structural theorems plus one foundational substrate rule. Theorems are FORCED-unconditional unless otherwise noted.

| T | Statement | Origin |
|---|---|---|
| T1 | Spin–statistics: η = (−1)^(2s) | Arc R; from Cl(3,1) uniqueness |
| T2 | Cl(3,1) uniqueness | Arc R |
| T3 | Anyon prohibition in 3+1D | Arc R |
| T4 | Dirac equation + g = 2 emergence | Arc R |
| T5 | Gauge-field-as-rule-type (form-level) | Arc Q — *subsumed by T17* |
| T6 | Canonical (anti-)commutation [φ,π]=iℏδ | Arc Q |
| T7 | UV-finiteness | Arc Q |
| T8 | V₁ finite-width vacuum kernel | Arc N |
| T9 | V₁ with Synge world function (curved spacetime) | Phase 3 |
| T10 | Born rule via Gleason–Busch | Phase 1 (born_gleason) |
| T11 | U2-Discrete: sesquilinear inner product | Phase 1 (U2) |
| T12 | U2-Continuum: with conformal gauge | Phase 1 (U2-c) |
| T13 | U5: momentum operator from translation | Phase 1 (U5) |
| T14 | U1: P_K = √b_K · e^(iπ_K) | Phase 1 (U1) |
| T15 | U4: Ĥ = p̂²/2m + V | Phase 1 (U4) |
| T16 | U3: Schrödinger evolution iℏ ∂_t ψ = Ĥψ | Phase 1 (U3); ★ Phase-1 closure |
| T17 | Gauge-field-as-rule-type (synthesis, supersedes T5) | Arc Q closure |
| T18 | V₁ kernel retardation: kernel-level arrow of time | Arc B closure |
| T19 | Newton's law from substrate; G = c³ ℓ_P² / ℏ | arc-SG |
| T20 | Transition acceleration; a₀ = c·H₀/(2π) | arc-SG |
| **R** | **ED Combination Rule** (substrate rule, no number) | arc-SG |
| T21 | Slope-4 BTFR: v⁴ = G·M·a₀ | arc-SG; ★ substrate-gravity closure |

"R" marks the foundational ED Combination Rule (substrate rule rather than numbered theorem). Stars mark closure points: ★ Phase-1 = T16 (all four QM postulates derived); ★ substrate-gravity closure = T21 (galactic phenomenology fully derived).

Sections 4–6 derive the load-bearing results.

---

## 4. Quantum Mechanics from the Substrate

### 4.1 The Born rule (T10) and the Hilbert-space arena (T11, T12)

The Born rule states that the probability of measuring outcome K is

$$\mathrm{Prob}(K) = \frac{|P_K|^2}{\sum_{K'} |P_{K'}|^2} = \frac{b_K}{\sum_{K'} b_{K'}}.$$

The squared form has been a postulate of quantum mechanics for a hundred years. ED derives it. The participation-graph ontology forces *non-contextuality* from below: channels are real structural features of the substrate, bandwidth is an intrinsic edge weight on those channels, and probability is bandwidth share at the measurement locus. The "context" — which other channels happen to be enumerated alongside a given one — is an external organizational choice, and external choices cannot reach intrinsic structure. With non-contextuality forced rather than postulated, Gleason's theorem (extended by Busch's POVM result for two-state systems) yields the squared form as a derivation.

The discrete-channel inner product on participation measures is forced by the same logic to be sesquilinear (T11):

$$\langle P | Q \rangle = \sum_K \overline{P_K} \, Q_K,$$

and lifts uniquely to the continuum under one description-level convention (the conformal gauge of T12). The Bell–Tsirelson bound `|S| ≤ 2√2` follows as a structural consequence of this inner product. The Hilbert space is no longer postulated; it is the Hilbert space the substrate forces.

### 4.2 Momentum, Hamiltonian, and Schrödinger evolution (T13, T15, T16)

Stone's theorem applied to spatial-translation symmetry on the participation-measure Hilbert space yields a unique self-adjoint generator, the momentum operator `p̂ = −iℏ∇` (T13). Plane waves are its eigenfunctions; the standard L² Fourier transform is the unique unitary intertwiner of position and momentum; the Heisenberg uncertainty bound `Δx · Δp ≥ ℏ/2` is a structural consequence.

The Hamiltonian is forced by Galilean Lie-algebra closure. The boost generator `K̂ = mx̂ − tp̂` together with the commutator condition `[Ĥ, K̂] = −iℏp̂` integrate uniquely to

$$\hat H = \frac{|\hat p|^2}{2m} + V(\hat x), \qquad \boxed{\text{factor of 2 = chain-rule integration Jacobian}}$$

The factor of 2 in 1/(2m) is not a convention borrowed from classical mechanics. It is the chain-rule coefficient that emerges when integrating the Galilean commutator condition (T15). With the Hamiltonian fixed, Stone's theorem on time-translation symmetry produces the Schrödinger equation

$$i\hbar \, \partial_t \psi = \hat H \psi$$

as the unique evolution rule the substrate supports (T16). The U3–U4 acyclicity discipline (identification not derivation) closes the loop without circularity. With T16 in hand, all four foundational postulates of non-relativistic quantum mechanics — Born, Bell–Tsirelson, Heisenberg, Schrödinger — are forced structural consequences of the substrate.

### 4.3 Gauge fields (T17)

Beyond the foundational postulates, the gauge field `A_μ` is forced as the participation measure of a structural rule-type `τ_g` (T17). The four-channel content of any non-Abelian gauge theory — group structure, the connection `A_μ`, minimal coupling `∂ → ∂ − igA`, and gauge invariance itself — is derived under a single unified gauge-quotient identification, with all 7/7 GRH refinements closed and 18/18 falsifiers dispatched dark. Gauge invariance is not imposed as a symmetry of an action; it is the interface property of a rule-type — the absence of distinction between structurally identical configurations. T17 supersedes the form-level statement T5.

### 4.4 The kernel-level arrow of time (T18)

The vacuum response kernel `V₁` that mediates how perturbations propagate is uniquely forced to have support restricted to the forward causal cone (T18). Symmetric, advanced, and hybrid kernels are not refuted by an external constraint; they are *non-constructible* from the chain ensemble. The argument runs through P11 (commitment irreversibility) plus locality: each chain's commitments are forward-only in proper time, each commitment can only reach its own causal future, and the chain-summed kernel therefore has forward-cone-only support. The retarded Green's function of standard QFT is the continuum correspondent of `V₁^ret`; the Wightman correlator and Feynman propagator remain unaffected as distinct continuum objects.

---

## 5. Gravity from the Substrate

### 5.1 Newton's law (T19)

Consider a chain at radius R from a baryonic mass M. The strain term Str in the chain stability landscape is determined by the integrated environmental gradient from the chain outward. For a point mass,

$$\int_R^\infty \rho_{\mathrm{grad}}(R')\, dR' \propto \frac{M}{R}, \qquad a \propto \frac{\partial}{\partial R}\!\left(\frac{M}{R}\right) \propto \frac{M}{R^2},$$

recovering the inverse-square law structurally. To fix the proportionality constant, apply the substrate's holographic participation count to a 2-sphere at radius R:

$$N_R = \frac{4\pi R^2}{\ell_{\mathrm{ED}}^2}.$$

A substrate-level equipartition `(1/2) N_R k_B T_R = M c²` together with the Unruh-analog inversion `T_R = ℏa/(2π k_B c)` yields, after the 2π factors cancel,

$$a = \frac{M c^3 \ell_{\mathrm{ED}}^2}{R^2 \hbar} = \frac{GM}{R^2}, \qquad \boxed{\;G = \frac{c^3 \ell_P^2}{\hbar}, \qquad \ell_{\mathrm{ED}} = \ell_P.\;}$$

The substrate's UV cutoff is forced by Newton-recovery to coincide with the Planck length. Newton's gravitational constant is now expressed in fundamental substrate quantities; it is no longer a free parameter.

### 5.2 The transition acceleration (T20)

When a chain accelerates, the three-dimensional isotropy of its participation environment breaks. The chain has a privileged axis along the acceleration direction, with full reciprocal participation forward and progressively-thinned participation backward (decoupled at `d_a = c²/a`). The cosmic decoupling surface, which contributes to the chain's stability landscape, projects onto this anisotropic accessible region not as an isotropic full-sphere fact but as a directional projection along the acceleration axis. Decomposing in spherical harmonics aligned with the acceleration axis, the leading anisotropic mode coupling to the chain's adjacency structure is the dipole `(l = 1, m = 0)`, whose only non-trivial spatial periodicity is the 2π azimuthal cycle. The chain integrates the cosmic-horizon contribution at the effective rate

$$\gamma_{\mathrm{cosmic}}^{\mathrm{eff}} = \frac{H_0}{2\pi}.$$

Setting this equal to the chain's experienced rate `γ_chain = a/c` yields the transition acceleration:

$$\boxed{\;a_0 = \frac{c \cdot H_0}{2\pi} \approx 1.08 \times 10^{-10}\,\mathrm{m/s^2}.\;}$$

The empirical MOND constant is `a₀^(emp) ≈ 1.2 × 10⁻¹⁰ m/s²`. The structural prediction matches to within 10%, parameter-free, robust to the Hubble tension at the 15% level. The factor of 2π is geometric — the azimuthal period of the leading anisotropic projection mode — not phenomenological.

### 5.3 The ED Combination Rule

In the joint weak-gradient regime, where neither local-mass nor cosmic-horizon contribution dominates the chain's accessible region, the chain stability landscape acquires a logarithmic cross-term:

$$\Sigma_{\mathrm{cross}}(R) = \sqrt{G M a_0} \cdot \log(R/R_0) + \mathrm{const},$$

with `R₀` a substrate-internal reference scale. The coefficient `√(GMa₀)` reflects multiplicative participation between the two source contributions: it is their geometric mean rather than their sum. The cross-term is not a perturbative correction; it is the substrate's structural response in the regime where both contributions co-shape the chain's accessible region. Differentiating yields the chain's effective acceleration:

$$\boxed{\;a = \sqrt{a_N \cdot a_0}.\;}$$

This is the foundational **ED Combination Rule**, registered as a substrate rule rather than a numbered theorem.

### 5.4 Flat rotation curves and the slope-4 BTFR (T21)

A chain in circular orbit at radius R from baryonic mass M, in the deep-acceleration regime (`a_N ≪ a₀`), has effective acceleration `a = √(GMa₀)/R` by the Combination Rule. Centripetal balance `a = v²/R` gives:

$$\boxed{\;v^2 = \sqrt{G M a_0}, \qquad v_{\mathrm{flat}}^4 = G \cdot M \cdot a_0.\;}$$

The orbital velocity is constant in R: *flat rotation curves derived structurally from the substrate*. Squaring yields the slope-4 baryonic Tully–Fisher relation, with prefactor

$$G \cdot a_0 = \frac{c^4 \ell_P^2 H_0}{2\pi \hbar}$$

expressed entirely in fundamental substrate constants. No free parameters appear at any step. Theorem T21 closes the substrate-gravity arc: Newton, transition scale, combination rule, and flat-curve / Tully–Fisher phenomenology are all structural consequences of the substrate.

---

## 6. Universal Soft-Matter Mobility from the Canonical PDE

The mobility channel of the canonical ED PDE produces a single universal law for diffusion in concentrated soft matter. We isolate the mobility channel by setting `P ≡ 0` and decoupling the participation variable, leaving

$$\partial_t \rho = D\,\nabla \cdot \bigl[\, M(\rho) \nabla \rho \,\bigr]$$

with the canonical degenerate mobility

$$M(\rho) = \left(1 - \frac{\rho}{\rho_{\mathrm{max}}}\right)^\beta.$$

This is a porous-medium-equation form. Recasting in terms of an effective diffusion coefficient `D_eff(ρ) = D · M(ρ)` and switching to volume fraction `c = ρ/ρ_max`:

$$\boxed{\;D(c) = D_0 \left(1 - \frac{c}{c_{\mathrm{max}}}\right)^\beta.\;}$$

This is the **universal degenerate-mobility law**.

The substrate prediction is structural: the law should fit diffusion data across systems whose microscopic mechanisms differ, with the same functional form and similar exponents, because the substrate's mobility channel produces this form regardless of the underlying material. The exponent β reflects the substrate's coarse-graining, not material-specific microphysics; it should cluster across chemically unrelated systems.

### 6.1 Empirical anchor: ten chemically unrelated systems

We fit the law to diffusion data from ten chemically and microscopically unrelated soft-matter systems: hard-sphere colloids, sucrose–water, BSA protein solutions, lysozyme, PMMA colloids, Ludox silica, PEG–water, dextran, casein micelles, and glycerol–water. The fits give:

$$\beta = 1.72 \pm 0.37, \qquad R^2 > 0.986\ \text{across all ten systems.}$$

A single law, a single clustered exponent, ten chemically unrelated substrates. The substrate prediction of structural universality is realized: the form is universal, the exponent is universal to within ±0.37, and no material-specific machinery is required to fit any of the ten systems. The full data and per-system fit parameters are given in the companion paper *Universal Degenerate-Mobility Scaling in Crowded Soft Matter*.

---

## 7. Empirical Falsifiers

The framework's structural commitments are sharp, and the predictions they generate expose them to laboratory verdict. We enumerate the pre-registered falsifiers:

1. **FRAP in concentrated protein solutions.** The law predicts a recovery profile distinct from the standard Fickian exponential. Specifically, for concentrated BSA the front-radius scaling is `R(t) ∝ t^(1/6)` rather than the Fickian `t^(1/2)`. The full predicted profile has an RLC-analogue ringing structure absent from any exponential model.

2. **AFM force–distance spectroscopy.** The chain stability landscape predicts a specific signature on substrate-resolved force curves at the canonical operating point.

3. **Optomechanical envelope.** Theorem N1 (V₁ finite-width vacuum kernel) predicts a ringdown envelope at `ω ≈ 8·γ_dec` that re-analysis of existing optomechanical data should either confirm or falsify.

4. **Quantum-classical boundary in matter-wave interferometry.** The framework predicts a sharp transition in the 140–250 kDa mass range, five to ten times beyond what current matter-wave interferometers can reach.

5. **Galactic Tully–Fisher with substrate-derived G·a₀.** T21 predicts `v⁴ = G·M·a₀` with prefactor `G·a₀ = c⁴ ℓ_P² H₀ / (2π ℏ)` entirely in substrate constants. This is testable to high precision against the SPARC catalog and similar surveys.

6. **The radial-acceleration relation.** For arbitrary `(a_N, a₀)` the framework predicts a single-valued function `a(a_N)` interpolating between Newtonian (`a → a_N` for `a_N ≫ a₀`) and deep-MOND (`a → √(a_N·a₀)` for `a_N ≪ a₀`) limits. Any galactic system departing from this curve falsifies T19, T20, or the Combination Rule.

These predictions are sharp, parameter-free, and directly testable. The framework is exposed to falsification at the laboratory level as well as the observational level. The pre-registered structure is not a hedge; it is the instrument.

---

## 8. Conclusion

Three nominally separate domains of physics rest on independent collections of postulates. Standard quantum mechanics postulates the Born rule, the Schrödinger equation, the Heisenberg bound, and the gauge structure, and treats their numerical values as inputs. Standard cosmology postulates Newton's law plus a dark-matter patch and treats the MOND transition acceleration as an empirical fit. Standard soft-matter physics treats every diffusing system as its own model. In each case, the question *why must it be that way?* has been deferred.

Event Density takes the question on. From substrate primitives — micro-events, participation, adjacency, channels, decoupling surfaces, commitment irreversibility — it derives, as forced theorems, the four foundational postulates of non-relativistic quantum mechanics; gauge fields and canonical commutation; UV-finiteness and the kernel-level arrow of time; Newton's gravitational law with G expressed in c, ℏ, and the Planck length; the MOND transition acceleration with the famous 2π as a geometric period; the deep-regime combination law; and the slope-4 baryonic Tully–Fisher relation. The same canonical PDE that produces the quantum and gravitational structures produces a universal degenerate-mobility law that fits ten chemically unrelated soft-matter systems with R² > 0.986 at a common exponent.

Twenty-one forced structural theorems plus one foundational substrate rule. No new laboratory predictions for the regimes where standard physics has been tested. New structural answers underneath the old postulates — and a small list of falsifiers exposing the framework to verdict in regimes standard physics has not yet reached.

The framework's case is on the table. The empirical program will dispose of it.

---

## References

- ED-06: *Horizons as Event Density Decoupling Surfaces* (Proxmire 2026).
- ED-07: *Event Density and Relativistic Phenomena* (Proxmire 2026).
- ED-10: *Event Density and the Emergence of Spacetime* (Proxmire 2026).
- ED-I-06: *Fields and Forces in Event Density* (Proxmire 2026).
- *Structural Foundations of ED-Substrate Gravity: Newton, the Transition Scale, the Combination Rule, and the Baryonic Tully–Fisher Relation* (Proxmire 2026). The substrate-gravity foundations paper.
- *Quantum Mechanics as a Forced Structural Consequence of Event Density Primitives* (Proxmire 2026).
- *Relativistic Quantum Mechanics as a Forced Structural Consequence of Event-Density Primitives* (Proxmire 2026).
- *The Born Rule as a Forced Theorem of Event Density: A Gleason–Busch Reconstruction from First Principles* (Proxmire 2026).
- *U3 — Time-Translation, Schrödinger Evolution, and the Closure of Phase 1* (Proxmire 2026).
- *Gauge Fields as Forced Rule-Type Structure: Theorem 17* (Proxmire 2026).
- *The Primitive-Level Arrow of Time in Event Density: The Closure of Arc B and Theorem 18* (Proxmire 2026).
- *A UV-Finite Quantum Field Theory from Event-Density Primitives* (Proxmire 2026).
- *Universal Degenerate-Mobility Scaling in Crowded Soft Matter* (Proxmire 2026). The empirical anchor paper.
- McGaugh, S. S., Lelli, F., & Schombert, J. M. (2016). *Radial Acceleration Relation in Rotationally Supported Galaxies.* Phys. Rev. Lett. 117, 201101.
- McGaugh, S. S. (2012). *The Baryonic Tully–Fisher Relation of Gas-Rich Galaxies as a Test of ΛCDM and MOND.* Astron. J. 143, 40.
- Milgrom, M. (1983). *A modification of the Newtonian dynamics as a possible alternative to the hidden mass hypothesis.* Astrophys. J. 270, 365.
- Gleason, A. M. (1957). *Measures on the closed subspaces of a Hilbert space.* J. Math. Mech. 6, 885.
- Busch, P. (2003). *Quantum states and generalized observables: a simple proof of Gleason's theorem.* Phys. Rev. Lett. 91, 120403.

---

*Event Density is an open research framework being developed publicly by independent physicist Allen Proxmire. The full technical program — primitives, derivations, simulations, twenty-one forced theorems plus the ED Combination Rule, and pre-registered experimental tests across all three domains — is available at github.com/allen-proxmire, with archival DOIs through Zenodo. April 2026.*
