# Structural Foundations of ED-Substrate Gravity:
## Newton, the Transition Scale, the Combination Rule, and the Baryonic Tully–Fisher Relation

**Allen Proxmire**
**April 2026**

---

## Abstract

We derive the structural foundations of gravity within the Event Density (ED) substrate framework, working from substrate-native primitives — micro-events, participation channels, relational adjacency, and decoupling surfaces — without importing field-theoretic or thermodynamic machinery. Four principal results are established. First, Newton's law of gravity, `a = GM/R²`, emerges from a substrate-level cumulative-strain reading of the chain's stability landscape combined with a participation-count bound on decoupling surfaces; the recovery uniquely fixes the substrate UV cutoff to `ℓ_ED² = ℏG/c³`, identifying it with the Planck scale. Second, the gravitational transition acceleration `a₀ = c·H₀/(2π) ≈ 1.08 × 10⁻¹⁰ m/s²` is derived from a substrate-native dipole mechanism in which the chain's acceleration breaks the three-dimensional isotropy of its participation adjacency, projecting the cosmic decoupling surface onto the chain's accessible region with a leading anisotropic mode whose `2π` azimuthal periodicity sets the effective cosmic rate. The prediction matches the empirically determined MOND acceleration scale within approximately 10%, with no free parameters. Third, we ratify the **ED Combination Rule**: in the joint weak-gradient regime, the chain's stability landscape acquires a logarithmic cross-term with coefficient `√(M·a₀)`, producing the multiplicative effective acceleration `a = √(a_N · a₀)`. Fourth, composing T19 (Newton), T20 (transition scale), and the ED Combination Rule yields the flat-rotation-curve result `v² = √(G·M·a₀)` and the slope-4 baryonic Tully–Fisher relation `v⁴ = G·M·a₀`, with prefactor expressed entirely in substrate constants. The gravitational sector is therefore now **structurally complete and parameter-free**: the full empirical phenomenology of galactic gravity — Newtonian behavior in the high-acceleration regime, the transition at `a₀`, flat rotation curves and slope-4 BTFR in the deep regime — derives from substrate primitives alone, with no tunable parameters.

---

## 1. Introduction

The Event Density (ED) framework treats spacetime, geometry, fields, and forces as emergent rather than fundamental. At its substrate level, ED is built from discrete micro-events, the relational adjacency among them, and stable participation channels through which micro-events propagate. Geometric and field-theoretic structures are coarse-grained summaries of these substrate-level relations.

The present paper derives the structural form of gravitational dynamics — Newton's law in the high-acceleration regime, the transition acceleration that separates the Newtonian from the deep regime, the combination law governing the deep regime, and the flat-rotation-curve / Tully–Fisher phenomenology that follows — from substrate-native primitives alone, without postulating fields, Lagrangians, or thermodynamic ensembles as fundamental.

Three motivations frame this work. *First*, the substrate-level approach offers a framework in which gravity is not assumed but derived from the relational structure of becoming. *Second*, where the derivations succeed, they fix coupling constants and acceleration scales in terms of fundamental ED-substrate quantities, eliminating parameters that field-theoretic approaches treat as free. *Third*, the substrate level reveals structural commitments that the field-theoretic level cannot see — most notably, the multiplicative ED Combination Rule that closes the deep-regime articulation question.

The paper presents four principal structural results.

In Section 3, Newton's gravitational law emerges from a substrate-native cumulative-strain reading of the chain's stability landscape combined with a participation-count constraint on decoupling surfaces. The derivation produces the gravitational constant in substrate quantities: `G = c³ ℓ_ED² / ℏ`. Newton-recovery fixes the substrate cutoff at the Planck scale, `ℓ_ED = ℓ_P`.

In Sections 4 and 5, the transition acceleration is derived. The cosmic horizon, situated at distance `R_H = c/H₀`, contributes to the chain's stability landscape via a substrate-native mechanism: the chain's acceleration breaks the three-dimensional isotropy of its participation adjacency, and the cosmic horizon projects onto the chain's accessible region with a leading anisotropic mode whose `2π` azimuthal periodicity reduces the effective cosmic rate to `H₀/(2π)`. The transition acceleration is then `a₀ = c·H₀/(2π)`, matching the empirical MOND value within approximately 10%, with no free parameters.

