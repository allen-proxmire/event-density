# Arc BH — Memo 4: Information and Evaporation

**Status:** Third technical memo of Arc BH. Consolidation-pattern memo grounded in DCGT + P11 commitment-irreversibility.

**Date:** 2026-05-01

---

## 1. Purpose

This memo:

- Distinguishes **committed** vs **uncommitted** structure at the substrate level — the load-bearing ED ontological split that replaces the standard QFT-on-curved-spacetime treatment of "information."
- Shows why horizons block committed structure but **do not** block entanglement.
- Derives evaporation as **participation re-routing** around a decoupling surface, not as Hawking-spectrum thermalization (the spectrum derivation is reserved for BH-5/BH-6 and remains explicitly out of scope here).
- Demonstrates that ED, by construction, has no information-loss paradox, no firewall paradox, and no complementarity contradiction. These paradoxes are artifacts of imposing global unitarity + monogamy + geometric boundary structure simultaneously on a setting where ED imposes none of those conditions.

This memo is consolidation-pattern: it assembles results already present in ED-06 §7.2 and ED-10 §8.3–§8.5 and routes them through Arc D (DCGT) + BH-2 (decoupling surface) + P11 (commitment irreversibility) into a single substrate-grounded account.

---

## 2. Upstream Foundations

This memo builds on:

- **ED-06 §7.2** — information preservation + horizon decoupling. Information at the substrate level is identified with committed participation history; horizons are surfaces where cross-bandwidth between sides falls below the hydrodynamic-window resolution.
- **ED-10 §8.3–§8.5** — substrate-level information flow, entanglement structure, thermal-like behavior near horizons. Establishes that what looks "thermal" from outside is a coarse-grained reading of saturated cross-bandwidth statistics.
- **BH-2** — horizon-as-decoupling-surface under DCGT. The decoupling surface is defined by $|\nabla\rho|\cdot\ell_P^2/\rho_\mathrm{local} \gtrsim \log(R_\mathrm{cg}/\ell_P)$, at which $\Gamma_\mathrm{cross}$ falls below hydrodynamic-window resolution.
- **BH-3** — singularity replacement by saturated participation zone. Establishes that the interior remains finite and that committed structure inside the horizon does not run to a singular endpoint.
- **P11 (commitment irreversibility)** — substrate primitive: once a participation event commits, the commitment cannot be reversed. P11 is what makes "information" a substrate-level concept rather than a derived bookkeeping device.
- **Arc D (DCGT)** — bandwidth suppression mechanism + multi-scale expansion. Provides the formal $\Gamma_\mathrm{cross}$ structure used here.
- **Arc SG** — SG-4 modified Poisson equation + SG-6 weak-field prerequisites. Sets the gravitational profile that determines where decoupling occurs.
- **Arc ED-10** — acoustic-metric scalar-tensor covariantization. Provides the kinematic geometry against which "horizon" is defined as a coarse-grained surface.

---

## 3. Information vs Entanglement: Substrate Distinction

The key substrate distinction is between two structurally different forms of correlation:

**Committed structure (information).** A pattern in the substrate that has gone through P11 commitment — i.e., participation events have been irreversibly recorded in the local ED-history. Committed structure at point $A$ can only be "read" by point $B$ if there exists a participation pathway from $A$ to $B$ across which substrate events can propagate. This requires nonzero **cross-bandwidth** $\Gamma_\mathrm{cross}$.

**Uncommitted structure (entanglement).** A correlation potential between two regions: the joint participation-amplitude structure prior to commitment. Uncommitted structure does not require ongoing cross-bandwidth between the two regions — it is set up by the prior participation history that produced the pair, and it persists as a correlation in joint outcomes whenever commitment events occur.

The structural difference:

- **Committed structure transmission** requires nonzero $\Gamma_\mathrm{cross}$ at the surface separating sender and receiver.
- **Entanglement amplitude** depends on the correlation structure laid down at pair-formation; once formed, it does not require ongoing cross-bandwidth to persist.

Schematically:

$$
\Gamma_\mathrm{cross} \to 0 \quad\Rightarrow\quad \text{committed structure blocked}
$$

but

$$
\text{entanglement amplitude remains finite}
$$

