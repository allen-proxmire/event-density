# §10 — Matter: the spinor, and mass without mass

*Draft v1, 2026-07-10. Register: peer-facing. Tiers: substrate→Dirac **form-complete** (operator form-forced, continuum limit computed, undoubling verified) with structure/value **inherited**; binding mass **measured** (V5-conditional); the fundamental Higgs mass **inherited**. Point-toward. Primary sources (read-first): `T4_14_Closure_SubstrateToDirac`, `Paper_106_DiracEquation`, `Paper_MassWithoutMass_BindingInertia` (this session). Computations: `chiral_3p1d.py`, `mass_from_binding_probe.py`.*

---

**The arrow's job here.** The matter sector uses the arrow three ways, and this section is organized around them. The arrow **undoubles** the lattice spinor, cutting the Nielsen–Ninomiya sixteen species to one. The arrow makes a lone excitation **massless**, moving always at the substrate speed, which is what forces mass to come from binding. And the arrow's commitment rate sets a **clock**, which turns out to be time dilation and not mass, a distinction the substrate had entangled and this section separates.

The matter sector splits into two questions: does ED produce the Dirac spinor, and does it produce mass? The spinor is form-complete and structure-inherited, the standard ED shape. Mass is the more interesting result, because ED at first looks unable to make it at all, and then makes it exactly where most of it actually lives.

## The spinor: substrate to Dirac, form-complete

The Dirac operator's *form* is forced: it is the unique first-order Clifford-linear factorization of the substrate's Klein–Gordon operator, `D = iγ^μ∂_μ − mc/ℏ`. Its *substrate continuum limit* is now computed, not asserted: retarded transport on the participation graph gives `D(p) = Σ γ^μ(e^{ip_μ} − 1) ≈ iγ^μp_μ` near `p = 0` (`Paper_106`, corrected this session from an earlier "asserted via inheritance" status). And the **arrow undoubles it**: a naive Hermitian lattice Dirac operator has sixteen doublers, and the arrow's retardation is exactly the Wilson term that removes them, leaving a single species at the origin, verified directly (`chiral_3p1d.py`). This is ED's concrete escape from Nielsen–Ninomiya, a relational graph plus a genuine (non-Hermitian) arrow.

The single 3+1D survivor is a full, vector-like Dirac point (both chiralities), which is exactly right: the Dirac fermion *is* L⊕R, and its handedness is the separate weak-force question settled in §9. So the "vector-like survivor" is a feature of a correct Dirac reduction, not a gap.

What is inherited is the standard ED value/structure layer: the Cl(3,1) spinor structure (via the acoustic-metric signature, the continuum arc), the metric signature, and the mass value. The one route that would make the spinor fully substrate-native, building the 4-spinor from graph degrees of freedom, runs into the same channel-topology wall as the representation spectrum (§7, §13): canonical channels carry no topology to be a spinor's, and the program that would supply one is unbuilt. So the spinor is form-complete and inherited-structured, with its one deepening blocked at the rep-spectrum wall.

## Mass looks impossible for a single front

ED's certified rule is **ballistic-or-extinct**: a front advances one hop at the maximal speed or it dies. There is no dwell, no fractional hop, no slow-but-surviving mode. Rest mass needs exactly that missing mode, something that lets a thing sit slower than `c`. So a lone ED front cannot have rest mass; it moves always at `c`.

That looks like a failure, and Allen's reframe turns it into the mechanism: a lone front shares the cosmic horizon's defining feature, `c`-moving, no rest frame, massless. Mass is therefore not a property a front can carry. If mass exists in ED, it has to come from what a *collection* of fronts can do that one cannot, bind. And this is how most real mass already works: roughly ninety-nine percent of a proton's mass is binding energy, not the Higgs coupling; a box of light has rest mass though every photon in it moves at `c`.

## Mass from binding, measured

The test is whether ED's cross-chain coupling V5, in its known finite-reach retarded attractive form, confines massless fronts into a bound composite. On the certified simulator it does (`Paper_MassWithoutMass`):

