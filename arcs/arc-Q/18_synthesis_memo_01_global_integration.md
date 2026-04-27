# Arc Q Synthesis — Memo 01: Global Integration and Falsifier Audit

**Arc:** Q (GRH closure trajectory)
**Stage:** Synthesis
**Memo:** 01 (global integration + falsifier audit)
**Status on entry:** Q.2 ✅ Q.3 ✅ Q.7 ✅ Q.8 ✅; refinement-closure map 7/7 CLOSED; synthesis falsifier inventory defined (Memo 00).
**Status on exit:** Global integration complete; SFal-1, SFal-2, SFal-3, SFal-4, SFal-6 NOT TRIGGERED; ready-for-Theorem-17 certification issued.

---

## 1. The synthesis task, restated

**Global integration** is the operation of taking the four CANDIDATE-FORCED Q-substage payloads (Q.2, Q.3, Q.7, Q.8), each closed within its own scope, and constructing a single global structural object — the unified GRH commitment ledger across all four structural axes (gauge-group + non-Abelian / vertex + minimal coupling / worldline + second-quantisation / vacuum + zero-point) and across all three commitment branches (vertex / worldline / vacuum).

**Why synthesis is required even after 7/7 refinements are closed.** Each substage closes CANDIDATE-FORCED — the substage payload is forced *given* upstream consistency *and* given that no global cross-substage falsifier triggers. The substage does not (and cannot) dispatch the global cross-substage audit, because the dispatch requires simultaneous access to all four payloads. Synthesis is the *unique* dispatch site. Without it, GRH would remain CANDIDATE-FORCED-across-substages, which is structurally distinct from FORCED-unconditional.

**Memo 01 deliverables (before Memo 02 can state Theorem 17):**
- Construction of the unified global structural object.
- Construction of the unified commitment ledger.
- Construction of the unified gauge-quotient ledger.
- Global primitive-load audit.
- Dispatch of SFal-1 through SFal-4 + SFal-6.
- "Ready-for-Theorem-17" certification.

SFal-5 (circular dependence on Arc M) is reserved for Memo 02 because it concerns the Theorem 17 derivation itself.

---

## 2. Global integration of Q.2 + Q.3 + Q.7 + Q.8

### 2.1 Q.2 payload (recap)

| Axis | FORCED | INHERITED | CONDITIONAL | NOT IMPORTED |
|---|---|---|---|---|
| Gauge group | Non-Abelian-capable group structure for τ_g; Killing-form / Jacobi closure; gauge-quotient identification at group level (R-2 partial); R-4. | Specific group (SU(N), product groups). | None at substage. | SM gauge group (SU(3)×SU(2)×U(1)); representation content. |

### 2.2 Q.3 payload (recap)

| Axis | FORCED | INHERITED | CONDITIONAL | NOT IMPORTED |
|---|---|---|---|---|
| Vertex / coupling | Vertex taxonomy; minimal coupling structural vertex; vertex-quotient extension (R-2 completion); vertex-anchored commitment (R-3 Q.3-side). | Coupling magnitudes; specific vertex strengths. | None at substage. | Yukawa, Higgs vertices, anomaly cancellation. |

### 2.3 Q.7 payload (recap)

| Axis | FORCED | INHERITED | CONDITIONAL | NOT IMPORTED |
|---|---|---|---|---|
| Worldline / second-quantisation | Lightlike worldline (R-1); worldline-anchored commitment (R-3 Q.7-side); excitation lifting / Fock-style count (R-5 partial). | Numerical excitation rates; propagator parametrisation. | None at substage. | Massless-vs-massive specifics; specific propagator forms. |

### 2.4 Q.8 payload (recap)

| Axis | FORCED | INHERITED | CONDITIONAL | NOT IMPORTED |
|---|---|---|---|---|
| Vacuum / zero-point | Gauge-invariant, UV-finite, V1-form, stationary vacuum kernel (VQ1 / R-5 completion form); three-class vacuum taxonomy (VQ2); strict non-commitment + B[v] background (VQ3 / R-3 Q.8-side); full vacuum gauge-quotient certification (VQ4). | V1 kernel parameters; B[v] amplitude; vacuum energy density; Λ value. | None at substage. | SM vacuum content; QFT vacuum prescriptions; thermal vacua; Λ phenomenology. |

