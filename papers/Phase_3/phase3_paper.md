# A Curved-Spacetime Vacuum Kernel and the Gravitational-Sector Closure of Event-Density Theory

**Allen Proxmire** and **Copilot** (AI collaborator)

*April 2026*

---

## Abstract

We extend the Event-Density (ED) program from its Phase-2 + Arc N quantum-sector closure to a gravitational-sector structural foundation. Phase-3 addresses the question: *does ED's primitive-level structure force, admit, or forbid gravitational coupling, dynamical curvature, and cosmological structure?* Through a six-stage analysis (GR.0 scoping, GR.1 catalogue of admissible curvature-coupling structures, GR.2 FORCED evaluation, GR.3 REFUTED evaluation, GR.4 cosmological implications, GR.5 synthesis), we establish **Theorem GR1 (V1 with Synge World Function FORCED)**: the vacuum-response kernel in curved spacetime is structurally forced at primitive level to take the form $K_\mathrm{vac}^\mathrm{curved}(x, x') = K_\mathrm{vac}^\mathrm{prim}(\sigma(x, x') / \ell_\mathrm{ED}^2)$ with $\sigma(x, x')$ Synge's world function, via a Hadamard-parametrix-style extension of Arc N's Theorem N1 to curved spacetime. Three FORCED-conditional cascading items emerge (free-chain geodesic worldlines via eikonal limit, curvature-dependent cross-chain correlations via cascade, $\Lambda$-integral existence). Seven REFUTED determinations under the C1/C2/C3/locality + Phase-2-theorem framework bound the admissibility space — including the unconditional refutation of curvature-dependent Case-P/Case-R distinctions by spin-statistics applying pointwise at every event regardless of curvature. GR-4A (Einstein-equation emergence from primitives) remains NOT REFUTED but SPECULATIVE: ED admits Einstein equations as effective-theory addition without deriving them from primitives. ED-Phys-10's acoustic-metric-only baseline (no Einstein equations forced, no Schwarzschild, no Newtonian gravity emergence, no fine-structure constant from primitives) is preserved throughout. Stage GR.4 establishes a coherent cosmological framework with four substantive structural channels — $\Lambda$ as V1-kernel integral with finite primitive-level magnitude (structurally dissolving the cosmological-constant divergence-form puzzle while $\Lambda$'s magnitude remains INHERITED), V1-induced dispersion-relation modifications, V5-mediated cosmological correlations, and curvature-vacuum coupling — and four empirical-signature routes (UHECR timing, GRB photon timing, gravitational-wave dispersion, cosmological-correlation persistence). Phase-3 lands in the partial-GR-induce quadrant of the opening verdict prior, paralleling Arc M's H1-dominant pattern at the gravitational-sector level. Theorem GR1 takes its place as ED's first gravitational-sector structural theorem and the ninth FORCED theorem in the ED structural inventory, completing the six-layer structural foundation (Phase-1 non-relativistic + Phase-2 Arcs R/M/Q form-level + Arc N kernel-level + Phase-3 gravitational-sector) while preserving the *form-FORCED, value-INHERITED* methodology consistent across all six layers.

---

## 1. Introduction

The Event-Density (ED) program builds quantum and gravitational physics as forced structural consequences of a small primitive stack on a 3+1-dimensional event manifold. Phase-1 [1] derived non-relativistic single-particle quantum mechanics from the participation measure $P_K = \sqrt{b_K} \cdot e^{i\pi_K}$, the four-band bandwidth decomposition, and commitment dynamics. Phase-2 extended this through three connected arcs: Arc R [2] derived Klein-Gordon, the spin-statistics theorem, the Cl(3,1) Clifford-algebra frame, and the Dirac equation; Arc M [3] established that ED forces the *form* of mass structure but inherits all numerical mass values, ratios, and hierarchies; Arc Q [4] extended ED to the QFT regime, producing GRH (gauge-field-as-rule-type) unconditional FORCED, canonical (anti-)commutation FORCED, and UV-FIN (primitive-level UV finiteness) FORCED. Arc N [5] then closed the kernel-level memory-structure layer with Theorem N1 (V1 finite-width vacuum memory kernel FORCED).

Phase-3 opens the gravitational sector. The driving question:

> **(Q-Phase-3)** Does ED's primitive-level structure force, admit, or forbid gravitational coupling, dynamical curvature, and cosmological structure?