- A **free front** moves at `c` (`v = 0.98`).
- With the coupling **off**, a cluster disperses (extent `28 → 55`): unbound.
- With the coupling **on**, the cluster is **confined** (extent stays `1.4 – 2.3`) while each constituent keeps moving at `c`, and the composite's center of mass is **sub-luminal** (`v ≈ 0.5 < c`). This is a genuine bound state of massless-moving parts.

The composite has the defining property of mass, **inertia**. Under a uniform force the bound composite responds at `v_x = 0.72`, while an *unbound* cluster of the same size responds at `0.97` (≈ the free front). The resistance is from binding, not from averaging, and that gap is the controlled, load-bearing result. And the composite heads toward rest as it grows: the center-of-mass drift shrinks monotonically with constituent count (`0.54 → 0.31` from eight to thirty-two), the internal momenta cancelling better in a larger bound state.

This is **mass without mass**: a bound system of `c`-moving constituents has rest energy, hence rest mass, and it is the physically dominant form of real mass. It is native to ED's dynamics, conditional on V5, which is a faithful structural addition (finite-reach, retarded, attractive, matching the corpus kernel) but not shown to be forced by the bare primitives.

## Mass is not time dilation

The substrate has a *second* way to make something move slower than `c`, and it is important that it is not mass. A front carrying commitment-memory dwells, re-committing in place, which lowers its advance rate. Push such a front and its forward drift tracks its path speed exactly (`v_x/path = 1` at every memory level): it has **no directional inertia**. A slow clock, not a mass. This is **time dilation**, and it is the same commitment-rate factor that appears in gravity's sparse-commitment parameter (§5), which is why gravitational time dilation and this share a factor. Only *binding* produces the directional inertia (`v_x/path < 1`) that is mass.

So two things the substrate had entangled come apart cleanly: **commitment sparseness sets the clock (time dilation, and it ties matter to gravity through the shared factor); binding sets the mass.** They are distinct phenomena, and the arrow is behind both, once as the commitment rate, once as what makes the bound constituents massless in the first place.

## Scope

- Binding mass is native but **V5-conditional**: V5 is a structural addition, not shown primitive-forced (the bare substrate's native cross-chain coupling was separately measured to be dispersive).
- This is **binding** mass, the dominant form. The **fundamental Higgs/electroweak mass** (electron, current-quark, W/Z from spontaneous breaking) is a separate mechanism, inherited; the condensate route to it comes up empty on the certified field.
- The rest limit is an extrapolated size-trend, not a measured zero; the equivalence-principle reading of the uniform-force response is a consistent interpretation, not a proof.
- No numerical mass values, and no generations, masses, or mixings, those are the inherited value layer (§11) and the rep-spectrum content (§7, §13).

## What this buys the report

The matter sector is the arrow three times over: undoubling the spinor, making the lone front massless (so mass must be binding), and setting the clock that is time dilation. The mass-from-binding result is a genuine native mechanism for the dominant form of real mass, measured on the certified substrate, and the clean mass/time-dilation split reuses the same commitment factor that runs gravity's clock, tying the matter and gravity sectors together through the arrow once more. The pieces that stay inherited, the Cl(3,1) structure, the fundamental Higgs mass, the generation spectrum, all point to the same two places the report is honest about: the value layer (§11) and the rep-spectrum wall (§7, §13).

---

*Draft notes for finalization:*
- *Spinor tiers: operator form-forced, continuum limit computed, undoubling verified — do not soften "computed/verified" (this session corrected Paper_106 from "asserted/OPEN"), and do not harden the inherited Cl(3,1)/signature/mass to "derived."*
- *Mass tiers exactly per the paper's audit: confinement + inertia = measured/controlled (keep the unbound-control 0.97 — it is what makes the inertia claim load-bearing); rest limit = extrapolated; EP = interpretation; V5 = structural addition, NOT primitive-forced; fundamental Higgs = inherited. Do not state "ED derives mass."*
- *The mass≠time-dilation separation is a real result and ties to §5 — keep the shared-factor link explicit but do not overclaim it as a derivation of the gravitational parameter.*
- *Generations/mixing → inherited (rep spectrum, #1); keep the "same wall" language consistent with §7/§9.*
- *Length ~1300 words (two-part, carries the biggest new result). Register OK: Nielsen–Ninomiya, Wilson term, Cl(3,1), ballistic-or-extinct, V5 named flat-out.*
