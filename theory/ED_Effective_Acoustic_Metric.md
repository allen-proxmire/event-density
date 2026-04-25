# Effective Acoustic Metric for Linearised ED

**Date.** 2026-04-22.
**Scope.** Working memo. Derive the effective metric `g^{eff}_{μν}` governing linearised ED fluctuations on a stationary background `ρ_0(x)`, in (i) the reversible slice `D = 0, ζ = 0` and (ii) the generic underdamped sector at leading order. Connect the metric's null cone to the reversible-slice QFT dispersion from `ED_Reversible_Sector_QFT.md`. Identify the acoustic-horizon locus with Canon P4's mobility-collapse surface (ED-06).
**Status.** Concrete calculation with explicit results. The metric is **kinematic** — it governs propagation of fluctuations on a given background — and is *not* accompanied by Einstein dynamics for `g^{eff}_{μν}`. This is the Unruh 1981 / Visser analogue-gravity construction applied to ED; the ED-specific content is the identification of `c_s²(x) = M(ρ_0(x))` and the horizon surface with the Canon P4 decoupling structure.

---

## 1. Linearised ED Equations

### 1A. Setup

Canonical ED (per `theory/PDE.md` §1):

$$
\partial_t\rho = D\bigl[M(\rho)\nabla^2\rho + M'(\rho)|\nabla\rho|^2 - P(\rho)\bigr] + H v,
\qquad
\tau\,\partial_t v = F[\rho] - \zeta v,
$$

with `H = 1 − D`, `F[ρ] = ∇·(M(ρ)∇ρ) − P(ρ)` (using `M∇²ρ + M'|∇ρ|² = ∇·(M∇ρ)`).

### 1B. Background ansatz and static condition

Take a **stationary** background `ρ(x, t) = ρ_0(x)`, `v(x, t) = v_0(x)`. For stationarity `∂_t ρ_0 = 0`, the P2 equation gives

$$
D\,F[\rho_0] + H\,v_0 = 0 \implies v_0(x) = -\frac{D}{H}\,F[\rho_0(x)].
$$

In the reversible slice `D = 0, H = 1`, this forces `v_0 = 0`. (Canonically: in the dissipationless limit, a stationary background has no participation flow.) In the generic case, `v_0 ≠ 0` is possible but is completely determined by `ρ_0`.

For the second equation, `τ∂_t v_0 = 0 = F[ρ_0] − ζ v_0`, so

$$
F[\rho_0] = \zeta v_0 = -\zeta\,\frac{D}{H}\,F[\rho_0] \implies F[\rho_0]\,(1 + \zeta D/H) = 0 \implies F[\rho_0] = 0.
$$

So **any stationary background must satisfy `F[ρ_0] = 0`** — the time-independent ED equation. In the reversible slice this is trivial (`v_0 = 0`). In the generic case it forces `v_0 = 0` as well (since `F[ρ_0] = 0`). **Stationary backgrounds are those with `F[ρ_0] = 0` and `v_0 = 0`.** We work in this class throughout.

### 1C. Linearised equations — reversible slice (D = 0, ζ = 0)

With `D = 0, ζ = 0, H = 1, τ = 1`. Let `ρ = ρ_0(x) + δρ(x, t)`, `v = δv(x, t)`. Second-order form for the reversible slice:

$$
\partial_t^2 \rho = F[\rho] \implies \partial_t^2 \delta\rho = \delta F[\rho_0]\cdot\delta\rho.
$$

Expanding `δF` around `ρ_0`:

$$
\delta F = \nabla\!\cdot\!\bigl(M(\rho_0)\nabla\delta\rho\bigr) + \nabla\!\cdot\!\bigl(M'(\rho_0)\,\delta\rho\,\nabla\rho_0\bigr) - P'(\rho_0)\,\delta\rho.
$$

Expanding the second term:

$$
\nabla\!\cdot\!\bigl(M'\,\delta\rho\,\nabla\rho_0\bigr) = M'(\rho_0)\,\nabla\rho_0\!\cdot\!\nabla\delta\rho + \bigl[\nabla\!\cdot\!(M'\nabla\rho_0)\bigr]\,\delta\rho.
$$

Writing `∇M(ρ_0(x)) = M'(ρ_0)∇ρ_0` for the spatial gradient of the background mobility, the linearised wave equation is

$$
\boxed{\;\;
\partial_t^2 \delta\rho \;-\; M(\rho_0)\,\nabla^2\delta\rho \;-\; 2\,\nabla M\!\cdot\!\nabla\delta\rho \;+\; V(x)\,\delta\rho \;=\; 0
\;\;}
$$

where

$$
V(x) \;\equiv\; P'(\rho_0) \;-\; \nabla\!\cdot\!(M'\nabla\rho_0).
$$

The coefficient structure `∂_t^2 − M\nabla^2 − 2\nabla M\!\cdot\!\nabla` is the key feature — it is **almost** a Laplace-Beltrami operator with spatially-varying `c_s²(x) = M(ρ_0(x))`, but the drift-term coefficient is `2\nabla M` rather than the `(1/2)\nabla M` that a pure `□_g` would give. This mismatch is resolved by a conformal field redefinition in §2.

### 1D. Linearised equations — generic underdamped sector

Redo with general `(D, ζ, τ)`. Eliminate `δv` from the 2×2 system using `δv = (1/H)(∂_t δρ + D·\delta F^{\rm linop}\delta\rho)` where `\delta F^{\rm linop}` is the linearisation of `F`. After algebra (detailed in Appendix A), the second-order equation for `δρ` is:

$$
\tau\partial_t^2\delta\rho + \bigl(\tau D\,\delta F^{\rm linop} + \zeta\bigr)\partial_t\delta\rho + (H + \zeta D)\,\delta F^{\rm linop}\delta\rho = 0,
$$

where `δF^{\rm linop}` acts on `δρ` as `M(ρ_0)∇²δρ + 2∇M·∇δρ − V(x)δρ` (same spatial operator as §1C, with opposite sign on `V`).

**Crucially, `δF^{\rm linop}` contains `∇²` operating on `δρ`**, so the middle term `(τD·δF^{\rm linop})∂_t δρ` contains `∇²∂_t δρ` — a dissipative-wave coupling. This breaks the exact acoustic-metric form at finite `γ`. At leading order in weak dissipation (`γ → 0`), the wave-like part dominates and the acoustic metric still applies with a rescaled signal speed (§3B).

---

## 2. Recasting into Acoustic-Metric Form

### 2A. Conformal field redefinition

Following standard Unruh-Visser: define

$$
\varphi(x, t) \;\equiv\; M(\rho_0(x))^{3/4}\,\delta\rho(x, t).
$$

Substituting into the reversible-slice wave equation (§1C) and using `∇M/M = (4/3)·(−∇Ω/Ω)` with `Ω = M^{-3/4}`, the drift-term coefficient transforms from `2\nabla M` to `(1/2)\nabla M`, matching the Laplace-Beltrami drift structure exactly. After simplification:

$$
-\frac{1}{M}\partial_t^2\varphi + \nabla^2\varphi + \frac{1}{2M}\nabla M\!\cdot\!\nabla\varphi \;=\; \frac{1}{M}\,\tilde V(x)\,\varphi,
$$

where `\tilde V(x)` absorbs the original `V(x)` plus the conformal-transformation corrections. Equivalently, using `√M = c_s(x)`:

$$
\frac{1}{\sqrt{-g}}\,\partial_\mu\!\bigl(\sqrt{-g}\,g^{\mu\nu}\partial_\nu\varphi\bigr) \;=\; m_{\rm eff}^2(x)\,\varphi,
$$

with the effective metric and mass defined in §2B.

### 2B. Explicit effective metric

**Effective metric (reversible slice, stationary background, signature `(−, +, +, +)`):**

$$
\boxed{\;\;
g^{\rm eff}_{\mu\nu}(x) \;=\; \mathrm{diag}\!\bigl(-M(\rho_0(x)),\; 1,\; 1,\; 1\bigr).
\;\;}
$$

Line element:

$$
ds^2 \;=\; -M(\rho_0(x))\,dt^2 + dx^2 + dy^2 + dz^2 \;=\; -c_s^2(x)\,dt^2 + d\vec x^{\,2},
$$

with

$$
c_s(x) \;\equiv\; \sqrt{M(\rho_0(x))}
$$

the local acoustic signal speed. Inverse metric: `g^{μν}_{\rm eff} = \mathrm{diag}(-1/M, 1, 1, 1)`. Determinant: `\det g_{\rm eff} = -M`, `\sqrt{-g_{\rm eff}} = \sqrt M = c_s`.

**Effective mass term:**

$$
m_{\rm eff}^2(x) \;=\; \frac{\tilde V(x)}{M(\rho_0(x))} \;\;\stackrel{\rho_0 = \rho^*}{\longrightarrow}\;\; \frac{P_0}{M_0} \;\equiv\; \frac{P'(\rho^*)}{M(\rho^*)}.
$$

For uniform background `ρ_0 = ρ*`, `\tilde V = P_0`, so `m_{\rm eff}^2 = P_0/M_0` — a parameter-free ED invariant of the reversible sector.

**Notes on this metric.**

- **Diagonal.** No `g_{0i}` off-diagonal "flow" terms, because the stationary background has `v_0 = 0` (§1B). This is the Unruh acoustic metric *without* background flow — the simplest case.
- **Purely background-dependent.** The metric is a functional of the static `ρ_0(x)` through `M(ρ_0(x))`. It has no dynamical equation of its own.
- **Conformally flat when uniform.** If `ρ_0 = ρ^*` everywhere, `g^{\rm eff}_{μν}` is Minkowski with sound speed `c_s = √M_0` instead of `c`.

### 2C. Non-uniform background: spatially varying c_s(x)

The interesting case: `ρ_0(x)` non-uniform, so `M(ρ_0(x))` varies in space, so `c_s(x)` varies. The metric is non-trivial Lorentzian with curvature. Ricci scalar (schematic, for diagonal `g`):

$$
R[g^{\rm eff}] \;\sim\; \frac{\nabla^2 c_s}{c_s} + \left(\frac{\nabla c_s}{c_s}\right)^2 \;\sim\; \frac{M'}{M}\nabla^2\rho_0 + \left(\frac{M'}{M}\right)^2|\nabla\rho_0|^2.
$$

Curvature is a **second-derivative functional of the background** `ρ_0(x)` — the statement "curvature is the path of easiest updating" finds its explicit form here: regions where `M(ρ_0)` varies quickly have high effective curvature, and null geodesics bend toward regions of lower `c_s` (where updating is slower).

---

## 3. Horizon and Causal-Cone Structure

### 3A. Null cones of g^{eff}

Null condition: `g^{\rm eff}_{μν}\,k^μ k^ν = 0 \implies -M(\rho_0)(k^0)^2 + |\vec k|^2 = 0 \implies |\vec k|/|k^0| = c_s(x)`.

**Locally, fluctuations `δρ` propagate inside a null cone of half-angle `c_s(x)`.** In regions where `M` is large, the cone opens; where `M` is small, the cone closes.

### 3B. Acoustic horizons

An acoustic horizon is a surface where `c_s(x) → 0`, i.e., `M(ρ_0(x)) → 0`. By Canon P4, `M(ρ_{\rm max}) = 0`: mobility vanishes at the density ceiling.

**So the acoustic-horizon locus of `g^{\rm eff}` is precisely the Canon P4 mobility-collapse surface `ρ_0(x) = ρ_{\rm max}`.**

This is a **direct identification** with ED-06 ("Horizons as Decoupling Surfaces"): the kinetic barrier at `ρ → ρ_{\rm max}` is simultaneously
- (P4 view) a surface where diffusive transport vanishes, so excitations cannot cross,
- (acoustic-metric view) a surface where `g^{\rm eff}_{00} → 0`, so null cones degenerate to vertical lines.

The two descriptions are consistent: **P4 mobility collapse ↔ acoustic horizon**. This is the tightest "geometry-emerges-from-ED" statement the framework currently supports.

### 3C. Horizon structure is not GR

Acoustic horizons in this construction have some GR-horizon features (one-way propagation for fluctuations, dispersionless causal disconnection at the leading-order metric) and lack others (no event-horizon dynamics independent of `ρ_0`, no Bekenstein-Hawking temperature in the strict sense — the analogue-gravity Hawking radiation argument requires stationarity *and* a specific ρ_0 profile). The statement `g^{\rm eff}_{00} → 0 ⇔ M → 0` is clean; the thermodynamic implications are separate (see ED-06 for the ED-specific treatment and `ED_Geometry_Emergence_Scoping.md` §3D for the Jacobson/entropic route, which is a separate and harder program).

---

## 4. Connection to the Reversible-Slice QFT Dispersion

### 4A. On-shell condition

Plane wave `\varphi(x, t) = e^{i(\vec k\cdot\vec x - \omega t)}` on the **uniform** background (`M = M_0` constant). The wave equation `(\Box_g - m_{\rm eff}^2)\varphi = 0` gives

$$
g^{\mu\nu}_{\rm eff}\,k_\mu k_\nu + m_{\rm eff}^2 = 0 \implies -\frac{(-\omega)^2}{M_0} + |\vec k|^2 + \frac{P_0}{M_0} = 0,
$$

$$
\implies \omega^2 = M_0\,|\vec k|^2 + P_0 \;=\; \Omega^2(k).
$$

**Exactly the reversible-slice QFT dispersion from `ED_Reversible_Sector_QFT.md` §2D.**

### 4B. Geometric interpretation of Ω(k)

- `\Omega(k)` is the **on-shell frequency** of a massive scalar field on the acoustic-metric Minkowski background with sound speed `c_s = √M_0` and mass `m_{\rm eff} = √(P_0/M_0)`.
- The gap at `k = 0` (`Ω_0 = √P_0`) is the emergent rest-mass of the reversible-sector field — penalty `P_0` plays the role of mass².
- The large-`k` asymptote (`Ω(k) → √M_0 \cdot k = c_s k`) is the linear acoustic-dispersion branch.
- Crossover scale: `k_* = √(P_0/M_0) = m_{\rm eff}` — the inverse Compton wavelength in these units.

### 4C. QFT + metric consistency

- The QFT is a free massive scalar with `c_s² = M_0`, `m_{\rm eff}² = P_0/M_0`.
- The acoustic metric is `g^{\rm eff}_{μν} = diag(−M_0, 1, 1, 1)`.
- The QFT dispersion is `ω² = c_s² k² + m_{\rm eff}² c_s²` (standard massive KG with `c → c_s`).
- The acoustic-metric null cones have `|\vec k|/|k^0| = c_s`, the speed at which massless perturbations would propagate — *in ED, there are none at linear order, since `P_0 > 0` implies all modes are massive.*

**This is consistent with the `c_0 = L_0/T_0 = c/0.6` identification from `theory/ED-Dimensional-01-Ext.md`:** in physical units, the dictionary's `c_0` is `c_s = √M_0`, so `M_0 = (c/0.6)^2 = c^2/0.36` pins the mobility at equilibrium in terms of the fundamental speed. This was flagged in `ED_Reversible_Sector_QFT.md` §7E; it is now sharpened to "the acoustic-metric signal speed equals the dictionary's `c_0`."

### 4D. Generic underdamped sector: rescaled c_s

At leading order in weak dissipation (§1D), the wave part of the generic-sector equation has `c_s²_{\rm gen} = (H + ζ D)\,M_0/τ`. Correspondingly:

$$
g^{\rm eff}_{\mu\nu}\bigr|_{\rm gen} \approx \mathrm{diag}\!\left(-\frac{(H + \zeta D)\,M(\rho_0)}{\tau},\; 1,\; 1,\; 1\right),
$$

with dispersion `\omega^2 ≈ c_{s,\rm gen}^2 |\vec k|^2 + (H + \zeta D)P_0/\tau` and an imaginary damping correction at next order (sub-leading). **The generic-sector acoustic metric is the reversible-sector metric with `M_0` rescaled by `(H + ζD)/τ`.** The dissipative correction is not captured by a real-valued metric.

---

## 5. Interpretation: What ED-10 Can Now Claim

### 5A. Tight, honest claim

> **ED-10 (geometry form).** "On a stationary background `ρ_0(x)` satisfying `F[ρ_0] = 0`, linearised fluctuations `δρ(x, t)` propagate on an emergent effective metric `g^{\rm eff}_{μν}(x) = diag(−M(ρ_0(x)), 1, 1, 1)` in the reversible slice. The metric's acoustic horizon surface `M(ρ_0(x)) → 0` coincides exactly with Canon P4's mobility-collapse surface, providing a direct structural identification with ED-06 ('Horizons as Decoupling Surfaces'). The metric's null cones set the causal structure for the reversible-sector free-scalar QFT derived in `ED_Reversible_Sector_QFT.md`: the QFT dispersion `Ω(k) = √(P_0 + M_0 k^2)` is the on-shell condition for the metric with `c_s² = M_0` and `m_{\rm eff}² = P_0/M_0`. In the generic underdamped sector, the leading-order metric has signal speed rescaled by `(H + ζD)/τ`; dissipation at sub-leading order is not captured by a real-valued metric."

### 5B. Three concrete structural statements

From this memo and the prior two (QFT, U(1) scoping):

1. **Kinematic geometry.** ED has an emergent effective metric for linearised fluctuations on any stationary background. Explicit form: `diag(−M(ρ_0), 1, 1, 1)`. *Derived, not postulated.*
2. **Causal cones.** Null cones of `g^{\rm eff}` set fluctuation causality. Cone half-angle = `c_s(x) = √M(ρ_0(x))`.
3. **Horizons.** Acoustic-horizon locus `g^{\rm eff}_{00} → 0` = Canon P4 surface `M(ρ) = 0` = ED-06 decoupling surface.

### 5C. What remains absent

**Explicitly not gained from this construction:**

- **Einstein dynamics.** `g^{\rm eff}_{μν}` is slaved to `ρ_0(x)`, which evolves under ED's own PDE. There is no equation of motion for `g^{\rm eff}_{μν}` analogous to `G_{μν} = 8πG T_{μν}`.
- **Tensor DOFs.** Only the trace / conformal-factor-like part of the metric is dynamical (through `ρ_0`). No transverse-traceless modes, no gravitational waves in the GR sense.
- **Gauge sector.** Reaffirming `Emergent_U1_in_ED_Scoping.md` §6 and `Fine_Structure_Constant_Scoping.md` §6: no vector potential, no field strength, no `α`.
- **Newton constant.** No emergent coupling `G` between matter and geometry. The metric is a kinematic backdrop for `δρ`, not a dynamical field coupled to a stress-energy source.

**This is a (ii)-grade result** in the scoping-memo taxonomy (`ED_Geometry_Emergence_Scoping.md` §1A): kinematic acoustic metric, not dynamical Einstein gravity.

---

## 6. Limitations

### 6A. No dynamical metric equation

The metric `g^{\rm eff}_{μν}` is a functional of `ρ_0(x)`. It inherits its dynamics from `ρ_0`'s evolution under the ED PDE — which is **not** the Einstein equation. Any statement of the form "`G_{μν}[g^{\rm eff}] = 8πG T_{μν}^{\rm eff}`" is unsupported by this construction.

### 6B. No tensor modes

The metric has `d(d+1)/2` components formally (10 in 4D), but only one independent scalar function `M(ρ_0(x))` drives the whole thing. Transverse-traceless tensor modes (gravitational-wave sector of GR) cannot be sourced by a single scalar background. This is the degrees-of-freedom obstruction from `ED_Geometry_Emergence_Scoping.md` §5C.

### 6C. Reversible slice is measure-zero

The exact acoustic-metric form is clean only for `D = 0, ζ = 0`. Generic underdamped sectors admit it at leading order; higher-order dissipative corrections break the metric structure.

### 6D. No gauge sector

No U(1), no charge, no vector potential. See `Fine_Structure_Constant_Scoping.md` §6 and `Emergent_U1_in_ED_Scoping.md` §6.

### 6E. Sound speed ≠ c, exactly

`c_s = √M_0` is set by ED's mobility at equilibrium, and equals `c/0.6 ≈ 1.667 c` via the ED-Dimensional-01 dictionary (§4C). In the real world, gravitational waves propagate at `c` to `|c_{GW}/c − 1| < 10^{-15}` (LIGO/GW170817). Without a mechanism that equates `c_s` with `c`, the emergent-metric story has a 60% speed mismatch that is not physically viable for a literal "gravity comes from ED" claim. This is **not new**: it was flagged in `ED_Geometry_Emergence_Scoping.md` §7B.

### 6F. Weak-dissipation approximation in the generic sector

At finite `γ`, the dissipative correction (imaginary part of the dispersion) is not a real metric. A doubled-formalism (Schwinger-Keldysh) or complexified metric could in principle capture it, but would no longer be "kinematic acoustic metric" in the standard sense.

### 6G. No Hawking temperature derivation

The acoustic-horizon surface is structurally present, but deriving the standard `T_H = ℏκ/(2π)` thermality requires the Unruh-Wald calculation in the specific acoustic-metric form, *with* a well-defined stationary Killing vector. For ED's `ρ_0 = ρ_{\rm max}` surface, this calculation is doable in principle but is a separate project.

---

## 7. Assessment and Recommendation

### 7A. Verdict

**ED admits a concrete, explicit, non-trivial emergent acoustic metric.** `g^{\rm eff}_{μν} = diag(−M(ρ_0(x)), 1, 1, 1)` is a kinematic result with three immediate structural consequences: null cones, horizons coinciding with Canon P4 / ED-06, and a dispersion `Ω(k) = √(P_0 + M_0 k²)` matching the reversible-slice QFT. **This is the strongest derivation-grade result the geometry-from-ED thread currently supports.**

### 7B. What it adds to the repo

- `theory/ED_Geometry_Emergence_Scoping.md` §9 Stage 1 is now complete: effective metric is explicit in closed form.
- `theory/ED_Reversible_Sector_QFT.md` §7E's flagged identification `c_0 = c_s = √M_0` is now sharpened: it is the null-cone speed of the acoustic metric.
- Canon P4 and ED-06 gain a second independent characterisation: the mobility ceiling is an acoustic horizon.
- Nothing breaks. No Canon update needed; §5A gives the precise ED-10 geometry line for orientation-doc adoption if desired.

### 7C. What to do (and not) with this

- **Do.** Use it where the question is *kinematic* — causality of fluctuations, horizons, propagation speed, dispersion.
- **Do.** Cite it when explaining how ED-10 connects geometry to ED microstructure.
- **Don't.** Use it to claim ED derives GR. The metric is slaved to `ρ_0`; no Einstein equation emerges.
- **Don't.** Use it to claim `c_s = c` or to paper over the 60% speed mismatch in physical units.
- **Don't.** Use it as a route to `α` or to SM-gauge content — neither is present.

### 7D. Natural next steps (if pursued)

- **Explicit curvature for a canonical `ρ_0` profile.** E.g., a Gaussian bump. Compute `R[g^{\rm eff}]`, check it is finite, check ansatz self-consistency. ~1 week.
- **Horizon thermality.** Specialise to a 1D `ρ_0(x)` with a mobility-collapse surface, check whether the surface gravity `κ` is well-defined, compute `T_H = ℏκ/(2π)` if so. Would make the P4/ED-06 identification quantitative. ~2–3 weeks.
- **Schwarzschild-like profile check.** For what `ρ_0(x)` does `g^{\rm eff}` match the Schwarzschild form? If such a profile exists, check it is self-consistent under the ED PDE. Important: a positive answer here does not imply Einstein dynamics — it implies ED *can* accommodate a Schwarzschild-like geometry as a kinematic backdrop, not that ED *predicts* it.
- **Generic-sector dissipative corrections.** Set up the Schwinger-Keldysh machinery for the underdamped regime and check whether the imaginary part of the dispersion can be captured as a metric complexification or requires a genuinely new formalism. Hard; deprioritised.

---

## Appendix A — Derivation of the generic-sector wave equation

Starting from the linearised 2×2 system (§1B):

$$
\partial_t\delta\rho = D\,\delta F + H\,\delta v,
\qquad
\tau\partial_t\delta v = \delta F - \zeta\,\delta v,
$$

with `δF = M_0∇²δρ + 2∇M·∇δρ − V(x)δρ ≡ 𝓛 δρ` (a linear spatial operator). From the first equation: `δv = (1/H)(∂_t δρ − D\mathcal L\delta\rho)`. Substitute into the second:

$$
\frac{\tau}{H}\,\partial_t\bigl(\partial_t\delta\rho - D\mathcal L\delta\rho\bigr) = \mathcal L\delta\rho - \frac{\zeta}{H}\bigl(\partial_t\delta\rho - D\mathcal L\delta\rho\bigr).
$$

Multiply through by `H` and rearrange:

$$
\tau\,\partial_t^2\delta\rho - \tau D\,\partial_t(\mathcal L\delta\rho) + \zeta\,\partial_t\delta\rho - \zeta D\mathcal L\delta\rho - H\mathcal L\delta\rho = 0.
$$

Since `\mathcal L` does not depend on `t`, `∂_t(\mathcal L\delta\rho) = \mathcal L\,\partial_t\delta\rho`. Combining terms:

$$
\tau\,\partial_t^2\delta\rho + \bigl(\zeta - \tau D\mathcal L\bigr)\,\partial_t\delta\rho - \bigl(H + \zeta D\bigr)\mathcal L\delta\rho = 0.
$$

Moving all to one side with consistent signs (and noting that `-\mathcal L` is the elliptic spatial operator governing restoring force):

$$
\tau\,\partial_t^2\delta\rho + (\tau D\,|\mathcal L| + \zeta)\,\partial_t\delta\rho + (H + \zeta D)\,|\mathcal L|\,\delta\rho = 0,
$$

reading `|\mathcal L|\delta\rho ≡ −𝓛 δρ = −M_0∇²δρ − 2∇M·∇δρ + V(x)δρ`. This is the form used in §1D.

At leading order in weak dissipation (`τD, ζ → 0` with ratios fixed such that underdamping holds), the dominant balance is `τ∂_t² + (H + ζD)|\mathcal L|`, giving a pure wave equation with effective operator `|\mathcal L|·(H + ζD)/τ` and hence `c_{s,{\rm gen}}^2 = (H + ζD)\,M_0/τ` (§4D).

---

**Status.** Working memo. Concrete result: explicit acoustic metric for ED fluctuations, with null cones, horizons, and QFT-dispersion cross-check all consistent. No new axioms, no new predictions, no Canon updates required. Recommend adopting §5A as a geometry-form companion to the ED-10 line updated in `ED_Reversible_Sector_QFT.md §7C`.
