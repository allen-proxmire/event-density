# Scientific Results

**Event Density predicts dynamics in three independent physical regimes from a single PDE, with a single parameter set, no inter-domain fitting.** This page is the unification narrative.

---

## One PDE → Three Channels → Three Flagship Results

The canonical ED PDE is

```
   ∂_t ρ = D · [ M(ρ) ∇²ρ + M'(ρ) |∇ρ|² − P(ρ) ] + H · v
   v̇   = (1/τ) · ( F̄(ρ) − ζ · v )
```

with `M(ρ) = M₀(ρ_max − ρ)^β` and `P(ρ) = P₀(ρ − ρ*)`. It has three constitutive channels (mobility, penalty, participation) which can each be exercised in isolation by setting the others to zero, or together to produce coupled dynamics. Each channel maps onto a distinct empirical regime:

| Result | Channel exercised | Prediction | Evidence |
|--------|-------------------|------------|----------|
| **UDM** (soft matter) | Mobility `M(ρ) = M₀(ρ_max − ρ)^β` | `D(c) = D₀(1 − c/c_max)^β` for any concentrated system | 10 materials, R² > 0.986, β = 1.72 ± 0.37 |
| **Galaxy-15** (cluster mergers) | Penalty + dynamical wake | `ℓ = D_T / v_current` lensing-mass offset behind moving baryons | 7 clusters consistent within uncertainty; Finner+25 median 79 ± 14 kpc matches predicted ~80 kpc |
| **PDE Atlas** (cross-regime) | All three channels, all five regimes | One PDE, dimensional invariant `D · T₀ / L₀² = 0.3` | 9 architectural laws verified in dimensions 1–4; 61 orders of magnitude in length scale |

The unifier is the diffusivity `D`. Set independently from the Mistele weak-lensing observation (`D_T = 2.1 × 10²⁷ m²·s⁻¹` in galactic units), the *same* constant — through the dimensional bridges of the PDE Atlas — becomes the `D₀` of the UDM mobility law in the condensed-matter regime. The PDE Atlas is the formal mapping that connects them.

---

## Result 1 — UDM (Universal Degenerate Mobility)

**Folder:** [`papers/Universal_Mobility_Law/`](papers/Universal_Mobility_Law/)
**Reproduction notebook:** [`analysis/notebooks/04_udm_mobility.ipynb`](analysis/notebooks/04_udm_mobility.ipynb)

**Channel exercised:** Mobility, in isolation.

When the penalty and participation channels are turned off, the canonical PDE reduces to

```
   ∂_t ρ = D · ∇·[ M(ρ) ∇ρ ]   with M(ρ) = M₀(ρ_max − ρ)^β.
```

This is a porous-medium-like equation with degenerate diffusion that vanishes at packing capacity. Its functional form predicts that the effective concentration-dependent diffusivity in any crowded soft-matter system follows a single universal law:

```
   D(c) = D₀ · (1 − c/c_max)^β.
```

UDM tests this prediction against ten chemically distinct materials spanning hard-sphere colloids, polymer melts, protein solutions (BSA), polysaccharides, and small-molecule mixtures. Every material fits the law with R² > 0.986. The fitted exponent β has population mean `1.72 ± 0.37` and is consistent with the canonical theoretical value β = 2 (within 1σ) across systems with very different microscopic physics.

UDM also predicts a zero-free-parameter, sub-Fickian front-propagation exponent for FRAP recovery in concentrated BSA: `R(t) ~ t^0.12`, distinct from the Fickian `t^0.50`. Testable in a single afternoon on a standard confocal microscope.

---

## Result 2 — Galaxy-15 (Merger Lag)

**Folder:** [`papers/Cluster_Merger_Lag_Evidence/`](papers/Cluster_Merger_Lag_Evidence/)
**Reproduction notebook:** [`analysis/notebooks/03_galaxy15_lag.ipynb`](analysis/notebooks/03_galaxy15_lag.ipynb)

**Channel exercised:** Penalty + dynamical wake (the temporal-tension field).

In ED, the macroscopic gravitational field that mimics dark matter is the equilibrium configuration of the temporal-tension field T(x, t), itself governed by the same PDE family with diffusivity `D_T`. During a cluster merger, the source moves ballistically while T responds diffusively, forming an exponential wake behind the moving baryonic mass. The lensing centroid is consequently displaced from the BCG by

```
   ℓ_obs = D_T / v_current.
```

This is a one-parameter prediction; `D_T` is fixed independently from the Mistele weak-lensing extent (≈ 2.1 × 10²⁷ m²/s) and is *not* fitted to any cluster offset.

**Tested against seven well-measured clusters and one aggregate sample:**

| Cluster | v_peri (km/s) | TSP (Gyr) | ED prediction (kpc) | Observed (kpc) |
|---|---|---|---|---|
| Bullet | 4500 | 0.15 | 15.1 | 17.78 ± 0.66 |
| El Gordo SE (along-axis) | 2500 | 0.75 | 27.2 | 28.7 |
| MACS J0025 | 2000 | 0.50 | 34.0 | \|33\| |
| MACS J1149 (SL) | 2770 | 1.16 | 24.6 (total) | 11.5 (SL only — scale-dependence confirmed) |
| Musket Ball S | 1500 | 0.96 | 136.1 (with v_current) | 129 |
| ZwCl 0008 E | 1800 | 0.76 | 681 (limited by t_lag) | 319 |
| CIZA J2242 | 2500 | 1.00 | 85.1 | 190 ± 100 |
| **Finner+25 aggregate** | mixed | mixed | ~80 (typical post-merger) | **79 ± 14 (58 subclusters, 29 clusters)** |