because the entanglement amplitude depends on the joint amplitude structure of the participation pair, not on the ongoing bandwidth between its two ends. In standard QFT terms: a horizon blocks signaling but not pre-existing correlations. In ED terms: a horizon blocks committed structure transmission but not uncommitted structure persistence.

This is not a new claim; it is the substrate translation of the standard quantum-information no-signaling theorem applied at a horizon. What is new in ED is that both sides — committed and uncommitted — have substrate-level definitions, so the no-signaling-but-correlations-persist behavior is **derived** rather than postulated.

---

## 4. Why Information Cannot Cross a Horizon

From BH-2, the decoupling surface is defined by the cross-bandwidth suppression:

$$
\Gamma_\mathrm{cross}(\mathbf{x}) \sim \exp\!\left[-\alpha\,\frac{|\nabla\rho|\,\ell_P^2}{\rho_\mathrm{local}}\right]
$$

with the decoupling surface at $|\nabla\rho|\cdot\ell_P^2/\rho_\mathrm{local} \gtrsim \log(R_\mathrm{cg}/\ell_P)$, beyond which $\Gamma_\mathrm{cross}$ falls below hydrodynamic-window resolution.

The argument:

1. Committed structure transmission across a surface $\Sigma$ requires nonzero $\Gamma_\mathrm{cross}$ across $\Sigma$ — without ongoing cross-bandwidth, no participation event on side $A$ can register as a participation event on side $B$.

2. At the decoupling surface, $\Gamma_\mathrm{cross}$ is below hydrodynamic-window resolution. From the coarse-grained continuum perspective accessible to any external observer, the cross-bandwidth is effectively zero.

3. Therefore committed structure cannot cross the decoupling surface. Information, in the substrate sense, does not pass through a horizon.

**This is not a causal prohibition.** ED has no fundamental light-cone primitive — light cones emerge as level sets of the acoustic metric (Arc ED-10), which is itself a coarse-grained reading. The prohibition against information crossing the horizon is a **participation-bandwidth prohibition**: the substrate channels that would carry committed structure have their bandwidth suppressed below resolution.

The distinction matters for two reasons:

- It does not require any global causal-structure argument; it follows from local bandwidth suppression.
- It is consistent with finite-$\Gamma_\mathrm{cross}$ tunneling behavior near (but not beyond) the surface — the suppression is exponential, not a hard cutoff. This will be load-bearing for the evaporation mechanism in §5.

---

## 5. Evaporation as Participation Re-Routing

The evaporation mechanism follows directly from the structure established above:

1. **Horizon blocks committed structure.** Per §4, committed structure does not cross.

2. **Uncommitted structure can straddle the surface.** Per §3, entanglement amplitude does not require ongoing cross-bandwidth — it is set by joint participation structure at pair formation. Pair-amplitude structures can therefore exist with one "leg" inside and one "leg" outside the decoupling surface without violating §4.

3. **Local participation gradients near the horizon support pair-creation-class events.** The decoupling surface is where $|\nabla\rho|\cdot\ell_P^2/\rho_\mathrm{local}$ is large. Large local gradients in the participation field are precisely the conditions under which uncommitted pair structures emerge — this is the substrate-level reading of vacuum pair production in a strong field, but here it is gradient-driven rather than externally-sourced.

4. **One branch commits inward, the other commits outward.** When commitment events occur on these straddling pair structures (as they generically do, via P11), the inward leg commits as part of the interior saturated zone (BH-3), and the outward leg commits as part of the exterior radiation field. The pair was uncommitted at formation; its commitment events are local and irreversible.

5. **This is participation re-routing.** No committed structure crosses the horizon. Instead, the **correlation structure** that was laid down at pair-formation is now distributed across an interior commitment + an exterior commitment, with the joint correlation preserved.

The outward branch inherits correlation structure from the interior branch via the joint amplitude that produced the pair. Globally, the correlation structure is preserved — no information is destroyed; it has been **re-routed** through pair-creation-class events at the decoupling surface, with one half ending up outside and one half ending up in the interior saturated zone.

What an external observer reads as "thermal Hawking radiation" is, in ED, the coarse-grained statistics of the outward-committed legs of these straddling pair structures. The thermal character (and the spectrum, and the area-law-1/4 entropy) are not derived in this memo — they are reserved for BH-5 / BH-6. What is derived here is the **substrate-level mechanism**: evaporation is participation re-routing, not information destruction.

