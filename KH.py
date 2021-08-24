import matplotlib.pyplot as plt 
import numpy as np

def getConservative (rho, vx, vy, P, gamma, vol):
    """
      rho      is matrix of cell densities
      vx       is matrix of cell x-velocity
      vy       is matrix of cell y-velocity
      P        is matrix of cell pressures
      gamma    is ideal gas gamma
      vol      is cell volume
      Mass     is matrix of mass in cells
      Momx     is matrix of x-momentum in cells
      Momy     is matrix of y-momentum in cells
      Energy   is matrix of energy in cells
    """
    Mass = rho * vol
    Momx = Mass * vx 
    Momy = Mass * vy 
    ue = P/(gamma - 1) # Internal energy density
    ke = ((vx**(2) + vy**(2))/2) * (rho) # Kinetic energy density 
    Energy = (ue + ke) * vol # Total energy 
    
    return Mass, Momx, Momy, Energy

def getPrimitive (Mass, Momx, Momy, Energy, gamma, vol):

    rho = Mass / vol
    vx = Momx / (rho * vol)
    vy = Momy / (rho * vol)
    P = (Energy/vol - 0.5 * rho * (vx**(2) + vy**(2)) * (gamma - 1))

    return rho, vx, vy, P

def getGradident (f, dx):

    """
      f        is a matrix of the field
      dx       is the cell size
      f_dx     is a matrix of derivative of f in the x-direction
      f_dy     is a matrix of derivative of f in the y-direction
    """

    # directions for np.roll()

    R = -1 # right
    L = 1 # left 

    f_dx = (np.roll(f, R, axis = 0) - np.roll(f, L, axis = 0)) / (2 * dx)
    f_dy = (np.roll(f, R, axis = 1) - np.roll(f, L, axis = 1) ) / (2 * dx)

    return f_dx, f_dy









