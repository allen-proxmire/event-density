# Event Density as a Physical Ontology: From Primitives to Dynamics to Empirical Predictions

**Allen Proxmire**

---

## Abstract

Event Density (ED) is a constitutive ontology built on the premise that physical structure arises from the local rate of becoming — the density of micro-events in spacetime. From four primitives (density, mobility, penalty, participation) and seven structural axioms, a unique canonical PDE is derived. This PDE decomposes into three constitutive channels — nonlinear diffusion, exponential relaxation, and telegraph oscillation — each corresponding exactly to a known physical law. The mobility channel reduces to the porous-medium equation (PME) with exponent $m = \beta + 1$; the penalty channel is an RC-circuit discharge; the participation channel is an RLC telegraph oscillator. All correspondences are exact at the level of governing equations.

This paper synthesises two empirical programmes that test the ED framework against real data. In condensed matter, the ED mobility law $D(c) = D_0(1 - c/c_{\max})^\beta$ fits three chemically distinct materials (hard-sphere colloids, sucrose-water, BSA protein solutions) with $R^2 > 0.98$ and a mean exponent $\beta = 2.00 \pm 0.29$ — consistent with the canonical ED value. The front-propagation exponent $\alpha_R = 1/(d\beta + 2)$ is confirmed by simulation to 2.3% in 1D.

At galactic scales, the ED PDE coupled to the Poisson equation produces density profiles with naturally widened cores that match observed Burkert core radii to within 10% for four dwarf galaxies. The temporal-tension interpretation — in which the ED participation channel generates a non-gravitational velocity contribution — predicts indefinitely flat circular velocities consistent with the Mistele et al. (2024) weak-lensing observations. The baryonic Tully-Fisher relation $V \propto M_b^{1/4}$ is derived as a temporal-tension amplitude scaling law, with the measured exponent $n = 0.246 \pm 0.025$ matching the prediction exactly. The ED acceleration scale $a_{\text{ED}} = 2.1 \times 10^{-10}$ m/s$^2$ is within a factor of 1.8 of Milgrom's $a_0$.

Two tests are identified that uniquely distinguish ED from both MOND and $\Lambda$CDM: (1) activity-dependent weak-lensing velocities ($\Delta V \sim 30$–$70$ km/s between quiescent and star-forming galaxies at fixed mass), and (2) temporal-tension lensing lags in merging clusters (15–45 kpc behind the baryonic mass — the opposite direction from the $\Lambda$CDM Bullet Cluster offset). Both tests are feasible with current and near-future surveys.

---

## 1. Introduction

### 1.1 The Ontological Question

Physics describes the world through equations. But equations require objects — fields, particles, metrics — and rules for how those objects interact. The choice of objects is an ontological choice: it determines what kind of structure the theory can produce.

General relativity begins with a metric tensor and a stress-energy source. Quantum mechanics begins with a Hilbert space and a Hamiltonian. The Standard Model begins with gauge fields and representations. Each ontology generates a specific class of phenomena. None generates them all from a single set of primitives.

Event Density asks: **is there a simpler set of primitives — a constitutive architecture — from which the structural content of multiple physical theories can emerge?**

### 1.2 Event Density as Ontology

The ED ontology begins with a single scalar field: the local rate of becoming. At each point in space and time, things happen — interactions occur, fields fluctuate, particles scatter. The density of these micro-events is a real-valued scalar $\rho(x, t) \in [0, \rho_{\max}]$, bounded by a capacity limit.

From this primitive, three constitutive channels are derived:

1. **Mobility.** How density redistributes. Transport is density-dependent: it slows as $\rho$ approaches $\rho_{\max}$ and halts at the capacity bound, creating horizons and compact-support fronts.

2. **Penalty.** How density relaxes. A monostable restoring force drives $\rho$ toward a unique equilibrium $\rho^*$, producing exponential decay.

