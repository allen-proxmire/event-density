# Gauge_07 — The Yang–Mills Mass Gap as the Signature of Non-Abelian Channel Structure

**Builds on:** `Gauge_06` (the F² action from the substrate coherence-deficit), `Gauge_02` (ED as a U(N) lattice gauge theory), Paper_021 (YM-4, the existing ℓ*→Δ mechanism). **Tier:** mechanism / physics — *not* a Clay-rigorous proof. It recasts and extends YM-4 in the coherence-deficit language, supplies candidates for its two open items (O-MG-1 coercivity, O-MG-4 confinement), and locates the gap's origin. Continuum survival remains conditional, exactly as YM-4 flags.

## 1. The question, sharpened by the layers map

The layers map already places **Maxwell** as a layer-1, **massless**, long-range coherent field — the Coulomb shadow ED casts directly (B4, Gauge_06 §2). Yang–Mills differs by one fact: it is **non-abelian**, and non-abelian gauge theory has a **mass gap** — no massless long-range excitation, only massive glueballs. So the gap is not a generic feature of "a gauge field." It is precisely **what changes when the channel structure stops commuting.** The ED question is therefore not "why is there a gap" in the abstract, but: *what, in the substrate, switches the gap on as the gauge group goes from U(1) to U(N≥2)?*

## 2. The origin: the commutator in the coherence-deficit

Gauge_06 derived the action from the plaquette coherence-deficit
$$ S \;=\; \sum_\square \Big(1 - \tfrac{1}{N}\,\mathrm{Re}\,\mathrm{Tr}\,U_\square\Big), \qquad U_\square = \exp\!\big(i a^2 F\big), \quad F = dA + [A,A]. $$

- **Abelian (Maxwell).** $U(1)$ holonomies commute, so $[A,A]=0$ and $F = dA$. The deficit is $1-\cos(a^2 F)\approx \tfrac12 (a^2 F)^2$ — **purely quadratic**, a free field. A free field has **no self-interaction and no gap**: arbitrarily long-wavelength excitations cost arbitrarily little energy. That *is* the massless layer-1 Coulomb field.
- **Non-abelian (Yang–Mills).** $U(N)$ holonomies do **not** commute, so $F$ carries the $[A,A]$ term. The same coherence-deficit, expanded, now contains **cubic and quartic self-interaction** $\sim \mathrm{Tr}[A,A]^2$. The gauge field sources itself. Non-perturbatively, that self-interaction is what gaps the spectrum.

So the ED-native statement is clean:

> **The mass gap is the signature of non-abelian channel structure in the coherence-deficit.** The same deficit that gives $-\tfrac14\mathrm{Tr}F^2$ gives, for a non-commuting channel group, a self-interaction $[A,A]$ with no abelian counterpart — and the gap is that self-interaction's non-perturbative effect. Maxwell (abelian) is massless because its channels commute; Yang–Mills (non-abelian) gaps because they do not.

This places the gap on the layers map exactly: **Maxwell = layer-1 massless; the YM gap = the non-perturbative cost of the non-abelian self-interaction the same substrate carries.**

## 3. A candidate for the coercivity (YM-4's O-MG-1)

YM-4 *postulates* `P-Gap-Coercivity`: $S_{\mathrm{eff}}[A]\ge c_1\|A\|_{H^1}^2 - c_2\|A\|_{L^2}^2$ on the gauge-fixed slice, and lists deriving it (O-MG-1) as the load-bearing open step. The coherence-deficit gives a candidate source. The deficit $1-\tfrac1N\mathrm{Re}\,\mathrm{Tr}\,U_\square$ is a function on the **compact** group manifold with a strict positive minimum-curvature at the identity (it is a Morse function with the identity its unique non-degenerate minimum on the relevant cell). The non-abelian $[A,A]$ term **couples the field modes** so that this positive curvature does not flatten in any direction — the abelian flat direction (the massless photon) is exactly the one the commutator removes. That mode-coupling is the structural content of a coercivity bound. **This does not prove `P-Gap-Coercivity`** — turning "compact-group positive curvature + non-abelian mode coupling" into the explicit $H^1$ bound is real work — but it identifies *where in the substrate the coercivity comes from*: the non-abelian curvature of the coherence-deficit. That is the right target for O-MG-1.

