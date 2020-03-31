# tests for HW10 solution


import pytest

import numpy as np

from numpy.testing import (assert_array_almost_equal,
                           assert_array_equal,
                           assert_equal,
                           assert_almost_equal)


def test_import_module():
    try:
        import functions
    except ImportError:
        raise AssertionError("Cannot import functions.py module")

def test_import_function():
    try:
        from functions import sqrt
    except ImportError:
        raise AssertionError("Cannot import the functions.sqrt function")

@pytest.mark.parametrize('decimals', [6, 4, 3, 8, 12])
@pytest.mark.parametrize('x',
                         [0, pytest.mark.xfail(0.456e-8),
                          pytest.mark.xfail(1e-3), 0.1, 0.64, 0.99,
                          1, 5, 9, 12.5, 1e3, 1.2345e8])
def test_sqrt(x, decimals):
    import functions
    tol = 10**(-decimals)
    assert_almost_equal(functions.sqrt(x, tol=tol), np.sqrt(x), decimal=decimals-1)

