# The Diffusion Arc — ED Diffuses (Linear/Fickian); the UDM's Degenerate Mobility Is the Capacity the Bare Rule Lacks

**Evaluation result — three tests probing "can the certified substrate diffuse, and does it reproduce AP's empirically-validated UDM degenerate mobility M(ρ)=M₀(ρ_max−ρ)^β?" Sims: `tracer_diffusion_test.py`, `mobility_recovery_test.py`, `crowding_capacity_test.py`. Verdict, two clean parts: (1) YES, ED diffuses — a worldline tracer and a front packet both disperse diffusively (tracer MSD∝t^1.18; packet R∝t^0.51 = Fickian), robustly. (2) NO, it does not reproduce the UDM degenerate mobility — the diffusion is LINEAR (constant mobility, amplitude-independent, does not slow as density rises). The sharp reason: the certified rule has NO CAPACITY (ρ grew to ~3.0, well past the nominal 1.0, with fronts still diffusing freely at α≈0.5). The UDM = linear diffusion + a capacity ρ_max; the substrate supplies the diffusion, not the capacity. The capacity (max packing / jamming) is the real, data-validated constitutive ingredient the bare worldline rule is too austere to contain — not a flaw, the physical heart of the law.**

---

## The three tests

**1. Tracer (`tracer_diffusion_test.py`) — a single worldline in a disordered medium DIFFUSES.**
MSD ∝ t^1.18 and the velocity autocorrelation decays to ~0 within ~2 steps (direction decorrelates). A worldline scattering off ρ-disorder random-walks — Einstein's Brownian setup. This *reconciles* with #3 (which found the deposited-density *field* obeys eikonal/transport in smooth setups): the **walkers** disperse diffusively (Lagrangian), while the **cumulative deposited field** evolves by transport (Eulerian) — different objects, both true. Eikonal in smooth media, diffusive in disorder.

**2. Mobility recovery (`mobility_recovery_test.py`) — D_eff is flat in background density.**
Tracer diffusivity across ρ₀ = 0.1…0.8: D_eff ≈ 0.94–1.13 (no decrease toward capacity), α ≈ 1.3–1.4 throughout, β-fit = −0.10 (R²=0.38, no power law). No degenerate mobility from background density. (Background density gives no *contrast*, so the strain term — which penalizes moving into dense cells — cancels; this test moved the wrong knob, which motivated test 3.)

**3. Crowding / capacity (`crowding_capacity_test.py`) — the packet diffuses Fickian, and never degenerates.**

| base ρ | spread exp α | core ρ: start→end | regime |
|---|---|---|---|
| 0.05 | 0.51 | 0.53 → 3.03 | diffusive |
| 0.20 | 0.51 | 0.68 → 3.21 | diffusive |
| 0.35 | 0.52 | 0.85 → 3.43 | diffusive |

A localized packet of fronts (filling its own core via deposits) spreads as R ∝ t^0.51 = **Fickian diffusion**, **amplitude-independent**, and the exponent **stays ~0.5 as the core density climbs to ~3.0** — far past the nominal capacity 1.0. **The certified rule has no ρ_max: ρ grows unbounded, fronts are never trapped, mobility never dies.** So the substrate's diffusion is the linear (heat-equation) class, not the UDM's degenerate porous-medium class.

## Verdict — the UDM ↔ substrate relationship

**UDM = linear diffusion + a capacity (ρ_max).** The certified substrate supplies the diffusion bottom-up (tests 1 & 3), for free. It does **not** supply the capacity — because the bare rule has no maximum packing / jamming / ρ_max. **The degenerate mobility IS the capacity, and the capacity is the one ingredient the substrate doesn't contain.**

This does **not** touch the UDM's validity: M(ρ)=M₀(ρ_max−ρ)^β is empirically validated across 11 materials / 8 domains (R²>0.986) — the capacity (materials jam at max packing) is the *most physical* part of the law, not an unjustified assumption. So:

- **"Is the UDM ED coarse-grained?" — axiomatically YES** (ED's principles → the unique dissipative PDE; AP's derivation, data-validated, untouched).
- **Bottom-up from the certified substrate** — it gives the **diffusion**; the **degenerate mobility comes from the capacity**, a real validated constitutive law the bare rule doesn't yet generate. To get the UDM bottom-up, the substrate rule needs a saturation/capacity term — *not foreign to ED*: the GR-keystone work already introduced P04 bandwidth-capacity (b→0). The capacity is a known ED ingredient, just absent from this minimal certified rule.

**Crank-rail:** the tracer result flipped my "no diffusion" prior (ED does diffuse). The degenerate-mobility recovery came back negative across two independent tests; reported straight, no shield — the negative is located precisely (no capacity in the rule), not waved away. Upside-only test: the UDM stands on its data regardless. **Notebook documentation; no external prediction (per AP).**

---

*Diffusion arc (3 tests). (1) ED DIFFUSES: tracer MSD∝t^1.18, VACF→0; packet R∝t^0.51 Fickian — robust. Reconciles #3 (walkers disperse diffusively = Lagrangian; deposited field = transport = Eulerian; eikonal in smooth media, diffusive in disorder). (2) NOT the UDM degenerate mobility: D_eff flat in density (β=−0.1), packet α=0.5 amplitude-independent and stable as core ρ→3.0. (3) Sharp reason: certified rule has NO capacity (ρ unbounded, fronts never trapped). UDM = linear diffusion + capacity(ρ_max); substrate gives the diffusion, not the capacity. Capacity = validated constitutive law (jamming, 11 materials), the physical heart of the UDM, absent from the bare rule (but = P04 bandwidth-capacity from the GR work, an ED ingredient not in this minimal rule). UDM ED-CGed axiomatically (yes, validated); bottom-up = diffusion yes + capacity-as-added-ingredient. Notebook only; no external prediction (per AP).*
