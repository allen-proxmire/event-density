# Structurally FORCED Non-Markovian Structures

**Arc N Stage N.2 — FORCED Evaluation Memo**
**Status:** Evaluation memo. Headline verdict: **V1 (finite-width vacuum memory kernel) is FORCED at primitive level by UV-FIN + Primitive 01 + 13 jointly.** Three secondary items (N1-E, N2-E, N3-D) are FORCED-conditional-on-V1 via the vacuum-coupling channel — the vacuum-coupled bandwidth, commitment, and adjacency mechanisms inherit FORCED status when the underlying vacuum-response kernel is forced. The remaining 16 catalogue items are NOT FORCED at Stage N.2 — they are ADMISSIBLE-NOT-FORCED, with REFUTED determinations deferred to Stage N.3. Total Stage N.2 outcome: **1 unconditionally FORCED + 3 FORCED-conditional + 16 NOT-FORCED.**

---

## 1. Evaluation Frame

### 1.1 Definition of FORCED

A non-Markovian structure is FORCED at primitive level iff *all three* conditions hold:

(a) **Consistency:** the structure is consistent with ED primitives 01–13 + Phase-2 structural theorems (spin-statistics R.2.5, GRH unconditional Q.1, UV-FIN Q.8 — see [1, 2]).

(b) **Necessity:** at least one of the following is true:
  - A primitive constraint *requires* the structure to be present (primitive-level forcing).
  - Removing the structure leads to inconsistency with a Phase-2 theorem (theorem-level forcing).
  - The structure is the unique solution to a structural requirement; no alternative exists (uniqueness forcing).

(c) **Constraint compliance:** the structure satisfies C1 (Lorentz covariance), C2 (spin-statistics preservation), and C3 (UV-FIN preservation).

A structure that satisfies (a) and (c) but not (b) is **ADMISSIBLE-NOT-FORCED**: it is consistent and constraint-compliant but not structurally required. Most catalogue items are expected to land in this category.

### 1.2 Definition of NOT FORCED (deferred)

A structure is NOT FORCED at Stage N.2 if any of:

- **Alternatives exist:** structurally admissible alternatives to the proposed structure exist; the structure is not unique. (Lands in ADMISSIBLE-NOT-FORCED.)
- **Required only conditionally:** the structure is required only conditional on a CANDIDATE that is itself not FORCED. (Lands in FORCED-CONDITIONAL.)
- **Constraint violation:** the structure violates C1, C2, or C3 in some sub-case. (Refers to Stage N.3 for REFUTED determination; the constraint-violating sub-case is REFUTED while admissible sub-cases may remain ADMISSIBLE-NOT-FORCED.)

Stage N.2 records the FORCED determinations only. REFUTED determinations and refined ADMISSIBLE-NOT-FORCED classifications are Stage N.3 deliverables.

### 1.3 Expected outcome distribution

Per the Arc N opening memo [3] §8.3 prior:

- 1–3 items FORCED, concentrated in the V-sector.
- 17–19 items ADMISSIBLE-NOT-FORCED (some of which will be partially REFUTED at Stage N.3).
- V1 is the leading FORCED candidate.

This memo confirms the prior: **1 unconditionally FORCED (V1)** + **3 FORCED-conditional-on-V1 (N1-E, N2-E, N3-D)** = 4 items with FORCED status under varying conditions; 16 remaining items NOT FORCED.

---

## 2. Special Analysis: Vacuum-Response Sector

The V-sector receives detailed analysis because it is the most plausible site for primitively-FORCED non-Markovian content. The argument runs through three sub-claims.

### 2.1 Why a δ-function vacuum response amplifies high-frequency contributions

In the Markovian limit, the effective vacuum's response to a chain perturbation $\delta P_\mathrm{chain}(x'^\mu)$ is instantaneous:
$$
\delta \langle b^\mathrm{env} \rangle_\mathrm{vac}(x^\mu) = K_\mathrm{vac}(x^\mu - x'^\mu) \cdot \delta P_\mathrm{chain}(x'^\mu)
$$
with $K_\mathrm{vac}(x - x') = c_0 \cdot \delta^4(x - x')$. The δ-function response means that a perturbation at any spacetime resolution produces a vacuum response at the same resolution — including arbitrarily fine resolutions.

