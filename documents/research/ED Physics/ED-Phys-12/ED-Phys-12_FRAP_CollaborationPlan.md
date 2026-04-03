# ED-Phys-12: Experimental Collaboration Plan — BSA-FRAP Void-Spreading Test

**Author:** Allen Proxmire
**Series:** ED-Phys-12
**Date:** March 2026
**Status:** Ready for distribution to collaborators

---

# 1. Executive Summary

We seek a collaborator with confocal FRAP capability to perform a single, decisive experiment: **measure the rate at which a photobleached spot recovers in a concentrated BSA protein solution.**

Standard FRAP experiments at dilute concentrations show recovery fronts that expand as $R(t) \propto t^{0.5}$ (Fickian diffusion). We predict that at high BSA concentration (200--350 mg/mL), the recovery front expands much more slowly:

$$R(t) \propto t^{0.16}$$

This specific exponent ($\alpha_R = 0.160 \pm 0.009$) is a zero-free-parameter prediction of the Event Density (ED) framework — a nonlinear diffusion theory that has been validated against 10 materials for its constitutive law but never tested for its dynamical front-propagation prediction. The experiment requires no specialised equipment beyond a standard confocal microscope with FRAP module, BSA-FITC conjugate, and temperature control.

**Why this experiment is decisive:** It is the first test of a *dynamical* ED prediction (front speed), as opposed to the *static* predictions (diffusion coefficient vs. concentration) that have been validated. A positive result would confirm that the ED porous-medium equation governs real protein dynamics at high concentration. A negative result (Fickian recovery at all concentrations) would falsify the dynamical prediction and restrict the ED mobility law to a phenomenological description of $D(c)$ only.

**What the collaborator contributes:** Sample preparation, FRAP imaging, and raw data (TIFF stacks). All data analysis, fitting, and interpretation will be performed on our side.

---

# 2. Scientific Background

## 2.1 The ED Mobility Law

We have tested a specific functional form for how diffusion slows in crowded solutions:

$$D(\phi) = D_0\,M_0\!\left(1 - \frac{\phi}{\phi_{\max}}\right)^\beta$$

where $\phi$ is volume fraction, $\phi_{\max}$ is the packing limit, and $\beta$ is the mobility exponent. Across 10 materials — colloids, proteins, polymers, polysaccharides, and small molecules — this law fits with $R^2 > 0.986$ and gives $\beta \approx 1.7 \pm 0.4$. For BSA specifically, $\beta = 2.12 \pm 0.18$.

## 2.2 The Front-Propagation Prediction

The mobility law implies that concentration fronts (boundaries between concentrated and dilute regions) propagate as a power law:

$$R(t) \propto t^{\alpha_R}, \qquad \alpha_R = \frac{1}{d\beta + 2}$$

where $d$ is the spatial dimension. For BSA in the 2D geometry of a FRAP experiment:

$$\alpha_R = \frac{1}{2 \times 2.12 + 2} = 0.160$$

This is dramatically different from Fickian diffusion ($\alpha_R = 0.5$). A measurement with even 20% precision would distinguish the two.

## 2.3 Why Standard Experiments Cannot Test This

We have shown computationally (ED-Phys-09) that standard concentration-spreading experiments — where a solute bump diffuses into a dilute background — do not produce the predicted exponent. The reason: the diffusion front propagates into the region where $D$ is *large* (fast diffusion), not where $D \to 0$ (the degenerate regime where the ED prediction applies).

The correct geometry requires a *void* (low-concentration region) spreading into a *dense* background. FRAP provides exactly this: the bleached spot is the void, and the concentrated unbleached background is the dense matrix.

## 2.4 Synthetic Validation

We have simulated the experiment computationally (ED-Phys-11) using the 2D porous-medium equation with BSA parameters. The simulated FRAP recovery produces $\alpha_R = 0.156$ (half-maximum front) and $\alpha_R = 0.142$ (threshold front), both consistent with the prediction of 0.160 within the expected finite-time correction. The measurement pipeline (front detection, log-log fitting, bootstrap uncertainty) has been validated on this synthetic data.

---

# 3. Experimental Requirements

## 3.1 Sample Preparation

