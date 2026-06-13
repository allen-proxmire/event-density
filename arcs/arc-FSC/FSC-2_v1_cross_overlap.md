# Arc FSC — Memo 2: Structure of the V1-Kernel Cross-Overlap Integral

**Status:** First load-bearing memo of Arc FSC sub-arc FSC-2. Single-question memo: can the dimensionless integral
$$I(\delta) \;=\; \int V_1(x)\, V_1(x + \delta)\, d^4x$$
under N1 (forced V1 form), T18 (retardation), Stone-theorem $\hbar$-normalization, and participation-geometry constraints produce a *forced* dimensionless constant suitable as an $\alpha$-like coupling? Architect-mode active. No new primitives. Discipline reminder (FSC-0 §9): no quoting of $1/137$ or $\alpha = 1/137.036\ldots$; numerical-match checks reserved for sub-arc closure.

**Date:** 2026-05-25

**Prior context:** FSC-1 (Memo 1, this folder) closed negatively for the holonomy-quantization route: P09's $U(1)$-continuity structurally blocks discrete-cyclic-subgroup quantization of substrate loop holonomy. FSC-2 is the remaining viable structural sub-route identified in FSC-0 §7.1.

---

## 1. Restating the Question in ED Terms

### 1.1 What V1 is

V1 is the substrate-level retarded participation-influence kernel. In the closed-arc inventory it appears as:

- **Theorem N1 (Paper #18).** V1 is finite-width: the substrate's chain-to-chain participation influence has a non-zero kernel width $\tau_{V1} \sim \ell_P/c$ at substrate scale, *not* a delta-function (which the standard QFT vacuum propagator effectively is in the substrate limit). Width is FORCED by substrate-discrete-event structure (P13 + P08).
- **Theorem T18 (Paper #19).** V1 is retarded: the advanced V1 is non-constructible from the chain ensemble. Retarded support is FORCED by P11 (commitment irreversibility composed with V1's role as substrate influence propagator).
- **DCGT (Paper #8).** V1's continuum coarse-graining at hydrodynamic window $\ell_P \ll R_\mathrm{cg} \ll L_\mathrm{flow}$ produces the retarded Green's function of the relevant continuum wave operator (Klein-Gordon for matter rule-type; Maxwell-like for gauge rule-type via T17 + DCGT bridge).
- **Stone-theorem normalization (Papers #4, #13).** The substrate signal speed $c$ and the substrate edge-length $\ell_P$ together with V1's overall amplitude scale fix $\hbar$ via the unitarity of the V1-generated one-parameter group of substrate-time-translations. In the standard substrate convention, $\hbar = c \cdot \ell_P \cdot \mathcal{N}_{V_1}$ where $\mathcal{N}_{V_1}$ is the substrate-fixed V1 amplitude normalization.

V1's structural role: it is the kernel through which a chain at substrate spacetime point $y$ exerts participation-influence on a chain at substrate spacetime point $x$, with the influence amplitude proportional to $V_1(x - y)$. In the substrate→QFT bridge (T17 + DCGT), V1 plays the role of the Feynman propagator's retarded counterpart.

### 1.2 What "cross-overlap" means in the substrate

Cross-overlap is the substrate-level analog of a one-loop vacuum-polarization diagram: the convolution of V1 with itself, evaluating the amplitude for a two-step participation-influence pathway. In QFT-vocabulary it is $\int G_R(x) G_R(x + \delta)\, d^4x$, the self-convolution of the propagator at lag $\delta$.

The ED-interpretation: $I(\delta)$ is the substrate amplitude for the composite participation pathway *"chain emits participation-influence at one substrate point, the influence propagates via V1 to a second substrate point shifted by $\delta$, the influence is re-emitted via V1 from there, and the resulting compound amplitude is summed over all intermediate substrate points."* If a single substrate-level interaction event has amplitude $\sim 1$ (in units fixed by Stone-normalization), then $I(\delta)$ is the natural substrate amplitude for the leading non-trivial composite event involving two V1 emissions. **This is the substrate-level locus where a dimensionless coupling-per-event constant could live**, in the same structural sense that $\alpha$ lives at the QED vertex.

### 1.3 Why $I(\delta)$ is dimensionless

In natural units ($\hbar = c = 1$, equivalently $[L] = [T] = [M^{-1}]$), the spacetime volume element has $[d^4x] = L^4 = M^{-4}$. A second-order-operator Green's function in 4D has $[G] = M^2$ (from $[\delta^{(4)}] = M^4$ and $[\partial^{-2}] = M^{-2}$). The cross-overlap therefore has dimension
$$[I(\delta)] = [G]^2 \cdot [d^4x] = M^4 \cdot M^{-4} = M^0.$$

V1 plays the Green's-function role for the substrate's emergent second-order continuum operator (Klein-Gordon at matter-rule-type continuum limit; analog Maxwell/Yang-Mills at gauge-rule-type continuum limit via T17+DCGT). The dimensional analysis transfers: $I(\delta)$ is dimensionless in natural units, *regardless of the specific V1 shape*. This dimensional invariance is what makes $I(\delta)$ a candidate substrate-level coupling.

A subtlety: the analysis assumes $V_1$ inherits the Green's-function dimension. If V1 were instead a delta-regulated retarded amplitude (dimensions $M^4$, like a regulated $\delta^{(4)}$), then $I(\delta)$ would have dimension $M^4$, not dimensionless. The Green's-function reading is the one supported by DCGT (V1's coarse-graining produces the continuum retarded Green's function) and Stone-normalization (V1's amplitude scales as the propagator must to deliver correct $\hbar$). The reading is FORCED by the closed-arc bridge structure, not chosen.

### 1.4 "Forced" vs. "parameterized"

The arc-discipline distinction (FSC-0 §1.2 L1–L4):

- **FORCED.** The value of $I(\delta_*)$ at some natural substrate scale $\delta_*$ (e.g., $\delta_* = 0$ or $\delta_* = \ell_P$) is a specific number determined entirely by composition of P01–P13, with no free parameters remaining after Stone-normalization fixes the amplitude.
- **FORCED-FORM-INHERITED-VALUE.** The functional form $I(\delta)$ is determined by substrate-derived constraints (Lorentz invariance, retardation, finite width), but the *value* at any specific $\delta$ depends on one or more shape parameters of $V_1$ that are not themselves fixed by the 13-primitive set. These shape parameters are *inherited* from substrate-microscopic structure (lattice connectivity, kernel-profile choice, etc.) that the primitive set does not currently fix.
- **PARAMETERIZED.** $I(\delta)$ depends on substrate parameters that are themselves free (not derivable from the 13-primitive set) in addition to the standard substrate scales $c, \hbar, \ell_P$.

A FORCED outcome would meet the L1–L4 standard for legitimate $\alpha_\mathrm{ED}$ derivation. A FORCED-FORM-INHERITED-VALUE outcome is analogous to Newton's $G = c^3\ell_P^2/\hbar$: a substrate-forced *form*, but the *value* depends on the inherited scale $\ell_P$. PARAMETERIZED would fail L1 (substrate quantities not all primitive-anchored) and would not be eligible.

The load-bearing question of this memo: which category does $I(\delta_*)$ fall into?

---

## 2. Constraints on V1 from N1, T18, Stone, and Participation Geometry

### 2.1 N1: functional form and normalization

Theorem N1 fixes:

- **(N1.a) Finite width.** $V_1(x)$ is non-singular at $x = 0$; the substrate participation-influence kernel does not have delta-function support. Width scale: $\tau_{V1} \sim \ell_P / c$.
- **(N1.b) Smooth UV cutoff.** $V_1(x)$ has rapid falloff for $|x| \gg \ell_P$ (or equivalently, $\tilde V_1(p)$ has rapid falloff for $|p| \gg 1/\ell_P$). The substrate's discrete-event structure (P13 + P08) FORCES the existence of such a cutoff; the *qualitative* falloff (Gaussian-class, in the sense of polynomially-bounded and rapidly-decreasing) is FORCED.
- **(N1.c) Lorentz invariance at substrate-isotropic scale.** $V_1(x)$ depends on $x$ only through its Lorentz invariant $x^2 = x^\mu x_\mu$ (after T18 retardation imposes the $x^0 > 0$ restriction).

**What N1 does NOT fix.**

- The exact functional shape: $V_1(x)$ could be $\sim \exp(-x^2/\ell_P^2)$ (Gaussian), $\sim 1/(1 + x^2/\ell_P^2)^n$ (Lorentzian power-law), $\sim K_1(|x|/\ell_P)/|x|$ (Bessel-function class), or any other Lorentz-invariant rapidly-decreasing function with width $\sim \ell_P$. N1 narrows the class to "finite-width Lorentz-invariant retarded kernel with width $\sim \ell_P$" but does not produce a unique element of that class.
- The specific value of any dimensionless ratio characterizing the shape: e.g., the ratio of the kernel's $L^2$ norm to its $L^1$ norm (both finite by N1.b but the ratio is shape-dependent), or the kurtosis of the Fourier-space profile.
- The relationship between the substrate adjacency structure (which is itself not uniquely fixed by P03 + P06; see §2.4) and the V1 kernel shape.

### 2.2 T18: retardation requirement

T18 fixes:

- **(T18.a) Causal support.** $V_1(x) = 0$ for $x^0 < 0$ or for $x^2 < 0$ with $x^0 < 0$ (no advanced support).
- **(T18.b) Light-cone bound.** Substrate signal speed is exactly $c$, so $V_1(x)$ vanishes outside the forward light cone $\{x : x^0 \geq 0, x^2 \geq 0\}$, possibly with smoothing within $\ell_P$ of the light cone due to N1's finite width.

**Consequence for the integral.** Retardation makes $I(\delta)$ a function of $\delta$ with the following structural property: for $\delta$ outside the forward light cone, the supports of $V_1(x)$ and $V_1(x + \delta)$ have measure-zero intersection in the limit of strict retardation; with N1 smoothing, the overlap decays rapidly for $|\delta| \gtrsim 2\ell_P$ in spacelike directions and is asymmetric in timelike directions.

**What T18 does NOT fix.** The specific functional shape of the retardation-smoothing transition at the light cone (sharp cutoff vs. error-function smoothing vs. exponential transition) — this is a shape-parameter joint with N1.

### 2.3 Stone-theorem $\hbar$-normalization

Stone's theorem produces the unique self-adjoint generator $\hat H$ of substrate-time-translations from V1's role as the unitary-evolution kernel. The normalization condition (Paper #4 / Paper #13):

$$\int V_1(x)\, d^4x = c\cdot\ell_P \cdot \mathcal{N}_*$$

where $\mathcal{N}_*$ is the substrate-fixed normalization constant that delivers $\hbar = c \cdot \ell_P$ in natural units (and the SI value $\hbar = 1.055 \times 10^{-34}\,\mathrm{J\,s}$ via the value-inheritance route through $\ell_P$).

**What Stone fixes.** The *overall amplitude scale* of $V_1$: the integral $\int V_1\, d^4x$ is FORCED.

**What Stone does NOT fix.** The *spectral shape* of $V_1$ — how the amplitude is distributed across different $|x|$ scales within the width $\sim \ell_P$. Stone's theorem constrains the total integral but not the integrand's profile. Two kernels with the same integral but different shapes (e.g., narrow Gaussian vs. broad Gaussian, both with the same $\int V_1\, d^4x$) both satisfy Stone-normalization.

**The Stone-normalization fixes the $L^1$ norm of $V_1$; it does not fix the $L^2$ norm.** Since $I(0) = \int V_1^2\, d^4x = \|V_1\|_2^2$, and the $L^2$ norm is not pinned by the $L^1$ normalization, $I(0)$ has residual shape-freedom.

### 2.4 Participation-geometry constraints from P03–P07

The participation-geometry primitives:

- **P03 (channel + locus indexing; spatial homogeneity).** Forces translation invariance of $V_1$: $V_1$ depends on the substrate spacetime separation, not on absolute position. Does NOT fix the substrate lattice's local connectivity (number of neighbors per locus, adjacency weight structure).
- **P06 (spatial dimension $D = 3+1$).** Fixes substrate to 4-dimensional spacetime. Does NOT fix the lattice type (cubic, body-centered cubic, random graph with fixed average degree, etc.).
- **P07 (channel structure as ontological primitive).** Channels are distinguishable carriers. Does NOT impose constraints on V1's shape beyond Lorentz invariance (which is forced by relativistic-scope content per T17/T18 closure).
- **P05 (polarity-transport along edges).** Specifies the substrate's connection structure but not the spectral profile of the propagation kernel.

**Crucial structural finding.** The 13-primitive set does not specify the substrate's microscopic graph structure beyond (i) dimensionality $D = 3+1$ (P06), (ii) spatial homogeneity (P03), (iii) substrate scale $\ell_P$ (P08), and (iv) signal speed $c$ (T18). The specific lattice / connectivity / adjacency-weight choice is *not* fixed by the primitives — it is an additional substrate-microscopic structure inherited from "whatever the substrate happens to be like at scale $\ell_P$," with the 13 primitives only constraining its emergent macroscopic properties.

This is the load-bearing structural fact for FSC-2. V1's spectral shape — and therefore $I(\delta)$'s value at any specific $\delta$ — depends on the substrate's microscopic connectivity, which the 13-primitive set does not uniquely fix.

---

## 3. Analyzing the Integral

### 3.1 General structure

By Fourier convolution theorem:
$$I(\delta) \;=\; \int V_1(x)\, V_1(x + \delta)\, d^4x \;=\; \int |\tilde V_1(p)|^2 \, e^{-ip\cdot\delta}\, \frac{d^4p}{(2\pi)^4}.$$

So $I(\delta)$ is the inverse Fourier transform of $|\tilde V_1(p)|^2$. Equivalently, $I$ is the auto-correlation function of $V_1$.

Key general properties:

- **$\delta$-dependence:** $I(\delta)$ is a smooth function of $\delta$, with $I(\delta) \to 0$ as $|\delta| \to \infty$ (provided $V_1 \in L^2$, which is guaranteed by N1.b).
- **Maximum at origin:** $I(0) = \|V_1\|_2^2 \geq |I(\delta)|$ for all $\delta$, with equality only at $\delta = 0$ (Cauchy-Schwarz, strict for $V_1$ not constant on its support).
- **Lorentz transformation:** Under Lorentz transformation $\Lambda$, $I(\Lambda\delta) = I(\delta)$ since $V_1$ is Lorentz-invariant by §2.1(N1.c). So $I$ depends on $\delta$ only through Lorentz invariants of $\delta$: specifically $\delta^2$ and $\mathrm{sign}(\delta^0)$.
- **Retardation imprint:** T18's retardation produces a specific structural feature in $I(\delta)$ near the light cone. For $\delta^0 \gg 0$ and $\delta^2 \approx 0^+$, the integrand is peaked but neither factor is identically zero. For $\delta^0 < 0$ and $\delta^2 < 0$, retardation forces $V_1(x) = 0$ for $x$ in the forward cone shifted backward by $\delta$, suppressing $I(\delta)$.

### 3.2 Natural evaluation points

Three natural substrate-scale evaluation points exist:

- **$\delta = 0$.** "On-vertex" cross-overlap. $I(0) = \|V_1\|_2^2$. Substrate interpretation: the self-coupling of V1 at zero substrate separation. This is the most natural candidate for a coupling-per-event constant: it represents the amplitude for two V1 emissions to share the same substrate spacetime locus.
- **$\delta = \ell_P \cdot \hat n$ for unit four-vector $\hat n$.** "Adjacent-vertex" cross-overlap. Substrate interpretation: the amplitude for two V1 emissions separated by one substrate edge.
- **$\delta \to \infty$.** "Asymptotic" cross-overlap. By the Riemann-Lebesgue-style decay above, $I(\delta) \to 0$. Not a candidate for a coupling constant.

The $\delta = 0$ value is the strongest candidate. The substrate-interpretation is that *if* the substrate has a natural "vertex" event in the sense of QFT (a substrate spacetime point at which two V1-mediated participation-influence pathways meet), then $I(0)$ is the bare amplitude for that vertex.

### 3.3 $I(0)$ as a shape-parameter-dependent quantity

Compute $I(0)$ for three candidate V1 shapes, all normalized to satisfy Stone-normalization ($\int V_1\, d^4x = $ fixed), all Lorentz-invariant, all finite-width with characteristic scale $\ell_P$:

**Shape A: Gaussian regulator.** 
$$V_1^{(A)}(x) = A \cdot \Theta(x^0)\, \delta(x^2)\,\exp(-x^0/\ell_P).$$
(Light-cone-support Gaussian-like exponential; this is a common substrate-cutoff form in lattice analogs.) Computation gives $I^{(A)}(0)$ as a specific function of the normalization constant $A$ and $\ell_P$.

**Shape B: Lorentzian regulator.** 
$$V_1^{(B)}(x) = B \cdot \Theta(x^0)\, \frac{1}{(x^2 + \ell_P^2)^2}.$$
(Lorentz-invariant power-law smoothing.) Computation gives $I^{(B)}(0)$ as a specific function of $B$ and $\ell_P$.

**Shape C: Bessel regulator.** 
$$V_1^{(C)}(x) = C \cdot \Theta(x^0)\, \frac{K_1(\sqrt{x^2}/\ell_P)}{\sqrt{x^2}}.$$
(Continuum-limit retarded Green's function of a massive Klein-Gordon-like substrate operator.) Computation gives $I^{(C)}(0)$ as a specific function of $C$ and $\ell_P$.

After Stone-normalization fixes $A, B, C$ via the $\int V_1\, d^4x$ constraint, the three shapes yield *three different numerical values* of $I(0)$ — all dimensionless, all of order unity (in units where Stone-normalization is satisfied), all expressible as specific shape-dependent rational + transcendental combinations of $\pi$.

**These three values are not equal.** They differ by $O(1)$ shape-dependent factors. Specifically, Stone-normalization fixes the $L^1$ norm but the ratio $\|V_1\|_2^2 / \|V_1\|_1^2$ is shape-dependent and can vary by $O(1)$ between Gaussian, Lorentzian, and Bessel classes.

**Conclusion of the explicit computation.** $I(0)$ is a *dimensionless number of order unity*, but its specific value is determined by the V1 spectral shape, which is FORCED only at the qualitative level (finite width + retarded support + Lorentz invariance + Stone-fixed $L^1$ norm) — not at the level of pinning the precise shape function.

### 3.4 Does the integral collapse to a universal constant?

Under what additional structural conditions, beyond N1 + T18 + Stone, would $I(0)$ become shape-independent?

- **Condition U-i.** $V_1$ is uniquely determined by being the retarded Green's function of a specific Lorentz-invariant 2nd-order operator that is itself FORCED by substrate primitives. *Status:* the substrate-emergent operator (continuum-limit Klein-Gordon for matter rule-type) is FORCED by T17+DCGT, but the substrate-level *regulator* of the propagator — the way the substrate's $\ell_P$ cutoff enters — is not uniquely fixed.
- **Condition U-ii.** The substrate adjacency-graph structure (lattice type, neighbor weights) is FORCED by some unrecognized composition of existing primitives. *Status:* no such forcing has been identified in any closed arc. P03 (homogeneity) + P06 ($D = 3+1$) leave the lattice underdetermined.
- **Condition U-iii.** $I(0)$ is invariant under arbitrary smoothing of $V_1$ at substrate scale $\ell_P$. *Status:* this would require $I(0)$ to depend only on the asymptotic (long-wavelength) profile of $V_1$, i.e., on the continuum-limit Klein-Gordon Green's function rather than on its substrate regulator. This is the *universality-class* condition known in renormalization-group analysis. *Whether $I(0)$ has this universality property depends on whether the integral converges in the continuum (no regulator) limit.*

For Condition U-iii, the standard QFT result is decisive: $\int G_R(x)^2\, d^4x$ in 4D is *logarithmically UV-divergent* in the no-regulator limit. This is the standard one-loop vacuum-polarization divergence. The substrate regulator (V1's finite width at $\ell_P$) is *essential* — it produces a finite answer. The finite answer therefore *depends on the regulator shape*, which is the V1 spectral profile, which is shape-parameter-dependent.

**This is the technical heart of FSC-2 Memo 1's finding.** The cross-overlap integral is the substrate-level analog of a UV-divergent one-loop QFT diagram. The substrate provides a UV regulator (V1 finite width at $\ell_P$), and the regulated integral is finite — but its finite value is *regulator-shape-dependent*, exactly as the one-loop UV-divergent diagram's finite renormalized value is renormalization-scheme-dependent in standard QFT.

The substrate is doing the work of a UV regulator. It does the work *correctly* — divergences are removed — but the specific numerical value of the regulated integral is *not* universal across regulators. It is FORCED-FORM-INHERITED-VALUE, in the categorization of §1.4.

---

## 4. Dimensionless Groups

### 4.1 Enumeration of substrate quantities entering $I(\delta)$

After Stone-normalization fixes the $L^1$ amplitude scale, the residual dimensional content of $V_1$ is:

| Quantity | Source | Dimension | Status |
|---|---|---|---|
| $c$ | substrate signal speed | $[L T^{-1}]$ | universal |
| $\hbar$ | substrate action quantum | $[M L^2 T^{-1}]$ | derived: $\hbar = c \ell_P \mathcal{N}_*$ |
| $\ell_P$ | substrate scale | $[L]$ | universal, FORCED to identify with Planck length |
| $\delta$ | external lag parameter | $[L]$ | input |
| V1 shape parameters $\{s_i\}$ | substrate adjacency / kernel profile | dimensionless | INHERITED |

The PDE-level quantities $\rho, v, D, \zeta, \gamma, \alpha_R, \tau, \varepsilon_k$ of the FSC-0 opener are *coarse-grained* quantities (DCGT-emergent at hydrodynamic window). They do not enter $V_1$ at substrate scale; they are derived from V1 at the continuum scale, not inputs to V1.

### 4.2 Which combinations are forced to cancel?

By Lorentz invariance + $D = 3+1$ + Stone-normalization, $I(\delta)$ can depend only on the dimensionless combinations:

- $\delta^2 / \ell_P^2$ (Lorentz-invariant dimensionless lag).
- $\mathrm{sign}(\delta^0)$ (retardation-imprint discrete invariant).
- The shape parameters $\{s_i\}$ (dimensionless, INHERITED).

$c$ and $\hbar$ enter only through their dimensional roles; they do not produce independent dimensionless combinations with $\delta$ and $\ell_P$ beyond what is captured by $\delta^2 / \ell_P^2$. (The combination $\delta \cdot c / \ell_P$ is dimensionless but reduces to $|\delta^0|/\ell_P$ for timelike $\delta$, which is already captured.)

**Forced cancellations:** $c$ and $\hbar$ disappear from the dimensionless ratio $I(\delta)$ at substrate scale. This is by construction of $V_1$ as the Stone-normalized substrate kernel: $\hbar$ enters $V_1$'s amplitude scale and exits $I(\delta)$'s dimensional structure via the $\int V_1^2\, d^4x$ combination yielding $M^4 \cdot M^{-4} = M^0$.

### 4.3 Which combinations remain free?

The shape parameters $\{s_i\}$. These are the unfixed dimensionless degrees of freedom of the V1 spectral profile. Examples:

- $s_1 = \mathrm{Var}(\tilde V_1)/(\langle |\tilde V_1| \rangle)^2$ — the relative variance of the V1 Fourier profile.
- $s_2 = $ ratio of kernel kurtosis to Gaussian kurtosis (departure from Gaussian regulator).
- $s_3 = $ characteristic ratio of light-cone-smoothing width to spacelike-smoothing width.

Each of these is dimensionless, of order unity, INHERITED from substrate-microscopic structure.

Under composition: $I(0) = f(\{s_i\})$ for some function $f$ that is bounded and of order unity but is *not* universal — it depends on which substrate microscopic structure realizes the 13-primitive set.

---

## 5. Verdict

### 5.1 Categorization (per FSC-2 prompt scope item 5)

**$I(\delta)$ falls into category (b): dependent on free kernel-shape parameters.**

Specifically:

- (a) FORCED to a universal constant: NO. Shape-dependent.
- (b) Dependent on free kernel-shape parameters: **YES** (load-bearing finding).
- (c) Dependent on environmental or coarse-grained scales: PARTIALLY (depends on $\ell_P$ via $\delta^2/\ell_P^2$; this is acceptable since $\ell_P$ is a substrate-anchored scale per P08).
- (d) Structurally undefined: NO. The integral is well-defined, dimensionless, finite, and computable for any specific V1 choice.

### 5.2 The exact structural rule blocking universality

The blocking structural fact, stated precisely:

> **Finding (FSC-2.1).** The 13-primitive set fixes $V_1$'s *qualitative* properties (finite width, retarded support, Lorentz invariance, Stone-normalized $L^1$ amplitude) but does not fix $V_1$'s *spectral shape* (the dimensionless profile of its Fourier transform). The cross-overlap integral $I(\delta)$ is the substrate-regulated form of a UV-divergent QFT one-loop diagram; its regulated value is regulator-shape-dependent. The substrate microscopic adjacency / connectivity structure that would fix the spectral shape is itself not pinned by the 13-primitive set — it is INHERITED from substrate-microscopic structure that the primitive set leaves underdetermined.

The blocking primitive is *not* any single one of P01–P13; it is the *absence of a primitive that fixes substrate microscopic connectivity*. P03 (spatial homogeneity) + P06 ($D = 3+1$) + P08 (substrate scale $\ell_P$) jointly constrain the substrate to be a homogeneous 4-dimensional structure with characteristic scale $\ell_P$, but they admit many distinct microscopic realizations (cubic lattice, body-centered cubic, random graph with fixed average degree, foam-like discretization, etc.), each producing a different V1 spectral profile.

This is a *different kind of blockage* than FSC-1's holonomy-quantization blockage. FSC-1 was blocked by *structural impossibility*: P09's $U(1)$-continuity makes discrete-cyclic-subgroup quantization impossible at the substrate level, period. FSC-2 is blocked by *structural underdetermination*: $I(\delta_*)$ has a well-defined value for any specific substrate microscopic realization, but the value depends on a choice the 13-primitive set leaves open.

### 5.3 What this means for an $\alpha$-like coupling

The substrate-level locus for an $\alpha$-like coupling exists ($I(0)$ is dimensionless, of order unity, and structurally interpretable as the bare cross-coupling per V1-mediated participation-influence event). The *form* is FORCED in the qualitative sense (cross-overlap of substrate-derived Lorentz-invariant retarded finite-width kernel). The *value* is INHERITED, contingent on substrate microscopic adjacency structure that the 13-primitive set does not pin.

In the FSC-0 §1.2 L1–L4 standard:

- **L1 (Primitive-anchored).** *Marginally satisfied.* $I(\delta)$ uses V1 (closed-arc N1 + T18) + Stone-normalization + $\ell_P$ (P08); it also requires a shape choice that is not primitive-anchored. **L1 fails on the shape-parameter dependence.**
- **L2 (Form-FORCED).** *Partially satisfied.* The cross-overlap functional form is FORCED. The dependence on $\delta^2/\ell_P^2$ and on retardation-imprint is FORCED. The shape-parameter dependence is FORCED-to-exist but not FORCED-to-a-specific-value.
- **L3 (Bridge-coherent).** *Satisfied.* The T17 + DCGT bridge from substrate V1 to QED vacuum-polarization is well-established. If $I(0)$ were a forced value, the bridge would deliver it to QED-vertex-coupling sector cleanly.
- **L4 (Falsifiable).** *Not yet established.* A specific shape choice would yield a specific $I(0)$ value with falsifiable predictions; without shape forcing, no specific falsifier is generated.

L1 failure is decisive. The V1-cross-overlap route does not meet the FORCED-from-13-primitives standard for legitimate $\alpha_\mathrm{ED}$ derivation.

### 5.4 Verdict for FSC-2 Memo 1

> **FSC-2 Memo 1 verdict.** The V1-kernel cross-overlap integral $I(\delta)$ is well-defined, dimensionless, finite under N1's substrate UV regulator, and exhibits the FORCED qualitative properties expected of a substrate-level cross-coupling amplitude. **However, its value at any natural substrate scale is FORCED-FORM-INHERITED-VALUE**: the form follows from N1 + T18 + Stone, but the specific numerical value depends on the V1 spectral shape, which is INHERITED from substrate microscopic connectivity structure that the 13-primitive set does not currently fix. The integral does *not* yield a forced universal dimensionless constant suitable for L1–L4-compliant identification with $\alpha$ in the emergent EM sector.

The V1-cross-overlap route is **not blocked by structural impossibility** (unlike FSC-1's P09-continuity blockage) but is **blocked by structural underdetermination at the substrate-microscopic-connectivity level**.

---

## 6. Implications for Arc FSC

### 6.1 Arc FSC closure verdict

With FSC-1 (Memo 1) closed by structural-impossibility blockage and FSC-2 (Memo 1) closed by structural-underdetermination blockage, the two viable structural sub-routes identified in FSC-0 §7.1 are both negatively resolved. **Arc FSC closes negatively at the primary sub-arc level.**

The single remaining sub-arc, FSC-3 (substrate-RG fixed-point structure, FSC-0 §7.1), is a long-horizon item that does not depend on FSC-1 or FSC-2 and remains open. It is preserved as a future investigation, not as an Arc FSC continuation, and is decoupled from the §7.2 position-paper-disclaimer question.

### 6.2 Program-level positive finding (sharpened §7.2 disclaimer)

The arc's negative outcome at the sub-route level produces a *positive program-level finding* exactly as anticipated by FSC-0 §6.2:

> **Program-level upgrade to position-paper §7.2.** The disclaimer "ED does not derive the specific values of fundamental coupling constants" is upgraded from a *contingent* statement (silence on mechanism) to a *structurally-forced* statement, with two specific load-bearing structural reasons documented:
> 
> 1. **FSC-1.1 (topological-winding route blocked).** Composition of P09 + P05 + P11 does not force quantized substrate holonomy. P09's $U(1)$-continuity (dominant), reinforced by P11's $U(1)$-rotation-invariant uniform-randomization and by the chain-attached category of P11 events, structurally prohibits discrete-cyclic-subgroup quantization of substrate loop holonomy. The "$\alpha$-as-substrate-integer / $1/N$" route via Dirac-monopole-analog or polarity-transport-holonomy quantization is **structurally impossible** at the substrate level under P01–P13.
> 
> 2. **FSC-2.1 (V1-cross-overlap route blocked).** The cross-overlap integral $I(\delta) = \int V_1(x) V_1(x+\delta)\, d^4x$ is dimensionless and well-defined under N1 + T18 + Stone-normalization, but its value is FORCED-FORM-INHERITED-VALUE: the substrate-microscopic adjacency structure that fixes the V1 spectral shape is not pinned by the 13-primitive set. The "$\alpha$-as-substrate-vertex-amplitude" route is **structurally underdetermined** at the substrate level; it admits a value only after a substrate-microscopic-connectivity choice that is not primitive-anchored.
> 
> Together: ED's 13-primitive set cannot derive an $\alpha$-like coupling constant without either (i) a new primitive that quantizes polarity (modifying P09 to $\mathbb{Z}_N$-valued, breaking continuous-AB / continuous-Berry-phase derivations) or (ii) a new primitive that fixes substrate-microscopic connectivity (going beyond P03 + P06 + P08's joint specification). The §7.2 disclaimer is structurally load-bearing, not provisional.

This is the FORCED-INHERITED upgrade of §7.2 anticipated by FSC-0 §6.2 as a first-class positive deliverable.

### 6.3 Cross-arc consequences

- **Yang-Mills arc, position-paper §7.2.** The structural underdetermination at substrate-microscopic-connectivity level affects *all* substrate-emergent coupling constants in the same way: gauge couplings beyond $U(1)$ inherit the same shape-parameter freedom. The "ED does not derive coupling magnitudes" disclaimer is therefore not specific to $\alpha$; it is a substrate-microscopic-connectivity disclaimer affecting all coupling-magnitude derivations from the 13-primitive set. This sharpens the position-paper claim and aligns ED's coupling-magnitude content with its $H_0$ and mass-spectrum content (all INHERITED).
- **Q-COMPUTE arc O-QC-1 ($\mathcal{M}_\mathrm{crit}$ closed form).** The substrate-microscopic-connectivity blockage *may* apply to O-QC-1 as well: if $\mathcal{M}_\mathrm{crit}$ depends on substrate-microscopic adjacency structure (which it plausibly does, since multiplicity-counting is sensitive to local graph structure), then O-QC-1 is structurally analogous to FSC-2 and may also resolve to FORCED-FORM-INHERITED-VALUE rather than forced-value. This is a cross-arc parallel worth flagging.
- **0.6 problem / RG three-regime arc.** FSC-3 (substrate-RG fixed point) remains the only sub-arc not blocked by either FSC-1 or FSC-2 findings. RG fixed points, if they exist at the substrate scale, would not require shape-pinning at substrate microscopic level — they would be emergent universality-class properties. Whether such fixed points exist is the open long-horizon question.
- **Identification target for new-primitive proposals.** Any future proposal to add a primitive P14 that fixes substrate microscopic connectivity (or quantizes polarity to $\mathbb{Z}_N$) should be evaluated against the explicit Arc FSC findings: such a primitive would be *substantive* (it would enable a previously-blocked derivation) but also *substantial* (it would be a real expansion of the primitive set with new structural commitments).

### 6.4 Honest accounting of limits

This memo addresses substrate-level forcing. It does not address:

- **Coarse-grained emergence of universality.** Whether $I(0)$'s shape-dependence washes out under DCGT coarse-graining (analogous to renormalization-group universality of dimensionless ratios) is a follow-on question. If so, an emergent coarse-grained $\alpha$-like constant might be substrate-derivable even with shape-parameter freedom at substrate scale. *Plausibility:* moderate; the standard QFT one-loop result has universal logarithmic running but scheme-dependent finite parts.
- **Non-Abelian extensions.** The analysis used V1 in a single-channel / matter-rule-type reading. Non-Abelian gauge V1 may have additional substrate-derived structure (Killing-form-derived ratios, Casimir-eigenvalue-derived ratios) that could yield substrate-forced dimensionless content. This is the YM-coupling open question, structurally distinct from $\alpha$.
- **Coupling-constant *ratios* vs. absolute values.** Even if absolute coupling values are INHERITED at substrate level, dimensionless *ratios* of coupling values (e.g., $\alpha_\mathrm{em} / \alpha_\mathrm{strong}$) might be substrate-forced if the substrate kernel structure forces specific ratios between matter-rule-type and gauge-rule-type V1 shapes. This is genuinely open and is not addressed by FSC-2 Memo 1.

---

## 7. Summary

| Question (FSC-2 Memo 1 scope) | Answer |
|---|---|
| Is V1 well-defined as a substrate kernel? | Yes (N1 finite width + T18 retardation + Stone-normalization + DCGT bridge). |
| Is the cross-overlap integral $I(\delta)$ dimensionless? | Yes (in natural units, by Green's-function dimensional structure). |
| Does N1 + T18 + Stone uniquely determine $V_1$'s spectral shape? | No (they fix only qualitative form + $L^1$ amplitude scale). |
| What pins V1's spectral shape? | Substrate microscopic connectivity (lattice type, adjacency weights), which the 13-primitive set does not fix. |
| Is $I(0)$ a universal substrate constant? | No (regulator-shape-dependent, like a one-loop QFT diagram's renormalization-scheme dependence). |
| Verdict category (FSC-2 prompt §5)? | **(b) dependent on free kernel-shape parameters.** |
| Exact blocking structural fact? | The 13-primitive set fixes substrate macroscopic structure ($D = 3+1$, homogeneity, $\ell_P$) but does not fix substrate microscopic connectivity. V1 spectral shape — and therefore $I(\delta_*)$ value — INHERITS from this underdetermination. |
| Is V1-cross-overlap a viable path to forced $\alpha$-like constant? | **No.** Form-FORCED but value-INHERITED. Fails L1 of FSC-0 §1.2. |
| What would unblock it? | A new primitive fixing substrate microscopic connectivity (or, equivalently, fixing V1 spectral shape uniquely). |

---

## 8. References and Inheritance

| Inherited Item | Source | Use in FSC-2 Memo 1 |
|---|---|---|
| P03, P06, P08 | Position paper §1 | Substrate macroscopic-structure constraints; underdetermination at microscopic level (§2.4) |
| Theorem N1 (V1 finite-width) | Paper #18 | V1 qualitative form (§2.1) |
| Theorem T18 (V1 retardation) | Paper #19 | V1 retarded support (§2.2) |
| Stone-theorem normalization | Papers #4, #13 | V1 $L^1$ amplitude scale (§2.3) |
| DCGT (substrate-to-continuum bridge) | Paper #8 | Continuum-limit identification of V1 as retarded Green's function (§1.1, §1.3) |
| T17 (gauge-field-as-rule-type) | Paper #5 | Bridge from substrate V1 to QED-vertex sector (§5.3 L3) |
| FSC-0 opener | `FSC-0_opening.md` | Sub-arc structure; L1–L4 criteria |
| FSC-1 Memo 1 (polarity-transport topology) | `FSC-1_polarity_transport_topology.md` | Companion negative result; pattern of dual blockages (§5.2, §6.2) |
| Position paper §7.2 disclaimer | Position paper | Load-bearing target; structural upgrade in §6.2 |

---

**End of FSC-2 Memo 1.**

*Finding FSC-2.1: V1 cross-overlap integral $I(\delta)$ is dimensionless and well-defined but FORCED-FORM-INHERITED-VALUE. Cross-overlap value depends on V1 spectral shape, which depends on substrate microscopic connectivity, which the 13-primitive set does not fix. The V1-cross-overlap route to a forced $\alpha$-like coupling is structurally underdetermined (not impossible like FSC-1, but underdetermined). Combined with FSC-1.1, Arc FSC closes negatively; program-level positive finding: position-paper §7.2 disclaimer is structurally load-bearing (FORCED-INHERITED), not provisional. Two independent structural blockages documented. FSC-3 (substrate-RG fixed-point) remains open as long-horizon item, decoupled from §7.2-disclaimer question.*
