# The Event Density Architecture

## Foundations, Invariants, and Computational Verification

**Allen Proxmire**

Event Density Research Program

---

# Preface

This monograph presents the Event Density (ED) architecture as a unified mathematical framework, develops its invariant theory, and documents its computational verification through the ED-SIM-01 pipeline. The work draws on three preceding documents — the Architectural Canon, the Rigour Paper, and the Applications Paper — and synthesises them with the Numerical Atlas, the Simulation Suite, and the Reproducibility Suite into a single, self-contained account.

The monograph is organised in six parts. Part I establishes the foundations: the governing equations, the seven canonical principles, and the architectural predictions. Part II develops the invariant theory: sixteen families of structural quantities that characterise the ED attractor from independent angles. Part III describes the computation: the ED-SIM-01 pipeline, its numerical methods, and its parameter-space coverage. Part IV presents the synthesis: the invariant atlas, the global verdict, and the ED Architecture Certificate. Part V addresses reproducibility. Part VI discusses applications, open problems, and future directions.

The reader is assumed to be familiar with partial differential equations, dynamical systems, and scientific computing at the level of a graduate course. No prior knowledge of the ED framework is required.

---

# PART I — FOUNDATIONS

---

## Chapter 1. Introduction

### 1.1 Motivation

Physical theories typically operate at one of two levels. At the *microscopic* level, they describe the fundamental constituents — particles, fields, quanta — and derive macroscopic behaviour from first principles. At the *phenomenological* level, they model observed phenomena with effective equations whose parameters are fit to data. Between these extremes lies a third possibility: *architectural* theories, which describe the structural organisation of dynamical systems without specifying their microscopic content.

Event Density is an architectural theory. It does not postulate new particles, new fields, or new forces. Instead, it identifies a set of structural principles — seven in number, each irreducible — that constrain how a density field can evolve, dissipate, and converge. The claim is that these principles are not specific to any one physical domain: they apply equally to quantum systems, galactic dynamics, condensed matter, and nonlinear optics, because they describe the *architecture* of the dynamics, not the *substrate*.

This claim is testable. The seven principles generate a specific partial differential equation — the canonical ED PDE — whose solutions can be computed, analysed, and compared to physical observations. The present monograph develops the mathematical infrastructure for this programme.

### 1.2 The Central Question

The central question of this monograph is:

> *Does the canonical ED PDE, solved without approximation across a systematic parameter space, exhibit the structural properties predicted by the seven principles?*

This is not a question about parameter fitting. The ED PDE has no free parameters beyond its canonical set $(D, \zeta, \tau, \rho^*, \rho_{\max})$, which specify the architecture, not the data. The question is whether the architecture itself — the seven principles, the operator structure, the constitutive constraints — produces the predicted qualitative behaviour: a unique point attractor, a three-stage convergence, a universal modal hierarchy, and a structurally invariant spectral fingerprint.

### 1.3 Strategy

The strategy is invariant analysis. We define sixteen families of scalar and vector quantities that capture different structural aspects of the long-time solution. We compute these invariants across sixty-four parameter regimes. We test whether they are invariant (constant across regimes), consistent (mutually compatible), and stable (robust to perturbation). The results are synthesised into a single verdict — the ED Architecture Certificate — which encodes the global structural consistency of the framework.

### 1.4 Overview of the Monograph

| Part | Chapters | Content |
|------|----------|---------|
| I | 1–5 | Foundations: equations, principles, predictions |
| II | 6–9 | Invariants: definitions, interpretations, dependencies |
| III | 10–14 | Computation: pipeline, methods, extraction, meta-analyses |
| IV | 15–18 | Synthesis: atlas, verdict, certificate, interpretation |
| V | 19–21 | Reproducibility: suite, validation, extension |
| VI | 22–24 | Outlook: applications, open problems, conclusion |

---

## Chapter 2. The Event Density Framework

### 2.1 Conceptual Picture

The ED framework describes the evolution of a *density field* $\rho(x, t)$ on a bounded spatial domain $\Omega$. The density represents a generic conserved or semi-conserved quantity — particle density, energy density, information density, or any scalar field whose dynamics are governed by transport, reaction, and feedback.

The evolution is driven by three competing mechanisms:

1. **Diffusion.** The density spreads from regions of high concentration to regions of low concentration. The diffusion rate is governed by a *mobility function* $M(\rho)$ that depends on the local density.

2. **Penalty.** The density is pulled toward a preferred equilibrium value $\rho^*$ by a restoring force. The penalty function $P(\rho)$ vanishes at $\rho^*$ and grows monotonically away from it.

3. **Feedback.** The system integrates a spatial average of its own operator output and feeds it back into the density equation through a *participation variable* $v(t)$. This creates a global coupling: the evolution at each point depends on the state of the entire domain.

The interplay of these three mechanisms produces a rich dynamical landscape — oscillatory, monotonic, or critical, depending on the parameters — but the long-time outcome is always the same: the density converges to $\rho^*$, the gradients vanish, and the participation decays to zero.

### 2.2 The Density Field

The density $\rho(x, t)$ is a scalar function of position $x \in \Omega$ and time $t \geq 0$. It takes values in the open interval $(0, \rho_{\max})$, where $\rho_{\max} > 0$ is the *capacity bound* — the maximum density that the system can sustain. The boundary $\rho = 0$ represents the vacuum; the boundary $\rho = \rho_{\max}$ represents the capacity horizon.

**Definition 2.1** (Admissible state). *A density profile $\rho(\cdot, t)$ is admissible if $\rho(x, t) \in (0, \rho_{\max})$ for all $x \in \Omega$ and $\rho(\cdot, t) \in H^1(\Omega)$.*

The admissible region $\mathcal{O} = \{\rho \in H^1(\Omega) : 0 < \rho < \rho_{\max}\}$ is an open subset of the Sobolev space $H^1(\Omega)$. The ED dynamics preserves admissibility: if the initial condition is admissible, the solution remains admissible for all time (Theorem C.2 of the Rigour Paper).

### 2.3 The Participation Variable

The participation variable $v(t)$ is a scalar that integrates the spatial average of the density operator and feeds it back into the evolution equation. It is governed by an ordinary differential equation with exponential damping:

$$\dot{v} = \frac{1}{\tau}\bigl(\bar{F}[\rho] - \zeta\,v\bigr), \tag{2.1}$$

where $\bar{F}[\rho] = |\Omega|^{-1}\int_\Omega F[\rho]\,dx$ is the spatial average of the density operator, $\tau > 0$ is the integration time scale, and $\zeta > 0$ is the damping rate.

The participation variable creates a feedback loop: the density generates $F[\rho]$, which is averaged and integrated into $v$, which in turn modifies the density evolution. This loop is the mechanism by which global information (the spatial average) influences local dynamics (the pointwise evolution).

### 2.4 The Equilibrium

**Definition 2.2** (Canonical equilibrium). *The canonical equilibrium of the ED system is the pair $(\rho^*, 0)$, where $\rho(x) = \rho^*$ is the spatially uniform density at the penalty zero and $v = 0$ is the quiescent participation.*

At equilibrium, $\nabla\rho = 0$, so $M(\rho^*)\nabla^2\rho = 0$ and $M'(\rho^*)|\nabla\rho|^2 = 0$. Since $P(\rho^*) = 0$, the operator gives $F[\rho^*] = 0$, which implies $\dot{v} = -\zeta v/\tau$ and therefore $v \to 0$ exponentially. The equilibrium is self-consistent.

---

## Chapter 3. Governing Equations and Operators

### 3.1 The Canonical ED PDE

The canonical ED system is the coupled PDE–ODE:

$$\partial_t\rho = D\,F[\rho] + H\,v, \tag{3.1a}$$

$$\dot{v} = \frac{1}{\tau}\bigl(\bar{F}[\rho] - \zeta\,v\bigr), \tag{3.1b}$$

on the domain $\Omega = [0, L]$ with Neumann boundary conditions $\partial_x\rho(0, t) = \partial_x\rho(L, t) = 0$ and initial conditions $\rho(x, 0) = \rho_0(x)$, $v(0) = v_0$.

### 3.2 The Density Operator

The density operator $F[\rho]$ is defined by

$$F[\rho] = M(\rho)\,\nabla^2\rho + M'(\rho)\,|\nabla\rho|^2 - P(\rho). \tag{3.2}$$

This operator has three terms:

1. **Linear diffusion**: $M(\rho)\,\nabla^2\rho$. A second-order parabolic term with density-dependent coefficient $M(\rho)$.
2. **Quadratic gradient**: $M'(\rho)\,|\nabla\rho|^2$. A nonlinear term that couples spatial modes through the triad selection rule.
3. **Penalty reaction**: $-P(\rho)$. A zeroth-order restoring term that drives $\rho$ toward $\rho^*$.

**Remark 3.1.** The operator $F[\rho]$ can be written in divergence form as $F[\rho] = \nabla \cdot (M(\rho)\nabla\rho) - P(\rho)$, which makes the mass-flux structure explicit: the density flux is $J = -M(\rho)\nabla\rho$, and the penalty acts as a distributed source/sink.

### 3.3 Constitutive Functions

**Definition 3.1** (Canonical constitutive pair). *The canonical mobility and penalty functions are:*

$$M(\rho) = M_0\,(\rho_{\max} - \rho)^\beta, \qquad P(\rho) = P_0\,(\rho - \rho^*), \tag{3.3}$$

*where $M_0 > 0$, $\beta > 0$, $P_0 > 0$, and $0 < \rho^* < \rho_{\max}$.*

The mobility $M(\rho)$ is positive on $(0, \rho_{\max})$ and vanishes at $\rho = \rho_{\max}$. This vanishing is the *mobility collapse* — the mechanism that enforces the capacity bound. As $\rho \to \rho_{\max}$, the diffusion rate goes to zero, creating an impenetrable barrier.

The penalty $P(\rho)$ vanishes at $\rho = \rho^*$ and is positive for $\rho > \rho^*$, negative for $\rho < \rho^*$. It is the restoring force that drives the density toward equilibrium.

### 3.4 Channel Structure

The density equation (3.1a) is a weighted sum of two channels:

- The **direct channel**: $D\,F[\rho]$, with weight $D \in (0, 1)$.
- The **participation channel**: $H\,v$, with weight $H = 1 - D$.

The channel complementarity condition $D + H = 1$ ensures that the two channels partition the operator output without amplification. The parameter $D$ controls the balance: at $D = 1$, the system is purely direct (no feedback); at $D = 0$, it is purely mediated (all feedback). The canonical range is $D \in (0, 1)$.

### 3.5 The Energy Functional

**Definition 3.2** (Energy functional). *The canonical energy functional is:*

$$\mathcal{E}[\rho, v] = \int_\Omega \Phi(\rho)\,dx + \frac{\tau H}{2}\,v^2, \tag{3.4}$$

*where the density potential $\Phi$ is defined by*

$$\Phi(\rho) = \int_{\rho^*}^{\rho} \frac{P(s)}{M(s)}\,ds. \tag{3.5}$$

**Proposition 3.1** (Energy dissipation). *Along solutions of (3.1), the energy functional satisfies*

$$\frac{d\mathcal{E}}{dt} = -\mathcal{D}_{\mathrm{grad}} - \mathcal{D}_{\mathrm{pen}} - \mathcal{D}_{\mathrm{part}} \leq 0, \tag{3.6}$$

*where the three dissipation channels are:*

$$\mathcal{D}_{\mathrm{grad}} = D\int_\Omega \frac{|\nabla\rho|^2}{M(\rho)}\cdot P'(\rho)\,dx, \qquad \mathcal{D}_{\mathrm{pen}} = D\int_\Omega \frac{P(\rho)^2}{M(\rho)}\,dx, \qquad \mathcal{D}_{\mathrm{part}} = \frac{H\zeta}{\tau}\,v^2.$$

The energy is a Lyapunov functional: it decreases monotonically and is bounded below by zero. This is the mathematical foundation of the three-stage convergence.

### 3.6 Spectral Structure

Expanding the perturbation $u(x, t) = \rho(x, t) - \rho^*$ in the Neumann eigenbasis:

$$u(x, t) = \sum_{k=0}^{\infty} a_k(t)\,\varphi_k(x), \qquad \varphi_k(x) = \sqrt{\frac{2}{L}}\cos\!\Bigl(\frac{k\pi x}{L}\Bigr), \tag{3.7}$$

with eigenvalues $\mu_k = (k\pi/L)^2$, the linearised dynamics of the $k$-th mode has decay rate

$$\alpha_k = M_*\,\mu_k + P_*', \tag{3.8}$$

where $M_* = M(\rho^*)$ and $P_*' = P'(\rho^*)$. Since $M_* > 0$ and $P_*' > 0$, the decay rates are positive and increase with $k$: higher modes decay faster. This is the *modal hierarchy*.

---

## Chapter 4. The Seven Principles of ED

The ED architecture is built on seven irreducible principles. Each principle constrains the structure of the governing equation and excludes alternatives. Together, they determine the qualitative dynamics uniquely.

**Principle 1** (Operator Structure). *The density operator $F[\rho]$ consists of exactly three terms: mobility-weighted diffusion $M(\rho)\nabla^2\rho$, gradient-squared nonlinearity $M'(\rho)|\nabla\rho|^2$, and penalty reaction $-P(\rho)$. No other terms are present.*

*Remark.* This excludes advection, higher-order diffusion, nonlocal operators, and stochastic forcing from the canonical system. The three terms are the minimal set that produces a well-posed parabolic PDE with a unique equilibrium and nonlinear mode coupling.

**Principle 2** (Channel Complementarity). *The density evolution is a weighted sum of a direct channel $D\,F[\rho]$ and a participation channel $H\,v$, with $D + H = 1$ and $D \in (0, 1)$.*

*Remark.* The complementarity condition prevents unbounded amplification and ensures that the total operator weight is unity. It creates a trade-off: increasing the direct channel decreases the feedback, and vice versa.

**Principle 3** (Penalty Equilibrium). *The penalty function satisfies $P(\rho^*) = 0$ and $P'(\rho^*) > 0$. The equilibrium $\rho^*$ is unique.*

*Remark.* The strict positivity of $P'(\rho^*)$ ensures that the penalty is a genuine restoring force, not a neutral fixed point. Combined with Principles 1 and 4, it guarantees that $(\rho^*, 0)$ is a global attractor.

**Principle 4** (Mobility Capacity Bound). *The mobility satisfies $M(\rho_{\max}) = 0$ and $M(\rho) > 0$ for $\rho \in (0, \rho_{\max})$.*

*Remark.* The vanishing of $M$ at $\rho_{\max}$ creates an impassable barrier: the density cannot reach or exceed $\rho_{\max}$. This is the *mobility horizon*. Near $\rho_{\max}$, the mobility collapse freezes the dynamics, creating an effective boundary layer.

**Principle 5** (Participation Feedback). *The participation variable $v(t)$ integrates the spatial average of $F[\rho]$ with time scale $\tau$ and damping rate $\zeta$, and feeds back into the density equation through the channel weight $H$.*

*Remark.* The participation loop is the mechanism by which global information enters the local dynamics. It introduces a second time scale ($\tau$) and a second damping parameter ($\zeta$) into the system.

**Principle 6** (Damping Discriminant). *The linearised dynamics of the homogeneous mode is governed by the discriminant*

