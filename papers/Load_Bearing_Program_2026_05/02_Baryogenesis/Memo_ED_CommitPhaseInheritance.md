# Memo_ED_CommitPhaseInheritance — Construction Memo (Exploration)

**Series:** Wave-3 Construction Memo (Cosmology Arc; baryogenesis sub-thread; follow-up to Memo_ED_KernelArrowAsymmetry)
**Status:** Substrate-graph investigation of whether the hypothesis $\pi_{\mathrm{commit}} = \pi_K$ — that P11 commitment events inherit the local kernel-arrow P09 phase — is derivable from existing primitives, or must be declared as a paper-specific postulate. **Not a claimed closure. No new primitives. No hard postulates declared.** Outcome: **(2) strongly natural under strict post-SCBU homogeneity, but full derivation depends on whether strict homogeneity holds in the ignition regime — a substrate-graph question that is itself partially OPEN.**
**Date:** 2026-05-16
**Anchors:** Paper_087 (primitives P09, P11); Paper_089 (V1 retarded kernel; T18); Paper_093 (T18 kernel-arrow); Paper_ED_CCC §3.6 + §3.7 (post-SCBU homogeneity, ignition regime); Memo_ED_ChainArrowChirality; Memo_ED_KernelArrowAsymmetry; Paper_ED_Baryogenesis_Open.

---

## §1 Restate the toy model

From Memo_ED_KernelArrowAsymmetry §4: **if** P11 commitment events at substrate locus $\ell$ create new chain content with P09 phase $\pi_{\mathrm{commit}}(\ell) = \pi_K(\ell)$, **then**:

- Newly-created chains have default chirality $\chi_C = \pi_{\mathrm{commit}} - \pi_K = 0$ (aligned).
- Anti-aligned chains ($\chi_C = \pi$) require commitment-phase inversion to $\pi_K + \pi$.
- In the saturation regime ($\Gamma_{\mathrm{prod}}$ at substrate-c bound), substrate slack for inversion is unavailable → asymmetric admission → matter dominance.
- Post-saturation, substrate slack returns → phase-inverted commitments resume → symmetric pair-production restores.

This memo asks whether $\pi_{\mathrm{commit}} = \pi_K$ is forced, strongly natural, or unsupported by existing primitives.

---

## §2 What a P11 commitment event supplies at substrate-graph level

P11 commitment-irreversibility supplies the substrate-side directionality of becoming: events have a forward/reverse binary distinction; commitments are irreversible. P11 alone does not supply P09 phase content. P09 supplies continuous $U(1)$ polarity at channels.

A P11 commitment event at substrate locus $\ell$ actualizes one particular outcome from prior substrate content. The newly-created chain content at the commitment event has some P09 phase $\pi_C(e_{\mathrm{new}})$ — this is the chain-arrow phase per Memo_ED_ChainArrowChirality §3.3.

The substrate-graph question: **what determines $\pi_C(e_{\mathrm{new}})$ at the moment of creation?**

Two sources are structurally distinguishable:

**Source A: upstream chain content via P05 transport.** For an existing chain commitment event $e_n$ (not a new-chain spawn), P05 polarity-transport along the chain edge from $e_{n-1}$ to $e_n$ supplies $\pi_C(e_n)$. The chain's phase persists from upstream. Existing-chain commitment events are not the subject of this memo.

**Source B: substrate-side phase content at the commitment locus.** For a *newly-created* chain (no upstream content), there is no $e_{n-1}$ to inherit from via P05. The initial $\pi_C(e_{\mathrm{new}})$ must come from substrate-side phase content available at locus $\ell$ at the time of the commitment event.

The baryogenesis-relevant case is Source B: the post-SCBU saturation regime is precisely the substrate cosmic phase where chains are being newly-created en masse from the post-boundary substrate state (Paper_ED_CCC §3.7 ignition regime). Established chain populations carrying their own phase content do not yet exist.

So: **what substrate-side phase content is available at $\ell$ for new-chain commitment events to inherit?**

