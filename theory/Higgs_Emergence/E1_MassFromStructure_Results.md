# E1 Results — Mass from Structured Participation (H2 on the certified substrate)

**Run:** 2026-07-05, `theory/Higgs_Emergence/mass_from_structured_participation_probe.py` against `evaluation/Bits/simulator` (certified substrate, default `SigmaCoeffs` kc=ks=kg=1, rho_star=0.5), 41×41 (fixed-point tests) and 61×61 (in-flight tests), 8 seeds. First substrate test of the **H2 (patterned-condensate) Higgs candidate** that Arc Q Stage Q.4 evaluated only analytically.

**Provenance note.** An initial write-up of this probe claimed the isotropic case grounded an "isotropic mass-like confinement." A cross-check from a second session flagged that (a) Test 4 swept only *amplitude*, not correlation length, and (b) the amplitude-invariance test (Test 2) was extinction-confounded, so the *object* was not yet identified. Adding the correlation-length sweep (Test 4b) and an extinction-immune / single-variable paired test (Tests 2, 2b) **overturned the earlier headline.** This doc is the corrected result. The correction is the point: run the disambiguation before drawing the conclusion.

## Headline (corrected)

**On the certified substrate's native field, H2 does NOT give a mass.** Patterning the commitment-density field ρ produces either channeling (anisotropic patterning) or worldline *termination* at gradient peaks (isotropic patterning) — neither is a Lorentz-scalar propagation mass. The decisive evidence: isotropic patterning does **not** slow the commit front (no early-time velocity deficit, extinction on or off); the confinement that appears at late times is fronts **dying at gradient peaks** (extinction), not a dispersion-relation gap. A real σ_τ mass would reduce front velocity from t=0. It does not. So the substrate-Higgs via the H2/σ_τ route is **not grounded** on the certified reference substrate; `Paper_113` row 10 stays OPEN, and we now understand *why*: the native ρ-field has no amplitude-invariant, velocity-slowing mechanism for σ_τ to be.

## Field mapping (the one correction that held up)

The certified Σ = kc·Coh(ρ) − ks·ρ − kg·|Δρ| reads the **commitment-density field ρ (B4)** and graph-local structure only; the edge `bandwidth` enters *solely* at the tie-break, orientation is never read. So the honest H2 test patterns ρ, not edge bandwidth (which would be a field-mismatch, the micro-stiffness error). Corollary that proved load-bearing below: Arc M's σ_τ is amplitude-invariant by construction (log-derivative), but the certified Σ is amplitude-*sensitive* in ρ (Str keys on absolute ρ; rho_star; the absolute extinction threshold). **The certified substrate has no amplitude-invariant native field for σ_τ to live on.**

## Results

| Test | Setup | Result | Reading |
|---|---|---|---|
| **1. Reach vs gradient** | uniform vs stripes, matched mean, fixed point | uniform reach 13.0 (296 commits); stripes λ=8 reach ↑ ~14.6 | Structure does not isotropically impede spread. |
| **3. Anisotropy** | stripes: along-channel vs across-wall | along ↑ 11.9, across ↓ 8.3, **col/row 0.70 flat across amp** | Anisotropic patterning = **crystal**: conduction lanes + blocking walls; deficit doesn't scale with gradient (geometric channeling, not a mass). |
| **4. Isotropic, sweep amp** | random field, fixed point, extinction ON | reach 13.0 → 9.7 → 8.1 → 5.0 (amp 0.15/0.3/0.45); isotropic; density holds | Late-time confinement that scales with amplitude. *Looked* like a mass — hence the retracted headline. |
| **4b. Isotropic, sweep corr** | fixed amp, vary correlation length, extinction ON | white (corr 0) deficit 0.62; smooth (corr ≥1.5) deficit ~1.1 | Confinement tracks gradient *content* (steep→confines, smooth→none). Consistent with σ_τ scaling **or** with termination-at-steep-gradients — does not by itself distinguish them. |
| **2. Amplitude-invariance** | rescale whole field ×α, **extinction OFF**, in-flight (30 steps), white | deficit 1.03 / 1.09 / 0.96 for α=0.5/1/2 | With extinction off, **no confinement** and no α-trend. The Test-4 effect is not present without extinction. |
| **2b. Is it extinction? (paired)** | same grid/field/budget, in-flight, **extinction ON vs OFF** | deficit **1.03 (ON)** and **1.09 (OFF)** | **No early-time velocity gap either way.** The front is not slowed by isotropic patterning. A σ_τ mass would slow it from t=0. |

