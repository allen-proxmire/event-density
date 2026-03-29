"""
edsim.invariants.topology — Euler characteristic and Betti numbers.

Computes topological invariants of excursion sets {rho >= threshold}
for dimensions d = 2, 3 (and d = 4 with a simple extension).

The Euler characteristic is computed via the cubical complex formula:
for a binary mask X on a regular grid, count the k-dimensional cells
(vertices, edges, faces, cubes, ...) that are fully contained in X,
then compute chi = sum_k (-1)^k * C_k.

Betti numbers require persistent homology libraries (gudhi, dionysus)
and are provided as a stub with a simple beta_0 implementation.
"""

from __future__ import annotations

from typing import Optional

import numpy as np
from scipy.ndimage import label, generate_binary_structure

from ..core.parameters import EDParameters


# ---------------------------------------------------------------------------
# Euler characteristic via cubical complex cell counting
# ---------------------------------------------------------------------------

def _euler_2d(mask: np.ndarray) -> int:
    """Compute Euler characteristic of a 2D binary mask via cubical complex.

    For a 2D grid, the cubical complex has:
        V = vertices (grid points where mask is True)
        E = edges (pairs of adjacent True vertices, horizontal + vertical)
        F = faces (2x2 squares where all 4 corners are True)

    chi = V - E + F

    Parameters
    ----------
    mask : np.ndarray
        2D boolean array.

    Returns
    -------
    int
        Euler characteristic.
    """
    m = mask.astype(np.int32)
    Nx, Ny = m.shape

    # Vertices: count of True cells
    V = int(np.sum(m))

    # Edges: horizontal (along x) and vertical (along y)
    # A horizontal edge exists between (i,j) and (i+1,j) if both are True
    E_h = int(np.sum(m[:-1, :] & m[1:, :]))
    E_v = int(np.sum(m[:, :-1] & m[:, 1:]))
    E = E_h + E_v

    # Faces: 2x2 squares where all 4 corners are True
    F = int(np.sum(m[:-1, :-1] & m[1:, :-1] & m[:-1, 1:] & m[1:, 1:]))

    return V - E + F


def _euler_3d(mask: np.ndarray) -> int:
    """Compute Euler characteristic of a 3D binary mask via cubical complex.

    For a 3D grid, the cubical complex has:
        V = vertices (True voxels)
        E = edges (adjacent True pairs along each axis)
        F = faces (2x2 True squares in each plane)
        C = cubes (2x2x2 True blocks)

    chi = V - E + F - C

    Parameters
    ----------
    mask : np.ndarray
        3D boolean array.

    Returns
    -------
    int
        Euler characteristic.
    """
    m = mask.astype(np.int32)

    # Vertices
    V = int(np.sum(m))

    # Edges along each axis
    E_x = int(np.sum(m[:-1, :, :] & m[1:, :, :]))
    E_y = int(np.sum(m[:, :-1, :] & m[:, 1:, :]))
    E_z = int(np.sum(m[:, :, :-1] & m[:, :, 1:]))
    E = E_x + E_y + E_z

    # Faces in each plane (xy, xz, yz)
    F_xy = int(np.sum(m[:-1, :-1, :] & m[1:, :-1, :] & m[:-1, 1:, :] & m[1:, 1:, :]))
    F_xz = int(np.sum(m[:-1, :, :-1] & m[1:, :, :-1] & m[:-1, :, 1:] & m[1:, :, 1:]))
    F_yz = int(np.sum(m[:, :-1, :-1] & m[:, 1:, :-1] & m[:, :-1, 1:] & m[:, 1:, 1:]))
    F = F_xy + F_xz + F_yz

    # Cubes: 2x2x2 blocks where all 8 corners are True
    C = int(np.sum(
        m[:-1, :-1, :-1] & m[1:, :-1, :-1] &
        m[:-1, 1:, :-1] & m[1:, 1:, :-1] &
        m[:-1, :-1, 1:] & m[1:, :-1, 1:] &
        m[:-1, 1:, 1:] & m[1:, 1:, 1:]
    ))

    return V - E + F - C