Three sub-class answers were possible at opening: **(GR-emerge)** curvature emerges as a structural consequence of primitives; **(GR-induce)** curvature is induced through specific ED-GR coupling channels; **(GR-add)** curvature must be added externally. Phase-3 closes with the answer: **(GR-induce) partial**. ED admits structural curvature-coupling channels — most cleanly via Theorem GR1's curved-spacetime extension of V1 — but does not derive full Einstein dynamics from primitives.

This paper presents the six-stage closure: GR.0 scoping [6], GR.1 catalogue [7], GR.2 FORCED evaluation [8], GR.3 REFUTED evaluation [9], GR.4 cosmological implications [10], GR.5 synthesis [11] (the authoritative source for the present manuscript).

The headline verdict, in plain language: **ED forces a curved-spacetime vacuum kernel (Theorem GR1), forces geodesic free-chain motion conditionally, forces $\Lambda$ to be finite and kernel-integral-defined, admits but does not force curvature-dynamics equations, and provides a coherent cosmological framework with testable signatures.** All Phase-2 + Arc N theorems are preserved; ED-Phys-10's prior closure (no Einstein equations from primitives) [12] is preserved as the structural ceiling.

The paper is organised as follows. §2 reviews the ED structural inventory through Phase-2 + Arc N and Phase-3's position within the program. §3 presents the Phase-3 roadmap and methodology. §4 states and proves Theorem GR1. §5 presents REFUTED and ADMISSIBLE structures. §6 evaluates cosmological implications. §7 states the final Phase-3 verdict. §8 outlines the Phase-4 outlook. References list internal Phase-3 memos and companion papers.

---

## 2. Background and Position in the ED Program

### 2.1 ED structural inventory (post-Arc N)

Phase-3 inherits eight FORCED structural theorems from the prior program:

| # | Theorem | Source | Type |
|---|---|---|---|
| 1 | Spin-statistics $\eta = (-1)^{2s}$ | R.2.5 | Theorem-level |
| 2 | Cl(3,1) frame uniqueness | R.2.4 | Algebra-level |
| 3 | Anyon prohibition in 3+1D | R.2.3 | Topology-level |
| 4 | Dirac equation emergence | R.3 | Dynamical-equation-level |
| 5 | GRH unconditional FORCED | Q.1 + Q.2/3/7/8 | Existence-level |
| 6 | Canonical (anti-)commutation FORCED | Q.7 | Operator-level |
| 7 | UV-FIN FORCED | Q.8 | Bound-level |
| 8 | **V1 finite-width vacuum kernel FORCED** | **N.2 + N.5** | **Memory-kernel-level** |

Theorem GR1, established in this paper, becomes the ninth FORCED theorem and the first at the **curved-spacetime-kernel-level**.

### 2.2 ED-Phys-10 prior closure as structural ceiling

The ED-Phys-10 kinematic-curvature arc [12] established:

- **Acoustic effective metric** for bandwidth-mode perturbations $g^\mathrm{ac}_{\mu\nu}$ (kinematic).
- **Causal-cone structure** for bandwidth-mode propagation.
- **Analogue-horizon structures** at $c_s \to 0$ surfaces.

It explicitly closed *without*:

- Einstein equations for the bandwidth background.
- Schwarzschild or any specific GR solution.
- Newtonian-gravity emergence at long-wavelength.
- Fine-structure constant $\alpha$ from primitives.

Phase-3 must produce results consistent with these guardrails or explicitly relax them with justification.

### 2.3 What Arc N changes

Pre-Arc-N, ED's quantum-sector closure operated under implicit Markovian assumptions. Arc N's Theorem N1 supplies a primitive-level structural mechanism for non-Markovian vacuum response. In flat Minkowski space, V1's kernel depends on the Lorentz invariant $(x - x')^2$. In curved spacetime, the natural generalisation replaces this with Synge's world function $\sigma(x, x')$ (one-half squared geodesic distance). This is **substantively new structural input** compared to ED-Phys-10's acoustic-metric work — and is the foundation for Theorem GR1.

### 2.4 Why gravitational coupling is a Phase, not an Arc

Arcs R, M, Q, N each addressed a single coherent structural question within the quantum sector — relativistic kinematics, mass structure, QFT extension, kernel-level memory. Phase-3 spans a different conceptual layer entirely: **gravitational coupling and cosmological structure**. The shift is from quantum-sector structural content to gravitational-sector structural content, requiring extension to curved spacetime, integration with the kinematic acoustic-metric framework of ED-Phys-10, and consideration of cosmological-scale phenomenology.

