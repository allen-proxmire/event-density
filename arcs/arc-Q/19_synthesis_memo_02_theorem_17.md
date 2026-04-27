# Arc Q Synthesis — Memo 02: Theorem 17 (GRH) and Arc Q Closure

**Arc:** Q (GRH closure trajectory)
**Stage:** Synthesis (terminal memo)
**Memo:** 02 — Theorem 17 statement, FORCED-unconditional verdict, Arc M cascade map, Arc Q closure
**Status on entry:** Synthesis Memo 01 ready-for-Theorem-17 certification issued; SFal-1, SFal-2, SFal-3, SFal-4, SFal-6 all NOT TRIGGERED; SFal-5 reserved for this memo.
**Status on exit:** **Theorem 17 (GRH) — FORCED-unconditional. Arc Q CLOSED.** FORCED-theorem inventory advances 16 → 17. Arc M F-M8 cascade unblocked.

---

## 1. The synthesis task, restated

**What Memo 02 must accomplish.**

1. State Theorem 17 (GRH) in canonical form (physics-facing + structural/refinement-indexed).
2. Provide the proof sketch tying Theorem 17 to R-1, R-2 FULL, R-3 FULL, R-4, R-5 FULL plus the unified global structural object from Memo 01.
3. Dispatch SFal-5 (Arc M circularity) — the only synthesis falsifier still outstanding.
4. Promote GRH from CANDIDATE-FORCED-across-substages to **FORCED-unconditional**.
5. Issue the final Arc Q verdict.
6. Map the cascade into Arc M (F-M8 promotion + downstream).
7. Close Arc Q.

**Why Theorem 17 is now admissible.** Three structural conditions for FORCED-unconditional promotion (Memo 00 §1) are all met:
- All upstream verdicts CLOSED with no falsifier triggered (Q.1 + Q.2 + Q.3 + Q.7 + Q.8).
- All cross-substage and acyclicity audits PASS (Synthesis Memo 01).
- Theorem statement derivable from primitives + Theorems 1–16 + Q-substage verdicts alone (this memo, §3).

The only remaining check is SFal-5 — that the Theorem 17 derivation chain itself does not implicitly use Arc M. §4 dispatches it.

**How Memo 02 completes Arc Q.** Memo 02 is the *terminal* memo of Arc Q. After this memo, Arc Q has no open items: GRH is FORCED-unconditional, the refinement-closure map is 7/7, all twelve substage falsifiers and all six synthesis falsifiers are dispatched, and the cascade map into Arc M is explicit.

---

## 2. Canonical statement of Theorem 17 (GRH)

### 2.1 Physics-facing statement

> **Theorem 17 (Gauge-field-as-Rule-Type Hypothesis, FORCED-unconditional).**
>
> *In the Event Density framework, the gauge field A_μ is the participation measure of a structural rule-type τ_g. The rule-type τ_g admits a non-Abelian-capable gauge-group structure with Killing-form / Jacobi closure; its excitations propagate on lightlike worldlines with second-quantised excitation lifting; commitments are vertex-anchored at the excitation level via a structural minimal-coupling vertex; the vacuum sector carries a gauge-invariant, UV-finite, V1-form, stationary fluctuation envelope, is strict-non-committing, and contributes a gauge-invariant V1-form background functional B[v;τ_g] additively to vertex-anchored commitment rates in non-vacuum states; all four channels (group, vertex, worldline, vacuum) respect a single unified gauge-quotient identification under the gauge group. The form of these structural commitments is forced by the primitives and Theorems 1–16; the numerical magnitudes (specific gauge group, coupling values, V1 kernel parameters, B[v] amplitude, vacuum energy density) are inherited from the value layer and not committed by the theorem.*

### 2.2 Structural / refinement-indexed statement

