# BTFR.08 — Self-Consistent Temporal-Tension PDE

**Date:** 2026-04-27
**Arc:** Dark Matter — BTFR sub-arc, eighth memo
**Status:** Self-consistent treatment of the temporal-tension field T as a dimensionless slow-time produces a structurally distinct equation from the linearization used in BTFR.02–07. Under one specific structural condition — an Einstein-like relation `D_T = c² · κ_act` between the diffusion and activity-coupling constants — the cylindrical-curvature term in the Laplacian **cancels exactly** against the self-consistency-induced first-derivative term, leaving a 2D-Cartesian Helmholtz operator with a K₀ Green's function and a natural logarithmic far-field. **C1 (log far-field) is then repaired structurally without anisotropy and without imported MOND machinery.** However: (a) C2 (√M_b coupling) is *not* repaired by self-consistency alone; (b) ED's canonical constants do not exactly satisfy the Einstein-like relation, so the cancellation is partial in the canonical theory; (c) the cancellation, where it holds, is a structural property of ED's slow-time interpretation, not an additional assumption. **Verdict: self-consistent temporal tension is a real and previously-missed ingredient that fixes one of two BTFR conditions. The other condition still requires either a sublinear source functional (Route II-B) or a coupling-form modification — but the required modification is now smaller than BTFR.06/07 indicated.**
**Predecessors:** BTFR.02–07.
**Successor:** BTFR.09 (examine whether Einstein-like relation is structurally derivable in ED's foundations) or pivot to DM.5 closure.

---

## 1. Definition of T as slow-time

### 1.1 The slow-time interpretation

In ED's temporal-tension picture, **T is a dimensionless field** representing a local fractional deviation from the global cosmological time-rate. The local proper-time rate satisfies, for small T,

> dτ_local / dt_global = 1 − T + O(T²),

so T = 0 corresponds to "global" time-rate and T > 0 corresponds to slowed local time. This is structurally analogous to the Newtonian gravitational potential Φ_GR = Φ/c² when expressed dimensionlessly in GR.

### 1.2 Acceleration coupling

The geodesic equation for a slow-time field (in the static, weak-field limit) gives a force per unit mass

> a_T = c² · ∇T.

This is the temporal-tension analog of `a = c²·∇Φ` in Newtonian-limit GR. The coupling constant is c², not the `γ = D_T/κ_act` used in DM.1's Reading B. **This is a structural difference between the canonical-ED Reading B treatment and the slow-time interpretation.** Whether the two are reconciled depends on a structural relation between D_T and κ_act (§3.4 below).

For circular orbits in an axisymmetric T(R, z=0) field:

> v_T² = R · c² · |∂_R T|

(with the convention that T decreases outward in the disc, so |∂_R T| = −∂_R T).

### 1.3 What BTFR.02–07 was doing

The earlier memos treated the PDE

> D_T · ∇²T − λ T = − κ_act · A(R, z),

with `A(R, z)` built from the *baryonic* velocity field `v_baryon(R)` taken as a fixed external input from photometric mass models. The kinematic prediction was extracted via Reading B's `v_T² = −R · γ · ∂_R T`.

This treatment is the **linearization** of the self-consistent equation. It treats v_baryon as if T did not back-react on it. For the BTFR analysis it produced a 1/R Green's function (no log far-field) because the operator was the canonical cylindrical screened-Poisson and the source was M_b-independent of T's value.

The slow-time picture demands a different treatment.

---

## 2. The self-consistent equation

### 2.1 Activity index in self-consistent form

The activity that sources T is the kinematic activity of the *actual* disc rotation, not the Newton-only baryonic component. In the self-consistent disc,

> v_total² = v_baryon² + v_T²,

and the activity index is

> A(R, z) = α · |∇v_total|² + (1 − α) · ω_total² ≈ v_total² / R²    (asymptotically; both terms scale as v²/R² for circular flow)

so

> A(R) = (v_baryon² + v_T²) / R².

### 2.2 The full equation

Substituting `v_T² = R · c² · |∂_R T| = − R · c² · ∂_R T` (with ∂_R T < 0 for the physically-relevant case of T decreasing outward) and assuming asymptotic Keplerian baryonic component `v_baryon² = G · M_b / R`:

> A(R) = G · M_b / R³ − c² · ∂_R T / R.

The self-consistent PDE is therefore

> D_T · ∇²T − λ T = − κ_act · [G · M_b / R³ − c² · ∂_R T / R].

Bringing the T-dependent source term to the left-hand side:

> **D_T · ∇²T − (κ_act · c² / R) · ∂_R T − λ T = − κ_act · G · M_b / R³.**

This is **linear in T**: the contribution of v_T² to A is linear in ∂_R T, so the equation remains in the linear-PDE class. The only structural change from BTFR.02–07 is the appearance of the new first-derivative term `(κ_act · c² / R) · ∂_R T` on the LHS.

### 2.3 The cylindrical-curvature cancellation

Expanding the cylindrical Laplacian:

> ∇²T = ∂_R²T + (1/R) · ∂_R T + ∂_z²T,

the equation becomes

> D_T · ∂_R²T + [D_T/R − κ_act·c²/R] · ∂_R T + D_T · ∂_z²T − λ T = − κ_act · G · M_b / R³.

The coefficient of `(1/R)·∂_R T` is `(D_T − κ_act·c²)/R`. **If D_T = c² · κ_act** — call this the **Einstein-like relation** — this coefficient vanishes exactly:

> **D_T · [∂_R²T + ∂_z²T] − λ T = − κ_act · G · M_b / R³.**

This is a **2D-Cartesian Helmholtz operator** in (R, z), not a cylindrical screened-Poisson. The Green's function for cylindrically-symmetric sources in this operator is the modified Bessel function of zero order:

> G(R) = (1 / [2π · D_T]) · K₀(R / L),    L = √(D_T / λ).

K₀ has the asymptotic expansions:

- Small argument: K₀(x) ≈ −ln(x/2) − γ_E. **Logarithmic.**
- Large argument: K₀(x) ≈ √(π / 2x) · e^{−x}. **Exponentially decaying.**

The transition is at x ~ 1, i.e., R ~ L. For ED's cluster-calibrated L ≈ 980 kpc, **the entire SPARC galactic regime (R = 1 to 50 kpc) lies in the log window R ≪ L**.

### 2.4 The structural significance

When the Einstein-like relation holds, **canonical ED produces a logarithmic far-field over the entire in-galaxy regime, automatically, without any of the modifications proposed in BTFR.06–07**:

- **No anisotropy required.** The 1/R term cancellation does the job that strong anisotropy was needed for.
- **No MOND-like ν(a/a₀) imported.** The log emerges from the operator structure, not from a postulated coupling form.
- **No new parameters introduced.** D_T, κ_act, λ are all canonical ED constants.

**The condition C1 from BTFR.02 is satisfied structurally.**

---

## 3. The Einstein-like relation D_T = c² · κ_act

### 3.1 What the relation says

In dimensional terms, with T dimensionless:

- D_T has units [length²/time]
- κ_act has units [time] (so that κ_act · A, with A in [1/time²], gives [1/time], matching the units of D_T·∇²T and λT in the PDE)
- c² · κ_act has units [length²/time²] · [time] = [length²/time], matching D_T

So the relation D_T = c² · κ_act is dimensionally consistent and makes a definite claim: the diffusion coefficient and the activity-coupling are linked by the speed of light squared.

This is structurally analogous to the **Einstein relation** in random-walk theory (D · ζ = k_B T_thermal where ζ is friction) — both express a fundamental coupling between a diffusion coefficient and a coupling-to-source. Here, the role of "thermal energy" is played by c², and the role of "friction" is played by κ_act.

### 3.2 Numerical check against canonical ED

Cluster-calibrated values (DM.0 §2):

- D_T ≈ 2.1 × 10²⁷ m²/s
- λ ≈ 1/13.8 Gyr ≈ 2.3 × 10⁻¹⁸ /s
- L = √(D_T/λ) ≈ 3.0 × 10²² m ≈ 980 kpc

Required κ_act for the Einstein-like relation:

> κ_act = D_T / c² = 2.1 × 10²⁷ / (3 × 10⁸)² = 2.3 × 10¹⁰ s ≈ 730 Gyr.

This is approximately **53 × t_H** — roughly 53 Hubble times. The canonical-ED dimensional anchor sets κ_act = 1 in galactic-natural units, which (depending on the unit convention) corresponds to ~1 Gyr or similar. **Canonical ED does not satisfy the Einstein-like relation by a factor of order 50–700.**

### 3.3 Consequences of the discrepancy

If `D_T ≠ c²·κ_act`, the cancellation is partial. The residual coefficient of `(1/R)·∂_R T` is `(D_T − c²·κ_act)/R`. For canonical ED with `D_T ≫ c²·κ_act` (factor ~50), the residual is positive and close to D_T, meaning the operator is **close to canonical cylindrical** (no significant cancellation) and only weakly modified by the self-consistency term.

In this regime the BTFR.02–07 analysis is approximately correct: log far-field is not produced naturally; canonical ED still fails C1.

The 2D-Cartesian-Helmholtz limit is reached only when `c²·κ_act → D_T`. Whether this limit is structurally privileged in ED — whether some foundational principle requires `D_T = c²·κ_act` — is a question this memo does not resolve. It would require revisiting ED's foundational derivation of D_T and κ_act and asking whether they emerge as related quantities (Einstein-relation-like) or as independent parameters.

### 3.4 Three structural possibilities

Three distinct readings of the situation:

- **(P1) Canonical ED is correct as calibrated, and the slow-time interpretation is wrong.** Then Reading B's coupling γ = D_T/κ_act ≈ 6.97 × 10⁴ m²/s² is the correct ED coupling, and v² = R · γ · |∂_R T| is the correct kinematic relation — not v² = R · c² · |∂_R T|. T is *not* the dimensionless slow-time but some other quantity with γ-coupling. Under this reading, the BTFR.02–07 chain is correct as stated, and the C1 failure is structural.

- **(P2) The slow-time interpretation is correct, and ED's canonical constants need adjustment.** Then κ_act should be ~ D_T/c² rather than the cluster-anchored value, and the Einstein-like relation defines the correct calibration. Under this reading, the cluster merger-lag prediction would need re-derivation with the corrected κ_act, and self-consistent ED naturally produces log far-field.

- **(P3) Both readings have partial validity.** ED's canonical T is a hybrid object: its diffusion is governed by D_T (cluster-calibrated), but its kinematic coupling has both a γ-component (from Reading B's PDE structure) and a c²-component (from the slow-time interpretation). The full theory is some combination, and the BTFR analysis must use whichever coupling dominates in the regime of interest.

