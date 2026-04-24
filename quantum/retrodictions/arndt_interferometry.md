# Arndt Matter-Wave Interferometry — Retrodiction Problem Specification

**Status:** **Problem-specification scaffold, not a retrodiction.** 2026-04-24.
**Author:** Allen Proxmire (program); drafted by Claude as a scaffolded task memo.
**Location:** `quantum/retrodictions/arndt_interferometry.md`

**This document does not compute a retrodiction. It specifies what a retrodiction would require, what is currently missing, and what concrete derivation steps would turn this scaffold into a real retrodiction. It exists so the task is legible and can be executed — by Allen, by a collaborator, or by a future session — without confabulation.**

---

## 1. The target claim

The Q-C Boundary paper asserts a quantitative prediction that is supposed to distinguish ED from standard decoherence theory and from dynamical-collapse models (GRW / CSL / Diósi-Penrose):

> **A matter-wave interferometry system exhibits a sharp quantum-to-classical transition at a specific value of an experimental control parameter `x`, predicted by the condition `D(x_c) = D_crit`, with ED's effective channel weight `D(x)` computed from the Dimensional Atlas and the control parameter fixed by the experiment.**

In the Arndt molecular-interferometry setting, the natural control parameters are (combinations of):

- Molecular mass `m`
- Mean velocity / de Broglie wavelength `λ_dB = h / (m v)`
- Internal vibrational temperature `T_int`
- Residual gas pressure / environmental collision rate `γ_env`
- Source-to-grating and grating-to-detector distances `L_1, L_2`
- Grating period `d_g`

Arndt's published datasets (Talbot-Lau, KDTLI, OTIMA, LUMI classes of interferometer) report **fringe visibility `V`** as a function of one or more of these control parameters, with classical (zero-visibility) behaviour recovered at large `m`, high `T_int`, high `γ_env`, etc. The "transition" for retrodiction purposes is the control-parameter value `x_c` at which `V(x)` crosses some operational threshold — typically halfway between the coherent bound and the classical floor.

The retrodiction, if it can be produced, is:

> *Using the Dimensional Atlas and the canonical ED PDE parameters, with no free parameters fit to Arndt's data, `D(x_c)` evaluated at Arndt's measured transition equals `D_crit` within tolerance.*

## 2. What is currently in place

**Canonical ED PDE (coupled two-channel).** `∂_t ρ = D·F[ρ] + H·v`; `∂_t v = (F[ρ] − ζv)/τ`; `D + H = 1`. Source: ED-Phys-16/17, 00.3, [D_crit_Resolution_Memo.md](../../theory/D_crit_Resolution_Memo.md).

**Dimensional Atlas, quantum regime.** Source: [ED-Dimensional-01_Quantum_Regime.md](../../papers/Dimensional_Atlas/regimes/ED-Dimensional-01_Quantum_Regime.md). Anchoring:

- Length: `L_0 = ℏ/(mc)` (reduced Compton wavelength)
- Diffusivity: `D_phys = ℏ/(2m)` (Madelung theorem — exact)
- Time: `T_0 = 2 D_nd ℏ/(mc²)`
- Density: `R_0 = L_0^{−d}`

**Linear-stability D_crit result.** From the D_crit Resolution Memo:

- `D_crit(ζ) = √(2 − ζ) · (2 − √(2 − ζ))` at reference mode `ε_k · τ = 1`
- At canon-default `ζ = 1/4`: `D_crit ≈ 0.896`
- At `ζ = 0`: `D_crit = 2√2 − 2 ≈ 0.828`
- As `ζ → 1`: `D_crit → 1`

**Q-C Boundary paper predictions (using the retired 0.5 threshold):**

- Transient oscillation count `N_osc` in quantum regime: 8–19 (~9) for D < 0.1
- Quality factor `Q`: ≈ 3.5 for D < 0.1
- Triad coupling: ≈ 0.03 all regimes
- Third-harmonic generation: 3–6% for D < 0.1
- Ground-state energy: `E_ground = αγρ₀`
- Relaxation time: `t_rel ≈ ρ₀/(αγ)`

## 3. What is missing — the blockers

### 3.1 Blocker 1 — the `x → D(x)` mapping for Arndt

The Dimensional Atlas anchors `L_0, T_0, R_0, D_phys` to particle mass `m`. These set the *scales* for the nondimensional PDE. They do **not** by themselves produce a function `D(x)` where `x` is an Arndt control parameter such as mass-at-fixed-velocity, velocity-at-fixed-mass, temperature, or collision rate.

`D` in the PDE is the nondimensional diffusion-channel weight (with `H = 1 − D` the participation-channel weight). Its physical meaning: the fraction of `F[ρ]` flux that advances the density directly vs. through the participation mode. Mapping this to an experimental control parameter requires an explicit physical argument about **which experimental knob modulates `D` vs. `H`, and how quantitatively.**

Plausible physical hypotheses (each requires explicit derivation):

