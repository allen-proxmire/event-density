# Structurally REFUTED Non-Markovian Structures

**Arc N Stage N.3 — REFUTED Evaluation Memo**
**Status:** Evaluation memo. Headline verdict: **Four primary catalogue items + two sub-cases of FORCED items are structurally REFUTED at primitive level by C1/C2/C3 constraints.** Specifically: N1-D (Case-P↔Case-R cross-band coupling) REFUTED by C2; N2-B (hysteresis-style commitment) REFUTED in Case-R sub-cases by C2; N3-E (non-local adjacency propagation) REFUTED in non-Lorentz-covariant forms by C1; V3 (power-law vacuum response above critical exponent) REFUTED by C3. Sub-cases V1-δ (zero-width limit) REFUTED by C3 and V1-∞ (infinite-width limit) REFUTED by C1 — these clarify the V1 FORCED class is bounded. **Remaining 11 NOT-FORCED items are NOT REFUTED at Stage N.3** — they are ADMISSIBLE-NOT-FORCED, deferred to Stage N.4 cross-arc-implications evaluation. V1 remains unconditionally FORCED with the cascading FORCED-conditional items (N1-E, N2-E, N3-D, V5-existence) unaffected by Stage N.3 refutations. Total Stage N.3 outcome: **4 fully REFUTED + 2 sub-case REFUTED + 11 NOT-REFUTED + 4 FORCED unaffected = 20 catalogue items resolved (with sub-case structure recorded).**

---

## 1. Evaluation Frame

### 1.1 Definition of REFUTED

A non-Markovian structure is REFUTED at primitive level iff it violates at least one of:

(a) **C1 Lorentz covariance:** the structure cannot be expressed as Lorentz-scalar combinations of event-manifold quantities; it picks out a preferred frame or violates Lorentz invariance under boosts.

(b) **C2 Spin-statistics preservation:** the structure violates Arc R Theorem R1's spin-statistics theorem $\eta = (-1)^{2s}$ at finite memory range — e.g., produces apparent η-violations in Case-R sectors at finite memory width.

(c) **C3 UV-FIN preservation:** the structure violates Arc Q Theorem Q3's UV-FIN — e.g., memory kernels with insufficient short-time decay that amplify high-frequency contributions and break primitive-level finiteness.

(d) **Primitive-level inconsistency:** the structure violates a specific primitive (01–13) requirement — e.g., non-local structures violating Primitive 11 commitment-event locality.

(e) **Phase-2 structural theorem violation:** the structure violates a Phase-2 FORCED theorem (R.2.5 spin-statistics, Q.1+Q.8 GRH unconditional, Q.7 canonical (anti-)commutation, Q.8 UV-FIN).

A structure is NOT REFUTED at Stage N.3 if it satisfies all five conditions. REFUTED structures are eliminated from the catalogue's admissibility class; NOT-REFUTED structures pass to Stage N.4 for cross-arc-implications evaluation.

### 1.2 Sub-case structure

Some catalogue items are best evaluated by sub-case: the broad item may admit multiple specific functional forms, some of which are REFUTED while others are admissible. Stage N.3 records sub-case structure where relevant — e.g., V3 power-law vacuum response is REFUTED only above a critical exponent; below the critical exponent, V3 is admissible.

For the FORCED class V1 (finite-width vacuum memory kernel), the FORCED status applies to the class but not to limiting cases. We evaluate V1-δ (zero-width limit) and V1-∞ (infinite-width limit) explicitly — these are sub-cases that bound the V1 admissibility class.

### 1.3 Expected outcome

Per Arc N opening §8.3 and Stage N.2 hand-off:

- **3–5 primary items REFUTED** (concentrated in N1-D, N2-B, N3-E, V3 — flagged in N.1 catalogue).
- **2 sub-cases REFUTED** (V1-δ and V1-∞ — bound the FORCED V1 class).
- Remainder NOT-REFUTED (ADMISSIBLE-NOT-FORCED).

This memo confirms the prior with **4 primary REFUTED + 2 sub-case REFUTED + 11 NOT-REFUTED**.

---

## 2. Primary REFUTED Candidates — Detailed Analysis

The four primary REFUTED candidates flagged in Stage N.1 catalogue and Stage N.2 hand-off receive detailed analysis here. These are the strongest cases for refutation.

### 2.1 N1-D — Cross-band Case-P ↔ Case-R coupling REFUTED by C2

**Catalogue claim (N.1 §2.4).** The memory kernel for one band depends on the history of another band, including potential cross-coupling between Case-P and Case-R sub-sectors of a multi-rule-type system.

**Refutation analysis.** Arc R Theorem R1 (spin-statistics, R.2.5) establishes $\eta = (-1)^{2s}$ at primitive level via the chain: exchange dichotomy → π_1(Q_2) = ℤ_2 → exchange-rotation generator identity → Cl(3,1) frame → MB closure. The exchange sign $\eta$ is a structural property of each rule-type's Lorentz representation content — Case-P rule-types satisfy $\eta = +1$ uniformly; Case-R rule-types satisfy $\eta = -1$ uniformly. There is no structural mechanism for inter-class mixing at the exchange-statistics level.

