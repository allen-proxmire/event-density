# From Primitives to the 0.6 Problem

## A Walkthrough of the Event Density Dimensional-Dictionary Resolution

**Allen Proxmire** · May 2026

---

## 1. The Question

In the framework's dimensional dictionary — the structural construction that maps substrate-level quantities to physical units — there appears a single conspicuous number:

$$
T_0 = 0.6 \cdot \hbar /(mc^{2})
$$

This is the canonical quantum-regime time scale, used to nondimensionalise simulation equations and to translate between substrate-level and physical-unit quantities. Combined with the canonical length scale $L_0 = \hbar/(mc)$ (the reduced Compton wavelength), it produces a canonical signal speed:

$$
c_0 = L_0 / T_0 = c / 0.6 \approx 1.667 c
$$

Faster than light. The framework's acoustic-metric derivation identifies the reversible-slice sound speed with this $c_0$, producing a 60% mismatch between the dictionary's "signal speed" and the physical speed of light.

The 0.6 is the framework's most conspicuous unexplained number. It looks like an empirical fit-parameter inserted into the dimensional construction. It looks like it might be wrong. And it produces a superluminal $c_0$ that has been flagged across multiple framework memos as a structural concern requiring resolution.

The question this document addresses is: where does the 0.6 come from, and what does it mean?

The answer is structurally clean and partially satisfying. The 0.6 is *not* a free constant. It is algebraically forced by the dictionary's nondimensionalisation construction to equal exactly $2 \cdot D_\mathrm{nd}(\mathrm{quantum})$ where $D_\mathrm{nd}$ is the canonical *dimensionless channel weight* in the quantum regime. The 0.6 problem reduces structurally to the question of what fixes $D_\mathrm{nd}(\mathrm{quantum})$. Five alternative derivation routes are audited and refuted; only the dictionary-construction route succeeds.

The reduction is partial because $D_\mathrm{nd}(\mathrm{quantum}) = 0.3$ is itself a convention inherited from the framework's initial nondimensionalisation, not a first-principles derivation. The "0.6 problem" reduces to the "$D_\mathrm{nd}$ anchoring problem" — these are the same question, and the framework's rate-balance-template program is the open work attempting to derive $D_\mathrm{nd}$ from primitives.

The reduction is satisfying because it produces three structural statements not previously in the corpus:

1. The "60% speed mismatch" is not a physical anomaly. It is a mismatch between an atlas-nondimensionalisation artifact and a physical invariant. The framework's parabolic substrate PDE has formally infinite signal speed anyway; $c_0 > c$ is a regime-boundary marker, not a physical prediction.

2. The structural identity $c_0/c = 1/(2 D_\mathrm{nd})$ is *universal* across the framework's regimes (quantum, optomechanical, condensed-matter, galactic, cosmological). It is purely a channel-weight relationship.

3. At the equal-rates point $D_\mathrm{nd} = 1/2$ (where decoherence rate equals coherent-system rate), $c_0 = c$ *exactly*. No free parameter, no fit. This is a clean structural selection rule: the regime where $D_\mathrm{nd} = 1/2$ is the regime where the dictionary's signal speed coincides with the physical speed of light.

The chain has three structural moves:

1. The dimensional dictionary construction $T_0 = L_0^2 \cdot D_\mathrm{nd}/D_\mathrm{phys}$ is required for the nondimensionalisation to work — rescaling $t \to t/T_0$, $x \to x/L_0$ must send the simulation's mobility coefficient to $D_\mathrm{nd}$ by construction.

2. Plugging in $L_0 = \hbar/(mc)$ (Compton length, Madelung-anchored), $D_\mathrm{phys} = \hbar/(2m)$ (Madelung diffusion coefficient), and the canonical quantum-regime convention $D_\mathrm{nd} = 0.3$ produces $T_0 = 0.6\,\hbar/(mc^2)$ algebraically.

3. The five alternative derivation routes (damping discriminant, reversible-slice QFT, acoustic-metric curvature, PME similarity, $\zeta$-interpolation) all fail to reproduce the 0.6 from independent dynamics. The dictionary-construction route is the unique successful route.

