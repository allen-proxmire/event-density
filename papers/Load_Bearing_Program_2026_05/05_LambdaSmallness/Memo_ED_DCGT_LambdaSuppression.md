# Memo_ED_DCGT_LambdaSuppression — Construction Memo (Path-L-1 Attempt)

**Series:** Wave-3 Construction Memo (Cosmology Arc; load-bearing #5 attack; Path-L-1 from Memo_ED_LambdaSmallness_Scoping)
**Status:** Substrate-graph attempt to derive the small value of $\rho_\Lambda \sim 10^{-47}$ GeV⁴ via DCGT coarse-graining at cosmological scales. **Not a derivation. No new primitives.** **Outcome: substantively positive, but via an unexpected reduction.** Path-L-1 (DCGT direct suppression) does NOT directly close Λ smallness. The substantive substrate-graph finding is that **Λ smallness reduces to Route A closure** (substrate-derived $\ell_{V_5}(H_0)$) + Friedmann inheritance + Paper_027 substrate-side $G$. The 120-OOM "problem" disappears substrate-side because ED's substrate doesn't have an infinite tower of zero-point modes to sum.
**Date:** 2026-05-16
**Anchors:** Memo_ED_LambdaSmallness_Scoping (Path-L-1 identification); Paper_073 (DCGT, A→regime hydrodynamic-window); Paper_ED_SC_4_9 ($S_{\mathrm{sub}}$ functional); Paper_ED_Cos_01 (M3-upgraded; M3-chain template); Paper_027 (Newton's $G$ derivation); Paper_ED_CCC (SCBU boundary $R_H = c/H_0$); ED_MEMORY anchor 7 (Route A = substrate-derived $\ell_{V_5}(H_0)$; **highest-leverage open derivation in the program**); Paper_038_5 (Lambda_V1_Cosmological — current M2 with smallness OPEN).

---

## §1 Setup: Path-L-1 reframed

Path-L-1 from the LambdaSmallness scoping: DCGT coarse-graining at cosmological scale $R_{cg} \sim 1/H_0$ supplies a substrate-graph suppression factor producing the observed small $\rho_\Lambda$.

**Adversarial framing for honest examination:** what scale-separation suppression factor would DCGT produce, and does it match the 120-OOM observed smallness?

**Result of examination (§3 below):** the standard "naive QFT vacuum energy" $\rho_{\mathrm{vac}}^{\mathrm{naive}} \sim M_P^4$ comes from summing zero-point modes up to Planck cutoff. **ED's substrate ontology doesn't have an infinite tower of modes** — substrate is fundamentally discrete at $\ell_{ED}$. The naive QFT estimate is structurally absent substrate-side; the 120-OOM "problem" is partially dissolved by the discrete substrate ontology before DCGT scale-separation enters.

**The actual substrate-graph derivation route:** $\rho_\Lambda$ is determined Friedmann-side from $H_0$ and $G$ via $\rho_\Lambda = (3/8\pi) H_0^2 M_P^2$. If both $H_0$ (via Route A) and $G$ (via Paper_027) are substrate-side derivable, $\rho_\Lambda$ is substrate-side derivable as a product. **Load-bearing #5 reduces to Route A closure.**

---

## §2 Standard cosmology $\rho_\Lambda$ formula

From Friedmann equations applied to Λ-dominated late universe ($w = -1$, $\rho = \rho_\Lambda$ constant):

$$
H_0^2 = \frac{8\pi G}{3}\rho_\Lambda \quad \Rightarrow \quad \rho_\Lambda = \frac{3 H_0^2}{8\pi G} = \frac{3}{8\pi} H_0^2 M_P^2
$$

In natural units:
- $H_0 \sim 70$ km/s/Mpc $\sim 2 \times 10^{-18}$ s$^{-1}$ $\sim 1.5 \times 10^{-33}$ eV $\sim 10^{-42}$ GeV
- $M_P \sim 10^{19}$ GeV
- $\rho_\Lambda \sim H_0^2 M_P^2 \sim 10^{-84} \times 10^{38} = 10^{-46}$ GeV⁴ ✓ matches observation

**The smallness of $\rho_\Lambda$ is the product of the smallness of $H_0^2$ and the smallness of $M_P^2$ relative to other scales.** Specifically: $H_0/M_P \sim 10^{-61}$ → $(H_0/M_P)^2 \sim 10^{-122}$ → $\rho_\Lambda/M_P^4 \sim 10^{-122}$.

**The 120-OOM discrepancy is the dimensionless ratio $H_0^2/M_P^2$**, not a separate fine-tuning. If $H_0$ and $M_P$ are both substrate-side derivable, the ratio is substrate-side determined automatically.

---

## §3 Why naive QFT estimate doesn't apply substrate-side

The standard "naive QFT vacuum energy" $\rho_{\mathrm{vac}}^{\mathrm{naive}} \sim M_P^4$ comes from summing zero-point energies of QFT modes:

$$
\rho_{\mathrm{vac}}^{\mathrm{naive}} = \frac{1}{2}\int_0^{M_P} \frac{d^3 k}{(2\pi)^3} \, \omega_k \sim M_P^4
$$

This requires an **infinite tower of QFT modes** between $k = 0$ and $k = M_P$ contributing zero-point energies. The result $\sim M_P^4$ is the cumulative contribution.

**Substrate-side:** ED's substrate is fundamentally discrete at $\ell_{ED}$ per Paper_087 + Paper_089. There is no infinite tower of modes between substrate-scale and observation-scale. The substrate's "vacuum-energy contribution" is bounded by substrate-graph content at substrate scale — not by Planck-cutoff zero-point summation.

**Standard QFT's naive estimate is structurally absent from the substrate ontology.** ED's substrate-side $\rho_\Lambda$ candidates:

- **Substrate-scale estimate:** $\rho \sim 1/\ell_P^4 \sim M_P^4$ (matches naive QFT; substrate gives one "mode" per substrate cell of volume $\ell_P^3$, contributing energy $1/\ell_P$). **This is the corpus's prior naïve V1-cutoff estimate per ED_MEMORY** — fails by ~10⁶⁰ OOM.
- **Cosmological-scale estimate:** $\rho \sim H_0^4$ or $H_0^2 M_P^2$. **Matches observation under appropriate formula.**

The discrete-substrate-ontology consideration **partially dissolves the 120-OOM problem** by eliminating the naive QFT infinite-mode-tower starting point. But it doesn't directly give the cosmological-scale estimate.

The further substrate-graph step is recognizing that **$\rho_\Lambda$ is dimensionally determined by $H_0$ and $M_P$** via Friedmann, and that the substrate-side derivation of $\rho_\Lambda$ reduces to substrate-side derivations of $H_0$ and $M_P$.

---

## §4 Substrate-graph reduction: $\rho_\Lambda$ from $H_0$ + $G$

Per §2, $\rho_\Lambda = (3/8\pi) H_0^2 M_P^2$. Substrate-side derivation of $\rho_\Lambda$ requires substrate-side derivation of $H_0$ and $M_P$ (equivalently $G$).

**Substrate-side $M_P$ / $G$:** Per Paper_027 (Newton's $G$ derivation), $G$ is substrate-side identified via dimensional rearrangement of $G$, $\hbar$, $c$ ↔ $\ell_P$. Per ED_MEMORY, this is at "I (dimensional rearrangement, per Paper_027 line 351)" level — INHERITED at dimensional level; substrate-side $G$ is derived structure modulo INHERITED constants.

**Substrate-side $H_0$:** Per Paper_ED_CCC, $H_0$ is related to SCBU boundary scale via $R_H = c/H_0$. Per ED_MEMORY anchor 7, **Route A (substrate-derived $\ell_{V_5}(H_0)$) is the highest-leverage open derivation in the program**. If Route A closes, $H_0$ is derived from substrate parameters ($\ell_{V_5}$, $c$, and presumably substrate-side constants).

**Substantive substrate-graph reduction:**

$$
\rho_\Lambda^{\mathrm{substrate}} = \frac{3}{8\pi} H_0^2(\text{substrate-derived via Route A}) \cdot M_P^2(\text{Paper\_027 substrate-side})
$$

If Route A closes, $\rho_\Lambda$ closes at D-via-I via Friedmann inheritance + Route A's $H_0$ + Paper_027's $G$.

**The 120-OOM "smallness" reduces to the smallness of $H_0/M_P$**, which is determined by the substrate-side scales ($\ell_{V_5}$ for $H_0$; $\ell_P$ for $M_P$). The ratio $\ell_{V_5}/\ell_P$ is itself the Route A question.

**Load-bearing #5 (Λ smallness) ≡ Route A closure + standard Friedmann inheritance.**

---

## §5 Connection to Route A closure

Per ED_MEMORY anchor 7:

> **"SCBU (Substrate-Cosmology Boundary Unification) is offered as the framework's organizing structural hypothesis**, not a closed cross-arc derivation. Paper ED-SC 4.2 explicitly acknowledges that the load-bearing derivation closing the synthesis — **Route A: a substrate-derived $\ell_{V_5}(H_0)$** — does not currently close. With Route A open, the six-projection picture is the framework's hypothesis about how cross-domain structure is organized, not a derived result. **Closing Route A is the highest-leverage open derivation in the program.**"

**Connecting Route A to Λ smallness:** Route A closure ($\ell_{V_5}$ substrate-derived) gives $H_0$ substrate-side derivable. Combined with Paper_027 $G$ substrate-side derivation + Friedmann inheritance, Λ smallness closes at D-via-I.

**The cross-arc consequence of Route A closure now extends to load-bearing #5.** If Route A closes:
- ED-SC 4.x arc upgrades M3 → M2 simultaneously (per ED_MEMORY anchor 7)
- Load-bearing #5 (Λ smallness) closes at D-via-I (this memo)
- Possibly: load-bearing #4 (ED radiation law) connects via $G$ + $H_0$ substrate-side derivations

**Route A is the substrate-research-frontier item with the most cross-arc impact in the corpus.** Its closure would resolve load-bearings #5 and several other arc-wide upgrade items simultaneously.

---

## §6 IDENTIFIED vs OPEN

### IDENTIFIED:

- **Path-L-1 (direct DCGT suppression) does NOT directly close Λ smallness.** DCGT scale-separation factors do not naturally give 120-OOM suppression. Standard hydrodynamic coarse-graining produces at most polynomial corrections.
- **The 120-OOM "problem" is partially dissolved at substrate-side** because ED's discrete substrate ontology does not admit the naive QFT infinite-mode-tower zero-point summation. The naive QFT estimate $\sim M_P^4$ is structurally absent substrate-side.
- **$\rho_\Lambda$ formula:** $\rho_\Lambda = (3/8\pi) H_0^2 M_P^2$ from standard Friedmann inheritance. The 120-OOM dimensionless smallness is the ratio $(H_0/M_P)^2 \sim 10^{-122}$.
- **Substrate-graph reduction:** $\rho_\Lambda^{\mathrm{substrate}}$ is substrate-side derivable IF $H_0$ (via Route A) and $G$ (via Paper_027) are substrate-side derivable. **Load-bearing #5 reduces to Route A closure + Friedmann inheritance.**
- **Paper_027 substrate-side $G$** is INHERITED at dimensional-rearrangement level per ED_MEMORY.
- **Route A** ($\ell_{V_5}(H_0)$) is the highest-leverage open derivation in the program per ED_MEMORY anchor 7.

### OPEN (load-bearing for load-bearing #5 closure):

- **Route A closure** — substrate-derived $\ell_{V_5}(H_0)$. Currently OPEN per ED_MEMORY. **Closing Route A would close load-bearing #5 simultaneously.**
- **Coincidence problem** — why universe transitions to Λ-dominated at current cosmic age. Independent of Route A; standard cosmology + cosmic-age dynamics. Not addressed by this memo.

### Reframing of load-bearing #5

Load-bearing #5 does NOT require substrate-research-frontier work independent of Route A. **It is structurally equivalent to Route A under Friedmann inheritance.** This is a substantively informative reframing:

- Before this memo: Λ smallness was thought to be an independent substrate-research-frontier item (potentially requiring specialized DCGT suppression machinery)
- **After this memo:** Λ smallness reduces to Route A closure + standard inheritance. Route A is the load-bearing item; Λ smallness is downstream.

This consolidates the substrate-research-frontier program: **Route A closure is the single highest-leverage open derivation**, with consequences across the ED-SC 4.x arc + load-bearing #5 + potentially other cosmological items.

---

## §7 Status update + recommended next steps

### Status of load-bearing program after this memo

| # | Item | Status |
|---|---|---|
| 1 | Exponential growth | **CLOSED D-via-I (robust)** |
| 2 | Chirality $\mathbb{Z}_2$ | OPEN; substrate is chirality-symmetric (negative finding) |
| 3 | Horizon motion | **CLOSED D-via-I (weaker, analog-inheritance qualifications)** |
| 4 | ED radiation law | TBD; not yet attacked |
| **5** | **Λ smallness** | **Reduces to Route A closure + Friedmann inheritance** (this memo). Route A independently identified as highest-leverage open derivation. Load-bearing #5 is **conditionally closed pending Route A**. |

**Two closed; one negative-finding (chirality); one TBD; one conditionally closed pending Route A.**

### Substrate-research-frontier consolidation

The substrate-research-frontier characterization continues to consolidate:

- **ED's substrate supports standard cosmology phenomenology via DCGT + standard QFT/cosmology inheritance** (loads #1, #3 closed via M3-chain template).
- **ED's substrate doesn't supply specialized substrate-graph derivations beyond standard physics inheritance for chirality discrimination** (load #2 substrate-symmetric).
- **ED's substrate's quantitative content reduces to substrate-side derivations of fundamental scales** ($\ell_P$ via Paper_027, $\ell_{V_5}$ via Route A) — load #5 reduces to Route A.

**Route A is THE central substrate-research-frontier item.** Its closure has the most cross-arc impact in the corpus.

### Update Paper_038_5 (Lambda_V1_Cosmological)?

The current corpus position on Paper_038_5 is M2 with smallness OPEN. After this memo's reframing:

- Paper_038_5 verdict: **stays M2 with smallness OPEN** because Route A remains OPEN
- **Add note:** load-bearing #5 reduces to Route A closure; Λ smallness is downstream of Route A; Paper_038_5 verdict can upgrade M2 → M3 retroactively when Route A closes (simultaneously with ED-SC 4.x arc-wide upgrade per ED_MEMORY anchor 7)
- The naïve V1-cutoff approach is correctly noted as failed (~10⁶⁰ off); the actual substrate-graph derivation route is via Route A + Friedmann, not via direct V1-cutoff

### Recommended next steps

**Path-Substantive (continue load-bearing program):** proceed to load-bearing #4 (ED radiation law) — last remaining unattacked item. The M3-chain template likely applies cleanly (radiation law = substrate-side analog of Larmor; closes via standard QFT inheritance through DCGT, like loads #1 and #3).

**Path-Consolidate (capture findings):** consolidate the substrate-research findings into an updated PAPER_WRITING_CHECKLIST or program-overview memo. The substrate-ontology characterization has substantively progressed:
- M3-chain template handles standard cosmology phenomenology
- Specialized substrate-graph machinery (chirality) doesn't close from existing primitives
- Quantitative magnitude items (Λ smallness) reduce to Route A
- Route A is the single most consequential open derivation

**Path-Update-038_5:** update Paper_038_5 to reflect this memo's reframing — Λ smallness as Route-A-conditional rather than independent OPEN.

**My recommended next step:** **Path-Substantive (load-bearing #4) followed by Path-Update-038_5.** Closing load-bearing #4 would consolidate the closure pattern; updating Paper_038_5 captures the substantive reframing for the corpus.

If load-bearing #4 also closes via M3-template (likely; radiation law is standard physics analog), the final load-bearing-program tally becomes:
- 3 closed (loads #1, #3, #4)
- 1 negative finding (load #2)
- 1 conditional closure pending Route A (load #5)

This would be a substantively complete substrate-research closure of the load-bearing program, **with Route A clearly identified as the single highest-leverage remaining open derivation**.

---

**End Memo_ED_DCGT_LambdaSuppression.**
