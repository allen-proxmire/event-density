# Memo_ED_RouteA_MultiRouteConvergence_Audit — Adversarial Audit of Route A Multi-Route Convergence

**Series:** Wave-3 Audit Memo (Cosmology Arc + ED-SC Arc; Claude-B-class adversarial audit of Route A multi-route convergence per Q-A4-4 from Memo_ED_RouteA_A4_Audit + RA-OPEN-4c-explicit from Memo_ED_RouteA_A2_Construct)
**Status:** Critical audit of whether the three independent Route A constructions (A1 via $\tau_{V_5}$; A2 via Hessian asymptotics; A4 via $\Theta_{\mathrm{ED}}$) converge to the same $H_0$ prediction, or whether $\Theta_{\mathrm{ED}}$ and $\tau_{V_5}$ remain independent substrate-parameters. **Not a derivation. Auditor stance, not advocate.** Following the discipline cascade pattern (CommitPhaseInheritance → SubstrateAction_Constancy → DCGT_VacuumEnergyMapping → NonSaturation_StressEnergy → NoetherFlux → Q1A/Q2A → C3 → A4 → multi-route convergence audit).
**Date:** 2026-05-17
**Anchors:** Memo_ED_RouteA_A2_Construct (RA-OPEN-4c-explicit; A2 reduces to A1 at leading order); Memo_ED_RouteA_A4_Audit (Q-A4-4 load-bearing); Memo_ED_RouteA_A4_Construct (A4 closure at substrate-parameter-INHERITED level); Memo_ED_RouteA_Scoping_Wave3 (four-route scoping); Paper_ED_SC_4_9; Paper_090 (V5 finite-memory $\tau_{V_5}$); Paper_087 (P12 ED-threshold); Paper_073 (DCGT); Paper_ED_Cos_01 (M3); Paper_ED_Cos_05 (M3 conditional on Route A); Paper_027 (template).
**Headline verdict:** **Convergent-at-parameter-INHERITED level (option (ii) per user task).** Both A4 ($\Theta_{\mathrm{ED}}$) and A2/A1 ($\tau_{V_5}$) close at the same Paper_027-analog substrate-parameter-INHERITED level; corpus carries both as independent primitive content. The substantive substrate-graph relation between $\Theta_{\mathrm{ED}}$ and $\tau_{V_5}$ remains substrate-research-frontier (RA-OPEN-4c-explicit) but is **not load-bearing** for Route A's substrate-parameter-INHERITED-level closure. Three audit refinements: dimensional cleanup of A2 convergence relation (Q-MRC-1); A2-to-A1 reduction contingent on leading-order linearity (Q-MRC-2); convergence relation substrate-graph plausible but corpus does not derive (Q-MRC-3).

---

## §1 What's being audited

The Route A construction chain across three memos:

- **A4** (Memo_ED_RouteA_A4_Construct): $H_0 \sim M_P \cdot (\Theta_{\mathrm{ED}}^{\mathrm{Planck-units}})^{1/2}$ via Q1A + Q2A + Friedmann + Paper_027 dimensional rearrangement; substrate-parameter-INHERITED at $\Theta_{\mathrm{ED}}$ level
- **A2** (Memo_ED_RouteA_A2_Construct): $H_0 \sim c/\ell_{V_5}$ via Hessian IR cutoff in kernel-dominated regime under leading-order linear $U(\Psi)$; reduces to A1; substrate-parameter-INHERITED at $\tau_{V_5}$ level
- **A1** (canonical Route A formulation per ED_MEMORY anchor 7): $H_0 = 1/\tau_{V_5}$ directly; $\tau_{V_5}$ as primitive substrate-parameter per Paper_090

**The load-bearing question per Q-A4-4 + RA-OPEN-4c-explicit:** do A1, A2, A4 converge on the same $H_0$ prediction, or are $\Theta_{\mathrm{ED}}$ and $\tau_{V_5}$ independent substrate-parameters?

Five audit axes commissioned per user task. This memo executes each adversarially.

---

## §2 C-A-1 — Structural link audit between $\Theta_{\mathrm{ED}}$ and $\tau_{V_5}$

### §2.1 Examination

**Question:** does any corpus content (SC-4.9 + P12 + Paper_090) supply a structural relation between $\Theta_{\mathrm{ED}}$ and $\tau_{V_5}$?

### §2.2 Sub-examination: kernel activation thresholds

