# ED-Data-Galaxy-01: First Halo Edge Test

**Allen Proxmire**
**March 2026**

---

## 0. Purpose

The ED-Data pipeline has established that the ED mobility law fits three condensed-matter systems with $R^2 > 0.98$, produces sub-Fickian front dynamics, and exhibits compact support. This note takes the next step: applying the same structural predictions to galaxy-scale observations.

The central prediction: **ED halos have a finite edge radius $R_{\text{edge}}$ where the density goes to zero.** This is the galactic analogue of compact-support fronts in condensed matter. Standard halo models (NFW, Einasto) have power-law or exponential tails extending to infinity. If real halos have finite edges, it is direct evidence for PME-like dynamics — and against infinite-tail models.

This is not a claim that ED replaces dark matter. It is a test of a specific structural prediction: does the density profile of a galactic halo end at a finite radius, or does it extend indefinitely?

---

## 1. ED Predictions for Halos

### 1.1 The Barenblatt Profile in $d = 3$

The ED PDE in the mobility-only limit ($P_0 = 0$, $H = 0$) reduces to the PME with $m = \beta + 1$. For canonical $\beta = 2$ ($m = 3$), the self-similar radial profile in $d = 3$ is:

$$\rho_{\text{ED}}(r) = \rho_0 \left[1 - \left(\frac{r}{R_{\text{edge}}}\right)^2\right]_+^{1/(m-1)} = \rho_0 \sqrt{1 - \left(\frac{r}{R_{\text{edge}}}\right)^2},$$

where $[x]_+ = \max(x, 0)$ and $R_{\text{edge}}$ is the finite edge radius beyond which $\rho = 0$ exactly.

This is a **parabolic cap** (for $m = 3$: a square-root profile). It has three defining features:

1. **Finite radius.** $\rho(R_{\text{edge}}) = 0$. No material beyond $R_{\text{edge}}$.
2. **Smooth approach to zero.** $\rho \propto (R_{\text{edge}} - r)^{1/2}$ near the edge — a square-root vanishing, not a step function.
3. **Flat core.** $\rho(0) = \rho_0$ with $d\rho/dr|_{r=0} = 0$. The central density is a maximum with zero gradient.

### 1.2 Comparison to Standard Profiles

| Feature | ED (Barenblatt) | NFW | Einasto |
|:--------|:----------------|:----|:--------|
| Central behaviour | Flat core ($\rho = \rho_0$) | Cusp ($\rho \propto r^{-1}$) | Flat or shallow cusp |
| Edge behaviour | Zero at $R_{\text{edge}}$ | Power-law tail ($\rho \propto r^{-3}$) | Exponential tail |
| $\rho(R_{\text{edge}})$ | **0** (exact) | $> 0$ (always) | $> 0$ (always) |
| Shape near edge | $\sqrt{R_{\text{edge}} - r}$ | $r^{-3}$ | $\exp(-r^{1/n})$ |
| Total mass | Finite (convergent) | Divergent (must be truncated) | Finite for $n < 3$ |

The NFW profile has $\rho \propto r^{-3}$ at large $r$, so its total mass diverges. In practice, it is truncated at the virial radius $R_{\text{vir}}$, but this truncation is imposed, not derived. The ED profile needs no truncation — the mass is automatically finite.

### 1.3 Scaling of $R_{\text{edge}}$

From the Barenblatt solution with total mass $M$ and central density $\rho_0$:

$$R_{\text{edge}} \sim \left(\frac{M}{\rho_0}\right)^{1/3}.$$

| Galaxy type | $M_{\text{halo}}$ ($M_\odot$) | $\rho_0$ (kg m$^{-3}$) | $R_{\text{edge}}$ (kpc) |
|:------------|:------------------------------|:------------------------|:-----------------------|
| Milky Way | $10^{12}$ | $\sim 7 \times 10^{-22}$ | $\sim 46$ |
| Dwarf spheroidal | $10^{9}$ | $\sim 7 \times 10^{-21}$ | $\sim 2$ |
| Galaxy cluster | $10^{15}$ | $\sim 7 \times 10^{-23}$ | $\sim 1000$ |

