# The Quadrupole Rate: ED's Scalar Radiation Is 1/6 of GR's (Same G), So the Radiative Sector Is Substantially Falsified by Binary Pulsars. An Honest Negative Result, and a Structural Tension in the ED Gravity Program

> **⚠️ MAJOR CORRECTION (2026-07-09, AP caught the over-conclusion). The "FALSIFIED" verdict below is RETRACTED; the honest verdict is OPEN.** The 1/6 rate and the scalar-only polarization both assume the emergent metric is the *conformal scalar shadow* `g~1/b` even in the dynamical/radiative regime. But `g~1/b` was DERIVED only for a **static, spherically-symmetric** mass (isotropy forces the conformal form); it was never derived for a time-varying, non-spherical source (a binary), whose emergent metric can carry genuine **tensor** structure (bandwidth *flows*, there is a current, not just a density). So the calc computed only the *scalar sector* of a possibly richer emergent metric, and the clean `1/6` is a missing-piece signature, not a random miss. Two further points AP raised, both correct: (1) binary pulsars are **high-acceleration** (`a ≫ a₀`), the Newton/GR regime, NOT the MOND regime (`a ≪ a₀`, galaxy outskirts) — so at pulsar scales ED should *reduce to GR*, tensor radiation included; the 1/6 came from wrongly applying the low-energy scalar-shadow picture to a high-acceleration system. (2) GR *also* fails an entire domain (galactic rotation without dark matter); calling ED "falsified" while treating GR as correct was asymmetric. **The real open question (the actual hard sub-problem): is ED's full coarse-grained emergent metric, for dynamic non-spherical sources, a genuine dynamical-TENSOR field (so GR emerges as its CG, per Newton ⊂ GR ⊂ ED) — with the scalar breathing mode non-propagating so it does NOT over-radiate (7/6)? Only the static conformal `g~1/b` is derived; the dynamical/tensor sector was CHARACTERIZED, not derived. So the radiative sector is OPEN.** The `P_scalar/P_GR = 1/6` computation below is CORRECT *as the scalar-shadow-only result*; what is retracted is the leap from that to "the radiative sector is falsified." Read the body as "the conformal-only approximation radiates scalar at 1/6," not as a verdict on ED.

**Foundations, gravity / curvature-emergence arc, the quadrupole rate. This completes the radiative-sector analysis, and the result is NEGATIVE for ED gravity, reported straight. The polarization note showed ED radiates a scalar (breathing) mode. This note computes the RATE. Probe: `evaluation/CurvatureEmergence/quadrupole_rate_probe.py`. Binary-pulsar orbital decay measures the total GW luminosity; GR attributes it to TENSOR quadrupole and matches Hulse-Taylor to `~0.1%`. ED must account for the SAME decay with SCALAR quadrupole radiation, and the coupling is NOT free, the same bandwidth field `b` gives the static Newtonian `G` (this session's Gauss law) and the radiation, so the comparison is parameter-free. Result: `P_scalar / P_GR = 1/6` exactly for a circular orbit (derived analytically and confirmed numerically: `0.1667`), holding at `~1/6` across eccentricities (`0.168` at Hulse-Taylor's `e=0.617`), with a small extra scalar MONOPOLE (breathing) term for eccentric orbits that GR has no analog of. So **ED radiates six times too little, predicting orbital decay `~6x` too slow**, a gross `O(1)` mismatch with the `0.1%` GR/pulsar agreement, not a marginal tension. Combined with the scalar-polarization result (ED predicts breathing-mode, LIGO favours tensor), **ED gravity's radiative sector, as a kinematic scalar metric, is substantially falsified by binary-pulsar + GW data**. This is the same wall that ruled out scalar gravity theories. The falsification is STRUCTURAL: the kinematic-scalar-metric stance that gives ED its distinctive MOND-not-GR content (a shadow metric, no dark matter) is exactly what forces the wrong radiation. ED cannot be both a kinematic scalar metric (=> MOND) and reproduce GW/pulsar radiation. Its static/galactic (MOND) results stand; its radiative predictions do not. Honest scope: the exact `1/6` uses the standard minimally-coupled-scalar normalization (ED has not derived its scalar action from the substrate), but the `O(1)`-mismatch KIND is robust.**

---

## 1. The parameter-free comparison

