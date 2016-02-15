# Test that the calculus module functions
# You can run the tests from within this directory with
#
#     nosetests -v test_calculus.py
#
# You should not get any tests with status FAILED or ERROR.

import numpy as np
from numpy.testing import assert_almost_equal


def test_import():
    try:
        import calculus
    except ImportError:
        raise AssertionError("calculus module failed to import")

class TestIntegration():
    def setUp(self):
        self.func = np.cos
        self.bounds = -10*np.pi, np.pi/2
        self.exact = self.exact_integral_cos(*self.bounds)

    @staticmethod
    def exact_integral_cos(a, b):
        """Integral cos x from a to b"""
        return np.sin(b) - np.sin(a)

    def test_simpson(self, N=1001):
        from calculus import simpson
        result = simpson(self.func, self.bounds[0], self.bounds[1], N)
        assert_almost_equal(result, self.exact, decimal=6,
                            err_msg="simpson integration failed")

    def test_trapezoidal(self, N=1001):
        from calculus import trapezoidal
        result = trapezoidal(self.func, self.bounds[0], self.bounds[1], N)
        assert_almost_equal(result, self.exact, decimal=3,
                            err_msg="trapezoidal integration failed")


class TestDifferentiation():
    def setUp(self):
        self.t_values = np.array([0.1, 1, 100], dtype=np.float64)
        self.func = np.cos
        self.exact = self.D_exact(self.t_values)

    @staticmethod
    def D_exact(t):
        return -np.sin(t)

    def test_forward_difference(self, h=1e-6):
        from calculus import D_fd
        results = D_fd(self.func, self.t_values, h)
        assert_almost_equal(results, self.exact, decimal=6,
                            err_msg="D_fd with h={0} gives wrong result".format(h))

    def test_central_difference(self, h=1e-6):
        from calculus import D_cd
        results = D_cd(self.func, self.t_values, h)
        assert_almost_equal(results, self.exact, decimal=9,
                            err_msg="D_cd with h={0} gives wrong result".format(h))

