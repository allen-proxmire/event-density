"""Tests for edsim.core.operators — Laplacian, gradient, and F[rho]."""

import numpy as np
import pytest
from edsim.core.parameters import EDParameters
from edsim.core.operators import (
    laplacian_fd_2d, laplacian_fd_3d,
    grad_squared_fd_2d, grad_squared_fd_3d,
    operator_F_local_fd,
)


class TestLaplacian2D:
    def test_constant_field_is_zero(self, params_2d):
        rho = np.full(params_2d.N, 0.5)
        lap = laplacian_fd_2d(rho, params_2d.dx)
        assert np.allclose(lap, 0, atol=1e-12)

    def test_cosine_approximation(self):
        N = 64
        p = EDParameters(d=2, N=(N, N), L=(1.0, 1.0))
        grid = p.make_grid()
        X, Y = np.meshgrid(grid[0], grid[1], indexing="ij")
        rho = np.cos(np.pi * X) * np.cos(np.pi * Y)
        expected = -2.0 * np.pi ** 2 * rho
        lap = laplacian_fd_2d(rho, p.dx)
        # Interior points (avoid boundaries where FD has larger error)
        interior = lap[3:-3, 3:-3]
        exact = expected[3:-3, 3:-3]
        rel_err = np.max(np.abs(interior - exact)) / np.max(np.abs(exact))
        assert rel_err < 0.02  # 2% relative error

    def test_correct_shape(self, params_2d, cosine_ic_2d):
        lap = laplacian_fd_2d(cosine_ic_2d, params_2d.dx)
        assert lap.shape == cosine_ic_2d.shape


class TestLaplacian3D:
    def test_constant_field_is_zero(self, params_3d):
        rho = np.full(params_3d.N, 0.5)
        lap = laplacian_fd_3d(rho, params_3d.dx)
        assert np.allclose(lap, 0, atol=1e-12)


class TestGradSquared:
    def test_constant_is_zero_2d(self, params_2d):
        rho = np.full(params_2d.N, 0.5)
        gs = grad_squared_fd_2d(rho, params_2d.dx)
        assert np.allclose(gs, 0, atol=1e-12)

    def test_positive_for_nontrivial_2d(self, params_2d, cosine_ic_2d):
        gs = grad_squared_fd_2d(cosine_ic_2d, params_2d.dx)
        assert np.all(gs >= -1e-15)
        assert np.max(gs) > 0

    def test_constant_is_zero_3d(self, params_3d):
        rho = np.full(params_3d.N, 0.5)
        gs = grad_squared_fd_3d(rho, params_3d.dx)
        assert np.allclose(gs, 0, atol=1e-12)


class TestOperatorF:
    def test_at_equilibrium_is_zero(self, params_2d):
        rho = np.full(params_2d.N, params_2d.rho_star)
        F = operator_F_local_fd(rho, params_2d)
        assert np.allclose(F, 0, atol=1e-10)

    def test_finite_values(self, params_2d, cosine_ic_2d):
        F = operator_F_local_fd(cosine_ic_2d, params_2d)
        assert np.all(np.isfinite(F))
        assert F.shape == cosine_ic_2d.shape

    def test_3d_finite(self, params_3d, cosine_ic_3d):
        F = operator_F_local_fd(cosine_ic_3d, params_3d)
        assert np.all(np.isfinite(F))
        assert F.shape == cosine_ic_3d.shape
