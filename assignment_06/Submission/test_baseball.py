# test HW 06 solution

import numpy as np

import pytest
from numpy.testing import assert_array_almost_equal

def test_import_module():
    try:
        import hw06
    except ImportError:
        raise AssertionError("Cannot import hw06.py module")

def test_import_function():
    try:
        from hw06 import simulate_baseball
    except ImportError:
        raise AssertionError("Cannot import the hw06.simulate_baseball function")

def run_simulation(omega):
    # run with fixed parameters except omega
    from hw06 import simulate_baseball

    v0 = np.array([30, 0])
    r0 = np.array([0, 2])
    return simulate_baseball(v0, omega, r0,
                             h=0.01, C_D=0.40, g=9.81, rho=1.225,
                             r=0.07468/2, m=0.14883,
                             R_homeplate=18.4)

@pytest.mark.parametrize("omega,final", [
    (0.001*np.array([0,0,1]), np.array([  0.61    ,  17.185799,   0.248502,   0.      ])),
    (200.*np.array([0,0,1]),  np.array([  0.65    ,  18.275451,   0.741821,   0.      ])),
    (200.*np.array([0,1,1]),  np.array([  0.65    ,  18.258024,   0.669868,  -0.653914])),
    ])
def test_simulation_position(omega, final):
    r = run_simulation(omega)
    assert_array_almost_equal(r[-1], final, decimal=3,
                              err_msg="final position for omega={} does not match".format(
                                  omega))