The structural payoff: the framework's most conspicuous unexplained number is reduced to a one-line algebraic identity that traces back to a single underlying convention — the value of the quantum-regime channel weight $D_\mathrm{nd}$. The 0.6 is no longer a structural mystery; it is a structural *bookmark* pointing to the genuinely open question of what fixes $D_\mathrm{nd}$ from first principles.

This walkthrough is shorter than Born or Schrödinger, because the math content is essentially one algebraic identity plus a five-route audit. But it serves a useful purpose: it documents how a conspicuous-looking constant in a substrate-level framework can be structurally clean once the construction is made explicit.

---

## 2. The Primitives That Matter

The 0.6 problem operates downstream of the framework's QM-emergence sector. The walkthrough uses the same substrate primitives that Born and Schrödinger used, plus three forced theorems and the framework's *dimensional atlas* — the catalog of regime-specific dimensional dictionaries.

**Micro-events (P01).** Discrete acts of becoming.

**Chains, bandwidth, polarity.** Standard substrate inventory.

**Substrate length scale $\ell_P$ (T19).** Newton-recovery identifies the substrate length scale as the Planck length.

**Madelung anchor.** The framework's QM emergence (U2 + U3) identifies the substrate's diffusion coefficient at the quantum regime as $D_\mathrm{phys} = \hbar/(2m)$ — the Madelung diffusion coefficient that makes the substrate evolution equation the Schrödinger equation in disguise. This identification is FORCED by the U3 closure (Schrödinger walkthrough §5).

**Compton length $L_0 = \hbar/(mc)$.** The reduced Compton wavelength of the chain, identified as the canonical quantum-regime length scale by inheriting from the substrate's relativistic structure (Klein-Gordon walkthrough plus Madelung).

**Dimensional atlas convention.** The framework's regime-specific dimensional dictionaries are catalogued in `papers/Dimensional_Atlas/regimes/`. Each regime specifies $L_0$, $T_0$, $D_\mathrm{phys}$, and $D_\mathrm{nd}$. The quantum-regime dictionary fixes $D_\mathrm{nd} = 0.3$ as the canonical channel-weight value.

**The simulation requirement.** Substrate-level simulation requires nondimensionalisation: the substrate PDE must be written in dimensionless form for numerical integration. The dictionary's job is to specify the rescaling $t \to t/T_0$, $x \to x/L_0$ such that the resulting dimensionless PDE has clean coefficient structure.

That's the structural setup. The 0.6 emerges from the algebra of this setup.

---

## 3. The Dimensional Dictionary Construction

The canonical quantum-regime dimensional dictionary specifies four quantities:

$$
L_0 = \hbar /(mc) (canonical length, reduced Compton wavelength)
D_{\mathrm{phys}} = \hbar /(2m) (canonical diffusion coefficient, Madelung)
D_{\mathrm{nd}} = 0.3 (canonical dimensionless channel weight)
T_0 = ? (canonical time, to be determined)
$$

The first three are inputs. The fourth is *derived* from a structural construction.

### 3.1 The construction

The dictionary's job: define $T_0$ such that the substrate PDE, after rescaling $t \to t/T_0$, $x \to x/L_0$, has its mobility-term coefficient equal to $D_\mathrm{nd}$.

The substrate's mobility coefficient in the rescaled equation is:

$$
D_{\mathrm{phys}} \cdot T_0 / L_0^{2}
$$

For this to equal $D_\mathrm{nd}$:

$$
D_{\mathrm{phys}} \cdot T_0 / L_0^{2} = D_{\mathrm{nd}}
$$

Solving for $T_0$:

$$
T_0 = L_0^{2} \cdot D_{\mathrm{nd}} / D_{\mathrm{phys}}
$$

This is the **dictionary construction**. It is not stipulative; it is required for the nondimensionalisation to produce the standard dimensionless simulation equation. If $T_0$ is chosen any other way, the rescaled equation has the wrong coefficient structure.

### 3.2 Plugging in the canonical values

Substituting $L_0 = \hbar/(mc)$ and $D_\mathrm{phys} = \hbar/(2m)$:

$$
T_0 = [\hbar /(mc)]^{2} \cdot D_{\mathrm{nd}} / [\hbar /(2m)]
= [\hbar^{2}/(m^{2}c^{2})] \cdot D_{\mathrm{nd}} \cdot[2m/\hbar]
= 2 D_{\mathrm{nd}} \cdot \hbar / (mc^{2})
$$

This is the algebraic relationship:

$$
T_0 = 2 D_{\mathrm{nd}} \cdot \hbar /(mc^{2})
$$

Substituting the canonical quantum-regime convention $D_\mathrm{nd} = 0.3$:

$$
T_0 = 2 \cdot 0.3 \cdot \hbar /(mc^{2}) = 0.6 \hbar /(mc^{2})
$$

The 0.6 is *algebraically* equal to $2 \cdot D_\mathrm{nd}(\mathrm{quantum})$. There is no freedom in this step.

### 3.3 The signal-speed identity

The canonical signal speed is $c_0 = L_0/T_0$:

$$
c_0 = [\hbar /(mc)] / [2 D_{\mathrm{nd}} \cdot \hbar /(mc^{2})] = c / (2 D_{\mathrm{nd}})
$$

Boxed:

$$
c_0 / c = 1 / (2 D_{\mathrm{nd}})
$$

For $D_\mathrm{nd} = 0.3$: $c_0/c = 1/0.6 \approx 1.667$. The 60% mismatch is the same algebraic fact as the 0.6 in $T_0$.

### 3.4 What the construction delivers

The 0.6 is reduced to a one-line identity: $0.6 = 2 \cdot D_\mathrm{nd}(\mathrm{quantum})$. This is not phenomenological. It is algebraic. The question "why 0.6?" is structurally identical to the question "why does the quantum regime have $D_\mathrm{nd} = 0.3$?"

Equivalently: $c_0/c = 1/(2 D_\mathrm{nd})$ is *universal* — it holds in every regime catalogued in the dimensional atlas, with $D_\mathrm{nd}$ the regime-specific channel weight. The "superluminal" $c_0 \approx 1.667 c$ is purely a statement about the canonical quantum-regime convention $D_\mathrm{nd} = 0.3$, not about any underlying physical signal.

---

## 4. The Five-Route Audit

If the algebraic reduction is correct, then independent derivation routes for the 0.6 must either (a) reproduce the same value through different physics, or (b) fail to produce 0.6. The framework audits five candidate routes; all five fail to produce the 0.6 from independent dynamics. This corroborates the dictionary-construction route as the unique source.

### 4.1 Route 1: Damping discriminant

Test: does the framework's damping discriminant function $D_\mathrm{crit}(\zeta) = \sqrt{2-\zeta} \cdot(2 - \sqrt{2-\zeta})$ produce $D_\mathrm{nd} = 0.3$ or $0.6$ as a fixed point, ratio, or invariant?

- At $\zeta= 0$: $D_\mathrm{crit} = 2\sqrt{2} - 2 \approx 0.828$. Not 0.3 or 0.6.
- At $\zeta= 1/4$ (canonical): $D_\mathrm{crit} \approx 0.896$. Not 0.3 or 0.6.
- At $\zeta= 1/2$: $D_\mathrm{crit} \approx 0.775$. Not 0.3 or 0.6.

Solving $D_\mathrm{crit}(\zeta) = 0.6$ yields $\zeta \approx 1.2$, outside the canonical $\zeta \in[0,1]$ range. No fixed point of the discriminant produces 0.3 or 0.6.

**Route 1 fails.**

### 4.2 Route 2: Reversible-slice QFT normalisation

Test: in the reversible slice ($D = 0$, $\zeta= 0$), does the free-scalar Hamiltonian's mass/speed normalisation force $T_0/L_0 = 0.6/c$?

The reversible slice has $D_\mathrm{nd} = 0$, so $T_0 = 2 \cdot 0 \cdot \hbar/(mc^2) = 0$. The $T_0/L_0$ ratio is formally degenerate. The QFT mode expansion uses $c_s = \sqrt{M_0}$ directly in absolute units and does not reference $T_0$ at all.

The 0.6 never enters the reversible-slice QFT construction. The $c_s = c/0.6$ identification is applied *after* the QFT construction, inherited from the dictionary.

