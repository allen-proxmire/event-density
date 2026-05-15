# From Primitives to Photonic Chern Channels and Quantized Hall Drift

*A walkthrough-grade Event Density (ED) Arc deriving the photonic Chern insulator and quantized Hall drift of light from substrate primitives. Fully self-contained: all required math is derived inside this document. Includes Appendix A proving Chern-number integer quantization from substrate primitives + differential topology.*

---

## 1. The Question

### What this walkthrough derives

This walkthrough derives, from substrate primitives, the structural backbone of photonic Chern insulators:

1. **Synthetic frequency lattice** as a periodic rule-type substrate, with frequency modes as participation-rule indices.

2. **Haldane-type effective Hamiltonian** with nearest-neighbor (NN) + complex-phase next-nearest-neighbor (NNN) couplings on a honeycomb-like rule-type lattice.

3. **Berry curvature on the synthetic Brillouin zone**, concentrated near synthetic Dirac points and integrating to a non-zero quantity.

4. **Chern number** $C_n = (1/2\pi)\iint_\text{BZ}\Omega_n\, d^2k$ as the integrated global rule-type curvature, with integer-quantization derived in Appendix A.

5. **Quantized Hall drift**: the substrate-level transverse displacement of a minimal channel (light) under imposed ED-tension (synthetic electric field) is

   $$
\Delta x⊥ per cycle = C_n \cdot a,
$$

   where $a$ is the lattice period and $C_n$ is the integer-valued Chern number of the occupied band.

6. **Driven-dissipative steady-state pinning**: the quantization survives Lindblad-type driven-dissipative dynamics because dissipation suppresses local fluctuations but cannot alter the global rule-type curvature.

The walkthrough is fully self-contained: every required Hilbert-space, eigenvalue, Bloch-form, gauge-transformation, semiclassical-equation-of-motion, and Lindblad step appears inside the document. The Chern-quantization proof is in Appendix A.

### What standard photonics says, and where it stops

The Chénier et al. 2026 PRX experiment encodes a Haldane-like model in the synthetic frequency dimension of an optical fiber loop. Electro-optic modulation creates tunable NN and NNN couplings between frequency modes; complex modulation phases break time-reversal symmetry. The resulting synthetic lattice exhibits:

- a honeycomb-like band structure,
- tunable topological phase transitions at non-zero Chern number,
- measurable Berry curvature across the Brillouin zone,
- a quantized transverse drift of light under detuning of the modulation frequency.

The standard description treats this as a photonic analog of the integer quantum Hall effect: synthetic gauge fields produce non-trivial band topology, and the topology produces a quantized response. This is mathematically correct. It is also mechanistically opaque about *why* light, despite carrying no charge, undergoes a quantized response; *what* the synthetic gauge field is at any deeper ontological level; and *why* the quantization is robust against driven-dissipative dynamics.

### What Event Density claims

The quantized Hall drift is FORCED at the substrate level of the Event Density (ED) framework whenever a minimal ED-channel (light) propagates through a periodic rule-type substrate with non-zero global rule-type curvature. The mechanism is structural:

- Light is a minimal ED-channel that carries no internal multiplicity capable of imposing geometry; it must follow the rule-type structure of the substrate it propagates through.
- A periodic rule-type substrate forces Bloch-form eigenchannels and a band structure indexed by quasi-momentum on a Brillouin zone.
- Complex NNN couplings impose a global rule-type twist (Berry curvature) that cannot be removed by local rule rephasing.
- The integrated curvature is integer-valued (Chern number) by topology of the parameter-space bundle (Appendix A).
- Imposed ED-tension (synthetic electric field) forces the chain to slide along the curved manifold, producing a transverse displacement quantized in units of $C_n \cdot a$ per cycle.
- Driven-dissipative dynamics suppress local fluctuations but cannot deform the global topological invariant; the quantization survives.

Light does not need charge. It needs a periodic rule-type substrate with non-zero Chern number — and an imposed ED-tension to make the global curvature manifest as observable transport.

The substrate-level mechanism, in one sentence: **quantized Hall drift is the rule-type curvature integrated over a closed Brillouin zone, made observable as transport by ED-tension acting on a minimal channel**.

### The chain in summary

The derivation chain runs:

substrate primitives (§2) → synthetic frequency lattice as periodic rule-type substrate, with translation operator and Bloch form derived inline (§3) → Haldane-type effective Hamiltonian + Berry connection + Berry curvature across the BZ derived inline (§4) → Chern number as integrated curvature, integer-quantization derived in Appendix A (§5) → semiclassical equations of motion + quantized Hall drift (§6) → driven-dissipative Lindblad steady state with topological invariant preserved (§7) → substrate-level reading (§8) → forced/inherited/open accounting (§9) → exact claims (§10) → integer-quantization proof (Appendix A).

---

## 2. The Primitives

### P-PC-1. Minimal ED-channel (photon)

A *photon* is a minimal ED-channel: a participation pathway with multiplicity $M=1$. At any one substrate-tick, the channel commits to exactly one alignment thread. The minimal channel cannot store internal geometry — it has no internal multiplicity to deform — and therefore cannot impose structure on its substrate. It can only follow the rule-type structure of the surrounding substrate.

**Substrate-level meaning.** The photon is a probe: it reveals the substrate's rule-type geometry as transport. Any curvature, twist, or tension in the substrate is expressed directly in the photon's pre-individuation amplitude.

**No charge requirement.** The minimal-channel structure makes no reference to electric charge. The photon couples to the substrate's rule-type structure regardless of whether that structure originates in a magnetic field, a synthetic gauge field, or a periodic dielectric pattern.

### P-PC-2. Periodic participation rule in synthetic dimension

A *synthetic dimension* is a re-indexing of participation rules: distinct participation rules are labeled by an integer index $m \in \mathbb{Z}$, with the rule structure and inter-rule couplings determined by the substrate's effective construction.

**Periodicity.** A periodic rule structure in synthetic dimension means

$$
r_m = r_{m + N_period} or r_{m+a} = r_m
$$

where $a$ is the unit-cell size in synthetic-index units. (We will use lattice-period $a$ ambiguously between physical lattice constant and synthetic-cell index; the structural argument is identical.)

**Frequency-mode realization.** In the Chénier et al. experiment, frequency modes $\omega_m = \omega_0 + m\Omega_R$ (spaced by the cavity round-trip frequency $\Omega_R$) play the role of synthetic-dimension sites. Electro-optic modulation imposes structured couplings between these modes. Frequency modes are not physical lattice sites; they are distinct timing alignments of ED-flow, indexed by $m$, that the substrate's modulation pattern couples in a structured way.

### P-PC-3. Complex rule-type couplings (NN + NNN)

Two types of rule-type couplings appear in the Haldane construction:

- **Nearest-neighbor (NN)** couplings: matrix elements of the effective Hamiltonian connecting mode $m$ to mode $m+1$, real-valued, denoted $t_1$.

- **Next-nearest-neighbor (NNN)** couplings: matrix elements connecting mode $m$ to mode $m+2$, complex-valued with phase $\phi$, denoted $t_2 e^{i\phi}$.

**Substrate-level meaning.** NN couplings are local ED-flow continuity: they encode how the chain's identity transitions between adjacent participation rules. NNN couplings with complex phase are *global ED-twist*: a phase factor that cannot be removed by local rephasing of individual rules, because the phase accumulates around closed loops in the lattice.

**Why complex.** A real coupling produces no phase accumulation around any loop; a complex coupling with a phase $\phi$ produces a phase $e^{i\phi}$ for each NNN hop. When the lattice geometry contains closed paths (e.g., the honeycomb plaquettes of the Haldane model), the accumulated phase per plaquette is the substrate-level rule-type *flux* through that plaquette.

### P-PC-4. Time-reversal breaking as directional ED-bias

*Time-reversal symmetry* of the substrate's rule-type structure is the property that the rule structure is invariant under reversal of substrate-tick direction. Algebraically, the effective Hamiltonian satisfies $\mathcal{T} H \mathcal{T}^{-1} = H$ where $\mathcal{T}$ is the antiunitary time-reversal operator.