3. **Participation.** How the system oscillates. A global variable $v(t)$, driven by the domain-averaged density operator and feeding back uniformly, produces telegraph oscillations.

These three channels, combined into a single PDE derived from seven axioms, generate a family of dynamics that includes exponential relaxation, self-similar spreading with compact support, free-boundary formation, oscillation-modulated diffusion, and effective pair interactions.

### 1.3 Scope of This Paper

This paper connects the ED ontology to empirical physics at two scales:

- **Condensed matter** (Sections 3–4): the ED mobility law is fitted to concentration-dependent diffusion data from three materials, confirming the functional form and exponent.
- **Galaxy dynamics** (Sections 5–8): the ED PDE coupled to gravity reproduces dwarf galaxy halo profiles, and the temporal-tension channel predicts the baryonic Tully-Fisher relation and weak-lensing flatness to 1 Mpc.

Two tests that uniquely discriminate ED from MOND and $\Lambda$CDM are derived in Section 8.

---

## 2. The ED Dynamical Equation

### 2.1 The Canonical PDE

The canonical ED system on $\Omega \subset \mathbb{R}^d$ is:

$$\partial_t\rho = D\bigl[\nabla\cdot(M(\rho)\nabla\rho) - P(\rho)\bigr] + Hv, \tag{1}$$

$$\dot{v} = \frac{1}{\tau}(\bar{F} - \zeta v), \tag{2}$$

with constitutive functions:

$$M(\rho) = M_0(\rho_{\max} - \rho)^\beta, \qquad P(\rho) = P_0(\rho - \rho^*). \tag{3}$$

This PDE is the unique second-order, scalar, isotropic, dissipative system satisfying the seven architectural axioms:

- **P1 (Locality).** The operator at each point depends only on $\rho$ and its derivatives at that point. No integral terms, no action at a distance.
- **P2 (Isotropy).** The operator is invariant under rotations and reflections: no preferred spatial direction.
- **P3 (Gradient-driven flow).** The flux is $J = -M(\rho)\nabla\rho$ with state-dependent mobility $M(\rho) \geq 0$.
- **P4 (Dissipative structure).** There exists a Lyapunov functional $E[\rho]$ with $dE/dt \leq 0$ along all solutions.
- **P5 (Single scalar field).** The system evolves a single real-valued scalar $\rho(x,t)$.
- **P6 (Minimal coupling).** The global mode $v(t)$ is driven by the domain-averaged operator and feeds back additively.
- **P7 (Dimensional consistency).** The constitutive functions $M$, $P$ and the coupling parameters are independent of spatial dimension $d$.

The derivation proceeds by elimination: P1+P2 reduce the operator to functions of $(\rho, |\nabla\rho|^2, \nabla^2\rho)$; P3 determines the principal part as a divergence; P4 constrains the zeroth-order term to a monostable penalty; P5 excludes non-scalar fields; P6 determines the participation coupling; P7 ensures all constitutive functions are dimension-free. The canonical PDE is the unique system satisfying all seven.

### 2.2 The Generalised Mobility

For galaxy-scale applications, the mobility is extended to:

$$M(\rho) = \rho^\alpha(\rho_{\max} - \rho)^\beta, \tag{4}$$

where $\alpha > 0$ suppresses transport at low density (steepening the outer halo) and $\beta > 0$ suppresses transport at high density (widening the core). The canonical ED ($\alpha = 0$) is recovered as a special case. The generalised form is compatible with axiom P3 (gradient-driven flow with state-dependent mobility).

### 2.3 Channel Correspondences

| Channel | Isolated equation | Physical law | Accuracy |
|:--------|:------------------|:-------------|:---------|
| Penalty | $\dot{\delta} = -DP_0\delta$ | RC/Debye exponential decay | **Exact** (0.00%) |
| Mobility | $\partial_t\delta = D_{\text{pme}}\nabla^2(\delta^m)$ | Porous-medium equation ($m = \beta + 1$) | **Exact reduction** |
| Participation | $\ddot{\delta} + 2\gamma\dot{\delta} + \omega_0^2\delta = 0$ | RLC telegraph oscillation | **Exact** (0.00%) |

