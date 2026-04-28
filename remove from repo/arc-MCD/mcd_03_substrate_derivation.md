# MCD.3 — Substrate-Level Derivation of Nonlinearity in the Many-Chain Action

**Date:** 2026-04-27
**Arc:** Many-Chain Dynamics — fourth memo (substrate-derivation pivot)
**Status:** Direct examination of whether ED's substrate physics *forces* any of the three nonlinearity routes (N1, N2, N3) identified in MCD.2 §4.3. **Honest finding: none of the three is forced by ED's currently-articulated substrate primitives. N1 (non-quadratic kinetic term) is allowed but suppressed at galactic scales by standard effective-field-theory power-counting arguments. N2 (non-quadratic potential V(T)) is conceptually plausible if the substrate-level relationship between event-density ρ and slow-time T has the right structure, but ED-07 does not specify this relationship explicitly enough to derive it. N3 (tensor-gravity beyond weak-field) is irrelevant to galactic-scale BTFR because galactic accelerations are firmly in the weak-field regime.** This is the third independent arc (after DM.1 and DM.G) to converge on the linearity wall: ED's PDE structure, taken at face value, cannot produce slope-4 BTFR. **Provisional program-level verdict: ED's currently-articulated substrate physics does not have the structural resources to produce nonlinear emergent gravity at galactic scales without an additional foundational commitment that has not yet been made.** The MCD arc should close at MCD.5 with a refutation analogous to DM.G.4. **The persistent open question — whether ED's substrate has hidden structure (e.g., the BTFR.09 P2 reading of the Einstein-like relation, or a substrate-level derivation of a non-trivial ρ-T relationship) that would change this verdict — is a foundational research question that exceeds MCD's scope and must be addressed at the substrate-physics level before any further gravitational-sector arc.**
**Predecessor:** MCD.2 (linear field equation under canonical Lagrangian).
**Successor:** MCD.4 (gravitational-limit consequences if MCD.3 closes with negative verdict; or pivot to fallback path); MCD.5 (decision memo).

---

## 1. The core question, restated

MCD.2 §4 established that the canonical Lagrangian construction (quadratic kinetic term, quadratic potential, linear-in-v_T² activity coupling) produces a linear field equation for T. **To escape the DM-arc linearity wall, MCD must adopt one of three nonlinearity routes:**

- **N1**: Non-quadratic kinetic term `F((∇T)²)`, replacing `(1/2)(∇T)²`. Produces MOND-style operator nonlinearity.
- **N2**: Non-quadratic potential `V(T)` beyond the canonical `(1/2)λ²T²`. Produces polynomial nonlinearity.
- **N3**: Tensor structure for slow-time (replacing scalar T with metric tensor g_μν). Produces Einstein-equation nonlinearity in strong-field regimes.

The MCD.2 verdict noted that these can be *postulated* but the structural payoff over MOND requires that they be *derived* from ED's substrate physics. **MCD.3's task is the derivation check: does ED's substrate physics force any of N1, N2, N3?**

If yes, MCD has a path to nonlinear emergent gravity that is structurally-rooted rather than postulated. If no, MCD's many-chain limit is canonical-ED-equivalent and the arc closes with refutation.

---

## 2. The substrate primitives

For the derivation check, we work with ED's substrate-level primitives as articulated in ED-07 and the canonical foundational documents. The relevant ingredients:

### 2.1 Event density ρ

The local rate of micro-event production. ED-07 §2.1: "Event Density is the local rate of becoming: the number of micro-events produced per unit of internal evolution." A scalar field over substrate locations; non-negative; defines the pace of physical processes.

### 2.2 Local update rule (becoming rate)

The substrate-level dynamics that extends a chain by one micro-event step. Not articulated as a single explicit formula in ED-07, but governs how chains propagate from one event to the next. Locality assumption: the next event depends only on the chain's current state and immediate neighborhood.

### 2.3 ED gradients, compression, boundaries, horizons

Spatial variation in ρ produces gradients ∇ρ. Compression: regions where ρ rises sharply (high "event accumulation rate"). Rarefaction: regions where ρ falls. Horizons: where participation across regions becomes impossible (causal disconnection).

### 2.4 Slow-time T and its geometric meaning

T is the slow-time field, dimensionless, encoding fractional reduction in local becoming rate: `dτ_proper / dt_global = 1 − T` to leading order. Geometric meaning: chains experience slowed local time in high-T regions.

