# BTFR.09 — Foundational Check of the Einstein-like Relation

**Date:** 2026-04-27
**Arc:** Dark Matter — BTFR sub-arc, ninth memo
**Status:** Structural and dimensional check of whether ED's primitives force the Einstein-like relation `D_T = c² · κ_act`. **The relation has the canonical form of a relativistic random-walk Einstein relation and is dimensionally exact (no hidden factors of 2 or π); however, ED's canonical cluster-anchored D_T and galactic-anchored κ_act do not satisfy it numerically by a factor of order 10⁶–10⁷, depending on unit convention. The relation is therefore "structurally permitted but not numerically realized" in the cluster-and-galactic-scale calibration of canonical ED.** Two possibilities follow: (P-A) the cluster-anchor of D_T is correct and κ_act needs a different interpretation; (P-B) one of D_T or κ_act is mis-calibrated relative to a foundational derivation that has not been carried out. **The relation is not forbidden by ED's structure, but it is not currently a forced theorem either.** This shifts the BTFR.08 analysis from "the cancellation works automatically" to "the cancellation works iff a foundational re-derivation produces the Einstein-like relation." The foundational re-derivation is identified as the missing structural work.
**Predecessors:** BTFR.02–08; user's pushback (slow-time interpretation surfacing the c²-coupling).
**Successor:** BTFR.10 (foundational re-derivation of D_T from ED primitives) or DM.5 closure with the relation noted as an open structural question.

---

## 1. The three constants in question

### 1.1 D_T — temporal-tension diffusion coefficient

**Dimensional content.** [D_T] = length²/time. In SI: m²/s. In galactic-natural units: kpc²/Gyr.

**Operational role.** Sets the spatial spread of T from a localized source. With λ as the screening rate, the screening length is L = √(D_T/λ).

**Calibration in canonical ED.** Anchored by cluster-scale merger-lag observations (DM.0 §2): a merger of two galaxy clusters produces a delayed peak in some observable; the lag time is governed by D_T and λ. The fit gives D_T ≈ 2.1 × 10²⁷ m²/s, equivalently 6.97 × 10⁴ kpc²/Gyr.

**Structural origin.** Not directly given by ED's foundational primitives in the form I have access to. Treated as a phenomenological constant that the cluster-scale physics determines empirically. Whether it emerges from a deeper derivation (e.g., a random-walk-like derivation of the propagation of temporal-tension corrections through a substrate of events) is an open question.

### 1.2 κ_act — activity-to-tension coupling

**Dimensional content.** Set by the requirement that κ_act · A enters the PDE with the same units as D_T · ∇²T or λT. Since A has units of [1/time²] (it is the square of an angular frequency) and the PDE's other terms have units [T-units / time], we need [κ_act] = [time × T-units / (1/time²)] = [time³ × T-units]. If T is dimensionless (slow-time interpretation), then [κ_act] = [time³] · [T] = [time²] · [time]/[1] which... actually the unit analysis depends on whether the PDE term is `λ·T` (units 1/time) or includes some other factor.

Let me redo cleanly. PDE: `D_T · ∇²T − λ · T = − κ_act · A`.
- [D_T · ∇²T] = (length²/time) · (T-units / length²) = T-units/time
- [λ · T] = (1/time) · T-units = T-units/time
- [κ_act · A] must equal T-units/time
- [A] = 1/time² (square of angular frequency)
- Therefore [κ_act] = T-units · time

If T is dimensionless (slow-time), [κ_act] = time. If T has other units, scale accordingly.

**Operational role.** Sets the magnitude of T's response to a given activity input. In the dimensional-anchor interpretation of DM.1, κ_act = 1 in galactic-natural units (where the time unit is left implicit; in practice the SPARC analysis used Gyr, but the DM.1 derivation was unit-agnostic).

