import numpy as np
import pandas as pd
from scipy.integrate import odeint
import matplotlib.pyplot as plt


def simulateBierModel(S, t):

    G, T = S

    V_in = 0.36
    k1 = 0.02
    kp = 6
    Km = 13

    # algebraic equations
    v1 = V_in
    v2 = k1*G*T
    v3 = kp*T/(Km+T)

    G_dt = v1 - v2
    T_dt = 2*v2 - v3

    return [G_dt, T_dt]

time = np.arange(0, 500, 0.5)
S0 = [1, 1]

solution = odeint(simulateBierModel, S0, time)
#plt.plot(time, solution)
#plt.legend(["G", "T"])
#plt.xlabel("time t")
#plt.ylabel("concentrations S")

plt.plot(solution[:, 0], solution[:, 1])
plt.xlabel("glucose G")
plt.ylabel("ATP T")
plt.show()