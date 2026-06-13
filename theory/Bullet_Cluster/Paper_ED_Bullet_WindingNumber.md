# Paper — The Winding Number, Charge Conservation, and Pair Evolution for *S²* Defects in Substrate-Organizational Mergers

## Bullet_Arc Phase-2, Deliverable D2.2

**Author:** Allen Proxmire
**Date:** June 2026
**Arc:** Bullet_Arc (ED-Bullet-01)
**Status:** Opening sections (Sections 1–2 of D2.2)
**Related deliverables:** D2.1 — `Paper_ED_Bullet_VacuumManifold.md` (complete); D2.3 — `Paper_ED_Bullet_RelaxationTime.md` (in progress)

---

## Abstract

D2.1 established the substrate's organizational order parameter as a unit vector field **n**(*x*) with vacuum manifold *S²*, and identified the point-monopole defects supported by π₂(*S²*) = ℤ. This paper defines the conserved topological charge — the **winding number** — that characterizes these defects formally, verifies its conservation under the Section-7 dynamics, and computes the post-formation evolution of monopole-antimonopole pairs through their three dynamical phases: **advection** with subcluster flow, **annihilation** when separations become small, and **decoherence** through environment-induced fluctuations.

The principal results: (i) the winding number Q is identically conserved by anti-symmetry of the topological current, holding in both V1 and V5 kernel formulations; (ii) pair lifetimes are dominated by annihilation suppression at large separations, giving τ_pair ≳ 10⁸ years for Bullet-class geometries; (iii) decoherence is sub-dominant on relevant timescales, validating the steady-state defect density estimate used in Section 10 of D2.1.

