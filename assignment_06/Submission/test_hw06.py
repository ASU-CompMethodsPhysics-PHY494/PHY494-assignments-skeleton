# tests for HW 5

import importlib
import math
import random
import numpy as np
from numpy.testing import assert_almost_equal

import pytest

class TestExpSeries:
    @pytest.fixture(scope="class")
    def solution(self):
        return importlib.import_module("problem2")

    def test_import_module(self):
        try:
            import problem2
        except ImportError:
            raise AssertionError("Cannot import problem2.py module")

    def test_import_function(self):
        try:
            from problem2 import exp_series
        except ImportError:
            raise AssertionError("Cannot import the problem1.exp_series function")

    def _exp_series(self, eps, solution):
        return np.array([solution.exp_series(x, eps=eps) for x in self.values])


    @pytest.fixture(scope="class")
    def values(self):
        return np.array([-9.2103437, 0, 1, 100])

    @pytest.fixture(scope="class")
    def reference(self):
        return {1e-15: np.array([9.999966701933933e-05, 1.0,
                                 2.7182818284590455, 2.688117141816135e+43]),
                1e-4: np.array([0.00010000127692008946, 1.0,
                                2.7182539682539684, 2.6876222340022607e+43]),
        }

    @pytest.mark.parametrize("eps", (1e-15, 1e-4))
    def test_exp_series(self, eps, values, reference, solution):
        decimal = abs(int(np.log10(eps)))
        computed = np.array([solution.exp_series(x, eps=eps) for x in values])
        expected = reference[eps]
        assert_almost_equal(computed, expected,
                            decimal=decimal,
                            err_msg="exp_series gives wrong answer for eps={}".format(eps))


@pytest.mark.xfail
class TestStableSum:
    @pytest.fixture(scope="class")
    def solution(self):
        return importlib.import_module("problem3")

    @pytest.mark.parametrize("values",
                             [
                                 [1, 1e100, 1, -1e100] * 10000,
                                 [1, 1e100, 1, -1e100] * int(1e6),
                             ])
    def test_stable_sum(self, values, solution):
        assert_almost_equal(solution.stable_sum(values), math.fsum(values))

    @pytest.fixture(scope="class", params=range(5))
    def random_values(self, request):
        # random sequence of values for each request.param

        # test due to Raymond Hettinger (used under PSF License)
        # Full URL available in the solution (not given here as
        # I don't want to make it too easy to find a solution...)
        values = [6, 2e100, -6, -2e100, -10e-20, 9e-20] * 100
        s = 0
        for i in range(200):
            v = random.gauss(0, random.random()) ** 7 - s
            s += v
            values.append(v)
        random.shuffle(values)
        return values

    def test_stable_sum_random(self, random_values, solution):
        assert_almost_equal(solution.stable_sum(random_values),
                            math.fsum(random_values))