A cross-band memory kernel between a Case-P band and a Case-R band would, in finite-memory-range applications, produce effective bilinears mixing $\eta = +1$ and $\eta = -1$ content. Specifically, the cross-band kernel $K_{P \leftrightarrow R}(\Delta\tau)$ at finite $\Delta\tau$ would produce contributions to two-chain joint participation that are neither symmetric nor antisymmetric under exchange — violating the dichotomy.

Stage R.2.3's π_1(Q_2) = ℤ_2 theorem is a topological statement: in 3+1D, exchange phases are restricted to {±1}. Memory-kernel-induced "intermediate" phases are not topologically admissible. Therefore cross-band Case-P↔Case-R coupling violates C2.

**Refuted sub-cases.** All cross-band kernels coupling Case-P and Case-R bands of the *same* multi-rule-type system. Cross-band kernels coupling distinct bands of a *single* statistics class (Case-P↔Case-P or Case-R↔Case-R within one rule-type) remain admissible.

**Verdict:** **N1-D in P↔R sub-case REFUTED by C2.** Same-class cross-band coupling within one rule-type's bands remains ADMISSIBLE-NOT-FORCED.

**Constraint violated:** C2 (spin-statistics preservation).

**Primitive dependencies of refutation:** Stage R.2 spin-statistics theorem; Primitive 07 L4 statistics-class structure; Primitive 10 individuation (C2 applied at multi-chain level).

### 2.2 N2-B — Hysteresis-style commitment REFUTED in Case-R sub-cases by C2

**Catalogue claim (N.1 §3.2).** When a chain's bandwidth crosses the individuation threshold from below, individuation does not occur instantaneously; instead, individuation requires the bandwidth to remain above threshold for a finite memory time $\tau_\mathrm{hys}$. Conversely, individuation persists for $\tau_\mathrm{hys}$ after the bandwidth drops below threshold.

**Refutation analysis.** For Case-R rule-types, Primitive 10 individuation enforces vanishing-on-coincidence: two same-type Case-R chains cannot coincide on the event manifold (this is the structural origin of Pauli exclusion at Stage R.2.1). Hysteresis-style commitment introduces a finite delay between bandwidth-threshold-crossing and individuation-event status: during the delay window of width $\tau_\mathrm{hys}$, the chain has crossed the bandwidth threshold but is not yet individuated.

Consider two Case-R chains $K_1, K_2$ both crossing their individuation thresholds within the hysteresis window at the same event-manifold point. Under hysteresis, both chains are in the "delay" state and have not yet established individuation. During this window, the standard Primitive 10 vanishing-on-coincidence does not apply — and two chains can coexist at the same point. This violates Pauli exclusion at the structural level: two same-type Case-R chains *would* coexist within the hysteresis window, contradicting Stage R.2.5's spin-statistics theorem.

Stage R.2.5 establishes $\eta = (-1)^{2s}$ as an *unconditional* primitive-level theorem — it is not a "long-time-average" or "asymptotic" statement. Pauli exclusion holds at every event-manifold point, not only after hysteresis windows close. Therefore hysteresis-style commitment violates C2 in Case-R sub-cases.

**Refuted sub-cases.** Hysteresis applied to Case-R rule-type individuation. Hysteresis applied to Case-P rule-type individuation does not violate spin-statistics (Case-P admits coincidence anyway), and remains structurally admissible.

**Verdict:** **N2-B in Case-R sub-case REFUTED by C2.** Case-P sub-case ADMISSIBLE-NOT-FORCED.

**Constraint violated:** C2 (spin-statistics preservation, specifically Pauli exclusion at every event).

**Primitive dependencies of refutation:** Primitive 10 individuation (vanishing-on-coincidence); Stage R.2.1 Case-R structure; Stage R.2.5 spin-statistics theorem.

### 2.3 N3-E — Non-local adjacency propagation REFUTED in non-Lorentz-covariant forms by C1

**Catalogue claim (N.1 §4.5).** Adjacency information propagates along the event manifold with memory: two chains separated by spacelike intervals can share correlated adjacency content if their lightcones intersect at past events where adjacency was established. Non-local in the sense that adjacency at $x^\mu$ depends on adjacency at points outside $x^\mu$'s strict past lightcone.

**Refutation analysis.** Lorentz covariance (C1) restricts admissible structures to Lorentz-scalar combinations of event-manifold quantities. Non-local-in-spacetime adjacency propagation requires correlations between events $x_1^\mu$ and $x_2^\mu$ that are *not* in causal contact — i.e., spacelike-separated events. For such correlations to be non-trivial, some structural mechanism must connect $x_1^\mu$ to $x_2^\mu$ at the dynamical level.

The candidate mechanisms are:

(i) **Frame-dependent propagation:** correlations between $x_1^\mu$ and $x_2^\mu$ propagate at a definite speed in some preferred frame (e.g., a "rest frame of the universe"). This is REFUTED by C1 — Lorentz covariance forbids preferred frames.

(ii) **Past-lightcone-mediated correlation:** $x_1^\mu$ and $x_2^\mu$ share correlation content because their past lightcones intersect at common ancestor events. This is *not* non-local in the strict sense — it is local correlation propagated forward via causal lightcones, and corresponds to the standard Phase-2 multi-chain content (Bell correlations etc.). Already captured in Phase-1 / Arc R structural content; not a distinct N3-E structure.

(iii) **Topological-shortcut propagation:** correlations propagate via non-trivial event-manifold topology (e.g., wormhole-like structures). This requires structural extensions beyond Primitives 01–13 and is SPECULATIVE.

The N3-E catalogue claim covers (i) explicitly and admits (ii) and (iii) as borderline cases. Sub-case (i) is REFUTED by C1; sub-case (ii) is not genuinely non-local and is structurally subsumed; sub-case (iii) is SPECULATIVE and not admissible at Stage N.3.

**Refuted sub-cases.** Frame-dependent non-local propagation (sub-case i). Sub-case (ii) is not REFUTED but is also not a distinct N3-E structure — it is captured by existing Phase-2 content. Sub-case (iii) is SPECULATIVE.

**Verdict:** **N3-E REFUTED** in primary frame-dependent form. The catalogue item is structurally eliminated; Lorentz-covariant "non-local" sub-cases reduce to existing Phase-2 multi-chain content.

**Constraint violated:** C1 (Lorentz covariance).

**Primitive dependencies of refutation:** Primitive 06 (Lorentz covariance); Primitive 11 (commitment locality); Stage R.1 (Lorentz-covariant participation measure).

### 2.4 V3 — Power-law vacuum response REFUTED above critical exponent by C3

**Catalogue claim (N.1 §5.3).** The vacuum-response kernel has power-law structure
$$
K_\mathrm{vac}(x - x') \propto \frac{1}{(-(x - x')^2)^\alpha},
$$
with exponent $\alpha$ to be determined.

