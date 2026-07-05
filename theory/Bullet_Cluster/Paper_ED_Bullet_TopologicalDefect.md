# The Bullet Cluster as a Substrate Topological Defect: An Event Density Synthesis

## Bullet_Arc Phase-2 Synthesis

**Author:** Allen Proxmire
**Date:** June 2026
**Arc:** Bullet_Arc (ED-Bullet-01)
**Status:** Synthesis paper — opening sections (Sections 1–2)
**Integrates:** D2.1 (`Paper_ED_Bullet_VacuumManifold.md`), D2.2 (`Paper_ED_Bullet_WindingNumber.md`), D2.3 (`Paper_ED_Bullet_RelaxationTime.md`)

---

## Abstract

The Bullet Cluster (1E 0657-56) shows a ~110 kpc offset between its weak-lensing mass peaks and its X-ray gas peaks following a high-velocity merger — the most-cited single piece of evidence for collisionless dark matter. This paper synthesizes the three Phase-2 deliverables of the Bullet_Arc into a single account in which the offset arises not from a dark-matter particle but from a **topological defect in the substrate's organizational order parameter**. A fast cluster merger drives the substrate's channel-orientation field through a Kibble-Zurek quench, freezing in a monopole-antimonopole pair on the *S²* vacuum manifold (π₂(*S²*) = ℤ). The pair's conserved topological charge forces it to form in two halves of opposite charge — the origin of the two-peak lensing signature. Each defect advects with its subcluster's collisionless galaxies (not the ram-stripped gas), cannot annihilate within cosmic history, and fades observably on the substrate organizational relaxation time τ_relax ~ 10⁹ years while its charge persists. Numerical closure from substrate primitives gives a defect-formation threshold v_crit ~ 150 km/s, a freeze-out correlation length ξ_KZ ~ 860 kpc (matching the observed ~700 kpc peak separation), and a three-regime offset-velocity law Δr_offset(v_rel) whose shape — sharp turn-on, linear growth, saturation — distinguishes the topological-defect mechanism from both ΛCDM and MOND-EFE. The arc converts a qualitative intuition into a quantitative, falsifiable prediction, with two substrate-physics ingredients flagged as open.

---

## 1. Introduction

### 1.1 Purpose of the synthesis paper

The Bullet Cluster is the textbook case for dark matter. Two galaxy clusters collided at ~3000 km/s; the collisionless galaxies passed through while the gas was slowed by ram pressure; and weak lensing places the gravitational mass with the galaxies, ~110 kpc offset from where most of the baryons (the gas) now sit. The standard reading: a collisionless, non-baryonic mass component passed through with the galaxies. Therefore, dark matter.

The Bullet_Arc proposes a different reading. The offset is not the signature of a particle but of a **topological defect** in the substrate's organizational structure — a frozen-in winding produced when the merger drove the substrate through a transition faster than it could relax. This paper synthesizes the three Phase-2 deliverables that develop this reading into a single, coherent account:

- **D2.1 — Topology** (`Paper_ED_Bullet_VacuumManifold.md`) identified the substrate's organizational order parameter as a unit vector field **n**(*x*) on the vacuum manifold *S²*, whose homotopy π₂(*S²*) = ℤ supports point-monopole defects. It constructed the effective Lagrangian, derived the Kibble-Zurek defect-density estimate, checked kernel-portability, and verified cosmological-rate consistency.

- **D2.2 — Dynamics** (`Paper_ED_Bullet_WindingNumber.md`) defined the conserved winding number, verified its conservation under four conditions, showed that conservation forces monopole-antimonopole pair production, and derived the full post-formation evolution: advection with the subclusters, annihilation suppression, and decoherence-limited observable lifetime.

- **D2.3 — Numerical closure** (`Paper_ED_Bullet_RelaxationTime.md`) derived the substrate organizational relaxation time from primitives, closed the five Lagrangian constants, and produced numerical values for the defect-formation threshold v_crit, the freeze-out length ξ_KZ, and the offset-velocity law Δr_offset(v_rel), all matched to the Bullet.

This synthesis paper integrates the three into one account, written for a reader who has not worked through the technical derivations. It states what the mechanism is, why it reproduces the Bullet, and what it predicts — and is the document from which the arc's claims should be cited.

### 1.2 The three synthesis-level claims

The integration of D2.1, D2.2, and D2.3 enables three claims, each resting on one deliverable but coherent only in combination.

**Claim 1 — The Bullet offset arises from a monopole-antimonopole pair in an *S²* order parameter.** The substrate's organizational state at cluster scales is a channel-orientation field on *S²*. A fast merger quenches this field, and the topology π₂(*S²*) = ℤ guarantees that the quench produces point-monopole defects. The two offset lensing peaks are the two members of a single monopole-antimonopole pair. *(Topology — D2.1.)*

**Claim 2 — The pair's dynamics reproduce the observed phenomenology.** Charge conservation forces the defects to form in opposite-charge pairs (two peaks). Each defect advects with its subcluster's collisionless galaxies, not the ram-stripped gas — placing the lensing peaks with the galaxies and offset from the gas, exactly as observed. The pair cannot annihilate within cosmic history, and its observable signature persists for ~τ_relax before fading. *(Dynamics — D2.2.)*

**Claim 3 — The numerical predictions match the Bullet and define falsifiable tests.** Closure from substrate primitives gives v_crit ~ 150 km/s (the Bullet is ~20× supercritical), ξ_KZ ~ 860 kpc (matching the observed ~700 kpc peak separation), and a three-regime offset-velocity law that reproduces both the Bullet's ~700 kpc peak separation and its ~110 kpc per-subcluster gas-lag offset. The law's distinctive shape defines tests that distinguish the mechanism from ΛCDM and MOND-EFE. *(Numerical closure — D2.3.)*

Together, the three claims constitute the arc's case: the Bullet offset is a topological-defect phenomenon, its dynamics reproduce the observed structure, and its quantitative predictions are testable and falsifiable.

### 1.3 Structure of the paper

This synthesis is organized to be read independently of the technical deliverables.

- **Section 2** — Executive summary of results: the topological, dynamical, and numerical structure in brief, with the falsifier table.
- **Section 3** — Topological structure: the *S²* order parameter, the vacuum manifold, and the monopole defect, in accessible form.
- **Section 4** — Dynamical structure: pair production, advection, annihilation suppression, and lifetime.
- **Section 5** — Numerical results: τ_relax, v_crit, ξ_KZ, and the offset-velocity law.
- **Section 6** — The central prediction and its distinction from ΛCDM and MOND-EFE.
- **Section 7** — Open items, Phase-3 program, and the place of the arc in the broader ED dark-matter account.

Sections 1–2 (this filing) introduce the synthesis and summarize the results. Sections 3–7 follow in continued work, each compressing the corresponding technical deliverable to synthesis level.

---

## 2. Executive Summary of Results

### 2.1 The topological structure

The substrate, in Event Density, is built from discrete events linked by channels — structural relations that carry the orientation of the substrate's organizational state. At cluster scales, that organizational state is described by a unit vector field **n**(*x*), the local channel orientation, taking values on the sphere of directions *S²*.

The space of equilibrium configurations — the **vacuum manifold** — is *S²* itself. The topology of this manifold is what matters: the second homotopy group π₂(*S²*) = ℤ is non-trivial, which means the field can wrap the sphere an integer number of times around a point in space. Each such wrapping is a **point-monopole defect**, labeled by an integer **winding number** Q. A Q = +1 defect is a "hedgehog" where the field points radially outward; a Q = −1 defect is its mirror.

The merger produces these defects. When two clusters collide faster than the substrate can reorganize, the field is forced into a configuration it cannot smoothly relax, and monopoles freeze in — the cluster-scale analogue of the Kibble mechanism by which cosmic defects form in early-universe phase transitions. The Bullet's two lensing peaks are a single monopole-antimonopole pair.

### 2.2 The dynamical structure

Three dynamical facts reproduce the observed phenomenology.

**Pair production is forced.** The total topological charge before the merger is zero (no defects). Charge is exactly conserved. So the merger cannot produce a lone monopole — it must produce defects in charge-canceling pairs. The two-peak structure of the Bullet is not a coincidence of two independent objects; it is the two halves of a single conserved-charge-zero pair. This is the topological origin of the two-peak signature.

**The defects track the galaxies, not the gas.** Each defect is anchored to its subcluster's organizational orientation, which is carried forward through the merger by the collisionless galaxies (which pass through unimpeded). The gas, decelerated by ram pressure, is mechanically decoupled from the organizational field and lags behind. The lensing peaks therefore sit with the galaxies and are offset from the gas — exactly the Bullet configuration.

