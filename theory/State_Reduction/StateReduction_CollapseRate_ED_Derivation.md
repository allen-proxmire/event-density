# Closing the gap: an ED derivation of the gravitational collapse rate

**2026-07-21. Status: structural derivation, honestly tiered — the gap is *partially* closed.** The state-reduction note (`Paper_ED_StateReduction_vs_CollapseModels.md`) named one owed thing: ED has no quantitative collapse rate to set against the Diósi–Penrose `τ ≈ ℏ/E_G`. This note derives one from ED's standing primitives (it is *not* Penrose's argument in ED words — it runs through the khronon = commitment-time and einselection = commitment-individuation), recovers `τ ≈ ℏ/E_G`, gives it a deeper origin, and produces three *distinctive* refinements — while leaving two honest residuals, one of which is a real experimental risk.

## The two standing ingredients (cited, not assumed)

1. **The khronon is the commitment-time, and it dilates with the field (Report §5, GR-I/GR-II).** ED's gravity is khronometric; the khronon is the arrow made dynamical, i.e. the substrate's direction of commitment. The emergent lapse is set by the bandwidth, `N² ~ b`, so a region's *committed-time rate relative to coordinate time is* `dτ/dt = N ~ √b`. In the weak field `N = 1 + Φ/c²` — this is exactly gravitational time dilation, and in ED it is literally a **commitment-rate**: where the field is deeper, the arrow commits at a different rate (the sparse-commitment factor of Mass-Without-Mass §5 is this same clock).
2. **Einselection is commitment, and it individuates when branches become distinguishable (Report §4).** P11 commitment is the sole collapse primitive; it resolves a superposition into one channel (a superposition is never itself a commitment outcome). And "orthogonality reduces to distinguishability" — two would-be branches are individuated by commitment exactly when they become perfectly distinguishable. Commitment is irreversible and stochastic, so the outcome is a *definite, recorded* branch, not a mixture.

## The derivation

Put a mass in a superposition of two configurations, `1` and `2` (the standard lump-in-two-places setup). Each configuration sources its own bandwidth field, `b₁(x)` and `b₂(x)`, hence its own lapse `N_i ~ √b_i`, hence — because the khronon *is* the committed-time — **its own commitment-clock.** The two branches do not merely sit in different potentials; in ED they *commit time at different rates*:

$$\frac{d\tau_1}{dt} - \frac{d\tau_2}{dt} = N_1 - N_2 = \frac{\Phi_1 - \Phi_2}{c^2}.$$

The relative phase between two branches of energy `E_1, E_2` runs as `exp[-i(E_1-E_2)t/\hbar]`. The energy that differs between the two *gravitational* configurations — the energy stored in the difference of their committed-participation fields — is the gravitational self-energy of the difference of the mass distributions,

$$E_G = -G\!\int\!\!\int \frac{[\rho_1(\mathbf{x})-\rho_2(\mathbf{x})]\,[\rho_1(\mathbf{y})-\rho_2(\mathbf{y})]}{|\mathbf{x}-\mathbf{y}|}\,d^3x\,d^3y,$$

which is Penrose's `E_Δ`. So the two branches accumulate a **relative committed-time difference** at the rate `E_G/\hbar`.

Now the ED-specific step, and it is where this stops being Penrose. In standard QM this relative phase merely oscillates and the superposition persists forever. In ED it cannot: the arrow is a *single* committed time, and it is being asked to hold two branches whose committed-times run at *different rates*. It individuates them — commits, einselects one branch — as soon as they are commitment-**distinguishable**, i.e. when the accumulated relative commitment-action reaches the commitment quantum,

$$E_G\,\tau \sim \hbar \quad\Longrightarrow\quad \boxed{\;\tau \approx \frac{\hbar}{E_G}\;}.$$

**ED recovers `τ ≈ ℏ/E_G`.** But look at *why*. Penrose gets it from the *ill-definedness* of a preferred time across the two spacetimes. ED gets it from the *presence* of one committed arrow-time that finds the two branches running on **different but well-defined** commitment-clocks and, being a single arrow, cannot carry both — so it commits. Penrose's "no fact about which time flows" becomes ED's "one arrow, two branch-clocks, forced to individuate." The `E_G` scale is the same; the mechanism is the arrow, not an energy uncertainty and not an injected noise.

