# ED-Data-Galaxy-09: Weak-Lensing Prediction for ED Halos

**Allen Proxmire**
**March 2026**

---

## 0. Purpose

Galaxy-08 showed that the combined ED halo (gravity + temporal tension) reproduces NGC 3198's rotation curve ($R < 30$ kpc) as well as Burkert. But the two models are degenerate at rotation-curve radii — the same $V(r)$ can be produced by a large Burkert halo or a smaller ED core plus temporal tension.

This note breaks the degeneracy by computing predictions at **weak-lensing radii** (50–1000 kpc), where the models diverge dramatically. Weak-lensing data from Mistele et al. (2024) show circular velocities remaining flat to $\sim 1$ Mpc. Which model — Burkert, NFW, or ED — is consistent with this observation?

---

## 1. The Three Models at Large Radii

### 1.1 Burkert (Cored DM Halo)

The Burkert profile has $\rho \propto r^{-3}$ at large $r$. This means the enclosed mass grows slowly ($M \propto \ln r$ at large $r$), and the circular velocity declines:

$$V_{\text{Burkert}}(r) \to 0 \quad \text{as } r \to \infty.$$

Burkert halos have **finite total mass**. Beyond the virial radius, the velocity drops toward Keplerian ($V \propto r^{-1/2}$).

### 1.2 NFW (Cuspy DM Halo)

The NFW profile has $\rho \propto r^{-3}$ at $r \gg r_s$, but the scale radius $r_s$ is typically 10–30 kpc. The enclosed mass grows as $M \propto \ln(1 + r/r_s)$, so:

$$V_{\text{NFW}}(r) \propto \sqrt{\frac{\ln(1 + r/r_s)}{r/r_s}} \to 0 \quad \text{slowly.}$$

NFW halos also have infinite total mass (requiring truncation), but their velocity declines more slowly than Burkert because the $r^{-1}$ inner cusp concentrates more mass at intermediate radii.

### 1.3 ED (Gravity + Temporal Tension)

The ED halo has two components:

$$V_{\text{ED}}^2(r) = V_{\text{grav}}^2(r) + V_{\text{temp}}^2.$$

The gravitational component declines (like Burkert), but the temporal-tension floor $V_{\text{temp}}$ is approximately constant to very large radii (ED-I-027 predicts it extends to $\sim 1$ Mpc). As $r \to \infty$:

$$V_{\text{ED}}(r) \to V_{\text{temp}} > 0 \quad \text{(finite asymptote).}$$

This is the key distinction: **ED predicts a finite asymptotic velocity; Burkert predicts zero.**

---

## 2. Numerical Predictions

Using the NGC 3198 parameters from Galaxy-08:

- **Burkert:** $\rho_s = 4.20 \times 10^7\;M_\odot$/kpc$^3$, $r_c = 4.69$ kpc.
- **NFW:** $\rho_s = 5.21 \times 10^6\;M_\odot$/kpc$^3$, $r_s = 23.9$ kpc.
- **ED Model A:** Burkert core + $V_{\text{temp}} = 12.5$ km/s.
- **ED Model B:** ED core ($r_c = 1.88$ kpc) + $V_{\text{temp}} = 86.5$ km/s.

### 2.1 Circular Velocity at Large Radii

| $R$ (kpc) | Burkert (km/s) | NFW (km/s) | ED Model A (km/s) | ED Model B (km/s) |
|:----------|:---------------|:-----------|:-------------------|:-------------------|
| 10 | 102 | 147 | 103 | 134 |
| 30 | 97 | 183 | 98 | 130 |
| 50 | 88 | 187 | 89 | 124 |
| 100 | 73 | 179 | 74 | 113 |
| 200 | 59 | 160 | 60 | 104 |
| 300 | 51 | 145 | 52 | 100 |
| 500 | 42 | 127 | 44 | **96** |
| 700 | 37 | 114 | 39 | **94** |
| 1000 | 32 | 102 | 35 | **92** |

### 2.2 Observed Values (Mistele et al. 2024)

Mistele et al. measured stacked weak-lensing signals for galaxies with $V_{\text{flat}} \sim 130$–$160$ km/s. The inferred circular velocity is approximately **constant at $V \sim 130$–$150$ km/s from 100 kpc to 1 Mpc**, with no Keplerian decline.

---

## 3. The Discriminator

### 3.1 Qualitative Comparison

