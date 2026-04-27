# Arc Q Synthesis — Memo 00: Scoping

**Arc:** Q (GRH closure trajectory)
**Stage:** Synthesis (post-substage integration)
**Memo:** 00 (synthesis opening / scoping)
**Status on entry:** Q.2 ✅ Q.3 ✅ Q.7 ✅ Q.8 ✅; refinement-closure map 7/7 (R-1, R-2 FULL, R-3 FULL, R-4, R-5 FULL all CLOSED at substage level).
**Status on exit of synthesis:** GRH promoted to FORCED-unconditional (Theorem 17); Arc M F-M8 cascade unblocked.

---

## 1. The synthesis question, restated

**What synthesis must accomplish.** Each Q-substage closed CANDIDATE-FORCED. CANDIDATE-FORCED at the substage level means: the substage's structural payload is forced *given* that all upstream substages and primitives are consistent and that no global cross-substage falsifier triggers. **Arc Q synthesis is the stage at which those global conditions are dispatched.** It must:

1. Integrate the four Q-substage payloads (Q.2 + Q.3 + Q.7 + Q.8) into a single globally consistent structural object — the GRH commitment ledger across all three commitment branches (vertex / worldline / vacuum) and across the gauge-group + non-Abelian + quotient + worldline + vacuum-classification axes.
2. Dispatch the synthesis-level falsifier inventory (cross-substage consistency, global quotient consistency, global commitment-rule consistency, primitive-level global compatibility, circularity check on Arc M).
3. Promote GRH from CANDIDATE-FORCED-across-substages to **FORCED-unconditional** by issuing **Theorem 17** in canonical form.
4. Map the cascade into Arc M (F-M8 promotion).

**Position in trajectory.** Synthesis sits *after* Q.8 (terminal Q-substage) and *before* Arc M cascade (which depends on Theorem 17 being in inventory). Synthesis is the *unique* place where global cross-substage audits can be discharged without circularity.

**What "FORCED-unconditional" means.** A theorem is FORCED-unconditional in ED's discipline when:
- Its statement is derivable from primitives + prior FORCED theorems alone (no new CANDIDATE).
- All upstream verdicts it depends on are CLOSED with no falsifier triggered.
- All cross-substage and acyclicity audits PASS at the synthesis level.
- The theorem stands without conditional clauses ("if X holds, then ...") at the structural level (numerical-magnitude conditioning via INHERITED parameters is permitted under "form FORCED, value INHERITED" discipline).

Theorem 17 (GRH FORCED-unconditional) will be the **17th FORCED structural theorem** in ED inventory.

---

## 2. Structural payload from Q.2, Q.3, Q.7, Q.8

### 2.1 Q.2 — Gauge-group admissibility + quotient structure

| Aspect | Status | Content |
|---|---|---|
| **FORCED** | Form-level | (a) Non-Abelian-capable gauge-group structure for τ_g (R-4); (b) gauge-quotient identification at group level (R-2 partial); (c) Killing-form / Jacobi closure for the gauge Lie algebra. |
| **INHERITED** | Value-layer | Specific gauge group (SU(N), product groups, etc.) — empirical / SM-specific; not committed by Q.2. |
| **CONDITIONAL** | None at substage level | Q.2 closure was unconditional within Q-internal scope. |
| **NOT IMPORTED** | — | SM gauge group (SU(3)×SU(2)×U(1)); specific representation content; Higgs sector. |

### 2.2 Q.3 — Vertex taxonomy + minimal coupling + vertex-anchored commitment

| Aspect | Status | Content |
|---|---|---|
| **FORCED** | Form-level | (a) Vertex taxonomy (V1+V2 + V4 partial in Memo 01); (b) minimal coupling structural vertex (V1); (c) gauge-quotient extension to vertex-quotient (V3+V4, R-2 completion); (d) vertex-anchored commitment (R-3 Q.3-side). |
| **INHERITED** | Value-layer | Coupling magnitudes; specific vertex strengths. |
| **CONDITIONAL** | None at substage level | All Q.3 falsifiers NOT TRIGGERED. |
| **NOT IMPORTED** | — | Yukawa couplings, Higgs mechanism vertices, anomaly cancellation specifics. |

### 2.3 Q.7 — Worldline + second-quantised structure

| Aspect | Status | Content |
|---|---|---|
| **FORCED** | Form-level | (a) Lightlike worldline for τ_g excitations (R-1); (b) Q.7-side worldline-anchored commitment ledger (R-3 Q.7-side); (c) second-quantised excitation lifting / Fock-style count (R-5 partial); (d) pre-vacuum scoping (W5). |
| **INHERITED** | Value-layer | Numerical excitation rates; specific worldline parametrisations. |
| **CONDITIONAL** | None at substage level | All Q.7 falsifiers (incl. WFal-5 circularity) NOT TRIGGERED. |
| **NOT IMPORTED** | — | Specific propagator forms; massless-vs-massive specifics for τ_g (Q.7 commits to lightlike worldline as the structural form; magnitude separately inherited). |

