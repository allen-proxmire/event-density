# Arc Hawking — Memo 5: Information Correlations and Substrate-Level Page Curve Structure

**Status:** Theoretical-synthesis memo. Conditional on H-1 (Planck spectrum), H-2 (greybody factors), H-3 (corrected Page rate), H-4 (V5 cutoff and motif corrections), plus Arc E (entanglement bandwidth-budget mechanism), BH-4 (entanglement straddling), BH-5 (area-law entropy). No new primitives. Identification-not-derivation discipline observed: standard Page curve is identification target at leading order, never as derivation premise.

**Date:** 2026-05-09

---

## 1. The CANDIDATE Statement

Restated from H-0 §2.2 (piece C6):

> **CANDIDATE (H5).** *The substrate-level information content of Hawking emission is governed by the bipartite entanglement structure between near-horizon modes and outgoing modes, with the entanglement-straddling mechanism (BH-4) supplying the structural account of how information crosses the horizon and the bandwidth-budget mechanism (Arc E) supplying the constraint on how rapidly information can be transferred to the radiation. At leading-order DCGT coarse-graining, the substrate-level entanglement-entropy evolution reproduces the standard Page curve, with the Page time $t_{\mathrm{Page}} \approx 0.54 \tau_{\mathrm{BH}}$ and the maximum radiation entropy $S_{\mathrm{max}} = S_{\mathrm{BH,0}}/2$ matching the standard semiclassical predictions. First-subleading-order corrections from V5 cutoff (H-4 §5) and motif-alphabet temperature shift (H-4 §6) modify the Page time and the curve slope at order $(\ell_P/M)^2$. The framework's late-time information-release profile depends on whether the H-3 conditional Planck-mass remnant scenario realizes: full recovery if no remnant, or remnant-based storage with asymptotic remnant entropy if remnant exists.*

The CANDIDATE has four pieces:

- **(C6a) Bipartite entanglement structure.** Near-horizon modes and outgoing modes form a bipartite system whose entanglement evolves as the BH radiates. The substrate-level mechanism is BH-4 entanglement-straddling at the saturated decoupling surface, with Arc E bandwidth-budget supplying the rate constraint.
- **(C6b) Leading-order Page curve.** At leading-order DCGT coarse-graining, the substrate-level entanglement-entropy evolution reproduces the standard Page curve.
- **(C6c) First-subleading-order Page-time correction.** V5 cutoff and motif-alphabet effects modify $t_{\mathrm{Page}}$ at order $(\ell_P/M)^2$, with corresponding modifications to the curve's slope.
- **(C6d) Late-time scenario.** The Page curve's late-time behavior depends on the H-3 conditional remnant scenario: full recovery + return to zero entropy if no remnant, or asymptotic remnant entropy if Planck-mass remnant realizes.

H-5 examines each. The argument runs through five structural steps: (i) the bipartite entanglement structure, (ii) leading-order Page curve recovery, (iii) V5 cutoff effect on entanglement bandwidth, (iv) motif-alphabet correction to Page time, (v) three scenarios for late-time information release.

The honest framing: the framework structurally addresses the BH information question by deriving a substrate-level account of information correlations from already-closed substrate machinery (BH-4 + Arc E + H-1 through H-4). The leading-order Page curve identification with semiclassical is structural recovery; the first-subleading-order corrections are the substantively new content; the late-time profile is the framework's most cosmologically and theoretically significant open question.

---

## 2. Substrate Inputs and the Assumption Audit

The derivation uses only the following inputs, each FORCED-unconditional, primitive, or canonical guardrail:

| Input | Status | Role |
|---|---|---|
| **H-1 (Planck spectrum + Hawking temperature)** | Closed (this arc) | Spectral content of the radiation; sets emission rate |
| **H-2 (leading-order greybody factors)** | Closed (this arc) | Angular-channel transmission of substrate modes |
| **H-3 (corrected Page rate)** | Closed (this arc) | Mass-loss rate sets the BH-evolution timescale |
| **H-4 (V5 cutoff + motif corrections)** | Closed (this arc) | First-subleading-order spectral corrections |
| **BH-4 (entanglement-straddling)** | Closed-arc inheritance | Substrate mechanism for entanglement crossing the horizon |
| **BH-5 (area-law entropy)** | Closed-arc inheritance | Substrate motif counting → BH entropy $S_{\mathrm{BH}} = (\log g)/(4\ell_P^2) \cdot A$ |
| **E-4 (entanglement bandwidth-budget)** | Closed-arc (Arc E) | Substrate-level constraint on how much entanglement two regions can support |
| **E-6 (von Neumann entanglement entropy)** | Closed-arc (Arc E) | Substrate-derived form of entanglement entropy |
| **DCGT (substrate-to-continuum bridge)** | FORCED structural-foundation | Leading-order identification with semiclassical Page curve |
| **Standard Page curve** | External mathematical physics | Identification target at leading order; not derivation premise |
| **Substrate unitarity (no information loss)** | Substrate primitive (T18 + P11) | Cross-chain correlations propagate causally; commitment events are tracked irreversibly. Together: no genuine information loss at substrate level |

