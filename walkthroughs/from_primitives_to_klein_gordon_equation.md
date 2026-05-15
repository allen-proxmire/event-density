# From Primitives to the Klein-Gordon Equation

## A Walkthrough of the Event Density Relativistic Wave Equation Derivation

**Allen Proxmire** · May 2026

---

## 1. The Question

The Schrödinger equation describes how quantum systems evolve when they're moving slowly compared to the speed of light. For atoms, molecules, and the chemistry of everyday matter, this is enough — atomic electrons typically move at less than 1% of the speed of light, well within the non-relativistic regime where Galilean invariance is a good approximation.

But quantum mechanics needs a relativistic version. The Schrödinger equation is structurally first-order in time and second-order in space, treating space and time on different footings. Special relativity says space and time are unified into a single four-dimensional structure where Lorentz transformations mix them, and any equation that privileges time over space breaks Lorentz invariance. A truly fundamental quantum equation must respect this symmetry.

The Klein-Gordon equation, written down in 1926 by Oskar Klein and Walter Gordon (and earlier in unpublished form by Schrödinger himself), is the natural relativistic extension for spin-zero particles:

$$
(□ + m^{2}c^{2}/\hbar^{2})\Psi= 0
$$

where □ = ∂_μ∂^μ = (1/c²)∂_t² − ∇² is the d'Alembertian operator. This equation is second-order in both time and space, treats space and time symmetrically, and reduces to the free-particle Schrödinger equation in the non-relativistic limit. Its plane-wave solutions satisfy the relativistic mass-shell condition p_μp^μ = m²c², equivalently E² = p²c² + m²c⁴ — the energy-momentum relation Einstein gave us in 1905.

The standard derivation of the Klein-Gordon equation runs by analogy: start with the relativistic energy-momentum relation E² = p²c² + m²c⁴, replace E by iℏ∂_t and p by −iℏ∇, and apply both sides to a wavefunction. This produces the right equation but it's not really a derivation — it's a guess, motivated by analogy with the Schrödinger procedure of replacing classical observables with quantum operators. The structural reasons for the Klein-Gordon equation, in the standard treatment, are not fundamental; they are operational.

The Event Density framework approaches this differently. The framework's claim is that the Klein-Gordon equation falls out of substrate primitives — the same primitives that gave the Born rule, the Schrödinger equation, and Bell-Tsirelson bound — plus the additional commitment to Lorentz covariance. The chain runs through a small number of structural moves:

The participation measure becomes Lorentz-covariant. Space and time are unified into spacetime events x^μ, the chain becomes a worldline parameterized by proper time, and the four-band bandwidth decomposition becomes four Lorentz-scalar fields.

The unique second-order Lorentz-scalar differential operator on a scalar field is the d'Alembertian. The minimum-order Lorentz-scalar linear equation for a scalar wavefunction is therefore (□ + M²)Ψ = 0 for some constant M with units of inverse length squared.

Dimensional analysis fixes M² = m²c²/ℏ² up to a dimensionless factor, with m the chain's mass, $\hbar$ inherited from the QM-emergence sector, and c the speed of light.

Plane-wave application gives the mass-shell condition p_μp^μ = m²c², equivalently E² = p²c² + m²c⁴.

Local U(1) gauge invariance forces the gauge-covariant derivative D_μ = ∂_μ + (iq/$\hbar$)A_μ, producing the interacting Klein-Gordon equation and the conserved four-current.

The non-relativistic limit, via rest-energy factorization Ψ = e^(−imc²t/$\hbar$)ψ, recovers the free-particle Schrödinger equation exactly. With electromagnetic coupling included, it recovers the Schrödinger equation with magnetic and scalar potentials.

The structural payoff: the Klein-Gordon equation is what you get when you push the framework's substrate ontology — micro-events, participation, channels, bandwidth, polarity — through a Lorentz-covariant reformulation. No new primitives are required. The Phase-1 non-relativistic results (Schrödinger equation, Born rule) are recovered as the v/c → 0 limit of the relativistic content. The framework demonstrates that relativistic and non-relativistic quantum mechanics aren't two separate theories glued together by analogy — they're the same substrate ontology applied at different velocity regimes.

The walkthrough also names what's not delivered. The negative-energy branch of the dispersion relation E_± = ±√(p²c² + m²c⁴) admits two solutions, mathematically forced by the square-root structure. The interpretation of the negative-energy branch as antiparticles requires QFT machinery beyond the present arc. The Klein-Gordon current j^μ = (iℏ/2m)(Ψ*∂^μΨ − Ψ∂^μΨ*) is real and conserved but j^0 is not positive-definite, which means it cannot be interpreted as a probability density at the single-particle level. This pathology resolves at the Dirac level (which has positive-definite density) and at the QFT level (where charged-particle interpretation replaces probability interpretation). For Klein-Gordon at the single-particle level, the framework reproduces the standard physics with the standard caveats.

The chain has six structural moves, and they unfold the same way the standard treatments do — but with each move forced by substrate primitives plus Lorentz covariance, rather than guessed by analogy.

---

## 2. The Substrate Ontology, Made Relativistic

The framework rests on substrate-level ontological commitments. The Klein-Gordon walkthrough uses the same primitives as the QM-emergence walkthroughs (Born, Schrödinger), but now in their Lorentz-covariant reformulations.

**Micro-events.** Reality consists of discrete acts of becoming. Each micro-event is a primitive ontological unit — discrete, irreducible, individuated.

**Chains as worldlines.** A chain is a sequence of micro-events held together by a consistent rule. In the non-relativistic walkthroughs, a chain was parameterized by coordinate time t. In the relativistic reformulation, a chain becomes a worldline x^μ(τ) — a one-dimensional curve in Minkowski spacetime parameterized by proper time τ. The chain identity (rule persistence) is Lorentz-invariant because proper time is Lorentz-invariant.