**Calibration in canonical ED.** Set by dimensional convenience in DM.1 §2. The DM2 production-run universality test (σ(κ_act)/mean ≈ 2.1% across SPARC galaxies) is consistent with a single fundamental value but does not pin it absolutely; the universality is up to a global rescaling.

**Structural origin.** Not directly derived from primitives. Acts as an effective coupling whose value should in principle emerge from how strongly kinematic activity sources temporal tension at the substrate level, but no such derivation has been carried out.

### 1.3 c — speed of light, implicit in T's identification as slow-time

**Role.** If T is a dimensionless fractional time-rate (slow-time), the geodesic-equation force per unit mass is `a = c² · ∇T`. The constant c enters not through ED's PDE structure directly (the PDE is non-relativistic-looking) but through the *interpretation* of what T physically is.

**Status.** A fundamental constant of nature, not an ED-specific constant. Its appearance in the slow-time interpretation is a structural commitment about T's physical nature, not a parameter introduced by ED.

---

## 2. The Einstein-like relation: structural derivation

### 2.1 The form of the relation

BTFR.08 derived the relation `D_T = c² · κ_act` from a single requirement: that the cylindrical-curvature term `(D_T/R) · ∂_R T` cancels exactly against the self-consistency-induced term `(κ_act · c² / R) · ∂_R T`. The cancellation is the structural feature that gives canonical ED a 2D-Cartesian Helmholtz operator with a K₀-log far-field.

The derivation involves no hidden factors. Tracing every coefficient:

- `v_T² = R · c² · |∂_R T|`: from the geodesic equation `a = c² · ∇T` and circular-orbit balance `v² = R · a`. **No factor of 2** (the geodesic equation in the weak-field static limit has no factor of 2, unlike the Schwarzschild metric expansion which has `g_00 = -(1 - 2GM/rc²)`; the factor of 2 there is in the metric, but the resulting force per unit mass is `c² · ∂_r(GM/rc²) = GM/r²`, with no leftover factor).
- `A = v_total²/R² = (v_baryon² + v_T²)/R²`: kinematic identity for axisymmetric circular flow. **No factor of 1/2** (the activity index in DM.1 §2 is defined without a kinetic-energy-like 1/2; if one wanted to redefine A → A/2, the corresponding redefinition of κ_act → 2κ_act would absorb the factor and leave the structural form unchanged).
- `S = κ_act · A`: the coupling. No hidden factor.
- The cylindrical-Laplacian term `(1/R) · ∂_R T`: standard result with no factor.

The cancellation condition is therefore **exactly D_T = c² · κ_act**, with no factors of 2, π, or 1/2. The relation is dimensionally and algebraically clean.

### 2.2 The Einstein-relation interpretation

The relation `D = c² · τ` is the relativistic analog of the standard Einstein relation in random-walk theory:

> Standard Einstein relation:   D = (k_B T_thermal / m) · τ_friction = v_thermal² · τ_friction

For thermal random walks, `v_thermal² = k_B T / m`, giving D = v_thermal² · τ.

For relativistic random walks (in a substrate where information propagates at c), `v_thermal → c`, giving:

> Relativistic Einstein relation:   D = c² · τ.

If ED's temporal-tension propagation is *physically* a relativistic random walk through some substrate (e.g., the event-density discretization), then `D_T = c² · κ_act` would be the natural prediction of the substrate physics, with κ_act playing the role of "characteristic step time" and D_T being the resulting macroscopic diffusion coefficient.

This interpretation is structurally compatible with ED's primitives: the framework is built on a substrate of events that propagate at finite speed, and a coarse-grained continuum equation could naturally have an Einstein-relation structure. **Whether this is what ED actually predicts depends on whether a foundational derivation has produced D_T from substrate parameters, which I do not have direct evidence for.**

### 2.3 Factor-of-2 / factor-of-π checks

Three places where factors might hide:

- **Random-walk dimensionality.** The Einstein relation in 1D vs 3D random walks differs by a factor: D_1D = ⟨x²⟩/(2τ), D_3D = ⟨r²⟩/(6τ). The relevant ED quantity is D_T as it appears in the PDE, which is the 3D-isotropic diffusion coefficient. Standard convention has D_T defined such that the 3D diffusion equation is `∂_t T = D_T · ∇²T`, with no factor of 2 or 6 in front of D_T. Under this convention, the relation `D_T = c² · κ_act` has no random-walk-dimensionality factor.

- **Source convention.** If the source enters the PDE as `−4π · κ_act · A` (Newton-Poisson convention) instead of `−κ_act · A`, then κ_act → κ_act/(4π) and the relation becomes `D_T = c² · κ_act / (4π)`. Standard ED convention has no 4π factor, so this is moot for ED but worth noting.

- **Geodesic-equation sign and factor.** In the weak-field static limit of GR, the geodesic equation gives `a = -∇Φ` with Φ = c² · T. So a = -c² · ∇T. The sign matters for the sign convention of T; the magnitude has no factor.

**Conclusion: in canonical ED conventions, the Einstein-like relation is exactly D_T = c² · κ_act, with no hidden factors of 2, π, or fractional powers.** Any numerical mismatch in canonical ED (§3) cannot be repaired by hidden factors.

---

## 3. Numerical check of canonical ED

### 3.1 Cluster-anchored D_T

D_T = 2.1 × 10²⁷ m²/s (DM.0 §2 cluster-merger-lag fit).

c² = 9.0 × 10¹⁶ m²/s².

Required κ_act for the Einstein-like relation:

> κ_act = D_T / c² = 2.1 × 10²⁷ / 9.0 × 10¹⁶ ≈ 2.3 × 10¹⁰ s.

Converting: 2.3 × 10¹⁰ s ≈ 730 Gyr ≈ 53 × t_H (where t_H ≈ 13.8 Gyr is the Hubble time).

### 3.2 Galactic-anchored κ_act

In DM.1 §2, κ_act is set as a dimensional anchor in galactic-natural units, with the convention κ_act = 1. The actual numerical value in SI depends on what time unit is implicit in "1":

- If "κ_act = 1 second": κ_act ≈ 1 s → ratio to required value ≈ 2.3 × 10¹⁰. Off by factor ~10¹⁰.
- If "κ_act = 1 Gyr": κ_act ≈ 3.16 × 10¹⁶ s → ratio ≈ 730. Off by factor ~700.
- If "κ_act = 1 Hubble time": κ_act ≈ 4.35 × 10¹⁷ s → ratio ≈ 53. Off by factor ~50.
- If "κ_act = 53 Hubble times": κ_act ≈ 2.3 × 10¹⁰ s → ratio ≈ 1. **Einstein-like relation satisfied.**

The DM2 production-run universality test (σ/mean ≈ 2.1%) measures the relative consistency of κ_act across galaxies, not its absolute value. The absolute value is only meaningful if a normalization convention is fixed. In the SPARC fits, κ_act = 1 was the dimensional anchor in the chosen unit system (kpc, Gyr, M_⊙), and the production-run analysis was internally consistent without needing to identify the absolute value.

### 3.3 Honest reading of the mismatch

The cluster-anchored D_T and the galactic-anchored κ_act do not satisfy the Einstein-like relation in any natural unit system. The mismatch is:

- Factor of ~10⁶–10⁷ in SI (if κ_act = 1 s).
- Factor of ~700 in Gyr-natural units.
- Factor of ~53 in Hubble-time-natural units.

**This is too large to be explained by hidden factors of 2, π, or 4π.** It is either:

- (P1) A genuine structural discrepancy. ED's D_T (relativistic-substrate-derived) and κ_act (effective-galactic-coupling) are physically different quantities; the Einstein-like relation does not hold structurally.