D2.2 hands off to D2.3 the requirement that τ_relax (from D2.3's substrate-parameter derivation) satisfies τ_relax ≲ τ_pair, so that the relaxation-time gates the active-defect population rather than the pair annihilation.

This paper covers **Sections 1–2**: introduction and scope, and the formal definition of the winding number. Sections 3–6 (charge conservation in merging environments; advection; annihilation; decoherence) and Section 7 (hand-off to D2.3 and the synthesis paper) follow in continued work.

---

## 1. Introduction and Scope

### 1.1 Purpose of D2.2

D2.1 closed with the *S²* order parameter recommendation, the Lagrangian construction, the Kibble-Zurek defect-density estimate, the kernel-portability profile, and the cosmological-rate consistency check. What D2.1 did *not* do is formally verify that the defects it predicts can persist long enough — on cosmological-rate-relevant timescales — for the Section-10 active-defect calculation to be valid.

D2.2 supplies that verification. Specifically, this deliverable must:

- **Define** the topological charge Q (the winding number) for the *S²* order parameter introduced in D2.1
- **Compute** Q for the explicit hedgehog configuration that represents an isolated Bullet monopole
- **Establish** the four conservation conditions (D2.1 Section 11.2) under which Q is preserved
- **Derive** the post-formation evolution of monopole-antimonopole pairs through their three dynamical phases
- **Verify** that the pair lifetime τ_pair satisfies τ_pair ≳ 10⁸ years for Bullet-class parameters, validating Section-10's active-defect estimate
- **Hand off** to D2.3 the explicit dependency on τ_relax, so that D2.3's substrate-parameter derivation closes the open numerical inputs

The deliverable is structurally tightly coupled to D2.3: D2.2 needs τ_relax from D2.3 to verify pair lifetimes, while D2.3 needs the conservation argument from D2.2 to verify that defects are actually stable on the timescales used in the steady-state calculation. The two should be developed in parallel; this paper produces the side of the calculation that does not require D2.3's substrate-parameter values.

### 1.2 Structural role of the winding number in the Bullet mechanism

The winding number plays three distinct structural roles in the Bullet_Arc mechanism. Each is load-bearing for the arc's overall claim.

**Role 1 — Quantization of defect identity.** The winding number is the integer that *labels* a topological defect. Without Q, "the substrate has a defect here" is qualitative; with Q, the defect is a specific quantum-mechanical-style discrete object — a monopole with Q = +1, an antimonopole with Q = −1, or higher-charge configurations Q = ±2, ±3, etc.

The quantization is enforced by the topology π₂(*S²*) = ℤ, identified in D2.1 Section 5. Continuous deformations of **n**(*x*) cannot change Q; only configurations passing through singularities (where **n** is ill-defined) can produce or destroy charge. This rigidity is what makes the defect *stable* on relevant timescales.

**Role 2 — Conservation under merger dynamics: monopole-antimonopole pair creation.** Charge conservation forces a structural requirement: defects must be created in pairs of opposite charge. Total topological charge of the universe pre-merger is zero (no defects); total post-merger must also be zero (charge cannot spontaneously appear from nothing). The merger therefore produces **monopole-antimonopole pairs** with Q_pair = Q_+ + Q_− = +1 + (−1) = 0.

This is essentially the same constraint that governs Higgs-mechanism defect production in early-universe cosmology, particle-antiparticle production in QED, and vortex-pair nucleation in superfluids. It is a generic feature of any topological-defect-formation mechanism in any field theory respecting charge conservation.

For Bullet_Arc, the pair-production requirement is what produces the *two* lensing peaks observed at the Bullet (one for each charge of the pair) — exactly the observational signature D2.1 was designed to reproduce.

**Role 3 — Post-formation evolution.** Once formed, the pair evolves dynamically. The monopole and antimonopole are not static — they drift with their subcluster's pre-merger orientation, can in principle annihilate when their separation drops, and lose coherence with their environment through interactions. The winding number is *conserved* only over timescales much shorter than these dissipative processes; over longer timescales, the pair "decays" through annihilation or decoherence, returning the substrate to a zero-charge configuration.

The post-formation evolution determines how long the Bullet-class signatures persist after the merger, and therefore how many active defects we observe at any given cosmological epoch. D2.2's calculation of this evolution is what validates Section 10's steady-state defect-density estimate.

### 1.3 The three dynamical phases

D2.2 must describe pair evolution through three phases. Each has distinct timescales and dynamics.

**Phase A — Advection with subcluster flow.** Immediately after formation at the merger interface, each defect drifts with its associated subcluster's pre-merger orientation **n**_eq^A or **n**_eq^B. This drift is *passive* in the sense that the defect does not undergo internal change; it simply moves with the substrate's organizational flow.

The advection equation governs the defect's position trajectory **r**(*t*) as a function of the substrate's organizational propagation speed c_s, the local **n**_eq gradient, and the gravitational drift of the host subcluster. Section 4 of D2.2 derives the advection equation explicitly.

For Bullet parameters, the advection timescale is t_advect ~ R_subcluster / v_subcluster ~ 10⁸ years — comparable to but shorter than τ_relax. The advection phase ends when the defects reach approximate equilibrium positions within their host subclusters.

**Phase B — Annihilation channels.** A monopole and antimonopole can in principle annihilate when their separation drops below the monopole core size r_core. Annihilation requires the pair to drift back together against the cluster expansion and against the natural advection of each defect into its own subcluster.

For Bullet-class systems, the pair separation is ~100s of kpc and remains so or grows as the subclusters separate. Annihilation rate Γ_ann is therefore expected to be exponentially suppressed in the separation-over-r_core ratio. Section 5 of D2.2 computes Γ_ann explicitly.

The annihilation timescale 1/Γ_ann for Bullet geometries is expected to exceed 10¹⁰ years — far longer than τ_relax, the cluster-merger crossing time, or even the cosmological age. Annihilation is *not* the lifetime-limiting process for Bullet-class pairs.

**Phase C — Decoherence / dissolution.** A subtler decay channel: the monopole's coupling to the substrate's commitment-density background allows slow "decoherence" of the topological charge through environment-induced fluctuations. This is analogous to the decoherence of quantum superpositions through environmental coupling, but applied to the substrate's organizational structure.

Decoherence does not move the defect; it dissipates the *topological coherence* of the defect, gradually returning the local **n**(*x*) configuration to the substrate's underlying vacuum. Over very long timescales, this could potentially destroy the defect even at large separations from its pair partner.

Section 6 of D2.2 computes the decoherence rate Γ_dec. The expected result: Γ_dec · τ_relax ≪ 1, meaning decoherence is sub-dominant to relaxation. The pair lifetime is bounded above by τ_relax (the substrate's organizational coherence time), not by decoherence.

### 1.4 Dependencies on D2.1 and interfaces with D2.3

**Dependencies inherited from D2.1.** D2.2 takes the following as established:

- The *S²* order parameter with constraint |**n**|² = 1 (D2.1 §5–§7)
- The Lagrangian 𝓛 = 𝓛_σ + 𝓛_Sky + 𝓛_quench + 𝓛_strain (D2.1 §7.4.1)
- The Euler-Lagrange equations of motion (D2.1 §7.6)
- The hedgehog monopole solution with finite-energy r_core (D2.1 §7.7)
- The Kibble-mechanism pair production at the merger interface (D2.1 §7.8, §8.5)
- The kernel-portability profile: topology kernel-independent, dynamics V5-native (D2.1 §9)

These are not re-derived; D2.2 builds on them.

**Interfaces with D2.3.** D2.2 produces three outputs that D2.3 consumes:

- Γ_ann(separation, v_pair, substrate parameters) — the annihilation rate as a function of pair separation and substrate constants
- Γ_dec(commitment density, substrate parameters) — the decoherence rate as a function of environmental coupling
- τ_pair (the pair lifetime) as a function of substrate parameters

D2.3 produces three outputs that D2.2 consumes:

- τ_relax derived from substrate primitives
- The numerical values of (κ, c_s, β, γ, e)
- The cosmological evolution of these parameters (if any)

The mutual dependency is:

| D2.2 needs from D2.3 | D2.3 needs from D2.2 |
|---|---|
| τ_relax (to bound τ_pair from above) | Conservation argument (to verify defect stability) |
| (κ, c_s, β, γ, e) numerical values | Γ_ann, Γ_dec (to estimate active-defect density) |
| Cosmological β(z), γ(z) if non-constant | τ_pair structural form (to close the steady-state calculation) |

Phase-2 closure requires both deliverables to be developed in parallel and converge.

### 1.5 Paper structure

Section 2 (below) defines the winding number Q formally. Sections 3 through 6 address the dynamical phases: Section 3 covers charge conservation in the merging-cluster environment; Section 4 derives the advection equation; Section 5 computes the annihilation rate; Section 6 derives the decoherence rate. Section 7 closes D2.2 with hand-off to D2.3 and the Phase-2 synthesis paper.

This paper covers Sections 1 and 2. The remaining sections will be filed as continued D2.2 work.

---

## 2. Formal Definition of the Winding Number

### 2.1 Setup — the map **n**(*x*): *S²*_surface → *S²*_target and homotopy classification

The substrate's organizational order parameter is the field **n**(*x*): ℝ³ → *S²*, with the constraint |**n**|² = 1 making the codomain the 2-sphere of channel orientations (the *target S²*).

To probe the topological structure produced by an isolated defect, consider any closed 2-surface Σ ⊂ ℝ³ enclosing the defect. The restriction of **n**(*x*) to Σ defines a *map* from Σ to the target:

```
n |_Σ  :  Σ → S²
```

If Σ is topologically a 2-sphere (and any closed 2-surface in ℝ³ is topologically equivalent to *S²*), this map is precisely a *S²* → *S²* mapping. The homotopy classification of such maps is:

```
π₂(S²) = ℤ
```

— maps from *S²* to *S²* are classified by an integer. Two maps with the same integer can be smoothly deformed into each other; two with different integers cannot. The integer is the **winding number** or **degree** of the map.

For the substrate's defect, the integer captures *how many times* the map **n**|_Σ wraps the target *S²* as one covers the surface Σ once. A trivially-mapped surface (where **n** points in the same direction everywhere on Σ) has degree zero — no winding, no defect inside. A surface where **n** wraps the target once has degree one — a monopole inside. A surface where **n** wraps the opposite way once has degree −1 — an antimonopole inside.

The winding number is the formal label for the defect.

### 2.2 The topological current and the winding-number integral

The conserved topological current for the *S²* order parameter is:

```
J^μ = (1/8π) ε^{μνρσ} ε_{abc} n^a (∂_ν n^b)(∂_ρ n^c) ∂_σ
```

Equivalently in 3+1D component form: the spatial part is

```
J^i = (1/8π) ε^{ijk} ε_{abc} n^a (∂_j n^b)(∂_k n^c)
```

— a 3-vector built from the order parameter and its gradients.

The total winding number enclosed by a closed surface Σ is obtained by integrating the topological current's flux through Σ:

```
Q = ∫_Σ  J · dS  =  (1/8π) ∫_Σ  ε^{ijk} n · (∂_i n × ∂_j n) dS_k
```

Where (in the simplified vector notation) the integrand inside the surface integral involves the cross product taken in the target *S²* internal space and the dot product taken in the same space. The result is a scalar field on Σ, and the integral is over the surface.

In spherical coordinates (θ, φ) parametrizing the surface Σ as a sphere of radius *R* around the defect:

```
Q = (1/4π) ∫₀^π ∫₀^{2π}  n · (∂_θ n × ∂_φ n)  dθ dφ
```

The factor 1/(4π) (rather than 1/(8π)) arises because the surface integral over θ-φ collapses the antisymmetric ε^{ijk} index structure into a single scalar. The two forms are equivalent.

### 2.3 Geometric interpretation as the degree of the map

The geometric meaning of Q is captured by the **degree of the map** interpretation. Given a continuous map f: *S²* → *S²*, the degree is defined as:

```
deg(f) = (number of pre-images of a generic point in the target, weighted by orientation)
```

Equivalently: the degree counts how many times the map covers the target. A degree-1 map covers the target once; degree-2 covers it twice; degree -1 covers it once with reversed orientation; degree 0 does not cover any open neighborhood of a generic point.

The winding-number integral expression above is the *explicit calculation* of the degree for our specific map **n**|_Σ. The factor 1/(4π) normalizes the integral so that a single covering of the target gives Q = 1; the integration formula realizes the geometric counting.

For our substrate field, the geometric reading is:

- **Q = +1:** As one walks around the defect, the field **n**(*x*) rotates through every direction on the target *S²* exactly once in the standard orientation. The defect is a **monopole** (channel-orientation hedgehog with outward-radial structure).
- **Q = −1:** Same, but with reversed orientation. The defect is an **antimonopole** (hedgehog with inward-radial structure).
- **Q = 0:** No net winding; the field can be smoothly deformed to a constant on Σ. No defect enclosed.

The Bullet's two lensing peaks correspond to Q = +1 and Q = −1 defects — a monopole-antimonopole pair with total charge zero.

### 2.4 Computation for the hedgehog configuration

The canonical monopole solution from D2.1 Section 7.7 is the hedgehog:

```
n(x) = x̂ = x / |x|

In spherical coordinates:  n = (sin θ cos φ, sin θ sin φ, cos θ)
```

Direct computation of the partial derivatives:

```
∂_θ n  =  (cos θ cos φ,  cos θ sin φ,  −sin θ)
∂_φ n  =  (−sin θ sin φ,  sin θ cos φ,  0)
```

The cross product (target-space):

```
(∂_θ n × ∂_φ n)  =  (sin² θ cos φ,  sin² θ sin φ,  sin θ cos θ)
                 =  sin θ · (sin θ cos φ,  sin θ sin φ,  cos θ)
                 =  sin θ · n
```

The integrand:

```
n · (∂_θ n × ∂_φ n)  =  n · (sin θ · n)  =  sin θ × |n|²  =  sin θ
```

(using |**n**|² = 1).

Integrating:

```
Q_hedgehog  =  (1/4π) ∫₀^π ∫₀^{2π}  sin θ  dφ dθ
            =  (1/4π) × 2π × ∫₀^π sin θ dθ
            =  (1/4π) × 2π × 2
            =  1
```

**Q = +1** for the hedgehog. ✓

The antihedgehog (**n**(*x*) = −*x̂*) gives **Q = −1** by symmetry. The two configurations together — co-located in a pair — sum to total charge zero, as required by conservation.

### 2.5 The four conservation conditions

D2.1 Section 11.2 specified four conditions under which the winding number must be conserved. We restate them here and identify which of Sections 3–6 will address each.

**C2.2.1 — Identical conservation by anti-symmetry.**
The topological current J^μ is identically conserved (∂_μ J^μ = 0) as a mathematical consequence of the anti-symmetry of ε^{μνρσ} and the constraint |**n**|² = 1. This must hold without further assumption.

*Addressed in:* Section 3.1 — direct calculation of ∂_μ J^μ = 0 using ε-tensor identities.

**C2.2.2 — Conservation under the Section-7 equations of motion.**
The dynamics of **n**(*x*) include the quench coupling β ρ_c (**n** · **n**_eq) and strain coupling γ ρ_c (∇**n**)². These terms could in principle introduce source terms for the topological current. D2.2 must verify they do not.

*Addressed in:* Section 3.2 — explicit calculation showing the quench and strain couplings preserve the *S²* manifold and therefore do not source J^μ.

**C2.2.3 — Conservation at the grain cutoff.**
The substrate's UV cutoff at the grain scale ℓ_P regularizes the monopole core. D2.2 must verify that the topological current is well-defined at and below the cutoff, and that the regularization does not introduce a spurious source at ℓ_P.

*Addressed in:* Section 3.3 — analysis of the current at the grain cutoff using either the Skyrme-type effective term or the explicit cutoff boundary condition.

**C2.2.4 — Conservation under V5 outer-scale coupling.**
The V5 outer-scale coupling produces the equilibrium orientation field **n**_eq(*t*, *x*). D2.2 must verify that **n**_eq's spatial structure does not introduce a spurious source term in the conservation equation.

*Addressed in:* Section 3.4 — explicit verification that the coupling β ρ_c (**n** · **n**_eq) is invariant under the symmetries that generate the topological current.

All four conditions must be satisfied for the conservation argument to close. Failure of any one would indicate that the dynamics violates topological charge conservation, which would in turn require revision of either the Lagrangian or the order-parameter identification.

### 2.6 Implications for Section 3 — Charge Conservation in a Merging Cluster Environment

Section 2 established the formal apparatus: the winding number Q as the degree of the map **n**|_Σ: Σ → *S²*, the explicit integral expression in both surface and spherical-coordinate forms, the geometric interpretation, and the computation Q = +1 for the hedgehog configuration. Section 2 also identified the four conservation conditions D2.2 must verify.

Section 3 takes up the verification work. The strategy:

1. **Section 3.1.** Show that ∂_μ J^μ = 0 *identically* (without using the equations of motion) by direct calculation. This is a standard result for topological currents in *S²* sigma models but should be reproduced explicitly for the substrate-specific case to verify no implicit assumptions are violated.

2. **Section 3.2.** Show that the equations of motion derived in D2.1 Section 7.6 preserve the conservation. The key technical step: verify that the quench coupling β ρ_c (**n** · **n**_eq) and the strain coupling γ ρ_c (∇**n**)² maintain |**n**|² = 1 and the topological structure of *S²*.

3. **Section 3.3.** Analyze the grain cutoff at ℓ_P. The substrate's UV regularization must not introduce a spurious source in the topological current. Either Skyrme-type regularization or explicit cutoff boundary conditions can be used; both should give the same result.

4. **Section 3.4.** Verify that the V5 outer-scale coupling does not source J^μ. This is the V5-specific consistency check; if it fails, kernel-portability for the conservation argument is broken.

The expected outcome of Section 3 is that all four conservation conditions are satisfied. The winding number Q is therefore a conserved quantum number in both V1 (kinematics) and V5 (dynamics) — establishing the topological-charge label as a rigorous invariant of the substrate's organizational state.

With Section 3's verification complete, Sections 4–6 will derive the three dynamical phases (advection, annihilation, decoherence) under the assumption that Q is conserved on the relevant timescales. Section 7 will close D2.2 by handing off to D2.3.

---

*End of Section 2. Section 3 below works through the conservation verifications C2.2.1–C2.2.4 in detail.*

---

## 3. Charge Conservation in a Merging Cluster Environment

### 3.0 Restatement of the four conditions and the goal of Section 3

Section 2.5 specified four conditions under which the winding number Q must be conserved. We restate them compactly:

- **C2.2.1 — Identical conservation.** The topological current is conserved as a mathematical identity (∂_μ J^μ = 0 by antisymmetry of ε and |**n**|² = 1), independent of dynamics. Consequence: total charge is fixed at its initial value.
- **C2.2.2 — EOM conservation.** The Euler-Lagrange equations of D2.1 §7.6, including the quench and strain couplings, preserve the conservation away from defect cores. Charge changes only via core-level processes (pair annihilation).
- **C2.2.3 — Grain-cutoff conservation.** The substrate grain ℓ_ED regularizes the defect core and prevents charge leakage through sub-grain (UV) channels.
- **C2.2.4 — V5-coupling conservation.** The V5 outer-scale coupling modifies the substrate's dynamics during the quench but does not source net topological charge.

**Goal of Section 3.** Verify that each of the four conditions holds for a Bullet-class merger. The verification establishes that the winding number is a rigorous conserved invariant throughout the merger event — which in turn forces the monopole-antimonopole pair structure that produces the Bullet's two-peak observational signature. Section 3 does not assume conservation; it derives it from the four conditions.

### 3.1 Identical-conservation condition (C2.2.1)

**Claim:** Q_total is identically zero before and after the merger.

**Identical conservation of the current.** The topological current (Section 2.2) is:

```
J^μ = (1/8π) ε^{μνρσ} ε_{abc} n^a (∂_ν n^b)(∂_ρ n^c)  [contracted appropriately]
```

Its divergence:

```
∂_μ J^μ = (1/8π) ε^{μνρσ} ε_{abc} (∂_μ n^a)(∂_ν n^b)(∂_ρ n^c)  [× constraint terms]
```

Every term in this expression contracts a *symmetric* pair of derivative indices (from the product of three first-derivatives, two must share a coordinate index when summed against the rank-4 antisymmetric ε) with the *antisymmetric* ε^{μνρσ}. A symmetric-antisymmetric contraction vanishes identically. Therefore:

```
∂_μ J^μ = 0     (identically, independent of equations of motion)
```

This is the standard result for *S²* sigma-model topological currents (the "topological" in topological current refers precisely to this identity-level conservation). It holds for *any* field configuration **n**(*x*), not only solutions of the equations of motion. The substrate-specific verification adds nothing new to the standard mathematics; it simply confirms that no implicit assumption in the substrate's formulation breaks the identity.

**Pre-merger configuration has Q = 0.** Before the merger, each subcluster carries a smooth, defect-free organizational field. Within subcluster A, **n**(*x*) ≈ **n**_eq^A (a constant direction up to slow spatial variation); within subcluster B, **n**(*x*) ≈ **n**_eq^B. A smooth field with no singularity is, by construction, homotopically trivial — it can be continuously deformed to a global constant. Its winding number through any enclosing surface is zero.

Total pre-merger charge, integrated over a surface enclosing the entire two-cluster system:

```
Q_total^pre = 0
```

**Post-merger configuration must satisfy Q_+ + Q_- = 0.** Because ∂_μ J^μ = 0 identically, the total charge enclosed by a surface that remains outside the entire system is *conserved* throughout the merger:

```
Q_total^post = Q_total^pre = 0
```

If the merger produces defects (which D2.1 §7.8 established it does, via the Kibble mechanism), those defects must carry charges that sum to zero. The minimal nontrivial configuration is a single pair:

```
Q_+ + Q_-  =  (+1) + (−1)  =  0  ✓
```

**Why this forces pair production — the structural origin of the two-peak signature.** Conservation forbids the creation of a single isolated monopole. A lone Q = +1 defect would change the total charge from 0 to +1, violating the identity ∂_μ J^μ = 0. The only way the merger can produce defects while respecting conservation is to produce them in charge-canceling sets — the simplest being a monopole-antimonopole pair.

This is the topological origin of the Bullet's two-peak lensing signature. The two peaks are not two independent objects that happen to appear; they are the two halves of a single conserved-charge-zero pair. The pair *must* have two members of opposite charge, and each member carries a localized gravitational signature (D2.1 §7.7). Two peaks, opposite topological charge, zero total — forced by conservation.

The observation of exactly two offset lensing peaks at the Bullet, rather than one or three, is therefore a direct consequence of topological charge conservation. A framework producing a single offset peak, or an odd number of peaks, would be inconsistent with the topological mechanism. The Bullet's two-peak structure is the conservation law made visible.

### 3.2 EOM conservation (C2.2.2)

**Claim:** The Euler-Lagrange dynamics of D2.1 §7.6 preserve charge conservation away from defect cores; charge can change only through monopole-antimonopole annihilation, which is dynamically suppressed on merger timescales.

**∂_μ J^μ = 0 holds away from cores.** Section 3.1 showed the conservation is an identity — it holds for any smooth field configuration regardless of the equations of motion. The equations of motion enter only at points where **n**(*x*) is *not* smooth: the defect cores, where **n** is ill-defined (the field "tries to point in all directions at once" at the singular point).

Away from cores, **n**(*x*) is smooth and the identity ∂_μ J^μ = 0 applies directly. The quench coupling β ρ_c (**n** · **n**_eq) and the strain coupling γ ρ_c (∇**n**)² appear in the equations of motion (D2.1 §7.6) but they act on the field's *dynamics* — how **n** evolves in time — not on the *topological structure* of a given field configuration. Since the topological current depends only on **n** and its spatial gradients at a fixed time, and since both couplings preserve the constraint |**n**|² = 1 (the field stays on *S²*), neither coupling can source the topological current away from cores.

Explicitly: the quench coupling drives **n** toward **n**_eq, but this driving is a *rotation on S²* (it preserves |**n**|² = 1). A rotation on the target sphere is a homotopically trivial deformation — it cannot change the degree of the map **n**|_Σ. The strain coupling modulates the gradient energy cost but likewise preserves the manifold. Therefore the equations of motion preserve Q away from cores.

**Charge can only change via annihilation.** The single way to change the total winding number is for two defects of opposite charge to meet and mutually cancel. When a Q = +1 monopole and a Q = −1 antimonopole approach within ~ r_core, their cores overlap, the field can smoothly "unwind" through the overlap region, and both charges disappear:

```
Q = +1  and  Q = −1   →   Q = 0      (annihilation)
```

This is the *only* charge-changing process. It requires the cores to physically meet — a process governed by the dynamical evolution of the defect positions (the advection of Section 4 and the annihilation rate of Section 5).

**Why annihilation is suppressed on merger timescales.** In a Bullet-class merger, the pair forms at the collision interface and is then *separated*, not brought together. Each defect advects with its host subcluster (Section 4), and the subclusters are moving apart at ~ v_rel ~ 3000 km/s after pericenter. The pair separation grows with time; the cores move *away* from each other.

For annihilation to occur, the defects would have to overcome the subcluster separation velocity and drift back together. The probability of this is exponentially small in the separation-over-core-size ratio (computed in Section 5). For Bullet parameters (separation ~ 100s of kpc, r_core ~ 100 kpc), the annihilation timescale far exceeds the merger crossing time, the relaxation time τ_relax, and even the cosmological age. Therefore on merger and post-merger timescales, charge is effectively *exactly* conserved — annihilation does not occur.

The conclusion: throughout the entire observable Bullet event, the winding number of each defect is conserved. The monopole stays Q = +1; the antimonopole stays Q = −1; neither decays nor changes.

### 3.3 Grain-cutoff conservation (C2.2.3)

**Claim:** The substrate grain ℓ_ED regularizes the defect core and prevents topological charge from leaking out through sub-grain (UV) channels; the Bullet's ~100 kpc scale is deep in the continuum regime where the topology is rigid.

**The UV-leakage concern.** In a pure continuum field theory, a point defect has a singular core where the field energy density formally diverges. One might worry that the field could "unwind" through the singular point — that charge could leak away through arbitrarily-small-scale fluctuations at the core, violating conservation. In continuum *O*(3) models without a stabilizing term, this is related to the Derrick-instability problem discussed in D2.1 §7.3.

**The substrate grain forbids sub-grain unwinding.** ED's substrate is not a continuum below the grain scale ℓ_ED (the substrate's fundamental resolution; the Planck-scale grain, P07). The field **n**(*x*) is *not defined* at scales below ℓ_ED — there is no substrate organizational state at finer resolution. A defect cannot unwind through a sub-grain channel because there is no sub-grain structure to unwind through.

Concretely: to change the winding number of a configuration, the field must pass through a configuration where **n** is undefined over a region — a "hole" punched in the target *S²* mapping. In the continuum, this hole can be made arbitrarily small (the unwinding happens at a point). With a grain cutoff, the smallest possible hole is one grain cell, ℓ_ED across. Unwinding requires the field to reorganize coherently over a grain cell, which costs a fixed minimum action set by the grain. This action barrier is what makes the topological charge *rigid* — it cannot leak continuously; it can only change through the discrete, action-costly process of core overlap during annihilation.

**r_core ≫ ℓ_ED ensures topological stability.** From D2.1 §7.7, the monopole core radius is:

```
r_core ~ √(κ c_s² / β ρ̄_c)  ~  tens to hundreds of kpc
```

The substrate grain is:

```
ℓ_ED ~ ℓ_P ~ 10⁻³⁵ m  ~  10⁻⁵¹ kpc
```

The ratio:

```
r_core / ℓ_ED  ~  (100 kpc) / (10⁻⁵¹ kpc)  ~  10⁵³
```

The monopole core is ~53 orders of magnitude larger than the substrate grain. The defect is an enormous, smooth continuum structure on grain scales — the field varies appreciably only over ~100 kpc, while the grain is ~10⁻³⁵ m. There is no sense in which the grain-scale physics "sees" the defect as anything other than a slowly-varying background.

**The Bullet is deep in the continuum regime.** Because r_core / ℓ_ED ~ 10⁵³, the Bullet defect lives in the deep-continuum regime where the topological classification π₂(*S²*) = ℤ applies with full rigor. The discreteness of the substrate is utterly negligible at the defect scale. The topology is rigid: charge cannot leak through UV channels because the UV cutoff is 53 orders of magnitude below any scale relevant to the defect, and the action cost of any sub-grain unwinding is correspondingly astronomical.

Grain-cutoff conservation is therefore satisfied trivially and overwhelmingly. The grain *stabilizes* the defect (preventing Derrick collapse, D2.1 §7.3) and simultaneously *protects* its charge (preventing UV leakage). Both roles follow from the single fact that the substrate has a finite, fundamental resolution.

### 3.4 V5-coupling conservation (C2.2.4)

**Claim:** V5's finite-memory structure preserves topological charge during the quench; the quench term modifies the substrate's dynamics but not its topology; V5 cannot create net charge, only redistribute zero total charge into ±1 pairs.

**The V5-specific concern.** Section 9 of D2.1 established that the quench dynamics is V5-native — the quench coupling β ρ_c (**n** · **n**_eq) involves V5's commitment-density variable and outer-scale equilibrium orientation. Since this coupling is the *driver* of defect formation, one must verify it respects charge conservation. A coupling that sourced net topological charge would allow the merger to create a lone monopole, violating C2.2.1.

**The quench coupling is a rotation on S².** The quench term drives **n** toward the local equilibrium **n**_eq. Geometrically, this is a force that rotates **n** on the target sphere toward **n**_eq. Crucially, a rotation on *S²* preserves the sphere — it maps *S²* to itself bijectively and continuously. Such a map is homotopically trivial (it is connected to the identity through the rotation group SO(3), which acts on *S²*).

A homotopically-trivial deformation of the field cannot change the degree of the map **n**|_Σ. Therefore the quench coupling, however violently it drives the field during the merger, cannot change the topological charge enclosed by any surface that does not pass through a defect core. The quench changes *where* the field points and *how fast* it moves, but not *how many times* it wraps the target.

**V5's finite memory preserves charge.** V5's substrate carries finite memory (P06): the organizational state at any event is constrained by the accumulated record of prior commitments. During the quench, the finite-memory structure means the field cannot "forget" its prior topological configuration and spontaneously rearrange to a different total charge. The accumulated commitment record carries the topological information forward continuously. Finite memory is, in this sense, the dynamical substrate-level mechanism that *enforces* the mathematical identity of Section 3.1: the substrate physically remembers its winding, commitment by commitment.

**V5 redistributes, it does not create.** What the V5 quench *does* do is take the zero-total-charge initial configuration and redistribute it into localized structures. Before the quench, the zero charge is spread smoothly (no defects, Q = 0 everywhere). After the quench, the same zero total charge is concentrated into a +1 monopole and a −1 antimonopole — still summing to zero, but now localized rather than diffuse.

This is precisely analogous to pair production in QED: an energetic process does not create net electric charge; it converts energy into a particle-antiparticle pair of zero net charge. The V5 quench does not create net topological charge; it converts merger kinetic energy into a monopole-antimonopole pair of zero net winding. In both cases, the conservation law is exact and the "creation" is really a redistribution of a conserved quantity that started (and remains) at zero.

V5-coupling conservation is therefore satisfied: the quench drives the dynamics and localizes the charge into a pair, but the net topological charge is conserved at zero throughout, enforced both mathematically (rotation on *S²* is homotopically trivial) and dynamically (finite memory carries the winding forward).

### 3.5 Consolidated conservation result

The four verifications:

| Condition | Verification | Result |
|---|---|---|
| C2.2.1 — Identical conservation | ∂_μ J^μ = 0 by antisymmetry; pre-merger Q = 0; post-merger Q_+ + Q_- = 0 | ✓ Forces pair production |
| C2.2.2 — EOM conservation | Quench/strain couplings preserve *S²*; charge changes only via core overlap; annihilation suppressed | ✓ Charge conserved on merger timescales |
| C2.2.3 — Grain-cutoff conservation | r_core / ℓ_ED ~ 10⁵³; deep continuum regime; UV leakage forbidden by grain | ✓ Topology rigid |
| C2.2.4 — V5-coupling conservation | Quench is rotation on *S²* (homotopically trivial); finite memory carries winding; redistributes not creates | ✓ V5 conserves net charge |

**All four conservation conditions are satisfied.** The winding number Q is a rigorous conserved invariant of the substrate's organizational state — conserved as a mathematical identity (C2.2.1), preserved by the equations of motion away from cores (C2.2.2), protected against UV leakage by the substrate grain (C2.2.3), and respected by the V5 quench dynamics that drives defect formation (C2.2.4).

**Structural consequence — Bullet-class mergers must produce monopole-antimonopole pairs.** The combination of the four results establishes a forced structural conclusion:

> A Bullet-class merger of two cluster-scale organizational fields, beginning from a defect-free (Q = 0) configuration, and producing defects via the V5 Kibble quench, *must* produce those defects as monopole-antimonopole pairs of total charge zero.

The "must" is the strength of a conservation law. It is not an assumption fitted to the Bullet observations; it is a forced consequence of topological charge conservation applied to a merger that produces defects. Given that defects form (D2.1 §8), conservation requires them to form in charge-zero pairs. Given that each pair member carries a localized gravitational signature (D2.1 §7.7), the observable consequence is two offset lensing peaks of equal magnitude and opposite topological charge.

The Bullet Cluster's two-peak structure is, under this mechanism, the visible manifestation of a conservation law. This is the strongest form of structural prediction the arc can make: not "the model can accommodate two peaks" but "conservation forces exactly two peaks, of opposite charge, summing to zero."

### 3.6 Implications for Section 4 — Advection of Pairs with Subcluster Flow

Section 3 established that the monopole-antimonopole pair, once formed, carries conserved topological charges (+1 and −1) that cannot change except through mutual annihilation — which Section 3.2 argued is dynamically suppressed in the separating post-merger geometry. This sets up Section 4's task.

Section 4 must derive *how the pair members move* after formation. The key questions:

1. **The advection equation.** Each defect drifts with the substrate's organizational flow. Section 4 must derive the equation of motion for the defect position **r**(*t*) in terms of the substrate's organizational propagation speed c_s, the local **n**_eq gradient, and the gravitational drift of the host subcluster.

2. **Which subcluster does each defect follow?** Section 3.1 established that the pair forms with one member preserving **n**_eq^A and the other preserving **n**_eq^B. Section 4 must show that the monopole drifts with subcluster A's collisionless galaxies while the antimonopole drifts with subcluster B's — explaining why each lensing peak co-locates with its subcluster's galaxies, not with the displaced gas.

3. **The separation trajectory.** Section 4 must derive the pair separation as a function of time, confirming that the separation grows (or remains large) after pericenter — which Section 3.2 *assumed* in arguing that annihilation is suppressed. Section 4 verifies the assumption.

4. **Setting up the offset prediction.** The pair separation at the time of observation, combined with the gas displacement, determines the observed offset between lensing peak and gas peak. Section 4 produces the separation; Section 5's annihilation analysis confirms the pair survives to the observation epoch; together they ground the offset prediction (D2.1 §8.6, falsifier F1).

With the advection equation in hand, Section 5 will compute the annihilation rate (verifying the suppression assumed in Section 3.2), and Section 6 will compute the decoherence rate. The conservation result of Section 3 is the foundation: because charge is conserved, the pair members are stable objects whose *positions* — not their charges — are what evolve. Section 4 tracks those positions.

---

*End of Section 3. All four conservation conditions verified; pair production is forced. Section 4 below derives the advection of the pair members with subcluster flow.*

---

## 4. Advection of Pairs with Subcluster Flow

### 4.0 Goal

Section 3 established that the merger produces a monopole-antimonopole pair (Q = +1 and Q = −1) of conserved charge, and that the pair can only be destroyed by mutual annihilation, which is suppressed if the pair separates after formation. This section derives the **advection equation** governing the motion of the two defect cores after their formation at the merger interface, determines which subcluster each defect follows, solves for the pair separation as a function of time, and verifies explicitly the separation assumption that Section 3.2 invoked.

The defects are treated as point-like topological charges (justified by r_core ≪ R_subcluster: the ~100 kpc core is small compared to the ~Mpc subcluster scale, so the defect can be approximated as a point carrying winding number Q). The method is the standard **collective-coordinate** approach: the defect's position is promoted to a dynamical degree of freedom, and its equation of motion is derived from the field Lagrangian by integrating out the field profile around the moving core.

### 4.1 Advection equation

**Collective-coordinate setup.** Let **X**(*t*) be the position of a defect core. The field around the core is approximately the hedgehog profile (D2.1 §7.7) centered on **X**(*t*):

```
n(x, t)  ≈  n_hedgehog(x − X(t))   [rotated to match the local n_eq]
```

The time-dependence of the field comes entirely from the motion of the center **X**(*t*) plus slow adjustments of the profile. Substituting this ansatz into the field Lagrangian (D2.1 §7.4.1) and integrating over the field profile yields an effective Lagrangian for the collective coordinate **X**(*t*).

**The effective equation of motion.** Carrying out the standard collective-coordinate reduction for the *S²* sigma model with the V5 quench coupling gives, to leading order:

```
M_core Ẍ  =  −η (Ẋ − v_flow)  +  F_quench  +  F_pair
```

Where:

- **M_core** is the defect's effective inertial mass (~ E_mono / c_s², from D2.1 §7.7's monopole energy)
- **η** is the substrate's organizational drag coefficient (resistance of the substrate to defect motion relative to the local organizational flow)
- **v_flow(x)** is the local advection velocity of the substrate's organizational field
- **F_quench** is the force from the quench coupling driving the defect toward regions where its winding matches the local **n**_eq
- **F_pair** is the inter-defect force between the monopole and antimonopole (attractive; analyzed in Section 5)