---

## §3 Substrate-side phase content available at a post-SCBU locus

Three candidate substrate-side phase contents at locus $\ell$ in the saturation regime:

**(i) Kernel-arrow phase $\pi_K(\ell)$.** Per Paper_093 T18, the kernel-arrow $\sigma_K(\ell)$ is the V1 retarded-support direction at $\ell$, and per Memo_ED_ChainArrowChirality §3.3, $\sigma_K$ has an associated P09 phase representation $\pi_K(\ell)$. This is the substrate's primary directional-phase content.

**(ii) V5 cross-boundary memory content.** Per Paper_ED_CCC §3.4 (twistor mass-conservation ↔ V5 cross-boundary memory identification), V5 carries pre-boundary substrate content across the SCBU boundary. If V5 cross-boundary content has phase structure, it supplies an additional substrate-side phase reference at post-boundary loci.

**(iii) Local ED-gradient noise / residual inhomogeneity.** The post-boundary substrate is *approximately* homogeneous (Paper_ED_CCC §3.6 + SC-4.x scale-collapse) but the ignition regime is structurally non-stationary. Substrate-graph noise — small ED-gradient fluctuations, residual content from boundary scale-collapse — could supply locally-variable phase content.

**Under strict post-SCBU homogeneity** (Paper_ED_CCC §3.6 + SC-4.x): the substrate has *no local content* distinguishing loci. Under this strict reading:

- $\pi_K$ is globally constant up to a global $U(1)$ choice → available.
- V5 cross-boundary content, if it carries phase information, must also be globally constant by homogeneity → reduces to a global phase contribution, possibly redundant with the global $U(1)$ choice of $\pi_K$.
- Local ED-gradient noise must be zero by homogeneity.

**Strict homogeneity therefore leaves $\pi_K$ as the unique locally-available phase reference at substrate loci.** Newly-created chains have no other phase to inherit from. **$\pi_{\mathrm{commit}}(\ell) = \pi_K(\ell)$ is the only available assignment.** This is Outcome (1): derivable from existing primitives via the strict-homogeneity reading.

**Under realistic ignition-regime non-stationarity** (Paper_ED_CCC §3.7 explicitly describes the ignition phase as non-stationary): strict homogeneity holds asymptotically as the boundary is approached but the ignition regime itself has structural non-stationarity. Local ED-gradient noise + V5 cross-boundary residual content + quantum fluctuations all may supply small deviations from $\pi_K$ as the substrate phase reference at $\ell$.

Under this realistic reading: $\pi_{\mathrm{commit}}(\ell) \approx \pi_K(\ell)$ with small deviations. The deviations are substrate-graph-bounded by the scale of post-boundary inhomogeneity, which is itself bounded by SC-4.x scale-collapse content. **Approximately-$\pi_K$ inheritance with small deviations.** This is Outcome (2): strongly natural, with the magnitude of deviations themselves structurally bounded by existing primitives.

---

## §4 The strongest substrate-graph argument

The cleanest argument for $\pi_{\mathrm{commit}} = \pi_K$ uses the following chain:

1. **P09 supplies $U(1)$ phase at channels.** Continuous, no preferred values.
2. **Paper_093 T18 identifies kernel-arrow $\sigma_K$ with V1 retarded-support direction at substrate locus.** Direction has an associated P09 phase $\pi_K$.
3. **Paper_089 T18 establishes V1 is strictly retarded** (advanced V1 refuted by P11). This means substrate-side propagation has a forward direction *forced* by P11.
4. **The substrate-side "forward" direction is structurally identified with the kernel-arrow direction** per (2) + (3): P11 forward direction ↔ V1 retarded support direction ↔ kernel-arrow direction.
5. **A P11 commitment event creates new chain content in the substrate's forward direction** (by P11 commitment-irreversibility definition). The newly-created chain content propagates forward via V1 from the commitment event.
6. **The chain-arrow direction of the new chain is the forward direction at the commitment locus.** This is the V1 retarded-support direction. This is the kernel-arrow direction.
7. **The P09 phase of the chain-arrow direction at creation IS the P09 phase of the kernel-arrow direction at the locus:** $\pi_C(e_{\mathrm{new}}) = \pi_K(\ell)$ by (6) + the P09 phase being attached to substrate-graph directional structure.
8. Therefore $\chi_C(e_{\mathrm{new}}) = \pi_C - \pi_K = 0$ by (7).