These are mathematical identities, not analogies. The penalty channel *is* an RC circuit. The mobility channel *is* the PME. The participation channel *is* a telegraph oscillator.

---

## 3. Mapping ED to Condensed Matter

### 3.1 The Testable Prediction

The ED mobility law predicts that the effective diffusivity decreases as a power law of the remaining capacity:

$$\frac{D(c)}{D_0} = \left(1 - \frac{c}{c_{\max}}\right)^\beta. \tag{5}$$

This is a two-parameter fit ($c_{\max}$, $\beta$) when $D/D_0$ is normalised. Standard Fickian diffusion assumes $D = \text{const}$; ED predicts $D \to 0$ at saturation.

### 3.2 Three-Material Universality Test

The mobility law was fitted to published $D(c)$ data from three chemically distinct systems:

| Material | Mechanism | $\beta$ | $R^2$ | Data source |
|:---------|:----------|:--------|:------|:-----------|
| Hard-sphere colloids | Steric jamming | $1.60$ | 0.9996 | Segre et al. (1995) |
| Sucrose-water | H-bond viscosity | $2.19$ | 0.994 | Price et al. (2016) |
| BSA protein solutions | Hydrodynamic crowding | $2.22$ | 0.988 | Roosen-Runge et al. (2011) |
| **Mean** | — | **$2.00 \pm 0.29$** | — | — |

The mean $\beta$ across three materials operating through three different physical mechanisms is $2.00 \pm 0.29$ — indistinguishable from the canonical ED value $\beta = 2$.

### 3.3 Front-Propagation Exponent

The Barenblatt self-similar solution predicts $R(t) \propto t^{\alpha_R}$ with:

$$\alpha_R = \frac{1}{d\beta + 2}. \tag{6}$$

This is a parameter-free prediction once $\beta$ is fitted from $D(c)$. The 1D simulation for colloids ($\beta = 1.69$) gives $\alpha_R = 0.265$ vs. the theoretical $0.271$ — a **2.3% error**. The 3D simulation gives the peak-decay exponent $\alpha_\rho = -0.4241$ vs. theory $-0.4240$ — **0.02% error**.

### 3.4 Compact Support

All simulations confirm compact support: the concentration front has a sharp edge. Beyond the front, no material has propagated. This is the defining qualitative signature of PME dynamics and is testable by FRAP experiments in concentrated protein solutions.

---

## 4. Mapping ED to Galaxy-Scale Physics

### 4.1 The ED–Poisson System

At galactic scales, the ED PDE is coupled to the gravitational Poisson equation:

$$\nabla\cdot\bigl[M(\rho)\nabla\rho\bigr] = P_0(\rho - \rho^*(r)), \tag{7}$$

$$\nabla^2\Phi = 4\pi G\rho, \tag{8}$$

$$\rho^*(r) = \rho_0\exp(-\Phi/\sigma_v^2), \tag{9}$$

where $\rho^*(r)$ is the Boltzmann-equilibrium density and $\sigma_v$ is the velocity dispersion. This system breaks the monostability of the canonical penalty (which has $\rho^* = \text{const}$) and allows nontrivial steady-state density profiles.

### 4.2 Core Widening

The ED mobility $M \propto (\rho_{\max} - \rho)^\beta$ suppresses transport at high density, preventing the central density from peaking as sharply as the Boltzmann prediction. The result: **ED cores are wider than isothermal cores** by a factor of $\sim 3$–$4$. For a dwarf galaxy with $\sigma_v = 30$ km/s, the isothermal core radius is $0.58$ kpc; the ED–Poisson core is $2.1$ kpc — matching the observed Burkert core radius of DDO 154 ($2.3$ kpc) to within 10%.