**Relationship between ρ and T:** ED-07 treats both fields as related ("regions with higher ED produce events more rapidly") but does not give an explicit functional relationship `T = T(ρ)` or `ρ = ρ(T)`. This is a foundational gap that bears directly on the N2 question (§4 below).

### 2.5 Chain geometry and chain bundles

A 1-chain is a single propagation track of micro-events. Chain bundles are coherent collections (stars, planets, galaxies). The bundle's collective "internal pattern of becoming" is what the path-of-easiest-updating principle preserves.

### 2.6 ED-07's principle of least disruption

> "A system tends to follow the path that minimizes disruption to its internal pattern of becoming. Three criteria: (a) ED gradient along the path is minimal; (b) internal micro-event structure remains maximally coherent; (c) participation with the surrounding field is least strained."

MCD.1 established that criterion (a) (gradient minimization, A1.d) and the proper-time-extremization (A1.c) coincide at the single-chain level. Criteria (b) and (c) — "maximal coherence" and "least strained participation" — were not given precise mathematical content in MCD.1; they are potentially separate principles that could provide structural input to the nonlinearity question.

---

## 3. N1 — Non-quadratic kinetic term

### 3.1 The structural question

Does ED's substrate physics force the Lagrangian to contain `F((∇T)²)` for some non-quadratic F? Equivalently: is the leading kinetic term in the coarse-grained effective field theory genuinely non-quadratic?

### 3.2 Effective-field-theory power-counting

The standard argument: any local effective field theory derived from a microscopic substrate has, at long wavelengths (low momenta), a kinetic term that is dominantly quadratic in derivatives. Higher-order corrections like `(∇T)⁴` or `(∇²T)²` are present but suppressed by powers of `k/Λ` where Λ is the substrate's UV cutoff and k is the momentum scale of interest.

For galactic-scale T: typical T values are O(v²/c²) ≈ 10⁻⁷, typical gradients |∇T| ≈ T/L_gal ≈ 10⁻⁷/10²¹ m ≈ 10⁻²⁸ m⁻¹. The substrate UV scale, if associated with the Planck scale, is Λ ≈ 10³⁵ m⁻¹. The ratio is `|∇T|/Λ ≈ 10⁻⁶³`, vanishingly small.

**Higher-order kinetic corrections are therefore suppressed by ~10⁻⁶³ relative to the quadratic term at galactic scales.** They cannot produce O(1) deviations from linear field equations.

### 3.3 Possible escapes from EFT power-counting

Three structural mechanisms could evade the EFT suppression:

- **(N1.a) Non-trivial UV fixed point.** If ED's substrate physics has a conformal or otherwise non-trivial UV completion (rather than being an asymptotically-free or asymptotically-safe theory with a clean Λ), the EFT power-counting may not apply. Candidate: ED's substrate as a critical phenomenon at all scales.
- **(N1.b) Field-redefinition obscured nonlinearity.** The natural "EFT field" might not be T directly but some non-linear function of T. In that case, T's effective Lagrangian could appear non-quadratic, while the underlying field is quadratic.
- **(N1.c) Non-perturbative corrections.** Discrete-substrate effects (instantons, solitons, topological defects) that don't appear in any perturbative EFT expansion.

**Status of these escapes:** speculative. None is established in ED's foundational documents. (N1.a) would require ED's substrate to be a non-trivial CFT, which is not currently claimed. (N1.b) would require identifying the "right" EFT field, which is open. (N1.c) requires explicit non-perturbative analysis that has not been done.

### 3.4 Verdict on N1

> **N1: allowed but not forced.** Standard EFT power-counting suppresses non-quadratic kinetic terms at galactic scales by factors of ~10⁻⁶³. Three structural escape routes exist (non-trivial UV completion, field-redefinition, non-perturbative corrections) but none is currently established in ED.
>
> **MCD cannot derive N1 from currently-articulated substrate physics.**

---

## 4. N2 — Non-quadratic potential V(T)

### 4.1 The structural question

Does ED's substrate physics force `V(T)` to contain terms beyond the canonical `(1/2)λ²T²`? Equivalently: is the screening rate λ effectively T-dependent, or is there self-interaction of T at the substrate level?

### 4.2 The ρ-T relationship gap

The cleanest path to N2 is through a non-trivial relationship between ρ and T. If T is a non-linear function of ρ (e.g., logarithmic), then the canonical PDE for T sourced by ρ may have non-quadratic effective potential when expressed in terms of T.

