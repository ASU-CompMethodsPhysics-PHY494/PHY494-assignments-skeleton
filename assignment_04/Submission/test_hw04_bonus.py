# tests for HW 4 Bonus problems

import numpy as np
from numpy.testing import assert_array_almost_equal

import pytest


class TestProblem3:
    def test_import_module(self):
        try:
            import problem3
        except ImportError:
            raise AssertionError("Cannot import problem3.py module")

    def test_import_function(self):
        try:
            from problem3 import double_factorial
        except ImportError:
            raise AssertionError("Cannot import the problem3.double_factorial function")
    @pytest.mark.parametrize("n,expected",
                             np.array([np.arange(-1, 21),
                                       np.array([1, 1, 1, 2, 3, 8, 15, 48, 105, 384, 945, 3840, 10395, 46080, 135135, 645120, 2027025, 10321920, 34459425, 185794560, 654729075, 3715891200])]).transpose())
    def test_double_factorial(self, n, expected):
        from  problem3 import double_factorial

        computed = double_factorial(n)
        assert computed == expected

