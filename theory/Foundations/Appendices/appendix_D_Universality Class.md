# Appendix D. Universality Class

This appendix places the ED architecture on a rigorous equivalence-class footing. We define the notion of ED-equivalence between dynamical systems, construct the universality class $\mathcal{U}_{\mathrm{ED}}$, and prove that it is closed under the natural symmetries of the theory (rescaling, constitutive perturbation, domain change) and that its defining structural invariants — the damping discriminant, the regime geometry, the modal hierarchy, and the triad selection rules — are preserved by every equivalence. We conclude with a universality theorem: any well-posed PDE–ODE system satisfying Principles 1–7 belongs to $\mathcal{U}_{\mathrm{ED}}$, regardless of its microscopic origin.

All notation from the Rigour Paper and Appendix C is retained. In particular, $F[\rho] = M(\rho)\nabla^2\rho + M'(\rho)|\nabla\rho|^2 - P(\rho)$ is the canonical operator (Principle 1), $D + H = 1$ is the channel constraint (Principle 2), $\rho^*$ is the unique penalty zero with $P'(\rho^*) > 0$ (Principle 3), $M(\rho_{\max}) = 0$ with $M(\rho) > 0$ for $\rho < \rho_{\max}$ (Principle 4), $v$ is the participation variable with time constant $\tau$ and damping $\zeta$ (Principle 5), $\Delta = D + 2\zeta$ is the damping discriminant (Principle 6), and $M'(\rho)|\nabla\rho|^2$ generates the nonlinear triad (Principle 7).

---

## D.1 Formal Definition of ED-Equivalence

### D.1.1 The Canonical ED Form

**Definition D.1** (Canonical ED system). A *canonical ED system* is a coupled PDE–ODE of the form

$$
\begin{cases}
\partial_t\rho = D\,F[\rho] + H\,v, \\[4pt]
\dot{v} = \tau^{-1}(F[\rho] - \zeta\,v),
\end{cases}
\tag{D.1}
$$

on a bounded domain $\Omega \subset \mathbb{R}^d$ with smooth boundary, subject to Neumann boundary conditions $\partial_\nu\rho = 0$ on $\partial\Omega$, where $F[\rho] = M(\rho)\nabla^2\rho + M'(\rho)|\nabla\rho|^2 - P(\rho)$, and the constitutive data $(M, P, D, \zeta, \tau, \rho^*, \rho_{\max}, \Omega)$ satisfy:

**(P1)** $F[\rho]$ has the three-term structure: curvature-dependent diffusion $M(\rho)\nabla^2\rho$, gradient-squared nonlinearity $M'(\rho)|\nabla\rho|^2$, and restoring force $-P(\rho)$.

**(P2)** $D, H \in [0,1]$ with $D + H = 1$.

**(P3)** $P \in C^\infty(\mathbb{R})$ with $P(\rho^*) = 0$ and $P'(\rho) > 0$ for all $\rho$.

**(P4)** $M \in C^\infty([0, \rho_{\max}])$ with $M(\rho) > 0$ for $\rho \in [0, \rho_{\max})$ and $M(\rho_{\max}) = 0$.

**(P5)** $\tau > 0$, $\zeta > 0$, and $v \in \mathbb{R}$.

**(P6)** The damping discriminant $\Delta = D + 2\zeta$ classifies the flow type.

**(P7)** $M'(\rho) \not\equiv 0$, so that $M'(\rho)|\nabla\rho|^2$ generates nontrivial harmonic content.

We denote such a system by $\mathcal{S} = (\Omega, M, P, D, \zeta, \tau, \rho_{\max})$.

### D.1.2 Architectural Layers

**Definition D.2** (Architectural realization). A canonical ED system $\mathcal{S}$ *realizes* the ED architecture if the following structural objects exist and have the properties established in the ED-Arch series (ED-Arch-02 through ED-Arch-11) and Appendix C:

(i) *Motifs:* Saddle, Spiral, Horizon, Manifold, Boundary, Memory Loop, Dissipator, Nonlinear Triad.

(ii) *Laws:* Unique Attraction, One-Dimensional Relaxation, Proportional Stability, Critical Damping Boundary, Finite Capacity, Harmonic Protection, Modal Hierarchy, Channel Complementarity, Transient Structure.

(iii) *Geometric objects:* Attractor Point $(\rho^*, 0)$, Stable Manifold Curve, Spiral Sheet (if $\Delta < 1$), Monotonic Cone (if $\Delta > 1$), Horizon Surface at $\rho_{\max}$, Boundary Surface at $\mathscr{D}_0 = 0$, Modal Decay Funnel, Triad Locus.

