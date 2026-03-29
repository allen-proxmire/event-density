"""Science tests for the ED architectural laws across dimensions.

These are regression/science tests that verify the nine laws established
in ED-Phys-40 hold for the ED-SIM-02 numerical implementation.
Uses generous tolerances — these confirm qualitative behaviour, not proofs.
"""

from __future__ import annotations

import numpy as np
import pytest

from edsim.experiments.scenarios import get_scenario
from edsim.experiments.atlas import run_atlas, summarize_time_series
from edsim.invariants.topology import euler_characteristic


@pytest.fixture(scope="module")
def results_2d():
    """Run 2D cosine scenario once for the module."""
    _, ts = run_atlas(get_scenario("A_2d_cosine"))
    return ts


@pytest.fixture(scope="module")
def results_3d():
    """Run 3D cosine scenario once for the module."""
    _, ts = run_atlas(get_scenario("B_3d_cosine"))
    return ts


@pytest.fixture(scope="module")
def results_4d():
    """Run 4D cosine scenario once for the module."""
    _, ts = run_atlas(get_scenario("C_4d_cosine"))
    return ts


class TestLaw1UniqueAttractor:
    """Law 1: rho -> rho_star, v -> 0."""

    def test_2d_rho_relaxes(self, results_2d):
        assert results_2d.fields[-1].std() < results_2d.fields[0].std()

    def test_3d_rho_relaxes(self, results_3d):
        assert results_3d.fields[-1].std() < results_3d.fields[0].std()

    def test_4d_rho_relaxes(self, results_4d):
        assert results_4d.fields[-1].std() < results_4d.fields[0].std()

    def test_2d_v_small(self, results_2d):
        assert abs(results_2d.v_history[-1]) < 0.1


class TestLaw2EnergyMonotonicity:
    """Law 2: E(t) monotonically decreasing."""

    def test_2d(self, results_2d):
        E = results_2d.energy
        assert all(E[i] >= E[i + 1] - 1e-12 for i in range(len(E) - 1))

    def test_3d(self, results_3d):
        E = results_3d.energy
        assert all(E[i] >= E[i + 1] - 1e-12 for i in range(len(E) - 1))

    def test_4d(self, results_4d):
        E = results_4d.energy
        assert all(E[i] >= E[i + 1] - 1e-12 for i in range(len(E) - 1))

    def test_2d_complexity_monotone(self, results_2d):
        C = results_2d.complexity
        assert all(C[i] >= C[i + 1] - 1e-12 for i in range(len(C) - 1))


class TestLaw3SpectralDecay:
    """Law 3: Modes decay exponentially; spectral entropy decreases."""

    def test_entropy_ordering(self, results_2d, results_3d, results_4d):
        """H(4D) > H(3D) > H(2D) at t=0 — more modes in higher d."""
        H2 = results_2d.spectral_entropy[0]
        H3 = results_3d.spectral_entropy[0]
        H4 = results_4d.spectral_entropy[0]
        assert H4 > H3 > H2

    def test_2d_entropy_decreases(self, results_2d):
        assert results_2d.spectral_entropy[-1] < results_2d.spectral_entropy[0]

    def test_2d_leading_mode_decays(self, results_2d):
        m0 = results_2d.modal_hierarchy[0][0]
        mT = results_2d.modal_hierarchy[-1][0]
        assert mT < m0


class TestLaw5DissipationChannels:
    """Law 5: R_grad + R_pen + R_part = 1; dissipation well-defined."""

    def test_sum_to_one_2d(self, results_2d):
        for i in range(len(results_2d.times)):
            s = results_2d.R_grad[i] + results_2d.R_pen[i] + results_2d.R_part[i]
            assert abs(s - 1.0) < 1e-8

    def test_sum_to_one_3d(self, results_3d):
        for i in range(len(results_3d.times)):
            s = results_3d.R_grad[i] + results_3d.R_pen[i] + results_3d.R_part[i]
            assert abs(s - 1.0) < 1e-8


class TestLaw6TopologicalConservation:
    """Law 6: chi constant at a fixed threshold below the field."""

    def test_2d_chi_conserved_low_threshold(self, results_2d):
        from edsim.core.parameters import EDParameters
        p = EDParameters(d=2, N=(32, 32), L=(1.0, 1.0))
        low_thresh = p.rho_star - 0.2
        chis = [euler_characteristic(f, p, threshold=low_thresh) for f in results_2d.fields]
        assert len(set(chis)) == 1, f"chi values: {set(chis)}"


class TestCorrelationScaling:
    """Correlation length grows in higher dimensions."""

    def test_xi_ordering_at_t0(self, results_2d, results_3d, results_4d):
        xi2 = results_2d.correlation_length[0]
        xi3 = results_3d.correlation_length[0]
        xi4 = results_4d.correlation_length[0]
        # 4D >= 3D (with small tolerance for numerical effects)
        assert xi4 >= xi3 - 0.05

    def test_2d_xi_grows(self, results_2d):
        """Cosine IC: xi grows as high-k modes decay faster."""
        xi0 = results_2d.correlation_length[0]
        xiT = results_2d.correlation_length[-1]
        assert xiT >= xi0 - 0.01


class TestMorphologyFractions:
    """Morphology fractions are valid across all dimensions."""

    def test_2d_sum(self, results_2d):
        for m in results_2d.morphology_fractions:
            assert abs(sum(m.values()) - 1.0) < 1e-10

    def test_3d_sum(self, results_3d):
        for m in results_3d.morphology_fractions:
            assert abs(sum(m.values()) - 1.0) < 1e-10

    def test_4d_sum(self, results_4d):
        for m in results_4d.morphology_fractions:
            assert abs(sum(m.values()) - 1.0) < 1e-10

    def test_4d_has_pancake_or_filament(self, results_4d):
        m = results_4d.morphology_fractions[0]
        assert m.get("pancake", 0) > 0.001 or m.get("filament", 0) > 0.001
