"""
edsim.core.spectral — Spectral transform utilities and precomputed state.

Provides the SpectralState frozen dataclass that holds all precomputed
spectral quantities (eigenvalues, ETD coefficients), plus forward/inverse
transform wrappers using DCT-II (Neumann) and DFT (periodic).
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

import numpy as np
from scipy.fft import dctn, idctn

from .parameters import EDParameters


@dataclass(frozen=True)
class SpectralState:
    """Precomputed spectral data for the ETD-RK4 integrator.

    Constructed once at simulation start and reused at every step.
    Immutable to ensure zero hidden state.

    Attributes
    ----------
    d : int
        Spatial dimension.
    N : tuple[int, ...]
        Grid points per axis.
    eigenvalues : np.ndarray
        Laplacian eigenvalues mu_k (non-negative), shape N.
    linear_op : np.ndarray
        Linear operator lambda_k = -D*(M_star*mu_k + P0), shape N.
        All values are <= 0 (stable modes).
    E : np.ndarray
        exp(lambda_k * dt), shape N.
    E2 : np.ndarray
        exp(lambda_k * dt/2), shape N.
    f1 : np.ndarray
        ETD-RK4 coefficient phi_1(lambda_k * dt), shape N.
    f2 : np.ndarray
        ETD-RK4 coefficient phi_2(lambda_k * dt), shape N.
    f3 : np.ndarray
        ETD-RK4 coefficient phi_3(lambda_k * dt), shape N.
    """

    d: int
    N: tuple
    eigenvalues: np.ndarray
    linear_op: np.ndarray
    E: np.ndarray
    E2: np.ndarray
    Q: np.ndarray     # half-step phi_1 coefficient for stages a, b, c
    f1: np.ndarray    # full-step combination coefficient
    f2: np.ndarray    # full-step combination coefficient
    f3: np.ndarray    # full-step combination coefficient


def _compute_etd_coefficients(L: np.ndarray, dt: float) -> tuple:
    """Compute ETD-RK4 coefficients using the Kassam-Trefethen contour method.

    The Cox-Matthews ETD-RK4 scheme requires these coefficients:

        E   = exp(L*dt)              full-step exponential
        E2  = exp(L*dt/2)            half-step exponential

    For the half-step stages (a, b, c):
        Q   = dt/2 * phi_1(L*dt/2)  half-step nonlinear weight

    For the full-step combination:
        f1  = dt * (-4 - L*dt + E*(4 - 3*L*dt + (L*dt)^2)) / (L*dt)^3
        f2  = dt * (2 + L*dt + E*(-2 + L*dt)) / (L*dt)^3
        f3  = dt * (-4 - 3*L*dt - (L*dt)^2 + E*(4 - L*dt)) / (L*dt)^3

    Uses contour integration for numerical stability near L*dt = 0.

    Parameters
    ----------
    L : np.ndarray
        Linear operator eigenvalues (all <= 0).
    dt : float
        Time step.

    Returns
    -------
    tuple of (E, E2, Q, f1, f2, f3), each same shape as L.
    """
    Ldt = L * dt
    Ldt_h = Ldt / 2.0
    E = np.exp(Ldt)
    E2 = np.exp(Ldt_h)

    # Contour integral (M=32 points on unit circle)
    M = 32
    Q = np.zeros(Ldt.shape, dtype=np.complex128)   # half-step phi_1
    f1 = np.zeros(Ldt.shape, dtype=np.complex128)
    f2 = np.zeros(Ldt.shape, dtype=np.complex128)
    f3 = np.zeros(Ldt.shape, dtype=np.complex128)

    for m in range(1, M + 1):
        theta = 2.0 * np.pi * m / M
        r = np.exp(1j * theta)

        # Half-step contour for Q = (dt/2) * phi_1(Ldt/2)
        zh = Ldt_h + r
        Q += (dt / 2.0) * (np.exp(zh) - 1.0) / zh

        # Full-step contour for f1, f2, f3
        z = Ldt + r
        ez = np.exp(z)
        z2 = z * z
        z3 = z2 * z
        f1 += dt * (-4.0 - z + ez * (4.0 - 3.0 * z + z2)) / z3
        f2 += dt * (2.0 + z + ez * (-2.0 + z)) / z3
        f3 += dt * (-4.0 - 3.0 * z - z2 + ez * (4.0 - z)) / z3

    Q = np.real(Q / M)
    f1 = np.real(f1 / M)
    f2 = np.real(f2 / M)
    f3 = np.real(f3 / M)

    return E, E2, Q, f1, f2, f3


def build_spectral_state_2d(params: EDParameters) -> SpectralState:
    """Construct SpectralState for a 2D Neumann problem.

    The Neumann Laplacian eigenvalues for a DCT-II basis on [0, L] with
    N grid points are:

        mu_k = (k * pi / L)^2,  k = 0, 1, ..., N-1

    The 2D eigenvalues are the tensor product:
        mu_{kx, ky} = (kx*pi/Lx)^2 + (ky*pi/Ly)^2

    The linear operator for ETD splitting is:
        lambda_k = -D * (M_star * mu_k + P0)

    Parameters
    ----------
    params : EDParameters
        Simulation parameters (must have d == 2).

    Returns
    -------
    SpectralState
        Precomputed spectral data.
    """
    Nx, Ny = params.N
    Lx, Ly = params.L
    dt = params.dt
    D = params.D
    M_star = params.M_star
    P0 = params.P0

    # 1D wavenumber arrays
    kx = np.arange(Nx) * np.pi / Lx
    ky = np.arange(Ny) * np.pi / Ly

    # 2D eigenvalue grid: mu_{kx,ky} = kx^2 + ky^2
    KX, KY = np.meshgrid(kx, ky, indexing="ij")
    mu = KX ** 2 + KY ** 2

    # Linear operator: lambda_k = -D * (M_star * mu_k + P0)
    linear_op = -D * (M_star * mu + P0)

    # ETD coefficients
    E, E2, Q, f1, f2, f3 = _compute_etd_coefficients(linear_op, dt)

    return SpectralState(
        d=2,
        N=params.N,
        eigenvalues=mu,
        linear_op=linear_op,
        E=E,
        E2=E2,
        Q=Q,
        f1=f1,
        f2=f2,
        f3=f3,
    )


def build_spectral_state(params: EDParameters) -> SpectralState:
    """Construct a SpectralState from simulation parameters.

    Dispatches to dimension-specific builders.

    Parameters
    ----------
    params : EDParameters
        Simulation parameters.

    Returns
    -------
    SpectralState
        Precomputed spectral data.

    Raises
    ------
    NotImplementedError
        If the dimension is not yet supported for spectral methods.
    """
    if params.d == 2:
        return build_spectral_state_2d(params)
    else:
        raise NotImplementedError(
            f"Spectral state not yet implemented for d={params.d}. "
            f"Use method='implicit_euler' for d != 2."
        )


# ---------------------------------------------------------------------------
# Forward / inverse transforms
# ---------------------------------------------------------------------------

def forward_transform_2d(rho: np.ndarray) -> np.ndarray:
    """Forward DCT-II transform for 2D Neumann fields.

    Uses orthonormal normalization so Parseval's theorem holds.

    Parameters
    ----------
    rho : np.ndarray
        Density field in physical space, shape (Nx, Ny).

    Returns
    -------
    np.ndarray
        Spectral coefficients, same shape.
    """
    return dctn(rho, type=2, norm="ortho")


def inverse_transform_2d(rho_hat: np.ndarray) -> np.ndarray:
    """Inverse DCT-II transform for 2D Neumann fields.

    Parameters
    ----------
    rho_hat : np.ndarray
        Spectral coefficients, shape (Nx, Ny).

    Returns
    -------
    np.ndarray
        Density field in physical space.
    """
    return idctn(rho_hat, type=2, norm="ortho")


def forward_transform(rho: np.ndarray, bc: str) -> np.ndarray:
    """Forward spectral transform (physical -> spectral).

    Uses DCT-II (orthonormal) for Neumann BCs, FFT for periodic BCs.

    Parameters
    ----------
    rho : np.ndarray
        Density field in physical space, any dimension.
    bc : str
        Boundary condition type.

    Returns
    -------
    np.ndarray
        Spectral coefficients.
    """
    if bc == "neumann":
        return dctn(rho, type=2, norm="ortho")
    else:
        return np.fft.fftn(rho)


def inverse_transform(rho_hat: np.ndarray, bc: str) -> np.ndarray:
    """Inverse spectral transform (spectral -> physical).

    Uses IDCT-II for Neumann BCs, IFFT for periodic BCs.

    Parameters
    ----------
    rho_hat : np.ndarray
        Spectral coefficients.
    bc : str
        Boundary condition type.

    Returns
    -------
    np.ndarray
        Density field in physical space.
    """
    if bc == "neumann":
        return idctn(rho_hat, type=2, norm="ortho")
    else:
        return np.real(np.fft.ifftn(rho_hat))
