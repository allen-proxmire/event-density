# The V1 Finite-Width Vacuum Memory Kernel (Theorem N1) is FORCED

**Paper #18 of the Event Density Forcing Series (Wave 2, Paper 8)**

**Author:** Allen Proxmire
**Status:** Publication draft
**Date:** 2026-05-13
**Series:** Event Density (ED) Forcing Papers — Paper #18 of the program
**Genre:** Forcing paper. Standalone. Cold-reader accessible.

---

## Abstract

The vacuum response kernel — the structural object describing how a quantum field's vacuum responds to a localized perturbation — is normally treated in standard quantum field theory as either a δ-function (instantaneous, Markovian response, the textbook default) or as an infinite-bandwidth response requiring regularization at the UV scale. Neither limit is physically realized: δ-function response amplifies high-frequency contributions and produces UV divergences; infinite-bandwidth response violates Lorentz covariance and the substrate's finite-frequency content. This paper shows that, given the substrate conditions $\{C\}$ of the ED program and the results of Papers #1-#17, the vacuum memory kernel is **forced to lie in a finite-width admissible class**, bounded above by the δ-width refutation (C3 UV-FIN preservation) and bounded below by the infinite-width refutation (C1 Lorentz covariance). This is **Theorem N1** (also known as T8 in the program's theorem inventory): the V1 finite-width vacuum memory kernel. Primitive event-discreteness (P01) and proper-time finite intervals between commitment events (P13) jointly establish a substrate-level scale $\ell_\mathrm{ED}$ below which the kernel cannot resolve perturbations; UV-FIN (T7) inherited from Arc Q closes the upper bound on admissible widths. Specific functional realizations (V2 exponential, V3 power-law-below-critical-exponent, V4 multi-scale) are admissible within the V1 class but the class itself is uniquely forced. The result is the substrate-level structural foundation on which Papers #19 (V1 retarded support / kernel-level arrow of time), #20 (V5 cross-chain kernel), #21 (memory-kernel cascade), and the substrate-gravity / black-hole sectors all build.

---

## 1. Framing

### 1.1 What a vacuum memory kernel is

In standard quantum field theory, the vacuum response kernel $K_\mathrm{vac}(x - x')$ governs how a small perturbation $\delta P_\mathrm{matter}(x')$ to the matter content at spacetime point $x'$ produces a vacuum response at point $x$:
$$
\delta\langle b^\mathrm{env}\rangle_\mathrm{vac}(x) = \int K_\mathrm{vac}(x - x')\,\delta P_\mathrm{matter}(x')\,d^4x'.
$$
The kernel encodes the vacuum's memory of past perturbations and its spatial spread. Three structural questions:

1. **Is the kernel a δ-function?** If $K_\mathrm{vac}(x - x') = c_0\,\delta^4(x - x')$, the vacuum responds instantaneously at every spacetime resolution. This is the Markovian (no-memory) limit and is the default in textbook treatments of perturbative QFT.

2. **Does the kernel have finite spatial / temporal extent?** Non-δ kernels with finite extent (in time, space, or both) describe vacuum content with *memory*: the vacuum response at $x$ depends on perturbations at all $x'$ within some support region of $x$.

3. **What is the UV behavior?** In Fourier space, $\widetilde{K}_\mathrm{vac}(\omega, \mathbf{k})$ describes how the vacuum response is weighted across frequencies. A δ-function kernel gives constant weighting at all frequencies (including arbitrarily high frequencies); a finite-width kernel suppresses high-frequency contributions, regulating UV behavior at the substrate level.

The standard QFT treatment takes the δ-function limit as the natural starting point and adds regularization (dimensional regularization, lattice cutoff, Pauli-Villars, etc.) to handle UV divergences. The regularization is treated as a mathematical convenience: the "true" vacuum response is presumed to be δ-function-like, with the regularization providing computational tools.

### 1.2 The puzzle

Empirically, the universe exhibits finite vacuum-correlation properties:

- The Casimir effect produces a finite vacuum-energy difference between conducting plates at finite separations — a hallmark of finite-width vacuum response.
- QED vacuum polarization has a finite range, set by the inverse electron mass at low energies.
- Lattice QCD simulations show finite vacuum-correlation lengths at zero temperature.
- The cosmological constant problem (the discrepancy between QFT vacuum-energy predictions and the observed cosmological constant by $\sim 10^{120}$) arises in part because the δ-function vacuum-response assumption produces divergent zero-point energy.

All of these point at the same structural fact: nature exhibits finite vacuum-response width. The standard QFT treatment encodes this only through ad-hoc regularization; a substrate-level program should derive the finite-width structure from primitive commitments.

### 1.3 What this paper does

The Event Density (ED) framework supplies a substrate. Papers #1-#4 establish the participation measure, Born rule, inner product, and Schrödinger dynamics. Paper #5 establishes the gauge-field-as-rule-type structure (Theorem T17) and inherits UV-FIN (Theorem T7) — the substrate-level UV cutoff at the Planck scale. Papers #11-#17 cover the rest of the Wave 2 substrate-level QM foundation.

The present paper extends to the vacuum memory kernel. Given the substrate primitives plus UV-FIN (T7), it forces:

1. **Finite kernel width is structurally required**. δ-function vacuum response is refuted by UV-FIN preservation (C3): it amplifies high-frequency contributions and produces divergent loop integrals at the substrate level.

2. **Finite kernel width is bounded above**. Infinite-width vacuum response is refuted by Lorentz covariance (C1): it would correspond to non-causal vacuum response or violate substrate-level locality.

3. **Primitive event-discreteness (P01) and proper-time finite-intervals (P13)** jointly establish a substrate scale $\ell_\mathrm{ED}$ at which the kernel smoothing occurs. Below this scale, the substrate is not continuum-like; the kernel cannot resolve perturbations.

4. **The V1 admissible class** — finite-width Lorentz-covariant kernels with sub-power-law-2 decay and UV-FIN-compatible UV behavior — is the unique class consistent with C1/C2/C3 substrate constraints. This is **Theorem N1**.

