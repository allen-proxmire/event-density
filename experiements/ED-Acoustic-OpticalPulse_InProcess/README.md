# ED-Acoustic-OpticalPulse — Optical-Pulse Peak-vs-Flank Differential (Stub, In Process)

**Target prediction.** ED acoustic metric → pulse-peak interior maxima are extremal (`κ = 0`); pulse flanks are monotonic horizons (`κ > 0`). Single-apparatus differential between peak-region and flank-region pair emission.

**Origin.** Experiment 2 of the ED acoustic-analogue experimental program. Native-platform second priority after the EIT differential test. See [`theory/ED_Acoustic_Analogue_Experimental_Program.md`](../../theory/ED_Acoustic_Analogue_Experimental_Program.md) §5.2, §8.1.

**Observable.** Pair-emission-rate ratio `R_peak / R_flank` within a single pulse geometry.

**Prediction.** `R_peak / R_flank < 0.1` with thermal flank spectrum, no peak emission above shot-noise.

**Platform.** Nonlinear photonic-crystal fibre with femtosecond pulse driver + co-propagating probe; frequency-resolved coincidence-counting detection.

**Methodological strength.** Native-extremal platform — the pulse peak automatically provides an interior-maximum refractive-index profile. No shaped control field required.

**Methodological risk.** Belgiorno et al. 2010 controversy — filamentation + Raman can mimic blackbody-like emission at an analogue-horizon. Any measurement on this platform inherits this systematic and must characterize it apparatus-by-apparatus.

**Status.** **Stub protocol, 2026-04-22.** Full protocol deferred until: (a) collaborating group committed; (b) apparatus Raman/filamentation noise floor quantified; (c) peak-vs-flank spatial-distinguishability confirmed for that apparatus. See [`protocol.md`](protocol.md) §5 for the open question.

**Files.**
- [`protocol.md`](protocol.md) — stub protocol documenting concept, placeholder parameters, and open questions.

**Primary collaboration targets.** Philbin (St Andrews), König (St Andrews), Faccio (Glasgow), Leonhardt (Weizmann).

**Cross-references.**
- [`theory/ED_Acoustic_Analogue_Experimental_Program.md`](../../theory/ED_Acoustic_Analogue_Experimental_Program.md) — parent program memo.
- [`ED-Acoustic-EIT-Extremal_InProcess/`](../ED-Acoustic-EIT-Extremal_InProcess/) — sibling experiment (full protocol, top priority).
- [`ED-Acoustic-BEC-Extremal_InProcess/`](../ED-Acoustic-BEC-Extremal_InProcess/) — sibling experiment (stub, high-profile follow-up).
