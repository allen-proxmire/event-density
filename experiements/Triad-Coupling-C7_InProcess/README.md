# Triad-Coupling-C7 — Nonlinear Triad Coupling Experiment (In Process)

**Target axiom.** Canon P7 / C7 — `M′(ρ)|∇ρ|²` generates k=3 from k=1 with invariant triad ratio.

**Origin.** Stage 4 of the Test-to-Axiom Mapping Project — identified C7 as the most load-bearing under-tested axiom in the current four-test ED empirical program.

**Observable.** Modal amplitude ratio `A₃/A₁` between third-harmonic and fundamental under single-mode drive or spontaneous single-mode organization; `A₃ ∝ A₁²` scaling; phase lock.

**Prediction.** `A₃/A₁ ∈ [0.02, 0.08]` (from ED-Phys-16 coupling ~0.03, harmonic 3–6%).

**Routes.** Three execution paths, ranked by marginal coverage gain per unit cost:

1. **Top-1** — AFM Spinodal-Dewetting Fourier Triad Reanalysis ($0–500, 1–6 weeks, reuses T1 pipeline).
2. **Alt-1** — Nonlinear RLC Third-Harmonic Generation (~$20, 1–2 weeks, reuses T4 rig + diode).
3. **Alt-2** — Patterned-FRAP k=3 Recovery (~$2000–5000, 4–8 weeks, reuses T2 sample prep).

Theoretical companion: Telegraph-PME triad simulation ($0, CPU-only) — calibrates the prediction band from first principles.

**Status.** Protocol drafted 2026-04-22. No route yet executed. Simulation companion is the recommended first step.

**Files.**
- [`protocol.md`](protocol.md) — full session-ready protocol (three routes, analysis pipeline, decision tree).

**Cross-references.**
- [`docs/ED-Test-to-Axiom-Mapping-v1.0.md`](../../docs/ED-Test-to-Axiom-Mapping-v1.0.md) — origin document.
- [`AFM-Dewetting-ED-SC_InProcess/protocol.md`](../AFM-Dewetting-ED-SC_InProcess/protocol.md) — reused for Top-1.
- [`FRAP-High-BSA_InProcess/protocol.md`](../FRAP-High-BSA_InProcess/protocol.md) — reused for Alt-2.
- [`ED-RLC-Analogue_InProcess/`](../ED-RLC-Analogue_InProcess/) — reused for Alt-1.
- [`edsim/phys/analogues/telegraph_pme.py`](../../edsim/phys/analogues/telegraph_pme.py) — simulation companion codebase (post 2026-04-22 line-162 patch).
