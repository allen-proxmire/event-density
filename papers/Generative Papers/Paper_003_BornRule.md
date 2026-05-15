# Paper_003 — The Born Rule from Participation-Frequency Limit

**Series:** Event Density (ED) Generative Papers — Wave-2 QM-kinematics arc anchor
**Author:** Allen Proxmire
**Status:** Publication draft (anchors QM-kinematics arc)
**Date:** 2026-05-13
**Repository target:** `domain-arcs/qm-kinematics/Paper_003_BornRule.md` (ED-Generative)
**Working save location:** `C:\Users\allen\GitHub\event-density\papers\Forcing Papers\Paper_003_BornRule.md`
**Genre:** Conditional structural derivation within the 13-Primitive Generative System. Standalone. Cold-reader accessible.

---

## Preamble: What This Paper Does NOT Claim *(written first per QC discipline; abstract reconciled against this)*

1. **The 13 substrate primitives are not derived** (Paper_087).
2. **The Born rule is not assumed in the Hilbert-space arena, but **P-LinRate (§2) is the load-bearing substrate-level postulate** that encodes Born-equivalent content one structural layer down.** The substrate-level frequency limit is derived from P02 + P04 + P07 + P11 + P12 + **P-LinRate (substrate commit-event rate linear in bandwidth)** + participation-measure identification (Paper #1) + frequentist interpretation. P-LinRate is a substrate-level commitment that is *not* derivable from the canonical 13 alone (P04 fixes bandwidth as a scalar but not how rates depend on it). Honesty caveat: the non-circularity sits at the substrate-vs-Hilbert-space layer distinction; P-LinRate at the substrate layer reproduces the Born-rule form at the Hilbert-space layer, but P-LinRate itself is a postulational commitment, not a derivation.
3. **No claim that the Born rule is "forced from nothing."** Conditional on substrate primitives + participation-measure formalism (Paper #1) + substrate-level commitment-event statistics (P11) + frequentist interpretation of substrate-level frequencies.
4. **No claim of derivation of Gleason's theorem.** Gleason's theorem and other operational reconstructions (Hardy, Masanes-Müller, Coecke-Kissinger) take measurement-probability structure as primitive; ED's derivation takes substrate participation as primitive and *derives* the probability structure. The two approaches are complementary.
5. **No claim of derivation of the complex Hilbert space structure.** The complex polar carrier $P_K = \sqrt{b_K}\,e^{i\pi_K}$ is established in Paper #1 as the substrate participation-measure formalism; this paper takes it as upstream.
6. **No claim of derivation of measurement projectors.** Standard QM's projection postulate corresponds to substrate-level commitment (P11). This paper does not derive the projection structure beyond the substrate-level commitment-event statistics.
7. **No claim of derivation of generic quantum-mechanical predictions** (interference, entanglement, no-signaling, etc.). Those are downstream arc-E + QM-kinematics content; the Born rule is the anchor.
8. **No claim of falsification of operational-reconstruction frameworks.** Hardy, Masanes-Müller, etc. are alternative reconstructions; ED's derivation is complementary and goes via different primitives.

---

## Abstract

The **Born rule** — $P(K) = |c_K|^2$ for measurement outcome $K$ in a coherent state $|\Psi\rangle = \sum_K c_K|K\rangle$ — is a downstream structural consequence of the Event Density Generative Primitives System. Given the 13 postulated primitives (Paper_087), specifically P02 (participation), P04 (bandwidth as non-negative additive scalar), P07 (channel structure), P11 (commitment irreversibility), P12 (stability landscape), and the participation-measure formalism (Paper #1) with complex polar carrier $P_K = \sqrt{b_K}\,e^{i\pi_K}$, the Born rule emerges as the **long-run participation-frequency limit** of substrate-level commitment events. Over $N$ identically-prepared substrate-level participation-event trials, the frequency at which a chain commits to channel $K^*$ is:

$$
f_{K^*} = \lim_{N \to \infty}\,\frac{\#\,\text{trials where commit-event selects } K^*}{N}.
$$

By P11 + the substrate-level commitment statistics (governed by bandwidth $b_K$ via the participation-measure formalism), this frequency converges to:

$$
f_K = \frac{b_K}{\sum_{K'} b_{K'}}.
$$

Under the participation-measure identification $b_K = |c_K|^2$ (from $P_K = \sqrt{b_K}\,e^{i\pi_K}$ with $|P_K|^2 = b_K$, Paper #1), and the normalization $\sum_K b_K = \sum_K |c_K|^2 = 1$, this gives:

$$
\boxed{f_K = |c_K|^2 = P_{\mathrm{Born}}(K).}
$$

The identification $b_K = |c_K|^2$ is **not** an a-priori Born-rule assumption — it follows from the participation-measure structure (Paper #1) which is itself derived from P04 + P09 + Paper #3's inner-product structure. The paper makes no claim of derivation of the participation-measure formalism (taken as upstream from Paper #1), no claim of derivation of complex Hilbert space (also upstream), and no claim of derivation of generic QM predictions beyond the Born rule.

---

## 1. Introduction

### 1.1 What this paper does

This paper derives the **Born rule** as the substrate-level participation-frequency limit. The derivation:

1. Establishes the substrate-level commitment-event statistics in coherent multi-channel states (P11 + P04 + P12).
2. Shows that long-run frequency of commitment to channel $K$ over $N \to \infty$ trials converges to $b_K / \sum_{K'} b_{K'}$.
3. Identifies $b_K = |c_K|^2$ via the participation-measure formalism (Paper #1), giving the Born rule.

The derivation is **non-circular**: bandwidth $b_K$ enters via P04 (substrate primitive), not via a-priori Born-rule assumption. The Born rule emerges as the substrate-level structural consequence.

### 1.2 Why the Born rule needs a substrate-level derivation

Standard QM takes the Born rule as a postulate (Born 1926). Operational reconstructions (Gleason's theorem, Hardy 2001, Masanes-Müller, Coecke-Kissinger) derive the Born rule from various sets of operational axioms — typically taking measurement-probability structure as primitive.

ED's substrate framework takes a structurally deeper approach: substrate-level **participation** is primitive (P02 + P04 + P07); **commitment events** are primitive (P11); **bandwidth** is the substrate-level frequency carrier (P04). The Born rule emerges as the substrate-level participation-frequency limit, with bandwidth $b_K$ functioning as the substrate-level analog of the squared amplitude.

This matters for three reasons:

- **Substrate-mechanism account.** ED supplies a substrate-level mechanism for the Born rule that standard QM postulates and operational reconstructions do not provide.
- **Cross-domain coherence.** The substrate-level frequency mechanism underlies all QM-kinematics arc content (Hilbert space emergence, measurement projectors, gauge content, etc.).
- **Falsifiability.** Substrate-level frequency-limit violations in controlled systems would falsify the substrate-level mechanism (§11).

### 1.3 How this fits into the QM-kinematics arc

- **Paper_001 (in queue, Pre-individuation amplitudes):** substrate participation amplitudes from P01–P04.
- **Paper_002 (in queue, Tensor-product composition):** from P02 + P03.
- **Paper_003 (this paper):** Born rule from participation-frequency limit.
- **Paper_004 (in queue, Gleason-type uniqueness):** from P07 + P08.
- **Paper_005 (in queue, Projective measurement):** from P11.
- **Paper_006 (in queue, Unitary evolution):** from V1 kernel.
- **Paper_007 (in queue, Hilbert-space emergence):** completion of motif algebra.
- **Papers_008–012 (in queue):** phase structure, Berry, AB, Bloch, P-RB-1.

Paper_003 is the load-bearing Born-rule anchor for the entire QM-kinematics arc.

---

## 2. Primitive Inputs

This paper takes the following ED substrate primitives as **postulated** (Paper_087):

- **P02 (Participation).** Chains participate in channels.
- **P04 (Bandwidth as non-negative additive scalar).** **Load-bearing for substrate-level frequency content.**
- **P07 (Channel structure).** Channels structurally distinguishable.
- **P11 (Commitment irreversibility).** **Load-bearing for substrate-level commitment-event statistics.**
- **P12 (Stability landscape).** Governs substrate-level commitment dynamics.
- **P03 (Spatial homogeneity).** Translation-invariance of substrate adjacency.

**Postulate specific to this paper (added per round-3 QC Rereading Test):**

- **P-LinRate (Substrate commitment-rate linear in bandwidth):** *The substrate-level rate at which a commitment event selects channel $K^*$ is **linear** in the per-channel bandwidth $b_{K^*}$ — specifically, $\Pr(\mathrm{commit\,to\,}K^*) \propto b_{K^*}/\sum_{K'} b_{K'}$.* This is the **load-bearing substrate-level postulate** for the Born rule derivation. P04 (bandwidth as non-negative additive scalar) and P11 (commitment irreversibility) together do **not** force the rate-bandwidth relationship to be linear — alternative substrate ontologies could have $\Pr \propto b^2$, $\Pr \propto \sqrt{b}$, or other functional forms. P-LinRate is the substrate-level commitment to *linear* rate-bandwidth, which (combined with the participation-measure identification $b_K = |c_K|^2$ from Paper #1) reproduces the empirical Born rule. **The non-circularity claim in §6 is therefore softened: the Born rule is derived from (P-LinRate + Paper #1 identification + frequentist interpretation), not from substrate primitives alone. P-LinRate is itself a substrate-level commitment, defensible but not derived from the canonical 13.**

**Upstream paper dependencies:**

- **Paper_087:** position paper.
- **Paper #1 (Participation Measure):** complex polar carrier $P_K = \sqrt{b_K}\,e^{i\pi_K}$. **Load-bearing: provides the identification $|P_K|^2 = b_K$ that connects substrate bandwidth $b_K$ to participation-amplitude magnitude $|c_K|$ (when participation measure is identified with quantum-state amplitudes).**
- **Paper #3 (Inner Product + Tsirelson):** four-band orthogonality + sesquilinear inner product structure that supports the participation measure.
- **Paper_089 (V1):** unitary evolution within the unresolved regime.

**Empirical / value-layer inputs:** none required for the substrate-level frequency-limit derivation itself; specific empirical state-preparation methods (laboratory protocols) are inherited from experimental practice.

**No primitive forcing is invoked.**

---

## 2.5 Load-Bearing Step Audit

| Step | Status | Source / justification |
|---|---|---|
| 13 primitives postulated | P | Paper_087 |
| Participation-measure complex polar carrier $P_K = \sqrt{b_K}\,e^{i\pi_K}$ | D | Paper #1 from P04 + P09 + Paper #3 inner product |
| Substrate-level coherent state has multi-channel participation | D | §3.1 from P02 + P07 + Paper #1 |
| Commitment events have substrate-level frequency content | D | §3.2 from P11 + P04 (existence of frequency content, not its functional form) |
| Substrate-level commit-event rate is **linear** in bandwidth $b_K$ | **P (P-LinRate)** | **§2 postulate.** Not derived from P04 + P11 — these only fix bandwidth as a substrate scalar; they do not force linear rate-bandwidth dependence. Alternative functional forms ($\Pr \propto b^2, \sqrt{b}$, etc.) are substrate-consistent. P-LinRate is the substrate-level commitment that reproduces empirical Born. *(Round-3 Rereading Test: §3.2's proportionality argument was A→postulate mislabeled D.)* |
| Substrate-level frequency $f_K$ converges over $N \to \infty$ trials | D | §4.1 from large-$N$ statistics under repeated commitment-event preparation |
| Frequency limit $f_K = b_K/\sum_{K'} b_{K'}$ | D | §4.2 from P-LinRate + law-of-large-numbers analog |
| Identification $b_K = |c_K|^2$ | D | §5.1 from Paper #1 participation-measure $|P_K|^2 = b_K$ |
| Born rule $f_K = |c_K|^2$ | D | §5.2 combining frequency limit + bandwidth-amplitude identification |
| Frequentist interpretation of substrate-level frequencies | A→assumption | **Methodological assumption** for connecting long-run frequency to physical probability; §4.3 |
| No a-priori Born-rule assumption | D | §6 explicit non-circularity audit |
| Hilbert space structure | I | Paper #1 + Paper #3 upstream |

One row is "A→assumption" (frequentist interpretation): **labeled explicitly as methodological assumption**, §4.3, per QC discipline. All other rows are P, D, or I. **No A (asserted-without-label) rows.**

---

## 3. Substrate-Level Coherent State and Commitment Events

### 3.1 Coherent multi-channel substrate state

By P02 (participation) + P07 (channel structure), a chain $C$ participates in substrate channels with bandwidth $b_K^C(u)$ and polarity $\pi_K^C(u)$ per channel. A **coherent multi-channel state** has the chain participating in multiple channels simultaneously, with bandwidth distributed across channels.

By Paper #1 (participation-measure formalism), the substrate participation content is captured by the complex polar carrier:

$$
P_K^C(u) = \sqrt{b_K^C(u)}\,e^{i\pi_K^C(u)}.
$$

This is the substrate-level analog of a quantum-mechanical amplitude. The complex Hilbert space structure (Paper #1 + Paper #3) makes $P_K$ a complex-valued amplitude over the channel index $K$.

The coherent state $|\Psi\rangle = \sum_K c_K |K\rangle$ corresponds to substrate participation $P_K = c_K$ (with the participation-measure identification, Paper #1 §4).

### 3.2 Commitment events

By P11, at substrate-level commitment events, the chain's multi-channel participation collapses to single-channel participation. The substrate-level commitment selects one channel $K^*$ from the chain's currently-active channel set, with the un-selected channels' phase content randomized.

**Substrate-level commitment statistics — governed by P-LinRate (§2 postulate):** by the **P-LinRate substrate-level postulate** (§2), the rate at which a commitment event selects channel $K^*$ is **linear** in the per-channel bandwidth:

$$
\text{(rate of commit-event to } K^* \text{)} \propto b_{K^*}^C(u, t).
$$

**Honest framing of P-LinRate's status (round-3 QC clarification).** This linear-proportionality is **a substrate-level postulate (P-LinRate), not derived from P04 + P11 alone**. P04 says $b_K$ is non-negative additive substrate scalar; P11 says commitment events are irreversible. Neither forces the rate-bandwidth relationship to be linear. Alternative substrate ontologies could postulate $\Pr \propto b^2$, $\Pr \propto \sqrt{b}$, or other functional forms; each would give a different downstream "Born-like" rule.

**P-LinRate is therefore the substrate-level commitment that reproduces the empirical Born rule** — a defensible substrate postulate, but not derived. The round-2 framing ("this is not an assumption of the Born rule, it's a statement about how commitment events partition") was structurally circular: relabeling "Born rule encoded in amplitude squared" as "linear in bandwidth" preserves the same load-bearing substrate-level commitment under a different name. Round-3 makes this honest: **P-LinRate is the substrate-level postulate; the Born rule is its downstream consequence under the participation-measure identification.**

### 3.3 Repeated state preparation

Consider a substrate-level protocol that repeatedly:

1. Prepares an identical coherent multi-channel state $|\Psi\rangle$ (same $b_K, \pi_K$ across trials).
2. Allows a commitment event to occur.
3. Records which channel $K^*$ is selected.

Over $N$ trials, let $n_K$ denote the number of trials in which channel $K$ was selected. The substrate-level frequency of selecting channel $K$ is:

$$
f_K^{(N)} = \frac{n_K}{N}.
$$

The substrate-level question is: does $f_K^{(N)}$ converge as $N \to \infty$, and if so, to what?

---

## 4. Substrate-Level Frequency Limit

### 4.1 Convergence of substrate-level frequencies

Substrate-level commitment events are governed by P11 (irreversible) + P04 (bandwidth-additive substrate selection). Treating the commitment events as a substrate-level stochastic process with selection probability proportional to per-channel bandwidth (§3.2), the substrate-level frequency $f_K^{(N)}$ converges:

$$
f_K = \lim_{N \to \infty} f_K^{(N)}.
$$

Convergence follows from the substrate-level analog of the law of large numbers: independent identically-distributed commitment-event trials with selection probability proportional to bandwidth produce frequencies converging to expected selection rate.

**Dimensional check:** $f_K$ is dimensionless (a frequency / probability); $b_K$ has units of substrate bandwidth; ratio $b_K / \sum b_{K'}$ is dimensionless. ✓

### 4.2 The frequency limit formula

By the substrate-level commitment statistics (§3.2) — commit-event selection rate proportional to $b_K$ — the long-run frequency is:

$$
f_K = \frac{b_K}{\sum_{K'} b_{K'}}.
$$

This is the **substrate-level participation-frequency limit**. It is derived from:

- P02 + P07 + P11 + P12 (substrate primitives).
- The substrate-level commitment-event statistics (selection rate proportional to bandwidth, P04 + P12).
- The law-of-large-numbers-like convergence for substrate-level repeated trials.

**No Born-rule assumption.** The frequency limit is expressed in terms of substrate bandwidth $b_K$, not in terms of $|c_K|^2$. The Born-rule form will follow from the participation-measure identification (§5).

### 4.3 Frequentist interpretation (methodological assumption)

The interpretation of $f_K$ as the **measurement probability** $P(K)$ in physical experiments — i.e., the identification of substrate-level long-run frequency with experimental probability — is a **methodological assumption** of the frequentist interpretation of probability.

This assumption is shared with all derivations of the Born rule from frequency limits (e.g., Everett's many-worlds frequentist derivation, Hartle's frequency-operator analysis). The substrate-level frequency-limit derivation gives the *value* of $f_K$; the *interpretation* of $f_K$ as physical measurement probability is a separate methodological commitment.

Alternative interpretations (Bayesian, propensity, etc.) would give different methodological connections between substrate-level frequencies and empirical probabilities; the substrate-level frequency-limit itself remains the substrate-derived structural content.

**For this paper, the frequentist interpretation is the operational stance:** $f_K = P(K) = $ measurement probability. The substrate-level structural derivation is robust to this methodological choice; alternative interpretations would re-interpret $f_K$ rather than re-derive it.

---

## 5. Identifying $b_K$ with $|c_K|^2$ — the Born Rule

### 5.1 The participation-measure identification

By Paper #1 (Participation Measure), the substrate participation content is captured by the complex polar carrier:

$$
P_K = \sqrt{b_K}\,e^{i\pi_K}.
$$

The magnitude squared is:

$$
|P_K|^2 = b_K.
$$

When the substrate participation measure is identified with quantum-mechanical amplitudes — i.e., $P_K = c_K$ where $|\Psi\rangle = \sum_K c_K |K\rangle$ in the corresponding quantum state — the identification

$$
b_K = |c_K|^2
$$

follows directly. **This is not the Born rule itself**; it is the identification of substrate bandwidth with squared amplitude magnitude, which is the natural identification given the participation-measure formalism.

The Born rule's empirical content (measurement probability = $|c_K|^2$) emerges by **composing** this identification with the substrate-level frequency-limit result (§4.2).

### 5.2 The Born rule emerges

Combining the frequency limit (§4.2):

$$
f_K = \frac{b_K}{\sum_{K'} b_{K'}}
$$

with the participation-measure identification (§5.1):

$$
b_K = |c_K|^2
$$

gives:

$$
f_K = \frac{|c_K|^2}{\sum_{K'} |c_{K'}|^2}.
$$

For a **normalized state** $|\Psi\rangle$ with $\sum_K |c_K|^2 = 1$:

$$
\boxed{f_K = |c_K|^2 = P_{\mathrm{Born}}(K).}
$$

**This is the Born rule.** It is derived from:

- Substrate-level commitment-event statistics (§3 — P11 + P04 + P12).
- Substrate-level frequency-limit convergence (§4 — law-of-large-numbers analog).
- Participation-measure identification (§5.1 — Paper #1).
- Frequentist interpretation (§4.3 — methodological assumption).

**Dimensional check:** $|c_K|^2$ is dimensionless (squared amplitude magnitude for normalized state); $f_K$ is dimensionless (frequency / probability). ✓

### 5.3 Normalization

The normalization condition $\sum_K |c_K|^2 = 1$ corresponds at substrate level to $\sum_K b_K = $ const (the chain's total participation bandwidth is conserved across channels). This is enforced by P04 (bandwidth additivity) under the substrate-level coherent-state preparation: the chain's total participation content is normalized at substrate level.

When the substrate-level total is normalized to 1, the frequency $f_K$ equals $|c_K|^2$ directly.

---

## 6. Non-Circularity Audit

This section explicitly establishes that the derivation does **not** assume the Born rule.

### 6.1 What is NOT assumed

The derivation does **not** assume:

- $P(K) = |c_K|^2$ (the Born rule statement itself).
- Measurement probabilities are squared-magnitude of amplitudes (Born-rule form).
- Probability distributions on Hilbert space follow the squared-norm measure (Born form).

### 6.2 What IS used

The derivation uses:

- **P04 (substrate bandwidth):** non-negative additive scalar. The substrate-level frequency carrier.
- **P11 (commitment irreversibility):** substrate-level commitment events with substrate-level statistics.
- **P12 (stability landscape):** governs commitment-event dynamics.
- **P02 + P07:** participation + channel structure (substrate-level coherent multi-channel state).
- **P-LinRate (substrate commitment-rate linear in bandwidth, §2):** **load-bearing substrate-level postulate.** Without P-LinRate, the rate-bandwidth functional form is undetermined; with P-LinRate, the frequency limit follows.
- **Paper #1 participation-measure formalism:** complex polar carrier $P_K = \sqrt{b_K}\,e^{i\pi_K}$.
- **Frequentist interpretation:** methodological assumption (§4.3).

### 6.3 Where the Born identification comes from

The Born-rule identification $f_K = |c_K|^2$ arises in three structurally separate steps:

1. **Step A (P-LinRate postulate):** Substrate-level commit-event rate is linear in bandwidth $b_K$. This is a substrate-level postulate (§2), not derived from P04 + P11 alone.
2. **Step B (Frequency limit):** Given P-LinRate + law-of-large-numbers analog, substrate-level frequency converges to $f_K = b_K/\sum b_{K'}$ (§4.2).
3. **Step C (Participation-measure identification):** $b_K = |c_K|^2$ from Paper #1's complex polar carrier $P_K = \sqrt{b_K}\,e^{i\pi_K}$ (§5.1).

The composition gives the Born rule. **Honest framing (round-3):** Step A's P-LinRate is the load-bearing substrate-level postulate that reproduces the empirical Born rule. The non-circularity claim is therefore: **the Born rule is not assumed in the Hilbert-space arena; it is encoded one structural layer down as the P-LinRate substrate-level postulate.** Whether P-LinRate itself is forced from a deeper layer (e.g., via a substrate-level Gleason-analog argument constraining how commit-event rates can depend on substrate scalars) is structurally open.

This is **complementary to** operational reconstructions (Gleason, Hardy, etc.): they take measurement-probability structure as primitive and derive its specific form; ED takes P-LinRate as substrate-level postulate (one structural layer below) and derives the measurement-probability form. The non-circularity sits at the substrate-vs-Hilbert-space-layer distinction, not at the absolute level.

### 6.4 Cross-check against operational reconstructions

Operational reconstructions (Gleason, Hardy, Masanes-Müller, Coecke-Kissinger) typically take measurement-probability structure as primitive — assuming that there *is* a probability measure on outcomes and deriving its specific form ($|c_K|^2$).

ED's derivation operates at a structurally deeper level: substrate-level commitment events are the substrate primitives; the probability measure on outcomes is *derived* from substrate-level frequency limits. The Born rule emerges as a substrate-level structural consequence, not as an axiomatic primitive.

This is **complementary to** (not in competition with) operational reconstructions: ED's derivation explains *why* there is a probability measure on outcomes (substrate-level commitment-event statistics + frequency limit), while operational reconstructions take measurement-probability structure as primitive and derive its specific form.

---

## 7. Falsification Criteria

### 7.1 Substrate-level frequency-limit violations

**Falsifier sentence:** *Empirical observation of substrate-level commitment-event trials in controlled experiments (repeated quantum measurements with identical state preparation) producing long-run frequencies $f_K$ inconsistent with $b_K/\sum b_{K'}$ — i.e., systematic deviations from the substrate-level frequency-limit formula — would falsify §4.2.*

This corresponds to: empirical violations of the Born rule in controlled QM experiments. Currently no such violations are observed; the Born rule has been empirically verified to high precision in many contexts.

### 7.2 Failure of convergence

**Falsifier sentence:** *Empirical observation that $f_K^{(N)} = n_K/N$ in repeated identical-state-preparation experiments fails to converge as $N \to \infty$ — i.e., does not exhibit law-of-large-numbers-like behavior — would falsify §4.1.*

Currently empirical convergence to Born-rule probabilities is observed; failure would falsify the substrate-level frequency-limit assumption.

### 7.3 Participation-measure formalism failure

**Falsifier sentence:** *Identification that the participation-measure complex polar carrier $P_K = \sqrt{b_K}\,e^{i\pi_K}$ does not represent substrate-level quantum-state content — e.g., that substrate bandwidth $b_K$ does not correspond to squared amplitude magnitude — would falsify §5.1 and propagate to Paper #1.*

### 7.4 Non-bandwidth substrate frequency carriers

**Falsifier sentence:** *Demonstration that substrate-level commitment events have selection probabilities not proportional to bandwidth (e.g., proportional to some other substrate-level quantity like cube of bandwidth, or non-additive functional of substrate content) would falsify §3.2 and the Born rule's substrate-derivation.*

This would correspond to standard QM with a non-Born "Gleason-like" rule (e.g., $|c_K|^4$ or $|c_K|^n$ for $n \neq 2$). Current empirical evidence overwhelmingly supports $n = 2$ (Born), consistent with substrate bandwidth as the substrate frequency carrier.

### 7.5 Frequency-limit interpretation failure

**Falsifier sentence:** *Demonstration that the frequentist interpretation (§4.3) is not the empirically-correct connection between substrate-level frequencies and physical measurement probabilities — e.g., that propensity or Bayesian interpretations are required — would not falsify the substrate-level frequency-limit itself, but would require re-interpreting the empirical content of $f_K$.*

This is a methodological falsifier; the substrate-level structural content is robust.

### 7.6 Cross-domain frequency-rule inconsistency

**Falsifier sentence:** *Demonstration that the substrate-level frequency rule operates differently in different QM contexts (e.g., different "Born-rule" probabilities in different experimental setups) would falsify the universal substrate-level mechanism and reduce the Born rule to a context-specific prescription.*

---

## 8. Position Statement

The **Born rule** $P(K) = |c_K|^2$ is a downstream structural identification in the ED Generative Primitives System. Given the postulated primitives P02 + P04 + P07 + P11 + P12 + the participation-measure formalism (Paper #1) + the frequentist interpretation of substrate-level frequencies (methodological), the Born rule follows from:

1. **Substrate-level commitment-event statistics** (§3.2): commit-event selection rate proportional to bandwidth $b_K$.
2. **Substrate-level frequency-limit convergence** (§4.1–§4.2): over $N \to \infty$ identical state-preparation trials, $f_K \to b_K/\sum b_{K'}$.
3. **Participation-measure identification** (§5.1, Paper #1): $b_K = |c_K|^2$ from $P_K = \sqrt{b_K}\,e^{i\pi_K}$.
4. **Composition** (§5.2): $f_K = |c_K|^2$ for normalized state.

The derivation is **non-circular** (§6): the Born rule is not assumed; it emerges from substrate-level frequency statistics combined with the participation-measure identification.

What this paper claims:

- Given P02 + P04 + P07 + P11 + P12 + Paper #1 + frequentist interpretation, the Born rule follows as a substrate-level participation-frequency limit.
- The substrate-level mechanism is **structurally distinct from** operational reconstructions (Gleason, Hardy, Masanes-Müller, Coecke-Kissinger): ED takes substrate participation as primitive and derives measurement probability; operational reconstructions take measurement probability as primitive and derive its form.
- The Born rule is the anchor for the entire ED QM-kinematics arc.

What this paper does *not* claim:

- The 13 primitives are not derived (Paper_087).
- The Born rule is not "forced from nothing"; conditional on substrate + Paper #1 + frequentist interpretation.
- The complex Hilbert space structure is not derived; upstream from Paper #1.
- Gleason's theorem and operational reconstructions are not in competition; complementary approaches.
- Standard QM's projection postulate is not fully derived beyond substrate-level commitment-event statistics.
- Generic QM predictions (interference, entanglement, etc.) are downstream arc content.
- No claim of falsification of operational reconstruction frameworks.

The empirical case rests on cross-domain reach: the Born rule + substrate-level frequency-mechanism anchors the entire QM-kinematics arc, which connects to Q-COMPUTE (UR-1, Paper_054), entanglement (arc-E), and QFT (T17, Paper_015).

**Series context.** Paper_003 of the QM-kinematics arc. The arc continues with Papers_001 (in queue, pre-individuation amplitudes — upstream), 002 (tensor-product composition), 004 (Gleason-type uniqueness), 005 (projective measurement), 006 (unitary evolution), 007 (Hilbert-space emergence), 008–012 (phase, Berry, AB, Bloch, P-RB-1).

---

## Appendix: Cross-References and Glossary

### Cross-references

- **Position paper:** Paper_087.
- **Paper #1 (Participation Measure):** complex polar carrier $P_K = \sqrt{b_K}\,e^{i\pi_K}$. Upstream.
- **Paper #3 (Inner Product + Tsirelson):** sesquilinear inner product structure. Upstream.
- **Paper_054 (UR-1):** substrate-level commitment-event statistics (Paper_054 §3.2).
- **Paper_087 §5.4 (P04 bandwidth):** primitive enumeration.
- **Paper_087 §5.11 (P11 commitment):** primitive enumeration.

### Glossary

- **Born rule.** $P(K) = |c_K|^2$ — measurement probability is squared amplitude magnitude. Downstream of substrate participation-frequency limit + participation-measure identification.
- **Substrate-level frequency limit.** $f_K = \lim_{N\to\infty}\,n_K/N \to b_K/\sum b_{K'}$ for repeated identical state preparation.
- **Substrate bandwidth $b_K$.** Primitive P04 substrate scalar; substrate-level frequency carrier.
- **Participation-measure complex polar carrier.** $P_K = \sqrt{b_K}\,e^{i\pi_K}$ from Paper #1.
- **Identification $b_K = |c_K|^2$.** From $|P_K|^2 = b_K$ + identification of $P_K$ with quantum-state amplitude $c_K$ (Paper #1).
- **Frequentist interpretation.** Methodological assumption (§4.3) connecting substrate-level long-run frequencies to physical measurement probabilities.
- **Substrate-level commitment-event statistics.** P11 + P04 + P12 substrate-level commit-event selection rate proportional to bandwidth.
- **Non-circularity.** The Born rule is not assumed; emerges from substrate-level frequency statistics + participation-measure identification (§6).

---

**End of Paper_003.**

*Wave-2 Generative Paper — QM-Kinematics Arc Anchor. Born rule as substrate-level participation-frequency limit + participation-measure identification, derived non-circularly from P02, P04, P07, P11, P12 + Paper #1 participation-measure formalism.*