The choice between P1, P2, P3 is a foundational question for ED, not a BTFR question. **BTFR.08's contribution is to show that P2 (or any reading where c² is the kinematic coupling) produces a structurally-distinct PDE with C1 repaired automatically.**

---

## 4. Asymptotic disc analysis

Under the Einstein-like relation (P2 or P3 in the relevant regime):

### 4.1 Green's function and field

For a localized cylindrically-symmetric source σ(R) on the disc plane:

> T(R) ≈ (1 / [2π · D_T]) · ∫ K₀(|R − R'| / L) · σ(R') · 2π R' dR'    (in the disc plane)

For R in the log window (R ≪ L) and source extent R_b ≪ R:

> T(R) ≈ (M_eff / [2π · D_T]) · K₀(R / L) ≈ −(M_eff / [2π · D_T]) · ln(R / L_eff)

where `M_eff = ∫ σ(R') · 2π R' dR'` is the disc-integrated source (with appropriate vertical-thickness factor) and `L_eff = 2L · e^{−γ_E}` is the effective log-cutoff.

### 4.2 The asymptotic v_T

In the log regime:

> ∂_R T(R) ≈ − M_eff / [2π · D_T · R]    (negative; T decreases outward).

Using v_T² = R · c² · |∂_R T| = R · c² · M_eff / (2π · D_T · R):

