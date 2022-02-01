import numpy as np
from scipy.integrate import odeint

# Plotting modules
import matplotlib.pyplot as plt
import pandas as pd

# for the 3D plot
from mpl_toolkits import mplot3d

# define the initial system state (aka x, y, z positions in space)
initial_state = np.array([1, 1, 1])

# define the system parameters sigma, rho, and beta
sigma = 16.0
rho = 45.92
beta = 4.0

args = (sigma, rho, beta)

t = np.arange(0, 20, 0.01)

def solveODESystem(current_state, t, sigma, rho, beta):
    """simple Lorenz system"""

    x, y, z = current_state

    dx_dt = sigma * (y - x)
    dy_dt = x * (rho - z) - y
    dz_dt = x * y - beta * z

    return np.array([dx_dt, dy_dt, dz_dt])


trajectorieValue = pd.DataFrame(odeint(solveODESystem, initial_state, t, args=(sigma, rho, beta)), columns=['x','y','z'])

fig = plt.figure(figsize=(5,5))
ax = plt.axes(projection='3d')

# plot the trajectorie line
x,y,z = trajectorieValue['x'], trajectorieValue['z'],trajectorieValue['z']
lines = ax.plot(x, y, z, '-', c='red')
plt.setp(lines, linewidth=1)

# rotate the plot
ax.view_init(0, 90)

plt.show()