- **H1 — mass-driven:** larger `m` → shorter `L_0, T_0` → higher effective coupling to environmental participation modes → higher `H`, lower `D`. Transition at the `m` where `D(m) = D_crit`.
- **H2 — coherence-length-driven:** `L_0 = ℏ/(mc)` vs. experimental coherence length `L_coh` (set by velocity spread, T_int, apparatus geometry). When `L_0 / L_coh` crosses a structural ratio, `D` crosses `D_crit`. In this case the relevant x is `L_coh / L_0` or equivalent.
- **H3 — environmental-coupling-driven:** collision rate `γ_env` or thermal photon emission rate `Γ_th` maps to participation-damping `ζ`; as `ζ` increases, `D_crit(ζ)` changes per the resolution memo, and the classical edge is crossed. This is different from H1/H2 because it works through `ζ` rather than `D` directly.
- **H4 — Markoffian decoherence rate:** environmental decoherence rate `Λ` (from Joos-Zeh / Hornberger-type calculations for the Arndt apparatus) maps directly into the PDE participation coupling `H` or timescale `τ`. `D(Λ)` is then derivable.

**None of these have been carried out in the current theory files.** H3 is closest to the spirit of the resolution memo (which shows how `D_crit` depends on `ζ`). H4 has the cleanest experimental handle because Hornberger et al. have published explicit `Λ(T, p, m)` calculations for Arndt-class apparatuses.

### 3.2 Blocker 2 — the retired `D_crit = 0.5` value

The Q-C Boundary paper asserts `D = 0.5` as the transition location, but the resolution memo (2026-04-22) retires that heuristic and replaces it with `D_crit(ζ=1/4) ≈ 0.896`. This is not a cosmetic fix — the two thresholds differ by ~80%.

Before the retrodiction can be executed, one of the following must happen:

- **(a)** Confirm that the Q-C Boundary paper's other quantitative predictions (`N_osc ≈ 9`, `Q ≈ 3.5`, 3–6% harmonic) rely on `D = 0.5` as a specific numerical substitution. If they do, they need to be re-derived against `D_crit ≈ 0.896` or whatever Arndt's anchored `ζ` yields.
- **(b)** Derive the physically appropriate `ζ` for Arndt's apparatus (per H3 / H4 above), compute `D_crit(ζ)` from the resolution-memo formula, and treat *that* as the prediction.
- **(c)** Explicitly note that Path C retrodiction requires re-deriving all quantitative Q-C Boundary predictions under the corrected `D_crit`, and treat this as prerequisite work.

Without one of these, the retrodiction has no well-defined target value.

### 3.3 Blocker 3 — missing experimental numbers

A real retrodiction requires specific numerical inputs from Arndt-group publications:

- **Fringe visibility vs. control parameter data** for at least one well-characterised experiment — e.g., visibility vs. mean thermal internal energy for functionalized oligoporphyrins in KDTLI (Eibenberger et al. 2013, *Phys. Chem. Chem. Phys.*), or visibility vs. intramolecular vibrational temperature for OTIMA class (Haslinger et al. 2013).
- **Apparatus parameters:** grating period `d_g`, Talbot length `L_T = d_g² / λ_dB`, source-to-grating distance `L_1`, grating-to-detector distance `L_2`, velocity spread `Δv/v`, residual pressure, UV-laser ionisation parameters (OTIMA), etc.
- **Reported transition control-parameter values:** the specific `x_c` at which visibility reaches the half-maximum between coherent and classical baselines.
- **Reported error bars** on visibility and on `x_c` determination, for tolerance assessment of the retrodiction.

These are in the public literature (Arndt, Hornberger, Brezger, Gerlich, Eibenberger, Fein, Geyer, etc.; see Arndt/Hornberger reviews). They are not compiled or cited in any file I have read inside the ED repo. Pulling them in is a specific literature task.

### 3.4 Blocker 4 — the `quantum_scales()` code inconsistency

