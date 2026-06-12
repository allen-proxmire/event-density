"""MWE integrity - the run is well-formed and exports/reloads faithfully.

Asserts: two strata, the decoupled bridge present, boundary_map correct, natural
termination (not by max_steps), and .npz round-trip fidelity.
"""
import numpy as np

from simulator import (
    boundary_map, detect_decoupled_edges, detect_boundary_nodes,
)
from mwe_demo import A_NODES, B_NODES, BRIDGE, MAX_STEPS


def test_two_strata(mwe):
    assert set(mwe["strata"].values()) == {0, 1}
    sizes = {0: 0, 1: 0}
    for sid in mwe["strata"].values():
        sizes[sid] += 1
    assert sizes == {0: len(A_NODES), 1: len(B_NODES)}


def test_decoupled_bridge_present(mwe):
    g = mwe["g"]
    assert detect_decoupled_edges(g) == [tuple(sorted(BRIDGE))]
    assert detect_boundary_nodes(g) == set(BRIDGE)


def test_boundary_map_correct(mwe):
    g = mwe["g"]
    u, v = sorted(BRIDGE)
    assert boundary_map(g) == {u: [v], v: [u]}


def test_terminates_naturally(mwe):
    # Reached a fixed point (no commits) strictly before the cap.
    assert mwe["steps_run"] < MAX_STEPS
    assert mwe["total_commits"] > 0


def test_npz_round_trip(mwe, tmp_path):
    rec = mwe["rec"]
    prefix = str(tmp_path / "rt")
    npz_path, json_path = rec.export(prefix)
    loaded = np.load(npz_path)
    assert np.allclose(loaded["rho_history"], rec.rho_history())
    assert np.allclose(loaded["orientation_history"], rec.orientation_history())
    assert loaded["rho_history"].shape == rec.rho_history().shape
    assert loaded["committed_edges"].shape == rec.committed_edges().shape
