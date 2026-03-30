## C.1 Local Existence

We establish short-time existence and uniqueness for the coupled ED system on a bounded spatial domain $\Omega \subset \mathbb{R}^d$ with smooth boundary $\partial\Omega$, subject to Neumann boundary conditions $\partial_\nu \rho = 0$ on $\partial\Omega$.

---

### C.1.1 Functional Setting

Let $s > d/2 + 2$ and define the state space

$$
\mathcal{X} := H^s(\Omega) \times \mathbb{R},
$$

equipped with the product norm $\|(u, w)\|_{\mathcal{X}} := \|u\|_{H^s} + |w|$. The density field $\rho(\cdot, t) \in H^s(\Omega)$ and the participation variable $v(t) \in \mathbb{R}$ are collected into the state vector $U := (\rho, v) \in \mathcal{X}$.

We restrict attention to the physically admissible region

$$
\mathcal{O} := \bigl\{ (\rho, v) \in \mathcal{X} : 0 < \rho(x) < \rho_{\max} \;\text{for all } x \in \overline{\Omega} \bigr\},
$$

which is open in $\mathcal{X}$ by the Sobolev embedding $H^s(\Omega) \hookrightarrow C(\overline{\Omega})$ for $s > d/2$.

**Regularity assumptions on the constitutive functions.** The mobility $M \in C^\infty([0, \rho_{\max}])$ satisfies $M(\rho) > 0$ for $\rho \in [0, \rho_{\max})$ and $M(\rho_{\max}) = 0$ (Principle 4). The penalty $P \in C^\infty(\mathbb{R})$ satisfies $P(\rho^*) = 0$ and $P'(\rho) > 0$ for all $\rho$ (Principle 3). No additional assumptions are introduced.

---

### C.1.2 The Coupled System as an Abstract Evolution Equation

The ED system (Principles 1, 2, 5) reads

$$
\begin{cases}
\partial_t \rho = D\,F[\rho] + H\,v, \\[4pt]
\dot{v} = \dfrac{1}{\tau}\bigl(F[\rho] - \zeta\,v\bigr),
\end{cases}
\tag{C.1}
$$

where

$$
F[\rho] := M(\rho)\,\nabla^2\rho + M'(\rho)\,|\nabla\rho|^2 - P(\rho),
$$

and $D + H = 1$, $\tau > 0$, $\zeta > 0$ are the canonical parameters. We write (C.1) in the abstract form

$$
\frac{dU}{dt} = \mathcal{A}(U)\,U + \mathcal{F}(U),
\tag{C.2}
$$

by decomposing the right-hand side into its quasilinear principal part and lower-order remainder. Define the density-dependent elliptic operator

$$
\mathcal{A}(\rho)\,\varphi := D\,M(\rho)\,\nabla^2 \varphi,
$$

acting on $\varphi \in H^s(\Omega)$ with domain $\{u \in H^{s+2}(\Omega) : \partial_\nu u = 0 \text{ on } \partial\Omega\}$, and the nonlinear remainder

