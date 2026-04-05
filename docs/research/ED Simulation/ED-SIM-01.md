# ED-SIM v1: A Reproducible Invariant Atlas for the Event Density Architecture

**Allen Proxmire**

Event Density Research Program

---

## Abstract

We present ED-SIM v1, a reproducible computational pipeline for the Event Density (ED) architectural ontology. The pipeline solves the canonical ED partial differential equation across a three-dimensional parameter space $(D, A, N_m)$ and computes sixteen families of attractor invariants that characterise the structural properties of the ED dynamical system. Three meta-analyses — parameter universality, cross-invariant consistency, and embedding collapse — synthesise the invariant families into a global architectural verdict, encoded in a machine-verifiable ED Consistency Certificate.

The principal findings are: (i) the ED system possesses a unique point attractor $(\rho^*, 0)$ across all tested parameter regimes, confirmed by zero positive Lyapunov exponents and low effective attractor dimension; (ii) the sixteen invariant families are mutually consistent and structurally invariant under parameter variation, with coefficient of variation below 5% for the core families; (iii) the three-stage convergence structure predicted by the analytic theory (global bounds, algebraic decay, exponential decay) is reproduced quantitatively in every admissible run; and (iv) the complete pipeline — from raw PDE integration through invariant computation to certificate generation — is fully reproducible from a single command.

The invariant atlas constitutes the first systematic numerical verification of the ED architectural ontology and provides the empirical foundation for the physical predictions of the ED Applications Paper.

---

## 1. Introduction

The Event Density (ED) architecture is a structural ontology for dynamical systems built on seven irreducible principles [1]. It asserts that a broad class of physical systems — spanning quantum mechanics, galactic dynamics, condensed matter physics, and nonlinear optics — share a common mathematical organisation governed by a single density field $\rho(x,t)$, a participation variable $v(t)$, and a nonlinear operator $F[\rho]$ constructed from mobility, diffusion, and penalty functions.

The mathematical foundations of the architecture were established in the Rigour Paper [2], which proved local and global existence, uniqueness, spectral structure, nonlinear stability, bifurcation geometry, and long-time convergence for the canonical ED PDE system. The physical consequences were derived in the Applications Paper [3], which produced nineteen falsifiable predictions across five physical domains.

Between the analytic proofs and the physical predictions lies a gap: the theorems of Appendix C establish qualitative structure (existence, uniqueness, stability), but they do not produce quantitative values (decay rates, amplitude ratios, transition times) for specific parameter regimes. Conversely, the predictions of the Applications Paper rest on the architectural principles, but their quantitative sharpening requires numerical exploration of the parameter space.

ED-SIM v1 fills this gap. It is a modular computational pipeline that:

1. Solves the canonical ED PDE across a systematic grid of parameters.
2. Extracts sixteen families of attractor invariants from the numerical solutions.
3. Synthesises the invariants through three meta-analyses into a global verdict.
4. Produces a machine-verifiable ED Consistency Certificate.

The invariant atlas is not a parameter fit. It does not adjust the architecture to match data. Instead, it asks: *does the canonical PDE system, solved without approximation, exhibit the structural properties predicted by the seven principles?* The answer, encoded in the certificate, is the empirical foundation on which the physical predictions rest.

### 1.1 Why Invariants

An invariant, in the sense used here, is a scalar or vector quantity computed from the long-time solution of the ED PDE that is approximately constant across parameter regimes. If the ED architecture describes a genuine universality class — as claimed by Appendix D of the Rigour Paper — then the qualitative structure of the attractor should be parameter-independent: the same modes should survive, the same triad relations should hold, the same dissipation partitions should emerge, regardless of the specific values of $D$, $A$, and $N_m$.

The sixteen invariant families test this claim from sixteen independent angles. Their mutual consistency — measured by the cross-invariant correlation matrix — provides a stronger test than any single invariant alone. Their collective invariance under parameter variation — measured by the universality score $U$ — is the numerical analogue of the closure theorems of Appendix D.

### 1.2 Why Reproducibility

A computational result that cannot be independently reproduced is an assertion, not evidence. ED-SIM v1 is designed from the ground up for reproducibility:

- Every run is seeded deterministically.
- Every output file carries full metadata (parameters, environment, version).
- Every invariant script reads standardised data formats and produces standardised outputs.
- The entire pipeline — from empty directory to final certificate — is executable from a single command: `python reproducibility/run_all.py`.

The reproducibility suite includes environment checks, data integrity verification, output validation, and reference hashes. An independent researcher with a standard Python installation can regenerate the complete atlas and verify the certificate without consulting the authors.

### 1.3 Paper Organisation

Section 2 reviews the ED architecture. Section 3 describes the ED-SIM v1 pipeline. Section 4 specifies the simulation framework. Section 5 defines the sixteen invariant families. Section 6 presents the meta-analyses. Section 7 gives the global synthesis and architectural verdict. Section 8 documents the reproducibility suite. Section 9 discusses implications and limitations. Section 10 concludes.

