# ED-Data-Galaxy-12: Activity-Dependence Test

**Allen Proxmire**
**March 2026**

---

## 0. Purpose

The BTFR ($V \propto M_b^{1/4}$) and the flat weak-lensing velocity are consistent with both ED (temporal tension) and MOND (modified gravity), and cannot distinguish between them. This note identifies the **one test that can**: the dependence of $V_{\text{temp}}$ on galactic activity at fixed baryonic mass.

- **ED predicts:** at fixed $M_b$, galaxies with higher star-formation rates have higher $V_{\text{temp}}$ (because activity sources the temporal-tension field).
- **MOND predicts:** no SFR dependence ($V$ depends only on $M_b$ and the acceleration scale $a_0$).
- **$\Lambda$CDM predicts:** no SFR dependence ($V$ depends on halo mass, which is set by formation history, not current SFR).

If activity-binned weak lensing reveals a systematic offset in $V_{\text{flat}}$ between star-forming and quiescent galaxies at the same $M_b$, **only ED can explain it**.

---

## 1. ED Prediction

### 1.1 The Activity Source

The temporal-tension field $T$ is sourced by galactic event density — the aggregate rate of dynamical interactions. In the ED interpretation (ED-I-002), the dominant sources are:

- **Gravitational encounters** — scale with total mass ($M_b$).
- **Star formation** — introduces turbulence, radiation pressure, supernova blast waves.
- **AGN feedback** — jets and winds in massive galaxies.
- **Magnetic reconnection** — in magnetised interstellar and circumgalactic media.

The total source strength is:

$$S_{\text{eff}} = S_{\text{mass}} + S_{\text{SF}} = \alpha M_b\left(1 + f\,\frac{\text{SFR}}{\text{SFR}_0}\right),$$

where $f$ is the fractional contribution of star-formation activity (relative to mass-driven activity) and $\text{SFR}_0$ is a reference SFR (e.g., the main-sequence value).

### 1.2 Velocity Scaling

From Galaxy-11, $V_{\text{temp}}^4 \propto S_{\text{eff}}$. Therefore:

$$V_{\text{temp}} \propto \left[M_b\left(1 + f\,\frac{\text{SFR}}{\text{SFR}_0}\right)\right]^{1/4}.$$

At fixed $M_b$, the fractional velocity difference between two SFR classes is:

$$\frac{\Delta V}{V_0} = \left(1 + f\,\frac{\text{SFR}}{\text{SFR}_0}\right)^{1/4} - 1 \approx \frac{f}{4}\,\frac{\Delta\text{SFR}}{\text{SFR}_0}.$$

### 1.3 The Parameter $f$

The parameter $f$ encodes how strongly star-formation activity contributes to temporal tension relative to mass-driven activity. Its value is not determined by the ED axioms — it is a constitutive parameter analogous to $\beta$ in the mobility law.

| $f$ | Physical meaning |
|:----|:-----------------|
| 0 | Mass only; no SFR dependence (standard BTFR) |
| 0.1 | 10% SFR contribution; subtle effect |
| 0.3 | 30% SFR contribution; moderate effect |
| 0.5 | 50% SFR contribution; strong effect |
| 1.0 | Equal mass and SFR contribution |

$f$ must be determined empirically. The test proposed here measures $f$ or places an upper bound on it.

---

## 2. Galaxy Classification

### 2.1 SFR Classes at Fixed Mass

For galaxies at $M_b \sim 3 \times 10^{10}\;M_\odot$ ($\log M_b \approx 10.5$), the main-sequence SFR is approximately $3.2\;M_\odot$/yr at $z \sim 0$. The five activity classes are:

| Class | SFR ($M_\odot$/yr) | SFR/SFR$_0$ | Typical population |
|:------|:-------------------|:-------------|:-------------------|
| Quiescent | $\sim 0.03$ | 0.01 | Red ellipticals, retired spirals |
| Low-SF | $\sim 0.3$ | 0.1 | Faded spirals, green valley |
| Main-sequence | $\sim 3.2$ | 1.0 | Normal spirals, Milky Way |
| Active | $\sim 9.5$ | 3.0 | Blue spirals, LIRG |
| Starburst | $\sim 32$ | 10 | ULIRG, merger remnants |

### 2.2 Expected $V_{\text{temp}}$ Offsets

Using $V_0 = 173$ km/s (mass-only baseline at $M_b = 3 \times 10^{10}\;M_\odot$):

**$f = 0.1$ (conservative):**

| Class | $V_{\text{temp}}$ (km/s) | $\Delta V$ (km/s) | $\Delta V/V_0$ |
|:------|:------------------------|:-------------------|:---------------|
| Quiescent | 173.0 | $-4.1$ | $-2.3\%$ |
| Main-sequence | 177.1 | reference | — |
| Starburst | 205.6 | $+28.5$ | $+16.1\%$ |

**$f = 0.3$ (moderate):**

| Class | $V_{\text{temp}}$ (km/s) | $\Delta V$ (km/s) | $\Delta V/V_0$ |
|:------|:------------------------|:-------------------|:---------------|
| Quiescent | 173.1 | $-11.6$ | $-6.3\%$ |
| Main-sequence | 184.6 | reference | — |
| Starburst | 244.5 | $+59.9$ | $+32.4\%$ |

**$f = 0.5$ (strong):**

| Class | $V_{\text{temp}}$ (km/s) | $\Delta V$ (km/s) | $\Delta V/V_0$ |
|:------|:------------------------|:-------------------|:---------------|
| Quiescent | 173.1 | $-18.2$ | $-9.5\%$ |
| Main-sequence | 191.4 | reference | — |
| Starburst | 270.6 | $+79.3$ | $+41.4\%$ |

Even at $f = 0.1$, the starburst-to-quiescent difference is **33 km/s** ($\sim 19\%$). At $f = 0.3$: **71 km/s** ($\sim 41\%$). These are large, measurable signals.

---

## 3. What MOND and $\Lambda$CDM Predict

### 3.1 MOND

In MOND, the asymptotic velocity is:

$$V_{\text{flat}} = (G\,a_0\,M_b)^{1/4}.$$

This depends **only** on $M_b$ and the fundamental constant $a_0$. Star-formation rate does not enter. At fixed $M_b$:

$$\Delta V_{\text{MOND}} = 0 \quad \text{(exact)}.$$

**MOND predicts zero activity dependence.**

### 3.2 $\Lambda$CDM

In $\Lambda$CDM, the circular velocity is set by the dark-matter halo mass $M_h$ through the stellar-to-halo-mass relation. At fixed $M_b$, galaxies with different SFR may have slightly different $M_h$ (due to different formation histories), but:

- The scatter in $M_h$ at fixed $M_b$ is $\sim 0.15$–$0.20$ dex (Behroozi et al. 2013).
- This gives $\Delta V/V \sim 0.15/3 = 5\%$ — scatter, not a systematic trend.
- There is no prediction that high-SFR galaxies have systematically higher $V$ at fixed $M_b$.

**$\Lambda$CDM predicts scatter but no systematic SFR trend.**

### 3.3 Summary

| Framework | $\Delta V$ (quiescent to starburst at fixed $M_b$) | Type of effect |
|:----------|:---------------------------------------------------|:---------------|
| **ED** ($f = 0.1$) | $+33$ km/s systematic | **Positive correlation** |
| **ED** ($f = 0.3$) | $+71$ km/s systematic | **Strong positive** |
| MOND | 0 | None |
| $\Lambda$CDM | $\sim \pm 10$ km/s scatter | Stochastic, not systematic |

---

## 4. Observational Strategy

### 4.1 Activity-Binned Weak-Lensing Stacks

**Step 1.** Select galaxies in a narrow mass bin: $10.3 < \log M_b/M_\odot < 10.7$.

