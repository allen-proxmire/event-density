# BEC Engineered Extremal Horizon — ED Acoustic-Metric Protocol (Stub)

**Status.** **Thin stub** — awaiting theory extension + collaboration contact. Experiment 3 of the ED acoustic-analogue experimental program. Highest-profile follow-up after within-apparatus differentials (EIT, optical pulse) have narrowed the parameter space.

**Why stub, not full protocol.** This experiment requires:

1. **Theory extension to moving backgrounds (v_0 ≠ 0).** The current ED acoustic-metric derivation ([`theory/ED_Effective_Acoustic_Metric.md`](../../theory/ED_Effective_Acoustic_Metric.md)) is for stationary backgrounds. BEC acoustic horizons are transonic: `v² − c_s² = 0`. Mapping ED's interior-max extremal prediction onto a transonic BEC horizon requires the moving-background extension, which is flagged as a deferred theory-memo target in [`theory/ED_Acoustic_Analogue_Experimental_Program.md`](../../theory/ED_Acoustic_Analogue_Experimental_Program.md) §9.
2. **Trap + flow engineering beyond standard Steinhauer protocols.** The extremal-horizon class in BEC requires `v²(x) − c_s²(x)` to have a smooth second-order zero at an interior point — not the linear transonic crossing Steinhauer-style setups produce by default. This needs custom trap design and flow-profile tailoring.
3. **Long-standing technical collaboration.** Steinhauer-group or Westbrook-group collaboration is a multi-year commitment, not a one-off.

**Relationship to prior work.**
- **Strategic framing** — [`theory/ED_Acoustic_Analogue_Experimental_Program.md`](../../theory/ED_Acoustic_Analogue_Experimental_Program.md) §5.3 (Experiment 3), §8.1 (fourth-priority ranking), §9 (theory extension required).
- **Reference experiments** — Steinhauer 2014, 2016, 2019 (stimulated / spontaneous Hawking-pair correlations in standard transonic BEC).
- **Sibling protocols** — [`ED-Acoustic-EIT-Extremal_InProcess/`](../ED-Acoustic-EIT-Extremal_InProcess/) (full, top priority), [`ED-Acoustic-OpticalPulse_InProcess/`](../ED-Acoustic-OpticalPulse_InProcess/) (stub, second priority).

---

## 1. The prediction in one paragraph (pending theory extension)

In an elongated 1D BEC with engineered trap potential and condensate flow, an acoustic horizon forms where `v(x) = c_s(x)`. A **monotonic** horizon (Steinhauer-style: first-order crossing) has `κ = (1/2)|d(c_s² − v²)/dx|_horizon > 0` and emits Hawking-analogue thermal phonon pairs. An **extremal** horizon — engineered by shaping the trap + flow such that `v²(x) − c_s²(x)` has a smooth second-order zero at an interior point `x_0` — has `κ = 0` and should emit no Hawking-analogue phonon pairs. The density-density correlation function `G(x, x')` is the primary observable (following Steinhauer 2016 methodology): in the monotonic case, show peaked correlations along the null-ray locus; in the extremal case, peaks should be suppressed below the noise floor.

**Theoretical caveat.** The current ED acoustic-metric derivation covers `v_0 = 0` only. Whether ED's P4 mobility-collapse structure generically produces extremal BEC horizons when extended to moving backgrounds is not yet established.

## 2. Pre-registered test parameters — **TBD pending theory + apparatus specification**

| Parameter | Placeholder | Notes |
|:---|:---|:---|
| Condensate species | Rb-87 or Na | Standard BEC analogue-gravity choice |
| Atom number | ~10⁵ | Balance between SNR and mean-field validity |
| Trap geometry | Elongated quasi-1D | Required for horizon localization |
| Flow protocol | Sweep of magnetic-field / dipole-force step | Engineered for extremal profile (TBD) |
| Horizon-profile engineering | Smooth second-order zero of `v² − c_s²` at `x_0` | **Requires trap + flow co-design; not yet specified** |
| **Primary observable** | `G(x, x')` correlation peak amplitude at null-ray locus | Prediction: suppressed in extremal config |
| **Secondary observable** | Phonon momentum distribution at Hawking-analogue frequency | Prediction: no thermal tail |
| **Surface-gravity extraction** | Bogoliubov-coefficient analysis on density-density spectrum | Prediction: `κ_E ≈ 0`, `κ_M > 0` |

**Action item.** Full parameter specification deferred until (i) moving-background ED theory extension is complete; (ii) trap + flow co-design is validated in a partner group's numerical model.

---

## 3. Apparatus requirements (summary)

- Elongated Rb-87 BEC with custom dipole-trap or magnetic-trap shaping.
- Stable flow-production protocol (e.g. time-dependent trap displacement).
- High-resolution in-situ imaging for density-profile extraction.
- Time-of-flight + absorption imaging for phonon momentum distribution.
- Density-density correlation analysis pipeline (Steinhauer-established methodology).

## 4. Collaboration targets

- **Steinhauer group (Technion)** — original BEC Hawking-analogue measurements; density-density correlation analysis pipeline.
- **Westbrook group (Institut d'Optique)** — independent BEC analogue-gravity work.
- **Cornell / Jin (JILA)** — cold-atom expertise, broader scope.
- **Ferrari group (Trento)** — Bogoliubov and analogue-gravity theory + experiment.

## 5. Blocking items before stub → full protocol

1. **Theory extension.** Moving-background ED acoustic metric memo must be written. This is a prerequisite to specifying the BEC prediction precisely.
2. **Trap + flow co-design.** A partner group's numerical model (Gross-Pitaevskii simulation) showing the extremal-profile configuration is physically realizable with feasible trap + atom-number parameters.
3. **Differential configuration feasibility.** The Steinhauer paradigm produces one horizon per run; a within-apparatus monotonic-vs-extremal comparison requires two runs (or two simultaneous horizons in a dual-well geometry). Operational feasibility needs partner-group confirmation.

---

## 6. What this stub does not do

- Does **not** prejudge whether ED's P4 mobility-collapse structure survives the moving-background extension. The theory may constrain extremal BEC horizons differently than static interior-max cases.
- Does **not** commit to a timeline. Conditional on the blocking items in §5 being resolved.
- Does **not** promise within-apparatus differential structure at the level the EIT experiment offers. BEC measurements are per-run, not toggle-based, which weakens the systematic-cancellation argument compared to the EIT test.

**When this stub graduates to a full protocol.** When (a) the moving-background ED theory extension memo is complete; (b) a partner group has modelled the extremal-profile configuration in GPE and confirmed physical realizability; (c) a two-run or dual-well differential-configuration protocol is designed. Until then, this stub documents the experimental concept at the level needed for informal outreach but not for execution.

**Informal outreach note.** Because Aspelmeyer-group contact is already planned for ED-09.5 Track A, an indirect pathway to BEC-analogue collaborators (via Aspelmeyer → Vienna ecosystem) may exist. Not prioritized at this stage.