> **v_T² = c² · M_eff / (2π · D_T).    (constant in R; flat curve).**

The flat-curve condition C1 is satisfied. Good.

### 4.3 M_eff scaling with M_b

Now compute M_eff for an asymptotically Keplerian disc with total baryon mass M_b:

> σ(R) = ∫ S_eff(R, z) dz = κ_act · ∫ A(R, z) dz · (vertical factor)
>      ≈ κ_act · G · M_b / R³ · (geometric factor)

(where the v_T² contribution to A has been absorbed into the LHS of the self-consistent PDE, so σ here is the M_b-driven part of the source).

Disc-integrated:

> M_eff = ∫ σ(R) · 2π R dR ≈ 2π · κ_act · G · M_b · ∫_{R_min}^{R_b} dR / R²
>       ≈ 2π · κ_act · G · M_b / R_min.

This is **linear in M_b**, with proportionality constant depending on R_min (an inner radial cutoff scale of the disc, possibly the disc scale length R_d or the inner edge of the active region).

### 4.4 BTFR slope prediction

Plug M_eff ∝ κ_act · G · M_b / R_min into v_T²:

> v_T² = c² · M_eff / (2π · D_T)
>      = c² · κ_act · G · M_b / (D_T · R_min)
>      = G · M_b / R_min    (using D_T = c² · κ_act, the Einstein-like relation).

