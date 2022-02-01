"""script for a minimal cellular automata"""

__author__ = "Jan Piotraschke"

import numpy as np
import matplotlib.pyplot as plt


def simulateCellAutoSimpler(N=100, K=150):
    """code for the Sierpiński Triangle"""

    RULES = np.array([0, 1, 1, 1, 1, 1, 1, 0])

    X = np.zeros((K,N), dtype=int)
    X[0, int(np.floor(N/2))] = 1

    for i in range(K-1):
        # set the boundaries
        X_idx = np.concatenate(([X[i, N-1]], X[i,:], [X[i,0]]))

        index = X_idx[:N]*4 + 2*X_idx[1:N+1] + X_idx[2:N+2]

        X[i+1,:] = RULES[index]

    return X


X = simulateCellAutoSimpler(250, 150)

plt.spy(X)
plt.show()
# plt.savefig('../img/cellular_automata.png', dpi=720, bbox_inches='tight')