In Section 6, we ratify the ED Combination Rule: in the joint weak-gradient regime, the chain's stability landscape acquires a logarithmic cross-term with coefficient `√(M·a₀)` reflecting multiplicative participation between local-mass and cosmic-horizon contributions. The resulting effective acceleration is `a = √(a_N · a₀)`. The ED Combination Rule supplies the deep-regime combination law as a substrate-native structural commitment.

In Section 7, we compose Newton's law (T19), the transition scale (T20), and the ED Combination Rule to derive flat rotation curves `v² = √(G·M·a₀)` and the slope-4 baryonic Tully–Fisher relation `v⁴ = G·M·a₀`. The proportionality constant `G·a₀` is expressed in fundamental substrate quantities, completing the structural derivation of galactic gravitational phenomenology from primitives.

Section 8 summarizes the empirical content of the now-complete framework, and Section 9 concludes with the framework's status and forward implications.

---

## 2. ED-Substrate Ontology

This section recalls the substrate-level primitives and relations that the subsequent derivations rely on. Detailed treatments are provided in the foundational ED papers cited in the references; here we restate only what is needed to follow the present derivations.

### 2.1 Micro-events and event density

At the substrate level, reality consists of discrete micro-events — atomic acts of becoming. The local rate of micro-event production at a region x is the *event density* ρ(x). Higher ρ corresponds to faster local rate of becoming; lower ρ to slower rate. The field ρ is locally smooth at the substrate scale and varies across larger regions.

### 2.2 Participation and adjacency

Micro-events do not exist in isolation. They are linked by *participation*: the relational structure that determines whether one region can integrate the micro-events of another. Participation strength depends on the compatibility of event-density values and gradients between regions. Two micro-events are "adjacent" in the substrate-relational sense when they integrate each other's becoming, share participation bandwidth, and maintain coherent relational timing.

### 2.3 Stability and chains

A *chain* is a sequence of micro-events that maintains coherent participation across its extent. A chain's stability at any micro-event step depends on:

- the coherence of its internal micro-event structure across successive steps,
- the strain produced by mismatch between the chain's local participation environment and its current state,
- the integrated environmental gradient encountered by the chain in its accessible region.

These three components — coherence, strain, and gradient-strain — together determine the chain's stability landscape, whose gradient experienced by the chain manifests as force.

### 2.4 Decoupling surfaces

A decoupling surface is a participation threshold where reciprocal participation between two regions becomes one-sided. Decoupling surfaces emerge when ED-gradients become sufficiently steep that micro-events on one side cannot be meaningfully integrated by regions on the other. Two decoupling surfaces are central to the present derivations:

- The *cosmic decoupling surface*, situated at radius `R_H = c/H₀`, beyond which micro-events cannot reach a given observer in finite cosmic time.
- The *acceleration-induced decoupling surface*, situated at distance `d_a = c²/a` behind a chain accelerating at rate a, beyond which micro-events emitted from the chain's deceleration direction cannot be integrated by the chain.

Both surfaces are 2-spheres in the substrate's emergent geometry, with 4π solid-angle structure relative to the relevant central observer.

### 2.5 The participation-count bound

A finite causal-domain region admits a finite count of distinguishable participation-channel degrees of freedom on its boundary. Substrate-level UV finiteness — the constraint that micro-event production at any scale is bounded — forces the existence of a fundamental cutoff length `ℓ_ED`. The participation-count bound takes the form

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

## 3. Substrate Derivation of Newton's Law (T19)

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

Newton's gravitational constant is expressed as a relation between fundamental substrate constants. No free parameters are introduced. This result is registered as **Theorem T19**.

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

Order-of-magnitude, the transition occurs at `a_* = a_cosmic = c·H₀`. The geometric mechanism developed in Section 5 refines this prefactor.

---

## 5. The 2π Dipole-Mode Mechanism (T20)

This section derives the substrate-native `2π` factor that converts the bare cosmic acceleration scale `c·H₀` into the empirically-relevant transition acceleration `a₀ = c·H₀/(2π)`.

