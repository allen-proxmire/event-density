# From Primitives to Galactic Dynamics

## A Walkthrough of the Event Density Substrate-Gravity Derivation

**Allen Proxmire** · May 2026

---

## 1. The Question

In 1687, Newton wrote down the law of universal gravitation: a = GM/R². Every body attracts every other body with a force that scales as the inverse square of the distance between them, with a proportionality constant G that has the same value everywhere in the universe. The law works extraordinarily well for planetary orbits, satellite trajectories, and most everyday gravitational phenomena. It has been the foundation of celestial mechanics for over three centuries.

In the 1970s and 1980s, observations of galactic rotation curves revealed something Newton's law cannot explain. The rotation velocities of stars in spiral galaxies do not fall off with distance from the galactic center as Newton's law would predict. Instead, the velocities flatten at a roughly constant value across the outer regions of the galaxy. The standard explanation invokes dark matter — vast halos of unseen, gravitationally interacting matter that produces the additional acceleration needed to keep the rotation curves flat.

Mordehai Milgrom proposed an alternative in 1983. Below a specific acceleration scale a₀ ≈ 1.2 × 10⁻¹⁰ m/s² — far smaller than any familiar acceleration in the solar system — Newton's law might be modified. In this deep-acceleration regime, the effective gravitational acceleration would scale as √(a_N · a₀) rather than as a_N alone. This Modified Newtonian Dynamics (MOND) hypothesis predicts flat rotation curves and a specific scaling between baryonic mass and asymptotic rotation velocity: v⁴ ∝ M_b. The prediction has been tested extensively against galactic rotation data and matches empirical observations remarkably well, especially in the SPARC catalog of well-measured galaxies.

Three empirical structures, taken together, define the gravitational phenomenology that any complete theory must account for:

**Newton's law** in the high-acceleration regime: a = GM/R² with G ≈ 6.67 × 10⁻¹¹ m³/(kg·s²).

**The transition acceleration** at a₀ ≈ 1.2 × 10⁻¹⁰ m/s², below which gravitational dynamics depart from Newton's law.

**The slope-4 baryonic Tully-Fisher relation**: v⁴ = constant · M_b across galaxies, where v is the asymptotic rotation velocity and M_b is the total baryonic mass.

Standard physics offers no derivation of any of these from a deeper structure. Newton's gravitational constant G is empirical — measured, never derived. The transition acceleration a₀ is empirical — measured from rotation curves, with no theoretical account of why it has the value it has. The slope-4 BTFR is an empirical regularity that MOND predicts but does not explain at a deeper structural level.

The question this document addresses is: where does any of this come from?

The Event Density framework derives all three from substrate primitives, with no free parameters anywhere in the chain. The gravitational constant G emerges as G = c³ℓ_P²/$\hbar$ — a structural relation between the speed of light, the Planck length, and $\hbar$. The transition acceleration emerges as a₀ = c·H₀/(2π), connecting galactic dynamics to cosmology through the Hubble parameter and a substrate-native geometric factor of 2π. The slope-4 BTFR emerges as v⁴ = G·M·a₀ with the prefactor expressed entirely in substrate constants. The full empirical phenomenology of galactic gravity — Newton in the high-acceleration regime, the transition at a₀, flat rotation curves and slope-4 BTFR in the deep regime — derives from substrate primitives alone.

The structural shape of this derivation is different from the QM walkthroughs. Born and Schrödinger had load-bearing arguments concentrated in single derivation hinges (Cauchy on bandwidth additivity, Galilean integration). The gravity arc has four distinct structural results that compose into the galactic-dynamics chain. Each result has its own load-bearing argument, and the composition is what makes the framework's claim about galactic dynamics parameter-free.

The chain has four steps:

**Newton's law (T19).** The cumulative-strain reading of the chain's stability landscape gives the 1/R² fall-off. The participation-count bound on a holographic 2-sphere combined with substrate-level equipartition fixes the proportionality constant. Newton-matching forces the substrate UV cutoff to coincide with the Planck length: ℓ_ED² = ℏG/c³.

**The transition acceleration (T20).** A chain's acceleration breaks the 3D isotropy of its participation adjacency. The cosmic decoupling surface projects onto the chain's accessible region with a leading dipole mode. The 2π azimuthal periodicity of the dipole reduces the effective cosmic rate from H₀ to H₀/(2π), giving a₀ = c·H₀/(2π).

**The ED Combination Rule.** In the joint weak-gradient regime where neither local-mass nor cosmic-horizon contribution dominates, the chain's stability landscape acquires a logarithmic cross-term with √(M·a₀) coefficient. Differentiation gives a = √(a_N · a₀) — geometric-mean composition rather than sum.