> **Theorem 17 (GRH, structural form).**
>
> Under ED primitives P-02, P-04, P-06, P-07, P-10, P-11, P-13 and FORCED theorems 1–16, the structural rule-type τ_g whose participation measure is the gauge field A_μ satisfies:
>
> **(C1) Carrier.** τ_g is a rule-type (P-02) with a non-empty participation measure on the gauge-Lie-algebra fibre (GRH-1, GRH-2). [Q.1 baseline.]
>
> **(C2) Group structure (R-2 + R-4, Q.2).** τ_g admits a non-Abelian-capable gauge-group structure with Killing-form / Jacobi closure; gauge-equivalent τ_g configurations are identified at group level.
>
> **(C3) Vertex (R-2 completion + R-3 Q.3-side, Q.3).** Commitment events for τ_g are vertex-anchored; the structural minimal-coupling vertex is gauge-quotient-invariant; the vertex-quotient is the pullback of the group-quotient through coupling.
>
> **(C4) Worldline (R-1 + R-3 Q.7-side + R-5 partial, Q.7).** Excitations of τ_g propagate on lightlike worldlines (R-1); the vertex-anchored commitment ledger lifts to an ordered worldline ledger {v_i}; second-quantised excitation lifting supplies a Fock-style count.
>
> **(C5) Vacuum kernel (R-5 completion form-side, Q.8 VQ1).** The no-excitation sector of τ_g carries a gauge-invariant, UV-finite, V1-form, stationary fluctuation envelope (the τ_g vacuum kernel), inherited as restriction of the global V1 vacuum kernel of Theorem 8.
>
> **(C6) Vacuum classification (Q.8 VQ2).** Three admissible classes (background / excitation / mixed) on two orthogonal axes (background expectation × worldline support); excitation-vacuum is the minimal FORCED class.
>
> **(C7) Vacuum commitment (R-3 Q.8-side + R-5 completion commitment-side, Q.8 VQ3).** The vacuum is strict-non-committing (forced by P-06 + P-07); a gauge-invariant V1-form background functional B[v;τ_g] contributes additively (P-04) to vertex-anchored commitment rates Γ_global[v;s] = Γ_excitation[v;τ_g,s] + B[v;τ_g] in non-vacuum states.
>
> **(C8) Unified quotient (Q.8 VQ4 + Synthesis Memo 01 §4).** All four channels (group / vertex / worldline / vacuum) respect a single unified gauge-quotient identification given by the orbits of the Q.2 gauge group; non-Abelian Killing-form / Jacobi consistency propagates through all four channels.
>
> **(C9) Acyclic derivability.** (C1)–(C8) are derivable from P-02..P-13 + Theorems 1–16 + Q-substage verdicts alone, with no input from Arc M or any other downstream stage.
>
> The numerical magnitudes (specific gauge group, coupling values, V1 kernel parameters, B[v] amplitude, vacuum energy density) are INHERITED from the value layer and are not committed by Theorem 17.

### 2.3 Status declaration

**Form FORCED, value INHERITED. FORCED-unconditional at the structural level.**

---

## 3. Proof sketch / justification

We trace each of (C1)–(C9) to its primitive + theorem + verdict provenance, then close the global integration.

### 3.1 (C1) — Carrier

Direct: P-02 commits τ_g to existence as a rule-type; GRH-1 + GRH-2 commit A_μ to being its participation measure on the gauge-Lie-algebra fibre. Q.1 baseline (Theorem 5, GRH form-level) establishes this as form-level FORCED. **Provenance: P-02 + GRH-1 + GRH-2 + Theorem 5.**

### 3.2 (C2) — Group structure

R-2 partial + R-4 close in Q.2 (Memos 01–02): non-Abelian extension via Killing-form + Jacobi + structure-constant admissibility, with gauge-quotient identification at group level. **Provenance: P-10 + Q.2 verdict + R-2 partial + R-4.**

### 3.3 (C3) — Vertex

R-2 completion + R-3 Q.3-side close in Q.3 (Memos 01–02): vertex taxonomy + minimal-coupling structural vertex (V1+V2+V4 partial) + vertex-quotient extension (V3+V4) + vertex-anchored commitment (P-06 + P-07). **Provenance: P-06 + P-07 + P-10 + Q.3 verdict + R-2 completion + R-3 Q.3-side.**

### 3.4 (C4) — Worldline

R-1 + R-3 Q.7-side + R-5 partial close in Q.7 (Memos 01–02): eikonal/null-geodesic limit forces lightlike worldline; vertex ledger lifts onto worldline; second-quantisation via Theorem 6 (canonical (anti-)commutation). **Provenance: P-13 + Q.7 verdict + Theorem 6 + R-1 + R-3 Q.7-side + R-5 partial.**

### 3.5 (C5) — Vacuum kernel

VQ1 closes in Q.8 Memo 01 via six constraints (non-vacuity, UV-FIN, V1-form, gauge-invariance, bandwidth additivity, stationarity). Inherits Theorem 7 (UV-FIN) + Theorem 8 (V1 vacuum kernel). **Provenance: P-02 + P-04 + P-10 + P-11 + P-13 + Theorem 7 + Theorem 8 + Q.8 Memo 01 + R-5 completion form-side.**

### 3.6 (C6) — Vacuum classification