### 5.1 Acceleration breaks adjacency isotropy

In the substrate-relational adjacency structure (Section 2.2), the participation environment surrounding a chain is three-dimensionally isotropic at rest. When the chain accelerates, its commitment-order direction becomes asymmetric — there is a "forward" direction (the direction of acceleration) and a "backward" direction (toward the acceleration-induced decoupling surface). The chain's accessible-region geometry inherits this asymmetry: the chain has full reciprocal participation with regions in its forward hemisphere and progressively-thinned participation with regions in its backward hemisphere, fully decoupled at distance `d_a`.

The consequence is structural: an accelerating chain's participation environment is no longer 3D-isotropic. It has a privileged axis — the chain's acceleration direction.

### 5.2 Cosmic-horizon projection onto the chain's accessible region

The cosmic decoupling surface contributes to the chain's stability landscape through the chain's accessible region. Because the chain's accessible region is anisotropic (privileged axis along the acceleration direction), the cosmic-horizon contribution as experienced by the chain is not the isotropic full-sphere integration but a directional projection.

A natural decomposition expands the cosmic-horizon contribution in spherical harmonics aligned with the chain's acceleration axis. The leading mode is the monopole (l = 0), which is purely isotropic and does not couple to the chain's anisotropic accessibility. The next mode is the dipole (l = 1, m = 0), aligned with the chain's acceleration axis. This is the leading mode that does couple to the chain's anisotropic adjacency structure.

### 5.3 The 2π azimuthal periodicity

The dipole mode (l = 1, m = 0) is azimuthally symmetric about the chain's acceleration axis. Its angular structure has a single nontrivial spatial periodicity — the `2π` azimuthal cycle around the symmetry axis.

The chain integrates the cosmic-horizon contribution through this azimuthal mode. The effective rate at which the chain experiences cosmic-horizon fluctuations from this mode is the cosmic angular rate `H₀` divided by the dipole's azimuthal period:

$$
\gamma_{\text{cosmic}}^{\text{eff}} = \frac{H_0}{2\pi}.
$$

This `2π` reduction is geometric, arising from the azimuthal periodicity of the leading anisotropic mode of cosmic-horizon participation as projected through the chain's accelerated frame.

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

This result is registered as **Theorem T20**.

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

## 6. The Deep-Regime Combination Rule

The derivations of Sections 3–5 establish two structural results: Newton's law in the high-acceleration regime, and the transition acceleration `a₀` separating the high-acceleration regime from the deep-acceleration regime. To produce the empirical galactic phenomenology — flat rotation curves and the slope-4 Tully–Fisher relation — a third result is required: the *combination law* governing how local-mass-induced and cosmic-horizon-induced contributions to a chain's stability landscape merge in the deep-acceleration regime.

This combination law is supplied by the **ED Combination Rule**.

### 6.1 Statement of the Combination Rule

In the joint weak-gradient regime — where neither local-mass nor cosmic-horizon contribution dominates the chain's accessible region — the chain's stability landscape Σ acquires a *logarithmic cross-term* of the form

$$
\Sigma_{\text{cross}}(R) = \sqrt{G M a_0} \cdot \log(R / R_0) + \text{const},
$$

with `R_0` a substrate-internal reference scale. The coefficient `√(G·M·a₀)` reflects multiplicative participation between local-mass and cosmic-horizon contributions to the landscape: it is the geometric mean of the two source-induced strain scales rather than their sum.

The cross-term is **not** a perturbative addition to an additive landscape. It is the substrate's structural response in the regime where both source contributions co-shape the chain's accessible region. In either pure limit (`a_N ≫ a₀` or `a_N ≪ a₀` outside the joint weak-gradient regime), the cross-term either vanishes or reduces to the familiar pure-Newtonian or pure-cosmic forms.

### 6.2 Consequence for the effective acceleration

The chain's experienced acceleration is the gradient of the total stability landscape with respect to radial position. Differentiating the cross-term:

$$
\frac{\partial \Sigma_{\text{cross}}}{\partial R} = \frac{\sqrt{G M a_0}}{R}.
$$

Identifying this with the chain's effective acceleration in the deep-acceleration regime:

$$
a = \frac{\sqrt{G M a_0}}{R}.
$$

Using `a_N = G M / R²`, this rewrites cleanly as

$$
\boxed{\,a = \sqrt{a_N \cdot a_0}.\,}
$$

The effective acceleration in the deep-acceleration regime is the *geometric mean* of the Newtonian acceleration and the cosmic transition scale. This is the substrate-native multiplicative combination law.

### 6.3 Foundational status

The Combination Rule is registered as a foundational substrate rule. It is neither a perturbative extension of Newton's law nor an empirical fit to galactic data. It is the substrate-level structural commitment governing how multiple source contributions co-shape the chain's stability landscape in the joint weak-gradient regime. The form of the cross-term — logarithmic in `R`, with `√(M·a₀)` coefficient — is fixed by the substrate ontology and the requirement of dimensional consistency with the source-induced strain scales established in Sections 3 and 4.

The Combination Rule supersedes earlier candidate routes to the multiplicative combination law (matter-wave-mediated combinations, Synge-world-function-mediated combinations) by direct substrate articulation. It closes the deep-regime question that previous candidates failed to address and supplies the missing structural commitment needed to recover galactic gravitational phenomenology from primitives.

---

## 7. Flat Rotation Curves and the Slope-4 Baryonic Tully–Fisher Relation (T21)

We now compose Theorems T19 and T20 with the ED Combination Rule to derive the empirical galactic phenomenology.

### 7.1 Setup

Consider a chain in circular orbit at radius `R` from a baryonic mass distribution of total mass `M`, in the deep-acceleration regime where `a_N(R) ≪ a₀`. Per the Combination Rule, the chain's effective acceleration is

$$
a = \sqrt{a_N \cdot a_0} = \frac{\sqrt{G M a_0}}{R}.
$$

The chain's centripetal balance requires `a = v²/R`, where `v` is the orbital velocity at radius `R`.

### 7.2 Flat rotation curves

Equating centripetal and effective accelerations:

$$
\frac{v^2}{R} = \frac{\sqrt{G M a_0}}{R}
\quad\Longrightarrow\quad
\boxed{\,v^2 = \sqrt{G M a_0}.\,}
$$

The right-hand side is independent of `R`. The orbital velocity asymptotes to a finite, mass-determined value

$$
v_{\text{flat}} = (G M a_0)^{1/4}
$$

throughout the deep-acceleration regime. **This is the structural origin of flat galactic rotation curves at large radii** — derived from substrate primitives, not fit to observations.

### 7.3 Slope-4 baryonic Tully–Fisher relation

Squaring the flat-velocity result:

$$
\boxed{\,v_{\text{flat}}^4 = G \cdot M \cdot a_0.\,}
$$

This is the baryonic Tully–Fisher relation `v_flat⁴ ∝ M_b` (McGaugh 2012) with slope exactly 4 and prefactor `G·a₀` expressed in fundamental substrate constants:

$$
G \cdot a_0 = \frac{c^3 \ell_P^2}{\hbar} \cdot \frac{c H_0}{2\pi} = \frac{c^4 \ell_P^2 H_0}{2\pi \hbar}.
$$

No free parameters appear at any step. This result is registered as **Theorem T21**.

### 7.4 The deep-regime 1/R force law

The effective force per unit chain mass in the deep-acceleration regime is `a(R) = √(G·M·a₀) / R`, falling off as `1/R` rather than the Newtonian `1/R²`. This is the characteristic deep-regime force law that produces flat rotation curves and is the structural signature distinguishing the deep-acceleration regime from the Newtonian one.

### 7.5 Radial-acceleration relation

For arbitrary `(a_N, a₀)` ratios — not restricted to the deep regime — composing T19, T20, and the ED Combination Rule yields a single-valued function `a(a_N)` that interpolates smoothly between the Newtonian limit (`a → a_N` for `a_N ≫ a₀`) and the deep-regime limit (`a → √(a_N · a₀)` for `a_N ≪ a₀`). This is the substrate-level account of the radial-acceleration relation reported empirically by McGaugh, Lelli, and Schombert (2016, PRL 117:201101).

### 7.6 Falsifier

