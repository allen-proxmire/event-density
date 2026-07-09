> **RETRACTED 2026-07-09 (same day). This "resolution" is WRONG: an over-banked save caught by Claude-B adversarial review and confirmed numerically. The claimed ~70-order headroom is a UNITS ARTIFACT: it counts the horizon holographically (AREA, `(R_H/ℓ_P)² ~ 10¹²³`) but the galaxy by MASS (`M/m_Pl ~ 10⁵⁰`). Since a horizon's area count = (its mass count)², the mismatch inflates the headroom by `~1.07×10⁶²` — the entire "save." Counted consistently (both by mass, horizon `M_hor/m_Pl ~ 10⁶¹`), `σ² ~ b_gal/b_hor ~ 10⁻¹²`, `σ ~ 1.6×10⁻⁶`, and a galaxy at star-counting gives `σ²·N ~ 0.27` — Newton FAILS. Worse, the paper's own §6 needs `σ ≈ 0.09` (from `2σ = a₀_obs/cH₀ ≈ 0.18`), which is the SAME σ, 36 orders from the `10⁻³⁷` this doc silently used. The MOND-survival "check" (`2σ√(b_hor/b_gal)=1.000`) is tautological (σ is DEFINED as `√(b_gal/4b_hor)`). And `σ² ~ b_onset/b_hor` makes σ system-dependent, contradicting MOND's fixed-acceleration universal onset. THE MANY-BODY NEWTON TENSION SURVIVES AS A POTENTIAL SHOWSTOPPER, now sharpened: the σ that protects Newton and the σ that sets a₀ are in direct numerical conflict, so the many-body tension and the unworked bandwidth↔acceleration bridge are ONE problem. Kept for the record (the failure is instructive: reverse-crank-rail, [[feedback_dont_over_bank_falsifications]]). Do not cite as a resolution.**

---

# ~~The Many-Body Newton Tension Resolves: the Holographic Horizon Bandwidth Forces σ Tiny Enough to Protect Newton While Sourcing MOND~~ [RETRACTED — see banner]

**Foundations, gravity / curvature-emergence arc. Resolves the central open problem of the interference-MOND recast (flagged as a potential showstopper): the σ²-vs-σ coherence asymmetry is per-pair, and coherence is transitive, so N separate masses each σ-coherent with the horizon (for MOND) are mutually σ²-coherent, giving a many-body Newton violation ~ σ²·N. Probe: `evaluation/CurvatureEmergence/manybody_newton_tension_probe.py`. RESULT: σ is NOT free. The MOND onset (cross-term ~ diagonal) fixes σ² ~ b_onset/b_hor, and the holographic horizon bandwidth b_hor ~ (R_H/ℓ_P)² ~ 10¹²³ (the arc-standard count, the same order as Θ_ED ~ 10⁻¹²²) forces σ² ~ 10⁻⁷³. That same tiny σ makes the many-body violation σ²·N safe for every physically-reasonable source count (solar system ~10⁻¹⁷ at atom-counting, galaxy ~10⁻⁶³ at star-counting), with ~70 orders of headroom, while MOND survives at O(1) by construction. So it is NOT a showstopper: the enormous horizon bandwidth simultaneously sets the MOND onset and protects Newton. HONEST: the resolution is order-of-magnitude/structural (relies on b_hor ~ 10¹²³ holographic and b_onset ~ 10⁵⁰); the precise dimensional bridge (bandwidth ↔ acceleration, the O(1) coefficient) is unworked but the headroom absorbs it; only unphysical Planck-locus source-counting fails. Held to the reverse-crank bar (overturning a negative needs the same scrutiny as a positive). See [[project_p14_partial_reduction]], [[feedback_dont_over_bank_falsifications]].**

---

## 1. The tension, precisely

The recast's coherence asymmetry (local-local coherence `σ²`, local-horizon `σ`) is a per-pair identity. Claude-B correctly pressed the many-body version: coherence is **transitive**. If mass `A` is `σ`-coherent with the horizon (as MOND requires) and mass `B` is too, then `A` and `B` are `σ²`-coherent with *each other*. A two-body probe confirms this exactly: two independent phases each `σ`-aligned to a fixed horizon reference (phase 0) have mutual coherence `⟨cos(π_A−π_B)⟩ = σ²` (measured `0.0098` at `σ=0.0995`, `0.6564` at `σ=0.81`), while each has `σ` coherence with the horizon. So the local-local Newton violation is **not** avoidable; summed over `N` separate masses it is `~ σ²·N` relative to the diagonal. Many-body Newton then requires `σ²·N ≪` (Newton-test precision). The showstopper question: is a `σ` that small compatible with a `σ` large enough to give MOND?

