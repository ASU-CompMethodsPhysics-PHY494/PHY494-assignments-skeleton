# tests for HW 4

import numpy as np
from numpy.testing import (assert_array_almost_equal,
                           assert_array_equal)

import pytest

class TestProblem2:
    values = np.array([-9.2103437, 0, 1, 100])

    def test_import_module(self):
        try:
            import problem2
        except ImportError:
            raise AssertionError("Cannot import problem2.py module")

    def test_import_function(self):
        try:
            from problem2 import exp_series
        except ImportError:
            raise AssertionError("Cannot import the problem2.exp_series function")

    def _exp_series(self, eps):
        from  problem2 import exp_series
        return np.array([exp_series(x, eps=eps) for x in self.values])

    @pytest.mark.parametrize("eps,expected", [
        (1e-15,
         np.array([9.999966701933933e-05, 1.0,
                   2.7182818284590455, 2.688117141816135e+43])),
        (1e-4,
         np.array([0.00010000127692008946, 1.0,
                    2.7182539682539684, 2.6876222340022607e+43])),
        ])
    def test_exp_series(self, eps, expected):
        decimal = abs(int(np.log10(eps)))
        computed = self._exp_series(eps)
        assert_array_almost_equal(computed, expected,
                                  decimal=decimal,
                                  err_msg="exp_series gives wrong answer for eps={}".format(eps))


class TestProblem4:
    text = """'But I don't want to go among mad people,' Alice remarked.
    'Oh, you can't help that,' said the Cat, 'we're all mad here. I'm mad. You're mad.'
    'How do you know I'm mad?' said Alice.
    'You must be,' said the Cat, 'or you wouldn't have come here.'"""

    def test_import_module(self):
        try:
            import problem4
        except ImportError:
            raise AssertionError("Cannot import problem4.py module")

    def test_import_function(self):
        try:
            from problem4 import count_vowels
        except ImportError:
            raise AssertionError("Cannot import the problem4.count_vowels function")

    def test_count_vowels(self):
        from problem4 import count_vowels
        computed = count_vowels(self.text)
        expected = np.array([ 19.,  19.,   8.,  17.,   8.,   5.])
        assert_array_equal(computed, expected,
                           err_msg="count_vowels() counted wrong")
