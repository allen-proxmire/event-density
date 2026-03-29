"""Tests for edsim.core.parameters.EDParameters."""

import math
import pytest
import numpy as np
from edsim.core.parameters import EDParameters


class TestConstruction:
    def test_default_creates_valid_1d(self):
        p = EDParameters()
        assert p.d == 1
        assert p.D == 0.3
        assert p.rho_star == 0.5

    def test_2d_construction(self):
        p = EDParameters(d=2, N=(32, 32), L=(1.0, 1.0))
        assert p.d == 2
        assert len(p.N) == 2

    def test_invalid_dimension_raises(self):
        with pytest.raises(ValueError):
            EDParameters(d=5, N=(4,) * 5, L=(1.0,) * 5)

    def test_mismatched_lengths_raises(self):
        with pytest.raises(ValueError):
            EDParameters(d=2, N=(32,), L=(1.0, 1.0))

    def test_invalid_rho_star_raises(self):
        with pytest.raises(ValueError):
            EDParameters(d=1, N=(16,), L=(1.0,), rho_star=1.5, rho_max=1.0)


class TestDerivedQuantities:
    def test_M_star_canonical(self):
        p = EDParameters()
        expected = 1.0 * (1.0 - 0.5) ** 2.0
        assert abs(p.M_star - expected) < 1e-12

    def test_R_grad_increases_with_d(self):
        r = []
        for d in [1, 2, 3, 4]:
            p = EDParameters(d=d, N=(8,) * d, L=(1.0,) * d)
            r.append(p.R_grad_predicted)
        assert all(r[i] < r[i + 1] for i in range(3))

    def test_total_grid_points(self):
        p = EDParameters(d=3, N=(4, 5, 6), L=(1.0, 1.0, 1.0))
        assert p.total_grid_points == 120

    def test_n_steps(self):
        p = EDParameters(d=1, N=(16,), L=(1.0,), dt=0.01, T=1.0)
        assert p.n_steps == 100

    def test_dx_neumann(self):
        p = EDParameters(d=2, N=(11, 21), L=(1.0, 2.0), bc="neumann")
        assert abs(p.dx[0] - 0.1) < 1e-12
        assert abs(p.dx[1] - 0.1) < 1e-12

    def test_make_grid_shapes(self, params_2d):
        grid = params_2d.make_grid()
        assert len(grid) == 2
        assert grid[0].shape == (params_2d.N[0],)
        assert grid[1].shape == (params_2d.N[1],)


class TestSerialization:
    def test_roundtrip(self):
        p = EDParameters(d=2, N=(16, 16), L=(1.0, 1.0), D=0.4, seed=99)
        d = p.to_dict()
        p2 = EDParameters.from_dict(d)
        assert p2.d == p.d
        assert p2.N == p.N
        assert p2.D == p.D
        assert p2.seed == p.seed

    def test_roundtrip_preserves_all_fields(self):
        p = EDParameters(d=3, N=(8, 8, 8), L=(2.0, 2.0, 2.0),
                         D=0.5, H=0.2, beta=3.0, P0=0.5, dt=1e-3, T=2.0)
        d = p.to_dict()
        p2 = EDParameters.from_dict(d)
        for key in d:
            assert getattr(p2, key) == getattr(p, key), f"Mismatch on {key}"