- (P2) A calibration issue. The cluster-anchored D_T is correct, but κ_act = 1 in galactic-natural units corresponds to a *different* foundational quantity than what appears in the temporal-tension PDE. A foundational re-derivation linking κ_act to D_T via the substrate physics would yield κ_act ≈ 2.3 × 10¹⁰ s ≈ 53 t_H, and the galactic SPARC universality result of "κ_act = 1" should be interpreted as the ratio (κ_act_actual / κ_act_natural-unit-anchor), which is universal, not as the absolute value.

- (P3) Conceptual mismatch. T as it appears in DM.1's PDE may not be the dimensionless slow-time of the GR-like geodesic interpretation. If T_canonical = c² · T_slow-time (T_canonical has units of velocity²), then the apparent mismatch evaporates: Reading B's `γ = D_T/κ_act` is the "coupling for T_canonical", and the equivalent relation for T_slow-time is just γ = c², which IS the structural Einstein-like relation in the appropriate variable.

(P3) is particularly attractive because it would mean the canonical-ED constants *are* consistent with the slow-time interpretation, just expressed in a different dimensional convention.

### 3.4 Checking P3

If T_DM.1 = c² · T_slow-time, then:

- v² = -R · γ · ∂_R T_DM.1 = -R · γ · c² · ∂_R T_slow-time
- For consistency with v² = R · c² · |∂_R T_slow-time|, we need γ = 1 (dimensionless).
- γ = D_T/κ_act = 6.97 × 10⁴ m²/s² in galactic units (when D_T is in kpc²/Gyr and κ_act in Gyr). In SI: γ = (kpc/Gyr)² · 1 ≈ 9.6 × 10⁵ m²/s² (since 1 kpc/Gyr ≈ 978 m/s).
- For γ = 1 (dimensionless), we'd need to be in units where γ · 1 has the right value. In velocity-squared units, γ ≈ 9.6 × 10⁵ m²/s² is much smaller than c² ≈ 9 × 10¹⁶ m²/s².

The ratio γ/c² ≈ 10⁻¹¹. So under interpretation P3, the discrepancy is even *larger* than under direct reading. Reading B's γ does not equal c²; they differ by 11 orders of magnitude.

So P3 doesn't repair the discrepancy. The honest conclusion is **P1 or P2**: either the Einstein-like relation does not hold structurally in ED, or κ_act needs a deep re-derivation that has not been carried out.

### 3.5 What a foundational derivation would look like

To resolve between P1 and P2, ED would need to derive D_T from substrate primitives explicitly. The natural derivation chain:

1. ED's substrate has a characteristic event-time τ_event (perhaps related to Planck time, perhaps to the cosmological time t_H, perhaps to something intermediate).
2. Information about temporal-tension corrections propagates between events at characteristic speed v_prop. If v_prop = c (lightlike propagation), the random-walk diffusion coefficient is D_T = c² · τ_event.
3. The activity-coupling κ_act is the phenomenological "response time" of T to a given activity input. Its structural value would be κ_act = τ_event (or some O(1) factor times τ_event).
4. Therefore D_T = c² · κ_act exactly, and any numerical mismatch is a sign that one of D_T or κ_act has been mis-calibrated relative to the substrate physics.

**This derivation has not been carried out in any of the ED arcs I have access to.** The cluster-anchor of D_T from merger-lag observations is a top-down empirical calibration, not a bottom-up derivation. The galactic-anchor of κ_act is similarly empirical. Without the substrate-level derivation, the Einstein-like relation is "hypothetically required" rather than "structurally forced."

---

## 4. Consequences for BTFR

### 4.1 Under P1 (relation not structural)

If the foundational derivation does not produce the Einstein-like relation, the BTFR.08 analysis collapses: the cylindrical-curvature cancellation does not hold structurally, the operator remains close to canonical cylindrical screened-Poisson, and BTFR.06's anisotropy requirement is the canonical extension path.