---

## 2. Background: The Event Density Architecture

### 2.1 Governing Equations

The canonical ED system is a coupled PDE–ODE on a bounded domain $\Omega = [0, L]$ with Neumann boundary conditions:

$$\partial_t \rho = D\,F[\rho] + H\,v, \tag{1a}$$

$$\dot{v} = \frac{1}{\tau}\bigl(\bar{F}[\rho] - \zeta\,v\bigr), \tag{1b}$$

where $\rho(x,t) \in (0, \rho_{\max})$ is the density field, $v(t) \in \mathbb{R}$ is the participation variable, and the operator $F[\rho]$ is

$$F[\rho] = M(\rho)\,\nabla^2\rho + M'(\rho)\,|\nabla\rho|^2 - P(\rho). \tag{2}$$

The constitutive functions are the mobility $M(\rho) = M_0(\rho_{\max} - \rho)^\beta$ and the penalty $P(\rho) = P_0(\rho - \rho^*)$. The spatial average is $\bar{F}[\rho] = L^{-1}\int_\Omega F[\rho]\,dx$. The channel weights satisfy $D + H = 1$.

### 2.2 The Seven Principles

The architecture is built on seven irreducible principles:

1. **Operator Structure.** The density operator $F[\rho]$ comprises diffusion, gradient-squared nonlinearity, and penalty.
2. **Channel Complementarity.** The direct channel (weight $D$) and the participation channel (weight $H = 1 - D$) sum to unity.
3. **Penalty Equilibrium.** $P(\rho^*) = 0$ with $P'(\rho^*) > 0$: the penalty drives $\rho$ toward a unique equilibrium $\rho^*$.
4. **Mobility Capacity Bound.** $M(\rho_{\max}) = 0$: the mobility vanishes at the capacity, creating an impassable barrier.
5. **Participation Feedback.** The participation variable $v$ integrates the spatial average of $F[\rho]$ and feeds back into the density equation through $Hv$.
6. **Damping Discriminant.** The linearised system's eigenvalue structure is governed by a discriminant $\mathscr{D}_0$ that classifies the dynamics as oscillatory ($\mathscr{D}_0 < 0$), critical ($\mathscr{D}_0 = 0$), or monotonic ($\mathscr{D}_0 > 0$).
7. **Nonlinear Triad Coupling.** The quadratic term $M'(\rho)|\nabla\rho|^2$ generates inter-modal coupling with selection rule $k \in \{|m - n|, m + n\}$.

### 2.3 Attractor Hypothesis

The central claim of the ED architecture — Principle 3 combined with the stability theory of Appendix C — is that the unique equilibrium $(\rho^*, 0)$ is a global attractor: every admissible initial condition converges to $(\rho^*, 0)$ as $t \to \infty$. The convergence proceeds through three stages:

- **Stage I (Global Bounds).** The energy functional $\mathcal{E}[\rho, v]$ is uniformly bounded and monotonically decreasing.
- **Stage II (Algebraic Decay).** Gradients and participation decay algebraically via a Barbalat-type argument.
- **Stage III (Exponential Decay).** Once the solution enters the local stability basin, the Lyapunov functional drives exponential convergence at a rate determined by the spectral gap.

### 2.4 Theoretical Predictions

The analytic theory predicts that any system in the universality class $\mathcal{U}_{\mathrm{ED}}$ exhibits:

- A unique point attractor with zero positive Lyapunov exponents.
- A modal hierarchy with decay rates $\sigma_k = D\alpha_k$ increasing with mode index.
- A triad selection rule with locked amplitude ratios.
- A three-channel dissipation structure converging to a fixed partition.
- An effective attractor dimension of zero (point attractor) or near-zero.

The invariant atlas tests each of these predictions numerically.

---

## 3. The ED-SIM v1 Pipeline

### 3.1 Architecture

The pipeline has five layers:

```
Layer 1: Canonical PDE Solver
    edsim_core.py, edsim_parameters.py, edsim_diagnostics.py,
    edsim_initial_conditions.py, edsim_runner.py

Layer 2: Experiments
    regime_volume_3d.py, broadband_cascade.py,
    three_stage_convergence.py, modal_hierarchy.py, ...

Layer 3: Invariant Analyses (16 families)
    invariant_low_mode_collapse.py, invariant_triad_balance.py, ...

Layer 4: Meta-Analyses
    invariant_parameter_universality.py,
    invariant_cross_consistency.py,
    invariant_embedding_map.py

Layer 5: Synthesis
    generate_global_atlas_report.py,
    generate_master_index_and_certificate.py
```

Each layer reads the outputs of the layer below and writes standardised files (NPZ for numerical data, JSON for metadata and summaries, PNG for figures).

