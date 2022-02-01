"""simple example of the Euler Method"""

__author__ = "Jan Piotraschke"

import numpy as np
import matplotlib.pyplot as plt

def simulateSimpleEuler(x0, T, N):
    """

    :param x0: initial conditions
    :param T: stop of the iteration
    :param N: number of iteration steps
    :return:
    """
    k: float = 1.0

    dt = float(T)/N
    time_span = np.arange(0, T, dt)
    x = [float(x0)]

    # integration
    for i in range(1,N):
        x.append(x[i-1]+dt*(-k*x[i-1]))
    #plt.plot(time_span, x, 'bo', markersize=2, label="Euler method")
    #plt.plot(time_span, x0*np.exp(-k*time_span), 'r-', label="analytical solution")
    #plt.xlabel("time t")
    #plt.ylabel("x(t)")
    #plt.legend(loc="upper right")
    #plt.show()
    x_analytical = x0*np.exp(-k*time_span[-1])
    x = x[N-1]

    return x_analytical - x

data_list = []
N_list = np.arange(10,55,5)
for N in N_list:
    data_list.append(simulateSimpleEuler(1, 1, N))

plt.plot(1/N_list, data_list, 'o')
plt.xlabel("inverse number of steps 1/N")
plt.ylabel("estimated Error for x(1) with Euler method")
plt.show()
