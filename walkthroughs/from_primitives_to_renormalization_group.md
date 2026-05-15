# From Primitives to the Renormalization-Group Three-Regime Structure

## A Walkthrough of the Event Density Wilsonian RG Analysis

**Allen Proxmire** · May 2026

---

## 1. The Question

In 1971, Kenneth Wilson published the framework that solved one of statistical physics' deepest problems: how systems with structure at every length scale — magnets near their critical temperature, fluids near liquid-gas transitions, polymer chains at the entanglement length — could be analyzed despite the apparent breakdown of every standard approximation. The answer was the renormalization group: instead of trying to solve the system at one scale, follow how the equations themselves change as you average over progressively larger length scales. Couplings flow with scale; some grow, some shrink, some remain marginal. The fixed points of the flow — couplings that don't change under coarse-graining — characterize the universal physics of critical phenomena. Wilson received the Nobel Prize in 1982 for this work, and the renormalization-group framework is now standard machinery in condensed-matter physics, particle physics, fluid dynamics, and quantum field theory.

The question this document addresses is: what does the renormalization-group analysis of the canonical Event Density PDE actually show, and what does it tell us about whether ED is a sensible coarse-grained theory?

The answer is more interesting than it might appear. Three structural results emerge from the Wilsonian analysis. First, the ED operator basis is *form-closed* under coarse-graining — the canonical ED PDE generates no operators not already present in its own ansatz, at tree level and at one loop. The operator structure of ED is a theorem rather than a guess. Second, ED is *not* an RG fixed point at physical couplings — the beta functions are non-trivial, and the couplings flow non-trivially under coarse-graining. ED-specific phenomenology is regime-dependent rather than scale-invariant. Third, the flow structure has *three distinct regimes* — a UV regime of free two-channel diffusion, an intermediate regime where the ED operator structure is fully active, and an IR regime of linear gapped diffusion. ED-specific predictions live in the intermediate regime only; outside it, the framework's effective PDE collapses to either free wave-like dispersion or trivial massive decay.

The structural payoff: cross-scale invariance in ED is *operator-structure invariance within a bounded window*, not coupling-invariance across all scales. The framework's "one PDE, three domains" claim is a claim about the *operator structure* surviving across the intermediate regime, not a claim that the couplings $(M_0, P_0, \zeta, \tau, H, D)$ take the same values at all scales. The window where ED-specific phenomenology applies is bounded by two crossover scales whose values are determined by the system's specific couplings.

This is the framework's renormalization-group result, and it serves a different purpose than the other walkthroughs in the series. The Born, Schrödinger, Heisenberg, and entanglement walkthroughs derive specific structural results — particular equations or inequalities. The RG walkthrough establishes the *self-consistency* of the framework: the canonical ED PDE is a closed structural object under the standard coarse-graining procedure of statistical physics, with a well-defined window of applicability and well-understood limits.

The chain has six structural moves:

1. The canonical ED PDE has a two-channel structure: a density-perturbation field $\delta$ coupled to a participation mode $v$, with mobility, penalty, and inter-channel-coupling terms organized around a finite operator basis.

2. Wilsonian coarse-graining — block-averaging plus rescaling — produces a flow on the space of couplings. Applied to the canonical ED PDE, the flow generates no operators outside the canonical basis at tree level or at one loop. ED is form-closed.

3. The beta functions for the principal couplings, computed at dynamic exponent $z = 2$, give explicit RG flow trajectories: the linear mobility $M_0$ is marginal, the linear penalty $P_0$ and the participation friction $\zeta$ grow toward IR, the participation timescale $\tau$ shrinks toward IR.

4. The fixed-point catalog identifies a Gaussian fixed point (UV-stable only), two fixed lines (Wilson-Fisher at $\chi= 1$, nonlinear-mobility at $\chi= 0$), and a "fixed point at infinity" $(P_0 \to \infty, \zeta \to \infty, \tau \to 0)$ that is the universal IR sink.

5. Two crossover scales — $\ell_v$ where participation slaving onsets, $\ell_\xi$ where the gap dominates — bound the *ED window* in which ED-specific phenomenology applies.

6. The three regimes are explicit: UV free two-channel diffusion ($\ell \to -\infty$), intermediate Model A universality ($\ell_v < \ell < \ell_\xi$), IR linear gapped diffusion ($\ell \to \infty$). ED-specific predictions — quantum-classical transitions, nonlinear triad coupling, mobility-saturation phenomenology — live in the intermediate regime only.

The structural payoff: ED is form-closed but not scale-invariant. Cross-scale invariance is structural rather than parametric. The framework's "one PDE applied across many domains" claim is rigorous within a bounded window and outside it the effective PDE simplifies to forms that do not support ED-specific phenomenology.

---

## 2. The Primitives That Matter