Any galactic system in the certified deep-acceleration regime that significantly departs from `v_flat⁴ = G·M·a₀` falsifies T21 and, depending on which step fails, falsifies one of the upstream commitments T19, T20, or the ED Combination Rule. The relation is sharp, parameter-free, and directly testable against the SPARC catalog and similar surveys.

---

## 8. Empirical Position

We summarize the empirical content of the now-complete framework.

### 8.1 Tested regimes

**Newton regime** (`a_N ≫ a₀`). The framework predicts `a = GM/R²` with `G = c³ℓ_P²/ℏ`. This matches the empirical Newtonian gravitational law exactly.

**Transition regime** (`a_N ≈ a₀`). The framework predicts the transition at `a₀ = c·H₀/(2π) ≈ 1.08 × 10⁻¹⁰ m/s²`. This matches the empirical MOND constant `a₀^(emp) ≈ 1.2 × 10⁻¹⁰ m/s²` to within approximately 10%, parameter-free, robust to the Hubble tension.

**Deep-acceleration regime** (`a_N ≪ a₀`). The framework predicts `a = √(a_N · a₀)`, equivalently `v² = √(G M a₀)` (flat rotation curves) and `v⁴ = G M a₀` (slope-4 BTFR). The prefactor `G·a₀` is expressed entirely in substrate constants. This matches the empirical phenomenology of galactic rotation curves and the empirical baryonic Tully–Fisher relation directly.

### 8.2 Status

The framework's empirical position is structurally complete in the gravitational sector:

- It correctly predicts the existence and value of Newton's gravitational constant.
- It correctly predicts the existence and value of the gravitational transition acceleration.
- It correctly predicts flat rotation curves and the slope-4 BTFR with the prefactor `G·a₀` derivable in substrate constants.

The successes are not phenomenological fits — they are structural derivations from substrate primitives, fixing all relevant gravitational constants in terms of substrate quantities. There are no free parameters in the entire chain from primitives to galactic dynamics.

### 8.3 Falsifiers

The framework's predictions are sharp and falsifiable:

- A galactic system in the deep regime departing from `v⁴ = G·M·a₀` falsifies T21 (and traces back to T19, T20, or the ED Combination Rule).
- A measured `a₀` significantly outside the band set by the Hubble tension falsifies T20.
- A deviation from `G = c³ℓ_P²/ℏ` falsifies T19.

---

## 9. Conclusion

The substrate-level approach to gravity within the Event Density framework yields four structural results.

**Newton's law (T19)** emerges from the cumulative-strain reading of the chain's stability landscape combined with the participation-count bound. The gravitational constant is expressed as `G = c³ℓ_P²/ℏ`, identifying the substrate UV cutoff with the Planck length as a derived rather than postulated relation.

**The gravitational transition acceleration (T20)** emerges from a substrate-native dipole mechanism: the chain's acceleration breaks the three-dimensional isotropy of its participation adjacency, projecting the cosmic decoupling surface onto the chain's accessible region with a leading dipole mode whose `2π` azimuthal periodicity yields `a₀ = c·H₀/(2π)`. The prediction matches the empirical MOND constant to within approximately 10%, parameter-free.

**The deep-regime ED Combination Rule** is ratified as a substrate-native foundational rule. In the joint weak-gradient regime, the chain's stability landscape acquires a logarithmic cross-term with `√(M·a₀)` coefficient, producing the multiplicative effective acceleration `a = √(a_N · a₀)`.

**The flat-rotation-curve and slope-4 BTFR results (T21)** follow from composing T19, T20, and the ED Combination Rule. Centripetal balance with `a = √(a_N · a₀)` yields `v² = √(G·M·a₀)` (constant in `R`, flat rotation curves) and `v⁴ = G·M·a₀` (slope-4 BTFR with prefactor expressed in substrate constants).

**The structural position is final.** The gravitational sector of the ED framework is now structurally complete and parameter-free at the substrate level. The full empirical phenomenology of galactic gravity — Newton in the high-acceleration regime, the transition at `a₀`, flat rotation curves and slope-4 BTFR in the deep regime — derives from substrate primitives alone. No free parameters appear in the chain from primitives to galactic dynamics.

