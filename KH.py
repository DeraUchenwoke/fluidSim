def getConserved (rho, vx, vy, P, gamma, vol):

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

    """
      Mass     is matrix of mass in cells
      Momx     is matrix of x-momentum in cells
      Momy     is matrix of y-momentum in cells
      Energy   is matrix of energy in cells
      gamma    is ideal gas gamma
      vol      is cell volume
      rho      is matrix of cell densities
      vx       is matrix of cell x-velocity
      vy       is matrix of cell y-velocity
      P        is matrix of cell pressures
    """

    rho = Mass / vol
    vx = Momx / (rho * vol)
    vy = Momy / (rho * vol)
    P = (Energy/vol - 0.5 * rho * (vx**(2) + vy**(2)) * (gamma - 1))

    return rho, vx, vy, P