The framework rests on substrate-level ontological commitments. The RG walkthrough operates on the *canonical ED PDE* — the continuum-level equation that DCGT produces from substrate primitives — rather than on the substrate itself. The primitives behind the canonical PDE are the same set used by Born, Schrödinger, and the gauge-fields walkthrough.

**Micro-events, chains, bandwidth, polarity, ED gradient, commitment irreversibility, locality, rule-type.** The standard substrate inventory.

**The Diffusion Coarse-Graining Theorem (DCGT).** The substrate-to-continuum bridge that produces the canonical ED PDE as the leading-order coarse-grained continuum content of substrate dynamics. The RG analysis takes the output of DCGT as its starting point.

The canonical ED PDE itself is the structural object the analysis runs on:

$$
\partial_t \delta= D F[\delta] + H v, \tau v̇ = F[\delta] − \zeta v, D + H = 1.
$$

where $\delta= \rho - \rho_*$ is the density perturbation around equilibrium, $v$ is the participation mode, and the spatial flux operator is

$$
F[\delta] = \nabla \cdot(M(\delta) \nabla \delta) − P(\delta) = M(\delta) \nabla^{2}\delta + M'(\delta) |\nabla \delta|^{2} − P(\delta).
$$

The mobility $M(\delta)$ and penalty $P(\delta)$ are smooth Taylor expansions:

$$
M(\delta) = M_0 + M_2 \delta^{2}/2 + ..., P(\delta) = P_0 \delta + P_3 \delta^{3}/6 + ...
$$

The penalty is odd in $\delta$ by the saturating-SY2 construction, so even coefficients vanish in $P$. Under the inherited $Z_2$ symmetry $(\delta, v) \to(-\delta, -v)$, mobility must be even, so odd coefficients vanish in $M$.

The system's principal couplings are six in number: $M_0, P_0, \zeta, \tau$ (linear), and $M_2, P_3$ (leading nonlinearities). The participation-mode coupling is parameterized by $H, D$ with $D + H = 1$ as a choice of normalization.

Symmetries inherited from the substrate: translations, spatial rotations, $Z_2$, and (in the absence of inter-channel coupling) gradient-flow structure with respect to a Lyapunov functional $L[\delta]$.

That's the structural setup. The RG analysis operates on this PDE.

---

## 3. The Canonical ED PDE and Its Operator Basis

Before the RG flow can be computed, the operator basis of the canonical PDE must be identified. The basis is the space of all operators consistent with the symmetries that *might* be generated under coarse-graining.

### 3.1 The reduced operator basis

Restricting to $Z_2$-symmetric operators of dimension up to four derivatives (the truncation consistent with the tree-level scaling of §4), the reduced basis has nine elements:

$$
O_0 = \delta from linear penalty P_0 \delta
O_2 = \nabla^{2}\delta from linear mobility M_0 \nabla^{2}\delta
O_{3,0} = \delta^{3} from cubic penalty P_3 \delta^{3}/6
O_{1,2} = \delta^{2}\nabla^{2}\delta from even mobility M_2 \delta^{2} \nabla^{2}\delta / 2
O_{2,2} = \delta|\nabla \delta|^{2} from even mobility M_2 \delta|\nabla \delta|^{2}
O_4 = \nabla^{4}\delta higher-derivative (not in bare ED; trial)
O_v = v participation mode
O_{v,t} = v̇ participation kinetic
O_{\delta v} = \delta v two-channel mixing (implicit via H v)
$$

Two of these are tied by the divergence-form identity:

$$
\nabla \cdot(M(\delta) \nabla \delta) = M(\delta) \nabla^{2}\delta + M'(\delta) |\nabla \delta|^{2}
$$

which constrains the coefficients of $O_{1,2}$ and $O_{2,2}$ as long as the divergence form is preserved. Whether the RG flow preserves this tying — whether the coarse-grained equation remains in divergence form — is part of what the analysis tests.

### 3.2 What "form-closure" means

The canonical PDE *generates* certain operators from this basis: $O_0, O_2, O_{3,0}, O_{1,2}, O_{2,2}, O_v, O_{v,t}, O_{\delta v}$ are all present in the bare equation. $O_4$ (the four-derivative term $\nabla^4 \delta$) is not present in the bare equation but is present in the basis as a trial operator — if the RG flow generates it, it must be added.

**Form-closure** means: the RG flow does not generate $O_4$ or any other operator outside the basis the bare equation already populates. The canonical ED PDE is closed under coarse-graining; its operator content does not expand under the flow.

If form-closure fails, the canonical PDE would be incomplete — coarse-graining at any scale would generate operators not present in the bare equation, requiring ad-hoc augmentation. Such a PDE would be a phenomenological starting point rather than a fundamental structural object.

If form-closure holds, the canonical PDE is a structural theorem of the substrate ontology: its operator content is what coarse-graining produces, with no additional operators forced by the flow.