**The signature is decoherence-limited, not annihilation-limited.** The pair separates with the outgoing subclusters and cannot recombine within cosmic history (annihilation is suppressed by ~10⁵–10²² Gyr). But the conserved charge, though permanent, becomes gravitationally invisible once the extended coherent field that lenses background galaxies relaxes — on the substrate organizational relaxation time τ_relax ~ 10⁹ years. The charge persists; the lensing signal fades. This resolves how an exactly-conserved integer charge produces a finite-lifetime observable, and it sets the observational window during which a merger looks like a Bullet.

### 2.3 The numerical closure

Closure from substrate primitives — the Planck mass M_P (organizational stiffness) and the cosmological outer-scale a₀ = cH₀/(2π) (quench coupling) — produces three numbers.

- **τ_relax ~ 10⁹ years** — the substrate organizational relaxation time, derived as τ_relax ~ c/a_cluster (interface-enhanced). This is the master timescale: it sets the observable lifetime, the defect-formation threshold, and the active-defect population.

- **v_crit ~ 150 km/s** — the critical merger velocity. Below it, the substrate has time to relax and no defects form; above it, the quench is supercritical and a pair freezes in. The Bullet (~3000 km/s) is ~20× supercritical.

- **ξ_KZ ~ 860 kpc** — the Kibble-Zurek freeze-out correlation length, setting the defect-network scale. It matches the observed ~700 kpc lensing-peak separation within ~20%.

These three, with the advection law from the dynamics, assemble into the central prediction.

### 2.4 The central falsifiable prediction

The **offset-velocity law** Δr_offset(v_rel) is the arc's headline result — a three-regime curve:

```
Δr_offset(v_rel)  =  { 0,                      v_rel < v_crit ~ 150 km/s   (subcritical)
                    { v_rel × t_post,          v_crit < v_rel ≲ 5600 km/s  (advection-limited)
                    { ξ_KZ ~ 860 kpc,          v_rel ≳ 5600 km/s           (saturated)
```

Below v_crit: no offset, lensing tracks gas. Between v_crit and the saturation velocity: the offset grows linearly with merger velocity, lensing tracks galaxies. Above the saturation velocity: the offset caps at ξ_KZ, and the fastest mergers may show multiple offset peaks.

The Bullet lands in the advection-limited regime, reproducing both its ~700 kpc peak separation and its ~110 kpc per-subcluster gas-lag offset from the single advection scale v_rel × t_post. The law's distinctive *shape* — sharp turn-on, linear growth, saturation — is what distinguishes the topological-defect mechanism from the alternatives: ΛCDM predicts no systematic offset-velocity relation, and MOND-EFE predicts a smooth relation with no threshold or saturation.

### 2.5 The three falsifiers

The arc makes three falsifiable predictions, each testable against the catalog of merging clusters.

| Falsifier | Prediction | Confirmed if | Refuted if |
|---|---|---|---|
| **F1** — Offset-velocity law | Δr_offset has a sharp turn-on at v_crit, then grows linearly (∝ v_rel × t_post) | Offsets scale linearly with v_rel × t_post above a threshold; no offset below | Offsets show no velocity scaling, or appear in clearly subcritical mergers |
| **F2** — Sharp Kibble knee | The turn-on at v_crit is a step (defect either forms or not), not a smooth roll-off | Offset switches on abruptly at a specific v_crit | Offset rises gradually with velocity (a smooth roll-off, consistent with MOND-EFE rather than topological defects) |
| **F3** — ξ_KZ saturation | The offset saturates at ξ_KZ ~ 860 kpc; the fastest mergers may show multiple peaks | High-velocity mergers show offsets capped at ~ξ_KZ; multiple peaks appear at the highest velocities | Offsets grow without bound at high velocity; no saturation or multiplicity ever observed |

The three falsifiers test the three regimes of the offset-velocity law. Together they constitute a sharp, multi-pronged test that distinguishes the topological-defect mechanism from both the particle-dark-matter and modified-gravity alternatives. The arc is falsifiable; Phase-3 performs the test.

### 2.6 Two open ingredients

The numerical closure rests on two substrate-physics ingredients used with physically-motivated estimates but not yet derived from first principles:

1. **The super-linear substrate shock response** sets the precision of τ_relax (and hence v_crit). If the substrate's commitment density responds super-linearly to the merger's rapid gravitational reconfiguration, τ_relax ~ 10⁹ years; if merely linearly, τ_relax ~ 10¹⁰ years and v_crit shifts to ~15 km/s. Either way the qualitative three-regime structure survives, and a longer τ_relax actually improves the cosmological-rate agreement.

2. **The external-stabilization two-timescale structure** reconciles the threshold scale (v_crit, set by the macroscopic relaxation time) with the freeze-out scale (ξ_KZ, set by the microscopic core time). The two differ because the monopole is stabilized by the cluster's commitment-density structure rather than a self-consistent vacuum mass gap — consistent with the core-vs-dressing distinction in the dynamics, but not yet fully derived.

Both are flagged as the natural next targets for deeper ED work. Neither threatens the qualitative predictions; both would tighten the numbers from order-of-magnitude to precise.

### 2.7 Implications for Section 3 — Topological Structure

Section 2 has summarized the arc's results at a glance: a monopole-antimonopole pair on the *S²* vacuum manifold (topology), forced into existence by charge conservation and tracking the galaxies (dynamics), with a defect-formation threshold and freeze-out scale that match the Bullet and define a three-regime offset-velocity prediction (numerical closure).

Section 3 develops the first of these — the topological structure — in accessible form. It will explain, without requiring the technical derivation:

1. **Why the order parameter is a vector field on *S²*.** The substrate's channels carry orientation; the space of orientations is the sphere; the organizational state at cluster scales is a field of such orientations. Section 3 motivates this identification from the substrate primitives.

2. **Why π₂(*S²*) = ℤ matters.** The non-trivial second homotopy group is what makes stable point defects possible. Section 3 explains the homotopy classification in intuitive terms — how a field can "wrap" the sphere of orientations an integer number of times, and why that wrapping cannot be smoothly undone.

3. **What a monopole is, physically.** The hedgehog configuration, its winding number, and why it produces a localized gravitational signature. Section 3 connects the abstract topology to the concrete object that lenses background galaxies.

With the topological structure established in accessible form, Section 4 will develop the dynamics (pair production, advection, lifetime) and Section 5 the numerical results, building the full synthesis for a reader approaching the arc for the first time.

---

*End of Section 2. The results are summarized; the three falsifiers are stated. Section 3 below develops the topological structure in accessible form.*

---

## 3. Topological Structure

### 3.1 Why a topological explanation is even on the table

Start with what makes the Bullet strange. In an ordinary gravitational system, the gravity points to where the mass is. Weigh the components of the Bullet — the gas carries five to ten times more mass than the stars — and the gravity ought to peak where the gas is. It doesn't. The lensing peaks sit with the galaxies, off to either side, while the bulk of the ordinary matter sits stranded in the middle.

The standard fix adds an invisible component — dark matter — that travels with the galaxies and carries the missing gravity. That works, but it requires a new kind of particle that has never been detected in any laboratory.

There is another way to read the picture, and it is worth stating the shift in plain terms.

The usual assumption is: **matter distribution causes gravity.** Put the mass somewhere, and the gravitational field follows it. On this view, gravity is a faithful reporter of where the stuff is.

Event Density proposes instead: **the gravitational field inherits its structure from the substrate.** Gravity, at bottom, is not sourced by a tally of matter at a point — it is the coarse-grained appearance of the substrate's organizational state. Usually that organizational state tracks the matter closely, so the two readings agree and you never notice the difference. But in a violent event — a fast cluster merger — the organizational state can be knocked into a configuration that *does not* track the current matter distribution, and then the gravity follows the substrate's structure rather than the gas.

This opens the door to a topological explanation. The core idea, stated once and developed through the rest of this section, is this: **the substrate's organizational field can wrap around a point in space an integer number of times, and that wrapping cannot be undone without tearing the field.** A wrapped region carries a localized gravitational signature that stays put even after the matter that produced it has moved on. The Bullet's two offset lensing peaks are two such wrapped regions.

That is the claim. The rest of this section explains what "wrapping" means, why it produces a stable, gravitationally-visible object, and why such objects must come in pairs.

### 3.2 The *S²* order parameter

An **order parameter** is a quantity that describes how a system is organized — a single field that captures the relevant structure of a complicated medium. A familiar example is a magnet: at every point inside a magnet, the magnetic material "points" in some direction (the direction the tiny atomic magnets are aligned). That direction, defined at every point, is the magnet's order parameter. It tells you how the magnet is organized without tracking every individual atom.

