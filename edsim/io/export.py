"""
edsim.io.export — Export simulation results to JSON, NPZ, and HDF5.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import numpy as np

from ..core.parameters import EDParameters


def export_json(
    data: dict,
    path: str | Path,
    params: Optional[EDParameters] = None,
) -> None:
    """Export a dictionary of results to a JSON file.

    NumPy arrays are converted to lists. EDParameters are serialised
    via ``to_dict()``.

    Parameters
    ----------
    data : dict
        Results to export.
    path : str or Path
        Output file path.
    params : EDParameters, optional
        If provided, included as metadata.
    """
    # TODO: json.dump with numpy serializer
    pass


def export_npz(
    arrays: dict[str, np.ndarray],
    path: str | Path,
) -> None:
    """Export named arrays to a compressed NPZ file.

    Parameters
    ----------
    arrays : dict[str, np.ndarray]
        Named arrays to save.
    path : str or Path
        Output file path.
    """
    # TODO: np.savez_compressed
    pass


def export_hdf5(
    data: dict,
    path: str | Path,
) -> None:
    """Export results to an HDF5 file (requires h5py).

    Parameters
    ----------
    data : dict
        Results to export. Supports nested dicts, arrays, and scalars.
    path : str or Path
        Output file path.

    Raises
    ------
    ImportError
        If h5py is not installed.
    """
    # TODO: try import h5py; create groups/datasets
    pass


# Work around forward reference
from typing import Optional
