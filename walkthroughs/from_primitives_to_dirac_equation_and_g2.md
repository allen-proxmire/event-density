# From Primitives to the Dirac Equation and g = 2

## A Walkthrough of the Event Density Spinor Wave Equation Derivation

**Allen Proxmire** · May 2026

---

## 1. The Question

The electron has a magnetic moment. It also has spin angular momentum. The ratio between them — the gyromagnetic ratio g — was one of the great surprises of early quantum mechanics. For a classical charged sphere with mass m and charge q rotating uniformly, the calculation gives g = 1: the magnetic moment is qℏ/(2m) times the spin in units of $\hbar$/2. For the electron, measurements give g ≈ 2.

That factor of two is not small. It is exact (to leading order, with corrections of order α/π ≈ 10⁻³ from quantum electrodynamics, but those are radiative corrections to a leading value of exactly 2). The discrepancy with the classical prediction is large enough that it forced a rethinking of how angular momentum and electromagnetic coupling work at the quantum level.

In 1928, Paul Dirac wrote down a relativistic wave equation for the electron — a first-order equation, unlike the second-order Klein-Gordon equation, requiring the wavefunction to have four components rather than one. The Dirac equation:

$$
(i\gamma^\mu \partial_\mu − mc/\hbar)\Psi= 0
$$

uses four matrices γ^μ satisfying the anticommutation relation {γ^μ, γ^ν} = 2η^μν · 𝟙. When you take the non-relativistic limit of the Dirac equation, you get the Pauli equation — the Schrödinger equation augmented with a Zeeman term that couples the electron's spin to an external magnetic field. The Zeeman coefficient is qℏ/(2m), corresponding to g = 2 exactly.

This was a triumph. The factor of two that had baffled experimenters for years fell out of the relativistic structure of the electron's wave equation, with no empirical tuning. Dirac's derivation forced g = 2 from first principles — but the first principles were Lorentz covariance plus the specific algebraic structure of the gamma matrices. Where did the gamma matrices come from? Dirac's original argument was operational: he wanted to take the square root of the Klein-Gordon equation, and the gamma matrices were what he needed to make the square root work. The algebraic structure was a means to an end.

The Event Density framework derives g = 2 from substrate primitives. The chain runs through several structural moves, each forced by primitive-level commitments rather than postulated:

The configuration space of two identical fermionic chains in three spatial dimensions has fundamental group $\pi_1$(Q_2) = ℤ_2. This forces the exchange phase η ∈ {+1, −1} — no continuous anyonic phases.

Half-integer spin representations of the Lorentz group require the double cover SL(2, ℂ), not just SO⁺(3,1). The 2π-rotation generator in SL(2, ℂ) is non-trivial: it acts as −𝟙 on half-integer representations.

The unique finite-dimensional real algebra compatible with Lorentz covariance, the metric structure, and half-integer representation content is the real Clifford algebra Cl(3,1). The defining anticommutation relation {γ^μ, γ^ν} = 2η^μν · 𝟙 is forced — neither pure commutation nor pure antisymmetry works.

The γ^μ realize the algebraic frame at the rule-type interface. The Lorentz generators σ^μν = (i/2)[γ^μ, γ^ν] generate SL(2, ℂ), and the half-angle factor in exp(−(i/2)θσ^12) makes 2π rotations act as −𝟙 automatically — no tuning.

The Dirac equation emerges as the unique first-order Lorentz-covariant linear equation on the spinor module that uses the Cl(3,1) frame structure non-trivially. The operator factorization (iγ^μ∂_μ − mc/$\hbar$)(iγ^μ∂_μ + mc/$\hbar$) = −(□ + m²c²/ℏ²) shows that solutions of the Dirac equation also satisfy Klein-Gordon component-wise.

Local U(1) gauge invariance forces minimal coupling D_μ = ∂_μ + (iq/$\hbar$)A_μ exactly as in the Klein-Gordon case, producing the interacting Dirac equation.

The conserved current j^μ = Ψ̄γ^μΨ is real, gauge-invariant, and has positive-definite density j^0 = Ψ†Ψ. This resolves the Klein-Gordon negative-density pathology at the spinor level.

The non-relativistic limit, via the same rest-energy factorization that worked for Klein-Gordon, gives the Pauli equation:

$$
i\hbar \partial_t\varphi= [(p − qA)^{2}/(2m) + qA^0 − (q\hbar /2m) \sigma \cdot B] \varphi
$$

The Zeeman coefficient is qℏ/(2m). This is g = 2.

The structural payoff: the gyromagnetic ratio of the electron is what falls out when you push the framework's substrate ontology — discreteness, finite participation bandwidth, commitment irreversibility, polarity, and the rule-type taxonomy distinguishing bosonic from fermionic chains — through the relativistic regime to the spin-1/2 case. No empirical inputs other than the chain mass m, charge q, and the universal constants $\hbar$, c. The half-angle factor in exp(−(i/2)θσ^12), which makes 2π rotations act as −𝟙 automatically, is the structural source of the factor of two.

This is one of the framework's clearest empirical wins. The electron's gyromagnetic ratio is one of the most precisely measured quantities in physics. The framework derives it from substrate primitives without empirical tuning.

The chain has seven structural moves, each forced. That's the walkthrough.

---

## 2. The Substrate Ontology, Made Relativistic and Spinor-Capable

The framework rests on substrate-level ontological commitments, the same primitives that gave the Born rule, the Schrödinger equation, the Klein-Gordon equation. The Dirac walkthrough adds two pieces: the rule-type taxonomy distinguishing bosonic from fermionic chains, and the spinor extension of the participation measure for fermionic rule-types.

**Micro-events, chains, channels, bandwidth.** Reality consists of discrete acts of becoming. Chains hold these together via persistent rules. Channels are the substrate's adjacency-mediated communication structure. Bandwidth measures local participation density and decomposes into four bands: internal rule-bandwidth, adjacency, environmental, and commitment-reserve. (Same as in the Klein-Gordon walkthrough.)

**Worldlines and proper time.** A chain becomes a worldline x^μ(τ) parameterized by proper time τ in Minkowski spacetime. Lorentz invariance of proper time preserves chain identity across reference frames.

