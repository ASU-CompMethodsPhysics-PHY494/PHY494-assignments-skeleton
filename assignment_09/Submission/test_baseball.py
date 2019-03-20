# test basic baseball simulation code in HW07
#
# NOTE: There are no tests for the advanced physics (problem 7.1).
#       This test only helps you to ensure that there are no mistakes
#       in the basic code.

import numpy as np

import importlib
import pytest
from numpy.testing import assert_array_almost_equal, assert_almost_equal



@pytest.fixture
def solution(name="hw09"):
    try:
        mod = importlib.import_module(name)
    except ImportError:
        raise AssertionError("Cannot import {} module".format(name))
    return mod

def test_import_module(solution):
    return True  # unless solution fixture fails


@pytest.mark.parametrize('function', ['simulate_baseball',
                                      'simulate_baseball_advanced',
                                      'C_D', 'omega_friction',
                                      ])
def test_import_function(function, solution):
    errmsg = "Module {0} does not have the '{1}()' function".format(
            solution.__name__, function)
    try:
        func = getattr(solution, function)
    except AttributeError:
        raise AssertionError(errmsg)
    if type(func) != type(lambda : None):
        raise AssertionError(errmsg)

class TestSimpleSimulation:
    def run_simulation(self, omega, func):
        # run with fixed parameters except omega

        v0 = np.array([30, 0, 0])
        r0 = np.array([0, 2, 0])
        return func(v0, omega, r0=r0,
                    h=0.01, g=9.81, rho=1.225,
                    r=0.07468/2, m=0.14883,
                    R_homeplate=18.4)

    @pytest.mark.parametrize("omega,final", [
        (0.001*np.array([0,0,1]), np.array([  0.61, 17.450345, 0.191753, 0.])),
        (200.*np.array([0,0,1]),  np.array([  0.65, 18.539559, 0.703006, 0.])),
        (200.*2**(-0.5)*np.array([0,1,1]),
         np.array([  0.65, 18.523035, 0.484009, -0.528245])),
    ])
    def test_simulation_position(self, omega, final, solution):
        r = self.run_simulation(omega, solution.simulate_baseball)
        assert_array_almost_equal(r[-1], final, decimal=3,
                                  err_msg="final position for omega={} does not match".format(
                                      omega))


class TestAdvancedSimulation(TestSimpleSimulation):
    @pytest.mark.parametrize("omega,final", [
        (0.001*np.array([0,0,1]), np.array([  0.61    ,  17.415078,   0.197944,   0.      ])),
        (200.*np.array([0,0,1]),  np.array([  0.65    ,  18.489508,   0.68564 ,   0.      ])),
        (200.*2**(-0.5)*np.array([0,1,1]),
         np.array([  0.65    ,  18.474653,   0.474119,  -0.510158])),
    ])
    def test_simulation_position(self, omega, final, solution):
        r = self.run_simulation(omega, solution.simulate_baseball_advanced)
        assert_array_almost_equal(r[-1], final, decimal=6,
                                  err_msg="final position for omega={} does not match".format(
                                      omega))

    @pytest.mark.parametrize("v,CD",
                             list(zip([   0.  ,   10.5 ,   30.  ,   33.9 ,   34.  ,   34.1 ,   45.  ,
                                          66.66,  100.  ],
                                      [ 0.49997152,  0.49960787,  0.36302075,  0.16104365,  0.16      ,
                                             0.15916723,  0.32764823,  0.36003979,  0.36000001])))
    def test_CD(self, v, CD, solution):
        assert_almost_equal(solution.C_D(v), CD, decimal=6)

    @pytest.mark.parametrize("omega0", [[0, 0, 1], [1, 0, 1], [-1, 3, -0.1]])
    @pytest.mark.parametrize("t", 10 * np.random.random(size=5))
    def test_omega_friction(self, omega0, t, solution):
        omega0 = np.asarray(omega0)
        assert_array_almost_equal(solution.omega_friction(omega0, t),
                                  omega0 * np.exp(-t/5), decimal=6)