The dimensional-01 memo §5 flags that `quantum_scales()` in `edsim/units/scales.py` does not currently pass `D_phys = ℏ/(2m)` to `compute_scales()`. The physical anchoring described in the atlas is not yet what the simulator computes. If the retrodiction needs simulator-side numerical work (e.g., to extract the specific `ε_k τ` product that fixes `D_crit` at Arndt's operating point), this code path has to be fixed first.

## 4. What a real retrodiction would look like — derivation steps

Step-by-step, the derivation needed is:

**Step 1: pick a specific Arndt dataset.** E.g., Eibenberger et al. 2013 visibility-vs-mass for functionalized oligoporphyrins at fixed velocity in KDTLI. Cite the paper, extract (m, V) points and apparatus parameters.

**Step 2: pick a physical hypothesis for `x → D(x)`.** Most defensible near-term: H4 — use the Hornberger-Joos-Zeh decoherence rate `Λ(m, T_env, p, v, apparatus)` and argue that the participation-channel weight `H = 1 − D` is a specific function of `Λ · τ_coh`, where `τ_coh` is the relevant coherence timescale (Talbot time `T_T = m d_g² / h`). State the hypothesis explicitly; justify it; make explicit any free-parameter assumption.

**Step 3: compute `ζ` at Arndt's operating point** from the same physical argument. `ζ` in the PDE is participation damping; in the Hornberger picture it should correspond to internal-state thermalisation or similar. Derive `ζ(T_int, m, apparatus)`.

**Step 4: compute `D_crit(ζ)`** from the resolution-memo formula `D_crit(ζ) = √(2 − ζ)(2 − √(2 − ζ))` at the value of `ζ` produced in Step 3.

**Step 5: compute `D(x)`** across the published range of `x` using the Step-2 hypothesis.

**Step 6: find `x_c` at which `D(x_c) = D_crit(ζ)`** — this is the ED prediction.

**Step 7: compare to Arndt's measured transition point.** Tolerance band from experimental error bars. Agreement within ~20% is suggestive; ~10% is strong; disagreement by >100% refutes the chosen hypothesis (Step 2) in this regime, not necessarily the framework.

**Step 8: document free parameters explicitly.** If any constant in Steps 2–5 was adjusted to make the prediction land, name it, quantify it, and note that the retrodiction is not "free-parameter-free." The difference between a zero-parameter retrodiction and a one-parameter fit is enormous for credibility.

## 5. What this retrodiction cannot yet rule in or out

Even if Steps 1–8 execute cleanly and the prediction matches Arndt's transition within tolerance, that result is:

- **Strong evidence** that ED's PDE-regime structure describes the Arndt regime correctly, at the order-of-magnitude level.
- **Not yet** a demonstration that ED predicts Arndt's transition with no free parameters — Step 2's hypothesis choice and Step 3's `ζ` derivation each involve modeling choices that a skeptic will press on.
- **Not yet** a demonstration that ED beats standard environmental decoherence theory, which *also* predicts the Arndt transition via Hornberger-Joos-Zeh calculations with similar accuracy. ED wins only if one of the distinguishing predictions (N_osc ≈ 9, 3–6% harmonic, sharp vs. smooth transition) is also checked against data.

The sharper win-condition: **a distinguishing prediction** — `N_osc ≈ 9` transient oscillations on the quantum side of the transition, or the 3–6% third-harmonic, or the sharpness of the transition — that standard decoherence theory and dynamical-collapse models do not make. If any of those is visible in Arndt's data and matches, that is a distinguishing retrodiction. The `D(x_c) = D_crit` check alone is a consistency check.

## 6. Tolerance framework

For the consistency check:

- **Refuted in this regime:** `D(x_c)` differs from `D_crit(ζ)` by more than a factor of 2. The chosen `x → D(x)` hypothesis (Step 2) is wrong for Arndt, or ED does not describe this regime at all.
- **Inconclusive:** `D(x_c) / D_crit(ζ) ∈ [0.5, 2]` but outside the tolerance set by apparatus uncertainty on `x_c` and any free-parameter slack in Steps 2–3. Consistent, but not a clean retrodiction.
- **Consistent:** `|D(x_c) − D_crit(ζ)| / D_crit(ζ) < 20%` with all free parameters zeroed or justified by independent argument. This is a real retrodiction result.
- **Distinguishing:** the previous, *plus* one of `N_osc ≈ 9`, 3–6% third-harmonic, sharp-transition signature, detected in Arndt's data within tolerance. This is what a headline Path C retrodiction looks like.

## 7. What this memo does and does not claim

**Claims:**

- The retrodiction task is well-posed once the four blockers in §3 are resolved.
- The path from blockers to retrodiction is the eight-step derivation in §4.
- The distinguishing-win-condition is stated in §5: consistency plus a distinguishing signature.

**Does not claim:**

- That any `D(x_c) = D_crit` retrodiction has been computed.
- That the Q-C Boundary paper's `D = 0.5` threshold is currently valid (it is retired in the resolution memo).
- That Arndt's apparatus has been mapped to ED's PDE in specific form — it has not.
- That ED's prediction beats standard decoherence for Arndt — this requires the distinguishing-signature check, not the consistency check alone.

## 8. Status and owner

- **Status:** Problem-specification scaffold. Not retrodiction. Not ready to cite as evidence for ED.
- **Owner:** Allen Proxmire (program).
- **To complete:** Steps 1–8 in §4. Any of them can be done independently; Steps 1 and 2 are prerequisite to all subsequent steps.
- **Earliest executable step:** Step 1 — compile the Arndt dataset(s) from published literature. This is a literature task requiring no new theory work.
- **Hardest step:** Step 2 — pick and defend the `x → D(x)` hypothesis. This is real physics modeling and should likely be collaborative with an experimental-decoherence specialist (Hornberger is the natural counterparty here; his published decoherence calculations for Arndt apparatuses are the existing state of the art).

---

## 9. One-line summary

> **Executing a real Arndt retrodiction requires (a) deriving the `x → D(x)` mapping that the Dimensional Atlas does not currently provide, (b) using the corrected `D_crit(ζ)` from the April 2026 resolution memo rather than the retired 0.5 heuristic, (c) compiling specific published Arndt visibility-vs-parameter data, and (d) executing the eight-step derivation in §4. This scaffold makes that task tractable; it does not execute it.**