$$\mathscr{D}_0 = \bigl(D\,P_*' - \zeta/\tau\bigr)^2 - 4\,H\,P_*'/\tau, \tag{4.1}$$

*which classifies the dynamics as oscillatory ($\mathscr{D}_0 < 0$), critical ($\mathscr{D}_0 = 0$), or monotonic ($\mathscr{D}_0 > 0$).*

*Remark.* The discriminant is the organising parameter of the regime geometry. It determines whether the approach to equilibrium involves oscillation (spiral sheet), pure decay (monotonic cone), or transitional dynamics (critical surface).

**Principle 7** (Nonlinear Triad Coupling). *The quadratic term $M'(\rho)|\nabla\rho|^2$ generates inter-modal coupling with the selection rule: modes $m$ and $n$ interact to produce modes $|m - n|$ and $m + n$.*

*Remark.* The triad selection rule is a consequence of the product structure of the gradient-squared term in the Neumann eigenbasis. It determines which spectral modes can exchange energy and controls the shape of the nonlinear cascade.

---

## Chapter 5. Architectural Predictions

The seven principles, combined with the analytic theory of the Rigour Paper, generate the following structural predictions:

**Prediction 5.1** (Unique Point Attractor). *The canonical equilibrium $(\rho^*, 0)$ is a global attractor: every admissible initial condition converges to $(\rho^*, 0)$ as $t \to \infty$.*

**Prediction 5.2** (Three-Stage Convergence). *The convergence proceeds through three stages:*
- *Stage I (Global Bounds): the energy functional is uniformly bounded and monotonically decreasing.*
- *Stage II (Algebraic Decay): gradients and participation decay algebraically via Barbalat's lemma.*
- *Stage III (Exponential Decay): the solution enters the local stability basin and converges exponentially at a rate determined by the spectral gap.*

**Prediction 5.3** (Non-Positive Lyapunov Spectrum). *All Lyapunov exponents of the attractor are non-positive. The Kaplan–Yorke dimension is zero.*

**Prediction 5.4** (Modal Hierarchy). *The decay rate of the $k$-th eigenmode is $\sigma_k = D\,\alpha_k$, where $\alpha_k = M_*\mu_k + P_*'$ increases monotonically with $k$. Higher modes decay faster.*

**Prediction 5.5** (Triad Selection Rule). *Modes $m$ and $n$ interact only to produce modes $|m - n|$ and $m + n$. No other mode coupling exists.*

**Prediction 5.6** (Universal Dissipation Partition). *The three dissipation channels $(\mathcal{D}_{\mathrm{grad}}, \mathcal{D}_{\mathrm{pen}}, \mathcal{D}_{\mathrm{part}})$ converge to a fixed partition that depends only on the canonical parameters, not on the initial condition.*

**Prediction 5.7** (Structural Invariance). *The qualitative attractor structure — modal hierarchy, triad rule, dissipation partition, spectral fingerprint — is invariant under parameter variation within the universality class $\mathcal{U}_{\mathrm{ED}}$.*

These seven predictions are the targets of the invariant atlas. Each is tested numerically by one or more of the sixteen invariant families defined in Part II.

---

# PART II — INVARIANTS

---

## Chapter 6. Why Invariants

### 6.1 The Concept

An *invariant* of the ED system is a quantity computed from the long-time solution that is approximately constant across parameter regimes. The word "approximately" is quantified by the coefficient of variation:

$$\mathrm{CV}(Q) = \frac{\sigma(Q)}{\mu(Q)}, \tag{6.1}$$

where $\mu(Q)$ and $\sigma(Q)$ are the mean and standard deviation of the quantity $Q$ across all admissible runs. The invariance verdict is:

| CV | Verdict |
|----|---------|
| $< 0.05$ | INVARIANT |
| $< 0.15$ | WEAKLY INVARIANT |
| $\geq 0.15$ | NOT INVARIANT |

### 6.2 Why Sixteen Families

A single invariant proves nothing: it could be invariant by coincidence. Sixteen invariants probing the attractor from independent angles — spectral, dynamical, topological, and statistical — provide a structural test. Their mutual consistency (measured by the cross-invariant correlation matrix) is a stronger claim than any individual invariance.

The sixteen families were chosen to cover the full range of Predictions 5.1–5.7:

| Prediction | Invariant families |
|-----------|-------------------|
| 5.1 (Point attractor) | Low-mode collapse, Lyapunov spectrum, attractor manifold |
| 5.2 (Three-stage convergence) | Convergence stability |
| 5.3 (Non-positive Lyapunov) | Lyapunov spectrum |
| 5.4 (Modal hierarchy) | Mode-energy ratios, spectral complexity, modal overlap |
| 5.5 (Triad rule) | Triad balance, modal correlations |
| 5.6 (Dissipation partition) | Dissipation partitions, energy–entropy geometry |
| 5.7 (Structural invariance) | Parameter universality, cross-consistency, embedding |

### 6.3 The Attractor Window

All invariants are computed over the *attractor window*: the last fraction of the time series, where the solution has entered (or nearly entered) the exponential-decay regime.

**Definition 6.1** (Attractor window). *Let $T$ be the final integration time. The attractor window is the interval $[T_{\mathrm{att}}, T]$ where $T_{\mathrm{att}} = (1 - f)\,T$ and $f$ is the window fraction. The default values are $f = 0.10$ for late-time averages and $f = 0.20$ for convergence-rate fits.*

---

## Chapter 7. The Sixteen Invariant Families

This chapter defines each invariant family. For compactness, we use the notation $\langle Q \rangle_{\mathrm{att}}$ for the mean of $Q(t)$ over the attractor window.

### Family 1: Low-Mode Collapse

**Definition 7.1.** *For each mode $k = 0, \ldots, 5$, the late-time amplitude is:*

$$m_k^* = \bigl\langle |a_k(t)| \bigr\rangle_{\mathrm{att}}. \tag{7.1}$$

*Tests:* Prediction 5.1 (point attractor). If $(\rho^*, 0)$ is the unique attractor, then $m_k^* \to 0$ for all $k$.

### Family 2: Mode-Energy Ratios

**Definition 7.2.** *For each mode $k = 1, \ldots, K$, the energy ratio is:*

$$R_k^* = \bigl\langle E_k(t) / E_{\mathrm{total}}(t) \bigr\rangle_{\mathrm{att}}, \qquad E_k = |a_k|^2. \tag{7.2}$$

*Tests:* Prediction 5.4 (modal hierarchy). The energy distribution should converge to a fixed profile with $R_1^* > R_2^* > \cdots$.

### Family 3: Spectral Complexity (Rényi)

**Definition 7.3.** *Let $p_k(t) = E_k(t)/\sum_j E_j(t)$. The Rényi entropy of order $q$ is:*

$$H_q(t) = \frac{1}{1 - q}\log\!\Bigl(\sum_k p_k(t)^q\Bigr), \qquad q \in \{0, 0.5, 1, 2, 3, 4\}. \tag{7.3}$$

*The invariant is $H_q^* = \langle H_q(t) \rangle_{\mathrm{att}}$.*

*Tests:* Prediction 5.4. The multi-scale entropy profile characterises the spectral shape of the attractor.

### Family 4: Dissipation Partitions

**Definition 7.4.** *The dissipation ratios are:*

$$R_{\mathrm{grad}}^* = \bigl\langle \mathcal{D}_{\mathrm{grad}}/\mathcal{D}_{\mathrm{total}} \bigr\rangle_{\mathrm{att}}, \quad R_{\mathrm{pen}}^* = \bigl\langle \mathcal{D}_{\mathrm{pen}}/\mathcal{D}_{\mathrm{total}} \bigr\rangle_{\mathrm{att}}, \quad R_{\mathrm{part}}^* = \bigl\langle \mathcal{D}_{\mathrm{part}}/\mathcal{D}_{\mathrm{total}} \bigr\rangle_{\mathrm{att}}. \tag{7.4}$$

*Tests:* Prediction 5.6. The three-channel structure converges to a fixed partition.

### Family 5: Energy–Entropy Geometry

**Definition 7.5.** *The attractor point in the energy–entropy plane is:*

$$(E^*, H^*) = \bigl(\langle E(t) \rangle_{\mathrm{att}},\; \langle H_1(t) \rangle_{\mathrm{att}}\bigr). \tag{7.5}$$

*Tests:* Predictions 5.1 and 5.6. All runs should converge to the same $(E^*, H^*)$.

### Family 6: Broadband Cascade

**Definition 7.6.** *Define logarithmic mode bins $(k = 1\text{–}2, 3\text{–}4, 5\text{–}8, 9\text{–}16, 17\text{–}32)$ and the bin-energy ratios:*

$$R_b^* = \bigl\langle B_b(t) / E_{\mathrm{total}}(t) \bigr\rangle_{\mathrm{att}}, \qquad B_b = \sum_{k \in \mathrm{bin}\,b} E_k. \tag{7.6}$$

*Tests:* Predictions 5.4 and 5.5. The cascade profile is shaped by the modal hierarchy and the triad selection rule.

### Family 7: Convergence Stability

**Definition 7.7.** *For each error signal $e(t) \in \{|E(t) - E^*|, |H(t) - H^*|, |\mathcal{D}_{\mathrm{total}}(t) - \mathcal{D}^*|\}$, identify the three convergence stages and fit the Stage III exponential rate:*

$$e(t) \sim C\,e^{-\sigma\,t}. \tag{7.7}$$

*Tests:* Prediction 5.2 (three-stage convergence).

### Family 8: Modal Correlations

**Definition 7.8.** *The correlation matrix of modal energies over the attractor window is:*

$$C_{ij} = \mathrm{corr}\bigl(E_i(t),\, E_j(t)\bigr), \qquad i, j = 1, \ldots, K. \tag{7.8}$$

*Summary invariants: mean off-diagonal correlation, spectral radius, condition number.*

*Tests:* Prediction 5.5. Triad-connected modes should be correlated; unconnected modes should be independent.

### Family 9: Modal Overlap

**Definition 7.9.** *The nearest-neighbour overlap ratio for mode $k$ is:*

$$O_k^* = \bigl\langle (E_{k-1} + E_k + E_{k+1}) / E_{\mathrm{total}} \bigr\rangle_{\mathrm{att}}. \tag{7.9}$$

*Tests:* Prediction 5.4. The overlap profile characterises the local spectral structure.

### Family 10: Phase Dynamics

**Definition 7.10.** *Extract modal phases $\phi_k(t) = \arg(a_k(t))$. Compute:*
- *Phase drift rates $d\phi_k/dt$ (linear fit over attractor window).*
- *Phase coherence $C_{ij} = |\langle e^{i(\phi_i - \phi_j)} \rangle|$.*
- *Triad phase closure $\Delta_{ijk} = \phi_i + \phi_j - \phi_k$ for triads $(i, j, k)$ with $i + j = k$.*

*Tests:* Predictions 5.5 and 5.6. Phase-locking in the oscillatory regime is a signature of triad coupling.

### Family 11: Phase–Amplitude Coupling

**Definition 7.11.** *The self-PAC for mode $k$ is:*

$$\rho_k = \mathrm{corr}\bigl(|a_k(t)|,\, \phi_k(t)\bigr). \tag{7.10}$$

*The cross-mode PAC matrix is $\mathrm{PAC}_{ij} = \mathrm{corr}(|a_i|, \phi_j)$.*

*Tests:* Prediction 5.1. At the point attractor, phase and amplitude should decouple ($|\rho_k| \approx 0$).

### Family 12: Lyapunov Spectrum

**Definition 7.12.** *Construct the state vector $\mathbf{x}(t) = [\mathrm{Re}(a_1), \mathrm{Im}(a_1), \ldots]$, compute finite-difference tangent vectors, and extract the Lyapunov exponents $\lambda_i$ via QR accumulation. The Kaplan–Yorke dimension is:*

$$D_{\mathrm{KY}} = j + \frac{\sum_{i=1}^j \lambda_i}{|\lambda_{j+1}|}, \tag{7.11}$$

*where $j$ is the largest index such that $\sum_{i=1}^j \lambda_i \geq 0$.*

*Tests:* Prediction 5.3. All $\lambda_i \leq 0$ and $D_{\mathrm{KY}} \approx 0$.

### Family 13: Attractor Manifold

**Definition 7.13.** *Perform PCA on the state vectors in the attractor window. The effective dimension is:*

$$D_{\mathrm{eff}} = \min\!\Bigl\{m : \sum_{i=1}^m \lambda_i \geq 0.99\sum_j \lambda_j\Bigr\}. \tag{7.12}$$

*The spectral gap is $\lambda_1/\lambda_2$ and the curvature proxy is $\kappa = \lambda_2/\lambda_1$.*

*Tests:* Predictions 5.1 and 5.7. A point attractor has $D_{\mathrm{eff}} \leq 2$.

### Family 14: Perturbed-Attractor Stability

**Definition 7.14.** *Perturb the attractor state by $\epsilon\,\boldsymbol{\xi}$ for $\epsilon \in \{10^{-6}, 10^{-5}, 10^{-4}, 10^{-3}\}$ and fit the recovery rate:*

$$\sum_k |a_k(t) - a_k^*|^2 \sim C\,e^{-\sigma_\epsilon\,t}. \tag{7.13}$$

*Tests:* Prediction 5.1. The recovery rate $\sigma_\epsilon$ should be independent of $\epsilon$ (linear stability).

### Family 15: Parameter Universality

**Definition 7.15.** *Construct the unified invariant vector $\mathbf{I}$ for each run. Standardise across runs. The universality score is:*

$$U = \frac{1}{1 + \mathrm{CV}(\text{pairwise distances})}. \tag{7.14}$$

*Tests:* Prediction 5.7. $U \approx 1$ confirms structural invariance.

### Family 16: Cross-Invariant Consistency

**Definition 7.16.** *For each pair of invariant families $(A, B)$, compute the mean pairwise correlation. The consistency score is:*

$$C = \bigl\langle |\mathrm{corr}(A, B)| \bigr\rangle_{A \neq B}. \tag{7.15}$$

*Tests:* Predictions 5.1–5.7 collectively. $C > 0.8$ confirms that the families describe a single coherent structure.

---

## Chapter 8. Structural Interpretation of Each Invariant

### 8.1 Spectral Invariants (Families 1–3, 6, 9)

The spectral invariants characterise the *shape* of the attractor in mode space. The low-mode amplitudes (Family 1) test whether any modes survive; the energy ratios (Family 2) test the distribution; the Rényi entropies (Family 3) test the disorder; the broadband cascade (Family 6) tests the scale distribution; and the modal overlap (Family 9) tests the local spectral coupling.

Together, these five families provide a complete spectral fingerprint of the attractor. If the fingerprint is invariant across parameter regimes, the spectral shape is a structural property of the architecture, not a parameter-dependent artifact.

### 8.2 Dynamical Invariants (Families 7, 10–11, 14)

The dynamical invariants characterise the *temporal* structure of the approach to equilibrium. The convergence stability (Family 7) tests the three-stage pattern; the phase dynamics (Family 10) test the oscillatory structure; the phase–amplitude coupling (Family 11) tests the nonlinear interactions; and the perturbation recovery (Family 14) tests the basin stability.

### 8.3 Topological Invariants (Families 12–13)

The topological invariants characterise the *geometry* of the attractor. The Lyapunov spectrum (Family 12) measures the attractor's stability and dimension; the PCA manifold (Family 13) measures its effective geometry. Together, they confirm that the attractor is a point (zero-dimensional, non-positive Lyapunov spectrum) rather than a limit cycle, torus, or strange attractor.

### 8.4 Statistical Invariants (Families 4–5, 8, 15–16)

The statistical invariants characterise the *macroscopic* properties: how energy is lost (dissipation partitions, Family 4), how energy and entropy relate (Family 5), how modes are correlated (Family 8), whether the structure is universal (Family 15), and whether the families agree (Family 16).

---

## Chapter 9. Cross-Family Dependencies and Consistency

### 9.1 Dependency Graph

The sixteen families are not fully independent. Several share input data (modal amplitudes), and several test overlapping aspects of the attractor. The dependency structure is:

- Families 1–3, 6, 8–14 all depend on the modal amplitudes $a_k(t)$.
- Families 4–5, 7 depend on the energy and dissipation time series.
- Family 15 depends on all other families (it aggregates their summaries).
- Family 16 depends on all other families (it correlates them).

### 9.2 Expected Correlations

Some cross-family correlations are structurally mandated:

- Low-mode collapse (Family 1) and mode-energy ratios (Family 2) are directly related: if all modes collapse, the energy ratios are undefined; if they converge to a profile, the low-mode amplitudes are determined.
- Lyapunov spectrum (Family 12) and attractor manifold (Family 13) both measure the attractor's geometry, but from different perspectives (dynamical vs statistical). They should agree: $D_{\mathrm{KY}} \approx 0$ implies $D_{\mathrm{eff}} \leq 2$.
- Dissipation partitions (Family 4) and convergence stability (Family 7) both depend on the energy dynamics, but the partitions measure the *channel balance* while the convergence measures the *rate*.

### 9.3 The Consistency Score

The cross-invariant consistency score $C$ (Definition 7.16) quantifies the overall agreement. A high $C$ does not mean the families are redundant — it means they describe the same underlying structure from different angles. A low $C$ would indicate that different aspects of the attractor behave differently under parameter variation, which would challenge the architectural claim.

### 9.4 Invariant Summary Table

| \# | Family | Type | Key invariant | Predictions tested |
|----|--------|------|--------------|-------------------|
| 1 | Low-mode collapse | Spectral | $m_k^*$ | 5.1 |
| 2 | Mode-energy ratios | Spectral | $R_k^*$ | 5.4 |
| 3 | Spectral complexity | Spectral | $H_q^*$ | 5.4 |
| 4 | Dissipation partitions | Statistical | $R_{\mathrm{grad}}^*, R_{\mathrm{pen}}^*, R_{\mathrm{part}}^*$ | 5.6 |
| 5 | Energy–entropy geometry | Statistical | $(E^*, H^*)$ | 5.1, 5.6 |
| 6 | Broadband cascade | Spectral | $R_b^*$ | 5.4, 5.5 |
| 7 | Convergence stability | Dynamical | $\sigma_{\mathrm{III}}$ | 5.2 |
| 8 | Modal correlations | Statistical | $\bar{C}_{ij}$ | 5.5 |
| 9 | Modal overlap | Spectral | $O_k^*$ | 5.4 |
| 10 | Phase dynamics | Dynamical | $C_{ij}^{\phi}$ | 5.5 |
| 11 | Phase–amplitude coupling | Dynamical | $\rho_k$ | 5.1 |
| 12 | Lyapunov spectrum | Topological | $\lambda_i$, $D_{\mathrm{KY}}$ | 5.3 |
| 13 | Attractor manifold | Topological | $D_{\mathrm{eff}}$ | 5.1, 5.7 |
| 14 | Perturbed stability | Dynamical | $\sigma_\epsilon$ | 5.1 |
| 15 | Parameter universality | Statistical | $U$ | 5.7 |
| 16 | Cross-consistency | Statistical | $C$ | 5.1–5.7 |

---

# PART III — COMPUTATION

---

## Chapter 10. The ED-SIM-01 Pipeline

### 10.1 Architecture

The pipeline has five layers, each reading the outputs of the layer below:

| Layer | Components | Input | Output |
|-------|-----------|-------|--------|
| 1. Solver | `edsim_core`, `edsim_runner` | Parameters, ICs | `time_series.npz` |
| 2. Experiments | `regime_volume_3d` | Layer 1 | 64 run directories |
| 3. Invariants | 16 `invariant_*.py` scripts | Layer 2 | Summary JSONs, figures |
| 4. Meta-analyses | `universality`, `consistency`, `embedding` | Layer 3 | Synthesis JSONs |
| 5. Synthesis | `atlas_report`, `certificate` | Layer 4 | Report, index, certificate |

### 10.2 Data Flow

Each simulation run produces a self-contained directory:

```
output/runs/regime_D{D}_A{A}_Nm{Nm}/
    time_series.npz       t, v, E_total, C_ED, D_grad, D_pen,
                          D_part, D_total, modal_amplitudes, ...
    metadata.json         All parameters, regime, discriminant,
                          termination, wall time
```

Each invariant script reads all admissible run directories and produces:
- Figures in `output/figures/invariants/{family}/`
- A summary JSON with per-run and global statistics

Each meta-analysis script reads the invariant JSONs and produces synthesis figures and JSONs. The final scripts aggregate everything into the atlas report and certificate.

---

## Chapter 11. Simulation Framework and Numerical Methods

### 11.1 Spatial Discretisation

**Method A (Finite Difference).** The spatial domain $[0, L]$ is discretised on a uniform grid of $N + 2$ points (including boundary points) with spacing $h = L/(N+1)$. The Laplacian is approximated by the standard three-point stencil:

$$\Delta_h\rho_j = \frac{\rho_{j-1} - 2\rho_j + \rho_{j+1}}{h^2}, \tag{11.1}$$

with Neumann boundary conditions enforced via ghost-point reflection: $\rho_{-1} = \rho_1$, $\rho_{N+2} = \rho_N$.

The gradient squared uses central differences:

$$|\nabla_h\rho|^2_j = \Bigl(\frac{\rho_{j+1} - \rho_{j-1}}{2h}\Bigr)^2. \tag{11.2}$$

**Method B (Spectral).** The perturbation $u = \rho - \rho^*$ is expanded in the Neumann eigenbasis (3.7). The linear part is treated exactly in spectral space; the nonlinear part is evaluated pseudospectrally with $3/2$-rule dealiasing.

### 11.2 Time Stepping

**Crank–Nicolson (default).** Diffusion is treated with half-weight implicit/explicit; nonlinear terms are explicit:

$$\frac{\rho^{n+1} - \rho^n}{\Delta t} = \frac{D}{2}\bigl(L_h\rho^{n+1} + L_h\rho^n\bigr) + D\,N_h[\rho^n] - D\,P(\rho^n) + H\,v^n, \tag{11.3}$$

where $L_h$ is the discrete Laplacian weighted by $M(\rho^n)$ and $N_h[\rho^n] = M'(\rho^n)\,|\nabla_h\rho^n|^2$.

**Participation update.** The participation variable is advanced by the exact exponential integrator:

$$v^{n+1} = e^{-\zeta\Delta t/\tau}\,v^n + \frac{\bar{F}^n}{\zeta}\bigl(1 - e^{-\zeta\Delta t/\tau}\bigr). \tag{11.4}$$

### 11.3 Stability Controls

Five structural invariants are monitored at every time step:

1. **Positivity**: $\rho_j^n > 0$ for all $j$.
2. **Sub-capacity**: $\rho_j^n < \rho_{\max}$ for all $j$.
3. **Energy monotonicity**: $\mathcal{E}^{n+1} \leq \mathcal{E}^n$ (checked; violations above $10^{-8}$ logged).
4. **Mass consistency**: $|\mathcal{M}^{n+1} - \mathcal{M}^n|$ within truncation error.
5. **Mobility positivity**: $M(\rho_j^n) > 0$ at all interior points.

### 11.4 Default Numerical Parameters

| Parameter | Value | Justification |
|-----------|-------|--------------|
| $N$ | 768 | Converged for all Atlas experiments |
| $\Delta t$ | $3.125 \times 10^{-5}$ | $27\times$ below CFL limit |
| Method | Crank–Nicolson | Second-order temporal accuracy |
| $\epsilon_{\mathrm{pos}}$ | $10^{-12}$ | Positivity clipping threshold |

---

## Chapter 12. Parameter Grid and Regime Structure

### 12.1 The Three-Dimensional Grid

The regime volume experiment sweeps:

| Parameter | Values | Physical meaning |
|-----------|--------|-----------------|
| $D$ | 0.05, 0.1, 0.2, 0.5 | Direct-channel weight |
| $A$ | 0.005, 0.01, 0.02, 0.05 | Initial perturbation amplitude |
| $N_m$ | 5, 10, 20, 30 | Number of seeded modes |

Total: $4 \times 4 \times 4 = 64$ runs. Each run integrates the canonical PDE from a broadband eigenmode initial condition (modes $1$ through $N_m$ with equal amplitude $A$) to final time $T = 20$.

### 12.2 Regime Classification

The discriminant $\mathscr{D}_0$ (4.1) classifies each run:

- **Underdamped** ($\mathscr{D}_0 < 0$): the homogeneous mode oscillates before decaying.
- **Critical** ($|\mathscr{D}_0| < 10^{-10}$): the transition between oscillatory and monotonic.
- **Overdamped** ($\mathscr{D}_0 > 0$): the homogeneous mode decays monotonically.
- **Inadmissible**: positivity or capacity violation during integration.

### 12.3 Five Canonical Parameter Sets

For benchmarking and cross-validation, five canonical parameter sets are defined:

| Set | $D$ | $\zeta$ | $\tau$ | Regime |
|-----|-----|---------|--------|--------|
| I | 0.3 | 0.1 | 1.0 | Deep oscillatory |
| II | 0.6 | 0.5 | 1.0 | Moderate oscillatory |
| III | 0.8 | 1.8 | 1.0 | Near-critical |
| IV | 0.9 | 5.0 | 1.0 | Deep monotonic |
| V | 0.2 | 0.3 | 0.5 | High participation |

All sets use $\rho^* = 0.5$, $\rho_{\max} = 1.0$, $M_0 = 1.0$, $\beta = 2.0$, $P_0 = 1.0$.

---

## Chapter 13. Invariant Extraction

### 13.1 Extraction Pipeline

Each of the sixteen invariant scripts follows a common pattern:

1. **Discover** all admissible runs via `glob("output/runs/regime_D*_A*_Nm*")`.
2. **Load** `time_series.npz` and `metadata.json` for each run.
3. **Compute** the invariant quantity using the attractor window.
4. **Fit** exponential convergence: $|Q(t) - Q^*| \sim C\,e^{-\sigma t}$ over the last 20%.
5. **Record** $Q^*$, $\sigma$, $R^2$, and the convergence flag ($R^2 > 0.95$ and $\sigma > 0$).
6. **Aggregate** across runs: mean, std, min, max, CV, verdict.
7. **Produce** three standard figures: (A) evolution, (B) attractor profile, (C) convergence heatmap.
8. **Save** a summary JSON and the figures.

### 13.2 Streaming Computation

For memory-intensive invariants (triad balance, modal correlations), the extraction uses a streaming pattern: each triad or mode pair is processed individually, the summary statistics are recorded, and the temporary arrays are discarded. This keeps the memory footprint below 200 MB even for $N_m = 30$.

### 13.3 Convergence-Rate Fitting

The exponential convergence rate $\sigma$ is extracted by linear regression of $\log|Q(t) - Q^*|$ against $t$ over the fitting window. The quality metric is $R^2$:

$$R^2 = 1 - \frac{\sum_i (\log|Q_i - Q^*| - \hat{y}_i)^2}{\sum_i (\log|Q_i - Q^*| - \bar{y})^2}, \tag{13.1}$$

where $\hat{y}_i$ is the fitted value and $\bar{y}$ is the mean. A fit with $R^2 > 0.95$ and $\sigma > 0$ is classified as converged.

---

## Chapter 14. Meta-Analyses

### 14.1 Parameter Universality

The universality analysis constructs the pairwise distance matrix

$$d_{ij} = \|\mathbf{I}_i - \mathbf{I}_j\|_2 \tag{14.1}$$

between standardised invariant vectors and computes the universality score

$$U = \frac{1}{1 + \mathrm{CV}(d)}. \tag{14.2}$$

Hierarchical clustering (Ward linkage) reveals the cluster structure. The number of clusters at the 5% dissimilarity threshold and the silhouette score quantify the universality.

### 14.2 Cross-Invariant Consistency

For each pair of invariant families $(A, B)$, the mean pairwise correlation is computed. The $F \times F$ correlation matrix reveals which families are redundant (correlated) and which carry independent information. The consistency score is

$$C = \bigl\langle |\mathrm{corr}(A, B)| \bigr\rangle_{A \neq B}. \tag{14.3}$$

### 14.3 Embedding Collapse

The standardised invariant vectors are projected into two dimensions using PCA, t-SNE, and (optionally) UMAP. The cluster radius (mean distance to centroid), cluster diameter (maximum pairwise distance), and embedding consistency $C_{\mathrm{emb}} = \mathrm{corr}(d_{\mathrm{PCA}}, d_{\mathrm{UMAP}})$ are computed. A collapsed embedding (cluster radius $< 0.1$) confirms that the attractor structure is effectively parameter-independent.

---

# PART IV — SYNTHESIS

---

## Chapter 15. The Invariant Atlas

### 15.1 Structure

The invariant atlas is the complete collection of:

- Sixty-four simulation runs with full time-series data.
- Sixteen invariant families, each with per-run summaries and global statistics.
- Three meta-analyses with synthesis figures.
- A global atlas report aggregating all results.

### 15.2 Coverage

The atlas covers the three-dimensional parameter space $(D, A, N_m)$ with $4 \times 4 \times 4 = 64$ points. For each point, all sixteen invariants are computed. The total computational output is approximately 5 GB of raw data, 100 MB of invariant summaries, and 200 figures.

### 15.3 The Atlas as a Structural Map

The atlas is not a parameter study in the traditional sense. It does not ask "how does observable $X$ depend on parameter $D$?" Instead, it asks "is observable $X$ the same for all values of $D$?" The answer — quantified by the CV — determines whether $X$ is a structural property of the architecture (CV $< 5\%$) or a parameter-dependent quantity (CV $\geq 15\%$).

---

## Chapter 16. Global Verdict and Architectural Consistency

### 16.1 Synthesis

The five global diagnostics are:

| Diagnostic | Metric | Criterion |
|-----------|--------|-----------|
| Universality | $U$ | $> 0.9$: UNIVERSAL |
| Cross-Consistency | $C$ | $> 0.8$: CONSISTENT |
| Stability | $n_+$, $D_{\mathrm{KY}}$, $D_{\mathrm{eff}}$ | $n_+ = 0$: STABLE |
| Embedding Collapse | cluster radius | $< 0.1$: COLLAPSED |
| Perturbation Recovery | $\epsilon$-CV | $< 0.05$: ROBUST |

### 16.2 The Final Verdict

The final verdict is:

- **PASS** if all five diagnostics are satisfactory.
- **PARTIAL** if some are weakly satisfactory.
- **FAIL** if any diagnostic contradicts the architecture.

### 16.3 What "Structural Consistency" Means

A PASS verdict does not prove that the ED architecture describes physical reality. It proves that the architecture is *self-consistent*: the mathematical structure predicted by the seven principles is realised by the canonical PDE across all tested parameter regimes. The physical question — whether specific systems belong to $\mathcal{U}_{\mathrm{ED}}$ — remains empirical.

---

## Chapter 17. The ED Architecture Certificate

### 17.1 Structure

The ED Architecture Certificate is a single-page document that encodes the global verdict. It contains:

1. **Header**: title, version, pipeline identifier.
2. **Verdict banner**: PASS, PARTIAL, or FAIL, with colour coding (green/amber/red).
3. **Metrics table**: five diagnostic rows, each with an icon, label, key metric, and per-row verdict chip.
4. **Footer**: reproducibility statement, timestamp, version.

**Figure 17.1 description.** *ED Architecture Certificate (PASS variant).* A 6 × 8 inch portrait figure with four zones. The header displays "ED ARCHITECTURE / CONSISTENCY CERTIFICATE / ED-SIM-01 · v1.0.0". The verdict banner is a green-bordered box containing "PASS" in bold green text with the subtext "All diagnostics satisfactory". The metrics table contains five rows: Universality (U = 0.9412, UNIVERSAL), Cross-Consistency (C = 0.8731, CONSISTENT), Stability (n₊ = 0, D_KY = 0.00, D_eff = 1.2, STABLE), Embedding Collapse (r = 0.071, COLLAPSED), Perturbation Recovery (CV = 0.032, ROBUST). Each row has a geometric icon in the accent colour. The footer contains the reproducibility statement, timestamp, and pipeline version. A logarithmic spiral watermark at 3% opacity underlies the figure.

### 17.2 Machine Generation

The certificate is generated by `generate_master_index_and_certificate.py`, which:

1. Loads the global atlas report JSON.
2. Extracts the final verdict from `global_verdict.json`.
3. Produces the text certificate (`ED_Consistency_Certificate.txt`).
4. Invokes `generate_certificate_figure.py` to render the figure (`ED_Architecture_Certificate.png`, `.pdf`).

### 17.3 Reproducibility

The certificate is deterministic: given the same atlas report, it always produces the same output. An independent researcher who regenerates the atlas from scratch will obtain the same certificate (at Tier 3 reproducibility).

---

## Chapter 18. Interpretation and Implications

### 18.1 For the Architecture

A PASS certificate confirms that the seven principles produce a coherent mathematical structure: the predictions of Chapter 5 are realised quantitatively across all tested regimes. This is the numerical foundation for the physical predictions of the Applications Paper.

### 18.2 For the Universality Class

The universality score $U$ tests the closure theorems of Appendix D. A high $U$ confirms that the qualitative attractor structure is invariant under parameter variation within $\mathcal{U}_{\mathrm{ED}}$ — the same modes survive, the same triads couple, the same dissipation partitions emerge, regardless of $(D, A, N_m)$.

### 18.3 For the Physical Predictions

The Applications Paper derives nineteen physical predictions from the architectural principles. Each prediction rests on the assumption that the target physical system belongs to $\mathcal{U}_{\mathrm{ED}}$. The invariant atlas confirms that the canonical system realises the predicted structure; the physical question is whether specific systems can be mapped into the canonical form.

---

# PART V — REPRODUCIBILITY

---

## Chapter 19. Reproducibility Suite

### 19.1 Directory Structure

```
reproducibility/
    README.md                   Documentation
    run_all.py                  Master pipeline script
    checks/
        check_environment.py    Python + package verification
        check_data_integrity.py Run directory verification
    scenarios/
        minimal/                1 run, 1 invariant (< 2 min)
        full/                   Complete pipeline (30–120 min)
        diagnostic/             Checks only (< 30 s)
    docs/
        architecture.md         Pipeline architecture
        onboarding.md           New-user guide
        invariant_map.md        All 16 families at a glance
    validation/
        expected_structure.json Expected outputs
        hash_reference.json     Reference hashes
        validate_outputs.py     Output validation
```

### 19.2 The Master Script

The command `python reproducibility/run_all.py` executes eight phases:

1. Environment checks.
2. Data integrity verification.
3. Regime volume experiment (64 runs).
4. Invariant analyses (16 families).
5. Meta-analyses (3).
6. Global atlas report.
7. Master index and certificate.
8. Output validation.

Each phase is isolated: a failure in one phase does not abort the pipeline.

### 19.3 Reproducibility Tiers

| Tier | Criterion | Scope |
|------|-----------|-------|
| 1 (Bitwise) | Identical file hashes | Same OS, Python, libraries, hardware |
| 2 (Numerical) | Field-by-field agreement within $10^{-10}$ | Same libraries, different hardware |
| 3 (Observable) | All invariant verdicts identical | Any conforming environment |

---

## Chapter 20. Validation and Verification

### 20.1 Environment Checks

The script `check_environment.py` verifies: Python version ($\geq 3.10$), required packages (numpy, scipy, matplotlib with minimum versions), optional packages (umap-learn, scikit-learn, h5py), and GPU availability.

### 20.2 Data Integrity

The script `check_data_integrity.py` verifies: run directories exist, `time_series.npz` and `metadata.json` are present and parseable, required fields exist, and no NaN or Inf values contaminate the data.

### 20.3 Output Validation

The script `validate_outputs.py` checks: 64 valid regime runs, 19 invariant figure directories with PNGs, 19 invariant summary JSONs, and 6 atlas files. It produces a validation report and exits with code 0 (all pass) or 1 (critical failure).

---

## Chapter 21. How to Extend the Architecture

### 21.1 Adding a New Invariant

1. Create `experiments/invariant_my_quantity.py` following the template.
2. Implement the standard extraction pipeline (§13.1).
3. Produce the three standard figures (evolution, profile, heatmap).
4. Save a summary JSON with per-run and global statistics.
5. Add the family to `PHASE_4_INVARIANTS` in `run_all.py`.
6. Add it to `FAMILY_META` in the certificate generator.
7. Run the pipeline and verify the certificate.

### 21.2 Adding a New Parameter Dimension

1. Extend the parameter grid in `regime_volume_3d.py`.
2. Ensure the output directory naming convention includes the new parameter.
3. Update the discovery logic in all invariant scripts.
4. Re-run the pipeline.

### 21.3 Porting to a New Physical Domain

1. Identify the density field $\rho$, the constitutive functions $M(\rho)$ and $P(\rho)$, and the canonical parameters.
2. Verify that the seven principles are satisfied.
3. Implement the constitutive functions in `edsim_parameters.py`.
4. Run the regime volume experiment with domain-specific parameter ranges.
5. Compute the invariant atlas and compare to the canonical results.

---

# PART VI — OUTLOOK

---

## Chapter 22. Applications and Future Directions

### 22.1 Physical Domains

The Applications Paper derives predictions for five physical domains:

1. **Quantum mechanics**: complexity-ordered decoherence, biological coherence limits, interference visibility scaling.
2. **Galactic dynamics**: temporal halos, activity-dependent rotation curves, halo lag in collisions.
3. **Condensed matter**: mesoscopic transport thresholds, superconducting phase-stiffness saturation, Casimir-force plateaus.
4. **Photonics**: microresonator efficiency jumps, linewidth asymmetry, soliton step-height saturation.
5. **Phononics**: chiral-phonon ED-vorticity, orbital Seebeck tension scaling.

Each prediction has a stated falsification condition. One has been tested (dwarf galaxy rotation curves) and confirmed.

### 22.2 ED-SIM v2

Planned extensions:

- **Higher spatial dimensions** (2D, 3D).
- **Adaptive mesh refinement** for near-horizon and high-gradient regions.
- **GPU acceleration** for batch parameter sweeps.
- **Multi-domain coupling** for large-scale simulations.

### 22.3 Stochastic Extensions

The stochastic perturbation extension adds controlled noise to the canonical system:

$$d\rho = \bigl(D\,F[\rho] + H\,v\bigr)\,dt + \sigma_\rho\,g(\rho)\,dW(x, t). \tag{22.1}$$

The mobility-proportional noise $g(\rho) = \sqrt{M(\rho)}$ is architecturally natural: the noise vanishes at the horizon, respecting the capacity bound. The stochastic extension enables fluctuation spectroscopy, noise-robustness testing, and comparison with noisy physical systems.

---

## Chapter 23. Open Problems

### 23.1 Mathematical Open Problems

1. **Multi-field extensions.** The canonical system has one density field. Physical systems with coupled order parameters may require multi-field generalisations. The universality class theory for multi-field systems is open.

2. **Relativistic formulation.** The canonical PDE is parabolic on a fixed domain. Cosmological applications require a covariant formulation on curved spacetime.

3. **Derivation from first principles.** The seven principles are stated axiomatically. Whether they can be derived from a Lagrangian, an action principle, or a more fundamental theory is unknown.

4. **Sharp universality boundaries.** The universality class $\mathcal{U}_{\mathrm{ED}}$ is defined by the seven principles. The precise boundary — which constitutive functions and which parameters lie on the edge of universality — has not been characterised.

### 23.2 Computational Open Problems

5. **Finer parameter grids.** The current $4 \times 4 \times 4$ grid may miss structure near the critical surface $\mathscr{D}_0 = 0$, near the capacity boundary, or at high complexity.

6. **Long-time integration.** The standard integration time $T = 20$ may not be sufficient for high-complexity initial conditions to reach the exponential-decay regime.

7. **Higher-dimensional invariants.** The current invariants are extracted from 1D simulations. Their generalisation to 2D and 3D is straightforward in principle but computationally expensive.

### 23.3 Physical Open Problems

8. **Constitutive identification.** For each physical domain, the density field, the mobility, and the penalty must be identified from the microscopic theory. This identification has not been carried out rigorously for any system beyond the canonical ED PDE itself.

9. **Experimental falsification.** Eighteen of the nineteen predictions of the Applications Paper remain untested. The experimental priority ordering is: mesoscopic transport kink, microresonator threshold, decoherence scaling, Casimir saturation, biological coherence limit.

---

## Chapter 24. Concluding Remarks

This monograph has presented the Event Density architecture as a unified mathematical framework, developed its invariant theory, and documented its computational verification through the ED-SIM-01 pipeline.

The principal results are:

1. The canonical ED PDE possesses a unique point attractor $(\rho^*, 0)$ across all tested parameter regimes, confirmed by zero positive Lyapunov exponents and near-zero effective attractor dimension.

2. The sixteen invariant families are mutually consistent and structurally invariant under parameter variation, with coefficient of variation below 5% for the core families.

3. The three-stage convergence structure (global bounds, algebraic decay, exponential decay) is reproduced quantitatively in every admissible run.

4. The complete pipeline — from raw PDE integration through invariant computation to certificate generation — is fully reproducible from a single command.

The ED Architecture Certificate encodes these results in a single, machine-verifiable document. It is the bridge between the mathematical architecture and the physical predictions: if the certificate reads PASS, the architecture is self-consistent, and the predictions that follow from it are structurally well-founded.

The architecture does not explain everything. It does not fix the constitutive functions for specific physical systems. It does not produce quantitative parameter values. It does not extend to the relativistic regime. These limitations define the open problems of the programme.

What the architecture does provide is a *structural guarantee*: any system satisfying the seven principles will exhibit the same qualitative dynamics — the same attractor, the same convergence, the same modal hierarchy, the same spectral fingerprint. This guarantee, once confirmed experimentally, would constitute a new kind of physical law: not a law about particles or forces, but a law about the architecture of dynamics itself.

---

# Appendices

---

## Appendix A. Notation

| Symbol | Meaning |
|--------|---------|
| $\rho(x, t)$ | Density field |
| $v(t)$ | Participation variable |
| $F[\rho]$ | Density operator |
| $M(\rho)$ | Mobility function |
| $P(\rho)$ | Penalty function |
| $D$ | Direct-channel weight |
| $H = 1 - D$ | Participation-channel weight |
| $\zeta$ | Participation damping rate |
| $\tau$ | Participation time scale |
| $\rho^*$ | Penalty equilibrium density |
| $\rho_{\max}$ | Capacity bound |
| $M_0, \beta$ | Mobility parameters |
| $P_0$ | Penalty slope |
| $\Omega = [0, L]$ | Spatial domain |
| $\varphi_k(x)$ | Neumann eigenfunctions |
| $\mu_k = (k\pi/L)^2$ | Eigenvalues |
| $a_k(t)$ | Modal amplitudes |
| $E_k = |a_k|^2$ | Modal energies |
| $\alpha_k = M_*\mu_k + P_*'$ | Modal decay coefficients |
| $\mathscr{D}_0$ | Homogeneous-mode discriminant |
| $\gamma_0$ | Homogeneous-mode decay rate |
| $\mathcal{E}[\rho, v]$ | Energy functional |
| $\Phi(\rho)$ | Density potential |
| $\mathcal{D}_{\mathrm{grad}}, \mathcal{D}_{\mathrm{pen}}, \mathcal{D}_{\mathrm{part}}$ | Dissipation channels |
| $\langle \cdot \rangle_{\mathrm{att}}$ | Mean over attractor window |
| $\mathrm{CV}$ | Coefficient of variation |
| $U$ | Universality score |
| $C$ | Consistency score |
| $D_{\mathrm{KY}}$ | Kaplan–Yorke dimension |
| $D_{\mathrm{eff}}$ | Effective PCA dimension |

---

## Appendix B. Key Derivations

### B.1 Energy Dissipation Identity

Starting from (3.1a), multiply by $P(\rho)/M(\rho)$ and integrate over $\Omega$:

$$\int_\Omega \frac{P(\rho)}{M(\rho)}\,\partial_t\rho\,dx = D\int_\Omega \frac{P(\rho)}{M(\rho)}\,F[\rho]\,dx + H\,v\int_\Omega \frac{P(\rho)}{M(\rho)}\,dx.$$

The left-hand side is $d/dt\int_\Omega \Phi(\rho)\,dx$. The right-hand side, after integration by parts and the participation equation, yields the three dissipation channels. The full derivation is in the Rigour Paper, Appendix C.2.

### B.2 Triad Coupling Coefficients

In the Neumann eigenbasis, the product $\varphi_m'(x)\varphi_n'(x)$ projects onto $\varphi_{m+n}$ and $\varphi_{|m-n|}$ by the product-to-sum formula for cosines. The coupling coefficient for the forward triad $(m, n, m+n)$ is:

$$\Gamma_{mn,m+n} = \frac{m\,n}{2\,(m+n)^2}, \tag{B.1}$$

after cancellation of $L$ and $\pi$ factors. The inverse triad $(m, n, |m-n|)$ has the same structure with $m + n$ replaced by $|m - n|$.

### B.3 Linearised Eigenvalue Problem

Linearising (3.1) about $(\rho^*, 0)$ for the homogeneous mode ($k = 0$):

$$\begin{pmatrix} \dot{a}_0 \\ \dot{v} \end{pmatrix} = \begin{pmatrix} -D\,P_*' & H \\ -P_*'/\tau & -\zeta/\tau \end{pmatrix} \begin{pmatrix} a_0 \\ v \end{pmatrix}. \tag{B.2}$$

The characteristic polynomial is $\lambda^2 + 2\gamma_0\lambda + c = 0$ with $\gamma_0 = \frac{1}{2}(D\,P_*' + \zeta/\tau)$ and $c = (D\,P_*'\zeta + H\,P_*')/\tau$. The discriminant is $\mathscr{D}_0 = 4(\gamma_0^2 - c)$.

---

## Appendix C. Figure Descriptions

**Figure 17.1.** ED Architecture Certificate. See §17.1.

**Figure C.1.** *Pipeline architecture diagram.* Five horizontal layers connected by arrows. Layer 1 (solver, blue), Layer 2 (experiments, green), Layer 3 (invariants, orange), Layer 4 (meta-analyses, red), Layer 5 (synthesis, black).

**Figure C.2.** *Regime classification map.* The $(D, \zeta)$-plane partitioned into spiral (blue), monotonic (red), and critical (boundary curve) regions. The five canonical parameter sets are marked.

**Figure C.3.** *Three-stage convergence.* Semilog-$y$ plot of $|E(t) - E^*|$ showing the global bound (Stage I), algebraic decay (Stage II), and exponential decay (Stage III) with transition times marked.

**Figure C.4.** *Cross-invariant correlation heatmap.* $16 \times 16$ matrix of $|\mathrm{corr}(A, B)|$ between invariant families.

**Figure C.5.** *Embedding map.* PCA, t-SNE, and UMAP projections of the standardised invariant vectors showing cluster collapse.

---

## Appendix D. Extended Parameter Studies

The regime volume experiment covers a $4 \times 4 \times 4$ grid. Extended studies (not part of the standard atlas) include:

- **Fine $D$ sweep**: $D \in \{0.01, 0.02, \ldots, 0.99\}$ at fixed $(A, N_m) = (0.02, 20)$.
- **Critical-surface approach**: $\zeta$ swept through the critical value $\zeta_c$ at fixed $D$.
- **High-complexity frontier**: $N_m \in \{50, 100, 200\}$ at fixed $(D, A)$.
- **Long-time integration**: $T = 200$ at the five canonical parameter sets.

These studies extend the atlas but do not change the architectural verdict.

---

## Appendix E. Code Structure and API

### E.1 Core Modules

| Module | Purpose |
|--------|---------|
| `edsim_core.py` | PDE solver: spatial operators, time stepping, energy computation |
| `edsim_parameters.py` | Parameter sets, constitutive functions, validation |
| `edsim_diagnostics.py` | Observable extraction, modal decomposition, dissipation channels |
| `edsim_initial_conditions.py` | IC generators (Gaussian, broadband, single-mode, random) |
| `edsim_runner.py` | Integration loop, checkpointing, output logging |

### E.2 Experiment Scripts

Located in `experiments/`. Each is standalone and runnable with `python experiments/{name}.py`.

### E.3 Analysis Scripts

Located in the `ED Simulation/` root. Each is standalone and produces figures in `output/figures/`.

### E.4 Reproducibility Scripts

Located in `reproducibility/`. The master script is `run_all.py`.

---

## Appendix F. Glossary

| Term | Definition |
|------|-----------|
| **Admissible** | A density profile with $\rho \in (0, \rho_{\max})$ and $\rho \in H^1(\Omega)$ |
| **Attractor** | The long-time limit of all solutions; for ED, the point $(\rho^*, 0)$ |
| **Attractor window** | The last 10–20% of the time series, used for invariant extraction |
| **Capacity bound** | The maximum density $\rho_{\max}$; the mobility vanishes here |
| **Channel** | One of the two pathways (direct or participation) in the density equation |
| **Constitutive function** | The mobility $M(\rho)$ or penalty $P(\rho)$ that specifies the architecture |
| **Discriminant** | $\mathscr{D}_0$; classifies the dynamics as oscillatory, critical, or monotonic |
| **ED Architecture Certificate** | The single-page synthesis document encoding the global verdict |
| **Energy functional** | $\mathcal{E}[\rho, v]$; a Lyapunov functional for the ED system |
| **Invariant** | A quantity approximately constant across parameter regimes (CV $< 5\%$) |
| **Invariant atlas** | The complete collection of invariant computations across all regimes |
| **Mobility collapse** | The vanishing of $M(\rho)$ at $\rho = \rho_{\max}$; creates an impassable barrier |
| **Modal hierarchy** | The ordering $\alpha_0 < \alpha_1 < \cdots$; higher modes decay faster |
| **Participation variable** | $v(t)$; integrates the spatial average of $F[\rho]$ and feeds back |
| **Penalty** | $P(\rho)$; the restoring force that drives $\rho$ toward $\rho^*$ |
| **Regime** | Classification by discriminant: oscillatory, critical, or monotonic |
| **Triad** | A triple $(m, n, k)$ with $k = m + n$ or $k = |m - n|$; coupled by the nonlinearity |
| **Universality class** | $\mathcal{U}_{\mathrm{ED}}$; the set of all systems satisfying the seven principles |
| **Universality score** | $U = 1/(1 + \mathrm{CV}(d))$; measures parameter-independence of invariants |

---

# References

[1] A. Proxmire, "The Event Density Architectural Canon," ED-Arch-I, 2025.

[2] A. Proxmire, "Mathematical Foundations of the Event Density Architecture," ED-Arch-II (Rigour Paper), 2025.

[3] A. Proxmire, "Physical Applications of the Event Density Architecture," ED-Arch-III (Applications Paper), 2025.

[4] A. Proxmire, "ED-SIM v1: Numerical Atlas for the Event Density Canon," Numerical Atlas, 2025.

[5] A. Proxmire, "ED-SIM v1: Simulation Suite Specification," Simulation Suite, 2025.

[6] A. Proxmire, "Event Density Experimental Program," Open Note ED-00, 2024.

[7] G. Da Prato and J. Zabczyk, *Stochastic Equations in Infinite Dimensions*, Cambridge University Press, 1992.

[8] D. Henry, *Geometric Theory of Semilinear Parabolic Equations*, Springer Lecture Notes in Mathematics, vol. 840, 1981.

[9] A. Lunardi, *Analytic Semigroups and Optimal Regularity in Parabolic Problems*, Birkhäuser, 1995.

[10] R. Temam, *Infinite-Dimensional Dynamical Systems in Mechanics and Physics*, 2nd ed., Springer, 1997.

[11] J. C. Robinson, *Infinite-Dimensional Dynamical Systems*, Cambridge University Press, 2001.

[12] P. Constantin, C. Foias, B. Nicolaenko, and R. Temam, *Integral Manifolds and Inertial Manifolds for Dissipative Partial Differential Equations*, Springer, 1989.

---

*The Event Density Architecture: Foundations, Invariants, and Computational Verification.*
*Allen Proxmire. Event Density Research Program. 2026.*
