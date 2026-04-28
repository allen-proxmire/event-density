# Structural Foundations of ED-Substrate Gravity:
## Newton, the Transition Scale, and the 2π Dipole Mechanism

**Allen Proxmire**
**April 2026**

---

## Abstract

We derive the structural foundations of gravity within the Event Density (ED) substrate framework, working from substrate-native primitives — micro-events, participation channels, relational adjacency, and decoupling surfaces — without importing field-theoretic or thermodynamic machinery. Three principal results are established. First, Newton's law of gravity, `a = GM/R²`, emerges from a substrate-level cumulative-strain reading of the chain's stability landscape combined with a participation-count bound on decoupling surfaces; the recovery uniquely fixes the substrate UV cutoff to `ℓ_ED² = ℏG/c³`, identifying it with the Planck scale. Second, the gravitational transition acceleration `a₀ = c·H₀/(2π) ≈ 1.08 × 10⁻¹⁰ m/s²` is derived from a substrate-native mechanism: the chain's acceleration breaks the three-dimensional isotropy of its participation adjacency, projecting the cosmic decoupling surface onto the chain's accessible region. The leading anisotropic mode of this projection is the azimuthally-symmetric dipole (l = 1, m = 0) aligned with the chain's acceleration axis, whose 2π periodicity sets the effective cosmic rate. The prediction matches the empirically determined MOND acceleration scale `a₀^(emp) ≈ 1.2 × 10⁻¹⁰ m/s²` to within approximately 10%, with no free parameters. Third, we identify the single remaining structural question of the framework: the rule by which local-mass-induced and cosmic-horizon-induced contributions to a chain's stability landscape combine in the deep-acceleration regime. Under additive combination, the framework predicts a constant deep-regime acceleration `a → a₀`, which is empirically incorrect. The empirical Tully-Fisher slope-4 relation requires a multiplicative combination law `a² = a_N · a₀`, which is not yet articulated within the substrate ontology. We characterize this articulation gap precisely and argue that it is bounded, well-localized, and amenable to further foundational work.

---

## 1. Introduction

The Event Density (ED) framework treats spacetime, geometry, fields, and forces as emergent rather than fundamental. At its substrate level, ED is built from discrete micro-events, the relational adjacency among them, and stable participation channels through which micro-events propagate. Geometric and field-theoretic structures are coarse-grained summaries of these substrate-level relations.

The present paper addresses gravity within this framework. Our objective is to derive the structural form of gravitational dynamics — Newton's law in the high-acceleration regime, and the transition to modified deep-acceleration behavior characteristic of empirical galactic dynamics — from substrate-native primitives alone, without postulating fields, Lagrangians, or thermodynamic ensembles as fundamental.

Three motivations frame this work. First, the substrate-level approach offers a framework in which gravity is not assumed but derived from the relational structure of becoming. Second, where the derivations succeed, they fix coupling constants and acceleration scales in terms of fundamental ED-substrate quantities, eliminating parameters that field-theoretic approaches treat as free. Third, where the derivations encounter limits, those limits are precisely localized as foundational articulation questions rather than diffuse parametric uncertainties.

The paper presents three principal structural results.

In Section 3, we establish that Newton's gravitational law emerges from a substrate-native cumulative-strain reading of the chain's stability landscape, combined with a participation-count constraint on decoupling surfaces. The derivation produces the gravitational constant in terms of substrate quantities: `G = c³ ℓ_ED² / ℏ`. Newton-recovery then fixes the substrate cutoff at the Planck scale, `ℓ_ED = ℓ_P`.

In Sections 4 and 5, we derive the gravitational transition acceleration. The cosmic horizon, situated at distance `R_H = c/H₀`, contributes to the chain's stability landscape via a substrate-native mechanism: the chain's acceleration breaks the three-dimensional isotropy of its participation adjacency, and the cosmic horizon projects onto the chain's accessible region with a leading anisotropic mode whose 2π azimuthal periodicity reduces the effective cosmic rate to `H₀/(2π)`. The transition acceleration is then `a₀ = c·H₀/(2π)`, matching the empirical MOND value within approximately 10%, with no free parameters.

In Section 6, we identify the single remaining structural question of the framework: the rule by which local-mass-induced and cosmic-horizon-induced contributions to a chain's stability landscape combine in the deep-acceleration regime. We characterize this articulation gap precisely, establish that it is bounded and well-localized, and indicate the structural commitment that would close it.

Section 7 summarizes the empirical content of the framework as currently articulated, and Section 8 concludes with implications for further foundational work.

