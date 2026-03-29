"""Tests for edsim.core.constitutive functions."""

import numpy as np
import pytest
from edsim.core.parameters import EDParameters
from edsim.core.constitutive import (
    mobility, mobility_deriv, penalty, penalty_deriv, enforce_bounds,
)


@pytest.fixture
def params():
    return EDParameters(d=1, N=(16,), L=(1.0,))


class TestMobility:
    def test_at_rho_star(self, params):
        rho = np.array([params.rho_star])
        M = mobility(rho, params)
        expected = params.M0 * (params.rho_max - params.rho_star) ** params.beta
        assert abs(M[0] - expected) < 1e-12

    def test_at_rho_max(self, params):
        rho = np.array([params.rho_max])
        M = mobility(rho, params)
        assert M[0] == 0.0

    def test_at_zero(self, params):
        rho = np.array([0.0])
        expected = params.M0 * params.rho_max ** params.beta
        assert abs(mobility(rho, params)[0] - expected) < 1e-12

    def test_non_negative(self, params):
        rho = np.linspace(0, params.rho_max, 50)
        assert np.all(mobility(rho, params) >= 0)

    def test_finite(self, params):
        rho = np.linspace(0, params.rho_max, 50)
        assert np.all(np.isfinite(mobility(rho, params)))


class TestMobilityDeriv:
    def test_finite(self, params):
        rho = np.linspace(0.01, 0.99, 50)
        Mp = mobility_deriv(rho, params)
        assert np.all(np.isfinite(Mp))

    def test_negative_interior(self, params):
        rho = np.array([0.5])
        Mp = mobility_deriv(rho, params)
        assert Mp[0] < 0  # M'(rho) < 0 for standard params


class TestPenalty:
    def test_at_rho_star(self, params):
        rho = np.array([params.rho_star])
        assert abs(penalty(rho, params)[0]) < 1e-12

    def test_sign_above(self, params):
        rho = np.array([params.rho_star + 0.1])
        assert penalty(rho, params)[0] > 0

    def test_sign_below(self, params):
        rho = np.array([params.rho_star - 0.1])
        assert penalty(rho, params)[0] < 0


class TestEnforceBounds:
    def test_clips_negative(self, params):
        rho = np.array([-0.5, 0.5, 1.5])
        result = enforce_bounds(rho, params)
        assert result[0] == 0.0
        assert result[1] == 0.5
        assert result[2] == params.rho_max