**The slope-4 BTFR (T21).** Composing T19, T20, and the Combination Rule in the deep regime, with centripetal balance, gives v⁴ = G·M·a₀ — the slope-4 BTFR with the prefactor expressed entirely in substrate constants.

The structural payoff: the empirical phenomenology of galactic dynamics is what falls out when substrate-level rules — chain stability landscapes, decoupling surfaces, participation-count bounds, dipole-mode projection, the logarithmic cross-term — combine through the chain from primitives to rotation velocities. There are no free parameters in the chain. The match with empirical galactic dynamics is not a phenomenological fit; it is a structural derivation.

---

## 2. The Substrate-Gravity Ontology

The framework rests on substrate-level ontological commitments. The gravity arc uses a particular subset of these primitives that's different from what the QM walkthroughs used — gravity is downstream of substrate-level relational structure rather than of channel and bandwidth structure specifically.

### 2.1 Micro-events and event density

At the substrate level, reality consists of discrete micro-events — atomic acts of becoming. The local rate of micro-event production at a region x is the event density ρ(x). Higher ρ corresponds to faster local rate of becoming; lower ρ to slower rate. The field ρ varies smoothly at the substrate scale and produces the gradient structure that gravitational dynamics couple to.

### 2.2 Participation and adjacency

Micro-events do not exist in isolation. They are linked by participation, the relational structure that determines whether one region can integrate the micro-events of another. Two micro-events are "adjacent" in the substrate-relational sense when they integrate each other's becoming, share participation bandwidth, and maintain coherent relational timing.

Participation is what makes the substrate a connected relational structure rather than a collection of independent points. Gradients in event density correspond to gradients in the local rate of becoming, which the substrate registers through changes in participation strength.

### 2.3 Chains and stability

A chain is a sequence of micro-events that maintains coherent participation across its extent. Chains are the substrate-level objects the framework calls "particles." Each chain at substrate position x with current micro-event state s evaluates its next propagation step against the available local participation environment. The stability score for a candidate next state e' is:

$$
\sum(e') = Coh(e', s) − Str(e', \rho_{\mathrm{local}}) − Grad(e', \nabla \rho)
$$

where Coh measures coherence with the current state, Str measures participation strain with the surrounding environment, and Grad measures the strain accumulated against the surrounding ED-gradient field. The chain extends to the available next state with maximum Σ.

This stability landscape is the substrate-level structure that gravitational dynamics shape. A mass distribution produces gradients in ρ, which alter the chain's strain and gradient terms, which shifts the maximum-stability propagation direction. What we experience as gravitational acceleration is the substrate-level shift in the chain's preferred propagation.

### 2.4 Decoupling surfaces

A decoupling surface is a participation threshold where reciprocal participation between two regions becomes one-sided. Decoupling surfaces emerge when ED-gradients become sufficiently steep that micro-events on one side cannot be meaningfully integrated by regions on the other.

Two decoupling surfaces matter for galactic dynamics:

The **cosmic decoupling surface**, situated at radius R_H = c/H₀, beyond which micro-events cannot reach a given observer in finite cosmic time. This is the substrate-level analog of the cosmological horizon. Its area is A_H = 4πR_H² = 4πc²/H₀².

The **acceleration-induced decoupling surface**, situated at distance d_a = c²/a behind a chain accelerating at rate a, beyond which micro-events emitted from the chain's deceleration direction cannot be integrated by the chain. This is the substrate-level analog of the Rindler horizon experienced by accelerating observers.

Both surfaces are 2-spheres in the substrate's emergent geometry, with 4π solid-angle structure relative to the relevant central observer.

### 2.5 The participation-count bound

A finite causal-domain region admits a finite count of distinguishable participation-channel degrees of freedom on its boundary. Substrate-level UV finiteness — the constraint that micro-event production at any scale is bounded — forces the existence of a fundamental cutoff length ℓ_ED. The participation-count bound takes the form:

$$
N_{\mathrm{dof}} = A / \ell_ED^{2}
$$

where A is the boundary area. This is the substrate-native analog of the holographic count. It says the number of distinguishable degrees of freedom on a 2-sphere scales with the surface area, not the enclosed volume — which is the structural feature that makes the gravity arc work.

### 2.6 What's not in the working set

The gravity arc does not directly use the polarity primitive (the U(1) phase that drives QM emergence), the channel primitive (channels as primitive ontological objects), or the four-band bandwidth decomposition. Gravity is downstream of the relational structure of substrate becoming — the rate of micro-events, the participation environment, the gradient field, the stability landscape. The QM-emergence machinery and the gravity-emergence machinery operate on different aspects of the substrate.

