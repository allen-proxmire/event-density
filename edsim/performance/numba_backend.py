"""
edsim.performance.numba_backend — Numba-accelerated FD operators.

Provides JIT-compiled versions of the core FD stencils. If Numba is not
installed, all functions fall back to the NumPy implementations.

The accelerated functions have identical signatures and semantics to
their NumPy counterparts in edsim.core.operators.
"""

from __future__ import annotations

import numpy as np

try:
    from numba import njit, prange
    NUMBA_AVAILABLE = True
except ImportError:
    NUMBA_AVAILABLE = False


if NUMBA_AVAILABLE:

    @njit(cache=True, parallel=True)
    def _laplacian_2d_numba(rho, dx0, dx1):
        """Numba-accelerated 2D Laplacian with Neumann (mirror) BCs."""
        Nx, Ny = rho.shape
        lap = np.empty_like(rho)
        idx2 = 1.0 / (dx0 * dx0)
        idy2 = 1.0 / (dx1 * dx1)

        for i in prange(Nx):
            for j in range(Ny):
                # Mirror BC indices
                im = i - 1 if i > 0 else 1
                ip = i + 1 if i < Nx - 1 else Nx - 2
                jm = j - 1 if j > 0 else 1
                jp = j + 1 if j < Ny - 1 else Ny - 2

                lap[i, j] = (
                    (rho[ip, j] + rho[im, j] - 2.0 * rho[i, j]) * idx2
                    + (rho[i, jp] + rho[i, jm] - 2.0 * rho[i, j]) * idy2
                )
        return lap

    @njit(cache=True, parallel=True)
    def _grad_squared_2d_numba(rho, dx0, dx1):
        """Numba-accelerated 2D |grad rho|^2 with Neumann BCs."""
        Nx, Ny = rho.shape
        gs = np.empty_like(rho)
        inv2dx0 = 0.5 / dx0
        inv2dx1 = 0.5 / dx1

        for i in prange(Nx):
            for j in range(Ny):
                im = i - 1 if i > 0 else 1
                ip = i + 1 if i < Nx - 1 else Nx - 2
                jm = j - 1 if j > 0 else 1
                jp = j + 1 if j < Ny - 1 else Ny - 2

                gx = (rho[ip, j] - rho[im, j]) * inv2dx0
                gy = (rho[i, jp] - rho[i, jm]) * inv2dx1
                gs[i, j] = gx * gx + gy * gy
        return gs

    @njit(cache=True, parallel=True)
    def _laplacian_3d_numba(rho, dx0, dx1, dx2):
        """Numba-accelerated 3D Laplacian with Neumann BCs."""
        Nx, Ny, Nz = rho.shape
        lap = np.empty_like(rho)
        idx2 = 1.0 / (dx0 * dx0)
        idy2 = 1.0 / (dx1 * dx1)
        idz2 = 1.0 / (dx2 * dx2)

        for i in prange(Nx):
            for j in range(Ny):
                for k in range(Nz):
                    im = i - 1 if i > 0 else 1
                    ip = i + 1 if i < Nx - 1 else Nx - 2
                    jm = j - 1 if j > 0 else 1
                    jp = j + 1 if j < Ny - 1 else Ny - 2
                    km = k - 1 if k > 0 else 1
                    kp = k + 1 if k < Nz - 1 else Nz - 2

                    lap[i, j, k] = (
                        (rho[ip, j, k] + rho[im, j, k] - 2.0 * rho[i, j, k]) * idx2
                        + (rho[i, jp, k] + rho[i, jm, k] - 2.0 * rho[i, j, k]) * idy2
                        + (rho[i, j, kp] + rho[i, j, km] - 2.0 * rho[i, j, k]) * idz2
                    )
        return lap

    @njit(cache=True, parallel=True)
    def _F_local_2d_numba(rho, dx0, dx1, M0, beta, P0, rho_star, rho_max):
        """Numba-accelerated 2D F_local = M*Lap + M'*|grad|^2 - P."""
        Nx, Ny = rho.shape
        F = np.empty_like(rho)
        idx2 = 1.0 / (dx0 * dx0)
        idy2 = 1.0 / (dx1 * dx1)
        inv2dx0 = 0.5 / dx0
        inv2dx1 = 0.5 / dx1

        for i in prange(Nx):
            for j in range(Ny):
                im = i - 1 if i > 0 else 1
                ip = i + 1 if i < Nx - 1 else Nx - 2
                jm = j - 1 if j > 0 else 1
                jp = j + 1 if j < Ny - 1 else Ny - 2

                r = rho[i, j]
                delta = rho_max - r
                if delta < 0.0:
                    delta = 0.0

                M = M0 * delta ** beta
                Mp = -beta * M0 * delta ** (beta - 1.0) if delta > 0 else 0.0
                P = P0 * (r - rho_star)

                lap = (
                    (rho[ip, j] + rho[im, j] - 2.0 * r) * idx2
                    + (rho[i, jp] + rho[i, jm] - 2.0 * r) * idy2
                )
                gx = (rho[ip, j] - rho[im, j]) * inv2dx0
                gy = (rho[i, jp] - rho[i, jm]) * inv2dx1
                gs = gx * gx + gy * gy

                F[i, j] = M * lap + Mp * gs - P
        return F

    # -------------------------------------------------------------------
    # Public wrappers matching the operators.py API
    # -------------------------------------------------------------------

    def laplacian_fd_2d_numba(rho, dx):
        return _laplacian_2d_numba(rho, dx[0], dx[1])

    def grad_squared_fd_2d_numba(rho, dx):
        return _grad_squared_2d_numba(rho, dx[0], dx[1])

    def laplacian_fd_3d_numba(rho, dx):
        return _laplacian_3d_numba(rho, dx[0], dx[1], dx[2])

    def operator_F_local_fd_2d_numba(rho, params):
        return _F_local_2d_numba(
            rho, params.dx[0], params.dx[1],
            params.M0, params.beta, params.P0, params.rho_star, params.rho_max,
        )

else:
    # Stubs that delegate to NumPy when Numba is not installed
    def laplacian_fd_2d_numba(rho, dx):
        from ..core.operators import laplacian_fd_2d
        return laplacian_fd_2d(rho, dx)

    def grad_squared_fd_2d_numba(rho, dx):
        from ..core.operators import grad_squared_fd_2d
        return grad_squared_fd_2d(rho, dx)

    def laplacian_fd_3d_numba(rho, dx):
        from ..core.operators import laplacian_fd_3d
        return laplacian_fd_3d(rho, dx)

    def operator_F_local_fd_2d_numba(rho, params):
        from ..core.operators import operator_F_local_fd_2d
        return operator_F_local_fd_2d(rho, params)
