# tests for HW08 solution

import numpy as np

from numpy.testing import (assert_array_almost_equal,
                           assert_array_equal,
                           assert_equal,
                           assert_almost_equal)

#----------------------------------------------------------------------
#
import capacitor
#
#----------------------------------------------------------------------

def test_run_long(Max_iter=10000, tol=1e-3):
    Phi = capacitor.calculate_phi_capacitor(Max_iter=Max_iter, tol=tol)
    assert_almost_equal(Phi.min(), -100)
    assert_almost_equal(Phi.max(), 100)
    assert_almost_equal(np.trace(Phi), 47.361932522707932, decimal=3)

def test_run_short(Max_iter=1000, tol=1):
    Phi = capacitor.calculate_phi_capacitor(Max_iter=Max_iter, tol=tol)
    assert_almost_equal(Phi.min(), -100)
    assert_almost_equal(Phi.max(), 100)
    assert_almost_equal(np.trace(Phi), 29.296772764719591, decimal=0)

class TestBoundaryConditions(object):
    def setUp(self):
        self.Nmax = 100
        self.Phi0 = np.zeros((self.Nmax, self.Nmax))
        self.Phi0 = capacitor.set_boundaries(self.Phi0)
        # correct values for the given problem
        self.plate_size = 50
        self.voltage = 100.

    def test_voltage(self):
        assert_almost_equal(self.Phi0.min(), -self.voltage)
        assert_almost_equal(self.Phi0.max(), self.voltage)

    def test_plate_size(self):
        plus_plate = self.Phi0 > 0
        minus_plate = self.Phi0 < 0
        assert_equal(np.sum(plus_plate), self.plate_size)
        assert_equal(np.sum(minus_plate), self.plate_size)

    def test_plus_plate_position(self):
        x, y = np.where(self.Phi0 > 0)
        assert_equal(x.min(), 25)
        assert_equal(y.min(), 40)
        assert_equal(x.max(), 74)
        assert_equal(y.max(), 40)

    def test_minus_plate_position(self):
        x, y = np.where(self.Phi0 < 0)
        assert_equal(x.min(), 25)
        assert_equal(y.min(), 60)
        assert_equal(x.max(), 74)
        assert_equal(y.max(), 60)

    def test_box_boundary(self):
        assert_array_equal(self.Phi0[:, 0], 0)
        assert_array_equal(self.Phi0[:, -1], 0)
        assert_array_equal(self.Phi0[0, :], 0)
        assert_array_equal(self.Phi0[-1, :], 0)