5. **Specific functional forms within V1** (exponential V2, power-law V3-below-critical-exponent, multi-scale V4) are admissible realizations but are INHERITED from value-layer / empirical content; the V1 *class* is forced, but the specific *form* is not.

**Series context.** Papers #1-#17 establish the substrate-level foundation for non-relativistic single-particle QM + gauge structure. The present paper opens the **kernel sector** of Wave 2: substrate-level structures governing vacuum response, memory, retarded support, and cross-chain correlations. Paper #19 will force the retarded support of V1 (kernel-level arrow of time, T18); Paper #20 the V5 cross-chain correlation kernel; Paper #21 the full memory-kernel cascade. These build directly on the V1-class forcing of the present paper.

---

## 2. Claim

> **Forcing Theorem (V1 Finite-Width Vacuum Memory Kernel; Theorem N1).** Let any substrate satisfy the conditions $\{C\}$ stated in §5. Then the vacuum response kernel $K_\mathrm{vac}(x - x')$ in flat spacetime is FORCED to lie in the **V1 admissible class** — finite-width Lorentz-covariant kernels with sub-power-law-2 decay, UV-FIN-compatible UV behavior, and natural smoothing at the substrate-level scale $\ell_\mathrm{ED}$:
> $$
> K_\mathrm{vac}(x - x') = K_\mathrm{vac}^\mathrm{prim}((x - x')/\ell_\mathrm{ED})
> $$
> with $K_\mathrm{vac}^\mathrm{prim}$ a bounded, Lorentz-covariant, finite-width function. The class is bounded above by the V1-δ refutation (zero-width limit fails C3 UV-FIN) and bounded below by the V1-∞ refutation (infinite-width limit fails C1 Lorentz covariance). Form of the class is FORCED; specific functional form (V2 exponential, V3 power-law-below-critical-exponent, V4 multi-scale) is INHERITED.

---

## 3. Scope

### 3.0 Primitive Inputs (postulated within the ED Generative Primitives System)

This paper takes the following Event Density (ED) substrate primitives as **postulated within the ED Generative Primitives System**:

- **V1 existence as a substrate vacuum-kernel rule-type:** the substrate carries a primitive vacuum response kernel acting on channel content. Supports empirically observed vacuum-fluctuation content (Casimir, Lamb shift, spontaneous emission).
- **P07 (channel structure):** supplies the substrate-level categorical domain on which the V1 kernel operates.
- **P11 (commitment irreversibility):** supplies the forward-causal structure on which V1's finite-width support operates.
- **Substrate-level UV cutoff (Theorem T7 / UV-FIN):** inherited from Arc Q closure. Required for C3.
- **Lorentz covariance of the substrate participation graph:** inherited from the substrate's relativistic-scope symmetry content. Required for C1.

The full 13-primitive Generative Primitives System is enumerated in the ED Foundations position paper. The empirical case for the primitives rests on their downstream reach across domains. This paper's contribution: given the primitives above, the V1 vacuum response kernel is forced to lie in the **V1 admissible class** — finite-width, Lorentz-covariant, UV-FIN-compatible (Theorem N1). The class is bounded above by V1-δ (zero-width limit fails C3) and below by V1-∞ (infinite-width fails C1). Specific functional form (V2 exponential, V3 power-law, V4 multi-scale) is inherited.

### 3.1 What is FORCED