These are order-of-magnitude estimates. The precise $R_{\text{edge}}$ depends on the full Barenblatt normalisation, which requires the diffusion coefficient and the age of the system. But the scaling $R_{\text{edge}} \propto M^{1/3}$ is a structural prediction.

---

## 2. Observables

### 2.1 Rotation Curves (SPARC)

Rotation curves measure $v_{\text{circ}}(r)$. The enclosed mass is $M(r) = v_{\text{circ}}^2 r / G$. The density profile is:

$$\rho(r) = \frac{1}{4\pi G r^2}\frac{d}{dr}\left[v_{\text{circ}}^2(r) \cdot r\right].$$

If the halo has a finite edge at $R_{\text{edge}}$, then $v_{\text{circ}}(r) \propto r^{-1/2}$ (Keplerian decline) for $r > R_{\text{edge}}$. The transition from flat rotation to Keplerian decline is the observable signature of a halo edge.

**Challenge.** Most SPARC rotation curves extend to $R_{\text{last}} \sim 10$–$30$ kpc — possibly inside $R_{\text{edge}}$. The edge is only detectable if $R_{\text{last}} > R_{\text{edge}}$ or if the onset of Keplerian decline is visible within the data range.

### 2.2 Stellar Halo Density (Gaia)

Gaia DR3 provides star counts as a function of galactocentric radius for the Milky Way stellar halo. The stellar density $\nu_*(r)$ traces the total mass density if the stellar-to-total-mass ratio is approximately constant. A sharp drop in $\nu_*(r)$ at some radius would indicate a halo edge.

**Challenge.** The stellar halo is contaminated by disc stars, satellite streams, and foreground/background confusion. Extracting a clean $\nu_*(r)$ requires careful selection cuts and modelling.

### 2.3 Ultra-Diffuse Galaxy Edges (Dragonfly)

The Dragonfly Telephoto Array provides deep surface-brightness imaging of ultra-diffuse galaxies (UDGs). These galaxies have very low surface brightness and extended morphologies. If their haloes have finite edges, the surface brightness should drop to zero at a definite radius — not fade exponentially.

**Challenge.** Surface brightness is a 2D projection of a 3D density profile. Extracting a 3D edge from a 2D image requires deprojection, which introduces model dependence.

### 2.4 Weak Lensing (Subaru/HSC, Euclid)

Weak gravitational lensing measures the projected mass distribution around galaxies. A stacked weak-lensing signal $\Delta\Sigma(R)$ declining to zero at a finite radius would indicate a finite halo extent.

**Challenge.** Stacking averages over many galaxies with different masses and concentrations. The edge signal, if present, may be smeared.

---

## 3. Candidate Datasets

### 3.1 SPARC (Spitzer Photometry and Accurate Rotation Curves)

| Property | Assessment |
|:---------|:----------|
| Galaxies | 175 disc galaxies with high-quality HI/H$\alpha$ rotation curves |
| $R_{\text{last}}$ range | 1–80 kpc |
| Data quality | Excellent; baryonic mass models provided |
| ED suitability | **High.** The transition from flat rotation to Keplerian decline would directly signal $R_{\text{edge}}$. |
| Limitation | Most curves end within the flat regime; few extend beyond the expected $R_{\text{edge}}$. |

**Verdict:** Best starting dataset. Look for galaxies with $R_{\text{last}} > 20$ kpc and hints of declining $v_{\text{circ}}$.

### 3.2 Gaia DR3 (Milky Way Stellar Halo)

| Property | Assessment |
|:---------|:----------|
| Coverage | Full sky; distances to $\sim 100$ kpc for bright giants |
| Data quality | Excellent within $\sim 30$ kpc; sparse beyond |
| ED suitability | **Moderate.** Can trace $\nu_*(r)$ to large $r$, but limited to one galaxy (MW). |
| Limitation | Stream contamination, selection effects, disc-halo separation. |

**Verdict:** Good for the MW only. Use as a consistency check after SPARC.

### 3.3 Dragonfly (Ultra-Diffuse Galaxies)

