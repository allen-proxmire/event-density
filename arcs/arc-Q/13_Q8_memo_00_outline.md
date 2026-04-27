# Q.8 Memo 00 — Substage Outline: Vacuum and Zero-Point Structure of τ_g

**Arc:** Q (GRH closure trajectory)
**Substage:** Q.8 — Vacuum / zero-point structural classification for the gauge rule-type τ_g
**Memo:** 00 (substage opening / scoping)
**Status on entry:** Q.2 ✅ Q.3 ✅ Q.7 ✅; refinements R-1, R-2 (full), R-3 (Q.3 + Q.7 sides), R-4, R-5 (partial) CLOSED.
**Status on exit of Q.8:** GRH refinement-closure map fully closed; Arc Q synthesis unblocked.

---

## 1. The Q.8 question, restated

**Structural question.** Given that τ_g (the gauge rule-type whose participation measure is the gauge field A_μ) has been:

- assigned a non-Abelian-capable group structure (Q.2 / R-2 / R-4),
- anchored at vertex-level commitment events (Q.3 / R-3 Q.3-side),
- carried along lightlike worldlines with second-quantised excitation lifting (Q.7 / R-1 + R-3 Q.7-side + R-5 partial),

what is **the structural status of τ_g in the absence of an excitation** — i.e., what does the **vacuum sector** of τ_g look like at the primitive level, and how does it commit (or fail to commit) at the vacuum?

**Position in trajectory.** Q.8 sits **after** Q.7 (which fixed the worldline + excitation lifting layer) and **before** Arc Q synthesis (which promotes GRH from CANDIDATE-FORCED across all six Q-substages to **FORCED-unconditional**, anticipated as Theorem 17). Q.8 is the **terminal Q-substage**: it closes the last open refinement (R-5 completion) and the last open commitment-side (R-3 Q.8-side), after which no Q-internal refinement remains outstanding.