**Step 2.** Split by specific star-formation rate (sSFR):
- **Low-activity bin:** sSFR $< 10^{-11}$ yr$^{-1}$ (quiescent + green valley).
- **High-activity bin:** sSFR $> 10^{-10}$ yr$^{-1}$ (main-sequence + active).

**Step 3.** Stack the weak-lensing shear signal $\gamma(R)$ for each bin at projected radii $R = 50$–$500$ kpc.

**Step 4.** Compute the inferred $V_{\text{circ}}(R)$ for each stack using the Mistele et al. deprojection formula.

**Step 5.** Compare the asymptotic $V_{\text{flat}}$ between the two bins.

### 4.2 Pseudocode

```python
import numpy as np

def activity_binned_lensing(catalog, mass_min=10.3, mass_max=10.7,
                            sSFR_split=3e-11):
    """Split galaxies by activity and stack lensing signals."""
    # Select mass bin
    mass_mask = (catalog['log_Mb'] > mass_min) & (catalog['log_Mb'] < mass_max)
    sample = catalog[mass_mask]

    # Split by sSFR
    low_act = sample[sample['sSFR'] < sSFR_split]
    high_act = sample[sample['sSFR'] >= sSFR_split]

    # Stack shear profiles
    gamma_low = stack_shear(low_act)   # averaged gamma(R)
    gamma_high = stack_shear(high_act)

    # Convert to V_circ
    V_low = deprojected_V(gamma_low)
    V_high = deprojected_V(gamma_high)

    # Measure asymptotic V_flat (average over 100-500 kpc)
    V_flat_low = np.mean(V_low[(R > 100) & (R < 500)])
    V_flat_high = np.mean(V_high[(R > 100) & (R < 500)])

    delta_V = V_flat_high - V_flat_low
    return delta_V, V_flat_low, V_flat_high
```

### 4.3 Required Sample Sizes

| Signal size ($\Delta V$) | Required $\sigma_V$ per bin | Required $N_{\text{lens}}$ per bin |
|:-------------------------|:---------------------------|:----------------------------------|
| 5 km/s | $< 1.7$ km/s | $\sim 8{,}000$ |
| 10 km/s | $< 3.3$ km/s | $\sim 2{,}000$ |
| 20 km/s | $< 6.7$ km/s | $\sim 500$ |

### 4.4 Available Surveys

| Survey | $N_{\text{galaxies}}$ (total) | $N$ at $\log M_b \sim 10.5$ | Feasible? |
|:-------|:------------------------------|:----------------------------|:----------|
| KiDS-1000 | $\sim 2 \times 10^7$ | $\sim 10^5$ | **Yes** (for $\Delta V > 10$ km/s) |
| HSC-SSP | $\sim 10^8$ | $\sim 10^6$ | **Yes** (for $\Delta V > 5$ km/s) |
| Euclid (future) | $\sim 10^9$ | $\sim 10^7$ | **Yes** (for any $\Delta V > 1$ km/s) |
| Rubin LSST (future) | $\sim 10^{10}$ | $\sim 10^8$ | **Yes** (trivially) |

**With current data (KiDS, HSC),** the test is feasible for $f \geq 0.1$ (signals $> 30$ km/s with $\sim 50{,}000$ galaxies per bin). **With Euclid,** even $f = 0.01$ would be detectable.

---

## 5. Interpretation

### 5.1 What a Detection Would Mean

If the activity-binned lensing test reveals $\Delta V > 0$ at $> 3\sigma$ (higher $V$ for higher SFR at fixed $M_b$):

1. **ED is confirmed.** The temporal-tension field is activity-sourced, not mass-sourced alone. This would be the first detection of a non-gravitational contribution to galaxy-scale dynamics.

2. **MOND is falsified** (as currently formulated). MOND predicts $V = (G a_0 M_b)^{1/4}$ with no activity dependence. A detection of SFR-correlated $V$ would require modifying MOND to include an activity term.

