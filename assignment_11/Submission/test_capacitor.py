# tests for HW 11 solution

import glob
import numpy as np

from numpy.testing import (assert_array_almost_equal,
                           assert_array_equal,
                           assert_equal,
                           assert_almost_equal)

import pytest

def test_import_module():
    try:
        import capacitor
    except ImportError:
        raise AssertionError("Cannot import capacitor.py module")

def test_import_function():
    try:
        from capacitor import calculate_phi_capacitor
    except ImportError:
        raise AssertionError("Cannot import the capacitor.calculate_phi_capacitor function")


@pytest.fixture(scope="module")
def phi_short(Max_iter=1000, tol=1):
    import capacitor
    Phi = capacitor.calculate_phi_capacitor(Max_iter=Max_iter, tol=tol)
    return Phi

class TestPhiShort(object):
    def test_shape(self, phi_short):
        Nx, Ny = phi_short.shape
        assert_equal(phi_short.shape, (100, 100))

    def test_min(self, phi_short):
        assert_almost_equal(phi_short.min(), -100)

    def test_max(self, phi_short):
        assert_almost_equal(phi_short.max(), 100)

    def test_diagonal_sum(self, phi_short):
        assert_almost_equal(np.trace(phi_short),
                            61.129276201665931, decimal=0)

    def test_half_sum(self, phi_short):
        Nx, Ny = phi_short.shape
        assert_almost_equal(phi_short[:Nx//2, :].sum(),
                            542.60037474563251, decimal=0)


@pytest.fixture(scope="module")
def phi_long(Max_iter=10000, tol=1e-3):
    import capacitor
    Phi = capacitor.calculate_phi_capacitor(Max_iter=Max_iter, tol=tol)
    return Phi

class TestPhiLong(object):
    def test_shape(self, phi_long):
        Nx, Ny = phi_long.shape
        assert_equal(phi_long.shape, (100, 100))

    def test_min(self, phi_long):
        assert_almost_equal(phi_long.min(), -100)

    def test_max(self, phi_long):
        assert_almost_equal(phi_long.max(), 100)

    def test_diagonal_sum(self, phi_long):
        assert_almost_equal(np.trace(phi_long),
                            72.637059850488143, decimal=3)

    def test_half_sum(self, phi_long):
        Nx, Ny = phi_long.shape
        assert_almost_equal(phi_long[:Nx//2, :].sum(),
                            1127.5308751853702, decimal=3)

@pytest.fixture(scope="class")
def Phi0(Nmax=100):
    import capacitor

    _Phi0 = np.zeros((Nmax, Nmax))
    _Phi0 = capacitor.set_boundaries(_Phi0)
    return _Phi0

class TestBoundaryConditions(object):
    # correct values for the given problem
    plate_size = 50
    voltage = 100.

    def test_voltage(self, Phi0):
        assert_almost_equal(Phi0.min(), -self.voltage)
        assert_almost_equal(Phi0.max(), self.voltage)

    def test_plate_size(self, Phi0):
        plus_plate = Phi0 > 0
        minus_plate = Phi0 < 0
        assert_equal(np.sum(plus_plate), self.plate_size)
        assert_equal(np.sum(minus_plate), self.plate_size)

    def test_plus_plate_position(self, Phi0):
        x, y = np.where(Phi0 > 0)
        assert_equal(x.min(), 25)
        assert_equal(y.min(), 40)
        assert_equal(x.max(), 74)
        assert_equal(y.max(), 40)

    def test_minus_plate_position(self, Phi0):
        x, y = np.where(Phi0 < 0)
        assert_equal(x.min(), 25)
        assert_equal(y.min(), 60)
        assert_equal(x.max(), 74)
        assert_equal(y.max(), 60)

    def test_box_boundary(self, Phi0):
        assert_array_equal(Phi0[:, 0], 0)
        assert_array_equal(Phi0[:, -1], 0)
        assert_array_equal(Phi0[0, :], 0)
        assert_array_equal(Phi0[-1, :], 0)




@pytest.mark.parametrize('filename',
                         ('iterations.txt',
                          'capacitor_potential_2d.*',
                          'capacitor_potential_3d.*')
                         )
def test_output_file_exists(filename):
    filenames = glob.glob(filename)
    assert len(filenames) >= 1, "File {} is missing".format(filename)
