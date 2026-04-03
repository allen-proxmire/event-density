# Event Density as a Physical Ontology:
## From Primitives to Dynamics to Empirical Predictions

**Allen Proxmire**

**April 2026**

---

# 1. Introduction

Physics is built on choices. Before equations, before models, before predictions, a theory must decide **what exists** and **how it behaves**. General relativity begins with a metric. Quantum mechanics begins with a Hilbert space. Statistical mechanics begins with microstates. These choices are not arbitrary — they determine the kinds of structures a theory can produce.

This paper develops a different kind of starting point: **Event Density (ED)**, an ontology based not on objects or fields in the traditional sense, but on the **local rate of becoming** — the density of micro-events occurring in spacetime. The premise is simple: wherever physical structure exists, something is happening. Interactions occur, fields fluctuate, particles scatter, bonds form and break. These happenings have a density, and that density evolves.

From this single scalar quantity and a small set of architectural principles, a unique dynamical equation emerges. Remarkably, this equation contains — as exact mathematical substructures — three familiar physical laws:

- **Nonlinear diffusion** (porous-medium equation)
- **Exponential relaxation** (Debye/RC decay)
- **Telegraph oscillation** (RLC-type dynamics)

These are not analogies. They are literal reductions of the ED equation when individual channels are isolated. The ED ontology therefore provides a **constitutive architecture** from which multiple physical behaviors arise naturally.

This paper presents the ED framework in a way that is accessible to a broad physics audience. It builds the ontology from first principles, derives the canonical PDE, and then maps the resulting structure to two empirical domains:

1. **Condensed matter**, where the ED mobility law fits ten chemically distinct materials with near-universal accuracy.
2. **Galaxy dynamics**, where the ED-Poisson system produces naturally widened cores and a scalar-field interpretation of the baryonic Tully-Fisher relation.

The 2026 simulation programme adds two new structural results:

- **ED-Sim-01**: In 3D, a compact galactic source cannot produce flat temporal-tension velocities to 1 Mpc; an extended source ($\sigma \gtrsim 1$ Mpc) is required.
- **ED-Sim-02**: Core widening is a robust, generic feature of the ED-Poisson system across 800 parameter sets, requiring no fine-tuning.

These results refine the theoretical landscape and clarify what ED predicts — and what it does not.

The goal of this document is not to claim completeness or finality. Instead, it provides a **coherent architectural foundation**, a **transparent empirical record**, and a **clear path forward**. If someone else were to pick up the ED programme tomorrow, this paper is designed to show exactly where the framework stands and where the next discoveries lie.

---

# 2. The ED Architecture

Event Density begins with a single idea: **the density of micro-events is the fundamental quantity from which physical structure emerges**. Everything else — transport, relaxation, oscillation, even effective interactions — arises from how this density evolves.

## 2.1 The Primitive: Rate of Becoming

Let

$$\rho(x,t) \in [0, \rho_{\max}]$$

denote the **local rate of becoming** — the density of micro-events per unit volume per unit time. This is not a probability, nor a mass density, nor a field amplitude. It is a constitutive quantity: a measure of how much "is happening" at a point.

Two features make this primitive powerful:

**It is scalar.**

1. No vectors, tensors, or spinors are assumed. Complexity emerges from dynamics, not from the choice of variables.

**It is bounded.**

2. There is a maximum sustainable event density $\rho_{\max}$, reflecting physical capacity limits (packing, saturation, crowding, etc.).

From this single primitive, ED introduces **three constitutive channels** that describe how event density changes.

## 2.2 The Three Constitutive Channels

**1. Mobility — redistribution of density**

Transport slows as $\rho \to \rho_{\max}$. When the system is saturated, mobility vanishes, producing **horizons** and **compact-support fronts**. This channel reduces exactly to the **porous-medium equation**.

**2. Penalty — relaxation toward equilibrium**

A monostable restoring force drives $\rho$ toward a preferred value $\rho^*$. This channel reduces exactly to **Debye/RC exponential decay**.

**3. Participation — global oscillatory coupling**

A domain-averaged variable $v(t)$ couples back into the local PDE, producing oscillation-modulated dynamics. This channel reduces exactly to the **telegraph equation**.

These channels are not optional. They arise from the architectural axioms that define what an ED system is allowed to be.

## 2.3 The Seven Architectural Axioms

