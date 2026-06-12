"""Update mechanics — Build Step 4: the ED substrate update loop.

Implements the asynchronous, canonical-order Sigma-maximizing update:
  - apply_tiebreak : resolve a Sigma-maximal set to a unique winner (Milestone 1).
  - apply_update   : one chain front — score candidates, tie-break, commit, advance.
  - step           : one global step — process active fronts in (stratum_id, node_id)
                     order, commits immediately visible.
  - hash_state     : deterministic hash of the whole StateVector (acyclicity support).

Determinism within a stratum and factorization across strata are properties of
this loop (see module notes and Phase_SimulatorDesign §4).
"""
from __future__ import annotations

from .graph import ParticipationGraph
from .sigma import SigmaCoeffs, compute_candidates, compute_sigma
from .state import StateVector


def apply_tiebreak(u: int, candidates: list[int],
                   graph: ParticipationGraph) -> int:
    """Among Sigma-tied candidates v, return the unique winner whose key
    kappa(v) = (bw(u, v), v) is lexicographically maximal (descending).

    Bandwidth (B2) is the primary key; node id (B1 distinctness) is the final
    key. Total order over distinct node ids ⇒ exactly one winner. Deterministic;
    called even when |candidates| == 1.
    """
    if not candidates:
        raise ValueError("apply_tiebreak called with empty candidate set")
    return max(candidates, key=lambda v: (graph.bw(u, v), v))


def apply_update(u: int, state: StateVector, graph: ParticipationGraph,
                 coeffs: SigmaCoeffs = SigmaCoeffs()):
    """One chain front at u. Returns the committed target v, or None if the
    front extinguishes.

    Steps: enumerate admissible candidates → score Sigma → take the maximal set
    → deterministic tie-break → commit at the winner (irreversibility chokepoint)
    → advance the front (active u -> v). Orientation transport: longitudinal set
    from the committed direction, transverse carried from the source (Phase E §7).

    Extinction: if there are no admissible candidates, or (when
    coeffs.extinction_threshold is not None) the maximal Sigma <= threshold, the
    front extinguishes — it stops, it never reverses (P11/B7).
    """
    cands = compute_candidates(u, state, graph)
    if not cands:
        state[u].active = False
        return None

    sig = {v: compute_sigma(u, v, state, graph, coeffs) for v in cands}
    smax = max(sig.values())

    if coeffs.extinction_threshold is not None and smax <= coeffs.extinction_threshold:
        state[u].active = False
        return None

    maximal = [v for v, s in sig.items() if s == smax]
    winner = apply_tiebreak(u, maximal, graph)

    # Commit at the winner — the SOLE rho writer (B7 chokepoint).
    transverse = state[u].orientation[1:].copy()
    state[winner].commit(
        coeffs.increment,
        longitudinal=float(winner),   # minimal: encode committed direction by target id
        transverse=transverse,
    )

    # Advance the front: u -> winner.
    state[u].active = False
    state[winner].active = True
    return winner


def step(state: StateVector, graph: ParticipationGraph,
         coeffs: SigmaCoeffs = SigmaCoeffs(),
         strata: dict[int, int] | None = None,
         recorder=None, t: int | None = None) -> int:
    """One global step. Process active fronts in canonical (stratum_id, node_id)
    order; each commit is visible to later fronts in the same step (asynchronous).

    Stratum id source: the optional `strata` mapping if given, else each node's
    NodeState.stratum_id (populated by strata.assign_stratum_ids). Either way the
    order is deterministic and stratum-grouped.

    Optional recording: if `recorder` is given, each commitment is logged via
    recorder.log_commit(t, u, v) and a snapshot is taken after the step via
    recorder.snapshot(t, state). `t` is the step index for the records. Recording
    is read-only on state and does not affect the dynamics.

    Returns the number of commits this step (0 ⇒ fixed point: all fronts
    extinguished). A front that advances into a node this step does NOT take a
    second hop the same step (newly-active fronts wait until the next step).
    """
    def sid(u: int) -> int:
        if strata is not None:
            return strata.get(u, state.stratum_id(u))
        return state.stratum_id(u)

    order = sorted(state.active_nodes(), key=lambda u: (sid(u), u))
    newly_active: set[int] = set()
    commits = 0
    for u in order:
        if u in newly_active:        # advanced into this step ⇒ wait for next step
            continue
        if not state.is_active(u):   # extinguished earlier this step
            continue
        v = apply_update(u, state, graph, coeffs)
        if v is not None:
            commits += 1
            newly_active.add(v)
            if recorder is not None and t is not None:
                recorder.log_commit(t, u, v)
    # Snapshot only when the step changed the state. A zero-commit step is the
    # terminal fixed point already captured at the previous step; recording it
    # again would duplicate the stationary state (not a cycle). Skipping it keeps
    # every recorded global state distinct (acyclicity, Gate 2).
    if recorder is not None and t is not None and commits > 0:
        recorder.snapshot(t, state)
    return commits


def hash_state(state: StateVector) -> int:
    """Deterministic hash of the entire StateVector — used by the acyclicity
    gate. Signature = sorted tuple of (node_id, rho, orientation...), rounded to
    suppress float noise. Two states with identical (rho, orientation) on every
    node hash identically; any difference changes the hash.
    """
    sig = tuple(
        (
            node_id,
            round(st.rho, 12),
            tuple(round(float(o), 12) for o in st.orientation),
        )
        for node_id, st in sorted(state.items())
    )
    return hash(sig)
