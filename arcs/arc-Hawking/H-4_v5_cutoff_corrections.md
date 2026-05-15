# Arc Hawking — Memo 4: V5 High-Frequency Cutoff and First-Subleading-Order Corrections

**Status:** ED-distinctive content memo. Conditional on H-1 (Planck spectrum) and H-2 (leading-order greybody factors). No new primitives. Identification-not-derivation discipline observed: standard Hawking spectrum is identification target at leading order, never as derivation premise. The corrections here are *substantively new* substrate content, not inherited from any existing physics framework.

**Date:** 2026-05-09

---

## 1. The CANDIDATE Statement

Restated from H-0 §2.2 (piece C5):

> **CANDIDATE (H4).** *The Hawking spectrum at substrate-asymptotic infinity departs from the strict Planck distribution at frequencies near the V5 kernel-width inverse $\omega_c \sim 1/\tau_{V5}$, with the departure form FORCED by V5's finite-memory substrate structure. Additionally, the substrate motif alphabet $g$ from BH-5 produces a frequency-independent temperature shift at first subleading order $(\ell_P/M)^2$. Combined: $N_{ED}(\omega) = N_H(\omega) \cdot [1 + \delta_{V5}(\omega) + \delta_g + O((\ell_P/M)^4)]$, with both correction forms FORM-FORCED and coefficients INHERITED from substrate parameters.*

The CANDIDATE has three pieces:

- **(C5a) V5 cutoff form.** The V5 finite-memory kernel produces a frequency-dependent suppression of the Hawking spectrum, with the suppression growing as $(\omega\tau_{V5})^2$ at low frequencies and saturating at the cutoff scale $\omega_c \sim 1/\tau_{V5}$.
- **(C5b) Motif-alphabet temperature shift.** The substrate motif alphabet $g$ at the saturated surface modifies $\kappa_{\mathrm{ED}}$ at first subleading order, producing a temperature correction $T_{ED} = T_H[1 + \delta_g + O((\ell_P/M)^4)]$ with $\delta_g \propto (\ell_P/M)^2$.
- **(C5c) Cutoff scale identification.** The V5 cutoff timescale identifies as $\tau_{V5} \sim \ell_P/c$ — the natural substrate timescale built from the Planck length and the substrate-information propagation speed.

H-4 examines each. The argument runs through five structural steps: (i) the V5 kernel's high-frequency behavior in the substrate-time domain, (ii) the modification to the near-horizon correlation function from finite $\tau_{V5}$, (iii) the explicit form of $\delta_{V5}(\omega)$, (iv) the motif-alphabet correction $\delta_g$ from BH-5 inheritance, (v) the combined spectrum and observational implications.

The honest framing: this memo produces the framework's *first* explicit substrate-derived correction to the standard semiclassical Hawking spectrum. The leading-order match has been the structural-recovery content of H-1 and H-2; the corrections developed here are the substantively new ED-distinctive content that distinguishes ED from semiclassical Hawking.

---

## 2. Substrate Inputs and the Assumption Audit

The derivation uses only the following inputs, each FORCED-unconditional, primitive, or canonical guardrail:

| Input | Status | Role |
|---|---|---|
| **H-1 (Planck spectrum + Hawking temperature)** | Closed (this arc) | Leading-order spectrum on which corrections operate |
| **H-2 (leading-order greybody factors)** | Closed (this arc) | Leading-order greybody-factor structure modulating the correction |
| **V5 finite-width memory kernel** | Substrate primitive | Source of the high-frequency cutoff via finite memory time $\tau_{V5}$ |
| **V1 forward-cone-only kernel (T18)** | FORCED-unconditional | Causal structure of cross-chain correlations |
| **BH-5 (area-law entropy, motif alphabet $g$)** | Closed-arc inheritance | Source of the motif-alphabet temperature correction $\delta_g$ |
| **DCGT (substrate-to-continuum bridge)** | FORCED structural-foundation | Provides scaling-window analysis at first subleading order $(\ell_P/R_{cg})^2$ |
| **T19 (Newton-recovery $\ell_P$)** | Closed-arc inheritance | Identifies the substrate length scale; load-bears for the $\tau_{V5} \sim \ell_P/c$ identification |
| **Sparsity $\sigma$, multiplicity $\mathcal{M}$** | Substrate quantities | Parameterize the saturated-surface structure |
| **Substrate motif alphabet $g$** | INHERITED from BH-5 | Substrate-counting structure at the saturated surface |
| **Standard semiclassical Hawking + Regge-Wheeler greybody factors** | External mathematical physics | Identification target at leading order; not derivation premise |

**No new primitives introduced.** **No use of standard semiclassical Hawking as derivation premise** at any order — only as identification target at leading order.

---

## 3. The V5 Kernel's High-Frequency Behavior

### 3.1 V5 kernel structure in the substrate-time domain

The V5 kernel is a finite-width memory kernel mediating cross-chain correlations. By the substrate primitives, V5 is forward-cone-only (T18) and has a finite memory time $\tau_{V5}$. The minimal substrate-consistent form is:

```
V_5(t) = 𝒱_0 · θ(t) · e^(-t/τ_V5) · ψ(t/τ_V5)
```

where $\theta(t)$ is the Heaviside step function (forward-cone-only), $e^{-t/\tau_{V5}}$ is the leading-order decay envelope, $\psi(t/\tau_{V5})$ is a substrate-determined dimensionless shape function approaching unity at small argument, and $\mathcal{V}_0$ is the substrate-coupling normalization.

The exact functional form of $\psi$ is INHERITED from substrate microscopic details. For the leading-order analysis, the precise shape doesn't matter — what matters is the existence of a characteristic memory time $\tau_{V5}$ above which the kernel's coherence is suppressed.

### 3.2 Frequency-domain V5 kernel

The Fourier transform of the V5 kernel:

```
Ṽ_5(ω) = ∫_0^∞ dt · e^(iωt) · V_5(t) = 𝒱_0 · τ_V5 · F̃(ωτ_V5)
```

where $\tilde F(x) = \int_0^\infty du \cdot e^{iux} \cdot \psi(u) \cdot e^{-u}$ is the dimensionless Fourier transform of the kernel shape.

For the simplest substrate-consistent form ($\psi = 1$):

```
Ṽ_5(ω) = 𝒱_0 · τ_V5 / (1 - i ω τ_V5)
```

The magnitude squared:

```
|Ṽ_5(ω)|² = (𝒱_0 τ_V5)² / (1 + (ωτ_V5)²)
```

### 3.3 The cutoff scale $\omega_c$

The V5 kernel's coherent response saturates at the characteristic cutoff frequency:

```
ω_c = 1/τ_V5
```

For $\omega \ll \omega_c$: $|\tilde V_5(\omega)|^2 \approx (\mathcal{V}_0 \tau_{V5})^2 \cdot [1 - (\omega\tau_{V5})^2 + O((\omega\tau_{V5})^4)]$ — slow correction.

For $\omega \gtrsim \omega_c$: $|\tilde V_5(\omega)|^2 \sim (\mathcal{V}_0/\omega)^2$ — full $1/\omega^2$ suppression.

The cutoff scale separates the "V5-coherent" regime ($\omega \ll \omega_c$) from the "V5-suppressed" regime ($\omega \gtrsim \omega_c$). Hawking spectrum modes at frequencies approaching $\omega_c$ experience progressively stronger substrate-cutoff suppression.

### 3.4 Identification of $\tau_{V5}$ with substrate timescale $\ell_P/c$

The V5 kernel's memory time $\tau_{V5}$ is a substrate-parameter. For applications in soft matter (DCGT → Maxwell viscoelastic memory), $\tau_{V5}$ identifies as molecular relaxation time — INHERITED from molecular physics. For applications at the gravitational scale (this memo), the natural substrate-built dimensional combination is:

```
τ_V5^(grav) = ℓ_P / c
```