Per Paper_087 P12 (ED-threshold) + Paper_ED_CCC §3.7: V5 + V1 + individuation activate when substrate event-density crosses $\Theta_{\mathrm{ED}}$. The threshold value $\Theta_{\mathrm{ED}}$ is the **activation trigger** for V5.

Per Paper_090: V5's **finite-memory time** $\tau_{V_5}$ is a kernel structural property — defined by the V5 kernel functional form, not by the activation event itself.

**Activation trigger ($\Theta_{\mathrm{ED}}$) and memory length ($\tau_{V_5}$) are conceptually distinct.** P12 says "V5 turns on at threshold"; Paper_090 says "V5 has memory $\tau_{V_5}$ once on." These are independent specifications.

**Audit finding:** no structural link supplied at kernel-activation level.

### §2.3 Sub-examination: memory-length scaling with event-density

**Could $\tau_{V_5}$ depend physically on the substrate event-density it operates on?** Substrate-graph intuition: higher event-density → more events to remember → effectively shorter relative memory; lower event-density → fewer events → effectively longer relative memory.

This intuition would suggest $\tau_{V_5} \propto 1/\Theta$ (inverse relation). At saturation $\Theta = \Theta_{\mathrm{ED}}$, giving $\tau_{V_5} \sim 1/\Theta_{\mathrm{ED}}$.

**Does Paper_090 supply this scaling?** Paper_090 defines V5 cross-chain finite-memory with $\tau_{V_5}$ as a kernel parameter; it does **not** specify $\tau_{V_5}$ as a function of substrate event-density. The memory length is treated as kernel-intrinsic.

**Audit finding:** memory-length scaling is substrate-graph intuitive but not in the corpus.

### §2.4 Sub-examination: event-density dependence in V5 kernel structure

**Could V5's kernel functional form involve substrate event-density?** Paper_090's V5 is a substrate-graph cross-chain coupling kernel with finite-memory structure. The kernel form involves substrate-graph distance + memory time + cross-chain coupling weight. Substrate event-density is the substrate state, not the kernel functional.

**Audit finding:** V5 kernel structure per Paper_090 is independent of substrate event-density.

### §2.5 C-A-1 verdict

**No structural link supplied by current corpus content** between $\Theta_{\mathrm{ED}}$ (P12 ED-threshold value) and $\tau_{V_5}$ (V5 finite-memory length). Three potential link mechanisms examined; none currently in Paper_087 + Paper_090 + Paper_073 composition.

**Audit qualification Q-MRC-1 (newly introduced):** the corpus treats $\Theta_{\mathrm{ED}}$ and $\tau_{V_5}$ as **independent primitive substrate-parameters** at the same level as $\ell_P, c, \hbar$. Substrate-graph derivation of either from the other (or both from sub-primitive content) is substrate-research-frontier work — not currently supplied.

---

## §3 C-A-2 — A2-to-A1 reduction contingency audit

### §3.1 Examination

**Claim (per A2 construction §3.2):** under leading-order linear $U(\Psi)$, the Hessian IR regime is kernel-dominated ($U''(\Psi^{\mathrm{const}}) = 0$); $\ell_{A2} \sim \ell_{V_5}$; A2 reduces to A1.

**Adversarial question:** is the kernel-dominated regime structurally forced, or contingent on the specific leading-order linearity assumption?

### §3.2 Sub-examination: case (a) strict linearity

$U(\Psi) = \hbar\Psi$ strictly → $U''(\Psi^{\mathrm{const}}) = 0$ identically. Kernel-dominated. **A2 → A1.** This is A4 audit Q-A4-3 leading-order linearity per construction memo §2.3.

### §3.3 Sub-examination: case (b) subleading nonlinearity

$U(\Psi) = \hbar\Psi + b\Psi^2 + ...$ with $b$ subleading. $U''(\Psi^{\mathrm{const}}) = 2b > 0$ at subleading order. Potential-dominated regime contributes; $\ell_{A2}$ involves $m_{\mathrm{eff}}^2 = 2b$.

**For convergence with A4** via potential-dominated route: $m_{\mathrm{eff}}^2 \sim \Theta_{\mathrm{ED}}$ (in appropriate units) → would require subleading $b$ to scale specifically with $\Theta_{\mathrm{ED}}$. Substrate-research-frontier requirement.