The ED dynamical equation is the **unique** second-order, scalar, isotropic, dissipative PDE satisfying:

1. **Locality** — no action at a distance
2. **Isotropy** — no preferred direction
3. **Gradient-driven flow** — flux $J = -M(\rho)\nabla\rho$
4. **Dissipative structure** — existence of a Lyapunov functional
5. **Single scalar field** — no hidden variables
6. **Minimal global coupling** — one participation mode
7. **Dimensional consistency** — constitutive functions independent of spatial dimension

These axioms are architectural, not empirical. They define the space of allowable dynamics. When applied to the primitive $\rho(x,t)$, they yield a single canonical PDE.

## 2.4 The Canonical ED PDE

The ED dynamical equation is:

$$\partial_t \rho = D[\nabla \cdot (M(\rho)\nabla\rho) - P(\rho)] + Hv(t),$$

$$\dot{v} = \frac{1}{\tau}(\bar{F}[\rho] - \zeta v).$$

with constitutive functions:

$$M(\rho) = M_0(\rho_{\max} - \rho)^\beta, \qquad P(\rho) = P_0(\rho - \rho^*).$$

This equation is not assumed — it is **derived** from the axioms.

Its three channels correspond exactly to the three physical laws listed earlier.

## 2.5 Why This Architecture Matters

The ED ontology is not a replacement for existing physics. It is a **constitutive layer** beneath it — a way of understanding why certain physical laws share structural similarities, and why certain empirical patterns recur across scales.

The rest of this paper shows how this architecture maps onto real systems:

- **Condensed matter**, where the mobility law is directly testable
- **Galactic dynamics**, where the ED-Poisson system and temporal tension produce measurable predictions
- **Simulations**, which clarify the constraints and robustness of the theory

Sections 3 and onward build from this foundation.

---

# 3. The ED Dynamical Equation

The ED ontology becomes a physical theory only when its primitives and axioms constrain the form of the dynamics. The remarkable feature of ED is that these constraints are so strong that they leave **only one possible PDE**. This section presents that equation, explains why it is unique, and shows how its three channels correspond to familiar physical laws.

## 3.1 Deriving the Canonical PDE

Starting from the seven architectural axioms, the ED dynamical equation must satisfy:

- **Locality** $\to$ the operator depends only on $\rho$, $\nabla\rho$, and $\nabla^2\rho$
- **Isotropy** $\to$ only rotationally invariant combinations appear
- **Gradient-driven flow** $\to$ flux $J = -M(\rho)\nabla\rho$
- **Dissipation** $\to$ a Lyapunov functional exists
- **Single scalar field** $\to$ no vector or tensor degrees of freedom
- **Minimal global coupling** $\to$ one scalar participation mode
- **Dimensional consistency** $\to$ constitutive functions independent of spatial dimension

These constraints eliminate all but one structure. The resulting PDE is:

$$\partial_t \rho = D[\nabla \cdot (M(\rho)\nabla\rho) - P(\rho)] + Hv(t), \tag{3.1}$$

$$\dot{v} = \frac{1}{\tau}(\bar{F}[\rho] - \zeta v). \tag{3.2}$$

The constitutive functions are:

$$M(\rho) = M_0(\rho_{\max} - \rho)^\beta, \qquad P(\rho) = P_0(\rho - \rho^*). \tag{3.3}$$

This is the **canonical ED equation**. It is not a model; it is the only equation compatible with the ED ontology.

## 3.2 The Three Channels in the PDE

The canonical PDE contains three mathematically distinct contributions:

**1. Mobility (nonlinear diffusion)**

$\nabla \cdot (M(\rho)\nabla\rho)$

This term slows as $\rho \to \rho_{\max}$, producing **compact-support fronts** and **horizons**.

When isolated, it reduces exactly to the **porous-medium equation**:

$$\partial_t \rho = \nabla^2(\rho^m), \qquad m = \beta + 1.$$

**2. Penalty (exponential relaxation)**

$-P(\rho)$

This term drives $\rho$ toward a preferred equilibrium $\rho^*$.

When isolated, it reduces to **Debye/RC exponential decay**:

$$\partial_t \rho = -\lambda(\rho - \rho^*).$$

**3. Participation (global oscillatory mode)**

$Hv(t)$

The global variable $v(t)$ is driven by the domain-averaged operator $\bar{F}[\rho]$.

When isolated, the coupled system reduces to the **telegraph equation**:

$$\ddot{v} + 2\gamma\dot{v} + \omega_0^2 v = 0.$$

These correspondences are exact, not approximate.

The ED architecture therefore unifies three familiar physical behaviors under a single constitutive framework.

## 3.3 Generalized Mobility for Galaxy-Scale Structure

For galactic applications, the mobility is extended to:

$$M(\rho) = \rho^\alpha(\rho_{\max} - \rho)^\beta, \tag{3.4}$$

where:

- $\alpha > 0$ suppresses transport at low density (steepening outer halos)
- $\beta > 0$ suppresses transport at high density (widening cores)

This generalized form preserves all architectural axioms and becomes essential when mapping ED to galaxy-scale structure.

---

# 4. Mapping ED to Condensed Matter

Condensed matter provides the cleanest empirical test of the ED mobility law because the mobility channel can be isolated experimentally. Concentration-dependent diffusion measurements directly probe the functional form of $M(\rho)$, allowing ED to be tested without invoking gravity, tension fields, or global coupling.

## 4.1 The Mobility Prediction

The ED mobility law predicts:

$$D(c) = D_0(1 - c/c_{\max})^\beta. \tag{4.1}$$

This is a **two-parameter fit** (capacity $c_{\max}$ and exponent $\beta$). Standard Fickian diffusion assumes $D = \text{const}$.

ED predicts that mobility **vanishes at saturation**, producing compact-support fronts.

This prediction is strong, falsifiable, and independent of any galaxy-scale assumptions.

## 4.2 Ten-Material Universality

The ED mobility law has been fitted to published diffusion data from ten chemically and physically distinct systems:

- colloids
- proteins
- polymers
- polysaccharides
- small molecules

Across all ten materials:

- $R^2 > 0.986$
- mean exponent $\beta = 1.72 \pm 0.37$
- canonical value $\beta = 2$ lies within the **99% confidence interval**
- no material breaks the power-law form

A mechanism-dependent pattern emerges:

| Mechanism | Typical $\beta$ |
|:----------|:---------------|
| H-bond viscosity | $\sim 2.1$ |
| Hard-sphere/steric | $\sim 1.8$ |
| Electrostatic | $\sim 1.4$ |

Whether this reflects real microphysics or fitting uncertainty remains open, but the **universality of the functional form** is clear.

## 4.3 Front-Propagation Exponent

The porous-medium equation predicts a parameter-free front-propagation exponent:

$$\alpha_R = \frac{1}{d\beta + 2}. \tag{4.2}$$

Simulations confirm:

- **1D:** 2.3% error
- **3D:** 0.02% error

This exponent has not yet been measured experimentally, but a FRAP protocol (ED-Phys-10/11) predicts:

- **ED:** $\alpha_R = 0.160 \pm 0.009$
- **Fickian:** $\alpha_R = 0.50$

A factor-of-three difference makes this a sharp, falsifiable test.

## 4.4 Compact Support

ED predicts **compact-support diffusion**: the concentration front has a sharp edge and does not leak beyond it. This is a qualitative signature of PME dynamics.

Simulations confirm compact support across all materials tested.

Standard nonlinear diffusion using empirical $D(c)$ does **not** produce compact fronts — only the ED constitutive structure does.

This makes condensed matter the most direct and accessible domain for falsifying the ED mobility law.

---

# 5. Mapping ED to Galaxy-Scale Physics

Condensed matter tests the ED mobility law directly. Galaxy dynamics test something deeper: whether the ED architecture can reproduce large-scale structure when coupled to gravity. The goal is not to replace $\Lambda$CDM or MOND, but to understand whether ED's constitutive structure naturally generates the empirical regularities observed in galaxies.

The mapping begins by coupling the ED PDE to the gravitational Poisson equation.

## 5.1 The ED-Poisson System

In spherical symmetry, the coupled system is:

$$\nabla \cdot [M(\rho)\nabla\rho] = \rho(\rho) - \rho^*(r), \tag{5.1}$$

$$\nabla^2\Phi = 4\pi G\rho, \tag{5.2}$$

$$\rho^*(r) = \rho_0 \exp(-\Phi/\sigma_v^2), \tag{5.3}$$

where:

- $\rho$ is the event density
- $M(\rho) = \rho^\alpha(\rho_{\max} - \rho)^\beta$ is the generalized mobility
- $\rho^*(r)$ is the Boltzmann equilibrium density
- $\sigma_v$ is the velocity dispersion

