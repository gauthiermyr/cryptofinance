# a: blocks minés en avance par l'attaquant
# h: blocks minés en avance par la banque
# n: nombre d'actions restantes 
# q: seuil minimal

import functools

a = 0
h = 0
n = 400
@functools.cache
def E (a, h, n, q, c): 
    if n == 0:
        return 0

    if a > h:
        return max(((h+1) - c + E(a-h-1, 0, n-1, q, c)),
                    (q * E(a+1, h, n-1, q, c) + (1-q) * (E(a, h+1, n-1, q, c) - c)))

    if a <= h:
        return max(E(0, 0, n-1, q, c),
                    (q * E(a+1, h, n-1, q, c) + (1-q) * (E(a, h +1, n-1, q, c) - c)))


q = 0.3293929 # seuil minimal
print(E(a, h, n, q, q))