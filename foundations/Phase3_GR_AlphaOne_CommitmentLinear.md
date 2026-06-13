# Phase-3 GR — `α = 1` from the P04 Band Law (closing P-Commitment-Linear)

**Foundations derivation attempt — closes a flagged residual of the Phase-3 GR arc (R8 §2 / R9 Q2). Not a rule proposal, not a corpus edit, not a new primitive. Nothing here derives the Einstein field equations.**
Round 8 *derived* the lapse `N² ~ b` and the Schwarzschild relation `g₀₀g_rr ~ −1` from the certified commitment-rate law `Γ_commit ~ b_int/reserve` — but only **under one load-bearing assumption**: `α = 1`, i.e. the commitment-reserve band does **not** co-scale with the internal band `b_int` (else `Γ ~ b_int/reserve ~ const`, `α = 0`, and ED collapses to **Nordström** — no light bending, experimentally dead). GR-I carries this as the labeled postulate **P-Commitment-Linear**. This note asks whether the P04 band law *forces* `α = 1`, or leaves the Einstein/Nordström fork genuinely open.
**Crank rail:** forward only — from the P04 four-band structure + P11 to the exponent, never backward from Einstein. The honest outcomes are "forced," "forbidden," or "contingent." This round can *kill* ED (if the band law gave `α = 0`), so let it.

---

## 1. The exponent, and what decides it

With `Γ_commit ~ b^α` the null condition gives `N² ~ b^{2α−1}` and `g₀₀g_rr ~ −b^{2(α−1)}` (R8 §2):

- **`α = 1` → Einstein** (`g₀₀g_rr ~ −1`, light bending ×2),
- **`α = 0` → Nordström** (conformal, no bending — ruled out),
- intermediate `α` → intermediate, non-GR classes.

Write the reserve's scaling against the metric band as `reserve ~ b_int^β`. Then `Γ ~ b_int/reserve ~ b_int^{1−β}`, so

> **`α = 1 − β`.**  Einstein `⟺ β = 0` (reserve independent of `b_int`); Nordström `⟺ β = 1` (reserve ∝ `b_int`).

The entire fork is the single question: **does the commitment-reserve band co-scale with the internal (metric) band?**

## 2. The P04 band structure (read from the primitives, not assumed)

P04 §1.5 + `commitment.md` (via R2 §2) give the four-band partition and its dynamics:

- **internal band `b_int`** — the adjacency/internal capacity; sets the metric (`g ~ b_int⁻¹`) **and** the commitment-rate numerator. *(Band-accounting premise, R2 Q5: the metric band and the rate-numerator band are the same `b_int`; flagged §6.)*
- **commitment-reserve band** — the rate *denominator*; **consumed by P11 commitment events**.
- **channel-distributed** and **single-channel-concentrated** bands — a commitment **converts channel-distributed bandwidth into single-channel concentrated bandwidth**.

The commitment operation, exactly: it **draws down the reserve** and **redistributes channel-distributed → concentrated**. Bandwidth is *redistributed, never created* (R2 §3), and crucially — **the reserve only drains: replenishing forms are inadmissible** (R2 §5: "no primitive supplies replenishment; conflicts with the irreversibility of commitment consumption," P11).

Two facts to carry forward: (i) the reserve is a **distinct band** from `b_int`, drawn down by commitment; (ii) the reserve is **monotone-draining** (P11), with **no replenishment**.

## 3. The reserve and the metric band are different state variables

`b_int` and the reserve are not merely distinct bands — they are functions of **different state variables**:

- **`b_int`** is the **ambient adjacency capacity** at a locus — a property of the graph/region, which the matter profile shapes (`∇²b_int ~ ρ`, R1).
- **the reserve** is a **carried, consumable budget** — its level at a locus is set by the **commitment history** there (monotone drain by P11), i.e. by *how many commitments have already fired*, not by the instantaneous ambient `b_int`.

So generically `reserve = f(commitment count)`, **not** `f(b_int)`: they are independent variables, which is exactly `β = 0`, `α = 1`. Co-scaling (`β ≠ 0`, `reserve = f(b_int)`) is not the default — it would require an *added* coupling that ties the reserve level to the ambient internal band. The next section shows that coupling is inadmissible at the Nordström endpoint.

## 4. The forcing — Nordström requires inadmissible replenishment

The Nordström value `β = 1` (`reserve ∝ b_int`) means the reserve must **track** `b_int`'s spatial profile — in particular, be **higher where `b_int` is higher**. In a quasi-static gravitational configuration `b_int` has both higher and lower regions (it is a field with a source). For the monotone-draining reserve to be *higher* in the high-`b_int` regions, it must be **raised** there — and raising a reserve that only ever drains is **replenishment**, which P11 + R2 §5 declare **inadmissible** (no replenishment primitive; it contradicts the irreversibility of commitment consumption).

> **The Nordström branch (`α = 0`) requires the reserve to co-scale with the metric band, which requires reserve replenishment slaved to `b_int` — and replenishment is structurally inadmissible (P11 irreversibility).** So `α = 0` is **excluded by the same irreversibility that defines commitment.** The surviving branch is `β = 0`, `α = 1`, **Einstein**.

This is a genuine could-say-no result that came back *no* for Nordström: had P04 defined the reserve as a *fixed fraction of the total* (which scales with `b_int`) or supplied a replenishment band, `β = 1` would hold and ED would be Nordström — experimentally dead. P04 does neither: the reserve is a distinct, monotone-draining, history-set band. **The band law forces `α = 1`.**