### 2.5 Unified global structural object

```
                          ┌──────────── τ_g ────────────┐
                          │                              │
        ┌─────────────────┼─────────────┐                │
        │                 │             │                │
   ┌────▼────┐       ┌────▼────┐   ┌────▼─────┐    ┌────▼────────┐
   │ GAUGE   │       │ VERTEX  │   │ WORLDLINE│    │  VACUUM     │
   │ GROUP   │       │ + COUPL │   │ + EXCIT  │    │  + KERNEL   │
   │ (Q.2)   │       │ (Q.3)   │   │ (Q.7)    │    │  (Q.8)      │
   └────┬────┘       └────┬────┘   └────┬─────┘    └────┬────────┘
        │                 │             │               │
        └─ R-2/R-4 ───────┼─ R-2/R-3 ───┼── R-1/R-3/R-5 ┴── R-3/R-5/quotient
                          │             │               │
                          ▼             ▼               ▼
                     ┌──────────────────────────────────────┐
                     │   UNIFIED COMMITMENT LEDGER          │
                     │   (vertex + worldline + vacuum)      │
                     └──────────────────┬───────────────────┘
                                        │
                                        ▼
                     ┌──────────────────────────────────────┐
                     │   UNIFIED GAUGE-QUOTIENT LEDGER      │
                     │   (group + vertex + worldline + vac) │
                     └──────────────────────────────────────┘
```

**Unified structural axes (4) × commitment branches (3) × quotient channels (4) = 48 cross-cells.** Each cell is either DIRECTLY-DERIVED (the payload of a single substage), CROSS-SUBSTAGE (consistency between two payloads), or GLOBAL (synthesis-level). §3 + §4 + §5 dispatch the cross-substage and global cells.

---

## 3. Global commitment-ledger integration

### 3.1 The three branches

| Branch | Source | Content |
|---|---|---|
| **Vertex** | Q.3 (R-3 Q.3-side) | Commitment events anchored at vertex v with rate Γ_excitation[v; τ_g]. |
| **Worldline** | Q.7 (R-3 Q.7-side) | Vertex-anchored commitments lifted onto the lightlike worldline of an excitation; ledger {v_i} along the worldline. |
| **Vacuum** | Q.8 (R-3 Q.8-side) | Strict non-commitment at vacuum + V1-form background functional B[v; τ_g] additively contributing to vertex-anchored rates. |

### 3.2 Global integration rule

The global commitment rate at any vertex anchor v in any state s is:

> **Γ_global[v; s] = Γ_excitation[v; τ_g, s] + B[v; τ_g]**

where:
- Γ_excitation = Q.3 vertex-anchored rate evaluated in state s along the Q.7 worldline structure (zero in pure vacuum states by P-07, since no anchor is present in a pure vacuum).
- B[v; τ_g] = VQ3 background functional from VQ1 V1 kernel, *evaluated at v* (which only exists when there is at least one excitation to anchor v in the first place).

**Additivity** is forced by P-04 (bandwidth additivity over independent sectors). **No double-counting** because:
- In pure vacuum states: no anchor v exists → ledger empty (consistent with VQ3 strict non-commitment).
- In excitation states: a single anchor v receives both an excitation contribution and a background contribution, summed once.
- Worldline ledger {v_i} is the ordered list of anchors along the Q.7 lightlike worldline; each v_i contributes once to Γ_global[v_i; s] with both terms.

### 3.3 Acyclicity check on commitment ledger

| Direction | Source | Sink | Cyclic? |
|---|---|---|---|
| Vertex → Worldline | Q.3 | Q.7 (lifts vertex ledger) | No. |
| Worldline → Vacuum | Q.7 | Q.8 (degenerate-zero limit) | No. |
| Vacuum → Vertex | Q.8 (B[v]) | Q.3 (additive contribution) | **Forward-only:** B[v] enters Γ_global at vertex anchors; vertex anchors do not feed back into B[v]. |