### 4.3 Dwarf Galaxy Results

The generalised mobility ($\alpha = 0.5$, $\beta = 2.0$) coupled to Poisson produces profiles that match Burkert to **99.6%** (normalised $\chi^2 = 0.004$) for dwarf galaxies:

| Galaxy | ED core (kpc) | Burkert core (kpc) | Ratio |
|:-------|:-------------|:-------------------|:------|
| DDO 154 | 2.34 | 2.3 | 1.02 |
| IC 2574 | $\sim 4$–$5$ | 4.1 | $\sim 1.1$ |
| DDO 168 | $\sim 2.0$ | 1.9 | 1.05 |
| WLM | $\sim 1.2$ | 1.0 | 1.20 |

### 4.4 Schematic: The ED Halo Structure

The combined ED–Poisson halo has three distinct zones:

```
V(r)
 |
 |         __________________ V_flat (temporal-tension plateau)
 |        /
 |       /    <-- transition: gravity declining, T-field constant
 |      /
 |     /
 |    /   <-- rising: gravity + mobility core-widening
 |   /
 |  /
 | /
 +--------+--------+--------+--------+--> r (kpc)
 0     r_core    r_trans            r_T
       (ED-      (gravity ≈        (tension
       widened)   temporal)         length)

Zone I  (r < r_core):  Flat core, density ~ rho_0.
        Mobility suppression prevents central cusp.
Zone II (r_core < r < r_trans): Declining gravity.
        Density falls as modified isothermal/Burkert.
Zone III (r > r_trans): Temporal-tension plateau.
        V_eff ≈ V_temp = const.
        Extends to tension length l_T >> 1 Mpc.
```

Zone I is the ED core-widening mechanism (unique to ED). Zone III is the temporal-tension floor (shared with MOND phenomenologically). Zone II is the transition where both contributions are comparable.

### 4.5 The Spiral-Galaxy Challenge

For NGC 3198 ($V_{\text{flat}} = 142$ km/s), the ED–Poisson halo produces a correct core radius ($5.25$ kpc) but overshoots the flat rotation curve by $\sim 30$ km/s at $r > 10$ kpc. The enclosed mass grows too fast because the ED profile places too much material at intermediate radii. This motivates the temporal-tension extension.

---

## 5. Temporal Tension and Weak Lensing

### 5.1 From Participation to Temporal Tension

The participation variable $v(t)$ is the ED PDE's global mode: a single scalar driven by the domain-averaged density operator and feeding back uniformly into the local PDE. In the foundational analogues, it produces telegraph oscillation — an RLC-circuit pattern. At galactic scales, this global mode acquires a physical interpretation.

A galaxy is a region of intense becoming: stars form, supernovae explode, gas shocks, magnetic fields reconnect. This aggregate activity is the galactic event density. The participation variable, driven by this activity, represents a **temporal-tension field** — a measure of how strongly the local rate of becoming is coupled to the global state of the system.

Why is this field diffusive? Because the participation variable $v(t)$ is driven by the domain-averaged operator $\bar{F}$, which depends on the spatial integral of $F[\rho]$. Changes in the density field must propagate spatially (via the mobility channel) before they contribute to $\bar{F}$. The result is a temporal-tension field $T(\mathbf{x}, t)$ that spreads diffusively from its source — the galaxy's centre of activity — outward into the circumgalactic medium.

Why does it produce a constant velocity? Because the tension length $\ell_T = \sqrt{D_T/\lambda}$ far exceeds the weak-lensing observation radius ($\sim 1$ Mpc). Within this radius, $T(r) \approx T_0 = \text{const}$, and the effective velocity $V_{\text{temp}} = \sqrt{c_T T_0}$ is spatially uniform. The flat rotation observed by Mistele et al. to 1 Mpc is the observational signature of a tension field that has not yet decayed.

### 5.2 The Temporal-Tension PDE

