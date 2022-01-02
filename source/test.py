import matplotlib.pyplot as plt
import numpy as np
import scipy

P=np.linspace(0,10,10000)
exp2 = np.exp(2)

X = []
Y = []
for u in P:
    # Add one value to X instead of resetting it.
    X.append(u)
    # Start with a random value of m instead of remaining stuck
    # on a particular branch of the diagram
    m = np.random.random()
    for l in range(1051):
        m=(u*m*np.exp(-m))
    # Collection of data in Y must be done once per value of u
    Y.append(m)

plt.figure(figsize=(8,4))

ax = plt.axes()
ax.set_xlabel('parameter a')
ax.set_ylabel('fixed points')

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.legend()
ax.yaxis.grid(alpha=0.4)

plt.plot(X, Y, ls='', marker=',')
plt.xlim(0, 10)
#plt.vlines(exp2,0,10, alpha=0.5)
plt.xticks(list(plt.xticks()[0]) + [1,exp2])

#plt.savefig('bifurcation.png', dpi=720, bbox_inches='tight')

plt.show()