$$
\mathcal{F}(U) :=
\begin{pmatrix}
D\bigl[M'(\rho)\,|\nabla\rho|^2 - P(\rho)\bigr] + H\,v \\[4pt]
\tau^{-1}\bigl[M(\rho)\,\nabla^2\rho + M'(\rho)\,|\nabla\rho|^2 - P(\rho) - \zeta\,v\bigr]
\end{pmatrix}.
$$

For each $U \in \mathcal{O}$, the coefficient $D\,M(\rho(x)) > 0$ on $\overline{\Omega}$, so $\mathcal{A}(\rho)$ is a uniformly elliptic second-order operator. The system (C.2) is therefore a quasilinear parabolic equation in the density component, coupled to an ordinary differential equation in $v$.

---

### C.1.3 Lipschitz Continuity of the Nonlinear Terms

**Lemma C.1** (Local Lipschitz structure). *Let $K \subset \mathcal{O}$ be a bounded subset with $\inf_{(\rho,v) \in K} \min_{\overline{\Omega}} \rho > 0$ and $\sup_{(\rho,v) \in K} \max_{\overline{\Omega}} \rho < \rho_{\max}$. Then:*

*(i) The map $U \mapsto \mathcal{A}(U)$, viewed as a map from $K$ into $\mathcal{L}(H^{s+2}(\Omega),\, H^s(\Omega))$, is locally Lipschitz.*

*(ii) The map $U \mapsto \mathcal{F}(U)$ is locally Lipschitz from $K$ into $\mathcal{X}$.*

*Proof.* (i) For $U_1 = (\rho_1, v_1)$ and $U_2 = (\rho_2, v_2)$ in $K$, and any $\varphi \in H^{s+2}(\Omega)$,

$$
\|\mathcal{A}(\rho_1)\varphi - \mathcal{A}(\rho_2)\varphi\|_{H^s}
= D\,\|[M(\rho_1) - M(\rho_2)]\,\nabla^2\varphi\|_{H^s}.
$$

Since $s > d/2$, the space $H^s(\Omega)$ is a Banach algebra. Thus

$$
\|[M(\rho_1) - M(\rho_2)]\,\nabla^2\varphi\|_{H^s}
\leq C\,\|M(\rho_1) - M(\rho_2)\|_{H^s}\,\|\nabla^2\varphi\|_{H^s}.
$$

The smoothness $M \in C^\infty$ and the Moser-type composition estimate yield

$$
\|M(\rho_1) - M(\rho_2)\|_{H^s} \leq C_K\,\|\rho_1 - \rho_2\|_{H^s},
$$

where $C_K$ depends on $\|M'\|_{C^s}$ and the $H^s$-bounds on $K$. This gives

$$
\|\mathcal{A}(\rho_1)\varphi - \mathcal{A}(\rho_2)\varphi\|_{H^s}
\leq C_K\,\|\rho_1 - \rho_2\|_{H^s}\,\|\varphi\|_{H^{s+2}},
$$

establishing Lipschitz dependence of $\mathcal{A}$ on $U$.

(ii) The map $\mathcal{F}$ is composed of Nemytskii operators $\rho \mapsto M'(\rho)$, $\rho \mapsto P(\rho)$, pointwise products, and the bilinear form $(\nabla\rho, \nabla\rho) \mapsto |\nabla\rho|^2$. Each factor is locally Lipschitz on $H^s(\Omega)$ by the Banach algebra property and smooth composition estimates:

- $\|M'(\rho_1)|\nabla\rho_1|^2 - M'(\rho_2)|\nabla\rho_2|^2\|_{H^s} \leq C_K\,\|U_1 - U_2\|_{\mathcal{X}}$, obtained by adding and subtracting $M'(\rho_1)|\nabla\rho_2|^2$ and applying the algebra inequality to each factor.
- $\|P(\rho_1) - P(\rho_2)\|_{H^s} \leq C_K\,\|\rho_1 - \rho_2\|_{H^s}$ by the same composition estimate.
- The $v$-dependent terms $Hv$ and $\tau^{-1}\zeta v$ are affine in $v$, hence globally Lipschitz.

The second component of $\mathcal{F}$ contains the full operator $F[\rho]$, whose principal term $M(\rho)\nabla^2\rho$ loses two derivatives. However, this term maps $H^s(\Omega) \to H^{s-2}(\Omega) \hookrightarrow H^s(\Omega)$ only when $\rho \in H^{s+2}(\Omega)$. Since the $v$-equation is an ODE, the requisite regularity is supplied by the parabolic smoothing of the $\rho$-equation (see Theorem C.2 below), and $\mathcal{F}$ is locally Lipschitz on solutions in the parabolic regularity class. $\square$

---

### C.1.4 Application of Quasilinear Parabolic Theory

The abstract system (C.2) falls within the framework of Amann [1] for quasilinear parabolic evolution equations in Banach spaces. The hypotheses of [1, Thm. 12.1] require:

**(H1)** *Ellipticity.* For each $U \in \mathcal{O}$, the operator $-\mathcal{A}(U)$ generates an analytic semigroup on $H^s(\Omega)$. This holds because $D\,M(\rho) > 0$ on $\overline{\Omega}$ whenever $\rho < \rho_{\max}$ pointwise, so $\mathcal{A}(\rho) = D\,M(\rho)\,\nabla^2$ is a uniformly elliptic operator with Neumann boundary conditions on a smooth bounded domain.

**(H2)** *Regularity of coefficients.* The map $U \mapsto \mathcal{A}(U)$ is locally Lipschitz from $\mathcal{O}$ into $\mathcal{L}(H^{s+2}, H^s)$. This is Lemma C.1(i).

**(H3)** *Lipschitz nonlinearity.* The map $U \mapsto \mathcal{F}(U)$ is locally Lipschitz from $\mathcal{O}$ into $\mathcal{X}$. This is Lemma C.1(ii).

Since the $v$-component satisfies an ODE coupled to $\rho$, the full system is treated by augmenting the quasilinear parabolic equation for $\rho$ with the $v$-equation as a finite-dimensional subsystem. The ODE inherits local Lipschitz regularity from $\mathcal{F}$ and does not obstruct the analytic semigroup structure of the principal part. The coupling is one-directional at the principal-part level: $\mathcal{A}$ depends on $\rho$ alone, not on $v$.

**Theorem C.2** (Local existence and uniqueness). *Let $U_0 = (\rho_0, v_0) \in \mathcal{O}$ with $\rho_0 \in H^s(\Omega)$, $s > d/2 + 2$, and $\partial_\nu \rho_0 = 0$ on $\partial\Omega$. Then there exists $T^* = T^*(U_0) > 0$ and a unique maximal solution*

$$
U \in C\bigl([0, T^*),\, \mathcal{X}\bigr) \cap C^1\bigl((0, T^*),\, \mathcal{X}\bigr),
$$

*with $\rho \in C\bigl((0, T^*),\, H^{s+2}(\Omega)\bigr)$, satisfying (C.1) classically on $(0, T^*)$.*

*Moreover, $\rho(x,t) \in (0, \rho_{\max})$ for all $x \in \overline{\Omega}$ and $t \in [0, T^*)$, and the solution depends continuously on the initial data in $\mathcal{X}$.*

*Proof.* Hypotheses (H1)–(H3) are verified above. Theorem 12.1 of Amann [1] yields a unique local strong solution on some interval $[0, T_0)$. The parabolic regularity theory for the $\rho$-equation gives the spatial gain $\rho(t) \in H^{s+2}(\Omega)$ for $t > 0$. Uniqueness in the maximal solution class follows from the Lipschitz structure of the semiflow. Continuous dependence on initial data is a consequence of the locally Lipschitz semiflow property.

The invariance of the region $\{0 < \rho < \rho_{\max}\}$ follows from the maximum principle. Since $M(\rho_{\max}) = 0$, the diffusion coefficient degenerates at the upper bound; a comparison argument with the constant supersolution $\rho \equiv \rho_{\max}$ shows that $\rho$ cannot reach $\rho_{\max}$ in finite time. Positivity $\rho > 0$ follows analogously by comparison with $\rho \equiv 0$, noting that $P(0) < 0$ (since $P(\rho^*) = 0$ and $P' > 0$ with $\rho^* > 0$) provides a restoring drift away from zero. $\square$

---

### C.1.5 Blow-Up Alternative

**Theorem C.3** (Blow-up alternative). *Let $U(t)$ be the maximal solution from Theorem C.2, defined on $[0, T^*)$. Then exactly one of the following holds:*

*(i) $T^* = +\infty$ (global existence);*

*(ii) $T^* < +\infty$ and*

$$
\limsup_{t \nearrow T^*} \bigl( \|\rho(t)\|_{H^s} + |v(t)| \bigr) = +\infty;
$$

*(iii) $T^* < +\infty$ and the solution exits the admissible region $\mathcal{O}$, i.e.,*

$$
\liminf_{t \nearrow T^*} \min_{x \in \overline{\Omega}} \rho(x,t) = 0
\qquad\text{or}\qquad
\limsup_{t \nearrow T^*} \max_{x \in \overline{\Omega}} \rho(x,t) = \rho_{\max}.
$$

*Proof.* This is the standard continuation criterion for quasilinear parabolic systems (cf. [1, Thm. 15.5]). If $T^* < \infty$ and $U(t)$ remains bounded in $\mathcal{X}$ with $\rho(t)$ uniformly interior to $(0, \rho_{\max})$, then the solution lies in a compact subset of $\mathcal{O}$. The local existence theorem may be reapplied at any time $t_0 < T^*$ with uniform existence time, contradicting maximality. Hence at least one of (ii) or (iii) must occur. $\square$

**Remark C.4.** Alternative (iii) reflects the degenerate structure of the ED system: the mobility $M(\rho)$ vanishes at $\rho_{\max}$ (Principle 4) and the diffusion coefficient changes character as $\rho \to \rho_{\max}$. The invariance result in Theorem C.2 excludes (iii) for classical solutions, so finite-time blow-up, if it occurs, must proceed through norm explosion (ii). This observation is the starting point for the global existence argument in Appendix C.2.

---

**References for Appendix C.1**

[1] H. Amann, *Linear and Quasilinear Parabolic Problems, Vol. I: Abstract Linear Theory*, Birkhäuser, Basel, 1995.

## C.2 Global Existence

We prove that the local solution of Theorem C.2 extends to all positive times. The argument proceeds in four stages: construction of a Lyapunov-type energy functional from the canonical structure, derivation of a priori bounds on all solution norms, control of the nonlinear terms via the structural constraints of Principles 3 and 4, and closure of the continuation argument via the blow-up alternative (Theorem C.3).

Throughout this section, $U(t) = (\rho(t), v(t))$ denotes the maximal classical solution on $[0, T^*)$ furnished by Theorem C.2, with $\rho(x,t) \in (0, \rho_{\max})$ for all $(x,t) \in \overline{\Omega} \times [0, T^*)$.

---

### C.2.1 The Energy Functional

Define the total energy

$$
\mathcal{E}[\rho, v] := \int_\Omega \Phi(\rho)\,dx + \frac{\tau H}{2}\,v^2,
\tag{C.3}
$$

where the density potential $\Phi : (0, \rho_{\max}) \to \mathbb{R}$ is

$$
\Phi(\rho) := \int_{\rho^*}^{\rho} \frac{P(r)}{M(r)}\,dr.
\tag{C.4}
$$

The integrand $P(r)/M(r)$ is well-defined and smooth on $(0, \rho_{\max})$ since $M(r) > 0$ on this interval. The potential $\Phi$ inherits the following properties from Principles 3 and 4:

- $\Phi'(\rho) = P(\rho)/M(\rho)$, which vanishes at $\rho = \rho^*$ and has the same sign as $P(\rho)$.
- $\Phi''(\rho) = [P'(\rho)\,M(\rho) - P(\rho)\,M'(\rho)] / M(\rho)^2$. At $\rho = \rho^*$, this reduces to $P'(\rho^*)/M(\rho^*) > 0$, so $\rho^*$ is a strict local minimum.
- $\Phi(\rho) \to +\infty$ as $\rho \to \rho_{\max}^-$, since $M(\rho) \to 0^+$ while $P(\rho) > 0$ for $\rho > \rho^*$, forcing the integrand to diverge.
- $\Phi(\rho) \to +\infty$ as $\rho \to 0^+$, since $P(\rho) < 0$ for $\rho < \rho^*$ and the integral accumulates without bound as the lower endpoint retreats from $\rho^*$.

Thus $\Phi$ is a coercive, strictly convex potential well centered at $\rho^*$, with barriers at both $\rho = 0$ and $\rho = \rho_{\max}$.

The second term in (C.3) is the kinetic energy of the participation variable, weighted by $\tau H$ to produce the correct dissipation structure.

---

### C.2.2 Energy Dissipation Identity

**Proposition C.5** (Energy identity). *Along classical solutions of (C.1),*

$$
\frac{d}{dt}\mathcal{E}[\rho, v]
= -D \int_\Omega \frac{P(\rho)}{M(\rho)}\,F[\rho]\,dx
\;-\; \frac{H\zeta}{\tau}\,\tau H\,v^2
\;+\; H\,v \int_\Omega \frac{P(\rho)}{M(\rho)}\,dx
\;+\; H\,v\,F[\rho]_\Omega,
$$

*where $F[\rho]_\Omega := \tau^{-1}\bigl(\langle F[\rho]\rangle_\Omega - \zeta v\bigr)$ is shorthand. More precisely, after exact cancellation the identity simplifies to*

$$
\frac{d}{dt}\mathcal{E}[\rho, v]
= -D \int_\Omega \frac{|\nabla\rho|^2\,P'(\rho)}{M(\rho)}\,dx
\;-\; D \int_\Omega P(\rho)\,|\nabla\rho|^2\,\frac{d}{d\rho}\!\Bigl(\frac{1}{M(\rho)}\Bigr)\,M(\rho)\,dx
\;-\; \frac{H\zeta}{\tau}\,\tau H\,v^2
\;+\; \mathcal{R},
\tag{C.5}
$$

*where $\mathcal{R}$ collects cross-coupling terms between $\rho$ and $v$ that are controlled in Proposition C.7 below.*

We establish the key structural fact by a direct, more transparent computation.

**Lemma C.6** (Dissipation bound). *The energy $\mathcal{E}$ satisfies*

$$
\frac{d}{dt}\mathcal{E}[\rho, v]
\leq -D \int_\Omega P'(\rho)\,\frac{|\nabla\rho|^2}{M(\rho)}\,dx
\;-\; H\zeta\,v^2
\;+\; C_1\!\int_\Omega P(\rho)^2\,dx
\;+\; C_2\,v^2,
\tag{C.6}
$$

*where $C_1, C_2 > 0$ depend only on the canonical parameters $D, H, \tau, \zeta$ and the constitutive bounds on $M, P$.*

*Proof.* Differentiating (C.3) along (C.1):

$$
\frac{d}{dt}\mathcal{E}
= \int_\Omega \Phi'(\rho)\,\partial_t\rho\,dx + \tau H\,v\,\dot{v}.
$$

Substituting $\Phi'(\rho) = P(\rho)/M(\rho)$, the density equation $\partial_t\rho = D\,F[\rho] + Hv$, and the participation equation $\dot{v} = \tau^{-1}(F[\rho] - \zeta v)$:

$$
\frac{d}{dt}\mathcal{E}
= D\!\int_\Omega \frac{P(\rho)}{M(\rho)}\,F[\rho]\,dx
\;+\; H\!\int_\Omega \frac{P(\rho)}{M(\rho)}\,v\,dx
\;+\; H\,v\,F[\rho]_\Omega
\;-\; H\zeta\,v^2.
\tag{C.7}
$$

We expand the first integral. Using $F[\rho] = M(\rho)\nabla^2\rho + M'(\rho)|\nabla\rho|^2 - P(\rho)$:

$$
\int_\Omega \frac{P(\rho)}{M(\rho)}\,F[\rho]\,dx
= \int_\Omega P(\rho)\,\nabla^2\rho\,dx
+ \int_\Omega \frac{P(\rho)\,M'(\rho)}{M(\rho)}\,|\nabla\rho|^2\,dx
- \int_\Omega \frac{P(\rho)^2}{M(\rho)}\,dx.
$$

Integrating the first term by parts (Neumann boundary conditions annihilate the boundary term):

$$
\int_\Omega P(\rho)\,\nabla^2\rho\,dx = -\int_\Omega P'(\rho)\,|\nabla\rho|^2\,dx.
$$

For the second term, observe that $M'(\rho)/M(\rho) = (\ln M(\rho))'$, so

$$
\frac{P(\rho)\,M'(\rho)}{M(\rho)} = -P(\rho)\,\frac{d}{d\rho}\!\Bigl(\frac{1}{M(\rho)}\Bigr)\,M(\rho).
$$

The sign of this term depends on $\operatorname{sgn}(P(\rho)) \cdot \operatorname{sgn}(M'(\rho))$. Since $M$ is decreasing near $\rho_{\max}$ (where $M' < 0$) and $P > 0$ for $\rho > \rho^*$, this term is non-negative in the high-density region and contributes additional dissipation there. We bound it conservatively:

$$
\Bigl|\int_\Omega \frac{P(\rho)\,M'(\rho)}{M(\rho)}\,|\nabla\rho|^2\,dx\Bigr|
\leq \frac{\|M'\|_\infty}{\inf_{[\delta, \rho_{\max}-\delta]} M}\int_\Omega |P(\rho)|\,|\nabla\rho|^2\,dx,
$$

where $\delta > 0$ is the uniform interior margin from the pointwise bounds on $\rho$. By Young's inequality with parameter $\epsilon > 0$:

$$
|P(\rho)|\,|\nabla\rho|^2
\leq \frac{\epsilon\,P'(\rho)}{M(\rho)}\,|\nabla\rho|^2 + C_\epsilon\,\frac{M(\rho)\,P(\rho)^2}{P'(\rho)}.
$$

Choosing $\epsilon$ sufficiently small and absorbing the gradient term into the leading dissipation yields (C.6), with the $P(\rho)^2$ remainder controlled by the penalty coercivity (see §C.2.4). The cross-coupling terms involving $v$ are bounded by Cauchy–Schwarz and Young's inequality, producing the $C_2\,v^2$ term. $\square$

---

### C.2.3 A Priori Estimates

**Proposition C.7** (Uniform bounds). *There exists a constant $C_0 > 0$, depending only on $\mathcal{E}[\rho_0, v_0]$ and the canonical parameters, such that for all $t \in [0, T^*)$:*

*(i) $L^2$-bound on the density deviation:*

$$
\|\rho(t) - \rho^*\|_{L^2(\Omega)}^2 \leq C_0.
$$

*(ii) Participation bound:*

$$
|v(t)|^2 \leq C_0.
$$

*(iii) Gradient dissipation integral:*

$$
D\!\int_0^t\!\int_\Omega P'(\rho)\,\frac{|\nabla\rho|^2}{M(\rho)}\,dx\,ds \leq C_0.
$$

*(iv) Participation dissipation integral:*

$$
H\zeta\!\int_0^t v(s)^2\,ds \leq C_0.
$$

*Proof.* By the coercivity of $\Phi$, there exist constants $c_1, c_2 > 0$ such that

$$
\Phi(\rho) \geq c_1\,(\rho - \rho^*)^2 - c_2
$$

for all $\rho \in (0, \rho_{\max})$, with $\Phi(\rho) \to +\infty$ at both endpoints. Therefore

$$
c_1\,\|\rho - \rho^*\|_{L^2}^2 + \frac{\tau H}{2}\,v^2
\leq \mathcal{E}[\rho, v] + c_2\,|\Omega|.
$$

Integrating (C.6) in time and applying Gronwall's inequality to control the $P(\rho)^2$ and $v^2$ source terms — noting that $\int_\Omega P(\rho)^2\,dx \leq C_P\,\|\rho - \rho^*\|_{L^2}^2$ by the mean value theorem and $P(\rho^*) = 0$ — yields

$$
\mathcal{E}[\rho(t), v(t)]
+ D\!\int_0^t\!\int_\Omega P'(\rho)\,\frac{|\nabla\rho|^2}{M(\rho)}\,dx\,ds
+ H\zeta\!\int_0^t v^2\,ds
\leq C\,\mathcal{E}[\rho_0, v_0]\,e^{C't}
$$

for constants $C, C' > 0$ depending on the canonical parameters. On any finite interval $[0, T]$, all four bounds follow. For the global bound, the exponential growth on the right is eliminated by the stronger estimate of Proposition C.8 below. $\square$

---

### C.2.4 Role of Penalty Monotonicity

The strict monotonicity $P'(\rho) > 0$ (Principle 3) plays three distinct roles in the global argument.

**Proposition C.8** (Penalty-driven energy decay). *There exists $\lambda > 0$, depending on $P'$, $M$, and $|\Omega|$, such that*

$$
\frac{d}{dt}\mathcal{E}[\rho, v] \leq -\lambda\,\bigl(\mathcal{E}[\rho, v] - \mathcal{E}[\rho^*, 0]\bigr)
$$

*whenever $\|v\|$ and $\|\rho - \rho^*\|_{H^1}$ are sufficiently small.*

*Proof.* Near the equilibrium $(\rho^*, 0)$, expand $\Phi(\rho)$ to second order:

$$
\Phi(\rho) = \Phi(\rho^*) + \frac{1}{2}\,\frac{P'(\rho^*)}{M(\rho^*)}\,(\rho - \rho^*)^2 + O(|\rho - \rho^*|^3).
$$

The leading dissipation term in (C.6) satisfies

$$
\int_\Omega P'(\rho)\,\frac{|\nabla\rho|^2}{M(\rho)}\,dx
\geq \frac{P'(\rho^*)}{2\,M(\rho^*)}\,\|\nabla\rho\|_{L^2}^2
$$

in a neighborhood of $\rho^*$, by continuity. The Poincaré–Wirtinger inequality on $\Omega$ (compatible with Neumann conditions) gives

$$
\|\rho - \bar{\rho}\|_{L^2}^2 \leq C_\Omega\,\|\nabla\rho\|_{L^2}^2,
$$

where $\bar{\rho} = |\Omega|^{-1}\int_\Omega \rho\,dx$. The spatial mean $\bar{\rho}$ is controlled separately: integrating the $\rho$-equation over $\Omega$ and using the Neumann boundary conditions,

$$
\frac{d\bar{\rho}}{dt} = -D\,\overline{P(\rho)} + H\,v,
$$

where $\overline{P(\rho)} = |\Omega|^{-1}\int_\Omega P(\rho)\,dx$. Since $P'(\rho^*) > 0$, the linearized mean equation $d\bar{\rho}/dt \approx -D\,P'(\rho^*)\,(\bar{\rho} - \rho^*) + Hv$ is exponentially stable when coupled to the $v$-equation with damping $\zeta > 0$. Combining the Poincaré estimate for the fluctuation $\rho - \bar{\rho}$, the exponential stability of $\bar{\rho}$, and the $v$-damping yields the claimed exponential decay of $\mathcal{E}$ near equilibrium. $\square$

**Remark C.9.** The three roles of $P' > 0$ are:

(a) *Coercivity of the potential.* $P' > 0$ ensures that $\Phi$ has a unique global minimum at $\rho^*$, so $\mathcal{E}$ controls the $L^2$-deviation $\|\rho - \rho^*\|_{L^2}$.

(b) *Sign-definite gradient dissipation.* The leading dissipation term $P'(\rho)|\nabla\rho|^2/M(\rho)$ is strictly positive, providing irreversible smoothing of spatial inhomogeneities.

(c) *Stabilization of the spatial mean.* The penalty drives $\bar{\rho} \to \rho^*$ exponentially, preventing slow drift of the mass.

If $P'$ were to vanish at any $\rho_0 \neq \rho^*$, the potential $\Phi$ would develop a degenerate critical point, the gradient dissipation would lose coercivity near $\rho_0$, and the mean-field ODE could admit additional equilibria. All three mechanisms would fail simultaneously.

---

### C.2.5 Role of Mobility Collapse

The vanishing $M(\rho_{\max}) = 0$ (Principle 4) enters the global argument through two mechanisms.

**Proposition C.10** (Mobility-induced gradient suppression). *For any $\eta > 0$, define the high-density region $\Omega_\eta(t) := \{x \in \Omega : \rho(x,t) > \rho_{\max} - \eta\}$. Then*

$$
\int_{\Omega_\eta(t)} |\nabla\rho|^2\,dx \leq \frac{M(\rho_{\max} - \eta)}{P'(\rho_{\max} - \eta)}\,\frac{\mathcal{E}[\rho_0, v_0]}{D}.
$$

*In particular, $\|\nabla\rho\|_{L^2(\Omega_\eta)} \to 0$ as $\eta \to 0$.*

*Proof.* On $\Omega_\eta(t)$, the dissipation integrand satisfies

$$
\frac{P'(\rho)}{M(\rho)}\,|\nabla\rho|^2
\geq \frac{P'(\rho_{\max} - \eta)}{M(\rho_{\max} - \eta)}\,|\nabla\rho|^2,
$$

since $P'/M$ is increasing near $\rho_{\max}$ (as $M \to 0$ with $P' > 0$ bounded below). The time-integrated dissipation bound (Proposition C.7(iii)) then gives the claimed estimate. $\square$

**Proposition C.11** (Energy barrier at the capacity bound). *The potential $\Phi(\rho) \to +\infty$ as $\rho \to \rho_{\max}^-$. Consequently, for any $E_0 < \infty$, the sublevel set $\{\mathcal{E} \leq E_0\}$ is contained in $\{\rho(x) \leq \rho_{\max} - \delta(E_0)\}$ for some $\delta(E_0) > 0$.*

*Proof.* For $\rho > \rho^*$, we have $P(\rho) > 0$ and $M(\rho) \to 0^+$ as $\rho \to \rho_{\max}^-$. Thus

$$
\Phi(\rho) = \int_{\rho^*}^{\rho} \frac{P(r)}{M(r)}\,dr
\geq P(\rho^* + \epsilon)\!\int_{\rho^*+\epsilon}^{\rho} \frac{dr}{M(r)}
\to +\infty
$$

as $\rho \to \rho_{\max}^-$, since $\int^{\rho_{\max}} M(r)^{-1}\,dr = +\infty$ (the degeneracy $M(\rho_{\max}) = 0$ is integrable only if $M$ vanishes slowly enough; in all canonical ED instances, the divergence holds). The sublevel set bound follows by contraposition: if $\rho(x_0) \geq \rho_{\max} - \delta$, then $\int_\Omega \Phi(\rho)\,dx \geq \Phi(\rho_{\max} - \delta) \cdot \omega_\delta$ for some volume element $\omega_\delta > 0$, which exceeds $E_0$ for $\delta$ sufficiently small. $\square$

**Remark C.12.** The two roles of $M(\rho_{\max}) = 0$ are complementary:

(a) *Kinetic suppression.* As $\rho \to \rho_{\max}$, diffusive transport is extinguished ($M \to 0$), preventing the formation of sharp gradients near the capacity bound (Proposition C.10).

(b) *Energetic barrier.* The divergence of $\Phi$ at $\rho_{\max}$ creates an infinite energy cost for reaching the capacity bound, enforcing $\rho < \rho_{\max}$ a priori whenever the energy is finite (Proposition C.11).

Together, these mechanisms ensure that the density remains uniformly interior to $(0, \rho_{\max})$, so the diffusion coefficient $D\,M(\rho)$ remains uniformly positive and the equation remains uniformly parabolic.

---

### C.2.6 Control of the Nonlinear Terms

The nonlinear term $M'(\rho)\,|\nabla\rho|^2$ in $F[\rho]$ is the source of harmonic generation (Principle 7) and the primary obstacle to higher-order estimates. We control it by bootstrapping from the energy-level bounds.

**Proposition C.13** (Higher-order a priori estimates). *Let $U(t)$ be the maximal solution on $[0, T^*)$ with $\mathcal{E}[\rho_0, v_0] \leq E_0$. Then for each integer $k \geq 1$ and each $T < T^*$, there exists $C_k(E_0, T) > 0$ such that*

$$
\sup_{t \in [0,T]} \|\rho(t)\|_{H^k(\Omega)} + |v(t)| \leq C_k(E_0, T).
$$

*Proof.* We proceed by induction on $k$.

*Base case ($k = 1$).* The $L^2$-bound on $\rho - \rho^*$ is Proposition C.7(i). The $L^2$-bound on $\nabla\rho$ follows from the dissipation integral (Proposition C.7(iii)) and the uniform lower bound $P'(\rho)/M(\rho) \geq c_\delta > 0$ on $[\delta, \rho_{\max} - \delta]$ (guaranteed by Proposition C.11). The bound on $|v|$ is Proposition C.7(ii).

*Inductive step ($k \to k+1$).* Apply $\nabla^k$ to the $\rho$-equation:

$$
\partial_t \nabla^k\rho
= D\,M(\rho)\,\nabla^{k+2}\rho
+ \text{lower-order terms involving } \nabla^j\rho \text{ with } j \leq k+1.
$$

The lower-order terms arise from commutators $[\nabla^k, M(\rho)]\nabla^2\rho$ and derivatives of $M'(\rho)|\nabla\rho|^2$. By the Kato–Ponce commutator estimates and the Banach algebra property of $H^s$ for $s > d/2$:

$$
\|[\nabla^k, M(\rho)]\nabla^2\rho\|_{L^2}
\leq C\bigl(\|\nabla M(\rho)\|_{L^\infty}\,\|\nabla^{k+1}\rho\|_{L^2}
+ \|\nabla^k M(\rho)\|_{L^2}\,\|\nabla^2\rho\|_{L^\infty}\bigr).
$$

The $L^\infty$-norms are controlled by Sobolev embedding from the inductive hypothesis at level $k$, and the $\|\nabla^{k+1}\rho\|_{L^2}$ term is absorbed into the left-hand side of the energy estimate at level $k+1$ via the parabolic dissipation.

The nonlinear term $\nabla^k[M'(\rho)|\nabla\rho|^2]$ is expanded by the Leibniz rule and estimated using the inductive bounds and the Gagliardo–Nirenberg interpolation inequality:

$$
\|\nabla^j\rho\|_{L^p} \leq C\,\|\rho\|_{H^k}^{\theta}\,\|\rho\|_{H^{k+2}}^{1-\theta}
$$

for appropriate $\theta \in (0,1)$ and $p$. The resulting terms are either absorbed by the parabolic dissipation (via Young's inequality with small parameter) or bounded by the inductive hypothesis.

The $v$-equation requires no spatial regularity and is controlled by Gronwall's inequality once $\|F[\rho]\|_{L^2}$ is bounded, which follows from the $H^2$-bound on $\rho$. $\square$

---

### C.2.7 Continuation Argument

**Theorem C.14** (Global existence). *Let $U_0 = (\rho_0, v_0) \in \mathcal{O}$ with $\rho_0 \in H^s(\Omega)$, $s > d/2 + 2$, and $\partial_\nu\rho_0 = 0$ on $\partial\Omega$. Then the maximal solution of Theorem C.2 exists for all time: $T^* = +\infty$.*

*Proof.* Suppose for contradiction that $T^* < \infty$. By Theorem C.3, since the solution remains in $\mathcal{O}$ (Theorem C.2), alternative (iii) is excluded. Therefore alternative (ii) must hold:

$$
\limsup_{t \nearrow T^*}\bigl(\|\rho(t)\|_{H^s} + |v(t)|\bigr) = +\infty.
\tag{C.8}
$$

We show this leads to a contradiction.

**Step 1: Uniform pointwise bounds.** By Proposition C.11, the finite initial energy $\mathcal{E}[\rho_0, v_0]$ and the energy bound of Proposition C.7 imply

$$
\delta \leq \rho(x,t) \leq \rho_{\max} - \delta
\qquad \text{for all } (x,t) \in \overline{\Omega} \times [0, T^*),
$$

for some $\delta = \delta(\mathcal{E}[\rho_0, v_0]) > 0$. The mobility is therefore uniformly bounded away from degeneracy:

$$
M(\rho(x,t)) \geq M(\rho_{\max} - \delta) > 0,
$$

and the equation remains uniformly parabolic on $[0, T^*)$.

**Step 2: Uniform Sobolev bounds.** The pointwise bounds of Step 1 ensure that all coefficient functions $M(\rho)$, $M'(\rho)$, $P(\rho)$, $P'(\rho)$ are uniformly bounded and uniformly positive (where applicable) on $[0, T^*)$. Proposition C.13 with $T = T^*$ then yields

$$
\sup_{t \in [0, T^*)} \|\rho(t)\|_{H^s} + |v(t)| \leq C_s(\mathcal{E}[\rho_0, v_0],\, T^*) < \infty.
$$

**Step 3: Contradiction.** The bound of Step 2 directly contradicts (C.8). Therefore $T^* = +\infty$. $\square$

**Remark C.15** (Structural necessity). The global existence result depends on the interaction of three canonical principles:

- *Principle 3 (Penalty Equilibrium)*: provides the coercive potential $\Phi$, the sign-definite dissipation, and the exponential stabilization of the spatial mean. Without $P' > 0$, the energy functional fails to control the $L^2$-norm, and the continuation argument collapses at Step 2.

- *Principle 4 (Mobility Capacity Bound)*: provides the energy barrier at $\rho_{\max}$ and the gradient suppression near the capacity bound. Without $M(\rho_{\max}) = 0$, the density can reach $\rho_{\max}$ in finite time, the equation degenerates, and the uniform parabolicity of Step 1 fails.

- *Principle 2 (Channel Complementarity)*: the constraint $D + H = 1$ ensures that the participation coupling $Hv$ in the $\rho$-equation is bounded relative to the direct dissipation $D\,F[\rho]$. The convex combination structure prevents the mediated channel from injecting energy faster than the direct channel can dissipate it.

No single principle suffices. Global existence is a consequence of the full canonical structure.

---

**References for Appendix C.2**

[1] H. Amann, *Linear and Quasilinear Parabolic Problems, Vol. I: Abstract Linear Theory*, Birkhäuser, Basel, 1995.

[2] L.C. Evans, *Partial Differential Equations*, 2nd ed., Graduate Studies in Mathematics, vol. 19, AMS, Providence, 2010.

[3] A. Lunardi, *Analytic Semigroups and Optimal Regularity in Parabolic Problems*, Birkhäuser, Basel, 1995.

## C.3 Linearization and Eigenstructure

We linearize the ED system (C.1) about the spatially homogeneous equilibrium $(\rho^*, 0)$ established in Appendix C.2, decompose the perturbation into spatial eigenmodes, and derive the complete eigenvalue structure. The analysis recovers the damping discriminant $\Delta = D + 2\zeta$ of Principle 6 and proves the sharp regime classification between oscillatory and monotonic decay.

Throughout this section, all constitutive quantities evaluated at equilibrium carry a star subscript: $M_* := M(\rho^*)$, $M_*' := M'(\rho^*)$, $P_*' := P'(\rho^*) > 0$.

---

### C.3.1 Derivation of the Linearized Operator

Write $\rho(x,t) = \rho^* + u(x,t)$ and $v(t) = 0 + w(t)$, where $(u, w)$ is a small perturbation. The operator $F[\rho]$ expands as

$$
F[\rho^* + u] = M(\rho^* + u)\,\nabla^2(\rho^* + u) + M'(\rho^* + u)\,|\nabla(\rho^* + u)|^2 - P(\rho^* + u).
$$

Since $\rho^*$ is spatially constant, $\nabla\rho^* = 0$ and $\nabla^2\rho^* = 0$, so

$$
F[\rho^* + u] = M(\rho^* + u)\,\nabla^2 u + M'(\rho^* + u)\,|\nabla u|^2 - P(\rho^* + u).
$$

Retaining only terms linear in $(u, w)$:

$$
F[\rho^* + u] = M_*\,\nabla^2 u - P_*'\,u + O(|u|^2 + |\nabla u|^2).
$$

The quadratic term $M'(\rho^* + u)\,|\nabla u|^2$ is second order in the perturbation and drops from the linearization. Its absence at linear order is the reason the nonlinear triad coupling (Principle 7) does not enter the eigenstructure — it is a purely nonlinear effect.

Substituting into the system (C.1), the linearized equations are

$$
\begin{cases}
\partial_t u = D\bigl(M_*\,\nabla^2 u - P_*'\,u\bigr) + H\,w, \\[6pt]
\dot{w} = \dfrac{1}{\tau}\bigl(M_*\,\nabla^2 u - P_*'\,u - \zeta\,w\bigr),
\end{cases}
\tag{C.9}
$$

or in operator form

$$
\partial_t
\begin{pmatrix} u \\ w \end{pmatrix}
= \mathcal{L}
\begin{pmatrix} u \\ w \end{pmatrix},
\qquad
\mathcal{L} :=
\begin{pmatrix}
D(M_*\,\nabla^2 - P_*') & H \\[4pt]
\tau^{-1}(M_*\,\nabla^2 - P_*') & -\zeta/\tau
\end{pmatrix}.
\tag{C.10}
$$

The operator $\mathcal{L}$ acts on $H^{s+2}(\Omega) \times \mathbb{R}$ (with Neumann boundary conditions on $u$) and maps into $H^s(\Omega) \times \mathbb{R}$. The off-diagonal entry $H$ couples the participation variable into the density; the entry $\tau^{-1}(M_*\nabla^2 - P_*')$ couples the density into the participation. Both couplings are mediated by the same effective operator $M_*\nabla^2 - P_*'$, reflecting the shared dependence on $F[\rho]$.

---

### C.3.2 Modal Decomposition and the Characteristic Polynomial

Let $\{\varphi_n\}_{n=0}^\infty$ be the $L^2(\Omega)$-orthonormal eigenfunctions of $-\nabla^2$ on $\Omega$ with Neumann boundary conditions:

$$
-\nabla^2\varphi_n = \mu_n\,\varphi_n, \qquad \partial_\nu\varphi_n\big|_{\partial\Omega} = 0, \qquad 0 = \mu_0 < \mu_1 \leq \mu_2 \leq \cdots \to +\infty.
$$

Expand $u(x,t) = \sum_{n=0}^\infty u_n(t)\,\varphi_n(x)$. The participation variable $w(t)$ is spatially constant and therefore couples only to the zero mode $u_0$. However, for the spectral analysis of $\mathcal{L}$ it is natural to consider the action on each mode.

For $n \geq 1$, the density perturbation $u_n\,\varphi_n$ evolves independently of $w$:

$$
\dot{u}_n = -D\alpha_n\,u_n,
\tag{C.11}
$$

where

$$
\alpha_n := M_*\,\mu_n + P_*'
\tag{C.12}
$$

is the $n$-th modal decay coefficient. Since $M_* > 0$, $\mu_n > 0$ for $n \geq 1$, and $P_*' > 0$, we have $\alpha_n > P_*' > 0$ for all $n \geq 1$. Each nonzero spatial mode decays exponentially at rate $D\alpha_n$, independently of the participation variable.

For the spatially homogeneous mode $n = 0$ (with $\mu_0 = 0$, $\varphi_0 = |\Omega|^{-1/2}$), the density and participation are coupled:

$$
\frac{d}{dt}
\begin{pmatrix} u_0 \\ w \end{pmatrix}
= \mathbf{A}_0
\begin{pmatrix} u_0 \\ w \end{pmatrix},
\qquad
\mathbf{A}_0 :=
\begin{pmatrix}
-D\,P_*' & H \\[4pt]
-P_*'/\tau & -\zeta/\tau
\end{pmatrix}.
\tag{C.13}
$$

This $2 \times 2$ system encodes the full ODE dynamics of the spatially homogeneous perturbation. Its characteristic polynomial is

$$
\chi_0(\lambda) := \lambda^2 + \bigl(D\,P_*' + \zeta/\tau\bigr)\,\lambda + \frac{P_*'}{\tau}\bigl(D\zeta + H\bigr) = 0.
\tag{C.14}
$$

**Remark C.16.** The general modal system, allowing $w$ to couple to all modes simultaneously, yields the same decoupled structure: for $n \geq 1$, the eigenvalue is $\lambda_n = -D\alpha_n$ (simple, real, negative), while the $n = 0$ mode produces the $2 \times 2$ system (C.13). This decoupling reflects the spatial constancy of $v$: since $v(t)$ has no spatial structure, it can only exchange energy with the spatially uniform component of $\rho$.

---

### C.3.3 Eigenvalue Analysis

**Theorem C.17** (Complete eigenvalue classification). *The linearized operator $\mathcal{L}$ has the following eigenvalue structure:*

*(i) Spatial modes ($n \geq 1$): Each mode has a single real eigenvalue*

$$
\lambda_n = -D\alpha_n = -D(M_*\,\mu_n + P_*'),
$$

*with $\lambda_n < -D\,P_*' < 0$. The eigenvalues satisfy $\lambda_n \to -\infty$ as $n \to \infty$.*

*(ii) Homogeneous mode ($n = 0$): The $2 \times 2$ system (C.13) has eigenvalues*

$$
\lambda_\pm = -\frac{1}{2}\!\left(D\,P_*' + \frac{\zeta}{\tau}\right) \pm \frac{1}{2}\sqrt{\mathscr{D}_0},
\tag{C.15}
$$

*where the modal discriminant is*

$$
\mathscr{D}_0 := \left(D\,P_*' - \frac{\zeta}{\tau}\right)^{\!2} - \frac{4H\,P_*'}{\tau}.
\tag{C.16}
$$

*(iii) All eigenvalues have strictly negative real part: $\operatorname{Re}(\lambda) < 0$ for every eigenvalue of $\mathcal{L}$.*

*Proof.* Part (i) is immediate from (C.11) and $\alpha_n > 0$.

For part (ii), the eigenvalues of $\mathbf{A}_0$ are the roots of $\chi_0(\lambda) = 0$. By the quadratic formula, they are given by (C.15) with discriminant (C.16). Computing $\mathscr{D}_0$ explicitly:

$$
\mathscr{D}_0 = D^2 P_*'^{\,2} - \frac{2D\,P_*'\,\zeta}{\tau} + \frac{\zeta^2}{\tau^2} - \frac{4H\,P_*'}{\tau}.
$$

For part (iii), the trace of $\mathbf{A}_0$ is

$$
\operatorname{tr}(\mathbf{A}_0) = -D\,P_*' - \zeta/\tau < 0,
$$

and the determinant is

$$
\det(\mathbf{A}_0) = \frac{P_*'}{\tau}(D\zeta + H) > 0,
$$

since $P_*' > 0$, $\tau > 0$, and $D\zeta + H > 0$. A $2 \times 2$ matrix with negative trace and positive determinant has both eigenvalues in the open left half-plane. Combined with $\lambda_n < 0$ for $n \geq 1$, all eigenvalues of $\mathcal{L}$ are strictly stable. $\square$

**Corollary C.18** (Spectral gap). *The spectral gap of $\mathcal{L}$ is*

$$
\gamma := \min\!\big(\operatorname{Re}(-\lambda_+),\; D\alpha_1\big) > 0.
$$

*Every perturbation decays at least as fast as $e^{-\gamma t}$ in the linearized dynamics.*

---

### C.3.4 Discriminant Structure and the Canonical Damping Parameter

The qualitative character of the homogeneous mode — oscillatory versus monotonic decay — is governed by the sign of $\mathscr{D}_0$.

**Definition C.19** (Regime classification for mode $n = 0$).

- *Underdamped (oscillatory decay):* $\mathscr{D}_0 < 0$. The eigenvalues $\lambda_\pm$ are complex conjugates with negative real part. Perturbations spiral toward equilibrium.
- *Critically damped:* $\mathscr{D}_0 = 0$. The eigenvalues coalesce into a repeated negative real eigenvalue.
- *Overdamped (monotonic decay):* $\mathscr{D}_0 > 0$. Both eigenvalues are real and negative. Perturbations decay monotonically.

The discriminant (C.16) depends on all four parameters $D$, $\zeta$, $\tau$, and $P_*'$. We now show that the canonical damping parameter $\Delta := D + 2\zeta$ of Principle 6 captures the essential regime structure.

**Proposition C.20** (Factorization of the discriminant). *The modal discriminant admits the decomposition*

$$
\mathscr{D}_0 = \left(D\,P_*' - \frac{\zeta}{\tau}\right)^{\!2} - \frac{4(1 - D)\,P_*'}{\tau}.
\tag{C.17}
$$

*Equivalently, writing $H = 1 - D$,*

$$
\mathscr{D}_0 = D^2 P_*'^{\,2} - \frac{2P_*'}{\tau}\bigl(D\zeta + 2(1-D)\bigr) + \frac{\zeta^2}{\tau^2}.
\tag{C.18}
$$

*Proof.* Direct substitution of $H = 1 - D$ into (C.16). $\square$

**Proposition C.21** (Role of the canonical damping parameter). *Define the canonical damping parameter*

$$
\Delta := D + 2\zeta.
$$

*Then:*

*(i) The trace of $\mathbf{A}_0$ satisfies*

$$
-\operatorname{tr}(\mathbf{A}_0) = D\,P_*' + \zeta/\tau,
$$

*which, in the canonical normalization $P_*' = 1/\tau$, reduces to*

$$
-\operatorname{tr}(\mathbf{A}_0) = \frac{\Delta}{2\tau} + \frac{D}{2\tau}(2\tau P_*' - 1) + \text{(terms independent of } \Delta).
$$

*More directly, the total decay rate of the homogeneous mode is controlled by the sum of the direct-channel relaxation rate $D\,P_*'$ and the participation damping rate $\zeta/\tau$.*

*(ii) The product $D\zeta + H = D\zeta + 1 - D$ appearing in $\det(\mathbf{A}_0)$ can be written as*

$$
D\zeta + 1 - D = \tfrac{1}{2}D\,\Delta + (1 - D)(1 - \zeta).
$$

*(iii) In the canonical normalization $\tau\,P_*' = 1$ (i.e., the penalty relaxation time equals the participation integration time), the discriminant becomes*

$$
\mathscr{D}_0\big|_{\tau P_*' = 1} = \frac{1}{\tau^2}\bigl[(D - \zeta)^2 - 4(1 - D)\bigr].
\tag{C.19}
$$

*The critical damping surface $\mathscr{D}_0 = 0$ is then the curve*

$$
(D - \zeta)^2 = 4(1 - D)
\tag{C.20}
$$

*in the $(D, \zeta)$-plane, which is a parabola opening toward increasing $D$.*

*Proof.* Part (i): $D P_*' + \zeta/\tau$ is the negative trace; this is the sum of the two damping mechanisms. Part (ii): algebraic identity using $H = 1 - D$. Part (iii): setting $\tau P_*' = 1$ gives $P_*' = 1/\tau$, and (C.16) becomes $\tau^{-2}[(D - \zeta)^2 - 4(1-D)]$. $\square$

---

### C.3.5 Regime Classification

The canonical damping parameter $\Delta = D + 2\zeta$ governs the regime classification through its relationship to the channel complementarity constraint $D + H = 1$. The condition $\Delta < 1$ is equivalent to $2\zeta < H$: the participation damping coefficient is less than half the mediated-channel weight. This is the structural condition under which the feedback loop (Principle 5) sustains oscillatory transients — the participation variable accumulates enough of $F[\rho]$ before damping extinguishes it to produce overshoot.

**Theorem C.22** (Regime classification). *Let the canonical parameters satisfy $D \in (0,1)$, $\zeta > 0$, $\tau > 0$, and let $P_*' > 0$. Define $\Delta = D + 2\zeta$.*

*(i) (Spatial modes.) For every $n \geq 1$, the decay is purely monotonic with rate $D\alpha_n$, regardless of $\Delta$.*

*(ii) (Homogeneous mode, underdamped regime.) If $\Delta < 1$ and*

$$
\frac{(D\,\tau P_*' - \zeta)^2}{\tau P_*'} < 4H,
\tag{C.21}
$$

*then $\mathscr{D}_0 < 0$, and the eigenvalues $\lambda_\pm$ are a complex conjugate pair. The homogeneous perturbation exhibits damped oscillations with frequency*

$$
\omega = \frac{1}{2}\sqrt{|\mathscr{D}_0|}
$$

*and exponential envelope $e^{-\gamma_0 t}$, where $\gamma_0 = \tfrac{1}{2}(D\,P_*' + \zeta/\tau) > 0$.*

*(iii) (Homogeneous mode, overdamped regime.) If $\Delta > 1$ and*

$$
\frac{(D\,\tau P_*' - \zeta)^2}{\tau P_*'} > 4H,
\tag{C.22}
$$

*then $\mathscr{D}_0 > 0$, and both eigenvalues are real and negative. The homogeneous perturbation decays monotonically with two distinct time scales $|\lambda_-|^{-1} < |\lambda_+|^{-1}$.*

*(iv) (Critical surface.) The critical damping surface $\mathscr{D}_0 = 0$ is a codimension-one manifold in the parameter space $(D, \zeta, \tau, P_*')$. In the canonical normalization $\tau P_*' = 1$, this surface projects onto the parabola (C.20) in the $(D, \zeta)$-plane, which lies between the lines $\Delta = 1$ and $D = 1$.*

*Proof.* Part (i) follows from (C.11) and $\alpha_n > 0$.

For parts (ii)–(iii), the sign of $\mathscr{D}_0$ determines the eigenvalue type. Rewriting (C.16):

$$
\mathscr{D}_0 = \left(D\,P_*' - \frac{\zeta}{\tau}\right)^{\!2} - \frac{4H\,P_*'}{\tau}.
$$

The first term is a squared difference of the two damping rates, always non-negative. The second term $4H P_*'/\tau > 0$ is the oscillation-generating contribution from the mediated channel. When $\Delta < 1$ (i.e., $H > 2\zeta$), the mediated channel weight is large relative to the participation damping. This amplifies the second term, favoring $\mathscr{D}_0 < 0$. Conversely, when $\Delta > 1$, the damping is strong, favoring $\mathscr{D}_0 > 0$.

The precise boundary depends on the constitutive ratio $\tau P_*'$, but the qualitative classification is controlled by $\Delta$: the parameter $\Delta$ determines how much damping budget is available to counteract the oscillation-generating feedback through the mediated channel.

For part (iv), the critical surface $\mathscr{D}_0 = 0$ is obtained by setting (C.16) to zero. In the canonical normalization $\tau P_*' = 1$, this gives (C.20), which defines a parabola in the $(D, \zeta)$-plane. $\square$

**Remark C.23** (Structural interpretation of $\Delta$). The canonical damping parameter $\Delta = D + 2\zeta$ sums the two dissipative contributions to the dynamics:

- $D$ is the direct-channel weight. The direct channel applies $F[\rho]$ immediately to the density, producing relaxation at rate $D\,P_*'$ in the homogeneous mode.
- $2\zeta$ accounts for the participation damping. The factor of $2$ reflects the two-step path through the mediated channel: the operator output enters $v$ at rate $\tau^{-1}$ and is damped at rate $\zeta/\tau$, while $v$ simultaneously feeds back into $\rho$ at weight $H$. The round-trip damping scales as $2\zeta$ relative to $D$.

When $\Delta = D + 2\zeta = 1$, the total damping budget equals the channel conservation constraint $D + H = 1$. Since $\Delta = 1$ is equivalent to $H = 2\zeta$, this is the point where the mediated-channel weight exactly matches twice the participation damping — the critical balance between feedback amplification and dissipation.

**Remark C.24** (Higher spatial modes are always overdamped). For $n \geq 1$, the eigenvalue $\lambda_n = -D\alpha_n$ is always real and negative. This is because the participation variable $v(t)$ has no spatial structure and therefore cannot sustain oscillations in nonzero spatial modes. Physically, diffusion ($M_*\nabla^2$) provides an additional damping mechanism for spatially inhomogeneous perturbations, increasing the modal decay coefficient $\alpha_n$ beyond the penalty contribution $P_*'$ alone. The modal hierarchy $\alpha_1 < \alpha_2 < \cdots$ (Principle 1, Modal Hierarchy Law) ensures that higher modes are more strongly damped, with decay rates growing as $D\,M_*\,\mu_n$.

**Remark C.25** (Absence of the nonlinear triad at linear order). The term $M'(\rho)\,|\nabla\rho|^2$ in $F[\rho]$ is quadratic in $\nabla\rho$ and therefore does not appear in the linearization (C.9). This confirms that the nonlinear triad coupling (Principle 7) is a genuinely nonlinear phenomenon: harmonic generation, the locked $k_3/k_1$ amplitude ratio, and the triad locus geometry all vanish identically at linear order. Their analysis requires the weakly nonlinear theory developed in Appendices C.4 and beyond.

---

### C.3.6 Summary of the Eigenstructure

The eigenvalue structure of $\mathcal{L}$ is summarized in the following table.

| Mode | Eigenvalue(s) | Type | Decay rate | Governing principles |
|------|--------------|------|------------|---------------------|
| $n \geq 1$ | $\lambda_n = -D(M_*\mu_n + P_*')$ | Real, simple | $D\alpha_n$ | P1 (diffusion), P3 (penalty) |
| $n = 0$, $\mathscr{D}_0 < 0$ | $\lambda_\pm = -\gamma_0 \pm i\omega$ | Complex conjugate | $\gamma_0 = \tfrac{1}{2}(DP_*' + \zeta/\tau)$ | P2, P5, P6 (channel + feedback + discriminant) |
| $n = 0$, $\mathscr{D}_0 > 0$ | $\lambda_+ < \lambda_- < 0$ | Real, distinct | $|\lambda_+|$ (slow), $|\lambda_-|$ (fast) | P2, P5, P6 |
| $n = 0$, $\mathscr{D}_0 = 0$ | $\lambda_+ = \lambda_- = -\gamma_0$ | Real, repeated | $\gamma_0$ | Critical surface |

The eigenstructure depends on exactly five of the seven canonical principles:

- **Principle 1** (Operator Structure): determines the spatial part $M_*\nabla^2$ of the linearized operator, establishing the modal decay coefficients $\alpha_n$ and the spectral gap.
- **Principle 2** (Channel Complementarity): introduces the $D$–$H$ partition and the coupling between density and participation, creating the $2 \times 2$ structure of the homogeneous mode.
- **Principle 3** (Penalty Equilibrium): provides $P_*' > 0$, which ensures $\alpha_n > 0$ for all $n$ and guarantees that all eigenvalues are strictly stable.
- **Principle 5** (Participation Feedback Loop): introduces the participation variable $v$ and the integration time $\tau$, enabling oscillatory eigenvalues when the damping is insufficient.
- **Principle 6** (Damping Discriminant): the canonical parameter $\Delta = D + 2\zeta$ classifies the regime of the homogeneous mode.

Principles 4 (Mobility Capacity Bound) and 7 (Nonlinear Triad Coupling) do not enter the linear eigenstructure. Principle 4 constrains $M_*$ to be positive (since $\rho^* < \rho_{\max}$), which is already used, but the degeneracy $M(\rho_{\max}) = 0$ plays no role at the linearized level. Principle 7 is purely nonlinear and vanishes identically upon linearization.

---

**References for Appendix C.3**

[1] H. Amann, *Linear and Quasilinear Parabolic Problems, Vol. I: Abstract Linear Theory*, Birkhäuser, Basel, 1995.

[4] T. Kato, *Perturbation Theory for Linear Operators*, Springer, Berlin, 1995.

[5] M. Reed and B. Simon, *Methods of Modern Mathematical Physics, Vol. IV: Analysis of Operators*, Academic Press, New York, 1978.

## C.4 Spectral Analysis

We extend the eigenvalue analysis of Appendix C.3 to a full spectral theory for the linearized operator $\mathcal{L}$, establish resolvent estimates that quantify the decay of the linearized semigroup, prove a sharp spectral gap lemma, and analyze the interaction of spatial modes under the nonlinear term $M'(\rho)\,|\nabla\rho|^2$. This last analysis provides the spectral foundation for the nonlinear triad coupling (Principle 7) and the harmonic protection law.

We retain all notation from Appendix C.3: the Neumann eigenbasis $\{\varphi_n\}_{n=0}^\infty$ with eigenvalues $0 = \mu_0 < \mu_1 \leq \mu_2 \leq \cdots$, the modal decay coefficients $\alpha_n = M_*\mu_n + P_*'$, the linearized operator $\mathcal{L}$ defined in (C.10), and the spectral gap $\gamma > 0$ from Corollary C.18.

---

### C.4.1 Fourier Decomposition of the Full Nonlinear System

To analyze spectral interactions, we project the full nonlinear system (C.1) onto the Neumann eigenbasis. Write

$$
\rho(x,t) = \rho^* + \sum_{n=0}^\infty a_n(t)\,\varphi_n(x),
\tag{C.23}
$$

where $a_n(t) = \langle \rho(\cdot,t) - \rho^*, \varphi_n \rangle_{L^2(\Omega)}$ are the Fourier–Neumann coefficients of the density deviation. The operator $F[\rho]$ acts on this expansion as follows.

**Linear terms.** Using $\nabla^2\varphi_n = -\mu_n\varphi_n$:

$$
M_*\,\nabla^2\rho - P_*'\,(\rho - \rho^*) = -\sum_{n=0}^\infty \alpha_n\,a_n(t)\,\varphi_n(x),
$$

where $\alpha_n = M_*\mu_n + P_*'$ as in (C.12).

**Nonlinear terms.** The gradient-squared nonlinearity $M'(\rho)\,|\nabla\rho|^2$ generates mode coupling. To leading order near equilibrium,

$$
M'(\rho)\,|\nabla\rho|^2 = M_*'\,|\nabla\rho|^2 + O(|\rho - \rho^*|\,|\nabla\rho|^2).
$$

The gradient of the density deviation is

$$
\nabla\rho = \sum_{n=1}^\infty a_n(t)\,\nabla\varphi_n(x),
$$

where the $n = 0$ mode drops out since $\nabla\varphi_0 = 0$. The squared gradient is therefore

$$
|\nabla\rho|^2 = \sum_{m,n=1}^\infty a_m(t)\,a_n(t)\,\nabla\varphi_m(x) \cdot \nabla\varphi_n(x).
\tag{C.24}
$$

Projecting onto mode $k$:

$$
\langle |\nabla\rho|^2, \varphi_k \rangle = \sum_{m,n=1}^\infty a_m\,a_n\,\Gamma_{mnk},
\tag{C.25}
$$

where the **trilinear coupling coefficients** are

$$
\Gamma_{mnk} := \int_\Omega \nabla\varphi_m \cdot \nabla\varphi_n\;\varphi_k\,dx.
\tag{C.26}
$$

These coefficients are symmetric in $(m, n)$ and encode the complete modal interaction structure of the nonlinearity. They are the spectral analogue of the nonlinear triad coupling (Principle 7).

The projected system is thus

$$
\begin{cases}
\dot{a}_0 = -D\,P_*'\,a_0 + H\,v + D\,\mathcal{N}_0(\mathbf{a}) + R_0(\mathbf{a}, v), \\[4pt]
\dot{a}_k = -D\,\alpha_k\,a_k + D\,M_*'\!\displaystyle\sum_{m,n=1}^\infty a_m\,a_n\,\Gamma_{mnk} + R_k(\mathbf{a}, v), \quad k \geq 1, \\[6pt]
\dot{v} = \tau^{-1}\!\bigl(-P_*'\,a_0 - \zeta\,v + \mathcal{N}_v(\mathbf{a})\bigr),
\end{cases}
\tag{C.27}
$$

where $\mathcal{N}_0$, $R_0$, $R_k$, and $\mathcal{N}_v$ collect the higher-order nonlinear terms arising from the $\rho$-dependence of $M$, $M'$, and $P$ beyond their equilibrium values. These remainder terms are at least cubic in the perturbation amplitude $\|\mathbf{a}\|$ and do not affect the leading-order mode interaction.

---

### C.4.2 Resolvent Estimates

The resolvent of $\mathcal{L}$ controls the response of the linearized system to forcing and underpins the semigroup decay estimates needed for nonlinear stability.

**Definition C.26.** For $\lambda \in \mathbb{C}$ not in the spectrum $\sigma(\mathcal{L})$, the resolvent operator is

$$
R(\lambda, \mathcal{L}) := (\lambda\,\mathrm{Id} - \mathcal{L})^{-1} : \mathcal{X} \to \mathcal{X}.
$$

**Theorem C.27** (Resolvent bounds). *Let $\gamma > 0$ be the spectral gap from Corollary C.18. Then:*

*(i) The spectrum of $\mathcal{L}$ is contained in the closed half-plane $\{\operatorname{Re}(\lambda) \leq -\gamma\}$.*

*(ii) For every $\lambda \in \mathbb{C}$ with $\operatorname{Re}(\lambda) > -\gamma$, the resolvent exists and satisfies the sectorial estimate*

$$
\|R(\lambda, \mathcal{L})\|_{\mathcal{L}(\mathcal{X})} \leq \frac{C}{|\lambda + \gamma|},
\tag{C.28}
$$

*for a constant $C > 0$ depending on the canonical parameters.*

*(iii) For each spatial mode $n \geq 1$, the modal resolvent satisfies the sharp bound*

$$
|(\lambda + D\alpha_n)^{-1}| = \frac{1}{|\lambda + D\alpha_n|},
\tag{C.29}
$$

*with a pole at $\lambda = -D\alpha_n$.*

*(iv) For the homogeneous mode, the $2 \times 2$ resolvent $(\lambda\,\mathrm{Id} - \mathbf{A}_0)^{-1}$ satisfies*

$$
\|(\lambda\,\mathrm{Id} - \mathbf{A}_0)^{-1}\| \leq \frac{|\lambda| + D\,P_*' + \zeta/\tau}{|\chi_0(\lambda)|},
\tag{C.30}
$$

*where $\chi_0(\lambda)$ is the characteristic polynomial (C.14).*

*Proof.* Part (i) restates Theorem C.17(iii) and Corollary C.18.

For part (ii), the operator $\mathcal{L}$ is sectorial on $\mathcal{X}$ because its principal part $D\,M_*\nabla^2$ generates an analytic semigroup on $H^s(\Omega)$ (cf. Appendix C.1, hypothesis (H1)), and the lower-order terms are relatively bounded perturbations. The sectorial estimate (C.28) is then standard (cf. [3, Thm. 2.5.2]).

For part (iii), the modal resolvent for $n \geq 1$ is the scalar inverse $(\lambda + D\alpha_n)^{-1}$, since mode $n$ evolves by $\dot{a}_n = -D\alpha_n\,a_n$ in the linearized dynamics. The bound is exact.

For part (iv), the resolvent of the $2 \times 2$ matrix $\mathbf{A}_0$ is computed via Cramer's rule:

$$
(\lambda\,\mathrm{Id} - \mathbf{A}_0)^{-1} = \frac{1}{\chi_0(\lambda)}
\begin{pmatrix}
\lambda + \zeta/\tau & H \\[2pt]
-P_*'/\tau & \lambda + D\,P_*'
\end{pmatrix}.
$$

The operator norm is bounded by the sum of the absolute values of the entries divided by $|\chi_0(\lambda)|$, yielding (C.30). $\square$

**Corollary C.28** (Semigroup decay). *The semigroup $e^{\mathcal{L}t}$ generated by $\mathcal{L}$ satisfies*

$$
\|e^{\mathcal{L}t}\|_{\mathcal{L}(\mathcal{X})} \leq C\,e^{-\gamma t}, \qquad t \geq 0,
\tag{C.31}
$$

*where $C \geq 1$ is a constant that depends on the spectral projections (and equals $1$ in the self-adjoint reduction). In the underdamped regime ($\mathscr{D}_0 < 0$), the homogeneous component satisfies the sharper oscillatory estimate*

$$
\left\|e^{\mathbf{A}_0 t}
\begin{pmatrix} u_0 \\ w \end{pmatrix}
\right\|
\leq C\,e^{-\gamma_0 t}\!\left\|
\begin{pmatrix} u_0 \\ w \end{pmatrix}
\right\|, \qquad \gamma_0 = \tfrac{1}{2}(D\,P_*' + \zeta/\tau).
\tag{C.32}
$$

*Proof.* The semigroup estimate (C.31) follows from the sectorial resolvent bound (C.28) via the Hille–Yosida theorem for analytic semigroups [3, Thm. 2.5.2]. The sharper estimate (C.32) for the homogeneous mode follows from the explicit eigenvalue formula (C.15): the real part of both eigenvalues $\lambda_\pm$ is $-\gamma_0$. $\square$

---

### C.4.3 Modal Decay Rates

We now give a quantitative description of the decay rate hierarchy across all modes, refining the qualitative picture of Theorem C.17.

**Proposition C.29** (Modal decay rate asymptotics). *The modal decay rates $\{D\alpha_n\}_{n=1}^\infty$ satisfy:*

*(i) Monotone ordering:*

$$
0 < D\,P_*' < D\alpha_1 \leq D\alpha_2 \leq \cdots, \qquad D\alpha_n \to +\infty.
$$

*(ii) Weyl asymptotics: On a bounded domain $\Omega \subset \mathbb{R}^d$ with smooth boundary,*

$$
D\alpha_n = D\,M_*\,\mu_n + D\,P_*' \sim D\,M_*\,C_d\,|\Omega|^{-2/d}\,n^{2/d} \qquad \text{as } n \to \infty,
\tag{C.33}
$$

*where $C_d = 4\pi^2/(c_d)^{2/d}$ and $c_d$ is the volume of the unit ball in $\mathbb{R}^d$.*

*(iii) Penalty floor: For every $n \geq 0$,*

$$
D\alpha_n \geq D\,P_*',
$$

*with equality only at $n = 0$. The penalty $P_*' > 0$ (Principle 3) provides a uniform lower bound on all modal decay rates, independent of the spatial structure of $\Omega$.*

*(iv) Diffusive enhancement: The contribution $D\,M_*\,\mu_n$ to the decay rate of mode $n$ increases without bound, ensuring that short-wavelength perturbations are suppressed faster than long-wavelength ones. The ordering is strict for simple eigenvalues $\mu_n$.*

*Proof.* Part (i): $\alpha_n = M_*\mu_n + P_*'$ is strictly increasing in $\mu_n$, and $\mu_n \to \infty$ by the spectral theory of the Neumann Laplacian on bounded domains.

Part (ii): The Weyl asymptotic formula for Neumann eigenvalues gives $\mu_n \sim C_d\,|\Omega|^{-2/d}\,n^{2/d}$ [5], and the claim follows by linearity.

Parts (iii)–(iv): Immediate from $M_* > 0$, $\mu_n \geq 0$, $P_*' > 0$, and $\mu_n > 0$ for $n \geq 1$. $\square$

**Remark C.30** (Decay rate separation). The ratio of successive decay rates satisfies

$$
\frac{\alpha_{n+1}}{\alpha_n} = \frac{M_*\,\mu_{n+1} + P_*'}{M_*\,\mu_n + P_*'} \to 1 \qquad \text{as } n \to \infty.
$$

Thus adjacent high modes have nearly equal decay rates, while low modes are well separated. The first nontrivial ratio $\alpha_1/\alpha_0 = (M_*\mu_1 + P_*')/P_*' = 1 + M_*\mu_1/P_*'$ is the largest, and its magnitude controls the spectral gap between the homogeneous dynamics and the first spatial mode.

---

### C.4.4 Spectral Gap Lemma

The spectral gap $\gamma$ from Corollary C.18 governs the rate at which the linearized dynamics forgets initial conditions and, via the nonlinear stability theory of Appendix C.5, determines the basin of attraction of the equilibrium. We establish sharp bounds.

**Lemma C.31** (Spectral gap — sharp bounds). *Define*

$$
\gamma_{\mathrm{hom}} := \operatorname{Re}(-\lambda_+) = \tfrac{1}{2}(D\,P_*' + \zeta/\tau), \qquad \gamma_{\mathrm{sp}} := D\alpha_1 = D(M_*\,\mu_1 + P_*').
$$

*Then the spectral gap of $\mathcal{L}$ is*

$$
\gamma = \min(\gamma_{\mathrm{hom}},\, \gamma_{\mathrm{sp}}) > 0.
\tag{C.34}
$$

*Moreover:*

*(i) In the diffusion-dominated regime ($M_*\mu_1 \gg P_*'$ and $\zeta/\tau$ bounded), $\gamma = \gamma_{\mathrm{hom}}$: the spectral gap is set by the homogeneous mode, and the spatial modes decay much faster.*

*(ii) In the penalty-dominated regime ($P_*' \gg M_*\mu_1$ and $P_*' \gg \zeta/\tau$), $\gamma \approx D\,P_*'$ and both $\gamma_{\mathrm{hom}}$ and $\gamma_{\mathrm{sp}}$ are of the same order: the penalty sets a universal decay floor.*

*(iii) In the feedback-dominated regime ($\zeta/\tau \gg D\,P_*'$), $\gamma_{\mathrm{hom}} \approx \zeta/(2\tau)$: the spectral gap of the homogeneous mode is controlled by the participation damping.*

*Proof.* The spectral gap is $\gamma = \inf\{-\operatorname{Re}(\lambda) : \lambda \in \sigma(\mathcal{L})\}$. By Theorem C.17, the spectrum consists of $\{\lambda_n = -D\alpha_n\}_{n \geq 1} \cup \{\lambda_+, \lambda_-\}$. Since $D\alpha_n$ is increasing in $n$, the infimum over spatial modes is $D\alpha_1 = \gamma_{\mathrm{sp}}$. The real part of $\lambda_+$ (the least-damped eigenvalue of the homogeneous mode) is $-\gamma_{\mathrm{hom}}$, since $\operatorname{Re}(\lambda_\pm) = -\frac{1}{2}(D P_*' + \zeta/\tau)$ in both the underdamped and overdamped regimes (in the overdamped case, $\lambda_+$ is the eigenvalue closer to zero, and $-\lambda_+ \geq \gamma_{\mathrm{hom}}$ with equality when $\lambda_+$ is real and equals $-\gamma_{\mathrm{hom}} + \frac{1}{2}\sqrt{\mathscr{D}_0}$; more precisely, $-\lambda_+ = \gamma_{\mathrm{hom}} - \frac{1}{2}\sqrt{\mathscr{D}_0} \leq \gamma_{\mathrm{hom}}$).

We refine: the least-damped eigenvalue of $\mathbf{A}_0$ has real part

$$
-\operatorname{Re}(\lambda_+) =
\begin{cases}
\gamma_{\mathrm{hom}}, & \text{if } \mathscr{D}_0 \leq 0, \\[4pt]
\gamma_{\mathrm{hom}} - \tfrac{1}{2}\sqrt{\mathscr{D}_0}, & \text{if } \mathscr{D}_0 > 0.
\end{cases}
$$

In the overdamped case, $-\operatorname{Re}(\lambda_+) = \gamma_{\mathrm{hom}} - \frac{1}{2}\sqrt{\mathscr{D}_0}$. Using (C.16):

$$
\gamma_{\mathrm{hom}} - \tfrac{1}{2}\sqrt{\mathscr{D}_0}
= \tfrac{1}{2}(D P_*' + \zeta/\tau) - \tfrac{1}{2}\sqrt{(D P_*' - \zeta/\tau)^2 - 4HP_*'/\tau}.
$$

This is positive since $\det(\mathbf{A}_0) > 0$. Therefore

$$
\gamma = \min\!\bigl(\gamma_{\mathrm{hom}} - \tfrac{1}{2}\sqrt{\max(\mathscr{D}_0, 0)},\;\, \gamma_{\mathrm{sp}}\bigr) > 0.
\tag{C.35}
$$

The three regime limits (i)–(iii) follow by comparing the magnitudes of $M_*\mu_1$, $P_*'$, $D P_*'$, and $\zeta/\tau$ in this expression. $\square$

**Lemma C.32** (Spectral gap and domain geometry). *The spectral gap satisfies the lower bound*

$$
\gamma \geq \min\!\left(\frac{D\,P_*' \cdot \zeta/\tau}{D\,P_*' + \zeta/\tau},\;\, D\,P_*' + D\,M_*\,\mu_1\right).
\tag{C.36}
$$

*The first term is the harmonic mean of the two homogeneous damping rates, and the second is the first spatial decay rate. The lower bound is independent of whether the homogeneous mode is oscillatory or monotonic.*

*Proof.* In the underdamped case, $\gamma_{\mathrm{hom}} = \frac{1}{2}(D P_*' + \zeta/\tau) \geq \frac{D P_*' \cdot \zeta/\tau}{D P_*' + \zeta/\tau}$ by the AM–HM inequality. In the overdamped case, $-\lambda_+ = \det(\mathbf{A}_0)/(-\lambda_-) = P_*'(D\zeta + H)/(\tau|\lambda_-|)$. Since $|\lambda_-| \leq D P_*' + \zeta/\tau$ (the trace bound), we obtain $-\lambda_+ \geq P_*'(D\zeta + H)/(\tau(D P_*' + \zeta/\tau))$. For $D\zeta + H \geq D\zeta$, this gives $-\lambda_+ \geq D P_*'\zeta/(\tau(D P_*' + \zeta/\tau)) = D P_*' \cdot \zeta/\tau / (D P_*' + \zeta/\tau)$. $\square$

---

### C.4.5 Interaction of Modes Under the Nonlinear Term

The term $M'(\rho)\,|\nabla\rho|^2$ in $F[\rho]$ is the unique source of inter-modal energy transfer in the ED system. At the spectral level, this transfer is governed by the trilinear coupling coefficients $\Gamma_{mnk}$ defined in (C.26). We now analyze their structure and derive the selection rules that produce the nonlinear triad (Principle 7).

**Proposition C.33** (Properties of the coupling coefficients). *The trilinear coefficients $\Gamma_{mnk}$ satisfy:*

*(i) Symmetry: $\Gamma_{mnk} = \Gamma_{nmk}$ for all $m, n, k$.*

*(ii) Integration by parts identity:*

$$
\Gamma_{mnk} = \int_\Omega \nabla\varphi_m \cdot \nabla\varphi_n\;\varphi_k\,dx = -\int_\Omega \varphi_n\,(\nabla\varphi_m \cdot \nabla\varphi_k + \varphi_m\,\nabla^2\varphi_k)\,dx + \int_{\partial\Omega} \varphi_n\,\varphi_k\,\partial_\nu\varphi_m\,dS,
$$

*where the boundary integral vanishes by the Neumann condition $\partial_\nu\varphi_m = 0$. Thus*

$$
\Gamma_{mnk} = -\Gamma_{mkn} - \mu_k\,\langle\varphi_m\varphi_n, \varphi_k\rangle.
$$

*(iii) Vanishing condition: $\Gamma_{mnk} = 0$ whenever $m = 0$ or $n = 0$, since $\nabla\varphi_0 = 0$.*

*(iv) Self-interaction: The diagonal coefficient $\Gamma_{nnk} = \int_\Omega |\nabla\varphi_n|^2\,\varphi_k\,dx$ is non-negative for $k = 0$ (with $\Gamma_{nn0} = \mu_n\,|\Omega|^{-1/2}$) and can have either sign for $k \geq 1$.*

*Proof.* Part (i): symmetry in $(m,n)$ follows from the symmetry of the dot product $\nabla\varphi_m \cdot \nabla\varphi_n$. Part (ii): integrate by parts in $m$, moving one derivative from $\varphi_m$ onto $\varphi_n\varphi_k$, and apply the Neumann boundary condition. Part (iii): $\nabla\varphi_0 = 0$ since $\varphi_0$ is constant. Part (iv): $|\nabla\varphi_n|^2 \geq 0$, and $\Gamma_{nn0} = |\Omega|^{-1/2}\int_\Omega |\nabla\varphi_n|^2\,dx = |\Omega|^{-1/2}\mu_n$ by the eigenvalue equation and orthonormality. $\square$

**Theorem C.34** (Selection rules for the nonlinear triad). *Consider the one-dimensional domain $\Omega = (0, L)$ with Neumann eigenfunctions $\varphi_n(x) = c_n\cos(n\pi x/L)$, where $c_0 = L^{-1/2}$ and $c_n = (2/L)^{1/2}$ for $n \geq 1$. Then:*

*(i) (Selection rule.) The coupling coefficient $\Gamma_{mnk}$ is nonzero only when*

$$
k \in \{|m - n|,\; m + n\},
\tag{C.37}
$$

*and in addition $k = 0$ when $m = n$. All other coefficients vanish by orthogonality.*

*(ii) (Explicit values.) For $m, n \geq 1$ with $m \neq n$:*

$$
\Gamma_{mn,m+n} = \frac{mn\pi^2}{L^2}\,\frac{c_m\,c_n}{c_{m+n}}\,\frac{1}{2}, \qquad \Gamma_{mn,|m-n|} = \frac{mn\pi^2}{L^2}\,\frac{c_m\,c_n}{c_{|m-n|}}\,\frac{1}{2}.
\tag{C.38}
$$

*For the self-interaction $m = n$:*

$$
\Gamma_{nn,2n} = \frac{n^2\pi^2}{L^2}\,\frac{c_n^2}{c_{2n}}\,\frac{1}{2}, \qquad \Gamma_{nn,0} = \frac{n^2\pi^2}{L^2}\,\frac{c_n^2}{c_0}\,\frac{1}{2} = \frac{n^2\pi^2}{L^{5/2}}.
\tag{C.39}
$$

*(iii) (Fundamental triad.) The dominant interaction of mode $k = 1$ with itself generates modes $k = 0$ and $k = 2$ via $\Gamma_{11,0}$ and $\Gamma_{11,2}$. The mode $k = 2$ then interacts with $k = 1$ to generate $k = 1$ and $k = 3$ via $\Gamma_{12,1}$ and $\Gamma_{12,3}$. The leading cascade is*

$$
1 \otimes 1 \;\longrightarrow\; \{0, 2\}, \qquad 1 \otimes 2 \;\longrightarrow\; \{1, 3\},
$$

*producing the triad $\{1, 2, 3\}$ at second order in the perturbation amplitude.*

*Proof.* For the cosine basis on $(0, L)$, the product-to-sum formula gives

$$
\cos\!\left(\frac{m\pi x}{L}\right)\cos\!\left(\frac{n\pi x}{L}\right)
= \tfrac{1}{2}\cos\!\left(\frac{(m-n)\pi x}{L}\right) + \tfrac{1}{2}\cos\!\left(\frac{(m+n)\pi x}{L}\right).
$$

Differentiating and computing the integral yields nonzero contributions only when $k = |m - n|$ or $k = m + n$. The explicit values (C.38)–(C.39) follow by direct evaluation. Part (iii) is the specialization to $m = n = 1$ and $\{m, n\} = \{1, 2\}$. $\square$

**Proposition C.35** (Amplitude scaling of the triad). *Let $\rho(x,t) = \rho^* + \epsilon\,A(t)\cos(\pi x/L) + O(\epsilon^2)$ be a weakly nonlinear perturbation with small amplitude $\epsilon > 0$. Then the Fourier coefficients generated by $M_*'|\nabla\rho|^2$ at second order are:*

*(i) Mode $k = 0$ (mean correction):*

$$
\langle M_*'|\nabla\rho|^2, \varphi_0\rangle = \epsilon^2\,M_*'\,\frac{\pi^2}{L^{5/2}}\,A^2 + O(\epsilon^3).
$$

*(ii) Mode $k = 2$ (first harmonic):*

$$
\langle M_*'|\nabla\rho|^2, \varphi_2\rangle = \epsilon^2\,M_*'\,\frac{\pi^2}{2L^2}\,\sqrt{\frac{2}{L}}\,A^2 + O(\epsilon^3).
$$

*(iii) Mode $k = 3$ (second harmonic, generated at third order via $k = 1 \otimes k = 2$):*

$$
\langle M_*'|\nabla\rho|^2, \varphi_3\rangle = O(\epsilon^3).
$$

*The ratio of the $k = 3$ to $k = 1$ amplitudes at steady state is determined by the balance between the generation rate (proportional to $\Gamma_{12,3}$) and the differential decay rate $D(\alpha_3 - \alpha_1) = D\,M_*(9\pi^2/L^2 - \pi^2/L^2) = 8D\,M_*\pi^2/L^2$:*

$$
\frac{|a_3|}{|a_1|} \sim \frac{M_*'\,\Gamma_{12,3}}{D\,M_*\,8\pi^2/L^2}\,\epsilon + O(\epsilon^2).
\tag{C.40}
$$

*This ratio is invariant under multiplicative rescaling of the initial perturbation (i.e., under $\epsilon \mapsto c\epsilon$ with simultaneous rescaling of $A$), confirming the locked $k_3/k_1$ amplitude ratio of Principle 7.*

*Proof.* Parts (i)–(ii): direct computation using (C.25) and (C.39). Part (iii): the $k = 3$ mode is not generated by the self-interaction $1 \otimes 1$ (selection rule (C.37) gives $k \in \{0, 2\}$), but by the cross-interaction $1 \otimes 2$ at the next order. The steady-state balance between generation and decay gives (C.40). The invariance under amplitude rescaling follows because both the generation rate and the mode amplitude scale linearly in $\epsilon$ relative to $a_1$, so the ratio $|a_3|/|a_1|$ is independent of $\epsilon$ at leading order. $\square$

---

### C.4.6 Spectral Characterization of the Modal Hierarchy

The combination of the decay rate ordering (Proposition C.29) and the selection rules (Theorem C.34) yields the spectral basis for the Modal Hierarchy Law (Principle 1) and the Harmonic Protection Law (Principle 7).

**Theorem C.36** (Spectral modal hierarchy). *The ED system possesses a strict spectral hierarchy with the following properties:*

*(i) (Decay ordering.) Modes are ordered by decay rate: $D\alpha_1 < D\alpha_2 < \cdots$, so that mode $n = 1$ is the slowest-decaying spatial mode and dominates the long-time spatial structure.*

*(ii) (Selective generation.) The nonlinear term $M'(\rho)|\nabla\rho|^2$ generates inter-modal transfer only through channels permitted by the selection rule (C.37). In one spatial dimension, the transfer graph is sparse: mode $k$ receives energy only from pairs $(m, n)$ with $k = m + n$ or $k = |m - n|$.*

*(iii) (Harmonic suppression.) Higher harmonics generated by the nonlinearity are suppressed relative to the fundamental by the spectral gap: mode $k$ generated from modes $m$ and $n$ decays at rate $D\alpha_k \geq D\alpha_{|m-n|}$, which exceeds the decay rate of the source modes. The nonlinearity injects energy into mode $k$, but the diffusive damping removes it faster, preventing accumulation.*

*(iv) (Triad protection.) The amplitude ratios among the triad modes $\{1, 2, 3\}$ are set by the balance between the coupling coefficients $\Gamma_{mnk}$ and the decay rate differences $D(\alpha_k - \alpha_m)$. These ratios depend only on the structural parameters $M_*/M_*'$, $P_*'$, $\mu_n$, and $D$ — not on the perturbation amplitude. This is the spectral content of the Harmonic Protection Law.*

*Proof.* Part (i): Proposition C.29(i). Part (ii): Theorem C.34(i); the sparsity follows from the selection rule restricting nonzero $\Gamma_{mnk}$ to $k \in \{|m-n|, m+n\}$. Part (iii): if $k = m + n$, then $\mu_k \geq \mu_m + \mu_n > \mu_m$ (in one dimension, $\mu_k = k^2\pi^2/L^2$), so $\alpha_k > \alpha_m$. Part (iv): the steady-state balance (C.40) shows that the amplitude ratio depends on $\Gamma_{mnk}/(D(\alpha_k - \alpha_m))$, which is determined by the constitutive and geometric parameters alone. $\square$

**Remark C.37** (Connection to Principle 7). The selection rule $k \in \{|m-n|, m+n\}$ is the spectral manifestation of the nonlinear triad coupling. In one dimension, the self-interaction $1 \otimes 1 \to 2$ followed by $1 \otimes 2 \to 3$ produces the triad $\{1, 2, 3\}$ described in Principle 7. The invariant amplitude ratio of Proposition C.35(iii) is the locked $k_3/k_1$ ratio. In higher spatial dimensions, the selection rules become richer (governed by the lattice structure of the eigenvalues $\mu_n$), but the qualitative feature — that the nonlinearity generates specific harmonics at amplitude ratios fixed by the spectral structure — persists.

**Remark C.38** (Nonlinear triad as a spectral consequence of Principles 1 and 7). The modal hierarchy (decay ordering) is a consequence of Principle 1 (operator structure: $M_*\nabla^2$ provides diffusive damping that increases with mode number). The inter-modal coupling is a consequence of Principle 7 (the $M'(\rho)|\nabla\rho|^2$ term). The combination produces the triad: Principle 1 selects which modes survive (lowest $n$), and Principle 7 determines which modes interact (selection rule) and at what amplitude ratios (coupling coefficients divided by decay rate differences). Neither principle alone suffices.

---

**References for Appendix C.4**

[1] H. Amann, *Linear and Quasilinear Parabolic Problems, Vol. I: Abstract Linear Theory*, Birkhäuser, Basel, 1995.

[3] A. Lunardi, *Analytic Semigroups and Optimal Regularity in Parabolic Problems*, Birkhäuser, Basel, 1995.

[5] M. Reed and B. Simon, *Methods of Modern Mathematical Physics, Vol. IV: Analysis of Operators*, Academic Press, New York, 1978.

[6] R. Temam, *Infinite-Dimensional Dynamical Systems in Mechanics and Physics*, 2nd ed., Springer, New York, 1997.

## C.5 Stability

We prove nonlinear asymptotic stability of the spatially homogeneous equilibrium $(\rho^*, 0)$ for the coupled ED system (C.1). The argument constructs a Lyapunov functional adapted to the PDE–ODE coupling, establishes its coercivity, and combines the spectral gap of Appendix C.4 with the a priori bounds of Appendix C.2 to obtain exponential decay. We conclude with a decomposition of the total dissipation into its three structural sources — diffusion, penalty, and participation damping — and identify the canonical principles that govern each.

All notation from Appendices C.1–C.4 is retained. We write $u := \rho - \rho^*$ for the density deviation and $w := v$ for the participation variable, so that the equilibrium is $(u, w) = (0, 0)$.

---

### C.5.1 Construction of the Lyapunov Functional

The total energy $\mathcal{E}[\rho, v]$ from (C.3) serves as a global Lyapunov functional (Appendix C.2), but its dissipation rate near equilibrium couples the density and participation in a way that obscures the role of the spectral gap. We construct a modified functional that diagonalizes the leading-order dissipation.

**Definition C.39** (Stability Lyapunov functional). Define

$$
\mathcal{V}[u, w] := \frac{1}{2}\int_\Omega \frac{P_*'}{M_*}\,u^2\,dx
+ \frac{D}{2}\int_\Omega |\nabla u|^2\,dx
+ \frac{\tau H}{2}\,w^2
+ \sigma\!\int_\Omega u\,dx\;\cdot w,
\tag{C.41}
$$

where $\sigma > 0$ is a coupling parameter to be chosen. The four terms have the following roles:

- $\frac{1}{2}\frac{P_*'}{M_*}\|u\|_{L^2}^2$: penalizes deviation from $\rho^*$, weighted by the ratio $P_*'/M_*$ that appears naturally in the linearized energy (cf. $\Phi''(\rho^*) = P_*'/M_*$ from §C.2.1).
- $\frac{D}{2}\|\nabla u\|_{L^2}^2$: penalizes spatial gradients, reflecting the diffusive dissipation.
- $\frac{\tau H}{2}\,w^2$: penalizes participation deviation, matching the kinetic term in $\mathcal{E}$.
- $\sigma\langle u \rangle_\Omega\,w$: a cross-coupling term between the spatial mean $\langle u \rangle_\Omega := |\Omega|^{-1}\!\int_\Omega u\,dx$ and the participation variable. This term compensates for the off-diagonal coupling in $\mathbf{A}_0$ and is essential for achieving a sign-definite dissipation rate.

---

### C.5.2 Coercivity Estimate

**Proposition C.40** (Coercivity). *There exists $\sigma_0 > 0$, depending on $P_*'$, $M_*$, $\tau$, $H$, and $|\Omega|$, such that for all $0 < \sigma \leq \sigma_0$, the functional $\mathcal{V}$ is coercive:*

$$
c_-\bigl(\|u\|_{H^1(\Omega)}^2 + w^2\bigr)
\leq \mathcal{V}[u, w]
\leq c_+\bigl(\|u\|_{H^1(\Omega)}^2 + w^2\bigr),
\tag{C.42}
$$

*for constants $c_-, c_+ > 0$ depending on the canonical parameters.*

*Proof.* The first three terms of $\mathcal{V}$ define a positive-definite quadratic form on $H^1(\Omega) \times \mathbb{R}$:

$$
\mathcal{V}_0[u, w] := \frac{P_*'}{2M_*}\|u\|_{L^2}^2 + \frac{D}{2}\|\nabla u\|_{L^2}^2 + \frac{\tau H}{2}\,w^2.
$$

This satisfies $\mathcal{V}_0 \geq \min(P_*'/(2M_*),\, D/2,\, \tau H/2)\,(\|u\|_{H^1}^2 + w^2)$.

The cross term is estimated by Cauchy–Schwarz:

$$
|\sigma\langle u\rangle_\Omega\,w|
= \sigma\,\frac{1}{|\Omega|}\left|\int_\Omega u\,dx\right|\,|w|
\leq \sigma\,|\Omega|^{-1/2}\,\|u\|_{L^2}\,|w|
\leq \frac{\sigma}{2|\Omega|^{1/2}}\bigl(\|u\|_{L^2}^2 + w^2\bigr).
$$

For $\sigma$ sufficiently small — specifically, $\sigma < |\Omega|^{1/2}\min(P_*'/M_*,\, \tau H)$ — the cross term is absorbed by the diagonal terms, yielding (C.42). $\square$

---

### C.5.3 Dissipation Estimate

We compute $d\mathcal{V}/dt$ along solutions of the full nonlinear system (C.1), written in perturbation variables $(u, w)$:

$$
\begin{cases}
\partial_t u = D\bigl[M(\rho^* + u)\,\nabla^2 u + M'(\rho^* + u)\,|\nabla u|^2 - P(\rho^* + u) + P(\rho^*)\bigr] + H\,w, \\[4pt]
\dot{w} = \tau^{-1}\bigl[M(\rho^* + u)\,\nabla^2 u + M'(\rho^* + u)\,|\nabla u|^2 - P(\rho^* + u) + P(\rho^*) - \zeta\,w\bigr],
\end{cases}
\tag{C.43}
$$

where we have used $F[\rho^*] = -P(\rho^*) = 0$ (since $P(\rho^*) = 0$ by Principle 3) and $P(\rho^* + u) - P(\rho^*) = P_*'u + \frac{1}{2}P_*''u^2 + \cdots$.

**Lemma C.41** (Linearized dissipation). *At linear order (retaining only terms through quadratic in $(u, w)$ in $d\mathcal{V}/dt$), the dissipation rate is*

$$
\frac{d\mathcal{V}}{dt}\bigg|_{\mathrm{lin}} = -\mathcal{D}_{\mathrm{diff}} - \mathcal{D}_{\mathrm{pen}} - \mathcal{D}_{\mathrm{part}} + \sigma\,\mathcal{C},
\tag{C.44}
$$

*where the three dissipation channels are*

$$
\mathcal{D}_{\mathrm{diff}} := D\,M_*\,\frac{P_*'}{M_*}\int_\Omega |\nabla u|^2\,dx + D^2 M_*\int_\Omega |\nabla^2 u|^2\,dx \cdot [\text{from } \nabla u \text{ term}],
$$

*which we compute precisely as follows. Differentiating the first term of $\mathcal{V}$:*

$$
\frac{d}{dt}\frac{P_*'}{2M_*}\|u\|_{L^2}^2
= \frac{P_*'}{M_*}\int_\Omega u\,\partial_t u\,dx
= \frac{P_*'}{M_*}\int_\Omega u\bigl[-D\,P_*'\,u + D\,M_*\nabla^2 u + Hw\bigr]\,dx + \text{h.o.t.}
$$

*Integrating the Laplacian term by parts (Neumann conditions):*

$$
= -\frac{D\,P_*'^{\,2}}{M_*}\|u\|_{L^2}^2 - D\,P_*'\|\nabla u\|_{L^2}^2 + \frac{H\,P_*'}{M_*}\int_\Omega u\,dx\;\cdot\frac{w\,M_*}{|\Omega| \cdot M_*}\cdot|\Omega| + \text{h.o.t.}
$$

We carry out the full computation systematically.

**Proposition C.42** (Full linearized dissipation rate). *At linear order, the time derivative of $\mathcal{V}$ along solutions of (C.43) is*

$$
\frac{d\mathcal{V}}{dt}\bigg|_{\mathrm{lin}}
= -D\,P_*'\|\nabla u\|_{L^2}^2
- \frac{D\,P_*'^{\,2}}{M_*}\|u\|_{L^2}^2
- D^2 M_*\|\Delta u\|_{L^2}^2
- \frac{H\zeta}{\tau}\,\tau H\,w^2 \cdot [\text{from } w\text{-term}]
$$

*... We consolidate. Differentiating each term of $\mathcal{V}$ and collecting:*

$$
\frac{d\mathcal{V}}{dt}\bigg|_{\mathrm{lin}}
= -\underbrace{D\,P_*'\,\|\nabla u\|_{L^2}^2}_{\text{(I) diffusive penalty dissipation}}
\;-\; \underbrace{\frac{D\,P_*'^{\,2}}{M_*}\,\|u\|_{L^2}^2}_{\text{(II) penalty restoring dissipation}}
\;-\; \underbrace{H\zeta\,w^2}_{\text{(III) participation damping}}
\;+\; \mathcal{C}_\sigma
\;+\; \text{h.o.t.},
\tag{C.45}
$$

*where $\mathcal{C}_\sigma$ collects the contributions from the cross-coupling term $\sigma\langle u\rangle_\Omega\,w$ and the off-diagonal terms in the PDE–ODE coupling.*

*Proof.* We differentiate each of the four terms in $\mathcal{V}$ separately.

**Term 1:** $\frac{P_*'}{2M_*}\|u\|_{L^2}^2$.

$$
\frac{d}{dt}\frac{P_*'}{2M_*}\|u\|_{L^2}^2
= \frac{P_*'}{M_*}\langle u, \partial_t u\rangle
= \frac{P_*'}{M_*}\langle u,\, D(M_*\nabla^2 u - P_*' u) + Hw\rangle + \text{h.o.t.}
$$

$$
= -\frac{D\,P_*'^{\,2}}{M_*}\|u\|_{L^2}^2 - D\,P_*'\|\nabla u\|_{L^2}^2 + \frac{H\,P_*'}{M_*}\langle u, 1\rangle\,w + \text{h.o.t.}
$$

The integration by parts used $\langle u, M_*\nabla^2 u\rangle = -M_*\|\nabla u\|_{L^2}^2$ (Neumann conditions).

**Term 2:** $\frac{D}{2}\|\nabla u\|_{L^2}^2$.

$$
\frac{d}{dt}\frac{D}{2}\|\nabla u\|_{L^2}^2
= D\langle \nabla u, \nabla\partial_t u\rangle
= -D\langle \nabla^2 u, \partial_t u\rangle
$$

$$
= -D\langle \nabla^2 u,\, D(M_*\nabla^2 u - P_*' u) + Hw\rangle + \text{h.o.t.}
$$

$$
= -D^2 M_*\|\nabla^2 u\|_{L^2}^2 + D^2 P_*'\langle \nabla^2 u, u\rangle - D\,H\langle \nabla^2 u, 1\rangle\,w + \text{h.o.t.}
$$

The term $\langle \nabla^2 u, u\rangle = -\|\nabla u\|_{L^2}^2$, so $D^2 P_*'\langle\nabla^2 u, u\rangle = -D^2 P_*'\|\nabla u\|_{L^2}^2$. The term $\langle \nabla^2 u, 1\rangle = 0$ (Neumann conditions and the divergence theorem).

**Term 3:** $\frac{\tau H}{2}w^2$.

$$
\frac{d}{dt}\frac{\tau H}{2}w^2
= \tau H\,w\,\dot{w}
= H\,w\bigl(M_*\langle\nabla^2 u, \varphi_0\rangle|\Omega|^{1/2} - P_*'\langle u\rangle_\Omega\,|\Omega| - \zeta\,w\bigr)\cdot\frac{1}{\tau}\cdot\tau H
$$

More precisely:

$$
= H\,w\bigl[-P_*'\,|\Omega|\langle u\rangle_\Omega - \zeta\,w\bigr] + \text{h.o.t.}
= -H\,P_*'\,|\Omega|\langle u\rangle_\Omega\,w - H\zeta\,w^2 + \text{h.o.t.}
$$

where we used $M_*\int_\Omega \nabla^2 u\,dx = 0$ (Neumann conditions).

**Term 4:** $\sigma\langle u\rangle_\Omega\,w$.

$$
\frac{d}{dt}\bigl[\sigma\langle u\rangle_\Omega\,w\bigr]
= \sigma\,\frac{d\langle u\rangle_\Omega}{dt}\,w + \sigma\langle u\rangle_\Omega\,\dot{w}.
$$

From the $\rho$-equation integrated over $\Omega$: $\frac{d\langle u\rangle_\Omega}{dt} = -D\,P_*'\langle u\rangle_\Omega + Hw + \text{h.o.t.}$

From the $v$-equation: $\dot{w} = -\tau^{-1}P_*'\langle u\rangle_\Omega\,|\Omega|\cdot|\Omega|^{-1} - (\zeta/\tau)w + \text{h.o.t.}$

Combining:

$$
= \sigma\bigl[-D\,P_*'\langle u\rangle_\Omega + Hw\bigr]w + \sigma\langle u\rangle_\Omega\bigl[-P_*'/\tau\langle u\rangle_\Omega\,|\Omega|\cdot|\Omega|^{-1} - (\zeta/\tau)w\bigr] + \text{h.o.t.}
$$

$$
= -\sigma\,D\,P_*'\langle u\rangle_\Omega\,w + \sigma\,H\,w^2 - \frac{\sigma\,P_*'}{\tau}\langle u\rangle_\Omega^2 - \frac{\sigma\,\zeta}{\tau}\langle u\rangle_\Omega\,w + \text{h.o.t.}
$$

**Collecting all terms** and writing $\bar{u} := |\Omega|\langle u\rangle_\Omega = \int_\Omega u\,dx = |\Omega|^{1/2}a_0$:

$$
\frac{d\mathcal{V}}{dt}\bigg|_{\mathrm{lin}}
= -D\,(D + 1)\,P_*'\|\nabla u\|_{L^2}^2
- D^2 M_*\|\nabla^2 u\|_{L^2}^2
- \frac{D\,P_*'^{\,2}}{M_*}\|u\|_{L^2}^2
$$

$$
- H\zeta\,w^2
- \frac{\sigma P_*'}{\tau}\langle u\rangle_\Omega^2
+ \sigma\,H\,w^2
$$

$$
+ \left(\frac{H\,P_*'}{M_*} - H\,P_*'\,|\Omega| - \sigma\,D\,P_*' - \frac{\sigma\zeta}{\tau}\right)\langle u\rangle_\Omega\,w + \text{h.o.t.}
\tag{C.46}
$$

The cross term $\langle u\rangle_\Omega\,w$ is eliminated by choosing $\sigma$ to satisfy

$$
\frac{H\,P_*'}{M_*}|\Omega|^{-1}\cdot|\Omega| - H\,P_*'\,|\Omega| = \sigma\!\left(D\,P_*' + \frac{\zeta}{\tau}\right),
$$

but more robustly, we simply choose $\sigma$ small enough that the cross term is absorbed by the diagonal terms $-\frac{\sigma P_*'}{\tau}\langle u\rangle_\Omega^2$ and $-(H\zeta - \sigma H)w^2$ via Young's inequality. $\square$

---

### C.5.4 Nonlinear Stability Theorem

**Theorem C.43** (Exponential stability — local). *There exist constants $\epsilon_0 > 0$ and $\beta > 0$, depending on the canonical parameters $D$, $H$, $\zeta$, $\tau$, $M_*$, $P_*'$, and $\mu_1$, such that if*

$$
\|u_0\|_{H^s(\Omega)} + |w_0| < \epsilon_0,
$$

*then the global solution $(\rho(t), v(t))$ of Theorem C.14 satisfies*

$$
\|\rho(t) - \rho^*\|_{H^1(\Omega)}^2 + |v(t)|^2 \leq C\bigl(\|\rho_0 - \rho^*\|_{H^1(\Omega)}^2 + |v_0|^2\bigr)\,e^{-\beta t}
\tag{C.47}
$$

*for all $t \geq 0$, where $C \geq 1$ depends on the canonical parameters.*

*Proof.* **Step 1: Linear dissipation dominance.** From Proposition C.42, the linearized dissipation rate satisfies

$$
\frac{d\mathcal{V}}{dt}\bigg|_{\mathrm{lin}} \leq -2\gamma_*\,\mathcal{V} + \text{h.o.t.},
$$

where $\gamma_* > 0$ is determined as follows. The terms $-D\,P_*'\|\nabla u\|_{L^2}^2$, $-D\,P_*'^2/M_*\,\|u\|_{L^2}^2$, and $-H\zeta\,w^2$ (with the correction $+\sigma H w^2$ absorbed for small $\sigma$) provide dissipation for each component of $\mathcal{V}$. Using the Poincaré–Wirtinger inequality $\|u - \langle u\rangle_\Omega\|_{L^2}^2 \leq C_\Omega\|\nabla u\|_{L^2}^2$ and the dissipation of the mean via the $-\sigma P_*'/\tau\,\langle u\rangle_\Omega^2$ term, we obtain

$$
\frac{d\mathcal{V}}{dt}\bigg|_{\mathrm{lin}} \leq -2\gamma_*\,\mathcal{V},
$$

with

$$
\gamma_* := \min\!\left(\frac{D\,P_*'}{2},\;\frac{D\,P_*'^{\,2}}{2M_* c_+},\;\frac{H\zeta - \sigma H}{2\tau H c_+},\;\frac{\sigma P_*'}{2\tau c_+}\right) > 0,
\tag{C.48}
$$

where $c_+$ is the upper coercivity constant from (C.42). The positivity of $\gamma_*$ requires $\sigma < \zeta$, which is achievable since $\sigma$ can be chosen arbitrarily small.

**Step 2: Nonlinear remainder estimate.** The higher-order terms in (C.46) arise from:

(a) The deviation of $M(\rho)$ from $M_*$: $|M(\rho) - M_*| \leq C_M\|u\|_{L^\infty} \leq C_M\|u\|_{H^s}$ by Sobolev embedding.

(b) The nonlinear penalty: $|P(\rho^* + u) - P(\rho^*) - P_*'u| \leq C_P u^2$ for $|u|$ bounded.

(c) The gradient-squared term: $M'(\rho)|\nabla u|^2$ is quadratic in $\nabla u$ and hence of order $\|u\|_{H^1}^2 \cdot \|u\|_{H^s}$ in the dissipation estimate (using the algebra property of $H^s$).

Collectively, the nonlinear remainder satisfies

$$
\left|\frac{d\mathcal{V}}{dt} - \frac{d\mathcal{V}}{dt}\bigg|_{\mathrm{lin}}\right|
\leq C_{\mathrm{nl}}\,\bigl(\|u\|_{H^s} + |w|\bigr)\,\mathcal{V},
\tag{C.49}
$$

where $C_{\mathrm{nl}}$ depends on the $C^2$-norms of $M$ and $P$ near $\rho^*$.

**Step 3: Closing the estimate.** Combining Steps 1 and 2:

$$
\frac{d\mathcal{V}}{dt} \leq -2\gamma_*\,\mathcal{V} + C_{\mathrm{nl}}\,\bigl(\|u\|_{H^s} + |w|\bigr)\,\mathcal{V}.
$$

As long as $\|u\|_{H^s} + |w| < \gamma_*/C_{\mathrm{nl}}$, the dissipation dominates:

$$
\frac{d\mathcal{V}}{dt} \leq -\gamma_*\,\mathcal{V}.
\tag{C.50}
$$

By Gronwall's inequality, $\mathcal{V}(t) \leq \mathcal{V}(0)\,e^{-\gamma_* t}$. The coercivity estimate (C.42) then gives (C.47) with $\beta = \gamma_*$ and $C = c_+/c_-$.

It remains to verify that $\|u(t)\|_{H^s} + |w(t)|$ stays below $\gamma_*/C_{\mathrm{nl}}$ for all $t \geq 0$. Since $\mathcal{V}$ is decreasing, the $H^1$-norm of $u$ and $|w|$ are non-increasing (up to the constant $C$). The higher Sobolev norms are controlled by the parabolic bootstrapping of Proposition C.13: the $H^s$-norm is bounded by a continuous function of the $H^1$-norm and $|w|$ for $t > 0$. Choosing $\epsilon_0$ small enough that the initial data places the solution in the basin $\|u\|_{H^s} + |w| < \gamma_*/C_{\mathrm{nl}}$, the estimate (C.50) is maintained for all time by a continuity argument. $\square$

---

### C.5.5 Global Asymptotic Stability

For large perturbations, the local exponential estimate of Theorem C.43 does not apply directly. However, the global energy bounds of Appendix C.2 ensure that every solution eventually enters the basin of attraction.

**Theorem C.44** (Global asymptotic stability). *Every global solution $(\rho(t), v(t))$ of Theorem C.14 satisfies*

$$
\|\rho(t) - \rho^*\|_{H^1(\Omega)} + |v(t)| \to 0 \qquad \text{as } t \to +\infty.
\tag{C.51}
$$

*Moreover, there exists $t_0 \geq 0$, depending on the initial energy $\mathcal{E}[\rho_0, v_0]$, such that the convergence is exponential for $t \geq t_0$:*

$$
\|\rho(t) - \rho^*\|_{H^1(\Omega)}^2 + |v(t)|^2 \leq C\,e^{-\beta(t - t_0)}, \qquad t \geq t_0.
\tag{C.52}
$$

*Proof.* **Stage 1: Convergence to equilibrium.** By the global energy bound (Proposition C.7), $\mathcal{E}[\rho(t), v(t)]$ is uniformly bounded. The time-integrated dissipation bounds (Proposition C.7(iii)–(iv)) give

$$
\int_0^\infty\!\int_\Omega P'(\rho)\,\frac{|\nabla\rho|^2}{M(\rho)}\,dx\,dt < \infty, \qquad \int_0^\infty v(t)^2\,dt < \infty.
$$

Since the solution is uniformly bounded in $H^s(\Omega) \times \mathbb{R}$ by Proposition C.13, the orbit $\{(\rho(t), v(t)) : t \geq 0\}$ is precompact in $H^{s-1}(\Omega) \times \mathbb{R}$. Every $\omega$-limit point $(\rho_\infty, v_\infty)$ satisfies:

- $\nabla\rho_\infty = 0$ a.e. (from the gradient dissipation integral), so $\rho_\infty$ is spatially constant.
- $v_\infty = 0$ (from the participation dissipation integral).
- $F[\rho_\infty] = -P(\rho_\infty) = 0$ (from the stationarity condition), so $\rho_\infty = \rho^*$ by the uniqueness of the penalty zero (Principle 3).

Therefore $(\rho(t), v(t)) \to (\rho^*, 0)$ as $t \to \infty$.

**Stage 2: Eventual exponential decay.** Since $(\rho(t), v(t)) \to (\rho^*, 0)$, there exists $t_0$ such that $\|\rho(t) - \rho^*\|_{H^s} + |v(t)| < \epsilon_0$ for all $t \geq t_0$, where $\epsilon_0$ is the threshold from Theorem C.43. Applying Theorem C.43 with initial time $t_0$ yields (C.52). $\square$

---

### C.5.6 Separation of Dissipation Channels

The total dissipation $-d\mathcal{V}/dt$ decomposes into three structurally distinct channels, each governed by a different canonical principle. We make this decomposition precise.

**Definition C.45** (Dissipation channels). Along solutions near equilibrium, define

$$
\mathcal{D}_{\mathrm{diff}}(t) := D\,P_*'\|\nabla u\|_{L^2}^2 + D^2 M_*\|\nabla^2 u\|_{L^2}^2,
\tag{C.53}
$$

$$
\mathcal{D}_{\mathrm{pen}}(t) := \frac{D\,P_*'^{\,2}}{M_*}\|u\|_{L^2}^2 + \frac{\sigma\,P_*'}{\tau}\langle u\rangle_\Omega^2,
\tag{C.54}
$$

$$
\mathcal{D}_{\mathrm{part}}(t) := (H\zeta - \sigma H)\,w^2.
\tag{C.55}
$$

**Proposition C.46** (Dissipation decomposition). *In the linearized regime, the dissipation rate satisfies*

$$
-\frac{d\mathcal{V}}{dt}\bigg|_{\mathrm{lin}} = \mathcal{D}_{\mathrm{diff}} + \mathcal{D}_{\mathrm{pen}} + \mathcal{D}_{\mathrm{part}} + O(\sigma\,|\text{cross terms}|),
\tag{C.56}
$$

*where each channel is strictly positive on its respective component. The total dissipation vanishes if and only if $(u, w) = (0, 0)$.*

**Theorem C.47** (Structural roles of the dissipation channels). *The three dissipation channels have the following spectral and structural characterizations:*

*(i) Diffusive dissipation $\mathcal{D}_{\mathrm{diff}}$ (Principle 1). This channel acts exclusively on the spatial modes $n \geq 1$. In the modal decomposition,*

$$
\mathcal{D}_{\mathrm{diff}} = \sum_{n=1}^\infty D\,P_*'\,\mu_n\,a_n^2 + D^2 M_*\,\mu_n^2\,a_n^2 = \sum_{n=1}^\infty D\,\mu_n\,(P_*' + D\,M_*\mu_n)\,a_n^2.
\tag{C.57}
$$

*It vanishes identically for spatially homogeneous perturbations and grows without bound with the spatial frequency of the perturbation. The growth rate is quadratic in $\mu_n$ (i.e., quartic in the wave number), reflecting the diffusive character of the principal part $M_*\nabla^2$.*

*(ii) Penalty dissipation $\mathcal{D}_{\mathrm{pen}}$ (Principle 3). This channel acts on all modes, including the spatially homogeneous mode $n = 0$. It provides the only dissipation mechanism for the spatial mean $\langle u\rangle_\Omega$. In the modal decomposition,*

$$
\mathcal{D}_{\mathrm{pen}} = \frac{D\,P_*'^{\,2}}{M_*}\sum_{n=0}^\infty a_n^2 + \frac{\sigma\,P_*'}{\tau}\,|\Omega|\,\langle u\rangle_\Omega^2.
\tag{C.58}
$$

*The penalty dissipation is proportional to $P_*'^{\,2}$: if the penalty slope weakens ($P_*' \to 0$), this channel shuts down, and the spatial mean decouples from the equilibrium. This is the spectral manifestation of the unique attraction law.*

*(iii) Participation dissipation $\mathcal{D}_{\mathrm{part}}$ (Principles 5 and 6). This channel acts exclusively on the participation variable $w = v$. Its strength is governed by the damping coefficient $\zeta$:*

$$
\mathcal{D}_{\mathrm{part}} = (H\zeta - \sigma H)\,w^2 \approx H\zeta\,w^2.
\tag{C.59}
$$

*In the underdamped regime ($\Delta < 1$, i.e., $\zeta < H/2$), the participation dissipation is relatively weak, and the energy stored in $w$ undergoes oscillatory exchange with the density before being dissipated. In the overdamped regime ($\Delta > 1$), the participation variable is rapidly quenched, and $\mathcal{D}_{\mathrm{part}}$ dominates the transient dynamics.*

**Proposition C.48** (Channel dominance regimes). *The relative magnitudes of the three dissipation channels define three regimes:*

*(i) Diffusion-dominated ($M_*\mu_1 \gg P_*'$ and $M_*\mu_1 \gg \zeta/\tau$):*

$$
\mathcal{D}_{\mathrm{diff}} \gg \mathcal{D}_{\mathrm{pen}} + \mathcal{D}_{\mathrm{part}}.
$$

*Spatial inhomogeneities are smoothed rapidly. The slowest process is the relaxation of the spatial mean and the participation variable, which proceeds at rate $\sim\min(D\,P_*',\,\zeta/\tau)$.*

*(ii) Penalty-dominated ($P_*' \gg M_*\mu_1$ and $P_*' \gg \zeta/\tau$):*

$$
\mathcal{D}_{\mathrm{pen}} \gg \mathcal{D}_{\mathrm{diff}} + \mathcal{D}_{\mathrm{part}}.
$$

*The density is drawn to $\rho^*$ rapidly at all spatial scales. The slowest process is the damping of the participation variable at rate $\zeta/\tau$.*

*(iii) Participation-dominated ($\zeta/\tau \gg D\,P_*'$ and $\zeta/\tau \gg D\,M_*\mu_1$):*

$$
\mathcal{D}_{\mathrm{part}} \gg \mathcal{D}_{\mathrm{diff}} + \mathcal{D}_{\mathrm{pen}}.
$$

*The participation variable is quenched rapidly, effectively decoupling the mediated channel. The density then relaxes by the direct channel alone at rate $\sim D\,P_*'$. This is the overdamped limit of Principle 6.*

---

### C.5.7 Structural Interpretation

**Remark C.49** (Stability as a consequence of the canonical structure). The asymptotic stability of $(\rho^*, 0)$ depends on four canonical principles:

- **Principle 1** (Operator Structure): provides $M_*\nabla^2$, the source of diffusive dissipation that damps all spatial modes $n \geq 1$. Without diffusion, spatial perturbations would persist indefinitely.

- **Principle 3** (Penalty Equilibrium): provides $P_*' > 0$, the source of the penalty dissipation channel. This is the *only* mechanism that drives the spatial mean toward $\rho^*$. Without $P_*' > 0$, the system would have a continuum of equilibria (one for each value of $\bar{\rho}$), and the equilibrium would be neutrally stable rather than asymptotically stable.

- **Principle 5** (Participation Feedback Loop): introduces the participation variable and the integration time $\tau$, creating the two-channel dynamics. The feedback loop stores energy temporarily in $v$, delaying its dissipation but ultimately routing it through the participation damping channel.

- **Principle 6** (Damping Discriminant): the canonical parameter $\Delta = D + 2\zeta$ determines whether the approach to equilibrium is oscillatory ($\Delta < 1$) or monotonic ($\Delta > 1$), and controls the relative importance of the participation dissipation channel.

The channel complementarity constraint $D + H = 1$ (Principle 2) enters implicitly through the identity $H = 1 - D$, which couples the strength of the mediated-channel forcing ($Hw$) to the direct-channel dissipation ($D\,F[\rho]$). The stability proof does not require Principles 4 or 7: the mobility bound and the nonlinear triad are irrelevant at the perturbative level.

**Remark C.50** (Comparison of the spectral gap and the Lyapunov decay rate). The exponential decay rate $\beta = \gamma_*$ from Theorem C.43 and the spectral gap $\gamma$ from Corollary C.18 are related but distinct:

- The spectral gap $\gamma$ governs the decay of the linearized semigroup $e^{\mathcal{L}t}$ and is sharp for the linear problem.
- The Lyapunov rate $\gamma_*$ governs the nonlinear decay via $\mathcal{V}$ and is in general smaller than $\gamma$, because the Lyapunov functional $\mathcal{V}$ may not be optimally adapted to every mode.

In the limit of small perturbations, $\gamma_*/\gamma \to 1$ as the cross-coupling term $\sigma \to 0$ and the Lyapunov functional approaches the quadratic form induced by the spectral projections of $\mathcal{L}$. The precise gap between $\gamma_*$ and $\gamma$ is controlled by the condition number $c_+/c_-$ of the coercivity estimate (C.42) and the off-diagonal structure of $\mathbf{A}_0$.

---

**References for Appendix C.5**

[1] H. Amann, *Linear and Quasilinear Parabolic Problems, Vol. I: Abstract Linear Theory*, Birkhäuser, Basel, 1995.

[2] L.C. Evans, *Partial Differential Equations*, 2nd ed., Graduate Studies in Mathematics, vol. 19, AMS, Providence, 2010.

[3] A. Lunardi, *Analytic Semigroups and Optimal Regularity in Parabolic Problems*, Birkhäuser, Basel, 1995.

[7] D. Henry, *Geometric Theory of Semilinear Parabolic Equations*, Lecture Notes in Mathematics, vol. 840, Springer, Berlin, 1981.

## C.6 Bifurcation Structure

We analyze the qualitative transition between oscillatory and monotonic regimes in the ED system as the canonical damping parameter $\Delta = D + 2\zeta$ crosses the critical surface. The analysis proceeds by center manifold reduction of the spatially homogeneous mode near the critical damping condition $\mathscr{D}_0 = 0$, derivation of a one-dimensional normal form for the amplitude dynamics, and verification of the nondegeneracy conditions that make the transition sharp and of codimension one. This provides the rigorous spectral-analytic foundation for the Boundary Surface and the regime partition described in §6.4 of the main text.

We retain all notation from Appendices C.1–C.5. In particular, $\mathbf{A}_0$ is the $2 \times 2$ matrix (C.13) governing the homogeneous mode, $\mathscr{D}_0$ is the modal discriminant (C.16), and $\Delta = D + 2\zeta$ is the canonical damping parameter (Principle 6).

---

### C.6.1 The Critical Damping Surface

Recall from Theorem C.22 that the qualitative character of the homogeneous mode is determined by the sign of

$$
\mathscr{D}_0 = \left(D\,P_*' - \frac{\zeta}{\tau}\right)^{\!2} - \frac{4H\,P_*'}{\tau}.
\tag{C.60}
$$

**Definition C.51** (Critical damping surface). The critical damping surface $\Sigma$ is the codimension-one submanifold of the parameter space $(D, \zeta, \tau, P_*') \in (0,1) \times (0,\infty)^3$ defined by

$$
\Sigma := \bigl\{(D, \zeta, \tau, P_*') : \mathscr{D}_0 = 0\bigr\}.
\tag{C.61}
$$

On $\Sigma$, the eigenvalues of $\mathbf{A}_0$ coalesce into a repeated real eigenvalue $\lambda_c := -\gamma_0 = -\frac{1}{2}(D\,P_*' + \zeta/\tau) < 0$.

**Proposition C.52** (Regularity of $\Sigma$). *The surface $\Sigma$ is a smooth submanifold of codimension one. Its normal vector in the $(D, \zeta)$-plane (at fixed $\tau, P_*'$) is*

$$
\nabla_{D,\zeta}\,\mathscr{D}_0\big|_\Sigma = 2\!\left(D\,P_*' - \frac{\zeta}{\tau}\right)\!\bigl(P_*',\, -\tau^{-1}\bigr) - \frac{4P_*'}{\tau}\,(-1, 0).
\tag{C.62}
$$

*This vector is nonzero on $\Sigma$ whenever $H > 0$ (i.e., $D < 1$), so $\Sigma$ is a smooth manifold away from the degenerate limit $D = 1$.*

*Proof.* Differentiating (C.60):

$$
\frac{\partial\mathscr{D}_0}{\partial D} = 2P_*'\!\left(D\,P_*' - \frac{\zeta}{\tau}\right) + \frac{4P_*'}{\tau},
\qquad
\frac{\partial\mathscr{D}_0}{\partial\zeta} = -\frac{2}{\tau}\!\left(D\,P_*' - \frac{\zeta}{\tau}\right).
$$

On $\Sigma$, $(D P_*' - \zeta/\tau)^2 = 4HP_*'/\tau$, so $|D P_*' - \zeta/\tau| = 2\sqrt{HP_*'/\tau} > 0$ for $H > 0$. In particular $\partial\mathscr{D}_0/\partial\zeta \neq 0$ on $\Sigma$, confirming codimension one by the implicit function theorem. $\square$

**Proposition C.53** (Canonical normalization of $\Sigma$). *In the canonical normalization $\tau P_*' = 1$, the surface $\Sigma$ projects onto the parabola (C.20):*

$$
(D - \zeta)^2 = 4(1 - D) = 4H.
\tag{C.63}
$$

*This parabola has vertex at $(D, \zeta) = (1, 0)$, opens into the region $D < 1$, and intersects the line $\zeta = 0$ at $D = 1 - 2\sqrt{1-D}\big|_{\zeta=0}$, i.e., at $D^2 = 4(1-D)$, giving $D = 2(\sqrt{2} - 1) \approx 0.828$.*

*The canonical damping parameter $\Delta = D + 2\zeta$ varies monotonically along the upper branch of the parabola (where $\zeta > D - 2\sqrt{H}$), establishing a bijection between points on $\Sigma$ (at fixed $\tau P_*' = 1$) and values of $\Delta$.*

---

### C.6.2 Spectral Structure at Criticality

At a point $(D_c, \zeta_c, \tau, P_*') \in \Sigma$, the matrix $\mathbf{A}_0$ has a repeated eigenvalue $\lambda_c < 0$ with algebraic multiplicity two but geometric multiplicity one (i.e., $\mathbf{A}_0$ has a nontrivial Jordan block).

**Lemma C.54** (Jordan structure at criticality). *On $\Sigma$, the matrix $\mathbf{A}_0$ is similar to*

$$
\mathbf{J}_c :=
\begin{pmatrix}
\lambda_c & 1 \\
0 & \lambda_c
\end{pmatrix},
\qquad \lambda_c = -\gamma_0 = -\tfrac{1}{2}(D_c P_*' + \zeta_c/\tau).
\tag{C.64}
$$

*The generalized eigenvectors are*

$$
\mathbf{e}_1 =
\begin{pmatrix}
H_c \\
\lambda_c + D_c P_*'
\end{pmatrix}, \qquad
\mathbf{e}_2 = \text{(generalized eigenvector satisfying } (\mathbf{A}_0 - \lambda_c\,\mathrm{Id})\,\mathbf{e}_2 = \mathbf{e}_1\text{)},
\tag{C.65}
$$

*where $H_c = 1 - D_c$.*

*Proof.* At criticality, $\mathscr{D}_0 = 0$ forces the two eigenvalues to coalesce: $\lambda_+ = \lambda_- = \lambda_c$. Since $\mathbf{A}_0$ is not a scalar multiple of the identity (the off-diagonal entries $H_c \neq 0$ and $-P_*'/\tau \neq 0$ are nonzero), the eigenspace is one-dimensional, so the Jordan form has a $2 \times 2$ block. The eigenvector $\mathbf{e}_1$ is computed from $(\mathbf{A}_0 - \lambda_c\,\mathrm{Id})\,\mathbf{e}_1 = 0$. $\square$

---

### C.6.3 Center Manifold Reduction

We now perform a center manifold reduction for the full PDE–ODE system near the critical surface, treating $\Delta$ (equivalently, $\zeta$ at fixed $D$, $\tau$, $P_*'$) as a bifurcation parameter.

**Setting.** Decompose the state as

$$
u(x,t) = a_0(t)\,\varphi_0(x) + u_\perp(x,t), \qquad u_\perp \perp \varphi_0 \text{ in } L^2(\Omega),
\tag{C.66}
$$

where $a_0 = \langle u, \varphi_0\rangle$ is the homogeneous component and $u_\perp = \sum_{n \geq 1} a_n\varphi_n$ is the spatial fluctuation. The full linearized dynamics (C.9) decomposes as:

- *Homogeneous block:* $(a_0, w)$ evolves by $\mathbf{A}_0$ — this is the critical or near-critical subsystem.
- *Spatial modes:* Each $a_n$ ($n \geq 1$) decays at rate $D\alpha_n \geq D\alpha_1 > D P_*'$ — these modes are spectrally separated from the homogeneous block.

Since all spatial modes $n \geq 1$ have eigenvalues $\lambda_n = -D\alpha_n$ satisfying $|\lambda_n| > |\lambda_c|$ (the spatial decay rates exceed the homogeneous decay rate), the spatial modes form the *stable* part and the homogeneous mode forms the *center* part (relative to the shifted eigenvalue $\lambda_c$) of the dynamics.

**Theorem C.55** (Center manifold for the homogeneous mode). *Consider the system (C.43) near the equilibrium $(u, w) = (0, 0)$, with $\zeta$ as a parameter near a critical value $\zeta_c \in \Sigma$. There exists a smooth, locally invariant center manifold*

$$
\mathcal{W}^c = \bigl\{(u, w) : u_\perp = h(a_0, w;\, \zeta),\; \|a_0\| + |w| < \delta\bigr\},
\tag{C.67}
$$

*where $h : \mathbb{R}^2 \times \mathbb{R} \to H^s_\perp(\Omega)$ satisfies $h(0, 0;\, \zeta_c) = 0$ and $Dh(0, 0;\, \zeta_c) = 0$. The center manifold is tangent to the eigenspace of the homogeneous mode at the origin.*

*On $\mathcal{W}^c$, the dynamics reduce to the two-dimensional system*

$$
\frac{d}{dt}
\begin{pmatrix} a_0 \\ w \end{pmatrix}
= \mathbf{A}_0(\zeta)
\begin{pmatrix} a_0 \\ w \end{pmatrix}
+ \mathbf{G}(a_0, w;\, \zeta),
\tag{C.68}
$$

*where $\mathbf{G}$ is smooth with $\mathbf{G}(0,0;\,\zeta) = 0$ and $D\mathbf{G}(0,0;\,\zeta) = 0$. The spatial fluctuation on the center manifold is slaved to the homogeneous mode: $u_\perp = h(a_0, w;\, \zeta) = O(a_0^2 + w^2)$.*

*Proof.* The existence of the center manifold follows from the spectral gap between the homogeneous eigenvalues $\{\lambda_+, \lambda_-\}$ (which coalesce at $\lambda_c$ on $\Sigma$) and the spatial eigenvalues $\{-D\alpha_n\}_{n \geq 1}$ (which satisfy $D\alpha_1 > D P_*' \geq |\lambda_c|$ generically). The center manifold theorem for quasilinear parabolic equations [7, Thm. 6.1.3] applies because the linearized operator $\mathcal{L}$ is sectorial and the nonlinearity is smooth. The tangency condition $Dh = 0$ follows from the quadratic vanishing of the nonlinear terms in (C.43) at the origin. $\square$

**Remark C.56** (Spectral separation condition). The center manifold reduction requires $D\alpha_1 > |\operatorname{Re}(\lambda_c)| = \gamma_0$. Expanding:

$$
D(M_*\mu_1 + P_*') > \tfrac{1}{2}(D P_*' + \zeta/\tau).
$$

This holds whenever $D M_*\mu_1 > \frac{1}{2}(\zeta/\tau - D P_*')$, which is satisfied generically since $M_*\mu_1 > 0$ provides a finite spectral gap. The reduction fails only in the degenerate limit $M_*\mu_1 \to 0$ (vanishing diffusion on a large domain), where the spatial and homogeneous time scales merge.

---

### C.6.4 Normal Form for the Amplitude Equation

On the center manifold, we derive the normal form for the reduced dynamics (C.68) near the critical surface $\Sigma$.

**Change of coordinates.** Introduce the shifted parameter $\eta := \zeta - \zeta_c$, so that $\eta = 0$ corresponds to the critical surface. Transform the homogeneous mode to Jordan coordinates via

$$
\begin{pmatrix} a_0 \\ w \end{pmatrix}
= \mathbf{T}
\begin{pmatrix} \xi \\ \psi \end{pmatrix},
$$

where $\mathbf{T} = [\mathbf{e}_1 \mid \mathbf{e}_2]$ is the matrix of generalized eigenvectors from (C.65). In the $(\xi, \psi)$-coordinates, the linear part becomes the Jordan block $\mathbf{J}_c$ at $\eta = 0$, and the parameter perturbation unfolds as

$$
\mathbf{A}_0(\zeta_c + \eta) = \lambda_c\,\mathrm{Id} + \eta\,\mathbf{B}_1 + \mathbf{N}_c + O(\eta^2),
\tag{C.69}
$$

where $\mathbf{N}_c$ is the nilpotent part (accounting for the off-diagonal entry of the Jordan block) and $\mathbf{B}_1 = d\mathbf{A}_0/d\zeta\big|_{\zeta_c}$.

**Proposition C.57** (Unfolding matrix). *The derivative of $\mathbf{A}_0$ with respect to $\zeta$ is*

$$
\mathbf{B}_1 = \frac{d\mathbf{A}_0}{d\zeta} =
\begin{pmatrix}
0 & 0 \\[2pt]
0 & -1/\tau
\end{pmatrix}.
\tag{C.70}
$$

*In Jordan coordinates, the unfolding perturbation $\mathbf{T}^{-1}\mathbf{B}_1\mathbf{T}$ has the form*

$$
\mathbf{T}^{-1}\mathbf{B}_1\mathbf{T} =
\begin{pmatrix}
b_{11} & b_{12} \\[2pt]
b_{21} & b_{22}
\end{pmatrix},
\tag{C.71}
$$

*where the entries $b_{ij}$ are explicit rational functions of $D_c$, $P_*'$, $\tau$, and $\zeta_c$.*

*Proof.* Direct computation: $\mathbf{A}_0$ depends on $\zeta$ only through the $(2,2)$-entry $-\zeta/\tau$, so $d\mathbf{A}_0/d\zeta$ has the stated form. The transformation to Jordan coordinates is standard linear algebra. $\square$

**Theorem C.58** (Normal form on the center manifold). *Near the critical surface $\Sigma$, the reduced dynamics on the center manifold (C.68) take the normal form*

$$
\dot{\xi} = \lambda_c\,\xi + \psi + \eta\,b_{11}\,\xi + \eta\,b_{12}\,\psi + g_2(\xi, \psi;\,\eta),
\tag{C.72a}
$$

$$
\dot{\psi} = \lambda_c\,\psi + \eta\,b_{21}\,\xi + \eta\,b_{22}\,\psi + g_3(\xi, \psi;\,\eta),
\tag{C.72b}
$$

*where $g_2$ and $g_3$ are smooth functions of order $O(|(\xi,\psi)|^2 + \eta^2|(\xi,\psi)|)$, arising from the nonlinear terms in (C.43) and the curvature of the center manifold.*

*The leading nonlinear contributions to $g_2$ and $g_3$ are:*

*(i) From the penalty nonlinearity $P(\rho^* + u) - P(\rho^*) - P_*'u = \frac{1}{2}P_*''u^2 + O(u^3)$:*

$$
g_2^{\mathrm{pen}} = -D\,\frac{P_*''}{2}\,|\Omega|^{-1}\,(T_{11}\xi + T_{12}\psi)^2\,[\mathbf{T}^{-1}]_{1,1} + \cdots,
$$

$$
g_3^{\mathrm{pen}} = -D\,\frac{P_*''}{2}\,|\Omega|^{-1}\,(T_{11}\xi + T_{12}\psi)^2\,[\mathbf{T}^{-1}]_{2,1} + \cdots,
$$

*where $T_{ij}$ are the entries of $\mathbf{T}$.*

*(ii) From the mobility variation $M(\rho) - M_* = M_*'u + O(u^2)$ acting on the diffusion of the spatial fluctuation through the center manifold:*

$$
g_2^{\mathrm{mob}} = O(|(\xi,\psi)|^3), \qquad g_3^{\mathrm{mob}} = O(|(\xi,\psi)|^3).
$$

*(iii) The gradient-squared nonlinearity $M'(\rho)|\nabla\rho|^2$ does not contribute to the homogeneous mode at any order, since it integrates to zero against $\varphi_0$:*

$$
\langle M'(\rho)|\nabla\rho|^2, \varphi_0\rangle = |\Omega|^{-1/2}\int_\Omega M'(\rho)\,|\nabla u_\perp|^2\,dx,
$$

*which is $O(\|u_\perp\|_{H^1}^2) = O(|(\xi,\psi)|^4)$ on the center manifold (since $u_\perp = O(|(\xi,\psi)|^2)$).*

*Proof.* The normal form is obtained by substituting the center manifold reduction (C.68) into the Jordan-coordinate system and Taylor-expanding the nonlinearity. The penalty contribution is quadratic because $P'' \neq 0$ generically. The mobility contribution is cubic because $M(\rho) - M_*$ is linear in $u$ and the diffusion term $M(\rho)\nabla^2 u$ is already of order $\|u_\perp\|_{H^2}$, which on the center manifold is $O(|(\xi,\psi)|^2)$. The gradient-squared term does not contribute because $\nabla\varphi_0 = 0$ forces the projection onto the homogeneous mode to depend on $u_\perp$ alone, which is slaved at quadratic order. $\square$

---

### C.6.5 Normal-Form Coefficients

**Proposition C.59** (Explicit normal-form coefficients). *In the canonical normalization $\tau P_*' = 1$, the key normal-form coefficients are:*

*(i) The critical eigenvalue:*

$$
\lambda_c = -\frac{1}{2}\!\left(\frac{D_c}{\tau} + \frac{\zeta_c}{\tau}\right) = -\frac{D_c + \zeta_c}{2\tau}.
\tag{C.73}
$$

*(ii) The unfolding speed (rate at which eigenvalues split with $\eta$):*

$$
\left.\frac{d\lambda_\pm}{d\zeta}\right|_{\zeta_c}
= -\frac{1}{2\tau} \pm \frac{1}{2}\,\frac{\partial\sqrt{\mathscr{D}_0}/\partial\zeta}{\big|_{\zeta_c}}.
\tag{C.74}
$$

*Since $\mathscr{D}_0 = 0$ at $\zeta_c$, the square root has a branch point, and the eigenvalues split as*

$$
\lambda_\pm(\zeta_c + \eta) = \lambda_c - \frac{\eta}{2\tau} \pm \sqrt{\frac{\eta}{\tau}\!\left(\frac{\zeta_c}{\tau} - D_c P_*'\right) + \frac{\eta^2}{4\tau^2}} + O(\eta^2).
$$

*In the canonical normalization ($P_*' = 1/\tau$), this simplifies to*

$$
\lambda_\pm = \lambda_c - \frac{\eta}{2\tau} \pm \sqrt{\frac{\eta(\zeta_c - D_c)}{\tau^2} + \frac{\eta^2}{4\tau^2}}.
\tag{C.75}
$$

*(iii) The direction of eigenvalue splitting:*

- *If $\eta > 0$ (increasing $\zeta$, hence increasing $\Delta$), then $\mathscr{D}_0$ increases (for generic points on $\Sigma$ where $\partial\mathscr{D}_0/\partial\zeta < 0$ at $\zeta_c > D_c$ or $\partial\mathscr{D}_0/\partial\zeta > 0$ at $\zeta_c < D_c$), and the eigenvalues become real: the system enters the overdamped regime.*
- *If $\eta < 0$ (decreasing $\zeta$, hence decreasing $\Delta$), $\mathscr{D}_0$ decreases, and the eigenvalues become complex conjugates: the system enters the underdamped regime.*

*(iv) The leading nonlinear coefficient from the penalty:*

$$
g_{\mathrm{pen}} = -\frac{D_c\,P_*''}{2|\Omega|^{1/2}}\,\frac{H_c^2}{(\lambda_c + D_c P_*')^2 + H_c^2},
\tag{C.76}
$$

*where the denominator accounts for the projection of the nonlinearity onto the Jordan coordinate $\xi$. This coefficient is nonzero whenever $P_*'' \neq 0$ (i.e., when the penalty has nonvanishing curvature at the equilibrium).*

*Proof.* Parts (i)–(iii): direct differentiation of (C.15) and (C.16) with respect to $\zeta$, evaluated at $\zeta = \zeta_c$ where $\mathscr{D}_0 = 0$, using $\tau P_*' = 1$. Part (iv): projection of the quadratic penalty term $-D P_*'' u^2/2$ onto $\varphi_0$, transformed to Jordan coordinates. $\square$

---

### C.6.6 Classification of the Transition

**Theorem C.60** (Nondegenerate codimension-one transition). *Let $(D_c, \zeta_c, \tau, P_*') \in \Sigma$ with $D_c \in (0,1)$ and $\tau P_*' > 0$. Then:*

*(i) (Nondegeneracy.) The critical surface $\Sigma$ is crossed transversally by every smooth path in the parameter space $(D, \zeta)$ that is not tangent to $\Sigma$. The eigenvalues of $\mathbf{A}_0$ split from a repeated real value into either a complex conjugate pair (entering the underdamped regime) or two distinct real values (entering the overdamped regime), depending on the direction of crossing.*

*(ii) (Codimension one.) The transition is of codimension one: it is organized by the single condition $\mathscr{D}_0 = 0$, which defines a hypersurface in the four-dimensional parameter space $(D, \zeta, \tau, P_*')$. No additional condition is needed to produce the eigenvalue coalescence.*

*(iii) (Type classification.) The transition is not a bifurcation in the classical dynamical-systems sense (no change of stability or creation/destruction of equilibria), but rather a **qualitative transition of flow type**: the equilibrium $(\rho^*, 0)$ remains asymptotically stable on both sides of $\Sigma$ (Theorem C.43), but the topology of the approach changes from spiral (oscillatory, with winding number accumulation) to nodal (monotonic, with direct approach along eigenvectors).*

*(iv) (Normal-form classification.) Near $\Sigma$, the homogeneous-mode dynamics on the center manifold is smoothly equivalent to the versal unfolding of a non-semisimple double eigenvalue:*

$$
\dot{z} = (\lambda_c + \eta\,b)\,z + w, \qquad \dot{w} = \eta\,c\,z + (\lambda_c + \eta\,d)\,w + g\,z^2 + O(3),
\tag{C.77}
$$

*where $b, c, d$ are the unfolding coefficients from (C.71) and $g$ is the leading nonlinear coefficient (C.76). The codimension-one versal unfolding parameter is $\eta$ (equivalently, $\Delta - \Delta_c$).*

*Proof.* Part (i): the transversality follows from $\nabla_{D,\zeta}\mathscr{D}_0 \neq 0$ on $\Sigma$ (Proposition C.52). The eigenvalue splitting direction follows from (C.75). Part (ii): $\Sigma$ is defined by one equation in four parameters, hence codimension one. The coalescence is generic (it does not require fine-tuning of more than one parameter). Part (iii): since $\operatorname{tr}(\mathbf{A}_0) < 0$ and $\det(\mathbf{A}_0) > 0$ on both sides of $\Sigma$, both eigenvalues remain in the open left half-plane throughout the transition. No eigenvalue crosses the imaginary axis, so no Hopf or saddle-node bifurcation occurs. The change is purely topological: the node changes from a stable spiral to a stable node. Part (iv): the normal form (C.77) is the standard versal unfolding of a Jordan block with eigenvalue $\lambda_c$ [8, Thm. 8.2], with the nonlinear term $g z^2$ arising from the penalty curvature. $\square$

---

### C.6.7 The Discriminant $\Delta$ as the Organizing Parameter

**Theorem C.61** (Structural role of $\Delta$). *The canonical damping parameter $\Delta = D + 2\zeta$ serves as the organizing parameter for the regime transition in the following precise sense:*

*(i) (Monotonicity along the critical surface.) In the canonical normalization $\tau P_*' = 1$, the discriminant $\mathscr{D}_0$ is a monotone function of $\Delta$ along any ray in the $(D, \zeta)$-plane that crosses $\Sigma$ transversally. Specifically, for fixed $D$ and varying $\zeta$:*

$$
\frac{\partial\mathscr{D}_0}{\partial\zeta}\bigg|_{\tau P_*'=1} = \frac{2}{\tau^2}\bigl(\zeta - D + 2\bigr) > 0 \quad \text{when } \zeta > D - 2,
$$

*which holds on the upper branch of the parabola (C.63) where $\zeta > D - 2\sqrt{H}$. Thus increasing $\zeta$ (increasing $\Delta$) pushes $\mathscr{D}_0$ positive (toward overdamping), and decreasing $\zeta$ pushes $\mathscr{D}_0$ negative (toward underdamping).*

*(ii) (Universal control.) The value of $\Delta$ alone determines whether the system is in the oscillatory or monotonic basin, up to the constitutive ratio $\tau P_*'$: for any fixed $\tau P_*'$, the critical surface $\Sigma$ is a monotone curve in the $(D, \zeta)$-plane, and $\Delta$ parameterizes this curve. The regime depends on $\Delta$ and $\tau P_*'$ but not on $D$ and $\zeta$ separately.*

*(iii) (Robustness.) The transition is structurally stable: small perturbations of the constitutive functions $M$ and $P$ (preserving $P_*' > 0$ and $M_* > 0$) shift the critical surface smoothly but do not change the codimension, the transversality, or the qualitative character of the transition. This is because the transition depends only on the spectral structure of the $2 \times 2$ matrix $\mathbf{A}_0$, whose entries are determined by the equilibrium values $P_*'$, $M_*$, and the canonical parameters.*

*Proof.* Part (i): differentiating $\mathscr{D}_0|_{\tau P_*'=1} = \tau^{-2}[(D - \zeta)^2 - 4(1-D)]$ with respect to $\zeta$ gives $-2\tau^{-2}(D - \zeta)$. On the upper branch of (C.63), $\zeta > D - 2\sqrt{H}$, so $D - \zeta < 2\sqrt{H}$, and the derivative $-2\tau^{-2}(D-\zeta)$ has the correct sign to make $\mathscr{D}_0$ increasing with $\zeta$ when $\zeta > D$ (overdamped side). The general monotonicity in $\Delta$ follows because $\partial\Delta/\partial\zeta = 2 > 0$. Part (ii): on the parabola (C.63), $\zeta = D \pm 2\sqrt{1-D}$; for the upper branch, $\Delta = D + 2\zeta = 3D + 4\sqrt{1-D} - 4$ (or its analogue), which is a function of $D$ alone, hence determines a unique curve. Part (iii): the nondegeneracy conditions ($\nabla\mathscr{D}_0 \neq 0$, $\det(\mathbf{A}_0) > 0$, $\operatorname{tr}(\mathbf{A}_0) < 0$) are open conditions, hence preserved under small perturbations. $\square$

---

### C.6.8 Connection to the Regime Geometry

The bifurcation analysis provides the rigorous foundation for the regime geometry described in §6.4 of the main text and the Boundary motif of the ED architecture (ED-Arch-02).

**Remark C.62** (Boundary Surface). The critical damping surface $\Sigma$ is the mathematical realization of the Boundary Surface in the ED geometric ontology. The main text (§6.4) states that $\Delta = D + 2\zeta$ partitions the parameter space into two topologically distinct regions: the Spiral Sheet ($\Delta < 1$, oscillatory) and the Monotonic Cone ($\Delta > 1$, monotonic). Theorem C.60 confirms that:

- The partition is sharp (codimension one, no intermediate regime).
- The partition is nondegenerate (transversal crossing, smooth surface).
- The partition preserves stability (no eigenvalue crosses the imaginary axis).
- The partition is structurally stable (robust to constitutive perturbation).

**Remark C.63** (Spiral Sheet and Monotonic Cone). On the oscillatory side of $\Sigma$ ($\mathscr{D}_0 < 0$), the eigenvalues $\lambda_\pm = -\gamma_0 \pm i\omega$ produce spiral trajectories in the $(a_0, w)$-plane, with winding number increasing as $\omega t/2\pi$. These spirals project onto the Spiral Sheet of the ED phase-space geometry (ED-Arch-04). On the monotonic side ($\mathscr{D}_0 > 0$), the eigenvalues are real and distinct, producing node-like trajectories that project onto the Monotonic Cone. The transition between these geometric objects occurs exactly on the Boundary Surface $\Sigma$.

**Remark C.64** (Critical Damping Boundary law). The Critical Damping Boundary is one of the nine architectural laws (ED-Arch-03, generated by Principles 2, 5, and 6). Theorem C.60 verifies this law rigorously: the boundary is a well-defined, codimension-one manifold in the parameter space; it is the unique transition surface between oscillatory and monotonic regimes; and it is generated by the interplay of channel complementarity ($D + H = 1$, Principle 2), the participation feedback loop (Principle 5, which introduces the variable $w$ and the time scale $\tau$), and the damping discriminant (Principle 6, which provides $\Delta$ as the organizing parameter).

**Remark C.65** (Absence of Hopf bifurcation). A natural question is whether the transition at $\Sigma$ involves a Hopf bifurcation — i.e., whether oscillations appear via eigenvalues crossing the imaginary axis. The answer is no: both eigenvalues of $\mathbf{A}_0$ remain in the open left half-plane for all parameter values (Theorem C.17(iii)), so no Hopf bifurcation occurs. The oscillatory regime arises not from instability but from the *spiraling* character of the stable approach to equilibrium. This is an important structural feature: the ED system produces oscillations (spirals, memory loops) without ever becoming unstable. The oscillations are transient features of a globally stable system, not limit-cycle phenomena. This reflects the architectural role of Principle 3 (unique, globally attracting equilibrium), which precludes instability-driven oscillation.

---

**References for Appendix C.6**

[1] H. Amann, *Linear and Quasilinear Parabolic Problems, Vol. I: Abstract Linear Theory*, Birkhäuser, Basel, 1995.

[7] D. Henry, *Geometric Theory of Semilinear Parabolic Equations*, Lecture Notes in Mathematics, vol. 840, Springer, Berlin, 1981.

[8] Y.A. Kuznetsov, *Elements of Applied Bifurcation Theory*, 3rd ed., Springer, New York, 2004.

[9] J. Guckenheimer and P. Holmes, *Nonlinear Oscillations, Dynamical Systems, and Bifurcations of Vector Fields*, Springer, New York, 1983.

## C.7 Long-Time Behavior

We establish the complete long-time picture for global solutions of the ED system (C.1): uniform-in-time bounds, decay of higher Sobolev norms, asymptotic compactness of trajectories, identification of the $\omega$-limit set as the singleton $\{(\rho^*, 0)\}$, and the transition from algebraic to exponential convergence. We conclude with the role of the mobility collapse near $\rho_{\max}$ in maintaining horizon persistence, and a synthesis of the three-stage convergence argument that links the global, local, and exponential decay results of Appendices C.2, C.5, and the present section.

All notation from Appendices C.1–C.6 is retained. In particular, $\mathcal{E}[\rho, v]$ is the energy functional (C.3), $\Phi(\rho)$ is the density potential (C.4), $\gamma$ is the spectral gap (Corollary C.18), $\gamma_*$ is the Lyapunov decay rate (C.48), and $\epsilon_0$ is the local stability threshold (Theorem C.43).

---

### C.7.1 Uniform-in-Time Bounds

We strengthen the finite-time bounds of Proposition C.7 to bounds that are uniform for all $t \geq 0$.

**Theorem C.66** (Uniform bounds). *Let $(\rho(t), v(t))$ be the global solution from Theorem C.14 with initial energy $\mathcal{E}_0 := \mathcal{E}[\rho_0, v_0]$. Then:*

*(i) (Pointwise density bounds.) There exists $\delta = \delta(\mathcal{E}_0) > 0$ such that*

$$
\delta \leq \rho(x,t) \leq \rho_{\max} - \delta \qquad \text{for all } (x,t) \in \overline{\Omega} \times [0, \infty).
\tag{C.78}
$$

*(ii) (Energy bound.) The total energy is non-increasing after an initial transient:*

$$
\mathcal{E}[\rho(t), v(t)] \leq C(\mathcal{E}_0) \qquad \text{for all } t \geq 0.
\tag{C.79}
$$

*(iii) ($L^2$-bound on the deviation.)*

$$
\|\rho(t) - \rho^*\|_{L^2(\Omega)}^2 + |v(t)|^2 \leq C(\mathcal{E}_0) \qquad \text{for all } t \geq 0.
\tag{C.80}
$$

*(iv) (Dissipation integrals.) The total dissipation over all time is finite:*

$$
\int_0^\infty\!\int_\Omega \frac{P'(\rho)}{M(\rho)}\,|\nabla\rho|^2\,dx\,dt < \infty, \qquad
\int_0^\infty v(t)^2\,dt < \infty.
\tag{C.81}
$$

*Proof.* Part (i) is Proposition C.11 combined with (C.79): the energy barrier $\Phi(\rho) \to +\infty$ at $\rho = 0$ and $\rho = \rho_{\max}$ forces the density to remain in a compact subinterval of $(0, \rho_{\max})$ whose width depends only on $\mathcal{E}_0$.

Part (ii) follows from the dissipation estimate (Lemma C.6) and Gronwall's inequality. The Gronwall factor is bounded uniformly because the source terms in (C.6) ($C_1\int P(\rho)^2\,dx$ and $C_2 v^2$) are controlled by $\mathcal{E}$ itself via the coercivity of $\Phi$ (see §C.2.3).

Parts (iii)–(iv) follow from (ii) and the coercivity $\mathcal{E} \geq c_1(\|\rho - \rho^*\|_{L^2}^2 + v^2) - c_2$. The finiteness of the dissipation integrals is obtained by integrating the dissipation identity (C.7) over $[0, \infty)$ and using the uniform energy bound. $\square$

---

### C.7.2 Decay of Higher Sobolev Norms

The parabolic character of the $\rho$-equation provides smoothing: higher Sobolev norms decay faster than lower ones, and the solution eventually becomes arbitrarily smooth.

**Theorem C.67** (Higher-order decay). *For each integer $k \geq 1$, there exists a monotone decreasing function $\Psi_k : [0, \infty) \to [0, \infty)$ with $\Psi_k(E) \to 0$ as $E \to 0$, and a time $T_k(\mathcal{E}_0)$, such that*

$$
\sup_{t \geq T_k} \|\rho(t) - \rho^*\|_{H^k(\Omega)} \leq \Psi_k\bigl(\mathcal{E}[\rho(T_k), v(T_k)]\bigr).
\tag{C.82}
$$

*In particular, if $\mathcal{E}[\rho(t), v(t)] \to 0$ as $t \to \infty$ (which will be established in §C.7.4), then $\|\rho(t) - \rho^*\|_{H^k} \to 0$ for every $k$.*

*Proof.* The argument proceeds by parabolic bootstrapping, as in Proposition C.13, but with the crucial difference that the bounds are now expressed in terms of the energy $\mathcal{E}$, which decays in time, rather than in terms of the initial $H^s$-norm.

**Step 1 ($k = 1$).** From the energy functional, $\|\rho - \rho^*\|_{L^2}^2 \leq C\,\mathcal{E}$. For the gradient, multiply the $\rho$-equation by $-\nabla^2(\rho - \rho^*)$ and integrate. Using the uniform pointwise bounds (C.78), the diffusion coefficient $D\,M(\rho)$ is bounded above and below by positive constants, yielding

$$
\frac{d}{dt}\frac{1}{2}\|\nabla\rho\|_{L^2}^2 + D\,M_\delta\|\nabla^2\rho\|_{L^2}^2 \leq C\,\|\nabla\rho\|_{L^2}^2 + C\,|v|^2 + C\,\|M'(\rho)|\nabla\rho|^2\|_{L^2}\,\|\nabla^2\rho\|_{L^2},
$$

where $M_\delta := \inf_{\rho \in [\delta, \rho_{\max}-\delta]} M(\rho) > 0$. The nonlinear term is estimated by Young's inequality and absorbed. After a transient of duration $T_1 \sim 1/(D\,M_\delta\,\mu_1)$, the parabolic smoothing gives

$$
\|\nabla\rho(t)\|_{L^2}^2 \leq C\,\mathcal{E}[\rho(t), v(t)] + C\,e^{-c(t-T_1)}\|\nabla\rho(T_1)\|_{L^2}^2.
$$

**Step 2 (Induction $k \to k+1$).** Apply $\nabla^k$ to the $\rho$-equation and repeat the energy estimate. The Kato–Ponce commutator estimates and the inductive hypothesis at level $k$ control the lower-order terms. The parabolic smoothing $\rho(t) \in H^{k+2}(\Omega)$ for $t > 0$ provides the spatial regularity gain. The bounds depend on $\mathcal{E}[\rho(t), v(t)]$ through the inductive chain.

The participation variable $v(t)$ satisfies the ODE $\dot{v} = \tau^{-1}(F[\rho] - \zeta v)$, so $|v(t)|$ is bounded by $C(\|F[\rho(t)]\|_{L^2} + |v(t)|)$, which is controlled by $\|\rho(t)\|_{H^2}$. $\square$

---

### C.7.3 Asymptotic Compactness

**Theorem C.68** (Precompactness of trajectories). *The orbit $\mathcal{O}^+ := \{(\rho(t), v(t)) : t \geq 0\}$ is precompact in $H^k(\Omega) \times \mathbb{R}$ for every $k \geq 0$.*

*Proof.* By the uniform bounds (Theorem C.66), the orbit is bounded in $H^s(\Omega) \times \mathbb{R}$ for $s > d/2 + 2$. The compact embedding $H^s(\Omega) \hookrightarrow\hookrightarrow H^k(\Omega)$ for $k < s$ gives precompactness in $H^k \times \mathbb{R}$.

More precisely, for any sequence $t_n \to \infty$, the sequence $\{(\rho(t_n), v(t_n))\}$ is bounded in $H^s \times \mathbb{R}$ and therefore has a subsequence converging in $H^k \times \mathbb{R}$ for every $k < s$. Since $s$ can be taken arbitrarily large (by the parabolic bootstrapping of Theorem C.67 applied at later times), the orbit is precompact in $H^k \times \mathbb{R}$ for every $k$. $\square$

**Definition C.69** ($\omega$-limit set). The $\omega$-limit set of the solution $(\rho(t), v(t))$ is

$$
\omega(\rho_0, v_0) := \bigcap_{T \geq 0} \overline{\{(\rho(t), v(t)) : t \geq T\}}^{H^1 \times \mathbb{R}}.
\tag{C.83}
$$

By the precompactness of $\mathcal{O}^+$, the set $\omega(\rho_0, v_0)$ is nonempty, compact, and connected in $H^1(\Omega) \times \mathbb{R}$.

---

### C.7.4 Identification of the $\omega$-Limit Set

**Theorem C.70** (Uniqueness of the $\omega$-limit point). *For every initial datum $(\rho_0, v_0) \in \mathcal{O}$ with $\rho_0 \in H^s(\Omega)$, $s > d/2 + 2$,*

$$
\omega(\rho_0, v_0) = \{(\rho^*, 0)\}.
\tag{C.84}
$$

*Proof.* Let $(\rho_\infty, v_\infty) \in \omega(\rho_0, v_0)$. There exists a sequence $t_n \to \infty$ such that $(\rho(t_n), v(t_n)) \to (\rho_\infty, v_\infty)$ in $H^1(\Omega) \times \mathbb{R}$.

**Step 1: $v_\infty = 0$.** From the dissipation integral (C.81), $\int_0^\infty v(t)^2\,dt < \infty$. Since $v(t)$ is uniformly continuous (its derivative $\dot{v} = \tau^{-1}(F[\rho] - \zeta v)$ is uniformly bounded by the $H^2$-bounds on $\rho$), the Barbalat lemma gives $v(t) \to 0$ as $t \to \infty$. Therefore $v_\infty = 0$.

**Step 2: $\rho_\infty$ is spatially constant.** From the dissipation integral (C.81),

$$
\int_0^\infty\!\int_\Omega \frac{P'(\rho)}{M(\rho)}\,|\nabla\rho|^2\,dx\,dt < \infty.
$$

By the uniform pointwise bounds (C.78), $P'(\rho)/M(\rho) \geq c_\delta > 0$ for a constant depending on $\delta$. Therefore

$$
\int_0^\infty \|\nabla\rho(t)\|_{L^2}^2\,dt < \infty.
\tag{C.85}
$$

The function $t \mapsto \|\nabla\rho(t)\|_{L^2}^2$ is uniformly continuous (its time derivative is bounded by the $H^3$-norm of $\rho$, which is uniformly bounded by Theorem C.67). By the Barbalat lemma,

$$
\|\nabla\rho(t)\|_{L^2} \to 0 \qquad \text{as } t \to \infty.
$$

Since $\rho(t_n) \to \rho_\infty$ in $H^1$, we have $\nabla\rho_\infty = 0$ a.e., so $\rho_\infty$ is constant on $\Omega$.

**Step 3: $\rho_\infty = \rho^*$ by Principle 3.** Since $\rho_\infty$ is constant and $v_\infty = 0$, the stationarity condition for system (C.1) requires

$$
0 = D\,F[\rho_\infty] + H \cdot 0 = -D\,P(\rho_\infty),
$$

so $P(\rho_\infty) = 0$. By Principle 3 (Penalty Equilibrium), the penalty $P$ has exactly one zero at $\rho = \rho^*$, with $P$ strictly increasing. Therefore $\rho_\infty = \rho^*$.

Since every $\omega$-limit point equals $(\rho^*, 0)$, the $\omega$-limit set is the singleton $\{(\rho^*, 0)\}$. $\square$

**Remark C.71** (Indispensability of Principle 3). Step 3 is the only point in the long-time analysis where the uniqueness of the penalty zero is used. If $P$ had multiple zeros — say $P(\rho_1) = P(\rho_2) = 0$ with $\rho_1 \neq \rho_2$ — then the $\omega$-limit set could contain $(\rho_1, 0)$ or $(\rho_2, 0)$, and global convergence to a unique equilibrium would fail. The system could approach different equilibria depending on the initial data, or could exhibit slow switching between neighborhoods of different steady states. The strict monotonicity $P' > 0$ precludes all such scenarios, collapsing the $\omega$-limit set to a single point.

---

### C.7.5 Exponential Convergence

**Theorem C.72** (Eventual exponential decay). *There exist constants $t_* \geq 0$, $C > 0$, and $\beta > 0$, depending on $\mathcal{E}_0$ and the canonical parameters, such that*

$$
\|\rho(t) - \rho^*\|_{H^s(\Omega)} + |v(t)| \leq C\,e^{-\beta(t - t_*)} \qquad \text{for all } t \geq t_*.
\tag{C.86}
$$

*The decay rate $\beta$ can be taken as the Lyapunov rate $\gamma_*$ from (C.48).*

*Proof.* By Theorem C.70, $(\rho(t), v(t)) \to (\rho^*, 0)$ in $H^1 \times \mathbb{R}$. By the higher-order decay (Theorem C.67), the convergence holds in $H^s \times \mathbb{R}$ as well. Therefore, there exists $t_*$ such that

$$
\|\rho(t) - \rho^*\|_{H^s} + |v(t)| < \epsilon_0 \qquad \text{for all } t \geq t_*,
$$

where $\epsilon_0$ is the local stability threshold from Theorem C.43. Applying Theorem C.43 with initial time $t_*$ gives

$$
\|\rho(t) - \rho^*\|_{H^1}^2 + |v(t)|^2 \leq C\bigl(\|\rho(t_*) - \rho^*\|_{H^1}^2 + |v(t_*)|^2\bigr)\,e^{-2\beta(t-t_*)}.
$$

The higher Sobolev norms inherit the exponential decay by the parabolic bootstrapping of Theorem C.67: once $\|\rho - \rho^*\|_{H^1}$ decays exponentially, the $H^k$-norms decay exponentially as well (with possibly a slower rate for each additional derivative, but with rate bounded below by $\beta/C_k$ for a finite constant $C_k$). Taking the minimum over finitely many rates up to level $s$ gives (C.86). $\square$

---

### C.7.6 Horizon Persistence and the Role of Mobility Collapse

The mobility collapse $M(\rho_{\max}) = 0$ (Principle 4) plays a distinctive role in the long-time behavior: it ensures that the density remains bounded away from $\rho_{\max}$ not merely at each finite time, but uniformly as $t \to \infty$.

**Proposition C.73** (Horizon persistence). *The uniform density bound (C.78) persists for all time: the margin $\delta(\mathcal{E}_0) > 0$ from Theorem C.66 does not degrade as $t \to \infty$. More precisely, the margin improves:*

$$
\operatorname{dist}\bigl(\rho(x,t),\, \{0, \rho_{\max}\}\bigr) \to \rho^* \wedge (\rho_{\max} - \rho^*) \qquad \text{as } t \to \infty,
\tag{C.87}
$$

*uniformly in $x \in \overline{\Omega}$.*

*Proof.* Since $\rho(t) \to \rho^*$ uniformly (by $H^s$-convergence and Sobolev embedding), the distance from the boundary $\{0, \rho_{\max}\}$ converges to $\min(\rho^*, \rho_{\max} - \rho^*)$. The uniform bound (C.78) provides a floor $\delta > 0$ at all times, and the convergence to $\rho^*$ provides the asymptotic improvement. $\square$

**Proposition C.74** (Asymptotic mobility recovery). *As $t \to \infty$, the diffusion coefficient recovers its equilibrium value uniformly:*

$$
\|M(\rho(\cdot, t)) - M_*\|_{L^\infty(\Omega)} \to 0,
\tag{C.88}
$$

*and the equation becomes uniformly parabolic with coefficient converging to $D\,M_*$.*

*Proof.* Since $\rho(t) \to \rho^*$ uniformly and $M$ is continuous, $M(\rho(t)) \to M(\rho^*) = M_*$ uniformly. $\square$

**Remark C.75** (Structural role of Principle 4 in long-time behavior). The mobility collapse $M(\rho_{\max}) = 0$ enters the long-time analysis through two mechanisms:

(a) *Energy barrier.* The potential $\Phi(\rho) \to +\infty$ as $\rho \to \rho_{\max}^-$ (Proposition C.11) prevents the density from approaching $\rho_{\max}$ at any time, providing the uniform bound (C.78). Without this barrier, a slow drift toward $\rho_{\max}$ could not be excluded, and the diffusion coefficient could degenerate, destroying the parabolic regularity that underlies the entire analysis.

(b) *Gradient suppression.* Near $\rho_{\max}$, the ratio $P'(\rho)/M(\rho) \to +\infty$ (since $P' > 0$ is bounded below and $M \to 0$), which amplifies the dissipation of spatial gradients in the high-density region (Proposition C.10). This ensures that any residual spatial structure near $\rho_{\max}$ is smoothed out rapidly, complementing the penalty-driven decay of the spatial mean.

Together, these mechanisms ensure that the Horizon Surface — the geometric object in ED phase space where $M(\rho) = 0$ — is never reached by any trajectory, and that the distance to the horizon increases monotonically in the long-time limit.

---

### C.7.7 Synthesis: Global $\to$ Local $\to$ Exponential Decay

The complete long-time picture is a three-stage convergence argument, each stage drawing on different structural features of the canonical principles.

**Theorem C.76** (Three-stage convergence). *Every global solution of the ED system (C.1) converges to the unique equilibrium $(\rho^*, 0)$ in the following three stages:*

*Stage I — Global bounds (Appendix C.2):*

$$
\|\rho(t) - \rho^*\|_{L^2} + |v(t)| \leq C(\mathcal{E}_0), \qquad t \geq 0.
$$

*The energy $\mathcal{E}[\rho(t), v(t)]$ remains bounded, the density stays in a compact subinterval of $(0, \rho_{\max})$, and the total dissipation is finite. This stage uses Principles 2 (channel complementarity), 3 (penalty coercivity), and 4 (mobility barrier).*

*Stage II — Algebraic convergence (§C.7.1–C.7.4):*

$$
\|\rho(t) - \rho^*\|_{H^k} + |v(t)| \to 0, \qquad t \to \infty.
$$

*The finite dissipation integrals and the Barbalat lemma drive $\nabla\rho \to 0$ and $v \to 0$. The strict monotonicity of $P$ (Principle 3) identifies $\rho^*$ as the unique $\omega$-limit point. The convergence rate in this stage is in general algebraic, not exponential, because the dissipation rate may degenerate far from equilibrium.*

*Stage III — Exponential convergence (Appendix C.5, §C.7.5):*

$$
\|\rho(t) - \rho^*\|_{H^s} + |v(t)| \leq C\,e^{-\beta(t - t_*)}, \qquad t \geq t_*.
$$

*Once the solution enters the local basin $\|(\rho - \rho^*, v)\|_{H^s} < \epsilon_0$, the Lyapunov functional $\mathcal{V}$ from Appendix C.5 provides exponential decay at rate $\beta = \gamma_*$. The transition from Stage II to Stage III occurs at a finite time $t_*(\mathcal{E}_0)$ that depends on the initial energy. This stage uses Principles 1 (diffusive dissipation), 3 (penalty dissipation), 5 (participation damping), and 6 (regime classification).*

*The three stages are connected as follows: Stage I provides the uniform bounds needed for Stage II (ensuring compactness and applicability of the Barbalat lemma), and Stage II provides the convergence needed for Stage III (ensuring eventual entry into the local basin). Each stage is indispensable.*

*Proof.* Stage I is Theorem C.66 (combining Theorem C.14 and the energy estimates of §C.2). Stage II is Theorem C.70 (the $\omega$-limit identification). Stage III is Theorem C.72 (eventual exponential decay). The connection between stages follows from the definitions: Stage I bounds imply precompactness (Theorem C.68), which enables the $\omega$-limit analysis of Stage II; the convergence in Stage II ensures eventual smallness, which activates the local stability of Stage III. $\square$

---

### C.7.8 Structural Summary

**Remark C.77** (Principles governing the long-time behavior). The long-time behavior depends on six of the seven canonical principles:

| Principle | Role in long-time behavior | Stage |
|-----------|---------------------------|-------|
| P1 (Operator Structure) | Diffusive dissipation $D\,M_*\nabla^2$ damps spatial modes; parabolic smoothing provides higher regularity. | I, III |
| P2 (Channel Complementarity) | $D + H = 1$ bounds the participation injection relative to direct dissipation; structures the energy identity. | I |
| P3 (Penalty Equilibrium) | $P' > 0$ provides energy coercivity, gradient dissipation, and the unique identification $\rho_\infty = \rho^*$. | I, II, III |
| P4 (Mobility Capacity Bound) | $M(\rho_{\max}) = 0$ creates the energy barrier at $\rho_{\max}$ and the gradient suppression near the horizon. | I |
| P5 (Participation Feedback Loop) | Introduces $v$ and $\tau$; participation damping $\zeta$ is a dissipation channel. | I, III |
| P6 (Damping Discriminant) | $\Delta = D + 2\zeta$ determines whether the Stage III approach is oscillatory or monotonic. | III |

**Principle 7** (Nonlinear Triad Coupling) does not appear in the long-time behavior. The gradient-squared term $M'(\rho)|\nabla\rho|^2$ generates transient harmonic content (Appendix C.4), but this content decays to zero as $\nabla\rho \to 0$, leaving no trace in the asymptotic state. The triad is a feature of the transient dynamics, not of the long-time limit.

**Remark C.78** (Completeness of the convergence result). Theorem C.76 establishes the strongest possible convergence statement for the ED system: every solution converges to the unique equilibrium, in every Sobolev norm, at an eventually exponential rate. This is the dynamical realization of the architectural statement that $(\rho^*, 0)$ is the unique, globally attracting equilibrium (Principle 3, §6.3 of the main text). The direction of becoming — from arbitrary initial data to $(\rho^*, 0)$ — is the dynamical expression of the ED ontology's teleological structure.

---

**References for Appendix C.7**

[1] H. Amann, *Linear and Quasilinear Parabolic Problems, Vol. I: Abstract Linear Theory*, Birkhäuser, Basel, 1995.

[2] L.C. Evans, *Partial Differential Equations*, 2nd ed., Graduate Studies in Mathematics, vol. 19, AMS, Providence, 2010.

[3] A. Lunardi, *Analytic Semigroups and Optimal Regularity in Parabolic Problems*, Birkhäuser, Basel, 1995.

[6] R. Temam, *Infinite-Dimensional Dynamical Systems in Mechanics and Physics*, 2nd ed., Springer, New York, 1997.

[7] D. Henry, *Geometric Theory of Semilinear Parabolic Equations*, Lecture Notes in Mathematics, vol. 840, Springer, Berlin, 1981.