VQ2 closes in Q.8 Memo 01: three classes on two axes (background expectation × worldline support); excitation-vacuum minimal FORCED. **Provenance: Q.7 worldline + VQ1 + R-2 + Q.8 Memo 01.**

### 3.7 (C7) — Vacuum commitment

VQ3 closes in Q.8 Memo 02: P-07 forces strict non-commitment at vacuum (no anchor); P-04 forces additive composition; V1-form B[v] inherits from VQ1. Global integration rule Γ_global = Γ_excitation + B established in Synthesis Memo 01 §3. **Provenance: P-04 + P-06 + P-07 + Q.8 Memo 02 + R-3 Q.8-side + R-5 completion commitment-side + Synthesis Memo 01 §3.**

### 3.8 (C8) — Unified quotient

VQ4 closes in Q.8 Memo 02 (four channels PASS); Synthesis Memo 01 §4 dispatches the global six-pair cross-channel audit (all PASS) and confirms non-Abelian global consistency. **Provenance: P-10 + Q.8 Memo 02 + Synthesis Memo 01 §4 + R-2 + R-4.**

### 3.9 (C9) — Acyclic derivability

All eight content-clauses (C1)–(C8) trace exclusively to upstream items: primitives P-02..P-13, Theorems 1–16, Q-substage verdicts (Q.1 + Q.2 + Q.3 + Q.7 + Q.8), refinements R-1 + R-2 FULL + R-3 FULL + R-4 + R-5 FULL, and the unified global structural object constructed in Synthesis Memo 01. **No downstream item invoked.** SFal-5 is dispatched in §4.

### 3.10 Falsifier integration

| Falsifier source | Status |
|---|---|
| Q.2 substage falsifiers (F-falsifiers) | All NOT TRIGGERED (Q.2 Memo 03). |
| Q.3 substage falsifiers (V-falsifiers) | All NOT TRIGGERED (Q.3 Memo 03). |
| Q.7 substage falsifiers (W-falsifiers, incl. WFal-5 circularity) | All NOT TRIGGERED (Q.7 Memo 03). |
| Q.8 substage falsifiers (VQ-falsifiers, incl. VQFal-4 circularity) | All NOT TRIGGERED (Q.8 Memo 03). |
| Synthesis SFal-1 (cross-substage) | NOT TRIGGERED (Synthesis Memo 01 §6.1). |
| Synthesis SFal-2 (global quotient) | NOT TRIGGERED (Synthesis Memo 01 §6.2). |
| Synthesis SFal-3 (commitment-ledger) | NOT TRIGGERED (Synthesis Memo 01 §6.3). |
| Synthesis SFal-4 (primitive global) | NOT TRIGGERED (Synthesis Memo 01 §6.4). |
| Synthesis SFal-6 (acyclicity) | NOT TRIGGERED (Synthesis Memo 01 §6.5). |
| **Synthesis SFal-5 (Arc M circularity)** | **NOT TRIGGERED (this memo, §4).** |

**No falsifier blocks Theorem 17.**

---

## 4. SFal-5 dispatch (Arc M circularity)

**Test.** Does the Theorem 17 derivation (clauses C1–C9) implicitly use any Arc M result — most importantly the F-M8 mass-form item — as an upstream input?

**Trace by clause.**

- **(C1) Carrier.** Provenance: P-02 + GRH-1 + GRH-2 + Theorem 5. Theorem 5 (GRH form-level) is in the Q-arc inventory (Theorem 5: GRH unconditional Q.1 + Q.8 form-level), not Arc M. **No Arc M input.**
- **(C2) Group structure.** Provenance: P-10 + Q.2 verdict + R-2 partial + R-4. Q.2 work is Q-internal. **No Arc M input.**
- **(C3) Vertex.** Provenance: P-06 + P-07 + P-10 + Q.3 verdict. Q.3 work is Q-internal. **No Arc M input.**
- **(C4) Worldline.** Provenance: P-13 + Q.7 verdict + Theorem 6 + R-1 + R-3 Q.7-side + R-5 partial. Theorem 6 (canonical (anti-)commutation) is Q-arc, not Arc M. **No Arc M input.**
- **(C5) Vacuum kernel.** Provenance: P-02 + P-04 + P-10 + P-11 + P-13 + Theorem 7 + Theorem 8 + Q.8 Memo 01. Theorem 7 (UV-FIN) is Q-arc; Theorem 8 (V1 vacuum kernel) is Arc N (not Arc M). **No Arc M input.**
- **(C6) Vacuum classification.** Provenance: Q.7 + VQ1 + R-2 + Q.8 Memo 01. **No Arc M input.**
- **(C7) Vacuum commitment.** Provenance: P-04 + P-06 + P-07 + Q.8 Memo 02 + Synthesis Memo 01 §3. **No Arc M input.**
- **(C8) Unified quotient.** Provenance: P-10 + Q.8 Memo 02 + Synthesis Memo 01 §4 + R-2 + R-4. **No Arc M input.**
- **(C9) Acyclic derivability.** Self-referential consistency check; no Arc M input by construction.