The vacuum-to-vertex direction is *additive contribution*, not a back-edge in the dependency graph. Q.3's derivation of vertex-anchored commitment did not require B[v]; Q.8's derivation of B[v] did not require Q.3's vertex anchors as inputs. The integration in §3.2 is a *global rule*, not a re-derivation. **Acyclicity preserved.**

### 3.4 Remaining sensitivities

- **Sensitivity-C1.** B[v] amplitude is INHERITED from V1 kernel parameter; its numerical contribution to Γ_global is therefore value-layer. This is consistent with "form FORCED, value INHERITED" discipline and is not a sensitivity at the form level.
- **Sensitivity-C2.** The additivity rule rests on P-04 (bandwidth additivity over independent sectors). If vacuum-sector and excitation-sector were not independent in the bandwidth sense, the rule would need modification. Independence holds here because the V1 kernel is *stationary background* (Constraint 6 of Memo 01 §2) while excitation contributions are *worldline-localised*. **Sensitivity flagged but not triggered.**

---

## 4. Global gauge-quotient integration

### 4.1 The four channels

| Channel | Source | Content |
|---|---|---|
| **Group-level quotient** | Q.2 (R-2 partial + R-4) | Gauge-equivalent group elements identified; non-Abelian Killing-form / Jacobi closure. |
| **Vertex quotient** | Q.3 (R-2 completion) | Gauge-equivalent vertex configurations identified; minimal-coupling structural vertex is gauge-invariant. |
| **Worldline quotient** | Q.7 (R-1 + R-3 Q.7-side) | Lightlike worldline is gauge-invariant geometric object; ledger {v_i} respects vertex-quotient. |
| **Vacuum quotient** | Q.8 (VQ4) | V1 kernel + classification + commitment all gauge-invariant; non-Abelian Killing-form/Jacobi inheritance preserved. |

### 4.2 Global integration rule

A configuration of τ_g is identified with another iff they differ by a gauge transformation acting consistently across all four channels. The unified gauge-quotient ledger is the *intersection* of the four channels' equivalence classes — that is, the equivalence relation that is finer than any single-channel relation but coarser than the trivial (no-identification) relation.

**Consistency claim.** All four channels' equivalence relations are *pulled back* from the single underlying group action on τ_g (the gauge group from Q.2). Therefore they are mutually consistent by construction: a gauge transformation g acts on all four channels via the same g; the equivalence classes are the orbits of g across all channels.

### 4.3 Cross-channel consistency check

| Pair | Check | Result |
|---|---|---|
| Group ↔ Vertex | Vertex-quotient must be the pullback of group-quotient through the vertex coupling. | PASSES (R-2 completion in Q.3 explicitly verifies this). |
| Group ↔ Worldline | Lightlike worldline (geometric object) is gauge-invariant under group action. | PASSES (Q.7 worldline derivation independent of gauge fixing). |
| Group ↔ Vacuum | Vacuum classification + V1 kernel + B[v] all gauge-invariant under group action. | PASSES (Q.8 VQ4 four-channel audit). |
| Vertex ↔ Worldline | Worldline ledger {v_i} respects vertex-quotient at each v_i. | PASSES (Q.7 R-3 Q.7-side derivation explicitly inherits vertex-quotient). |
| Vertex ↔ Vacuum | B[v] is gauge-invariant at any vertex anchor v. | PASSES (Q.8 VQ4 Channel 4 cross-substage audit). |
| Worldline ↔ Vacuum | Worldline ledger inherits B[v] additively at each anchor; gauge-invariance preserved. | PASSES (combined Q.7 + Q.8 derivations). |

All six pairs PASS. **No cross-channel quotient inconsistency.**

### 4.4 Non-Abelian global consistency

R-4 closure (Q.2) supplies the Killing-form / Jacobi structure. This structure must propagate to vertex (Q.3), worldline (Q.7), and vacuum (Q.8) without contradiction.

- Vertex: minimal-coupling vertex is constructed using gauge-Lie-algebra structure constants → Jacobi-respecting. PASSES.
- Worldline: ledger entries respect non-Abelian gauge action on excitations. PASSES.
- Vacuum: V1 kernel inherits gauge-invariance under the non-Abelian group; Killing form supplies the natural inner product on gauge-Lie-algebra fibre at vacuum. PASSES.

