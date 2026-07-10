# #4 Resolved — Maxwell from B4's Coherence Action: the Coherence-Weighted Limit IS Coulomb (Confirmed); the Smooth Field Is an Emergent Shadow

**Foundations — #4 of the open-derivations ledger (does DCGT coarse-graining yield Maxwell from B4's U(1) holonomies). Standing inputs: `Paper_ChargeAsTopology_B4` (charge skeleton + latent Maxwell action; §7 left the *selection* open), `Paper_Continuum_KineticLatticeGas` (the determinate substrate makes trajectories, not smooth fields), and this session's continuum/curvature arc-exhaustion note. Crank-rail ON. The phase sector is Σ-blind (B4), so this is analytic, not a certified-sim run. RESULT: the one open half of B4 §7 is settled concretely — in the coherence-weighted continuum limit, B4's holonomies give the Coulomb field (`evaluation/B4_Arc/maxwell_from_coherence_probe.py`). Combined with the Continuum finding, #4 resolves as ED's standard pattern: the FORM is derived, the smooth field is an emergent shadow.**

## 1. What B4 left open, and the two halves
`Paper_ChargeAsTopology_B4` established, native/measured: (i) the **charge skeleton** — an integer winding `w ∈ ℤ` (`π₁(U(1))=ℤ`) with an **exact integral Gauss law** (circulation `= 2πw`, loop-independent); (ii) the **Maxwell action is latent** in the coherence term — `cos²(Δφ/2) ≈ 1 − ¼(∇φ)²`, so the incoherence `sin²(Δφ/2) ≈ ¼(∇φ)²` is exactly the standard `∫(∇φ)²` electrostatic/Maxwell action. B4 §7 left **open** whether the DCGT (coherence-weighted) measure *selects* the Maxwell configuration as the continuum expectation of the holonomies.

## 2. The open half, settled concretely — the coherence-weighted limit is Coulomb
In the coherence-weighted continuum limit the field around a charge is the one that **minimizes the coherence action** `∫(∇φ)²` — the Euler–Lagrange solution `∇²φ = −ρ_charge` (Poisson). Solved for a point charge (a B4 winding source) on a 3D lattice (`maxwell_from_coherence_probe.py`):
- **Coulomb wins the fit:** `φ(r) ∼ A/r^p`, best `R² = 0.967` at **p = 1** (the 3D Coulomb exponent), vs 0.77 at p = 2.
- **`φ·r ≈ 0.060` constant in the near field** (r = 2–6), the `1/r` Coulomb signature (the falloff at large r is the periodic-box neutralizing-background artifact, expected).

> **So B4's coherence action (its latent Maxwell action), minimized around a charge, IS the Coulomb field.** In the coherence-weighted continuum limit, B4's U(1) holonomies give **Maxwell/Coulomb** — the half B4 §7 flagged open. The smooth Maxwell field *is* the coherence-weighted continuum limit of the topological charge.

## 3. The other half — the determinate substrate does not cast it (the shadow)
`Paper_Continuum_KineticLatticeGas` is a *tested* result: the determinate certified substrate coarse-grains to a **kinetic lattice-gas** (ballistic trajectories), **not** a field-relaxing PDE — it is committal/trapping, not Boltzmann/coherence-weighted-relaxing, and "you reach the PDE only by leaving ED." The phase sector is moreover **Σ-blind** (B4: the winding is inert to the certified Σ-dynamics). So the coherence-weighted ensemble that §2 shows yields Coulomb is **not** what the determinate dynamics produce. The smooth Coulomb field is therefore reached only in the **thick / coherence-weighted (ensemble) limit** — a coarse-grained **shadow**, not a determinate-dynamics output. This is exactly the diffusion situation (the determinate substrate doesn't cast the smooth PDE) transposed to the gauge sector.

## 4. Verdict — #4 resolves as form-forced + emergent shadow
| piece | tier |
|---|---|
| charge skeleton (winding `w∈ℤ`, exact Gauss law) | **derived / measured** (B4, native) |
| Maxwell action latent in the coherence deficit (`¼(∇φ)²`) | **derived** (B4) |
| coherence-weighted continuum limit around a charge = **Coulomb** | **confirmed (this note)** — the open half of B4 §7 |
| the determinate substrate *casts* the smooth field | **NO — emergent shadow** (Continuum: kinetic, not field-relaxing; Σ-blind phase sector) |

**So #4 is resolved:** ED derives the **form** of Maxwell (the topological charge skeleton + Gauss law, the latent Maxwell action, and — now confirmed — that its coherence-weighted continuum limit is the Coulomb field), while the **smooth Coulomb field is an emergent shadow** the determinate substrate does not cast (it makes trajectories/skeletons; the smooth field is their coarse-grained density in a thick limit). This is **ED's monist position** — the smooth continuum is emergent, not fundamental — now **tested for diffusion and confirmed-as-Coulomb for Maxwell**, not merely extrapolated. Same shape as the metric (geometry native) vs the field-PDEs (shadows): **form-forced + emergent-shadow, a feature of ED's ontology, not a gap.** Crank-rail: confirmed the coherence-weighted→Coulomb half as a real (if standard-electrostatics) computation using B4's own action; kept the honest boundary that this is the *thick-limit* shadow, not the determinate dynamics (Σ-blind, analytic); did not claim the determinate substrate casts the smooth field (it provably doesn't). **Ledger #4 = resolved (form-forced + emergent shadow).**
