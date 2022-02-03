import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def simulateSimpleGlycolysis(S,t, param):

    # define metabolites
    G, TP, P, ATP = S

    # parameter
    Gx = param
    A_total = 2
    ADP = A_total - ATP

    k0 = 2
    k1 = 2
    k2 = 1.5
    k3 = 3
    k4 = 0.5
    Vm5 = 2
    Km5 = 1

    if t>30:
        Vm5 = 2.5

    # rate equations
    v0 = k0*(Gx -G)
    v1 = k1*G*ATP
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

Gx_list = np.arange(0,4,0.05)
S_final = np.zeros([len(Gx_list), 4])

time = np.arange(0, 10, 0.1)
S0 = np.random.rand(4) #[1, 1, 1, 1]
for idx, Gx in enumerate(Gx_list):
    solution = odeint(simulateSimpleGlycolysis, S0, time, args=(Gx,))
    S_final[idx, :] = solution[-1,:]

plt.plot(Gx_list, S_final, "o-")
plt.xlabel("external glucose concentration")
plt.ylabel("internal concentrations S")
plt.show()