- **Finite kernel width**: $K_\mathrm{vac}$ has finite extent in both temporal and spatial directions, with a natural width scale $\ell_\mathrm{ED}$ inherited from substrate primitives.
- **Non-singular support**: the kernel is a bounded function (or distribution that is regular in the sense of distributional convergence at the substrate scale), not a δ-function singularity.
- **Sub-power-law-2 decay**: the kernel decays faster than $1/(x-x')^2$ at large separation, ensuring UV-FIN compatibility when convolved with matter content.
- **Lorentz-covariant envelope**: the kernel transforms as a Lorentz scalar (or appropriate tensor) under Lorentz transformations; no preferred frame is selected.
- **UV-FIN compatibility (C3)**: the kernel respects the Theorem T7 substrate-level UV cutoff at the Planck scale.
- **The V1 class is bounded above and below**: V1-δ (zero-width limit) and V1-∞ (infinite-width limit) are both refuted; the admissible class lies strictly between.

### 3.2 What is INHERITED

- **Numerical value of the substrate-level scale $\ell_\mathrm{ED}$**. Identified with the Planck length $\ell_P$ in the substrate-gravity arc (Paper #9 §7.1), inheriting its numerical value from Newton-recovery.
- **Specific functional form** within the V1 class. V2 (exponential), V3 (power-law below critical exponent), V4 (multi-scale) are admissible realizations; the choice is INHERITED from value-layer / empirical content.
- **Specific envelope parameters** (decay rate, peak amplitude, spectral structure). INHERITED from substrate microscopic details.

### 3.3 What is OUT OF SCOPE

- **V1 retarded support / kernel-level arrow of time** (Theorem T18). The forcing argument that V1 must have retarded (not symmetric or advanced) support is the content of Paper #19, building on the present paper's V1-class forcing.
- **V5 cross-chain correlation kernel**. The V5 substrate-level kernel for cross-chain correlations is the subject of Paper #20.
- **Full memory-kernel cascade** (N1-E, N2-E, N3-D). The downstream cascade of memory-kernel structures inheriting FORCED status from V1 is the content of Paper #21.
- **Curved-spacetime extension** (Theorem GR1). V1 in curved spacetime via Synge world function lives in Arc N's curved-spacetime extension (T9), beyond the flat-spacetime scope of the present paper.

---

## 4. Key Vocabulary

- **Substrate.** Pre-quantum primitive layer of ED.
- **Vacuum response kernel $K_\mathrm{vac}(x - x')$.** Substrate-level structural object describing how the vacuum responds to a localized perturbation; the substrate analog of the two-point vacuum correlation function.
- **Vacuum memory kernel.** Synonym for vacuum response kernel; the "memory" terminology emphasizes the kernel's role in encoding past-perturbation dependence.
- **Kernel width.** Characteristic temporal or spatial extent of the kernel; the "support" of the function modulo decay.
- **V1 (finite-width vacuum memory kernel).** The substrate-level admissible class of vacuum kernels: finite-width, Lorentz-covariant, UV-FIN-compatible. The result FORCED in this paper.
- **V1-δ.** The zero-width limit of V1: the δ-function vacuum response. REFUTED by C3 UV-FIN.
- **V1-∞.** The infinite-width limit of V1: vacuum response with no spatial / temporal localization. REFUTED by C1 Lorentz covariance.
- **V2, V3, V4.** Specific functional realizations within the V1 class: V2 exponential, V3 power-law (admissible below a critical exponent), V4 multi-scale.
- **UV-FIN (Theorem T7).** Substrate-level UV finiteness: the substrate has a fundamental cutoff at $\ell_P$ (Planck length) preventing divergent UV behavior. Established in Arc Q.
- **Primitive event-discreteness (P01).** Substrate-level structural fact: events on the event manifold are discrete; the manifold is not infinitely refinable.
- **Proper-time finite intervals (P13).** Substrate-level structural fact: time between commitment events takes finite proper-time values; there is no zero-time-interval limit at primitive level.
- **C1 / C2 / C3.** Substrate-level constraints on the kernel: C1 Lorentz covariance, C2 spin-statistics preservation, C3 UV-FIN preservation.
- **Correlation envelope.** The functional shape of the vacuum kernel; the structural-form of $K_\mathrm{vac}^\mathrm{prim}$.

---

## 5. Substrate Class $\{C\}$

### C1. Lorentz covariance

The vacuum kernel must transform as a Lorentz scalar (or appropriate tensor) under Lorentz transformations. This forbids preferred-frame structures and requires the kernel to be expressible as a function of Lorentz-invariant combinations of $x - x'$ (e.g., proper time $\tau^2 = -(x-x')^\mu(x-x')_\mu$).

Source: substrate-level Lorentz-invariance of the participation graph in 3+1D (Paper #7's Cl(3,1) frame; broader Arc R inheritance).

### C2. Spin-statistics preservation

The vacuum kernel must respect the spin-statistics theorem (Paper #7): Case-P (bosonic, $\eta = +1$) and Case-R (fermionic, $\eta = -1$) rule-types have distinct statistics, and the kernel cannot induce mixings or violations at finite memory range.

Source: Theorem T1 spin-statistics (Paper #7) + Primitive P02 rule-type structure.

### C3. UV-FIN preservation

The vacuum kernel must respect the substrate-level UV cutoff at the Planck scale. In Fourier space, $\widetilde{K}_\mathrm{vac}(\omega, \mathbf{k})$ must be bounded (or decay) at high frequencies $\omega \to \infty$ and high wavenumbers $|\mathbf{k}| \to \infty$, preventing divergent contributions when convolved with matter content.

Source: Theorem T7 UV-FIN (Arc Q).

### C4. Primitive event-discreteness (P01)

The substrate's event manifold has primitive discreteness at the scale $\ell_\mathrm{ED}$ (later identified with $\ell_P$ by Newton-recovery in Paper #9). Below this scale, the manifold is not continuum-like; structural objects on the manifold cannot resolve content finer than $\ell_\mathrm{ED}$.

### C5. Proper-time finite intervals (P13)

Time between commitment events takes finite proper-time values. There is no zero-time-interval limit at primitive level; the substrate-level temporal resolution is finite.

### C6. Inherited results from Papers #1-#17

- **Paper #1**: participation measure $P_K = \sqrt{b_K}\,e^{i\pi_K}$ with $|P_K|^2 = b_K$.
- **Paper #5 (T17)**: gauge-field-as-rule-type with vacuum sector containing V1-form fluctuation envelope (C5-C7 of T17).
- **Paper #7 (Arc R)**: Lorentz-covariant relativistic structure + spin-statistics.
- **UV-FIN (T7)**: substrate-level UV cutoff at $\ell_P$.

### C7. No specific kernel form as input

The forcing argument invokes only C1-C6 plus standard mathematical infrastructure (Fourier analysis on $L^2(\mathbb{R}^4)$, distribution theory, Lorentz-invariance + UV-finiteness constraints on tempered distributions). No specific kernel form (δ-function, exponential, power-law) is assumed.

---

## 6. Alternative Encodings

### 6.1 Structural alternatives

**A1. V1-δ (δ-function kernel).** $K_\mathrm{vac}(x - x') = c_0\,\delta^4(x - x')$. Zero-width instantaneous vacuum response. The Markovian default of standard QFT.

**A2. V1-∞ (infinite-width kernel).** $K_\mathrm{vac}(x - x') = c_0$ for all $(x - x')$. No spatial / temporal localization; the vacuum responds identically to perturbations at all spacetime points.

**A3. Non-decaying finite-width kernel.** Finite-width but with oscillatory or constant behavior at large separation (no decay to zero). Includes kernels with persistent oscillations at constant amplitude.

**A4. Non-covariant kernels.** Finite-width kernels that fail Lorentz covariance — e.g., kernels with a preferred temporal direction not arising from substrate-level time-translation symmetry, or kernels with frame-dependent envelopes.

**A5. Singular kernels.** Kernels with divergent behavior at $(x - x') = 0$ but not strict δ-functions — e.g., $1/(x-x')^4$ as a structural form rather than as a UV-cutoff-regularized object.

**A6. Multi-scale kernels with separated supports.** Kernels that are zero on $\ell_\mathrm{ED} < |x-x'| < L$ for some intermediate $L$, with non-trivial support both below and above this gap. (Pathological multi-scale forms.)

**A7. Non-decaying-at-infinity kernels with bounded support.** Kernels with strict cutoff at some maximum scale rather than smooth decay.

### 6.2 Mainstream alternatives

**B1. QFT δ-function vacuum response.** The standard QFT treatment uses δ-function kernels and adds regularization (dimensional, lattice, Pauli-Villars) to handle the resulting UV divergences. Regularization is treated as a computational convenience rather than as a physical statement.

**B2. Markovian approximations.** Markovian master equations and Lindblad-form dynamics assume zero-memory environmental coupling, equivalent to δ-function vacuum response. Used extensively in open-quantum-system theory.

**B3. White-noise vacuum models.** Stochastic-process treatments of the vacuum as a Gaussian white-noise process. The white-noise correlation function is δ-function in time.

**B4. Stochastic-process analogues.** Ornstein-Uhlenbeck or other Gaussian-process treatments with finite correlation times. These are *consistent* with V1 in functional form but lack substrate-level derivation.

**B5. Wightman two-point function as primitive.** Standard QFT's Wightman two-point function $W(x - y) = \langle 0 | \phi(x)\phi(y) | 0\rangle$ is taken as a defining property of the field theory. Its specific form (e.g., $1/(x-y)^2$ for massless scalars) is derived from the Lagrangian.

**B6. Hadamard parametrix.** In curved spacetime, the Hadamard parametrix construction supplies a well-defined vacuum two-point function. This is downstream of the present paper (it lives in Arc N's curved-spacetime extension, Theorem T9 / GR1).

---

## 7. Constructive Necessity

The argument establishes the V1 class as the unique substrate-derived admissible class via five steps.

### 7.1 V1-δ refutation: zero-width kernels violate UV-FIN

Consider the δ-function vacuum response $K_\mathrm{vac}^{(\delta)}(x - x') = c_0\,\delta^4(x - x')$. In Fourier space:
$$
\widetilde{K}_\mathrm{vac}^{(\delta)}(\omega, \mathbf{k}) = c_0
$$
— a *constant* across all frequencies and wavenumbers.

The substrate-level vacuum response feeds into loop integrals and correlation functions involving the matter content. A typical contribution at the substrate-level is
$$
\Pi(p) \sim \int\frac{d^4k}{(2\pi)^4}\,\widetilde{K}_\mathrm{vac}(k)\,M(p, k),
$$
where $M(p, k)$ is the matter-content function. For $\widetilde{K}_\mathrm{vac}(k) = c_0$ (constant), the integral inherits the UV behavior of $M$ alone. For matter-content functions that fall off polynomially or are constant at high $|k|$, the integral diverges as $|k| \to \infty$.

This contradicts the substrate-level UV-FIN (C3, Theorem T7): the substrate has a finite UV cutoff at $\ell_P$, so loop integrals must be finite. δ-function vacuum response amplifies UV contributions and produces divergent integrals — incompatible with UV-FIN.

**Equivalently** (in position space): the δ-function vacuum response means the vacuum responds at arbitrarily fine spatial / temporal resolutions, including resolutions below the substrate's primitive discreteness scale $\ell_\mathrm{ED}$. But the substrate (C4 + C5) does not admit such resolutions: primitive event-discreteness (P01) places a minimum scale below which the manifold is not continuum-like, and primitive proper-time finite-intervals (P13) place a minimum temporal resolution. A δ-function kernel demands resolution below these substrate-level minimum scales — structurally inadmissible.

**V1-δ is REFUTED by C3 (UV-FIN) + C4/C5 (substrate-discreteness primitives).**

### 7.2 V1-∞ refutation: infinite-width kernels violate Lorentz covariance

Consider the infinite-width limit $K_\mathrm{vac}^{(\infty)}(x - x') = c_0$ — a constant function. In Fourier space:
$$
\widetilde{K}_\mathrm{vac}^{(\infty)}(\omega, \mathbf{k}) = c_0\,(2\pi)^4\,\delta^4(\omega, \mathbf{k}).
$$
The Fourier transform is a δ-function at zero frequency — i.e., the vacuum response is purely zero-frequency content.

This has two structural problems:

**(i) Non-decaying at spatial infinity.** The position-space constant function $K_\mathrm{vac}(x - x') = c_0$ does not decay at large $|x - x'|$. A vacuum kernel that responds with the same strength to perturbations at arbitrarily large distances is non-physical: it implies action at a distance with no falloff, violating substrate-level locality.

**(ii) Lorentz-covariance failure for time/space separation.** A constant function in 4D spacetime is Lorentz-invariant in the formal sense, but its Fourier content (δ at zero frequency) implies the vacuum's response is dominated by zero-frequency contributions in *every frame*. This means the vacuum singles out a "rest" structure in every frame simultaneously — which is impossible: different inertial frames have different zero-frequency reference points. Specifically, a perturbation at non-zero $\omega'$ in one frame is at non-zero $\omega$ in another (related by Lorentz boost), but a kernel that responds only to $\omega = 0$ cannot match these frame-dependent zero-frequencies consistently.

In rigorous terms: $\widetilde{K}_\mathrm{vac}^{(\infty)} \propto \delta(\omega)\delta^3(\mathbf{k})$ is not Lorentz-invariant under boosts because the boost mixes $\omega$ and $\mathbf{k}$. A Lorentz-invariant constant function in 4D would have to be the constant 1 (in position space), but its Fourier transform is the δ-function at zero, which is *not* boost-invariant in the relevant sense.

**V1-∞ is REFUTED by C1 (Lorentz covariance) + substrate-level locality.**

### 7.3 Primitive event-discreteness + proper-time intervals force a finite scale

Primitive 01 establishes that events on the event manifold are discrete: there is a primitive-level event-discreteness scale $\ell_\mathrm{ED}$ below which the manifold structure is not continuum-like. Below $\ell_\mathrm{ED}$, structural objects on the manifold do not have well-defined values — the substrate "stops resolving" finer content.

Primitive 13 establishes that commitment events have finite proper-time separations: there is no zero-time-interval limit at primitive level. The substrate-level temporal resolution is finite.

These two primitives jointly imply that primitive-level vacuum response has a natural width: the vacuum kernel cannot respond at resolutions finer than the event-discreteness scale because the substrate itself does not admit such resolutions. The vacuum-response kernel must therefore be smoothed at the $\ell_\mathrm{ED}$ scale:
$$
K_\mathrm{vac}(x - x') = K_\mathrm{vac}^\mathrm{prim}((x - x')/\ell_\mathrm{ED}),
$$
with $K_\mathrm{vac}^\mathrm{prim}$ a bounded function that converges to the δ-function only in the formal continuum limit $\ell_\mathrm{ED} \to 0$. At any finite primitive-discreteness scale, the kernel has finite width.

The scale $\ell_\mathrm{ED}$ is identified with the Planck length $\ell_P$ via Newton-recovery in the substrate-gravity arc (Paper #9 §7.1):
$$
\ell_\mathrm{ED}^2 = \frac{\hbar G}{c^3} = \ell_P^2.
$$
At $\ell_\mathrm{ED} = \ell_P \sim 10^{-35}\,\mathrm{m}$, the substrate's finite resolution is far below any currently observable scale — vacuum kernels appear effectively δ-function-like at laboratory scales, but the substrate-level structural fact is that they are not.

### 7.4 Three substrate constraints bound the V1 class

The admissible vacuum-kernel class is bounded by three substrate-level constraints inherited from earlier theorems:

**C1 Lorentz covariance.** Forces the kernel to be expressible as a function of Lorentz-invariant combinations of $(x - x')$. The natural invariants are the proper-time-squared $\tau^2 = -(x - x')^\mu(x - x')_\mu$ (or its sign-discriminated variants for spacelike vs. timelike separations). The kernel envelope must be $K_\mathrm{vac}^\mathrm{prim}(\tau/\ell_\mathrm{ED}, \mathrm{sign}(\tau^2))$.

**C2 Spin-statistics preservation.** Forces the kernel to respect the spin-statistics theorem. For multi-rule-type vacuum content (multiple Case-P and Case-R sectors), the kernel cannot induce cross-class mixings or violate the $\eta = (-1)^{2s}$ exchange dichotomy at finite memory range. This excludes specific cross-band coupling forms (N1-D Case-P↔Case-R coupling, refuted in Arc N Stage N.3).

**C3 UV-FIN preservation.** Forces the kernel's spectral content to be UV-finite: $\widetilde{K}_\mathrm{vac}(\omega, \mathbf{k}) \to 0$ as $|\omega|, |\mathbf{k}| \to \infty$. This excludes V1-δ (constant spectral content, §7.1) and admits only kernels with sufficient UV decay. Specifically, V3 power-law decay forms $\widetilde{K}_\mathrm{vac}(\omega) \sim \omega^{-\alpha}$ are admissible only for $\alpha$ above a critical exponent (Arc N Stage N.3 V3 refutation for sub-critical exponents); exponential V2 and multi-scale V4 forms with sufficient UV decay are admissible without restriction.

The combined constraints bound the V1 class:
- **Lower bound (C3)**: kernels must have non-zero width — V1-δ refuted.
- **Upper bound (C1)**: kernels must have finite extent — V1-∞ refuted.
- **Class-internal bounds (C2, C3 sub-cases)**: specific forms must respect spin-statistics + sufficient UV decay; sub-critical V3 power-laws refuted.

### 7.5 The V1 class is forced; specific forms are inherited

The composite result of §§7.1-7.4: the vacuum response kernel is forced to lie in the **V1 admissible class**, defined as the class of finite-width Lorentz-covariant kernels satisfying C1, C2, and C3 substrate constraints. Explicitly:

> **Theorem N1 (V1 finite-width vacuum memory kernel).** The vacuum response kernel $K_\mathrm{vac}(x - x')$ in flat spacetime is FORCED to lie in the V1 class:
> 1. **Finite temporal width**: support primarily within $|x - x'| \lesssim \ell_\mathrm{ED}$ scale (or specific kernel-dependent multiple thereof), with smooth decay beyond.
> 2. **Lorentz-covariant envelope**: $K_\mathrm{vac}(x - x') = K_\mathrm{vac}^\mathrm{prim}(\tau/\ell_\mathrm{ED}, \mathrm{sign}(\tau^2))$ with $\tau^2 = -(x-x')^\mu(x-x')_\mu$.
> 3. **UV-FIN compatible**: spectral content decays at high frequencies, ensuring finite loop integrals.
> 4. **Spin-statistics preserving**: kernel respects $\eta = (-1)^{2s}$ at finite memory range.
> 5. **Sub-power-law-2 decay**: $K_\mathrm{vac}(x - x') = O(|x - x'|^{-\alpha})$ with $\alpha > 2$ asymptotically, or exponentially fast (for V2-class forms).

**Specific functional realizations within V1**:

- **V2 (exponential)**: $K_\mathrm{vac}(\tau) \propto e^{-\tau/\tau_{V1}}$ with $\tau_{V1} \sim \ell_\mathrm{ED}/c$. Admissible; exponential UV decay is more than sufficient for UV-FIN.
- **V3 (power-law)**: $K_\mathrm{vac}(\tau) \propto \tau^{-\alpha}$ for $\alpha > 2$ (above critical exponent). Sub-critical exponents ($\alpha \leq 2$) are refuted by C3.
- **V4 (multi-scale)**: $K_\mathrm{vac}(\tau) = \sum_i c_i\,e^{-\tau/\tau_i}$ with multiple timescales $\tau_i$. Admissible; multi-scale forms appear in physical applications (Arc D's V5 viscoelastic identification uses multi-scale structure).

The **V1 class is FORCED**; the *specific* functional form within the class (V2, V3-above-critical, V4, or others) is **INHERITED** from value-layer / empirical content. Different physical applications (gauge sector, gravity sector, soft matter) may realize different specific forms within V1.

**The V1 class is bounded above and below**:
- **Upper bound (V1-δ refutation)**: zero-width kernels refuted by C3.
- **Lower bound (V1-∞ refutation)**: infinite-width kernels refuted by C1.

The admissible class lies strictly between these bounds, with the substrate-scale $\ell_\mathrm{ED}$ providing the natural width parameter.

---

## 8. Exclusion Arguments

### 8.1 A1 — V1-δ (δ-function kernel)

Excluded by C3 UV-FIN preservation (§7.1). The δ-function spectral content $\widetilde{K}_\mathrm{vac} = c_0$ is constant at all frequencies; loop integrals over matter content amplify high-frequency contributions and produce divergent results. This contradicts Theorem T7's substrate-level UV finiteness.

Equivalently, the δ-function position-space form requires resolution below the substrate's primitive discreteness scale $\ell_\mathrm{ED}$ (C4 + C5), which the substrate does not admit.

### 8.2 A2 — V1-∞ (infinite-width kernel)

Excluded by C1 Lorentz covariance + substrate-level locality (§7.2). A constant kernel in position space does not decay at large separation; vacuum response with no spatial / temporal falloff violates substrate locality. The Fourier δ-content at zero frequency is not Lorentz-boost-invariant.

### 8.3 A3 — Non-decaying finite-width kernels

A finite-width kernel that fails to decay (e.g., persistent oscillations at constant amplitude beyond the substrate scale) violates C1 Lorentz covariance: the persistent content at large separation has no Lorentz-covariant interpretation — at large $\tau^2$, a Lorentz-invariant function must either approach a constant (excluded by C1 as in §7.2) or decay. Sub-power-law-2 decay (§7.5) is the structural minimum.

### 8.4 A4 — Non-covariant kernels

Direct violation of C1 Lorentz covariance. Finite-width kernels with frame-dependent envelopes (e.g., kernels that depend on $(x - x')^0$ separately from $|\mathbf{x} - \mathbf{x}'|$) select a preferred frame, contradicting substrate-level Lorentz invariance inherited from Paper #7's relativistic structure.

### 8.5 A5 — Singular kernels

Kernels with divergent behavior at $(x - x') = 0$ but not strict δ-functions (e.g., $1/(x-x')^4$ as a position-space form) fail C3 UV-FIN: the Fourier transform of $1/(x-x')^4$ has divergent spectral content at high $\omega$. The substrate's UV cutoff at $\ell_P$ regularizes such singularities, smoothing them into the V1 finite-width envelope; the singular form *as a structural commitment* is excluded.

### 8.6 A6 — Multi-scale kernels with separated supports

A kernel with support only on $|x - x'| < \ell_\mathrm{ED}$ and $|x - x'| > L$ (with no support in the intermediate region) is structurally pathological: the Fourier transform of such a kernel oscillates wildly, producing non-physical interference patterns. The substrate-level event discreteness (C4) supports kernels with monotonic decay or continuous support; gapped supports are not admitted by primitive structure.

### 8.7 A7 — Non-decaying-at-infinity kernels with bounded support

Strict cutoff at some maximum scale $L$ (kernel exactly zero beyond $L$) is structurally admissible for some applications but is *not* Lorentz-covariant: a sharp cutoff at $L$ in one frame appears as a frame-dependent cutoff in another. Smooth decay (exponential, power-law-above-critical, etc.) is forced by C1 Lorentz covariance.

### 8.8 B1 — QFT δ-function vacuum response

Standard QFT's δ-function vacuum response is *the* approach the present paper refutes (§7.1). The regularization techniques (dimensional, lattice, Pauli-Villars) used to handle the resulting UV divergences are *implicitly* recognizing the need for finite-width structure but apply it via mathematical convenience rather than substrate-level necessity.

Under the substrate-conditions test, standard QFT's regularization machinery is *downstream* of the V1-class forcing: the regularization implements the substrate-level finite-width property at the level of perturbative calculations. The substrate forcing makes explicit what regularization implicitly assumes.

### 8.9 B2 — Markovian approximations

Markovian master equations (Lindblad, Pauli, Born-Markov) assume zero-memory environmental coupling. Under the substrate-conditions test, these are *effective* descriptions valid when the environment correlation time is much shorter than the system relaxation time — i.e., when the substrate-level V1 width is negligibly small compared to system timescales. Markovian approximations are *valid* in such regimes but are not substrate-level commitments; they are operational simplifications.

### 8.10 B3 — White-noise vacuum models

Gaussian white-noise models of the vacuum use δ-function-in-time correlations. Under the substrate-conditions test, white-noise models are the Markovian limit of finite-width V1 kernels (B2). They are valid in regimes where the substrate-level V1 width is negligible; they are not substrate-level alternatives but operational limits.

### 8.11 B4 — Stochastic-process analogues

Ornstein-Uhlenbeck processes and similar Gaussian-process treatments with finite correlation times are *consistent with* V1 in functional form (V2 exponential or V4 multi-scale, depending on the specific process). They lack substrate-level derivation but match the V1-class structural content. Under the substrate-conditions test, these are admissible V2 / V4 realizations within the V1 class — not alternatives to the V1 class itself.

### 8.12 B5 — Wightman two-point function as primitive

Standard QFT's Wightman two-point function is taken as a defining property; its specific form (e.g., $1/(x-y)^2$ for massless scalars in the continuum limit) is derived from the Lagrangian. Under the substrate-conditions test, the Wightman function is *downstream* of the V1-class forcing: the specific functional form within V1 (V2, V3-above-critical, V4) supplies the Wightman content at the substrate-grounded level. The δ-function or singular continuum-Wightman limit is the unregularized form that the V1 class regularizes naturally.

### 8.13 B6 — Hadamard parametrix (curved spacetime)

The Hadamard parametrix construction in curved spacetime supplies a well-defined vacuum two-point function via the Synge world function. This is the *curved-spacetime extension* of V1, established in Theorem T9 / GR1 (Arc N curved-spacetime extension). It is downstream of the present paper (which covers flat-spacetime V1) and is the subject of the substrate-gravity / GR-emergence track (Paper #9 + ED-10 arc).

### 8.14 Summary of exclusions

| Alternative | Violates | Reason |
|---|---|---|
| A1 V1-δ (zero-width) | C3 (UV-FIN), C4/C5 | Spectral content constant → UV divergence; requires sub-substrate-scale resolution. |
| A2 V1-∞ (infinite-width) | C1 (Lorentz covariance) | Non-decaying at infinity violates substrate locality; Fourier δ at zero violates boost invariance. |
| A3 non-decaying finite-width | C1 | Persistent content at large separation lacks Lorentz-covariant interpretation. |
| A4 non-covariant kernels | C1 (direct) | Frame-dependent envelope selects preferred frame. |
| A5 singular kernels | C3 | Power-law singularities have divergent UV spectral content. |
| A6 multi-scale gapped supports | C4 (substrate discreteness) | Gapped supports produce non-physical interference; substrate admits monotonic / continuous support. |
| A7 sharp cutoff at finite scale | C1 | Sharp cutoff is frame-dependent; smooth decay is Lorentz-required. |
| B1 QFT δ-vacuum + regularization | not in space | Regularization implicit-recognizes V1; substrate makes it explicit. |
| B2 Markovian approximations | not in space | Effective description in narrow-V1-width limit; not substrate-level. |
| B3 white-noise vacuum | not in space | Markovian limit of V2; same status as B2. |
| B4 stochastic processes | consistent | Admissible V2/V4 realizations within V1 class. |
| B5 Wightman as primitive | downstream | Specific V1 functional form supplies Wightman content. |
| B6 Hadamard parametrix | scope-different | Curved-spacetime extension (Theorem T9 / GR1). |

**The V1 finite-width vacuum memory kernel class is the unique substrate-derived admissible class for the vacuum response in flat spacetime.**

---

## 9. Falsifiers and Empirical Exposure

### 9.1 Empirical falsifier

The empirical falsifier is sharp:

**Any reproducible observation of δ-function vacuum response at the kinematic level** (i.e., not handled by perturbative regularization but as a structural property) falsifies the substrate-level forcing along with the standard QFT regularization assumption.

Specific empirical contexts:

- **Casimir effect**: the finite Casimir energy between conducting plates is direct evidence of finite-width vacuum response. The substrate-level forcing predicts the Casimir effect from the V1 class structure (with specific functional form V2/V3/V4 inherited from the gauge sector); observed Casimir energies match the standard QED calculation at high precision.
- **QED vacuum polarization**: the photon propagator's vacuum-polarization correction has a finite range characterized by the electron mass. This is consistent with V1-class structure realized in the QED gauge sector.
- **Lattice QCD vacuum-correlation lengths**: zero-temperature lattice QCD measurements yield finite correlation lengths for various vacuum operators, consistent with V1-class structure realized in the QCD gauge sector.
- **Cosmological constant**: the observed value of $\Lambda$ is far smaller than the naive QFT zero-point estimate, consistent with substrate-level V1 regulation of vacuum energy.

Any reproducible observation of a divergent loop integral that cannot be regularized via the V1-class structure — i.e., a divergence that survives even after substrate-level UV cutoff — would falsify the V1 forcing.

### 9.2 Structural falsifier

Construct a substrate satisfying C1-C7 (Lorentz covariance, spin-statistics, UV-FIN, primitive event-discreteness, proper-time finite intervals, Papers #1-#17 inherited, no specific kernel form as input) but for which the vacuum response kernel is forced to lie *outside* the V1 class — i.e., a substrate where V1-δ or V1-∞ is admissible, or where the kernel must be non-Lorentz-covariant or non-UV-FIN-compatible.

The author's claim is that no such substrate exists. Each alternative is dispatched by a specific substrate-condition violation. A reader who exhibits a counterexample refutes the present paper.

### 9.3 Downstream exposure

V1 is the structural foundation for several downstream substrate-level results:

**Paper #19 (V1 retarded support, Theorem T18).** The V1 class permits both retarded (causal) and advanced (anti-causal) support; Paper #19 establishes that the retarded form is FORCED via the kernel-level arrow of time, dispatching the symmetric and advanced alternatives.

**Paper #20 (V5 cross-chain correlation kernel).** The cross-chain correlation kernel V5 inherits the V1-class structure (finite-width, Lorentz-covariant, UV-FIN-compatible) extended to cross-chain content. Paper #20 establishes the specific V5 structure in the substrate.

**Paper #21 (memory-kernel cascade).** N1-E (vacuum-induced bandwidth memory), N2-E (vacuum-modulated commitment memory), N3-D (vacuum-mediated adjacency memory) all inherit FORCED status from V1.

**Paper #5 T17 vacuum sector.** The gauge-sector vacuum kernel (C5 of T17) is a V1-class structure specialized to gauge fields. The substrate-level UV-finite gauge vacuum-kernel arises from the V1 forcing of the present paper.

**Paper #9 substrate gravity (V1 cosmological-scale integral).** The cosmological constant $\Lambda$ as a V1 cosmological-scale integral (form-FORCED via Synge structure, weak-strength forcing flagged in Paper #9 §3.2) builds on the V1 class via curved-spacetime extension.

**Paper #10 BH + Hawking spectrum (V5 KMS argument).** The substrate-level KMS condition on V5 imaginary-time correlations (Paper #10 §7.5) uses V1-class structure to derive the Hawking temperature. Without the V1 forcing of the present paper, the V5-KMS argument would lack its structural foundation.

The substrate-level V1 forcing supports all of these downstream results.

---

## Appendix A — Derivation Chain and Glossary

### A.1 The δ-function refutation calculation — explicit

Consider a substrate-level loop integral involving the vacuum kernel:
$$
\Pi(p) = \int\frac{d^4k}{(2\pi)^4}\,\widetilde{K}_\mathrm{vac}(k)\,\frac{1}{(p - k)^2 + m^2}\,\frac{1}{k^2 + m^2}.
$$
For $\widetilde{K}_\mathrm{vac}(k) = c_0$ (δ-function vacuum response):
$$
\Pi(p) = c_0\int\frac{d^4k}{(2\pi)^4}\,\frac{1}{(p - k)^2 + m^2}\,\frac{1}{k^2 + m^2}.
$$
The integrand at large $|k|$ behaves as $1/|k|^4$, so the integral $\int d^4k/|k|^4$ diverges logarithmically. UV divergence.

For a V1-class kernel with $\widetilde{K}_\mathrm{vac}(k) = c_0\,e^{-(k\ell_\mathrm{ED})^2}$ (V2-form, Gaussian cutoff at substrate scale):
$$
\Pi(p) = c_0\int\frac{d^4k}{(2\pi)^4}\,\frac{e^{-(k\ell_\mathrm{ED})^2}}{(p - k)^2 + m^2}\,\frac{1}{k^2 + m^2}.
$$
The Gaussian damping factor suppresses large-$|k|$ contributions; the integral is finite. UV-FIN preserved.

### A.2 Lorentz-covariance constraint on the envelope

A Lorentz-invariant function on flat spacetime can depend only on Lorentz-invariant combinations of its argument. For a 4-vector $\Delta x = x - x'$, the Lorentz-invariant combinations are:
- $\Delta\tau^2 = -\Delta x^\mu \Delta x_\mu$ (signed: positive for timelike, negative for spacelike).
- $\mathrm{sign}(\Delta x^0)$ (only meaningful for timelike separations).

The most general Lorentz-invariant kernel envelope is therefore
$$
K_\mathrm{vac}(\Delta x) = F_+(\Delta\tau^2/\ell_\mathrm{ED}^2)\,\theta(\Delta\tau^2)\,\mathrm{sign}(\Delta x^0) + F_-(|\Delta\tau^2|/\ell_\mathrm{ED}^2)\,\theta(-\Delta\tau^2),
$$
for some functions $F_+$ (timelike support) and $F_-$ (spacelike support). The specific functional forms of $F_+$ and $F_-$ are INHERITED; the form-FORCED content is the Lorentz-invariant dependence on $\Delta\tau^2$.

### A.3 Substrate-discreteness smoothing

The substrate-discreteness scale $\ell_\mathrm{ED}$ smooths the vacuum kernel at primitive resolutions:
$$
K_\mathrm{vac}^\mathrm{prim}(\Delta x) = K_\mathrm{vac}^\mathrm{continuum}(\Delta x) * S_{\ell_\mathrm{ED}}(\Delta x),
$$
where $*$ is convolution and $S_{\ell_\mathrm{ED}}$ is a smoothing function with characteristic scale $\ell_\mathrm{ED}$. The δ-function continuum limit is recovered when $\ell_\mathrm{ED} \to 0$ (formal continuum); at any finite $\ell_\mathrm{ED}$, the kernel has finite width.

The Newton-recovery identification $\ell_\mathrm{ED} = \ell_P$ (Paper #9 §7.1) fixes the substrate-discreteness scale empirically:
$$
\ell_P = \sqrt{\hbar G/c^3} \approx 1.6 \times 10^{-35}\,\mathrm{m}.
$$
At this scale, the V1 finite-width property is far below currently observable scales.

### A.4 Glossary

- **C1 Lorentz covariance.** Substrate constraint forcing kernels to transform as Lorentz scalars (or appropriate tensors) under Lorentz transformations.
- **C2 spin-statistics preservation.** Substrate constraint forcing kernels to respect $\eta = (-1)^{2s}$ at finite memory range.
- **C3 UV-FIN preservation.** Substrate constraint forcing kernels to have finite UV spectral content.
- **Event-discreteness scale $\ell_\mathrm{ED}$.** Substrate-level minimum resolution scale below which the manifold is not continuum-like. Identified with $\ell_P$ via Newton-recovery (Paper #9).
- **FORCED.** Derived from substrate primitives + standard mathematics with no additional commitments.
- **INHERITED.** Quantitative content (specific functional form, envelope parameters, numerical $\ell_P$ value) used but not derived in this paper.
- **Kernel width.** Characteristic temporal or spatial extent of the kernel.
- **Lorentz covariance.** Invariance under Lorentz transformations; transformation as a scalar / tensor.
- **Markovian approximation.** Zero-memory limit; δ-function-in-time correlation.
- **Primitive event-discreteness (P01).** Substrate-level structural fact: events on the event manifold are discrete.
- **Proper-time finite intervals (P13).** Substrate-level structural fact: time between commitment events takes finite proper-time values.
- **Substrate.** Pre-quantum primitive layer of ED.
- **UV-FIN.** Theorem T7 / Q.8: substrate-level UV finiteness with cutoff at $\ell_P$.
- **V1 (finite-width vacuum memory kernel).** The substrate-derived admissible class of vacuum kernels; the FORCED result of Theorem N1 / T8.
- **V1-δ.** Zero-width limit of V1; refuted by C3.
- **V1-∞.** Infinite-width limit of V1; refuted by C1.
- **V2 (exponential), V3 (power-law), V4 (multi-scale).** Specific functional realizations within the V1 class; INHERITED.
- **Vacuum response kernel $K_\mathrm{vac}(x - x')$.** Substrate-level structural object describing how the vacuum responds to localized perturbations.
- **Wightman two-point function.** Standard QFT's vacuum two-point function $\langle 0 | \phi(x)\phi(y) | 0\rangle$; downstream of V1 in the substrate hierarchy.

### A.5 Source-repository citations (for ED-internal readers)

- `arcs/arc-N/non_markov_forced.md` — Stage N.2 FORCED evaluation memo establishing V1 as FORCED at primitive level.
- `arcs/arc-N/non_markov_refuted.md` — Stage N.3 REFUTED evaluation memo establishing V1-δ and V1-∞ as the bounds of the V1 admissible class.
- `arcs/arc-N/arc_n_synthesis.md` — Arc N synthesis with V1 as the headline result.
- `arcs/arc-N/non_markov_catalogue.md` — full catalogue of 20 non-Markovian structures; V1 is item #1.
- `arcs/arc-N/memory_kernel_derivation.md` — substrate-level derivation of the memory kernel structure.
- `arcs/arc-N/non_markov_implications.md` — cross-arc implications (Stage N.4) of V1 forcing.
- `theorems/T8.md` — theorem-level index entry: T8 / N1 FORCED.

These are *not* required reading for the present paper.

---

*End of Paper #18.*
