# Pinning the Knee: Reducing the Offset–Velocity Law's Two Open Ingredients to Substrate Dynamics

**Author:** Allen Proxmire
**Arc:** Bullet_Arc (ED-Bullet-01) — Phase-3 (theory)
**Status:** Theory memo. Attacks the two open ingredients flagged in `Paper_ED_Bullet_TopologicalDefect` §7.1 that float the knee location (v_crit ~ 15–1500 km/s). Companion to the Phase-3 observational protocol (`Paper_ED_Bullet_Phase3_ObservationalProtocol`).
**Claim of this memo:** the two open ingredients are not two independent unknowns. Recast in standard Kibble–Zurek / relaxational-dynamics language, one is fixed by an already-derived ED result (GR-III), the other is resolved structurally by the defect's own pinned character, and what remains is a single residual: the static universality class of the substrate's organizational field. Net, the knee's location reduces to one number, and the reduction is honestly tiered.

---

## 0. The two ingredients, as Phase-2 left them

`Paper_ED_Bullet_TopologicalDefect` §7.1 named two physically-motivated estimates that its numbers rest on:

1. **The super-linear shock response.** Whether the substrate's organizational density rises super-linearly (vs merely linearly) under the merger's rapid reconfiguration sets the relaxation time τ_relax, hence the defect-formation threshold v_crit. Super-linear gives τ_relax ~ 10⁹ yr, v_crit ~ 150 km/s; linear gives τ_relax ~ 10¹⁰ yr, v_crit ~ 15 km/s.
2. **The two-timescale core/dressing structure.** The threshold (v_crit, a slow macroscopic clock) and the freeze-out separation (ξ_KZ, a fast core clock) are governed by different timescales, because the defect is stabilized by the cluster's own structure rather than a self-consistent vacuum mass gap. The mechanism was called consistent but "not yet fully worked out."

The two were treated as separate open items. They are not. Both are standard objects in the theory of defect formation once the problem is stated in its proper language.

## 1. The proper language: Kibble–Zurek with a dynamic exponent

Defect formation by a quench is Kibble–Zurek (KZ) physics, and KZ has a fixed anatomy. A system driven through its ordering transition at rate 1/τ_Q falls out of equilibrium when its relaxation time τ(ε) can no longer keep up with the drive. Near the transition, with reduced control parameter ε,
$$\tau(\varepsilon) = \tau_0\,\varepsilon^{-\nu z}, \qquad \xi(\varepsilon) = \xi_0\,\varepsilon^{-\nu},$$
where ν is the **static** correlation-length exponent and z the **dynamic** exponent. Freeze-out at $\hat t$ where $\tau(\varepsilon)=|\varepsilon/\dot\varepsilon|$ gives the two observables the arc needs:
$$\xi_{KZ}\sim\xi_0\left(\tau_Q/\tau_0\right)^{\nu/(1+\nu z)},\qquad \tau_{\rm freeze}\sim\tau_0\left(\tau_Q/\tau_0\right)^{\nu z/(1+\nu z)}.$$
And the **threshold** to form a defect at all is the condition that the drive outruns relaxation somewhere: the merger's interface-crossing time falls below the local relaxation time,
$$v_{\rm crit}\sim \frac{L_{\rm interface}}{\tau_{\rm relax}}.$$

So the whole knee is controlled by three inputs: the static exponent ν, the dynamic exponent z, and the macroscopic relaxation time τ_relax that sets the threshold. Phase-2's "super-linear shock response" is not a free knob; it is a statement about **how τ_relax scales**, i.e. about z and the interface value of τ_relax. Phase-2's "two-timescale structure" is the ordinary KZ fact that the correlation length and the relaxation time freeze on **different** power laws of the same quench (exponents ν/(1+νz) and νz/(1+νz)), *plus* a modification from pinning (§3). Naming them this way is the whole reduction: two vague ingredients become {ν, z, τ_relax}, and two of those three are now fixable.