In Fourier space, $\delta^4(x - x')$ is a constant (independent of frequency $\omega$ or wavenumber $\mathbf{k}$): $\widetilde{K_\mathrm{vac}}(\omega, \mathbf{k}) = c_0$ for all $\omega, \mathbf{k}$. This means the vacuum response carries equal weight at all frequencies, including the deep UV.

In any subsequent loop integral or correlation function involving the vacuum response, this constant frequency-weighting **amplifies high-frequency contributions** — there is no built-in suppression at the UV scale. Naive continuum integrals with δ-function vacuum response produce divergent contributions when integrated over momentum.

### 2.2 Why primitive event-discreteness suggests finite-width structure

Primitive 01 establishes that events are discrete on the event manifold; there is a primitive-level event-discreteness scale $\ell_\mathrm{ED}$ (or equivalently a time scale $\tau_\mathrm{ED}$) below which the manifold structure is not continuum-like. Primitive 13 supplies finite proper-time intervals between commitment events; there is no zero-time-interval limit at primitive level.

These two primitives jointly imply that primitive-level vacuum response has a natural width: the vacuum cannot respond at resolutions finer than the event-discreteness scale because the substrate itself does not admit such resolutions. The vacuum-response kernel must therefore be smoothed at the $\ell_\mathrm{ED}$ scale:
$$
K_\mathrm{vac}(x - x') = K_\mathrm{vac}^\mathrm{prim}((x - x')/\ell_\mathrm{ED}),
$$
with $K_\mathrm{vac}^\mathrm{prim}$ a bounded function that converges to the δ-function only in the formal continuum limit $\ell_\mathrm{ED} \to 0$. At any finite primitive-discreteness scale, the kernel has finite width.

This is structurally identical to the Arc Q.8 argument for UV-FIN [2] §5.2: primitive-level discreteness imposes a natural cutoff that is absent in continuum approximations.

### 2.3 V1 is structurally FORCED

Combining §2.1 and §2.2: a δ-function vacuum response is incompatible with primitive-level event-discreteness; primitive-discreteness forces a finite-width kernel. The Markovian limit corresponds to taking $\ell_\mathrm{ED} \to 0$ (continuum approximation), but at primitive level $\ell_\mathrm{ED}$ is finite, so the kernel is finite-width.

> **V1 (finite-width vacuum memory kernel) is FORCED at primitive level by UV-FIN + Primitive 01 + Primitive 13 jointly.**

This is Stage N.2's headline FORCED result.

### 2.4 Specific functional form is NOT FORCED

V1 forces the *class* of finite-width kernels but does not force a *specific functional form*. V2 (exponential-decay) and V3 (power-law) and V4 (multi-scale) are all admissible specific realisations within the V1 class, distinguished by their decay structure. Stage N.3 will evaluate which specific forms are REFUTED by C3 critical-exponent constraints; Stage N.4 will evaluate cross-arc implications of specific forms.

The **class** is FORCED; the **functional form** is INHERITED.

This parallels Arc M's pattern: the σ_τ master formula's *form* is FORCED via selection criteria SC1–SC6, but the *specific values* of $w_\tau^X$ and $\langle (\partial \ln b)^2 \rangle_\tau$ are INHERITED.

### 2.5 Cascading FORCED status

If V1 is unconditionally FORCED, then any catalogue item whose status depends on the underlying V1 kernel inherits FORCED status conditional on V1. Specifically:

- **N1-E (vacuum-induced bandwidth memory)** — bandwidth-memory kernel inherits structure from the vacuum-response V1 kernel. **FORCED-conditional-on-V1.**
- **N2-E (vacuum-modulated commitment memory)** — commitment dynamics modulated by V1 vacuum response. **FORCED-conditional-on-V1.**
- **N3-D (vacuum-mediated adjacency memory)** — multi-chain adjacency mediated by V1 cross-chain vacuum kernel. **FORCED-conditional-on-V1.**

Since V1 is unconditionally FORCED, the conditional FORCED status of N1-E, N2-E, N3-D is effectively unconditional. However, we record them as "FORCED-conditional" to preserve the conceptual hierarchy: they are forced *because* V1 is forced, not by independent primitive arguments.

---

## 3. Bandwidth-Memory Sector (N1) Evaluation

### 3.1 N1-A — Finite-width memory kernels in $b^\mathrm{env}$