### 2.4 Q.8 — Vacuum + zero-point structure

| Aspect | Status | Content |
|---|---|---|
| **FORCED** | Form-level | (a) Gauge-invariant, UV-finite, V1-form, stationary vacuum kernel for τ_g (VQ1 — R-5 completion form-side); (b) three-class vacuum taxonomy (VQ2); (c) strict non-commitment at vacuum + V1 background functional B[v] additively contributing to vertex-anchored rates (VQ3 — R-3 Q.8-side); (d) full vacuum-sector gauge-quotient certification (VQ4). |
| **INHERITED** | Value-layer | V1 kernel parameters, B[v] amplitude, vacuum energy density magnitude, Λ value. |
| **CONDITIONAL** | None at substage level | All seven Q.8 falsifiers (incl. VQFal-4 circularity) NOT TRIGGERED. |
| **NOT IMPORTED** | — | SM vacuum content (Higgs VEV, QCD condensates, instantons, θ-vacua); QFT vacuum prescriptions; thermal vacua; cosmological constant phenomenology. |

---

## 3. Synthesis falsifier inventory

### 3.1 SFal-1 — Cross-substage inconsistency

**Condition.** Any pair of Q-substage payloads (Q.2 ↔ Q.3, Q.2 ↔ Q.7, Q.2 ↔ Q.8, Q.3 ↔ Q.7, Q.3 ↔ Q.8, Q.7 ↔ Q.8) makes incompatible structural commitments — e.g., Q.2 forces a gauge-group property that Q.7's worldline structure cannot accommodate, or Q.8's vacuum kernel form contradicts Q.3's vertex commitment rule.

**Tested in:** Synthesis Memo 01 (global integration).

### 3.2 SFal-2 — Quotient inconsistency under global integration

**Condition.** R-2 + R-2 completion + VQ4 are individually consistent at substage level, but their *global integration* breaks gauge-quotient identification — e.g., a gauge-equivalent configuration that is identified at vertex level becomes distinguishable at vacuum level once Q.8 + Q.3 ledgers are combined.

**Tested in:** Synthesis Memo 01 (global quotient audit).

### 3.3 SFal-3 — Commitment-rule inconsistency across vertex/worldline/vacuum

**Condition.** R-3 Q.3-side + R-3 Q.7-side + R-3 Q.8-side are individually consistent, but the global commitment ledger combining vertex-anchored events + worldline ledger + vacuum strict-non-commitment + B[v] background is internally inconsistent — e.g., double-counting of events, missing branch, or incompatible additivity rules between the V1-background contribution and the vertex-anchored rate.

**Tested in:** Synthesis Memo 01 (commitment-ledger integration).

### 3.4 SFal-4 — Primitive-level incompatibility under global integration

**Condition.** No individual Q-substage triggered any primitive-level forbid, but the global integration uses some combination of primitives (e.g., P-04 + P-10 + P-13 simultaneously across all three commitment branches) in a way that violates a primitive constraint — e.g., bandwidth additivity fails when summed across vertex + worldline + vacuum branches.

**Tested in:** Synthesis Memo 01 (primitive-load global audit).

### 3.5 SFal-5 — Circular dependence on Arc M

**Condition.** Theorem 17 derivation (Memo 02) implicitly uses Arc M results (F-M8 in particular) as input — i.e., the FORCED-unconditional GRH theorem is being justified by appealing to a downstream Arc M item, breaking acyclicity.

**Tested in:** Synthesis Memo 02 (theorem statement + verdict).

### 3.6 (Reserved) SFal-6 — Acyclicity break in dependency graph

**Condition.** The synthesis-level dependency graph has any cycle (any FORCED theorem 1–17 used to justify itself transitively).

**Tested in:** Synthesis Memo 01 (acyclicity audit).

---

## 4. Allowed inputs

### 4.1 ED primitives

| Primitive | Synthesis-level commitment | Does NOT commit to |
|---|---|---|
| P-02 (rule-types) | τ_g exists as a structural carrier with vacuum + excitation sectors. | Specific group structure or coupling. |
| P-04 (bandwidth additivity) | Additive composition across vertex + worldline + vacuum branches in commitment-rate ledger. | Specific bandwidth magnitudes. |
| P-06 (commitment events) | Commitment-event ontology applies globally; specialised per branch as Q.3/Q.7/Q.8 specify. | Specific commitment rates. |
| P-07 (vertex anchoring) | Commitment requires anchor; vacuum strict non-commitment forced by P-06 + P-07. | Specific vertex strengths. |
| P-10 (gauge-quotient identification) | Global quotient identification holds; vacuum + vertex + worldline all gauge-quotient-consistent. | Specific gauge-fixing prescription. |
| P-11 (UV-FIN) | Global structural envelope UV-finite; Theorem 7 inherited. | Specific kernel parameter values. |
| P-13 (continuous-time closure) | Stationarity in minimal branch; time-translation generator commutes with gauge action globally. | Specific time-evolution operator. |

