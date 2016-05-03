# ASU PHY494 Makeup02
#
# Copyright (c) 2016 Oliver Beckstein
# All rights reserved.
#
# You may use this code as basis for your assignment and distribute it
# freely.

import numpy as np
import scipy.linalg

def extract_tridiag_ab(A):
    """extract diagonals from matrix A and pad (as required for solve_banded())"""

    ud = np.insert(np.diag(A, 1), 0, 0)         # upper diagonal
    d = np.diag(A)                              # main diagonal
    ld = np.insert(np.diag(A, -1), len(d)-1, 0) # lower diagonal
    # matrix as required by solve_banded()
    return np.array([ud, d, ld])

# material parameters
# http://www.engineeringtoolbox.com/thermal-conductivity-d_429.html
# http://www.engineeringtoolbox.com/specific-heat-solids-d_154.html
# http://www.engineeringtoolbox.com/density-solids-d_1265.html

# material   Kappa (W/(mK))   C (J/(kg K)   rho
# ----------------------------------------------------
# brick        1.0            0.9e3          2e3
# aluminum   205              0.87e3         2.7e3

def T_diurnal(t, Tmin, Tmax, t_max=12*3600):
    """Estimate the temperature at t seconds since midnight.

    The diurnal temperature cycle is modelled with a simple sine
    function, with the maximum at t_max (12pm noon) by default and assuming
    a 12/12h cycle.

    Arguments
    ---------

    t : float
        time in seconds since midnight
    Tmin : float
        minimum daily temperature
    Tmax : float
        maximum daily temperature
    t_max : float, optional
        time of the maximum in the cycle

    Returns
    -------
    temperature : float
        temperature in K
    """
    raise NotImplementedError


def CrankNicholson_T(L=0.3, t_max=3*24*3600, Dx=0.02, Dt=60,
                     step=30, verbose=True,
                     Kappa=1.0, CHeat=0.9e3, rho=2e3,
                     Tin=293, Tmin=301.4, Tmax=314.1):
    """Solve the 1d heat equation for a daily oscillating temperature variation.

    The left end of the material is oscillating (see
    :func:`T_diurnal`), the right end is held constant at `Tin`.

    The heat equation is solved with the Crank-Nicholson algorithm so
    any combinations of `Dx` and `Dt` can be used.

    Some Arguments
    --------------
    Tin : float
        constant T at right end
    Tmin, Tmax : float
        min and max T in the diurnal temperature cycle

    """
    Nx = int(L // Dx)
    Nt = int(t_max // Dt)

    eta = Kappa * Dt / (CHeat * rho * Dx**2)

    if verbose:
        print("Nx = {0}, Nt = {1}".format(Nx, Nt))
        print("eta = {0}".format(eta))

    T = np.zeros(Nx)
    T_plot = np.zeros((int(np.ceil(Nt/step)) + 1, Nx))

    # initial conditions
    raise NotImplementedError
    # boundary conditions
    raise NotImplementedError

    #---------------------
    # M_eta * T[1:-1, j+1] = bT
    # M_eta * xT = bT
    # Nx-2 x Nx-2 matrix: tridiagonal
    NM = Nx - 2
    alpha = 2/eta + 2
    beta = 2/eta - 2
    M_eta = np.diagflat(-np.ones(NM-1), 1) \
            + np.diagflat(alpha * np.ones(NM), 0) \
            + np.diagflat(-np.ones(NM-1), -1)
    M_eta_ab = extract_tridiag_ab(M_eta)
    bT = np.zeros(NM)

    t_index = 0
    T_plot[t_index, :] = T
    for jt in range(1, Nt):
        raise NotImplementedError

        # Crank-Nicholson with fast banded matrix solver
        # set up RHS
        bT[:] = T[:-2] + beta*T[1:-1] + T[2:]
        # boundaries are special cases
        bT[0] += T[0]  #  + T[0,j+1]
        bT[-1] += T[-1] #  + T[-1,j+1]

        # solve implicit problem
        T[1:-1] = scipy.linalg.solve_banded((1, 1), M_eta_ab, bT)
        #T[1:-1] = np.linalg.solve(M_eta, bT)

        if jt % step == 0 or jt == Nt-1:
            t_index += 1
            T_plot[t_index, :] = T
            if verbose:
                print("Iteration {0:5d}".format(jt), end="\r")
    else:
        if verbose:
            print("Completed {0:5d} iterations: t={1} s".format(jt, jt*Dt))

    parameters = (Dx, Dt, step)
    return T_plot, parameters


def plot_wireframe(T_plot, Dx, Dt, step):
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D

    X, Y = np.meshgrid(range(T_plot.shape[0]), range(T_plot.shape[1]))
    Z = T_plot[X, Y]
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.plot_wireframe(X*Dt*step/3600, Y*Dx, Z)
    ax.set_xlabel(r"time $t$ (h)")
    ax.set_ylabel(r"position $x$ (m)")
    ax.set_zlabel(r"temperature $T$ (K)")
    fig.tight_layout()
    return ax

def plot_surface(T_plot, Dx, Dt, step,
                 figname="heatequation_3d.pdf",
                 rstride=2, cstride=2):
    """Plot the T values."""

    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D

    X, Y = np.meshgrid(range(T_plot.shape[0]), range(T_plot.shape[1]))
    Z = T_plot[X, Y]

    offset = T_plot.min() - 0.3*(T_plot.max() - T_plot.min())

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    surf = ax.plot_surface(X*Dt*step/3600, Y*Dx, Z, cmap=plt.cm.coolwarm,
                           rstride=rstride, cstride=cstride,
                           alpha=0.3)
    cset = ax.contour(X*Dt*step/3600, Y*Dx, Z, 20, zdir='z', offset=offset,
                      cmap=plt.cm.coolwarm)
    ax.set_xlabel(r"time $t$ (h)")
    ax.set_ylabel(r"position $x$ (m)")
    ax.set_zlabel(r"temperature $T$ (K)")
    ax.set_zlim(offset, T_plot.max())
    fig.colorbar(surf, shrink=0.5, aspect=5)

    if figname:
        fig.savefig(figname)
        print("Wrote 3D figure to {}".format(figname))

    return ax
