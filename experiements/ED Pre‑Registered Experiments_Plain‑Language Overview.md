# ED Pre‑Registered Experiments — Plain‑Language Overview

Six experiments, one file.  
Each section: **what it is**, **how it’s done**, **what counts as a result**, **why it matters**.

---

## 1. ED‑FRAP Mobility Collapse Test

### What this experiment is

You take a fluorescently labeled material (like a protein network or soft gel), bleach a small region with a laser, and watch how fast fluorescence comes back. That recovery reflects how mobile the molecules are.

ED predicts something sharp:  
when you condition on the **right geometric motif** (curvature/shape of the environment), the **apparent mobility should collapse** onto a single ED‑predicted curve—across different systems and conditions.

### How it’s done (plain language)

1. **Prepare a sample**  
   **Label** molecules with a fluorophore in a soft, structured environment (e.g., cytoskeleton, gel, condensate).

2. **Bleach a small region**  
   Use a focused laser to bleach a spot or line. This creates a dark region surrounded by bright, unbleached molecules.

3. **Record the recovery movie**  
   Take high‑framerate images as fluorescence returns. This gives you a recovery curve: intensity vs. time.

4. **Extract mobility curves**  
   Fit the recovery to get an effective mobility (like a diffusion coefficient or similar measure).

5. **Condition on motif / geometry**  
   Use the local structure (e.g., curvature, confinement, network geometry) to group data into “same motif” sets.

6. **Check for collapse**  
   Rescale according to the ED mobility law and see if curves from different conditions **collapse onto one master curve**.

### What counts as a result

- **Supports ED:**  
  After motif‑conditioning and ED rescaling, recovery curves from different conditions **collapse** onto a single curve.

- **Falsifies ED:**  
  Even after proper conditioning and rescaling, curves **refuse to collapse** and remain systematically different.

### Why this experiment matters

It turns FRAP from a vague “diffusion‑ish” measurement into a **sharp geometric test**.  
If ED is right, mobility is not arbitrary—it’s **locked to curvature and structure** in a very specific way.

---

## 2. ED‑FRAP Participation Test

### What this experiment is

Instead of just asking “how fast does fluorescence recover?”, this experiment asks:  
**“What fraction of molecules actually participate in the recovery?”**

ED predicts that the **participation fraction**—how many molecules are effectively mobile—follows a **curvature‑weighted law** tied to the ED geometry, not just random binding/unbinding.

### How it’s done (plain language)

1. **Same basic FRAP setup as mobility test**  
   Fluorescently labeled sample, bleach a region, record recovery.

2. **Measure total possible signal**  
   Before bleaching, measure the full fluorescence level—this is your “all molecules present” baseline.

3. **Measure the recovery plateau**  
   After recovery, see how high the fluorescence gets in the bleached region. It may not return to the original level.

4. **Compute participation fraction**  
   Participation ≈ (recovered signal) / (original signal).  
   This tells you what fraction of molecules actually took part in the exchange.

5. **Relate participation to geometry**  
   Use local structural features (curvature, confinement, network topology) to see how participation changes with geometry.

6. **Compare to ED participation law**  
   ED gives a specific way participation should scale with curvature/geometry. You test that scaling directly.

### What counts as a result

- **Supports ED:**  
  Participation fractions across different geometries follow the ED‑predicted scaling when plotted in the right variables.

- **Falsifies ED:**  
  Even with correct geometry measures, participation behaves in a way that **systematically disagrees** with ED’s law.

### Why this experiment matters

It turns a subtle, often ignored quantity—“how many molecules actually move?”—into a **precision probe of ED geometry**.  
It’s a second, independent FRAP‑based test, not just a repeat of mobility.

---

## 3. ED‑AFM Indentation Test

### What this experiment is

You use an Atomic Force Microscope (AFM) to poke a soft material (like a gel, cell, or membrane) and record how it pushes back. That gives you a force–distance curve.

ED predicts a specific **tension–curvature relation**: how the material’s effective tension responds to curvature and indentation in a way that differs from standard elasticity models.

### How it’s done (plain language)

1. **Prepare a soft sample**  
   Could be a gel, a thin film, a membrane, or a cell surface—something you can indent with an AFM tip.

2. **Indent with a known tip**  
   Use an AFM cantilever with a calibrated tip (sphere, cone, or pyramid) and press into the sample at controlled depth.

3. **Record force vs. indentation**  
   As you push in and pull out, you get a force–distance curve: how hard the sample pushes back at each depth.

4. **Extract effective tension and curvature**  
   From the shape of the curve and the tip geometry, you infer local curvature and an effective surface tension.

5. **Compare to ED tension–curvature law**  
   ED predicts a specific relationship between curvature and tension that differs from classical Hertz or thin‑shell models.

6. **Test across conditions**  
   Repeat for different loading rates, environments, or sample preparations to see if the ED relation holds robustly.

### What counts as a result

- **Supports ED:**  
  When you plot tension vs. curvature in the ED‑prescribed way, data from different conditions **fall on the ED curve**.

- **Falsifies ED:**  
  Even with careful analysis, the tension–curvature data **systematically follow a different law** than ED predicts.

### Why this experiment matters

It connects ED directly to **mechanical response**—how matter resists being deformed.  
If ED’s geometry is real, it should show up not just in transport (FRAP) but in **force–response** as well.

---

## 4. ED‑RLC Analogue (Benchtop)

### What this experiment is

You build a simple electrical circuit with a resistor (R), inductor (L), and capacitor (C). You excite it and watch how the voltage or current decays and oscillates.