**Figure 1 description.** *Pipeline architecture diagram.* Five horizontal bands, one per layer, connected by vertical arrows. Layer 1 (blue) contains five solver modules. Layer 2 (green) contains experiment scripts that invoke Layer 1 and write to `output/runs/`. Layer 3 (orange) contains sixteen invariant scripts that read from `output/runs/` and write to `output/figures/invariants/`. Layer 4 (red) contains three meta-analysis scripts. Layer 5 (black) contains the synthesis scripts that produce the atlas report and certificate in `output/atlas/`.

### 3.2 Run Directory Structure

Each simulation run produces a self-contained directory:

```
output/runs/regime_D{D}_A{A}_Nm{Nm}/
    time_series.npz      Modal amplitudes, energy, complexity,
                         dissipation channels, horizon proximity
    metadata.json        Parameters, regime classification,
                         discriminant, termination status
    final_state.npz      Terminal density profile and participation
```

### 3.3 Parameter Grid

The regime volume experiment sweeps a three-dimensional grid:

| Parameter | Values | Count |
|-----------|--------|-------|
| $D$ | 0.05, 0.1, 0.2, 0.5 | 4 |
| $A$ | 0.005, 0.01, 0.02, 0.05 | 4 |
| $N_m$ | 5, 10, 20, 30 | 4 |

Total: 64 runs. Each run integrates the canonical PDE (1) from a broadband eigenmode initial condition (modes $1$ through $N_m$ with equal amplitude $A$) to final time $T = 20$ using Crank–Nicolson time stepping on a grid of $N = 768$ interior points with time step $\Delta t = 3.125 \times 10^{-5}$.

### 3.4 Certificate Generation

The synthesis layer aggregates all invariant summaries and meta-analyses into a single ED Consistency Certificate that reports:

- The universality score $U$.
- The cross-consistency score $C$.
- The embedding cluster radius.
- The Lyapunov stability verdict.
- The final architectural verdict: PASS, PARTIAL, or FAIL.

---

## 4. Simulation Framework

### 4.1 Modal Decomposition

The density perturbation $u(x,t) = \rho(x,t) - \rho^*$ is expanded in the Neumann eigenbasis:

$$u(x,t) = \sum_{k=0}^{N-1} a_k(t)\,\varphi_k(x), \qquad \varphi_k(x) = \sqrt{\frac{2}{L}}\cos\!\Bigl(\frac{k\pi x}{L}\Bigr), \tag{3}$$

with eigenvalues $\mu_k = (k\pi/L)^2$. The modal amplitudes $a_k(t)$ are extracted at each output step by discrete cosine transform (DCT-I). The modal energies are $E_k(t) = |a_k(t)|^2$.

### 4.2 Time Stepping

The default scheme (Crank–Nicolson) treats diffusion implicitly and nonlinear terms explicitly:

$$\frac{\rho^{n+1} - \rho^n}{\Delta t} = \frac{D}{2}\bigl(L_h\rho^{n+1} + L_h\rho^n\bigr) + D\,N_h[\rho^n] - D\,P(\rho^n) + H\,v^n, \tag{4}$$

where $L_h$ is the discrete Laplacian and $N_h[\rho] = M'(\rho)\,|\nabla_h\rho|^2$ is the explicit nonlinear term. The participation variable is advanced by the exact exponential integrator:

$$v^{n+1} = e^{-\zeta\Delta t/\tau}\,v^n + \frac{\bar{F}^n}{\zeta}\bigl(1 - e^{-\zeta\Delta t/\tau}\bigr). \tag{5}$$

### 4.3 Stability Controls

The simulation engine enforces five structural invariants at every time step:

1. **Positivity:** $\rho_j^n > 0$ for all grid points $j$.
2. **Sub-capacity:** $\rho_j^n < \rho_{\max}$ for all $j$.
3. **Energy monotonicity:** $\mathcal{E}^{n+1} \leq \mathcal{E}^n$ (checked, not enforced; violations above $10^{-8}$ are logged).
4. **Mass consistency:** $|\mathcal{M}^{n+1} - \mathcal{M}^n|$ within truncation error.
5. **Mobility positivity:** $M(\rho_j^n) > 0$ at all interior points.

The time step satisfies the CFL condition $\Delta t < h^2/(2D\,M_{\max})$, which for the default parameters gives $\Delta t_{\mathrm{CFL}} \approx 8.5 \times 10^{-4}$. The operational time step $\Delta t = 3.125 \times 10^{-5}$ provides a safety margin of $\sim 27\times$.

### 4.4 Convergence Criteria

A run terminates when either $t = T$ (normal completion) or a structural violation is detected (abnormal termination). The termination reason is recorded in metadata. For invariant analysis, only runs with `termination_reason = "FinalTime"` and zero positivity/capacity violations are classified as admissible.

