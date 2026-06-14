# Phase-3 GR — The Band-Level Sim, and the Honest Limit of Simulation on the Preferred-Frame Front

**Foundations build-and-run — the band-level (`F`-native) test, evolving explicit bandwidth bands under conservative vs dissipative rules. Not a corpus edit, not a new primitive. Sim: `evaluation/DynamicalBandwidth/band_level_ppn.py`. This is the capstone of the simulation route on `α₁, α₂`: it confirms the mechanism is structurally real and self-consistent, and it marks precisely where simulation stops and analysis must take over.**

The moving-binary (field-level) sim *imposed* the conserved/dissipative split. This band-level sim evolves the two bands by their own rules — metric band P04-conserved, directed flux P11-dissipated — and reads off whether they behave differently, letting the split's *structural reality* emerge rather than be assumed.

**Crank rail (load-bearing, and stated plainly to the reader after several over-corrections):** report exactly what the sim shows, what it imposes, and what it cannot reach. The honest finding is that this confirms the picture's self-consistency but does **not** settle the two real questions (which band carries which physical effect; the absolute magnitude), because those are multiscale/analytic, not simulable.

---

## 1. What the sim evolves

A Gaussian source moves at `w` through a static 2D lattice (the cosmic frame). Two bands:

- **Metric band `b` — P04-conserved.** Per tick: symmetric P02 sharing (conserves the sum) plus P11 commitment that moves `b` into a matter channel (conserved overall). A conserved scalar.
- **Directed flux `J` — P11-dissipated.** Sourced by the moving matter current (`κρw`, curl-bearing), transported, and drained at rate `Γ ∝ ρ` where commitment is active. A dissipated vector.

Nothing tells the metric what `g_{0i}` "should" be; the two bands evolve by their own conservative/dissipative rules, and the fields are measured afterward.

## 2. Results

| measurement | value | reading |
|---|---|---|
| P04 conservation (`b` + matter channel) | error `1.5×10⁻¹⁵` | the metric band is conserved to machine precision |
| conserved-band field at far annulus | `U_far = 8.6` (nonzero) | conserved scalar ⟹ **long-range, unscreened** field (Newton + frame-drag carrier) |
| dissipative flux far, drain off → on | `2.0×10⁻⁴ → 6.9×10⁻⁵` (×0.35) | the drain **suppresses** the dissipative flux |
| preferred-frame proxy `J_far/U_far`, off → on | `2.3×10⁻⁵ → 8.0×10⁻⁶` | the drain suppresses the flux *relative to* the conserved field |

So the two bands behave **structurally differently** under the *same* moving source: the conserved scalar gives a long-range field the drain cannot touch (conservation ⟹ no screening), while the dissipative flux is suppressed by the drain (dissipation ⟹ screening). With these (modest, grid-resolvable) parameters the flux suppression is `~3×`; it grows with the drain strength/range, exactly as the Yukawa picture predicts.

## 3. What this settles — and what it does not

**Settles (qualitative, structural):**
- The conserved/dissipative split is a **real structural difference** between the two bands, not a single imposed knob. P04-conservation genuinely produces an unscreened long-range field; P11-dissipation genuinely produces a screened one. The two coexist under one source. This is the mechanism the `Γ`/moving-binary verdict invoked, now shown to be a structural feature rather than an assumption about one equation.

**Does NOT settle (the two real questions):**
1. **The band assignment.** The sim shows the conserved band is unscreened and the dissipative band screened — but *which physical effect rides which band* (does the legitimate frame-dragging live in the conserved sector, the preferred-frame wake in the dissipative sector?) is an assignment the sim does not decide. If frame-dragging rode the dissipative band, the drain would kill it; the verdict's safety needs it on the conserved band, and that is an analytic claim about the emergent metric, not something this lattice proves.
2. **The absolute magnitude.** The physical drain range is the *substrate* scale (`~ℓ_P`); a real system is `~10⁴⁴×` larger. No lattice spans that. The sim shows the *direction* (drain suppresses the flux) and the *scaling*, never the number.

