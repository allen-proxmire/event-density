# What Is Event Density?

## The Ontology

Event Density (ED) is a constitutive ontology. It posits that the fundamental quantity is the local rate of becoming — a bounded scalar field representing the density of micro-events at each point in space and time. From this single primitive, three constitutive channels emerge:

- **Mobility.** How density redistributes. Transport is density-dependent: it slows as the field approaches its capacity bound and halts at the maximum, creating horizons and compact-support fronts.
- **Penalty.** How density relaxes. A monostable restoring force drives the field toward a unique equilibrium, producing exponential decay.
- **Participation.** How the system oscillates. A global variable, driven by the domain-averaged operator and feeding back uniformly, produces telegraph oscillations.

## The Seven Axioms

The canonical PDE is derived — not postulated — from seven structural principles:

| Axiom | Constraint |
|:------|:----------|
| P1 Locality | Operator depends only on local values and derivatives |
| P2 Isotropy | No preferred spatial direction |
| P3 Gradient-driven flow | Flux is proportional to gradient with state-dependent mobility |
| P4 Dissipative structure | A Lyapunov functional decreases along all solutions |
| P5 Single scalar field | One real-valued field, not a vector or tensor |
| P6 Minimal coupling | The global mode couples additively with minimal structure |
| P7 Dimensional consistency | Constitutive functions are independent of spatial dimension |

These seven axioms uniquely determine the canonical PDE. No other second-order scalar PDE satisfies all seven.

## The Canonical PDE

The ED system on a bounded domain is:

∂ₜρ = D [ ∇·(M(ρ)∇ρ) − P(ρ) ] + Hv,    v̇ = (F̄ − ζv)/τ

with M(ρ) = M₀(ρ_max − ρ)^β and P(ρ) = P₀(ρ − ρ*).

Each channel, isolated, corresponds exactly to a known physical law: the penalty is an RC circuit (exact to machine precision), the mobility is the porous-medium equation (exact reduction), and the participation is a telegraph oscillator (exact to machine precision).

## The Generalised Mobility

For galaxy-scale applications, the mobility is extended to M(ρ) = ρ^α (ρ_max − ρ)^β, where α suppresses transport at low density (steepening the outer halo) and β suppresses transport at high density (widening the core). The canonical ED (α = 0) is a special case.

## Condensed-Matter Mapping

The mobility law D(c)/D₀ = (1 − c/c_max)^β fits three chemically distinct materials — hard-sphere colloids (steric jamming), sucrose-water (H-bond viscosity), and BSA protein solutions (hydrodynamic crowding) — with R² > 0.98 and a mean β = 2.00 ± 0.29. The front-propagation exponent α_R = 1/(dβ + 2) is confirmed to 2.3% in 1D and 0.02% for the peak-decay exponent in 3D.

## Galaxy-Scale Mapping

The ED PDE coupled to the Poisson equation produces halo profiles with naturally widened cores that match observed Burkert core radii to within 10% for four dwarf galaxies. The generalised mobility (α = 0.5, β = 2) produces density profiles matching Burkert to 99.6%.

For massive spirals, the gravity-only model overshoots the flat rotation curve. Adding the temporal-tension channel resolves this, reproducing NGC 3198's rotation curve with RMS = 1.9 km/s.

## Temporal Tension and Weak Lensing

The participation channel, interpreted at galactic scales, generates a temporal-tension field that extends to megaparsec radii. This predicts indefinitely flat circular velocities — consistent with Mistele et al. (2024), who measured flat V ≈ 135 km/s from 34 kpc to 1 Mpc.

## The Baryonic Tully-Fisher Relation

The BTFR is derived as a temporal-tension amplitude scaling law: V_temp = (G·a_ED·M_b)^(1/4). The measured exponent n = 0.246 ± 0.025 matches the prediction of 1/4 exactly and rejects the ΛCDM virial prediction of 1/3 at > 3σ. The ED acceleration scale a_ED = 2.1 × 10⁻¹⁰ m/s² is within a factor of 1.8 of Milgrom's a₀.

## Two ED-Unique Predictions

1. **Activity dependence.** At fixed baryonic mass, galaxies with higher star-formation rates should have higher V_temp (ΔV ~ 30–70 km/s). Neither MOND nor ΛCDM predicts this.

2. **Merger lag.** During a merger, the temporal-tension field lags behind the baryonic mass by 15–45 kpc — the opposite direction from the ΛCDM Bullet Cluster offset. Neither MOND nor ΛCDM predicts this.

---

**Next:** [Core Papers](CORE_PAPERS.md) · [Results Overview](RESULTS_OVERVIEW.md) · [How to Run](HOW_TO_RUN.md) · [Repo Structure](REPO_STRUCTURE.md)
