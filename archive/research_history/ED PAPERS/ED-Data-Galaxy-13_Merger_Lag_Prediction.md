# ED-Data-Galaxy-13: Merger-Lag Prediction

**Allen Proxmire**
**March 2026**

---

## 0. Purpose

Galaxy-12 identified the first ED-unique discriminator: activity-dependent weak-lensing velocities. This note derives the **second**: the temporal-tension halo should **lag behind** the baryonic mass during galaxy and cluster mergers, producing a measurable offset between the mass centroid and the lensing centroid.

This prediction is unique to ED:
- **$\Lambda$CDM:** Collisionless dark matter tracks the collisionless stars. Gas lags behind both (ram-pressure stripping). The lensing peak is *ahead of* the gas.
- **MOND:** Modified gravity is instantaneous (no propagation delay). No lag.
- **ED:** The temporal-tension field is diffusive. It cannot move ballistically. It lags *behind* the baryons. The lensing signal (which includes the temporal contribution) peaks *behind* the mass.

The direction of the offset is **opposite** to the Bullet Cluster prediction in $\Lambda$CDM. This makes the test unambiguous.

---

## 1. ED Merger Dynamics

### 1.1 The Temporal-Tension Field During a Merger

The temporal-tension field $T(\mathbf{x}, t)$ satisfies:

$$\partial_t T = D_T\,\nabla^2 T + S(\mathbf{x}, t) - \lambda\,T,$$

where $S(\mathbf{x}, t)$ is the source (concentrated at the baryonic centre), $D_T$ is the temporal diffusivity, and $\lambda$ is the decay rate.

During a merger, the source moves ballistically at velocity $v_{\text{merge}}$. The field $T$ responds diffusively: it cannot "jump" to the new source location. Instead, it forms a **wake** — a trail of elevated $T$ behind the moving source.

### 1.2 The Steady-State Wake

For a source moving at constant velocity $v$ through a diffusive medium, the steady-state solution in the co-moving frame is:

$$T(x') \propto e^{-x'/\ell_{\text{wake}}}, \qquad \ell_{\text{wake}} = \frac{D_T}{v_{\text{merge}}}.$$

The wake length $\ell_{\text{wake}}$ is the characteristic distance by which the $T$-field trails the source. This is the predicted **lag distance**.

### 1.3 Transport Parameters

The temporal diffusivity $D_T$ is estimated from the requirement that the $T$-field extends coherently to $\sim 1$ Mpc (the Mistele et al. observation). The tension length $\ell_T = \sqrt{D_T/\lambda}$, with $\lambda \sim 1/t_H$:

$$D_T = \lambda\,\ell_T^2 = \frac{1}{t_H}\,(1\;\text{Mpc})^2 \approx 2.1 \times 10^{27}\;\text{m}^2/\text{s}.$$

### 1.4 Lag Build-Up Time

The lag reaches its steady-state value on a timescale:

$$t_{\text{lag}} = \frac{D_T}{v_{\text{merge}}^2} = \frac{\ell_{\text{wake}}}{v_{\text{merge}}}.$$

For fast mergers, the lag develops rapidly. For slow mergers, it takes longer — but the lag distance is also larger.

---

## 2. Predicted Lensing Offsets

### 2.1 Lag Distance by Merger Type

| System | $v_{\text{merge}}$ (km/s) | $\ell_{\text{lag}}$ (kpc) | $t_{\text{lag}}$ (Myr) | Angular offset ($z = 0.1$) |
|:-------|:--------------------------|:-------------------------|:-----------------------|:---------------------------|
| Dwarf–dwarf | 50 | **1350** | 26,000 | $> 10'$ (unphysical: exceeds system size) |
| Spiral–spiral | 300 | **225** | 730 | $\sim 2'$ |
| Cluster–cluster | 1500 | **45** | 29 | $\sim 24''$ |
| Bullet Cluster | 4500 | **15** | 3 | $\sim 8''$ |

### 2.2 Physical Interpretation

**Dwarf mergers:** The lag distance (1350 kpc) greatly exceeds the system size ($\sim 10$ kpc). This means the $T$-field essentially does not respond to the merger — it remains at the pre-merger configuration. The "lensing halo" would appear detached from the merging dwarfs.