3. **$\Lambda$CDM requires fine-tuning.** A systematic SFR trend would require a physical mechanism linking current star-formation rate to dark-matter halo mass — plausible through baryonic feedback models but not a natural prediction.

### 5.2 What a Non-Detection Would Mean

If $\Delta V$ is consistent with zero at $< 5$ km/s:

1. **$f < 0.01$ (upper bound).** The SFR contribution to temporal tension is negligible. The field is sourced primarily by mass.

2. **ED is not falsified** but is less distinctive. If $f \approx 0$, ED reduces to a mass-only temporal-tension theory indistinguishable from MOND at the BTFR level.

3. **MOND and ED remain degenerate.** Further discriminators (merger lag, redshift evolution) would be needed.

### 5.3 The Decision Matrix

| Observation | ED interpretation | MOND interpretation | $\Lambda$CDM interpretation |
|:------------|:-----------------|:--------------------|:---------------------------|
| $\Delta V > 20$ km/s (strong) | $f \geq 0.1$; temporal tension confirmed | Falsified | Requires unknown SFR-halo mechanism |
| $\Delta V = 5$–$20$ km/s (weak) | $f \sim 0.01$–$0.1$ | Marginal tension | Compatible (scatter) |
| $\Delta V < 5$ km/s (null) | $f < 0.01$; mass-dominated | Consistent | Consistent |

---

## 6. Honest Assessment

| Question | Answer |
|:---------|:-------|
| Is the activity-dependence prediction unique to ED? | **Yes** — neither MOND nor $\Lambda$CDM predict it |
| Is the signal large enough to detect? | **Yes** — even $f = 0.1$ gives 33 km/s (19%) |
| Are current data sufficient? | **Possibly** (KiDS-1000, HSC-SSP) |
| Are future data sufficient? | **Definitely** (Euclid, Rubin LSST) |
| Is $f$ predicted by ED theory? | **No** — it is a free parameter |
| Would a detection prove ED? | **Not uniquely** — but it would disfavour MOND and motivate ED strongly |
| Would a non-detection falsify ED? | **No** — but it would constrain $f < 0.01$ |

---

## 7. Next Steps

### 7.1 Immediate

1. **KiDS/HSC analysis.** Apply the activity-binned stacking to existing weak-lensing data. This requires: (a) matching lens catalogs with SFR estimates (from UV/IR photometry), (b) stacking shear in mass-matched SFR bins, (c) computing $\Delta V$. The analysis pipeline is standard; only the SFR binning is new.

2. **SPARC activity test.** The SPARC database includes morphological types and gas fractions. Split SPARC galaxies by gas fraction (a proxy for activity) at fixed $V_{\text{flat}}$ and check whether the rotation-curve shape differs. This is a lower-fidelity version of the lensing test but can be done immediately with existing data.

### 7.2 Medium-Term

3. **Euclid proposal.** When Euclid early-release data become available, propose an activity-binned lensing analysis. The Euclid sample size ($> 10^7$ galaxies with lensing) makes $f > 0.01$ detectable.

4. **Merger-lag prediction.** In an ED galaxy merger, the temporal-tension fields of the two galaxies should lag behind the baryonic mass (because the field diffuses). This creates an offset between the mass centroid and the lensing centroid — testable with merging-cluster weak-lensing data.

### 7.3 Pipeline Status

| Note | Key Result |
|:-----|:-----------|
| Galaxy-10 | Mistele data: flat V confirmed; ED consistent |
| Galaxy-11 | BTFR = $V_T \propto M_b^{1/4}$; $a_{\text{ED}} \approx 2a_0$ |
| **Galaxy-12** | **Activity-dependence: ED predicts $\Delta V \sim 30$–$70$ km/s; MOND/ΛCDM predict 0; detectable with current surveys** |
| Galaxy-13 | Planned: merger-lag prediction |