**Evaluation.** N1-A admits memory kernels in the environment-coupled bandwidth band. The Markovian limit (δ-function kernel) is structurally consistent — Phase-2 derivations all use Markovian $b^\mathrm{env}$ — but no primitive *requires* memory in this band beyond what V1 supplies. Apparent need for memory in $b^\mathrm{env}$ is largely subsumed by N1-E (vacuum-induced bandwidth memory).

**Verdict:** **NOT FORCED** (independent of V1). Falls under N1-E if vacuum-coupling is the dominant memory source.

### 3.2 N1-B — History-weighted spectral-rate terms in σ_τ

**Evaluation.** Arc M's σ_τ master formula uses a local proper-time average. Replacing this with a history-weighted average is structurally admissible but not forced — the local average passes Arc M's selection criteria SC1–SC6, and no primitive demands a history-weighted form. The non-local form would modify Arc M's σ_τ structure but is not required for σ_τ stability.

**Verdict:** **NOT FORCED.** Deferred to Stage N.4 cross-arc implications evaluation.

### 3.3 N1-C — Multi-scale bandwidth memory

**Evaluation.** Multi-scale memory structures are admissible structurally — different bands or different chains may carry independent memory timescales. However, no primitive forces multi-scale structure: a single-scale memory is equally admissible. Multi-scale forms are physically motivated (e.g., environment + cosmological timescales) but not primitive-forced.

**Verdict:** **NOT FORCED.**

### 3.4 N1-D — Cross-band memory coupling (incl. P↔R)

**Evaluation.** Cross-band coupling between bands is structurally admissible at primitive level (Primitive 04 admits any inter-band relationship). However, no primitive forces cross-band coupling — bands may evolve independently. Some cross-band sub-cases (specifically Case-P ↔ Case-R coupling) are likely REFUTED at Stage N.3 by C2 spin-statistics preservation; this REFUTED determination is a Stage N.3 task.

**Verdict:** **NOT FORCED.** Sub-cases potentially REFUTED at Stage N.3.

### 3.5 N1-E — Vacuum-induced bandwidth memory

**Evaluation.** N1-E is the bandwidth-memory mechanism induced by vacuum coupling: the chain's $b^\mathrm{env}$ band receives memory content from the underlying V1 vacuum-response kernel. Since V1 is FORCED (§2.3), and bandwidth-coupling to the vacuum is structurally inherent to the effective-vacuum framework (Arc Q.8), N1-E is FORCED conditional on V1.

**Verdict:** **FORCED-CONDITIONAL-ON-V1.** Effectively unconditional since V1 is unconditionally FORCED.

---

## 4. Commitment-Memory Sector (N2) Evaluation

### 4.1 N2-A — Thresholds depending on past event density

**Evaluation.** Density-dependent thresholds are structurally admissible — Primitive 10's individuation threshold could in principle be event-history-dependent. However, no primitive forces this dependence: a constant threshold is equally admissible and is the structurally simpler choice. Phase-2 derivations consistently use density-independent thresholds without inconsistency.

**Verdict:** **NOT FORCED.**

### 4.2 N2-B — Hysteresis-style commitment

**Evaluation.** Hysteresis in individuation is structurally admissible but not required. No primitive demands delayed individuation — Primitive 10's threshold-crossing is naturally instantaneous, and Phase-2 spin-statistics derivation (R.2.5) uses instantaneous individuation. Stage N.3 will likely REFUTE the hysteresis sub-cases that violate spin-statistics at finite memory range.

**Verdict:** **NOT FORCED.** Likely partially REFUTED at N.3.

### 4.3 N2-C — Memory-weighted commitment spacing

**Evaluation.** Memory-weighted commitment spacing (renewal-process-like with kernel) is structurally admissible. However, no primitive forces a specific spacing kernel. Primitive 11 admits any spacing structure consistent with discrete-event content; the standard Poisson-process limit is consistent with primitives.

**Verdict:** **NOT FORCED.**

### 4.4 N2-D — Multi-chain commitment correlations

**Evaluation.** Multi-chain commitment correlations are structurally admissible but largely subsumed by N3-A/B/C (adjacency-memory) and N3-D (vacuum-mediated). The independent N2-D content beyond what N3 captures is small. No primitive forces multi-chain commitment correlations beyond what individuation pairing already supplies (Q.2 R-2 adjacency-equivalence-class construction).

**Verdict:** **NOT FORCED.** Largely subsumed by N3 sector.

