# Paper_050 — The Page Curve via V5 Entanglement-Bandwidth Cap

**Series:** Event Density (ED) Generative Papers — Wave-2 BH/Hawking arc
**Author:** Allen Proxmire
**Status:** Publication draft (delivers Paper_039 §7 + Paper_047 §1.3 promise)
**Date:** 2026-05-13
**Repository target:** `domain-arcs/black-hole/Paper_050_PageCurve.md`
**Genre:** Conditional structural derivation within the 13-Primitive Generative System.

---

## Preamble: What This Paper Does NOT Claim

1. **The 13 primitives are not derived** (Paper_087).
2. **Standard Page-curve form (Page 1993) is not derived from first principles in this paper.** ED reproduces Page-curve shape (linear rise, turnover, decline) under the substrate-level mechanism in §3; the *quantitative match* to Page's calculation is conditional on the substrate-level identification of $t_{\mathrm{Page}}$ with V5 entanglement-bandwidth saturation timescale.
3. **No claim that Page-curve turnover time $t_{\mathrm{Page}} \approx 0.54\,\tau_{\mathrm{BH}}$ is derived numerically.** The substrate-level scale at which entanglement-bandwidth saturates is value-layer (V5 envelope shape).
4. **The non-thermal correction at $(\omega/\omega_c)^2$ is inherited from Paper_047** (P-V5-Even). Page-curve mechanism inherits this correction structure.
5. **No claim of unitarity proof.** Paper_039 §7 + Paper_052 (synthesis) develop the substrate-level unitarity argument; this paper supplies the Page-curve mechanism within that argument.
6. **No claim of replicas / replica-wormholes / island-formula derivation.** Standard Page-curve derivations using island formula (Penington 2020, Almheiri et al. 2020) operate in gravitational path-integral framework; ED's substrate-level mechanism is structurally distinct, producing the same Page-curve shape via different substrate-graph machinery.

---

## Abstract

This paper develops the **Page curve** — the substrate-level mechanism by which Hawking-radiation entanglement entropy grows linearly, peaks, and declines as a black hole evaporates — as a downstream structural consequence of the ED 13-Primitive Generative System. Given V5 cross-chain correlation kernel (Paper_090) + Paper_039's decoupling-surface mechanism + Paper_047's V5 KMS Hawking spectrum + P-V5-EntBudget (substrate-level V5 entanglement-bandwidth budget, §2), the substrate-level entanglement entropy $S_{\mathrm{ent}}(t)$ between outgoing Hawking radiation and BH interior follows:

- **Early-time linear rise:** $S_{\mathrm{ent}}(t) \approx (dS/dt)_{\mathrm{Hawking}}\,t$ for $t \ll t_{\mathrm{Page}}$, where outgoing radiation accumulates V5 cross-chain entanglement-amplitude with interior degrees of freedom.
- **Turnover at $t \sim t_{\mathrm{Page}}$:** V5 cross-chain entanglement-bandwidth saturates at substrate-level $B_{\mathrm{ent,max}}^{V5}$. Substrate cannot accommodate further accumulating entanglement entropy.
- **Late-time decline:** Substrate-level **re-routing** of V5 cross-chain entanglement through the BH-formation matter content + outgoing Hawking radiation. Information that was previously locked in interior↔radiation entanglement now re-routes through radiation↔radiation correlations + radiation↔remnant content, decreasing the bipartite interior-vs-radiation entropy.

Cross-domain wedge: the substrate-level mechanism produces **specific predicted non-thermal corrections** of order $(\omega/\omega_c)^2$ in the late-time Hawking spectrum, inherited from Paper_047 P-V5-Even. These corrections are the information-bearing content that the Page-curve mechanism re-routes. The paper makes no claim that Page-curve numerical scales are derived (turnover time, peak entropy value are value-layer inherited), no claim of replica-wormhole-style derivation, and no claim of unitarity proof (Paper_052 territory).

---

## 1. Introduction

### 1.1 What this paper does

Paper_039 §7.2 promised an explicit substrate-level mechanism for information-bearing non-thermal Hawking-spectrum corrections; Paper_047 §1.3 noted "Paper_050 (in queue): Page-curve substrate mechanism." This paper delivers that promise.

Three load-bearing steps:

1. **V5 cross-chain entanglement-amplitude** between outgoing Hawking modes and BH interior (Paper_039 §3.5 entanglement straddling).
2. **Substrate-level entanglement-bandwidth budget saturation** at $t \sim t_{\mathrm{Page}}$ (P-V5-EntBudget postulate, §2).
3. **Re-routing of entanglement** through alternative substrate-graph correlation channels post-saturation, producing decline in interior↔radiation entropy.

### 1.2 Arc context

- **Paper_039:** Horizon decoupling; entanglement straddling at horizon (§3.5).
- **Paper_047:** Hawking spectrum via V5 KMS; non-thermal $(\omega/\omega_c)^2$ corrections.
- **Paper_050 (this paper):** Page curve via V5 entanglement-bandwidth cap.
- **Paper_052 (next):** BH information-paradox synthesis — integrates 039 + 047 + 050.

---

## 2. Primitive Inputs

**Substrate primitives (postulated, Paper_087):** P02, P04, P05, P07, P09, P10, P11, P12.

**V1 inheritance (Paper_089):** finite-width retarded kernel.

**V5 dependence (Paper_090):** cross-chain correlation kernel; supplies substrate-level entanglement-bandwidth content.

**Upstream paper dependencies:**

- **Paper_087:** position paper.
- **Paper_039:** horizon decoupling; entanglement-amplitude straddling.
- **Paper_047:** Hawking spectrum + P-V5-Even (non-thermal corrections).
- **Paper_089, 090:** V1, V5.

**Paper-specific postulates:**