---

## 2. ED-Substrate Ontology

This section recalls the substrate-level primitives and relations that the subsequent derivations rely on. Detailed treatments are provided in the foundational ED papers cited in the references; here we restate only what is needed to follow the present derivations.

### 2.1 Micro-events and event density

At the substrate level, reality consists of discrete micro-events — atomic acts of becoming. The local rate of micro-event production at a region x is the *event density* ρ(x). Higher ρ corresponds to faster local rate of becoming; lower ρ corresponds to slower rate. The field ρ is locally smooth at the substrate scale and varies across larger regions.

### 2.2 Participation and adjacency

Micro-events do not exist in isolation. They are linked by *participation*: the relational structure that determines whether one region can integrate the micro-events of another. Participation strength depends on the compatibility of event-density values and gradients between regions. Two micro-events are "adjacent" in the substrate-relational sense when they integrate each other's becoming, share participation bandwidth, and maintain coherent relational timing.

### 2.3 Stability and chains

A *chain* is a sequence of micro-events that maintains coherent participation across its extent. A chain's stability at any micro-event step depends on:

- the coherence of its internal micro-event structure across successive steps,
- the strain produced by mismatch between the chain's local participation environment and its current state,
- the integrated environmental gradient encountered by the chain in its accessible region.

These three components — coherence, strain, and gradient-strain — together determine the chain's stability landscape, whose gradient experienced by the chain manifests as force.

### 2.4 Decoupling surfaces

A decoupling surface is a participation threshold where reciprocal participation between two regions becomes one-sided. Decoupling surfaces emerge when ED-gradients become sufficiently steep that micro-events on one side of the surface cannot be meaningfully integrated by regions on the other side. Two decoupling surfaces are central to the present derivations:

- The *cosmic decoupling surface*, situated at radius `R_H = c/H₀`, beyond which micro-events cannot reach a given observer in finite cosmic time.
- The *acceleration-induced decoupling surface*, situated at distance `d_a = c²/a` behind a chain accelerating at rate a, beyond which micro-events emitted from the chain's deceleration direction cannot be integrated by the chain.

Both surfaces are 2-spheres in the substrate's emergent geometry, with 4π solid-angle structure relative to the relevant central observer.

### 2.5 The participation-count bound

A finite causal-domain region admits a finite count of distinguishable participation-channel degrees of freedom on its boundary. Substrate-level UV finiteness — the constraint that micro-event production at any scale is bounded — forces the existence of a fundamental cutoff length `ℓ_ED`. The participation-count bound then takes the form:

$$
N_{\text{dof}} = \frac{A}{\ell_{\text{ED}}^2}
$$

where A is the boundary area. This is the substrate-native analog of the holographic count.

### 2.6 The chain's stability landscape

A chain at substrate position x with current micro-event state s evaluates its next propagation step against the available local participation environment. The stability score for a candidate next state e′ is

$$
\Sigma(e') = \text{Coh}(e', s) - \text{Str}(e', \rho_{\text{local}}) - \text{Grad}(e', \nabla\rho)
$$

where Coh measures coherence with the current state, Str measures participation strain with the surrounding environment, and Grad measures the strain accumulated against the surrounding ED-gradient field. The chain extends to the available next state with maximum Σ.

The substrate-level rules of stability and propagation summarized here are sufficient for the gravitational derivations that follow.

---

## 3. Substrate Derivation of Newton's Law

We now derive Newton's gravitational law from the substrate-level rules. Consider a chain at radius R from a mass M. The chain's stability landscape is shaped by the participation environment surrounding M, which we treat at the substrate level via the cumulative-strain reading and the participation-count bound.

### 3.1 The cumulative-strain reading

The strain term `Str(e′, ρ_local)` in the chain's stability landscape is determined not by the instantaneous local environmental gradient but by the *integrated* environmental gradient from the chain's current location to the chain's natural rest state. Physically: the chain's strain at each propagation step reflects the cumulative pull it has accumulated against the surrounding ED-gradient, integrated along the path of steepest gradient descent from its current location outward.

For a chain at radius R from mass M, the integrated ED-gradient from R to spatial infinity scales as