## 2. Ingredient 1, fixed: the dynamic exponent is z = 2, from GR-III

The dynamic exponent z is set by *how the order parameter relaxes*, and ED has already derived the relevant dynamics. GR-III (`Paper_GR-III_DynamicalRule`) gives the substrate's dynamical bandwidth rule
$$\dot b = D\,\nabla^2 b - \kappa\,\rho,$$
a **relaxational, dissipative, non-conserved** evolution: the field relaxes diffusively toward the source-determined configuration, with no conservation law pinning its integral. In the Hohenberg–Halperin classification of dynamic critical behavior, a non-conserved order parameter relaxing by exactly this kind of dissipative gradient flow is **Model A**, whose dynamic exponent is
$$z = 2 + c\,\eta \approx 2$$
(η the small anomalous dimension). The organizational field n on S² is the orientation companion of b, and its natural relaxation is the same dissipative gradient flow (∂ₜn ∝ ∇²n + …, non-conserved, since orientation is not a conserved density). So the substrate's organizational transition inherits **Model A dynamics, z = 2**, from a rule that is already part of the corpus rather than a new assumption.

This is the honest tier: z = 2 is **structural**, grounded in GR-III's derived relaxational form, conditional on the orientation field sharing b's dissipative dynamics (a natural reading, stated as such). It removes one of the three unknowns.

**What z = 2 does to "super-linear."** With z fixed at 2, the relaxation time near the transition scales as τ ~ ε^{−2ν}. The "super-linear shock response" Phase-2 invoked is the statement that, at the compressed interface where ε is driven hard, τ_relax is shortened relative to the naive gas-compression estimate — which is exactly what a diffusive relaxation time τ ~ L²/D does when the effective D rises with the organizational density at the shock. Super-linearity is not an extra hypothesis; it is τ ~ ε^{−2ν} evaluated at the interface, i.e. Model-A relaxation with the interface's driven ε. The remaining freedom is entirely in ν and the interface value of D, not in a separate "response exponent."

## 3. Ingredient 2, resolved: the defect is a pinned texture, so two clocks is structural

Phase-2's second open item was *why* the threshold clock and the freeze-out clock differ. In a textbook KZ soliton they need not: a self-consistent defect has one healing length ξ_core = 1/(mass gap) and one relaxation time, both set by the same vacuum stiffness. The arc's numbers require them decoupled, and Phase-2 attributed this to the defect being "held together by the cluster's structure rather than a self-contained object" without working out the mechanism.

The mechanism is that the defect is a **pinned texture, not a free soliton**, and this is forced, not optional, by ED's own account (Phase-2 §4.4 core/dressing; the winding is topologically protected but has no self-consistent vacuum mass gap in the substrate). Concretely:

- **The core (fast clock).** The winding's healing length ξ_core is set not by a vacuum mass gap (there is none) but by the local gradient of the cluster's commitment density ρ_event — the scale over which the pinning environment varies. This is a **microscopic, environment-set** length, and it sets ξ_KZ. It responds on the fast core time because it is a local balance against a fixed external gradient.
- **The dressing (slow clock).** The extended field around the core relaxes by the macroscopic Model-A diffusion of §2, on τ_relax ~ L²/D over the cluster scale L. This is the **macroscopic** clock that sets v_crit and the observable lifetime.

Because one length is pinned to an external gradient and the other is macroscopic diffusion, the two clocks are **independent by construction** — there is no single vacuum stiffness forcing them equal, precisely because the defect has no self-consistent mass gap. So the "two-timescale structure" is not an unexplained coincidence to be worked out; it is the direct signature of an externally-pinned texture, and its existence is **structural**. What remains quantitative is the value of ξ_core (the ρ_event gradient scale at a cluster interface), an astrophysical input, not a substrate unknown.

This converts ingredient 2 from "open mechanism" to "resolved in kind, one astrophysical length to plug in."