### 3.3 Why form-closure is the right diagnostic

Wilsonian coarse-graining is a *projection* onto larger length scales. If the projection produces the same operator structure that was already present, the structure is *closed* under the projection. This is the strongest sense in which a PDE can be "fundamental at the continuum level": its operator content is preserved under the procedure that produces continuum content from microscopic content.

For the canonical ED PDE, form-closure is the test of whether the framework's operator ansatz is structural or phenomenological. The answer is structural.

---

## 4. Wilsonian Coarse-Graining and Form-Closure

The Wilsonian coarse-graining map applied to the canonical ED PDE proceeds in three steps: a momentum-shell split, a rescaling step, and a flow on the couplings.

### 4.1 The momentum-shell split

Fields are split into low- and high-momentum components:

$$
\delta(x, t) = \delta_<(x, t) + \delta_>(x, t), v(t) = v_<(t) + v_>(t)
$$

with $\delta_<$ supported on $|k| < \Lambda/b$ and $\delta_>$ on $\Lambda/b \leq|k| < \Lambda$ for some rescaling factor $b > 1$. The high-momentum modes are integrated out, producing an effective theory for the low-momentum modes alone.

### 4.2 The rescaling step

After integrating out high-momentum modes, the coordinates and fields are rescaled to restore the original momentum cutoff:

$$
x' = x/b, t' = t/b^z, \delta'(x', t') = b^\chi \delta_<(bx', b^z t'), v'(t') = b^{\chi_v} v_<(b^z t')
$$

Here $z$ is the *dynamic exponent* (the scaling of time relative to space) and $(\chi, \chi_v)$ are the field scaling dimensions. The dimensionless choice $z = 2$ corresponds to diffusive dynamics, which is appropriate for the canonical ED PDE.

### 4.3 The form-closure result

Carrying out the coarse-graining at tree level (tracking dimensional scaling without loop integrals) and at one loop (including the leading-order quantum corrections from integrating out the high-momentum modes) produces an effective theory whose operator content is:

**Tree level:** the bare operators $O_0, O_2, O_{3,0}, O_{1,2}, O_{2,2}, O_v, O_{v,t}, O_{\delta v}$, with coefficients rescaled by appropriate powers of $b$. No $O_4$ generated.

**One loop:** the bare operators with corrections proportional to coupling products. The corrections renormalize existing coefficients but do not generate new operators outside the basis.

The bare operator structure is preserved under the coarse-graining map. **The canonical ED PDE is form-closed.**

This is a non-trivial result. Many continuum field theories are *not* form-closed at one loop — they require the addition of operators absent from the bare equation. The Klein-Gordon equation requires the addition of $\phi^4$ at one loop in $d = 4$. The Navier-Stokes equation requires the addition of multiple operators when treated as a stochastic field theory. For ED, the operators present in the canonical PDE are sufficient to absorb the one-loop corrections; the structural ansatz is closed.

### 4.4 The participation-channel structure survives

The two-channel structure ($\delta$ coupled to $v$) is not destroyed by coarse-graining. The participation mode $v$ remains as a separate dynamical variable; its coupling to $\delta$ via $H$ is renormalized but not eliminated. The participation channel is *intrinsic* to the structural form of the canonical PDE; it is not an artifact of the bare equation that washes out under coarse-graining.

This survival is what allows the three-regime structure to exist. If participation washed out under coarse-graining, the equation would reduce to a single-channel diffusion-reaction equation (a Cahn-Hilliard or Allen-Cahn class equation) at all scales, and there would be no two-channel structure to produce different regimes at different scales.

---

## 5. The Beta Functions and the Fixed-Point Catalog

The flow on the couplings is computed by tracking how each coupling rescales at each step of the RG procedure. The result, expressed as beta functions $\beta_g = dg/d\ell$ where $\ell= \ln b$ is the logarithmic scale, gives explicit equations for the flow trajectories.

### 5.1 The beta functions at $z = 2$

At dynamic exponent $z = 2$, with field-scaling dimension $\chi$ chosen to make the linear mobility marginal:

$$
\beta_{M_0} = 0 (marginal)
\beta_{P_0} = 2 P_0 (relevant; P_0 grows toward IR)
\beta_\zeta= 2 \zeta(relevant; \zeta grows toward IR)
\beta_\tau= −2 \tau(irrelevant; \tau shrinks toward IR)
\beta_{P_3} = (2 − 2\chi) P_3
\beta_{M_2} = −2\chi M_2
$$

The linear mobility $M_0$ is marginal — its scaling dimension is zero, so it does not flow under the leading-order RG. The penalty $P_0$ and participation friction $\zeta$ are *relevant* — both grow exponentially toward the IR limit. The participation timescale $\tau$ is *irrelevant* — it shrinks exponentially toward the IR limit.

