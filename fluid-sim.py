# Test push for 2D Fluid Simulation.
# Test graph visulisation in VS. 

from math import radians
import numpy as np     # installed with matplotlib
import matplotlib.pyplot as plt
import sys

def main():

    x = np.arange(0, radians(1800), radians(12))
    plt.plot(x, np.cos(x), 'b')
    plt.show()

main()

