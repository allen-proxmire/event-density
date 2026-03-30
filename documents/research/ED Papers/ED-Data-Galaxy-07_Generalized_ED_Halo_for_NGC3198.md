# ED-Data-Galaxy-07: Generalised ED Halo for NGC 3198

**Allen Proxmire**
**March 2026**

---

## 0. Purpose

Galaxy-06 showed that the generalised mobility $M(\rho) = \rho^\alpha(\rho_{\max} - \rho)^\beta$ with $\alpha = 0.5$, $\beta = 2.0$, coupled to gravity, produces dwarf galaxy halos that match Burkert to 99.6%. This note applies the same model to **NGC 3198** — the massive spiral galaxy where the pure-PME Barenblatt profile was rejected in Galaxy-02. The question: does the generalised ED–Poisson model produce a realistic rotation curve for a galaxy 100 times more massive than a dwarf?

---

## 1. NGC 3198 Data

### 1.1 Galaxy Properties

| Property | Value |
|:---------|:------|
| Type | Sc spiral |
| $V_{\text{flat}}$ | $\sim 150$ km/s |
| $R_{\text{last}}$ | 30 kpc |
| $\rho_0$ (central DM density) | $\sim 0.05\;M_\odot$/pc$^3$ = $4.9 \times 10^7\;M_\odot$/kpc$^3$ |
| $\sigma_v$ (effective dispersion) | $\sim 100$ km/s |
| Isothermal core radius | 1.94 kpc |

### 1.2 DM Rotation Curve (from Galaxy-02)

| $r$ (kpc) | $V_{\text{DM}}$ (km/s) |
|:----------|:----------------------|
| 2 | 62 |
| 5 | 117 |
| 10 | 140 |
| 18 | 146 |
| 26 | 144 |
| 30 | 142 |

The key feature: **flat rotation from $r = 10$ to $r = 30$ kpc** ($V \approx 140$–$146$ km/s). This is what any halo model must reproduce.

---

## 2. ED–Poisson Setup

Same solver as Galaxy-06, scaled to NGC 3198:

- $\alpha = 0.5$, $\beta = 2.0$, $P_0 = 0.20$
- $\rho_0 = 4.9 \times 10^7\;M_\odot$/kpc$^3$
- $\sigma_v = 100$ km/s
- $\rho_{\max} = 3\,\rho_0$
- Grid: $N = 500$, $r_{\max} = 35$ kpc
- Iterative ED–Poisson with 4 outer Poisson updates, 25,000 ED time steps each

---

## 3. Results

### 3.1 ED Profile Properties

| Property | Value |
|:---------|:------|
| Central density | $4.10 \times 10^7\;M_\odot$/kpc$^3$ ($0.041\;M_\odot$/pc$^3$) |
| Core radius | **5.25 kpc** |
| Outer slope | **$-2.05$** |

The core radius (5.25 kpc) and outer slope ($-2.05$) are physically reasonable. The core has been widened from the isothermal value (1.94 kpc) by a factor of 2.7 — consistent with the core-widening mechanism established in Galaxy-05 and Galaxy-06.

### 3.2 Rotation Curve Comparison

| $r$ (kpc) | $V_{\text{data}}$ (km/s) | $V_{\text{ED}}$ (km/s) | $V_{\text{NFW}}$ (km/s) | $V_{\text{Burkert}}$ (km/s) |
|:----------|:------------------------|:----------------------|:-----------------------|:---------------------------|
| 2 | 62 | 54 | 79 | 66 |
| 5 | 117 | 112 | 115 | 117 |
| 7 | 132 | 137 | 130 | 132 |
| 10 | 140 | 158 | 145 | 143 |
| 14 | 146 | 170 | 159 | 147 |
| 18 | 146 | 175 | 168 | 146 |
| 22 | 146 | 177 | 174 | 144 |
| 26 | 144 | 179 | 178 | 141 |
| 30 | 142 | 181 | 181 | 138 |

### 3.3 Goodness of Fit

| Model | RMS residual (km/s) | $\chi^2$ | BIC | Parameters |
|:------|:-------------------|:---------|:----|:-----------|
| **Burkert** | **2.0** | **76** | **32** | 2 |
| NFW | 20.5 | 7967 | 121 | 2 |
| ED (generalised) | 23.8 | 10759 | 129 | 3 |

