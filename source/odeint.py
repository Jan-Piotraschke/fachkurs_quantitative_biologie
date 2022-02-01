from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt


def simulateODE(x,t):
    """ simple ODE

    :param x:
    :param t:
    :return:
    """
    c = 1
    k = 2

    dx_dt = c - k*x

    return dx_dt

T = np.arange(0, 10, 0.1)
initial_conditions_list = list(range(10))
for X_0 in initial_conditions_list:
    X = odeint(simulateODE, X_0, T)
    plt.plot(T, X, linewidth=2)
plt.show()