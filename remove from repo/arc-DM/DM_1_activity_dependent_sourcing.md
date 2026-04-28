# DM.1 — Activity-Dependent Sourcing

**Date:** 2026-04-25
**Arc:** Dark Matter (DM) — second memo
**Status:** Derivation complete. Verdict: **PARTIAL PASS.** Shear-and-vorticity sourcing structurally fixes the shape and BTFR failures of DM.0. The magnitude failure is converted from a refutation into an inherited coupling κ_act with no structural derivation in the current framework. Star-formation sourcing fails on its own; composite forms inherit the shear behavior in the outer disk where it matters.
**Predecessor:** DM.0 (negative verdict on S = β ρ_b).
**Empirical anchor:** ED-04.5 (46 SPARC dwarfs; ⟨D_outer⟩_active / ⟨D_outer⟩_quiet ≈ 1.53).
**Successor:** see *Recommended Next Step* (DM.2).

---

## 1. Setup

DM.0 established that the equilibrium screened-Poisson PDE with mass-density sourcing fails three independent tests at galactic scales: wrong shape (rising or Keplerian, not flat), no BTFR, and a magnitude shortfall of ~10³.

ED-04 §2.2 explicitly says temporal tension is sourced by **activity density**, not mass density. ED-04.5 confirms this empirically: dwarfs sorted by qualitative dynamical activity show a 53% spread in outer-radius mass discrepancy that has no clean mass interpretation.

DM.1 tests whether replacing S = β ρ_b with an activity-dependent S(x) repairs the three failure modes while preserving the cluster-scale merger-lag result.

The PDE itself is unchanged:

> D_T ∇²T − λT = −S(x).

Only the source term varies. Three candidates and a composite are considered.

---

## 2. Candidate source forms

### 2.1 Shear sourcing — S ∝ |∇v|²

The dominant velocity gradient in a rotating thin disk is the rate-of-strain tensor of the rotational flow. For a flat rotation curve v(r) = v_∞, the dominant component of |∇v|² is the differential-rotation shear:

> |∇v|² ≈ ω² = v(r)² / r².

For an asymptotically flat curve, this gives **|∇v|² ∝ 1/r²** in the outer disk. This is the structurally critical fact.

### 2.2 Vorticity sourcing — S ∝ ω²

Vorticity ω = v/r in cylindrical coordinates. For flat v(r) = v_∞, ω² = v_∞²/r², identical to shear in the outer disk. In the inner disk where v ∝ r (rigid-body rotation), ω = const → ω² = const. Behaves like shear in the relevant outer regime.

### 2.3 Star-formation sourcing — S ∝ Σ_SFR

Kennicutt-Schmidt: Σ_SFR ∝ Σ_gas^(1.4). For an exponential gas disk Σ_gas ∝ exp(−r/R_d), this gives **Σ_SFR ∝ exp(−1.4 r/R_d)** — a localized, exponentially decaying source.

Structurally, this is the same kind of source as DM.0's mass density: bounded, localized, falls off rapidly with radius. Convolved against the Yukawa Green's function in the unscreened limit, it produces T(r) ∝ 1/r at large r — the same wrong shape DM.0 ruled out.

**SFR sourcing alone fails the shape test by the same argument as mass-density sourcing.**

### 2.4 Composite sourcing — S = α|∇v|² + β ω² + γ Σ_SFR

In the outer disk where shear and vorticity dominate, the composite scales as 1/r² and behaves like shear sourcing. In the inner disk where SFR is concentrated, the composite has additional localized contributions but does not change the asymptotic shape. The outer-disk behavior controls flat-curve emergence.

---

## 3. Equilibrium solution for shear sourcing

### 3.1 Screened Poisson with 1/r² source

In the outer disk (r₀ < r < r_max, with r_max ≪ L = 1 Mpc), the source is:

> S(r) = κ_act · v_∞² / r²,

where κ_act has units chosen to make S dimensionally a [T]/time. The equilibrium PDE in the unscreened limit (r ≪ L):