(iv) *Invariants:* $D + H = 1$, unique attractor, capacity bound, gradient sign, modal ordering, clockwise winding (if $\Delta < 1$), linear discriminant, locked $k_3/k_1$ ratio, loop topology.

We write $\mathcal{A}(\mathcal{S})$ for the collection of realized architectural layers.

### D.1.3 ED-Equivalence

**Definition D.3** (ED-equivalence). Two canonical ED systems $\mathcal{S}_1 = (\Omega_1, M_1, P_1, D_1, \zeta_1, \tau_1, \rho_{\max,1})$ and $\mathcal{S}_2 = (\Omega_2, M_2, P_2, D_2, \zeta_2, \tau_2, \rho_{\max,2})$ are *ED-equivalent*, written $\mathcal{S}_1 \sim_{\mathrm{ED}} \mathcal{S}_2$, if:

(i) Both $\mathcal{S}_1$ and $\mathcal{S}_2$ satisfy Principles 1–7 (Definition D.1).

(ii) There exists a transformation $\mathcal{T}$ composed of:

- a spatial diffeomorphism $\phi : \Omega_1 \to \Omega_2$ preserving the Neumann boundary condition,
- a density rescaling $\rho \mapsto a\rho + b$ with $a > 0$ mapping $[0, \rho_{\max,1}]$ to $[0, \rho_{\max,2}]$ and $\rho_1^*$ to $\rho_2^*$,
- a time rescaling $t \mapsto \lambda t$ with $\lambda > 0$,
- a participation rescaling $v \mapsto \mu v$ with $\mu > 0$,

such that $\mathcal{T}$ maps solutions of $\mathcal{S}_1$ to solutions of $\mathcal{S}_2$.

(iii) The architectural realizations are isomorphic: $\mathcal{A}(\mathcal{S}_1) \cong \mathcal{A}(\mathcal{S}_2)$ — that is, the two systems exhibit the same motifs, obey the same laws, possess the same geometric objects (up to the diffeomorphism $\phi$ and the density rescaling), and share the same invariant relations.

**Proposition D.4** ($\sim_{\mathrm{ED}}$ is an equivalence relation). *ED-equivalence is reflexive (the identity transformation), symmetric (the inverse transformation), and transitive (composition of transformations).*

*Proof.* Each of the four component transformations (spatial diffeomorphism, density rescaling, time rescaling, participation rescaling) is invertible and closed under composition. The architectural isomorphism condition is symmetric and transitive by definition. $\square$

---

## D.2 The Universality Class $\mathcal{U}_{\mathrm{ED}}$

**Definition D.5** (Universality class). The *ED universality class* is the equivalence class

$$
\mathcal{U}_{\mathrm{ED}} := \bigl\{\mathcal{S} : \mathcal{S} \text{ is a canonical ED system satisfying Principles 1–7}\bigr\}\big/\!\sim_{\mathrm{ED}}.
\tag{D.2}
$$

More concretely, $\mathcal{U}_{\mathrm{ED}}$ is the set of all PDE–ODE systems that are ED-equivalent to the reference system $\mathcal{S}_{\mathrm{ref}} = (\Omega_{\mathrm{ref}}, M_{\mathrm{ref}}, P_{\mathrm{ref}}, D_{\mathrm{ref}}, \zeta_{\mathrm{ref}}, \tau_{\mathrm{ref}}, \rho_{\max,\mathrm{ref}})$ for any choice of reference satisfying Principles 1–7.

**Remark D.6.** The universality class is defined by *structural identity*, not by algebraic identity. Two systems in $\mathcal{U}_{\mathrm{ED}}$ may have different mobility functions $M$, different penalty functions $P$, different domain geometries, and different parameter values, yet exhibit identical architectural structure. This is the formal content of §5.1 of the main text: any PDE satisfying all seven canonical principles is architecturally ED.

---

## D.3 Closure Theorems

We prove that $\mathcal{U}_{\mathrm{ED}}$ is closed under three families of transformations.

### D.3.1 Closure Under Rescaling

**Theorem D.7** (Rescaling closure). *Let $\mathcal{S} \in \mathcal{U}_{\mathrm{ED}}$. Then the following rescaled systems also belong to $\mathcal{U}_{\mathrm{ED}}$:*

