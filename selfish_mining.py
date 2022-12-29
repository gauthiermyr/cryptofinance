import random
import matplotlib.pyplot as plt

q = 0.01 # S hashrate
# p = 1 - q # honest miners hashrate
n = 1000  # amount of cycle to do

Q = []
R = []

# strategy
for i in range(49):
    G = 0
    H = 0
    for j in range(n):
        g = 0
        h = 1
        if (random.random() <= q): # S mines first else end of the cycle
            if (random.random() > q): # S is firrst to validate a block but then H mines one block before S
                g = 1 # S broadcast the secret block
                # end of the cycle
            else: # S mines two in a row
                h = 2
                fork = 2
                legacy = 0
                while fork - legacy > 1: # while S advances > 1 : mine
                    if (random.random() <= q): # S mines
                        fork += 1
                    else: # H mines
                        legacy += 1
                    h += 1
                # S lost the advance
                g = fork # broadcast the fork

        G += g
        H += h

    r = G/H
    R.append(r)
    Q.append(q)
    q += 0.01

fig, ax = plt.subplots()
ax.plot(Q, R)
ax.set(xlabel='q', ylabel='R')
ax.set_title("Simulation selfish mining")
ax.grid()
plt.show()