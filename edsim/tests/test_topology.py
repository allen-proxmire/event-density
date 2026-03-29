"""Tests for edsim.invariants.topology — Euler characteristic and Betti numbers."""

import numpy as np
import pytest
from edsim.core.parameters import EDParameters
from edsim.invariants.topology import (
    euler_characteristic, betti_numbers, connected_components,
)
from edsim.experiments.runner import RunConfig, run_simulation


class TestEulerCharacteristic2D:
    def test_full_domain(self, params_2d):
        """All-True mask: chi = 1 (single connected component, no holes)."""
        rho = np.full(params_2d.N, params_2d.rho_star + 0.1)
        chi = euler_characteristic(rho, params_2d, threshold=params_2d.rho_star)
        assert chi == 1

    def test_empty_set(self, params_2d):
        """All-False mask: chi = 0."""
        rho = np.full(params_2d.N, params_2d.rho_star - 0.1)
        chi = euler_characteristic(rho, params_2d, threshold=params_2d.rho_star)
        assert chi == 0

    def test_cosine_ic_peaks(self, params_2d, cosine_ic_2d):
        """Cosine IC at rho_star threshold should have positive chi (peaks above threshold)."""
        chi = euler_characteristic(cosine_ic_2d, params_2d, threshold=params_2d.rho_star)
        assert chi > 0

    def test_constant_at_low_threshold(self, params_2d):
        """Short run: chi constant at a low threshold where whole domain is above."""
        p = EDParameters(d=2, N=(16, 16), L=(1.0, 1.0), dt=5e-4, T=0.02, k_out=10,
                         method="implicit_euler", bc="neumann")
        config = RunConfig(params=p, ic_type="cosine", ic_kwargs={"A": 0.03, "Nm": 2})
        ts = run_simulation(config)
        low_thresh = p.rho_star - 0.2
        chis = [euler_characteristic(f, p, threshold=low_thresh) for f in ts.fields]
        assert len(set(chis)) == 1, f"chi changed: {set(chis)}"


class TestEulerCharacteristic3D:
    def test_full_domain(self, params_3d):
        rho = np.full(params_3d.N, params_3d.rho_star + 0.1)
        chi = euler_characteristic(rho, params_3d, threshold=params_3d.rho_star)
        assert chi == 1

    def test_empty_set(self, params_3d):
        rho = np.full(params_3d.N, params_3d.rho_star - 0.1)
        chi = euler_characteristic(rho, params_3d, threshold=params_3d.rho_star)
        assert chi == 0


class TestConnectedComponents:
    def test_single_blob(self):
        mask = np.zeros((10, 10), dtype=bool)
        mask[3:7, 3:7] = True
        n, labels = connected_components(mask)
        assert n == 1

    def test_two_blobs(self):
        mask = np.zeros((10, 10), dtype=bool)
        mask[1:3, 1:3] = True
        mask[7:9, 7:9] = True
        n, labels = connected_components(mask)
        assert n == 2


class TestBettiNumbers:
    def test_full_domain_2d(self, params_2d):
        rho = np.full(params_2d.N, params_2d.rho_star + 0.1)
        betti = betti_numbers(rho, params_2d, threshold=params_2d.rho_star)
        assert betti[0] == 1  # one component
        assert betti[1] == 0  # no holes

    def test_returns_correct_length(self, params_2d, cosine_ic_2d):
        betti = betti_numbers(cosine_ic_2d, params_2d)
        assert len(betti) == 2  # d=2: [beta_0, beta_1]

    def test_3d_returns_three(self, params_3d, cosine_ic_3d):
        betti = betti_numbers(cosine_ic_3d, params_3d)
        assert len(betti) == 3