ED predicts a specific **relaxation law**—how the amplitude and phase evolve over time—that differs in a controlled way from the standard textbook RLC solution when interpreted through ED’s geometry.

### How it’s done (plain language)

1. **Build an RLC circuit**  
   Connect R, L, and C in a known configuration (series or parallel), with well‑measured component values.

2. **Excite the circuit**  
   Apply a pulse or step input (e.g., charge the capacitor and let it discharge, or apply a voltage step).

3. **Measure voltage and/or current over time**  
   Use an oscilloscope or data‑acquisition system to record the time‑dependent signal.

4. **Extract amplitude, phase, and decay rate**  
   Fit the oscillations to get how fast they decay, how the phase shifts, and how the envelope behaves.

5. **Map to ED variables**  
   Interpret the circuit’s dynamics as a simple analogue of ED’s relaxation equation, with a specific mapping from circuit parameters to ED parameters.

6. **Compare to ED relaxation law**  
   Check whether the measured decay and phase evolution follow the ED‑predicted form, not just the standard RLC formula.

### What counts as a result

- **Supports ED:**  
  When analyzed in ED variables, the circuit’s relaxation matches the ED law across different R, L, C choices.

- **Falsifies ED:**  
  The data stubbornly follow only the standard RLC behavior and **cannot be reconciled** with ED’s predicted form.

### Why this experiment matters

It’s a **cheap, fast, tabletop** test of ED’s relaxation structure.  
If ED can’t even survive a simple RLC analogue, it doesn’t deserve to claim deeper physical relevance.

---

## 5. ED‑Optomechanical Extremal‑Horizon Test

### What this experiment is

You use an optical cavity (mirrors and light) where the effective refractive index or cavity length can be shaped so that light experiences something like a “horizon” inside the cavity.

ED predicts that when the profile has an **interior maximum** (a smooth peak inside), the corresponding horizon becomes **extremal**, and a certain “temperature‑like” signal should **vanish**—similar in spirit to the EIT differential test, but in a static optical setting.

### How it’s done (plain language)

1. **Set up an optical cavity**  
   Two or more mirrors forming a resonator, with a medium inside whose refractive index can be controlled (e.g., via intensity, temperature, or another field).

2. **Engineer two index profiles**  
   - **Case A (monotonic):** index changes steadily along the cavity.  
   - **Case B (interior max):** index rises to a peak in the middle, then falls.

3. **Inject light and measure mode structure**  
   Shine in a probe beam and measure how modes are distributed, how they mix, and how energy flows near the effective “horizon” region.

4. **Look for horizon‑like signatures**  
   Analyze mode mixing, spectral features, and any thermal‑like emission or noise associated with the horizon.

5. **Compare monotonic vs. interior‑max**  
   As in the EIT case, the key is the **difference** between the two profiles using the same apparatus.

6. **Check for extremal suppression**  
   ED predicts that the interior‑max case should show **suppressed or vanishing** horizon‑like signal compared to the monotonic case.

### What counts as a result

- **Supports ED:**  
  Horizon‑like signatures are present in the monotonic case but **collapse or vanish** in the interior‑max case.

- **Falsifies ED:**  
  The interior‑max case shows **no special suppression**; signals behave similarly in both profiles.

### Why this experiment matters

It tests ED’s **extremal‑horizon condition** in a clean, static optical system.  
It’s a bridge between abstract horizon geometry and **concrete optical cavities** that many labs already understand well.

---

## 6. ED‑Acoustic EIT Differential Experiment

### What this experiment is

You use a medium where light can be slowed dramatically using Electromagnetically Induced Transparency (EIT). By shaping the control laser, you sculpt how the **speed of a probe pulse** changes as it moves through the medium.

ED predicts that:

- A **monotonic** slow‑down profile gives a **normal horizon** with a nonzero “temperature‑like” signal.  
- A profile with an **interior maximum** (a smooth peak in the middle) gives an **extremal horizon**, where that signal should **vanish**.

The experiment is: **switch between these two profiles and see if the horizon signal disappears.**

### How it’s done (plain language)

1. **Set up a slow‑light EIT medium**  
   Typically a vapor cell (e.g., rubidium) with:
   - a **control** laser that prepares the atoms,  
   - a **probe** pulse whose speed you control and measure.

2. **Create two speed profiles for the probe**  
   By shaping the control beam intensity along the cell:
   - **Case A (monotonic):** probe slows more and more as it travels.  
   - **Case B (interior max):** probe slows, then speeds up, then slows again—creating an interior maximum.

3. **Launch probe pulses**  
   Send in probe pulses and record how they propagate, split, and distort near the effective “horizon” region.

4. **Measure horizon‑like signals**  
   Look at mode mixing, backward/forward components, and any thermal‑like emission associated with the horizon.

5. **Do the differential comparison**  
   Using the same apparatus, alternate between monotonic and interior‑max profiles and compare the measured signals.

6. **Check for extremal suppression**  
   ED says: the interior‑max (extremal) case should show **strongly suppressed or vanishing** horizon signal relative to the monotonic case.

### What counts as a result

- **Supports ED:**  
  Clear horizon‑like signal in the monotonic case, and **collapse/suppression** of that signal in the interior‑max case.

- **Falsifies ED:**  
  No special suppression in the interior‑max case; both profiles show similar horizon signals.

### Why this experiment matters

It’s the **first analogue‑gravity experiment with a full ED protocol in progress**, using **one apparatus, two profiles, one clean differential**.  
If ED’s extremal‑horizon prediction is right, this is where it can be seen decisively.

---

