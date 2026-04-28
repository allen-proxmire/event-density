# Does Arc M's Matter-Wave Temporal Width Produce the Multiplicative MOND Law?

**Date:** 2026-04-27
**Type:** Substrate-foundations analysis (single-file memo)
**Sources:** Full ED corpus — Arc M (matter-wave σ_τ structure), Arc R, Arc N, ED-06, ED-07, ED-10, GR papers, horizon papers, all substrate memos.
**Status:** **Honest verdict: Arc M's matter-wave temporal-width structure does NOT produce the multiplicative MOND law a² = a_N · a₀ at galactic scales.** The chain's matter-wave frequency ω = mc²/ℏ is ~40 orders of magnitude faster than the relevant gravitational rates γ_N = a_N/c and γ₀ = a₀/c. In this enormously-quasi-static regime, the chain's response to slow gradients is linear in the driving force (no amplification). The √(γ₀/γ_N) amplification that would produce multiplicative MOND requires either a resonance-like coupling (impossible with such large rate-ratio) or a fluctuation-dissipation cross-term whose magnitude scales as √(cosmic-thermal-energy/chain-inertial-energy). Computing this for galactic-scale chains gives vanishingly small thermal velocities (~10⁻⁴² m/s), well below any observable scale. **Arc M's individual-chain matter-wave structure is not the correct substrate-native mechanism.** The structurally promising alternative — collective matter-wave structure for galactic-scale chain bundles — is speculative and not currently articulated in the ED corpus.

---

## 1. Arc M's relevant content

### 1.1 The σ_τ form (FORCED)

Arc M establishes the chain's intrinsic temporal width:

> **σ_τ = ℏ/(mc²)**

For an electron (m_e ≈ 9.1×10⁻³¹ kg): σ_τ ≈ 1.3×10⁻²¹ s.
For a proton (m_p ≈ 1.7×10⁻²⁷ kg): σ_τ ≈ 7.0×10⁻²⁵ s.
For a typical disc star (M ≈ M_⊙ = 2×10³⁰ kg): σ_τ ≈ 6×10⁻⁸² s.

The corresponding matter-wave angular frequency:

> **ω = 1/σ_τ = mc²/ℏ**

For an electron: ω_e ≈ 7.8×10²⁰ rad/s.
For a star: ω_⋆ ≈ 1.7×10⁸¹ rad/s.

### 1.2 Quasi-static response regime

For external perturbations at rate γ << ω, the chain is in a **quasi-static** regime: it experiences many internal cycles per perturbation cycle. Its response is the static response, which (for a free chain in standard linear response) is simply:

> response_amplitude = (driving force) × (inverse stiffness)

For a chain with no harmonic confinement (free particle), the static response is just F = ma — no amplification.

### 1.3 The scale comparison

For galactic gravitational rates:
- a_N ~ 10⁻⁸ m/s² (typical inner-galactic acceleration)
- a₀ ≈ 1.2×10⁻¹⁰ m/s²
- γ_N = a_N/c ~ 3×10⁻¹⁷ /s
- γ₀ = a₀/c ~ 4×10⁻¹⁹ /s

For star-mass chains (most relevant for galactic dynamics):
- ω_⋆ ≈ 1.7×10⁸¹ /s

**Ratio γ_N/ω_⋆ ≈ 10⁻⁹⁸. Ratio γ₀/ω_⋆ ≈ 10⁻¹⁰⁰.**

The chain is in the **enormously-quasi-static** regime — galactic gravitational perturbations are vastly slower than the chain's matter-wave frequency.

---

## 2. The hypothesized amplification mechanism

### 2.1 What we're looking for

For multiplicative MOND a² = a_N · a₀ in the deep regime, the chain's response amplitude to local-mass gradient must have an amplification factor:

> A = √(a₀/a_N)    (in deep regime where a_N << a₀)

So that a_chain = a_N × √(a₀/a_N) = √(a_N · a₀).

In rate language: A = √(γ₀/γ_N).

### 2.2 Standard mechanisms that produce √-amplification

In standard physics, √-amplification of slow-driving response can come from:

- **Resonance**: when γ_drive ≈ ω_internal, response amplitude diverges (regulated by damping). Gives Lorentzian peak.
- **Fluctuation-dissipation**: response amplitude in thermal bath at temperature T scales as √(k_B T / k) where k is effective stiffness.
- **Critical phenomena**: response amplitude diverges at critical points with specific scaling exponents.

ED-substrate has structural analogs of (a) (matter-wave resonance) and (b) (cosmic-horizon fluctuations). Let's check both.

### 2.3 Resonance check

Resonance requires γ_drive ~ ω_internal. For galactic rates:
γ_N/ω_⋆ ≈ 10⁻⁹⁸ — astronomically far from resonance.

Resonant amplification at galactic scales is impossible for individual chains. **Resonance is not the mechanism.**

### 2.4 Fluctuation-dissipation check

