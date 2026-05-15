# Q-COMPUTE Inheritance Ledger Update: Arc E (Entanglement) Closure Impact

**Date:** 2026-05-09
**Source of truth:** `arcs/arc-E/E-8_inheritance_ledger_updates.md` §3

## Summary

Arc E closed 2026-05-08. The substrate quantities $\mathcal{M}, \mathcal{U}, \sigma, \Gamma_{\mathrm{cross}}$ introduced in Q-COMPUTE Memo 1 are now identified as the *same* substrate quantities operating in bipartite-entanglement structure (Arc E memos E-2, E-4, E-6).

## Cross-arc identification of substrate quantities

| Substrate quantity | Q-COMPUTE role (Memo 1) | Arc E role |
|---|---|---|
| $\mathcal{M}(A)$ | Counts substrate-resolvable participation channels at qubit-region; bounds Class A | Sets $\Gamma_{\mathrm{max}}(A)$ in E-4 monogamy; counts shared participation channels via E-3 Schmidt rank; same as ED-I-01 entropy-analogue in E-6 |
| $\mathcal{U}$ | Dynamical state of unresolved participation rule | Tracks (SP)-class shared-rule persistence in E-2 |
| $\sigma$ | Determines $\Gamma_{\mathrm{cross}} \sim \exp[-\alpha\sigma]$ | Determines bandwidth available for shared participation channels in E-4 |
| $\Gamma_{\mathrm{cross}}$ | Cross-bandwidth between substrate regions | $\Gamma_{AB}$ in E-4 monogamy; sets entanglement strength via bandwidth-monotone link |

## Class C plateau ↔ E-4 monogamy

Q-COMPUTE Memo 5/6's Class C correlation-budget plateau prediction (saturation at $N_{\mathrm{corr}}$ correlated qubits because cross-bandwidth budget is finite) is the **multipartite extension of Arc E-4's bipartite monogamy**. With $N = 2$ subsystems → $\Gamma_{AB} \leq \Gamma_{\mathrm{max}}(A)$. With $N \geq 3$ → CKW-style inequalities (E-4 §6) and the multipartite generalization (E-4 §7). **Same substrate mechanism, different multipartite scales.**

## Structural equivalence

> **Entanglement is the unresolved regime of participation-rule individuation.**

This sharpens Q-COMPUTE Memo 1 §2.1's substrate description of "what a quantum computer is" and makes explicit that *entanglement* and *quantum computation* are the same phenomenon used for different purposes:

- **Quantum computation:** hold the unresolved rule long enough to perform substrate manipulations.
- **Entanglement:** maintain the unresolved rule across spatially-separated endpoints.

## What is unchanged

- All Q-COMPUTE verdicts unchanged.
- Three sharp predictions (Class A wall, Class B exponential gap-suppression, Class C plateau) stand as written.
- $\mathcal{M}_{\mathrm{crit}}$ matter-wave anchor (140–250 kDa) unchanged.
- UR-1 theorem unchanged.

## What is updated

- Inheritance ledger reflects cross-arc unification with Arc E.
- Class C plateau now structurally explicable as bipartite-monogamy multipartite extension.

For full derivation content, see `arcs/arc-E/E-4_monogamy_from_bandwidth.md` and `arcs/arc-E/E-6_entropy_form.md`. For the cross-arc unification reading, see `arcs/arc-E/E-7_synthesis.md` §3.
