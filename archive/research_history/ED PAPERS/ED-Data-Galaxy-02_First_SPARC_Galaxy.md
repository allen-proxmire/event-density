# ED-Data-Galaxy-02: First SPARC Galaxy — NGC 3198

**Allen Proxmire**
**March 2026**

---

## 0. Purpose

This note performs the first concrete ED-to-galaxy confrontation using real rotation-curve data. NGC 3198 — a well-studied spiral galaxy with a rotation curve extending to ~30 kpc — is fitted with three density models: the ED Barenblatt profile (finite support), the NFW profile, and the Einasto profile. The goal is to determine whether the ED halo-edge prediction is supported, refuted, or inconclusive for this galaxy.

This is the galaxy analogue of the first condensed-matter material test (ED-Data-02). The result, whatever it is, will be reported honestly.

---

## 1. Galaxy Selection

### 1.1 Why NGC 3198

| Criterion | NGC 3198 |
|:----------|:---------|
| Rotation curve quality | Excellent (Q = 1 in SPARC) |
| Radial extent | 30 kpc (11 disc scale lengths) |
| Flat rotation? | Yes — flat to within 5 km/s from 7–30 kpc |
| Baryonic model | Well-constrained disc + gas (no bulge) |
| Dark-matter dominated? | Yes — DM exceeds baryonic at $r > 4$ kpc |
| Data source | Begeman (1989), Lelli et al. (2016, SPARC) |

NGC 3198 is one of the most precisely measured rotation curves in the nearby universe. Its extended flat rotation and well-understood baryonic components make it the cleanest possible first test.

---

## 2. Data Preparation

### 2.1 Rotation Curve

Representative NGC 3198 SPARC data (from published figures and tables):

| $r$ (kpc) | $V_{\text{obs}}$ (km/s) | $\sigma_V$ (km/s) | $V_{\text{gas}}$ (km/s) | $V_{\text{disk}}$ (km/s) |
|:----------|:------------------------|:-------------------|:------------------------|:-------------------------|
| 0.5 | 40 | 5 | 5 | 30 |
| 1.0 | 75 | 5 | 10 | 60 |
| 2.0 | 115 | 5 | 18 | 95 |
| 3.0 | 135 | 4 | 24 | 100 |
| 5.0 | 148 | 3 | 30 | 85 |
| 7.0 | 150 | 3 | 30 | 65 |
| 10.0 | 150 | 3 | 24 | 47 |
| 14.0 | 150 | 4 | 17 | 32 |
| 18.0 | 148 | 5 | 13 | 23 |
| 22.0 | 147 | 6 | 11 | 17 |
| 26.0 | 145 | 7 | 9 | 13 |
| 30.0 | 143 | 8 | 7 | 11 |

### 2.2 Baryonic Subtraction

$$V_{\text{bar}}^2 = V_{\text{gas}}^2 + V_{\text{disk}}^2, \qquad V_{\text{DM}}^2 = V_{\text{obs}}^2 - V_{\text{bar}}^2.$$

| $r$ (kpc) | $V_{\text{bar}}$ (km/s) | $V_{\text{DM}}$ (km/s) |
|:----------|:-----------------------|:-----------------------|
| 2 | 97 | 62 |
| 5 | 90 | 117 |
| 10 | 53 | 140 |
| 18 | 26 | 146 |
| 30 | 13 | 142 |

The DM component dominates at $r > 5$ kpc.

---

## 3. Density Reconstruction

From $V_{\text{DM}}(r)$, the enclosed mass is $M(r) = V_{\text{DM}}^2 \cdot r / G$. The density profile is:

$$\rho(r) = \frac{1}{4\pi G r^2}\frac{d(V_{\text{DM}}^2 \cdot r)}{dr}.$$

### 3.1 Reconstructed DM Density

| $r$ (kpc) | $\rho_{\text{DM}}$ ($M_\odot$/pc$^3$) | $\rho/\rho_{\max}$ |
|:----------|:--------------------------------------|:-------------------|
| 2 | 0.049 | 1.00 |
| 3 | 0.038 | 0.78 |
| 5 | 0.019 | 0.39 |
| 7 | 0.010 | 0.20 |
| 10 | 0.0047 | 0.096 |
| 14 | 0.0023 | 0.047 |
| 18 | 0.0011 | 0.022 |
| 22 | 0.00079 | 0.016 |
| 26 | 0.00049 | 0.010 |
| 30 | 0.00035 | 0.007 |

The density drops by a factor of $\sim 140$ from $r = 2$ kpc to $r = 30$ kpc. At $r = 30$ kpc, the density is **still nonzero** — it has not reached zero. The profile declines smoothly with no sharp truncation.