### 4.5 N2-E — Vacuum-modulated commitment memory

**Evaluation.** N2-E couples commitment dynamics to V1 vacuum response. Since V1 is FORCED, and commitment events occur in the presence of vacuum content (any chain's commitment necessarily interacts with the local vacuum state per Q.8), N2-E inherits FORCED status conditional on V1.

**Verdict:** **FORCED-CONDITIONAL-ON-V1.**

---

## 5. Adjacency-Memory Sector (N3) Evaluation

### 5.1 N3-A — Time-lagged adjacency graphs

**Evaluation.** Time-lagged adjacency relations are structurally admissible. Primitive 10's adjacency relation is in principle a snapshot at each event; smoothing over a finite memory window is a consistent extension. However, no primitive forces this smoothing — the instantaneous adjacency relation used in Q.2 R-2 closure is structurally consistent.

**Verdict:** **NOT FORCED.**

### 5.2 N3-B — History-dependent adjacency weights

**Evaluation.** History-dependent adjacency-weight content is structurally admissible. However, no primitive forces it — the Q.2 R-2 adjacency-equivalence-class construction works without history-dependent weights.

**Verdict:** **NOT FORCED.**

### 5.3 N3-C — Multi-chain (3+) correlation kernels

**Evaluation.** Higher-order multi-chain correlation kernels are structurally admissible. However, no primitive forces three-or-more-chain temporal correlations beyond the two-chain individuation pairing of Primitive 10. Higher-order content is admissible but not required.

**Verdict:** **NOT FORCED.**

### 5.4 N3-D — Vacuum-mediated adjacency memory

**Evaluation.** N3-D couples adjacency relations to V1 vacuum response. Since V1 is FORCED, and adjacency between chains is structurally affected by the local vacuum state when both chains couple to the same vacuum sector (Q.8 effective vacuum factorisation), N3-D inherits FORCED status conditional on V1.

**Verdict:** **FORCED-CONDITIONAL-ON-V1.**

### 5.5 N3-E — Non-local adjacency propagation

**Evaluation.** Non-local-in-spacetime adjacency propagation is structurally admissible only in restricted Lorentz-covariant forms. C1 likely REFUTES most sub-cases at Stage N.3. No primitive forces non-local propagation beyond what Lorentz-covariant locality already supplies.

**Verdict:** **NOT FORCED.** Most sub-cases expected to be REFUTED at N.3.

---

## 6. Vacuum-Response Sector (V) Evaluation

### 6.1 V1 — Finite-width vacuum memory kernel

**Evaluation.** Per §2: V1 is FORCED at primitive level by UV-FIN + Primitive 01 + Primitive 13 jointly. A δ-function vacuum response is incompatible with primitive event-discreteness; primitive-discreteness forces a finite-width kernel. This is the unique non-Markovian structure that ED *requires* at primitive level.

**Verdict:** **FORCED.** Stage N.2's headline result.

### 6.2 V2 — Exponential-decay vacuum response

**Evaluation.** V2 is a specific functional form within the V1 admissibility class. The exponential decay is the Green's function of a damped field equation and is structurally natural, but it is not the unique admissible form — power-law decay (V3, restricted), multi-scale forms (V4), and other bounded forms are equally admissible.

**Verdict:** **NOT FORCED** (V1 forces the class; V2 is one admissible specific form within it).

### 6.3 V3 — Power-law vacuum response

**Evaluation.** V3 is admissible only for restricted exponent ranges that preserve UV-FIN. For sufficiently steep power-laws, UV-FIN is preserved; for shallow power-laws, UV-FIN is violated. Stage N.3 will determine the critical exponent. V3 is not FORCED — alternative forms (V2, V4) are equally admissible within the V1 class.

**Verdict:** **NOT FORCED** (admissible sub-cases retained; refuted sub-cases at N.3).

### 6.4 V4 — Multi-scale vacuum memory

**Evaluation.** Multi-scale structure is admissible but not forced. A single-scale exponential V2 is consistent with primitives; multi-scale V4 is admissible if multiple physical timescales are present (e.g., event-discreteness + cosmological), but no primitive forces multi-scale structure.

**Verdict:** **NOT FORCED.**

### 6.5 V5 — Vacuum-induced cross-chain correlations

**Evaluation.** V5 is the cross-chain extension of V1: vacuum-mediated correlations between separated chains. Since V1 is FORCED and the effective vacuum couples to all chains in its support (Q.8 multi-rule-type vacuum factorisation), cross-chain correlations are structurally implied — chains in the same vacuum sector necessarily acquire correlated $b^\mathrm{env}$ content.

However, V5 differs from V1 in that V1 only forces the *kernel form* of single-chain vacuum response; V5 makes a stronger claim about cross-chain *correlation amplitude*. The correlation amplitude is INHERITED, not FORCED — it depends on multi-chain couplings to the vacuum sector. The *existence* of cross-chain correlations is FORCED-conditional-on-V1; the *amplitude* is INHERITED.

**Verdict:** **FORCED-CONDITIONAL-ON-V1 in existence-of-correlations sense; values INHERITED.**

We record V5 as FORCED-conditional under the structural-existence criterion (consistent with the "form-FORCED, value-INHERITED" Phase-2 framing).

---

## 7. Summary Table

| ID | Description | FORCED? | Justification | Primitive dependencies | Constraint drivers |
|---|---|---|---|---|---|
| **N1-A** | Finite-width $b^\mathrm{env}$ kernels | NO | Markovian alternative admissible | 04, 11, 13 | C1, C3 |
| **N1-B** | History-weighted σ_τ spectral-rate | NO | Local average passes Arc M SC1–SC6 | 04, 06, 11, 13 | C1, C3 |
| **N1-C** | Multi-scale bandwidth memory | NO | Single-scale structure admissible | 04, 11, 13 | C2, C3 |
| **N1-D** | Cross-band memory coupling | NO | Independent bands admissible; sub-cases REFUTED at N.3 | 04, 07-L1, 11, 13 | C2 (esp. P↔R) |
| **N1-E** | Vacuum-induced bandwidth memory | **FORCED-CONDITIONAL-ON-V1** | Inherits V1 forced kernel structure | 04, 11, 13 + Q.8 | inherits V-sector |
| **N2-A** | Density-dependent thresholds | NO | Constant threshold admissible | 10, 11, 13 | C1, C2 |
| **N2-B** | Hysteresis-style commitment | NO | Instantaneous individuation admissible; REFUTED sub-cases at N.3 | 10, 11, 13 | C2 (tight) |
| **N2-C** | Memory-weighted commitment spacing | NO | Poisson-process limit admissible | 04, 11, 13 | C1, C3 |
| **N2-D** | Multi-chain commitment correlations | NO | Largely subsumed by N3 | 10, 11, 13 | C1, C2, C3 |
| **N2-E** | Vacuum-modulated commitment memory | **FORCED-CONDITIONAL-ON-V1** | Commitment necessarily interacts with vacuum | 10, 11 + Q.8 | inherits V-sector |
| **N3-A** | Time-lagged adjacency graphs | NO | Instantaneous adjacency admissible (Q.2 R-2) | 10, 11, 13 | C1, C2 |
| **N3-B** | History-dependent adjacency weights | NO | Constant weights admissible | 10, 11, 13, 07-L3 | C3 |
| **N3-C** | Multi-chain (3+) correlation kernels | NO | Two-chain pairing sufficient | 10, 11, 13 | C2, C3 |
| **N3-D** | Vacuum-mediated adjacency memory | **FORCED-CONDITIONAL-ON-V1** | Same-vacuum-sector chains acquire correlated $b^\mathrm{env}$ | 10 + Q.8 | inherits V-sector |
| **N3-E** | Non-local adjacency propagation | NO | Mostly REFUTED at N.3 | 02, 10, 11, 13 | C1 (central) |
| **V1** | **Finite-width vacuum memory kernel** | **FORCED** | δ-function response amplifies UV; primitive-discreteness forces width | Q.8, 01, 04, 13 | UV-FIN (C3), Primitive 01 |
| **V2** | Exponential-decay vacuum response | NO | One admissible form within V1 class | Q.8, 13 | none obvious |
| **V3** | Power-law vacuum response | NO | Alternative forms admissible; sub-cases REFUTED at N.3 | Q.8, 13 | C3 (critical exponent) |
| **V4** | Multi-scale vacuum memory | NO | Single-scale admissible | Q.8, 01, 13 | C3 per sub-kernel |
| **V5** | Vacuum-induced cross-chain correlations | **FORCED-CONDITIONAL-ON-V1** (existence); INHERITED (amplitude) | Same-sector chains acquire correlations | Q.8, 04, 10, 13 | C1, C2 |

### 7.1 Final tally

- **1 unconditionally FORCED:** V1.
- **3 FORCED-conditional-on-V1:** N1-E, N2-E, N3-D.
- **1 FORCED-conditional-on-V1 (existence-only):** V5.
- **15 NOT FORCED:** N1-A, N1-B, N1-C, N1-D, N2-A, N2-B, N2-C, N2-D, N3-A, N3-B, N3-C, N3-E, V2, V3, V4.

Total: 4 FORCED (1 unconditional + 3 conditional), 1 partial-FORCED (V5), 15 NOT-FORCED.

---

## 8. Stage N.2 Verdict

### 8.1 Headline result

**V1 (finite-width vacuum memory kernel) is structurally FORCED at primitive level by UV-FIN + Primitive 01 + Primitive 13 jointly.**

This is Stage N.2's headline FORCED result. The structural argument:

(i) A δ-function vacuum response amplifies high-frequency contributions in continuum approximation, threatening UV-FIN.
(ii) Primitive 01 event-discreteness imposes a primitive-level event-resolution scale $\ell_\mathrm{ED}$ below which vacuum response cannot resolve perturbations.
(iii) Primitive 13 supplies finite proper-time intervals between commitment events, providing the second leg of finiteness.

These three jointly force the vacuum-response kernel to be finite-width at primitive level. The **class** of finite-width kernels is FORCED; the **specific functional form** (V2 exponential vs V3 power-law vs V4 multi-scale) is INHERITED.

### 8.2 Cascading FORCED items

V1's unconditional FORCED status cascades to four secondary items via vacuum-coupling channels:

- **N1-E (vacuum-induced bandwidth memory):** FORCED-conditional-on-V1.
- **N2-E (vacuum-modulated commitment memory):** FORCED-conditional-on-V1.
- **N3-D (vacuum-mediated adjacency memory):** FORCED-conditional-on-V1.
- **V5 (vacuum-induced cross-chain correlations):** FORCED-conditional-on-V1 in existence-of-correlations sense; correlation amplitudes INHERITED.

Since V1 is unconditionally FORCED, these conditional FORCED statuses are effectively unconditional, but we retain the conceptual hierarchy: they are FORCED *because* V1 is forced.

### 8.3 NOT FORCED items

The remaining 15 catalogue items are NOT FORCED at Stage N.2. Each is ADMISSIBLE structurally but not required by primitive-level argument. Stage N.3 will evaluate which of these have sub-cases REFUTED by C1/C2/C3 constraints.

### 8.4 Form-FORCED, value-INHERITED preserved

Stage N.2's FORCED determinations preserve the Phase-2 methodological framing established in Arc M [4] and Arc Q [2]:

- **Form-level FORCED:** V1's kernel-class is structurally required; existence of vacuum-induced bandwidth, commitment, adjacency memory is structurally required.
- **Value-level INHERITED:** specific kernel functional form, specific memory timescales, specific correlation amplitudes all inherited from rule-type / chain-initial-condition / cosmological-boundary data.

This is consistent with the Arc N opening expected verdict (40% admissible-bounded / 30% mixed-with-FORCED-element); Stage N.2 lands in the "mixed-with-FORCED-element" quadrant with V1 + cascading items as the FORCED elements.

### 8.5 Comparison with Phase-2 FORCED structural results

V1 takes its place alongside the Phase-2 FORCED theorems as a structural prediction of ED:

| Theorem | Source | Type |
|---|---|---|
| Spin-statistics η = (−1)^{2s} | R.2.5 | Theorem-level structural |
| Cl(3,1) frame uniqueness | R.2.4 | Algebra-level structural |
| Anyon prohibition in 3+1D | R.2.3 | Topology-level structural |
| GRH unconditional FORCED | Q.1+Q.8 | Existence-level structural |
| Canonical (anti-)commutation FORCED | Q.7 | Operator-level structural |
| UV-FIN FORCED | Q.8 | Bound-level structural |
| **V1 forced finite-width vacuum kernel** | **N.2** | **Memory-kernel-level structural** |

V1 is the first **memory-kernel-level structural** prediction of ED — a structurally-forced non-Markovian element distinct in character from the Phase-2 theorems. Its empirical relevance lies in vacuum-response phenomenology, dispersion-relation structure, and cosmological-Λ analysis under UV-FIN reframing.

### 8.6 Defer REFUTED to Stage N.3

Stage N.2 records FORCED determinations only. REFUTED determinations and refined ADMISSIBLE-NOT-FORCED classifications for the 15 NOT-FORCED items are Stage N.3 deliverables. Expected REFUTED targets at N.3 (per N.1 catalogue and Arc N opening):

- **N3-E (non-local adjacency propagation)** — heavily restricted by C1.
- **N2-B (hysteresis-style commitment)** — sub-cases violating spin-statistics REFUTED.
- **N1-D (Case-P↔Case-R cross-band coupling)** — sub-cases violating spin-statistics REFUTED.
- **V3 (power-law vacuum response)** — sub-cases violating UV-FIN REFUTED above critical exponent.

---

## 9. Hand-Off

### 9.1 To Stage N.3 (REFUTED evaluation)

`non_markov_refuted.md`. Will evaluate the 15 NOT-FORCED items + sub-cases of FORCED items against C1/C2/C3 constraints. Expected outcome: 2–5 items partially REFUTED in restricted sub-cases; remainder ADMISSIBLE-NOT-FORCED.

### 9.2 To Stage N.4 (cross-arc implications)

`non_markov_implications.md`. Will evaluate the consequences of FORCED V1 + cascading items for Arc M, Arc Q.5, Arc Q.6, Arc Q.8 closures. Expected back-flow effects:

- **Arc M σ_τ:** N1-E (vacuum-induced bandwidth memory) introduces vacuum-coupled corrections to σ_τ. Form-FORCED, value-INHERITED preserved; Arc M H1-dominant verdict unchanged.
- **Arc Q.5 vacuum polarisation:** V1 + V5 are the structural origin of finite-width photon self-energy. Transversality preserved (gauge invariance); numerical content INHERITED.
- **Arc Q.6 mixing/CP:** N3-D (vacuum-mediated adjacency memory) plus V5 cross-chain correlations may generate additional phase content; specific values INHERITED.
- **Arc Q.8 vacuum factorisation:** unchanged by V1 (V1 is a kernel structure, not a sector-mixing structure).

### 9.3 To Stage N.5 (synthesis)

`arc_n_synthesis.md`. Will integrate N.0 + N.1 + N.2 + N.3 + N.4 into a final Arc N verdict. Expected closure: **non-Markovian structure ADMISSIBLE in restricted sectors with V1 FORCED at primitive level via UV-FIN; cascading FORCED items in vacuum-coupled bandwidth, commitment, and adjacency mechanisms; specific kernel forms INHERITED.**

---

## 10. Cross-References

- Arc N opening: `arc_n_scoping.md` (N.0).
- Catalogue: `non_markov_catalogue.md` (N.1).
- Phase-2 closures: `phase2_synthesis.md`, `arc_q_synthesis.md`, `chain_mass_synthesis.md`.
- Memory-kernel precursor: `memory_kernel_derivation.md`.
- Downstream: `non_markov_refuted.md` (N.3), `non_markov_implications.md` (N.4), `arc_n_synthesis.md` (N.5).

---

## 11. One-Line Summary

**Stage N.2 evaluates the 20 catalogue items and finds V1 (finite-width vacuum memory kernel) FORCED at primitive level by UV-FIN + Primitive 01 + Primitive 13 jointly — a δ-function vacuum response amplifies high-frequency contributions and is incompatible with primitive event-discreteness, so the vacuum-response kernel must have finite width set by the event-discreteness scale; cascading FORCED-conditional status to N1-E (vacuum-induced bandwidth memory), N2-E (vacuum-modulated commitment memory), N3-D (vacuum-mediated adjacency memory), and V5 (vacuum-induced cross-chain correlations) via the V1 vacuum-coupling channel; the remaining 15 catalogue items are NOT FORCED with REFUTED sub-cases deferred to Stage N.3 (N3-E non-local adjacency propagation, N2-B hysteresis, N1-D cross-band P↔R coupling, V3 power-law beyond critical exponent expected REFUTED targets); V1 takes its place as ED's first memory-kernel-level structural prediction alongside Phase-2's spin-statistics, GRH, and UV-FIN FORCED theorems, with form-FORCED / value-INHERITED methodology preserved at the non-Markovian layer.**