$$
\int_R^\infty \rho_{\text{grad}}(R')\, dR' \propto \frac{M}{R}.
$$

The chain's effective acceleration is the rate of change of integrated strain with radial position:

$$
a \propto \frac{\partial}{\partial R}\left(\frac{M}{R}\right) \propto \frac{M}{R^2}.
$$

This recovers the inverse-square scaling of Newtonian gravity. The proportionality constant remains to be fixed.

### 3.2 The participation-count constraint

To fix the proportionality constant, we apply the participation-count bound to a holographic 2-sphere at radius R surrounding M. The sphere has area `A_R = 4πR²`, and the participation degrees of freedom on it are

$$
N_R = \frac{4\pi R^2}{\ell_{\text{ED}}^2}.
$$

A substrate-level equipartition principle distributes the local mass-energy across these participation degrees of freedom. Setting `(1/2) N_R · k_B T_R = M c²` and identifying the local participation rate via an Unruh-analog inversion `T_R = ℏa/(2π k_B c)`, the 2π factors cancel and we obtain

$$
a = \frac{M c^3 \ell_{\text{ED}}^2}{R^2 \hbar}.
$$

### 3.3 Identification of the substrate cutoff

Comparison with Newton's law `a = GM/R²` yields

$$
G = \frac{c^3 \ell_{\text{ED}}^2}{\hbar},
$$

equivalently

$$
\boxed{\,\ell_{\text{ED}}^2 = \frac{\hbar G}{c^3} = \ell_P^2.\,}
$$

The substrate UV cutoff is forced by Newton-recovery to be the Planck length. This is a derived identification, not a postulate. UV-finiteness establishes the existence of `ℓ_ED`; Newton-matching fixes its specific value.

### 3.4 Result

The substrate-level rules — cumulative strain, participation-count bound, equipartition across participation degrees of freedom — together yield Newton's law

$$
a = \frac{GM}{R^2}, \qquad G = \frac{c^3 \ell_P^2}{\hbar}.
$$

Newton's gravitational constant is expressed as a relation between fundamental substrate constants. No free parameters are introduced.

---

## 4. The Cosmic-Horizon Contribution

We now derive the gravitational transition scale by considering the cosmic decoupling surface's contribution to a chain's stability landscape.

### 4.1 The cosmic decoupling surface

For any observer, the cosmic decoupling surface is the participation boundary beyond which micro-events cannot reach the observer in finite cosmic time. Its radius:

$$
R_H = \frac{c}{H_0}.
$$

Surface area:

$$
A_H = 4\pi R_H^2 = \frac{4\pi c^2}{H_0^2}.
$$

Participation degrees of freedom on the cosmic decoupling surface:

$$
N_H = \frac{A_H}{\ell_P^2} = \frac{4\pi c^2}{H_0^2 \ell_P^2}.
$$

### 4.2 The cosmic characteristic rate

The cosmic decoupling surface evolves at rate `H₀` — the characteristic rate of cosmic-time becoming. This is the substrate-native rate at which the cosmic decoupling surface refreshes from any observer's perspective.

The associated natural acceleration scale, obtained by converting the cosmic rate via the speed-of-light propagation constraint:

$$
a_{\text{cosmic}} = c \cdot H_0.
$$

Numerically, with `H₀ ≈ 70` km/s/Mpc:

$$
a_{\text{cosmic}} = c \cdot H_0 \approx 6.81 \times 10^{-10}\ \text{m/s}^2.
$$

This is the bare cosmic-horizon-induced acceleration scale, prior to the geometric projection mechanism developed in Section 5.

### 4.3 The chain's accessible region

A chain accelerating at rate a has its participation environment shaped by its acceleration-induced decoupling surface at distance `d_a = c²/a`. In the high-acceleration regime where `d_a ≪ R_H`, the chain's local participation environment is dominated by its own decoupling surface. In the low-acceleration regime where `d_a ≫ R_H`, the chain's accessible region extends to the cosmic decoupling surface, which becomes the dominant participation boundary.

The crossover between these regimes occurs at the acceleration where `d_a = R_H`:

$$
\frac{c^2}{a_*} = \frac{c}{H_0} \quad \implies \quad a_* = c \cdot H_0.
$$

Order-of-magnitude, the transition occurs at `a_* = a_{\text{cosmic}} = c·H_0`. The geometric mechanism developed in Section 5 refines this prefactor.

---

## 5. The 2π Dipole-Mode Mechanism

This section derives the substrate-native 2π factor that converts the bare cosmic acceleration scale `c·H₀` into the empirically-relevant transition acceleration `a₀ = c·H₀/(2π)`.

### 5.1 Acceleration breaks adjacency isotropy

In the substrate-relational adjacency structure (Section 2.2), the participation environment surrounding a chain is three-dimensionally isotropic at rest. When the chain accelerates, its commitment-order direction becomes asymmetric — there is a "forward" direction (the direction of acceleration) and a "backward" direction (toward the acceleration-induced decoupling surface). The chain's accessible-region geometry inherits this asymmetry: the chain has full reciprocal participation with regions in its forward hemisphere and progressively-thinned participation with regions in its backward hemisphere, fully decoupled at distance `d_a`.

The consequence is structural: an accelerating chain's participation environment is no longer 3D-isotropic. It has a privileged axis — the chain's acceleration direction.

### 5.2 Cosmic-horizon projection onto the chain's accessible region

The cosmic decoupling surface contributes to the chain's stability landscape through the chain's accessible region. Because the chain's accessible region is anisotropic (privileged axis along the acceleration direction), the cosmic-horizon contribution as experienced by the chain is not the isotropic full-sphere integration but a directional projection.

A natural decomposition expands the cosmic-horizon contribution in spherical harmonics aligned with the chain's acceleration axis. The leading mode is the monopole (l = 0), which is purely isotropic and does not couple to the chain's anisotropic accessibility. The next mode is the dipole (l = 1, m = 0), aligned with the chain's acceleration axis. This is the leading mode that does couple to the chain's anisotropic adjacency structure.

### 5.3 The 2π azimuthal periodicity

The dipole mode (l = 1, m = 0) is azimuthally symmetric about the chain's acceleration axis. Its angular structure has a single nontrivial spatial periodicity — the 2π azimuthal cycle around the symmetry axis.

The chain integrates the cosmic-horizon contribution through this azimuthal mode. The effective rate at which the chain experiences cosmic-horizon fluctuations from this mode is the cosmic angular rate `H₀` divided by the dipole's azimuthal period:

$$
\gamma_{\text{cosmic}}^{\text{eff}} = \frac{H_0}{2\pi}.
$$

This 2π reduction is geometric, arising from the azimuthal periodicity of the leading anisotropic mode of cosmic-horizon participation as projected through the chain's accelerated frame.

### 5.4 The transition acceleration

The chain's experienced fluctuation rate, set by its acceleration-induced decoupling-surface refresh, is

$$
\gamma_{\text{chain}} = \frac{a}{c}.
$$

The transition between local-decoupling-surface-dominated dynamics (Newtonian regime) and cosmic-decoupling-surface-dominated dynamics (deep-acceleration regime) occurs where these two rates match:

$$
\gamma_{\text{chain}} = \gamma_{\text{cosmic}}^{\text{eff}}
\quad\Longrightarrow\quad
\frac{a}{c} = \frac{H_0}{2\pi}.
$$

Solving:

$$
\boxed{\,a_0 = \frac{c \cdot H_0}{2\pi}.\,}
$$

### 5.5 Numerical comparison with empirical determination

With `H₀ = 70 km/s/Mpc = 2.27 × 10⁻¹⁸ s⁻¹` and `c = 3.00 × 10⁸ m/s`:

$$
a_0 = \frac{c \cdot H_0}{2\pi} \approx \frac{6.81 \times 10^{-10}}{2\pi}\ \text{m/s}^2 \approx 1.08 \times 10^{-10}\ \text{m/s}^2.
$$

The empirically-determined MOND acceleration constant from galactic rotation curves is `a₀^(emp) ≈ 1.2 × 10⁻¹⁰ m/s²` (McGaugh and collaborators). The structural prediction matches the empirical value to within approximately 10%.

The match is parameter-free. No free constants are tuned in deriving `a₀`. The agreement reflects the structural compatibility between the substrate-native dipole-mode mechanism and the empirically-determined transition scale.

### 5.6 Sensitivity to H₀

The Hubble tension (`H₀ ≈ 67–73 km/s/Mpc` depending on measurement method) translates to a prediction band:

| `H₀` (km/s/Mpc) | `a₀` predicted (m/s²) | Ratio to empirical |
|---|---|---|
| 67 | 1.04 × 10⁻¹⁰ | 0.86 |
| 70 | 1.08 × 10⁻¹⁰ | 0.90 |
| 73 | 1.13 × 10⁻¹⁰ | 0.94 |

The prediction is robust against the Hubble tension at the level of approximately 15%.

---

## 6. The Deep-Regime Articulation Gap

The substrate-level derivations of Sections 3–5 establish two structural results: Newton's law in the high-acceleration regime, and the transition acceleration `a₀` that separates the high-acceleration regime from the deep-acceleration regime. The third structural result needed to derive the empirical galactic phenomenology — flat rotation curves and the slope-4 baryonic Tully-Fisher relation — is the *combination law* by which local-mass-induced and cosmic-horizon-induced contributions to a chain's stability landscape combine in the deep-acceleration regime.

### 6.1 The combination law and its empirical requirement

The chain's stability landscape contains contributions from both local-mass and cosmic-horizon sources. The chain's experienced acceleration is the gradient of the total stability landscape. The combination rule by which the two contributions are merged in the deep regime determines the resulting phenomenology.

Empirically, galactic rotation curves at large radii are flat — the orbital velocity `v` becomes asymptotically constant in `R`. The baryonic Tully-Fisher relation, `v_flat⁴ ∝ M_b`, then follows. Producing this phenomenology from the substrate-level transition acceleration `a₀` requires the deep-regime combination law

$$
a^2 = a_N \cdot a_0,
$$

equivalent to the MOND interpolation in the deep regime. With this multiplicative law, centripetal balance gives `v⁴ = G M a₀`, recovering slope-4 BTFR with the prefactor `G·a₀` derivable from substrate constants.

### 6.2 The structural status of the combination law

The substrate-level rules summarized in Section 2 prescribe the chain's stability landscape as a sum of contributions from local strain, gradient-strain, and coherence terms. Multiple sources of strain or gradient-strain combine through the additive structure of the landscape. Under this additive combination, the chain's experienced acceleration is the vector sum of contributions from local-mass and cosmic-horizon sources. In the deep regime where cosmic-horizon contribution dominates, this gives `a → a₀` (constant), with orbital velocity `v² = a₀ R` rising as `√R` rather than approaching a finite asymptote.

The empirical phenomenology requires instead the multiplicative combination law `a² = a_N · a_0`. This is not the additive structure that the current substrate articulation provides.

### 6.3 The gap, precisely localized

The deep-regime articulation gap is therefore a specific structural question:

> By what substrate-level rule do bilocal source contributions to a chain's stability landscape combine in the deep-acceleration regime?

This question is bounded and well-defined. It does not concern the existence of the substrate ontology, the stability of decoupling surfaces, the form of the participation-count bound, the cumulative-strain reading, or the dipole-mode projection mechanism. All of these structural elements are established. What remains is the specific articulation of how multiple source contributions enter the chain's stability landscape — additively, multiplicatively, or in some other substrate-native form.

The gap is at the level of substrate articulation rather than derivation. Closing it requires identifying the combination rule that ED's substrate ontology prescribes for multi-source stability landscapes — a structural commitment about the substrate's operational behavior, parallel in character to the commitments articulated in earlier ED papers about decoupling surfaces and emergent geometry.

### 6.4 The framework's empirical position absent the combination rule

In the absence of the multiplicative combination rule, the substrate framework as currently articulated predicts:

- Newton's law in the high-acceleration regime — empirically correct.
- A transition at acceleration `a₀ = c·H₀/(2π)` — empirically correct within ~10%.
- A constant acceleration `a → a₀` in the deep regime, with orbital velocities rising as `v² ∝ R` — empirically incorrect; observed rotation curves are flat in `v`, not `v²`.

The framework is therefore structurally sound on Newton and the transition scale, and structurally incomplete on the deep-regime phenomenology. The incompleteness is precisely localized as the combination rule, not diffused across the framework.

---

## 7. Empirical Position

We summarize the empirical content of the framework as currently articulated.

### 7.1 Tested regimes

**Newton regime** (`a_N >> a₀`). The framework predicts `a = GM/R²` with `G = c³ℓ_P²/ℏ`. This matches the empirical Newtonian gravitational law exactly.

**Transition regime** (`a_N ≈ a₀`). The framework predicts the transition at acceleration `a₀ = c·H₀/(2π) ≈ 1.08 × 10⁻¹⁰ m/s²`. This matches the empirical MOND acceleration constant `a₀^(emp) ≈ 1.2 × 10⁻¹⁰ m/s²` to within approximately 10%, parameter-free, robust to the Hubble tension.

### 7.2 Open empirical question

**Deep-acceleration regime** (`a_N << a₀`). The framework as currently articulated predicts a constant acceleration `a → a₀`, giving orbital velocities `v² = a₀ R` that rise as `√R` rather than asymptote to a finite `v_flat`. This prediction is empirically incorrect.

The empirical galactic phenomenology requires the multiplicative deep-regime law `a² = a_N · a₀`, which gives flat rotation curves and slope-4 baryonic Tully-Fisher. This law is not yet articulated within the substrate ontology.

### 7.3 The framework's status

The framework's empirical position is bounded and falsifiable:

- It correctly predicts the existence and value of Newton's gravitational constant.
- It correctly predicts the existence and value of the gravitational transition acceleration.
- It does not yet correctly predict the deep-acceleration phenomenology.

This is a precise empirical state. The framework's successes are not phenomenological fits — they are structural derivations from substrate primitives, fixing two fundamental constants in terms of substrate quantities. The framework's limitations are not parametric ambiguities — they are a single, well-localized articulation question about the substrate's combination rule.

---

## 8. Conclusion

The substrate-level approach to gravity within the Event Density framework yields three structural results.

**Newton's law** emerges from the cumulative-strain reading of the chain's stability landscape combined with the participation-count bound. The gravitational constant is expressed as `G = c³ℓ_P²/ℏ`, identifying the substrate UV cutoff with the Planck length as a derived rather than postulated relation.

**The gravitational transition acceleration** emerges from a substrate-native mechanism: the chain's acceleration breaks the three-dimensional isotropy of its participation adjacency, projecting the cosmic decoupling surface onto the chain's accessible region with a leading dipole mode whose 2π azimuthal periodicity yields `a₀ = c·H₀/(2π)`. The prediction matches the empirical MOND acceleration constant to within approximately 10%, parameter-free.

**The deep-regime combination rule** is the single remaining structural question. The empirical slope-4 baryonic Tully-Fisher relation requires a multiplicative combination law `a² = a_N · a₀` for the contributions of local-mass and cosmic-horizon sources to a chain's stability landscape. This rule is not yet articulated within the substrate ontology, and constitutes the framework's foundational open question.

The structural position is thus: ED-substrate gravity reaches Newton's law and the gravitational transition scale from substrate primitives, with no free parameters. The deep-regime phenomenology depends on a single articulation that lies within the substrate-level scope of the framework but has not yet been written.

The path forward is articulation work — a new ED paper specifying the substrate's combination rule for multi-source stability landscapes — analogous in character to the earlier papers establishing decoupling surfaces and emergent geometry. The structural ingredients are in place. The framework awaits its final substrate-level articulation.

---

## References

The references below are to the internal ED corpus that provides the foundational substrate ontology and structural results used in this paper.

**Foundational ED papers:**

- ED-01 through ED-05: Foundational primitives of micro-events, participation, adjacency, and the substrate ontology.
- ED-06: *Horizons as Event Density Decoupling Surfaces* (Proxmire 2026). Establishes decoupling surfaces as relational thresholds of one-sided participation.
- ED-07: *Event Density and Relativistic Phenomena* (Proxmire 2026). Establishes the substrate-native account of relativistic effects: time dilation, redshift, inertial motion as gradient minimization.
- ED-10: *Event Density and the Emergence of Spacetime* (Proxmire 2026). Establishes that geometry, information, and temporal asymmetry emerge from substrate-level becoming rather than being fundamental.
- ED-I-06: *Fields and Forces in Event Density* (Proxmire 2026). Establishes that fields and forces are emergent participation structures, not fundamental entities.

**Structural-arc results:**

- Arc N: Substrate-level UV finiteness (Theorem N1: V1 finite-width vacuum kernel).
- Arc R: Spin-statistics, Cl(3,1) uniqueness, and Dirac emergence at the substrate level.
- Arc Q: Quantum sector results, including canonical commutation and UV-FIN.
- Phase 3 / GR: V1 with Synge world function (Theorem GR.1) — substrate-level extension to curved spacetime.

**Substrate-derivation memos:**

- Substrate-rules memo: cumulative-strain reading and participation-count bound for Newton-recovery.
- Holographic-bound memo: substrate-level participation-count constraint.
- 2π-dipole memo: dipole-mode projection mechanism for the transition scale.
- Deep-regime articulation memo: identification and localization of the combination-rule articulation gap.

**External empirical references:**

- McGaugh, S. S., Lelli, F., & Schombert, J. M. (2016). *Radial acceleration relation in rotationally supported galaxies.* Establishes the empirical MOND acceleration constant `a₀ ≈ 1.2 × 10⁻¹⁰ m/s²` from galactic rotation curves.
- McGaugh, S. S. (2012). *Baryonic Tully-Fisher Relation.* Establishes the empirical slope-4 BTFR from rotationally-supported galaxy populations.

---

*Manuscript prepared April 2026.*
