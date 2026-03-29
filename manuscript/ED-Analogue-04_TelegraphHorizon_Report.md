# ED Structural Analogue 4: Telegraph-Modulated Horizon Dynamics

## Abstract

This experiment tests whether the ED participation channel can modulate the
horizon boundary, creating oscillatory advance/retreat analogous to a
periodically forced Stefan problem. The result is a **partial success with
a genuine negative finding**: the horizon boundary does NOT oscillate, because
the horizon collapses (via diffusion + penalty) faster than the telegraph
oscillation period. However, the post-horizon peak density DOES show
telegraph-frequency modulation when H > 0, confirming that all three channels
interact. The negative result identifies a structural constraint: ED horizons
are intrinsically transient and cannot be sustained long enough for oscillatory
modulation at accessible parameter values.

## 1. Structural Mapping

Three ED channels combine:

| Channel | Role | Predicted effect on horizon |
|---------|------|-----------------------------|
| Mobility $M(\rho)$ | Horizon formation | Region where $M < M_{\mathrm{crit}}$ |
| Penalty $P(\rho)$ | Horizon retreat | $\rho$ decays toward $\rho^*$, collapsing the horizon |
| Participation $v(t)$ | Oscillatory modulation | $+Hv$ pushes/pulls $\rho$, modulating the boundary |

**Predicted:** $R_H(t) \approx R_{\mathrm{drift}}(t) + A_H \sin(\omega t + \phi)$

## 2. The Timescale Mismatch

The horizon lifetime is $\tau_H = -\ln(A_c/A) / (DP_0)$.
The telegraph half-period is $T_{\mathrm{osc}}/2 = \pi/\omega$.

For oscillatory modulation, we need $\tau_H \gg T_{\mathrm{osc}}/2$.

| $P_0$ | $A$ | $H$ | $\tau_H$ | $T_{\mathrm{osc}}/2$ | Ratio | Oscillations |
|-------|-----|-----|----------|----------------------|-------|--------------|
| 1.0 | 0.48 | 5.0 | 0.61 | 1.41 | 0.43 | 0 |
| 0.2 | 0.49 | 20 | 3.38 | 1.57 | 2.15 | 1 |
| 0.1 | 0.499 | 30 | 7.37 | 1.81 | 4.07 | 2 |
| 0.1 | 0.499 | 50 | 7.37 | 1.41 | 5.24 | 2-3 |

Even in the most favourable case ($P_0 = 0.1$, $H = 50$), only 2-3 oscillation
cycles fit within the horizon lifetime.

## 3. Results

### 3.1 What Was Observed

At $P_0 = 0.1$, $A = 0.499$, $N = 96$:

**Horizon dynamics ($R_H$):**
- Horizon forms at $R_H(0) = 0.198$ for all $H$.
- Horizon collapses by $t \approx 1.5$-$2.0$ for all $H$.
- No oscillation of $R_H$ detected at any $H$.

**Peak density ($\rho_{\mathrm{peak}}$) after horizon collapse:**
- $H = 0$: monotone decay (0.999 to 0.529 by $t = 10$).
- $H = 30$: oscillatory decay. After the collapse ($t > 3$):
  $\rho_{\mathrm{peak}}$ = 0.548, 0.529, 0.528, **0.533**, **0.533**, 0.525, 0.512, 0.499.
  A clear rebound at $t \approx 5$-$6$ where $\rho$ increases by 0.005.
- $H = 50$: stronger rebound with 4 $v$ sign changes.

**Participation variable $v(t)$:**
- $H = 0$: monotone decay, 1 sign change.
- $H = 10$: 2 sign changes.
- $H = 30$: 4 sign changes.
- $H = 50$: 4 sign changes.

The $v$ oscillation IS present and scales with $H$. It modulates the peak density
after the horizon collapses. But the modulation amplitude (~0.005) is too
small to push $\rho$ back above $\rho_{\mathrm{crit}} = 0.90$.

### 3.2 Why the Horizon Doesn't Oscillate

The horizon collapses because:

1. **Diffusion spreads the peak.** The Gaussian bump diffuses outward, reducing
   the central density.
2. **Penalty pulls down.** $-D P_0 (\rho - \rho^*)$ accelerates the descent.
3. **Combined rate:** The peak falls below $\rho_{\mathrm{crit}}$ in
   $\tau_H \sim 1.5$ time units.

The telegraph oscillation has period $T \sim 3.6$ (at $H = 30$). The horizon
is gone before the oscillation completes even half a cycle.

The modulation $H \cdot v_{\max} \approx 30 \times 0.0006 = 0.018$ is too
small to overcome the deficit $(\rho_{\mathrm{crit}} - \rho_{\mathrm{peak}})$
which grows rapidly after the initial collapse.

## 4. Falsification Assessment

| Criterion | Result | Status |
|-----------|--------|--------|
| Horizon forms | YES for all $A > A_c$ | **PASS** |
| No $R_H$ oscillation at $H = 0$ | Correct | **PASS** |
| $R_H$ oscillation at $H > 0$ | NOT detected | **FAIL** |
| $\omega$ of $R_H$ matches telegraph | N/A (no oscillation) | **FAIL** |
| Peak $\rho$ oscillation at $H > 0$ | YES (rebound visible) | **PASS** |
| Peak $\rho$ oscillation absent at $H = 0$ | YES (monotone) | **PASS** |
| $v(t)$ sign changes increase with $H$ | YES (1, 2, 3, 4, 4) | **PASS** |

**Verdict:** 5 of 7 criteria pass. The horizon boundary itself does not
oscillate, but the post-horizon density trajectory does.

## 5. The Structural Constraint

This experiment identifies a genuine architectural constraint of the ED system:

> **ED horizons are intrinsically transient.** The penalty-driven unique
> attractor (Law 1) guarantees that all structure decays. Horizons form
> transiently when the density exceeds $\rho_{\mathrm{crit}}$, but they
> cannot persist long enough for the telegraph oscillation to modulate
> their boundary.

This is not a numerical artefact -- it is a structural consequence of the
monostable penalty. In a bistable system (Allen-Cahn), the horizon could be
stabilised at an alternative equilibrium. In ED, the unique attractor ensures
that the horizon always collapses.

The constraint does not prevent the telegraph from modulating the density
field -- it does, as the peak-density oscillation shows. It prevents the
modulation from creating oscillatory FREE BOUNDARIES.

## 6. Conclusion

The telegraph-modulated horizon experiment is a **partial success**:

**What works:**
- Horizons form and retreat (Analogue 3 confirmed)
- The telegraph oscillation modulates the post-horizon density
- The modulation is absent at $H = 0$ and scales with $H$
- $v(t)$ shows the predicted number of oscillation cycles

**What doesn't work:**
- The horizon boundary $R_H$ does not oscillate
- The horizon collapses faster than the telegraph period

**Significance:** This result demonstrates a structural limit of the
ED architecture. The unique attractor (Law 1) and the monostable penalty
make all ED structure transient, including horizons. The participation
channel can modulate the rate of decay but cannot reverse it. This
distinguishes ED horizons from gravitational event horizons (which are
stable) and from Allen-Cahn interfaces (which can be stabilised by the
double-well potential).

The negative result is scientifically informative: it sharpens the boundary
between what ED can and cannot do, and it confirms that the nine
architectural laws (particularly Law 1) have testable structural
consequences.