The transformation is forced by Lorentz invariance. The Phase-1 concept of "the chain's current time" is replaced by "the chain's current proper time," and the commitment-event rate is parameterized by dτ rather than dt. Different inertial frames observe the chain's commitment rate as dτ/dt = √(1 − v²/c²) — the standard relativistic time dilation. The non-relativistic version is recovered in the limit v/c → 0.

**Participation measure on spacetime.** The participation measure for a scalar (bosonic) chain becomes a complex-valued field on Minkowski spacetime:

$$
P_K(x^\mu) = \sqrt(b_K(x^\mu)) \cdot e^{i\pi_K(x^\mu}) \in \mathbb{C}
$$

with x^μ = (ct, **x**) and the polar decomposition (amplitude × phase) inherited from Theorem 14 — the participation measure form was forced in the Born rule walkthrough as the unique structurally admissible measure compatible with substrate consistency.

Under Lorentz transformations Λ, the scalar participation measure transforms as a scalar at each spacetime point:

$$
P_K(x^\mu) \to P'_K(x'^\mu) = P_K(\Lambda^(−1)x'^\mu)
$$

This is the bosonic case — the case where the rule-type's interaction structure is orientation-insensitive at the sub-rotation scale. The fermionic case (spinor transformation) is the subject of the Dirac walkthrough; here we work strictly with bosonic chains.

**Coherent sum and event density.** The total wavefunction is the coherent sum across channels:

$$
\Psi(x^\mu) = \sum_K P_K(x^\mu) \in \mathbb{C}
$$

a Lorentz-scalar field. The event density ρ(x^μ) = $\sum_K$ |P_K(x^μ)|² is a Lorentz scalar. These are the natural relativistic generalizations of the Phase-1 wavefunction and event density.

**Four-band bandwidth decomposition.** In the Phase-1 framework, bandwidth is partitioned into four bands: internal (rule-bandwidth), adjacency (with spatial neighbors), environmental (with broader environment), and commitment-reserve. Each band is a non-negative real-valued field on space and time.

In the relativistic reformulation, each of the four bands becomes a Lorentz-scalar field on spacetime: b_K^int(x^μ), b_K^adj(x^μ), b_K^env(x^μ), b_K^com(x^μ). The decomposition and the sum-rule b_K = $\sum_i$ b_K^(i) are Lorentz-invariant. The four bands carry Lorentz-scalar content at each spacetime event.

A refinement enters here that didn't exist at the non-relativistic level: spatial adjacency in the Phase-1 framework becomes light-cone adjacency in the relativistic framework. Adjacency between two regions is restricted by the causal structure of spacetime. Spacelike-separated regions can participate only through their common causal past. This is the substrate-level statement of no-signaling — the relativistic framework's locality constraint.

**Four-gradient.** The Phase-1 ED gradient ∇ρ becomes the four-gradient ∂_μρ, which transforms as a covariant four-vector under Lorentz transformations. The Phase-1 spatial and temporal derivatives are unified — no distinction between "time-component" and "spatial-components" is primitively significant; only the four-vector structure is. This is forced by Lorentz invariance: the four-gradient is the unique Lorentz-covariant derivative operator on scalar fields.

Two covariant differential operators are accessible at the primitive level: the four-divergence ∂_μV^μ for a four-vector V^μ, which gives continuity equations; and the d'Alembertian □ = ∂_μ∂^μ = (1/c²)∂_t² − ∇², which is the unique second-order Lorentz-scalar differential operator on scalar fields. The d'Alembertian is the operator that will appear in the Klein-Gordon equation.

**Relational timing as proper-time phase coupling.** The Phase-1 relational-timing primitive — phase coupling between channels parameterized by coordinate time — becomes proper-time phase coupling in the relativistic reformulation. Each chain's intrinsic timing is its proper time τ, which is the same in every inertial frame. Relational timing between two chains is specified by the difference in their proper-time parameterizations along their worldlines.

For coherent channel structure within a single chain, the relational timing is the phase advancement ∂_τ$\pi_K$ per proper-time interval — Lorentz-invariant. This is forced by Lorentz invariance: proper time is the natural Lorentz-invariant parameter.

**No new primitives.** The four primitive reformulations (chain → worldline, four-band → covariant scalar fields, ED gradient → four-gradient, relational timing → proper-time) are forced by Lorentz invariance, but none of them is a new primitive. The Phase-1 versions are non-relativistic limits of the covariant versions; the covariant versions reduce to Phase-1 forms in the v/c → 0 limit. The framework's primitive stack is preserved.

That's the working set. From here, the Klein-Gordon equation falls out of two structural arguments: the unique second-order Lorentz-scalar operator and the mass-shell condition.

---

## 3. The d'Alembertian Forced

The first structural move is showing that the d'Alembertian is the unique second-order Lorentz-scalar differential operator on a scalar field — and therefore the unique candidate for the leading-order term in any Lorentz-covariant linear scalar wave equation.

### 3.1 The space of Lorentz-scalar differential operators on a scalar field

Consider a complex-valued scalar field Ψ(x^μ) on Minkowski spacetime. A linear differential operator acting on Ψ produces another field. The question is: what linear differential operators are Lorentz scalars (so that the resulting equation transforms covariantly under Lorentz transformations)?

At zeroth order, any constant α multiplying Ψ produces a scalar field αΨ. The operator α (a multiplication operator) is a Lorentz scalar trivially.

At first order, the only available differential operator is the four-gradient ∂_μΨ. But ∂_μΨ is a four-vector, not a scalar — it has an index that transforms under Lorentz transformations. There is no Lorentz-scalar first-order differential operator constructible linearly from Ψ alone.

(One could form the scalar ∂_μΨ ∂^μΨ*, but this is quadratic in Ψ, producing nonlinear equations. The framework's linearity commitment — inherited from Theorem U3 in the Schrödinger walkthrough — restricts attention to linear equations.)

At second order, two differential operators are available. The first is ∂_μ∂_νΨ, which carries two indices and is a rank-2 tensor — not a scalar. The second is the contraction ∂_μ∂^μΨ, where the indices are contracted using the Minkowski metric η^μν. This contraction is a Lorentz scalar. We define:

$$
□ \equiv \partial_\mu \partial^\mu= \eta^\mu \nu \partial_\mu \partial_\nu= (1/c^{2})\partial_t^{2} − \nabla^{2}
$$

The d'Alembertian. This is the unique second-order linear differential operator on a scalar field that produces a Lorentz scalar.

At third order and higher, additional operators are constructible, but they involve higher-order derivative structures. For the minimum-order linear scalar equation — the simplest dynamical equation compatible with Lorentz invariance — second order is sufficient.

### 3.2 The minimum-order linear scalar equation

The most general linear, Lorentz-scalar equation in Ψ at second order has the form:

$$
A □\Psi + B \Psi= 0
$$

for real constants A and B. (Higher-order equations would involve □²Ψ, □³Ψ, etc. — these are not minimum-order.)

Normalizing A = 1 without loss of generality:

$$
(□ + M^{2})\Psi= 0
$$

where M² = B is some real constant with units of [length]^(−2), since □ has units of [length]^(−2) and Ψ has whatever units it has independently.

This is the structural form of the Klein-Gordon equation, derived from Lorentz invariance plus the minimum-order linear-scalar-equation requirement. The constant M² is not yet specified; that requires dimensional analysis plus the mass-shell argument of Section 4.

### 3.3 Why second-order in time is forced

A natural worry: the Schrödinger equation iℏ∂_tΨ = $\hat{H}$Ψ is first-order in time. Why does the relativistic version need to be second-order?

The answer is forced by Lorentz invariance. The first-order time derivative ∂_t is the zero-component of the four-gradient ∂_μ — it transforms as a four-vector component, not as a scalar. An equation involving ∂_tΨ alone privileges the time direction over the spatial directions, breaking Lorentz invariance. The Schrödinger equation is acceptable in the non-relativistic regime because Galilean invariance treats time as absolute, but Lorentz invariance requires that any equation involving ∂_t must also involve spatial derivatives in a structurally-paired way that reconstructs a Lorentz scalar.

The unique Lorentz-scalar operator built from second-order time derivatives is (1/c²)∂_t², appearing as one component of the d'Alembertian □ = (1/c²)∂_t² − ∇². The pairing with the spatial Laplacian is forced by the contraction structure ∂_μ∂^μ. Once you commit to Lorentz invariance, you are forced into second-order time derivatives in any minimum-order linear scalar equation.

This is not an aesthetic preference. It is a structural consequence of how Lorentz transformations mix time and space derivatives. There is no first-order Lorentz-covariant linear scalar wave equation in the strict sense. (The Dirac equation is first-order, but at the cost of introducing spinor-valued fields and the Cl(3,1) structure — that's the Dirac walkthrough.)

### 3.4 Status

The d'Alembertian is the unique second-order Lorentz-scalar differential operator on a scalar field. The minimum-order linear scalar equation has the form (□ + M²)Ψ = 0 for some constant M² with units of [length]^(−2).

Both results are forced. Lorentz covariance plus linearity plus minimum-order plus scalar-field constraints leave no other choice.

---

## 4. The Mass-Shell Condition and Relativistic Dispersion

The constant M² is not yet specified. The framework gives M² a structural meaning by applying the Klein-Gordon form to plane-wave participation modes.

### 4.1 Plane-wave participation modes

A plane-wave participation mode has the form:

$$
P_K(x^\mu) = c_K \cdot e^{−ip_\mu x^\mu /\hbar}
$$

where p_μ = (E/c, −**p**) is the four-momentum (with the lower-index convention) and c_K is a complex amplitude. Writing out the components:

$$
p_\mu x^\mu= (E/c) \cdot ct − (−**p**) \cdot **x** = Et − **p** \cdot **x**
$$

so:

$$
P_K(x^\mu) = c_K \cdot e^{i(**p** \cdot **x** − Et}/\hbar)
$$

This is the standard plane-wave wavefunction familiar from non-relativistic QM, but now with the time-dependence Et appearing alongside the space-dependence **p**·**x** in a four-dimensional inner product structure.

The plane-wave form is the Lorentz-covariant generalization of Phase-1's momentum-basis mode P_k(x, t) = c_k · e^(ikx/2π). In the Schrödinger walkthrough, the plane-wave form was forced by Stone's theorem applied to spatial translation: continuous-symmetry one-parameter groups generate self-adjoint operators whose eigenfunctions are exponentials. The same argument applies to four-translation in the relativistic framework — Poincaré invariance applied to the participation-measure structure forces plane-wave modes parameterized by four-momentum.

### 4.2 The d'Alembertian on plane-wave modes

Apply the d'Alembertian to a plane-wave mode:

$$
□P_K = \partial_\mu \partial^\mu(c_K \cdot e^{−ip_\nu x^\nu /\hbar})
$$

Using ∂_μ e^(−ip_νx^ν/$\hbar$) = (−ip_μ/$\hbar$) e^(−ip_νx^ν/$\hbar$):

$$
□P_K = c_K \cdot(−ip_\mu /\hbar)(−ip^\mu /\hbar) \cdot e^{−ip_\nu x^\nu /\hbar}
= −(p_\mu p^\mu /\hbar^{2}) \cdot P_K
$$

This is an algebraic identity. For any plane-wave mode with well-defined four-momentum p_μ, the d'Alembertian acts as multiplication by −p_μp^μ/ℏ².

### 4.3 The mass-shell condition

For the plane-wave mode to satisfy the Klein-Gordon form (□ + M²)P_K = 0, equate:

$$
−(p_\mu p^\mu /\hbar^{2}) + M^{2} = 0
$$

which gives:

$$
p_\mu p^\mu= \hbar^{2}M^{2}
$$

This is the mass-shell condition. It says that the four-momentum of any plane-wave mode satisfying the Klein-Gordon equation must lie on a specific hypersurface in four-momentum space — the "mass shell" — characterized by a single scalar invariant ℏ²M².

### 4.4 Identifying M with the chain mass

The constant M² has units of [length]^(−2). The unique combination of the framework's dimensional anchors — the chain mass m, the speed of light c, and $\hbar$ — with units of [length]^(−2) is:

$$
M^{2} = (mc/\hbar)^{2} = m^{2}c^{2}/\hbar^{2}
$$

up to a dimensionless multiplicative factor. The dimensionless factor is set to unity by physical identification: M is the inverse Compton wavelength of the chain, and the mass-shell condition becomes:

$$
p_\mu p^\mu= m^{2}c^{2}
$$

In components, p_μp^μ = (E/c)² − |**p**|² = m²c², equivalently:

$$
E^{2} = |**p**|^{2}c^{2} + m^{2}c^{4}
$$

This is the relativistic energy-momentum dispersion relation. Einstein's 1905 result is now the structural consequence of plane-wave application to the framework's minimum-order Lorentz-scalar linear equation.

The Klein-Gordon equation in its standard form:

$$
(□ + m^{2}c^{2}/\hbar^{2})\Psi(x^\mu) = 0
$$

is now derived. The d'Alembertian is forced by Lorentz covariance plus minimum-order linearity. The mass term is forced by dimensional consistency plus the mass-shell identification.

### 4.5 Positive and negative energy branches

The mass-shell condition admits two energy branches:

$$
E_ \pm= \pm \sqrt{|**p**|^{2}c^{2} + m^{2}c^{4}}
$$

Both branches are mathematically forced by the square-root structure of the dispersion relation. In the standard treatment, the positive-energy branch describes particles, and the negative-energy branch is reinterpreted (after Dirac's hole theory and the development of QFT) as antiparticles propagating backward in time, or equivalently as forward-propagating antiparticles with positive energy.

At the single-particle level, the negative-energy branch is structurally awkward — single-particle quantum mechanics has no natural place for negative-energy states with arbitrarily-large negative energies, since there's nothing preventing transitions to lower and lower energies. This is one of the standard motivations for the QFT extension. At the QFT level, the negative-energy branch becomes the antiparticle sector of the field, and the conceptual issue is resolved.

The framework does not address the antiparticle interpretation in this walkthrough. The mass-shell condition is what's forced; the antiparticle interpretation requires QFT machinery (the framework's Arc Q) that's beyond the present scope.

### 4.6 Status

The mass-shell condition p_μp^μ = m²c² is forced by applying the Klein-Gordon form to plane-wave modes. The relativistic dispersion E² = p²c² + m²c⁴ follows in components. The Klein-Gordon equation in its standard form is now derived from substrate primitives plus Lorentz covariance.

The negative-energy branch is mathematically forced; its physical interpretation as antiparticles requires QFT extension beyond the present arc.

---

## 5. The Coherent Sum

The Klein-Gordon equation was derived for a single plane-wave participation mode. The full wavefunction is the coherent sum across channels:

$$
\Psi(x^\mu) = \sum_K P_K(x^\mu)
$$

By linearity of the d'Alembertian and the linearity of the Klein-Gordon equation:

$$
(□ + m^{2}c^{2}/\hbar^{2})\Psi(x^\mu) = (□ + m^{2}c^{2}/\hbar^{2}) \sum_K P_K(x^\mu)
= \sum_K (□ + m^{2}c^{2}/\hbar^{2})P_K(x^\mu)
= 0
$$

provided each P_K is a solution. The coherent sum inherits the Klein-Gordon equation from each individual mode.

The linearity used here is the same linearity that Theorem U3 established in the non-relativistic Schrödinger walkthrough: the participation-measure evolution is linear, and the coherent sum of solutions is itself a solution. The Lorentz-covariant version of U3 inherits the linearity content; it is the structural backbone that makes superposition work.

This means general solutions to the Klein-Gordon equation are linear combinations of plane-wave modes:

$$
\Psi(x^\mu) = \int d^{4}p/(2\pi)^{4} \cdot(2\pi \hbar) \delta(p_\mu p^\mu − m^{2}c^{2}) \cdot ã(p) \cdot e^{−ip_\mu x^\mu /\hbar}
$$

with the delta function δ(p_μp^μ − m²c²) restricting the integration to the mass shell, and ã(p) the four-momentum-space amplitude. This integral form is the standard expansion of Klein-Gordon solutions in plane-wave modes.

The coherent-sum structure carries over from the Phase-1 framework without modification. What's new is that the modes are now Lorentz-covariant plane waves on the mass shell, rather than non-relativistic plane waves with quadratic dispersion.

---

## 6. Local Gauge Invariance and Minimal Coupling

The Klein-Gordon equation derived so far is the free-particle equation. Real charged particles interact with electromagnetic fields. The framework forces the form of this interaction through local U(1) gauge invariance.

### 6.1 The local phase symmetry

The participation measure has a global U(1) symmetry: the phase $\pi_K$(x^μ) can be shifted by a constant α/$\hbar$, which multiplies the wavefunction by an overall phase factor e^(iqα/$\hbar$):

$$
\Psi(x^\mu) \to e^{iq\alpha /\hbar} \Psi(x^\mu)
$$

(The factor of q/$\hbar$ in the phase is conventional — it sets the natural scale.)

The free Klein-Gordon equation is invariant under this global phase shift: the d'Alembertian and the mass term both commute with multiplication by a constant phase factor.

Now consider promoting α from a constant to a function of spacetime: α(x^μ). Under a local phase shift:

$$
\Psi(x^\mu) \to e^{iq\alpha(x^\mu}/\hbar) \Psi(x^\mu)
$$

the d'Alembertian is no longer invariant — derivatives of the phase appear:

$$
\partial_\mu(e^{iq\alpha /\hbar} \Psi) = e^{iq\alpha /\hbar} (\partial_\mu \Psi + (iq/\hbar)(\partial_\mu \alpha) \Psi)
$$

The Klein-Gordon equation, which involves second derivatives of Ψ, picks up additional terms involving derivatives of α(x^μ) and is no longer satisfied by the transformed Ψ.

### 6.2 The gauge-covariant derivative

To restore local invariance, introduce a four-vector field A_μ(x^μ) — the electromagnetic four-potential — and replace ∂_μ by:

$$
D_\mu \equiv \partial_\mu + (iq/\hbar)A_\mu
$$

Under a local U(1) transformation parameterized by α(x^μ):

$$
\Psi(x^\mu) \to \Psi'(x^\mu) = e^{iq\alpha /\hbar} \Psi(x^\mu)
A_\mu(x^\mu) \to A'_\mu(x^\mu) = A_\mu − \partial_\mu \alpha
$$

Direct computation:

$$
D'_\mu \Psi' = (\partial_\mu + (iq/\hbar)A'_\mu)(e^{iq\alpha /\hbar} \Psi)
= e^{iq\alpha /\hbar} [\partial_\mu \Psi + (iq/\hbar)(\partial_\mu \alpha)\Psi + (iq/\hbar)(A_\mu − \partial_\mu \alpha)\Psi]
= e^{iq\alpha /\hbar} [\partial_\mu \Psi + (iq/\hbar)A_\mu \Psi]
= e^{iq\alpha /\hbar} D_\mu \Psi
$$

The (∂_μα) terms cancel. The covariant derivative D_μΨ transforms with the same phase factor as Ψ itself. This is the defining property of a gauge-covariant derivative: it preserves the local-symmetry transformation.

### 6.3 The interacting Klein-Gordon equation

Replace ∂_μ by D_μ in the free equation:

$$
(D_\mu D^\mu + m^{2}c^{2}/\hbar^{2})\Psi(x^\mu) = 0
$$

Applying the same transformation argument twice, D_μD^μΨ transforms as:

$$
(D'_\mu D'^\mu)\Psi' = e^{iq\alpha /\hbar} D_\mu D^\mu \Psi
$$

so the equation transforms as a multiplication by an overall phase, which leaves the equation 0 = 0 invariant. The equation is gauge-covariant.

Expanding the covariant derivative:

$$
D_\mu D^\mu= (\partial_\mu + (iq/\hbar)A_\mu)(\partial^\mu + (iq/\hbar)A^\mu)
= □ + (iq/\hbar)[A_\mu \partial^\mu + \partial_\mu(A^\mu \cdot)] − (q^{2}/\hbar^{2})A_\mu A^\mu
$$

In Lorenz gauge ∂_μA^μ = 0, this simplifies to:

$$
D_\mu D^\mu \Psi= □\Psi + (2iq/\hbar)A_\mu \partial^\mu \Psi − (q^{2}/\hbar^{2})A_\mu A^\mu \Psi
$$

The interacting Klein-Gordon equation reduces to the free equation when A_μ = 0.

### 6.4 Why minimal coupling is forced

The replacement ∂_μ → D_μ is the unique first-order modification that restores local U(1) gauge invariance. To see this: any modification that preserves local invariance must transform Ψ-dependent terms in ways compatible with the local phase factor. The first-order option is to add a term proportional to A_μΨ to ∂_μΨ, with the proportionality constant fixed by requiring covariance. The result is D_μ as written.

Higher-order modifications (terms proportional to A_μA_νΨ at first order in derivatives, or non-minimal couplings involving curvature-like field strengths) are also gauge-covariant in principle but introduce additional structure that's not forced by local invariance alone. The minimal-coupling prescription D_μ = ∂_μ + (iq/$\hbar$)A_μ is the unique first-order, minimum-structure solution.

The framework treats local U(1) gauge invariance as a structural commitment at the participation-phase level. The gauge symmetry itself is a primitive-level feature: the participation measure's overall phase has no absolute meaning; only relative phases between channels carry physical content. Local invariance — phase shifts varying across spacetime — is the natural extension of this primitive content to the relativistic regime, and it forces the minimal-coupling structure.

### 6.5 Status

The gauge-covariant derivative D_μ = ∂_μ + (iq/$\hbar$)A_μ is forced by local U(1) gauge invariance. The interacting Klein-Gordon equation (D_μD^μ + m²c²/ℏ²)Ψ = 0 is the unique first-order gauge-covariant extension of the free equation.

The charge q and the electromagnetic four-potential A_μ are inherited at the species and apparatus levels respectively — q is the chain's electromagnetic charge per rule-type, A_μ is the external field configuration set by the experimental context.

The non-Abelian extension to SU(N) gauge groups (replacing the single phase by an internal index and A_μ by a Lie-algebra-valued field) follows the same structural pattern, with the choice of gauge group entering as rule-type data rather than being primitive-derivable. That's content for the framework's gauge arc, not the present walkthrough.

---

## 7. The Conserved Four-Current

The interacting Klein-Gordon equation produces a conserved four-current associated with charge conservation. The argument is direct algebraic computation.

### 7.1 Definition

The four-current for the minimally-coupled Klein-Gordon equation is:

$$
j^\mu(x^\nu) = (i\hbar /2m)[\Psi * D^\mu \Psi − \Psi(D^\mu \Psi)*]
$$

The factor of i and the antisymmetric combination Ψ*(D^μΨ) − Ψ(D^μΨ)* make j^μ a real four-vector (the bracketed quantity is purely imaginary, multiplied by i gives a real number, and $\hbar$/(2m) is real).

### 7.2 Gauge invariance

Under a local U(1) transformation, Ψ → e^(iqα/$\hbar$)Ψ and D_μΨ → e^(iqα/$\hbar$)D_μΨ. The bilinear Ψ*(D^μΨ) transforms as:

$$
\Psi *(D^\mu \Psi) \to(e^{−iq\alpha /\hbar}\Psi *)(e^{iq\alpha /\hbar}D^\mu \Psi) = \Psi *(D^\mu \Psi)
$$

The phase factors cancel — the bilinear is gauge-invariant. The same applies to Ψ(D^μΨ)*. Therefore j^μ is gauge-invariant.

### 7.3 The continuity equation

Take the four-divergence of j^μ:

$$
\partial_\mu j^\mu= (i\hbar /2m)[\partial_\mu(\Psi *D^\mu \Psi) − \partial_\mu(\Psi(D^\mu \Psi)*)]
$$

Since Ψ*(D^μΨ) is gauge-invariant (net charge zero), its ordinary four-divergence equals its gauge-covariant four-divergence:

$$
\partial_\mu(\Psi *D^\mu \Psi) = D_\mu(\Psi *D^\mu \Psi) = (D_\mu \Psi)*(D^\mu \Psi) + \Psi *(D_\mu D^\mu \Psi)
$$

Using the interacting Klein-Gordon equation D_μD^μΨ = −(m²c²/ℏ²)Ψ:

$$
\partial_\mu(\Psi *D^\mu \Psi) = (D_\mu \Psi)*(D^\mu \Psi) − (m^{2}c^{2}/\hbar^{2})|\Psi|^{2}
$$

Similarly for the conjugate term:

$$
\partial_\mu(\Psi(D^\mu \Psi)*) = (D_\mu \Psi)(D^\mu \Psi)* − (m^{2}c^{2}/\hbar^{2})|\Psi|^{2}
$$

Subtracting:

$$
\partial_\mu(\Psi *D^\mu \Psi) − \partial_\mu(\Psi(D^\mu \Psi)*) = (D_\mu \Psi)*(D^\mu \Psi) − (D_\mu \Psi)(D^\mu \Psi)*
$$

The two terms on the right are complex conjugates of each other, and both are real (they are sesquilinear contractions). Their difference vanishes.

Therefore:

$$
\partial_\mu j^\mu= 0
$$

The four-current is conserved as an algebraic consequence of the interacting Klein-Gordon equation.

### 7.4 Physical interpretation

The four-current has components j^μ = (c$\rho_e$m, **j**_em) where $\rho_e$m is the electric charge density and **j**_em is the charge-current density. The continuity equation in components reads:

$$
\partial_t \rho_{\mathrm{em}} + \nabla \cdot **j**_{\mathrm{em}} = 0
$$

expressing local conservation of electric charge.

### 7.5 The negative-density pathology

The zeroth component j^0 of the Klein-Gordon current is not positive-definite. For a stationary plane-wave mode Ψ = e^(−iEt/$\hbar$) with positive energy E > 0, the time component j^0 is positive. But for a negative-energy mode Ψ = e^(+i|E|t/$\hbar$), j^0 is negative.

This means j^0 cannot be interpreted as a probability density at the single-particle level. In the Schrödinger framework, |ψ|² is the positive-definite probability density. In the Klein-Gordon framework, j^0 is the charge density rather than a probability density, and it can take both signs depending on the phase structure of the wavefunction.

This is one of the standard arguments motivating the QFT extension. At the field-theoretic level, j^0 is reinterpreted as the difference between particle and antiparticle densities — positive j^0 corresponds to an excess of particles, negative j^0 to an excess of antiparticles. The single-particle interpretive obstacle is resolved at the field-theoretic level.

For the framework, this is honest territory: the Klein-Gordon equation reproduces the standard physics including the standard pathologies. The pathology resolves at the Dirac level (which has positive-definite density for fermionic chains, derived in the Dirac walkthrough) and at the QFT level (which is future arc work).

### 7.6 Status

The conserved four-current j^μ = (iℏ/2m)[Ψ*D^μΨ − Ψ(D^μΨ)*] is gauge-invariant, real, and satisfies ∂_μj^μ = 0 as a direct algebraic consequence of the interacting Klein-Gordon equation.

The non-positive-definiteness of j^0 is honestly named as an interpretive limitation of single-particle Klein-Gordon. It is not a pathology of the framework; it is a pathology of single-particle scalar relativistic quantum mechanics that's been known since 1926, resolved only at the QFT level.

---

## 8. The Non-Relativistic Limit

The framework's claim of structural completeness requires that the Klein-Gordon equation reduce to the Phase-1 Schrödinger equation in the non-relativistic limit v/c → 0. This section verifies the reduction explicitly.

### 8.1 Rest-energy factorization

In the non-relativistic regime, the particle's total energy is dominated by its rest energy E_0 = mc². Kinetic energy and potential energy are small corrections. Write the wavefunction as:

$$
\Psi(x^\mu) = e^{−iE_0t/\hbar} \cdot \psi(**x**, t) = e^{−imc^{2}t/\hbar} \cdot \psi(**x**, t)
$$

factoring out the rapidly-oscillating rest-energy time-dependence. The residual ψ captures the slow non-relativistic dynamics.

### 8.2 Computing derivatives

Time derivatives:

$$
\partial_t\Psi= e^{−imc^{2}t/\hbar} [−(imc^{2}/\hbar)\psi + \partial_t\psi]

\partial_t^{2}\Psi= e^{−imc^{2}t/\hbar} [−(m^{2}c^{4}/\hbar^{2})\psi − (2imc^{2}/\hbar)\partial_t\psi + \partial_t^{2}\psi]
$$

Dividing by c²:

$$
(1/c^{2})\partial_t^{2}\Psi= e^{−imc^{2}t/\hbar} [−(m^{2}c^{2}/\hbar^{2})\psi − (2im/\hbar)\partial_t\psi + (1/c^{2})\partial_t^{2}\psi]
$$

Spatial derivatives:

$$
\nabla^{2}\Psi= e^{−imc^{2}t/\hbar} \nabla^{2}\psi
$$

### 8.3 Substitution into Klein-Gordon

The free Klein-Gordon equation:

$$
[(1/c^{2})\partial_t^{2} − \nabla^{2} + m^{2}c^{2}/\hbar^{2}]\Psi= 0
$$

Substituting and dividing through by e^(−imc²t/$\hbar$):

$$
−(m^{2}c^{2}/\hbar^{2})\psi − (2im/\hbar)\partial_t\psi + (1/c^{2})\partial_t^{2}\psi − \nabla^{2}\psi + (m^{2}c^{2}/\hbar^{2})\psi= 0
$$

The (m²c²/ℏ²)ψ terms cancel — the rest-energy factor was chosen precisely to make this happen. The remaining equation:

$$
−(2im/\hbar)\partial_t\psi + (1/c^{2})\partial_t^{2}\psi − \nabla^{2}\psi= 0
$$

### 8.4 Dropping the relativistic correction

The term (1/c²)∂_t²ψ is suppressed relative to (2im/$\hbar$)∂_tψ in the non-relativistic regime. To see this: if the characteristic energy scale of ψ is the kinetic energy E_kin ~ p²/(2m) ≪ mc², then:

$$
(1/c^{2})\partial_t^{2}\psi ~ E_{\mathrm{kin}}^{2}/(\hbar^{2}c^{2}) \cdot \psi
(2im/\hbar)\partial_t\psi ~ 2mE_{\mathrm{kin}}/\hbar^{2} \cdot \psi
$$

The ratio is E_kin/(2mc²) ≪ 1. The (1/c²)∂_t² term is the leading relativistic correction and can be dropped in the strict v/c → 0 limit.

Dropping the suppressed term:

$$
−(2im/\hbar)\partial_t\psi − \nabla^{2}\psi= 0
$$

Rearranging:

$$
(2im/\hbar)\partial_t\psi= −\nabla^{2}\psi
$$

Multiplying both sides by ℏ²/(2m):

$$
i\hbar \partial_t\psi= −(\hbar^{2}/2m)\nabla^{2}\psi
$$

This is the free-particle Schrödinger equation. The non-relativistic limit of Klein-Gordon is exactly the equation derived in the Phase-1 Schrödinger walkthrough.

### 8.5 Including potentials

For Klein-Gordon with electromagnetic coupling, the non-relativistic limit includes the magnetic and scalar potentials. Following the same rest-energy factorization with the full interacting Klein-Gordon equation, dropping the suppressed term, and rearranging:

$$
i\hbar \partial_t\psi= [(1/2m)(−i\hbar \nabla − q**A**)^{2} + q\varphi] \psi
$$

where φ is the scalar potential and **A** is the magnetic vector potential. This is the Schrödinger equation with electromagnetic coupling — the standard non-relativistic wave equation for a charged particle in an external electromagnetic field.

For a generic non-electromagnetic potential V(**x**), the corresponding limit of Klein-Gordon (with V incorporated through E_0 → E_0 + V) gives:

$$
i\hbar \partial_t\psi= [−(\hbar^{2}/2m)\nabla^{2} + V(**x**)] \psi
$$

the Schrödinger equation with potential. This matches the Phase-1 Schrödinger result exactly.

### 8.6 Status

The non-relativistic limit of Klein-Gordon, via rest-energy factorization Ψ = e^(−imc²t/$\hbar$)ψ and dropping the suppressed (1/c²)∂_t² term, recovers the free-particle Schrödinger equation iℏ∂_tψ = −(ℏ²/2m)∇²ψ exactly. With electromagnetic coupling, it recovers the Schrödinger equation with magnetic and scalar potentials.

This is the framework's consistency check: the relativistic structural derivation reproduces the non-relativistic structural derivation in the appropriate limit. Phase-1 (Schrödinger) is recovered as a sub-theory of Phase-2 (Klein-Gordon) at low velocities. The framework is internally consistent across the two regimes.

---

## 9. What's Forced, What's Inherited, What's Open

The framework is honest about what its current machinery delivers and what remains future work.

**Forced at substrate level:**

The Lorentz-covariant participation measure P_K(x^μ) = √b_K · e^(i$\pi_K$) on Minkowski spacetime, transforming as a scalar under SO⁺(3,1) for bosonic chains.

The four primitive reformulations: chain → worldline parameterized by proper time, four-band → four covariant Lorentz-scalar fields, ED gradient → four-gradient ∂_μ, relational timing → proper-time phase coupling.

The d'Alembertian □ = ∂_μ∂^μ as the unique second-order Lorentz-scalar differential operator on a scalar field.

The Klein-Gordon form (□ + m²c²/ℏ²)Ψ = 0 as the minimum-order linear Lorentz-scalar wave equation, with the mass-term coefficient forced by dimensional consistency.

The mass-shell condition p_μp^μ = m²c² as the algebraic consequence of plane-wave application to the Klein-Gordon form.

The relativistic dispersion E² = p²c² + m²c⁴ in components.

The two energy branches E_± = ±√(p²c² + m²c⁴) as mathematical consequences of the square-root structure.

The gauge-covariant derivative D_μ = ∂_μ + (iq/$\hbar$)A_μ as the unique first-order modification restoring local U(1) gauge invariance.

The interacting Klein-Gordon equation (D_μD^μ + m²c²/ℏ²)Ψ = 0.

The conserved four-current j^μ = (iℏ/2m)[Ψ*D^μΨ − Ψ(D^μΨ)*] satisfying ∂_μj^μ = 0 as a direct algebraic consequence.

The non-relativistic limit recovering the Phase-1 Schrödinger equation exactly.

**Inherited at value layer:**

The speed of light c (the Lorentz invariance scale, set by the Minkowski metric normalization).

The reduced Planck constant $\hbar$ (inherited via U3 from the Phase-1 framework, as in the Schrödinger walkthrough).

The chain mass m (species-level empirical input; chain-mass derivation is open work in the framework's Arc M).

The electromagnetic charge q (species-level empirical input).

The external electromagnetic four-potential A_μ(x^ν) (apparatus-level specification).

**Open or future arc work:**

**Antiparticle interpretation of the negative-energy branch.** The mathematical structure forces both energy branches; their physical interpretation as particles and antiparticles requires QFT machinery beyond the present walkthrough. This is Arc Q content.

**The KG negative-density pathology.** The j^0 component is not positive-definite, so it cannot be interpreted as a probability density at the single-particle level. This is one of the standard motivations for the QFT extension. The framework reproduces this standard limitation.

**The fermionic case.** The Klein-Gordon equation applies to bosonic (scalar) chains. The fermionic case requires the Cl(3,1) algebraic structure, the spinor participation measure, and the Dirac equation — these are the subject of the Dirac walkthrough.

**Multi-particle content.** Second quantization, field operators, particle creation and annihilation — all require the QFT extension (Arc Q), which builds on the Arc R foundation laid by Klein-Gordon and Dirac.

**Chain-mass derivation.** The numerical value of m is currently inherited at the species level. Whether the framework derives specific mass values, structural mass-hierarchy form, or both is the subject of Arc M (chain-mass), which the framework's author has flagged as substantively explained in the corpus but which has not yet been walkthrough-presented.

**The dynamical electromagnetic field.** A_μ is treated as an external field in this walkthrough. Its primitive-level emergence (Maxwell's equations in the framework) is content for the gauge arc, beyond present scope.

---

## 10. What This Argument Establishes

The chain runs:

Primitives (micro-events, participation, chains, channels, bandwidth, polarity, commitment irreversibility, relational timing) → Lorentz-covariant reformulation (chain → worldline, ED gradient → four-gradient, relational timing → proper-time, four-band → covariant scalar fields) → Lorentz-covariant participation measure P_K(x^μ) = √b_K · e^(i$\pi_K$) → unique second-order Lorentz-scalar operator □ → minimum-order linear scalar equation (□ + M²)Ψ = 0 → dimensional analysis fixes M² = m²c²/ℏ² → mass-shell condition from plane-wave application → relativistic dispersion E² = p²c² + m²c⁴ → local U(1) invariance forces D_μ = ∂_μ + (iq/$\hbar$)A_μ → interacting Klein-Gordon equation → conserved four-current → non-relativistic limit recovers Schrödinger.

Each move has its load-bearing argument worked out. The d'Alembertian is forced by Lorentz covariance plus minimum-order linearity plus scalar-field constraints. The mass term is forced by dimensional consistency. The mass-shell condition is forced by plane-wave application. The minimal-coupling prescription is forced by local U(1) gauge invariance. The conserved current is forced by direct algebraic consequence. The non-relativistic limit recovers Phase-1 exactly.

The framework reproduces the Klein-Gordon equation. It does not derive the negative-energy branch's antiparticle interpretation. It does not produce a positive-definite probability density at the single-particle level. It operates within bosonic-chain content; fermionic content requires Cl(3,1) and the Dirac equation. These are honestly named limitations, with explicit pointers to the arcs that close them.

What the framework does that standard treatments do not: it derives the Klein-Gordon equation from substrate primitives plus Lorentz covariance, rather than guessing it by analogy with the Schrödinger procedure. The standard treatment starts with the relativistic dispersion E² = p²c² + m²c⁴ and replaces E by iℏ∂_t, p by −iℏ∇, giving the Klein-Gordon form by quantization. The framework reverses this: it derives the Klein-Gordon form from substrate structure (Lorentz-scalar minimum-order linear equation, plus dimensional consistency), and the relativistic dispersion falls out as the mass-shell condition for plane-wave solutions. The standard treatment is operational; the framework is structural.

This matters because the substrate-level derivation makes explicit which features of relativistic quantum mechanics are forced by Lorentz covariance and which are model-dependent. The d'Alembertian is forced. The mass-shell condition is forced. The minimal-coupling prescription is forced by local U(1) invariance. The non-relativistic limit's recovery of Schrödinger is structural. None of these is a guess; each is a structural consequence of substrate primitives plus the framework's commitment to Lorentz covariance at the relativistic level.

Whether the substrate commitments are right is the load-bearing question, as in every walkthrough. The framework stands or falls on whether discreteness, finite participation bandwidth, commitment irreversibility, and the rest of the substrate ontology are the correct foundational concepts. The empirical exposure of the Klein-Gordon content is the standard empirical exposure of relativistic scalar quantum mechanics — pion physics, scalar-field cosmology, the Higgs sector at low energies. The framework reproduces this content with the standard limitations and is consistent with all known empirical constraints on scalar relativistic QM.

For relativistic scalar quantum mechanics specifically, the structural case is closed at the form level. The Klein-Gordon equation is forced. The mass-shell condition is forced. The minimal-coupling extension is forced. The conserved four-current is forced. The non-relativistic limit reduces cleanly to Schrödinger. The framework's primitive stack supports both regimes — non-relativistic (Schrödinger) and relativistic (Klein-Gordon) — as a single ontology applied at different velocity scales.

The next step, structurally, is the fermionic case: spin-1/2 chains, the Cl(3,1) algebraic structure forced from spinor representation theory, the Dirac equation as the unique first-order Lorentz-covariant equation on the spinor module, and the gyromagnetic ratio g = 2 emerging from the non-relativistic reduction without empirical tuning. That's the Dirac walkthrough. Klein-Gordon is the structural foundation it builds on.

---

## 11. References

- Klein, O. "Quantentheorie und fünfdimensionale Relativitätstheorie." *Zeitschrift für Physik* 37, 895–906 (1926).
- Gordon, W. "Der Comptoneffekt nach der Schrödingerschen Theorie." *Zeitschrift für Physik* 40, 117–133 (1926).
- Dirac, P. A. M. "The Quantum Theory of the Electron." *Proceedings of the Royal Society A* 117, 610–624 (1928).
- Bjorken, J. D. and Drell, S. D. *Relativistic Quantum Mechanics.* McGraw-Hill, 1964.
- Weinberg, S. *The Quantum Theory of Fields, Vol. 1.* Cambridge University Press, 1995.
- Peskin, M. E. and Schroeder, D. V. *An Introduction to Quantum Field Theory.* Westview Press, 1995.
- Proxmire, A. *Relativistic Participation-Measure Scoping (Arc R, Stage R.0).* April 2026.
- Proxmire, A. *Klein-Gordon Emergence (Arc R, Stage R.1).* April 2026.
- Proxmire, A. *Klein-Gordon Minimal Coupling and Conserved Four-Current (Arc R, Stage R.1 follow-up).* April 2026.
- Proxmire, A. *Event Density Foundations: A Unified Substrate Architecture for Quantum, Fluid, Gauge, and Gravitational Dynamics.* April 2026.
- The full Event Density corpus, including all forced theorems and supporting memos, is available at https://github.com/allen-proxmire/event-density.
