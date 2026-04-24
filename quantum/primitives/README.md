# ED Primitives — Reference Index

**Purpose:** One canonical definition per primitive. Every ED-I paper and every quantitative prediction should be able to cite this folder instead of re-introducing the ontology. Consistency enforcement.

**Reading order for someone new:** 01 → 02 → 03 → 05 → 06 → 04 → 07 → 08 → 09 → 10 → 11 → 12 → 13.

(Atomic unit → composite → relational fabric → field measure → spatial structure → quantitative measure → pathway structure → pathway count → phase relation → identity threshold → transition → accumulation → timing.)

---

## The thirteen primitives

| # | Primitive | Role | Status |
|---|---|---|---|
| 01 | Micro-event | Atomic unit of becoming | **Drafted** |
| 02 | Chain | Sequence of micro-events with consistent update rule | **Drafted** |
| 03 | Participation | Relational substrate | **Drafted** |
| 04 | Participation bandwidth | Graded measure of relational richness | Pending |
| 05 | Event density (ED) | Scalar field measuring accumulated becoming | Pending |
| 06 | ED gradient | Variation of ED across regions | Pending |
| 07 | Channel | Stable participation pathway | Pending |
| 08 | Multiplicity | Count/measure of viable channels | Pending |
| 09 | Tension polarity | Phase relation of update rule to relaxation direction | Pending |
| 10 | Individuation | Threshold for distinct identity | Pending |
| 11 | Commitment | Irreversible channel selection event | Pending |
| 12 | Thickening | Accumulation of committed structure | Pending |
| 13 | Relational timing | Phase coupling between channels | Pending |

---

## Document template (applied in each file)

Each primitive document has the following sections:

1. **Definition** — what it is, distinct from what it's not
2. **Mathematical object** — scalar / vector / tensor / graph / relation / threshold / etc.
3. **Relations to other primitives** — what composes from it, what it composes
4. **Measurable signature** — what experimentally observable quantity it corresponds to
5. **Example applications** — one or two phenomena where it's the load-bearing concept
6. **Simulator / PDE instantiation** — where it exists operationally in existing code/math
7. **Open questions** — unsettled aspects

---

## Citation convention

When citing the primitives from other ED work, use the form:

> *"Per `quantum/primitives/01_micro_event.md` §1–2"*

That keeps everything traceable and lets any reader verify the definition being used.

---

## Change log

- **2026-04-24** — Folder created. Primitive #01 (Micro-event) drafted as the starting anchor.
- **2026-04-24** — Primitive #02 (Chain) drafted. First composite structure. Load-bearing for particle identity, photon propagation, superconducting phase, neutrino oscillations, Josephson supercurrent. Four circular-definition flags surfaced in §3 pointing at later primitives (07, 09, 10, 11, 12). η derivation thread tagged explicitly in §7 (5) as Phase 4 target.
- **2026-04-24** — Primitive #03 (Participation) drafted. Relational substrate. Completes the core triad (01 + 02 + 03). Key clarifications: participation is the *relation* itself, distinct from its measure (04 bandwidth) and from stable patterns in it (07 channels). Load-bearing for entanglement, distance/locality emergence, measurement as forced participation, light cones as participation limits, topological phases as participation geometry, superposition persistence. Two circular-definition flags surfaced in §3. η derivation thread re-tagged in §7 (4) with more specific framing: η comes from a *participation selection rule* that saturated early-universe ED-flow imposed on chain update rules — this is where the Phase 4 derivation has to bottom out formally. Also flagged: formal gauge theory from participation topology as a major Phase 2/3 target (§7.2).