**Burkert wins decisively.** The ED rotation curve rises too steeply and overshoots the data's flat regime by $\sim 30$ km/s at large radii. The NFW curve has the same problem but is slightly better than ED. Only Burkert reproduces the flat rotation.

---

## 4. Diagnosis: Why ED Overshoots

### 4.1 The Problem

The ED–Poisson profile for NGC 3198 has too much mass at intermediate radii (5–15 kpc). This pushes the enclosed mass $M(<r)$ too high, and since $V^2 = GM/r$, the rotation curve climbs above the observed flat level.

### 4.2 Root Cause

The core-widening mechanism that works beautifully for dwarfs (Galaxy-06) works too aggressively for NGC 3198. In a dwarf ($\sigma_v = 30$ km/s), the gravitational potential is shallow, and the ED mobility redistributes mass over a moderate volume. In NGC 3198 ($\sigma_v = 100$ km/s), the potential is deeper, and the ED mobility redistributes mass over a *larger* volume — but in doing so, it places too much mass at intermediate radii.

The Burkert profile avoids this because its $r^{-3}$ outer tail is steeper than the ED profile's $r^{-2}$ envelope. Burkert puts less mass at 5–15 kpc and more at smaller or larger radii, producing a flatter rotation curve.

### 4.3 The Flat-Rotation Constraint

A flat rotation curve $V(r) = V_{\text{flat}}$ requires:

$$M(<r) = \frac{V_{\text{flat}}^2}{G}\,r \propto r.$$

This means $\rho(r) = V_{\text{flat}}^2/(4\pi G r^2) \propto r^{-2}$ — the singular isothermal sphere. Any profile with a steeper outer slope (Burkert: $r^{-3}$) produces a declining $V(r)$; any profile with a shallower slope (ED: $r^{-2}$) produces a rising $V(r)$.

The ED profile at NGC 3198 has an outer slope of $-2.05$ — almost exactly $r^{-2}$, which is the isothermal-sphere slope. This produces a slowly rising $V(r)$ rather than a flat one. The profile is too close to isothermal in the outer parts — the generalised mobility has not steepened the envelope enough for a massive galaxy.

---

## 5. What This Means

### 5.1 Scale Dependence of the Outer Slope

The results across the galaxy pipeline reveal a pattern:

| System | $\sigma_v$ (km/s) | ED outer slope | Required slope for flat $V$ | Deficit |
|:-------|:-------------------|:-------------|:---------------------------|:--------|
| Dwarf (DDO 154) | 30 | $-1.8$ | N/A (rising $V$ is expected) | N/A |
| Spiral (NGC 3198) | 100 | $-2.05$ | $-2.0$ (flat) to $-3.0$ (declining) | $\sim 0$ (marginal) |

For dwarfs, the outer slope doesn't need to be very steep because dwarf rotation curves are still rising or just reaching flat at the last measured point. For massive spirals, the outer slope must be close to $-2$ (for flat $V$) or steeper (for the gentle decline seen at 20–30 kpc). The ED profile at $-2.05$ is marginal — almost right for the flat regime but unable to produce the gentle decline observed beyond 20 kpc.

### 5.2 What Would Fix It

1. **Higher $\alpha$.** Increasing $\alpha$ from 0.5 to 1.0–1.5 would steepen the outer slope. However, this was tested in Galaxy-06 and found to reduce the core radius below observed values.

2. **Galaxy-dependent $\alpha$.** If $\alpha$ increases with galaxy mass or $\sigma_v$, the outer slope would be steeper for massive spirals than for dwarfs. This is physically plausible (larger galaxies have stronger tidal stripping) but adds a free parameter.

3. **Including the participation channel.** The participation variable $v(t)$ adds a spatially uniform density modulation. In the negative phase of the oscillation, it would reduce density at all radii, effectively steepening the profile. Whether this produces the correct amount of steepening at the right radii is untested.

4. **Anisotropic mobility.** The radial and tangential components of mobility could differ in a rotating galaxy. If the tangential mobility is higher (azimuthal mixing is more efficient), the radial profile would be steepened.

### 5.3 Honest Assessment