ED-07 articulates ρ and T as related but does not give the explicit functional relationship. Three plausible candidates:

- **(R1) Linear:** `T = α · (ρ_ref − ρ)` for some reference ρ_ref. Quadratic V(T) preserved.
- **(R2) Logarithmic:** `T = log(ρ_ref / ρ)`. Then ρ = ρ_ref · exp(−T), and any "λ²·ρ"-like term in the substrate equation becomes `λ²·ρ_ref·exp(−T)`, which expanded in T gives `λ²·ρ_ref·(1 − T + T²/2 − T³/6 + ...)`. **Non-quadratic V(T)** with all polynomial corrections.
- **(R3) Power-law:** `T = (ρ/ρ_ref)^α` for some α. Similar non-quadratic structure.

**Under (R2) or (R3), N2 holds and the field equation is nonlinear.** The substrate-level question is whether ED's foundational principles select (R1), (R2), (R3), or something else.

### 4.3 Why ED-07 doesn't settle this

ED-07 §3 says: "A region with higher ED produces micro-events more rapidly. Thus, the 'tick rate' of any clock is a direct reflection of the ED field in which it is embedded."

This is consistent with (R1), (R2), or (R3) — any of them gives the qualitative claim "high ρ ↔ fast clocks ↔ low T." The quantitative form is not constrained by ED-07's narrative.

The choice between (R1) and (R2) has structural consequences:

- Under (R1), T-shifts produce additive changes in clock rate. Slow-time is a linearly-shifted version of becoming rate.
- Under (R2), T-shifts produce multiplicative changes in clock rate. This is the standard GR convention (gravitational time dilation factor `e^{−T}` for some normalization).

**The standard GR convention favors (R2).** In GR, the metric component `g_00 = −e^{−2Φ/c²}` (in fully nonlinear form) gives `dτ_proper/dt = e^{−Φ/c²}`. Linearizing: `1 − Φ/c² + (Φ/c²)²/2 − ...`. The quadratic correction `(Φ/c²)²/2` is a real GR effect, present at second order.

**If ED inherits this convention (T = Φ_GR/c² in slow-time), then (R2) is the natural relationship and N2 is at least allowed at second order in T.**

### 4.4 Magnitude of the effect