**Spiral mergers:** The lag (225 kpc) is comparable to the halo extent. The $T$-field peak trails significantly behind the baryonic peak. This is observable with current weak-lensing surveys.

**Cluster mergers:** The lag (45 kpc) is well within the cluster core radius ($\sim 100$–$300$ kpc). The offset between the lensing peak and the mass peak is $\sim 24''$ at $z = 0.1$ — well within the angular resolution of HSC, Euclid, and Rubin.

**Bullet Cluster:** The lag (15 kpc) at $v = 4500$ km/s is small but measurable ($\sim 8''$). This is the most testable regime.

### 2.3 Caveat: $D_T$ Uncertainty

The temporal diffusivity $D_T$ is estimated from the tension length ($\ell_T \sim 1$ Mpc) and the Hubble decay rate ($\lambda \sim 1/t_H$). Both are order-of-magnitude estimates. A factor-of-10 change in $D_T$ would scale all lag distances by the same factor. The relative ranking (cluster lags $<$ spiral lags $<$ dwarf lags) is robust; the absolute values are uncertain by a factor of $\sim 3$–$10$.

---

## 3. The Bullet Cluster: Opposite Offset

### 3.1 $\Lambda$CDM Prediction

In $\Lambda$CDM, the Bullet Cluster (1E 0657-56) is interpreted as a collision between two galaxy clusters. The observed offset between the X-ray gas (hot ICM) and the weak-lensing mass peak is explained by:

- **Gas:** collisional (ram-pressure stripping) $\to$ gas lags behind.
- **Dark matter:** collisionless $\to$ DM passes through, leading the gas.
- **Lensing peak:** coincides with DM $\to$ *ahead of* the gas.

### 3.2 ED Prediction

In ED, the same collision is interpreted differently:

- **Baryons (stars + gas):** both move ballistically through the collision.
- **Temporal-tension field:** diffusive $\to$ lags behind the baryons.
- **Lensing signal:** includes temporal-tension contribution $\to$ peaks *behind* the baryonic mass.

The offset direction is **opposite** to $\Lambda$CDM:

| Component | $\Lambda$CDM position | ED position |
|:----------|:---------------------|:------------|
| Stars | Intermediate | Leading |
| Gas | Lagging (ram pressure) | Lagging (ram pressure) |
| DM / $T$-field | **Leading** | **Lagging** |
| Lensing peak | Ahead of gas | **Behind stars** |

### 3.3 The Observed Bullet Cluster

The Bullet Cluster observation shows the lensing peak coinciding with the galaxies (stars), *not* with the gas. This is consistent with $\Lambda$CDM (DM tracks stars; both lead the gas).

In ED, the $T$-field lag of 15 kpc at $v = 4500$ km/s would place the $T$-peak slightly *behind* the stellar peak. Whether this is consistent with the Bullet Cluster data depends on the $T$-field's fractional contribution to the total lensing signal. If the gravitational (mass-based) lensing dominates over the temporal contribution at cluster scales, the offset would be small and within the observational uncertainty ($\sim 10''$).

**Honest assessment:** The Bullet Cluster is not straightforwardly consistent with the ED prediction if temporal tension provides a large fraction of the lensing signal. If $V_{\text{temp}}$ is $\sim 100\%$ of $V_{\text{flat}}$ (as Galaxy-10 suggests for field galaxies), the offset should be detectable. If the cluster's deep gravitational potential dominates the lensing signal ($V_{\text{grav}} \gg V_{\text{temp}}$), the offset would be negligible.

---

## 4. Mock Observational Signatures

### 4.1 Lensing Map During a Cluster Merger

