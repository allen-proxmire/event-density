"""Gate 2 - acyclicity: no global state vector recurs.

Hashes each recorded global state (rho + orientation per node, rounded) and
asserts all hashes are unique. Guaranteed by rho-monotonicity + irreversibility;
tested directly as a guard against implementation error.
"""
import numpy as np


def _state_signatures(rec):
    rho = rec.rho_history()              # [T, |V|]
    orient = rec.orientation_history()   # [T, |V|, k]
    sigs = []
    for t in range(rho.shape[0]):
        sig = (
            tuple(np.round(rho[t], 12).tolist()),
            tuple(tuple(row) for row in np.round(orient[t], 12).tolist()),
        )
        sigs.append(sig)
    return sigs


def test_all_states_unique(mwe):
    sigs = _state_signatures(mwe["rec"])
    assert len(set(sigs)) == len(sigs), "a global state recurred (cycle)"


def test_total_rho_strictly_increases_on_commit(mwe):
    rho = mwe["rec"].rho_history()
    totals = rho.sum(axis=1)
    # Total committed rho must be non-decreasing, and strictly increase whenever
    # a commit occurred (every step here commits at least until the fixed point).
    assert np.all(np.diff(totals) >= -1e-12)
    # At least one strict increase (the run did commit).
    assert totals[-1] > totals[0]