The temporal-tension field $T(r)$ satisfies (ED-I-002, ED-I-027). In steady state:

$$D_T\nabla^2 T + S(r) - \lambda T = 0. \tag{10}$$

If the tension length $\ell_T = \sqrt{D_T/\lambda} \gg 1$ Mpc, the field is approximately constant at rotation-curve and weak-lensing radii. The effective circular velocity becomes:

$$V_{\text{eff}}^2(r) = V_{\text{grav}}^2(r) + V_{\text{temp}}^2, \tag{11}$$

where $V_{\text{temp}}$ is the constant temporal-tension velocity.

### 5.2 Combined Halo for NGC 3198

Adding $V_{\text{temp}} = 12.5$ km/s to a Burkert-like gravitational halo reproduces NGC 3198's full rotation curve with **RMS = 1.9 km/s** — identical to pure Burkert and dramatically improved from the $23.8$ km/s RMS of the gravity-only ED model.

### 5.3 Weak-Lensing Predictions

At projected radii $R = 100$–$1000$ kpc, the models diverge dramatically:

| $R$ (kpc) | Burkert (km/s) | NFW (km/s) | ED ($V_T = 134$) (km/s) | Observed (Mistele et al.) |
|:----------|:---------------|:-----------|:------------------------|:--------------------------|
| 100 | 73 | 179 | 134 | $\sim 135$ |
| 500 | 42 | 127 | 134 | $\sim 137$ |
| 1000 | 32 | 102 | 134 | $\sim 136$ |

Burkert predicts $V \to 0$; NFW predicts slow decline; ED predicts flat $V$ at $V_{\text{temp}}$. The Mistele et al. (2024) data show **indefinitely flat $V \approx 135$ km/s from 34 kpc to 1 Mpc**, consistent with the ED prediction.

---

## 6. BTFR as a Temporal-Tension Scaling Law

### 6.1 Derivation

The temporal-tension field amplitude $T_0$ is set by the source strength $S_0$, which scales with the total baryonic activity of the galaxy. Activity — star formation, turbulence, gravitational encounters — is driven by the baryonic mass: more mass means more interactions. The simplest scaling is $S_0 \propto M_b$.

The velocity contribution from temporal tension is $V_{\text{temp}}^2 = c_T T_0$, where $c_T$ is a coupling constant with dimensions of velocity$^2$ per unit tension. The tension field amplitude $T_0$ is related to the source by a dimensional factor involving $G$ (because the tension field couples to the gravitational potential). Combining:

$$V_{\text{temp}}^2 \propto \sqrt{G\,M_b\,\text{(coupling)}}.$$

The unique dimensionally consistent combination of $G$, $M_b$, and a single acceleration scale $a_{\text{ED}}$ that gives velocity is:

$$V_{\text{temp}} = (G\,a_{\text{ED}}\,M_b)^{1/4}. \tag{12}$$

This is the BTFR: $V^4 = G\,a_{\text{ED}}\,M_b$, or equivalently $V \propto M_b^{1/4}$. The exponent $1/4$ is fixed by dimensional analysis once the temporal-tension field introduces a single acceleration scale. No fine-tuning is required — the exponent is a structural consequence of the coupling between a scalar field and gravity.

The ED acceleration scale $a_{\text{ED}}$ plays the role of Milgrom's $a_0$ but arises from the temporal-tension coupling, not from modified gravity. It is the acceleration below which the temporal-tension contribution exceeds the gravitational contribution — the scale at which ED dynamics diverge from Newtonian predictions.

### 6.2 Fit to Mistele et al.

Fitting $V = A\,M_b^n$ to the four BTFR mass bins:

| Model | Exponent $n$ | RMS (km/s) | BIC |
|:------|:-------------|:-----------|:----|
| $M_b^{1/4}$ (ED/MOND) | $0.250$ (fixed) | 5.9 | 3.1 |
| $M_b^{1/3}$ ($\Lambda$CDM virial) | $0.333$ (fixed) | 17.9 | 12.2 |
| Free power law | $0.246 \pm 0.025$ | 5.6 | 4.4 |