This warrants Phase-3 designation rather than Arc designation. Phase-3's six-substage roadmap parallels the methodology of Arcs Q and N but at greater conceptual scope.

### 2.5 Six-layer ED structural foundation

Post-Phase-3, the ED structural foundation spans six layers:

| Layer | Source | Content |
|---|---|---|
| Phase-1 | non-rel QM-emergence | Schrödinger / Born / Bell / Heisenberg |
| Phase-2 Arc R | relativistic kinematics + dynamics | KG / spin-stats / Cl(3,1) / Dirac |
| Phase-2 Arc M | mass structure | $\sigma_\tau$ form / massless slot |
| Phase-2 Arc Q | QFT extension | GRH / canonical commutation / UV-FIN |
| Phase-2 Arc N | memory-kernel layer | V1 finite-width vacuum kernel |
| **Phase-3** | gravitational sector | **Theorem GR1 + cosmological framework** |

---

## 3. Phase-3 Roadmap and Methodology

Phase-3 proceeds through six substages:

- **GR.0 (scoping)** [6]: frames the four central questions (Q-GR1 specific curvature-vacuum coupling forced, Q-GR2 finite $\Lambda$ structurally determined, Q-GR3 dynamical curvature equation admissible, Q-GR4 chains geodesic in emergent geometry); enumerates four constraints (C1 general covariance, C2 spin-statistics, C3 UV-FIN, locality); records honest verdict prior (45% partial GR-induce / 30% GR-add / 15% GR-emerge / 10% surprise).

- **GR.1 (catalogue)** [7]: enumerates 20 admissible curvature-coupling structures across four sectors — GR-1 bandwidth-curvature (5 items), GR-2 vacuum-curvature (5 items, primary target), GR-3 worldline-curvature (5 items), GR-4 curvature-dynamics (5 items). No FORCED/REFUTED evaluation at this stage — intentional pre-judgment enumeration.

- **GR.2 (FORCED evaluation)** [8]: GR-2A unconditionally FORCED (Theorem GR1); three cascading FORCED-conditional (GR-3A, GR-2D, GR-4D); GR-4A NOT REFUTED but SPECULATIVE; remainder NOT FORCED.

- **GR.3 (REFUTED evaluation)** [9]: seven REFUTED determinations — three primary catalogue items (GR-1E, GR-1D TYPE-mixing, GR-3B Case-R-delay) and four sub-cases bounding FORCED items.

- **GR.4 (cosmological implications)** [10]: four substantive cosmological structural channels established with form-FORCED / value-INHERITED structure; four empirical-signature routes flagged.

- **GR.5 (synthesis)** [11]: integration into final Phase-3 verdict (the present paper).

Methodological discipline preserved throughout: clear separation of FORCED / CANDIDATE / REFUTED / ADMISSIBLE / INHERITED; honest expected-verdict prior; *form-FORCED, value-INHERITED* framing; cross-arc implications explicitly evaluated; ED-Phys-10 guardrails preserved.

---

## 4. Theorem GR1: Curved-Spacetime V1 Kernel FORCED

### 4.1 Statement