```python
import numpy as np

def mock_merger_lensing(v_merge, D_T, t_since, mass_1, mass_2,
                         R_grid, V_temp_frac=0.5):
    """Generate mock lensing convergence for an ED merger.

    v_merge: merger velocity (km/s)
    D_T: temporal diffusivity (m^2/s)
    t_since: time since closest approach (Myr)
    mass_1, mass_2: baryonic masses (Msun)
    R_grid: 2D array of positions (kpc)
    V_temp_frac: fraction of lensing from temporal tension
    """
    kpc = 3.086e19  # m
    v_ms = v_merge * 1e3
    t_s = t_since * 1e6 * 3.156e7

    # Baryonic positions (move ballistically)
    x1 = -v_ms * t_s / (2 * kpc)  # kpc
    x2 = +v_ms * t_s / (2 * kpc)

    # T-field peaks (lag behind baryons)
    lag = D_T / v_ms / kpc  # kpc
    x1_T = x1 + lag  # lag toward center (behind motion direction)
    x2_T = x2 - lag

    # Convergence maps (simplified as Gaussian peaks)
    sigma_mass = 50  # kpc (cluster core)
    sigma_T = 200    # kpc (wider temporal field)

    # Gravitational convergence (from mass)
    kappa_grav = (mass_1 * np.exp(-((R_grid[0]-x1)**2 + R_grid[1]**2)/(2*sigma_mass**2))
                + mass_2 * np.exp(-((R_grid[0]-x2)**2 + R_grid[1]**2)/(2*sigma_mass**2)))

    # Temporal convergence (from T-field, lagging)
    kappa_temp = (mass_1 * np.exp(-((R_grid[0]-x1_T)**2 + R_grid[1]**2)/(2*sigma_T**2))
                + mass_2 * np.exp(-((R_grid[0]-x2_T)**2 + R_grid[1]**2)/(2*sigma_T**2)))

    # Total lensing
    kappa_total = (1 - V_temp_frac) * kappa_grav + V_temp_frac * kappa_temp

    return kappa_grav, kappa_temp, kappa_total, lag
```

### 4.2 Expected Observables

For a cluster merger at $v = 1500$ km/s, $t = 100$ Myr post-closest-approach:

| Observable | Value |
|:-----------|:------|
| Baryonic separation | $\sim 150$ kpc |
| $T$-field lag per cluster | 45 kpc |
| Effective lensing-mass offset | 10–45 kpc (depends on $V_{\text{temp}}$ fraction) |
| Angular offset at $z = 0.3$ | $\sim 6''$–$27''$ |
| HSC/Euclid resolution | $\sim 0.2''$ |

The offset is $\sim 10$–$50\times$ the angular resolution — easily detectable if the signal-to-noise is sufficient.

---

## 5. Feasibility

### 5.1 Required Observations

| Requirement | Threshold | Current capability |
|:------------|:----------|:-------------------|
| Angular resolution | $< 5''$ | HSC: $0.6''$; Euclid: $0.2''$ |
| Lensing centroid precision | $< 10$ kpc ($\sim 5''$ at $z = 0.1$) | Single cluster: $\sim 10''$; stacked ($N = 30$): $\sim 2''$ |
| Number of merging systems | $> 10$ (for stacking) | $\sim 50$–$100$ known merging clusters |
| Spectroscopic redshifts | For distance/velocity | Available for most clusters |

### 5.2 Candidate Systems

| System | $v_{\text{merge}}$ (km/s) | $z$ | Predicted $\ell_{\text{lag}}$ (kpc) | Angular lag |
|:-------|:--------------------------|:----|:------------------------------------|:-----------|
| 1E 0657-56 (Bullet) | 4500 | 0.296 | 15 | $\sim 3''$ |
| MACS J0025.4 (Baby Bullet) | 2000 | 0.586 | 34 | $\sim 5''$ |
| Abell 520 | 2500 | 0.201 | 27 | $\sim 8''$ |
| Musket Ball Cluster | 1200 | 0.530 | 56 | $\sim 8''$ |

### 5.3 Stacking Strategy

For individual clusters, the centroid precision is $\sim 10''$. Stacking $N$ merging clusters reduces this to $\sim 10''/\sqrt{N}$:

| $N_{\text{clusters}}$ | Centroid precision (arcsec) | Precision (kpc at $z = 0.2$) | Detectable lag |
|:-----------------------|:---------------------------|:------------------------------|:---------------|
| 10 | 3.2 | 10 | $> 30$ kpc |
| 30 | 1.8 | 6 | $> 15$ kpc |
| 100 | 1.0 | 3 | $> 10$ kpc |

With 30 merging clusters, lags $> 15$ kpc are detectable at $3\sigma$. This is achievable with current surveys.