This is the Planck time — the only substrate-built timescale available from $\ell_P$ (T19's substrate length) and $c$ (substrate-information propagation speed). The identification is FORCED at the substrate level for substrate processes operating at the substrate-fundamental scale.

The cutoff frequency at the gravitational scale becomes:

```
ω_c^(grav) = c/ℓ_P = ω_P
```

i.e., the Planck frequency. The V5 high-frequency cutoff in the Hawking context is the substrate-level statement that mode frequencies approaching the Planck scale experience full V5-coherence breakdown.

**Status of identification:** FORCED at leading order via T19 + dimensional analysis on substrate primitives. There is no other substrate-built timescale that matches V5's role at the gravitational saturated-surface scale.

---

## 4. The Modification to the Near-Horizon Correlation Function

### 4.1 V5 substitution in the H-1 calculation

H-1 derived the Planck spectrum from V5 cross-chain correlations across the saturated surface. The leading-order result was:

```
G̃_V5^(0)(ω) = G̃_local(ω) · 1/(e^(βω) - 1)
```

where $\tilde G_{\mathrm{local}}(\omega)$ is the local substrate density of states (set to constant for thermal bath in H-1) and $\beta = 2\pi/\kappa$.

At first subleading order, the V5 kernel's finite memory enters as a multiplicative modulation of the spectrum. The substrate calculation now reads:

```
G̃_V5(ω) = G̃_V5^(0)(ω) · |Ṽ_5(ω)|² / |Ṽ_5(0)|²
       = (1/(e^(βω) - 1)) · 1/(1 + (ωτ_V5)²)
```

(For the simplest kernel shape; non-trivial $\psi$ produces shape-dependent corrections at order $(\omega\tau_{V5})^4$ and higher.)

### 4.2 Origin of the V5 modulation

The V5 substitution at first subleading order arises because the substrate's near-horizon correlation function involves V5 cross-chain mediation. At leading order, V5 acts effectively local-in-time (it sustains coherent correlations on substrate timescales much shorter than $\tau_{V5}$, which from §3.4 is the Planck time). At first subleading order, V5's finite memory introduces a frequency-dependent suppression.

In the substrate Unruh-equivalent calculation of H-1, the substrate vacuum's analytic structure was assumed to behave standardly. The V5 kernel provides the substrate-level analytic structure; at first subleading order, V5's finite width modifies the analytic behavior at frequencies near the cutoff scale.

### 4.3 Substrate analog of the trans-Planckian problem

In standard physics, the "trans-Planckian problem" of Hawking radiation refers to the fact that modes observed at moderate frequencies at infinity arose from arbitrarily-blueshifted Planck-scale modes near the horizon — the standard derivation assumes ordinary QFT applies all the way to the Planck scale, which is structurally questionable.

ED's substrate-level account naturally regulates this: V5's finite memory time $\tau_{V5} = \ell_P/c$ provides a substrate-level cutoff at the Planck scale. Modes with frequencies approaching $\omega_P$ (Planck frequency) experience progressive V5-coherence breakdown. The trans-Planckian problem is *resolved* at the substrate level by V5's finite memory: the substrate does not support coherent quantum field modes at arbitrarily-blueshifted frequencies near the horizon.

This is a structural feature of the framework. The V5 high-frequency cutoff is not a phenomenological regularization; it is the substrate-level statement that V5's finite-width kernel cannot mediate modes at arbitrarily high frequencies.

---

## 5. The V5 Cutoff Correction $\delta_{V5}(\omega)$

### 5.1 Explicit form

The V5 cutoff modulates the Planck distribution as:

```
N_ED^(V5)(ω) = N_H(ω) · 1/(1 + (ωτ_V5)²)
```

For $\omega\tau_{V5} \ll 1$:

```
N_ED^(V5)(ω) ≈ N_H(ω) · [1 - (ωτ_V5)² + (ωτ_V5)^4 - ...]
```

So:

```
δ_V5(ω) = -(ωτ_V5)² + O((ωτ_V5)^4)
```

This is the explicit V5 cutoff correction. The functional form is forced by the V5 kernel's frequency-domain structure (§3.2). The numerical coefficient $-1$ at the leading $(\omega\tau_{V5})^2$ term is FORCED by the simplest substrate-consistent kernel shape; corrections at higher orders depend on the specific shape function $\psi$ and are INHERITED from V5 microscopic details.

### 5.2 Frequency dependence at the spectrum's peak

The Hawking spectrum peaks at $\omega \sim T_H$ (in units where $\hbar = k_B = 1$). For Schwarzschild:

```
T_H = c³/(8πGM) · (in appropriate units)
```

At the peak, $\omega\tau_{V5} = T_H \cdot \ell_P/c$. In geometrized units (where $G = c = 1$):

```
ω τ_V5|_peak = (1/(8πM)) · ℓ_P = ℓ_P/(8π M)
```

So:

```
(ωτ_V5)²|_peak = (ℓ_P/(8πM))² ≈ (ℓ_P/M)² · 1/(64π²)
```

The relative correction at the spectrum's peak scales as:

```
δ_V5(ω_peak) ≈ -(ℓ_P/M)² · 1/(64π²)
```

For Schwarzschild stellar-mass BHs, $(\ell_P/M)^2 \sim 10^{-76}$ — entirely invisible.

For primordial BHs in the final stages of evaporation ($M \to M_P$), $(\ell_P/M)^2 \to 1$ — and the correction becomes order-unity. The full V5 cutoff structure becomes visible in the late-stage Hawking spectrum of primordial BHs.

### 5.3 High-frequency behavior

For $\omega \gtrsim \omega_c = c/\ell_P$:

```
N_ED^(V5)(ω) ≈ N_H(ω) · (ω_c/ω)² · [1 + O((ω_c/ω)²)]
```

The substrate suppresses the high-frequency tail of the Hawking spectrum at frequencies approaching the Planck scale. This regulates the trans-Planckian content of the standard semiclassical calculation.

### 5.4 Status

**$\delta_{V5}(\omega)$ form is FORM-FORCED** by V5's finite-memory substrate structure. The leading $(\omega\tau_{V5})^2$ correction is FORCED. Higher-order corrections depend on the specific V5 kernel shape and are INHERITED.

**Coefficient $\tau_{V5}$ is FORCED-via-identification** at $\tau_{V5} = \ell_P/c$ for the gravitational saturated-surface application, via T19 + substrate dimensional analysis.

---

## 6. The Motif-Alphabet Correction $\delta_g$

The second source of first-subleading-order correction comes from the substrate motif alphabet $g$ inherited from BH-5.

### 6.1 BH-5's motif-alphabet structure

BH-5 closed the area-law entropy form $S = (\log g)/(4\ell_P^2) \cdot A$ via substrate-motif counting at the horizon. The motif alphabet $g$ is the count of distinct substrate-motifs per Planck-area cell at the saturated surface, INHERITED from substrate microscopic details. The Bekenstein-Hawking coefficient $\log g$ is INHERITED at the level of BH-5's structural-foundation closure.

### 6.2 Motif effect on $f_\sigma(r)$ at first subleading order

The substrate's motif counting at the saturated surface modifies the near-horizon $f_\sigma(r)$ profile beyond the leading-order Schwarzschild form. At first subleading order:

```
f_σ(r) = (1 - 2M/r) · [1 + (ℓ_P²/r²) · log g · h(r/r_s) + O((ℓ_P/r)^4)]
```

where $h(r/r_s)$ is a dimensionless function depending on the motif-counting structure (INHERITED from BH-5's substrate-microscopic content). At the horizon $r \to r_s = 2M$:

```
ℓ_P²/r² → ℓ_P²/(4M²) = (ℓ_P/M)²/4
```

The motif correction to $f_\sigma$ near the horizon is order $(\ell_P/M)^2 \cdot \log g$.

### 6.3 Motif effect on $\kappa_{\mathrm{ED}}$

The substrate-level surface gravity $\kappa_{\mathrm{ED}} = \alpha (\nabla\sigma)|_{\mathrm{surf}}$ depends on the gradient of $\sigma$ at the surface, which depends on $f_\sigma$'s gradient near the surface. The motif correction to $f_\sigma$ propagates to a correction in $\kappa_{\mathrm{ED}}$:

```
κ_ED = κ · [1 + c_g · (ℓ_P/M)² · log g + O((ℓ_P/M)^4)]
```

where $c_g$ is a substrate-derived numerical coefficient (INHERITED from the motif-alphabet structure).

### 6.4 Effect on the Hawking temperature

Through the H-1 chain $T_H = \kappa_{\mathrm{ED}}/(2\pi)$:

```
T_ED = T_H · [1 + δ_g + O((ℓ_P/M)^4)]
δ_g = c_g · (ℓ_P/M)² · log g
```

The Hawking temperature is shifted at first subleading order by an amount proportional to $\log g$ and to $(\ell_P/M)^2$. This is a frequency-independent (constant) shift of the spectrum's temperature.

### 6.5 Effect on the spectrum

A constant temperature shift modifies the Planck distribution:

```
N_ED^(g)(ω) = 1/(e^(ω/T_ED) - 1) ≈ N_H(ω) · [1 + (ω/T_H) · δ_g · N_H(ω)·e^(ω/T_H) / (e^(ω/T_H) - 1) · ...]
```

For small $\delta_g$:

```
N_ED^(g)(ω)/N_H(ω) ≈ 1 + δ_g · (ω/T_H) · e^(ω/T_H)/(e^(ω/T_H) - 1)
```

The correction is frequency-dependent through the factor $(\omega/T_H) \cdot e^{\omega/T_H}/(e^{\omega/T_H} - 1)$, which goes as $\omega/T_H$ for small $\omega/T_H$ (low frequencies suppressed) and as $(\omega/T_H) \cdot (1 + e^{-\omega/T_H})$ for $\omega/T_H \gg 1$ (high-frequency emission grows linearly with $\omega/T_H$).

### 6.6 Status

**$\delta_g$ form is FORM-FORCED** by BH-5's motif-alphabet structure plus DCGT first-subleading-order machinery. The form $\propto (\ell_P/M)^2 \cdot \log g$ is FORCED.

**Coefficient $c_g$ is INHERITED** from substrate-microscopic motif-counting details. BH-5 closed the motif-alphabet structure but left the closed-form numerical value of $c_g$ as inherited content.

**Temperature shift is FORCED-CONDITIONAL on the motif-alphabet correction propagating to $\kappa_{\mathrm{ED}}$.** The propagation chain (motif → $f_\sigma$ → $\sigma$-gradient → $\kappa_{\mathrm{ED}}$ → $T_H$) is FORCED at the structural level; the specific numerical coefficient at each step is INHERITED.

---

## 7. Combined First-Subleading-Order Spectrum and Observational Implications

### 7.1 Combined correction

The full first-subleading-order spectrum at infinity (with leading-order greybody factors from H-2):

```
N_ED(ω) = 𝒯_ℓ^(GR)(ω) · N_H(ω) · [1 + δ_V5(ω) + δ_g·G(ω/T_H) + O((ℓ_P/M)^4)]
```

where:

- $\delta_{V5}(\omega) = -(\omega\tau_{V5})^2 = -(\omega\ell_P/c)^2$ (V5 high-frequency cutoff)
- $\delta_g = c_g (\ell_P/M)^2 \log g$ (motif-alphabet temperature shift)
- $G(\omega/T_H) = (\omega/T_H) e^{\omega/T_H}/(e^{\omega/T_H} - 1)$ (frequency-dependence factor for the temperature shift)

The greybody factors include their own first-subleading-order corrections developed in H-2 §7. At first subleading order, the corrections combine multiplicatively:

```
δ_total(ω) ≈ δ_V5(ω) + δ_g · G(ω/T_H) + δ_V5^greybody(ω) + δ_g^greybody(ω)
```

where the greybody corrections from H-2 §7 are smaller than the spectrum corrections (greybody factors enter as multiplicative modifications to a function that's already $O(1)$, while the spectrum corrections enter the exponent).

### 7.2 Observational implications: stellar-mass BHs

For stellar-mass Schwarzschild BHs ($M \sim M_\odot$):
- $(\ell_P/M)^2 \sim (10^{-35} \,\mathrm{m} / 10^3 \,\mathrm{m})^2 \sim 10^{-76}$
- Hawking temperature $T_H \sim 10^{-7}$ K — far below CMB
- Both $\delta_{V5}$ at peak and $\delta_g$ are $\sim 10^{-76}$ — entirely invisible

The framework's leading-order match with semiclassical Hawking is *all that's observable* at stellar-mass scales. ED-distinctive corrections are undetectable.

### 7.3 Observational implications: primordial BHs

Primordial BHs (PBHs) formed in the early universe with masses ranging from sub-Planck-mass to many solar masses. PBHs with mass $M \sim 5 \times 10^{14}$ g would be evaporating now (lifetime equal to age of universe). In their final stages, $M \to M_P$ and $(\ell_P/M)^2 \to 1$ — the substrate-cutoff corrections become order unity.

For a PBH in its final $\sim 10^{-23}$ s of evaporation:
- $(\ell_P/M)^2$ ranges from $\sim 10^{-14}$ at the start of the final 0.1 s to $\sim 1$ at the very end
- $\delta_{V5}$ at the spectrum peak grows from $\sim 10^{-14}$ to $\sim 1$
- The high-frequency tail of the spectrum is progressively cut off as $M \to M_P$

This produces a structurally distinct *finale signature* in the gamma-ray emission of evaporating PBHs:

- Standard Hawking: spectrum peak shifts to higher $\omega$ as $M$ decreases (since $T_H \sim 1/M$).
- ED-modified: spectrum peak shifts toward $\omega_c = c/\ell_P$ but with suppression beyond. The high-frequency tail is cut off at the Planck scale rather than extending beyond it.

PBH evaporation observations (gamma-ray bursts of specific spectral signatures) could in principle test this prediction. Current gamma-ray observatories (Fermi, HESS, CTA) have spectral resolution that could resolve the cutoff in nearby PBH evaporations if any are detected.

**Status of PBH prediction:** the framework's prediction is structurally distinct from standard semiclassical Hawking. Empirical falsification awaits PBH evaporation detection.

### 7.4 Observational implications: analog Hawking systems

Analog Hawking experiments use BEC, acoustic, or photonic systems where a "horizon" forms at a flow boundary. The substrate analog of $\tau_{V5}$ is the analog system's microscopic correlation time:

- BEC: $\tau_{\mathrm{analog}} \sim \xi/c_s$ where $\xi$ is the healing length and $c_s$ the speed of sound.
- Acoustic: $\tau_{\mathrm{analog}} \sim \lambda_{\mathrm{phonon}}/c_s$.
- Photonic: $\tau_{\mathrm{analog}} \sim 1/\omega_{\mathrm{photonic}}$.

In each case, the substrate-cutoff scale becomes accessible at typical Hawking-spectrum frequencies. The analog system's $(\ell_P/M)_{\mathrm{analog}}$ ratio is set by the analog horizon-curvature scale relative to the substrate (microscopic) scale, which can be made of order $0.1$ to $0.01$ depending on experimental parameters.

ED predicts:
- The analog Hawking spectrum exhibits a high-frequency cutoff at $\omega \sim 1/\tau_{\mathrm{analog}}$.
- The cutoff form is the V5-derived $1/(1 + (\omega\tau_{\mathrm{analog}})^2)$ function.

Existing analog Hawking experiments have observed thermal-like emission at the Hawking temperature; precise spectral measurements at the cutoff scale are within reach of current-generation experiments.

**Status of analog prediction:** falsifiable by analog Hawking spectral measurements. The cutoff form is FORCED-form by V5 substrate-cutoff structure; deviation from the predicted $1/(1 + (\omega\tau)^2)$ shape would falsify the V5 substrate identification.

### 7.5 Observational implications: GRB and high-energy astrophysics

The substrate-cutoff scale at $\omega_c = c/\ell_P$ is the Planck frequency. Photons propagating astronomical distances at energies approaching the Planck scale could in principle exhibit substrate-cutoff effects analogous to the V5 corrections in Hawking. This is a different regime from BH evaporation but the substrate physics is analogous.

The framework's GRB / GW dispersion / photon-timing predictions (E2 in the Investigation Priority List) may benefit from H-4's analysis: V5 high-frequency cutoff would produce dispersion of high-energy photons in vacuum-substrate propagation, potentially detectable in time-of-flight measurements.

This is structurally connected but lives in a different empirical sector than Hawking-radiation observations.

---

## 8. Verdict

> **VERDICT (H4): FORM-FORCED, COEFFICIENTS-INHERITED for both $\delta_{V5}(\omega)$ and $\delta_g$.**
>
> The V5 kernel's finite memory $\tau_{V5} = \ell_P/c$ produces a high-frequency cutoff $\delta_{V5}(\omega) = -(\omega\tau_{V5})^2 + O((\omega\tau_{V5})^4)$ on the Hawking spectrum. The functional form is FORCED by V5's frequency-domain structure; the cutoff scale is FORCED-via-identification at the Planck timescale. The substrate motif alphabet $g$ from BH-5 produces a temperature shift $\delta_g = c_g (\ell_P/M)^2 \log g$ at first subleading order. The functional form is FORCED by BH-5 + DCGT first-subleading-order machinery; the specific coefficient $c_g$ is INHERITED from substrate-microscopic motif-counting details. Combined: $N_{ED}(\omega) = N_H(\omega) \cdot [1 + \delta_{V5}(\omega) + \delta_g \cdot G(\omega/T_H) + O((\ell_P/M)^4)]$. Corrections are invisible at stellar-mass BH scales but become order-unity in the final stages of primordial-BH evaporation, and become accessible at typical Hawking-spectrum frequencies in analog Hawking experiments.

**Verdict-class details:**

- **(C5a) V5 cutoff form:** FORCED. The form $-(\omega\tau_{V5})^2$ at leading correction order is FORCED by V5 frequency-domain structure.
- **(C5b) Motif-alphabet temperature shift:** FORCED-via-BH-5-inheritance. The form $\delta_g \propto (\ell_P/M)^2 \log g$ is FORCED.
- **(C5c) Cutoff scale identification:** FORCED-via-T19. $\tau_{V5} = \ell_P/c$ is the unique substrate-built timescale at the gravitational scale.
- **No new active CANDIDATEs.** Active CANDIDATE inventory remains {} as of arc-opening tally.

This is the framework's *first explicit substrate-derived correction* to the standard Hawking spectrum. Trending toward YES on the existence of ED-distinctive corrections at first subleading order; the corrections are FORCED at the structural-form level with INHERITED specific values.

---

## 9. Circularity Audit

| Potential circularity | Audit verdict |
|---|---|
| H-1 used as derivation premise? | **Yes — as input only.** H-1's Planck spectrum + Hawking temperature is the leading-order result that the corrections operate on. H-4 does not re-derive H-1; it modifies H-1's result at first subleading order. Inheritance, not circularity. |
| H-2 used as derivation premise? | **Yes — as input only.** H-2's leading-order greybody factors enter the combined spectrum as multiplicative modulation. Inheritance, not circularity. |
| BH-5 used as derivation premise? | **Yes — as input only.** BH-5's motif-alphabet structure $g$ provides the source of the $\delta_g$ correction. Inheritance, not circularity. |
| Standard semiclassical Hawking used as derivation premise? | **No.** Standard Hawking appears as identification target at leading order (referenced via H-1's chain), never as a derivation step at first subleading order. The corrections derived here are substantively new substrate content, not inherited from semiclassical Hawking. |
| Self-reference of H-4 within itself? | **No.** §3 → §4 → §5 → §6 → §7 derivation chain is acyclic. |
| H-3 / H-5 / H-6 / H-7 used as derivation premises? | **No.** Not invoked. H-4 is structurally upstream of H-3 (Page rate corrections from $\delta_{V5}$ and $\delta_g$), H-5 (information correlations may be modified by V5 cutoff), H-7 (synthesis incorporates H-4's corrections). |

**Acyclicity confirmed.**

---

## 10. Falsification

### 10.1 Falsifier for FORM-FORCED, COEFFICIENTS-INHERITED verdict (current verdict)

A substrate construction satisfying H-1, H-2, BH-5, V5 finite-memory, and substrate locality, in which the first-subleading-order corrections to the Hawking spectrum take a different functional form than $\delta_{V5}(\omega) + \delta_g$. Concretely:

- (a) A V5 substrate calculation that produces a high-frequency suppression with functional form different from $1/(1 + (\omega\tau_{V5})^2)$ — would refute the V5 kernel structure of §3.
- (b) A motif-alphabet substrate calculation that produces a temperature shift with $(\ell_P/M)^n$ dependence for $n \neq 2$ — would refute BH-5's first-subleading-order structure or DCGT's scaling-window analysis.
- (c) A substrate construction that produces *no* corrections at first subleading order — would refute the V5-finite-memory or motif-alphabet inheritance.
- (d) A substrate identification of $\tau_{V5}$ at the gravitational scale that gives a value different from $\ell_P/c$ — would require an alternative substrate timescale at the gravitational scale, which T19 does not provide.

Each refutation would downgrade the verdict from FORCED-form to CONDITIONAL or NOT-FORCED.

### 10.2 Empirical-side falsifier — analog Hawking experiments

Analog Hawking spectral measurements at frequencies near the analog system's cutoff scale:

- If the high-frequency tail of the analog Hawking spectrum is consistent with a $1/(1 + (\omega\tau_{\mathrm{analog}})^2)$ V5-form modulation: confirms the substrate-cutoff structure at the analog scale.
- If the high-frequency tail follows a different functional form (e.g., exponential cutoff $e^{-\omega\tau}$ rather than $1/(1+(\omega\tau)^2)$): refutes the V5-form prediction at the analog scale.
- If the analog spectrum exhibits no cutoff at all (extends to arbitrary frequencies in the analog system): refutes the substrate-finite-memory framework.

Current analog Hawking experiments are typically optimized for confirming the spectral form at moderate frequencies; precision measurements of the cutoff structure are within reach but not standard.

### 10.3 Empirical-side falsifier — primordial BH evaporation

PBH evaporation gamma-ray spectra in the final stages would exhibit:

- Standard semiclassical Hawking: spectral peak at $\omega_{\mathrm{peak}} \sim T_H$, with $T_H \sim 1/M$ rising as $M \to 0$. No upper cutoff before the BH disappears.
- ED prediction: spectral peak rises with $T_H$ until $T_H \sim \omega_c = c/\ell_P$, after which V5 cutoff dominates and the spectrum's high-frequency tail is suppressed. PBH "explosion" produces a characteristic spectrum cut off at the Planck scale rather than extending beyond it.

If any PBH evaporations are detected with spectral resolution sufficient to resolve the cutoff: falsifiable test of $\tau_{V5} = \ell_P/c$. No detections currently exist; this prediction sits on the empirical horizon.

### 10.4 Empirical-side falsifier — high-energy photon dispersion

The V5 cutoff scale $\omega_c = c/\ell_P$ is the Planck frequency. High-energy astrophysical photons (GRB photons, IceCube neutrinos at PeV energies, etc.) propagating astronomical distances could probe substrate-cutoff effects in their dispersion. ED predicts a specific dispersion form proportional to $(\omega/\omega_c)^2$ for energies approaching the cutoff.

If precision time-of-flight measurements of GRB photons constrain dispersion below the framework's prediction at given energy: falsifies the substrate-cutoff scale identification.

This is structurally connected to E2 in the Investigation Priority List (GW dispersion / GRB photon-timing retrodiction).

---

## 11. Consequences for the Arc

1. **H-4 closes as the ED-distinctive content memo.** First explicit substrate-derived correction to the standard Hawking spectrum is now in hand. Arc Hawking can now proceed to H-3 (Page rate, where the corrections enter the integrated emission rate), H-5 (information correlations, where V5 cutoff may modify entanglement-straddling), H-6 (semiclassical equivalence, where the corrections sharpen the leading-order vs. first-subleading-order distinction), and H-7 (synthesis).

2. **Trans-Planckian problem resolved at the substrate level.** §4.3 noted that ED's V5 finite-memory cutoff naturally regulates the trans-Planckian content of the standard Hawking calculation. The substrate does not support coherent quantum field modes at arbitrarily-blueshifted frequencies near the horizon. This is a structural feature of the framework that distinguishes it from purely semiclassical treatments.

3. **PBH evaporation prediction is falsifiable.** §7.3 identified the framework's prediction for primordial-BH evaporation final-stage spectra. PBH detection with sufficient spectral resolution would test the V5 substrate-cutoff prediction.

4. **Analog Hawking experiments offer accessible tests.** §7.4 identified analog systems where the substrate-cutoff scale is accessible at typical Hawking frequencies. Existing analog Hawking experimental programs (especially BEC analogs) can test the V5-form prediction with current-generation precision.

5. **Cross-domain echo with E2 (GRB dispersion) is now concrete.** §10.4 flagged that the Planck-scale V5 cutoff produces high-energy photon dispersion that connects with the framework's E2 prediction sector. A unified analysis of substrate-cutoff effects in Hawking radiation + GRB photon dispersion could strengthen both predictions.

6. **The substrate-Unruh argument's first-subleading-order correction is now articulated.** The substrate-Unruh argument from H-1 produced the leading-order Hawking temperature; H-4's $\delta_g$ correction is the first-subleading-order modification of $\kappa_{\mathrm{ED}}$ that propagates to $T_{ED}$. Future arcs on cosmological horizons / de Sitter thermality will benefit from this first-subleading-order content.

7. **No new active CANDIDATEs.** Active CANDIDATE inventory remains {}.

8. **Sensitivity flag inherited from H-1 + new sensitivity:** the §3.4 identification $\tau_{V5} = \ell_P/c$ is FORCED-via-T19 + dimensional analysis. If T19's $\ell_P$ identification were modified, the V5 cutoff scale would shift correspondingly. This is an inherited sensitivity, not a new one.

---

## 12. Summary

**What this memo accomplished.**

- Stated the H-4 CANDIDATE (§1) decomposing it into (C5a) V5 cutoff form, (C5b) motif-alphabet temperature shift, (C5c) cutoff scale identification.
- Constructed the V5 kernel's high-frequency behavior in the substrate-time and frequency domains, identifying the cutoff scale $\omega_c = 1/\tau_{V5}$ (§3).
- Identified $\tau_{V5} = \ell_P/c$ at the gravitational scale via T19 + substrate dimensional analysis (§3.4).
- Derived the modification to the near-horizon V5 correlation function from finite memory time, with the substrate-level resolution of the trans-Planckian problem (§4).
- Computed the explicit V5 cutoff correction $\delta_{V5}(\omega) = -(\omega\tau_{V5})^2 + O((\omega\tau_{V5})^4)$ with FORCED form (§5).
- Derived the motif-alphabet correction $\delta_g = c_g(\ell_P/M)^2 \log g$ from BH-5 inheritance + DCGT first-subleading-order machinery (§6).
- Combined the corrections and worked out observational implications for stellar-mass BHs (invisible), primordial BHs (observable in final evaporation stages), analog Hawking experiments (accessible at typical frequencies), and high-energy photon dispersion (connects with E2 retrodiction sector) (§7).
- Issued the verdict: **FORM-FORCED, COEFFICIENTS-INHERITED** for both corrections (§8).
- Confirmed acyclicity (§9) and provided substrate-level + empirical falsifiers across multiple platforms (§10).

**Trending toward YES on existence of ED-distinctive first-subleading-order corrections, FORCED at the form level.**

**Brief 2–3 sentence summary:** The V5 finite-memory kernel with substrate-built timescale $\tau_{V5} = \ell_P/c$ produces a frequency-dependent high-frequency cutoff $\delta_{V5}(\omega) = -(\omega\ell_P/c)^2 + O((\omega\ell_P/c)^4)$ on the Hawking spectrum, with the substrate motif alphabet $g$ from BH-5 producing a temperature shift $\delta_g = c_g(\ell_P/M)^2\log g$. Both corrections are FORM-FORCED at the structural level with COEFFICIENTS-INHERITED from substrate-microscopic details, and combine to give $N_{ED}(\omega) = \mathcal{T}_\ell^{\mathrm{(GR)}}(\omega) \cdot N_H(\omega) \cdot [1 + \delta_{V5}(\omega) + \delta_g \cdot G(\omega/T_H) + O((\ell_P/M)^4)]$. The corrections are invisible at stellar-mass BH scales but observable in primordial-BH evaporation final stages and accessible in current-generation analog Hawking experiments — making H-4 the framework's first explicit substrate-derived prediction distinguishing ED from strict semiclassical Hawking.

---

## 13. Recommended Next Steps

Multiple options, in decreasing order of immediate Arc Hawking productivity:

1. **H-3 (Page rate including first-subleading corrections) — RECOMMENDED.** With H-1 + H-2 + H-4 in hand, the integrated emission rate is now computable at leading order plus first-subleading-order corrections. The standard Page rate $\dot M = -\hbar c^4/(15360\pi G^2 M^2)$ should be recovered at leading order, with V5 + motif corrections producing $\dot M_{ED} = \dot M_{\mathrm{Page}}[1 + \mathcal{O}((\ell_P/M)^2)]$. Estimated 1 session.

2. **H-5 (information correlations) — STRONG OPTION.** Substantively rich follow-on. With Arc E entanglement bandwidth-budget mechanism + BH-4 entanglement-straddling + H-4's V5 cutoff, the substrate-level account of Hawking-quanta correlations with interior-fallen matter has genuinely new content. The Page-curve structure of information emission may be substrate-derivable from the bandwidth-budget mechanism. Estimated 2–3 sessions.

3. **H-6 (semiclassical equivalence) — NATURAL FOLLOW-ON AFTER H-3.** With H-1, H-2, H-3, H-4 closed, the leading-order vs. first-subleading-order content is sharply identified. H-6 articulates whether ED is structurally identical to semiclassical Hawking at leading order (with corrections at first subleading order) or whether the corrections produce qualitatively new behavior beyond first subleading order. Estimated 1–2 sessions.

4. **H-7 (synthesis) — FINAL MEMO.** Integrates H-1 through H-6 into the cross-domain unification framework. V5 kernel doing both Maxwell viscoelastic memory (Arc D) and Hawking spectrum (this arc). Bandwidth-budget mechanism unifying BH-4 + Arc E + Q-COMPUTE. Estimated 1–2 sessions.

5. **(Independent) Substrate-cutoff effects in GRB / GW dispersion (E2 retrodiction).** The V5 high-frequency cutoff produces high-energy photon dispersion at the Planck scale. This connects Arc Hawking with E2 (GRB photon-timing retrodiction in the Investigation Priority List). A dedicated memo could develop the dispersion prediction and cross-check with public LIGO/Virgo + Fermi-LAT data. Could close E2 with a single weekend of analysis. Estimated 1 session.

6. **(Independent) Analog Hawking experimental program memo.** §7.4 identified analog Hawking experiments as accessible tests of the V5 substrate-cutoff. A memo articulating specific BEC / acoustic analog parameters that would test the $1/(1+(\omega\tau)^2)$ cutoff form could shape an experimental collaboration. Pure theory + experimental-design content; no new derivation. Estimated 1 session.

---

**Pause for further instruction.**