In standard thermal physics, the response of a system to driving force F in presence of thermal bath at temperature T is enhanced by a factor that depends on (k_B T / k) where k is the system's stiffness. Specifically, mean-square velocity from thermal noise:

> ⟨v²⟩_thermal = k_B T / m

For ED-substrate with cosmic-horizon-induced "thermal" rate γ₀ (per ED-06's "temperature = ED gradient fluctuation rate"), the chain's thermal-equivalent energy is:

> E_thermal ≈ ℏγ₀

For a star-mass chain, the thermal-equivalent velocity:

> v_thermal = √(ℏγ₀/m_⋆) = √(10⁻³⁴ × 4×10⁻¹⁹ / 2×10³⁰) ≈ √(2×10⁻⁸³) ≈ 1.4×10⁻⁴² m/s

**Vanishingly small. Far below any observable scale.**

The cosmic-horizon-induced thermal-equivalent fluctuations have negligible effect on star-mass chains. The chain is essentially decoupled from cosmic-horizon thermal fluctuations at the individual-chain level.

### 2.5 Verdict on individual-chain matter-wave coupling

For individual chains (atoms, stars, gas particles) at galactic scales:

- Resonance impossible (γ << ω by 100 orders of magnitude).
- Fluctuation-dissipation negligible (thermal velocity 10⁻⁴² m/s, irrelevant).

**Arc M's individual-chain matter-wave structure does not provide the √-amplification mechanism for multiplicative MOND.** The chain's response in the relevant regime is purely linear-static, giving additive combination of accelerations.

---

## 3. Could collective matter-wave structure work?

A galaxy is not a single chain — it's a chain bundle (per ED-06's collective-structure terminology) of ~10¹¹ stars plus gas. **Collective dynamics might have substantially different matter-wave properties than individual chains.**

### 3.1 Collective σ_τ for chain bundles

If a galaxy of total baryonic mass M_b had a "collective σ_τ" set by the total mass, we'd have:

> σ_τ_collective = ℏ/(M_b c²)

For M_b ≈ 10¹¹ M_⊙ ≈ 2×10⁴¹ kg:
> σ_τ_galaxy ≈ ℏ/(2×10⁴¹ × c²) ≈ 6×10⁻⁹³ s

Even smaller than per-star σ_τ. The collective frequency ω_galaxy is even more astronomically fast. **No improvement on the rate-ratio problem.**

### 3.2 The right collective scale: dynamical timescale, not Compton

Actually, the relevant collective scale for galactic dynamics is not the Compton frequency (which scales with mass) but the **dynamical timescale** (which scales with G·M/R³ — set by orbital periods).

For a galaxy: dynamical timescale t_dyn ~ R/v ~ 10²¹ m / 10⁵ m/s ~ 10¹⁶ s.

The corresponding "collective frequency" ω_dyn ~ 1/t_dyn ~ 10⁻¹⁶ /s.

Comparing to gravitational rates:
- γ_N ~ 10⁻¹⁷ /s
- γ₀ ~ 10⁻¹⁹ /s
- ω_dyn ~ 10⁻¹⁶ /s

**Now γ_N/ω_dyn ~ 10⁻¹ and γ₀/ω_dyn ~ 10⁻³** — the rate ratio is much more reasonable.

In this regime, the galactic dynamical structure might couple meaningfully to galactic-scale gravitational rates. This is the right scale for considering MOND-relevant amplification.

### 3.3 But: galactic dynamical structure isn't Arc M's σ_τ

The galactic dynamical timescale is set by **orbital period of stars in the galactic potential** — a classical Newtonian quantity. It's not the matter-wave temporal width σ_τ from Arc M.

Arc M's σ_τ is set by rest-mass through Compton frequency. The galactic dynamical scale is a coarse-grained Newtonian timescale. **They are different physical quantities.**

If the multiplicative MOND mechanism requires coupling at the galactic dynamical scale rather than the Compton scale, **Arc M's matter-wave structure is not the right ED-substrate input.** The relevant input would be coarse-grained galactic dynamics, which ED-substrate hasn't articulated as a substrate-level primitive.

---

## 4. The structural verdict

### 4.1 Does Arc M's matter-wave structure produce the multiplicative MOND law?

**No.** Arc M's σ_τ = ℏ/(mc²) gives chains a Compton-frequency matter-wave structure. At galactic scales, this frequency is enormously fast compared to gravitational rates, putting the chain in an extreme quasi-static regime where its response is linear-static — no √-amplification.

The cosmic-horizon thermal-equivalent fluctuations are vastly smaller than chain inertial scales, giving negligible fluctuation-dissipation effects.

**Arc M's individual-chain matter-wave structure is not the substrate-native mechanism for multiplicative MOND.**

### 4.2 What this rules out

