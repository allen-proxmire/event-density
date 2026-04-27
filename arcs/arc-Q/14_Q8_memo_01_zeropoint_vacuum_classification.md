# Q.8 Memo 01 — Zero-Point Structure and Vacuum Classification for τ_g

**Arc:** Q (GRH closure trajectory)
**Substage:** Q.8 — Vacuum / zero-point structural classification for τ_g
**Memo:** 01 (substantive: VQ1 + VQ2)
**Status on entry:** Q.2 ✅ Q.3 ✅ Q.7 ✅; R-1, R-2 (full), R-3 (Q.3 + Q.7), R-4, R-5 partial CLOSED. Only R-5 completion + R-3 Q.8-side outstanding.
**Status on exit:** VQ1 + VQ2 → CANDIDATE-FORCED; R-5 completion structurally derived (subject to VQ3 + VQ4 audit in Memo 02).

---

## 1. The VQ1 and VQ2 questions, restated

**VQ1 — Zero-point structure for τ_g.** What structural content does τ_g possess in the absence of an excitation? Concretely: in any state with zero excitation count for the gauge rule-type, is there (a) no structural content at all, (b) a kernel-bounded structural fluctuation envelope, (c) a kernel-modulated coherence structure, or (d) a mixed configuration — and which of these is FORCED by primitives + prior verdicts + inherited theorems?