| Property | Assessment |
|:---------|:----------|
| Coverage | Small samples of UDGs in Coma and Virgo clusters |
| Data quality | Deep imaging ($\mu \sim 30$ mag/arcsec$^2$) |
| ED suitability | **Moderate.** UDGs are extended and low-density — more likely to show edges. |
| Limitation | Small sample; deprojection uncertainty; distance uncertainties. |

**Verdict:** Interesting but small sample. Use after SPARC and Gaia.

---

## 4. Extraction Pipeline

### 4.1 From Rotation Curve to Density Profile

Given a rotation curve $v(r_i)$ at radii $r_1 < r_2 < \ldots < r_N$:

```python
import numpy as np
from scipy.interpolate import UnivariateSpline

def rotation_to_density(r, v, G=4.302e-3):  # G in pc (km/s)^2 / Msun
    """Convert rotation curve to density profile.

    r: radii in kpc
    v: circular velocities in km/s
    G: gravitational constant in compatible units
    """
    r_pc = r * 1e3  # kpc to pc

    # Enclosed mass: M(r) = v^2 * r / G
    M_enc = v**2 * r_pc / G  # Msun

    # Density from d(M)/dr = 4*pi*r^2 * rho
    # Use finite differences on M_enc
    dM_dr = np.gradient(M_enc, r_pc)
    rho = dM_dr / (4 * np.pi * r_pc**2)  # Msun/pc^3

    return rho  # Msun/pc^3
```

### 4.2 Fit Three Profile Models

```python
from scipy.optimize import curve_fit

# Model 1: ED Barenblatt (parabolic cap)
def rho_ED(r, rho0, R_edge):
    x = np.clip(1 - (r / R_edge)**2, 0, None)
    return rho0 * np.sqrt(x)

# Model 2: NFW
def rho_NFW(r, rho_s, r_s):
    x = r / r_s
    return rho_s / (x * (1 + x)**2 + 1e-10)

# Model 3: Einasto
def rho_Einasto(r, rho_e, r_e, n):
    d_n = 3*n - 1./3 + 0.0079/n  # approx
    return rho_e * np.exp(-d_n * ((r/r_e)**(1./n) - 1))

def fit_profiles(r, rho, rho_err=None):
    """Fit ED, NFW, and Einasto to density data."""
    results = {}

    # ED fit (2 parameters)
    try:
        p_ed, c_ed = curve_fit(rho_ED, r, rho, p0=[rho[0], r[-1]*1.5],
                                sigma=rho_err, bounds=([0, r[0]], [np.inf, 10*r[-1]]))
        rho_pred = rho_ED(r, *p_ed)
        chi2_ed = np.sum(((rho - rho_pred) / (rho_err if rho_err is not None else 1))**2)
        results['ED'] = {'params': p_ed, 'chi2': chi2_ed, 'npar': 2}
    except:
        results['ED'] = None

    # NFW fit (2 parameters)
    try:
        p_nfw, c_nfw = curve_fit(rho_NFW, r, rho, p0=[rho[0]*r[1], r[-1]/5],
                                  sigma=rho_err, bounds=([0, 0.01], [np.inf, 10*r[-1]]))
        rho_pred = rho_NFW(r, *p_nfw)
        chi2_nfw = np.sum(((rho - rho_pred) / (rho_err if rho_err is not None else 1))**2)
        results['NFW'] = {'params': p_nfw, 'chi2': chi2_nfw, 'npar': 2}
    except:
        results['NFW'] = None

    # Einasto fit (3 parameters)
    try:
        p_ein, c_ein = curve_fit(rho_Einasto, r, rho, p0=[rho[0], r[-1]/3, 4],
                                  sigma=rho_err, bounds=([0, 0.01, 0.5], [np.inf, 10*r[-1], 20]))
        rho_pred = rho_Einasto(r, *p_ein)
        chi2_ein = np.sum(((rho - rho_pred) / (rho_err if rho_err is not None else 1))**2)
        results['Einasto'] = {'params': p_ein, 'chi2': chi2_ein, 'npar': 3}
    except:
        results['Einasto'] = None

    return results
```