## 4. The honest limit: this is where simulation stops

Across four simulations — `directed_flux.py` (vector sector + screening functional), `boost_noncovariance.py` (the wake is real, `α₁` not symmetry-protected), `moving_binary.py` (mechanism at the field level), and this band-level run — the preferred-frame front has been pushed to the edge of what simulation can do. Every sim agrees and is self-consistent; **none can reach the absolute `α₁`**, because the physics spans the substrate-to-system scale gap (`ℓ_P` screening vs astronomical orbits), and the band assignment is a property of the *emergent* metric, not the microscopic lattice. **Settling `α₁` is therefore a multiscale / effective-field-theory problem: coarse-grain the substrate dynamics to the emergent khronometric action and read off its preferred-frame couplings.** That is a hard analytic derivation (the same class of problem as deriving any condensed-matter EFT's transport coefficients from microscopics), and it is the genuine remaining frontier — not a simulation.

## 5. Verdict, and the honest standing of the whole front

**The band-level sim confirms the conserved/dissipative split is structurally real and self-consistent, and thereby marks the honest limit of the simulation route.** The preferred-frame front now stands as:

- **Established (robust):** ED is not boost-covariant, so `α₁` is not symmetry-protected (it is generically nonzero) — the arrow's first liability. The preferred-frame wake is real and `∝ w`. A dissipative-reserve screening mechanism exists and demonstrably suppresses the dissipative sector.
- **Leans safe (mechanism identified, self-consistent, but unproven in magnitude):** if the screening range is substrate-scale (`~ℓ_P`) and the frame-dragging rides the conserved band, then `α₁ ≈ 0` with frame-dragging and MOND preserved. Both conditions are motivated and now shown structurally possible, but neither is proven, and the magnitude is not computed.
- **The genuine open problem (analytic, hard):** the multiscale/EFT derivation of the emergent khronometric couplings — which would fix the band assignment and the magnitude together. Simulation cannot do it.

**So the honest one-line standing: ED's preferred-frame front is OPEN, with the mechanism identified, demonstrated, and self-consistent, leaning safe — and the remaining work is a hard analytic coarse-graining problem that no simulation will settle.** This is a clean, well-documented resting point for the arc: not a victory (the number is not computed and not faked), not a defeat (no inconsistency found; the mechanism works as far as it can be tested), but an honest frontier.

## 6. Next — two legitimate options

1. **Attempt the analytic EFT derivation** — coarse-grain the substrate (the two-band dynamics) to the emergent khronometric action, derive the preferred-frame couplings and the band assignment. This is the only thing that closes the front, and it is a genuine, hard research problem that may or may not yield.
2. **Bank the arc here.** The seven-step preferred-frame chain (Route A → B → η → vector sector → λ_J → Γ → both sims) is complete, documented, and self-consistent, with the open frontier sharply identified. It is a natural, honest stopping point.

---

*Band-level F-native sim (`band_level_ppn.py`): two bands under a moving source — metric band P04-conserved, directed flux P11-dissipated. Confirms (machine-precision conservation; measured screening) that the conserved/dissipative split is a real STRUCTURAL difference (conserved → long-range unscreened; dissipative → drained/screened), not one imposed knob. Does NOT settle the two real questions: the band assignment (which sector carries frame-dragging vs the wake) and the absolute magnitude (drain range ~ℓ_P, ~10⁴⁴ below any lattice). Marks the honest LIMIT of simulation on this front — settling α₁ is a multiscale/EFT problem, not a sim. Honest standing: preferred-frame front OPEN, mechanism identified + demonstrated + self-consistent, leans safe, remaining work = a hard analytic coarse-graining derivation. A clean resting point: not a victory, not a defeat, an honest frontier. No corpus edits, no new primitives; Einstein not derived; the number not faked.*
