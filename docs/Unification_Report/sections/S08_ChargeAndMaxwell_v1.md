# §8 — Charge and Electromagnetism: a native skeleton, a shadow field

*Draft v1, 2026-07-10. Register: peer-facing. Tiers: charge skeleton **measured** (graph-first, certified substrate); the smooth Maxwell field **analytic + structural** (the coherence-weighted limit is Coulomb; the smooth field is a coarse-grained shadow). Point-toward. Primary sources (read-first): `Paper_ChargeAsTopology_B4` (the skeleton), `Paper_MaxwellEmergentShadow` (the shadow field, this session), `Paper_Continuum_KineticLatticeGas` (why the determinate substrate is not a field-relaxing ensemble).*

---

**The arrow's job here.** Two of the arrow's roles from §3 show up together in the charge sector. Irreversibility (P11) makes the substrate's phase winding single-valued, which is what quantizes charge and protects it. And the arrow's continuum-sorting job decides what electromagnetism *is* in ED: not a fundamental field, but the coarse-grained shadow the determinate substrate casts.

## The skeleton is native and quantized

ED's charge result is reached graph-first: the participation graph is asked which topological invariants it carries, and only then is the survivor compared to charge. The survivor is the U(1) holonomy on cycles. Committed single-valued polarity (P09 phase made single-valued by P11 commitment) forces its holonomy to an **integer winding `w ∈ ℤ`** — exactly `π₁(U(1)) = ℤ`, to machine precision. That winding is **conserved and irreversibility-protected**: changing it would require uncommitting a polarity, which P11 forbids. And it sources a field topologically, obeying the **integral Gauss law** — the circulation around any enclosing loop is `2πw`, independent of the loop's size and shape (B4).

So charge quantization, conservation, and the unscreenable Gauss-law sourcing are structural facts of the ED graph, not inputs. Quantization is `π₁(U(1)) = ℤ`; protection is the arrow. This is the topological skeleton of charge, and it is genuinely native.

The scope of this result is the skeleton, not the values. ED produces an integer winding with no selected magnitude — not the `±1, ∓⅓` spectrum, not the fine-structure constant. Those live in the representation content, which the report inherits (§7, §13). §8's claim is about the *structure* of charge: that it is topological, quantized, and protected. The magnitudes are a separate question, and ED does not set them.

## The smooth field is the coherence-weighted limit — and a shadow

B4 established the skeleton but left one question open: the determinate substrate carries the integer winding and the Gauss law, but it does not produce a determined local `1/r²` field. The per-edge configuration is gauge/sweep-dependent; a determined isotropic Coulomb field appears only if one removes *both* orientation-blindness and P11 — at which point the system is ordinary lattice-field relaxation and no longer ED. B4's open edge was whether the *coarse-grained* limit recovers Maxwell.

It does. The Maxwell action is already latent in the coherence term: `cos²(Δφ/2) ≈ 1 − ¼(∇φ)²`, so the incoherence is the standard `¼(∇φ)²` electrostatic action. Minimizing that coherence action around a point charge gives the **Coulomb field** — the FFT Poisson solve fits `φ ~ A/r` with `p = 1` (3D Coulomb) at `R² = 0.97`, best among the tested exponents, with `φ·r ≈ const` in the near field (`Paper_MaxwellEmergentShadow`, this session). So the coherence-weighted continuum limit of B4's holonomies is Maxwell/Coulomb.

But that is a statement about the coherence-weighted ensemble, not about the determinate substrate. The certified substrate is kinetic and committal — it traps and commits, it does not relax toward a field-minimizing configuration (`Paper_Continuum`). It is Σ-blind to the phase sector. So the determinate substrate does **not** cast the smooth field: B4 §7 resolves negatively for it. The smooth Maxwell field is the thick-limit **shadow** — form native (the charge skeleton is real substrate structure), smooth field coarse-grained (a came-back-no for determinate-dynamics, the same verdict ED reached for the diffusion PDE).

## ED's monist position on electromagnetism

Put the two halves together and the sector has a clean ontology. The charge *skeleton* — winding, quantization, Gauss law — is native substrate structure. The electromagnetic *field* — the smooth `A_μ`, `F_{μν}`, the Coulomb `1/r²` — is not a second fundamental thing sitting beside the substrate; it is what the substrate looks like coarse-grained, exactly as the smooth metric (§5) and the diffusion equation are. ED does not have a fundamental field and a fundamental substrate to reconcile. It has one substrate, and the field is its shadow. That is the same monist move the whole program makes, and electromagnetism is its cleanest instance, because the lattice-to-continuum dictionary here (Wilson's lattice gauge theory) is already standard.

## Scope

- The winding is a structural realization of charge's skeleton. It is not a claim that the winding *is* electric charge, and no electromagnetic *content* is derived.
- The charge magnitudes and the fine-structure constant are not produced (inherited; the spectrum question is §7/#1).
- The skeleton results are on minimal certified arenas (rings, small grids); multi-winding interactions and coupling to matter fronts are not covered.
- The shadow result is analytic (the coherence-action minimizer is Coulomb) plus the structural reading (the determinate substrate does not cast it). It is not a certified-substrate simulation of the field, because the phase sector is Σ-blind, so there is nothing to run there.

## What this buys the report

This is the arrow in the charge sector: irreversibility quantizing and protecting the winding, and the continuum-sorting deciding that electromagnetism is a shadow rather than a fundamental field. It also sets the pattern for §5's metric and the rest of ED's continuum objects — the determined continuum is always the coarse-grained shadow, and charge is where that reading is sharpest. The representation content that would fix the charge *magnitudes* is the open rep-spectrum question, taken up in §7 and §13.

---

*Draft notes for finalization:*
- *Tiers: skeleton = measured (B4 certified sim); Maxwell limit = analytic (the FFT Poisson fit, p=1 R²=0.97); shadow extension = structural. Do not state ED "derives electromagnetism" or "derives Coulomb" — B4 preamble 2 and the Maxwell paper both disclaim it; the claim is coherence-weighted-limit + shadow.*
- *Keep the ±1/∓⅓ spectrum firmly in the "not produced, inherited (#1)" column — this is the boundary B4 is most careful about (graph-first, never charge-first).*
- *The "shadow" framing must match §5 (metric) and §12/§13 so the monist ontology reads consistently across sectors — the determined continuum is always the coarse-grained shadow.*
- *Length ~1000 words. This is a clean two-part box (skeleton native, field shadow); resist re-deriving the B4 fork in detail — cite it.*
- *Register OK: π₁(U(1))=ℤ, holonomy, integral Gauss law, lattice gauge theory, DCGT, Σ-blind named flat-out.*
