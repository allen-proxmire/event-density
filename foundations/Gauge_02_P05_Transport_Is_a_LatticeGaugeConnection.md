# Gauge Program · Step 2 — P05-Transport of N Channels Is a U(N) Lattice Gauge Connection

**Foundations — step 2 (continues `Gauge_01`). Question: is the U(N) channel-multiplicity symmetry (step 1) actually *gauged* — realized by transport — or merely a global symmetry? Result: yes, gauged. **P05-transport of N indistinguishable channels, with bandwidth conservation (P04), is a position-dependent unitary map on ℂ^N — i.e. a U(N) link variable.** That is, by definition, a lattice gauge connection: the gauge field is the per-edge U(N) rotation, and the field strength is the plaquette holonomy (non-commutativity of transport around a loop). So **ED's channel substrate is intrinsically a lattice gauge theory** — on the *relational* graph (irregular, no Brillouin torus) with the *retarded* arrow, which is exactly why it escapes Nielsen–Ninomiya (SQ1). This grounds T17's *postulated* "P05 = connection" as a derivation, and the continuum Yang–Mills emerges via DCGT. Unitary U(N) transport holds *between* commitments; commitments are the non-unitary projections (measurement) — the sparse-commitment structure. Honest: "P05 re-routes channels unitarily" is a structural reading of P05 + P07 composition + P04; the Yang–Mills *action* (why F²) is not derived here.**

---

## 1. The question

Step 1 showed the fiber of N indistinguishable channels carries a **U(N)** symmetry (bandwidth conservation on `ψ ∈ ℂ^N`). A *global* symmetry is not a force. For SU(N) to be a **gauge** symmetry — a force with a connection, parallel transport, and field strength — transport must (i) be able to rotate among the N channels, and (ii) do so *position-dependently*, so that transport around a closed loop need not return to the identity (non-trivial holonomy = curvature = field strength).

## 2. P05-transport is a U(N) link variable

Transport one locus to the next. The chain's amplitude `ψ(u) ∈ ℂ^N` over the N channels maps to `ψ(u') ∈ ℂ^N`. Three substrate facts fix the form of that map:

- **Channels re-route through the graph** (P07 §2 composition: channels branch and merge; the N channels at `u` connect to a *different* arrangement at `u'`). So the map mixes components — it is not forced diagonal.
- **Bandwidth is conserved** (P04): `Σ|ψ_i|²` is preserved along the transport ⇒ the map is an **isometry** of ℂ^N.
- **Between commitments, transport is invertible** (commitment/irreversibility P11 is the *only* non-invertible event; between commitments the evolution is reversible — the sparse-commitment structure).