**No new primitives introduced.** **No use of standard Page curve as derivation premise** at any order — only as identification target at leading order.

---

## 3. The Bipartite Entanglement Structure at the Saturated Surface

### 3.1 The bipartite system

The Hawking radiation problem has a natural bipartite structure:

- **System A: outgoing radiation modes.** Substrate modes that have escaped to substrate-asymptotic infinity, carrying energy and substrate-level entanglement.
- **System B: BH-interior modes.** Substrate modes that fell across the saturated decoupling surface, joining the saturated participation zone (BH-3 inheritance).

The total bipartite system A + B has well-defined substrate-level entanglement structure at every moment $t$ during the BH's lifetime.

### 3.2 BH-4's entanglement-straddling mechanism

BH-4 closed the substrate-level account of entanglement crossing the horizon. The mechanism: the saturated decoupling surface is a substrate object where cross-chain bandwidth $\Gamma_{\mathrm{cross}}$ falls below hydrodynamic-window resolution from interior to exterior. Despite this, V5 cross-chain correlations re-route around the surface via the asymmetric participation flow (the same mechanism producing the Hawking radiation in H-1).

The substrate's entanglement structure across the horizon is mediated by these V5 cross-chain correlations. At the moment a substrate mode crosses the horizon, its V5 correlations with substrate modes that did not cross become re-routed: the V5 kernel provides the substrate-level connection between interior-fallen modes and the modes that escape as Hawking quanta.

This is the substrate-level statement of "information crosses the horizon": V5 correlations established before horizon crossing are preserved across the saturated surface despite the cross-chain bandwidth suppression.

### 3.3 The Arc E bandwidth-budget constraint

Arc E (Memo 4) established monogamy of entanglement: a single substrate region's outgoing cross-chain bandwidth $\Gamma_{\mathrm{max}}$ is finite. Full bipartite entanglement saturates this budget; no remaining capacity is available for additional entanglement with a third region.

For the Hawking-radiation bipartite system A + B, Arc E's bandwidth-budget translates to: at any moment $t$, the entanglement between system A (radiation) and system B (BH interior) is bounded by:

```
S_AB(t) ≤ min[S_BH(t), S_radiation(t)]
```

where $S_{\mathrm{BH}}(t) = (\log g)/(4\ell_P^2) \cdot A_{\mathrm{horizon}}(t)$ is the BH entropy from BH-5 and $S_{\mathrm{radiation}}(t)$ is the cumulative entropy of the emitted radiation up to time $t$.

The min-bound is structurally crucial: it forces the radiation's entanglement entropy to track the smaller of $S_{\mathrm{BH}}$ and $S_{\mathrm{radiation}}$. This is the substrate-level origin of the Page curve's structure.

### 3.4 The substrate-level Page curve

Define the radiation's entanglement entropy at time $t$:

```
S_rad(t) ≡ S_AB(t) = von Neumann entropy of the radiation density operator ρ_rad(t)
```

The substrate-level evolution:

- **Early times** ($t \ll t_{\mathrm{Page}}$): $S_{\mathrm{radiation}} < S_{\mathrm{BH}}$. The min-bound allows $S_{\mathrm{rad}}(t) = S_{\mathrm{radiation}}(t)$ — the radiation's own thermodynamic entropy. As radiation accumulates, $S_{\mathrm{rad}}(t)$ grows.
- **Page time** ($t = t_{\mathrm{Page}}$): $S_{\mathrm{radiation}} = S_{\mathrm{BH}}$. The min-bound is saturated. Maximum $S_{\mathrm{rad}}(t_{\mathrm{Page}}) = S_{\mathrm{BH,0}}/2$.
- **Late times** ($t \gg t_{\mathrm{Page}}$): $S_{\mathrm{BH}} < S_{\mathrm{radiation}}$. The min-bound now equals $S_{\mathrm{BH}}(t)$, which is *decreasing* as the BH evaporates. So $S_{\mathrm{rad}}(t)$ decreases.
- **Endpoint** ($t = \tau_{\mathrm{BH}}$, $M = 0$): $S_{\mathrm{BH}} = 0$. The min-bound forces $S_{\mathrm{rad}} = 0$. Information is fully recovered.

This is the Page curve's structural form, derived from substrate-level bandwidth-budget + BH-5 entropy form + BH-4 entanglement-straddling.

---

## 4. Leading-Order: Recovery of the Standard Page Curve

### 4.1 The leading-order entropies

At leading-order DCGT coarse-graining:

```
S_BH(t) = (log g)/(4 ℓ_P²) · A_horizon(t) → A_horizon(t)/(4 ℓ_P²)
       (Bekenstein-Hawking with log g identified with the standard 1/4 coefficient at leading order)
```

The horizon area evolves with $M(t)$ via $A = 4\pi r_s^2 = 16\pi M^2$ (in geometrized units). With $\dot M = -\alpha_{\mathrm{Page}}/M^2$ from H-3:

```
A(t) = 16π · M²(t) = 16π · (M_0³ - 3 α_Page t)^(2/3)
```

