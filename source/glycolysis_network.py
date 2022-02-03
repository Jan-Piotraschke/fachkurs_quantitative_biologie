import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def simulateSimpleGlycolysis(S,t):

    # define metabolites
    G, TP, P, ATP = S

    # parameter
    A_total = 2
    ADP = A_total - ATP
    Gx = 1

    k0 = 2
    k1 = 2
    k2 = 1.5
    k3 = 3
    k4 = 0.5
    Vm5 = 2
    Km5 = 1
    kATP = 5
    KI = 0.1
    n = 4

    if t>30:
        Vm5 = 2.5

    fATP = kATP/(1+(ATP/KI)**n)
    # rate equations
    v0 = k0*(Gx -G)
    v1 = fATP*k1*G*ATP
    v2 = k2*TP*ADP
    v3 = k3*P
    v4 = k4*TP
    v5 = Vm5*ATP/(Km5+ATP)

    # stoichiometry
    G_dt = v0 - v1
    TP_dt = 2*v1 - v2 - v4
    P_dt = v2 - v3
    ATP_dt = -2*v1 + 2*v2 - v5

    return [G_dt, TP_dt, P_dt, ATP_dt]

time = np.arange(0, 50, 0.1)
S0 = [1, 1, 1, 1.8]

solution = odeint(simulateSimpleGlycolysis, S0, time)
plt.plot(time, solution)
plt.legend(["G", "TP", "P", "ATP"])
plt.xlabel("time t")
plt.ylabel("concentrations S")
plt.show()