### 4.5 Remaining sensitivities

- **Sensitivity-Q1.** The unified ledger assumes the *same* gauge group acts on all four channels. This is true at the structural level (a single τ_g rule-type with a single gauge-Lie-algebra fibre). If the gauge group were enlarged at a particular channel (e.g., spontaneous symmetry breaking introducing additional structure), the unified ledger would need a refined treatment. SSB is forbidden input here (SM-specific). **Sensitivity flagged, not triggered.**

---

## 5. Primitive-level global audit

For each primitive, we test compatibility with the unified global structural object (§2.5) and the unified commitment + quotient ledgers (§3 + §4).

| Primitive | Global compatibility | Classification | Implication for SFal-4 |
|---|---|---|---|
| **P-02** (rule-types) | τ_g is a structural carrier across all four substage axes; unified object inherits non-vacuity. | **supports** | NOT TRIGGERED. |
| **P-04** (bandwidth additivity) | Used in §3.2 for global commitment-rate additivity (vertex + vacuum-background). Bandwidth additivity must hold simultaneously across all three branches (vertex / worldline / vacuum). Independence holds (Sensitivity-C2 §3.4). | **constrains (load-bearing)** | NOT TRIGGERED. |
| **P-06** (commitment events) | Commitment-event ontology applies globally; specialised per branch consistently. No double-counting (§3.2). | **constrains** | NOT TRIGGERED. |
| **P-07** (vertex anchoring) | Forces strict non-commitment at vacuum globally; consistent with Γ_global = 0 in pure-vacuum states. | **constrains (decisively)** | NOT TRIGGERED. |
| **P-10** (gauge-quotient identification) | Used in §4 for unified four-channel quotient ledger. All six cross-channel checks PASS. | **constrains (load-bearing)** | NOT TRIGGERED. |
| **P-11** (UV-FIN) | Global structural envelope UV-finite across all branches; vacuum kernel + vertex rate + worldline ledger all bounded. | **constrains** | NOT TRIGGERED. |
| **P-13** (continuous-time closure) | Time-translation generator commutes with gauge action globally (§4.4 + Q.8 VQ4); stationarity in minimal branch preserved. | **constrains** | NOT TRIGGERED. |

**Summary.** Seven primitives load-bearing across the global integration. All seven consistent with global structure. No primitive forbids; no new CANDIDATE introduced. **SFal-4 NOT TRIGGERED.**

---

## 6. Synthesis falsifier analysis

### 6.1 SFal-1 — Cross-substage inconsistency

Pairs (Q.2 ↔ Q.3, Q.2 ↔ Q.7, Q.2 ↔ Q.8, Q.3 ↔ Q.7, Q.3 ↔ Q.8, Q.7 ↔ Q.8) and triples (Q.2+Q.3+Q.7, Q.2+Q.3+Q.8, Q.2+Q.7+Q.8, Q.3+Q.7+Q.8) tested via §2.5 unified object and §3 + §4 cross-checks.

| Pair / triple | Status |
|---|---|
| Q.2 ↔ Q.3 | PASSES (R-2 partial extends to R-2 completion). |
| Q.2 ↔ Q.7 | PASSES (Q.2 group structure compatible with R-1 lightlike worldline). |
| Q.2 ↔ Q.8 | PASSES (Q.2 group structure preserved at vacuum; VQ4 confirms). |
| Q.3 ↔ Q.7 | PASSES (vertex ledger lifts to worldline ledger; R-3 Q.7-side explicit). |
| Q.3 ↔ Q.8 | PASSES (B[v] gauge-invariant; additivity at vertex anchor; §3.2). |
| Q.7 ↔ Q.8 | PASSES (worldline degenerates to vacuum cleanly; R-5 partial + R-5 completion glue). |
| Q.2+Q.3+Q.7 | PASSES (gauge-group + vertex + worldline form Q.7-side closed envelope). |
| Q.2+Q.3+Q.8 | PASSES (gauge-group + vertex + vacuum form vacuum-sector envelope). |
| Q.2+Q.7+Q.8 | PASSES (gauge-group + worldline + vacuum form excitation-vacuum interface). |
| Q.3+Q.7+Q.8 | PASSES (commitment ledger global integration §3.2). |