For galactic T ~ 10⁻⁷, the ratio of quadratic to linear corrections is `T/2 ~ 10⁻⁷/2 ≈ 5 × 10⁻⁸`. This is small but not vanishingly small (unlike N1's 10⁻⁶³ suppression).

However: even with non-quadratic V(T), the field equation's *nonlinearity* in T enters at order T³ (since `V'(T) = λ²T − λ²T²/2 + ...` has a T² correction; the field equation `∇²T = V'(T)` becomes `∇²T = λ²T − λ²T²/2`). For the disc-integrated source `M_eff`, the nonlinear correction is suppressed by `T_typical ≈ 10⁻⁷`, giving a subleading contribution far smaller than the M_b-linear leading term.

**Even if N2 holds, it does not produce O(1) nonlinearity at galactic scales.** The relevant regime for BTFR is firmly in the weakly-nonlinear T regime, where polynomial V(T) corrections are perturbative around the quadratic.

The MOND-style nonlinearity required for slope-4 BTFR is **non-perturbative in (∇T)/a₀**, not perturbative in T itself. Polynomial V(T) corrections are the wrong type of nonlinearity.

### 4.5 Verdict on N2

> **N2: allowed and weakly motivated by GR-convention parallels (R2 reading), but the nonlinearity it produces is perturbative in T, not the non-perturbative nonlinearity required for MOND-like deep-regime behavior.**
>
> **N2 is the wrong type of nonlinearity for galactic-scale BTFR.** It corresponds to second-order GR corrections (small at galactic scales) rather than to the deep-acceleration interpolation function needed for slope-4.

---

## 5. N3 — Tensorial slow-time structure

### 5.1 The structural question

Does ED need more than a scalar T? Does the gravitational sector require a metric tensor g_μν rather than the slow-time scalar?

### 5.2 The weak-field reduction

In GR weak-field: the metric can be written `g_μν = η_μν + h_μν` with `|h_μν| ≪ 1`. In appropriate gauge, the metric is fully determined by a single scalar potential Φ:

> g_00 = −(1 + 2Φ/c²),    g_ij = (1 − 2Φ/c²) δ_ij.

The scalar Φ contains all the gravitational degrees of freedom relevant to slow-moving particles. Both `g_00` and the spatial `g_ij` components are determined by the single scalar, with sign correlations fixed by the metric ansatz.

**ED's slow-time scalar T plays this role:** if `T = Φ/c²`, the slow-time framework reproduces all weak-field GR effects on slow-moving chains. The chain equation `a = c²·∇T` is exactly the Newtonian limit of geodesic motion in this metric.

### 5.3 Nonlinearity at strong-field

GR's nonlinearity (Einstein equation `G_μν = 8πG T_μν^matter` with `G_μν` nonlinear in `g_μν`) becomes important when:

- `|h_μν|` is O(1), i.e., near black holes or neutron stars.
- Gravitational waves are present (transverse-traceless modes that can't be written in scalar form).
- Cosmological-scale physics where the metric varies non-trivially.

**For galactic-scale BTFR, none of these regimes apply.** Galactic T values are O(10⁻⁷); gravitational waves are not relevant to rotation-curve dynamics; cosmological-scale physics is far above galactic scales.

**N3 nonlinearity is therefore irrelevant to BTFR.** Even if ED has a hidden tensor structure that emerges in strong-field regimes, this does not affect the galactic-scale prediction.

### 5.4 Verdict on N3

> **N3: allowed (and probably required for full ED-GR consistency in strong-field regimes), but irrelevant to galactic-scale BTFR.**
>
> **N3 cannot rescue MCD's BTFR prediction.**

---

## 6. The honest aggregate verdict

Combining N1, N2, N3:

| Route | Forced? | Allowed? | Relevant to BTFR? | Status |
|---|---|---|---|---|
| **N1** (non-quadratic kinetic) | No | Yes (with caveats) | Yes if forced | **Suppressed at galactic scales by EFT** |
| **N2** (non-quadratic V) | No | Yes (mild) | No (wrong type) | **Wrong nonlinearity for BTFR** |
| **N3** (tensor structure) | No | Yes | No (weak-field) | **Irrelevant to galactic regime** |

**None of the three nonlinearity routes is forced by ED's currently-articulated substrate physics.** Of the three, only N1 has the right *type* of nonlinearity to produce MOND-like behavior, but it is suppressed at galactic scales by ~10⁻⁶³.

### 6.1 What this means for MCD

**MCD's many-chain limit, under the canonical Lagrangian construction, gives a linear field equation.** No structural escape route from the DM-arc linearity wall has been identified. MCD reproduces the canonical-ED PDE at the field-equation level and the same slope-2 BTFR result follows under appropriate conditions.

**MCD does not provide a route to slope-4 BTFR within ED's currently-articulated framework.**

### 6.2 The pattern across three arcs

This is the **third independent arc** to converge on the linearity wall:

| Arc | Approach | Reason for failure |
|---|---|---|
| **DM.1** | T sourced by kinematic activity | C2 fails: M_eff ∝ M_b under self-consistency |
| **DM.G** | T sourced by disc geometry | C2 fails: same linearity-plus-disc-integration trap |
| **MCD** | Path-of-easiest-updating action principle | Canonical Lagrangian gives linear field equation; substrate physics doesn't force nonlinearity |

**Three structurally-independent attacks have all failed at the same wall.** This is strong evidence that the linearity wall is robust and not an artifact of any specific source-functional choice or framework. **The wall is fundamental to ED's currently-articulated PDE structure, not contingent on any single arc's hypothesis.**

---

## 7. Provisional program-level verdict

> **ED, in its currently-articulated form, does not have the structural resources to produce nonlinear emergent gravity at galactic scales.** The linearity wall is robust across multiple independent approaches, and MCD's substrate-derivation analysis confirms that none of the three nonlinearity routes (N1, N2, N3) is forced by ED's existing primitives.
>
> **MCD should close at MCD.5 with refutation analogous to DM.G.4.** The single-chain principle is GR-equivalent (no theoretical advance over GR); the many-chain limit is canonical-ED-equivalent (DM-arc result reproduced); the substrate-derivation check finds no forced nonlinearity (this memo).

### 7.1 What is *not* refuted by this verdict

- **ED's foundational structure** (Theorems N1, GR.1, spin-statistics, Cl(3,1) uniqueness, UV-FIN, etc.) is unaffected. The linearity wall is at the gravitational-sector PDE, not at the substrate level.
- **ED's qualitative reproduction of relativistic phenomena** (ED-07 chapters 3–7) is unaffected. The path-of-easiest-updating principle correctly recovers GR weak-field at single-chain level.
- **ED's cluster-scale predictions** (merger-lag from canonical D_T, λ) are unaffected.
- **ED's universality of the gravitational coupling** (DM.5 §3.2: σ(κ_act)/mean ≈ 2.1%) is unaffected.

### 7.2 What is refuted

- **Any claim that ED can derive slope-4 BTFR from currently-articulated primitives.** The claim now has three independent structural arguments against it (DM.1, DM.G, MCD).
- **The expectation that "trying yet another source functional" or "trying yet another action principle" will rescue ED's BTFR derivation.** The wall is structural and indifferent to source-functional choice.

### 7.3 What remains genuinely open

- **Whether ED's substrate physics can be augmented with additional foundational commitments** (the BTFR.10 candidate; substrate-level ρ-T relationship; entropic-principle articulation) that would change the verdict.
- **Whether the c·H_0 ≈ a₀ coincidence from BTFR.09** can be promoted to a structural rather than coincidental result through deeper foundational analysis.
- **Whether ED needs a fundamentally different gravitational-sector structure** (not the screened-Poisson form) to produce slope-4 BTFR. This would be a major reformulation, not a within-MCD task.

These are foundational research questions that exceed MCD's scope and the scope of any source-functional-level arc. They belong at the substrate-physics or foundational-arc level.

---

## 8. The fourth criterion: principle of least disruption beyond geodesic

ED-07 §5.1's three criteria for an inertial path were:
- (a) ED gradient along the path is minimal.
- (b) Internal micro-event structure remains maximally coherent.
- (c) Participation with the surrounding field is least strained.

MCD.1 mapped (a) onto A1.d (gradient minimization) and showed it coincides with A1.c (proper-time extremization) at the single-chain level. **MCD.1 did not give criteria (b) and (c) precise mathematical content.**

If (b) and (c) encode genuinely additional principles beyond geodesic motion — e.g., an entropic component to "maximal coherence" or a non-local "participation" measure — they could provide a structural input to nonlinearity that the single-criterion MCD analysis missed.

This is speculative. Articulating (b) and (c) precisely is foundational substrate-level work, not a within-MCD task. **But it represents a genuine open route that the program-level verdict in §7 should not foreclose.** If a future foundational arc gives (b) or (c) mathematical form, it might surface a structurally-distinct fourth nonlinearity route (call it N4) that the MCD.3 analysis did not consider because it was scoped to N1, N2, N3 from MCD.2.

---

## 9. Recommended Next Steps

Three concrete next steps, in priority order:

1. **MCD.4 + MCD.5 as a combined closure pair.** Given the §7 verdict, MCD.4 (gravitational-limit consequences) and MCD.5 (decision memo) can be folded into a single closing memo. The structural conclusions are clear: linear field equation → DM-arc-equivalent → slope-2 BTFR → MCD closes with refutation. The remaining work is documentation and program-level integration. **Recommended as the immediate next step**, parallel in tone to DM.G.4.

2. **Elevate the foundational research questions identified in §7.3 to a separate Phase-2-style arc.** The three open questions — substrate-level ρ-T relationship, c·H_0 ↔ a₀ structural status, fourth-nonlinearity-route from ED-07 §5.1 (b)/(c) — are foundational substrate-physics tasks. They should be scoped as a single foundational-research arc (working title: "ED Substrate Foundations" or similar), with no expectation of immediate gravitational-sector payoff. The arc may produce a positive result that revives the gravitational-sector question, or it may confirm that ED's substrate as currently articulated is structurally limited. Either outcome is informative.

3. **Lock in the DM-arc + MCD-arc convergence finding for the program record.** Three independent arcs (DM.1, DM.G, MCD) have now reached the same structural verdict. The ED-Orientation document should be updated to record this as a stable finding: ED's gravitational-sector PDE, in its currently-articulated form, cannot derive slope-4 BTFR. This is not a refutation of ED as a research program; it is a precise statement of what the current articulation cannot do, with clear identification of where the missing structure would have to live.

The MCD arc has delivered its honest result. The single-chain principle is GR; the many-chain limit is canonical-ED; the substrate-derivation analysis finds no forced nonlinearity. The path-of-easiest-updating principle, taken at face value, is consistent and structurally clean — but it does not, by itself, produce the deep-regime nonlinearity required for empirical BTFR. **The arc closes with this verdict; the broader question (what ED would need to look like to derive BTFR) is forwarded to foundational research.**

Status: complete.
