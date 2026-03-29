"""Tests for edsim.invariants.morphology — Hessian eigenvalues and classification."""

import numpy as np
import pytest
from edsim.invariants.morphology import hessian_eigenvalues, morphology_fractions


class TestHessianEigenvalues:
    def test_constant_field_zero(self, params_2d, constant_field_2d):
        eigvals = hessian_eigenvalues(constant_field_2d, params_2d)
        assert eigvals.shape == params_2d.N + (2,)
        assert np.allclose(eigvals, 0, atol=1e-10)

    def test_correct_shape_2d(self, params_2d, cosine_ic_2d):
        eigvals = hessian_eigenvalues(cosine_ic_2d, params_2d)
        assert eigvals.shape == params_2d.N + (2,)

    def test_correct_shape_3d(self, params_3d, cosine_ic_3d):
        eigvals = hessian_eigenvalues(cosine_ic_3d, params_3d)
        assert eigvals.shape == params_3d.N + (3,)

    def test_sorted_descending(self, params_2d, cosine_ic_2d):
        eigvals = hessian_eigenvalues(cosine_ic_2d, params_2d)
        # lambda_1 >= lambda_2 at every point
        assert np.all(eigvals[..., 0] >= eigvals[..., 1] - 1e-12)

    def test_finite_values(self, params_2d, cosine_ic_2d):
        eigvals = hessian_eigenvalues(cosine_ic_2d, params_2d)
        assert np.all(np.isfinite(eigvals))


class TestMorphologyFractions2D:
    def test_sum_to_one(self, params_2d, cosine_ic_2d):
        eigvals = hessian_eigenvalues(cosine_ic_2d, params_2d)
        morph = morphology_fractions(eigvals, params_2d)
        total = sum(morph.values())
        assert abs(total - 1.0) < 1e-10

    def test_blob_nontrivial(self, params_2d, cosine_ic_2d):
        eigvals = hessian_eigenvalues(cosine_ic_2d, params_2d)
        morph = morphology_fractions(eigvals, params_2d)
        assert morph["blob"] > 0.01

    def test_sheet_nontrivial(self, params_2d, cosine_ic_2d):
        eigvals = hessian_eigenvalues(cosine_ic_2d, params_2d)
        morph = morphology_fractions(eigvals, params_2d)
        assert morph["sheet"] > 0.01

    def test_no_filament_in_2d(self, params_2d, cosine_ic_2d):
        eigvals = hessian_eigenvalues(cosine_ic_2d, params_2d)
        morph = morphology_fractions(eigvals, params_2d)
        assert morph["filament"] == 0.0


class TestMorphologyFractions3D:
    def test_sum_to_one(self, params_3d, cosine_ic_3d):
        eigvals = hessian_eigenvalues(cosine_ic_3d, params_3d)
        morph = morphology_fractions(eigvals, params_3d)
        total = sum(morph.values())
        assert abs(total - 1.0) < 1e-10


class TestMorphologyFractions4D:
    def test_sum_to_one(self, params_4d, cosine_ic_4d):
        eigvals = hessian_eigenvalues(cosine_ic_4d, params_4d)
        morph = morphology_fractions(eigvals, params_4d)
        total = sum(morph.values())
        assert abs(total - 1.0) < 1e-10

    def test_has_pancake_or_filament(self, params_4d, cosine_ic_4d):
        eigvals = hessian_eigenvalues(cosine_ic_4d, params_4d)
        morph = morphology_fractions(eigvals, params_4d)
        assert morph.get("pancake", 0) > 0.001 or morph.get("filament", 0) > 0.001
