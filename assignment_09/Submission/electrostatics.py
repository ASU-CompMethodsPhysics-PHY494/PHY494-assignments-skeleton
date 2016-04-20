# Skeleton code for PHY494 HW09
# Copyright (c) Oliver Beckstein <obeckste@asu.edu>. All rights reserved.
# You may use it as a basis for your homework.


import numpy as np

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def set_boundaries(Phi, w=50, d=10, b=10, r=10, voltage=100, verbose=False):
    raise NotImplementedError

    return Phi


def calculate_potential(Nmax=140, Max_iter=30000, tol=1e-6):
    """Calculate the electrostatic potential for the electrostatics problem.

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

    raise NotImplementedError

    return Phi

def calculate_chargedensity(Phi, Delta=1.0):
    """Calculate the charge density from Poisson's equation."""
    raise NotImplementedError


def Laplace_Gauss_Seidel_odd_even(Phi):
    """One update in the Gauss-Seidel algorithm on odd or even fields"""
    # odd update (uses old even)
    Phi[1:-2:2, 1:-2:2] = 0.25*(Phi[2::2, 1:-2:2] + Phi[0:-2:2, 1:-2:2] + Phi[1:-2:2, 2::2] + Phi[1:-2:2, 0:-2:2])
    Phi[2:-1:2, 2:-1:2] = 0.25*(Phi[3::2, 2:-1:2] + Phi[1:-2:2, 2:-1:2] + Phi[2:-1:2, 3::2] + Phi[2:-1:2, 1:-2:2])

    # even update (uses new odd)
    Phi[1:-2:2, 2:-1:2] = 0.25*(Phi[2::2, 2:-1:2] + Phi[0:-2:2, 2:-1:2] + Phi[1:-2:2, 3::2] + Phi[1:-2:2, 1:-1:2])
    Phi[2:-1:2, 1:-2:2] = 0.25*(Phi[3::2, 1:-2:2] + Phi[1:-2:2, 1:-2:2] + Phi[2:-1:2, 2::2] + Phi[2:-1:2, 0:-2:2])
    return Phi


def plot_phi(Phi, figname="electrostatics_potential_3d.pdf",
             rstride=2, cstride=2):
    """Plot the potential `Phi`."""
    nx, ny = Phi.shape
    x = np.arange(nx)
    y = np.arange(ny)
    X, Y = np.meshgrid(x, y)
    Z = Phi[X, Y]
    offset = Phi.min() - 0.3*(Phi.max() - Phi.min())

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    surf = ax.plot_surface(X, Y, Z, cmap=plt.cm.coolwarm,
                           rstride=rstride, cstride=cstride,
                           alpha=0.3)
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

def plot_panel(Phi, figname="electrostatics_potential_2d.pdf"):
    """Plot a panel with 2d plots of initial potential and final solution Phi"""

    Phi0 = np.zeros_like(Phi)
    Phi0 = set_boundaries(Phi0)

    fig = plt.figure()

    ax1 = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)

    img = ax1.imshow(Phi0.T, cmap=plt.cm.coolwarm,
                     interpolation="none", origin="lower")
    ax1.set_aspect(1)

    cont = ax2.contourf(*get_XYZ(Phi), 20, cmap=plt.cm.coolwarm)
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


def plot_contour(Phi, filename=None):
    """Plot Phi as a contour plot.

    Arguments
    ---------
    Phi : 2D array
          potential on lattice
    filename : string or None, optional (default: None)
          If `None` then show the figure and return the axes object.
          If a string is given (like "contour.png") it will only plot
          to the filename and close the figure but return the filename.
    """
    fig = plt.figure(figsize=(5,4))
    ax = fig.add_subplot(111)

    x = np.arange(Phi.shape[0])
    y = np.arange(Phi.shape[1])
    X, Y = np.meshgrid(x, y)
    Z = Phi[X, Y]
    cset = ax.contourf(X, Y, Z, 20, cmap=plt.cm.coolwarm)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_aspect(1)

    cb = fig.colorbar(cset, shrink=0.5, aspect=5)
    cb.set_label(r"potential $\Phi$ (V)")

    if filename:
        fig.savefig(filename)
        plt.close(fig)
        return filename
    else:
        return ax


def plot_surf(Phi, filename=None, offset=-20, zlabel=r'potential $\Phi$ (V)',
              elevation=40, azimuth=20,
              rstride=2, cstride=2):
    """Plot Phi as a 3D plot with contour plot underneath.

    Arguments
    ---------
    Phi : 2D array
          potential on lattice
    filename : string or None, optional (default: None)
          If `None` then show the figure and return the axes object.
          If a string is given (like "contour.png") it will only plot
          to the filename and close the figure but return the filename.
    offset : float, optional (default: 20)
          position the 2D contour plot by offset along the Z direction
          under the minimum Z value
    zlabel : string, optional
          label for the Z axis and color scale bar
    elevation : float, optional
          choose elevation for initial viewpoint
    azimuth : float, optional
          chooze azimuth angle for initial viewpoint
    rstride, cstride : int, optional
          strides for the wireframe/surface plots
    """

    x = np.arange(Phi.shape[0])
    y = np.arange(Phi.shape[1])
    X, Y = np.meshgrid(x, y)
    Z = Phi[X, Y]

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    surf = ax.plot_surface(X, Y, Z, cmap=plt.cm.coolwarm,
                           rstride=rstride, cstride=cstride,
                           alpha=0.3)
    cset = ax.contourf(X, Y, Z, 20, zdir='z', offset=offset+Z.min(), cmap=plt.cm.coolwarm)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel(zlabel)
    ax.set_zlim(offset + Z.min(), Z.max())

    ax.view_init(elev=elevation, azim=azimuth)

    cb = fig.colorbar(surf, shrink=0.5, aspect=5)
    cb.set_label(zlabel)

    if filename:
        fig.savefig(filename)
        plt.close(fig)
        return filename
    else:
        return ax


def plot_chargedensity(rho, filename=None, **kwargs):
    """Plot the charge density rho.

    Arguments
    ---------
    rho : array
          charge density
    filename : string or None, optional (default: None)
          If `None` then show the figure and return the axes object.
          If a string is given (like "contour.png") it will only plot
          to the filename and close the figure but return the filename.
    vmin, vmax : float, optional
          lowest and highest charge density value to be shown
          in the color scale
    """
    fig = plt.figure()
    ax = fig.add_subplot(111)
    img = ax.imshow(rho.T, origin="lower",
                    cmap=plt.cm.coolwarm, interpolation="nearest",
                    **kwargs)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    cb = fig.colorbar(img, extend="both", extendrect=False)
    cb.set_label(r"charge density $\rho$")

    if filename:
        fig.savefig(filename)
        plt.close(fig)
        return filename
    else:
        return ax