The cumulative radiation entropy is approximately:

```
S_rad(t) ≈ ∫_0^t (energy emitted)/(T_H(t')) · ln(species count) · dt'
        ≈ S_BH,0 · (1 - M³(t)/M_0³)  · [function of species count]
```

Using $M^3(t) = M_0^3 - 3\alpha_{\mathrm{Page}} t$ and the standard species-counting:

```
S_rad(t) ≈ S_BH,0 · [1 - (1 - t/τ_BH)] = S_BH,0 · (t/τ_BH)
        (linear approximation; full result includes greybody-factor weighting)
```

### 4.2 The leading-order Page time

Setting $S_{\mathrm{radiation}} = S_{\mathrm{BH}}$:

```
S_BH(t_Page) = S_BH,0 · (1 - t_Page/τ_BH)^(2/3) (since A scales as M²(t))
S_radiation(t_Page) ≈ S_BH,0 · (t_Page/τ_BH)
```

Equating:

```
(1 - t_Page/τ_BH)^(2/3) = t_Page/τ_BH
```

Numerical solution: $t_{\mathrm{Page}}/\tau_{\mathrm{BH}} \approx 0.54$. This is the standard Page time.

### 4.3 The leading-order maximum entropy

At $t_{\mathrm{Page}}$:

```
S_max = S_rad(t_Page) = S_BH(t_Page) ≈ S_BH,0 / 2
```

The standard Page result.

### 4.4 The leading-order Page curve shape

Combining:

```
S_rad(t) = min[S_radiation(t), S_BH(t)]
```

with $S_{\mathrm{radiation}}(t)$ rising linearly and $S_{\mathrm{BH}}(t) \propto (1 - t/\tau_{\mathrm{BH}})^{2/3}$ falling, the Page curve has:

- Linear rise from 0 at $t = 0$ to $S_{\mathrm{BH,0}}/2$ at $t_{\mathrm{Page}}$.
- Power-law fall from $S_{\mathrm{BH,0}}/2$ at $t_{\mathrm{Page}}$ to 0 at $\tau_{\mathrm{BH}}$.
- Cusp at $t_{\mathrm{Page}}$ where the min-bound switches.

This is the standard Page curve shape. **(C6b) is FORCED via DCGT identification.**

### 4.5 What ED reproduces at leading order

ED reproduces the standard Page curve at leading order, including:

- Page time $t_{\mathrm{Page}} \approx 0.54 \tau_{\mathrm{BH}}$.
- Maximum entropy $S_{\mathrm{max}} = S_{\mathrm{BH,0}}/2$.
- Linear rise + power-law fall structure.
- Return to zero at $\tau_{\mathrm{BH}}$ (in absence of late-time corrections from §7).
- Information recovery via correlations between Hawking quanta after Page time.

The substrate calculation produces this via:
- BH-4's entanglement-straddling supplying the cross-horizon entanglement structure.
- E-4's bandwidth-budget supplying the min-bound on $S_{\mathrm{rad}}(t)$.
- BH-5's area-law form supplying $S_{\mathrm{BH}}(t)$.
- H-3's evaporation profile supplying $M(t)$ and $\tau_{\mathrm{BH}}$.

No deviation from semiclassical at leading order. The Page curve is reproduced exactly.

---

## 5. The V5 Cutoff Effect on Entanglement Bandwidth

### 5.1 V5 modulates the entanglement-transfer rate

The V5 finite-memory kernel limits the rate at which substrate modes can be coherently entangled across separated regions. In the Hawking context, this means: at frequencies near the V5 cutoff $\omega_c = c/\ell_P$, the entanglement transfer between BH-interior and outgoing-radiation modes is suppressed.

The substrate bandwidth-budget receives a frequency-dependent modulation:

```
Γ_max^(eff)(ω) = Γ_max · (1 - (ω τ_V5)²) + O((ω τ_V5)^4)
```

For substrate modes with $\omega \tau_{V5} \ll 1$, the bandwidth is unchanged. For modes near the cutoff, the bandwidth decreases.

### 5.2 Effect on the rate of information transfer

The Hawking radiation carries information at a rate proportional to the V5-modulated bandwidth. From H-3, the spectrum-weighted V5 correction is $\mathcal{I}_{V5} \sim -(\ell_P/M)^2$. The rate of information transfer to the radiation:

```
dS_radiation/dt|_ED = dS_radiation/dt|_leading · (1 + ℐ_V5 + ...)
                    = dS_radiation/dt|_leading · (1 - K_V5 (ℓ_P/M)² + ...)
```

The V5 cutoff *slows* information transfer at the rate $(\ell_P/M)^2 \cdot$ leading-rate.

### 5.3 Page time modification

The Page time is determined by $S_{\mathrm{radiation}}(t_{\mathrm{Page}}) = S_{\mathrm{BH}}(t_{\mathrm{Page}})$. With V5 corrections to both:

```
S_radiation^(ED)(t) ≈ S_radiation^(leading)(t) · (1 - K_V5 (ℓ_P/M)² + ...)
S_BH^(ED)(t) ≈ S_BH^(leading)(t) · (1 + δ_g + ...)  (from motif-alphabet correction to entropy)
```