The cubic penalty $P_3$ and quadratic mobility $M_2$ have field-dependent scaling: their behavior depends on the choice of $\chi$, and there are two natural values ($\chi= 0$ and $\chi= 1$) that make different operators marginal.

### 5.2 Flow invariants

Three combinations of couplings are exactly RG-invariant on any trajectory:

$$
P_0/\zeta invariant (both scale as e^{2\ell})
P_0 \cdot \tau invariant (one scales as e^{2\ell}, other as e^{−2\ell})
\zeta \cdot \tau invariant (same combination)
$$

These invariants are the RG-conserved structural ratios. They label distinct trajectories: two systems with the same $P_0/\zeta$ ratio belong to the same RG orbit, even if their absolute couplings differ.

### 5.3 Fixed-point catalog

A *fixed point* of the RG flow is a coupling configuration $(M_0^*, P_0^*, \zeta^*, \tau^*, P_3^*, M_2^*)$ satisfying $\beta_g = 0$ for all $g$. The canonical ED PDE has the following fixed-point structure:

**Gaussian fixed point $G$:** $(M_0^*, 0, 0, \infty)$ with all interactions absent. Free two-channel diffusion at infinite participation timescale. UV-stable only — it is the limit reached by running the RG flow backward to short distances.

**Wilson-Fisher fixed line at $\chi= 1$:** $\beta_{P_3} = 0$ at $\chi= 1$ makes the cubic penalty marginal. A line of fixed points parameterized by the value of $P_3$, structurally analogous to the Wilson-Fisher fixed point of $\phi^4$ theory in $d = 3$ near the upper critical dimension.

**Nonlinear-mobility fixed line at $\chi= 0$:** $\beta_{M_2} = 0$ at $\chi= 0$ makes the quadratic mobility marginal. A different line of fixed points, structurally analogous to fixed points of nonlinear-diffusion equations.

**"Fixed point at infinity":** $(P_0 \to \infty, \zeta \to \infty, \tau \to 0)$ with the relevant couplings running to infinity and the irrelevant coupling running to zero. This is the universal IR sink — every trajectory in the principal flow basin approaches this limit at sufficiently large $\ell$.

The stability matrix $J_{ij} = \partial \beta_i / \partial g_j$ is diagonal at all fixed points, which makes the local flow analysis particularly clean.

### 5.4 ED is not a fixed point

ED at physical couplings is not a fixed point. The canonical PDE has $P_0 \neq 0$, $\zeta \neq 0$, $\tau$ finite, and the beta functions are non-zero in this regime. The system flows non-trivially under coarse-graining: $P_0$ and $\zeta$ grow toward IR, $\tau$ shrinks toward IR, and the system progresses from its starting point at intermediate couplings toward the fixed point at infinity.

This is structurally important. ED is not a scale-invariant theory in the strict RG sense. Its couplings flow, its operator coefficients change with scale, and its phenomenology depends on what scale you analyze it at. What is preserved under the flow is the *operator structure* — the set of operators present in the equation — not the *coupling values*.

---

## 6. The Two Crossover Scales and the ED Window

The flow from initial physical couplings toward the fixed point at infinity passes through structurally distinct regimes separated by two crossover scales. These scales bound the *ED window* — the regime in which ED-specific phenomenology applies.

### 6.1 The participation-slaving onset $\ell_v$

The participation mode $v$ has a relaxation timescale governed by $\tau$. As $\tau$ shrinks toward IR (per $\beta_\tau= -2\tau$), the relaxation becomes faster and at some scale becomes faster than the dynamics of $\delta$. At that scale, $v$ ceases to be an independent dynamical degree of freedom — its dynamics are *slaved* to $\delta$ via the algebraic relation $v = F[\delta]/\zeta$ obtained by setting $\dot{v} = 0$ in the original two-channel equations.

The crossover scale is

$$
\ell_v = ½ \ln(\xi_v \Lambda)
$$

where $\xi_v$ is a characteristic length set by the participation parameters. For $\ell < \ell_v$ (i.e., shorter length scales), $v$ is unfrozen and the two-channel dynamics are active. For $\ell > \ell_v$, $v$ is slaved to $\delta$ and the system collapses to an effective single-channel dynamics for $\delta$.

### 6.2 The gap-dominated scale $\ell_\xi$

The penalty $P_0$ grows toward IR (per $\beta_{P_0} = 2P_0$). At some scale, the gap energy $P_0$ dominates the dynamics: the linear gapped term in the equation for $\delta$ overwhelms the spatial gradient terms, and the system settles into an exponentially-decaying trivial-massive phase.

The crossover scale is

$$
\ell_\xi= \ln(\xi \Lambda)
$$

