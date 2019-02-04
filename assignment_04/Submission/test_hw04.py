# tests for HW 4

import numpy as np
import scipy.special
from numpy.testing import (assert_array_almost_equal,
                           assert_array_equal)

import pytest


class TestCountingVowels:
    text = """'But I don't want to go among mad people,' Alice remarked.
    'Oh, you can't help that,' said the Cat, 'we're all mad here. I'm mad. You're mad.'
    'How do you know I'm mad?' said Alice.
    'You must be,' said the Cat, 'or you wouldn't have come here.'"""

    expected = np.array([ 19.,  19.,   8.,  17.,   8.,   5.])

    def test_import_module(self):
        try:
            import problem1
        except ImportError:
            raise AssertionError("Cannot import problem1.py module")

    def test_import_function(self):
        try:
            from problem1 import count_vowels
        except ImportError:
            raise AssertionError("Cannot import the problem1.count_vowels function")

    def test_count_vowels(self):
        from problem1 import count_vowels
        computed = count_vowels(self.text)
        assert_array_equal(computed, self.expected,
                     err_msg="count_vowels() counted wrong")

    def test_counts(self):
        import problem1

        if not hasattr(problem1, "counts"):
            raise AssertionError("Variable problem1.counts not defined")

        assert_array_equal(problem1.counts, self.expected,
                               err_msg="counts wrong")


class TestMathFactorial:
    def test_import_module(self):
        try:
            import problem2a
        except ImportError:
            raise AssertionError("Cannot import problem2a.py module")

    def test_import_function(self):
        try:
            from problem2a import factorial_math
        except ImportError:
            raise AssertionError("Cannot import the problem2a.factorial_math function")

    def test_imports_math(self):
        import problem2a
        import math
        assert problem2a.math is math

    @pytest.mark.parametrize("n,expected",
                             np.array([np.arange(0, 21),
                                       scipy.special.factorial(np.arange(0, 21), exact=True)],
                                      dtype=np.int64).transpose())
    def test_factorial_math(self, n, expected):
        from  problem2a import factorial_math

        computed = factorial_math(n)
        assert computed == expected

class TestFactorial:
    def test_import_module(self):
        try:
            import problem2b
        except ImportError:
            raise AssertionError("Cannot import problem2b.py module")

    def test_import_function(self):
        try:
            from problem2b import factorial
        except ImportError:
            raise AssertionError("Cannot import the problem2a.factorial_math function")

    @pytest.mark.parametrize("n,expected",
                             np.array([np.arange(0, 21),
                                       scipy.special.factorial(np.arange(0, 21), exact=True)],
                                      dtype=np.int64).transpose())
    def test_factorial(self, n, expected):
        from  problem2b import factorial

        computed = factorial(n)
        assert computed == expected

    def test_own_function(self):
        from  problem2b import factorial
        try:
            factorial(-1)
        except ValueError:
            raise AssertionError("This looks like math.factorial()!")

class TestDoubleFactorial:
    def test_import_module(self):
        try:
            import problem2c
        except ImportError:
            raise AssertionError("Cannot import problem2c.py module")

    def test_import_function(self):
        try:
            from problem2c import double_factorial
        except ImportError:
            raise AssertionError("Cannot import the problem2c.double_factorial function")
    @pytest.mark.parametrize("n,expected",
                             np.array([np.arange(-1, 21, dtype=np.int64),
                                       np.array([1, 1, 1, 2, 3, 8, 15, 48, 105, 384, 945, 3840, 10395, 46080, 135135, 645120, 2027025, 10321920, 34459425, 185794560, 654729075, 3715891200])]).transpose())
    def test_double_factorial(self, n, expected):
        from  problem2c import double_factorial

        computed = double_factorial(n)
        assert computed == expected