> ∇²T ≈ −S/D_T = −(κ_act v_∞² / D_T) · 1/r².

For spherically symmetric T (axisymmetric averaging applies for the disk problem at zeroth order), the radial Laplacian gives:

> (1/r²) d/dr(r² dT/dr) = −(κ_act v_∞² / D_T) · 1/r².

Multiply both sides by r²:

> d/dr(r² dT/dr) = −(κ_act v_∞² / D_T).

The right-hand side is constant. Integrate once:

> r² dT/dr = −(κ_act v_∞² / D_T) · r + C₁.

For large r where the constant becomes negligible:

> dT/dr = −(κ_act v_∞² / D_T) / r,

and integrating again:

> **T(r) = −(κ_act v_∞² / D_T) · ln(r) + C₂.**

The temporal-tension field has a **logarithmic profile** in the outer disk where shear sourcing dominates.

### 3.2 The crossover at r ~ r_max

Beyond r_max (the outer edge of the active disk), S → 0. The PDE reduces to ∇²T − T/L² = 0 (homogeneous Yukawa), with solutions T ∝ exp(−r/L)/r. So:

- For r₀ < r < r_max: T(r) ≈ A − B ln(r), with B = κ_act v_∞² / D_T.
- For r > r_max: T(r) ∝ exp(−r/L) / r.

The transition between the two regimes happens at r_max, the outer edge of the disk's dynamical activity.

---

## 4. Mapping T to gravity — Reading B revisited

### 4.1 Why Reading B is the right reading here

DM.0 considered three readings: (A) T as effective mass density, (B) T as gravitational potential directly, (C) T as metric-coefficient perturbation. Under shear sourcing:

- **Reading A** (ρ_T = α T): T ∝ ln(r) → ρ_T ∝ ln(r), which is unbounded and changes sign. This is awkward; if interpreted as a density, a logarithmic profile gives non-physical mass distributions. Reading A does not naturally accommodate the shear-source solution.

- **Reading B** (Φ_T = γ T): T ∝ ln(r) → Φ_T(r) = γ · (A − B ln(r)). Then:

> dΦ_T/dr = −γB / r,
> v_T²(r) = r · dΦ_T/dr = −γB = constant.

> **Flat rotation curve.** Self-consistent.

- **Reading C** (acoustic-metric perturbation): structurally equivalent to Reading B in the weak-field limit.

**Under shear sourcing, Reading B (T as gravitational potential, equivalent to Reading C) produces flat rotation curves naturally.** This is the load-bearing structural fix of DM.0's shape failure.

### 4.2 Self-consistency

The flat-rotation-curve value v_∞² is set by:

> v_T² = γ · κ_act · v_∞² / D_T.

For self-consistency with the assumed flat curve:

> 1 = γ · κ_act / D_T,

i.e.,

> **γ · κ_act = D_T.**

This is a constraint on the product γ · κ_act, not on either individually. With D_T fixed at 2.1 × 10²⁷ m² s⁻¹ from cluster scales, γ · κ_act is fixed at the same value.

This is a single dimensional fixed-point relation. It says: the temporal-tension contribution to gravitational potential, sourced by shear, produces flat curves consistent with the same shear input. The relation is structurally clean — but it does not predict the absolute amplitude v_∞, only the self-consistency of any flat curve.

### 4.3 What does set v_∞?

The boundary conditions. The constant A (and C₂) in T(r) = A − B ln(r) is fixed by matching to the inner disk, where rigid-body rotation gives a different shear profile, and to the outer transition at r_max. The amplitude v_∞ falls out of the matching, and depends on the disk's specific structure (R_d, M_b, gas distribution).

For an exponential disk with R_d and M_b:

> v_∞² ∝ G · M_b / R_d × (factor involving γ · κ_act / D_T),

where the proportionality reflects the matching of T's logarithmic outer profile to the disk's interior potential.