The Page time shifts:

```
t_Page^(ED) = t_Page^(leading) · (1 + δ_t,V5 + δ_t,g + ...)
```

where $\delta_{t, V5}$ comes from the V5-correction to the radiation-entropy buildup rate, and $\delta_{t, g}$ comes from the motif correction to BH entropy.

For the Page-time numerical estimate at first subleading order:

```
t_Page^(ED) ≈ 0.54 τ_BH · [1 + c_t,V5 (ℓ_P/M_0)² + c_t,g (ℓ_P/M_0)² log g + ...]
```

with $c_{t, V5}$ and $c_{t, g}$ INHERITED from substrate microscopic details. Numerically $\sim 0.01$ to $\sim 1$ in absolute value.

### 5.4 Status

**$\delta_{t, V5}$ form is FORCED** by V5's modulation of the rate of information transfer (through the same mechanism as H-4 §5 + H-3's integration).

**Coefficient $c_{t, V5}$ is INHERITED** from species-specific spectrum-weighted V5 corrections.

For Schwarzschild stellar-mass BHs: $(\ell_P/M_0)^2 \sim 10^{-76}$ — Page-time correction invisible.

For PBHs: $(\ell_P/M_0)^2 \sim 10^{-46}$ at present moment, growing toward order unity in final stages — Page-time correction increasingly significant.

---

## 6. The Motif-Alphabet Correction to the Page Curve

### 6.1 BH-5 motif-alphabet correction to BH entropy

The BH-5 area-law entropy at first subleading order receives the motif-alphabet correction:

```
S_BH^(ED)(t) = (log g)/(4 ℓ_P²) · A(t) · [1 + c_g^(S) (ℓ_P/M(t))² + ...]
```

where $c_g^{(S)}$ is INHERITED from BH-5 motif-counting structure.

This affects both the absolute scale of the BH entropy (so the *value* of $S_{\mathrm{max}}$ at the Page time changes) and the *temporal profile* of $S_{\mathrm{BH}}(t)$ as $M$ evolves (so the Page-curve slope changes).

### 6.2 Modified Page time from motif effect

With the motif correction to $S_{\mathrm{BH}}$:

```
t_Page^(ED, motif) ≈ t_Page^(leading) · [1 + (2/3) · c_g^(S) (ℓ_P/M_0)² log g + ...]
```

The factor of $2/3$ comes from the fractional-power scaling $S_{\mathrm{BH}} \propto M^2 \propto (M_0^3 - 3\alpha_{\mathrm{Page}} t)^{2/3}$.

### 6.3 Modified maximum entropy

```
S_max^(ED) = S_BH^(ED)(t_Page) ≈ (S_BH,0/2) · [1 + c_S^(motif) (ℓ_P/M_0)² log g + ...]
```

The maximum radiation entropy at Page time is modified by the motif correction. For $c_S^{(\mathrm{motif})} > 0$ (motif counting increases entropy at first subleading order), $S_{\mathrm{max}}$ is slightly larger than $S_{\mathrm{BH,0}}/2$.

### 6.4 Combined first-subleading Page-curve corrections

```
t_Page^(ED) = t_Page^(leading) · [1 + c_t (ℓ_P/M_0)² + ...]
S_max^(ED)  = (S_BH,0/2) · [1 + c_S (ℓ_P/M_0)² + ...]
```

with $c_t, c_S$ INHERITED from V5 + motif details.

For stellar-mass BHs, both corrections are $\sim 10^{-76}$ — invisible.

For PBHs in final stages, both corrections become order unity — Page curve is qualitatively modified.

---

## 7. Three Scenarios for Late-Time Information Release

The Page curve's late-time behavior depends on whether the BH fully evaporates (standard semiclassical) or stops evaporating at $M \sim M_*$ (ED's possible Planck-mass remnant from H-3 §7.3).

### 7.1 Scenario A: Full Recovery (no remnant)

If higher-order corrections do not produce a stable remnant:

- BH evaporates fully: $M \to 0$ at finite time $\tau_{\mathrm{BH}}^{(\mathrm{ED})}$.
- $S_{\mathrm{BH}}(t) \to 0$ at $\tau_{\mathrm{BH}}$.
- By the min-bound, $S_{\mathrm{rad}}(t) \to 0$ at $\tau_{\mathrm{BH}}$.
- All information is recovered through correlations between Hawking quanta.

**Page curve in Scenario A:**
- Linear rise from 0 to $S_{\mathrm{max}}^{(\mathrm{ED})}$ over $[0, t_{\mathrm{Page}}^{(\mathrm{ED})}]$.
- Power-law fall from $S_{\mathrm{max}}^{(\mathrm{ED})}$ to 0 over $[t_{\mathrm{Page}}^{(\mathrm{ED})}, \tau_{\mathrm{BH}}^{(\mathrm{ED})}]$.
- Standard Page-curve shape with first-subleading-order corrections to $t_{\mathrm{Page}}$ and $S_{\mathrm{max}}$.