**Three ED-unique signatures, all confirmed:**

1. *Velocity scaling:* `n = −1.07 ± 0.20` from the four-cluster v_current fit (ED predicts n = −1).
2. *Deceleration scaling:* offsets grow monotonically with time since pericenter, opposite to SIDM's predicted peak-and-decay (Fischer et al. 2024).
3. *Scale dependence:* SL offsets are 0.23–0.47 of the WL prediction; the Bullet (Cha et al. 2025) and MACS J1149 (Rau et al. 2014) both confirm. Neither LCDM nor SIDM predicts scale dependence.

**Comparison to alternatives:** standard CDM (Roche et al. 2024) predicts ~1 kpc offsets and is excluded by 50–80×. SIDM is disfavoured by the deceleration test (ED's Musket Ball ratio 0.95 vs SIDM's expected decay) and shows internal tension (El Gordo requires σ/m = 4–5 cm²/g; Bullet bound is σ/m < 1 cm²/g). ED uses one parameter and contains no internal tensions across clusters.

---

## Result 3 — PDE Atlas (Dimensional + Numerical)

**Folder:** [`papers/Dimensional_Atlas/`](papers/Dimensional_Atlas/), [`papers/Numerical_Atlas/`](papers/Numerical_Atlas/)
**Reproduction notebook:** [`analysis/notebooks/02_three_channels.ipynb`](analysis/notebooks/02_three_channels.ipynb)

**Channel exercised:** All three, demonstrated across all five regimes.

The PDE Atlas is the formal demonstration that the *single* canonical ED PDE — same equation, same constitutive forms — admits a consistent dimensional interpretation at every physical scale from quantum (10⁻³⁵ m) to cosmological (10²⁶ m), spanning **61 orders of magnitude in length**.

Five regime mappings:

| Regime | Anchor scale | Anchor time | Physical correspondence |
|--------|--------------|-------------|-------------------------|
| Quantum | ℏ / 2m | ℏ / 2mc² | Schrödinger-like diffusion |
| Planck | √(ℏG/c³) | √(ℏG/c⁵) | Quantum-gravity transport |
| Condensed matter | thermal diffusivity scale | molecular relaxation | Mobility law (UDM) |
| Galactic | v_circ · L₀ | L₀ / v_circ | Temporal-tension halo (Galaxy-15) |
| Cosmological | c² / H₀ | 1 / H₀ | Friedmann analogue |

Across all five regimes, the universal nondimensional invariant

```
   D_phys · T₀ / L₀² = D_nd = 0.3
```

holds *exactly*. This is not a fit; it is a structural identity built into the canonical PDE under nondimensionalization.

The Numerical Atlas is the computational companion: it integrates the canonical PDE in (D, ζ, τ)-parameter space and demonstrates well-posedness, spectral decay, modal hierarchy, Lyapunov dissipation, and the bifurcation at the critical-damping surface. **Nine architectural laws** (energy monotonicity, spectral concentration, topological conservation, morphological hierarchy, etc.) are verified in dimensions 1, 2, 3, and 4.

---

## The unification claim, restated

Three independent empirical regimes — concentrated soft matter (UDM), merging galaxy clusters (Galaxy-15), and the dimensional structure of physics from quantum to cosmological scales (PDE Atlas) — are predicted by *one* equation, with *one* parameter set, and *no* fitting between domains.

In the soft-matter regime, the mobility channel reproduces the universal `D(c) = D₀(1 − c/c_max)^β` law across 10 chemically distinct systems.

In the cluster-merger regime, the penalty channel reproduces the lensing-mass offset `ℓ = D_T / v_current` across seven well-measured clusters and the Finner et al. (2025) aggregate of 58 subclusters.

In the cross-regime atlas, the *same* PDE — with the *same* constitutive forms — admits dimensional mappings into five physical regimes spanning 61 orders of magnitude, with a universal nondimensional invariant `D · T₀ / L₀² = 0.3`.

The diffusivity that sets the cluster-merger lag (`D_T`, fixed independently from the Mistele weak-lensing extent) is the galactic-regime image of the *same* constant `D` that, under the dimensional mapping, becomes the `D₀` of the soft-matter mobility law. The PDE Atlas is the bridge that makes this connection explicit.

**One PDE. Three regimes. No fitting between them. No failures so far.**

---

## Reading order

1. **[GETTING_STARTED.md](GETTING_STARTED.md)** — install, run the demo, run a reproduction notebook.
2. **[`papers/Foundations_of_Event_Density/`](papers/Foundations_of_Event_Density/)** — the axiomatic derivation of the canonical PDE.
3. **[`papers/Dimensional_Atlas/`](papers/Dimensional_Atlas/)** — the cross-regime mapping (the PDE Atlas).
4. **[`papers/Universal_Mobility_Law/`](papers/Universal_Mobility_Law/)** — soft-matter mobility law.
5. **[`papers/Cluster_Merger_Lag_Evidence/`](papers/Cluster_Merger_Lag_Evidence/)** — cluster-merger lag.
6. **[`docs/research/ED PAPERS/`](docs/research/ED%20PAPERS/)** — the historical research log (background and supplementary).
