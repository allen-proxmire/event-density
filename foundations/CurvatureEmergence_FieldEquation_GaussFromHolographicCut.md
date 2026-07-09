# The Newtonian Field Equation Is Forced by Bandwidth Conservation + the Holographic Cut: a Substrate Gauss's Law (the Same Count That Forces g~1/b)

**Foundations, gravity / curvature-emergence arc, the linear field-equation piece. The static half closed the *metric* (`g~1/b`, forced by the holographic cut, 3D-unique), but the foothold IMPOSED the bandwidth dip around a mass by hand, and Paper_027 recovers the Newtonian `1/r` by INHERITING a Coulomb-like `1/R` falloff from the V1 kernel (with the holographic count cancelling). Neither derives the `b(r)` profile / the field equation from the substrate. This note derives it. Probe: `evaluation/CurvatureEmergence/gauss_law_newtonian_probe.py`. Result: bandwidth conservation (P04) + the holographic surface-count (cut `N(R)~R^{d-1}`, the same count the reach law uses) give a substrate GAUSS'S LAW: a conserved influence `Q` spread across `N(R)` channels has per-channel flux (force) `= Q/N(R) ~ 1/R^{d-1}` (measured cleanly at `-(d-1)`: inverse-square `-1.999` in 3D), and its radial integral (the potential) `~ 1/R^{d-2}` (form-fit: `1/r` in 3D `R²=0.998`, `log` in 2D `R²=1.000`, `1/R²` in 4D `R²=1.000`). An independent full-lattice sparse solve of the conservative field equation (discrete Laplace, point source) on a real 3D lattice confirms the potential is `1/R` (`R²=0.998`, rejecting `1/R²` at `0.904`). So the `1/R` falloff Paper_027 inherits from the kernel is DERIVED from conservation + holography, and it is the SAME holographic count that forces `g~1/b`. Inverse-square force and the `1/r` potential are uniquely 3D. Tier: a layer-2 counting/conservation derivation of the FORM; `G`/`ℓ_P` inherited; the nonlinear MOND term is the separate interference cross-term.**

---

## 1. What was open

The curvature-emergence arc had closed the *kinematic metric*: a metric emerges from bandwidth-connectivity, and `g~1/b` is forced by the holographic channel-count in 3D (`CurvatureEmergence_ReachLaw_Derived_Holographic`). But two gaps remained on the way to *gravity around a mass*:

- **The foothold imposed the source profile by hand.** The metric measurement put a bandwidth dip on a background line (`bandwidth_field(...)`, a Gaussian dip) and read the metric off it. What *sets* the `b(r)` profile around a mass, the field equation, was never derived.
- **Paper_027 (Newton's `G`) inherits the `1/R`.** It recovers `Φ ∝ -M/R` and the inverse-square acceleration, but the `1/R` per-channel falloff is taken from the **V1 kernel's** Coulomb-like envelope (Paper #18 via DCGT), and the holographic count `N(R)=4πR²/ℓ²` **cancels** in the final potential. So the `1/R` is kernel-inherited, not derived from the substrate's geometry.

The open question this note answers: **can the `b(r)` profile / the Newtonian field equation be *derived* from bandwidth conservation + the holographic surface-count, grounding the kernel-`1/R` Paper_027 assumes, and using the same holographic ingredient that forces `g~1/b`?**

## 2. The argument: a substrate Gauss's law

- **P04, a mass's influence is conserved.** Bandwidth is additive/conserved; a localized mass is a single conserved substrate fact (a source of participation-influence `Q`), not something each channel carries a separate copy of (Paper_027 §4.3 makes the same "single substrate-source fact" point).
- **Holographic count, the channels threading a sphere.** The independent channels connecting the source to a shell at radius `R` number the boundary **cut** `N(R) ~ R^{d-1}` (the area-law-as-edge-count, `AreaLaw_FromStraddlingEdges` / Paper_025), the SAME surface-count the reach law uses.
- **Gauss's law.** A conserved influence `Q` distributed across `N(R)` channels gives a per-channel flux, the field strength (force):
$$F(R) = \frac{Q}{N(R)} \sim \frac{Q}{R^{\,d-1}}.$$
The potential is its radial integral,
$$\Phi(R) = \sum_{r\ge R} F(r) \sim \frac{1}{R^{\,d-2}} \quad (\log R \text{ in } d=2).$$

So **force `~ 1/R^{d-1}` (inverse-square only in `d=3`)** and **potential `~ 1/R^{d-2}` (Newtonian `1/r` only in `d=3`; `log` in 2D; `1/R²` in 4D)**, forced by {conservation + the holographic cut}. This is exactly the classical Gauss's-law dimension argument, but the surface it uses is ED's own holographic channel-count, and the conservation is P04.

Combined with the metric: for a mass, the bandwidth perturbation `δb(R)` is the accumulated influence `~ Φ(R) ~ 1/R` in 3D; since `g~1/b`, the metric perturbation `δg ~ -δb/b² ~ 1/R`, the Newtonian weak-field metric `g_{tt} ~ 1 + 2Φ`. The `b(r)` profile the foothold imposed is now derived: harmonic, `1/r` in 3D.

## 3. Probe results (`gauss_law_newtonian_probe.py`)

| `d` | cut `N~R^s` (exp `d-1`) | force `=1/N ~R^a` (exp `-(d-1)`) | potential form-fit `R²` |
|---|---|---|---|
| 2 | 0.985 (1) | -0.985 (`R²`=1.000) | 1.000 `[A log R + C]` |
| **3** | **1.999 (2)** | **-1.999 (`R²`=1.000)** | **0.998 `[A/R + C]`  ← inverse-square (Newtonian)** |
| 4 | 2.956 (3) | -2.956 (`R²`=0.999) | 1.000 `[A/R² + C]` |

**Independent full-lattice check (3D).** A direct sparse solve of the discrete Laplace equation (conservative steady-state spreading) with a point source on a real `45³` lattice, `φ=0` on the boundary: the radial potential fits `1/R + C` at `R²=0.9978` and *rejects* `1/R² + C` (`R²=0.9044`). The full-lattice conservative field equation gives the `1/r` Green's function, agreeing with the counting route, two independent computations landing on Newtonian `1/r`.

## 4. What this converts, and the relation to Paper_027

**Converted.** The foothold's imposed dip and Paper_027's kernel-inherited `1/R` become "**the `1/r` potential and inverse-square force are FORCED by bandwidth conservation + the holographic surface-count**." The `1/R` falloff is no longer an input (a hand-placed dip, or the V1 kernel's envelope); it is the substrate's own Gauss's law. And it uses the **same** holographic cut `N(R)~R^{d-1}` that forces `g~1/b`, so the metric and the field equation come from one ingredient.

**Relation to Paper_027 (complementary, deeper, not contradictory).** Paper_027 gets `1/R` from the V1 kernel and finds the holographic count *cancels*; this note gets `1/R` from the holographic count being the *source* (Gauss). These agree, and together they explain *why the V1 kernel falls off as `1/R` in 3D*: a retarded kernel's `1/R` envelope **is** the 3D Green's function, i.e., Gauss's law for a conserved flux through a holographic surface. So this grounds Paper_027's inherited kernel-falloff in conservation + geometry, and leaves Paper_027's `G = c³ℓ_P²/ℏ` identification (the *value*) untouched and inherited.

**A third face of "3".** The holographic surface-count now forces two GR-matching results, both uniquely in 3D: the metric `g~1/b` (reach law) and the inverse-square Newtonian law (this note). These are two consequences of one ingredient (the cut `~R^{d-1}`), not two independent selections, so this is strong internal coherence of the geometry (one holographic count, two GR features, same dimension), distinct from the *independent* linking selection of 3 (`ThreeDimensions_ConsolidatedReview`).

## 5. Honest scope

- **Layer-2 counting/conservation derivation.** The `1/r` potential is a coarse-grained (layer-2) object; the derivation is a counting/flux argument (clean, like the reach-law cut-count), valid where bandwidth spreading is conservative/diffusive. The raw layer-1 substrate is ballistic (the standing two-layer lesson, `CurvatureEmergence_3DIsotropy`); reading `1/r` off raw ballistic transport would not be clean. The probe measures counts and solves the conservative field equation, not ballistic transport, which is why it is clean.
- **FORM derived, VALUE inherited.** This forces the *form* (`1/r`, inverse-square, 3D-unique) from {P04 conservation + holographic cut + the layer-2 conservative-spreading reading}. It does **not** derive `G` or `ℓ_P` (inherited, per Paper_027's identification), nor the absolute normalization.
- **A reading of P04.** "A mass is a conserved bandwidth-influence `Q`" is the natural reading of P04 (bandwidth conservation) joined to "mass = localized bandwidth perturbation" (the foothold's curvature signature), but it is a reading, not a canonical statement.
- **Linear only; the nonlinear term is separate.** This is the Newtonian/Poisson (linear) field equation. The nonlinearity of ED gravity is the *interference cross-term* (P14, `CurvatureEmergence_NonlinearIsMOND_KinematicMetric`), which gives MOND, not a metric self-coupling. This note does not touch it; it grounds the linear base on which the MOND correction sits.

## 6. Status

**The linear field equation is derived.** Curvature emergence now has: a metric emerges and curves (foothold); `g~1/b` is forced by the holographic cut in 3D (reach law); the *source profile* `b(r)~1/r` and the inverse-square Newtonian force are forced by bandwidth conservation + the same holographic cut, a substrate Gauss's law (this note); and the nonlinearity is the interference/MOND term (characterized). What remains open: the covariant/nonlinear field equation as a *derived* (not characterized) object, a background-free construction (the lattice/topology is still input), and `G`/`ℓ_P` values (inherited). The "`b`-dip imposed by hand" gap is closed, and the Newtonian `1/r` is now substrate-derived from the same holographic principle as the metric, rather than inherited from the kernel.
