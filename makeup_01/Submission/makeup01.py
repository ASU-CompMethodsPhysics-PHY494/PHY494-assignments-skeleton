# Skeleton code for ASU PHY494 Makeup01
#
# Copyright (c) 2016 Oliver Beckstein
# All rights reserved.
#


import numpy as np
import scipy.integrate

def factorial(n):
    """Compute the factorial n!"""
    raise NotImplementedError
    return factorial

# def initial_values_qmhosc(n):
#     """Return physically correct initial values at x=0 for QM SHOSC.
#
#     Convention: always choose the positive values for psi(0) and psi'(0).
#
#     Arguments
#     ---------
#     n : int
#         energy level (0, 1, 2, ...)
#
#     Returns
#     -------
#     y :  array
#         initial values [psi(0), psi'(0)]
#     """



def f_qmhosc(y, t, E):
    """Standard form derivative vector dy/dt = f

    Equation to be solved:

       -1/2 u'' + 1/2 x^2 u = E u

    """
    raise NotImplementedError

def ode_qmhosc(x, y0_0, y1_0, n=0):
    """Solve -1/2 u'' + 1/2 x^2 u = E u.

    Initial conditions (at x0 = x[0]):

      y0_0: value u(x0)
      y1_0: derivative du/dx at x0
    """
    raise NotImplementedError

    y = scipy.integrate.odeint( )
    return y