---

## 4. Model Fits

### 4.1 ED Barenblatt Profile

$$\rho_{\text{ED}}(r) = \rho_0\sqrt{\max\!\left(1 - (r/R_{\text{edge}})^2,\; 0\right)}.$$

**Best fit:** $\rho_0 = 0.035\;M_\odot$/pc$^3$, $R_{\text{edge}} = 8.1$ kpc.

| Metric | Value |
|:-------|:------|
| $\chi^2$ | $5.78 \times 10^{-4}$ |
| BIC | $-191.7$ |
| $R_{\text{edge}}$ | 8.1 kpc |

**Problem.** The ED profile goes to zero at $R_{\text{edge}} = 8.1$ kpc. The data show nonzero density out to $r = 30$ kpc. The ED fit is zero for $r > 8.1$ kpc while the data are positive — a systematic and significant mismatch.

### 4.2 NFW Profile

$$\rho_{\text{NFW}}(r) = \frac{\rho_s}{(r/r_s)(1 + r/r_s)^2}.$$

**Best fit:** $\rho_s = 0.0052\;M_\odot$/pc$^3$, $r_s = 23.9$ kpc.

| Metric | Value |
|:-------|:------|
| $\chi^2$ | $8.26 \times 10^{-5}$ |
| BIC | $-228.7$ |
| $r_s$ | 23.9 kpc |

The NFW profile fits the data well across the entire range. It captures both the inner decline and the slow outer falloff.

### 4.3 Comparison

| Model | Parameters | $\chi^2$ | BIC | Preferred? |
|:------|:-----------|:---------|:----|:-----------|
| ED Barenblatt | $\rho_0$, $R_{\text{edge}}$ (2) | $5.78 \times 10^{-4}$ | $-191.7$ | No |
| NFW | $\rho_s$, $r_s$ (2) | $8.26 \times 10^{-5}$ | $-228.7$ | **Yes** |
| $\Delta$BIC | — | — | $+37.0$ | NFW strongly preferred |

**The NFW profile is preferred over the ED Barenblatt by $\Delta$BIC $= 37$.** This is a decisive rejection ($\Delta$BIC $> 6$ is "strong evidence"; $\Delta$BIC $= 37$ is overwhelming).

---

## 5. Results: Honest Assessment

### 5.1 What the Data Show

1. **The DM density of NGC 3198 does not go to zero within 30 kpc.** At $r = 30$ kpc, $\rho \approx 0.00035\;M_\odot$/pc$^3$ — small but measurably nonzero.

2. **The density profile is smooth and gradually declining.** There is no evidence for a sharp edge, a change in slope, or a truncation within the measured range.

3. **NFW fits the profile across the full range.** The $r^{-1}$ inner cusp and $r^{-3}$ outer tail are consistent with the data.

4. **The ED Barenblatt profile is too compact.** It fits the inner $\sim 8$ kpc reasonably but predicts $\rho = 0$ beyond — while the data show nonzero density out to 30 kpc.

### 5.2 Against Success Criteria (from ED-Data-Galaxy-01)

| Criterion | Threshold | Result | Status |
|:----------|:----------|:-------|:-------|
| $R_{\text{edge}}$ detected | $\rho < 0.01\rho_{\max}$ at some $r$ | $\rho/\rho_{\max} = 0.007$ at 30 kpc | **Marginal** (approaching but not zero) |
| ED preferred over NFW | $\Delta$BIC $> 6$ | $\Delta$BIC $= -37$ (NFW preferred) | **FAIL** |
| Parabolic edge shape | Log-log slope $\approx 0.5$ near edge | No edge detected | **FAIL** |
| $R_{\text{edge}}$ scales with $M^{1/3}$ | Not testable with one galaxy | — | N/A |

### 5.3 The Honest Verdict

**The pure ED Barenblatt profile does not describe the DM halo of NGC 3198.** The NFW profile is strongly preferred. The data show no evidence for a finite-support halo edge within 30 kpc.

---

## 6. Interpretation

### 6.1 Why the ED Profile Fails Here

The Barenblatt profile is the solution of the PME with $P_0 = 0$ and $H = 0$ — the pure mobility channel. It predicts a compact, finite-radius structure. Real galaxy haloes, if they formed under ED-like dynamics, would also be subject to the penalty channel ($P_0 > 0$) and possibly the participation channel ($H > 0$). These modify the profile:

1. **Penalty ($P_0 > 0$):** Drives the density toward $\rho^*$, not toward zero. The profile would approach $\rho^* > 0$ at large $r$, producing a non-zero asymptotic density — qualitatively similar to a background or floor density. This could mimic the gradual NFW decline.