An invertible isometry of ℂ^N is a **unitary** matrix. So:
$$U_{u u'} \in U(N), \qquad \psi(u') = U_{u u'}\,\psi(u).$$
**A U(N) matrix on each edge is precisely a lattice gauge link variable.** P05-transport of multiplicity-N channels *is* a U(N) lattice connection — not by analogy (T17 §6.1), but because bandwidth-conserving invertible re-routing of N indistinguishable channels is exactly a unitary link map.

## 3. The gauge field and the field strength

The lattice-gauge structure follows immediately:

- **Gauge field** `A`: the infinitesimal generator of `U_{uu'}` per edge (`U_{uu'} = exp(i A_{uu'})`, `A ∈ 𝔲(N)`). The SU(N) part is the non-abelian gauge field; the U(1) part is the common P09 phase.
- **Field strength** `F`: the **plaquette holonomy** — the product of link variables around a smallest loop, `U_□ = U_{u u'}U_{u' u''}U_{u'' u'''}U_{u''' u}`. If `U_□ ≠ 𝟙`, transport around the loop rotates the channel amplitude ⇒ non-zero curvature ⇒ a genuine gauge *field*, not pure gauge. The non-commutativity of SU(N) link variables makes `F` non-abelian (`F = dA + A∧A`).
- **Holonomy:** the loop product `U_C = ∏_C U_{uu'}` is the substrate realization of the holonomy that Aharonov–Bohm (Paper_010) and Berry-phase (Paper_009) already use as *inherited* standard math — step 2 grounds it: the connection whose holonomy those papers invoke **is** the P05 re-routing of channels.

So the U(N) symmetry of step 1 is genuinely **gauged**: it is local (per-edge link variables) and curved (non-trivial plaquette holonomy).

## 4. ED's channel substrate is a lattice gauge theory — on the right kind of lattice

Steps 1+2 say: **the channel sector of the ED substrate is a U(N) lattice gauge theory.** Two features make it the *right* kind, and tie back to #2b:

- **It lives on the relational participation graph**, not a regular periodic lattice — so there is **no Brillouin torus**. This is exactly the feature SQ1 identified as why ED escapes Nielsen–Ninomiya: the doubling no-go needs the compact torus topology, which the relational graph does not have.
- **Transport carries the retarded arrow** (P05 → V1 retardation, T18): the link variables are *forward-directed*, the non-hermitian structure of #2b. So this is a *non-hermitian, irregular-graph* lattice gauge theory — precisely the regime where chiral fermions are not forbidden (the #2b thread).

The two threads now sit in one structure: **the gauge sector (U(N) channel-lattice connection) and the fermion sector (spinor = channel-topology, T4 step 2) are the same lattice gauge theory** — internal U(N) from channel multiplicity, spinors from channel topology, both transported by P05/V1/V5, all on the relational graph with the arrow.

## 5. Unitary between commitments; commitments are the projections

The U(N) link variables are unitary *between* commitments. At a **commitment** (P11), the chain's distribution over the N channels collapses to one — a **non-unitary projection**. So the picture is the standard one in gauge-theoretic language: **unitary U(N) gauge evolution between rare commitments, punctuated by projective measurements (commitments).** This is the sparse-commitment structure (the same one behind α₁-safety and the #2b topological robustness): the gauge field lives in the unitary between-commitment transport; commitments are where the gauge-covariant amplitude is read out.

## 6. What step 2 does and doesn't give

**Gives:** the U(N) channel symmetry is *gauged* — P05-transport of N indistinguishable channels with bandwidth conservation is a U(N) lattice connection, with gauge field (per-edge generator) and field strength (plaquette holonomy). This **derives** T17's postulated "P05 = connection" and "channels = fiber" from P04 + P07 + the invertibility-between-commitments structure, and identifies the substrate as a non-hermitian lattice gauge theory on the relational graph — consistent with the #2b N–N escape.

**Doesn't give (the remaining program):**
1. **The Yang–Mills *action*** — why the gauge-field dynamics are `∝ F²` (the YM Lagrangian). Step 2 builds the *connection and curvature*; the action/dynamics (from the substrate, via DCGT coarse-graining of the plaquette structure — the lattice → continuum YM step) is the next derivation.
2. **Uniqueness {1,2,3}** — still the deep open question (Gauge_01 §5.1).
3. **The single hypercharge U(1)** and electroweak mixing (Gauge_01 §5.2).
4. **Spin-SU(2) frame bundle** — separate (deferred).

## 7. Status

**Gauge step 2: P05-transport of N indistinguishable channels (bandwidth-conserving, invertible between commitments) is a U(N) lattice gauge link variable — so the U(N) channel-multiplicity symmetry of step 1 is genuinely gauged, with gauge field = per-edge generator and field strength = plaquette holonomy.** ED's channel substrate is a non-hermitian lattice gauge theory on the relational graph — which is *why* it escapes Nielsen–Ninomiya (no Brillouin torus, retarded arrow) and where the gauge and fermion sectors unify. This grounds T17's postulated connection as derived. Next: the Yang–Mills action via DCGT (lattice → continuum), then the uniqueness {1,2,3} and the hypercharge/electroweak structure. Honest flag: "P05 re-routes channels unitarily" is a structural reading of P05 + P07 composition + P04 invertibility — defensible, not a closed substrate proof; the action is not yet derived.

---

*Gauge program step 2. Is the U(N) channel symmetry (step 1) gauged? Yes. P05-transport of N indistinguishable channels: amplitude ψ∈ℂ^N maps u→u' by re-routing (P07 branch/merge composition), bandwidth-conserving (P04 isometry), invertible between commitments (P11 the only non-invertible event) ⇒ the map is UNITARY ⇒ U_{uu'} ∈ U(N) = a lattice gauge link variable. Gauge field = per-edge generator (U=exp(iA), A∈𝔲(N)); field strength = plaquette holonomy U_□ (≠𝟙 ⇒ curvature; SU(N) non-commutativity ⇒ non-abelian F=dA+A∧A); loop holonomy = the connection AB (Paper_010) + Berry (Paper_009) already use as inherited math — now grounded. So ED's channel substrate = a U(N) lattice gauge theory on the RELATIONAL graph (no Brillouin torus) with the RETARDED arrow (non-hermitian) — exactly the #2b N–N escape; gauge sector (U(N) from multiplicity) + fermion sector (spinor = channel topology, T4_02) = one lattice gauge theory. Unitary between commitments; commitments = non-unitary projections (sparse-commitment, measurement). Grounds T17's postulated "P05=connection"/"channels=fiber" as derived (from P04+P07+invertibility). Doesn't give: YM action (why F² — next, via DCGT lattice→continuum); uniqueness {1,2,3}; single hypercharge U(1)/electroweak mixing; spin-SU(2) frame bundle (deferred). Flag: "P05 re-routes channels unitarily" is a structural reading, defensible not closed; action not derived.*
