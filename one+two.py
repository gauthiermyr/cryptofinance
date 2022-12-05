import random
import matplotlib.pyplot as plt

# inputs: cycles d'attaques n
# q: hasrate

# output: rendement: (G1 + Gn) / (H1 + Hn)

n = 1000
q = 0.01 
Q = []
R = []
T = []
for _ in range(100):
    G = 0
    H = 0

    for i in range(n):

        round = []

        for _ in range(3):
            round.append(random.random() <= q)

            if not round[0]:
                break

        mined = sum(round)
        if mined < 2: 
            g = 0
        else:
            g = mined
            h = 3

        if len(round) == 1:
            h = 1
        elif mined < 3:
            h = 2

        G += g
        H += h

    r = G/H
    t = (q**2*(4 - q)) / (1 + q + q**3)
    R.append(r)
    Q.append(q)
    T.append(t)
    q += 0.01

fig, ax = plt.subplots()
ax.plot(R, Q)
fig2, ax2 = plt.subplots()
ax2.plot(T, Q)

ax.set(xlabel='q', ylabel='R')
ax2.set(xlabel='q', ylabel='Rt')
ax.grid()
ax2.grid()
plt.show()

