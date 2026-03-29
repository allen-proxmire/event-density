"""Tests for edsim.core.boundary — Ghost-cell boundary conditions."""

import numpy as np
import pytest
from edsim.core.boundary import (
    apply_bc_2d, strip_ghost_2d,
    apply_bc_3d, strip_ghost_3d,
    apply_bc_4d, strip_ghost_4d,
    apply_bc, strip_ghost,
)


class TestNeumann2D:
    def test_pad_shape(self):
        rho = np.ones((8, 10))
        padded = apply_bc_2d(rho)
        assert padded.shape == (10, 12)

    def test_mirror_symmetry(self):
        rho = np.arange(20.0).reshape(4, 5)
        padded = apply_bc_2d(rho)
        # Row 0 of padded mirrors row 2 (= interior row 1)
        np.testing.assert_array_equal(padded[0, 1:-1], rho[1, :])
        # Last row of padded mirrors second-to-last interior row
        np.testing.assert_array_equal(padded[-1, 1:-1], rho[-2, :])

    def test_strip_roundtrip(self):
        rho = np.random.default_rng(0).random((6, 8))
        padded = apply_bc_2d(rho)
        recovered = strip_ghost_2d(padded)
        np.testing.assert_array_equal(recovered, rho)


class TestNeumann3D:
    def test_pad_shape(self):
        rho = np.ones((4, 5, 6))
        padded = apply_bc_3d(rho)
        assert padded.shape == (6, 7, 8)

    def test_strip_roundtrip(self):
        rho = np.random.default_rng(1).random((4, 5, 6))
        recovered = strip_ghost_3d(apply_bc_3d(rho))
        np.testing.assert_array_equal(recovered, rho)


class TestNeumann4D:
    def test_pad_shape(self):
        rho = np.ones((3, 4, 5, 6))
        padded = apply_bc_4d(rho)
        assert padded.shape == (5, 6, 7, 8)

    def test_strip_roundtrip(self):
        rho = np.random.default_rng(2).random((3, 4, 5, 6))
        recovered = strip_ghost_4d(apply_bc_4d(rho))
        np.testing.assert_array_equal(recovered, rho)


class TestGeneric:
    def test_neumann_dispatch(self):
        rho = np.ones((4, 5))
        padded = apply_bc(rho, "neumann", 2)
        assert padded.shape == (6, 7)

    def test_periodic_wraps(self):
        rho = np.arange(4.0).reshape(2, 2)
        padded = apply_bc(rho, "periodic", 2)
        # Periodic wrap: padded[0,:] wraps from last row
        assert padded[0, 1] == rho[-1, 0]

    def test_generic_strip(self):
        rho = np.ones((3, 4, 5))
        padded = apply_bc(rho, "neumann", 3)
        recovered = strip_ghost(padded, 3)
        assert recovered.shape == (3, 4, 5)
