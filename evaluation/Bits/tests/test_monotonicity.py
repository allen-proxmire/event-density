"""Gate 1 - I4 monotonicity: rho never decreases.

Asserts the recorded rho history is elementwise non-decreasing across steps
(no negative deltas anywhere).
"""
import numpy as np


def test_rho_history_non_decreasing(mwe):
    rho = mwe["rec"].rho_history()          # [T, |V|]
    assert rho.shape[0] >= 2
    deltas = np.diff(rho, axis=0)
    assert np.all(deltas >= -1e-12), "rho decreased somewhere (I4 violation)"


def test_no_negative_deltas_per_node(mwe):
    rho = mwe["rec"].rho_history()
    for j in range(rho.shape[1]):
        col = rho[:, j]
        assert np.all(np.diff(col) >= -1e-12), f"node column {j} decreased"


def test_final_rho_at_least_initial(mwe):
    rho = mwe["rec"].rho_history()
    assert np.all(rho[-1] + 1e-12 >= rho[0]), "final rho below initial somewhere"
