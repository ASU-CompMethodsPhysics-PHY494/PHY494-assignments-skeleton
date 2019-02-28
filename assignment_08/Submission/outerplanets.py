# PHY 494 Homework 06 --- Orbit of Uranus
# Copyright (c) 2016 Oliver Beckstein
# Released under the BSD 3-clause license
#
# Skeleton Code for Students: You may use all of this code without any further
# attribution. You don't have to use any of it but it must be possible to run
# your code in the way described in the assignment.
#
# Incomplete functions contain the line
#
#   raise NotImplementedError
#
# when code is missing: remove this line and add code. Only one of these 'raise
# NotImplementedError' is added to a function, i.e., you might have to add more
# code than just one line.


import numpy as np


# gravitational constant in astronomical units
G_gravity = 4*np.pi**2

#============================================================
# Parameters of the problem
#------------------------------------------------------------
#
# store parameters in dict; use as e.g.
#  theta0['Uranus']
# to access initial angle of Uranus.

# angular position in 1690 in degrees
theta0 = {'Uranus': 205.640,
         'Neptune': 288.380,
}
# distance from the sun in AU
distance = {'Uranus': 19.1914,
            'Neptune': 30.0611,
}
# mass in AU
mass = {'Sun': 1.,
        'Uranus': 4.366244e-5,
        'Neptune': 5.151389e-5,
}
# orbital period in Earth years
period = {'Uranus': 84.0110,
          'Neptune': 164.7901,
}

#------------------------------------------------------------


def initial_position(angle, distance):
    """Calculate initial planet position.

    Parameters
    ----------
    angle : float
       initial angle relative to x axis (in degrees)
    distance : float
       initial distane from sun (in AU)

    Returns
    -------
    array
       position (x, y)
    """
    x = np.deg2rad(angle)
    return distance * np.array([np.cos(x), np.sin(x)])

def initial_velocity(angle, distance, period):
    raise NotImplementedError

def F_gravity(r, m, M):
    """Force due to gravity between two masses.

    Parameters
    ----------
    r : array
      distance vector (x, y)
    m, M : float
      masses of the two bodies

    Returns
    -------
    array
       force due to gravity (along r)
    """
    rr = np.sum(r*r)
    rhat = r/np.sqrt(rr)
    # replace NotImplemented with the correct force
    # expression (Eq 2)
    return NotImplemented


def omega(v, r):
    """Calculate angular velocity.

    The angular velocity is calculated as
    .. math::

          \omega = \frac{|\vec{v}|}{|\vec{r}|}

    Parameters
    ----------
    v : array
       velocity vectors for all N time steps; this
       should be a (N, dim) array
    r : array
       position vectors (N, dim) array

    Returns
    -------
    array
       angular velocity for each time step as 1D array of
       length N
    """
    speed = np.linalg.norm(v, axis=1)
    distance = np.linalg.norm(r, axis=1)
    return speed/distance

def integrate_orbits(dt=0.1, t_max=320, coupled=True):
    """Integrate equations of motions of Uranus and Neptune.

    Parameters
    ----------
    dt : float
       integrator timestep
    t_max : float
       integrate to t_max years
    coupled : bool
       * `True`: include the interaction between Neptune and Uranus
       * `False`: no interaction (Uranus and Neptune move independently)

    Returns
    -------
    time : array
       array with the times for each step (in years)
    r : array
       positions of the planets, shape (N, 2, 2), where::
          r[:, 0] = rU : Uranus x, y
          r[:, 1] = rN : Neptune x, y
    v : array
       velocities of the planets, shape (N, 2, 2), where::
          v[:, 0] = vU : Uranus vx, vy
          v[:, 1] - vN : Neptune vx, vy
    """
    nsteps = int(t_max/dt)
    time = dt * np.arange(nsteps)

    # shape = (step, planet, x/y)
    r = np.zeros((nsteps, 2, 2))
    v = np.zeros_like(r)

    r[0, 0, :] = initial_position(theta0['Uranus'], distance['Uranus'])
    r[0, 1, :] = initial_position(theta0['Neptune'], distance['Neptune'])

    raise NotImplementedError
    #v[0, 0, :] = ...
    #v[0, 1, :] = ...

    # ...

    return time, r, v

if __name__ == "__main__":
    # The following code only runs when the script is executed from the shell with
    #
    #    python ./outerplanets.py
    #
    # or inside a notebook with
    #
    #    %run ./outerplanets.py
    #
    # If you 'import outerplanets' then only the function definitions will be
    # executed, and *not* the following code.
    import matplotlib
    import matplotlib.pyplot as plt
    matplotlib.style.use("ggplot")


    print("Simulating Uranus and Neptune orbits WITHOUT interactions")
    time, r0, v0 = integrate_orbits(t_max=160, coupled=False)
    rU0 = r0[:, 0]
    vU0 = v0[:, 0]
    omegaU0 = omega(vU0, rU0)

    print("Simulating Uranus and Neptune orbits WITH interactions")
    time, r, v = integrate_orbits(t_max=160, coupled=True)
    rU = r[:, 0]
    rN = r[:, 1]
    vU = v[:, 0]
    omegaU = omega(vU, rU)

    #----------
    # IMPLEMENT
    #
    raise NotImplementedError
    DeltaOmegaU = None
    #
    #---------

    # plot orbits
    fig_orbits = "uranus_neptune_orbits.pdf"
    fig_anomaly = "uranus_anomaly.pdf"

    ax = plt.subplot(1,2,1)
    ax.plot(rU[:,0], rU[:, 1], label="Uranus")
    ax.plot(rN[:,0], rN[:, 1], label="Neptune")
    ax.plot(rU0[:,0], rU0[:,1], linestyle="--", label="Uranus (no Neptune)")
    ax.set_aspect(1)
    ax.set_xlabel(r"$x$ (AU)")
    ax.set_ylabel(r"$y$ (AU)")
    ax.legend(loc="upper right")
    ax.set_title("Uranus and Neptune orbits")

    ax = plt.subplot(1,2,2)
    ax.plot(time, DeltaOmegaU)
    ax.set_xlabel("years")
    ax.set_ylabel(r"Uranus anomaly $\Delta\omega_U$")
    ax.set_title("Uranus anomaly")
    ax.figure.tight_layout()
    ax.figure.savefig(fig_anomaly)
    print("Uranus anomaly plotted in {0}".format(fig_anomaly))