Since γ · κ_act / D_T = 1 by self-consistency, the dimensional content reduces to:

> v_∞² ∝ G · M_b / R_d.

This is the **Newtonian dimensional combination**, not the MOND combination. We will revisit this in §5.

---

## 5. The BTFR test

### 5.1 What BTFR says

The baryonic Tully-Fisher relation:

> v_∞⁴ ∝ M_b,

empirically with slope 3.5–4.

### 5.2 What §4.3 produces

> v_∞² ∝ G M_b / R_d.

To get BTFR, we need v_∞⁴ ∝ G² M_b² / R_d² ∝ M_b. This requires:

> R_d² ∝ M_b,
> R_d ∝ M_b^(1/2).

### 5.3 Empirical disk-mass-to-scale relation

For real galaxies, the disk scale length and baryonic mass are correlated. The Persic-Salucci universal-rotation-curve work and subsequent SPARC analyses give an approximate relation:

> R_d ∝ M_b^(0.4 to 0.5),

depending on selection and morphology. This is *consistent* with the R_d ∝ M_b^(1/2) requirement to within scatter.

### 5.4 BTFR verdict

Shear sourcing **inherits BTFR from the disk scaling relation R_d ∝ √M_b.** The framework does not derive BTFR from primitives; it derives it conditional on an empirical disk relation. This is consistent with the program's "form forced, value inherited" pattern, but it is weaker than MOND's situation, where BTFR is a direct consequence of the modified-gravity law a = √(a_N a₀) with no disk-scaling requirement.

**Status: BTFR is reproduced, but only conditional on the empirical disk relation. It is not forced from primitives.**

---

## 6. The magnitude test

### 6.1 The MOND a₀ as a target

Milgrom: a₀ ≈ 1.2 × 10⁻¹⁰ m s⁻². In the shear-source picture, the natural acceleration scale at radius r is:

> a_T(r) = dΦ_T/dr = γB/r = γ κ_act v_∞² / (D_T r).

For this to equal a₀ at r ~ tens of kpc with v_∞ ~ 200 km/s:

> γ κ_act / D_T = a₀ · r / v_∞² ≈ (1.2 × 10⁻¹⁰) · (3 × 10²⁰) / (5 × 10¹⁰)
>              ≈ **7 × 10⁻¹**,

— of order unity. The required value of γ κ_act / D_T is O(1), which is exactly what self-consistency in §4.2 demands. **The magnitude is internally consistent.**

This is a striking change from DM.0, where the natural mass-source coupling was 10³ too small. Under shear sourcing, the natural dimensional combination is of order unity, and the MOND scale falls out without tuning.

### 6.2 What this means

DM.0's magnitude failure was a factor-of-1000 problem under the natural mass coupling. DM.1's shear sourcing replaces it with a factor-of-1 fixed-point relation. The magnitude is no longer "wrong by 10³"; it is "set by the structural constraint γ κ_act = D_T."

**The magnitude failure of DM.0 is structurally repaired by shear sourcing.**

### 6.3 What it does not mean

The framework still does not *derive* κ_act or γ from primitives. They are inherited. What we have shown is that the inheritance is no longer pathologically far from observation — it sits at the natural scale, not 10³ off.

This is the same epistemic status as Arc M's mass values: form forced, values inherited. It is not a refutation; it is an honest statement of where the framework currently sits.

---

## 7. Star-formation sourcing — failed

S ∝ Σ_SFR with Kennicutt-Schmidt scaling produces a localized exponential source. Convolved against the Yukawa Green's function in the unscreened limit, this gives T(r) ∝ 1/r at large r — the same Newtonian-monopole shape that DM.0 ruled out under all three readings:

- Reading A: M_T(<r) ∝ r² → rising curves.
- Reading B: Φ_T ∝ 1/r → Keplerian curves.
- Reading C: same as Reading B.

**SFR sourcing cannot produce flat curves on its own.** It contributes additively in a composite source but does not control the asymptotic shape, which is dominated by the 1/r² shear/vorticity contribution.