def _euler_4d(mask: np.ndarray) -> int:
    """Compute Euler characteristic of a 4D binary mask via cubical complex.

    chi = V - E + F - C + H

    where V, E, F, C, H are counts of 0,1,2,3,4-dimensional cells.

    Parameters
    ----------
    mask : np.ndarray
        4D boolean array.

    Returns
    -------
    int
        Euler characteristic.
    """
    m = mask.astype(np.int32)
    s = slice(None)  # shorthand

    # --- 0-cells: vertices ---
    V = int(np.sum(m))

    # --- 1-cells: edges along each of 4 axes ---
    E = 0
    for ax in range(4):
        sl_lo = [s] * 4
        sl_hi = [s] * 4
        sl_lo[ax] = slice(0, -1)
        sl_hi[ax] = slice(1, None)
        E += int(np.sum(m[tuple(sl_lo)] & m[tuple(sl_hi)]))

    # --- 2-cells: faces in each of C(4,2)=6 planes ---
    F = 0
    axes = list(range(4))
    for i in range(4):
        for j in range(i + 1, 4):
            # 2x2 square in the (i,j) plane
            # Need all 4 corners: (0,0), (1,0), (0,1), (1,1) along axes i,j
            sl00 = [s] * 4
            sl10 = [s] * 4
            sl01 = [s] * 4
            sl11 = [s] * 4
            sl00[i] = slice(0, -1); sl00[j] = slice(0, -1)
            sl10[i] = slice(1, None); sl10[j] = slice(0, -1)
            sl01[i] = slice(0, -1); sl01[j] = slice(1, None)
            sl11[i] = slice(1, None); sl11[j] = slice(1, None)
            F += int(np.sum(
                m[tuple(sl00)] & m[tuple(sl10)] &
                m[tuple(sl01)] & m[tuple(sl11)]
            ))

    # --- 3-cells: cubes in each of C(4,3)=4 triples of axes ---
    C = 0
    for i in range(4):
        for j in range(i + 1, 4):
            for k in range(j + 1, 4):
                # 2x2x2 cube in the (i,j,k) hyperplane
                # The result shape has size N_a-1 along axes a in {i,j,k}, N_a along others
                result_shape = list(m.shape)
                result_shape[i] -= 1
                result_shape[j] -= 1
                result_shape[k] -= 1
                cube = np.ones(result_shape, dtype=bool)
                for bi in range(2):
                    for bj in range(2):
                        for bk in range(2):
                            sl = [s] * 4
                            sl[i] = slice(bi, m.shape[i] - 1 + bi)
                            sl[j] = slice(bj, m.shape[j] - 1 + bj)
                            sl[k] = slice(bk, m.shape[k] - 1 + bk)
                            cube &= m[tuple(sl)].astype(bool)
                C += int(np.sum(cube))

    # --- 4-cells: hypercubes (2x2x2x2 blocks) ---
    H = np.ones([n - 1 for n in m.shape], dtype=bool)
    for b0 in range(2):
        for b1 in range(2):
            for b2 in range(2):
                for b3 in range(2):
                    H &= m[b0:m.shape[0]-1+b0,
                           b1:m.shape[1]-1+b1,
                           b2:m.shape[2]-1+b2,
                           b3:m.shape[3]-1+b3].astype(bool)
    H_count = int(np.sum(H))

    return V - E + F - C + H_count