---

## 6. Comparison to Other Models

| Prediction | ED | $\Lambda$CDM | MOND |
|:-----------|:---|:-------------|:-----|
| Lensing-mass offset in mergers? | **Yes** ($T$-field lags baryons) | **Yes** (gas lags DM) | **No** |
| Direction of offset | **Lensing behind baryons** | **Lensing ahead of gas** | N/A |
| Offset magnitude (Bullet) | $\sim 15$ kpc | $\sim 100$ kpc (gas-DM separation) | 0 |
| Offset in cluster-cluster? | **Yes** (always) | Only for gas-DM | **No** |
| Offset in galaxy-galaxy? | **Yes** ($\sim 50$–$200$ kpc) | Very small | **No** |

The key distinction: in $\Lambda$CDM, the offset is between **gas** and **DM**. In ED, the offset is between **baryons** (stars) and the **temporal-tension lensing signal**. These are different components and different directions.

---

## 7. Honest Assessment

| Question | Answer |
|:---------|:-------|
| Is the merger-lag prediction unique to ED? | **Yes** — neither MOND nor $\Lambda$CDM predicts a diffusive lensing lag |
| Is the predicted lag detectable? | **Yes** — 15–45 kpc for clusters ($> 3''$ at typical redshifts) |
| Is it distinguishable from $\Lambda$CDM offsets? | **Yes** — opposite direction (behind baryons, not ahead of gas) |
| Is $D_T$ well-determined? | **No** — uncertain by factor $\sim 3$–$10$ |
| Is the Bullet Cluster consistent with ED? | **Unclear** — depends on $V_{\text{temp}}$ fraction at cluster scales |
| Can current surveys detect the lag? | **Probably** — with $\sim 30$ stacked merging clusters |

---

## 8. The Two ED-Unique Tests

Combining Galaxy-12 and Galaxy-13, ED now has two tests that are *exclusively* ED predictions:

| Test | ED prediction | MOND prediction | $\Lambda$CDM prediction |
|:-----|:-------------|:----------------|:-----------------------|
| Activity-dependent $V$ at fixed $M_b$ | $\Delta V \sim 30$–$70$ km/s | 0 | 0 |
| Lensing-baryon offset in mergers | 15–45 kpc behind baryons | 0 | Gas-DM offset (opposite direction) |

If *either* test produces a positive detection consistent with the ED prediction, the temporal-tension interpretation is strongly supported. If *both* tests produce positive detections, ED becomes the leading candidate explanation for galaxy-scale dynamics.

---

## 9. Next Steps

### 9.1 Immediate

1. **Bullet Cluster reanalysis.** Examine the published Bullet Cluster lensing reconstruction for any offset between the lensing peak and the stellar-mass peak (not the gas peak). In $\Lambda$CDM, these should coincide. In ED, the lensing peak should be $\sim 15$ kpc behind the stellar peak.

2. **Stacked merger analysis.** Identify $\sim 30$ merging clusters from existing surveys (SDSS, ACT, SPT). Stack the weak-lensing signal relative to the stellar-mass centroid. Measure any systematic offset.

### 9.2 Medium-Term

3. **Euclid merging-cluster program.** Euclid will discover $\sim 10^4$ galaxy clusters, of which $\sim 1000$ will be merging. Stacking $\sim 100$ merging systems would achieve centroid precision of $\sim 3$ kpc — sufficient to detect lags of $> 10$ kpc.

4. **Galaxy-galaxy merger lensing.** For spiral-spiral mergers ($\ell_{\text{lag}} \sim 225$ kpc), the offset is much larger but the lensing signal per system is much weaker. Stacking $\sim 10^4$ merging galaxy pairs from LSST could detect the average offset.

### 9.3 Pipeline Status

| Note | Key Result |
|:-----|:-----------|
| Galaxy-12 | Activity dependence: $\Delta V \sim 30$–$70$ km/s; detectable with current surveys |
| **Galaxy-13** | **Merger lag: 15–45 kpc; opposite to ΛCDM Bullet Cluster; detectable by stacking 30 merging clusters** |
| Galaxy-14 | Planned: cluster-scale temporal-tension superposition |