---

## 6. Why ED Has No Information Paradox

The standard information-loss paradox arises by combining four assumptions:

(a) Global unitarity of the full quantum state.
(b) Global Cauchy-data evolution on a connected spacelike surface.
(c) A geometric horizon as a sharp boundary.
(d) Monogamy of entanglement enforced at that geometric boundary.

ED imposes **none** of these assumptions at the substrate level:

- **No global unitarity requirement.** ED is local and irreversible at the substrate level (P11). Unitarity is a coarse-grained continuum property of the QM-emergence sector (Phase-1, T1–T16) for closed sub-systems in the canonical-ED hydrodynamic window. It is not a global constraint on the substrate. There is therefore no global-unitarity requirement that must be reconciled with horizon-blocked information.

- **No need for global Cauchy data.** ED commits events locally; there is no spacelike surface on which the entire universe's state must be specified. The "information" question is answered locally, event by event, by P11.

- **No firewall.** Firewalls arise from forcing entanglement-monogamy at a geometric surface where complementarity also requires preservation of effective-field-theory smoothness. In ED, the horizon is a **decoupling surface**, not a geometric boundary. There is no requirement to enforce monogamy at it because the surface is a coarse-grained statistical feature of $\Gamma_\mathrm{cross}$, not a knife-edge geometric locus.

- **No complementarity contradiction.** Complementarity arises from asking whether information is "inside" or "outside" — a question that presupposes a sharp geometric boundary. In ED the horizon is not a geometric boundary; the relevant question is whether commitment events have occurred on a given side, and that question has a local answer for each event. There is no contradiction to reconcile.

- **No information-loss paradox.** Information never crosses the horizon (§4); committed structure inside the horizon remains finite (BH-3); evaporation re-routes correlation structure (§5). The exterior radiation carries correlation with the interior commitments via the joint amplitude structure of the pair-creation events. No committed structure is lost.

The structural point: **the information paradox is not solved in ED; it does not arise.** The four assumptions that generate it are not present at the substrate level. They are continuum-level assumptions imposed in standard treatments because the underlying ontology is a global field on a fixed spacetime. ED's ontology is local participation events with irreversible commitment, and at that level the paradox-generating assumptions are not available to be made.

This is the same structural pattern as the singularity result in BH-3 (substrate constraints forbid divergence) and the horizon result in BH-2 (decoupling surface emerges from bandwidth suppression). ED handles black-hole "paradoxes" by not generating them in the first place, rather than by resolving them within a paradox-generating framework.

---

## 7. Deliverables

This memo produces:

- **Substrate-grounded committed/uncommitted distinction** as the ED-level reading of information-vs-entanglement, derived from P11 + DCGT.
- **Derivation of why information cannot cross a horizon** as a participation-bandwidth prohibition (not a causal prohibition), using BH-2's decoupling-surface condition.
- **Substrate-level evaporation mechanism** as participation re-routing through pair-creation-class events at the decoupling surface, with global correlation preserved.
- **Structural resolution of the information paradox** by showing that the four paradox-generating assumptions (global unitarity, global Cauchy data, geometric boundary, monogamy at boundary) are not imposed at the ED substrate level.

Hawking spectrum derivation, area-law $1/4$-coefficient derivation, and explicit wave–BH scattering match are explicitly **not** in scope here. They are the load-bearing new-derivation work of BH-5 (entropy) and BH-6 (scattering).

---

## 8. Recommended Next Step

Proceed to **Arc_BH_5_Area_Law_Entropy.md** — the area-law entropy + $1/4$-coefficient derivation. This is the load-bearing new-derivation memo of Arc BH: it must produce, from substrate primitives + DCGT + the decoupling-surface condition (BH-2) + the saturated-zone structure (BH-3) + the participation-re-routing mechanism (BH-4), an area-law entropy with the correct $1/4$ Bekenstein-Hawking coefficient, or explicitly identify what blocks the derivation.

File path: `theory/Black_Holes/Arc_BH_5_Area_Law_Entropy.md`. Estimated 1–2 sessions.
