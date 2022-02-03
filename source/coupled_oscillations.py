import numpy as np
import pandas as pd
from scipy.integrate import odeint
import matplotlib.pyplot as plt


def simulateTwoBier(S, t, param):
    G1, T1, G2, T2 = S

    epsi = param

    V_in = 0.36
    k1 = 0.02
    kp = 6
    Km = 13

    # algebraic equations
    v1 = V_in
    v2 = k1*G1*T1
    v3 = kp*T1/(Km+T1)
    v4 = k1*G2*T2
    v5 = kp*T2/(Km+T2)

    G1_dt = v1 - v2
    T1_dt = 2 * v2 - v3 + epsi*(T2-T1)
    G2_dt = v1 - v4
    T2_dt = 2 * v4 - v5 - epsi*(T2-T1)

    return [G1_dt, T1_dt, G2_dt, T2_dt]


time = np.arange(0, 1000, 0.5)
S0 = [1, 1, 10, 10]
epsilon_list = np.arange(0,0.1,0.01)
S_final = np.zeros([len(epsilon_list), 4])

for idx, epsilon in enumerate(epsilon_list):
    solution = odeint(simulateTwoBier, S0, time, args=(epsilon,))
    S_final[idx, :] = solution[-1,:]

data = pd.DataFrame(S_final, columns=["G1", "T1", "G2", "T2"], index=epsilon_list)
data["difference"] = data["G1"] - data["G2"]
data["difference"].plot()
#plt.plot(epsilon_list, S_final, "o-")
#solution = odeint(simulateTwoBier, S0, time)
#plt.plot(time, solution)
#plt.legend(["G", "T"])
#plt.xlabel("coupling constant epsilon")
#plt.ylabel("concentrations S")

plt.show()