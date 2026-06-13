# Memo_ED_KernelArrowAsymmetry — Construction Memo (Exploration)

**Series:** Wave-3 Construction Memo (Cosmology Arc; baryogenesis sub-thread; Direction 1 from Memo_ED_Baryogenesis_NextExplorations)
**Status:** Substrate-graph exploration of whether kernel-arrow + V1 retarded propagation can act as a natural symmetry-breaker for asymmetric admission between chirality classes in the post-SCBU saturation regime. **Not a claimed closure. Not a derivation. No new primitives. No hard postulates declared.** This memo arrives at a **mixed result**: V1 transport-side reading is negative; P11 commitment-side reading is structurally promising but the load-bearing identification is OPEN.
**Date:** 2026-05-16
**Anchors:** Paper_087 (primitives); Paper_089 (V1 retarded kernel; T18 advanced-V1 refuted); Paper_093 (T18 kernel-arrow); Paper_ED_CCC §3.6 + §3.7 (post-SCBU homogeneity); Paper_072 (individuation regime); Memo_ED_ChainArrowChirality (chirality definition); Memo_ED_AdmissionFilter; Memo_ED_BinaryChirality; Paper_ED_Baryogenesis_Open (M2 with P-BinaryAdmission); Memo_ED_Baryogenesis_NextExplorations (Direction 1 priority).

---

## §1 Problem restatement

The four-memo cascade arrived at honest M2 framing for Paper_ED_Baryogenesis: chirality $\chi_C \in S^1$ operationally defined; binary admission $\chi_C \in \{0, \pi\}$ postulated via P-BinaryAdmission (substrate-graph derivation OPEN); **asymmetric admission cost** between aligned ($\chi_C = 0$) and anti-aligned ($\chi_C = \pi$) classes in the saturation regime separately OPEN.

This memo addresses the second OPEN item: even granting P-BinaryAdmission, why one chirality class survives saturation and the other decoheres. Direction 1 from Memo_ED_Baryogenesis_NextExplorations asks: **does maintaining $\chi_C = \pi$ under V1 retarded transport impose a substrate-graph cost that $\chi_C = 0$ does not, given a globally coherent kernel-arrow in the post-SCBU regime?**

Two readings of "imposes a cost" are explored below:

- **Transport-side:** the cost is on V1 retarded transport — anti-aligned chains require V1 to perform additional substrate-graph work during propagation.
- **Production-side:** the cost is on P11 commitment-event creation — anti-aligned chains require P11 to create commitments against the substrate's natural commitment-phase content.

---

## §2 Setup from existing primitives

Per Memo_ED_ChainArrowChirality and Paper_ED_CCC §3.6–§3.7:

- $\chi_C(e_n) := \pi_C(e_n) - \pi_K(\ell(e_n)) \pmod{2\pi}$, where $\pi_C$ is the P09 phase of the chain-arrow $\sigma_C$ and $\pi_K$ is the P09 phase of the kernel-arrow $\sigma_K$ at the chain's locus $\ell(e_n)$.
- In the post-SCBU regime, $\pi_K$ is globally coherent across substrate — constant up to a global $U(1)$ choice. **$\Delta\pi_K(\ell \to \ell') = 0$ for all $\ell, \ell'$.**
- Per Paper_072 individuation, chain-identity preservation requires $\chi_C$ to be stable along the chain's commitment sequence.
- Per Paper_089 T18, V1 is strictly retarded — advanced V1 refuted by P11.
- Per Paper_093 T18, the kernel-arrow $\sigma_K$ is identified with V1's retarded-support direction.

The substrate-graph question: in the saturation regime, does V1 transport or P11 commitment introduce a structural asymmetry between $\chi_C = 0$ and $\chi_C = \pi$ chains?

---

## §3 Toy model 1: V1 transport-side reading (negative result)

Consider V1's action on chain phase content during one commitment step. Let $V_1$ transport the chain amplitude $A_C(e_n) \cdot e^{i\pi_C(e_n)}$ from event $e_n$ to event $e_{n+1}$.

Two structural cases for V1's phase content:

**Case A: V1 is phase-trivial along chain transport.** $V_1$ acts on amplitude without rotating phase: $\pi_C(e_{n+1}) = \pi_C(e_n)$. Chirality $\chi_C(e_{n+1}) = \pi_C(e_{n+1}) - \pi_K(\ell(e_{n+1})) = \pi_C(e_n) - \pi_K = \chi_C(e_n)$ (using post-SCBU global coherence). $\chi_C$ is conserved per Memo_ED_ChainArrowChirality §3.5. **Symmetric** for both chirality classes — both transport with identical phase preservation.

**Case B: V1 has a per-step phase contribution $\delta\pi^{V_1}$.** $\pi_C(e_{n+1}) = \pi_C(e_n) + \delta\pi^{V_1}$. For $\chi_C$ to be conserved (Paper_072 individuation requirement), $\delta\pi^{V_1} = \Delta\pi_K = 0$ in the post-SCBU regime. **Forced $\delta\pi^{V_1} = 0$** — V1 is structurally phase-trivial in this regime.

Either case yields the same conclusion: **V1 transport in the post-SCBU regime is symmetric across $\chi_C = 0$ and $\chi_C = \pi$ chains.** Both transport with identical phase preservation; neither incurs substrate-graph cost beyond the other.

**Negative result.** The transport-side reading does not supply asymmetric admission. The substrate symmetry between {0, π} under V1 transport in the globally-coherent kernel-arrow regime is too clean to admit a transport-side bias.

This matches the structural pattern from Memo_ED_BinaryChirality: the post-SCBU regime's substrate symmetry (globally-coherent $\pi_K$, trivial P05 transport) precludes most substrate-side discriminations between chirality classes. V1 transport falls into the same bucket.

---

## §4 Toy model 2: P11 commitment-side phase inheritance (promising; OPEN)

The transport-side reading is symmetric. The production-side reading is structurally different.

**Setup.** P11 commitment-irreversibility supplies the substrate's forward time-direction. Paper_093 T18 identifies the kernel-arrow $\sigma_K$ with V1's retarded support direction. Per Paper_089 T18, V1 retarded support is forward *because* P11 is forward (advanced V1 refuted by P11). **P11's forward direction and the kernel-arrow direction are substrate-side identified.**

**Hypothesis.** P09 phase content attached to substrate directional structure inherits the kernel-arrow phase. Specifically: when a P11 commitment event creates new chain content at substrate locus $\ell$, the commitment carries P09 phase $\pi_{\mathrm{commit}}(\ell) = \pi_K(\ell)$.

Under this hypothesis, newly-created chains have default chirality $\chi_C = \pi_{\mathrm{commit}} - \pi_K = 0$. Aligned chirality is the natural outcome of commitment-event creation. Anti-aligned chirality ($\chi_C = \pi$) would require commitments to be created at phase $\pi_K + \pi$ — *inverted* relative to the natural commitment-phase content.

**Implication for saturation regime.** In the saturation regime ($\Gamma_{\mathrm{prod}}$ near its substrate-c bound, capacity at minimum), only the natural outcome is realized. Substrate slack required to "invert" the commitment phase is unavailable; anti-aligned chain creation is suppressed.

**Post-saturation restoration.** Once substrate capacity recovers, the substrate has slack to invert commitment phase; anti-aligned chain creation resumes. This matches Paper_ED_Baryogenesis_Open §3.6 (post-saturation symmetric pair-production restoration) and ED-I-11's "asymmetry as a one-time event" framing.

**This is structurally what's needed for asymmetric admission.** The substrate-graph mechanism is identified — kernel-arrow-phase-inheritance via P11 commitment events — without requiring new primitives. The asymmetry is naturally biased toward $\chi_C = 0$ (matter-class) chains by the substrate's directional structure.

**Status: structurally promising, but the load-bearing identification is OPEN.**

The hypothesis $\pi_{\mathrm{commit}} = \pi_K$ is not currently derivable from existing primitives. P11 supplies binary commitment-direction (forward); Paper_093 T18 supplies kernel-arrow ↔ V1 retarded support; P09 supplies continuous $U(1)$ phase. **The conjunction P11 + Paper_093 T18 + P09 does not automatically supply that P11 commitments inherit $\pi_K$ phase content.** The inheritance is a substrate-graph identification that would need separate construction.

Two readings of the hypothesis's status:

- **(i) Constructible:** the inheritance might follow from a deeper substrate-graph derivation that recognizes commitment-event creation as a substrate-side reflection of the kernel-arrow's directional content. P11 commitment events occur *along* the V1 retarded direction; if "along V1 direction" carries P09 phase $\pi_K$, the inheritance follows. This direction is worth a focused construction memo.
- **(ii) Requires postulate:** if the inheritance is not derivable, it becomes a paper-specific postulate **P-CommitPhaseInheritance** that would join P-BinaryAdmission as a second declared postulate in Paper_ED_Baryogenesis. Verdict would remain M2 but with two postulates instead of one — strictly weaker.

The honest path: attempt (i) first via focused construction. If (i) closes, asymmetric admission is derived from existing primitives and the baryogenesis paper upgrades M2 → M3-form-IDENTIFIED with one postulate (P-BinaryAdmission) and the asymmetric-admission step closed at D-via-I. If (i) fails after focused attempt, fall back to (ii) with explicit P-CommitPhaseInheritance.

---

## §5 IDENTIFIED vs OPEN

### IDENTIFIED in this memo:

- **V1 transport-side reading is symmetric** in the post-SCBU globally-coherent regime. No asymmetric admission via V1 transport alone. (§3, negative result.)
- **P11 commitment-side reading is structurally promising.** Substrate-graph mechanism via P11 + Paper_093 T18 + P09 conjunction is identified as a candidate route for asymmetric admission. (§4.)
- **The hypothesis $\pi_{\mathrm{commit}} = \pi_K$** — that P11 commitment events inherit kernel-arrow P09 phase content — is the load-bearing structural identification. If true, asymmetric admission follows naturally; saturation regime gives matter dominance; post-saturation restores symmetric pair-production.

### OPEN:

- **Substrate-graph derivation that P11 commitments inherit $\pi_K$ phase.** Whether the inheritance follows from existing primitives or requires a paper-specific postulate is unresolved. **This is the load-bearing OPEN item.**
- **Quantitative substrate-graph derivation of the admission-cost asymmetry.** Even granting the inheritance, the *magnitude* of the substrate-graph cost difference between $\chi_C = 0$ and $\chi_C = \pi$ commitments in the saturation regime is not constructed. Would determine the quantitative baryon-to-photon ratio $\eta_B$ derivation (currently INHERITED).
- **Connection to standard QFT charge conjugation $C$.** Whether the substrate-graph commitment-phase-inheritance corresponds to the standard QFT $C$ eigenvalue assignment is a separate identification, deferred to RQM-arc follow-up.

### Cross-arc consequences:

- If Direction 1 closes via the inheritance hypothesis, baryogenesis paper upgrades M2 → M3 retroactively. P-BinaryAdmission remains as the only paper-specific postulate; asymmetric admission becomes D-via-I.
- If Direction 1 fails (requires postulate), framework remains M2 with two postulates. Acceptable but strictly weaker than current single-postulate M2.

---

## §6 Status + recommended next exploration

**Mixed result.** The transport-side reading of Direction 1 is negative: V1 transport in the post-SCBU regime is too symmetric to supply asymmetric admission. The production-side reading is structurally promising: P11 commitment-phase inheritance from the kernel-arrow gives the right structural form for matter-dominance via saturation-regime selective admission, **but the inheritance itself is the load-bearing OPEN derivation**.

This is consistent with the substrate-research-frontier pattern across the four-memo cascade: the post-SCBU regime's substrate symmetry is structurally clean enough that most substrate-side discriminations between chirality classes don't admit closure from existing primitives. The production-side toy model identifies *where* the asymmetry could enter (commitment-phase inheritance) without supplying the substrate-graph closure.

**Recommended next exploration (non-restrictive):**

The natural follow-up is a focused construction memo attempting the kernel-arrow-phase-inheritance derivation: **Memo_ED_CommitPhaseInheritance**, examining whether P11 + Paper_093 T18 + P09 jointly imply $\pi_{\mathrm{commit}} = \pi_K$ at substrate-graph level, or whether the inheritance requires a paper-specific postulate.

Three possible outcomes:

1. **Derivable from existing primitives** → asymmetric admission closes; baryogenesis paper M2 → M3 upgrade.
2. **Requires postulate but the postulate is natural** (single sentence of substrate-graph commitment-phase identification) → declare P-CommitPhaseInheritance; baryogenesis paper M2 with two postulates; honest research-program state.
3. **Inheritance fails to close** (substrate-graph counterexample) → asymmetric admission remains OPEN at deeper level; reconsider direction.

Either way the corpus learns something. The memo is cheap to attempt (focused, ~2k words) and the outcome propagates retroactively to Paper_ED_Baryogenesis_Open.

**Alternative directions still open** (per Memo_ED_Baryogenesis_NextExplorations):

- **Direction 2 (Memo_ED_T17_RuleTypeBundle_ChiralityExtension)** — addresses binary admission, not asymmetric admission. Independent route.
- **Direction 3 (Memo_ED_P05_Holonomy)** — also binary admission, not asymmetric admission.
- **Angle 2 (V5 cross-chain coupling as baryogenesis carrier)** — could supply asymmetric admission via V5 algebraic content; substantively different from kernel-arrow approach; speculative.
- **Angle 4 (Saddle-Hessian eigenvalue asymmetry under V1)** — ties baryogenesis to inflation arc; speculative connection.

**Non-restrictive note.** This memo's mixed result does not close Direction 1 negatively — it identifies which sub-reading (transport vs production) is negative and which is promising-but-OPEN. The production-side toy model is the cleanest substrate-graph candidate for asymmetric admission to emerge from the four-memo cascade so far. Worth pursuing via the follow-up memo. If it closes, the baryogenesis arc reaches M3; if not, the framework remains honest at M2 and the substrate-research frontier is sharper.

---

**End Memo_ED_KernelArrowAsymmetry.**
