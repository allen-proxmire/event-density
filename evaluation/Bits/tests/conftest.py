"""Shared pytest fixtures for the ED substrate simulator test suite.

Tests REGENERATE the MWE deterministically from seeds (run_mwe) rather than
depending on a committed .npz artifact — self-contained and reproducible. The
.npz round-trip is exercised in the integrity test via a tmp_path export.
"""
import os
import sys

import pytest

# Make `simulator`, `examples` (mwe_demo) and `analysis` importable.
_BITS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
for p in (_BITS, os.path.join(_BITS, "examples")):
    if p not in sys.path:
        sys.path.insert(0, p)

from mwe_demo import run_mwe, A_NODES, B_NODES, BRIDGE  # noqa: E402


@pytest.fixture(scope="session")
def mwe():
    """The canonical MWE run (deterministic, recorded)."""
    return run_mwe(record=True)


@pytest.fixture(scope="session")
def a_nodes():
    return list(A_NODES)


@pytest.fixture(scope="session")
def b_nodes():
    return list(B_NODES)


@pytest.fixture(scope="session")
def bridge():
    return tuple(BRIDGE)
