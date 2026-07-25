# Khronon vs Lorentz in Jacobson's Derivation — RUNNING RESULTS LOG

**Date opened:** 2026-07-24
**Status:** OPEN research thread. Running log; write-up to follow when the thread closes. Append results as they land; do not delete (audit trail).

## The question
Jacobson's 1995 equation-of-state derivation assumes **local Lorentz invariance** ("an approximately flat region with the usual Poincaré symmetries," Unruh boost-thermality, boost Killing field). ED's gravity is **khronometric** — a preferred foliation (the khronon = the arrow made dynamical, GR-II). So: (a) *where* in Jacobson's derivation does Lorentz enter? (b) what does the khronon do to each such step? (c) does the deviation map to ED's preferred-frame parameters `α₁, α₂` (GR-IV: `α₂=0` exact, `α₁` ~70 orders below bounds)? Working hypothesis (to test/break): in ED the derivation runs on a **universal horizon** (khronon-trapping surface = the `b→0` locus), not the metric Rindler horizon, and the preferred-frame corrections are governed by `α₁, α₂`.

## Where Lorentz enters Jacobson (from the paper, read in full)
1. **Unruh temperature** `T=ħκ/2π` — assumes the Minkowski vacuum is *thermal w.r.t. boosts* (boost invariance of the vacuum).
2. **Boost Killing field `χ`** — "approximately flat region with the usual Poincaré symmetries" (p4); all boost directions equivalent.
3. **Local Rindler horizons "in all null directions"** — isotropy of the light cone / no preferred frame.
4. **Entanglement entropy across the horizon** — Lorentz-invariant vacuum correlations.

## Results (append below, dated)

### R1 — ED khronometric side (GR-IV, read in full) — DONE
Key facts (Paper_GR-IV_ArrowsAlibi):
- **Both gravitational cones are LUMINAL:** tensor `c_T = c` (single P05 transport) and scalar/khronon `c_s = c` (GR-III: the reserve sector is dissipative, not kinetic). No superluminal mode.
- **`α₂ = 0` EXACTLY** — a structural consequence of both cones luminal (`c_T=c, c_s=c`), independent of any tuning. Verified by GR-IV against the published khronometric PPN formulas (Hořava arXiv:1105.5149 eq.31; Blas–Sibiryakov arXiv:1412.4828). So the *tighter* preferred-frame bound is met for free.
- **`α₁ = −4λ_local`**, `λ_local = f²/M_P² = (k₁₁/s₀₂)·ρ_event/ρ_Planck`. Metric stiffness `M_P²` is ALWAYS-ON (P02 reciprocal sharing, density-independent, Planck-dense); khronon stiffness `f²` tracks COMMITMENT density (P11, sparse). Their ratio = the commitment sparsity.
- **`λ_local ≪ 1` forced** (dense commitment = quantum Zeno = no QM). So `α₁ ~ 10⁻⁹³`, ~70+ orders below the bound. ED is a *screened* khronometric theory: observationally GR except at Planck density.
- **Two faces of the khronon:** LOCAL (stiffness `λ_local` → `α₁`) vs COSMOLOGICAL (decoupling surface `R_H=c/H₀` → `a₀=cH₀/2π`, MOND). Different scales.

**Immediate implication for the thread (candidate, to verify in R2/R3):** Jacobson's derivation is LOCAL (local Rindler horizons) and rests on the light-cone/Unruh structure. ED's `α₂=0` (both cones luminal) means the causal/null structure is the STANDARD light cone — so Rindler horizons + Unruh temperature are unmodified at that order. The only Lorentz-violating footprint is `α₁ = −4λ_local ~ ρ_event/ρ_Planck` — a velocity-dependent correction, ~70 orders suppressed. So the hypothesis sharpens: **the khronon enters Jacobson's derivation only at the `α₁` level (tiny, density-suppressed); the luminal cones (`α₂=0`) keep Jacobson's kinematic scaffolding (light cone, Rindler, Unruh) intact.** Also: because `c_s=c` (no superluminal khronon), ED plausibly has NO separate "universal horizon" complication (that arises in Hořava from superluminal modes) — the metric horizon is the causal horizon. **Verify the universal-horizon and Unruh-in-LV claims in R2.**