## 5. The arrow selects Einstein — twice

The selection mechanism is worth naming, because it is the program's signature commitment again. The reserve cannot track `b_int` *because it cannot replenish* — i.e. because commitment consumption is **irreversible (P11, the arrow)**. So:

> **P11 irreversibility selects the Einstein branch at the lapse (`α = 1`)** — the *same* arrow that, at the mode count (R10/GR-II), forces the khronon and makes the gravity khronometric.

Two independent Einstein-branch selections — the lapse exponent here, the propagating-mode structure in GR-II — trace to **one source: the arrow in the law.** The factor of two and the khronon are the same commitment wearing two hats. (This also sharpens the irony of the class: the arrow forces ED *onto* Einstein's weak field at the lapse, and *off* pure Einstein at the mode count — both by P11.)

## 6. Structural vs contingent

| Item | Verdict |
|---|---|
| `α = 1 − β`, `reserve ~ b_int^β` | **definitional** (R8 §2 + §1) |
| reserve = distinct, monotone-draining band (no replenishment) | **structural** (P04 §1.5 + P11; R2 §5) |
| reserve set by commitment history, not ambient `b_int` | **structural** (different state variables, §3) |
| Nordström `α=0` needs reserve ∝ `b_int` → replenishment | **structural** — **inadmissible** (P11; R2 §5) |
| therefore `α = 1` (Einstein branch forced) | **forced** (the round's result) |
| Einstein-branch selection ↔ P11 (same arrow as the khronon) | **structural unification** (§5) |
| metric band = rate-numerator band = `b_int` | **premise** (R2 Q5 band-accounting; standard GR-I/R8 reading; flagged) |
| precise quasi-static reserve profile (sub-leading) | **contingent — needs full `F`** (R2 C3); affects *magnitude*, not the *branch* |
| any structural block | **none — and Nordström positively excluded** |

## 7. Verdict

**The P04 band law forces `α = 1`: ED's lapse is Einstein-branch, and Nordström is structurally excluded.** The exponent reduces to whether the commitment-reserve band co-scales with the internal (metric) band: `α = 1 − β`, `reserve ~ b_int^β`. The reserve and `b_int` are **different state variables** — the reserve is a carried, monotone-draining budget set by *commitment history* (P11), the internal band is the *ambient* adjacency capacity shaped by `ρ` — so generically `β = 0`, `α = 1`. The Nordström value `β = 1` would require the reserve to *track* `b_int`'s profile, i.e. to be **raised** where `b_int` is high, which is **replenishment** — and replenishment is inadmissible by the same P11 irreversibility that defines commitment (R2 §5). So the band law does not merely *lean* Einstein (R8's "leading reading"); it **forces** it, and **positively excludes** Nordström. The Einstein-branch selection is the arrow (P11) — the same commitment that forces the khronon at the mode count (R10), now acting at the lapse.

**This upgrades R8's load-bearing assumption to a derived result.** P-Commitment-Linear (`α = 1`) is no longer a labeled postulate of GR-I but a consequence of P04's distinct, non-replenishing reserve band + P11 irreversibility. The residual is sub-leading: the precise quasi-static reserve profile needs the full dynamical rule `F` (R2 C3) and could shift `α` by a small, computable amount — but **not across the branch**, because the branch-flip endpoint (`α = 0`) is structurally forbidden. The band-accounting premise (metric band = rate-numerator band = `b_int`, R2 Q5) is the one stated assumption. **Einstein is still not derived; one of its two load-bearing weak-field assumptions is now derived from the primitives.**

## 8. Next questions

1. **Band accounting (closes the premise).** Confirm from P04 that the band feeding `g ~ b⁻¹` is the same internal band `b_int` that is the commitment-rate numerator (R2 Q5). If a different band feeds the metric, recompute `α` for that band's reserve-scaling.
2. **The sub-leading `α` correction.** With the full `F` (R2 C3), compute the quasi-static reserve profile and the small departure of `α` from 1 — a potential *post-Newtonian* signature (does it feed `α₁, α₂`?).
3. **Pairs with the timelike-geodesic note.** Together, `α = 1` (this note) and the timelike geodesic identity remove **both** standing weak-field assumptions of GR-I/GR-II; the remaining open keystone is the explicit dynamical rule `F` (the #1/#8 shared build), now with both its lapse-exponent and its geodesic structure independently pinned.

---

*Closes (to a forced result) the `α = 1` / P-Commitment-Linear assumption. The lapse exponent is `α = 1 − β` with `reserve ~ b_int^β`; the commitment-reserve is a distinct, monotone-draining band set by commitment history, not the ambient internal band, so `β = 0` (`α = 1`, Einstein) generically — and the Nordström endpoint `β = 1` requires the reserve to co-scale with `b_int`, i.e. **replenishment**, which P11 irreversibility forbids (R2 §5). So the band law **forces `α = 1` and positively excludes Nordström**; the Einstein-branch selection is the arrow (P11) — the same commitment that forces the khronon. R8's load-bearing assumption becomes a derived result; the residual is the sub-leading reserve profile (needs the full `F`; cannot flip the branch) plus the band-accounting premise. Could-say-no (a fixed-fraction or replenishing reserve would have given Nordström and killed ED); it came back Einstein. No corpus edits, no new primitives; Einstein not derived; one fewer postulate.*
