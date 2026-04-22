# The ED PDE as an Electrical Circuit: RC and RLC Reductions

**Status:** Derivation + scoping pass. No simulation or experiment run.
**Date:** 2026-04-17
**Context:** [theory/PDE.md](../../theory/PDE.md), [papers/Universal_Mobility_Law/](../Universal_Mobility_Law/), [papers/Cluster_Merger_Lag_Evidence/](../Cluster_Merger_Lag_Evidence/)

---

## 0. What this memo does

The canonical ED PDE reduces, in the spatially-uniform limit, to a **two-dimensional linear dynamical system** in (ρ, v). This memo:

1. Derives the RC first-order decay as the limit where the participation channel is absent or instantaneous.
2. Derives the RLC second-order damped-oscillator equation as the full two-channel limit.
3. Exhibits a concrete circuit — capacitor with parallel resistor, in parallel with a series L–R branch — that is *exactly* isomorphic to the ED uniform-limit equations.
4. Produces a mapping table between ED parameters and (L, R, C) values, and identifies the underdamped / critically damped / overdamped regimes in ED parameter space.
5. Sketches a minimal breadboard experiment that tests the coupling structure of the canonical ED PDE.

The RC and RLC correspondences are already noted in [theory/PDE.md §4.2–§4.3](../../theory/PDE.md); this memo makes them quantitatively precise and buildable.

---

## 1. The uniform-limit PDE

Starting from the canonical form

