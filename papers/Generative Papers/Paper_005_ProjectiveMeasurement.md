# Paper_005 — Projective Measurement from P11 Commitment

**Series:** Event Density (ED) Generative Papers — Wave-2 QM-kinematics arc
**Author:** Allen Proxmire
**Status:** Publication draft
**Date:** 2026-05-13
**Repository target:** `domain-arcs/qm-kinematics/Paper_005_ProjectiveMeasurement.md`
**Genre:** Conditional structural derivation within the 13-Primitive Generative System.

---

## Preamble: What This Paper Does NOT Claim

1. **The 13 primitives are not derived** (Paper_087).
2. **No claim that projective-measurement structure is derived from P11 alone.** Derivation uses P11 + P-Channel-Orthogonality (Paper_004) + P-LinRate (Paper_003) + Paper_001 amplitude content + the substrate-level identification of commitment-event outcomes with channel-basis projectors (P-Commit-Projector-Match, this paper's substrate-level commitment).
3. **No claim of derivation of generalized POVM measurement.** Standard projective (von Neumann) measurement only.
4. **No claim of derivation of measurement-back-action / wave-function-collapse phenomenology beyond P11 commitment.** P11 itself is the substrate-level postulate; this paper translates P11 to projector form via P-Commit-Projector-Match.
5. **No claim of unitarity-of-measurement** (no claim that measurement is unitary at substrate level). Measurement is **commitment-induced** at substrate level, which is by P11 irreversible. Unitary evolution covers the pre-measurement regime (Paper_006); measurement is the commitment step.
6. **No claim of decoherence-program derivation.** Decoherence is downstream; this paper supplies the projector-form structure that decoherence theory operates on.

---

## Abstract

This paper derives **projective measurement structure** at substrate level from P11 commitment-irreversibility + Paper_001 pre-individuation amplitudes + Paper_004 P-Channel-Orthogonality + Paper_003 P-LinRate + a paper-specific commitment **P-Commit-Projector-Match** that identifies substrate-level commitment-event outcomes with channel-basis projectors. Under these inputs:

- A substrate-level **measurement event** for chain $C$ is a P11 commitment selecting one channel $K^*$ from the chain's currently-active set.
- The **projector** $\Pi_{K^*} = |K^*\rangle\langle K^*|$ is the substrate-level operator that, when applied to pre-individuation amplitude content $\Psi^C = \sum_K P_K |K\rangle$, gives the post-commitment state $\Psi^C_{\mathrm{post}} = (1/\sqrt{P(K^*)})\,\Pi_{K^*}\,\Psi^C = |K^*\rangle$ — the standard projective-measurement post-state.
- The **completeness** of projectors $\sum_K \Pi_K = I$ follows from P-Channel-Orthogonality + P-Bipartite-Mapping-like joint coverage.
- **Probability** $P(K^*) = |P_{K^*}|^2 = \langle\Psi|\Pi_{K^*}|\Psi\rangle$ follows from Paper_003 P-LinRate + Paper_001 identification.

The paper makes no claim of POVM-generalization, no claim of unitarity-of-measurement (P11 is irreversible at substrate level), and no claim of decoherence-program derivation. The substrate-level **structural form** of projective measurement is delivered; standard measurement-theory machinery operates on it via Paper_007 Hilbert-space completion.

---

## 1. Introduction

### 1.1 What this paper does

Paper_007 forward-pointed Paper_005 as the projective-measurement derivation. This paper supplies it: P11 commitment events + Paper_001 amplitude content + Paper_004 P-Channel-Orthogonality + P-Commit-Projector-Match → standard projective-measurement structure.

### 1.2 Arc context

- Paper_001 (amplitudes), Paper_003 (Born rule), Paper_004 (Gleason-uniqueness attempt), **Paper_005 (this paper: projective measurement)**, Paper_006 (unitary evolution), Paper_007 (Hilbert-space emergence).

---

## 2. Primitive Inputs

**Substrate primitives (postulated, Paper_087):** P02, P04, P07, P11.

**Upstream paper dependencies:** Paper_087, Paper_001 (amplitudes), Paper_003 (Born rule + P-LinRate), Paper_004 (P-Channel-Orthogonality).

**Paper-specific postulate:**

- **P-Commit-Projector-Match (Substrate commitment-event outcomes identified with channel-basis projectors):** *A P11 commitment event for chain $C$ that selects channel $K^*$ corresponds, in the motif-algebra / Hilbert-space arena, to action of the projector $\Pi_{K^*} = |K^*\rangle\langle K^*|$ on the pre-individuation amplitude content $\Psi^C$, normalized by $1/\sqrt{P(K^*)}$.* Substrate-level identification commitment; bridges P11 commitment-event substrate language to standard projector-arena Hilbert-space language.

---

## 2.5 Load-Bearing Step Audit

| Step | Status | Justification |
|---|---|---|
| 13 primitives postulated | P | Paper_087 |
| P11 commitment irreversibility | P | Paper_087 §5.11 |
| Pre-individuation amplitudes | D | Paper_001 |
| P-Channel-Orthogonality | P | Paper_004 |
| P-LinRate (Born) | P | Paper_003 |
| Substrate commit-event ↔ projector identification | **P (P-Commit-Projector-Match)** | §2 substrate-level identification commitment |
| Projector $\Pi_K = |K\rangle\langle K|$ as substrate operator | **P (definitional, part of P-Commit-Projector-Match)** | §3.1 — definitional form following the identification commitment |
| Completeness $\sum_K \Pi_K = I$ | **I (standard linear algebra)** | §3.2 — standard linear-algebraic consequence of completeness of orthonormal basis projectors. Not substrate-derived. *(Round-7 relabel.)* |
| Post-commitment state $\Psi^C_{\mathrm{post}} = |K^*\rangle$ | **P (definitional consequence of P-Commit-Projector-Match)** | §3.3 — post-state form follows definitionally from the postulate + normalization; not an additional derivation step. *(Round-7 relabel.)* |
| Probability $P(K^*) = |P_{K^*}|^2$ | **D conditional on P-LinRate** | §3.4 — substantive composition step combining P-LinRate (Paper_003 substrate-level) with Paper_001 amplitude identification; gives the Born rule for projective measurement |
| Measurement is irreversible at substrate level | **P (postulational consequence of P11)** | §3.5 — restating P11 commitment-irreversibility for measurement context; not a new derivation from P11. *(Round-7 relabel: restated-postulate, not derived.)* |

All rows P, D, I, or labeled. **No A (asserted) rows.**

---

## 3. Substrate-Level Projective Measurement

### 3.1 Substrate commitment events as projector action

By P11, at a commitment event for chain $C$ at substrate time $t_{\mathrm{commit}}$, the chain's multi-channel pre-individuation amplitude content $\Psi^C(t < t_{\mathrm{commit}}) = \sum_K P_K^C |K\rangle$ collapses to single-channel content $\Psi^C(t > t_{\mathrm{commit}}) = |K^*\rangle$ for some selected channel $K^*$.

By **P-Commit-Projector-Match (§2)**, this corresponds in the motif-algebra arena to projector action:

$$
\Pi_{K^*}\,\Psi^C = P_{K^*}^C |K^*\rangle.
$$

Normalized post-commitment state:

$$
\Psi^C_{\mathrm{post}} = \frac{\Pi_{K^*}\,\Psi^C}{\|\Pi_{K^*}\,\Psi^C\|} = \frac{P_{K^*}^C|K^*\rangle}{|P_{K^*}^C|} = e^{i\pi_{K^*}^C}\,|K^*\rangle.
$$

Modulo overall phase (gauge equivalence), $\Psi^C_{\mathrm{post}} = |K^*\rangle$ — standard projective-measurement post-state.

### 3.2 Completeness of projectors

By Paper_004 P-Channel-Orthogonality, $\{|K\rangle\}_{K \in \mathcal{K}}$ is an orthonormal basis of the motif algebra (Paper_007 §3.1). The completeness relation:

$$
\sum_{K \in \mathcal{K}} \Pi_K = \sum_K |K\rangle\langle K| = I
$$

follows from standard linear-algebra (algebraic step: any motif-algebra element decomposes uniquely as $\Psi = \sum_K \Psi_K |K\rangle = \sum_K \Pi_K \Psi$).

### 3.3 Post-commitment state form

From §3.1: the post-commitment state under projector $\Pi_{K^*}$ is $|K^*\rangle$ (up to gauge phase). This is the standard von Neumann post-measurement state.

### 3.4 Born rule for measurement probability

By Paper_003 P-LinRate, the substrate-level rate of commitment to channel $K^*$ is $\propto b_{K^*} = |P_{K^*}|^2$. Normalized:

$$
P(K^*) = \frac{|P_{K^*}|^2}{\sum_K |P_K|^2} = |P_{K^*}|^2 \quad \text{(normalized state)}.
$$

In Hilbert-space arena: $P(K^*) = |\langle K^*|\Psi\rangle|^2 = \langle\Psi|\Pi_{K^*}|\Psi\rangle$ — standard Born-rule for projective measurement.

### 3.5 Irreversibility

By P11, the commitment event is **irreversible**: there is no substrate-level operation that maps the post-commitment state $|K^*\rangle$ back to the pre-commitment superposition $\Psi^C = \sum_K P_K|K\rangle$. **Measurement is therefore irreversible at substrate level.**

This is distinct from unitary evolution (Paper_006), which covers pre-measurement substrate-level dynamics. Unitary evolution preserves coherent multi-channel content; commitment events break it irreversibly.

### 3.6 Sequential measurements

For sequential commitment events at $t_1 < t_2$:

- At $t_1$: commit to $K_1^*$; post-state $|K_1^*\rangle$.
- Between $t_1, t_2$: unitary evolution (Paper_006) acts on $|K_1^*\rangle$, producing $\Psi(t_2) = U(t_2, t_1)|K_1^*\rangle$.
- At $t_2$: commit from $\Psi(t_2)$ to $K_2^*$ with probability $|\langle K_2^*|U(t_2, t_1)|K_1^*\rangle|^2$.

Standard sequential-projective-measurement structure.

---

## 4. Falsification Criteria

### 4.1 Commitment without projector form

**Falsifier sentence:** *Empirical demonstration that substrate-level commitment events produce post-states inconsistent with projector action — e.g., post-state retains coherent multi-channel content — would falsify P-Commit-Projector-Match.*

### 4.2 Completeness violation

**Falsifier sentence:** *Empirical demonstration that $\sum_K \Pi_K \neq I$ — i.e., the channel-basis projectors are incomplete in the motif-algebra arena — would falsify §3.2 + P-Channel-Orthogonality.*

### 4.3 Measurement reversibility

**Falsifier sentence:** *Empirical demonstration that substrate-level measurement is reversible — i.e., a post-commitment state $|K^*\rangle$ can be mapped back to a pre-commitment superposition via a substrate-level operation — would falsify P11.*

### 4.4 Born-rule violation in projective measurement

**Falsifier sentence:** *Empirical violation of $P(K^*) = |\langle K^*|\Psi\rangle|^2$ in standard projective measurements — beyond noise — would falsify §3.4 + P-LinRate.*

---

## 5. Position Statement

**Projective measurement** at the substrate level is the structural consequence of P11 commitment-irreversibility + Paper_001 amplitude content + Paper_004 P-Channel-Orthogonality + Paper_003 P-LinRate + P-Commit-Projector-Match. The substrate-level structural form matches standard von Neumann projective measurement.

What this paper claims:

- Substrate commitment events correspond to projector action via P-Commit-Projector-Match.
- Standard Born-rule probability + post-state form follow from upstream Paper_001/003/004 + this paper.
- Measurement irreversibility is built in via P11.

What this paper does *not* claim:

- POVM generalization not delivered.
- Decoherence-program derivation not in this paper.
- P-Commit-Projector-Match not derivable from canonical 13 alone.

**Series context.** Paper_005 of QM-kin arc.

---

## Appendix

**Cross-references:** Paper_087, Paper_001, Paper_003, Paper_004, Paper_006, Paper_007.

**Glossary:**
- **Projective measurement.** Standard von Neumann measurement: projector action + Born-rule probability + post-state collapse.
- **P-Commit-Projector-Match.** Substrate-level identification of P11 commitment with projector action.
- **Commitment event.** P11 substrate-level event: multi-channel → single-channel.

---

**End of Paper_005.**
