import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def solveLinearChain(S, t):

    S1, S2, S3 = S

    influx = 1

    # different flux after 10s
    if t > 10:
        influx = 0.5

    Km1, Km2, Km3 = 1, 1, 1
    Vm1 = 2
    Vm2 = 3
    Vm3 = 4

    v0 = influx
    v1 = Vm1*S1/(Km1+S1)
    v2 = Vm2*S2/(Km2+S2)
    v3 = Vm3*S3/(Km3+S3)

    S1_dt = v0 - v1
    S2_dt = v1 - v2
    S3_dt = v2 - v3

    return [S1_dt, S2_dt, S3_dt]

time = np.arange(0, 20, 0.01)
S0 = [1, 2, 2]

solution = odeint(solveLinearChain, S0, time)
plt.plot(time, solution)
plt.legend(["S1", "S2", "S3"])
plt.xlabel("time t")
plt.ylabel("concentrations S")
plt.show()