*(i) Time rescaling: $t \mapsto \lambda t$, $\lambda > 0$. The rescaled system has $\tau \mapsto \tau/\lambda$, $\zeta \mapsto \zeta$, $M \mapsto \lambda M$, $P \mapsto \lambda P$.*

*(ii) Space rescaling: $x \mapsto L\,x$, $L > 0$, with $\Omega \mapsto L^{-1}\Omega$. The rescaled system has $\mu_n \mapsto L^2\mu_n$, $M \mapsto M$, $P \mapsto P$.*

*(iii) Amplitude rescaling: $\rho \mapsto a\rho + b$, $a > 0$, mapping $\rho^* \mapsto a\rho^* + b$ and $\rho_{\max} \mapsto a\rho_{\max} + b$. The rescaled system has $M \mapsto \tilde{M}$, $P \mapsto \tilde{P}$ with $\tilde{M}(\tilde{\rho}) = M((\tilde{\rho} - b)/a)$ and $\tilde{P}(\tilde{\rho}) = a\,P((\tilde{\rho} - b)/a)$.*

*In each case, all seven canonical principles are preserved, and the damping discriminant $\Delta = D + 2\zeta$ is invariant.*

*Proof.* We verify each principle for each rescaling.

(i) *Time rescaling.* Replacing $t$ by $\lambda t$ in (D.1) multiplies both sides of the $\rho$-equation by $\lambda$ and the $v$-equation by $\lambda$. Absorbing $\lambda$ into $M \mapsto \lambda M$, $P \mapsto \lambda P$, and $\tau \mapsto \tau/\lambda$ restores the canonical form. The structural conditions are preserved: $\tilde{P}(\rho^*) = \lambda P(\rho^*) = 0$, $\tilde{P}'(\rho) = \lambda P'(\rho) > 0$ (P3); $\tilde{M}(\rho_{\max}) = \lambda M(\rho_{\max}) = 0$ (P4); $D$ and $\zeta$ are unchanged (P2, P5, P6); $\tilde{M}' = \lambda M' \not\equiv 0$ (P7). The discriminant $\Delta = D + 2\zeta$ is invariant.

