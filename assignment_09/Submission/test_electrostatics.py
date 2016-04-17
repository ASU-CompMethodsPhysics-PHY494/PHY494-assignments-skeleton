# tests for HW08 solution

import numpy as np

from numpy.testing import (assert_array_almost_equal,
                           assert_array_equal,
                           assert_equal,
                           assert_almost_equal)

#----------------------------------------------------------------------
#
import electrostatics
#
#----------------------------------------------------------------------

NMAX = 140
TOL = 1e-6

def test_run_long(Nmax=NMAX, Max_iter=30000, tol=TOL):
    Phi = electrostatics.calculate_potential(
        Nmax=Nmax, Max_iter=Max_iter, tol=tol)
    assert_almost_equal(Phi.min(), -100)
    assert_almost_equal(Phi.max(), 100)
    assert_almost_equal(np.trace(Phi), 1211.2044887186539,
                        decimal=5)

def test_run_short(Nmax=NMAX, Max_iter=1000, tol=1):
    Phi = electrostatics.calculate_potential(
        Nmax=Nmax, Max_iter=Max_iter, tol=tol)
    assert_almost_equal(Phi.min(), -100)
    assert_almost_equal(Phi.max(), 100)
    assert_almost_equal(np.trace(Phi), 1141.5704932189408,
                        decimal=0)

class TestBoundaryConditions(object):
    def setUp(self, Nmax=NMAX):
        self.Nmax = Nmax
        self.Phi0 = np.zeros((self.Nmax, self.Nmax))
        self.Phi0 = electrostatics.set_boundaries(self.Phi0)
        # correct values for the given problem
        self.voltage = 100.

    def test_voltage(self):
        assert_almost_equal(self.Phi0.min(), -self.voltage)
        assert_almost_equal(self.Phi0.max(), self.voltage)

    def test_plate_size(self):
        plus_plate = self.Phi0 > 0
        minus_plate = self.Phi0 < 0
        assert_equal(np.sum(plus_plate), 500)
        assert_equal(np.sum(minus_plate), 300)

    def test_plus_plate_position(self):
        x, y = np.where(self.Phi0 > 0)
        assert_equal(x.min(), 45)
        assert_equal(y.min(), 55)
        assert_equal(x.max(), 94)
        assert_equal(y.max(), 64)

    def test_minus_plate_position(self):
        x, y = np.where(self.Phi0 < 0)
        assert_equal(x.min(), 45)
        assert_equal(y.min(), 75)
        assert_equal(x.max(), 94)
        assert_equal(y.max(), 84)

    def test_box_boundary(self):
        assert_array_equal(self.Phi0[:, 0], 0)
        assert_array_equal(self.Phi0[:, -1], 0)
        assert_array_equal(self.Phi0[0, :], 0)
        assert_array_equal(self.Phi0[-1, :], 0)

    def test_hole(self):
        assert_equal(np.sum(self.Phi0[55:85, :] != 0), 400)
        assert_equal(np.sum(self.Phi0[65:75, 70:] != 0), 0)        

class TestChargedensity(object):
    def setUp(self, Nmax=NMAX, Max_iter=30000, tol=TOL):
        self.Phi = electrostatics.calculate_potential(
            Nmax=Nmax, Max_iter=Max_iter, tol=tol)
        self.Delta = 1.0
        
    def test_chargedensity(self):
        rho = electrostatics.calculate_chargedensity(self.Phi, Delta=self.Delta)
        assert_almost_equal(rho.sum(), 3.8189203316939451, decimal=5)
        assert_almost_equal(rho.max(), 11.448452396998144, decimal=5)
        assert_almost_equal(rho.min(), -12.775747943406886, decimal=5)        
        
    
