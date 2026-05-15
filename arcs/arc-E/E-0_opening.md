# Arc E — Memo 0: Opening, Scope, and Load-Bearing Decomposition

**Status:** Opening memo of Arc E (Entanglement). Architect-mode active. Form-FORCED / value-INHERITED methodology. No new primitives. Identification-not-derivation discipline for cross-links to closed arcs.

**Date:** 2026-05-08

---

## 1. Structural Summary

The arc's load-bearing question, in ED's own language:

> *Of the mathematical structure that quantum mechanics calls "entanglement," which features are FORCED by ED's primitives, which are CONDITIONAL on auxiliary assumptions, and which are merely inherited mathematical structure once a smaller load-bearing item is settled?*

ED-I-02 (2026-02) provides the conceptual account: entanglement is the persistence of non-individuation — a single undeveloped participation rule expressed at multiple endpoints, until ED-injection forces individuation. This is ontologically clean. It is not yet structural-mathematical at the level the U-arcs, T17, T18, T19, T20, T21, BH-arc, Q-COMPUTE arc operate.

Arc E's job is to take that conceptual account and produce the FORCED / INHERITED / CONDITIONAL classification of the mathematical content — the same treatment given to Born (T10), Schrödinger (U3), Heisenberg (Phase-1), area-law entropy (BH-5), and the multiplicity-cap function (Q-COMPUTE).

**Central load-bearing question:**

> **E1.** Why is the composite-system participation measure carried on $\mathcal{H}_A \otimes \mathcal{H}_B$ (tensor product) rather than $\mathcal{H}_A \oplus \mathcal{H}_B$ (direct sum), $\mathcal{H}_A \times \mathcal{H}_B$ (classical Cartesian product), or any other bilocal construction?

E1 is the gate condition for the arc. Once tensor-product composition is FORCED, the existence of entangled (non-factorizable) states is automatic, Schmidt decomposition is downstream of inner-product + tensor-product, Bell–Tsirelson 2√2 is already in inventory, and the remaining items (E2–E7) reduce to articulation work. If E1 cannot be FORCED at the substrate level, every downstream item degrades to CONDITIONAL.

This memo:

- States the current CANDIDATE formulation of tensor-product composition as it appears implicitly in ED-I-02 + the Phase-1 Bell–Tsirelson derivation.
- Inventories what is already FORCED-unconditional from prior closed arcs.
- Identifies the seven load-bearing-open items (E1–E7) with primitive-level loadings, FORCED/CONDITIONAL/NOT-FORCED criteria, and substrate-level falsifiers.
- Proposes the memo structure E-1 through E-7 with the same discipline used in Arc U2 and Arc Q-COMPUTE.
- Produces the inheritance map showing how Arc E depends on U2, Q-COMPUTE, BH-4, and ED-I-02.

The arc proceeds: E1 first (gate), then E2–E5 in any order once E1 closes, then E6 (entropy form), then E7 (synthesis). E6 and E7 are not written before E1 closes.

---

## 2. Current CANDIDATE Status of Tensor-Product Composition

### 2.1 As it appears in ED-I-02

ED-I-02 says: a high-ED parent system splits into low-ED fragments; the fragments inherit *one* participation rule expressed at multiple endpoints; spatial separation does not develop the rule into two distinct rules; measurement at one endpoint forces individuation, and the other endpoint must complete the same rule complementarily.

What this *implies* mathematically (but does not state):

- The joint description of the two fragments cannot be a Cartesian product of independent single-endpoint descriptions, because in such a product the two endpoints have independent identities, contradicting "single undeveloped rule."
- The joint description cannot be a direct sum, because in a direct sum the global state is *either* in $\mathcal{H}_A$ *or* in $\mathcal{H}_B$, never genuinely bilocal.
- The joint description must support superpositions across joint configurations — i.e., complex-linear combinations of basis vectors $|i\rangle_A \otimes |j\rangle_B$ — to reproduce the perfect correlations that ED-I-02's "complementary completion" mechanism predicts.

ED-I-02 *does not derive* the tensor product. It is consistent with tensor product but does not force it. **Tensor-product composition is therefore currently CANDIDATE in Arc E's ledger** — neither FORCED nor refuted at the substrate level. This is the gap E1 closes.