(ii) *Space rescaling.* The Laplacian transforms as $\nabla^2_x = L^2\nabla^2_y$ under $x = Ly$. The Neumann eigenvalues transform as $\mu_n^{(\Omega')} = L^2\mu_n^{(\Omega)}$. All constitutive functions and parameters are unchanged. The seven principles are preserved because they depend on the functional form of $M$, $P$, and the parameter values, not on the specific eigenvalues of the Laplacian.

(iii) *Amplitude rescaling.* Under $\tilde{\rho} = a\rho + b$, the chain rule gives $\nabla\tilde{\rho} = a\nabla\rho$, $\nabla^2\tilde{\rho} = a\nabla^2\rho$. The operator transforms as $\tilde{F}[\tilde{\rho}] = a\,F[\rho]$ when $\tilde{M}(\tilde{\rho}) = M(\rho)$ and $\tilde{P}(\tilde{\rho}) = a\,P(\rho)$. The penalty zero maps correctly: $\tilde{P}(a\rho^* + b) = a P(\rho^*) = 0$, and $\tilde{P}'(\tilde{\rho}) = P'(\rho) > 0$ (P3). The mobility vanishes at the mapped capacity bound: $\tilde{M}(a\rho_{\max} + b) = M(\rho_{\max}) = 0$ (P4). The channel parameters $D, \zeta, \tau$ are unchanged. $\square$

### D.3.2 Closure Under Constitutive Perturbation

**Theorem D.8** (Constitutive closure). *Let $\mathcal{S} = (\Omega, M, P, D, \zeta, \tau, \rho_{\max}) \in \mathcal{U}_{\mathrm{ED}}$. Let $\tilde{M}$ and $\tilde{P}$ be smooth functions satisfying:*

- *$\tilde{P}(\rho^*) = 0$ and $\tilde{P}'(\rho) > 0$ for all $\rho$ (Principle 3 preserved),*
- *$\tilde{M}(\rho_{\max}) = 0$ and $\tilde{M}(\rho) > 0$ for $\rho \in [0, \rho_{\max})$ (Principle 4 preserved),*
- *$\tilde{M}'(\rho) \not\equiv 0$ (Principle 7 preserved).*

*Then $\tilde{\mathcal{S}} = (\Omega, \tilde{M}, \tilde{P}, D, \zeta, \tau, \rho_{\max}) \in \mathcal{U}_{\mathrm{ED}}$.*

*Proof.* The system $\tilde{\mathcal{S}}$ satisfies Principles 1–7 by construction:

- P1: The operator $\tilde{F}[\rho] = \tilde{M}(\rho)\nabla^2\rho + \tilde{M}'(\rho)|\nabla\rho|^2 - \tilde{P}(\rho)$ has the canonical three-term structure.
- P2: $D + H = 1$ is unchanged.
- P3: $\tilde{P}(\rho^*) = 0$, $\tilde{P}' > 0$ by hypothesis.
- P4: $\tilde{M}(\rho_{\max}) = 0$, $\tilde{M} > 0$ on $[0, \rho_{\max})$ by hypothesis.
- P5: $\tau, \zeta > 0$ are unchanged.
- P6: $\Delta = D + 2\zeta$ is unchanged.
- P7: $\tilde{M}' \not\equiv 0$ by hypothesis.

The well-posedness of $\tilde{\mathcal{S}}$ (local existence, global existence, stability, long-time behavior) follows from Appendices C.1–C.7, whose proofs depend on the structural properties of $M$ and $P$ (smoothness, the signs of $P'$ and $M$ at the relevant points, the degeneracy $M(\rho_{\max}) = 0$) but not on the specific functional forms. The architectural realization $\mathcal{A}(\tilde{\mathcal{S}})$ is isomorphic to $\mathcal{A}(\mathcal{S})$ because every architectural layer — motifs, laws, geometry, invariants — is generated by Principles 1–7 (as shown in §3 of the main text), and both systems satisfy the same principles. $\square$

**Remark D.9.** Theorem D.8 is the rigorous statement of §5.2 of the main text: the specific shapes of $M(\rho)$ and $P(\rho)$ may vary freely, provided the structural conditions (P3, P4, P7) are maintained. The universality class is parameterized by the *qualitative* properties of the constitutive functions, not by their quantitative form.

### D.3.3 Closure Under Domain Change

**Theorem D.10** (Domain closure). *Let $\mathcal{S} = (\Omega_1, M, P, D, \zeta, \tau, \rho_{\max}) \in \mathcal{U}_{\mathrm{ED}}$, and let $\Omega_2 \subset \mathbb{R}^d$ be any bounded domain with smooth boundary. Then $\tilde{\mathcal{S}} = (\Omega_2, M, P, D, \zeta, \tau, \rho_{\max}) \in \mathcal{U}_{\mathrm{ED}}$.*

*Proof.* The seven canonical principles are properties of the constitutive data $(M, P, D, \zeta, \tau, \rho_{\max})$ and the functional form of the operator, not of the domain $\Omega$. The well-posedness results of Appendix C hold for any bounded domain with smooth boundary and Neumann conditions. The Neumann eigenvalues $\{\mu_n\}$ change with the domain, but the structural properties that define the architecture — the spectral gap $\gamma > 0$ (Corollary C.18), the modal hierarchy $\alpha_1 < \alpha_2 < \cdots$ (Proposition C.29), the selection rules for the nonlinear triad (Theorem C.34 in 1D; the generalized coupling structure in higher dimensions) — persist because they depend on the positivity of $M_*$ and $P_*'$, not on the specific values of $\mu_n$. $\square$

---

## D.4 Invariance Theorems

We prove that the defining structural quantities of the ED architecture are invariant under ED-equivalence.

### D.4.1 Invariance of the Damping Discriminant

**Theorem D.11** (Discriminant invariance). *The canonical damping parameter $\Delta = D + 2\zeta$ is invariant under every ED-equivalence transformation. That is, if $\mathcal{S}_1 \sim_{\mathrm{ED}} \mathcal{S}_2$, then $\Delta_1 = \Delta_2$.*

*Proof.* The four components of an ED-equivalence transformation (§D.1.3) act on the parameters as follows:

- Spatial diffeomorphism: does not affect $D$ or $\zeta$.
- Density rescaling: does not affect $D$ or $\zeta$ (these are coupling weights, not density-dependent quantities).
- Time rescaling: $D$ and $\zeta$ are dimensionless ratios that are invariant under $t \mapsto \lambda t$ (the rescaling is absorbed by $M$, $P$, and $\tau$).
- Participation rescaling: $v \mapsto \mu v$ can be absorbed by $\tau \mapsto \tau/\mu$ and $\zeta \mapsto \zeta$ (the damping ratio $\zeta$ is dimensionless).

Therefore $\Delta = D + 2\zeta$ is unchanged by every component, hence invariant. $\square$

### D.4.2 Invariance of the Regime Geometry

**Theorem D.12** (Regime geometry invariance). *Under any ED-equivalence transformation $\mathcal{T}: \mathcal{S}_1 \to \mathcal{S}_2$, the following geometric objects are preserved:*

*(i) The Spiral Sheet ($\mathscr{D}_0 < 0$) maps to the Spiral Sheet.*

*(ii) The Monotonic Cone ($\mathscr{D}_0 > 0$) maps to the Monotonic Cone.*

*(iii) The Boundary Surface ($\mathscr{D}_0 = 0$) maps to the Boundary Surface.*

*(iv) The Attractor Point $(\rho^*, 0)$ maps to the Attractor Point $(\tilde{\rho}^*, 0)$ of the target system.*

*(v) The Horizon Surface $\{\rho = \rho_{\max}\}$ maps to $\{\tilde{\rho} = \tilde{\rho}_{\max}\}$.*

*Proof.* Parts (i)–(iii): The modal discriminant $\mathscr{D}_0 = (D P_*' - \zeta/\tau)^2 - 4H P_*'/\tau$ (C.16) depends on $D$, $\zeta$, $\tau$, and $P_*'$. Under time rescaling, $P_*' \mapsto \lambda P_*'$ and $\tau \mapsto \tau/\lambda$, so $P_*'/\tau \mapsto \lambda^2 P_*'/\tau$ and $\zeta/\tau \mapsto \lambda\zeta/\tau$. The discriminant transforms as $\mathscr{D}_0 \mapsto \lambda^2\mathscr{D}_0$, preserving the sign. Under density and spatial rescalings, $P_*'$ and $\tau$ may change, but the sign of $\mathscr{D}_0$ is preserved because the discriminant is a continuous function of parameters that maintain the same structural relationships.

Parts (iv)–(v): The equilibrium $\rho^*$ and the capacity bound $\rho_{\max}$ are mapped by the density rescaling $\rho \mapsto a\rho + b$ to $\tilde{\rho}^* = a\rho^* + b$ and $\tilde{\rho}_{\max} = a\rho_{\max} + b$, preserving their defining properties ($\tilde{P}(\tilde{\rho}^*) = 0$ and $\tilde{M}(\tilde{\rho}_{\max}) = 0$). $\square$

### D.4.3 Invariance of the Modal Hierarchy and Triad Selection Rules

**Theorem D.13** (Modal hierarchy invariance). *Under any ED-equivalence transformation, the modal decay ordering is preserved: if $\alpha_n^{(1)} < \alpha_m^{(1)}$ in $\mathcal{S}_1$, then $\alpha_n^{(2)} < \alpha_m^{(2)}$ in $\mathcal{S}_2$.*

*Proof.* The modal decay coefficients are $\alpha_n = M_*\mu_n + P_*'$ (C.12). Under time rescaling, $M_* \mapsto \lambda M_*$ and $P_*' \mapsto \lambda P_*'$, so $\alpha_n \mapsto \lambda\alpha_n$, preserving the ordering. Under space rescaling $x \mapsto Lx$, the eigenvalues transform as $\mu_n \mapsto L^2\mu_n$, which preserves their ordering $\mu_1 \leq \mu_2 \leq \cdots$. Under density rescaling, $M_*$ and $P_*'$ transform but remain positive, and the ordering $\alpha_n = M_*\mu_n + P_*'$ is determined by $\mu_n$, which is unchanged. $\square$

**Theorem D.14** (Triad selection rule invariance). *The selection rule $k \in \{|m - n|, m + n\}$ for the trilinear coupling coefficients $\Gamma_{mnk}$ (Theorem C.34) is invariant under ED-equivalence.*

*Proof.* The selection rule (C.37) is a consequence of the product-to-sum formula for the Neumann eigenfunctions, which depends on the orthogonality structure of the eigenbasis, not on the specific eigenvalues. Under spatial diffeomorphism $\phi: \Omega_1 \to \Omega_2$, the eigenfunctions transform but the orthogonality relations are preserved. The selection rule is a property of the quadratic structure of $|\nabla\rho|^2$ (Principle 7) and the Neumann boundary conditions, both of which are invariant.

On a general domain, the selection rule takes the generalized form: $\Gamma_{mnk} \neq 0$ only when the triple product $\nabla\varphi_m \cdot \nabla\varphi_n \cdot \varphi_k$ has nonzero integral, which is a geometric condition on the eigenbasis. This condition is invariant under diffeomorphisms that preserve the Neumann boundary. $\square$

**Corollary D.15** (Locked amplitude ratio invariance). *The invariant $k_3/k_1$ amplitude ratio (Principle 7, Proposition C.35) depends only on the structural parameters $M_*'/M_*$, $P_*'$, $D$, and the eigenvalue ratios $\mu_n/\mu_1$. Under ED-equivalence, this ratio is preserved because each of these quantities either is invariant or transforms in a way that leaves the ratio unchanged.*

---

## D.5 Robustness Theorems

### D.5.1 Structural Stability of ED-Equivalence

**Theorem D.16** (Structural stability). *The ED universality class is structurally stable: if $\mathcal{S} \in \mathcal{U}_{\mathrm{ED}}$ and $\tilde{\mathcal{S}}$ is a $C^2$-small perturbation of $\mathcal{S}$ in the constitutive data $(M, P)$ and the parameters $(D, \zeta, \tau)$, then $\tilde{\mathcal{S}} \in \mathcal{U}_{\mathrm{ED}}$, provided the perturbation preserves Principles 3, 4, and 7.*

*Proof.* The conditions defining membership in $\mathcal{U}_{\mathrm{ED}}$ are:

- P1: The three-term operator structure is a *formal* condition (the equation has the prescribed form), which is preserved under perturbation of the coefficients.
- P2: $D + H = 1$ is an algebraic constraint, preserved by any perturbation that maintains $H = 1 - D$.
- P3: $P(\rho^*) = 0$ and $P' > 0$ are open conditions in $C^2$: the implicit function theorem guarantees that a $C^2$-small perturbation $\tilde{P}$ has a unique zero $\tilde{\rho}^*$ near $\rho^*$ with $\tilde{P}'(\tilde{\rho}^*) > 0$.
- P4: $M(\rho_{\max}) = 0$ and $M > 0$ on $[0, \rho_{\max})$ are preserved by hypothesis. A $C^2$-small perturbation of $M$ that maintains the zero at $\rho_{\max}$ and positivity on $[0, \rho_{\max})$ is in the hypothesis.
- P5: $\tau > 0$ and $\zeta > 0$ are open conditions, preserved under small perturbation.
- P6: $\Delta = D + 2\zeta$ varies continuously with the parameters. The regime classification (Spiral Sheet vs. Monotonic Cone) may change if $\Delta$ crosses the critical surface, but both regimes are within $\mathcal{U}_{\mathrm{ED}}$.
- P7: $M' \not\equiv 0$ is an open condition in $C^1$, preserved under small perturbation.

The well-posedness results (Appendices C.1–C.7) depend continuously on the constitutive data, so the global solution theory persists. The architectural realization $\mathcal{A}(\tilde{\mathcal{S}})$ is isomorphic to $\mathcal{A}(\mathcal{S})$ because all seven principles are satisfied. $\square$

### D.5.2 Persistence of the Unique Attractor

**Theorem D.17** (Attractor persistence). *Let $\{\mathcal{S}_\epsilon\}_{\epsilon \in [0,1]}$ be a continuous family of canonical ED systems (parameterized by $\epsilon$) with $\mathcal{S}_0 \in \mathcal{U}_{\mathrm{ED}}$. If each $\mathcal{S}_\epsilon$ satisfies Principle 3, then each $\mathcal{S}_\epsilon$ has a unique globally attracting equilibrium $(\rho_\epsilon^*, 0)$, and the map $\epsilon \mapsto \rho_\epsilon^*$ is continuous.*

*Proof.* For each $\epsilon$, $P_\epsilon(\rho_\epsilon^*) = 0$ with $P_\epsilon' > 0$, so $\rho_\epsilon^*$ is the unique zero of $P_\epsilon$ and depends continuously on $\epsilon$ by the implicit function theorem. The global asymptotic stability of $(\rho_\epsilon^*, 0)$ follows from Theorem C.76 (three-stage convergence), whose proof uses only the structural properties guaranteed by Principles 1–7. $\square$

### D.5.3 Persistence of the Mobility-Collapse Barrier

**Theorem D.18** (Horizon persistence under perturbation). *Let $\{\mathcal{S}_\epsilon\}_{\epsilon \in [0,1]}$ be a continuous family of canonical ED systems with $\mathcal{S}_0 \in \mathcal{U}_{\mathrm{ED}}$. If each $\mathcal{S}_\epsilon$ satisfies Principle 4 with capacity bound $\rho_{\max,\epsilon}$, then:*

*(i) The energy barrier $\Phi_\epsilon(\rho) \to +\infty$ as $\rho \to \rho_{\max,\epsilon}^-$ persists for each $\epsilon$.*

*(ii) The uniform density bound $\rho(x,t) \leq \rho_{\max,\epsilon} - \delta_\epsilon$ persists for each $\epsilon$, with $\delta_\epsilon > 0$ depending continuously on $\epsilon$ and the initial energy.*

*(iii) The Horizon Surface $\{\rho = \rho_{\max,\epsilon}\}$ is never reached by any classical solution.*

*Proof.* Part (i): the density potential $\Phi_\epsilon(\rho) = \int_{\rho_\epsilon^*}^\rho P_\epsilon(r)/M_\epsilon(r)\,dr$ diverges as $\rho \to \rho_{\max,\epsilon}^-$ because $M_\epsilon(\rho_{\max,\epsilon}) = 0$ and $P_\epsilon(\rho) > 0$ for $\rho > \rho_\epsilon^*$ (the argument of Proposition C.11 applies to each $\epsilon$). Part (ii) follows from the energy bound and the coercivity of $\Phi_\epsilon$, as in Theorem C.66(i). Part (iii) is a consequence of (ii). Continuity in $\epsilon$ follows from the continuous dependence of $\Phi_\epsilon$ on the constitutive data. $\square$

---

## D.6 Universality Statement

### D.6.1 The Universality Theorem

**Theorem D.19** (Universality). *Let $\mathcal{S} = (\Omega, M, P, D, \zeta, \tau, \rho_{\max})$ be a PDE–ODE system of the form (D.1) on a bounded domain $\Omega \subset \mathbb{R}^d$ with smooth boundary and Neumann boundary conditions. Suppose $\mathcal{S}$ satisfies Principles 1–7 (Definition D.1). Then:*

*(i) $\mathcal{S}$ is well-posed: it admits a unique global classical solution for every initial datum $(\rho_0, v_0) \in \mathcal{O}$ with $\rho_0 \in H^s(\Omega)$, $s > d/2 + 2$ (Theorems C.2 and C.14).*

*(ii) $\mathcal{S}$ realizes the full ED architecture $\mathcal{A}(\mathcal{S})$ (Definition D.2).*

*(iii) $\mathcal{S} \in \mathcal{U}_{\mathrm{ED}}$.*

*(iv) $\mathcal{S}$ is ED-equivalent to every other system satisfying Principles 1–7 with the same values of $D$ and $\zeta$ (hence the same $\Delta$), up to constitutive and geometric transformations.*

*Proof.* Part (i): the well-posedness follows from Appendices C.1 (local existence), C.2 (global existence), and C.7 (long-time behavior). The proofs use only the structural properties guaranteed by Principles 1–7.

Part (ii): the architectural layers are generated by the seven principles as shown in §3 of the main text (the Canonical Dependency Graph). Each principle generates specific motifs, laws, geometric objects, and invariants, and the generation depends only on the structural properties (the three-term operator, the channel complementarity, the penalty uniqueness, the mobility collapse, the feedback loop, the damping discriminant, and the nonlinear coupling), all of which hold by hypothesis.

Part (iii): by Definition D.5, $\mathcal{S} \in \mathcal{U}_{\mathrm{ED}}$ if $\mathcal{S}$ satisfies Principles 1–7. This is the hypothesis.

Part (iv): given two systems $\mathcal{S}_1, \mathcal{S}_2$ with the same $D$ and $\zeta$, the density rescaling $\rho \mapsto a\rho + b$ (mapping $\rho_1^*$ to $\rho_2^*$ and $\rho_{\max,1}$ to $\rho_{\max,2}$), the time rescaling (matching $\tau_1 P_{1*}'$ to $\tau_2 P_{2*}'$), and the spatial diffeomorphism (if the domains differ) produce an ED-equivalence $\mathcal{T}: \mathcal{S}_1 \to \mathcal{S}_2$. The architectural realizations are isomorphic because both systems satisfy the same principles with the same $\Delta$. $\square$

### D.6.2 Universality Across Physical Domains

**Corollary D.20** (Cross-domain universality). *Let $\mathcal{S}_1$ and $\mathcal{S}_2$ be dynamical systems arising from different physical contexts — e.g., quantum density evolution, galactic structure formation, condensed-matter pattern dynamics, or photonic mode coupling. If each system can be written in the canonical ED form (D.1) satisfying Principles 1–7, then $\mathcal{S}_1 \sim_{\mathrm{ED}} \mathcal{S}_2$.*

*In particular, the two systems exhibit:*

- *the same eight motifs (Saddle, Spiral, Horizon, Manifold, Boundary, Memory Loop, Dissipator, Nonlinear Triad),*
- *the same nine laws (Unique Attraction through Transient Structure),*
- *the same eight geometric objects (Attractor Point through Triad Locus),*
- *the same nine invariants and seven invariant relations,*
- *the same regime classification governed by $\Delta = D + 2\zeta$.*

*The physical interpretation of $\rho$ (quantum probability density, stellar mass density, order parameter, photon occupation number) is irrelevant to the architectural identity. What matters is the structural form of the dynamics.*

*Proof.* By Theorem D.19, both $\mathcal{S}_1, \mathcal{S}_2 \in \mathcal{U}_{\mathrm{ED}}$. By Theorem D.8, the constitutive differences (different $M$ and $P$ functions reflecting different microscopic physics) do not affect the architectural realization, provided Principles 3, 4, and 7 are satisfied. By Theorem D.10, the domain differences do not affect the architecture. The architectural isomorphism $\mathcal{A}(\mathcal{S}_1) \cong \mathcal{A}(\mathcal{S}_2)$ follows. $\square$

**Remark D.21** (Architectural universality vs. quantitative universality). ED-equivalence is *architectural*, not *quantitative*. Two ED-equivalent systems share the same structural features (motifs, laws, geometry, invariants) but may differ in all quantitative details: the specific decay rates, oscillation frequencies, triad amplitude ratios, and convergence time scales depend on the constitutive functions and parameters. The universality is in the *form* of the dynamics, not in the *numbers*. This is analogous to the universality of critical exponents in statistical mechanics, where systems with different microscopic Hamiltonians share the same scaling behavior near a phase transition. In the ED context, the "phase transition" is replaced by the regime transition at $\Delta = 1$, and the "scaling behavior" is replaced by the full nine-layer architecture.

---

## D.7 Summary

The ED universality class $\mathcal{U}_{\mathrm{ED}}$ is characterized by the following properties:

| Property | Statement | Reference |
|----------|-----------|-----------|
| Definition | $\mathcal{U}_{\mathrm{ED}}$ = all PDE–ODE systems satisfying P1–P7 | Definition D.5 |
| Closure (rescaling) | Invariant under time, space, and amplitude rescaling | Theorem D.7 |
| Closure (constitutive) | Invariant under perturbation of $M, P$ preserving P3–P4, P7 | Theorem D.8 |
| Closure (domain) | Invariant under domain change with Neumann conditions | Theorem D.10 |
| Invariant ($\Delta$) | $D + 2\zeta$ is preserved by all equivalences | Theorem D.11 |
| Invariant (geometry) | Spiral Sheet, Monotonic Cone, Boundary Surface preserved | Theorem D.12 |
| Invariant (spectrum) | Modal hierarchy and triad selection rules preserved | Theorems D.13–D.14 |
| Robustness | Structurally stable under small perturbation | Theorem D.16 |
| Attractor persistence | Unique equilibrium persists continuously | Theorem D.17 |
| Horizon persistence | Mobility-collapse barrier persists continuously | Theorem D.18 |
| Universality | Any system satisfying P1–P7 belongs to $\mathcal{U}_{\mathrm{ED}}$ | Theorem D.19 |
| Cross-domain | Different physics, same architecture | Corollary D.20 |

The universality class is defined by seven structural principles, not by a specific equation. This is the formal content of the closing statement of the Architectural Canon:

*Seven principles, one identity, one universe of systems.*

---

**References for Appendix D**

[1] H. Amann, *Linear and Quasilinear Parabolic Problems, Vol. I: Abstract Linear Theory*, Birkhäuser, Basel, 1995.

[8] Y.A. Kuznetsov, *Elements of Applied Bifurcation Theory*, 3rd ed., Springer, New York, 2004.

[10] J. Hale, *Asymptotic Behavior of Dissipative Systems*, Mathematical Surveys and Monographs, vol. 25, AMS, Providence, 1988.

[11] M. Golubitsky and D.G. Schaeffer, *Singularities and Groups in Bifurcation Theory, Vol. I*, Springer, New York, 1985.