**Refinements Q.8 owns.**
- **R-5 completion** — vacuum-vs-particle status of τ_g, specifically the *zero-point structure* (R-5 partial in Q.7 only handled excitation-side; vacuum-side is Q.8's load).
- **R-3 Q.8-side** — final commitment structure at the vacuum level (do vacuum configurations commit? if so, how, and under what gauge-quotient discipline?).

---

## 2. Sub-feature decomposition (VQ1–VQ6)

### VQ1 — Zero-point structure for τ_g (R-5 completion)

**Definition.** The structural classification of τ_g configurations in the no-excitation sector: does τ_g possess a non-trivial structural fluctuation envelope at zero excitation count, and if so, of what type (kernel-bounded / kernel-modulated / kernel-absent)?

**Structural commitment.** A zero-point classification of τ_g in {none, kernel-bounded structural fluctuation, kernel-modulated coherence, mixed} that is FORCED by primitives + prior verdicts.

**Falsifier.** Any consistent zero-point classification that requires a NEW upstream CANDIDATE (e.g., "assume a vacuum normalisation prescription"), or that contradicts UV-FIN (Q.8 verdict from prior Arc Q work) or N-arc V1 vacuum kernel.

**Out of scope.** Numerical magnitude of zero-point energy density; renormalised vacuum energy; cosmological-constant inheritance (lives in Arc N / Phase-3 GR).

### VQ2 — Vacuum classification (background vs excitation vs mixed)

**Definition.** The structural decomposition of τ_g states into (a) background-only configurations, (b) excitation-bearing configurations, (c) mixed configurations, and the rule by which a configuration is assigned to one class.

**Structural commitment.** A primitive-level partition rule of τ_g configurations consistent with Q.7's excitation-lifting structure and with Primitive 13 (continuous-time evolution closure).

**Falsifier.** Any classification that (i) violates gauge-quotient discipline established in R-2, (ii) makes the partition rule depend on Arc M / SM-specific vacuum machinery, or (iii) breaks the worldline structure at vacuum.

**Out of scope.** SM-specific vacuum structure (Higgs VEV, QCD condensates, instanton sectors); thermal-state vacua; environmental decoherence vacua.

### VQ3 — Vacuum-level commitment events (R-3 Q.8-side)

**Definition.** Whether vacuum (no-excitation) configurations of τ_g commit at all, and if so, what counts as a commitment event in the absence of a vertex-anchored excitation.

**Structural commitment.** A binary or graded answer: either (a) vacuum is non-committing (commitment lives strictly at vertex-anchored excitations, Q.3 closure), or (b) vacuum admits a structurally-distinct "vacuum commitment" mode whose form is FORCED by primitives + R-3 Q.3-side + R-3 Q.7-side discipline.

**Falsifier.** Any commitment rule at vacuum that contradicts Q.3's vertex-anchored R-3 closure, or that introduces a new commitment primitive not derivable from P-06 / P-07 / P-13 + prior Q-substage verdicts.

**Out of scope.** Measurement-induced vacuum projection; observer-dependent vacuum commitment; cosmological "decoherence at vacuum."

### VQ4 — Gauge-quotient consistency at vacuum level

**Definition.** Verification that the vacuum sector of τ_g respects the gauge-quotient individuation established in R-2 (Q.2 closure): vacuum configurations related by gauge transformations must be identified.

**Structural commitment.** A demonstration that the VQ1 + VQ2 + VQ3 commitments are gauge-quotient-respecting (no fixed-gauge artefact survives into the vacuum classification).

**Falsifier.** A vacuum classification or commitment rule that distinguishes gauge-equivalent vacuum configurations (would refute R-2 retroactively).

**Out of scope.** Gribov ambiguity at the vacuum (non-perturbative gauge-fixing pathology); BRST machinery (path-integral / Faddeev-Popov vacuum constructions are forbidden inputs — see §5).

### VQ5 — Downstream constraints for Arc Q synthesis

**Definition.** The catalogue of structural constraints Q.8's verdict imposes on Arc Q synthesis, including: (a) which GRH refinement items are now closed, (b) which Arc M items are unblocked for cascade (notably F-M8), (c) what form the anticipated FORCED-unconditional GRH theorem must take.

**Structural commitment.** A complete downstream dependency map covering all six Q-substages → Arc Q synthesis → Arc M cascade.

**Falsifier.** Any downstream commitment that requires a Q-substage to be re-opened, or that introduces a circular dependency on Arc Q synthesis itself (see VQFal-4 below).

**Out of scope.** Empirical predictions; specific Λ value; specific running-coupling values.

### VQ6 — Bookkeeping

**Definition.** Falsifier dispatch log, primitive-load tally, acyclicity audit, refinement-closure-map update, memo-record cross-references.

**Structural commitment.** A clean ledger that survives external review without ambiguity.

**Falsifier.** Inconsistency between memo claims and the global refinement-closure map.

**Out of scope.** Style / formatting choices.

---

## 3. Refinement mapping

| Refinement | Q.8 sub-feature(s) | Closure target |
|---|---|---|
| **R-5 completion** (vacuum / zero-point) | **VQ1 + VQ2** | CLOSED at end of Q.8 |
| **R-3 Q.8-side** (vacuum-level commitment) | **VQ3** | CLOSED at end of Q.8 |
| R-2 (gauge-quotient discipline at vacuum) | VQ4 (consistency check) | Already CLOSED in Q.2; VQ4 verifies no retroactive break |
| Arc Q synthesis preparation | VQ5 | Map only; closure lives in Arc Q synthesis |

**Load-bearing for GRH-3 (the anticipated FORCED-unconditional GRH theorem):** VQ1, VQ2, VQ3 are all load-bearing. VQ4 is a consistency audit (necessary but not generative). VQ5 is a hand-off.

---

## 4. Structural inputs (allowed)

### ED primitives
- **P-02** (rule-types as structural carriers) — commits τ_g to having a vacuum sector at all (no excitation ≠ no rule-type); does NOT commit to its zero-point form.
- **P-04** (bandwidth additivity) — commits vacuum bandwidth to additive composition under independent rule-type sectors; does NOT commit to non-zero vacuum bandwidth.
- **P-06** (commitment events) — commits commitment-event ontology; does NOT commit to vacuum-level commitments existing.
- **P-07** (vertex anchoring) — commits commitments to vertex anchors when excitations are present; does NOT commit to vacuum-vertex structure.
- **P-10** (gauge-quotient identification) — commits vacuum gauge-equivalent configurations to identification; does NOT commit to vacuum being non-trivial.
- **P-11** (UV-FIN) — commits vacuum sector to UV-finite structural fluctuation envelope; does NOT commit to its magnitude.
- **P-13** (continuous-time evolution closure) — commits vacuum sector to closure under time evolution; does NOT commit to time-translation-invariant vacua being unique.

### Prior FORCED theorems (1–16)
- Theorems 1–9 (Phase-1 + R/M/Q form-level + N-arc V1 + Phase-3 GR1): all available as upstream structural commitments. Most directly load-bearing: **#5 (GRH unconditional, Q.1 + Q.8 form-level)**, **#7 (UV-FIN, Q.8)**, **#8 (V1 finite-width vacuum kernel)**.
- Theorems 10–16 (Phase-1 QM-emergence): available as upstream; primarily relevant via Stone-theorem-style commitments to time-translation generators on the vacuum sector.

### Q.2 + Q.3 + Q.7 substage verdicts
- **Q.2 verdict:** non-Abelian gauge-group capability + R-4 closure. Q.8 inherits the group-structure scaffold.
- **Q.3 verdict:** vertex-anchored commitment + R-3 Q.3-side. Q.8 inherits the commitment-at-excitation discipline as a baseline against which vacuum-level commitment is measured.
- **Q.7 verdict:** lightlike worldline + R-1 closure + R-3 Q.7-side + R-5 partial (excitation-side). Q.8 inherits the excitation-lifting structure and the partial vacuum-vs-particle treatment.

### GRH refinements
- **R-1, R-2 (full), R-3 (Q.3 + Q.7), R-4, R-5 partial** — all CLOSED. Q.8 may use any of their committed forms; Q.8 may NOT reopen them.

---

## 5. Forbidden inputs (with justification)

| Forbidden input | Justification |
|---|---|
| **Arc M cascade results (F-M8 in particular)** | F-M8 is downstream of Arc Q synthesis. Using it in Q.8 would create circularity: Arc M ← Arc Q ← Q.8 ← Arc M. |
| **Standard Model vacuum specifics** (Higgs VEV, QCD condensates, instanton sectors, θ-vacua) | Empirical / phenomenological inputs; Arc Q discipline is "form FORCED, value INHERITED" — SM vacuum content lives in the value layer, not the form layer. |
| **Empirical couplings or renormalised vacuum energies** | Same as above; introduces value-level content into a form-level memo. |
| **Standard QFT vacuum machinery** (path-integral vacuum prescriptions, Faddeev-Popov ghosts, BRST cohomology, renormalised zero-point energy, dimensional regularisation) | These are constructed within a chosen quantisation scheme. Q.8 must commit at the primitive level; importing a quantisation scheme would smuggle in upstream CANDIDATES (e.g., a measure on field-space) not derived from P-02..P-13. |
| **Cosmological-constant phenomenology** | Λ inheritance lives in Arc N / Phase-3 GR. Q.8 commits only to vacuum *form*; Λ value is downstream. |
| **Thermal / KMS vacua, observer-dependent vacua** | Frame-dependent vacuum content; would break gauge-quotient discipline (VQ4) and would require an additional CANDIDATE about preferred frames. |

---

## 6. Falsifier inventory

### Specialised global falsifiers
- **Fal-1 (acyclicity break)** at vacuum: any Q.8 claim that requires Arc Q synthesis or Arc M results.
- **Fal-3 (new upstream CANDIDATE)** at vacuum: any vacuum classification requiring a new primitive-level assumption.
- **Fal-5 (gauge-quotient break)**: any vacuum classification that distinguishes gauge-equivalent configurations.
- **VFal-2, VFal-7, WFal-3, WFal-7** (commitment / individuation pathologies): inherited from Q.3 + Q.7 falsifier inventories; specialised to vacuum sector.

### Q.8-specific falsifiers
| ID | Condition | Targets | Tested in |
|---|---|---|---|
| **VQFal-1** | Zero-point structure for τ_g requires a vacuum normalisation prescription not derivable from P-02..P-13 + prior verdicts. | VQ1 | Q.8 Memo 01 |
| **VQFal-2** | Vacuum classification (background / excitation / mixed) inconsistent with Q.7's worldline + excitation-lifting structure. | VQ2 | Q.8 Memo 01 |
| **VQFal-3** | Vacuum-level commitment rule contradicts R-3 (Q.3 + Q.7 sides) — e.g., posits a commitment primitive at vacuum not reducible to vertex-anchored commitment + structural extension. | VQ3 | Q.8 Memo 02 |
| **VQFal-4** | Q.8 verdict has a circular dependence on Arc Q synthesis (e.g., assumes the FORCED-unconditional GRH theorem to derive its own closure). | VQ5 | Q.8 Memo 03 (verdict + dispatch) |
| **VQFal-5** | Vacuum classification breaks gauge-quotient identification (R-2 retroactive break). | VQ4 | Q.8 Memo 02 |
| **VQFal-6** | Vacuum sector violates UV-FIN (Theorem 7) or N-arc V1 vacuum kernel (Theorem 8). | VQ1 | Q.8 Memo 01 |
| **VQFal-7** | Vacuum sector requires a non-Markovian memory kernel beyond the V1 finite-width form (would conflict with Theorem 8 + N-arc Markov-compatibility). | VQ1 | Q.8 Memo 01 |

---

## 7. Expected deliverables

For Q.8 to close CANDIDATE-FORCED, the substage must produce:

1. **A structural zero-point classification for τ_g (R-5 completion)** — VQ1.
2. **A vacuum classification (background / excitation / mixed) compatible with GRH and worldline structure** — VQ2.
3. **A vacuum-level commitment rule (R-3 Q.8-side)** that is either (a) "vacuum is non-committing" or (b) a primitive-derivable vacuum commitment mode, with full justification — VQ3.
4. **A gauge-quotient consistency audit at the vacuum** — VQ4.
5. **A downstream dependency map into Arc Q synthesis and Arc M cascade** — VQ5.
6. **A substage verdict** (Memo 03), with falsifier dispatch log and refinement-closure-map update — VQ6.

---

## 8. Dependency graph

```
   Q.2 ─┐
        │
   Q.3 ─┼──> Q.7 ──> Q.8 ──> Arc Q synthesis ──> Theorem 17 (FORCED-unconditional GRH)
        │                                              │
   Q.1 ─┘                                              ↓
   (form-level GRH                              Arc M cascade (F-M8 promotion)
    Theorem 5, prior)
```

| Substage | Refinements closed |
|---|---|
| Q.1 (prior) | GRH form-level (Theorem 5) |
| Q.2 | R-2 (full), R-4 |
| Q.3 | R-3 Q.3-side |
| Q.7 | R-1, R-3 Q.7-side, R-5 partial |
| **Q.8** | **R-3 Q.8-side, R-5 completion** |
| Arc Q synthesis | All refinements integrated → GRH FORCED-unconditional |

**Q.8 → Arc Q synthesis constraints:** Arc Q synthesis must (a) inherit Q.8's vacuum classification verbatim, (b) integrate the vacuum commitment rule into the global GRH commitment ledger, (c) verify no Q-substage requires reopening, (d) issue the FORCED-unconditional verdict only if all six Q-substages are CLOSED CANDIDATE-FORCED with no falsifier triggered.

---

## 9. Honest scope limits

**Q.8 cannot resolve:**
- Numerical vacuum energy density (empirical / value-layer).
- SM vacuum content (Higgs VEV, condensates, instantons).
- Cosmological constant Λ value (lives in Arc N + Phase-3 GR; only the *form* of Λ as a V1-kernel integral is structurally available, and that lives in Arc N).
- Vacuum-stability questions (false-vacuum decay, etc.) — requires renormalised potentials.

**Must be deferred to Arc Q synthesis:**
- Promotion of GRH from CANDIDATE-FORCED-across-substages to FORCED-unconditional (requires global integration).
- Theorem 17 statement (the FORCED-unconditional GRH theorem).

**Must be deferred to Arc M cascade:**
- F-M8 promotion (mass-form item that depends on GRH closure).
- Any τ_g-mediated mass-form refinements.

---

## 10. Recommended next memo

**Q.8 Memo 01 — Zero-point structure + vacuum classification (VQ1 + VQ2 + VQ4 partial).**

Memo 01 should:
- Derive VQ1 (zero-point classification) from P-02 + P-04 + P-11 + Theorem 7 + Theorem 8 + R-5 partial.
- Derive VQ2 (vacuum classification) from Q.7 worldline + excitation-lifting + P-13.
- Perform a partial VQ4 audit on the VQ1 + VQ2 commitments (full VQ4 in Memo 02).
- Dispatch VQFal-1, VQFal-2, VQFal-6, VQFal-7.

**Q.8 Memo 02 — Vacuum-level commitment + gauge-quotient consistency (VQ3 + VQ4 completion).**
**Q.8 Memo 03 — Substage verdict + Arc Q synthesis hand-off (VQ5 + VQ6).**

Anticipated total: **3 substantive memos** (Memo 01, 02, 03), matching Q.7 substage cadence.

---

## 11. One-line summary

**Q.8 fixes the structural status of τ_g in the no-excitation sector and completes the GRH refinement-closure map by deriving (a) the zero-point classification of τ_g from primitives + UV-FIN + V1 vacuum kernel, and (b) the vacuum-level commitment rule from R-3 (Q.3 + Q.7) discipline — after which Arc Q synthesis can promote GRH to FORCED-unconditional.**

---

## Recommended Next Steps

1. **Begin Q.8 Memo 01** — Derive VQ1 (zero-point structure for τ_g) and VQ2 (vacuum classification), dispatching VQFal-1, VQFal-2, VQFal-6, VQFal-7.
2. **Begin Q.8 Memo 02** — Derive VQ3 (vacuum-level commitment, R-3 Q.8-side) and complete VQ4 (gauge-quotient consistency at vacuum), dispatching VQFal-3, VQFal-5.
3. **Begin Q.8 Memo 03** — Issue Q.8 substage verdict, complete VQ5 (downstream dependency map) + VQ6 (bookkeeping), dispatch VQFal-4, update GRH refinement-closure map to 7/7 closed.
4. **Open Arc Q synthesis Memo 00** — Once Q.8 closes, scope the synthesis memo that promotes GRH to FORCED-unconditional (anticipated Theorem 17).
5. **Prepare Arc M cascade memo** — Stage F-M8 promotion as a follow-on once Theorem 17 is in inventory.