## 4. A candidate for confinement (YM-4's O-MG-4)

The gap's companion is the **Wilson-loop area law**. In the coherence-deficit picture this is the standard strong-coupling argument, and ED sits in the regime where it applies. ED's gauge evolution is **sparse-commitment**: unitary channel transport between *rare* commitments (Gauge_02). Rare commitments = a **stiff / strongly-coupled** gauge field — the regime where a Wilson loop $\langle \mathrm{Tr}\!\prod U\rangle$ is dominated by *tiling* its interior with plaquettes, each suppressed by the coherence-deficit cost, giving
$$ \langle W(C)\rangle \sim \exp(-\sigma\,\mathrm{Area}(C)), \qquad \sigma \sim \text{(coherence-deficit per plaquette)}. $$
Area law ⟹ confinement ⟹ gap. **Honest limit — and it is the crux:** the strong-coupling area law confines **both** abelian *and* non-abelian theories (every lattice gauge theory confines at strong coupling). So §4 explains why ED is in a confining regime *at all*; it does **not** by itself distinguish Maxwell from Yang–Mills. That distinction is a **continuum-limit** fact: $U(1)$ lattice gauge theory has a *deconfinement transition* — it goes to the massless Coulomb (layer-1) phase in the continuum — whereas the non-abelian theory, by asymptotic freedom, **stays confined all the way down**. The thing that keeps the non-abelian theory confined where the abelian one deconfines is exactly the §2 self-interaction $[A,A]$. So §4 (strong-coupling, both) and §2 (the commutator, non-abelian only) are about *different* things: §4 = why ED confines; §2 = why only the non-abelian channel structure *keeps* the gap into the continuum. **The continuum survival is the hard, unsettled half** — the non-perturbative core of the Clay problem, exactly YM-4's conditional `P-Profile-Rescaling`.

## 5. Why the gap survives the arrow-averaging

The gap is defined on the **hermitian, OS-positive** theory — which, by the layers thesis, is the *arrow-averaged shadow* of ED's retarded (non-hermitian) graph, one coarse-graining up. The point worth stating: the gap is a property that **survives that averaging**. The coherence-deficit floor (a minimum non-trivial plaquette cost) is set by the substrate's non-abelian curvature, which is real-valued and orientation-blind in magnitude; averaging the arrow away does not erase it. So the layer-2 OS-positive YM inherits the gap from the layer-1 graph's deficit floor. (The hard part — that the averaging *delivers reflection positivity* — is the OS-positivity audit of Paper_020, inherited and still conditional.)

## 6. What this contributes, honestly

- **New (physics):** the gap's *origin* in ED's own language — the non-abelian commutator in the coherence-deficit, switched on exactly as $U(1)\to U(N)$. This explains, on the layers map, why Maxwell is layer-1 massless and YM is gapped: same substrate, commuting vs non-commuting channels.
- **Connects:** Gauge_06's *derived* action to YM-4's *postulated* coercivity — the non-abelian curvature is the candidate for O-MG-1 — and gives the strong-coupling area-law route for O-MG-4.
- **Does NOT claim:** a constructive proof, the gap's numerical value, asymptotic freedom, or continuum survival. Those remain open / conditional, as YM-4 states. This is the *mechanism* — ED's physical account of why the gap exists — not the Clay proof, which is a different (rigorous) discipline.

## 7. Falsifier

If the abelian theory (Maxwell) showed a substrate-generated gap, or the non-abelian self-interaction in the coherence-deficit could be shown *not* to lift the massless flat direction, the mechanism fails. The mechanism stands or falls on: **gap ⟺ non-commuting channels**, traced to the $[A,A]$ term in the same coherence-deficit that gives $F^2$.