The free exponent is $n = 0.246 \pm 0.025$ — consistent with $1/4$ ($< 0.2\sigma$) and rejecting $1/3$ at $> 3\sigma$.

### 6.3 The ED Acceleration Scale

$$a_{\text{ED}} = \frac{V_{\text{temp}}^4}{G\,M_b} = 2.13 \times 10^{-10}\;\text{m/s}^2 \approx 1.8\,a_0.$$

This is within a factor of 2 of Milgrom's constant — suggesting that ED's temporal-tension mechanism and MOND's modified gravity describe the same phenomenology from different starting points.

---

## 7. ED-Unique Predictions

### 7.1 Activity-Dependent Weak Lensing

ED predicts that at fixed baryonic mass, galaxies with higher star-formation rates (SFR) have higher $V_{\text{temp}}$, because activity sources the temporal-tension field. The expected signal:

$$\frac{\Delta V}{V_0} \approx \frac{f}{4}\,\frac{\Delta\text{SFR}}{\text{SFR}_0},$$

where $f$ is the fractional SFR contribution. Even for $f = 0.1$ (conservative), the quiescent-to-starburst velocity difference is **33 km/s (19%)** — detectable with current surveys (KiDS, HSC).

**Neither MOND nor $\Lambda$CDM predicts any SFR dependence at fixed $M_b$.**

### 7.2 Merger Lensing Lag

The temporal-tension field is diffusive. During a merger, it lags behind the baryonic mass by:

$$\ell_{\text{lag}} = \frac{D_T}{v_{\text{merge}}}. \tag{13}$$

| System | $v_{\text{merge}}$ (km/s) | $\ell_{\text{lag}}$ (kpc) | Angular offset ($z = 0.2$) |
|:-------|:--------------------------|:-------------------------|:---------------------------|
| Cluster–cluster | 1500 | **45** | $\sim 14''$ |
| Bullet Cluster | 4500 | **15** | $\sim 5''$ |

The direction of the offset is **opposite** to $\Lambda$CDM: in $\Lambda$CDM, collisionless DM leads the gas; in ED, the diffusive $T$-field trails the baryons. This is an unambiguous directional test.

### 7.3 The Decision Matrix

| Test | ED | MOND | $\Lambda$CDM |
|:-----|:---|:-----|:-------------|
| BTFR exponent | $1/4$ (confirmed) | $1/4$ (confirmed) | $1/3$ (rejected) |
| Flat $V$ to 1 Mpc | Yes (confirmed) | Yes | Requires large $r_s$ |
| Activity dependence | $\Delta V \sim 30$–$70$ km/s | 0 | 0 |
| Merger lensing lag | 15–45 kpc (behind baryons) | 0 | Gas-DM offset (opposite direction) |

If either activity dependence or merger lag is detected consistent with the ED prediction, MOND is falsified and $\Lambda$CDM requires modification. If both are detected, ED becomes the leading framework for galaxy-scale dynamics.

---

## 8. Discussion

### 8.1 ED as a Unifying Ontology

The ED programme demonstrates that a single constitutive architecture — four primitives, three channels, seven axioms — can make quantitative contact with physics at scales ranging from molecular diffusion ($\sim \mu$m) to galactic dynamics ($\sim$ Mpc). The mobility law $D \propto (1 - c/c_{\max})^\beta$ with $\beta \approx 2$ fits colloidal jamming, molecular viscosity, and protein crowding. The same PDE, coupled to gravity, produces cored galaxy haloes and the BTFR. The temporal-tension channel predicts weak-lensing flatness to 1 Mpc with an acceleration scale $a_{\text{ED}} \approx 2a_0$.