**Route 2 fails.**

### 4.3 Route 3: Acoustic-metric curvature scaling

Test: does the Gaussian-bump closed-form curvature $R(0) = -a/[\sigma^2 (1-a)]$ or the Visser surface-gravity normalisation introduce a natural 0.6?

All curvature quantities are dimensionless functions of the bump amplitude $a$ and width $\sigma$ in units of $L_0$. No universal numerical prefactor of 0.6 or 0.3 appears at any order. The horizon-temperature formula $T_H = \hbar c_\infty^2 / (4\pi L k_B)$ inherits $c_\infty= c/0.6$ from the dictionary but does not *generate* it.

**Route 3 fails.**

### 4.4 Route 4: Coarse-graining / PME similarity scaling

Test: does porous-medium-equation similarity scaling produce $T_0/L_0 = 0.6/c$ as a self-similar fixed point?

The PME similarity solution $\rho_t = \Delta \rho^m$ in dimension $d$ decays as $t^{-\alpha}$ with $\alpha= d/(d(m-1)+2)$. For $d = 3$, $m = 2$: $\alpha= 3/5 = 0.6$.

This is a suggestive numerical coincidence. But $\alpha$ is a *temporal-decay exponent of the density*, not a velocity ratio. The Barenblatt similarity variable is $\xi= x \cdot t^{-\beta}$ with $\beta= 1/(d(m-1)+2) = 1/5$, giving a *time-dependent* characteristic velocity $\propto t^{\beta-1}$, not a constant $L_0/T_0$ ratio.

The 3/5 does not sit at the right place in the dimensional hierarchy to fix $T_0/L_0$. **Route 4 is a false positive — coincidentally the right number, structurally the wrong quantity.**

### 4.5 Route 5: $\zeta$-dependence interpolation

Test: does canonical $\zeta= 1/4$ combined with the reversible limit $\zeta= 0$ produce 0.6 as an interpolation constant?

No natural interpolation formula between $\zeta= 0$ and $\zeta= 1/4$ produces 0.6 or 0.3.

- Solving $\sqrt{2-\zeta}/2 = 0.6$ gives $\zeta= 0.56$, not canonical.
- Solving $1 - \sqrt{2-\zeta}/2 = 0.6$ gives $\zeta= 1.36$, outside the canonical range.

**Route 5 fails.**

### 4.6 The audit summary

| Route | Test | Verdict |
|---|---|---|
| 1: Damping discriminant | $D_\mathrm{crit}(\zeta)$ fixed point | Fails |
| 2: Reversible-slice QFT | Normalisation forces 0.6 | Fails (degenerate) |
| 3: Acoustic-metric curvature | Curvature formulae generate 0.6 | Fails |
| 4: PME similarity scaling | Self-similar fixed point | False positive |
| 5: $\zeta$-interpolation | Natural interpolation formula | Fails |
| **Dictionary construction** | $T_0 = L_0^2 D_\mathrm{nd}/D_\mathrm{phys}$ | **Succeeds (algebraically forced)** |

The dictionary-construction route is the unique successful route. The 0.6 inherits cleanly from $D_\mathrm{nd}(\mathrm{quantum}) = 0.3$ and from no other source.

---

## 5. The Equal-Rates Selection Rule

The boxed identity $c_0/c = 1/(2 D_\mathrm{nd})$ implies a clean structural fact: there is exactly one value of $D_\mathrm{nd}$ at which the dictionary's signal speed $c_0$ coincides with the physical speed of light $c$.

Setting $c_0 = c$:

$$
1 = 1 / (2 D_{\mathrm{nd}}) \implies D_{\mathrm{nd}} = 1/2
$$

At $D_\mathrm{nd} = 1/2$: $c_0 = c$ exactly. No free parameter, no fit.

### 5.1 Physical meaning of $D_\mathrm{nd} = 1/2$

The framework's substrate-level $D_\mathrm{nd}$ is the dimensionless ratio:

$$
D_{\mathrm{nd}} = \gamma_{\mathrm{dec}} / (\gamma_{\mathrm{dec}} + \omega_{\mathrm{sys}})
$$