where $\xi$ is the correlation length of the gapped phase, related to $\sqrt{D M_0/P_0}$ at the relevant scale. For $\ell < \ell_\xi$, the system has interesting spatial structure. For $\ell > \ell_\xi$, the system is gap-dominated and decays exponentially to $\delta= 0$.

### 6.3 The ED window

The ED window is the intermediate range $\ell_v < \ell < \ell_\xi$. Within this window:

- Participation slaving has occurred: $v$ is no longer an independent dynamical variable, and the equation reduces to an effective single-channel form for $\delta$.
- The gap has not yet dominated: the spatial gradient and nonlinear mobility terms are still active, and the system supports non-trivial spatial structure.
- The full nonlinear ED structure — quadratic mobility $M_2$, cubic penalty $P_3$, the divergence-form mobility flux — is present and active.

Outside the window — at scales smaller than $\ell_v$ or larger than $\ell_\xi$ — the effective PDE simplifies to one of two forms: free two-channel diffusion in the UV or linear gapped diffusion in the IR. Neither supports ED-specific phenomenology.

The ED window is the regime in which the framework's predictive content lives. Quantum-classical transitions, nonlinear triad coupling, mobility-saturation phenomenology, the Universal Mobility Law, the saturating-penalty soft-matter content — all of these are intermediate-regime effects. None of them survives the collapse to UV or IR.

---

## 7. The Three Regimes

The three regimes — UV, intermediate, and IR — have explicit effective PDEs that the canonical ED PDE reduces to in each limit.

### 7.1 UV ($\ell \to -\infty$): free two-channel diffusion

In the UV limit, $\tau \to \infty$ freezes the participation mode: $\dot{v} \approx 0$ to leading order, so $v(t) = v_0 + O(1/\tau)$ remains constant. The penalty $P_0 \to 0$ in this limit, and the nonlinear couplings $P_3, M_2$ also vanish (they are subleading at small scales).

The effective PDE in the UV is:

$$
\partial_t \delta= D M_0 \nabla^{2}\delta + H v
\tau v̇ = M_0 \nabla^{2}\delta
$$

This is *free two-channel diffusion*. The participation mode has frozen out; $\delta$ obeys a linear diffusion equation with a constant forcing $Hv$. At long wavelengths, the dispersion is wave-like — the participation mode supplies a frozen-in restoring force that produces second-order time dynamics in the coupled system.

This is the kinematic-acoustic-metric regime of the framework: the regime where free-scalar-QFT-like dynamics emerge from the canonical ED PDE. At UV scales, the canonical PDE is structurally the same as a free relativistic scalar field theory, with the participation mode supplying the "speed of sound" through the $H/\tau$ coupling.

### 7.2 Intermediate ($\ell_v < \ell < \ell_\xi$): Model A universality

In the intermediate regime, $\tau \to 0$ slaves the participation mode: $v = F[\delta]/\zeta$. The coupling between $\delta$ and $v$ becomes an effective single-channel coupling, with effective relaxation rate $\Gamma_\mathrm{eff} = D + H/\zeta$.

The effective PDE in the intermediate regime is:

$$
\partial_t \delta= \Gamma_{\mathrm{eff}} [M_0 \nabla^{2}\delta + (M_2/2) \delta^{2} \nabla^{2}\delta + M_2 \delta|\nabla \delta|^{2} − P_0 \delta − (P_3/6) \delta^{3}]
$$

This is *Model A universality* — the standard relaxational dynamics for a non-conserved scalar order parameter, with quadratic-mobility nonlinearities and cubic penalty. The full ED operator structure is present and active. The RG flow within this regime drives the system toward the fixed point at infinity but the trajectory passes through a regime where ED-specific phenomenology is rich and predictive.

This is the regime in which the framework's predictions live. Soft-matter mobility saturation (the Universal Mobility Law). The matter-wave quantum-classical boundary. Nonlinear triad coupling. Saturating-penalty dynamics in concentrated solutions. Each of these is intermediate-regime content.

### 7.3 IR ($\ell \to \infty$): linear gapped diffusion

In the IR limit, the gap $P_0 \to \infty$ dominates the dynamics. The nonlinear couplings $P_3, M_2$ are still present but their contributions become field-amplitude-suppressed: as $\delta \to 0$ under the gap-dominated decay, $\delta^3 \to 0$ even faster, so the cubic terms become negligible. The same field-amplitude suppression applies to the quadratic mobility.

The effective PDE in the IR is:

$$
\partial_t \delta= D M_0 \nabla^{2}\delta − D P_0(\ell) \delta, P_0(\ell) \to \infty, \delta \to 0
$$

This is *linear gapped diffusion*. The system decays exponentially to the trivial state $\delta= 0$ at a rate set by $D P_0$. The nonlinear mobility and cubic penalty are eliminated through two stages: RG irrelevance (the couplings shrink under the flow) and field-amplitude suppression (the operators are evaluated at $\delta \to 0$). The universal endpoint is the trivial massive phase $\delta \equiv 0$.