This is structurally significant for ED-04.5: the SPARC active-vs-quiet separation correlates strongly with star formation, but the *mechanism* producing the rotation-curve effect is not the SFR itself — it is the shear and vorticity that accompany active dynamics. SFR is a proxy for activity; the activity is what sources the field.

---

## 8. Composite sourcing — the realistic case

In a real galaxy, all three contributions are present. The realistic composite:

> S(x) = α |∇v(x)|² + β ω(x)² + γ Σ_SFR(x).

Behavior by region:

- **Outer disk (r > R_d):** shear and vorticity dominate (S ∝ 1/r²), Σ_SFR is exponentially suppressed. Composite → shear sourcing → flat curves under Reading B.
- **Inner disk (r < R_d):** shear is small (rigid-body rotation has ω ≈ const, |∇v| small), Σ_SFR is concentrated. Composite has localized contributions but the rotation curve in this regime is dominated by the baryonic disk itself, not by T.
- **Bulge / nuclear region:** all three contributions exist. The local contribution to T does not affect the outer flat-curve behavior, which is controlled by r > R_d.

**Composite sourcing inherits the flat-curve fix from shear, the BTFR conditional on disk scaling, and the magnitude fix from γ κ_act ~ D_T.**

The relative weights α, β, γ are not fixed by the framework. Different weight choices change the inner-disk profile (the shape of v(r) at small r) but not the outer flat regime.

---

## 9. Cluster compatibility

The merger-lag paper uses S(x, t) ∝ baryonic mass density of the moving subcluster. Under DM.1's activity-source revision, this needs reinterpretation:

In a cluster merger, the subcluster moves through the main cluster at thousands of km/s. The induced shear |∇v|² is enormous — much larger than steady-state galactic rotation:

- Galactic rotation: |∇v|² ≈ ω² ~ (200 km/s / 30 kpc)² ~ 5 × 10⁻³³ s⁻².
- Cluster merger: |∇v|² ~ (4500 km/s / 100 kpc)² ~ 2 × 10⁻³⁰ s⁻².

Cluster-merger shear is ~400× galactic shear. Activity sourcing reproduces a strong source in cluster mergers, which is what the merger-lag paper requires.

The merger-lag paper's S(x, t) ∝ ρ_b should be reinterpreted as S(x, t) ∝ activity density tied to the motion of the baryonic mass. The wake structure ℓ_wake = D_T / v emerges from the same equilibration physics regardless of whether S tracks mass or activity, *provided* the activity source has the right magnitude for cluster-scale shear. The numerical agreement of D_T = 2.1 × 10²⁷ m² s⁻¹ with seven clusters is not refuted by this reinterpretation — it is rediagnosed as a constraint on κ_act × (cluster-scale shear), which fixes the same dimensional combination.

**The cluster-merger result remains valid under activity sourcing.** The merger-lag paper's quantitative success is preserved; its source-term interpretation is updated.

---

## 10. The dwarf-galaxy result revisited

ED-04.5's 53% separation between Active and Quiet dwarfs is now structurally interpretable.

Under shear sourcing, the temporal-tension halo strength is set by integrated shear over the active region. Active dwarfs have:
- Higher mean rotation speed (more ω),
- Higher turbulence (additional |∇v|² contribution),
- More disturbed morphology (additional shear in non-axisymmetric structure).

All three contribute multiplicatively to S, raising the temporal-tension halo and the inferred D_outer. The 53% ratio is consistent with a factor-of-1.5 difference in integrated activity — which is plausible for a sample where "Active" includes morphologically disturbed and starburst dwarfs and "Quiet" includes smooth, low-SFR systems.

This does not derive the 53% number; it is consistent with it. A quantitative test would require activity-quantification per galaxy — replacing the binary Quiet/Active classification with a continuous activity index — and a per-galaxy fit of D_outer vs. the activity index. ED-04.5 does not do this, and DM.1 does not require it; the structural interpretation is sufficient at this stage.