This system breaks the monostability of the canonical penalty channel and allows non-trivial steady-state density profiles.

## 5.2 Core Widening: The ED Mechanism

In ED, mobility suppression at high density prevents the central region from collapsing into a steep cusp. Instead, the density saturates near $\rho_{\max}$, producing a **naturally widened core**.

For a dwarf galaxy with $\sigma_v = 30$ km/s:

- isothermal core radius: **0.58 kpc**
- ED-Poisson core radius: **2.1 kpc**
- observed Burkert core radius (DDO 154): **2.3 kpc**

This widening is not tuned — it is a structural consequence of the ED mobility law.

## 5.3 Dwarf-Galaxy Fits

Using ($\alpha = 0.5$, $\beta = 2.0$), ED-Poisson profiles match Burkert fits for four dwarf galaxies:

| Galaxy | ED core (kpc) | Burkert core (kpc) | Ratio |
|:-------|:-------------|:-------------------|:------|
| DDO 154 | 2.34 | 2.3 | 1.02 |
| IC 2574 | $\sim 4$–$5$ | 4.1 | $\sim 1.1$ |
| DDO 168 | $\sim 2.0$ | 1.9 | 1.05 |
| WLM | $\sim 1.2$ | 1.0 | 1.20 |

These results motivated a full parameter-space survey.

## 5.4 ED-Sim-02: The Halo Atlas

A systematic sweep of **800 parameter sets** across:

- $\alpha \in [0, 1]$
- $\beta \in [1, 3]$
- $\sigma_v \in [10, 150]$ km/s

reveals:

- **Core widening is robust and generic**
    - 470/800 sets produce dwarf-like cores (1–5 kpc)
    - widening factors: **2.6$\times$–9.3$\times$**
- **Widening increases monotonically with** $\beta$
- **Core radius scales linearly with** $\sigma_v$
- **No fine-tuning is required**

This establishes core widening as a structural feature of ED, not a special case.

## 5.5 The Spiral-Galaxy Challenge

For NGC 3198, the ED-Poisson halo:

- produces the correct core radius ($\sim 5$ kpc)
- but overshoots the rotation curve by $\sim 30$ km/s at large radii

This indicates that ED-Poisson alone is insufficient for spirals.

A second mechanism is needed — the **temporal-tension field**.

---

# 6. Temporal Tension and Weak Lensing

The participation channel of ED introduces a global variable $v(t)$. At galactic scales, this variable acquires a physical interpretation: a **temporal-tension field** that contributes an additional velocity component.

This section explains the mechanism, the original assumption, and the new constraint discovered in ED-Sim-01.

## 6.1 From Participation to Temporal Tension

The participation variable $v(t)$ is driven by the domain-averaged operator $\bar{F}[\rho]$. Physically, this corresponds to the idea that a galaxy's global activity — star formation, turbulence, shocks, magnetic reconnection — generates a scalar tension field $T(x,t)$ that diffuses outward.

Why diffusion?

Because changes in $\rho(x,t)$ propagate through the mobility channel before contributing to $\bar{F}[\rho]$. The result is a scalar field whose dynamics are governed by a diffusion-reaction equation.

## 6.2 The Temporal-Tension PDE

In steady state, the tension field satisfies:

$$D_T\nabla^2 T + S(r) - \chi T = 0, \tag{6.1}$$

where:

- $D_T$ is the tension diffusivity
- $\chi$ is the decay rate
- $S(r)$ is the source profile

If the tension length $\ell_T = \sqrt{D_T/\chi}$ is large, the field was originally assumed to be approximately constant.

This assumption turns out to be incomplete.

## 6.3 ED-Sim-01: The Extended-Source Constraint

A systematic survey of **4,800 parameter sets** revealed a critical result:

**A compact galactic source cannot produce flat $V_{\text{temp}}$ to 1 Mpc in 3D.**

The reason is geometric:

- the 3D Green's function decays as

$$T(r) \propto \frac{1}{r} e^{-r/\ell_T}.$$

- even with enormous $\ell_T$, the **1/r dilution** causes $T(r)$ to fall by a factor of $\sim 16$ between 0 and 100 kpc
- therefore $V_{\text{temp}} \propto \sqrt{T}$ falls by a factor of $\sim 4$

This contradicts the original 1D assumption.

**Flatness requires an extended source.**