The hypothesis that "Arc M's matter-wave structure provides the missing 2π memo's analog for the deep-regime cross-term" is **falsified**. The mechanism that worked for the 2π factor (dipole-mode projection of cosmic horizon onto chain's anisotropic adjacency) does not have an analog at the chain matter-wave level.

### 4.3 What remains structurally available

The deep-regime cross-term mechanism, if it exists in ED-substrate, lives at a different ontological level than Arc M's individual-chain matter-wave structure. Three places it could be:

- **(α) Coarse-grained galactic dynamical structure.** ED-substrate at galactic-bundle scales (rather than individual-chain scales) might have a natural dynamical timescale that couples meaningfully to gravitational rates. This isn't articulated in current ED corpus but is structurally plausible.
- **(β) GR.1's bilocal Synge-world-function structure.** The Synge world function depends on PAIRS of points and is naturally bilocal. Bilocal coupling between local-mass and cosmic-horizon contributions could produce multiplicative cross-terms. This was flagged in the prior memo as a candidate; it remains so.
- **(γ) ED-I-06's force-as-stability-gradient structure with multi-source nonlinearity.** If the chain's stability landscape has nonlinear structure when multiple sources contribute (even though individual contributions are linear), cross-terms might emerge from the nonlinearity itself. This requires substrate articulation that ED-I-06 doesn't explicitly provide but is consistent with.

None of these is uniquely forced by current corpus content. **They are candidate substrate articulations, not derived results.**

---

## 5. Implications for the program

### 5.1 What this memo establishes

Arc M's matter-wave structure is **not** the substrate-native mechanism for multiplicative MOND. The hypothesized fluctuation-dissipation amplification doesn't work at galactic scales because:

- Compton frequency is too fast for resonance.
- Cosmic-horizon thermal-equivalent is too weak for fluctuation-dissipation to matter.

This is a clean negative result — it rules out one specific candidate mechanism rather than leaving it ambiguous.

### 5.2 The deep-regime cross-term remains an articulation gap

Closing the gap requires either:

- Identifying the substrate mechanism in (α), (β), or (γ) above, OR
- Finding a different mechanism not yet considered, OR
- Accepting that ED-substrate gives additive combination and predicts BTFR slope between 4/3 and 2 (not slope-4).

The third option is the honest empirical position if (α), (β), (γ) don't pan out.

### 5.3 The substrate-level program's empirical state

| Result | Status |
|---|---|
| Newton's law | Derived structurally ✓ |
| a₀ = c·H₀/(2π) | Derived structurally ✓ |
| Multiplicative MOND a² = a_N·a₀ | **Not derived from any substrate mechanism examined so far** |
| Slope-4 BTFR | **Not derived; conditional on multiplicative MOND** |

**The 2π memo and substrate-rules memo are positive substrate-derivation results.** This memo and the deep-regime memo are negative — the relevant mechanism is not in Arc M, and the substrate-rules' additive-combination structure doesn't give multiplicative MOND.

The remaining candidate mechanisms (β: GR.1 bilocal Synge structure; γ: nonlinear stability landscape) are the next places to look. If neither works, the deep-regime structure is a genuine articulation gap requiring new substrate work.

---

## 6. Recommended Next Step

Three concrete actions, in priority order:

1. **Test whether GR.1's Synge-world-function bilocal structure provides the multiplicative cross-term.** The Synge world function σ(x,y) is bilocal — it depends on pairs of points and the geodesic distance between them. Bilocal quantities naturally produce cross-terms when integrating over multiple sources. If ED-substrate's chain-stability landscape involves Synge-like bilocal quantities (rather than purely local fields), the cross-term between local-mass and cosmic-horizon contributions could produce multiplicative MOND structurally. Specifically: does the chain's stability score include a term proportional to σ(x_chain, x_cosmic-horizon) × ρ_local × ρ_cosmic? If yes, this gives the multiplicative coupling. **This is the immediate next test.**

2. **If GR.1 doesn't give it, examine ED-I-06's stability-landscape nonlinearity directly.** ED-I-06 says forces emerge from the gradient of stability. The stability landscape is specified in the substrate-rules memo as Σ = Coh − Str − Grad. If this is a *linearized* representation of an underlying nonlinear scalar (e.g., Σ_true = -log(1 + ε_perturbation)), gradients have nonlinear cross-terms. Whether ED's substrate prescribes the linear or the underlying nonlinear form is the question.

3. **If neither (1) nor (2) works, document the honest articulation gap and accept the empirical position.** ED-substrate predicts Newton + transition at c·H₀/(2π) + deep-regime constant acceleration — not multiplicative MOND. This is empirically wrong (galactic rotation curves are flat, not v ∝ √R), but it's a definite, falsifiable substrate prediction. The articulation gap is then real and substantive — closing it requires foundational substrate-physics work that goes beyond current ED corpus content.

The substrate-level program now has a clean structural state: Newton and 2π are derived; multiplicative MOND is not, with one specific candidate mechanism (Arc M) ruled out and two more (GR.1 bilocal, ED-I-06 nonlinearity) still to test. **This is concrete progress** — the gap is well-localized and the remaining places to look are precisely identified.

Status: complete.