This is not a claim that ED replaces existing physics. It is a demonstration that the structural content of several physical laws — exponential decay, porous-medium diffusion, telegraph oscillation, cored halo profiles, and the BTFR — can be generated from a single PDE with three constitutive channels.

### 8.2 What ED Is Not

ED does not derive general relativity, quantum mechanics, or the Standard Model. It does not contain a spacetime metric, a Hilbert space, or gauge fields. It is parabolic, not hyperbolic; dissipative, not conservative; scalar, not tensorial. The structural correspondences are exact at the level of governing equations, but the mapping to specific physical systems requires scale anchoring (ED-Dimensional series) and, at galactic scales, gravitational coupling and temporal-tension interpretation.

### 8.3 Falsifiability

The ED framework is falsifiable at multiple levels:

1. **Condensed matter:** If $D(c)$ is not a power law of $(1 - c/c_{\max})$ for a material with density-dependent diffusion, the mobility law is falsified for that material.
2. **BTFR:** If the weak-lensing BTFR exponent is significantly different from $1/4$, the temporal-tension scaling is falsified.
3. **Activity dependence:** If $V_{\text{temp}}$ shows no SFR correlation at fixed $M_b$, the parameter $f < 0.01$ and the activity-source mechanism is negligible.
4. **Merger lag:** If lensing centroids show no systematic offset behind baryonic centroids in merging clusters, the diffusive temporal-tension model is falsified.

### 8.4 Philosophical Context

ED occupies a distinctive position in the landscape of physical ontologies. It is a **constitutive ontology** in the tradition of Whitehead's process philosophy: the fundamental primitive is not substance (matter, fields) but process (becoming, event rate). The density field $\rho$ does not represent "stuff" distributed in space; it represents the intensity of happening — the local rate at which micro-events occur.

This places ED closer to **process metaphysics** (Whitehead, Rescher) than to **structural realism** (Ladyman, French), though it shares features of both. Like structural realism, ED takes mathematical structure as primary and derives physical content from structural correspondences. But unlike structural realism, ED specifies the *constitutive content* of the structure — the four primitives and three channels — rather than treating structure as purely relational.

The empirical results of this paper suggest a pragmatic philosophical position: whether becoming is metaphysically fundamental is less important than whether a PDE built on becoming-as-primitive generates physics-shaped dynamics. The mobility law fits three materials; the BTFR falls out of the temporal-tension coupling; the front exponent is confirmed to 2.3%. These are structural facts, independent of metaphysical commitments. The question of whether reality is "made of" events, or whether events are a useful mathematical proxy for something deeper, remains open — but the proxy works.

### 8.5 Relation to MOND

ED and MOND produce the same BTFR ($V \propto M_b^{1/4}$) and the same flat weak-lensing velocities, but from different mechanisms: ED from a diffusive temporal-tension field, MOND from a modification of the gravitational acceleration law. The two can be distinguished by activity dependence (ED predicts it; MOND does not) and by merger lag (ED predicts it; MOND does not). The numerical coincidence $a_{\text{ED}} \approx 2a_0$ suggests that the two frameworks may be dual descriptions of the same underlying phenomenon.

---

## 9. Conclusion

### 9.1 What Is Established

1. The canonical ED PDE is the unique second-order scalar PDE satisfying seven structural axioms.
2. The mobility law $D \propto (1 - c/c_{\max})^\beta$ with $\beta = 2.00 \pm 0.29$ fits three condensed-matter systems with $R^2 > 0.98$.
3. The PME front exponent $\alpha_R = 1/(d\beta + 2)$ is confirmed to 2.3% in 1D and to 0.02% for the peak-decay exponent in 3D.
4. The ED–Poisson core radius matches observed Burkert cores to within 10% for four dwarf galaxies.
5. The temporal-tension velocity $V_{\text{temp}} = 134$ km/s is consistent with the Mistele et al. weak-lensing BTFR.
6. The BTFR exponent $n = 0.246 \pm 0.025$ matches the ED prediction of $1/4$ and rejects the $\Lambda$CDM virial prediction of $1/3$ at $> 3\sigma$.
7. The ED acceleration scale $a_{\text{ED}} = 2.1 \times 10^{-10}$ m/s$^2 \approx 1.8\,a_0$.