### R2 — external literature (web, cited) — DONE
**CONFIRMED (settled):**
- **Universal horizon requires superluminal modes.** It exists because the khronon/scalar can propagate superluminally, so the metric (Killing) horizon isn't a true trapping surface (Barausse–Jacobson–Sotiriou arXiv:1104.2889; Blas–Sibiryakov arXiv:1110.2195). **Luminal-coincidence holds:** if all modes are luminal, the metric light-cone is the true causal boundary and the universal horizon collapses onto the metric horizon. (Strongly implied by the construction; not isolated as a headline theorem, but solid.) → **ED (`c_s=c`) dodges the universal-horizon complication.**
- **`α₂ = 0` exactly, `α₁ = −4α`, in the luminal limit — VERIFIED ANALYTICALLY** from the literature's own PPN formulas (Ramos–Barausse arXiv:1811.07786 Eqs.17/19; Blas–Lim arXiv:1412.4828; Foster–Jacobson gr-qc/0509083). `c_T=c ⇒ β=0`; `c_s=c ⇒ α=λ/(2λ+1)`; then `α₂ ≡ 0` across the whole luminal family and `α₁=−4α` is the sole preferred-frame handle. **Matches GR-IV exactly** (`α₁=−4λ_local`, `α₂=0`).
- **Unruh temperature survives luminal Lorentz violation.** The thermality-breaker is dispersion *nonlinearity*, not the preferred frame: linear/luminal dispersion preserves KMS/thermality (arXiv:2102.08944); nonlinear/superluminal breaks it (Campo–Obadia arXiv:1003.0112). Direct "rescue" in LV gravity via aether-flow (arXiv:2312.03070), reducing to standard Rindler in the luminal/IR regime. → **`T=ħκ/2π` expected to survive in ED.**

**CORRECTIONS / NEW subtlety:**
- **Citation error in GR-IV:** it cites arXiv:1105.5149 as "Hořava PPN eq.31," but that ID is Blas–Sanctuary (GW radiation), NOT the PPN derivation. Correct refs: Blas–Lim arXiv:1412.4828, Foster–Jacobson gr-qc/0509083, Ramos–Barausse arXiv:1811.07786. **→ fix in GR-IV.**
- **NON-EQUILIBRIUM subtlety (the real new find):** Eling–Guedens–Jacobson (gr-qc/0602001, "Nonequilibrium Thermodynamics of Spacetime") showed any horizon entropy density that is *not pure area* forces an internal entropy-production term — the Clausius relation goes **non-equilibrium** (`dS = δQ/T + d_iS`). Generic khronometric BH thermo carries a non-area *aether entropy* + an extra first-law term (Berglund–Bhattacharyya–Mattingly arXiv:1210.4940, 1309.0907; 2606.27437).
- **ABSENT in the literature:** nobody has actually carried out Jacobson's *local-Rindler* `δQ=TdS` derivation for khronometric/aether gravity and shown the corrections are `α₁`-governed. So "Jacobson survives in ED with `α₁` corrections" is an **open, unwritten inference**, not a citable theorem.

### R3 — synthesis — DONE (honest, tiered)
- **(b) GROUNDED:** ED's luminal cones (`c_T=c_s=c`) keep Jacobson's *kinematic scaffolding* intact — no universal-horizon complication (superluminal-mode artifact ED avoids), Unruh `T=ħκ/2π` preserved (linear dispersion), `α₂=0` exactly (verified). So the "khronometric-vs-Lorentz obstruction" I first flagged is **real but benign at the kinematic level.**
- **(a) OPEN, and the crux is equilibrium-vs-non-equilibrium ENTROPY, not the α₁ velocity term.** The literature's non-equilibrium result reframes the question: does the khronon add a *non-area* entropy to ED's horizon? If ED's horizon entropy is *pure area* (GR-III §7.4 *measured* the severance count scales as perimeter `r_h^0.96`, holographic), then ED may stay in the **tidy equilibrium regime** — and Jacobson's clean derivation applies. If the khronon adds a non-area piece, the derivation goes **non-equilibrium** (`d_iS` term). **This is the open crux.**
- **The beautiful connection (a LEAD, not a claim):** the non-equilibrium `d_iS` term is *exactly* what Jacobson himself flagged in 1995 (p6: "non-equilibrium spacetime," where the equilibrium Einstein EoS fails at high frequency/amplitude) — and in ED that is **the arrow** (P11 irreversibility, the khronon = the arrow made dynamical). So *if* the khronon enters as a non-area entropy, **the khronon's footprint in Jacobson's derivation is the entropy-production term = ED's arrow = Jacobson's own "non-equilibrium spacetime."** This would map the How-Coarse-Grain thesis (thermo keeps the arrow; the arrow shows in the non-equilibrium correction) onto Jacobson's machinery precisely. Flagged as a lead to test, NOT banked.
- **Net answer to the thread:** the khronon does NOT obstruct Jacobson kinematically (luminal cones make it benign — grounded). WHERE it enters is the entropy: either (i) pure area → equilibrium Jacobson applies cleanly, `α₁` the only tiny correction; or (ii) non-area khronon entropy → non-equilibrium, and the extra term is the arrow. **Deciding (i) vs (ii) is the genuine open derivation** — a real target, carryable via the Eling–Guedens–Jacobson non-equilibrium machinery + ED's severance entropy + the khronon.

## Write-up scope (when the thread closes)
Grounded: (b) luminal cones ⇒ Jacobson scaffolding survives; `α₂=0`; Unruh survives; no universal horizon. Open lead: (a) equilibrium-vs-non-equilibrium entropy; the khronon-as-non-equilibrium-arrow connection. Fix: GR-IV citation (1105.5149). Do NOT claim (a) as done.

## Honest guardrail
Do NOT force a clean "khronon → α₁,α₂" map (fifth+ over-bank risk this session). If it's indeterminate or the universal-horizon identification doesn't hold, log that. Adversarially check any positive claim before banking.