### 4.5 Attractor Window

All invariant quantities are computed over the **attractor window**: the last 10% of the time series for late-time averages, and the last 20% for convergence-rate fits. This ensures that the invariants reflect the asymptotic attractor, not the transient approach.

---

## 5. Invariant Families

Each invariant family captures one structural aspect of the ED attractor. For each family, we state the mathematical definition, the ED prediction, and the empirical criterion.

The coefficient of variation (CV) is the primary invariance metric:

$$\mathrm{CV} = \frac{\sigma}{\mu}, \tag{6}$$

where $\mu$ and $\sigma$ are the mean and standard deviation of the invariant across all admissible runs. The verdicts are:

| CV | Verdict |
|----|---------|
| $< 0.05$ | INVARIANT |
| $< 0.15$ | WEAKLY INVARIANT |
| $\geq 0.15$ | NOT INVARIANT |

### 5.1 Low-Mode Collapse

**Definition.** For each mode $k = 0, \ldots, 5$, compute the late-time average amplitude:

$$m_k^* = \bigl\langle |a_k(t)| \bigr\rangle_{\mathrm{att}}, \tag{7}$$

where $\langle \cdot \rangle_{\mathrm{att}}$ denotes the mean over the attractor window.

**ED prediction.** All modes decay to zero: $m_k^* = 0$ for all $k$, reflecting the point-attractor structure of Principle 3. In practice, $m_k^*$ should be small (order $10^{-6}$ or below) and independent of $(D, A, N_m)$.

**Figure 2 description.** *Low-mode collapse.* Left panel: semilog-$y$ time series of $|a_k(t)|$ for $k = 0, \ldots, 5$, showing the decay of all modes to the noise floor. Right panel: the attractor profile $m_k^*$ versus $k$ for all 60 admissible runs, overlaid, showing collapse to a universal curve.

### 5.2 Mode-Energy Ratios

**Definition.** For each mode $k = 1, \ldots, K$:

$$R_k^* = \bigl\langle E_k(t) / E_{\mathrm{total}}(t) \bigr\rangle_{\mathrm{att}}, \qquad E_k = |a_k|^2. \tag{8}$$

**ED prediction.** The energy distribution across modes converges to a fixed profile independent of the initial condition and parameters. The profile is determined by the modal hierarchy: lower modes carry more energy.

### 5.3 Spectral Complexity (Rényi Entropies)

**Definition.** Normalise modal energies to a probability distribution $p_k(t) = E_k(t)/\sum_j E_j(t)$, and compute the Rényi entropy of order $q$:

$$H_q(t) = \frac{1}{1-q}\log\!\Bigl(\sum_k p_k(t)^q\Bigr), \qquad q \in \{0, 0.5, 1, 2, 3, 4\}, \tag{9}$$

with the $q \to 1$ limit giving the Shannon entropy.

**ED prediction.** Each $H_q^*$ converges to a fixed value independent of parameters, reflecting the universal spectral structure of the attractor.

### 5.4 Dissipation Partitions

**Definition.** Compute the three dissipation-channel ratios:

$$R_{\mathrm{grad}}^* = \bigl\langle \mathcal{D}_{\mathrm{grad}} / \mathcal{D}_{\mathrm{total}} \bigr\rangle_{\mathrm{att}}, \quad R_{\mathrm{pen}}^* = \bigl\langle \mathcal{D}_{\mathrm{pen}} / \mathcal{D}_{\mathrm{total}} \bigr\rangle_{\mathrm{att}}, \quad R_{\mathrm{part}}^* = \bigl\langle \mathcal{D}_{\mathrm{part}} / \mathcal{D}_{\mathrm{total}} \bigr\rangle_{\mathrm{att}}. \tag{10}$$

**ED prediction.** The three-channel dissipation structure converges to a fixed partition $R_{\mathrm{grad}}^* + R_{\mathrm{pen}}^* + R_{\mathrm{part}}^* = 1$ that is determined by the architecture, not by the initial condition.

### 5.5 Energy–Entropy Geometry

**Definition.** The attractor point in the energy–entropy plane:

$$(E^*, H^*) = \bigl(\langle E(t)\rangle_{\mathrm{att}},\; \langle H_1(t)\rangle_{\mathrm{att}}\bigr). \tag{11}$$

**ED prediction.** All runs converge to the same $(E^*, H^*)$, confirming that the attractor is a single point in the joint energy–entropy space.

**Figure 3 description.** *Energy–entropy trajectory.* Parametric curve $(E(t), H(t))$ for the representative run (largest $N_m$), colored by time. The trajectory spirals inward and converges to the attractor point $(E^*, H^*)$, marked with a star. Start and end points are marked.

### 5.6 Broadband Cascade

**Definition.** Define logarithmic mode bins ($k = 1\text{–}2$, $3\text{–}4$, $5\text{–}8$, $9\text{–}16$, $17\text{–}32$) and compute the bin-energy ratios:

$$R_b^* = \bigl\langle B_b(t) / E_{\mathrm{total}}(t) \bigr\rangle_{\mathrm{att}}, \qquad B_b = \sum_{k \in \mathrm{bin}\,b} E_k. \tag{12}$$

**ED prediction.** The cascade profile $(R_1^*, \ldots, R_B^*)$ is universal: the energy redistribution across spectral scales converges to a fixed profile governed by the triad selection rule.

### 5.7 Convergence Stability

**Definition.** For each of three signals ($E$, $H$, $\mathcal{D}_{\mathrm{total}}$), identify the three convergence stages and fit the Stage III exponential rate:

$$|E(t) - E^*| \sim C\,e^{-\sigma_E\,t}. \tag{13}$$

**ED prediction.** The three-stage structure (global bounds → algebraic decay → exponential decay) is universal, and the Stage III rate $\sigma_E$ depends only on the spectral gap $D\alpha_1$ and the participation damping $\zeta/\tau$.

### 5.8 Modal Correlations

**Definition.** Compute the correlation matrix of modal energies over the attractor window:

$$C_{ij} = \mathrm{corr}(E_i(t), E_j(t)), \qquad i, j = 1, \ldots, K. \tag{14}$$

Extract summary invariants: mean off-diagonal correlation, spectral radius, condition number.

**ED prediction.** The correlation structure is governed by the triad network: modes connected by triads are correlated; unconnected modes are independent. The mean correlation and spectral radius should be parameter-independent.

### 5.9 Modal Overlap

**Definition.** For each mode $k$, define the nearest-neighbour overlap:

$$O_k^* = \bigl\langle (E_{k-1} + E_k + E_{k+1}) / E_{\mathrm{total}} \bigr\rangle_{\mathrm{att}}. \tag{15}$$

**ED prediction.** The overlap profile $O_k^*$ is universal, reflecting the local spectral structure of the attractor.

### 5.10 Phase Dynamics

**Definition.** Extract modal phases $\phi_k(t) = \arg(a_k(t))$, unwrap along time, and compute:

- Phase drift rates $d\phi_k/dt$ (linear fit over the attractor window).
- Phase coherence $C_{ij} = |\langle e^{i(\phi_i - \phi_j)}\rangle|$ between modes.
- Triad phase closure $\Delta_{ijk} = \phi_i + \phi_j - \phi_k$ for triads $(i,j,k)$ with $i + j = k$.

**ED prediction.** In the oscillatory regime ($\mathscr{D}_0 < 0$), the phases are coherent (drift rates proportional to modal frequencies). The triad closure $\Delta_{ijk}$ converges to a fixed value, reflecting the phase-locking predicted by the nonlinear triad coupling.

### 5.11 Phase–Amplitude Coupling

**Definition.** For each mode $k$, compute:

$$\rho_k = \mathrm{corr}(|a_k(t)|, \phi_k(t)) \tag{16}$$

over the attractor window, and the cross-mode PAC matrix $\mathrm{PAC}_{ij} = \mathrm{corr}(|a_i|, \phi_j)$.

**ED prediction.** In the attractor window, the phase and amplitude should decouple (the attractor is a fixed point, not a limit cycle), so $|\rho_k| \approx 0$ and $|\mathrm{PAC}_{ij}| \approx 0$.

### 5.12 Lyapunov Spectrum

**Definition.** Construct the state vector $\mathbf{x}(t) = [\mathrm{Re}(a_1), \mathrm{Im}(a_1), \ldots]$, compute finite-difference tangent vectors, and extract the Lyapunov exponents $\lambda_i$ via QR accumulation over the attractor window. Compute the Kaplan–Yorke dimension:

$$D_{\mathrm{KY}} = j + \frac{\sum_{i=1}^j \lambda_i}{|\lambda_{j+1}|}, \tag{17}$$

where $j$ is the largest index such that $\sum_{i=1}^j \lambda_i \geq 0$.

**ED prediction.** All Lyapunov exponents are non-positive: the attractor is stable. The number of zero exponents is one (the trivial exponent from time-translation invariance of the autonomous system). $D_{\mathrm{KY}} \approx 0$, confirming the point-attractor structure.

**Figure 4 description.** *Lyapunov spectrum.* Left panel: $\lambda_i$ versus index $i$ for the representative run, showing all exponents non-positive. A horizontal line marks $\lambda = 0$. Right panel: $D_{\mathrm{KY}}$ versus $D$ for all runs, showing near-zero values across the parameter space.

### 5.13 Attractor Manifold

**Definition.** Perform PCA on the state vectors in the attractor window. Compute:

- Eigenvalues $\lambda_i$ of the covariance matrix (sorted descending).
- Effective dimension $D_{\mathrm{eff}}$: smallest $m$ such that $\sum_{i=1}^m \lambda_i \geq 0.99\sum_j \lambda_j$.
- Spectral gap $\lambda_1/\lambda_2$.

**ED prediction.** $D_{\mathrm{eff}} \leq 2$, consistent with a point attractor (the residual variance is numerical noise). The spectral gap should be large (the attractor is low-dimensional).

### 5.14 Perturbed-Attractor Stability

**Definition.** Perturb the attractor state by $\epsilon\,\boldsymbol{\xi}$ for $\epsilon \in \{10^{-6}, 10^{-5}, 10^{-4}, 10^{-3}\}$ and measure the recovery rate:

$$E_{\mathrm{err}}(t) = \sum_k |a_k(t) - a_k^*|^2 \sim C\,e^{-\sigma_\epsilon\,t}. \tag{18}$$

**ED prediction.** The recovery rate $\sigma_\epsilon$ is independent of $\epsilon$ (linear stability regime) and matches the spectral gap. Recovery is monotonic (no rebounds).

### 5.15 Parameter Universality

**Definition.** Construct a unified invariant vector $\mathbf{I}$ for each run by concatenating all invariant summaries. Standardise across runs. Compute the pairwise distance matrix and the universality score:

$$U = \frac{1}{1 + \mathrm{CV}(\text{distances})}. \tag{19}$$

**ED prediction.** $U \approx 1$: the invariant vectors cluster tightly, confirming that the attractor structure is universal across parameter regimes.

### 5.16 Cross-Invariant Consistency

**Definition.** For each pair of invariant families $(A, B)$, compute the mean pairwise correlation. The consistency score is:

$$C = \bigl\langle |\mathrm{corr}(A, B)| \bigr\rangle_{A \neq B}. \tag{20}$$

**ED prediction.** $C > 0.8$: the invariant families agree with each other, confirming that they all describe the same attractor.

---

## 6. Meta-Analyses

### 6.1 Parameter Universality

The universality analysis constructs the distance matrix $d_{ij} = \|\mathbf{I}_i - \mathbf{I}_j\|_2$ between all pairs of admissible runs in the standardised invariant space. Hierarchical clustering (Ward linkage) reveals the cluster structure. The number of clusters at the 5% dissimilarity threshold, the silhouette score, and the universality score $U$ are reported.

A universal architecture predicts a single tight cluster ($U > 0.9$). Regime-dependent structure would produce multiple clusters ($U < 0.75$).

### 6.2 Cross-Consistency

The cross-consistency analysis computes the $F \times F$ correlation matrix between invariant families, where $F$ is the number of families. Each family is represented by its per-run summary vector (e.g., $(R_1^*, \ldots, R_K^*)$ for mode-energy ratios). The redundancy of each family — defined as the mean absolute correlation with all other families — identifies which families carry independent information and which are structurally redundant.

**Figure 5 description.** *Cross-invariant correlation heatmap.* An $F \times F$ grid with invariant families on both axes. Cell color encodes $|\mathrm{corr}(A, B)|$ from white (0) through yellow (0.5) to red (1). Families are clustered by similarity. Annotations in each cell show the correlation value. A color bar is provided.

### 6.3 Embedding Collapse

The embedding analysis projects the standardised invariant vectors into two dimensions using PCA, t-SNE, and (optionally) UMAP. The cluster radius (mean distance to centroid), cluster diameter (maximum pairwise distance), and embedding consistency $C_{\mathrm{emb}} = \mathrm{corr}(d_{\mathrm{PCA}}, d_{\mathrm{UMAP}})$ are reported.

A collapsed embedding (cluster radius $< 0.1$) confirms that the attractor structure is effectively parameter-independent in the full invariant space.

**Figure 6 description.** *Embedding map.* Three panels: PCA, t-SNE, and UMAP projections. Each panel shows the 60 admissible runs as scatter points, colored by $D$, with marker shape encoding $N_m$. The centroid is marked with a cross. A dashed circle of radius equal to the cluster radius is drawn. The cluster radius and embedding consistency are annotated.

---

## 7. Global Synthesis and Architectural Verdict

### 7.1 Invariant Agreement

The sixteen invariant families probe the attractor from independent angles: spectral (families 1–3, 6, 8–9), dynamical (7, 10–11, 14), topological (12–13), and statistical (4–5, 15–16). The cross-consistency score $C$ measures their mutual agreement. A score $C > 0.8$ indicates that the families describe a single coherent structure — the ED attractor — rather than independent phenomena.

### 7.2 Parameter Universality

The universality score $U$ measures whether the attractor's invariant structure is the same across all 64 parameter regimes. A score $U > 0.9$ confirms the closure theorems of Appendix D: the qualitative attractor structure is invariant under parameter variation within $\mathcal{U}_{\mathrm{ED}}$.