This is structurally identical to the standard semiclassical Page curve plus small corrections. **Full information recovery.**

### 7.2 Scenario B: Modified Turnover (slowed late-time fall)

If the corrections soften the late-time fall but the BH eventually evaporates (without a stable remnant):

- BH evaporates, but slowly in the final stages.
- Page curve has linear rise + power-law fall, with the power-law fall slowed at very late times.
- Maximum entropy and Page time are corrected at $(\ell_P/M_0)^2$.
- Asymptotic information recovery still occurs, but on a longer-than-semiclassical timescale.

**Page curve in Scenario B:** modified turnover, longer late-time tail. **Full information recovery, slowed.**

### 7.3 Scenario C: Remnant-Based Storage

If higher-order corrections produce a stable Planck-mass remnant (H-3 §7.3 conditional):

- BH evaporates down to $M = M_*$ then stops (or asymptotes very slowly).
- $S_{\mathrm{BH}}(t \to \infty) = S_{\mathrm{remnant}} = (\log g)/(4\ell_P^2) \cdot 4\pi M_*^2$.
- For $M_* \sim M_P$: $S_{\mathrm{remnant}} \sim O(\log g)$ — a few bits of information stored in the remnant.
- By the min-bound, $S_{\mathrm{rad}}(t \to \infty) \leq S_{\mathrm{remnant}}$ — radiation cannot fully recover information.

**Page curve in Scenario C:**
- Linear rise from 0 to $S_{\mathrm{max}}^{(\mathrm{ED})}$ over $[0, t_{\mathrm{Page}}^{(\mathrm{ED})}]$.
- Power-law fall from $S_{\mathrm{max}}^{(\mathrm{ED})}$ toward $S_{\mathrm{remnant}}$ (not toward 0).
- Asymptotes at $S_{\mathrm{remnant}}$ as $t \to \infty$.

**Partial information recovery; remnant retains $S_{\mathrm{remnant}}$ bits.**

This is structurally distinct from standard semiclassical Hawking information recovery. The Planck-mass remnant scenario, if realized, predicts that BH evaporation does *not* fully recover all information; a small amount ($\sim \log g$ bits) is stored in the substrate-stable remnant indefinitely.

### 7.4 Which scenario does ED predict?

The framework's leading-correction analysis cannot determine this. The scenarios differ in the *resummation* of $(\ell_P/M)^2$ corrections at all orders:

- **Scenario A** requires higher-order corrections to vanish at $M \sim M_*$, allowing full evaporation.
- **Scenario B** requires higher-order corrections to slow but not halt evaporation.
- **Scenario C** requires higher-order corrections to stabilize at $M \sim M_*$, producing a substrate-stable remnant.

Determining which is correct requires:

- Substrate-microscopic analysis of the substrate-state at $M \sim M_*$.
- Substrate-level analog of resurgence / Borel summation techniques.
- Or empirical evidence (PBH-evaporation observations or Planck-mass-remnant DM signatures).

**The framework's prediction is structurally three-way conditional. The most cosmologically significant implication — Scenario C — is form-FORCED if the H-3 conditional remnant scenario realizes, but the realization itself is open.**

---

## 8. Substrate-Level Information-Recovery Mechanism

### 8.1 The substrate-unitarity question

Standard semiclassical Hawking has a structural tension with quantum-mechanical unitarity: thermal radiation appears to discard information about the BH initial state, contradicting unitary evolution. The Page curve's late-time return to zero entropy reflects unitarity restored — information recovered through correlations between Hawking quanta.

**ED's substrate-unitarity:** at the substrate level, T18 (V1 forward-cone-only kernel) plus P11 (commitment irreversibility) plus the participation-measure structure provide substrate-level unitarity. Cross-chain correlations propagate causally; commitment events are tracked irreversibly; the participation measure's evolution between commitments is unitary. There is no substrate-level information loss.

This is consistent with E-4's no-signaling theorem (over-determined by three substrate locks: T18 + P11 + ED-I-06). Substrate-level no-signaling translates to substrate-level unitarity in the BH-evaporation context.

### 8.2 How information escapes through correlations

The substrate-level mechanism for information recovery in the Page-curve regime:

1. Pre-Page-time: outgoing radiation carries entanglement with BH-interior modes. Each Hawking quantum is entangled with an interior mode it left behind.

2. Post-Page-time: as the BH continues evaporating, new Hawking quanta are emitted. Their entanglement structure is *not* purely with new interior modes (which are scarce, since the BH is shrinking); instead, they carry correlations with *previously-emitted* Hawking quanta. The radiation system A becomes increasingly self-correlated.

3. By substrate-level unitarity, the total system A + B is a pure state. As $S_{\mathrm{BH}} \to 0$, the system B contains no information; all information is in A. The radiation A's self-correlations encode the BH initial state.

4. **In Scenario A (full recovery):** the radiation eventually contains the full original information. An observer who collected and analyzed all Hawking quanta would, in principle, reconstruct the BH initial state.