### 4.3 Extract $R_{\text{edge}}$

```python
def extract_R_edge(r, rho, threshold_frac=0.01):
    """Find the radius where density drops below threshold."""
    rho_max = rho.max()
    threshold = threshold_frac * rho_max
    above = np.where(rho > threshold)[0]
    if len(above) > 0:
        R_edge = r[above[-1]]
    else:
        R_edge = r[-1]  # density never drops below threshold
    return R_edge
```

---

## 5. Comparison Metrics

### 5.1 Edge Detection

| Metric | ED prediction | NFW prediction | How to measure |
|:-------|:-------------|:---------------|:---------------|
| $R_{\text{edge}}$ exists? | **Yes** | No (infinite extent) | Is there $r$ where $\rho < 0.01 \rho_0$? |
| $\rho(r)$ at $r = 1.5 R_s$ | $> 0$ (still within halo) | $\sim 0.02 \rho_s$ | Direct from profile |
| $\rho(r)$ at $r = R_{\text{edge}}$ | $= 0$ | $> 0$ | Direct from profile |
| Edge shape | $\sqrt{R_{\text{edge}} - r}$ | $r^{-3}$ | Log-log slope at large $r$ |

### 5.2 Goodness of Fit

| Metric | Definition | Threshold |
|:-------|:-----------|:----------|
| $\chi^2_\nu$ | $\chi^2 / (N - n_{\text{par}})$ | $< 2$ for acceptable fit |
| $\Delta\text{BIC}$ | BIC(NFW) $-$ BIC(ED) | $> 6$ for strong ED preference |
| $\Delta\text{AIC}$ | AIC(NFW) $-$ AIC(ED) | $> 4$ for strong preference |
| Edge residual | Mean $|\rho_{\text{data}} - \rho_{\text{model}}|$ at $r > 0.7 R_{\text{last}}$ | ED residual $<$ NFW residual |

BIC penalises extra parameters: $\text{BIC} = \chi^2 + n_{\text{par}} \ln N$. ED has 2 parameters ($\rho_0$, $R_{\text{edge}}$), NFW has 2 ($\rho_s$, $r_s$), and Einasto has 3 ($\rho_e$, $r_e$, $n$). ED and NFW are directly comparable; Einasto is penalised for the extra parameter.

### 5.3 Edge Sharpness

```python
def edge_sharpness(r, rho, R_edge_est):
    """Measure sharpness: slope at 0.9 R_edge / slope at R_max."""
    # Gradient
    grad = np.gradient(rho, r)

    # Slope near edge (at 0.9 * R_edge)
    idx_edge = np.argmin(np.abs(r - 0.9 * R_edge_est))
    slope_edge = np.abs(grad[idx_edge])

    # Slope at profile maximum (should be ~0)
    slope_max = np.max(np.abs(grad[:len(grad)//4]))

    # Ratio: high = sharp edge; low = gradual tail
    return slope_edge / (slope_max + 1e-20)
```

---

## 6. Success / Failure Criteria

| Criterion | Threshold | How to assess |
|:----------|:----------|:-------------|
| $R_{\text{edge}}$ detected in $\geq 3$ galaxies | $\rho < 0.01\rho_0$ at some $r < R_{\text{last}}$ | Profile drops to near-zero |
| ED fit preferred over NFW | $\Delta\text{BIC} > 6$ in $\geq 3$ galaxies | Information-criterion comparison |
| Edge shape consistent with parabolic | Log-log slope near edge $\approx 0.5$ | Slope measurement |
| $R_{\text{edge}}$ scales with $M^{1/3}$ | Correlation coefficient $> 0.7$ | Across SPARC sample |
| No Keplerian decline faked by baryonic disc | Control: fit baryon-only model and check for residual edge | Baryonic mass model subtraction |

### 6.1 What Counts as Success

**Strong success:** ED profile fits the outer rotation curve (or density profile) better than NFW by $\Delta\text{BIC} > 6$ in at least 5 galaxies, with a consistent $R_{\text{edge}}$ scaling.