$$
\partial_t \rho = D\bigl[M(\rho)\nabla^2\rho + M'(\rho)|\nabla\rho|^2 - P(\rho)\bigr] + H\,v,
\qquad
\dot v = \frac{1}{\tau}\bigl(\bar F(\rho) - \zeta v\bigr),
$$

impose spatial uniformity (`∇²ρ = 0`, `|∇ρ|² = 0`). The mobility channel drops out entirely because it is divergence-form. What remains is a coupled ODE pair on the shifted variable `y ≡ ρ − ρ*`:

$$
\dot y = -D P_0\, y + H\, v,
\qquad
\dot v = -\frac{\kappa}{\tau}\, y - \frac{\zeta}{\tau}\, v,
$$

where we have linearised the penalty and participation-source terms around equilibrium: `P(ρ) = P₀(ρ − ρ*)` (exact, from the constitutive form) and `F̄(ρ) = −κ(ρ − ρ*)` (leading-order expansion around ρ*). The sign of `κ` is chosen so that the participation channel provides *restoring* coupling — this is the convention under which [theory/PDE.md §4.3](../../theory/PDE.md) reports the decoupled form `τv̈ + ζv̇ + v = 0`. Opposite-sign κ gives instability rather than oscillation.

The system in matrix form:

$$
\begin{pmatrix}\dot y \\ \dot v\end{pmatrix}
=
\underbrace{\begin{pmatrix} -D P_0 & H \\ -\kappa/\tau & -\zeta/\tau \end{pmatrix}}_{A}
\begin{pmatrix}y \\ v\end{pmatrix}.
$$

Eigenvalues of A satisfy `λ² + tr(A)|_{-} λ + det(A) = 0`:

$$
\lambda^2 + \Bigl(DP_0 + \tfrac{\zeta}{\tau}\Bigr)\lambda + \frac{DP_0\,\zeta + H\kappa}{\tau} = 0. \tag{★}
$$

Equation (★) is a second-order linear ODE in disguise. It is the master equation of this memo.

---

## 2. The RC limit

**Condition.** Either (a) the participation channel is absent (`H = 0` or `κ = 0`), or (b) the participation channel equilibrates instantaneously (`τ → 0` at fixed `ζ/τ` finite). Physically, (a) means no global feedback; (b) means v tracks its source with negligible lag.

In either case, the system collapses to

$$
\dot y = -D P_0\, y \quad\Longrightarrow\quad y(t) = y_0\, e^{-DP_0\, t},
$$

so

$$
\boxed{\;\; \rho(t) = \rho^\ast + (\rho_0 - \rho^\ast)\, e^{-DP_0\, t} \;\;}
$$

This is the Debye / RC exponential decay with time constant

$$
\tau_{\rm RC}^{(\rm ED)} = \frac{1}{DP_0}.
$$

**Direct circuit mapping.** For an RC circuit with a charged capacitor discharging through a resistor, `V(t) = V_0 e^{-t/RC}`. Matching:

$$
\boxed{\;\; DP_0 \;\longleftrightarrow\; \frac{1}{RC} \;\;}
$$

- `y = ρ − ρ*` corresponds to `V` (voltage relative to equilibrium).
- The product `D · P₀` is the only ED combination that appears; individual factors of D and P₀ are not separately observable in this limit. This matches the dimensional identity `D · T₀ / L₀² = D_nd` from [theory/PDE.md §6](../../theory/PDE.md): in the uniform limit, only the time-scale combination survives.
- Any breadboard RC circuit is a valid realisation of ED in this limit. The match is exact, not approximate.

---

## 3. The RLC limit (full two-channel)

Return to equation (★). This is already a second-order characteristic polynomial. To get the second-order ODE explicitly, differentiate the first ED equation:

$$
\ddot y = -DP_0\, \dot y + H\, \dot v.
$$

Substitute `v = (ẏ + DP₀ y)/H` (from the first equation) into `v̇` from the second:

$$
H\,\dot v = -\frac{H\kappa}{\tau}\, y - \frac{\zeta}{\tau}\bigl(\dot y + DP_0\, y\bigr).
$$

So

$$
\ddot y + \Bigl(DP_0 + \tfrac{\zeta}{\tau}\Bigr)\dot y + \frac{DP_0\,\zeta + H\kappa}{\tau}\, y \;=\; 0. \tag{★★}
$$

Equation (★★) is a **damped harmonic oscillator**. Standard form: `ÿ + 2γẏ + ω₀² y = 0`, with

$$
2\gamma \;=\; DP_0 + \frac{\zeta}{\tau},
\qquad
\omega_0^2 \;=\; \frac{DP_0\,\zeta + H\kappa}{\tau}.
$$

### 3.1 Regime classification

The discriminant is `Δ = γ² − ω₀²`:

$$
\Delta \;=\; \frac{1}{4}\Bigl(DP_0 - \tfrac{\zeta}{\tau}\Bigr)^{2} \;-\; \frac{H\kappa}{\tau}.
$$

| Regime | Condition | Behaviour |
|---|---|---|
| **Underdamped** | `Δ < 0`, i.e. `Hκ/τ > (DP₀ − ζ/τ)²/4` | Decaying sinusoid; participation feedback large enough to overcome mismatch between the two decay rates. Damped frequency `ω_d = √(ω₀² − γ²)`. |
| **Critically damped** | `Δ = 0` | Fastest non-oscillatory return to equilibrium. |
| **Overdamped** | `Δ > 0` | Two real exponentials, essentially two uncoupled RC decays. Recovered in particular whenever `Hκ = 0` (participation off). |

The underdamped regime **requires nonzero coupling H·κ** between the ρ channel and the participation channel. In the fully-decoupled limit (H = 0 or κ = 0) ED is always overdamped in the uniform slice. **Oscillations are a feature of channel coupling, not of any single channel in isolation.**

### 3.2 The exact circuit isomorphism

The ED uniform-limit 2D system maps onto a **parallel RLC + parallel-R** circuit — a capacitor `C` with a resistor `R_P` directly across it, the whole in parallel with a series L–R_L branch. Let `V(t)` be the voltage on C and `i(t)` the current in the L branch (positive into L from the top node). Kirchhoff gives

$$
C\dot V + \frac{V}{R_P} + i = 0,
\qquad
L\dot i + R_L\, i = V,
$$

which rearranges to

$$
\begin{pmatrix}\dot V \\ \dot i\end{pmatrix}
=
\begin{pmatrix} -\frac{1}{R_P C} & -\frac{1}{C} \\[2pt] \frac{1}{L} & -\frac{R_L}{L} \end{pmatrix}
\begin{pmatrix} V \\ i \end{pmatrix}.
$$

Comparing term-by-term with the ED matrix `A`:

$$
\boxed{\;\;
\begin{array}{c|c}
\text{ED parameter} & \text{Circuit parameter} \\ \hline
D P_0 & 1/(R_P C) \\
H & -1/C \\
\kappa/\tau & 1/L \\
\zeta/\tau & R_L / L
\end{array}
\;\;}
$$

Equivalently, solving for circuit values in terms of ED parameters (absorbing `κ` into the definition of `L` by setting a unit `κ = 1`):

$$
L = \frac{\tau}{\kappa},
\qquad
R_L = \frac{\zeta}{\kappa},
\qquad
C = \frac{1}{|H|},
\qquad
R_P = \frac{1}{D P_0\, C} = \frac{|H|}{D P_0}.
$$

The sign of `H` (and the direction convention of `i` vs `v`) is absorbed into the choice of which node in the circuit is called "positive". Every ED uniform-limit trajectory is reproduced by a specific choice of (L, R_L, C, R_P), and vice versa.

---

## 4. Physical interpretation

| ED concept | Circuit realisation | Why |
|---|---|---|
| **Equilibrium density ρ\*** | Zero voltage across C | The attractor of the penalty channel corresponds to the discharged capacitor. |
| **Offset y = ρ − ρ\*** | Capacitor voltage V | The displacement from equilibrium. |
| **Participation v** | Current i in the L branch | Global state variable with its own first-order relaxation τ, like current in an inductor with characteristic L/R_L decay. |
| **Penalty channel P(ρ) with strength D P₀** | Parallel resistor R_P across C | Directly dissipates the displacement; no channel to store it. |
| **Participation inertia τ** | Inductance L | Resistance to rapid change in v (i) — the "memory" of the global feedback. |
| **Participation drag ζ** | Series resistance R_L on the L branch | Dissipates participation energy. |
| **Channel coupling H · κ** | 1/(LC) — the LC resonance frequency squared | The strength with which v feeds back into ρ and vice versa. Without coupling, no oscillation. |

The architectural reading is clean: the penalty channel is a **pure dissipator** (resistor), the participation channel is a **stored-momentum element with its own dissipator** (inductor + series resistor), and the capacitor is the thing they both act on.

The canonical ED PDE is therefore — in its uniform-limit, linear-constitutive-function reduction — **the most general 2-element second-order linear circuit**. Any circuit obeying Kirchhoff's laws with one storage element per channel plus channel-specific dissipation maps onto it with the table above.

---

## 5. Minimal breadboard experimental design

### 5.1 Component values (order-of-magnitude)

For a test that runs comfortably on a student-grade oscilloscope (10 MHz bandwidth, 1 mV resolution):

| Element | Value | Rationale |
|---|---|---|
| C | 1 µF (film capacitor) | Large enough to see on scope, small enough for good ripple response |
| L | 10 mH (iron-core inductor) | LC resonance at `ω₀ = 1/√LC ≈ 10⁴ rad/s` → frequency ~1.6 kHz, audible range |
| R_L | 10 Ω – 1 kΩ (varied across runs) | Spans underdamped → overdamped |
| R_P | 1 kΩ – 1 MΩ (varied across runs) | Spans strong to negligible penalty coupling |

Initial conditions set by a 5 V pulse from a function generator, either charging C to 5 V (measures penalty decay + participation response) or driving an initial `i` through L (measures participation decay + penalty response).

### 5.2 What to measure

1. **Voltage across C**, V(t), sampled at 1 MS/s or faster.
2. **Current in the L branch**, i(t), inferred from voltage across a small sense resistor (say 1 Ω) in series with L and R_L. Optional — V(t) alone is sufficient to fit all four parameters.

### 5.3 The four canonical runs

Each run fixes component values so that a specific ED regime is tested.

| Run | Design | ED interpretation | Expected V(t) |
|---|---|---|---|
| **A — Pure RC** | L branch open (remove L–R_L) | Penalty channel only, no participation | Single exponential decay, τ_RC = R_P · C |
| **B — Pure LR** | R_P removed | Participation channel only, no penalty | Capacitor discharges through L–R_L at frequency `1/√LC`, damping `R_L/(2L)` |
| **C — Overdamped RLC** | R_L large (e.g. 1 kΩ), R_P large | Strong participation drag, weak coupling | Double-exponential, no oscillation |
| **D — Underdamped RLC** | R_L small (e.g. 10 Ω), R_P moderate | Weak drag, strong coupling, oscillatory | Decaying sinusoid at `ω_d = √(ω₀² − γ²)` |

For each run, fit V(t) to the analytic form (single exponential, sum of two exponentials, or damped sinusoid). Extract (γ, ω₀) or equivalent.

### 5.4 The consistency test

The four runs are not independent — they all share the same underlying ED parameter set `(D P₀, H, κ, τ, ζ)`. Specifically:

- Run A measures `1/(R_P C)` → `D P₀` (once `C` and `R_P` are known from the components).
- Run B measures `R_L/L` and `1/√(LC)` → `ζ/τ` and `√(Hκ/τ)`.
- Run C measures the sum `DP₀ + ζ/τ` and product-like `(DP₀ζ + Hκ)/τ`.
- Run D measures `γ = (DP₀ + ζ/τ)/2` and `ω_d = √((DP₀ζ + Hκ)/τ − γ²)`.

The constraint is: **the four ED parameters extracted from Runs A and B should predict the exact V(t) observed in Runs C and D**, with no free adjustment.

If they do, the uniform-limit coupling structure of the canonical ED PDE is verified to the precision of the oscilloscope (~10⁻³). If they don't, one of the following is implicated:

- The linearization `P(ρ) = P₀(ρ−ρ*)` and `F̄(ρ) = −κ(ρ−ρ*)` is inadequate at small displacements (unlikely — these are exact by construction for the canonical form).
- The coupling between the two channels has additional structure not captured in the `H v` and `F̄(ρ)/τ` terms.
- The participation ODE needs a higher-order time derivative (i.e., τ is not a single timescale).

### 5.5 Cost and timeline

- Components: < $50 total (film capacitors and iron-core inductors are cheap).
- Breadboard + oscilloscope: ~$300 entry level; may already be available.
- Time to complete all four runs, fit the data, and write up: one afternoon for someone competent with a breadboard; two afternoons for a careful newcomer.

---

## 6. What this test confirms or falsifies

### 6.1 What a positive result would add

The empirical footprint of ED would expand to:

| Channel tested | Realm | Cost |
|---|---|---|
| Mobility (done) | Soft-matter concentration dynamics | Months of chemistry |
| Penalty + source coupling (done) | Cluster-merger wake | Large surveys, years |
| Penalty + participation coupling (RLC) | Electronic circuit — this memo | One afternoon |
| Participation channel isolation (pending) | FRAP fluorescence recovery | Creative Proteomics quote |
| Activity signature (pending) | BIG-SPARC galaxy rotation | Awaits catalog release |

The RLC test **cannot replace** the astronomy tests because it doesn't exercise spatial dynamics. It *does* exercise the two non-spatial channels in precisely the coupled form that matters for the full PDE — and it does so at benchtop precision. It is a **consistency check on the canonical PDE's coupling architecture** at a level of precision unavailable in any other regime.

### 6.2 What a null would mean

If the four-run consistency test fails by more than the measurement uncertainty:

- **First check:** are your L and C values accurate? Inductors in particular have poor tolerances (10–20%) and frequency-dependent series resistance. Use a bridge or impedance meter before drawing conclusions.
- **Second check:** are the nonlinearities in the components (ferrite-core saturation, electrolytic leakage) larger than the ED predicted signal? Use film capacitors and air-core or toroidal iron-core inductors to suppress this.
- **Third, genuine-physics check:** if the components are known to 1% and the predicted V(t) deviates from observed V(t) by more than 1%, the ED PDE's linear uniform-limit reduction is wrong. This is a *real* falsification of the canonical form — not of the whole framework (the canonical form might still hold with modifications), but of the specific linear coupling `Hv` and `F̄/τ` terms that appear in [theory/PDE.md §1](../../theory/PDE.md).

Either outcome is informative. A positive result adds a high-precision consistency check to the empirical suite. A null result localises a methodological or constitutive problem to the linear-coupling structure.

### 6.3 What this test does *not* do

- It does not test the mobility channel (no spatial variation).
- It does not test the nonlinear constitutive forms `M(ρ) = M₀(ρ_max − ρ)^β` (they don't appear in the uniform limit).
- It does not determine `D`, `P₀`, `κ`, `H`, `τ`, `ζ` separately — only the combinations that appear in the 2×2 matrix A.
- It does not confirm ED's uniqueness-theorem derivation — that is a mathematical result, not an empirical one.

These are limitations of what "uniform-limit electrical analogue" means. They are not defects of the test. The point is to verify a piece of the PDE structure, not to overdetermine the full system.

---

## 7. Next steps

1. **Numerical verification (before lab).** Integrate the ED uniform-limit ODE pair (eq. ★) with a chosen parameter set, and integrate the corresponding RLC circuit equations, and confirm the trajectories match to machine precision. This validates the mapping table in §3.2 before any soldering. Can be done in `analysis/notebooks/` as a short companion to the existing `02_three_channels.ipynb`.
2. **Circuit build + measurement.** Source components, build the four configurations of §5.3, capture V(t) in each, fit parameters, check consistency.
3. **Short write-up.** If the test passes (or fails) cleanly, a 2–3 page follow-up memo here replaces this scoping document. If the test surfaces unexpected structure, it becomes a full investigation.
4. **Extensions if desired.** Driven response (add a sinusoidal source), frequency-domain sweep, noise characterisation. None of these are required for the basic consistency check.

---

*This memo is a derivation and scoping pass only; no numerical simulation or laboratory experiment has been performed.*