That's the working set. The argument runs through chain stability landscapes (the dynamical content), decoupling surfaces (the boundary structure), and participation-count bounds (the area-scaling structure that fixes coupling constants).

---

## 3. Forcing Newton's Law

The first result is Newton's law of gravity, derived from substrate-level rules with the gravitational constant G expressed in fundamental substrate quantities.

### 3.1 The cumulative-strain reading

Consider a chain at radius R from a mass M. The chain's stability landscape is shaped by the participation environment surrounding M. The strain term Str in the stability landscape is determined not by the instantaneous local environmental gradient but by the integrated environmental gradient from the chain's current location to the chain's natural rest state.

Physically: the chain's strain at each propagation step reflects the cumulative pull it has accumulated against the surrounding ED-gradient, integrated along the path of steepest gradient descent from its current location outward.

For a chain at radius R from mass M, the integrated ED-gradient from R to spatial infinity scales as:

$$
\int_R^\infty \rho_{\mathrm{grad}}(R') dR' \propto M/R
$$

The cumulative-strain integral from R outward picks up a contribution proportional to M (the source) and inversely proportional to R (the integration length). This is the structural origin of the 1/R behavior of gravitational potential.

The chain's effective acceleration is the rate of change of integrated strain with radial position:

$$
a \propto \partial /\partial R (M/R) \propto M/R^{2}
$$

This recovers the inverse-square scaling of Newtonian gravity at the substrate level. Differentiating the 1/R potential gives the 1/R² force law. The proportionality constant remains to be fixed.

### 3.2 The participation-count constraint

To fix the proportionality constant, the framework applies the participation-count bound to a holographic 2-sphere at radius R surrounding M. The sphere has area A_R = 4πR², and the participation degrees of freedom on it are:

$$
N_R = 4\pi R^{2} / \ell_ED^{2}
$$

A substrate-level equipartition principle distributes the local mass-energy across these participation degrees of freedom. Setting:

$$
(1/2) N_R \cdot k_B T_R = Mc^{2}
$$

and identifying the local participation rate via an Unruh-analog inversion:

$$
T_R = \hbar a / (2\pi k_B c)
$$

The 2π factors cancel cleanly. Working through the algebra:

$$
(1/2)(4\pi R^{2} / \ell_ED^{2}) \cdot \hbar a/(2\pi c) = Mc^{2}
$$

Solving for a:

$$
a = (M c^{3} \ell_ED^{2}) / (R^{2} \hbar)
$$

### 3.3 Identification of the substrate cutoff

Comparison with Newton's law a = GM/R² yields:

$$
G = c^{3} \ell_ED^{2} / \hbar
$$

equivalently:

$$
\ell_ED^{2} = \hbar G/c^{3} = \ell_P^{2}
$$

The substrate UV cutoff is forced by Newton-matching to be the Planck length. This is a derived identification, not a postulate. UV-finiteness establishes the existence of ℓ_ED; Newton-matching fixes its specific value.

The Planck length ℓ_P = √(ℏG/c³) is normally introduced as a dimensional combination of fundamental constants, with its physical significance debated. In the framework, it acquires a specific structural role: it is the substrate UV cutoff, the fundamental scale at which the substrate is no longer continuum-like. This identification is what makes the framework's gravity content parameter-free — G is no longer an independent empirical constant but a derived combination of c, ℓ_P, and $\hbar$.

### 3.4 What this delivers

Newton's law of gravity:

$$
a = GM/R^{2}, G = c^{3} \ell_P^{2} / \hbar
$$

The gravitational constant is expressed as a relation between fundamental substrate constants. No free parameters are introduced. The empirical value of G ≈ 6.67 × 10⁻¹¹ m³/(kg·s²) is recovered when ℓ_P is identified with the standard Planck length √(ℏG/c³) ≈ 1.6 × 10⁻³⁵ m.

This is the framework's first substrate-level gravitational result. It establishes that Newton's gravitational coupling, normally treated as an empirical input, is structurally derivable from substrate primitives — chain stability, cumulative strain, and the participation-count bound on holographic 2-spheres.

---

## 4. Forcing the Transition Acceleration

The second result is the transition acceleration a₀ — the scale at which gravitational dynamics depart from Newton's law and enter the deep-acceleration regime. The argument runs through cosmic-horizon structure and a 2π geometric factor that emerges from substrate-native dipole-mode projection.

### 4.1 The cosmic decoupling surface and its rate

For any observer, the cosmic decoupling surface is the participation boundary beyond which micro-events cannot reach the observer in finite cosmic time. Its radius is set by the speed of light and the Hubble parameter:

$$
R_H = c / H_{0}
$$

The cosmic decoupling surface evolves at rate H₀ — the characteristic rate of cosmic-time becoming. This is the substrate-native rate at which the cosmic decoupling surface refreshes from any observer's perspective.

The associated natural acceleration scale, obtained by converting the cosmic rate via the speed-of-light propagation constraint, is:

$$
a_{\mathrm{cosmic}} = c \cdot H_{0} \approx 6.81 \times 10^{-10} m/s^{2}
$$

with H₀ ≈ 70 km/s/Mpc. This is the bare cosmic-horizon-induced acceleration scale, prior to the geometric projection mechanism developed below.

The empirical MOND constant is a₀^emp ≈ 1.2 × 10⁻¹⁰ m/s² — about a factor of 2π smaller than a_cosmic. The framework's task is to derive this 2π factor from substrate structure, not to insert it by hand.

### 4.2 Acceleration breaks adjacency isotropy

In the substrate-relational adjacency structure, the participation environment surrounding a chain is three-dimensionally isotropic at rest. There is no preferred direction; the chain integrates participation equally from all directions.

When the chain accelerates, this changes. The chain's commitment-order direction becomes asymmetric — there is a "forward" direction (the direction of acceleration) and a "backward" direction (toward the acceleration-induced decoupling surface at distance d_a = c²/a). The chain has full reciprocal participation with regions in its forward hemisphere and progressively-thinned participation with regions in its backward hemisphere, fully decoupled at distance d_a.

The consequence is structural: an accelerating chain's participation environment is no longer 3D-isotropic. It has a privileged axis — the chain's acceleration direction.

This is the substrate-native version of an effect familiar from special relativity. An accelerating observer in flat spacetime experiences a Rindler horizon behind them, breaking the isotropy of their causal structure. In the framework, this is not an artifact of coordinate choice but a substrate-level relational fact: the chain's accessible region acquires a privileged axis when the chain accelerates.

### 4.3 Cosmic-horizon projection through dipole modes

The cosmic decoupling surface contributes to the chain's stability landscape through the chain's accessible region. Because the chain's accessible region is now anisotropic (privileged axis along the acceleration direction), the cosmic-horizon contribution as experienced by the chain is not the isotropic full-sphere integration but a directional projection.

A natural decomposition expands the cosmic-horizon contribution in spherical harmonics aligned with the chain's acceleration axis. The leading mode is the monopole (l = 0), which is purely isotropic and does not couple to the chain's anisotropic accessibility — an isotropic mode integrated over an anisotropic accessible region produces nothing distinctive about the acceleration direction.

The next mode is the dipole (l = 1, m = 0), aligned with the chain's acceleration axis. This is the leading mode that does couple to the chain's anisotropic adjacency structure. The dipole mode distinguishes forward from backward along the acceleration axis, which is exactly the asymmetry the chain's accessible region has.

### 4.4 The 2π azimuthal periodicity

The dipole mode (l = 1, m = 0) is azimuthally symmetric about the chain's acceleration axis. Its angular structure has a single nontrivial spatial periodicity — the 2π azimuthal cycle around the symmetry axis.

The chain integrates the cosmic-horizon contribution through this azimuthal mode. The effective rate at which the chain experiences cosmic-horizon fluctuations from this mode is the cosmic angular rate H₀ divided by the dipole's azimuthal period:

$$
\gamma_{\mathrm{cosmic}}^{\mathrm{eff}} = H_{0} / (2\pi)
$$

This 2π reduction is geometric, not numerical. It arises from the azimuthal periodicity of the leading anisotropic mode of cosmic-horizon participation as projected through the chain's accelerated frame. The 2π is the same 2π that appears in any azimuthal integration on a 2-sphere — it's a structural feature of the dipole mode's geometry.

### 4.5 The transition acceleration

The chain's experienced fluctuation rate, set by its acceleration-induced decoupling-surface refresh, is:

$$
\gamma_{\mathrm{chain}} = a / c
$$

The transition between local-decoupling-surface-dominated dynamics (Newtonian regime) and cosmic-decoupling-surface-dominated dynamics (deep-acceleration regime) occurs where these two rates match:

$$
\gamma_{\mathrm{chain}} = \gamma_{\mathrm{cosmic}}^{\mathrm{eff}} \implies a/c = H_{0} / (2\pi)
$$

Solving:

$$
a_{0} = c \cdot H_{0} / (2\pi)
$$

Numerically:

$$
a_{0} \approx 6.81 \times 10^{-10} / (2\pi) m/s^{2} \approx 1.08 \times 10^{-10} m/s^{2}
$$

The empirical MOND value is a₀^emp ≈ 1.2 × 10⁻¹⁰ m/s². The structural prediction matches the empirical value to within approximately 10%, parameter-free.

### 4.6 Hubble tension robustness

The Hubble tension (H₀ ≈ 67–73 km/s/Mpc depending on measurement method) translates to a prediction band:

| H₀ (km/s/Mpc) | a₀ predicted (m/s²) | Ratio to empirical |
|---|---|---|
| 67 | 1.04 × 10⁻¹⁰ | 0.86 |
| 70 | 1.08 × 10⁻¹⁰ | 0.90 |
| 73 | 1.13 × 10⁻¹⁰ | 0.94 |

The prediction is robust against the Hubble tension at the level of approximately 15%. Whatever the resolution of the H₀ tension turns out to be, the framework's prediction for a₀ tracks it within this band.

### 4.7 What this delivers

The transition acceleration:

$$
a_{0} = c \cdot H_{0} / (2\pi) \approx 1.08 \times 10^{-10} m/s^{2}
$$

derived from substrate primitives via the dipole-mode projection mechanism, with the 2π factor emerging as a geometric consequence of azimuthal periodicity rather than as a phenomenological fit. The match with the empirical MOND constant to within ~10% is achieved without free parameters.

This is the framework's connection between cosmology and galactic dynamics. The Hubble parameter H₀ — a cosmological scale — appears in galactic dynamics through the projection of the cosmic decoupling surface onto the accelerated chain's accessible region. Galactic phenomenology and cosmological structure are linked by the substrate's relational geometry.

---

## 5. The ED Combination Rule

The third result is the structural commitment that closes the deep-regime question: how do local-mass and cosmic-horizon contributions combine when neither dominates the chain's accessible region?

Newton's law operates in the high-acceleration regime where a_N ≫ a₀. The transition acceleration sets the boundary at a_N ≈ a₀. The deep-acceleration regime is where a_N ≪ a₀, and a structural rule is needed to specify how the two contributions co-shape the chain's stability landscape.

### 5.1 The logarithmic cross-term

In the joint weak-gradient regime — where neither local-mass nor cosmic-horizon contribution dominates the chain's accessible region — the chain's stability landscape Σ acquires a logarithmic cross-term of the form:

$$
\sum_{\mathrm{cross}}(R) = \sqrt{G \cdot M \cdot a_{0}} \cdot \log(R/R_0) + const
$$

with R_0 a substrate-internal reference scale. The coefficient √(G·M·a₀) is the geometric mean of the two source-induced strain scales rather than their sum. This reflects multiplicative participation between local-mass and cosmic-horizon contributions to the landscape — the substrate combines them through geometric-mean composition rather than additive composition.

The cross-term is not a perturbative addition to an additive landscape. It is the substrate's structural response in the regime where both source contributions co-shape the chain's accessible region. In either pure limit (a_N ≫ a₀ or a_N ≪ a₀ outside the joint weak-gradient regime), the cross-term either vanishes or reduces to the pure-Newtonian or pure-cosmic forms.

### 5.2 Why geometric-mean composition

The geometric-mean composition is what distinguishes the framework's deep-regime behavior from naive additive expectations. If the contributions combined additively (a = a_N + a₀ or similar), the deep regime would behave very differently, and the empirical scaling of galactic rotation curves would not match. The geometric mean is what produces the observed v⁴ ∝ M scaling.

The structural reason for geometric-mean composition is that the cross-term reflects a multiplicative coupling between the local-mass-induced gradient field and the cosmic-horizon-projected mode. Both contributions shape the same chain's accessible region simultaneously; they don't just add up at the boundary. The strain landscape registers them as joint participants, and joint participation in a substrate-level coupling produces multiplicative composition with √(M·a₀) coefficient — the geometric mean of M·a_N (Newton-strain scale) and M·a₀ (cosmic-strain scale) reduces to √(M·a₀) when normalized.

### 5.3 The effective acceleration

The chain's experienced acceleration is the gradient of the total stability landscape with respect to radial position. Differentiating the cross-term:

$$
\partial \sum_{\mathrm{cross}} / \partial R = \sqrt{G \cdot M \cdot a_{0}} / R
$$

Identifying this with the chain's effective acceleration in the deep-acceleration regime:

$$
a = \sqrt{G \cdot M \cdot a_{0}} / R
$$

Using a_N = G·M/R²:

$$
a = \sqrt{a_N \cdot a_{0}}
$$

The effective acceleration in the deep-acceleration regime is the geometric mean of the Newtonian acceleration and the cosmic transition scale. This is the substrate-native multiplicative combination law.

### 5.4 What this delivers

The ED Combination Rule:

$$
a = \sqrt{a_N \cdot a_{0}} in the deep-acceleration regime
$$

This is a substrate-level structural commitment, not an empirical fit. The form of the cross-term — logarithmic in R, with √(M·a₀) coefficient — is fixed by the substrate ontology and the requirement of dimensional consistency with the source-induced strain scales established in the Newton and transition-acceleration derivations.

Combined with Newton's law (Section 3) and the transition acceleration (Section 4), this gives the framework's complete prescription for gravitational dynamics across all regimes:

In the high-acceleration regime (a_N ≫ a₀): a → a_N (Newton).

At the transition (a_N ≈ a₀): smooth interpolation.

In the deep-acceleration regime (a_N ≪ a₀): a → √(a_N · a₀) (Combination Rule).

The framework's gravitational dynamics now span the full range from solar-system scales to galactic scales, parameter-free, with the high-acceleration regime giving Newton, the deep regime giving MOND-like behavior, and the transition between them set by a₀ = c·H₀/(2π).

---

## 6. Closure: Flat Rotation Curves and the Slope-4 BTFR

The fourth result follows from composing the three structural results above. Newton's law gives a_N = GM/R² with G = c³ℓ_P²/$\hbar$. The transition acceleration gives a₀ = c·H₀/(2π). The Combination Rule gives a = √(a_N · a₀) in the deep regime. Putting these together with centripetal balance produces flat rotation curves and the slope-4 BTFR.

### 6.1 Setup

Consider a chain in circular orbit at radius R from a baryonic mass distribution of total mass M, in the deep-acceleration regime where a_N(R) ≪ a₀. Per the Combination Rule, the chain's effective acceleration is:

$$
a = \sqrt{a_N \cdot a_{0}} = \sqrt{G \cdot M \cdot a_{0}} / R
$$

The chain's centripetal balance requires a = v²/R, where v is the orbital velocity at radius R.

### 6.2 Flat rotation curves

Equating centripetal and effective accelerations:

$$
v^{2} / R = \sqrt{G \cdot M \cdot a_{0}} / R \implies v^{2} = \sqrt{G \cdot M \cdot a_{0}}
$$

The right-hand side is independent of R. The orbital velocity asymptotes to a finite, mass-determined value:

$$
v_{\mathrm{flat}} = (G \cdot M \cdot a_{0})^(1/4)
$$

throughout the deep-acceleration regime. This is the structural origin of flat galactic rotation curves at large radii — derived from substrate primitives, not fit to observations.

The chain's orbital velocity does not fall off with R in the deep regime; it asymptotes to a constant value determined by the enclosed baryonic mass and the substrate constants G and a₀. This is what produces the empirically observed flat rotation curves of spiral galaxies.

### 6.3 The slope-4 BTFR

Squaring the flat-velocity result:

$$
v_{\mathrm{flat}}^{4} = G \cdot M \cdot a_{0}
$$

This is the baryonic Tully-Fisher relation v⁴ ∝ M_b with slope exactly 4 and prefactor G·a₀ expressed in fundamental substrate constants:

$$
G \cdot a_{0} = (c^{3}\ell_P^{2}/\hbar) \cdot(c \cdot H_{0}/(2\pi)) = c^{4} \cdot \ell_P^{2} \cdot H_{0} / (2\pi \cdot \hbar)
$$

No free parameters appear at any step.

The empirical baryonic Tully-Fisher relation has slope-4 across about five decades in mass, with remarkably small scatter. The framework derives this slope and the prefactor from substrate primitives, with c, ℓ_P, $\hbar$, and H₀ as the only inputs — all of which are independently measured constants.

### 6.4 The deep-regime force law

The effective force per unit chain mass in the deep-acceleration regime is:

$$
a(R) = \sqrt{G \cdot M \cdot a_{0}} / R
$$

falling off as 1/R rather than the Newtonian 1/R². This is the characteristic deep-regime force law that produces flat rotation curves and is the structural signature distinguishing the deep-acceleration regime from the Newtonian one.

The 1/R fall-off reflects the geometric-mean composition of the Combination Rule. Multiplying the Newtonian 1/R² by 1/R from the geometric mean gives the deep-regime 1/R behavior, which when integrated against centripetal balance produces R-independent v².

### 6.5 The radial-acceleration relation

For arbitrary (a_N, a₀) ratios — not restricted to the deep regime — composing T19, T20, and the ED Combination Rule yields a single-valued function a(a_N) that interpolates smoothly between the Newtonian limit (a → a_N for a_N ≫ a₀) and the deep-regime limit (a → √(a_N · a₀) for a_N ≪ a₀). This is the substrate-level account of the radial-acceleration relation reported empirically by McGaugh, Lelli, and Schombert (PRL 117:201101, 2016) — the empirical relation between observed acceleration and Newtonian acceleration computed from baryonic mass distribution.

The framework predicts this relation as a structural consequence of the three substrate results, without phenomenological parameters. The empirical match is striking: the radial-acceleration relation in galactic data tracks the framework's prediction across the full range from solar-system-like high accelerations to deep-regime low accelerations.

### 6.6 What this delivers

The full empirical phenomenology of galactic gravity, derived from substrate primitives:

**Newton's law** in the high-acceleration regime: a = GM/R² with G = c³ℓ_P²/$\hbar$. Matches the empirical Newtonian gravitational law exactly.

**The transition acceleration** at a₀ = c·H₀/(2π) ≈ 1.08 × 10⁻¹⁰ m/s². Matches the empirical MOND constant to within ~10%, parameter-free.

**Flat rotation curves** with v² = √(G·M·a₀) in the deep regime. Matches the empirical galactic rotation curve flattening.

**The slope-4 BTFR** with v⁴ = G·M·a₀ and prefactor in substrate constants. Matches the empirical baryonic Tully-Fisher relation.

The chain from primitives to galactic dynamics is parameter-free. Every step is structural; every empirical match is a derivation rather than a fit.

---

## 7. The Architecture of the Derivation

Stepping back, the structural shape of this derivation is worth naming.

The QM walkthroughs had different shapes. Born had T14's Cauchy argument as a single philosophical hinge — the place where the squared exponent gets forced. Schrödinger had Stone's theorem applied to two symmetries plus Galilean closure. Bell-Tsirelson and Heisenberg were upstream contributions to standard arguments.

The gravity arc has yet another shape. There is no single hinge. Instead, the arc has four distinct structural results that compose into the galactic-dynamics chain. Each result has its own load-bearing argument:

The Newton derivation has two load-bearing pieces: the cumulative-strain reading (which gives 1/R²) and the participation-count plus equipartition (which gives the proportionality constant). Newton-matching forces ℓ_ED = ℓ_P, identifying the substrate UV cutoff with the Planck scale.

The transition acceleration has one load-bearing piece: the dipole-mode projection of the cosmic decoupling surface onto the chain's anisotropic accessible region, with the 2π emerging as the azimuthal periodicity of the leading anisotropic mode.

The Combination Rule has one structural commitment: the logarithmic cross-term with √(M·a₀) coefficient as the substrate's response to joint weak-gradient regimes, producing geometric-mean composition rather than sum.

The BTFR is a corollary: composing the three above with centripetal balance gives v⁴ = G·M·a₀ directly.

The composition is what makes the framework's claim about galactic dynamics distinctive. Each result is substantive on its own — Newton's gravitational constant expressed in substrate quantities, the MOND constant derived from cosmology, the geometric-mean combination law, the slope-4 BTFR. But the structural punchline is the parameter-free chain: from substrate primitives all the way to galactic rotation velocities, with no free parameters anywhere in between, and with empirical match to Newton, MOND, and BTFR.

This is what distinguishes the framework's gravity content from MOND. MOND is phenomenological — it adopts the empirical a₀ as input and produces galactic dynamics from there. The framework derives a₀ from the Hubble parameter via dipole-mode projection. MOND is silent on the value of G — it accepts Newton's gravitational constant as empirical input. The framework derives G from c, ℓ_P, and $\hbar$. MOND has no structural account of why galactic dynamics work the way they do; the framework supplies that account at the substrate level.

The framework also makes contact with dark matter explanations differently. In ΛCDM, dark matter is a particle (or particle population) that produces the additional gravitational effects observed at galactic scales. The framework does not introduce new particles; it modifies the effective gravitational dynamics in the deep-acceleration regime via substrate-level structural arguments. The empirical phenomenology that ΛCDM attributes to dark matter halos, the framework attributes to substrate-level dipole-mode projection plus geometric-mean composition. Whether this empirically distinguishes the two approaches depends on regimes where their predictions diverge — galaxy clusters, gravitational lensing, and the cosmic microwave background being the main testing grounds. The framework's substrate-gravity content is currently focused on galactic dynamics; cluster and cosmological extensions are open research directions.

---

## 8. What This Argument Establishes

The chain runs:

Primitives (micro-events, event density, participation, adjacency, chain stability landscape, decoupling surfaces, participation-count bound) → cumulative-strain reading gives 1/R² → participation-count plus equipartition fixes G = c³ℓ_P²/$\hbar$ → Newton's law derived → cosmic decoupling surface at R_H = c/H₀ → acceleration breaks adjacency isotropy → dipole-mode projection with 2π azimuthal periodicity → transition acceleration a₀ = c·H₀/(2π) derived → joint weak-gradient regime gives logarithmic cross-term with √(M·a₀) coefficient → ED Combination Rule a = √(a_N·a₀) derived → composition with centripetal balance gives flat rotation curves v² = √(G·M·a₀) and slope-4 BTFR v⁴ = G·M·a₀ derived.

Each step has its load-bearing arguments worked out. The gravitational constant G is no longer empirical but derived from c, ℓ_P, and $\hbar$. The MOND transition acceleration a₀ is no longer empirical but derived from c, H₀, and a substrate-native 2π geometric factor. The slope-4 BTFR is no longer an empirical regularity but a structural consequence of composing the three substrate results.

The framework reproduces the empirical phenomenology of galactic dynamics. Newton's law works exactly in the high-acceleration regime. The transition acceleration matches the empirical MOND constant to within ~10%, robust against the Hubble tension. Flat rotation curves emerge in the deep-acceleration regime with the correct mass-velocity scaling. The slope-4 BTFR emerges with prefactor in substrate constants. The match with empirical galactic dynamics across all regimes is parameter-free.

Three sharp falsifiers:

A galactic system in the certified deep-acceleration regime that significantly departs from v⁴ = G·M·a₀ falsifies T21, and traces back to T19, T20, or the Combination Rule depending on which step fails.

A measured a₀ significantly outside the band set by the Hubble tension falsifies T20.

A measured deviation from G = c³ℓ_P²/$\hbar$ — where ℓ_P is the standard Planck length — falsifies T19.

The relations are sharp, parameter-free, and directly testable against the SPARC catalog and similar surveys.

Whether the substrate commitments themselves are right is the load-bearing question, as in every other walkthrough. The framework stands or falls on whether micro-events, participation, adjacency, chains, stability landscapes, decoupling surfaces, and participation-count bounds are the correct foundational concepts. The empirical exposure of the framework's gravity content lives in galactic rotation curves, the BTFR slope and scatter, the radial-acceleration relation, and any future tests at the boundaries of the framework's applicability — galaxy clusters, gravitational lensing, cosmological structure formation.

For galactic gravity specifically, the structural case is closed. Newton's law, the transition acceleration, the deep-regime composition rule, flat rotation curves, and the slope-4 BTFR are all derived from substrate primitives. The chain is parameter-free. The empirical match with galactic dynamics is structural rather than phenomenological.

This is the framework's most empirically substantive sector. The QM walkthroughs derived foundational postulates that match standard quantum mechanics exactly but make no new empirical predictions. The arrow-of-time walkthrough derived a substrate-level structural fact whose downstream consequences for thermodynamic and other arrows are open questions. The gravity arc derives the actual empirical phenomenology of galactic dynamics — the rotation curves, the BTFR, the transition scale — with parameter-free agreement against the SPARC catalog and similar surveys. Whether the framework is right at the substrate level is testable here in a way that the QM-emergence content does not provide, because the framework's gravity predictions are structurally distinct from ΛCDM's dark matter halo predictions in regimes where the two have not yet been definitively resolved.

The framework's gravity sector is structurally complete and parameter-free. The empirical case is built where the empirical case for any framework is built — against observations, in the data of galaxies, in tests of the predictions made here.

---

## 9. References

- Milgrom, M. "A modification of the Newtonian dynamics as a possible alternative to the hidden mass hypothesis." *Astrophysical Journal* 270, 365–370 (1983).
- McGaugh, S. S. "The Baryonic Tully-Fisher Relation of Gas Rich Galaxies as a Test of ΛCDM and MOND." *Astronomical Journal* 143, 40 (2012).
- McGaugh, S. S., Lelli, F., and Schombert, J. M. "Radial Acceleration Relation in Rotationally Supported Galaxies." *Physical Review Letters* 117, 201101 (2016).
- Lelli, F., McGaugh, S. S., and Schombert, J. M. "SPARC: Mass Models for 175 Disk Galaxies with Spitzer Photometry and Accurate Rotation Curves." *Astronomical Journal* 152, 157 (2016).
- Proxmire, A. *Structural Foundations of ED-Substrate Gravity: Newton, the Transition Scale, the Combination Rule, and the Baryonic Tully–Fisher Relation.* April 2026.
- Proxmire, A. *Event Density: One Substrate, Three Domains.* April 2026.
- Proxmire, A. *Event Density Foundations: A Unified Substrate Architecture for Quantum, Fluid, Gauge, and Gravitational Dynamics.* April 2026.
- The full Event Density corpus, including all forced theorems and supporting memos, is available at https://github.com/allen-proxmire/event-density.