## 4. The residual: one number, the static universality class ν

After §2 (z = 2) and §3 (pinning resolves the two-clock structure and hands ξ_core to astrophysics), the knee's location reduces to a **single** substrate unknown: the static correlation-length exponent ν of the organizational field's ordering transition. It enters both observables through KZ:
$$\xi_{KZ}\sim\xi_0\left(\tau_Q/\tau_0\right)^{\nu/(1+2\nu)},\qquad v_{\rm crit}\sim L_{\rm interface}/\tau_{\rm relax}(\nu).$$

The natural expectation, stated as a target not a result: the order parameter is a unit vector on S², i.e. an O(3) field, and a 3D O(3) (Heisenberg) ordering transition has ν ≈ 0.70. **If** the substrate's coarse-grained organizational transition sits in the 3D O(3) universality class, then ν ≈ 0.70 with z = 2 fixes the KZ exponents outright, and the v_crit band collapses from the Phase-2 factor-of-100 (15–1500 km/s) toward a specific value near the arc's 150 km/s working number. That "if" is the honest residual: it requires the substrate's actual coarse-grained free energy for the n-field, which is not derived. Deriving it (or measuring the effective ν from the certified substrate's organizational relaxation) is the one remaining theory step, and it is a well-posed one.

## 5. Net result and honest ledger

The two open ingredients are reduced to one:

| Phase-2 open item | Status after this memo | Tier |
|---|---|---|
| Super-linear shock response (sets τ_relax, v_crit) | **= the dynamic exponent z; fixed at z ≈ 2 by GR-III's relaxational (Model-A) rule** | structural (grounded in a derived ED result; conditional on n sharing b's dissipative dynamics) |
| Two-timescale core/dressing structure | **Resolved: the defect is a pinned texture with no vacuum mass gap, so core (ξ_core, environment-set) and dressing (τ_relax, macroscopic diffusion) clocks are independent by construction** | structural (forced by ED's own no-mass-gap account); leaves ξ_core as an astrophysical input, not a substrate unknown |
| Where the knee sits | **Reduced to a single residual: the static exponent ν of the S² organizational transition** | open — needs the substrate's coarse-grained free energy; O(3)/Heisenberg ν ≈ 0.70 is the target, not yet derived |

Two consequences worth stating:

- **The observational protocol is unchanged and its logic is vindicated.** The Phase-3 protocol targets the knee's *existence and sharpness*, not its location, precisely because the location depended on open ingredients. This memo tightens the location (z fixed, two-clock structure resolved, one residual ν) but does not change that the shape is the robust, ED-distinctive test. The sharpness (F2) in particular is untouched: it follows from the transition being genuine ordering (all-or-nothing defect formation), independent of ν.
- **The next theory step is now singular and well-posed.** Derive (or measure on the certified substrate) the static exponent ν of the organizational field's ordering transition. With z = 2 already in hand and the pinning structure resolved, ν alone converts the arc's order-of-magnitude v_crit into a pinned prediction. That is a far sharper target than "work out the shock response and the stabilization," which is what Phase-2 left.

## 6. Honest scope

This memo derives nothing from nothing. z = 2 is conditional on the orientation field n inheriting the dissipative, non-conserved relaxation that GR-III derives for b — a natural but stated reading. The pinning resolution of the two-clock structure is forced by ED's own no-self-consistent-mass-gap account, but the value of ξ_core is an astrophysical gradient scale, not computed here. And the residual ν is genuinely open: the O(3)/Heisenberg reading is a target motivated by the S² order parameter, not a derivation, and could be wrong if the substrate's coarse-grained free energy is not in that class (e.g. if long-range or non-standard couplings shift the universality class). What the memo does is real and bounded: it collapses two vague open ingredients into one sharp, well-posed one, grounds the dynamic half in an existing corpus result, and resolves the two-timescale puzzle structurally — turning "two things to work out" into "one exponent to pin."
