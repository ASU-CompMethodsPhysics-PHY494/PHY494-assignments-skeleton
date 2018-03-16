# PHY 494 Homework 07 --- Baseball Physics
# Copyright (c) 2018 Oliver Beckstein
# Released under the BSD 3-clause license
#
# Skeleton Code for Students: You may use all of this code without any further
# attribution. You don't have to use any of it but it must be possible to run
# your code in the way described in the assignment.
#
#
# See also https://github.com/ASU-CompMethodsPhysics-PHY494/PHY494-resources/blob/master/11_ODE_applications/baseball_solution.ipynb


import numpy as np

import ode

def C_L(S):
    return 0.62 * S**0.7

def simulate_baseball(v0, omega, r0=None,
                      h=0.01, C_D=0.40, g=9.81, rho=1.225,
                      r=0.07468/2, m=0.14883,
                      R_homeplate=18.4):
    """simulate baseball pitch

    Parameters
    ----------
    v0 : array
         initial velocity (vx, vy) in m/s
    omega : array
         angular velocity vector of the ball ("spin"), in rad/s
    r0 : array, optional
         initial position of the ball (in m) when it leaves the pitcher's hand
         as (x, y); the default is (0, 2)
    h : float, optional
         integration time step in s, default is 0.01 s
    C_D : float, optional
         drag coefficient, default is 0.40
    g : float, optional
         acceleration due to gravity, default 9.81 kg/(m*s^2)
    rho : float, optional
         density of air, default 1.225 kg/m^3
    r : float, optional
         radius of the baseball
    m : float, optional
         mass of the baseball
    R_homeplate : float, optional
         distance of the catcher from the pitcher

    Returns
    -------

    positions : array
         The array contains an entry (time, x, y, z) for each time step.
    """
    # all SI units (kg, m)
    if r0 is None:
        r0 = np.array([0, 2])  # pitching at 2m height

    omega = np.asarray(omega)

    domega = np.linalg.norm(omega)
    A = np.pi*r**2
    rhoArm = rho * A * r / m
    b2 = 0.5 * C_D * rho * A

    a_gravity = np.array([0, -g, 0])

    def f(t, y):
        # y = [x, y, z, vx, vy, vz]
        v = y[3:]
        dv = np.linalg.norm(v)
        S = r*domega/dv
        a_magnus = 0.5 * C_L(S) * rhoArm / S * np.cross(omega, v)
        a_drag = -b2/m * dv * v
        a = a_gravity + a_drag + a_magnus
        return np.array([y[3], y[4], y[5],
                         a[0], a[1], a[2]])

    x0, y0 = r0
    vx, vy = v0
    t = 0
    positions = []
    # initialize 3D!
    y = np.array([x0, y0, 0, vx, vy, 0], dtype=np.float64)

    while y[0] < R_homeplate and y[1] >= 0.2:
        positions.append([t, y[0], y[1], y[2]])  # record t, x and y, z
        y[:] = ode.rk4(y, f, t, h)
        t += h

    return np.array(positions)


# add your code here; you can copy and paste and modify
# simulate_baseball() from above

def simulate_baseball_advanced(v0, omega, r0=None,
                               h=0.01, C_D=0.40, g=9.81, rho=1.225,
                               r=0.07468/2, m=0.14883,
                               R_homeplate=18.4):
    pass  # you can remove this line once you add your own code; it does nothing
