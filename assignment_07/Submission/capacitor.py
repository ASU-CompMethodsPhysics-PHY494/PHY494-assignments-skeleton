# Sekeleton Code for PHY494 HW07
# Copyright (c) Oliver Beckstein <obeckste@asu.edu>. All rights reserved.
# You may use it as a basis for your homework.

# Parallel plate capacitor in a box
#
#    two thin sheets of conducting materials at +100 V and -100 V
#    width 50, distance 20, box 100
#    box is grounded

import numpy as np

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def set_boundaries(Phi, w=50, d=20, voltage=100):
    # box (edges) always at 0 V

    ### NOTE: MODIFY Phi in place
    # Example:  y=0 (left) boundary of the box
    Phi[:, 0] = 0

    # plate 1 always at +100 V, plate 2 always -100V

    raise NotImplementedError

    return Phi


def calculate_phi_capacitor(Nmax=100, Max_iter=2000, tol=1e-2):
    """Calculate the electrostatic potential for the capacitor problem.

    The boundaries must be created in a function `set_boundaries(Phi)`.

    Arguments
    ---------
    Nmax : int
        square lattice size

    Max_iter : int
        maximum number of iterations

    tol : float
        The solver iterates until the Frobenius norm of the change in
        the potential between iterations falls below tol or `Max_iter`
        are exceeded.

    Returns
    -------
    Phi : (Nmax, Nmax) array
        potential on the lattice

    """

    # the code below has gaps and is incomplete
    raise NotImplementedError

    Phi = np.zeros((Nmax, Nmax), dtype=np.float64)

    set_boundaries(Phi)

    print("Starting...")
    for n_iter in range(Max_iter):
        if n_iter % 10 == 0:
            print("Iteration {0:5d}".format(n_iter), end="\r")

        # use this fast Laplace_Jacobi() function instead of the
        # Gauss-Seidel algorithm that we used in class (see comments
        # below...)
        Phi = Laplace_Jacobi(Phi)


    return Phi


#------------------------------------------------------------
# Code below this line is complete and does not have to be
# modified (unless you want to)
#------------------------------------------------------------

def Laplace_Gauss_Seidel(Phi):
    """One update in the Gauss-Seidel algorithm"""
    Nx, Ny = Phi.shape
    for xi in range(1, Nx-2):
        for yj in range(1, Ny-2):
            Phi[xi, yj] = 0.25*(Phi[xi+1, yj] + Phi[xi-1, yj]
                                + Phi[xi, yj+1] + Phi[xi, yj-1])
    return Phi

def Laplace_Jacobi(Phi):
    """One update in the Jacobi algorithm"""

    # Numpy array Jacobi is 100 times faster than Gauss-Seidel with
    # Python loops. Gauss-Seidel converges twice as fast as Jacobi so
    # the effective speed-up is still 50, so USE THIS ROUTINE!

    Phi[1:-1, 1:-1] = 0.25*(Phi[2:, 1:-1] + Phi[0:-2, 1:-1] + Phi[1:-1, 2:] + Phi[1:-1, 0:-2])
    return Phi


def plot_phi(Phi, figname="capacitor_potential_3d.pdf"):
    """Plot the potential `Phi`."""
    nx, ny = Phi.shape
    x = np.arange(nx)
    y = np.arange(ny)
    X, Y = np.meshgrid(x, y)
    Z = Phi[X, Y]
    offset = Phi.min() - 0.3*(Phi.max() - Phi.min())

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    surf = ax.plot_surface(X, Y, Z, cmap=plt.cm.coolwarm, rstride=2, cstride=2, alpha=0.3)
    cset = ax.contour(X, Y, Z, 20, zdir='z', offset=offset,
                      cmap=plt.cm.coolwarm)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel(r'potential $\Phi$ (V)')
    ax.set_zlim(offset, Phi.max())
    fig.colorbar(surf, shrink=0.5, aspect=5)

    if figname:
        fig.savefig(figname)
        print("Wrote 3D figure to {}".format(figname))

    return fig

def get_XYZ(Phi, x0=0, y0=0, dx=1, dy=1):
    """Convert Phi to X, Y, Z = Phi[X, Y] suitable for surface plotting."""
    nx, ny = Phi.shape
    x = np.arange(nx)
    y = np.arange(ny)
    X, Y = np.meshgrid(x, y)
    Z = Phi[X, Y]
    return x0 + X*dx, y0 + Y*dy, Z

def plot_panel(Phi, figname="capacitor_potential_2d.pdf"):
    """Plot a panel with 2d plots of initial potential and final solution Phi"""

    Phi0 = np.zeros_like(Phi)
    Phi0 = set_boundaries(Phi0)

    fig = plt.figure()

    ax1 = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)

    img = ax1.imshow(Phi0.T, cmap=plt.cm.coolwarm_r, interpolation="none", origin="lower")
    ax1.set_aspect(1)

    cont = ax2.contourf(*get_XYZ(Phi), 20, cmap=plt.cm.coolwarm_r)
    ax2.set_aspect(1)
    cb = ax2.figure.colorbar(img, shrink=0.6, ax=[ax1, ax2])
    cb.set_label(r"potential $\Phi$ (V)")

    ax1.set_xlabel("$x$")
    ax1.set_ylabel("$y$")
    ax2.set_xlabel("$x$")

    if figname:
        fig.savefig(figname)
        print("Wrote 2D figure to {}".format(figname))

    return fig