### 2.2 As it appears in the Phase-1 Bell–Tsirelson derivation

Phase-1's Bell–Tsirelson 2√2 derivation (FORCED-unconditional in inventory) is constructed *given* tensor-product composition: it derives the maximum CHSH violation as a Tsirelson-bound consequence of the inner-product structure on $\mathcal{H}_A \otimes \mathcal{H}_B$. It does not derive the tensor product itself — it inherits it.

This means Phase-1's inheritance ledger has tensor-product composition listed as a structural input that closed-arc work has not yet justified. Arc E's E1 supplies the missing justification (or fails to, in which case Bell–Tsirelson's status is downgraded from FORCED-unconditional to FORCED-conditional-on-tensor-product-composition).

### 2.3 The CANDIDATE statement to be addressed

> **CANDIDATE (E1).** *Given two ED-substrate endpoints $A$ and $B$ that share a single undeveloped participation rule (in the sense of ED-I-02), the joint participation measure on the bilocal endpoint configuration is carried on the tensor product $\mathcal{H}_A \otimes \mathcal{H}_B$ of the single-endpoint Hilbert spaces (in the sense of U2), with the natural induced inner product $\langle \psi_A \otimes \psi_B \,|\, \phi_A \otimes \phi_B\rangle = \langle\psi_A|\phi_A\rangle \langle\psi_B|\phi_B\rangle$ extended bilinearly.*

E-1 (the next memo) closes or refutes this CANDIDATE.

---

## 3. Inventory: What Is Already FORCED-Unconditional

The following items are inputs to Arc E, not deliverables. They will not be re-derived; they are identified by source.

| Item | Source | What Arc E Inherits |
|---|---|---|
| **Inner-product Hilbert-space structure on a single endpoint** | U2 (T11/T12) | $\mathcal{H}_A$ and $\mathcal{H}_B$ each carry inner products as derived structures, not assumptions. |
| **Born rule** | T10 (Born–Gleason via Busch) | Probability rule on single-endpoint measurements is FORCED. Arc E may invoke it on either endpoint. |
| **Bell–Tsirelson 2√2 bound** | Phase-1 closure | Maximal CHSH violation derived *given* tensor-product composition. Arc E inherits this as identification target for the joint-Hilbert-space structure (identification-not-derivation discipline). |
| **V1 kernel cross-chain correlations** | T18 (Arc B closure) | Substrate cross-chain correlations propagate forward-cone-only on the V1 kernel. Load-bearing for E5 (no-signaling) and E3 (Schmidt-form locality). |
| **Cross-chain bandwidth structure** $\Gamma_{\mathrm{cross}}$ | Arc Q-COMPUTE, BH-2, DCGT | Substrate bandwidth between regions takes the form $\Gamma_{\mathrm{cross}} \sim \exp[-\alpha\sigma]$ with $\sigma$ gradient-sparsity. Load-bearing for E4 (monogamy). |
| **Multiplicity $\mathcal{M}$, unresolvedness $\mathcal{U}$, sparsity $\sigma$** | Q-COMPUTE Memo 1, ED-I-01 | The substrate quantities Q-COMPUTE used to characterize the unresolved regime — directly applicable to entanglement, since "single undeveloped participation rule" is the unresolved regime in another language. |
| **BH-4 entanglement straddling** | Arc BH | Information blocking + entanglement straddling at decoupling surfaces. Cross-domain echo for E7; identifies the substrate mechanism by which entanglement persists across substrate boundaries with finite cross-bandwidth. |
| **DCGT (Diffusion Coarse-Graining Theorem)** | Arc D | Substrate-to-continuum bridge. Load-bearing for showing that whatever joint structure is FORCED at the substrate level survives coarse-graining to the continuum-Hilbert-space level. |
| **P11 commitment irreversibility** | Primitives | Load-bearing for E5 (no-signaling sharpened to no-classical-signaling-via-entanglement) and for the measurement-as-forced-individuation account. |
| **ED-I-02 conceptual framing** | Interpretations | "Single undeveloped participation rule expressed at multiple endpoints." Conceptual ground; provides ontological reading of every mathematical object Arc E touches. |
| **ED-I-06 (no fundamental fields)** | Interpretations | Guardrail: Arc E must not introduce a "field of entanglement" or any ontologically primary field-level construct. Entanglement lives at the substrate level, not in a field. |

These eleven anchors are *taken as given*. The arc neither rederives them nor relaxes them.

---

## 4. Load-Bearing Open Questions: E1 Through E7

For each item: (a) the question, (b) which primitives load-bear, (c) FORCED / CONDITIONAL / NOT-FORCED criteria, (d) substrate-level falsifier.

### E1 — Tensor-product composition

(a) **Question.** Is the CANDIDATE in §2.3 FORCED at the substrate level?

(b) **Loads on:** P04 (bandwidth additivity for independent contributions); P09 (independence / U(1) structure on participation phases); U2 (single-endpoint inner product); T18 (cross-chain V1 kernel — establishes that bilocal correlations have a substrate-level bilinear structure).

(c) **Criteria.**
- **FORCED** if a substrate-level argument shows that the joint participation measure of two endpoints sharing one rule must be bilinear in single-endpoint contributions, that bilinearity uniquely determines tensor product as the free bilinear extension of the inner-product structure, and that no non-tensor-product alternative (direct sum, Cartesian product, exotic non-associative product) is consistent with single-endpoint U2.
- **CONDITIONAL** if some piece of the argument is FORCED but tensor-product is uniquely picked only after an auxiliary assumption (e.g., a no-superselection assumption, or a continuity assumption that Arc E does not derive).
- **NOT FORCED** if no substrate-level argument selects tensor product over alternatives, in which case Bell–Tsirelson's status is retroactively downgraded.

(d) **Falsifier.** A substrate construction that satisfies P04 + P09 + U2 + T18 + ED-I-02-style bilocal participation, but produces a non-tensor-product joint Hilbert space. Such a construction would refute tensor-product-as-FORCED.

### E2 — Generic non-factorizability (entangled states are dense in product space)

(a) **Question.** Once tensor product is FORCED, is the existence of non-factorizable (entangled) states automatic, generic (dense), and structurally inevitable rather than contingent?

(b) **Loads on:** E1 (must close first); pure-mathematical density results (free); inner-product structure (U2).

(c) **Criteria.**
- **FORCED** if standard mathematical density results apply to ED's joint Hilbert space without auxiliary assumptions. (Expected outcome: trivially FORCED once E1 closes.)
- **CONDITIONAL** only if the substrate restricts the joint Hilbert space to a sub-manifold of $\mathcal{H}_A \otimes \mathcal{H}_B$ that excludes entangled states.
- **NOT FORCED** if the substrate forces all joint states to be product states, contradicting Bell–Tsirelson and ED-I-02.

(d) **Falsifier.** A substrate-level superselection rule that forbids non-factorizable joint states.

### E3 — Schmidt decomposition (form-FORCED vs. value-INHERITED)

(a) **Question.** Is the Schmidt decomposition $|\psi\rangle_{AB} = \sum_i \sqrt{\lambda_i} |i\rangle_A \otimes |i\rangle_B$ FORCED as a structural feature of every bipartite entangled state, with the Schmidt coefficients $\lambda_i$ INHERITED from inner-product structure on each subsystem?

(b) **Loads on:** E1 (tensor product); U2 (inner products on subsystems); singular-value-decomposition / spectral-theorem mathematics (free).

(c) **Criteria.**
- **FORM-FORCED, VALUE-INHERITED** is the expected pattern: Schmidt decomposition is a theorem of finite-dimensional inner-product algebra; once E1 + U2 are in place, the form is automatic and the values $\{\lambda_i\}$ are determined by the specific state.
- **CONDITIONAL** if some non-trivial substrate constraint affects the existence or uniqueness of the decomposition.

(d) **Falsifier.** A bipartite ED-substrate state that admits no Schmidt decomposition (would contradict E1 + U2).

### E4 — Monogamy from cross-chain bandwidth budgets

(a) **Question.** Is the monogamy of entanglement (the Coffman–Kundu–Wootters inequality $C^2_{AB} + C^2_{AC} \leq C^2_{A(BC)}$ and its qualitative content) FORCED by the cross-chain bandwidth structure $\Gamma_{\mathrm{cross}}$ established in Q-COMPUTE / BH-2 / DCGT?

(b) **Loads on:** E1 (tensor product over three subsystems); $\Gamma_{\mathrm{cross}} \sim \exp[-\alpha\sigma]$ from DCGT/BH-2; substrate bandwidth-additivity (P04 and Q-COMPUTE Memo 1's failure-mode F2).

(c) **Criteria.**
- **FORM-FORCED** if monogamy is FORCED qualitatively (full A–B entanglement precludes additional A–C entanglement) from substrate bandwidth budgets across chain triples.
- **VALUE-INHERITED** is the expected status of the specific CKW coefficient (the "1" on the right-hand side and the squared structure).
- **CONDITIONAL** if substrate bandwidth structure is consistent with monogamy but does not uniquely force it.
- **NOT FORCED** if substrate bandwidth permits unbounded multipartite entanglement, contradicting CKW.

(d) **Falsifier.** A substrate triple-chain configuration that maintains full A–B and full A–C entanglement simultaneously.

### E5 — No-signaling from V1 retardation + locality

(a) **Question.** Is the no-signaling theorem (no faster-than-light classical communication via entanglement-only) FORCED by V1 kernel retardation (T18) + ED locality structure?

(b) **Loads on:** T18 (V1 kernel forward-cone-only); P11 (commitment irreversibility, prevents retroactive update); ED-I-06 substrate-level locality; E1 (tensor-product structure to define partial-trace).

(c) **Criteria.**
- **FORCED** if the partial trace of a measurement-disturbed bipartite state on the un-measured subsystem is independent of the measurement choice — this is the standard no-signaling statement and follows once the substrate respects T18-style forward-cone-only correlations and P11.
- **CONDITIONAL** if a substrate channel (e.g., V5-mediated cross-chain correlation under non-generic conditions) admits backward-cone influence under specific circumstances.
- **NOT FORCED** would refute T18 or P11.

(d) **Falsifier.** A substrate configuration in which Bob's marginal distribution depends on Alice's measurement-basis choice. Equivalent to refuting T18 or P11.

### E6 — Entanglement-entropy form $S = -\mathrm{Tr}(\rho \log \rho)$

(a) **Question.** Is the von Neumann form of entanglement entropy FORCED at the substrate level (form-FORCED, coefficient-INHERITED), in the same way BH-5 establishes area-law form FORCED with coefficient INHERITED?

(b) **Loads on:** Born rule (T10); inner-product (U2); tensor-product (E1); ED-I-01's multiplicity-as-ED-entropy-analogue; thermodynamic counting on ED gradient pathways.

(c) **Criteria.**
- **FORM-FORCED, COEFFICIENT-INHERITED** is the structural target: $S(\rho_A) = -k \cdot \mathrm{Tr}(\rho_A \log \rho_A)$ with the form FORCED by Shannon-Khinchin-style axiomatic counting on ED gradient pathways, and the coefficient $k$ INHERITED from $\hbar$ / $k_B$ / substrate-density-of-states. (Standard Shannon–Khinchin already does most of this work; the substrate-level question is whether the axioms apply at the substrate level.)
- **CONDITIONAL** if the form is FORCED only after assuming continuous additivity on a particular substrate sub-structure.
- **NOT FORCED** if substrate ED-pathway counting leads to a non-Shannon entropy (e.g., Tsallis or Rényi forms) without external selection.

(d) **Falsifier.** An ED-substrate counting that produces a non-Shannon entropy from primitive axioms.

### E7 — Cross-domain synthesis (ER=EPR-class hooks, BH-4, Q-COMPUTE ceilings)

(a) **Question.** Do the closures of E1–E6 produce cross-domain echoes with closed arcs — specifically, an ER=EPR-class structural relation between substrate-level entanglement and BH-4 entanglement-straddling, plus a unification of Q-COMPUTE's cross-chain bandwidth ceiling with E4's monogamy budget?

(b) **Loads on:** all of E1–E6; BH-4; Q-COMPUTE Memo 4 / 5 (architectural classes; multiplicity-cap function).

(c) **Criteria.**
- **STRUCTURAL ECHO ESTABLISHED** if an explicit identity (or close structural correspondence) holds between the BH-4 entanglement-straddling mechanism and the substrate mechanism Arc E identifies for cross-endpoint entanglement.
- **STRUCTURAL ECHO ABSENT** is a valid honest outcome.
- **NOT FORCED** is not an applicable verdict — E7 is synthesis, not derivation.

(d) **Falsifier.** N/A — synthesis content is non-falsifiable by design; what is falsifiable lives in E1–E6.

---

## 5. Memo Structure

| Memo | Title | Status / Disposition |
|---|---|---|
| **E-0** | This opening memo | **Drafted** (this file) |
| **E-1** | Tensor-product composition derived from substrate bilocal participation + bilinearity | Gate; must close before E-2 onward |
| **E-2** | Generic non-factorizability + density of entangled states | Articulation memo, conditional on E-1 |
| **E-3** | Schmidt decomposition: form-FORCED, values-INHERITED | Articulation memo, conditional on E-1 + U2 |
| **E-4** | Monogamy from cross-chain bandwidth budgets | Substantive derivation, loads on Q-COMPUTE/DCGT/BH-2 |
| **E-5** | No-signaling from V1 retardation + P11 + locality | Identification memo, loads on T18 + P11 |
| **E-6** | Entanglement-entropy form FORCED, coefficient INHERITED | Substantive derivation, structural parallel to BH-5 |
| **E-7** | Synthesis: ER=EPR-class echo to BH-4, unification with Q-COMPUTE bandwidth ceiling | Synthesis memo, written last |

**Discipline.**

- **No new primitives.** Arc E will not introduce any substrate-level CANDIDATE that is not already on the active inventory (currently {} as of 2026-04-30 closure tally).
- **Form-FORCED / value-INHERITED separation** explicit in every memo's verdict section.
- **Identification-not-derivation discipline** for the Bell–Tsirelson cross-link in E-1: Phase-1 Bell–Tsirelson is identified as the structural target downstream of E-1, never used as a derivation premise inside E-1.
- **Acyclicity discipline** as in U3 Memo 03 §1.4: each memo opens with a circularity audit confirming it does not depend on any later-numbered memo's content.

---

## 6. Inheritance Map

```
                         ED-I-02 (conceptual ground)
                              │
                              │ [conceptual reading
                              │  of every step]
                              ▼
       U2 ─────────────► Arc E ◄───────── Q-COMPUTE
   (single-endpoint                       (Γ_cross,
    inner product)                         M, U, σ)
       │                  │  │                │
       │                  │  │                │
       ▼                  │  ▼                ▼
   E-3 (Schmidt)          E-1 (tensor)    E-4 (monogamy)
                          │
                          ▼
                      ╔════════╗
                      ║  Gate  ║
                      ╚════════╝
                       │   │   │
        T10 (Born) ────┘   │   └──── BH-4 (straddling)
                           │             │
                           ▼             ▼
                        E-2 (density)  E-7 (synthesis)
                           │
                           │
        T18 (V1 retard) ───┼─► E-5 (no-signaling)
        + P11              │
                           │
        ED-I-01 (multi-    │
        plicity-as-ED-     ├─► E-6 (entropy form)
        entropy)           │
                           │
        Phase-1 Bell ──────┘ [identification target only,
        (Tsirelson 2√2)        not derivation premise]
```

**Arc E is downstream of:** U2 (single-endpoint Hilbert space), T10 (Born), T18 (V1 retardation), P11 (commitment irreversibility), Arc D / DCGT (coarse-graining), Arc BH (BH-4 straddling), Arc Q-COMPUTE (Γ_cross, M, U, σ), ED-I-01 (multiplicity-as-entropy), ED-I-02 (conceptual framing), ED-I-06 (no fundamental fields guardrail).

**Arc E is upstream of:** Phase-1 Bell–Tsirelson's inheritance ledger (E-1 closure retroactively justifies an input previously listed as substrate-input-without-substrate-justification); future arcs that touch multipartite entanglement, GHZ-class correlations, quantum-error-correction substrate accounts (couples with Q-COMPUTE O-QC-5), and any extension of T18 / BH-4 cross-chain machinery.

---

## 7. Verdict-Class Projection

Anticipated verdict structure when Arc E closes (based on inheritance map and analogous arc patterns):

- **E1: Form-FORCED** expected, contingent on bilinearity-from-bilocal-participation argument going through. **CONDITIONAL** is a real possibility if no-superselection or continuity needs to be assumed rather than derived.
- **E2: Trivially FORCED** once E1 closes (mathematical density).
- **E3: Form-FORCED, values-INHERITED** expected (mathematical theorem of inner-product algebra given E1 + U2).
- **E4: Form-FORCED qualitatively, coefficient-INHERITED** expected (parallel to BH-5 area-law).
- **E5: FORCED** expected (loads only on already-FORCED-unconditional T18 + P11).
- **E6: Form-FORCED, coefficient-INHERITED** expected (parallel to BH-5, with Shannon–Khinchin doing standard work).
- **E7: Synthesis** — non-falsifiable; structural-positive expected.

The arc's **load-bearing risk** is concentrated at E1. Every other memo's verdict is contingent on E1, but E1's verdict is contingent only on whether the bilinearity-from-bilocal-participation argument can be made FORCED at the substrate level. If E1 produces only CONDITIONAL, the entire Arc E's verdict structure inherits that conditionality.

---

## 8. What Arc E Is Not

- **Not** a re-derivation of Bell's theorem or Tsirelson's bound; those are FORCED-unconditional in inventory (Phase-1).
- **Not** a re-derivation of measurement / decoherence / mixed-state structure; ED-I-02 §6–§8 supply the conceptual reading, and no closed arc has identified a load-bearing mathematical gap there.
- **Not** an extension of Q-COMPUTE; Q-COMPUTE's three-class architectural decomposition is closed and Arc E only inherits Γ_cross / M / U / σ.
- **Not** a contribution to GR / quantum-gravity / ER=EPR debates beyond the structural-echo level of E7.
- **Not** an experimental-prediction arc; predictive content is downstream of E1's closure and lives in a follow-on (analogous to Q-COMPUTE Memo 6 only if and when E1 + E4 both close).

The deliverable is the FORCED / CONDITIONAL / INHERITED classification of entanglement's mathematical content at the substrate level, with E1 as the gate.

---

## 9. Recommended Next Steps

1. **E-1 (next memo): Derive tensor-product composition from substrate bilocal participation.** Construct the substrate-level argument: (a) bilocal participation rule of two endpoints sharing one rule has a joint participation measure that is bilinear in single-endpoint contributions; (b) bilinearity over the inner-product structure of U2 uniquely picks tensor product as the free bilinear construction; (c) audit alternatives (direct sum, Cartesian product, non-associative products) for substrate-consistency and confirm only tensor product survives. Honest verdict whether the construction is FORCED, CONDITIONAL (and on what), or NOT FORCED. File: `arcs/arc-E/E-1_tensor_product_composition.md`. Estimated 1–2 sessions.

2. **Cross-check audit with Phase-1 Bell–Tsirelson inheritance ledger.** Once E-1 produces a verdict, update Phase-1's structural-foundations-paper inheritance ledger to reflect the new status of tensor-product composition. If FORCED, Bell–Tsirelson's "FORCED-unconditional" status is now genuinely unconditional. If CONDITIONAL, Bell–Tsirelson is downgraded to "FORCED-conditional-on-E1-CONDITIONAL." This is a documentation update, not new derivation work.

3. **(Defer until E-1 closes) Open OQ-E-Bilinear:** is the bilinearity-from-bilocal-participation step itself substrate-FORCED, or is it the kind of step that requires an articulation memo (analogous to ED-I-06 articulating "no fundamental fields") rather than a derivation? Worth flagging now even though we don't act on it until E-1 surfaces it.

---

**Pause for further instruction.**