where $\gamma_\mathrm{dec}$ is the local decoherence rate (the rate at which substrate channels populate / individuate via P11 commitments) and $\omega_\mathrm{sys}$ is the local coherent-system rate (the rate at which the substrate's reversible dynamics propagate the chain's participation rule).

For $D_\mathrm{nd} \to 0$: $\gamma_\mathrm{dec} \ll \omega_\mathrm{sys}$ — coherent dynamics dominate. The chain propagates reversibly with little individuation. This is the "deep-coherent" limit, structurally aligned with QM in its idealised form.

For $D_\mathrm{nd} \to 1$: $\gamma_\mathrm{dec} \gg \omega_\mathrm{sys}$ — decoherence dominates. The chain individuates rapidly. This is the "classical" limit.

For $D_\mathrm{nd} = 1/2$: $\gamma_\mathrm{dec} = \omega_\mathrm{sys}$ — *equal rates*. Decoherence and coherent propagation operate at the same substrate-level rate. This is a structurally distinguished operating point — the regime where the substrate operates symmetrically between commitment and propagation.

### 5.2 The selection rule

At the equal-rates point, the dictionary's canonical signal speed coincides exactly with the physical speed of light. This is a *new structural statement* not previously articulated in the corpus:

> **Equal-rates selection rule.** The substrate operates with $c_0 = c$ if and only if it sits at $D_\mathrm{nd} = 1/2$. Equivalently: rate-balance ($\gamma_\mathrm{dec} = \omega_\mathrm{sys}$) is the structurally distinguished regime where the dictionary's signal speed is the physical speed of light.

The canonical quantum-regime convention $D_\mathrm{nd} = 0.3$ sits *off* this distinguished point. The dictionary's $c_0$ is therefore *not* the physical speed of light at the canonical operating point — it is an atlas-nondimensionalisation artifact, not a physical signal speed.

### 5.3 Where ED-09.5 (Q-C transition) sits

The framework's quantum-classical transition arc (ED-09.5) identified the Q-C transition at $D_\mathrm{crit} \approx 0.896$ (post-2026-04-22 correction). This is substantially closer to $D_\mathrm{nd} = 1/2$ than the canonical-convention quantum regime at $D_\mathrm{nd} = 0.3$.

Whether the *true* Q-C transition sits at the equal-rates point $D_\mathrm{nd} = 1/2$ (where $c_0 = c$ exactly) or at $D_\mathrm{crit} \approx 0.896$ (where the damping discriminant signature appears) is a quantitative question. If they coincide, the framework has a clean structural identification: Q-C transition = rate-balance point = $c_0 = c$ point. If they don't coincide, the framework has two structurally distinct critical scales.

This is open work. The selection rule from §5.2 is structurally forced; whether it identifies with the Q-C transition is empirically open.

---

## 6. What the Reduction Buys

Even though the 0.6 is not independently derived, the reduction produces three structural statements that were not previously in the corpus:

### 6.1 The "60% speed mismatch" is not a physical anomaly

The framework's geometry-emergence and acoustic-analogue memos previously flagged $c_0 \approx 1.667 c$ as a mismatch requiring resolution. The reduction shows this is *not* a physical anomaly. It is a mismatch between an atlas-nondimensionalisation artifact and a physical invariant. The framework's substrate PDE is parabolic and has formally infinite signal speed anyway; the dictionary's $c_0$ is a regime-boundary marker, not a physical prediction.

The geometry-emergence memos can be updated to incorporate this framing rather than treat the mismatch as physically anomalous.

### 6.2 The universal channel-weight scaling

The identity $c_0/c = 1/(2 D_\mathrm{nd})$ is universal across the dimensional atlas. Each regime's signal speed is predicted to scale inversely with $2 D_\mathrm{nd}$. This is testable across analog-gravity platforms with differing $D_\mathrm{nd}$:

| Regime | $D_\mathrm{nd}$ | $c_0/c$ predicted |
|---|---|---|
| Quantum (canonical) | 0.3 | 1.667 |
| Equal rates | 0.5 | 1.0 |
| Strongly classical | $\to 1$ | $\to 0.5$ |
| Deep coherent | $\to 0$ | $\to \infty$ |
| ED-SC canonical | 0.25 | 2.0 |
| Galactic (per atlas) | varies | varies |

