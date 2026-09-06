# New-Session Onboarding — Event Density (ED)

*Read this first when starting a fresh AI session on the ED program. Goal: get oriented — know the structure and where things live — without ingesting the whole corpus (~120 papers + working notes). Read the small anchor set below, build a map, then stop and ask what we're working on.*

---

## Read these now, and only these

1. **`ED Generative/PAPERS_INDEX.md`** — the canonical index of every paper (arcs, numbers, titles, file locations). Your table of contents for the whole program.
2. **`event-density/docs/ED-Orientation.md`** — the program's orientation/state document in this (working) repo.
3. **`event-density/docs/ED_Research_Targets.md`** — the live open/closed map: what's done, what's open, what's deliberately not being chased, and the highest-leverage next move. (Companion to this file.)
4. **`C:\Users\allen\.claude\projects\C--Users-allen-GitHub-ED-Generative\memory\MEMORY.md`** — the persistent memory index (one line per memory, ~27 entries). Recent research state + where the deeper memory files are. *Treat any specific file/flag/commit it names as possibly stale — verify before relying on it.*
5. **`ED Generative/physics-papers/gravity/Gravity_TieredClaims_Ledger.md`** — a worked example of the program's current frontier (the gravity line) and the house style: claim-forward but honesty-tiered. It is also the arc's staleness detector, so it doubles as the current state of the flagship. *(Path corrected 2026-09-05: this slot used to name `Gravity_Line_Readers_Map.md`, which was moved out of EDG on 2026-07-09 and now lives at `event-density/foundations/relocated_from_EDG_2026-07-09/Gravity_Line_Readers_Map.md`. The pointer had been dead for ~2 months.)*

That's enough to know *where to look*. Do not read further until asked.

---

## Repo geography (three repos)

- **`C:\Users\allen\GitHub\ED Generative`** — "EDG": the **standalone, publication-grade papers repo** (what goes on Zenodo). Self-contained papers. Subfolders: `physics-papers/`, `position-paper/`, `predictions/`, `falsifiers/`, `internal notes/`, `scale correspondence/`, `theorems/`. Index = `PAPERS_INDEX.md`.
- **`C:\Users\allen\GitHub\event-density`** — the **working repo** (this one). Everything-in-progress: `foundations/` (derivation rounds, incl. Phase-3 GR and Khronon–MOND), `evaluation/` (certified-substrate simulations), `papers/` (the numbered corpus, under `papers/Forcing Papers/`), `theory/`, `arcs/`, `theorems/`, `docs/`.
- **`C:\Users\allen\GitHub\Architectual Distillation`** — "AD": a separate repo (note the spelling); some older ED-substrate material originated here. Rarely the right place to work now.

## Where to find things

- **A specific paper** → look it up in `PAPERS_INDEX.md` (it gives the file path).
- **The gravity program (current capstone)** → EDG `physics-papers/gravity/`: GR-I, GR-II, KM-I, KM-II, the One-Field letter, the Reader's Map. Its working rounds are in `event-density/foundations/` (Phase-3 GR rounds R1–R12; `KhrononMOND_Round1..7`).
- **Substrate simulations / empirical tests** → `event-density/evaluation/` (`Bits`, `B4_Arc`, `CoarseGrain_Arc`, `Primes_Arc`, etc.).
- **"How do I say this out loud?" / summaries** → EDG `internal notes/`.
- **The constitution:** the 13 primitives (P01–P13) + 2 kernels (V1 retarded, V5 finite-memory) are **Paper_087**; the methodology is **Paper_095**. Both indexed in `PAPERS_INDEX.md`.

## Vocabulary you'll see everywhere (learn these — they're load-bearing)

- **form-FORCED vs value-INHERITED** — ED claims to force the *structure/form* of a law; numerical constants are usually inherited from observation, not derived. Verdict tiers **M1/M2/M3** encode how much is forced vs inherited.
- **crank-safety** — deliberate discipline against overclaiming: every paper opens with a **"What This Paper Does NOT Claim"** preamble and carries a **load-bearing audit** (each step tagged P / D / I / measured / structural / open).
- **DCGT** — the coarse-graining (discrete → continuum) limit.
- **Wall 1 / Wall 2** — the two kinds of ED limit: Wall 1 = coarse-graining (continuum object; mostly open/attainable-in-principle); Wall 2 = finite-memory/uncomputable (proven, e.g. the prime escape).

## Working conventions (honor these)

- This is real, in-progress research the user cares about. **Be the honest counterweight:** flag overclaims, verify file references before citing them, never inflate a result's verdict tier. The user explicitly values you correcting Copilot-style overstatements.
- **Git:** the user often has their *own* uncommitted work in the working repo. **Never bulk-commit it.** Commit only what *you* changed, via explicit pathspecs. Leave `.claude/settings.local.json` alone. Branch before committing on `main`. End commit messages with the `Co-Authored-By` line.
- **Papers** are written in `.md`; EDG has a `_build_papers.py` that renders `.tex`/`.pdf` beside each source (the user moves `.tex` by hand). Reader's-maps/letters keep their intro content above the first `## ` heading.
- **Memory:** persistent memory lives at the `.claude/.../memory/` path above; update it (and its `MEMORY.md` index) when a research arc closes or a durable fact changes.

## Then

Summarize back, in ~10 lines, your map of the program (the repos, where the gravity line lives, the current frontier and highest-leverage open target, and the methodology vocabulary). **Then stop and ask what we're working on.**