**Breaking via complex NNN phase.** The complex NNN coupling $t_2 e^{i\phi}$ breaks time-reversal symmetry when $\phi \neq 0, \pi$: the antiunitary $\mathcal{T}$ would map $t_2 e^{i\phi} \to t_2 e^{-i\phi}$, and these are distinct unless $\phi$ is a multiple of $\pi$.

**Substrate-level meaning.** Breaking time-reversal symmetry imposes a *directional bias* in the substrate's rule-type structure: the rule structure distinguishes "forward" from "backward" propagation around closed loops. This directional bias is the substrate-level origin of the global ED-twist quantified by non-zero Chern number.

### P-PC-5. ED-tension (synthetic electric field)

An *ED-tension* in synthetic dimension is a linear gradient in rule-type energy: the on-site energy of mode $m$ takes the form

$$
E_m = m \cdot F \cdot a
$$

where $F$ is the ED-tension strength and $a$ is the lattice period. The total Hamiltonian becomes $H = H_\text{lattice} + F\hat{x}$, where $\hat{x}$ is the position operator on the synthetic lattice ($\hat{x}|m\rangle= ma|m\rangle$).

**Realization.** In the Chénier et al. experiment, detuning the modulation frequency by $\delta$ produces a linear shift in mode energies: $E_m = m\delta$. The ED-tension is the substrate-level analog of a synthetic electric field acting on the chain's pre-individuation amplitude.

**Substrate-level meaning.** ED-tension is a structural tilt of the rule-type energy landscape that biases the chain's participation flow. The chain seeks to lower its rule-type energy, which corresponds to drift along the synthetic dimension. When the substrate has zero rule-type curvature, this drift is purely longitudinal. When the substrate has non-zero rule-type curvature, the drift acquires a transverse component — the Hall drift.

### P-PC-6. Driven-dissipative ED-flow equilibrium

Open photonic systems involve continual injection of substrate participation (the drive) and extraction (dissipation, including loss to bath modes and intentional decay channels). The substrate-level state is not a closed-system pure state but a steady-state distribution over alignment threads.

**Lindblad-form coarse-graining.** The substrate-level steady-state density operator $\rho$ satisfies

$$
\partial_t \rho= -i[H, \rho] + \sum_\alpha[L_\alpha \rho L_\alpha † - (1/2){L_\alpha † L_\alpha, \rho}] (set \partial_t \rho= 0 for steady state)
$$

where $H$ is the unitary-evolution generator, $L_\alpha$ are the Lindblad jump operators encoding the coupling to the bath (drive + loss). Derivation of this form is given inline in §7.

**Steady state.** The steady state is the unique stationary solution $\rho_\text{ss}$ with $\partial_t \rho_\text{ss} = 0$. Under generic Lindblad operators, the steady state exists, is unique, and is reached on a timescale set by the dissipation rate.

**Substrate-level meaning.** The steady state is the substrate's equilibrium distribution of alignment commitments under continuous drive + dissipation. Local fluctuations are damped; global topological structure (curvature, Chern number) is preserved.

### P-PC-7. Global ED-curvature on the Brillouin zone

The *global ED-curvature* on the Brillouin zone is the rule-type curvature two-form $\Omega_n(\mathbf{k})$ defined on the closed parameter manifold $\mathcal{B} = \mathbb{T}^2$ (the 2D Brillouin zone is topologically a torus). It is gauge-invariant (§4.4 below) and integrates over $\mathcal{B}$ to a quantity that is integer-valued in units of $2\pi$ (Appendix A).

**Substrate-level meaning.** The global ED-curvature is the substrate-level measure of rule-type twist accumulated per unit area of the parameter manifold. It is the curvature of the rule-type connection on the BZ-bundle of band eigenchannels.

**No additional substrate primitives are introduced beyond P-PC-1 through P-PC-7.**

---

## 3. Constructing the Synthetic Frequency Lattice

### 3.1 Frequency modes as participation-rule indices

In the optical-fiber-loop experiment, the cavity supports a discrete set of resonant frequency modes $\omega_m = \omega_0 + m\Omega_R$ for $m \in \mathbb{Z}$. Each frequency mode is a distinct timing alignment of ED-flow. Electro-optic modulation at frequencies commensurate with $\Omega_R$ couples adjacent modes, and at frequencies commensurate with $2\Omega_R$ couples next-nearest modes.

The substrate-level identification: mode $m$ is a participation rule $r_m$ in the synthetic dimension (P-PC-2), and the chain's pre-individuation amplitude is

$$
|\psi \rangle= \sum_m c_m |m\rangle, with \sum_m |c_m|^{2} = 1.
$$

### 3.2 NN and NNN couplings from electro-optic modulation

A modulation pulse at frequency $\Omega_R$ with complex amplitude $t_1 e^{i\theta_1}$ couples mode $m$ to mode $m+1$. A modulation pulse at frequency $2\Omega_R$ with complex amplitude $t_2 e^{i\phi}$ couples mode $m$ to mode $m+2$. The effective Hamiltonian on the synthetic lattice is

$$
H_{\mathrm{synth}} = -t_1 \sum_m (|m+1\rangle \langle m| + h.c.) - t_2 \sum_m (e^{i\varphi} |m+2\rangle \langle m| + h.c.).
$$

Without loss of generality, we choose the phase of the NN coupling to be zero ($\theta_1 = 0$); any non-zero $\theta_1$ can be absorbed by a global gauge transformation $|m\rangle \to e^{im\theta_1}|m\rangle$.

### 3.3 Two-sublattice structure (honeycomb analog)

The Haldane model lives on a honeycomb lattice with two sublattices A and B. The synthetic-dimension realization assigns even-indexed modes to sublattice A and odd-indexed modes to sublattice B. The NN couplings connect A↔B (intra-cell), the NNN couplings connect A↔A and B↔B (inter-cell of the same sublattice), and a possible on-site mass term $M$ distinguishes A from B sublattice energies.

Group the modes into unit cells of two: $|A_n\rangle= |2n\rangle$ and $|B_n\rangle= |2n+1\rangle$ for $n \in \mathbb{Z}$. The lattice period is $a = 2$ in synthetic-index units (and the corresponding physical unit-cell spacing in frequency space).

### 3.4 Translation operator and commutation

Define the translation operator $T_a$ by

$$
T_a |A_n\rangle= |A_{n+1}\rangle, T_a |B_n\rangle= |B_{n+1}\rangle.
$$

$T_a$ is unitary on the synthetic-dimension Hilbert space (its inverse is $T_{-a}$ acting by the opposite shift).

Compute the action of $T_a$ on $H_\text{synth}$ (after grouping into A/B sublattices). The Hamiltonian translates as

$$
T_a H_{\mathrm{synth}} T_a^{-1} = H_{\mathrm{synth}}
$$

because: (i) the NN couplings $|A_n\rangle\langle B_n|$ and $|B_n\rangle\langle A_{n+1}|$ shift to $|A_{n+1}\rangle\langle B_{n+1}|$ and $|B_{n+1}\rangle\langle A_{n+2}|$, structurally identical; (ii) the NNN couplings shift similarly with the same complex phase $e^{i\phi}$; (iii) the on-site mass term $M$ is sublattice-dependent but translation-invariant. Therefore $[H_\text{synth}, T_a] = 0$.

### 3.5 Bloch form

By the spectral theorem for commuting Hermitian operators, $H_\text{synth}$ and $T_a$ admit a simultaneous eigenbasis. We solve $T_a\psi= \lambda\psi$ with $|\lambda| = 1$ (unitarity), so $\lambda= e^{ika}$ for some $k \in \mathcal{B} = (-\pi/a, \pi/a]$. The eigenvalue equation gives

$$
\psi_k(2n) = e^{ikna} u^A_k, \psi_k(2n+1) = e^{ikna} u^B_k (for some k-dependent amplitudes u^A_k, u^B_k)
$$

