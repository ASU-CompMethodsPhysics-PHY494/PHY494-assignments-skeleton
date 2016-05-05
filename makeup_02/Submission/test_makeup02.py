# tests for makeup02

import os.path
import numpy as np

from numpy.testing import (assert_array_almost_equal, assert_equal,
                           assert_array_equal,
                           assert_almost_equal,
                           assert_,
                           )

import makeup02


Tin = 293
Tmin = 301.4
Tmax = 314.1
t_max = 12*3600

class TestTdiurnal(object):
    def setUp(self):
        t = np.linspace(0, 1.5*24*60*60, 100000)
        self.Temp = makeup02.T_diurnal(t, Tmin, Tmax, t_max=t_max)
        self.Tmean = 0.5*(Tmin + Tmax)

    def test_minmax(self):
        assert_array_almost_equal(self.Temp[[0, -1]], [Tmin, Tmax])

    def test_zeros(self):
        n_zeros = (np.abs(self.Temp - self.Tmean) < 3*1e-4).sum()
        assert_equal(n_zeros, 6)  # not reall number, just test

class TestCrankNicholson_T(object):
    def setUp(self):
        self.Dx = 0.005
        self.Dt = 30
        self.step = 30
        self.t_max = 3*24*3600
        self.Tmin = 301.4
        self.Tmax = 314.1
        self.Tin = 293
        self.length = 0.3
        self.figname = "heatequation_3d.pdf"
        self.T_plot, self.parameters = self.CrankNicholson_T()

    def CrankNicholson_T(self):
        return makeup02.CrankNicholson_T(
            Dx=self.Dx, Dt=self.Dt, step=self.step,
            Tin=self.Tin, Tmin=self.Tmin, Tmax=self.Tmax,
            L=self.length, t_max=self.t_max,
            Kappa=1.0, CHeat=0.9e3, rho=2e3)

    def test_parameters(self):
        assert_array_almost_equal(self.parameters, (0.005, 30, 30))

    def test_initial_conditions_as_implemented(self):
        T = np.empty_like(self.T_plot[0])
        T[1:-1] = Tin
        T[0] = makeup02.T_diurnal(0, Tmin, Tmax)
        T[-1] = Tin
        assert_array_almost_equal(self.T_plot[0], T)

    def test_initial_conditions_as_in_PDF(self):
        T = np.empty_like(self.T_plot[0])
        T[:] = Tmin
        if np.allclose(self.T_plot[0], T):
            import textwrap
            raise AssertionError(textwrap.fill(
                "In principle you implemented the correct initial conditions "
                "as required in the PDF. However, the tests were written for "
                "slightly different initial conditions: see issue #5"
                "https://github.com/ASU-CompMethodsPhysics-PHY494/PHY494-assignments-skeleton/issues/5."
                "Please implement the alternative initial conditions as provided in the "
                "link above."))

    def test_left_boundary(self):
        Nt = int(self.t_max // self.Dt)
        t = np.array([
            jt*self.Dt for jt in range(Nt)
                if jt % self.step == 0 or jt == Nt-1])
        T_outside = makeup02.T_diurnal(t, self.Tmin, self.Tmax)
        assert_equal(self.T_plot.shape[0], T_outside.shape[0])
        assert_array_almost_equal(self.T_plot[:, 0], T_outside)

    def test_right_boundary(self):
        assert_almost_equal(self.T_plot[:, -1], Tin)

    def test_lattice_size(self):
        assert_array_equal(self.T_plot.shape, (289, 59))

    def test_solution(self):
        assert_almost_equal(self.T_plot.sum(), 5116599.9475197177,
                            decimal=4)

    def test_figure_pdf(self):
        try:
            if not os.path.exists(self.figname):
                # generate plot on the fly for convenience
                makeup02.plot_surface(self.T_plot,
                                      *self.parameters, figname=self.figname)
        except:
            pass
        assert_(os.path.exists(self.figname),
                "Figure {} is missing.".format(self.figname))


class TestCrankNicholson_T_2(TestCrankNicholson_T):
    # Better test where step and Dt are not the same number (catches
    # cases where step was used instead of Dt)
    # NOTE: These tests were added AFTER the submission deadline to
    #       aid in grading.
    def setUp(self):
        self.Dx = 0.005
        self.Dt = 100
        self.step = 30
        self.t_max = 3*24*3600
        self.Tmin = 301.4
        self.Tmax = 314.1
        self.Tin = 293
        self.length = 0.3
        self.figname = "heatequation_3d.pdf"
        self.T_plot, self.parameters = self.CrankNicholson_T()

    def test_parameters(self):
        assert_array_almost_equal(self.parameters, (0.005, 100, 30))

    def test_lattice_size(self):
        assert_array_equal(self.T_plot.shape, (88, 59))

    def test_solution(self):
        assert_almost_equal(self.T_plot.sum(), 1557760.8276307792,
                            decimal=4)