The substrate has an order parameter of the same kind. At every point in space, the substrate's channels — the structural relations that carry its organizational state — have an **orientation**. Bundle them together and coarse-grain, and you get a single direction defined at every point: the local channel orientation. Call it **n**(*x*) — a field that points in some direction at every location *x* in space, exactly like the magnetization of a magnet.

Now ask: what is the space of all the directions **n** could point? A direction in three-dimensional space is an arrow of unit length from the origin. The tips of all such arrows trace out the surface of a sphere. So the space of all possible orientations is a sphere — denoted *S²*, the two-dimensional surface of a ball.

This is the key geometric fact. The order parameter **n**(*x*) is a field of directions, and every direction is a point on the sphere *S²*. The substrate's organizational state, at any location, is a point on this sphere; the organizational state across all of space is an assignment of a sphere-point to every location. The sphere *S²* is the **vacuum manifold** — the space of all the equilibrium configurations the field can settle into.

### 3.3 Why "wrapping the sphere" matters

Here is where topology enters, and it is worth slowing down because this is the crux.

Consider a small closed surface — a little sphere — drawn around some point in space. At every location on that little surface, the field **n** points in some direction, i.e., picks out a point on the orientation-sphere *S²*. So the field defines a map: from the little surface in space, to the sphere of orientations.

Most of the time this map is boring. If **n** points in roughly the same direction everywhere on the little surface, the map covers only a tiny patch of the orientation-sphere, and you can smoothly slide it down to a single point. Nothing interesting.

But the map can be more interesting. As you move around the little surface in space, the direction **n** can rotate in such a way that it sweeps across the *entire* orientation-sphere — covering it completely, once, before you return to your starting point. When this happens, the field is said to **wrap** the sphere once. It can also wrap twice, or three times, or — in the opposite sense — once backward. The number of wrappings is an integer, and it is called the **winding number**.

The crucial fact: **you cannot change the winding number by smoothly adjusting the field.** This is the content of the mathematical statement "π₂(*S²*) = ℤ" — the wrappings of a sphere by a sphere come in integer classes, and you cannot continuously deform one class into another.

The standard way to feel this is the **balloon analogy**. Imagine wrapping a rubber band around a balloon. You can wind it around once, twice, or not at all. If it's wound once, you cannot get to zero windings by sliding and stretching the band — you would have to cut it. The number of times the band is wound is a discrete, integer property, and changing it requires a discontinuous act (cutting), never a smooth one (sliding). The winding number of the substrate's organizational field works the same way: it is an integer that smooth changes cannot touch. To change it, you have to tear the field — punch a hole in it — which costs a definite, irreducible amount.

This rigidity is what makes a wrapped configuration *stable*. Once the field wraps the orientation-sphere once around some point in space, it is stuck there. No amount of gentle relaxation can unwind it. The winding is **topologically protected**.

### 3.4 What a monopole is in this context

The simplest non-zero winding — winding number +1 — has a concrete, picturable shape. It is the configuration in which the field **n** points radially *outward* from a central point, like the spikes of a sea urchin, or the quills of a hedgehog standing on end. Everywhere around the center, the field points straight away from it. As you walk around a little surface enclosing the center, the outward-pointing field sweeps across every direction on the orientation-sphere exactly once. Winding number: +1.