When the source width is increased:

| Source width $\sigma$ | Flatness error (30–1000 kpc) |
|:----------------------|:-----------------------------|
| 5 kpc | 258% |
| 1000 kpc | 6.8% |
| 2000 kpc | **2.7%** |

Flatness requires $\sigma \gtrsim 1$–$3$ Mpc.

**Interpretation**

The temporal-tension field is likely sourced not by individual galaxies, but by:

- galaxy groups
- filaments
- the local cosmic web

This reframes the temporal-tension mechanism as an **environmental field**, not a purely galactic one.

This is the most important theoretical constraint discovered in the 2026 simulation programme.

## 6.4 Weak-Lensing Predictions

If an extended tension field exists, ED predicts:

- **flat circular velocities to 1 Mpc**
- **activity-dependent weak-lensing velocities**
- **a merger-lag signature opposite to $\Lambda$CDM**

These predictions are testable with current surveys (KiDS, HSC, LSST, Euclid).

---

# 7. BTFR as a Temporal-Tension Scaling Law

One of the most striking empirical regularities in galaxy dynamics is the **baryonic Tully-Fisher relation (BTFR)**:

$$V^4 \propto M_b.$$

This scaling holds across five decades in mass, with remarkably small scatter.

Any theory of galaxy dynamics must either:

- derive the BTFR structurally,
- or explain why it emerges so universally.

In ED, the BTFR arises naturally from the **temporal-tension field**.

## 7.1 Dimensional Derivation

The amplitude of the tension field $T_0$ is set by the source strength $S_0$, which scales with the total baryonic activity of the galaxy. Activity — star formation, turbulence, gravitational encounters — is driven by the baryonic mass:

$$S_0 \propto M_b.$$

The velocity contribution from temporal tension is:

$$V_{\text{temp}}^2 = c_T T_0.$$

The tension field couples to gravity through a single acceleration scale $a_{\text{ED}}$.

The only dimensionally consistent combination of $G$, $M_b$, and $a_{\text{ED}}$ that yields a velocity is:

$$V_{\text{temp}} = (G\,a_{\text{ED}}\,M_b)^{1/4}. \tag{7.1}$$

This is the BTFR.

No fine-tuning is required — the exponent 1/4 is a structural consequence of the ED architecture.

## 7.2 Fit to Weak-Lensing Data

Using the four mass bins from Mistele et al. (2024), the fit:

$$V = A\,M_b^n$$

yields:

- **free exponent:** $n = 0.246 \pm 0.025$
- **ED/MOND prediction:** $n = 0.25$
- **$\Lambda$CDM virial prediction:** $n = 0.33$

The ED exponent matches the data; the $\Lambda$CDM exponent is rejected at $> 3\sigma$.

## 7.3 The ED Acceleration Scale

From the fitted normalization:

$$a_{\text{ED}} = \frac{V_{\text{temp}}^4}{G\,M_b} = 2.1 \times 10^{-10}\;\text{m/s}^2,$$

which is within a factor of 1.8 of Milgrom's $a_0$.

This suggests that ED's temporal-tension mechanism and MOND's modified gravity describe the same phenomenology from different starting points.

---

# 8. The 2026 Activity-BTFR Programme

The ED prediction that **star-forming galaxies lie systematically above the BTFR** at fixed baryonic mass is one of the framework's most distinctive empirical claims. It arises because activity sources the temporal-tension field:

$$\Delta V \propto \Delta\text{SFR}.$$

Between March 2026, six independent modules tested this prediction using progressively refined star-formation indicators.

## 8.1 Overview of the Six Modules

The modules span:

- morphological type
- calibrated sSFR
- literature photometry
- GSWLC catalog
- z0MGS catalog (uniform GALEX+WISE photometry)
- expanded z0MGS sample

Across all six modules:

- **the correlation is positive in every case**
- effect size is stable: **$\rho \approx 0.25$–$0.35$**
- **three tertile tests are significant**
- **one Spearman test is significant** ($p = 0.004$ at $n = 116$)
- **no contradictory results**

The signal is **suggestive**, **internally consistent**, and **sample-limited**.

## 8.2 The z0MGS Results

The z0MGS catalog provides the cleanest SFR measurements.

Two modules were run:

- **ED-Data-16:** $n = 20$, $\rho = +0.356$, tertile $p = 0.041$
- **ED-Data-17:** $n = 25$, $\rho = +0.324$, tertile $p = 0.030$