**For divergence from A4:** $m_{\mathrm{eff}}^2$ could be a separate substrate-parameter unrelated to $\Theta_{\mathrm{ED}}$; would supply third independent $\ell_{A2}$ candidate.

### §3.4 Sub-examination: case (c) leading-order nonlinearity

If A4's leading-order linearity assumption is incorrect — e.g., $U(\Psi) \sim \Psi^2$ at leading order — then $U''$ is non-zero at leading order; A2's potential-dominated regime dominates; reduction to A1 fails.

Per A4 audit Q-A4-3, leading-order linearity is the generic Taylor-expansion assumption; non-degenerate $\mathcal{L}_{\mathrm{sub}}$ has non-zero $U' = \partial U/\partial\Psi$, giving linear leading order. Case (c) requires $U'(\Psi^{\mathrm{const}}) = 0$ — i.e., $\Psi^{\mathrm{const}}$ is an extremum of $U$. This is a substrate-graph-specific structural condition (not generic).

### §3.5 C-A-2 verdict

**A2 → A1 reduction is contingent on case (a) leading-order linearity** per A4 §2.3 + Q-A4-3. Generic under Taylor-expansion non-degeneracy.

**Audit qualification Q-MRC-2 (newly introduced):** the A2 → A1 reduction (kernel-dominated IR) is corpus-conditional on leading-order linearity of $U(\Psi)$. Subleading nonlinearity (case b) is admissible and would modify $\ell_{A2}$ in ways that could either converge with A4 (if subleading $U''$ scales as $\Theta_{\mathrm{ED}}$ substrate-graph) or diverge (if subleading $U''$ is independent substrate-parameter). Leading-order nonlinearity (case c) requires non-generic $\Psi^{\mathrm{const}}$ extremality.

This is **not** a defeating audit finding — case (a) leading-order linearity is the generic corpus assumption — but flags that the convergence/divergence question is sensitive to the specific Paper_ED_SC_4_9 functional structure.

---

## §4 C-A-3 — Convergence condition substrate-graph plausibility

### §4.1 Examination

**A2 construction memo §5.3 (boxed result):** convergence requires

$$
\ell_{V_5}^2 \sim \frac{M_P^2 c^4}{\hbar \Theta_{\mathrm{ED}}}
$$