### 4.2 Prior FORCED theorems 1–16

All available as upstream structural commitments. **Most directly load-bearing for Theorem 17:**
- Theorem 5 (GRH unconditional, form-level Q.1 + Q.8 baseline) — synthesis upgrades this from form-level to FORCED-unconditional.
- Theorem 6 (canonical (anti-)commutation, Q.7) — load-bearing for excitation-side commitment ledger.
- Theorem 7 (UV-FIN, Q.8) — load-bearing for vacuum kernel.
- Theorem 8 (V1 finite-width vacuum kernel, N.5) — load-bearing for VQ1 vacuum form.
- Theorem 16 (time-translation Schrödinger evolution, U3) — load-bearing for stationarity + time-translation closure across branches.

Theorems 1, 2, 3, 4, 9, 10, 11, 12, 13, 14, 15 available; not directly load-bearing for synthesis but available for global consistency checks.

### 4.3 All Q-substage verdicts

Q.1 (prior Theorem 5 baseline), Q.2, Q.3, Q.7, Q.8 — all CLOSED CANDIDATE-FORCED. Synthesis may use any of their committed payloads verbatim; synthesis may NOT reopen any.

### 4.4 GRH-1 through GRH-4

- **GRH-1** (participation measure of τ_g) — committed.
- **GRH-2** (vertex anchoring) — committed.
- **GRH-3** (anticipated FORCED-unconditional GRH) — *the synthesis output*; not an input.
- **GRH-4** (gauge-quotient discipline) — committed.

### 4.5 Refinement-closure map

R-1, R-2 FULL, R-3 FULL, R-4, R-5 FULL — all CLOSED. Available verbatim.

---

## 5. Forbidden inputs

| Forbidden input | Justification |
|---|---|
| **Arc M cascade results (F-M8)** | F-M8 is downstream of Theorem 17. Using it would cycle: Arc M ← Theorem 17 ← synthesis ← Arc M. |
| **Standard Model specifics** (gauge group SU(3)×SU(2)×U(1), Higgs sector, Yukawa couplings, generations, anomaly content) | Empirical/phenomenological; "form FORCED, value INHERITED" discipline keeps SM content out of the form layer. |
| **Empirical couplings** (α, α_s, sin²θ_W, etc.) | Value-layer; would smuggle empirical content into a form-level theorem. |
| **Renormalised vacuum energy** | Constructed within a chosen quantisation/regularisation scheme; would import upstream CANDIDATE not derivable from P-02..P-13. |
| **QFT vacuum prescriptions** (path-integral measure, Faddeev-Popov ghosts, BRST cohomology, dimensional regularisation, MS-bar scheme) | Same as above; quantisation-scheme-dependent constructs. |
| **Thermal / KMS vacua, observer-dependent vacua** | Frame-dependent vacuum content; would require additional CANDIDATE about preferred frames. |
| **Cosmological-constant phenomenology** (Λ value, dark-energy equation of state) | Value-layer; lives in Arc N + Phase-3 GR. |

---

## 6. Expected deliverables

For Arc Q synthesis to close FORCED-unconditional, synthesis must produce:

1. **A globally consistent integration of Q.2 + Q.3 + Q.7 + Q.8** — the unified GRH structural object across gauge-group / vertex / worldline / vacuum axes, with the unified commitment ledger spanning all three commitment branches.
2. **A global falsifier audit** — SFal-1 through SFal-6 dispatched without trigger.
3. **A structural closure statement for GRH** — explicit confirmation that GRH-3 holds at synthesis level (FORCED-unconditional).
4. **Theorem 17 (GRH) in canonical form** — a single, self-contained theorem statement that is derivable from primitives + Theorems 1–16 + Q-substage verdicts alone, with no conditional clauses at the structural level.
5. **A dependency map into Arc M** — explicit identification of how Theorem 17 unblocks F-M8 promotion (and any other Arc M items dependent on GRH closure).
6. **A verdict** (Memo 02) — issuing FORCED-unconditional status and updating the global FORCED-theorem inventory from 16 to 17.

---

## 7. Synthesis structure (memo sequence)