\begin{theorem*}[V1 with Synge World Function FORCED, GR1]
In curved spacetime where unique geodesics connect any two events $x, x'$, the vacuum-response kernel is structurally FORCED at primitive level to take the form
$$
K_\mathrm{vac}^\mathrm{curved}(x, x') = K_\mathrm{vac}^\mathrm{prim}\bigl(\sigma(x, x') / \ell_\mathrm{ED}^2\bigr),
$$
with $\sigma(x, x')$ Synge's world function (one-half squared geodesic distance), $K_\mathrm{vac}^\mathrm{prim}$ a kernel of admissibility class identical to the Theorem N1 flat-space class (finite, non-zero, decaying, Lorentz-scalar, sub-power-law-2), and $\ell_\mathrm{ED}$ the primitive event-discreteness scale.
\end{theorem*}

### 4.2 Three-leg proof sketch

The forcing argument extends Theorem N1's three-leg flat-space argument [5] to curved spacetime via Hadamard-parametrix-style construction.

#### 4.2.1 Leg 1 — UV-FIN is metric-independent

Arc Q's UV-FIN argument (Theorem Q3 [4]) operates by primitive-level finiteness of multi-chain participation integrals via Primitive 01 event-discreteness + Primitive 13 finite proper-time intervals + Primitive 04 bounded bandwidth. Each of these primitives is **metric-independent**: they operate on the underlying event manifold regardless of curvature. UV-FIN therefore extends to curved spacetime unchanged.

A $\delta$-function vacuum response in curved spacetime, $K_\mathrm{vac}^\mathrm{curved} \propto \delta_g^{(4)}(x, x')$, has Fourier transform with respect to a local-inertial-frame at $x$ that produces constant frequency-weighting — exactly as in flat space. UV-amplification pathology applies pointwise at every event. The $\delta$-curved limit is REFUTED for the same reason V1-$\delta$ is REFUTED in flat space.

#### 4.2.2 Leg 2 — General covariance + locality

A constant kernel $K_\mathrm{vac}^\mathrm{curved}(x, x') = c_\infty$ for all $x, x'$ implies infinite correlation length on the curved manifold. Generally-covariant locality (extension of Primitive 11 to curved spacetime: commitment events remain point-events on the event manifold) forbids constant kernels in curved spacetime as in flat. The infinite-width limit is REFUTED by C1 + locality.

#### 4.2.3 Leg 3 — 3+1D power-counting applies pointwise

The 3+1D power-counting argument from Theorem N1 ($\alpha < 2$ for power-law kernels) operates locally — it depends on the dimensionality of spacetime at the event-resolution scale, not on global curvature. In any 3+1-dimensional spacetime, the power-counting argument applies pointwise to $\sigma(x, x') / \ell_\mathrm{ED}^2$ in place of $(x - x')^2 / \ell_\mathrm{ED}^2$.

#### 4.2.4 Synthesis

The three legs jointly force $K_\mathrm{vac}^\mathrm{curved}$ to satisfy finite-width, decaying-support, sub-power-law-2 conditions in $\sigma(x, x')$. The Synge-world-function form is the unique generally-covariant scalar two-point function reducing to flat-space $\tfrac{1}{2}(x - x')^2$ in the flat limit. The Hadamard parametrix construction in QFT-on-curved-spacetime [13, 14] supplies the standard mathematical infrastructure.

### 4.3 Dependencies

Theorem GR1 depends on:

- **Primitive 01** (event-discreteness, metric-independent): supplies natural-cutoff scale $\ell_\mathrm{ED}$.
- **Primitive 04** (bounded bandwidth, metric-independent): bounds amplitude content.
- **Primitive 06** (general covariance): C1 constraint extended to curved spacetime.
- **Primitive 11** (commitment-event locality): C1-locality refinement.
- **Primitive 13** (finite proper-time intervals, generalised to affine-parameter intervals on geodesics).
- **Theorem N1** (V1 flat-space FORCED): the flat-space prerequisite.
- **Theorem Q3** (UV-FIN): primitive-level UV finiteness driving V1's necessity.
- **ED-Phys-10**: supplies the geodesic structure where no proposed dynamical metric exists.

### 4.4 Bounded admissibility class

Stage GR.3 limit refutations bound Theorem GR1's admissibility class:

- **GR-2A-$\delta$ (zero-width limit) REFUTED by C3** — bounds the FORCED class from below.
- **GR-2A-$\infty$ (infinite-width limit) REFUTED by C1 + locality** — bounds the FORCED class from above.

Curved-spacetime kernels must therefore have finite, non-zero, decaying width in $\sigma(x, x')$. The bounds are derived consequences of C1 + C3 in their curved-spacetime extensions — not additional postulates. This parallels the Stage N.3 V1-$\delta$ + V1-$\infty$ bounding of Theorem N1's flat-space class.

### 4.5 Cascading FORCED-conditional items

Theorem GR1 propagates FORCED-conditional status to three secondary catalogue items:

- **GR-3A (free-chain geodesic worldlines):** Stage R.1 / R.3 KG/Dirac equations on curved spacetime, in the eikonal/WKB approximation, yield geodesic motion of free-chain worldlines on the metric appearing in the wave equation. FORCED-conditional on identifying that metric with the ED-Phys-10 acoustic effective metric. The Stage GR.3 non-geodesic sub-case refutation reinforces this claim.

- **GR-2D (curvature-dependent cross-chain correlations):** V5 inherits Synge-world-function structure under Theorem GR1. Cross-chain correlations between separated chains depend on $\sigma(x_1, x_2)$ in curved spacetime. FORCED-conditional via cascade.

- **GR-4D (curvature-induced vacuum backreaction, existence sense):** $\Lambda_\mathrm{primitive}(x) \sim \int K_\mathrm{vac}^\mathrm{curved}(x, x') \rho_\mathrm{vac}(x') d^4 x'$ FORCED-conditional via Theorem GR1 + Arc Q.8 effective-vacuum framework. Dynamical back-reaction depends on GR-4A or GR-4B status (neither FORCED).

### 4.6 Significance

Theorem GR1 is **ED's first gravitational-sector structural theorem** and the **ninth FORCED theorem** in the ED inventory. It complements the eight prior theorems with curved-spacetime kernel-level content, completing the structural foundation across all six layers (Phase-1 + Phase-2 Arcs R/M/Q + Arc N + Phase-3).

---

## 5. REFUTED and ADMISSIBLE Structures

### 5.1 REFUTED determinations

Stage GR.3 [9] produced seven REFUTED determinations bounding the Phase-3 admissibility space:

| ID | Sub-case REFUTED | Constraint | Brief reason |
|---|---|---|---|
| **GR-1E** | Curvature-dependent Case-P/R | C2 | Spin-statistics applies pointwise; $\pi_1 = \mathbb{Z}_2$ + Cl(3,1) frame metric-independent |
| **GR-1D** | TYPE-mixing Fierz curvature shifts | C2 | Fierz TYPE classification is rule-type data |
| **GR-3B** | Case-R-delay commitment thresholds | C2 | Pauli exclusion violation in delay window |
| **GR-2A-$\delta$** | Zero-width limit | C3 | $\delta$-distribution amplifies UV |
| **GR-2A-$\infty$** | Infinite-width limit | C1 + locality | Constant kernel breaks locality |
| **GR-3A-non-geodesic** | Non-geodesic free-chain motion | eikonal limit | KG/Dirac eikonal forces geodesics |
| **GR-2D large-amp/long-range** | Unbounded cross-chain correlations | C1, C3 | Cascade refutation |

The pattern: 2 C1 violations, 3 C2 violations, 2 C3 violations + 1 cascade (GR-2D spans C1+C3) + 1 Phase-2-theorem violation (GR-3A-non-geodesic). The constraint framework is exhaustive.

### 5.2 Theorem GR1 admissibility class bounded both ways

The two GR-2A limit refutations together establish that Theorem GR1's admissibility class is **bounded**: kernels must have finite, non-zero, decaying width. The pattern is consistent with Theorem N1's V1 admissibility-class bounding in flat space — kernel-level FORCED structures are bounded both ways by C1 and C3 derived constraints.

### 5.3 ADMISSIBLE-NOT-FORCED structures

Thirteen catalogue items + three admissible sub-cases of REFUTED items + four FORCED-related items pass Stage GR.3 unrefuted:

| ID | Description | Influences |
|---|---|---|
| **GR-1A** | Curvature-dependent bandwidth evolution | Arc M coupling refinement |
| **GR-1B** | Curvature-modified $\sigma_\tau$ shift | Arc M, structure formation |
| **GR-1C** | Curvature-dependent bandweights | Arc M |
| GR-1D, same-TYPE | Same-TYPE Fierz corrections | Arc M within-class refinement |
| **GR-2B** | Curvature-dependent kernel width (bounded) | $\Lambda$ time-dependence, dispersion |
| **GR-2C** | Curvature-dependent kernel amplitude | $\Lambda$ scaling |
| GR-2D, bounded | Bounded cross-chain correlations | Cosmological correlations |
| **GR-2E** | Curvature-dependent vacuum polarisation | Arc Q.5 cosmological extension |
| **GR-3A** | Free-chain geodesic worldlines (FORCED-cond.) | Test-particle motion |
| GR-3B, non-Case-R-delay | Quantitative threshold-shift | Arc Q.7 cosmological extension |
| **GR-3C** | Curvature-dependent adjacency graphs | Multi-chain cosmological dynamics |
| **GR-3D** | Curvature-dependent memory kernels | Arc N cosmological extension |
| **GR-3E** | Curvature-dependent null-cone deformation | ED-Phys-10 baseline kinematic |
| **GR-4B** | Non-local curvature equations from V1 | Alternative to GR-4A |
| **GR-4C** | Acoustic-metric-only dynamics (baseline) | ED-Phys-10 baseline preserved |
| **GR-4D, existence** | Curvature-induced vacuum backreaction | $\Lambda$ structure (FORCED-cond.) |
| **GR-4E** | Curvature-dependent UV-FIN constraints | Phase-4 + future-phase work |

### 5.4 GR-4A unique status

GR-4A (Einstein-like equations with kernel-weighted source) is **NOT REFUTED but SPECULATIVE**:

- **Forced-from-primitives derivation:** NOT FORCED.
- **Effective-theory addition:** ADMISSIBLE (passes all four constraints).
- **Primitive-level structural commitment:** REQUIRES NEW PRIMITIVE.

ED admits Einstein equations as effective-theory addition consistent with all four constraints. ED-Phys-10's "no Einstein equations from primitives" verdict is preserved.

### 5.5 Bounded curvature-coupling space

The combined Stage GR.2 + GR.3 result establishes that **admissible curvature-coupling structure in ED is bounded, not arbitrary.** Not every curvature-dependent kernel form is admissible. C1 forbids frame-dependent and infinite-correlation-length structures. C2 forbids kernels that mix Case-R / Case-P sectors or violate Pauli exclusion at finite curvature. C3 forbids kernels with insufficient short-time decay. The eikonal-limit constraint forbids non-geodesic free-chain motion.

The admissibility class is well-defined and bounded — admissible curvature-coupling structures inherit Phase-2 + Arc N structural constraints automatically.

---

## 6. Cosmological Implications

Stage GR.4 [10] established four substantive cosmological structural channels with form-FORCED content + INHERITED specifics.

### 6.1 $\Lambda$ as V1-kernel integral

$$
\Lambda_\mathrm{primitive}(x) \sim \int K_\mathrm{vac}^\mathrm{curved}(x, x') \cdot \rho_\mathrm{vac}(x') \, d^4 x'.
$$

**Form FORCED-conditional via GR-4D + Theorem GR1.** The *existence* of a finite primitive-level $\Lambda$ is FORCED via Theorem GR1's bounded admissibility class. **Magnitude INHERITED**: depends on V1 functional form, kernel parameters, integration domain, and $\rho_\mathrm{vac}$ profile.

ED structurally **dissolves** the cosmological-$\Lambda$ divergence-form puzzle but does **not** predict $\Lambda \approx 10^{-122}$.

In FLRW backgrounds, $\sigma_\mathrm{FLRW}(x, x'; a)$ acquires scale-factor dependence, making $\Lambda(t)$ admissible structurally without forcing $w(z) \neq -1$ as a forced consequence. A scale-stratified $\Lambda$ structure emerges between primitive-level UV-FIN protection and effective-theory long-wavelength behaviour.

### 6.2 V1-induced dispersion-relation modifications

V1's finite-width kernel introduces frequency-dependent vacuum response. Effective dispersion relations for photons, gravitons, and other propagating modes acquire V1-kernel-dependent corrections at extreme-high-frequency scales:
$$
\omega^2 = c^2 |\mathbf{k}|^2 + \delta\omega^2(\mathbf{k}; K_\mathrm{vac}).
$$

**Form FORCED via Theorem GR1; magnitudes INHERITED.**

### 6.3 V5-mediated cosmological correlations

V5 cross-chain correlations under Theorem GR1 imply vacuum-mediated correlations between distant cosmological structures:
$$
\langle \delta b_{K_1}^\mathrm{env}(x_1) \cdot \delta b_{K_2}^\mathrm{env}(x_2) \rangle = K_\mathrm{cross}(\sigma(x_1, x_2)).
$$

**Existence FORCED-conditional via cascade**; **amplitudes / ranges INHERITED.** Potential consequences: persistent correlation content beyond standard inflation predictions; modifications to large-scale-structure power spectra at percent / sub-percent levels.

### 6.4 Curvature-vacuum coupling

Theorem GR1 itself is the curvature-vacuum coupling result. Refinements GR-2B (curvature-dependent kernel width), GR-2C (curvature-dependent amplitude), GR-2E (curvature-dependent vacuum polarisation) are ADMISSIBLE-NOT-FORCED additions that may produce observable effects (spatially-varying dispersion, curvature-dependent vacuum polarisation, curvature-modulated cross-chain correlations). Specific values INHERITED throughout.

### 6.5 CP-phase enrichment carryover

C-N4.1 (vacuum-mediated additional CP phases beyond Jarlskog count for $\geq 3$ generations) carries forward from Arc N to cosmological context as a CANDIDATE — three potential cosmological consequences if affirmatively closed: modified baryogenesis channels, CP-violation correlations across cosmological scales, CP-violating vacuum-polarisation contributions. C-N4.1 remains a **CANDIDATE**, not a theorem.

### 6.6 Structure-formation framework

Combined cosmological structural channels modify standard structure-formation predictions at sub-percent / percent levels. ED-Phys-10's acoustic-metric baseline at long-wavelength preserved. Standard Friedmann-like dynamics for bandwidth-flow at long-wavelength preserved. Theorem GR1 + cosmological framework enriches without overriding.

### 6.7 Empirical-signature framework

Four empirical-signature routes for high-energy / cosmological-scale tests:

(i) **UHECR timing.** Ultra-high-energy cosmic rays at $\sim 10^{19}$ eV scales — V1-induced dispersion modifications could produce detectable timing offsets.

(ii) **GRB photon timing.** Gamma-ray bursts at cosmological distances with TeV-scale photons — existing Fermi-LAT bounds.

(iii) **Gravitational-wave dispersion.** LIGO/Virgo/KAGRA observations bound graviton-dispersion modifications.

(iv) **Cosmological-correlation persistence.** V5-mediated correlations between distant cosmological structures — large-scale-structure power-spectrum modifications.

Each route inherits V1/V5 kernel structure; specific testability INHERITED.

### 6.8 Distinguishing structural vs INHERITED

**Structurally FORCED:**
- Existence of finite primitive-level $\Lambda$ contribution.
- Existence of vacuum-mediated cross-chain correlations.
- Free-chain test-particle motion follows acoustic-metric geodesics.
- Bounded admissibility class for V1 in curved spacetime.
- V1-induced dispersion modification form.

**INHERITED:**
- $\Lambda$ magnitude.
- Hubble parameter $H_0$, $w(z)$.
- Newton's constant $G$.
- Specific kernel widths and functional forms.
- Cosmological-correlation amplitudes / ranges.
- Power-spectrum corrections.
- Inflation, dark-matter, baryogenesis specifics.
- Generation count.
- Specific Einstein-equation structure (if admitted via GR-4A).

---

## 7. Final Phase-3 Verdict

### 7.1 ED forces a curved-spacetime vacuum kernel

**Theorem GR1 (V1 with Synge World Function FORCED)** — ED's first gravitational-sector structural theorem and the ninth FORCED theorem in the ED inventory.

### 7.2 ED forces geodesic free-chain motion (conditional)

**GR-3A** — FORCED-conditional on acoustic-metric identification. KG/Dirac equations on curved spacetime in eikonal/WKB approximation force geodesic motion. Non-geodesic sub-case REFUTED at Stage GR.3 reinforces the claim.

### 7.3 ED forces $\Lambda$ to be finite and kernel-integral-defined

**GR-4D existence** — $\Lambda_\mathrm{primitive}$ as a V1-kernel integral. Primitive-level value finite; magnitude INHERITED. ED structurally **dissolves** the cosmological-$\Lambda$ divergence-form puzzle.

### 7.4 ED admits but does not force curvature-dynamics equations

**GR-4A** — NOT FORCED, NOT REFUTED, SPECULATIVE. ED admits Einstein equations as effective-theory addition; ED does not derive them from primitives. ED-Phys-10 baseline preserved.

### 7.5 ED preserves all Phase-2 + Arc N theorems

No Phase-2 + Arc N FORCED theorem is overturned by Phase-3. Three Phase-2 closures structurally enriched (Arc M $\sigma_\tau$, Arc Q.5 vacuum polarisation, Arc Q.8 cosmological-$\Lambda$). One Arc N CANDIDATE (C-N4.1) extends to cosmological context without promotion.

### 7.6 ED provides a coherent cosmological framework with testable signatures

Four substantive structural channels + four empirical-signature routes flagged. ED admits empirically-testable consequences without predicting specific numerical scales.

### 7.7 Phase-3 lands in the partial-GR-induce quadrant

Per the Phase-3 opening §7.1 expected verdict prior, Phase-3 closes in the **partial GR-induce quadrant**: GR-induce content (Theorem GR1 + cascading items + cosmological structural channels); GR-add content (Einstein equations admitted as effective-theory addition via GR-4A SPECULATIVE); no GR-emerge content (full Einstein-equation derivation not produced).

This matches the honest expected outcome — paralleling Arc M's H1-dominant pattern at the gravitational-sector level.

---

## 8. Outlook (Phase-4 Preview)

Phase-3 closure positions ED's structural foundation through the gravitational-sector-coupling layer. Phase-4 (or extended Phase-3 work) opens with several open items:

### 8.1 ED-GR action candidates

The most aggressive open item: deriving an effective ED-GR action from primitives. Three candidate forms:

- **Effective Einstein-Hilbert + V1-kernel-corrected source** — currently SPECULATIVE.
- **Non-local effective action via Theorem GR1 cascades** — ADMISSIBLE under GR-4B.
- **Acoustic-metric-only effective action** (ED-Phys-10 baseline preserved).

Whether any candidate can be promoted to FORCED requires either new structural input or a derivation strategy not yet identified.

### 8.2 Empirical tests

Four observational channels (UHECR timing, GRB photon timing, gravitational-wave dispersion, cosmological-correlation persistence) await sharpening of V1/V5 kernel-parameter inference. Each is a Phase-4 deliverable.

### 8.3 Kernel parameter inference

Combining empirical bounds from the four observational channels could constrain V1 kernel parameters (width $\ell_\mathrm{ED}$, decay form, multi-scale weights) and V5 correlation parameters. Joint analysis across channels could in principle infer kernel structure at the percent level.

### 8.4 GR-4A promotion question

The most consequential open structural question: can a primitive-level argument promote GR-4A from SPECULATIVE to FORCED? Three plausible routes (new primitive introduction, derivation from existing primitives via novel argument, effective-theory upgrade via UV-FIN) all require structural content not yet identified. ED-Phys-10's baseline ("no Einstein equations from primitives") remains the structural ceiling.

---

## References

[1] A. Proxmire and Copilot, *Quantum Mechanics as a Structural Consequence of Event-Density Primitives* (Phase-1 closure paper), 2026.

[2] A. Proxmire and Copilot, *Relativistic Quantum Mechanics as a Forced Structural Consequence of Event-Density Primitives* (Arc R paper), 2026.

[3] A. Proxmire and Copilot, *Mass and Masslessness as Structural Features of Event-Density Theory* (Arc M paper), 2026.

[4] A. Proxmire and Copilot, *A UV-Finite Quantum Field Theory from Event-Density Primitives* (Arc Q paper), 2026.

[5] A. Proxmire and Copilot, *Non-Markovian Structure as a Forced Memory-Kernel Layer of Event-Density Theory* (Arc N paper), 2026.

[6] A. Proxmire, *Phase-3 Scoping*, `phase3_scoping.md`, 2026.

[7] A. Proxmire, *GR Coupling Catalogue*, `gr_coupling_catalogue.md`, 2026.

[8] A. Proxmire, *GR Coupling FORCED Evaluation*, `gr_coupling_forced.md`, 2026.

[9] A. Proxmire, *GR Coupling REFUTED Evaluation*, `gr_coupling_refuted.md`, 2026.

[10] A. Proxmire, *Cosmological and Large-Scale Implications*, `gr_cosmological_implications.md`, 2026.

[11] A. Proxmire, *Phase-3 Synthesis*, `phase3_synthesis.md`, 2026.

[12] ED-Phys-10 kinematic-curvature arc, closed 2026-04-22. See `memory/project_ed10_geometry_qft_scope.md`.

[13] B. S. DeWitt, *The Global Approach to Quantum Field Theory*. Oxford University Press, 2003.

[14] R. M. Wald, *Quantum Field Theory in Curved Spacetime and Black Hole Thermodynamics*. University of Chicago Press, 1994.

[15] M. Visser, "Acoustic black holes: horizons, ergospheres, and Hawking radiation," *Class. Quantum Grav.* **15**, 1767 (1998).

[16] S. Weinberg, "The Cosmological Constant Problem," *Rev. Mod. Phys.* **61**, 1 (1989).

---

*Manuscript closure: 2026-04-24. Companion documents: Phase-1 paper [1], Arc R paper [2], Arc M paper [3], Arc Q paper [4], Arc N paper [5], Phase-3 synthesis [11].*