**Refutation analysis.** Arc Q Theorem Q3 (UV-FIN) establishes primitive-level UV finiteness via Primitive 01 + 13 + 04 jointly. A power-law vacuum-response kernel with sufficiently small exponent $\alpha$ is bounded at short timescales and preserves UV-FIN; sufficiently large $\alpha$ produces divergent contributions at $(x - x')^2 \to 0$ and violates UV-FIN.

Specifically, in 4-dimensional spacetime, the integral
$$
\int d^4 z \, |z|^{-2\alpha} \cdot (\text{bounded test function})
$$
converges at small $|z|$ iff $2\alpha < 4$, i.e., $\alpha < 2$. For $\alpha \geq 2$, the integral diverges as $|z| \to 0$ — corresponding to UV divergence in the continuum approximation, threatening UV-FIN.

At primitive level, the divergence does not actually occur because of event-discreteness (Primitive 01 imposes a natural cutoff). However, the *form* of the power-law kernel with $\alpha \geq 2$ produces an effective theory that at scales above the event-discreteness scale would exhibit divergent behaviour, contradicting the Q.8 reframing of UV divergences as continuum-approximation artefacts. The primitive-level kernel must be such that its continuum limit is non-divergent — this requires $\alpha < 2$.

**Refuted sub-cases.** Power-law kernels with $\alpha \geq 2$ in 3+1D. Power-law kernels with $\alpha < 2$ remain admissible (specifically $\alpha < 2$ within the V1 finite-width class).

**Verdict:** **V3 REFUTED for $\alpha \geq 2$.** Sub-cases with $\alpha < 2$ remain ADMISSIBLE-NOT-FORCED within the V1 class.

**Constraint violated:** C3 (UV-FIN).

**Primitive dependencies of refutation:** Primitive 01 (event-discreteness); Primitive 04 (bounded amplitudes); Primitive 13 (finite intervals); Arc Q Theorem Q3.

---

## 3. Sub-Case Refutations of FORCED Items

V1 (finite-width vacuum memory kernel) is FORCED unconditionally per Stage N.2. The FORCED class admits a range of specific functional forms; we identify two limiting sub-cases that are REFUTED to bound the V1 admissibility class.

### 3.1 V1-δ — Zero-width limit REFUTED by C3

**Sub-case statement.** The V1-δ sub-case is the zero-width limit of V1: $K_\mathrm{vac}(x - x') \to c_0 \cdot \delta^4(x - x')$, recovering the Markovian δ-function vacuum response.

**Refutation analysis.** This is exactly the case ruled out by Stage N.2 §2.1: a δ-function vacuum response amplifies high-frequency contributions in continuum approximation, threatening UV-FIN. The zero-width limit is the boundary between V1 (finite-width FORCED) and the Markovian assumption. By the Stage N.2 forcing argument, V1-δ violates C3.

**Verdict:** **V1-δ REFUTED by C3.** This bounds the V1 class from below: vacuum-response kernels must have non-zero width at primitive level.

**Constraint violated:** C3 (UV-FIN).

### 3.2 V1-∞ — Infinite-width limit REFUTED by C1

**Sub-case statement.** The V1-∞ sub-case is the infinite-width limit of V1: $K_\mathrm{vac}(x - x') \to c_\infty$ for all $x - x'$, i.e., the kernel is constant across all separations.

**Refutation analysis.** A constant kernel $K_\mathrm{vac}(x - x') = c_\infty$ for all $x - x'$ does not depend on the separation $x - x'$ at all. While this is trivially Lorentz-scalar (any constant is Lorentz-scalar), the resulting vacuum response makes every event correlated with every other event with equal weight — including events at arbitrary spacelike separations.

This violates Lorentz covariance in a subtle but real way: physical correlations should decay with spacelike separation, not be constant. A constant kernel implies an infinite correlation length, which corresponds to a singular limit of the correlation structure. Such a singular limit is not Lorentz-covariant in the physical sense (it does not respect causal-structure constraints embedded in Lorentz covariance) and is structurally incompatible with primitive-level locality (Primitive 11 commitment events are point-events, not infinitely-extended objects).

More precisely: any structurally consistent finite-width kernel must have *some* decay with separation (exponential, power-law, multi-scale, etc.). Constant kernels with no decay correspond to infinite memory and are structurally pathological — they would mean the vacuum at any event "remembers" perturbations at every other event with equal weight, including events arbitrarily far in the past or future. This is incompatible with C1 in its locality-respecting interpretation.

**Verdict:** **V1-∞ REFUTED by C1.** This bounds the V1 class from above: vacuum-response kernels must have finite (decaying) width, not infinite/constant width.

**Constraint violated:** C1 (Lorentz covariance, in its locality-respecting interpretation).

### 3.3 V1 class is bounded both ways

V1-δ REFUTED at zero-width limit and V1-∞ REFUTED at infinite-width limit jointly establish that V1's admissibility class is **bounded**: kernels must have *finite, non-zero, decaying* width. The exact decay form is INHERITED (V2 exponential, V3 with $\alpha < 2$ power-law, V4 multi-scale all admissible specific realisations within the bounded V1 class).

This is structurally clean: V1 is FORCED, and its admissibility class has well-defined bounds. The bounds are themselves consequences of C1 + C3 constraints — they are not additional postulates but derived restrictions.

---

## 4. Evaluation of Remaining NOT-FORCED Items

Stage N.2 identified 15 NOT-FORCED items. Four (N1-D, N2-B, N3-E, V3) are REFUTED in primary or restricted-sub-case form per §2. The remaining 11 items are evaluated here for REFUTED status.

### 4.1 N1-A — Finite-width memory kernels in $b^\mathrm{env}$ — NOT REFUTED

**Evaluation.** N1-A admits memory kernels in the environment-coupled bandwidth band. Lorentz-scalar finite-width kernels are admissible per C1; bounded kernels preserve C3; no spin-statistics implications per C2. No structural inconsistency identified.

**Verdict:** **NOT REFUTED.** ADMISSIBLE-NOT-FORCED. Largely subsumed by N1-E (vacuum-induced) in practice.

### 4.2 N1-B — History-weighted spectral-rate terms in σ_τ — NOT REFUTED

**Evaluation.** A history-weighted spectral-rate average modifies Arc M's σ_τ master formula. Lorentz-covariant kernels (functions of proper-time difference) preserve C1; bounded kernels preserve C3; no spin-statistics implications since σ_τ is a per-rule-type scalar quantity. The local average is the Markovian choice; non-local extension is admissible.

**Verdict:** **NOT REFUTED.** ADMISSIBLE-NOT-FORCED. Stage N.4 will evaluate cross-arc implications for Arc M.

### 4.3 N1-C — Multi-scale bandwidth memory — NOT REFUTED

**Evaluation.** Multi-scale memory structures are admissible. Each sub-kernel must independently satisfy C1/C3; if all sub-kernels are Lorentz-scalar and bounded, the multi-scale composition is admissible. No constraint violation.

**Verdict:** **NOT REFUTED.** ADMISSIBLE-NOT-FORCED.

### 4.4 N1-D, same-class within-rule-type sub-case — NOT REFUTED

**Evaluation.** While N1-D's Case-P↔Case-R sub-case is REFUTED (§2.1), the same-statistics-class cross-band sub-case (within a single rule-type's bands) is admissible. E.g., a Case-R rule-type's $b^\mathrm{int}$ band can have memory kernel coupled to its own $b^\mathrm{env}$ band; both bands carry the same $\eta = -1$, no spin-statistics violation.

**Verdict:** **NOT REFUTED in same-class sub-case.** ADMISSIBLE-NOT-FORCED.

### 4.5 N2-A — Density-dependent thresholds — NOT REFUTED

**Evaluation.** Threshold-modulation by past event density is admissible if the modulation kernel is Lorentz-scalar (C1) and bounded (C3), and if the modulation does not violate Pauli exclusion in Case-R sectors (C2). For Case-R, density-dependent thresholds *could* in principle delay individuation similarly to N2-B hysteresis, but the modulation here is *quantitative* (threshold value shifts) rather than *qualitative* (delay before individuation occurs). A higher threshold simply means the chain individuates at a higher bandwidth amplitude; coincidence remains forbidden because the chain is not individuated until the bandwidth crosses the (modulated) threshold.

The key distinction: density-dependent thresholds modify *when* individuation occurs (at what bandwidth value); hysteresis modifies *whether* individuation has occurred during a delay window. The former preserves Pauli exclusion structurally; the latter does not.

**Verdict:** **NOT REFUTED.** ADMISSIBLE-NOT-FORCED in both Case-P and Case-R.

### 4.6 N2-B, Case-P sub-case — NOT REFUTED

**Evaluation.** While N2-B in Case-R is REFUTED (§2.2), the Case-P sub-case is admissible. Case-P rule-types admit coincidence (no Pauli exclusion); hysteresis-induced delay in individuation does not violate spin-statistics.

**Verdict:** **NOT REFUTED in Case-P sub-case.** ADMISSIBLE-NOT-FORCED.

### 4.7 N2-C — Memory-weighted commitment spacing — NOT REFUTED

**Evaluation.** Memory-weighted commitment spacing is admissible if the spacing kernel is Lorentz-scalar (C1) and bounded (C3). Spacing kernels do not directly affect spin-statistics; C2 is preserved trivially.

**Verdict:** **NOT REFUTED.** ADMISSIBLE-NOT-FORCED.

### 4.8 N2-D — Multi-chain commitment correlations — NOT REFUTED

**Evaluation.** Multi-chain commitment correlations are admissible if they preserve spin-statistics across all chain pairs (C2), Lorentz covariance (C1), and UV-FIN (C3). Stage R.2.5 spin-statistics applies per chain; N2-D correlations modify *how* chains commit relative to each other, not the per-chain $\eta$ sign. Lorentz-covariant correlations satisfy C1; bounded kernels satisfy C3.

**Verdict:** **NOT REFUTED.** ADMISSIBLE-NOT-FORCED.

### 4.9 N3-A — Time-lagged adjacency graphs — NOT REFUTED

**Evaluation.** Time-lagged adjacency relations modify *when* two chains are deemed adjacent — but the adjacency relation itself remains a per-event-pair instantaneous quantity at each event. Lorentz-covariant smoothing kernels (C1) preserve covariance; bounded kernels preserve C3; spin-statistics applied at each event preserves C2.

**Verdict:** **NOT REFUTED.** ADMISSIBLE-NOT-FORCED.

### 4.10 N3-B — History-dependent adjacency weights — NOT REFUTED

**Evaluation.** Adjacency-weight content with history dependence is admissible. Lorentz-covariant weight kernels (C1), bounded weights (C3), and spin-statistics-respecting weights (C2) are all admissible structurally.

**Verdict:** **NOT REFUTED.** ADMISSIBLE-NOT-FORCED.

### 4.11 N3-C — Multi-chain (3+) correlation kernels — NOT REFUTED

**Evaluation.** Higher-order multi-chain correlation kernels are admissible if they preserve Pauli exclusion across all Case-R chain pairs (C2), Lorentz covariance (C1), and UV-FIN (C3). Higher-order kernels in 3+1D are structurally well-defined and consistent with primitives.

**Verdict:** **NOT REFUTED.** ADMISSIBLE-NOT-FORCED.

### 4.12 V2 — Exponential-decay vacuum response — NOT REFUTED

**Evaluation.** V2 is one specific functional form within the FORCED V1 class. Exponential decay is bounded (C3 satisfied) and Lorentz-scalar in its proper-time-invariant form (C1 satisfied). No spin-statistics implications (C2 satisfied trivially since vacuum response is a per-rule-type scalar).

**Verdict:** **NOT REFUTED.** ADMISSIBLE specific realisation within V1.

### 4.13 V3, $\alpha < 2$ sub-case — NOT REFUTED

**Evaluation.** While V3 with $\alpha \geq 2$ is REFUTED (§2.4), the sub-case $\alpha < 2$ is admissible. Power-law kernels with $\alpha < 2$ are bounded at short timescales (C3 satisfied) and Lorentz-scalar (C1 satisfied).

**Verdict:** **NOT REFUTED in $\alpha < 2$ sub-case.** ADMISSIBLE specific realisation within V1.

### 4.14 V4 — Multi-scale vacuum memory — NOT REFUTED

**Evaluation.** Multi-scale vacuum-response structure is admissible if each sub-scale is admissible per C3. Multi-scale composition does not introduce constraint violations beyond those of the constituent sub-kernels.

**Verdict:** **NOT REFUTED.** ADMISSIBLE specific realisation within V1.

### 4.15 V5, large-amplitude / long-range sub-case — REFUTED partially

**Evaluation.** V5 (vacuum-induced cross-chain correlations) is FORCED-conditional-on-V1 in existence-of-correlations sense (Stage N.2 §6.5). However, the *amplitude* and *range* of cross-chain correlations admit sub-cases — large-amplitude or long-range forms could potentially violate C1 or C3.

- **Large-amplitude V5**: cross-chain correlation amplitudes that violate cluster decomposition (i.e., correlations that do not decay at large separation) are pathological — they would imply infinite correlation length, similar to V1-∞. **REFUTED by C1** in the locality-respecting sense.
- **Long-range V5 with insufficient decay**: power-law correlations with $\alpha \geq 2$ in the cross-chain kernel inherit V3's REFUTATION. **REFUTED by C3.**
- **Bounded-amplitude, finite-range V5**: admissible, satisfies C1 + C3, preserves spin-statistics across chain pairs (C2).

**Verdict:** **V5 large-amplitude / long-range sub-cases REFUTED**; bounded-amplitude finite-range remains FORCED-conditional-on-V1 in existence sense, INHERITED in amplitude/range values.

---

## 5. Summary Table

| ID | Description | REFUTED? | Violated constraint(s) | Primitive dependencies | Notes |
|---|---|---|---|---|---|
| **N1-A** | Finite-width $b^\mathrm{env}$ kernels | NO | — | 04, 11, 13 | ADMISSIBLE-NOT-FORCED |
| **N1-B** | History-weighted σ_τ spectral-rate | NO | — | 04, 06, 11, 13 | ADMISSIBLE; modifies Arc M σ_τ at N.4 |
| **N1-C** | Multi-scale bandwidth memory | NO | — | 04, 11, 13 | ADMISSIBLE |
| **N1-D** | Cross-band memory coupling, P↔R sub-case | **YES** | **C2** | R.2 + 07-L4 + 10 | Same-class sub-case ADMISSIBLE |
| N1-D, same-class sub-case | Same-class cross-band coupling | NO | — | 04, 07-L1, 11 | ADMISSIBLE-NOT-FORCED |
| **N1-E** | Vacuum-induced bandwidth memory | NO | — | 04, 11, 13 + Q.8 | **FORCED-CONDITIONAL-on-V1** (per N.2) |
| **N2-A** | Density-dependent thresholds | NO | — | 10, 11, 13 | ADMISSIBLE; quantitative shift, not qualitative delay |
| **N2-B** | Hysteresis-style commitment, Case-R sub-case | **YES** | **C2** | 10 + R.2.5 | Pauli exclusion violation in delay window |
| N2-B, Case-P sub-case | Hysteresis on Case-P | NO | — | 10, 11, 13 | ADMISSIBLE; coincidence permitted in Case-P |
| **N2-C** | Memory-weighted commitment spacing | NO | — | 04, 11, 13 | ADMISSIBLE |
| **N2-D** | Multi-chain commitment correlations | NO | — | 10, 11, 13 | ADMISSIBLE; per-chain spin-statistics preserved |
| **N2-E** | Vacuum-modulated commitment memory | NO | — | 10, 11 + Q.8 | **FORCED-CONDITIONAL-on-V1** (per N.2) |
| **N3-A** | Time-lagged adjacency graphs | NO | — | 10, 11, 13 | ADMISSIBLE |
| **N3-B** | History-dependent adjacency weights | NO | — | 10, 11, 13 | ADMISSIBLE |
| **N3-C** | Multi-chain (3+) correlation kernels | NO | — | 10, 11, 13 | ADMISSIBLE |
| **N3-D** | Vacuum-mediated adjacency memory | NO | — | 10 + Q.8 | **FORCED-CONDITIONAL-on-V1** (per N.2) |
| **N3-E** | Non-local adjacency propagation | **YES** | **C1** | 06, 11 | Frame-dependent forms violate Lorentz |
| **V1** | Finite-width vacuum memory kernel | NO | — | Q.8, 01, 04, 13 | **FORCED unconditionally** (per N.2) |
| V1-δ sub-case | Zero-width limit | **YES** | **C3** | Q.8, Theorem Q3 | δ-response amplifies UV (per N.2 §2.1) |
| V1-∞ sub-case | Infinite-width limit | **YES** | **C1** | 06, 11 | Constant kernel breaks locality |
| **V2** | Exponential-decay vacuum response | NO | — | Q.8, 13 | ADMISSIBLE within V1 class |
| **V3** | Power-law vacuum response, $\alpha \geq 2$ | **YES** | **C3** | Q.8, Theorem Q3 | $\alpha < 2$ admissible within V1 class |
| V3, $\alpha < 2$ sub-case | Power-law $\alpha < 2$ | NO | — | Q.8, 13 | ADMISSIBLE within V1 class |
| **V4** | Multi-scale vacuum memory | NO | — | Q.8, 01, 13 | ADMISSIBLE within V1 class |
| **V5** | Vacuum-induced cross-chain correlations, large-amp/long-range sub-cases | **YES (partial)** | **C1, C3** | Q.8, Theorem Q3 | Bounded sub-case FORCED-CONDITIONAL (per N.2) |
| V5 bounded sub-case | Finite-amp, finite-range | NO | — | Q.8, 04, 10, 13 | **FORCED-CONDITIONAL-on-V1** existence; values INHERITED |

### 5.1 Final tally

**REFUTED items (at primary or sub-case level):**

- **N1-D in P↔R cross-band sub-case** (C2 violation).
- **N2-B in Case-R sub-case** (C2 violation, Pauli exclusion).
- **N3-E in frame-dependent form** (C1 violation, Lorentz covariance).
- **V3 for $\alpha \geq 2$** (C3 violation, UV-FIN).
- **V1-δ zero-width limit** (C3 violation; bounds V1 class from below).
- **V1-∞ infinite-width limit** (C1 violation; bounds V1 class from above).
- **V5 large-amplitude / long-range sub-cases** (C1/C3 violation).

**Total REFUTED: 4 primary catalogue items (in restricted sub-cases) + 2 V1 limit sub-cases + 1 V5 sub-case = 7 REFUTED determinations.**

**NOT-REFUTED items:** 11 catalogue items (N1-A, N1-B, N1-C, N1-D same-class, N2-A, N2-B Case-P, N2-C, N2-D, N3-A, N3-B, N3-C) + V2, V3 with $\alpha < 2$, V4 + V5 bounded sub-case.

**FORCED items (unaffected by Stage N.3):** V1 (unconditional), N1-E + N2-E + N3-D (FORCED-conditional-on-V1), V5 in existence sense (FORCED-conditional, with value INHERITED).

---

## 6. Stage N.3 Verdict

### 6.1 Headline result

**Four primary catalogue items are REFUTED in restricted sub-cases:**

- **N1-D Case-P↔Case-R cross-band coupling REFUTED by C2** (spin-statistics dichotomy violated at finite memory range).
- **N2-B hysteresis-style commitment REFUTED in Case-R sub-cases by C2** (Pauli exclusion violated in delay window).
- **N3-E non-local adjacency propagation REFUTED in frame-dependent forms by C1** (Lorentz covariance violated).
- **V3 power-law vacuum response REFUTED for $\alpha \geq 2$ by C3** (UV-FIN critical-exponent violation).

**Two V1 limit sub-cases REFUTED, bounding the V1 FORCED class:**

- **V1-δ (zero-width limit) REFUTED by C3.**
- **V1-∞ (infinite-width limit) REFUTED by C1.**

**One V5 sub-case partially REFUTED:**

- **V5 large-amplitude / long-range sub-cases REFUTED by C1/C3.** Bounded-amplitude finite-range form remains FORCED-conditional-on-V1.

### 6.2 NOT REFUTED items (admissible)

**11 NOT-FORCED catalogue items remain ADMISSIBLE-NOT-FORCED** at Stage N.3:

N1-A (finite-width $b^\mathrm{env}$ kernels), N1-B (history-weighted σ_τ spectral-rate), N1-C (multi-scale bandwidth memory), N1-D same-class within-rule-type sub-case, N2-A (density-dependent thresholds), N2-B Case-P sub-case, N2-C (memory-weighted commitment spacing), N2-D (multi-chain commitment correlations), N3-A (time-lagged adjacency graphs), N3-B (history-dependent adjacency weights), N3-C (multi-chain (3+) correlation kernels).

Plus **specific-form sub-cases admissible within V1**: V2 (exponential), V3 with $\alpha < 2$ (restricted power-law), V4 (multi-scale).

These pass Stage N.3 unrefuted and proceed to Stage N.4 cross-arc-implications evaluation.

### 6.3 V1 unconditional FORCED status reaffirmed

The V1 FORCED class is **bounded both ways** by V1-δ and V1-∞ refutations: vacuum-response kernels must have finite, non-zero, decaying width. Specific functional forms (V2, V3 with $\alpha < 2$, V4) are admissible specific realisations within the bounded class. The bounds are themselves consequences of C1 + C3 — they are derived restrictions, not additional postulates.

V1's unconditional FORCED status from Stage N.2 is **reaffirmed**. Cascading FORCED-conditional items (N1-E, N2-E, N3-D, V5-existence) are unaffected by Stage N.3 refutations — those refutations apply to limit sub-cases or specific-form sub-cases, not to the existence-of-mechanism level.

### 6.4 Pattern of refutations

The four primary REFUTED items + two limit-sub-cases + one V5-sub-case all follow the predicted pattern from Arc N opening §6:

- **C1 violations** (Lorentz covariance): N3-E primary (frame-dependence), V1-∞ sub-case (constant kernel breaks locality), V5 large-amplitude sub-case (infinite correlation length).
- **C2 violations** (spin-statistics): N1-D P↔R sub-case (statistics-class mixing), N2-B Case-R sub-case (delay-window coincidence allowed).
- **C3 violations** (UV-FIN): V3 for $\alpha \geq 2$ (high-frequency amplification), V1-δ sub-case (δ-response continuum-divergent), V5 long-range sub-case (insufficient decay).

This confirms the Arc N opening §6 prediction that all three constraints would be active in restricted sub-cases. No new constraint sources have surfaced; the C1/C2/C3 framework is structurally exhaustive at Stage N.3.

### 6.5 Form-FORCED, value-INHERITED preserved

Stage N.3's REFUTED determinations preserve the Phase-2 methodological framing:

- **Form-level structural commitments** (Lorentz covariance, spin-statistics, UV-FIN) restrict admissible forms cleanly.
- **Value-level numerical content** (specific kernel widths, specific exponents, specific amplitudes) remains INHERITED within admissible classes.
- **No primitive-level refutation requires modifying Phase-2 closures** — Stage N.3 refutations are downstream consequences of Phase-2 structural theorems, not contradictions of them.

---

## 7. Hand-Off

### 7.1 To Stage N.4 (cross-arc implications)

`non_markov_implications.md`. Will evaluate the consequences of FORCED V1 + cascading items + ADMISSIBLE-NOT-FORCED non-Markovian structures for Phase-2 closures:

- **Arc M σ_τ:** N1-B (history-weighted spectral-rate) and N1-E (vacuum-induced bandwidth memory) modify σ_τ structure. Form-FORCED preserved; value-INHERITED preserved; Arc M H1-dominant verdict unchanged.
- **Arc Q.5 vacuum polarisation:** V1 + V2 + V3 ($\alpha < 2$) + V4 + V5 bounded supply finite-width photon self-energy. Transversality preserved (gauge invariance). Numerical coefficients INHERITED.
- **Arc Q.6 mixing/CP:** N3-D (vacuum-mediated adjacency) + V5 cross-chain correlations may generate additional phase content. Specific values INHERITED.
- **Arc Q.7 second quantisation:** equal-time canonical (anti-)commutation extends to unequal-time forms with V1 vacuum content. Spin-statistics preservation FORCED at every event (per N2-B Case-R refutation).
- **Arc Q.8 vacuum factorisation:** unchanged structurally. Effective-vacuum content gains memory-kernel structure; factorisation preserved.

### 7.2 To Stage N.5 (synthesis)

`arc_n_synthesis.md`. Will integrate N.0 + N.1 + N.2 + N.3 + N.4 into a final Arc N verdict.

### 7.3 No back-flow to Phase-2 closures

Stage N.3 refutations do not require modification of Phase-2 closures. The REFUTED structures are:
- Limit sub-cases of the V1 FORCED class (V1-δ, V1-∞).
- Sub-cases of catalogue items (N1-D P↔R, N2-B Case-R, N3-E frame-dependent, V3 $\alpha \geq 2$, V5 large-amp/long-range).
- All consistent with Phase-2 structural theorems; the refutations are *consequences* of those theorems, not *contradictions* of them.

Arc N's structural verdict integrates with Phase-2 cleanly.

---

## 8. Cross-References

- Arc N opening: `arc_n_scoping.md` (N.0).
- Catalogue: `non_markov_catalogue.md` (N.1).
- FORCED evaluation: `non_markov_forced.md` (N.2).
- Phase-2 closures: `phase2_synthesis.md`, `arc_q_synthesis.md`, `chain_mass_synthesis.md`, `rule_type_taxonomy_synthesis.md`.
- Downstream: `non_markov_implications.md` (N.4), `arc_n_synthesis.md` (N.5).

---

## 9. One-Line Summary

**Stage N.3 evaluates the 15 NOT-FORCED items + sub-cases of FORCED items against C1/C2/C3 constraints and REFUTES four primary items in restricted sub-cases (N1-D Case-P↔Case-R cross-band coupling by C2 spin-statistics-dichotomy, N2-B hysteresis-style commitment in Case-R by C2 Pauli-exclusion, N3-E non-local adjacency propagation in frame-dependent forms by C1 Lorentz-covariance, V3 power-law vacuum response for $\alpha \geq 2$ by C3 UV-FIN), two V1 limit sub-cases (V1-δ zero-width by C3, V1-∞ infinite-width by C1) bounding the V1 FORCED class, and one V5 sub-case (large-amplitude / long-range cross-chain correlations by C1/C3); 11 catalogue items + V2 + V3 ($\alpha < 2$) + V4 + V5 bounded sub-case remain NOT-REFUTED ADMISSIBLE-NOT-FORCED for hand-off to Stage N.4 cross-arc-implications evaluation; V1 unconditional FORCED status from Stage N.2 reaffirmed and now bounded both ways by V1-δ and V1-∞ refutations, with Phase-2 closures unaffected — all REFUTED structures are downstream consequences of Phase-2 structural theorems rather than contradictions of them.**