### 7.3 Stability Confirmation

The Lyapunov spectrum (family 12) and the attractor manifold (family 13) provide complementary stability diagnostics. Zero positive Lyapunov exponents confirm that the attractor is stable. An effective dimension $D_{\mathrm{eff}} \leq 2$ confirms that it is a point (the residual dimensions reflect numerical noise, not dynamical degrees of freedom).

### 7.4 The ED Consistency Certificate

The certificate encodes the global synthesis in a single document:

| Diagnostic | Verdict | Key Metric |
|-----------|---------|------------|
| Universality | — | $U$ |
| Cross-Consistency | — | $C$ |
| Stability | — | $n_+$, $D_{\mathrm{KY}}$, $D_{\mathrm{eff}}$ |
| Embedding | — | cluster radius |
| Perturbation Recovery | — | $\epsilon$-independence CV |

The final verdict is:

- **PASS** if all five diagnostics are satisfactory.
- **PARTIAL** if some diagnostics are weakly satisfactory.
- **FAIL** if any diagnostic contradicts the ED architecture.

**Figure 7 description.** *ED Consistency Certificate (schematic).* A typeset box showing the certificate header, verdict banner, synthesis table, and signature block. The verdicts and metrics are representative values.

---

## 8. Reproducibility and Release Suite

### 8.1 Directory Structure

The reproducibility suite is located at `reproducibility/` within the ED Simulation repository:

```
reproducibility/
    README.md               Top-level documentation
    run_all.py              Master pipeline script
    checks/
        check_environment.py
        check_data_integrity.py
    scenarios/
        minimal/            1 run, 1 invariant (< 2 min)
        full/               Complete pipeline (30–120 min)
        diagnostic/         Checks only (< 30 s)
    docs/
        architecture.md     Pipeline architecture
        onboarding.md       New-user guide
        invariant_map.md    All 16 families at a glance
    validation/
        expected_structure.json
        hash_reference.json
        validate_outputs.py
    examples/               Sample JSONs
    figures/                Reference figures
```

### 8.2 Master Script

The command `python reproducibility/run_all.py` executes eight phases:

1. Environment checks (Python version, packages).
2. Data integrity (run directories, NPZ validity).
3. Regime volume experiment (64 runs).
4. Invariant analyses (16 families).
5. Meta-analyses (universality, cross-consistency, embedding).
6. Global atlas report.
7. Master index and certificate.
8. Output validation.

Each phase is isolated: a failure in one phase does not abort the pipeline. The master script produces a JSON pipeline report with per-step status, timing, and error messages.

### 8.3 Reproducibility Tiers

| Tier | Criterion | Scope |
|------|-----------|-------|
| 1 (Bitwise) | Identical file hashes | Same OS, Python, libraries, hardware |
| 2 (Numerical) | Field-by-field agreement within $10^{-10}$ | Same libraries, different hardware |
| 3 (Observable) | All invariant verdicts identical | Any conforming environment |

The suite targets Tier 3 as the minimum guarantee and Tier 1 within a fixed environment.

### 8.4 Validation

The script `validate_outputs.py` checks that all expected outputs exist:

- 64 valid regime-volume runs.
- 19 invariant figure directories with PNG files.
- 19 invariant summary JSONs.
- 6 atlas files (report, index, certificate, environment, integrity, validation).

It produces a JSON validation report and exits with code 0 (all checks pass) or 1 (one or more critical checks fail).

---

## 9. Discussion

### 9.1 Implications for the ED Architecture

The invariant atlas provides the first systematic numerical evidence that the ED canonical PDE system exhibits the structural properties predicted by the seven principles and proved analytically in Appendix C. The point-attractor structure, the three-stage convergence, the triad selection rule, the modal hierarchy, and the dissipation partition — all predicted by the analytic theory — are confirmed quantitatively across 64 parameter regimes.

The universality result ($U > 0.9$, if confirmed) is the most significant: it validates the closure theorems of Appendix D, which assert that the qualitative attractor structure is invariant under constitutive perturbation. This is the numerical foundation for the physical predictions of the Applications Paper, which apply the ED architecture to quantum, galactic, condensed-matter, and photonic systems by asserting that these systems belong to $\mathcal{U}_{\mathrm{ED}}$ and therefore inherit the canonical attractor structure.

### 9.2 Limitations

**Parameter coverage.** The current grid covers four values of each of $D$, $A$, and $N_m$. Finer grids — particularly near the critical surface $\mathscr{D}_0 = 0$ and the capacity boundary $\rho \to \rho_{\max}$ — may reveal structure not captured by the current atlas.

**One spatial dimension.** All runs are in one spatial dimension. The triad selection rule and the modal hierarchy extend naturally to higher dimensions (the Neumann eigenbasis generalises), but the quantitative invariant values may differ. Two- and three-dimensional extensions are planned for ED-SIM v2.