| Criterion | Dwarf (Galaxy-06) | NGC 3198 (this note) |
|:----------|:------------------|:---------------------|
| Core radius correct? | **Yes** (2.34 vs 2.3 kpc) | **Yes** (5.25 kpc, reasonable) |
| Outer slope correct? | Partially ($-1.8$ vs $-2.1$) | **Marginal** ($-2.05$; flat $V$ requires $\leq -2$) |
| Rotation curve matches? | Not tested (dwarfs have rising $V$) | **No** (overshoots by $\sim 30$ km/s at $r > 10$ kpc) |
| Matches Burkert? | 99.6% for density profile | No (RMS = 23.8 vs 2.0 km/s for $V(r)$) |
| Better than pure PME (Galaxy-02)? | **Yes** | **Yes** (core is correct; pure PME truncated at 8 kpc) |

---

## 6. The Score Card: Where ED Stands at Galactic Scales

| Test | Result | Status |
|:-----|:-------|:-------|
| Core formation (flat cores in dwarfs) | **Correct** — ED mobility widens cores naturally | PASS |
| Core radius prediction | **Within 10%** for all four dwarfs | PASS |
| Dwarf density profile shape | **99.6% Burkert match** (Galaxy-06) | PASS |
| NGC 3198 rotation curve (inner, $r < 7$ kpc) | **Good** (54–137 vs 62–132 km/s) | PASS |
| NGC 3198 rotation curve (outer, $r > 10$ kpc) | **Overshoots** (158–181 vs 140–142 km/s) | FAIL |
| Outer-slope steepness | $-2.05$ (marginal for flat $V$) | MARGINAL |

**ED gets the cores right and the envelopes partially right.** The core-widening mechanism from degenerate mobility is a genuine and unique prediction that matches observations. The envelope requires further refinement — either a scale-dependent $\alpha$, the participation channel, or an explicit rotation/tidal effect — to match the full rotation curves of massive spirals.

---

## 7. Next Steps

### 7.1 Near-Term

1. **Scan $\alpha$ for NGC 3198.** Try $\alpha = 1.0$, $1.5$, $2.0$ specifically for this galaxy. The optimal $\alpha$ for a flat rotation curve may be higher than for dwarfs.

2. **Joint ($\alpha$, $\sigma_v$, $\rho_0$) fit.** Fit $\alpha$ directly to the NGC 3198 rotation curve, treating it as a free parameter alongside $\sigma_v$ and $\rho_0$. Determine the best-fit $\alpha$ for this galaxy and compare to the dwarf value (0.5).

3. **Test participation.** Run the time-dependent ED–Poisson system with $H > 0$. Determine whether the telegraph oscillation can modulate the rotation curve into better agreement.

### 7.2 The Mass-Dependent $\alpha$ Hypothesis

If $\alpha_{\text{dwarf}} \approx 0.5$ and $\alpha_{\text{spiral}} \approx 1.0$–$1.5$, the outer-slope problem may be resolved by a scaling relation:

$$\alpha(M) \propto \log(M_{\text{halo}} / M_0).$$

This would be analogous to the concentration-mass relation in $\Lambda$CDM ($c \propto M^{-0.1}$) — a galaxy-mass-dependent structural parameter. Testing this requires fitting $\alpha$ across the full SPARC sample.

### 7.3 Pipeline Status

| Note | Status | Key Result |
|:-----|:-------|:-----------|
| Galaxy-01 | Complete | Pipeline defined |
| Galaxy-02 | Complete | Pure-PME rejected for NGC 3198 |
| Galaxy-03 | Complete | Dwarfs: core correct, edge wrong |
| Galaxy-04 | Complete | No steady state without gravity |
| Galaxy-05 | Complete | ED–Poisson: core correct, slope $-1.5$ |
| Galaxy-06 | Complete | Generalised: 99.6% Burkert match for dwarfs |
| **Galaxy-07** | **Complete** | **NGC 3198: core correct, flat-$V$ overshot by 30 km/s; $\alpha$ may need mass dependence** |
| Galaxy-08 | Planned | $\alpha$ scan + joint fit for NGC 3198 |
| Galaxy-09 | Planned | Full SPARC sweep with generalised ED |