## Three distinctive refinements (where ED is not just re-deriving the others)

1. **It is the *difference*, not the sum (ED sides with Penrose/Diósi against Hossenfelder).** The rate is driven by `N_1 − N_2`, the *difference* of the branch clocks, so `E_G` is the self-energy of the *difference* of the mass distributions. Hossenfelder's residual scales with the *sum* of potentials (mean-field). ED's committed-time-difference mechanism forces the difference — a clean, distinguishing sub-prediction.
2. **A genuine reduction, not decoherence (ED matches Penrose, cleaner than Diósi).** Diósi's master equation yields a *mixed state* — decoherence, no definite outcome, so it does not by itself solve the measurement problem. ED's einselection commits, irreversibly and stochastically, to *one recorded branch*. ED delivers the definite outcome Penrose argues for, by the same primitive that already gives it the pointer basis (§4) — it does not need a separate reduction postulate.
3. **A native regulator (ED escapes the DP point-mass divergence *structurally*).** `E_G` diverges for point masses; Diósi and Penrose must insert a regularization length by hand (~the nucleon size), and the *choice* of that length is exactly what experiment constrains. ED has no point masses: participation is finite-grained at the substrate scale and mass is *binding* (a bound composite of finite extent, Mass-Without-Mass), so the difference-field is smeared and `E_G` is finite without an ad-hoc cutoff. The regularization the DP program needs is built into ED's ontology.

## Two honest residuals — and one is a real risk

- **The individuation coefficient is not pinned.** The *scaling* `τ ∝ ℏ/E_G` follows from the committed-time-difference (grounded); the exact prefactor (is it `ℏ`, `2πℏ`, `ℏ/2`?) rides on the precise distinguishability threshold for commitment, which §4 grounds in kind but not to a number. Rigor here = the same distinguishability/A1 machinery, pushed to a coefficient.
- **The experimental status is genuinely open, and possibly adverse.** The 2020 underground search excluded the *parameter-free* Diósi–Penrose model by looking for the spontaneous X-ray radiation collapse must emit. If ED's native regulator lands near the Planck/substrate scale, ED's `E_G` could sit in or near the *excluded* region — **so ED is not automatically safe.** The escape, if there is one, is that ED's collapse is a *discrete commitment/recording event*, not Diósi's *continuous* stochastic potential, so it need not radiate the same way — the spontaneous-emission signature of a commitment-individuation is a different (unshown) calculation. This must be computed before claiming ED evades the bound; right now it is an open question that could go against ED. State it as a risk, not a win.
- **Minor:** ED's gravity is the *quadratic-strain interference cross-term*, not the Einstein–Hilbert term (Report §5, Paper_QuadraticStrain), so the exact energy combination driving the branch-phase could differ subtly from the textbook `E_G`; whether the interference reading modifies the self-energy-of-the-difference is a refinement to check.

## Tiers

- `τ ≈ ℏ/E_G` recovered from the khronon-clock difference + einselection — **structural derivation** (both ingredients standing; the individuation *criterion* grounded-in-kind, the coefficient open).
- Deeper origin (one arrow, two branch-clocks → individuation) vs Penrose's ill-defined time — **interpretive, grounded in §5+§4**.
- Difference-not-sum; reduction-not-decoherence; native regulator — **distinctive consequences of the mechanism**.
- Exact coefficient; the spontaneous-radiation/experimental status — **open** (the latter a live risk).

## Net

The gap named in the note is **partially closed**: ED now has a derivation that recovers the program's `ℏ/E_G` from its own primitives, gives it a deeper origin (the arrow, not `E_G` itself, is fundamental), and adds three distinctive refinements — with the honest caveat that the exact rate coefficient and, more importantly, whether ED's version survives the 2020 collapse-radiation bound are not yet settled. Next moves: (i) pin the individuation coefficient via the §4/A1 distinguishability machinery; (ii) **compute the spontaneous-emission signature of a commitment-individuation** — the make-or-break, since it decides whether ED is excluded with the simplest DP model or escapes by being discrete-and-recording rather than continuous-noise. Fold the "partially closed" status back into `Paper_ED_StateReduction_vs_CollapseModels.md` §5.