| Memo | Scope | Key dispatches |
|---|---|---|
| **Memo 00** (this memo) | Scoping: deliverables, allowed/forbidden inputs, falsifier inventory, structural payload survey. | — |
| **Memo 01** | Global integration of Q.2 + Q.3 + Q.7 + Q.8 + Theorem-baseline; full falsifier audit. | SFal-1, SFal-2, SFal-3, SFal-4, SFal-6. Acyclicity audit. Commitment-ledger global integration. |
| **Memo 02** | Theorem 17 derivation + canonical statement; final verdict; Arc M cascade map. | SFal-5. FORCED-unconditional verdict. Theorem 17 in canonical form. |

**Anticipated total: 3 substantive memos** (Memo 00 scoping + Memo 01 integration/audit + Memo 02 theorem/verdict). Matches the cadence of prior arc-synthesis stages (Arc R, Arc M, Arc N).

---

## 8. Dependency graph

```
   Phase-1 + Theorems 6–9   (upstream baseline)
              │
              ▼
   Q.1 ──> Q.2 ──> Q.3 ──> Q.7 ──> Q.8
                    │       │       │
                    └───────┼───────┘
                            ▼
                  Arc Q synthesis (this stage)
                            │
                            ▼
                  Theorem 17 (GRH FORCED-unconditional)
                            │
                            ├──> Arc M cascade (F-M8 promotion)
                            │
                            └──> Inventory update: 16 → 17 FORCED theorems
```

**Acyclicity guarantee.** Each substage feeds synthesis; synthesis feeds Theorem 17; Theorem 17 feeds Arc M. No back-edges. SFal-6 (Memo 01) and SFal-5 (Memo 02) jointly certify this.

---

## 9. Honest scope limits

Arc Q synthesis cannot resolve:
- **Empirical vacuum energy density** (value-layer; INHERITED).
- **SM-specific vacuum content** (Higgs VEV, QCD condensates, instanton sectors, θ-vacua).
- **Cosmological constant Λ value** (Arc N + Phase-3 GR; only Λ-as-V1-integral form is structural).
- **F-M8 mass-form magnitude** (Arc M cascade).
- **Specific gauge group of nature** (SM input; Theorem 17 commits to non-Abelian-capable group structure, not SU(3)×SU(2)×U(1)).
- **Higgs mechanism structure** (Arc M and beyond).
- **Renormalisation-group running of couplings** (Arc M / Phase-2).

Must be deferred to Arc M cascade:
- **F-M8 promotion** and any further mass-form refinements that depend on Theorem 17.
- **τ_g-mediated mass-form contributions** from the V1 vacuum kernel.

---

## 10. Recommended next memo

**Arc Q synthesis Memo 01 — Global integration + falsifier audit + acyclicity audit.**

Memo 01 should:
- Walk the four Q-substage payloads (§2.1–§2.4) in pairs and triples to dispatch SFal-1.
- Audit the global gauge-quotient ledger (Q.2 + Q.3 + Q.8) to dispatch SFal-2.
- Integrate the three commitment branches (vertex / worldline / vacuum) into a single ledger with explicit additivity rules; dispatch SFal-3.
- Run the global primitive-load audit across all four Q-substages simultaneously; dispatch SFal-4.
- Walk the dependency graph and dispatch SFal-6 (acyclicity).
- Conclude with a "ready-for-Theorem-17" certification that Memo 02 can use directly.

Anticipated content density: largest synthesis memo (matches Arc R + Arc N synthesis Memo 01 lengths).

---

## 11. One-line summary

**Arc Q synthesis integrates the four CANDIDATE-FORCED Q-substage payloads (Q.2 + Q.3 + Q.7 + Q.8) under a single global cross-substage + quotient + commitment-ledger + primitive + acyclicity audit, and — if all five synthesis-level falsifiers (SFal-1..5; plus reserved SFal-6) NOT TRIGGER — promotes GRH from CANDIDATE-FORCED to FORCED-unconditional via Theorem 17, the 17th FORCED structural theorem in ED inventory.**

---

## Recommended Next Steps

1. **Begin Arc Q synthesis Memo 01** — Global integration + falsifier audit (SFal-1, SFal-2, SFal-3, SFal-4, SFal-6); produce "ready-for-Theorem-17" certification.
2. **Begin Arc Q synthesis Memo 02** — Derive Theorem 17 in canonical form; dispatch SFal-5; issue FORCED-unconditional verdict; map Arc M cascade.
3. **Pre-stage Arc M cascade memo (F-M8 promotion)** — Will fire as soon as Theorem 17 lands.
4. **Bundled memory-record update** — Defer until Memo 02 closes; then update `project_qm_emergence_arc.md` + main `MEMORY.md` with Theorem 17 + 7/7 closure + Arc Q synthesis verdict.
5. **Update Sixteen-Theorems SVG catalogue** — Promote anticipated Theorem 17 (FORCED-unconditional GRH) to confirmed slot once Memo 02 closes.
