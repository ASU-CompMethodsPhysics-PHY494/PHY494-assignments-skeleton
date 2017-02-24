# test HW 05 solution

import numpy as np

from numpy.testing import (assert_array_almost_equal, assert_equal,
                           )

from outerplanets import integrate_orbits

try:
    from outerplanets import omega
except ImportError:
    def omega(v, r):
        speed = np.linalg.norm(v, axis=1)
        distance = np.linalg.norm(r, axis=1)
        return speed/distance

def test_import_module():
    try:
        import outerplanets
    except ImportError:
        raise AssertionError("Cannot import outerplanets.py module")

def test_import_function():
    try:
        from outerplanets import integrate_orbits
    except ImportError:
        raise AssertionError("Cannot import the outerplanets.integrate_orbits function")

def test_DeltaOmega(t_max=160):
    time, r0, v0 = integrate_orbits(t_max=t_max, coupled=False)
    time, r, v = integrate_orbits(t_max=160, coupled=True)
    DeltaOmegaU = omega(v0[:, 0], r0[:, 0]) - omega(v[:, 0], r[:, 0])
    result = [DeltaOmegaU.min(), DeltaOmegaU.max()]
    assert_array_almost_equal(result,
                              [-1.0492366485e-05, 7.84639028908e-05],
                              err_msg="DeltaOmega incorrect")

def test_neptune_initial_conditions(t_max=10, dt=0.01):
    time, r, v = integrate_orbits(t_max=t_max, dt=dt)
    assert_equal(len(r), int(t_max/dt))
    assert_array_almost_equal(r[0, 1], np.array([  9.47879984, -28.52756714]),
                              err_msg="Neptune initial position wrong")
    assert_array_almost_equal(v[0, 1], np.array([-1.08771092, -0.36141161]),
                              err_msg="Neptune initinal velocity wrong")

def test_uranus_initial_conditions(t_max=10, dt=0.01):
    time, r, v = integrate_orbits(t_max=t_max, dt=dt)
    assert_equal(len(r), int(t_max/dt))
    assert_array_almost_equal(r[0, 0], np.array([-17.30163539,  -8.30441128]),
                              err_msg="Uranus initial position wrong")
    assert_array_almost_equal(v[0, 0], np.array([-0.62108718,  1.29398985]),
                              err_msg="Uranus initinal velocity wrong")