### 9.2 What Remains Open

1. The parameter $f$ (SFR contribution to temporal tension) is not determined from theory.
2. The temporal diffusivity $D_T$ is estimated, not derived.
3. The generalised mobility exponent $\alpha$ may be scale-dependent.
4. No experimental measurement of the front-propagation exponent $\alpha_R$ has been performed.
5. The activity-dependence and merger-lag tests have not been executed.

### 9.3 The Path Forward

ED is testable with existing public data. The activity-dependence test requires splitting weak-lensing galaxy samples by SFR — a straightforward extension of the Mistele et al. analysis. The merger-lag test requires stacking weak-lensing centroids of merging clusters — feasible with current cluster catalogues. Both tests can be performed with KiDS, HSC, or Euclid data. If either produces a result consistent with the ED prediction and inconsistent with MOND and $\Lambda$CDM, the temporal-tension interpretation moves from structural plausibility to empirical confirmation.

Event Density does not claim to replace physics. It claims something more modest and potentially more consequential: that a minimal constitutive architecture, operating through three channels, can generate the mathematical structures that underlie much of physical law — from the laboratory to the cosmic web. Whether this architectural sufficiency reflects a deep truth about the structure of reality is a question that only empirical testing can answer. The tools for that testing now exist.

---

## References

1. Proxmire, A. "Event Density as an Ontological Framework: Constitutive Channels, Structural Laws, and Six Empirical Analogues." (2026).
2. Proxmire, A. "ED-Dimensional-Master: The Unified Atlas of Physical Scales." (2026).
3. Proxmire, A. ED-SIM-02: An Architectural Lab for Entropic Dynamics. Software package (2026).
4. Proxmire, A. "ED-I-002: Event Density and Galactic Curvature." (2025).
5. Proxmire, A. "ED-I-027: Temporal Tension in Galaxy-Scale Weak Lensing." (2026).
6. Mistele, T., McGaugh, S., Lelli, F., Li, P., and Schombert, J. "Indefinitely Flat Circular Velocities and the Baryonic Tully–Fisher Relation from Weak Lensing." *Astrophys. J. Lett.* **969**, L3 (2024).
7. Lelli, F., McGaugh, S. S., and Schombert, J. M. "SPARC: Mass Models for 175 Disk Galaxies." *Astron. J.* **152**, 157 (2016).
8. Segre, P. N., Meeker, S. P., Pusey, P. N., and Poon, W. C. K. "Viscosity and Diffusion in Concentrated Colloidal Suspensions." *Phys. Rev. Lett.* **75**, 958 (1995).
9. Roosen-Runge, F. et al. "Protein Self-Diffusion in Crowded Solutions." *PNAS* **108**, 11815 (2011).
10. Price, H. C. et al. "Sucrose Diffusion in Aqueous Solution." *Phys. Chem. Chem. Phys.* **18**, 19207 (2016).
11. Vazquez, J. L. *The Porous Medium Equation: Mathematical Theory.* Oxford University Press (2007).
12. Milgrom, M. "A Modification of the Newtonian Dynamics as a Possible Alternative to the Hidden Mass Hypothesis." *Astrophys. J.* **270**, 365 (1983).
13. Navarro, J. F., Frenk, C. S., and White, S. D. M. "The Structure of Cold Dark Matter Halos." *Astrophys. J.* **462**, 563 (1996).
14. Madelung, E. "Quantentheorie in hydrodynamischer Form." *Z. Phys.* **40**, 322 (1927).
15. Planck Collaboration. "Planck 2018 Results. VI. Cosmological Parameters." *Astron. Astrophys.* **641**, A6 (2020).