In this case, BTFR.08 has shown a *possibility* (the slow-time interpretation gives a different operator) but not a *necessity*. The BTFR sub-arc verdict reverts to BTFR.07's three-option table, with Option A (anisotropy + ν) remaining the most parsimonious BTFR-compatible extension of canonical ED.

### 4.2 Under P2 (relation holds after foundational re-derivation)

If a foundational substrate derivation produces D_T = c² · κ_act with κ_act ≈ 53 t_H (or whatever value the substrate physics dictates), then:

- BTFR.08's analysis applies in full.
- The 2D-Cartesian-Helmholtz operator with K₀ Green's function is canonical ED's actual structure.
- C1 (log far-field) is satisfied automatically over the entire SPARC galactic regime.
- C2 (√M_b coupling) is still not repaired; the slope-2 result of BTFR.08 §4.4 stands.

In this case, the *minimal* BTFR-compatible ED extension is just the C2 fix (Route II-A or II-B). The anisotropy is not required.

### 4.3 The cluster anchor under P2

Under P2, the cluster-anchored D_T = 2.1 × 10²⁷ m²/s is consistent with the Einstein-like relation if and only if κ_act ≈ 53 t_H. The DM.1-anchor κ_act = 1 in galactic-natural units would then be reinterpreted as a relative anchor (κ_act_actual / κ_act_universal = 1 ± 2.1%), not an absolute one.

The merger-lag prediction would need re-derivation to confirm consistency: the cluster-scale time scales involved in the merger lag must be consistent with κ_act ≈ 53 t_H. This is a non-trivial check; the cluster merger-lag observation gives a delay time of order Gyr, not 100s of Gyr, so the relevant time scale in the merger physics is probably λ⁻¹ = t_H, not κ_act. **The merger-lag derivation only sees D_T directly through L = √(D_T/λ), not through κ_act.** So the cluster anchor is consistent with any value of κ_act, as long as D_T and λ are calibrated correctly. P2 is not refuted by the cluster anchor.

### 4.4 The galactic anchor under P2

Under P2, the galactic universality of κ_act (σ/mean ≈ 2.1% across SPARC) is preserved as a *relative* universality. The absolute value would be κ_act ≈ 53 t_H. The DM2 numerical fit produced kappa_act_fit ≈ 0.997 in galactic-natural units (DM.1-anchor convention). Under P2, this should be reinterpreted as kappa_act_actual ≈ 0.997 × 53 t_H ≈ 53 t_H, not as 1 Gyr or any other "natural" galactic timescale.

The DM2 production-run rotation curves were computed with the canonical (linearized) PDE, so they don't reflect the self-consistent 2D-Cartesian-Helmholtz operator. The BTFR slope of 0.24 from the run is a property of the linearized, canonical-ED prediction, not of self-consistent ED. **A re-run with the self-consistent equation under P2 would produce a different (presumably better-shaped) prediction.**

---

## 5. Structural verdict

> **The Einstein-like relation `D_T = c² · κ_act` is structurally permitted but not currently demonstrated in ED.** The relation has the canonical form of a relativistic random-walk Einstein relation (D = c²·τ), with no hidden factors. ED's primitives do not forbid it; a substrate-level derivation could plausibly produce it. **But the cluster-and-galactic-scale calibration of canonical ED does not realize it numerically**, with mismatch factors of ~50 (in t_H units) to ~10⁶ (in SI). This mismatch is too large to be explained by factors of 2 or π and indicates either:
>
> - **(P1) The relation is not structural.** D_T and κ_act are independent ED constants, and the BTFR.08 cancellation requires postulating D_T = c²·κ_act as an additional constraint not implied by the existing foundations. BTFR.06's anisotropy path remains the canonical extension.
>
> - **(P2) The relation is structural, but the canonical calibration is incomplete.** A foundational derivation linking D_T and κ_act via substrate physics would produce the Einstein-like relation automatically, with κ_act ≈ 53 t_H as the absolute value. The DM.1-anchor κ_act = 1 is a relative anchor compatible with this re-interpretation. BTFR.08's analysis applies in full; only the C2 fix is needed for BTFR derivation.
>
> **The choice between P1 and P2 cannot be made from the BTFR analysis alone.** It requires a foundational re-derivation of D_T and κ_act from ED's substrate primitives — work that has not been done in any arc I have access to.