This is what happens to ED at very long length scales: the system has decayed to the equilibrium density $\rho_*$, with no spatial structure left to support any phenomenology.

### 7.4 The full three-regime flow diagram

$$
UV: \ell \to −\infty Intermediate: \ell_v < \ell < \ell_\xi IR: \ell \to \infty
───────────────────── ────────────────────────── ─────────────
Free two-channel Model A universality Linear gapped
diffusion Full ED operator structure diffusion
v unfrozen Participation slaved (v = F[\delta]/\zeta) Trivial massive
P_0 \approx 0 Quadratic-mobility nonlinearities endpoint \delta \to 0
M_2, P_3 \approx 0 Cubic-penalty nonlinearities Nonlinearities
Wave-like dispersion Saturating-penalty phenomenology eliminated
ED-specific predictive content
The "ED window"
$$

The flow through the three regimes is monotone: the system starts at small $\ell$ in the UV regime, passes through the intermediate ED window as $\ell$ grows past $\ell_v$, and exits the window into the IR regime as $\ell$ exceeds $\ell_\xi$. Each regime has its own structural form, and the transitions are sharp at the crossover scales.

---

## 8. Cross-Scale Invariance: What It Is and Isn't

The framework's "one PDE applied across many domains" claim is sometimes summarized as cross-scale invariance. The RG analysis sharpens what this claim does and does not assert.

### 8.1 What cross-scale invariance is in ED

Cross-scale invariance, in ED, is the structural fact that the *operator structure* of the canonical PDE is preserved across the intermediate window. The same operators — linear mobility, linear penalty, quadratic mobility, cubic penalty, two-channel coupling — are active throughout the window. The same nonlinear features — saturation behavior, triad coupling, Q-C boundary phenomenology — are produced by the same operator structure at every scale in the window.

This is a non-trivial structural statement. In standard physics, different domains (soft matter, quantum mechanics, fluid dynamics, gravity) are described by different equations with different operator content. ED's claim is that one operator structure suffices, applied at scales determined by the domain-specific values of the couplings. The Universal Mobility Law in soft matter, the matter-wave Q-C boundary in matter-wave physics, the triad-coupling structure in molecular dynamics — all are projections of the same canonical PDE structure at different domain-specific intermediate-window locations.

### 8.2 What cross-scale invariance is NOT in ED

Cross-scale invariance is *not* the claim that the couplings $(M_0, P_0, \zeta, \tau, H, D)$ take the same numerical values at all scales. They flow per the beta functions; they take domain-specific values at each scale. A laboratory soft-matter experiment and a matter-wave interferometry experiment do not have the same couplings; they have the same operator structure with different couplings appropriate to each system.

Cross-scale invariance is *not* the claim that ED is an RG fixed point. It is not. The flow is non-trivial, and ED at any specific scale is not invariant under coarse-graining as a coupling configuration. The window of scales over which the operator structure is active is also not invariant — it shifts with the system being analyzed.

Cross-scale invariance is *not* a claim about scales outside the ED window. At UV scales smaller than $\ell_v$, the equation is free two-channel diffusion and supports no ED-specific phenomenology. At IR scales larger than $\ell_\xi$, the equation is linear gapped diffusion and again supports no ED-specific phenomenology. Outside the window, the canonical PDE simplifies to forms that are structurally distinct from what ED predicts.

### 8.3 The structural meaning

The structural meaning of cross-scale invariance in ED: a finite set of operators, preserved under coarse-graining, suffices to describe phenomenology across a wide range of physical domains, *within each domain's intermediate window*. The framework's predictive power lies in the domain-specific position of the window (where $\ell_v$ and $\ell_\xi$ lie for each system) and in the operator structure that is active throughout it.

This is what "one PDE, three domains" actually means at the level of the RG analysis. Not coupling-invariance. Not fixed-point status. Operator-structure invariance within bounded windows whose locations are domain-specific. The framework's empirical predictions follow from this structural fact.

---

## 9. What's Forced, What's Inherited, What's Open

It is worth being precise about what the RG analysis establishes and what it does not.

### 9.1 What's forced

The form-closure of the canonical ED PDE under Wilsonian coarse-graining is forced. At tree level and at one loop, the operator basis is preserved; no new operators are generated. The canonical PDE is structurally closed.

The beta functions for the principal couplings at $z = 2$ are forced by the dimensional structure of the operators and the standard Wilsonian scaling rules. $M_0$ marginal, $P_0$ and $\zeta$ relevant, $\tau$ irrelevant, $P_3$ and $M_2$ field-dimension-dependent.

The flow invariants $P_0/\zeta$, $P_0 \cdot \tau$, $\zeta \cdot \tau$ are exactly RG-invariant on any trajectory. This is forced by the structure of the beta functions (cancellation of scaling dimensions in the ratio).