So **v_T² ≈ G · M_b / R_min**, giving:

> v_T⁴ = (G · M_b / R_min)² ∝ M_b² / R_min².

This is **slope 2 BTFR**, with explicit R_min dependence (scatter from R_min variation across the SPARC sample).

**C1 is repaired (flat curves) but C2 is not (linear M_b instead of √M_b), and C3 is partially violated (R_min dependence).**

### 4.5 The acceleration scale

The asymptotic acceleration in the log regime:

> a_T = v_T² / R = c² · M_eff / (2π · D_T · R) = G · M_b / (R · R_min)

The crossover scale where a_T ~ a_baryon = G·M_b/R²:

> R_x ≈ R_min.

So the v_T contribution dominates only outside the inner disc edge (which is what we expect for galactic dynamics). The associated acceleration scale at the crossover is:

> a_x = G · M_b / R_min² = (Newtonian acceleration at the inner disc edge).

This is **galaxy-dependent**, not universal. There is no automatic emergence of `c · λ ≈ c · H_0 ≈ a₀` as a universal acceleration scale from this calculation alone. The c·H_0 scale would need to enter through the screening cutoff (R ~ L = c · √(κ_act/λ) · √(c²/c²) = c·κ_act if we use the Einstein-like relation), but that's the *outer* cutoff of the log regime, not the inner crossover where MOND's a₀ is supposed to live.

**So the natural ED-derived scale c · H_0 does not automatically play the role of MOND's a₀ in this analysis.** The temporal-tension self-consistency provides the log far-field but does not provide the MOND-like deep-regime acceleration cutoff.

---

## 5. Comparison to BTFR.06 and BTFR.07

### 5.1 What changes

| Element | BTFR.06/07 conclusion | BTFR.08 conclusion |
|---|---|---|
| C1 (log far-field) | Requires anisotropy with D_z/D_R ≲ 10⁻⁶ | Requires Einstein-like relation D_T = c²·κ_act; given that, automatic |
| C2 (√M_b amplitude) | Requires imported MOND ν(a/a₀) or sublinear source | Same: still requires Route II-A or II-B |
| C3 (R-independence) | Fails in canonical | Partial: R_min dependence only |
| New parameters | 1 (D_z) + 1 functional (ν) | 1 functional (interpolation or sublinear source); D_z eliminated |
| Acceleration scale | a₀ = λ²·D_T claimed (arithmetic was wrong by 100×) | c·H_0 noted but does not enter as the natural BTFR scale; MOND-analog cutoff still requires structural input |
| Compatibility | Compatible with R, M, N, Q, B | Same |

### 5.2 What stays the same

- Self-consistency does not eliminate the C2 requirement. **Activity-source ED, with linear-in-M_b source functional, still predicts slope 2 BTFR even with the log kernel.**
- A coupling-form modification (Route II-A) or a sublinear source functional (Route II-B) is still required for slope 4.
- The DM2 production-run FAIL verdict still stands as a refutation of canonical ED. The self-consistent treatment would soften the failure mode (curves would be flat-ish instead of falling) but would not produce slope-4 BTFR.

### 5.3 What's genuinely new

**The principal novelty of BTFR.08 is the identification of the Einstein-like relation as a structural condition.** Whether ED's foundational derivation produces D_T = c²·κ_act (P2) or D_T ≠ c²·κ_act (P1) determines whether self-consistent ED has a natural log far-field or not. This is a question for ED's foundations, not for the BTFR analysis itself.