**Where the argument is strong:** steps 1–6 are direct inheritances from existing primitives + corpus content (P09, P11, Paper_089 T18, Paper_093 T18, Memo_ED_ChainArrowChirality).

**Where the argument leans:** step 7 requires that "P09 phase attached to substrate directional structure" is a *meaningful identification* — that there is a well-defined map from substrate-graph directions to P09 phases, and that this map is the same for the chain-arrow of a new chain and the kernel-arrow at the same locus. This identification is already used implicitly in Memo_ED_ChainArrowChirality §3.3 to define $\chi_C$ (which compares two phase-representations at the same locus), so it's not novel — but its strict form here (chain-arrow phase EQUALS kernel-arrow phase at creation) goes one step beyond.

**Honest reading of step 7:** it follows from steps 1–6 *under the strict-homogeneity assumption* that the locus has no phase content other than $\pi_K$. Without strict homogeneity, step 7 is approximately true (the dominant substrate-side phase reference is $\pi_K$, but small deviations are possible).

---

## §5 IDENTIFIED vs OPEN

### IDENTIFIED in this memo:

- **Under strict post-SCBU homogeneity, $\pi_{\mathrm{commit}}(\ell) = \pi_K(\ell)$ follows from existing primitives** (P09 + P11 + Paper_089 T18 + Paper_093 T18) at D-via-I composition level. The chain-arrow direction of a new chain at the commitment event IS the kernel-arrow direction at the locus, and the P09 phase representations of those two directions are the same.
- **The new-chain default chirality is $\chi_C = 0$** under the strict-homogeneity reading. Anti-aligned chains ($\chi_C = \pi$) require substrate work to invert the natural commitment phase, supplying the asymmetric admission cost in the saturation regime.
- **The substrate-side mechanism is structurally clean and uses no new primitives or postulates** under the strict reading.

### OPEN:

- **Whether strict post-SCBU homogeneity holds in the ignition regime is itself partially OPEN.** The ignition regime is explicitly non-stationary per Paper_ED_CCC §3.7 — substrate event-density climbing rapidly toward saturation — but the substrate may still be globally homogeneous in P09 phase content even while being non-stationary in other respects. **Substrate-graph clarification of which substrate-side properties are strictly homogeneous vs only approximately homogeneous in the ignition regime is itself a substrate-research-frontier question.**
- **V5 cross-boundary memory phase content** — Paper_ED_CCC §3.4 identifies the twistor mass-conservation integral with V5 cross-boundary memory, but does not specify whether V5 cross-boundary content carries P09 phase information at substrate-graph level. If it does, V5 cross-boundary phase could supply an additional substrate-side phase reference competing with $\pi_K$. **OPEN.**
- **Quantitative substrate-graph derivation of the asymmetric-admission magnitude.** Even with $\pi_{\mathrm{commit}} = \pi_K$ derivable, the substrate-graph cost difference between $\chi_C = 0$ (default) and $\chi_C = \pi$ (inverted) commitment events in the saturation regime is not constructed quantitatively. Would determine $\eta_B$ derivation; currently INHERITED.

### Three-outcome classification (per memo brief):