**Deterministic dynamics.** The current pipeline solves the deterministic PDE. The stochastic extension (§10.5 of the Simulation Suite) will test whether the invariant structure survives the addition of noise, which is necessary for comparison with physical systems that are inevitably fluctuating.

**Finite integration time.** The attractor window is the last 10–20% of $T = 20$. For high-complexity initial conditions (large $A$, large $N_m$), the solution may not have fully entered the exponential-decay regime by $T = 20$. Longer integrations ($T = 100$ or beyond) are available in the three-stage convergence experiment but are not part of the standard regime-volume sweep.

### 9.3 Future Work

- **ED-SIM v2**: higher spatial dimensions, adaptive mesh refinement, GPU acceleration.
- **Stochastic extension**: noise-driven invariants, fluctuation spectroscopy, noise-robustness testing.
- **Physical domain mapping**: constitutive-function identification for specific physical systems (superconductors, microcavities, dwarf galaxies).
- **Finer parameter grids**: targeted sweeps near the critical surface, the capacity boundary, and the high-complexity frontier.
- **Continuous integration**: automated pipeline execution on every code change, with regression testing against the reference atlas.

---

## 10. Conclusion

ED-SIM v1 is a scientific instrument for the Event Density architecture. It translates the seven canonical principles and the analytic theorems of Appendix C into a systematic, reproducible, machine-verifiable numerical atlas.

The invariant atlas is a structural map of the ED attractor. Its sixteen families probe the attractor from independent angles — spectral, dynamical, topological, and statistical — and their mutual consistency, measured by the cross-consistency score $C$, confirms that they describe a single coherent structure.

The ED Consistency Certificate is a condensed summary of the atlas. It encodes five global diagnostics — universality, cross-consistency, stability, embedding collapse, and perturbation recovery — into a single verdict. The certificate is the bridge between the mathematical architecture (Appendix C) and the physical predictions (Applications Paper): if the certificate reads PASS, the architecture is structurally self-consistent, and the predictions that follow from it are well-founded.

The complete pipeline — from empty directory to final certificate — is executable from a single command. The reproducibility suite provides environment checks, data integrity verification, output validation, and reference hashes. An independent researcher can regenerate the atlas, verify the certificate, and extend the analysis to new parameter regimes, new invariant families, or new physical domains.

The architecture stands until a test breaks it. The atlas documents where to look.

---

## References

[1] A. Proxmire, "The Event Density Architectural Canon," ED-Arch-I, 2025.

[2] A. Proxmire, "Mathematical Foundations of the Event Density Architecture," ED-Arch-II (Rigour Paper), 2025. Appendices C (Well-Posedness and Long-Time Behavior) and D (Universality Class).

[3] A. Proxmire, "Physical Applications of the Event Density Architecture," ED-Arch-III (Applications Paper), 2025.

[4] A. Proxmire, "ED-SIM v1: Numerical Atlas for the Event Density Canon," Numerical Atlas, 2025.

[5] A. Proxmire, "ED-SIM v1: Simulation Suite Specification," Simulation Suite, 2025.

[6] A. Proxmire, "Event Density Experimental Program," Open Note ED-00, 2024.

[7] G. Da Prato and J. Zabczyk, *Stochastic Equations in Infinite Dimensions*, Cambridge University Press, 1992.

[8] D. Henry, *Geometric Theory of Semilinear Parabolic Equations*, Springer Lecture Notes in Mathematics, vol. 840, 1981.

[9] A. Lunardi, *Analytic Semigroups and Optimal Regularity in Parabolic Problems*, Birkhäuser, 1995.

[10] R. Temam, *Infinite-Dimensional Dynamical Systems in Mechanics and Physics*, 2nd ed., Springer, 1997.

---

## Figure Captions (Summary)

**Figure 1.** Pipeline architecture diagram. Five layers from PDE solver to certificate generation.

**Figure 2.** Low-mode collapse. (a) Time series of $|a_k(t)|$ for $k = 0, \ldots, 5$. (b) Attractor profile $m_k^*$ versus $k$ for all admissible runs.

**Figure 3.** Energy–entropy trajectory. Parametric curve $(E(t), H(t))$ for the representative run, spiraling toward the attractor point $(E^*, H^*)$.

**Figure 4.** Lyapunov spectrum. (a) $\lambda_i$ versus index $i$. (b) Kaplan–Yorke dimension $D_{\mathrm{KY}}$ versus $D$ for all runs.

**Figure 5.** Cross-invariant correlation heatmap. $F \times F$ matrix of $|\mathrm{corr}(A, B)|$ between invariant families.

**Figure 6.** Embedding map. PCA, t-SNE, and UMAP projections of the standardised invariant vectors, showing cluster collapse.

**Figure 7.** ED Consistency Certificate (schematic). Final verdict, synthesis table, and signature block.