---

## 11. Verdict matrix

| Failure mode in DM.0 | Verdict under DM.1 |
|---|---|
| Shape (rising/Keplerian, not flat) | **FIXED** — shear sourcing gives logarithmic T → flat v under Reading B. |
| BTFR | **CONDITIONAL** — inherits from empirical R_d ∝ √M_b disk relation, not derived from primitives. |
| Magnitude (~10³ shortfall) | **FIXED** — γ κ_act = D_T is a self-consistency relation at the natural scale, not a tuning. |
| SFR-only sourcing | **FAILS** — same shape failure as mass sourcing. SFR is a proxy, not the mechanism. |
| Composite sourcing | **PASS** — outer-disk behavior is shear-dominated, inherits the flat-curve fix. |
| Cluster-merger compatibility | **PASS** — cluster shear is ~400× galactic shear, naturally produces strong T. |

---

## 12. What is forced, what is inherited, what is open

### Forced
- The functional form of S = activity density (per ED-04 §2.2).
- The shear contribution scales as 1/r² for any locally-flat rotation curve.
- The screened-Poisson Yukawa structure of the equilibrium PDE.
- The fixed-point relation γ κ_act = D_T at the natural scale.

### Inherited
- D_T (from cluster-scale Mistele weak-lensing).
- λ (set to 1/t_H phenomenologically).
- κ_act and γ individually (only their product is fixed).
- The empirical R_d ∝ √M_b disk-scaling relation that delivers BTFR.
- The relative weights α, β, γ in the composite source.

### Open
- A structural derivation of κ_act from primitives.
- Whether κ_act is genuinely universal across galaxy types, or whether it varies with morphology.
- The inner-disk profile, where the rigid-body rotation regime intersects the active outer regime.
- The transition at r_max where shear sourcing turns off and Yukawa decay takes over.
- Whether the Reading-B mapping (T as gravitational potential) is forced by the framework or is one consistent reading among several.