| Item | Specification | Notes |
|------|---------------|-------|
| Protein | BSA (bovine serum albumin, Fraction V, $\geq 96\%$) | Sigma-Aldrich A7906 or equivalent |
| Fluorescent label | BSA-FITC or BSA-Alexa488 conjugate | Pre-labelled commercial product or in-house conjugation |
| Labelling ratio | 0.5--2.0 dye/protein | Low enough to avoid self-quenching |
| Concentrations | 200, 250, 300, 350 mg/mL (4 points) | Prepare by dissolving lyophilised BSA-FITC in buffer |
| Buffer | 50 mM sodium phosphate, pH 7.0, 150 mM NaCl | Standard physiological; minimises aggregation |
| Temperature | 25.0 $\pm$ 0.5 $^\circ$C | Must be controlled during imaging |
| Sample chamber | Coverslip sandwich with 10--50 $\mu$m spacer | Thin chamber for quasi-2D geometry |
| Volume per sample | $\sim 5$ $\mu$L | Fills the thin chamber |

## 3.2 Imaging Setup

| Parameter | Required | Preferred |
|-----------|----------|-----------|
| Microscope type | Confocal (any brand) | Laser-scanning confocal with FRAP module |
| Excitation wavelength | 488 nm | — |
| Emission filter | 500--550 nm (FITC/Alexa488 channel) | — |
| Objective | 40$\times$ or 63$\times$, NA $\geq 1.2$ (water immersion preferred) | 63$\times$/1.4 oil |
| Pixel size | $\leq 0.4$ $\mu$m | 0.1--0.2 $\mu$m |
| Frame rate | $\geq 10$ fps | 30--60 fps |
| Bit depth | 12-bit or 16-bit | — |
| Temperature stage | $\pm 0.5$ $^\circ$C stability | Okolab or similar incubation chamber |

## 3.3 Photobleaching Parameters

| Parameter | Value |
|-----------|-------|
| Bleach wavelength | 488 nm (same as imaging laser, full power) |
| Bleach geometry | Circular ROI, radius 2--5 $\mu$m |
| Bleach iterations | 10--50 scans at full power |
| Bleach duration | 0.5--2.0 s total |
| Target bleach depth | $> 80\%$ fluorescence reduction at ROI centre |
| Post-bleach delay | 0 (begin recording immediately after bleach) |

---

# 4. Measurement Protocol

## 4.1 Step-by-Step Procedure

**For each concentration (200, 250, 300, 350 mg/mL):**

1. **Prepare sample chamber.** Place $\sim 5$ $\mu$L of BSA-FITC solution between coverslip and slide with spacer. Seal edges with vacuum grease.

2. **Mount on microscope.** Allow 10 min for thermal equilibration on the temperature stage.

3. **Find a clear field.** Choose a region away from air bubbles, dust, or chamber edges ($> 20$ $\mu$m from any boundary).

4. **Acquire pre-bleach baseline.** Record 5--10 frames at imaging power. Save as the reference $I_{\text{pre}}(x,y)$.

5. **Bleach.** Switch to full-power 488 nm in the circular ROI. Bleach for the specified duration. Immediately switch back to imaging power.

6. **Record recovery movie.** Acquire frames at the specified rate for 2 s total (or longer if recovery is slow). Save as a TIFF stack.

7. **Verify bleach depth.** In the first post-bleach frame, check that the centre of the ROI has $< 20\%$ of the pre-bleach intensity.

8. **Repeat.** Perform 3--5 replicate bleaches per concentration, each in a different field of view.

## 4.2 Total Experiment Time

| Task | Time |
|------|------|
| Sample preparation (4 concentrations) | 2--4 hours |
| Mounting + equilibration (per sample) | 15 min |
| FRAP acquisition (5 replicates $\times$ 2 s + setup) | 15 min per concentration |
| Total imaging time | $\sim 1.5$ hours |
| **Total experiment time** | **4--6 hours** |

---

# 5. Data Processing Pipeline

All analysis will be performed on our side using validated code. The collaborator sends raw data; we return the extracted $\alpha_R$ values and comparison to the ED prediction.

## 5.1 Pipeline Steps

1. **Load TIFF stack** and pre-bleach reference.
2. **Compute fluorescence deficit:** $\delta(x,y,t) = 1 - I(x,y,t)/I_{\text{pre}}(x,y)$.
3. **Identify bleach centre** from the first post-bleach frame (centroid of the deficit).
4. **Radial averaging:** Compute $\delta(r, t)$ in annular bins (width = 1 pixel).
5. **Front detection** at each time frame:
   - Half-maximum: $R(t)$ where $\delta(r) = \delta_{\text{centre}} / 2$.
   - Threshold: $R(t)$ where $\delta(r) = 0.1 \times \delta_{\text{centre}}(t_0)$.
6. **Power-law fit:** $\ln R = \alpha_R \ln t + \text{const}$ on the interval $[0.05\text{ s}, 1.0\text{ s}]$.
7. **Bootstrap uncertainty:** 1000 resamples.
8. **Threshold sensitivity:** Compare half-max and threshold results.
9. **Compare to prediction:** $\epsilon = |\alpha_R^{\text{meas}} - 0.160| / \sigma_{\text{total}}$.

