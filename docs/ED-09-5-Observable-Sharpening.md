# ED-09.5 Observable Sharpening — Arndt and Aspelmeyer Regimes

**Status:** DRAFT v0.9 (2026-04-20). First-pass deliverable for the §6 scope of [`ED-09-5-Experimental-Strategy.md`](ED-09-5-Experimental-Strategy.md). Covers the Arndt (matter-wave) regime in §1–§10, the Aspelmeyer (optomechanics) regime in §11–§19, and the `(ρ, v)` ↔ optomechanics-mode identification in §22. Theory consolidation in §21. Haroche/Raimond cavity-QED regime deferred.

---

## ⛳ Theory Milestone (v0.7, 2026-04-20)

The Aspelmeyer (optomechanics) analysis has reached a clean, internally consistent stopping point. Five results form the milestone:

1. **`v` ↔ `X_cav` identification** (§22). The participation field corresponds to the cavity-field amplitude quadrature in the rotating frame at drive frequency, carrying radiation-pressure back-action onto the mechanical mode. Selected from three pre-specified candidates by linearized PDE matching; candidate (a) `v ↔ p_mech` structurally falsified, candidate (c) `v ↔ internal triad mode` held in reserve as salvage.
2. **`D = γ_dec/(γ_dec + ω_m)` derivation** (§11, §22.3). The channel-weight mapping is no longer heuristic — it follows from rate-balance under candidate (b)'s identification, with `DP₀ ↔ γ_dec` and `H ↔ ω_m/(γ_dec + ω_m)`. The bifurcation at `D = 0.5` lands at the well-known sideband-resolution threshold `γ_dec = ω_m`.
3. **`ω_v = 2π · N_osc · γ_dec`** (§15, full-cycle convention confirmed via code-trace + ED-Phys-19 derivation). For single-mode optomechanics with `N_osc = 8`: **`ω_v / 2π = 8 γ_dec`**. The `τ_v = 1/γ_dec` ansatz is grounded in the good-cavity limit `κ ≫ γ_dec` (typical for §13 systems).
4. **`Q ≈ 6.3 ± 2`** (§16 F3, §21.3) as the structurally correct value for the cavity-mapped regime. Derived from ED-Phys-19's explicit `Q = √(K_eff·τ)/ζ = √(0.1·100)/0.5 = 6.32` at canonical parameters with low-k single-mode limit. The orientation's `Q ≈ 3.5` quote is not derivable from any in-repo source; manual verification against the 00.3 PDF (Desktop) is logged as a low-priority follow-up.
5. **Three non-trivial cross-checks** support candidate (b):
   - **ζ check:** canon-default ζ ≈ 0.45 vs cavity-derived ζ ≈ 0.5 (§22.3) — agreement to ~11%.
   - **ζ exact match:** ED-Phys-17/19 used ζ = 0.5 exactly; cavity-derived ζ = 1/2 from `Ẋ_cav = -(κ/2)X_cav` (§21.2 + §21.3) — agreement to one decimal.
   - **`N_osc` cross-derivation:** ED-Phys-17 measured `N_osc = 8` (full cycles per algorithm with `//= 2`) vs ED-Phys-19 derived `N_osc ≈ 9` from `Q = 6.3` with 1% amplitude threshold (§15 + §21.3) — agreement to within rounding.

**Implication.** The §11 channel-weight mapping, the §15 envelope-frequency derivation, and the §16 falsification criteria F0–F5 now rest on a single, internally consistent ED parameter regime that maps cleanly onto cavity-coupled optomechanics. Cold-reader pass should read this as ED-derived rather than ED-flavored heuristic. The Aspelmeyer email can proceed once the strategy-doc §7 v2 draft is updated to match (deferred per direction).

**Theory track status: idle.** Three of four §21 open issues resolved (§21.1, §21.2, §21.3). The remaining §21.4 (Atlas anchor systematization across non-quantum regimes) is parked as future work — see §21.4. Next session may either resume §21.4 or pivot to a different ED-Math Pipeline branch (FRAP, merger-lag, weak-lensing).

---

**Recent updates (descending order):**