**VQ2 — Vacuum classification.** Given an answer to VQ1, what classes of τ_g state are admissible at zero excitation count? Specifically:
- a **background vacuum** (non-zero structural expectation, no worldline support),
- an **excitation vacuum** (zero structural expectation, worldline-supported in the sense of Q.7's lifting structure),
- a **mixed vacuum** (background + excitation).

What is the structural criterion that assigns a configuration to one class versus another?

**Joint role in R-5 completion.** R-5 partial (closed in Q.7) addressed only the *excitation-side*: it established that a τ_g excitation (a "particle") lifts via the Q.7 second-quantisation structure with a definite worldline + commitment ledger. R-5 completion requires the *vacuum-side*: a structural account of τ_g when no excitation is present. **VQ1 supplies the zero-point structural content; VQ2 supplies the classification of admissible vacuum states.** Together they close R-5 in the form sense; the *commitment* status of the vacuum (does the vacuum commit?) is VQ3, handled in Memo 02.

---

## 2. Structural commitments for VQ1 (zero-point structure)

### 2.1 Minimal structural form

We seek the **minimal** zero-point content for τ_g that is consistent with all upstream commitments. "Minimal" here means: any reduction below this content triggers a falsifier; any addition above it requires a new CANDIDATE.

**Claim.** The minimal structural zero-point content for τ_g is a **gauge-invariant, finite-width, V1-form fluctuation envelope** — i.e., the no-excitation sector of τ_g carries a non-trivial structural fluctuation kernel of the same V1 form (finite-width, kernel-bounded) established by Theorem 8 for the generic vacuum sector, restricted to the gauge rule-type, and quotiented by the gauge action established in R-2.

We now derive the four constraints that force this form.

### 2.2 Constraint 1 — Non-vacuity (from P-02 + GRH-2)

P-02 commits any rule-type that exists structurally to *having* a structural carrier in any admissible state, vacuum included. GRH-2 (vertex-anchored participation measure) commits τ_g to being a participation measure of a *non-empty* rule-type. Combined: τ_g cannot have *zero* structural content in the vacuum sector — there must be at least a fluctuation envelope. **Excludes option (a) "no structural content at all."**

### 2.3 Constraint 2 — UV finiteness (from P-11 + Theorem 7)

P-11 forbids divergent structural content at any scale. Theorem 7 (UV-FIN, Arc Q form-level) commits the entire ED structural envelope to UV-finiteness. The vacuum sector of τ_g is part of that envelope; therefore its zero-point fluctuation kernel must be UV-finite. **Excludes any kernel form whose support is unbounded in mode-frequency or whose magnitude diverges in any UV limit.**

### 2.4 Constraint 3 — V1 form (from Theorem 8 + N-arc kernel discipline)

Theorem 8 establishes that the vacuum kernel is V1 (finite-width, Markov-compatible-but-not-Markov-forcing). The vacuum sector of τ_g is a *restriction* of the global vacuum kernel to the gauge rule-type carrier. By the form-restriction discipline (Arc N memo N.5 + supporting), restriction of a V1 kernel to a sub-rule-type carrier is itself V1, unless the restriction breaks the finite-width property — which would require additional non-V1 structure (a new CANDIDATE). **Forces option (b) or (c) into V1 form; excludes any non-V1 zero-point kernel.**

### 2.5 Constraint 4 — Gauge invariance (from R-2 + P-10)

R-2 (full closure in Q.2) commits gauge-equivalent τ_g configurations to identification. P-10 enforces gauge-quotient identification at primitive level. The vacuum kernel must therefore be gauge-invariant — its form cannot depend on a fixed-gauge representative. **Excludes any kernel form that picks out a preferred gauge.**

### 2.6 Constraints 5 — Bandwidth additivity (from P-04)

P-04 commits independent rule-type sectors to additive bandwidth composition. The vacuum sector of τ_g must therefore have a bandwidth contribution that adds linearly with bandwidth contributions from other independent rule-type sectors at vacuum. This is automatically satisfied by V1-form kernels (variance-based composition is additive over independent sectors), so Constraint 5 *constrains* but does not further narrow the form beyond what Constraints 1–4 already deliver.

### 2.7 Constraint 6 — Continuous-time closure (from P-13 + Theorem 16)

P-13 commits the global structural envelope to closure under continuous-time evolution. Theorem 16 (Schrödinger evolution) identifies the time-translation generator with the Hamiltonian. The vacuum sector of τ_g must therefore be invariant under the time-translation generator (a stationary vacuum), or admit a structurally-derivable time-dependence (e.g., a slowly-varying background). The minimal form consistent with everything above is **stationarity** — a time-translation-invariant V1 vacuum kernel. Time-dependent backgrounds are admissible but require additional CANDIDATE (e.g., specifying a background evolution); they are therefore *not* minimal.

### 2.8 What is FORCED, what remains empirical

| Aspect | Status |
|---|---|
| Existence of a non-zero zero-point fluctuation envelope for τ_g | **FORCED** (Constraint 1) |
| UV-finiteness of that envelope | **FORCED** (Constraint 2) |
| V1 form (finite-width, kernel-bounded) | **FORCED** (Constraint 3) |
| Gauge-invariance of the vacuum kernel | **FORCED** (Constraint 4) |
| Bandwidth additivity over independent rule-type sectors | **FORCED** (Constraint 5) |
| Stationarity (time-translation invariance) of minimal vacuum | **FORCED** (Constraint 6, minimal branch) |
| **Numerical magnitude of the vacuum fluctuation amplitude** | **EMPIRICAL** (inherited from the V1 kernel parameter, value layer) |
| **Numerical width of the vacuum kernel** | **EMPIRICAL** (inherited; same as Arc N) |
| Closed-form theorem statement (FORCED-unconditional GRH at vacuum) | **DEFERRED** to Arc Q synthesis |

**Form FORCED, value INHERITED** — same Arc M / Arc Q discipline.

---

## 3. Structural commitments for VQ2 (vacuum classification)

### 3.1 The three admissible classes

Given the VQ1 minimal form, we classify admissible vacuum states by two structural axes: (i) **background expectation** (does the τ_g configuration have a non-zero expectation in the vacuum?) and (ii) **worldline support** (does the vacuum configuration sit on the Q.7 lightlike-worldline support of an excitation?).

| Class | Background expectation | Worldline support | Structural criterion |
|---|---|---|---|
| **Background vacuum** | Non-zero | Absent | Stationary V1 kernel + non-zero gauge-invariant background expectation (e.g., a constant gauge-invariant scalar built from τ_g); no Q.7 worldline anchor. |
| **Excitation vacuum** | Zero | Present (degenerate) | Stationary V1 kernel + zero expectation; Q.7 worldline structure is present but in its degenerate "no excitation count" sector. |
| **Mixed vacuum** | Non-zero | Present (degenerate) | Stationary V1 kernel + non-zero background + Q.7 degenerate worldline support. |

### 3.2 Structural criteria

- **Background vacuum** is admissible iff a gauge-invariant scalar built from τ_g admits a non-trivial structurally-FORCED expectation. At the form level, no such scalar is forced; therefore background vacuum is *admissible but not forced* (the trivial-background branch is the minimal one, with non-trivial background lifted to a value-layer choice).
- **Excitation vacuum** is the *minimal* class: it is the no-excitation sector of the Q.7 second-quantised structure, restricted to zero count. It is FORCED-admissible.
- **Mixed vacuum** is admissible whenever both criteria are met simultaneously; the structural rule for combining them is additive (P-04 bandwidth additivity over independent contributions).

### 3.3 Consequences

| Consequence | Effect |
|---|---|
| **Worldline density** | In excitation-class vacuum, the Q.7 worldline density at zero count is well-defined as the kernel restriction; in background-class vacuum, worldline density is structurally absent (no excitation anchor); in mixed vacuum, density inherits from the excitation component. |
| **Commitment-rate construction** | Excitation-vacuum admits the Q.3-Q.7 commitment-rate machinery in its degenerate (zero-rate) limit; background-vacuum admits no commitment-rate (deferred to VQ3 / Memo 02 for full treatment); mixed vacuum inherits from the excitation component. |
| **Gauge-quotient individuation** | All three classes must respect R-2; this is automatic for excitation- and mixed-vacuum (inherited from Q.7); for background-vacuum the criterion *is* the gauge-invariance of the background scalar (Constraint 4 of §2). |
| **Second-quantised correspondence** | Excitation-vacuum is the structural analog of the Fock vacuum |0⟩ at the τ_g sector; background-vacuum is the structural analog of a non-trivial classical background (no Fock-vacuum analog at this level); mixed vacuum is the structural analog of a coherent-state-over-vacuum hybrid. |

---

## 4. Primitive-level audit for VQ1 and VQ2

For each primitive, we test compatibility with VQ1 (zero-point structure) and VQ2 (vacuum classification), and classify it as **supports / neutral / constrains / forbids**.

| Primitive | VQ1 (zero-point) | VQ2 (classification) | Falsifier implication |
|---|---|---|---|
| **P-02** (rule-types as structural carriers) | **supports** — forces non-vacuity (Constraint 1) | **supports** — admits all three classes | None. |
| **P-04** (bandwidth additivity) | **constrains** — forces additive composition over sectors | **constrains** — forces additive combination in mixed-vacuum class | Would trigger VQFal-1 if VQ1 form violated additivity; does not. |
| **P-06** (commitment events) | **neutral** at vacuum (commitments are vertex-anchored, Q.3) | **neutral** — commitment-rate at vacuum deferred to VQ3 | None at this memo; load for Memo 02. |
| **P-07** (vertex anchoring) | **neutral** — vertex anchoring is excitation-side; vacuum sector has no vertex anchor unless excitation present | **constrains** — forces excitation-vacuum to inherit Q.7 degenerate worldline support | None; defines worldline-support axis cleanly. |
| **P-10** (gauge-quotient identification) | **constrains** — forces gauge-invariant kernel form (Constraint 4) | **constrains** — forces background scalar to be gauge-invariant if non-trivial | Would trigger VQFal-1 + VQFal-2 if violated; does not. |
| **P-11** (UV-FIN) | **constrains** — forces UV-finite kernel (Constraint 2) | **constrains** — forces all admissible vacua to have UV-finite envelopes | Direct relevance to VQFal-6 + VQFal-7; not triggered. |
| **P-13** (continuous-time closure) | **constrains** — forces stationarity in minimal branch (Constraint 6) | **constrains** — forces classification to be time-translation-invariant in minimal branch | Would trigger VQFal-1 if VQ1 form violated time-translation closure; does not. |

**Summary:** No primitive *forbids* VQ1 or VQ2 in their minimal-form derivation. Five primitives *constrain* and force the V1 form + gauge-invariance + UV-finiteness + stationarity. Two primitives are *neutral / supportive* at the vacuum (P-02 forces non-vacuity; P-06 / P-07 are vertex / commitment-related and live in Memo 02).

---

## 5. Integration of VQ1 and VQ2 into R-5 completion

### 5.1 Joint closure mechanism

R-5 asks: what is the structural status of τ_g as vacuum vs. particle?

- **R-5 partial** (Q.7) closed the *particle-side*: a τ_g excitation lifts via the Q.7 second-quantisation structure with a definite lightlike worldline (R-1) and vertex-anchored commitment ledger (R-3 Q.7-side).
- **VQ1** now closes the *vacuum-side structural form*: the no-excitation sector carries a gauge-invariant, UV-finite, V1-form, stationary fluctuation envelope (the τ_g vacuum kernel).
- **VQ2** classifies the admissible vacuum states (background / excitation / mixed) and identifies the minimal class as the excitation-vacuum (the structural analog of the Fock vacuum at the τ_g sector).

Together VQ1 + VQ2 supply the *form-level* answer to R-5 completion: τ_g has a definite structural status in both the no-excitation and excitation regimes, with a consistent V1 kernel form spanning both, gauge-quotient-respecting, UV-finite, and stationary in the minimal branch.

### 5.2 Minimal structural form of vacuum-level observables

A vacuum-level observable for τ_g is a gauge-invariant functional of the τ_g configuration evaluated in a vacuum-class state. The minimal structural form is:

- **Two-point structural correlators** of gauge-invariant scalars built from τ_g, evaluated at vacuum, with kernel given by the V1 vacuum kernel restricted to the τ_g sector.
- **Higher-point correlators** built additively over independent sectors (P-04) and gauge-quotient-respecting (R-2 / P-10).

This is the form-level analog of a "vacuum two-point function" without committing to any specific QFT vacuum prescription.

### 5.3 What remains for VQ3 + VQ4 (Memo 02)

- **VQ3 (R-3 Q.8-side, vacuum-level commitment).** Does the vacuum *commit*? If yes, in what mode? VQ1 + VQ2 do not by themselves resolve this — they fix the form of the vacuum content and its classification, but commitment is a separate structural axis (per the Q.3 closure pattern). Memo 02 derives this from R-3 (Q.3 + Q.7) discipline + P-06 + P-07.
- **VQ4 (gauge-quotient consistency at vacuum, full audit).** Memo 01 has performed a *partial* VQ4 audit (Constraint 4 of §2; gauge-invariance baked into VQ2 criteria). Memo 02 completes the audit by checking that the vacuum-level commitment rule (VQ3) also respects gauge-quotient identification.

---

## 6. Falsifier analysis

### 6.1 Per-falsifier dispatch

**VQFal-1 — Zero-point structure incompatible with GRH.**
Test: does the VQ1 minimal form (V1, UV-finite, gauge-invariant, stationary) require any input not derivable from P-02..P-13 + prior verdicts + Theorems 6/7/8/9?
Result: every constraint (1–6) traces to a primitive or an inherited theorem. No new CANDIDATE introduced.
**NOT TRIGGERED.**

**VQFal-2 — Vacuum classification inconsistent with worldline structure.**
Test: does the VQ2 classification break Q.7's worldline structure? Specifically, does the excitation-vacuum class respect the lightlike-worldline support in its degenerate (zero-count) limit?
Result: by construction, the excitation-vacuum is the zero-count sector of the Q.7 second-quantised structure; the worldline support is preserved in its degenerate form. Background-vacuum has no worldline support but is structurally distinct from excitation-vacuum, not in conflict with it. Mixed vacuum inherits both consistently.
**NOT TRIGGERED.**

**VQFal-6 — Theorem 7 (UV-FIN) incompatibility.**
Test: does the VQ1 form admit any UV divergence?
Result: Constraint 2 directly inherits UV-FIN. The V1 finite-width kernel is bounded in mode-frequency by construction (Theorem 8). The τ_g restriction does not increase support (it restricts to a sub-sector of the global kernel).
**NOT TRIGGERED.**

**VQFal-7 — P-11 incompatibility at vacuum level (non-Markovian memory beyond V1).**
Test: does the VQ1 form require a memory kernel beyond V1?
Result: Constraint 3 forces V1 form; the τ_g restriction inherits V1. No non-V1 memory structure is invoked. Per Arc N closure, ED is Markov-*compatible* but not Markov-forcing — V1 is the kernel-level structural form, and the restriction respects this.
**NOT TRIGGERED.**

### 6.2 Cumulative falsifier-status table for VQ1 and VQ2

| Falsifier | Sub-feature | Status |
|---|---|---|
| VQFal-1 | VQ1 | NOT TRIGGERED |
| VQFal-2 | VQ2 | NOT TRIGGERED |
| VQFal-6 | VQ1 | NOT TRIGGERED |
| VQFal-7 | VQ1 | NOT TRIGGERED |
| VQFal-3 | VQ3 | DEFERRED to Memo 02 |
| VQFal-4 | VQ5 | DEFERRED to Memo 03 |
| VQFal-5 | VQ4 | DEFERRED to Memo 02 |

---

## 7. Provisional verdicts for VQ1 and VQ2

### VQ1 — Zero-point structure for τ_g

**Verdict: CANDIDATE-FORCED.**

**Justification.**
- Primitive-level audit: 5 primitives constrain the form; 2 are neutral/supportive; none forbid.
- Inheritance: GRH-1 through GRH-4 + Theorems 7, 8 + R-1 + R-2 + R-5-partial all consistent and load-bearing.
- All four load-bearing falsifiers (VQFal-1, VQFal-2, VQFal-6, VQFal-7) NOT TRIGGERED.
- Form is FORCED at the substage level; final unconditional promotion deferred to Arc Q synthesis (per discipline; matches Q.7 verdict cadence).

### VQ2 — Vacuum classification

**Verdict: CANDIDATE-FORCED.**

**Justification.**
- Three admissible classes (background / excitation / mixed) derived structurally from two orthogonal axes (background expectation × worldline support).
- Excitation-vacuum is the minimal FORCED class; background and mixed are FORCED-admissible (their existence depends on a value-layer choice but their *form* is FORCED).
- Compatible with Q.7 worldline structure, R-2 gauge-quotient discipline, and P-13 time-translation closure.
- VQFal-2 NOT TRIGGERED.
- Final unconditional promotion deferred to Arc Q synthesis.

---

## 8. Implications for R-5 and downstream refinements

### 8.1 R-5 closure status

After this memo, **R-5 is form-level CLOSED at Q.8** for the vacuum-side, conditional on:
- VQ3 closure (Memo 02): vacuum-level commitment rule must not retroactively break VQ1 or VQ2.
- VQ4 closure (Memo 02): full gauge-quotient audit must not retroactively break VQ1 or VQ2.

If both Memo-02 sub-features close consistently, R-5 completion is CLOSED CANDIDATE-FORCED at the end of Q.8 substage.

### 8.2 Remaining for Q.8 Memo 02

- **VQ3.** Derive vacuum-level commitment rule from R-3 (Q.3 + Q.7) + P-06 + P-07. Likely outcome (anticipated, not derived here): vacuum is **non-committing** (commitment lives strictly at vertex-anchored excitations), which is the minimal-CANDIDATE branch consistent with Q.3 + Q.7 discipline.
- **VQ4.** Complete gauge-quotient audit by checking that VQ3 commitment rule respects R-2.

### 8.3 Deferred to Arc Q synthesis

- Promotion of GRH from CANDIDATE-FORCED-across-substages to FORCED-unconditional.
- Theorem 17 statement.
- Integration of vacuum-level structural form with the global GRH commitment ledger.

---

## 9. Honest scope limits

Memo 01 cannot resolve:
- **Vacuum-level commitment** (VQ3, Memo 02).
- **Full gauge-quotient audit** (VQ4, Memo 02; Memo 01 only performed a partial audit on VQ1 + VQ2).
- **Numerical vacuum kernel parameters** (value layer, INHERITED from Arc N V1 kernel).
- **Cosmological-constant magnitude** (Arc N + Phase-3 GR; only the Λ-as-V1-integral *form* is structurally available, and lives in Arc N).
- **SM-specific vacuum content** (Higgs VEV, condensates) — forbidden inputs per Q.8 Memo 00 §5.
- **Vacuum-stability questions** (false-vacuum decay etc.) — out of structural scope.

Must be deferred to:
- **Q.8 Memo 02:** VQ3 + VQ4.
- **Q.8 Memo 03:** substage verdict + downstream dependency map for Arc Q synthesis.
- **Arc Q synthesis:** Theorem 17, GRH FORCED-unconditional promotion.
- **Arc M cascade:** F-M8 promotion.

---

## 10. One-line summary

**The no-excitation sector of τ_g carries a gauge-invariant, UV-finite, V1-form, stationary fluctuation envelope (VQ1) admitting three structural vacuum classes — background, excitation, mixed — with the excitation-vacuum as the minimal FORCED class (VQ2); together VQ1 + VQ2 close R-5 completion at the form level, conditional on VQ3 + VQ4 in Memo 02.**

---

## Recommended Next Steps

1. **Begin Q.8 Memo 02** — Derive VQ3 (vacuum-level commitment, R-3 Q.8-side) and complete VQ4 (gauge-quotient consistency audit at vacuum); dispatch VQFal-3, VQFal-5.
2. **Stage Q.8 Memo 03** — Substage verdict + downstream dependency map for Arc Q synthesis; final dispatch of VQFal-4; refinement-closure-map → 7/7 CLOSED.
3. **Open Arc Q synthesis Memo 00** — Once Q.8 closes, scope the synthesis memo that promotes GRH to FORCED-unconditional (anticipated Theorem 17).
4. **Stage Arc M cascade memo (F-M8 promotion)** — Once Theorem 17 is in inventory.
5. **(Optional) Update the Sixteen-Theorems SVG catalogue** to mark Theorem 17 (anticipated FORCED-unconditional GRH) as imminent, with placeholder slot.