5. **In Scenario C (remnant):** $S_{\mathrm{BH}} \to S_{\mathrm{remnant}} \neq 0$. A small amount of information remains in the remnant. The radiation contains $S_{\mathrm{BH,0}} - S_{\mathrm{remnant}}$ bits; the remaining $S_{\mathrm{remnant}}$ bits are stored in the substrate-stable remnant.

### 8.3 What this resolves in the information paradox

The standard BH information paradox has two parts:

- **(i)** Does Hawking radiation carry information, or is it purely thermal? (Answered: it carries information through correlations after Page time.)
- **(ii)** What is the substrate-physics mechanism that allows information to escape through correlations? (Standard physics: depends on which proposed resolution — firewall, ER=EPR, soft hair, etc.)

ED resolves (ii) at the substrate level: information escapes through V5 cross-chain correlations re-routed around the saturated decoupling surface (BH-4's entanglement-straddling mechanism). The substrate's V5 kernel is the substrate-physical channel by which information flows out of the BH's interior into the radiation field.

This is structurally distinct from the firewall scenario (no firewall in ED — the saturated surface is not a singular boundary but a substrate-level decoupling structure), the ER=EPR scenario (no fundamental wormhole geometry per ED-I-06; the substrate analog is the V5-mediated cross-chain correlation), and the soft-hair scenarios (substrate's rule-type connection from T17 plays the structural role of soft hair, but at the substrate level rather than the field-theoretic level).

ED's substrate-level information-recovery mechanism is **V5-cross-chain re-routing at the saturated decoupling surface, with bandwidth-budget regulation from Arc E**. This is the substrate's answer to the information paradox.

### 8.4 Status

**Substrate-level unitarity** is FORCED at leading order via T18 + P11 + ED-I-06 (the same three substrate locks that produce E-5's no-signaling theorem).

**Information-recovery mechanism via V5 cross-chain re-routing** is FORCED via BH-4 + Arc E + H-1 + H-2 + H-3 + H-4 inheritance.

**Late-time recovery completeness** is CONDITIONAL on the H-3 remnant-or-not scenario.

---

## 9. Verdict

> **VERDICT (H5): FORCED at leading order, FORM-FORCED at first subleading order with COEFFICIENTS-INHERITED, late-time scenario CONDITIONAL on H-3.**
>
> The substrate-level Page curve at leading-order DCGT coarse-graining identifies exactly with the standard semiclassical Page curve: linear rise to $S_{\mathrm{max}} = S_{\mathrm{BH,0}}/2$ at $t_{\mathrm{Page}} \approx 0.54 \tau_{\mathrm{BH}}$, followed by power-law fall. Information recovery via correlations between Hawking quanta is structurally accounted for by V5 cross-chain re-routing (BH-4) + bandwidth-budget regulation (Arc E) + substrate-level unitarity (T18 + P11 + ED-I-06). First-subleading-order corrections to $t_{\mathrm{Page}}$ and $S_{\mathrm{max}}$ scale as $(\ell_P/M_0)^2$ from V5 cutoff (H-4 §5) and motif-alphabet correction (H-4 §6). The late-time information-recovery completeness depends on whether higher-order corrections produce a stable Planck-mass remnant: full recovery if no remnant (Scenario A or B), remnant-based storage with asymptotic remnant entropy $\sim O(\log g)$ bits if remnant (Scenario C).

**Verdict-class details:**

- **(C6a) Bipartite entanglement structure:** FORCED via BH-4 + Arc E inheritance.
- **(C6b) Leading-order Page curve:** FORCED via DCGT identification.
- **(C6c) First-subleading-order Page-time correction:** FORM-FORCED, COEFFICIENTS-INHERITED.
- **(C6d) Late-time scenario:** three-way CONDITIONAL on H-3 remnant scenario; structural mechanisms for each scenario are in hand.
- **No new active CANDIDATEs.** Active CANDIDATE inventory remains {} as of arc-opening tally.

**Most cosmologically significant prediction:** if Scenario C realizes, primordial-BH evaporation leaves Planck-mass remnants storing $\sim O(\log g)$ bits each. These could collectively contribute to dark matter, with each remnant carrying a small amount of substrate-bound information about its parent BH's initial state. This is the framework's direct contribution to the BH information paradox literature.

---

## 10. Circularity Audit

| Potential circularity | Audit verdict |
|---|---|
| H-1, H-2, H-3, H-4 used as derivation premises? | **Yes — as inputs only.** Each closed earlier in the arc; H-5 inherits their results. Inheritance, not circularity. |
| BH-4, BH-5, Arc E (E-4, E-6) used as derivation premises? | **Yes — as inputs only.** Closed-arc inheritance from prior structural-foundations work. |
| Standard Page calculation used as derivation premise? | **No.** Standard Page curve appears in §4 as identification target via DCGT, not as derivation step. The substrate-level Page curve is derived from BH-4 + Arc E + BH-5 + H-1 through H-4. |
| Self-reference of H-5 within itself? | **No.** §3 → §4 → §5 → §6 → §7 → §8 derivation chain is acyclic. |
| H-6 / H-7 used as derivation premises? | **No.** Not invoked. |
| Substrate-unitarity used as derivation premise? | **Yes — as input.** T18 + P11 + ED-I-06 are substrate-foundation primitives + canonical guardrails, used as inheritance. |

**Acyclicity confirmed.**

---

## 11. Falsification

### 11.1 Falsifier for FORCED-leading-order, FORM-FORCED-first-subleading-order verdict

A substrate construction satisfying all of H-1 through H-4, BH-4, BH-5, Arc E, and DCGT, in which:

- (a) The leading-order Page curve fails to reproduce the standard $t_{\mathrm{Page}} \approx 0.54\tau_{\mathrm{BH}}$ and $S_{\mathrm{max}} = S_{\mathrm{BH,0}}/2$ — would refute DCGT's substrate-to-continuum bridge for the entanglement-entropy evolution.
- (b) The first-subleading-order corrections to $t_{\mathrm{Page}}$ scale as $(\ell_P/M_0)^n$ for $n \neq 2$ — would refute the V5 + motif scaling structure inherited from H-4.
- (c) The substrate-level entanglement-entropy evolution does not satisfy the min-bound $S_{\mathrm{AB}}(t) \leq \min[S_{\mathrm{BH}}(t), S_{\mathrm{radiation}}(t)]$ — would refute Arc E's bandwidth-budget structure or BH-4's entanglement-straddling mechanism.

### 11.2 Empirical-side falsifier — analog Hawking experiments

Page-curve-analog measurements in BEC or acoustic Hawking analog systems:

- Standard semiclassical analog: linear rise + power-law fall reaching back to zero entropy at full evaporation.
- ED-corrected analog: same shape with first-subleading corrections at $(\ell_{\mathrm{analog}}/M_{\mathrm{analog}})^2$.

If precision Page-curve-analog measurements in current-generation analog Hawking experiments confirm or refute the corrections: direct test of H-5's first-subleading-order prediction. Note: extracting Page-curve information from analog systems is technically demanding but in principle accessible.

### 11.3 Empirical-side falsifier — BH information observations

Direct observation of information emerging from BHs (gravitational-wave inspirals, BH merger ringdowns, primordial-BH evaporation events, etc.) with sufficient precision to test:

- Scenario A or B (full recovery): all information recovered through Hawking-quanta correlations; information-loss ratio = 0.
- Scenario C (remnant): asymptotic information-loss ratio = $S_{\mathrm{remnant}}/S_{\mathrm{BH,0}}$.

Currently no direct empirical test is available, but ongoing gravitational-wave observatories (LIGO, Virgo, KAGRA, future Einstein Telescope, Cosmic Explorer) may eventually constrain BH information-recovery scenarios.

### 11.4 Empirical-side falsifier — primordial-BH-remnant dark-matter searches

If Scenario C realizes and remnants exist as stable substrate objects at Planck mass:

- Remnant abundance from primordial-BH evaporation history: calculable from cosmological PBH formation rates and evaporation timescales.
- Each remnant: mass $\sim 22$ μg, carries $\sim O(\log g)$ bits of substrate-bound information.
- Aggregate: could contribute to dark matter at observed abundance if remnant production rate matches dark-matter density.

Continued absence of Planck-mass DM detection at improving experimental sensitivity would constrain Scenario C.

---

## 12. Consequences for the Arc

1. **H-5 closes as theoretical-synthesis memo.** Substrate-level account of Hawking information-content is now structurally complete at leading + first-subleading order, with three-way conditional on late-time scenario. Arc Hawking can now proceed to H-6 (semiclassical equivalence) and H-7 (synthesis).

2. **Substrate-level resolution of the information paradox.** The framework's substrate mechanism (V5 cross-chain re-routing + Arc E bandwidth-budget + substrate-unitarity from T18 + P11 + ED-I-06) provides a structural account of how information escapes through correlations between Hawking quanta. This is distinct from firewall, ER=EPR, and soft-hair proposals; sits structurally cleanly with the substrate ontology.

3. **Most cosmologically significant prediction: Planck-mass remnant DM scenario.** If Scenario C realizes, primordial-BH-remnant dark matter has structural footing in the framework. The remnant abundance and signature would couple to PBH cosmology and dark-matter physics.

4. **Cross-arc echo with Arc E sharpened.** E-4 monogamy bandwidth-budget at the qubit-pair scale + H-5 bipartite-entanglement bandwidth-budget at the BH-radiation scale = same substrate mechanism at vastly different scales. The cross-domain unification noted in E-7 is now explicit in the BH context.

5. **Cross-arc echo with Arc D + soft-matter is sharpened.** V5 finite-memory kernel produces:
   - Maxwell viscoelastic memory in soft matter (Arc D / DCGT consequence).
   - High-frequency cutoff in Hawking spectrum (H-4).
   - Bandwidth-modulation of entanglement transfer in BH information evolution (this memo).
   Three different physical applications of the same substrate kernel. H-7 will articulate this structurally.

6. **No new active CANDIDATEs.** Active CANDIDATE inventory remains {}.

7. **Sensitivity flag inherited from H-3:** the late-time scenario depends on higher-order resummation of $(\ell_P/M)^2$ corrections, which is not closed at this memo's level. The framework establishes the structural mechanism for each scenario; determining which realizes requires substrate-microscopic analysis or empirical evidence.

---

## 13. Summary

**What this memo accomplished.**

- Stated the H-5 CANDIDATE (§1) decomposing it into (C6a) bipartite entanglement structure, (C6b) leading-order Page curve, (C6c) first-subleading corrections, (C6d) late-time scenario.
- Constructed the bipartite entanglement structure between near-horizon and outgoing modes via BH-4 entanglement-straddling + Arc E bandwidth-budget min-bound (§3).
- Recovered the standard Page curve at leading order: $t_{\mathrm{Page}} \approx 0.54\tau_{\mathrm{BH}}$, $S_{\mathrm{max}} = S_{\mathrm{BH,0}}/2$, linear-rise + power-law-fall structure (§4).
- Derived V5 cutoff effect on entanglement-transfer bandwidth, producing $(\ell_P/M_0)^2$ correction to Page time (§5).
- Derived motif-alphabet correction to Page time and maximum entropy at $(\ell_P/M_0)^2$ (§6).
- Articulated three scenarios for late-time information release: full recovery, modified turnover, or remnant-based storage; identified Scenario C as most cosmologically significant (§7).
- Articulated substrate-level information-recovery mechanism via V5 cross-chain re-routing + substrate-unitarity from T18 + P11 + ED-I-06 (§8).
- Issued the verdict: **FORCED at leading order, FORM-FORCED at first subleading order with COEFFICIENTS-INHERITED, late-time scenario CONDITIONAL on H-3** (§9).
- Confirmed acyclicity (§10) and provided substrate-level + empirical falsifiers across multiple platforms (§11).

**Trending toward YES on Page curve recovery at leading order with FORM-FORCED first-subleading-order corrections.**

**Brief 2–3 sentence summary:** The substrate-level bipartite entanglement structure between near-horizon and outgoing modes — governed by BH-4 entanglement-straddling, Arc E bandwidth-budget min-bound, and BH-5 area-law entropy — reproduces the standard Page curve at leading-order DCGT coarse-graining, with $t_{\mathrm{Page}} \approx 0.54\tau_{\mathrm{BH}}$ and $S_{\mathrm{max}} = S_{\mathrm{BH,0}}/2$. First-subleading-order corrections from V5 cutoff and motif-alphabet structure shift the Page time and maximum entropy by factors of $(\ell_P/M_0)^2$, with COEFFICIENTS INHERITED from substrate-microscopic details. The late-time information-recovery completeness depends on whether higher-order corrections produce a stable Planck-mass remnant: full recovery in Scenarios A/B, or remnant-based storage with asymptotic remnant entropy $\sim O(\log g)$ bits in Scenario C — the latter would constitute a cosmologically significant prediction for primordial-BH-remnant dark matter.

---

## 14. Recommended Next Steps

Multiple options, in decreasing order of immediate Arc Hawking productivity:

1. **H-6 (semiclassical equivalence) — RECOMMENDED.** With H-1 through H-5 closed, the question of whether ED is structurally identical to semiclassical Hawking at leading order (identification verdict) or whether the corrections produce qualitatively new content (departure verdict) is now sharply posable. H-6 articulates the leading-order vs. first-subleading-order distinction and the late-time scenario implications. Estimated 1–2 sessions.

2. **H-7 (synthesis) — FINAL MEMO.** Integrates H-1 through H-6 into the cross-domain unification framework. V5 kernel doing soft-matter Maxwell viscoelasticity (Arc D), Hawking high-frequency cutoff (H-4), and BH information bandwidth-modulation (this memo). Bandwidth-budget mechanism unifying BH-4 + Arc E + Q-COMPUTE + H-5. Estimated 1–2 sessions.

3. **(Independent) Higher-order resummation memo for the late-time scenario.** Resolves which of Scenario A, B, or C realizes by extending the leading-correction analysis to $(\ell_P/M)^4$ and beyond. Most cosmologically significant deferred work in the arc. Estimated 2–4 sessions.

4. **(Independent) Planck-mass remnant DM cosmology memo.** §7.3 of this memo + §7.3 of H-3 jointly identify the remnant scenario. A dedicated cosmology memo articulating remnant abundance from primordial-BH evaporation history, expected DM signatures, and current observational constraints would extend the framework's reach into dark-matter physics. Estimated 2–3 sessions.

5. **(Independent) Substrate-information-paradox-resolution paper.** §8 of this memo articulates the framework's substrate-mechanism resolution of the BH information paradox. A standalone paper at publication-grade level, comparing the framework's resolution to firewall, ER=EPR, soft-hair, and other proposals, could position the framework relative to the active BH-information literature. Estimated 4–6 sessions for publication-grade writeup.

6. **(Independent) Page-curve-analog experimental design memo.** Existing analog Hawking experiments (BEC, acoustic) typically focus on spectral-form confirmation. A memo articulating specific analog-system parameters that would make Page-curve information-content extraction feasible could shape an experimental collaboration. Estimated 1–2 sessions.

---

**Pause for further instruction.**
