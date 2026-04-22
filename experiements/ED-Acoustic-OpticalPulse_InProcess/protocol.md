# Optical-Pulse Peak-vs-Flank Differential — ED Acoustic-Metric Protocol (Stub)

**Status.** **Thin stub** — awaiting collaboration contact. Experiment 2 of the ED acoustic-analogue experimental program. Native-platform second priority after the EIT differential test.

**Why stub, not full protocol.** Unlike the EIT experiment, this test depends on a specific fibre-nonlinear-optics apparatus that is not widely available and has a known systematic (Belgiorno 2010 blackbody-claim controversy) that requires apparatus-specific noise characterization *before* a pre-registered parameter set can be fixed. The full protocol should be written **after** a collaborating group is identified and their noise-budget is quantified.

**Relationship to prior work.**
- **Strategic framing** — [`theory/ED_Acoustic_Analogue_Experimental_Program.md`](../../theory/ED_Acoustic_Analogue_Experimental_Program.md) §5.2 (Experiment 2) and §8.1 (second-priority rationale).
- **Theoretical basis** — same as the EIT protocol: [`theory/ED_Effective_Acoustic_Metric.md`](../../theory/ED_Effective_Acoustic_Metric.md), [`theory/ED_Acoustic_Metric_Curvature.md`](../../theory/ED_Acoustic_Metric_Curvature.md).
- **Sibling protocol (full)** — [`ED-Acoustic-EIT-Extremal_InProcess/protocol.md`](../ED-Acoustic-EIT-Extremal_InProcess/protocol.md).
- **Known systematic to resolve** — Belgiorno et al. 2010 claimed blackbody emission from a filamentation-induced optical horizon; subsequent reanalyses attributed the signal to Raman scattering and pulse filamentation, not a Hawking mechanism. Any fibre-pulse analogue-horizon measurement inherits this controversy.

---

## 1. The prediction in one paragraph

A bright bell-shaped pulse (Gaussian or sech²) propagating in a nonlinear photonic-crystal fibre creates a co-moving refractive-index profile `n(x)` with a **smooth interior maximum** at the pulse peak. Probe photons co-propagating with the pulse see an effective horizon on the **flanks** of the pulse where `v_g,probe = v_pulse`. Flank horizons are monotonic (non-extremal): `κ_flank > 0`. The **peak** region of the same pulse is an interior-maximum horizon: `κ_peak = 0` by smooth-extremum geometry. A single-apparatus differential is possible: frequency-resolved coincidence counting of probe photon pairs emitted from the flank vs. from the peak region should show thermal spectrum on flanks and no spontaneous pair emission at the peak, within the same pulse geometry.

## 2. Pre-registered test parameters — **TBD pending apparatus specification**

The following are placeholders that depend on the target fibre / pulse / probe wavelength. They must be fixed only after domain-expert review.

| Parameter | Placeholder value | Notes |
|:---|:---|:---|
| Pulse peak intensity `I_0` | TBD | Must be above filamentation threshold but avoid Raman regime for the chosen fibre |
| Pulse duration | TBD | ~100 fs to 1 ps typical |
| Probe-pulse delay vs. driver | TBD | Controls whether probe encounters flank or peak region |
| Fibre nonlinearity `γ_NL` | TBD | Sets the refractive-index change amplitude |
| Fibre length | TBD | Balance between horizon formation time and loss |
| Photon-pair signal band | TBD | Frequency-shifted from probe by the Hawking-analogue formula |
| **Primary observable** | Flank-vs-peak pair-emission ratio `R_flank / R_peak` | Prediction: `R_peak / R_flank < 0.1` |
| **Secondary observable** | Flank-emission spectrum thermality | Fit to blackbody vs. non-thermal forms |
| **Systematic filter** | Raman / filamentation contribution to each band | Independent characterization required |

**Action item.** Draft the pre-registered parameter table *only* after a collaborating group's apparatus has been characterized on the Belgiorno-systematic dimensions.

---

## 3. Apparatus requirements (summary)

- Nonlinear photonic-crystal fibre with characterized dispersion and nonlinearity.
- Femtosecond-pulse laser with stable repetition rate.
- Frequency-resolved single-photon detection (e.g. superconducting nanowire single-photon detectors) with time-tagging.
- Coincidence-counting electronics.
- Raman-filter and filamentation-diagnostic subsystems.
- Spatially-resolved pump-probe geometry to distinguish peak-region from flank-region pair emission.

---

## 4. Collaboration targets

- **Philbin group (St Andrews)** — original optical-analogue-horizon group.
- **König group (St Andrews)** — related.
- **Faccio group (Glasgow)** — pulse-horizon and quantum-optics expertise; independent of Belgiorno controversy.
- **Leonhardt (Weizmann)** — theoretical underpinning of optical analogue gravity.

## 5. Key open question before executing

**Can peak-region and flank-region pair emission be spatially distinguished in a single pulse geometry?** The answer depends on pulse length, fibre dispersion, and detector resolution. If the answer is no — if all pair emission is indistinguishably lumped — then the within-apparatus differential collapses and this experiment reduces to a standard analogue-horizon measurement with the associated controversy. Resolve this question before any pre-registration.

---

## 6. What this stub does not do

- Does not substitute for a full protocol; outreach to any of the §4 groups should be accompanied by a request for their feedback on §2 parameter fixing and §5 open question before a full protocol is drafted.
- Does not prejudge Belgiorno-controversy noise floor for a specific apparatus. Each fibre + laser combination has its own Raman / filamentation / dispersion-mixing systematics.
- Does not commit to a timeline; this is a follow-up to the EIT experiment, not a parallel priority.

**When this stub graduates to a full protocol.** When (a) a collaborating group is committed; (b) their apparatus Raman / filamentation noise floor is quantified; (c) the spatial-distinguishability question in §5 is answered in the affirmative for that apparatus. Until then, this stub documents the experimental concept at the level needed for outreach but not for execution.