| Model | $V(500$ kpc$)$ | $V(1$ Mpc$)$ | Matches Mistele? |
|:------|:---------------|:-------------|:-----------------|
| Burkert | 42 km/s | 32 km/s | **No** (too low by 3–4$\times$) |
| NFW | 127 km/s | 102 km/s | **Marginal** (declining slowly) |
| ED Model A ($V_T = 12.5$) | 44 km/s | 35 km/s | **No** (temporal tension too small) |
| ED Model B ($V_T = 86.5$) | **96** km/s | **92** km/s | **Partial** (lower than observed but flat) |
| Observed | $\sim 140$ km/s | $\sim 140$ km/s | — |

### 3.2 What the Data Require

The Mistele et al. observation of flat $V \sim 140$ km/s to 1 Mpc requires one of:

1. **A very extended massive halo** (NFW with $r_s \sim 20$–$30$ kpc reaches $\sim 100$ km/s at 1 Mpc — close but declining).
2. **A non-gravitational velocity contribution** that remains constant to very large radii (ED temporal tension).
3. **Modified gravity** (MOND deep-MOND regime).

### 3.3 Where the Models Diverge

| Radius range | Distinguishable? | What to measure |
|:-------------|:-----------------|:----------------|
| $< 30$ kpc (rotation curve) | **No** — all models fit | $V(r)$ from HI |
| 30–100 kpc | Marginal | Satellite kinematics |
| **100–500 kpc** | **Yes** — models diverge by $2$–$3\times$ | **Weak lensing** |
| $> 500$ kpc | **Strongly** — Burkert $\to 0$, NFW declining, ED flat | Stacked lensing |

The 100–500 kpc range is the **decisive discriminator**. At 500 kpc:

- Burkert predicts $V = 42$ km/s (declining toward zero).
- NFW predicts $V = 127$ km/s (declining slowly).
- ED Model B predicts $V = 96$ km/s (nearly flat).
- Observed: $\sim 140$ km/s (flat).

### 3.4 What ED Needs

ED Model B gives $V \sim 92$–$96$ km/s at 500–1000 kpc. The observed value is $\sim 140$ km/s. To match, ED would need $V_{\text{temp}} \approx 120$–$130$ km/s (rather than 86.5 km/s). This would mean temporal tension provides $\sim 80\%$ of the centripetal acceleration at 500 kpc — a dramatically different interpretation from Burkert or NFW.

---

## 4. Application to NGC 3198

### 4.1 Predicted Lensing-Inferred $V(R)$ Profile

For NGC 3198 ($V_{\text{flat}} = 142$ km/s at 10–30 kpc), the models predict:

| $R$ (kpc) | Burkert | NFW | ED ($V_T = 120$) |
|:----------|:--------|:----|:-----------------|
| 30 | 97 | 183 | 155 |
| 100 | 73 | 179 | 140 |
| 300 | 51 | 145 | 131 |
| 500 | 42 | 127 | 127 |
| 1000 | 32 | 102 | 124 |

With $V_{\text{temp}} = 120$ km/s, the ED model produces a lensing-inferred velocity of $\sim 124$–$140$ km/s at 100–1000 kpc — consistent with the observed $\sim 130$–$150$ km/s.

### 4.2 The Trade-Off

| $V_{\text{temp}}$ (km/s) | Fraction of $V_{\text{flat}}$ | Rotation curve fit | Weak-lensing match |
|:--------------------------|:------------------------------|:-------------------|:-------------------|
| 12.5 (Model A) | 9% | Excellent (1.9 km/s) | No ($V$ too low at 500 kpc) |
| 86.5 (Model B) | 61% | Good (2.4 km/s) | Partial ($V \sim 96$ km/s) |
| 120 (hypothetical) | 85% | To be tested | Good ($V \sim 124$–$140$ km/s) |
| 140 (maximal) | 99% | Requires very small grav. halo | Yes ($V \sim 140$ km/s) |

If temporal tension is responsible for the weak-lensing flatness observed by Mistele et al., it must contribute $\sim 80$–$90\%$ of the centripetal acceleration at $> 100$ kpc. The gravitational halo would be much smaller than standard models assume.

---

## 5. Testable Predictions

### 5.1 ED vs. Burkert at 100–500 kpc

| Prediction | Burkert | ED ($V_T \sim 120$) | How to test |
|:-----------|:--------|:--------------------|:-----------|
| $V(500$ kpc$)$ | $\sim 40$ km/s | $\sim 127$ km/s | Stacked weak lensing (HSC, Euclid) |
| Slope at 200–500 kpc | Steep decline ($d\ln V/d\ln R \approx -0.5$) | Nearly flat ($\sim -0.02$) | Shear profile shape |
| Galaxy-type dependence | Same for ETGs and LTGs at fixed mass | Scales with activity (SFR, gas content) | Activity-binned stacking |
| Post-merger lag | No lag (halo tracks mass) | Lag (temporal field responds slowly) | Merging-cluster offsets |

