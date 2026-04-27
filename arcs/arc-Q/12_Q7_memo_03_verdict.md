# Q.7 Memo 03 — Substage Verdict and Downstream Cascade

**Stage:** Arc Q · Q.7 · Memo 03 (substage closure)
**Date:** 2026-04-26
**Location:** `arcs/arc-Q/`
**Goal:** Integrate the results of Memo 01 (W1 + W2 closed CANDIDATE-FORCED → R-1 CLOSED) and Memo 02 (W3 + W4 closed CANDIDATE-FORCED → R-5 partial CLOSED + R-3 Q.7-side CLOSED), close W5 (pre-vacuum structure) + W6 (downstream dependency map), dispatch WFal-5 (Q.7 ⟷ Q.8 circular dependency check), issue the Q.7 substage verdict, and produce the cascade map into Q.8 (R-5 completion).
**Predecessors:** Q.1 / Q.2 / Q.3 trajectory · [`09_Q7_memo_00_outline.md`](09_Q7_memo_00_outline.md) (Q.7 Memo 00) · [`10_Q7_memo_01_lightlike_worldline.md`](10_Q7_memo_01_lightlike_worldline.md) · [`11_Q7_memo_02_excitation_lifting.md`](11_Q7_memo_02_excitation_lifting.md)
**Status:** Integration + verdict memo. Operates under the same forbidden-input discipline as Memos 00–02 (no R-5 completion; no Q.8 results; no SM specifics; no Higgs / generations / coupling constants; no F-M8 cascade target; no Yang-Mills / BRST as derivation premise). Inherits all structural commitments and falsifier dispatches from Memos 01–02.
**Purpose:** Issue the Q.7 substage verdict and prepare the GRH closure trajectory's advance to Q.8 — the **final** Q-substage before Arc Q synthesis.

---

## 1. The Q.7 Question (Restated)

### 1.1 What Q.7 was tasked to determine

Q.7 was opened (per Memo 00) to discharge three refinements outstanding after Q.3's substage closure:

- **R-1** (lightlike-worldline reformulation): how does the proper-time-degenerate lightlike-worldline structure for $\tau_g$ accommodate per-worldline accounting, and what affine-parameter machinery replaces the proper-time framework that fails when $d\tau = 0$?
- **R-5 partial** (vacuum-field aspect of $\tau_g$'s vacuum-vs-particle status): how does the framework distinguish $\tau_g$ as a propagating excitation (worldline-supported) from $\tau_g$ as a background field (non-worldline-supported)?
- **R-3 Q.7-side** (per-worldline accounting integrating Q.3's vertex-anchored commitment with the lightlike-worldline framework): how does Q.3 V4's vertex-density commitment rate lift into the affine-parameter framework, and how does the lifting reconcile fully with Primitive 11's general specification?

Q.7's full sub-feature decomposition (per Memo 00):

- **W1** Lightlike-worldline structure (forced-via-derivation; R-1 core)
- **W2** Second-quantised field/worldline correspondence (load-bearing; R-1)
- **W3** $\tau_g$ excitation vs background at the worldline level (load-bearing; R-5 partial)
- **W4** Vertex-to-worldline lifting of commitment events (load-bearing; R-3 Q.7-side)
- **W5** Pre-vacuum structure (forced-via-derivation; honest scoping)
- **W6** Downstream dependency map for Q.8 (bookkeeping)

Memos 01 and 02 closed the four substantive sub-features (W1, W2, W3, W4) at CANDIDATE-FORCED. Memo 03 closes W5 + W6 (largely bookkeeping per the Memo 00 anticipation), dispatches WFal-5, and issues the substage verdict.

### 1.2 Q.7's position in the GRH-closure trajectory

The GRH closure roadmap sequences Q.7 as the third substage: Q.2 → Q.3 → **Q.7** → Q.8 → Arc Q synthesis → cascade to Arc M.

Q.7 is the substantive bridge between vertex-level kinematics+dynamics (Q.3) and the full vacuum framework (Q.8). It carried the substantively heaviest substage load — the second-quantisation framework requirement plus the lightlike-worldline reformulation plus the vacuum-field aspect of R-5.

With Q.7 closure, the GRH closure trajectory has its second-quantised + worldline + vacuum-field-aspect framework in place. **Only Q.8's R-5 completion (zero-point aspect of vacuum) remains before Arc Q synthesis.**

### 1.3 Refinements Q.7 was responsible for

| Refinement | Description | Q.7 sub-feature | Closure scope |
|---|---|---|---|
| **R-1** | Lightlike-worldline reformulation | W1 + W2 | Full (R-1 fully closed at Q.7 Memo 01) |
| **R-3 Q.7-side** | Per-worldline lift of vertex-anchored commitment | W4 | Q.7-side (combined with Q.3-side, R-3 substantively closed) |
| **R-5 partial** | Vacuum-field aspect of $\tau_g$ | W3 + W5 | Partial (vacuum-field aspect; zero-point aspect remains R-5 completion at Q.8) |

Q.7 closes 3 of the 3 refinement items it was responsible for. The 1 remaining refinement (R-5 completion) is Q.8 content.

---

## 2. Sub-Feature Integration (W1–W6)

### 2.1 W1 — Lightlike-Worldline Structure Under GRH

**Status: CLOSED — CANDIDATE-FORCED (Memo 01).**

**Key structural findings (recap from Memo 01):**

- Null-propagation derivation: GRH-4 ($\sigma_{\tau_g} = 0$) → standard relativistic kinematics (massless ⟹ null in 3+1D) → proper-time degeneracy ($d\tau = 0$) → affine parameter $\lambda$ as natural parametrisation.
- Affine-parameter machinery: $\lambda$ with affine reparametrisation freedom $\lambda \to a\lambda + b$; tangent vector $u^\mu = dx^\mu/d\lambda$ satisfies $u_\mu u^\mu = 0$.
- Per-primitive audit: P-02, P-04, P-06, P-07, P-10, P-11, P-13 all support. **No primitive forbids.**
- WFal-1 NOT triggered.

**Open items:** none.

**Downstream dependencies:**
- Q.8 inherits the affine-parameter framework for vacuum-state worldline content.

### 2.2 W2 — Second-Quantised Field/Worldline Correspondence

**Status: CLOSED — CANDIDATE-FORCED (Memo 01).**

**Key structural findings (recap from Memo 01):**

- Minimal second-quantised structure: field operator $\hat{A}^a_\mu(x)$, mode expansion in null momentum modes, creation/annihilation operators satisfying canonical commutation per Theorem 6.
- Propagator content $\Delta^{ab}_{\mu\nu}(x-y) \propto \delta^{ab} \eta_{\mu\nu} K(x-y)$ with V₁ kernel finite-width regulator inheriting from Theorems 8 + 9.
- Three structurally-equivalent worldline interpretations (expectation-value trajectories, support curves, null curves under GRH).
- WFal-2, WFal-6, WFal-8 (structural level) all NOT triggered.

**Open items:** none from W2's own scope. Full propagator details (iε prescription, vacuum-state structure) deferred to Q.8.

**Downstream dependencies:**
- Q.8 inherits the operator algebra + propagator structural form for full vacuum-state work.

### 2.3 W3 — τ_g Excitation vs Background (R-5 Partial)

**Status: CLOSED — CANDIDATE-FORCED (Memo 02).**

**Key structural findings (recap from Memo 02):**

- (E)/(B) structural distinction: excitations (zero field-operator expectation, worldline-supported, vertex-mediated commitment) vs. background fields (non-zero field-operator expectation, non-worldline-supported, mean-field content).
- Three minimal structural criteria for each (E-1/E-2/E-3 and B-1/B-2/B-3); complementary additive structure on combined states.
- Per-primitive audit: all seven primitives support; **no primitive forbids**.
- WFal-3 NOT triggered.
- R-5 partial CLOSED.

**Open items:** none from W3's own scope.

**Downstream dependencies:**
- Q.8 inherits the (E)/(B) distinction for full vacuum-state work; vacuum state itself is the limiting case of background field $A^{a, \text{cl}}_\mu \to 0$ plus zero-point quantum content.

### 2.4 W4 — Vertex-to-Worldline Lifting (R-3 Q.7-Side)

**Status: CLOSED — CANDIDATE-FORCED (Memo 02).**

**Key structural findings (recap from Memo 02):**

- Per-worldline commitment-rate accounting: $dN_{\text{commit}}/d\lambda = \rho_V(\lambda)$ in the affine-parameter framework.
- Worldline-level conservation (bandwidth, gauge-charge, Lorentz/momentum) inherited from Q.3 V1 + V2.
- Worldline-level gauge-quotient consistency lifting kinematic + vertex-level closures.
- **Full Phase-1 reconciliation:** Primitive 11's general specification invariant under worldline parametrisation choice (proper-time for timelike, affine-parameter for lightlike).
- WFal-4 NOT triggered; **WFal-7 NOT triggered at full reconciliation level**.
- R-3 Q.7-side CLOSED.

**Open items:** none from W4's own scope.

**Downstream dependencies:**
- Q.8 inherits the per-worldline accounting framework for vacuum-level vertex content (virtual vertex pairs, vacuum polarisation).

### 2.5 W5 — Pre-Vacuum Structure

**Status: CLOSED — see §3 below.**

**Memo 03 closure.** W5 specifies what Q.7's framework can say about $\tau_g$'s vacuum-related content *before* Q.8's full vacuum + zero-point work. Substantive content addressed in §3.

**Open items:** none.

**Downstream dependencies:** W5's pre-vacuum scoping defines Q.8's substantive starting point.

### 2.6 W6 — Downstream Dependency Map

**Status: CLOSED — issued in §7 below.**

**Memo 03 closure.** W6 is bookkeeping: precise inventory of what Q.8 inherits from Q.7's closure. Built from W1–W5 outputs and presented in §7 as the substantive cascade content.

**Open items:** none.

**Downstream dependencies:** W6 *is* the dependency specification.

### 2.7 Residual: WFal-5 Dispatch (Q.7 ⟷ Q.8 Acyclicity Check)

**WFal-5 — Q.7 ⟷ Q.8 circular dependency.** The falsifier asks whether Q.7's closure (especially W3 background-field aspect, W4 per-worldline lifting, W5 pre-vacuum scoping) requires Q.8's full vacuum-state content for its own definition.

*Audit at Memo 03 level.*

Q.7's closures commit to:
- **W3 (Memo 02 §2):** background-field aspect = non-zero field-operator expectation $\langle\hat{A}^a_\mu\rangle$ in some structural state. Does *not* invoke the specific structure of Q.8's vacuum state — only the operator-expectation-value content.
- **W4 (Memo 02 §4):** per-worldline commitment-rate accounting in affine-parameter framework. Does *not* invoke vacuum-level vertex content (vacuum polarisation, virtual vertex pairs) — only the excitation-content commitment-event structure.
- **W5 (this Memo §3):** pre-vacuum structure scoping. Explicitly identifies what Q.7 says (background-field aspect, worldline density, operator expectations) and what Q.8 must add (zero-point fluctuations, full vacuum-state structure, vacuum polarisation, R-5 completion).

Q.7 → Q.8 is a clean one-way dependency: Q.8 inherits Q.7's framework and supplies the vacuum-state machinery + zero-point content + vacuum-level vertex events. Q.8 does not feed back into Q.7 — the vacuum-state machinery does not modify the structural content of W1–W4 (it adds *vacuum-level* content on top of Q.7's framework, not modifies Q.7's framework itself).

**WFal-5 verdict: NOT triggered.** No Q.7 ⟷ Q.8 circular dependency identified.

The dispatch confirms W5 + W6's downstream dependency map (§7 below) is well-defined: Q.7 → Q.8 is a clean one-way dependency with no feedback loops.

---

## 3. W5 — Pre-Vacuum Structure (Closure)

### 3.1 What Q.7 can say about vacuum structure before Q.8

Q.7's framework establishes the following pre-vacuum content — i.e., what is structurally fixed about $\tau_g$'s vacuum-related behaviour without invoking Q.8's full vacuum + zero-point machinery:

#### 3.1.1 Background-field behaviour

The background-field aspect of $\tau_g$'s status (R-5 partial, W3 closure):
- Background field $\langle\hat{A}^a_\mu(x)\rangle = A^{a, \text{cl}}_\mu(x)$ is a primitive-level structural object.
- Background field is non-worldline-supported; physical content is computed from gauge-invariant Killing-form-contracted observables (per Q.3 V3 inheritance).
- Background-field configurations are individuated by gauge-equivalence-class $[A^{a, \text{cl}}_\mu]$ per Q.2 Memo 02 kinematic gauge-quotient.

The vacuum state itself (in Q.7's framework) is the *limiting case* of background field: $A^{a, \text{cl}}_\mu \to 0$ (no background field) plus the (Q.8-deferred) zero-point quantum content.

#### 3.1.2 Worldline density

In the absence of vertex events, $\tau_g$ excitations propagate freely along their null worldlines (per W2's expectation-value trajectory interpretation). In a vacuum state (no excitations + no background field), there is no $\tau_g$ worldline density — the field operator's expectation vanishes everywhere.

This is the *worldline-density-zero* characterisation of the vacuum at the W3 + W5 level: vacuum = no excitations + no background field. Q.8 will add the *zero-point* content (residual quantum fluctuations even when both excitations and background field vanish).

#### 3.1.3 Operator expectations

At the W2 + W3 level, the field operator $\hat{A}^a_\mu(x)$ has a well-defined expectation value structure on each state:
- On a one-particle state $|k, \sigma\rangle$: $\langle k, \sigma | \hat{A}^a_\mu(x) | k, \sigma \rangle = 0$ (excitation, zero expectation).
- On a coherent / background state: $\langle\Phi_{\text{bg}}|\hat{A}^a_\mu(x)|\Phi_{\text{bg}}\rangle = A^{a, \text{cl}}_\mu(x) \neq 0$ (background, non-zero expectation).
- On the vacuum state $|\Omega\rangle$: $\langle\Omega|\hat{A}^a_\mu(x)|\Omega\rangle = 0$ (vacuum, no background).

The vacuum's two-point correlator $\langle\Omega|\hat{A}^a_\mu(x)\hat{A}^b_\nu(y)|\Omega\rangle = \Delta^{ab}_{\mu\nu}(x-y)$ is the propagator (W2 §3.1.4). Its full content (iε prescription for time-ordered propagators, gauge-invariant quotient structure) is Q.8 work.

### 3.2 What is explicitly deferred to Q.8 (R-5 completion)

- **Zero-point fluctuations:** residual quantum fluctuations of the field operator in the vacuum state — distinguish ED's vacuum from a classical empty configuration.
- **Vacuum classification:** is the vacuum state $|\Omega\rangle$ unique (Poincaré-invariant), or are there multiple admissible vacuum states? Q.7 commits to *some* vacuum state existing (W2's mode expansion presumes this); Q.8 specifies which.
- **Vacuum polarisation:** virtual vertex pairs (T1 + T2 emission/absorption pairs in vacuum) modify the vacuum-state propagator structure. Q.7 does not address vacuum-level vertex events; Q.8 does.
- **Full propagator details:** iε prescription for time-ordered propagators; vacuum expectation values of operator products beyond two-point functions.
- **Λ derivation refinement:** extension of Theorem 9's V₁ + Synge content with vacuum-vertex contributions.
- **Vacuum-level commitment events:** virtual vertex pairs do not contribute observable commitment events but modify vacuum-state structure.

These constitute **R-5 completion**, Q.8's substantive load.

### 3.3 Constraints Q.7 imposes on Q.8

- **Vacuum state must extend the background-field aspect (W3).** Q.8's vacuum state must satisfy the (E)-criterion or (B)-criterion at the operator-expectation level (or some combination), with a clean reduction to the W3 framework.
- **Vacuum state must respect kinematic + vertex-level + worldline-level gauge-quotient (Q.2 + Q.3 + W4 inheritance).** Vacuum state must be gauge-invariant (or gauge-equivalence-class object).
- **Zero-point content must be UV-finite per Theorem 7.** Vacuum two-point correlators (and higher) must be finite without renormalisation.
- **Vacuum state must be compatible with the affine-parameter framework (W1).** Vacuum-state content along null worldlines must be consistent with the affine-parameter parametrisation.
- **Vacuum-level commitment events (if any) must respect R-3's substantive closure.** Virtual vertex pairs in vacuum must be vertex-anchored (per R-3 Q.3-side + Q.7-side closures).

### 3.4 W5 status

**W5: CLOSED — forced-via-derivation (honest scoping).**

Pre-vacuum structure cleanly identifies what Q.7 says (background-field, worldline density, operator expectations in non-vacuum states) and what Q.8 must add (zero-point, vacuum classification, vacuum polarisation, full vacuum-state structure). The constraints Q.7 imposes on Q.8 supply the structural framework Q.8 must operate within.

---

## 4. Refinement-Closure Summary

| Refinement | Description | Closure stage | Q.7 closure status |
|---|---|---|---|
| **R-1** | Lightlike-worldline reformulation | Q.7 Memo 01 | **CLOSED ✅** |
| R-2 partial | Gauge-quotient individuation, kinematic | Q.2 Memo 02 | (unchanged) ✅ |
| R-2 completion | Vertex-level gauge-quotient | Q.3 Memo 02 | (unchanged) ✅ |
| R-2 FULL | combined kinematic + vertex-level | Q.2 + Q.3 | FULLY CLOSED ✅✅ |
| R-3 Q.3-side | Vertex-anchored commitment specification | Q.3 Memo 02 | (unchanged) ✅ |
| **R-3 Q.7-side** | Per-worldline lift of vertex-anchored commitment | Q.7 Memo 02 | **CLOSED ✅** |
| **R-3 SUBSTANTIVE** | combined Q.3 + Q.7 sides | Q.3 + Q.7 | **SUBSTANTIVELY CLOSED ✅✅** |
| **R-3 Q.8-side** (if applicable) | Vacuum-level vertex content for $\tau_g$ commitment | Q.8 | minor; vacuum-level refinement |
| R-4 | Non-Abelian extension scoping | Q.2 Memo 01 | (unchanged) ✅ |
| **R-5 partial** | Vacuum-field aspect of $\tau_g$ status | Q.7 Memo 02 | **CLOSED ✅** |
| **R-5 completion** | Zero-point aspect | Q.8 | **outstanding** |

**Q.7 closes three refinement items (R-1, R-3 Q.7-side, R-5 partial), all at CANDIDATE-FORCED. Cumulative GRH refinement-closure progress: 6/7 items closed; 1/7 remaining (R-5 completion).** In the original 5-refinement count: R-1, R-2, R-3, R-4 fully closed; R-5 partially closed (vacuum-field aspect done; zero-point aspect outstanding for Q.8).

---

## 5. Falsifier Status Table

### 5.1 Per-falsifier status across Memos 00–03

| Falsifier | Description | Memo tested | Status | Remaining downstream tests |
|---|---|---|---|---|
| **WFal-1** | W1 primitive incompatibility | Memo 01 §6.1 | **NOT triggered** | none |
| **WFal-2** | Second-quant. framework incompat. | Memo 01 §6.2 | **NOT triggered** | Q.8 vacuum-level analog |
| **WFal-3** | $\tau_g$ excitation vs background incompat. | Memo 02 §6.1 | **NOT triggered** | Q.8 vacuum-state classification |
| **WFal-4** | Vertex-to-worldline lifting fails | Memo 02 §6.2 | **NOT triggered** | none |
| **WFal-5** | Q.7 ⟷ Q.8 circular dependency | Memo 03 §2.7 | **NOT triggered** | none |
| **WFal-6** | Theorem 6 incompat. with worldline | Memo 01 §6.3 | **NOT triggered** | none |
| **WFal-7** | P-11 incompat. (full reconciliation) | Memo 02 §6.3 (full); Memo 01 §6.4 (partial) | **NOT triggered (full level)** | none |
| **WFal-8** | UV-FIN conflict (structural) | Memo 02 §6.4 (structural); Memo 01 §3.1.4 (background) | **NOT triggered (structural level)** | Q.8 full propagator details |

### 5.2 Cumulative Q.7 falsifier-status verdict

**All eight falsifiers (WFal-1 through WFal-8) NOT triggered for Q.7 substage.**

Q.7's structural admissibility for lightlike-worldline reformulation, second-quantised correspondence, $\tau_g$ excitation/background distinction, and per-worldline commitment-event accounting closes without falsifier obstruction.

The downstream tests noted (WFal-2 vacuum-level analog at Q.8; WFal-3 vacuum-state classification at Q.8; WFal-8 full propagator details at Q.8) are *new* falsifier-tests at Q.8 scope, not residual Q.7 falsifier-tests. Q.7's own falsifier inventory is fully discharged.

---

## 6. Q.7 Verdict

### 6.1 Verdict

**Q.7 substage: CLOSED — CANDIDATE-FORCED.**

Specifically: the Q.7 substage discharges its three assigned refinements (R-1 + R-3 Q.7-side + R-5 partial) at CANDIDATE-FORCED, derives the lightlike-worldline structure (W1) and second-quantised correspondence (W2) at CANDIDATE-FORCED → R-1 closure, derives the excitation/background distinction (W3) at CANDIDATE-FORCED → R-5 partial closure, derives the vertex-to-worldline lifting (W4) at CANDIDATE-FORCED with full Phase-1 reconciliation → R-3 Q.7-side closure, scopes the pre-vacuum structure (W5) and downstream dependency map (W6) cleanly. All eight Q.7 falsifiers are NOT triggered. The GRH closure trajectory advances to Q.8 (R-5 completion) — the **final** Q-substage before Arc Q synthesis.

### 6.2 Justification

The verdict rests on the integration of Memos 01 and 02:

- **W1 + W2 (Memo 01) closed CANDIDATE-FORCED → R-1 CLOSED.** Affine-parameter machinery for null worldlines + second-quantised operator framework + propagator content via Theorem 7 inheritance; no falsifier triggered.
- **W3 (Memo 02) closed CANDIDATE-FORCED → R-5 partial CLOSED.** Excitation vs background distinction structurally clean; vacuum-field aspect settled; complementary additive structure on combined states.
- **W4 (Memo 02) closed CANDIDATE-FORCED → R-3 Q.7-side CLOSED.** Per-worldline accounting in affine-parameter framework; full Phase-1 reconciliation; R-3 substantively closed across Q.3 + Q.7.
- **W5 closed via §3 above.** Pre-vacuum structure cleanly identifies Q.7-side content vs. Q.8-side requirements.
- **W6 closed via §7 below.** Downstream dependency map for Q.8.
- **WFal-5 dispatched** (§2.7) — no Q.7 ⟷ Q.8 circular dependency.
- **All eight falsifiers NOT triggered** (§5).

The CANDIDATE-FORCED designation reflects the same conditional-forcing structure that closed Q.2 + Q.3 + Memos 01-02: specific gauge-group choice + coupling values remain empirical inheritance per Arc M's "form FORCED, value INHERITED" methodology, and Q.8 closure must complete before GRH itself promotes to FORCED-unconditional.

### 6.3 Why CANDIDATE-FORCED rather than FORCED

Q.7's CANDIDATE-FORCED verdict carries forward the conditional-forcing aspects of all prior substage closures:

- **Specific gauge-group choice empirical** (per Q.2 F4 closure inherited).
- **Coupling constants empirical** (Dimensional Atlas).
- **Q.8 closure pending** for R-5 completion (zero-point aspect).
- **Cascade target F-M8 still conditional.**

Promoting Q.7 to FORCED unconditionally would require either pre-emptive Q.8 closure (inverting dependencies) or forcing specific empirical content from primitives (overstating). The CANDIDATE-FORCED verdict is the strongest defensible substage closure.

### 6.4 Why not weaker verdicts

- **CANDIDATE-admissible** would understate. All four substantive sub-features (W1, W2, W3, W4) close at CANDIDATE-FORCED; the substage-level conditional-forcing characterisation is the strongest defensible.
- **SPECULATIVE-admissible** would imply substantial gaps. None remain at Q.7 level — WFal-5 dispatched; W5 + W6 closed.
- **REFUTED** would require a primitive-level obstruction. None identified across Memos 01–03.

---

## 7. Structural Cascade into Q.8

### 7.1 What Q.7 commits to downstream

The Q.7 substage commits to the following structural content for Q.8 to inherit:

**Lightlike-worldline framework (W1):**
- Affine parameter $\lambda$ for $\tau_g$'s null worldline; affine reparametrisation freedom $\lambda \to a\lambda + b$.
- Tangent vector $u^\mu = dx^\mu/d\lambda$ with $u_\mu u^\mu = 0$.
- Lorentz behaviour of $\lambda$ via Primitive 06 + Theorem 16 inheritance.

**Second-quantised operator framework (W2):**
- Field operator $\hat{A}^a_\mu(x)$ with mode expansion in null momentum modes.
- Creation/annihilation operators $\hat{a}^{a, \sigma}_k$, $\hat{a}^{a, \sigma \dagger}_k$ satisfying canonical commutation per Theorem 6.
- Propagator structural form $\Delta^{ab}_{\mu\nu}(x-y) \propto \delta^{ab} \eta_{\mu\nu} K(x-y)$ with V₁ kernel finite-width regulator.
- Three structurally-equivalent worldline interpretations (expectation-value, support-curve, null-curve).

**Excitation/background distinction (W3):**
- (E) propagating excitation vs (B) background field structural distinction.
- Complementary additive structure on combined states: $\hat{A}^a_\mu = A^{a, \text{cl}}_\mu + \hat{a}^a_\mu$.
- (E)/(B) criteria for state classification.

**Per-worldline accounting (W4):**
- $dN_{\text{commit}}/d\lambda = \rho_V(\lambda)$ in affine-parameter framework.
- Worldline-level conservation (bandwidth, gauge-charge, Lorentz/momentum).
- Worldline-level gauge-quotient consistency.
- Full Phase-1 reconciliation: Primitive 11 invariant under worldline parametrisation choice.

**Pre-vacuum structure (W5):**
- Background-field behaviour, worldline density, operator expectations on non-vacuum states.
- Vacuum state constraints (Q.8 must satisfy): inheritance from W3 (E)/(B) framework; gauge-quotient respect; UV-finite zero-point content; affine-parameter compatibility; vertex-anchored vacuum-level commitment events.

**Honest scoping (carried forward from Q.2 + Q.3):**
- Specific gauge-group choice empirical inheritance.
- Coupling constant values empirical via Dimensional Atlas.
- Charged-rule-type representations empirical / Q.4-onward.

### 7.2 What Q.7 does NOT commit to

- **Specific gauge group** (U(1) vs SU(2) vs SU(3) vs combinations).
- **Coupling constant values** ($q$, $g_s$, $g_w$).
- **Charged-rule-type representations**.
- **Zero-point fluctuations** (R-5 completion, Q.8).
- **Vacuum classification** (uniqueness of vacuum state, etc.) — Q.8.
- **Vacuum polarisation contributions** — Q.8.
- **Full propagator details** (iε prescription for time-ordered propagators) — Q.8.
- **Λ derivation refinement** (extension of Theorem 9's V₁ + Synge content) — Q.8.
- **Vacuum-level commitment events** (virtual vertex pairs in vacuum) — Q.8.
- **Higgs / SSB sector** (Q.4, SPECULATIVE).
- **Generation structure** (Q.6 / empirical).
- **Standard QFT amplitude content** — built from Q.7's framework + Q.8's vacuum content but specific computations downstream.

### 7.3 Dependency map: how Q.7 constrains Q.8

| Q.8 sub-feature (anticipated) | Q.7 inheritance | Q.8 deliverable |
|---|---|---|
| **Vacuum state structure** | (E)/(B) distinction (W3); pre-vacuum scoping (W5) | Full vacuum state $|\Omega\rangle$ with zero-point content; Poincaré-invariance verification |
| **Zero-point fluctuations** | Second-quantised operator framework (W2); propagator structural form | Specific zero-point content; reconciliation with V₁ kernel finite-width regulator |
| **Vacuum polarisation** | Vertex content from Q.3 + propagator from W2 | Vacuum polarisation diagrams; gauge-invariance preserved; UV-FIN per Theorem 7 |
| **Λ from vacuum-vertex content** | V₁ vacuum kernel (Theorems 8 + 9) + W3 background-field aspect | Λ derivation refinement; specific vacuum-vertex contributions |
| **R-5 completion** | All Q.7 closures | Full vacuum-vs-particle status reconciliation; vacuum-state vertex content gauge-quotient-respecting |

Q.7 → Q.8 is a clean one-way dependency (per WFal-5 dispatch in §2.7).

### 7.4 Minimal deliverables Q.8 must produce to close R-5 completion

For **R-5 completion**:
- **Zero-point fluctuation specification.** Residual quantum fluctuations of $\hat{A}^a_\mu$ in the vacuum state $|\Omega\rangle$, compatible with Theorem 7's UV-FIN and Theorem 8's V₁ kernel.
- **Vacuum classification.** Identify the vacuum state(s) admissible at the structural level; verify Poincaré invariance.
- **Vacuum polarisation content.** Virtual vertex pairs (T1 + T2 emission/absorption pairs) contribution to vacuum-state propagator structure.
- **Λ derivation refinement.** Integration of Theorem 9's V₁ + Synge content with vacuum-vertex contributions; specific Λ value structure.
- **Vacuum-level R-3 reconciliation (if needed).** Verify that vacuum-level vertex events (virtual pairs) are consistent with R-3's substantive closure (vertex-anchored commitment).

For **Arc Q synthesis** (post-Q.8):
- Integration of Q.2 + Q.3 + Q.7 + Q.8 results.
- Verification all five refinements affirmatively closed.
- Verification zero new CANDIDATEs introduced.
- Statement of FORCED GRH theorem.

---

## 8. Implications for GRH Closure

### 8.1 Effect on GRH-3 (the load-bearing GRH clause)

GRH-3 advances to **CANDIDATE-FORCED at second-quantised + vertex + worldline + vacuum-field-aspect levels.** The L3-interface gauge-invariance constraint is established at:
- Kinematic level (Q.2 Memo 02)
- Vertex level (Q.3 Memo 02)
- Worldline level (Q.7 Memo 02 W3 + W4)
- Background-field aspect of vacuum (Q.7 Memo 02 W3)

GRH-3 still awaits:
- **Q.8 closure (R-5 completion)** for the zero-point aspect of vacuum.

When Q.8 closes, GRH-3 promotes to FORCED-unconditional, and GRH itself promotes to FORCED-unconditional via Arc Q synthesis.

### 8.2 Updated GRH refinement-closure map

| Refinement | Pre-Q.7 status | Post-Q.7 status | Closure stage |
|---|---|---|---|
| **R-1** | outstanding | **CLOSED ✅** | Q.7 Memo 01 |
| R-2 partial | CLOSED (Q.2) | (unchanged) | Q.2 Memo 02 |
| R-2 completion | CLOSED (Q.3) | (unchanged) | Q.3 Memo 02 |
| R-2 FULL | FULLY CLOSED | (unchanged) | Q.2 + Q.3 |
| R-3 Q.3-side | CLOSED (Q.3) | (unchanged) | Q.3 Memo 02 |
| **R-3 Q.7-side** | outstanding | **CLOSED ✅** | Q.7 Memo 02 |
| **R-3 SUBSTANTIVE** | partial | **SUBSTANTIVELY CLOSED ✅✅** | Q.3 + Q.7 |
| R-4 | CLOSED (Q.2) | (unchanged) | Q.2 Memo 01 |
| **R-5 partial** | outstanding | **CLOSED ✅** | Q.7 Memo 02 |
| **R-5 completion** | outstanding | outstanding | Q.8 |

**Cumulative closure: 6/7 items closed; only R-5 completion remaining.** In 5-refinement count: R-1, R-2, R-3 (substantive), R-4 fully closed; R-5 partially closed (R-5 partial done; R-5 completion outstanding).

### 8.3 Remaining structural work before GRH promotes to FORCED at Arc Q synthesis

The path from "Q.7 closed" to "GRH FORCED-unconditional" requires:

1. **Q.8 substage closure** (vacuum + zero-point + R-5 completion). Anticipated 3–4 memos; substantively lighter than Q.7 (no full second-quantisation framework requirement; primarily R-5 completion via zero-point + vacuum classification + vacuum polarisation + Λ refinement work).
2. **Arc Q synthesis** (integration of Q.2, Q.3, Q.7, Q.8 results; verification all five refinements affirmatively closed; verification zero new CANDIDATEs introduced; statement of FORCED GRH theorem). Anticipated 1–2 memos.
3. **Cascade promotion of Arc M's F-M8** (massless slot existence from FORCED-conditional to FORCED-unconditional). Memo back into Arc M.

Total anticipated remaining Q-substage memos: 4–6. Plus Arc M cascade memo. The trajectory is concrete and well-scoped; no structural blocker has been identified across Q.2 + Q.3 + Q.7 substages.

### 8.4 Position relative to the 16-theorem inventory

When GRH promotes to FORCED-unconditional (post-Q.8 + Arc Q synthesis), it becomes Theorem 17 in the structural-foundations inventory:

> **Theorem 17 (GRH — Gauge-Field-as-Rule-Type, anticipated).** The gauge connection $A^a_\mu$ is itself the participation measure of a rule-type $\tau_g$ (bosonic, four-vector, gauge-invariant L3 interface, structurally massless via MR-P), with the gauge group $G$ admissible as any compact Lie group (specific choice empirical inheritance). Local gauge invariance is an interface property of $\tau_g$'s L3 specification. Vertex content: four admissible vertex types (T1–T4); minimal coupling as structural vertex; vertex-level gauge-quotient individuation. Worldline content: lightlike worldlines parametrised by affine parameter; second-quantised operator framework with Theorem 6 canonical commutation + Theorem 7 UV-FIN inheritance. Vacuum content: $\tau_g$ admits both excitation and background-field interpretations; full vacuum-state structure via Q.8 + Theorem 8 V₁ kernel inheritance.

Cascade: Arc M's F-M8 (massless slot existence) promotes to FORCED-unconditional.

---

## 9. Honest Scope Limits

Per the discipline established across Memos 00–03, Q.7 explicitly cannot resolve:

### 9.1 Within-trajectory items (deferred to Q.8)

- **R-5 completion (zero-point aspect).** Q.8 substantive content.
- **Vacuum classification.** Q.8.
- **Vacuum polarisation contributions.** Q.8.
- **Full propagator details** (iε prescription, vacuum expectation values of operator products). Q.8.
- **Λ derivation refinement.** Q.8.
- **Vacuum-level commitment events.** Q.8.

### 9.2 Outside-trajectory items (empirical inheritance or out of GRH scope)

- **Specific gauge group choice.** Empirical inheritance per Q.2 F4.
- **Coupling constant values.** Empirical via Dimensional Atlas.
- **Charged-rule-type representations.** Empirical / Q.4-onward.
- **Higgs sector / SSB.** Q.4; SPECULATIVE.
- **Generation structure.** Q.6 / empirical.
- **Charge quantization pattern.** Possibly Q.2 / Q.3 partial sub-memo or empirical.
- **Standard QFT amplitude content.** Q.7's framework + Q.8's vacuum content underwrite the content; specific computations downstream.
- **Anomalous magnetic moment of the electron.** Standard QED loop-correction content; ED's analog requires Q.7 + Q.8 framework + specific computation.

### 9.3 Sensitivity flags carried forward

- **Phase-observable discipline** (from Q.2 Memo 03). Confirmed; lifts cleanly to vertex level (Q.3) and worldline level (Q.7).
- **Compactness of $G$** (from Q.2 Memo 01 §3.4.2). Derived constraint from unitarity (U2 inheritance); preserved across Q.2 + Q.3 + Q.7.
- **Killing-form non-degeneracy** (from Q.2 Memo 03). Verified for compact semi-simple groups; preserved across Q.3 + Q.7.
- **Vertex-density commitment-rate construction** (Q.3 Memo 01 + Memo 02). Q.3-side admissibility established; Q.7 Memo 02 W4 closure with full Phase-1 reconciliation.
- **Affine-parameter / proper-time structural relationship** (Q.7 Memo 01 W1). Established as structural generalisation; preserved at W4 + W5.
- **(E)/(B) excitation-vs-background structural distinction** (Q.7 Memo 02 W3). Preserved at W5; constrains Q.8's vacuum-state specification.

---

## 10. Recommended Next Memo

**Q.8 Memo 00 — Vacuum + Zero-Point Structure + R-5 Completion**

The natural next deliverable. Q.8 Memo 00 should:

- Restate the Q.8 question: how does the framework specify the vacuum state $|\Omega\rangle$ with full zero-point content, and what does R-5 completion (the zero-point aspect of $\tau_g$'s vacuum-vs-particle status) require?
- Decompose Q.8 into sub-features (likely: vacuum state classification; zero-point fluctuations; vacuum polarisation; Λ derivation refinement; downstream dependency map for Arc Q synthesis).
- Inventory structural inputs (Primitives 02, 04, 06, 07, 10, 11, 13; inherited theorems including Theorems 1–16 with Theorems 7, 8, 9 directly relevant; Q.2 + Q.3 + Q.7 closures as background; Phase-3 V₁ + Synge content as background).
- Set forbidden-input discipline (no SM specifics; no Higgs / generations / coupling constants; no F-M8 cascade target; no specific renormalisation prescriptions as derivation premise).
- Falsifier inventory for what would refute GRH at the vacuum + zero-point level.

Anticipated length: comparable to Q.7 Memo 00 but substantively lighter overall (Q.8's three substantive memos likely cover R-5 completion + vacuum-state work without the full second-quantisation framework requirement Q.7 carried).

The subsequent Q.8 memos would address sub-feature derivations parallel to the Q.2 / Q.3 / Q.7 patterns.

---

## 11. One-Line Summary

> Q.7 substage closes **CANDIDATE-FORCED** at Memo 03: the GRH framework structurally admits $\tau_g$'s lightlike worldline parametrised by affine parameter $\lambda$ with affine reparametrisation freedom (W1: R-1 closure), supports a minimal second-quantised operator framework with field operator $\hat{A}^a_\mu(x)$ + mode expansion in null momentum modes + Theorem 6 canonical commutation + Theorem 7 UV-FIN inheritance + V₁ kernel finite-width regulator (W2: R-1 closure), distinguishes $\tau_g$ as propagating excitation (worldline-supported, zero field expectation, vertex-mediated commitment) from $\tau_g$ as background field (non-worldline-supported, non-zero field expectation, mean-field content) with complementary additive structure on combined states (W3: R-5 partial closure), lifts Q.3 V4's vertex-density commitment rate to per-worldline accounting $dN_{\text{commit}}/d\lambda = \rho_V(\lambda)$ in the affine-parameter framework with worldline-level conservation laws + gauge-quotient consistency + full Phase-1 reconciliation establishing Primitive 11 invariance under worldline parametrisation choice (W4: R-3 Q.7-side closure → R-3 substantively CLOSED across Q.3 + Q.7), scopes the pre-vacuum structure cleanly identifying what Q.7 says vs. what Q.8 must add (W5), issues the downstream dependency map for Q.8 (W6), all eight Q.7 falsifiers (WFal-1 through WFal-8) NOT triggered including WFal-5 (Q.7 ⟷ Q.8 circular dependency dispatched), six of seven GRH refinements now closed (R-1 + R-2 partial + R-2 completion + R-3 Q.3-side + R-3 Q.7-side + R-4 + R-5 partial; in 5-refinement count: R-1, R-2, R-3 substantive, R-4 fully closed; R-5 partial), only R-5 completion (zero-point aspect, Q.8 work) remaining for GRH closure, GRH-3 advancing to CANDIDATE-FORCED at second-quantised + vertex + worldline + vacuum-field-aspect levels, GRH itself awaiting Q.8 + Arc Q synthesis before promotion to FORCED-unconditional and addition as Theorem 17 to the structural-foundations inventory with cascade promotion of Arc M's F-M8 to FORCED-unconditional.

---

## Recommended Next Steps

**(a) Begin Q.8 Memo 00 (vacuum + zero-point structure + R-5 completion).** The natural next deliverable. Following the Q.2 / Q.3 / Q.7 Memo 00 templates, Q.8 Memo 00 should decompose Q.8 into sub-features (vacuum state classification, zero-point fluctuations, vacuum polarisation, Λ derivation refinement, downstream dependency map for Arc Q synthesis), inventory structural inputs, set forbidden-input discipline, and prepare the substage opening. Q.8 is anticipated to be **the final Q-substage** before Arc Q synthesis. Anticipated length: comparable to Q.2 / Q.3 / Q.7 Memo 00. Q.8's substantive memos: 2–3 anticipated (lighter than Q.7's load).

**(b) Bundled memory-record update covering Q.7 closure.** Per the discipline established in U3 / U4 / U5 arcs and the GRH closure roadmap §10. The memory update should capture: R-1 closure (CANDIDATE-FORCED at Q.7 Memo 01), R-3 Q.7-side closure (CANDIDATE-FORCED at Q.7 Memo 02; R-3 substantively closed across Q.3 + Q.7), R-5 partial closure (CANDIDATE-FORCED at Q.7 Memo 02), Q.7 substage verdict (CLOSED CANDIDATE-FORCED), cumulative refinement-closure status (6/7 closed), GRH-3 status update (CANDIDATE-FORCED at second-quantised + vertex + worldline + vacuum-field-aspect levels), anticipated remaining trajectory (Q.8 → Arc Q synthesis → cascade), sensitivity flags carried forward.

**(c) Update the Sixteen-Theorems desktop graphic if appropriate.** Theorem 5's GRH entry can now be updated to reflect 6/7 refinements closed (only R-5 completion remaining; in 5-refinement count, only R-5 zero-point completion remaining). The graphic could either: (i) update to "CANDIDATE-FORCED with 6/7 refinements closed at Q.2 + Q.3 + Q.7; only R-5 completion remaining for Q.8" framing, or (ii) defer until full GRH closure (anticipated Q.8 + Arc Q synthesis, ~3–5 memos out). User preference.

**(d) Defer further substantive memo work until Q.8 Memo 00 is opened.** Per the discipline of one substage at a time. The trajectory is well-scoped and the dependencies are clean. Q.8's substantive load is anticipated to be lighter than Q.7's.

**(e) (Optional) Draft anticipated FORCED-GRH theorem statement now.** With 6/7 refinements closed and only Q.8 + Arc Q synthesis remaining, the anticipated FORCED-GRH theorem statement (per `00_grh_closure_roadmap.md` §5 + Q.7 Memo 03 §8.4 anticipated formulation) can be drafted in skeleton form. This would let Arc Q synthesis (post-Q.8) work efficiently. Optional but useful for trajectory visibility.