---

## 6. The honest BTFR verdict, accounting for §5

Putting BTFR.02–09 together:

- Canonical linearized ED (BTFR.02–07): does not derive BTFR. Slope-0.24 numerical fit consistent with C1 + C2 structural failures.
- Self-consistent ED with Einstein-like relation (BTFR.08): repairs C1 automatically (gives flat curves with log kernel). Slope-2 BTFR. C2 still fails.
- Self-consistent ED without Einstein-like relation (BTFR.06's path): repairs C1 via postulated anisotropy. Slope-2 BTFR. C2 still fails. Same C2 problem.

**In neither case does ED naturally derive slope-4 BTFR.** The C2 condition is the genuine and persistent structural obstacle. Whether C1 is repaired automatically (via Einstein-like relation) or via postulated anisotropy is the foundational question, but it does not affect whether ED can derive BTFR — only how parsimoniously it can derive a slope-2 BTFR.

The honest statement of where things stand:

> Canonical ED, properly self-consistent, predicts **flat rotation curves with slope-2 BTFR**, regardless of whether the cancellation is achieved by the Einstein-like relation or by anisotropy. **Empirical BTFR is slope 4. ED does not derive this without an additional structural commitment** (Route II-A: a₀-weighted coupling; Route II-B: sublinear source functional; Route C: nonlinear ED variant).

The BTFR sub-arc has therefore identified:
1. The structural reason canonical ED fails BTFR (C1 + C2).
2. Which structural fix repairs C1 (Einstein-like relation OR anisotropy).
3. Which structural commitments would repair C2 (any of Routes II-A/B/C).
4. None of the C2 fixes emerge automatically from ED's existing primitives.

---

## 7. Recommended Next Steps

Three concrete next steps, ranked by structural priority:

1. **BTFR.10 — Substrate derivation of D_T from ED primitives.** Examine whether ED's substrate (event-density discretization, propagation rules) admits a derivation of D_T as a macroscopic diffusion coefficient. If yes, identify the implicit κ_act and test whether D_T = c² · κ_act holds. Output: foundational evidence for or against the Einstein-like relation. This is the only way to settle P1 vs P2.

2. **C2 structural search, independent of C1.** Examine whether ED's source construction admits a √M_b-yielding form without imported MOND machinery. Specifically: investigate whether the ED-derived acceleration scale c·H_0 (within factor 6 of MOND's a₀) emerges naturally as the coupling cutoff in some structural derivation. If yes, ED's a₀-equivalent is automatic and Route II-A becomes parameter-free. If no, Route II-A requires postulating ν(a/a₀) ad hoc.

3. **Pivot to DM.5 closure with full BTFR context.** If the foundational work in (1) and (2) is too large for the current arc's bandwidth, write DM.5 with BTFR.02–09 as the structural-explanation context. The verdict becomes: *Canonical ED fails BTFR. Self-consistent ED with the Einstein-like relation gives slope-2 BTFR with flat curves; the relation's structural status is an open foundational question (BTFR.10). The slope-4 empirical BTFR requires an additional structural commitment that no version of ED examined here provides without ad-hoc assumption.*

The BTFR.09 finding — that the Einstein-like relation is structurally permitted but not demonstrated — is the right note to close BTFR on. It is honest about what we know (the slow-time interpretation gives a structurally cleaner equation), what we don't know (whether the substrate forces the Einstein-like relation), and what's left to do (the foundational derivation in BTFR.10, or pivot to DM.5).

Status: complete.