**Specifically: F-M8 (Arc M mass-form item) is NOT invoked anywhere in the Theorem 17 derivation.** F-M8's promotion is a *consequence* of Theorem 17 (mapped in §6 below), not an input to it.

**Acyclicity argument.** The full dependency chain is:

```
Primitives + Theorems 1–16 (Theorem 8 from Arc N; Theorems 5, 6, 7 from Arc Q form-level)
        │
        ▼
Q.1 → Q.2 → Q.3 → Q.7 → Q.8 (Q-substage closures)
        │
        ▼
Synthesis Memo 01 (global integration + 5/6 SFals dispatched)
        │
        ▼
Theorem 17 (this memo)
        │
        ▼
Arc M cascade (F-M8 promotion)
```

There is no back-edge from Arc M to any node in this chain. The vacuum-to-vertex commitment-rate additivity (Synthesis Memo 01 §3.3) is forward-only. The Q-substage internal circularity checks (WFal-5 in Q.7, VQFal-4 in Q.8) and the synthesis-level acyclicity check (SFal-6 in Memo 01) all PASSED. SFal-5 here completes the acyclicity certification at the Theorem 17 derivation level.

**SFal-5 NOT TRIGGERED.**

---

## 5. Final Arc Q verdict

**Verdict: FORCED-unconditional.**

**Justification.**
- Theorem 17 stated in canonical form (§2.1 + §2.2) with full structural payload (C1)–(C9).
- Proof sketch (§3) traces each clause to primitives + Theorems 1–16 + Q-substage verdicts alone.
- All twelve Q-substage falsifiers + all six synthesis falsifiers NOT TRIGGERED.
- Refinement-closure map: 7/7 CLOSED (R-1, R-2 FULL, R-3 FULL, R-4, R-5 FULL).
- Global integration: unified four-axis × three-branch × four-channel structure consistent (Synthesis Memo 01 §2–§5).
- SFal-5 dispatch (§4): no Arc M input invoked; acyclicity preserved.
- Per discipline (Memo 00 §1 definition of "FORCED-unconditional"): all four conditions met (derivable from primitives + prior FORCED theorems alone; all upstream verdicts CLOSED; cross-substage + acyclicity audits PASS; no conditional clauses at structural level).

**FORCED-theorem inventory:** advances 16 → **17**. Theorem 17 (GRH) is the 17th FORCED structural theorem in ED inventory and the **fifth FORCED theorem in Arc Q** (joining Theorems 5, 6, 7, plus the Q-form-level baselines).

**Arc Q closure declaration:** Arc Q is **CLOSED**. No open Q-internal item remains.

---

## 6. Arc M cascade map (F-M8)

### 6.1 What Arc M inherits from Theorem 17

| Inherited content | From Theorem 17 clause | Use in Arc M |
|---|---|---|
| Non-Abelian gauge-group capability | (C2) | Closes Arc M's gauge-group dependency for mass-form items that require non-Abelian context. |
| Vertex-anchored commitment + minimal coupling | (C3) | Supplies the structural vertex into which Arc M mass-form contributions enter as additive corrections. |
| Lightlike-worldline structure for τ_g excitations | (C4) | Establishes the massless-default for τ_g excitations at the structural form-level (mass magnitude is INHERITED, not committed). |
| V1 vacuum kernel + B[v] background | (C5) + (C7) | Supplies the vacuum-kernel-mediated mass-form contribution channel — this is precisely what F-M8 was waiting on. |
| Unified gauge-quotient | (C8) | Certifies that Arc M mass-form items respect gauge-quotient identification globally. |

### 6.2 What F-M8 promotes to

F-M8 was the Arc M item awaiting GRH closure: the τ_g-mediated structural mass-form contribution via the V1 vacuum kernel. With Theorem 17 in inventory:

- **Form FORCED** at Arc M: F-M8 promotes to FORCED-conditional or FORCED-unconditional within Arc M (depending on Arc M's own internal audit).
- **Magnitude INHERITED** from V1 kernel parameter and B[v] amplitude (consistent with Arc M's "form FORCED, value INHERITED" verdict).

### 6.3 What Arc M must prove next (after F-M8 promotion)

| Item | Description | Status pre-Arc-M-cascade |
|---|---|---|
| F-M8 promotion | Arc M's τ_g-mediated mass-form item promotes via V1 background functional | UNBLOCKED |
| Massless-slot resolution | Whether τ_g excitations remain massless at form-level (Arc M consistency check) | OPEN |
| Mass-form additivity | Verification that F-M8 contribution composes additively with other Arc M mass-form items per P-04 | OPEN |
| τ_g coupling to other rule-types' mass forms | Whether B[v] background contributes to mass forms of other rule-types via cross-sector kernel coupling | OPEN |
| Arc M global re-audit | Whether Arc M synthesis verdict needs update post-F-M8 promotion | OPEN |

These are Arc-M-internal items; Arc Q does not own them. Arc Q's responsibility ends with the F-M8 promotion *trigger*.

### 6.4 Cascade dependency graph

```
Theorem 17 (GRH FORCED-unconditional)
        │
        ├──► F-M8 promotion (Arc M cascade memo)
        │           │
        │           ├──► Arc M massless-slot resolution
        │           ├──► Arc M mass-form additivity audit
        │           └──► Arc M cross-sector coupling audit
        │
        ├──► Inventory update: 16 → 17 FORCED theorems
        │
        └──► (Independent) Empirical-test program: B[v] background contributions
              detectable via vertex-anchored commitment-rate measurements?
              (Speculative; lives outside Arc Q.)
```

---

## 7. Honest scope limits

**Theorem 17 does NOT claim:**
- A specific gauge group of nature (SU(3)×SU(2)×U(1) is empirical / SM-specific; (C2) commits only to non-Abelian-capable group *structure*).
- Any specific coupling magnitude (α, α_s, sin²θ_W are empirical).
- Any specific vacuum energy density (INHERITED from V1 kernel parameter; cosmological constant Λ value lives in Arc N + Phase-3 GR).
- Any SM vacuum content (Higgs VEV, QCD condensates, instantons, θ-vacua all forbidden inputs).
- Any QFT vacuum prescription (path-integral measure, Faddeev-Popov, BRST, dimensional regularisation all forbidden).
- Any specific propagator form for τ_g excitations.
- Any thermal / observer-dependent vacuum content.
- Vacuum-stability questions (false-vacuum decay etc.).
- Mass magnitudes for τ_g excitations or other rule-types (Arc M value layer).

**What remains for Arc M:**
- F-M8 promotion (cascade memo).
- Massless-slot resolution.
- Mass-form additivity audit.
- Cross-sector coupling audit.
- Arc M synthesis verdict update.

**What remains for Phase-3 GR:**
- GR-side integration of B[v] vacuum kernel into curved-spacetime contexts (extends Arc N's V1-with-Synge-world-function framework).

**What remains for empirical work:**
- Detection of B[v] background contributions to commitment rates (speculative).
- Specific numerical predictions (require value-layer inheritance).

---

## 8. One-line summary

**Theorem 17 (GRH) is the FORCED-unconditional structural theorem stating that the gauge field A_μ is the participation measure of a rule-type τ_g whose group / vertex / worldline / vacuum content is fully forced by ED primitives + Theorems 1–16 across all five refinement axes (R-1, R-2 FULL, R-3 FULL, R-4, R-5 FULL) and unified under a single global gauge-quotient — closing Arc Q, advancing the FORCED-theorem inventory 16 → 17, and unblocking the Arc M F-M8 cascade.**

---

## Recommended Next Steps

1. **Write the Arc M cascade memo (F-M8 promotion)** — the immediate downstream consequence of Theorem 17; promotes F-M8 form-level via inherited B[v] background channel.
2. **Bundled memory-record update** — Update `project_qm_emergence_arc.md` + main `MEMORY.md` index with: Arc Q CLOSED, Theorem 17 added, FORCED-theorem inventory 16 → 17, Arc M cascade unblocked, four-stage GRH closure trajectory complete.
3. **Update the Sixteen-Theorems SVG catalogue** → **Seventeen-Theorems**: add Theorem 17 (GRH FORCED-unconditional) with the §2.1 physics-facing one-paragraph statement.
4. **Begin a publication paper for Arc Q** (`papers/Arc_Q/`) — analogous to Arc R / Arc M / Arc N papers — with Theorem 17 as its centrepiece result.
5. *(Optional)* Draft a desktop "Science Friday"-voice explainer for Theorem 17 (`ED_Theorem17_GRH_Explainer.md`) for the public-facing track.
