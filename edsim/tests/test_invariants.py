"""Tests for edsim.invariants — Energy, spectral, dissipation, correlation."""

import numpy as np
import pytest
from edsim.core.parameters import EDParameters
from edsim.experiments.runner import RunConfig, run_simulation


@pytest.fixture
def short_run_2d():
    """Run a short 2D simulation and return the TimeSeries."""
    params = EDParameters(
        d=2, N=(16, 16), L=(1.0, 1.0),
        D=0.3, H=0.15, zeta=0.1, tau=1.0,
        dt=5e-4, T=0.05, k_out=20,
        method="implicit_euler", bc="neumann",
    )
    config = RunConfig(params=params, ic_type="cosine", ic_kwargs={"A": 0.03, "Nm": 2})
    return run_simulation(config)


class TestEnergyInvariants:
    def test_energy_monotone(self, short_run_2d):
        E = short_run_2d.energy
        assert all(E[i] >= E[i + 1] - 1e-12 for i in range(len(E) - 1))

    def test_complexity_monotone(self, short_run_2d):
        C = short_run_2d.complexity
        assert all(C[i] >= C[i + 1] - 1e-12 for i in range(len(C) - 1))

    def test_mass_conserved(self, short_run_2d):
        M = short_run_2d.mass
        rel_change = abs(M[-1] - M[0]) / abs(M[0])
        assert rel_change < 0.01

    def test_energy_positive(self, short_run_2d):
        assert all(e >= 0 for e in short_run_2d.energy)

    def test_complexity_positive(self, short_run_2d):
        assert all(c >= 0 for c in short_run_2d.complexity)

    def test_constant_field_zero_complexity(self, params_2d):
        from edsim.invariants.energy import ed_complexity
        rho = np.full(params_2d.N, params_2d.rho_star)
        assert ed_complexity(rho, params_2d) < 1e-12


class TestSpectralInvariants:
    def test_entropy_decreases(self, short_run_2d):
        H = short_run_2d.spectral_entropy
        assert H[-1] < H[0]

    def test_entropy_positive(self, short_run_2d):
        assert all(h >= 0 for h in short_run_2d.spectral_entropy)

    def test_leading_mode_decays(self, short_run_2d):
        m0 = short_run_2d.modal_hierarchy[0][0]
        mT = short_run_2d.modal_hierarchy[-1][0]
        assert mT < m0

    def test_hierarchy_sorted_descending(self, short_run_2d):
        modes = short_run_2d.modal_hierarchy[0]
        assert all(modes[i] >= modes[i + 1] - 1e-15 for i in range(len(modes) - 1))


class TestDissipationInvariants:
    def test_ratios_sum_to_one(self, short_run_2d):
        for i in range(len(short_run_2d.times)):
            s = short_run_2d.R_grad[i] + short_run_2d.R_pen[i] + short_run_2d.R_part[i]
            assert abs(s - 1.0) < 1e-8

    def test_ratios_non_negative(self, short_run_2d):
        for i in range(len(short_run_2d.times)):
            assert short_run_2d.R_grad[i] >= -1e-10
            assert short_run_2d.R_pen[i] >= -1e-10
            assert short_run_2d.R_part[i] >= -1e-10


class TestCorrelationInvariants:
    def test_xi_positive(self, short_run_2d):
        assert all(x >= 0 for x in short_run_2d.correlation_length)

    def test_S2_non_negative(self, short_run_2d):
        for S2 in short_run_2d.structure_S2:
            assert np.all(S2 >= -1e-15)
