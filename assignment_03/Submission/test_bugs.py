import pytest

import numpy as np
from numpy.testing import assert_almost_equal

def test_a():
    try:
        import bug_a
    except ValueError as err:
        raise AssertionError("assignment not fixed (ValueError):\n{0}".format(err))
    except SyntaxError as err:
        raise AssertionError("comparison or if statement not fixed (SyntaxError):\n{0}".format(err))
    assert bug_a.value == "bar"

def test_b():
    try:
        import bug_b
    except TypeError as err:
        raise AssertionError("index access not fixed (TypeError):\n{0}".format(err))
    except IndexError as err:
        raise AssertionError("indexing error not fixed (IndexError):\n{0}".format(err))
    assert_almost_equal(bug_b.c, [57.6, 16.77, 32.4])

@pytest.mark.parametrize("x,y",
                         [[0, 0], [0, 1], [1, 0]] +
                         np.random.uniform(-100, 100, size=(30, 2)).tolist()
)
def test_c(x, y):
    import bug_c

    result = bug_c.sinc(x, y)
    # see https://docs.scipy.org/doc/numpy/reference/generated/numpy.sinc.html
    ref = np.sinc(x/np.pi) * np.sinc(y/np.pi)

    assert_almost_equal(result, ref)

def test_c_import():
    try:
        import bug_c
    except SyntaxError as err:
        raise AssertionError("Check the Python code... (SyntaxError):\n{0}".format(err))
    except IndexError as err:
        raise AssertionError("indexing error not fixed (IndexError):\n{0}".format(err))