The fixed-point catalog is forced: Gaussian fixed point, two fixed lines, fixed point at infinity. The stability matrix is diagonal at all fixed points. ED at physical couplings is not at any fixed point.

The two crossover scales $\ell_v$ and $\ell_\xi$ are forced by the relative magnitudes of the participation-mode-relaxation and gap-dominance phenomena. The ED window between them is forced as the regime where neither limit applies.

The three-regime structure is forced: UV free two-channel, intermediate Model A, IR linear gapped. The effective PDEs in each regime are explicit.

The participation slaving / freezing dichotomy ($v$ algebraically slaved in IR, $v$ frozen in UV) is forced by the limits of the participation mode's $\tau$-controlled dynamics.

### 9.2 What's inherited

The *values* of the couplings $(M_0, P_0, \zeta, \tau, M_2, P_3, H, D)$ at any specific scale are INHERITED. The framework establishes the flow equations; the numerical values of the couplings at any starting scale come from the substrate microscopic details + the system being analyzed.

The *positions* of the crossover scales $\ell_v$ and $\ell_\xi$ in any specific system are INHERITED from the system's couplings. The framework establishes that the crossover scales exist; their locations depend on the system.

The *width* of the ED window is INHERITED from the ratio $\ell_\xi - \ell_v$, which depends on the couplings.

The *specific predictions* in the intermediate window — the Universal Mobility Law's saturating exponent, the matter-wave Q-C boundary's molecular-mass range, the triad-coupling phenomenology — are INHERITED from the values of the couplings within the window. The framework establishes the structural form of these predictions; the numerical values come from the inherited couplings.

The dynamic exponent $z = 2$ is inherited from the diffusive nature of the canonical ED PDE; if the substrate dynamics were different (relativistic, non-diffusive), $z$ would take a different value.

### 9.3 What's open

The two-loop corrections to the beta functions are open. The analysis closed at one loop with form-closure preserved; whether form-closure also holds at two loops is not yet established. If form-closure were to break at two loops, the canonical PDE would need to be supplemented with additional operators at sufficient precision.

The closed-form derivation of the crossover scales $\ell_v$ and $\ell_\xi$ from substrate primitives is open. The framework establishes the scales exist; pinning them to substrate constants would require closed-form expressions for the participation parameters in terms of $\ell_P$, $\hbar$, $c$.

The relationship between the ED window and the hydrodynamic window of DCGT is structurally clear (both bound the regime where ED-specific phenomenology applies) but not formally derived. A unified treatment of the two windows would be a useful extension.

The behavior of the canonical PDE at the boundaries of the ED window — exactly at $\ell= \ell_v$ and $\ell= \ell_\xi$ — is not fully analyzed. The transitions are described as "crossovers" rather than sharp boundaries; the precise functional shape of the crossover is open.

The non-Abelian generalization of the RG analysis (for the Yang-Mills sector and the substrate-gravity sector) is open. The Abelian RG analysis closes here; the extension to non-Abelian content would parallel the DCGT non-Abelian generalization.

---

## 10. What This Argument Establishes

The chain runs:

Substrate primitives (micro-events, chains, bandwidth, polarity, ED gradient, locality, rule-type, finite-width kernels) → DCGT (substrate-to-continuum bridge producing the canonical ED PDE) → canonical ED PDE with two-channel structure ($\delta$ coupled to $v$) and finite operator basis ($O_0, O_2, O_{3,0}, O_{1,2}, O_{2,2}, O_v, O_{v,t}, O_{\delta v}$) → Wilsonian coarse-graining (momentum-shell split + rescaling) → form-closure at tree level and one loop (no new operators generated) → beta functions at $z = 2$ ($M_0$ marginal, $P_0$ and $\zeta$ relevant, $\tau$ irrelevant) → fixed-point catalog (Gaussian, Wilson-Fisher fixed line, nonlinear-mobility fixed line, fixed point at infinity) → flow invariants ($P_0/\zeta$, $P_0\tau$, $\zeta\tau$) → two crossover scales ($\ell_v$ participation-slaving onset, $\ell_\xi$ gap-dominated) → ED window $\ell_v < \ell < \ell_\xi$ → three regimes (UV free two-channel, intermediate Model A, IR linear gapped) → cross-scale invariance as operator-structure invariance within the window.

The renormalization-group analysis of the canonical ED PDE is now complete. The framework's predictive content is structurally bounded: ED-specific phenomenology applies within a finite window of length scales determined by the system's couplings, and outside that window the effective PDE collapses to forms that are either free wave-like dispersion (UV) or trivial massive decay (IR). The framework reproduces standard relaxational dynamics in the intermediate regime (Model A universality) and standard linear diffusion in the limits.

