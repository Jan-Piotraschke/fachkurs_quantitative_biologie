import numpy as np
import pandas as pd
from scipy.integrate import odeint
import matplotlib.pyplot as plt


def function_A(A):
    K_i = 1
    n = 4

    return (1+(A/K_i)**n)**(-1)


def simulateWolfGlycolysis(S, t):
    S1, S2, S3, S4, S5, S6, S6_ex, A3, N2 = S

    # parameter
    J0 = 50
    k1 = 550
    k2 = 9.8
    k4 = 80
    k5 = 9.7
    k6 = 2000
    k7 = 28
    k8 = 85.7
    k9 = 80
    kappa = 375
    phi = 0.1
    A = 4 # cell surface
    N = 1
    k_GAPDHp = 323.8
    k_GAPDHm = 57823.1
    k_PGKp = 76411.1
    k_PGKm = 23.7

    # algebraic equations
    A2 = A - A3
    N1 = N - N2
    v1 = k1*S1*A3*function_A(A3)
    v2 = k2*S2
    v3 = (k_GAPDHp * k_PGKp * S3 * N1 * (A-A3) - k_GAPDHm * k_PGKm * S4 * A3 * N2)/ (k_GAPDHm * N2 + k_PGKp*(A-A3))
    v4 = k4*S4*(A-A3)
    v5 = k5*S5
    v6 = k6*S6*N2
    v7 = k7*A3
    v8 = k8*S3*N2
    v9 = k9*S6_ex
    J = kappa * (S6 - S6_ex)

    # ODEs
    S1_dt = J0 - v1
    S2_dt = v1 - v2
    S3_dt = 2*v2 - v3 - v8
    S4_dt = v3 - v4
    S5_dt = v4 - v5
    S6_dt = v5 - v6 - J
    S6ex_dt = phi*J - v9
    A3_dt = -2*v1 + v3 + v4 - v7
    N2_dt = v3 - v6 - v8

    return [S1_dt, S2_dt, S3_dt, S4_dt, S5_dt, S6_dt, S6ex_dt, A3_dt, N2_dt]

time = np.arange(0, 0.5, 0.01)
# S0 = [1.09, 5.1, 0.55, 0.66, 8.31, 0.08, 0.02, 2.19, 0.41]
# from data.iloc[[-1]].values.round(2).tolist()
# for the plot of the paper: [0.45, 5.57, 0.6, 0.49, 8.56, 0.07, 0.02, 2.05, 0.46]
S0 = [0.45, 5.57, 0.6, 0.49, 8.56, 0.07, 0.02, 2.05, 0.46]
data = pd.DataFrame(odeint(simulateWolfGlycolysis, S0, time),
                    columns=['S1','S2','S3', "S4", "S5", "S6", "S6ex", "A3", "N2"],
                    index=time)
data[["N2",'A3']].plot()
plt.show()
