"""script for the simulation of a 3 nodes Boolean Network"""

__author__ = "Jan Piotraschke"

import itertools

import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

# possible states
states_number = 3

# Boolean Logic
A_table = [1, 0]
B_table = [1, 1, 1, 0]
C_table = [1, 0, 0, 0]

# possible start values
X_combi = list(itertools.product([1, 0], repeat=states_number))
for X in X_combi:
    A_t, B_t, C_t = X

    # next steps according to the logic
    A_ix = A_t
    B_ix = 2*A_t + B_t
    C_ix = B_ix
    A_new = A_table[A_ix]
    B_new = B_table[B_ix]
    C_new = C_table[C_ix]

    # add the next states to the graph
    G.add_edge((A_t, B_t, C_t),(A_new, B_new, C_new))

nx.draw_networkx(G)

ax = plt.gca()
ax.margins(0.20)
plt.axis("off")
plt.show()