**Lorentz-covariant participation measure.** The participation measure is a function on spacetime events:

$$
P_K(x^\mu) = \sqrt(b_K(x^\mu)) \cdot e^{i\pi_K(x^\mu}) \in \mathbb{C}
$$

For a bosonic rule-type, P_K transforms as a Lorentz scalar. For a fermionic rule-type, P_K carries an internal index α and transforms under the spinor representation of the Lorentz group:

$$
P_{K,\alpha}(x^\mu) \to S(\Lambda)_\alpha^\beta P_{K,\beta}(\Lambda^(−1)x'^\mu)
$$

The distinction between scalar and spinor transformation comes from the rule-type taxonomy.

**Rule-type taxonomy.** The framework's rule-type primitive (Primitive 07) classifies chains into structurally distinct categories. The taxonomy distinguishes two cases under exchange symmetry: Case P, where the rule-type's bandwidth content interacts symmetrically with the individuation threshold under two-chain exchange (η = +1, bosonic), and Case R, where it interacts antisymmetrically (η = −1, fermionic).

This is the same Case P / Case R distinction that produces the bosonic / fermionic split. Bosonic chains carry scalar participation measures and satisfy Klein-Gordon (the previous walkthrough). Fermionic chains carry spinor participation measures and satisfy the Dirac equation (this walkthrough). The structural difference between the two arises from how the rule-type interacts with the substrate's individuation structure.

**The four primitive reformulations.** Same as in the Klein-Gordon walkthrough: chain → worldline, four-band → covariant Lorentz-scalar fields, ED gradient → four-gradient ∂_μ, relational timing → proper-time phase coupling. All forced by Lorentz invariance, none introducing a new primitive.

**No new primitives for the Dirac extension.** The substrate ontology is the same. What changes is which sector of the rule-type taxonomy a given chain belongs to — bosonic or fermionic — and that determines whether the participation measure is scalar or spinor-valued.

That's the working set. From here, the chain to the Dirac equation runs through configuration-space topology, the rotational double cover, the Cl(3,1) algebra, and the square-root factorization.

---

## 3. The Configuration-Space Topology Forces the Double Cover

The first structural move establishes that the framework's primitive stack, applied to two identical fermionic chains in 3+1D spacetime, forces the existence of a non-trivial double cover. This is what makes half-integer spin structurally available.

### 3.1 The two-chain configuration space

Consider two identical (same-rule-type) chains at positions x_1, x_2 ∈ ℝ³ on a constant-time slice. Their classical configuration space, with the two chains regarded as interchangeable (since they are the same rule-type), is:

$$
Q_2 = (\mathbb{R}^{3} \times \mathbb{R}^{3} \ \Delta) / S_2
$$

where Δ = {(x, x) : x ∈ ℝ³} is the diagonal where the two chains coincide (excluded for fermionic rule-types because Primitive 10's individuation threshold forbids same-type coincidence in Case R), and S_2 is the symmetric group acting by exchange.

For fermionic chains the diagonal is excluded; the configuration space is non-trivial.

### 3.2 Computing $\pi_1$(Q_2)

Introduce center-of-mass and relative coordinates:

$$
R = (x_1 + x_2)/2
r = x_1 − x_2 \in \mathbb{R}^{3} \ {0}
$$

The S_2 action sends R → R and r → −r. So:

$$
Q_2 ≃ \mathbb{R}^{3} \times(\mathbb{R}^{3} \ {0}) / \mathbb{Z}_2
$$

The ℝ³ factor is contractible. The quotient (ℝ³ \ {0})/ℤ_2 deformation-retracts onto ℝP² (since ℝ³ \ {0} retracts onto S², and the antipodal quotient of S² is ℝP²). Therefore:

$$
\pi_1(Q_2) = \pi_1(\mathbb{R}P^{2}) = \mathbb{Z}_2
$$

This is a topological theorem with three inputs:

The ambient spatial dimension is 3. (From Primitive 02 — chains live in 3+1D spacetime.)

Two same-type chains exchange via continuous paths. (From Primitive 11 — commitment dynamics produces continuous evolution.)

Same-type coincidence is excluded for fermionic chains. (From Primitive 10 — individuation threshold for Case R.)

No further structure is needed. The result $\pi_1$(Q_2) = ℤ_2 is forced.

### 3.3 Why this forces η ∈ {+1, −1}

A 1D unitary representation of ℤ_2 is a homomorphism ℤ_2 → U(1). There are exactly two:

The trivial homomorphism: generator ↦ +1. (Bosonic exchange phase.)

The sign homomorphism: generator ↦ −1. (Fermionic exchange phase.)

No phase e^(iθ) with θ ≠ 0, π is a valid 1D representation of ℤ_2. Continuous anyonic exchange phases are forbidden in 3+1D.

This is a structural theorem. The framework's commitment to 3+1D spacetime, combined with continuous exchange paths and the rule-type taxonomy producing two cases, forces the dichotomy η ∈ {+1, −1} at the topological level.

(In 2+1D, the configuration-space $\pi_1$ is ℤ — the braid group — with U(1) representations forming a circle. This permits anyons. The framework's commitment to 3+1D collapses ℤ to ℤ_2 because the spatial dimension is high enough for exchange paths to "unknot.")

### 3.4 The exchange path as a 2π rotation

Consider two identical chains at positions ±r_0 on the x-axis. The exchange path is a continuous trajectory x_1(s), x_2(s) for s ∈ [0, 1] with x_1(0) = −r_0 and x_2(0) = +r_0, ending with x_1(1) = +r_0 and x_2(1) = −r_0, and avoiding coincidence throughout.

The canonical such path rotates the line segment joining x_1 and x_2 by π about an axis perpendicular to the segment. A geometric fact (familiar from the Dirac belt trick and similar constructions): this π-rotation of an unframed segment corresponds to a 2π rotation of the relative-coordinate frame. The segment without orientation returns to itself after π; a framed segment returns only after 2π.

More precisely: the exchange path represents the non-trivial class of $\pi_1$(Q_2) = ℤ_2. Under the SO(3)-equivariant identification of the relative coordinate, the exchange-class generator maps to the 2π-rotation generator in $\pi_1$(SO(3)) = ℤ_2. Both are the non-trivial element of ℤ_2.

So:

$$
Exchange generator in \pi_1(Q_2) \equiv 2\pi -rotation generator in \pi_1(SO(3))
$$

Both are the same ℤ_2 generator. This is a geometric theorem, not a postulate.

### 3.5 The double cover

The group SO⁺(3,1) (the proper orthochronous Lorentz group) has fundamental group $\pi_1$(SO⁺(3,1)) = ℤ_2. Its universal cover is SL(2, ℂ), the double cover. Two elements of SL(2, ℂ) project onto each element of SO⁺(3,1).

A representation D of SL(2, ℂ) descends to a representation of SO⁺(3,1) if and only if D(−𝟙) = +𝟙 on the internal index space, where −𝟙 ∈ SL(2, ℂ) is the non-trivial element of the kernel of the covering map.

Lorentz representations are classified by pairs (j_L, j_R) with j_L, j_R ∈ {0, 1/2, 1, 3/2, ...}. The (j_L, j_R) representation has D(−𝟙) = (−1)^(2(j_L + j_R)). So:

If j_L + j_R is integer (scalar, vector, rank-2 tensor, etc.): D descends to SO⁺(3,1). These are "true" Lorentz representations.

If j_L + j_R is half-integer (Weyl spinor, Dirac spinor, Rarita-Schwinger, etc.): D does not descend. These are representations of SL(2, ℂ) only.

Half-integer representations are structurally available if and only if SL(2, ℂ) is the framework's admissible covariance group. The framework's primitive stack, applied to two-chain exchange in 3+1D with the individuation structure forbidding fermionic coincidence, produces $\pi_1$ = ℤ_2 forcing exchange phases η ∈ {+1, −1}, with the exchange-class generator identified with the 2π-rotation generator. This forces SL(2, ℂ) as the admissible covariance group for fermionic rule-types.

### 3.6 Status

Configuration-space topology in 3+1D forces $\pi_1$(Q_2) = ℤ_2 from substrate primitives plus 3+1D spatial structure. This forbids continuous anyonic phases and forces η ∈ {+1, −1}.

The exchange-class generator is identified with the 2π-rotation generator in SO(3) by a geometric theorem.

Half-integer Lorentz representations require the double cover SL(2, ℂ). For fermionic rule-types, the substrate's individuation structure forces this double cover to be the admissible covariance group.

These are forced. The double cover is structurally available, not postulated.

---

## 4. The Cl(3,1) Algebra Forced

The next structural move identifies the unique algebraic structure that realizes half-integer Lorentz representations at the rule-type interface. The result: the real Clifford algebra Cl(3,1), with the defining anticommutation relation {γ^μ, γ^ν} = 2η^μν · 𝟙. This relation is forced — neither pure commutation nor pure antisymmetry works.

### 4.1 The algebraic problem

Pose the problem in algebraic terms. Seek a real, finite-dimensional associative algebra 𝒜 with:

(P1) **Lorentz tangent-space compatibility.** 𝒜 contains a four-dimensional real subspace V spanned by elements {e_0, e_1, e_2, e_3} that transform as a Lorentz four-vector under a representation ρ: SL(2, ℂ) → Aut(𝒜).

(P2) **Metric compatibility.** The symmetric bilinear combination e_μe_ν + e_νe_μ reproduces the Lorentz metric η_μν · 𝟙_𝒜 (up to an overall real scale), so the algebra encodes the metric structure from Primitive 06.

(P3) **Half-integer representation realization.** The adjoint action of 𝒜 on a faithful module of 𝒜 contains a representation of SL(2, ℂ) of half-integer (j_L, j_R) type — equivalently, a representation on which D(R(2π)) = −𝟙.

(P4) **Minimal dimension.** 𝒜 is the smallest among algebras satisfying (P1)–(P3).

(P1) and (P2) transcribe the framework's Primitive 06 covariance and metric content into algebraic language. (P3) is the half-integer requirement forced by the configuration-space topology argument of Section 3. (P4) is Occam at the structural level — no superfluous representation content.

### 4.2 The anticommutation relation is forced

Suppose (P2) is satisfied with a commutation relation:

$$
e_\mu e_\nu= e_\nu e_\mu
$$

Then the only symmetric bilinear on V taking values in 𝟙 is the symmetric product, and (P2) reduces to e_μe_ν = (η_μν/2) · 𝟙 for all μ, ν. This forces e_μ = 0 for μ ≠ ν, and the diagonal products are rigid scalars. The resulting algebra is the quotient of the polynomial ring by these relations, which does not support non-trivial SL(2, ℂ) representations of half-integer type. (P3) fails.

Suppose alternatively that:

$$
e_\mu e_\nu= −e_\nu e_\mu
$$

strictly (purely antisymmetric). Then e_μe_μ = 0 for each μ — there are no squared elements. (P2) with diagonal η fails: it would require e_μe_μ = η_μμ · 𝟙 ≠ 0, contradicting e_μe_μ = 0.

The only remaining possibility is a mixed relation:

$$
e_\mu e_\nu + e_\nu e_\mu= 2\eta_\mu \nu \cdot 𝟙
$$

This is the defining relation of the real Clifford algebra Cl(3,1). (P2) reduces to it exactly, with the factor 2 being conventional.

The anticommutator — not the commutator — is the structurally mandatory pairing. Pure commutation collapses the algebra to triviality. Pure antisymmetry contradicts the metric. The Clifford anticommutator is the unique algebraic structure compatible with Lorentz covariance, the metric, and half-integer representation content.

### 4.3 Uniqueness up to isomorphism

The real Clifford algebra Cl(3,1) is unique up to isomorphism once the metric signature is fixed. As a real algebra it is isomorphic to the 4×4 real matrix algebra M_4(ℝ). Its dimension as a real vector space is 2^4 = 16, with grading:

$$
{𝟙, \gamma^\mu, \gamma^\mu \nu, \gamma^\mu \nu \rho, \gamma^5} = {1 scalar, 4 vectors, 6 bivectors, 4 trivectors, 1 pseudoscalar}
$$

This is the exhaustive grading. The 16-dimensional Fierz basis spans every Lorentz-covariant local pairing available from two spinors — nothing further is generated.

### 4.4 Status

Under (P1) plus (P2), the generator algebra is forced to be Cl(3,1) up to convention. The anticommutator structure is structurally mandatory.

The 16-dimensional Fierz basis exhausts admissible Lorentz-covariant bilinears.

The complex Clifford algebra Cl(3,1)_ℂ ≅ M_4(ℂ) used in practical Dirac calculations is a tool, not a structural commitment; the primitive-level algebra is real Cl(3,1).

Cl(3,1) is forced.

---

## 5. The γ Frame and the Half-Angle Factor

With the Cl(3,1) algebra in hand, identify e_μ ≡ γ^μ. Then {γ^μ} is a four-component object transforming as a Lorentz vector (by P1) and squaring via the anticommutator to the metric. This is precisely a local tetrad at the rule-type interface — an orthonormal frame in which inner products reproduce η_μν.

The γ^μ are not a superimposed structure. They are the generating set of the minimal algebra compatible with Primitive 06 plus half-integer representation content. The frame is forced.

### 5.1 The Lorentz generators

Define:

$$
\sigma^\mu \nu \equiv(i/2)[\gamma^\mu, \gamma^\nu]
$$

Using the anticommutation relation {γ^μ, γ^ν} = 2η^μν · 𝟙, direct computation gives:

$$
[\sigma^\mu \nu, \sigma^\rho \sigma] = i(\eta^\mu \rho \sigma^\nu \sigma − \eta^\nu \rho \sigma^\mu \sigma − \eta^\mu \sigma \sigma^\nu \rho + \eta^\nu \sigma \sigma^\mu \rho)
$$

This is the Lorentz-algebra commutation relation. Therefore {σ^μν} generate a representation of the Lie algebra so(3,1) on the 4-dimensional spinor module of Cl(3,1). Exponentiation:

$$
S(\Lambda) = \exp(−(i/4) \omega_\mu \nu \sigma^\mu \nu)
$$

for a finite Lorentz transformation parameterized by the antisymmetric tensor ω_μν produces a representation of the Lorentz group.

Crucially, because σ^μν are quadratic in γ^μ, the exponent S(Λ) generates not SO⁺(3,1) directly but its double cover SL(2, ℂ) acting on the spinor module. This is the standard Dirac-spinor construction, now grounded at substrate level.

### 5.2 The 2π sign falls out automatically

Consider a pure spatial rotation by angle θ about the z-axis: $\omega_1$2 = θ, others zero. Then:

$$
U(\theta) = \exp(−(i/2) \theta \sigma^12)
$$

Using (σ^12)² = 𝟙 on the 4-dimensional spinor module (direct computation from the anticommutation relation):

$$
U(\theta) = \cos(\theta /2) \cdot 𝟙 − i \sin(\theta /2) \cdot \sigma^12
$$

At θ = 2π:

$$
U(2\pi) = \cos(\pi) \cdot 𝟙 − i \sin(\pi) \cdot \sigma^12 = −𝟙
$$

At θ = 4π:

$$
U(4\pi) = +𝟙
$$

So D(R(2π)) = −𝟙 on the spinor module automatically. The half-angle factor in U(θ) is structurally forced by σ^μν being quadratic in γ^μ and the γ^μ anticommuting — there is no tuning.

This half-angle factor is the structural origin of the factor of two in g = 2. The 2π-rotation acts as −𝟙 on spinor states because the σ^μν generators are quadratic in the Cl(3,1) anticommuting elements, producing an exp(−iθ/2) form rather than an exp(−iθ) form. This same factor of 1/2 appears in the spin-orbit coupling and in the Pauli equation's Zeeman term, where it produces the factor of 2 in the gyromagnetic ratio.

### 5.3 Status

γ^μ is the algebraic frame at the rule-type interface, forced by the Cl(3,1) algebra.

σ^μν = (i/2)[γ^μ, γ^ν] generates SL(2, ℂ) on the spinor module.

D(R(2π)) = −𝟙 on the spinor module automatically. The half-angle factor in exp(−(i/2)θσ^12) is forced by the quadratic structure of σ^μν in the Cl(3,1) anticommuting generators.

This is the structural source of the factor of 2 in g = 2. It will reappear in Section 8 when the non-relativistic limit produces the Pauli equation.

---

## 6. The Dirac Equation Forced

With the Cl(3,1) frame in hand and the spinor module identified, derive the Dirac equation.

### 6.1 The spinor participation measure

For a fermionic rule-type, the participation measure is a spinor-valued field:

$$
\Psi_\alpha(x^\mu), \alpha= 1, 2, 3, 4
$$

on the 4-dimensional Cl(3,1) spinor module. α indexes the internal (spinor) index; x^μ is the ambient spacetime coordinate. Under Lorentz transformations:

$$
\Psi(x) \to S(\Lambda) \Psi(\Lambda^(−1) x)
$$

with S(Λ) = exp(−(i/4) ω_μν σ^μν) ∈ SL(2, ℂ).

The Dirac adjoint is Ψ̄ ≡ Ψ†γ^0 (forced by the metric signature; the γ^0 factor ensures Ψ̄Ψ is a Lorentz scalar).

### 6.2 The square-root factorization

Each spinor component satisfies Klein-Gordon component-wise:

$$
(□ + m^{2}c^{2}/\hbar^{2})\Psi_\alpha= 0
$$

But this is a second-order equation, and a second-order equation on a spinor field does not use the Cl(3,1) frame structure non-trivially. It is blind to the γ^μ generators.

Section 4 established that γ^μ are structurally present at the fermionic rule-type interface. A dynamical equation that uses this structure must be first-order in ∂_μ and must contain the γ^μ.

Consider the operator iγ^μ∂_μ. Squaring:

$$
(i\gamma^\mu \partial_\mu)(i\gamma^\nu \partial_\nu) = −\gamma^\mu \gamma^\nu \partial_\mu \partial_\nu
= −(1/2){\gamma^\mu, \gamma^\nu}\partial_\mu \partial_\nu − (1/2)[\gamma^\mu, \gamma^\nu]\partial_\mu \partial_\nu
= −\eta^\mu \nu \cdot 𝟙 \partial_\mu \partial_\nu − 0
= −□
$$

The commutator term vanishes because ∂_μ∂_ν is symmetric in μ↔ν while [γ^μ, γ^ν] is antisymmetric — symmetric times antisymmetric integrates to zero.

Therefore:

$$
(i\gamma^\mu \partial_\mu − mc/\hbar)(i\gamma^\mu \partial_\mu + mc/\hbar) = −□ − m^{2}c^{2}/\hbar^{2} = −(□ + m^{2}c^{2}/\hbar^{2})
$$

If Ψ satisfies the first-order equation:

$$
(i\gamma^\mu \partial_\mu − mc/\hbar)\Psi= 0
$$

then applying (iγ^μ∂_μ + mc/$\hbar$) from the left gives:

$$
(−□ − m^{2}c^{2}/\hbar^{2})\Psi= 0 \iff(□ + m^{2}c^{2}/\hbar^{2})\Psi= 0
$$

Each component of Ψ satisfies Klein-Gordon. The first-order equation is the Dirac equation.

### 6.3 Three forcing arguments for the first-order form

Three independent arguments force the first-order Dirac form over component-wise Klein-Gordon for fermionic chains.

**(A) Use of the Cl(3,1) structure.** Section 4 established γ^μ as primitive-level frame generators at the fermionic rule-type interface. A dynamical equation that does not contain γ^μ leaves this structure inert. The Dirac equation is the unique Lorentz-covariant first-order linear operator on Ψ constructible from γ^μ, ∂_μ, and a mass scale.

**(B) Single time-derivative for positive-norm evolution.** Klein-Gordon as a second-order equation on the spinor module gives a Klein-Gordon inner product that is indefinite (negative-energy / negative-norm sector). The first-order Dirac form is needed for a positive-definite current (see Section 7) and for a Hilbert-space evolution compatible with the Phase-1 participation-measure inner product structure.

**(C) Half-integer representation content.** Klein-Gordon is the natural equation for the (0,0) representation. For the (1/2, 0) ⊕ (0, 1/2) Dirac spinor module, the minimal covariant first-order equation using the Cl(3,1) frame is exactly the Dirac equation. This is a Lorentz-representation-theoretic statement: the Dirac equation is the unique (up to equivalence) first-order Lorentz-covariant wave equation on the Dirac spinor module.

Given Section 4 (Cl(3,1) frame at fermionic rule-type interfaces) and the Klein-Gordon foundation (each spinor component satisfies KG), the Dirac equation is the unique structurally admissible first-order dynamical equation for fermionic participation measures.

### 6.4 Dimensional consistency

Rewriting the Dirac equation in SI-standard form:

$$
(i\hbar \gamma^\mu \partial_\mu − mc) \Psi= 0
$$

Here $\hbar$, m, c enter as dimensional anchors inherited from the framework's Dimensional Atlas — $\hbar$ from the QM-emergence sector (the Schrödinger walkthrough's U3 derivation), m from the rule-type's empirical mass content, c from the Lorentz metric normalization. The form of the equation is forced; the numerical values are inherited.

### 6.5 Status

The Dirac equation (iγ^μ∂_μ − mc/$\hbar$)Ψ = 0 is forced by the Cl(3,1) frame plus three independent structural arguments (use of the frame, positive-norm evolution, unique first-order Lorentz-covariant equation on the spinor module).

Each spinor component satisfies Klein-Gordon by the operator factorization.

The Dirac equation is structurally complete for free-particle fermionic dynamics.

---

## 7. Minimal Coupling and the Conserved Current

### 7.1 Minimal coupling

The minimal-coupling prescription from the Klein-Gordon walkthrough extends to Dirac unchanged. Local U(1) gauge invariance — phase rotations Ψ → e^(iqα(x)/$\hbar$)Ψ varying across spacetime — forces:

$$
\partial_\mu \to D_\mu= \partial_\mu + (iq/\hbar)A_\mu
$$

Substituting into the Dirac equation:

$$
(i\gamma^\mu D_\mu − mc/\hbar)\Psi= 0
$$

equivalently:

$$
(i\hbar \gamma^\mu \partial_\mu − q\gamma^\mu A_\mu − mc) \Psi= 0
$$

Under local U(1), Ψ(x) → e^(iqα(x)/$\hbar$)Ψ(x) and A_μ(x) → A_μ(x) − ∂_μα(x). Then D_μΨ → e^(iqα/$\hbar$)D_μΨ (the standard computation from the Klein-Gordon walkthrough). The Dirac equation transforms as:

$$
(i\gamma^\mu D_\mu − mc/\hbar)\Psi \to e^{iq\alpha /\hbar} \cdot(i\gamma^\mu D_\mu − mc/\hbar)\Psi= 0
$$

The equation is gauge-covariant. The argument is structurally identical to the Klein-Gordon case — the spinor index is untouched by the U(1) phase rotation, so the gauge-covariant derivative works the same way.

### 7.2 The conserved current

Multiply the Dirac equation from the left by Ψ̄:

$$
\Psi ̄ i\gamma^\mu D_\mu \Psi= (mc/\hbar) \Psi ̄ \Psi
$$

Take the Hermitian conjugate of the Dirac equation. Using (γ^μ)† = γ^0 γ^μ γ^0 (a standard identity from the metric signature) and multiplying by γ^0 from the right gives the adjoint equation:

$$
\Psi ̄ (i\gamma^\mu D̄_\mu + mc/\hbar) = 0
$$

with D̄_μ the conjugate covariant derivative acting to the left.

Subtracting Ψ̄ multiplied into the adjoint equation from Ψ̄ multiplied into the original, the mass terms cancel, leaving:

$$
\partial_\mu(\Psi ̄ \gamma^\mu \Psi) = 0
$$

The current:

$$
j^\mu \equiv \Psi ̄ \gamma^\mu \Psi
$$

is conserved: ∂_μ j^μ = 0.

### 7.3 Positive-definite density

The time component:

$$
j^0 = \Psi ̄ \gamma^0 \Psi= \Psi † \gamma^0 \gamma^0 \Psi= \Psi † \Psi= \sum_\alpha|\Psi_\alpha|^{2} \geq 0
$$

This is positive-definite, unlike the Klein-Gordon current's j^0 which is indefinite.

The Dirac current gives a bona fide probability density (or participation-measure-amplitude density) at the single-particle level. The Klein-Gordon negative-density pathology — j^0 not positive-definite, blocking the single-particle probability interpretation — is resolved at the spinor level. This is one of the structural advantages of the Dirac equation over Klein-Gordon for fermionic chains.

The structural origin: the first-order form of Dirac, with its single time-derivative, produces a current that is sesquilinear in Ψ rather than involving Ψ*∂_tΨ − Ψ∂_tΨ*. The sesquilinear form is positive-definite. The Klein-Gordon form, with second time-derivatives, requires the antisymmetric combination Ψ*∂_tΨ − Ψ∂_tΨ* for the current, and that combination is indefinite.

### 7.4 Status

The conserved current j^μ = Ψ̄γ^μΨ is gauge-invariant, real, and satisfies ∂_μj^μ = 0 as a direct algebraic consequence of the Dirac equation.

The density j^0 = Ψ†Ψ is positive-definite, resolving the Klein-Gordon negative-density pathology for fermionic chains.

This is forced.

---

## 8. The Non-Relativistic Limit and g = 2

The structural payoff of the Dirac walkthrough: non-relativistic reduction produces the Pauli equation, with Zeeman coefficient (qℏ/2m) corresponding to g = 2 exactly.

### 8.1 Setup

Write the four-component Dirac spinor as a pair of two-component Pauli spinors:

$$
\Psi= (\varphi, \chi)^T \cdot e^{−imc^{2}t/\hbar}
$$

where φ and χ are two-component Pauli spinors and the phase factor removes the rest-energy oscillation (the same rest-energy factorization that worked for Klein-Gordon).

In the standard Dirac representation, the gamma matrices are:

$$
\gamma^0 = diag(𝟙, −𝟙) (block structure on 2 \times 2 blocks)
\gamma^i = ((0, \sigma^i), (−\sigma^i, 0)) (off-diagonal with Pauli matrices)
$$

where σ^i are the 2×2 Pauli spin matrices.

The Dirac equation becomes a coupled system for φ and χ.

### 8.2 First-order elimination of χ

In the non-relativistic limit, χ is small (of order v/c) compared to φ. The Dirac equation produces an algebraic equation for χ at lowest order:

$$
\chi \approx(1/2mc) \sigma \cdot(p − qA) \varphi
$$

Substituting back into the equation for φ, keeping terms to lowest non-trivial order in v/c, the resulting equation is the Pauli equation:

$$
i\hbar \partial_t \varphi= [(p − qA)^{2}/(2m) + qA^0 − (q\hbar /2m) \sigma \cdot B] \varphi
$$

where B = ∇×A is the magnetic field and σ = (σ^1, σ^2, σ^3) is the Pauli spin vector.

This is the Schrödinger equation augmented by the Zeeman term −(qℏ/2m) σ·B coupling the spin to the magnetic field.

### 8.3 The gyromagnetic ratio

The Zeeman coefficient in the Pauli equation is (qℏ/2m). The general form of the Zeeman energy for a particle with spin S and gyromagnetic ratio g is:

$$
H_Zeeman = −g \cdot(q\hbar /2m) \cdot(S \cdot B / \hbar)
$$

For a spin-1/2 particle, S = ℏσ/2, so:

$$
H_Zeeman = −g \cdot(q\hbar /2m) \cdot(\sigma /2) \cdot B = −g \cdot(q\hbar /4m) \sigma \cdot B
$$

Comparing with the Dirac-derived result −(qℏ/2m) σ·B:

$$
g \cdot(q\hbar /4m) = q\hbar /2m
g = 2
$$

The gyromagnetic ratio is exactly 2. This is the Dirac prediction, confirmed by experiment (with quantum-electrodynamic corrections of order α/π that bring it to g ≈ 2.00231930... — the famous anomalous magnetic moment).

### 8.4 The structural origin of the factor of 2

The factor of 2 in g = 2 traces back to the half-angle factor in exp(−(i/2)θσ^12) from Section 5.2. The structural chain:

The Cl(3,1) anticommutation relation forces γ^μ to anticommute, making products γ^μγ^ν have specific symmetric/antisymmetric structure.

The Lorentz generators σ^μν = (i/2)[γ^μ, γ^ν] are quadratic in γ^μ.

The rotation operator U(θ) = exp(−(i/2)θσ^12) has a half-angle θ/2 because σ^μν appears with a factor of 1/2 in the exponential.

This same factor of 1/2 appears in the spin operator S = ($\hbar$/2)σ for spin-1/2, and in the magnetic moment μ = (g/2) · (qℏ/2m)σ.

The Dirac-derived Zeeman coefficient (qℏ/2m) corresponds to a magnetic moment per unit spin of (qℏ/2m), which when written in terms of S as (qℏ/m) · (S/$\hbar$) = (q/m)S corresponds to gyromagnetic ratio g = 2 because the classical formula gives $\mu_c$lassical = (q/2m)L for orbital angular momentum.

The factor of 2 in g comes from the factor of 2 difference between the half-angle structure of spin (where U(2π) = −𝟙 because of the σ/2) and the full-angle structure of orbital angular momentum (where U(2π) = +𝟙 from L). The half-angle is forced by Cl(3,1). Therefore g = 2 is forced by Cl(3,1).

This is the structural derivation of g = 2 from substrate primitives:

substrate primitives → 3+1D configuration-space topology → $\pi_1$(Q_2) = ℤ_2 → exchange-class generator equals 2π-rotation generator → SL(2, ℂ) is admissible covariance group for fermionic rule-types → Cl(3,1) is unique algebraic frame → σ^μν quadratic in γ^μ → half-angle in U(θ) = exp(−(i/2)θσ^12) → factor of 1/2 in spin operator → factor of 2 in gyromagnetic ratio of Dirac-derived Pauli equation.

No empirical input enters the structural chain other than the chain mass m, charge q, and universal constants $\hbar$, c. The factor of 2 in g = 2 is forced by substrate primitives plus 3+1D spatial structure.

### 8.5 Higher-order corrections

The Dirac result g = 2 is the leading order. Quantum electrodynamics produces radiative corrections:

$$
g = 2 + \alpha /\pi + O(\alpha^{2})
$$

with α ≈ 1/137 the fine-structure constant. The leading correction α/π was computed by Schwinger in 1948 and is one of the most precisely tested predictions in physics. Higher orders have been computed to tenth order in α and agree with experiment to about 10 significant figures.

The framework's Dirac walkthrough produces the leading-order g = 2 from substrate structure. Radiative corrections require the QFT extension (Arc Q in the framework's roadmap), which is open work.

### 8.6 Schrödinger consistency check

In the spinless limit — projecting onto a single Pauli component or ignoring the spin coupling — the Pauli equation reduces to:

$$
i\hbar \partial_t \psi= [(p − qA)^{2}/(2m) + qA^0] \psi
$$

This is the Schrödinger equation with electromagnetic coupling, exactly as derived in the Klein-Gordon walkthrough's non-relativistic limit and consistent with the Phase-1 Schrödinger walkthrough.

The framework's three regimes — non-relativistic (Schrödinger), relativistic scalar (Klein-Gordon), relativistic spinor (Dirac) — are mutually consistent. Each is recovered from the next as an appropriate limit. The framework is internally consistent across the QM-emergence territory.

### 8.7 Status

Non-relativistic reduction of the Dirac equation gives the Pauli equation with Zeeman coefficient (qℏ/2m).

This corresponds to gyromagnetic ratio g = 2 exactly. Forced.

The factor of 2 traces structurally to the half-angle in exp(−(i/2)θσ^12), which is forced by the Cl(3,1) anticommutation relation, which is forced by Lorentz covariance plus half-integer representation content, which is forced by configuration-space topology in 3+1D from substrate primitives.

Higher-order corrections (g = 2 + α/π + ...) require QFT machinery beyond present scope.

Spinless limit recovers Schrödinger with electromagnetic coupling, consistent with the Phase-1 walkthroughs.

---

## 9. What's Forced, What's Inherited, What's Open

The framework is honest about what its current machinery delivers and what remains future work.

**Forced at substrate level:**

The Lorentz-covariant participation measure on Minkowski spacetime, with the bosonic / fermionic split inherited from the rule-type taxonomy.

The configuration-space topology $\pi_1$(Q_2) = ℤ_2 in 3+1D from substrate primitives plus spatial dimension 3.

The exchange-phase dichotomy η ∈ {+1, −1} from the only 1D unitary representations of ℤ_2.

The identification of the exchange-class generator with the 2π-rotation generator.

The double cover SL(2, ℂ) as the admissible covariance group for fermionic rule-types.

The unique Clifford algebra Cl(3,1) with anticommutation relation {γ^μ, γ^ν} = 2η^μν · 𝟙 as the algebraic frame at the fermionic rule-type interface.

The Lorentz generators σ^μν = (i/2)[γ^μ, γ^ν] generating SL(2, ℂ) on the spinor module.

The half-angle factor in exp(−(i/2)θσ^12), making D(R(2π)) = −𝟙 automatic.

The first-order Dirac equation (iγ^μ∂_μ − mc/$\hbar$)Ψ = 0 by square-root factorization plus three independent forcing arguments.

The minimal-coupling extension D_μ = ∂_μ + (iq/$\hbar$)A_μ from local U(1) gauge invariance.

The conserved current j^μ = Ψ̄γ^μΨ with ∂_μj^μ = 0 as algebraic consequence.

The positive-definite density j^0 = Ψ†Ψ resolving the Klein-Gordon negative-density pathology for fermionic chains.

The Pauli equation as non-relativistic limit, with Zeeman coefficient (qℏ/2m).

The gyromagnetic ratio g = 2 exactly, traced structurally to the half-angle factor in the Cl(3,1) generators.

The Schrödinger consistency check in the spinless limit, recovering the Phase-1 result.

**Inherited at value layer:**

The chain mass m (species-level empirical input; chain-mass derivation is open work in the framework's Arc M).

The electromagnetic charge q (species-level empirical input).

The reduced Planck constant $\hbar$ (inherited via U3 from the Phase-1 framework).

The speed of light c (Lorentz invariance scale, inherited from the Minkowski metric normalization).

The choice of Dirac vs. Weyl vs. Majorana representation (algebraic refinement of Cl(3,1), not primitive-forced).

**Open or future arc work:**

**Mass origin.** The chain mass m is currently inherited; the framework's Arc M (chain-mass) is flagged as substantively explained in the corpus but not yet walkthrough-presented. Whether the framework derives specific mass values, structural mass-hierarchy form, or both is the most empirically substantive open question.

**Gauge group specification beyond U(1).** Non-Abelian gauge groups (SU(2), SU(3)) entering the Standard Model are not derived in this walkthrough. The structural machinery extends straightforwardly (local invariance forces Lie-algebra-valued covariant derivatives), but the specific gauge groups SU(3)×SU(2)×U(1) are content for the framework's gauge arc.

**QED radiative corrections.** The g = 2 + α/π + O(α²) correction series requires the QFT extension (Arc Q). The structural derivation gives leading order; radiative corrections need second-quantized field theory.

**Multi-particle and second quantization.** Particle creation and annihilation, Feynman rules, vacuum structure — all require Arc Q.

**Number of fermion generations.** Why three generations of quarks and leptons exist is open. The framework may address this via Arc M plus Arc Q.

**Yukawa couplings, CP violation, flavor mixing.** All Standard Model parameters beyond the basic spinor structure are inherited as empirical. Whether Arc M plus Arc Q can derive these is open work.

**Spin-statistics theorem.** The framework establishes that fermionic chains carry half-integer spin and exchange antisymmetrically. The full spin-statistics theorem η = (−1)^(2s) requires synthesis with locality / microcausality arguments that are content for the framework's R.2.5 stage, not derived in the present walkthrough.

---

## 10. What This Argument Establishes

The chain runs:

Primitives (micro-events, participation, chain stability landscape, rule-type taxonomy, individuation, polarity, commitment irreversibility, relational timing) → 3+1D spacetime (Primitive 02) → configuration-space topology $\pi_1$(Q_2) = ℤ_2 → exchange-phase dichotomy η ∈ {+1, −1} → identification of exchange generator with 2π-rotation generator → SL(2, ℂ) double cover as admissible covariance group for fermionic rule-types → Cl(3,1) as unique algebraic frame with anticommutation relation forced → γ^μ at fermionic rule-type interface → σ^μν generates SL(2, ℂ) on spinor module with half-angle factor making D(R(2π)) = −𝟙 → square-root factorization of Klein-Gordon component-wise → Dirac equation forced by three independent arguments → minimal coupling from local U(1) → conserved current with positive-definite density → non-relativistic reduction to Pauli equation with Zeeman coefficient (qℏ/2m) → gyromagnetic ratio g = 2 exactly.

Each move has its load-bearing argument worked out. The configuration-space topology is forced from substrate primitives plus 3+1D spatial structure. The Cl(3,1) algebra is the unique solution to a clearly-stated algebraic problem. The first-order Dirac form is forced by three independent arguments (use of frame, positive-norm evolution, unique covariant first-order equation). The g = 2 result falls out of the half-angle factor in the Cl(3,1) generators with no empirical tuning.

The framework reproduces the gyromagnetic ratio of the electron from substrate primitives.

The standard treatment of g = 2 derives it from the Dirac equation plus minimal coupling, taking the Dirac equation as a postulated input. The framework derives the Dirac equation itself from substrate structure, with each move forced by primitive-level commitments. The g = 2 prediction is then a structural consequence of substrate primitives plus 3+1D spatial topology — not a postulate, not a guess, but a forced result.

This is a clear empirical win for the framework. The electron's gyromagnetic ratio is one of the most precisely measured quantities in physics. The Dirac value g = 2 is reproduced exactly. Higher-order radiative corrections require the QFT extension and are open work, but the leading-order structural prediction is in hand and is correct.

What the framework does that standard treatments do not: it traces the factor of 2 in g = 2 to its substrate origin. The standard treatment treats g = 2 as a consequence of the Dirac equation's structure without saying where that structure comes from. The framework says it comes from the half-angle factor in the rotation operator on the spinor module, which comes from the Cl(3,1) anticommutation relation, which comes from the algebraic problem of finding a Lorentz-covariant frame compatible with half-integer representations, which comes from the configuration-space topology forcing the double cover, which comes from substrate primitives plus 3+1D spatial structure. The factor of 2 is not arbitrary. It is a structural consequence of the substrate's dimensionality and individuation properties.

Whether the substrate commitments are right is the load-bearing question, as in every walkthrough. The framework stands or falls on whether discreteness, finite participation bandwidth, commitment irreversibility, the rule-type taxonomy, and 3+1D spatial structure are the correct foundational concepts. The empirical exposure of the Dirac content is enormous: every measurement of the electron's gyromagnetic ratio, every test of relativistic spin-1/2 dynamics, every confirmation of fermionic exchange statistics in many-body systems. The framework reproduces this content and is consistent with all known experimental constraints.

For relativistic spinor quantum mechanics specifically, the structural case is closed at the form level. The Dirac equation is forced. The gyromagnetic ratio g = 2 is forced. The conserved current with positive-definite density is forced. The non-relativistic reduction to Pauli is forced. The Schrödinger consistency check in the spinless limit is forced. The framework's primitive stack supports the full QM-emergence territory — non-relativistic (Schrödinger), relativistic scalar (Klein-Gordon), relativistic spinor (Dirac) — as a single ontology applied at different velocity and rule-type regimes.

The next steps, structurally, involve mass (Arc M — possibly the most empirically substantive open territory in the framework), gauge structure beyond U(1) (gauge arc), and QFT (Arc Q — multi-particle content, radiative corrections, Standard Model parameters). The QM-emergence walkthroughs — Born, Schrödinger, Bell-Tsirelson, Heisenberg, Klein-Gordon, Dirac — establish the framework's foundational quantum content. Mass and the rest of the Standard Model are downstream.

---

## 11. References

- Dirac, P. A. M. "The Quantum Theory of the Electron." *Proceedings of the Royal Society A* 117, 610–624 (1928).
- Pauli, W. "Zur Quantenmechanik des magnetischen Elektrons." *Zeitschrift für Physik* 43, 601–623 (1927).
- Pauli, W. "The Connection Between Spin and Statistics." *Physical Review* 58, 716–722 (1940).
- Schwinger, J. "On Quantum-Electrodynamics and the Magnetic Moment of the Electron." *Physical Review* 73, 416–417 (1948).
- Weinberg, S. *The Quantum Theory of Fields, Vol. 1.* Cambridge University Press, 1995.
- Peskin, M. E. and Schroeder, D. V. *An Introduction to Quantum Field Theory.* Westview Press, 1995.
- Bjorken, J. D. and Drell, S. D. *Relativistic Quantum Mechanics.* McGraw-Hill, 1964.
- Proxmire, A. *Relativistic Participation-Measure Scoping (Arc R, Stage R.0).* April 2026.
- Proxmire, A. *Lorentz Representations from Primitives (Arc R, Stage R.2.2).* April 2026.
- Proxmire, A. *Rotational Double-Cover Scoping and Partial Derivation (Arc R, Stage R.2.3).* April 2026.
- Proxmire, A. *Clifford Algebra from Spinor Structure (Arc R, Stage R.2.4).* April 2026.
- Proxmire, A. *Dirac Emergence (Arc R, Stage R.3).* April 2026.
- Proxmire, A. *Event Density Foundations: A Unified Substrate Architecture for Quantum, Fluid, Gauge, and Gravitational Dynamics.* April 2026.
- The full Event Density corpus, including all forced theorems and supporting memos, is available at https://github.com/allen-proxmire/event-density.
