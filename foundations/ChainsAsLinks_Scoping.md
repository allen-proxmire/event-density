# Scoping Note: Does ED Hold Commitment-Order by Linking, Asked the Right Way

**Foundations — matter-sector / #2b arc. No simulation, no numbers. This note exists to fix what went wrong with the first attempt (`evaluation/Braiding/chains_as_links_probe.py`, retracted 2026-07-01) before trying again: it assumed a continuous 3D space to throw worldlines through, when the whole point of the question is to explain why a continuous 3D space exists. This note looks for a version of the question that doesn't assume its own answer, and finds one — a real, existing piece of mathematics that may be the right tool, not yet applied.**

## 1. The question, restated carefully

MS-II §7's dimensional argument is pure topology: a link is the only structure that can hold an order in one dimension, and a link only forms and holds in exactly three spatial dimensions. That's settled and doesn't depend on anything below.

What's still open is whether **ED itself** reaches for that structure. The retracted probe tried to answer this by building commitment chains as curves in an assumed 3D box and checking whether they wind around each other. That's backwards. ED's substrate is a relational participation graph, not a rigid lattice and not a pre-given continuum, so **any test that starts by dropping chains into a ready-made 3D space has already assumed the thing the argument is supposed to produce**. A test built that way can't fail in the way that matters, and it can't succeed in the way that matters either.

## 2. What's actually available, pre-geometry

Before any spatial embedding, what ED gives you is graph structure: nodes, channels (P07, directional participation pathways), and commitments (P11) that lay down an irreversible order among events. A "commitment chain" at this level is not a curve in space. It's a sequence of graph edges and nodes, an object with connectivity but no metric, no coordinates, and no notion of "winding" in the ordinary sense, because winding is a property of curves in a continuous ambient space, and there isn't one yet.

So the honest question is not "do these curves link in 3D." It's: **does the graph's own connectivity structure, considered purely combinatorially, force linking whenever the graph is embedded in 3-space at all** — a property of the graph itself, not of any one embedding someone chooses to build.

## 3. This is an existing, real piece of mathematics

That reframed question has a name and a body of theory already built around it: **intrinsic linking**. A graph is called *intrinsically linked* if *every* way of drawing it in ordinary 3D space contains two cycles that are topologically linked — you cannot avoid the linking no matter how you embed the graph. This is not a fact about one drawing; it's a fact about the graph's abstract structure, and it can be checked without ever picking coordinates.

The relevant result (Robertson–Seymour–Thomas, building on earlier work by Conway, Gordon, and Sachs): the graphs that are intrinsically linked are exactly those containing one of a specific finite family of forbidden substructures, **the Petersen family** (seven graphs, related by a certain local move, of which the Petersen graph itself is the best known). If ED's participation-graph structure, or the relevant class of sub-graphs its commitment chains actually form, contains a member of the Petersen family as a minor, then **linking is forced, structurally, with no assumption of a pre-given 3D space** — the graph carries the property intrinsically, and 3D is simply the unique dimension in which that intrinsic property can be realized without contradiction (in 2D no embedding exists at all; in 4D and above, the RS Thomas theory's whole point is that linking can always be undone, so an intrinsically-linked graph's forcing is a specifically-3D phenomenon).

This is the right shape of question for ED, because it asks about the **graph itself**, which is primitive, rather than about a curve in space, which is not.

## 4. What this route needs, honestly

This is not a quick check. It requires:

- **Characterizing the actual connectivity structure** that ED's commitment chains form at the graph level — degree, branching, how channels compose (P07 §7.4's channel-topology material is the closest existing thread) — well enough to ask a graph-minor question about it.
- **Checking that structure against the Petersen family** (or showing it provably can't contain one, which would be the honest negative this route can also produce).
- This is graph theory, not simulation. It may be tractable by hand/by known theorems rather than by code, which is a genuine advantage over the retracted approach — no proxy-fidelity problem, because there's no proxy; you'd be working with ED's actual combinatorial primitives directly.

## 5. The fallback, if this route doesn't typecheck

If ED's chains don't naturally form graph structures rich enough to ask an intrinsic-linking question (e.g., if the relevant sub-graphs are too sparse or too simple to ever contain a Petersen-family minor, which is itself possible and would be an honest, informative negative), the question likely has to wait on the curvature-emergence arc (Arc ED-10) to supply a legitimate map from graph to continuum, and only then can chains-as-curves be asked about honestly, downstream of that map rather than in a space assumed for the occasion.

## 6. Recommended next step

Before any further simulation: pull ED's channel-composition rules (P07 §7.4, the existing "channel-topology classes" material already used for the gauge-group and spin-double-cover results) and check, as a graph-theory exercise, whether the resulting connectivity class can contain a Petersen-family minor at all. That answer, on its own, either opens a real, non-circular route to "why 3D" or closes it honestly — without writing a single simulation.

## 7. Status

Scoping only. No claim made about ED in either direction. This supersedes the retracted probe as the live open thread for #2b's fourth item: "does ED hold commitment-order by spatial linking" now reads as "does ED's channel-composition graph contain an intrinsically-linked (Petersen-family) substructure" — a sharper, non-circular, and checkable-by-graph-theory version of the same question.