If analogue platforms at differing $D_\mathrm{nd}$ reproduce this scaling, the dictionary is empirically validated. If not, the $D_\mathrm{nd}$ anchoring is wrong in at least one regime. This is a precise falsifiable test.

### 6.3 The acoustic-analogue cross-regime consistency check

The framework's acoustic-analogue experimental program now has a sharper consistency test. Each regime's measured analog signal speed $c_s$ is predicted to obey $c_s/c = 1/(2 D_\mathrm{nd}(\mathrm{regime}))$. Cross-regime comparison of measured $c_s$ values against the framework's $D_\mathrm{nd}$ assignments is a direct empirical validation.

---

## 7. What's Forced, What's Inherited, What's Open

### 7.1 What's forced

The dictionary construction $T_0 = L_0^2 \cdot D_\mathrm{nd}/D_\mathrm{phys}$ is FORCED by the requirement that nondimensionalisation produce the standard dimensionless simulation equation. Any other choice of $T_0$ produces the wrong coefficient structure.

The algebraic identity $T_0 = 2 D_\mathrm{nd} \cdot \hbar/(mc^2)$ is FORCED by substituting Madelung-anchored $L_0 = \hbar/(mc)$ and $D_\mathrm{phys} = \hbar/(2m)$ into the construction.

The boxed identity $c_0/c = 1/(2 D_\mathrm{nd})$ is FORCED as a corollary, universal across regimes.

The equal-rates selection rule ($c_0 = c$ at $D_\mathrm{nd} = 1/2$) is FORCED as a structural consequence of the boxed identity.

### 7.2 What's inherited

The canonical quantum-regime convention $D_\mathrm{nd}(\mathrm{quantum}) = 0.3$ is INHERITED. It is set by the framework's initial nondimensionalisation, not derived from substrate primitives.

The Madelung anchor $D_\mathrm{phys} = \hbar/(2m)$ is INHERITED from U3 closure (Schrödinger walkthrough §5).

The Compton length $L_0 = \hbar/(mc)$ is INHERITED from the substrate's relativistic structure.

The numerical value of $\hbar$, $c$, $m$ are all inherited from substrate constants via the dimensional-atlas program.

### 7.3 What's open

The closed-form derivation of $D_\mathrm{nd}(\mathrm{quantum})$ from substrate primitives is the load-bearing open question. The 0.6 problem reduces to this exactly: the work of deriving 0.6 *is* the work of deriving $D_\mathrm{nd}(\mathrm{quantum})$.

The framework's *rate-balance-template program* (`ED-Dimensional-01-Ext.md`) is the active attempt to apply rate-balance derivation *within* the quantum regime to produce $D_\mathrm{nd}$ from first principles. Currently the template anchors $D_\mathrm{nd}$ for optomechanical, cavity-QED, condensed-matter, galactic, and cosmological regimes from independent rate identifications, but does not yet produce the quantum-regime value.

Whether the true Q-C transition sits at the equal-rates point $D_\mathrm{nd} = 1/2$ (where $c_0 = c$ exactly) or at the damping-discriminant point $D_\mathrm{crit} \approx 0.896$ is empirically open. If they coincide, the framework has a clean structural identification; if not, two distinct critical scales.

The atlas-independent formulation of the acoustic metric — expressing $c_s$ in observable-only quantities, bypassing $D_\mathrm{nd}$ — would resolve the dependence of $c_s$ on the dictionary convention. This is a tractable theory-only target.

---

## 8. What This Argument Establishes

The chain runs:

Substrate primitives + Madelung anchor (U3 closure → $D_\mathrm{phys} = \hbar/(2m)$) + Compton length ($L_0 = \hbar/(mc)$) + dimensional-atlas convention ($D_\mathrm{nd}(\mathrm{quantum}) = 0.3$) → dictionary construction $T_0 = L_0^2 \cdot D_\mathrm{nd}/D_\mathrm{phys}$ → algebraic identity $T_0 = 2 D_\mathrm{nd} \cdot \hbar/(mc^2) = 0.6 \, \hbar/(mc^2)$ → boxed identity $c_0/c = 1/(2 D_\mathrm{nd})$ → equal-rates selection rule ($c_0 = c$ at $D_\mathrm{nd} = 1/2$).