This configuration is called a **monopole** (a "hedgehog," in the physicists' affectionate term). It has a center — the point from which all the spikes emanate — where the field cannot decide which way to point (it would have to point in all directions at once), so the field is singular there. Around that center, the field carries the protected winding.

Because the winding is topologically protected (Section 3.3), the monopole cannot be smoothed away. You cannot comb the hedgehog flat. Any attempt to relax the field back to a uniform configuration is blocked by the integer winding number, which smooth deformations cannot change. The monopole is a stable, localized, permanent feature of the field — a knot that cannot be untied without cutting.

And a monopole carries a localized gravitational signature. The substrate's organizational gradient — how rapidly **n** changes from point to point — is concentrated around the monopole's center, and that concentrated gradient sources a localized contribution to the gravitational field (in the same way the substrate's organizational structure sources gravity everywhere in Event Density). The monopole is therefore an object that *lenses* background galaxies: a gravitational mass, of sorts, but made of frozen substrate structure rather than matter.

The mirror configuration — the field pointing radially *inward*, the hedgehog turned outside-in — has winding number −1 and is called an **antimonopole**. The Bullet mechanism, as the next subsection explains, produces a monopole and an antimonopole together.

### 3.5 Why a pair must form

Why a pair, and not a single monopole?

The answer is a conservation law, and it has an intuitive form. The **total winding number** of the whole system — counted over all of space — is a conserved quantity. It cannot change through any smooth process, for exactly the reason a single winding cannot be undone: smooth changes never touch integer windings. The only way to change the total is the discontinuous act of creating or destroying a winding, and even that must respect the total.

Before the merger, the substrate's organizational field is smooth and unwound. The total winding number is zero. There are no defects.

After the merger, if defects have formed, the total winding number must *still* be zero — because no smooth process during the merger could have changed it, and the merger, however violent, drives the field through smooth (if rapid) evolution everywhere except at the defect cores. So whatever defects appear must have winding numbers that sum to zero.

A single monopole has winding +1. That would change the total from 0 to +1 — forbidden. The simplest allowed configuration is a **monopole and an antimonopole together**: +1 and −1, summing to zero. The conservation law permits the merger to create defects only in such charge-canceling pairs.

This is the topological origin of the Bullet's two-peak structure. The two offset lensing peaks are not two independent objects that happened to form side by side. They are the two halves of a single pair — a monopole and its antimonopole — forced to appear together by the conservation of total winding number. One peak carries winding +1; the other carries −1; together they carry zero, exactly as the unwound pre-merger state required.

The observation of *exactly two* offset peaks, rather than one or three, is therefore not a coincidence to be fit but a consequence to be expected. A topological mechanism producing a single offset peak would violate winding conservation; an odd number of equal-strength peaks would be impossible. Two peaks of opposite winding, summing to zero, is what the conservation law demands.

### 3.6 Consolidated picture

The substrate's organizational state at cluster scales is a field of directions — at every point in space, the channels point some way, and the space of all possible ways is a sphere. This field can wrap the sphere of directions an integer number of times around a point in space, and such a wrapping — a "monopole" — cannot be smoothed away, because integer windings are immune to continuous change. A fast cluster merger knocks the field into a wrapped configuration, freezing in a monopole. But the total winding must stay zero, so monopoles can form only in monopole-antimonopole pairs — and those two opposite windings, each carrying a localized gravitational signature, are the Bullet's two offset lensing peaks. The gravity sits with the windings, not the gas, because the windings are made of frozen substrate structure rather than matter.

That is the topological story: a stable, protected, paired structure in the substrate's organizational field, produced by the merger and carrying gravity that does not track the displaced gas.

### 3.7 Implications for Section 4 — Dynamical Structure

Section 3 established *what* the defects are: a topologically protected monopole-antimonopole pair in the substrate's *S²* organizational field, forced to form together by winding conservation. What it has not yet explained is how the pair *behaves* once formed — and that behavior is what reproduces the detailed Bullet phenomenology.

Section 4 takes up the dynamics. Three questions drive it:

1. **Where do the two defects go after they form?** Section 4 explains that each defect drifts with its own subcluster's galaxies — carried along by the collisionless matter that passed through the merger — rather than with the gas, which was left behind by ram pressure. This is why the lensing peaks track the galaxies and are offset from the gas.

2. **Why don't the monopole and antimonopole simply find each other and annihilate?** Opposite windings attract, and if they met they would cancel (the one place the conservation law permits the total to return toward zero). Section 4 explains why the merger carries them apart faster than they can recombine, so the pair survives.

3. **Why does the Bullet signature have a finite lifetime if the windings are permanent?** Section 4 resolves this apparent paradox: the winding number is conserved forever, but the extended field that makes it gravitationally visible relaxes over the substrate's organizational timescale, so the lensing signal fades even though the topological charge persists.

With the dynamics established, Section 5 turns to the numbers — the defect-formation threshold, the freeze-out scale, and the offset-velocity law — that make the picture quantitatively testable.

---

*End of Section 3. The topological structure is established: a protected monopole-antimonopole pair forced by winding conservation. Section 4 below develops how the pair behaves.*

---

## 4. Dynamical Structure

### 4.1 How the pair forms

The pair forms in a brief, violent window — the moment the two clusters interpenetrate.

Before the collision, each cluster is a settled thing. Its substrate organizational field — the field of channel orientations from Section 3 — has had a long time to smooth itself out, and it sits in a calm, defect-free configuration, pointing one way through one cluster and another way through the other. Two calm fields, each at peace with its own cluster.

Then the clusters slam together at thousands of kilometers per second.

At the collision interface, the two organizational fields meet. One side wants to point the way the first cluster's field pointed; the other side wants to point the way the second cluster's field pointed; and the two directions do not match. Ordinarily the substrate would resolve this by smoothly rotating the field from one orientation to the other across the interface — a gradual turn, like the gradual change of wind direction across a weather front. But smoothing takes time, and the collision does not give it time.

This is the **quench**: the substrate is forced to reorganize faster than it can relax. The merger drives the field through its transition so quickly that the field cannot keep up. It is the same mechanism by which defects form in the early universe — a system rushed through a change faster than it can settle responds by trapping defects — applied here at the scale of colliding galaxy clusters.

When a field is forced to reconcile two mismatched orientations faster than it can smooth them, it cannot complete the reconciliation everywhere. At certain points, the field gets caught — pulled toward incompatible directions at once — and freezes into the wrapped, knotted configuration of Section 3. A winding appears. And because the total winding must stay zero (Section 3.5), the windings appear in canceling pairs: a +1 monopole and a −1 antimonopole, born together in the violence of the interface, frozen into the substrate before it has any chance to relax them away.

That is the moment of creation: not a gentle condensation but a sudden trapping, the substrate snagged on its own inability to reorganize fast enough.

### 4.2 Why the defects follow the galaxies, not the gas

Once formed, the two defects have to go somewhere. Where they go is the whole point — it is what reproduces the Bullet's defining feature, the gravity sitting with the galaxies and away from the gas.

The merger separates the cluster into two kinds of stuff that behave very differently.

The **galaxies** are, on the scale of the collision, effectively collisionless. They are tiny compared to the distances between them, so when two clusters pass through each other, the galaxies of one simply sail between the galaxies of the other, almost untouched. They keep going. After the collision they have passed clean through and emerged on the far side, still moving with their original cluster.

The **gas** is different. It fills the space between the galaxies, and when the two gas clouds meet, they cannot pass through each other — they collide, compress, heat up, and are slowed by the pressure of the impact (ram pressure). The gas of each cluster is left behind, stranded near the collision point, while its galaxies race ahead.

Now, which of these does the substrate's organizational field follow?

The field's orientation is anchored to the bulk organizational structure of each cluster — and that structure is carried by the collisionless component, the galaxies, which preserve their cluster's configuration as they pass through. The gas, mechanically torn away from the cluster's organizational structure by the collision, does not carry the orientation with it. It is just matter that got stuck; the organizational field has moved on with the galaxies.

So each defect, anchored to its cluster's orientation, drifts with that cluster's galaxies — the collisionless component that carried the orientation through the merger. The monopole goes with one cluster's galaxies; the antimonopole with the other's. Neither follows the gas.

And because each defect carries a localized gravitational signature (Section 3.4), the gravity goes where the defects go: with the galaxies. The lensing peaks sit with the galaxies. The gas, left behind in the middle, has most of the ordinary mass but none of the windings — so the gravity is offset from it. That offset is the Bullet.

### 4.3 Why the pair separates instead of annihilating

There is a loose end. A monopole and an antimonopole are opposite windings, and opposite windings attract. If they were to meet, they would cancel — the one circumstance in which the conservation law permits the total winding to return toward zero (a +1 and a −1 annihilating to nothing). So why don't the two defects simply find each other and wink out, erasing the whole signature?

Because the merger is pulling them apart far faster than they can attract each other back together.

After the clusters pass through each other (after "pericenter," the moment of closest approach), the two subclusters are receding — moving apart at thousands of kilometers per second, the same speed at which they collided. Each defect is glued to its own subcluster's galaxies, and those galaxies are racing away from the other subcluster's galaxies. So the two defects are carried apart at the full merger velocity.

The attraction between them is real but weak at large separation, and it falls off rapidly as they get further apart. The receding subclusters win, easily. By the time the defects might have drifted back together, they are hundreds of kiloparsecs apart and still separating.

The intuitive picture: imagine two magnets, of opposite poles, each glued to a separate ice floe, and the two floes drifting apart on a fast current. The magnets attract — but the current carries the floes away far faster than the magnets can pull them back. The magnets never rejoin. They are separated by the motion of the thing they are stuck to.

So it is with the defects. They are stuck to diverging subclusters, and the subclusters carry them apart. The pair cannot annihilate; it survives, the two windings frozen and separating, for as long as the merger geometry holds them apart — which, the numbers show, is far longer than the age of the universe.

### 4.4 Why the signal fades even though the charge persists

This raises a puzzle that has to be faced directly. If the windings are topologically protected and cannot annihilate, they last essentially forever. Yet we see only a handful of Bullet-like systems in the sky at any time — which means the *signature* must fade, even if the windings do not. How can a permanent object have a temporary signal?

The resolution is the distinction between the defect's **core** and its **dressing**.

The **core** is the winding itself — the knotted center where the field wraps the sphere of orientations. This is the topologically protected part. It is permanent; nothing smooth can undo it.

The **dressing** is the extended field around the core — the smooth, large-scale configuration that surrounds the winding and gives it its gravitational reach. It is the dressing, spread over hundreds of kiloparsecs, that actually bends the light of background galaxies. And the dressing is *not* topologically protected. It is an ordinary smooth field, and it can relax — settle gradually back toward the cluster's calm equilibrium — without ever touching the protected winding at the center.

So here is what happens to an old defect. The winding at its core stays, exactly as it was, forever. But the extended dressing that made it gravitationally bright slowly relaxes, over the substrate's organizational settling time. As the dressing fades, the concentrated gradient that lensed background galaxies softens and spreads, and the lensing signal weakens. Eventually the dressing has melted back into the cluster's ambient field, and the defect — though its core winding is still there, still protected — no longer lenses. It has gone quiet.

This is why the Bullet is bright now and older mergers would not be. The Bullet is a recent collision; its defects are freshly formed, their dressings still concentrated and bright. We are seeing it within its window. A merger that happened many settling-times ago still carries its windings — they are permanent — but its dressings have long since relaxed, and it no longer shows a Bullet-style offset. The conserved charge persists; the visible signal fades. Both statements are true, and they describe different parts of the same object.

### 4.5 The full dynamical story in one place

The dynamical arc, start to finish: A fast cluster merger drives the substrate's organizational field through a quench at the collision interface, trapping a monopole-antimonopole pair before the field can relax. Each defect, anchored to its cluster's orientation, drifts with that cluster's collisionless galaxies — which pass cleanly through the merger — rather than with the gas, which is slowed by ram pressure and left behind, so the lensing peaks sit with the galaxies and are offset from the gas. The two defects, glued to subclusters that are receding at thousands of kilometers per second, are carried apart far faster than their mutual attraction can pull them back, so the pair cannot annihilate and survives essentially forever. But the gravitational signature does not survive forever: the protected winding at each defect's core is permanent, while the extended dressing that makes it gravitationally bright relaxes over the substrate's organizational settling time, so the lensing signal fades even as the charge persists. The Bullet is a system caught early, within its bright window; older mergers carry the same conserved windings but have long since gone quiet.

### 4.6 Implications for Section 5 — Numerical Results

Sections 3 and 4 have told the whole story in words: what the defects are (protected monopole-antimonopole pairs) and how they behave (formed by the quench, tracking the galaxies, separating without annihilating, fading by relaxation while the charge persists). The story is coherent and it reproduces the Bullet's qualitative phenomenology — the two peaks, their offset from the gas, the high significance of the signal.

But a qualitative story is not yet a test. To know whether the mechanism is *right*, and not merely plausible, the story has to make numbers — and the numbers have to match.

Section 5 supplies them. It draws on the substrate's fundamental scales — the Planck scale and the cosmological horizon scale a₀ — to compute three quantities that the qualitative story has so far left as words:

1. **How fast a merger must be to trap a defect at all** — the critical velocity below which the substrate has time to relax and no defect forms. The story said "fast enough"; Section 5 says how fast.

2. **How far apart the two defects end up** — the characteristic scale of the frozen-in defect network, which sets the separation of the lensing peaks. The story said "hundreds of kiloparsecs"; Section 5 says how many.

3. **How the offset depends on merger velocity** — the full relationship between how fast two clusters collide and how far their lensing peaks end up offset from the gas. This is the central testable prediction, and Section 5 derives its specific shape.

With these numbers in hand, Section 6 states the prediction in testable form and shows how it distinguishes the topological-defect mechanism from both dark matter and modified gravity, and Section 7 lays out the observational program that would confirm or refute it.

---

*End of Section 4. The dynamical story is complete in accessible form. Section 5 below supplies the numbers that make it testable.*

---

## 5. Numerical Results

The qualitative story of Sections 3 and 4 used three phrases it never pinned down: a merger "fast enough" to trap a defect, defects "hundreds of kiloparsecs" apart, a signal that fades over "the substrate's settling time." This section replaces those phrases with numbers, computed from the substrate's two fundamental scales — the Planck scale (the substrate's finest grain) and the cosmological horizon scale a₀ (the substrate's outer reach, the same scale that explains galaxy rotation curves elsewhere in Event Density). The point of the numbers is not to prove the picture but to make it concrete enough to test: a story that says "fast enough" cannot be checked against an observation, but a story that says "faster than 150 kilometers per second" can.

### 5.1 The relaxation time τ_relax

The most important number is the one that governs everything else: the **relaxation time**, the time it takes the substrate's organizational field to settle back to calm after being disturbed. In the language of Section 4, it is how long the "dressing" around a defect — the extended field that makes it gravitationally bright — stays concentrated before relaxing away.

Computed from the substrate scales, the relaxation time comes out to **roughly a billion years**. (More precisely, it is of order the time light would take to cross the scale set by a cluster's own gravity — which, for a massive cluster, works out to something between a hundred million and ten billion years, with a billion years as the representative value. The remaining uncertainty is one of the two open ingredients discussed in Section 7.)

A billion years sounds long, but on cosmic scales it is brief — the universe is about fourteen billion years old, so a billion years is a few percent of cosmic history. This is the key to a fact the qualitative story left hanging: why we see only a few Bullet-like systems at any moment. A merger produces a defect pair whose dressing stays bright for about a billion years, then fades. So at any given time, the only Bullet-like systems visible are the ones whose mergers happened within roughly the last billion years. Older mergers still carry their permanent windings, but their dressings relaxed long ago, and they no longer lens. The Bullet is bright because it is young — its collision was recent, and we are seeing it well within its billion-year window.

### 5.2 The critical velocity v_crit

The second number is the threshold for forming a defect at all: the **critical velocity**.

Recall the logic of Section 4.1: a defect forms only if the merger reorganizes the field faster than the field can relax. If the merger is slow, the field keeps up — it smoothly follows the changing orientation, settles as it goes, and traps nothing. If the merger is fast, the field falls behind, gets caught, and freezes in a defect. The dividing line between "slow enough to keep up" and "fast enough to get caught" is the critical velocity.

Computed from the relaxation time and the size of the collision region, the critical velocity comes out to **about 150 kilometers per second**.

This number matters because of how it compares to real cluster mergers. Galaxy clusters collide at *thousands* of kilometers per second — the Bullet at about 3000, others in the range of 1000 to 5000. Every one of these is far above 150 km/s. In the language of the mechanism, essentially all observed major cluster mergers are "supercritical" — comfortably fast enough to trap defects. The Bullet, at twenty times the critical velocity, is not a borderline case; it is deep in the defect-forming regime, which is consistent with its showing a clean, unambiguous offset. Only the very slowest mergers — gentle infalls of small groups — would fall below the threshold and form no defect.

### 5.3 The freeze-out scale ξ_KZ

The third number is the characteristic distance between defects at the moment they freeze in — the **freeze-out scale**.

When the merger quenches the field, defects do not appear at random distances from each other. There is a characteristic spacing, set by how far apart the field can stay "coordinated" during the rapid freezing. Closer than this scale, the field is correlated and smooth; farther apart, it is independent. The freeze-out scale is that crossover distance, and it sets the natural separation of the defect pair.

Computed from the substrate scales, the freeze-out scale comes out to **about 860 kiloparsecs** — close to a million light-years, and remarkably close to the Bullet's *observed* separation between its two lensing peaks, which is about 700 kiloparsecs.

This is one of the arc's cleaner successes. The same calculation that gave the critical velocity also gives a defect-separation scale that matches what the Bullet actually shows, to within about twenty percent. The freeze-out scale also sets an upper limit: the two peaks cannot end up farther apart than this scale, because beyond it the defects are no longer a correlated pair. The Bullet's peaks sit just inside this limit, exactly where the mechanism says they should.

### 5.4 The offset-velocity curve

The three numbers combine, together with the simple fact that faster mergers carry their defects apart faster, into the arc's central prediction: a relationship between how fast two clusters collide and how far their lensing peaks end up offset from the gas. The relationship has three regimes.

**Below the critical velocity**, no defect forms, so there is no topological offset at all. The gravity tracks the total mass (gas-dominated), and the lensing peak sits near the gas. No Bullet.

**Above the critical velocity**, a defect pair forms, and the offset grows roughly in proportion to the merger speed — faster collisions fling the defects farther apart before the signal fades, so faster mergers show larger offsets.

**At very high speeds**, the offset stops growing and saturates near the freeze-out scale. Once the defects would be separated by more than that scale, they are no longer a correlated pair, and the offset is capped. The fastest mergers may also show more than two peaks.

In compact form, with v_rel the merger velocity, t_post the time since the collision, v_crit ≈ 150 km/s, and ξ_KZ ≈ 860 kpc:

```
Δr_offset(v_rel)  =  { 0,                      v_rel < v_crit ~ 150 km/s   (subcritical: no offset)
                    { v_rel × t_post,          v_crit < v_rel ≲ 5600 km/s  (offset grows with speed)
                    { ξ_KZ ~ 860 kpc,          v_rel ≳ 5600 km/s           (offset saturates)
```

The shape — flat at zero, then a straight rise, then a flat ceiling — is the signature. It is this *shape* that distinguishes the topological-defect mechanism from the alternatives, as Section 6 develops.

### 5.5 What these numbers mean for the Bullet

Place the Bullet on this curve. Its merger velocity is about 3000 km/s — twenty times the critical velocity, and well below the saturation speed of about 5600. So the Bullet sits squarely in the middle regime, where the offset grows in proportion to merger speed.

The predicted separation between its two lensing peaks, computed from its velocity and the time since its collision, comes out to roughly **450 to 700 kiloparsecs**. The observed separation is about 700 kiloparsecs. The prediction matches the observation, the small remaining gap easily accounted for by the fact that we see the merger somewhat in projection (the true three-dimensional separation is a little larger than the separation we measure on the sky) and by the modest uncertainty in how long ago the collision happened.

The famous *smaller* offset — the ~110 kiloparsec displacement between the lensing peak and the gas peak for the fast-moving "bullet" subcluster that gave the system its name — is the same physics measured a different way. That number is the distance the gas of that subcluster has lagged behind its galaxies, slowed by ram pressure, while the defect raced ahead with the galaxies. The ~700 kpc is the separation between the two defects; the ~110 kpc is the lag of the gas behind one of them. Both come from the single fact that the collisionless components (galaxies and defects) outrun the gas, measured once as a defect-to-defect distance and once as a defect-to-gas distance. The mechanism reproduces both from the same underlying motion.

### 5.6 Consolidated numerical picture

Three numbers, computed from the substrate's fundamental scales, make the qualitative story testable. The relaxation time is about a billion years — a few percent of cosmic history — which is why only recent mergers show the effect and the Bullet is bright because it is young. The critical velocity is about 150 kilometers per second, far below the thousands of kilometers per second at which clusters actually collide, so essentially all major mergers are fast enough to trap defects. The freeze-out scale is about 860 kiloparsecs, close to the Bullet's observed peak separation of about 700. Together with the fact that faster mergers separate their defects more, these combine into a three-regime offset-velocity curve — no offset below the threshold, growth in proportion to speed above it, saturation at the freeze-out scale — and the Bullet, at 3000 km/s, lands in the growth regime at a predicted separation that matches what is seen. The picture is not only coherent; it is quantitatively consistent with the one system we can examine in detail.

### 5.7 Implications for Section 6 — The Central Prediction and Framework Distinction

Section 5 has done something the qualitative story could not: it has put numbers on the page that match an observation. But matching the *one* system we have studied in detail — the Bullet — is necessary, not sufficient. Dark matter also matches the Bullet. Modified gravity, with enough adjustment, can be made to match the Bullet. A mechanism that only reproduced the Bullet would be one more entry in a crowded field, indistinguishable from the others by the one case they all fit.

What distinguishes a mechanism is not the case it was built to explain but the cases it predicts *differently* from its rivals. And here the offset-velocity curve of Section 5.4 becomes decisive — not because it fits the Bullet, but because its distinctive *shape* makes predictions for *other* merging clusters that dark matter and modified gravity do not make.

Section 6 develops this. It takes the three-regime curve and asks: what does it say about mergers at other velocities, and how do those statements differ from what dark matter and modified gravity predict for the same systems? The answer is that the three frameworks predict three different *shapes* for how the offset depends on merger velocity:

1. **Dark matter (ΛCDM)** predicts no systematic offset-velocity relation at all — the offset in any merger depends on the messy details of that particular collision, with no universal threshold or ceiling.

2. **Modified gravity (MOND-EFE)** predicts a smooth, gradual relation — offsets that grow continuously with merger properties, with no sharp turn-on and no saturation.

3. **The topological-defect mechanism** predicts the specific three-regime shape — a sharp turn-on at the critical velocity, linear growth, and a ceiling at the freeze-out scale.

These are different, testable shapes. Measuring the offset-velocity relation across many merging clusters — not just the Bullet — would distinguish them. Section 6 states this prediction precisely and lays out why it is the sharpest available test of the dark-matter question for merging clusters; Section 7 turns it into an observational program.

---

*End of Section 5. The three numbers match the Bullet; the offset-velocity curve is the testable prediction. Section 6 below shows how its shape distinguishes the mechanism from dark matter and modified gravity.*

---

## 6. The Central Prediction and the Framework Distinction

The Bullet Cluster has been called the smoking gun of dark matter. The phrase is worth examining, because a smoking gun is supposed to identify a culprit uniquely — and the Bullet does not. It is consistent with dark matter, yes. But it is also consistent with modified gravity, and, as this arc has argued, with a topological defect in the substrate. Three different culprits, one piece of evidence that fits all of them. The Bullet does not decide between them.

What decides between them is not the Bullet alone but the *pattern across many mergers* — and that pattern is exactly what the three frameworks predict differently. This section states the difference, in plain terms, and shows that it is measurable.

### 6.1 The three-regime prediction, restated

Event Density predicts a specific relationship between how fast two clusters collide and how far their lensing peaks end up offset from the gas. In words:

- **Below a threshold speed** — about 150 kilometers per second — there is no offset at all. The merger is too slow to trap a defect; the gravity tracks the gas; nothing interesting happens.
- **Above the threshold**, a defect pair forms, and the offset grows roughly in proportion to the merger speed. Faster collisions produce larger offsets, in a clean, near-linear relationship.
- **At very high speeds** — a few thousand kilometers per second and up — the offset stops growing and levels off near a ceiling set by the freeze-out scale, about 860 kiloparsecs.

The crucial thing to grasp is that this is a **shape**, not a single number. Plotted as offset against merger speed, it is a flat line at zero, then a sharp upward bend at the threshold, then a straight rise, then a flattening to a ceiling. A flat-bend-rise-flatten shape. The bend at the threshold — the place where the offset switches on abruptly — is the most distinctive feature, and it has a name worth using: a **knee**.

The prediction is not "the Bullet has an offset of such-and-such." It is "the whole population of merging clusters, plotted offset against speed, traces out this particular flat-bend-rise-flatten shape, with the bend at about 150 km/s and the ceiling at about 860 kpc." That is a far stronger, far more falsifiable claim than any single number — and it is one that dark matter and modified gravity do not make.

### 6.2 What ΛCDM predicts

In the standard dark-matter picture, the offset in a merging cluster arises because the dark matter is collisionless (it passes through, like the galaxies) while the gas is collisional (it gets slowed). So dark matter naturally produces offsets — that is exactly why the Bullet was read as evidence for it.

But notice what the dark-matter picture does *not* predict.

It predicts no **sharp threshold**. There is no special speed below which offsets suddenly vanish. A slow merger and a fast merger both separate their collisionless and collisional components; the slow one just separates them less. The offset shrinks smoothly toward zero as the merger slows, but there is no knee, no abrupt switch-off.

It predicts no **universal scaling**. How big the offset is depends on the specific geometry of each collision — the impact angle, the mass ratio, the gas distribution, the viewing angle, the time since impact. Two mergers at the same speed can show very different offsets depending on these messy details. There is no clean line relating offset to speed; there is a scatter-plot.

It predicts no **saturation**. Nothing in the dark-matter picture caps the offset at a particular scale. A fast enough, well-aligned merger could in principle separate its components by any distance; there is no ceiling built into the physics.

So the dark-matter prediction for the offset-velocity relation is, essentially, *there is no clean relation* — just a scatter of points whose spread reflects the case-by-case diversity of mergers. Dark matter explains the Bullet, but it does not predict a curve.

### 6.3 What MOND-EFE predicts

Modified gravity — specifically MOND with its external-field effect, the version equipped to handle environments like a cluster merger — produces offsets too, but through a different mechanism: the modified gravitational response shifts where the effective gravity peaks as the matter reconfigures during the merger.

The signature of this mechanism is **smoothness**. MOND-EFE is a continuous modification of gravity; its response changes gradually as conditions change. So it predicts offsets that grow *gradually* with merger properties — no sharp turn-on, because the modified-gravity response does not have an on-off threshold; it has a continuous dial. And no saturation ceiling, because the modified response does not freeze anything in at a fixed scale; it simply tracks the evolving matter distribution.

The MOND-EFE prediction for the offset-velocity relation is therefore a **smooth roll-off**: offsets that rise gently and continuously from zero as mergers get faster or more extreme, with no knee and no ceiling. Where dark matter predicts a scatter, MOND-EFE predicts a smooth curve — but a *smooth* one, gradual at the low-speed end rather than switching on abruptly.

### 6.4 The distinguishing feature: a sharp knee

Now the three predictions can be set side by side, and the distinguishing feature stands out.

**Event Density predicts a sharp knee.** Below the critical velocity, no offset; above it, the offset switches on abruptly and rises. The turn-on is a step, not a ramp, because defect formation is all-or-nothing: the merger either traps a defect or it does not, with nothing in between. This is the hallmark of a topological mechanism — windings are integers, and you either make one or you don't.

**ΛCDM predicts no knee at all** — not a sharp one, not a smooth one. It predicts a scatter of offsets with no clean dependence on speed, because the offset in each merger is governed by that merger's particular geometry rather than by any universal threshold.

**MOND-EFE predicts the opposite of a knee** — a smooth, gradual rise from zero, with offsets fading continuously toward zero as mergers slow, never switching off abruptly.

So the three frameworks are distinguished by the *character of the low-speed transition*. ED: a sharp switch-on at a specific speed. MOND-EFE: a gradual fade. ΛCDM: no systematic transition, just scatter. The presence or absence of a sharp knee — and, if present, the speed at which it sits — is the cleanest single discriminator among the three. Measure the offset-velocity relation across enough mergers to see whether there is a knee, and you have separated the topological mechanism from both of its rivals.

### 6.5 The framework comparison

The three predictions, compared on the three features of the offset-velocity relation:

| Feature | Event Density | ΛCDM (dark matter) | MOND-EFE (modified gravity) |
|---|---|---|---|
| **Threshold (low-speed turn-on)** | Sharp knee at ~150 km/s — offset switches on abruptly | No threshold — offset fades smoothly toward zero, governed case-by-case | No threshold — offset fades smoothly and gradually toward zero |
| **Scaling (mid-speed behavior)** | Clean near-linear growth with merger speed | No universal scaling — scatter, set by per-merger geometry | Smooth continuous growth, no clean universal line |
| **Saturation (high-speed behavior)** | Ceiling at ~860 kpc — offset stops growing | No ceiling — offset can grow without a built-in limit | No ceiling — offset tracks matter, no fixed cap |

Read down the Event Density column: knee, line, ceiling — a definite, structured shape. Read down the other two columns: smooth or scattered, with no built-in features. The three columns are three different, distinguishable predictions for the same measurable relation.

### 6.6 Why this matters for the merging-cluster dark-matter question

The dark-matter debate has, for two decades, leaned heavily on the Bullet. The argument runs: here is a system where the gravity is plainly separated from the gas, so the gravity must be sourced by something invisible that travels with the galaxies — and that something is dark matter. The argument is clean, and it convinced most of the field.

But it rests on examining a single system. And a single system, as Section 6.0 noted, cannot distinguish three mechanisms that all reproduce it. The Bullet is evidence that the gravity separates from the gas; it is *not* evidence for any particular reason the separation happens. Dark matter, modified gravity, and substrate defects all separate the gravity from the gas. The Bullet does not choose.

The choice emerges only when you stop looking at one merger and start looking across *many*. The three mechanisms make their living in different places: dark matter in the case-by-case diversity of individual systems, modified gravity in the smooth continuity of its response, and the topological defect in the sharp, structured shape of the offset-velocity relation. These differences are invisible in any single system and unmistakable across a population.

The offset-velocity relation — measured across the full catalog of merging clusters, fast and slow, recent and not — is therefore the sharpest available test of the underlying physics of the merging-cluster dark-matter question. It is a test the field has not yet run, because the framing has been "does the Bullet show dark matter?" rather than "what shape does the offset-velocity relation take?" The arc reframes the question into one that can actually distinguish the candidates.

### 6.7 Consolidated statement

All three frameworks — dark matter, modified gravity, and the substrate topological defect — reproduce the Bullet Cluster, so the Bullet alone cannot choose among them. They diverge only across a population of mergers, where each predicts a different shape for the relationship between merger speed and lensing-gas offset: dark matter predicts a scatter with no clean relation, modified gravity predicts a smooth gradual roll-off, and Event Density predicts a structured shape with a sharp knee at a threshold speed, near-linear growth above it, and a ceiling at the freeze-out scale. The sharp knee is the decisive feature — a step-like turn-on that the topological mechanism requires and that neither rival produces. Measuring the offset-velocity relation across many merging clusters would reveal which shape nature actually traces, and so would distinguish, for the first time, among three explanations that the Bullet alone leaves tied. That measurement is the test the arc proposes, and it is the sharpest test available for the merging-cluster dark-matter question.

### 6.8 Implications for Section 7 — Open Items, Phase-3 Program, and the Broader ED Dark-Matter Account

Section 6 has stated the arc's central claim in its strongest form: a measurable, falsifiable prediction that distinguishes the topological-defect mechanism from both of its rivals. This is where the synthesis has been heading. But two things remain to be said honestly before the paper closes.

First, the prediction rests on a closure that is not yet airtight. Two ingredients in the numerical derivation — flagged throughout — are physically motivated but not fully derived, and they affect the precision of the numbers (where exactly the knee sits, how high the ceiling is). Section 7 states these open items plainly, so that a reader knows what is established and what is still to be earned.

Second, the prediction is a program, not yet a result. The offset-velocity relation has not been measured across a population of clusters; the test is proposed, not performed. Section 7 lays out what that observational program would involve — which clusters to measure, what to look for, and how the three falsifiers of Section 2 map onto specific observations.

And finally, the Bullet arc does not stand alone. It is one piece of a larger Event Density account of the phenomena usually attributed to dark matter — alongside the derivation of the galaxy-rotation acceleration scale and the reading of the "dark-matter-free" galaxies DF2 and DF4. Section 7 places the Bullet arc in that broader context, showing how the same substrate, read in different regimes, accounts for the full range of dark-matter evidence without a dark-matter particle. With those three things said — the open items, the observational program, and the broader account — the synthesis is complete.

---

*End of Section 6. The central prediction is stated and distinguished from both rivals by the sharp knee. Section 7 below addresses open items, the Phase-3 program, and the broader ED dark-matter account.*

---

## 7. Open Items, Phase-3 Program, and the Broader ED Dark-Matter Account

### 7.1 The two open items, stated plainly

A synthesis paper owes its reader an honest ledger of what is established and what is not. The Bullet arc rests on a chain of reasoning — topology, dynamics, numbers — that is, in its structure, complete. But two links in the numerical chain are physically motivated estimates rather than fully derived results, and it is worth naming them clearly.

**The first open item is the super-linear shock response.** When two clusters collide, the gas piles up and compresses at the interface, and the substrate's organizational density rises there. How much it rises is the question. The gas compression itself is well understood — a strong shock compresses gas by about a factor of four, no more. But the arc's numbers depend on the substrate's organizational density rising by considerably more than that — on the substrate responding *super-linearly* to the rapid reconfiguration. If it does, the relaxation time comes out to about a billion years and the critical velocity to about 150 km/s, the values used throughout. If the substrate responds only linearly, the relaxation time is longer — closer to ten billion years — and the critical velocity drops to about 15 km/s. This single question controls the *exact values* of the relaxation time and the critical velocity.

**The second open item is the two-timescale core/dressing structure.** The arc uses two different clocks: a slow one (the relaxation time, about a billion years) that sets the critical velocity and the observable lifetime, and a fast one (the time for the defect's core to respond) that sets the freeze-out separation. These differ because the defect is held together by the cluster's own structure rather than being a self-contained object — the same core-versus-dressing distinction that explained, in Section 4, why a permanent winding has a fading signal. The picture is consistent and it matches the dynamics, but the detailed mechanism by which the cluster stabilizes the defect has not been fully worked out. This question controls why the freeze-out scale and the critical velocity are governed by different clocks.

The essential point about both items: **they affect precision, not the qualitative predictions.** Whichever way they resolve, the offset-velocity relation still has its three-regime shape — a threshold, a linear rise, a ceiling. The *knee still exists*; the open items only shift exactly where it sits (somewhere between 15 and 1500 km/s) and exactly how high the ceiling stands. The distinction from dark matter and modified gravity — the presence of a sharp knee at all — survives regardless. And there is a reassuring wrinkle: if the relaxation time turns out to be the longer value, the predicted number of visible Bullet-like systems actually improves its agreement with what is observed. The arc is robust to the outcome.

Resolving these two items — deriving the substrate's shock response and the defect's stabilization from first principles — is the natural target for the next round of theoretical work. They would turn the arc's order-of-magnitude numbers into precise ones, sharpening the prediction without changing its character.

### 7.1a Phase-3 update: the two items reduced, and the deeper honesty point (a crystal/knot clarification)

Subsequent theory work sharpened the ledger above and, more importantly, located the arc's real assumption precisely. Two updates a careful reader is owed:

**The two open items reduce to one.** The dynamic side (the shock response, which sets the relaxation time and hence the threshold) is fixed: the substrate's organizational relaxation is dissipative and non-conserved, i.e. Hohenberg–Halperin Model A, with dynamic exponent *z ≈ 2*, inherited from the derived GR-III relaxational rule rather than assumed. The two-timescale core/dressing structure is resolved structurally: the defect is an *externally-pinned texture* (no self-consistent vacuum mass gap), so its microscopic core clock and macroscopic relaxation clock are independent by construction. What remains is a single number, the static exponent *ν* of the organizational transition, which pins the knee's location; under the flagged 3D O(3) value *ν ≈ 0.70* the knee sits near the working *v*_crit ≈ 150 km/s.

**The ordered field is an explicit layer-2 assumption, and that is the honest status — but it does not weaken the knot.** The mechanism assumes a cluster-scale organizational field that is ordered on *S²* and supports protected monopoles. Direct probing of the certified substrate microrule finds no emergent long-range *correlation*-order in any sector: the rule has only common-cause coherence in the sectors it is blind to and short-range stiffness in the sector it reads, and no ordering coupling anywhere (the "blindness invariant"). So the ordered *S²* field does not emerge from the certified primitives; it is a coarse-grained (layer-2) assumption. Crucially, **this is not a strike against the mechanism**, because a topological defect is a *knot*, not a *crystal*: a protected winding on a target space with nontrivial homotopy (π₂(*S²*) = ℤ) is categorically different from correlation-based order and lives in a different layer. It requires the field to be *S²*-valued, a quench to freeze a winding, and topology to protect it — none of which is long-range correlation. The correlation-negatives therefore measure the wrong observable for a knot and do not bear on it. The honest position: the ordered field is an assumed layer-2 object, the knot is a topological phenomenon at that layer, and the **observational offset–velocity test is the arbiter** — the microrule was never expected to grow the ordered field, and its failure to do so is not evidence against the defect.

### 7.2 The Phase-3 observational program

The arc's prediction is a curve, and a curve is tested by measuring many points on it. The observational program is therefore straightforward to state, if demanding to execute: **measure the lensing-gas offset and the merger velocity for as many merging clusters as can be characterized, and plot one against the other.**

Each of the arc's three falsifiers maps onto a specific feature of that plot.

**F1 — Does the offset-velocity relation have a knee?** This is the first and most basic test. Plot offset against merger speed across the catalog. Event Density predicts a flat stretch at low speeds (no offset), then a bend, then a rise. Dark matter predicts a scatter with no clean relation; modified gravity predicts a smooth curve with no bend. The mere *presence* of a knee — a place where the relation visibly changes character — would favor the topological mechanism over both rivals. Its absence would challenge the arc.

**F2 — Is the turn-on sharp or smooth?** If there is a knee, its character matters. Event Density predicts a *sharp* turn-on — a step, because defect formation is all-or-nothing. Modified gravity, if it produced any bend at all, would produce a *gradual* one. So the sharpness of the transition, measured by sampling mergers at speeds near the threshold, separates the topological mechanism (sharp) from modified gravity (smooth). This is the cleanest single discriminator, and the one that most directly tests the topological character of the mechanism.

**F3 — Does the offset saturate, and do the fastest mergers show multiple peaks?** At the high-speed end, Event Density predicts the offset levels off at the freeze-out scale, and that the very fastest collisions may trap more than one defect pair, showing more than two offset peaks. Dark matter and modified gravity predict no such ceiling and no such multiplicity. Sampling the rarest, fastest mergers — the kind future wide-area surveys will turn up in greater numbers — tests this regime.

The unifying theme is the one Section 6 insisted on: **the Bullet alone cannot decide.** No single merger, however clean, distinguishes mechanisms that all reproduce it. Only the *pattern across the catalog* — the shape of the offset-velocity relation, traced by many systems at many speeds — carries the distinguishing information. The program is not "examine the Bullet more closely"; it is "examine the population, and read its shape."

### 7.3 How the Bullet mechanism fits the broader ED dark-matter account

The Bullet arc is not a standalone curiosity. It is the third of three independent pieces by which Event Density accounts for the phenomena usually attributed to dark matter — and the three pieces reinforce one another, because they arise from the same substrate physics expressed under different conditions.

**The first piece is the universal acceleration scale, a₀.** Ordinary galaxies rotate too fast at their edges; the standard fix is a dark-matter halo around each one. Event Density instead derives a universal acceleration scale, a₀ = cH₀/(2π) — the cosmological horizon expressed as an acceleration — below which the substrate's outer reach makes itself felt as extra effective gravity. This is the substrate's *steady-state* response: a calm, settled galaxy sitting in the substrate's outer-scale field, with the "missing gravity" appearing wherever the local acceleration drops below a₀. It explains the rotation curves of ordinary galaxies without a halo.

**The second piece is the DF2/DF4 suppression.** Two galaxies famously *lack* the dark-matter-like behavior — they rotate exactly as their visible mass alone predicts. In the standard picture this is a puzzle (why would two galaxies form without halos?). In Event Density it is expected: both galaxies sit deep inside a massive group, where the group's gravity overpowers the substrate's gentle outer-scale contribution. The universal a₀ effect is still present but locally drowned out — like a candle in a sunlit room. This is the substrate's *environmental* response: the same outer-scale physics, suppressed where a strong local field dominates.

**The third piece is the Bullet mechanism developed in this paper.** Here the substrate's response is neither steady-state nor merely environmental but *dynamical*: a violent merger drives the substrate through a quench, trapping a topological defect whose gravity is offset from the gas. This is the substrate's response to *rapid change* — the regime that the steady-state and environmental pieces do not reach.

Three regimes, one substrate. A settled galaxy shows the steady-state a₀ enhancement. A galaxy in a dense environment shows that enhancement suppressed. A cluster caught in a fast merger shows a frozen-in dynamical defect. The galaxy-rotation evidence, the dark-matter-free galaxies, and the Bullet Cluster — three of the headline pieces of "dark matter evidence" — are, in this account, three faces of the same substrate physics, read under steady, suppressed, and dynamical conditions respectively. **None of the three requires a dark-matter particle.** They require the substrate to have an outer scale (a₀), to be locally overpowerable (DF2/DF4), and to trap defects when rushed (the Bullet). Those are properties of one substrate, not three separate hypotheses.

This is what makes the Bullet arc more than a single clever explanation. It is the dynamical corner of a unified account — the piece that shows the same substrate physics reaching even into the most-cited evidence for the particle it dispenses with.

### 7.4 The arc in one page

The Bullet Cluster shows its gravity offset from its gas, and this has stood for two decades as the clearest evidence that dark matter exists. Event Density reads the offset differently: not as a particle traveling with the galaxies, but as a topological defect frozen into the substrate's organizational field. The substrate's state at cluster scales is a field of directions, and that field can wrap an integer number of times around a point in space — a winding that cannot be smoothed away, a "monopole." A fast cluster merger drives the field through a quench, trapping such windings, and because the total winding must stay zero, they appear in monopole-antimonopole pairs — two opposite windings, which are the Bullet's two offset lensing peaks. Each defect drifts with its cluster's collisionless galaxies rather than the ram-stripped gas, which is why the gravity sits with the galaxies; the pair is carried apart too fast to annihilate; and its visible signal fades over about a billion years as the field around it relaxes, even though the winding itself is permanent — which is why we see the Bullet bright and young while older mergers have gone quiet. Closing the numbers from the substrate's own scales gives a defect-forming threshold near 150 km/s, a peak-separation scale near 860 kpc that matches the Bullet's observed 700, and a three-regime relationship between merger speed and offset: no offset below the threshold, growth above it, a ceiling at the freeze-out scale. That relationship — a sharp knee, a linear rise, a flat ceiling — is a shape that neither dark matter nor modified gravity predicts, and measuring it across many merging clusters would distinguish the three for the first time. The Bullet, in this account, is not just explainable; it is predictable — and the prediction can be proven wrong.

### 7.5 Closure statement

With this section, the Bullet_Arc synthesis is complete. The three Phase-2 deliverables — the topology of the order parameter, the dynamics of the defect pair, and the numerical closure from substrate primitives — are here integrated into a single account, written to be read without the technical derivations and to be cited as the arc's statement of record.

What the reader should take away is three things.

First, **the Bullet's offset is not merely explainable but predictable.** Many frameworks can accommodate a single system after the fact; the value of this account is that it predicts a specific, structured relationship between merger speed and offset across the whole population of merging clusters, derived from the substrate's own fundamental scales rather than fitted to the Bullet.

Second, **the prediction is falsifiable.** It can be proven wrong — by the absence of a knee, by a smooth rather than sharp turn-on, by an offset that grows without a ceiling. A prediction that can be proven wrong is the kind worth making, and the kind that distinguishes a physical mechanism from an accommodation.

Third, **the next step is observational.** The theory has done what theory can do: it has produced a sharp, testable prediction and located the measurement that would decide it. What remains is to make that measurement — to gather the offsets and velocities of many merging clusters and read the shape they trace.

The Bullet has been read for twenty years as the answer to the dark-matter question. The arc proposes that it has instead been the wrong question, cleanly answered: not "does the Bullet prove dark matter?" but "what shape does the offset-velocity relation take?" That shape is waiting in the data of the merging-cluster catalog, and reading it is the work of Phase-3.

---

*End of Section 7. End of the Bullet_Arc synthesis. Phase-2 is complete; Phase-3 is the observational program that tests the prediction.*

---

## Synthesis Closure Summary

**Paper:** *The Bullet Cluster as a Substrate Topological Defect: An Event Density Synthesis*
**Arc:** Bullet_Arc (ED-Bullet-01) — Phase-2 Synthesis
**Status:** **COMPLETE**
**Sections:** 1–7; ~12,000 words; accessible synthesis level
**Integrates:** D2.1 (topology), D2.2 (dynamics), D2.3 (numerical closure)

**Principal statement:**
The Bullet Cluster's gravitational-baryonic offset is read as a topological defect — a monopole-antimonopole pair on the substrate's *S²* organizational order parameter (π₂(*S²*) = ℤ), frozen in by the merger's Kibble-Zurek quench. Conservation forces the two-peak structure; advection places the defects with the galaxies and offset from the gas; the signal fades on the relaxation time (~10⁹ yr) while the charge persists. Numerical closure gives v_crit ~ 150 km/s, ξ_KZ ~ 860 kpc, and a three-regime offset-velocity law whose sharp-knee shape distinguishes the mechanism from ΛCDM (scatter) and MOND-EFE (smooth roll-off). The Bullet alone cannot decide among the three; the offset-velocity relation across the merging-cluster population can. Two open ingredients (super-linear shock response; two-timescale core/dressing structure) affect precision, not the qualitative prediction. The Bullet mechanism is the dynamical third of a unified ED dark-matter account, alongside the steady-state a₀ scale and the environmental DF2/DF4 suppression — three regimes of one substrate, none requiring a dark-matter particle.

**Phase-2 status: COMPLETE.**
- D2.1 — Vacuum Manifold ✓
- D2.2 — Winding Number ✓
- D2.3 — Relaxation Time ✓
- Synthesis — this paper ✓

**Remaining:**
- Memo_02 — Phase-2 integration (corpus cross-reference, dependency graph update)
- Phase-3 — observational program (offset-velocity relation across the merging-cluster catalog)
- Possible: combined ED dark-matter paper (a₀ + DF2/DF4 + Bullet) for standalone publication

---

*End of paper.*
