# PHY 494 Homework 06 --- Baseball Physics
# Copyright (c) 2016 Oliver Beckstein
# Released under the BSD 3-clause license
#
# Skeleton Code for Students: You may use all of this code without any further
# attribution. You don't have to use any of it but it must be possible to run
# your code in the way described in the assignment.
#
# Incomplete functions contain comments that indicate that you need to complete
# them. They may also contain the line
#
#   raise NotImplementedError
#
# when code is missing: remove this line and add code. Only one of these 'raise
# NotImplementedError' is added to a function, i.e., you might have to add more
# code than just one line.



import numpy as np

def C_L(S):
    return 0.62 * S**0.7

def simulate_baseball(v0, omega, r0,
                      h=0.01, C_D=0.40, g=9.81, rho=1.225,
                      r=0.07468/2, m=0.14883, R_homeplate=18.4):

    # make sure that omega is a numpy array
    omega = np.asarray(omega)

    # all SI units (kg, m)
    # air density rho in kg/m^3

    domega = np.linalg.norm(omega)
    A = np.pi*r**2
    rhoArm = rho * A * r / m

    # internally, use 3d coordinates [x,y,z];
    # y = [x, y, z, vx, vy, vz]

    a_gravity = np.array([0, -g, 0])

    def f(t, y):
        # y = [x, y, z, vx, vy, vz]
        v = y[3:]
        dv = np.linalg.norm(v)
        # COMPLETE
        # 1. acceleration due to drag
        # 2. acceleration due to Magnus effect
        # 3. acceleration due to gravity (a_gravity)

        # need to return array f of length 6!
        raise NotImplementedError

    x0, y0 = r0
    vx, vy = v0
    t = 0
    positions = []
    # initialize 3D!
    y = np.array([x0, y0, 0, vx, vy, 0], dtype=np.float64)


    # IMPLEMENT integration loop
    # - use ode.rk4()
    # - stop when x >= R_homeplate or y < 0.2 (i.e. cannot be caught)

    return np.array(positions)
