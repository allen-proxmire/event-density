"""
edsim.tests.conftest — Shared pytest fixtures for ED-SIM-02 tests.

Provides small-grid EDParameters and standard initial conditions
for fast testing across dimensions d = 2, 3, 4.
"""

from __future__ import annotations

import numpy as np
import pytest

from edsim.core.parameters import EDParameters
from edsim.experiments.runner import generate_ic


# ---------------------------------------------------------------------------
# Parameters fixtures
# ---------------------------------------------------------------------------

@pytest.fixture
def params_2d() -> EDParameters:
    """Small 2D parameters for fast testing."""
    return EDParameters(
        d=2, N=(16, 16), L=(1.0, 1.0),
        D=0.3, H=0.15, zeta=0.1, tau=1.0,
        rho_star=0.5, rho_max=1.0, M0=1.0, beta=2.0, P0=1.0,
        dt=5e-4, T=0.05, k_out=20,
        method="implicit_euler", bc="neumann", seed=42,
    )


@pytest.fixture
def params_3d() -> EDParameters:
    """Small 3D parameters for fast testing."""
    return EDParameters(
        d=3, N=(8, 8, 8), L=(1.0, 1.0, 1.0),
        D=0.3, H=0.15, zeta=0.1, tau=1.0,
        rho_star=0.5, rho_max=1.0, M0=1.0, beta=2.0, P0=1.0,
        dt=5e-4, T=0.025, k_out=10,
        method="implicit_euler", bc="neumann", seed=42,
    )


@pytest.fixture
def params_4d() -> EDParameters:
    """Small 4D parameters for fast testing."""
    return EDParameters(
        d=4, N=(6, 6, 6, 6), L=(1.0, 1.0, 1.0, 1.0),
        D=0.3, H=0.15, zeta=0.1, tau=1.0,
        rho_star=0.5, rho_max=1.0, M0=1.0, beta=2.0, P0=1.0,
        dt=5e-4, T=0.01, k_out=4,
        method="implicit_euler", bc="neumann", seed=42,
    )


# ---------------------------------------------------------------------------
# Initial condition fixtures
# ---------------------------------------------------------------------------

@pytest.fixture
def cosine_ic_2d(params_2d) -> np.ndarray:
    """Standard 2D cosine IC with A=0.03, Nm=2."""
    grid = params_2d.make_grid()
    return generate_ic("cosine", grid, params_2d, A=0.03, Nm=2)


@pytest.fixture
def cosine_ic_3d(params_3d) -> np.ndarray:
    """Standard 3D cosine IC with A=0.03, Nm=2."""
    grid = params_3d.make_grid()
    return generate_ic("cosine", grid, params_3d, A=0.03, Nm=2)


@pytest.fixture
def cosine_ic_4d(params_4d) -> np.ndarray:
    """Standard 4D cosine IC with A=0.03, Nm=2."""
    grid = params_4d.make_grid()
    return generate_ic("cosine", grid, params_4d, A=0.03, Nm=2)


@pytest.fixture
def random_ic_2d(params_2d) -> np.ndarray:
    """2D random IC with A=0.02, fixed seed."""
    grid = params_2d.make_grid()
    return generate_ic("random", grid, params_2d, A=0.02)


@pytest.fixture
def constant_field_2d(params_2d) -> np.ndarray:
    """Uniform 2D field at rho_star."""
    return np.full(params_2d.N, params_2d.rho_star)


@pytest.fixture
def constant_field_3d(params_3d) -> np.ndarray:
    """Uniform 3D field at rho_star."""
    return np.full(params_3d.N, params_3d.rho_star)