**SFal-1 NOT TRIGGERED.**

### 6.2 SFal-2 — Global quotient inconsistency

Tested via §4 four-channel + six cross-channel pair checks.

All six pairs PASS; non-Abelian global consistency PASSES (§4.4).

**SFal-2 NOT TRIGGERED.**

### 6.3 SFal-3 — Commitment-rule inconsistency

Tested via §3 global integration rule (Γ_global = Γ_excitation + B), no double-counting (§3.2), acyclicity check (§3.3).

**SFal-3 NOT TRIGGERED.**

### 6.4 SFal-4 — Primitive-level global incompatibility

Tested via §5 global primitive audit. All seven primitives consistent globally.

**SFal-4 NOT TRIGGERED.**

### 6.5 SFal-6 — Acyclicity break in dependency graph

Dependency graph from Memo 00 §8:

```
Phase-1 + Theorems 6–9 → Q.1 → Q.2 → Q.3 → Q.7 → Q.8 → Synthesis → Theorem 17 → Arc M
```

Back-edges checked:
- Synthesis ← Arc M? NO (Arc M is downstream).
- Q.8 ← Synthesis? NO (Q.8 closure was independent; VQFal-4 already dispatched in Q.8 Memo 03).
- Q.7 ← Q.8? NO (Q.7 closure independent; WFal-5 already dispatched in Q.7 Memo 03).
- Any Q-substage ← any later Q-substage? NO (each substage closure was independent).
- Theorems 1–16 ← Theorem 17? NO (Theorem 17 derivation will use Theorems 1–16; reverse not invoked).
- Vacuum-to-vertex commitment integration (§3.3): forward additive contribution, not back-edge.

**No back-edge found. SFal-6 NOT TRIGGERED.**

### 6.6 Cumulative falsifier-status table

| Falsifier | Tested in | Status |
|---|---|---|
| SFal-1 (cross-substage inconsistency) | This memo §6.1 | NOT TRIGGERED |
| SFal-2 (global quotient inconsistency) | This memo §6.2 | NOT TRIGGERED |
| SFal-3 (commitment-rule inconsistency) | This memo §6.3 | NOT TRIGGERED |
| SFal-4 (primitive-level global incompatibility) | This memo §6.4 | NOT TRIGGERED |
| SFal-5 (circular dependence on Arc M) | Memo 02 (Theorem 17 derivation) | DEFERRED |
| SFal-6 (acyclicity break) | This memo §6.5 | NOT TRIGGERED |

Five of six synthesis falsifiers dispatched without trigger.

---

## 7. Provisional synthesis verdict

**Verdict: CANDIDATE-FORCED.**

**Justification.**
- Global integration of Q.2 + Q.3 + Q.7 + Q.8 produces a unified structural object (§2.5) with internally consistent four-axis × three-branch × four-channel structure.
- Global commitment ledger consistent (§3): additivity rule clean, no double-counting, acyclicity preserved.
- Global quotient ledger consistent (§4): all six cross-channel pairs PASS; non-Abelian global consistency PASSES.
- Primitive-level global audit consistent (§5): seven primitives load-bearing, all compatible globally.
- Five of six synthesis falsifiers NOT TRIGGERED (only SFal-5 remains, dispatched in Memo 02).
- Refinement-closure map: 7/7 CLOSED (inherited from Q.8 Memo 03).

**Per discipline:** Memo 01 closes CANDIDATE-FORCED rather than FORCED because final FORCED-unconditional promotion lives at Memo 02 with the Theorem 17 statement and SFal-5 dispatch. Memo 01's role is to *certify* that everything except the theorem statement itself is in place.

**Ready-for-Theorem-17 certification: ISSUED.**

---

## 8. Implications for Theorem 17

### 8.1 What Memo 02 must do

To promote GRH from CANDIDATE-FORCED to FORCED-unconditional, Memo 02 must:

1. **State Theorem 17 in canonical form** — a single, self-contained theorem statement derivable from primitives + Theorems 1–16 + Q-substage verdicts alone, with no conditional clauses at the structural level.
2. **Derive Theorem 17 explicitly** from the unified global structural object (Memo 01 §2.5) + unified commitment ledger (§3) + unified quotient ledger (§4) + primitive ledger (§5).
3. **Dispatch SFal-5** — verify that Theorem 17 derivation does not implicitly use Arc M results (F-M8 in particular).
4. **Issue FORCED-unconditional verdict** — update FORCED-theorem inventory from 16 to 17.
5. **Map Arc M cascade** — explicit identification of how Theorem 17 unblocks F-M8 promotion and any other Arc M items dependent on GRH closure.

### 8.2 Minimal structural payload of Theorem 17

Theorem 17 must encode:

- **(Carrier)** τ_g is a structural rule-type whose participation measure is the gauge field A_μ (GRH-1 + GRH-2).
- **(Group)** τ_g admits a non-Abelian-capable gauge-group structure with Killing-form / Jacobi closure (R-2 + R-4, Q.2).
- **(Vertex)** Commitment events are vertex-anchored; minimal coupling supplies the structural vertex (R-3 Q.3-side, Q.3).
- **(Worldline)** τ_g excitations propagate on lightlike worldlines with second-quantised excitation lifting (R-1 + R-3 Q.7-side + R-5 partial, Q.7).
- **(Vacuum)** τ_g vacuum sector carries a gauge-invariant, UV-finite, V1-form, stationary fluctuation envelope; vacuum is strict-non-committing with V1-form additive background functional B[v] (R-3 Q.8-side + R-5 completion + VQ4, Q.8).
- **(Quotient)** All four channels respect a single unified gauge-quotient identification under the gauge group (§4).
- **(Acyclicity)** Theorem 17 derivable from primitives + Theorems 1–16 + Q-substage verdicts alone (§6.5 + Memo 02 SFal-5 dispatch).

### 8.3 Remaining sensitivities + global checks for Memo 02

- **Sensitivity-C2 (§3.4):** vacuum-excitation independence in bandwidth additivity. Flagged; Memo 02 should re-confirm in the theorem-statement context.
- **Sensitivity-Q1 (§4.5):** unified gauge group across all four channels. Flagged; Memo 02 should explicitly note SSB exclusion in scope-limit clause.
- **SFal-5 dispatch:** the only remaining falsifier; Memo 02 will trace the Theorem 17 derivation chain and confirm no Arc M input.

---

## 9. Honest scope limits

Memo 01 cannot resolve:
- **Theorem 17 statement** (lives in Memo 02).
- **SFal-5 dispatch** (concerns the Theorem 17 derivation itself; lives in Memo 02).
- **Arc M cascade map** (lives in Memo 02).
- **Numerical magnitudes** (value-layer; INHERITED throughout).
- **SM-specific content** (forbidden; out of synthesis scope).
- **F-M8 promotion** (Arc M cascade; downstream of Theorem 17).

Must be deferred to Memo 02:
- Theorem 17 canonical statement.
- SFal-5 dispatch.
- FORCED-unconditional verdict.
- Arc M cascade map.

---

## 10. One-line summary

**Global integration of Q.2 + Q.3 + Q.7 + Q.8 produces a single unified structural object with consistent four-axis × three-branch × four-channel content; SFal-1 / SFal-2 / SFal-3 / SFal-4 / SFal-6 all NOT TRIGGERED; ready-for-Theorem-17 certification issued, leaving only SFal-5 dispatch + Theorem 17 statement for Memo 02.**

---

## Recommended Next Steps

1. **Begin Arc Q synthesis Memo 02** — Derive Theorem 17 in canonical form from the unified structural object; dispatch SFal-5; issue FORCED-unconditional verdict; map Arc M cascade.
2. **Pre-stage Arc M cascade memo (F-M8 promotion)** — Will fire as soon as Theorem 17 lands.
3. **Bundled memory-record update** — Defer until Memo 02 closes.
4. **Update Sixteen-Theorems SVG catalogue** — Promote anticipated Theorem 17 to confirmed slot once Memo 02 closes.
5. *(Optional)* Draft skeleton Theorem 17 statement now (using §8.2 minimal payload) as forward-reference target for Memo 02.