**The overdamped (advection-dominated) limit.** For cluster-scale defects, the substrate's organizational drag dominates the inertial term: the defect's relaxation time M_core/η is short compared to the merger timescale. In this overdamped regime, the inertial term M_core Ẍ is negligible, and the equation reduces to:

```
η (Ẋ − v_flow)  ≈  F_quench  +  F_pair
```

Solving for the defect velocity:

```
Ẋ  ≈  v_flow  +  (F_quench + F_pair) / η
```

To leading order, **the defect moves with the local organizational flow v_flow**, with corrections from the quench force (which keeps the defect aligned with its subcluster's orientation) and the inter-defect pair force (which is sub-dominant for large separations; Section 5). The motion is **advection-dominated**:

```
Ẋ  ≈  v_flow(X)     [leading order]
```

**The flow field from post-pericenter geometry.** After pericenter, the two subclusters are moving apart. The substrate's organizational field is dragged along with the gravitational flow of each subcluster — the channels reorganize to track the moving mass concentrations. The flow field v_flow(x) is therefore approximately the local bulk velocity of the substrate's organizational structure, which tracks the subcluster motion:

```
v_flow(x)  ≈  { +v_A,   in the region dominated by subcluster A's organizational field
             { +v_B,   in the region dominated by subcluster B's organizational field
```

Where **v**_A and **v**_B are the post-pericenter velocities of the two subclusters (moving apart). The interface between the two flow regions is where **n**_eq^A and **n**_eq^B meet — precisely where the pair was formed.

A defect sitting just on the A-side of the interface advects with **v**_A; a defect just on the B-side advects with **v**_B. Since **v**_A and **v**_B point in opposite directions (the subclusters separate), the two defects are carried apart.

### 4.2 Which subcluster each defect follows

**Claim:** The +1 defect follows subcluster A; the −1 defect follows subcluster B. The structural reason is that the quench inherits the channel-orientation field from each subcluster.

**The orientation inheritance.** At formation (D2.1 §7.8), the monopole-antimonopole pair forms at the interface where **n**_eq^A and **n**_eq^B meet. The winding of each defect is determined by *which way* the field rotates as one moves from the defect outward into the surrounding region.

Consider the +1 monopole. Its hedgehog structure means **n** points radially outward from the core, matching the surrounding field at large radius. For the monopole to smoothly connect to subcluster A's organizational field, its outer profile must approach **n**_eq^A in the A-direction. The monopole's winding is "anchored" to **n**_eq^A: the field configuration that surrounds the monopole and connects it to the bulk is the A-subcluster's orientation.

Symmetrically, the −1 antimonopole's outer profile connects to **n**_eq^B. Its winding is anchored to subcluster B's orientation.

**Why this fixes the advection.** The quench force F_quench drives each defect toward the region where its winding matches the local **n**_eq (it is energetically costly for a defect anchored to **n**_eq^A to sit in a region dominated by **n**_eq^B, because the field would have to strain to connect the mismatched orientations). The monopole, anchored to **n**_eq^A, is therefore driven to remain in the A-dominated region; the antimonopole, anchored to **n**_eq^B, remains in the B-dominated region.

Combined with the advection result of Section 4.1 (each region moves with its subcluster), the conclusion follows:

- The **+1 monopole** stays in the A-region and advects with **v**_A → it tracks subcluster A's collisionless galaxies
- The **−1 antimonopole** stays in the B-region and advects with **v**_B → it tracks subcluster B's collisionless galaxies

**Why the defects track galaxies, not gas.** The collisionless galaxies of each subcluster carry the pre-merger organizational orientation forward through the merger — they pass through the collision unimpeded (D2.1 §7.8) and remain associated with their subcluster's **n**_eq. The gas, by contrast, is ram-pressure-stripped and mechanically decoupled from the organizational field; it lags behind at the collision interface. The defects, anchored to the organizational orientations **n**_eq^A and **n**_eq^B, follow those orientations — which travel with the galaxies, not the gas.

This is the structural origin of the Bullet's defining feature: the lensing peaks (at the defects) co-locate with the galaxies, while the X-ray gas is displaced. The defect tracks the orientation; the orientation tracks the collisionless matter; the gas is left behind.

### 4.3 Separation trajectory

**Solving the advection equation for the relative coordinate.** Define the pair separation **Δr**(*t*) = **X**_+(*t*) − **X**_−(*t*). From Section 4.1, each defect advects with its subcluster velocity:

```
Ẋ_+  ≈  v_A
Ẋ_-  ≈  v_B
```

The relative velocity:

```
Δṙ  =  Ẋ_+ − Ẋ_-  ≈  v_A − v_B  =  v_rel
```

Where **v**_rel = **v**_A − **v**_B is the relative velocity of the two subclusters (the merger velocity). Integrating from the time of pericenter (t = 0, where the pair forms at separation ~ r_core ≈ 0 on cluster scales):

```
Δr(t_post)  ≈  Δr(0)  +  v_rel × t_post  ≈  v_rel × t_post
```

To leading order, **the pair separation grows linearly with post-pericenter time at the merger velocity**:

```
Δr(t_post)  ≈  v_rel × t_post
```

**Connection to the offset law of D2.1 §8.6.** D2.1 §8.6 predicted the offset between the lensing peak and the gas peak. The defect positions are the lensing peaks; the gas position is set by ram-pressure hydrodynamics. The two have related but distinct displacements:

- The defects (lensing peaks) separate at Δr_defect ≈ v_rel × t_post (this section)
- The gas, slowed by ram pressure, lags behind the collisionless components, displaced by Δr_gas relative to its parent subcluster's galaxies

The observed offset between a given subcluster's lensing peak and the gas peak is the difference between the defect position (tracking the galaxies) and the gas position (lagging). For each subcluster:

```
Δr_offset  ≈  (defect position − gas position)  ≈  v_rel × t_post × (1 − f_gas-drag)
```

Where f_gas-drag accounts for the fraction of the motion the gas retains before stalling. The leading scaling — **Δr_offset ∝ v_rel × t_post** — matches D2.1 §8.6's predicted offset law and supports falsifier F1 (offset scales with merger velocity). Section 4 thus derives the kinematic foundation of the offset prediction from the advection dynamics.

### 4.4 Verification of the assumption in Section 3.2

Section 3.2 *assumed* that the pair separates rather than annihilates, in arguing that charge is conserved on merger timescales. Section 4.3 now *verifies* this assumption explicitly.

**The pair separates.** From Section 4.3, Δr(t_post) ≈ v_rel × t_post grows monotonically with time. The defects move apart at the merger velocity. For the Bullet (v_rel ~ 3000 km/s, t_post ~ 0.15 Gyr since pericenter):

```
Δr(Bullet)  ≈  3000 km/s × 0.15 Gyr  ≈  460 kpc
```

— consistent with the observed ~700 kpc total separation between the Bullet's two lensing peaks (the factor-of-2 difference is within the order-of-magnitude precision and the geometric projection effects). The pair is separating, not converging.

**The flow field is repulsive in configuration space.** In the relative coordinate **Δr**, the advection dynamics gives Δṙ ≈ v_rel — a constant outward velocity. In configuration space (the space of pair separations), the trajectory moves monotonically away from Δr = 0 (the annihilation point). The advection acts as an effective *repulsion*: the subcluster flow carries the defects apart faster than the attractive inter-defect force F_pair can bring them together.

Quantitatively, the inter-defect attractive force F_pair (Section 5) scales as ~ 1/Δr² (a Coulomb-like attraction between opposite topological charges in the *S²* sigma model). The advection drift velocity is v_rel. The defects separate as long as the advection dominates the attraction:

```
v_rel  >  (F_pair / η)  ~  (constant / Δr²) / η
```

At formation (Δr small), the attraction is strongest, but the advection imparts the full v_rel ~ 3000 km/s immediately as the subclusters separate. As Δr grows, the attraction weakens as 1/Δr², so advection dominates increasingly. Once the pair has separated to ~ r_core, the attraction is negligible and the separation is locked in by the receding subclusters.

**The condition under which annihilation is dynamically forbidden.** Annihilation requires the pair to return to Δr ≲ r_core. This is forbidden when the advection-imparted separation velocity exceeds the maximum attractive recombination velocity at all separations beyond formation:

```
v_rel  >  v_attract^max  ≈  √(F_pair(r_core) × r_core / M_core)
```

For Bullet parameters, v_rel ~ 3000 km/s vastly exceeds the attractive recombination velocity (which is of order the substrate organizational propagation speed times a small coupling factor). The condition is satisfied with large margin: **the pair cannot annihilate because the merger carries the defects apart far faster than they can attract back together.**

This confirms the Section 3.2 assumption. Annihilation is dynamically forbidden for any supercritical merger (v_rel > v_crit), and Bullet-class mergers are deeply supercritical (v_rel ~ 10 × v_crit, from D2.1 §8.6). The pair survives.

### 4.5 Consolidated result

**Advection dynamics summary.** The monopole-antimonopole pair, formed at the merger interface, evolves by advection with the subcluster flow:

- Each defect advects with its host subcluster's organizational flow (Section 4.1): Ẋ ≈ v_flow, overdamped/advection-dominated
- The +1 monopole follows subcluster A; the −1 antimonopole follows subcluster B (Section 4.2), because the quench anchors each defect's winding to its subcluster's orientation
- The defects track the collisionless galaxies (which carry the orientation), not the ram-stripped gas
- The pair separation grows linearly: Δr(t) ≈ v_rel × t_post (Section 4.3)
- The pair separates rather than annihilates; annihilation is dynamically forbidden for supercritical mergers (Section 4.4)

**Structural consequence.** A Bullet-class merger produces two defects of opposite topological charge that separate along the outgoing subcluster trajectories, each defect co-located with its subcluster's collisionless galaxies, with a separation growing at the merger velocity. The two lensing peaks of the Bullet are these two separating defects; their offset from the gas is the consequence of the defects tracking the orientation-carrying galaxies while the gas is mechanically left behind.

This completes the kinematic picture: Section 3 established that the pair *must* form (conservation); Section 4 establishes that the pair *separates* (advection); together they predict two lensing peaks, co-located with galaxies, offset from gas, with separation scaling as v_rel × t_post.

### 4.6 Implications for Section 5 — Annihilation Channels

Section 4 derived the advection dynamics and showed that the pair separates with the outgoing subclusters. Section 4.4 argued that annihilation is dynamically forbidden for supercritical mergers, but the argument was kinematic — it showed the advection carries the defects apart faster than they can recombine. Section 5 must make the annihilation analysis *quantitative*.

Three tasks propagate to Section 5:

1. **Compute the inter-defect force F_pair explicitly.** Section 4 used F_pair ~ 1/Δr² as a scaling estimate. Section 5 must derive the precise force law between a +1 monopole and a −1 antimonopole in the substrate's *S²* sigma model with the V5 quench coupling, including any screening from the commitment-density background.

2. **Compute the annihilation rate Γ_ann.** Even with the pair separating on average, there could be a small probability of annihilation through fluctuations that bring the cores together. Section 5 must compute Γ_ann as a function of separation Δr, relative velocity, and substrate parameters, and verify Γ_ann is exponentially suppressed for Bullet-class separations.

3. **Verify the annihilation timescale exceeds all relevant timescales.** Section 5 must confirm 1/Γ_ann ≫ τ_relax, the merger crossing time, and the cosmological age — establishing that annihilation does not limit the pair lifetime. This validates the Section 1.3 Phase-B claim that annihilation gives 1/Γ_ann > 10¹⁰ years and is not lifetime-limiting.

The advection result of Section 4 is the input: because the pair separates to ~ hundreds of kpc and stays separated, the annihilation rate evaluated at that separation is what determines whether the pair can survive. Section 5 computes that rate. Section 6 will then address the remaining decay channel (decoherence), and Section 7 will close D2.2 with the combined pair-lifetime result and hand-off to D2.3.

---

*End of Section 4. The pair separates with the outgoing subclusters; annihilation is kinematically forbidden for supercritical mergers. Section 5 below quantifies the annihilation rate.*

---

## 5. Annihilation Channels

### 5.0 Goal

Section 4 established kinematically that the monopole-antimonopole pair separates after formation, and argued that annihilation is dynamically forbidden for supercritical mergers. This section makes that argument **quantitative**: it derives the effective interaction force between the two defects, combines it with the advection dynamics to determine when annihilation is dynamically allowed, computes the annihilation rate Γ_ann, and compares the annihilation timescale 1/Γ_ann to all other relevant timescales.

The conclusion to be established: for Bullet-class mergers, 1/Γ_ann exceeds every relevant timescale (advection, relaxation, post-pericenter, and cosmological age) by many orders of magnitude. Annihilation does not limit the pair lifetime. This validates the Section 1.3 Phase-B claim and supports the Section 10 (D2.1) steady-state defect-density calculation.

### 5.1 Force law between defects

**The gradient-energy origin of the interaction.** Two defects of opposite topological charge interact through the gradient energy of the field configuration that connects them. From the Lagrangian (D2.1 §7.4.1), the relevant energy is the gradient term:

```
E_grad  =  (κ c_s² / 2) ∫ (∇n)² d³x
```

When a +1 monopole and a −1 antimonopole are present, the field **n**(*x*) must interpolate between the two hedgehog cores. The total gradient energy depends on their separation Δr: bringing them closer reduces the volume over which the field strains, lowering the energy; pulling them apart increases it. The force is the negative gradient of this energy with respect to separation.

**Large-separation behavior — F_pair ∝ 1/Δr².** At separations large compared to the core size (Δr ≫ r_core), each defect appears point-like to the other, and the field between them is approximately a superposition of the two hedgehog tails. The hedgehog field falls off as **n** deviation ~ 1/r from each core (the standard *S²* sigma-model monopole tail). The gradient energy of the combined configuration, computed as a function of separation, gives an interaction energy:

```
E_int(Δr)  ~  − (C κ c_s²) / Δr        [large Δr]
```

Where C is a dimensionless constant of order unity from the angular integration. The interaction energy is *negative* (attractive — opposite charges lower their energy by approaching) and scales as −1/Δr, Coulomb-like. The force is:

```
F_pair  =  − dE_int/dΔr  ~  − (C κ c_s²) / Δr²        [attractive, large Δr]
```

This confirms the F_pair ∝ 1/Δr² scaling used in Section 4. The interaction is Coulomb-like: opposite topological charges in the *S²* sigma model attract with an inverse-square force, exactly analogous to opposite electric charges. (The analogy is structural: in both cases the field mediating the interaction is a long-range gradient field, and the topological/electric charge sources it.)

**Small-separation behavior — core regularization.** As Δr → r_core, the point-like approximation breaks down. The two cores begin to overlap, and the field can "short-circuit" between them — the winding from one core directly cancels the anti-winding of the other through the overlap region. In this regime, the interaction energy saturates rather than diverging:

```
E_int(Δr)  →  − E_core-overlap        [Δr ≲ r_core]
```

The force smoothly turns over from the 1/Δr² Coulomb form at large separation to a finite maximum at Δr ~ r_core, then drives rapid annihilation once the cores fully overlap (Δr ≲ ℓ_ED-regularized core scale). The core regularization (D2.1 §7.3, the grain stabilizer) ensures the force is finite at all separations; there is no true singularity.

The physical picture: at large separations, a weak Coulomb-like attraction; at separations approaching r_core, a stronger but still finite pull; at full core overlap, annihilation. The key scale separating "can attract back" from "locked apart" is r_core ~ 100 kpc.

### 5.2 Competing effects: attraction vs. advection

**Combining the force law with advection.** From Section 4.1, the overdamped equation of motion for the relative separation, including both the advection drift and the inter-defect force, is:

```
η Δṙ  =  η v_rel  +  F_pair(Δr)
```

Substituting the large-separation force law:

```
Δṙ  =  v_rel  −  (C κ c_s²) / (η Δr²)
```

The first term (advection) drives the separation outward at the merger velocity. The second term (attraction) drives it inward. The competition between them determines whether the pair separates or recombines.

**The condition for annihilation to be dynamically allowed.** Annihilation requires the separation to *decrease* — Δṙ < 0:

```
v_rel  <  (C κ c_s²) / (η Δr²)
```

Rearranging, annihilation is allowed only when:

```
Δr  <  Δr_capture  ≡  √( C κ c_s² / (η v_rel) )
```

This defines a **capture radius** Δr_capture: if the pair separation is smaller than Δr_capture, the attraction wins and the pair recombines; if larger, the advection wins and the pair separates irreversibly.

**Evaluating for Bullet-class parameters.** The capture radius depends on substrate parameters (κ, c_s, η, the same VALUE-INHERITED constants D2.3 will pin down). Using the dimensional relations from D2.1 §8.3 (κ ~ M_P²·(c/c_s), and the drag η ~ κ c_s / r_core from the collective-coordinate reduction):

```
Δr_capture  ~  √( κ c_s² / (η v_rel) )
            ~  √( κ c_s² r_core / (κ c_s v_rel) )
            ~  √( c_s r_core / v_rel )
            ~  r_core × √(c_s / v_rel)
```

For the Bullet: the organizational propagation speed c_s ≤ c is the relevant scale, but the *effective* recombination velocity (the speed at which attraction can pull the pair together) is set by the substrate dynamics, not c itself. Taking the conservative estimate where the attraction's characteristic velocity is of order the substrate organizational speed times a coupling factor, and v_rel ~ 3000 km/s:

```
Δr_capture(Bullet)  ~  r_core × √(v_attract / v_rel)  ≪  r_core
```

Because v_rel ≫ v_attract (the merger velocity vastly exceeds the recombination velocity for a supercritical merger), Δr_capture is *smaller* than r_core. But the pair forms at separation ~ r_core and immediately begins separating at v_rel. The pair separation exceeds Δr_capture essentially from the moment of formation.

**The conclusion:** the pair never satisfies the annihilation condition Δr < Δr_capture after formation, because the advection carries it outward past Δr_capture immediately. The capture radius is smaller than the formation separation; the pair starts outside the capture region and moves further out. Annihilation is dynamically forbidden from the outset.

### 5.3 Annihilation rate Γ_ann

Even though the *average* trajectory separates, one should ask whether *fluctuations* could bring the cores back together — a statistical annihilation rate. We compute Γ_ann using the standard rate expression.

**The rate expression.** The annihilation rate for a pair is:

```
Γ_ann  =  n_eff × σ_ann × v_thermal
```

Where n_eff is the effective probability density of the antimonopole at the monopole's location, σ_ann ~ r_core² is the annihilation cross-section (the cores must overlap to annihilate), and v_thermal is the velocity dispersion of the defect positions about their advected trajectories (from substrate fluctuations).

**Exponential suppression at large separation.** The probability that fluctuations bring the cores from separation Δr back to overlap (Δr ≲ r_core) against the advective outward drift is governed by a competition between fluctuation-driven diffusion and deterministic advection. This is a classic Kramers escape / barrier-crossing problem in reverse: the pair must climb "uphill" against the advection to annihilate. The probability is exponentially suppressed:

```
Γ_ann  ~  Γ_0 × exp( − Δr / Δr_capture )       [Δr ≫ Δr_capture]
```

Where Γ_0 is a microscopic attempt frequency (~ c_s / r_core). The exponential suppression factor exp(−Δr/Δr_capture) reflects the improbability of a fluctuation large enough to overcome the advective separation.

**Order-of-magnitude estimate for the Bullet.** With Δr ~ 460 kpc (Section 4.4), r_core ~ 100 kpc, and Δr_capture ≪ r_core (Section 5.2):

```
Δr / Δr_capture  ~  460 kpc / (≪ 100 kpc)  ≳  10
```

The exponential suppression is therefore at least exp(−10) ~ 5 × 10⁻⁵, and plausibly far smaller (exp(−50) or beyond) depending on the precise value of Δr_capture, which D2.3 will tighten. The attempt frequency Γ_0 ~ c_s/r_core ~ (10⁵ km/s)/(100 kpc) ~ 1/Gyr (taking c_s of order a fraction of c). Therefore:

```
Γ_ann(Bullet)  ~  (1/Gyr) × exp(−10 to −50)  ~  10⁻⁵ to 10⁻²² /Gyr
```

The annihilation timescale:

```
1/Γ_ann(Bullet)  ~  10⁵ to 10²² Gyr
```

Even at the most conservative end of the estimate (1/Γ_ann ~ 10⁵ Gyr), this is far longer than the age of the universe (~14 Gyr). Annihilation does not occur within cosmic history for a Bullet-class pair.

### 5.4 Lifetime comparison

We compare the annihilation timescale to the other relevant timescales:

| Timescale | Value | Source |
|---|---|---|
| t_advect (advection phase) | ~ 10⁸ years (0.1 Gyr) | Section 1.3, Section 4 |
| t_post (post-pericenter elapsed time, Bullet) | ~ 1.5 × 10⁸ years (0.15 Gyr) | Markevitch et al. observations |
| τ_relax (substrate organizational relaxation) | ~ 10⁸–10⁹ years (0.1–1 Gyr) | D2.1 §8.3 estimate; D2.3 will pin down |
| t_Hubble (age of universe) | ~ 1.4 × 10¹⁰ years (14 Gyr) | Cosmological |
| **1/Γ_ann (annihilation)** | **~ 10⁵–10²² Gyr** | **Section 5.3** |

The hierarchy:

```
t_advect ~ t_post ~ τ_relax ≪ t_Hubble ≪ 1/Γ_ann
```

The annihilation timescale exceeds *every* other relevant timescale by, at minimum, four orders of magnitude (compared to the Hubble time) and at maximum more than twenty orders of magnitude. **Annihilation is the slowest process in the problem by an enormous margin.**

In particular, 1/Γ_ann ≫ τ_relax. This is the crucial inequality for the pair-lifetime argument: the pair's existence is *not* limited by annihilation. Whatever ends the defect's life (and Section 6 will argue it is decoherence/relaxation, not annihilation), it happens on the τ_relax timescale, long before the pair could ever annihilate.

### 5.5 Consolidated result

**The force law.** Opposite topological charges in the substrate's *S²* sigma model attract with a Coulomb-like force F_pair ∝ 1/Δr² at large separation, regularized to a finite maximum at Δr ~ r_core by the substrate grain (Section 5.1).

**The competition.** The advection drift (v_rel outward) competes with the attraction (inward). Annihilation requires Δr < Δr_capture, where the capture radius Δr_capture ~ r_core × √(v_attract/v_rel) is smaller than r_core for supercritical mergers. The pair forms outside the capture radius and advects further out; annihilation is dynamically forbidden from formation (Section 5.2).

**The rate.** The statistical annihilation rate, accounting for fluctuations attempting to overcome the advective separation, is exponentially suppressed: Γ_ann ~ Γ_0 exp(−Δr/Δr_capture), giving 1/Γ_ann ~ 10⁵–10²² Gyr for the Bullet (Section 5.3).

**The comparison.** 1/Γ_ann exceeds t_advect, t_post, τ_relax, and even t_Hubble by at least four and up to twenty-plus orders of magnitude (Section 5.4).

**Structural conclusion:** *Annihilation is dynamically forbidden for Bullet-class mergers.* The monopole-antimonopole pair, once formed and separated by the merger, cannot recombine within cosmic history. The pair lifetime is therefore *not* set by annihilation. This confirms the Section 1.3 Phase-B claim (1/Γ_ann > 10¹⁰ years; annihilation not lifetime-limiting) and validates the Section 10 (D2.1) cosmological-rate calculation, which assumed the pair survives from formation to observation.

The defect's eventual fate must therefore be the *other* decay channel: decoherence/dissolution of the topological structure through environmental coupling, which Section 6 addresses. The pair does not die by recombination; it can only fade by losing organizational coherence over the substrate's relaxation time.

### 5.6 Implications for Section 6 — Decoherence / Dissolution

Section 5 established that annihilation cannot end the pair's life within cosmic history. By elimination, the pair's lifetime — if finite — must be set by the remaining decay channel: **decoherence/dissolution** of the topological structure.

Three tasks propagate to Section 6:

1. **Define the decoherence mechanism for a topological defect.** Unlike annihilation (which requires the two cores to physically meet), decoherence acts on a single defect: the substrate's commitment-density background fluctuates, and these fluctuations can in principle erode the coherent winding structure of an isolated monopole. Section 6 must define precisely what "decoherence of a topological charge" means in the substrate framework — and reconcile it with the fact that Section 3 proved Q is a conserved integer (how can a conserved integer "decohere"?).

2. **Compute the decoherence rate Γ_dec.** Section 6 must compute Γ_dec as a function of the commitment-density background and substrate parameters, and determine whether decoherence acts on the topological charge itself (forbidden by Section 3's conservation) or only on the *spatial coherence* of the defect's gravitational signature (allowed, and the likely actual mechanism).

3. **Establish the pair lifetime τ_pair.** Combining Section 5's annihilation result (1/Γ_ann ≫ all timescales) with Section 6's decoherence result, Section 6 must produce the final pair lifetime τ_pair = min(1/Γ_ann, 1/Γ_dec). The expectation from Section 1.3 is that decoherence is sub-dominant to relaxation (Γ_dec · τ_relax ≪ 1), making τ_pair ~ τ_relax — i.e., the pair persists for the substrate's organizational relaxation time, then fades as the substrate's overall organizational coherence relaxes.

The resolution of the apparent tension — a conserved integer charge that nonetheless has a finite-lifetime gravitational signature — is the central conceptual content of Section 6. The likely answer: the topological charge Q is exactly conserved (Section 3), but the defect's *observable gravitational signature* depends on the coherence of the surrounding organizational field, which relaxes on τ_relax. The charge persists; the lensing signal fades as the cluster's organizational structure equilibrates. Section 6 develops this distinction and Section 7 closes D2.2 with the combined lifetime result and hand-off to D2.3.

---

*End of Section 5. Annihilation is dynamically forbidden; 1/Γ_ann exceeds all timescales by orders of magnitude. Section 6 below addresses decoherence as the remaining decay channel.*

---

## 6. Decoherence / Dissolution

### 6.0 The conceptual tension and its resolution

Sections 3 and 5 produced two results that appear, at first, to be in tension.

- **Section 3** proved that the winding number Q is an *exactly conserved integer*. It cannot change except through monopole-antimonopole annihilation.
- **Section 5** proved that annihilation is *dynamically forbidden* for Bullet-class mergers — 1/Γ_ann exceeds the age of the universe by many orders of magnitude.

Together these say: the topological charge of a Bullet defect, once formed, persists essentially forever. Yet observationally, the Bullet signature is *not* expected to persist forever. We observe a handful of Bullet-class systems at any epoch (D2.1 §10), which requires the signatures to have a finite lifetime — otherwise defects would accumulate over cosmic history and we would see far more than a handful.

**How can an exactly-conserved, annihilation-protected integer charge produce a finite-lifetime observable?**

The resolution is a distinction between three different things that the loose phrase "the defect" conflates:

1. **The topological charge Q.** An integer, strictly conserved (Section 3), annihilation-protected (Section 5). It does not decay. Once a Bullet merger produces a Q = +1 monopole, that winding number persists.

2. **The coherent organizational field surrounding the defect.** The extended configuration **n**(*x*) that gives the defect its large-scale gravitational reach. This field is *not* topologically protected — it is a smooth configuration that can relax toward the substrate's local equilibrium **n**_eq through the dissipative dynamics of the Lagrangian. It relaxes on the timescale τ_relax.

3. **The observable gravitational signature.** The weak-lensing signal we measure. This depends on the *coherent alignment* of **n**(*x*) over large (~100 kpc to Mpc) scales — not on the bare integer Q. As the coherent field relaxes, the lensing signature fades, even though Q is unchanged.

The resolution in one sentence: **the topological charge is conserved, but the coherent field that makes the charge gravitationally visible relaxes on τ_relax, so the observable signature has a finite lifetime even though Q does not.**

The defect does not disappear. Its winding number is still there, encoded in the substrate. But the extended organizational structure that lensed background galaxies has equilibrated back into the cluster's ambient organizational field, and the lensing signal is gone. The charge becomes "invisible" — topologically present, gravitationally quiet.

This section develops the distinction quantitatively.

### 6.1 What decoheres?

**The organizational-coherence field.** Surrounding the defect core is the extended field configuration **n**(*x*) that interpolates between the core (where the winding is concentrated) and the cluster's ambient organizational field at large radius. Write this as:

```
n(x)  =  n_defect(x)  +  δn(x)
```

Where **n**_defect(*x*) is the idealized hedgehog (carrying the winding) and δ**n**(*x*) captures the deviation of the actual field from the idealized profile — the "dressing" of the topological core by the surrounding coherent structure.

The **coherent organizational field** is the large-scale, smoothly-varying part of **n**(*x*) that maintains the defect's extended gravitational reach. It is coherent in the sense that **n**(*x*) is correlated over large scales — the field "knows about" the winding out to radii ~ r_core and beyond, maintaining a smooth interpolation.

**How the lensing signal depends on coherent alignment.** The weak-lensing convergence produced by the defect depends on the defect's contribution to the substrate's commitment-density distribution, which in turn depends on the gradient energy of **n**(*x*) (D2.1 §7). The gradient energy is large where **n**(*x*) varies coherently over the extended profile:

```
Σ_lensing(x)  ∝  (κ c_s² / 2) (∇n)²
```

This is largest when **n**(*x*) maintains a coherent, smoothly-winding configuration over the full ~r_core scale. The lensing signal is sourced by the *coherent gradient field*, not by the integer Q directly. A defect with Q = +1 but a relaxed, incoherent surrounding field (δ**n** large, the smooth profile washed out) produces little lensing — because the gradient energy has been dissipated even though the winding number is unchanged.

**Why Q persists even when coherence decays.** The winding number Q is computed by the surface integral (Section 2.2) over a closed surface Σ surrounding the core. This integral is a *topological* quantity — it depends only on the homotopy class of the map **n**|_Σ, not on the detailed profile. Adding a smooth perturbation δ**n**(*x*) that does not pass through a singularity cannot change the homotopy class. Therefore Q is invariant under any smooth relaxation of the surrounding field:

```
Q[n_defect + δn]  =  Q[n_defect]  =  +1     (for any smooth δn)
```

The relaxation δ**n** → (some equilibrium deviation) changes the *energy* and the *gradient structure* of the field — and therefore the lensing signal — but cannot change Q. The integer is protected by topology; the coherent profile that makes it visible is not.

This is the heart of the resolution: **Q is a topological invariant immune to smooth relaxation; the lensing signature is an energetic quantity sensitive to it.** They decouple. Q persists; the signal fades.

### 6.2 Mechanism of decoherence

**The relaxation equation for perturbations.** Consider the defect's surrounding field relaxing toward equilibrium. Write **n**(*x*, *t*) = **n**_defect(*x*) + δ**n**(*x*, *t*), and linearize the equation of motion (D2.1 §7.6) around the defect profile. The perturbation δ**n** (constrained to be tangent to *S²*, i.e. **n**_defect · δ**n** = 0) obeys:

```
∂_t² δn  −  c_s² ∇²δn  +  (β ρ_c / κ) δn  +  Γ_d ∂_t δn  =  S_defect(x)
```

Where:
- The first three terms are the Klein-Gordon-like structure from D2.1 §8.3 (kinetic, gradient, mass term from the quench coupling)
- **Γ_d ∂_t δn** is a dissipative (friction) term arising from the substrate's finite memory and commitment-density coupling — this is the new ingredient that drives relaxation
- **S_defect(x)** is a source term from the defect profile (the defect "anchors" a particular equilibrium dressing)

The dissipative term Γ_d ∂_t δn is the channel that drives δ**n** toward its equilibrium value. Without it, perturbations would oscillate indefinitely (the Klein-Gordon structure is non-dissipative). With it, perturbations *relax* — any excess coherent structure decays away, leaving the field at its equilibrium dressing of the topological core.

**The dissipative channel.** The friction Γ_d originates from the substrate's commitment-density coupling (V5) combined with finite memory (P06). Physically: as the field **n** evolves, each substrate event commits irreversibly, and the irreversibility dissipates organizational coherence — the field cannot maintain an arbitrary coherent configuration indefinitely because the substrate's commitment process continually "measures" and partially randomizes the local orientation against the ambient commitment-density background. This is the substrate-level analogue of environmental decoherence in open quantum systems: the commitment-density background is the "environment," and the defect's coherent dressing is the "system" that loses coherence to it.

**Why decoherence is governed by τ_relax.** The relaxation timescale of the dissipative equation is set by the friction coefficient and the mass term. In the overdamped regime (friction-dominated, consistent with the advection analysis of Section 4.1), the relaxation time is:

```
τ_decohere  ~  Γ_d / (β ρ_c / κ)  ~  Γ_d κ / (β ρ_c)
```

Comparing to the substrate organizational relaxation time from D2.1 §8.3 (τ_relax ~ √(κ/βρ_c)): with the friction coefficient Γ_d scaling as the substrate's natural organizational frequency (Γ_d ~ √(βρ_c/κ), the same scale that sets the mass term's oscillation frequency), the two timescales coincide:

```
τ_decohere  ~  τ_relax
```

The decoherence of the defect's coherent dressing is governed by the *same* substrate organizational relaxation time that governs all organizational-state relaxation. This is not a coincidence — decoherence *is* the relaxation of the organizational field, applied to the specific case of the field surrounding a topological defect. The defect's signature fades on the same timescale that any organizational disturbance in the substrate relaxes.

### 6.3 Decoherence rate Γ_dec

**Computing Γ_dec from the linearized dynamics.** The decoherence rate is the inverse of the relaxation time of the coherent dressing:

```
Γ_dec  =  1 / τ_decohere  ~  1 / τ_relax
```

From the linearized dissipative equation (Section 6.2), the slowest-decaying mode (the longest-wavelength perturbation of the dressing, which dominates the late-time relaxation) has decay rate:

```
Γ_dec  ~  √(β ρ_c / κ)  ~  1 / τ_relax
```

**Order-of-magnitude estimate.** Using the D2.1 §8.3 parameter estimates (β ρ_c / κ ~ (a_cluster/c)², where a_cluster is the cluster's characteristic internal gravitational acceleration):

```
Γ_dec  ~  a_cluster / c
```

For a typical cluster, a_cluster ~ 10⁻⁸ cm/s² (the gravitational acceleration at ~Mpc scales in a 10¹⁵ M☉ cluster), and c ~ 3 × 10¹⁰ cm/s:

```
Γ_dec  ~  (10⁻⁸) / (3 × 10¹⁰)  ~  3 × 10⁻¹⁹ /s  ~  1 / (10⁸–10⁹ years)
```

This gives:

```
1/Γ_dec  ~  τ_relax  ~  10⁸–10⁹ years
```

consistent with the D2.1 §8.3 estimate. The decoherence rate is set by the cluster's organizational relaxation time, which is itself set by the cluster's internal gravitational scale through the substrate parameters. The estimate is order-of-magnitude; D2.3 will tighten it by deriving κ, β, c_s from substrate primitives.

**Decoherence dominates annihilation.** Comparing the two decay channels:

```
Γ_dec  ~  1/(10⁸–10⁹ yr)        ≫        Γ_ann  ~  1/(10⁵–10²² Gyr)
```

Decoherence is faster than annihilation by at least four orders of magnitude (and up to twenty-plus). **Decoherence is the dominant decay channel for the observable signature.** The defect's lensing signal fades by organizational relaxation long before the pair could ever annihilate.

Note also that the Section 1.3 claim "Γ_dec · τ_relax ≪ 1" requires reinterpretation: since Γ_dec ~ 1/τ_relax, we have Γ_dec · τ_relax ~ 1, not ≪ 1. The Section 1.3 anticipation was imprecise. The corrected statement: decoherence acts *on* the τ_relax timescale (not much slower than it), which is exactly what makes τ_relax the observable lifetime. We correct this below.

### 6.4 Observable lifetime of the Bullet signature

**Defining the pair lifetime.** The observable lifetime of the Bullet signature is the shorter of the two decay timescales:

```
τ_pair  =  min(1/Γ_ann, 1/Γ_dec)
```

From Section 5, 1/Γ_ann ~ 10⁵–10²² Gyr. From Section 6.3, 1/Γ_dec ~ τ_relax ~ 0.1–1 Gyr. The minimum is overwhelmingly set by decoherence:

```
τ_pair  =  min(10⁵–10²² Gyr,  0.1–1 Gyr)  =  0.1–1 Gyr  ≈  τ_relax
```

**τ_pair ≈ τ_relax because annihilation is negligible.** Since annihilation is forbidden (Section 5), the only thing that ends the observable signature is decoherence, which acts on τ_relax. Therefore:

```
τ_pair  ≈  τ_relax  ~  10⁸–10⁹ years
```

This is the observable lifetime of a Bullet-class lensing signature: of order the cluster's organizational relaxation time, ~0.1–1 Gyr.

**How a conserved charge produces a finite observational window.** The picture is now complete and self-consistent:

1. **At formation:** the merger produces a Q = +1 / Q = −1 pair with a coherent extended organizational dressing. The dressing sources a strong lensing signal. The signature is bright.

2. **During the observational window (~τ_relax):** the pair separates (Section 4), the cores carry their conserved charges (Section 3), annihilation does not occur (Section 5), and the coherent dressing is still largely intact. The lensing signal is strong and offset from the gas. *This is when we observe a Bullet.*

3. **After ~τ_relax:** the coherent dressing relaxes toward the cluster's ambient organizational equilibrium (Section 6.2). The gradient energy that sourced the lensing signal dissipates. The lensing signature fades. The integer charge Q is *still there* — topologically conserved — but it is no longer gravitationally visible. The system stops looking like a Bullet.

The finite observational window (~τ_relax) emerges naturally: it is the time during which the coherent dressing remains intact, after which the charge persists but goes quiet. The conserved integer and the finite-lifetime signature are reconciled — they describe different aspects of the defect, decoupled by the topological invariance of Q under smooth relaxation.

The Bullet we observe is a defect *caught within its coherence window* — a recent merger (~0.15 Gyr post-pericenter, well within τ_relax ~ 0.1–1 Gyr) whose organizational dressing is still bright. Older mergers, beyond their coherence window, have conserved charges but no visible signature; they are not counted as Bullet-class systems because they no longer lens.

### 6.5 Consolidated result

**The three-way distinction, resolved.** The apparent tension between conserved charge and finite signature is resolved by distinguishing:

| Quantity | Behavior | Timescale |
|---|---|---|
| Topological charge Q | Strictly conserved (Section 3); annihilation-protected (Section 5) | ∞ (within cosmic history) |
| Coherent organizational dressing | Relaxes toward equilibrium via dissipative dynamics (Section 6.2) | τ_relax |
| Observable lensing signature | Sourced by coherent gradient energy; fades as dressing relaxes (Section 6.1) | τ_relax |

**Structural conclusion:** *The defect persists topologically but its observable signature fades on τ_relax.* The winding number Q is an exactly conserved integer that, once created by a Bullet merger, remains in the substrate indefinitely. But the extended coherent field that makes Q gravitationally visible relaxes toward the cluster's ambient organizational equilibrium on the substrate relaxation time τ_relax ~ 10⁸–10⁹ years. The Bullet signature therefore has a finite observational lifetime τ_pair ≈ τ_relax, set by decoherence (not annihilation, which is forbidden).

This validates the D2.1 §10 cosmological-rate calculation, which assumed active-defect lifetime ~ τ_relax. The steady-state defect population is set by the formation rate times τ_relax (Section 10's n_active = R_defect × τ_relax), and this section confirms that τ_relax is indeed the correct lifetime — because annihilation is negligible and decoherence acts precisely on τ_relax.

The combined D2.2 picture, Sections 3 through 6: a Bullet merger produces a conserved monopole-antimonopole pair (Section 3); the pair separates with the outgoing subclusters and tracks the galaxies (Section 4); annihilation cannot recombine them within cosmic history (Section 5); the observable lensing signature fades by organizational decoherence on τ_relax while the conserved charge persists invisibly (Section 6). Every dynamical phase identified in Section 1.3 is now derived.

### 6.6 Implications for Section 7 — Hand-off to D2.3 and Synthesis

Sections 2 through 6 have established the complete dynamical picture of the winding number and its associated defect pair. Section 7 closes D2.2 by summarizing the results, stating explicitly what D2.3 must deliver to make the picture quantitative, and handing off to the Phase-2 synthesis paper.

Three items propagate to Section 7 and onward to D2.3:

1. **τ_relax is the master quantity.** Every timescale in D2.2 — the advection time, the decoherence rate, the observable lifetime — reduces to τ_relax. D2.3's central deliverable is the derivation of τ_relax from substrate primitives (κ, c_s, β, γ). Once D2.3 fixes τ_relax, every D2.2 lifetime becomes a number.

2. **The substrate parameters (κ, c_s, β, γ, η) appear throughout D2.2.** Section 5's capture radius, Section 6's decoherence rate, and Section 4's advection drag all depend on these constants. D2.3 must supply their values (or their substrate-primitive expressions), at which point D2.2's order-of-magnitude estimates become tight predictions.

3. **The conserved-charge / finite-signature distinction must propagate to the synthesis paper.** The Phase-2 synthesis (`Paper_ED_Bullet_TopologicalDefect.md`) must carry this distinction carefully, because it is the conceptual key to the whole arc: the Bullet is a *topologically conserved* structure with a *finite observable lifetime*, and conflating the two would misrepresent the prediction. The synthesis must state clearly that ED predicts conserved charges with relaxation-limited signatures.

Section 7 will consolidate the D2.2 deliverable, state the D2.3 mandate precisely, and confirm that D2.2's structural commitments (winding number definition, conservation, pair evolution, lifetime) are all met. With D2.2 and D2.3 complete, the Phase-2 synthesis can integrate the full topological-defect mechanism.

---

*End of Section 6. The conserved charge persists; the observable signature fades on τ_relax. Section 7 below closes D2.2 and hands off to D2.3.*

---

## 7. Hand-off to D2.3 and the Synthesis Paper

### 7.0 Summary of what D2.2 has established

D2.2 set out to define the topological charge of the *S²* defects identified in D2.1, verify its conservation, and derive the post-formation evolution of the monopole-antimonopole pairs. Sections 2 through 6 have delivered:

- **Definition and computation of Q** (Section 2). The winding number Q is the degree of the map **n**|_Σ: Σ → *S²*, expressed by the surface integral Q = (1/4π) ∫ **n** · (∂_θ**n** × ∂_φ**n**) dθ dφ. Explicit computation gives Q = +1 for the hedgehog monopole, Q = −1 for the antihedgehog.

- **Four conservation conditions verified** (Section 3). The current is conserved by antisymmetry (C2.2.1); the equations of motion preserve charge away from cores (C2.2.2); the substrate grain forbids UV leakage with r_core/ℓ_ED ~ 10⁵³ (C2.2.3); the V5 quench redistributes but does not create net charge (C2.2.4).

- **Forced pair production** (Section 3.1). Charge conservation from a Q = 0 initial state requires defects to form as monopole-antimonopole pairs of total charge zero — the topological origin of the Bullet's two-peak lensing signature.

- **Advection with subcluster flow** (Section 4). Each defect advects with its host subcluster (overdamped, advection-dominated); the +1 monopole tracks subcluster A, the −1 antimonopole tracks B; both track the collisionless galaxies (which carry the orientation), not the ram-stripped gas; pair separation grows as Δr(t) ≈ v_rel × t_post.

- **Annihilation suppression** (Section 5). Opposite charges attract Coulomb-like (F_pair ∝ 1/Δr²), but the advection carries them apart past the capture radius from formation; the statistical annihilation rate is exponentially suppressed, giving 1/Γ_ann ~ 10⁵–10²² Gyr — far longer than any other timescale.

- **Decoherence setting the observable lifetime** (Section 6). The conserved charge persists indefinitely, but the coherent organizational dressing that makes it gravitationally visible relaxes on τ_relax; the observable Bullet signature has lifetime τ_pair ≈ τ_relax ~ 10⁸–10⁹ years, set by decoherence (not annihilation).

The dynamical picture is complete: pairs form (forced by conservation), separate (advection), survive (annihilation forbidden), and fade observably on τ_relax (decoherence) while their charges persist.

### 7.1 Structural commitments satisfied

D2.1 Section 11.2 specified the D2.2 mandate. We list each commitment and its fulfillment.

| D2.2 mandate (from D2.1 §11.2) | Fulfilled in | Status |
|---|---|---|
| Formal definition of the winding number for the *S²* field | Section 2.2 — surface integral and topological current | ✓ |
| Write the topological current J^μ explicitly | Section 2.2 | ✓ |
| Prove ∂_μ J^μ = 0 (antisymmetry + constraint) | Section 3.1 | ✓ |
| Verify Q gauge-independent under surface reparameterization | Section 2.3 (degree-of-map invariance) | ✓ |
| Confirm Q integer-valued under the dynamics | Section 3.1–3.2 | ✓ |
| Conservation: identical (C2.2.1) | Section 3.1 | ✓ |
| Conservation: under EOM (C2.2.2) | Section 3.2 | ✓ |
| Conservation: at grain cutoff (C2.2.3) | Section 3.3 | ✓ |
| Conservation: under V5 coupling (C2.2.4) | Section 3.4 | ✓ |
| Post-formation: advection drift equation | Section 4.1 | ✓ |
| Post-formation: annihilation rate Γ_ann | Section 5.3 | ✓ |
| Post-formation: decoherence rate Γ_dec | Section 6.3 | ✓ |
| Combined lifetime τ_pair | Section 6.4 | ✓ |
| Verify τ_pair ≳ τ_relax for cosmological-rate consistency | Section 6.4 (τ_pair ≈ τ_relax) | ✓ |

Every commitment in the D2.2 mandate is fulfilled. **D2.2 is structurally complete.** The winding number is defined, its conservation is verified under all four conditions, pair production is shown to be forced, and the full post-formation evolution (advection, annihilation, decoherence) is derived. What remains is purely numerical: the order-of-magnitude estimates throughout D2.2 depend on the substrate parameters (κ, c_s, β, γ, η, e), which D2.3 must pin down.

### 7.2 What D2.3 must now deliver

D2.3 is the **Substrate Organizational Relaxation Timescale** deliverable. After D2.1 and D2.2, its mandate is sharply defined: every structural and dynamical result is in place; D2.3 supplies the numbers.

**1. Derive τ_relax from substrate primitives.** D2.2 established that τ_relax is the master quantity — the advection time, the decoherence rate, and the observable lifetime all reduce to it. D2.3 must express τ_relax ~ √(κ/βρ_c) in terms of substrate-primitive quantities (M_P, a₀, c, and the substrate organizational speed c_s), producing a closed-form expression and verifying it falls in the 10⁸–10⁹ year range required by D2.1 §10 and D2.2 §6.

**2. Close the open parameters of D2.1 §7 and §8.** The five Lagrangian constants must be fixed:
- **κ** — substrate organizational stiffness (sets r_core, M_core, τ_relax)
- **c_s** — substrate organizational propagation speed (sets τ_0, the Kibble time-scale)
- **β** — quench coupling strength (sets τ_relax, the quench force)
- **γ** — strain coupling (sets the commitment-density-modulated gradient cost)
- **e** — grain stabilizer coupling (sets the core regularization at ℓ_ED)

Each is either derived from substrate primitives (preferred; makes the predictions form-forced) or fit to multi-cluster observations (acceptable; makes them value-inherited).

**3. Produce numerical values for the four key predictions:**
- **τ_relax** — the master timescale (~10⁸–10⁹ yr, to be tightened)
- **v_crit** — the critical merger velocity below which no defects form (~300 km/s estimated in D2.1 §8.6, to be tightened)
- **ξ_KZ** — the Kibble-Zurek freeze-out correlation length (~700 kpc estimated in D2.1 §8.4)
- **Δr_offset(v_rel)** — the predicted offset-vs-velocity law (Δr_offset ∝ v_rel × t_post above v_crit; from D2.1 §8.6 and D2.2 §4.3)

**4. Provide the quantitative inputs for Phase-3 observational tests.** With v_crit and the offset law pinned, Phase-3 can identify supercritical and subcritical mergers in the observational catalog and test the predicted scaling (falsifier F1) and the sharp transition (falsifier F2). D2.3 supplies the numbers that turn the D2.2 structural predictions into testable quantitative ones.

### 7.3 Interfaces between D2.2 and D2.3

The two deliverables exchange a specific set of quantities.

**What D2.2 hands to D2.3:**

| Quantity | Where derived | Role for D2.3 |
|---|---|---|
| The decoherence equation (linearized δ**n** dynamics) | Section 6.2 | Provides the relaxation structure from which τ_relax is extracted |
| The lifetime condition τ_pair = τ_relax | Section 6.4 | Confirms τ_relax is the master quantity D2.3 must derive |
| The separation law Δr(t) ≈ v_rel × t_post | Section 4.3 | Input to the offset prediction; D2.3 supplies the gas-drag correction factor |
| The annihilation-suppression condition (Δr > Δr_capture) | Section 5.2 | Confirms D2.3 need not track annihilation; only τ_relax matters for lifetime |
| The capture radius Δr_capture(κ, c_s, η, v_rel) | Section 5.2 | Function of substrate parameters D2.3 will pin down |
| The decoherence rate Γ_dec ~ √(βρ_c/κ) | Section 6.3 | Direct expression for τ_relax in substrate parameters |

**What D2.3 returns to D2.2 (closing the order-of-magnitude estimates):**

| Quantity | D2.2 estimate | D2.3 deliverable |
|---|---|---|
| τ_relax | ~10⁸–10⁹ yr | Closed-form value from substrate primitives |
| v_crit | ~300 km/s (D2.1 §8.6) | Tightened value with uncertainty |
| ξ_KZ | ~700 kpc (D2.1 §8.4) | Tightened value |
| (κ, c_s, β, γ, η, e) | dimensional estimates | Numerical or primitive-derived values |
| Δr_capture | ≪ r_core (qualitative) | Numerical value, confirming annihilation suppression quantitatively |

The interface is clean: D2.2 produces every *structural form* and *functional dependence*; D2.3 produces every *number*. Neither deliverable is complete without the other, and Phase-2 closes only when both are filed.

### 7.4 Preparation for the synthesis paper

The Phase-2 synthesis paper (`Paper_ED_Bullet_TopologicalDefect.md`) will integrate the three deliverables into a single account of the Bullet mechanism:

- **Topology (D2.1).** The substrate's organizational order parameter is a vector field on *S²*; its vacuum manifold supports π₂(*S²*) = ℤ point monopoles; the Lagrangian, Kibble-Zurek defect-density, kernel-portability, and cosmological-rate consistency are established.
- **Dynamics (D2.2).** The winding number is conserved under all four conditions; pair production is forced; the pair advects with the subclusters, resists annihilation, and fades observably on τ_relax while its charge persists.
- **Numerical closure (D2.3).** τ_relax, v_crit, ξ_KZ, and the offset law are pinned to numbers from substrate primitives, making the predictions quantitatively testable.

Three synthesis-level claims become possible **only after D2.3** closes:

**Synthesis Claim 1 — A quantitative offset-velocity law.** With v_crit and the substrate parameters fixed, the synthesis can state the predicted Δr_offset(v_rel) as a numerical curve, not just a scaling. This is the central Phase-3-testable prediction (falsifier F1). It cannot be stated quantitatively until D2.3 supplies v_crit and the gas-drag correction.

**Synthesis Claim 2 — A sharp transition at a specific velocity.** The Kibble mechanism predicts a knee (not a smooth roll-off) at v_crit (falsifier F2). The synthesis can state the *location* of the knee as a specific velocity only after D2.3 derives v_crit. This distinguishes the topological-defect mechanism from MOND-EFE-style smooth accommodations.

**Synthesis Claim 3 — A closed cosmological-rate prediction.** D2.1 §10 estimated ~0.5–1 active Bullet-class systems in the observable universe using τ_relax as input. With D2.3's derived τ_relax, the synthesis can state the predicted count and formation rate as tightened numbers, completing the cosmological-consistency argument and confirming Ω_defects ~ 10⁻¹⁰ at the parameter level.

These three claims are the payoff of the full Phase-2 effort. D2.1 makes them structurally possible; D2.2 makes them dynamically grounded; D2.3 makes them quantitative. The synthesis paper states them and prepares the Phase-3 observational program.

### 7.5 D2.2 closure statement

With this section filed, **D2.2 — The Winding Number, Charge Conservation, and Pair Evolution — is complete.**

D2.2's structural commitments are all satisfied (Section 7.1). The winding number is defined and computed; its conservation is verified under all four conditions; pair production is shown to be forced by conservation; and the complete post-formation evolution — advection, annihilation suppression, and decoherence — is derived. The observable Bullet lifetime is established as τ_pair ≈ τ_relax, validating the D2.1 cosmological-rate calculation. The deliverable hands off to D2.3 a single master quantity (τ_relax) and a clean set of substrate parameters to numericalize.

**Summary paragraph for Memo_02:**

> *D2.2 (Paper_ED_Bullet_WindingNumber) defines the conserved topological charge of the substrate's S² defects and derives the complete evolution of the monopole-antimonopole pairs produced in a Bullet-class merger. The winding number Q is computed (Q = +1 hedgehog, Q = −1 antihedgehog) and shown conserved under all four conditions from D2.1 §11.2 — identically, under the equations of motion, at the substrate grain (r_core/ℓ_ED ~ 10⁵³), and under the V5 quench coupling. Charge conservation forces defects to form as monopole-antimonopole pairs of total charge zero, which is the topological origin of the Bullet's two-peak lensing signature. The pair advects with the outgoing subclusters (each defect tracking its subcluster's collisionless galaxies, not the ram-stripped gas), separates as Δr(t) ≈ v_rel × t_post, and cannot annihilate within cosmic history (1/Γ_ann ~ 10⁵–10²² Gyr). The observable lensing signature fades by organizational decoherence on the substrate relaxation time τ_relax ~ 10⁸–10⁹ years, while the conserved charge persists invisibly — resolving the apparent tension between exact charge conservation and finite signature lifetime. Every dynamical phase is derived; every result reduces to the master quantity τ_relax, which D2.3 must now derive from substrate primitives. D2.2 is structurally complete.*

**Phase-2 status after D2.2 closure:**

- D2.1 — Vacuum Manifold: ✓ Complete
- D2.2 — Winding Number: ✓ Complete (this paper)
- D2.3 — Relaxation Time: Open — mandate sharply defined (Section 7.2); ready to begin
- Phase-2 synthesis (Paper_ED_Bullet_TopologicalDefect): awaits D2.3
- Phase-2 integration (Memo_02): awaits D2.3
- Phase-3 catalog work: can begin in parallel; requires D2.3's v_crit for full quantitative testing

D2.3 takes it from here.

---

*End of Section 7. End of D2.2.*

---

## D2.2 Closure Summary

**Paper:** *The Winding Number, Charge Conservation, and Pair Evolution for S² Defects in Substrate-Organizational Mergers*
**Arc:** Bullet_Arc (ED-Bullet-01) — Phase-2, Deliverable D2.2
**Status:** **COMPLETE**
**Sections:** 1–7; ~13,500 words

**Principal result:**
The topological charge Q of the substrate's *S²* defects is an exactly conserved integer (Q = +1 monopole, Q = −1 antimonopole), conserved under all four conditions from D2.1 §11.2. Conservation forces monopole-antimonopole pair production — the topological origin of the Bullet's two-peak signature. The pair advects with the outgoing subclusters (tracking galaxies, not gas), cannot annihilate within cosmic history, and fades observably by organizational decoherence on τ_relax while its charge persists. The observable Bullet lifetime is τ_pair ≈ τ_relax ~ 10⁸–10⁹ years.

**Next deliverable:**
- D2.3 — *Paper_ED_Bullet_RelaxationTime.md* (derive τ_relax and the substrate parameters; produce numerical v_crit, ξ_KZ, and the offset law)

**After D2.3:**
- Phase-2 synthesis — *Paper_ED_Bullet_TopologicalDefect.md*
- Phase-2 integration — *Memo_02_Bullet_Arc_Integration.md*
- Phase-3 observational catalog work

---

*End of paper.*
