# NS-Q5 — Q-Factor Arc Synthesis

**Date:** 2026-04-30
**Status:** Arc closed. **Final verdict: H1 null.** ED's canonical Q ≈ 3.5 is an internal-canon invariant of the participation-channel ODE in the underdamped regime; it does not correspond to a specific empirical universal in fluid mechanics. H2 weakly supported only at the "generic moderate-damping regime overlap" level via V5 (not architectural); H3 fails for both P7 and P4 channels. Brief-note exploratory arc closes cleanly with negative-leaning verdict.
**Companions:** [`NS_Q1_Opening.md`](NS_Q1_Opening.md), [`NS_Q2_V5_Memory.md`](NS_Q2_V5_Memory.md), [`NS_Q3_P7_Amplitude.md`](NS_Q3_P7_Amplitude.md), [`NS_Q4_P4_Mobility.md`](NS_Q4_P4_Mobility.md), [`../../Architectural_Canon.md`](../../Architectural_Canon.md) §3 (Q ≈ 3.5 canonical-PDE invariant).

---

## 1. Purpose

This memo synthesizes NS-Q1 through NS-Q4 and delivers the final verdict on the three hypotheses framed in NS-Q1 §6 (H1 null / H2 weak / H3 speculative). The arc closes as a brief-note exploratory investigation of whether ED's canonical Q ≈ 3.5 has empirical fluid-mechanical correspondence.

---

## 2. Inputs

| Memo | Content |
|---|---|
| [`NS_Q1_Opening.md`](NS_Q1_Opening.md) | Arc opening; H1/H2/H3 framework; honest a-priori (Q ≈ 3.5 is *not* a textbook universal across viscous oscillators); default H1 null |
| [`NS_Q2_V5_Memory.md`](NS_Q2_V5_Memory.md) | V5 channel: Q = 3.5 corresponds to $\omega_0\tau_R \approx 0.144$ in user-spec'd Maxwell-oscillator formulation; fast-relaxation regime; V5 doesn't force this ratio architecturally |
| [`NS_Q3_P7_Amplitude.md`](NS_Q3_P7_Amplitude.md) | P7 channel: 3–6% amplitude ratio vs. ζ = 1/(2Q) = 14.3% — factor 2.4–4.8× mismatch; mechanism mismatch (nonlinear harmonic generation vs. linear damping); H3(P7) fails |
| [`NS_Q4_P4_Mobility.md`](NS_Q4_P4_Mobility.md) | P4 channel: steady-state mobility vs. time-domain damping — different dynamical axes; no canonical algebraic relation between β and ζ; H3(P4) fails |
| ED canonical Q ≈ 3.5 status | Internal-canon invariant of the participation-channel ODE at canon-default $\zeta = 1/4$ ([`../../Architectural_Canon.md`](../../Architectural_Canon.md) §3) |

---

## 3. H1 Verdict — Null Hypothesis

**Verdict: H1 succeeds.**

ED's canonical Q ≈ 3.5 is a real *derived* property of the canonical PDE's participation-channel ODE in the underdamped regime — established by ED-Phys-17 / ED-Phys-18 simulation traces and codified as a universal invariant in [`../../Architectural_Canon.md`](../../Architectural_Canon.md) §3. As an *internal-canon* invariant, the value is meaningful and reproducible.

**However:** Q ≈ 3.5 does **not** correspond to a specific empirical universal in fluid mechanics. The §4.1 honest assessment from NS-Q1 already flagged that Q ≈ 3.5 is not a textbook universal across viscous oscillators; Q-factors span enormous ranges across systems (atomic clocks ~10¹⁰⁻¹², tuning forks ~10⁴, mechanical pendulums in viscous fluid ~1–10, Stokes-class oscillations O(1)–O(10)). Q ≈ 3.5 sits in the moderately-damped regime that overlaps with some specific oscillator classes but is not a concentrated empirical cluster.

**The default expectation (H1 null) is supported by the three correspondence-channel investigations.** The arc's value is in confirming this honestly rather than overclaiming an empirical fluid-mechanical universal that does not exist.

---

## 4. H2 Verdict — V5 Memory-Kernel Correspondence

**Verdict: H2 weakly supported at "moderate-damping overlap" level only; not architectural.**

NS-Q2 derived: Q = 3.5 corresponds to $\omega_0\tau_R \approx 0.144$ in the user-spec'd Maxwell-oscillator formulation $Q_\mathrm{eff} = \frac{1}{2}\sqrt{1+(\omega_0\tau_R)^2}/(\omega_0\tau_R)$. Solving algebraically: $48(\omega_0\tau_R)^2 = 1$, giving $\omega_0\tau_R = 1/\sqrt{48} \approx 0.144$.

This sits in the **fast-relaxation regime** where Maxwell-viscoelastic medium behaves predominantly viscous-fluid-like (memory time short relative to oscillation period). Three structural facts prevent this from being an architectural correspondence:

1. **V5's $\tau_R$ is INHERITED** per arc-N N.2 §6.5. No canon-level constraint specifies $\tau_R$ relative to any oscillation frequency.
2. **No canon-level link between $\tau_R$ and $\omega_0$.** $\tau_R$ depends on molecular-relaxation physics; $\omega_0$ depends on system geometry / restoring force. They are independent inputs.
3. **The match between canon Q ≈ 3.5 and any fluid-mechanical Q ≈ 3.5 is incidental** — both happen to be in the moderate-Q regime, but for unrelated structural reasons (canon: participation-channel underdamped at $\zeta = 1/4$; fluid: specific $\omega_0\tau_R$ regime).

**H2 verdict:** weak support at trivial "both in moderate-Q regime" level only. No architectural correspondence; no specific ED forcing of Q ≈ 3.5 in fluid-mechanical viscoelastic oscillators.

---

## 5. H3 Verdict — P7 and P4 Channels

**Verdict: H3 fails for both P7 and P4.**

### 5.1 P7 channel (NS-Q3)

- **Numerical mismatch:** $\zeta = 1/(2Q) = 0.143$ (14.3%) vs. P7 amplitude ratio 3–6%; factor 2.4–4.8× off. No clean algebraic combination matches.
- **Mechanism mismatch:** P7 is nonlinear harmonic generation (cubic in field, $M'(\rho)|\nabla\rho|^2$); Q-damping is linear viscous decay. Different physical channels; both are independent canonical-PDE invariants without canon-level structural link.
- **No P7 → Q derivation** exists in canon. They are independent invariants.

### 5.2 P4 channel (NS-Q4)

- **Different dynamical axes:** P4 governs steady-state mobility-saturation (state-space constitutive); Q governs time-dependent oscillation decay (linear damping). No mechanism-level link.
- **No structural relation:** β values (1.30–2.49 across UDM 10 systems; canonical 2.0) and ζ = 0.143 don't match under any algebraic combination.
- **Indirect influence only:** P4 affects effective viscosity, which affects damping coefficient, which affects ζ. But the resulting Q is *embedding-specific* (depends on density, frequency, geometry), not canon-level architectural.

### 5.3 H3 aggregate

Neither P7 nor P4 architecturally explains Q ≈ 3.5. The two channels investigate distinct aspects of the canonical PDE structure — nonlinear harmonic generation (P7) and steady-state mobility (P4) — neither of which connects to the linear-damping / time-decay structure that Q characterizes. **H3 fails on both channels.**

---

## 6. Aggregate Architectural Classification

The final classification of ED's canonical Q ≈ 3.5:

| Aspect | ED status |
|---|---|
| **Internal-canon invariant** | **Yes.** Q ≈ 3.5 is a real derived property of the canonical PDE's participation-channel ODE in the underdamped regime at canon-default $\zeta = 1/4$. Reproducible from ED-Phys-17/18 simulation traces. Listed as universal invariant in [`../../Architectural_Canon.md`](../../Architectural_Canon.md) §3. |
| **Empirical universal across fluid-mechanical oscillators** | **No.** Q ≈ 3.5 is not a textbook value clustering across viscous-oscillator classes; Q-factors span many orders of magnitude across systems. ED's canon Q ≈ 3.5 overlaps with the moderately-damped regime that includes some specific oscillator classes but is not a concentrated empirical cluster. |
| **Architectural prediction via V5** | **Weak / incidental only.** Match in $\omega_0\tau_R \approx 0.144$ regime is coincidental moderate-damping overlap, not architecturally forced by V5 (which has $\tau_R$ INHERITED). |
| **Architectural prediction via P7** | **No.** Different mechanism class (nonlinear harmonic generation vs. linear damping); numerical mismatch by factor 2.4–4.8×. |
| **Architectural prediction via P4** | **No.** Different dynamical axes (steady-state mobility vs. time-domain damping); no canonical algebraic relation. |

**Aggregate verdict: ED's canonical Q ≈ 3.5 should be framed as an *internal-canon invariant* — a property of canonical-PDE simulation traces — not as a fluid-mechanical universal prediction. No ED architectural channel (P4, P7, V5) forces Q ≈ 3.5 in fluid-mechanical oscillators. The only overlap is generic moderate-damping regime, which is not ED-specific.**

---

## 7. Implications for the ED Program

### 7.1 Framing of Q ≈ 3.5 going forward

The canonical Q ≈ 3.5 should be presented in any future external-facing material (papers, public explainers, orientation documents) as:

- **A canon-internal property** of the canonical PDE's underdamped regime.
- **One of several universal invariants** of the canonical-PDE simulation traces (alongside $D_\mathrm{crit} \approx 0.896$, $N_\mathrm{osc} \approx 9$, harmonic ratio 3–6%, etc.) — listed in Universal_Invariants.md and Architectural_Canon §3.
- **Not** as an empirical fluid-mechanical universal, *not* as a prediction about specific oscillator classes, and *not* as a meaningful match to any known empirical clustering.

This is consistent with the program's structurally-honest methodology: claim what the canon delivers, no more.

### 7.2 No ED → fluid-mechanical Q correspondence

The arc establishes that the apparent agreement between ED's canon Q ≈ 3.5 and Q-values seen in some viscous oscillators is **coincidental moderate-damping overlap**, not architectural correspondence. The three correspondence channels (V5, P7, P4) all fail to deliver a non-trivial structural link.

### 7.3 What this rules out

- **No ED-architectural prediction** for Q-values of viscoelastic oscillators, mechanical pendulums in viscous fluid, Stokes-class oscillations, or any other specific oscillator class.
- **No ED-architectural derivation** of why Q ≈ 3.5 appears across moderately-damped systems (which it doesn't, in any concentrated sense — the apparent clustering is artifactual).

This is consistent with NS-Turb-5's parallel finding: ED's contribution to fluid mechanics in oscillation/turbulence regimes is *limited* — restricted-regime forced-response prediction in NS-Turb arc; no Q-factor prediction in NS-Q arc.

---

## 8. Recommended Next Steps

1. **Close the Q-Factor arc.** This memo (NS-Q5) is the final deliverable. The arc closed at H1 null verdict in 5 brief-note memos (~2.5 effective sessions), as planned.

2. **Optional brief framing-note** for any future external-facing material on ED's universal invariants. Recommend a sentence-level clarification that Q ≈ 3.5 is a canon-internal property of the canonical-PDE simulation traces, not an empirical fluid-mechanical universal. This avoids overclaiming. Could be a single line in any future paper that mentions the universal-invariants block.

3. **Return to the ED-NS Exploration Roadmap** ([`../ED-NS_Exploration_Roadmap.md`](../ED-NS_Exploration_Roadmap.md)). Remaining items per §3 / §6:
   - **#3 Reynolds number from substrate** — stuck on articulation gap; lower priority unless substrate-articulation extension is pursued in parallel.
   - **Standalone-paper drafts:** P4-NN paper (per [`../P4_NN_Synthesis.md`](../P4_NN_Synthesis.md) §9.1) is the highest-value pending program-level deliverable. Sequel to the existing UDM paper. ~2–3 sessions for paper draft beyond existing memo content.
   - **Other roadmap items at lower priority** per the roadmap §6 parking lot.

### Decisions for you — preferred next direction

The honest priority ranking after Q-Factor arc closure:

1. **P4-NN paper draft** — highest value-per-effort; substantive empirical anchoring already in place (UDM β = 1.72 ± 0.37 within 1σ of canonical β = 2.0); publication-grade content.
2. **NS-1/2/3 synthesis paper** — broader scope; structurally significant Clay-NS-relevance content; longer effort.
3. **Memory + orientation updates** — small editorial passes capturing arc closures across NS-Turb, P4-NN, Q-Factor; quick maintenance work.
4. **#3 Reynolds-from-substrate articulation work** — speculative; requires new substrate articulation; lower expected return.

**Recommended next direction: drafting the P4-NN paper.** With the P4-NN arc closed publication-grade and three "ED on Earth" arcs now closed (P4-NN, NS-Turb, Q-Factor), the program has substantial empirical-application content ready for external communication. The P4-NN paper is the most direct deliverable — sequel to the existing UDM paper, tightly anchored empirically, structurally clean.

### Decisions for you

- **Confirm Q-Factor arc closure verdict.** H1 null with H2 weak-coincidental from V5 only; H3 fails on both P7 and P4. Q ≈ 3.5 is canon-internal, not fluid-mechanical universal.
- **Confirm preferred next direction.** Recommended: P4-NN paper draft as highest-value-per-effort program-level deliverable. Alternative: NS-1/2/3 synthesis paper, memory/orientation updates, or specific roadmap follow-on.

---

*NS-Q5 closes the Q-Factor arc. **Final verdict: H1 null.** ED's canonical Q ≈ 3.5 is an internal-canon invariant of the participation-channel ODE in the underdamped regime; it does not correspond to a specific empirical universal in fluid mechanics. H2 weakly supported only at "generic moderate-damping regime overlap" level via V5 (not architectural). H3 fails for both P7 (different mechanism, factor 2.4–4.8× mismatch) and P4 (different dynamical axes). The arc closed at H1 null in 5 brief-note memos as planned — appropriately smaller than the NS-Turb arc's deeper 5-memo analysis. Q ≈ 3.5 should be framed as canon-internal in future external-facing material to avoid overclaiming. P4-NN paper draft recommended as next program-level deliverable.*