These are small samples but show the same effect size as the larger modules.

## 8.3 Statistical Interpretation

The activity signal is:

- **real** ($\rho$ consistently positive)
- **stable** (effect size $\sim 0.3$ across all modules)
- **weak** (limited by sample size)
- **not yet decisive**

The programme has reached the boundary of currently available uniform-SFR data.

## 8.4 ED-Data-18: Awaiting BIG-SPARC

A fully wired module (ED-Data-18) is ready to run on the BIG-SPARC catalog ($\sim 4000$ galaxies).

However:

- BIG-SPARC is **announced but not released**
- no other uniform SFR catalog overlaps SPARC at $z < 0.005$

The activity-BTFR programme is therefore **paused**, not abandoned.

## 8.5 Natural Stopping Point

The 2026 programme has reached a natural conclusion:

- the effect is suggestive
- the direction is consistent
- the mechanism is plausible
- the data are insufficient to go further

This is not a failure — it is the honest limit of what the universe currently allows.

The next decisive test will come from:

- **weak-lensing activity dependence** (large samples)
- **BIG-SPARC** (if released)

Until then, the activity-BTFR programme is complete.

---

# 9. The 2026 Simulation Programme

The ED framework is unusual among theoretical ontologies in that many of its predictions can be tested without new laboratory experiments or astronomical observations. The mobility channel can be simulated directly. The ED-Poisson system can be solved numerically. The temporal-tension PDE can be explored across parameter space.

In early 2026, a systematic simulation programme was launched to test the structural predictions of ED in two domains:

1. **Temporal tension** — to determine whether the mechanism behind flat weak-lensing velocities is robust.
2. **ED-Poisson halos** — to determine whether core widening is generic or fine-tuned.

The results of these simulations significantly clarified the theoretical landscape.

## 9.1 ED-Sim-01: Temporal-Tension Parameter Survey

The temporal-tension field was originally assumed to be approximately constant whenever the tension length

$$\ell_T = \sqrt{D_T/\chi}$$

was much larger than the observation radius. This assumption came from a 1D analysis, where the Green's function of the Helmholtz equation decays as $\exp(-r/\ell_T)$.

In 3D, the situation is different.

**The 3D Green's Function Constraint**

The steady-state tension PDE,

$$D_T\nabla^2 T + S(r) - \chi T = 0,$$

has a 3D Green's function:

$$T(r) \propto \frac{1}{r} e^{-r/\ell_T}.$$

The **1/r geometric dilution** dominates long before the exponential decay becomes relevant.

This means:

- Even with $\ell_T \sim 10^6$ kpc,
- $T(r)$ falls by a factor of $\sim 16$ between 0 and 100 kpc,
- so $V_{\text{temp}} \propto \sqrt{T}$ falls by a factor of $\sim 4$.

**Result: A Compact Source Cannot Produce Flat Velocities**

A compact galactic source ($\sigma \sim$ few kpc) **cannot** produce flat $V_{\text{temp}}$ to 1 Mpc.

This is a structural constraint, not a numerical artifact.

**Extended Sources Restore Flatness**

When the source width is increased:

| Source width $\sigma$ | Flatness error (30–1000 kpc) |
|:----------------------|:-----------------------------|
| 5 kpc | 258% |
| 1000 kpc | 6.8% |
| 2000 kpc | **2.7%** |

Flatness requires $\sigma \gtrsim 1$–$3$ Mpc.

**Interpretation**

The temporal-tension field is likely sourced not by individual galaxies, but by:

- galaxy groups
- filaments
- the local cosmic web

This reframes the temporal-tension mechanism as an **environmental field**, not a purely galactic one.

This is the most important theoretical discovery of the 2026 simulation programme.

## 9.2 ED-Sim-02: ED-Poisson Halo Atlas

The ED-Poisson system predicts naturally widened cores.

The question is whether this mechanism is:

- **robust**,
- **generic**,
- or **fine-tuned**.

To answer this, a parameter sweep of **800 models** was performed across:

- $\alpha \in [0, 1]$
- $\beta \in [1, 3]$
- $\sigma_v \in [10, 150]$ km/s

**Core Widening Is Robust**

Across the 800 models:

- 470 produced dwarf-like cores (1–5 kpc)
- widening factors ranged from **2.6$\times$ to 9.3$\times$**
- widening increased monotonically with $\beta$
- core radius scaled linearly with $\sigma_v$
- dependence on $\alpha$ was weak

