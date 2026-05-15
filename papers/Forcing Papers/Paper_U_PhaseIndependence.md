# Paper U-PhaseIndependence — Phase-Independence of Bandwidth Values

**Series:** Wave-3 U-Series (Phase-1 Schrödinger Program, methodological)
**Status:** Wave-3 generative paper; **M3** verdict (definitional lemma + identification with $U(1)$ gauge invariance; no Hardy-class closed-proof derivation)
**Companions:** Paper_U1 (participation measure), Paper_002 (Born-Gleason), Paper_087, Paper_089 (V1), Paper_090 (V5).

---

## Preamble — What This Paper Does NOT Claim

1. This paper does **not** claim derivation of $U(1)$ gauge invariance of QM from nothing. Result is conditional on the 13 ED primitives (Paper_087) + declared paper-specific postulates.
2. It does **not** claim closed-proof reconstruction in the Hardy 2001 / CDP 2011 / Coecke-Kissinger operational-reconstruction sense. ED sits in the substrate-ontology lineage ('t Hooft cellular-automaton, Wolfram Ruliad, causal-set program), not the operational-reconstruction lineage.
3. It does **not** override Paper_095's three-tier verdict grammar. Verdict for this paper is stated in §1.
4. It does **not** claim closed-proof derivation of $U(1)$ gauge invariance from substrate primitives — that derivation is OPEN. Relative phases between amplitudes carry observable interference content; only global-phase independence of bandwidth magnitudes is claimed here.
5. The paper is a **definitional lemma** (polar-decomposition invariance of $|P_K| = b_K$ under global $U(1)$) combined with **identification** of P09 with standard $U(1)$ gauge invariance. No new numerical content; substrate-derivation of $U(1)$ gauge invariance from P09 alone is OPEN.

---

## Abstract

This paper supplies a definitional lemma: under the participation-measure polar decomposition $P_K = b_K e^{i\pi_K}$ (Paper_U1), bandwidth magnitudes $b_K$ are invariant under global $U(1)$ phase rotation $\Psi \to e^{i\alpha}\Psi$, with P03 + P04 + P08 acting as gauge-invariant primitive content. The structural lemma is combined with an identification of P09 ($U(1)$-valued polarity) with the standard $U(1)$ gauge invariance of QM. Closed-proof derivation of $U(1)$ gauge invariance from P09 alone is OPEN. Verdict: **M3** (definitional lemma + identification) per Paper_095's three-tier verdict grammar. Key falsifier **F1**: empirical detection of an observable that depends on global $U(1)$ phase of a participation amplitude.

---

## §1 Statement of Result

**Scope reframe.** This paper is a **definitional lemma**: polar-decomposition invariance of $|P_K| = b_K$ under global $U(1)$ phase rotation, combined with **identification** of P09 with the standard $U(1)$ gauge invariance of QM. It is NOT a closed-proof derivation of $U(1)$ gauge invariance from substrate primitives; that derivation is **OPEN**.


**Claim.** Under the participation-measure structure $P_K = b_K e^{i\pi_K}$ (Paper_U1), the bandwidth magnitudes $b_K \geq 0$ are **invariant under global $U(1)$ phase transformations** of substrate participation amplitudes:
$$\Psi \to e^{i\alpha}\Psi \implies b_K \to b_K , \quad \pi_K \to \pi_K + \alpha .$$

The phase-independence of bandwidth values is form-IDENTIFIED (no D rows in audit table; downgraded from FORM-FORCED per Paper_095 §2.3) by:
1. P03 (channel + locus indexing) — locus structure is gauge-invariant.
2. P08 (substrate scale $\ell_{\mathrm{ED}}$) — scale is gauge-invariant.
3. V1/V5 kernel structure — kernel rule-types act on amplitudes; their bandwidth content is the amplitude modulus $|P_K| = b_K$, which is phase-invariant.

This is the substrate-level foundation for the operational unobservability of global $U(1)$ phase in QM.

Verdict: **M3** — definitional polar-decomposition lemma plus identification of P09 with $U(1)$ gauge invariance; substrate derivation of $U(1)$ gauge invariance from P09 alone is OPEN.

---

## §2 Primitive Inputs

### 2.1 Primitives invoked

- **P03 (Channel + locus indexing; spatial homogeneity)** — gauge-invariant locus.
- **P04 (Bandwidth)** — non-negative real bandwidth content.
- **P08 (Substrate scale $\ell_{\mathrm{ED}}$)** — gauge-invariant scale.
- **P09 ($U(1)$-valued polarity)** — the gauge group under which the phase transformation acts.

### 2.2 Upstream Dependencies

- **I-U1:** Participation measure $P_K = b_K e^{i\pi_K}$.
- **I-008:** Phase structure $S^1$ on rule-types (Paper_008).
- **I-002:** Born-Gleason rule (Paper_002).
- **I-089, I-090:** V1 and V5 kernel structures.
- **I-Gauge:** Standard $U(1)$ gauge-theory machinery.

---

## §3 Derivation

### 3.1 Participation measure under global $U(1)$ phase

By Paper_U1, the participation measure for motif $K$ is $P_K = b_K e^{i\pi_K}$ with $b_K \geq 0$ and $\pi_K \in [0, 2\pi)$. Under a global $U(1)$ phase transformation acting on all amplitudes uniformly:
$$\Psi \to e^{i\alpha}\Psi \implies P_K \to e^{i\alpha} P_K = b_K e^{i(\pi_K + \alpha)} .$$

Decomposing the transformed measure:
- Modulus: $|P_K^{new}| = b_K$ (**unchanged**).
- Phase: $\pi_K^{new} = \pi_K + \alpha$ (changed by global $\alpha$).

The bandwidth magnitudes $b_K$ are phase-invariant. This is by direct construction of the $b_K e^{i\pi_K}$ polar decomposition.

### 3.2 Substrate origin of phase-independence

The substrate-level reason for phase-independence of bandwidth values:

**P04 bandwidth is real-valued.** P04 (bandwidth as non-negative additive scalar) supplies bandwidth content that is **inherently real-valued** at substrate level. No phase information is encoded in P04 itself; phase is supplied separately by P09.

**P03 + P08 are gauge-invariant.** Channel + locus indexing (P03) and substrate scale (P08) are gauge-invariant primitives — they do not transform under $U(1)$ phase rotation. Bandwidth content, being indexed by P03 + P08, inherits gauge-invariance.

**Kernel rule-types (V1, V5) act on amplitudes.** V1 and V5 kernels (P10) modulate amplitudes including their phases. But the **amount of substrate-bandwidth content** carried by a motif — its $b_K$ — is determined by P04 + P03 + P08, not by the kernel-induced phase.

### 3.3 Operational unobservability of global phase

The phase-independence of bandwidth values translates to **operational unobservability** of global $U(1)$ phase in QM:

- The Born rule (Paper_002) gives probability $|P_K|^2 = b_K^2$, depending only on $b_K$.
- Observables $\hat O$ have expectation values $\langle\Psi|\hat O|\Psi\rangle$ that transform trivially under $\Psi \to e^{i\alpha}\Psi$ (the $\alpha$'s cancel between bra and ket).
- All measurement outcomes are insensitive to global phase.

This is the substrate-level foundation for the **gauge equivalence** of states differing by global $U(1)$ phase — a foundational structural feature of QM.

### 3.4 Why relative phases ARE observable

By contrast, **relative phases** between distinct amplitudes are observable. For a superposition
$$\Psi = c_1 \Psi_1 + c_2 \Psi_2 = b_1 e^{i\pi_1}\Psi_1 + b_2 e^{i\pi_2}\Psi_2 ,$$
the interference term in $|\Psi|^2$ depends on $\pi_1 - \pi_2$ (the relative phase). Global $U(1)$ rotation shifts both $\pi_1$ and $\pi_2$ by the same $\alpha$, leaving $\pi_1 - \pi_2$ invariant.

The substrate origin: relative phases between distinct motifs carry **structural adjacency content** (Paper_U1 §3.4); global phase carries no structural content (it can be absorbed by a constant gauge transformation that acts on all motifs uniformly).

### 3.5 Consistency with Born-Gleason

Paper_002 (Born-Gleason rule) derives $\mathrm{Prob}(K) = |P_K|^2 = b_K^2$. The probability assignment is **manifestly** phase-independent in the bandwidth magnitudes — it depends only on $b_K$.

This paper supplies the substrate-level structural reason for that phase-independence: P04 + P03 + P08 are gauge-invariant; only P09 phase content is gauge-charged.

### 3.6 Connection to Wick-rotation and time-reversal

The phase-independence of bandwidth values is preserved under:
- **Wick rotation** $t \to it$: transforms $e^{i\pi_K}$ globally but leaves $b_K$ unchanged.
- **Time-reversal** $T: \Psi \to \Psi^*$: complex-conjugates $e^{i\pi_K} \to e^{-i\pi_K}$ but leaves $b_K$ unchanged.

Both operations act on the phase sector while preserving the bandwidth sector — consistent with the substrate-level structural separation of P04 (bandwidth) from P09 (phase).

### 3.7 Numerical content

No numerical content. This is a **pure structural / definitional** result: $b_K$ is phase-invariant by definition of polar decomposition + gauge-invariance of P03, P04, P08.

What is form-IDENTIFIED: the structural independence of bandwidth values from global $U(1)$ phase.

What is INHERITED: nothing substantive. This paper supplies a structural lemma used by downstream papers (Born rule, Heisenberg, etc.) but has no inherited numerical content of its own.

---

## §4 Audit Table

| # | Step | Label | Notes |
|---|---|---|---|
| 1 | P03 channel + locus indexing | P | Primitive. |
| 2 | P04 bandwidth (real-valued) | P | Primitive. |
| 3 | P08 substrate scale | P | Primitive. |
| 4 | P09 $U(1)$ polarity (gauge group) | P | Primitive. |
| 5 | $P_K = b_K e^{i\pi_K}$ polar decomposition | I | Paper_U1. |
| 6 | Global $U(1)$ phase rotation $\Psi \to e^{i\alpha}\Psi$ | I | Standard math. |
| 7 | $|P_K|$ phase-invariant under polar decomposition | P | Polar decomposition is definitional (Paper_095 §2.3); not a derivation. |
| 8 | $b_K$ phase-invariant | P | Definitional consequence of step 7. |
| 9 | P03, P04, P08 are gauge-invariant primitives | I | Per definitions. |
| 10 | Born rule probability depends only on $b_K$ | I | Paper_002. |
| 11 | Operational unobservability of global phase | I | Standard QM. |
| 12 | Relative phases observable (interference) | I | Standard QM. |
| 13 | Identification: P09 $\leftrightarrow$ standard $U(1)$ gauge invariance | A→position | Framing claim; substrate derivation of $U(1)$ gauge invariance from P09 alone OPEN. |
| 14 | Role of P11 (global-phase unobservability) | OPEN | Currently absent from body text; substrate role of P11 in fixing global-phase unobservability OPEN. |
| 15 | Verdict M3 (definitional lemma + identification) | A→position | Per Paper_095. |

---

## §5 Falsification Criteria

- **F1:** Empirical detection of an observable that depends on global $U(1)$ phase of a substrate participation amplitude. Would refute phase-independence.
- **F2:** Substrate evidence that P04 bandwidth content can carry phase information directly (not just via the multiplicative $e^{i\pi_K}$ factor). Would refute the structural separation.
- **F3:** Polar decomposition $P_K = b_K e^{i\pi_K}$ shown to fail (e.g., $b_K$ depending implicitly on $\pi_K$). Would refute step 5.

---

## §6 Position Statement

This paper sits within the **substrate-ontology research-program lineage** ('t Hooft cellular-automaton interpretation of QM; Wolfram Ruliad / hypergraph-rewriting; causal-set program, Sorkin et al.), **not** within the operational-reconstruction lineage (Hardy 2001, CDP 2011, Coecke-Kissinger). Methodology per Paper_095 (form-FORCED / value-INHERITED).

This paper supplies a methodological / structural lemma underpinning the Phase-1 QM-emergence program: bandwidth values are phase-invariant, supporting the operational unobservability of global $U(1)$ phase.

**Relationship to other ED papers:**
- **Paper_U1:** supplies the participation-measure polar decomposition.
- **Paper_002:** Born-Gleason rule depends only on $b_K^2$.
- **Paper_008:** phase structure supplies $\pi_K$'s $S^1$ content.

**Numerical content:** none. **Form IDENTIFIED.** Phase-independence of bandwidth values under global $U(1)$ (no D rows in audit table; downgraded from FORM-FORCED per Paper_095 §2.3).

Verdict: **M3** (definitional lemma + identification of P09 with $U(1)$ gauge invariance; substrate-derivation of gauge invariance from P09 alone OPEN).

---

**End Paper U-PhaseIndependence.**