## 2. The resolution: σ is fixed by the onset, and the horizon is enormous

**`σ` is not a free parameter.** The MOND onset is where the interference cross-term equals the diagonal: `2σ√(b_loc b_hor) ~ b_loc`, i.e.
$$ \sigma^2 \;\sim\; \frac{b_{\text{onset}}}{4\,b_{\text{hor}}}, $$
where `b_onset` is the bandwidth of a system *at* the MOND onset (a galaxy) and `b_hor` is the horizon bandwidth. Now use the numbers the arc already commits to:

- `b_hor = (holographic horizon count) ~ (R_H/ℓ_P)² ~ 10¹²³` (the same count that gives the area law and the `g~1/b` metric, and the same order as `Θ_ED ~ 10⁻¹²²`).
- `b_gal ~ M_gal/m_Pl ~ 10⁵⁰` (a galaxy's bandwidth, mass in Planck units).

So `σ² ~ b_gal/(4 b_hor) ~ 10⁻⁷³` (probe: `2.5×10⁻⁷⁴`, `σ ~ 1.6×10⁻³⁷`), and the probe confirms this same `σ` gives MOND at the onset (`2σ√(b_hor/b_gal) = 1.000`, O(1)). **The enormous horizon bandwidth forces `σ` tiny, and that is exactly what many-body Newton needs.** The headroom `b_hor/b_gal ~ 10⁷³` is the margin.

## 3. Newton is safe for every physical source count

The many-body violation `σ²·N` with `σ² ~ 2.5×10⁻⁷⁴`, swept over source counts (probe):

| system, source count | `N` | `σ²·N` | verdict |
|---|---|---|---|
| solar system, bodies | `~10` | `2.5×10⁻⁷³` | safe (bound `~10⁻⁹`) |
| solar system, atoms in Sun | `~10⁵⁷` | `3×10⁻¹⁷` | safe (bound `~10⁻¹³`) |
| galaxy, stars | `~10¹¹` | `2.5×10⁻⁶³` | safe |
| galaxy, atoms | `~10⁶⁹` | `3×10⁻⁵` | untested at this level, and below the MOND effect itself |
| galaxy, Planck loci (unphysical) | `~10⁸⁰` | `2.5×10⁶` | fails, but Planck loci are not independent gravitating sources |

So for any physically-reasonable notion of an independent gravitating source (coarse bodies through atoms), the violation is far below the relevant Newton bound. The only failure is at Planck-locus counting, which is not a physical source count for gravity (gravity is coarse; and within a bound co-local system the horizon bias is shared, cf. the QM-consistency result). The double-slit QM-consistency is a *separate* matter: the two paths of one particle share that particle's alignment, which cancels in their relative phase, so the `σ²` mutual coherence is between distinct masses, not within one particle.

## 4. Honest tiers and verdict

- **The transitivity (violation nonzero, forced) is exact** (probe): the MOND coherence unavoidably induces an `σ²·N` Newton violation. This is real, not wished away.
- **`σ` fixed by the onset** (`σ² ~ b_onset/b_hor`) is the onset condition, sound.
- **The resolution is order-of-magnitude / structural:** it relies on `b_hor ~ 10¹²³` (holographic, used throughout the arc) and `b_onset ~ b_gal ~ 10⁵⁰` (order of magnitude). The precise dimensional bridge (bandwidth ↔ acceleration, hence the O(1) coefficient in `a₀`) is unworked, but the `~70`-order headroom comfortably absorbs O(1)-to-several-order uncertainties.
- **Residual:** the effective-source-count principle (safe from bodies to atoms; only unphysical Planck-locus counting fails) and the unworked dimensional bridge. A real but `~10⁻¹⁷` (untestable) source-source Newton correction is predicted.

**Verdict.** The many-body Newton tension is **resolved with large margin**, and is **not a showstopper**. The key is that `σ` is not free: the MOND onset fixes `σ² ~ b_onset/b_hor`, and the holographic horizon bandwidth `b_hor ~ 10¹²³` forces `σ² ~ 10⁻⁷³`, so the same enormous horizon count that *sets* the MOND onset also *protects* Newton, with `~70` orders of headroom that keep the (forced, nonzero) many-body violation far below bounds for every physical source count. Held to the reverse-crank bar ([[feedback_dont_over_bank_falsifications]]): the resolution is order-of-magnitude/structural and rests on the arc-standard holographic horizon bandwidth, not on a tuned parameter, and it honestly retains a real (tiny) violation and the unworked dimensional bridge as residuals. This converts the recast's central open problem from "potential showstopper" to "resolved under any physical source count, residual = the dimensional-bridge coefficient." The interference-MOND mechanism survives its sharpest internal test.