**Moderate success:** A subset of SPARC galaxies ($\sim 10$–$20\%$) show evidence for declining $v(r)$ consistent with $R_{\text{edge}}$, even if the majority do not (because $R_{\text{last}} < R_{\text{edge}}$).

**Null result:** No galaxy in SPARC shows evidence for $R_{\text{edge}}$. All rotation curves are consistent with flat (NFW-like) to the last measured point.

### 6.2 What a Null Result Means

A null result does **not** falsify the ED halo prediction. It means either:

1. $R_{\text{edge}}$ is beyond the measured range ($R_{\text{edge}} > R_{\text{last}}$), or
2. The penalty channel ($P_0 > 0$) modifies the pure-PME profile near the edge, or
3. The galaxy-specific $\beta$ is larger than 2, producing a sharper edge at a smaller radius (harder to detect).

A null result would redirect the search to deeper surveys (Euclid weak lensing, Rubin LSST) or to dwarf galaxies (smaller $R_{\text{edge}}$, more accessible).

---

## 7. Practical Notes

### 7.1 SPARC Data Access

The SPARC database is publicly available at [astroweb.cwru.edu/SPARC](http://astroweb.cwru.edu/SPARC/). Each galaxy entry includes:

- Observed rotation curve $v_{\text{obs}}(r)$.
- Baryonic rotation curve $v_{\text{bar}}(r)$ (decomposed into disc, bulge, gas).
- Distance, inclination, and quality flag.

### 7.2 Baryonic Subtraction

To isolate the dark-matter (or ED) halo contribution:

$$v_{\text{halo}}^2(r) = v_{\text{obs}}^2(r) - v_{\text{bar}}^2(r).$$

The halo density is then derived from $v_{\text{halo}}(r)$ using the formula in Section 4.1.

### 7.3 Galaxy Selection

For the first test, select galaxies with:

1. Quality flag = 1 or 2 (high quality).
2. $R_{\text{last}} > 15$ kpc (extends well into the halo).
3. Flat or declining $v_{\text{obs}}$ at $R_{\text{last}}$ (not still rising).
4. Low inclination uncertainty ($< 5^\circ$).

This should yield $\sim 30$–$50$ galaxies from the SPARC sample of 175.

---

## 8. Next Steps

### 8.1 If Evidence for Halo Edges Is Found

1. **ED-Data-Galaxy-02: Full SPARC sweep.** Fit all 175 galaxies. Build an $R_{\text{edge}}$-vs-$M$ scaling relation. Compare to the ED prediction $R_{\text{edge}} \propto M^{1/3}$.

2. **Gaia cross-check.** Compare the MW $R_{\text{edge}}$ from SPARC-type analysis to the stellar halo truncation radius from Gaia DR3.

3. **Weak-lensing confirmation.** Stacked weak-lensing profiles from Subaru/HSC or Euclid should show $\Delta\Sigma(R) \to 0$ at $R \sim R_{\text{edge}}$.

### 8.2 If No Evidence Is Found

4. **Reinterpret as a lower bound.** $R_{\text{edge}} > R_{\text{last}}$ for most galaxies. This constrains $R_{\text{edge}}$ from below.

5. **Focus on dwarfs.** Dwarf spheroidal galaxies have smaller expected $R_{\text{edge}}$ ($\sim 2$ kpc) and well-measured stellar kinematics. They may be the best targets for detecting ED edges.

6. **Include penalty channel.** Run the full ED PDE (not pure PME) with $P_0 > 0$ and compare. The penalty modifies the edge shape: instead of going to zero, the density approaches $\rho^*$. If $\rho^*$ is very low, the edge is still effectively sharp.

### 8.3 Pipeline Status

| Note | Title | Status |
|:-----|:------|:-------|
| ED-Data-01–11 | Condensed-matter pipeline | **Complete** |
| **ED-Data-Galaxy-01** | **First Halo Edge Test** | **Complete** |
| ED-Data-Galaxy-02 | Full SPARC sweep | Planned |
| ED-Data-Galaxy-03 | Gaia MW halo | Planned |
| ED-Data-Galaxy-04 | Weak-lensing stacking | Planned |