The binary pulsar measures one number: the orbital decay rate, i.e. the total gravitational luminosity. GR predicts it from the tensor quadrupole formula and matches to `~0.1%`. If ED gravity is correct, its (scalar) radiation must account for the *same* observed decay. The crucial point that makes this a sharp test: **the coupling is not free.** The same bandwidth field `b` produces the static Newtonian potential (this arc's Gauss-law result, `Φ ~ GM/r`, coupling `G`) and the radiation, so the radiation coupling *is* that `G`. There is no adjustable parameter to rescale ED's luminosity to fit.

The standard multipole luminosities, for the same source second-moment `M_ij = Σ_i m_i x_i^a x_i^b` and the same `G`:
$$P_{\text{GR}} = \frac{G}{5c^5}\big\langle \dddot Q_{ij}\dddot Q_{ij}\big\rangle, \quad Q_{ij}=M_{ij}-\tfrac13\delta_{ij}M_{kk}\ \text{(reduced, traceless)},$$
$$P_{\text{scalar}} = \frac{G}{60c^5}\Big[\big\langle(\dddot M_{ii})^2\big\rangle + 2\big\langle\dddot M_{ij}\dddot M_{ij}\big\rangle\Big],$$
where the scalar formula follows from a minimally-coupled massless scalar with the same static coupling `G`. The `(\dddot M_{ii})^2` term is the scalar **monopole / breathing** radiation, which GR has no analog of; it vanishes for a circular orbit (constant moment of inertia) and contributes for an eccentric one.

## 2. Result: ED radiates six times too little

For a circular orbit the mass second-moment gives `⟨\dddot Q_{ij}\dddot Q_{ij}⟩ = ⟨\dddot M_{ij}\dddot M_{ij}⟩ = 32\,μ^2 a^4 ω^6` and `\dddot M_{ii}=0`, so
$$P_{\text{GR}} = \frac{32}{5}\frac{G}{c^5}μ^2a^4ω^6, \qquad P_{\text{scalar}} = \frac{16}{15}\frac{G}{c^5}μ^2a^4ω^6, \qquad \boxed{\frac{P_{\text{scalar}}}{P_{\text{GR}}} = \frac16}.$$

The probe confirms it numerically for Hulse-Taylor-like masses:

| eccentricity | `P_scalar / P_GR` | scalar monopole fraction |
|---|---|---|
| 0.000 (circular) | **0.1667** (= 1/6) | 0.0% |
| 0.300 | 0.1673 | 0.2% |
| 0.617 (Hulse-Taylor) | 0.1683 | 0.6% |

So ED's scalar quadrupole luminosity is `~1/6` of GR's tensor quadrupole, robustly across eccentricity, with a small additional scalar-monopole contribution for eccentric orbits. **ED radiates six times too little, so it predicts the binary to inspiral `~6x` too slowly.** GR matches the observed Hulse-Taylor decay to `0.1%`; a factor of `1/6` is off by `~500%`, a gross mismatch, not a marginal tension.

## 3. Why this is a structural tension, not a fixable coefficient

There is no escape within ED gravity as formulated:

- **No free coupling.** `G` is fixed by the static Newtonian limit (the same field radiates), so ED cannot rescale its luminosity.
- **No tensor sector.** The `1/6` and the scalar polarization both follow from "radiation = the scalar bandwidth field." To get GR's tensor rate and polarization, ED would need a *dynamical* tensor metric, which is the Einstein sector the kinematic-metric stance explicitly rejects. Acquiring it means abandoning the kinematic metric, and with it the structural basis for "MOND, not GR."

So the deepest honest statement is a **tension internal to the ED gravity program**: the feature that gives ED its distinctive content, a *kinematic* metric that is a scalar shadow of the bandwidth field (which yields MOND phenomenology and needs no dark matter), is exactly the feature that makes its radiation wrong (scalar, at `1/6` the rate). **ED cannot simultaneously be a kinematic scalar metric (=> MOND, no dark matter) and reproduce binary-pulsar / GW radiation.** This is the same wall that ruled out historical scalar and scalar-dominated gravity theories: the dipole is evadable (universal coupling), but the quadrupole rate and the polarization are not.

## 4. What stands and what falls (honest scope)

- **Stands (quasi-static / galactic).** The metric emergence, `g~1/b` forced holographically in 3D, the Gauss-law Newtonian limit, the relational (background-free) character, and the MOND fits to galaxy rotation curves are all quasi-static results, untouched by the radiative analysis. ED's static and galactic (MOND) gravity is not falsified by this.
- **Falls (radiative).** ED's gravitational-wave predictions, both the *polarization* (scalar breathing, LIGO favours tensor) and the *rate* (`1/6`, pulsars match GR), are wrong, by `O(1)`, unless ED acquires a genuine dynamical-tensor sector (abandoning the kinematic metric). So ED gravity's radiative sector is substantially falsified by binary-pulsar + GW data.
- **The exact number is normalization-dependent, the kind of mismatch is not.** The `1/6` uses the standard minimally-coupled-scalar normalization; ED has not derived its scalar action from the substrate, so the precise factor is uncertain. But any standard scalar gives an `O(1)` ratio `≠ 1` (not `0.1%`), plus a monopole term for eccentric orbits, so the mismatch is robust in kind.

## 5. Net for the ED gravity program

This is an honest negative result, and it is the most consequential finding of the radiative sector. Worked to completion, ED gravity's radiation is wrong in both polarization and rate, and the reason is structural: the kinematic scalar metric that gives ED its distinctive MOND-not-GR, dark-matter-free content forces scalar radiation at `1/6` the observed rate. The program now faces a sharp fork, stated plainly:

- **Keep the kinematic scalar metric** (MOND, no dark matter, distinctive): accept that the radiative sector is falsified by pulsars and LIGO, so ED gravity is at best an approximate quasi-static / galactic theory, not a complete theory of gravity including radiation.
- **Add a genuine dynamical-tensor sector** (to fix the radiation): this abandons the pure kinematic metric, undercuts the structural argument for MOND-not-GR, and moves ED toward a GR-like dynamical metric, i.e. gives up the distinctive content.

Either way, the honest verdict is that ED gravity as a kinematic scalar metric is **falsified on radiation** while succeeding on static/galactic gravity. Paper E should carry this straight: the radiative sector is not a "live tension to be resolved" but a substantial, structural falsification of the pure-kinematic-metric picture on GW/pulsar data, coexisting with the static/MOND successes. This is exactly the kind of sharp, falsifiable consequence that makes ED a real theory, and here the consequence comes out against it.