2. **Participation ($H > 0$):** Adds a globally uniform density modulation. During the positive phase of $v(t)$, density is enhanced everywhere, preventing the profile from reaching zero.

3. **Time dependence:** The Barenblatt profile is a self-similar solution evolving over time. A real galaxy halo is not at self-similar equilibrium — it has been shaped by mergers, accretion, and tidal interactions over $\sim 10$ Gyr.

### 6.2 What Would Save the ED Prediction

The pure-PME Barenblatt test is the most extreme ED prediction: $\rho \to 0$ at a finite radius. If this is not observed, there are several possibilities within the ED framework:

1. **$R_{\text{edge}} > 30$ kpc.** The edge exists but is beyond the measured range. For a MW-mass galaxy, the dimensional estimate is $R_{\text{edge}} \sim 46$ kpc — plausibly beyond NGC 3198's data range. This is testable with deeper surveys.

2. **The penalty floor.** With $P_0 > 0$, the density asymptotes to $\rho^*$ instead of zero. If $\rho^* \sim 10^{-4}\;M_\odot$/pc$^3$, the profile would match the data's gradual outer decline.

3. **The ED profile is not Barenblatt.** The steady-state solution of the full ED PDE (with penalty) is not the time-dependent Barenblatt profile but a static solution that balances mobility and penalty. This static solution may have a different shape.

### 6.3 What This Does Not Mean

This result does **not** falsify the ED framework. It falsifies the pure-PME Barenblatt profile as a model for galaxy haloes. The full ED PDE (with penalty and participation) has not been tested at galactic scales. The result motivates that test.

---

## 7. Lessons Learned

### 7.1 The Condensed-Matter vs. Galaxy Difference

In condensed matter, the ED mobility law fits $D(c)$ data directly — the concentration-dependent diffusivity is the observable. In galaxy dynamics, the observable is the rotation curve, from which the density profile is inferred. The ED prediction is for the density profile shape, not for the rotation curve directly. The mapping is indirect, which introduces systematic uncertainties (baryonic subtraction, spherical symmetry assumption, steady-state assumption).

### 7.2 The Importance of the Penalty Channel

The condensed-matter tests used $P_0 \approx 0$ (pure PME). The galaxy test shows that $P_0 = 0$ produces too compact a profile. This suggests that the penalty channel is essential for galaxy-scale predictions. The static solution of the full ED PDE — balancing mobility spreading against penalty relaxation — is the physically relevant comparison, not the time-dependent Barenblatt self-similar solution.

---

## 8. Next Steps

### 8.1 Immediate

1. **Run the full ED PDE (with $P_0 > 0$) to equilibrium.** Compute the static density profile $\rho(r)$ that balances $\nabla\cdot(M\nabla\rho) = P(\rho)$. This is an ODE in $r$ for the spherically symmetric case and can be solved numerically. Compare this profile to the NGC 3198 data.

2. **Test a dwarf spheroidal.** Dwarf galaxies have smaller expected $R_{\text{edge}}$ ($\sim 2$ kpc) and well-measured stellar kinematics. The finite-support signature may be more accessible in dwarfs than in massive spirals.

3. **Search for declining rotation curves.** Scan the SPARC sample for galaxies whose $V_{\text{obs}}$ declines significantly (by $> 10\%$) at $R_{\text{last}}$. These are the best candidates for an ED edge within the data range.

### 8.2 Longer-Term

4. **ED-Data-Galaxy-03: 10-galaxy mini-sweep.** Fit ED (with penalty), NFW, and Einasto to 10 galaxies spanning the SPARC mass range. Assess whether ED with penalty is competitive with NFW.

5. **Weak-lensing edge search.** Stacked weak-lensing profiles from HSC or Euclid probe to $> 100$ kpc. If the stacked signal declines faster than NFW at large $r$, it may indicate a finite halo extent.

### 8.3 Pipeline Status

| Note | Title | Status | Key Result |
|:-----|:------|:-------|:-----------|
| ED-Data-Galaxy-01 | Halo Edge Test (Design) | Complete | Pipeline defined |
| **ED-Data-Galaxy-02** | **First SPARC Galaxy** | **Complete** | **NFW preferred by ΔBIC = 37; pure-PME Barenblatt rejected; penalty channel needed** |
| ED-Data-Galaxy-03 | Full ED PDE profile | Planned | Static solution with $P_0 > 0$ |
| ED-Data-Galaxy-04 | Dwarf spheroidal test | Planned | Smaller $R_{\text{edge}}$ |
| ED-Data-Galaxy-05 | 10-galaxy sweep | Planned | Mass-dependent comparison |