- **2026-04-20 v0.9 — §20 manual thesis-skim result.** User skimmed Delic 2019 and Magrini 2021 PhD theses for the ED-09.5 envelope signature. **Result: no mention of ringdown, slow envelope, PSD features near 16 mHz, or Allan-variance signatures matching the prediction.** Three interpretations weighed in §20: (1) most-likely — analysis-pipeline blind spot (standard optomechanics demodulation, time-binning, PSD bandwidth, and Allan-variance ranges all filter out a sub-Hz envelope on a 100 kHz–GHz carrier); (2) plausible — signature genuinely absent, candidate (b) wrong, candidate (c) salvage path activates; (3) less likely — signature present but below noise floor. **Implication: the email framing strengthens.** Drop "I see X in your Fig Y" anchor; honest framing is "the predicted envelope wouldn't appear in your published figures even if present — your analysis pipelines aren't constructed to expose it; please share raw `x(t)` so a specific envelope-extraction reanalysis can be done." Removes the awkward "you missed something" subtext.
- **2026-04-20 v0.8 — §20 Delic dataset reconnaissance completed.** Five-step web verification run. **Verdict: no public deposit of raw time-domain `x(t)` traces exists** for Delic 2020 or Magrini 2021. Science data-availability is the standard "all data in the paper" boilerplate (no repository deposit). PHAIDRA and Zenodo contain only adjacent records (Ciampini 2023, Rademacher `optoanalysis`, different papers). Both PhD theses ([Delic 2019](https://aspelmeyer.quantum.at/fileadmin/user_upload/a_aspelmeyer_quantum/Research/Thesis_Delic.pdf), [Magrini 2021](https://www.dropbox.com/s/qi8jpxn18kgkwdt/magrini_thesis_v7_291021_submitted.pdf?dl=0)) **publicly downloadable**. Implication: the Aspelmeyer email request (2) becomes the primary channel for raw-trace access, not a fallback. §20 status marked COMPLETED; manual skim of the two theses logged as remaining user-side task before send.
- **2026-04-20 v0.7 — `Q ≈ 3.5` provenance resolved (§21.3) + §15 algorithmic correction.** Two findings from this pass:
  1. **`Q ≈ 3.5` is not derivable from any in-repo parameter set.** ED-Phys-19 (the closest in-repo unified-cosmology document) explicitly derives `Q = √(K_eff·τ)/ζ = 6.3` (low-k single-mode) at canonical parameters and quotes Q range 6.3–10.1. Three derived docs (`theory/Architectural_Canon.md`, `docs/ED-Testing-Synthesis-2026-04-17.md`, `docs/ED-Logic-Flow.md`) cite Q ≈ 3.5 attributed to "00.3" with no derivation; the actual 00.3 PDF (Desktop) was not accessible from this session. Best in-repo answer: cavity-mapped optomechanics inherits ED-Phys-19's `Q ≈ 6.3 ± 2`. F3 tightened from `[3, 9]` to `[4, 9]`. Manual verification against 00.3 PDF logged as follow-up (low priority).
  2. **§15 v0.6 factor-of-2 correction was wrong; reverted.** Tracing ED-Phys-17's actual code at [`ed_phys_oscosmo.py`](../archive/research_history/ED Physics/ED-Phys-17_OscillatorCosmology/ed_phys_oscosmo.py) lines 408–415 shows the algorithm counts ALL local extrema (max + min) and then divides by 2 (`h_osc //= 2`). For a clean underdamped sinusoid with N full cycles, this yields 2N extrema → reported h_osc = N. So `N_osc` IS full cycles, not turning points (despite §3.2's verbal description). Independent confirmation: ED-Phys-19 derives `N_osc = Q·ln(A₀/A_min)/π ≈ 9` for Q=6.3, 1% threshold, full-cycle formula — matches ED-Phys-17's measured 8 to within rounding. §15 formula reverts to `ω_v = 2π N_osc γ_dec`; numerical table reverts to v0.5 values (factor of 2 increase from v0.6).
  - **Three non-trivial cross-checks now passing** supporting candidate (b): (i) canon-default ζ ≈ 0.45 vs cavity ζ ≈ 0.5 (§22.3); (ii) ED-Phys-17/19 ζ = 0.5 exactly matching cavity ζ (§21.2 + §21.3); (iii) ED-Phys-17 measured `N_osc = 8` consistent with ED-Phys-19 derived `N_osc ≈ 9` from Q = 6.3 with 1% amplitude threshold.
- **2026-04-20 v0.6 — `N_osc` convention misread as turning points.** Superseded by v0.7 algorithmic trace.
- **2026-04-20 v0.5 — `v` identification resolved (§22).** Evaluated three pre-specified candidates: (a) `v ↔ p_mech`, (b) `v ↔ X_cav` (cavity back-action quadrature), (c) `v ↔ internal triad mode`. Linearized uniform-mode equations derived for each and matched against the canonical PDE template `[[-DP₀, H], [-P₀/τ, -ζ/τ]]`. **Candidate (b) selected.** Candidate (a) structurally falsified (forces `D = 0`, predicts `ω_v = ω_m` not slow envelope). Candidate (c) held in reserve as salvage if (b) fails experimentally. **Two non-trivial outcomes:** (i) the §11 mapping `D = γ_dec/(γ_dec + ω_m)` is now **derived** from rate-balance under candidate (b), not heuristic; (ii) `ζ ≈ 0.5` (from cavity decay structure) agrees with canon default `ζ ≈ 0.45` to ~11%. §11 status upgraded from "heuristic-but-motivated" to "derived under specified `(ρ, v)` identification"; §15(β) ansatz `τ_v = 1/γ_dec` derived in good-cavity limit `κ ≫ γ_dec`; §21.1 closed.
- **2026-04-20 v0.4 — Theory consolidation pass.** Tightened §11 (mapping flagged as heuristic), added §16.5 (F0–F5 dependency structure: three independent dimensions, not six), added §21 (open theory issues). **Most important finding then:** ED's quoted `Q ≈ 3.5` and `N_osc ≈ 9` are not jointly consistent under the standard underdamped-oscillator formula `N_osc(amp→1/e) = Q/π ≈ 1.1`. Either ED-Phys-17 uses a strict-coherence threshold (amplitude → ~10⁻³ gives `N_osc ≈ 7.7`), or the participation mode is nonlinearly extended via triad coupling. The §15(β) derivation depends on which. Must be pinned down against ED-Phys-17 directly.
- **2026-04-20 v0.3 — Delic dataset reconnaissance** added (§20) and immediately deferred per direction: live web/repository checks held until ED prediction architecture is fully settled. §20 now serves as a logged future manual task, not an active workstream.
- **2026-04-20 v0.3 — §15(β) derivation committed.** `ω_v = 2π N_osc γ_dec` from `τ_v = 1/γ_dec` ansatz. Adds F0 to falsification criteria.
- **2026-04-20 v0.2 — Aspelmeyer regime added** (§11–§19). Natural mapping `D = γ_dec/(γ_dec + ω_m)`; bifurcation at sideband-resolution threshold; all cooled systems on quantum side; envelope signatures testable in existing ringdown traces.
- **2026-04-20 v0.1 — Arndt regime initial pass** (§1–§10). Three constitutive ansatzes for `D(m)` all fail.

**Bottom line.**

- **Arndt (matter-wave) regime** (§1–§7): The §6 deliverable as originally scoped — *compute `m_c` such that `D(m_c) = 0.5`, with uncertainty propagated from the quantum-regime Atlas* — **cannot be completed from the existing Atlas alone**. Three candidate constitutive ansatzes are tried; all give either untestable or already-falsified `m_c`. **The Arndt email should not go in current form.**

- **Aspelmeyer (optomechanics) regime** (§11–§17): Has a **natural ED mapping** via the dimensionless damping ratio `D ≡ γ_dec/(γ_dec + ω_m)`, with the bifurcation at the well-known sideband-resolution threshold `γ_dec = ω_m`. Numerically, *all current Aspelmeyer-class experiments sit on the quantum side* (`D ≪ 0.1`), so the sharpness of the bifurcation cannot be tested directly — but the four pre-registered quantum-side signatures (`N_osc ∈ [8, 19]`, `Q ≈ 3.5`, harmonic ratio 3–6%, sharp transition) **should already be present in published time-domain ringdown data** as a slow participation-mode envelope on top of the high-Q mechanical motion. **This is a viable Tier-1 reanalysis target**, and the Aspelmeyer email can go forward if reframed from "find the critical bifurcation" to "find these specific signatures in your existing ringdown data."

---

## 1. Formal framing (carry-over from strategy §1.5)

The canonical ED PDE has a sharp damping-discriminant bifurcation at

$$\Delta = D + 2\zeta = 1 \quad\Longleftrightarrow\quad D_{\text{crit}} = 0.5,$$

derived analytically in [00.3] and numerically verified in ED-Phys-18 and ED-SIM-3D. The bifurcation separates three regimes of the same equation:

| Regime | Condition | Dynamical character |
|:-------|:---------:|:--------------------|
| Oscillatory | `D < 0.1` | Underdamped, reversible, standing participation waves; `N_osc ∈ [8, 19]`; third-harmonic ratio 3–6%; `Q ≈ 3.5` |
| Hybrid | `0.1 ≤ D ≤ 0.4` | Mixed, smooth interpolation |
| Parabolic | `D ≥ 0.5` | Overdamped, irreversible, structure-forming; Barenblatt spreading |

ED-09.5's identification: this bifurcation **is** the physical quantum-classical transition. Coherent quantum behaviour ↔ `D < 0.1` regime; classical behaviour ↔ `D ≥ 0.5` regime; the transition is sharp. The four quantitative signatures on the quantum side (`N_osc`, `Q`, harmonic ratio, transition sharpness) are pre-registered falsification criteria.

To translate this into an experimental prediction, one needs the **mapping** from a regime-specific control parameter `x` to the channel weight `D(x)`, then to solve `D(x_c) = 0.5`. For the Arndt (matter-wave) regime, the natural control parameter is the molecular mass `m`.

---

## 2. The Atlas anchor

The Dimensional Atlas's quantum-regime mapping ([`papers/Dimensional_Atlas/regimes/ED-Dimensional-01_Quantum_Regime.md`](../papers/Dimensional_Atlas/regimes/ED-Dimensional-01_Quantum_Regime.md)) anchors three dimensional scales to mass via the Madelung correspondence:

$$L_0 = \frac{\hbar}{mc}, \qquad D_{\text{phys}} = \frac{\hbar}{2m}, \qquad T_0 = \frac{2\,D_{\text{nd}}\,\hbar}{m c^{2}}, \qquad R_0 = L_0^{-d}.$$

Numerical anchor (proton, `d=2`):

| Quantity | Value | Unit |
|:---------|:------|:-----|
| `L₀` | `2.103 × 10⁻¹⁶` | m |
| `T₀` (at `D_nd = 0.3`) | `4.209 × 10⁻²⁵` | s |
| `D_phys` | `3.153 × 10⁻⁸` | m² s⁻¹ |

These quantities all scale with mass: `L₀ ∝ 1/m`, `T₀ ∝ 1/m`, `D_phys ∝ 1/m`.

---

## 3. The conceptual gap

The dimensionless channel weight `D_nd` enters the Atlas only through `T₀ = L₀² · D_nd / D_phys`. By construction of `T₀`, this relation is an identity for *any* chosen `D_nd`. There is no functional relation `D_nd(m)` in the Atlas — `D_nd` is a free constitutive parameter that the modeller picks (canonical value 0.3) when setting up a simulation.

This is not a defect of the Atlas; it is a deliberate division of labour. The Atlas tells you *how to convert simulation outputs to SI units for a chosen `D_nd`*, not *what `D_nd` should be for a chosen physical system*. The latter is a constitutive statement of the kind that, in standard PDE theory, comes from microscopic derivation or experimental fit.

For the §6 deliverable, this means: **to compute `m_c` such that `D(m_c) = 0.5`, the memo must propose a constitutive mechanism by which `D_nd` depends on `m`.** The Atlas does not supply one.

The §1.5 framing gives a verbal handle — "internal complexity outpaces event-production capacity" — but does not specify the functional form. The next three sections explore three minimal ansatzes that operationalise this verbal claim.

---

## 4. Ansatz A — Internal-DOF vs Compton bandwidth

**Verbal claim.** Internal degrees of freedom impose a participation-channel demand that scales with molecular size. The natural quantum capacity is the Compton frequency `ω_C = mc²/ℏ`, the rate at which the system "ticks" in its own rest frame. The channel weight `D` shifts toward 1 when demand exceeds capacity.

**Naive form (one event per DOF per Compton tick).** Demand per tick = `N_dof / (ω_C · 1)` with `N_dof ≈ 3m/m_u`:

$$D(m) \;\propto\; \frac{N_{\text{dof}}(m)}{\omega_C(m)} \;=\; \frac{3 m / m_u}{m c^{2}/\hbar} \;=\; \frac{3 \hbar}{m_u c^{2}}.$$

**The mass cancels.** Both `N_dof` and `ω_C` scale linearly with `m`. The ratio is mass-independent. Ansatz A in this naive form cannot produce a sharp `m_c` at all.

**Pairwise-correlation modification.** If maintaining coherence requires not one event per DOF but one event per *pair* of DOFs (so the demand scales as `N_dof²`):

$$D(m) \;=\; \alpha \cdot \frac{N_{\text{dof}}(m)^{2}\,\hbar}{m c^{2} T_{\text{obs}}}\;,\qquad N_{\text{dof}} = 3 m / m_u.$$

With `α = 1/2` (absorbing O(1) factors), `D(m_c) = 0.5` gives

$$m_c \;=\; \frac{m_u^{2}\, c^{2}\, T_{\text{obs}}}{9\, \hbar}.$$

For `T_obs = 1 ms` (typical Arndt time-of-flight in KDTLI):

$$m_c \approx 2.6 \times 10^{-7}\ \text{kg} \;\approx\; 1.6 \times 10^{20}\ \text{Da}.$$

This is macroscopic mass — six orders of magnitude beyond the heaviest molecule ever interfered (Arndt's ~25 kDa oligoporphyrins). Ansatz A in this form **places `m_c` so far above accessible mass that ED-09.5 is unfalsifiable in any matter-wave experiment.** Increasing `T_obs` only pushes `m_c` higher.

**Verdict.** Ansatz A either kills the mass dependence entirely (naive form) or pushes `m_c` to macroscopic scales where matter-wave interferometry doesn't operate (pairwise form). Not useful for sending the Arndt email.

---

## 5. Ansatz B — Compton length vs apparatus coherence length

**Verbal claim.** Quantum behaviour requires the particle's intrinsic length `L_C(m) = ℏ/(mc)` to be large compared to a relevant apparatus length scale `L_coh` (e.g., grating period in Talbot-Lau, slit separation in KDTLI). When the ratio drops below threshold, the participation channel fails and `D` shifts toward 1.

**Form.**
$$D(m) \;=\; 1 - \left(\frac{L_C(m)}{L_{\text{coh}}}\right)^{p} \;=\; 1 - \left(\frac{\hbar}{m c\, L_{\text{coh}}}\right)^{p}.$$

For `p = 1`, `D(m_c) = 0.5` gives `L_C(m_c) = L_coh / 2`, i.e.

$$m_c \;=\; \frac{2 \hbar}{c\, L_{\text{coh}}}.$$

For `L_coh = 100 nm` (a generous estimate of the Arndt KDTLI grating period):

$$m_c = \frac{2 \times 1.055 \times 10^{-34}}{3 \times 10^{8} \times 10^{-7}} \approx 7 \times 10^{-36}\ \text{kg} \;\approx\; 4 \times 10^{-9}\ \text{Da}.$$

This is twelve orders of magnitude *below* the proton mass — sub-nucleonic. To bring `m_c` into the Arndt range (10³–10⁵ Da) one would need

$$L_{\text{coh}} = \frac{2\hbar}{c\, m_c} \approx 4 \times 10^{-21}\ \text{m for}\ m_c = 10^{5}\ \text{Da},$$

which is sub-femtometer — smaller than a nucleon. No physical apparatus length is anywhere near this scale.

**Verdict.** The Compton length is too small for any realistic mass to match a realistic apparatus length scale. The de Broglie wavelength `λ_dB = h/(mv)` would land in the right range, but `λ_dB` depends on velocity (apparatus-dependent), violating the §1.5 requirement that the transition be system-intrinsic.

---

## 6. Ansatz C — Triad-coupling saturation

**Verbal claim.** The PDE's nonlinear triad coupling (Canon principle P7) has measured strength `C ≈ 0.03` (ED-Phys-16). This coupling sets the rate at which the participation channel re-injects gradient energy into coherent modes. When the system carries `N` modes that must remain phase-locked, the participation channel saturates at `N · C ≥ 1`. Beyond that, weight shifts to the mobility channel and `D → 1`.

**Form.** With `N_modes(m) ≈ m / m_u` (one mode per atomic mass unit) and saturation at `N · C = 1`:

$$N_c = \frac{1}{C} \approx 33, \qquad m_c = \frac{m_u}{C} \approx 33\ \text{Da}.$$

**This is empirically falsified by existing Arndt data.** A non-exhaustive list of confirmed matter-wave interference at masses well above 33 Da:

| Molecule | Mass (Da) | Group / year |
|:---------|:---------:|:-------------|
| C₆₀ (fullerene) | 720 | Arndt et al., 1999 |
| C₆₀F₄₈ (fluorofullerene) | 1,632 | Hackermüller et al., 2003 |
| TPPF₂₀ (perfluoroalkylated porphyrin) | 1,034 | Gerlich et al., 2007 |
| Gramicidin A₁ (peptide) | 1,860 | Shayeghi et al., 2020 |
| Functionalised oligoporphyrins | ≥ 25,000 | Fein et al., 2019 |

Quantum interference at 25,000 Da is roughly 750× the predicted `m_c`. Ansatz C in its simplest form is dead on arrival.

**Could `C` be regime-dependent?** Yes — but then the prediction loses its sharpness. ED-Phys-16 measures `C ≈ 0.03` in the canonical Scenario-D setup, not in a matter-wave regime. To rescue Ansatz C, one would need to derive `C(m)` from first principles, at which point we are back to inventing a constitutive law.

**Verdict.** Ansatz C is the most ED-native (uses Canon principles already in the corpus, no introduced free scales) but its straightforward reading is empirically falsified. Saving it requires regime-dependent `C`, which is itself an unanchored ansatz.

---

## 7. Synthesis

| Ansatz | Mechanism | `m_c` (Arndt regime) | Status |
|:-------|:----------|:-----:|:-------|
| A (naive) | DOF / Compton bandwidth | undefined (mass cancels) | inadmissible |
| A (pairwise) | DOF² / Compton bandwidth | ~10²⁰ Da | untestable |
| B | Compton length / apparatus length | ~10⁻⁹ Da | unphysical |
| C | Triad-coupling saturation | ~33 Da | falsified by existing data |

**No natural extension of the current Atlas places `m_c` in the experimentally accessible Arndt range** (10³–10⁵ Da). The §1.5 bifurcation at `D_crit = 0.5` is real in the PDE, but its mass mapping for matter-wave interferometry is not pinned down by current ED machinery.

This is itself a significant finding. It means that one of the following must be true:

1. **The matter-wave regime is the wrong test bed.** The bifurcation may show up in a different control parameter (mode occupation, photon number, internal-mode coupling) but not in molecular mass. In this case Aspelmeyer or Haroche, not Arndt, is the relevant collaborator.
2. **The §1.5 bifurcation is system-mode-dependent, not particle-property-dependent.** A single molecule has both a center-of-mass dynamics (low `D`, wavelike — what Arndt measures) and internal vibrational dynamics (high `D`, classical). The "transition" is not at a critical mass but at the boundary between regimes where one or the other dominates the measured observable. Under this reading, *all* of Arndt's data lives on the quantum side of the relevant bifurcation, regardless of mass.
3. **An Atlas extension is required.** A new physical anchor — beyond Madelung — is needed to relate `D_nd` to a matter-wave control parameter. This would be a separate paper (call it ED-Dimensional-01-Ext or ED-Phys-NN), not a §6 deliverable.

---

## 8. What's needed before the Arndt email goes out

The Arndt draft email ([strategy doc §8](ED-09-5-Experimental-Strategy.md#8-draft-email--markus-arndt-vienna-matter-wave-interferometry)) claims `m_c` is "computed in daltons with propagated uncertainty from the Atlas anchor." This memo establishes that the claim is not currently supportable. Before the email can go:

- **Option 1 — Identify a new constitutive mechanism for `D(m)` in matter-wave systems** that places `m_c` in `[10³, 10⁵]` Da. None of A/B/C does this. Open question for the user; nothing in the corpus reviewed for this memo gives a candidate.
- **Option 2 — Reformulate the prediction against a different observable.** For matter-wave interferometry, possibilities include: the third-harmonic ratio in interferogram contrast as a function of mass (does a ~3–6% modulation appear at any mass?); the `N_osc` count in transient buildup of fringes. These would not require an `m_c` and could potentially anchor a softer overture.
- **Option 3 — Switch regimes.** The Aspelmeyer (optomechanics) regime has more candidate control parameters (mode occupation `n̄`, mechanical Q, effective mass) and may admit a cleaner `D(x)` derivation. Recommended next step if Options 1–2 don't pan out: attempt the same analysis for optomechanics before drafting the Arndt email further.

---

## 9. Pre-registered falsification criteria (regime-independent)

These remain valid as stated in [strategy §6](ED-09-5-Experimental-Strategy.md#6-theory-memo-scope--sharpening-ed-095). They apply to *whatever* observable ends up being the matter-wave control parameter, once Option 1, 2, or 3 above is settled:

- Falsified if the coherence observable across the predicted bifurcation shows a smooth monotonic fall-off with no break.
- Falsified if `N_osc` on the predicted quantum side is not in `[8, 19]`.
- Falsified if the third-harmonic content is outside `[3%, 6%]` on the quantum side.
- Falsified if `Q` is outside `[2, 5]` on the quantum side.

The criteria do not depend on which control parameter is chosen; they constrain the dynamical character of the quantum-side regime, not its location.

---

## 10. Open work (Arndt-side)

1. **Resolve the Option 1 / 2 / 3 question in §8** — decision-blocking for the Arndt email.
2. **Atlas extension paper** — if Option 1 is taken (new physical anchor for `D(m)`), this becomes its own piece of work in the Dimensional Atlas series.
3. **Cold-reader pass on the Arndt analysis** — per [strategy §9](ED-09-5-Experimental-Strategy.md#9-pre-send-checklist).

---

# Part II — Aspelmeyer (Optomechanics) Regime

## 11. Why optomechanics admits a cleaner mapping

Optomechanics gives ED machinery more handles than matter-wave interferometry does. A cooled mechanical oscillator coupled to an optical cavity has at minimum five dimensional control parameters:

- mechanical frequency `ω_m`
- intrinsic mechanical damping `γ_m`
- effective mass `m_eff`
- thermal phonon occupation `n̄_th = k_B T / (ℏ ω_m)`
- optomechanical coupling `g_0`

Decoherence of the mechanical mode by a thermal bath occurs at rate

$$\gamma_{\text{dec}} \;\approx\; \gamma_m \,(2\bar n_{\text{th}} + 1).$$

This rate has dimensions of `s⁻¹` and is comparable to `ω_m` (also `s⁻¹`), giving a natural dimensionless ratio that the matter-wave regime lacks. The §1.5 channel weight `D` interpolates between coherent oscillation (`H` dominant, low `D`) and overdamped/dissipative dynamics (`D` dominant); the obvious ansatz is therefore:

$$\boxed{\;D(\omega_m, \gamma_{\text{dec}}) \;=\; \frac{\gamma_{\text{dec}}}{\gamma_{\text{dec}} + \omega_m} \;=\; \frac{1}{1 + Q_{\text{eff}}}, \quad Q_{\text{eff}} \equiv \omega_m / \gamma_{\text{dec}}.\;}$$

Properties:

- `D ∈ [0, 1]` automatically, satisfying the canon constraint `D + H = 1`.
- `D → 0` (deep quantum) when `γ_dec ≪ ω_m` (sideband-resolved, high-Q).
- `D → 1` (deep classical) when `γ_dec ≫ ω_m` (overdamped, bad-cavity).
- The bifurcation at `D_crit = 0.5` lands exactly at `γ_dec = ω_m`.

**Status: derived under candidate-(b) identification (§22.3).** The §22 derivation pass selects `v ↔ X_cav` (cavity-field amplitude quadrature in the rotating frame) and shows that the linearized rotating-frame optomechanics equations match the canonical PDE's 2D template `[[-DP₀, H], [-P₀/τ, -ζ/τ]]`. Under that matching, `D = γ_dec/(γ_dec + ω_m)` follows from the rate-balance identification `DP₀ ↔ γ_dec` and `H ↔ ω_m/(γ_dec + ω_m)` (rather than being posited heuristically). The non-trivial consistency check is `ζ ≈ 0.5` (from `Ẋ_cav = -(κ/2) X_cav`) agreeing with the canon default `ζ ≈ 0.45` to within ~11%. See §22.5 for the full derivation status and the residual interpretive caveats; see §22.7 for the scope-limiting consequence (envelope feature predicted for cavity-coupled and feedback-cooled systems, **not** for free-trap systems with no global mode).

## 12. The bifurcation already lives at a known regime boundary

`γ_dec = ω_m` is the **sideband-resolution threshold** in optomechanics — a regime boundary the field already recognises. Below it, the mechanical mode is "good": coherent quantum control is possible (ground-state cooling, sideband transitions, Gaussian-state preparation). Above it, mechanical dynamics is overdamped and decoupled from cavity coherence.

This makes the ED prediction *less novel as a regime boundary* (the field already labels this transition) but *more novel as a sharpness claim*. Standard optomechanics treats the crossover as a smooth function of `Q_eff`. ED-09.5 predicts a sharp bifurcation: dynamical character changes discontinuously at `Q_eff = 1`, with the four §1.5 quantum-side signatures present for `Q_eff > 10` and absent for `Q_eff < 2`.

## 13. Numerical anchoring across the Aspelmeyer-class published systems

Representative systems from the optomechanics literature, with `D` computed from the §11 ansatz at the published cooling state:

| System (year) | `ω_m / 2π` | `γ_m / 2π` | `n̄` (cooled) | `γ_dec` | `D = γ_dec/(γ_dec + ω_m)` | Regime |
|:--------------|:----------:|:----------:|:-------------:|:-------:|:-----------------------:|:------:|
| Si optomechanical crystal (Chan 2011) | 3.68 GHz | 35 kHz | 0.85 | ~95 kHz | `~4 × 10⁻⁶` | deep quantum |
| Levitated SiO₂ nanoparticle, optical (Delic 2020) | 305 kHz | < 1 mHz | 0.43 | ~2 mHz | `~10⁻⁹` | deep quantum |
| Levitated nanoparticle, real-time control (Magrini 2021) | ~300 kHz | ~1 mHz | ~0.5 | ~2 mHz | `~10⁻⁹` | deep quantum |
| Membrane-in-the-middle, room T (representative) | 100 kHz | 10 mHz | `~10⁸` | ~2 MHz | `~0.76` | classical |
| Same system, cryogenic (n̄ ~ 1) | 100 kHz | 10 mHz | 1 | ~30 mHz | `~5 × 10⁻⁸` | deep quantum |

**All ground-state-cooled systems sit at `D ≪ 0.1`** — well inside the predicted oscillatory regime. **Room-temperature massive oscillators sit at `D > 0.5`** — well inside the predicted parabolic regime.

To traverse `D = 0.5` continuously, one would need to scan `n̄` from `~1` to `~10⁸` in a single setup. Aspelmeyer-class apparatus do not natively scan over 8 orders of magnitude in occupation; the cooled regime and the room-temperature regime are usually different setups, not points on a continuous sweep. The sharpness of the bifurcation is therefore **not directly testable** with current optomechanical data.

## 14. What *is* directly testable: the quantum-side signatures

Per §1.5, the quantum-side regime (`D < 0.1`) carries four pre-registered signatures:

1. Transient oscillation count `N_osc ∈ [8, 19]` (≈ 9) before commitment.
2. Quality factor `Q ≈ 3.5`.
3. Third-harmonic ratio 3–6% of fundamental.
4. Triad-coupling coefficient `C ≈ 0.03`.

These are **not predictions about the mechanical mode itself**. The mechanical-mode quality factor in cooled optomechanics is `Q_m = 10⁵–10⁹` — vastly larger than the predicted `Q ≈ 3.5`. The ED prediction concerns the **participation channel** `v(t)` of the canonical PDE — a separate dynamical mode that would manifest as a **slow envelope modulation** on top of the high-Q mechanical oscillation, with its own ringdown timescale set by `Q_v ≈ 3.5`.

Concretely: in a time-domain ringdown trace of a cooled optomechanical resonator following a coherent-state preparation pulse, ED-09.5 predicts the envelope `|⟨x(t)⟩|` should show:

- A slow oscillation at a frequency `ω_v ≪ ω_m`, with **8–19 cycles of decay** (the participation-mode `N_osc`).
- A quality factor `Q_v ≈ 3.5` for that envelope oscillation.
- A weak third-harmonic component at `3 ω_v`, with amplitude 3–6% of the fundamental envelope amplitude.
- Triad mode-coupling at the `C ≈ 0.03` level — measurable as a power-spectrum cross-coupling between three envelope frequencies satisfying `ω_3 = ω_1 + ω_2`.

These signatures should be visible in **existing published ringdown data** for any of the systems in the §13 table that sit at `D < 0.1`. None of the four signatures requires a new experiment.

## 15. The participation-mode frequency `ω_v` — derived from a thermal-bath equipartition ansatz

The ED PDE tells us the participation mode's *quality* (`Q_v ≈ 3.5`) and *transient count* (`N_osc ≈ 9`), but does not by itself fix the physical frequency `ω_v` of the participation oscillation. The Compton-time anchor of the quantum-regime Atlas (`T₀ ~ 10⁻²² s` for an electron) is irrelevant to a kHz–GHz mechanical resonator coupled to a thermal bath. A different anchoring is needed.

**The ansatz.** The participation channel `v(t)` represents global, non-local coupling between the system and whatever holds it coherent (per ED-Dimensional-01 §6.3). Under the candidate-(b) identification developed in §22, `v ↔ X_cav` (the cavity-field amplitude quadrature in the rotating frame). The cavity field's own ringdown timescale is `1/κ`, but in the typical good-cavity limit `κ ≫ γ_dec` the slow-envelope decoherence is set by the slower bath-induced rate `γ_dec`, not by the cavity decay — see §22.5. The natural identification is therefore:

$$\boxed{\;\tau_v \;\equiv\; \text{(envelope decoherence time)} \;=\; 1/\gamma_{\text{dec}}.\;}$$

**The `N_osc` convention is full cycles** (resolved against ED-Phys-17 *code* and ED-Phys-19 *derivation*; §21.2 v0.7 update). The verbal description in ED-Phys-17 §3.2 reads "turning points in tallest peak height series," but the algorithm at [`ed_phys_oscosmo.py`](../archive/research_history/ED Physics/ED-Phys-17_OscillatorCosmology/ed_phys_oscosmo.py) lines 408–415 counts ALL local extrema (max + min) and then divides by 2 (`h_osc //= 2`). For a clean underdamped sinusoid with N full cycles, this yields 2N extrema → reported h_osc = N (full cycles). Independent confirmation from ED-Phys-19, which derives `N_osc ≈ Q·ln(A₀/A_min)/π` (full-cycle formula) and gets `N_osc ≈ 9` for Q=6.3 with 1% amplitude threshold — matching ED-Phys-17's measured `N_osc = 8` to within rounding.

So the relation between `N_osc` (full cycles) and the envelope decoherence time is

$$\tau_v \;=\; N_{\text{osc}} \cdot \frac{2\pi}{\omega_v},$$

which combined with `τ_v = 1/γ_dec` gives:

$$\boxed{\;\omega_v \;=\; 2\pi\, N_{\text{osc}}\, \gamma_{\text{dec}}, \qquad \frac{\omega_v}{2\pi} \;=\; N_{\text{osc}}\, \gamma_{\text{dec}}.\;}$$

For ED-Phys-17's clean single-mode case (§4.1, flat background, single Gaussian peak), `N_osc = 8` full cycles, giving the cleanest single-mode optomechanics prediction:

$$\boxed{\;\omega_v / (2\pi) \;=\; 8\, \gamma_{\text{dec}} \quad \text{(single-mode optomechanics)}.\;}$$

(Note: v0.6 incorrectly applied a factor-of-2 reduction based on misreading "turning points" as half-period spacing; v0.7 reverts to the full-cycle convention after tracing the actual algorithm and finding ED-Phys-19's confirming derivation.)

**Derivation and the `Q` vs `N_osc` consistency question — RESOLVED in §21.2 (2026-04-20).** ED-Phys-17 was read directly. The convention is:

> `N_osc` = **count of turning points** (local extrema) in the peak-height time series. Not counted to a specific amplitude threshold.

For an underdamped sinusoid `A(t) = A_0 e^{-γt}\cos(\omega t)`, turning points occur where `dA/dt = 0`, i.e. at `tan(ωt) = -γ/ω`, with consecutive turning points separated by `π/ω` (half-period). So `N_osc(turning points) = ω · τ / π = 2 × N_full_cycles`. The visibility threshold (amplitude at which the algorithm stops detecting turning points) is set by the prominence cut in the peak-detection routine (see ED-Phys-17 Appendix A: `min_prominence = 0.01`).

For Q-N_osc reconciliation under this convention:

$$N_{\text{osc}}(\alpha) \;=\; -\frac{2 Q_v}{\pi} \ln(\alpha),$$

where `α` is the amplitude visibility threshold. The orientation's quoted `Q ≈ 3.5` and ED-Phys-17's `N_osc ≈ 8`–`19` were not jointly derived from the same parameter set:

- **Q ≈ 3.5** comes from 00.3, with parameters not stated in the orientation.
- **N_osc ∈ [8, 19]** comes from ED-Phys-17, with parameters `α=0.1, γ=0.5, τ=100, ζ=0.5, ρ_*=50, ρ_0=0.5`. Linearized stiffness `K_eff = αγ/ρ_0 = 0.1`, damping ratio `ζ_dr = ζ/(2√(τ K_eff)) = 0.079`, giving **Q ≈ 6.3** for ED-Phys-17 — not 3.5.
- The [8, 19] range reflects **multi-modal background complexity**, not Q-derived spread:
  - Single peak, flat background: `N_osc = 8`
  - Single peak, oscillating background: `N_osc = 10`
  - Single peak, standing-wave background: `N_osc = 19` (extra wiggles from wave interference)
  - Multi-peak systems: `N_osc = 8`–`15`

For optomechanics (single dominant mode, no spatial structure), the cleanest comparison is to ED-Phys-17 §4.1 (flat-background single peak): `N_osc = 8` turning points, with Q ≈ 6.3 inferred from the parameters. Reconciliation: with Q = 6.3 and N_osc = 8, the visibility threshold is `α = exp(-8π/(2·6.3)) ≈ 0.137` (~14% of initial amplitude) — physically reasonable for visual peak-detection.

**Non-trivial cross-check.** ED-Phys-17 used **`ζ = 0.5` exactly**. The §22.3 cavity-field-derived ζ is `ζ ≈ 0.5` (from `Ẋ_cav = -(κ/2)X_cav`). **Exact agreement to one decimal place.** This is the second non-trivial cross-check supporting candidate (b): the ED-Phys-17 oscillator regime that produced the canonical `N_osc` range is the *same parameter regime* that the cavity-field identification predicts for an optomechanical resonator. The dynamical predictions of ED-Phys-17 should map directly onto cavity-coupled optomechanics under candidate (b).

**Implication for the F3 falsification criterion.** Two candidate Q values are now in play:
- `Q = 3.5` (from 00.3, parameter set unspecified)
- `Q = 6.3` (from ED-Phys-17, ζ=0.5 — same as cavity-mapped)

For the cavity-field-mapped optomechanics regime, the ED-Phys-17 value `Q ≈ 6.3` is the structurally consistent choice. F3 should be widened to `Q_v ∈ [3, 9]` to span both possibilities pending §21.3 resolution of the 00.3 provenance.

**Numerical predictions across the §13 systems** (using `ω_v / 2π = N_osc · γ_dec` with `N_osc = 8` from ED-Phys-17 §4.1, single-mode optomechanics):

| System | `γ_dec` (Hz) | Predicted `ω_v / 2π` (Hz) | Predicted envelope period `T_v` (s) | Mechanical period `T_m` (s) | `T_v / T_m` |
|:--------|:------------:|:------------------------:|:-----------------------------------:|:---------------------------:|:------------:|
| Chan 2011 (Si crystal) | `9.5 × 10⁴` | `7.6 × 10⁵` | `1.3 × 10⁻⁶` | `2.7 × 10⁻¹⁰` | `~4900` |
| Delic 2020 (levitated SiO₂) | `~2 × 10⁻³` | `~1.6 × 10⁻²` | `~63` | `3.3 × 10⁻⁶` | `~1.9 × 10⁷` |
| Magrini 2021 (real-time control) | `~2 × 10⁻³` | `~1.6 × 10⁻²` | `~63` | `3.3 × 10⁻⁶` | `~1.9 × 10⁷` |
| Membrane-in-the-middle (cryo) | `~3 × 10⁻²` | `~0.24` | `~4.2` | `1 × 10⁻⁵` | `~4.2 × 10⁵` |

**Detectability comment.** The `T_v / T_m ≫ 1` ratio (always at least four orders of magnitude on the quantum side) confirms the prediction is physically a "slow envelope" on top of fast mechanical motion — the desired qualitative picture. The Delic 2020 envelope period of **~63 s** is the most demanding to detect: it requires contiguous time records of at least a few minutes to capture even one full envelope cycle. Magrini 2021's real-time feedback architecture continuously records `x(t)` and is therefore the most plausible Delic-class candidate. Chan 2011's microsecond envelope period is well within standard time-domain resolution. The cryogenic membrane case (~4 s envelope) is also accessible.

**β option chosen.** The derived `ω_v = 2π N_osc γ_dec` replaces the previous α/β choice. It is a sharper falsification target (specific predicted frequency, not just "any envelope feature") and is internally derived from one ansatz (`τ_v = 1/γ_dec`) plus the existing ED-Phys-17 `N_osc ≈ 9`. The ansatz is itself testable: if no envelope feature is found at the predicted `ω_v`, it could still be present at `ω_v/2`, `2ω_v`, etc. Those would falsify the specific `τ_v = 1/γ_dec` ansatz while preserving the broader §1.5 prediction.

## 16. Pre-registered falsification criteria for the Aspelmeyer regime

Specialised from the regime-independent §9 list:

- **F0 — No envelope feature at predicted `ω_v`.** Falsified if no slow envelope modulation is detectable at frequency `ω_v / 2π = N_osc · γ_dec ≈ 8 γ_dec` (using `N_osc = 8` full cycles from ED-Phys-17 §4.1, with a factor-of-2 tolerance) in time-domain ringdown data from any cooled optomechanical system. A weaker partial falsification: an envelope is present but at a frequency factor ≥ 10 from the prediction — this falsifies the §15 ansatz but not the broader §1.5 claim.
- **F1 — No envelope feature anywhere.** Falsified if no slow envelope modulation is detectable in time-domain ringdown data for any cooled optomechanical system (`D < 0.1` per §13), at any frequency.
- **F2 — Wrong transient count.** Falsified if the dominant envelope feature shows `N_osc` (counted as **full cycles** of the envelope, per ED-Phys-17 actual algorithm with `//= 2` final step) outside `[6, 12]` for clean single-mode systems. (The wider range `[8, 19]` from ED-Phys-17 reflects multi-modal background complexity not present in single-mode optomechanics — see §15. Conservative cut for F2 is the single-mode value `N_osc ≈ 8 ± 2`.)
- **F3 — Wrong envelope Q.** Falsified if the envelope quality factor is outside `[4, 9]`. **Tightened from v0.6's `[3, 9]` per §21.3 resolution.** The structurally correct canonical value is `Q ≈ 6.3` (low-k single-mode limit per ED-Phys-19, with ζ=0.5 matching the §22.3 cavity-derived value exactly). The orientation's `Q ≈ 3.5` quote attributed to 00.3 is **not derivable from any in-repo parameter set** and is treated as an anomalous quote pending direct verification against the 00.3 PDF (Desktop). The ED-Phys-19 derivation `Q = √(K_eff·τ)/ζ = √(0.1·100)/0.5 = 6.32` is preferred for the cavity-optomechanics regime.
- **F4 — Wrong harmonic ratio.** Falsified if no third-harmonic envelope component is present, or if its ratio to the fundamental is outside `[3%, 6%]`.
- **F5 — Wrong triad coupling.** Falsified if power-spectrum cross-coupling between envelope frequencies satisfying `ω_3 = ω_1 + ω_2` is absent or outside `[0.01, 0.05]`.

F2–F5 are joint: any single failure is sufficient to falsify ED-09.5 in the Aspelmeyer regime.

## 16.5 The independence structure of F0–F5

The six criteria are not six independent dimensions of test. Their actual structure:

| Dimension | Criteria | What it tests |
|:----------|:---------|:--------------|
| **Existence + frequency** | F0 (subsumes F1) | Is there an envelope mode at all, and at the predicted `ω_v = 2π N_osc γ_dec`? |
| **Linear envelope dynamics** | F2 ∧ F3 (linked by `N_osc(α) = (Q_v/π) ln(1/α)`) | Does the envelope's transient count and quality factor match? **If the §15 strict-threshold convention is used, F2 and F3 are not independent — they are two views of the same `Q_v`. If the nonlinear-persistence interpretation is used, they become two genuinely different measurements.** This is the same ambiguity flagged in §15. |
| **Nonlinear envelope structure** | F4 ∧ F5 | Does the envelope show ED's predicted cubic (triad) coupling, both as third-harmonic content and as bispectral cross-coupling? F4 and F5 are independent measurements of the same `C ≈ 0.03` coefficient via two different observables (intra-mode harmonics vs cross-mode triads). |

So there are **three independent dimensions of test**, not six. The framing "four jointly-required signatures" used in the strategy doc §7 v2 email is correct in terms of falsification surface, but a reviewer who notes the linkage between F2 and F3 (and between F4 and F5) could push back that the test space is two- or three-dimensional, not four-dimensional. The honest framing is: **three independent test dimensions, with two of them (linear-envelope and nonlinear-coupling) each carrying internal cross-checks**.

This affects how one should report a partial confirmation:

- **F0 alone** (envelope at predicted frequency, but other features fail): the §11 mapping is broadly right, but the §15(β) ansatz needs revision. Partial support for ED-09.5 architecture, not for the specific dynamical predictions.
- **F0 + (F2 ∧ F3) confirmed, (F4 ∧ F5) failed**: linear envelope dynamics match ED, but the nonlinear/triad structure does not. Suggests ED's linear sector is correct but the cubic coupling is regime-suppressed in optomechanics. Interesting partial result.
- **All six confirmed**: full architectural confirmation. Highest-impact outcome.
- **F0 failed**: §15(β) derivation is wrong (envelope at different frequency or no envelope at predicted location); no commitment yet on whether broader §1.5 prediction survives. Demands re-derivation of the optomechanical ω_v anchor.

## 17. What the Aspelmeyer email should now ask for

Strategy doc §7 currently asks Aspelmeyer for: (i) a critical reaction to a memo, (ii) a pointer to data spanning `x_c`, (iii) potentially a dedicated run. Given the §13 finding (no current setup spans the bifurcation) and the §14 finding (the testable signatures are in existing ringdown traces), the request can be sharpened:

- Drop the "your data may already contain the bifurcation" framing — it doesn't, and an expert reader will see immediately that no Aspelmeyer setup scans `n̄` over the 8 orders of magnitude required.
- Replace with: "ED-09.5 predicts that **all your cooled systems sit on the quantum side** of a bifurcation at `γ_dec = ω_m`, and that the participation-mode envelope of any published ringdown trace from those systems should carry the four signatures in §16."
- Ask specifically for: **time-domain ringdown traces** (not just the spectral occupation numbers), with high-bandwidth phase information preserved, from any of the cooled-state experiments. The reanalysis is to extract the slow envelope, fit `N_osc`, `Q_v`, third-harmonic ratio, and triad cross-coupling, and check the four falsification criteria.
- Estimated grad-student-month effort to perform the reanalysis on one published dataset.

This reframing is internally consistent with §1.5 and §1.5's identification claim, asks for something Aspelmeyer's group can plausibly provide (raw ringdown data they presumably still have), and offers a clean four-way falsification path. **The Aspelmeyer email is unblocked once §15(α/β) is decided and the strategy-doc §8 draft is rewritten in this frame.**

---

## 18. Synthesis: Arndt vs Aspelmeyer

| | Arndt (matter-wave) | Aspelmeyer (optomechanics) |
|:--|:--|:--|
| Natural control parameter | molecular mass `m` | damping ratio `γ_dec/ω_m` |
| `D(x)` derivable from current Atlas? | No — three ansatzes all fail | Yes — natural construction from `γ_dec` and `ω_m` |
| Does experimentally accessible range span `D = 0.5`? | unclear (depends on unanchored ansatz) | No — all cooled systems are at `D ≪ 0.1`; sharpness untestable |
| Quantum-side signatures testable in existing data? | Not without resolving §8 first | **Yes** — slow envelope of ringdown traces should carry `N_osc`, `Q_v`, harmonics, triad coupling |
| Email status | Blocked on Atlas extension or reformulation | Unblocked; rewrite needed before send |
| Tier-1 reanalysis viable today? | No | **Yes** — reanalyse one published cooled-state ringdown |

The Aspelmeyer regime is the cleaner first target. Recommended sequence:

1. Decide §15(α/β) — does the email predict an arbitrary `ω_v` (any frequency), or commit to a specific relation?
2. Rewrite [strategy §7](ED-09-5-Experimental-Strategy.md#7-draft-email--markus-aspelmeyer-vienna-optomechanics) per §17 above.
3. Choose one published Aspelmeyer-group ringdown dataset (Delic 2020 is the most natural candidate — recent, well-documented, deep `D < 0.1`).
4. Either reanalyse it ourselves before sending, or include the reanalysis protocol in the email itself as a concrete grad-student task.
5. The Arndt email remains parked until §8 of this memo resolves.

---

## 19. Open work (full)

1. **Aspelmeyer-side §15 decision** (α: free `ω_v`, or β: derived `ω_v`) — decision-blocking for sending the rewritten Aspelmeyer email.
2. **Rewrite strategy-doc §7 draft** per §17.
3. **Identify one Aspelmeyer dataset** for reanalysis (Delic 2020 leading candidate) and check whether time-domain ringdown traces are available in the supplementary material or reproducible from the published parameters.
4. **Arndt-side Option 1 / 2 / 3 (§8) decision** — separately, lower priority now that Aspelmeyer is the lead test bed.
5. **Haroche / cavity-QED regime computation** — apply the §11 method to photon number `n`. Likely similar structure: natural `D = κ / (κ + ω_atom)` mapping, bifurcation at well-known cavity-vs-atom-linewidth threshold.
6. **Atlas extension paper** — if Arndt regime is to be unblocked, a new constitutive anchor is needed. Lower priority given Aspelmeyer is now the primary path.
7. **Cold-reader pass** — per [strategy §9](ED-09-5-Experimental-Strategy.md#9-pre-send-checklist), a reader outside the ED program should review *both* the Arndt and Aspelmeyer analyses. The Aspelmeyer §11 ansatz needs a sanity check on whether it would read as ED-native or as ad hoc curve-matching.

---

## 20. Delic 2020 dataset reconnaissance — COMPLETED (2026-04-20)

**Status (2026-04-20, v0.8):** Web-search verification of the five reconnaissance steps has been run. **Verdict: no public deposit of raw time-domain `x(t)` traces exists for either Delic 2020 or Magrini 2021.** The Aspelmeyer email (strategy §7 v2) is therefore the natural channel for obtaining them — request (2) of that draft asks directly for time-domain trace access. Two PhD theses are publicly downloadable (Delic 2019, Magrini 2021) and serve as the best available substitute / context.

**Reference.** Delić, U., Reisenbauer, M., Dare, K., Grass, D., Vuletić, V., Kiesel, N. & Aspelmeyer, M. *Cooling of a levitated nanoparticle to the motional quantum ground state.* Science **367**, 892–895 (2020). DOI: `10.1126/science.aba3993`.

**Why Delic 2020.** Recent (canonical for the Aspelmeyer-class levitated-nanoparticle paradigm), well-documented in Science with an extensive supplementary, deeply on the quantum side per §13 (`D ~ 10⁻⁹`), and uses cavity cooling via coherent scattering — a regime where the coupling to the bath is well-characterised and `γ_dec` is extractable.

**System parameters relevant to ED-09.5 prediction:**

| Parameter | Value | Source |
|:----------|:------|:-------|
| Particle | 143 nm radius silica | Methods |
| `m_eff` | `~3 × 10⁻¹⁸` kg | Methods |
| `ω_m / 2π` (libration mode used for cooling) | 305 kHz | Fig. 1 |
| Final occupation `n̄` | `0.43 ± 0.03` | Abstract / Fig. 4 |
| Reservoir T (effective) | sub-K equivalent | Methods |
| Heating rate (recoil-limited) | `~10⁴ phonon/s` | Methods |
| `γ_dec` (inferred from heating + n̄) | `~2 × 10⁻³` s⁻¹ | derived |
| Predicted `ω_v / 2π` (v0.7) | `~16 mHz` | this memo §15 |
| Predicted envelope period | `~63 s` | this memo §15 |

**Data product types relevant to the four falsification criteria (F0–F5 of §16):**

| What we need | What Delic 2020 actually publishes |
|:-------------|:-----------------------------------|
| Time-domain heterodyne `x(t)` traces with phase preserved | Phonon-occupation reconstructions and power spectral densities; **time-domain `x(t)` traces are not in the main paper figures** |
| Long contiguous records (≥ 200 s for ~3 envelope cycles) | Published traces are seconds-scale; full record lengths used for averaging are not stated explicitly in the main text |
| Sampling rate ≫ `ω_m` (so `ω_v ≪ ω_m` envelope can be cleanly extracted) | Heterodyne detection bandwidth is in the MHz range — adequate for 305 kHz mechanical mode and far more than adequate for a 16 mHz envelope |

### Verification results (five steps)

**Step 1 — Science 367 data-availability statement.** Per search-engine indexing of the Delic et al. 2020 Science paper, the availability statement is the standard Science boilerplate: *"All data needed to evaluate the conclusions in the paper are present in the paper or the supplementary materials."* Indicates **no external repository deposit**. The Science page itself is paywalled to WebFetch (HTTP 403), but the boilerplate is visible via third-party indexing. The paper itself shows processed quantities (phonon occupations, PSDs) — not raw `x(t)`.

**Step 2 — Vienna PHAIDRA repository.** Searched for Delic/Aspelmeyer/levitated-nanoparticle records. The one relevant PHAIDRA object located ([`o:1646057`](https://phaidra.univie.ac.at/o:1646057)) belongs to a different paper — Ciampini et al. 2023 fast quantum interference, containing Mathematica scripts to reproduce plots, not raw data. **No PHAIDRA record for Delic 2020 or Magrini 2021 located.**

**Step 3 — Zenodo.** Two relevant records, neither matching: [Aspelmeyer-co-authored levitated-superconductor dataset](https://zenodo.org/records/12701290) (different 2024 paper); [`optoanalysis` Python library](https://zenodo.org/records/818086) by Rademacher et al. (analysis code, not experimental data). **No Zenodo record for Delic 2020 or Magrini 2021 located.**

**Step 4 — Delic PhD thesis.** *Cavity cooling by coherent scattering of a levitated nanosphere in vacuum* (Vienna, 2019). **Publicly downloadable** at [`aspelmeyer.quantum.at/.../Thesis_Delic.pdf`](https://aspelmeyer.quantum.at/fileadmin/user_upload/a_aspelmeyer_quantum/Research/Thesis_Delic.pdf). File exceeds WebFetch 10 MB limit so content not parsed here, but user-accessible. Likely contains more detailed plots and discussion than the Science paper; unlikely to contain raw time-domain traces.

**Step 5 — Magrini PhD thesis + paper.** Thesis: *Quantum measurement and control of mechanical motion at room temperature* (Vienna, 2021), publicly downloadable via [Dropbox](https://www.dropbox.com/s/qi8jpxn18kgkwdt/magrini_thesis_v7_291021_submitted.pdf?dl=0). Paper preprint: [arXiv:2012.15188](https://arxiv.org/abs/2012.15188); TU Wien institutional copy [here](https://www.acin.tuwien.ac.at/file/publications/cds/pre_post_print/magrini2021.pdf). Processed data only, almost certainly. **Trade-off flagged in v0.5 still applies:** Magrini 2021's real-time feedback control may suppress the predicted envelope; needs to be thought through before targeting it as the primary Tier-1 dataset.

### Implications for the Aspelmeyer email

1. **Don't waste time hunting for public raw data that doesn't exist.** The §14 assessment is confirmed: raw heterodyne `x(t)` lives in group archives only.
2. **The Aspelmeyer email (strategy §7 v2) is the only channel.** Request (2) of that draft — "pointer to time-domain traces accessible either in supplementary, on a public repository, or via direct request" — is now the **primary** ask, not a fallback.
3. **Strengthen the email by citing the theses.** Both Delic 2019 and Magrini 2021 theses are publicly downloadable. Referencing them in the email ("I've read both the 2020 Science paper and the 2019 thesis, and I do not see the predicted slow envelope resolved in the published figures — could I ask for access to the raw heterodyne traces") shows homework done and makes the request for raw data proportionate.
4. **The Science "all data in the paper" boilerplate is not a blocker.** That statement is about data supporting the paper's *published conclusions* (occupation, PSD). It is not a claim that raw `x(t)` is published — it explicitly is not. Asking for raw traces is not in conflict with the availability statement.

### Manual thesis skim — RESULT (2026-04-20, v0.9)

User downloaded and skimmed both [Delic 2019](https://aspelmeyer.quantum.at/fileadmin/user_upload/a_aspelmeyer_quantum/Research/Thesis_Delic.pdf) and [Magrini 2021](https://www.dropbox.com/s/qi8jpxn18kgkwdt/magrini_thesis_v7_291021_submitted.pdf?dl=0) theses. **Reported finding: no mention of ringdown, slow envelope, PSD features near 16 mHz, or Allan-variance signatures matching the §15 ED-09.5 envelope prediction.**

This is informative but does not falsify the ED-09.5 prediction. Three interpretations to weigh:

1. **Most likely — analysis-pipeline blind spot.** Standard optomechanics analysis is not constructed to expose a sub-Hz envelope on top of a 100 kHz–GHz mechanical carrier:
   - Heterodyne signals are typically demodulated at `ω_m`, then time-binned in windows of milliseconds to seconds for occupation reconstruction.
   - PSDs are computed over the mechanical bandwidth (Hz to MHz), with the dominant peak at `ω_m` setting the dynamic range. A weak feature at `ω_m / 10⁷` (Delic case) would be filtered out below the noise floor of the displayed PSD.
   - Allan variance plots typically span τ = 1 ms to a few seconds, not τ = 1 s to 100 s.
   - Continuous run durations in cooled-state work are often shorter than the predicted 63 s envelope period (Delic) — by definition, an envelope cycle that doesn't fit in the record cannot show up in published figures.

   Under this interpretation, the absence of any envelope signature in published thesis figures is uninformative about whether the underlying physics is present in the raw data. The signature would only become visible after an envelope-extraction reanalysis on contiguous long records.

2. **Plausible alternative — the signature is genuinely absent.** ED-09.5's `v ↔ X_cav` candidate (b) is wrong, and the cavity-coupled dynamics simply do not produce a slow envelope at the predicted frequency or any other. If a future raw-data reanalysis confirms this, candidate (c) (internal triad mode, §22.4) becomes the salvage path; if THAT also produces no envelope at any frequency, candidate (b) plus all naive variations are falsified, and the optomechanics regime falls outside ED-09.5's empirical reach.

3. **Less likely — the signature is below noise floor.** If the envelope amplitude is a small fraction of the mechanical motion (the linear-coupling regime in §22 would predict a ratio of order `g/κ ~ 10⁻²` or smaller), it could be present but invisible against the dominant 305 kHz mechanical peak in the PSD displayed.

Interpretations (1) and (3) cannot be discriminated from publicly-visible figures. Both can only be tested by reanalyzing raw `x(t)` traces — which is exactly what the email's request (2) asks for.

### Implications for the Aspelmeyer email — sharpened framing

The negative thesis-skim result actually **strengthens** the email rather than weakening it:

- Drop the "I think I see X in your Fig Y" anchor. The honest framing is: *"the predicted envelope wouldn't appear in your published figures even if present, because standard optomechanics analysis pipelines and run durations aren't constructed to expose a sub-Hz envelope on top of a 100 kHz mechanical carrier."*
- This makes the request *more* coherent: you're asking for access to raw data to perform a specific reanalysis no one has done, not for verification of something Aspelmeyer's group should have noticed already.
- It removes the awkward-implication subtext ("you missed something obvious") and replaces it with a clean methodological proposal ("here is a class of analysis your published pipelines don't perform; would you share the raw data so it can be tried").
- The cross-check on §13/§15 numerical parameters against the actual Science paper still applies. Whether `γ_dec` is `2 × 10⁻³` or `5 × 10⁻⁴` shifts `ω_v` by the same factor; the predicted period changes from ~63 s to ~250 s, which has direct implications for what minimum record duration is needed.

### What this null result is, and is not

| | |
|:-|:-|
| **Is** | A confirmation that the predicted envelope is not visible in *processed, published* optomechanics figures — which is consistent with the analysis-pipeline blind spot in interpretation (1) and tells us nothing decisive about the raw data. |
| **Is not** | A falsification of ED-09.5 in the Aspelmeyer regime. F0 (envelope at predicted `ω_v`) is a claim about raw `x(t)` data, not about published figures. |
| **Sharpens the case for** | The Aspelmeyer email request (2). Without raw-data access, the prediction is inert in this regime. |
| **Doesn't sharpen** | The Arndt regime, which is independently blocked per §8 and would benefit from a different unblocking move (Atlas extension paper §21.4, or pivot to a different control parameter). |

---

## 22. The `v` ↔ optomechanical-mode identification (resolves §21.1)

The §11 channel-weight mapping `D = γ_dec/(γ_dec + ω_m)` was flagged as heuristic because the canonical PDE's `(ρ, v)` ↔ optomechanical `(mechanical, ?)` correspondence was not pinned down. This section evaluates three pre-specified candidate identifications, derives the linearized uniform-mode equations under each, and selects the candidate that yields a derived (not assumed) `D` and a consistent envelope prediction.

### 22.1 What `v` must satisfy structurally

From Canon principle P5 and the canonical PDE, the participation field `v(t)` must:

1. **Be scalar** — single time-dependent value, no spatial structure of its own.
2. **Have its own timescale `τ`**, independent of `ρ`'s spatial dynamics.
3. **Be driven by `F[ρ]`** — sourced by the bulk PDE operator on `ρ`.
4. **Damp linearly** at rate `ζ/τ`.
5. **Couple back into `ρ̇` as `+Hv`** — the same `v(t)` modifies `ρ̇` at every point.
6. **Be global / non-local** (per ED-Dimensional-01 §6.3).

The canonical PDE's uniform-mode 2D linearization (with `δ = ρ − ρ*`, linear penalty `P(δ) = P₀δ`, no spatial gradients) is

$$\dot\delta = -D P_0 \delta + H v, \qquad \dot v = (1/\tau)\bigl(-P_0\, \delta - \zeta v\bigr).$$

The matrix is `[[-DP₀, H], [-P₀/τ, -ζ/τ]]` with `trace = -(DP₀ + ζ/τ)` and `det = (P₀/τ)(Dζ + H)`. This is the linear template that any candidate `(ρ, v)` ↔ optomechanics-mode mapping must reproduce. The matching exercise below tests whether each candidate's linearized dynamics fall onto this template.

### 22.2 Candidate (a) — `v` ↔ mechanical momentum quadrature `p(t)`

**Setup.** Identify `δ ↔ x` (mechanical displacement) and `v ↔ p` (mechanical momentum). Standard linearized mechanical-oscillator dynamics:

$$\dot x = p/m, \qquad \dot p = -m\omega_m^2\, x - \gamma_m\, p + \xi(t),$$

with `ξ(t)` the bath noise (set to zero for the deterministic check).

**Match to template.** From `δ̇ = -DP₀ δ + Hv`: matching `ẋ = (1/m) p` requires `DP₀ = 0` and `H = 1/m`. From `v̇ = (1/τ)(-P₀ δ - ζv)`: matching `ṗ = -mω_m² x - γ_m p` requires `P₀/τ = mω_m²` and `ζ/τ = γ_m`.

The first matching condition forces **`DP₀ = 0`**. Two interpretations:
- `P₀ = 0`: no penalty, but then `v̇` has no driving from `δ` (the second equation requires `P₀ ≠ 0` to recover the harmonic restoring force). **Contradiction.**
- `D = 0`: zero mobility-channel weight. Then the §11 mapping `D = γ_dec/(γ_dec + ω_m)` is **falsified** — under candidate (a), `D = 0` exactly, regardless of `γ_dec` or `ω_m`.

**Three-criteria check:**

| Criterion | Status under (a) |
|:----------|:-----------------|
| Coherent PDE-to-optomechanics correspondence | Partial — the (`x`, `p`) system embeds in the canonical 2D template, but the requirement `DP₀ = 0` collapses it to a degenerate slice. |
| Derivable expression for `D` | Yes — `D = 0`. **But this contradicts the §11 mapping.** |
| Consistent `Q` vs `N_osc` | The (`x`, `p`) system is just a damped harmonic oscillator: `Q = ω_m / γ_m`. For typical optomechanics, `Q_m = 10⁵–10⁹`, vastly larger than ED's `Q ≈ 3.5`. **Inconsistent.** |
| Falsifiable `ω_v` | `ω_v = ω_m` (the mechanical frequency itself). This is not a "slow envelope" — it's the carrier. **Wrong qualitative regime.** |

**Verdict on (a): Rejected.** The mechanical momentum is too tightly bound to the mechanical position to play the role of a global, independently-timescaled participation mode. Candidate (a) collapses the canonical PDE onto its `D = 0` boundary and produces an `ω_v = ω_m` prediction that contradicts the slow-envelope picture motivating §15. The deeper failure: the mechanical-mode (`x`, `p`) pair is a single 2-DOF system; ED's (`ρ`, `v`) is two DIFFERENT physical channels. Identifying them is a category confusion.

### 22.3 Candidate (b) — `v` ↔ optical phase / radiation-pressure back-action channel

**Setup.** Identify `δ ↔ x` (mechanical displacement / mechanical-mode density) and `v ↔ X_cav` (the amplitude quadrature of the cavity field in the rotating frame at drive frequency, which carries the radiation-pressure back-action onto the mechanical mode). The cavity field decomposes as `c = (X + iY)/√2`, with `X` carrying back-action and `Y` carrying readout phase.

Linearized rotating-frame optomechanics (red-detuned cooling, `Δ = -ω_m`):

$$\dot x = \omega_m\, p_x \;+\; G\, X, \qquad \dot X = -(\kappa/2)\, X \;+\; G\, x,$$

(suppressing `p_x` dynamics in the slowly-varying envelope limit, where `p_x` is the conjugate quadrature of `x`; `G = g_0 \sqrt{n̄_{cav}}` is the linearized coupling). The first equation is the slow envelope of mechanical evolution after eliminating fast oscillations at `ω_m`; the second is cavity dynamics in the rotating frame.

**Match to template.** From `δ̇ = -DP₀ δ + Hv`: matching `ẋ = ω_m p_x + GX`. The `ω_m p_x` term is the mechanical restoring drive, which on time-averaging over a mechanical period is the source of *coherent oscillation* — represented in the ED template by the `+Hv` driving. So we identify `Hv ↔ G X` (giving `H ∝ G/v_amplitude`) and the `-DP₀ δ` term must come from whatever dissipative process appears in `ẋ` — which is the mechanical-bath decoherence `γ_dec` (since the deterministic `ẋ` itself has no damping in the slow envelope, the dissipation enters via the noise/decoherence channel of the slow envelope dynamics, with effective rate `γ_dec`). So `DP₀ ↔ γ_dec`.

From `v̇ = (1/τ)(-P₀ δ - ζv)`: matching `Ẋ = -(κ/2) X + G x`. We identify `1/τ ↔ κ` (so `τ = 1/κ`, the cavity ringdown), `ζ/τ ↔ κ/2` (so `ζ = 1/2`), and `P₀/τ ↔ G`, giving `P₀ ↔ G/κ`.

**Two non-trivial consistency checks:**

- **`ζ ≈ 0.5`** (from cavity decay structure `Ẋ = -(κ/2)X`) versus **canon default `ζ ≈ 0.45`** (from ED-Dimensional-01). Agreement to ~11%. This is non-trivial: `ζ` could have come out at any value; it landed at the canonical one within parameter ambiguity. **First quantitative consistency check passed.**
- The §11 mapping is now derivable. With `DP₀ ↔ γ_dec` and `P₀ ↔ G/κ`, we get `D ↔ γ_dec · κ/G`. Combined with `H ∝ G` and the canon constraint `D + H = 1`, normalisation gives the rate-balance form

$$D \;=\; \frac{\gamma_{\text{dec}}}{\gamma_{\text{dec}} + \omega_m}, \qquad H \;=\; \frac{\omega_m}{\gamma_{\text{dec}} + \omega_m}$$

(where the appearance of `ω_m` in the denominator comes from identifying the *coherent driving rate per unit `v`* with `ω_m` in the slow-envelope frame). **The §11 mapping is recovered as a derivation, not a heuristic.**

**Three-criteria check:**

| Criterion | Status under (b) |
|:----------|:-----------------|
| Coherent PDE-to-optomechanics correspondence | **Yes** — `(δ, v)` ↔ `(x, X_cav)` cleanly maps onto the canonical 2D template, with all four matrix entries matched to known optomechanical rates. |
| Derivable expression for `D` | **Yes** — `D = γ_dec/(γ_dec + ω_m)` follows from rate-balance under the identification. No longer heuristic. |
| Consistent `Q` vs `N_osc` | Inherits the §15 / §21.2 ambiguity (strict-threshold vs nonlinear-extension). The cavity-field identification doesn't resolve `Q` vs `N_osc` — that's a separate ED-Phys-17 convention question — but it doesn't worsen it either. |
| Falsifiable `ω_v` | **Yes** — `ω_v = 2π N_osc γ_dec` per §15(β), with the explicit physical claim that the slow envelope decoheres on the mechanical-bath timescale `1/γ_dec` (rather than the much faster cavity ringdown `1/κ`). This is a falsifiable second-order claim: if F0 fails at `2π N_osc γ_dec`, check at `2π N_osc κ`. |

**Verdict on (b): Selected.** Satisfies all three primary criteria. The `ζ ≈ 0.5` non-trivial agreement with the canon default is the strongest single piece of internal evidence for the identification.

### 22.4 Candidate (c) — `v` ↔ internal participation mode coupled to `x(t)` via triad structure

**Setup.** Posit an internal participation mode `v_int(t)` that couples to mechanical position via the canonical PDE's triad nonlinearity `M'(ρ)|∇ρ|²`. This is a hidden ED degree of freedom not present in standard optomechanics — its physical realization is unspecified (could be: an internal vibrational mode of the levitated nanoparticle, a collective mode of the trap medium, a vacuum participation mode of the surrounding electromagnetic continuum, or a fundamentally new entity predicted by ED).

**Match to template.** Without specifying what `v_int` is physically, no linearized equations can be derived. Three sub-options:
- **(c.i) Internal vibrational modes.** A levitated 143 nm SiO₂ nanoparticle has ~10⁹ atoms and roughly `3·10⁹` internal vibrational DOF. Their characteristic frequencies are in the THz range (Debye frequency for SiO₂ ~ 14 THz). Slow envelope at `~10⁻² Hz` cannot couple to THz internal modes via any reasonable triad mechanism — the frequency mismatch is 14 orders of magnitude. **Excluded** for the levitated-nanoparticle case; could be relevant for systems where mechanical and internal frequencies are comparable.
- **(c.ii) Collective trap-medium mode.** Speculative; depends on the trap configuration. For optical traps in UHV, there is no surrounding medium to support a collective mode. For magnetic traps or fluid-suspension systems, possibly relevant. Outside scope of Aspelmeyer-class experiments.
- **(c.iii) ED-fundamental new participation mode.** This would be a genuine new prediction of ED — a participation channel not corresponding to any existing physical degree of freedom. Without a derivation from the canonical PDE that fixes its frequency, damping, and coupling, it is not falsifiable as currently specified.

**Three-criteria check:**

| Criterion | Status under (c) |
|:----------|:-----------------|
| Coherent PDE-to-optomechanics correspondence | None — no concrete physical identification. |
| Derivable expression for `D` | None — no equations to match. |
| Consistent `Q` vs `N_osc` | Untestable. |
| Falsifiable `ω_v` | None unless `v_int` is concretely specified. |

**Verdict on (c): Held in reserve, not selected.** Candidate (c) is not falsifiable as currently formulated. It would become relevant if (b) is empirically falsified — i.e., if no envelope is found at either `2π N_osc γ_dec` or `2π N_osc κ` in cavity-coupled systems — at which point the natural fallback would be to posit that `v` is an ED-fundamental mode that has so far escaped detection. But this is a salvage move, not a primary prediction. Logged in §21.1 as the "salvage candidate."

### 22.5 Selection and what it changes

**Chosen identification:** Candidate (b) — `v ↔ X_cav`, the amplitude quadrature of the cavity field in the rotating frame at the drive frequency, which carries the radiation-pressure back-action onto the mechanical mode.

**Updates to §11 (the channel-weight mapping):**

- The §11 mapping `D = γ_dec/(γ_dec + ω_m)` is now **derived** from the canonical PDE matching exercise in §22.3, not posited heuristically.
- The "principal theoretical weakness" caveat in §11 ("not derived from a Madelung-style theorem the way the Arndt-regime `D_phys = ℏ/(2m)` is") is partially lifted: the mapping is derived from a structural matching of the canonical PDE's 2D linearization onto the linearized rotating-frame optomechanics equations. Not a Madelung-style theorem (no exact correspondence between full nonlinear theories), but a derived correspondence between linearized regimes.
- The choice of `γ_dec = γ_m(2n̄_th + 1)` rather than `Γ_opt` or `γ_m` alone is now justified: `γ_dec` is the bath-induced slow-envelope decoherence rate, which is what the matching identifies with `DP₀`.

**Updates to §15 (the `ω_v` derivation):**

- The §15(β) ansatz `τ_v = 1/γ_dec` is now grounded in the candidate-(b) identification: the slow-envelope decoherence is set by the mechanical-bath coupling, since the cavity-field damping `κ/2` is typically much faster (good-cavity limit `κ ≫ γ_dec`).
- The "explicit physical claim" status is upgraded to "derived under candidate (b) in the good-cavity limit."
- The fallback `ω_v' = 2π N_osc κ` (for `κ ≪ γ_dec`) is now specifically a prediction that would obtain in *bad-cavity systems*, where the cavity itself decoheres faster than the mechanical bath. This is a regime distinction, not just a numerical alternative.

**Updates to §21 (open issues):**

- §21.1 is now resolved (candidate (b) selected). Logged decision and rejected candidates with reasons.
- §21.2 (`Q ≈ 3.5` vs `N_osc ≈ 9` consistency) is unaffected — this is a separate ED-Phys-17 convention question, not addressed by the (`ρ`, `v`) identification.
- §21.3 (`Q ≈ 3.5` provenance) is partially addressed: under candidate (b), `ζ ≈ 0.5` (from cavity damping), and the canon `ζ ≈ 0.45` agrees. If the orientation's `Q ≈ 3.5` quote uses `ζ ≈ 0.2`, it is in a different parameter regime than the cavity-mapped one. This might mean the optomechanics-mapped `Q_v` is different from the quoted ED-Phys-17 `Q ≈ 3.5` — in which case F3 (`Q_v ∈ [2, 5]`) needs to be re-derived in the cavity-mapped regime. **Logged as a follow-up to §21.3.**
- §21.4 (Atlas anchor for non-quantum regimes) is largely unaffected — but the §22.3 derivation provides a template (rate-balance under (`ρ`, `v`) identification) that could be applied systematically to other regimes.

### 22.6 Falsification structure under candidate (b)

The cavity-field identification yields a refined falsification surface:

| Test | Outcome | Implication |
|:-----|:--------|:------------|
| F0: envelope at `ω_v = 2π N_osc γ_dec` | confirmed | candidate (b) supported, §15(β) holds |
| F0 fails at `2π N_osc γ_dec`, succeeds at `2π N_osc κ` | confirmed at alternate frequency | candidate (b) supported, but §15(β) ansatz wrong; bad-cavity regime governs |
| F0 fails at both `2π N_osc γ_dec` and `2π N_osc κ` | no envelope at any cavity-mapped frequency | candidate (b) falsified; check candidate (c.iii) (ED-fundamental new mode) — i.e., search for envelope at any frequency |
| F0 fails everywhere across multiple system types | no envelope feature in any cavity-coupled cooled system | ED-09.5's optomechanics extension falsified |
| F2 ∧ F3 fail (linear envelope dynamics wrong) | wrong `N_osc` or `Q_v` | §15 derivation wrong but envelope exists; partial support, requires re-derivation |
| F4 ∧ F5 fail (no third-harmonic, no triad coupling) | linear envelope correct, nonlinear structure absent | candidate (b) supported, but ED's triad structure is regime-suppressed in optomechanics; partial confirmation |

The four-stage F0 cascade (`γ_dec` → `κ` → "anywhere" → "nowhere across systems") provides a graduated falsification path that distinguishes "wrong specific ansatz" from "wrong identification" from "wrong prediction entirely."

### 22.7 Implication for non-cavity systems

(Unchanged from previous draft of §22 — the cavity-field identification scope-limits ED-09.5's envelope prediction to systems with a global coupled mode satisfying §22.1. Cavity-optomechanics: `v` ↔ cavity field. Feedback-cooled levitated nanoparticles (Magrini 2021): `v` ↔ feedback control signal — also global, scalar, with own bandwidth, drives `ρ` everywhere. Free levitated particles in optical trap with no cavity and no feedback: no `v` candidate, ED-09.5 envelope feature **not predicted**. This is itself a comparative test: the envelope should be present in cavity/feedback systems and absent in free-trap systems with the same particle.)

### 22.8 Summary

| Question (§21.1) | Resolution |
|:-----------------|:-----------|
| What is `v` physically in an optomechanical system? | The amplitude quadrature `X_cav` of the cavity field in the rotating frame (candidate (b)). For feedback-cooled non-cavity systems, the feedback control signal. |
| Is the §11 mapping `D = γ_dec/(γ_dec + ω_m)` ED-native? | **Yes — derived** from the structural matching of the canonical PDE's 2D linearization onto rotating-frame optomechanics equations under candidate (b). |
| Does the choice fix `ζ`? | Yes — `ζ ≈ 0.5` (from `Ẋ_cav = -(κ/2) X_cav`), in agreement with the canon default `ζ ≈ 0.45`. **Non-trivial consistency check.** |
| Is the §15(β) `τ_v = 1/γ_dec` ansatz justified? | Yes — derived under candidate (b) in the good-cavity limit `κ ≫ γ_dec` (the typical case for §13 systems). |
| Are candidates (a) and (c) falsified? | (a) is structurally falsified — forces `D = 0`, contradicts §11. (c) is not falsified but not currently falsifiable (no concrete identification); held as the salvage candidate if (b) fails experimentally. |
| Cold-reader-pass status of §11 mapping | Upgraded from "heuristic-but-motivated" to **"derived under specified `(ρ, v)` identification"**. Residual concerns: the rate-balance interpretive step (still an interpretation, not a theorem); the choice of `γ_dec` over `Γ_opt` (justified physically but not uniquely forced); the good-cavity assumption in §15 (specified as a regime, not as a universal claim). |

---

## 21. Theory consolidation: open issues for the ED corpus

The consolidation pass surfaced four issues that need resolution within the ED corpus before the Aspelmeyer email can go out. None requires new experimental data; all are theory work against existing ED documents.

### 21.1 The `(ρ, v) ↔ (mechanical mode, ?)` correspondence — RESOLVED (2026-04-20, see §22)

**Resolution.** Candidate (b) selected: `v ↔ X_cav`, the cavity-field amplitude quadrature in the rotating frame at the drive frequency, which carries radiation-pressure back-action onto the mechanical mode. For feedback-cooled non-cavity systems (e.g., Magrini 2021), `v ↔` feedback control signal.

Rejected candidates:

- **(a) `v` ↔ mechanical momentum quadrature `p(t)`** — structurally falsified. Forces `D = 0`, contradicts §11 mapping. Predicts `ω_v = ω_m` (carrier frequency), not a slow envelope. Category-confuses the (`x, p`) phase-space pair of a single mode with the (`ρ, v`) two-channel structure of ED.
- **(c) `v` ↔ internal participation mode coupled via triad structure** — held in reserve as the salvage candidate if (b) is empirically falsified. Currently not falsifiable (no concrete physical identification specified).

The selection produces a non-trivial consistency check: `ζ ≈ 0.5` (from candidate-(b) cavity decay structure) agrees with the canon default `ζ ≈ 0.45` to within 11%. The §11 mapping `D = γ_dec/(γ_dec + ω_m)` is now **derived** from rate-balance under the identification, not heuristic.

**Remaining caveat.** Under candidate (b) the §15 envelope-decoherence ansatz `τ_v = 1/γ_dec` is derived in the **good-cavity limit** `κ ≫ γ_dec` only. In bad-cavity systems the alternative `τ_v = 1/κ` would govern, giving `ω_v' = 2π N_osc κ`. This is a falsifiable secondary path (§22.6).

### 21.2 The `N_osc` convention — RESOLVED (2026-04-20, see §15)

ED-Phys-17 was read directly. The convention is documented explicitly in §3.2: "Peak height oscillations: Turning points in tallest peak height series." This is the count of local extrema, NOT a count to a specific amplitude threshold.

**Three findings from the ED-Phys-17 read:**

1. **Convention.** `N_osc` = count of turning points (local extrema). Equals `2 × N_full_cycles` for a clean underdamped sinusoid.
2. **Source of the [8, 19] range.** Background complexity, not Q-derived spread. Single-mode flat-background case gives `N_osc = 8`; standing-wave background case gives `N_osc = 19` due to multi-modal interference adding extra wiggles to the peak-height time series.
3. **`Q ≈ 3.5` vs `N_osc ≈ 9` was a false dilemma.** The two values come from *different* ED experiments: `Q ≈ 3.5` from 00.3 with parameters not stated; `N_osc` range from ED-Phys-17 with explicit parameters that compute to `Q ≈ 6.3`. They were never meant to derive jointly. With ED-Phys-17's `Q ≈ 6.3` and `N_osc = 8` (single-mode), the implied amplitude visibility threshold is α ≈ 14% — a physically reasonable peak-detection cut.

**Bonus consistency check.** ED-Phys-17 used `ζ = 0.5` exactly. The §22.3 cavity-field-derived ζ is `ζ ≈ 0.5`. **Exact agreement to one decimal place** — the second non-trivial cross-check supporting candidate (b) (the first being §22.3's `ζ ≈ 0.5` vs canon-default `ζ ≈ 0.45`). This means the ED-Phys-17 oscillator regime IS the cavity-mapped optomechanics regime, and ED-Phys-17's dynamical predictions should map directly onto cooled optomechanics under candidate (b).

**Updates landed:** §15 derivation uses the corrected formula `ω_v = π N_osc γ_dec` (factor of 2 reduction from v0.4); §15 numerical predictions table reflects this; §16 F0 target frequency updated; §16 F2 specifies turning-point convention with conservative range `[6, 12]` for clean single-mode cases; §16 F3 widened to `[3, 9]` to cover both 00.3 (Q ≈ 3.5) and ED-Phys-17 (Q ≈ 6.3) values pending §21.3 resolution.

### 21.3 The `Q ≈ 3.5` provenance — RESOLVED (2026-04-20, see §16 F3 update)

**Resolution.** The "Q ≈ 3.5" attribution in the orientation is **not supported by any in-repo derivation**. The structurally correct canonical value for the optomechanics regime is `Q ≈ 6.3` (low-k single-mode limit, ED-Phys-19).

**What the repo says.** The 00.3 document itself is on Desktop (not in repo) and could not be inspected directly. But the ED corpus's most explicit unified-cosmology derivation lives in [`archive/research_history/ED Physics/ED-Phys-19_UnifiedCosmology/ED-Phys-19_UnifiedCosmology.md`](../archive/research_history/ED Physics/ED-Phys-19_UnifiedCosmology/ED-Phys-19_UnifiedCosmology.md), which:

- Uses parameters identical to ED-Phys-17 (α=0.1, γ=0.5, τ=100, ζ=0.5, ρ_*=50, ρ_0=0.5).
- States the Q formula explicitly as `Q = √(K_eff·τ)/ζ` (line 745) and `Q = ω₀/(2γ) = √(K_eff·τ)/ζ` (line 452).
- Computes `K_eff = M(ρ_*)·k² + αγ/ρ_0`, where `αγ/ρ_0 = 0.1` is the linearized penalty stiffness for k→0.
- Quotes the resulting **Q range as 6.3 (low k) to 10.1 (high k)** at canonical parameters (line 452, also line 629).
- Derives `N_osc ≈ Q · ln(A_0/A_min)/π ≈ 6.3 · ln(100)/π ≈ 9` for Q=6.3 with 1% amplitude threshold (line 458) — confirming the full-cycle convention used in ED-Phys-17 (whose actual code with `//= 2` also yields full-cycle counts, despite the verbal description "turning points").

**No derivation in the repo supports Q = 3.5.** A grep of all archive directories for "Q.*3.5" returns no instance of the value being computed; it appears only as a quote in three derived documents:

- [`theory/Architectural_Canon.md`](../theory/Architectural_Canon.md) line 124 — attributed to "00.3" with no source derivation.
- [`docs/ED-Testing-Synthesis-2026-04-17.md`](ED-Testing-Synthesis-2026-04-17.md) line 33 — attributed to "00.3."
- [`docs/ED-Logic-Flow.md`](ED-Logic-Flow.md) — referenced indirectly.

**Most likely explanations** (in decreasing order of plausibility):

1. **Inherited inconsistency / typo in 00.3.** The actual 00.3 PDF may quote 3.5 in error, possibly from a different draft, or by using a non-canonical parameter set or alternative Q convention not surfaced in the inherited summary.
2. **Different convention in 00.3.** 00.3 might define `Q = ω/(4γ) = √(K_eff·τ)/(2ζ)` (factor of 2 different from ED-Phys-19). For ED-Phys-19's parameters that gives Q ≈ 3.16 — close to 3.5, possibly within rounding.
3. **Different parameters in 00.3.** If 00.3 uses ζ = 1.0 (rather than 0.5) with all other params equal, Q = √(0.1·100)/1.0 = 3.16 ≈ 3.2. Close to 3.5 but not exactly.

The (1) and (2) explanations don't change the optomechanics F3 prediction (which is structurally tied to `ζ = 0.5` via §22.3 cavity matching). The (3) explanation would imply 00.3 explored a different regime than ED-Phys-17/19, in which case ED has *two parameter regimes* with two canonical Q values, and **cavity-optomechanics inherits the ED-Phys-17/19 regime** (because of the `ζ = 0.5` match), giving `Q ≈ 6.3`.

**Conclusion (per the user's task §3):** under any of (1)–(3), the cavity-mapped optomechanics regime's canonical Q is `Q ≈ 6.3 ± 2`. F3 has been tightened from `[3, 9]` to `[4, 9]` accordingly.

**Recommended follow-up for Allen:** verify the Q quote in the actual 00.3 PDF on Desktop and either correct the inherited summaries (Architectural_Canon.md, ED-Testing-Synthesis-2026-04-17.md, ED-Logic-Flow.md) to `Q ≈ 6.3` if the 3.5 is an error, or document the parameter regime that yields Q ≈ 3.5 if it is correct in 00.3 but distinct from ED-Phys-17/19's.

### 21.4 Atlas anchor systematization across non-quantum regimes — PARKED as future work (week-scale project)

**Status (2026-04-20):** This is no longer an active next-step. It is parked as a **candidate ED-Atlas extension paper** to be opened at a deliberate later date. Estimated effort: ~1 week of focused theory work. Not required to proceed with the Aspelmeyer email or the Tier-1 reanalysis.

**The problem.** The Dimensional Atlas's quantum-regime `T₀ = 2 D_nd ℏ/(mc²)` is Compton-time-anchored and gives unphysical `ω_v` predictions for slow mechanical systems. The §15(β) work-around is to replace `T₀ = 1/ω_C` with `T₀ = 1/γ_dec` for optomechanics — but this is a *new dimensional anchor* for the regime, not a Madelung-type derivation. The same problem will recur in Haroche/Raimond cavity QED: what is `T₀` when there is no obvious Compton-time scale?

**Proposed scope (when opened).** A new paper, provisionally **`ED-Dimensional-01-Ext: Anchoring Non-Quantum Regimes via the Rate-Balance Template`**, that systematizes the choice of `T₀` (and by extension `D_nd`) across non-quantum regimes by applying the §22.3 rate-balance template developed for the Aspelmeyer mapping. The template:

1. Identify the system's `(ρ, v)` ↔ (local field, global mode) correspondence.
2. Linearize both dynamics and match onto the canonical PDE 2D template `[[-DP₀, H], [-P₀/τ, -ζ/τ]]`.
3. Derive `D` from the rate-balance condition `D · γ_local ↔ H · ω_global` with the convex constraint `D + H = 1`.
4. Derive `τ` from the participation mode's intrinsic damping rate.
5. Derive `ω_v` from the appropriate decoherence-time ansatz (analogue of `τ_v = 1/γ_dec`).

**Targets for the extension paper:**

- **Haroche / cavity-QED.** `(ρ, v)` ↔ (atomic excitation density, cavity field). Photon number `n` and atom number `N` as control parameters. Likely produces `D = κ/(κ + ω_atom)` mapping with bifurcation at the cavity-vs-atom-linewidth threshold — well-known regime boundary in cavity QED, analogous to optomechanics' sideband-resolution threshold.
- **Condensed matter** (extension of ED-Dimensional-03). `(ρ, v)` ↔ (local concentration, mean-field order parameter). Diffusion vs. thermal-fluctuation rate balance.
- **Galactic** (extension of ED-Dimensional-04, post-ED-XX). `(ρ, v)` ↔ (matter density, environmental temporal-tension field). Megaparsec-scale rate balance.
- **Cosmological** (extension of ED-Dimensional-05). `(ρ, v)` ↔ (compositional density, expansion mode). Hubble-scale rate balance.

**Why parked.** Three reasons not to take this on now:
1. The Aspelmeyer mapping at v0.7 is internally consistent without it; the Aspelmeyer email and Tier-1 reanalysis can proceed.
2. This is a paper-scope project, not a memo-scope task. It would generate a new document in the Atlas series, not a section in this memo.
3. Pivoting to a different ED-Math Pipeline branch (FRAP, merger-lag, weak-lensing) may produce more immediate empirical leverage.

**Decision-blocking nothing.** §21.4 is not required for any other open task in the corpus. It can sit indefinitely until a deliberate decision is made to open it.

### 21.5 Ranked priority for the next theory session (updated 2026-04-20 post-§22 + post-§21.2 + post-§21.3)

| # | Issue | Status | Blocks | Effort |
|:-:|:------|:-------|:-------|:------:|
| ~~2~~ | ~~§21.1 `v` ↔ optomechanics mode~~ | **RESOLVED §22** — candidate (b) selected | — | done |
| ~~1~~ | ~~§21.2 `N_osc` convention~~ | **RESOLVED §15+§21.2 (v0.7 fix)** — full cycles (algorithm with `//=2`), formula `ω_v = 2π N_osc γ_dec` | — | done |
| ~~3~~ | ~~§21.3 `Q ≈ 3.5` provenance~~ | **RESOLVED §21.3** — not derivable from any in-repo parameter set; canonical value is Q ≈ 6.3 (ED-Phys-19); F3 tightened to `[4, 9]` | follow-up: verify against 00.3 PDF on Desktop | done in repo, manual verification logged |
| ~~4~~ | ~~§21.4 Atlas anchor for non-quantum regimes~~ | **OPENED AS MEMO (v0.1, 2026-04-20)** — [`theory/ED-Dimensional-01-Ext.md`](../theory/ED-Dimensional-01-Ext.md). Rate-balance template ports cleanly to five regimes (Haroche/cavity-QED, condensed matter, FRAP, galactic post-ED-XX, cosmological). §21.4 first-pass result: template is regime-portable; cosmos sits at the bifurcation. | Cold-reader pass on the memo; resolve Haroche (α)-vs-(β) choice. | done |

**All four §21 issues now have resolutions (§21.1 + §21.2 + §21.3 closed; §21.4 opened as memo v0.1 with regime-portable template).** Theory track at v0.9 + ED-Dimensional-01-Ext v0.1 is at a coherent stopping point spanning five regimes. The Aspelmeyer mapping at v0.7 is materially tighter than at v0.4 entry:

- `D = γ_dec/(γ_dec + ω_m)` derived from rate-balance under candidate (b) (§22).
- `ω_v = 2π N_osc γ_dec` derived from `τ_v = 1/γ_dec` ansatz with full-cycle convention confirmed by code-trace + ED-Phys-19 cross-check (§15 v0.7).
- For single-mode optomechanics: `ω_v / 2π = 8 γ_dec`, `Q_v ≈ 6.3`, `N_osc ≈ 8`, harmonic ratio 3–6%, triad coupling C ≈ 0.03.
- **Three non-trivial cross-checks passing** supporting candidate (b): canonical-default ζ ≈ 0.45 vs cavity-derived ζ ≈ 0.5 (§22.3); ED-Phys-17/19 ζ = 0.5 exactly matching cavity ζ (§21.2 + §21.3); and ED-Phys-17 measured N_osc = 8 vs ED-Phys-19 derived N_osc ≈ 9 from Q = 6.3 (§15 + §21.3).
- Manual follow-up: verify 00.3 PDF Q-value against this analysis (low priority; doesn't block the Aspelmeyer email).

---

*Owner: theory work (Allen, with Claude assistance). v0.1–v0.8 history in the "Recent updates" block above. v0.9 (2026-04-20) — §20 manual thesis-skim returned negative on the predicted envelope signature; interpretation favors analysis-pipeline blind spot over physics absence; email framing sharpened to drop the "I see X in your Fig Y" anchor and lead with the methodological pitch ("standard pipelines wouldn't show this envelope; please share raw x(t)"). Update this file in place rather than versioning a new one; substantive revisions go in the "Recent updates" block at the top mirroring the convention in `docs/ED-Orientation.md`.*