What's new is the structural account of why ED has the operator content it does. Standard continuum field theories are written down as ansätze and the operator content is justified empirically. ED's operator content is closed under the Wilsonian RG procedure — the canonical PDE generates no operators outside its own basis under coarse-graining at tree level or one loop. This is a stronger structural result than empirical justification: the operator content of the equation is preserved under the procedure that produces continuum content from microscopic content.

The cross-scale invariance the framework claims is sharpened by the analysis. It is not coupling-invariance across all scales — the couplings flow non-trivially per the beta functions, and ED at any specific scale is not at an RG fixed point. It is operator-structure invariance within a bounded window — the same operators are active throughout the intermediate regime, with their values determined by the system's specific couplings. Cross-scale invariance, properly understood, is structural rather than parametric.

The three-regime structure is the framework's account of how ED's phenomenology depends on scale. At short scales, the equation simplifies to free two-channel diffusion with frozen participation; this is the regime where the kinematic-acoustic-metric and free-scalar-QFT-like content emerges. At intermediate scales — the ED window — the full nonlinear operator structure is active, and the framework's domain-specific predictions (soft-matter mobility, matter-wave Q-C boundary, triad coupling) live here. At long scales, the equation simplifies to linear gapped diffusion that decays to the trivial state; this is the universal IR endpoint where any specific structure has been smoothed away.

The factor that's worth emphasizing: form-closure is non-trivial. Many continuum field theories require operator augmentation under one-loop corrections — $\phi^4$ in QFT, multiple operators in stochastic Navier-Stokes, similar augmentations in quantum chromodynamics. The canonical ED PDE does not require augmentation. The operator basis the framework writes down is what the substrate-to-continuum bridge produces, and what the coarse-graining procedure preserves. This is a structural property of the canonical PDE, not an aesthetic choice.

Whether the substrate primitives themselves are right is the load-bearing empirical question, as in every walkthrough. The framework's empirical exposure lives across closed sectors — soft-matter mobility, substrate-gravity transitions, quantum-computational ceilings, Clay-relevance results. The RG analysis does not change the empirical content; it shows that the canonical PDE that produces the empirical content is structurally well-defined under the standard coarse-graining procedure of statistical physics.

For the renormalization-group analysis specifically, the structural case is closed at one loop. Form-closure holds. The beta functions are explicit. The fixed-point catalog is complete. The three regimes are identified with their effective PDEs explicit. The ED window is bounded by two crossover scales, with the operator structure invariant within the window and simplifying outside it. Cross-scale invariance is established as operator-structure invariance, not coupling-invariance, with the appropriate honest framing throughout.

---

## 11. References

- Wilson, K. G. "The Renormalization Group: Critical Phenomena and the Kondo Problem." *Reviews of Modern Physics* 47, 773–840 (1975).
- Wilson, K. G., Kogut, J. "The Renormalization Group and the $\epsilon$ Expansion." *Physics Reports* 12, 75–199 (1974).
- Hohenberg, P. C., Halperin, B. I. "Theory of Dynamic Critical Phenomena." *Reviews of Modern Physics* 49, 435–479 (1977).
- Forster, D., Nelson, D. R., Stephen, M. J. "Large-Distance and Long-Time Properties of a Randomly Stirred Fluid." *Physical Review A* 16, 732–749 (1977).
- Goldenfeld, N. *Lectures on Phase Transitions and the Renormalization Group.* Westview Press, 1992.
- Cardy, J. *Scaling and Renormalization in Statistical Physics.* Cambridge University Press, 1996.
- Zinn-Justin, J. *Quantum Field Theory and Critical Phenomena.* Oxford University Press, 4th edition, 2002.
- Polchinski, J. "Renormalization and Effective Lagrangians." *Nuclear Physics B* 231, 269–295 (1984).
- Proxmire, A. *Wilsonian RG-Flow Analysis of the Canonical ED PDE: Operator-Basis Form-Closure and One-Loop Check.* April 2026.
- Proxmire, A. *ED RG Flow Geometry: Fixed-Point Catalog, Diagonal Stability, and the ED Window.* April 2026.
- Proxmire, A. *ED IR Effective PDE: Slaving Derivation and Two-Stage Nonlinearity Elimination.* April 2026.
- Proxmire, A. *ED UV PDE and the Three-Regime Flow.* April 2026.
- Proxmire, A. *The 0.6 Problem Resolution: Structural Identity from the Cross-Regime Nondimensional Invariant.* April 2026.
- Proxmire, A. *The Diffusion Coarse-Graining Theorem: Substrate-to-Continuum Bridge for Canonical-ED Dynamical Content.* April 2026.
- Proxmire, A. *Event Density: One Substrate, Three Domains.* April 2026.
- The full Event Density corpus, including all forced theorems and supporting memos, is available at https://github.com/allen-proxmire/event-density.