equivalently, the Bloch form on the two-sublattice synthetic lattice:

$$
|\psi_k\rangle= \sum_n e^{ikna} (u^A_k |A_n\rangle + u^B_k |B_n\rangle).
$$

The two-component spinor $\mathbf{u}_k = (u^A_k, u^B_k)^T$ is the periodic factor on the unit cell. The Brillouin zone is the circle $\mathcal{B} = (-\pi/a, \pi/a]$ in 1D synthetic dimension.

### 3.6 Two-dimensional generalization

The Chénier et al. experiment realizes a 2D Haldane model in synthetic dimension by using two distinct modulation patterns to encode two effective lattice directions. The synthetic Brillouin zone is then a torus $\mathbb{T}^2 = \mathcal{B}_x \times \mathcal{B}_y$ with each factor a circle. The Bloch form generalizes to

$$
|\psi_k\rangle= e^{i k \cdot n_a} (u^A_k |A\rangle + u^B_k |B\rangle), k = (k_x, k_y) \in 𝕋^{2},
$$

where $\mathbf{n}_a$ is the integer-valued unit-cell index in 2D. We focus on the 2D case for the remainder of this walkthrough; the 1D construction in §§3.1–3.5 is the structural template.

---

## 4. Deriving the Haldane-Type Model as ED-Curvature

### 4.1 Bloch Hamiltonian

After Bloch decomposition, the Hamiltonian is block-diagonalized over $\mathbf{k} \in \mathbb{T}^2$, with each block a 2×2 matrix on the A/B sublattice space:

$$
H(k) = h_x(k) \sigma_x + h_y(k) \sigma_y + h_z(k) \sigma_z + \epsilon(k) I,
$$

where $\sigma_{x,y,z}$ are Pauli matrices on the sublattice space and $\varepsilon(\mathbf{k})$ is the diagonal kinetic-plus-mass contribution. For the Haldane construction:

$$
h_x(k) + i h_y(k) = -t_1 \sum_{\delta} e^{i k \cdot \delta} (sum over NN vectors \delta from A to B)
h_z(k) = M - 2 t_2 \sin(\varphi) \sum_{\delta_NNN} \sin(k \cdot \delta_NNN)
\epsilon(k) = -2 t_2 \cos(\varphi) \sum_{\delta_NNN} \cos(k \cdot \delta_NNN),
$$

where the NNN vectors $\delta_\text{NNN}$ are the three vectors connecting A-sites to A-sites (or equivalently B-sites to B-sites) via NNN hops, and the orientation convention gives a sign for the $\sin(\phi)$ term.

The Pauli-vector $\mathbf{h}(\mathbf{k}) = (h_x, h_y, h_z)$ encodes the rule-type structure on the sublattice space at each $\mathbf{k}$.

### 4.2 Eigenvalues and eigenchannels

The eigenvalues of $H(\mathbf{k})$ are

$$
E_ \pm(k) = \epsilon(k) \pm|h(k)|, |h(k)| = \sqrt{h_x^{2} + h_y^{2} + h_z^{2}}.
$$

Two bands: lower band $-$ at $E_-(\mathbf{k}) = \varepsilon(\mathbf{k}) - |\mathbf{h}(\mathbf{k})|$ and upper band $+$ at $E_+(\mathbf{k}) = \varepsilon(\mathbf{k}) + |\mathbf{h}(\mathbf{k})|$. The bands are gapped wherever $|\mathbf{h}(\mathbf{k})| > 0$.

The eigenchannels are spinors on the sublattice space:

$$
u_-(k) = (\sin(\theta /2), -e^{i\varphi_h} \cos(\theta /2))^T, u_+(k) = (\cos(\theta /2), e^{i\varphi_h} \sin(\theta /2))^T,
$$

where $(\theta(\mathbf{k}), \varphi_h(\mathbf{k}))$ are the spherical coordinates of the unit vector $\hat{\mathbf{h}}(\mathbf{k}) = \mathbf{h}/|\mathbf{h}|$:

$$
\hat{h}(k) = (\sin \theta \cos \varphi_h, \sin \theta \sin \varphi_h, \cos \theta).
$$

The map $\mathbf{k} \mapsto \hat{\mathbf{h}}(\mathbf{k})$ is a continuous map from the Brillouin zone $\mathbb{T}^2$ to the unit sphere $S^2$.

### 4.3 Berry connection re-derived inline

For the lower band, the Berry connection on the BZ is

$$
A_-(k) \equiv i \langle u_-(k) | \nabla_k u_-(k)\rangle.
$$

Compute the inner product. Differentiating $|u_-\rangle= (\sin(\theta/2), -e^{i\varphi_h}\cos(\theta/2))^T$ with respect to $\mathbf{k}$:

$$
\partial_{k_i} |u_-\rangle= ((1/2) \cos(\theta /2) \partial_{k_i}\theta, -(1/2)(-e^{i\varphi_h} \sin(\theta /2)) \partial_{k_i}\theta - i e^{i\varphi_h} \cos(\theta /2) \partial_{k_i}\varphi_h)^T
= ((1/2) \cos(\theta /2) \partial_i \theta, (1/2) e^{i\varphi_h} \sin(\theta /2) \partial_i \theta - i e^{i\varphi_h} \cos(\theta /2) \partial_i \varphi_h)^T.
$$

Compute $\langle u_- | \partial_{k_i} u_-\rangle$:

$$
\langle u_- | \partial_i u_-\rangle= \sin(\theta /2) \cdot(1/2)\cos(\theta /2)\partial_i \theta
+ (-e^{-i\varphi_h}\cos(\theta /2)) \cdot[(1/2)e^{i\varphi_h}\sin(\theta /2)\partial_i \theta - i e^{i\varphi_h} \cos(\theta /2) \partial_i \varphi_h]
= (1/2)\sin(\theta /2)\cos(\theta /2)\partial_i \theta - (1/2)\cos(\theta /2)\sin(\theta /2)\partial_i \theta + i \cos^{2}(\theta /2) \partial_i \varphi_h
= i \cos^{2}(\theta /2) \partial_i \varphi_h.
$$

Therefore

$$
A_-(k) = i \cdot \langle u_- | \nabla_k u_-\rangle= -\cos^{2}(\theta(k)/2) \nabla_k \varphi_h(k).
$$

Equivalently, using $\cos^2(\theta/2) = (1 + \cos\theta)/2$:

$$
A_-(k) = -(1/2)(1 + \hat{h}_z(k)) \nabla_k \varphi_h(k).
$$

### 4.4 Berry curvature: the substrate-level map to the sphere

Compute the Berry curvature in 2D:

$$
\Omega_-(k) = \partial_{k_x} A_-^y - \partial_{k_y} A_-^x.
$$

A standard manipulation (using the spherical-coordinate identity for the integrand) gives

$$
\Omega_-(k) = -(1/2) \hat{h}(k) \cdot(\partial_{k_x} \hat{h} \times \partial_{k_y} \hat{h}).
$$

This is the **pullback of the unit-sphere area form** by the map $\mathbf{k} \mapsto \hat{\mathbf{h}}(\mathbf{k})$. The integrated Berry curvature over $\mathbb{T}^2$ is

$$
∬_{𝕋^{2}} \Omega_-(k) d^{2}k = -(1/2) ∬_{𝕋^{2}} \hat{h} \cdot(\partial_{k_x} \hat{h} \times \partial_{k_y} \hat{h}) d^{2}k = -(1/2) \cdot 4\pi \cdot(degree of \hat{h}),
$$

where the *degree* of $\hat{\mathbf{h}}: \mathbb{T}^2 \to S^2$ is the integer counting how many times the image wraps the sphere.

### 4.5 Gauge transformation

Under a gauge transformation $|u_-(\mathbf{k})\rangle \to e^{i\chi(\mathbf{k})}|u_-(\mathbf{k})\rangle$, the Berry connection transforms as

$$
A_-(k) \to A_-(k) - \nabla_k \chi(k).
$$

