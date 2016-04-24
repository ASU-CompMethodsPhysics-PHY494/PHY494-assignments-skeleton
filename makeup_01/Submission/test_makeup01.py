# Tests for ASU PHY494 Makeup01

import os.path
import itertools

import numpy as np
import numpy.random
import scipy.misc

from numpy.testing import (assert_array_almost_equal, assert_equal,
                           assert_raises, assert_, assert_almost_equal,
                           )

import makeup01

class TestFactorial(object):
    def test_factorial(self, nmax=10000, ntests=6):
        def assert_factorial(n):
            reference = scipy.misc.factorial(n, exact=True)
            assert_equal(makeup01.factorial(int(n)), reference)

        for n in numpy.random.random_integers(nmax, size=ntests):
            yield assert_factorial, n

    def test_zero(self):
        assert_equal(makeup01.factorial(0), 1)

    def test_one(self):
        assert_equal(makeup01.factorial(1), 1)

    def test_TypeError(self):
        assert_raises(TypeError, makeup01.factorial, 0.5)

    def test_ValueError(self):
        assert_raises(ValueError, makeup01.factorial, -3)

class TestODE(object):
    def setUp(self):
        self.xmin = 0
        self.xmax = 6
        self.dx = 0.01
        self.x = np.arange(self.xmin, self.xmax, self.dx)
        self.y0 = np.array([1., 0.])
        self.n_values = (0, 2, 8)
        self.figname = "qmhosc.pdf"

    def tearDown(self):
        pass

    def test_figure_pdf(self):
        try:
            # generate figures on demand...
            makeup01.plot_all_ode_figures()
        except:
            pass
        assert_(os.path.exists(self.figname),
                "Figure {} is missing.".format(self.figname))

    def test_f_qmhosc(self):
        self.setUp()

        def assert_even(n):
            En = n + 0.5
            f = makeup01.f_qmhosc([1., 0.], 0., En)
            assert_array_almost_equal(f, [0, -2*En])

        try:
            for n in self.n_values:
                yield assert_even, n
        finally:
            self.tearDown()

    def test_integration_range(self):
        y = makeup01.ode_qmhosc(self.x, self.y0[0], self.y0[1], 0)
        assert_equal(len(y), len(self.x),
                     err_msg="different number of x values (0 <= x < 6, dx=0.01)")

    def test_ode_qmhosc_x0_behavior(self):
        self.setUp()
        def assert_even(n, ix=0):
            y = makeup01.ode_qmhosc(self.x, self.y0[0], self.y0[1], n)
            assert_almost_equal(y[ix], self.y0, decimal=6)
        try:
            for n in self.n_values:
                yield assert_even, n
        finally:
            self.tearDown()

    def test_ode_qmhosc_large_x_behavior(self):
        self.setUp()
        def assert_even(n, ix=-1):
            y = makeup01.ode_qmhosc(self.x, self.y0[0], self.y0[1], n)
            assert_almost_equal(y[ix], [0, 0], decimal=2)
        try:
            for n, ix in itertools.zip_longest(self.n_values, (-200, -100), fillvalue=-1):
                yield assert_even, n, ix
        finally:
            self.tearDown()

    def test_ode_qmhosc_integral(self):
        self.setUp()
        def assert_even(n, value, ix=-1):
            y = makeup01.ode_qmhosc(self.x, self.y0[0], self.y0[1], n)
            psi = y[:ix, 0]
            norm = 0.5 * scipy.integrate.simps(psi**2, x=self.x[:ix])
            assert_almost_equal(norm, value, decimal=5)
        try:
            for n, value, ix in zip(self.n_values,
                                    (0.44311342242174678, 0.8862267907458522, 1.6205289343075246),
                                    (-150, -100, -1)):
                yield assert_even, n, value, ix
        finally:
            self.tearDown()

class TestODEbonus(TestODE):
    def setUp(self):
        super(TestODEbonus, self).setUp()
        self.y0 = self.y0[::-1]
        self.n_values = (1, 3)
        self.figname = name="qmhosc_odd.pdf"

    def test_initial_values_qmhosc(self):
        self.setUp()
        def assert_initial(n):
            y0 = makeup01.initial_values_qmhosc(n)
            if n % 2 == 0:
                assert_almost_equal(y0, [1, 0])
            else:
                assert_almost_equal(y0, [0, 1])
        try:
            yield assert_initial, 0
            yield assert_initial, 1
        finally:
            self.tearDown()

    def test_f_qmhosc(self):
        self.setUp()
        def assert_odd(n):
            En = n + 0.5
            f = makeup01.f_qmhosc([0., 1.], 0., En)
            assert_array_almost_equal(f, [1., 0])
        try:
            for n in self.n_values:
                yield assert_odd, n
        finally:
            self.tearDown()

    def test_ode_qmhosc_integral(self):
        self.setUp()
        def assert_even(n, value, ix=-1):
            y = makeup01.ode_qmhosc(self.x, self.y0[0], self.y0[1], n)
            psi = y[:ix, 0]
            norm = 0.5 * scipy.integrate.simps(psi**2, x=self.x[:ix])
            assert_almost_equal(norm, value, decimal=5)
        try:
            for n, value, ix in zip(self.n_values,
                                    (0.22155676341755839, 0.14770451311708355),
                                    (-150, -100)):
                yield assert_even, n, value, ix
        finally:
            self.tearDown()