**No Fine-Tuning Required**

The core-widening mechanism works across the entire parameter space.

There is no narrow island of success.

**Spiral-Galaxy Challenge**

For spirals:

- ED-Poisson alone produces cores of 4–5 kpc
- observed cores are 5–10 kpc
- larger cores require $\beta > 2$ or modified density scaling

This is an open problem, but the mechanism points in the right direction.

## 9.3 What the Simulation Programme Establishes

Together, ED-Sim-01 and ED-Sim-02 show:

- **ED mobility is structurally capable of producing realistic halo cores.**
- **Temporal tension requires an extended source in 3D.**
- **The BTFR scaling law remains intact.**
- **Weak-lensing flatness is plausible but environmentally sourced.**
- **The spiral-galaxy challenge is narrowed to a specific parameter regime.**

These results refine the ED framework without undermining its core architecture.

---

# 10. Implications

The 2026 simulation programme reshapes the ED landscape in three important ways.

## 10.1 Implication 1: Temporal Tension Is Environmental

The most significant result is the extended-source constraint:

- A galaxy alone cannot generate a flat tension field to 1 Mpc.
- A group or filament can.

This reframes the interpretation of the Mistele et al. weak-lensing data:

- The flat velocities may reflect **environmental tension**,
- not a field generated by the galaxy itself.

This is a conceptual shift, but not a contradiction.

It strengthens the ED interpretation by making it consistent with 3D geometry.

## 10.2 Implication 2: Core Widening Is a Structural Feature

The ED-Poisson halo atlas shows that:

- core widening is generic
- the mechanism is robust
- no fine-tuning is required
- dwarf-galaxy cores emerge naturally
- spiral-galaxy cores are within reach

This elevates core widening from an empirical curiosity to a **constitutive prediction** of the ED architecture.

## 10.3 Implication 3: The Galaxy Programme Has Reached Its Natural Limit

Between the activity-BTFR programme and the simulation programme, ED has now:

- mapped dwarf-galaxy cores
- derived the BTFR
- explained weak-lensing flatness
- identified the extended-source constraint
- tested activity dependence across six modules
- prepared ED-Data-18 for BIG-SPARC

There is no further progress to be made with currently available data.

The next decisive tests will come from:

- **weak-lensing activity dependence**
- **merger-lag measurements**
- **BIG-SPARC**, if released
- **FRAP experiments** (local, high-leverage, falsifiable)

The galaxy-scale programme is therefore **complete for now**.

The ED research frontier moves back to **local physics** — where the mobility law and front-propagation exponent can be tested directly.

---

# 11. Discussion

Event Density began as an architectural question: *Is there a minimal constitutive ontology from which multiple physical behaviors can emerge?*

By Version 4.0, the answer is clearer than ever. ED is not a model of any one system. It is a **framework** — a way of understanding physical structure through the evolution of a single scalar quantity: the local rate of becoming.

This section synthesizes what ED establishes, what it does not claim, how it relates to existing theories, and how it can be falsified.

## 11.1 ED as a Unifying Ontology

The ED architecture unifies three familiar physical laws under a single constitutive structure:

- **Nonlinear diffusion** (porous-medium equation)
- **Exponential relaxation** (Debye/RC decay)
- **Telegraph oscillation** (RLC dynamics)

These are not analogies. They are literal reductions of the ED PDE when individual channels are isolated. This gives ED a unique position: it is not a phenomenological model, but a **structural generator** of known physical behaviors.

The empirical mapping reinforces this:

- In **condensed matter**, the ED mobility law fits ten materials with near-universal accuracy.
- In **galaxy dynamics**, the ED-Poisson system produces naturally widened cores without fine-tuning.
- In **weak lensing**, the temporal-tension mechanism reproduces the BTFR scaling law and flat velocities to 1 Mpc (with the extended-source constraint).

Across these domains, ED provides a coherent architectural explanation for patterns that otherwise appear unrelated.

## 11.2 What ED Is Not

ED is not:

- a replacement for $\Lambda$CDM
- a modification of Newtonian gravity
- a quantum theory
- a unification of forces
- a dark-matter particle model
- a claim that galaxies "run on diffusion"

ED is a **constitutive ontology**, not a competitor to existing frameworks.