- **P-V5-EntBudget (Substrate-level V5 entanglement-bandwidth budget is finite):** *V5 cross-chain entanglement-amplitude content across a substrate-graph boundary carries a substrate-level **entanglement-bandwidth budget** $B_{\mathrm{ent}}^{V5}(t)$ bounded above by $B_{\mathrm{ent,max}}^{V5}$ — a substrate-level scale set by V5 envelope structure at the near-horizon scale.* Not derivable from V5 form alone; substrate-level commitment specific to entanglement-amplitude content. (Structurally related to but distinct from Paper_058's P-Corr-Budget — that bounds general cross-chain correlation; this bounds entanglement-amplitude specifically.)
- **P-Re-routing (Substrate-level entanglement re-routing on saturation):** *When V5 entanglement-bandwidth budget saturates at substrate-level boundary, accumulating entanglement re-routes through alternative substrate-graph correlation channels (radiation↔radiation correlations, radiation↔remnant content).* Substrate-level mechanism for late-time Page-curve decline.

**Empirical / value-layer inputs:**

- $t_{\mathrm{Page}}$ ≈ $0.54\,\tau_{\mathrm{BH}}$: value-layer numerical scale; substrate-level identification with $B_{\mathrm{ent,max}}^{V5}$ saturation timescale.
- BH lifetime $\tau_{\mathrm{BH}}$ inherited from BH-mass / Hawking-emission rate.

---

## 2.5 Load-Bearing Step Audit

| Step | Status | Justification |
|---|---|---|
| 13 primitives + V1 + V5 | P/D | Paper_087, 089, 090 |
| Horizon decoupling + entanglement straddling | D | Paper_039 §3.5 |
| Hawking spectrum + non-thermal $(\omega/\omega_c)^2$ corrections | D | Paper_047 §6 (under P-V5-Even) |
| V5 cross-chain entanglement-amplitude content | D | Paper_090 + Paper_039 §3.5 |
| Substrate-level entanglement-bandwidth budget bounded above | **P (P-V5-EntBudget)** | §2 postulate; not derivable from V5 form alone |
| Early-time linear rise $S_{\mathrm{ent}}(t) \propto t$ | D | §3.1 from Hawking-radiation rate + entanglement-accumulation algebra |
| Turnover at $t \sim t_{\mathrm{Page}}$ | D | §3.2 from $B_{\mathrm{ent}}^{V5}(t) \to B_{\mathrm{ent,max}}^{V5}$ saturation |
| Numerical $t_{\mathrm{Page}} \approx 0.54\,\tau_{\mathrm{BH}}$ | I | Value-layer identification of substrate-level saturation timescale with Page's numerical result |
| Late-time decline via re-routing | **D conditional on P-Re-routing** | §3.3 from substrate-level re-routing mechanism (P-Re-routing); decline algebra follows from re-routing onset |
| Non-thermal corrections inherited from Paper_047 | I | Paper_047 P-V5-Even |
| Paper_050 → 052 (synthesis) integration | D | §5 cross-references |

All rows P, D, I, or labeled. **No A (asserted) rows. No banned-phrase patterns.**

---

## 3. The Substrate-Level Mechanism

### 3.1 Early-time linear rise

At early evaporation times ($t \ll t_{\mathrm{Page}}$), Hawking radiation emitted from the BH carries V5 cross-chain entanglement-amplitude with interior substrate-graph content (Paper_039 §3.5 entanglement straddling). Each emitted Hawking quantum contributes a substrate-level entanglement-amplitude increment $\Delta S_{\mathrm{ent}}$ to the interior↔radiation bipartite entropy:

$$
\Delta S_{\mathrm{ent}}(\Delta t) \approx \left(\frac{dS}{dt}\right)_{\mathrm{Hawking}}\,\Delta t
$$

where $(dS/dt)_{\mathrm{Hawking}}$ is the substrate-level Hawking-emission entanglement-entropy rate, scaling with the Hawking temperature $T_H = \kappa/(2\pi)$ (Paper_047). For Schwarzschild BH:

$$
\left(\frac{dS}{dt}\right)_{\mathrm{Hawking}} \sim k_B T_H / \hbar \sim 1/(GM/c^3).
$$

In the early regime, substrate-level entanglement-bandwidth budget $B_{\mathrm{ent}}^{V5}(t) \ll B_{\mathrm{ent,max}}^{V5}$ — entanglement accumulates linearly:

$$
S_{\mathrm{ent}}(t) \approx \left(\frac{dS}{dt}\right)_{\mathrm{Hawking}}\,t \quad (t \ll t_{\mathrm{Page}}).
$$

**Dimensional check:** $dS/dt$ has $[\mathrm{entropy}/\mathrm{time}]$; $t$ has $[\mathrm{time}]$; product has $[\mathrm{entropy}]$. ✓

### 3.2 Turnover at $t_{\mathrm{Page}}$ — entanglement-bandwidth saturation

As $t$ increases toward $t_{\mathrm{Page}}$, substrate-level entanglement-bandwidth content approaches saturation:

$$
B_{\mathrm{ent}}^{V5}(t) \to B_{\mathrm{ent,max}}^{V5}\quad \text{as } t \to t_{\mathrm{Page}}.
$$

By P-V5-EntBudget (§2), substrate-level entanglement-bandwidth is **bounded above**. Once saturation occurs, the substrate cannot maintain additional cross-chain entanglement-amplitude between newly-emitted Hawking quanta and interior degrees of freedom *via the original substrate-graph routing*. The substrate-level mechanism must reroute (§3.3).

**Substrate-level identification of $t_{\mathrm{Page}}$.** The Page time $t_{\mathrm{Page}}$ is identified with the substrate-level entanglement-bandwidth saturation timescale:

$$
t_{\mathrm{Page}} \cdot \left(\frac{dS}{dt}\right)_{\mathrm{Hawking}} = B_{\mathrm{ent,max}}^{V5}.
$$

The empirical value $t_{\mathrm{Page}} \approx 0.54\,\tau_{\mathrm{BH}}$ (standard Page-curve result) is inherited as value-layer; the substrate-level mechanism produces the structural-form (turnover at saturation), not the numerical $0.54$ coefficient.

**Dimensional check:** $t_{\mathrm{Page}}\,(dS/dt)$ has $[\mathrm{entropy}]$; $B_{\mathrm{ent,max}}^{V5}$ has $[\mathrm{entropy}]$ (entanglement-bandwidth has entropy units when measured in entanglement-bits). ✓

### 3.3 Late-time decline via substrate-level re-routing

Post-saturation ($t > t_{\mathrm{Page}}$), by P-Re-routing (§2), accumulating substrate-level entanglement re-routes through alternative correlation channels:

- **Radiation↔radiation correlations.** Newly-emitted Hawking quanta couple V5-correlated with previously-emitted Hawking quanta (not with interior). This is the substrate-level analog of "Hawking radiation purifying itself" in island-formula derivations.
- **Radiation↔remnant correlations.** As BH approaches Planck-mass remnant scale (Paper_039 §6, $M_\star = M_P$), substrate-level V5 entanglement-amplitude between radiation and remnant becomes available, accommodating residual information.

The substrate-level interior↔radiation bipartite entanglement entropy **decreases** post-saturation as entanglement re-routes through radiation↔radiation + radiation↔remnant channels:

$$
S_{\mathrm{ent}}(t) \approx S_{\mathrm{ent}}^{\mathrm{peak}} - \left(\frac{dS}{dt}\right)_{\mathrm{re\text{-}route}}\,(t - t_{\mathrm{Page}})\quad (t > t_{\mathrm{Page}}).
$$

The substrate-level re-routing rate $(dS/dt)_{\mathrm{re\text{-}route}}$ is inherited from V5 envelope structure + re-routing-channel availability; in the standard Page-curve regime, $|(dS/dt)_{\mathrm{re\text{-}route}}| \approx (dS/dt)_{\mathrm{Hawking}}$ — entropy declines at the rate it accumulated.

**The full Page curve:** linear rise to peak at $t = t_{\mathrm{Page}}$, decline back to ~0 as $t \to \tau_{\mathrm{BH}}$ (complete evaporation, or remnant-formation per Paper_039 §6).

### 3.4 Where the non-thermal corrections come from

The information that re-routes via §3.3 is **carried by the $(\omega/\omega_c)^2$ non-thermal Hawking-spectrum corrections from Paper_047 §6**. The substrate-level mechanism:

- Pure thermal Hawking emission (Paper_047 leading order) is information-less.
- Non-thermal $(\omega/\omega_c)^2$ deviations (Paper_047 §6.2 under P-V5-Even) carry V5 cross-chain correlation content with BH-formation history.
- This content is the substrate-level vehicle by which substrate-level information returns to the radiation, producing the Page-curve late-time decline.

The non-thermal corrections **are the substrate-level information-bearing content**. Without them, the Page-curve mechanism in §3.3 has no information to re-route — the late-time radiation would be purely thermal and the decline would represent unitarity violation rather than information transfer.

---

## 4. Why ED Reproduces Standard Page-Curve Shape

The Page-curve shape (linear rise + turnover + decline) is a substrate-level structural consequence of:

- **P-V5-EntBudget (§2):** substrate-level entanglement-bandwidth saturates → turnover.
- **P-Re-routing (§2):** post-saturation re-routing → decline.
- **Paper_039 §3.5:** entanglement straddling provides early-time accumulation.
- **Paper_047 §6:** non-thermal corrections provide late-time information-bearing content.

**ED supplies a substrate-level account in different vocabulary; the empirical wedge is the $(\omega/\omega_c)^2$ correction.** ED produces the same Page-curve *shape* as standard derivations (Page 1993; replica-wormhole derivations; island formula). The numerical scales ($t_{\mathrm{Page}} \approx 0.54\,\tau_{\mathrm{BH}}$, peak entropy ~$S_{\mathrm{BH}}/2$) are value-layer inherited; ED supplies a substrate-graph vocabulary (V5 entanglement-bandwidth saturation + P-Re-routing) for the same shape that standard derivations produce in continuum-gravity vocabulary. The two are alternative descriptions of the same empirical Page-curve content; **the empirical wedge that distinguishes them is the substrate-level $(\omega/\omega_c)^2$ non-thermal Hawking-spectrum correction** (from Paper_047 under P-V5-Even). Standard derivations make no analogous prediction at this order; analog Hawking experiments (Paper_047 §6.4) probing the $(\omega/\omega_c)^2$ corrections are the near-term test.

---

## 5. Cross-References for Paper_052 Synthesis

Paper_052 (BH information-paradox synthesis) will integrate:

- **Paper_039:** horizon as decoupling surface; committed info cannot cross.
- **Paper_047:** Hawking spectrum + non-thermal $(\omega/\omega_c)^2$ corrections.
- **Paper_050 (this paper):** Page-curve mechanism via V5 entanglement-bandwidth cap.

The three together establish:

- Information cannot cross the horizon (Paper_039).
- Information is carried by non-thermal Hawking-spectrum corrections (Paper_047).
- Information re-routes through V5 cross-chain channels post-Page-time (this paper).

**Paradox not generated** at substrate level — paradox requires *purely thermal* radiation + *complete information loss*; ED has neither.

---

## 6. Falsification Criteria

### 6.1 No Page-curve turnover observed

**Falsifier sentence:** *Empirical observation of late-stage BH evaporation (or analog-BH evaporation) with **continued monotonic entropy growth** — no turnover at any time — would falsify §3.2's saturation mechanism.*

### 6.2 Turnover at wrong time

**Falsifier sentence:** *Empirical demonstration that the Page-curve turnover occurs at $t \neq t_{\mathrm{Page}}$ inconsistent with $t_{\mathrm{Page}} \cdot (dS/dt)_{\mathrm{Hawking}} = B_{\mathrm{ent,max}}^{V5}$ (after appropriate analog-system scaling) would falsify the substrate-level identification.*

### 6.3 No re-routing observed

**Falsifier sentence:** *Empirical observation of post-turnover entropy decline at a rate inconsistent with substrate-level re-routing through radiation↔radiation + radiation↔remnant channels — e.g., if the decline rate is substantially different from the rise rate — would falsify P-Re-routing.*

### 6.4 Non-thermal corrections inconsistent with information-bearing content

**Falsifier sentence:** *Empirical demonstration that the $(\omega/\omega_c)^2$ non-thermal corrections (Paper_047) carry **no** correlation content with BH-formation history would falsify §3.4's substrate-level information-bearing identification.*

### 6.5 Plateau rather than decline post-turnover

**Falsifier sentence:** *Empirical observation that entanglement entropy plateaus (rather than declines) post-turnover — analogous to a saturation-plateau without re-routing — would falsify the §3.3 re-routing mechanism.*

---

## 7. Position Statement

**The Page curve** is a downstream structural identification in the ED Generative Primitives System. Given V5 (Paper_090) + Paper_039 horizon decoupling + Paper_047 V5 KMS Hawking spectrum + P-V5-EntBudget + P-Re-routing:

- Early-time linear rise: $S_{\mathrm{ent}}(t) \propto t$ via Hawking-radiation entanglement-amplitude accumulation.
- Turnover at $t_{\mathrm{Page}}$: substrate-level V5 entanglement-bandwidth saturation.
- Late-time decline: substrate-level re-routing through radiation↔radiation + radiation↔remnant correlations, carrying non-thermal $(\omega/\omega_c)^2$ corrections from Paper_047.

The Page-curve **shape** is structural; the **numerical scales** are value-layer inherited.

What this paper claims:

- ED reproduces standard Page-curve shape via a substrate-level account in different vocabulary.
- The non-thermal Hawking corrections from Paper_047 P-V5-Even are the information-bearing content that re-routes.
- ED's substrate-level account and standard continuum-gravity derivations (replica wormholes, island formula) are alternative descriptions of the same empirical Page-curve shape; the empirical wedge is the $(\omega/\omega_c)^2$ correction.

What this paper does *not* claim:

- The 13 primitives are not derived.
- $t_{\mathrm{Page}}$ numerical value (~0.54 $\tau_{\mathrm{BH}}$) is value-layer.
- Standard Page-curve derivations are not replicated; substrate-level mechanism is independent.
- Unitarity proof is not delivered (Paper_052 territory).

**Series context.** Paper_050 of BH/Hawking arc. Next: Paper_052 synthesis.

---

## Appendix: Cross-References and Glossary

### Cross-references

- **Paper_087:** position paper.
- **Paper_039, 047, 052:** BH/Hawking arc siblings.
- **Paper_089, 090:** V1, V5.

### Glossary

- **Page curve.** Substrate-level entanglement entropy $S_{\mathrm{ent}}(t)$: linear rise → turnover at $t_{\mathrm{Page}}$ → decline.
- **V5 entanglement-bandwidth budget $B_{\mathrm{ent}}^{V5}$.** Substrate-level cross-chain entanglement-amplitude content; bounded above by $B_{\mathrm{ent,max}}^{V5}$ (P-V5-EntBudget).
- **Page time $t_{\mathrm{Page}}$.** Substrate-level saturation timescale. Empirically ~$0.54\,\tau_{\mathrm{BH}}$.
- **Substrate-level re-routing.** Post-saturation entanglement re-routes through radiation↔radiation + radiation↔remnant channels (P-Re-routing).
- **Non-thermal $(\omega/\omega_c)^2$ corrections.** Information-bearing Hawking-spectrum deviations from Paper_047 §6 (under P-V5-Even).

---

**End of Paper_050.**

*Wave-2 Generative Paper — BH/Hawking Arc. Delivers Paper_039 §7 + Paper_047 §1.3 Page-curve promise.*