def euler_characteristic(
    rho: np.ndarray,
    params: EDParameters,
    threshold: Optional[float] = None,
) -> int:
    """Compute the Euler characteristic of the excursion set {rho >= threshold}.

    Uses the cubical complex formula on the binary grid:
        d=2: chi = V - E + F
        d=3: chi = V - E + F - C
        d=4: chi = V - E + F - C + H

    Parameters
    ----------
    rho : np.ndarray
        Density field (2D, 3D, or 4D).
    params : EDParameters
        Simulation parameters.
    threshold : float, optional
        Excursion threshold. Defaults to params.rho_star.

    Returns
    -------
    int
        Euler characteristic of {rho >= threshold}.
    """
    if threshold is None:
        threshold = params.rho_star

    mask = rho >= threshold
    d = rho.ndim

    if d == 2:
        return _euler_2d(mask)
    elif d == 3:
        return _euler_3d(mask)
    elif d == 4:
        return _euler_4d(mask)
    else:
        raise NotImplementedError(f"Euler characteristic not implemented for d={d}")


# ---------------------------------------------------------------------------
# Connected components
# ---------------------------------------------------------------------------

def connected_components(mask: np.ndarray) -> tuple[int, np.ndarray]:
    """Count connected components and label them.

    Uses full connectivity (8-connected in 2D, 26-connected in 3D, etc.).

    Parameters
    ----------
    mask : np.ndarray
        Binary mask (bool or int).

    Returns
    -------
    tuple[int, np.ndarray]
        (n_components, label_array).
    """
    d = mask.ndim
    structure = generate_binary_structure(d, d)  # full connectivity
    labels, n = label(mask.astype(np.int32), structure=structure)
    return int(n), labels


# ---------------------------------------------------------------------------
# Betti numbers (stub with beta_0 implementation)
# ---------------------------------------------------------------------------

def betti_numbers(
    rho: np.ndarray,
    params: EDParameters,
    threshold: Optional[float] = None,
) -> list[int]:
    """Compute Betti numbers of the excursion set {rho >= threshold}.

    Currently provides:
        - beta_0 = number of connected components (exact, via scipy.ndimage.label)
        - beta_1 ... beta_{d-1} = estimated from chi and beta_0

    For d=2: chi = beta_0 - beta_1, so beta_1 = beta_0 - chi.
    For d=3: chi = beta_0 - beta_1 + beta_2.  Without persistent homology,
             we cannot separate beta_1 and beta_2 independently.
             Returns [beta_0, chi_remainder, 0] as a placeholder.

    Full Betti number computation requires external libraries
    (gudhi, dionysus, or similar) and is not provided here.

    Parameters
    ----------
    rho : np.ndarray
        Density field.
    params : EDParameters
        Simulation parameters.
    threshold : float, optional
        Excursion threshold. Defaults to params.rho_star.

    Returns
    -------
    list[int]
        Betti numbers [beta_0, ..., beta_{d-1}].
        Higher Betti numbers are approximate for d >= 3.
    """
    if threshold is None:
        threshold = params.rho_star

    mask = rho >= threshold
    d = rho.ndim

    # beta_0: connected components (exact)
    beta_0, _ = connected_components(mask)

    # chi: Euler characteristic (exact)
    chi = euler_characteristic(rho, params, threshold)

    if d == 2:
        # chi = beta_0 - beta_1  =>  beta_1 = beta_0 - chi
        beta_1 = beta_0 - chi
        return [beta_0, max(beta_1, 0)]

    elif d == 3:
        # chi = beta_0 - beta_1 + beta_2
        # Without PH we can't separate beta_1 and beta_2.
        # We know beta_0 and chi; return [beta_0, ?, ?] with
        # the constraint beta_1 - beta_2 = beta_0 - chi.
        # As a simple heuristic: assume beta_2 = 0 (no enclosed voids),
        # giving beta_1 = beta_0 - chi.
        beta_1_est = beta_0 - chi
        return [beta_0, max(beta_1_est, 0), 0]

    elif d == 4:
        # chi = beta_0 - beta_1 + beta_2 - beta_3
        # Minimal stub: return [beta_0, 0, 0, 0]
        return [beta_0, 0, 0, 0]

    else:
        return [beta_0]