The 0.6 is no longer a structural mystery. It is a one-line algebraic consequence of the dictionary construction plus the canonical quantum-regime convention. Its appearance in the dimensional dictionary is structurally clean once the construction is made explicit.

The five-route audit confirms that no independent derivation route produces the 0.6 from non-dictionary physics. The dictionary-construction route is the unique source.

What's distinctive about this walkthrough's payload is its *honesty*. The 0.6 is not derived to closed form; it is *reduced* to a more fundamental open question (the $D_\mathrm{nd}$ anchoring problem). The reduction is partial. Three structural statements emerge that were not previously in the corpus:

1. The "superluminal" $c_0 \approx 1.667 c$ is a nondimensionalisation artifact, not a physical anomaly. The framework's substrate PDE has formally infinite signal speed anyway; $c_0 > c$ is a regime-boundary marker.

2. The universal scaling $c_0/c = 1/(2 D_\mathrm{nd})$ is a falsifiable cross-regime prediction. Analogue platforms at differing $D_\mathrm{nd}$ should reproduce the scaling.

3. The equal-rates selection rule ($c_0 = c$ at $D_\mathrm{nd} = 1/2$) is a structurally distinguished operating point. Whether the framework's Q-C transition sits at this point is open.

The framework reproduces the dimensional dictionary that generates the 0.6 exactly. It does not derive the underlying $D_\mathrm{nd}(\mathrm{quantum}) = 0.3$ from substrate primitives. That remains the framework's most directly addressable open question in the dimensional-atlas sector.

For the 0.6 specifically, the structural case is closed at the form level. The number is algebraically forced by the dictionary construction. The "60% speed mismatch" is a structural artifact, not a physical anomaly. The reduction to the $D_\mathrm{nd}$ anchoring problem is a clean rewriting of an apparently mysterious constant into a more fundamental open question.

This walkthrough's payload is smaller than Born or Schrödinger because the math content is one algebraic identity. But it serves a useful structural purpose: it documents how a conspicuous-looking constant in the framework's dimensional construction can be made transparent without requiring closed-form first-principles derivation. The 0.6 problem is no longer a problem; it is a bookmark pointing to a specific tractable open question.

---

## 9. References

- Bohm, D. "A Suggested Interpretation of the Quantum Theory in Terms of 'Hidden' Variables." *Physical Review* **85**, 166–179 (1952). [Madelung formulation]
- Madelung, E. "Quantentheorie in hydrodynamischer Form." *Zeitschrift für Physik* **40**, 322–326 (1927).
- Vázquez, J. L. *The Porous Medium Equation: Mathematical Theory.* Oxford University Press, 2007. [PME similarity scaling]
- Visser, M. "Acoustic black holes: horizons, ergospheres and Hawking radiation." *Classical and Quantum Gravity* **15**, 1767–1791 (1998).
- Proxmire, A. *The 0.6 Problem Resolution: Structural Identity from the Cross-Regime Nondimensional Invariant.* April 2026.
- Proxmire, A. *ED-Dimensional-01: Quantum Regime Dimensional Dictionary.* April 2026.
- Proxmire, A. *ED-Dimensional-01-Ext: Rate-Balance Template for $D_\mathrm{nd}$ Anchoring.* April 2026.
- Proxmire, A. *Walkthrough: From Primitives to the Schrödinger Equation.* April 2026. [Madelung anchor for $D_\mathrm{phys}$]
- Proxmire, A. *Wilsonian RG-Flow Analysis of the Canonical ED PDE: Operator-Basis Form-Closure and One-Loop Check.* April 2026.
- Proxmire, A. *Effective Acoustic Metric in Event Density.* April 2026.
- Proxmire, A. *Acoustic Analogue Experimental Program for Cross-Regime Signal-Speed Consistency.* April 2026.
- Proxmire, A. *Event Density: One Substrate, Three Domains.* April 2026.
- The full Event Density corpus, including all forced theorems and supporting memos, is available at https://github.com/allen-proxmire/event-density.