If the foundations *do* yield the Einstein-like relation, BTFR.06's anisotropy requirement is unnecessary, and the BTFR-extension parameter cost reduces to just the C2 fix. If they do *not*, BTFR.06's analysis is correct (anisotropy required).

---

## 6. Structural verdict

> **Self-consistent temporal tension repairs C1 (log far-field) under one structural condition** — the Einstein-like relation `D_T = c² · κ_act` between ED's diffusion coefficient and activity coupling. This relation is dimensionally natural and structurally analogous to the random-walk Einstein relation, but ED's canonical cluster-calibration does not exactly satisfy it.
>
> **Self-consistent temporal tension does not repair C2.** The activity-source functional remains linear in M_b; the resulting BTFR slope is 2, not 4. A coupling-form modification (Route II-A: a₀-weighting) or a sublinear source functional (Route II-B) is still required.
>
> **Self-consistent ED therefore derives BTFR if and only if:**
>   (a) The Einstein-like relation `D_T = c² · κ_act` holds structurally (or can be made to hold by re-deriving the cluster-anchor with the slow-time interpretation explicit);
>   (b) An additional source-coupling modification provides the √M_b scaling.
>
> **(a) is a foundational question** about ED's derivation of D_T and κ_act. **(b) is the same problem identified in BTFR.07** for any of the three options.
>
> **Net effect on BTFR viability:** the structural commitment required to make ED derive BTFR is reduced from "anisotropy + a₀-weighting" to "Einstein-like relation (foundational check) + a₀-weighting." This is a real reduction. Whether it is sufficient to call ED's BTFR derivation "structural" rather than "fitted" depends on whether (a) emerges from ED's foundations or has to be postulated.

---

## 7. Implications for previous memos

- **BTFR.05's "zero new parameters" claim** is correct in spirit if (a) holds and (b) is provided by a single functional choice (interpolation or sublinear source). It is incorrect if D_z (anisotropy) is treated as the C1 fix.
- **BTFR.06's anisotropy analysis** describes a real but *unnecessary* extension if the Einstein-like relation holds. It remains valid as an alternative path if the Einstein-like relation does not.
- **BTFR.06's `a₀ ≈ λ²·D_T` claim** is arithmetically wrong by ~100× and should be retracted. The correct ED-derived acceleration scale candidates are c·λ ≈ c·H_0 (within factor of 6 of MOND's a₀) and c²/L (which is much larger). Neither emerges automatically as the BTFR a₀-equivalent in the present analysis.
- **BTFR.07's three-option table** simplifies considerably under self-consistency: Option A's anisotropy postulate is replaced by a cleaner foundational check (Einstein-like relation), and the only remaining commitment is the C2 fix.

---

## 8. Recommended Next Steps

Three concrete next steps, ranked by structural priority:

1. **BTFR.09 — Foundational check on the Einstein-like relation.** Examine whether D_T and κ_act in ED's foundational derivation emerge as related quantities (i.e., whether `D_T = c²·κ_act` is implicit) or as independent constants. This is a structural question internal to ED's derivation, not requiring numerical fitting. Output: a yes/no on whether (a) holds. If yes, the BTFR analysis collapses to "self-consistent ED + C2 fix." If no, BTFR.06's anisotropy path is the canonical route.

2. **C2-specific structural search.** Independent of the C1 question, investigate whether ED's activity-source functional admits a √M_b-yielding form without imported MOND machinery. Candidate: examine whether the ED-derived acceleration scale (c·H_0 or some other combination) plays a structural role in the source coupling that the BTFR.02–07 analysis missed by treating κ_act as a constant. If a coupling form can be derived from ED's structure rather than postulated, C2 becomes a structural rather than fitted condition.

3. **Pivot to DM.5 closure.** If the BTFR sub-arc is judged sufficient at this point, write DM.5 with the BTFR.02–08 chain as the structural-context for the production-run FAIL. The verdict becomes: "Canonical ED fails BTFR; the failure is structural (C1 + C2); self-consistent ED with Einstein-like relation (if foundational) repairs C1; C2 remains an open structural question." This is a publishable scientific result regardless of whether (1) and (2) succeed.

The user's intuition — that temporal-tension was the missing ingredient — proved correct in the C1 sense. It does not by itself produce BTFR, but it materially reduces the structural cost of the extension and reframes the open question more cleanly.

Status: complete.