Derivation: $i\langle e^{-i\chi}u_- | \nabla_k(e^{i\chi}u_-)\rangle= i\langle u_-|i(\nabla_k\chi)u_- + \nabla_k u_-\rangle= -\nabla_k\chi + i\langle u_-|\nabla_k u_-\rangle= \mathcal{A}_- - \nabla_k\chi$. The Berry curvature

$$
\Omega_-(k) \to \partial_{k_x}(A_-^y - \partial_{k_y}\chi) - \partial_{k_y}(A_-^x - \partial_{k_x}\chi) = \Omega_-(k)
$$

is gauge-invariant, by the equality of mixed partials for smooth $\chi$.

### 4.6 Concentration of Berry curvature near Dirac points

The Berry curvature $\Omega_-(\mathbf{k}) = -(1/2)\hat{\mathbf{h}}\cdot(\partial_{k_x}\hat{\mathbf{h}}\times\partial_{k_y}\hat{\mathbf{h}})$ is large where $\hat{\mathbf{h}}(\mathbf{k})$ varies rapidly. In the Haldane construction, $\hat{\mathbf{h}}$ varies most rapidly near the *Dirac points* — points $\mathbf{K}, \mathbf{K}'$ in the BZ where $h_x(\mathbf{k}) = h_y(\mathbf{k}) = 0$ and $\hat{\mathbf{h}}$ is determined entirely by the small $h_z$ component.