### 5.2 The BTFR Discriminator

The baryonic Tully-Fisher relation (BTFR) states $V_{\text{flat}}^4 \propto M_{\text{bar}}$. In the ED interpretation:

$$V_{\text{flat}}^4 = V_{\text{grav}}^4 + (\text{cross terms}) + V_{\text{temp}}^4.$$

If $V_{\text{temp}}$ dominates, the BTFR becomes $V_{\text{temp}}^4 \propto M_{\text{bar}}$, which means the temporal-tension amplitude is set by the baryonic mass — a prediction consistent with ED-I-027's interpretation of the BTFR as a temporal-amplitude scaling law.

### 5.3 Observational Strategy

The cleanest test is **galaxy-galaxy weak lensing** stacked by baryonic mass:

1. Select galaxies with $V_{\text{flat}} = 120$–$160$ km/s from SPARC or similar.
2. Stack their weak-lensing shear signals from HSC/Euclid data at $R = 50$–$1000$ kpc.
3. Measure the inferred $V_{\text{circ}}(R)$ profile.
4. Compare to Burkert (declining), NFW (slowly declining), and ED (flat at $V_{\text{temp}}$).

If the stacked $V_{\text{circ}}$ is flat to 1 Mpc, **only ED (or MOND) can explain it without modifying gravity.** Burkert and NFW require halos extending far beyond the virial radius.

---

## 6. Honest Assessment

| Question | Answer |
|:---------|:-------|
| Does ED predict flat $V$ to 1 Mpc? | **Yes** (temporal tension provides a floor) |
| Is the predicted $V$ large enough? | **Partially** (Model B: 92 km/s at 1 Mpc; needs $V_T \sim 120$ for full match) |
| Does Burkert predict flat $V$ to 1 Mpc? | **No** ($V \to 32$ km/s at 1 Mpc) |
| Does NFW? | **Partially** ($V \sim 102$ km/s at 1 Mpc, declining) |
| Can current data distinguish the models? | **Yes, at 200–500 kpc** (models differ by $2$–$3\times$) |
| Is the ED prediction falsifiable? | **Yes** — if $V$ declines below $V_{\text{temp}}$ at large $R$, temporal tension is refuted |

---

## 7. Next Steps

### 7.1 Immediate

1. **Compare to Mistele et al. data directly.** Digitise their stacked $V_{\text{circ}}(R)$ profile and overlay the ED, NFW, and Burkert predictions. Compute $\chi^2$ for each model.

2. **Fit $V_{\text{temp}}$ from lensing.** Using the Mistele et al. data at $R > 100$ kpc, fit $V_{\text{temp}}$ as the asymptotic floor. Determine whether $V_{\text{temp}} \approx 120$ km/s is consistent with the data.

### 7.2 Medium-Term

3. **Activity-binned lensing.** Split galaxies by star-formation rate (at fixed mass) and compare the stacked lensing signals. ED predicts: higher SFR $\to$ higher $V_{\text{temp}}$ (temporal tension sourced by activity). Burkert/NFW predict: no SFR dependence.

4. **DESI/Euclid forecasts.** Compute the precision needed to distinguish ED from NFW at 500 kpc. If Euclid can measure $V_{\text{circ}}$ to $\pm 10$ km/s at 500 kpc, the ED vs. NFW difference ($96$ vs. $127$ km/s) is detectable at $3\sigma$.

### 7.3 Pipeline Status

| Note | Status | Key Result |
|:-----|:-------|:-----------|
| Galaxy-01 | Complete | Pipeline defined |
| Galaxy-02 | Complete | Pure-PME rejected |
| Galaxy-03 | Complete | Dwarfs: core correct, edge wrong |
| Galaxy-04 | Complete | No steady state without gravity |
| Galaxy-05 | Complete | ED–Poisson: core correct, slope shallow |
| Galaxy-06 | Complete | Generalised: 99.6% Burkert (dwarfs) |
| Galaxy-07 | Complete | NGC 3198: core correct, V overshoots |
| Galaxy-08 | Complete | ED + temporal tension: ties Burkert at 30 kpc |
| **Galaxy-09** | **Complete** | **Weak-lensing predictions: ED flat at $V_T$; Burkert drops to 32 km/s at 1 Mpc; discriminator at 100–500 kpc** |
| Galaxy-10 | Planned | Direct comparison to Mistele et al. data |
