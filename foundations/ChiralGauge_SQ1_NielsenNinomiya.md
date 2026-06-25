# #2b · SQ1 — Does Nielsen–Ninomiya Bind ED? The Binding Analysis

**Foundations analysis — executes SQ1 of the chiral-gauge scoping (`ChiralGauge_Parity_Gap_Scoping.md`): does the Nielsen–Ninomiya fermion-doubling theorem (or any generalization) forbid ED a chiral fermion sector? Not a corpus edit, not a new primitive, no chiral coupling constructed. The honest result: the *literal* theorem does not bind ED, and it fails on two independent premises that are ED's defining features (no Brillouin torus; non-hermitian/retarded dynamics) — but escaping the theorem's premises is necessary, not sufficient. The doubling question does not vanish; it *migrates* to a now-sharp open computation (the net chirality of ED's continuum-limit Dirac sector), and the harder target — a chiral *gauge* theory with anomaly cancellation — is unsolved even where the free-fermion no-go is beaten. Verdict: NOT Wall 2; the front is open, with two concrete next computations named.**

**Crank rail — maximal.** This is a favorable-leaning result on the program's sharpest external objection (the Tong / "the universe can't be discrete" argument). The discipline here: state the theorem's premises exactly, check ED against each without flattering, distinguish "the premise fails" from "the physics is solved," and identify precisely where the difficulty re-concentrates. No claim that ED *produces* chiral fermions is made or implied.

---

## 1. The theorem, stated exactly, and its real engine

**Nielsen–Ninomiya (1981).** A lattice fermion theory whose single-particle Hamiltonian $H(\mathbf{p})$ satisfies:

1. **Locality** — couplings decay fast enough that $H(\mathbf{p})$ is a *smooth, periodic* function over the Brillouin zone;
2. **Translation invariance** — the lattice is periodic, so $\mathbf{p}$ is a good quantum number and $H(\mathbf{p})$ lives on the Brillouin **torus** $T^d$;
3. **Hermiticity** — $H(\mathbf{p}) = H(\mathbf{p})^\dagger$ (real energy bands, unitary evolution);
4. **A conserved (exact) chiral charge** — a local bilinear $U(1)$ chiral symmetry;

has **net chirality zero**: the left- and right-handed Weyl modes are equal in number. Unpaired Weyl fermions are impossible; chiral fermions come in opposite-chirality "doubler" pairs, so the theory is effectively *vector-like* (parity-conserving).

**The engine is topological, and that is the load-bearing point.** The Weyl points are zeros of the dispersion on the Brillouin torus, each carrying a chirality = the sign of a winding number (a local index). On a **compact manifold without boundary** the sum of those indices is fixed by the topology (Poincaré–Hopf: it is the Euler characteristic, and for the torus $\chi(T^d)=0$). So the chiralities must cancel. Premises 1–3 are exactly what build that argument: locality makes $H(\mathbf p)$ continuous, translation-invariance supplies the *compact torus*, hermiticity makes the bands real so the zeros and their winding are well-defined. **N–N is, at bottom, a statement about the topology of the Brillouin torus.** Remove the torus, or remove the hermiticity that makes the index real, and the argument has nothing to stand on.

## 2. ED's discrete fermion structure (grounded)

From RQM-T4 + the V1 kernel (Paper_089), ED's fermion sector is: a four-component Cl(3,1) spinor amplitude $\Psi$ carried on the participation graph (T2/T4); inter-component coupling supplied by the gamma-matrices; and propagation by the **finite-width retarded** V1 kernel — *advanced V1 is refuted by P11* (T18). The continuum Dirac equation is asserted as the DCGT coarse-grained limit of this transport, with the explicit substrate-V1 → Dirac chain **flagged OPEN** (T4 §3.7, audit row 15).

Two structural facts about this operator decide SQ1:

- **It does not live on a Brillouin torus.** ED is a *relational participation graph*, not a periodic lattice. P03 is homogeneity of the substrate *operations*, not a fixed translation-invariant grid; there is no global momentum space, no Brillouin zone, no torus. (This is the same fact that lets ED's gravity be background-free.)
- **It is not hermitian.** The retarded-only V1 (T18) is a one-way, causal propagator — the arrow of time written into the dynamics. A retarded kernel is *not* a hermitian Hamiltonian; the evolution is not time-reversal symmetric.
- **It is local.** The V1 kernel has finite width (a bounded substrate reach, $\sim\ell_{\rm ED}$). This matters: ED is *not* evading any no-go by smuggling in non-locality (the disreputable escape). Its escape is by the two structural features above, with locality intact.

## 3. Premise-by-premise

| N–N premise | ED | Verdict |
|---|---|---|
| **Translation-invariant lattice (→ Brillouin torus)** | Relational graph; no periodic grid, no global momentum space, no torus | **FAILS** — the topological engine has no compact manifold to run on |
| **Hermiticity** | Strictly retarded V1 (T18); the arrow makes the dynamics non-hermitian / non-time-reversal-symmetric | **FAILS** — the real-band index that pairs the doublers is not defined |
| **Locality** | Finite-width V1 ($\sim\ell_{\rm ED}$) | **HOLDS** — ED is *not* cheating via non-locality |
| **Exact conserved chiral charge** | No chiral coupling defined yet (the gap itself) | N/A — premature; this is what #2b is trying to build |

The literal theorem requires all of 1–4. ED fails 1 and 2 — and fails them on its *defining* features (relational background-freedom and the arrow), not by an engineered loophole, while keeping locality (3̄). **So the literal Nielsen–Ninomiya theorem does not bind ED.** That is a real conclusion, and it is the principled basis for the "ED is discrete but not a lattice" reply to the Tong objection.

## 4. Necessary, not sufficient — where the difficulty actually goes

Escaping the premises is not solving the physics. Two honest caveats, and they are the substance of SQ1:

**(a) The doubling question migrates to the continuum limit — and becomes a sharp open computation.** N–N at the graph level is dissolved, but the physical question it encodes does not disappear: *is ED's DCGT continuum-limit Dirac sector chiral, or doubled (vector-like)?* That is decided by the substrate-V1 → Dirac coarse-graining — which T4 explicitly leaves **OPEN**. So "no torus, no theorem" buys the *possibility* of net chirality; it does not deliver it. The new, sharp target this analysis hands the open T4 derivation: **compute the net chirality of the coarse-grained Dirac operator.** If it comes out zero (doublers re-pair in the continuum), ED is effectively vector-like after all and the gap is real; if nonzero, ED carries chiral fermions and the front opens. Until that is computed, the honest status is *possible, not shown*.

**(b) Chiral *gauge* theory is hard even where the free-fermion no-go is beaten.** Lattice field theory *did* find ways past N–N for *free / vector-like* fermions — Ginsparg–Wilson, overlap, and domain-wall fermions, which satisfy a *lattice-modified* chiral symmetry (relaxing premise 4) and reproduce the right anomaly. But constructing a genuinely **chiral gauge theory** (the electroweak sector — gauge fields coupling differently to the two chiralities) non-perturbatively on a lattice **remains an open problem in lattice field theory.** So even the community that beat N–N has not solved ED's actual target. The lesson for #2b: the real difficulty is not the free-fermion doubling theorem (which ED sidesteps) but the chiral *gauge* coupling and its **anomaly cancellation** — exactly SQ3, which this scoping already flagged as the hardest piece and the most plausible home of a genuine obstruction.

## 5. The positive thread (hypothesis, flagged)

There is a reason to think ED's non-hermiticity is not merely an *escape* from N–N but a candidate *mechanism* for net chirality. In a hermitian lattice the doublers pair because the real band structure crosses zero an even number of times with cancelling windings — a consequence of the hermitian/time-reversal structure on the torus. **Non-hermitian systems are known to host *unpaired* chiral modes** (point-gap topology, the non-hermitian skin effect): relaxing hermiticity is precisely how one unpairs what the hermitian no-go pairs. ED's non-hermiticity is the *arrow* (retarded V1, P11). So the hypothesis — to be tested in the SQ2/continuum-limit work, not asserted here — is that **the arrow is what unpairs the doublers**, i.e. the same irreversibility that gives ED the khronon, α₁-safety, and the position-dependent clock could be what lets it carry a chiral fermion sector. That would make chirality the arrow's *fourth* job. It is a genuine, motivated hypothesis with real non-hermitian-topology precedent — and it is *not* proven; the continuum-limit net-chirality computation (4a) is its test.

## 6. Verdict

**SQ1: the literal Nielsen–Ninomiya theorem does NOT bind ED — confirming the scoping's provisional verdict, "not Wall 2."** The theorem's topological engine is the compact Brillouin torus of a translation-invariant lattice, and its proof requires hermiticity; ED has neither (relational graph; retarded, non-hermitian arrow), while keeping locality intact — so the escape is principled, not a loophole, and it is the rigorous basis for the discreteness reply to the Tong objection. **But this is necessary, not sufficient:** the doubling question migrates to the continuum limit as a now-sharp open computation (the net chirality of ED's DCGT Dirac sector — the derivation T4 left open), and the harder target — a chiral *gauge* theory with anomaly cancellation (SQ3) — is unsolved even where the free-fermion no-go is beaten. **The front is OPEN, not walled.** The non-hermitian arrow is a motivated candidate *mechanism* for producing the net chirality (point-gap/skin-effect precedent), turning the escape into a possible engine — to be tested, not claimed.

**Next computations, in order:** (i) **the continuum-limit net-chirality** — push the open substrate-V1 → Dirac coarse-graining (T4 §3.7) with net chirality as the explicit target; decide chiral vs doubled. (ii) **SQ3 — the chiral gauge coupling + anomaly structure**, the hardest piece and the most plausible site of a real obstruction. (iii) cross-check against the non-hermitian-topology literature for whether a *non-hermitian* doubling no-go exists that would re-bind ED (the residual Wall-2 risk).

---

*SQ1 of #2b. Nielsen–Ninomiya's engine is the Brillouin-torus topology + hermiticity; ED has no Brillouin torus (relational graph, not a periodic lattice) and is non-hermitian (retarded V1, the arrow, T18), while keeping locality (finite V1 width) — so the literal theorem does NOT bind ED, on its defining features, not a loophole. This is the principled basis for the "discrete but not a lattice" reply to the chiral-fermion objection. NECESSARY NOT SUFFICIENT: the doubling question migrates to the continuum limit as a sharp open computation (net chirality of the DCGT Dirac sector — the substrate-V1→Dirac derivation T4 leaves open); and chiral GAUGE theory + anomaly cancellation (SQ3) is unsolved even with the lattice escapes (Ginsparg-Wilson/overlap solve free/vector-like, not chiral gauge; electroweak-on-lattice open). Positive thread (hypothesis, not proven): non-hermiticity is a known route to UNPAIRED chiral modes (point-gap topology, skin effect), so the arrow may be the mechanism that produces net chirality — chirality as the arrow's fourth job. Verdict: NOT Wall 2; front OPEN. Next: (i) compute continuum-limit net chirality; (ii) SQ3 anomalies; (iii) check for a non-hermitian doubling no-go. No primitive added, no chiral coupling constructed, no number faked.*