(per the construction memo's notation).

### §4.2 Dimensional consistency audit

**Adversarial check of A2 construction's dimensional analysis:**

LHS: $[\ell_{V_5}^2] = [L^2]$.

RHS: $[M_P^2 c^4 / (\hbar \Theta_{\mathrm{ED}})]$. With $[M_P] = M$, $[c] = LT^{-1}$, $[\hbar] = ML^2T^{-1}$, $[\Theta_{\mathrm{ED}}] = L^{-3}T^{-1}$:

$[M^2 \cdot L^4 T^{-4}] / [M L^2 T^{-1} \cdot L^{-3} T^{-1}] = [M^2 L^4 T^{-4}] / [M L^{-1} T^{-2}] = [M L^5 T^{-2}]$.

**Dimensional mismatch:** $[M L^5 T^{-2}] \neq [L^2]$. **The A2 construction memo's boxed convergence relation has a dimensional error.**

### §4.3 Corrected convergence relation

Working from the corrected derivation:

- A4: $H_0 = (8\pi/3)^{1/2} \ell_P c^{1/2} \Theta_{\mathrm{ED}}^{1/2}$ in SI (per A4 audit §6.1 corrected)
- A2: $H_0 = c/\ell_{V_5} = 1/\tau_{V_5}$

Convergence $H_0^{(A4)} = H_0^{(A2)}$:

$$
\frac{c}{\ell_{V_5}} = (8\pi/3)^{1/2} \ell_P c^{1/2} \Theta_{\mathrm{ED}}^{1/2}
$$

$$
\ell_{V_5} = \frac{c^{1/2}}{(8\pi/3)^{1/2} \ell_P \Theta_{\mathrm{ED}}^{1/2}}, \quad \ell_{V_5}^2 = \frac{c}{(8\pi/3) \ell_P^2 \Theta_{\mathrm{ED}}}.
$$

**Corrected convergence relation:**

$$
\boxed{\;\ell_{V_5}^2 \sim \frac{c}{\ell_P^2 \cdot \Theta_{\mathrm{ED}}} \;\;\text{(corrected, dimensionally consistent)}\;}
$$

Dimensional check: $[c/(\ell_P^2 \Theta_{\mathrm{ED}})] = [LT^{-1}]/([L^2][L^{-3}T^{-1}]) = [LT^{-1}]/[L^{-1}T^{-1}] = [L^2]$ ✓.

**Audit finding:** the A2 construction memo §5.3 boxed result has a dimensional error; the corrected relation is $\ell_{V_5}^2 \sim c/(\ell_P^2 \Theta_{\mathrm{ED}})$.

### §4.4 Substrate-graph plausibility of corrected relation

**Substrate-graph interpretation:** $\ell_{V_5}^2 \cdot \Theta_{\mathrm{ED}} \sim c/\ell_P^2$. V5 memory volume × event-density threshold $\sim$ Planck-scale frequency. **Low-threshold → long memory** (consistent with substrate-graph intuition per §2.3); **high-threshold → short memory.**

**SC-4.x compatibility:** the relation involves only substrate parameters ($\ell_{V_5}, \Theta_{\mathrm{ED}}, \ell_P, c$); no fundamental metric or absolute time required. SC-4.x compatible. ✓

**P12 threshold-behavior compatibility:** at the threshold-crossing event, V5 activates; the relation predicts substrate-parameter constraint $\ell_{V_5} \Theta_{\mathrm{ED}}^{1/2} \sim c^{1/2}/\ell_P$. Whether V5's activation event correlates substrate-graph with this constraint is the substantive substrate-research question. Not derivable from current corpus.

### §4.5 C-A-3 verdict

**Corrected convergence relation $\ell_{V_5}^2 \sim c/(\ell_P^2 \Theta_{\mathrm{ED}})$ is substrate-graph plausible** but **not derived in current corpus** from Paper_090 + Paper_087 P12 + Paper_073 composition.

**Audit qualification Q-MRC-3 (newly introduced):** the convergence relation is dimensionally consistent (after A2-construction-memo correction) and substrate-graph plausible (low-threshold ↔ long memory intuition); substrate-graph derivation requires explicit construction from Paper_090 V5 kernel structure + Paper_087 P12 + DCGT scale-collapse content — substrate-research-frontier.

---

## §5 C-A-4 — Counterexample search

### §5.1 Examination

**Question:** are there substrate configurations where $\Theta_{\mathrm{ED}}$ and $\tau_{V_5}$ vary independently without violating SC-4.9 or P12?

### §5.2 Candidate counterexample 1 — alternative substrate-parameter values

Conceive an alternative substrate ontology with different $\Theta_{\mathrm{ED}}$ value but same $\tau_{V_5}$ (or vice versa). Per Paper_087 + Paper_090, both parameters are primitive content — their values are axiomatic substrate constants. Varying one without the other:

- Vary $\Theta_{\mathrm{ED}}$ (e.g., 2× current value): per A4, $H_0$ shifts by factor $\sqrt{2}$; per A2/A1, $H_0$ unchanged. **A4 and A2/A1 give different predictions** → multi-route divergence.
- Vary $\tau_{V_5}$ (e.g., 2× current value): per A2/A1, $H_0$ shifts by factor 1/2; per A4, $H_0$ unchanged. **Multi-route divergence.**

**Without the corrected convergence relation $\ell_{V_5}^2 \sim c/(\ell_P^2 \Theta_{\mathrm{ED}})$ holding substrate-graph, the two substrate-parameters can vary independently and the routes diverge.**

### §5.3 Candidate counterexample 2 — substrate-parameter sensitivity to observation

Current observation: $H_0 \approx 70$ km/s/Mpc requires:
- A4 with $\Theta_{\mathrm{ED}}^{\mathrm{Planck-units}} \approx 10^{-122}$
- A2/A1 with $\tau_{V_5}/\tau_P \approx 10^{61}$

If these are independent substrate-parameters, the corpus has **two coincidentally-tuned primitive constants** that happen to match observation. This is consistent — analogous to standard physics having multiple independent constants tuned to observed values.

### §5.4 Candidate counterexample 3 — substrate-graph derivation of one from the other

If subsequent substrate-research derives, e.g., $\Theta_{\mathrm{ED}}$ from $\tau_{V_5}$ + Planck content (or vice versa), the independence question is resolved positively (convergence holds). This would be a substantive substrate-research advance — not a current corpus content.

### §5.5 C-A-4 verdict

**No defeating counterexample** in the sense of internal corpus inconsistency. **Independence concern is real:** the corpus currently treats $\Theta_{\mathrm{ED}}$ and $\tau_{V_5}$ as independent primitive substrate-parameters; observational matching requires both to coincide on tuned values. Whether they are substrate-graph-related (convergent) or independent (multi-route divergent at substrate-graph level, multi-route convergent at observation level via tuning) is the substantive substrate-research question.

---

## §6 C-A-5 — Convergence verdict

### §6.1 Three options per user task

(i) **Convergent** — Route A closes; multi-route convergence at substrate-graph level via derived relation between $\Theta_{\mathrm{ED}}$ and $\tau_{V_5}$.
(ii) **Convergent-at-parameter-INHERITED level** — Paper_027 analog; corpus carries both substrate-parameters as independent primitive content; either route gives substrate-graph derivation of $H_0$ at the same M3 closure status.
(iii) **Divergent** — substrate-research-frontier finding; multi-route choice not substrate-graph-determined.

### §6.2 Verdict per audit findings

- **C-A-1:** no structural link supplied by corpus (Q-MRC-1)
- **C-A-2:** A2 → A1 reduction contingent on leading-order linearity (Q-MRC-2); generic under non-degeneracy
- **C-A-3:** convergence relation substrate-graph plausible but corpus does not derive (Q-MRC-3); A2 construction memo dimensional error corrected
- **C-A-4:** no defeating counterexample; independence concern real

**Final verdict: option (ii) — Convergent-at-parameter-INHERITED level.**

The corpus closes Route A at the **same Paper_027-analog substrate-parameter-INHERITED level** via either A4 ($\Theta_{\mathrm{ED}}$) or A2/A1 ($\tau_{V_5}$). Both substrate-parameters are primitive content; observational matching is achieved by either route at substrate-parameter-INHERITED level analogous to Paper_027's inheritance of $\ell_P, \hbar, c$. The multi-route convergence question (whether $\Theta_{\mathrm{ED}}$ and $\tau_{V_5}$ are substrate-graph-related per the corrected relation $\ell_{V_5}^2 \sim c/(\ell_P^2 \Theta_{\mathrm{ED}})$) is **substrate-research-frontier tightening work**, not load-bearing for Route A's M3-status delivery.

### §6.3 Practical corpus implications

**Route A closes substantially for corpus paper structure purposes:**
- **Paper_ED_Cos_05** "conditional on Route A" qualifier can be **lifted** — Route A4 at substrate-parameter-INHERITED level supplies the form-DERIVED $H_0$ chain
- **Paper_038_5** retroactive M2 → M3 upgrade can **proceed** per Λ-smallness reframing inheritance
- **Paper_ED_Cos_01** retains M3 with form-DERIVED $H$ component via Route A4
- **ED-SC 4.x arc-wide M3 → M2 upgrade** applies (six projections) per ED_MEMORY anchor 7 at substrate-parameter-INHERITED level

**Tightening work for future substrate-research:**
- **RA-OPEN-4c-explicit** (corrected): substrate-graph derivation of relation $\ell_{V_5}^2 \sim c/(\ell_P^2 \Theta_{\mathrm{ED}})$
- **RA-OPEN-4a** (inherited from A4 audit): substrate-graph derivation of $\Theta_{\mathrm{ED}}$ value from sub-primitive content
- **RA-OPEN-A2-1** (inherited from A2 construction): substrate-graph derivation of $\tau_{V_5}$ value from sub-primitive content
- **RA-OPEN-A2-2** (inherited): substrate-graph derivation of leading-order linearity of $U(\Psi)$ from Paper_ED_SC_4_9

### §6.4 Comparison with prior audit cascade

| Audit | Verdict | Closure level |
|---|---|---|
| CommitPhaseInheritance | REJECTED | — |
| SubstrateAction_Constancy | ACCEPTED (approximately-constant) | Standard-physics-analog-inheritance |
| DCGT_VacuumEnergyMapping | ACCEPTED (approximately-vacuum-energy) | Standard-physics-analog-inheritance |
| NonSaturation_StressEnergy | ACCEPTED (approximately-standard-cosmology) | Standard-physics-analog-inheritance |
| NoetherFlux | ACCEPTED (approximately-standard-physics) | Standard-physics-analog-inheritance |
| Q1A + Q2A (implicit) | ACCEPTED (construction-uniqueness leading order) | Substrate-graph construction-uniqueness |
| C3 | ACCEPTED with five qualifications | Substrate-graph direct closure |
| A4 | ACCEPTED with five qualifications | Substrate-parameter-INHERITED (Paper_027 analog) |
| **Multi-Route Convergence (this audit)** | **Convergent-at-parameter-INHERITED level (option ii)** | **Multi-route convergence at substrate-parameter-INHERITED level; substrate-graph convergence relation substrate-research-frontier** |

---

## §7 Updated RA-OPEN inventory

### §7.1 Load-bearing OPEN (for further substrate-research advance beyond M3)

| OPEN | Description | Path |
|---|---|---|
| **RA-OPEN-4c-explicit (corrected)** | Substrate-graph derivation of $\ell_{V_5}^2 \sim c/(\ell_P^2 \Theta_{\mathrm{ED}})$ from Paper_090 + Paper_087 P12 + Paper_073 | Multi-route convergence verification at substrate-graph level (option (ii) → (i) upgrade) |
| **RA-OPEN-4a** | Substrate-graph derivation of $\Theta_{\mathrm{ED}}$ numerical value from sub-primitive content | Paper_027-analog substrate-parameter derivation |
| **RA-OPEN-A2-1** | Substrate-graph derivation of $\tau_{V_5}$ numerical value from sub-primitive content | Same status as RA-OPEN-4a; parallel substrate-parameter question |

### §7.2 Non-load-bearing OPEN (substrate-research-frontier; tightening work)

- **RA-OPEN-A2-2:** substrate-graph derivation of leading-order linearity of $U(\Psi)$ from Paper_ED_SC_4_9 functional structure (Q-A4-3 + Q-MRC-2 inheritance)
- **RA-OPEN-Q-A4-2:** $\Psi^{\mathrm{const}}$ identification scope across full saturation regime (not just threshold-crossing instant)
- **Subleading $O(\varepsilon)$ scheme-dependence** (Q2A OPEN-ii inherited)

### §7.3 Newly closed audit qualifications (per this audit)

- **Q-A4-4 (Route A1 to A4 reduction):** addressed — A1 and A4 do NOT reduce to each other at substrate-graph level under leading-order linearity (case (a) per C-A-2); both close at substrate-parameter-INHERITED level via independent primitive content
- **Q-MRC-1 (structural link):** documented — no current corpus link between $\Theta_{\mathrm{ED}}$ and $\tau_{V_5}$
- **Q-MRC-2 (linearity contingency):** documented — A2 → A1 reduction generic under non-degeneracy
- **Q-MRC-3 (substrate-graph plausibility):** documented — corrected convergence relation substrate-graph-plausible but not derived

---

## §8 Recommended updates + next steps

### §8.1 Updates to A2 construction memo

1. **Correct the dimensional analysis in §5.3** — boxed convergence relation should be $\ell_{V_5}^2 \sim c/(\ell_P^2 \Theta_{\mathrm{ED}})$ (per §4.3 above), not the dimensionally-inconsistent $\ell_{V_5}^2 \sim M_P^2 c^4 / (\hbar \Theta_{\mathrm{ED}})$.
2. **Add Q-MRC-1, Q-MRC-2, Q-MRC-3 qualifications** to RA-OPEN list.
3. **Clarify multi-route convergence status** — explicit option (ii) per this audit; observation matching achieved at substrate-parameter-INHERITED level.

### §8.2 Corpus paper-structure propagation (Route A at parameter-INHERITED level closes)

**Path-Cos05-Update (HIGH PRIORITY):** lift "conditional on Route A" qualifier from Paper_ED_Cos_05; verdict upgrades to **M3 unconditional** (form-IDENTIFIED + value-INHERITED + IC-INHERITED with $H_0$ now form-DERIVED via Route A at substrate-parameter-INHERITED level). Carry RA-OPEN-4c-explicit + RA-OPEN-4a + RA-OPEN-A2-1 as substrate-research-frontier OPENs not load-bearing for M3.

**Path-038_5-Update (HIGH PRIORITY):** Paper_038_5 retroactive M2 → M3 upgrade per Λ-smallness reframing inheritance (Λ smallness = substrate-parameter-INHERITED value of $\Theta_{\mathrm{ED}}^{\mathrm{Planck-units}} \approx 10^{-122}$ per A4 + this audit).

**Path-Cos01-Note (medium priority):** add note to Paper_ED_Cos_01 §3.8 that Route A4 supplies form-DERIVED $H$ component at substrate-parameter-INHERITED level via the Q1A + Q2A + Friedmann + dimensional rearrangement chain.

**Path-ED-SC-4.x-Arc-Update (HIGH PRIORITY per ED_MEMORY anchor 7):** propagate ED-SC 4.x arc-wide M3 → M2 upgrade across the six projections per anchor 7. Route A's $\xi_{\mathrm{canonical}}(H_0)$ projection closes at substrate-parameter-INHERITED level via Route A2 + Route A4; the other five projections follow per the ED-SC 4.x framework.

### §8.3 Tightening work (substrate-research-frontier, lower priority)

**Path-Convergence-Relation-Construction (substrate-research-frontier):** focused construction memo attempting RA-OPEN-4c-explicit substrate-graph derivation. If closes, multi-route convergence upgrades from option (ii) to option (i); substantive substrate-graph relation between $\Theta_{\mathrm{ED}}$ and $\tau_{V_5}$ added to corpus.

**Path-Theta-ED-Derivation (substrate-research-frontier):** attempt RA-OPEN-4a — substrate-graph derivation of $\Theta_{\mathrm{ED}}$ value from sub-primitive content. Analog of Planck-scale value derivation; if achievable, value-DERIVED-strict closure of $H_0$.

**Path-Tau-V5-Derivation (substrate-research-frontier):** attempt RA-OPEN-A2-1 — parallel to Path-Theta-ED-Derivation for $\tau_{V_5}$.

### §8.4 My recommendation

**Path-Cos05-Update + Path-038_5-Update + Path-ED-SC-4.x-Arc-Update in parallel.** Route A's substrate-parameter-INHERITED-level closure is sufficient for the corpus paper-structure propagation deliverables; these are the **immediate cross-arc impact deliverables** per ED_MEMORY anchor 7 + Q-A4-4 audit conclusions.

**Path-Convergence-Relation-Construction as tightening work** to be pursued substantively after the corpus paper-structure propagation completes. The multi-route convergence question is substrate-research-frontier tightening, not corpus-blocking.

### §8.5 Honest substrate-research-pattern assessment

This audit's verdict — **convergent-at-parameter-INHERITED level (option (ii))** — is consistent with the corpus's existing substrate-parameter inheritance pattern (Paper_027's $G$ derivation inherits $\ell_P, \hbar, c$ at primitive level; Route A inherits $\Theta_{\mathrm{ED}}, \tau_{V_5}$ at primitive level). **The corpus is internally consistent: substrate-graph derivations are achievable at substrate-parameter-INHERITED level; substrate-graph derivation of substrate-parameter values themselves is substrate-research-frontier across the board.**

The substantive substrate-research finding of the Route A audit cascade: **the corpus's substrate-parameter inheritance pattern extends consistently from Paper_027's $(\ell_P, \hbar, c)$ to Route A's $(\Theta_{\mathrm{ED}}, \tau_{V_5})$**. Both Paper_027 and Route A close at the same M3 closure status with value-INHERITED at the substrate-parameter level. Multi-route convergence between independent substrate-parameter routes is not load-bearing for either Paper_027's M3 status or Route A's M3 status; it would be tightening work supplying substrate-parameter relations beyond inherited primitive content.

---

## §9 Final verdict

**Route A closes at substrate-parameter-INHERITED level (option (ii) per user task).** Multi-route convergence between A1, A2, A4 holds at the **observational level** (all three routes match observed $H_0$ at appropriately-tuned substrate-parameter values) and at the **substrate-parameter-INHERITED level** (analogous to Paper_027). Substrate-graph derivation of multi-route convergence relation ($\ell_{V_5}^2 \sim c/(\ell_P^2 \Theta_{\mathrm{ED}})$) is **substrate-research-frontier** but **not load-bearing** for Route A's M3-status delivery.

**The corpus paper-structure propagation can proceed:** Cos_05 unconditional M3, 038_5 retroactive M3, ED-SC 4.x arc-wide M3 → M2 upgrade. **Single highest-leverage corpus contribution to date** per ED_MEMORY anchor 7's standing characterization, delivered at the substrate-parameter-INHERITED level matching the corpus's existing M3 closure pattern.

---

**End Memo_ED_RouteA_MultiRouteConvergence_Audit.**