- **(1) Derivable (D-via-I):** YES under strict post-SCBU homogeneity — the chain in §4 (steps 1–8) composes existing primitives + corpus content cleanly. Strict reading supplies the closure.
- **(2) Not derivable but strongly natural (candidate postulate):** YES under realistic ignition-regime non-stationarity — the $\pi_{\mathrm{commit}} \approx \pi_K$ reading is structurally clean; deviations are bounded by SC-4.x scale-collapse content; the substrate-graph mechanism is the natural one and a tightening postulate (P-CommitPhaseInheritance: "$\pi_{\mathrm{commit}} = \pi_K$ at substrate-graph level in the post-SCBU ignition regime") would be minimal and well-motivated.
- **(3) Clearly not supported:** NO — the argument in §4 is structurally substantive, not handwaving. The hypothesis is well-supported by existing primitives; the only question is whether the support is strict (Outcome 1) or strong-but-not-strict (Outcome 2).

**Net result: between Outcome (1) and Outcome (2), depending on which homogeneity reading applies to the ignition regime.**

---

## §6 Verdict + recommended next exploration

**Verdict.** The hypothesis $\pi_{\mathrm{commit}} = \pi_K$ is **strongly supported by existing primitives** — substantially stronger than the substrate-graph closures attempted for binary admission (Memo_ED_BinaryChirality, where all three reduction paths failed). The chain in §4 composes P09 + P11 + Paper_089 T18 + Paper_093 T18 + post-SCBU homogeneity to produce the inheritance result. The only weak link is whether post-SCBU homogeneity is strict or only approximate in the ignition regime — a substrate-graph clarification question that is itself partially OPEN but structurally minor.

**Recommended path for Paper_ED_Baryogenesis upgrade:**

Given Outcome (1) / Outcome (2) status, two paths to upgrading the baryogenesis paper M2 → M3:

**Path-A (preferred if strict-homogeneity reading holds):** Update Paper_ED_Baryogenesis_Open to add a new substrate-graph composition row in the audit table — "P-CommitPhaseInheritance derivable from P09 + P11 + Paper_089 T18 + Paper_093 T18 + Paper_ED_CCC §3.6 + §3.7 strict homogeneity" labeled D-via-I. Asymmetric admission cost row (currently OPEN row 12 in baryogenesis audit table) closes to D-via-I via the production-side mechanism. Verdict upgrades **M2 → M3 form-IDENTIFIED**. P-BinaryAdmission remains as the only paper-specific postulate.

**Path-B (if strict-homogeneity reading is contested):** Declare **P-CommitPhaseInheritance** as a second paper-specific postulate in Paper_ED_Baryogenesis alongside P-BinaryAdmission. Verdict remains M2 but with two postulates instead of one. Honest framing: "$\pi_{\mathrm{commit}} = \pi_K$ at substrate-graph level under post-SCBU homogeneity; substrate-graph closure of the strict-vs-approximate homogeneity reading OPEN; declared as postulate pending closure." Strictly weaker than current single-postulate M2.

**Recommended:** attempt Path-A first. The strict-homogeneity argument in §4 is structurally substantive. If Claude-B-class audit accepts the strict-homogeneity reading as substrate-graph derivable, baryogenesis paper upgrades cleanly. If audit pushes back on the strict reading, fall back to Path-B.

**Alternative directions (per Memo_ED_Baryogenesis_NextExplorations):**

- **Direction 2 (T17 bundle extension)** — addresses binary admission (P-BinaryAdmission OPEN), not the asymmetric admission addressed in this memo. Independent route; remains worth attempting separately.
- **Direction 3 (P05 holonomy)** — also binary admission. Independent.
- **Closing this memo's outcome plus Direction 2 or 3 would together close both OPEN items in baryogenesis** — chirality binary admission and asymmetric admission cost — upgrading the paper to fully M3 form-IDENTIFIED with zero paper-specific postulates. That would be the cleanest research-program outcome.

**Non-restrictive note.** This memo's exploration arrives at a stronger result than Memo_ED_KernelArrowAsymmetry suggested. The kernel-arrow asymmetry route, attacked at the commitment-event creation step, has a clean substrate-graph reading under existing primitives. The cleanness depends on the strict-homogeneity reading of the post-SCBU ignition regime — a substrate-graph clarification worth pursuing in its own right but not load-bearing for the asymmetric admission mechanism itself.

---

**End Memo_ED_CommitPhaseInheritance.**