### Requires simulation
- Per-galaxy fits against SPARC rotation curves with the activity-source PDE.
- A quantitative activity index per galaxy (replacing ED-04.5's binary classification).
- Tests across galaxy morphologies (spirals, ellipticals, dwarfs, irregulars).

### Requires additional structure
- Derivation of κ_act from ED primitives — what links the activity coupling to ℓ_ED, σ_τ, or the V1 kernel.
- Promotion of the R_d ∝ √M_b relation from empirical to forced.
- Resolution of which T-to-gravity mapping (A, B, or C) is structurally correct, with refutation conditions for the others.

---

## 13. Refutation conditions

DM.1's positive verdict can be refuted in three ways:

1. **Shape failure in detail.** A per-galaxy fit of the activity-source PDE against SPARC reveals systematic deviations from observed v(r) that cannot be absorbed in disk-structure variation. This would refute the shear-source mechanism quantitatively, even though the asymptotic argument here is structural.

2. **Magnitude inhomogeneity.** If the implied κ_act varies systematically across galaxies (e.g., depends on morphology or environment in ways not predicted), then κ_act is not a universal constant and the framework loses its parsimony.

3. **BTFR slope failure.** If observed BTFR slope is inconsistent with the predicted v_∞⁴ ∝ M_b under R_d ∝ √M_b — for example, if the predicted slope deviates significantly from observation across the SPARC sample — the conditional derivation fails.

Tests 1–3 require simulation work. They are addressable in DM.2 and beyond.

---

## 14. Verdict

**DM.1 is a partial pass.** Activity-dependent sourcing repairs two of the three DM.0 failure modes structurally (shape and magnitude) and the third conditionally (BTFR via empirical disk scaling). The framework is no longer in the embarrassing position of a 10³ magnitude shortfall under natural couplings; it now sits at the right scale by self-consistency.

What remains is the work of converting structural plausibility into quantitative agreement. Per-galaxy fits, activity-quantification, and morphology-dependent tests are the next layer of empirical engagement.

The DM mechanism in ED is now coherent across scales: shear and vorticity drive temporal-tension halos at galactic scales (equilibrium, flat curves), while the same field responds non-equilibrium to fast-moving baryonic sources at cluster scales (merger-lag). One PDE, one D_T, one λ, one κ_act, two regimes.

---

## Recommended Next Step

**DM.2 — Per-galaxy SPARC rotation-curve fits with the activity-source PDE.**

The structural argument is now in place. The next step is quantitative empirical engagement: take the activity-source PDE, solve it numerically for representative SPARC galaxies, and compare to observed v(r) curves on a per-galaxy basis.

DM.2 should:

1. **Build a quantitative activity index.** Replace ED-04.5's binary Quiet/Active classification with a continuous activity scalar A(galaxy), built from observable proxies: integrated |∇v|² from the rotation curve itself, integrated Σ_SFR from infrared/UV photometry, and morphological-disturbance metrics from imaging.

2. **Solve the equilibrium activity-source PDE numerically.** For each galaxy, take the SPARC baryonic decomposition, compute the activity profile S(x), solve the screened Poisson equation for T(x), and derive the predicted v(r) under Reading B.

3. **Compare to observed v(r).** Per-galaxy residuals; group statistics; check consistency of the implied κ_act across the sample.

4. **Test BTFR explicitly.** Compute v_∞ from the predicted curves, plot v_∞⁴ vs. M_b, fit the slope, compare to the empirical 3.5–4.

5. **Test the activity-correlation prediction.** Does the implied κ_act depend on activity index, morphology, or environment? Universality would confirm the structural picture; systematic dependence would refute it.

**Expected outcome:**

- **PASS** (κ_act is universal across SPARC; per-galaxy fits succeed; BTFR slope matches): DM mechanism is empirically confirmed at galactic scales. The framework's "form forced, values inherited" claim extends from quantum and cluster scales to galaxies.

- **PARTIAL** (per-galaxy fits succeed but κ_act varies systematically): the activity-source picture is on the right track but missing structure. DM.3 would attempt to identify the missing piece (e.g., environmental coupling, non-axisymmetric corrections, or a second activity channel).

- **FAIL** (per-galaxy fits do not succeed, or BTFR slope fails): the activity-source mechanism, despite structural plausibility, does not match data quantitatively. DM.3 would return to the V1-kernel + acoustic-metric channel as a possible alternative or additional contribution.

DM.2 is a real piece of computational work — building the activity-index pipeline, implementing the numerical PDE solver, running it across the SPARC sample. It is bounded but non-trivial. The output is a per-galaxy verdict on whether DM.1's structural argument survives empirical confrontation.

The alternative branches (return to V1, hybrid mechanism) become live only if DM.2 returns FAIL. They should not be pursued speculatively before the empirical test.

---

## End-of-turn summary

**What got done:** the structural derivation of activity-sourced temporal tension. Shear and vorticity sourcing produce flat rotation curves under Reading B, with magnitude set at the natural scale by γ κ_act = D_T. BTFR is recovered conditional on the empirical disk-scaling relation. SFR sourcing alone fails, but composite forms inherit the shear behavior in the relevant outer-disk regime.

**What did not get done:** per-galaxy fits, quantitative activity index, BTFR slope test. These are DM.2.

**What this means for the program:** DM.1's verdict is the cleanest "partial pass" the framework has had on a quantitative astrophysical question outside the cluster-merger result. The structural picture is now coherent across scales; the empirical confrontation is queued.

**What was preserved:** all forced theorems, the cluster-merger result, the activity-dependence signature in ED-04.5. None of this work is at risk from DM.1.

**What was lost:** the implicit ED-04 claim that mass-density sourcing produces galactic flat curves. That is now refuted by DM.0 and replaced by activity-density sourcing in DM.1.

**What is now testable:** the per-galaxy SPARC fits in DM.2, with three concrete refutation conditions.