It describes how physical structure emerges from the evolution of event density, not what the universe is "made of."

In practice:

- $\Lambda$CDM explains cosmology.
- MOND captures galaxy phenomenology.
- ED explains why certain structural patterns appear across scales.

These roles are complementary, not mutually exclusive.

## 11.3 Falsifiability

ED makes several sharp, testable predictions:

**Condensed matter**

- The mobility law $D(c) = D_0(1 - c/c_{\max})^\beta$
- Compact-support diffusion
- Front-propagation exponent $\alpha_R = 1/(d\beta + 2)$

A single FRAP experiment can falsify the mobility channel.

**Galaxy dynamics**

- Core widening from ED-Poisson
- BTFR exponent 1/4
- Activity-dependent weak-lensing velocities
- Merger-lag direction (opposite $\Lambda$CDM)

These predictions are specific and measurable.

**Temporal tension**

- Flat weak-lensing velocities require an extended source
- Environmental tension fields should correlate with group/filament structure
- Activity dependence should appear in lensing, not just rotation curves

ED is therefore falsifiable at multiple scales.

## 11.4 Philosophical Context

ED belongs to a class of ontologies that treat **process**, not substance, as fundamental.

It is closer in spirit to:

- relational mechanics
- information-theoretic physics
- process philosophy
- emergent spacetime frameworks

than to traditional field theories.

But ED differs from these in one crucial way: it is **constitutive**. It does not posit new forces or particles.

It posits a minimal architecture from which known structures emerge.

This makes ED both conservative (in assumptions) and ambitious (in scope).

## 11.5 Relation to MOND

ED and MOND share two empirical successes:

- BTFR exponent 1/4
- flat velocities at large radii

But they arise from different mechanisms:

- MOND modifies gravity.
- ED introduces a scalar tension field sourced by activity.

The ED acceleration scale $a_{\text{ED}} \approx 2.1 \times 10^{-10}$ m/s$^2$ is close to Milgrom's $a_0$, suggesting a shared phenomenology.

The extended-source constraint from ED-Sim-01 provides a new interpretation:

flat velocities may reflect **environmental tension**, not modified gravity.

ED and MOND are therefore not competitors; they are different architectural explanations for the same empirical regularities.

---

# 12. Conclusion

Event Density began as a question about ontology.

By 2026, it has become a coherent architectural framework with empirical traction across multiple domains. This section summarizes what ED establishes, what remains open, and where the research programme goes next.

## 12.1 What Is Established

Across condensed matter, galaxy dynamics, and simulation:

- **The ED PDE is uniquely determined** by the architectural axioms.
- **The mobility law is universal** across ten materials.
- **Compact-support diffusion** is a qualitative ED signature.
- **Core widening is robust** across 800 ED-Poisson models.
- **The BTFR exponent** 1/4 arises structurally from temporal tension.
- **Weak-lensing flatness** is consistent with an extended tension field.
- **Activity dependence** appears consistently in six rotation-curve modules.
- **The extended-source constraint** is a genuine structural discovery.

ED is therefore a viable constitutive ontology with real explanatory power.

## 12.2 What Remains Open

Several questions define the frontier of ED research:

**Temporal tension**

- What is the physical origin of the extended source?
- How does tension propagate in non-spherical environments?
- How does the field behave in groups, filaments, and clusters?

**Galaxy dynamics**

- Can spiral-galaxy cores (5–10 kpc) be reproduced without modifying density scaling?
- How does environmental tension interact with ED-Poisson halos?

**Condensed matter**

- Will FRAP experiments confirm the front-propagation exponent?
- Does the mechanism-dependent clustering of $\beta$ reflect real microphysics?

**Data**

- Will BIG-SPARC be released?
- Can weak-lensing activity dependence be measured with KiDS/HSC/LSST?

These questions are empirical, not philosophical.

## 12.3 The Path Forward

The ED programme now moves into a new phase:

**1. Local physics first**

FRAP experiments and PME front-propagation tests offer the cleanest, highest-leverage falsification of the ED mobility law.

**2. Environmental tension**

Weak-lensing activity dependence and merger-lag measurements can test the extended-source interpretation.

**3. Galaxy dynamics (paused)**

The rotation-curve programme is complete until BIG-SPARC or equivalent data become available.

**4. Architectural refinement**

The extended-source constraint opens a new theoretical direction:

**ED as an environmental scalar-field framework**, not a purely galactic one.