## 5.2 Quality Checks

| Check | Criterion |
|-------|-----------|
| Bleach depth | Centre intensity $< 20\%$ of pre-bleach |
| Bleach symmetry | Aspect ratio of the deficit region $< 1.2$ |
| Drift | Centre position moves $< 0.5$ $\mu$m over 2 s |
| Noise | Signal-to-noise at the front $> 3$ |
| $R^2$ of fit | $> 0.95$ |

---

# 6. Deliverables

## 6.1 What the Collaborator Sends

| Item | Format | Notes |
|------|--------|-------|
| Raw TIFF stacks | 16-bit TIFF, one stack per replicate | Include pre-bleach frames |
| Metadata file | Text or spreadsheet | Frame rate (fps), pixel size ($\mu$m), bleach ROI coordinates, bleach duration, BSA concentration, temperature |
| Bleach depth verification | One image or number | Centre intensity as fraction of pre-bleach |

## 6.2 What We Return

| Item | Timeline |
|------|----------|
| Extracted $\alpha_R$ per concentration with uncertainties | 1 week after data receipt |
| Comparison to ED prediction ($\epsilon$ and classification) | Same |
| Plots: $R(t)$, log-log fit, radial profiles, residuals | Same |
| Draft results section for joint publication (if warranted) | 2 weeks after data receipt |

---

# 7. Timeline and Milestones

| Week | Task | Milestone |
|------|------|-----------|
| 1 | Sample prep + pilot FRAP at one concentration | Pilot data reviewed; bleach depth and frame rate confirmed |
| 2 | Full dataset: 4 concentrations $\times$ 5 replicates | 20 TIFF stacks delivered |
| 3 | Analysis: front extraction, $\alpha_R$ fitting | Preliminary $\alpha_R$ values reported |
| 4 | Joint interpretation meeting | Verdict (Strong confirmation / Consistent / Tension / Falsified) |

**Total calendar time: 4 weeks from start of sample prep to final verdict.**

---

# 8. Risks and Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Bleach depth $< 80\%$ | Moderate | Cannot enter nonlinear regime | Increase laser power or dwell time; use longer bleach duration |
| Convection during recovery | Low (high viscosity) | Drift corrupts radial averaging | Seal chamber completely; verify drift $< 0.5$ $\mu$m |
| Recovery too fast to resolve | Moderate at 200 mg/mL | Few data points in power-law regime | Increase frame rate to 60 fps; reduce temperature to 20 $^\circ$C to slow diffusion |
| Recovery too slow to complete | Low | Cannot see approach to plateau | Extend recording time to 5--10 s |
| Photobleaching artifacts (chemical damage) | Low | Irreversible bleach mimics degenerate mobility | Use Alexa488 (more photostable); verify by repeated bleaching of same region |
| BSA aggregation at high concentration | Moderate at $> 300$ mg/mL | Non-Brownian dynamics | Filter sample through 0.22 $\mu$m before loading; check DLS for aggregates |
| Insufficient signal-to-noise | Moderate | Noisy front positions | Average over 5 replicates; apply mild smoothing (1-pixel Gaussian) |

---

# 9. Contact and Collaboration Structure

## 9.1 Roles

| Role | Responsibility |
|------|----------------|
| **Theory/analysis (our side)** | Experimental design, data analysis pipeline, $\alpha_R$ extraction, comparison to prediction, manuscript drafting |
| **Experiment (collaborator)** | Sample preparation, FRAP imaging, raw data delivery, pilot experiment feedback |

## 9.2 Data Sharing

- **Method:** Shared cloud folder (Google Drive, Dropbox, or institutional equivalent).
- **Organisation:** One folder per concentration, containing TIFF stacks and metadata.
- **Naming convention:** `BSA_FITC_{conc}mgmL_rep{N}_fps{rate}.tif`

## 9.3 Authorship

If the experiment produces a publishable result (positive or negative), we propose joint authorship with the collaborator contributing the experimental data and the theory side contributing the analysis and interpretation. Specific authorship order to be discussed after results are in hand.

## 9.4 What the Collaborator Does NOT Need to Know

This protocol is self-contained. The collaborator does not need to understand the Event Density framework, the porous-medium equation, or the theoretical basis for the $\alpha_R$ prediction. They only need to:
1. Prepare concentrated BSA-FITC.
2. Perform standard confocal FRAP.
3. Send us the raw data.

We handle everything else.

---

*ED-Phys-12 · Event Density Research Programme · March 2026*