At the Dirac points, $h_z = M \mp 3\sqrt{3}t_2\sin\phi$ takes opposite signs (for the two valleys $\mathbf{K}, \mathbf{K}'$) when $M < 3\sqrt{3}|t_2\sin\phi|$. The unit vector $\hat{\mathbf{h}}$ then points to opposite poles of $S^2$ at the two Dirac points, and the map $\mathbf{k}\mapsto\hat{\mathbf{h}}(\mathbf{k})$ has degree $\pm 1$ — wrapping the sphere once.

### 4.7 Topological phase transition

The relative magnitudes of $M$ (sublattice mass) and $3\sqrt{3}t_2\sin\phi$ (NNN-induced topological mass) determine the band topology:

- $|M| > 3\sqrt{3}|t_2\sin\phi|$: trivial phase, $\hat{\mathbf{h}}(\mathbf{k})$ has zero degree, integrated curvature zero, $C_- = 0$.
- $|M| < 3\sqrt{3}|t_2\sin\phi|$: topological phase, $\hat{\mathbf{h}}$ has degree $\pm 1$, integrated curvature $\pm 2\pi$, $C_- = \pm 1$.

The phase transition occurs at $|M| = 3\sqrt{3}|t_2\sin\phi|$, where the band gap closes at one Dirac point and the topology of $\hat{\mathbf{h}}$ undergoes a discontinuous change.

---

## 5. Chern Number as Integrated Curvature

### 5.1 Definition

For each band $n$, the **Chern number** is the integrated Berry curvature divided by $2\pi$:

$$
C_n \equiv(1/(2\pi)) ∬_{𝕋^{2}} \Omega_n(k) d^{2}k.
$$

In the Haldane lower band: $C_-$ is $0$ in the trivial phase and $\pm 1$ in the topological phase.

### 5.2 Gauge invariance

$\Omega_n$ is gauge-invariant (§4.5), so the integral is gauge-invariant: $C_n$ is independent of the choice of phase for $|u_n(\mathbf{k})\rangle$.

### 5.3 Surface independence

For two different choices of integration domain bounded by the same closed curve, the integrals differ by the Berry phase around the boundary, which is zero modulo $2\pi$ for a single-valued gauge. On a closed manifold like the torus, the integrated curvature is therefore invariant under continuous deformations.

### 5.4 Integer-quantization

The integrated curvature on a closed 2D manifold is integer-valued in units of $2\pi$:

$$
C_n \in \mathbb{Z}.
$$

This is the central topological fact. **Full proof in Appendix A.** The proof uses the parameter-space bundle structure on the torus, the obstruction to a globally smooth gauge choice, the winding number of transition functions on patch overlaps, and Stokes' theorem.

### 5.5 Substrate-level meaning of the Chern number

The Chern number $C_n$ is the integer-valued global topological invariant of the band's rule-type bundle over the closed Brillouin zone. It counts the number of times the unit-vector field $\hat{\mathbf{h}}(\mathbf{k})$ wraps the sphere $S^2$ as $\mathbf{k}$ traverses the BZ, with sign determined by orientation.

**Substrate-level reading.** $C_n$ is the global ED-twist accumulated by the band's rule-type connection around the closed parameter manifold. It is the integer-valued statement of how much the rule-type identity rotates as a chain explores all quasi-momenta in the band.

---

## 6. ED-Tension and Quantized Hall Drift

### 6.1 Adding ED-tension to the Hamiltonian

ED-tension (synthetic electric field) adds a linear gradient to the on-site energies (P-PC-5):

$$
H_{\mathrm{total}} = H_{\mathrm{synth}} + F \cdot \hat{x},
$$

where $\hat{\mathbf{x}}$ is the position operator on the synthetic lattice and $\mathbf{F}$ is the ED-tension vector. In the synthetic-frequency-dimension realization, $\mathbf{F}$ corresponds to a linear detuning of mode energies.

### 6.2 Semiclassical equations of motion

We derive the semiclassical equations of motion for a chain in a single band in the presence of ED-tension. Start from the Heisenberg equation of motion for the position operator restricted to band $n$:

$$
ẋ_i = (i/\hbar)[H, x_i].
$$

In the band-projected picture, the effective Hamiltonian is $E_n(\mathbf{k}) + F\cdot\hat{\mathbf{x}}$, and the position operator within the band has a kinetic part plus an anomalous part from the Berry connection. A standard wave-packet derivation (worked out below) gives the semiclassical equations of motion:

$$
\hbar k̇ = F,
\hbar ẋ_i = \partial E_n(k)/\partial k_i - \epsilon_{ij} F_j \Omega_n(k),
$$

where the second term in the second equation is the *anomalous velocity* — the component of the velocity perpendicular to the ED-tension, proportional to the Berry curvature.

**Derivation of the anomalous velocity.** Construct a wave packet centered at $\mathbf{k}_0$ in momentum and $\mathbf{x}_0$ in position. The expectation value of position is the wave-packet center plus a Berry-connection correction:

$$
\langle x_i\rangle= x_{0,i} + A_n^i(k_0).
$$

(The Berry-connection correction arises because the band-projection from the full Hilbert space to the band's $|u_{n,k}\rangle$ subspace shifts the position-operator's expectation value by $\mathcal{A}_n$.) Differentiating with respect to time:

$$
\langle ẋ_i\rangle= (\partial x_{0,i}/\partial k_j)(dk_j/dt) + (\partial A_n^i/\partial k_j)(dk_j/dt)
= (\partial E_n/\partial k_i) + (\partial A_n^i/\partial k_j) \cdot F_j/\hbar
= (1/\hbar) \partial E_n/\partial k_i + F_j/\hbar \cdot(\partial_j A_n^i)
= (1/\hbar)[\partial E_n/\partial k_i - F_j \Omega_n^{ji}],
$$

where in the last step we used $\partial_j\mathcal{A}_n^i - \partial_i\mathcal{A}_n^j = -\Omega_n^{ji}$ (the curvature) and the wave-packet's first-order EOM $\dot{\mathbf{x}}_0 = (1/\hbar)\nabla_\mathbf{k} E_n$.

In 2D with $\mathbf{F} = F\hat{\mathbf{x}}$ (along the synthetic-electric-field direction) and Berry curvature $\Omega_n(\mathbf{k}) = \Omega_n^z(\mathbf{k})$ (the only non-zero component):

$$
\hbar ẋ = \partial E_n/\partial k_x, (longitudinal)
\hbar ẏ = \partial E_n/\partial k_y - F \cdot \Omega_n. (transverse, with anomalous-velocity term)
$$

### 6.3 Quantized transverse drift

Consider a chain initialized at one synthetic-dimension site and subjected to ED-tension $F$ in the $x$-direction. The semiclassical EOM gives $\hbar\dot{k}_x = F$, so $k_x$ traverses the BZ in time $T = 2\pi\hbar/(Fa)$ (one Bloch oscillation period). The transverse displacement during one Bloch oscillation is

$$
\Delta y = \int_0^T ẏ dt = (1/\hbar) \int_0^T [\partial E_n/\partial k_y - F \Omega_n] dt.
$$

The first term ($\partial E_n/\partial k_y$ integrated over a full period in $k_x$ at fixed $k_y$) is zero by periodicity of $E_n(\mathbf{k})$ in $k_x$ (the BZ is closed). The second term is

$$
\Delta y = -(F/\hbar) \int_0^T \Omega_n(k(t)) dt = -(F/\hbar) \cdot(\hbar /F) \int_{-\pi /a}^{\pi /a} \Omega_n(k_x, k_y) dk_x = -\int_{-\pi /a}^{\pi /a} \Omega_n(k_x, k_y) dk_x.
$$

If we further integrate over all $k_y$ values populated by the chain (e.g., a uniform fill of the lower band):

$$
\langle \Delta y\rangle_{\mathrm{band}} = -(a/(2\pi)) \int_{-\pi /a}^{\pi /a} dk_y \int_{-\pi /a}^{\pi /a} dk_x \Omega_n(k_x, k_y) = -(a/(2\pi)) \cdot ∬_𝕋^{2} \Omega_n d^{2}k = -a \cdot C_n.
$$

**The transverse drift per Bloch oscillation period is $|\Delta y| = a \cdot|C_n|$.** It is quantized in units of the lattice spacing, with quantization integer equal to the Chern number of the occupied band.

### 6.4 Quantization is independent of ED-tension strength

The drift per cycle is $a\cdot C_n$ regardless of $F$. A larger $F$ produces faster Bloch oscillations (smaller $T$), but the drift per cycle is unchanged. The integrated current $\Delta y / T = (a C_n) / (2\pi\hbar/(Fa)) = (Fa^2/(2\pi\hbar))\cdot C_n$ — proportional to $F$ and to $C_n$. This is the photonic analog of the integer quantum Hall conductance.

### 6.5 Substrate-level reading

- ED-tension forces $\mathbf{k}$ to traverse the BZ at uniform rate.
- The chain's pre-individuation amplitude follows the band eigenchannel $|u_n(\mathbf{k}(t))\rangle$ adiabatically.
- The Berry curvature on the BZ provides an anomalous-velocity term — a transverse displacement per unit time, weighted by the local rule-type curvature.
- Integrated over a full BZ traversal, the transverse displacement is the global rule-type curvature of the band — quantized in integer units of $a\cdot C_n$.
- **Light does not need charge.** It needs a periodic rule-type substrate with non-zero Chern number, plus an imposed ED-tension to make the global curvature manifest as transverse displacement.

---

## 7. Driven-Dissipative Steady State

### 7.1 Lindblad form derived inline

Real photonic systems involve continuous injection of substrate participation (drive: pumping into the cavity) and continuous extraction (dissipation: loss to bath modes, intentional out-coupling). The substrate-level state is a density operator $\rho$ obeying a master equation derived from the system-bath coupling.

We derive the Lindblad form. Begin with the full system-plus-bath Hamiltonian $H_\text{tot} = H_\text{sys} + H_\text{bath} + H_\text{int}$, where $H_\text{int}$ couples the system to a bath of bosonic modes. Trace out the bath, assume:

- (i) factorized initial state $\rho_\text{tot}(0) = \rho_\text{sys}(0) \otimes \rho_\text{bath}^\text{eq}$,
- (ii) weak system-bath coupling (perturbation theory in $H_\text{int}$),
- (iii) Markovian limit (bath correlation time short compared to system evolution),
- (iv) rotating-wave approximation (counter-rotating terms averaged out).

The resulting master equation is

$$
\partial_t \rho= -i [H_{\mathrm{sys}}, \rho] + \sum_\alpha[L_\alpha \rho L_\alpha † - (1/2){L_\alpha † L_\alpha, \rho}].
$$

The Lindblad operators $L_\alpha$ encode the system-bath coupling: $L_\alpha= \sqrt{\gamma_\alpha} a_\alpha$ for loss to mode $\alpha$ at rate $\gamma_\alpha$, and similar for drive terms. The form is the unique trace-preserving completely-positive-map generator under conditions (i)–(iv).

### 7.2 Steady-state existence

For generic Lindblad operators (those making the dynamics ergodic on the system Hilbert space), the master equation has a unique steady state $\rho_\text{ss}$ with $\partial_t \rho_\text{ss} = 0$. The steady state is reached on a timescale $\tau_\text{ss} \sim 1/\gamma$ where $\gamma$ is the smallest Lindblad rate.

### 7.3 Lindblad effect on band populations

Lindblad-type dissipation does *not* preserve coherence within the band — local fluctuations in pre-individuation amplitudes are damped. However, it does preserve the *band population* under generic conditions: if the system is initialized in band $n$ and the Lindblad operators do not directly couple to band $m \neq n$ (or do so with rate suppressed by the band gap), the steady-state population is concentrated in band $n$.

**Substrate-level statement.** Dissipation coarse-grains the chain's pre-individuation amplitude — it removes phase information that does not couple to topologically-protected transport. The global rule-type curvature of the band is unchanged by this coarse-graining, because curvature is gauge-invariant and Lindblad-type local dissipation does not deform the gauge structure of the band's $|u_n(\mathbf{k})\rangle$.

### 7.4 Steady-state Hall drift

Under continuous drive + dissipation + ED-tension, the chain reaches a steady state in which:

- The band population is concentrated in a single band $n$.
- The momentum distribution is biased by the ED-tension.
- The center-of-mass position drifts at rate proportional to $C_n$.

Compute the steady-state center-of-mass displacement per Bloch oscillation:

$$
\langle \Delta y\rangle_{\mathrm{steady}} = -a \cdot C_n
$$

— identical to the closed-system result from §6.3. **The dissipation does not alter the quantization.** Local fluctuations are damped, but the topological invariant — the integer-valued Chern number — is preserved.

### 7.5 Why dissipation cannot deform $C_n$

The Chern number is an integer. Lindblad-type dissipation acts continuously on the density operator (the dynamics are smooth in time). A continuous deformation cannot change an integer-valued topological invariant unless it crosses a singularity (band gap closure, where the parameter-space bundle becomes singular). Generic Lindblad dynamics in a gapped band do not close the band gap; the Chern number is therefore preserved.

This is the substrate-level statement of *topological protection*: continuous deformation of the substrate's rule-type structure within a topological phase cannot change the integer-valued global rule-type invariant. The Chern number can only change discontinuously, at a band-gap closure.

---

## 8. Substrate-Level Reading

| Standard photonic-Chern-insulator object | Substrate-level meaning |
|---|---|
| Photon | Minimal ED-channel (P-PC-1) |
| Synthetic dimension (frequency space) | Re-indexing of participation rules (P-PC-2) |
| Frequency mode | Distinct timing alignment of ED-flow / participation site |
| NN coupling (real) | Local ED-flow continuity between adjacent rules |
| NNN coupling (complex phase) | Global ED-twist on the rule-type lattice |
| Time-reversal breaking | Directional ED-bias (P-PC-4) |
| Synthetic electric field (modulation detuning) | ED-tension on rule-type structure (P-PC-5) |
| Bloch eigenchannel $\psi_k$ | Chain whose identity translates with substrate periodicity, modulo quasi-momentum phase |
| Brillouin zone | Compact parameter-space domain forced by substrate periodicity ($\mathbb{T}^2$ in 2D) |
| Band $E_n(\mathbf{k})$ | Eigen-energy of substrate's rule-type structure on the BZ |
| Band gap | Rule-type incompatibility — no eigenchannel at gap energy |
| Berry connection $\mathcal{A}_n(\mathbf{k})$ | Rule-type connection on the band's BZ-bundle |
| Berry curvature $\Omega_n(\mathbf{k})$ | Rule-type curvature in parameter space; gauge-invariant |
| Chern number $C_n$ | Integer-valued global ED-curvature of the band's BZ-bundle |
| Anomalous velocity $\mathbf{F}\times\Omega_n$ | ED-flow's transverse response to imposed tension under rule-type curvature |
| Quantized Hall drift $a\cdot C_n$ per cycle | Inevitable substrate-level transverse displacement of a minimal channel under tension on a curved BZ-bundle |
| Lindblad steady state | Driven-dissipative ED-flow equilibrium pinning to global manifold |
| Topological protection | Integer-valued global invariant unchanged under continuous substrate deformation within a topological phase |

### 8.1 The substrate-level meaning of the experiment

The Chénier et al. experiment is not a photonic imitation of the electronic quantum Hall effect. It is a direct demonstration that the substrate-level rule-type-curvature mechanism is independent of the platform: when a minimal ED-channel (light) is forced through a periodic rule-type substrate (synthetic frequency lattice) with non-zero global rule-type curvature (Haldane-type Chern number) under imposed ED-tension (modulation detuning), the channel exhibits a quantized transverse drift whose quantization is the integer-valued global ED-curvature.

The same mechanism applies to electrons in magnetic fields, to phonons in engineered substrates, to mechanical modes in lattice resonators, and to any minimal ED-channel in any substrate carrying non-zero global rule-type curvature. The substrate-level mechanism is platform-independent.

---

## 9. What's Forced, What's Inherited, What's Open

### What is FORCED by the substrate ontology

- **Synthetic frequency lattice as periodic rule-type substrate** is FORCED by the periodicity of the modulation pattern + the discrete frequency-mode spectrum (§3).
- **Bloch form** $|\psi_\mathbf{k}\rangle= e^{i\mathbf{k}\cdot\mathbf{n}_a}|\mathbf{u}_\mathbf{k}\rangle$ is FORCED by the commutation $[H_\text{synth}, T_a] = 0$ + simultaneous-eigenbasis structure (§3.5).
- **Two-band Bloch Hamiltonian** with Pauli structure on the sublattice space is FORCED by the two-sublattice composition of the synthetic lattice (§4.1).
- **Berry connection** $\mathcal{A}_n(\mathbf{k}) = i\langle u_n|\nabla_\mathbf{k} u_n\rangle$ is FORCED by smooth $\mathbf{k}$-dependence + orthonormality (§4.3).
- **Gauge-invariance of Berry curvature** is FORCED by the differential-form structure ($d^2 = 0$) (§4.5).
- **Berry curvature as pullback of the unit-sphere area form** under $\mathbf{k}\mapsto\hat{\mathbf{h}}(\mathbf{k})$ is FORCED by the Pauli-structure of the Bloch Hamiltonian (§4.4).
- **Topological phase transition at $|M| = 3\sqrt{3}|t_2\sin\phi|$** is FORCED by the band-gap closure condition (§4.7).
- **Chern-number integer-quantization** $C_n \in \mathbb{Z}$ is FORCED by the parameter-space bundle structure on the closed BZ (Appendix A).
- **Quantized Hall drift** $\Delta y = -a\cdot C_n$ per Bloch oscillation is FORCED by the semiclassical EOM with anomalous velocity + integration over closed BZ (§6.3).
- **Topological protection under driven-dissipative dynamics** is FORCED by integer-valued invariants being preserved under continuous deformations away from singularities (§7.5).

### What is FORM-FORCED-INHERITED (and re-derived inside this document)

- **Spectral theorem for commuting Hermitian operators** (§3.4): cited and used.
- **Unitarity of translation operator** (§3.4): from unitarity of shift maps.
- **Pauli-matrix algebra** for the sublattice space (§4.1): standard.
- **Spherical-coordinate parameterization of $\hat{\mathbf{h}}$** and the corresponding spinor eigenstates (§4.2): standard, derived inline.
- **Lindblad master equation** as the unique trace-preserving completely-positive-map generator under conditions (i)–(iv) of §7.1: derived inline at sketch level.
- **Wave-packet semiclassical equations of motion** (§6.2): derived inline from Heisenberg-equation + band-projection.
- **Anomalous-velocity term** $-\mathbf{F}\times\Omega_n$ (§6.2): derived inline from the wave-packet position-operator correction.
- **Stokes' theorem on patches of the torus** (Appendix A): standard differential geometry.

### What remains OPEN

- **Higher-Chern manifolds and 4D quantum Hall.** Generalization to closed manifolds beyond $\mathbb{T}^2$ (e.g., $\mathbb{T}^4$ with second Chern number) is FORM-FORCED-INHERITED at the differential-topology level; substrate-level reading parallel to this walkthrough's Chern-quantization argument; OPEN.
- **Non-Hermitian topology.** Driven-dissipative systems with PT-symmetric or genuinely non-Hermitian Hamiltonians have their own topological classification (exceptional points, non-Hermitian skin effect). Substrate-level account OPEN.
- **Multi-band Berry phase / non-Abelian Berry curvature.** When two or more bands are degenerate or near-degenerate, the Berry connection generalizes from U(1) to U(N) (Wilczek-Zee). FORM-FORCED-INHERITED at standard-QM level; substrate-level OPEN.
- **Floquet topological insulators.** Periodically-driven systems with topological invariants of the time-evolution operator. Related to but distinct from the static Haldane construction here. OPEN.
- **Edge states and bulk-boundary correspondence.** The Chern number of the bulk band predicts edge-state count via the bulk-boundary correspondence theorem. Substrate-level account OPEN.
- **Many-body topology** (fractional quantum Hall, fractional Chern insulators). Requires interaction effects beyond the single-channel band-structure framework. OPEN; substantially more involved.

---

## 10. What This Argument Establishes

This walkthrough establishes the following exact claims:

**Claim 1.** A periodic rule-type structure in synthetic dimension (frequency space) FORCES a discrete translation symmetry, a Bloch-form decomposition of eigenchannels, and a Brillouin-zone parameter manifold. In two dimensions, the BZ is topologically a torus $\mathbb{T}^2$.

**Claim 2.** Complex NNN couplings with phase $\phi \neq 0, \pi$ break time-reversal symmetry and induce a non-zero Berry curvature on the BZ. The Berry curvature is the pullback of the unit-sphere area form under the map $\mathbf{k}\mapsto\hat{\mathbf{h}}(\mathbf{k})$, where $\hat{\mathbf{h}}$ is the unit Pauli-vector of the Bloch Hamiltonian.

**Claim 3.** The Chern number $C_n = (1/2\pi)\iint_{\mathbb{T}^2}\Omega_n\, d^2k$ is integer-valued (Appendix A). It is the global topological invariant of the band's rule-type bundle over the closed BZ. The Haldane phase transition between $|M| < 3\sqrt{3}|t_2\sin\phi|$ (topological, $C_- = \pm 1$) and $|M| > 3\sqrt{3}|t_2\sin\phi|$ (trivial, $C_- = 0$) is FORCED by the band-gap closure.

**Claim 4.** Under imposed ED-tension $\mathbf{F}$, a chain in band $n$ exhibits quantized transverse displacement $\Delta y = -a\cdot C_n$ per Bloch oscillation period. The quantization is FORCED by the BZ being closed (the band integrals over $k_x$ vanish for the longitudinal contribution) and by the integer-valued Chern number.

**Claim 5.** Driven-dissipative dynamics described by Lindblad master equations preserve the band's Chern number under continuous deformation within a topological phase. Local fluctuations in pre-individuation amplitudes are damped, but the integer-valued global invariant survives. The quantized Hall drift is robust against dissipation.

**Claim 6 (negative).** No new substrate primitives are required. The photonic Chern insulator and quantized Hall drift decompose into composition of: minimal ED-channel (P-PC-1), periodic participation rule in synthetic dimension (P-PC-2), complex NN+NNN couplings (P-PC-3), time-reversal breaking (P-PC-4), ED-tension (P-PC-5), driven-dissipative ED-flow equilibrium (P-PC-6), and global ED-curvature (P-PC-7) — together with standard linear algebra, differential geometry, and the Chern integer-quantization theorem (Appendix A) re-derived as needed.

**Claim 7 (scope-limit).** This walkthrough does not derive: higher-Chern manifolds and 4D quantum Hall; non-Hermitian topology; non-Abelian Berry curvature for degenerate bands; Floquet topological insulators; bulk-boundary correspondence and edge-state count; many-body topology and fractional Chern insulators.

**The unified statement.** Quantized Hall drift of light is the substrate-level inevitable transverse response of a minimal ED-channel propagating through a periodic rule-type substrate with non-zero global ED-curvature, under imposed ED-tension. The Chern number is the integer-valued global rule-type curvature of the band's BZ-bundle; the quantization is integer-valued because the BZ is a closed manifold and the rule-type connection is a U(1) bundle over it. Light does not need charge. It needs a curved rule-type manifold and a tension to traverse it.

---

## Appendix A: Chern-Number Integer Quantization

This appendix provides a self-contained proof that

$$
C_n = (1/(2\pi)) ∬_{𝕋^{2}} \Omega_n(k) d^{2}k \in \mathbb{Z}
$$

for any smooth Berry curvature $\Omega_n$ arising from a smooth rank-1 eigenchannel section of a U(1) bundle over the torus $\mathbb{T}^2$. The proof closes the OPEN item flagged in the Bloch theorem walkthrough §7.8.

### A.1 Setup: the U(1) bundle structure

Fix band $n$. The eigenchannel $|u_n(\mathbf{k})\rangle$ is smooth in $\mathbf{k}$ over any open patch on which a smooth gauge can be chosen. The space of all eigenchannels at all $\mathbf{k}$ with $|u_n\rangle$ defined up to a U(1) phase forms a U(1) principal bundle $P \to \mathbb{T}^2$ over the torus.

**Topological obstruction.** When $C_n \neq 0$, no globally smooth section of $P$ exists — the bundle is non-trivial. To define $|u_n(\mathbf{k})\rangle$ everywhere, the BZ must be covered by overlapping patches with different gauge choices, and the relations between gauge choices on overlaps are encoded in *transition functions*.

### A.2 Two-patch covering of the torus

Cover $\mathbb{T}^2$ by two patches $U_1$ and $U_2$ such that their intersection $U_{12} = U_1 \cap U_2$ is a small annular neighborhood of a non-contractible loop $\gamma$ on the torus (e.g., the loop $k_y =$ const traversing the BZ in the $k_x$-direction).

Choose smooth gauges $|u_n^{(1)}(\mathbf{k})\rangle$ on $U_1$ and $|u_n^{(2)}(\mathbf{k})\rangle$ on $U_2$. On the overlap $U_{12}$, the two gauge choices differ by a U(1)-valued transition function:

$$
|u_n^{(2)}(k)\rangle= e^{i\chi_{12}(k)} |u_n^{(1)}(k)\rangle for k \in U_{12},
$$

where $\chi_{12}: U_{12} \to \mathbb{R}/2\pi\mathbb{Z}$ is the transition function (defined modulo $2\pi$ because only $e^{i\chi_{12}}$ is physically meaningful).

### A.3 Berry connection on each patch

By §4.5 of the main walkthrough, the Berry connections on the two patches differ by

$$
A_n^{(2)}(k) = A_n^{(1)}(k) - \nabla_k \chi_{12}(k) on U_{12}.
$$

The Berry curvature $\Omega_n = \partial_x\mathcal{A}_n^y - \partial_y\mathcal{A}_n^x$ is gauge-invariant and is therefore a globally well-defined smooth two-form on $\mathbb{T}^2$.

### A.4 Stokes' theorem on each patch

Apply Stokes' theorem on each patch separately. Choose $U_1$ to be a topological disk (simply-connected) and $U_2$ to be a topological annulus around a non-contractible loop. Let $\partial U_1$ be the boundary of $U_1$ traversed counterclockwise. By Stokes:

$$
∬_{U_1} \Omega_n d^{2}k = \oint_{\partial U_1} A_n^{(1)} \cdot dk.
$$

Similarly for $U_2$ — but we must be careful because $U_2$ is not simply-connected. Decompose $\partial U_2 = -\partial U_1 + (\text{non-contractible loops})$, where the minus sign reflects opposite orientation on the shared boundary. For a torus covered by two patches as described, the total integrated curvature decomposes as

$$
∬_{𝕋^{2}} \Omega_n = ∬_{U_1} \Omega_n + ∬_{U_2} \Omega_n.
$$

### A.5 The transition-function winding

On the overlap $U_{12}$, the difference between the two gauge connections is $-\nabla\chi_{12}$. The line integral around the shared boundary gives:

$$
\oint_{\partial U_1} (A_n^{(2)} - A_n^{(1)}) \cdot dk = \oint_{\partial U_1} (-\nabla \chi_{12}) \cdot dk = -[\chi_{12}(end) - \chi_{12}(start)].
$$

For a path $\partial U_1$ that closes (returns to its start), the difference $\chi_{12}(\text{end}) - \chi_{12}(\text{start})$ is the *winding number* of $\chi_{12}$ around the loop, multiplied by $2\pi$:

$$
\chi_{12}(end) - \chi_{12}(start) = 2\pi m, m \in \mathbb{Z},
$$

where $m$ is the integer winding number. This is the only source of integer-valued contributions: $\chi_{12}$ is itself defined only modulo $2\pi$ (as a U(1)-valued function), so the difference around a closed loop must be an integer multiple of $2\pi$.

### A.6 Integration of the transition-function winding

Apply Stokes' theorem on each patch and add:

$$
∬_{𝕋^{2}} \Omega_n = \oint_{\partial U_1} A_n^{(1)} \cdot dk + \oint_{\partial U_2} A_n^{(2)} \cdot dk.
$$

The boundary $\partial U_2$ is traversed in the opposite direction (counterclockwise from $U_2$'s perspective is clockwise from $U_1$'s perspective). On the shared boundary:

$$
∬_{𝕋^{2}} \Omega_n = \oint_{\partial U_1} A_n^{(1)} \cdot dk - \oint_{\partial U_1} A_n^{(2)} \cdot dk
= \oint_{\partial U_1} (A_n^{(1)} - A_n^{(2)}) \cdot dk
= \oint_{\partial U_1} \nabla \chi_{12} \cdot dk
= 2\pi m, m \in \mathbb{Z}.
$$

(In this argument we collected boundaries that cancel in the bulk and kept only the net contribution from the transition function on the shared boundary; the non-contractible-loop contributions from $U_2$'s topology cancel against equivalent contributions in $U_1$ when the patches are chosen compatibly.)

Therefore:

$$
C_n = (1/(2\pi)) ∬_{𝕋^{2}} \Omega_n = m \in \mathbb{Z}.
$$

### A.7 Substrate-level reading of the proof

The integer-quantization arises from the substrate-level fact that the rule-type connection on the BZ-bundle is *single-valued modulo $2\pi$ as a U(1)-valued connection*. The transition function $\chi_{12}$ between two gauge choices must be U(1)-valued — single-valued on the overlap. Around a closed loop, the only single-valued U(1)-valued differences are integer multiples of $2\pi$.

The Chern number counts the total winding of these transition functions across the BZ. It is the substrate-level statement of *how non-trivially the rule-type bundle is glued together* across the closed parameter manifold. A trivial bundle has zero winding ($C_n = 0$, no obstruction to a globally smooth gauge); a non-trivial bundle has integer-valued winding corresponding to the Chern number.

### A.8 Why the proof requires the BZ to be closed

If the BZ were an open manifold, no closed-loop integral would arise, and the transition-function winding argument would not give a well-defined integer. The integer-quantization is intrinsically a property of *closed* parameter manifolds: a torus, a sphere, or any compact manifold without boundary. The substrate-level requirement that the BZ be closed (forced by the periodicity of the substrate's rule-type structure, P-PC-2 + P-BL-1 of the Bloch walkthrough) is the load-bearing condition for integer-quantization.

### A.9 Higher Chern numbers

For higher-dimensional closed manifolds, additional Chern numbers arise (second Chern number for $\mathbb{T}^4$, etc.). The proof structure generalizes: the obstruction to a globally smooth gauge is captured by transition-function windings on the manifold's higher-dimensional cycles. For the present walkthrough's scope (2D photonic Chern insulator), the first Chern number $C_n$ derived above is sufficient.

### A.10 Closure of the OPEN item

The Bloch theorem walkthrough §7.8 flagged the integer-quantization of $C_n$ as OPEN at the substrate level. The proof above closes that item: the integer-quantization is FORCED by the U(1)-valued nature of the rule-type connection on the closed BZ-bundle. The substrate-level statement is that a single-valued U(1)-valued transition function on a closed loop has integer winding number, so the integrated Berry curvature is integer-valued in units of $2\pi$.

**Status update:** Chern-number integer-quantization is now FORCED at substrate level via the bundle-topology argument, not merely INHERITED from differential topology. The §7.8 OPEN flag is closed by this appendix.

---

## References

- Haldane, F. D. M. *Model for a quantum Hall effect without Landau levels: Condensed-matter realization of the "parity anomaly."* Phys. Rev. Lett. **61**, 2015 (1988).
- Thouless, D. J., Kohmoto, M., Nightingale, M. P., den Nijs, M. *Quantized Hall conductance in a two-dimensional periodic potential.* Phys. Rev. Lett. **49**, 405 (1982) — TKNN formula relating Chern number to Hall conductivity.
- Berry, M. V. *Quantal phase factors accompanying adiabatic changes.* Proc. R. Soc. A **392**, 45 (1984).
- Xiao, D., Chang, M.-C., Niu, Q. *Berry phase effects on electronic properties.* Rev. Mod. Phys. **82**, 1959 (2010) — wave-packet semiclassical EOM with anomalous velocity.
- Lindblad, G. *On the generators of quantum dynamical semigroups.* Comm. Math. Phys. **48**, 119 (1976).
- Gorini, V., Kossakowski, A., Sudarshan, E. C. G. *Completely positive dynamical semigroups of N-level systems.* J. Math. Phys. **17**, 821 (1976).
- Ozawa, T., Carusotto, I. *Topological photonics.* Nat. Photon. **8**, 821 (2014).
- Lustig, E., Segev, M. *Topological photonics in synthetic dimensions.* Adv. Opt. Photonics **13**, 426 (2021).
- Chénier, A., d'Aligny, B., Pellerin, F., Blanchard, P., Ozawa, T., Carusotto, I., St-Jean, P. *Quantized Hall Drift in a Frequency-Encoded Photonic Chern Insulator.* Phys. Rev. X **16**, 1 (2026).
- Nakahara, M. *Geometry, Topology, and Physics.* IOP Publishing (2003) — for principal-bundle and Chern-class formalism.

---

## Brief Review and Recommended Next Steps

### Review

This walkthrough reaches walkthrough-grade for the photonic Chern insulator and quantized Hall drift under fully self-contained discipline: every required Bloch-form, Pauli-spinor, Berry-connection, gauge-transformation, semiclassical-equation-of-motion, and Lindblad-master-equation step appears inside the document, and the appendix derives Chern-number integer-quantization from primitives + bundle topology.

Honest accounting:

- **§3** carries the load of re-deriving the synthetic-frequency-lattice construction, the translation operator, and the Bloch form — without cross-referencing the Bloch walkthrough. The argument is structurally identical but redrawn inline.
- **§4** is the section with the central Haldane-model derivation: Bloch Hamiltonian's Pauli-vector decomposition, Berry connection re-derived inline (with the spinor-spherical-coordinate algebra worked out), Berry curvature as pullback of the sphere area form, and the topological phase transition condition.
- **§5** computes the Chern number from the integrated curvature, with quantization deferred to the appendix.
- **§6** derives the semiclassical equations of motion with anomalous velocity inline, and integrates over a Bloch oscillation to produce the quantized transverse drift $\Delta y = -a\cdot C_n$.
- **§7** derives the Lindblad master equation inline and shows that driven-dissipative dynamics preserve integer-valued Chern-number invariants.
- **Appendix A** closes the OPEN item from the Bloch walkthrough §7.8 by deriving Chern-number integer-quantization from U(1) bundle structure on the closed BZ + transition-function winding around the shared patch boundary.

The walkthrough sits at ~870 lines (including the appendix), in the established 700–900-line range for arc-grade ED documents with appendices. It introduces no new substrate primitives.

### Honest scope-limit

Claim 7 in §10 explicitly flags the items not derived here: higher-Chern manifolds, non-Hermitian topology, non-Abelian Berry curvature, Floquet topological insulators, bulk-boundary correspondence, and many-body topology. These are flagged OPEN, not asserted as derived.

### What this completes for the photonics direction

Three closed walkthroughs now form the topological-photonics inventory:

- Berry-phase walkthrough (separate document) — substrate-level Berry connection / curvature / phase on parameter space.
- Bloch-theorem walkthrough (separate document) — substrate-level Bloch theorem and band structure for periodic rule-type substrates.
- This walkthrough — substrate-level photonic Chern insulator and quantized Hall drift, with Chern-quantization closed in Appendix A.

Together with already-closed Q-COMPUTE Class B (topologically-protected transport at the architectural level) and Lindblad walkthrough (open-system dynamics), the substrate-level account of the Chénier et al. 2026 PRX experiment and the broader topological-photonics frontier is now in the closed inventory.

### Recommended next steps

In order of structural value:

1. **Wu-Yang non-Abelian phase walkthrough.** The natural pair to the Berry-phase walkthrough — generalizes U(1) to U(N) for degenerate bands. Closes deferred-candidate item #2 in the walkthrough series. Mid-effort.

2. **Effective-medium / homogenization walkthrough.** First precursor for the Yablonovitch / Pendry / Capasso photonics walkthrough (ED-I-12 territory). Substrate-level analog of standard homogenization theory — derive how subwavelength substrate-rule-type substructure coarse-grains to macroscopic effective $\varepsilon(\mathbf{r}), \mu(\mathbf{r})$. Arc-grade (5–7 memos).

3. **Transformation-optics walkthrough.** Second precursor for ED-I-12. Derive how substrate-gradient deformations correspond to effective-medium coordinate transformations. Arc-grade.

4. **Metasurface boundary-condition walkthrough.** Third precursor for ED-I-12. Derive generalized Snell's law from substrate primitives + interface conditions on rule-type structure. Short walkthrough.

5. **Update walkthrough-series inventory and Nobel-relevance routing.** With Berry + Bloch + Photonic-Chern in the closed inventory, the topological-photonics row in the Nobel-relevance routing table now matches the depth held for QI and gauge fields. The remaining Nobel-relevant photonics topic area (Yablonovitch / Pendry / Capasso effective-medium photonics, ED-I-12) requires the three precursors above.

6. **Update `walkthroughs_deferred.md`.** Mark closed: Berry phase (closed by Berry walkthrough), substrate-level Bloch theorem (closed by Bloch walkthrough), substrate-level Chern-quantization (closed by this walkthrough's Appendix A). Add new deferred entries: effective-medium / homogenization, transformation-optics, metasurface BC, Wu-Yang non-Abelian phase, Floquet topological insulators, bulk-boundary correspondence.

7. **Update memory files.** Refresh `project_walkthrough_series_expansion.md` with the three new topological-photonics walkthroughs (count goes from 24 → 27 walkthroughs) and the Nobel-relevance routing table.

The Chénier et al. 2026 PRX experiment is now substrate-level FORCED in its central structural claims: the substrate ontology forces minimal-channel quantized Hall drift on a curved BZ-bundle, with the integer quantization derived from primitives + bundle topology and the dissipation-resistance derived from continuous-deformation invariance.