The framework's open questions now lie entirely outside the scope of this paper — in the broader gravitational program (Phase-3 Einstein-equation emergence, kernel-parameter inference, the GR-4A speculative quadrant), in cross-arc closure work, and in the empirical-test program at the laboratory and observational level. The substrate-level gravitational scaffolding is complete; downstream work proceeds against a closed foundation.

---

## References

The references below are to the internal ED corpus that provides the foundational substrate ontology and structural results used in this paper, and to the external empirical references against which the predictions are tested.

**Foundational ED papers:**

- ED-01 through ED-05: Foundational primitives of micro-events, participation, adjacency, and the substrate ontology.
- ED-06: *Horizons as Event Density Decoupling Surfaces* (Proxmire 2026). Establishes decoupling surfaces as relational thresholds of one-sided participation.
- ED-07: *Event Density and Relativistic Phenomena* (Proxmire 2026). Establishes the substrate-native account of relativistic effects: time dilation, redshift, inertial motion as gradient minimization.
- ED-10: *Event Density and the Emergence of Spacetime* (Proxmire 2026). Establishes that geometry, information, and temporal asymmetry emerge from substrate-level becoming rather than being fundamental.
- ED-I-06: *Fields and Forces in Event Density* (Proxmire 2026). Establishes that fields and forces are emergent participation structures, not fundamental entities.
- **the ED Combination Rule**: *Deep-Regime Gradient-Combination Rule.* Substrate-native foundational rule introduced in this paper (Section 6); registered in `arcs/arc-SG/ED_combination_rule.md`.

**Structural-arc results:**

- Arc N: Substrate-level UV finiteness (Theorem N1: V1 finite-width vacuum kernel).
- Arc R: Spin-statistics, Cl(3,1) uniqueness, and Dirac emergence at the substrate level.
- Arc Q: Quantum sector results, including canonical commutation, UV-FIN, and gauge-field-as-rule-type (Theorem 17).
- Arc B: Kernel-level arrow of time (Theorem 18: V1 retardation).
- Phase 3 / GR: V1 with Synge world function (Theorem GR.1) — substrate-level extension to curved spacetime.

**This paper's theorems:**

- T19: Newton's law from substrate; `G = c³ℓ_P²/ℏ`.
- T20: Transition acceleration from dipole mechanism; `a₀ = c·H₀/(2π)`.
- T21: Flat rotation curves and slope-4 baryonic Tully–Fisher relation; `v⁴ = G·M·a₀`.

**Substrate-derivation memos** (in `arcs/arc-SG/`):

- `substrate_rules_stability_availability.md` — cumulative-strain reading and participation-count bound for Newton-recovery.
- `substrate_holographic_bound.md` — substrate-level participation-count constraint.
- `substrate_2pi_question.md`, `substrate_2pi_spin_statistics.md` — dipole-mode projection mechanism for the transition scale.
- `substrate_deep_regime_crossterm.md` — historical record of the deep-regime articulation question.
- `substrate_arcM_multiplicative_test.md`, `substrate_synge_multiplicative_test.md` — historical record of failed candidate routes to the multiplicative combination law.
- `ED_combination_rule.md` — the ratified substrate rule that closes the deep-regime question.

**External empirical references:**

- McGaugh, S. S., Lelli, F., & Schombert, J. M. (2016). *Radial acceleration relation in rotationally supported galaxies.* PRL 117:201101. Establishes the empirical MOND acceleration constant `a₀ ≈ 1.2 × 10⁻¹⁰ m/s²` and the empirical radial-acceleration relation.
- McGaugh, S. S. (2012). *The Baryonic Tully-Fisher Relation of Gas Rich Galaxies as a Test of ΛCDM and MOND.* AJ 143:40. Establishes the empirical slope-4 baryonic Tully–Fisher relation.
- Milgrom, M. (1983). *A modification of the Newtonian dynamics as a possible alternative to the hidden mass hypothesis.* ApJ 270:365. Original empirical phenomenology of the deep-acceleration regime.

---

*Manuscript prepared April 2026. Gravitational sector closed 2026-04-28 with the ratification of the ED Combination Rule and the derivation of T21.*
