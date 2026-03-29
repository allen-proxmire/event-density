"""Tests for edsim.core.integrators — Implicit Euler and ETD-RK4."""

import numpy as np
import pytest
from edsim.core.parameters import EDParameters
from edsim.core.integrators.implicit_euler import ImplicitEulerIntegrator
from edsim.invariants.energy import lyapunov_energy, total_mass


class TestImplicitEuler:
    def test_single_step_reduces_energy(self, params_2d, cosine_ic_2d):
        integrator = ImplicitEulerIntegrator()
        state = integrator.setup(params_2d)
        E_before = lyapunov_energy(cosine_ic_2d, params_2d)
        rho_new, v_new, _ = integrator.step(cosine_ic_2d, 0.0, 0.0, params_2d, state)
        E_after = lyapunov_energy(rho_new, params_2d)
        assert E_after <= E_before + 1e-12

    def test_equilibrium_preserved(self, params_2d):
        rho = np.full(params_2d.N, params_2d.rho_star)
        integrator = ImplicitEulerIntegrator()
        state = integrator.setup(params_2d)
        rho_new, v_new, _ = integrator.step(rho, 0.0, 0.0, params_2d, state)
        assert np.allclose(rho_new, params_2d.rho_star, atol=1e-10)
        assert abs(v_new) < 1e-10

    def test_short_run_relaxes(self, params_2d, cosine_ic_2d):
        integrator = ImplicitEulerIntegrator()
        state = integrator.setup(params_2d)
        rho = cosine_ic_2d.copy()
        v = 0.0
        for _ in range(50):
            rho, v, state = integrator.step(rho, v, 0.0, params_2d, state)
        assert rho.std() < cosine_ic_2d.std()

    def test_mass_approximately_conserved(self, params_2d, cosine_ic_2d):
        integrator = ImplicitEulerIntegrator()
        state = integrator.setup(params_2d)
        M_before = total_mass(cosine_ic_2d, params_2d)
        rho = cosine_ic_2d.copy()
        v = 0.0
        for _ in range(20):
            rho, v, state = integrator.step(rho, v, 0.0, params_2d, state)
        M_after = total_mass(rho, params_2d)
        assert abs(M_after - M_before) / abs(M_before) < 0.01

    def test_3d_works(self, params_3d, cosine_ic_3d):
        integrator = ImplicitEulerIntegrator()
        state = integrator.setup(params_3d)
        rho_new, v_new, _ = integrator.step(cosine_ic_3d, 0.0, 0.0, params_3d, state)
        assert np.all(np.isfinite(rho_new))
        assert rho_new.shape == params_3d.N


class TestETDRK4:
    @pytest.fixture
    def params_etd(self):
        return EDParameters(
            d=2, N=(16, 16), L=(1.0, 1.0),
            D=0.3, H=0.15, zeta=0.1, tau=1.0,
            dt=1e-4, T=0.01, k_out=20,
            method="etdrk4", bc="neumann", seed=42,
        )

    def test_energy_monotone(self, params_etd):
        from edsim.experiments.runner import RunConfig, run_simulation
        config = RunConfig(params=params_etd, ic_type="cosine",
                           ic_kwargs={"A": 0.03, "Nm": 2})
        ts = run_simulation(config)
        E = ts.energy
        assert all(E[i] >= E[i + 1] - 1e-10 for i in range(len(E) - 1))

    def test_agrees_with_implicit_euler(self):
        """ETD-RK4 and IE should produce similar results over short T."""
        from edsim.experiments.runner import RunConfig, run_simulation
        base = dict(d=2, N=(16, 16), L=(1.0, 1.0), D=0.3, H=0.15,
                    zeta=0.1, tau=1.0, dt=1e-4, T=0.005, k_out=50,
                    bc="neumann", seed=42)
        p_ie = EDParameters(**base, method="implicit_euler")
        p_etd = EDParameters(**base, method="etdrk4")
        ts_ie = run_simulation(RunConfig(params=p_ie, ic_type="cosine",
                                         ic_kwargs={"A": 0.03, "Nm": 2}))
        ts_etd = run_simulation(RunConfig(params=p_etd, ic_type="cosine",
                                          ic_kwargs={"A": 0.03, "Nm": 2}))
        L2 = np.sqrt(np.mean((ts_ie.fields[-1] - ts_etd.fields[-1]) ** 2))
        assert L2 < 0.01  # should agree to ~1%