## Interpretation (what the substrate actually does)

Putting Tests 2, 2b, 4, 4b together:

- **No velocity gap.** At early in-flight times the patterned front travels as far as (slightly farther than) the uniform front, with or without extinction (Test 2b: 1.03 / 1.09). A dispersion-relation mass slows propagation immediately; this does not. So there is **no σ_τ-type propagation mass**.
- **The confinement is late-time termination.** The strong deficit (Test 4, 0.62) appears only by fixed point, and only with extinction on. It is fronts reaching high-ρ gradient peaks, dropping below the "no positive-Σ continuation" threshold, and **stopping**. That is worldline termination (finite range by absorption/decay), physically distinct from a mass (massive-but-continuing propagation).
- **Two responses to structure, both wrong-object for a Higgs.** Anisotropic patterning → a crystal (channels). Isotropic patterning → termination at peaks. A Lorentz-scalar boson mass is neither a lattice nor a decay; it is a smooth, isotropic, propagation-preserving gap. The native ρ-field delivers neither.

This is the crystal-vs-knot theme again, sharpened: the substrate's cheap responses to structure are crystalline channeling and worldline termination. A σ_τ mass would need an amplitude-invariant field that *slows* worldlines without killing them, and the certified substrate has no such field.

## Tier impact (corrected)

The retracted headline would have softened `Paper_113` row 10 (substrate-Higgs). **It should not.** Row 10 stays OPEN / asserted. What E1 adds is *diagnostic*, not a grounding: the H2/σ_τ route does not realize a mass on the certified substrate's native field, because that field channels or terminates rather than dispersively-masses. This sharpens the open question rather than closing it, and it makes the H1 (inserted-τ_H |D_μφ|²) leg comparatively more likely to be where any real ED gauge mass lives — since H1 gets mass from a gauge coupling to an amplitude, not from a gradient of the propagating field.

## What survived, what didn't

- **Survived:** the field-mapping correction (Σ reads ρ); the anisotropic→crystal finding (Test 3, clean and amplitude-robust); the observation that the substrate has no amplitude-invariant native field.
- **Did not survive:** "isotropic patterning grounds a σ_τ-like mass." The follow-up tests show that confinement is extinction/termination, not a velocity gap.
- **Method lesson (banked):** the density-holds discriminator is necessary but **not sufficient** — it rules out sparse internal holes but not termination at a confining boundary. The sufficient test is the early-time velocity gap with extinction off (Test 2b). Add that to the probe-hygiene kit.

## Next (revised)

1. **Do NOT go to E2 (formation) yet.** E2 tests whether a condensate *forms*; but E1 shows the native ρ-field would not turn a formed isotropic condensate into a mass anyway. Formation of the wrong object is not worth the expensive shared-bottleneck rung.
2. **Reframe onto the H1 leg.** The live question is whether a gauge mass can arise on the substrate from a *coupling to an amplitude* (H1, |D_μφ|²-analog) rather than a *gradient of the propagating field* (H2/σ_τ). That is a different probe: introduce a second (scalar-like) participation channel and test whether a gauge-like channel coupled to its amplitude acquires a velocity gap. Scope it before building.
3. **Kick the σ_τ faithfulness finding upstream.** Arc M's σ_τ assumes an amplitude-invariant bandwidth field; the certified substrate has none. Either the reference Σ is too thin to carry σ_τ (needs a genuine rule-type bandwidth field added), or σ_τ's amplitude-invariance is an idealization. This belongs in the Arc M / `Paper_113` open-questions, and it is the real gate under the whole mass sector.
